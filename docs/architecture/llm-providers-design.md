# LLM Provider 추상화 설계 (LLM Providers Design)

> **모든 LLM 호출이 단일 어댑터를 거치며, provider/모델 교체가 코드 변경 없이 config 1줄로 가능한 구조**

**최종 수정**: 2026-05-04
**상태**: 초안 (3+1 합의 대기)
**상위 문서**: `ADR-008-hermes-adoption-decision.md` (차단조건 #4 충족 메커니즘)
**관련 ADR**: ADR-004 (생성 AI 확장성, 동일 패턴), ADR-006 (환경 변수 + Docker)
**관련 메모리**: `feedback_provider_liquidity.md` (영구 기억)

---

## 1. 개요

### 1.1 문제 정의

LLM 도구 도입(Hermes, 외부 LLM 호출 등)이 진행되면 다음 문제가 발생한다:

```
현재 (단일 LLM 의존):
  애플리케이션 → Claude SDK 직접 호출 → Claude 응답
                  ↑
             모델 교체하려면 코드 곳곳을 수정

목표 (Provider Liquidity):
  애플리케이션 → Provider Adapter (단일 인터페이스)
                  ↓
             config 기반 라우팅 → Claude / GPT / Ollama / ...
```

사용자의 비협상 제약은 **"모델/구독 교체가 코드 변경 없이 가능해야 한다"**(`feedback_provider_liquidity.md`). 이 제약을 만족하는 메커니즘이 필요하다.

### 1.2 해결 방안

**ADR-004의 `generative-models.yaml` 패턴을 LLM 도메인에 동일 적용**한다:

1. 단일 config 파일(`llm-providers.yaml`)에 모든 provider/모델 등록
2. **단 하나의 Provider Adapter 인터페이스** — 모든 LLM 호출은 이 인터페이스를 통과
3. 라우팅·폴백·헬스체크는 config 기반 결정적 동작
4. 정적 검사(depcruise) + 런타임 검사로 위반 차단

### 1.3 하네스 위치

```
Layer 0:   CLAUDE.md (가이드 — provider 선택 정책)
Layer 0.5: 본 설계 문서 (가이드 — 어댑터 계약)
Layer 1:   PostToolUse Hook (센서 — 분기 코드 lint)
Layer 1.5: depcruise 정적 검사 (센서 — 위반 패턴 차단)
Layer 5:   3+1 합의 (센서 — 신규 provider 추가 시 검토)
```

---

## 2. 핵심 원칙

| 원칙 | 설명 | 근거 |
|------|------|------|
| **Single Adapter** | 모든 LLM 호출이 통과하는 어댑터 인터페이스는 **정확히 1개**. 분기 금지 | Provider Liquidity 위반 패턴 #2 차단 |
| **Config-Driven** | provider/모델 추가·교체·제거 = `llm-providers.yaml` 편집만. 코드 변경 0 | ADR-004 패턴 일관 적용 |
| **API Key First, OAuth Second** | API 키 경로를 우선. OAuth(구독)는 보조 옵션 | ADR-008 부록 A.1 (Codex ToS 변동성) + R4 (Claude OAuth 버그) |
| **Min 2 Always-On** | 항상 최소 2개 provider가 active. 단일 의존 금지 | ADR-008 차단조건 #5 |
| **Stateless Adapter** | Adapter는 호출 컨텍스트만 받고 상태를 내부에 저장하지 않음 | 락인 회피, 테스트 용이성 |

---

## 3. Provider 레지스트리

### 3.1 단일 설정 파일

```yaml
# llm-providers.yaml (단일 진실 원천)

defaults:
  primary: anthropic-claude-api    # 1순위
  secondary: openai-gpt-api        # 폴백 (Min 2 Always-On)

# 라우팅 우선순위 — 정책별 다른 디폴트 가능
routing:
  consensus_agent_a: anthropic-claude-api    # 3+1 합의 Agent A (Claude)
  consensus_agent_b: openai-gpt-api          # 3+1 합의 Agent B (GPT)
  consensus_agent_c: ollama-llama-local      # 3+1 합의 Agent C (로컬, 비용 0)
  reviewer: anthropic-claude-api              # Reviewer
  background_jobs: ollama-llama-local         # 비용 민감 백그라운드
  default: anthropic-claude-api               # 명시 안 된 경우

providers:
  anthropic-claude-api:
    type: anthropic                # SDK 종류
    model_id: claude-opus-4-7
    auth_method: api_key           # api_key | oauth_subscription
    api_key_env: ANTHROPIC_API_KEY
    endpoint: https://api.anthropic.com
    cost: per_token                # per_token | flat_subscription | free
    cost_estimate: $15/1M_input + $75/1M_output
    status: active                 # active | standby | deprecated | blocked
    health_check: /v1/messages
    notes: "Phase 1 기본 provider"

  anthropic-claude-oauth:
    type: anthropic
    model_id: claude-opus-4-7
    auth_method: oauth_subscription
    oauth_credentials_path: ~/.claude/.credentials.json
    cost: flat_subscription
    cost_estimate: $100/month (Max 5x) + extra credits
    status: standby                 # 기본은 API 키, 필요 시 active 전환
    known_bugs:
      - "Issue #15080 (third-party OAuth billing routing)"
      - "Issue #6475 (extra usage exhaustion)"
      - "Issue #12905 (credential management)"
      - "Issue #10575 (system prompt misclassification)"
    notes: "ADR-008 R4: 사용 시 헬스체크 + 폴백 강제"

  openai-gpt-api:
    type: openai
    model_id: gpt-5.5
    auth_method: api_key
    api_key_env: OPENAI_API_KEY
    endpoint: https://api.openai.com
    cost: per_token
    cost_estimate: $TBD
    status: active

  openai-gpt-oauth:
    type: openai
    model_id: gpt-5.5
    auth_method: oauth_subscription
    oauth_credentials_path: ~/.codex/auth.json
    cost: flat_subscription
    cost_estimate: $200/month (ChatGPT Pro)
    status: standby
    tos_notes: "개인 단일 사용자만. Reselling/aggregation 시 ToS 위반"
    notes: "ADR-008 부록 A.1: 정책 변동 모니터링 필요"

  ollama-llama-local:
    type: ollama
    model_id: llama-3.3-70b
    auth_method: none
    endpoint: http://localhost:11434
    cost: free
    cost_estimate: $0 (로컬 GPU/CPU)
    status: active
    notes: "구독 의존성 0, 응답 시간 ↑"

  openrouter-fallback:
    type: openrouter
    model_id: anthropic/claude-opus-4.7    # OpenRouter 통한 멀티 모델
    auth_method: api_key
    api_key_env: OPENROUTER_API_KEY
    cost: per_token
    status: standby
    notes: "통합 폴백 — 어떤 모델이든 OpenRouter 경유 가능"

# 폴백 체인 — primary 실패 시 순차 시도
fallback:
  default: [anthropic-claude-api, openai-gpt-api, openrouter-fallback, ollama-llama-local]
  consensus_agent_a: [anthropic-claude-api, openrouter-fallback]
  consensus_agent_b: [openai-gpt-api, openrouter-fallback]
  consensus_agent_c: [ollama-llama-local, openrouter-fallback]
```

### 3.2 status 필드 정의

| 값 | 의미 | Adapter 동작 |
|---|------|-------------|
| `active` | 정상 사용 가능 | 라우팅에 포함, 폴백 체인에 포함 |
| `standby` | 등록은 되어 있으나 기본 비활성. 명시 호출 또는 폴백 시에만 사용 | 라우팅 디폴트에서 제외, 폴백 체인에는 포함 |
| `deprecated` | 사용 시 경고 출력. 새 코드에서 사용 금지 | 사용 시 stderr 경고 + 메트릭 기록 |
| `blocked` | 즉시 사용 차단 (장애·보안 이슈 등) | 사용 시 즉시 폴백, 알림 발송 |

### 3.3 cost 필드 정의

| 값 | 의미 | 비용 추적 방식 |
|---|------|---------------|
| `per_token` | 토큰 단위 종량제 | 호출별 토큰 수 × 단가 |
| `flat_subscription` | 월정액 구독 | 사용량만 추적 (한도 도달 모니터링) |
| `free` | 비용 없음 (로컬·자체 호스팅) | 사용량만 (자원 모니터링용) |

---

## 4. Provider Adapter 인터페이스

### 4.1 단일 인터페이스 강제

```python
# adapters/llm_provider.py — 정확히 이 인터페이스만 존재

from typing import Protocol, Iterable
from dataclasses import dataclass

@dataclass(frozen=True)
class LLMRequest:
    messages: list[dict]           # 표준 OpenAI-호환 메시지 형식
    model_alias: str               # 라우팅 alias (예: "consensus_agent_a")
    temperature: float = 0.7
    max_tokens: int = 4096
    tools: list[dict] | None = None
    metadata: dict | None = None   # 호출 메타 (요청 ID 등)

@dataclass(frozen=True)
class LLMResponse:
    content: str
    finish_reason: str
    usage: dict                    # {input_tokens, output_tokens, cost_estimate}
    provider_used: str             # 실제 사용된 provider key (폴백 추적)
    metadata: dict                 # 모델별 raw 메타는 여기로 격리

class LLMProvider(Protocol):
    """모든 LLM 호출은 이 Protocol을 통과한다. 구현체는 1개만 존재."""

    async def complete(self, request: LLMRequest) -> LLMResponse: ...

    async def stream(self, request: LLMRequest) -> Iterable[str]: ...

    async def health(self, provider_key: str) -> bool: ...
```

### 4.2 응답 정규화 (Liquidity 위반 패턴 #6 차단)

provider별 응답 차이는 **Adapter 내부에서 정규화**한다. 다운스트림 코드는 정규화된 형식만 본다.

| 차이 | Adapter 내부 처리 |
|-----|------------------|
| Claude `content` blocks vs GPT `choices[0].message.content` | 모두 `LLMResponse.content` 단일 문자열로 정규화 |
| `stop_reason` vs `finish_reason` 명칭 차이 | `LLMResponse.finish_reason` 단일 명칭 |
| 토큰 카운트 필드명 차이 (`input_tokens` vs `prompt_tokens`) | `LLMResponse.usage` 단일 dict |
| 모델별 raw 메타 (예: Claude `stop_sequence`) | `LLMResponse.metadata`로 격리, 다운스트림 직접 접근 금지 |

### 4.3 에러 분류 (Adapter 내부)

```python
class LLMError(Exception): pass
class AuthError(LLMError): pass         # 401/403 — 즉시 폴백 트리거
class RateLimitError(LLMError): pass    # 429 — 백오프 후 재시도
class ModelUnavailableError(LLMError): pass  # 모델 부재 — 폴백
class ProviderError(LLMError): pass     # 5xx — 백오프 후 폴백
```

**에러도 정규화** — provider 고유 에러 객체는 Adapter 외부로 누출 금지.

### 4.4 호출 흐름

```
caller.code:
  response = await llm.complete(LLMRequest(
      messages=[...],
      model_alias="consensus_agent_a",
  ))

Adapter 내부:
  1. routing[model_alias] → provider_key 결정
  2. provider 상태 확인 (status == active)
  3. provider 어댑터 호출
  4. 실패 시 fallback[model_alias] 순차 시도
  5. 응답 정규화 → LLMResponse
  6. 메트릭 기록 (provider_used, latency, cost)
```

---

## 5. 라우팅 정책

### 5.1 라우팅 우선순위

```
요청 경로:
  ① model_alias 명시 → routing[alias] → provider_key
  ② model_alias가 routing에 없음 → routing[default]
  ③ provider status != active → fallback chain 순차 시도
  ④ 모든 fallback 실패 → LLMError 발생
```

### 5.2 헬스체크

각 provider는 주기적으로 헬스체크 실행 (Phase 2+):

```yaml
health_check:
  interval: 60s
  timeout: 5s
  failure_threshold: 3   # 3회 연속 실패 시 status=blocked 자동 전환
  recovery_threshold: 2  # 2회 연속 성공 시 active 복귀
```

### 5.3 명시적 라우팅 vs 자동 라우팅

```
명시적 (사용자 코드가 alias 지정):
  llm.complete(LLMRequest(model_alias="consensus_agent_b", ...))

자동 (alias 없이 default):
  llm.complete(LLMRequest(messages=[...]))  → routing[default]
```

명시적 라우팅도 **alias** 단위만 허용. 직접 provider key 지정 금지(분기 코드 패턴 #1 회피).

---

## 6. 최소 2 Provider Always-On (ADR-008 차단조건 #5)

### 6.1 정책

`llm-providers.yaml`은 **항상 status=active인 provider가 2개 이상**이어야 한다. 1개 이하면 시스템 시작 시 fail-fast.

```python
# Adapter 초기화 시 검증
def validate_config(config):
    active = [p for p, v in config["providers"].items() if v["status"] == "active"]
    if len(active) < 2:
        raise ConfigError(
            f"최소 2 provider always-on 정책 위반. 현재 active: {active}. "
            f"ADR-008 차단조건 #5 참조."
        )
```

### 6.2 Provider 다양성 권장

active 2개는 가급적 **type이 다른** provider 권장:
- 같은 type (둘 다 `anthropic`) → API 정전 시 동시 실패 가능
- 다른 type (예: `anthropic` + `openai`) → 진정한 폴백

권장 구성 (Phase 1):
```
active: [anthropic-claude-api, ollama-llama-local]
       (Claude API + 로컬 폴백, 구독 만료에도 시스템 동작)
```

### 6.3 구독 취소 시나리오

사용자가 Claude Max를 취소하는 시나리오:
```
Step 1: anthropic-claude-oauth → status=blocked
Step 2: anthropic-claude-api는 API 키 별도 결제이므로 영향 없음
Step 3: 시스템 정상 동작 (active 여전히 2개+)
```

OAuth만 사용 중이었다면 API 키 provider로 즉시 전환:
```
Step 1: anthropic-claude-api로 routing 변경 (config 1줄)
Step 2: API 키 발급/결제
Step 3: 재시작
```

---

## 7. OAuth 직결 금지 정책 (ADR-008 부록 A.1)

### 7.1 우선순위

| 순위 | 인증 방법 | 사용 조건 |
|-----|----------|----------|
| 1 | `api_key` | 기본. 모든 새 코드는 이 방식 우선 |
| 2 | `oauth_subscription` | 비용 절감 시. 단 헬스체크·폴백 강제, 정책 변동 모니터링 |

### 7.2 OAuth 사용 시 필수 조건

OAuth provider를 active로 전환하려면:
1. ✅ 같은 type의 API 키 provider가 **최소 1개 standby** 등록되어 있어야 함 (즉시 폴백 가능)
2. ✅ 헬스체크 활성화 (`health_check.interval` 설정)
3. ✅ 정책 변동 모니터링 task 등록 (월 1회 ToS 검토)
4. ✅ ADR-008 R4 인지 (Claude OAuth 버그 4종)

### 7.3 ChatGPT Pro Codex OAuth 특별 조항

- **개인 단일 사용자만** (third-party 집계 시 ToS 위반)
- 정책 변동 시 즉시 standby 전환
- 변동 모니터링: OpenAI 정책 페이지 + 커뮤니티 사례 (Reddit, GitHub)

---

## 8. 비용·관측성

### 8.1 메트릭 수집

각 호출마다 다음 기록:

```
{
  "request_id": "...",
  "timestamp": "...",
  "model_alias": "consensus_agent_a",
  "provider_used": "anthropic-claude-api",   # 폴백 발생 시 다름
  "fallback_chain": ["anthropic-claude-api"], # 시도된 provider 순서
  "input_tokens": 1234,
  "output_tokens": 567,
  "cost_estimate": 0.0234,
  "latency_ms": 2300,
  "status": "success"   # success | fallback | failure
}
```

### 8.2 의사결정 대시보드

월별 집계로 다음 지표 노출:
- provider별 비용 (구독 취소/유지 결정용)
- provider별 가용성 (failure rate)
- alias별 평균 응답 시간
- fallback 발생 빈도 (안정성 지표)

### 8.3 한도 알림

`flat_subscription` provider:
- 사용량 80% → 경고
- 사용량 100% → 자동 폴백 (active provider 전환)

---

## 9. Liquidity 위반 패턴 차단

### 9.1 위반 패턴 카탈로그 (ADR-008 합의 결과)

| # | 패턴 | 차단 메커니즘 |
|---|------|-------------|
| 1 | 모델명/provider 분기 코드 (`if model == "claude-opus-4-7"`) | depcruise 룰 (별도 P5 문서) + lint |
| 2 | provider별 응답 후처리 함수 분리 | Adapter 응답 정규화 강제 (4.2 항) |
| 3 | 스킬/프롬프트 안 특정 모델 가정 | 코드 리뷰 체크리스트 + 테스트 (다른 모델로도 통과해야 함) |
| 4 | 메모리에 provider별 메타 저장 | `LLMResponse.metadata`만 사용, 그 외 직접 저장 금지 |
| 5 | provider 전용 인증 갱신 로직 | Adapter 내부에 격리, 외부 코드는 인증 모름 |
| 6 | 포맷별 다운스트림 파서 | Adapter 응답 정규화 강제 |

### 9.2 정적 검사 (depcruise — P5 문서로 상세화)

```javascript
// .depcruise.cjs (개략, 상세는 P5)
{
  forbidden: [
    {
      name: "no-direct-llm-sdk-import",
      from: { pathNot: "^src/adapters/llm/" },
      to: { path: "^(anthropic|openai|@anthropic-ai|@openai)" }
    },
    {
      name: "no-provider-name-branching",
      // grep 기반 보조 검사: src/ 안에서 'claude-opus' 등 모델명 문자열 금지
    }
  ]
}
```

### 9.3 런타임 검사

Adapter 초기화 시:
- 응답 정규화 확인 (raw 응답이 외부로 새지 않음)
- active provider ≥ 2 검증 (6.1)
- routing alias 무결성 (모든 alias가 유효한 provider key 가리키는지)

### 9.4 코드 리뷰 체크리스트

PR 검토 시 확인:
- [ ] LLM 호출이 모두 Adapter를 거치는가?
- [ ] 모델/provider 이름이 코드에 하드코딩되지 않았는가?
- [ ] 응답 처리가 `LLMResponse` 표준 필드만 사용하는가?
- [ ] 새 provider 추가 시 `llm-providers.yaml`만 수정했는가? (Adapter 코드 수정은 신중)

---

## 10. 마이그레이션 경로

### 10.1 Provider 추가

```
새 모델 "Llama 4 70B" 추가:

Step 1: llm-providers.yaml에 항목 추가
  ollama-llama4-local:
    type: ollama
    model_id: llama-4-70b
    ...
    status: standby   # 처음엔 standby

Step 2: 검증 (테스트로 호출 동작 확인)

Step 3: status: active 또는 routing의 특정 alias에 할당

Step 4: 끝. 코드 변경 없음.
```

### 10.2 Provider 제거

```
"openai-gpt-oauth" 제거 (정책 변동 등):

Step 1: status: blocked로 전환 (즉시 모든 호출 차단)
Step 2: 의존하던 routing alias가 있는지 확인
        → 있으면 routing 재할당 (다른 active provider로)
Step 3: 1주 모니터링 (사용 흔적 없는지)
Step 4: yaml에서 항목 삭제
```

### 10.3 모델 변경

```
Claude Opus 4.7 → Claude Opus 5.0 출시:

Step 1: llm-providers.yaml의 model_id 수정
  anthropic-claude-api:
    model_id: claude-opus-5-0   # 변경

Step 2: 끝. 코드 변경 없음.
```

### 10.4 응급 폴백 (active provider 전체 장애)

```
Anthropic API 정전 + OpenAI 동시 장애:

자동:
  Adapter가 fallback 체인 순차 시도 → ollama-llama-local로 도달
  → degraded mode (응답 시간 ↑, 일부 능력 ↓)

수동:
  llm-providers.yaml에서 standby provider를 active로 임시 전환
  (예: openrouter-fallback)
```

---

## 11. 적용 시나리오

### 11.1 Hermes Phase 1 (1~2주)

```
설정:
  active: [anthropic-claude-api, openai-gpt-api]
  routing.default: anthropic-claude-api
  routing.background_jobs: openai-gpt-api

목적: API 키만 사용. OAuth 직결 금지 정책 검증.
검증: 비핵심 작업(문서 요약 등)을 Hermes로 수행, Adapter 정상 동작 확인.
```

### 11.2 Hermes Phase 2 (2~4주) — 3+1 합의 다중 모델

```
설정:
  active: [anthropic-claude-api, openai-gpt-api, ollama-llama-local]
  routing:
    consensus_agent_a: anthropic-claude-api
    consensus_agent_b: openai-gpt-api
    consensus_agent_c: ollama-llama-local
    reviewer: anthropic-claude-api

목적: 3+1 합의의 메타 한계(전 에이전트 Claude 기반) 해소.
검증: 3+1 합의를 다중 모델로 실행, 결과 품질 ≥ 단일 Claude 합의.
```

### 11.3 Claude Max 구독 취소 시나리오

```
사용자 결정: Claude Max 비용 부담 → 취소 결정.

작업:
  Step 1: llm-providers.yaml
    anthropic-claude-oauth:
      status: blocked   # 또는 항목 삭제

  Step 2: routing 확인 — Claude Max OAuth를 사용하던 alias가 있는가?
    → 있으면 anthropic-claude-api로 재할당

  Step 3: API 키 결제로 전환 (또는 Claude 자체를 빼고 GPT만 사용)

영향: 코드 변경 0. 시스템 정상 동작.
```

### 11.4 새 provider 추가 (Gemini 2.5)

```
Step 1: llm-providers.yaml에 추가
  google-gemini-api:
    type: google_genai
    model_id: gemini-2.5-pro
    auth_method: api_key
    api_key_env: GOOGLE_API_KEY
    status: standby

Step 2: Adapter에 google_genai type 핸들러 추가 (Adapter 내부 변경)
        — 단 외부 인터페이스(LLMRequest/Response)는 동일
        — depcruise 룰: 외부 코드의 google sdk 직접 import는 여전히 금지

Step 3: 테스트 → status: active

Step 4: 필요 시 routing alias 재할당
```

> 신규 provider type 추가는 Adapter 내부 구현 변경이 필요한 유일한 경우. 단, **외부 인터페이스는 불변** → 다운스트림 코드는 영향 없음.

---

## 12. ADR-008 차단조건 매핑

| 차단조건 | 본 설계의 충족 메커니즘 |
|---------|----------------------|
| #1 SQLCipher 암호화 | 본 문서 범위 외 (Hermes 도입 설계 P2에서 다룸) |
| #2 JSONL export | 본 문서 범위 외 (P2) |
| #3 v0.x 버전 핀 | 본 문서 범위 외 (P2) |
| **#4 provider 어댑터 1개 추상화 + 분기 금지** | **본 설계 전체** (§4 Adapter, §9 위반 차단) |
| **#5 최소 2 provider always-on** | **§6 정책 + 시작 시 fail-fast 검증** |
| #6 Docker 격리 | 본 문서 범위 외 (P2) |

---

## 13. 다른 ADR과의 정합성

| 관련 문서 | 정합성 |
|---------|--------|
| **ADR-004** (생성 AI 확장성) | 동일 패턴 적용. `<도메인>-<resource>.yaml` 단일 config + status/fallback 구조 일관 |
| **ADR-006** (환경 변수 + Docker) | API 키는 환경 변수, OAuth credentials는 mounted volume. 하드코딩 0 원칙 준수 |
| **ADR-005** (AI 백엔드 스택) | Python 분리 기준 따름. Adapter는 Python 또는 호출 환경에 맞춰 |
| **PROJECT_CONSTITUTION 제8조** | API 키는 환경 변수, 응답·메타에 비밀값 echo 없음 (감사 가능) |
| **harness-engineering-design** | Layer 1 hook으로 분기 코드 검출, Layer 5 합의로 신규 provider 검토 |

---

## 14. Phase 로드맵

| Phase | 내용 | 상태 | 진입 조건 |
|-------|------|------|----------|
| **MVP** | `llm-providers.yaml` + Adapter 인터페이스 + 정적 검사 (depcruise) + active 2 검증 | 구현 대상 | 본 설계 3+1 합의 완료 |
| **v1.1** | 헬스체크 + 자동 폴백 + 메트릭 수집 | 필요 입증 후 | MVP 운영 1주 + 폴백 시나리오 발생 |
| **v1.2** | 한도 알림 + 의사결정 대시보드 | 필요 입증 후 | flat_subscription 한도 도달 사례 |
| **v2.0** | LiteLLM 통합 검토 (자체 Adapter → 표준 라이브러리 전환) | 필요 입증 후 | 자체 Adapter 유지 비용 ≥ 통합 비용일 때 |

> v2.0 검토는 Agent C(대안 탐색가)가 권장한 LiteLLM 옵션을 정식 진입점으로 보존. 자체 Adapter가 충분히 작동하면 유지, 유지 부담이 커지면 LiteLLM으로 전환.

---

## 15. Phase 2 검토 사항 (현재 미구현)

다음 항목은 MVP에서 제외하고, 추후 필요성 검증 후 도입한다.

| 항목 | 도입 조건 |
|------|----------|
| 추론 캐시 레이어 | 동일 요청 반복 비율 ≥ 20% |
| Provider별 prompt 최적화 | 모델 간 결과 품질 편차 측정 후 |
| 자동 모델 추천 (성능/비용 학습 기반) | 의사결정 대시보드 데이터 누적 후 |
| Streaming 응답 표준화 | streaming 사용 사례 발생 시 |
| Multi-modal (이미지/오디오) 통합 | 별도 도메인. ADR-003·004 참조 |

---

## 16. 검증 항목 (3+1 합의용)

다음 항목을 3+1 에이전트가 검증하길 권장:

### Agent A (구현 분석가)
- Adapter 인터페이스가 Anthropic/OpenAI/Ollama/OpenRouter 모두 수용 가능한가?
- 폴백 체인의 race condition 가능성?
- depcruise 룰의 완전성 (회피 가능한가)?

### Agent B (품질·안전성)
- 위반 패턴 6종이 실제로 모두 차단되는가?
- OAuth 토큰 누출 가능성?
- "최소 2 active" 검증의 회피 경로?

### Agent C (대안 탐색가)
- LiteLLM을 처음부터 채택하지 않은 이유는 충분한가? (자체 Adapter 유지 비용 vs LiteLLM 통합 비용)
- 본 설계가 ADR-004 패턴을 충실히 따르는가? 차이점이 정당한가?

### Reviewer
- ADR-008 차단조건 #4·#5 충족 여부 최종 판정
- Provider Liquidity 위반 가능성 잔존 여부

---

**이 문서는 3+1 에이전트 합의 검증을 통과해야 확정됩니다.**
