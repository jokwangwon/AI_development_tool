# 3+1 합의 — boss/worker facade 통합 (트랙 B → facade.complete()) — Agent C (대안 탐색가)

> **cycle**: 70번째 entry 진입 (세션 #4) — `OllamaBoss`/`OllamaWorker` urllib 직호출 → `facade.complete()` 경유 전환
> **lens**: "더 나은 방법이 있는가?" — 대안 기술 / 트레이드오프 / scope 경계
> **작성**: 2026-05-28 / Agent C / Phase 2 독립 (Agent A/B/codex 미참조)
> **대상**: `docs/phase0/boss-worker-facade-consolidation-brief.md` (v1)
> **직접 read 답습**: boss.py / worker.py / facade.py / redaction.py / llm-providers.yaml / orchestrator.py / ADR-009 §2.2·§3 / test_ollama_boss.py / test_ollama_worker.py / .importlinter / examples/*.py(6)

---

## 판정: **APPROVE WITH CONDITIONS**

통합 방향(트랙 B 번복)은 ADR-009 §2.2 단일 진입점 의무 + 헌법 5조-2 Provider Liquidity + RT-1 보안 확장 관점에서 **정당**하며 더 나은 구조적 대안 없음(아래 §대안 평가). D2 sync(asyncio.run) 선택은 자비스 동기 orchestrator 흐름에 **최적**(기존 `test_facade_router.py` 전체가 `asyncio.run` 패턴 답습 — convention 일관). 단 **scope 경계 1건이 실측상 부정확**(examples 6 파일 누락) + D4 rename 트레이드오프가 미해소 상태로 합의 위임 — BLOCKING 2 + 권고 5.

---

## BLOCKING (번호 + file:line + 대안)

### B-C1 — D1/D4 "src 내 instantiation 0" claim 이 examples 6 파일을 누락 (scope 정직성 over-claim)
- **근거**: brief §2 D1 line 62 "외부 wiring + 2 test만 영향, **src 내 instantiation 0 실측**" + D4 line 73 "rename = 2 test + 외부 wiring 영향" + line 138 RT-5 "src 내 instantiation 0".
- **실측 반증**: `OllamaBoss(model=...)` / `OllamaWorker(alias=..., model=...)` 가 **examples/ 6 파일에서 직접 instantiate**:
  - `examples/jarvis_v00_glm_worker.py:74` (`OllamaWorker(alias=, model=, output_filename=)`) + `:82` (`OllamaBoss(model=, timeout_s=)`)
  - `examples/jarvis_v00_codex_worker.py:135` (`OllamaBoss(model=, timeout_s=)`)
  - `examples/jarvis_v00_claude_worker.py:86`
  - `examples/jarvis_v00_layer0_memory.py:55`
  - `examples/jarvis_v00_round_trip.py:61`
  - `examples/jarvis_v00_dev_task.py:62`
- **2중 파괴**: 이 6 파일은 (a) D1 의 `model`→`model_alias` rename + 필수 `facade` 인자 추가, (b) D4 의 클래스 rename — **둘 다에 의해 깨진다**. brief 의 "외부 wiring 은 사용자 영역"(RT-5 line 138) framing 은 src 내부 = 0 이라 정당하나, **examples 는 repo-in 자산**(`git ls-files`)이며 worker.py docstring line 10 이 직접 `OllamaWorker model 인자 교체` 를 사용 예시로 명문.
- **검증 green ≠ 정확 위험 ⭐**: examples 는 testpaths/CI 미포함(실측: tests/·.github/ 에 `examples/` 참조 0). 따라서 brief E-1/E-2(jarvis 144 green) **PASS 하면서도 6 entry point 가 silent 하게 import-time/runtime 파괴** → "verify green = 통합 완료" over-claim 으로 이어진다(P-1 인접).
- **요구**: §0.2 scope 표 또는 §2 D1 에 **examples 6 파일 처리 방침 명문** — 택1:
  1. **examples 동반 수정**(facade build wiring 추가 — 권장: 사용자 단일 사용자 데모 = facade 주입 패턴 시연 가치) 을 scope 에 포함, 또는
  2. **examples = out-of-scope known-breakage** 명시 + INDEX/세션에 "70 entry 후 examples 6 wiring 갱신 필요" carry-over 등록(silent 파괴 방지).
- **금지**: "src 내 0 → 영향 0" 추론(P-1 over-claim 재발).

### B-C2 — D2 RT-2 fallback("asyncio.new_event_loop")이 nested-loop 를 *실제로* 해소하지 못함(잘못된 안전 주장)
- **근거**: brief §9 RT-2 line 135 "asyncio.run 내부 호출이 기존 이벤트 루프와 충돌(중첩 루프) → 충돌 시 **asyncio.new_event_loop fallback**".
- **기술적 결함**: `asyncio.run()` 이 `RuntimeError: asyncio.run() cannot be called from a running event loop` 를 던지는 상황 = *이미 실행 중인 루프 안*. 이때 `asyncio.new_event_loop()` 로 새 루프를 만들어 `run_until_complete` 해도, **같은 스레드에 실행 중 루프가 있으면 동일 RuntimeError** 또는 루프 재진입 미정의 동작. 표준 해소책은 (a) 별도 스레드에서 `asyncio.run`, 또는 (b) `nest_asyncio`(외부 dep — 비례성 위반 후보), 또는 (c) **애초에 nested 진입을 구조적으로 차단**.
- **실측 정상 경로 = nested 없음**: orchestrator.py 전체 + `src/jarvis/` 전체에 `asyncio`/`async def`/`await` **0건**(실측). orchestrator `dispatch`(line 120)·`_advise`(line 112)·`worker.run`(line 125) 모두 top-level sync 진입. 따라서 **정상 경로에선 nested loop 가 발생하지 않음**(RT-2 trigger 자체가 거의 불가).
- **요구**: RT-2 를 **"nested 진입 = 구조적 0(orchestrator sync 실측), fallback 코드 작성 0 — nested 발생 = 호출 계약 위반으로 fail-loud(억지 봉합 금지)"** 로 정정. `new_event_loop` fallback 은 **삭제**(잘못된 안전감 + 미정의 동작 유발). 만약 미래 async caller 가 생기면 그것은 D2 재설계 trigger(별도 cycle)이지 본 cycle fallback 대상 아님.
- **대안(권장)**: 자비스 단일 사용자 sync 툴 = `asyncio.run` 1회/호출이 정확. 굳이 robust 하게 하려면 모듈 레벨 helper `_run_sync(coro)` 가 `try: asyncio.get_running_loop()` 로 **실행 중 루프 감지 시 명시 RuntimeError**(fail-loud) — 묵시 fallback 금지.

---

## 권고 (대안 제시 — non-blocking)

### R-C1 — D4 rename: "현 명칭 유지 + docstring 정정" 이 비례성상 우월(잠정 rename 권고 재고)
- **brief 잠정**: line 73 "rename 권고, 합의 확정" (`OllamaBoss`→`LLMBoss`/`FacadeBoss`).
- **대안 트레이드오프 분석**:

  | 안 | provider-neutral(위반패턴 #1) | rename 비용 | known-limitation |
  |----|----|----|----|
  | (A) rename `LLMBoss`/`LLMWorker` | ✅ 식별자에서 provider 제거 | **2 test + 6 examples + worker.py docstring line 10** 동시 갱신(B-C1 와 결합 시 파괴면 ↑) | 명칭이 추상 수준만 표현(`LLM`=의미적 명칭) |
  | (B) 현 명칭 유지 + docstring 정정 | ⚠️ `Ollama` 잔존 — **단 위반패턴 #1 = "코드 *분기/라우팅* 식별자에 provider 인코딩"**(`if model=="claude"`, llm-providers-design.md §9). **클래스 *명칭* 은 분기 로직 아님** → 위반패턴 #1 *본문* 직접 위반 아님(인접) | 최소(0 rename) | 명칭이 역사적 출처(Ollama 트랙) 보존 — 단 facade 경유 후 routing 은 model_alias 가 결정(명칭과 무관) |
  | (C) `FacadeBoss`/`FacadeWorker` | ✅ | (A)와 동일 | 명칭이 *구현 수단*(facade) 인코딩 — 또 다른 결합(facade 교체 시 또 rename) → **(A) `LLMBoss` 가 (C)보다 우월** |

- **권고**: 위반패턴 #1 의 *본질* = "**provider 교체 시 코드 변경 강제**"(헌법 5조-2). 명칭 `OllamaBoss` 는 **routing 을 강제하지 않음**(model_alias 가 routing, 명칭은 라벨) → 위반패턴 #1 본문 위반 아님. 따라서 **(B) 현 명칭 유지 + docstring 정정**(트랙 B urllib 직결 → facade 경유 사실 반영)이 **비례성상 최소 비용 + B-C1 파괴면 최소화**로 우월. rename 을 강행한다면 **(A) `LLMBoss`/`LLMWorker`**(추상 수준 명칭, 수단 비인코딩) 채택하되 **B-C1 examples 동반 갱신과 묶음 처리** 필수. **(C) Facade* 는 비채택 권고**(수단 인코딩 = 또 다른 lock-in).
- **단일 사용자 비례성**: 개인 자비스 = 외부 API 안정성 부담 0. rename 의 유일 이득(식별자 정직성)이 6 examples + docstring 갱신 비용 + B-C1 파괴면 확대 비용을 넘는지 사용자 판단 영역 — Agent C 잠정 = **(B) 우선, rename 보류**.

### R-C2 — D5 registry alias: "기존 `ollama-llama-local` 재사용" 우선(신규 alias 추가는 Min 2 검증 부담)
- **근거**: llm-providers.yaml line 28~33 `ollama-llama-local`(active, type=ollama, endpoint localhost:11434) 이미 존재 + line 17~18 `routing.background_jobs: ollama-llama-local` 매핑.
- **대안 트레이드오프**:
  - (A) 기존 `ollama-llama-local` 재사용 + `routing` 에 `jarvis_worker`/`jarvis_boss` alias 만 추가(→ 동일 provider key 매핑): providers `active` 집합 **불변** → `validate_config`(facade line 75) Min 2 + 동일 type 금지 **무영향**(실측: active 2 = anthropic+ollama, type 상이). **가장 안전**.
  - (B) 워커 전용 ollama provider 신규 추가: active 집합 변동 → Min 2 보존되나 **동일 type(ollama) 2개 active = `validate_config` line 85 ConfigError**(`동일 type 2개 active 금지`) 위험. brief §4 line 76 "동일 type 금지 보존" 은 인지하나, 신규 ollama provider 를 `active` 로 올리면 **즉시 위반**. standby 로만 추가 가능(routing 불가 — facade `_resolve` 는 providers/routing 만 조회).
- **권고**: **(A) 기존 재사용 + routing alias 만 추가** 채택. brief §4 "또는 기존 active alias 재사용" 을 **기본값으로 승격**, "워커 전용 모델 추가" 는 동일-type 함정 명문(active 금지 → standby 시 routing 불가)과 함께 보류. boss/worker 가 서로 다른 ollama 모델을 원하면 → **routing alias 2개가 같은 provider key 가리키되 model 은 provider 의 litellm_model 단일**(현 registry 구조상 alias 별 모델 분기 불가 — 이건 D5 의 *숨은 제약*, R-C3 참조).

### R-C3 — D1 `model`→`model_alias` 의 의미 변화 명문(boss/worker 별 모델 선택 능력 상실 가능성)
- **현 구조**: `OllamaBoss(model="qwen3-30b...")` / `OllamaWorker(model="glm-4.7...")` = **인스턴스별 임의 Ollama 모델명 자유 지정**(boss=Qwen, worker=GLM 처럼 *다른* 로컬 모델 — examples 가 실제로 그렇게 사용: glm_worker.py 가 `--worker-model` + `--boss-model` 분리).
- **facade 경유 후**: `model_alias` = registry routing 키 → 실제 모델은 `providers[key].litellm_model` **단일 고정**. 즉 **alias 1개 = 모델 1개**. boss/worker 가 다른 로컬 모델을 쓰려면 **registry 에 ollama provider 2개 필요** → 그러나 R-C2 의 동일-type-active 함정에 걸림(둘 다 active 불가).
- **트레이드오프 명문 요구**: 본 통합은 "boss/worker 가 임의 Ollama 모델명을 런타임 자유 지정" → "registry 가 사전 정의한 alias→모델 단일 매핑" 으로 **유연성 1단계 감소**(Provider Liquidity 의 의도된 trade — 코드 자유도↓, config 중앙화↑). 이는 ADR-009 §2.2 #3(모델명 분기 금지) 답습상 **올바른 방향**이나, examples 의 `--boss-model`/`--worker-model` CLI 인자가 **무의미해진다**(B-C1 와 결합). brief §2 D1 에 "model_alias 도입 = 인스턴스별 임의 모델명 지정 능력 → registry alias 사전 정의로 전환(의도된 유연성 trade)" 명문 권고.
- **대안**: 만약 boss=Qwen / worker=GLM 의 *다른 모델* 사용이 자비스 핵심 요구라면(MEMORY: 로컬 사장+tmux 워커 방향) → registry 가 alias 별 모델 override 를 지원해야 함(현 `to_router_config` line 96~104 = provider 단위 litellm_model 단일). 이건 **facade/registry 설계 영역**(본 cycle scope 밖) → §0.2 에 "boss/worker 별 상이 로컬 모델 = registry alias 별 모델 분기 필요 시 별도 cycle" carry-over 권고.

### R-C4 — 점진(boss 먼저 → worker) vs 동시(c) 트레이드오프: 동시 적정, 단 RT-1 검증은 boss 우선
- **사용자 명시 = (c) 둘 다**(brief line 8) → scope 결정 존중. Agent C 독립 판단: boss/worker 가 **동일 패턴**(urllib `/api/chat` → facade.complete)이고 **동일 facade 협력자** 재사용이므로 동시 처리가 중복 cycle 회피상 적정(점진 이득 < 오버헤드).
- **단** RT-1 보안 가치는 **boss 가 worker 보다 높다**(brief §3 line 84: boss = untrusted worker output 을 송신 = prompt injection 표적). worker 는 user prompt(상대적 trusted) 송신. → TDD 순서에서 **boss RT-1 T-RT1 을 우선 GREEN** 권고(보안 critical path 먼저). scope 변경 아님(둘 다 유지) — 검증 우선순위만.

### R-C5 — ADR-009 §3 v2.0 트리거 무관 확인 + import-linter 보존 실측 보강
- **§3 v2.0 트리거(T1~T4) 무관 확인**: 본 cycle = facade *사용처 확대*(boss/worker → facade 경유)이지 facade *구현 교체*(LiteLLM→자체 adapter) 아님. T1(provider 미지원)/T2(라이센스)/T3(결함)/T4(운영부담) **어느 것도 trigger 0** — LiteLLM 유지. ✅ brief 무언급이나 명문 권고(P2-3 트랙 B 번복이 v2.0 진입으로 오인되지 않도록).
- **import-linter 실측 보강**: `.importlinter` forbidden = `{openai, anthropic, litellm, ollama}`, ignore = `facade -> *` 한정. boss/worker 가 신규로 import 할 `src.adapters.llm.facade` 는 **forbidden 목록에 없음** → 계약 PASS(실측). 단 **boss/worker 가 실수로 `litellm`/`ollama` SDK 직접 import 하면 차단됨**(현재도 stdlib urllib 라 0건). brief §7 line 121 "boss/worker 는 facade 만 import, SDK 직접 import 0" 은 **실측 정합**(현 jarvis→adapters import 0건 실측 → 통합 후 facade 1개만 추가가 유일 신규 import). E-3 negative control 에 "boss/worker→litellm/ollama 직접 import 시 계약 FAIL" 양성 대조 포함 권고.

---

## NOTE (관찰 — 조치 불요)

- **N-1 트랙 B 번복 정당성 = 견고**: brief §6 line 116 "facade real *후* = 트랙 B 의 'SDK 미사용/urllib' 전제(facade 부재)가 해소" + Protocol/StubBoss 보존(번복 = OllamaBoss 내부만). boss.py docstring line 15~18 의 "트랙 B = stdlib urllib 단독" 전제는 facade `complete()` real(facade.py line 8~10, 69 entry) 로 **사실상 무효화** → 번복 = prior 합의 *무시* 아니라 *전제 변화 반영*. P-3 처리 정합.
- **N-2 D3 에러 매핑 = 계약 정합**: boss `_advise`(orchestrator line 111~118)가 이미 `except Exception → advisory_failed=True` 흡수 → facade 예외(`AuthenticationError`/`DegradedError`/`ConfigError`)가 boss.advise 에서 RuntimeError 로 변환되든 raw 로 누출되든 **orchestrator catch-all 이 R3 계약 보존**. worker 도 `_error()`(worker.py line 322) fail-soft 패턴 존재 → facade 예외 catch→WorkerResult(is_error) 자연 흡수. D3 = 기존 계약과 정합(신규 위험 낮음).
- **N-3 RT-1 redaction 동기 호출 = 정합**: redaction.py `redact_messages`/`redact_text`/`scrub` 모두 **sync 순수 함수**(line 52/62/76), facade `_redact_request`(facade.py line 156) 가 `complete()` 내부에서 동기 호출 → asyncio.run 래핑이 redaction 에 영향 0. T-RT1(brief §5.1) 양방향 검증(원본 secret 부재 AND REDACTION_MARK 존재)은 69 T-A 동형 — 패턴 적정.
- **N-4 worker.py urllib 제거 범위 정밀**: 실측 urllib 사용 = line 20~21(import) + 288/293/295(OllamaWorker.run 한정). **TmuxWorker/CliWorker 는 urllib 미사용**(subprocess 한정) → brief §5.2 line 106 "urllib import 제거(OllamaWorker 한정)" 정합. 단 import 제거 시 OllamaWorker 만 facade 전환되고 다른 클래스 무영향 — 안전.
- **N-5 SSRF posture 이전(D6) 정합**: 통합 후 `localhost:11434` 하드코딩(boss.py line 98 / worker.py line 231)이 registry endpoint(llm-providers.yaml line 32 `endpoint: http://localhost:11434`)로 이전. 외부 host 주입 경로는 registry config 편집뿐(코드 0) → SSRF posture = config 책임. `test_*_endpoint_is_localhost_only`(test_ollama_boss.py line 111 / test_ollama_worker.py line 162)의 "생성자에 url/host/endpoint 인자 부재" assert 는 facade 주입 후에도 **유지 가능**(생성자에 url 인자 신규 추가 0 — facade 가 endpoint 소유) → 의도 보존, 단 검증 대상이 "registry endpoint=localhost" 로 이동(brief §2 D6 line 79 정합).

---

## scope / 번복 독립 판단 (Agent C 고유)

1. **scope (c) 둘 다 = 적정** (R-C4): 동일 패턴·동일 facade 재사용 → 동시 처리가 점진보다 효율. 단 **examples 6 파일 = scope 누락**(B-C1) → scope 표 §0.2 에 명문 필수(silent 파괴 차단).
2. **CliWorker/TmuxWorker 제외 = 정확** (§0.2 #1): subprocess 기반 비-LLM(외부 바이너리 실행) → facade.complete(LLM 호출) 대상 아님. N-4 실측(urllib = OllamaWorker 한정)이 뒷받침. 통합 대상 식별 정확.
3. **registry alias = 기존 재사용 우선** (R-C2): 신규 active ollama provider = 동일-type 함정. routing alias 만 추가가 안전.
4. **번복 = 정당** (N-1): facade real 후 전제 해소 + Protocol 보존 → prior 합의 무시 아님. **두 추상(BossLLM Protocol + LLMFacade) 공존은 모순 아님** — BossLLM = *판단 지점 추상*(advise 계약 + StubBoss 트랙 A), LLMFacade = *LLM 호출 추상*(provider 라우팅). OllamaBoss 가 후자를 경유해 전자를 구현 = **계층 정합**(BossLLM Protocol 이 facade 불요 주장은 *오류* — Protocol 은 advise 계약일 뿐 provider 라우팅·redaction·Min2 미제공). ADR-009 §2.2 #6(provider 추가 = facade 변경만) 실효 위해 facade 경유 **필수**. 통합 > 공존 우월.
5. **v2.0 트리거 무관** (R-C5): LiteLLM 유지 — facade 사용처 확대이지 구현 교체 아님. T1~T4 trigger 0.

**더 나은 통합 방법?**: 구조적 대안은 없음(facade 경유 = ADR-009 §2.2 의무 실효의 유일 경로). 개선 여지는 (a) D2 RT-2 fallback 삭제+fail-loud(B-C2), (b) examples 동반/carry-over(B-C1), (c) rename 보류 또는 `LLMBoss` 묶음(R-C1), (d) registry 기존 alias 재사용(R-C2) — 모두 *방법 내 정련*이지 *방법 교체*가 아님.

---

## 요약 표

| 항목 | 판정 |
|----|----|
| 전체 | **APPROVE WITH CONDITIONS** |
| BLOCKING | 2 (B-C1 examples 6 누락 / B-C2 RT-2 fallback 결함) |
| 권고 | 5 (R-C1 rename 보류·R-C2 alias 재사용·R-C3 model_alias 유연성 trade·R-C4 검증 순서·R-C5 v2.0+import-linter) |
| NOTE | 5 |
| scope | (c) 적정, examples 누락 보정 필요 |
| 번복 | 정당(전제 해소 + Protocol 보존 + 통합>공존) |
| v2.0 trigger | 0 (LiteLLM 유지) |

**Agent C 검토 끝.**
