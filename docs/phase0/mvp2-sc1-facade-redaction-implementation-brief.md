# SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief (v1.1)

> **작성**: 2026-05-28 (65번째 entry 진입 cycle — 세션 #3)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 4 + 권고 6 1pass 흡수**. 핵심 정정: **B-1 catalog 재사용 (i) src→tools import → (ii) 공유 모듈 추출** (Reviewer verify: (i) namespace package 동작하나 의존 방향 부적절, 3:1 majority) / **B-2 `[REDACTED]` whole-match → group-aware 치환** (값만 마스킹, key/구조 보존 — secret_scanner = 검출 전용 치환 함수 0) / **B-3 송신 redaction 권위 = governance §4.1 + 64 trajectory** (§8.2 = egress 보조) / **B-4 범위 = messages + metadata** (full fields deferred). §12 흡수 매트릭스 추가.
>
> **scope** (사용자 명시 "RedactionFilter 집중"): **RedactionFilter 완전 구현 (secret_scanner Tier-1 45 catalog 공유 모듈 추출 재사용, R-2-c (ii)) + facade `complete()` 송신 전 redaction 적용 layer 통합**. **LiteLLM Router 위임 = deferred (Provider Liquidity 별도 sub-cycle)**. TDD 적용.
>
> ⚠️ **명칭 정직성 (over-claim 차단, 본 세션 #2 4회 cascade 교훈 답습)**: 본 cycle = **facade redaction layer real (R-2 GP-2 prevention)** — **full facade real 아님** (LiteLLM Router 위임 + Min 2 검증 + registry yaml = deferred). "facade real 완성" 표현 금지.
>
> **본 cycle = 큰 cycle (실 코드 + TR-1)** — facade.py 헤더 명시 "real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화". 64 entry SC-1 = 풀 3+1 (TR-1) + 실 코드.
>
> **본 cycle 발효 효과** = R-2 facade RedactionFilter prevention layer **in-repo operative** + GP-2 (a) "facade redaction filter 검증" 충족 (full GP-2 PASS Exit (a)의 R-2 prong). **full GP-2 PASS 발효 = SC-2 (R-1 위임 검증) + SC-3 후 (별도)**.
>
> **선행 답습**: 64 trajectory entry brief (SC-1 정의 + R-2-a 동시 + R-2-c catalog 재사용 + RedactionFilter = facade 내부 협력자 + RT-1 atomic) + llm-providers-design §4.1/§8.2 (설계 명세) + ADR-009 §2.2 (facade 단일 진입점 의무) + secret_scanner Tier-1 45 catalog

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정** (§2)
2. **송신 redaction 역할 명세** (GP-2 prevention = request body secret strip, §3)
3. **facade 통합 지점 + Router deferred 처리** (RT-1 window 회피, §4)
4. **TDD 계획** (RED → GREEN → REFACTOR, §5)
5. **합의 형태 + 승격 트리거** (§6)
6. **Provider Liquidity 보존 + 금지 + Rollback Trigger + Evidence + 자기진단** (§7~§11)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | **LiteLLM 설치 + Router 위임 구현** (Provider Liquidity 별도 sub-cycle, deferred) | 0 |
| 2 | **full facade real** (Min 2 검증 + registry yaml + 에러분류 + 정규화 + OAuth lock + callback) | 0 |
| 3 | **full GP-2 PASS 발효** (SC-2 R-1 위임 검증 + SC-3 후) | 0 |
| 4 | **R-1 Hermes 위임 검증** (SC-2 별도 sub-cycle) | 0 |
| 5 | secret_scanner Tier-1 45 catalog **패턴 내용 변경** (R-4.1 답습 "변경 0건", R-7(b) 차등) | 0 |
| 6 | Tier-2/3 catalog 확장 / base64 evasion (R-5 영구 분리) | 0 |
| 7 | detection-layer PASS (60) / MVP-2 PASS (62) 재선언 | 0 |
| 8 | ADR / 헌법 / governance / llm-providers-design 본문 변경 | 0 |
| 9 | llm-providers.yaml registry 작성 (Min 2 검증 의존, Router deferred와 함께) | 0 |
| 10 | 자동 후속 sub-cycle (SC-2/SC-3) 진입 | 0 (사용자 명시 의무) |

### §0.3 권위 답습 source

- ⭐ **송신 redaction 권위 (B-3 정정)**: **governance-preconditions.md §4.1** (line 422 — "LLM API request body 에 secret 노출 차단" 송신 경로) + **64 trajectory brief §3** = 송신 redaction PRIMARY 권위. **§8.2 RedactionFilter (docstring "응답·예외·메트릭") = egress(응답/로그) scrub 보조** (송신 redaction은 §8.2 직접 문구 아님, governance 정합 확장).
- **llm-providers-design.md §8.2** (RedactionFilter 설계 — PATTERNS 4 + KEY_BLACKLIST 6, 블랙리스트 채택, egress scrub) + **§4.1** (facade `complete()` 흐름) + **§4.4** (호출 흐름 — redaction 적용 지점 step 5)
- **governance-preconditions.md §4.5 (a)** (facade redaction filter 검증)
- **ADR-009 §2.2** (facade 단일 진입점 의무 — LiteLLM 직접 import = facade.py 한정, provider SDK 직접 import 금지)
- **secret_scanner.py** (Tier-1 45 catalog = baseline 5 + prefix 31 + regex 7 + alternation 2, `ALL_PATTERNS`/`COMPILED_PATTERNS`/`scan_text()`, 외부 의존성 0 stdlib)
- **.importlinter** (root=src, forbidden=LLM SDK facade 예외 — src↔tools 경계 결정 입력)
- **64 trajectory entry brief §4.4** (R-2-a/c 권고 + RedactionFilter = facade 내부 협력자 + RT-1 atomic)
- **redaction-pattern-equivalence.md** (R-4 — Tier-1 catalog 설계 동등성, Hermes 안전성 선언 금지 §7.3)

---

## §1 진입 컨텍스트

- 64 entry trajectory 진입 합의 (APPROVE WITH CONDITIONS 4 source) → carry-over 1순위 SC-1 진입 (사용자 명시).
- GP-2 현 상태: detection-layer PASS (60, R-3 secret-hygiene D-2 CI operative). prevention (R-1/R-2) deferred.
- 본 cycle = **R-2 prevention prong** (facade redaction filter) in-repo 구현 → GP-2 Exit (a)의 R-2 검증 충족 (R-1 = SC-2 별도).

---

## §2 RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정

### §2.1 catalog 재사용 방식 (핵심 설계 결정 — 풀 3+1 검증 대상)

secret_scanner Tier-1 45 catalog 재사용 (R-2-c, single source detection↔prevention) — import 경계 4 옵션:

| 옵션 | 방식 | 장점 | 단점 |
|------|----|----|----|
| (i) src → tools.secret_scanner import | RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import | 즉시 single source, 변경 0 | **src(런타임) → tools(개발도구) 역방향 의존** (아키텍처 부적절, .importlinter root=src 밖이라 미차단이나 nonidiomatic) |
| (ii) ⭐ catalog 공유 모듈 추출 | Tier-1 catalog를 `src/adapters/llm/redaction_patterns.py` (또는 공유 위치) 추출, secret_scanner + RedactionFilter 공유 | single source + 런타임 정합 | **secret_scanner 변경 = R-4.1 "변경 0건" 위반 = R-7(b) 차등 자격** (별도 평가) |
| (iii) RedactionFilter 자체 복제 | Tier-1 45 패턴 복사 | 경계 깔끔 | **중복 → detection↔prevention drift 위험** (single source 위반) |
| (iv) §8.2 자체 패턴 | RedactionFilter = §8.2 4 패턴 + 6 키 | 설계 명세 직접 답습 | Tier-1 45 catalog 미사용 (R-2-c 비채택, 커버리지 ↓) |

⭐ **결정 = (ii) 공유 모듈 추출** (B-1 흡수, 4 source 3:1 majority + codex BLOCKING). **Reviewer verify**: (i) `from tools.secret_scanner import` = namespace package 동작하나 (pyproject 부재 run-from-source), **src(런타임)→tools(개발도구 PoC) 의존 방향 nonidiomatic** (.importlinter root=src 미제어 = "미차단 ≠ 승인").

**(ii) 구체화**: Tier-1 catalog literal을 **src 하위 공유 모듈** (`src/adapters/llm/redaction_patterns.py`)로 추출 → `RedactionFilter`(src) + `secret_scanner`(tools) 둘 다 import (**tools→src = 도구가 런타임 참조 = 정방향**). **secret_scanner 패턴 *내용* 변경 0건** (id/src/cat/vendor/regex 동일, R-4.1 충실) + **equivalence test 필수** (`len(ALL_PATTERNS)==45` + pattern snapshot 동일 + scan-source/scan-log pass/fail fixture 유지). secret_scanner 구조 변경 (literal 정의 → import)은 패턴 내용 0이므로 **detection 동작 불변** (R-7(b) = 패턴 *내용* 변경 아님).

### §2.2 RedactionFilter 인터페이스 (§8.2 답습)

```
class RedactionFilter:
    """LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""
    def redact_text(self, text: str) -> str: ...          # str 패턴 매칭 → secret 값만 마스킹
    def redact_messages(self, messages: list[dict]) -> list[dict]: ...  # 송신 request body redaction (GP-2 핵심)
    def scrub(self, obj) -> ...: ...                       # dict/str 재귀 (응답/메트릭/로그, §8.2 + KEY_BLACKLIST)
```

- 패턴 source = `src/adapters/llm/redaction_patterns.py` 공유 모듈 (Tier-1 45 catalog, §2.1 (ii)).
- ⭐ **B-2 흡수 — group-aware 치환 (값만 마스킹, 구조 보존)**: secret_scanner 패턴 = *검출*용 (prefix `key=` 포함 매칭 / regex group / alternation). **whole-match `[REDACTED]` 치환 시 key명·JSON 구조 소거 + word-joining artifact** (3 Agent 실증). → redaction = **매칭된 secret *값* 부분만** 마스킹 (key명/구조 보존). detection 패턴 ≠ redaction 치환 — 값 추출/group 분리 로직 별도 (R-6: `sk-***last4` 부분 마스킹 평가, 또는 `[REDACTED]` 값 한정).
- ⭐ **R-3 흡수 — `scrub()` KEY_BLACKLIST**: §8.2 `KEY_BLACKLIST` (api_key/token/secret/auth/credential/authorization) dict key 기반 redaction 구현 (Tier-1 regex만으론 key 기반 누락).
- **frozen / 순수 함수** (Layer 1 자가진화 패턴 답습, 부작용 0 — R-1 불변성).

---

## §3 송신 redaction 역할 명세 (GP-2 prevention)

⭐ **핵심 = 송신 경로 (request body) redaction** (권위 = governance §4.1 line 422 verbatim "LLM API request body 에 secret 노출 차단" + 64 trajectory §3, B-3 정정):
- `complete(req)` 흐름에서 **Router 위임 *전*** request 입력을 `redact_messages()` 통과 → secret strip 후 송신.
- ⭐ **B-4 흡수 — 범위 명시**: 본 cycle 최소 = **`req.messages` + `req.metadata`** redaction (현 placeholder `LLMRequest(alias, messages, metadata)` 기준 — `system` 필드 없음). 설계 §4.1 full fields (`system`/`tools`/`tool_choice`/`response_format`/`stop_sequences`/`metadata_in`)는 **Router 위임 sub-cycle과 함께 deferred** (시그니처 전면 개편 deferred 명시).
- ⭐ **R-5 흡수 — content list/structured 재귀**: OpenAI-compatible message content가 `str` 외 `list[dict]`(multimodal/tool) 가능 → `scrub()` 기반 재귀 처리 (str 단독 가정 회피).
- §4.4 호출 흐름 step 5 "메트릭 기록 (redaction 적용)" = 응답/로그 redaction (`scrub`).
- **GP-2 prevention 핵심 = 송신 (request body)**. 응답/로그 redaction = 보조 (§8.2 scrub).

⚠️ **redaction 의미 명확화**: GP-2 = "secret이 *실수로* LLM request body에 포함되는 것 차단" (예: 메시지에 API key 평문 노출). 정상 대화 내용 손상 아님 — Tier-1 catalog는 secret 패턴 (sk-/Bearer/api_key 등) 한정 매칭.

---

## §4 facade 통합 지점 + Router deferred (RT-1 window 회피)

### §4.1 통합 설계 (현 placeholder → redaction layer real)

현 `facade.py` (41 LOC placeholder):
- `LLMFacade.__init__(registry_path)` → RedactionFilter 인스턴스 추가 (`self._redactor = RedactionFilter(...)`)
- `complete(req)` → **redaction 적용 후 Router deferred**:
  1. `redacted = self._redactor.redact_messages(req.messages)` (송신 전 redaction — GP-2 prevention operative)
  2. Router 위임 = **deferred** → `raise NotImplementedError("LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred")` (redaction *후* 명시적 deferred)

### §4.2 RT-1 window 회피

- 64 brief RT-1 = "facade real 후 RedactionFilter 미부착 window 금지 (atomic)".
- 본 cycle: **Router deferred = 실제 LLM 송신 0 = redaction 미부착 window 없음** (송신 자체가 deferred). RedactionFilter는 complete() 진입 시 부착 → Router 발효 (SC-Provider Liquidity) 시점에 이미 redaction layer 존재 (선부착).
- ⭐ **선부착 보장**: SC-Provider Liquidity (Router 위임)가 본 SC-1 (redaction layer) *후* 진입 → Router 발효 시 redaction 이미 operative (window 0).

### §4.3 시그니처 정합 (설계 §4.1 vs 현 placeholder)

- 현 placeholder: `LLMRequest(alias, messages, metadata)`. 설계 §4.1: `LLMRequest(messages, model_alias, system, ...)`.
- 본 cycle = **redaction 통합 최소 변경** — 시그니처 전면 개편 (설계 §4.1 full)은 Router 위임 sub-cycle과 함께 (deferred). 현 placeholder 시그니처 기반 redaction layer 추가 (over-engineering 회피).

---

## §5 TDD 계획 (RED → GREEN → REFACTOR)

### §5.1 RED (실패 test 먼저)

`tests/adapters/llm/test_redaction_filter.py` (신규):
- T-1: `redact_text("sk-ant-..." secret)` → secret 값 마스킹 (group-aware, key명 보존)
- T-2: `redact_messages([{role, content: "key=sk-..."}])` → content secret 값 redacted (key 구조 보존)
- T-3: Tier-1 45 catalog 대표 패턴 (baseline + prefix + regex + alternation 각 1+) redaction 검증
- T-4 ⭐ (R-2): false positive **edge case fixture** — 정상 내용 (`sort(key=...)`, `keyboard`, `monkeypatch`, 일반 URL query) → 무변경 (secret_scanner line 157-158 `sort(key=)` 회피 의도 답습)
- T-5: `scrub(dict)` 재귀 (nested) + **KEY_BLACKLIST** (R-3) redaction + **dict 구조 무결성** (B-2 — key명/구조 보존 검증)
- T-6 ⭐ (R-4): facade `complete()` — **spy/fake redactor 주입**으로 redaction *선행* 검증 (Router deferred NotImplementedError 전 redaction 호출 입증, 단순 NotImplementedError 확인만으론 순서 미입증)
- T-7 ⭐ (R-1): **원본 불변성** — `redact_messages()` 입력 list/dict in-place mutate 0 (재시도/로그 부작용 차단)
- T-8 (B-1): **equivalence test** — `src/adapters/llm/redaction_patterns.py` 추출 후 `len(ALL_PATTERNS)==45` + pattern snapshot 동일 + secret_scanner scan-source/scan-log 동작 불변

### §5.2 GREEN (최소 구현)

- `src/adapters/llm/redaction_patterns.py` (Tier-1 45 catalog 공유 모듈 추출, §2.1 (ii)) + `secret_scanner.py` import 전환 (패턴 내용 0 변경)
- `src/adapters/llm/redaction.py` (RedactionFilter — redact_text/redact_messages/scrub, group-aware 치환 + KEY_BLACKLIST)
- `facade.py` complete() redaction 통합 (messages + metadata, Router deferred)

### §5.3 REFACTOR

- frozen / 순수 함수 정리 + test 유지 green
- **커버리지 목표 70%+** (CLAUDE.md §1)

### §5.4 verify (구현 후)

- pytest (신규 redaction test + 기존 회귀 0)
- import-linter (LLM SDK 경계 보존 — litellm import 0, Router deferred)
- secret_scanner scan-source (src + .github, violations 0)
- jarvis pytest 회귀 0

---

## §6 합의 형태 + 승격 트리거

### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (TR-1)

**정당화**: facade.py 헤더 명시 TR-1 (real 본문 작성 풀 3+1 trigger) + GP-2 prevention 보안 영역 (CLAUDE.md §3 보안 = 풀 3+1 필수) + 실 코드 + Provider Liquidity 직결.

### §6.2 승격 트리거

| # | trigger | 발화 |
|---|---------|----|
| 1 | TR-1 (facade real 본문) | ✅ |
| 2 | 보안 관련 변경 (GP-2 prevention) | ✅ |
| 3 | 실 코드 (런타임 redaction) | ✅ |
| 4 | Provider Liquidity 영향 (facade 단일 진입점) | ✅ |
| 5 | 외부 LLM cross-vendor (5조-2) | ✅ |

→ **5/5 발화 → 풀 3+1 + 외부 LLM 1+ 의무**.

### §6.3 합의 시점

본 brief = **구현 *전* 설계 승인** (SDD "문서 검토 완료 후 코드 구현" 답습). 합의 APPROVE 후 TDD 구현 (§5).

---

## §7 Provider Liquidity 보존 (ADR-009 §2.2, 5조-2 비협상)

- LiteLLM 직접 import = facade.py 한정 (Router deferred이므로 본 cycle litellm import 0 — import-linter 보존).
- RedactionFilter = facade 내부 협력자 (provider-agnostic, 모델명 분기 0).
- facade 단일 진입점 의무 보존 ([[feedback_provider_liquidity]]).

---

## §8 금지 사항

§0.2 답습 (10). 추가: LiteLLM 설치 0 / Router 위임 구현 0 / secret_scanner 패턴 변경 0 / litellm import 0 / full facade real 표현 0 / full GP-2 PASS 발효 0 / 자동 SC-2/SC-3 진입 0.

---

## §9 Rollback Trigger

| # | trigger | 대응 |
|---|---------|----|
| RT-1 | Router 발효가 redaction layer *전* 진입 (window) | SC-Provider Liquidity는 본 SC-1 후 진입 (선부착 §4.2) |
| RT-2 | catalog 재사용 (i) src→tools 의존 방향 BLOCKING | (ii) 공유 모듈 추출 fallback (R-7(b) 차등) |
| RT-3 | redaction false positive (정상 내용 손상) | Tier-1 catalog = secret 패턴 한정 + T-4 test |
| RT-4 | base64 evasion (Tier-1 미커버) | known limitation 명문 (R-5 영구 분리) |
| RT-5 | redaction 성능 (매 송신 45 패턴 매칭) | COMPILED_PATTERNS 재사용 (사전 compile) |

---

## §10 Evidence

- E-1: redaction test green (T-1~T-6) + 커버리지 70%+
- E-2: facade complete() redaction 적용 + Router deferred 순서 검증
- E-3: import-linter green (litellm import 0, 경계 보존)
- E-4: secret_scanner scan-source violations 0
- E-5: jarvis pytest 회귀 0

---

## §11 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | "facade real 완성" over-claim | §0 명칭 정직성 — facade *redaction layer* real, Router deferred ([[feedback_pass_scope_overclaim]]) |
| P-2 | full GP-2 PASS 기정사실화 | full GP-2 PASS = SC-2 (R-1) + SC-3 후 (§0.2 #3) |
| P-3 | catalog 재사용 import 경계 임의 결정 | §2.1 4 옵션 풀 3+1 검증 (권고 (i), fallback (ii)) |
| P-4 | secret_scanner 변경 (R-4.1 위반) | §0.2 #5 — 패턴 변경 0 (재사용만) |
| P-5 | 송신 redaction 정상 내용 손상 | §3 — Tier-1 secret 패턴 한정 + T-4 false positive test |
| P-6 | RT-1 window | §4.2 선부착 보장 (Router deferred = 송신 0) |
| P-7 | 작성자 = 64 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 |

---

## §12 v1.1 흡수 매트릭스 (BLOCKING 4 + 권고 6 1pass)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md` 답습 1pass 흡수 (별도 v2 cycle 0). **4 source 전원 APPROVE WITH CONDITIONS** (codex BLOCKING 2 + Agent A 2 + Agent B 3 + Agent C 2). 방향 견고, 구현 *방식* 정정.

| # | 흡수 | source | 정정 위치 |
|---|------|--------|------|
| B-1 ⭐ | catalog 재사용 (i) src→tools import → **(ii) 공유 모듈 추출** (src 하위 + tools import + 패턴 내용 0 + equivalence test) | codex + Agent B + Agent C (3:1, Reviewer verify) | §2.1 + §5.2 |
| B-2 ⭐ | `[REDACTED]` whole-match → **group-aware 치환** (값만 마스킹, key/구조 보존, secret_scanner = 검출 전용) | Agent A + Agent B + Agent C | §2.2 + §5.1 T-5 |
| B-3 | 송신 redaction 권위 = **governance §4.1 + 64 trajectory** (§8.2 = egress 보조) | codex + Agent B | §0.3 + §3 |
| B-4 | redaction 범위 = **messages + metadata** (full fields system/tools/... deferred) | codex | §3 |
| R-1 | 원본 불변성 test (in-place mutate 0) | codex 1 | §5.1 T-7 |
| R-2 | T-4 false positive edge case fixture | codex 2 + Agent A | §5.1 T-4 |
| R-3 | scrub() KEY_BLACKLIST | codex 3 | §2.2 |
| R-4 | T-6 spy/fake redactor (redaction 선행 입증) | codex 4 | §5.1 T-6 |
| R-5 | redact_messages content list/structured 재귀 | codex 5 | §3 |
| R-6 | group-aware 값 마스킹 (B-2 연계) | Agent C | §2.2 |

**4 source 정합 (positive)**: 명칭 정직성 양호 (facade redaction layer real, full facade real / full GP-2 PASS 아님 — over-claim 0) / RT-1 window 회피 타당 (Router deferred) / Provider Liquidity 보존 (litellm import 0) / 권위 인용 일치 (codex 6/7, §8.2 부분 확장만). pytest 152 green (Agent A 실측) + redaction 성능 ~2.1ms/request.

---

**본 brief v1.1 끝.**

**다음 단계**: **TDD 구현 (RED→GREEN→REFACTOR, catalog (ii) 공유 모듈 + group-aware 치환)** → verify (pytest + import-linter + secret_scanner equivalence + jarvis 회귀) → commit + push → **R-2 facade RedactionFilter prevention layer in-repo operative**. 후속: SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) / SC-Provider Liquidity (Router 위임) = 사용자 명시 별도 sub-cycle.
