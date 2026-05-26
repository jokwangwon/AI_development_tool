# GP-3 진입 C-3 / GP-5 진입 C-2 ("T3 영역 별도 풀 3+1") condition row 갱신 합의 보고서 (Reviewer-only 단축)

> **본 합의 = GP-3 MVP-1 진입 합의 condition C-3 + GP-5 MVP-1 진입 합의 condition C-2 ("T3 영역 별도 풀 3+1") 의 *해소 status 갱신* 한정** — Backlog #3 T3 영역 4 진입 단위 (α/β/γ-1/γ-2) 풀 3+1 합의 모두 발효 (`2e9d46b`) *반영*. **Reviewer-only 단축 합의 = APPROVE — GP-3 C-3 해소 / GP-5 C-2 부분 해소**. 새 T3 *결정* 0건 (완료된 4 풀 3+1 합의의 *status 반영* 한정).
>
> 본 합의의 어떤 §도 그 자체로 (i) **GP-3/GP-5 MVP-1 진입 합의 (`3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` / `...-gp5-mvp1-entry.md`) *본문 변경***, (ii) **GP-5 C-2 *완전 해소* 과대 선언** (facade real 본문 P1 v2 = Backlog #4 미진입), (iii) **MVP-1 exit 발효 / GP-3 5/5 / GP-5 5/5 선언 / MVP-2 자동 진입**, (iv) **T3 4 진입 단위 (α/β/γ-1/γ-2) 합의 *결과 재변경*** (수단 채택 / hard-block 발효 / Vault HSM 구현 / γ-2 DEFER 변경), (v) **T3 items 의 실 채택/구현/발효** (β = Tier-2/3 catalog 실 확장 / α = branch protection 실 활성화 / γ-1 = Hermes upstream 변경 / γ-2 = Vault HSM 구현), (vi) **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언**, (vii) Backlog #4 (P1 v2 facade real 본문) / Group I 자동 진입, (viii) governance-preconditions.md / ADR 본문 자동 갱신, (ix) **Phase α defer-lockdown 변경**, (x) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (condition row 갱신 합의 진입 — resolution brief 옵션 (A) 답습)
**상태**: APPROVED (Reviewer-only 단축 합의) — 사용자 명시 승인 *전*, commit 0건
**합의 판정**: **APPROVE — GP-3 진입 C-3 = 해소 (Resolved) / GP-5 진입 C-2 = 부분 해소 (Partially Resolved)** (Reviewer-only 단축 합의)
**합의 영역**: C-3/C-2 해소 status 갱신 한정 — GP entry 합의 본문 변경 0건 + T3 items 실 채택/구현 0건
**상위 권위**:
- 진입 brief (본 합의 직접 source) = `docs/phase0/gp3-c3-gp5-c2-t3-zone-resolution-brief.md` (`2e9d46b` 이후 untracked, §3 해소 판정 + §5 형태 권고 + 옵션 (A))
- GP-3 MVP-1 진입 합의 = `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (Reviewer-only — C-3 "T3 영역 별도 풀 3+1": AR-2 / Vault HSM / Tier-2/3 catalog 확장)
- GP-5 MVP-1 진입 합의 = `docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` (Reviewer-only — C-2 "T3 영역 별도 풀 3+1": AR-2 / facade real 본문 P1 v2 / Tier-2/3 vendor 확장)
- Backlog #3 T3 4 진입 단위 합의 = α (`3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`) + β (`...-2026-05-20-backlog3-groupbeta-catalog-policy.md`) + γ-1 (`...-groupgamma1-st1-hermes-perm.md`) + γ-2 (`...-groupgamma2-st4-vault-hsm.md`)
- ADR-011 §2.4 T3 영역 / ADR-011 §2.1 (a)~(d) [+(e) 합의 패턴] / 5 영구 핵심 제약 / Layer D condition satisfaction 선례 (C-1/C-2 Satisfied 별도 commit)

---

## 0. 본 합의의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "옵션 (A)로 진행 — Reviewer-only 단축 합의"

선행 명령: "d 로 진행해주세요" (= γ-2 합의 §8 옵션 (D) = GP-3 C-3 / GP-5 C-2 condition row 갱신 합의 (해소 선언)) → resolution brief 작성 → 옵션 (A) Reviewer-only 단축 합의 진입.

### 0.2 본 합의가 *하는* 것

1. Reviewer-only 단축 합의 적격성 검증 (§1)
2. C-3/C-2 구성 항목 ↔ Backlog #3 T3 4 진입 단위 evidence 매핑 (§2)
3. 해소 판정 (GP-3 C-3 = 해소 / GP-5 C-2 = 부분 해소) (§3)
4. "해소" 의미 명확화 + condition row 갱신 (§4)
5. 합의 조건 등록 (C-T3R-1 ~ C-T3R-10) (§5)
6. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§6)
7. 메타 검증 (§7) / 합의 요약 한 단락 (§8) / 부록

### 0.3 본 합의가 *하지 않는* 것 (사용자 명시 영구 답습)

| # | 금지 | 본 합의 위반 |
|---|------|------------|
| 1 | **GP-3/GP-5 MVP-1 진입 합의 본문 변경** | 0건 (A-1 보수적 반영 chain — 새 갱신 합의가 권위 source) |
| 2 | **GP-5 C-2 *완전 해소* 과대 선언** (facade real 본문 P1 v2 = Backlog #4 미진입) | 0건 (부분 해소만 선언) |
| 3 | **MVP-1 exit 발효 / GP-3 5/5 / GP-5 5/5 선언 / MVP-2 자동 진입** | 0건 |
| 4 | **T3 4 진입 단위 합의 결과 재변경** (수단 채택 / hard-block 발효 / Vault HSM 구현 / γ-2 DEFER 변경) | 0건 |
| 5 | **T3 items 실 채택/구현/발효** (Tier-2/3 catalog 실 확장 / branch protection 실 활성화 / Hermes upstream 변경 / Vault HSM 구현) | 0건 |
| 6 | **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언** | 0건 |
| 7 | **Backlog #4 / Group I 자동 진입** | 0건 |
| 8 | **governance-preconditions.md / ADR 본문 자동 갱신** | 0건 |
| 9 | **Phase α defer-lockdown 변경** | 0건 (별개 트랙) |
| 10 | 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 | 0건 |

### 0.4 본 합의의 권위 한계

- 본 합의 = **C-3/C-2 해소 status 갱신 한정** — 완료된 4 풀 3+1 합의의 *반영* (새 T3 결정 0건).
- "해소" = C-3/C-2 가 요구한 *별도 풀 3+1 거버넌스 process 충족* — T3 items 의 실 채택/구현/발효 아님.
- GP-5 C-2 = *부분 해소만* (facade real 본문 P1 v2 = Backlog #4 미진입).
- GP entry 합의 본문 변경 0건 — 본 합의 보고서가 satisfaction 권위 source (Layer D 선례 답습).

---

## 1. Reviewer-only 단축 합의 적격성 검증

### 1.1 단축 합의 적격 기준 (8/8 충족)

| # | 기준 | 충족 |
|---|------|----|
| 1 | 새 T3 *결정* 0건 (완료된 4 풀 3+1 합의의 status *반영* 한정) | ✅ |
| 2 | 새 수단 결정 / threshold 고정 0건 | ✅ |
| 3 | T3 items 실 채택/구현/발효 0건 | ✅ |
| 4 | GP entry 합의 본문 변경 0건 (A-1 보수적 반영 chain) | ✅ |
| 5 | GP entry 합의 자체가 Reviewer-only 단축 (동일 형식 정합) | ✅ |
| 6 | Layer D condition satisfaction 선례 (C-1/C-2 Satisfied 별도 commit) 답습 | ✅ |
| 7 | evidence = 완료된 4 풀 3+1 합의 (확정적 — 추론 여지 최소) | ✅ |
| 8 | GP-5 C-2 부분 해소 정밀 표기 (과대 선언 방지) | ✅ |

### 1.2 풀 3+1 승격 트리거 (5/5 미발화)

| # | 트리거 | 발화 |
|---|------|----|
| 1 | T3 영역 *자동 진입* (새 T3 결정) | ❌ 0건 (status 반영 — T3 결정은 4 풀 3+1 에서 이미 완료) |
| 2 | 수단 *재결정* / threshold 고정 | ❌ 0건 |
| 3 | 5 영구 핵심 제약 약화 | ❌ 0건 |
| 4 | Provider Liquidity 5-way 약화 | ❌ 0건 |
| 5 | MVP-1 exit / Operational Readiness PASS / Hermes PMO 격상 | ❌ 0건 |

**합산**: 8/8 단축 적격 + 5/5 풀 3+1 트리거 미발화 → **Reviewer-only 단축 합의 적격 확정** (사용자 명시 형태 선택 답습).

---

## 2. C-3/C-2 구성 항목 ↔ Backlog #3 T3 4 진입 단위 evidence 매핑

| C-3/C-2 구성 항목 | 별도 풀 3+1 합의 | 발효 | process 충족 |
|----|----|----|----|
| **AR-2 branch protection** (C-3 i / C-2 i) | Group α | ✅ `2026-05-14` 3/3 만장일치 APPROVE WITH CONDITIONS | ✅ |
| **Tier-2/3 catalog 확장** (C-3 iii) | Group β | ✅ `aa8a29a` 3/3 만장일치 APPROVE WITH CONDITIONS | ✅ |
| **Tier-2/3 vendor 확장** (C-2 iii) | Group β (동일) | ✅ `aa8a29a` 3/3 | ✅ |
| **Vault HSM** (C-3 ii) | Group γ-2 | ✅ `2e9d46b` 3/3 만장일치 BLOCK/DEFER (MVP-6 보류) | ✅ |
| **facade real 본문 P1 v2** (C-2 ii) | Backlog #4 (= GP-5 C-3 영역) | ⏳ **미진입** | ❌ |

**보조**: Group γ-1 (C-5b ST-1, `9b1f8cd`) = GP-3 Secret Hygiene Defense in depth (ST-1) — C-3 3 구성 항목에 직접 포함되진 않으나 T3 zone 완주 보강. (C-3 (ii) Vault HSM 은 GP-3 entry §94 "ST-4 Vault HSM = Operational Readiness 영역" 답습 = γ-2 직접 대응.)

---

## 3. 해소 판정

### 3.1 GP-3 진입 C-3 = **해소 (Resolved)**

| 구성 항목 | process 충족 |
|----|----|
| (i) AR-2 branch protection | ✅ Group α |
| (ii) Vault HSM | ✅ Group γ-2 |
| (iii) Tier-2/3 catalog 확장 | ✅ Group β |

→ **3/3 구성 항목 모두 별도 풀 3+1 거버넌스 process 충족 → 해소** (process 요구 충족).

### 3.2 GP-5 진입 C-2 = **부분 해소 (Partially Resolved)**

| 구성 항목 | process 충족 |
|----|----|
| (i) AR-2 branch protection | ✅ Group α |
| (ii) facade real 본문 P1 v2 | ❌ **Backlog #4 미진입** (GP-5 C-3 / Backlog #4 영역) |
| (iii) Tier-2/3 vendor 확장 | ✅ Group β |

→ **2/3 구성 항목 충족 → 부분 해소**. **완전 해소 ❌** — facade real 본문 P1 v2 가 별도 풀 3+1 (또는 GP-5 C-3 답습 별도 합의 — Backlog #4) 을 거쳐야 GP-5 C-2 완전 해소. 본 합의는 이를 *과대 선언하지 않음* (C-T3R-2).

### 3.3 비대칭 핵심

GP-3 C-3 ({AR-2, Vault HSM, Tier-2/3 catalog} — Backlog #3 T3 zone 내부 3개) ≠ GP-5 C-2 ({AR-2, facade real 본문 P1 v2, Tier-2/3 vendor} — facade real 본문 P1 v2 = Backlog #4 외부). → Backlog #3 T3 4 단위 완료로 **GP-3 C-3 = 해소 / GP-5 C-2 = 부분 해소만**.

---

## 4. "해소" 의미 명확화 + condition row 갱신

### 4.1 "해소" 의미 (process 충족 ≠ T3 items 채택/구현)

> C-3/C-2 가 요구한 것 = "T3 영역 *별도 풀 3+1*" = *거버넌스 process* (GP entry Reviewer-only 합의에서 결정하지 않고 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시로 분리). **해소 = 이 process 충족** (별도 풀 3+1 실제 가동 완료) — *T3 items 의 채택/구현/발효가 아님*.

| T3 진입 단위 | 별도 풀 3+1 결과 | 실 채택/구현 status (해소와 무관) |
|----|----|----|
| Group α (AR-2) | APPROVE WITH CONDITIONS | 실 branch protection 활성화 = Backlog #6 + 사용자 명시 별도 |
| Group β (Tier-2/3) | APPROVE WITH CONDITIONS | 실 catalog 확장 = Implementation Evidence PASS + 별도 합의 |
| Group γ-2 (Vault HSM) | BLOCK/DEFER (MVP-6 보류) | 실 Vault HSM 구현 = MVP-6 + Operational Readiness 별도 |

### 4.2 condition row 갱신 (GP entry 합의 본문 변경 0건 — 본 합의가 권위 source)

| condition | 현 상태 | **갱신 상태** | 근거 |
|----|----|----|----|
| **GP-3 진입 C-3** | ⏳ 미해소 | ✅ **해소 (Resolved)** | AR-2 (α) + Vault HSM (γ-2) + Tier-2/3 catalog (β) 3/3 별도 풀 3+1 완료 |
| **GP-5 진입 C-2** | ⏳ 미해소 | ⚠️ **부분 해소 (Partially Resolved)** | AR-2 (α) + Tier-2/3 vendor (β) 완료 / facade real 본문 P1 v2 = Backlog #4 미진입 잔존 |

> Layer D condition satisfaction 패턴 답습 — GP-3/GP-5 MVP-1 진입 합의 (`...2026-05-12...`) 본문 변경 0건 + 본 합의 보고서가 satisfaction 권위 source.

---

## 5. 합의 조건 (C-T3R-1 ~ C-T3R-10)

| # | 조건 |
|---|----|
| **C-T3R-1** | **GP-3 진입 C-3 = 해소 (Resolved)** — AR-2 (α) + Vault HSM (γ-2) + Tier-2/3 catalog (β) 3/3 별도 풀 3+1 거버넌스 process 충족 |
| **C-T3R-2** | **GP-5 진입 C-2 = 부분 해소 (Partially Resolved)** — AR-2 + Tier-2/3 vendor 충족 / **facade real 본문 P1 v2 = Backlog #4 미진입 잔존** (완전 해소 과대 선언 금지) |
| **C-T3R-3** | **"해소" = 별도 풀 3+1 거버넌스 process 충족 한정** — T3 items 의 실 채택/구현/발효 아님 (β = Evidence PASS 후 / α = Backlog #6 / γ-2 = MVP-6 보류) |
| **C-T3R-4** | **GP-3/GP-5 MVP-1 진입 합의 본문 변경 0건** (A-1 보수적 반영 chain — 본 합의 보고서가 satisfaction 권위 source) |
| **C-T3R-5** | **T3 4 진입 단위 (α/β/γ-1/γ-2) 합의 결과 재변경 0건** (수단 채택 / hard-block 발효 / Vault HSM 구현 / γ-2 DEFER 변경 모두 0건 보존) |
| **C-T3R-6** | **MVP-1 exit ≠ 본 갱신** — GP-3 5/5 + GP-5 5/5 별도 (C-3/C-2 해소는 GP-3/GP-5 의 *한 condition* 해소일 뿐, 5/5 전체 충족 아님). MVP-1 exit 발효 = 별도 합의 + 사용자 명시 |
| **C-T3R-7** | **GP-5 C-2 완전 해소 trigger = facade real 본문 P1 v2 (Backlog #4 / GP-5 C-3) 별도 풀 3+1 발효** — 후속 영역 |
| **C-T3R-8** | **Reviewer-only 단축 합의 적격** (8/8 적격 기준 + 5/5 풀 3+1 트리거 미발화) — 새 T3 결정 0건 status 반영 한정 |
| **C-T3R-9** | **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / Backlog #4 / Group I 자동 진입 0건** + Phase α defer-lockdown 변경 0건 |
| **C-T3R-10** | **본 합의 = condition row 갱신 (해소 status) 한정** — 해소 발효는 사용자 명시 승인 + commit 후. governance-preconditions.md / ADR 본문 자동 갱신 0건 |

**합의 조건 합산**: **10 조건 등록 (C-T3R-1~C-T3R-10)**. 합산 731 → 741 (29 합의 — commit 시 발효).

---

## 6. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|----|----|----|
| **(A)** | 본 합의 그대로 승인 → 파일화 + commit + push (resolution brief + 본 합의 별도 2 commit chain) | commit + push |
| (B) | 본 합의 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 합의 그대로 승인 → 파일화 + commit *까지만* (push 보류) | commit |
| (D) | 본 합의 승인 + push → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief** | Group I |
| (E) | 본 합의 승인 + push → 세션 종료 marker | 세션 종료 |
| (F) | 본 합의 보류 → 세션 종료 | — |

### 6.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 후보: "옵션 (A)로 진행 — 본 합의 그대로 승인하고 resolution brief + 합의 별도 2 commit chain commit + push."

---

## 7. 메타 검증

| 검증 영역 | 결과 |
|--------|----|
| Reviewer-only 단축 합의 적격 | ✅ 8/8 적격 기준 + 5/5 풀 3+1 트리거 미발화 (§1) |
| C-3/C-2 evidence 매핑 | ✅ 4 진입 단위 합의 ↔ 구성 항목 매핑 (§2) |
| 해소 판정 정밀 | ✅ GP-3 C-3 = 해소 / GP-5 C-2 = 부분 해소 (과대 선언 0건) |
| GP entry 합의 본문 변경 | ✅ 0건 (A-1 보수적 반영 chain) |
| 10 합의 조건 (C-T3R-1~10) | ✅ 등록 |
| 사용자 명시 금지 10건 (§0.3) | ✅ 모두 0건 (GP entry 본문 변경 0 / GP-5 C-2 완전 해소 0 / MVP-1 exit 0 / T3 4 단위 결과 재변경 0 / T3 items 실 채택 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / Backlog #4·Group I 자동 진입 0 / Phase α defer-lockdown 변경 0) |
| 합산 합의 조건 | 731 → 741 (29 합의 — commit 시 발효) |
| **Backlog #3 T3 거버넌스 매듭** | ✅ T3 4 진입 단위 완료 + GP-3 C-3 해소 / GP-5 C-2 부분 해소 — T3 영역 process 매듭 |

---

## 8. 합의 요약 (한 단락)

Backlog #3 T3 영역 4 진입 단위 (α `2026-05-14` AR-3/AR-2 + β `aa8a29a` Tier-2/3 catalog·vendor + γ-1 `9b1f8cd` C-5b ST-1 + γ-2 `2e9d46b` Vault HSM ST-4) 풀 3+1 합의 모두 발효 *반영* → GP-3 진입 condition C-3 + GP-5 진입 condition C-2 ("T3 영역 별도 풀 3+1") condition row 갱신 = **Reviewer-only 단축 합의 APPROVE — GP-3 C-3 = 해소 (Resolved) / GP-5 C-2 = 부분 해소 (Partially Resolved)**. 정밀 판정 = GP-3 C-3 의 3 구성 항목 (AR-2=α / Vault HSM=γ-2 / Tier-2/3 catalog=β) 모두 별도 풀 3+1 process 충족 → 해소 / GP-5 C-2 의 3 구성 항목 中 AR-2 (α) + Tier-2/3 vendor (β) 충족, **facade real 본문 P1 v2 = Backlog #4 미진입** 잔존 → 부분 해소만 (완전 해소 과대 선언 금지). "해소" = C-3/C-2 가 요구한 *별도 풀 3+1 거버넌스 process 충족* 한정 — T3 items 의 실 채택/구현/발효 아님 (β = Implementation Evidence PASS 후 / α = Backlog #6 / γ-2 = MVP-6 보류). Reviewer-only 단축 합의 적격 (8/8 적격 기준 + 5/5 풀 3+1 트리거 미발화 — 새 T3 결정 0건, 완료된 4 풀 3+1 합의 status 반영 한정, GP entry 합의 자체 Reviewer-only, Layer D condition satisfaction 선례 답습). GP-3/GP-5 MVP-1 진입 합의 본문 변경 0건 (A-1 보수적 반영 chain — 본 합의 보고서가 satisfaction 권위 source). 10 합의 조건 (C-T3R-1~C-T3R-10) 등록. 본 합의 = condition row 갱신 (해소 status) 한정 — GP entry 합의 본문 변경 / GP-5 C-2 완전 해소 과대 선언 / MVP-1 exit 발효 / GP-3 5/5·GP-5 5/5 선언 / MVP-2 자동 진입 / T3 4 단위 합의 결과 재변경 / T3 items 실 채택·구현·발효 / Operational Readiness PASS / Hermes PMO 격상 / Backlog #4·Group I 자동 진입 / governance-preconditions.md·ADR 본문 자동 갱신 / Phase α defer-lockdown 변경 모두 0건이며, 해소 *발효* 는 사용자 명시 승인 + commit 후. 합산 합의 조건 731 → 741 (29 합의 — commit 시 발효). **Backlog #3 T3 영역 4 진입 단위 완료 + GP-3 C-3 해소 / GP-5 C-2 부분 해소 = T3 영역 거버넌스 process 매듭.**

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
GP-3/GP-5 MVP-1 진입 합의 (`...2026-05-12...`) 본문 변경 / GP-5 C-2 완전 해소 과대 선언 / MVP-1 exit 발효 / GP-3 5/5·GP-5 5/5 선언 / MVP-2 자동 진입 / T3 4 진입 단위 (α/β/γ-1/γ-2) 합의 결과 재변경 (수단 채택 / hard-block 발효 / Vault HSM 구현 / γ-2 DEFER 변경) / T3 items 실 채택·구현·발효 (Tier-2/3 catalog 실 확장 / branch protection 실 활성화 / Hermes upstream 변경 / Vault HSM 구현) / Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언 / Backlog #4 (facade real 본문 P1 v2) 자동 진입 / Group I 자동 진입 / governance-preconditions.md·ADR 본문 자동 갱신 / Phase α defer-lockdown 변경 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화 / 본 합의 자체의 commit·push 자동 진입.
