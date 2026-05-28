# LLM Provider 추상화 설계 (LLM Providers Design)

> **모든 LLM 호출이 LiteLLM facade를 거치며, provider/모델 교체가 코드 변경 없이 config 1줄로 가능한 구조**

**최종 수정**: 2026-05-28 (SC-Provider Liquidity 풀 3+1 + 외부 LLM 합의 — §17 재합의 folding, CB-2 staged 조건부 승격)
**상태**: **확정 v2 / Core MVP 구현분리 승인 (staged implementation 허용)** — 2026-05-04 Option β(12 보강 + 4 β-추가) 채택 + 2026-05-28 §17 재합의 통과(`docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md`, 4 source APPROVE WITH CONDITIONS). **Core MVP(`complete()` Router 위임 + Min 2 + 동일 type + redaction + 런타임 강등 감지) = 발효(69 entry, mock-verified)**. **streaming / OAuth single-flight / degraded 모드·R4 자동복구 / metrics callback / 폴백 race 완화 = 12 보강 단계화(deferred phase, 명세 존속 — 본 §15)**. ⚠️ "v1.0 전체 구현 완료" 아님(CB-2 over-claim 차단).
**상위 문서**: `ADR-008-hermes-adoption-decision.md` (차단조건 #4·#5 충족 메커니즘)
**관련 ADR**: ADR-004 (생성 AI 확장성, **외부 SDK 우선 원칙 일치**), ADR-006 (환경 변수 + Docker), ADR-009 (자체 Adapter v2.0 진입조건)
**관련 메모리**: `feedback_provider_liquidity.md` (영구 기억)
**관련 합의**: `review/3plus1-consensus-2026-05-04-p1-llm-providers.md`

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
  애플리케이션 → LLM Facade (단일 인터페이스)
                  ↓
             LiteLLM (40k 스타, 200+ provider 정규화)
                  ↓
             config 기반 라우팅 → Claude / GPT / Ollama / ...
```

사용자의 비협상 제약은 **"모델/구독 교체가 코드 변경 없이 가능해야 한다"**(`feedback_provider_liquidity.md`).

### 1.2 해결 방안 (Option β — LiteLLM facade 승격)

ADR-004 본질("자체 어댑터 불필요 — 외부 SDK 활용") + 3+1 합의 권고에 따라 다음 구조 채택:

1. **LiteLLM SDK가 외부 추상화 계층** — provider별 응답·에러 정규화는 LiteLLM이 자체 제공
2. **얇은 facade (~100 LOC)** — LiteLLM 위에 본 프로젝트 도메인 보강(redaction, single-flight, active 재검증, 도메인 메트릭)
3. **단일 config (`llm-providers.yaml`)** — provider/모델 등록은 ADR-004 패턴 그대로
4. **LiteLLM Router 위임** — 라우팅·폴백·헬스체크·cooldown
5. **정적 검사** — `litellm` 외 LLM SDK 직접 import 금지 1줄 룰

### 1.3 Option β 채택 근거 (요약)

| 비교 | 자체 Adapter (Option α) | LiteLLM facade (Option β, 채택) |
|------|------------------------|--------------------------------|
| 코드 LOC | ~600 + 차단 테스트 ~600 | ~100 facade + 보강 ~150 + 테스트 ~200 |
| 연간 유지 | ~40~80h | ~5~10h |
| 위반 패턴 차단 | 100% 자력 (depcruise 6종) | #1·#2·#5·#6 LiteLLM 자연 차단 |
| ADR-004 정합성 | 본질 위반 | 본질 일치 |
| 외부 종속성 | 없음 | LiteLLM (Apache 2.0) |

### 1.4 하네스 위치

```
Layer 0:   CLAUDE.md (가이드 — provider 선택 정책)
Layer 0.5: 본 설계 문서 (가이드 — facade 계약 + redaction 정책)
Layer 1:   PostToolUse Hook (센서 — SDK 직접 import 검출)
Layer 1.5: depcruise 정적 검사 (센서 — 회피 차단)
Layer 5:   3+1 합의 (센서 — 신규 provider 추가 시 검토)
```

---

## 2. 핵심 원칙

| 원칙 | 설명 | 근거 |
|------|------|------|
| **External SDK First** | LiteLLM이 1차. 자체 코드는 facade 100 LOC + 도메인 보강만 | ADR-004 본질, Reviewer 권고 |
| **Single Facade** | 모든 LLM 호출이 통과하는 facade는 정확히 1개 | ADR-008 차단조건 #4 + 위반 패턴 #2 |
| **Config-Driven** | provider/모델 추가·교체·제거 = `llm-providers.yaml` 편집만 | ADR-004 패턴 일관 |
| **API Key First, OAuth Second** | API 키 경로 우선. OAuth(구독)는 보조 옵션 | ADR-008 부록 A.1 + R4 |
| **Min 2 Always-On (Runtime 재검증)** | 항상 active≥2. 시작 + 모든 강등 경로에서 재검증 | ADR-008 차단조건 #5 (3+1 합의 R4 보강) |
| **Stateless Facade** | facade는 호출 컨텍스트만 받고 상태를 내부에 저장하지 않음. LiteLLM Router 상태는 Router 자체가 관리 | 락인 회피, 테스트 용이성 |
| **Redaction Mandatory** | 모든 응답·예외·메트릭에서 token/key/auth 패턴 자동 strip | ADR-008 R1 + 헌법 제8조 |

---

## 3. Provider 레지스트리

### 3.1 단일 설정 파일

```yaml
# llm-providers.yaml (단일 진실 원천)

defaults:
  primary: anthropic-claude-api    # 1순위
  secondary: openai-gpt-api        # 폴백 (Min 2 Always-On)
  tertiary: ollama-llama-local     # 비용 0, type 다양성

# 라우팅 우선순위 — alias 기반
routing:
  consensus_agent_a: anthropic-claude-api
  consensus_agent_b: openai-gpt-api
  consensus_agent_c: ollama-llama-local
  reviewer: anthropic-claude-api
  background_jobs: ollama-llama-local
  default: anthropic-claude-api

providers:
  anthropic-claude-api:
    type: anthropic
    litellm_model: anthropic/claude-opus-4-7   # LiteLLM model prefix
    auth_method: api_key
    api_key_env: ANTHROPIC_API_KEY
    cost: per_token
    cost_estimate: $15/1M_input + $75/1M_output
    status: active
    health_check: dry                          # dry probe (실 토큰 호출 안 함)

  anthropic-claude-oauth:
    type: anthropic
    litellm_model: anthropic/claude-opus-4-7
    auth_method: oauth_subscription
    oauth_credentials_env: CLAUDE_CREDS_PATH   # ⚠️ 경로는 env로 보간 (R7)
    cost: flat_subscription
    cost_estimate: $100/month (Max 5x) + extra credits
    status: standby
    known_bugs:
      - "ADR-008 R4: #15080, #6475, #12905, #10575"
    notes: "API 키 경로 우선. OAuth는 폴백·비용 절감 시에만"

  openai-gpt-api:
    type: openai
    litellm_model: openai/gpt-5.5
    auth_method: api_key
    api_key_env: OPENAI_API_KEY
    cost: per_token
    status: active
    health_check: dry

  openai-gpt-oauth:
    type: openai
    litellm_model: openai/gpt-5.5
    auth_method: oauth_subscription
    oauth_credentials_env: CODEX_CREDS_PATH
    cost: flat_subscription
    cost_estimate: $200/month (ChatGPT Pro)
    status: standby
    tos_notes: "개인 단일 사용자만. ADR-008 부록 A.1 정책 변동 모니터링"

  ollama-llama-local:
    type: ollama
    litellm_model: ollama/llama-3.3-70b
    auth_method: none
    endpoint: http://localhost:11434
    cost: free
    status: active

  openrouter-fallback:
    type: openrouter
    litellm_model: openrouter/anthropic/claude-opus-4.7
    auth_method: api_key
    api_key_env: OPENROUTER_API_KEY
    cost: per_token
    status: standby
```

### 3.2 status 필드

| 값 | 의미 | facade 동작 |
|---|------|-----------|
| `active` | 정상 사용 가능 | 라우팅에 포함, 폴백 체인에 포함 |
| `standby` | 명시 호출 또는 폴백 시에만 사용 | 라우팅 디폴트에서 제외, 폴백에 포함 |
| `deprecated` | 사용 시 경고 | stderr 경고 + 메트릭 |
| `blocked` | 즉시 차단 (장애·보안) | 즉시 폴백 + 알림 |

### 3.3 cost 필드 + 동일 type active 강제 금지 (R5)

`flat_subscription` 또는 동일 `type`은 active로 동시에 둘 수 없다. 시작 시 검증:

```python
# config 검증 (시작 시 fail-fast)
def validate_config(config):
    active = [(k, v) for k, v in config["providers"].items() if v["status"] == "active"]
    if len(active) < 2:
        raise ConfigError(f"Min 2 active 정책 위반. ADR-008 #5")

    types = [v["type"] for k, v in active]
    if len(set(types)) != len(types):
        raise ConfigError(
            f"동일 type 2개 active 금지 (정전 시 동시 실패). 현재 type 분포: {types}. "
            f"3+1 합의 R5 강제."
        )
```

---

## 4. LLM Facade 인터페이스

### 4.1 단일 facade — `LLMFacade` (~100 LOC)

```python
# adapters/llm/facade.py — 정확히 이 파일만 LiteLLM 직접 import

import litellm
from typing import AsyncIterator, Literal
from dataclasses import dataclass, field

# ===== Request/Response 표준 스키마 =====

@dataclass(frozen=True)
class LLMRequest:
    messages: list[dict]                 # OpenAI 호환 messages 배열
    model_alias: str                     # 라우팅 alias (예: "consensus_agent_a")
    system: str | None = None            # ← R1 보강 (Anthropic system 분리 지원)
    temperature: float = 0.7
    max_tokens: int = 4096
    tools: list[dict] | None = None
    tool_choice: dict | str | None = None       # ← R1 보강
    response_format: dict | None = None         # ← R1 보강 (json mode)
    stop_sequences: list[str] | None = None     # ← R1 보강
    stream: bool = False                        # ← R1 보강 (명시화)
    metadata_in: dict | None = None             # 호출 메타 (요청 ID 등 — redaction 대상)

@dataclass(frozen=True)
class LLMMetadata:
    """metadata는 화이트리스트 키만 (R2 보강). raw dict 금지."""
    provider_used: str                   # 실제 사용된 provider key
    fallback_chain: list[str]            # 시도된 provider 순서
    finish_reason: str
    request_id: str | None = None
    # ↑ 화이트리스트 — 새 키 추가는 본 데이터클래스 수정 필요 (depcruise로 강제)

@dataclass(frozen=True)
class LLMResponse:
    content: str                         # 정규화된 본문 (multimodal은 별도 — §4.4)
    usage: dict                          # {input_tokens, output_tokens, cost_estimate}
    metadata: LLMMetadata                # 구조화된 메타 (raw dict 아님)

# ===== Stream 이벤트 합 타입 (R11 보강) =====

@dataclass(frozen=True)
class StreamTextDelta:
    text: str

@dataclass(frozen=True)
class StreamToolCallDelta:
    tool_call_id: str
    name: str | None
    arguments_delta: str

@dataclass(frozen=True)
class StreamUsageEnd:
    usage: dict
    finish_reason: str

StreamEvent = StreamTextDelta | StreamToolCallDelta | StreamUsageEnd

# ===== Facade =====

class LLMFacade:
    """모든 LLM 호출의 단일 진입점. 본 클래스 외 LiteLLM 직접 호출 금지."""

    def __init__(self, config: dict):
        validate_config(config)                  # Min 2 + 동일 type 강제
        self._router = litellm.Router(...)       # LiteLLM Router에 위임
        self._redactor = RedactionFilter(...)    # R3 보강
        self._oauth_lock = SingleFlightLock(...) # R6 보강

    async def complete(self, req: LLMRequest) -> LLMResponse:
        provider_key = self._resolve(req.model_alias)
        try:
            raw = await self._router.acompletion(
                model=self._litellm_model(provider_key),
                messages=self._build_messages(req),
                **self._build_options(req),
            )
        except litellm.AuthenticationError:
            await self._on_active_degraded(provider_key)  # R4 재검증
            raise
        return self._normalize(raw, provider_key)

    async def stream(self, req: LLMRequest) -> AsyncIterator[StreamEvent]:
        # ... LiteLLM streaming + first-token 후 폴백 금지 (R8 보강)
        ...

    async def health(self) -> dict[str, bool]:   # ← R10 보강 (provider_key 인자 제거)
        """전체 active provider 헬스 — facade 내부에서 alias 조회. 외부 분기 금지."""
        return await self._router.health_check(dry=True)
```

### 4.2 응답 정규화 — LiteLLM 위임 (R2 보강)

LiteLLM이 모든 provider 응답을 **OpenAI 포맷으로 자동 통일**하므로, 본 facade의 정규화는 다음에만 집중:

| 항목 | 처리 |
|-----|------|
| `content` 정규화 | LiteLLM이 자동 — facade는 `raw["choices"][0]["message"]["content"]` 추출만 |
| 토큰 카운트 (`usage`) | LiteLLM 통일 (`prompt_tokens`/`completion_tokens`) — facade가 cost_estimate 추가 |
| `finish_reason` | LiteLLM 통일 — `LLMMetadata.finish_reason`로 격리 |
| **provider 고유 메타** | **버림** — `LLMMetadata` 화이트리스트 외 키는 통과 못 함 (raw dict 누출 차단) |
| `tool_use` 왕복 (R12) | OpenAI tool_calls 표준 사용. Anthropic tool_use는 LiteLLM이 자동 변환 |
| multimodal (이미지) | OpenAI vision 포맷 표준 — `content`가 list[dict] 케이스만 별도 핸들링 |

### 4.3 에러 분류 — LiteLLM 표준 예외 위임

```python
# LiteLLM 표준 예외만 catch
litellm.AuthenticationError       # 401/403 → 즉시 폴백
litellm.RateLimitError            # 429 → 백오프 후 재시도
litellm.ServiceUnavailableError   # 5xx → 백오프 후 폴백
litellm.BadRequestError           # 400 → 사용자 에러 (재시도 안 함)
```

provider 고유 예외는 **LiteLLM이 표준 예외로 변환**하므로 facade는 별도 매핑 불필요.

### 4.4 호출 흐름

```
caller.code:
  response = await llm.complete(LLMRequest(
      messages=[{"role": "user", "content": "..."}],
      model_alias="consensus_agent_a",
      system="당신은 ...",
  ))

Facade 내부:
  1. routing[model_alias] → provider_key
  2. validate_config() 통과 (Min 2 active)
  3. LiteLLM Router에 위임 (model_id 매핑, fallback chain 적용)
  4. 응답 정규화: LiteLLM 표준 → LLMResponse + LLMMetadata 화이트리스트
  5. 메트릭 기록 (redaction 적용)
  6. 응답 반환
```

---

## 5. 라우팅 — LiteLLM Router 위임

### 5.1 Router 설정 매핑

본 설계의 `llm-providers.yaml`을 LiteLLM Router 형식으로 변환:

```python
def to_router_config(providers_yaml):
    return {
        "model_list": [
            {
                "model_name": alias,                          # routing alias
                "litellm_params": {
                    "model": providers[alias]["litellm_model"],
                    "api_key_env": providers[alias].get("api_key_env"),
                    # ...
                },
            }
            for alias in providers_yaml["routing"].values()
        ],
        "router_settings": {
            "fallbacks": build_fallbacks(providers_yaml),
            "cooldown_time": 60,                              # blocked status 자동 전환 트리거
            "num_retries": 3,
            "timeout": 30,
        },
    }
```

### 5.2 폴백 race 완화 (R8 보강)

LiteLLM Router의 fallback에 추가 보강:

| Race | LiteLLM 기본 | 본 facade 보강 |
|------|-------------|--------------|
| 헬스체크 전이 race | cooldown_time으로 일부 흡수 | call 단위 immutable snapshot — 호출 시점 routing 캡처 |
| Rate limit thundering herd | num_retries + 백오프 | per-provider semaphore + 지터 (jitter) |
| OAuth refresh race | 없음 | **R6 single-flight lock** (§7.2) |
| Streaming 폴백 이중 출력 | 없음 | **first-token 후 폴백 금지** 규칙 — facade가 stream 도중 끊기면 에러 발생, 폴백 안 함 |
| active=2 검증 race | 없음 | 자동 강등 시 **R4 재검증** (§6.2) |

### 5.3 명시 vs 자동

```
명시: llm.complete(LLMRequest(model_alias="consensus_agent_b", ...))
자동: llm.complete(LLMRequest(messages=[...]))  → routing[default]
```

`model_alias`는 의미 없는 명칭만 허용. provider/모델명을 alias에 인코딩 금지(예: `claude_only_path` 같은 alias는 lint 룰로 차단 — 위반 패턴 #1 회피 차단).

---

## 6. Min 2 Always-On + 런타임 재검증 (R4 보강)

### 6.1 시작 시점 검증 (불변)

```python
def validate_config(config):
    active = [(k, v) for k, v in config["providers"].items() if v["status"] == "active"]

    if len(active) < 2:
        raise ConfigError("Min 2 active 정책 위반 (시작 시) — ADR-008 #5")

    types = [v["type"] for k, v in active]
    if len(set(types)) != len(types):
        raise ConfigError(f"동일 type 2개 active 금지 — 3+1 합의 R5")
```

### 6.2 런타임 재검증 (R4 신규)

**모든 강등 경로**에서 active 카운트를 재계산하고 부족하면 degraded 모드로 전환:

```python
async def _on_active_degraded(self, provider_key: str):
    """헬스체크 자동 강등, 한도 도달 폴백, blocked 전환 등에서 호출."""
    self._mark_provider_blocked(provider_key)
    active_count = self._count_active()

    if active_count < 2:
        await self._enter_degraded_mode(reason=f"active={active_count} (need ≥2)")
```

### 6.3 Degraded 모드 (R4 신규)

```
Degraded 모드 진입 시:
  1. stderr 경고 + 메트릭 알람 (전 시스템 알림)
  2. 새 호출은 처리 가능한 alias만 수용 (degraded provider 의존 alias는 503)
  3. 사용자 노출 방식 (P3 라이프사이클과 연계 결정 필요):
     [선택지] UI 배너 / 로그만 / 메트릭 알람만 — 미해결 결정 #5
  4. 강등 provider 복구 시 자동 active 복귀 + degraded 모드 해제
  5. degraded 모드 30분 지속 시 운영자 호출 (escalation)
```

### 6.4 시나리오 — Claude Max 구독 취소

```
Step 1: 사용자가 llm-providers.yaml에서 anthropic-claude-oauth status=blocked
Step 2: anthropic-claude-api는 별도 결제 → 영향 없음
Step 3: ollama-llama-local 그대로 active → 시스템 정상

만약 anthropic-claude-api도 미사용이라면:
Step 1-2: oauth 차단 + api 미설정 시 동일 type 검증 통과 (anthropic 없음)
Step 3: Min 2 검증 → openai + ollama 활성 시 통과
```

---

## 7. OAuth 직결 금지 정책 + Credentials 처리 (R7 보강)

### 7.1 우선순위

| 순위 | 인증 | 사용 조건 |
|-----|------|---------|
| 1 | `api_key` | 기본. 모든 새 코드 |
| 2 | `oauth_subscription` | 비용 절감 시. 단 §7.2~7.3 조건 충족 |

### 7.2 OAuth 사용 시 필수 조건

OAuth provider를 active로 전환하려면:
1. ✅ 같은 type의 API 키 provider가 **최소 1개 standby** 등록 (즉시 폴백 가능)
2. ✅ **Single-flight lock** 적용 — 동시 호출이 만료된 토큰을 동시에 refresh하지 못하도록 (R6 보강)
3. ✅ 헬스체크 활성화 (dry probe만 — §9.2)
4. ✅ 정책 변동 모니터링 task 등록 (월 1회 ToS 검토)
5. ✅ ADR-008 R4 인지 (Claude OAuth 버그 4종)

```python
# OAuth refresh single-flight (R6)
class SingleFlightLock:
    async def refresh_with_lock(self, provider_key: str):
        async with self._locks[provider_key]:   # provider별 lock
            if not self._needs_refresh(provider_key):
                return self._cached_token(provider_key)
            new_token = await self._do_refresh(provider_key)
            self._cache_token(provider_key, new_token)
            return new_token
```

### 7.3 Credentials 처리 (R7 신규)

| 항목 | 정책 |
|-----|------|
| **경로 환경변수화** | `oauth_credentials_env: CLAUDE_CREDS_PATH` — yaml에 절대 경로 평문 금지 |
| **파일 권한** | `chmod 600` 강제 검증 (시작 시) — 권한 위반 시 fail-fast |
| **Docker mount** | `:ro` (read-only) + 권한 검증 |
| **로그/메트릭 echo 금지** | RedactionFilter가 `auth/token/key/secret` 패턴 자동 strip (§8.2) |
| **테스트** | 토큰이 응답·로그·메트릭 어디에도 echo되지 않는지 단위 테스트 필수 |

### 7.4 ChatGPT Pro Codex OAuth 특별 조항

- **개인 단일 사용자만** (ToS — third-party 집계 금지)
- 정책 변동 시 즉시 standby 전환
- 변동 모니터링: OpenAI 정책 페이지 + 커뮤니티 (Reddit, GitHub)

---

## 8. 비용·관측성 + Redaction (R3 보강)

### 8.1 LiteLLM Callback 활용

LiteLLM의 callback 시스템에 본 도메인 메트릭 + redaction을 등록:

```python
litellm.success_callback = [DomainMetricsCallback(redactor=...)]
litellm.failure_callback = [DomainMetricsCallback(redactor=...)]

class DomainMetricsCallback:
    def log_event(self, event):
        # event는 LiteLLM의 표준 이벤트 객체
        record = {
            "request_id": event.request_id,
            "timestamp": event.timestamp,
            "model_alias": self._reverse_alias(event.model),
            "provider_used": event.provider,
            "fallback_chain": event.fallback_chain,
            "input_tokens": event.usage.prompt_tokens,
            "output_tokens": event.usage.completion_tokens,
            "cost_estimate": event.cost,
            "latency_ms": event.duration_ms,
            "status": event.status,
        }
        # ⚠️ Redaction 의무 (R3) — 모든 필드를 redactor 통과
        record = self._redactor.scrub(record)
        self._sink.write(record)
```

### 8.2 Redaction 정책 (R3 신규)

```python
class RedactionFilter:
    """모든 응답·예외·메트릭에서 비밀값 자동 strip."""

    PATTERNS = [
        re.compile(r"sk-[a-zA-Z0-9]{20,}"),         # OpenAI API key
        re.compile(r"sk-ant-[a-zA-Z0-9]{20,}"),     # Anthropic API key
        re.compile(r"Bearer [a-zA-Z0-9._-]+"),      # Bearer token
        re.compile(r"\"(api_key|token|auth|secret|password|credential)\"\s*:\s*\"[^\"]+\""),
    ]
    KEY_BLACKLIST = {"api_key", "token", "secret", "auth", "credential", "authorization"}

    def scrub(self, obj):
        # dict는 키 기반 + 값 패턴 매칭
        # str은 패턴 매칭으로 [REDACTED] 치환
        # ...
```

**화이트리스트 vs 블랙리스트** (미해결 결정 #4): 본 설계는 **블랙리스트(패턴 + 키 매칭)** 채택. 화이트리스트는 운영 부담 ↑, 새 메타 추가 시마다 화이트리스트 갱신 필요. 단 `LLMResponse.metadata`는 데이터클래스로 화이트리스트화(R2)되어 있어 누출 통로 자체가 좁음.

### 8.3 의사결정 대시보드

월별 집계로 다음 지표 노출:
- provider별 비용 (구독 취소/유지 결정용)
- provider별 가용성 (failure rate)
- alias별 평균 응답 시간
- fallback 발생 빈도
- OAuth refresh 빈도 (R6 lock 활용도)

### 8.4 한도 알림

`flat_subscription`:
- 사용량 80% → 경고 + 메트릭 알람
- 사용량 100% → 자동 폴백 → R4 재검증 트리거

---

## 9. Liquidity 위반 패턴 차단

### 9.1 위반 패턴 카탈로그 — LiteLLM 자연 차단 활용

| # | 패턴 | LiteLLM 채택 시 차단 | 추가 메커니즘 |
|---|------|---------------------|-------------|
| 1 | 모델명/provider 분기 코드 | 모델명은 LiteLLM 형식(`anthropic/...`)으로 yaml에만 존재 | depcruise: alias 외 모델명 문자열 금지 |
| 2 | provider별 응답 후처리 함수 분리 | LiteLLM이 OpenAI 포맷으로 통일 → 후처리 단일 | `LLMResponse.metadata` 화이트리스트(R2) |
| 3 | 스킬/프롬프트 안 특정 모델 가정 | LiteLLM 무관 | 코드 리뷰 + 테스트(다른 alias로도 통과해야 함) |
| 4 | 메모리에 provider별 메타 저장 | LiteLLM이 raw 메타 통일 | `LLMMetadata` 화이트리스트(R2) |
| 5 | provider 전용 인증 갱신 로직 | LiteLLM이 자체 처리 | facade 외 OAuth 코드 금지 + R6 single-flight |
| 6 | 포맷별 다운스트림 파서 | LiteLLM 통일 | `LLMResponse.content` 단일 필드 |

### 9.2 Health Check — Dry Probe (R9 보강)

실 토큰을 매 60s마다 echo하면 인증 노출 (R6 위험). LiteLLM Router의 health_check를 **dry mode**로 사용:

```python
# 무토큰 헬스 검증
async def health(self) -> dict[str, bool]:
    """endpoint 도달성만 확인. 실 인증 토큰 사용 안 함."""
    results = {}
    for alias, provider in self._active_providers().items():
        try:
            await self._router.health_check(provider, dry=True)  # endpoint ping만
            results[alias] = True
        except Exception:
            results[alias] = False
    return results
```

MVP에 dry probe 헬스체크 포함 (이전 P1의 §6.3 시나리오와 일관성 확보 — A 발견 보강).

### 9.3 정적 검사 — depcruise (단순화, Bβ-2)

```javascript
// .depcruise.cjs (개략, P5 문서로 상세화)
{
  forbidden: [
    {
      name: "no-direct-llm-sdk",
      from: { pathNot: "^src/adapters/llm/facade\\.py$" },
      to: { path: "^(litellm|anthropic|openai|@anthropic-ai|@openai|ollama)" }
    },
    {
      name: "no-llm-via-httpx",
      // grep 보조: src/ 안에서 'api.anthropic.com', 'api.openai.com' 등 endpoint 문자열 직접 사용 금지
    },
    {
      name: "no-model-name-in-code",
      // grep: 'claude-opus', 'gpt-' 등 모델 ID 패턴 src/ 안 금지 (yaml만 허용)
    },
  ]
}
```

LiteLLM 채택 시 룰이 6종 → 3종으로 단순화 (Option α 대비).

### 9.4 정적 검사 — AST 동적 import 차단 (R8/R9 보강)

```python
# pre-commit: ruff custom rule 또는 AST 스캐너
# src/ 하위에서 다음 패턴 금지:
#   importlib.import_module("anthropic")
#   __import__("openai")
#   exec("import litellm")
```

### 9.5 코드 리뷰 체크리스트

- [ ] LLM 호출이 모두 facade를 거치는가?
- [ ] 모델/provider 이름이 코드에 하드코딩되지 않았는가? (yaml만 허용)
- [ ] 응답 처리가 `LLMResponse` 표준 필드만 사용하는가? (metadata raw dict 접근 금지)
- [ ] 새 provider 추가 시 `llm-providers.yaml`만 수정했는가?
- [ ] OAuth 사용 시 §7.2~7.3 조건을 충족하는가?
- [ ] 메트릭/로그에 비밀값 echo 가능 경로가 없는가?

---

## 10. 마이그레이션 경로

### 10.1 Provider 추가

```
새 모델 "Llama 4 70B" 추가:
  Step 1: llm-providers.yaml에 항목 추가 (litellm_model: ollama/llama-4-70b)
  Step 2: 검증 (테스트로 호출 동작 확인)
  Step 3: status: active 전환 (또는 routing alias 할당)
  Step 4: 끝.
```

### 10.2 Provider 제거

```
"openai-gpt-oauth" 제거 (정책 변동 등):
  Step 1: status: blocked → 즉시 모든 호출 차단 → R4 재검증 트리거
  Step 2: routing alias 재할당 확인
  Step 3: 1주 모니터링
  Step 4: yaml 항목 삭제
```

### 10.3 모델 변경

```
Claude Opus 4.7 → Claude Opus 5.0:
  Step 1: yaml의 litellm_model 수정 (anthropic/claude-opus-5-0)
  Step 2: 끝.
```

### 10.4 응급 폴백

```
Anthropic + OpenAI 동시 장애:
  자동: LiteLLM Router fallback → openrouter-fallback 또는 ollama-llama-local 도달
  수동: standby provider를 active로 임시 전환 (R4 재검증 자동 통과)
```

---

## 11. 적용 시나리오

### 11.1 Hermes Phase 1 (1~2주) — 3 active type 다양성 (A 발견 보강)

```
설정:
  active: [anthropic-claude-api, openai-gpt-api, ollama-llama-local]
  routing.default: anthropic-claude-api
  routing.background_jobs: ollama-llama-local

목적: API 키만 사용. OAuth 직결 금지 정책 검증. Min 2 + type 다양성 동시 충족.
검증: 비핵심 작업을 Hermes로 수행, facade 정상 동작 확인.
```

**이전 P1의 Phase 1 문제 (ollama 미포함, §6.2 type 다양성 위반) 해소**.

### 11.2 Hermes Phase 2 (2~4주) — 3+1 합의 다중 LLM

```
설정:
  active: [anthropic-claude-api, openai-gpt-api, ollama-llama-local]
  routing:
    consensus_agent_a: anthropic-claude-api
    consensus_agent_b: openai-gpt-api
    consensus_agent_c: ollama-llama-local
    reviewer: anthropic-claude-api

목적: 3+1 합의의 메타 한계 해소 (전 에이전트 Claude → 다중 모델).
검증: 3+1 다중 모델 합의 실행, 결과 품질 ≥ 단일 Claude.
```

### 11.3 Claude Max 취소 시나리오

```
사용자: Claude Max 비용 부담 → 취소.
Step 1: anthropic-claude-oauth status=blocked → R4 재검증 → active 카운트 OK
Step 2: anthropic-claude-api는 영향 없음 (별도 결제)
Step 3: 끝. 코드 변경 0.
```

### 11.4 신규 provider 추가 (Gemini)

```
Step 1: yaml에 google-gemini-api 추가 (litellm_model: gemini/gemini-2.5-pro)
Step 2: status: standby → 테스트
Step 3: status: active (단 동일 type 검증 통과 시)
Step 4: 끝. facade 코드 수정 0 (LiteLLM이 google_genai 자체 지원).
```

신규 provider type 추가도 LiteLLM이 처리 → facade 변경 불필요.

---

## 12. ADR-008 차단조건 매핑

| 차단조건 | 본 설계의 충족 메커니즘 |
|---------|----------------------|
| #1 SQLCipher 암호화 | 본 문서 범위 외 (P2) |
| #2 JSONL export | 본 문서 범위 외 (P2) |
| #3 v0.x 버전 핀 | 본 문서 범위 외 (P2) |
| **#4 provider 어댑터 1개 추상화 + 분기 금지** | **§4 LLMFacade (단일) + §9.3 depcruise + §9.4 AST 차단** |
| **#5 최소 2 provider always-on** | **§6.1 시작 시 fail-fast + §6.2 런타임 재검증 + §6.3 degraded 모드** |
| #6 Docker 격리 | 본 문서 범위 외 (P2) |

---

## 13. ADR-004 정합성 — 본질 일치

ADR-004 핵심 원칙: **"자체 어댑터 불필요 — 외부 SDK 활용. 자체 어댑터는 외부 SDK 부족 입증 후에만(v2.0)"**

본 P1은 ADR-004를 그대로 따른다:
- LiteLLM(외부 SDK)이 1차
- 자체 코드는 facade 100 LOC + 도메인 보강만
- 자체 Adapter 작성은 v2.0 — 진입조건은 **ADR-009**에서 명세

**3+1 합의 (Agent C) 결과**: 이전 초안(자체 Adapter 1차)은 ADR-004 본질 위반이었으나, Option β 채택으로 정합성 회복.

---

## 14. 다른 ADR과의 정합성

| 관련 문서 | 정합성 |
|---------|--------|
| **ADR-004** (생성 AI 확장성) | **본질 일치** — 외부 SDK(LiteLLM) 우선 + config-driven |
| **ADR-006** (환경 변수 + Docker) | API 키 환경 변수, OAuth credentials env 보간(R7) + Docker mount :ro |
| **ADR-005** (AI 백엔드 스택) | Python 분리 기준 따름 |
| **ADR-008** (Hermes 도입) | 차단조건 #4·#5 충족 메커니즘 |
| **ADR-009** (자체 Adapter v2.0 진입조건) | 본 문서 §15 v2.0 로드맵의 정량 트리거 |
| **PROJECT_CONSTITUTION 제8조** | redaction 의무화(R3), 비밀값 echo 금지 테스트(R7) |
| **harness-engineering-design** | Layer 1.5 정적 검사 + Layer 5 신규 provider 합의 |

---

## 15. Phase 로드맵

> **⚠️ v1.0 단계화 (CB-2, 2026-05-28 SC-Provider Liquidity 합의)**: v1.0 은 "12 보강 *모두* 동시 구현"이 아니라 **Core MVP 발효 + 나머지 보강 deferred phase 단계화**로 분리 승인됨. deferred 항목은 *삭제 아님 — 설계 명세 존속*, 사용자 명시 별도 sub-cycle 로만 진입.

| Phase | 내용 | 상태 | 진입 조건 |
|-------|------|------|----------|
| **v1.0 Core MVP** | `complete()` LiteLLM Router 위임(model=alias) + `llm-providers.yaml` + Min 2 fail-fast + 동일 type 강제 + redaction(RT-1 송신) + 런타임 강등 감지(fail-loud) + 응답 정규화(LLMMetadata 화이트리스트) | **✅ 발효 (69 entry, mock-verified)** | §17 재합의 통과 (2026-05-28) |
| **v1.0 보강 단계화 (deferred phase)** | streaming(StreamEvent) + OAuth single-flight + degraded *모드*·R4 자동복구·UI/timer + DomainMetricsCallback + 폴백 race 완화 + dry probe health 실배선 | 명세 존속·구현 deferred | 사용자 명시 별도 sub-cycle |
| **v1.1** | LiteLLM Router 고급 기능 (cooldown 튜닝, custom retry strategy) + 의사결정 대시보드 | 필요 입증 후 | MVP 운영 1~2주 + 폴백/한도 이벤트 발생 |
| **v1.2** | 자동 모델 추천 (성능/비용 학습 기반) + multi-modal 통합 | 필요 입증 후 | 사용 데이터 축적 |
| **v2.0** | 자체 Adapter 작성 (LiteLLM 폐기) | **ADR-009 진입조건 충족 시에만** | LiteLLM이 신규 provider X를 N분기 내 미지원 + PR 거부 등 |

> ADR-009에 v2.0 진입조건의 **정량 트리거**가 명세되어 있다. LiteLLM 사용은 v1.0~1.2까지의 기본 노선이며, v2.0으로의 전환은 명시 트리거 없이 발생하지 않는다.

---

## 16. Phase 2 검토 사항 (현재 미구현)

| 항목 | 도입 조건 |
|------|----------|
| 추론 캐시 레이어 | 동일 요청 반복 비율 ≥ 20% |
| Provider별 prompt 최적화 | 모델 간 결과 품질 편차 측정 후 |
| Streaming 응답 표준화 보강 | streaming 사용 사례 발생 시 |
| Multi-modal (이미지/오디오) 통합 | 별도 도메인 (ADR-003·004 참조) |

---

## 17. 검증 항목 (재합의용)

본 v2 설계가 3+1 합의 12 보강 + 4 β-추가를 모두 반영했는지 재합의 시 검증:

### Agent A (구현)
- [ ] LLMRequest 신규 필드 5종 (system, response_format, tool_choice, stop_sequences, stream) — §4.1
- [ ] AsyncIterator[StreamEvent] 합 타입 — §4.1
- [ ] tool_use 정규화 (LiteLLM 위임 명시) — §4.2
- [ ] §4.1 health(provider_key) 모순 해소 — §4.1, §9.2
- [ ] 폴백 race 5종 완화 — §5.2
- [ ] Phase 1 시나리오 ollama 포함 — §11.1

### Agent B (안전)
- [ ] LLMResponse.metadata 화이트리스트화 — §4.1, §4.2
- [ ] Redaction 필터 의무화 (응답·예외·메트릭) — §8.2
- [ ] OAuth credentials 처리 명세 — §7.3
- [ ] OAuth refresh single-flight — §7.2
- [ ] 동일 type 2개 active 금지 강제 — §3.3, §6.1
- [ ] 런타임 active 재검증 + degraded 모드 — §6.2, §6.3
- [ ] Health dry probe — §9.2

### Agent C (대안)
- [ ] LiteLLM facade 승격 — §1.2, §4
- [ ] depcruise 단순화 — §9.3
- [ ] LiteLLM redaction + facade 보강 통합 — §8.1, §8.2
- [ ] ADR-009 진입조건 ADR 작성 (별도 파일)

### Reviewer
- [ ] ADR-004 본질 일치 — §13
- [ ] ADR-008 차단조건 #4·#5 충족 — §12
- [ ] Hermes 합의 일관성 (Option β로 외부 SDK 우선 정신 유지) — §1.3

---

**이 문서는 2026-05-28 SC-Provider Liquidity 풀 3+1 + 외부 LLM 1+(codex gpt-5.5 cross-vendor) §17 재합의를 통과하여 "확정 v2 / Core MVP 구현분리 승인(staged)" 으로 승격되었습니다** (`docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md`, 4 source APPROVE WITH CONDITIONS, BLOCKING 8 흡수). Core MVP 발효(69 entry), 12 보강 단계화(deferred phase 명세 존속, §15).
