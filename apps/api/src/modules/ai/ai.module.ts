import { Module } from '@nestjs/common';

import { LlmClient } from './llm-client';

/**
 * AI 모듈 (ADR-009).
 *
 * LangChain Chat Model + Langfuse callback을 캡슐화한 LlmClient를 제공한다.
 * 다른 모듈은 이 모듈을 import하고 LlmClient를 inject하여 사용한다.
 *
 * 다음 PR에서 BullMQ Queue + Processor + AiQuestionGenerator를 이 모듈에
 * 추가할 예정.
 */
@Module({
  providers: [LlmClient],
  exports: [LlmClient],
})
export class AiModule {}
