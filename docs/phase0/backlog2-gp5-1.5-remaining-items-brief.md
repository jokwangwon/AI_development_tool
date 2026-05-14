# Backlog #2 GP-5 1.5차 *잔여* 항목 (T-1 / T-3 / T-4 단독 + T-5 강화 + AR-3) 검토 Brief (DRAFT)

> **본 brief = Backlog #2 (GP-5 1.5차 보강) 中 PC-4 T2 sub 외 *잔여 5 항목* — T-1 (depcruise) 단독 / T-3 (grimp) 단독 / T-4 (ruff) 단독 / T-5 (Group A 1차/3차 custom AST scanner) 강화 / AR-3 (AR-1 + AR-2 통합) — 의 *진입 적격성* 과 *처리 형태* (합의 단위·합의 형태·우선순위·차단 요인) 를 검토하는 *준비안* (DRAFT)** — 본 brief 의 어떤 §도 그 자체로 수단 결정 / 본문 채택 / 합의 발효 / 후속 backlog 자동 진입 을 발생시키지 않는다.
>
> 본 brief 의 어떤 §도 (i) T-1 / T-3 / T-4 *수단 결정 / 도입 / 채택*, (ii) T-5 도구 본문 변경 / Tier-2 / Tier-3 catalog 확장, (iii) AR-3 *진입* / branch protection rule 변경, (iv) `.pre-commit-config.yaml` 변경 / 신규 hook 추가, (v) `.importlinter` config 변경, (vi) **MVP-1 PASS *재선언***, (vii) **Operational Readiness PASS** 선언, (viii) **Hermes PMO 격상**, (ix) **T3 영역 자동 진입**, (x) Backlog #3 / #4 / #7 자동 진입, (xi) PC-4 T2 sub *재처리* (이미 `78483c5` 합의로 Partially Satisfied 흡수 완료), (xii) §C-5c / §C-6 / §C-5 *상태 표기 재변경*, (xiii) Layer D 합의 보고서 본문 변경, (xiv) §5.5 9 sub-수단 본문 채택 변경, (xv) ADR 본문 자동 갱신, (xvi) ADR-012 §2.2 `event` enum 정식 등록, (xvii) 외부 LLM 자동 호출, (xviii) 실 API key / provider SDK / 외부 API 호출 을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 6
**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**상위 권위**:
- C-6 Partially Satisfied 합의 = `78483c5 docs(review): approve PC-4 T2 C-5c C-6 partial satisfaction` (Reviewer-only 단축 합의 APPROVE, A-1 상태 표기 한정)
- C-6 갱신 메타 = `28c89ab docs(context): record PC-4 T2 partial satisfaction status` (CONTEXT/INDEX/SESSION §40)
- C-6 갱신 brief = `3be81da docs(phase0): add PC-4 T2 C-5c C-6 satisfaction brief`
- GP-5 진입 합의 = `6808d17 docs(review): add GP-5 MVP-1 entry consensus` (APPROVE WITH CONDITIONS — C-1 1.5차 보강 영역 분리 명시)
- MVP-1 Implementation Entry = `1eab814 docs(review): approve MVP-1 implementation entry` (READY, Backlog #2 우선순위 = (2) GP-3 1.5차 또는 GP-5 1.5차)
- MVP-1 roadmap deepening = `cddd22f` + `bbc05ca` + `5939c93` (mvp1.md §4.3 T-1~T-6 후보 매트릭스 + §4.5 권고 + §4.6 Rollback Trigger 10건)
- §5.5 9 sub-수단 본문 채택 = `f40423f` + `55c5b4b` (양 GP PC-3 본문 채택 — Layer B `f40423f` 발효 답습)
- 도구 PoC 답습: Group A 1차 (`tools/provider_import_scanner.py` AST 5종) / Group A 2차 (`.importlinter` + lint-imports `25605665191`) / Group A 3차 (`tools/provider_url_scanner.py` URL+모델명 `25629390384`)
- ADR-011 §2.1 (a)~(e) 5조건 + §2.4 T3 영역 분리 답습

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 6)

> "Backlog #2 GP-5 1.5차 나머지 항목 brief 를 작성해주세요. 범위는 C-6에서 아직 Deferred로 남은 T-1 / T-3 / T-4 단독, T-5 강화, AR-3 항목을 검토하는 것입니다. PC-4 T2 sub 는 이미 Partially Satisfied로 반영되었으므로 중복 처리하지 마세요. MVP-1 PASS 재선언, Operational Readiness PASS, Hermes PMO 격상, T3 영역 자동 진입은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. C-6 Partially Satisfied (`78483c5`) 후 *잔여 영역* 정의 (§1)
2. T-1 (depcruise) 단독 진입 적격성 검토 (§2.1)
3. T-3 (grimp) 단독 진입 적격성 검토 (§2.2)
4. T-4 (ruff custom rule) 단독 진입 적격성 검토 (§2.3)
5. T-5 강화 (도구 본문 / Tier-2/3 catalog 확장 / 자체 transitive 분석) 적격성 검토 (§2.4)
6. AR-3 (AR-1 + AR-2 통합) 진입 적격성 검토 (§2.5)
7. 5 항목 합산 + 차단 요인 매트릭스 (§3)
8. 합의 단위 권고 (개별 vs bundled) + 합의 형태 권고 (Reviewer-only vs 풀 3+1) (§4)
9. 우선순위 권고 (§5)
10. 7/7 풀 3+1 승격 트리거 검증 (§6)
11. 메타 검증 (§7)
12. 다음 단계 결정 옵션 (부록 A)
13. 금지 사항 (부록 B)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 4 금지 + 추가)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | **MVP-1 PASS *재선언*** | 0건 (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| 2 | **Operational Readiness PASS** (Layer E) 선언 | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 3 | **Hermes PMO 격상** (Layer F) | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| 4 | **T3 영역 자동 진입** | 0건 (AR-3 진입 / branch protection / `pre-commit install` 의무화 / dev 환경 강제 / commit signing 모두 0건 — Backlog #3 보존) |
| (추가) | **PC-4 T2 sub *재처리*** | 0건 (`78483c5` 흡수 완료 — §C-6 Partially Satisfied (PC-4 T2 sub only) 그대로 유지) |
| (추가) | T-1 / T-3 / T-4 / T-5 / AR-3 *수단 결정* / *도입* / *본문 채택 commit* | 0건 (본 brief = 검토 준비안) |
| (추가) | T-5 도구 본문 변경 (`tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) | 0건 |
| (추가) | Tier-2 / Tier-3 catalog 자동 확장 (URL 10 / Model 19 보존) | 0건 |
| (추가) | `.importlinter` config 본문 변경 | 0건 |
| (추가) | `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 | 0건 |
| (추가) | CI workflow 변경 (provider-adapter-enforcement.yml / secret-scan.yml / etc.) | 0건 |
| (추가) | Node 환경 도입 (T-1 depcruise 의존) | 0건 |
| (추가) | §C-5c / §C-6 / §C-5 *상태 표기 재변경* | 0건 (`78483c5` 그대로 유지) |
| (추가) | Layer D 합의 보고서 (`210c98f`) *본문 변경* | 0건 (A-1 답습 보존) |
| (추가) | §5.5 9 sub-수단 본문 채택 변경 | 0건 (양 GP PC-3 본문 채택 유지) |
| (추가) | ADR 본문 자동 갱신 | 0건 |
| (추가) | ADR-012 §2.2 `event` enum 정식 등록 | 0건 |
| (추가) | Backlog #3 (T3 영역) / Backlog #4 (P1 v2 facade MVP) / Backlog #7 (Operational Readiness) 자동 진입 | 0건 |
| (추가) | 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출 | 0건 |
| (추가) | 합의 보고서 *작성* / commit / push | 0건 (본 brief = 준비안 — 합의 단계 = 사용자 명시 후속) |

### 0.4 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 본 brief 가 발생시키는 *유일한* 효과 = **Backlog #2 잔여 5 항목 각각의 진입 *적격성* + *합의 단위/형태* + *우선순위* 권고를 *합의 *직전* 의사결정 입력* 으로 정비**. *수단 결정* / *본문 채택* / *Tier-2/3 확장* / *T3 영역 진입* / *합의 발효* 0건.

---

## 1. C-6 Partially Satisfied 후 *잔여* 영역 정의

### 1.1 C-6 현 상태 (`78483c5` + `28c89ab` 후 시점)

```
C-6 (GP-5 1.5차 보강 — Backlog #2) = ✅ Partially Satisfied (PC-4 T2 sub only)
   PC-4 T2 sub (provider-import + provider-url-model + import-linter 3 hook)  = Satisfied  ← `78483c5`
   T-1 단독 (depcruise)                                                          = ⏳ Deferred
   T-3 단독 (grimp)                                                              = ⏳ Deferred
   T-4 단독 (ruff custom rule)                                                   = ⏳ Deferred
   T-5 단독 강화 (도구 본문 / Tier-2/3 catalog 확장 / 자체 transitive 분석)         = ⏳ Deferred
   PC-4 T3 sub (`pre-commit install` 의무화 / dev 환경 강제)                       = ⏳ Deferred (Backlog #3 T3 영역)
   AR-3 (AR-1 + AR-2 통합)                                                       = ⏳ Deferred (T3 영역 진입 속성)
```

### 1.2 본 brief 의 *대상* 5 항목

| 항목 | mvp1.md 출처 | 본 brief §  |
|----|----------|---------|
| T-1 단독 (depcruise) | §4.3 row T-1 + §4.5 미채택 사유 #1 | §2.1 |
| T-3 단독 (grimp) | §4.3 row T-3 + §4.5 미채택 사유 #2 | §2.2 |
| T-4 단독 (ruff custom rule) | §4.3 row T-4 + §4.5 미채택 사유 #3 | §2.3 |
| T-5 단독 강화 | §4.3 row T-5 + Group A 1차/3차 답습 | §2.4 |
| AR-3 (AR-1 + AR-2 통합) | §4.8 row AR-3 + line 400 (T3 영역 진입 명시) | §2.5 |

### 1.3 본 brief 의 *대상 외* (이미 처리 / 분리 영역)

| 영역 | 처리 위치 | 이유 |
|------|--------|-----|
| **PC-4 T2 sub** (provider-import + provider-url-model + import-linter 3 hook) | ✅ 이미 처리 — `78483c5` Partially Satisfied | 사용자 명시 — 중복 처리 금지 |
| **PC-4 T3 sub** (`pre-commit install` 의무화 / dev 환경 강제 / branch protection) | Backlog #3 T3 영역 | T3 영역 자동 진입 금지 답습 |
| **AR-2 단독** (branch protection rule 변경) | Backlog #3 T3 영역 | T3 영역 — AR-3 = AR-1 + AR-2 통합이므로 AR-3 진입 자체가 T3 진입 |
| **P1 v2 facade real 본문** (GP-5 C-3) | Backlog #4 P1 v2 facade MVP | 별도 영역 (Group A 2차 §8 TR-1 답습) |
| **Layer 2 runtime block** (G5-5) | MVP-3 분리 영역 | MVP-1 영역 외 |
| **의미적 lock-in** (G4 §4.6) | MVP-3 분리 영역 | MVP-1 영역 외 |

---

## 2. 잔여 5 항목 검토

### 2.1 T-1 (dependency-cruiser) 단독 검토

#### 2.1.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | `.dependency-cruiser.cjs` 단독 운영 — JS native 정적 그래프 도구 |
| mvp1.md §4.3 row | T-1 컬럼 — 정적 그래프 강점 ✅ / transitive 강점 ✅ / dynamic ❌ / URL ❌ / model-name ❌ / 비공식 ⚠️ / 비용 **高 (Node 환경 + npm 의존)** |
| PoC 답습 | `g2-gp5-poc2-depcruise-rule-scope.md` §9.3 (`.depcruise.cjs` 직접 답습) — Provider Liquidity 4-way 와 충돌 부분 분석 답습 |
| §4.5 미채택 사유 (현 시점) | "T-1 (depcruise) — Node 환경 도입 비용 高 + Python repo 정합성 저하" |

#### 2.1.2 진입 *차단 요인* 매트릭스

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | **Provider Liquidity 하드 요구 약화** (Node 환경 도입 = 모델/구독 교체 외 환경 의존 신설) | ⚠️ 부분 — 도입 시 dev 환경 Node + npm 의존 신설 (현재 Python repo 단일 환경) |
| 2 | **Python repo 정합성 저하** | ✅ HIGH — `.dependency-cruiser.cjs` config = JS 본문 |
| 3 | **T-2 (import-linter, PoC 채택) 와 중복 cover** (양쪽 모두 transitive 분석 강점) | ✅ HIGH — `.importlinter` 본문 채택 (`f40423f`) 후 추가 도구의 *novel coverage* 없음 |
| 4 | **R-MVP1-G5-1 (T-1/T-3/T-4/T-5 단독 진입 결정) 트리거 발화** | ✅ HIGH — mvp1.md §4.6 R-MVP1-G5-1 = "풀 3+1 합의 + 도구 변경 영향 분석" 의무 답습 |
| 5 | T3 영역 진입 의무성 | ❌ 0건 — Layer 1 정적 도구 한정 (T2 영역) |
| 6 | 외부 LLM 의무성 (Provider Liquidity) | ❌ 0건 (수단 *결정* 시 풀 3+1 권고 한정) |

#### 2.1.3 §2.1 판정

❌ **T-1 단독 진입 *부적합*** — Node 환경 도입 비용 高 + T-2 (PoC 채택) 와 중복 cover + R-MVP1-G5-1 풀 3+1 트리거 발화. **본 brief 권고 = Deferred 그대로 유지** (mvp1.md §4.5 미채택 사유 답습 + Group A 2차 합의 §C-7 silent fail 위험 명시 답습).

### 2.2 T-3 (grimp) 단독 검토

#### 2.2.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | `grimp` 단독 운영 — import-linter 의 lower-level Python 라이브러리 |
| mvp1.md §4.3 row | T-3 컬럼 — 정적 그래프 ✅ / transitive ✅ / dynamic ❌ / URL ❌ / model-name ❌ / 공식 ✅ / 비용 **低** |
| PoC 답습 | `g2-gp5-poc2-depcruise-rule-scope.md` §8 미언급 — mvp1.md §4.3 신규 후보 |
| §4.5 미채택 사유 | "T-3 (grimp) 단독 — import-linter 보다 lower-level, 본 PoC 답습 충실성 ↓" |

#### 2.2.2 진입 *차단 요인* 매트릭스

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | **T-2 (import-linter, PoC 채택) 와 책무 중복** — import-linter 가 grimp 를 *내부적으로* 사용 (상위 라이브러리) | ✅ HIGH — `.importlinter` `f40423f` 답습 후 grimp 단독 추가 = source-of-truth 분리 위험 |
| 2 | **PoC 답습 충실성 저하** — Group A 2차 PoC = T-2 import-linter 단독 채택 답습 (Group A 2차 합의 §5.5 #C-7 답습) | ✅ HIGH — 합의된 PoC 결과를 *우회* 하는 효과 |
| 3 | **R-MVP1-G5-1 트리거 발화** | ✅ HIGH — mvp1.md §4.6 답습 |
| 4 | **단일 source-of-truth 보존** | ✅ HIGH — Layer B `f40423f` `.importlinter` 본문 채택 답습 |
| 5 | T3 영역 진입 의무성 | ❌ 0건 (Layer 1 정적 도구 한정) |
| 6 | Provider Liquidity 하드 요구 약화 | ❌ 0건 (stdlib + grimp Python 단독) |

#### 2.2.3 §2.2 판정

❌ **T-3 단독 진입 *부적합*** — T-2 (PoC 채택) 와 책무 중복 + import-linter 의 *내부 의존* 이므로 grimp 단독 채택 시 단일 source-of-truth 위반 + Group A 2차 합의 답습 충실성 저하. **본 brief 권고 = Deferred 그대로 유지** (mvp1.md §4.5 미채택 사유 답습).

### 2.3 T-4 (ruff custom rule) 단독 검토

#### 2.3.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | ruff custom plugin / AST plugin — file-level 정적 검사 도구 |
| mvp1.md §4.3 row | T-4 컬럼 — 정적 그래프 ✅ / **transitive ❌** (ruff = file-level) / dynamic ✅ / URL 부분 / model-name 부분 / 공식 ✅ / 비용 中 (plugin 작성) |
| PoC 답습 | `g2-gp5-poc2-depcruise-rule-scope.md` §8 (T-3 row 답습) |
| §4.5 미채택 사유 | "T-4 (ruff custom rule) 단독 — transitive 미지원, T-2 의 강점 손실" |

#### 2.3.2 진입 *차단 요인* 매트릭스

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | **transitive import 미커버** (ruff = file-level) → T-2 강점 손실 | ✅ HIGH — mvp1.md §4.3 답습 (T-4 transitive ❌) |
| 2 | **책무 분담 매트릭스 7/8 cover 약화** — T-6 (T-2 + T-5) 의 transitive cover 손실 | ✅ HIGH — GP-5 진입 합의 §1.4 답습 |
| 3 | **R-MVP1-G5-1 트리거 발화** | ✅ HIGH — mvp1.md §4.6 답습 |
| 4 | **ruff plugin 작성 비용** (custom plugin 작성 + 유지 보수 + ruff version skew 영향) | ⚠️ MEDIUM — 중간 비용 |
| 5 | T3 영역 진입 의무성 | ❌ 0건 (Layer 1 정적 도구 한정) |
| 6 | Provider Liquidity 하드 요구 약화 | ❌ 0건 (Python stdlib 단독) |

#### 2.3.3 §2.3 판정

❌ **T-4 단독 진입 *부적합*** — transitive 미커버 = T-2 의 핵심 강점 손실 + T-6 책무 분담 매트릭스 7/8 cover 직접 약화 + R-MVP1-G5-1 트리거 발화. **본 brief 권고 = Deferred 그대로 유지** (mvp1.md §4.5 미채택 사유 답습).

### 2.4 T-5 단독 강화 검토

#### 2.4.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | Group A 1차/3차 채택 형태 (`tools/provider_import_scanner.py` AST 5종 + `tools/provider_url_scanner.py` URL 10 + Model 19) 의 *단독 강화* — *자체 transitive 분석 추가* / *Tier-2 / Tier-3 catalog 확장* / *추가 패턴 도입* |
| mvp1.md §4.3 row | T-5 컬럼 — 정적 그래프 ✅ / transitive 부분 (자체 구현 부담 高) / dynamic ✅ / URL ✅ / model-name ✅ / stdlib ✅ / 비용 **高 (자체 구현 transitive)** |
| PoC 답습 | Group A 1차 (`tools/provider_import_scanner.py`) + Group A 3차 (`tools/provider_url_scanner.py` URL Tier-1=10 / Model Tier-1=19) — 양 PoC 모두 *Tier-1 한정* + 의도된 보존 명시 |

#### 2.4.2 T-5 강화 *3 하위 후보* 분해 매트릭스

| 하위 후보 | 내용 | 적격성 | 차단 요인 |
|---------|----|------|--------|
| **(α)** *자체 transitive 분석 추가* (provider_import_scanner.py 확장) | T-2 (import-linter) 가 이미 cover 하는 영역을 stdlib 로 재구현 | ❌ 부적합 | T-2 와 책무 중복 + R-MVP1-G5-1 발화 + Group A 1차 합의 답습 충실성 저하 |
| **(β)** *Tier-2 / Tier-3 catalog 확장* (URL 10 → 20+ / Model 19 → 50+ 등) | Group D 41 패턴 답습 / Group A 3차 답습 의 Tier-1 보존 정책 변경 | ❌ 부적합 — **T3 영역 진입** | GP-3 §3.5 R-MVP1-G3-1 + GP-5 §4.6 R-MVP1-G5-1 모두 "Tier-2/3 catalog 변경 결정 후 채택 trigger" 답습 → Backlog #3 T3 영역 |
| **(γ)** *추가 패턴 도입* (FP / FN 검출 결과 반영 — 신규 vendor / 신규 URL prefix / 신규 model id 패턴) | 도구 본문 변경 (catalog 외 패턴 본문 추가) | ⚠️ 부분 — *실 운영 FN 검출 evidence* 의존 | MVP-1 1차 진입 시점 = 실 운영 evidence 0건 (Implementation Evidence PASS 미발효) |

#### 2.4.3 §2.4 판정

❌ **T-5 강화 단독 진입 *전체 부적합 (현 시점)*** — (α) T-2 와 중복 + (β) Tier-2/3 = T3 영역 진입 = Backlog #3 보존 의무 + (γ) 실 운영 evidence 의존 (Implementation Evidence PASS 미발효 시점에 의미 없음). **본 brief 권고 = Deferred 그대로 유지** + (γ) 는 Implementation Evidence PASS 발효 후 별도 합의 영역.

### 2.5 AR-3 (AR-1 + AR-2 통합) 검토

#### 2.5.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | AR-1 (CI step fail-closed) + AR-2 (GitHub branch protection rule 강제) 통합 = PR auto-reject runtime |
| mvp1.md §4.8 row | AR-3 = T2 + T3 / T3 (포함) / 우회 차단 강화 |
| mvp1.md line 400 | "MVP-1 1.5차 (보강) = AR-3 (AR-1 + AR-2 통합) — **T3 영역 진입** + branch protection rule 변경 + 사용자 명시 결정" |
| §4.6 R-MVP1-G5-2 답습 | "AR-2 / AR-3 진입 (branch protection rule 변경) = **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** — T3 영역" |

#### 2.5.2 진입 *차단 요인* 매트릭스 ⭐

| # | 차단 요인 | 발화 |
|---|--------|------|
| 1 | **T3 영역 진입 = 사용자 명시 4 금지 #4 답습** | ✅ **HIGH (BLOCKING)** — 본 brief 진입 명령 #4 답습 ("T3 영역 자동 진입은 하지 마세요") |
| 2 | **AR-2 (branch protection rule) 본문 변경 = Hermes upstream / GitHub repo 정책 변경** | ✅ HIGH — ADR-011 §2.4 T3 영역 답습 |
| 3 | **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 의무** (mvp1.md §4.6 R-MVP1-G5-2 답습) | ✅ HIGH — 본 brief 진입 명령 답습 (외부 LLM 자동 호출 0건 + 합의 형태 결정 0건) |
| 4 | **Backlog #3 보존 의무** | ✅ HIGH — `78483c5` 합의 §C-6 답습 (AR-3 ⏳ Deferred) |
| 5 | T-2 / T-5 책무 분담 영향 | ❌ 0건 (AR-3 = PR auto-reject runtime — Layer 1 정적 도구 *외* 영역) |
| 6 | Provider Liquidity 하드 요구 약화 | ❌ 0건 (CI / branch protection 영역 — provider 의존 없음) |

#### 2.5.3 §2.5 판정 ⭐

❌ **AR-3 진입 *부적합 (본 brief 영역에서)*** — **AR-3 = T3 영역 진입 (branch protection rule 변경)** → 사용자 명시 4 금지 #4 답습 + Backlog #3 보존 의무 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 (mvp1.md §4.6 R-MVP1-G5-2 답습). **본 brief 권고 = Deferred 그대로 유지 + Backlog #3 T3 영역 풀 3+1 합의 영역으로 *이관 명시***.

---

## 3. 5 항목 합산 + 차단 요인 매트릭스

### 3.1 5 항목 *진입 적격성* 합산

| 항목 | 본 brief 권고 | 차단 요인 1 | 차단 요인 2 | 차단 요인 3 | mvp1.md §4.5 / §4.6 답습 |
|----|---------|---------|---------|---------|----------------------|
| T-1 (depcruise) 단독 | ❌ Deferred 유지 | Node 환경 도입 高 | T-2 와 중복 | R-MVP1-G5-1 발화 | §4.5 #1 |
| T-3 (grimp) 단독 | ❌ Deferred 유지 | T-2 의 lower-level | 단일 source-of-truth 위반 | R-MVP1-G5-1 발화 | §4.5 #2 |
| T-4 (ruff) 단독 | ❌ Deferred 유지 | transitive 미커버 | 책무 분담 7/8 약화 | R-MVP1-G5-1 발화 | §4.5 #3 |
| T-5 강화 (α/β/γ) | ❌ Deferred 유지 | (α) T-2 중복 | (β) Tier-2/3 = T3 영역 | (γ) Evidence PASS 의존 | Group A 1차/3차 답습 |
| AR-3 (AR-1 + AR-2) | ❌ Deferred 유지 + Backlog #3 이관 | **T3 영역 진입 (BLOCKING)** | 풀 3+1 + 외부 LLM 1+ 의무 | Backlog #3 보존 의무 | §4.6 R-MVP1-G5-2 |

### 3.2 5 항목 *진입 가능* 영역 = 0건

✅ **본 brief 의 5 항목 中 *MVP-1 1.5차 단계에서 단독 진입 적합* 한 항목 = 0건**. 모든 항목이 (i) Group A 2차 PoC 채택 답습 충실성 (T-1/T-3/T-4) 또는 (ii) T3 영역 진입 (AR-3) 또는 (iii) Tier-2/3 catalog 영역 (T-5 β) 또는 (iv) Implementation Evidence PASS 의존 (T-5 γ) 으로 인해 *현 시점에서는 부적합*.

### 3.3 후속 진입 *조건* (재진입 시점 권고)

| 항목 | 후속 진입 *조건* | 합의 영역 |
|----|--------------|--------|
| T-1 단독 | T-2 (PoC 채택) 가 **silent fail 발생** + Group A 2차 §C-7 트리거 발화 시 (mvp1.md §4.6 R-MVP1-G5-3 답습) | 풀 3+1 + 도구 변경 영향 분석 |
| T-3 단독 | T-2 (import-linter) deprecation / 라이선스 변경 / `.importlinter` rule 충돌 폭증 시 | 풀 3+1 + 도구 변경 영향 분석 |
| T-4 단독 | T-2 (import-linter) deprecation + ruff plugin 으로 transitive 우회 가능성 검증 후 | 풀 3+1 + 도구 변경 영향 분석 |
| T-5 (α) | T-2 가 *기능적으로 부족* 한 영역 검출 (PoC 결과 의존) | 풀 3+1 + Group A 2차 §C-7 답습 |
| T-5 (β) Tier-2/3 catalog 확장 | **Backlog #3 T3 영역 합의 영역** + 사용자 명시 결정 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| T-5 (γ) 추가 패턴 도입 | **Implementation Evidence PASS 발효 후** + 실 운영 FN evidence 수집 | 단축 또는 풀 3+1 (실 evidence 결정적성에 따라) |
| AR-3 | **Backlog #3 T3 영역 합의 영역** + branch protection rule 변경 결정 + 외부 LLM 1+ + 사용자 명시 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |

---

## 4. 합의 단위 + 합의 형태 권고

### 4.1 합의 *단위* 권고

| 옵션 | 단위 | 적합성 |
|-----|-----|------|
| **(I)** 5 항목 *단일 bundled* 합의 | 1 합의 = 5 항목 동시 검토 | ✅ **권고** — 모든 항목이 *Deferred 유지* 권고이므로 단일 합의로 *진입 부적합* 확정 + 후속 조건 명시 적격 |
| (II) T-1/T-3/T-4 bundled + T-5 + AR-3 분리 (3 합의) | 3 합의 분리 | ⚠️ 가능 — 도구별 차단 요인이 유사 (T-2 답습 보존) 하므로 단일 권고 |
| (III) 5 항목 각각 분리 (5 합의) | 5 합의 분리 | ❌ 비효율 — 모든 항목이 *진입 부적합* 권고로 동일 |
| (IV) AR-3 분리 (T3 영역) + 나머지 4 항목 bundled | 2 합의 분리 | ⚠️ 가능 — AR-3 의 T3 영역 속성을 명시적 분리 |

**본 brief 권고**: (I) 단일 bundled 합의 — 5 항목 모두 *Deferred 유지* 권고 + 후속 조건 명시.

### 4.2 합의 *형태* 권고

| 합의 형태 | 적합성 | 사유 |
|--------|------|------|
| **(가) Reviewer-only 단축 합의** | ✅ **권고** | (i) 본 brief 5 항목 모두 *Deferred 유지* 권고 = *수단 결정 0건* = 7/7 풀 3+1 트리거 0건 발화 / (ii) mvp1.md §4.5 미채택 사유 답습 한정 (새 권위 결정 0건) / (iii) GP-5 진입 합의 §C-7 답습 한정 / (iv) Group A 2차 합의 §C-7 답습 한정 |
| (나) 풀 3+1 합의 | ❌ 부적합 (현 시점) | 7/7 트리거 0건 발화 — 풀 3+1 의무 없음. 후속 *재진입* 시 mvp1.md §4.6 R-MVP1-G5-1 답습 의무 |
| (다) 풀 3+1 + 외부 LLM 1+ | ❌ 부적합 | T3 영역 결정 0건 — 외부 LLM 의무 발화 없음 |

**본 brief 권고**: (가) Reviewer-only 단축 합의 (단일 bundled).

### 4.3 합의 보고서 *경로* 권고

| 옵션 | 경로 | 적합성 |
|-----|----|------|
| (A) | `docs/review/3plus1-consensus-2026-05-14-backlog2-remaining-deferred-confirmation.md` | ✅ 권고 |
| (B) | 사용자 명시 영역 | (사용자 결정 한정) |

---

## 5. 우선순위 권고 (재진입 *시점* 권고)

### 5.1 후속 재진입 *우선순위*

```
1순위 (즉시 의미 = 0건)    : 본 brief 의 5 항목 모두 — 현 시점 진입 부적합 확정
2순위 (Backlog #3 합의 시) : AR-3 (T3 영역 풀 3+1 + 외부 LLM 1+ 의무)
                            T-5 (β) Tier-2/3 catalog 확장 (T3 영역 일부)
3순위 (Implementation     : T-5 (γ) 추가 패턴 도입 — 실 운영 FN evidence 수집 후
       Evidence PASS 후)
4순위 (Trigger 발화 시)    : T-1 / T-3 / T-4 단독 — Group A 2차 §C-7 silent fail trigger 발화 의존
                            R-MVP1-G5-1 발화 시 풀 3+1 + 도구 변경 영향 분석 의무
```

### 5.2 7 backlog 中 본 brief 의 위치

| Backlog # | 영역 | 본 brief 와 관계 |
|---------|------|--------------|
| #1 | GP-3 1.5차 보강 | 별도 brief — 영향 0건 (양 GP PC-3 본문 채택 답습 유지) |
| **#2** | **GP-5 1.5차 보강** | ✅ **본 brief 영역** — PC-4 T2 sub Satisfied (`78483c5`) + 잔여 5 항목 Deferred 유지 권고 |
| #3 | T3 영역 (AR-2 / Vault HSM ST-4 / Tier-2/3) | AR-3 + T-5 (β) 영역 *이관 권고* (본 brief 영역 외) |
| #4 | P1 v2 facade MVP (G5-4) | 별도 영역 (Group A 2차 §8 TR-1 답습) |
| #5 | ADR-012 §2.2 evidence enum 정식 등록 | 별도 합의 영역 (G4 §10.2 schema 진화 정책 답습) |
| #6 | Runtime enforcement / CI-hook implementation | MVP-1 Implementation Entry 최종 합의 권고 우선순위 1 (`1eab814` 답습) |
| #7 | Operational Readiness parity check | MVP-6 영역 |

### 5.3 본 brief 후속 다음 단계 우선순위 권고

| 우선순위 | 다음 단계 | 사유 |
|--------|--------|------|
| **(I)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 → §C-6 *재변경 0건* + 5 항목 *Deferred 유지 확정* 권위 source 발행** | A-1 패턴 답습 + Layer D 본문 변경 0건 |
| (II) | Backlog #6 (Runtime enforcement / CI-hook implementation) 우선 진입 — MVP-1 Implementation Entry 최종 합의 권고 우선순위 1 (`1eab814` §6 답습) | 본 brief 5 항목 모두 *진입 부적합* 확정 후 다음 합리적 단계 |
| (III) | Backlog #3 (T3 영역) 풀 3+1 brief 진입 — AR-3 + T-5 (β) 포함 | 본 brief 가 AR-3 + T-5 (β) 의 Backlog #3 이관을 명시 |
| (IV) | MVP-2 deepening | 본 brief 의 후속 단계로 적합하지 않음 — MVP-1 Implementation Evidence PASS 미발효 |

---

## 6. 7/7 풀 3+1 승격 트리거 검증

| # | 트리거 | 본 brief 발화 |
|---|----|---------|
| 1 | 9 sub-수단 외 수단 *재결정* | ❌ 0건 (5 항목 모두 *Deferred 유지* 권고 — 수단 결정 0건) |
| 2 | **T3 영역 자동 진입** | ❌ 0건 (AR-3 = Backlog #3 이관 명시 + 사용자 명시 4 금지 #4 답습) |
| 3 | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | ❌ 0건 (Cycle 4 답습 한정 — 본 brief 영역 외) |
| 4 | Provider Liquidity 5-way 약화 | ❌ 0건 (T-1 Node 환경 = *진입 부적합* 사유로 명시 — 약화 0건) |
| 5 | 5 영구 핵심 제약 약화 | ❌ 0건 (Hermes ≠ root of trust 보존 + 수단/목적 분리 보존 + 메타포 강제 금지 보존 + 단일 source-of-truth 보존 + Provider Liquidity 보존) |
| 6 | **MVP-1 PASS 재선언 / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상)** | ❌ 0건 (사용자 명시 4 금지 #1 + #2 + #3 답습) |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ❌ 0건 (T3 결정 0건 — AR-3 + T-5 (β) Backlog #3 이관) |

**합산 = 7/7 0건 발화** → **Reviewer-only 단축 합의 적격 확정**.

---

## 7. 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 검토 범위 답습 (T-1 / T-3 / T-4 단독 + T-5 강화 + AR-3 검토) | ✅ §2.1 ~ §2.5 |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) | ✅ §0.3 + §2.5 + §6 + 부록 B |
| **PC-4 T2 sub *재처리 0건*** (이미 `78483c5` 흡수) | ✅ §1.3 (대상 외 명시) + §3.1 5 항목에서 명시적 제외 |
| §C-6 *재변경 0건* (Partially Satisfied (PC-4 T2 sub only) 그대로 유지) | ✅ (5 항목 모두 *Deferred 유지* 권고) |
| §C-5c / §C-5 전체 *재변경 0건* | ✅ |
| Layer D 합의 보고서 (`210c98f`) *본문 변경 0건* | ✅ |
| 합의 보고서 (`78483c5`) *본문 변경 0건* | ✅ |
| MVP-1 PASS *재선언 0건* (Layer D `210c98f` 그대로 유지) | ✅ |
| Operational Readiness PASS (Layer E) 선언 0건 | ✅ |
| Hermes PMO 격상 (Layer F) 0건 | ✅ |
| T3 영역 자동 진입 0건 (AR-3 + T-5 (β) Backlog #3 이관 명시) | ✅ §2.5 + §3.3 + §5.1 |
| Backlog #3 / #4 / #7 자동 진입 0건 (#3 이관 권고만 — 진입 0건) | ✅ |
| 수단 결정 / 본문 채택 0건 (T-1 / T-3 / T-4 / T-5 / AR-3 모두 Deferred 유지) | ✅ |
| 도구 본문 변경 0건 (Group A 1차/3차 `tools/provider_*.py`) | ✅ |
| Tier-2 / Tier-3 catalog 자동 확장 0건 (URL 10 / Model 19 보존) | ✅ |
| `.importlinter` / `.pre-commit-config.yaml` 변경 0건 | ✅ |
| CI workflow 변경 0건 | ✅ |
| Node 환경 도입 0건 | ✅ (T-1 *부적합* 사유로 명시) |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| ADR 본문 자동 갱신 0건 | ✅ |
| ADR-012 §2.2 enum 정식 등록 0건 | ✅ |
| 외부 LLM 자동 호출 0건 | ✅ |
| 실 API key / provider SDK / 외부 API 호출 0건 | ✅ |
| 7/7 풀 3+1 승격 트리거 0건 발화 → Reviewer-only 단축 적격 | ✅ §6 |
| 5 영구 핵심 제약 보존 (Hermes ≠ root of trust / 수단·목적 분리 / 메타포 강제 금지 / 단일 source-of-truth / Provider Liquidity) | ✅ |
| ADR-011 §2.1 (a)~(d) 매핑 (a) 동등 이상 보안 결과 = (T-6 PoC 채택 답습 보존) | ✅ |
| 합의 보고서 *작성* / commit / push 0건 (본 brief = 준비안) | ✅ |

---

## 8. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #2 (GP-5 1.5차 보강) 中 PC-4 T2 sub Satisfied (`78483c5`) 후 *잔여 5 항목* — T-1 (depcruise) 단독 / T-3 (grimp) 단독 / T-4 (ruff custom rule) 단독 / T-5 (Group A 1차/3차 custom AST scanner) 단독 강화 / AR-3 (AR-1 + AR-2 통합) — 의 진입 *적격성* 과 *처리 형태* 를 검토하는 *합의 준비안* (DRAFT)** 이다. 사용자 명시 검토 범위 답습 + 사용자 명시 4 금지 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) 답습 + PC-4 T2 sub 중복 처리 0건. 본 brief 5 영역 검토 결과: (§2.1) **T-1 단독 = Deferred 유지** (Node 환경 도입 高 + T-2 와 중복 + R-MVP1-G5-1 발화) / (§2.2) **T-3 단독 = Deferred 유지** (T-2 의 lower-level + 단일 source-of-truth 위반) / (§2.3) **T-4 단독 = Deferred 유지** (transitive 미커버 + 책무 분담 7/8 약화) / (§2.4) **T-5 강화 = Deferred 유지** ((α) T-2 중복 + **(β) Tier-2/3 = T3 영역 = Backlog #3 이관** + (γ) Evidence PASS 의존) / (§2.5) **AR-3 = Deferred 유지 + Backlog #3 이관 명시** (**T3 영역 진입 BLOCKING** + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무). 합산 = **5/5 항목 모두 현 시점 진입 *부적합*** + 후속 재진입 조건 명시 (T-1/T-3/T-4 = R-MVP1-G5-1 발화 시 / T-5 (β) + AR-3 = Backlog #3 / T-5 (γ) = Implementation Evidence PASS 후). 합의 *단위* 권고 = (I) 5 항목 *단일 bundled* + 합의 *형태* 권고 = (가) **Reviewer-only 단축 합의** (7/7 풀 3+1 트리거 0건 발화) + 합의 보고서 경로 = `docs/review/3plus1-consensus-2026-05-14-backlog2-remaining-deferred-confirmation.md` (가칭). **본 brief 후속 다음 단계 우선순위 권고** = (I) 본 brief 승인 → Reviewer-only 단축 합의 → §C-6 *재변경 0건* + 5 항목 Deferred 유지 확정 권위 source 발행 / (II) Backlog #6 (Runtime + CI-hook) 우선 진입 — `1eab814` 답습 / (III) Backlog #3 (T3 영역) 풀 3+1 brief 진입. **본 brief ≠ 수단 결정** + **§C-6 / §C-5c / §C-5 *재변경* 0건** + **Layer D 본문 변경 0건** + **합의 보고서 (`78483c5`) 본문 변경 0건** + **MVP-1 PASS *재선언* 0건** + **Operational Readiness PASS (Layer E) 0건** + **Hermes PMO 격상 (Layer F) 0건** + **T3 영역 자동 진입 0건** + **Backlog #3 / #4 / #7 자동 진입 0건** + **도구 본문 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건** + **Tier-2/3 catalog 자동 확장 0건** + **Node 환경 도입 0건** + **§5.5 9 sub-수단 본문 채택 변경 0건** + **ADR 본문 자동 갱신 0건** + **외부 LLM 자동 호출 0건**. 다음 단계 = 사용자 결정 영역 (부록 A 옵션 A~F).

---

## 부록 A. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성** (`docs/review/3plus1-consensus-2026-05-14-backlog2-remaining-deferred-confirmation.md` 가칭) → §C-6 *재변경 0건* + 5 항목 Deferred 유지 확정 권위 source 발행 → 메타 commit → push | 3-commit chain (brief 파일화 + 합의 + 메타) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 그대로 승인 → 합의 보고서 작성 → 메타 + push 보류 | 2 commit 한정 |
| (D) | 본 brief 그대로 승인 → 파일화 + commit *까지만* | 1 commit 한정 |
| (E) | 본 brief 보류 → Backlog #6 (Runtime + CI-hook implementation) 우선 진입 brief 작성 | `1eab814` §6 답습 우선순위 1 |
| (F) | 본 brief 보류 → Backlog #3 (T3 영역) 풀 3+1 brief 작성 | AR-3 + T-5 (β) + PC-4 T3 sub + C-5b ST-1 + Vault HSM ST-4 통합 영역 |
| (G) | 본 brief 보류 → MVP-2 진입 brief 작성 | 본 brief 의 후속으로 적합하지 않음 (Implementation Evidence PASS 미발효) |
| (H) | 본 brief 보류 → 세션 종료 | — |

### A.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 시작 명령 후보: "옵션 (A) 로 진행해주세요. 본 brief 그대로 승인하고, `docs/review/3plus1-consensus-2026-05-14-backlog2-remaining-deferred-confirmation.md` 작성 → 메타 + push 까지 3-commit chain 으로 진행."

---

## 부록 B. 금지 사항 (사용자 명시 4 금지 + 추가 답습)

### B.1 사용자 명시 4 금지 답습 (이번 진입 명령)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | **MVP-1 PASS *재선언*** | 0건 (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| 2 | **Operational Readiness PASS** (Layer E) 선언 | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 3 | **Hermes PMO 격상** (Layer F) | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| 4 | **T3 영역 자동 진입** | 0건 (AR-3 + T-5 (β) Backlog #3 이관 명시 + branch protection / commit signing / Tier-2/3 catalog 확장 모두 0건) |

### B.2 추가 금지 (본 brief 자체)

- ❌ **PC-4 T2 sub 재처리 0건** — `78483c5` 흡수 완료 (§C-6 Partially Satisfied (PC-4 T2 sub only) 그대로 유지)
- ❌ §C-6 / §C-5c / §C-5 전체 *재변경* 0건 (5 항목 모두 *Deferred 유지* 권고)
- ❌ Layer D 합의 보고서 (`210c98f`) *본문 변경* 0건 (A-1 답습)
- ❌ 합의 보고서 (`78483c5`) *본문 변경* 0건
- ❌ T-1 / T-3 / T-4 / T-5 / AR-3 *수단 결정* / *도입* / *본문 채택 commit* 0건
- ❌ T-5 도구 본문 변경 (`tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 0건
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건 (URL 10 / Model 19 보존)
- ❌ `.importlinter` config 본문 변경 0건
- ❌ `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 0건
- ❌ CI workflow 변경 0건
- ❌ Node 환경 도입 0건 (T-1 *부적합* 사유로 명시)
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건 (양 GP PC-3 본문 채택 유지)
- ❌ ADR 본문 자동 갱신 0건
- ❌ ADR-012 §2.2 `event` enum 정식 등록 0건
- ❌ Backlog #3 (T3 영역) 자동 진입 0건 (AR-3 + T-5 (β) 이관 *권고만* — 진입 0건)
- ❌ Backlog #4 (P1 v2 facade MVP) / Backlog #7 (Operational Readiness) 자동 진입 0건
- ❌ Backlog #6 (Runtime + CI-hook implementation) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건 (T3 결정 0건 — 외부 LLM 의무 발화 없음)
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화 0건
- ❌ 사용자 명시 3 결정 (α/ii/(가)) *재변경* 0건 (Cycle 4 답습 한정)
- ❌ Production `docker-compose.yml` / Hermes upstream Dockerfile 변경 0건
- ❌ 합의 보고서 *작성* 0건 (본 brief = 준비안 — 합의 보고서 = 별도 단계)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리)
- ❌ git commit / push 0건 (본 brief 파일화 + commit = 사용자 명시 후속)

---

**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**다음 단계**: 사용자 명시 결정 영역 (부록 A 옵션 A~H)
**주요 결정 필요 영역**:
- (a) **5 항목 모두 *Deferred 유지* 권고** 적절성 확인 (T-1 / T-3 / T-4 / T-5 / AR-3)
- (b) **AR-3 + T-5 (β) Backlog #3 이관 권고** 적절성 확인
- (c) **합의 단위** = (I) 5 항목 단일 bundled vs (II) 3 합의 분리 vs (IV) AR-3 분리 中 선택
- (d) **합의 형태** = (가) Reviewer-only 단축 합의 (7/7 트리거 0건 발화 답습) 확인
- (e) **합의 보고서 경로** = `docs/review/3plus1-consensus-2026-05-14-backlog2-remaining-deferred-confirmation.md` (가칭) 또는 사용자 명시 영역
- (f) **후속 다음 단계 우선순위** = (II) Backlog #6 Runtime / (III) Backlog #3 T3 영역 中 권고 영역 (사용자 결정 한정)
