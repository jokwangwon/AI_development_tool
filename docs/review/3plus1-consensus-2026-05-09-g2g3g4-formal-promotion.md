# 3+1 멀티에이전트 합의 보고서 — G2 + G3 + G4 정식 PASS 승격 (2026-05-09)

**합의 형태**: 옵션 3 — G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (cross-vendor 1 + 인접 컨텍스트 1)
**합의 일자**: 2026-05-09
**검토 대상**:
- G2 — `docs/architecture/governance-preconditions.md` (DRAFT)
- G3 — `docs/architecture/hermes-not-root-of-trust-runtime.md` (DRAFT)
- G4 — `docs/architecture/provider-agnostic-memory-skill-design.md` (DRAFT)

**합의 목적**:
1. 3 게이트 (G2/G3/G4) 동시 정식 PASS 승격 가능 여부 판정
2. P2 v3 정식 채택 합의 단계 진입 가능 여부 판정

**Hermes PMO 격상 선언**: ❌ 본 합의 범위 외 (4 게이트 모두 PASS + 외부 LLM 1+ + 사용자 명시 결정 후 별도 합의로만 발생 가능 — G3 §4.4.2 영구 권위)

**상위 권위**: ADR-011 §2.1 (수단/목적 분리, (a)~(d) + (e)) / §2.3 (권위 위계) / §2.4 (T1/T2/T3) — G3 §4.4.2 (외부 LLM 조건) — system-identity-prequel §3.3 #2 (사용자 명시 commit + Hermes-originated 자동 reject)

---

## 0. 5 입력 요약 + 메타 정보

### 0.1 입력 매트릭스

| # | Agent | 모델 / 컨텍스트 | 판정 | 핵심 조건 수 | 핵심 영역 |
|---|-------|------------|------|----------|--------|
| 1 | **Agent A** (구현/운영 가능성) | Claude Opus 4.7 / 동일 컨텍스트 패밀리 | **APPROVE WITH CONDITIONS** | 7 조건 | 운영 부담 40~70일, 8.1/10, HIGH 위험 2건 (R-8 G2 §9 fox-guarding / R-9 외부 LLM 1+ 필수), 3 게이트 의존 일관성 8/8 PASS |
| 2 | **Agent B** (보안/거버넌스) | Claude Opus 4.7 / 동일 | **APPROVE WITH CONDITIONS** | 4 조건 + 7 Gap | Provider Liquidity 4-way 보호, T3 위반 0건, 7 Gap (Gap-1 헌법 8조 #4 / Gap-3 external-review write 차단 / Gap-6 .git/ read-only / Gap-7 자기참조 외부 LLM 1+ MEDIUM, Gap-5 git append commit LOW-MEDIUM, Gap-2/4 LOW) |
| 3 | **Agent C** (대안/단순화) | Claude Opus 4.7 / 동일 | **APPROVE WITH CONDITIONS** | 3 조건 | 6 GP / 22 권한 / 17 필드 축소 *불필요*, 옵션 3 정당화 재서술 권고 ("격상 답습" → "PR 묶음 + 자기참조 통제 + 의존 묶기"), 외부 LLM *권장→필수* 격상 권고 |
| 4 | **GPT** (외부 cross-vendor) | GPT (별 vendor) / 외부 | **APPROVE WITH CONDITIONS** | 7 조건 | PASS 범위를 *Design/Governance Gate PASS* 로 한정 — Implementation PASS 제외, GP-2~GP-6 "DESIGN PASS / IMPLEMENTATION PENDING" 표기, Evidence Ledger 11 필드 + hash chain/signed commit, .git/ + .github/workflows/ + pre-commit + CI config 보호, P9~P12 후보 4건 |
| 5 | **Claude (인접 컨텍스트)** | Claude / 외부 세션 (동일 모델 패밀리, 메타 면책 명시) | **APPROVE WITH CONDITIONS** | 7 필수 + 2 권고 | C-1 Specification PASS vs Operational PASS 분리, C-2 PoC 의무, C-3 cross-vendor LLM 추가 (본 응답 동봉 금지), C-4 P9~P11 deferred, C-5 메타-순환 청산, C-6 SPOF accepted risk, C-7 Tier-2/3 catalog, C-8 단순화 (6→3-4/22→12/17→8), C-9 ADR-009/P1 진입 조건 |

### 0.2 5/5 일치 판정

→ **5/5 입력 모두 APPROVE WITH CONDITIONS**. BLOCK 0건, PARTIAL 0건, 무조건 APPROVE 0건.
→ 단, *조건의 구체성·깊이·강조점*은 입력별로 비대칭 (Agent A = 운영 부담 정량 / Agent B = 7 Gap enumeration / Agent C = 단순화 부재 + 정당화 재서술 / GPT = PASS 범위 명시 + 7 보호 대상 명시 + P9~P12 / Claude = 자기참조 메타-순환 + SPOF + Tier-2/3 검증 + 단순화 적극 권고 + cross-vendor 추가).

### 0.3 Reviewer 종합 책임 분리

본 Reviewer 도 Claude Opus 4.7 — **5 입력 중 4 (A/B/C + Claude 인접 컨텍스트) = Claude 패밀리, cross-vendor (GPT) 1건만**. 이 메타 한계를 §12 에서 명시 노출.

본 Reviewer 의 권한:
- ✅ 5 입력 통합 + 조건 매트릭스 작성 (중복 제거 + 우선순위 분류 + 출처 표시)
- ✅ 게이트별 판정 종합 (5/5 일치이므로 Reviewer 가 BLOCK / PARTIAL 판정 변경 *금지* — 사용자 결정 영역)
- ❌ Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 자동 갱신 / archive / 실 코드 / G2/G3/G4 본문 자동 갱신 (사용자 결정 영역)

---

## 1. 일치 (Consensus) — 5/5 또는 4/5 입력 동의

### 1.1 최종 판정 일치 (5/5)

| 항목 | A | B | C | GPT | Claude |
|-----|---|---|---|-----|--------|
| 최종 판정 | APPROVE WITH CONDITIONS | 동일 | 동일 | 동일 | 동일 |
| BLOCK 사유 | 0건 | 0건 | 0건 (§7.4 명시) | 0건 ("BLOCK은 아닙니다") | 0건 |

### 1.2 동시 PASS (옵션 3) 가 단계별 PASS 보다 적절 (4/5)

- **A (§4.1, §8.1 #1)**: "옵션 3 (G2 + G3 + G4 통합 풀 3+1 합의 + PR 묶음) 채택 — 단독 PASS 시 §9 (G2) / §6.5 (G4) 의존 무력화 위험 (R-8) 회피 필수"
- **B (§9.2)**: 본 통합 PASS 가 T3 위반 0건, 의존 일관성 정합 — 통합 합의 적격
- **C (§7.2)**: "옵션 3 권고 유지" — 단 정당화 재서술 (격상 답습 표현 제거)
- **GPT (§3)**: "G2/G3/G4는 서로 강하게 의존합니다 ... 세 게이트를 하나의 묶음으로 통과시키는 것이 정합성 측면에서 더 낫습니다"
- **Claude (§3.1)**: "묶음 검토" ≠ "묶음 PASS" — *옵션 4 (묶음 검토 + 단계별 PASS)* 제안. 이는 옵션 3 *변종* 으로 4/5 동의로 분류

→ **4/5 입력 옵션 3 명시 동의**. Claude 만 *변종 옵션 4* 제안 (묶음 검토 후 PoC 실증 순서대로 단계별 PASS).

### 1.3 PASS 범위 분리 필수 (Design/Governance vs Implementation, Specification vs Operational) — 5/5

- **A (§9.3)**: "본 합의 = G2/G3/G4 *DRAFT 정의 PASS* 한정 ... 단정 금지" — 함의 명시
- **B (§0.1, §10.2)**: "단 *설계 한정* — 실 hook/wrapper 코드 0건은 Exit (b)/(d) 잔여" — 함의 명시
- **C (§7.2 #1)**: "합의 보고서 *전제 정의* 명시: G2/G3/G4 정식 채택 = DRAFT 헤더 제거 + 정식 status 한정. 각 GP/§ Exit (a)~(e) 충족 검증은 *후속 합의*"
- **GPT (조건 1)**: 명시 "**Design/Governance PASS** vs **Implementation PASS**" + 최종 문구 제안 "Design/Governance PASS as a bundled gate set ... this does not constitute implementation/runtime PASS"
- **Claude (C-1)**: "Specification PASS vs Operational PASS 분리"

→ **5/5 입력 일치**. 본 합의의 **비협상 P0 조건**.

### 1.4 외부 LLM 추가 필요성 (cross-vendor 명시 또는 함의) — 4/5

- **A (§8.1 #2)**: "외부 LLM 1+ 의견 수집 — G3 §4.4.2 영구 권위에 따라 본 합의 자체에서 외부 LLM 1+ 의견 의무화 (R-9)"
- **B (Gap-7)**: "본 통합 PASS 합의 형태 결정 시 외부 LLM 1+ 강력 권장 — 격상 통합 합의 답습 (G3 §4.4.2)"
- **C (§7.2 #2)**: "외부 LLM 1+ *권장 → 필수* 격상"
- **Claude (C-3)**: "GPT-5.x 또는 Gemini 1+ 추가 검토 후 P2 v3 진입. 본 응답은 동봉하지 말 것 (동조 편향 통제)"
- **GPT**: 명시 X — 단 "외부 LLM 1개만으로 *최종 안전성*을 보장한다고 보기는 어렵습니다" 명시 + Hermes PMO 격상 단계에서 "외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰" 권고 — *함의 동의*

→ **4/5 명시, 5/5 함의 동의**. 단, *적용 시점* (본 PASS 시점 vs P2 v3 시점 vs Hermes PMO 격상 시점) 은 입력별 차이 → §2.2 부분 일치 영역.

### 1.5 Provider Liquidity 4-way 보호 적정성 (5/5)

- **A (§3.2 §3.4)**: "G4 §3.5 검증 가능 verifiable 규칙 ... depcruise + 자동 schema 검증으로 운영 가능"
- **B (§3.2)**: "**3-way (GP-5 + G3 §6.4 + G4 §3.5) + GP-6 = 4-way 보호**"
- **C (§3.3)**: "#15 `provider_bindings` ... **권장 → 필수 격상 권고**"
- **GPT (단순화 권고 표)**: "G4 provider_bindings | optional only, required/exclusive 금지, 최소 2 provider 재해석 가능을 schema lint 규칙으로 강제"
- **Claude (§2.4)**: "강력합니다. 그러나 enforcement는 PR review + depcruise에 의존 ... P2-5 라운드트립 검증이 진짜 enforcement"

→ **5/5 적정성 동의**. 단, lint 규칙 강제 + 라운드트립 PoC 실증이 후속 의무.

### 1.6 헌법 8조 위반 경로 P1~P8 enumeration의 완전성 — 4/5 (조건부)

- A: 완전성 명시 X (운영 측면 한정)
- **B (§5.1)**: "Gap-1 — 헌법 8조 #4 (보안 변경은 3+1 합의) *프로세스 강제* 가 P1~P8 enumeration 또는 GP 매트릭스 본문에 누락"
- C: 완전성 명시 X
- **GPT (§2 누락된 위반 경로)**: "P9~P12 후보 — prompt injection / evidence forgery / supply-chain / memory poisoning / generated docs poisoning / migration import-export path traversal / Memory poisoning"
- **Claude (§2.2)**: "P9 후보 — Memory poisoning side-channel / P10 후보 — Provider-specific endpoint hardcoding / P11 후보 — CLAUDE.md 프롬프트 파일 lock-in"

→ **4/5 (B + GPT + Claude 명시 동의 + A 운영 한정 미언급)**. 본 PASS 차단 사유 X — 후속 *deferred candidates* 등록 권고. P0 조건 아닌 P1 조건.

### 1.7 단일 실패점 / 메타 안전장치 — 5/5 (수용 가능 + 외부 anchor 결합 보강 권고)

- **A**: §2.4 § §5.5 메커니즘 운영 가능, 신규 발명 0
- **B (§6.1)**: "상호 보강 강함 (정책 파일 / Hermes-originated / T3 변경 — 2~3중 보호) ... 외부 anchor (외부 LLM / git history) 결합으로 강화"
- **C (§6.2)**: "메타 한계 *완전 보강 부재* — 본 합의 PASS 판정은 *통제 유의미하나 완전하지 않은* 상태"
- **GPT (§2)**: "Evidence Ledger 자체의 변조 방지 ... .git 및 CI 설정 보호 ... 외부 LLM 검토 결과 저장 경로"
- **Claude (§2.3, C-6)**: "G2 §9 + G3 §4 + G3 §5.5의 단일 실패점이 *1인 동일 호스트 운영 환경에서 의도적 수용된 risk*임을 명시 기록"

→ **5/5 일치 — SPOF 수용 가능 + accepted risk 명시 권고 + 외부 anchor (git history / 외부 LLM) 보강**.

---

## 2. 부분 일치 (Partial) — 2~3/5 입력 동의

### 2.1 단순화 깊이 — 3/5 차이

| 입력 | 단순화 입장 |
|------|--------|
| **A** | 미언급 (운영 측면 한정) |
| **B** | 미언급 (보안 측면 한정) |
| **C (§3)** | 6 GP / 22 권한 / 17 필드 축소 *불필요* — 단 G4 #15 권장→필수 격상 + #10/#11/#12/#14/#16 MVP/후속 분리 표기 |
| **GPT (§3)** | "줄이지 말고 유지. 다만 GP-2~GP-6은 *Implementation Pending* 상태 표기 ... 17 필드 ... 줄이기보다는 MVP required / recommended / future 로 나누는 것이 낫습니다" |
| **Claude (§3.2, C-8)** | **적극 단순화 권고** — G2 6→3-4 카테고리, G3 22→12 권한 (derivation rule), G4 17→8 MVP 필드 (id/name/version/scope/allowed_actions/forbidden_actions/promotion_status/provider_bindings) |

→ **C + GPT (2/5)**: 유지 + MVP/후속 분리 표기. **Claude (1/5)**: 적극 단순화. **A + B (2/5)**: 미언급.

**Reviewer 채택**: **C + GPT 입장 (유지 + MVP/후속 분리 표기)**. 근거:
- 본 합의 단계는 *DRAFT 정의 PASS 한정* (5/5 §1.3 일치) — 단순화는 *PoC 운영 단계* 의 별도 합의 영역
- C (§3.1 #1, §3.2 #1, §3.3 #1) 가 6 GP / 22 권한 / 17 필드 *각각 분석* 후 통합 *권장하지 않음* 결론 — 단순화 시 의도된 layer 분리 손상 위험 명시
- Claude C-8 도 "강력 권고, 의무 아님" 명시 — Claude 자신도 P2 (별도 합의) 분류
- GPT 도 "MVP required / recommended / future 로 나누는 것이 낫습니다" — 동일 절충안

→ **단순화 적극 검토는 P2 (별도 합의)**. MVP/후속 분리 표기는 P1 (PASS 직후 흡수).

### 2.2 외부 LLM 추가 의견의 *적용 시점* — 5/5 함의 동의 X, 4 시점 분기

| 입력 | 외부 LLM 추가 시점 |
|------|--------------|
| **A (§8.1 #2)** | 본 합의 시점 (binary 조건) |
| **B (Gap-7)** | 본 합의 시점 (강력 권장) |
| **C (§7.2 #2)** | 본 합의 시점 또는 옵션 3 정당화 재서술과 결합 |
| **GPT (§4 표)** | "G2/G3/G4 설계 PASS = 외부 LLM 1개로 충분" / "Hermes PMO 격상 = 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰" |
| **Claude (C-3)** | P2 v3 정식 채택 *전* (cross-vendor GPT 또는 Gemini, 본 응답 동봉 금지) |

→ **본 합의 시점 (G2/G3/G4 PASS) 외부 LLM 1+ = 5/5 충족** (GPT + Claude 응답 = 2건). **단, P2 v3 정식 채택 합의 *진입 자체* 에 추가 cross-vendor (Gemini 등) 필요 여부는 4 시점 분기**:
- A/B/C/Claude 입장 = 본 합의 후 P2 v3 진입 *전* 추가 cross-vendor 권고
- GPT 입장 = "외부 LLM 1개 + 내부 3+1 종합이면 가능" (본 합의 시점에서 충분)

**Reviewer 종합**: P2 v3 정식 채택 *합의 형태 결정* 시점에 사용자가 cross-vendor (Gemini 등) 추가 수집 vs 본 합의로 충분 결정. **본 Reviewer 가 단정 금지** (사용자 결정 영역, Claude C-3 메타 편향 통제 권고 답습).

### 2.3 P9~P12 (누락 위반 경로) 의 *우선순위* — 2/5 명시

| 입력 | P9~P12 입장 |
|------|------|
| GPT (§2 + 조건 7) | P9~P12 추가 (4건) — Implementation Pending 단계의 일부로 흡수 |
| Claude (§2.2, C-4) | P9~P11 (3건) — *deferred candidates* 명시 기록 (즉시 GP 추가 의무 아님) |
| A | 미언급 |
| B | Gap-1 (헌법 8조 #4 프로세스 강제) 만 명시 — 별도 영역 |
| C | 미언급 |

→ **2/5 (GPT + Claude) 명시**. **Reviewer 채택**: Claude 입장 ("deferred candidates 명시 기록, 즉시 GP 추가 의무 아님") — GPT 도 "별도 보조 위험으로 둬야 합니다" 동조. **P1 조건** (PASS 직후 흡수, 합의 보고서 본문 + 신규 ADR 또는 G2 §X 등록).

### 2.4 1인 메타-템플릿 거버넌스 부담 — 3/5 우려 vs 2/5 비례 적정

| 입력 | 부담 평가 |
|------|------|
| A (§6) | "메타-템플릿 가정 시 정당, 단일 프로젝트 시 과대" — 명시 적정 (R-10 명시 권고) |
| B | 미언급 (보안 측면 한정) |
| C (§3) | 단순화 *불필요* — 부담 적정 (6 GP / 22 권한 / 17 필드 모두 MVP 시점 적정) |
| GPT (§1) | "1인 개발자 기준으로는 운영 부담이 큽니다 ... 자동화하지 않으면 사람이 계속 기억해야 하는 체계" — 우려 |
| Claude (§1.3) | "1인 메타-템플릿에는 2~5배 과잉으로 보입니다" — 적극 우려 |

→ **3/5 (A 부분 + GPT + Claude) 우려, 2/5 (C 명시 + B 함의) 적정**. **Reviewer 종합**: 부담 *우려는 정직하게 노출하되*, 본 합의 PASS 차단 사유 X (5/5 일치). 메타-템플릿 가정 명시 + 자동화 (체크리스트/CI/pre-commit) 의무는 후속 PoC 단계 흡수. **P1 조건** (메타-템플릿 가정 명시는 합의 보고서 + G2/G3/G4 헤더 또는 §X 권고).

---

## 3. 불일치 (Divergence) — 입력 간 명확한 의견 차

### 3.1 옵션 3 정당화 표현

- **A (§4)**: "Hermes PMO 격상 통합 합의 답습" 표현 *허용* (옵션 3 명시 권고)
- **B**: 미언급 (입장 X)
- **C (§7.2 #3)**: **"격상 답습" 표현 제거 권고** — "PR 묶음 + 자기참조 통제 + 의존 묶기" 로 재서술 (격상 답습 정당화는 *순환 논리 위험*)
- **GPT**: 미언급 (입장 X)
- **Claude (§3.1)**: "묶음 검토 ≠ 묶음 PASS" — 격상 답습 의미 자체에 부분 이의 (옵션 4 제안)

→ **A vs C/Claude 약한 불일치**. **Reviewer 채택**: **C 입장**. 근거:
- 본 합의 ≠ Hermes PMO 격상 합의 (사용자 명시 답습)
- "격상 답습" 표현 사용 시 본 합의가 *격상의 일부* 로 오인 위험 (C §1.2 메타 편향 식별)
- 옵션 3 정당화는 (a) PR 묶음 효율 (b) 외부 LLM 의견 누적으로 자기참조 통제 강화 (c) G2 ↔ G3 ↔ G4 의존 그래프 동시 검증 (d) 본 의뢰 자료 §3 답습 — 4 명시 가능

→ **본 합의 본문 (§9 종합 판정) 에서 "격상 통합 합의 답습" 표현 사용 시 *함의* 명시 (Hermes PMO 격상 자동 발화 X)**.

### 3.2 옵션 3 vs 옵션 4 (묶음 PASS vs 묶음 검토 + 단계별 PASS)

- **A/B/C/GPT**: 옵션 3 (묶음 PASS) 권고
- **Claude (§3.1)**: 옵션 4 (묶음 검토 + 단계별 PASS) 대안 제안

→ **4/5 vs 1/5**. **Reviewer 채택**: **옵션 3 (다수 입장)**. 근거:
- Claude 자체도 옵션 4 를 *대안* 으로만 제안, 옵션 3 *부정 X*
- 본 합의 = "DRAFT 정의 PASS 한정" (5/5 §1.3 일치) → 묶음 PASS 와 묶음 검토 + 단계별 PASS 의 *실질적 차이* 가 작음 (PoC 는 모두 후속)
- 사용자 명시 결정 답습 = 옵션 3 명시 의도

→ **옵션 4 는 Reviewer 종합 후 사용자 결정 영역 — *사용자 결정 시 옵션 4 채택 가능*** 명시.

---

## 4. 누락 (Gap) — 특정 입력만 언급

### 4.1 Agent A 단독 발견

- **R-8 (HIGH)**: G2 §9 fox-guarding-the-henhouse 위험 — G2 단독 PASS 시 G3 §5.2 #5 / §5.5 위임 무력화. 옵션 3 채택 필수 조건.
- **R-1 (MEDIUM)**: P1 v2 facade MVP 진입 trigger 명시 필요 — GP-5 PASS 의 prerequisite
- **R-7 (MEDIUM)**: G3 §5.3 (iii) 사용자 명시 승인의 *기술적 검증 메커니즘* 약함 (GitHub branch protection / PR review 강제 / GPG 서명)
- **운영 부담 정량 추정 40~70일** (1인 full-time)

### 4.2 Agent B 단독 발견 (7 Gap)

- **Gap-1 (MEDIUM)**: 헌법 8조 #4 ("보안 변경은 3+1 합의") *프로세스 강제* 가 P1~P8 enumeration 또는 GP 매트릭스 본문에 누락
- **Gap-2 (LOW)**: Skill `created_from` 가 *Hermes-originated 검증* 항목으로 직접 활용 명시 부재
- **Gap-3 (MEDIUM)**: `docs/external-review/` Hermes write 권한 명시 부재 (GPT 조건 4 와 부분 중복)
- **Gap-4 (LOW)**: Skill `allowed_actions` enum *추가* 절차 (T3 분류) 명시 권고 — 미래 `policy_write` 등 등록 시 §5.2 #2 차단 우회 차단
- **Gap-5 (LOW-MEDIUM)**: Hash chain git append commit option 명시 권고 (GPT 조건 6 와 부분 중복)
- **Gap-6 (MEDIUM)**: `.git/` filesystem read-only 강제 명시 부재 — `.git/config` (Hermes git author 위조 경로) cover X (GPT 조건 4 와 부분 중복)
- **Gap-7 (MEDIUM)**: 본 통합 PASS 합의의 외부 LLM 1+ 적용 명시 부재 (현 합의로 충족)

### 4.3 Agent C 단독 발견

- **ADR-009 정렬도 부재** — GP-5 / G4 §6.4 가 ADR-009 미인용, T1~T4 측정 시작 시점 미정의
- **신규 ADR 번호 할당 (ADR-012/013/014)** — 동시 발행 시 충돌 위험, PR 묶음 시점 이전 결정 권고
- **P1 v2 facade 현 상태 (재합의 대기)** 명시 누락 — G2 GP-5 §7.4 entry 기준에 *합의 통과* 가 *암묵적 전제*
- **옵션 3 정당화 자기참조 위험** — "격상 답습" 표현 = 순환 논리 위험 (§3.1 답습)

### 4.4 GPT 단독 발견

- **PASS 범위를 "Design/Governance Gate PASS" 로 명시 한정** — *최종 문구 제안* 본문 포함 ("this does not constitute implementation/runtime PASS")
- **Evidence Ledger 11 필드 enumeration**: evidence_id / gate_id / tool / command / expected result / actual result / artifact path / hash / reviewer / timestamp / pass-fail status / rollback trigger
- **보호 대상 7항목 enumeration**: `.git/`, `.github/workflows/`, pre-commit config, CI config, evidence ledger, external-review 문서, ADR/SDD/gate 정의 문서
- **P9~P12 후보 4건** (Claude 와 부분 중복, *prompt injection / tool-output injection / evidence forgery / dependency-supply-chain / memory poisoning / migration path traversal / generated docs poisoning* 종합)
- **G4 hash chain 7 보강 항목**: canonical JSON / newline-encoding / field ordering / genesis hash / prev_hash 검증 실패 처리 / full rewrite 방어 / migration round-trip 의미 보존 ledger

### 4.5 Claude (인접 컨텍스트) 단독 발견

- **C-5 메타-순환 청산** — G3 §4 "외부 LLM 권장/필수" 자체가 *외부 LLM 없이 작성된 메타-순환*. ADR-011 Amendment 또는 별도 합의 보고서 명시 기록. 본 응답 + cross-vendor (GPT) 응답이 청산 evidence
- **C-6 SPOF accepted risk 명시** — "1인 동일 호스트 운영 환경에서 의도적 수용된 risk", multi-host 운영 전환 시 추가 layer 의무 발동 트리거 정의
- **C-7 Tier-2/Tier-3 catalog 검증** — GP-1 G1b 흡수 주장의 완전성. 미검증 시 "Tier-1 한정 흡수" 로 표현 정정
- **§4.4 메타 편향 관찰** — 본 의뢰 자료 §10 framework (4 차원 + 4 판정 옵션) 자체가 평가 형식 사전 결정 → 검토자가 framework 외부 fundamental 질문 ("왜 GP가 6개인가") 제기 인센티브 약화
- **추론적 보조의 우위 영역** — "계산적 = 우월 가정에 일부 허점. 계산적 메커니즘 (regex, depcruise, SQL trigger) 은 false negative 시 조용히 실패. GP-4 외부 입력 검증과 GP-6 Memory/Skill Migration 은 추론적 보조를 우위로 설계"

---

## 5. 통합 조건 매트릭스 (중복 제거 + 출처 명시 + 우선순위 분류)

**우선순위 정의**:
- **P0**: PASS 차단 — 즉시 흡수 의무 (본 합의 보고서 본문 + G2/G3/G4 헤더 갱신 권고)
- **P1**: PASS 직후 — 본 합의 PR 묶음 또는 후속 PR (1~2주 내) 흡수
- **P2**: PASS 후 — 별도 합의 또는 별도 PR (특정 시점에 의무 발동)

| # | 조건 | 출처 (입력 동의) | 우선순위 | 책임 영역 |
|---|------|------|--------|----------|
| **C-A** | **PASS 범위를 "Design/Governance Gate PASS" 로 명시 한정** (Implementation/Runtime PASS 제외) | A 함의 §9.3 + B §0.1 + C §7.2 #1 + GPT 조건 1 + 최종 문구 제안 + Claude C-1 = **5/5** | **P0** | 본 합의 보고서 §9 + G2/G3/G4 헤더 갱신 권고 |
| **C-B** | **GP-2~GP-6 / G3 운영 / G4 라운드트립 = "DESIGN PASS / IMPLEMENTATION PENDING" 표기** | A §1.1 (GP-1=즉시충족, GP-2~6=PoC 5/6) + B §10.2 + C §1.3 (시나리오 X 함의) + GPT 조건 2 (표 명시) + Claude C-2 = **5/5** | **P0** | G2 §3.4~§8.4 헤더 + 본 합의 보고서 §6 |
| **C-C** | **메타-템플릿 가정 명시** (단일 production 프로젝트 사용 시 부담 재평가) | A §6.2 + GPT §1 (함의) + Claude §1.3 (함의) = **3/5** | **P1** | 본 합의 보고서 §10 또는 G2/G3/G4 §1 답습 |
| **C-D** | **Evidence Ledger 보호 강화** (11 필드 + hash chain/signed commit 대상) | GPT 조건 3 + B Gap-5 (git append commit) 부분 중복 + Claude C-2 (ledger 등재 의무) = **3/5** | **P1** | 신규 ADR 후보 또는 G3 §1.3 / §5.3 보강 |
| **C-E** | **Git/CI/external-review 파일 보호 명시** (`.git/`, `.github/workflows/`, pre-commit, CI config, evidence ledger, external-review, ADR/SDD/gate 정의 문서) | GPT 조건 4 (7 항목 명시) + B Gap-3 (external-review) + Gap-6 (.git/) = **2/5 명시 + 1/5 부분 중복** | **P1** | G3 §2.2 #11 확장 |
| **C-F** | **G4 hash chain 사양 보강** (canonical JSON / newline-encoding / field ordering / genesis hash / prev_hash 실패 / full rewrite 방어 / migration round-trip 의미 보존 ledger) | GPT 조건 6 (7 항목) + B Gap-5 (git append commit) + A R-5 (RFC 8785 JCS 인용) + 본 G4 검토 §3.1 P-1 자체 명시 = **3/5** | **P1** | G4 §4.4 / §4.6 보강 |
| **C-G** | **P9~P12 (누락 위반 경로) deferred candidates 명시 기록** (prompt injection / evidence forgery / supply-chain / memory poisoning / Memory poisoning side-channel / Provider-specific URL hardcoding / CLAUDE.md prompt-level lock-in) | GPT 조건 7 + Claude C-4 + B Gap-1 (헌법 8조 #4 별 영역) = **2/5 명시 (P9~P12) + 1/5 별 영역** | **P1** | 본 합의 보고서 §11 또는 G2 §1.2 P 후보 부록 |
| **C-H** | **헌법 8조 #4 ("보안 변경은 3+1 합의") 프로세스 강제 row 추가** | B Gap-1 = **1/5** | **P1** | G2 §11 영구 핵심 제약 표 |
| **C-I** | **ADR-009 / P1 v2 facade 진입 조건 의존성 명시** (GP-2 LLM facade redaction filter / GP-5 P1 facade 단일 진입점 / G4 migration provider-neutral interface) | GPT 조건 5 + Claude C-9 + A R-1 + C §4.2 = **4/5** | **P1** | 본 합의 PR 묶음 + ADR-009 §X 갱신 후보 |
| **C-J** | **메타-순환 청산 — G3 §4 "외부 LLM 권장/필수" 자체가 외부 LLM 없이 작성됨을 ADR Amendment 또는 별도 합의 보고서에 명시 기록** (본 GPT + Claude 응답이 청산 evidence) | Claude C-5 = **1/5** | **P1** | 본 합의 보고서 §12 + G3 §4 cross-reference 또는 ADR-011 Amendment 후보 |
| **C-K** | **SPOF accepted risk 명시** (G2 §9 + G3 §4 + G3 §5.5 단일 호스트 권한 모델 의존, multi-host 전환 시 추가 layer 의무 발동 트리거) | Claude C-6 = **1/5** | **P1** | 본 합의 보고서 §10 또는 G3 §4 부록 |
| **C-L** | **Tier-2/Tier-3 catalog 검증** (GP-1 G1b 흡수 완전성 — 미검증 시 "Tier-1 한정 흡수" 표현 정정) | Claude C-7 = **1/5** | **P1** | G2 §3.5 GP-1 본문 또는 합의 보고서 §6 |
| **C-M** | **Skill `created_from` Hermes-originated 검증 활용** | B Gap-2 = **1/5** | **P2** | G4 §3 + G3 §3.1.2 cross-reference |
| **C-N** | **Skill `allowed_actions` enum *추가* T3 분류** (미래 `policy_write` 등) | B Gap-4 = **1/5** | **P2** | G4 §10 변경 절차 표 |
| **C-O** | **G3 §5.3 (iii) 기술적 검증 메커니즘** (GitHub branch protection / PR review 강제 / GPG 서명) | A R-7 = **1/5** | **P2** | PoC 진입 시점 별도 합의 |
| **C-P** | **단순화 별도 합의 검토** (G2 6→3-4 카테고리 / G3 22→12 권한 / G4 17→8 MVP) | Claude C-8 (강력 권고, 의무 아님 명시) + GPT (MVP/recommended/future 분리 부분 동조) + C (불필요 명시) = **1/5 적극 + 1/5 절충 + 1/5 반대** | **P2** | 별도 합의 — Reviewer 종합 채택 = **유지 + MVP/후속 분리 표기 (P1)** + 적극 단순화 = **P2** |
| **C-Q** | **Cross-vendor 외부 LLM 추가 (Gemini 등)** P2 v3 정식 채택 진입 *전* 또는 Hermes PMO 격상 *전* | Claude C-3 + A 함의 + B Gap-7 함의 + C §7.2 #2 = **4/5 (적용 시점 4 분기)** | **P2** | 사용자 결정 영역 (P2 v3 정식 채택 합의 형태 결정 시점) |
| **C-R** | **운영 부담 자동화 (체크리스트/CI/pre-commit/Evidence Ledger 템플릿)** | GPT §1 (함의) + Claude §1.3 (함의) + A §6 (함의) = **3/5** | **P2** | PoC 진입 후 Phase 2 의 일부 |
| **C-S** | **신규 ADR 번호 할당 + 우선순위** (ADR-012/013/014 후보 동시 발행 vs 순차) | C §4.3 = **1/5** | **P1 또는 P2** | PR 묶음 시점 이전 사용자 명시 결정 |
| **C-T** | **외부 LLM 1+ 본 합의 시점 충족 명시** (GPT + Claude = 2건, 본 합의 §10 명시) | A §8.1 #2 + B Gap-7 + C §7.2 #2 + Claude C-3 + GPT 함의 = **5/5** | **P0** (이미 충족) | 본 합의 보고서 §0 + §12 명시 |

---

## 6. 게이트별 판정

| 게이트 | 판정 | 근거 | 부수 조건 (참조) |
|-------|------|-----|---------|
| **G2** (governance-preconditions.md) | **APPROVE WITH CONDITIONS — Design/Governance Gate PASS** | 5/5 입력 합의: P1~P8 매핑 적정 (B §5.2), GP-1 = G1b 흡수 즉시 PASS (A §1.1), GP-2~GP-6 implementation evidence 미충족 (게이트 정의 (b) 조건 미달, GPT 조건 1·2 + Claude §1.2 + A §1.1 + B §10.2 일치). §9 메타 안전장치 *interface 한정* 명시 정직 (A §1.4), 단 G3 §5.2 #5 / §5.5 위임 — 옵션 3 (G3 동시 PASS) 채택으로 무력화 위험 (R-8) 회피 | C-A, C-B, C-C, C-E, C-H, C-I, C-L 흡수 |
| **G3** (hermes-not-root-of-trust-runtime.md) | **APPROVE WITH CONDITIONS — Design/Governance Gate PASS** | 5/5 합의: 권위 위계 운영 충실 (B §1.1), 22 권한 (T1 8 / T2 2 / T3 12) enumeration 명료 (A §2.1, GPT §1, Claude §1.1), 자기참조 차단 §4 13 매트릭스 + §5.3 PASS 4 요건 *상호 보강* (B §1.2, §6.1), Evidence Ledger / Git/CI/external-review 보호 보강 권고 (GPT 조건 3·4 + B Gap-3·6 + Claude §2.1·§2.3 메타-순환). 외부 LLM 1+ 본 합의 시점 충족 (GPT + Claude = 2건) | C-D, C-E, C-J, C-K, C-O 흡수 |
| **G4** (provider-agnostic-memory-skill-design.md) | **APPROVE WITH CONDITIONS — Design/Governance Gate PASS** | 5/5 합의: Memory scope 4단계 (MVP Global+Project) 정의 적정 (A §3.1), 17 schema 필드 표준 타입 + 필수/권장 분리 (A §3.2, GPT §3 표, Claude §3.2), §3.5 `provider_bindings` *required/exclusive 금지* + 최소 2 provider 재해석 4-way 보호 (B §3, GPT 단순화 권고 표, Claude §2.4), JSONL hash chain 변조 방지 정의 충실 + 사양 보강 권고 (B §4.2, GPT 조건 6, A §3.3 R-5), 라운드트립 PoC 0건 = (b) 잔여 (B §3.3, Claude §1.2, A §3.3) | C-D, C-F, C-G, C-M, C-N 흡수, #15 권장→필수 격상 권고 (C §3.3 + GPT §3 + Claude §3.2 4/5 동의) |

→ **3 게이트 모두 동시 정식 PASS 승격 가능** — 단, **C-A + C-B + C-T 의 P0 조건 충족 명시 시에만**.

---

## 7. P2 v3 정식 채택 합의 단계 진입 가능 여부

### 7.1 진입 가능 (조건부)

5/5 입력이 *진입 가능* 함의 동의 (GPT 명시: "조건부 PASS, 조건 충족 후 가능" / Claude 명시: "✅ specification PASS 승격: 가능 (조건 C-1 충족 시) ⏳ P2 v3 정식 채택 합의 진입: C-1 ~ C-7 모두 충족 후" / A §9 / B §10 / C §8.3).

### 7.2 진입 *전* 충족 의무 조건 (P0 + P1 일부)

**P0 (필수)**:
- C-A (PASS 범위 명시 한정) — 본 합의 보고서 §9 + G2/G3/G4 헤더 갱신 권고
- C-B ("DESIGN PASS / IMPLEMENTATION PENDING" 표기) — G2/G3/G4 §X 갱신 권고
- C-T (외부 LLM 1+ 본 합의 시점 충족 명시) — 본 합의 보고서 §0 + §12 (GPT + Claude = 2건)

**P1 (강력 권고, P2 v3 진입 *전* 흡수 권장)**:
- C-C (메타-템플릿 가정 명시)
- C-D (Evidence Ledger 보호 강화)
- C-E (Git/CI/external-review 파일 보호 명시)
- C-F (G4 hash chain 사양 보강)
- C-G (P9~P12 deferred candidates 명시 기록)
- C-I (ADR-009 / P1 v2 facade 진입 조건 의존성 명시)
- C-J (메타-순환 청산 명시 기록)
- C-K (SPOF accepted risk 명시)
- C-L (Tier-2/Tier-3 catalog 검증 또는 "Tier-1 한정 흡수" 표현 정정)

### 7.3 진입 *후* 흡수 가능 조건 (P2)

- C-H (헌법 8조 #4 row 추가)
- C-M (Skill `created_from` Hermes-originated 검증)
- C-N (Skill `allowed_actions` enum 추가 T3 분류)
- C-O (GitHub branch protection / GPG 서명)
- C-P (단순화 적극 검토 별도 합의)
- C-Q (Cross-vendor 외부 LLM Gemini 등 추가)
- C-R (운영 부담 자동화)
- C-S (신규 ADR 번호 할당)

### 7.4 P2 v3 정식 채택 *자체* 의 합의 형태

**4/5 함의 동의**: 단축 합의 (Reviewer-only) 가능 + cross-vendor 외부 LLM (C-Q) 추가 권고. **GPT (§4 표)**: "외부 LLM 1개 + 내부 3+1 종합이면 가능" — 단축 합의 충분 입장. **Claude (C-3)**: P2 v3 진입 전 cross-vendor 추가 권고.

→ **Reviewer 종합**: P2 v3 정식 채택 합의 형태는 **사용자 결정 영역**. 본 Reviewer 권고는:
- 시나리오 X (분리): 본 합의 (옵션 3) → G2/G3/G4 PASS → 별도 단축 합의로 P2 v3 정식 채택 (cross-vendor 추가 시점 사용자 결정)
- 시나리오 Y (통합): 본 합의 PR 묶음에 P2 v3 정식 채택 동시 흡수 (cross-vendor 추가 P2 분류, 본 합의로 충분)

**본 Reviewer 단정 금지** — 양 시나리오 모두 합리적, C §8.3 답습.

---

## 8. 본 합의의 자기참조 / 메타 편향 통제 평가

### 8.1 외부 LLM 2건 (cross-vendor 1 + 인접 컨텍스트 1) 의 G3 §4.4.2 충족 수준

**G3 §4.4.2 외부 LLM 필수 영역**:
- Hermes PMO 격상 합의 = **필수** (본 합의 범위 외)
- Hermes 정책 변경 합의 = **권장**
- Constitution / ADR 갱신 = **권장**
- 자기 작성 산출 검증 (본 합의 영역) = **권장**

**현 상태**:
- ✅ Cross-vendor 1건 (GPT) — vendor 다양성 통제
- ✅ 인접 컨텍스트 1건 (Claude, 별 세션, 메타 면책 명시) — 동일 모델 패밀리 한계 자체 노출
- → **외부 LLM 2건 = G3 §4.4.2 "권장" 영역 충족 + 부분 "필수" 영역 충족**

**부분 미충족**: Claude 입장 (C-3) "GPT-5.x 또는 Gemini 1+ 추가 검토 후 P2 v3 진입. 본 응답은 동봉하지 말 것" — 본 GPT 응답이 *cross-vendor 1건* 충족 → Claude C-3 의 "추가 cross-vendor" = *2건째* 의미 (Gemini 등). **본 합의에는 미충족 이지만 P2 v3 정식 채택 *전* 또는 Hermes PMO 격상 *전* 충족 권고 (C-Q, P2 분류)**.

### 8.2 본 의뢰 자료 §10 framework 자체의 메타 편향 (Claude §4.4 식별)

> "§10이 4 차원 + 판정 4옵션을 미리 framework 해서 제공. 이는 평가의 형식을 사전 결정하므로 검토자가 framework 외부의 결함 (예: '왜 GP가 5개나 7개가 아닌 6개인가' 같은 fundamental 질문) 을 제기할 인센티브가 약화됩니다."

**Reviewer 평가**: Claude 식별 정확. 본 합의 보고서가 *4 차원 + 4 판정 옵션* 답습 시 동일 메타 편향 재생산. 본 §8 자체에서 명시 노출함으로써 부분 통제 — *완전 해소 X*.

**후속 통제 권고**: 후속 합의 (P2 v3 정식 채택 / Hermes PMO 격상 등) 시 *framework 외부 fundamental 질문* 인센티브 강화 — 의뢰 자료에 "framework 외부 결함 제기 권고" 항목 추가 또는 외부 LLM 의견에 *framework 자유 형식* 답변 옵션 명시.

### 8.3 본 Reviewer 자체의 동조 편향 (자기진단 §12 답습)

본 Reviewer 도 Claude Opus 4.7 — 5 입력 중 4 (A/B/C + Claude 인접 컨텍스트) 가 Claude 패밀리. 본 Reviewer 가 *통합 조건 매트릭스* (§5) 작성 시:
- 입력 phrasing 그대로 인용 (출처 명시)
- 5 입력의 *중복* 을 통합 조건으로 묶을 때 어느 입력의 phrasing 채택할지 silent 영향력 → 가능한 한 출처 표시

**잔여 동조 편향 위험**: 본 Reviewer 가 Claude 패밀리 입장에 무의식 가중치 부여 가능성. C-Q (cross-vendor 추가) 의 P2 분류는 *본 Reviewer 의 결정* — Claude C-3 자체도 "P2 v3 정식 채택 전" 권고이므로 P2 분류 정합. 단, 사용자 결정 시 P1 으로 격상 가능.

---

## 9. 최종 종합 판정

### 9.1 판정

```
APPROVE WITH CONDITIONS — Design/Governance Gate PASS (Bundled)
```

### 9.2 발화 한정

**G2 + G3 + G4 가 다음 조건 충족 시 동시 정식 PASS (Design/Governance Gate PASS) 승격 가능 + P2 v3 정식 채택 합의 단계 진입 가능**:

#### P0 (PASS 차단 — 즉시 흡수 의무 = 본 합의 보고서 commit 시점 충족)

1. **C-A**: PASS 범위를 "Design/Governance Gate PASS" 로 명시 한정 (Implementation/Runtime PASS 제외 명시) — 본 합의 보고서 §6 + §9 명시, G2/G3/G4 헤더 갱신 권고 (사용자 결정 영역)
2. **C-B**: GP-2~GP-6 / G3 운영 / G4 라운드트립 = "DESIGN PASS / IMPLEMENTATION PENDING" 표기 — G2 §3.4~§8.4 헤더 갱신 권고
3. **C-T**: 외부 LLM 1+ 본 합의 시점 충족 명시 — 본 §0 + §8 (GPT cross-vendor + Claude 인접 컨텍스트 = 2건 충족, G3 §4.4.2 "권장" 영역 충족)

#### P1 (PASS 직후 — 본 합의 PR 묶음 또는 후속 PR 1~2주 내 흡수)

4. **C-C**: 메타-템플릿 가정 명시 (단일 production 프로젝트 사용 시 부담 재평가)
5. **C-D**: Evidence Ledger 보호 강화 (11 필드 + hash chain 또는 signed commit 대상)
6. **C-E**: Git/CI/external-review 파일 보호 명시 (`.git/`, `.github/workflows/`, pre-commit, CI config, evidence ledger, external-review, ADR/SDD/gate 정의 문서)
7. **C-F**: G4 hash chain 사양 보강 (canonical JSON / RFC 8785 JCS 인용 / newline-encoding / field ordering / genesis hash / prev_hash 실패 / full rewrite 방어 / migration round-trip 의미 보존 ledger)
8. **C-G**: P9~P12 deferred candidates 명시 기록 (prompt injection / evidence forgery / supply-chain / memory poisoning side-channel / provider-specific URL hardcoding / CLAUDE.md prompt-level lock-in)
9. **C-H**: 헌법 8조 #4 ("보안 변경은 3+1 합의") row 추가 (G2 §11 영구 핵심 제약)
10. **C-I**: ADR-009 / P1 v2 facade 진입 조건 의존성 명시 (GP-2 / GP-5 / G4 migration)
11. **C-J**: 메타-순환 청산 명시 기록 (G3 §4 자체가 외부 LLM 없이 작성됨, 본 GPT + Claude 응답이 청산 evidence)
12. **C-K**: SPOF accepted risk 명시 (G2 §9 + G3 §4 + G3 §5.5 단일 호스트 권한 모델 의존, multi-host 전환 시 추가 layer 의무 발동 트리거)
13. **C-L**: Tier-2/Tier-3 catalog 검증 또는 "Tier-1 한정 흡수" 표현 정정

#### P2 (PASS 후 — 별도 합의 또는 별도 PR, 특정 시점에 의무 발동)

14. **C-M**: Skill `created_from` Hermes-originated 검증 활용
15. **C-N**: Skill `allowed_actions` enum *추가* T3 분류
16. **C-O**: G3 §5.3 (iii) 기술적 검증 메커니즘 (GitHub branch protection / PR review 강제 / GPG 서명) — PoC 진입 시점 별도 합의
17. **C-P**: 단순화 적극 검토 별도 합의 (G2 6→3-4 카테고리 / G3 22→12 권한 / G4 17→8 MVP 필드) — Claude C-8 적극 / GPT MVP 분리 절충 / C 불필요 — Reviewer 종합: PASS 후 별도 합의 영역
18. **C-Q**: Cross-vendor 외부 LLM 추가 (Gemini 등) — P2 v3 정식 채택 합의 *전* 또는 Hermes PMO 격상 *전* 사용자 결정
19. **C-R**: 운영 부담 자동화 (체크리스트 / CI / pre-commit / Evidence Ledger 템플릿) — Phase 2 PoC 진입 후
20. **C-S**: 신규 ADR 번호 할당 + 우선순위 (ADR-012 / 013 / 014 후보 동시 발행 vs 순차) — PR 묶음 시점 이전 사용자 명시 결정 (P1 또는 P2)

---

## 10. 본 합의에서 *발생하지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 선언 (G3 §4.4.2 + 본 의뢰 자료 §0 영구 답습)
- ❌ P2 v3 정식 채택 자동 선언 (본 합의는 *진입 가능 여부* 판정까지)
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 (별도 PR 묶음, T3 영역)
- ❌ P2 v2 / system-identity-prequel.md archive 자동 처리 (정식 채택 시점 사용자 명시 결정)
- ❌ INDEX.md / CONTEXT.md 자동 갱신 (본 합의 commit 후 사용자 결정으로 별도 commit)
- ❌ 실 runtime code / migration script / hook 구현 (Phase 2 PoC 영역)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 (T3 분류 답습)
- ❌ G2 / G3 / G4 본문 자동 갱신 (헤더 갱신 권고만, 본문 변경은 사용자 결정 + 별도 PR)
- ❌ 본 합의 결과의 Hermes-originated 갱신 (외부 LLM 응답 + 본 합의 보고서는 git commit + 사용자 명시만 권위 인정 — system-identity-prequel §3.3 #2 + G3 §4.5)
- ❌ ADR-012 / 013 / 014 신규 ADR 본문 자동 작성 (사용자 결정 영역)
- ❌ 메타포 강제 (system-identity-prequel §7 답습)

---

## 11. 본 합의 후 권고 후속 단계

### 11.1 즉시 (본 합의 commit 직후, 사용자 결정 후)

1. **본 합의 결과 commit** (사용자 명시 commit 만 권위 인정)
2. **G2/G3/G4 헤더 갱신 권고**: "DRAFT" → "Design/Governance Gate PASS (2026-05-09 합의 답습)" + DRAFT 흔적 보존 (예: `## 부록 X — DRAFT 검토 흔적`)
3. **CONTEXT.md 갱신**: 4 게이트 진행 상태 (G1b PASS / G2/G3/G4 Design PASS / Implementation PENDING)
4. **INDEX.md 갱신**: 본 합의 보고서 등록

### 11.2 P0 / P1 조건 흡수 PR 묶음 (1~2주 내)

5. C-A / C-B (헤더 갱신) — 11.1 #2 와 결합 가능
6. C-C / C-J / C-K (합의 보고서 §10 또는 G2/G3/G4 §X 명시) — 본 합의 보고서 후속 갱신 또는 별도 부록
7. C-D / C-E / C-F (G3 §1.3 / §2.2 #11 / G4 §4.4 보강) — 별도 PR 묶음
8. C-G (P9~P12 deferred candidates 명시 기록) — G2 §1.2 부록 또는 신규 합의 보고서 부록
9. C-H (G2 §11 row 추가) — G2 §11 갱신
10. C-I (ADR-009 / P1 v2 facade 진입 조건 의존성 명시) — 본 합의 보고서 §X 또는 ADR-009 §X 갱신
11. C-L (Tier-2/Tier-3 catalog 검증 또는 표현 정정) — G2 §3.5 GP-1 본문 또는 합의 보고서 §6

### 11.3 P2 v3 정식 채택 합의 형태 결정 (사용자 결정 영역)

12. 시나리오 X (분리): 본 합의 → G2/G3/G4 PASS → 별도 단축 합의로 P2 v3 정식 채택
13. 시나리오 Y (통합): 본 합의 PR 묶음에 P2 v3 정식 채택 동시 흡수
14. C-Q (Cross-vendor 외부 LLM Gemini 등 추가) 적용 시점 결정 — P2 v3 진입 전 / Hermes PMO 격상 전 / 본 합의로 충분

### 11.4 ADR 갱신 PR 묶음 (별도)

15. ADR-008 cross-reference 갱신 (Hermes 도입 후속 영역)
16. ADR-009 (P1 v2 / Adapter v2.0) cross-reference 갱신 + T1~T4 측정 시작 시점 명시 (C-I)
17. ADR-010 cross-reference 갱신 (SQLCipher Vault HSM)
18. ADR-011 cross-reference 갱신 (수단/목적 분리) + 메타-순환 청산 Amendment 후보 (C-J)
19. 신규 ADR 후보 (ADR-012 / 013 / 014) 번호 할당 + 우선순위 결정 (C-S)

### 11.5 Phase 1 진입 (해당 시) — Hermes PMO 격상은 별도

20. P2 v3 정식 채택 후 Phase 1 진입 가능 — 단, **G1b PASS 가 이미 Phase 1 acceptance** (2026-05-07 합의 답습) 이므로 Phase 1 진입 자체는 G2/G3/G4 PASS 와 *독립*
21. **Hermes PMO 격상 선언은 본 합의 + Phase 1 진입과 *완전 분리* 영역** — 4 게이트 모두 *Implementation PASS* + 외부 LLM 1+ (cross-vendor) + 사용자 명시 결정 후 별도 합의

---

## 12. 메타 편향 자기진단 (본 합의 자체)

### 12.1 모델 패밀리 비대칭

본 Reviewer 도 Claude Opus 4.7 — 5 입력 중 3 (A/B/C) + 1 (Claude 인접 컨텍스트) = **4/5 가 Claude 패밀리**. Cross-vendor 외부 LLM 은 **GPT 1건만**. → P2 v3 정식 채택 *전* 또는 Hermes PMO 격상 *전* Gemini 등 추가 cross-vendor 권고 (Claude C-3 흡수, C-Q P2 분류).

### 12.2 의뢰 자료 §10 framework 자체의 메타 편향 (Claude §4.4 식별)

본 합의 보고서가 *5 입력 일치도 5/5/4/5/3/5/2/5/1/5* 등 framework 답습 — 입력별 *fundamental 질문* (예: "왜 6 GP 인가, 5 또는 7 이어야 하지 않은가?") 를 *충분히 강조하지 못함*. 후속 합의에서 framework 외부 결함 제기 인센티브 강화 권고.

### 12.3 본 Reviewer 종합 자체의 silent 영향력

5 입력의 *중복* 을 통합 조건으로 묶을 때 *어느 입력의 phrasing* 채택할지가 silent 영향력. 본 보고서는 가능한 한 입력 phrasing 그대로 인용 + 통합 시 출처 표시 — 단, *완전 해소 X*. 후속 합의에서 외부 LLM 이 본 합의 보고서 자체를 검토 (C-Q 시점) 시 본 silent 영향력 부분 통제 가능.

### 12.4 옵션 3 자체의 외부 검증 부재

본 합의 (옵션 3) 채택은 *사용자 명시 결정 답습*. 5 입력 모두 옵션 3 또는 변종 (Claude 옵션 4 = 묶음 검토 + 단계별 PASS) *수용 가능* 평가 — *외부 검증* 은 부분만 (옵션 3 자체에 대한 외부 LLM 의견은 본 합의 결과로 회수 후 사용자 결정). 사용자 결정 시 옵션 4 채택 가능 명시 (§3.2 답습).

### 12.5 본 합의의 *완전 해소 부재* 영역

본 합의는 *통제 유의미하나 완전하지 않은 상태* (C §6.2 답습). 다음 영역 잔여:
- C-Q (cross-vendor Gemini 등 추가) — P2 분류
- C-R (운영 부담 자동화) — Phase 2 영역
- C-P (단순화 적극 검토) — 별도 합의
- 본 Reviewer 동조 편향 — 외부 검토로 부분 통제 (C-Q 시점)
- §10 framework 메타 편향 — 후속 합의 framework 자유 형식 옵션

---

**작성일**: 2026-05-09
**작성자**: Reviewer (Claude Opus 4.7, 종합 합의 작성)
**5 입력 출처**:
- A/B/C — Opus 독립 분석 (`docs/review/agents-2026-05-09-g2g3g4/`)
- GPT — cross-vendor 외부 LLM (`docs/external-review/2026-05-09-g2g3g4-promotion-response.md`)
- Claude (인접 컨텍스트) — 별 세션, 메타 면책 명시 (`docs/external-review/2026-05-09-g2g3g4-promotion-response-claude.md`)

**합의 권위**: 본 보고서는 *Reviewer 종합 + 사용자 명시 결정* 으로 권위. Hermes-originated 변경 자동 reject (G3 §2.2 #20 답습 + system-identity-prequel §3.3 #2)

**최종 판정**: **APPROVE WITH CONDITIONS — Design/Governance Gate PASS (Bundled)** — G2 + G3 + G4 동시 정식 PASS 승격 가능 + P2 v3 정식 채택 합의 단계 진입 가능 (P0 3 조건 + P1 10 조건 흡수 권고)

**다음 단계** (사용자 결정 영역):
1. 본 보고서 commit
2. P0 조건 흡수 — G2/G3/G4 헤더 갱신 + CONTEXT.md / INDEX.md 갱신
3. P1 조건 흡수 PR 묶음 결정
4. P2 v3 정식 채택 합의 형태 결정 (시나리오 X 분리 / Y 통합)
5. C-Q (Cross-vendor Gemini 등) 적용 시점 결정 (P2 v3 진입 전 / Hermes PMO 격상 전 / 본 합의로 충분)
