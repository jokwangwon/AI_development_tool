# GP-2 detection-layer PASS 발효 합의 entry brief (v1.1)

> **작성**: 2026-05-28 (60번째 entry 진입 cycle — 신규 세션 #2)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-gp2-pass-activation.md`) **REVISE (3-way framing over-claim) → BLOCKING 2 + 권고 4 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: "GP-2 (full) 송신 redaction PASS" + "(a) ✅" = over-claim → **"GP-2 detection-layer PASS"** 강등. (a) 동등 이상 보안 결과 = governance §4 상 R-1/R-2 prevention 검증인데 deferred (redaction-pattern-equivalence = 설계 동등성 문서, Hermes safety 선언 아님). evidence 자체는 실증 (over-claim 0, β B-1 / 59 B-2 framing 동형). §11 흡수 매트릭스 추가.
>
> **scope**: G2 GP-2 **detection-layer** PASS **발효 (e2)** — R-3/D-2 자동 회귀 검증 operative. **full GP-2 PASS (prevention R-1/R-2) = 잔여 trajectory (deferred)**
>
> **본 cycle = 큰 cycle** (PASS *발효* milestone, 풀 3+1 + 외부 LLM 1+ 의무, 59 Layer 통합 PASS 발효 + 32 MVP-1 PASS 발효 답습 동형)
>
> **본 cycle 발효 자격** = (b)(d) detection evidence + (a) 설계 동등성 + (e2) 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
>
> **본 cycle 발효 효과** = **GP-2 detection-layer PASS 발효** (R-3/D-2 회귀 검증 + R-4 설계 동등성 + ADR 권위). prevention (R-1 Hermes runtime / R-2 facade real) = in-repo 입증 0, Hermes upstream 위임 (ADR-011 §2.3 #2). MVP-2 Implementation Evidence PASS = Layer 통합 PASS (59 ✅) + GP-2 detection-layer PASS (본 cycle) + R-S1 hard gate → **full GP-2 PASS (prevention) = MVP-2 PASS 잔여 trajectory (별도 cycle)**
>
> **선행 답습**: 51 audit (GP-2 Exit 5조건, R-1~R-5 후보) + 57 ((β) R-4 = R-3 detection 우선 + R-1/R-2 prevention deferred) + 59 (Layer 통합 PASS 발효, means-vs-ends + DEFER 패턴 답습)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **GP-2 Exit 5조건 evidence 매트릭스** ((a)~(d) + (e2)) — 51 audit §2.2 현행화 (§2)
2. **R-3 detection (operative) + R-1/R-2 prevention (deferred trajectory) 분리** (57 (β) + 59 Layer 2a DEFER 패턴 답습) (§3)
3. **ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 매핑** (59 B-2 정정 framing 답습) (§4)
4. **R-5 base64 evasion = known limitation 명문** (R-5 영구 분리) (§4)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ + 승격 트리거** (§5)
6. **GP-2 PASS 발효 권고 + 조건** (§6)
7. 금지 / 다음 단계 / cross-ref / 자기진단 (§7~§10)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | GP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0 |
| 3 | **R-1 Hermes import 결정** (prevention 구현 경로, 별도 cycle) | 0 |
| 4 | **R-2 facade real (TR-1)** (prevention 구현 경로, 별도 trajectory) | 0 |
| 5 | R-5 base64/URL-encoded/압축 evasion 영역 진입 (MVP-2/3 분리, G3-4) | 0 |
| 6 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
| 7 | R-S1 cross-reference 정정 (MVP-2 PASS 전 hard gate, 별도 cycle) | 0 |
| 8 | Layer 통합 PASS 재선언 (59 답습 유지) / MVP-1 PASS 재선언 (32 답습) | 0 |
| 9 | ADR / 헌법 / roadmap / governance / ADR-008/011/012 본문 갱신 | 0 |
| 10 | secret_scanner.py / secret-hygiene-egress-redaction.yml 본문 변경 | 0 (PoC 시제 보존) |
| 11 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1) | 0 (사용자 명시 의무) |
| 12 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법** (line 52~61) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **ADR-011 §2.3 운영 함의 #2** (Hermes redaction = 로그/LLM 송신 방어 신뢰, 저장 경로 책임 0) — 동상 line 112
- **ADR-012 §4 (a)~(d) + (e) 5조건 답습 확장** (PASS 발효 (e2) 권위) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **governance-preconditions.md §4** (GP-2 Egress Redaction Entry/Exit) — `docs/architecture/governance-preconditions.md`
- **`docs/architecture/redaction-pattern-equivalence.md`** (R-4, (a) 설계 동등성) + **`docs/phase0/r4-1-trigger-extension-evidence.md`** (R-4.1, (b) PoC — N-2 경로 정정: phase0, architecture 아님)
- **51 audit §2** (GP-2 Exit 5조건) — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **57 (β) brief v1.1** (R-4 = R-3 detection + R-1/R-2 prevention deferred) — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
- **59 Layer 통합 PASS 발효 brief v1.1 + 합의** (means-vs-ends + DEFER + B-2 framing 답습) — `docs/phase0/mvp2-layer-124-pass-activation-brief.md`
- **본 cycle audit (read-only, 2026-05-28)** — secret-hygiene CI + fixtures + secret_scanner filesystem direct

---

## §1 진입 컨텍스트

### §1.1 선행 chain

| 합의/구현 | 본 cycle 답습 |
|----------|-----------|
| 59 Layer 1+2+4 통합 PASS 발효 (`0f49eb9`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = Layer 통합 PASS ✅ + **GP-2 PASS (본 cycle)** + R-S1. means-vs-ends + DEFER 패턴 + B-2 (a)~(d)/(e2) framing 답습 |
| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred trajectory). R-5 영구 분리 |
| 51 audit §2 (`f7ac61d`) | GP-2 Exit 5조건 — 본 cycle 현행화 (51 audit "(d) gap" = 부정확, secret-hygiene D-2 이미 운영) |

### §1.2 GP-2 = 송신 redaction 영역 정의 (governance §4)

- Hermes / Worker Agent 가 stdout/stderr/log file/LLM API request body 에 secret 노출 차단 (송신/로그 경로 한정).
- ADR-011 §2.3 #2: "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 차단 책임 0" (DB INSERT = GP-1 책임).
- 본 repo = DESIGN/governance repo (docs + tools + CI). 실 runtime redaction = Hermes upstream (R-1). 본 repo GP-2 PASS = redaction 패턴 정의 (R-4) + CI 회귀 검출 (R-3) + 설계 권위 (ADR-011 §2.3).

---

## §2 Evidence 매트릭스 (GP-2 Exit 5조건, 51 audit §2.2 현행화)

⭐ **B-1 정정**: GP-2 Exit 조건을 **3축 분리** (detection-layer PASS scope 명확화) — (a) 설계 동등성 ≠ prevention 입증, prevention 능동 redaction 은 in-repo 입증 0 (Hermes upstream 위임).

**축 1 — detection-layer (본 cycle PASS scope, operative ✅)**:

| # | 조건 | 상태 | evidence |
|---|------|------|---------|
| (b) | 격리 환경 PoC 실증 (detection) | ✅ | secret-hygiene D-2 scan-log redaction PoC (`redaction_pass/env_redacted.txt` rc=0 잔존 0 + `redaction_fail/partial_redact.txt` rc=1 leak 검출) + `r4-1-trigger-extension-evidence.md` (R-4.1 PoC) — N-3: 51 "(b) 부분" → ✅ 격상 근거 = secret-hygiene D-2 송신 redaction residual CI |
| (d) | 자동 회귀 검증 경로 (detection) | ✅ ⭐ | **`secret-hygiene-egress-redaction.yml` D-2 step (scan-log redaction residual, `secret_scanner.py --mode scan-log`) — 51 audit "❌ gap" 부정확 정정 (52 entry PoC 시제 발견 동형). actual run `26517803107` success (headSha `4fec6485`). secret-hygiene = `workflow_dispatch` 미지원 (schedule cron `0 3 * * *` 만) — secret_scanner.py + workflow + redaction fixtures = 49 entry (`4fec6485`) 이후 변경 0 (불변) → 유효 evidence** |
| (c) | ADR/SDD 권위 명시 | ✅ | ADR-011 §2.3 #2 (송신 방어 신뢰, 저장 경로 책임 0) + governance §4 (GP-2 정의) |

**축 2 — 설계 동등성 (⚠️ partial, prevention 입증 아님)**:

| # | 조건 | 상태 | evidence |
|---|------|------|---------|
| (a) | 동등 이상 보안 결과 | ⚠️ **partial (설계 동등성 한정)** | `redaction-pattern-equivalence.md` (R-4 — Tier-1 42 catalog 패턴 *동등성 문서*). ⚠️ **B-1**: governance §4 (a) (line 451) = "Hermes native redaction 적용 검증 + facade redaction filter 검증" = **prevention (R-1/R-2) 검증** — 현 상태 R-1 부재 + R-2 placeholder. redaction-pattern-equivalence = 설계 비교 문서 (line 33 Hermes safety 선언 *금지*), prevention *입증* 아님. → (a) full 충족 = R-1/R-2 prevention 선행 (deferred) |

**축 3 — prevention (능동 redaction, in-repo 입증 0 = Hermes upstream 위임)**:

| 수단 | 상태 | 위임 |
|------|------|----|
| R-1 Hermes native redaction | ❌ 본 repo 부재 | Hermes upstream runtime operative (ADR-011 §2.3 #2 위임 권위), import 결정 별도 cycle |
| R-2 facade RedactionFilter | ⚠️ placeholder | facade real (TR-1) deferred trajectory |

→ **detection-layer PASS = (b)(d)(c) ✅ operative + (a) 설계 동등성 partial. prevention (R-1/R-2) = in-repo 입증 0 (upstream 위임)**. (e2) = 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시. **full GP-2 PASS = detection-layer + prevention (R-1/R-2) 선행 (별도 trajectory)**.

---

## §3 R-3 detection (operative) + R-1/R-2 prevention (deferred) 분리 (57 (β) + 59 Layer 2a 답습)

### §3.1 수단별 상태 (R-4 defense-in-depth)

| 수단 | 역할 | 본 repo 상태 | PASS 영향 |
|------|----|-----------|---------|
| **R-3** log canary CI (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | **detection (회귀 검증)** | ✅ operative green | GP-2 (d) 자동 회귀 충족 — in-repo operative means |
| **R-1** Hermes native redaction (`agent/redact.py`) | **prevention (능동 redaction)** | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | runtime prevention = Hermes upstream operative (import 결정 별도 cycle). ADR-011 §2.3 #2 송신 방어 신뢰 |
| **R-2** facade RedactionFilter | prevention (LLM API 진입점) | ⚠️ facade placeholder | facade real (TR-1) 시점 추가 layer (deferred trajectory) |
| **R-5** base64/URL/압축 evasion | (out of scope) | ❌ known limitation (`base64_evasion.txt` fixture) | 영구 분리 (MVP-2/3, G3-4) |

### §3.2 means-vs-ends 정합 (59 Layer 2a DEFER **부분 동형** — B-2 정정)

- **ends** = secret 송신/로그 leak 0.
- **detection ends** = R-3 (secret-hygiene D-2 CI) ✅ operative green — 송신/로그에 secret 잔존 시 BLOCK (회귀 검증). **본 repo in-repo operative**.
- **prevention ends** = R-1 (Hermes upstream native redaction, 실 runtime operative — 본 repo DESIGN repo 이므로 import 미결정) + R-2 (facade real deferred). **본 repo in-repo 능동 redaction 보증 0**.
- ⚠️ **B-2 — 59 Layer 2a 와 *부분 동형* (의사결정 형식만, cover 구조 비대칭)**: 59 = DEFER ends (history rewrite 차단) 가 **in-repo 2 operative layer** (2b branch protection + rewrite-defense CI) 이중 cover. GP-2 = DEFER prevention (능동 redaction) ends 를 cover 하는 **in-repo layer 0** — Hermes upstream (repo 외부) 단독 위임 (ADR-011 §2.3 #2). 즉 보안 cover 구조 비대칭, "완전 동형" 표현 회피.

→ **GP-2 detection-layer PASS = detection (R-3 in-repo operative) + 설계 권위 + 패턴 동등성 (설계 한정). prevention 능동 redaction = in-repo 보증 0, Hermes upstream 위임 (R-1) + facade real (R-2) deferred trajectory = full GP-2 PASS 선행** (57 (β) 결정 답습, 59 DEFER *부분* 동형).

---

## §4 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 (59 B-2 framing 답습)

> ⚠️ 59 B-2 답습: ADR-011 §2.1 = (a)~(d) 4조건 모법, "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d)+(e) 5조건 답습" 확장. **N-1**: "(e2)" = 59 B-2 도입 *프로젝트 내부 label* ((e2) PASS 발효 / (e1) 진입 권한 분리), ADR 본문 문자열 아님.

| 조건 | 출처 | GP-2 detection-layer 충족 |
|------|------|---------|
| (a) 동등 이상 보안 결과 | ADR-011 §2.1 | ⚠️ **partial (설계 동등성 한정)** — R-4 패턴 동등성 문서. full = R-1/R-2 prevention 검증 선행 (B-1) |
| (b) 격리 PoC (detection) | ADR-011 §2.1 | ✅ secret-hygiene D-2 + r4-1 PoC |
| (c) ADR/SDD 권위 | ADR-011 §2.1 | ✅ ADR-011 §2.3 #2 + governance §4 |
| (d) 자동 회귀 검증 (detection) | ADR-011 §2.1 | ✅ secret-hygiene D-2 CI green |
| (e2) 합의 APPROVE | ADR-012 §4 확장 (내부 label) | ⏳ 본 cycle |

→ **detection-layer PASS = (b)(c)(d) ✅ + (a) partial. full GP-2 PASS = (a) prevention (R-1/R-2) 선행**.

### §4.1 R-5 base64 evasion = known limitation (영구 분리)

`tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt` 존재 — secret-hygiene D-2 가 base64 evasion 미검출 (known limitation 명문, workflow line 13). R-5 = MVP-2/3 분리 (G3-4), GP-2 PASS scope 외. GP-2 PASS = Tier-1 42 catalog 평문 redaction 한정 (base64 evasion 제외 명문).

---

## §5 합의 형태 + 풀 3+1 승격 트리거

### §5.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: PASS *발효* milestone (59 Layer PASS + 32 MVP-1 PASS 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + MVP-2 PASS 직전 단계.

### §5.2 7 승격 트리거

| # | trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 큰 결정 (PASS 발효 milestone) | ✅ | GP-2 PASS 발효 = MVP-2 PASS 절반 |
| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1 |
| 3 | ADR 본문 변경 | ❌ | 0 |
| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (MVP-2 PASS 전 hard gate, 본 cycle 비차단) |
| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 |
| 6 | Tier-2/3 catalog 확장 | ❌ | 0 |
| 7 | Hermes PMO 격상 | ❌ | 0 |

→ **2/7 발화 + 1 부분 → 풀 3+1 + 외부 LLM 1+ 적격**.

---

## §6 GP-2 PASS 발효 권고 + 조건

⭐ **권고 = GP-2 detection-layer PASS 발효 APPROVE WITH CONDITIONS** (B-1: "full GP-2 PASS" 아닌 detection-layer 강등):

1. **detection-layer (b)(c)(d) ✅ operative + (a) 설계 동등성 partial** — secret-hygiene D-2 PoC + ADR 권위 + R-3 CI 회귀 green + R-4 패턴 동등성 (설계 한정). (e2) = 본 cycle.
2. **조건**:
   - (C-1) **R-1 (Hermes runtime redaction 검증) / R-2 (facade real) = prevention 잔여 trajectory 명문 — full GP-2 PASS 선행** (detection-layer PASS = in-repo 능동 redaction 0, Hermes upstream 위임 ADR-011 §2.3 #2, B-1/B-2)
   - (C-2) **R-5 base64 evasion = known limitation 명문** (Tier-1 42 평문 한정)
   - (C-3) secret-hygiene D-2 actual run = `26517803107` green (`4fec6485`) + 코드 불변 (49 entry 이후 변경 0) = 유효 evidence. workflow_dispatch 미지원 → fresh run = schedule/path 변경 시 (비차단)
3. **R-S1 = GP-2 detection-layer PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle).

→ **GP-2 detection-layer PASS 발효 자격 = (b)(c)(d) detection 충족 + (a) 설계 동등성 + (e2) 합의 APPROVE + 사용자 명시 + (C-1) prevention 잔여 trajectory 명문**. **full GP-2 PASS = + R-1/R-2 prevention 검증 (별도 trajectory)**.

---

## §7 금지 사항

§0.2 답습 (12). 추가: MVP-2 PASS 자동 선언 0 / R-1 Hermes import 결정 0 / R-2 facade real 0 / R-5 evasion 진입 0 / R-S1 자동 정정 0 / 자동 후속 0.

---

## §8 다음 단계 (사용자 명시 의무 — 자동 진입 0)

1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → **GP-2 detection-layer PASS 발효**
2. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS ✅ + GP-2 **detection-layer** PASS ✅ + R-S1 hard gate 후, 32 답습) — ⚠️ **full GP-2 PASS (prevention R-1/R-2) = MVP-2 PASS 잔여 trajectory** (MVP-2 PASS 도 prevention deferred scope 명문 또는 prevention 선행 — MVP-2 PASS cycle 에서 결정)
3. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
4. **full GP-2 PASS trajectory** — R-1 Hermes runtime redaction 검증 (import) / R-2 facade real (TR-1) prevention (별도 cycle)

---

## §9 cross-reference 답습

- ADR-011 §2.1 (a)~(d) 모법 + §2.3 #2 (송신 방어 신뢰) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- ADR-012 §4 (e 확장) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- governance-preconditions.md §4 (GP-2)
- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
- 51 audit §2 + 57 (β) brief v1.1 + 59 Layer PASS brief v1.1 + 합의
- 실 evidence: `secret-hygiene-egress-redaction.yml` (D-2) + `tools/secret_scanner.py` (--mode scan-log) + `tests/fixtures/secret_hygiene/{redaction_pass,redaction_fail}/`

---

## §10 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | GP-2 PASS *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §8) |
| P-2 | R-3 detection 만으로 GP-2 PASS *단순화* (prevention R-1/R-2 부재 은폐) | §3 detection/prevention 분리 명시 + (C-1) deferred 명문 (59 Layer 2a DEFER 답습, β B-1 cascade 교훈) |
| P-3 | 51 audit "(d) gap" → 본 brief "(d) ✅" 격상 over-claim risk | §2 (d) = secret-hygiene D-2 CI green actual run 근거 (filesystem + run direct verify), 52 entry PoC 시제 발견 동형 (gap 표기 부정확 정정) |
| P-4 | DESIGN repo GP-2 PASS vs runtime redaction 혼동 | §1.2 + §3.2 = 본 repo = 설계/CI, 실 runtime redaction = Hermes upstream (R-1) 명시 |
| P-5 | R-5 base64 known limitation 과소 | §4.1 명문 (base64_evasion.txt fixture + workflow line 13) |
| P-6 | 본 brief 작성자 = 57/59 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (59 동형 — over-claim 0 입증) |
| P-7 | 권위 인용 (ADR-011 §2.1 (a)~(e)) 전도 (59 B-2 재발) | §4 = "(a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장" framing 답습 |

---

---

## §11 v1.1 흡수 매트릭스 (BLOCKING 2 + 권고 4 1pass — detection-layer reframe)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-gp2-pass-activation.md` 답습 1pass 흡수 (별도 v2 cycle 0, 52/57/59 동형). **4 source: Agent A APPROVE + Agent B/C APPROVE WITH CONDITIONS + codex REVISE → REVISE (3-way framing over-claim)**. evidence 실증 (over-claim 0), framing 만 over-claim.

| # | 흡수 | source | 정정 |
|---|------|--------|------|
| B-1 ⭐ (3-way) | "GP-2 (full) PASS" + "(a) ✅" over-claim → **GP-2 detection-layer PASS** 강등 + §2 3축 분리 ((a) 설계 동등성 ⚠️ / (b)(d) detection ✅ / prevention upstream 위임 입증 0) + full GP-2 PASS = R-1/R-2 선행 | codex + Agent C + Agent B | title + §2 + §4 + §6 + 발효 효과 |
| B-2 | "59 동형" → "부분 동형 (cover 비대칭, in-repo 능동 redaction 보증 0)" | Agent B R-B-1 | §3.2 |
| N-1 | "(e2)" = 59 B-2 도입 내부 label | Agent B | §4 |
| N-2 | r4-1 경로 = docs/phase0/ | Agent A | §0.3 |
| N-3 | 51 "(b) 부분" → ✅ 격상 근거 (secret-hygiene D-2) | Agent A | §2 (b) |
| N-4 | C-1 prevention deferred + workflow_dispatch 한계 유지 | Agent A + codex | §6 |

**4 source 정합 (evidence 실증)**: (d) 격상 정당 (D-2 step + run `26517803107` success + 코드 불변, 4 source verify) / fixtures 실행 / R-1 부재 / R-2 placeholder / R-5 known limitation / pytest 152 / (e2) framing 59 정합 / scope 침입 0 / 발효 형태 32·59 일관.

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push → 본 cycle 합의 발효 (REVISE → v1.1 흡수) → **GP-2 detection-layer PASS 발효**. 후속: MVP-2 Implementation Evidence PASS 발효 합의 (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1, full GP-2 PASS prevention = 잔여 trajectory) = 사용자 명시 별도 cycle.
