# boss/worker 송신 redaction 적용 (RT-1, 축소 scope (나)) 구현 brief (v1.1)

> **작성**: 2026-05-28 (70번째 entry 진입 cycle — 세션 #4)
>
> **v1 → v1.1 reframe (scope 축소 (나))**: v1은 "boss/worker facade.complete() 전체 통합"이었으나, 풀 3+1 + 외부 LLM 1+(codex gpt-5.5) 합의(`docs/review/3plus1-consensus-2026-05-28-boss-worker-facade-consolidation.md`, 4 source APPROVE WITH CONDITIONS)가 **CC-0 중대 충돌**을 발견 → 사용자 **(나) 축소 선택**:
> - **CC-0**: facade `validate_config` "동일 type 2개 active 금지"(R5) ↔ jarvis boss=Qwen/worker=GLM(둘 다 ollama type) → facade 전체 마이그레이션은 **역할별 모델 분리 상실** + examples 파괴(CC-3) + silent cloud fallback(CC-2). 게다가 `jarvis-mvp1-m3-m4` 합의가 현 `OllamaBoss(model=...)` arg 주입을 *이미 Provider Liquidity 정합(M3-F)*으로 판정 → (c)의 Liquidity gap 동인 약함.
> - **(나) 결정**: facade 전체 마이그레이션 대신 **boss/worker의 urllib 송신 경로에 `RedactionFilter`만 적용**(송신 secret strip). 보안 gap(RT-1) 해소 + 역할별 모델 분리 보존 + examples 무파괴 + facade 마이그레이션 0.
>
> **scope (나)**:
> - `OllamaBoss.advise()` + `OllamaWorker.run()`이 urllib POST *전* request messages를 `RedactionFilter.redact_messages`로 redact.
> - **facade.complete() 마이그레이션 0** / model_alias/registry 0 / asyncio 0 / 생성자 호환(redactor optional default → examples/test 무파괴).
> - ⚠️ **RT-1 = 송신(request body) 경로 한정**(CC-4): boss summary→`memory.py` JSONL 평문 영속 + worker 응답→파일 작성은 *응답 redaction*(deferred, 69 CB-6 동형) — 본 cycle 미적용. "boss/worker 경로 *전체* 보호" over-claim 금지.
>
> **명칭 정직성** ([[feedback_pass_scope_overclaim]], 누적 8회 cascade — CC-4 = 본 세션 #4 2번째): 본 cycle = **송신 redaction 적용 한정**. "facade 통합 / Provider Liquidity 완전 발효 / boss/worker 경로 완전 보호" 아님. ADR-009 §2.2 facade 단일 진입점은 **미충족**(BossLLM Protocol 추상 유지 — 별도 영역).
>
> **선행 답습**: `src/adapters/llm/redaction.py`(65 SC-1 RedactionFilter — redact_messages, 패턴 내용 0 변경) + `boss.py`/`worker.py`(트랙 B urllib 현 구현 보존) + governance §4.1(LLM request body redaction = GP-2) + 합의 보고서(CC-0 (나) + CC-4 송신 한정)

---

## §0 범위

### §0.1 하는 것
1. `OllamaBoss`/`OllamaWorker`에 `redactor: RedactionFilter` 주입(optional default) (§2)
2. `advise()`/`run()` urllib POST *전* messages redact (송신 secret strip) (§2)
3. RT-1 송신 한정 정직 framing(CC-4) + GP-2 prevention boss/worker 송신 경로 확장 (§3)
4. TDD (신규 T-RED + 기존 test 무변경 검증) (§4)
5. 금지 + Rollback + Evidence + 자기진단 (§5~§8)

### §0.2 하지 않는 것

| # | 영역 | 본 cycle |
|---|------|----|
| 1 | facade.complete() 마이그레이션 / model_alias / registry / asyncio | 0 ((나) = redaction만, CC-0 충돌 회피) |
| 2 | ADR-009 §2.2 facade 단일 진입점 충족 | 0 (BossLLM Protocol 추상 유지 — 별도 영역) |
| 3 | 응답 redaction (boss summary memory JSONL / worker 파일) | 0 (deferred, 69 CB-6 동형 — CC-4 송신 한정) |
| 4 | 65 RedactionFilter 패턴 *내용* 변경 | 0 (협력자 재사용) |
| 5 | 생성자 시그니처 breaking (model→model_alias 등) | 0 (redactor optional default → examples/test 무파괴) |
| 6 | CliWorker/TmuxWorker (subprocess 비-LLM) | 0 |
| 7 | "facade 통합 / Provider Liquidity 완전 발효" 선언 | 0 |
| 8 | 자동 후속 sub-cycle | 0 |

### §0.3 권위 답습
- `src/adapters/llm/redaction.py`(RedactionFilter.redact_messages — 송신 redaction, group-aware) / `boss.py`(OllamaBoss.advise messages) / `worker.py`(OllamaWorker.run messages) / governance §4.1(GP-2 LLM request body) / 합의 CC-0(나)·CC-4

---

## §1 진입 컨텍스트
- 69 facade real → carry-over streaming 검토 → boss/worker 트랙 B urllib 우회 발견 → (c) facade 통합 시도 → 합의 CC-0 충돌(동일 type 금지 ↔ 역할별 모델) → 사용자 (나) 축소.
- 현 보안 gap: boss는 **untrusted worker output**(prompt injection 표적, `boss.py` docstring §5 신뢰 경계)을 urllib로 **redaction 없이** Ollama 송신. 본 cycle = 그 송신 경로에 RedactionFilter 적용(GP-2 prevention 확장, 송신 한정).

---

## §2 구현 설계

### D1. redactor 주입 (optional default — 무파괴)
- `OllamaBoss.__init__(model, timeout_s=..., system_prompt=None, redactor: RedactionFilter | None = None)` — `redactor or RedactionFilter()`. 기존 인자 순서/이름 보존 → `OllamaBoss(model=..., timeout_s=...)`(examples/test) 무파괴.
- `OllamaWorker.__init__(alias, model, output_filename=None, timeout_s=..., system_prompt=None, redactor=None)` 동형.
- import: `from src.adapters.llm.redaction import RedactionFilter` (SDK 아님 → import-linter 무관, 정상 내부 의존 src.jarvis → src.adapters.llm.redaction).

### D2. 송신 redaction 적용 지점
- `advise()`: `messages = [{system}, {user_blob}]` 구성 후 **`messages = self._redactor.redact_messages(messages)`** → body에 redacted messages. user_blob(worker output 포함) secret strip.
- `run()`: `messages = [{system}, {prompt}]` 구성 후 동일 redact → body.
- urllib POST 경로 자체는 보존(트랙 B 유지 — facade 미경유). redaction은 json.dumps 전 적용.

### D3. 정상 내용 무손상
- RedactionFilter = Tier-1 secret 패턴 한정(sk-/Bearer/api_key= 등). 정상 worker 코드/명령/한국어 텍스트 무변경(65 T-4 false-positive 동형). 기존 test fixture(benign "작업 X"/"결과 Y") → redaction 무변경 → **기존 urllib-mock test 무영향**(실측 §4).

---

## §3 RT-1 송신 한정 정직 (CC-4 over-claim 차단)
- **적용**: 송신(request body) 경로 — boss/worker가 Ollama로 보내는 messages secret strip. GP-2 prevention(governance §4.1)이 boss/worker **송신 경로**까지 확장.
- ⚠️ **미적용 (deferred, 정직 명문)**: 응답 경로 — boss `BossAdvice.summary`는 orchestrator/`memory.py` JSONL 평문 영속, worker 응답은 파일 작성. 이들 *응답* redaction은 본 cycle 0(69 CB-6 동형 deferred). → **"boss/worker 경로 *전체* 보호" 표현 금지** — "송신 경로 redaction 적용" 한정.
- detection≠prevention가 응답 경로에 적용(누적 8회 cascade 교훈).

---

## §4 TDD 계획

### §4.1 RED
- **T-RED-1 (boss 송신 redaction)**: secret(`sk-ant-...`) 포함 worker output으로 `OllamaBoss.advise()` → urllib mock이 capture한 POST body messages에 **원본 secret 부재 AND `REDACTION_MARK` 존재**(양방향). + benign 부분("작업 X" 등) 보존.
- **T-RED-2 (worker 송신 redaction)**: secret 포함 prompt로 `OllamaWorker.run()` → POST body messages redacted (양방향).
- **T-RED-3 (정상 내용 무손상)**: benign prompt → redaction 무변경(기존 동작).
- **기존 test 무변경 검증**: test_ollama_boss/worker.py 기존 urllib-mock test가 benign fixture라 redaction 무영향 — 회귀 0 확인(재작성 0).

### §4.2 GREEN
- `boss.py`: redactor 주입 + advise messages redact. `worker.py`: redactor 주입 + run messages redact.

### §4.3 REFACTOR + verify
- 커버리지 70%+. **verify**: `.venv/bin/python -m pytest tests/ -q`(177 회귀 0) + import-linter(SDK import 0 보존 — RedactionFilter는 SDK 아님) + grimp negative control(facade 외부 litellm 0) + secret_scanner scan-source 0.

---

## §5 금지
§0.2 답습. 추가: facade.complete() 호출 0 / litellm import 0 / model_alias·registry 변경 0 / 생성자 breaking 0 / 응답 redaction 0 / 65 패턴 내용 0 / "facade 통합/Provider Liquidity 완전 발효/경로 전체 보호" 표현 0 / 자동 후속 0.

---

## §6 Rollback Trigger
| # | trigger | 대응 |
|---|---------|----|
| RT-1 | redaction이 정상 worker 코드/한국어 손상 | §2 D3 — Tier-1 secret 패턴 한정 + T-RED-3 + 기존 test 무영향 |
| RT-2 | redactor 인자 추가가 examples/test 파괴 | optional default → 무파괴(실측 §4) |
| RT-3 | "경로 전체 보호" over-claim 재발 | §3 — 송신 한정 명문(CC-4) |
| RT-4 | RedactionFilter import가 import-linter 위반 | RedactionFilter = SDK 아님(litellm/openai/anthropic/ollama 아님) → 계약 무관 |

---

## §7 Evidence
- E-1: T-RED-1/2 양방향 green (boss/worker 송신 redacted) + T-RED-3 무손상
- E-2: 기존 test_ollama_boss/worker.py 회귀 0(재작성 0, benign fixture)
- E-3: pytest 177+신규 회귀 0 + 커버리지 70%+
- E-4: import-linter green(SDK import 0) + grimp negative control + scan-source 0
- E-5: boss/worker urllib 경로 보존(트랙 B, facade 미경유) 확인

---

## §8 자기진단
| # | 위험 | 처리 |
|---|------|----|
| P-1 | "facade 통합" over-claim | (나) = redaction만, facade 마이그레이션 0(§0.2 #1) |
| P-2 | "boss/worker 경로 전체 보호" over-claim | CC-4 — 송신 한정, 응답/영속 deferred(§3) |
| P-3 | "Provider Liquidity 완전 발효/ADR-009 §2.2 충족" | 미충족 — BossLLM Protocol 추상 유지(§0.2 #2) |
| P-4 | redaction 정상 코드 손상 | §2 D3 + T-RED-3 |
| P-5 | 65 RedactionFilter 변경 유혹 | 협력자 재사용만, 패턴 내용 0 |
| P-6 | 작성자 = Claude single-vendor | 본 (나) = 직전 4 source 합의 추천 옵션(CC-0 §3 (나)) 답습 — 재합의 불요(ceremony 차단), 구현만 |

---

## §9 합의 상태 + 다음 단계
- **합의 = 완료** (직전 풀 3+1 + codex 4 source APPROVE WITH CONDITIONS가 (나)를 명시 추천 — CC-0 §3). (나) = 축소 구현이라 재합의 불요(ceremony-inflation 차단, [[feedback_ceremony_inflation]]). 적용 BLOCKING = CC-4(송신 한정 framing)뿐 — 본 brief §3 흡수.
- 다음: 사용자 TDD 승인 → 구현(T-RED + boss/worker redact) → verify(177 회귀 0) → commit + push. 자동 진입 0.

**본 brief v1.1 끝.**
