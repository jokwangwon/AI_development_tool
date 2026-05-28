# 3+1 합의 통합 보고서 — GP-2 송신 redaction PASS 발효 (60 entry)

> **작성**: 2026-05-28 (Reviewer 통합)
>
> **대상**: `docs/phase0/mvp2-gp2-pass-activation-brief.md` (v1)
>
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) — 4 source
>
> **입력**: Agent A (구현 분석가, filesystem+CI direct) + Agent B (품질/안전성) + Agent C (대안 탐색) + codex (cross-vendor blind) — 3 Agent 병렬 독립 + codex 독립

---

## §1 4 source verdict 요약

| source | verdict | BLOCKING | 핵심 |
|--------|---------|---------|------|
| Agent A (구현 분석가) | **APPROVE** | 0 | evidence 전원 실증 (over-claim 0). (d) 격상 정당 (D-2 step 43c51ef 이래 존재 + run `26517803107` success + 코드 불변), R-4 29KB, fixtures 실행 일치, R-1 부재/R-2 placeholder/R-5 known limitation, pytest 152 |
| Agent B (품질/안전성) | **APPROVE WITH CONDITIONS** | 1 (R-B-1) | "59 Layer 2a DEFER 동형" framing 비대칭 — 59 = in-repo 2 layer 이중 cover, GP-2 = in-repo 능동 보증 0 (Hermes upstream 단독). PASS 정당(§2.3 #2 위임)하나 보안 결과 over-claim |
| Agent C (대안 탐색) | **APPROVE WITH CONDITIONS** | 1 (R-C-1) | (a) ✅ 논리 모순 — (a) 모법 + R-4 = prevention 동등성 입증인데 prevention deferred. §2 → 3축 분리 (설계 동등성/detection operative/prevention upstream 위임). 발효 형태 (c) detection PASS = 4 대안 中 dominant |
| codex (cross-vendor) | **REVISE** | 1 | "GP-2 PASS" + "(a) ✅" over-claim. (d) 정당하나 (a) = governance §4 Hermes/facade 검증 (deferred). R-3 detection green 으로 "4/4 close" = prevention 부재를 detection 으로 대체. → "GP-2 detection-layer PASS" 명시 강등 |

→ **Reviewer 통합 verdict = REVISE** (codex REVISE 최강 + Agent B/C 정렬 + Agent A APPROVE). **핵심 3-way consensus (codex + Agent B + Agent C)**: brief 가 "GP-2 (full) 송신 redaction PASS" + "(a) 동등 이상 보안 결과 ✅" 를 **over-claim** — 실제는 **"GP-2 detection-layer PASS"** (R-3/D-2 자동 회귀 검증 operative, prevention R-1/R-2 = Hermes upstream deferred, in-repo 능동 redaction 0). **evidence 자체는 실증 (over-claim 0) — framing 만 over-claim** → **brief v1.1 1pass 흡수 (detection-layer 강등 reframe) 후 GP-2 detection-layer PASS 발효**.

---

## §2 cross-validation 매트릭스

### §2.1 핵심 BLOCKING (3-way consensus — framing over-claim)

| # | BLOCKING | source | 근거 (Reviewer verify) | 정정 |
|---|----------|--------|---------------------|------|
| **B-1** ⭐⭐⭐ (3-way) | **"GP-2 (full) PASS" + "(a) ✅" over-claim → "GP-2 detection-layer PASS" 강등** | codex + Agent C R-C-1 + Agent B R-B-1 | governance-preconditions §4 (a) = "Hermes native redaction Tier-1 catalog 적용 검증 + P1 facade redaction filter 검증" (line 451) = **prevention (R-1/R-2) 검증**. 현 상태 = `agent/redact.py` 부재 + facade placeholder + redaction-pattern-equivalence.md = 설계 동등성 문서 (line 33 Hermes safety 선언 *금지* 명시). R-3 detection green 으로 "(a) ✅ / 4/4 close" = **prevention 부재를 detection 으로 대체**. (β B-1 / 59 B-2 framing over-claim 동형 재발) | **(1)** title/scope/발효 효과 → "**GP-2 detection-layer PASS** (R-3/D-2 자동 회귀 검증)". **(2)** §2 evidence 3축 분리 (Agent C): (a) → 설계 동등성 ⚠️ partial (prevention 입증 아님) / (b)(d) detection operative ✅ / prevention = Hermes upstream 위임 (본 repo 입증 0). **(3)** full GP-2 PASS = R-1 Hermes runtime redaction 검증 + R-2 facade real 선행 조건 (deferred trajectory) |
| **B-2** ⭐ | **"59 Layer 2a DEFER 동형" framing 비대칭** | Agent B R-B-1 | 59 = DEFER ends (history rewrite) 가 in-repo 2 operative layer (2b branch protection + rewrite-defense CI) 이중 cover. GP-2 = DEFER prevention (능동 redaction) ends 를 in-repo cover layer **0** (Hermes upstream repo 외부 단독). 57 (β) line 135 = "MVP-2 PASS 시점 GP-2 (a)~(e) = detection + prevention 합산" → 본 brief detection-only carve-out | "59 동형" → "**부분 동형 (의사결정 형식만, cover 구조 비대칭)**" 강등 + "**in-repo 능동 redaction 보증 0, Hermes upstream 위임**" 정직 명문 |

### §2.2 권고 (non-blocking)

| # | 권고 | source | v1.1 흡수 |
|---|------|--------|---------|
| N-1 | "(e2)" = 59 B-2 도입 프로젝트 내부 label (ADR 본문 문자열 아님) 출처 1줄 | Agent B | §4 1줄 |
| N-2 | r4-1-trigger-extension-evidence.md 경로 = `docs/phase0/` (architecture 아님) | Agent A | §0.3 + §9 정정 |
| N-3 | 51 "(b) 부분" → "✅" 격상 근거 명시 (secret-hygiene D-2 PoC) | Agent A | §2 (b) 근거 |
| N-4 | C-1 prevention deferred 명문 발효 문구 유지 + workflow_dispatch 미지원 한계 | Agent A + codex | §6 (C-1) 유지 |

### §2.3 4 source 정합 확인 (evidence 실증 — over-claim 0, framing 만)

- ✅ **evidence 전원 실증** (4 source direct verify): (d) D-2 step 실재 (43c51ef 이래) + actual run `26517803107` success/`4fec6485` + 코드 49 entry(`4fec648`) 이후 불변 (git log 0) → (d) 격상 = **over-claim 아님** (codex/A/B/C 일치)
- ✅ R-4 `redaction-pattern-equivalence.md` 실재 (29KB, 3-way 동등성) — 단 설계 문서 (Hermes safety 선언 아님, B-1)
- ✅ fixtures 실행: redaction_pass rc=0 violations=0 / redaction_fail rc=1 violations=3 (partial_redact leak)
- ✅ R-1 `agent/redact.py` 부재 / R-2 facade placeholder (NotImplementedError) / R-5 base64_evasion known limitation 실측
- ✅ pytest tests/tools + tests/jarvis 152 pass
- ✅ (e2) framing = ADR-011 §2.1 (a)~(d) + ADR-012 §4 확장 (59 B-2 정합, 권위 전도 0)
- ✅ R-5 base64 known limitation 정당 (G3-4 MVP-2/3 분리)
- ✅ scope 침입 0 (MVP-2 PASS / R-1 import / R-2 facade / R-5 / R-S1 / workflow 본문 0)
- ✅ 발효 형태 (detection PASS + prevention deferred) = 32/59 일관 (Agent C 4 대안 dominant)

---

## §3 v1.1 흡수 매트릭스 (BLOCKING 2 + 권고 4 1pass — detection-layer reframe)

| # | 흡수 | 정정 |
|---|------|------|
| B-1 | title/scope/발효 효과 → "GP-2 detection-layer PASS" + §2 3축 분리 ((a) 설계 동등성 ⚠️ / (b)(d) detection ✅ / prevention upstream 위임 입증 0) + full GP-2 PASS = R-1/R-2 선행 |
| B-2 | §3 "59 동형" → "부분 동형 (cover 비대칭)" + "in-repo 능동 redaction 보증 0" 명문 |
| N-1 | §4 "(e2)" label 출처 (59 B-2) |
| N-2 | §0.3 + §9 r4-1 경로 docs/phase0/ |
| N-3 | §2 (b) secret-hygiene D-2 PoC 격상 근거 |
| N-4 | §6 (C-1) prevention deferred + workflow_dispatch 한계 유지 |

---

## §4 메타 자기진단 (Reviewer)

| # | 위험 | 처리 |
|---|------|----|
| M-1 | 3 Agent 병렬 독립 + cross-vendor | A/B/C 미참조 + codex (OpenAI) blind (헌법 5조-2) |
| M-2 | framing over-claim 반복 (β B-1, 59 B-2, 본 B-1) | **process 가치 입증** — 4 source 가 또다시 framing over-claim 포착. evidence 실증이나 "PASS" scope 과장 → detection-layer 강등 |
| M-3 | REVISE → REJECT 회피 | evidence 실증 + 발효 형태 정당 (detection-layer) → reframe 후 발효 정당 (REJECT 아님, codex/A/B/C 모두 발효 가능 판정) |
| M-4 | detection-layer PASS = "빈 껍데기" risk | §2.1 B-1 정정 = prevention upstream 위임 명문 (ADR-011 §2.3 #2 권위) + full GP-2 PASS 선행 조건 분리 |
| M-5 | ceremony-inflation (v2 cycle) | 1pass 흡수 (52/57/59 동형) |
| M-6 | **MVP-2 PASS 영향** (GP-2 = detection-layer 만) | ⭐ MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 **detection-layer** PASS + R-S1 → full GP-2 PASS (prevention R-1/R-2) 는 MVP-2 PASS 의 잔여 trajectory (별도 cycle, 사용자 명시). 본 합의 = 이 사실 명문화 |

---

**본 합의 verdict = REVISE (3-way framing over-claim) → brief v1.1 1pass 흡수 (BLOCKING 2 + 권고 4, detection-layer reframe) → GP-2 detection-layer PASS 발효**.

**발효 효과**: GP-2 **detection-layer** PASS (R-3/D-2 자동 회귀 검증 operative green + R-4 설계 동등성 + ADR 권위). **prevention (R-1 Hermes runtime redaction + R-2 facade real) = in-repo 입증 0, Hermes upstream 위임 (ADR-011 §2.3 #2) — full GP-2 PASS 의 잔여 trajectory (deferred)**. ⭐ **MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 detection-layer PASS + R-S1 hard gate → full GP-2 PASS (prevention) 는 MVP-2 PASS 후속 또는 선행 trajectory (별도 cycle, 사용자 명시)**.

**본 합의 발효 = brief v1.1 commit + SESSION + INDEX commit + push 후** (단계별 합의 cycle 답습).
