# ADR-008 / 010 / 011 본문 갱신 PR 묶음 *범위 결정* 검토 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 ("우선은 Reviewer-only 단축 검토로 범위 결정을 진행 ... 6 트리거 1+ 발화 시 풀 3+1 승격")
**합의 일자**: 2026-05-09 (후속 9 — ADR-008/010/011 갱신 PR 묶음 범위 결정)
**검토 대상**: ADR-008 (`docs/decisions/ADR-008-hermes-adoption-decision.md`, 195 줄) + ADR-010 (`docs/decisions/ADR-010-sqlcipher-vault-key-management.md`, 169 줄) + ADR-011 (`docs/decisions/ADR-011-means-vs-ends-redaction.md`, 266 줄) — **갱신 범위 결정** (실 본문 갱신은 본 검토 APPROVE *후* 별도 PR/commit, 사용자 명시 답습)
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — 3 ADR 갱신 = 단순 cross-reference 갱신 영역, 결정 내용 변경 0건. 단축 합의 적격, 단일 PR 묶음 권고**

---

## 0. 사전 점검

### 0.1 가동 사유

P2 v3 Adopted (2026-05-09 후속 6) + P2 v2 Archived (2026-05-09 후속 7) + system-identity-prequel.md Archived (2026-05-09 후속 8) 후속 — **P2 v3 §9.2 별도 PR 우선순위 #3 ~ #5 답습** ("ADR-008 / 010 / 011 본문 갱신 PR 묶음").

**사용자 명시 결정 답습** (2026-05-09 후속 8 후속):
- 작업명 = "ADR-008 / ADR-010 / ADR-011 본문 갱신 PR 묶음 범위 결정"
- 목적 = "P2 v3가 Adopted 되었고, P2 v2와 system-identity-prequel이 Archived 되었으므로, 기존 ADR들이 현재 권위 상태를 정확히 참조하도록 갱신"
- 작업 단계 = **본문 수정 X, 범위 결정만** (사용자 명시 답습)
- 검토 형태 = Reviewer-only 단축 검토 우선
- 6 풀 3+1 승격 트리거 1+ 발화 시 풀 3+1 승격

### 0.2 단축 채택 사유

본 검토는 다음 단축 합의 충분 조건 모두 충족:

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (3 ADR 모두 결정 변경 0건, cross-reference 갱신 한정) | ✅ §1 답습 |
| 직전 합의 (P2 v2 archive 단축 + prequel archive 단축) 패턴 답습 | ✅ 동일 검토 패턴 |
| ADR-011 §2.4 T2/T3 분류 (cross-reference 갱신 = 권위 내부 변경) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **6 풀 3+1 승격 트리거 발화 0건** | ✅ §2 답습 (6/6 트리거 0 발화) |

### 0.3 메타 편향 인지 (G3 §4.7 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-008 / 010 / 011 작성자와 동일 패밀리. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘** (G3 §4.7.2 답습):
1. **사후 외부 LLM 충족** — P2 v3 정식 채택 (2026-05-09 후속 6) cross-vendor 외부 LLM 2건 + ADR-012 발행 (2026-05-09 후속 3 PR-2) 외부 LLM 2건 권위 *내부* 작업. 본 검토는 *cross-reference 갱신* 한정 — 별도 외부 LLM 회수 *불필요*
2. **격상 전 면제** — Hermes PMO 격상 *전*
3. **합의 권위 내부 변경** — 본 검토 = P2 v3 §9.2 #3 + ADR-012 §12.4 + ADR-009 C-N §9.4 답습 = *권위 내부* 작업
4. **자기 작성 한계 명시 의무** — 본 §0.3 + §3 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ |
| Implementation/Runtime PASS 선언 | ❌ |
| G2 / G3 / G4 Implementation PASS 선언 | ❌ |
| 실 runtime code / migration script / hook 구현 | ❌ |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |
| **3 ADR 본문 수정** (본 검토 = 범위 결정만, 본문 수정은 본 검토 APPROVE *후* 별도 PR/commit) | ❌ 사용자 명시 답습 |
| **3 ADR 결정 내용 변경** (Option B 채택 / Vault HSM + Shamir / 수단/목적 분리 모두 변경 0건) | ❌ §1 답습 |

---

## 1. 사용자 명시 6 항목 분류 (3 ADR 갱신 범위)

### 1.1 ADR-008 에 반드시 반영해야 할 내용

#### 1.1.1 갱신 영역 enumeration

| # | 갱신 영역 | 갱신 유형 |
|---|----|----|
| **A1** | §관련 문서 — `hermes-adoption-design.md` | "(P2 v2, **Archived** 2026-05-09 후속 7)" 표기 추가 |
| **A2** | §관련 문서 — `hermes-adoption-design-v3.md` 신규 추가 | "(P2 v3, **Adopted — Design Adoption only** 2026-05-09 후속 6, 후속 권위)" 신규 row 추가 |
| **A3** | §관련 문서 — ADR-009 (C-N 갱신) cross-reference 추가 | "(C-N 갱신 2026-05-09 후속 4 — P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR)" |
| **A4** | §관련 문서 — ADR-011 cross-reference 추가 (현재 부록 B 에만 명시) | "(수단/목적 분리 원칙 — 본 ADR-008 R1 specific Amendment 권위 근거)" |
| **A5** | §관련 문서 — **ADR-012 신규 cross-reference 추가** | "(Evidence Ledger Protection — Hermes 차단조건 #2 JSONL export 표준 + ADR-009 C-N + G4 §4 hash chain 보강 권위, 2026-05-09 후속 3 PR-2 신규 발행)" |
| **A6** | §관련 문서 — G2 / G3 / G4 정식 산출 cross-reference 추가 | "G2 (`governance-preconditions.md`, Design/Governance Gate PASS Bundled 2026-05-09) + G3 (`hermes-not-root-of-trust-runtime.md`, 동일) + G4 (`provider-agnostic-memory-skill-design.md`, 동일 + §4 hash chain 보강 PR-2)" |
| **A7** | §결정 §6 차단조건 #2 (JSONL export 표준) cross-reference 추가 (선택) | ADR-012 §1.4 + G4 §4.2 mandatory reference cross-reference (P2 v3 §1.6 + §6.7 답습) |
| **A8** | §결정 §6 차단조건 #4 (provider 어댑터 추상화) cross-reference 추가 (선택) | ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) cross-reference |
| **A9** | §부록 B Amendment §B.6 정식 충족 절차 cross-reference 추가 (선택) | G1b PASS 승격 (2026-05-07) + G2 GP-1 흡수 cross-reference |

**ADR-008 결정 내용 변경 0건** — 6 차단조건 + Option B 채택 + 단계 마이그레이션 모두 변경 없음. **단순 cross-reference 갱신 영역**.

**Hermes PMO 격상 절차 추가**: P2 v3 §2.6 + §11.1 + §2.6.1 권위 답습 — ADR-008 본문에 *별도 §추가 0건* (P2 v3 §2.6 cross-reference 만 충분, §관련 문서 A2 답습으로 자동).

### 1.2 ADR-010 에 반드시 반영해야 할 내용

#### 1.2.1 갱신 영역 enumeration

| # | 갱신 영역 | 갱신 유형 |
|---|----|----|
| **A10** | §맥락 §11 / §관련 문서 §166 — `hermes-adoption-design.md` (P2 v2) | "(P2 v2, **Archived** 2026-05-09 후속 7)" 표기 추가 |
| **A11** | §관련 문서 — `hermes-adoption-design-v3.md` 신규 추가 | "(P2 v3, **Adopted — Design Adoption only** 2026-05-09 후속 6, 후속 권위 — §6 G4 + §10.2 Archive Migration Note 답습)" |
| **A12** | §관련 문서 — **ADR-012 신규 cross-reference 추가** | "(Evidence Ledger Protection — Evidence Ledger DB secret 처리 cross-reference, ADR-012 §원칙 5 Layer 답습)" |
| **A13** | §결정 §핵심 메커니즘 또는 §주의 사항 — Evidence Ledger DB secret 처리 cross-reference 추가 (선택) | ADR-012 §원칙 5 (Provider Liquidity 5-way Layer 5 — Evidence 형식 차원 provider-neutral 강제) cross-reference. **Evidence Ledger entry 가 secret 평문 포함 가능 시 GP-1 SQLCipher trigger 보호 범위 명시 의무** (ADR-012 §1.4 + 외부 LLM 2 C-1 답습) |

**ADR-010 결정 내용 변경 0건** — Vault HSM + Shamir SSS 3-of-3 + 90일 자동 회전 + dual-key 운영 + PGP 봉인 백업 + 시간별 incremental + 일일 full + sample restore 분기 1회 모두 변경 없음. **단순 cross-reference 갱신 영역**.

### 1.3 ADR-011 에 반드시 반영해야 할 내용

#### 1.3.1 갱신 영역 enumeration

| # | 갱신 영역 | 갱신 유형 |
|---|----|----|
| **A14** | §8.1 상위 권위 — `system-identity-prequel.md` 인용 | "(**Archived** 2026-05-09 후속 8, 본 ADR §2.3 / §2.4 영구 권위 승격 직접 명시 답습 — prequel §3 / §6 → 본 ADR §2.3 / §2.4)" 표기 추가 |
| **A15** | §8.2 갱신 대상 — `hermes-adoption-design.md` (P2 v2) | "(P2 v2, **Archived** 2026-05-09 후속 7)" 표기 추가 |
| **A16** | §8.2 / §8.3 — `hermes-adoption-design-v3.md` 신규 추가 | "(P2 v3, **Adopted — Design Adoption only** 2026-05-09 후속 6 — 본 ADR §2.1 / §2.2 / §2.3 / §2.4 모두 답습 권위 발행)" 신규 row 추가 |
| **A17** | §8.5 후속 작업 R-4 ~ R-7 — 각 작업 ✅ 완료 표기 | R-4 / R-4.1 / R-5 / R-6 / R-7 = 모두 **✅ 완료** (2026-05-06 ~ 2026-05-07 Part 1) — 작성 예정 → 작성 완료 |
| **A18** | §8.5 후속 작업 신규 추가 — **G1b PASS 승격** (2026-05-07) | "G1b PASS = R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only — Phase 1 acceptance PASS 선언" cross-reference 추가 |
| **A19** | §8.5 후속 작업 신규 추가 — **G2 / G3 / G4 Design/Governance Gate PASS** (2026-05-09 후속 1) | 옵션 3 통합 풀 3+1 + 외부 LLM 2건 cross-reference + GP-1 ~ GP-6 / G3 / G4 정식 산출 등록 |
| **A20** | §8.5 후속 작업 신규 추가 — **ADR-012 발행** (2026-05-09 후속 3 PR-2) | "Evidence Ledger Protection — 본 ADR §2.1 (a)~(d) + (e) 5조건 패턴 답습 + §2.3 Hermes ≠ root of trust 답습 (ADR-012 §2.12 변조 차단 매트릭스 4항목) + §2.4 T3 답습 (ADR-012 §원칙 9)" |
| **A21** | §8.5 후속 작업 신규 추가 — **ADR-009 C-N 갱신** (2026-05-09 후속 4) | "P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR (Layer 1 = ADR-009 §5)" cross-reference |
| **A22** | §8.5 후속 작업 신규 추가 — **G2 §1.2.6 P10 정식 등록** (2026-05-09 후속 5) | "Evidence Forgery 정식 위반 경로 — 본 ADR §2.3 + ADR-012 §2.12 답습" cross-reference |
| **A23** | §8.5 후속 작업 신규 추가 — **P2 v3 정식 채택** (2026-05-09 후속 6) | "Design Adoption only — 본 ADR §2.3 + §2.4 직접 답습 + §10 Normative Constraints + §10.2 Archive Migration Note" |
| **A24** | §8.5 후속 작업 신규 추가 — **P2 v2 / system-identity-prequel Archived** (2026-05-09 후속 7 + 후속 8) | "옵션 A 최소 침습 채택 — 5 영구 핵심 제약 보호 강도 HIGH 5/5 유지" cross-reference |
| **A25** | §3 R-4 ~ R-7 모법 역할 표 — 각 작업 ✅ 완료 표기 (선택, A17 답습) | A17 와 통합 |

**ADR-011 결정 내용 변경 0건** — §2.1 수단/목적 분리 / §2.2 G1a/G1b 분리 / §2.3 Hermes ≠ root of trust / §2.4 T1/T2/T3 모두 변경 없음 (영구 권위 답습). **단순 cross-reference 갱신 영역**.

### 1.4 단순 cross-reference 갱신 vs 결정 내용 변경 분류

| ADR | 결정 내용 변경 | cross-reference 갱신 |
|----|----|----|
| **ADR-008** | ❌ 0건 (Option B / 6 차단조건 / 단계 마이그레이션 모두 변경 없음) | ✅ §관련 문서 9 항목 (A1~A9) |
| **ADR-010** | ❌ 0건 (Vault HSM + Shamir SSS / 90일 회전 / dual-key 등 모두 변경 없음) | ✅ §관련 문서 + §결정 cross-reference 4 항목 (A10~A13) |
| **ADR-011** | ❌ 0건 (§2.1 / §2.2 / §2.3 / §2.4 모두 영구 권위 답습) | ✅ §8.1 / §8.2 / §8.5 후속 작업 12 항목 (A14~A25) |

→ **3 ADR 모두 단순 cross-reference 갱신 영역** (총 25 항목). **결정 내용 변경 0건**.

### 1.5 단축 합의 vs 풀 3+1

**단축 합의 적격성** (사용자 명시 6 트리거 검증 §2 답습):

- 결정 내용 변경 0건 (§1.4 답습) → 풀 3+1 승격 트리거 #1 / #2 / #3 모두 0 발화
- 5 영구 핵심 제약 약화 0건 (cross-reference 갱신은 *권위 보강* 영역) → 트리거 #4 0 발화
- Hermes PMO 격상 오해 0건 (P2 v3 §2 Non-Activation Clause + §11.1 인간 리뷰 의무화 cross-reference) → 트리거 #5 0 발화
- Implementation/Runtime PASS 오해 0건 (P2 v3 §3.1.4 Implementation Pending 표 cross-reference) → 트리거 #6 0 발화

→ **6/6 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정 (실 ADR 본문 갱신 PR/commit 시점에도 동일 평가).

### 1.6 ADR-012 / P2 v3 / G2 / G3 / G4 와의 참조 관계

#### 1.6.1 권위 위계 매트릭스 (3 ADR 갱신 후)

```
헌법 (Constitution)
  > ADR
    > ADR-008 (Hermes 도입 결정 — Option B 채택)
       └─→ 부록 B Amendment (R-3 시점, 2026-05-06) — ADR-011 권위 답습
       └─→ §관련 문서 갱신 (cross-reference) — A1~A9 영역
    > ADR-009 (자체 Adapter v2.0 진입조건 — C-N 갱신, 2026-05-09 후속 4)
       └─→ §5 Provider Liquidity 5-way Multi-layer Defense Layer 1 모법 ADR
    > ADR-010 (SQLCipher Vault HSM 키 관리)
       └─→ §관련 문서 갱신 (cross-reference) — A10~A13 영역
    > **ADR-011 (수단/목적 분리 원칙 — 모법 ADR)**
       └─→ §2.1 (a)~(d) 4조건 — ADR-012 §4 (a)~(e) 5조건 답습
       └─→ §2.3 Hermes ≠ root of trust — ADR-012 §2.12 변조 차단 매트릭스 4항목 답습
       └─→ §2.4 T1/T2/T3 — ADR-012 §원칙 9 답습
       └─→ §8.5 후속 작업 갱신 — A17~A25 영역
    > **ADR-012 (Evidence Ledger Protection — 2026-05-09 후속 3 PR-2 신규 발행)**
       └─→ §1.4 cross-reference (헌법 8조 P1 변종 / Provider Liquidity / 메타포 회피 / G3 §5 / G4 §4.2/§4.4/§4.6 / ADR-008 차단조건 #2 / ADR-010 / ADR-011 §2.1/§2.3/§2.4)
  > SDD
    > P2 v3 (Hermes Adoption Design v3 — Adopted Design Adoption only, 2026-05-09 후속 6)
       └─→ §7 ADR 매트릭스 (ADR-008 / 009 / 010 / 011 / 012 cross-reference)
       └─→ §10 Normative Constraints + §10.2 Archive Migration Note
    > G2 (Governance Preconditions — Design/Governance Gate PASS Bundled, 2026-05-09)
       └─→ §1.2.6 P10 (Evidence Forgery 정식 등록, 2026-05-09 후속 5)
       └─→ §2 6 GP (GP-1 ~ GP-6) — A6 cross-reference
    > G3 (Hermes ≠ Root of Trust Runtime — Design/Governance Gate PASS Bundled)
       └─→ §1.3 + §5 (Evidence decision principle)
       └─→ §2.5 + §4.5 + §2.2 #20 (Hermes 변조 차단 매트릭스 4항목)
    > G4 (Provider-agnostic Memory/Skill — Design/Governance Gate PASS Bundled + §4 PR-2 보강)
       └─→ §4.2 11 필드 schema + §4.4 hash chain + §4.6 round-trip
  > Hermes (현 미활성 — P2 v3 §2 Non-Activation Clause)
  > Worker Agents
```

#### 1.6.2 cross-reference 의무 매트릭스 (25 항목 합산)

| 출처 | 답습 의무 |
|----|----|
| ADR-008 → ADR-009 C-N (A3) | Provider Liquidity 5-way Layer 1 모법 ADR |
| ADR-008 → ADR-011 (A4) | 부록 B Amendment 권위 근거 |
| ADR-008 → ADR-012 (A5) | 차단조건 #2 (JSONL export) + Evidence Ledger Protection mandatory reference |
| ADR-008 → P2 v2 Archived (A1) + P2 v3 Adopted (A2) | 후속 권위 |
| ADR-008 → G2/G3/G4 (A6) | 정식 산출 |
| ADR-010 → P2 v2 Archived + P2 v3 Adopted (A10/A11) | 후속 권위 |
| ADR-010 → ADR-012 (A12) | Evidence Ledger DB secret 처리 |
| ADR-011 → prequel Archived (A14) | §2.3/§2.4 영구 권위 승격 명시 |
| ADR-011 → P2 v2 Archived + P2 v3 Adopted (A15/A16) | 후속 권위 |
| ADR-011 → R-4 ~ R-7 + G1b PASS + G2/G3/G4 + ADR-012 + ADR-009 C-N + G2 §1.2.6 P10 + P2 v3 + Archive (A17~A24) | §8.5 후속 작업 ✅ 완료 등록 |

→ **3 ADR 갱신 = ADR-012 / P2 v3 / G2 / G3 / G4 / ADR-009 C-N / archive 권위 모두 cross-reference 답습 의무**.

---

## 2. 6 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

본 §2 는 사용자 명시 6 풀 3+1 승격 트리거 검증 — **0건 발화 시 단축 합의 적격, 1건이라도 발화 시 풀 3+1 승격 의무**.

| # | 트리거 | 본 ADR-008/010/011 갱신 | 발화 |
|---|----|----|----|
| 1 | **ADR-008 Hermes 도입 결정 자체 변경** | §결정 (Option B 채택) + §6 차단조건 + §단계 마이그레이션 모두 *변경 0건* — A1~A9 = cross-reference 갱신 한정 | ❌ 발화 0 |
| 2 | **ADR-010 키 관리 원칙 변경** | §결정 (Vault HSM + Shamir SSS 3-of-3 + 90일 회전 + dual-key + PGP 백업 + sample restore) *변경 0건* — A10~A13 = cross-reference 갱신 한정 | ❌ 발화 0 |
| 3 | **ADR-011 수단/목적 분리 원칙 변경** | §2.1 수단/목적 분리 / §2.2 G1a/G1b 분리 / §2.3 Hermes ≠ root of trust / §2.4 T1/T2/T3 모두 *영구 권위 답습 변경 0건* — A14~A25 = cross-reference + ✅ 완료 표기 갱신 한정 | ❌ 발화 0 |
| 4 | **5 영구 핵심 제약 약화 가능성** | cross-reference 갱신 = *권위 보강* 영역 (ADR-012 + ADR-009 C-N + G2/G3/G4 정식 산출 + archive 권위 추가). 5 영구 핵심 제약 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) 모두 강화 (ADR-009 §5 5-way 모법 + ADR-012 §원칙 5/6/9 + P2 v3 §10.1 + §10.2 cross-reference 추가) | ❌ 발화 0 |
| 5 | **Hermes PMO 격상 오해 가능성** | A2 (P2 v3 Adopted "Design Adoption only" 명시) + A24 (Archive 옵션 A — Hermes PMO 격상 자동 처리 0건) + A23 (P2 v3 §2 Non-Activation Clause + §11.1 인간 전문 리뷰 의무화 cross-reference). PMO 격상 오해 0건 | ❌ 발화 0 |
| 6 | **Implementation/Runtime PASS 오해 가능성** | A18 (G1b PASS = Implementation/Runtime PASS) + A19 (G2/G3/G4 = Design/Governance Gate PASS Bundled, GP-2~GP-6 = Implementation Pending 명시) + A23 (P2 v3 §3.1.4 Implementation Pending 표 cross-reference). Implementation PASS 오해 0건 | ❌ 발화 0 |

→ **6/6 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

---

## 3. PR 묶음 형태 권고

### 3.1 옵션 비교

| 옵션 | 정체성 | 장점 | 단점 |
|-----|------|------|------|
| **옵션 1 (사용자 명시 답습 + 본 검토 권고)** | 3 ADR 단일 PR (단축 합의 + 본문 갱신 동시) | (+) cross-reference drift 차단 (Agent A R-8 답습) / (+) 합의 비용 1회 / (+) git history 단일 commit 추적 단순 / (+) 25 항목 동시 흡수 | (-) PR diff 분량 ↑ (3 ADR 합산 ~50~70 줄 갱신) |
| 옵션 2 | 3 ADR 별도 PR (각 단축 합의) | (+) 작은 diff | (-) 합의 3회 / (-) cross-reference drift 위험 / (-) ADR-008 ↔ ADR-011 ↔ ADR-012 cross-reference 정합 검증 비용 ↑ |
| 옵션 3 | 본 검토 후 ADR-008 + ADR-010 단일 PR + ADR-011 별도 PR (2 PR 분기) | (+) ADR-011 (모법 ADR) 의 §8.5 후속 작업 12 항목이 큰 diff → 별도 PR 정당 | (-) 옵션 2 와 유사 단점 |

### 3.2 옵션 1 권고 사유

1. **6 트리거 모두 0건 발화** (§2 답습) → 옵션 1 단축 합의 적격
2. **Agent A R-8 답습** (cross-reference drift 차단 — 동일 PR 묶음 의무, P2 v3 정식 채택 합의 §5.2 답습)
3. **PR-2 합의 §5.5 답습** (ADR-012 + G4 §4 보강 동일 PR commit 권고와 동일 패턴)
4. **사용자 명시 답습** (작업명 = "ADR-008 / ADR-010 / ADR-011 본문 갱신 PR 묶음")
5. **합의 비용 ↓** (단축 합의 1회 + 본문 갱신 PR 1회 = 합산 2 commit)

### 3.3 옵션 1 적용 본문 갱신 영역 (본 검토 *후* 별도 PR/commit, 사용자 명시 답습)

본 검토 APPROVE → 다음 별도 PR/commit 으로 진행 권고:

```
[ADR-008 / 010 / 011 본문 갱신 PR (사용자 결정 시점 별도 진행)]
1. ADR-008 본문 갱신 (9 항목 — A1~A9):
   - §관련 문서: P2 v2 Archived 표기 + P2 v3 Adopted 신규 row + ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 cross-reference 추가
   - §6 차단조건 #2 / #4: ADR-012 / ADR-009 C-N cross-reference (선택)
   - 부록 B Amendment §B.6 정식 충족 절차: G1b PASS + G2 GP-1 cross-reference (선택)

2. ADR-010 본문 갱신 (4 항목 — A10~A13):
   - §맥락 §11 / §관련 문서 §166: P2 v2 Archived 표기
   - §관련 문서: P2 v3 Adopted 신규 row + ADR-012 cross-reference 추가
   - §결정 §주의 사항: ADR-012 §원칙 5 (Evidence Ledger DB secret 처리) cross-reference (선택)

3. ADR-011 본문 갱신 (12 항목 — A14~A25):
   - §8.1 상위 권위: prequel Archived 표기
   - §8.2 갱신 대상: P2 v2 Archived 표기 + P2 v3 Adopted 신규 row
   - §8.5 후속 작업 갱신: R-4 ~ R-7 ✅ 완료 + G1b PASS + G2/G3/G4 PASS + ADR-012 발행 + ADR-009 C-N + G2 §1.2.6 P10 + P2 v3 + Archive 8 항목 신규 등록
```

분량 추정: ADR-008 ~30 줄 + ADR-010 ~15 줄 + ADR-011 ~50 줄 = 합산 ~95 줄 갱신 (3 ADR 합산 ~630 줄 대비 ~15% 추가). 결정 내용 변경 0건 — *cross-reference 보강* 만.

---

## 4. 메타 편향 자기진단

### 4.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-008 / 009 / 010 / 011 / 012 작성자 + P2 v3 + G2 / G3 / G4 + archive 검토 작성자와 동일 컨텍스트 패밀리. 자기 작성 산출 자기 검토 한계 인지.

### 4.2 본 한계의 청산 (G3 §4.7 답습)

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | P2 v3 정식 채택 cross-vendor 외부 LLM 2건 + ADR-012 발행 외부 LLM 2건 권위 *내부* 작업 — 본 검토는 *cross-reference 갱신 범위 결정* 한정 |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* |
| 3 | 합의 권위 내부 변경 | 본 검토 = P2 v3 §9.2 #3 + ADR-012 §12.4 + ADR-009 C-N §9.4 답습 = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §4 명시 |

### 4.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 작업명 + 목적 + 작업 단계 + 6 항목 분류 + 6 트리거 모두 본 §0 + §1 + §2 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 6 항목 분류 + §2 6 트리거 + §3 PR 묶음 권고 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.4 (cross-reference 갱신 = T2 권위 내부 변경, 결정 변경 = T3 영역, 본 검토 = T2 한정) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1 (수단 = 3 ADR 본문 cross-reference 갱신 / 목적 = ADR ↔ ADR-012 ↔ P2 v3 ↔ G2/G3/G4 ↔ archive 권위 정합성 보강) |
| 5 | 본 검토가 *하지 않는* 것 명시 (§0.4 + §5.2) | ✅ 명시 |

### 4.4 본 단축 합의가 *하지 않는* 것

§5.2 답습.

---

## 5. 결론

```
✅ APPROVE (단축 합의, Reviewer-only) — 3 ADR 갱신 PR 묶음 적격, 옵션 1 (단일 PR 묶음) 권고
```

본 결론은 **ADR-008 / ADR-010 / ADR-011 본문 갱신 PR 묶음 *범위 결정*** 의 *6 항목 분류 PASS + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 1 단일 PR 묶음 권고* 한정. **본 검토는 본문 수정 X — 실 ADR 본문 갱신은 본 검토 APPROVE *후* 별도 PR/commit (사용자 명시 답습)**.

### 5.1 본 합의가 *발생시키는* 것

- ✅ ADR-008 / 010 / 011 갱신 **범위 결정 권위 인정** (실 본문 갱신 PR/commit 수행 적격)
- ✅ 25 cross-reference 갱신 항목 enumeration (A1~A25)
- ✅ 3 ADR 모두 단순 cross-reference 갱신 영역 분류 (결정 내용 변경 0건)
- ✅ 단축 합의 적격성 확정 (6/6 트리거 0건 발화)
- ✅ 옵션 1 (단일 PR 묶음) 권고 채택
- ✅ ADR-012 / P2 v3 / G2 / G3 / G4 / ADR-009 C-N / archive 권위 cross-reference 답습 매트릭스 명시

### 5.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 선언
- ❌ Runtime Implementation PASS 자동 선언
- ❌ G2 / G3 / G4 Implementation PASS 자동 선언
- ❌ 실 runtime code / migration script / hook 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ **3 ADR 본문 수정** (본 검토 = 범위 결정만, 본문 갱신은 별도 PR/commit)
- ❌ 3 ADR 결정 내용 변경 (Option B / Vault HSM / 수단/목적 분리 모두 변경 0건)
- ❌ 옵션 2 / 3 (별도 PR 또는 분기 PR) 자동 채택 (본 합의 = 옵션 1 권고만)

### 5.3 다음 진입점 (사용자 결정 영역)

본 검토 APPROVE → ADR-008 / 010 / 011 본문 갱신 PR/commit 별도 진행:

1. ADR-008 본문 갱신 (9 항목 — A1~A9)
2. ADR-010 본문 갱신 (4 항목 — A10~A13)
3. ADR-011 본문 갱신 (12 항목 — A14~A25)
4. 단일 PR 묶음 commit (옵션 1 권고) 또는 사용자 결정 영역
5. INDEX / CONTEXT / SESSION 갱신 (별도 commit)
6. 다음 작업 (P2 v3 §9.2 별도 PR 우선순위 답습):
   - **G2 / G3 / G4 헤더 P2 v3 cross-reference 갱신** (단축 PR)
   - **ADR-013 / 014 후보 발행 결정** (별도 합의)
   - **Hermes PMO 격상 적격성 검토** (4 게이트 Implementation/Runtime PASS + 외부 LLM + 인간 전문 리뷰 후)

---

**합의 commit 권위**: 본 commit (`docs(review): record ADR-008/010/011 update scope decision short consensus APPROVE`)
**본 commit + (사용자 결정 시) ADR 본문 갱신 PR/commit + housekeeping commits = 본 세션 후속 9 (ADR 갱신 범위 결정) 완료**
**다음 세션 진입점**: ADR-008 / 010 / 011 본문 갱신 PR/commit 진행 (옵션 1 권고) → G2 / G3 / G4 헤더 P2 v3 cross-reference 갱신 → ADR-013 / 014 후보 발행 결정 → Hermes PMO 격상 적격성 검토
