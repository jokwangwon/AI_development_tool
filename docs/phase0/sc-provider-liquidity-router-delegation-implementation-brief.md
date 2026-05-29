# SC-Provider Liquidity — facade `complete()` Router 위임 real (Core MVP, mock-verified) 구현 brief (v1.1)

> **작성**: 2026-05-28 (69번째 entry 진입 cycle — 세션 #4)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 8 + 권고 12 1pass 흡수**. 핵심 정정: **CB-1 `complete()` model=alias (litellm_model 모순 정정)** / **CB-2 status flip "Core MVP 구현분리 승인(staged)" 제한 + §15 단계화** / **CB-3 manifest=requirements.txt + sha256/lock diff 의무 + P11 위상 정직 + R-RF2 gate lift 명시** / **CB-4 test_t6 = RT-1 동치검증 대체 + "무회귀" 정정 + T-A 양방향** / **CB-5 redaction 범위 messages+system + metadata_in 통일** / **CB-6 응답 "누출 통로 0" over-claim 정직 축소(set_verbose=False)** / **CB-7 런타임 강등 감지 10 LOC Core 포함(사용자 결정)** / **CB-8 lazy import negative control**. §15 흡수 매트릭스 추가.
>
> **명칭** (Reviewer 채택): **"facade `complete()` Router 위임 real (Core MVP, mock-verified)"** — "Core MVP" + "mock-verified" 명칭 내장.
>
> **scope** (사용자 명시 AskUserQuestion):
> - **구현 = Core MVP**: `complete()` Router 실배선 + `validate_config`(Min 2 + 동일 type) + **런타임 강등 감지 fail-loud(CB-7, ~10 LOC)** + `llm-providers.yaml` + LiteLLM 설치·핀(requirements.txt) + 응답 정규화(`LLMResponse`/`LLMMetadata` 화이트리스트) + RT-1.
> - **DEFER**: streaming(`StreamEvent`) / OAuth single-flight / **degraded *모드*·R4 자동 복구·UI/timer**(감지 fail-loud는 Core) / `DomainMetricsCallback` / 폴백 race 완화.
> - **검증 = Router mock만** (hermetic). 실 LLM 호출 = 수동/별도 (ollama smoke = 권장 evidence, CB-9/R-9).
> - **설계 v2 §17 재합의 = 본 합의 겸함** (staged 조건부 승격, CB-2).
>
> ⚠️ **명칭 정직성 (over-claim 차단 — 세션 #2 4 + #3 2 + #4 1(CB-6) = 누적 7회 cascade 교훈, [[feedback_pass_scope_overclaim]])**: **"full facade real" / "facade 완성" / "Provider Liquidity 완전 발효" / "런타임 검증 완료" 영구 금지**. "operative"는 항상 **"코드 경로상 operative (mock 검증; 실 end-to-end 미입증)"** 병기(R-7). 응답/예외 redaction = deferred — **"송신 경로 누출 0"은 OK, "누출 통로 0"(전 경로)은 over-claim**(CB-6).
>
> **본 cycle = 큰 cycle (실 코드 + 첫 runtime dependency 도입 + 보안/아키텍처 결정)**.
>
> **본 cycle 발효 효과** = facade `complete()` core 경로상 operative (config 기반 provider/model 교체 *코드 경로* 실동작 — 5조-2 실동작 기반; mock 검증, 실 end-to-end 미입증) + 설계 v2 §17 staged 조건부 "확정" 승격.
>
> **선행 답습**: `llm-providers-design.md` (P1 v2 §3/§4/§5/§6/§9.2/§15/§17) + ADR-009 §2 + ADR-008 #3/#4/#5 + 65 SC-1 (RedactionFilter — RT-1 협력자) + governance §1.2.7 P11 + 원본 P1 합의 C-4(차단조건 #5 런타임 재검증)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. 핵심 설계 결정 8건 (D1~D8) — 풀 3+1 검증 통과 (§2)
2. RT-1 redaction 선부착 + 범위(messages+system, CB-5) + 응답 누출 정직 축소(CB-6) (§3)
3. LiteLLM 도입 — requirements.txt manifest + 핀 + sha256/lock diff + P11 위상 정직 (§4)
4. registry yaml + validate_config + 런타임 강등 감지 fail-loud(CB-7) (§5)
5. Router 위임(model=alias, CB-1) + 응답 정규화(LLMMetadata, 속성접근) (§6)
6. 설계 v2 §17 staged 조건부 재합의 folding (§7)
7. TDD 계획 (Router mock, test_t6 대체, T-A 양방향) (§8)
8. 합의 + Liquidity 보존 + 금지 + Rollback + Evidence + 자기진단 + 흡수 매트릭스 (§9~§15)

### §0.2 본 brief 가 *하지 않는* 것 (Core MVP scope 경계)

| # | 영역 | 본 cycle |
|---|------|----|
| 1 | streaming (`stream()`/`StreamEvent`) | 0 (deferred, 명세 존속) |
| 2 | OAuth single-flight lock (§7.2) | 0 (deferred — api_key 경로만) |
| 3 | degraded **모드**·R4 자동 복구·UI 배너·30분 escalation timer (§6.3) | 0 (deferred). **단 런타임 강등 *감지*+fail-loud는 Core 포함 (CB-7)** |
| 4 | `DomainMetricsCallback` (§8.1 메트릭 sink) | 0 (deferred) |
| 5 | 폴백 race 5종 완화 (§5.2) | 0 (deferred — Router 기본 fallback만) |
| 6 | 실 LLM end-to-end 검증 (credential/네트워크) | 0 (mock만; ollama smoke = 권장 evidence) |
| 7 | 65 SC-1 RedactionFilter 패턴 *내용* 변경 | 0 (협력자 재사용) |
| 8 | full GP-2 PASS 재선언 / R-1 canary / R-6 Hermes trigger | 0 |
| 9 | ADR / 헌법 / governance 본문 변경 | 0 (설계 v2 status flip + §15 단계화 + cross-ref만) |
| 10 | 자동 후속 sub-cycle 진입 | 0 (사용자 명시 의무) |
| 11 | P11 전체 enforcement (SBOM / Action SHA pin / Docker digest / auto-recheck) | 0 (Implementation Pending 영구 존속 — 본 cycle은 (i)(ii) *일부*만 조기 발효, CB-3) |

### §0.3 권위 답습 source

- `llm-providers-design.md` §3.1 / §3.3·§6.1 / §4.1 / §4.2 / §4.3 / §5.1 / §9.2 / **§15(v1.0 staged 갱신)** / §17 / **line 76(Min 2 모든 강등 경로 재검증)**
- ADR-009 §2.1 / §2.2 / §2.3 / **§3(v2.0 트리거 4/4 미충족 — LiteLLM 유지)**
- ADR-008 #3 / #4 / #5
- governance §1.2.7 P11 (i)(ii)(v) + **line 280(Implementation Pending)** + §4.5(a)
- `.importlinter` + `requirements-dev.txt`(R-RF2 gate lift 대상) + **원본 P1 합의 C-4**(차단조건 #5 런타임 재검증)
- 65 SC-1 (`redaction.py` + `facade.py` `_redact_request` — RT-1 협력자)

---

## §1 진입 컨텍스트

- 67 GP-2 prevention PASS → 68 roadmap → 세션 #3 종료. carry-over = **SC-Provider Liquidity** (사용자 명시, 세션 #4).
- 현 `facade.py`(61 LOC): redaction layer real(65) + Router 위임 `NotImplementedError` → 실제 LLM 호출 0.
- 본 cycle = Router 위임 deferred 해제 → `complete()` core 경로 operative (mock 검증). 자비스 "로컬 사장 + tmux 워커" 기반 ([[project_jarvis_local_boss_direction]]) + 5조-2 config 교체 *코드 경로* 실동작.

---

## §2 핵심 설계 결정 8건 (D1~D8) — 합의 통과

### D1. `complete()` async 전환 (sync → async) ✅

- 설계 §4.1 = `async def complete`. LiteLLM `acompletion`(async). **caller 0 실측**(`grep .complete( src/`=0, A/C 독립 확인) → breaking 0. **자비스 워커 fan-out 동시성 적합**(R-1, C-3) + caller 0 시점 전환비용 최소. test 1건(`test_redaction_filter.py:105`)만 갱신(CB-4).

### D2. `LLMRequest` 필드 정합 (alias → model_alias + core 필드) ✅

- `model_alias`(rename) + `messages` + `system` + `temperature`(0.7) + `max_tokens`(4096) + `tools` + `tool_choice`/`response_format`/`stop_sequences`(trivial passthrough) + **`metadata_in`**(설계 §4.1 line 217 필드명 통일 — CB-5/codex 권고1). `stream` = deferred.
- 실측: src caller 0 / `test_redaction_filter.py:105` 1건(CB-4 대체) / fixture 독립(영향 0).

### D3. `LLMResponse` 정규화 + `LLMMetadata` 화이트리스트 ✅

- `LLMResponse(content, usage, metadata: LLMMetadata)`. `LLMMetadata`(frozen: provider_used / fallback_chain / finish_reason / request_id).
- **`_normalize` 입력 = 속성 접근 단일화**(`raw.choices[0].message.content` — R-3, litellm `ModelResponse` pydantic). mock fake Router도 *속성 인터페이스* 노출(dict mock 금지).
- **`usage`도 명시 키만 추출**(`{input_tokens, output_tokens}` — provider 고유 키 `prompt_tokens_details` 등 차단, raw usage dict 통과 0 — R-4).

### D4. LiteLLM 도입 형식 — requirements.txt manifest + 핀 + supply-chain ✅ (CB-3)

- **manifest = `requirements.txt`(runtime 신규)** — pyproject 기각(R-RF2 "별도 합의" gate 회피 + 기존 핀 컨벤션 + `--require-hashes` native). **R-RF2 gate lift = 본 합의 명시 결정 항목**(암묵 금지). 상세 §4.

### D5. `validate_config` — Min 2 active + 동일 type 금지 (시작 fail-fast) ✅

- active ≥ 2(ADR-008 #5) + active 동일 type 2개 금지(R5). + 엣지케이스(type/status 필드 누락, malformed → ConfigError — R-5). 상세 §5.2.

### D6. `llm-providers.yaml` registry (repo 루트) ✅

- 단일 파일(**repo 루트** — `config/` 미신설, R-11). `defaults` + `routing` + `providers`(type/litellm_model/auth_method/api_key_env/status). api_key 평문 금지(env 보간) + OAuth `metadata_in` 경로 env(standby 스키마만). 상세 §5.1.

### D7. 에러 분류 + 런타임 강등 감지 fail-loud (CB-7) ✅

- `litellm.AuthenticationError`/`RateLimitError`/`ServiceUnavailableError`/`BadRequestError` 인지. **Core MVP + CB-7**: `AuthenticationError`/`ServiceUnavailableError` 경로에서 **active 카운트 재계산 → <2 면 명시 예외 raise + stderr 경고**(fail-loud ~10 LOC). **degraded *모드*/자동복구/UI/timer = deferred**. Router fallback/num_retries는 Router 설정 위임. 상세 §6.2.

### D8. `health()` — 축소 fallback (R-2) ✅

- 현 stub `{}` → **축소 fallback**: "active alias 목록 + config validation 결과" 반환(`dict[str, bool]` 타입 고정). 실 LiteLLM dry probe API 형태 불명 → dry probe 실배선 deferred(설계 §9.2 명세 존속). R-2/codex 권고2.

---

## §3 RT-1 redaction 선부착 + 범위 + 응답 누출 정직 (보안 핵심)

### §3.1 RT-1 선부착 (미부착 window 0)

- 현 `complete()`: `_redact_request(req)` → `NotImplementedError` (redaction이 Router 위임 *전* 위치).
- 본 cycle: `redacted = self._redact_request(req)` → `raw = await self._router.acompletion(model=provider_key, messages=redacted["messages"], **redacted_opts)`. **redacted body가 Router 인자로 전달** → window 0.

### §3.2 redaction 범위 (CB-5 — messages + system + outbound text)

- **redaction 대상 = 모든 outbound text field**: `messages` + `system` + (`tools` 내 문자열) + `metadata_in`. 단순 `messages`만이면 system/tools에 secret 누출 가능(codex BLOCKING 1).
- redacted `metadata_in` 행선지: **request_id만 추출 → `LLMMetadata`**, 나머지는 `acompletion(metadata=)` **미전달**(callback deferred = metadata sink 0). 명시적 drop.

### §3.3 응답/예외 redaction — 정직 축소 (CB-6 — over-claim 차단)

- ⭐ **"누출 통로 0"(전 경로) 단정 철회**. 정직 재서술:
  - **송신 경로(request body) 누출 0** (§3.1/§3.2 redaction operative).
  - **litellm 내장 로깅 비활성 의무**: `litellm.set_verbose=False`(또는 동등) `_build_router()`에서 설정 + **test 강제**(litellm 내장 로깅이 응답/요청을 stdout/파일로 흘리지 않음).
  - **응답/예외 경로 redaction = deferred** (metrics callback 동반, 별도 sub-cycle). re-raise되는 litellm 예외 본문(endpoint/key fragment)은 본 cycle redaction 대상 아님 — caller 책임 경계 + 별도 sub-cycle 명문.
- detection≠prevention가 *응답 경로*에도 적용 ([[feedback_pass_scope_overclaim]]).

---

## §4 LiteLLM 도입 — requirements.txt manifest + 핀 + supply-chain (CB-3)

### §4.1 import / 설치 전략 (hermetic — lazy import + Router 주입)

- top-level `import litellm` = 미설치 시 facade import 실패 → 주입 테스트도 실패.
- **lazy import + Router 주입**: `LLMFacade.__init__(self, registry_path_or_config, *, redactor=None, router=None)`. `router is None`이면 `_build_router()` 내부 `import litellm` → `litellm.Router(...)`. 테스트 = fake router 주입 → **litellm import 0 = 미설치 hermetic** (A 실측: grimp 함수-레벨 import facade 귀속 + 모듈 import 시 미발화, `/tmp/lazytest`).
- import-linter: lazy import도 facade 발신 = `ignore_imports = facade -> *` 면제 → 계약 PASS. **CB-8 verify 의무**: (a) lazy import + litellm 미설치 PASS 실측 + (b) facade 외부 의도적 lazy import → 계약 FAIL (negative control). 둘 다 §8.3 E-3.
- 순수 DI(외부 router factory) = ADR-009 §2.2 #1("litellm import = facade 한 파일") 누출 → **기각**(C-2). lazy import는 facade 내부 = 의무 충족(위치만 함수 내부).
- 설계 §4.1 top-level 예시 deviation = §17 folding에서 "facade 한정 import 충족, 위치만 함수 내부"로 정정(설계 §4.1 주석).

### §4.2 manifest + 핀 + supply-chain (CB-3 — 4 source 수렴)

| 항목 | 본 cycle 처리 | 권위 |
|------|----|----|
| manifest | **`requirements.txt`(runtime 신규)** 결정 (pyproject 기각) | R-RF2 gate / C-1 |
| **R-RF2 gate lift** | "runtime 의존성 0건 / pyproject 별도 합의" gate lift = **본 합의 명시 결정** (암묵 금지) | requirements-dev.txt:8~9 |
| 버전 핀 | litellm `==<정확 버전>` | ADR-008 #3 |
| Apache 2.0 | 라이센스 재확인 | ADR-009 §2.1(c) |
| **hash** | **litellm 직접 핀 sha256 + lock diff 회귀 = 비협상 의무**(P11 i/v). transitive 전체 hash = 비례성 평가 후 결정(미결정 금지 — best-effort 명문) | P11 (ii)(i)(v) |
| **P11 위상 정직** | 본 cycle = P11 **(i)(ii) 일부 조기 발효**. 전체 enforcement(SBOM/Action SHA/Docker digest/auto-recheck) = governance §1.2.7 **Implementation Pending 영구 존속**(over-claim 차단) | governance:280 |

→ 개인 툴 비례성([[feedback_proportionate_security_personal_tool]]) ↔ supply-chain gate(P11). 비례성 = *과잉 ceremony 회피*이지 *gate 생략 아님*(C-B2).

---

## §5 registry yaml + validate_config

### §5.1 `llm-providers.yaml` (repo 루트 — R-11)

```yaml
defaults: { primary: anthropic-claude-api, secondary: ollama-llama-local }
routing: { default: anthropic-claude-api, background_jobs: ollama-llama-local }
providers:
  anthropic-claude-api: { type: anthropic, litellm_model: anthropic/claude-opus-4-7, auth_method: api_key, api_key_env: ANTHROPIC_API_KEY, status: active }
  ollama-llama-local:    { type: ollama,    litellm_model: ollama/llama-3.3-70b,     auth_method: none, endpoint: http://localhost:11434, status: active }
```

- active 2종 다른 type(anthropic + ollama) → Min 2 + 동일 type 금지 충족. standby/blocked/deprecated 스키마 포함(degraded 전이 deferred).

### §5.2 `validate_config` (시작 fail-fast + 엣지케이스 R-5)

```python
def validate_config(config):
    providers = config.get("providers") or {}
    active = [(k, v) for k, v in providers.items() if v.get("status") == "active"]
    if len(active) < 2: raise ConfigError("Min 2 active 위반 — ADR-008 #5")
    types = [v.get("type") for _, v in active]
    if None in types: raise ConfigError("active provider type 필드 누락")
    if len(set(types)) != len(types): raise ConfigError("동일 type 2개 active 금지 — R5")
```

- 시작 1회(`__init__`). type/status 누락 → ConfigError(R-5). **런타임 강등 *감지*는 §6.2(CB-7)** — 시작-한정 아님.
- **실 키 부재 동작**(R-6): validate_config는 status/type만 검증 → 실 키 부재여도 PASS(시작). 첫 `acompletion`에서 AuthenticationError(§6.2). **"Min2 PASS ≠ 실 호출 가능"** 명문(mock 검증 = 실 키 부재 정상 경로).

---

## §6 Router 위임 + 응답 정규화 + 강등 감지

### §6.1 `to_router_config` (CB-1 + R-12)

- `llm-providers.yaml` → Router `model_list`[{`model_name`=**alias**, `litellm_params`={`model`=litellm_model, `api_key`=`os.environ.get(api_key_env)`}}] + `router_settings`(fallbacks, num_retries, timeout). **`api_key_env` → 실값 보간**(R-12 — litellm은 api_key 실값 기대, env 키 자동해석 안 함; ollama=none은 endpoint만). cooldown/고급 = deferred.

### §6.2 `complete()` 흐름 (Core MVP + CB-1 + CB-7)

```
1. provider_key = routing.get(req.model_alias, routing["default"])   # = model_name = alias
2. redacted = self._redact_request(req)                              # RT-1 (Router 전) — messages+system+metadata_in
3. raw = await self._router.acompletion(model=provider_key,          # ⭐ CB-1: model=alias (litellm_model 아님)
                                        messages=redacted["messages"], **redacted_opts)
   except (AuthenticationError | ServiceUnavailableError) as e:      # ⭐ CB-7: 런타임 강등 감지
       if self._count_active() < 2:
           raise DegradedError("active<2 (런타임 강등) — 차단조건 #5 fail-loud") + stderr 경고
       raise
4. return self._normalize(raw, provider_key)                         # LLMResponse + LLMMetadata (속성접근)
```

- **CB-1**: `model=provider_key`(=alias=model_name) → Router fallback/routing 정상. `litellm_model`은 `to_router_config` 내부에만(complete() 노출 0, 위반패턴 #1 회피).
- **CB-7**: 강등 *감지*+fail-loud(~10 LOC). degraded *모드*/복구/UI/timer deferred. **차단조건 #5 = "시작 fail-fast + 런타임 강등 감지(fail-loud); 자동 복구/모드/UI = deferred" — 부분 충족 정직 표기**(무수식 "충족" 금지).

### §6.3 `_normalize` (R-3 / R-4)

- `content = raw.choices[0].message.content`(속성). `usage = {input_tokens, output_tokens}`(명시 키만). `LLMMetadata(provider_used, fallback_chain, finish_reason, request_id)`. raw dict/usage 통과 0.

---

## §7 설계 v2 §17 staged 조건부 재합의 folding (CB-2)

- 본 풀 3+1이 §17 체크리스트 수행 → 통과 시 status flip. **단 CB-2 — "단순 확정" 금지**:
  - status = **"확정 v2 / Core MVP 구현분리 승인 (staged implementation 허용)"**.
  - **설계 §15 v1.0 row 갱신**(본 합의 산출 포함): "v1.0(MVP) = 12 보강 모두" → **"v1.0 Core MVP(complete 경로 + Min2 + 강등 감지) + 12 보강 단계화(streaming/OAuth/degraded 모드/race/metrics = deferred phase, 명세 존속)"**.
- deferred 항목 = **"설계 명세 존속 + 구현 deferred"**(삭제 아님). §17 Agent A/B/C/Reviewer 항목 판정표 = 합의 보고서 §(각 Agent §5).
- ADR/헌법/governance 본문 변경 0 — 설계 §6/§15 + status + cross-ref만(T3 회피).

---

## §8 TDD 계획 (Router mock — RED → GREEN → REFACTOR)

### §8.1 RED — `tests/adapters/llm/test_facade_router.py` (신규) + `test_redaction_filter.py` test_t6 대체(CB-4)

- **T-A ⭐ (RT-1 양방향, CB-4)**: 실 `RedactionFilter()` + secret(`sk-ant-...`) 포함 messages+system → fake Router 주입 → captured `messages`/`system`에 **원본 secret 문자열 부재 AND `REDACTION_MARK` 존재**(양방향 — 한쪽만 = trap). **현 `test_t6`(line 92~109)를 본 T-A로 *대체/migration***(spy "호출됨" trap + `NotImplementedError` 전제 폐기).
- **T-B (CB-1)**: 정상 경로 → fake Router가 받은 `model` 인자 = **alias**(=provider_key) 단언 + `LLMResponse(content, usage, LLMMetadata)` 정규화(속성접근, raw 누출 0).
- **T-C (R-5)**: `validate_config` — active 1개 → ConfigError; 동일 type 2개 → ConfigError; type/status 누락 → ConfigError.
- **T-D**: 정상 2 active 다른 type → pass.
- **T-E (CB-7)**: fake Router `AuthenticationError` raise + active<2 → `DegradedError` raise + stderr. active≥2 → 원 예외 re-raise.
- **T-F (D2/D3)**: `LLMRequest(model_alias=, metadata_in=)` + `LLMMetadata` frozen 화이트리스트(raw 키 거부).
- **T-G (D6/CB-1)**: yaml 로드 → `to_router_config` `model_list[].model_name=alias` + `api_key` 보간.
- **T-H (hermetic)**: litellm 미설치에서 facade import + 위 test green + **`import facade; 'litellm' not in sys.modules`** 단언(R-A4 — top-level 회귀 시 RED).
- **T-I (CB-6)**: `_build_router()`가 `litellm.set_verbose=False` 설정 (litellm 내장 로깅 비활성).
- **T-J (65 회귀)**: redaction 순수함수 7건(T-1~T-5,T-7,T-8) 회귀 0. **(CB-4: test_t6은 T-A로 대체 — "15 test 무회귀" 아님)**.

### §8.2 GREEN

- `facade.py`: lazy litellm import + Router 주입 + async `complete()`(model=alias) + 강등 감지(CB-7) + `validate_config` + `to_router_config`(api_key 보간) + `_normalize`(속성) + `LLMRequest`(model_alias/metadata_in)/`LLMResponse`/`LLMMetadata` + `set_verbose=False`.
- `llm-providers.yaml`(repo 루트) + `requirements.txt`(runtime, litellm 핀 + sha256) + `requirements-dev.txt`에 `pytest-asyncio` 추가(R-8).
- registry 로드(facade 내부 또는 `registry.py`).

### §8.3 REFACTOR + verify

- 커버리지 70%+. frozen/순수성.
- **verify**: `.venv/bin/python -m pytest tests/ -q`(baseline 167 → test_t6 대체 + 신규 T-A~T-J 반영 재계산, R-10) / **import-linter (CB-8 negative control 포함)** / secret_scanner scan-source 0 / (R-9 권장) ollama 가용 시 실 `litellm.Router` + ollama 호출 1건 smoke(credential 불요) — 미가용 시 "litellm.Router 인터페이스 정합 = 실 호출까지 미입증" 공백 명문.

---

## §9 합의 형태 + 승격 트리거

| # | trigger | 발화 |
|---|---------|----|
| 1 | 아키텍처(Router 위임 + manifest) | ✅ |
| 2 | SDD 명세(§17 folding) | ✅ |
| 3 | 보안(RT-1 + P11 + credential env + CB-7 #5) | ✅ |
| 4 | 실 코드 + 첫 runtime dep | ✅ |
| 5 | Provider Liquidity 5조-2 (cross-vendor 외부 LLM) | ✅ |

→ 5/5 → 풀 3+1 + 외부 LLM 1+ 의무. **본 brief v1.1 = 합의 통과 (4 source APPROVE WITH CONDITIONS, BLOCKING 8 1pass 흡수)**.

---

## §10 Provider Liquidity 보존 (ADR-009 §2.2/§2.3, 5조-2)

- litellm import = facade.py 한정(lazy도 facade 내부, import-linter PASS + CB-8 negative control). 모델명 = yaml만(complete() model=alias, 위반패턴 #1 0). `LLMMetadata`/`usage` 화이트리스트(위반패턴 #2/#4). Hermes ↔ provider 분리(§2.3). LiteLLM 유지(ADR-009 §3 v2.0 트리거 4/4 미충족 — C-7).

---

## §11 금지 사항

§0.2(11) 답습. 추가: "full facade real / 완성 / 완전 발효 / 런타임 검증 완료" 표현 0 / **"누출 통로 0"(전 경로) 0**(CB-6, 송신 경로만 OK) / 무수식 "차단조건 #5 충족" 0(부분 충족 표기, CB-7) / 실 API 호출·credential 0 / 65 패턴 내용 변경 0 / P11 전체 enforcement 충족 주장 0 / 자동 후속 0.

---

## §12 Rollback Trigger

| # | trigger | 대응 |
|---|---------|----|
| RT-1 | redaction이 Router 위임 후로 밀림 | §3.1 redacted body Router 인자 + T-A 양방향 동치 |
| RT-2 | litellm 미설치 → facade import 실패 | §4.1 lazy import + 주입(T-H) |
| RT-3 | `alias` rename breaking | src 0 / test_t6 대체(CB-4) |
| RT-4 | CB-1 model=litellm_model 회귀 → 라우팅 무력화 | §6.1/§6.2 model=alias + T-B/T-G 단언 |
| RT-5 | manifest hash 과도 ceremony | §4.2 직접핀 의무 + transitive best-effort(비례성) |
| RT-6 | health dry probe API 불명 | §2 D8 축소 fallback(R-2) |
| RT-7 | 런타임 강등 무방비(차단조건 #5) | §6.2 감지 fail-loud(CB-7) + #5 부분 충족 표기 |
| RT-8 | 응답/예외 secret 누출 | §3.3 set_verbose=False(T-I) + 응답 redaction deferred 명문(CB-6) |
| RT-9 | lazy import가 GP-5 Layer 1 약화 | §4.1 negative control(CB-8) FAIL 실측 |

---

## §13 Evidence

- E-1: facade test green(T-A~T-J) + 커버리지 70%+ (RT-1 T-A 양방향)
- E-2: `validate_config` Min2 + 동일 type + 필드누락 fail-fast (T-C/T-D)
- E-3: **import-linter green (lazy PASS 실측 + facade 외부 negative control FAIL — CB-8)**
- E-4: redaction 순수함수 7건(T-1~T-5,T-7,T-8) 회귀 0 + **test_t6 = T-A 대체**(CB-4) + jarvis pytest 회귀 0 (baseline 167 재계산, R-10)
- E-5: `llm-providers.yaml`(루트) 로드 + `to_router_config` model_name=alias(T-G) + secret_scanner scan-source 0
- E-6: 설계 v2 §17 staged 판정표 → status flip 근거(CB-2)
- E-7: `set_verbose=False`(T-I) + `requirements.txt` litellm 핀+sha256
- E-8: (R-9 권장) ollama smoke 1건(가용 시) — 미가용 시 인터페이스 정합 미입증 공백 명문

---

## §14 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | "full facade real / 완성" over-claim | §0 명칭 — core 경로 + Core MVP/mock-verified 내장 ([[feedback_pass_scope_overclaim]]) |
| P-2 | "실 호출 검증 완료" over-claim | mock만 + ollama smoke 권장(E-8) |
| P-3 | "Provider Liquidity 완전 발효" | 코드 경로 operative ≠ 5-way 완결(ADR-009 §5) |
| P-4 | "누출 통로 0" 응답 경로 over-claim | CB-6 — 송신만 0, 응답/예외 deferred + set_verbose |
| P-5 | "차단조건 #5 충족" over-claim | CB-7 — 부분 충족(시작+감지, 복구/모드 deferred) |
| P-6 | P11 전체 충족 over-claim | CB-3 — (i)(ii) 일부, 전체 Pending 존속 |
| P-7 | manifest/hash 과도 ceremony | §4.2 비례성(개인 툴) |
| P-8 | 65 RedactionFilter 변경 유혹 | 협력자 재사용만, 패턴 내용 0 |
| P-9 | RT-1 단순 "호출됨" trap | T-A 양방향(원본 부재 AND MARK 존재) |
| P-10 | 작성자 = Claude single-vendor cascade | cross-vendor codex + 풀 3+1 독립(누적 7회 catch) |

---

## §15 v1.1 흡수 매트릭스 (BLOCKING 8 + 권고 12 1pass)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md` 답습 1pass 흡수(별도 v2 cycle 0). **4 source 전원 APPROVE WITH CONDITIONS**.

| # | 흡수 | source | 위치 |
|---|------|--------|------|
| CB-1 ⭐⭐ | `complete()` model=alias (litellm_model 모순 정정) | A + codex (2 수렴) | §6.1/§6.2 + T-B/T-G |
| CB-2 ⭐⭐⭐ | status flip "Core MVP 구현분리 승인(staged)" + §15 단계화 | B + C + codex (3 수렴) | §7 |
| CB-3 ⭐⭐⭐⭐ | manifest=requirements.txt + sha256/lock diff 의무 + P11 위상 정직 + R-RF2 gate lift 명시 | 4 source 전원 | §4.2 |
| CB-4 ⭐⭐ | test_t6 = RT-1 동치검증 대체 + "무회귀" 정정 + T-A 양방향 | A + B (2 수렴) | §8.1 T-A/T-J + E-4 |
| CB-5 ⭐⭐ | redaction 범위 messages+system+metadata_in + 행선지 + 필드명 통일 | codex + A (2 수렴) | §3.2 + D2 |
| CB-6 ⭐⭐ (over-claim) | "누출 통로 0" → 송신만 0 + set_verbose=False + 응답/예외 deferred | B (C 부분이견, Reviewer B 채택) | §3.3 + T-I |
| CB-7 ⭐⭐ (scope) | 런타임 강등 감지 fail-loud 10 LOC Core(사용자 결정) + #5 부분충족 정직 | C (design-authority) | §6.2 + D7 |
| CB-8 ⭐ (verify) | lazy import PASS 실측 + facade 외부 negative control FAIL | C (A positive half) | §4.1 + §8.3 E-3 |
| R-1 | async fan-out 동시성 근거 | A/C/codex | D1 |
| R-2 | health 축소 fallback + dict[str,bool] | A/B/C/codex | D8 |
| R-3 | _normalize 속성접근 단일화 + mock 속성 인터페이스 | C + A | D3/§6.3 |
| R-4 | usage 명시 키 추출(raw 통과 0) | B | D3/§6.3 |
| R-5 | validate_config 엣지케이스(필드 누락 → ConfigError) | B | §5.2/T-C |
| R-6 | 실 키 부재 동작(Min2 PASS ≠ 실 호출) | B | §5.2 |
| R-7 | "operative" 항상 mock 한정 병기 | B | §0 |
| R-8 | pytest-asyncio dev-dep 추가 | B | §8.2 |
| R-9 | ollama smoke 권장 evidence 격상 | C | §8.3/E-8 |
| R-10 | "15 test" 수치 명확화(8 def + parametrize, baseline 167) | B + A | §8.3/E-4 |
| R-11 | registry yaml repo 루트 | C | §5.1/D6 |
| R-12 | api_key_env os.environ 보간 | A | §6.1 |

**4 source 정합(positive)**: over-claim 차단 framing 양호(4 source 공통, "full/완성/완전/런타임 완료" 4종 금지) + 권위 인용 정확(codex cross-verify 대부분 일치) + async/LiteLLM 유지 타당 + A 실측(pytest 167, grimp lazy 귀속, redaction 0.193ms/call). over-claim catch 1건(CB-6) = 본 세션 #4 첫 포착(누적 7회).

---

**본 brief v1.1 끝.**

**다음 단계**: TDD 구현(RED→GREEN→REFACTOR, Router mock, test_t6 대체, model=alias, 강등 감지, redaction 범위, set_verbose) → verify(negative control + 커버리지 70%+ + jarvis 회귀) → 정리 commit + push → **facade `complete()` Router 위임 real (Core MVP, mock-verified)**. 후속: streaming / OAuth / degraded 모드 / metrics = 사용자 명시 별도 sub-cycle.
