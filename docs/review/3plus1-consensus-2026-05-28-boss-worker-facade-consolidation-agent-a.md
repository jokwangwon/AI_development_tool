# 3+1 합의 — boss/worker facade 통합 (트랙 B → facade.complete()) — Agent A (구현 분석가)

> **렌즈**: "실제로 동작하는가?" — 구현 가능성 / 의존성 / 성능 / 실현가능성
> **작성**: 2026-05-28 (70번째 entry cycle, 세션 #4) — Phase 2 독립 분석 (Agent B/C/codex 미참조)
> **검토 대상**: `docs/phase0/boss-worker-facade-consolidation-brief.md` (v1) + boss.py/worker.py/orchestrator.py/facade.py/redaction.py/llm-providers.yaml + test_ollama_boss.py/test_ollama_worker.py
> **근거**: 직접 read + 실행만 (추측 0)

---

## 0. 판정

**APPROVE WITH CONDITIONS**

구현은 실현 가능하며 핵심 설계(D1 DI / D2 sync asyncio.run / RT-1 redaction / D6 SSRF 이전)는 코드로 입증된다. 단 **BLOCKING 3건**(facade 예외 매핑 부정확 / model_alias 미등록 silent 오라우팅 / pytest baseline 수치 불일치)을 brief v1.1 흡수 전 정정해야 한다.

---

## 1. 실행 baseline (실측)

| 항목 | 측정값 | 명령 |
|------|--------|------|
| 전체 suite | **177 passed in 0.11s** | `.venv/bin/python -m pytest tests/ -q` |
| jarvis suite | **144 passed in 0.07s** | `.venv/bin/python -m pytest tests/jarvis/ -q` |
| boss+worker test | **36 passed in 0.03s** | `test_ollama_boss.py` + `test_ollama_worker.py` |
| litellm 설치 | **미설치** (`ModuleNotFoundError: No module named 'litellm'`) | `import litellm` |
| import-linter | **PASS** (exit=0, baseline) | `lint-imports --no-cache` |

→ brief §5.3/§10 E-2 가 "jarvis 144 + adapters, 회귀 0" 라 표현한 것은 **jarvis 144 는 정확**하나, **"144" 를 전체 회귀 기준으로 쓰면 안 됨** (전체 177). BLOCKING-3 참조.

---

## 2. BLOCKING (번호 + file:line)

### BLOCKING-1 — facade 예외 매핑 부정확 (D3 §2 line 70 / facade.py:32,36,205,209)
brief §2 D3(line 70)은 facade 가 `AuthenticationError`/`DegradedError`/`ConfigError`/`RuntimeError` 를 raise 한다고 열거한다. **실측 불일치**:
- facade.py 가 *정의*하는 예외는 `ConfigError`(facade.py:32) + `DegradedError`(facade.py:36) 둘뿐.
- `AuthenticationError` 는 facade 클래스가 **아님** — litellm 표준 예외 *이름*을 문자열로 감지(`_DEGRADATION_EXC_NAMES`, facade.py:41)할 뿐이며, `complete()` 는 강등 조건 미충족 시 원본 예외를 **그대로 re-raise**(facade.py:209 `raise`).
- 따라서 boss/worker 가 facade 예외를 "종류별로 catch" 하는 것은 **불가능**(런타임에 litellm 예외 타입·name-only 강등 예외·ConfigError·DegradedError·임의 Exception 모두 가능).

**요구**: D3 를 "specific 예외 타입 catch" 가 아니라 **catch-all (`except Exception`)** 로 명문화. boss → `RuntimeError`(re-raise), worker → `WorkerResult(is_error=True)`. 이는 기존 boss(URLError/OSError catch)/worker(fail-soft) 계약과 동형이며 실현 가능. brief §9 RT-4 가 이미 "catch-all" 을 암시하나 §2 D3 본문의 예외 열거가 오해를 유발하므로 **본문 정정 필수**.

### BLOCKING-2 — model_alias 미등록 시 silent 오라우팅 (D5 §2 line 64/76 + §9 RT-3 / facade.py:148-154)
brief §9 RT-3 은 "model_alias 미등록 → routing KeyError → facade `_resolve` default fallback + registry alias 등록으로 완화" 라 기술. **실측**: `_resolve`(facade.py:148-154)는 **KeyError 를 던지지 않는다** — 미등록 alias 는 `routing.default` 로 **silent fallback**.
```
resolve('jarvis_worker_unregistered') -> 'anthropic-claude-api'  (실측)
```
즉 jarvis worker/boss 용 alias 를 `llm-providers.yaml` 에 등록하지 **않으면** crash 가 아니라 **로컬 Ollama 대신 cloud anthropic(default)로 조용히 라우팅**된다. 이는:
1. **로컬 사장(Ollama) 전제 위반** (MEMORY: 로컬 LLM=사장 방향) — 의도와 다른 provider 호출.
2. **보안/비용 영향** — untrusted worker output 이 의도치 않게 외부 cloud 로 송신(RT-1 redaction 은 적용되나 provider 자체가 의도 외).

**요구**: D5 의 registry alias 등록을 *선택*이 아닌 **필수 선행 조건**으로 격상. RT-3 의 "default fallback" 을 "silent 오라우팅 위험" 으로 재기술하고, 통합 GREEN 단계에서 alias 등록 + 라우팅 검증 test(model_alias → 의도한 provider_key) 의무화. (RT-3 의 KeyError 전제는 실측상 틀림.)

### BLOCKING-3 — pytest 회귀 기준 수치 불일치 (§5.3 line 110 / §10 E-2 line 145)
brief §5.3(line 110)·§10 E-2(line 145)가 "jarvis 144 + adapters, 회귀 0" / "jarvis 144 회귀 0" 라 기재. 전체 suite 는 **177**(jarvis 144 + 나머지 33). verify 기준을 "jarvis 144" 만으로 한정하면 adapters/redaction 회귀(특히 facade 주입으로 인한 import 경로 변화)를 **놓칠 수 있다**. 

**요구**: verify 기준을 **전체 177 회귀 0** + boss/worker test 재작성 후 신규 카운트로 명문화. (현재 boss 20 + worker 16 = 36 → 재작성 후 카운트 변동 예상치 brief 에 기록.)

---

## 3. 권고 (non-blocking)

### 권고-1 — D2 asyncio.run 안전성 = 입증됨, 단 fallback 불필요 명문 (§2 line 66 / §9 RT-2)
**실측**: src/jarvis·tests/jarvis 전체에 `async`/`await`/`asyncio`/event loop **0건**(grep). orchestrator.dispatch → worker.run/boss.advise 는 **완전 sync** 경로. 따라서:
- top-level `asyncio.run(facade.complete(...))` = **안전**(실측: `top-level asyncio.run: ok`).
- 중첩 루프(이미 running loop 안)는 `RuntimeError: asyncio.run() cannot be called from a running event loop`(실측) — 그러나 **그런 호출 경로가 현재 0**.

→ RT-2 의 "asyncio.new_event_loop fallback" 은 현 아키텍처에서 **불필요**(YAGNI). 추가하면 오히려 죽은 코드. 권고: fallback 코드 미추가 + "현 sync 아키텍처 한정 안전, 향후 async orchestrator 도입 시 재검토" known-limitation 1줄. (만약 미래 대비 방어 코드를 원하면 `try asyncio.run except RuntimeError: asyncio.new_event_loop().run_until_complete(...)` 패턴이 표준이나, 본 cycle 범위 외.)

### 권고-2 — D4 rename(OllamaBoss/OllamaWorker → provider-neutral) 우선순위 (§2 line 73)
실측 instantiation: **src 내 0건**(boss.py:17/172 는 docstring·주석, 실 호출 아님), **test 내 13건(boss) + 12건(worker)**. 즉 rename 영향 = test + 외부 wiring(사용자 영역)뿐. 실현 가능하나, **D4 rename 은 본 cycle scope 를 키운다**(브리프도 §2 D4 "합의 확정" 으로 유보). 권고: **rename 을 별도 후속 cycle 로 분리** — 본 cycle 은 facade 통합(동작 변경)에 집중하고, 명칭은 docstring 정정(트랙 B → facade 경유)으로 충분. rename 을 본 cycle 에 묶으면 test 재작성(BLOCKING-1/2 정정 동반)과 명칭 변경이 섞여 diff 노이즈 ↑.

### 권고-3 — RT-1 redaction 적용 위치 = facade 내부, boss/worker 추가 작업 0 (§3 / facade.py:156-162,193-203)
**실측**: `complete()` 가 `_redact_request`(facade.py:156)를 Router 위임 *전* 호출 — boss/worker 는 `facade.complete()` 만 부르면 redaction 자동 상속. 추가 코드 0. RT-1 효과는 정확하나, **응답 redaction 은 적용 안 됨**(facade `_normalize` 는 `LLMResponse.content` 원본 반환, scrub 미적용 — facade.py:212-228). brief §3(line 86)이 이미 "응답 redaction deferred" 라 명문하므로 정합. 권고: T-RT1 신규 test 는 **송신 방향(LLMRequest.messages 에 원본 secret 부재 + REDACTION_MARK 존재)만** 검증 — "양방향" 표현(§5.1 line 101)은 응답 redaction 미적용과 모순이므로 **"송신 단방향"** 으로 수정. (REDACTION_MARK = `"[REDACTED]"` 실측, redaction_patterns.py:170.)

### 권고-4 — urllib import 제거 = OllamaBoss/OllamaWorker 한정 가능, 단 조건부 (§5.2 line 105-106)
**실측**: `urllib` 사용처 = boss.py(OllamaBoss) + worker.py(OllamaWorker, line 288-295)뿐. worker.py 의 `subprocess`(line 18,90,130)는 CliWorker/TmuxWorker 용 → **유지 필수**. `import urllib.error`/`import urllib.request`(worker.py:20-21, boss.py:23-24) 제거는 OllamaWorker/OllamaBoss 전환 *완료 후*에만 가능. 권고: 제거 순서 명문(전환 GREEN → urllib 참조 0 확인 → import 제거). `os`/`re`/`json`/`shlex`/`uuid`/`time` 은 다른 클래스가 사용하므로 **제거 금지**(worker.py).

### 권고-5 — registry Min 2 보존 = alias 추가는 무영향, 단 type 검증 (§4 line 92 / facade.py:75-85)
**실측**: `validate_config`(facade.py:79)는 *providers active 集合*만 검사(routing alias 무관). jarvis alias 를 `routing:` 에만 추가하면 active 集合 불변 → Min 2 보존. 단 **신규 ollama provider 추가** 시엔 동일 type(ollama 2개) 금지(facade.py:84)에 걸릴 수 있음. 권고: 기존 `ollama-llama-local`(active) 재사용 또는 `routing.jarvis_worker: ollama-llama-local` alias 만 추가(provider 추가 0). 별도 ollama provider 신설은 BLOCKING-2 의 Min2/type 충돌 trigger.

### 권고-6 — fake facade 주입 = 실현 가능, hermetic 보장 (§5.1)
**실측**: litellm 미설치 환경에서 `from src.adapters.llm.facade import LLMFacade, LLMRequest, LLMResponse, ConfigError, DegradedError` + redaction import 모두 **성공**(facade lazy import, CB-8). test 는 실 `LLMFacade` 대신 **fake**(complete 가 scripted `LLMResponse` 반환 + 받은 `LLMRequest` 캡처)를 주입 가능 — Protocol/duck-typing 으로 충분(facade 는 ABC 아님). T-RT1 의 redaction 검증은 fake 가 *실 RedactionFilter 를 통과시킨 messages 를 캡처* 하거나, 실 `LLMFacade(config=cfg, router=fake_router)` 주입(redaction 실경로 보존)이 더 정확. 후자 권장(redaction 우회 fake 는 RT-1 입증력 약화).

---

## 4. NOTE (관찰)

- **N-1 (test 분류 실측)**: boss 20 test 중 urllib.urlopen mock = 8 → 재작성 ~8, 나머지 ~12 = prompt-rendering 순수함수(`boss_prompt_for`/`_render_prompt`/`_SYSTEM_PROMPT`/mirror/axes/authority) → **보존**. worker 16 test 중 urllib mock = 15 → 재작성 ~15, 보존 = `test_implements_worker_protocol` 1. brief §5.1 의 "prompt-rendering test 다수 보존" 은 boss 에 정확, worker 는 거의 전부 재작성(1 보존)임을 명문 권장.
- **N-2 (endpoint test 의미 전환)**: `test_*_endpoint_is_localhost_only`(boss test:111, worker test:162)는 생성자 시그니처에 url/host/endpoint 인자 부재를 검증. 통합 후 endpoint 책임이 registry 로 이전(D6) → 이 test 는 "boss/worker 생성자에 endpoint 주입 경로 0"(SSRF 회피 보존) 의미로 **유지 가능**(registry endpoint 검증은 facade 책무, jarvis test 범위 외). brief §6 D6 의 "registry endpoint 검증으로 재작성" 보다 **현 의미 보존**(생성자 url 인자 0)이 더 적합 — 책무 분리.
- **N-3 (성능)**: `asyncio.run` 오버헤드 = 호출당 event loop 1회 생성/파괴(~ms 단위). boss.advise/worker.run 은 호출당 1회(중첩 0) → 무시 가능. 단 실 LLM 호출(Ollama 70b/30b)은 초 단위이므로 asyncio.run 오버헤드는 **노이즈 수준**. 성능 BLOCKING 0.
- **N-4 (트랙 B 번복 정당성)**: facade real(69 entry) *후* = 트랙 B 의 "facade 부재 → urllib 직결" 전제 해소. BossLLM/Worker Protocol·StubBoss 보존(번복 = OllamaBoss/OllamaWorker 내부 호출 경로만) → prior 합의 추상 훼손 0. 구현 관점 정당.

---

## 5. 실현가능성 / 성능 종합 판정

| 차원 | 판정 | 근거 |
|------|------|------|
| 구현 가능성 | **가능** | facade.complete() async 확인(facade.py:193), fake 주입 hermetic 입증, sync 아키텍처 asyncio.run 안전 실측 |
| 의존성 | **무증가** | litellm = facade 한정(import-linter PASS), boss/worker 는 facade만 import, 신규 dep 0 |
| 성능 | **무영향** | asyncio.run 호출당 1회, LLM 응답 시간 대비 노이즈 (N-3) |
| 회귀 위험 | **중**(BLOCKING-3) | verify 기준을 177 전체로 격상해야 redaction/adapters 회귀 포착 |
| 누락 구현 위험 | **중**(BLOCKING-1/2) | 예외 catch-all 명문 + model_alias 등록 필수화 미반영 시 silent 오동작 |

**최종**: APPROVE WITH CONDITIONS — BLOCKING 3 흡수 후 구현 진입 적합.

---

**Agent A 검토 끝.**
