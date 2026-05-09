# ADR-008 본문 갱신 PR (부록 C 신설 — Hermes PMO Activation Cross-Reference) 단축 합의 보고서

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 ("우선 Reviewer-only 단축 합의로 진행 ... 6 트리거 1+ 발화 시 풀 3+1 승격")
**합의 일자**: 2026-05-09 (후속 13 — ADR-008 본문 갱신 PR)
**검토 대상**: ADR-008 (`docs/decisions/ADR-008-hermes-adoption-decision.md`) 본문 갱신 — **부록 C 신설** (Hermes PMO Activation Cross-Reference, 사용자 명시 7 항목 답습)
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — ADR-008 부록 C 신설 적격, 결정 내용 변경 0건 + cross-reference 강화 한정**

---

## 0. 사전 점검

### 0.1 가동 사유

ADR-013 / 014 후보 발행 결정 검토 (2026-05-09 후속 12) §1.1.3 답습 — "ADR-008 본문 갱신 PR (부록 추가) 으로 ADR-013 대체 가능". 사용자 명시 결정 답습 — "다음 작업은 ② ADR-008 본문 갱신 PR".

**사용자 명시 결정 답습** (2026-05-09 후속 12 후속):
- 작업명 = "ADR-008 본문 갱신 PR"
- 목적 = "Hermes PMO 격상 절차와 P2 v3의 12조건 체크리스트를 ADR-008에 연결"
- 작업 단계 = ADR-008 부록 C 신설 (Hermes PMO Activation Cross-Reference)
- 사용자 명시 7 항목:
  1. P2 v3 Design Adoption 이후 Hermes PMO activation 별도 결정 명시
  2. Hermes PMO 격상 전 12 조건 체크리스트 참조
  3. 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 필요 조건 명시
  4. 사용자 명시 결정 없이는 PMO 격상 불가
  5. Implementation/Runtime PASS 와 Design/Governance PASS 분리
  6. ADR-013 현 시점 발행 보류 사유 참조
  7. ADR-009 C-N / ADR-011 / ADR-012 / G2/G3/G4 cross-reference 보강
- 검토 형태 = Reviewer-only 단축 합의 우선 — 6 풀 3+1 승격 트리거 1+ 발화 시 풀 3+1 승격

### 0.2 단축 채택 사유

본 검토는 다음 단축 합의 충분 조건 모두 충족:

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (cross-reference 강화 + 부록 C 신설 한정, ADR-008 결정 본문 변경 0건) | ✅ |
| 직전 합의 (ADR-013/014 후보 결정 검토, 후속 12) 패턴 답습 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **6 풀 3+1 승격 트리거 발화 0건** | ✅ §2 답습 |

### 0.3 메타 편향 인지 (G3 §4.7 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-008 작성자 + P2 v3 작성자 + ADR-013/014 후보 결정 검토자와 동일 패밀리. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘**:
1. 사후 외부 LLM 충족 — P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업
2. 격상 전 면제 — Hermes PMO 격상 *전*
3. 합의 권위 내부 변경 — 본 검토 = 후속 12 §1.1.3 + ADR-013 보류 사유 답습 = *권위 내부* 작업
4. 자기 작성 한계 명시 — 본 §0.3 + §3 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ |
| Implementation/Runtime PASS 선언 | ❌ |
| G2 / G3 / G4 Implementation PASS 선언 | ❌ |
| **ADR-013 신규 발행** | ❌ (사용자 명시 금지 — 본 부록 C 가 ADR-013 대체) |
| **ADR-014 신규 발행** | ❌ |
| ADR-008 §결정 본문 변경 (Option B / 6 차단조건 / 단계 마이그레이션) | ❌ (cross-reference 강화 한정) |
| 실 runtime code / migration script / hook 구현 | ❌ |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |

---

## 1. 사용자 명시 7 항목 분류 (ADR-008 부록 C 갱신 범위)

### 1.1 항목 1 — P2 v3 Design Adoption 이후 Hermes PMO activation 별도 결정 명시

부록 C 본문에 다음 명시:

> P2 v3 (`hermes-adoption-design-v3.md`) 정식 채택 (2026-05-09 후속 6) = **Design Adoption only** — Hermes PMO Activation 미발생. PMO Activation 은 본 부록 C §C.6 절차 답습 *별도 결정* 영역.

**권위 출처**: P2 v3 §0 헤더 + §2 Non-Activation Clause.

### 1.2 항목 2 — Hermes PMO 격상 전 12 조건 체크리스트 참조

P2 v3 §2.6.1 12 조건 PMO 격상 체크리스트 cross-reference + 본 부록 C 에 enumerate:

| # | PMO 격상 조건 | 권위 출처 |
|---|------|----|
| 1 | G1b Implementation/Runtime PASS | ADR-008 부록 B + R-7 SOP §7.3 |
| 2 | GP-1 (G1b 흡수) Implementation/Runtime PASS | G2 §3 |
| 3 | GP-2 ~ GP-6 Implementation/Runtime PASS | G2 §4~§8 + Implementation 별도 합의 |
| 4 | G3 runtime hooks/wrappers + Hermes 변조 차단 매트릭스 runtime | G3 §1~§7 + ADR-012 §2.12 |
| 5 | G4 migration round-trip PASS + JSONL writer + 11 필드 schema 활성 | G4 §4.5 + §4.6 + ADR-012 §2.10 |
| 6 | ADR-012 evidence protection CI | ADR-012 §10.2 별도 PR |
| 7 | ADR-009 T1~T4 trigger detection task | ADR-009 §3.1~§3.4 분기별 별도 합의 |
| 8 | Provider Liquidity 5-way Layer 1~5 runtime 활성 | C-H 별도 합의 + ADR-009 C-N §5 + ADR-012 §원칙 5/6 |
| 9 | 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 | 합의 시점 별도 |
| 10 | **인간 전문 리뷰 (Human-in-the-loop)** | P2 v3 §11.1 + §2.6 단계 5.5 |
| 11 | 사용자 명시 격상 결정 | 합의 시점 별도 |
| 12 | **ADR-008 본문 Hermes PMO 격상 절차 추가 PR** | **본 부록 C** (현 발행 — ADR-013 대체) |

### 1.3 항목 3 — 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 필요 조건 명시

본 부록 C §C.3 본문에 명시:

> Hermes PMO 격상은 다음 조건 모두 충족 시에만 발생:
> - 외부 LLM 2개 (예: GPT-5.x + Gemini cross-vendor) 또는 외부 LLM 1개 + 인간 전문 리뷰
> - **인간 전문 리뷰 (Human-in-the-loop)** 의무 (P2 v3 §11.1 + Gemini 사고모델 §7.10 #3 직접 답습)
> - 사용자 명시 격상 결정

본 조건은 P2 v3 §11 변경 절차 + §2.6.1 PMO 격상 체크리스트 답습.

### 1.4 항목 4 — 사용자 명시 결정 없이는 PMO 격상 불가

부록 C §C.4 본문에 명시:

> Hermes PMO 격상은 *자동 발생 절대 금지* (ADR-011 §2.4 T3 위반). 사용자 명시 결정 + 외부 LLM 2 + 인간 전문 리뷰 + 4 게이트 Implementation/Runtime PASS evidence + Adoption decision commit + Evidence Ledger entry 모두 충족 시에만 발생.

권위 출처: ADR-011 §2.4 T3 + ADR-012 §원칙 9 + ADR-009 C-N §2.3 + P2 v3 §11.1 + §2.6.1.

### 1.5 항목 5 — Implementation/Runtime PASS 와 Design/Governance PASS 분리

부록 C §C.5 본문에 명시:

| 영역 | Design/Governance PASS | Implementation/Runtime PASS |
|------|----|----|
| G1b | (해당 없음) | ✅ 2026-05-07 |
| G2 GP-1 | ✅ | ✅ (G1b 흡수) |
| G2 GP-2 ~ GP-6 | ✅ 2026-05-09 | ⏳ Pending |
| G3 운영 구현 | ✅ 2026-05-09 | ⏳ Pending |
| G4 migration / round-trip | ✅ 2026-05-09 | ⏳ Pending |
| ADR-012 CI enforcement | (해당 없음) | ⏳ Pending |
| Hermes PMO Activation | ❌ Not authorized | ❌ Not authorized — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM + 인간 전문 리뷰 + 사용자 명시 결정 후 |

**합산**: Implementation/Runtime PASS 합산 = **1/4 (G1b 만)**. P2 v3 정식 채택 = *Design Adoption only*, Implementation PASS 미발생.

### 1.6 항목 6 — ADR-013 현 시점 발행 보류 사유 참조

부록 C §C.6 본문에 명시:

> ADR-013 (Hermes PMO Activation 영구 권위) 신규 발행은 *현 시점 보류* (`docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` §1.1.3 답습). 사유: P2 v3 §2.6 + §11.1 + §2.6.1 + 본 부록 C + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 = **8 권위 layer 중첩 답습 충족**.
>
> 발행 시점 후보 (조건부, 별도 합의 + 풀 3+1 + 외부 LLM 1+ 의무):
> - (a) Hermes PMO 격상 적격성 검토 시점 (4 게이트 모두 Implementation/Runtime PASS 후)
> - (b) 영구 ADR 권위 정착 사용자 결정 시점
> - (c) 외부 LLM 권고 발생 시 (cross-vendor 의견 추가 권고)

### 1.7 항목 7 — ADR-009 C-N / ADR-011 / ADR-012 / G2/G3/G4 cross-reference 보강

본 부록 C §C.7 + §관련 문서에 cross-reference 매트릭스:

| 권위 | cross-reference 영역 |
|----|----|
| ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위) + §5 (Provider Liquidity 5-way Layer 1 모법 ADR) | 본 부록 C §C.4 자동 격상 금지 + §C.5 5-way Multi-layer Defense Layer 1 |
| ADR-011 §2.3 (Hermes ≠ root of trust 영구 권위) + §2.4 (T1/T2/T3) | 본 부록 C §C.4 T3 자동 금지 + §C.5 권위 위계 |
| ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목) + §원칙 5 (Provider Liquidity 5-way Layer 5) + §원칙 9 (자동 정책 변경 금지 / prev_hash BLOCK) | 본 부록 C §C.5 변조 차단 + §C.4 자동 정책 변경 금지 |
| G2 §1.2.6 P10 (Evidence Forgery 정식 등록) | 본 부록 C §C.5 Evidence Integrity |
| G3 §1.3 + §5 (Evidence decision principle: PASS 성립 4 요건) + §2.5 #11 + §4.5 + §2.2 #20 (Hermes 변조 차단) | 본 부록 C §C.5 Evidence decision + 변조 차단 |
| G4 §4.2 (11 필드) + §4.4 (Layer 1~5 hash chain) + §4.6 (Tier-based round-trip) | 본 부록 C §C.5 Migration round-trip PoC |
| P2 v3 §2 (Hermes PMO 구조) + §2.6 (격상 절차 7 단계) + §2.6.1 (12 조건 체크리스트) + §11.1 (인간 전문 리뷰 의무화) + §10.1 + §10.2 | 본 부록 C 전체 |

---

## 2. 6 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **Hermes PMO 격상 절차 자체 변경** | P2 v3 §2.6 + §2.6.1 권위 답습, 본 부록 C = *cross-reference 강화* 한정. 절차 변경 0건 | ❌ 0 |
| 2 | **Human review 의무 수준 변경** | P2 v3 §11.1 + §2.6 단계 5.5 권위 답습. *Human-in-the-loop 1회 이상* 의무 그대로, 변경 0건 | ❌ 0 |
| 3 | **기존 P2 v3 §2.6.1 12 조건 완화** | 본 부록 C §C.2 = P2 v3 §2.6.1 직접 답습 (12 조건 enumerate). 완화 0건, 강화 0건 | ❌ 0 |
| 4 | **ADR-008 Hermes 도입 결정 자체 변경** | ADR-008 §결정 (Option B / 6 차단조건 / 단계 마이그레이션) 변경 0건. 본 부록 C = *부록 추가* 한정 | ❌ 0 |
| 5 | **Implementation/Runtime PASS 로 오해될 표현 발생** | 본 부록 C §C.5 = Design/Governance PASS ↔ Implementation Pending 분리 매트릭스 명시 + Hermes PMO Activation = "Not authorized" 명시 | ❌ 0 |
| 6 | **Hermes PMO 격상 선언으로 읽힐 위험** | 본 부록 C §C.1 첫 줄 = "본 부록 C 는 Hermes PMO 격상 선언이 *아니다* — 격상 *cross-reference* + *조건 명시* 한정" 명시. P2 v3 §2 Non-Activation Clause cross-reference 강화 | ❌ 0 |

→ **6/6 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

---

## 3. 메타 편향 자기진단

### 3.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-008 작성자 + P2 v3 작성자 + ADR-013/014 후보 결정 검토자와 동일 컨텍스트 패밀리. 자기 작성 산출 자기 검토 한계 인지.

### 3.2 본 한계의 청산 (G3 §4.7 답습)

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 — 본 검토 = ADR-008 부록 C 신설 (cross-reference 강화) 한정, 별도 외부 LLM 회수 *불필요* |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 부록 C 자체가 *격상 전 cross-reference 강화* 영역 |
| 3 | 합의 권위 내부 변경 | 본 검토 = ADR-013/014 후보 결정 검토 (후속 12) §1.1.3 + ADR-013 보류 사유 답습 = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §3 명시 |

### 3.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 7 항목 + 6 풀 3+1 트리거 + 6 금지 사항 모두 §0 + §1 + §2 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 7 항목 분류 + §2 6 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.4 (Hermes PMO 격상 = T3 자동 금지 답습) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1 (수단 = ADR-008 부록 C 신설 / 목적 = ADR-013 대체 + 권위 정착) |
| 5 | 본 검토가 *하지 않는* 것 명시 (§0.4 + §4.2) | ✅ 명시 |

### 3.4 본 단축 합의가 *하지 않는* 것

§4.2 답습.

---

## 4. 결론

```
✅ APPROVE (단축 합의, Reviewer-only) — ADR-008 부록 C 신설 (Hermes PMO Activation Cross-Reference) 적격
```

본 결론은 **ADR-008 본문 갱신 PR (부록 C 신설)** 의 *cross-reference 강화 + ADR-013 대체* 한정. **결정 내용 변경 0건**.

### 4.1 본 합의가 *발생시키는* 것

- ✅ ADR-008 부록 C 신설 (사용자 명시 7 항목 답습) — Hermes PMO Activation Cross-Reference + P2 v3 §2.6.1 12 조건 체크리스트 + ADR-013 보류 사유 + cross-reference 매트릭스
- ✅ ADR-013 신규 발행 *대체* 권위 정착 (사용자 명시 답습)
- ✅ ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 + P2 v3 cross-reference 강화
- ✅ Hermes PMO 격상 *조건* 명시 강화 (격상 *발생* 0건)

### 4.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ G2 / G3 / G4 Implementation PASS 자동 선언
- ❌ **ADR-013 신규 발행** (사용자 명시 금지 — 본 부록 C 대체)
- ❌ **ADR-014 신규 발행**
- ❌ ADR-008 §결정 본문 변경 (Option B / 6 차단조건 / 단계 마이그레이션 모두 변경 0건)
- ❌ 실 runtime code / migration script / hook 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ P2 v3 §2.6.1 12 조건 완화 또는 강화 (변경 0건)

### 4.3 다음 진입점 (사용자 결정 영역)

본 검토 APPROVE → ADR-008 부록 C 신설 별도 commit + housekeeping → 다음 작업 (사용자 결정 영역):

1. **G2 GP-2~GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수** (다음 진입점 후보 #1) — 각 별도 합의 (Implementation 영역)
2. **ADR-010 / ADR-011 후속 보강 필요 여부 확인** (다음 진입점 후보 #2)
3. **Hermes PMO 격상 적격성 검토** (다음 진입점 후보 #3) — 4 게이트 모두 Implementation/Runtime PASS 후 (사용자 명시 답습 = "보류")

---

**합의 commit 권위**: 본 commit (`docs(review): record ADR-008 PMO activation cross-reference appendix short consensus APPROVE`)
**본 commit + ADR-008 부록 C 신설 commit + housekeeping commits = 본 세션 후속 13 (ADR-008 본문 갱신 PR) 완료**
**다음 세션 진입점**: G2 GP-2~GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수 또는 ADR-010 / 011 후속 보강 확인 또는 Hermes PMO 격상 적격성 검토 보류 (사용자 명시 결정)
