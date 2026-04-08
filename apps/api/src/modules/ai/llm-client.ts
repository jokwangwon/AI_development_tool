import { Injectable, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { ChatAnthropic } from '@langchain/anthropic';
import type { BaseChatModel } from '@langchain/core/language_models/chat_models';
import type { BaseMessage } from '@langchain/core/messages';
import type { Callbacks } from '@langchain/core/callbacks/manager';
import { CallbackHandler } from 'langfuse-langchain';

/**
 * LLM 클라이언트 (ADR-009).
 *
 * 모든 LLM 호출은 이 클라이언트를 통해서만 이루어진다. Anthropic SDK 등
 * 공급자 SDK를 직접 호출하는 코드는 ADR-009 §강제 사항 1번에 의해 거부된다.
 *
 * 책임:
 *  - LangChain Chat Model 인스턴스 보관 (provider별 어댑터)
 *  - Langfuse Callback Handler 관리 (key가 있으면 부착, 없으면 NoOp)
 *  - invoke()를 단일 진입점으로 제공
 *
 * 환경변수:
 *  - LLM_PROVIDER: 'anthropic' (현재) | 'openai' (TODO)
 *  - LLM_API_KEY, LLM_MODEL
 *  - LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST (옵셔널)
 *
 * Langfuse 키가 없으면 trace는 비활성화되고 callback 배열이 비어 있는다.
 * 이는 개발/CI 환경에서 자연스럽게 동작하기 위함이며, 프로덕션에서는
 * 다음 워커 PR에서 LANGFUSE_*를 필수 환경변수로 승격할 예정이다.
 */
@Injectable()
export class LlmClient {
  private readonly logger = new Logger(LlmClient.name);
  private readonly model: BaseChatModel;
  private readonly callbacks: Callbacks;
  private readonly langfuseEnabled: boolean;

  constructor(private readonly config: ConfigService) {
    const provider = this.config.get<string>('LLM_PROVIDER') ?? 'anthropic';
    const apiKey = this.config.get<string>('LLM_API_KEY') ?? '';
    const modelName =
      this.config.get<string>('LLM_MODEL') ?? 'claude-opus-4-6';

    this.model = this.createModel(provider, apiKey, modelName);

    const langfuseHandler = this.createLangfuseHandler();
    this.callbacks = langfuseHandler ? [langfuseHandler] : [];
    this.langfuseEnabled = langfuseHandler !== null;

    this.logger.log(
      `LlmClient ready: provider=${provider}, model=${modelName}, langfuse=${this.langfuseEnabled ? 'enabled' : 'disabled'}`,
    );
  }

  /**
   * 단일 진입점. 모든 LLM 호출은 이 메서드를 통해 이루어지며 자동으로
   * Langfuse callback이 부착된다 (활성화된 경우).
   */
  async invoke(messages: BaseMessage[]): Promise<BaseMessage> {
    return this.model.invoke(messages, { callbacks: this.callbacks });
  }

  /**
   * 테스트 / 진단용. 외부에서 직접 호출하지 말고 invoke()를 사용한다.
   */
  getModel(): BaseChatModel {
    return this.model;
  }

  getCallbacks(): Callbacks {
    return this.callbacks;
  }

  isLangfuseEnabled(): boolean {
    return this.langfuseEnabled;
  }

  private createModel(
    provider: string,
    apiKey: string,
    modelName: string,
  ): BaseChatModel {
    if (provider === 'anthropic') {
      return new ChatAnthropic({
        model: modelName,
        apiKey,
        temperature: 0.7,
        maxTokens: 4096,
      });
    }
    // openai는 LangChain 어댑터(@langchain/openai)가 추가되면 지원
    throw new Error(
      `LLM_PROVIDER='${provider}'는 아직 지원되지 않습니다. 현재는 'anthropic'만 가능 (ADR-009).`,
    );
  }

  private createLangfuseHandler(): CallbackHandler | null {
    const publicKey = this.config.get<string>('LANGFUSE_PUBLIC_KEY');
    const secretKey = this.config.get<string>('LANGFUSE_SECRET_KEY');
    const baseUrl =
      this.config.get<string>('LANGFUSE_HOST') ?? 'https://cloud.langfuse.com';

    if (!publicKey || !secretKey) {
      return null;
    }

    return new CallbackHandler({
      publicKey,
      secretKey,
      baseUrl,
    });
  }
}
