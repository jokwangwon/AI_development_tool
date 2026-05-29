Reading prompt from stdin...
OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6ed9-cfbc-7b61-98d2-101e07187270
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI, gpt-5.5), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2 Provider Liquidity).

## 본 cycle 개요

AI_development_tool 프로젝트 (SDD + TDD + 하네스 엔지니어링 + 3+1 멀티에이전트 합의). 본 cycle = **boss/worker facade 통합 (트랙 B → facade.complete())** (70번째 entry 예정, 세션 #4).

배경: 69 entry로 `src/adapters/llm/facade.py`의 `LLMFacade.complete()` LiteLLM Router 위임이 real이 됨. 그러나 jarvis `OllamaBoss`(`src/jarvis/boss.py`) + `OllamaWorker`(`src/jarvis/worker.py`)는 *의도된 "트랙 B" 설계*(stdlib `urllib` → Ollama `localhost:11434/api/chat` 직결, LLM SDK 미사용)로 **facade를 우회**한다. facade가 real이 되기 *전* 합의 결정(`jarvis-mvp1-local-boss-design-brief` + `jarvis-v00-working-sprint-brief`)이라 당시엔 정당했으나, 이제 두 LLM 직호출 경로가 facade 단일 진입점을 안 거쳐 Provider Liquidity(5조-2) gap + redaction(RT-1) 미적용 gap이 남음.

본 cycle = facade real *후* 두 경로를 facade.complete() 경유로 통합 (트랙 B 번복).

scope (사용자 명시):
- (c) **OllamaBoss + OllamaWorker 둘 다** 내부 urllib→Ollama를 facade.complete() 경유로 전환.
- sync 인터페이스 유지: advise()/run()은 Protocol상 sync → 내부 asyncio.run(facade.complete(...)). BossLLM/Worker Protocol·StubBoss·WorkerRegistry·orchestrator **무변경**.
- 트랙 B 번복 (prior 합의 reverse) — BossLLM Protocol(provider 추상)은 보존, OllamaBoss가 facade 우회하는 부분만 번복.

두 핵심 효과: ① Provider Liquidity 완성도 ↑ (boss/worker도 facade 단일 진입점). ② 보안 — RT-1 첫 적용 (현재 boss는 untrusted worker output[prompt injection 표적]을 redaction 없이 송신 → facade 경유 시 RedactionFilter가 secret strip, GP-2 prevention 확장).

본 cycle 발효 *하지 않는* 것: CliWorker/TmuxWorker(subprocess 비-LLM 워커) 변경 0 / Protocol·Stub·orchestrator 변경 0 / facade.complete() 본문 변경 0 / streaming 0 / 실 Ollama end-to-end 호출 검증 0 (mock=facade fake) / 65 RedactionFilter 패턴 내용 변경 0 / "Provider Liquidity 완전 발효 / jarvis 전체 통합" 선언 0 / 자동 후속 0.

⚠️ over-claim 경고: 이 프로젝트는 over-claim cascade를 세션 #2 4회 + #3 2회 + #4 1회(69 응답 누출) 포착(누적 7회). 본 cycle도 "Provider Liquidity 완전 발효"·"jarvis 전체 facade 통합"·"실 검증 완료" over-claim 주의 — boss/worker 2 LLM 경로 한정 + mock 검증.

## 검토 대상 (codex 직접 read 의무 — 추측 금지, line 인용 기반)

PRIMARY:
- docs/phase0/boss-worker-facade-consolidation-brief.md (v1, §0~§11) ← 본 검토 핵심

권위/code source (직접 read cross-verify):
- src/jarvis/boss.py (OllamaBoss urllib→Ollama 현 구현 + BossLLM Protocol + StubBoss + AdviceRequest/BossAdvice + boss_prompt_for)
- src/jarvis/worker.py (OllamaWorker urllib→Ollama + Worker Protocol + WorkerResult + CliWorker/TmuxWorker[subprocess 비-LLM] + _strip_code_fences/_write_workdir_file)
- src/jarvis/orchestrator.py (boss/worker 주입 + _advise fail-closed)
- src/adapters/llm/facade.py (69 entry — complete() / LLMRequest / LLMResponse / _redact_request / validate_config / 강등 감지)
- llm-providers.yaml (registry — active providers + routing)
- tests/jarvis/test_ollama_boss.py + tests/jarvis/test_ollama_worker.py (urllib mock test — 재작성 대상 + prompt-rendering test 보존 대상)
- docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.2(facade 단일 진입점 6 의무) + §2.3 / ADR-008 #4(단일 facade)
- docs/architecture/governance-preconditions.md §4.1(LLM request body redaction) + §4(GP-2)

## 검토 관점 (외부 cross-vendor 독립 — 추측 금지)

1. **트랙 B 번복 정당성**: facade real *후* 트랙 B("SDK 미사용/urllib")의 전제가 해소됐다는 논리가 타당한가? BossLLM Protocol(provider 추상, 헌법 5조 동형) 보존이 적절한가? prior 합의 번복을 본 합의로 처리하는 것이 SDD상 견고한가?
2. **RT-1 보안 개선 (핵심)**: brief §3 — 현 boss/worker가 untrusted worker output을 redaction 없이 urllib 송신 → facade 경유 시 RedactionFilter 적용 = GP-2 prevention 확장 주장이 정확한가? 응답 redaction deferred(69 CB-6 일관)가 boss/worker 응답→파일 작성 경로(worker)에서 누출 위험 없는가? redaction이 정상 worker 코드(생성물)를 손상시킬 위험(false positive)은?
3. **sync 유지 (asyncio.run 내부, D2)**: advise()/run() sync 유지 위해 내부 asyncio.run(facade.complete(...)) — 이벤트 루프 중첩/충돌 위험(이미 실행 중인 루프 내 호출 시 RuntimeError)? Protocol 무변경이 타당한가, 아니면 async 전파가 더 정합한가?
4. **facade 주입(DI) + model→model_alias (D1)**: OllamaBoss/Worker 생성자에 facade 추가 + model→model_alias 매핑. src 내 instantiation 0(외부 wiring) 실측이 맞는가? registry alias 매핑(D5) + Min 2 보존 타당?
5. **D4 명칭 rename**: OllamaBoss/OllamaWorker → provider-neutral(LLMBoss 등) 권고가 적절한가(위반패턴 #1 provider 명 하드코딩)? rename vs 현 명칭 유지 트레이드오프?
6. **에러 매핑 (D3)**: facade 예외(AuthenticationError/DegradedError/ConfigError) → boss RuntimeError(R3 계약) / worker WorkerResult(is_error, fail-soft) 매핑이 기존 계약 보존하는가?
7. **test 재작성 범위 (§5.1)**: urllib mock test → facade fake 재작성 + prompt-rendering test 보존 + Stub 주입 jarvis test 무영향 — 범위 판정이 정확한가? 누락된 회귀 위험?
8. **over-claim + 권위 인용 정확성**: "Provider Liquidity 완전 발효" 회피 + boss/worker 2 경로 한정 명문이 충실한가? 권위 인용 일치?

## 응답 형식 (필수)

1. **판정**: APPROVE / APPROVE WITH CONDITIONS / REVISE
2. **BLOCKING 항목** (있으면): 번호 + 근거 (직접 read한 파일/line 인용)
3. **권고 항목**: 번호 + 내용
4. **NOTE**: 관찰
5. **트랙 B 번복 독립 판단**: 번복이 정당한가, 아니면 트랙 B 보존이 나은가? 근거.
6. **권위 인용 cross-verify 매트릭스**: brief 인용 vs 실제 문서 일치/모순

한국어로 응답하되 기술 용어는 영어 원문 유지. 반드시 직접 파일을 read하여 검증하고, 추측이 아닌 구체적 line 인용 기반으로 응답하세요.

codex
요청하신 대로 blind review 관점으로 문서와 코드 원문을 직접 대조하겠습니다. 먼저 관련 파일의 line 번호를 확보한 뒤, brief 주장과 실제 구현/ADR 문구가 맞는지 교차 검증하겠습니다.
exec
/bin/bash -lc "nl -ba docs/phase0/boss-worker-facade-consolidation-brief.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# boss/worker facade 통합 (트랙 B → facade.complete()) 구현 brief (v1)
     2	
     3	> **작성**: 2026-05-28 (70번째 entry 진입 cycle — 세션 #4)
     4	>
     5	> **배경**: 69 entry로 `LLMFacade.complete()` Router 위임이 real이 됨. 그러나 jarvis `OllamaBoss`/`OllamaWorker`는 *의도된 "트랙 B" 설계*(stdlib `urllib` → Ollama `localhost:11434/api/chat` 직결, SDK 미사용)로 **facade를 우회**한다(`jarvis-mvp1-local-boss` + `v00-working-sprint` 합의). facade가 real이 되기 *전* 결정이라 당시엔 정당했으나, 이제 두 LLM 직호출 경로가 facade 단일 진입점을 거치지 않아 **Provider Liquidity(5조-2) gap** + **redaction(RT-1) 미적용 gap**이 남아 있다.
     6	>
     7	> **scope** (사용자 명시 AskUserQuestion):
     8	> - **(c) 둘 다 통합**: `OllamaBoss` + `OllamaWorker` 내부의 urllib→Ollama 직호출을 **`facade.complete()` 경유**로 전환.
     9	> - **sync 인터페이스 유지**: `advise()`/`run()`은 Protocol상 sync → 내부에서 `asyncio.run(facade.complete(...))` (Protocol/`StubBoss`/`Worker` Protocol/`WorkerRegistry`/orchestrator **무변경**).
    10	> - **트랙 B 번복**: 본 cycle = "stdlib urllib 단독" 트랙 B 결정을 facade 통합으로 *번복* — 자체 합의 필요(prior 합의 reverse).
    11	>
    12	> **본 cycle의 두 핵심 효과**:
    13	> 1. **Provider Liquidity 완성도 ↑**: boss/worker LLM 호출이 facade 단일 진입점 경유 → config 기반 provider/model 교체가 boss/worker에도 적용(ADR-009 §2.2 단일 진입점 의무 실효).
    14	> 2. ⭐ **보안 개선 (RT-1 첫 적용)**: 현재 boss는 **untrusted worker output**(prompt injection 표적)을 urllib로 redaction 없이 Ollama에 송신. facade 경유 시 `RedactionFilter`가 송신 전 secret strip → **GP-2 prevention이 boss/worker 경로까지 확장**.
    15	>
    16	> **명칭 정직성** ([[feedback_pass_scope_overclaim]]): 본 cycle = "boss/worker LLM 직호출 → facade 통합" 한정. **"jarvis 전체 facade 통합" / "Provider Liquidity 완전 발효" 아님**(CliWorker/TmuxWorker = subprocess 기반 비-LLM, 통합 대상 아님). 실 LLM 호출 검증 = mock(facade fake 주입), 실 Ollama 호출은 수동/별도.
    17	>
    18	> **선행 답습**: `src/adapters/llm/facade.py`(69 entry, `complete()` real) + `llm-providers.yaml`(registry) + `boss.py`/`worker.py`(트랙 B 현 구현) + `jarvis-mvp1-local-boss-design-brief`(BossLLM Protocol = provider 추상) + ADR-009 §2.2(facade 단일 진입점 6 의무) + governance §4(GP-2 송신 redaction)
    19	
    20	---
    21	
    22	## §0 본 brief 의 범위
    23	
    24	### §0.1 하는 것
    25	1. `OllamaBoss.advise()` + `OllamaWorker.run()` 내부 urllib→Ollama → `facade.complete()` 경유 전환 (§2)
    26	2. sync 유지(asyncio.run) + facade 주입(DI) + `model`→`model_alias` (§2)
    27	3. RT-1 redaction 적용(보안 개선) + 응답/에러 매핑 (§3)
    28	4. registry alias 매핑(ollama 모델) + SSRF posture(registry endpoint) (§4)
    29	5. test_ollama_boss/worker 재작성(urllib mock → facade fake) + prompt test 보존 (§5)
    30	6. 트랙 B 번복 합의 + 금지 + Rollback + Evidence + 자기진단 (§6~§10)
    31	
    32	### §0.2 하지 않는 것 (scope 경계)
    33	
    34	| # | 영역 | 본 cycle |
    35	|---|------|----|
    36	| 1 | `CliWorker` / `TmuxWorker` (subprocess 기반 비-LLM 워커) | 0 (LLM 직호출 아님 — 통합 대상 아님) |
    37	| 2 | `BossLLM` / `Worker` Protocol / `StubBoss` / `WorkerRegistry` / orchestrator 변경 | 0 (내부 구현만, 주입 계약 보존) |
    38	| 3 | facade.py `complete()` 본문 변경 | 0 (69 entry real 그대로 사용) |
    39	| 4 | streaming(`stream()`) | 0 (별도 보류 cycle) |
    40	| 5 | 실 Ollama end-to-end 호출 검증 | 0 (mock — facade fake 주입) |
    41	| 6 | 65 RedactionFilter 패턴 *내용* 변경 | 0 (협력자 재사용) |
    42	| 7 | "Provider Liquidity 완전 발효" 선언 | 0 (boss/worker 2 경로 통합 한정) |
    43	| 8 | 자동 후속 sub-cycle 진입 | 0 (사용자 명시 의무) |
    44	
    45	### §0.3 권위 답습 source
    46	- `src/adapters/llm/facade.py`(`complete()`/`LLMRequest`/`LLMResponse`, 69 entry) + `llm-providers.yaml`
    47	- `src/jarvis/boss.py`(`OllamaBoss`/`BossLLM`/`StubBoss`/`AdviceRequest`/`BossAdvice`) + `src/jarvis/worker.py`(`OllamaWorker`/`Worker`/`WorkerResult`)
    48	- ADR-009 §2.2(facade 단일 진입점) + §2.3(provider 분리) / governance §4.1(LLM request body redaction) / ADR-008 #4(단일 facade)
    49	- `jarvis-mvp1-local-boss-design-brief`(트랙 B 채택 합의 — 본 cycle 번복 대상)
    50	
    51	---
    52	
    53	## §1 진입 컨텍스트
    54	- 69 entry: facade `complete()` Router 위임 real. carry-over에서 streaming 검토 → SDD audit로 boss/worker 트랙 B 우회 발견 → 사용자 (c) 선택(우회 정상화 우선).
    55	- boss/worker 트랙 B = facade real *전* 합의 결정. 본 cycle = facade real *후* 통합(번복).
    56	
    57	---
    58	
    59	## §2 핵심 설계 결정 (D1~D6) — 합의 검증 대상
    60	
    61	### D1. facade 주입(DI) + `model` → `model_alias`
    62	- `OllamaBoss.__init__(model_alias, facade, timeout_s=..., system_prompt=None)` / `OllamaWorker.__init__(alias, model_alias, facade, output_filename=None, ...)`. `name`/`alias` = 기존 유지. **facade 주입**(테스트 = fake facade) — 생성자에 facade 추가(외부 wiring + 2 test만 영향, src 내 instantiation 0 실측).
    63	- `model`(특정 Ollama 모델명) → **`model_alias`**(registry routing 키). registry에 ollama 모델 alias 등록(§4).
    64	
    65	### D2. sync 유지 (asyncio.run 내부)
    66	- `advise()`/`run()`은 `BossLLM`/`Worker` Protocol상 sync. 내부 `asyncio.run(self._facade.complete(LLMRequest(...)))`. **Protocol/orchestrator 무변경**(async 전파 0). 단일 호출이므로 asyncio.run 1회 적정.
    67	
    68	### D3. 응답/에러 매핑
    69	- 응답: `LLMResponse.content` → boss는 `BossAdvice(summary=content)`, worker는 fence strip 후 파일/blob(기존 `_strip_code_fences`/`_write_workdir_file` 재사용).
    70	- 에러: facade는 `AuthenticationError`/`DegradedError`/`ConfigError`/`RuntimeError` 등 raise. **boss**: catch → `RuntimeError`(R3 계약 보존 — advise가 던지고 orchestrator가 누락→경고). **worker**: catch → `WorkerResult(is_error=True)`(fail-soft 계약 보존).
    71	
    72	### D4. 클래스 명칭 — provider-neutral 권고 (검증)
    73	- `OllamaBoss`/`OllamaWorker` 명칭은 facade 경유 후 **provider 명 하드코딩**(위반패턴 #1 인접 — 코드 식별자에 provider 인코딩). **권고 = provider-neutral 명칭**(`LLMBoss`/`LLMWorker` 또는 `FacadeBoss`/`FacadeWorker`). 단 rename = 2 test + 외부 wiring 영향 → 합의에서 결정(rename vs 현 명칭 유지 + docstring 정정). **본 brief 잠정: rename 권고, 합의 확정**.
    74	
    75	### D5. registry ollama alias
    76	- boss/worker용 ollama 모델을 `llm-providers.yaml`에 alias 등록(예 `routing.jarvis_worker: ollama-llama-local`). 기존 `ollama-llama-local`(active) 재사용 또는 워커 전용 모델 추가. **Min 2 active + 동일 type 금지 보존**(추가 시 §5.2 validate_config 통과 확인).
    77	
    78	### D6. SSRF posture (registry endpoint)
    79	- 현 boss/worker: `localhost:11434` 하드코딩(SSRF 회피, 생성자 url 인자 0). 통합 후: facade가 registry `endpoint: http://localhost:11434`(ollama provider)로 라우팅 → **SSRF posture = registry config 책임으로 이전**(여전히 localhost 고정, 외부 host 주입 경로 0). `test_*_endpoint_is_localhost_only` 의도 = registry endpoint 검증으로 재작성.
    80	
    81	---
    82	
    83	## §3 RT-1 redaction (보안 개선) + 송신 범위
    84	- 현재 boss는 **untrusted worker output**(prompt injection 표적, boss.py docstring)을 urllib로 **redaction 없이** Ollama 송신 = GP-2 prevention 미적용 경로.
    85	- 통합 후: `facade.complete()`가 `_redact_request`(messages + system, 69 CB-5)로 송신 전 secret strip → **GP-2 prevention이 boss/worker 경로까지 확장**(governance §4.1).
    86	- 응답 redaction = 69 CB-6 동형(deferred — caller 반환, set_verbose=False는 facade가 이미 보장). boss/worker가 응답을 로그/파일에 쓰는 경로: worker는 코드를 파일 작성(응답 redaction deferred 일관) — 본 cycle은 송신 redaction 적용에 한정, 응답 redaction은 facade 정책 답습.
    87	- ⚠️ redaction이 정상 worker output(코드/명령)을 손상시키지 않는지 확인(Tier-1 catalog = secret 패턴 한정, 69 T-4 false-positive 동형). worker가 *생성한 코드*에 secret-유사 패턴 포함 시 redaction 가능성 → known limitation 명문(secret 패턴 한정).
    88	
    89	---
    90	
    91	## §4 registry + validate_config 보존
    92	- §5.1 `llm-providers.yaml`에 jarvis worker/boss용 alias 추가 또는 기존 active alias 재사용. **Min 2 active(다른 type) 보존** — alias 추가는 routing만, providers active 集合 불변이면 validate_config 무영향.
    93	- facade는 69 entry `validate_config`(시작 fail-fast) + 강등 감지(CB-7) 그대로 적용 → boss/worker도 Min 2 보호 상속.
    94	
    95	---
    96	
    97	## §5 TDD 계획 (Router/facade mock — RED → GREEN → REFACTOR)
    98	
    99	### §5.1 RED (test 재작성 — `test_ollama_boss.py` + `test_ollama_worker.py`)
   100	- **재작성 (urllib mock → facade fake)**: `advise_returns_text_only_advice` / `posts_chat_endpoint_with_model`(→ facade가 model_alias로 호출 검증) / `raises_on_http_failure`(→ facade 예외→RuntimeError) / `raises_on_missing_content`(→ content 누락) / `endpoint_is_localhost_only`(→ registry endpoint localhost 검증) / worker 동형(fail-soft is_error).
   101	- **신규**: ⭐ T-RT1 — boss가 secret 포함 worker output을 advise → fake facade가 받은 `LLMRequest.messages`에 원본 secret 부재 AND `REDACTION_MARK` 존재(양방향, 69 T-A 동형). worker 동형.
   102	- **보존 (무변경)**: prompt-rendering test 다수(`boss_prompt_for_*`/`_render_prompt`/`_SYSTEM_PROMPT`/mirror/axes/authority — 순수 함수, migration 무관) + `implements_protocol`.
   103	
   104	### §5.2 GREEN
   105	- `boss.py`: `OllamaBoss`(→ 명칭 D4) 내부 urllib → `asyncio.run(facade.complete(...))` + 에러 catch→RuntimeError. urllib import 제거.
   106	- `worker.py`: `OllamaWorker`(→ 명칭 D4) 내부 urllib → facade + fence strip/파일 작성 재사용 + 에러 catch→WorkerResult(is_error). urllib import 제거(OllamaWorker 한정 — TmuxWorker subprocess는 유지).
   107	- `llm-providers.yaml`: jarvis alias(필요 시).
   108	
   109	### §5.3 REFACTOR + verify
   110	- 커버리지 70%+. **verify**: `.venv/bin/python -m pytest tests/ -q`(jarvis 144 + adapters, 회귀 0 — Stub 주입 test 무영향 확인) + import-linter(litellm facade 한정 유지 + boss/worker가 facade만 import) + grimp negative control + secret_scanner scan-source 0.
   111	
   112	---
   113	
   114	## §6 합의 형태 + 트랙 B 번복
   115	- 형태 = **풀 3+1 + 외부 LLM 1+(codex)**: 아키텍처(facade 단일 진입점 통합) + 보안(RT-1 확장) + Provider Liquidity 직결 + **prior 합의(트랙 B) 번복** → CLAUDE.md §3 다관점 필수.
   116	- 트랙 B 번복 정당성: facade real *후* = 트랙 B의 "SDK 미사용/urllib" 전제(facade 부재)가 해소됨. BossLLM Protocol(provider 추상)은 **보존**(StubBoss 트랙 A 유지) — 번복 대상은 "OllamaBoss가 facade 우회" 부분만.
   117	
   118	---
   119	
   120	## §7 Provider Liquidity 보존/완성
   121	- boss/worker LLM 호출이 facade 단일 진입점 경유 → ADR-009 §2.2 단일 진입점 의무가 jarvis까지 실효. provider 교체 = llm-providers.yaml 편집만(boss/worker 코드 변경 0). litellm import = facade 한정 유지(boss/worker는 facade만 import, SDK 직접 import 0 — import-linter 보존).
   122	
   123	---
   124	
   125	## §8 금지 사항
   126	§0.2 답습. 추가: CliWorker/TmuxWorker 변경 0 / Protocol·Stub·orchestrator 변경 0 / facade.complete() 본문 0 / streaming 0 / 실 Ollama 호출 0 / 65 패턴 내용 0 / "Provider Liquidity 완전 발효"·"jarvis 전체 통합" 표현 0 / 자동 후속 0.
   127	
   128	---
   129	
   130	## §9 Rollback Trigger
   131	
   132	| # | trigger | 대응 |
   133	|---|---------|----|
   134	| RT-1 | 통합 후 redaction이 정상 worker 코드 손상 | §3 — Tier-1 secret 패턴 한정 + false-positive test |
   135	| RT-2 | asyncio.run 내부 호출이 기존 이벤트 루프와 충돌(중첩 루프) | 단일 호출 진입점 — 중첩 루프 없음(advise/run = top-level sync). 충돌 시 asyncio.new_event_loop fallback |
   136	| RT-3 | model_alias 미등록 → routing KeyError | facade `_resolve` default fallback + registry alias 등록(§4) |
   137	| RT-4 | facade 예외 매핑 누락 → R3/fail-soft 계약 깨짐 | §2 D3 — boss=RuntimeError, worker=WorkerResult(is_error) catch-all |
   138	| RT-5 | 명칭 rename이 외부 wiring 깨뜨림 | §2 D4 — rename은 합의 확정 후, 외부 wiring은 사용자 영역(src 내 instantiation 0) |
   139	| RT-6 | 트랙 B 번복이 BossLLM Protocol 추상 훼손 | Protocol/StubBoss 보존(번복 = OllamaBoss 내부만) |
   140	
   141	---
   142	
   143	## §10 Evidence + 자기진단
   144	
   145	**Evidence**: E-1 boss/worker test 재작성 green + RT-1 양방향(T-RT1) / E-2 jarvis 144 회귀 0(Stub 주입 무영향) / E-3 import-linter(litellm facade 한정 + boss/worker SDK import 0) + negative control / E-4 secret_scanner scan-source 0 / E-5 커버리지 70%+ / E-6 urllib import 제거(OllamaBoss/OllamaWorker).
   146	
   147	**자기진단 (메타 편향)**:
   148	| # | 위험 | 처리 |
   149	|---|------|----|
   150	| P-1 | "Provider Liquidity 완전 발효" over-claim | boss/worker 2 경로 한정, CliWorker/TmuxWorker 제외 명문 |
   151	| P-2 | "실 Ollama 검증 완료" over-claim | mock(facade fake) — 실 호출 수동/별도 |
   152	| P-3 | 트랙 B 번복 = prior 합의 무시 | §6 — facade real 후 전제 해소 명시 + Protocol 보존 + 자체 합의 |
   153	| P-4 | redaction이 정상 코드 손상 | §3 — secret 패턴 한정 + false-positive test (known limitation 명문) |
   154	| P-5 | asyncio.run 중첩 루프 | RT-2 — top-level sync 진입, 중첩 없음 |
   155	| P-6 | 작성자 = Claude single-vendor | cross-vendor codex + 풀 3+1 |
   156	
   157	---
   158	
   159	## §11 합의 후 다음 단계
   160	사용자 승인 → 풀 3+1 + codex(`--sandbox danger-full-access`) 4 source → Reviewer 통합 → brief v1.1 흡수 → TDD(test 재작성 + boss/worker 내부 전환) → verify(144 회귀 0) → commit + push. 자동 진입 0.
   161	
   162	**본 brief v1 끝.**

exec
/bin/bash -lc "nl -ba src/jarvis/boss.py | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""Boss LLM 추상 — 로컬 사장의 판단 지점(결과 검토 advisory).
     2	
     3	답습: docs/phase0/jarvis-mvp1-local-boss-design-brief.md (v2) §3·§4·§5
     4	  [[3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss]] (풀 3+1, APPROVE w/ COND)
     5	  - §3: Boss = provider 추상(헌법 5조 동형). 순수 추론(부작용 0) — Worker(외부
     6	    바이너리, 부작용 有)와 대칭. OpenAI-호환 endpoint 로 통일(트랙 B).
     7	  - §4 R2: BossAdvice = 텍스트 전용 frozen — 콜백·경로·명령 필드 *금지*. "Boss
     8	    출력 실행 권한 0"을 산문이 아니라 데이터 모델 제약으로 강제. R6: confidence 삭제.
     9	  - §4 R1(fail-safe): advisory 는 결정적 flag 를 *추가*(union)만 — 감산 불가.
    10	    합집합 강제는 호출측(orchestrator)에서. 의미적 green washing(summary 오도)은
    11	    불변식이 막지 못함 → 결정적 flag 분리표시·raw diff·ReviewGuard 권위로 한정.
    12	  - §5 R3: advisory 실패는 게이트 진행(비차단) + 명시 경고. 본 모듈은 advise 가
    13	    실패를 *던지게* 두고, 누락→경고 변환은 orchestrator(가용성 정책)에서.
    14	
    15	본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(트랙 B 에서 stdlib urllib).
    16	트랙 A = StubBoss 주입으로 결정적 — 실 호출·HTTP·설치 0건.
    17	트랙 B = OllamaBoss(stdlib urllib.request 단독, `ollama` python SDK import 0건 —
    18	`.importlinter` 답습 + 신규 dep 0).
    19	"""
    20	from __future__ import annotations
    21	
    22	import json
    23	import urllib.error
    24	import urllib.request
    25	from dataclasses import dataclass, field
    26	from typing import Protocol, runtime_checkable
    27	
    28	
    29	@dataclass(frozen=True)
    30	class AdviceRequest:
    31	    """Boss 가 검토할 입력 — 모두 untrusted(워커 출력 포함, prompt injection 표적).
    32	
    33	    Boss 는 이 입력으로 *텍스트만* 생성한다. 실행·게이트 통과·workdir·argv 에
    34	    대한 어떤 제어 정보도 여기서 도출되지 않는다(§5 신뢰 경계).
    35	    """
    36	
    37	    prompt: str
    38	    worker_alias: str
    39	    output: str
    40	    deterministic_flags: list[str] = field(default_factory=list)
    41	
    42	
    43	@dataclass(frozen=True)
    44	class BossAdvice:
    45	    """Boss advisory 결과 — *텍스트 전용*(R2). 제어 흐름 필드 금지.
    46	
    47	    - summary: 사람에게 보여줄 자연어 검토 요약(표시용 — 게이트 결정에 자동 반영 0).
    48	    - extra_flags: 결정적 flag 에 *추가*할 위험 태그(union, 감산 불가 = R1 fail-safe).
    49	    - advisory_failed: advisory 가 실패(누락)했는지 표지(R3 명시 경고용 *상태* — 게이트
    50	      통과를 좌우하지 않는 표시 메타데이터). confidence 없음(R6).
    51	    """
    52	
    53	    summary: str
    54	    extra_flags: list[str] = field(default_factory=list)
    55	    advisory_failed: bool = False
    56	
    57	
    58	@runtime_checkable
    59	class BossLLM(Protocol):
    60	    """로컬 사장 추상 — provider 교체 단위(헌법 5조). 순수 추론(부작용 0).
    61	
    62	    name = 교체 키. advise() = MVP-1 유일 판단 지점(결과 검토). 실패 시 예외를
    63	    던질 수 있다(R3: 호출측이 누락→경고로 처리).
    64	    """
    65	
    66	    name: str
    67	
    68	    def advise(self, req: AdviceRequest) -> BossAdvice:
    69	        ...
    70	
    71	
    72	class StubBoss:
    73	    """결정적 테스트용 Boss — scripted advice 반환(트랙 A, 실 호출 0).
    74	
    75	    fail=True 면 advise 가 예외(endpoint timeout/다운 모사) → R3 경로 검증.
    76	    calls 로 호출 여부 관찰(R8: 워커 실패 시 미호출 확인).
    77	    """
    78	
    79	    def __init__(
    80	        self,
    81	        name: str,
    82	        advice: BossAdvice | None = None,
    83	        fail: bool = False,
    84	    ) -> None:
    85	        self.name = name
    86	        self._advice = advice if advice is not None else BossAdvice(summary="")
    87	        self._fail = fail
    88	        self.calls: list[AdviceRequest] = []
    89	
    90	    def advise(self, req: AdviceRequest) -> BossAdvice:
    91	        self.calls.append(req)
    92	        if self._fail:
    93	            raise RuntimeError("boss endpoint 실패(모사)")
    94	        return self._advice
    95	
    96	
    97	# Ollama 직결 — endpoint 하드코딩(SSRF 회피, 외부 host 주입 경로 0).
    98	_OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
    99	_DEFAULT_TIMEOUT_S = 60.0
   100	
   101	# 시스템 prompt 골격 — Boss 출력 책무 (R2 텍스트 전용 + 게이트 비-자동통과 +
   102	# 재출력 금지 + 체크리스트 형식). 답습: jarvis-boss-prompt-refinement-brief.md
   103	# (h) 및 jarvis-boss-prompt-branching-brief.md (m). 4 도메인 (code/shell/file/
   104	# general) 모두 동일 골격 + 도메인 어휘만 교체.
   105	
   106	# 도메인별 4 평가 항목 + few-shot 예시. mirror 차단 + R2 권위 = 답습 보존.
   107	_DOMAIN_TEMPLATES: dict[str, tuple[tuple[str, str, str, str], tuple[str, str, str, str]]] = {
   108	    # (4 axis labels), (4 few-shot examples)
   109	    "code": (
   110	        ("의도 부합: 작업이 요청대로 수행됐는가",
   111	         "정확성: 결과 자체가 올바른가",
   112	         "위험 신호: 파괴적 명령·민감 정보·외부 호출 등 사후 검토 사항",
   113	         "품질: 간결성·완성도 (간단히)"),
   114	        ("의도 부합: ✅ fizzbuzz.py 생성 요청 충족",
   115	         "정확성: ✅ 1~15 출력, FizzBuzz 분기 정확",
   116	         "위험 신호: 없음",
   117	         "품질: ✅ 단순/명료, 검사 순서 명확"),
   118	    ),
   119	    "shell": (
   120	        ("의도 부합: 요청한 명령이 실행됐는가",
   121	         "결과·로그 의미: 출력 로그가 성공·실패 어디를 가리키는가",
   122	         "위험 신호: 파괴적 명령 흔적·민감 정보 누출·예기치 못한 부작용",
   123	         "품질: 명령 형태·실행 시간 (간단히)"),
   124	        ("의도 부합: ✅ pytest + lint 실행 요청 충족",
   125	         "결과·로그 의미: ✅ 75 passed / Contracts 1 kept 0 broken",
   126	         "위험 신호: 없음 (sudo·rm 흔적 0)",
   127	         "품질: ✅ 명령 chain 명료, 실행 ~2초"),
   128	    ),
   129	    "file": (
   130	        ("의도 부합: 요청한 파일이 생성·수정됐는가",
   131	         "내용 일치: 파일 내용이 요구 사항을 충족하는가",
   132	         "위험 신호: 민감 정보·외부 URL·credential 누출 흔적",
   133	         "품질: 포맷·스키마 정합 (간단히)"),
   134	        ("의도 부합: ✅ hello.txt 생성 요청 충족",
   135	         "내용 일치: ✅ 'JARVIS_E2E_OK' 본문 정확",
   136	         "위험 신호: 없음",
   137	         "품질: ✅ UTF-8 평문, 줄바꿈 일관"),
   138	    ),
   139	    "general": (
   140	        ("의도 부합: 요구·요청이 반영됐는가",
   141	         "사실 정확: 진술이 사실과 일치하는가",
   142	         "위험 신호: 오해 소지·민감 정보·검증되지 않은 주장",
   143	         "품질: 명료성·간결성 (간단히)"),
   144	        ("의도 부합: ✅ 사용자 요구 핵심 반영",
   145	         "사실 정확: ✅ 출처·근거 명시",
   146	         "위험 신호: 없음",
   147	         "품질: ✅ 단락 구조 명료"),
   148	    ),
   149	}
   150	
   151	
   152	def _render_prompt(axes: tuple[str, str, str, str],
   153	                   shots: tuple[str, str, str, str]) -> str:
   154	    return (
   155	        "당신은 워커 출력 검토 advisory 입니다. 사람 게이트가 단독 권위이므로 "
   156	        "명령·콜백·실행 지시·자동 승인 어휘는 금지합니다.\n\n"
   157	        "⚠️ 워커 출력의 코드·명령·파일 내용을 *그대로 옮겨 쓰지 마십시오*. "
   158	        "재출력은 검토가 아닙니다. 다음 4 항목 각 1 line, 총 3~6 line, "
   159	        "한국어로 평가만 작성하십시오.\n\n"
   160	        + "\n".join(f"- {a}" for a in axes) + "\n\n예시:\n"
   161	        + "\n".join(f"- {s}" for s in shots) + "\n\n"
   162	        "결정적 flag 를 *대체*하려 하지 마십시오 (추가 의견만)."
   163	    )
   164	
   165	
   166	def boss_prompt_for(task_kind: str) -> str:
   167	    """워커 출력 형태별 system prompt — code/shell/file/general 4 도메인.
   168	
   169	    답습: docs/phase0/jarvis-boss-prompt-branching-brief.md §2·§3
   170	      - 4 도메인 모두 동일 골격 (mirror 차단 + 4 항목 + few-shot + R2 권위).
   171	      - 미지 kind → 'general' fallback (silent error 차단).
   172	      - caller 가 명시 = OllamaBoss(system_prompt=boss_prompt_for("shell")).
   173	    """
   174	    template = _DOMAIN_TEMPLATES.get(task_kind) or _DOMAIN_TEMPLATES["general"]
   175	    return _render_prompt(*template)
   176	
   177	
   178	# 기본 prompt = code 도메인 (회귀 0 — 기존 _SYSTEM_PROMPT 상수 답습).
   179	_SYSTEM_PROMPT = boss_prompt_for("code")
   180	
   181	
   182	class OllamaBoss:
   183	    """Ollama HTTP `/api/chat` 직결 BossLLM — stdlib urllib 단독.
   184	
   185	    답습: docs/phase0/jarvis-v00-working-sprint-brief.md §2
   186	      - `name` = 모델 식별자(헌법 5조 provider 교체 키).
   187	      - endpoint = localhost:11434 하드코딩(생성자에 url 인자 0건 — SSRF 회피).
   188	      - HTTP 실패·malformed JSON·content 누락 → RuntimeError (R3: 호출측 누락→경고).
   189	      - BossAdvice(summary, extra_flags=[], advisory_failed=False) — R2 텍스트 전용.
   190	
   191	    extra_flags 자동 추출 0건 = "boss 출력은 결정적 flag 를 *대체* 못 한다" 답습.
   192	    flag 합집합은 호출측(orchestrator merge_flags)이 결정적 flag 위주로 수행.
   193	    """
   194	
   195	    def __init__(
   196	        self,
   197	        model: str,
   198	        timeout_s: float = _DEFAULT_TIMEOUT_S,
   199	        system_prompt: str | None = None,
   200	    ) -> None:
   201	        self.name = model
   202	        self._timeout = timeout_s
   203	        # None = 기본 code 도메인 (회귀 0). caller = boss_prompt_for(kind) 주입.
   204	        self._system_prompt = system_prompt or _SYSTEM_PROMPT
   205	
   206	    def advise(self, req: AdviceRequest) -> BossAdvice:
   207	        user_blob = (
   208	            f"[task prompt]\n{req.prompt}\n\n"
   209	            f"[worker alias] {req.worker_alias}\n\n"
   210	            f"[worker output]\n{req.output}\n\n"
   211	            f"[deterministic flags]\n" + ", ".join(req.deterministic_flags)
   212	        )
   213	        body = {
   214	            "model": self.name,
   215	            "stream": False,
   216	            "messages": [
   217	                {"role": "system", "content": self._system_prompt},
   218	                {"role": "user", "content": user_blob},
   219	            ],
   220	        }
   221	        data = json.dumps(body).encode("utf-8")
   222	        request = urllib.request.Request(
   223	            _OLLAMA_CHAT_URL,
   224	            data=data,
   225	            method="POST",
   226	            headers={"Content-Type": "application/json"},
   227	        )
   228	        try:
   229	            with urllib.request.urlopen(request, timeout=self._timeout) as resp:
   230	                raw = resp.read()
   231	        except (urllib.error.URLError, OSError) as exc:
   232	            raise RuntimeError(f"Ollama 호출 실패: {exc}") from exc
   233	
   234	        try:
   235	            payload = json.loads(raw)
   236	        except (ValueError, TypeError) as exc:
   237	            raise RuntimeError(f"Ollama 응답 JSON 파싱 실패: {exc}") from exc
   238	
   239	        # Ollama `/api/chat` 응답 schema = {"message": {"role": ..., "content": "..."}}
   240	        message = payload.get("message") if isinstance(payload, dict) else None
   241	        content = message.get("content") if isinstance(message, dict) else None
   242	        if not isinstance(content, str) or not content:
   243	            raise RuntimeError(
   244	                "Ollama 응답에 message.content 누락 — silent empty advice 차단"
   245	            )
   246	        return BossAdvice(summary=content, extra_flags=[], advisory_failed=False)
   247	
   248	
   249	def merge_flags(deterministic: list[str], extra: list[str]) -> list[str]:
   250	    """결정적 flag ∪ advisory flag — *추가만*, 감산 불가(R1 fail-safe 불변식).
   251	
   252	    결정적 flag 는 전부 보존되고, extra 중 새것만 뒤에 덧붙는다(중복 없음).
   253	    advisory 가 결정적 flag 를 줄이는 경로는 구조적으로 존재하지 않는다.
   254	    """
   255	    return [*deterministic, *(f for f in extra if f not in deterministic)]

exec
/bin/bash -lc "nl -ba src/jarvis/worker.py | sed -n '1,340p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""Worker 추상 — headless CLI 워커 결과 모델.
     2	
     3	답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md
     4	  - §3: headless subprocess 1급. exit code = 결정적 완료신호, json = 출력 +
     5	    total_cost_usd(비용신호 공짜). 화면 스크래핑 함정 회피.
     6	  - D-2: 워커 = CLI 에이전트, headless subprocess 우선.
     7	
     8	본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(워커 = 외부 *바이너리* 실행 또는
     9	stdlib HTTP 호출). Provider Liquidity(헌법 5조) 답습: 워커 교체 = 다른 바이너리
    10	headless 호출 또는 OllamaWorker model 인자 교체.
    11	"""
    12	from __future__ import annotations
    13	
    14	import json
    15	import os
    16	import re
    17	import shlex
    18	import subprocess
    19	import time
    20	import urllib.error
    21	import urllib.request
    22	import uuid
    23	from dataclasses import dataclass
    24	from typing import Any, Callable, Protocol, runtime_checkable
    25	
    26	from src.jarvis.isolation import IsolationBackend, PassthroughIsolation
    27	
    28	# runner(cmd, workdir) -> (exit_code, stdout, stderr). 주입으로 테스트 결정성 확보.
    29	Runner = Callable[[list[str], str], "tuple[int, str, str]"]
    30	
    31	
    32	@dataclass(frozen=True)
    33	class WorkerResult:
    34	    """워커 1회 실행 결과. exit_code 가 완료/성공의 *결정적* 권위."""
    35	
    36	    exit_code: int
    37	    output: str
    38	    cost_usd: float | None
    39	    is_error: bool
    40	    raw: dict[str, Any] | None
    41	
    42	    @property
    43	    def succeeded(self) -> bool:
    44	        return not self.is_error
    45	
    46	    @classmethod
    47	    def from_cli(cls, exit_code: int, stdout: str, stderr: str = "") -> "WorkerResult":
    48	        """headless CLI 출력(json 우선) 파싱.
    49	
    50	        exit code 가 최우선 권위(비0 = 실패). json 파싱 실패 시 raw 보존 +
    51	        실패 처리(출력 잘림/비표준 provider 를 거짓 성공으로 오인 금지).
    52	        """
    53	        nonzero = exit_code != 0
    54	        try:
    55	            raw: dict[str, Any] | None = json.loads(stdout)
    56	        except (json.JSONDecodeError, TypeError):
    57	            raw = None
    58	
    59	        if raw is None:
    60	            return cls(
    61	                exit_code=exit_code,
    62	                output=stdout,
    63	                cost_usd=None,
    64	                is_error=True,  # 파싱 불가 = 거짓 성공 금지
    65	                raw=None,
    66	            )
    67	
    68	        cost = raw.get("total_cost_usd")
    69	        return cls(
    70	            exit_code=exit_code,
    71	            output=str(raw.get("result", "")),
    72	            cost_usd=float(cost) if cost is not None else None,
    73	            is_error=nonzero or bool(raw.get("is_error", False)),
    74	            raw=raw,
    75	        )
    76	
    77	
    78	@runtime_checkable
    79	class Worker(Protocol):
    80	    """워커 추상 — provider 교체 단위(헌법 5조). alias = 라우팅 키."""
    81	
    82	    alias: str
    83	
    84	    def run(self, prompt: str, workdir: str) -> WorkerResult:
    85	        ...
    86	
    87	
    88	def _subprocess_runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
    89	    """기본 runner — headless subprocess 실행(완료 = 프로세스 종료 = 결정적)."""
    90	    proc = subprocess.run(  # noqa: S603 (cmd = 신뢰된 argv + prompt)
    91	        cmd, cwd=workdir, capture_output=True, text=True
    92	    )
    93	    return proc.returncode, proc.stdout, proc.stderr
    94	
    95	
    96	class CliWorker:
    97	    """headless CLI 워커 — `argv + prompt` 를 격리 wrap 후 subprocess 실행.
    98	
    99	    예: argv=["claude", "--output-format", "json", "-p"] →
   100	        실행 `claude --output-format json -p "<prompt>"`.
   101	    runner 주입 시 실제 호출 없이 테스트 가능. 외부 LLM SDK import 0(바이너리 실행).
   102	    """
   103	
   104	    def __init__(
   105	        self,
   106	        alias: str,
   107	        argv: list[str],
   108	        isolation: IsolationBackend | None = None,
   109	        runner: Runner | None = None,
   110	    ) -> None:
   111	        self.alias = alias
   112	        self._argv = list(argv)
   113	        self._isolation = isolation or PassthroughIsolation()
   114	        self._runner = runner or _subprocess_runner
   115	
   116	    def run(self, prompt: str, workdir: str) -> WorkerResult:
   117	        cmd = self._isolation.wrap([*self._argv, prompt], workdir)
   118	        exit_code, stdout, stderr = self._runner(cmd, workdir)
   119	        return WorkerResult.from_cli(exit_code, stdout, stderr)
   120	
   121	
   122	# tmux subprocess runner = argv → (exit_code, stdout, stderr). 주입으로 테스트 결정성.
   123	TmuxRunner = Callable[[list[str]], "tuple[int, str, str]"]
   124	
   125	_SENTINEL_RE = re.compile(r"__JARVIS_DONE_(-?\d+)__")
   126	
   127	
   128	def _default_tmux_runner(argv: list[str]) -> tuple[int, str, str]:
   129	    """기본 tmux runner — `tmux <subcommand> ...` subprocess 실행."""
   130	    proc = subprocess.run(  # noqa: S603 (argv = 신뢰된 tmux 호출 + workdir 인자)
   131	        argv, capture_output=True, text=True
   132	    )
   133	    return proc.returncode, proc.stdout, proc.stderr
   134	
   135	
   136	class TmuxWorker:
   137	    """tmux 패널 실 spawn 워커 — 사용자가 관전 가능한 워커 모델 입증용.
   138	
   139	    답습: docs/phase0/jarvis-v00-working-sprint-brief.md §3
   140	      - 흐름: new-session -d → send-keys(격리 wrap 된 inner cmd + sentinel) →
   141	        capture-pane polling(sentinel 등장 시 종료) → kill-session(try/finally).
   142	      - 완료 sentinel = `__JARVIS_DONE_<exit_code>__` (echo $?).
   143	      - sentinel 미발화 = is_error=True(타임아웃·hang 거짓 성공 금지).
   144	      - tmux 패널 출력은 JSON 아님 → WorkerResult.from_cli 미경유, 직접 구성.
   145	      - cost_usd = None(headless JSON 경유 아님).
   146	    """
   147	
   148	    def __init__(
   149	        self,
   150	        alias: str,
   151	        argv: list[str],
   152	        isolation: IsolationBackend | None = None,
   153	        tmux_runner: TmuxRunner | None = None,
   154	        poll_attempts: int = 60,
   155	        poll_interval_s: float = 1.0,
   156	        session_prefix: str = "jarvis",
   157	    ) -> None:
   158	        self.alias = alias
   159	        self._argv = list(argv)
   160	        self._isolation = isolation or PassthroughIsolation()
   161	        self._tmux = tmux_runner or _default_tmux_runner
   162	        self._poll_attempts = max(1, poll_attempts)
   163	        self._poll_interval = max(0.0, poll_interval_s)
   164	        self._session_prefix = session_prefix
   165	
   166	    def run(self, prompt: str, workdir: str) -> WorkerResult:
   167	        inner = self._isolation.wrap([*self._argv, prompt], workdir)
   168	        session = f"{self._session_prefix}-{uuid.uuid4().hex[:8]}"
   169	        # sentinel 포함 shell 한 줄 — exit code 보존(`$?`).
   170	        inner_shell = shlex.join(inner)
   171	        full_cmd = f"cd {shlex.quote(workdir)} && {inner_shell}; echo __JARVIS_DONE_$?__"
   172	
   173	        new_rc, _, new_err = self._tmux([
   174	            "tmux", "new-session", "-d", "-s", session, "-x", "200", "-y", "50",
   175	        ])
   176	        if new_rc != 0:
   177	            return WorkerResult(
   178	                exit_code=new_rc or 1,
   179	                output=f"tmux new-session 실패: {new_err}",
   180	                cost_usd=None,
   181	                is_error=True,
   182	                raw=None,
   183	            )
   184	
   185	        try:
   186	            self._tmux(["tmux", "send-keys", "-t", session, full_cmd, "Enter"])
   187	            pane_text, sentinel_code = self._poll_for_sentinel(session)
   188	        finally:
   189	            self._tmux(["tmux", "kill-session", "-t", session])
   190	
   191	        if sentinel_code is None:
   192	            return WorkerResult(
   193	                exit_code=124,                            # 관행: timeout 코드
   194	                output=pane_text,
   195	                cost_usd=None,
   196	                is_error=True,                            # 거짓 성공 금지
   197	                raw=None,
   198	            )
   199	
   200	        cleaned = _SENTINEL_RE.sub("", pane_text).rstrip()
   201	        return WorkerResult(
   202	            exit_code=sentinel_code,
   203	            output=cleaned,
   204	            cost_usd=None,
   205	            is_error=sentinel_code != 0,
   206	            raw=None,
   207	        )
   208	
   209	    def _poll_for_sentinel(self, session: str) -> tuple[str, int | None]:
   210	        """capture-pane polling — sentinel 등장 시 즉시 반환."""
   211	        pane_text = ""
   212	        for _ in range(self._poll_attempts):
   213	            _, out, _ = self._tmux(["tmux", "capture-pane", "-p", "-t", session])
   214	            pane_text = out
   215	            m = _SENTINEL_RE.search(pane_text)
   216	            if m is not None:
   217	                return pane_text, int(m.group(1))
   218	            if self._poll_interval > 0:
   219	                time.sleep(self._poll_interval)
   220	        return pane_text, None
   221	
   222	
   223	# ─── OllamaWorker (LLM-only) ──────────────────────────────────────────────
   224	# 답습: docs/phase0/jarvis-ollama-worker-promotion-brief.md
   225	#   - LLM 응답 텍스트만 수신. fs 행동 능력 *경로 부재* (구조적 안전 본질).
   226	#   - 결정적 fs 쓰기 = workdir 안 단일 파일 한정 + realpath traversal 차단.
   227	#   - claude/codex(CliWorker) 와 다른 책임 모델 = prompt injection 으로 LLM 이
   228	#     위험 명령 출력해도 실행 0건.
   229	# 헌법 5조: model 인자 교체 = provider 교체 = Provider Liquidity 답습.
   230	
   231	_OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
   232	_OLLAMA_WORKER_DEFAULT_TIMEOUT_S = 180.0
   233	
   234	# 기본 system prompt — "코드 외 출력 차단" 어휘. 사용자 override 가능.
   235	_DEFAULT_SYSTEM_PROMPT = (
   236	    "You output only code with no explanations or markdown fences."
   237	)
   238	
   239	# 마크다운 fence 제거 — `` ```python ... ``` `` 또는 ``` ... ``` 모두 처리.
   240	_FENCE_RE = re.compile(r"^```[a-zA-Z0-9_+-]*\n?|\n?```$", re.MULTILINE)
   241	
   242	
   243	def _strip_code_fences(text: str) -> str:
   244	    """LLM 응답에서 마크다운 코드 fence 제거. fence 없으면 원문 그대로."""
   245	    stripped = _FENCE_RE.sub("", text).strip()
   246	    return stripped or text.strip()
   247	
   248	
   249	class OllamaWorker:
   250	    """Ollama HTTP /api/chat LLM-only 워커.
   251	
   252	    답습: docs/phase0/jarvis-ollama-worker-promotion-brief.md §1·§4
   253	      - 책무 = LLM 응답 + fence 제거 + (option) workdir 안 단일 파일 작성.
   254	      - LLM 임의 명령 실행 *경로 부재* → prompt injection 안전 본질.
   255	      - fail-soft (HTTP/JSON/content 실패 → WorkerResult is_error=True, raise 0).
   256	      - endpoint = localhost:11434 하드코딩 (SSRF 회피).
   257	
   258	    fs 행동:
   259	      - output_filename=None → 파일 미작성 (텍스트만 반환).
   260	      - output_filename="x.py" → workdir/x.py 결정적 작성 (realpath traversal 차단).
   261	      - 절대 경로 / .. escape → is_error=True + 파일 미생성.
   262	    """
   263	
   264	    def __init__(
   265	        self,
   266	        alias: str,
   267	        model: str,
   268	        output_filename: str | None = None,
   269	        timeout_s: float = _OLLAMA_WORKER_DEFAULT_TIMEOUT_S,
   270	        system_prompt: str | None = None,
   271	    ) -> None:
   272	        self.alias = alias
   273	        self._model = model
   274	        self._output_filename = output_filename
   275	        self._timeout = timeout_s
   276	        self._system_prompt = system_prompt or _DEFAULT_SYSTEM_PROMPT
   277	
   278	    def run(self, prompt: str, workdir: str) -> WorkerResult:
   279	        body = {
   280	            "model": self._model,
   281	            "stream": False,
   282	            "messages": [
   283	                {"role": "system", "content": self._system_prompt},
   284	                {"role": "user", "content": prompt},
   285	            ],
   286	        }
   287	        data = json.dumps(body).encode("utf-8")
   288	        req = urllib.request.Request(
   289	            _OLLAMA_CHAT_URL, data=data, method="POST",
   290	            headers={"Content-Type": "application/json"},
   291	        )
   292	        try:
   293	            with urllib.request.urlopen(req, timeout=self._timeout) as resp:
   294	                raw = resp.read()
   295	        except (urllib.error.URLError, OSError) as exc:
   296	            return self._error(f"Ollama 호출 실패: {exc}")
   297	
   298	        try:
   299	            payload = json.loads(raw)
   300	        except (ValueError, TypeError) as exc:
   301	            return self._error(f"Ollama 응답 JSON 파싱 실패: {exc}")
   302	
   303	        message = payload.get("message") if isinstance(payload, dict) else None
   304	        content = message.get("content") if isinstance(message, dict) else None
   305	        if not isinstance(content, str) or not content.strip():
   306	            return self._error("Ollama 응답에 message.content 누락 — silent 차단")
   307	
   308	        code = _strip_code_fences(content)
   309	
   310	        if self._output_filename:
   311	            written = self._write_workdir_file(code, workdir)
   312	            if written is not None:
   313	                return written      # path traversal 또는 IO 실패 → 조기 종료
   314	
   315	        # WorkerResult.from_cli 가 기대하는 claude-shaped JSON 으로 정규화
   316	        result_blob = json.dumps(
   317	            {"result": code, "is_error": False, "total_cost_usd": 0.0},
   318	            ensure_ascii=False,
   319	        )
   320	        return WorkerResult.from_cli(0, result_blob)
   321	
   322	    def _error(self, msg: str) -> WorkerResult:
   323	        return WorkerResult(
   324	            exit_code=1, output=msg, cost_usd=None, is_error=True, raw=None,
   325	        )
   326	
   327	    def _write_workdir_file(self, code: str, workdir: str) -> WorkerResult | None:
   328	        """workdir 안 결정적 fs 쓰기. 성공 = None / 실패 = WorkerResult(is_error)."""
   329	        path = os.path.join(workdir, self._output_filename)  # type: ignore[arg-type]
   330	        # path traversal 차단: realpath 가 workdir 안인지 검증
   331	        try:
   332	            real_workdir = os.path.realpath(workdir)
   333	            real_path = os.path.realpath(path)
   334	        except OSError as exc:
   335	            return self._error(f"realpath 실패: {exc}")
   336	        if not real_path.startswith(real_workdir + os.sep):
   337	            return self._error(
   338	                f"path traversal 차단: {self._output_filename} → {real_path}"
   339	            )
   340	        try:

exec
/bin/bash -lc "nl -ba src/jarvis/worker.py | sed -n '340,430p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   340	        try:
   341	            with open(real_path, "w", encoding="utf-8") as fh:
   342	                fh.write(code)
   343	        except OSError as exc:
   344	            return self._error(f"파일 쓰기 실패: {exc}")
   345	        return None

exec
/bin/bash -lc "nl -ba src/jarvis/orchestrator.py | sed -n '1,320p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""Orchestrator(사장) — 결정적 배관 + 라우팅 + 완료감지.
     2	
     3	답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §5 MVP-0 트랙 A
     4	  - D-1: 사장 = 결정적 오케스트레이터. 판단 지점(작업 분해·품질 평가) LLM 은
     5	    트랙 A 범위 밖(후속) — 본 골격은 *결정적 배관*만(증명 ①②③④).
     6	  - 흐름: 워커 선택(라우팅) → workdir 준비 → worker.run(headless) →
     7	    guard.review(무비판 수용 금지) → gate.request("반영 전" 사람 게이트) → 보고.
     8	  - Q-5: 라우팅 = MVP 수동/설정(alias). 자동 감지는 후속.
     9	"""
    10	from __future__ import annotations
    11	
    12	import tempfile
    13	from dataclasses import dataclass
    14	from enum import Enum
    15	from typing import Callable
    16	
    17	from src.jarvis.approval import ApprovalGate, ApprovalRequest
    18	from src.jarvis.boss import AdviceRequest, BossAdvice, BossLLM, merge_flags
    19	from src.jarvis.memory import MemoryLog
    20	from src.jarvis.review import ReviewGuard, ReviewVerdict
    21	from src.jarvis.worker import Worker, WorkerResult
    22	
    23	
    24	class OutcomeStatus(str, Enum):
    25	    APPLIED = "applied"          # 사람 승인 → 반영
    26	    DENIED = "denied"            # 사람 게이트 거부(또는 default-deny)
    27	    WORKER_FAILED = "worker_failed"  # 워커 실패(exit≠0/파싱불가) — 게이트 미진입
    28	
    29	
    30	@dataclass(frozen=True)
    31	class OutcomeReport:
    32	    task_prompt: str
    33	    worker_alias: str
    34	    result: WorkerResult
    35	    verdict: ReviewVerdict
    36	    approved: bool
    37	    applied: bool
    38	    status: OutcomeStatus
    39	    advice: BossAdvice | None = None  # MVP-1 advisory(boss 주입 시), 미주입=None
    40	
    41	
    42	class WorkerRegistry:
    43	    """alias → Worker 매핑. 첫 등록 워커 = 기본(Q-5 수동/설정)."""
    44	
    45	    def __init__(self) -> None:
    46	        self._workers: dict[str, Worker] = {}
    47	
    48	    def register(self, worker: Worker) -> None:
    49	        self._workers[worker.alias] = worker
    50	
    51	    def select(self, alias: str | None = None) -> Worker:
    52	        if alias is None:
    53	            if not self._workers:
    54	                raise KeyError("no workers registered")
    55	            return next(iter(self._workers.values()))
    56	        return self._workers[alias]  # 미등록 alias = KeyError
    57	
    58	
    59	def _default_workdir_factory(task_id: str) -> str:
    60	    """기본 작업디렉터리 — 워커당 격리 경로(트랙 B 격리 backend 의 mount 대상)."""
    61	    return tempfile.mkdtemp(prefix=f"jarvis-{task_id}-")
    62	
    63	
    64	class Orchestrator:
    65	    def __init__(
    66	        self,
    67	        registry: WorkerRegistry,
    68	        guard: ReviewGuard,
    69	        gate: ApprovalGate,
    70	        workdir_factory: Callable[[str], str] | None = None,
    71	        boss: BossLLM | None = None,
    72	        memory: MemoryLog | None = None,
    73	    ) -> None:
    74	        self._registry = registry
    75	        self._guard = guard
    76	        self._gate = gate
    77	        self._workdir_factory = workdir_factory or _default_workdir_factory
    78	        # R7: boss=None 이면 advisory 없이 MVP-0 동작 그대로 보존(하위 호환).
    79	        self._boss = boss
    80	        # 자가진화 Layer 0: memory=None 이면 누적 0(하위 호환). 주입 시 fail-soft 적재.
    81	        self._memory = memory
    82	
    83	    def _record(self, report: "OutcomeReport") -> None:
    84	        """Layer 0 관찰 누적 — 부재·실패 모두 dispatch 차단 사유 0건(fail-soft).
    85	
    86	        MemoryLog 자체도 fail-soft 이지만 호출측 또 한 겹 try/except = 책무 분리
    87	        (memory 가 예외를 던지더라도 dispatch 는 완료).
    88	        """
    89	        if self._memory is None:
    90	            return
    91	        try:
    92	            self._memory.append(report)
    93	        except Exception:
    94	            return
    95	
    96	    def _advise(
    97	        self, prompt: str, worker: Worker, result: WorkerResult, verdict: ReviewVerdict
    98	    ) -> BossAdvice:
    99	        """판단 지점(MVP-1 유일) — 결과 검토 advisory. R3: 실패는 누락+경고로 흡수.
   100	
   101	        ApprovalGate.request 의 fail-closed try/except 와 동형으로, Boss endpoint
   102	        timeout/다운/비정상은 advisory *부재*로 처리하되 사람에게 명시 경고한다
   103	        (부재를 안전으로 오해 금지). advisory 는 보조이므로 부재가 차단은 아니다.
   104	        """
   105	        req = AdviceRequest(
   106	            prompt=prompt,
   107	            worker_alias=worker.alias,
   108	            output=result.output,
   109	            deterministic_flags=list(verdict.flags),
   110	        )
   111	        try:
   112	            return self._boss.advise(req)  # type: ignore[union-attr]
   113	        except Exception:
   114	            return BossAdvice(
   115	                summary="⚠️ Boss advisory 실패 — 결정적 flag 만으로 판단",
   116	                extra_flags=[],
   117	                advisory_failed=True,
   118	            )
   119	
   120	    def dispatch(
   121	        self, prompt: str, task_id: str, worker_alias: str | None = None
   122	    ) -> OutcomeReport:
   123	        worker = self._registry.select(worker_alias)
   124	        workdir = self._workdir_factory(task_id)
   125	        result = worker.run(prompt, workdir)
   126	        verdict = self._guard.review(result)
   127	
   128	        # 완료감지 = exit code(결정적). 실패 워커 결과는 반영 후보가 아님 → 게이트 미진입.
   129	        # R8: 실패 워커엔 advise 미호출(비용·injection 표면 회피) — early-return 위.
   130	        if result.is_error:
   131	            failed = OutcomeReport(prompt, worker.alias, result, verdict,
   132	                                   approved=False, applied=False,
   133	                                   status=OutcomeStatus.WORKER_FAILED)
   134	            self._record(failed)        # Layer 0: 실패도 관찰 (운영 신호)
   135	            return failed
   136	
   137	        # MVP-1 판단 지점: boss 주입 시에만 advisory(결정적 가드 *뒤*, 사람 게이트 *앞*).
   138	        advice = self._advise(prompt, worker, result, verdict) if self._boss else None
   139	        # R1/fail-safe: 결정적 flag 에 advisory flag 를 union(추가만, 감산 불가).
   140	        flags = (merge_flags(list(verdict.flags), advice.extra_flags)
   141	                 if advice else list(verdict.flags))
   142	
   143	        req = ApprovalRequest(
   144	            summary=f"반영 승인 요청: worker={worker.alias} task={task_id}",
   145	            worker_alias=worker.alias,
   146	            flags=flags,
   147	            output_preview=result.output[:200],
   148	            advice=advice,
   149	        )
   150	        approved = self._gate.request(req)
   151	        status = OutcomeStatus.APPLIED if approved else OutcomeStatus.DENIED
   152	        report = OutcomeReport(prompt, worker.alias, result, verdict,
   153	                               approved=approved, applied=approved, status=status,
   154	                               advice=advice)
   155	        self._record(report)            # Layer 0: 정상 종료도 관찰
   156	        return report

exec
/bin/bash -lc "nl -ba src/adapters/llm/facade.py | sed -n '1,340p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""LLMFacade — Provider-agnostic facade (G2 GP-5, Provider Liquidity 5조-2).
     2	
     3	본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다
     4	(`llm-providers-design.md` §4.1 + ADR-009 §2.2 #1 답습). import 는 `_build_router()`
     5	함수 내부 lazy import — litellm 미설치 환경에서도 facade import + Router 주입 테스트가
     6	hermetic 하게 동작 (CB-8). import-linter `ignore_imports = facade -> *` 로 계약 PASS.
     7	
     8	SC-Provider Liquidity (69 entry): **facade `complete()` Router 위임 real (Core MVP, mock-verified)** —
     9	65 SC-1 의 redaction layer real 위에 LiteLLM Router 위임을 실배선. RT-1: redaction 은
    10	Router 위임 *전* 위치 (송신 secret strip, 미부착 window 0).
    11	
    12	답습 출처:
    13	  - docs/architecture/llm-providers-design.md §3(registry) / §4(facade) / §5(Router 위임) / §6(Min 2)
    14	  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.2 (facade 단일 진입점 6 의무)
    15	  - docs/decisions/ADR-008-hermes-adoption-decision.md #4(단일 facade) / #5(Min 2)
    16	  - docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md (v1.1)
    17	  - docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md (BLOCKING 8 흡수)
    18	
    19	scope (Core MVP): complete() + validate_config + 런타임 강등 감지(fail-loud) + 응답 정규화.
    20	deferred (명세 존속): streaming / OAuth single-flight / degraded 모드·자동복구·UI / metrics callback / 폴백 race 완화.
    21	"""
    22	from __future__ import annotations
    23	
    24	import os
    25	import sys
    26	from dataclasses import dataclass
    27	from typing import Any
    28	
    29	from src.adapters.llm.redaction import RedactionFilter
    30	
    31	
    32	class ConfigError(Exception):
    33	    """registry 검증 실패 (Min 2 active / 동일 type / 필드 누락) — 시작 시 fail-fast."""
    34	
    35	
    36	class DegradedError(Exception):
    37	    """런타임 강등 감지 — active provider 실패로 always-on(≥2) 침해 (CB-7 fail-loud)."""
    38	
    39	
    40	# litellm 표준 예외 = name 기반 감지 (hermetic — litellm import 0)
    41	_DEGRADATION_EXC_NAMES = frozenset({"AuthenticationError", "ServiceUnavailableError"})
    42	
    43	
    44	@dataclass(frozen=True)
    45	class LLMRequest:
    46	    messages: list[dict[str, Any]]
    47	    model_alias: str = "default"
    48	    system: str | None = None
    49	    temperature: float = 0.7
    50	    max_tokens: int = 4096
    51	    tools: list[dict[str, Any]] | None = None
    52	    tool_choice: dict[str, Any] | str | None = None
    53	    response_format: dict[str, Any] | None = None
    54	    stop_sequences: list[str] | None = None
    55	    metadata_in: dict[str, Any] | None = None  # Core MVP: 미전달 (metrics callback deferred)
    56	
    57	
    58	@dataclass(frozen=True)
    59	class LLMMetadata:
    60	    """화이트리스트 키만 (위반패턴 #2/#4 — raw provider 메타 누출 차단)."""
    61	
    62	    provider_used: str
    63	    fallback_chain: list[str]
    64	    finish_reason: str
    65	    request_id: str | None = None
    66	
    67	
    68	@dataclass(frozen=True)
    69	class LLMResponse:
    70	    content: str
    71	    usage: dict[str, Any]
    72	    metadata: LLMMetadata
    73	
    74	
    75	def validate_config(config: dict[str, Any]) -> None:
    76	    """시작 시 fail-fast: Min 2 active + 동일 type 금지 + 필드 누락 (§3.3/§6.1, R-5)."""
    77	    providers = config.get("providers") or {}
    78	    active = [(k, v) for k, v in providers.items() if v.get("status") == "active"]
    79	    if len(active) < 2:
    80	        raise ConfigError(f"Min 2 active 위반 (active={len(active)}) — ADR-008 #5")
    81	    types = [v.get("type") for _, v in active]
    82	    if None in types:
    83	        raise ConfigError("active provider type 필드 누락 — registry 정합성")
    84	    if len(set(types)) != len(types):
    85	        raise ConfigError(f"동일 type 2개 active 금지 (정전 동시 실패 회피) — R5 (types={types})")
    86	
    87	
    88	def to_router_config(config: dict[str, Any]) -> dict[str, Any]:
    89	    """llm-providers.yaml → LiteLLM Router model_list (CB-1: model_name = provider alias).
    90	
    91	    litellm_model 은 litellm_params.model 내부에만 존재 (complete() 호출 경로 노출 0,
    92	    위반패턴 #1 회피). api_key_env → os.environ 실값 보간 (R-12 — litellm 은 실값 기대).
    93	    """
    94	    providers = config["providers"]
    95	    model_list: list[dict[str, Any]] = []
    96	    for alias, p in providers.items():
    97	        params: dict[str, Any] = {"model": p["litellm_model"]}
    98	        env = p.get("api_key_env")
    99	        if env:
   100	            params["api_key"] = os.environ.get(env)
   101	        if p.get("endpoint"):
   102	            params["api_base"] = p["endpoint"]
   103	        model_list.append({"model_name": alias, "litellm_params": params})
   104	    return {"model_list": model_list}
   105	
   106	
   107	class LLMFacade:
   108	    """LLM 호출 단일 진입점. Router 위임 real (Core MVP). litellm import = 본 파일 한정."""
   109	
   110	    def __init__(
   111	        self,
   112	        config_path: str | None = None,
   113	        *,
   114	        config: dict[str, Any] | None = None,
   115	        redactor: RedactionFilter | None = None,
   116	        router: Any | None = None,
   117	    ) -> None:
   118	        if config is None:
   119	            if config_path is None:
   120	                raise ConfigError("config 또는 config_path 필요")
   121	            config = self._load_config(config_path)
   122	        validate_config(config)
   123	        self._config = config
   124	        self._providers: dict[str, Any] = config["providers"]
   125	        self._routing: dict[str, str] = config.get("routing", {})
   126	        self._redactor: RedactionFilter = redactor if redactor is not None else RedactionFilter()
   127	        self._router = router  # None → lazy build (litellm import 시점)
   128	
   129	    @staticmethod
   130	    def _load_config(path: str) -> dict[str, Any]:
   131	        import yaml  # stdlib 외 (forbidden 아님)
   132	
   133	        with open(path, encoding="utf-8") as f:
   134	            return yaml.safe_load(f)
   135	
   136	    def _build_router(self) -> Any:
   137	        import litellm  # lazy — facade 한정 (ADR-009 §2.2 #1, import-linter ignore)
   138	
   139	        litellm.set_verbose = False  # CB-6: 내장 로깅 비활성 (응답/요청 stdout 누출 차단)
   140	        rc = to_router_config(self._config)
   141	        return litellm.Router(model_list=rc["model_list"], num_retries=3, timeout=30)
   142	
   143	    def _get_router(self) -> Any:
   144	        if self._router is None:
   145	            self._router = self._build_router()
   146	        return self._router
   147	
   148	    def _resolve(self, model_alias: str) -> str:
   149	        """routing alias → provider key (= model_list model_name, CB-1)."""
   150	        if model_alias in self._routing:
   151	            return self._routing[model_alias]
   152	        if model_alias in self._providers:
   153	            return model_alias
   154	        return self._routing.get("default") or next(iter(self._providers))
   155	
   156	    def _redact_request(self, request: LLMRequest) -> dict[str, Any]:
   157	        """송신 전 redaction (RT-1, CB-5 범위 = messages + system). Router 위임 전 호출."""
   158	        messages = self._redactor.redact_messages(request.messages)
   159	        if request.system:
   160	            redacted_system = self._redactor.redact_text(request.system)
   161	            messages = [{"role": "system", "content": redacted_system}, *messages]
   162	        return {"messages": messages}
   163	
   164	    def _build_opts(self, request: LLMRequest) -> dict[str, Any]:
   165	        opts: dict[str, Any] = {"temperature": request.temperature, "max_tokens": request.max_tokens}
   166	        if request.tools:
   167	            opts["tools"] = self._redactor.scrub(request.tools)  # CB-5 outbound text
   168	        if request.tool_choice is not None:
   169	            opts["tool_choice"] = request.tool_choice
   170	        if request.response_format is not None:
   171	            opts["response_format"] = request.response_format
   172	        if request.stop_sequences:
   173	            opts["stop"] = request.stop_sequences
   174	        return opts
   175	
   176	    def _active_keys(self) -> list[str]:
   177	        return [k for k, v in self._providers.items() if v.get("status") == "active"]
   178	
   179	    def _on_provider_failure(self, failed_key: str) -> bool:
   180	        """런타임 강등 감지 (CB-7 fail-loud). 실패한 provider 제외 active < 2 → True + stderr.
   181	
   182	        degraded *모드*/자동복구/UI/timer 는 deferred — 감지+fail-loud 만 (차단조건 #5 부분 충족).
   183	        """
   184	        remaining = [k for k in self._active_keys() if k != failed_key]
   185	        if len(remaining) < 2:
   186	            sys.stderr.write(
   187	                f"[DEGRADED] active provider '{failed_key}' 실패 — remaining active "
   188	                f"{len(remaining)} < 2 (차단조건 #5 always-on 침해 — fail-loud)\n"
   189	            )
   190	            return True
   191	        return False
   192	
   193	    async def complete(self, request: LLMRequest) -> LLMResponse:
   194	        provider_key = self._resolve(request.model_alias)
   195	        # RT-1: 송신 전 redaction (Router 위임 전 — 미부착 window 0)
   196	        redacted = self._redact_request(request)
   197	        router = self._get_router()
   198	        try:
   199	            raw = await router.acompletion(
   200	                model=provider_key,  # CB-1: alias(=model_name), litellm_model 아님
   201	                messages=redacted["messages"],
   202	                **self._build_opts(request),
   203	            )
   204	        except Exception as exc:
   205	            if type(exc).__name__ in _DEGRADATION_EXC_NAMES and self._on_provider_failure(provider_key):
   206	                raise DegradedError(
   207	                    f"런타임 강등 — '{provider_key}' 실패 후 active < 2 (차단조건 #5)"
   208	                ) from exc
   209	            raise
   210	        return self._normalize(raw, provider_key)
   211	
   212	    def _normalize(self, raw: Any, provider_key: str) -> LLMResponse:
   213	        """LiteLLM ModelResponse(OpenAI 포맷 통일) → LLMResponse. 속성 접근 (R-3), raw 누출 0 (R-4)."""
   214	        choice = raw.choices[0]
   215	        content = choice.message.content
   216	        finish_reason = getattr(choice, "finish_reason", "stop")
   217	        usage_obj = getattr(raw, "usage", None)
   218	        usage = {
   219	            "input_tokens": getattr(usage_obj, "prompt_tokens", None),
   220	            "output_tokens": getattr(usage_obj, "completion_tokens", None),
   221	        }
   222	        metadata = LLMMetadata(
   223	            provider_used=provider_key,
   224	            fallback_chain=[provider_key],
   225	            finish_reason=finish_reason,
   226	            request_id=getattr(raw, "id", None),
   227	        )
   228	        return LLMResponse(content=content, usage=usage, metadata=metadata)
   229	
   230	    async def health(self) -> dict[str, bool]:
   231	        """축소 fallback (R-2): active alias + config 검증 결과 (dry probe 실배선 deferred, §9.2 명세 존속)."""
   232	        return {alias: True for alias in self._active_keys()}

codex
현재 코드 확인상 brief의 핵심 전제인 `OllamaBoss`/`OllamaWorker`의 urllib 직결은 실제로 존재합니다. 다음으로 registry, 기존 테스트, ADR/governance 권위 문구를 대조해서 blocking 여부를 판단하겠습니다.
exec
/bin/bash -lc "nl -ba llm-providers.yaml | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# llm-providers.yaml — LLM provider 단일 진실 원천 (Provider Liquidity 5조-2)
     2	#
     3	# SC-Provider Liquidity (69 entry) — facade complete() Router 위임 real (Core MVP).
     4	# 답습: docs/architecture/llm-providers-design.md §3.1 + ADR-009 §2 + ADR-008 #5(Min 2)
     5	#
     6	# 교체/추가/제거 = 본 파일 편집만 (코드 변경 0 — 5조-2 비협상). model_alias 는 의미 명칭만
     7	# (provider/모델명 인코딩 금지 — 위반패턴 #1). api_key 는 평문 금지, *_env 환경변수 보간.
     8	#
     9	# Core MVP active 2종 = 다른 type (anthropic + ollama) → Min 2 + 동일 type 금지 동시 충족.
    10	# OAuth / openrouter 등 standby 스키마는 설계 §3.1 참조 (본 cycle 미활성).
    11	
    12	defaults:
    13	  primary: anthropic-claude-api
    14	  secondary: ollama-llama-local
    15	
    16	routing:
    17	  default: anthropic-claude-api
    18	  background_jobs: ollama-llama-local
    19	
    20	providers:
    21	  anthropic-claude-api:
    22	    type: anthropic
    23	    litellm_model: anthropic/claude-opus-4-7
    24	    auth_method: api_key
    25	    api_key_env: ANTHROPIC_API_KEY
    26	    status: active
    27	
    28	  ollama-llama-local:
    29	    type: ollama
    30	    litellm_model: ollama/llama-3.3-70b
    31	    auth_method: none
    32	    endpoint: http://localhost:11434
    33	    status: active

exec
/bin/bash -lc "nl -ba tests/jarvis/test_ollama_boss.py | sed -n '1,280p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""OllamaBoss — Ollama HTTP `/api/chat` 직결 BossLLM 구현 (TDD).
     2	
     3	답습: docs/phase0/jarvis-v00-working-sprint-brief.md §2
     4	  - BossLLM Protocol 충족(`name`, `advise(AdviceRequest) -> BossAdvice`)
     5	  - stdlib `urllib.request` 단독(신규 dep 0, `ollama` SDK import 0 — `.importlinter` 답습)
     6	  - endpoint = `http://localhost:11434/api/chat` 하드코딩(SSRF 회피)
     7	  - HTTP 실패 → RuntimeError (R3 호출측 누락→경고 변환 답습)
     8	  - 응답 → BossAdvice(summary=text, extra_flags=[], advisory_failed=False)
     9	
    10	본 test 는 실 HTTP 호출 0건 — urllib.request.urlopen monkeypatch 한정.
    11	"""
    12	from __future__ import annotations
    13	
    14	import io
    15	import json
    16	from typing import Any
    17	from unittest.mock import patch
    18	
    19	import pytest
    20	
    21	from src.jarvis.boss import AdviceRequest, BossAdvice, BossLLM, OllamaBoss
    22	
    23	
    24	def _fake_response(payload: dict[str, Any]) -> io.BytesIO:
    25	    """urlopen 응답 객체 모사 — read() 가 JSON bytes 반환."""
    26	    buf = io.BytesIO(json.dumps(payload).encode("utf-8"))
    27	    return buf
    28	
    29	
    30	def test_ollama_boss_implements_protocol() -> None:
    31	    boss = OllamaBoss(model="qwen3-30b-a3b-instruct-2507-bartowski:latest")
    32	    assert isinstance(boss, BossLLM)
    33	    assert boss.name == "qwen3-30b-a3b-instruct-2507-bartowski:latest"
    34	
    35	
    36	def test_ollama_boss_advise_returns_text_only_advice() -> None:
    37	    boss = OllamaBoss(model="m1")
    38	    payload = {"message": {"role": "assistant", "content": "검토 요약 — 위험 없음."}, "done": True}
    39	    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
    40	        out = boss.advise(AdviceRequest(prompt="p", worker_alias="claude",
    41	                                        output="hello", deterministic_flags=[]))
    42	    assert isinstance(out, BossAdvice)
    43	    assert out.summary == "검토 요약 — 위험 없음."
    44	    assert out.extra_flags == []        # R2 텍스트 전용 답습 — 자동 flag 추출 0건
    45	    assert out.advisory_failed is False
    46	
    47	
    48	def test_ollama_boss_advise_posts_chat_endpoint_with_model() -> None:
    49	    """endpoint·모델·prompt 가 정확히 HTTP body 에 실리는가."""
    50	    boss = OllamaBoss(model="m1")
    51	    captured: dict[str, Any] = {}
    52	
    53	    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
    54	        captured["url"] = req.full_url
    55	        captured["data"] = json.loads(req.data.decode("utf-8"))
    56	        captured["timeout"] = timeout
    57	        return _fake_response({"message": {"content": "ok"}, "done": True})
    58	
    59	    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
    60	        boss.advise(AdviceRequest(prompt="작업 X", worker_alias="claude",
    61	                                  output="결과 Y", deterministic_flags=["risk"]))
    62	
    63	    assert captured["url"] == "http://localhost:11434/api/chat"
    64	    assert captured["data"]["model"] == "m1"
    65	    assert captured["data"]["stream"] is False
    66	    msgs = captured["data"]["messages"]
    67	    assert msgs[0]["role"] == "system"
    68	    # system prompt 가 검토 책무 + 재출력 금지 + 체크리스트 어휘를 명시
    69	    sp = msgs[0]["content"]
    70	    assert "재출력" in sp or "옮겨 쓰" in sp     # mirror 차단 어휘
    71	    assert "advisory" in sp.lower() or "검토" in sp
    72	    # 사용자 prompt / worker 출력 / deterministic flags 가 user 메시지에 포함
    73	    user_blob = msgs[-1]["content"]
    74	    assert "작업 X" in user_blob
    75	    assert "결과 Y" in user_blob
    76	    assert "risk" in user_blob
    77	    assert captured["timeout"] is not None and captured["timeout"] > 0
    78	
    79	
    80	def test_ollama_boss_advise_raises_on_http_failure() -> None:
    81	    """HTTP 예외 → RuntimeError (R3 호출측 처리 답습)."""
    82	    import urllib.error
    83	    boss = OllamaBoss(model="m1")
    84	    err = urllib.error.URLError("connection refused")
    85	    with patch("urllib.request.urlopen", side_effect=err):
    86	        with pytest.raises(RuntimeError):
    87	            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
    88	                                      output="o", deterministic_flags=[]))
    89	
    90	
    91	def test_ollama_boss_advise_raises_on_malformed_json() -> None:
    92	    """응답이 JSON 아니면 RuntimeError — 부재≠안전 답습(silent empty advice 금지)."""
    93	    boss = OllamaBoss(model="m1")
    94	    bad = io.BytesIO(b"not-json")
    95	    with patch("urllib.request.urlopen", return_value=bad):
    96	        with pytest.raises(RuntimeError):
    97	            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
    98	                                      output="o", deterministic_flags=[]))
    99	
   100	
   101	def test_ollama_boss_advise_raises_on_missing_content() -> None:
   102	    """응답 schema 누락 → RuntimeError (silent empty 차단)."""
   103	    boss = OllamaBoss(model="m1")
   104	    payload = {"done": True}  # message.content 없음
   105	    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
   106	        with pytest.raises(RuntimeError):
   107	            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
   108	                                      output="o", deterministic_flags=[]))
   109	
   110	
   111	def test_ollama_boss_endpoint_is_localhost_only() -> None:
   112	    """endpoint = localhost:11434 하드코딩 (SSRF 회피 답습)."""
   113	    boss = OllamaBoss(model="m1")
   114	    # endpoint 인자로 외부 host 주입 불가 — 생성자 시그니처에 url 인자 없음
   115	    import inspect
   116	    sig = inspect.signature(OllamaBoss.__init__)
   117	    assert "url" not in sig.parameters
   118	    assert "host" not in sig.parameters
   119	    assert "endpoint" not in sig.parameters
   120	
   121	
   122	# --- prompt 정밀화 (h) 답습: mirror 차단 + 4 항목 체크리스트 ---
   123	
   124	def test_system_prompt_forbids_mirroring_worker_output() -> None:
   125	    """신규 _SYSTEM_PROMPT 가 코드/명령 재출력 명시 금지 어휘 포함."""
   126	    from src.jarvis.boss import _SYSTEM_PROMPT
   127	    # mirror 차단 = "재출력" / "옮겨 쓰지 마십시오" / "그대로" 중 1+ 어휘
   128	    assert "재출력" in _SYSTEM_PROMPT
   129	    assert "옮겨 쓰" in _SYSTEM_PROMPT or "그대로" in _SYSTEM_PROMPT
   130	
   131	
   132	def test_system_prompt_includes_four_evaluation_axes() -> None:
   133	    """4 항목 체크리스트 어휘 (의도 부합 / 정확성 / 위험 / 품질) 모두 포함."""
   134	    from src.jarvis.boss import _SYSTEM_PROMPT
   135	    assert "의도" in _SYSTEM_PROMPT
   136	    assert "정확성" in _SYSTEM_PROMPT
   137	    assert "위험" in _SYSTEM_PROMPT
   138	    assert "품질" in _SYSTEM_PROMPT
   139	
   140	
   141	def test_system_prompt_long_enough_for_guidance() -> None:
   142	    """sufficient guidance 길이 — few-shot + 체크리스트 (도메인별 어휘 차이 허용)."""
   143	    from src.jarvis.boss import _SYSTEM_PROMPT
   144	    assert len(_SYSTEM_PROMPT) >= 380
   145	
   146	
   147	def test_system_prompt_preserves_authority_invariants() -> None:
   148	    """기존 R2 답습 어휘 — 사람 게이트 단독 권위 + 결정적 flag 대체 금지 보존."""
   149	    from src.jarvis.boss import _SYSTEM_PROMPT
   150	    assert "사람 게이트" in _SYSTEM_PROMPT
   151	    assert "대체" in _SYSTEM_PROMPT     # 결정적 flag 대체 금지 답습
   152	
   153	
   154	# --- (m) 워커별 prompt 분기: boss_prompt_for + 4 도메인 + override ---
   155	
   156	def test_boss_prompt_for_code_equals_default_system_prompt() -> None:
   157	    """boss_prompt_for('code') = 기존 _SYSTEM_PROMPT (회귀 0, (h) 정밀화 보존)."""
   158	    from src.jarvis.boss import _SYSTEM_PROMPT, boss_prompt_for
   159	    assert boss_prompt_for("code") == _SYSTEM_PROMPT
   160	
   161	
   162	def test_boss_prompt_for_shell_includes_command_vocabulary() -> None:
   163	    from src.jarvis.boss import boss_prompt_for
   164	    p = boss_prompt_for("shell")
   165	    assert "명령" in p
   166	    assert "로그" in p or "결과" in p
   167	
   168	
   169	def test_boss_prompt_for_file_includes_file_vocabulary() -> None:
   170	    from src.jarvis.boss import boss_prompt_for
   171	    p = boss_prompt_for("file")
   172	    assert "파일" in p
   173	    assert "내용" in p
   174	
   175	
   176	def test_boss_prompt_for_general_includes_request_vocabulary() -> None:
   177	    from src.jarvis.boss import boss_prompt_for
   178	    p = boss_prompt_for("general")
   179	    assert "요구" in p or "요청" in p
   180	    assert "사실" in p or "명료" in p
   181	
   182	
   183	def test_boss_prompt_for_unknown_kind_falls_back_to_general() -> None:
   184	    from src.jarvis.boss import boss_prompt_for
   185	    assert boss_prompt_for("nonexistent_kind") == boss_prompt_for("general")
   186	
   187	
   188	def test_all_domains_preserve_mirror_block_and_authority() -> None:
   189	    """4 도메인 모두 (h) 정밀화 답습 — mirror 차단 + R2 권위."""
   190	    from src.jarvis.boss import boss_prompt_for
   191	    for kind in ("code", "shell", "file", "general"):
   192	        p = boss_prompt_for(kind)
   193	        assert "재출력" in p, f"{kind}: mirror 차단 어휘 누락"
   194	        assert "사람 게이트" in p, f"{kind}: R2 권위 어휘 누락"
   195	        assert "대체" in p, f"{kind}: 결정적 flag 대체 금지 어휘 누락"
   196	        assert len(p) >= 380, f"{kind}: sufficient guidance 길이 미달 ({len(p)})"
   197	
   198	
   199	def test_ollama_boss_defaults_to_code_domain_prompt() -> None:
   200	    """OllamaBoss(system_prompt=None) → boss_prompt_for('code') 사용."""
   201	    from src.jarvis.boss import OllamaBoss, boss_prompt_for
   202	    boss = OllamaBoss(model="m")
   203	    captured: dict = {}
   204	
   205	    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
   206	        captured["data"] = json.loads(req.data.decode("utf-8"))
   207	        return _fake_response({"message": {"content": "ok"}, "done": True})
   208	
   209	    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
   210	        boss.advise(AdviceRequest(prompt="p", worker_alias="w",
   211	                                  output="o", deterministic_flags=[]))
   212	    assert captured["data"]["messages"][0]["content"] == boss_prompt_for("code")
   213	
   214	
   215	def test_all_domains_quality_axis_few_shot_starts_with_check_emoji() -> None:
   216	    """(o) 답습 — 4 도메인 모두 few-shot 의 품질 line 이 ✅ 시작.
   217	
   218	    (n) Layer 1 evidence 에서 발견된 unknown=3/3 mode collapse 차단.
   219	    Qwen3 가 응답에서 품질도 ✅ 로 시작하도록 mode 유도.
   220	    """
   221	    from src.jarvis.boss import boss_prompt_for
   222	    for kind in ("code", "shell", "file", "general"):
   223	        p = boss_prompt_for(kind)
   224	        # few-shot 영역 (예시: 이후) 의 "- 품질: ✅" 패턴 검증
   225	        # 단일 매칭 — 4 도메인 모두 1 회 등장
   226	        assert "품질: ✅" in p, f"{kind}: 품질 axis few-shot 이 ✅ 시작 아님"
   227	
   228	
   229	def test_ollama_boss_system_prompt_override_applied() -> None:
   230	    """caller 가 명시한 system_prompt 가 HTTP body 에 그대로 전달."""
   231	    from src.jarvis.boss import OllamaBoss
   232	    custom = "CUSTOM-DOMAIN-PROMPT-XYZ"
   233	    boss = OllamaBoss(model="m", system_prompt=custom)
   234	    captured: dict = {}
   235	
   236	    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
   237	        captured["data"] = json.loads(req.data.decode("utf-8"))
   238	        return _fake_response({"message": {"content": "ok"}, "done": True})
   239	
   240	    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
   241	        boss.advise(AdviceRequest(prompt="p", worker_alias="w",
   242	                                  output="o", deterministic_flags=[]))
   243	    assert captured["data"]["messages"][0]["content"] == custom

exec
/bin/bash -lc "nl -ba tests/jarvis/test_ollama_worker.py | sed -n '1,320p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""OllamaWorker — LLM-only Ollama HTTP /api/chat 워커 (TDD).
     2	
     3	답습: docs/phase0/jarvis-ollama-worker-promotion-brief.md
     4	  - §1: 책무 = LLM 응답 + 마크다운 fence 제거 + workdir 안 단일 파일 (optional).
     5	    fs 행동 능력 0 (LLM 텍스트 한정) = prompt injection 안전 본질.
     6	  - §3: stdlib urllib.request 단독 (신규 dep 0), endpoint localhost 하드코딩.
     7	  - §4: HTTP/JSON/content 실패 = is_error=True (raise 0). worker pattern 답습.
     8	
     9	실 HTTP 호출 0건 — urllib.request.urlopen monkeypatch 한정.
    10	"""
    11	from __future__ import annotations
    12	
    13	import io
    14	import json
    15	import os
    16	from pathlib import Path
    17	from typing import Any
    18	from unittest.mock import patch
    19	
    20	import pytest
    21	
    22	from src.jarvis.worker import OllamaWorker, Worker, WorkerResult
    23	
    24	
    25	def _fake_response(payload: dict[str, Any]) -> io.BytesIO:
    26	    return io.BytesIO(json.dumps(payload).encode("utf-8"))
    27	
    28	
    29	def _chat(content: str) -> dict[str, Any]:
    30	    return {"message": {"role": "assistant", "content": content}, "done": True}
    31	
    32	
    33	# --- §1 Worker Protocol ---
    34	
    35	def test_implements_worker_protocol(tmp_path: Path) -> None:
    36	    w = OllamaWorker(alias="glm", model="glm-4.7-flash:latest")
    37	    assert isinstance(w, Worker)
    38	    assert w.alias == "glm"
    39	
    40	
    41	# --- §2 정상 응답 → WorkerResult ---
    42	
    43	def test_returns_worker_result_with_response_text(tmp_path: Path) -> None:
    44	    w = OllamaWorker(alias="glm", model="m1")
    45	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("hello"))):
    46	        res = w.run(prompt="say hello", workdir=str(tmp_path))
    47	    assert isinstance(res, WorkerResult)
    48	    assert res.exit_code == 0
    49	    assert res.is_error is False
    50	    assert "hello" in res.output
    51	
    52	
    53	# --- §1 output_filename=None: 파일 미생성 ---
    54	
    55	def test_no_file_written_when_output_filename_none(tmp_path: Path) -> None:
    56	    w = OllamaWorker(alias="glm", model="m", output_filename=None)
    57	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("ignored"))):
    58	        w.run(prompt="p", workdir=str(tmp_path))
    59	    assert list(tmp_path.iterdir()) == []
    60	
    61	
    62	# --- §1 output_filename: workdir 안 작성 + 내용 일치 ---
    63	
    64	def test_writes_response_to_output_filename(tmp_path: Path) -> None:
    65	    w = OllamaWorker(alias="glm", model="m", output_filename="hello.py")
    66	    with patch("urllib.request.urlopen",
    67	               return_value=_fake_response(_chat("print('hi')"))):
    68	        w.run(prompt="p", workdir=str(tmp_path))
    69	    out = (tmp_path / "hello.py")
    70	    assert out.exists()
    71	    assert out.read_text(encoding="utf-8") == "print('hi')"
    72	
    73	
    74	# --- §1 마크다운 fence 제거 ---
    75	
    76	def test_strips_code_fences_before_writing(tmp_path: Path) -> None:
    77	    fenced = "```python\nprint('x')\n```"
    78	    w = OllamaWorker(alias="glm", model="m", output_filename="x.py")
    79	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat(fenced))):
    80	        res = w.run(prompt="p", workdir=str(tmp_path))
    81	    written = (tmp_path / "x.py").read_text(encoding="utf-8")
    82	    assert "```" not in written
    83	    assert written.strip() == "print('x')"
    84	    assert "```" not in res.output
    85	
    86	
    87	def test_strips_bare_fences_without_language(tmp_path: Path) -> None:
    88	    """언어 토큰 없는 ``` 도 제거."""
    89	    fenced = "```\nfoo\n```"
    90	    w = OllamaWorker(alias="glm", model="m", output_filename="x.txt")
    91	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat(fenced))):
    92	        w.run(prompt="p", workdir=str(tmp_path))
    93	    assert (tmp_path / "x.txt").read_text(encoding="utf-8").strip() == "foo"
    94	
    95	
    96	# --- §1 path traversal 차단 ---
    97	
    98	def test_path_traversal_blocked(tmp_path: Path) -> None:
    99	    """output_filename 이 workdir 밖으로 escape 시도 → is_error + 파일 미생성."""
   100	    outside = tmp_path / "outside"
   101	    outside.mkdir()
   102	    workdir = tmp_path / "ws"
   103	    workdir.mkdir()
   104	    w = OllamaWorker(alias="glm", model="m", output_filename="../outside/evil.py")
   105	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("payload"))):
   106	        res = w.run(prompt="p", workdir=str(workdir))
   107	    assert res.is_error is True
   108	    assert not (outside / "evil.py").exists()
   109	    # workdir 안에도 파일 미생성
   110	    assert list(workdir.iterdir()) == []
   111	
   112	
   113	def test_absolute_path_traversal_blocked(tmp_path: Path) -> None:
   114	    """절대 경로 output_filename 도 차단."""
   115	    workdir = tmp_path / "ws"
   116	    workdir.mkdir()
   117	    bad_abs = str(tmp_path / "elsewhere.py")
   118	    w = OllamaWorker(alias="glm", model="m", output_filename=bad_abs)
   119	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("payload"))):
   120	        res = w.run(prompt="p", workdir=str(workdir))
   121	    assert res.is_error is True
   122	    assert not os.path.exists(bad_abs)
   123	
   124	
   125	# --- §4 fail-soft (raise 0, is_error=True) ---
   126	
   127	def test_http_failure_returns_is_error_not_raise(tmp_path: Path) -> None:
   128	    import urllib.error
   129	    w = OllamaWorker(alias="glm", model="m")
   130	    with patch("urllib.request.urlopen",
   131	               side_effect=urllib.error.URLError("connection refused")):
   132	        res = w.run(prompt="p", workdir=str(tmp_path))
   133	    assert res.is_error is True
   134	    assert res.exit_code != 0
   135	
   136	
   137	def test_malformed_json_response_returns_is_error(tmp_path: Path) -> None:
   138	    bad = io.BytesIO(b"not-json")
   139	    w = OllamaWorker(alias="glm", model="m")
   140	    with patch("urllib.request.urlopen", return_value=bad):
   141	        res = w.run(prompt="p", workdir=str(tmp_path))
   142	    assert res.is_error is True
   143	
   144	
   145	def test_missing_message_content_returns_is_error(tmp_path: Path) -> None:
   146	    payload: dict[str, Any] = {"done": True}    # message.content 없음
   147	    w = OllamaWorker(alias="glm", model="m")
   148	    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
   149	        res = w.run(prompt="p", workdir=str(tmp_path))
   150	    assert res.is_error is True
   151	
   152	
   153	def test_empty_content_returns_is_error(tmp_path: Path) -> None:
   154	    w = OllamaWorker(alias="glm", model="m")
   155	    with patch("urllib.request.urlopen", return_value=_fake_response(_chat(""))):
   156	        res = w.run(prompt="p", workdir=str(tmp_path))
   157	    assert res.is_error is True
   158	
   159	
   160	# --- §3 endpoint hardcoded (SSRF 회피) ---
   161	
   162	def test_endpoint_is_localhost_hardcoded() -> None:
   163	    """생성자에 url/host/endpoint 인자 부재 = 외부 host 주입 경로 0."""
   164	    import inspect
   165	    sig = inspect.signature(OllamaWorker.__init__)
   166	    forbidden = {"url", "host", "endpoint", "base_url"}
   167	    assert not (set(sig.parameters) & forbidden), \
   168	        f"OllamaWorker 생성자에 {forbidden} 인자 금지 (SSRF 회피)"
   169	
   170	
   171	def test_request_targets_localhost_chat_endpoint(tmp_path: Path) -> None:
   172	    """실 호출 URL 이 http://localhost:11434/api/chat 인지 검증."""
   173	    captured: dict[str, Any] = {}
   174	
   175	    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
   176	        captured["url"] = req.full_url
   177	        captured["data"] = json.loads(req.data.decode("utf-8"))
   178	        return _fake_response(_chat("ok"))
   179	
   180	    w = OllamaWorker(alias="glm", model="m-x")
   181	    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
   182	        w.run(prompt="hi", workdir=str(tmp_path))
   183	    assert captured["url"] == "http://localhost:11434/api/chat"
   184	    assert captured["data"]["model"] == "m-x"
   185	    assert captured["data"]["stream"] is False
   186	
   187	
   188	# --- §2 system_prompt 기본값 + override ---
   189	
   190	def test_default_system_prompt_emphasizes_code_only(tmp_path: Path) -> None:
   191	    captured: dict[str, Any] = {}
   192	
   193	    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
   194	        captured["data"] = json.loads(req.data.decode("utf-8"))
   195	        return _fake_response(_chat("ok"))
   196	
   197	    w = OllamaWorker(alias="glm", model="m")
   198	    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
   199	        w.run(prompt="p", workdir=str(tmp_path))
   200	    sys_msg = captured["data"]["messages"][0]
   201	    assert sys_msg["role"] == "system"
   202	    # 기본 prompt = "code-only" 어휘 (마크다운/설명 금지)
   203	    text = sys_msg["content"].lower()
   204	    assert "code" in text
   205	    assert "markdown" in text or "fence" in text or "explanation" in text
   206	
   207	
   208	def test_custom_system_prompt_overrides_default(tmp_path: Path) -> None:
   209	    captured: dict[str, Any] = {}
   210	
   211	    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
   212	        captured["data"] = json.loads(req.data.decode("utf-8"))
   213	        return _fake_response(_chat("ok"))
   214	
   215	    w = OllamaWorker(alias="glm", model="m",
   216	                     system_prompt="Reply ONLY in haiku.")
   217	    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
   218	        w.run(prompt="p", workdir=str(tmp_path))
   219	    sys_msg = captured["data"]["messages"][0]
   220	    assert sys_msg["content"] == "Reply ONLY in haiku."

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-009: P1 Facade MVP 진입조건 + 자체 LLM Adapter v2.0 진입 트리거
     2	
     3	**상태**: 승인 (3+1 합의 결과 반영, Bβ-4) + **C-N 갱신 (단축 합의, 2026-05-09 후속 4)**
     4	**날짜**: 2026-05-04 (초기 승인) / **2026-05-09 (C-N 갱신 — P1 facade MVP 진입조건 명시 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 답습 + P2 v3 cross-reference)**
     5	**의사결정자**: 사용자 + 3+1 에이전트 합의 (초기) + **사용자 + Reviewer 단축 합의 (C-N 갱신, 2026-05-09)**
     6	**상위 권위**: 헌법 제5조-2 관용 (Provider Liquidity, 비협상), ADR-004 (외부 SDK 우선), ADR-008 (Hermes 도입 Option B), **ADR-011 §2.3 (Hermes ≠ root of trust)**, **ADR-012 §원칙 5 (Provider Liquidity 5-way Multi-layer Defense)**
     7	**관련 합의**: `docs/review/3plus1-consensus-2026-05-04-p1-llm-providers.md` (Bβ-4 출처), **`docs/review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md` (C-N 갱신 단축 합의)**
     8	
     9	---
    10	
    11	## C-N 갱신 요약 (2026-05-09 후속 4)
    12	
    13	본 갱신은 다음 5 영역 흡수:
    14	
    15	1. **P1 facade MVP 진입조건 명시** (§2 신설) — 기존 ADR-009 는 *v2.0 진입 트리거* 만 명시. MVP 조건이 *부재* 하여 P2 v3 정식 채택 합의 참조 시 모호. 본 갱신으로 명료화.
    16	2. **Hermes PMO ≠ provider 직접 소유** (§2.3 신설) — Hermes PMO (활성화 후 후보 시점) 가 provider SDK 직접 import / 모델명 분기 코드 *금지*. P1 facade 단일 진입점 강제 (ADR-011 §2.3 + Provider Liquidity 5-way Layer 1 답습).
    17	3. **Provider Liquidity 5-way Multi-layer Defense 답습** (§5 갱신) — 본 ADR-009 가 5-way Layer 1 (코드 lock-in 차단) 의 *모법 ADR* 임을 명시 (ADR-012 §원칙 5 발행으로 확정).
    18	4. **자체 Adapter v2.0 진입 트리거 (T1~T4) vs P1 facade MVP 조건 명확 구분** (§3.0 신설) — 두 개념을 표 형식으로 분리. v2.0 트리거 4종 본문 변경 0건.
    19	5. **P2 v3 정식 채택 합의 cross-reference** (§8 갱신) — 본 ADR 이 P2 v3 §1.6 (P1 과의 관계) + §6 G4 + §10 영구 핵심 제약에서 참조 가능하도록 cross-reference 명시.
    20	
    21	**핵심 결정 변경 0건** + **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** → 단축 합의 적격 (사용자 명시 답습).
    22	
    23	---
    24	
    25	## 1. 맥락 (Context)
    26	
    27	### 1.1 P1 v2 설계 채택 (2026-05-04)
    28	
    29	P1 설계(`llm-providers-design.md`)에서 LLM Provider 추상화 방안으로 **Option β (LiteLLM facade 승격)** 가 채택되었다. P1 facade 는 다음 핵심 보장:
    30	
    31	- **모든 Worker / Hermes Agent 의 LLM 호출 = P1 facade 단일 진입점 경유**
    32	- **LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정** (`llm-providers-design.md` §4 답습)
    33	- **provider SDK (anthropic / openai / gemini 등) 직접 import = 어떤 작성 주체도 금지** (`llm-providers-design.md` §9 답습 — depcruise 룰 + AST 스캐너)
    34	- **모델명 분기 코드 (`if model == "claude": ...`) = 어떤 작성 주체도 금지** (`llm-providers-design.md` §9)
    35	
    36	자체 Adapter 작성은 v2.0 백업 옵션으로 보존되며, 본 ADR 은 (a) **P1 facade MVP 진입조건** + (b) **v2.0 으로 전환할 때의 정량 트리거** 를 명세한다.
    37	
    38	### 1.2 본 ADR 부재 시 위험
    39	
    40	이 ADR 이 없으면 다음 위험 발생 가능:
    41	
    42	- 매몰비용·관성으로 LiteLLM 에 영구 종속 (P1 facade lock-in)
    43	- 일시적 불편을 이유로 v2.0 자체 작성 시작 → ADR-004 본질 ("외부 SDK 우선") 재위반
    44	- **P1 facade MVP 진입조건 부재 → P2 v3 정식 채택 합의 시 P1 ↔ Hermes ↔ provider 계층 모호** (C-N 갱신 사유)
    45	- **Hermes PMO 가 자체 provider 소유 시도 → Provider Liquidity (헌법 5조 관용) 위반** (Provider Liquidity 5-way Layer 1 차단 부재 시)
    46	
    47	---
    48	
    49	## 2. P1 Facade MVP 진입조건 (C-N 신설, 2026-05-09)
    50	
    51	### 2.1 MVP 진입 시점
    52	
    53	**P1 facade MVP 는 다음 *모든* 조건 충족 시점에 *즉시* 진입 가능**:
    54	
    55	| # | 조건 | 충족 시점 |
    56	|---|------|---------|
    57	| (a) | ADR-008 (Hermes 도입) Option B 합의 APPROVE | 2026-05-04 ✅ 충족 |
    58	| (b) | P1 v2 (`llm-providers-design.md`) Option β 합의 APPROVE | 2026-05-04 ✅ 충족 |
    59	| (c) | LiteLLM 라이센스 = Apache 2.0 (또는 동등 호환) 확인 | 2026-05-04 시점 ✅ |
    60	| (d) | LiteLLM `Min 2 Active` provider 충족 가능성 (`llm-providers-design.md` §6) | 2026-05-04 시점 ✅ |
    61	
    62	본 4 조건 모두 *2026-05-04 시점 이미 충족* — **별도 트리거 없음**. ADR-008 + P1 v2 합의 APPROVE = MVP 진입 의무 도화선 (자체 Adapter v2.0 진입 트리거와 *별도 개념*).
    63	
    64	### 2.2 MVP 진입 의미
    65	
    66	P1 facade MVP 진입 = 다음 의무 *즉시* 활성화:
    67	
    68	| # | 의무 | 강제 매커니즘 |
    69	|---|------|----------|
    70	| 1 | LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정 | depcruise 룰 + AST 스캐너 (`llm-providers-design.md` §9) |
    71	| 2 | provider SDK 직접 import (anthropic / openai / gemini 등) = 모든 작성 주체 금지 | depcruise 룰 + pre-commit hook |
    72	| 3 | 모델명 분기 코드 (`if model == "claude": ...`) = 모든 작성 주체 금지 | depcruise 룰 + AST 스캐너 |
    73	| 4 | `Min 2 Active` provider 의무 (런타임 재검증) | `llm-providers-design.md` §6 |
    74	| 5 | OAuth 직결 금지 (P1 facade 경유 의무) | `llm-providers-design.md` §7 |
    75	| 6 | provider 추가 시 P1 facade `adapters/llm/facade.py` 변경만으로 가능 (단일 진입점) | `llm-providers-design.md` §4 + §10 |
    76	
    77	### 2.3 Hermes PMO ↔ Provider 분리 (C-N 핵심)
    78	
    79	**Hermes PMO (활성화 후 후보 시점) 가 provider 를 직접 소유하지 않는다** — 본 ADR-009 §2.3 영구 권위.
    80	
    81	| 영역 | Hermes PMO 권한 | P1 Facade 권한 |
    82	|----|-------------|-------------|
    83	| LLM 호출 진입점 소유 | ❌ (provider SDK 직접 import 금지) | ✅ (`adapters/llm/facade.py` 한 파일 한정) |
    84	| Provider 라우팅 결정 | ❌ (LiteLLM Router 위임) | ✅ (`llm-providers-design.md` §5) |
    85	| 모델명 분기 | ❌ (`if model == "claude":` 등 금지) | ✅ (config 기반, `llm-providers-design.md` §3 `llm-providers.yaml`) |
    86	| 요청 / 응답 표준화 | ❌ | ✅ (Request/Response 표준 스키마, `llm-providers-design.md` §4) |
    87	| 비용 / 관측성 / Redaction | ❌ (Tier-1 42 catalog 강제) | ✅ (`llm-providers-design.md` §8) |
    88	| OAuth refresh single-flight | ❌ | ✅ (`llm-providers-design.md` §7) |
    89	| Provider 추가 / 제거 / 교체 | ❌ (자기 격상 금지 — ADR-011 §2.4 T3) | ✅ (config 변경 + 사용자 명시 승인 — T2) |
    90	
    91	**근거** (영구 권위):
    92	- ADR-011 §2.3 (Hermes ≠ root of trust) — Hermes 권한 위계 답습
    93	- ADR-008 차단조건 #4 (P1 Facade 위임 — `hermes-adoption-design.md` §2.4 답습)
    94	- ADR-012 §원칙 6 (provider-neutral 강제) — Hermes 가 evidence ledger entry 작성 시에도 `agent` 필드 = provider-neutral identifier
    95	- 헌법 5조 관용 (Provider Liquidity 비협상)
    96	
    97	**Hermes PMO 격상 (활성화) 시점** (P2 v3 §2.6 7 단계 답습):
    98	- 본 ADR-009 §2.3 분리는 *Hermes PMO 격상 후에도 영구 유지* — 격상 = 책임 활성화 *까지*, provider 소유 *아님*
    99	- 격상 후 Hermes 가 provider SDK 직접 import 시도 = T3 위반 + Hermes-originated commit auto-reject (G3 §2.2 #20 답습)
   100	
   101	---
   102	
   103	## 3. 자체 LLM Adapter v2.0 진입 트리거 (초기 결정 — 변경 0건)
   104	
   105	### 3.0 P1 Facade MVP vs v2.0 트리거 분리 (C-N 신설)
   106	
   107	본 ADR 은 두 *별도* 개념을 다룬다:
   108	
   109	| 개념 | 위치 | 진입 시점 | 트리거 |
   110	|----|----|---------|------|
   111	| **P1 facade MVP** | §2 | 2026-05-04 (ADR-008 + P1 v2 합의 APPROVE 시점) | 별도 트리거 없음 (4 충족 조건 § 2.1) |
   112	| **자체 LLM Adapter v2.0** | §3.1 ~ §3.5 | 미정 (트리거 1개 이상 충족 시) | T1 ~ T4 정량 트리거 (§3.1~§3.4) |
   113	
   114	**핵심**: P1 facade MVP 는 *현재 운영 중* (LiteLLM Option β). 자체 Adapter v2.0 은 *백업 옵션* — 트리거 충족 시점에만 진입.
   115	
   116	### 3.1 결정 (Decision) — 자체 LLM Adapter v2.0 진입 결정 (변경 0건)
   117	
   118	자체 LLM Adapter v2.0 작성은 다음 **트리거 중 1개 이상** 이 충족될 때에만 시작한다. 추측·선호·"느낌"으로는 진입할 수 없다.
   119	
   120	#### T1. LiteLLM 신규 provider 미지원 (강한 트리거)
   121	- 본 프로젝트가 도입하려는 신규 provider/모델을 **LiteLLM이 2분기(약 6개월) 내 지원하지 않음**
   122	- AND 본 프로젝트가 제출한 PR이 거부 또는 무대응 1분기 이상 지속
   123	- AND 해당 provider/모델이 본 프로젝트 핵심 워크플로의 필수 요소
   124	
   125	#### T2. LiteLLM 라이센스 변경 (즉시 트리거)
   126	- LiteLLM이 Apache 2.0에서 비호환 라이센스로 전환
   127	- AND 새 라이센스가 본 프로젝트 운영 모델과 충돌 (예: 상업적 사용 제한)
   128	
   129	#### T3. LiteLLM 정상화 불가 결함 (강한 트리거)
   130	- LiteLLM에서 다음 결함 중 하나가 **2분기 이상 미해결**:
   131	  - 보안 결함 (CVE 등급 HIGH 이상)
   132	  - 본 프로젝트 핵심 워크플로 차단 버그 (회피 불가능)
   133	  - 응답 정규화 결함으로 Provider Liquidity 위반 (역설적 lock-in)
   134	
   135	#### T4. LiteLLM 운영 부담 정량 역전 (정량 트리거)
   136	- 자체 Adapter 추정 유지 부담(40~80h/년)보다 **LiteLLM 통합/우회 부담이 더 커짐**
   137	- 측정 기간: 4분기 연속
   138	- 측정 방법: facade 보강 시간 + LiteLLM 버그 우회 시간 + 버전 추적 시간을 분기별 기록
   139	
   140	### 3.2 트리거 미충족 시 — 자동 NO-GO (변경 0건)
   141	
   142	위 4개 트리거 중 어느 것도 충족되지 않으면, 자체 Adapter 작성 제안은 **자동 반려** 한다. 다음 같은 사유는 트리거가 아니다:
   143	- "외부 종속성 줄이고 싶다" (선호)
   144	- "LiteLLM 업데이트가 잦다" (불편)
   145	- "모든 코드를 자가 통제하고 싶다" (취향)
   146	- "특정 provider만 사용하면 되니 LiteLLM 과잉" (단기적 판단)
   147	
   148	---
   149	
   150	## 4. 선택지 (Options Considered) — 변경 0건
   151	
   152	### 옵션 A: 트리거 없이 v2.0 시점만 명시 (예: "1년 후 재검토")
   153	- 장점: 단순
   154	- 단점: 시점 도달 시 정당성 없이 자동 진입 가능 → ADR-004 본질 재위반
   155	
   156	### 옵션 B: 정량 트리거 4종 명세 (T1~T4) ⭐ 채택
   157	- 장점: 객관적 의사결정, ADR-004 본질 보호, 매몰비용 회피
   158	- 단점: 트리거 측정 부담 (특히 T4의 시간 기록)
   159	
   160	### 옵션 C: "필요 시 결정"으로 미명세
   161	- 장점: 유연성
   162	- 단점: 본 ADR 작성 목적 자체가 무력화
   163	
   164	---
   165	
   166	## 5. Provider Liquidity 5-way Multi-layer Defense (C-N 갱신, 2026-05-09)
   167	
   168	본 ADR-009 는 **Provider Liquidity 5-way Multi-layer Defense 의 Layer 1 모법 ADR** 이다 (ADR-012 §원칙 5 발행으로 확정).
   169	
   170	| Layer | 책임 영역 | 모법 / 답습 |
   171	|------|--------|---------|
   172	| **Layer 1** (코드 lock-in 차단) | 모든 작성 주체의 provider SDK 직접 import / 모델명 분기 코드 차단 | **본 ADR-009 §2.2** + G2 GP-5 (depcruise 룰) + `llm-providers-design.md` §9 |
   173	| Layer 2 (Hermes-originated lock-in 변경 차단) | Hermes 작성 주체 한정 차단 | G3 §6.4 + 본 ADR-009 §2.3 |
   174	| Layer 3 (Skill 메타데이터 차원) | `provider_bindings` schema *required*/*exclusive* 금지 | G4 §3.5 |
   175	| Layer 4 (export format 차원) | JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능 | G4 §4.3 |
   176	| Layer 5 (Evidence 형식 차원) | 11 필드 모두 provider-neutral 강제 | ADR-012 §2.1 원칙 6 + G4 §4.2 |
   177	
   178	**5 Layer 모두 충족** 시 Provider Liquidity 의 *완결성* 확보. 1 Layer 만 깨져도 lock-in 위험 잔존.
   179	
   180	### 5.1 자체 Adapter v2.0 진입 시 Provider Liquidity 보장
   181	
   182	자체 Adapter v2.0 진입 시점 (트리거 1+ 충족) 에도 **Provider Liquidity 5-way Layer 1~5 모두 보존 의무**:
   183	
   184	- Layer 1: v2.0 자체 Adapter 도 단일 진입점 강제 (provider SDK 직접 import 금지)
   185	- Layer 2 ~ Layer 5: 변경 없음 (Hermes / Skill / JSONL / Evidence 차원은 v2.0 무관)
   186	- v2.0 진입 = *수단 변경* (LiteLLM → 자체 Adapter), *목적 보존* (Provider Liquidity 비협상) — ADR-011 §2.1 (a)~(e) 5조건 답습 의무
   187	
   188	---
   189	
   190	## 6. 근거 (Rationale)
   191	
   192	### 6.1 초기 근거 (변경 0건)
   193	
   194	P1 v2 설계가 LiteLLM 의존을 채택하는 만큼, 그 의존을 끊는 의사결정도 동일한 엄격함으로 게이트되어야 한다. ADR-004는 "외부 SDK 부족 입증 후에만 v2.0"이라 명시했고, 본 ADR은 그 "입증"을 정량 트리거로 구체화한 것이다.
   195	
   196	### 6.2 C-N 갱신 근거 (2026-05-09)
   197	
   198	P2 v3 정식 채택 합의 진입 *전*, 다음 모호 영역 해소 의무:
   199	
   200	1. **P1 facade MVP 진입조건 부재** — P2 v3 §1.6 (P1 과의 관계) 참조 시 "MVP 가 언제 시작됐고 어떤 의무가 활성화되어 있는가" 모호 → 본 갱신 §2.1 + §2.2 명시
   201	2. **Hermes PMO ↔ provider 계층 분리 부재** — Hermes PMO 격상 후 provider 소유 가능성 시사 → 본 갱신 §2.3 영구 권위로 차단
   202	3. **Provider Liquidity 5-way Multi-layer Defense 모법 ADR 부재** — ADR-012 §원칙 5 가 "5-way" 명명을 발행했으나 Layer 1 의 *모법 ADR* 부재 → 본 갱신 §5 명시
   203	4. **v2.0 트리거 vs MVP 조건 분리 부재** — 두 개념 혼동 가능 → 본 갱신 §3.0 매트릭스 명시
   204	5. **P2 v3 cross-reference 부재** — 본 ADR 이 P2 v3 정식 채택 합의에서 인용 가능하도록 §8 강화
   205	
   206	본 갱신 = *MVP 조건 명시* + *cross-reference 강화* + *모법 ADR 권위 확정* 한정. **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** + **핵심 결정 (옵션 B 채택) 변경 0건** → 단축 합의 적격 (사용자 명시 답습).
   207	
   208	---
   209	
   210	## 7. 합의 결과
   211	
   212	### 7.1 초기 3+1 합의 (2026-05-04, 변경 0건)
   213	
   214	P1 (Option β) 합의의 일부로 다뤄짐. 별도 ADR 작성 의무는 Bβ-4 항목.
   215	
   216	| 출처 | 핵심 |
   217	|------|------|
   218	| Agent C | "v2.0 진입조건을 정량 트리거로 명시 — 매몰비용 누적 회피" |
   219	| Reviewer | "Option β 채택 시 진입조건 ADR 작성 의무 (Bβ-4)" |
   220	

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-008-hermes-adoption-decision.md | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-008: Hermes Agent 도입 결정 (Option B)
     2	
     3	**상태**: 승인 (3+1 합의 완료, 사용자 Option B 선택)
     4	**날짜**: 2026-05-04
     5	**의사결정자**: 사용자 + 3+1 에이전트 합의
     6	
     7	---
     8	
     9	## 맥락 (Context)
    10	
    11	사용자가 "Hermes Agent를 메인 오케스트레이터로 도입, Claude Opus 4.7과 GPT-5.5를 서브 LLM으로 활용"하는 시스템 진화를 제안. 현재 시스템은 Claude Code 단일 의존이며, 사용자는 모델/구독 교체의 자유를 강하게 요구함 (Provider Liquidity 하드 제약: "Claude Max 사용중이지만 모델 성능에 따라 구독 취소나 모델 변경이 용이해야함").
    12	
    13	## 결정 (Decision)
    14	
    15	**Option B 채택**: Hermes를 메인 오케스트레이터로 단계 도입하되, **6개 차단조건이 모두 충족된 후에만 다음 Phase로 진입**한다.
    16	
    17	### 6개 차단조건 (비협상)
    18	1. **SQLCipher**로 Hermes SQLite 암호화 + redaction 필터 (헌법 제8조 준수)
    19	2. **JSONL export 표준** + 메모리/스킬 마이그레이션 경로 정의 (Hermes lock-in 회피)
    20	3. v0.x API **버전 핀** + 회귀 테스트 + 카나리 환경
    21	4. **provider 어댑터 1개 추상화** + 분기 코드 금지 (depcruise로 강제)
    22	5. **최소 2 provider always-on** (단일 구독 의존 금지)
    23	6. Docker **격리 + egress 화이트리스트**
    24	
    25	### 단계 마이그레이션
    26	- **Phase 1** (1~2주): Hermes worktree 설치, **API 키만 사용**(OAuth 직결 금지), 비핵심 작업 검증
    27	- **Phase 2** (2~4주): Layer 5(3+1 합의)만 Hermes 서브에이전트로 이전 (A=Claude / B=GPT / C=로컬)
    28	- **Phase 3** (조건부): Hook 계층 watchexec 재구축 + provider 어댑터 본격 적용. **선결조건**: Phase 2 메트릭 ≥ 현 시스템
    29	
    30	## 선택지 (Options Considered)
    31	
    32	### Option A: LiteLLM 우선 + Hermes 좁은 PoC (3+1 권장 ★★★★★)
    33	- 장점: Provider Liquidity 본업 충족, 기존 SDD/TDD 자산 100% 보존, 즉시 시작
    34	- 단점: Hermes 셀프-임프루빙 가치 일부 늦게 확인
    35	
    36	### Option B: Hermes 메인 + 6개 차단조건 단계 도입 ⭐ **채택**
    37	- 장점: 사용자 원안 직접 실현, 셀프-임프루빙 빠른 체험
    38	- 단점: 차단조건 6개 미충족 위험, v0.x 불안정, Hook 재구축 공수 미지수
    39	
    40	### Option C: 6개월 보류
    41	- 장점: 신생 프레임워크 리스크 회피
    42	- 단점: 다중 LLM 활용·Liquidity 개선 지연
    43	
    44	## 근거 (Rationale)
    45	
    46	3+1 합의는 Option A를 1순위로 권장했으나, 사용자가 의식적으로 Option B를 선택. 사용자 의지·선호 존중. 단, 6개 차단조건은 **비협상** — 미충족 시 자동 NO-GO하며, Hermes 도입을 중단하고 Option A로 자동 폴백한다.
    47	
    48	## 3+1 에이전트 합의 결과
    49	
    50	| 에이전트 | 의견 | 핵심 근거 |
    51	|---------|------|----------|
    52	| Agent A (구현) | 조건부 GO | 8-Layer 통합 MEDIUM, Phase 1·2 즉시 가능, Phase 3는 Hook 재구축 PoC 성공 시 |
    53	| Agent B (품질) | GO with strict conditions | R1 학습루프 평문(CRITICAL), R2 Hermes lock-in(CRITICAL), 6개 차단조건 미충족 시 HOLD |
    54	| Agent C (대안) | LiteLLM 우선 권장 (Option A) | Liquidity는 도구 추상화 문제, Hermes만의 솔루션 아님 |
    55	| **Reviewer** | **Option A 1순위, B는 차단조건 충족 시 가능** | 메타 한계 보정으로 C에 가중치, 사용자 선호 시 B 진행 가능 |
    56	
    57	## CRITICAL 위험 (운영 중 상시 감시)
    58	
    59	- **R1 학습루프 평문 누적**: Hermes SQLite FTS5에 사용자 컨텍스트·LLM 응답·환경변수 echo가 평문 영구 저장. **헌법 제8조 직접 위반**. 차단조건 #1 미구현 시 자동 NO-GO.
    60	- **R2 Hermes 자체 lock-in**: 누적 학습 결과(스킬/메모리/프로필)는 Hermes 떠나면 손실. Provider Liquidity 정신 위반. 차단조건 #2 미정의 시 자동 NO-GO.
    61	- **A-meta ChatGPT Pro Codex CLI OAuth ToS 위반 가능성**: 위반 시 구독 강제 해지 → 시스템 정지. **API 키 경로만 사용**.
    62	- **R4 Claude Max OAuth race**: 다수 미해결 버그(#15080, #6475, #12905, #10575) — Hermes 동시 호출 시 무한 인증루프 가능. API 키 경로 우선.
    63	- **R8 단일 구독 의존**: 어떤 단계에서도 single point of failure 금지. 차단조건 #5로 강제.
    64	
    65	## 메타 한계 (사용자 인지 필요)
    66	
    67	본 합의는 3 Claude 에이전트가 작성. Hermes(외부 도구)에 대한 평가에 친화 편향 가능. Reviewer가 Agent C 회의적 입장에 의식적 가중치 부여로 보정함. Option B 진행 중에도 외부(비-Claude) 검증 권장.
    68	
    69	## 결과 (Consequences)
    70	
    71	- **긍정적**: 다중 LLM 환경 구축, 셀프-임프루빙 학습루프 도입 시도, Provider Liquidity 강제 메커니즘 정착
    72	- **부정적**: 신생 프레임워크 리스크 감수, Hook 재구축 공수 발생, v0.x API 변동 대응 부담, R1/R2 차단조건 미충족 시 전면 폴백 위험
    73	- **주의사항**:
    74	  - 6개 차단조건 중 1개라도 미충족 시 도입 중단 → Option A 자동 폴백
    75	  - 진행 중에도 정기적 재평가 (Phase 종료마다)
    76	  - 차단조건 충족 검증은 별도 SDD 문서로 명세 예정
    77	  - Provider Liquidity 위반 패턴 6종(모델명 분기/provider별 후처리/스킬 내 모델 가정 등)은 depcruise 룰로 정적 차단
    78	
    79	---
    80	
    81	**관련 문서** (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only):
    82	
    83	### 합의 보고서 / 헌법
    84	
    85	- `docs/review/3plus1-consensus-2026-05-04-hermes.md` (3+1 합의 보고서 전문)
    86	- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
    87	- `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` (Provider Liquidity 영구 기억)
    88	
    89	> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S3 답습]**: 본 line 86 표기 "제5조 관용 (Provider Liquidity, 비협상)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") 中 ADR-008 정정 자격 직접 발효 (R-S3 CRITICAL). ADR-008 = ADR-011 직접 모법 (ADR ↔ ADR 부록 B Amendment 패턴). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 87/98/107/274/329/366/370 (P2 cross-ref + P3 본문) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
    90	
    91	### Hermes 도입 설계 (P2)
    92	
    93	- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건. archive 합의: `docs/review/3plus1-consensus-2026-05-09-p2-v2-archive-decision.md`)
    94	- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — P2 v2 §2.1.3 가정 (외부 pre-record hook) 폐기 + R-2~R-7 evidence 흡수 + G1b PASS 권위 + Hermes PMO 구조 사전 정의 (활성화 *아님*) + G2/G3/G4 entry/exit. **본 ADR-008 의 Option B 단계 마이그레이션은 P2 v3 §2.6 + §11.1 + §2.6.1 12 조건 PMO 격상 체크리스트로 운영 절차화** (인간 전문 리뷰 의무 명문화, P2 v3 §2.6 단계 5.5)
    95	- `docs/architecture/system-identity-prequel.md` (**Archived 2026-05-09 후속 8** — AI Dev Company OS 정체성 직접 권위 출처 영구 보존. archive 합의: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md`)
    96	
    97	### Provider 추상화 / Adapter (차단조건 #4)
    98	
    99	- `docs/architecture/llm-providers-design.md` (P1 v2, LiteLLM facade — Option β 채택)
   100	- **`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`** (C-N 갱신 2026-05-09 후속 4 — P1 facade MVP 진입조건 명시 + **Hermes PMO ↔ provider 분리 영구 권위 (§2.3)** + **Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1 (§5)** + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference). 본 ADR-008 차단조건 #4 (provider 어댑터 추상화) 의 *Hermes PMO ↔ provider 분리* 권위 출처
   101	
   102	### 차단조건 #1 충족 (수단/목적 분리)
   103	
   104	- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-008 부록 B Amendment R1 specific 갱신의 권위 근거. §2.1 (a)~(d) 4조건 + §2.2 G1a/G1b 분리 + §2.3 Hermes ≠ root of trust 영구 권위 + §2.4 T1/T2/T3 영구 권위)
   105	- `docs/decisions/ADR-010-sqlcipher-vault-key-management.md` (SQLCipher Vault HSM 키 관리 — 차단조건 #1 키 관리 측면)
   106	
   107	### Evidence 무결성 (2026-05-09 후속 3 PR-2 신규 발행)
   108	
   109	- **`docs/decisions/ADR-012-evidence-ledger-protection.md`** (Evidence Ledger Protection — 본 ADR-008 차단조건 #2 (JSONL export 표준) 의 *Evidence Ledger 무결성* 강화 권위. 12 보호 원칙 + Layer 1~5 다층 강제 + RFC 8785 JCS + Hermes 변조 차단 매트릭스 4항목 + Provider Liquidity 5-way Layer 5)
   110	- 신규 위반 경로 P10 (Evidence Forgery) 정식 등록 (G2 §1.2.6, 2026-05-09 후속 5)
   111	
   112	### 4 게이트 정식 산출 (2026-05-09 Design/Governance Gate PASS Bundled)
   113	
   114	- `docs/architecture/governance-preconditions.md` (G2, **Design/Governance Gate PASS Bundled, 2026-05-09**) — 6 거버넌스 사전조건 GP-1~GP-6 + §1.2.6 P10 Evidence Forgery 정식 등록. **GP-1 = G1b PASS evidence 흡수 (Implementation/Runtime PASS), GP-2~GP-6 = Design PASS / Implementation Pending**
   115	- `docs/architecture/hermes-not-root-of-trust-runtime.md` (G3, **Design/Governance Gate PASS Bundled**) — 권위 위계 운영 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + Hermes 변조 차단 매트릭스 4항목. **운영 구현 = Design PASS / Implementation Pending**
   116	- `docs/architecture/provider-agnostic-memory-skill-design.md` (G4, **Design/Governance Gate PASS Bundled** + §4.2 11 필드 schema + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강 PR-2). **라운드트립 + migration script = Design PASS / Implementation Pending**
   117	- `docs/phase0/redaction-verification-sop.md` (R-7 SOP — G1b PASS 정식 충족 절차)
   118	
   119	### 부록 B §B.6 정식 충족 절차 cross-reference (G1b PASS + G2 GP-1 흡수)
   120	
   121	- 부록 B §B.6 R-3 ~ R-7 6단계 ✅ 완료 (2026-05-06 ~ 2026-05-07 Part 1) + R-6 GitHub Actions actual run `25482284523` PASS (24초, 42/42, leak 0) + R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only (2026-05-07) → G1b CONDITIONALLY PASS → **PASS** 승격 + Phase 1 acceptance PARTIAL → **PASS** 선언. **G2 GP-1 = G1b PASS evidence 흡수** (Tier-1 한정, 2026-05-09 G2 정식 PASS 시점)
   122	
   123	---
   124	
   125	## 부록 A — 검증 결과 (2026-05-04)
   126	
   127	Phase 1 진입 전 사실 확인 작업 2건 완료. 결과 CRITICAL 위험 2건이 다운그레이드되었으나, 차단조건 6개는 그대로 유지(방어 자세).
   128	
   129	### A.1 ChatGPT Pro Codex CLI ToS 검증
   130	- **공식 지원**: Hermes는 OpenAI Codex `device code` OAuth flow를 정식 지원. credentials는 `~/.hermes/auth.json`에 저장, `~/.codex/auth.json`에서 import 가능
   131	- **개인 단일 사용자 시나리오**: ToS 위반 위험 **LOW** — Codex CLI 자체와 동등 사용
   132	- **금지 사례**: "Reselling access" 또는 "third-party services에 ChatGPT 전력 공급". 본 프로젝트는 개인 사용이므로 해당 없음
   133	- **정책 변동성**: OpenAI/Anthropic가 third-party 도구의 구독 집계를 최근 제한한 사례 존재 → API 키 경로 우선 정책은 그대로 유지
   134	- **A-meta 위험 등급**: CRITICAL → **MEDIUM** (정책 변동 모니터링 필요)
   135	
   136	### A.2 Hermes JSONL Export 검증
   137	- **공식 명령어**: `hermes sessions export backup.jsonl` 존재. 전체/플랫폼별/단일 세션 export 지원, full message history 포함
   138	- **데이터 저장소 정정**: ChromaDB는 사용하지 않음. **SQLite + FTS5 단일** — 암호화는 SQLCipher 단일 적용으로 충분 (차단조건 #1 단순화)
   139	- **마이그레이션 도구**: `hermes claw migrate` (OpenClaw → Hermes) 존재. 역방향 export는 sessions 단위로 가능
   140	- **스키마 버전 관리**: `schema_version` 테이블 존재
   141	- **R2 위험 등급**: CRITICAL → **HIGH** (skills/memory 범위는 P1 설계 단계에서 추가 검증)
   142	- **추가 검증 항목**: `hermes sessions export`가 sessions만 다루는지, agent-curated memory와 skills도 포함하는지 P1에서 확인 필요
   143	
   144	### A.3 차단조건 영향
   145	6개 차단조건은 **그대로 유지**. 검증 결과는 충족 가능성을 높였을 뿐 의무를 약화하지 않음.
   146	- #1 SQLCipher: 적용 대상이 SQLite 단일 → 구현 단순화
   147	- #2 JSONL export: 공식 명령어 활용. skills/memory 범위 보강 필요
   148	- #3 버전 핀: 그대로
   149	- #4 어댑터 추상화: 그대로 (P1 설계의 핵심)
   150	- #5 2 provider always-on: 그대로
   151	- #6 Docker 격리: 그대로
   152	
   153	---
   154	
   155	## 부록 B — Amendment (2026-05-06): R1 해석 갱신 (수단/목적 분리)
   156	
   157	**상태**: 갱신 (단축 합의 — Reviewer-only)
   158	**날짜**: 2026-05-06
   159	**근거 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
   160	**근거 Phase 0 evidence**: R-1 FAIL (`docs/phase0/day2-r1-redaction-location-verification.md`), R-2 PASS (`docs/phase0/day3-r2-sqlite-trigger-poc.md`)
   161	**근거 합의**: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
   162	
   163	### B.1 R1 비협상 핵심 재정의
   164	
   165	R1의 비협상 핵심은 **특정 외부 hook 구현이 아니라, AI 학습 루프/메모리 DB에 비밀값이 평문으로 영구 저장되지 않도록 차단하는 결과**이다.
   166	
   167	본 Amendment 이전 부록 A R1 텍스트는 "외부 pre-record hook"을 수단으로 가정한 표현을 포함했다. 본 Amendment는 그 가정을 ADR-011 §2.1 수단/목적 분리 원칙에 따라 갱신한다.
   168	
   169	### B.2 G1a / G1b 분리 관리
   170	
   171	Hermes native redaction이 DB INSERT 경로에 적용된다는 기존 가정은 **R-1에서 FAIL로 판정**되었다.
   172	
   173	그러나 R-2 PoC에서 SQLCipher BEFORE INSERT trigger 기반 DB-level fallback이 plaintext secret persistence를 차단할 수 있음이 실증되었으므로, G1은 다음과 같이 분리 관리한다:
   174	
   175	- **G1a**: Hermes native redaction applies before DB INSERT — **FAIL** (폐기)
   176	- **G1b**: DB-level fallback prevents plaintext secret persistence — **PASS by R-2 PoC** (정식 충족은 R-3~R-7 후)
   177	
   178	정식 충족 조건은 ADR-011 §2.2 G1b 정식 충족 조건 표를 따른다.
   179	
   180	### B.3 권위화 출처
   181	
   182	이 해석은 **ADR-011 Means-vs-Ends Redaction Principle**에 의해 권위화된다. 본 Amendment는 ADR-011 §2.1~§2.3을 ADR-008 R1 specific 갱신으로 적용한 것이며, 일반 원칙 본문 해석은 ADR-011을 우선 참조한다.
   183	
   184	### B.4 본 Amendment의 의미 (오해 방지)
   185	
   186	본 Amendment는 "Hermes가 안전하다"는 선언이 **아니다**. 정확한 의미는 다음과 같다:
   187	
   188	1. Hermes native redaction은 DB INSERT 보호 수단으로 **신뢰하지 않는다**.
   189	2. DB INSERT 경로는 SQLCipher trigger 기반 fallback으로 **별도 보호한다**.
   190	3. **Hermes는 root of trust가 아니다** (ADR-011 §2.3 권위 위계 명문화).
   191	
   192	### B.5 6 차단조건 영향
   193	
   194	ADR-008 결정 본문 §6 차단조건 #1 (SQLCipher + redaction 필터) 의 충족 메커니즘은 다음으로 갱신된다:
   195	
   196	| 메커니즘 | 위치 | 신뢰도 |
   197	|---------|------|------|
   198	| SQLCipher 암호화 (디스크) | DB 파일 | 기존대로 |
   199	| Hermes native redaction | 로그 / LLM 송신 / 도구 출력 | 보조 (DB 차단 책임 없음) |
   200	| **SQLCipher BEFORE INSERT trigger + REGEXP UDF** | **DB INSERT 경로** | **Primary (G1b)** |
   201	
   202	차단조건 #2~#6은 변경 없음. 6 차단조건 자체의 비협상성은 유지된다 — 본 Amendment는 #1 충족 *수단*을 ADR-011 (a)~(d) 4조건 하에 재정의한 것이다.
   203	
   204	### B.6 정식 충족 절차
   205	
   206	차단조건 #1 정식 exit 기준은 다음 6단계 완료를 요한다 (R-4.1 은 R-4 추가 격리 PoC 분기로 ADR-011 §2.1 (b) 직접 충족 산출):
   207	
   208	```
   209	R-3   ✅ 본 Amendment 발행 (2026-05-06)
   210	R-4   ✅ 패턴 동등성 비교 + gap 식별 + 보충 권고 — `docs/architecture/redaction-pattern-equivalence.md` (2026-05-06)
   211	R-4.1 ✅ Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS — `docs/phase0/r4-1-trigger-extension-evidence.md` (2026-05-06)
   212	R-5   ✅ canary 재검증 트리거 설계 — `docs/architecture/canary-recheck-design.md` (2026-05-06)
   213	R-6   ✅ CI/nightly canary regression workflow 구현 — `.github/workflows/r2-canary.yml` (2026-05-06, commit `bbcc1af`; **GitHub Actions actual run 은 push 후 별도 검증 의무**)
   214	R-7   ✅ Phase 1 합격 SOP — `docs/phase0/redaction-verification-sop.md` (2026-05-06)
   215	```
   216	
   217	**6단계 작성 완료 + R-6 actual run PASS + 단축 합의 APPROVE → G1b 정식 PASS 도달** (2026-05-07):
   218	
   219	- ✅ R-6 GitHub Actions 실제 run PASS — run ID `25482284523` (commit `939125b` 기준 24초 완료, 모든 step ✓)
   220	  - 1차 run (`25480443667`) FAIL 은 docker compose stdout prefix JSON parse infra bug — 보안 위반 / catalog drift / 실 secret 노출 / CI 자동 정책 변경 모두 *아님* (사용자 단축 합의 결정 답습). Fix `939125b` 는 workflow YAML 1 file 한정 (`r4_1_poc.py` / Tier-1 catalog / trigger UDF / redaction config 변경 0건)

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# 6 Governance Preconditions (G2) — Design/Governance Gate PASS (Bundled, 2026-05-09)
     2	
     3	> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 G2 — "헌법 8조·5조-2(Provider Liquidity, 비협상) 위반 경로 P1~P8 강제 메커니즘 매핑 + 6 거버넌스 사전조건 GP-1~GP-6 정의 + 각 사전조건의 entry/exit 기준" 정의. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
     4	>
     5	> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 문서 구조 / 권위 위계 / 6 GP 정의 / 강제 메커니즘 분류 매트릭스 / Entry·Exit 기준 정의의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — GP-2~GP-6 의 PoC 실증 / CI 강제 / runtime hook 구현 / Evidence Ledger 검증은 *별도 합의* 로만 발생.
     6	>
     7	> **GP 별 상태 (P0 조건 C-B, 5/5 입력 일치)**:
     8	> - **GP-1**: PASS (G1b PASS evidence 흡수, 단 Tier-1 한정 — Tier-2/Tier-3 catalog 확장은 후속, Claude C-7)
     9	> - **GP-2 ~ GP-6**: **DESIGN PASS / IMPLEMENTATION PENDING** (각 GP 의 PoC 실증 + (a)~(e) 5조건 충족 검증은 별도 합의)
    10	>
    11	> **§1.2.6 P10 Evidence Forgery 정식 등록 (2026-05-09 후속 5 단축 합의 APPROVE Reviewer-only)**: ADR-012 §1.4 cross-reference + Hermes 변조 차단 매트릭스 4항목 + Layer 1~5 enforcement.
    12	>
    13	> **§1.2.7 P11 Supply-chain Compromise 정식 등록 (2026-05-12 단축 합의 적격 — Reviewer-only)**: Gate Enforcement Layer 보호 보강 (G3 §2.6, 2026-05-12 commits `3e46440` + `fa2cbdb`) 시점 트리거 답습. 5 측면 (Dependency Pinning Integrity / Checksum / Action SHA Pin / Docker Digest Pin / Vendor Change Auto-recheck) + 5 Layer 다층 강제 + Enforcement Tool Self-protection + 5 기준 (감지/차단/Evidence/Rollback/사용자 승인). **Hermes PMO 격상 *전* precondition 권장 (blocking 아님)** — Implementation/Runtime PASS 영역의 우선 권장 항목 (Claude C-3 + C-6 답습). 외부 LLM Gap-N 중 N-5 (supply chain / dependency integrity) 답습. **본 §1.2.7 = P11 row 추가 한정 — runtime code 구현 / CI workflow 수정 / hook 구현 / 신규 GP 신설 / 신규 ADR 발행 / Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS / G2/G3/G4 PASS 재선언 / ADR 본문 자동 갱신 모두 본 작업 범위 외** (사용자 명시 답습).
    14	>
    15	> **P2 v3 (`hermes-adoption-design-v3.md`) = Adopted (Design Adoption only, 2026-05-09 후속 6)** 후속 권위. 본 G2 = P2 v3 §4 (G2 정의) + P2 v3 §3.1.4 Implementation Pending 표 + P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화 답습.
    16	>
    17	> **P2 v2 (`hermes-adoption-design.md`) = Archived (옵션 A 최소 침습, 2026-05-09 후속 7)** + **`system-identity-prequel.md` = Archived (옵션 A, 2026-05-09 후속 8)** — 본 G2 cross-reference 영향 0건 (path 변경 0건).
    18	>
    19	> **Hermes PMO 격상은 본 PASS 에 포함되지 않는다** (사용자 명시 답습) — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 (Human-in-the-loop) + 사용자 명시 결정 후 별도 (P2 v3 §2.6.1 12 조건 PMO 격상 체크리스트 답습). G2 운영 구현 PASS / ADR 본문 자동 갱신 / archive 자동 처리도 본 PASS 미포함.
    20	
    21	**작성일**: 2026-05-07
    22	**Status (2026-05-07 통합 합의)**: **Design/Governance Gate PASS (Bundled, 2026-05-07)** — `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` (4/4 입력 만장일치 APPROVE WITH CONDITIONS — Agent A/B/C + 외부 LLM GPT-5.5 Thinking, 12 통합 조건 + Gap-N 6건 흡수 처리). 본 PASS 는 Design/Governance Gate 한정 — Implementation/Runtime PASS / Operational Readiness PASS / Hermes PMO 격상 / P2 v3 정식 채택 모두 미포함.
    23	**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G3 + G4 — 2026-05-07 통합 합의의 후속 reaffirmation)
    24	**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
    25	**P10 정식 등록 합의**: `docs/review/3plus1-consensus-2026-05-09-g2-p10-evidence-forgery.md` (2026-05-09 후속 5 단축 합의 APPROVE Reviewer-only)
    26	**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상, `148fbbe` 신설) — 본 §1.1 명명 정정 *역할 종료* (cross-ref block 답습)
    27	**상위 결정**: ADR-008 (Hermes 도입 Option B) 6 차단조건, ADR-011 (수단/목적 분리, §2.3 권위 위계, §2.4 T1/T2/T3), **ADR-009 C-N (P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행)**
    28	**관련 설계**: **`hermes-adoption-design-v3.md` §4 (G2 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3.3 / §4.2 (**Archived 2026-05-09 후속 8**, 본 ADR-011 §2.3 영구 권위 승격 답습으로 권위 보존), `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
    29	**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Agent B 6 거버넌스 사전조건 + 8 위반 경로 P1~P8 식별), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G2 정식 PASS 합의), `docs/review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` (P2 v3 정식 채택 풀 3+1 + 외부 LLM 2건 — 본 G2 = P2 v3 §4 답습 권위)
    30	**관련 evidence**: R-2 ~ R-7 + R-6 actual run `25482284523` (G1b PASS)
    31	
    32	---
    33	
    34	## 0. 본 초안의 범위
    35	
    36	### 0.1 본 초안이 *하는* 것
    37	
    38	1. "헌법 5조 (Provider Liquidity)" 명명 정정 (프로젝트 관용 답습 + 1회 명시)
    39	2. 헌법 8조 + Provider Liquidity 위반 경로 **P1~P8** 정의 (Agent B 합의 §29~§30 직접 기반)
    40	3. **GP-1 ~ GP-6** 6 거버넌스 사전조건 정의 + P1~P8 매핑
    41	4. 각 GP의 강제 메커니즘 분류 (계산적 / 추론적 / 자동 롤백) — 합의 §31 "Hermes 금지 8가지 × {계산적/추론적/자동 롤백}, 8 중 7 계산적 가능" 답습
    42	5. 각 GP의 Entry / Exit 기준 (ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 + (e) 합의 APPROVE)
    43	6. 각 GP의 산출 후보 + 의존 ADR cross-reference 후보
    44	7. 메타 안전장치 — 본 6 사전조건 자체의 무결성 보호 (Hermes 자기참조 차단)
    45	8. G2 통합 entry/exit 기준 종합
    46	
    47	### 0.2 본 초안이 *하지 않는* 것 (사용자 명시 답습)
    48	
    49	1. ❌ **G2 PASS 선언** — 본 초안은 *정의*까지만, GP-1~GP-6 각각의 (a)~(e) Exit 기준 충족 검증은 후속
    50	2. ❌ **G3 / G4 PASS 선언**
    51	3. ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 통과 + 사용자 명시 결정 후 별도
    52	4. ❌ **P2 v3 정식 채택 선언** — `hermes-adoption-design-v3.md` 헤더 DRAFT 그대로 유지
    53	5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음
    54	6. ❌ **P2 v2 (`hermes-adoption-design.md`) archive 처리** — v3 정식 채택 시점에
    55	7. ❌ **`system-identity-prequel.md` archive 처리** — v3 정식 채택 시점에
    56	8. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
    57	9. ❌ **사전조건별 PoC 자동 실행** — 본 초안은 PoC 설계 *기준*까지, 실 PoC는 후속
    58	10. ❌ **Tier-2 / Tier-3 catalog 확장** — 별도 합의
    59	
    60	### 0.3 본 초안의 단계별 정식화 절차 (예정)
    61	
    62	| # | 단계 | 산출 | 시점 |
    63	|---|------|------|------|
    64	| 1 | 본 초안 작성 (현 단계) | 본 문서 (DRAFT) | 2026-05-07 |
    65	| 2 | 사용자 검토 + Reviewer-only 단축 검토 (DRAFT 적격) | 검토 보고서 | 사용자 명시 결정 후 |
    66	| 3 | 각 GP entry 진입 + PoC 작성 + Exit 기준 (a)~(e) 충족 검증 | 6 PoC 산출 + 각 GP별 evidence | GP별 순차 또는 병행 |
    67	| 4 | G2 PASS 합의 가동 (단축 또는 풀 3+1) | `docs/review/3plus1-consensus-YYYY-MM-DD-g2.md` | 단계 3 완료 후 |
    68	| 5 | G2 PASS 선언 + ADR cross-reference 갱신 (G3/G4와 묶음 가능) | 별도 PR | 단계 4 후 |
    69	
    70	본 초안 자체는 단계 1까지만 처리. 단계 2~5는 본 초안 범위 외.
    71	
    72	---
    73	
    74	## 1. 명명 정정 + 위반 경로 P1~P8 정의
    75	
    76	### 1.1 "헌법 5조 (Provider Liquidity)" 명명 정정 (선행, 1회 명시)
    77	
    78	**관용 표현**: ADR-008 / ADR-011 / system-identity-prequel / 본 v3 모두 "헌법 제5조-2 (Provider Liquidity, 비협상)" 표현 사용 ((g1-N-1) commit `148fbbe` 후 헌법 본문 직접 등재 완료).
    79	
    80	**실제 헌법 본문**:
    81	- `docs/constitution/PROJECT_CONSTITUTION.md` 제5조 본문: **"코드 품질 원칙"** (5개 항목, 단일 책임 / 가독성 / 중복 제거 / 외부 입력 검증 / 린터)
    82	- 제8조 본문: 보안 원칙 (4개 항목) — 관용과 일치
    83	
    84	**Provider Liquidity 실제 권위 출처**:
    85	- `~/.claude/projects/.../memory/feedback_provider_liquidity.md` (사용자 비협상 메모리)
    86	- ADR-008 본문 + 부록 A.1 (구독 교체 자유 + Hermes lock-in 차단)
    87	- 본 프로젝트 모든 헌법-동급 제약으로 보호됨 (관용 "헌법 5조"로 인용)
    88	
    89	**본 초안의 처리**:
    90	- 본 초안은 **프로젝트 관용 답습** — 본문 내 "헌법 5조 (Provider Liquidity)" 표현 그대로 사용
    91	- 단, 본 §1.1 1회 명시로 명명 불일치 인지 + 향후 *헌법 본문 갱신* 또는 *ADR-012 (가칭) Provider Liquidity 정관 흡수* 등 정정 후보 제시 (본 초안 범위 외)
    92	- 후속 작업: 헌법 본문 갱신 또는 ADR Amendment 결정은 풀 3+1 합의 영역 (T3 변경 — ADR-011 §2.4)
    93	
    94	**[Cross-reference Block — (g1-N-3-gov) (ii-c) verbatim 부분 정정 + R-4 답습]**: 본 §1.1 = (g1-N-1) commit `148fbbe` 후 **역할 종료**. 헌법 본문 line 75~80 "제5조-2: Provider Liquidity 원칙 (비협상)" 신설 완료 — 본 §1.1 line 91 "정정 후보 제시 (본 초안 범위 외)" 부분 obsolete. 단 본 §1.1 의 *역사적 의의* (관용 명명 불일치 *최초 명문 식별* + (g1-N) cycle chain 의 *직접 동기 출처*) 영구 보존. 후속 인용 chain (line 26 + line 38 + line 835) 모두 본 §1.1 cross-ref 답습 자격. (ii-a) 전체 삭제 / (ii-b) 본문 수정 / (ii-d) archive 표시 = 사전 기각 (합의 기각-3, A-B2 cascading failure risk + (10-f) sub-boundary).
    95	
    96	### 1.2 위반 경로 P1~P8 정의
    97	
    98	> **본 §1.2는 합의 §29~§30 (Agent B "헌법 8조·5조 위반 경로 8건 P1~P8" + B-P5/P7 cross-reference) 의 본 초안 명시 enumeration 이다.** 합의 보고서에는 P1~P8 enumeration 이 명시되지 않아 본 §1.2 가 *최초 명시* — 후속 합의 시 GP 매핑 적정성 검증 대상.
    99	
   100	#### 1.2.1 헌법 제8조 (보안) 위반 경로 5건 (P1~P5)
   101	
   102	| # | 경로 | 시나리오 | 헌법 8조 어느 항 | G1b 와 관계 |
   103	|---|------|---------|--------------|----------|
   104	| **P1** | **DB INSERT 평문 secret 누적** | Worker Agent 가 LLM 응답·환경변수 echo·tool output 을 SessionDB / Memory DB / Skill DB 에 INSERT 시 평문 secret 영구 저장 | 8조 #1 (하드코딩 차단) + 8조 #2 (비밀 관리) | **G1b PASS 로 차단** (SQLCipher trigger + Tier-1 42 catalog) |
   105	| **P2** | **로그/LLM 송신 경로 평문 노출** | Hermes / Worker 가 secret 을 stdout / stderr / log file / LLM API request body 에 노출 | 8조 #2 | Hermes native redaction 보조 (ADR-011 §2.3 운영 함의 #2) |
   106	| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + entrypoint stat 검증 (35번째 entry R-S1 정정 답습) |
   107	| **P4** | **비밀값 하드코딩** | secret 이 git commit 본문 / 환경변수 default / docker-compose.yml 평문 / Skill 정의 평문 등에 영구 기록 | 8조 #1 (직접) | gitleaks / detect-secrets / pre-commit hook |
   108	| **P5** | **외부 입력 미검증/이스케이프** | Worker Agent 또는 Hermes 출력이 *내부* 처럼 취급되어 SQL injection / command injection / path traversal 등 발생 | 8조 #3 (직접) | **헌법 8조 #4 — 보안 변경은 3+1 합의** + 헌법 5조 #4 (외부 입력 검증) |
   109	
   110	#### 1.2.2 Provider Liquidity (관용 헌법 5조) 위반 경로 3건 (P6~P8)
   111	
   112	| # | 경로 | 시나리오 | Provider Liquidity 어느 측면 | 관련 ADR-008 차단조건 |
   113	|---|------|---------|--------------------------|------------------|
   114	| **P6** | **Hermes 자체 SDK 직접 import** | Worker Agent / Skill / Hermes plugin 코드가 `import hermes_agent.*` 또는 `import litellm` 직접 import 로 P1 facade 우회 | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (provider 어댑터 추상화) |
   115	| **P7** | **모델명/Provider 분기 코드** | `if model == "claude-opus-4-7": ... elif model == "gpt-5.5": ...` 또는 provider 별 후처리 분기 / Skill 내 모델 가정 (ADR-008 §결과 §주의사항 6종) | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (P1 v2 depcruise 룰) |
   116	| **P8** | **Memory / Skill Hermes 종속 형식** | Skill 정의 / Memory entry 가 Hermes 자체 schema (binary protocol / proprietary key) 사용으로 다른 오케스트레이터 import 불가 | Provider 교체 자유 (학습 자산 유지) | **차단조건 #2** (JSONL export) + **G4** (Provider-agnostic Memory/Skill 형식) |
   117	
   118	#### 1.2.3 정식 위반 경로 합산 (P1~P8 + P10 + P11, 2026-05-12 갱신)
   119	
   120	```
   121	헌법 8조 (보안) 위반 경로 = 5건 (P1~P5)
   122	Provider Liquidity 위반 경로 = 3건 (P6~P8)
   123	Evidence Integrity 위반 경로 = 1건 (P10)            ← 2026-05-09 후속 5 정식 등록
   124	Supply-chain Integrity 위반 경로 = 1건 (P11)        ← 2026-05-12 정식 등록
   125	─────────────────────────────────────────────────
   126	정식 위반 경로 합계 = 10건 (P1~P8 + P10 + P11)     ← ✅ 합의 §29~§30 일치 + ADR-012 발행 시점 P10 흡수 + Gate Enforcement Layer 보호 보강 시점 P11 흡수
   127	Deferred candidates = 2건 (P9 / P12, §1.2.5)
   128	```
   129	
   130	P10 정식 등록 = ADR-012 (Evidence Ledger Protection) 발행 시점 (2026-05-09 후속 3 PR-2) 트리거 답습 — §1.2.5.2 명시 "P10 정식 등록 시점 = PR-2 신규 ADR-012 발행 시점" 답습. 본 §1.2.6 답습.
   131	
   132	P11 정식 등록 = Gate Enforcement Layer 보호 보강 (2026-05-12, commits `3e46440` + `fa2cbdb`) 시점 트리거 — §1.2.5 명시 "P11 정식 등록 시점 = SBOM + supply-chain 검증 PoC 합의 시점, Hermes PMO 격상 *전* 권장" + 본 보강 작업의 Layer 2 (CI / hook / test) enforcement mechanism 이 supply-chain compromise 로 무력화 가능 + 외부 LLM Gap-N 중 N-5 supply chain / dependency integrity 답습. 본 §1.2.7 답습.
   133	
   134	#### 1.2.4 본 §1.2 가 *다루지 않는* 위반 경로
   135	
   136	본 §1.2는 *헌법 8조 + Provider Liquidity* 위반 경로에 한정. 다음은 본 G2 범위 외:
   137	- 헌법 1조 (SDD) / 2조 (TDD) 위반 — 일반 Harness Layer 1~4 hook 가 다룸
   138	- 헌법 4조 (3+1 합의) 위반 — Layer 5 + 사용자 결정
   139	- 헌법 7조 (투명성) 위반 — Layer 0 (CLAUDE.md) + ADR 절차
   140	- 헌법 10조 (문서 일관성) 위반 — `docs/INDEX.md` + 의존 관계 매트릭스
   141	- ADR-011 §2.4 T3 (자동 정책 변경) 위반 자체 — **G3** ("Hermes ≠ root of trust" 운영 구현) 범위. 본 G2 §9 메타 안전장치에서 *interface*만 명시
   142	
   143	#### 1.2.5 P9 ~ P12 deferred candidates (C-I 흡수 — 2026-05-09 후속 2)
   144	
   145	> **본 §1.2.5 는 합의 보고서 §11.2 P1 조건 C-I 흡수** (출처: GPT 조건 7 + Claude C-4). 본 §1.2.1 ~ §1.2.3 의 *현재 enumeration P1~P8* 외에 **누락 위반 경로 후보 4 ~ 6 건** 을 *deferred candidates* 로 명시 등록한다. **deferred candidate = 향후 합의에서 P9~P12 정식 등록 가능, 본 G2 PASS 시점 정식 enumeration 외**.
   146	
   147	| 후보 ID | 위반 경로 (요약) | 핵심 위험 | 현 등록 상태 | 정식 등록 시점 |
   148	|--------|-------------|--------|----------|----------|
   149	| **P9 (후보)** | **Prompt Injection** — Hermes / Worker / LLM 출력 내 *지시 명령* 이 후속 LLM / Tool 에 의해 *명령* 으로 해석 (예: "ignore previous instructions ...") | 합의 결과 silent override / 자동 정책 변경 위장 / Skill escalation | deferred (GPT 조건 7) | 외부 입력 검증 GP-4 PoC 진입 시점에 P5 (외부 입력 검증) 와 *별 카테고리* 로 정식 등록 검토 |
   150	| ~~**P10 (후보)**~~ → **P10 (정식 등록 완료, §1.2.6 답습, 2026-05-09 후속 5)** | **Evidence Forgery** — JSONL ledger / 합의 보고서 / GitHub Actions run artifact 위조 또는 변조 | PASS 위장 / Hermes-originated 변경 위장 / 합의 권위 침해 | ✅ **정식 등록 완료 (§1.2.6 답습)** | ✅ **2026-05-09 후속 5** — PR-2 ADR-012 발행 (2026-05-09 후속 3) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록 |
   151	| ~~**P11 (후보)**~~ → **P11 (정식 등록 완료, §1.2.7 답습, 2026-05-12)** | **Supply-chain Compromise** — Hermes / pysqlcipher3 / litellm / Hermes-agent 의존성 또는 GitHub Actions runner / Docker base image 침해 | 자동 redaction 무력화 / SQLCipher trigger silent 깨짐 / canary catalog silent 변경 / R-6 actual run 위장 / Gate Enforcement Layer Layer 1~4 (lint/test/hook/CI) 무력화 | ✅ **정식 등록 완료 (§1.2.7 답습)** | ✅ **2026-05-12** — Gate Enforcement Layer 보호 보강 (commits `3e46440` + `fa2cbdb`) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록. **Hermes PMO 격상 *전* precondition (권장)** — blocking 까지는 아님, Implementation/Runtime PASS 영역의 *우선 권장 항목* (Claude C-3 + C-6 답습) |
   152	| **P12 (후보)** | **Memory Poisoning Side-channel** — Memory / Skill 의 *우회 경로* (CLAUDE.md prompt-level lock-in / 외부 import skill / Memory 자동 흡수) 를 통한 Memory 오염 + 후속 결정 silent 영향 | 자동 학습 → 자동 정책 변경 위장 (T1 → T3 우회) / Skill 권한 escalation 우회 / Provider lock-in 우회 | deferred (Claude C-4 + GPT 조건 7) | G4 (provider-agnostic-memory-skill-design.md) Implementation/Runtime PASS 합의 시점에 정식 등록 — Memory boundary hook + Skill wrapper 실 구현 후 |
   153	
   154	##### 1.2.5.1 추가 후보 (lower priority, 2 건)
   155	
   156	| 후보 ID | 위반 경로 (요약) | 처리 |
   157	|--------|-------------|----|
   158	| **P13 (후보)** | **Provider-specific URL Hardcoding** — `https://api.anthropic.com/...` / `https://api.openai.com/...` 등 provider 도메인 하드코딩 (P1 facade 우회) | GP-5 / G3 §6.4 / G4 §3.5 (provider_bindings) *동작 측면* 충분 — 별도 P 등록 *불필요* (Claude C-9 답습) |
   159	| **P14 (후보)** | **CLAUDE.md prompt-level Lock-in** — CLAUDE.md / system prompt 본문 내 특정 모델명 / vendor 분기 명시 | system-identity-prequel §7 ("메타포 강제 금지") 답습 + 헌법 5조 (Provider Liquidity) — 별도 P 등록 *불필요* (관용 권위로 흡수) |
   160	
   161	##### 1.2.5.2 본 §1.2.5 의 권위 한계
   162	
   163	- 본 §1.2.5 는 *deferred candidates* 만 등록 — **본 G2 PASS 시점 P1~P8 enumeration 변경 0건**
   164	- P9 ~ P12 정식 등록은 *각 후보의 정식 등록 시점* (위 표 4 행) 에 별도 합의 (단축 또는 풀 3+1)
   165	- 본 §1.2.5 변경 (P9~P12 정식 등록 / 추가 후보) 자체는 풀 3+1 합의 + ADR Amendment 절차 (T3 변경)
   166	- 본 §1.2.5 등록 후보가 *현 시점* enforcement 의무화 대상 *아님* — deferred candidates 는 *위험 식별 + 후속 합의 진입 trigger*
   167	
   168	##### 1.2.5.3 본 §1.2.5 가 *하지 않는* 것
   169	
   170	- ❌ P9 / P12 자동 정식 등록 (각 후보 별도 합의 시점) — **P10 은 §1.2.6 답습 정식 등록 완료 (2026-05-09 후속 5) / P11 은 §1.2.7 답습 정식 등록 완료 (2026-05-12)**
   171	- ❌ 현 G2 PASS 무력화 (deferred 는 *후속* 영역)
   172	- ❌ Hermes PMO 격상 전 P9 / P12 enforcement 의무 (격상 합의 시점 또는 별도 합의) — **P11 = Hermes PMO 격상 전 precondition 권장 (blocking 아님, Implementation/Runtime PASS 영역, §1.2.7 답습)**
   173	- ❌ P13 ~ P14 정식 등록 (관용 권위로 흡수, 별도 P 불필요)
   174	
   175	#### 1.2.6 Evidence Integrity 위반 경로 1건 (P10) — 정식 등록 (2026-05-09 후속 5)
   176	
   177	> **본 §1.2.6 는 §1.2.5.2 명시 "P10 정식 등록 시점 = PR-2 신규 ADR-012 발행 시점" 답습 흡수.** ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 발행) 시점이 P10 정식 등록 *트리거*. 본 후속 5 단축 합의 (Reviewer-only) 로 정식 등록.
   178	
   179	##### 1.2.6.1 P10 정식 row
   180	
   181	| # | 경로 | 시나리오 | Evidence Integrity 측면 (5건) | 관련 ADR / 게이트 / 합의 |
   182	|---|------|---------|--------------------------|------------------|
   183	| **P10** | **Evidence Forgery** | Evidence Ledger entry / external-review 응답 / 합의 보고서 / hash chain / GitHub Actions run artifact / commit history 가 *위조* 또는 *변조* 되어 (a) 잘못된 PASS 판정 / (b) Hermes-originated 변경 silent 수용 / (c) 합의 권위 silent 침해 / (d) 자동 정책 변경 위장 / (e) 외부 LLM 응답 위조 발생 | (i) Ledger entry 형식적 무결성 (11 필드 schema, hash chain) / (ii) prev_hash 검증 실패 처리 / (iii) git history rewrite 차단 / (iv) Hermes-originated commit auto-reject (변조 차단 매트릭스 4항목) / (v) external LLM response `agent="user"` 강제 | **ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5** (12 보호 원칙 + 4 매트릭스 + 5 추가 의무) + **G3 §5** (Evidence decision principle: PASS 성립 4 요건 — Tools 검증 + Evidence Ledger entry + 사용자 명시 승인 + 합의 보고서 commit) + **G4 §4.2 / §4.4 / §4.6** (11 필드 schema + Layer 1~5 다층 강제 + Tier-based round-trip) + 본 PR-2 합의 (`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`) |
   184	
   185	##### 1.2.6.2 P10 enforcement layer 매핑
   186	
   187	본 P10 enforcement 는 **ADR-012 직접 권위** + **G3 §5 + G4 §4** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.6 = P10 row 추가 한정, GP 신설은 별도 합의 영역):
   188	
   189	| Enforcement Layer | 책임 영역 | 권위 |
   190	|----|--------|----|
   191	| **Layer 1** (Hash chain) | Middle entry tampering 차단 | ADR-012 §2.3 + G4 §4.4 (sha256 + canonical JSON) |
   192	| **Layer 2** (Git append-only) | History 재작성 차단 (denyNonFastForwards) | ADR-012 §2.3 (Layer 2 MANDATORY) |
   193	| **Layer 3** (Signed commit) | Host compromise 후 위조 차단 | ADR-012 §2.3 (Layer 3 RECOMMENDED MVP / MANDATORY multi-host) |
   194	| **Layer 4** (CI 회귀 검증) | canonical JSON 위반 / prev_hash mismatch / timestamp monotonicity 자동 검출 | ADR-012 §2.3 + R-6 workflow 답습 확장 (Implementation 영역) |
   195	| **Layer 5** (External anchor) | 1인 SPOF 완화 + 침해 후 발견 | ADR-012 §2.3 (Layer 5 RECOMMENDED MVP / MANDATORY P2 v3 정식 채택) |
   196	| **Hermes 변조 차단 매트릭스 4항목** | Hermes-originated entry / 파일 변조 / git commit / 외부 LLM 응답 위조 차단 | ADR-012 §2.12 (Gap-17 HIGH 흡수) + G3 §2.5 #11 / §4.5 / §2.2 #20 cross-reference |
   197	| **External LLM `agent="user"` 강제** | 사용자 직접 paste 시 Hermes 위조 차단 | ADR-012 §2.1 원칙 7 + §3.1 |
   198	
   199	##### 1.2.6.3 P10 처리 범위 (사용자 명시 답습)
   200	
   201	| 차원 | 본 §1.2.6 처리 |
   202	|----|----|
   203	| **상태** | Deferred Candidate (§1.2.5) → **Formal P-row (§1.2.6)** |
   204	| **처리 범위** | Design/Governance row 추가 한정 |
   205	| **Implementation status** | **Pending** — ADR-012 §10.2 답습 (실 runtime hook / migration script / CI step / pre-commit hook 미구현, 별도 Implementation/Runtime PASS 합의) |
   206	| **GP 매핑** | 별도 합의 영역 (본 §1.2.6 = P10 row 추가 한정, GP 신설 또는 기존 GP 매핑 갱신은 별도) |
   207	
   208	##### 1.2.6.4 P10 정식 등록의 합의 권위
   209	
   210	본 P10 정식 등록 = **단축 합의 (Reviewer-only) 적격** (사용자 명시 답습):
   211	- ADR-012 발행 (PR-2 풀 3+1 합의, 2026-05-09 후속 3) 권위 *내부* 작업
   212	- ADR-012 §11.2 + §1.3 cross-reference 의무 답습
   213	- 본 §1.2.6 = §1.2.5.2 deferred candidate 정식 등록 시점 명시 답습
   214	- 본 P10 정식 row 본문 = ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5 답습 한정 (새 권위 결정 0건)
   215	
   216	**4 풀 3+1 승격 트리거 검증** (사용자 명시 답습):
   217	
   218	| 트리거 | 본 §1.2.6 |
   219	|----|----|
   220	| P10 이 기존 P1~P12 구조와 충돌 | ❌ — §1.2.5 deferred 에 이미 등록, 정식 row 승격은 §1.2.5.2 명시 트리거 답습 |
   221	| Evidence Forgery 가 ADR-012 범위를 넘어 새 정책 변경 요구 | ❌ — ADR-012 §2.1 ~ §3.5 답습 한정, 새 정책 0건 |
   222	| G2 / G3 / G4 Design PASS 상태를 흔드는 내용 | ❌ — §1.2 본문 추가, GP 매핑 변경 0건, 게이트 PASS 상태 영향 0 |
   223	| T3 자동 정책 변경 영역 발생 | ❌ — 정식 row 등록 자체는 T3 변경이지만 *ADR-012 발행 권위 내부* 작업, 사용자 명시 결정 답습 |
   224	
   225	→ **4/4 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격**.
   226	
   227	##### 1.2.6.5 본 §1.2.6 이 *하지 않는* 것
   228	
   229	- ❌ ADR-012 본문 재작성 (cross-reference 만 가능)
   230	- ❌ ADR-009 추가 갱신 (C-N 별도)
   231	- ❌ G3 / G4 본문 자동 갱신 (cross-reference 만)
   232	- ❌ 신규 GP 신설 (별도 합의 영역)
   233	- ❌ P9 / P12 자동 정식 등록 (각 후보 별도 합의 시점 답습) — **P11 은 §1.2.7 답습 정식 등록 완료 (2026-05-12)**
   234	- ❌ P10 enforcement Implementation 자동 (Implementation/Runtime PASS 별도)
   235	- ❌ R-6 workflow ledger 검증 step 자동 추가 (Implementation 영역)
   236	- ❌ Hermes-originated commit auto-reject 자동 구현 (Implementation 영역)
   237	- ❌ Hermes PMO 격상 자동 선언
   238	- ❌ P2 v3 정식 채택 자동 선언 (다음 진입점 풀 3+1 합의)
   239	- ❌ P2 v2 / system-identity-prequel archive 자동 처리
   240	
   241	#### 1.2.7 Supply-chain Integrity 위반 경로 1건 (P11) — 정식 등록 (2026-05-12)
   242	
   243	> **본 §1.2.7 은 §1.2.5 명시 "P11 정식 등록 시점 = SBOM + supply-chain 검증 PoC 합의 시점, Hermes PMO 격상 *전* 권장" 답습 흡수.** Gate Enforcement Layer 보호 보강 (2026-05-12, commits `3e46440` + `fa2cbdb`) 시점이 P11 정식 등록 *트리거* — 본 보강 작업의 Layer 2 (CI / hook / test) enforcement mechanism 이 supply-chain compromise 로 무력화 가능 + 외부 LLM Gap-N 중 N-5 supply chain / dependency integrity 답습. 본 후속 단축 합의 (Reviewer-only) 로 정식 등록.
   244	
   245	##### 1.2.7.1 P11 정식 row
   246	
   247	| # | 경로 | 시나리오 | Supply-chain Integrity 측면 (5건) | 관련 ADR / 게이트 / 합의 |
   248	|---|------|---------|--------------------------|------------------|
   249	| **P11** | **Supply-chain Compromise** | (a) Hermes / pysqlcipher3 / litellm / Hermes-agent / agents-sdk 의존성 (PyPI / 외부 소스) 침해 — 악성 코드 주입 / typosquatting / dependency confusion (b) GitHub Actions runner image / 3rd-party action 침해 — workflow step 위장 / artifact 변조 (c) Docker base image 침해 — 자동 redaction 무력화 / canary catalog silent 변경 / SQLCipher trigger silent 깨짐 (d) Vendor 변경 silent — `hermes-version.yaml` / `requirements.txt` / `pyproject.toml` / lock 파일의 silent drift (e) Tooling supply chain — `import-linter` / `grimp` / `rfc8785` / `jcs` / `gitleaks` 등 *enforcement tool 자체* 침해 → Gate Enforcement Layer Layer 1~4 무력화 | (i) **Dependency Pinning Integrity** — `hermes-version.yaml` v0.12.0 명시 + `requirements.txt` / `pyproject.toml` / `poetry.lock` 정확 핀 + lock 파일 git diff 회귀 검출 (G3 §3.2.2 #3 답습) / (ii) **Checksum / Hash Verification** — pip install `--require-hashes` + SBOM 정합성 + 패키지 sha256 매니페스트 검증 / (iii) **GitHub Actions Action SHA Pinning** — `uses: actions/checkout@<commit_sha>` (not `@v4` tag) + 3rd-party action 사용 시 commit SHA pin 강제 / (iv) **Docker Base Image / Runner Image Immutability** — `FROM python:3.11@sha256:<digest>` digest 고정 + reproducible build + cosign 또는 동등 image signing verification (별도 합의 영역) / (v) **Vendor Change Auto-recheck** — 의존성 lock diff 검출 시 R-6 actual run 자동 R-2 / R-4.1 PoC 재실행 + canary 자동 검증 PASS 후만 merge (G3 §3.2.3 #2 답습) | **G3 §3.2** (Upstream Silent Breakage 5 측면 + ROLLBACK trigger R6) + **G3 §2.5 #14** (`hermes-version.yaml` + dependency lock T2 사용자 명시 PR merge) + **G3 §2.6** (Gate Enforcement Layer 보호 — Layer 1~4 enforcement mechanism 무력화 위험 cross-reference) + **GP-2 / GP-3 / GP-5** (redaction / credential / provider lock-in supply-chain 침해 시 무력화 위험 cross-reference) + **ADR-008 차단조건 #3** (Hermes 의존성 업그레이드 자동 R-2 재실행) + **외부 LLM Gap-N 중 N-5** (supply chain / dependency integrity 답습) + 본 §1.2.7 단축 합의 (Reviewer-only) |
   250	
   251	##### 1.2.7.2 P11 enforcement layer 매핑 (5 Layer 다층 강제)
   252	
   253	본 P11 enforcement 는 **G3 §3.2 직접 권위** + **G3 §2.5 #14** + **GP-2/GP-3/GP-5 cross-reference** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.7 = P11 row 추가 한정, GP 신설은 별도 합의 영역):
   254	
   255	| Enforcement Layer | 책임 영역 | 권위 |
   256	|----|--------|----|
   257	| **Layer 1** (Lockfile + Version Pin) | Dependency drift 차단 | G3 §2.5 #14 (T2 사용자 명시 PR merge) + ADR-008 차단조건 #3 + `hermes-version.yaml` v0.12.0 핀 + `requirements.txt` / `pyproject.toml` / `poetry.lock` 정확 핀 |
   258	| **Layer 2** (GitHub Actions Action SHA Pin + Docker Image Digest Pin) | CI / Image silent 변경 차단 | G3 §2.6 §2.6.3 (b) (Hook / CI workflow 비활성화 차단) cross-reference + 별도 합의 영역 (Implementation/Runtime PASS — 3rd-party action 사용 시 commit SHA pin 강제 hook + Docker FROM digest 고정) |
   259	| **Layer 3** (Checksum / Hash Verification + SBOM) | Tampered package 차단 | pip `--require-hashes` + SBOM 정합성 (예: `pip-audit` / `safety` / `cyclonedx-py`) + 별도 합의 영역 (Implementation/Runtime PASS — SBOM 생성 / 검증 hook) |
   260	| **Layer 4** (CI 회귀 검증 — Vendor Change Auto-recheck) | 의존성 lock diff 감지 시 자동 R-2 / R-4.1 PoC 재실행 + canary 자동 검증 + R-6 actual run PASS 후만 merge | G3 §3.2.2 #3 + §3.2.3 #2 (이미 G3 본문 권위) + R-6 workflow 답습 확장 (Implementation 영역) |

exec
/bin/bash -lc 'rg -n "GP-2|request body|LLM request|redaction|송신|stdout|LLM API" docs/architecture/governance-preconditions.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
5:> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 문서 구조 / 권위 위계 / 6 GP 정의 / 강제 메커니즘 분류 매트릭스 / Entry·Exit 기준 정의의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — GP-2~GP-6 의 PoC 실증 / CI 강제 / runtime hook 구현 / Evidence Ledger 검증은 *별도 합의* 로만 발생.
9:> - **GP-2 ~ GP-6**: **DESIGN PASS / IMPLEMENTATION PENDING** (각 GP 의 PoC 실증 + (a)~(e) 5조건 충족 검증은 별도 합의)
28:**관련 설계**: **`hermes-adoption-design-v3.md` §4 (G2 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3.3 / §4.2 (**Archived 2026-05-09 후속 8**, 본 ADR-011 §2.3 영구 권위 승격 답습으로 권위 보존), `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
105:| **P2** | **로그/LLM 송신 경로 평문 노출** | Hermes / Worker 가 secret 을 stdout / stderr / log file / LLM API request body 에 노출 | 8조 #2 | Hermes native redaction 보조 (ADR-011 §2.3 운영 함의 #2) |
151:| ~~**P11 (후보)**~~ → **P11 (정식 등록 완료, §1.2.7 답습, 2026-05-12)** | **Supply-chain Compromise** — Hermes / pysqlcipher3 / litellm / Hermes-agent 의존성 또는 GitHub Actions runner / Docker base image 침해 | 자동 redaction 무력화 / SQLCipher trigger silent 깨짐 / canary catalog silent 변경 / R-6 actual run 위장 / Gate Enforcement Layer Layer 1~4 (lint/test/hook/CI) 무력화 | ✅ **정식 등록 완료 (§1.2.7 답습)** | ✅ **2026-05-12** — Gate Enforcement Layer 보호 보강 (commits `3e46440` + `fa2cbdb`) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록. **Hermes PMO 격상 *전* precondition (권장)** — blocking 까지는 아님, Implementation/Runtime PASS 영역의 *우선 권장 항목* (Claude C-3 + C-6 답습) |
249:| **P11** | **Supply-chain Compromise** | (a) Hermes / pysqlcipher3 / litellm / Hermes-agent / agents-sdk 의존성 (PyPI / 외부 소스) 침해 — 악성 코드 주입 / typosquatting / dependency confusion (b) GitHub Actions runner image / 3rd-party action 침해 — workflow step 위장 / artifact 변조 (c) Docker base image 침해 — 자동 redaction 무력화 / canary catalog silent 변경 / SQLCipher trigger silent 깨짐 (d) Vendor 변경 silent — `hermes-version.yaml` / `requirements.txt` / `pyproject.toml` / lock 파일의 silent drift (e) Tooling supply chain — `import-linter` / `grimp` / `rfc8785` / `jcs` / `gitleaks` 등 *enforcement tool 자체* 침해 → Gate Enforcement Layer Layer 1~4 무력화 | (i) **Dependency Pinning Integrity** — `hermes-version.yaml` v0.12.0 명시 + `requirements.txt` / `pyproject.toml` / `poetry.lock` 정확 핀 + lock 파일 git diff 회귀 검출 (G3 §3.2.2 #3 답습) / (ii) **Checksum / Hash Verification** — pip install `--require-hashes` + SBOM 정합성 + 패키지 sha256 매니페스트 검증 / (iii) **GitHub Actions Action SHA Pinning** — `uses: actions/checkout@<commit_sha>` (not `@v4` tag) + 3rd-party action 사용 시 commit SHA pin 강제 / (iv) **Docker Base Image / Runner Image Immutability** — `FROM python:3.11@sha256:<digest>` digest 고정 + reproducible build + cosign 또는 동등 image signing verification (별도 합의 영역) / (v) **Vendor Change Auto-recheck** — 의존성 lock diff 검출 시 R-6 actual run 자동 R-2 / R-4.1 PoC 재실행 + canary 자동 검증 PASS 후만 merge (G3 §3.2.3 #2 답습) | **G3 §3.2** (Upstream Silent Breakage 5 측면 + ROLLBACK trigger R6) + **G3 §2.5 #14** (`hermes-version.yaml` + dependency lock T2 사용자 명시 PR merge) + **G3 §2.6** (Gate Enforcement Layer 보호 — Layer 1~4 enforcement mechanism 무력화 위험 cross-reference) + **GP-2 / GP-3 / GP-5** (redaction / credential / provider lock-in supply-chain 침해 시 무력화 위험 cross-reference) + **ADR-008 차단조건 #3** (Hermes 의존성 업그레이드 자동 R-2 재실행) + **외부 LLM Gap-N 중 N-5** (supply chain / dependency integrity 답습) + 본 §1.2.7 단축 합의 (Reviewer-only) |
253:본 P11 enforcement 는 **G3 §3.2 직접 권위** + **G3 §2.5 #14** + **GP-2/GP-3/GP-5 cross-reference** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.7 = P11 row 추가 한정, GP 신설은 별도 합의 영역):
342:| **GP-2** | Egress Redaction (로그/LLM 송신) | P2 | Hermes native redaction (보조 — ADR-011 §2.3 #2) + LLM facade redaction filter (P1) | ADR-008 차단조건 #1 보조 + ADR-011 §2.3 |
355:| GP-2 | ✅ test_redaction.py + base64 evasion test (R2-6) | ⚠️ 보조 | ✅ ROLLBACK trigger R5 (Hermes 학습 평문 검출) |
363:- 추론적 보조: 4/6 (GP-1, GP-2, GP-4, GP-6)
388:| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R1~R3 | `docs/phase0/redaction-verification-sop.md` |
401:| (a) | 동등 이상의 보안 결과 | R-4 redaction-pattern-equivalence.md (3-way 비교 + Tier-1 42 gap 식별) |
418:## 4. GP-2 — Egress Redaction (로그/LLM 송신)
422:Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.
424:**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
428:- **P2** — 로그/LLM 송신 경로 평문 노출
434:| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
436:| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
444:- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
445:- ⏳ 사용자 명시 GP-2 작업 진입 결정
451:| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
455:| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |
459:- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
465:- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
765:| GP-2 | (a)~(e) 미충족 — PoC + 합의 필요 | ⏳ |

exec
/bin/bash -lc "rg -n \"OllamaBoss\\(|OllamaWorker\\(\" src tests docs | head -100" in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc 'rg -n "class RedactionFilter|REDACTION_MARK|redact_messages|redact_text|Tier|catalog|secret" src/adapters/llm tests/adapters tests | head -120' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
src/jarvis/boss.py:17:트랙 B = OllamaBoss(stdlib urllib.request 단독, `ollama` python SDK import 0건 —
src/jarvis/boss.py:172:      - caller 가 명시 = OllamaBoss(system_prompt=boss_prompt_for("shell")).
docs/phase0/jarvis-mvp1-m3-m4-fixation-brief.md:21:본 합의 = brief + 권고 보고서 + 합의 commit/push 한정. 사용자 결정 *후* 별도 cycle 에서 실 코드/config 갱신 가능 (`OllamaBoss(model="...")` default 변경 등).
docs/phase0/jarvis-mvp1-m3-m4-fixation-brief.md:128:- `OllamaBoss(model=DEFAULT)` 변경 — 사용자 결정 후 별도 cycle
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:259:    17	트랙 B = OllamaBoss(stdlib urllib.request 단독, `ollama` python SDK import 0건 —
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:414:   172	      - caller 가 명시 = OllamaBoss(system_prompt=boss_prompt_for("shell")).
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1321:    31	    boss = OllamaBoss(model="qwen3-30b-a3b-instruct-2507-bartowski:latest")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1327:    37	    boss = OllamaBoss(model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1340:    50	    boss = OllamaBoss(model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1373:    83	    boss = OllamaBoss(model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1383:    93	    boss = OllamaBoss(model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1393:   103	    boss = OllamaBoss(model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1403:   113	    boss = OllamaBoss(model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1490:   200	    """OllamaBoss(system_prompt=None) → boss_prompt_for('code') 사용."""
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1492:   202	    boss = OllamaBoss(model="m")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1523:   233	    boss = OllamaBoss(model="m", system_prompt=custom)
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1573:    36	    w = OllamaWorker(alias="glm", model="glm-4.7-flash:latest")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1581:    44	    w = OllamaWorker(alias="glm", model="m1")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1593:    56	    w = OllamaWorker(alias="glm", model="m", output_filename=None)
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1602:    65	    w = OllamaWorker(alias="glm", model="m", output_filename="hello.py")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1615:    78	    w = OllamaWorker(alias="glm", model="m", output_filename="x.py")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1627:    90	    w = OllamaWorker(alias="glm", model="m", output_filename="x.txt")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1641:   104	    w = OllamaWorker(alias="glm", model="m", output_filename="../outside/evil.py")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1655:   118	    w = OllamaWorker(alias="glm", model="m", output_filename=bad_abs)
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1666:   129	    w = OllamaWorker(alias="glm", model="m")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1676:   139	    w = OllamaWorker(alias="glm", model="m")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1684:   147	    w = OllamaWorker(alias="glm", model="m")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1691:   154	    w = OllamaWorker(alias="glm", model="m")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1717:   180	    w = OllamaWorker(alias="glm", model="m-x")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1734:   197	    w = OllamaWorker(alias="glm", model="m")
docs/external-review/2026-05-28-boss-worker-facade-consolidation-codex-response.md:1752:   215	    w = OllamaWorker(alias="glm", model="m",
docs/phase0/jarvis-claude-worker-integration-brief.md:3:> **scope**: TmuxWorker(shell) 단일 워커 → **CliWorker(claude headless) 추가** = 실 LLM 워커 통합. OllamaBoss(Qwen3) 가 claude 출력을 검토. Layer 0 누적.
docs/phase0/jarvis-glm-worker-integration-brief.md:16:| **`OllamaWorker(GLM)`** | **응답 텍스트만** (Ollama 는 fs 행동 능력 없음) | **orchestrator → demo helper 가 결정적으로 파일 쓰기** |
docs/phase0/jarvis-mvp1-local-boss-design-brief.md:77:        ├─ OllamaBoss(endpoint, model)      # 로컬 (OpenAI-호환 /v1/chat/completions)
docs/phase0/jarvis-v00-working-sprint-brief.md:14:| (1) Ollama Qwen3-30B-A3B 직결 1건 | `OllamaBoss(BossLLM)` (stdlib urllib, HTTP `/api/chat`) + TDD + 실 endpoint smoke 1회 | 단일 | 없음 |
docs/phase0/jarvis-v00-working-sprint-brief.md:66:| 모델명 hardcoded → Provider Liquidity 위반 | OllamaBoss(model="..." 인자 default 한정. `name` 필드는 BossLLM 답습. 헌법 5조 = 교체 *가능성* 답습 = 인자 주입 충족. |
tests/jarvis/test_ollama_worker.py:36:    w = OllamaWorker(alias="glm", model="glm-4.7-flash:latest")
tests/jarvis/test_ollama_worker.py:44:    w = OllamaWorker(alias="glm", model="m1")
tests/jarvis/test_ollama_worker.py:56:    w = OllamaWorker(alias="glm", model="m", output_filename=None)
tests/jarvis/test_ollama_worker.py:65:    w = OllamaWorker(alias="glm", model="m", output_filename="hello.py")
tests/jarvis/test_ollama_worker.py:78:    w = OllamaWorker(alias="glm", model="m", output_filename="x.py")
tests/jarvis/test_ollama_worker.py:90:    w = OllamaWorker(alias="glm", model="m", output_filename="x.txt")
tests/jarvis/test_ollama_worker.py:104:    w = OllamaWorker(alias="glm", model="m", output_filename="../outside/evil.py")
tests/jarvis/test_ollama_worker.py:118:    w = OllamaWorker(alias="glm", model="m", output_filename=bad_abs)
tests/jarvis/test_ollama_worker.py:129:    w = OllamaWorker(alias="glm", model="m")
tests/jarvis/test_ollama_worker.py:139:    w = OllamaWorker(alias="glm", model="m")
tests/jarvis/test_ollama_worker.py:147:    w = OllamaWorker(alias="glm", model="m")
tests/jarvis/test_ollama_worker.py:154:    w = OllamaWorker(alias="glm", model="m")
tests/jarvis/test_ollama_worker.py:180:    w = OllamaWorker(alias="glm", model="m-x")
tests/jarvis/test_ollama_worker.py:197:    w = OllamaWorker(alias="glm", model="m")
tests/jarvis/test_ollama_worker.py:215:    w = OllamaWorker(alias="glm", model="m",
tests/jarvis/test_ollama_boss.py:31:    boss = OllamaBoss(model="qwen3-30b-a3b-instruct-2507-bartowski:latest")
tests/jarvis/test_ollama_boss.py:37:    boss = OllamaBoss(model="m1")
tests/jarvis/test_ollama_boss.py:50:    boss = OllamaBoss(model="m1")
tests/jarvis/test_ollama_boss.py:83:    boss = OllamaBoss(model="m1")
tests/jarvis/test_ollama_boss.py:93:    boss = OllamaBoss(model="m1")
tests/jarvis/test_ollama_boss.py:103:    boss = OllamaBoss(model="m1")
tests/jarvis/test_ollama_boss.py:113:    boss = OllamaBoss(model="m1")
tests/jarvis/test_ollama_boss.py:200:    """OllamaBoss(system_prompt=None) → boss_prompt_for('code') 사용."""
tests/jarvis/test_ollama_boss.py:202:    boss = OllamaBoss(model="m")
tests/jarvis/test_ollama_boss.py:233:    boss = OllamaBoss(model="m", system_prompt=custom)
docs/phase0/jarvis-boss-prompt-branching-brief.md:48:- caller 가 도메인 prompt 명시 = `OllamaBoss(model, system_prompt=boss_prompt_for("shell"))`.
docs/phase0/jarvis-boss-prompt-branching-brief.md:63:| 9 | `OllamaBoss(system_prompt=None)` → 기본 = boss_prompt_for("code") |
docs/phase0/jarvis-boss-prompt-branching-brief.md:64:| 10 | `OllamaBoss(system_prompt="X")` → 실 HTTP body 의 system msg.content = "X" |
docs/review/3plus1-consensus-2026-05-26-jarvis-mvp1-m3-m4-fixation.md:17:| **C (대안)** | **REVISE** | **M3-A vs M3-C 이분법 false dichotomy**. `OllamaBoss(model: str)` 답습 시 *현재 코드 자체가 M3-F* (default 인자 + caller 교체 자유 양립). M3-F 신규 후보 brief 본문 silent. (q) 응답 길이 통제 *선행* = 본 cycle 권고 자격 boundary. M3-E 카탈로그 9 후보 식별 확장. |
docs/review/3plus1-consensus-2026-05-26-jarvis-mvp1-m3-m4-fixation.md:83:| **R-2** | CRITICAL | **M3 후보 표 재정비** — M3-A vs M3-C 이분법 → M3-F (default + 교체 자유 양립) 신규 행 추가 + ADR-011 §2.1 (a)~(d) 4조건 답습 명문. 현 `OllamaBoss(model: str)` 답습 = default 0건 + caller 명시 의무 = Provider Liquidity 헌법 5조-2 line 77~80 정합. M3-A *단독* 권고 자격 0건 명문. P-2 답습. | §3.1 |
docs/review/3plus1-consensus-2026-05-26-jarvis-mvp1-m3-m4-fixation.md:163:| `OllamaBoss(model="...")` default 신설 (M3-F 채택) | ✅ 사용자 명시 + 별도 cycle (코드 변경 = 헌법 5조-2 정합 검증 의무) |

 succeeded in 0ms:
tests/adapters/llm/test_redaction_filter.py:12:from src.adapters.llm.redaction_patterns import ALL_PATTERNS, REDACTION_MARK
tests/adapters/llm/test_redaction_filter.py:20:# ── T-1: redact_text — secret 값 마스킹 (prefix = whole, key명 없음) ──────────
tests/adapters/llm/test_redaction_filter.py:21:def test_t1_redact_text_prefix_token(rf: RedactionFilter) -> None:
tests/adapters/llm/test_redaction_filter.py:22:    out = rf.redact_text("use sk-ant-ABCDEFGHIJ1234567890 now")
tests/adapters/llm/test_redaction_filter.py:24:    assert REDACTION_MARK in out
tests/adapters/llm/test_redaction_filter.py:28:# ── T-2: redact_messages — content secret 값 redacted, key=구조 보존 ──────────
tests/adapters/llm/test_redaction_filter.py:29:def test_t2_redact_messages_env_assignment(rf: RedactionFilter) -> None:
tests/adapters/llm/test_redaction_filter.py:31:    out = rf.redact_messages(msgs)
tests/adapters/llm/test_redaction_filter.py:34:    assert REDACTION_MARK in content
tests/adapters/llm/test_redaction_filter.py:39:# ── T-3: Tier-1 45 catalog 대표 패턴 (baseline/prefix/regex/alternation) ──────
tests/adapters/llm/test_redaction_filter.py:41:    "secret",
tests/adapters/llm/test_redaction_filter.py:46:        "https://example.com/cb?access_token=eyJsecretvalue123",  # T1-041 alternation
tests/adapters/llm/test_redaction_filter.py:49:def test_t3_catalog_representative_patterns(rf: RedactionFilter, secret: str) -> None:
tests/adapters/llm/test_redaction_filter.py:50:    out = rf.redact_text(secret)
tests/adapters/llm/test_redaction_filter.py:51:    assert REDACTION_MARK in out
tests/adapters/llm/test_redaction_filter.py:52:    # secret 고유 값 (raw alphanum 시퀀스)이 평문 노출 0
tests/adapters/llm/test_redaction_filter.py:53:    for leak in ("ABCDEFGHIJ1234567890", "sk_live_ABCDEFGHIJ1234", "eyJsecretvalue123"):
tests/adapters/llm/test_redaction_filter.py:54:        if leak in secret:
tests/adapters/llm/test_redaction_filter.py:66:        "the secret garden was lovely",  # 'secret' 단어 but =value 아님
tests/adapters/llm/test_redaction_filter.py:70:    assert rf.redact_text(benign) == benign
tests/adapters/llm/test_redaction_filter.py:82:    assert out["api_key"] == REDACTION_MARK
tests/adapters/llm/test_redaction_filter.py:83:    assert out["nested"]["token"] == REDACTION_MARK
tests/adapters/llm/test_redaction_filter.py:95:# ── T-7: 원본 불변성 — redact_messages in-place mutate 0 (R-1) ────────────────
tests/adapters/llm/test_redaction_filter.py:96:def test_t7_redact_messages_no_inplace_mutation(rf: RedactionFilter) -> None:
tests/adapters/llm/test_redaction_filter.py:99:    out = rf.redact_messages(original)
tests/adapters/llm/test_redaction_filter.py:105:# ── T-8: equivalence — catalog single source 45 patterns (B-1) ────────────────
tests/adapters/llm/test_redaction_filter.py:106:def test_t8_catalog_equivalence_45_patterns() -> None:
src/adapters/llm/redaction_patterns.py:1:"""Tier-1 secret pattern catalog — single source (detection + prevention 공유).
src/adapters/llm/redaction_patterns.py:4:  - `tools/secret_scanner.py` (detection, GP-3 + GP-2 D-2 scan-log)
src/adapters/llm/redaction_patterns.py:6:둘 다 본 catalog 를 import → detection ↔ prevention 패턴 drift 0 (single source).
src/adapters/llm/redaction_patterns.py:9:secret_scanner 에서 literal 그대로 이동 (equivalence test 강제: len(ALL_PATTERNS)==45 + snapshot 동일).
src/adapters/llm/redaction_patterns.py:12:  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (Tier-1 42 + baseline 5 = 45)
src/adapters/llm/redaction_patterns.py:22:# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습 (secret_scanner literal 이동, 변경 0)
src/adapters/llm/redaction_patterns.py:41:# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
src/adapters/llm/redaction_patterns.py:65:    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
src/adapters/llm/redaction_patterns.py:67:    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
src/adapters/llm/redaction_patterns.py:107:# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
src/adapters/llm/redaction_patterns.py:111:    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
src/adapters/llm/redaction_patterns.py:112:     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
src/adapters/llm/redaction_patterns.py:125:# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
src/adapters/llm/redaction_patterns.py:128:     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
src/adapters/llm/redaction_patterns.py:130:     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
src/adapters/llm/redaction_patterns.py:150:# pattern_id → secret *값* 의 capturing group index.
src/adapters/llm/redaction_patterns.py:151:#   0   = whole match 가 secret 값 (prefix/JWT/private key — key명 없음, 구조 손상 0)
src/adapters/llm/redaction_patterns.py:169:# Redaction marker (RedactionFilter 출력 + secret_scanner scan-log FP 회피 정합).
src/adapters/llm/redaction_patterns.py:170:REDACTION_MARK: str = "[REDACTED]"
tests/adapters/llm/test_facade_router.py:29:from src.adapters.llm.redaction_patterns import REDACTION_MARK
tests/adapters/llm/test_facade_router.py:96:    # 양방향: 원본 secret 부재 AND REDACTION_MARK 존재 (한쪽만 = trap)
tests/adapters/llm/test_facade_router.py:99:    assert REDACTION_MARK in blob
src/adapters/llm/facade.py:10:Router 위임 *전* 위치 (송신 secret strip, 미부착 window 0).
src/adapters/llm/facade.py:158:        messages = self._redactor.redact_messages(request.messages)
src/adapters/llm/facade.py:160:            redacted_system = self._redactor.redact_text(request.system)
src/adapters/llm/redaction.py:1:"""RedactionFilter — GP-2 R-2 prevention (LLM 송신 request body secret strip).
src/adapters/llm/redaction.py:4:  - 권위: governance §4.1 ("LLM API request body 에 secret 노출 차단") + 64 trajectory §3
src/adapters/llm/redaction.py:6:  - B-1 (ii): Tier-1 45 catalog single source = redaction_patterns (detection 과 공유)
src/adapters/llm/redaction.py:7:  - B-2: group-aware 치환 — secret *값* 만 마스킹, key명/JSON 구조 보존 (whole-match 금지)
src/adapters/llm/redaction.py:10:GP-2 prevention 핵심 = 송신 (redact_messages). 응답/로그 redaction = 보조 (scrub).
src/adapters/llm/redaction.py:20:    REDACTION_MARK,
src/adapters/llm/redaction.py:27:    {"api_key", "apikey", "token", "secret", "auth", "credential", "authorization", "password"}
src/adapters/llm/redaction.py:34:        # whole match 가 secret 값 (prefix/JWT/private key — key명 없음)
src/adapters/llm/redaction.py:35:        return REDACTION_MARK
src/adapters/llm/redaction.py:40:        return full[: eq + 1] + REDACTION_MARK if eq != -1 else REDACTION_MARK
src/adapters/llm/redaction.py:45:        return full[: start - off] + REDACTION_MARK + full[end - off :]
src/adapters/llm/redaction.py:46:    return REDACTION_MARK
src/adapters/llm/redaction.py:49:class RedactionFilter:
src/adapters/llm/redaction.py:52:    def redact_text(self, text: str) -> str:
src/adapters/llm/redaction.py:53:        """str 에서 Tier-1 45 catalog 매칭 secret 값 group-aware 마스킹."""
src/adapters/llm/redaction.py:62:    def redact_messages(self, messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
src/adapters/llm/redaction.py:69:                new_msg["content"] = self.redact_text(content)
src/adapters/llm/redaction.py:83:                    result[key] = REDACTION_MARK if isinstance(value, str) else self.scrub(value)
src/adapters/llm/redaction.py:90:            return self.redact_text(obj)
tests/adapters/llm/test_redaction_filter.py:12:from src.adapters.llm.redaction_patterns import ALL_PATTERNS, REDACTION_MARK
tests/adapters/llm/test_redaction_filter.py:20:# ── T-1: redact_text — secret 값 마스킹 (prefix = whole, key명 없음) ──────────
tests/adapters/llm/test_redaction_filter.py:21:def test_t1_redact_text_prefix_token(rf: RedactionFilter) -> None:
tests/adapters/llm/test_redaction_filter.py:22:    out = rf.redact_text("use sk-ant-ABCDEFGHIJ1234567890 now")
tests/adapters/llm/test_redaction_filter.py:24:    assert REDACTION_MARK in out
tests/adapters/llm/test_redaction_filter.py:28:# ── T-2: redact_messages — content secret 값 redacted, key=구조 보존 ──────────
tests/adapters/llm/test_redaction_filter.py:29:def test_t2_redact_messages_env_assignment(rf: RedactionFilter) -> None:
tests/adapters/llm/test_redaction_filter.py:31:    out = rf.redact_messages(msgs)
tests/adapters/llm/test_redaction_filter.py:34:    assert REDACTION_MARK in content
tests/adapters/llm/test_redaction_filter.py:39:# ── T-3: Tier-1 45 catalog 대표 패턴 (baseline/prefix/regex/alternation) ──────
tests/adapters/llm/test_redaction_filter.py:41:    "secret",
tests/adapters/llm/test_redaction_filter.py:46:        "https://example.com/cb?access_token=eyJsecretvalue123",  # T1-041 alternation
tests/adapters/llm/test_redaction_filter.py:49:def test_t3_catalog_representative_patterns(rf: RedactionFilter, secret: str) -> None:
tests/adapters/llm/test_redaction_filter.py:50:    out = rf.redact_text(secret)
tests/adapters/llm/test_redaction_filter.py:51:    assert REDACTION_MARK in out
tests/adapters/llm/test_redaction_filter.py:52:    # secret 고유 값 (raw alphanum 시퀀스)이 평문 노출 0
tests/adapters/llm/test_redaction_filter.py:53:    for leak in ("ABCDEFGHIJ1234567890", "sk_live_ABCDEFGHIJ1234", "eyJsecretvalue123"):
tests/adapters/llm/test_redaction_filter.py:54:        if leak in secret:
tests/adapters/llm/test_redaction_filter.py:66:        "the secret garden was lovely",  # 'secret' 단어 but =value 아님
tests/adapters/llm/test_redaction_filter.py:70:    assert rf.redact_text(benign) == benign
tests/adapters/llm/test_redaction_filter.py:82:    assert out["api_key"] == REDACTION_MARK
tests/adapters/llm/test_redaction_filter.py:83:    assert out["nested"]["token"] == REDACTION_MARK
tests/adapters/llm/test_redaction_filter.py:95:# ── T-7: 원본 불변성 — redact_messages in-place mutate 0 (R-1) ────────────────
tests/adapters/llm/test_redaction_filter.py:96:def test_t7_redact_messages_no_inplace_mutation(rf: RedactionFilter) -> None:
tests/adapters/llm/test_redaction_filter.py:99:    out = rf.redact_messages(original)
tests/adapters/llm/test_redaction_filter.py:105:# ── T-8: equivalence — catalog single source 45 patterns (B-1) ────────────────
tests/adapters/llm/test_redaction_filter.py:106:def test_t8_catalog_equivalence_45_patterns() -> None:
tests/adapters/llm/test_facade_router.py:29:from src.adapters.llm.redaction_patterns import REDACTION_MARK
tests/adapters/llm/test_facade_router.py:96:    # 양방향: 원본 secret 부재 AND REDACTION_MARK 존재 (한쪽만 = trap)
tests/adapters/llm/test_facade_router.py:99:    assert REDACTION_MARK in blob
tests/jarvis/test_review_guard.py:56:    g = ReviewGuard(extra_patterns=[("secret-exfil", r"AWS_SECRET")])
tests/jarvis/test_review_guard.py:59:    assert any("secret-exfil" in f for f in v.flags)
tests/fixtures/gp3_st2/README.md:18:- R-4.1 Tier-1 catalog (fake canary 의무) + ADR-008 §A.2 R1-2 + GP-3 §5.3
tests/fixtures/gp3_st2/README.md:27:| `pass/init_phase/` | init grace period 내 정상 secret 주입 | event 무시 (grace) / hermes-mock healthy |
tests/fixtures/gp3_st2/README.md:28:| `fail/chmod_644/` | runtime `chmod 644 /run/secrets/mock_api_key` 시뮬레이션 | `IN_ATTRIB` 감지 / status `UNHEALTHY: IN_ATTRIB ...` / hermes-mock unhealthy |
tests/fixtures/gp3_st2/README.md:29:| `fail/content_modified/` | runtime mock secret 본문 변경 시뮬레이션 | `IN_MODIFY` 감지 / status `UNHEALTHY: IN_MODIFY ...` / hermes-mock unhealthy |
tests/fixtures/gp3_st2/README.md:30:| `fail/file_deleted/` | runtime mock secret 파일 삭제 시뮬레이션 | `IN_DELETE_SELF` 감지 / status `UNHEALTHY: IN_DELETE_SELF ...` / hermes-mock unhealthy |
tests/fixtures/gp3_st2/README.md:41:├── run-secrets/         # mock secret 파일 (Cycle 3 docker-compose 가 /run/secrets/ 로 mount)
tests/fixtures/gp3_st2/README.md:56:| 1 | **실 secret 본문 commit 0건** (영구 금지 — R-4.1 답습) — 모든 mock secret = `FAKE_CANARY_DO_NOT_USE_*` prefix |
tests/fixtures/gp3_st2/README.md:58:| 3 | sidecar 가 mock secret 본문을 logging / hashing / export 하지 않음 (Cycle 3 sidecar 본문 구현 시점 강제) |
tests/fixtures/provider_url_scanner/model_name/fail/hardcoded_model_anthropic.py:2:# 답습: 사양 §7.4 — Tier-1 model ID 가 src/ 코드 (.py) 에 직접 사용 시 violation
tests/fixtures/secret_hygiene/mvp1_entry/fail/tier1_prefix_variety.py:5:# cover 하는 한계를 MVP-1 entry 시점 회귀 보강. Tier-1 prefix 31 中 6 vendor sample cover.
tests/fixtures/secret_hygiene/mvp1_entry/fail/tier1_prefix_variety.py:6:# 답습 변경 0건 — Tier-1 catalog 자동 확장 0건 (R-4.1 §4.1 답습 한정).
tests/fixtures/secret_hygiene/mvp1_entry/fail/tier1_prefix_variety.py:9:#   모든 fake secret 은 FAKE / NOTAREAL / fakecanary / R41T marker 포함.
tests/fixtures/provider_url_scanner/model_name/fail/hardcoded_model_llama.py:2:# 답습: 사양 §7.4 — Tier-1 model ID 가 src/ 코드 (.py) 에 직접 사용 시 violation
tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py:1:# S-3 detect-secrets FAIL fixture — KeywordDetector plugin 검출 evidence
tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py:2:# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py:6:# 답습 변경 0건 — tools/secret_scanner.py 본문 / R-4.1 Tier-1 45 patterns 변경 0건.
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py:9:#   모든 fake secret 은 FAKE / NOTAREAL / fakecanary / R41T marker 포함.

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '330,470p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   330	
   331	본 cross-reference 강화로 **Gate Enforcement Layer 보호 (G3 §2.6) ↔ Supply-chain Integrity (P11)** 양방향 보호 *완결성* 확보 — 1 layer 만 깨져도 enforcement 무력화 위험 잔존 (예: Layer 1~4 hook 정상 + supply-chain 침해 시 hook *도구 자체* 가 침해되어 silent PASS).
   332	
   333	---
   334	
   335	## 2. 6 거버넌스 사전조건 (GP-1 ~ GP-6) 정의 + 매핑
   336	
   337	### 2.1 GP 정의 + P1~P8 매핑 매트릭스
   338	
   339	| GP | 명칭 | 위반 경로 | 핵심 강제 메커니즘 | 관련 G* / ADR |
   340	|----|------|---------|----------------|-------------|
   341	| **GP-1** | DB-level Secret Persistence 차단 | P1 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | G1b PASS (이미 충족) + ADR-011 §2.1 |
   342	| **GP-2** | Egress Redaction (로그/LLM 송신) | P2 | Hermes native redaction (보조 — ADR-011 §2.3 #2) + LLM facade redaction filter (P1) | ADR-008 차단조건 #1 보조 + ADR-011 §2.3 |
   343	| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | (저장) docker secret + chmod 600 + entrypoint stat + inotify, (코드) gitleaks / detect-secrets pre-commit hook + CI step | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 (35번째 entry R-S1 정정 답습) |
   344	| **GP-4** | 외부 입력 검증 (Hermes/Worker 출력 포함) | P5 | Hermes / Worker Agent 출력을 *외부 입력*으로 분류 + 검증 layer 강제 (헌법 5조 #4 + 8조 #3) | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력) |
   345	| **GP-5** | Provider Adapter 강제 (코드 레벨 lock-in 차단) | P6, P7 | depcruise 룰 정적 차단 + P1 facade 단일 진입점 + 분기 코드 PR 자동 reject | ADR-008 차단조건 #4 + P1 v2 |
   346	| **GP-6** | Memory / Skill Migration 가능성 (학습 자산 lock-in 차단) | P8 | JSONL append-only 표준 + 변환 스크립트 (Hermes ↔ Claude / GPT) 1회 시연 (R2-5 답습) | ADR-008 차단조건 #2 + **G4** (depend) |
   347	
   348	### 2.2 강제 메커니즘 분류 매트릭스 (계산적 / 추론적 / 자동 롤백)
   349	
   350	> **합의 §31 답습**: "Hermes 금지 8가지 × {계산적/추론적/자동 롤백}, 8 중 7 계산적 가능". 본 §2.2 는 6 GP 각각에 동일 분류 적용.
   351	
   352	| GP | 계산적 (Computational) | 추론적 (Inferential) | 자동 롤백 (Auto Rollback) |
   353	|----|---------------------|------------------|----------------------|
   354	| GP-1 | ✅ Tier-1 42 trigger UDF + R-6 actual run regex test | ⚠️ 보조 (LLM 기반 sensitive content 감지 — 본 G2 범위 외) | ✅ ROLLBACK trigger R1~R3 (R-7 SOP §5) |
   355	| GP-2 | ✅ test_redaction.py + base64 evasion test (R2-6) | ⚠️ 보조 | ✅ ROLLBACK trigger R5 (Hermes 학습 평문 검출) |
   356	| GP-3 | ✅ gitleaks / detect-secrets / chmod check / entrypoint stat | ❌ 추론 불필요 | ✅ inotify 감시 즉시 컨테이너 정지 (R1-2) |
   357	| GP-4 | ✅ 입력 schema validation + regex sanitizer + 명시 escape | ✅ 보조 (LLM 기반 prompt injection 감지 — Reviewer Agent) | ✅ Worker 출력 검증 실패 시 BLOCK |
   358	| GP-5 | ✅ depcruise 정적 분석 + PR auto-reject | ❌ 추론 불필요 | ✅ depcruise 위반 PR auto-reject (CI 강제) |
   359	| GP-6 | ✅ JSONL schema 검증 + 변환 스크립트 자동 테스트 | ⚠️ 보조 (다른 오케스트레이터 import 검증 — 부분 추론) | ✅ schema_version 호환 실패 시 export 차단 |
   360	
   361	**합산**:
   362	- 계산적 가능: 6/6 (모든 GP 가 계산적 우선 가능)
   363	- 추론적 보조: 4/6 (GP-1, GP-2, GP-4, GP-6)
   364	- 자동 롤백: 6/6 (모든 GP 가 자동 롤백 경로 명시)
   365	
   366	→ "8 중 7 계산적 가능" 보다 본 6 GP 분류는 **6/6 계산적 가능** — 합의 §31 보다 계산적 비중 높음. 사유: 본 6 GP 는 *Path-level (P1~P8)* 보다 *Enforcement-level* 추상화로 계산적 메커니즘 집계 가능.
   367	
   368	---
   369	
   370	## 3. GP-1 — DB-level Secret Persistence 차단
   371	
   372	### 3.1 정의
   373	
   374	DB INSERT 경로 (SessionDB / Memory DB / Skill DB) 에 평문 secret 이 영구 저장되지 않도록 SQLCipher BEFORE INSERT trigger + REGEXP UDF 가 모든 INSERT 를 사전 검사하여 secret 패턴 일치 시 reject 한다.
   375	
   376	### 3.2 위반 경로
   377	
   378	- **P1** — DB INSERT 평문 secret 누적
   379	
   380	### 3.3 강제 메커니즘
   381	
   382	| 분류 | 메커니즘 | 위치 |
   383	|-----|---------|-----|
   384	| 계산적 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | DB layer |
   385	| 계산적 | R-2 PoC 6 자동 검증 항목 (C1~C6) | `docker/r2-poc/` |
   386	| 계산적 | R-4.1 Tier-1 42 trigger UDF 격리 PoC | `docker/r4-1-poc/` |
   387	| 자동 회귀 | R-6 GitHub Actions workflow (push/PR/nightly) | `.github/workflows/r2-canary.yml` |
   388	| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R1~R3 | `docs/phase0/redaction-verification-sop.md` |
   389	
   390	### 3.4 Entry 기준
   391	
   392	- ✅ G1b PASS (2026-05-07, 이미 충족)
   393	- ⏳ 사용자 명시 GP-1 작업 진입 결정 (단, GP-1 은 G1b PASS 로 대부분 이미 충족)
   394	
   395	### 3.5 Exit 기준
   396	
   397	> 본 GP-1 은 **G1b PASS 의 직접 흡수** — Exit (a)~(e) 5조건이 G1b 승격 시점에 모두 충족된 상태. 본 §3.5 는 그 *증거 cross-reference* 만 명시.
   398	
   399	| # | 조건 | 충족 evidence |
   400	|---|------|------------|
   401	| (a) | 동등 이상의 보안 결과 | R-4 redaction-pattern-equivalence.md (3-way 비교 + Tier-1 42 gap 식별) |
   402	| (b) | 격리 환경 PoC 실증 | R-2 (`docker/r2-poc/`) + R-4.1 (`docker/r4-1-poc/`) |
   403	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.1 + ADR-008 부록 B Amendment |
   404	| (d) | 자동 회귀 검증 경로 확보 | R-6 actual run `25482284523` PASS (24초, 42/42, leak 0) |
   405	| (e) | 합의 APPROVE | R-7 SOP §7.3 단축 합의 (Reviewer-only) `3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` |
   406	
   407	### 3.6 산출 후보 (보강 — 본 GP-1 범위 *내*)
   408	
   409	본 GP-1 은 G1b 흡수이므로 *추가 산출 0건*. 단, G2 통합 검증 시점에 **본 §3 자체를 G1b cross-reference 형태로 합의 보고서에 인용** — 이중 보호.
   410	
   411	### 3.7 의존 ADR / 갱신 후보
   412	
   413	- ADR-011 §2.1: 본문 변경 없음, §8.5 후속 작업에 G2 GP-1 흡수 등록 (G2 PASS 시점)
   414	- ADR-008 부록 B: 본문 변경 없음, B.6 결과를 G2 GP-1 cross-reference 추가 (G2 PASS 시점)
   415	
   416	---
   417	
   418	## 4. GP-2 — Egress Redaction (로그/LLM 송신)
   419	
   420	### 4.1 정의
   421	
   422	Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.
   423	
   424	**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
   425	
   426	### 4.2 위반 경로
   427	
   428	- **P2** — 로그/LLM 송신 경로 평문 노출
   429	
   430	### 4.3 강제 메커니즘
   431	
   432	| 분류 | 메커니즘 | 위치 |
   433	|-----|---------|-----|
   434	| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
   435	| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
   436	| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
   437	| 계산적 | log file grep canary 자동 검증 | CI step (R-6 확장) |
   438	| 자동 회귀 | Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4) | R-6 workflow trigger 확장 |
   439	| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R5 (Hermes 학습 평문 검출) | R-7 SOP |
   440	
   441	### 4.4 Entry 기준
   442	
   443	- ✅ R-4 pattern equivalence 작성 완료 (충족됨)
   444	- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
   445	- ⏳ 사용자 명시 GP-2 작업 진입 결정
   446	
   447	### 4.5 Exit 기준
   448	
   449	| # | 조건 | 검증 방식 |
   450	|---|------|---------|
   451	| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
   452	| (b) | 격리 환경 PoC 실증 | log file canary inject + grep 검증 PoC (Docker 격리) |
   453	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #2 cross-reference + 본 §4 권위 |
   454	| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 에 log file canary inject step 추가 |
   455	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |
   456	
   457	### 4.6 산출 후보
   458	
   459	- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
   460	- R-6 workflow 확장 — log file canary inject step
   461	- 합의 보고서
   462	
   463	### 4.7 의존 ADR / 갱신 후보
   464	
   465	- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
   466	- ADR-008 차단조건 #1 보조 메커니즘 cross-reference
   467	
   468	---
   469	
   470	## 5. GP-3 — Credential / Secret Hygiene (저장 + 코드)

exec
/bin/bash -lc "nl -ba src/adapters/llm/redaction.py | sed -n '1,130p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""RedactionFilter — GP-2 R-2 prevention (LLM 송신 request body secret strip).
     2	
     3	SC-1 (65 entry) 합의 산출 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md`):
     4	  - 권위: governance §4.1 ("LLM API request body 에 secret 노출 차단") + 64 trajectory §3
     5	          (§8.2 RedactionFilter = egress scrub 보조)
     6	  - B-1 (ii): Tier-1 45 catalog single source = redaction_patterns (detection 과 공유)
     7	  - B-2: group-aware 치환 — secret *값* 만 마스킹, key명/JSON 구조 보존 (whole-match 금지)
     8	  - R-3: scrub() KEY_BLACKLIST (dict key 기반 redaction, §8.2 답습)
     9	
    10	GP-2 prevention 핵심 = 송신 (redact_messages). 응답/로그 redaction = 보조 (scrub).
    11	순수 함수 / 원본 불변 (R-1) — frozen 의도.
    12	"""
    13	from __future__ import annotations
    14	
    15	import re
    16	from typing import Any
    17	
    18	from src.adapters.llm.redaction_patterns import (
    19	    COMPILED_PATTERNS,
    20	    REDACTION_MARK,
    21	    REDACTION_VALUE_GROUP,
    22	    SKIP_DIRECT_REGISTER,
    23	)
    24	
    25	# §8.2 KEY_BLACKLIST — dict key 기반 redaction (값 통째 마스킹)
    26	KEY_BLACKLIST: frozenset[str] = frozenset(
    27	    {"api_key", "apikey", "token", "secret", "auth", "credential", "authorization", "password"}
    28	)
    29	
    30	
    31	def _redact_match(m: re.Match[str], value_group: int) -> str:
    32	    """단일 매칭 → group-aware 치환 (B-2). 값만 [REDACTED], key명/구분자 보존."""
    33	    if value_group == 0:
    34	        # whole match 가 secret 값 (prefix/JWT/private key — key명 없음)
    35	        return REDACTION_MARK
    36	    full = m.group(0)
    37	    if value_group == -1:
    38	        # alternation (capturing group 없음) → 첫 '=' 뒤만 (delimiter+key 보존)
    39	        eq = full.find("=")
    40	        return full[: eq + 1] + REDACTION_MARK if eq != -1 else REDACTION_MARK
    41	    # value_group > 0 → 해당 capturing group span 만 마스킹
    42	    if m.lastindex and value_group <= m.lastindex and m.group(value_group) is not None:
    43	        off = m.start()
    44	        start, end = m.span(value_group)
    45	        return full[: start - off] + REDACTION_MARK + full[end - off :]
    46	    return REDACTION_MARK
    47	
    48	
    49	class RedactionFilter:
    50	    """모든 LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""
    51	
    52	    def redact_text(self, text: str) -> str:
    53	        """str 에서 Tier-1 45 catalog 매칭 secret 값 group-aware 마스킹."""
    54	        result = text
    55	        for pid, _src, _cat, _vendor, pattern in COMPILED_PATTERNS:
    56	            if pid in SKIP_DIRECT_REGISTER:
    57	                continue
    58	            value_group = REDACTION_VALUE_GROUP.get(pid, 0)
    59	            result = pattern.sub(lambda m, vg=value_group: _redact_match(m, vg), result)
    60	        return result
    61	
    62	    def redact_messages(self, messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    63	        """송신 request body redaction (GP-2 prevention 핵심). 원본 불변 (R-1)."""
    64	        out: list[dict[str, Any]] = []
    65	        for msg in messages:
    66	            new_msg = dict(msg)  # shallow copy (원본 dict 불변)
    67	            content = new_msg.get("content")
    68	            if isinstance(content, str):
    69	                new_msg["content"] = self.redact_text(content)
    70	            elif isinstance(content, (list, dict)):
    71	                # multimodal/tool structured content → 재귀 (R-5)
    72	                new_msg["content"] = self.scrub(content)
    73	            out.append(new_msg)
    74	        return out
    75	
    76	    def scrub(self, obj: Any) -> Any:
    77	        """dict/list/str 재귀 redaction (응답/메트릭/로그, §8.2) + KEY_BLACKLIST (R-3). 원본 불변."""
    78	        if isinstance(obj, dict):
    79	            result: dict[Any, Any] = {}
    80	            for key, value in obj.items():
    81	                if isinstance(key, str) and key.lower() in KEY_BLACKLIST:
    82	                    # blacklist key → 값 통째 마스킹 (str) 또는 재귀
    83	                    result[key] = REDACTION_MARK if isinstance(value, str) else self.scrub(value)
    84	                else:
    85	                    result[key] = self.scrub(value)
    86	            return result
    87	        if isinstance(obj, list):
    88	            return [self.scrub(item) for item in obj]
    89	        if isinstance(obj, str):
    90	            return self.redact_text(obj)
    91	        return obj  # int / float / bool / None — 비밀 아님

exec
/bin/bash -lc "nl -ba tests/adapters/llm/test_facade_router.py | sed -n '1,150p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""SC-Provider Liquidity — facade complete() Router 위임 real (Core MVP, mock-verified) test.
     2	
     3	TDD RED→GREEN. 합의 `docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md` 답습:
     4	  - CB-1 model=alias (Router model_name) / CB-4 RT-1 T-A 양방향 (test_t6 대체)
     5	  - CB-5 redaction 범위 messages+system / CB-6 set_verbose=False / CB-7 강등 감지 fail-loud
     6	  - CB-8 lazy import hermetic / R-3 _normalize 속성접근 / R-5 validate_config 엣지케이스
     7	
     8	hermetic: litellm 미설치 — Router 주입 fake + asyncio.run() (pytest-asyncio 의존 0, R-8 비례 대안).
     9	"""
    10	from __future__ import annotations
    11	
    12	import asyncio
    13	import sys
    14	import types
    15	
    16	import pytest
    17	
    18	from src.adapters.llm.facade import (
    19	    ConfigError,
    20	    DegradedError,
    21	    LLMFacade,
    22	    LLMMetadata,
    23	    LLMRequest,
    24	    LLMResponse,
    25	    to_router_config,
    26	    validate_config,
    27	)
    28	from src.adapters.llm.redaction import RedactionFilter
    29	from src.adapters.llm.redaction_patterns import REDACTION_MARK
    30	
    31	# ── 공유 fixture 자료 ─────────────────────────────────────────────────────────
    32	
    33	CFG_OK = {
    34	    "routing": {"default": "anthropic-claude-api", "background_jobs": "ollama-llama-local"},
    35	    "providers": {
    36	        "anthropic-claude-api": {
    37	            "type": "anthropic",
    38	            "litellm_model": "anthropic/claude-opus-4-7",
    39	            "auth_method": "api_key",
    40	            "api_key_env": "ANTHROPIC_API_KEY",
    41	            "status": "active",
    42	        },
    43	        "ollama-llama-local": {
    44	            "type": "ollama",
    45	            "litellm_model": "ollama/llama-3.3-70b",
    46	            "auth_method": "none",
    47	            "endpoint": "http://localhost:11434",
    48	            "status": "active",
    49	        },
    50	    },
    51	}
    52	
    53	
    54	def _fake_response(content: str = "ok"):
    55	    """litellm ModelResponse 형태 모사 — 속성 접근 (R-3, dict mock 금지)."""
    56	    msg = types.SimpleNamespace(content=content)
    57	    choice = types.SimpleNamespace(message=msg, finish_reason="stop")
    58	    usage = types.SimpleNamespace(prompt_tokens=11, completion_tokens=22)
    59	    return types.SimpleNamespace(choices=[choice], usage=usage, id="req-123")
    60	
    61	
    62	class FakeRouter:
    63	    """litellm.Router 주입 대체 — acompletion 인자 캡처 (속성 인터페이스)."""
    64	
    65	    def __init__(self, *, raise_exc: Exception | None = None) -> None:
    66	        self.received: dict = {}
    67	        self._raise = raise_exc
    68	
    69	    async def acompletion(self, *, model, messages, **opts):
    70	        self.received = {"model": model, "messages": messages, "opts": opts}
    71	        if self._raise is not None:
    72	            raise self._raise
    73	        return _fake_response()
    74	
    75	
    76	# litellm 표준 예외 모사 (name 기반 감지 — hermetic)
    77	class AuthenticationError(Exception):
    78	    pass
    79	
    80	
    81	class ServiceUnavailableError(Exception):
    82	    pass
    83	
    84	
    85	# ── T-A ⭐ (RT-1 양방향, CB-4 — test_t6 대체): Router 입력 = redacted output ──
    86	def test_a_rt1_router_receives_redacted_messages_and_system() -> None:
    87	    facade = LLMFacade(config=CFG_OK, redactor=RedactionFilter(), router=FakeRouter())
    88	    req = LLMRequest(
    89	        messages=[{"role": "user", "content": "my key sk-ant-LEAKSECRET1234567890 here"}],
    90	        model_alias="default",
    91	        system="system prompt API_KEY=sk-ant-SYSLEAK1234567890 trailing",
    92	    )
    93	    asyncio.run(facade.complete(req))
    94	    sent = facade._router.received["messages"]  # type: ignore[attr-defined]
    95	    blob = str(sent)
    96	    # 양방향: 원본 secret 부재 AND REDACTION_MARK 존재 (한쪽만 = trap)
    97	    assert "sk-ant-LEAKSECRET1234567890" not in blob
    98	    assert "sk-ant-SYSLEAK1234567890" not in blob
    99	    assert REDACTION_MARK in blob
   100	    # system 이 redacted 된 채 messages 에 포함
   101	    assert any(m.get("role") == "system" for m in sent)
   102	
   103	
   104	# ── T-B (CB-1): model=alias(provider_key) + 정규화 (raw 누출 0) ───────────────
   105	def test_b_router_model_is_alias_and_normalized_response() -> None:
   106	    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
   107	    resp = asyncio.run(
   108	        facade.complete(LLMRequest(messages=[{"role": "user", "content": "hi"}], model_alias="default"))
   109	    )
   110	    # CB-1: Router 가 받은 model = routing 해소 alias(=model_name), litellm_model 아님
   111	    assert facade._router.received["model"] == "anthropic-claude-api"  # type: ignore[attr-defined]
   112	    assert facade._router.received["model"] != "anthropic/claude-opus-4-7"  # type: ignore[attr-defined]
   113	    # 정규화: LLMResponse(content, usage, LLMMetadata) — 속성접근, raw 누출 0
   114	    assert isinstance(resp, LLMResponse)
   115	    assert resp.content == "ok"
   116	    assert resp.usage == {"input_tokens": 11, "output_tokens": 22}
   117	    assert isinstance(resp.metadata, LLMMetadata)
   118	    assert resp.metadata.provider_used == "anthropic-claude-api"
   119	    assert resp.metadata.finish_reason == "stop"
   120	    assert resp.metadata.request_id == "req-123"
   121	
   122	
   123	# ── T-C (R-5): validate_config fail-fast 엣지케이스 ───────────────────────────
   124	def test_c_validate_config_failfast() -> None:
   125	    # active 1개 → Min 2 위반
   126	    with pytest.raises(ConfigError, match="Min 2"):
   127	        validate_config({"providers": {"a": {"type": "anthropic", "status": "active"}}})
   128	    # 동일 type 2개 active 금지
   129	    with pytest.raises(ConfigError, match="동일 type"):
   130	        validate_config(
   131	            {
   132	                "providers": {
   133	                    "a": {"type": "anthropic", "status": "active"},
   134	                    "b": {"type": "anthropic", "status": "active"},
   135	                }
   136	            }
   137	        )
   138	    # type 필드 누락
   139	    with pytest.raises(ConfigError, match="type 필드 누락"):
   140	        validate_config(
   141	            {"providers": {"a": {"status": "active"}, "b": {"type": "ollama", "status": "active"}}}
   142	        )
   143	
   144	
   145	# ── T-D: 정상 2 active 다른 type → pass ───────────────────────────────────────
   146	def test_d_validate_config_ok() -> None:
   147	    validate_config(CFG_OK)  # 예외 0
   148	
   149	
   150	# ── T-E (CB-7): 런타임 강등 감지 fail-loud ────────────────────────────────────

exec
/bin/bash -lc "nl -ba tests/adapters/llm/test_facade_router.py | sed -n '150,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   150	# ── T-E (CB-7): 런타임 강등 감지 fail-loud ────────────────────────────────────
   151	def test_e_runtime_degradation_failloud() -> None:
   152	    # 2 active 중 1개 auth 실패 → remaining active < 2 → DegradedError + stderr
   153	    facade = LLMFacade(config=CFG_OK, router=FakeRouter(raise_exc=AuthenticationError("401")))
   154	    with pytest.raises(DegradedError, match="차단조건 #5"):
   155	        asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "x"}])))
   156	
   157	
   158	def test_e2_degradation_reraise_when_spare_active() -> None:
   159	    # 3 active → 1개 실패해도 remaining 2 ≥ 2 → 원 예외 re-raise (DegradedError 아님)
   160	    cfg = {
   161	        "routing": {"default": "p1"},
   162	        "providers": {
   163	            "p1": {"type": "anthropic", "litellm_model": "anthropic/x", "status": "active"},
   164	            "p2": {"type": "ollama", "litellm_model": "ollama/y", "status": "active"},
   165	            "p3": {"type": "openai", "litellm_model": "openai/z", "status": "active"},
   166	        },
   167	    }
   168	    facade = LLMFacade(config=cfg, router=FakeRouter(raise_exc=ServiceUnavailableError("503")))
   169	    with pytest.raises(ServiceUnavailableError):
   170	        asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "x"}], model_alias="default")))
   171	
   172	
   173	# ── T-F (D2/D3): LLMRequest/LLMMetadata frozen 화이트리스트 ────────────────────
   174	def test_f_dataclass_whitelist_frozen() -> None:
   175	    req = LLMRequest(messages=[{"role": "user", "content": "hi"}], model_alias="default", metadata_in={"x": 1})
   176	    assert req.model_alias == "default"
   177	    meta = LLMMetadata(provider_used="p", fallback_chain=["p"], finish_reason="stop")
   178	    with pytest.raises(Exception):  # frozen — 변경 불가
   179	        meta.provider_used = "q"  # type: ignore[misc]
   180	    # 화이트리스트 외 키 거부
   181	    with pytest.raises(TypeError):
   182	        LLMMetadata(provider_used="p", fallback_chain=[], finish_reason="s", raw="leak")  # type: ignore[call-arg]
   183	
   184	
   185	# ── T-G (D6/CB-1): to_router_config model_name=alias + api_key 보간 ───────────
   186	def test_g_to_router_config_model_name_is_alias(monkeypatch) -> None:
   187	    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-REALKEY")
   188	    rc = to_router_config(CFG_OK)
   189	    entries = {e["model_name"]: e for e in rc["model_list"]}
   190	    # model_name = provider key(alias), litellm_params.model = litellm_model
   191	    assert "anthropic-claude-api" in entries
   192	    assert entries["anthropic-claude-api"]["litellm_params"]["model"] == "anthropic/claude-opus-4-7"
   193	    assert entries["anthropic-claude-api"]["litellm_params"]["api_key"] == "sk-ant-REALKEY"
   194	    # ollama auth_method=none → endpoint(api_base)만, api_key 0
   195	    assert entries["ollama-llama-local"]["litellm_params"]["api_base"] == "http://localhost:11434"
   196	    assert "api_key" not in entries["ollama-llama-local"]["litellm_params"]
   197	
   198	
   199	# ── T-H (CB-8 hermetic): litellm 미설치에서 facade 동작 + import 0 ────────────
   200	def test_h_hermetic_no_litellm_import() -> None:
   201	    sys.modules.pop("litellm", None)
   202	    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
   203	    asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "hi"}])))
   204	    # 주입 경로 = litellm import 0 (top-level 회귀 시 RED)
   205	    assert "litellm" not in sys.modules
   206	
   207	
   208	# ── T-I (CB-6): _build_router 가 litellm.set_verbose=False 설정 ───────────────
   209	def test_i_build_router_disables_litellm_verbose(monkeypatch) -> None:
   210	    fake_litellm = types.ModuleType("litellm")
   211	    fake_litellm.set_verbose = True  # type: ignore[attr-defined]
   212	
   213	    class _Router:
   214	        def __init__(self, **kw):
   215	            self.kw = kw
   216	
   217	    fake_litellm.Router = _Router  # type: ignore[attr-defined]
   218	    monkeypatch.setitem(sys.modules, "litellm", fake_litellm)
   219	
   220	    facade = LLMFacade(config=CFG_OK)  # router=None → lazy build
   221	    router = facade._build_router()  # type: ignore[attr-defined]
   222	    assert fake_litellm.set_verbose is False  # CB-6 내장 로깅 비활성
   223	    # model_list 가 Router 에 전달 (model_name=alias)
   224	    names = {e["model_name"] for e in router.kw["model_list"]}
   225	    assert names == {"anthropic-claude-api", "ollama-llama-local"}
   226	
   227	
   228	# ── T-K (R-2): health() 축소 fallback — dict[str, bool] ───────────────────────
   229	def test_k_health_reduced_fallback() -> None:
   230	    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
   231	    h = asyncio.run(facade.health())
   232	    assert isinstance(h, dict)
   233	    assert h == {"anthropic-claude-api": True, "ollama-llama-local": True}

exec
/bin/bash -lc "rg -n \"complete\\(|LLMRequest|LLMFacade|asyncio\\.run|pytest-asyncio|async\" src tests/jarvis tests/adapters -g '*.py'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/adapters/llm/test_facade_router.py:1:"""SC-Provider Liquidity — facade complete() Router 위임 real (Core MVP, mock-verified) test.
tests/adapters/llm/test_facade_router.py:8:hermetic: litellm 미설치 — Router 주입 fake + asyncio.run() (pytest-asyncio 의존 0, R-8 비례 대안).
tests/adapters/llm/test_facade_router.py:12:import asyncio
tests/adapters/llm/test_facade_router.py:21:    LLMFacade,
tests/adapters/llm/test_facade_router.py:23:    LLMRequest,
tests/adapters/llm/test_facade_router.py:69:    async def acompletion(self, *, model, messages, **opts):
tests/adapters/llm/test_facade_router.py:87:    facade = LLMFacade(config=CFG_OK, redactor=RedactionFilter(), router=FakeRouter())
tests/adapters/llm/test_facade_router.py:88:    req = LLMRequest(
tests/adapters/llm/test_facade_router.py:93:    asyncio.run(facade.complete(req))
tests/adapters/llm/test_facade_router.py:106:    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
tests/adapters/llm/test_facade_router.py:107:    resp = asyncio.run(
tests/adapters/llm/test_facade_router.py:108:        facade.complete(LLMRequest(messages=[{"role": "user", "content": "hi"}], model_alias="default"))
tests/adapters/llm/test_facade_router.py:153:    facade = LLMFacade(config=CFG_OK, router=FakeRouter(raise_exc=AuthenticationError("401")))
tests/adapters/llm/test_facade_router.py:155:        asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "x"}])))
tests/adapters/llm/test_facade_router.py:168:    facade = LLMFacade(config=cfg, router=FakeRouter(raise_exc=ServiceUnavailableError("503")))
tests/adapters/llm/test_facade_router.py:170:        asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "x"}], model_alias="default")))
tests/adapters/llm/test_facade_router.py:173:# ── T-F (D2/D3): LLMRequest/LLMMetadata frozen 화이트리스트 ────────────────────
tests/adapters/llm/test_facade_router.py:175:    req = LLMRequest(messages=[{"role": "user", "content": "hi"}], model_alias="default", metadata_in={"x": 1})
tests/adapters/llm/test_facade_router.py:202:    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
tests/adapters/llm/test_facade_router.py:203:    asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "hi"}])))
tests/adapters/llm/test_facade_router.py:220:    facade = LLMFacade(config=CFG_OK)  # router=None → lazy build
tests/adapters/llm/test_facade_router.py:230:    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
tests/adapters/llm/test_facade_router.py:231:    h = asyncio.run(facade.health())
src/adapters/llm/facade.py:1:"""LLMFacade — Provider-agnostic facade (G2 GP-5, Provider Liquidity 5조-2).
src/adapters/llm/facade.py:8:SC-Provider Liquidity (69 entry): **facade `complete()` Router 위임 real (Core MVP, mock-verified)** —
src/adapters/llm/facade.py:19:scope (Core MVP): complete() + validate_config + 런타임 강등 감지(fail-loud) + 응답 정규화.
src/adapters/llm/facade.py:45:class LLMRequest:
src/adapters/llm/facade.py:91:    litellm_model 은 litellm_params.model 내부에만 존재 (complete() 호출 경로 노출 0,
src/adapters/llm/facade.py:107:class LLMFacade:
src/adapters/llm/facade.py:156:    def _redact_request(self, request: LLMRequest) -> dict[str, Any]:
src/adapters/llm/facade.py:164:    def _build_opts(self, request: LLMRequest) -> dict[str, Any]:
src/adapters/llm/facade.py:193:    async def complete(self, request: LLMRequest) -> LLMResponse:
src/adapters/llm/facade.py:230:    async def health(self) -> dict[str, bool]:

exec
/bin/bash -lc 'rg -n "import-linter|litellm|adapters.llm.facade|forbidden|provider" .importlinter pyproject.toml setup.cfg tox.ini requirements.txt 2>/dev/null' in /home/delangi/문서/project/category/AI_development_tool
 exited 2 in 0ms:
requirements.txt:4:#   - docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md (v1.1) §4.2
requirements.txt:5:#   - docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md (CB-3, 4 source 수렴)
requirements.txt:6:#   - docs/architecture/llm-providers-design.md §1.2 (Option β — LiteLLM facade 승격, Apache 2.0)
requirements.txt:16:#   - 충족 (비협상): litellm 직접 핀 exact version + sha256 wheel hash (아래) + lock diff 회귀(git diff)
requirements.txt:21:# LiteLLM 직접 import = src/adapters/llm/facade.py 한 파일 한정 (ADR-009 §2.2 #1, import-linter).
requirements.txt:24:litellm==1.86.2 \
.importlinter:1:; G2 GP-5 2차 PoC — Provider Adapter Enforcement Layer 1 (T-2 import-linter)
.importlinter:4:;   - docs/architecture/llm-providers-design.md §9.3 (allow path / forbidden path 시제 의도)
.importlinter:9:;   - 본 룰: 4종 (openai, anthropic, litellm, ollama) direct/from/transitive 차단
.importlinter:10:;   - google.generativeai: 1차 AST scanner 단독 책무 (각주 1 — import-linter 제약 답습)
.importlinter:17:;   forbidden 모듈 미설치 환경에서도 정상 검출 (C-9 RA-9 사전 검증 PASS, 2026-05-10).
.importlinter:26:type = forbidden
.importlinter:29:forbidden_modules =
.importlinter:32:    litellm
.importlinter:35:    src.adapters.llm.facade -> *

codex
1. **판정: APPROVE WITH CONDITIONS**

설계 방향은 승인 가능하지만, test/redaction 경계와 alias fallback 해석은 v1.1에서 수정해야 합니다.

2. **BLOCKING 항목**

1. **T-RT1 테스트 위치가 facade 책임 경계와 불일치**
   - brief는 “fake facade가 받은 `LLMRequest.messages`에 원본 secret 부재 AND `REDACTION_MARK` 존재”를 요구합니다: [boss-worker-facade-consolidation-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/boss-worker-facade-consolidation-brief.md:101).
   - 그러나 실제 redaction은 `LLMFacade.complete()` 내부에서 `_redact_request()` 호출 후 Router로 넘기기 직전에 수행됩니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:193), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:196).
   - 따라서 `OllamaBoss/OllamaWorker`가 fake facade에 넘기는 `LLMRequest`는 원칙상 raw input이어야 합니다. redaction된 request를 fake facade 입력에서 기대하면 redaction 책임이 caller로 새거나, fake가 real facade와 다른 의미를 갖습니다.
   - 조건: T-RT1은 “real `LLMFacade` + `FakeRouter`”로 Router가 받은 messages를 검사하도록 바꾸십시오. 기존 facade test도 같은 경계를 검증합니다: [test_facade_router.py](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_facade_router.py:85), [test_facade_router.py](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_facade_router.py:93).

2. **미등록 `model_alias` fallback을 안전장치로 서술한 점은 부정확**
   - brief RT-3은 “model_alias 미등록 → facade `_resolve` default fallback”을 대응으로 둡니다: [boss-worker-facade-consolidation-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/boss-worker-facade-consolidation-brief.md:136).
   - 실제 `_resolve()`는 unknown alias를 `routing.default` 또는 첫 provider로 조용히 fallback합니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:148), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:154).
   - 현재 default는 Anthropic입니다: [llm-providers.yaml](/home/delangi/문서/project/category/AI_development_tool/llm-providers.yaml:16), [llm-providers.yaml](/home/delangi/문서/project/category/AI_development_tool/llm-providers.yaml:17). Jarvis local boss/worker alias typo가 생기면 Ollama가 아니라 default provider로 나갈 수 있습니다.
   - 조건: `jarvis_boss`/`jarvis_worker` routing alias를 명시 등록하거나, 생성자에서 기존 `ollama-llama-local` alias만 쓰도록 test로 고정하십시오. 이 cycle에서 facade 본문 변경 0을 유지한다면 fallback을 “대응”으로 쓰면 안 됩니다.

3. **권고 항목**

1. `asyncio.run()`은 Protocol 보존을 위해 수용 가능하지만, “중첩 루프 없음” 단정은 약합니다. `advise()`/`run()`이 async test, notebook, async orchestrator 후보에서 호출되면 `RuntimeError`가 납니다. brief의 RT-2 문구는 “현재 sync orchestrator 경로에서는 허용, async caller에서는 unsupported/fail-loud”로 낮추는 편이 정확합니다. 현재 `Orchestrator.dispatch()`는 sync이고 worker/boss 호출도 sync입니다: [orchestrator.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/orchestrator.py:120), [orchestrator.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/orchestrator.py:125), [orchestrator.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/orchestrator.py:138).

2. D4 rename은 권고로만 두는 것이 적절합니다. `OllamaBoss`/`OllamaWorker` 명칭은 provider-neutral 원칙과 긴장이 있지만, 외부 wiring 문서와 테스트 영향이 큽니다. 이번 cycle의 핵심은 facade 통합이므로 rename은 별도 또는 alias class 방식이 더 안전합니다.

3. worker 응답 redaction deferred는 기존 facade 정책과 일관되지만, “응답/파일 누출 방지”로 확장 주장하면 안 됩니다. `OllamaWorker`는 응답 content를 fence strip 후 파일에 씁니다: [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:308), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:310), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:341).

4. **NOTE**

- 현 구현이 facade를 우회한다는 brief 전제는 맞습니다. `OllamaBoss`는 `urllib.request.urlopen()`으로 localhost `/api/chat`에 직접 POST합니다: [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:222), [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:229). `OllamaWorker`도 동일합니다: [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:288), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:293).
- `BossLLM`/`Worker` Protocol 보존은 타당합니다: [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:58), [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:68), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:78), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:84).
- src 내 instantiation 0 주장은 대체로 맞습니다. `rg` 결과 `src/`에서는 class 정의/docstring 외 호출처가 없고, 실 instantiation은 tests/docs에 집중되어 있습니다.

5. **트랙 B 번복 독립 판단**

번복이 정당합니다. 트랙 B의 원래 정당성은 “외부 LLM SDK 직접 import 없이 stdlib urllib로 로컬 Ollama 호출”이었지만, 현재 facade는 Router 위임 real이며 redaction도 facade 내부에 붙어 있습니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:8), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:193). ADR-009는 모든 Worker/Hermes Agent LLM 호출의 facade 단일 진입점을 요구합니다: [ADR-009](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:31), [ADR-009](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:64).

다만 번복 대상은 정확히 “OllamaBoss/OllamaWorker 내부의 provider 직결”이어야 합니다. `BossLLM` Protocol, `StubBoss`, `WorkerRegistry`, orchestrator는 유지하는 것이 SDD상 더 견고합니다.

6. **권위 인용 Cross-Verify 매트릭스**

| brief 인용 | 실제 문서/코드 | 판정 |
|---|---|---|
| ADR-009 §2.2 facade 단일 진입점 | 모든 Worker/Hermes Agent LLM 호출 facade 경유, LiteLLM 직접 import facade 한정: [ADR-009:31](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:31), [ADR-009:70](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:70) | 일치 |
| ADR-008 #4 단일 provider adapter | “provider 어댑터 1개 추상화 + 분기 코드 금지”: [ADR-008](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-008-hermes-adoption-decision.md:21) | 일치 |
| governance §4.1 LLM request body redaction | GP-2가 stdout/stderr/log/LLM API request body secret 노출 사전 차단을 정의: [governance](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:420), [governance](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:422) | 일치 |
| facade redaction 범위 messages + system | `_redact_request()`가 messages와 optional system을 redact: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:156), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:162) | 일치 |
| Min 2 active 보존 | `validate_config()` active < 2 및 동일 type active 차단: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:75), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:85) | 일치 |
| “T-RT1 fake facade received redacted request” | redaction은 facade 입력 전이 아니라 facade 내부 Router 위임 전 수행 | 모순, 수정 필요 |
tokens used
92,014
1. **판정: APPROVE WITH CONDITIONS**

설계 방향은 승인 가능하지만, test/redaction 경계와 alias fallback 해석은 v1.1에서 수정해야 합니다.

2. **BLOCKING 항목**

1. **T-RT1 테스트 위치가 facade 책임 경계와 불일치**
   - brief는 “fake facade가 받은 `LLMRequest.messages`에 원본 secret 부재 AND `REDACTION_MARK` 존재”를 요구합니다: [boss-worker-facade-consolidation-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/boss-worker-facade-consolidation-brief.md:101).
   - 그러나 실제 redaction은 `LLMFacade.complete()` 내부에서 `_redact_request()` 호출 후 Router로 넘기기 직전에 수행됩니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:193), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:196).
   - 따라서 `OllamaBoss/OllamaWorker`가 fake facade에 넘기는 `LLMRequest`는 원칙상 raw input이어야 합니다. redaction된 request를 fake facade 입력에서 기대하면 redaction 책임이 caller로 새거나, fake가 real facade와 다른 의미를 갖습니다.
   - 조건: T-RT1은 “real `LLMFacade` + `FakeRouter`”로 Router가 받은 messages를 검사하도록 바꾸십시오. 기존 facade test도 같은 경계를 검증합니다: [test_facade_router.py](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_facade_router.py:85), [test_facade_router.py](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_facade_router.py:93).

2. **미등록 `model_alias` fallback을 안전장치로 서술한 점은 부정확**
   - brief RT-3은 “model_alias 미등록 → facade `_resolve` default fallback”을 대응으로 둡니다: [boss-worker-facade-consolidation-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/boss-worker-facade-consolidation-brief.md:136).
   - 실제 `_resolve()`는 unknown alias를 `routing.default` 또는 첫 provider로 조용히 fallback합니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:148), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:154).
   - 현재 default는 Anthropic입니다: [llm-providers.yaml](/home/delangi/문서/project/category/AI_development_tool/llm-providers.yaml:16), [llm-providers.yaml](/home/delangi/문서/project/category/AI_development_tool/llm-providers.yaml:17). Jarvis local boss/worker alias typo가 생기면 Ollama가 아니라 default provider로 나갈 수 있습니다.
   - 조건: `jarvis_boss`/`jarvis_worker` routing alias를 명시 등록하거나, 생성자에서 기존 `ollama-llama-local` alias만 쓰도록 test로 고정하십시오. 이 cycle에서 facade 본문 변경 0을 유지한다면 fallback을 “대응”으로 쓰면 안 됩니다.

3. **권고 항목**

1. `asyncio.run()`은 Protocol 보존을 위해 수용 가능하지만, “중첩 루프 없음” 단정은 약합니다. `advise()`/`run()`이 async test, notebook, async orchestrator 후보에서 호출되면 `RuntimeError`가 납니다. brief의 RT-2 문구는 “현재 sync orchestrator 경로에서는 허용, async caller에서는 unsupported/fail-loud”로 낮추는 편이 정확합니다. 현재 `Orchestrator.dispatch()`는 sync이고 worker/boss 호출도 sync입니다: [orchestrator.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/orchestrator.py:120), [orchestrator.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/orchestrator.py:125), [orchestrator.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/orchestrator.py:138).

2. D4 rename은 권고로만 두는 것이 적절합니다. `OllamaBoss`/`OllamaWorker` 명칭은 provider-neutral 원칙과 긴장이 있지만, 외부 wiring 문서와 테스트 영향이 큽니다. 이번 cycle의 핵심은 facade 통합이므로 rename은 별도 또는 alias class 방식이 더 안전합니다.

3. worker 응답 redaction deferred는 기존 facade 정책과 일관되지만, “응답/파일 누출 방지”로 확장 주장하면 안 됩니다. `OllamaWorker`는 응답 content를 fence strip 후 파일에 씁니다: [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:308), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:310), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:341).

4. **NOTE**

- 현 구현이 facade를 우회한다는 brief 전제는 맞습니다. `OllamaBoss`는 `urllib.request.urlopen()`으로 localhost `/api/chat`에 직접 POST합니다: [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:222), [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:229). `OllamaWorker`도 동일합니다: [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:288), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:293).
- `BossLLM`/`Worker` Protocol 보존은 타당합니다: [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:58), [boss.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/boss.py:68), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:78), [worker.py](/home/delangi/문서/project/category/AI_development_tool/src/jarvis/worker.py:84).
- src 내 instantiation 0 주장은 대체로 맞습니다. `rg` 결과 `src/`에서는 class 정의/docstring 외 호출처가 없고, 실 instantiation은 tests/docs에 집중되어 있습니다.

5. **트랙 B 번복 독립 판단**

번복이 정당합니다. 트랙 B의 원래 정당성은 “외부 LLM SDK 직접 import 없이 stdlib urllib로 로컬 Ollama 호출”이었지만, 현재 facade는 Router 위임 real이며 redaction도 facade 내부에 붙어 있습니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:8), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:193). ADR-009는 모든 Worker/Hermes Agent LLM 호출의 facade 단일 진입점을 요구합니다: [ADR-009](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:31), [ADR-009](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:64).

다만 번복 대상은 정확히 “OllamaBoss/OllamaWorker 내부의 provider 직결”이어야 합니다. `BossLLM` Protocol, `StubBoss`, `WorkerRegistry`, orchestrator는 유지하는 것이 SDD상 더 견고합니다.

6. **권위 인용 Cross-Verify 매트릭스**

| brief 인용 | 실제 문서/코드 | 판정 |
|---|---|---|
| ADR-009 §2.2 facade 단일 진입점 | 모든 Worker/Hermes Agent LLM 호출 facade 경유, LiteLLM 직접 import facade 한정: [ADR-009:31](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:31), [ADR-009:70](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:70) | 일치 |
| ADR-008 #4 단일 provider adapter | “provider 어댑터 1개 추상화 + 분기 코드 금지”: [ADR-008](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-008-hermes-adoption-decision.md:21) | 일치 |
| governance §4.1 LLM request body redaction | GP-2가 stdout/stderr/log/LLM API request body secret 노출 사전 차단을 정의: [governance](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:420), [governance](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:422) | 일치 |
| facade redaction 범위 messages + system | `_redact_request()`가 messages와 optional system을 redact: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:156), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:162) | 일치 |
| Min 2 active 보존 | `validate_config()` active < 2 및 동일 type active 차단: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:75), [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:85) | 일치 |
| “T-RT1 fake facade received redacted request” | redaction은 facade 입력 전이 아니라 facade 내부 Router 위임 전 수행 | 모순, 수정 필요 |
