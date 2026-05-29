# 3+1 합의 (Reviewer 통합) — boss/worker facade 통합 (트랙 B → facade.complete())

> **날짜**: 2026-05-28 (세션 #4, 70번째 entry 진입 cycle)
> **검토 대상**: `docs/phase0/boss-worker-facade-consolidation-brief.md` (v1)
> **4 source**: Agent A (구현) / Agent B (안전) / Agent C (대안) / codex (gpt-5.5 cross-vendor, `--sandbox danger-full-access`)

---

## 0. 최종 판정 — **APPROVE WITH CONDITIONS (4 source 전원)** + ⚠️ **중대 충돌 1건 (사용자 결정 필요)**

| source | 판정 | BLOCKING | 권고 |
|--------|------|----------|------|
| codex | APPROVE WITH CONDITIONS | 2 | 3 |
| Agent A (구현) | APPROVE WITH CONDITIONS | 3 | 6 |
| Agent B (안전) | APPROVE WITH CONDITIONS | 4 | 5 |
| Agent C (대안) | APPROVE WITH CONDITIONS | 2 | 5 |

**4 source 공통**: 트랙 B 번복은 *정당*(facade real 후 "urllib 단독" 전제 해소 + ADR-009 §2.2 단일 진입점) + BossLLM/Worker Protocol·StubBoss·orchestrator 보존 타당. **단 brief v1의 구현 세부 다수 부정확 + 새 충돌 surface 발견** → BLOCKING 흡수 + ⚠️ **CC-0 충돌은 사용자 결정 선행**.

---

## ⚠️ CC-0 (중대 충돌 — Reviewer verify, 사용자 결정 선행 의무)

**facade `validate_config` "동일 type 2개 active 금지"(R5) ↔ jarvis boss/worker 역할별 *상이* ollama 모델 패턴 — 직접 충돌.**

- **근거** (Reviewer 직접 verify): examples/ 가 `OllamaBoss(model="qwen3-30b...")` (boss=Qwen) + `OllamaWorker(model="glm-4.7-flash...")` (worker=GLM) = **boss/worker에 서로 다른 로컬 ollama 모델**을 사용 (`examples/jarvis_v00_glm_worker.py:74/82` `--worker-model`+`--boss-model` 분리). Agent C 실측 + 본 Reviewer 확인.
- **충돌**: facade.complete()는 registry(`llm-providers.yaml`) routing alias → provider. boss=Qwen + worker=GLM를 facade로 라우팅하려면 ollama-qwen + ollama-glm 2 provider 필요 → 둘 다 type=ollama → **`validate_config` 동일 type 2개 active 금지(R5, `facade.py:85`)로 fail-fast**. 즉 **둘을 동시 active 불가** → boss/worker가 *하나의* ollama 모델 공유 강제 (역할별 모델 분리 능력 상실) OR 하나를 cloud(anthropic)로 (로컬 사장 위배 + 과금).
- **결과**: **(c) 전체 마이그레이션은 boss=Qwen/worker=GLM 분리 패턴을 regress**시킨다. facade의 "Min 2 *다른* type" 복원력 설계 ↔ jarvis "역할별 *같은* type 다중 모델" 패턴 = 설계 가정 불일치.
- **추가 맥락**: `jarvis-mvp1-m3-m4-fixation` 합의(`docs/review/3plus1-consensus-2026-05-26`)는 현 `OllamaBoss(model: str)` arg 주입을 *이미 Provider Liquidity 헌법 5조-2 정합(M3-F, 교체 가능성 충족)*으로 판정. 즉 boss/worker는 *이미* (다른 방식으로) Liquidity-compliant — (c)의 "Liquidity gap" 동인이 약함.

→ **남는 진짜 동인 = RT-1 redaction(보안)** + ADR-009 §2.2 facade 단일 진입점(형식). 모델 분리 regress 비용과 견줘 사용자 결정 필요 (§3).

---

## 1. 통합 BLOCKING (brief v1.1 흡수 — CC-0 결정 후)

| ID | finding | source | 흡수 정정 |
|----|---------|--------|----------|
| **CC-1** ⭐ | T-RT1 test 경계 오류 — brief는 "fake facade가 받은 LLMRequest에 secret 부재" 요구하나 redaction은 facade *내부*(`_redact_request` → Router 전, `facade.py:193/196`)에서 발생. boss/worker는 raw LLMRequest를 facade에 전달 → fake facade는 raw 받음 | codex(B1) + A/B 정합 | boss/worker unit test = **fake facade 주입(canned response)**, redaction 재검증 안 함(facade 책임, 69 T-A 기검증). RT-1 보안 입증 = **1 integration test**(boss→real facade+FakeRouter→Router가 redacted 수신) |
| **CC-2** ⭐⭐⭐ | 미등록 model_alias → `_resolve` silent fallback to `routing.default`=**anthropic(cloud!)** (`facade.py:148/154`, `llm-providers.yaml:16/17`) — KeyError 아님. brief RT-3 "fallback=대응"은 *위험* | codex(B2) + A(B2) + B(B4) — 3 source HIGH | `jarvis_boss`/`jarvis_worker` routing alias를 **ollama-llama-local로 명시 등록** + test 고정. fallback을 안전장치로 서술 금지 |
| **CC-3** ⭐⭐ | brief "src instantiation 0" → **examples/ 6 파일이 OllamaBoss/Worker instantiate**(`glm_worker.py:74/82` 등). CI 미포함 → test green이어도 silent 파괴 | Agent C(B-C1), codex NOTE 부분 | D1(생성자 변경) 시 examples **동반 수정 OR backward-compat 생성자** OR carry-over 명문. "verify green ≠ examples 정확" |
| **CC-4** ⭐⭐ (over-claim) | RT-1 = **송신 경로 한정**. boss summary→`memory.py:53` JSONL 평문 영속 + worker 응답→파일 작성(`worker.py:308/341`). 응답 redaction deferred(69 CB-6) → "boss/worker 경로 확장" over-claim | Agent B(B-1) + codex(권고3) | brief §3 정직 축소 — "**송신(request body) redaction만**; 응답/영속(memory JSONL/파일) = deferred" known limitation |
| **CC-5** ⭐ | facade 정의 예외 = `ConfigError`+`DegradedError`뿐. `AuthenticationError` = name-string 감지 후 re-raise(`facade.py:209`). D3 "종류별 catch" 불가 | Agent A(B1) | D3 = **catch-all `except Exception`** → boss RuntimeError(R3) / worker WorkerResult(is_error) |
| **CC-6** | SSRF posture 변동 — 현 `boss.py:98` 코드 하드코딩 localhost(생성자 url 0) → facade `api_base=yaml endpoint`(config 신뢰 이전). brief D6 "여전히 localhost 고정" 부정확(yaml 값) | Agent B(B-2) | 정직 표기 — SSRF 신뢰가 registry yaml로 이전(여전히 yaml=localhost이나 코드 불변식 아님) |
| **CC-7** | D5 registry — 신규 active ollama provider 추가 시 동일 type fail-fast(CC-0 동형). routing alias만(기존 ollama-llama-local 재사용) | Agent B(B-3) + Agent C(R-C2) | routing alias만, 신규 active provider 0 |
| **CC-8** | RT-2 `asyncio.new_event_loop` fallback = nested loop 미해소(미정의 동작). 정상 경로 nested 0(orchestrator sync 실측) | Agent C(B-C2) + codex(권고1) + A | fallback 삭제 + "sync-only; async caller=RuntimeError unsupported/fail-loud" 명문 |

---

## 2. 통합 권고

| # | 권고 | source |
|---|------|--------|
| R-1 | **D4 rename(OllamaBoss→provider-neutral) = DEFER** (별도 cycle/alias class). 현 명칭은 routing 분기 아님 → 위반패턴 #1 본문 위반 아님. rename = examples+test+wiring 영향 큼 | A + C(R-C1) + codex(권고2) — 수렴 |
| R-2 | D2 sync(asyncio.run) 채택 적정 — orchestrator 전체 sync 실측(`src/jarvis` async 0). `test_facade_router` asyncio.run 패턴 답습 | A + C + codex |
| R-3 | 회귀 기준 = **177**(전체), jarvis 144 아님. boss/worker test 재작성 후 재계산 | Agent A(B-3) |
| R-4 | model_alias 강제 시 boss/worker별 상이 로컬 모델 능력 상실(CC-0) — 별도 cycle 또는 per-role alias(단 동일 type 충돌) | Agent C(R-C3) |
| R-5 | LiteLLM 유지(ADR-009 §3 v2.0 트리거 0) | Agent C |

---

## 3. CC-0 사용자 결정 (선행 의무)

(c) 전체 마이그레이션이 boss=Qwen/worker=GLM 분리를 regress시키므로, 사용자 결정 필요:
- **(가)** (c) 진행 — boss/worker가 **하나의 ollama 모델 공유** 수용(역할별 모델 분리 포기) + CC-1~8 흡수. facade 단일 진입점 + RT-1 확보, 모델 분리 상실.
- **(나)** **축소: RT-1(redaction)만** — facade 전체 마이그레이션 대신 boss/worker urllib 경로에 `RedactionFilter`만 적용(송신 secret strip). 보안 gap 해소 + 모델 분리 보존 + examples 무파괴. 단 ADR-009 §2.2 facade 단일 진입점은 미충족(BossLLM Protocol 추상은 유지).
- **(다)** **보류** — boss/worker는 이미 m3-m4 합의로 Liquidity-compliant 판정 + facade와 설계 가정 불일치(동일 type) → (c) 접고 다른 작업.

---

## 4. 명칭/트랙 B 번복 독립 판단 (4 source)
- 트랙 B 번복 = **정당**(4 source) — 단 대상은 "OllamaBoss/Worker 내부 provider 직결"만, Protocol/Stub/orchestrator 보존(SDD 견고). codex: "통합 > 공존 우월(BossLLM=판단추상, LLMFacade=호출추상, 계층 정합)".
- 단 CC-0(모델 분리 regress) + CC-3(examples) 때문에 *전체 마이그레이션*의 순이익이 brief 가정보다 작음 — §3 사용자 결정.
- over-claim: brief의 "Provider Liquidity 완전 발효" 회피·2경로 한정 framing은 양호. 단 CC-4(RT-1 송신 한정) + CC-6(SSRF) framing 정정 필요.

---

## 5. 합의 결론
**APPROVE WITH CONDITIONS (4 source 전원)** — 트랙 B 번복 방향 정당하나, brief v1은 (1) CC-0 모델 분리 regress 충돌 미인지 (2) CC-1 test 경계 오류 (3) CC-2 silent cloud fallback (4) CC-3 examples 파괴 (5) CC-4 RT-1 송신 한정 over-claim 등 다수 정정 필요. **CC-0 = 사용자 결정 선행**(가/나/다) → 결정 후 brief v1.1 흡수 → TDD. over-claim catch: CC-4(RT-1 송신 한정) — 본 세션 #4 두 번째(누적 8회).
