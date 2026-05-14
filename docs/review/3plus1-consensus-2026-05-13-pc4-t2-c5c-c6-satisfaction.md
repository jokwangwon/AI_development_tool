# Backlog #1 + #2 PC-4 T2 §C-5c + §C-6 Partially Satisfied 갱신 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 (옵션 (A) brief 그대로 승인 + A-1 패턴 답습 — Layer D 본문 변경 0건 + §C-5c·§C-6 양쪽 부분 갱신 + §C-5 전체 = `Partially Satisfied (C-5a + C-5c partial)` 표기)
**합의 일자**: 2026-05-14 후속 5
**검토 대상**: **Backlog #1 + #2 통합 PC-4 T2 sub `.pre-commit-config.yaml` Cycle 4 + fix + 메타 chain (`b2f99f4` + `3d3cd21` + `5f878d6`) 위에서 §C-5c (PC-4 local pre-commit framework) + §C-6 (GP-5 1.5차 보강) 양쪽 `Deferred → Partially Satisfied` 갱신 적격성** — `pre-commit run --all-files` warm 6/6 hook PASS (0.482초) actual run evidence + 양쪽 부분 상태 갱신 (T3 sub Backlog #3 보존 + GP-5 나머지 sub-수단 보존) + Layer D 본문 변경 0건 + MVP-1 PASS 재선언 0건
**보조 참조**:
- 본 합의 대상 brief = `docs/phase0/backlog1-2-pc4-t2-c5c-c6-satisfaction-brief.md` (commit `3be81da`, DRAFT 10 섹션 + 부록 A/B, 468 lines)
- PC-4 T2 sub Cycle 4 본문 = `b2f99f4 feat(pc4): add integrated pre-commit config` (`.pre-commit-config.yaml` 110 lines, 1 entry `repo: local` + 6 hook 정의)
- PC-4 T2 sub Cycle 4 fix = `3d3cd21 fix(pc4): use python3 + scope secret-scanner to src/.github` (R-MVP1-G3-PC4-T2-INTG-8 + INTG-4 통합 1회 처리)
- PC-4 T2 sub Cycle 4 메타 = `5f878d6 docs(context): record PC-4 T2 pre-commit validation` (CONTEXT/INDEX/SESSION §39 신설, local pre-commit 6/6 PASS warm 0.482초 evidence 기록)
- 구현 진입 합의 = `docs/review/3plus1-consensus-2026-05-13-pc4-t2-implementation-entry.md` (commit `3c0a1c1`, APPROVE — 실 구현 진입 권한 발효, 사용자 결정 3개 α/ii/(가) 확정)
- 구현 진입 brief = `docs/phase0/backlog1-2-pc4-t2-implementation-brief.md` (commit `edf1f89`, DRAFT 19 섹션 793 lines)
- §C-5a Satisfied 갱신 합의 (A-1 패턴 sibling 답습) = `docs/review/3plus1-consensus-2026-05-13-st2-c5a-satisfaction.md` (commit `6fa87dc`, APPROVE — A-1 답습, §C-5a 상태 갱신, Layer D 본문 변경 0건)
- §C-1 갱신 합의 (A-1 패턴 권위 source) = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass-c1-k2-satisfaction.md` (commit `1dd1036`, A-1 §C-1 상태 표기만 갱신, Layer D 본문 변경 0건)
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, APPROVE WITH CONDITIONS, §C-5 GP-3 1.5차 Backlog #1 + §C-6 GP-5 1.5차 Backlog #2 Deferred 정의)
- §5.5 본문 채택 = `f40423f` + `55c5b4b` (양 GP PC-3 일관 본문 채택)
- 도구 검증 답습: `tools/secret_scanner.py` (Group D `25623028888`) / `tools/provider_import_scanner.py` (Group A 1차) / `tools/provider_url_scanner.py` (Group A 3차 `25629390384`) / `lint-imports` + `.importlinter` (Group A 2차 `25605665191`) / `tools/workflow_*.py` (Stage 5)

**검토 목적**: PC-4 T2 sub Cycle 4 chain + local `pre-commit run --all-files` 6/6 PASS evidence 위에서 §C-5c + §C-6 양쪽 *Deferred → Partially Satisfied* 부분 갱신 적격성 확정. **본 합의 = §C-5c + §C-6 상태 표기 부분 갱신 한정 (A-1 답습)** ≠ Layer D 본문 변경 / §C-5c 전체 Satisfied / §C-6 전체 Satisfied / §C-5 전체 Satisfied / MVP-1 PASS 재선언 / C-5b·C-1~C-4·C-5a·C-7·C-8 자동 변경 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / T3 영역 자동 진입 / 다른 backlog 자동 진입 / ADR 본문 자동 갱신.

**판정**: ✅ **APPROVE — §C-5c (PC-4) + §C-6 (GP-5 1.5차) Deferred → Partially Satisfied 양쪽 부분 갱신 (Reviewer-only 단축 합의, A-1 상태 표기 한정, Layer D 본문 변경 0건)**

⚠️ **본 합의 = §C-5c + §C-6 양쪽 *부분* 상태 표기 갱신 한정** — Layer D 합의 보고서 (`210c98f`) **본문 변경 0건** (역사적 기록 보존). 본 합의 보고서가 §C-5c + §C-6 부분 갱신 권위 source.

⚠️ **본 합의 ≠ MVP-1 PASS 재선언** — Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지.

⚠️ **본 합의 ≠ Operational Readiness PASS (Layer E) 선언** — MVP-6 + Backlog #7 별도 영역.

⚠️ **본 합의 ≠ Hermes PMO 격상 (Layer F)** — MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무.

⚠️ **본 합의 ≠ T3 영역 자동 진입** — PC-4 T3 sub (`pre-commit install` 의무화 / dev 환경 강제) + AR-3 + Tier-2/3 catalog 확장 모두 Backlog #3 / Backlog #2 별도 합의 의무.

⚠️ **§C-5 전체 = `Partially Satisfied (C-5a + C-5c partial)` 갱신** — C-5b (ST-1) **Deferred 그대로 유지**.

⚠️ **§C-6 = `Partially Satisfied (PC-4 T2 sub only)` 갱신** — T-1 / T-3 / T-4 단독 + T-5 단독 강화 + PC-4 T3 sub + AR-3 **Deferred 그대로 유지**.

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-14 후속 5 — §C-5c + §C-6 부분 갱신 합의 결정 답습):

> "옵션 A로 진행해주세요. 본 brief 그대로 승인 → brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. C-5c와 C-6은 Partially Satisfied로만 갱신하고, MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 자동 진입은 하지 않음."

> "본 brief는 PC-4 T2 sub의 local validation 결과를 근거로, 다음 두 조건을 부분 갱신할 수 있는지 검토하는 단계입니다. C-5c = Partially Satisfied (T2 sub only) / C-6 = Partially Satisfied (PC-4 T2 sub only). 단, 다음은 유지합니다: C-5 전체 = Partially Satisfied / C-5b ST-1 = Deferred / PC-4 T3 sub = Deferred / C-6의 GP-5 1.5차 나머지 항목 = Deferred."

> "근거 evidence: pre-commit run --all-files = 6/6 PASS / runtime = 0.482초 / 6 hook local validation 완료."

> "합의 형태: Reviewer-only 단축 합의. 이유: 7/7 풀 3+1 승격 트리거 0건 / A-1 패턴 답습 / MVP-1 PASS 재선언 없음 / T3 영역 자동 진입 없음."

**사용자 명시 결정 답습**:
- 검토 형태 = Reviewer-only 단축 합의
- 검토 대상 = §C-5c + §C-6 양쪽 `Deferred → Partially Satisfied` 부분 갱신 적격성
- 판정 = **APPROVE — C-5c / C-6 Partially Satisfied**
- 합의 형태 = Reviewer-only 단축 합의 (`1dd1036` + `6fa87dc` chain 답습)
- 반영 방식 = **A-1 답습** (Layer D 합의 보고서 본문 변경 0건, 본 합의 보고서가 §C-5c + §C-6 부분 갱신 권위 source)
- **본 합의 범위** = §C-5c + §C-6 양쪽 *부분* 상태 표기 갱신 한정 — MVP-1 PASS 재선언 / Layer D 본문 변경 / §C-5c 전체 Satisfied / §C-6 전체 Satisfied / §C-5 전체 Satisfied / C-5b·C-1~C-4·C-5a·C-7·C-8 자동 변경 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / T3 영역 자동 진입 / 다른 backlog 자동 진입 / ADR 본문 자동 갱신 / ADR-012 §2.2 enum 정식 등록 **모두 불가**

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 검토 = brief §1~§8 + Cycle 4 chain *결과 행사* 한정 — 새 권위 도입 0건 + Layer D 본문 변경 0건 + §5.5 9 sub-수단 본문 채택 변경 0건 + ADR 본문 갱신 0건 + 도구 본문 / `.importlinter` config / `.pre-commit-config.yaml` 변경 0건 + CI workflow 변경 0건) | ✅ |
| 직전 합의 chain (Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독 / ST-2 실 구현 / Cycle 1~6 / §C-5a 갱신 / 선행 단독 PC-4 brief / 통합 brief / 통합 검토 / 진입 직전 brief / 진입 권한 / 구현 진입 / Cycle 4 + fix + 메타 모두 Reviewer-only) 패턴 답습 | ✅ |
| brief §8 본문 명시 답습 — "**Reviewer-only 단축 합의 적격 확정** (7/7 풀 3+1 트리거 0건 발화)" | ✅ |
| `1dd1036` + `6fa87dc` (§C-1 + §C-5a 갱신) A-1 패턴 본문 명시 답습 — "Layer D 합의 보고서 본문 변경 0건 + 본 합의 보고서가 갱신 권위 source" | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — 상태 표기 갱신 한정) | ✅ |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) | ✅ §0.1 답습 |
| **7/7 풀 3+1 승격 트리거 0건 발화** | ✅ §2 답습 |
| PC-4 T2 sub Cycle 4 + fix + 메타 chain 완료 + local pre-commit 6/6 PASS warm 0.482초 actual run evidence + 11/11 검증 항목 충족 + ADR-011 §2.1 (a)~(d) 4/4 충족 | ✅ §1 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독·실 구현·Cycle 1~6 / §C-5a 갱신 / 선행 단독 PC-4 brief / 통합 brief / 통합 검토 합의 / 진입 직전 brief / 진입 권한 합의 / 구현 진입 brief / 구현 진입 합의 / Cycle 4 + fix + 메타 commit / §C-5c+§C-6 갱신 합의 *준비 brief* 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

**청산 매커니즘**:
1. **사후 외부 LLM 충족 보존** — 누적 cross-vendor blind 의뢰 5건 답습 — 모두 권위 *내부* 작업으로 통합
2. **격상 전 면제 보존** — Hermes PMO 격상 *전 단계*. 본 검토 = §C-5c + §C-6 상태 표기 부분 갱신 한정 — Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 미진입
3. **합의 권위 내부 변경 한정** — 본 검토 = Cycle 4 chain + local pre-commit 6/6 PASS *결과 행사* — 권위 *내부 행사* 작업
4. **자기 작성 한계 명시** — 본 §0.3 + §5 명시
5. **A-1 패턴 답습** (Layer D 본문 변경 0건 + 본 합의 보고서가 §C-5c + §C-6 부분 갱신 권위 source, `1dd1036` + `6fa87dc` 답습)
6. **C-5c + C-6 부분 상태 표기 한정** (Layer D 합의 본문 변경 0건 + C-1~C-4·C-5a·C-5b·C-7·C-8 자동 변경 0건 + Layer E~F 미진입 + 다른 backlog 자동 진입 0건 + ADR 본문 갱신 0건 + 도구 본문 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건)
7. **외부 LLM cross-vendor blind 의뢰 미진입** — 7/7 단축 합의 적격 트리거 0건 발화 + 직전 합의 chain 일관성 + Cycle 4 actual run = 결정적 검증 (외부 추론 의존성 0건)

### 0.4 비검토 대상 (사용자 명시 4 금지 + 추가 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| **MVP-1 PASS *재선언*** | ❌ (Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지) |
| **Operational Readiness PASS (Layer E)** *선언* | ❌ (MVP-6 + Backlog #7 별도 영역) |
| **Hermes PMO 격상 (Layer F)** | ❌ (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| **T3 영역 *자동 진입*** | ❌ (`pre-commit install` 의무화 / dev 환경 강제 / branch protection / commit signing / required check / `default_install_hook_types` / `fail_fast` / commit-msg / pre-push stage / AR-3 / Tier-2/3 catalog 확장 모두 0건 — Backlog #3 / Backlog #2 보존) |
| **Layer D 합의 보고서 본문 변경** | ❌ (A-1 답습 — `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` 본문 변경 0건) |
| **§C-5c 전체 Satisfied 갱신** | ❌ (T3 sub Backlog #3 영역 보존 — Partially Satisfied (T2 sub only) 표기 한정) |
| **§C-6 전체 Satisfied 갱신** | ❌ (GP-5 1.5차 나머지 sub-수단 Backlog #2 보존 — Partially Satisfied (PC-4 T2 sub only) 표기 한정) |
| **§C-5 전체 Satisfied 갱신** | ❌ (C-5b ST-1 Deferred + C-5c T3 sub Deferred — Partially Satisfied (C-5a + C-5c partial) 표기 한정) |
| **C-5b (ST-1) *자동 진입*** | ❌ (Backlog #3 T3 영역 별도 풀 3+1 의무) |
| **C-1 / C-2 / C-3 / C-4 / C-5a / C-7 / C-8 *자동 변경*** | ❌ (§C-5c + §C-6 단독 부분 갱신 — 다른 7 Conditions 그대로 유지) |
| 다른 backlog (#3/#4/#7) *자동 진입* | ❌ |
| ADR 본문 *자동 갱신* | ❌ (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건) |
| ADR-012 §2.2 enum 정식 등록 (`pre_commit_config_local_definition_unified`) | ❌ (candidate-only 유지 — 별도 합의) |
| §5.5 9 sub-수단 본문 채택 *변경* | ❌ (`f40423f` + `55c5b4b` 답습) |
| 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `tools/workflow_secrets_usage_check.py` / `tools/workflow_permissions_check.py`) *변경* | ❌ |
| `.importlinter` config 본문 *변경* | ❌ (Group A 2차 답습) |
| `.pre-commit-config.yaml` 본문 *변경* | ❌ (Cycle 4 `b2f99f4` + fix `3d3cd21` 답습) |
| CI workflow *변경* | ❌ (PC-3 본문 채택 답습 그대로) |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |
| 외부 LLM 자동 호출 | ❌ |

---

## 1. 검토 기준 충족 분석 (8/8 + 11/11)

### 1.0 brief §1~§8 결과 답습

본 합의 = brief §1~§8 결과 *행사* 한정. 새 권위 결정 0건. 본 §1 = brief §1~§8 결과 답습 확정.

### 1.1 PC-4 T2 sub Cycle 4 + fix + 메타 chain 완료 검증 (brief §1)

| # | commit | 영역 | 검증 |
|---|--------|-----|-----|
| (1) | `b2f99f4 feat(pc4): add integrated pre-commit config` | `.pre-commit-config.yaml` 110 lines, 1 entry `repo: local`, 6 hook 정의 | ✅ Cycle 4 본문 완료 |
| (2) | `3d3cd21 fix(pc4): use python3 + scope secret-scanner to src/.github` | 3 lines (R-MVP1-G3-PC4-T2-INTG-8 `python3` 대체 4 entry + INTG-4 secret-scanner scope src + .github) | ✅ Trigger 발화 1회 통합 처리 |
| (3) | `5f878d6 docs(context): record PC-4 T2 pre-commit validation` | CONTEXT/INDEX/SESSION §39 (11 sub-section) | ✅ 메타 chain 보존 |

사용자 결정 3개 (α/ii/(가)) 답습 검증: (a) Cycle 분할 = α (1 entry `repo: local` 6 hook 통합) ✅ / (b) `import-linter` `language` = ii (`language: python` + `additional_dependencies: [import-linter==2.11]`) ✅ / (c) GP-3 도구 신설 = (가) 기존 Stage 5 `.py` 도구 reuse (Cycle 5 도구 신설 0건) ✅.

### 1.2 local `pre-commit run --all-files` actual run evidence 충분성 (brief §2)

| # | 검증 항목 | 결과 |
|---|--------|------|
| 1 | pre-commit 4.6.0 격리 venv 답습 | ✅ |
| 2 | secret-scanner hook (scope src + .github) | ✅ PASS |
| 3 | workflow-secret-usage-check hook | ✅ PASS |
| 4 | workflow-permissions-check hook | ✅ PASS |
| 5 | provider-import-scanner hook | ✅ PASS |
| 6 | provider-url-model-scanner hook | ✅ PASS |
| 7 | import-linter hook (venv 자동 install) | ✅ PASS |
| 8 | warm runtime 합산 | ✅ 0.482초 < 30초 (R-MVP1-G3-PC4-T2-INTG-3 발화 0건) |
| 9 | hook PASS 합산 | ✅ 6/6 |
| 10 | 사용자 결정 3개 (α/ii/(가)) 답습 | ✅ |
| 11 | Trigger 발화 처리 (INTG-8 + INTG-4 통합 1회) | ✅ fix `3d3cd21` |

→ **11/11 검증 항목 충족** + ADR-011 §2.1 (a)~(d) 4/4 충족 (a 보안 결과 / b 격리 PoC / c ADR·SDD 권위 / d 자동 회귀 — (e) 합의 APPROVE = 본 합의).

### 1.3 §C-5c = PC-4 sub-condition 분리 적절성 (brief §4)

| Sub-영역 | T2/T3 분류 | 본 Cycle 4 cover | Backlog 분리 |
|--------|--------|----------|------------|
| **T2 sub** = `.pre-commit-config.yaml` config 정의 (1 entry + 6 hook + opt-in) | T2 | ✅ Cycle 4 완료 + 6/6 PASS | Backlog #1 + #2 공유 — 본 합의 영역 |
| **T3 sub** = `pre-commit install` / dev 환경 강제 / branch protection / required check / `default_install_hook_types` / `fail_fast` / commit-msg / pre-push stage | T3 | ❌ 0건 (의도된 보존) | Backlog #3 T3 영역 — 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 |

**§C-5c sub-condition 분리 적절 — `Partially Satisfied (T2 sub only)` 권고 적격**.

### 1.4 §C-6 = GP-5 1.5차 보강 sub-수단 분리 적절성 (brief §5)

| Sub-수단 | 본 Cycle 4 cover | 본 evidence 적용 |
|---------|--------------|--------------|
| **PC-4 T2 sub** (provider-import + provider-url-model + import-linter 3 hook) | ✅ Cycle 4 + 3/3 PASS | ✅ 본 합의 영역 |
| **T-1 / T-3 / T-4 단독** | ❌ 0건 | Backlog #2 별도 영역 |
| **T-5 단독 강화** (도구 본문 / Tier-2/3 catalog 확장) | ❌ 0건 (도구 본문 변경 0건 답습) | Backlog #2 별도 영역 |
| **PC-4 T3 sub** | ❌ 0건 (T3 영역) | Backlog #3 T3 |
| **AR-3** (PR auto-reject runtime) | ❌ 0건 (T3 영역) | Backlog #3 T3 |

**§C-6 sub-수단 분리 적절 — `Partially Satisfied (PC-4 T2 sub only)` 권고 적격**.

### 1.5 §C-5 전체 = Partially Satisfied 갱신 적절성 (brief §6)

| Sub-condition | 상태 | 사유 |
|--------------|------|-----|
| C-5a (ST-2) | ✅ Satisfied (`6fa87dc`) | Cycle 1~6 완료 + actual run SUCCESS |
| **C-5c (PC-4)** | ✅ **Partially Satisfied (T2 sub only)** — 본 합의 권고 | Cycle 4 + local 6/6 PASS — T3 sub Backlog #3 보존 |
| C-5b (ST-1) | ⏳ **Deferred** | Backlog #3 T3 영역 별도 풀 3+1 의무 |

**§C-5 전체 = `Partially Satisfied (C-5a + C-5c partial)` 표기 갱신 — sibling 표기 패턴 답습**.

### 1.6 §C-5b (ST-1) / PC-4 T3 sub / GP-5 1.5차 나머지 보존 적절성 (brief §4 + §5)

| 영역 | 보존 사유 |
|------|---------|
| C-5b (ST-1 entrypoint stat) | T3 영역 (Hermes upstream Dockerfile 변경 필요) — Backlog #3 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 |
| C-5c PC-4 T3 sub (pre-commit install 의무화 / dev 환경 강제) | T3 영역 — Backlog #3 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 |
| C-6 GP-5 1.5차 나머지 (T-1/T-3/T-4 단독, T-5 강화, AR-3) | Backlog #2 별도 영역 — 도구 본문 변경 0건 답습 |

→ **사용자 명시 4 금지 #4 (T3 영역 자동 진입) 답습 + Backlog #2 / Backlog #3 분리 보존**.

### 1.7 MVP-1 PASS 재선언 없이 §C-5c + §C-6 만 부분 갱신 가능 (brief §7)

A-1 패턴 답습 (`1dd1036` + `6fa87dc` chain):

| 항목 | C-1 (K-2 fix) | C-5a (ST-2) | **C-5c + C-6 (본 합의)** |
|------|--------------|----------|------------------|
| 상태 변경 형태 | Deferred → Satisfied | Deferred → Satisfied | Deferred → Partially Satisfied (양쪽) |
| Layer D 본문 변경 | 0건 | 0건 | 0건 (A-1 답습) |
| 합의 권위 source | `1dd1036` 자체 | `6fa87dc` 자체 | 본 합의 보고서 자체 |
| MVP-1 PASS *재선언* | 0건 | 0건 | **0건 (Layer D `210c98f` 그대로 유지)** |
| Operational Readiness PASS (Layer E) | 0건 | 0건 | **0건** |
| Hermes PMO 격상 (Layer F) | 0건 | 0건 | **0건** |
| T3 영역 자동 진입 | 0건 | 0건 | **0건 (Backlog #3 보존)** |
| 다른 backlog 자동 진입 | 0건 | 0건 | 0건 |

→ **A-1 패턴 양쪽 sibling 답습 + 사용자 명시 4 금지 답습 — MVP-1 PASS 재선언 없이 §C-5c + §C-6 부분 갱신 가능**.

### 1.8 8/8 검토 기준 충족 합산

| # | 검토 기준 | 판정 |
|---|--------|------|
| 1 | PC-4 T2 sub Cycle 4 + fix + 메타 chain 완료 여부 | ✅ 3/3 commit 완료 |
| 2 | local `pre-commit run --all-files` actual run evidence 충분성 | ✅ 11/11 + ADR-011 §2.1 (a)~(d) 4/4 |
| 3 | §C-5c = PC-4 sub-condition 분리 적절성 (T2 / T3 분리) | ✅ Partially Satisfied (T2 sub only) 권고 |
| 4 | §C-6 = GP-5 1.5차 sub-수단 분리 적절성 (PC-4 T2 sub only / 나머지 Backlog #2) | ✅ Partially Satisfied (PC-4 T2 sub only) 권고 |
| 5 | §C-5 전체 = Partially Satisfied 갱신 적절성 (C-5a + C-5c partial) | ✅ sibling 표기 답습 |
| 6 | C-5b / PC-4 T3 sub / GP-5 1.5차 나머지 보존 적절성 | ✅ 각 backlog 분리 보존 |
| 7 | MVP-1 PASS 재선언 없이 §C-5c + §C-6 만 부분 갱신 가능 (A-1 패턴) | ✅ `1dd1036` + `6fa87dc` 답습 |
| 8 | 7/7 풀 3+1 트리거 0건 발화 → Reviewer-only 적격 | ✅ §2 답습 |

**합산 = 8/8 적절** — brief §1~§8 결과 + A-1 패턴 답습 + 풀 3+1 트리거 0건 발화 + 사용자 명시 4 금지 답습 모두 권위 근거 충실.

---

## 2. 풀 3+1 승격 트리거 검증 (7/7 0건 발화)

| # | 트리거 | 본 합의 검토 결과 |
|---|----|------------|
| 1 | 본 합의가 9 sub-수단 *외* 수단 *재결정* 권고 | ❌ 0건 발화 (영역 *상태 갱신* 답습 한정 — PC-3 본문 채택 답습 변경 0건) |
| 2 | 본 합의가 **T3 영역 *자동 진입*** 권고 | ❌ 0건 발화 (사용자 명시 4 금지 #4 답습 — `pre-commit install` 의무화 / dev 환경 강제 / branch protection / `fail_fast` / `default_install_hook_types` / commit-msg / pre-push stage / AR-3 / Tier-2/3 확장 모두 0건) |
| 3 | 본 합의가 사용자 명시 3 결정 (α/ii/(가)) *재변경* 권고 | ❌ 0건 발화 (Cycle 4 답습 한정) |
| 4 | 본 합의가 Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 발화 (`repo: local` + option (b)=ii pre-commit venv 격리 답습 + 외부 repo 의존 0건) |
| 5 | 본 합의가 5 영구 핵심 제약 약화 포함 | ❌ 0건 발화 (Hermes ≠ root of trust 보존 + 수단/목적 분리 보존 + 메타포 강제 금지 보존 + T3 분리 보존 + Provider Liquidity 보존) |
| 6 | 본 합의가 **MVP-1 PASS *재선언* / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상)** 포함 | ❌ 0건 발화 (사용자 명시 4 금지 #1 + #2 + #3 답습) |
| 7 | 본 합의가 외부 LLM *없이* T3 영역 결정 권고 | ❌ 0건 발화 (T3 결정 0건 — 사용자 명시 4 금지 #4 답습) |

**합산 = 7/7 0건 발화** → Reviewer-only 단축 합의 적격 확정.

---

## 3. §C-5c + §C-6 + §C-5 상태 표기 갱신

### 3.1 §C-5c 상태 표기 갱신 (본 합의 권위 source)

```
C-5c (PC-4 local pre-commit framework) = ✅ Partially Satisfied (T2 sub only) (`<본 합의 commit>`)
  T2 sub (.pre-commit-config.yaml + 6 hook + opt-in)   = Satisfied
    └ Cycle 4 (b2f99f4) + fix (3d3cd21) + 메타 (5f878d6)
    └ local pre-commit run --all-files = 6/6 PASS warm 0.482초
  T3 sub (pre-commit install / dev 환경 강제 / branch protection 등)
                                                        = ⏳ Deferred (Backlog #3 T3 영역)
```

### 3.2 §C-6 상태 표기 갱신 (본 합의 권위 source)

```
C-6 (GP-5 1.5차 보강 — Backlog #2) = ✅ Partially Satisfied (PC-4 T2 sub only) (`<본 합의 commit>`)
  PC-4 T2 sub (provider-import + provider-url-model + import-linter)  = Satisfied
    └ Cycle 4 (b2f99f4) GP-5 hook 3/3 PASS
  T-1 / T-3 / T-4 단독                                                  = ⏳ Deferred (Backlog #2 별도)
  T-5 단독 강화 (도구 본문 / Tier-2/3 catalog 확장)                      = ⏳ Deferred (Backlog #2 별도)
  PC-4 T3 sub / AR-3                                                    = ⏳ Deferred (Backlog #3 T3)
```

### 3.3 §C-5 전체 상태 표기 갱신 (본 합의 권위 source)

```
C-5 (GP-3 1.5차 보강 — Backlog #1) = ✅ Partially Satisfied (C-5a + C-5c partial)
  C-5a (ST-2 inotify sidecar)        = ✅ Satisfied (`6fa87dc`)
  C-5b (ST-1 entrypoint stat)        = ⏳ Deferred (Backlog #3 T3 영역)
  C-5c (PC-4 local pre-commit)       = ✅ Partially Satisfied (T2 sub only) — 본 합의
```

### 3.4 Layer D 본문 변경 0건 (A-1 답습)

`docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (`210c98f`) 본문 변경 0건 — 역사적 기록 보존. 본 합의 보고서가 §C-5c + §C-6 + §C-5 전체 표기 부분 갱신 권위 source.

---

## 4. 본 합의 발효 범위

### 4.1 본 합의가 *발생시키는* 것

| # | 영역 |
|---|------|
| 1 | §C-5c (PC-4 local pre-commit framework) `Deferred → Partially Satisfied (T2 sub only)` 갱신 (A-1 상태 표기 한정) |
| 2 | §C-6 (GP-5 1.5차 보강) `Deferred → Partially Satisfied (PC-4 T2 sub only)` 갱신 (A-1 상태 표기 한정) |
| 3 | §C-5 전체 상태 표기 갱신 = **`Partially Satisfied (C-5a + C-5c partial)`** |
| 4 | 본 합의 보고서 = §C-5c + §C-6 + §C-5 전체 부분 갱신 권위 source |
| 5 | PC-4 T2 sub Cycle 4 + fix + 메타 chain + local pre-commit 6/6 PASS evidence 권위 확정 |
| 6 | Reviewer-only 단축 합의 chain 답습 (A-1 sibling pattern — `1dd1036` + `6fa87dc` 후속) |
| 7 | 다음 단계 = 사용자 결정 영역 (자동 진입 0건) |

### 4.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 4 금지 + 추가 답습)

| # | 영역 | 본 합의 발효 시점 위반 |
|---|------|------------------|
| 1 | **MVP-1 PASS *재선언*** | **0건 (Layer D `210c98f` 판정 = APPROVE WITH CONDITIONS 그대로 유지)** |
| 2 | **Operational Readiness PASS (Layer E)** *선언* | **0건 (MVP-6 + Backlog #7 별도 영역)** |
| 3 | **Hermes PMO 격상 (Layer F)** | **0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무)** |
| 4 | **T3 영역 *자동 진입*** | **0건 (`pre-commit install` 의무화 / dev 환경 강제 / branch protection / commit signing / required check / `default_install_hook_types` / `fail_fast` / commit-msg / pre-push stage / AR-3 / Tier-2/3 catalog 확장 모두 0건 — Backlog #3 / Backlog #2 보존)** |
| 5 | Layer D 합의 보고서 *본문 변경* | 0건 (A-1 답습) |
| 6 | **§C-5c 전체 Satisfied 갱신** | 0건 (T3 sub Backlog #3 보존 — Partially Satisfied (T2 sub only) 표기 한정) |
| 7 | **§C-6 전체 Satisfied 갱신** | 0건 (GP-5 1.5차 나머지 Backlog #2 보존 — Partially Satisfied (PC-4 T2 sub only) 표기 한정) |
| 8 | **§C-5 전체 Satisfied 갱신** | 0건 (C-5b Deferred + C-5c T3 sub Deferred — Partially Satisfied (C-5a + C-5c partial) 표기 한정) |
| 9 | **C-5b (ST-1) *자동 진입* / 자동 갱신** | 0건 (Backlog #3 T3 미진입) |
| 10 | C-1 / C-2 / C-3 / C-4 / C-5a / C-7 / C-8 *자동 변경* | 0건 (§C-5c + §C-6 단독 부분 갱신) |
| 11 | 다른 backlog (#3 / #4 / #7) *자동 진입* | 0건 |
| 12 | ADR 본문 *자동 갱신* | 0건 |
| 13 | ADR-012 §2.2 enum 정식 등록 (`pre_commit_config_local_definition_unified`) | 0건 (candidate-only 유지) |
| 14 | §5.5 9 sub-수단 본문 채택 *변경* | 0건 (`f40423f` + `55c5b4b` 답습) |
| 15 | 도구 본문 (`tools/secret_scanner.py` / `tools/provider_*.py` / `tools/workflow_*.py`) *변경* | 0건 |
| 16 | `.importlinter` config 본문 *변경* | 0건 (Group A 2차 답습) |
| 17 | `.pre-commit-config.yaml` 본문 *변경* | 0건 (Cycle 4 `b2f99f4` + fix `3d3cd21` 답습) |
| 18 | CI workflow 본문 *변경* | 0건 (PC-3 본문 채택 답습 그대로) |
| 19 | 강제 commit blocking 정책 (`fail_fast` / `default_install_hook_types` 등) | 0건 |
| 20 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 21 | Cycle 5 도구 신설 0건 (사용자 결정 (가) 답습) | 0건 |
| 22 | Production `docker-compose.yml` *변경* | 0건 |
| 23 | Hermes upstream Dockerfile *변경* | 0건 |
| 24 | 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 25 | Provider Liquidity 5-way / 5 영구 핵심 제약 약화 | 0건 |
| 26 | CONTEXT / INDEX / SESSION 메타 갱신 (본 commit ≠ 메타 — 별도 commit 분리) | 0건 |

### 4.3 본 합의 발효 후 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 후보 | 영역 |
|------|------|
| (1) | CONTEXT / INDEX / SESSION 메타 갱신 commit (별도 commit 분리 답습 — 본 합의 직후) |
| (2) | PC-4 T3 sub / Backlog #3 풀 3+1 brief |
| (3) | Backlog #2 GP-5 1.5차 나머지 항목 brief |
| (4) | C-5b ST-1 / T3 영역 검토 |
| (5) | MVP-2 진입 합의 (G2 GP-2 + G4 §4.4 Layer 4) |
| (6) | 세션 종료 |

⚠️ **본 합의 APPROVE 직후 자동 다음 단계 진입 금지** — 사용자 명시 결정 의무.

⚠️ **§C-5b (ST-1) / §C-5c T3 sub / §C-6 GP-5 나머지 *자동 진입* 금지** — 각각 Backlog #3 / Backlog #2 별도 합의 의무.

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
Backlog #1 진입 *직전* 사전 정비                          — APPROVE AS BRIEF (43b898c)
ST-2 단독·실 구현·Cycle 1~6                                — 완료 (다중 commit)
ST-2 §C-5a Satisfied 갱신 (γ sub-condition 분리)          — APPROVE (6fa87dc) — §C-5a Satisfied
PC-4 T2 sub 선행 / 통합 / 진입 직전 / 진입 권한 / 구현 진입 — APPROVE (11d7ebb → e9614a6 → c292c9d → 611aab3 → 1efb75d → 3c0a1c1)
PC-4 T2 sub Cycle 4 + fix + 메타                           — 완료 (b2f99f4 + 3d3cd21 + 5f878d6, local 6/6 PASS warm 0.482초)
■ §C-5c + §C-6 Partially Satisfied 갱신 (T2 sub only)     — APPROVE (brief 3be81da + 본 합의 + 후속 메타 commit) ← 본 단계
§C-5 전체 = Partially Satisfied (C-5a + C-5c partial)     — 표기 갱신 (본 합의 권위)
C-5b ST-1                                                  — Deferred 그대로 유지
C-5c PC-4 T3 sub                                           — Deferred 그대로 유지 (Backlog #3)
C-6 GP-5 1.5차 나머지 (T-1/T-3/T-4/T-5 강화/AR-3)          — Deferred 그대로 유지 (Backlog #2)
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
| **C-5 (GP-3 1.5차 보강)** | ✅ **Partially Satisfied (C-5a + C-5c partial)** | **표기 갱신 (본 합의 권위)** |
| ├ C-5a (ST-2) | ✅ Satisfied (`6fa87dc`) | 변경 0건 |
| ├ C-5b (ST-1) | ⏳ **Deferred** | 변경 0건 (Backlog #3 T3) |
| **└ C-5c (PC-4)** | ✅ **Partially Satisfied (T2 sub only) (본 합의)** | **Deferred → Partially Satisfied** ✅ |
|   ├ T2 sub | ✅ Satisfied | Cycle 4 + 6/6 PASS |
|   └ T3 sub | ⏳ Deferred | Backlog #3 |
| **C-6 (GP-5 1.5차 보강)** | ✅ **Partially Satisfied (PC-4 T2 sub only) (본 합의)** | **Deferred → Partially Satisfied** ✅ |
| ├ PC-4 T2 sub | ✅ Satisfied | Cycle 4 GP-5 hook 3/3 PASS |
| ├ T-1 / T-3 / T-4 단독 | ⏳ Deferred | Backlog #2 |
| ├ T-5 단독 강화 | ⏳ Deferred | Backlog #2 |
| └ PC-4 T3 sub / AR-3 | ⏳ Deferred | Backlog #3 |
| C-7 | ⏳ Requires separate full 3+1 (Backlog #3) | 변경 0건 |
| C-8 | ⏳ Deferred (Backlog #4) | 변경 0건 |

**핵심**: 본 합의 = §C-5c + §C-6 양쪽 *부분* 상태 갱신 — Layer D 본문 변경 0건 + C-5 전체 = Partially Satisfied (C-5a + C-5c partial) 표기 한정 + C-5b·C-1/2/3/4/5a/7/8 그대로 유지 + Layer E·F 미진입.

### 5.3 본 합의 행사 의무 (사용자 명시 답습)

| 항목 | 의무 |
|------|------|
| commit 분리 (3 commit) | ✅ Commit 1 (brief `3be81da`) + Commit 2 (본 합의 — 본 commit) + Commit 3 (메타 갱신 — 후속) |
| CONTEXT / INDEX / SESSION 메타 갱신 분리 | ✅ 별도 commit (다음 단계) |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 자동 진입) | ✅ §0.1 + §0.4 + §4.2 답습 |
| C-5b / PC-4 T3 sub / GP-5 1.5차 나머지 자동 진입 금지 | ✅ §4.2 답습 |
| MVP-1 PASS 재선언 금지 | ✅ §3.4 답습 |
| 다른 backlog 자동 진입 금지 | ✅ §4.2 답습 |

---

## 6. 메타 검증

| 메타 검증 | 본 합의 |
|---------|--------|
| 사용자 명시 진입 명령 답습 (옵션 (A) + A-1 답습 + Partially Satisfied 양쪽 + Layer D 본문 변경 0건 + 4 금지) | ✅ |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 자동 진입) | ✅ (§0.4 + §4.2 답습) |
| 8/8 검토 기준 충족 (brief §1~§8 답습 + A-1 패턴 답습 + 풀 3+1 트리거 0건 발화) | ✅ §1.8 |
| 7/7 풀 3+1 승격 트리거 0건 발화 | ✅ §2 |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| C-1~C-8 상태 답습 (C-5c + C-6 양쪽 부분 갱신 / Partially Satisfied 표기 한정 / 나머지 7 Conditions 그대로) | ✅ §5.2 |
| Layer D 본문 변경 0건 (`210c98f` 그대로 유지) | ✅ (A-1 답습) |
| MVP-1 PASS *재선언* 0건 | ✅ |
| Operational Readiness PASS (Layer E) 선언 0건 | ✅ |
| Hermes PMO 격상 (Layer F) 0건 | ✅ |
| T3 영역 자동 진입 0건 (Backlog #3 + Backlog #2 GP-5 나머지 보존) | ✅ |
| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ |
| 5 영구 핵심 제약 보존 | ✅ (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단·목적 분리) |
| 7 backlog 분리 매트릭스 답습 | ✅ |
| 자동 진입 0건 (C-5b / PC-4 T3 / GP-5 나머지 / 다른 backlog / T3 / Layer E·F) | ✅ |
| 도구 본문 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건 | ✅ |
| ADR-012 §2.2 enum 정식 등록 0건 (candidate-only 유지) | ✅ |
| 합의 권위 자기 내부 변경 한정 (외부 LLM 미진입) | ✅ |

---

## 7. 본 합의 요약 (한 단락)

본 합의 는 **Backlog #1 + #2 통합 PC-4 T2 sub `.pre-commit-config.yaml` Cycle 4 chain (`b2f99f4` + `3d3cd21` + `5f878d6`) + local `pre-commit run --all-files` warm 6/6 PASS (0.482초 < 30초 충족) evidence 위에서 §C-5c (PC-4 local pre-commit framework) + §C-6 (GP-5 1.5차 보강) 양쪽 *Deferred → Partially Satisfied* 부분 갱신 (Reviewer-only 단축 합의, A-1 상태 표기 한정)** 이다. 11/11 검증 항목 + ADR-011 §2.1 (a)~(d) 4/4 충족 + 사용자 결정 3개 (α/ii/(가)) 답습 일관 + 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입). 8/8 검토 기준 충족 (Cycle 4 + fix + 메타 chain 완료 / actual run evidence 충분성 / §C-5c sub-condition 분리 적절성 / §C-6 sub-수단 분리 적절성 / §C-5 전체 Partially Satisfied 갱신 적절성 / C-5b·T3 sub·GP-5 나머지 보존 적절성 / MVP-1 PASS 재선언 없이 §C-5c + §C-6 만 부분 갱신 가능 / 풀 3+1 트리거 0건 발화) + **7/7 풀 3+1 트리거 0건 발화** → Reviewer-only 단축 합의 적격 확정. **상태 표기 갱신**: **§C-5c = Partially Satisfied (T2 sub only)** (T3 sub Backlog #3 Deferred) / **§C-6 = Partially Satisfied (PC-4 T2 sub only)** (T-1/T-3/T-4 단독·T-5 강화·PC-4 T3 sub·AR-3 Backlog #2/#3 Deferred) / **§C-5 전체 = Partially Satisfied (C-5a + C-5c partial)** (C-5b Deferred). **A-1 패턴 답습** (`1dd1036` §C-1 + `6fa87dc` §C-5a 갱신 chain 답습): Layer D 합의 보고서 (`210c98f`) **본문 변경 0건** (역사적 기록 보존) + 본 합의 보고서가 §C-5c + §C-6 + §C-5 전체 부분 갱신 권위 source. **본 합의 ≠ MVP-1 PASS 재선언 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / T3 영역 자동 진입 / §C-5c 전체 Satisfied / §C-6 전체 Satisfied / §C-5 전체 Satisfied / C-5b·C-1~C-4·C-5a·C-7·C-8 자동 변경 / 다른 backlog 자동 진입 / ADR 본문 자동 갱신 / ADR-012 §2.2 enum 정식 등록 / 도구 본문 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 / Tier-2/3 catalog 자동 확장 / 외부 LLM 자동 호출** (사용자 명시 4 금지 답습). 다음 단계 = 사용자 결정 영역 (메타 commit / PC-4 T3 sub brief / Backlog #2 GP-5 1.5차 brief / C-5b ST-1 검토 / MVP-2 / 세션 종료).

---

**합의 일자**: 2026-05-14 후속 5
**판정**: ✅ **APPROVE — §C-5c (PC-4) + §C-6 (GP-5 1.5차) Deferred → Partially Satisfied 양쪽 부분 갱신 (Reviewer-only 단축 합의, A-1 상태 표기 한정, Layer D 본문 변경 0건)**
**다음 단계**: CONTEXT / INDEX / SESSION 메타 갱신 commit (별도 commit 분리 답습) — 사용자 명시 결정 후 진입

**금지 (사용자 명시 4 금지 답습 — 본 합의 영역 + 본 합의 발효 후 단계 양쪽)**:
- ❌ **MVP-1 PASS *재선언*** (Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지)
- ❌ **Operational Readiness PASS (Layer E)** *선언* (MVP-6 + Backlog #7 별도 영역)
- ❌ **Hermes PMO 격상 (Layer F)** (MVP-6 + 외부 LLM 의무)
- ❌ **T3 영역 *자동 진입*** (`pre-commit install` 의무화 / dev 환경 강제 / branch protection / `fail_fast` / `default_install_hook_types` / commit-msg / pre-push stage / AR-3 / Tier-2/3 확장 모두 0건)
- ❌ Layer D 합의 보고서 *본문 변경* (A-1 답습)
- ❌ **§C-5c 전체 Satisfied 갱신** (Partially Satisfied (T2 sub only) 표기 한정)
- ❌ **§C-6 전체 Satisfied 갱신** (Partially Satisfied (PC-4 T2 sub only) 표기 한정)
- ❌ **§C-5 전체 Satisfied 갱신** (Partially Satisfied (C-5a + C-5c partial) 표기 한정)
- ❌ **C-5b (ST-1) *자동 갱신* / *자동 진입***
- ❌ C-1 / C-2 / C-3 / C-4 / C-5a / C-7 / C-8 상태 *자동 변경*
- ❌ PC-4 T3 sub / GP-5 1.5차 나머지 *자동 진입*
- ❌ 다른 backlog (#3 / #4 / #7) *자동 진입*
- ❌ ADR 본문 *자동 갱신*
- ❌ ADR-012 §2.2 enum *정식 등록* (`pre_commit_config_local_definition_unified` candidate-only 유지)
- ❌ §5.5 9 sub-수단 본문 채택 *변경*
- ❌ 도구 본문 / `.importlinter` config / `.pre-commit-config.yaml` 본문 *변경*
- ❌ CI workflow 본문 *변경*
- ❌ 강제 commit blocking 정책 (`fail_fast` / `default_install_hook_types` 등) 추가
- ❌ Cycle 5 도구 신설 (사용자 결정 (가) 답습 — 기존 Stage 5 `.py` reuse)
- ❌ Production `docker-compose.yml` *변경*
- ❌ Hermes upstream Dockerfile *변경*
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 사용자 명시 3 결정 (α/ii/(가)) *재변경*
- ❌ 외부 LLM *자동 호출* / 실 API key / provider SDK / 외부 API 호출
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 (본 commit ≠ 메타 갱신 — 별도 commit 분리 답습)
