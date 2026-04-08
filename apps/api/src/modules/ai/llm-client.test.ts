import { describe, expect, it } from 'vitest';
import { ChatAnthropic } from '@langchain/anthropic';

import { LlmClient } from './llm-client';

/**
 * LlmClient 단위 테스트.
 *
 * 외부 LLM/Langfuse 서버는 호출하지 않는다. 검증 대상은:
 *  - provider/api key/model 조립이 의도대로 이루어지는가
 *  - Langfuse key 부재 시 callback이 빈 배열이고 isLangfuseEnabled()=false
 *  - Langfuse key가 있으면 callback이 1개 부착되고 isLangfuseEnabled()=true
 *  - 미지원 provider는 명확한 오류를 던지는가 (ADR-009 §강제 사항 1번)
 */

class FakeConfig {
  constructor(private readonly map: Record<string, string | undefined>) {}

  get<T = string>(key: string): T {
    return this.map[key] as unknown as T;
  }
}

function makeClient(env: Record<string, string | undefined>): LlmClient {
  const config = new FakeConfig(env);
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  return new LlmClient(config as any);
}

describe('LlmClient', () => {
  describe('provider 분기', () => {
    it("LLM_PROVIDER='anthropic'이면 ChatAnthropic 인스턴스를 사용한다", () => {
      const client = makeClient({
        LLM_PROVIDER: 'anthropic',
        LLM_API_KEY: 'sk-test',
        LLM_MODEL: 'claude-opus-4-6',
      });

      expect(client.getModel()).toBeInstanceOf(ChatAnthropic);
    });

    it('미지원 provider는 명확한 에러를 throw 한다', () => {
      expect(() =>
        makeClient({
          LLM_PROVIDER: 'cohere',
          LLM_API_KEY: 'sk-test',
          LLM_MODEL: 'whatever',
        }),
      ).toThrow(/cohere/);
    });

    it('LLM_PROVIDER 미설정 시 anthropic으로 기본값 처리한다', () => {
      const client = makeClient({
        LLM_API_KEY: 'sk-test',
        LLM_MODEL: 'claude-opus-4-6',
      });

      expect(client.getModel()).toBeInstanceOf(ChatAnthropic);
    });
  });

  describe('Langfuse callback', () => {
    it('LANGFUSE_PUBLIC_KEY/SECRET_KEY가 모두 비어있으면 callbacks가 빈 배열이다 (NoOp)', () => {
      const client = makeClient({
        LLM_PROVIDER: 'anthropic',
        LLM_API_KEY: 'sk-test',
        LLM_MODEL: 'claude-opus-4-6',
        // LANGFUSE_* 의도적 누락
      });

      expect(client.isLangfuseEnabled()).toBe(false);
      expect(Array.isArray(client.getCallbacks())).toBe(true);
      expect((client.getCallbacks() as unknown[]).length).toBe(0);
    });

    it('두 키 중 하나만 있으면 NoOp으로 동작한다 (부분 설정 거부)', () => {
      const client = makeClient({
        LLM_PROVIDER: 'anthropic',
        LLM_API_KEY: 'sk-test',
        LLM_MODEL: 'claude-opus-4-6',
        LANGFUSE_PUBLIC_KEY: 'pk-test',
        // SECRET 누락
      });

      expect(client.isLangfuseEnabled()).toBe(false);
      expect((client.getCallbacks() as unknown[]).length).toBe(0);
    });

    it('두 키가 모두 있으면 CallbackHandler 1개를 callbacks에 부착한다', () => {
      const client = makeClient({
        LLM_PROVIDER: 'anthropic',
        LLM_API_KEY: 'sk-test',
        LLM_MODEL: 'claude-opus-4-6',
        LANGFUSE_PUBLIC_KEY: 'pk-test',
        LANGFUSE_SECRET_KEY: 'sk-langfuse-test',
        LANGFUSE_HOST: 'https://cloud.langfuse.com',
      });

      expect(client.isLangfuseEnabled()).toBe(true);
      const cbs = client.getCallbacks() as unknown[];
      expect(cbs).toHaveLength(1);
      // CallbackHandler는 BaseCallbackHandler를 상속하므로 객체 + name 속성을 가짐
      expect(typeof cbs[0]).toBe('object');
    });
  });
});
