# Backlog #2 GP-5 1.5차 *잔여* 항목 (T-1 / T-3 / T-4 단독 + T-5 강화 + AR-3) Deferred 유지 확정 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 (옵션 (A) brief 그대로 승인 + 5/5 항목 모두 Deferred 유지 권위화 + C-6 상태 표기 *재변경 0건* + Layer D 본문 변경 0건)
**합의 일자**: 2026-05-14 후속 6
**검토 대상**: **Backlog #2 (GP-5 1.5차 보강) 中 PC-4 T2 sub 외 *잔여 5 항목* — T-1 (depcruise) 단독 / T-3 (grimp) 단독 / T-4 (ruff custom rule) 단독 / T-5 (Group A 1차/3차 custom AST scanner) 단독 강화 / AR-3 (AR-1 + AR-2 통합) — 의 *진입 적격성* + *처리 형태* + *Deferred 유지 권위화***. PC-4 T2 sub 는 이미 `78483c5` 합의로 Partially Satisfied 흡수 완료 — 본 합의 영역 외.
**보조 참조**:
- 본 합의 대상 brief = `docs/phase0/backlog2-gp5-1.5-remaining-items-brief.md` (commit `59adef3`, DRAFT 9 섹션 + 부록 A/B, 466 lines)
- 직전 합의 (PC-4 T2 sub `78483c5` Partially Satisfied) = `docs/review/3plus1-consensus-2026-05-13-pc4-t2-c5c-c6-satisfaction.md` (commit `78483c5`, APPROVE — §C-5c + §C-6 양쪽 Partially Satisfied 갱신, A-1 패턴 답습)
- 직전 합의 메타 = `28c89ab docs(context): record PC-4 T2 partial satisfaction status` (CONTEXT/INDEX/SESSION §40)
- GP-5 진입 합의 = `6808d17 docs(review): add GP-5 MVP-1 entry consensus` (APPROVE WITH CONDITIONS — C-1 1.5차 보강 영역 분리 명시)
- MVP-1 Implementation Entry = `1eab814 docs(review): approve MVP-1 implementation entry` (READY, Backlog 우선순위 권고)
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, APPROVE WITH CONDITIONS, §C-6 GP-5 1.5차 Backlog #2 Deferred 정의)
- MVP-1 roadmap deepening = `cddd22f` + `bbc05ca` + `5939c93` (mvp1.md §4.3 T-1~T-6 후보 매트릭스 + §4.5 권고 + §4.6 Rollback Trigger 10건)
- §5.5 9 sub-수단 본문 채택 = `f40423f` + `55c5b4b` (양 GP PC-3 본문 채택 — Layer B `f40423f` 발효 답습)
- 도구 PoC 답습: Group A 1차 (`tools/provider_import_scanner.py` AST 5종) / Group A 2차 (`.importlinter` + lint-imports `25605665191`) / Group A 3차 (`tools/provider_url_scanner.py` URL+모델명 `25629390384`)
- A-1 패턴 답습: `1dd1036` (§C-1) / `6fa87dc` (§C-5a) / `78483c5` (§C-5c + §C-6 부분 갱신) chain

**검토 목적**: Backlog #2 잔여 5 항목 각각의 진입 *적격성* 검토 + Deferred 유지 권위화. **본 합의 = 5 항목 모두 Deferred 유지 확정 한정** ≠ 수단 결정 / 본문 채택 / Tier-2/3 catalog 확장 / Backlog #3 자동 진입 / §C-6 상태 표기 재변경 / Layer D 본문 변경 / MVP-1 PASS 재선언 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / T3 영역 자동 진입.

**판정**: ✅ **APPROVE — Keep Backlog #2 remaining GP-5 1.5 items Deferred** (5 항목 모두 진입 부적합 확정 + Deferred 유지 권위화, Reviewer-only 단축 합의)

⚠️ **본 합의 = 5 항목 *Deferred 유지 권위화* 한정** — §C-6 = `Partially Satisfied (PC-4 T2 sub only)` 그대로 유지 (`78483c5` 합의 권위 source 유지) + Layer D 본문 변경 0건 (A-1 답습).

⚠️ **본 합의 ≠ Backlog #3 자동 진입** — AR-3 + T-5 (β) Tier-2/3 영역 *이관 권고만* — Backlog #3 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 별도 합의 영역.

⚠️ **본 합의 ≠ MVP-1 PASS 재선언** — Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지.

⚠️ **본 합의 ≠ Operational Readiness PASS (Layer E) 선언** — MVP-6 + Backlog #7 별도 영역.

⚠️ **본 합의 ≠ Hermes PMO 격상 (Layer F)** — MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무.

⚠️ **본 합의 ≠ T3 영역 자동 진입** — AR-3 (branch protection rule 변경) + T-5 (β) Tier-2/3 catalog 확장 + PC-4 T3 sub 모두 Backlog #3 별도 합의 의무.

⚠️ **PC-4 T2 sub 재처리 0건** — 이미 `78483c5` 합의로 Partially Satisfied 흡수 완료 (§C-6 = Partially Satisfied (PC-4 T2 sub only) 그대로 유지).

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-14 후속 6 — Backlog #2 GP-5 1.5차 나머지 항목 Deferred 유지 확정):

> "옵션 (A)로 진행해주세요. brief 승인 → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. Backlog #2 나머지 항목은 모두 Deferred 유지. 구현 / T3 자동 진입 / MVP-1 PASS 재선언은 하지 않음."

> "이번 brief의 핵심 결론: Backlog #2 GP-5 1.5차 나머지 항목 5개는 현 시점에서 모두 진입 부적합. T-1 / T-3 / T-4 / T-5 강화 / AR-3 = Deferred 유지. 이번 합의는 구현 진입 합의가 아니라, Deferred 유지 판단을 권위화하는 합의."

> "합의 형태: Reviewer-only 단축 합의. 이유: 7/7 풀 3+1 승격 트리거 0건 / T3 영역 자동 진입 0건 / 새 수단 채택 0건 / 도구 본문 변경 0건 / .importlinter 변경 0건 / CI workflow 변경 0건 / Node 환경 도입 0건."

> "보고서에 반드시 포함할 내용: T-1/T-3/T-4 = Deferred 유지 / T-5 강화 = Deferred 유지 / AR-3 = Deferred 유지 + Backlog #3 이관 / PC-4 T2 sub는 이미 78483c5에서 Partially Satisfied 반영 완료, 재처리 없음 / C-6은 Partially Satisfied 상태 유지 / MVP-1 PASS 재선언 없음 / Operational Readiness PASS 없음 / Hermes PMO 격상 없음 / T3 영역 자동 진입 없음."

**사용자 명시 결정 답습**:
- 검토 형태 = Reviewer-only 단축 합의
- 검토 대상 = Backlog #2 잔여 5 항목 진입 적격성 + Deferred 유지 권위화
- 판정 = **APPROVE — Keep Backlog #2 remaining GP-5 1.5 items Deferred**
- 합의 형태 = Reviewer-only 단축 합의 (`1dd1036` + `6fa87dc` + `78483c5` chain 답습)
- 반영 방식 = **A-1 답습** (Layer D 본문 변경 0건 + 직전 합의 `78483c5` 본문 변경 0건 + C-6 상태 표기 재변경 0건)
- **본 합의 범위** = 5 항목 *Deferred 유지 권위화* 한정 — 수단 결정 / 본문 채택 / Tier-2/3 catalog 확장 / Backlog #3 자동 진입 / §C-6 상태 표기 재변경 / Layer D 본문 변경 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입 **모두 불가**

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 검토 = 5 항목 *Deferred 유지* 확정 = 수단 결정 0건 + 본문 채택 0건 + ADR 본문 갱신 0건 + 도구 본문 / `.importlinter` config / `.pre-commit-config.yaml` 변경 0건 + CI workflow 변경 0건 + §5.5 9 sub-수단 본문 채택 변경 0건) | ✅ |
| 직전 합의 chain (Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독·실 구현·Cycle 1~6 / §C-5a 갱신 / 선행 단독 PC-4 brief / 통합 brief / 진입 직전 brief / 진입 권한 / 구현 진입 / Cycle 4 + fix + 메타 / §C-5c + §C-6 부분 갱신 모두 Reviewer-only) 패턴 답습 | ✅ |
| brief §6 본문 명시 답습 — "**Reviewer-only 단축 합의 적격 확정** (7/7 풀 3+1 트리거 0건 발화)" | ✅ |
| `1dd1036` + `6fa87dc` + `78483c5` (§C-1 + §C-5a + §C-5c·§C-6 갱신) A-1 패턴 본문 명시 답습 — "Layer D 합의 보고서 본문 변경 0건 + 직전 합의 본문 변경 0건 + 본 합의 보고서가 Deferred 유지 권위 source" | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — Deferred 유지 권위화 한정) | ✅ |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) | ✅ §0.1 답습 |
| **7/7 풀 3+1 승격 트리거 0건 발화** | ✅ §2 답습 |
| brief §2.1~§2.5 5 항목 모두 진입 *부적합* 판정 + mvp1.md §4.5 미채택 사유 답습 + §4.6 R-MVP1-G5-1 + R-MVP1-G5-2 답습 | ✅ §1 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독·실 구현·Cycle 1~6 / §C-5a 갱신 / 선행 단독 PC-4 brief / 통합 brief / 진입 직전 brief / 진입 권한 / 구현 진입 / Cycle 4 + fix + 메타 commit / §C-5c+§C-6 부분 갱신 합의 / Backlog #2 잔여 5 항목 검토 brief 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

**청산 매커니즘**:
1. **사후 외부 LLM 충족 보존** — 누적 cross-vendor blind 의뢰 5건 답습 — 모두 권위 *내부* 작업으로 통합
2. **격상 전 면제 보존** — Hermes PMO 격상 *전 단계*. 본 검토 = Deferred 유지 권위화 한정 — Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 미진입
3. **합의 권위 내부 변경 한정** — 본 검토 = 5 항목 Deferred 유지 *결과 행사* — 권위 *내부 행사* 작업
4. **자기 작성 한계 명시** — 본 §0.3 + §5 명시
5. **A-1 패턴 답습** (Layer D 본문 변경 0건 + 직전 합의 `78483c5` 본문 변경 0건 + C-6 상태 표기 재변경 0건 + 본 합의 보고서가 Deferred 유지 권위 source)
6. **Deferred 유지 권위화 한정** (수단 결정 0건 + 본문 채택 0건 + Tier-2/3 확장 0건 + Backlog #3 진입 0건 + C-6 상태 표기 재변경 0건 + Layer D 본문 변경 0건 + Layer E~F 미진입 + ADR 본문 갱신 0건)
7. **외부 LLM cross-vendor blind 의뢰 미진입** — 7/7 단축 합의 적격 트리거 0건 발화 + 직전 합의 chain 일관성 + mvp1.md §4.5 미채택 사유 답습 = 결정적 검증 (외부 추론 의존성 0건)

### 0.4 비검토 대상 (사용자 명시 4 금지 + 추가 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| **MVP-1 PASS *재선언*** | ❌ (Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지) |
| **Operational Readiness PASS (Layer E)** *선언* | ❌ (MVP-6 + Backlog #7 별도 영역) |
| **Hermes PMO 격상 (Layer F)** | ❌ (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| **T3 영역 *자동 진입*** | ❌ (AR-3 = branch protection rule 변경 = T3 진입 + T-5 (β) Tier-2/3 catalog 확장 = T3 진입 + PC-4 T3 sub 모두 0건 — Backlog #3 보존) |
| **PC-4 T2 sub *재처리*** | ❌ (이미 `78483c5` 합의로 Partially Satisfied 흡수 완료 — 재처리 0건) |
| **§C-6 상태 표기 *재변경*** | ❌ (`Partially Satisfied (PC-4 T2 sub only)` 그대로 유지 — `78483c5` 권위 source 보존) |
| **§C-5c / §C-5 전체 상태 표기 *재변경*** | ❌ (`78483c5` 권위 source 그대로 유지) |
| **Layer D 합의 보고서 본문 변경** | ❌ (A-1 답습 — `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` 본문 변경 0건) |
| **직전 합의 (`78483c5`) 본문 변경** | ❌ (A-1 chain 답습 — 본문 변경 0건) |
| T-1 / T-3 / T-4 / T-5 / AR-3 *수단 결정* / *본문 채택 commit* | ❌ (모두 Deferred 유지) |
| T-5 도구 본문 변경 (`tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) | ❌ |
| Tier-2 / Tier-3 catalog 자동 확장 (URL 10 / Model 19 보존) | ❌ |
| `.importlinter` config 본문 *변경* | ❌ (Group A 2차 답습) |
| `.pre-commit-config.yaml` 본문 *변경* / 신규 hook 추가 | ❌ (Cycle 4 `b2f99f4` + fix `3d3cd21` 답습) |
| CI workflow *변경* | ❌ (PC-3 본문 채택 답습 그대로) |
| Node 환경 도입 (T-1 depcruise 의존) | ❌ |
| **C-1 / C-2 / C-3 / C-4 / C-5a / C-5b / C-5c / C-7 / C-8 *자동 변경*** | ❌ (본 합의 = 5 항목 Deferred 유지 한정 — 다른 9 Conditions 그대로 유지) |
| **Backlog #3 (T3 영역) *자동 진입*** | ❌ (AR-3 + T-5 (β) *이관 권고만* — 진입 0건, 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무) |
| **Backlog #4 (P1 v2 facade MVP) / Backlog #6 (Runtime + CI-hook) / Backlog #7 (Operational Readiness) *자동 진입*** | ❌ |
| ADR 본문 *자동 갱신* | ❌ (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건) |
| ADR-012 §2.2 enum 정식 등록 | ❌ |
| §5.5 9 sub-수단 본문 채택 *변경* | ❌ (`f40423f` + `55c5b4b` 답습) |
| 도구 본문 변경 | ❌ |
| 외부 LLM 자동 호출 | ❌ |
| 실 API key / provider SDK / 외부 API 호출 | ❌ |

---

## 1. 검토 기준 충족 분석 (8/8)

### 1.0 brief §1~§6 결과 답습

본 합의 = brief §1~§6 결과 *행사* 한정. 새 권위 결정 0건. 본 §1 = brief §1~§6 결과 답습 확정.

### 1.1 C-6 Partially Satisfied 후 잔여 영역 정의 (brief §1)

```
C-6 (GP-5 1.5차 보강 — Backlog #2) = ✅ Partially Satisfied (PC-4 T2 sub only)  ← `78483c5` 권위 source
   PC-4 T2 sub (provider-import + provider-url-model + import-linter 3 hook)  = Satisfied  ← 본 합의 영역 외 (재처리 0건)
   T-1 단독 (depcruise)                                                          = ⏳ Deferred  ← 본 합의 §1.2
   T-3 단독 (grimp)                                                              = ⏳ Deferred  ← 본 합의 §1.3
   T-4 단독 (ruff custom rule)                                                   = ⏳ Deferred  ← 본 합의 §1.4
   T-5 단독 강화                                                                  = ⏳ Deferred  ← 본 합의 §1.5
   PC-4 T3 sub                                                                   = ⏳ Deferred (Backlog #3 T3 영역)  ← 본 합의 영역 외
   AR-3 (AR-1 + AR-2 통합)                                                       = ⏳ Deferred  ← 본 합의 §1.6 (Backlog #3 이관 명시)
```

### 1.2 T-1 (dependency-cruiser) 단독 검토 (brief §2.1)

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | Provider Liquidity 약화 (Node 환경 + npm 의존 신설) | ⚠️ 부분 |
| 2 | Python repo 정합성 저하 (`.dependency-cruiser.cjs` = JS 본문) | ✅ HIGH |
| 3 | T-2 (import-linter, PoC 채택) 와 중복 cover | ✅ HIGH |
| 4 | R-MVP1-G5-1 트리거 발화 (풀 3+1 + 도구 변경 영향 분석 의무) | ✅ HIGH |

→ **T-1 단독 = Deferred 유지** (mvp1.md §4.5 #1 답습).

### 1.3 T-3 (grimp) 단독 검토 (brief §2.2)

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | T-2 (import-linter, PoC 채택) 와 책무 중복 (import-linter 가 grimp 내부 사용) | ✅ HIGH |
| 2 | PoC 답습 충실성 저하 (Group A 2차 PoC = T-2 단독 채택) | ✅ HIGH |
| 3 | R-MVP1-G5-1 트리거 발화 | ✅ HIGH |
| 4 | 단일 source-of-truth 보존 위반 | ✅ HIGH |

→ **T-3 단독 = Deferred 유지** (mvp1.md §4.5 #2 답습).

### 1.4 T-4 (ruff custom rule) 단독 검토 (brief §2.3)

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | transitive 미커버 (ruff = file-level) → T-2 강점 손실 | ✅ HIGH |
| 2 | 책무 분담 매트릭스 7/8 cover 약화 (T-6 transitive cover 손실) | ✅ HIGH |
| 3 | R-MVP1-G5-1 트리거 발화 | ✅ HIGH |
| 4 | ruff plugin 작성 + 유지 보수 비용 | ⚠️ MEDIUM |

→ **T-4 단독 = Deferred 유지** (mvp1.md §4.5 #3 답습).

### 1.5 T-5 단독 강화 검토 (brief §2.4) — 3 하위 후보

| 하위 후보 | 내용 | 차단 요인 |
|---------|----|--------|
| (α) 자체 transitive 분석 추가 | T-2 와 중복 + R-MVP1-G5-1 발화 + Group A 1차 답습 충실성 저하 | ❌ 부적합 |
| **(β) Tier-2 / Tier-3 catalog 확장** | **T3 영역 진입** (GP-3 §3.5 R-MVP1-G3-1 + GP-5 §4.6 R-MVP1-G5-1 답습) → **Backlog #3** | ❌ 부적합 — T3 영역 |
| (γ) 추가 패턴 도입 (FP/FN) | 실 운영 evidence 의존 (Implementation Evidence PASS 미발효 시점에 의미 없음) | ❌ 부적합 (현 시점) |

→ **T-5 강화 = Deferred 유지** + (β) Backlog #3 이관 명시 + (γ) Implementation Evidence PASS 후 별도 합의 영역.

### 1.6 AR-3 (AR-1 + AR-2 통합) 검토 (brief §2.5) ⭐

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | **T3 영역 진입 = 사용자 명시 4 금지 #4 답습** | ✅ **HIGH (BLOCKING)** |
| 2 | AR-2 (branch protection rule) 본문 변경 = T3 정책 변경 | ✅ HIGH |
| 3 | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 의무 (mvp1.md §4.6 R-MVP1-G5-2 답습) | ✅ HIGH |
| 4 | Backlog #3 보존 의무 (`78483c5` 합의 §C-6 답습) | ✅ HIGH |

→ **AR-3 = Deferred 유지 + Backlog #3 이관 명시** (mvp1.md line 400 + §4.6 R-MVP1-G5-2 답습).

### 1.7 5 항목 합산 매트릭스 (brief §3)

| 항목 | 본 합의 판정 | 후속 진입 *조건* |
|----|---------|------------|
| T-1 단독 (depcruise) | ❌ Deferred 유지 | T-2 silent fail + Group A 2차 §C-7 트리거 발화 시 (mvp1.md §4.6 R-MVP1-G5-3) |
| T-3 단독 (grimp) | ❌ Deferred 유지 | T-2 deprecation / 라이선스 / `.importlinter` rule 충돌 폭증 시 |
| T-4 단독 (ruff) | ❌ Deferred 유지 | T-2 deprecation + ruff plugin 으로 transitive 우회 가능성 검증 후 |
| T-5 (α) | ❌ Deferred 유지 | T-2 가 기능적으로 부족한 영역 검출 (PoC 결과 의존) |
| T-5 (β) Tier-2/3 | ❌ Deferred 유지 + **Backlog #3 이관** | Backlog #3 T3 영역 합의 + 사용자 명시 결정 |
| T-5 (γ) 추가 패턴 | ❌ Deferred 유지 | Implementation Evidence PASS 발효 후 + 실 운영 FN evidence 수집 |
| AR-3 | ❌ Deferred 유지 + **Backlog #3 이관** | Backlog #3 T3 영역 + branch protection rule 변경 + 외부 LLM 1+ + 사용자 명시 |

→ **5/5 항목 모두 현 시점 진입 *부적합* 확정 + 후속 재진입 조건 명시**.

### 1.8 8/8 검토 기준 충족 합산

| # | 검토 기준 | 판정 |
|---|--------|------|
| 1 | C-6 Partially Satisfied 후 잔여 영역 정의 적절성 | ✅ §1.1 |
| 2 | T-1 (depcruise) 단독 진입 부적합 판정 | ✅ §1.2 |
| 3 | T-3 (grimp) 단독 진입 부적합 판정 | ✅ §1.3 |
| 4 | T-4 (ruff) 단독 진입 부적합 판정 | ✅ §1.4 |
| 5 | T-5 단독 강화 부적합 판정 (3 하위 후보 모두) | ✅ §1.5 |
| 6 | AR-3 부적합 판정 + Backlog #3 이관 명시 | ✅ §1.6 |
| 7 | 합의 단위 (5 항목 단일 bundled) + 합의 형태 (Reviewer-only) 권고 | ✅ brief §4 답습 |
| 8 | 7/7 풀 3+1 트리거 0건 발화 → Reviewer-only 적격 | ✅ §2 답습 |

**합산 = 8/8 적절** — brief §1~§6 결과 + mvp1.md §4.5 미채택 사유 답습 + §4.6 R-MVP1-G5-1 + R-MVP1-G5-2 답습 + A-1 패턴 답습 + 사용자 명시 4 금지 답습 모두 권위 근거 충실.

---

## 2. 풀 3+1 승격 트리거 검증 (7/7 0건 발화)

| # | 트리거 | 본 합의 검토 결과 |
|---|----|------------|
| 1 | 본 합의가 9 sub-수단 *외* 수단 *재결정* 권고 | ❌ 0건 발화 (5 항목 모두 Deferred 유지 — 수단 결정 0건) |
| 2 | 본 합의가 **T3 영역 *자동 진입*** 권고 | ❌ 0건 발화 (AR-3 + T-5 (β) Backlog #3 *이관 권고만* — 진입 0건 — 사용자 명시 4 금지 #4 답습) |
| 3 | 본 합의가 사용자 명시 3 결정 (α/ii/(가)) *재변경* 권고 | ❌ 0건 발화 (Cycle 4 답습 한정 — 본 합의 영역 외) |
| 4 | 본 합의가 Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 발화 (T-1 Node 환경 도입 = *부적합* 사유로 명시 — 약화 0건) |
| 5 | 본 합의가 5 영구 핵심 제약 약화 포함 | ❌ 0건 발화 (Hermes ≠ root of trust 보존 + 수단/목적 분리 보존 + 메타포 강제 금지 보존 + 단일 source-of-truth 보존 + Provider Liquidity 보존) |
| 6 | 본 합의가 **MVP-1 PASS *재선언* / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상)** 포함 | ❌ 0건 발화 (사용자 명시 4 금지 #1 + #2 + #3 답습) |
| 7 | 본 합의가 외부 LLM *없이* T3 영역 결정 권고 | ❌ 0건 발화 (T3 결정 0건 — AR-3 + T-5 (β) Backlog #3 이관) |

**합산 = 7/7 0건 발화** → Reviewer-only 단축 합의 적격 확정.

---

## 3. 5 항목 Deferred 유지 권위화 + C-6 상태 표기 재변경 0건

### 3.1 5 항목 Deferred 유지 권위화 (본 합의 권위 source)

```
T-1 단독 (depcruise)            = ⏳ Deferred (`<본 합의 commit>`)
T-3 단독 (grimp)                = ⏳ Deferred (`<본 합의 commit>`)
T-4 단독 (ruff custom rule)     = ⏳ Deferred (`<본 합의 commit>`)
T-5 단독 강화 (α/β/γ)            = ⏳ Deferred (`<본 합의 commit>`)
  ├ (α) 자체 transitive 분석 추가  = Deferred — T-2 와 중복
  ├ (β) Tier-2/3 catalog 확장      = Deferred — Backlog #3 T3 영역 이관
  └ (γ) 추가 패턴 도입             = Deferred — Implementation Evidence PASS 후 별도 영역
AR-3 (AR-1 + AR-2 통합)         = ⏳ Deferred (`<본 합의 commit>`)
                                  + Backlog #3 T3 영역 이관 명시
```

### 3.2 §C-6 상태 표기 *재변경 0건* (`78483c5` 권위 source 보존)

```
C-6 (GP-5 1.5차 보강 — Backlog #2) = ✅ Partially Satisfied (PC-4 T2 sub only) (`78483c5` 권위 source 그대로 유지)
  PC-4 T2 sub (provider-import + provider-url-model + import-linter)  = Satisfied (`78483c5`)
  T-1 / T-3 / T-4 단독                                                  = ⏳ Deferred (본 합의 권위화)
  T-5 단독 강화                                                          = ⏳ Deferred (본 합의 권위화)
  PC-4 T3 sub                                                           = ⏳ Deferred (Backlog #3 T3)
  AR-3                                                                  = ⏳ Deferred (본 합의 권위화 + Backlog #3 이관)
```

### 3.3 §C-5c / §C-5 전체 상태 표기 *재변경 0건* (`78483c5` 권위 source 보존)

```
C-5 (GP-3 1.5차 보강 — Backlog #1) = ✅ Partially Satisfied (C-5a + C-5c partial) (`78483c5` 그대로)
  C-5a (ST-2)         = ✅ Satisfied (`6fa87dc`)
  C-5b (ST-1)         = ⏳ Deferred (Backlog #3 T3)
  C-5c (PC-4)         = ✅ Partially Satisfied (T2 sub only) (`78483c5` 그대로)
```

### 3.4 Layer D 본문 변경 0건 + `78483c5` 본문 변경 0건 (A-1 chain 답습)

| 합의 보고서 | 본문 변경 |
|---------|--------|
| `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (`210c98f`) | ❌ 0건 (A-1 답습) |
| `docs/review/3plus1-consensus-2026-05-13-pc4-t2-c5c-c6-satisfaction.md` (`78483c5`) | ❌ 0건 (A-1 chain 답습) |
| `docs/review/3plus1-consensus-2026-05-13-st2-c5a-satisfaction.md` (`6fa87dc`) | ❌ 0건 |
| `docs/review/3plus1-consensus-2026-05-13-mvp1-pass-c1-k2-satisfaction.md` (`1dd1036`) | ❌ 0건 |

→ **본 합의 보고서 = 5 항목 Deferred 유지 권위 source** (다른 합의 본문 변경 0건).

---

## 4. 본 합의 발효 범위

### 4.1 본 합의가 *발생시키는* 것

| # | 영역 |
|---|------|
| 1 | T-1 단독 (depcruise) Deferred 유지 권위화 |
| 2 | T-3 단독 (grimp) Deferred 유지 권위화 |
| 3 | T-4 단독 (ruff custom rule) Deferred 유지 권위화 |
| 4 | T-5 단독 강화 (α/β/γ) Deferred 유지 권위화 |
| 5 | AR-3 (AR-1 + AR-2 통합) Deferred 유지 권위화 + Backlog #3 T3 영역 *이관 권고* (진입 0건) |
| 6 | T-5 (β) Tier-2 / Tier-3 catalog 확장 = Backlog #3 *이관 권고* (진입 0건) |
| 7 | 본 합의 보고서 = 5 항목 Deferred 유지 권위 source |
| 8 | 후속 재진입 조건 명시 (R-MVP1-G5-1 / R-MVP1-G5-2 / R-MVP1-G5-3 트리거 발화 시) |
| 9 | Reviewer-only 단축 합의 chain 답습 (A-1 sibling pattern — `1dd1036` + `6fa87dc` + `78483c5` 후속) |
| 10 | 다음 단계 = 사용자 결정 영역 (자동 진입 0건) |

### 4.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 4 금지 + 추가 답습)

| # | 영역 | 본 합의 발효 시점 위반 |
|---|------|------------------|
| 1 | **MVP-1 PASS *재선언*** | **0건 (Layer D `210c98f` 판정 = APPROVE WITH CONDITIONS 그대로 유지)** |
| 2 | **Operational Readiness PASS (Layer E)** *선언* | **0건 (MVP-6 + Backlog #7 별도 영역)** |
| 3 | **Hermes PMO 격상 (Layer F)** | **0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무)** |
| 4 | **T3 영역 *자동 진입*** | **0건 (AR-3 + T-5 (β) Backlog #3 *이관 권고만* — 진입 0건 + branch protection rule 변경 / Tier-2/3 catalog 확장 / commit signing / required check 모두 0건)** |
| 5 | **PC-4 T2 sub *재처리*** | **0건 (`78483c5` 합의 흡수 완료 — Partially Satisfied (PC-4 T2 sub only) 그대로 유지)** |
| 6 | **§C-6 상태 표기 *재변경*** | **0건 (`Partially Satisfied (PC-4 T2 sub only)` 그대로 유지 — `78483c5` 권위 source 보존)** |
| 7 | **§C-5c / §C-5 전체 상태 표기 *재변경*** | **0건 (`78483c5` 권위 source 그대로 유지)** |
| 8 | Layer D 합의 보고서 *본문 변경* | 0건 (A-1 답습) |
| 9 | 직전 합의 (`78483c5`) *본문 변경* | 0건 (A-1 chain 답습) |
| 10 | T-1 / T-3 / T-4 / T-5 / AR-3 *수단 결정* / *본문 채택 commit* | 0건 (모두 Deferred 유지) |
| 11 | T-5 도구 본문 변경 (`tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) | 0건 |
| 12 | Tier-2 / Tier-3 catalog 자동 확장 (URL 10 / Model 19 보존) | 0건 |
| 13 | `.importlinter` config 본문 *변경* | 0건 (Group A 2차 답습) |
| 14 | `.pre-commit-config.yaml` 본문 *변경* / 신규 hook 추가 | 0건 |
| 15 | CI workflow 본문 *변경* | 0건 (PC-3 본문 채택 답습 그대로) |
| 16 | Node 환경 도입 (T-1 depcruise 의존) | 0건 |
| 17 | C-1 / C-2 / C-3 / C-4 / C-5a / C-5b / C-5c / C-7 / C-8 *자동 변경* | 0건 |
| 18 | Backlog #3 (T3 영역) *자동 진입* | 0건 (AR-3 + T-5 (β) 이관 *권고만* — 별도 합의 의무) |
| 19 | Backlog #4 (P1 v2 facade MVP) / Backlog #6 (Runtime + CI-hook) / Backlog #7 (Operational Readiness) *자동 진입* | 0건 |
| 20 | ADR 본문 *자동 갱신* | 0건 |
| 21 | ADR-012 §2.2 enum 정식 등록 | 0건 |
| 22 | §5.5 9 sub-수단 본문 채택 *변경* | 0건 (`f40423f` + `55c5b4b` 답습) |
| 23 | 도구 본문 변경 (`tools/secret_scanner.py` / `tools/provider_*.py` / `tools/workflow_*.py`) | 0건 |
| 24 | Production `docker-compose.yml` *변경* | 0건 |
| 25 | Hermes upstream Dockerfile *변경* | 0건 |
| 26 | 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 27 | Provider Liquidity 5-way / 5 영구 핵심 제약 약화 | 0건 |
| 28 | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | 0건 (Cycle 4 답습 한정) |
| 29 | CONTEXT / INDEX / SESSION 메타 갱신 (본 commit ≠ 메타 — 별도 commit 분리) | 0건 |

### 4.3 본 합의 발효 후 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 후보 | 영역 |
|------|------|
| (1) | CONTEXT / INDEX / SESSION 메타 갱신 commit (별도 commit 분리 답습 — 본 합의 직후) |
| (2) | Backlog #3 T3 영역 풀 3+1 brief (AR-3 + T-5 (β) + PC-4 T3 sub + C-5b ST-1 + Vault HSM ST-4 통합 영역) |
| (3) | Backlog #6 Runtime + CI-hook implementation brief (MVP-1 Implementation Entry 권고 우선순위 1, `1eab814` 답습) |
| (4) | Backlog #4 P1 v2 facade MVP brief |
| (5) | MVP-2 진입 합의 (G2 GP-2 + G4 §4.4 Layer 4) |
| (6) | 세션 종료 |

⚠️ **본 합의 APPROVE 직후 자동 다음 단계 진입 금지** — 사용자 명시 결정 의무.

⚠️ **Backlog #3 / Backlog #4 / Backlog #6 / Backlog #7 *자동 진입* 금지** — 각각 별도 합의 의무.

---

## 5. 발효 영향 매트릭스

### 5.1 Layer + Backlog + Cycle 분리 매트릭스 (본 합의 발효 시점)

```
Layer A : Backlog #6 entry 기준 정의                       — APPROVE (f1e0b23)
Layer B : 9 sub-수단 본문 채택 + 시작 권한                 — APPROVE (f40423f + 55c5b4b)
Layer B 행사: Stage 1+3 / 2 / 4 / 5                        — 발효 (5 runs PASS)
Layer C : MVP-1 Implementation Evidence PASS              — APPROVE (6973935)
Layer D : MVP-1 PASS                                      — APPROVE WITH CONDITIONS (210c98f, 본문 변경 0건)
Backlog #5 ADR-012 event enum 정식 등록                   — APPROVE (b705370) — §C-2 Satisfied
K-2 baseline fix + §C-1 갱신                              — APPROVE (1dd1036) — §C-1 Satisfied
ST-2 §C-5a Satisfied 갱신 (γ sub-condition 분리)          — APPROVE (6fa87dc) — §C-5a Satisfied
PC-4 T2 sub Cycle 4 + fix + 메타                           — 완료 (b2f99f4 + 3d3cd21 + 5f878d6, local 6/6 PASS warm 0.482초)
§C-5c + §C-6 Partially Satisfied 갱신 (T2 sub only)       — APPROVE (78483c5, brief 3be81da + 메타 28c89ab)
■ Backlog #2 GP-5 1.5차 나머지 5 항목 Deferred 유지 확정  — APPROVE (brief 59adef3 + 본 합의 + 후속 메타 commit) ← 본 단계
§C-6 상태 표기 *재변경 0건* (`78483c5` 권위 source 보존)  — 표기 유지
C-5b ST-1                                                  — Deferred 그대로 유지 (Backlog #3 T3)
C-5c PC-4 T3 sub                                           — Deferred 그대로 유지 (Backlog #3 T3)
C-6 GP-5 1.5차 나머지 5 항목                                — Deferred 유지 권위화 (본 합의)
  ├ T-1 / T-3 / T-4 단독 / T-5 (α/γ)                       — Deferred (Backlog #2 별도)
  └ T-5 (β) Tier-2/3 / AR-3                                — Deferred (Backlog #3 이관 권고)
Layer E (Operational Readiness PASS)                       — 아직 아님 (C-3, MVP-6, Backlog #7)
Layer F (Hermes PMO 격상)                                  — 아직 아님 (C-4, MVP-6, 외부 LLM + 사람 리뷰 의무)
```

### 5.2 C-1~C-8 상태 (본 합의 발효 후)

| Condition | 상태 | 본 합의 영향 |
|----------|------|----------|
| C-1 | ✅ Satisfied (`1dd1036`) | 변경 0건 |
| C-2 | ✅ Satisfied (Backlog #5 `b705370`) | 변경 0건 |
| C-3 | ⏳ Deferred (MVP-6, Backlog #7) | 변경 0건 |
| C-4 | ⏳ Deferred (MVP-6, 외부 LLM + 사람 리뷰) | 변경 0건 |
| **C-5 (GP-3 1.5차 보강)** | ✅ Partially Satisfied (C-5a + C-5c partial) (`78483c5`) | **변경 0건 (재변경 0건)** |
| ├ C-5a (ST-2) | ✅ Satisfied (`6fa87dc`) | 변경 0건 |
| ├ C-5b (ST-1) | ⏳ Deferred | 변경 0건 (Backlog #3 T3) |
| └ C-5c (PC-4) | ✅ Partially Satisfied (T2 sub only) (`78483c5`) | 변경 0건 (재변경 0건) |
| **C-6 (GP-5 1.5차 보강)** | ✅ Partially Satisfied (PC-4 T2 sub only) (`78483c5`) | **변경 0건 (재변경 0건) — 5 항목 Deferred 유지 권위화** |
| ├ PC-4 T2 sub | ✅ Satisfied (`78483c5`) | 변경 0건 (재처리 0건) |
| ├ **T-1 / T-3 / T-4 단독** | ⏳ **Deferred 유지 권위화 (본 합의)** | Backlog #2 별도 |
| ├ **T-5 단독 강화 (α/β/γ)** | ⏳ **Deferred 유지 권위화 (본 합의)** | (β) Backlog #3 이관 명시 |
| ├ PC-4 T3 sub | ⏳ Deferred | Backlog #3 T3 |
| └ **AR-3** | ⏳ **Deferred 유지 권위화 (본 합의) + Backlog #3 이관 명시** | T3 영역 |
| C-7 | ⏳ Requires separate full 3+1 (Backlog #3) | 변경 0건 |
| C-8 | ⏳ Deferred (Backlog #4) | 변경 0건 |

**핵심**: 본 합의 = 5 항목 Deferred 유지 *권위화* — Layer D 본문 변경 0건 + `78483c5` 본문 변경 0건 + §C-6 상태 표기 *재변경 0건* + 다른 9 Conditions 그대로 유지 + Layer E·F 미진입 + Backlog #3 자동 진입 0건.

### 5.3 본 합의 행사 의무 (사용자 명시 답습)

| 항목 | 의무 |
|------|------|
| commit 분리 (3 commit) | ✅ Commit 1 (brief `59adef3`) + Commit 2 (본 합의 — 본 commit) + Commit 3 (메타 갱신 — 후속) |
| CONTEXT / INDEX / SESSION 메타 갱신 분리 | ✅ 별도 commit (다음 단계) |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 자동 진입) | ✅ §0.1 + §0.4 + §4.2 답습 |
| PC-4 T2 sub 재처리 금지 | ✅ §4.2 #5 답습 |
| C-6 상태 표기 재변경 금지 | ✅ §3.2 + §4.2 #6 답습 |
| MVP-1 PASS 재선언 금지 | ✅ §4.2 #1 답습 |
| Backlog #3 자동 진입 금지 (이관 권고만) | ✅ §4.2 #18 답습 |
| 다른 backlog 자동 진입 금지 | ✅ §4.2 #19 답습 |

---

## 6. 메타 검증

| 메타 검증 | 본 합의 |
|---------|--------|
| 사용자 명시 진입 명령 답습 (옵션 (A) + 5 항목 Deferred 유지 + C-6 Partially Satisfied 유지 + PC-4 T2 sub 재처리 없음 + 4 금지) | ✅ |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 자동 진입) | ✅ (§0.4 + §4.2 답습) |
| 8/8 검토 기준 충족 (brief §1~§6 답습 + mvp1.md §4.5 + §4.6 답습 + A-1 패턴 답습 + 풀 3+1 트리거 0건 발화) | ✅ §1.8 |
| 7/7 풀 3+1 승격 트리거 0건 발화 | ✅ §2 |
| **PC-4 T2 sub 재처리 0건** (`78483c5` 흡수 완료) | ✅ §0.4 + §4.2 #5 |
| **§C-6 상태 표기 재변경 0건** (`Partially Satisfied (PC-4 T2 sub only)` 그대로 유지) | ✅ §3.2 + §5.2 |
| **§C-5c / §C-5 전체 상태 표기 재변경 0건** | ✅ §3.3 |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| C-1~C-8 상태 답습 (5 항목 Deferred 유지 한정 — 9 Conditions 그대로) | ✅ §5.2 |
| Layer D 본문 변경 0건 (`210c98f` 그대로 유지) | ✅ (A-1 답습) |
| 직전 합의 `78483c5` 본문 변경 0건 | ✅ (A-1 chain 답습) |
| MVP-1 PASS *재선언* 0건 | ✅ |
| Operational Readiness PASS (Layer E) 선언 0건 | ✅ |
| Hermes PMO 격상 (Layer F) 0건 | ✅ |
| T3 영역 자동 진입 0건 (AR-3 + T-5 (β) Backlog #3 *이관 권고만* — 진입 0건) | ✅ |
| Backlog #3 / #4 / #6 / #7 자동 진입 0건 | ✅ |
| 수단 결정 / 본문 채택 / 도구 본문 변경 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건 | ✅ |
| Tier-2 / Tier-3 catalog 자동 확장 0건 (URL 10 / Model 19 보존) | ✅ |
| Node 환경 도입 0건 (T-1 *부적합* 사유 명시) | ✅ |
| ADR 본문 자동 갱신 0건 | ✅ |
| ADR-012 §2.2 enum 정식 등록 0건 | ✅ |
| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ |
| 5 영구 핵심 제약 보존 (Hermes ≠ root of trust / 수단·목적 분리 / 메타포 강제 금지 / 단일 source-of-truth / Provider Liquidity) | ✅ |
| 7 backlog 분리 매트릭스 답습 | ✅ |
| 자동 진입 0건 (Backlog #3 이관 권고만 + 다른 backlog / T3 / Layer E·F) | ✅ |
| 합의 권위 자기 내부 변경 한정 (외부 LLM 미진입) | ✅ |
| 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출 0건 | ✅ |

---

## 7. 본 합의 요약 (한 단락)

본 합의 는 **Backlog #2 (GP-5 1.5차 보강) 中 PC-4 T2 sub Partially Satisfied (`78483c5`) 후 *잔여 5 항목* — T-1 (depcruise) 단독 / T-3 (grimp) 단독 / T-4 (ruff custom rule) 단독 / T-5 (Group A 1차/3차 custom AST scanner) 단독 강화 / AR-3 (AR-1 + AR-2 통합) — 의 *Deferred 유지 권위화* (Reviewer-only 단축 합의)** 이다. 사용자 명시 옵션 (A) 답습 + 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) + PC-4 T2 sub 재처리 0건 + §C-6 상태 표기 재변경 0건. 8/8 검토 기준 충족 (C-6 잔여 영역 정의 / T-1 부적합 / T-3 부적합 / T-4 부적합 / T-5 (α/β/γ) 부적합 / AR-3 부적합 + Backlog #3 이관 / 합의 단위·형태 권고 / 풀 3+1 트리거 0건 발화) + **7/7 풀 3+1 트리거 0건 발화** → Reviewer-only 단축 합의 적격 확정. **5 항목 권위화 결과**: **T-1 단독 = Deferred 유지** (Node 환경 高 + T-2 중복 + R-MVP1-G5-1 발화) / **T-3 단독 = Deferred 유지** (T-2 의 lower-level + 단일 source-of-truth 위반) / **T-4 단독 = Deferred 유지** (transitive 미커버 + 책무 분담 7/8 약화) / **T-5 강화 = Deferred 유지** ((α) T-2 중복 + (β) Tier-2/3 = Backlog #3 이관 + (γ) Implementation Evidence PASS 후) / **AR-3 = Deferred 유지 + Backlog #3 이관 명시** (T3 영역 진입 BLOCKING + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무). **C-6 상태 표기 *재변경 0건***: `Partially Satisfied (PC-4 T2 sub only)` 그대로 유지 (`78483c5` 권위 source 보존). **A-1 패턴 chain 답습** (`1dd1036` §C-1 + `6fa87dc` §C-5a + `78483c5` §C-5c·§C-6 + 본 합의 5 항목 Deferred 유지 권위화): Layer D 합의 보고서 (`210c98f`) **본문 변경 0건** + 직전 합의 (`78483c5`) **본문 변경 0건** + 본 합의 보고서가 5 항목 Deferred 유지 권위 source. **본 합의 ≠ MVP-1 PASS 재선언 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / T3 영역 자동 진입 / PC-4 T2 sub 재처리 / §C-6 / §C-5c / §C-5 상태 표기 재변경 / Backlog #3 자동 진입 (이관 권고만) / Backlog #4 / Backlog #6 / Backlog #7 자동 진입 / C-1~C-8 다른 9 Conditions 자동 변경 / 수단 결정 / 본문 채택 / 도구 본문 변경 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 / Tier-2/3 catalog 자동 확장 / Node 환경 도입 / ADR 본문 자동 갱신 / ADR-012 §2.2 enum 정식 등록 / 외부 LLM 자동 호출** (사용자 명시 4 금지 답습). 다음 단계 = 사용자 결정 영역 (메타 commit / Backlog #3 T3 영역 brief / Backlog #6 Runtime brief / MVP-2 / 세션 종료).

---

**합의 일자**: 2026-05-14 후속 6
**판정**: ✅ **APPROVE — Keep Backlog #2 remaining GP-5 1.5 items Deferred** (5/5 항목 모두 진입 부적합 확정 + Deferred 유지 권위화, Reviewer-only 단축 합의, A-1 chain 답습)
**다음 단계**: CONTEXT / INDEX / SESSION 메타 갱신 commit (별도 commit 분리 답습) — 사용자 명시 결정 후 진입

**금지 (사용자 명시 4 금지 답습 — 본 합의 영역 + 본 합의 발효 후 단계 양쪽)**:
- ❌ **MVP-1 PASS *재선언*** (Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지)
- ❌ **Operational Readiness PASS (Layer E)** *선언* (MVP-6 + Backlog #7 별도 영역)
- ❌ **Hermes PMO 격상 (Layer F)** (MVP-6 + 외부 LLM 의무)
- ❌ **T3 영역 *자동 진입*** (AR-3 + T-5 (β) Backlog #3 이관 *권고만* — 진입 0건 + branch protection / commit signing / Tier-2/3 확장 모두 0건)
- ❌ **PC-4 T2 sub *재처리*** (`78483c5` 흡수 완료 — 재처리 0건)
- ❌ **§C-6 / §C-5c / §C-5 상태 표기 *재변경*** (`78483c5` 권위 source 보존)
- ❌ Layer D 합의 보고서 *본문 변경* (A-1 답습)
- ❌ 직전 합의 (`78483c5`) *본문 변경* (A-1 chain 답습)
- ❌ T-1 / T-3 / T-4 / T-5 / AR-3 *수단 결정* / *본문 채택 commit*
- ❌ T-5 도구 본문 변경 (`tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 (URL 10 / Model 19 보존)
- ❌ `.importlinter` config / `.pre-commit-config.yaml` 본문 *변경* / 신규 hook 추가
- ❌ CI workflow 본문 *변경*
- ❌ Node 환경 도입 (T-1 depcruise 의존)
- ❌ C-1 / C-2 / C-3 / C-4 / C-5a / C-5b / C-5c / C-7 / C-8 상태 *자동 변경*
- ❌ Backlog #3 (T3 영역) *자동 진입* (AR-3 + T-5 (β) 이관 *권고만*)
- ❌ Backlog #4 (P1 v2 facade MVP) / Backlog #6 (Runtime + CI-hook) / Backlog #7 (Operational Readiness) *자동 진입*
- ❌ ADR 본문 *자동 갱신*
- ❌ ADR-012 §2.2 enum *정식 등록*
- ❌ §5.5 9 sub-수단 본문 채택 *변경*
- ❌ 도구 본문 (`tools/secret_scanner.py` / `tools/provider_*.py` / `tools/workflow_*.py`) *변경*
- ❌ Production `docker-compose.yml` / Hermes upstream Dockerfile *변경*
- ❌ 사용자 명시 3 결정 (α/ii/(가)) *재변경*
- ❌ 외부 LLM *자동 호출* / 실 API key / provider SDK / 외부 API 호출
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 (본 commit ≠ 메타 갱신 — 별도 commit 분리 답습)
