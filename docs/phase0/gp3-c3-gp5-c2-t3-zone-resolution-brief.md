# GP-3 진입 C-3 / GP-5 진입 C-2 ("T3 영역 별도 풀 3+1") condition row 갱신 (해소 선언) Brief (DRAFT)

> **본 brief = GP-3 MVP-1 진입 합의 condition C-3 + GP-5 MVP-1 진입 합의 condition C-2 ("T3 영역 별도 풀 3+1") 의 *해소 여부* 판정 + condition row 갱신 *합의 진입 전 정비* (DRAFT)** — Backlog #3 T3 영역 4 진입 단위 (α/β/γ-1/γ-2) 풀 3+1 합의 모두 발효 (`2e9d46b`) 이후, 두 condition 이 요구한 "T3 영역 별도 풀 3+1" 이 충족되었는지 evidence 매핑 + 갱신 형태 정비 한정.
>
> ⚠️ **핵심 정밀 판정**: GP-3 C-3 (3 항목 AR-2/Vault HSM/Tier-2-3 catalog 모두 별도 풀 3+1 완료) = **해소 가능** / GP-5 C-2 (3 항목 中 AR-2 + Tier-2/3 vendor 완료, **facade real 본문 P1 v2 = Backlog #4 미진입**) = **부분 해소만 가능**.
>
> 본 brief 의 어떤 §도 그 자체로 (i) **condition row 갱신 *합의 보고서 작성* / commit / push**, (ii) **C-3 / C-2 *해소 발효***, (iii) **GP-3/GP-5 MVP-1 진입 합의 (`3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` / `...-gp5-mvp1-entry.md`) *본문 변경***, (iv) **MVP-1 exit 발효 / GP-3 5/5 / GP-5 5/5 선언 / MVP-2 자동 진입**, (v) **T3 영역 4 진입 단위 (α/β/γ-1/γ-2) 합의 *결과 재변경*** (수단 채택 / hard-block 발효 / Vault HSM 구현 / 보류 발효), (vi) **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언**, (vii) Backlog #4 (P1 v2 facade real 본문) 자동 진입 / Group I 자동 진입, (viii) governance-preconditions.md / ADR 본문 자동 갱신, (ix) **Phase α defer-lockdown 변경**, (x) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (γ-2 합의 후 옵션 (D) 답습 — GP-3 C-3 / GP-5 C-2 해소 선언 brief)
**상태**: DRAFT (사용자 명시 승인 *전*, 합의·commit·push 0건)
**관계**: Backlog #3 T3 4 진입 단위 합의 (α `2026-05-14` / β `aa8a29a` / γ-1 `9b1f8cd` / γ-2 `2e9d46b`) 발효 후속 — 본문 변경 0건 + condition 해소 판정 *직전* 정비
**상위 권위**:
- GP-3 MVP-1 진입 합의 = `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (Reviewer-only 단축 — **C-3 "T3 영역 별도 풀 3+1": AR-2 / Vault HSM / Tier-2/3 catalog 확장**)
- GP-5 MVP-1 진입 합의 = `docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` (Reviewer-only 단축 — **C-2 "T3 영역 별도 풀 3+1": AR-2 / facade real 본문 P1 v2 / Tier-2/3 vendor 확장**, C-3 = G5-4 P1 v2 facade real 본문 별도 합의)
- Backlog #3 T3 4 진입 단위 합의 = α (`3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`) + β (`...-2026-05-20-backlog3-groupbeta-catalog-policy.md`) + γ-1 (`...-groupgamma1-st1-hermes-perm.md`) + γ-2 (`...-groupgamma2-st4-vault-hsm.md`)
- follow-up brief = `backlog3-t3-zone-followup-brief.md` (`79c8ad6`, §2 GP-3 C-3/GP-5 C-2 직결 매핑)
- ADR-011 §2.4 T3 영역 / ADR-011 §2.1 (a)~(d) [+(e) 합의 패턴] / 5 영구 핵심 제약

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "d 로 진행해주세요" (= γ-2 합의 §8 옵션 (D) = GP-3 C-3 / GP-5 C-2 condition row 갱신 합의 (해소 선언) 진입)

### 0.2 본 brief 가 *하는* 것

1. C-3 / C-2 원문 + 구성 항목 정밀 확인 (§1)
2. Backlog #3 T3 4 진입 단위 합의 ↔ C-3/C-2 구성 항목 evidence 매핑 (§2)
3. **해소 판정**: GP-3 C-3 = 해소 / GP-5 C-2 = **부분 해소** (facade real 본문 P1 v2 = Backlog #4 미진입) (§3)
4. "해소" 의미 명확화 — *별도 풀 3+1 process 충족* ≠ T3 items 채택/구현 (§4)
5. 합의 형태 권고 (Reviewer-only 단축 적격성 vs 풀 3+1) (§5)
6. 제안 condition row 갱신 (GP 진입 합의 본문 변경 0건 — 새 갱신 합의가 권위 source) (§6)
7. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§7)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

- ❌ **condition row 갱신 합의 보고서 작성 / commit / push** (본 brief = untracked DRAFT 한정)
- ❌ **C-3 / C-2 *해소 발효*** (해소 = 갱신 합의 + 사용자 명시 별도 단계)
- ❌ **GP-3/GP-5 MVP-1 진입 합의 (`...2026-05-12...`) *본문 변경*** (A-1 보수적 반영 chain 답습 — 새 갱신 합의가 권위 source)
- ❌ **MVP-1 exit 발효 / GP-3 5/5 / GP-5 5/5 선언 / MVP-2 자동 진입**
- ❌ **T3 4 진입 단위 (α/β/γ-1/γ-2) 합의 *결과 재변경*** (수단 채택 / hard-block 발효 / Vault HSM 구현 / 보류 발효 / γ-2 DEFER 변경)
- ❌ **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언**
- ❌ **Backlog #4 (P1 v2 facade real 본문) 자동 진입 / Group I 자동 진입**
- ❌ governance-preconditions.md / ADR 본문 자동 갱신
- ❌ **Phase α defer-lockdown 변경** (별개 트랙 — 충돌 0건)
- ❌ 5 영구 핵심 제약 / Provider Liquidity 5-way 약화
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계 — staged cycle)

### 0.4 본 brief 의 권위 한계

본 brief = **C-3/C-2 해소 판정 + condition row 갱신 합의 *진입 전 정비* DRAFT 한정**. 본 brief 가 발생시키는 *유일한* 효과 = **해소 판정 정비 답습 한정** (Layer 0.5 가이드). 해소 *발효* + condition row 갱신 = 별도 합의 + 사용자 명시.

---

## 1. C-3 / C-2 원문 + 구성 항목 (정밀 확인)

### 1.1 GP-3 진입 C-3

| 항목 | 내용 |
|----|----|
| 출처 | `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (Reviewer-only 단축 합의 APPROVE WITH CONDITIONS) |
| 원문 | **C-3 T3 영역 별도 풀 3+1** |
| 구성 항목 (line 56) | **T3 영역 진입 = (i) AR-2 branch protection + (ii) Vault HSM + (iii) Tier-2/3 catalog 확장** → 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| 요구 본질 | 위 3 항목이 *별도 풀 3+1* 거버넌스 process 를 거칠 것 (GP entry Reviewer-only 합의에서 *결정하지 않고* 분리) |

### 1.2 GP-5 진입 C-2

| 항목 | 내용 |
|----|----|
| 출처 | `3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` (Reviewer-only 단축 합의 APPROVE WITH CONDITIONS) |
| 원문 | **C-2 T3 영역 별도 풀 3+1** |
| 구성 항목 (line 57) | **T3 영역 진입 = (i) AR-2 branch protection + (ii) facade real 본문 P1 v2 + (iii) Tier-2/3 vendor 확장** → 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| 관련 | GP-5 C-3 = "G5-4 P1 v2 facade real 본문 별도 합의" (line 169, `g2-gp5-poc2-import-linter-implementation.md` §8 TR-1 답습) — facade real 본문 = Backlog #4 영역 중복 추적 |

---

## 2. Backlog #3 T3 4 진입 단위 합의 ↔ C-3/C-2 구성 항목 evidence 매핑

| C-3/C-2 구성 항목 | 별도 풀 3+1 합의 | 발효 | process 충족 |
|----|----|----|----|
| **AR-2 branch protection** (C-3 i / C-2 i) | Group α (`3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`) | ✅ `2026-05-14` 3/3 만장일치 APPROVE WITH CONDITIONS | ✅ |
| **Tier-2/3 catalog 확장** (C-3 iii) | Group β (`...-backlog3-groupbeta-catalog-policy.md`) | ✅ `aa8a29a` 3/3 만장일치 APPROVE WITH CONDITIONS | ✅ |
| **Tier-2/3 vendor 확장** (C-2 iii) | Group β (동일 — T-5 β + Tier-2/3 일반) | ✅ `aa8a29a` 3/3 | ✅ |
| **Vault HSM** (C-3 ii) | Group γ-2 (`...-backlog3-groupgamma2-st4-vault-hsm.md`) | ✅ `2e9d46b` 3/3 만장일치 BLOCK/DEFER (MVP-6 보류) | ✅ |
| **facade real 본문 P1 v2** (C-2 ii) | Backlog #4 (P1 v2 facade real 본문) | ⏳ **미진입** (별도 영역 — GP-5 C-3 / Backlog #4) | ❌ |

**보조 답습**: Group γ-1 (C-5b ST-1 Hermes upstream chmod, `9b1f8cd`) = GP-3 Secret Hygiene Defense in depth (ST-1) 영역 — C-3 의 3 구성 항목에 *직접* 포함되진 않으나 (C-3 = AR-2/Vault HSM/Tier-2/3), T3 zone 완주를 보강. ST-4 Vault HSM 은 GP-3 entry §94 "ST-4 Vault HSM = Operational Readiness 영역" 답습 = C-3 (ii) 직접 대응.

---

## 3. 해소 판정 (synthesis — 발효 아님)

### 3.1 GP-3 C-3 = **해소** (3/3 구성 항목 별도 풀 3+1 완료)

| 구성 항목 | process 충족 |
|----|----|
| (i) AR-2 branch protection | ✅ Group α |
| (ii) Vault HSM | ✅ Group γ-2 |
| (iii) Tier-2/3 catalog 확장 | ✅ Group β |

→ **GP-3 C-3 의 3 구성 항목 모두 별도 풀 3+1 거버넌스 process 충족** → **해소 가능** (process 요구 충족).

### 3.2 GP-5 C-2 = **부분 해소** (2/3 구성 항목 완료)

| 구성 항목 | process 충족 |
|----|----|
| (i) AR-2 branch protection | ✅ Group α |
| (ii) facade real 본문 P1 v2 | ❌ **Backlog #4 미진입** (별도 영역) |
| (iii) Tier-2/3 vendor 확장 | ✅ Group β |

→ **GP-5 C-2 = 부분 해소** (AR-2 + Tier-2/3 vendor 충족 / facade real 본문 P1 v2 = Backlog #4 미진입 잔존). **완전 해소 ❌** — facade real 본문 P1 v2 가 별도 풀 3+1 (또는 GP-5 C-3 답습 별도 합의) 을 거쳐야 GP-5 C-2 완전 해소.

### 3.3 ⚠️ 비대칭 핵심

> GP-3 C-3 ≠ GP-5 C-2 — 두 condition 의 구성 항목이 다름. GP-3 C-3 = {AR-2, Vault HSM, Tier-2/3 catalog} (Backlog #3 T3 zone 내부 3개). GP-5 C-2 = {AR-2, facade real 본문 P1 v2, Tier-2/3 vendor} — **facade real 본문 P1 v2 = Backlog #3 T3 zone 외부 (Backlog #4)**. 따라서 Backlog #3 T3 4 단위 완료로 **GP-3 C-3 = 해소 / GP-5 C-2 = 부분 해소만**. 본 brief 는 이 비대칭을 *과대 선언하지 않음* (GP-5 C-2 완전 해소 선언 = 금지).

---

## 4. "해소" 의미 명확화 (별도 풀 3+1 process 충족 ≠ T3 items 채택/구현)

> C-3/C-2 가 요구한 것 = "T3 영역 *별도 풀 3+1*" — 즉 *거버넌스 process* (GP entry Reviewer-only 합의에서 결정하지 않고, 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시로 분리). **해소 = 이 process 가 충족됨** (별도 풀 3+1 가 *실제로* 가동됨), *T3 items 의 채택/구현/발효가 아님*.

| T3 진입 단위 | 별도 풀 3+1 결과 | 해소 의미 |
|----|----|----|
| Group α (AR-2) | APPROVE WITH CONDITIONS (수단 적격성 권고) | process 충족 — 실 branch protection 활성화 = Backlog #6 + 사용자 명시 별도 |
| Group β (Tier-2/3) | APPROVE WITH CONDITIONS (정책 frame 적격 / hard-block = Evidence PASS 후) | process 충족 — 실 catalog 확장 = Evidence PASS + 별도 합의 |
| Group γ-2 (Vault HSM) | BLOCK/DEFER (MVP-6 보류) | process 충족 — 실 Vault HSM 구현 = MVP-6 + Operational Readiness 별도 |

→ **해소 = process 요구 충족** (별도 풀 3+1 가동 완료). 각 T3 item 의 *실 채택/구현/발효* 는 여전히 별도 단계 (β = Evidence PASS / α = Backlog #6 / γ-2 = MVP-6 보류). 해소 선언이 T3 items 실 채택을 *의미하지 않음* 을 명문화 의무.

---

## 5. 합의 형태 권고 (Reviewer-only 단축 적격성 vs 풀 3+1)

### 5.1 본 갱신의 성격

본 condition row 갱신 = **완료된 4 풀 3+1 합의를 *반영* 하는 거버넌스 status 갱신** — 새 T3 결정 0건 / 새 수단 결정 0건 / T3 items 채택 0건. C-3/C-2 의 *process 충족 사실* 을 기록.

### 5.2 형태 후보 비교

| 형태 | 적격성 | 근거 |
|----|----|----|
| **(가) Reviewer-only 단축 합의** ⭐ 권고 후보 | ✅ 적격 후보 | 새 T3 결정 0건 (status 반영 한정) + GP entry 합의 자체가 Reviewer-only 단축 + Layer D condition satisfaction 선례 답습 (C-1/C-2 Satisfied 별도 commit). 풀 3+1 트리거 (T3 자동 진입 / 5 영구 핵심 제약 약화 / 수단 재결정) 발화 0건 |
| (나) 풀 3+1 | 가능 (보수적) | GP entry condition + ADR-011 §2.4 T3 영역 cross-reference → 신중 시. 단 본 갱신 = T3 *결정* 이 아닌 *완료 반영* → 풀 3+1 트리거 미발화 |

### 5.3 권고

**(가) Reviewer-only 단축 합의 적격 후보** — 단, 사용자 명시 결정 영역. 본 갱신이 (i) T3 영역 *새 결정* 0건 + (ii) 4 풀 3+1 합의 *반영* 한정 + (iii) GP-5 C-2 *부분 해소* 정밀 표기 (과대 선언 방지) 조건 충족 시 단축 적격. 풀 3+1 선택도 사용자 결정 시 정당.

---

## 6. 제안 condition row 갱신 (GP 진입 합의 본문 변경 0건 — 새 갱신 합의가 권위 source)

> A-1 보수적 반영 chain 답습: GP-3/GP-5 MVP-1 진입 합의 (`...2026-05-12...`) *본문 변경 0건* + 새 갱신 합의 보고서가 권위 source (Layer D condition satisfaction 패턴 답습).

| condition | 현 상태 | 제안 갱신 상태 | 근거 |
|----|----|----|----|
| **GP-3 진입 C-3** | ⏳ 미해소 ("T3 영역 별도 풀 3+1") | ✅ **해소** (Resolved) | AR-2 (α) + Vault HSM (γ-2) + Tier-2/3 catalog (β) 3/3 별도 풀 3+1 완료 |
| **GP-5 진입 C-2** | ⏳ 미해소 ("T3 영역 별도 풀 3+1") | ⚠️ **부분 해소** (Partially Resolved) | AR-2 (α) + Tier-2/3 vendor (β) 완료 / facade real 본문 P1 v2 = Backlog #4 미진입 잔존 |

**갱신 caveat (명시 의무)**: (1) 해소 = 별도 풀 3+1 process 충족 (T3 items 채택/구현 아님) / (2) GP-5 C-2 = 부분 해소만 (facade real 본문 P1 v2 별도) / (3) GP entry 합의 본문 변경 0건 / (4) MVP-1 exit 발효 ≠ 본 갱신 (GP-3 5/5 + GP-5 5/5 별도) / (5) γ-2 DEFER 결과 변경 0건.

---

## 7. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|----|----|----|
| **(A)** | 본 brief 그대로 승인 → **condition row 갱신 합의 진입** (형태 = §5.3 권고 Reviewer-only 단축 또는 사용자 명시 풀 3+1) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 brief 승인 → commit (`docs/phase0/gp3-c3-gp5-c2-t3-zone-resolution-brief.md`) *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (D) | 본 brief 보류 → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief** | Group I |
| (E) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 합의 / commit / push = 사용자 명시 승인 후 별도 단계.

---

## 8. 한 단락 요약

Backlog #3 T3 영역 4 진입 단위 (α `2026-05-14` AR-3/AR-2 + β `aa8a29a` Tier-2/3 catalog·vendor + γ-1 `9b1f8cd` C-5b ST-1 + γ-2 `2e9d46b` Vault HSM ST-4) 풀 3+1 합의 모두 발효 이후, GP-3 진입 condition C-3 + GP-5 진입 condition C-2 ("T3 영역 별도 풀 3+1") 의 해소 여부 판정 + condition row 갱신 *합의 진입 전 정비* DRAFT. 정밀 판정 = **GP-3 C-3 (구성 항목 AR-2/Vault HSM/Tier-2-3 catalog 3/3 모두 별도 풀 3+1 완료) = 해소 / GP-5 C-2 (AR-2 + Tier-2/3 vendor 완료, facade real 본문 P1 v2 = Backlog #4 미진입) = *부분 해소만***. 두 condition 의 구성 항목 비대칭 (GP-5 C-2 가 Backlog #3 T3 zone 외부의 facade real 본문 P1 v2 = Backlog #4 를 포함) 으로 GP-5 C-2 완전 해소 = 과대 선언 금지. "해소" 의미 = C-3/C-2 가 요구한 *별도 풀 3+1 거버넌스 process 충족* (별도 풀 3+1 가동 완료) 한정 — T3 items 의 실 채택/구현/발효 아님 (β = Evidence PASS 후 / α = Backlog #6 / γ-2 = MVP-6 보류). 합의 형태 = Reviewer-only 단축 합의 적격 후보 (새 T3 결정 0건 + 4 풀 3+1 반영 한정 + GP entry 합의 자체 Reviewer-only + Layer D condition satisfaction 선례), 단 사용자 명시 결정 영역. GP-3/GP-5 MVP-1 진입 합의 본문 변경 0건 (A-1 보수적 반영 chain — 새 갱신 합의가 권위 source). 본 brief = 해소 판정 정비 DRAFT 한정 — condition row 갱신 합의 보고서 작성 / commit / push / C-3·C-2 해소 발효 / GP entry 합의 본문 변경 / MVP-1 exit 발효 / GP-3 5/5·GP-5 5/5 선언 / T3 4 단위 합의 결과 재변경 / Operational Readiness PASS / Hermes PMO 격상 / Backlog #4·Group I 자동 진입 / Phase α defer-lockdown 변경 모두 0건이며, 모든 *결정* (해소 발효 포함) 은 별도 합의 (사용자 명시 승인 후).

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
condition row 갱신 합의 보고서 작성 / commit / push / C-3·C-2 해소 발효 / GP-5 C-2 완전 해소 과대 선언 / GP-3·GP-5 MVP-1 진입 합의 (`...2026-05-12...`) 본문 변경 / MVP-1 exit 발효 / GP-3 5/5·GP-5 5/5 선언 / MVP-2 자동 진입 / T3 4 진입 단위 (α/β/γ-1/γ-2) 합의 결과 재변경 (수단 채택 / hard-block 발효 / Vault HSM 구현 / γ-2 DEFER 변경) / Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언 / Backlog #4 (facade real 본문 P1 v2) 자동 진입 / Group I 자동 진입 / governance-preconditions.md·ADR 본문 자동 갱신 / Phase α defer-lockdown 변경 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화 / 본 brief 자체의 합의 자동 진입.
