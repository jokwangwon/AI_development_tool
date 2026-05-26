# PC-4 T2 actual evidence / §C-5c + §C-6 갱신 Brief (DRAFT)

> **본 brief = `.pre-commit-config.yaml` 6 hook local validation 결과 (`pre-commit run --all-files` warm 0.482초, 6/6 PASS) 를 *근거*로, §C-5c (PC-4 local pre-commit framework) + §C-6 (GP-5 1.5차 보강) 를 **Satisfied** 또는 **Partially Satisfied** 로 갱신할 수 있는지 *검토 준비안* (DRAFT)** — 본 brief 의 어떤 §도 그 자체로 §C-5c·§C-6 Satisfied 갱신 발효를 발생시키지 않는다.
>
> 본 brief 의 어떤 §도 (i) §C-5c / §C-6 Satisfied 자동 갱신, (ii) Layer D 합의 보고서 본문 변경, (iii) **MVP-1 PASS 재선언**, (iv) **Operational Readiness PASS** 선언, (v) **Hermes PMO 격상**, (vi) **T3 영역 자동 진입**, (vii) 다른 backlog (#3/#4/#7) 자동 진입, (viii) ADR 본문 자동 갱신, (ix) ADR-012 §2.2 `event` enum 정식 등록, (x) `pre-commit install` 의무화 / dev 환경 강제, (xi) branch protection / CI workflow 변경, (xii) 도구 본문 / `.importlinter` config 변경, (xiii) §5.5 9 sub-수단 본문 채택 변경, (xiv) Tier-2 / Tier-3 catalog 자동 확장, (xv) 외부 LLM 자동 호출 을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 5
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위**:
- 구현 진입 합의 = `3c0a1c1 docs(review): approve PC-4 T2 implementation entry` (Reviewer-only 단축, APPROVE — 실 구현 진입 권한 발효)
- 구현 진입 brief = `edf1f89 docs(phase0): add PC-4 T2 implementation brief` (793 lines, 사용자 결정 3개 α/ii/ii 확정)
- Cycle 4 본문 = `b2f99f4 feat(pc4): add integrated pre-commit config` (`.pre-commit-config.yaml` 110 lines, 1 entry `repo: local`, 6 hook 정의)
- Cycle 4 fix = `3d3cd21 fix(pc4): use python3 + scope secret-scanner to src/.github` (R-MVP1-G3-PC4-T2-INTG-8 + INTG-4 통합 처리)
- 메타 commit = `5f878d6 docs(context): record PC-4 T2 pre-commit validation` (CONTEXT/INDEX/SESSION §39)
- §C-5a Satisfied 패턴 답습 = `6fa87dc docs(review): approve ST-2 C-5a satisfaction` (A-1 패턴 — Layer D 본문 변경 0건)
- MVP-1 PASS (Layer D) = `210c98f docs(review): approve mvp1 pass` (APPROVE WITH CONDITIONS)
- §C-1 갱신 패턴 답습 = `1dd1036` (A-1 패턴 — 상태 표기 한정 갱신)
- §5.5 본문 채택 = `f40423f` + `55c5b4b` (양 GP PC-3 일관 본문 채택)
- 도구 검증 답습: `tools/secret_scanner.py` (Group D `25623028888`) / `tools/provider_import_scanner.py` (Group A 1차) / `tools/provider_url_scanner.py` (Group A 3차 `25629390384`) / `lint-imports` + `.importlinter` (Group A 2차 `25605665191`)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 5)

> "PC-4 T2 actual evidence / C-5c+C-6 갱신 brief 를 작성해주세요. 범위는 `.pre-commit-config.yaml` 6 hook local validation 결과를 근거로, C-5c 와 C-6 을 Satisfied 또는 Partially Satisfied 로 갱신할 수 있는지 검토하는 것입니다. MVP-1 PASS 재선언, Operational Readiness PASS, Hermes PMO 격상, T3 영역 자동 진입은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. Cycle 4 + fix + 메타 chain 완료 여부 검증 (§1)
2. local `pre-commit run --all-files` actual run evidence 충분성 평가 (§2)
3. ADR-011 §2.1 (a)~(e) 5조건 답습 매핑 (§3)
4. §C-5c (PC-4 local pre-commit framework) 갱신 적격성 검토 — Satisfied vs Partially Satisfied (§4)
5. §C-6 (GP-5 1.5차 보강) 갱신 적격성 검토 — Satisfied vs Partially Satisfied (§5)
6. §C-5 전체 표기 갱신 후보 검토 (§6)
7. MVP-1 PASS *재선언 없이* §C-5c + §C-6 만 갱신 가능 여부 (A-1 패턴 답습) (§7)
8. 합의 형태 권고 + 7/7 풀 3+1 트리거 검증 (§8)
9. 메타 검증 (§9)
10. 다음 단계 결정 옵션 (부록 A)
11. 금지 사항 (부록 B)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 4 금지 + 추가)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | **MVP-1 PASS *재선언*** | 0건 (Layer D `210c98f` 그대로 유지) |
| 2 | **Operational Readiness PASS** (Layer E) 선언 | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 3 | **Hermes PMO 격상** (Layer F) | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| 4 | **T3 영역 자동 진입** | 0건 (`pre-commit install` 의무화 / dev 환경 강제 / branch protection / commit signing / required check 모두 0건) |
| (추가) | §C-5c / §C-6 *Satisfied 자동 갱신* | 0건 (본 brief = 준비안 — 합의 보고서 = 별도 단계) |
| (추가) | Layer D 합의 보고서 *본문 변경* | 0건 (A-1 패턴 답습) |
| (추가) | C-2 ~ C-4 / C-5a / C-5b / C-7 / C-8 자동 변경 | 0건 |
| (추가) | §5.5 9 sub-수단 본문 채택 변경 | 0건 (양 GP PC-3 본문 채택 유지) |
| (추가) | ADR 본문 자동 갱신 | 0건 |
| (추가) | ADR-012 §2.2 `event` enum 정식 등록 | 0건 (`pre_commit_config_local_definition_unified` candidate-only 유지) |
| (추가) | 도구 본문 (`tools/secret_scanner.py` / `tools/provider_*.py` / `tools/workflow_*.py`) 변경 | 0건 |
| (추가) | `.importlinter` config 본문 변경 | 0건 |
| (추가) | `.pre-commit-config.yaml` 본문 *변경* | 0건 (본 brief = 검토 준비안, 본문 작성/수정 0건) |
| (추가) | CI workflow 변경 | 0건 (PC-3 본문 채택 답습 그대로) |
| (추가) | 강제 commit blocking 정책 (`fail_fast` / `default_install_hook_types` / commit-msg / pre-push stage 추가) | 0건 |
| (추가) | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| (추가) | 다른 backlog (#3/#4/#7) 자동 진입 | 0건 |
| (추가) | 외부 LLM 자동 호출 | 0건 |
| (추가) | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| (추가) | 합의 보고서 *작성* / commit / push | 0건 (본 brief 파일화 + commit = 사용자 명시 후속) |

### 0.4 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 본 brief 가 발생시키는 *유일한* 효과 = **§C-5c·§C-6 부분 Satisfied 갱신 합의 *직전* 의사결정 입력 정비 — 갱신 범위 (전체 Satisfied vs Partially Satisfied) 결정 + Layer D 본문 변경 0건 패턴 답습 + 합의 형태 권고 + 7/7 트리거 검증**.

---

## 1. Cycle 4 + fix + 메타 chain 완료 검증 (검토 영역 #1)

### 1.1 commit chain 완료 매트릭스

| # | commit | 영역 | 검증 |
|---|--------|-----|-----|
| (1) | `b2f99f4 feat(pc4): add integrated pre-commit config` | `.pre-commit-config.yaml` 110 lines, 1 entry `repo: local`, 6 hook 정의 | ✅ Cycle 4 본문 작성 완료 |
| (2) | `3d3cd21 fix(pc4): use python3 + scope secret-scanner to src/.github` | 3 lines 수정 (R-MVP1-G3-PC4-T2-INTG-8 `python` → `python3` 4 entry + INTG-4 secret-scanner scope = src + .github 한정) | ✅ Trigger 발화 1회 통합 처리 |
| (3) | `5f878d6 docs(context): record PC-4 T2 pre-commit validation` | CONTEXT/INDEX/SESSION 메타 갱신 (§39 신설 11 sub-section) | ✅ 메타 chain 보존 |

### 1.2 사용자 결정 3개 (α/ii/(가)) 답습 검증

| 결정 영역 | 사용자 결정 | Cycle 4 적용 |
|---------|---------|-----------|
| (a) Cycle 분할 정책 | α (1 Cycle 통합) | ✅ 6 hook 한 번에 통합 정의 (1 entry `repo: local`) |
| (b) `import-linter` `language` 옵션 | ii (`language: python` + `additional_dependencies: [import-linter==2.11]`) | ✅ Cycle 4 본문 line 99~107 채택 — `.importlinter` config 본문 변경 0건 |
| (c) GP-3 도구 신설 옵션 | (가) 기존 Stage 5 `.py` 도구 reuse — Cycle 5 도구 신설 0건 | ✅ entry `python3 tools/workflow_secrets_usage_check.py` + `python3 tools/workflow_permissions_check.py` (도구 본문 변경 0건) |

### 1.3 §1 판정

✅ **Cycle 4 + fix + 메타 chain = 완료 확정** — 3 commit chain (`b2f99f4` → `3d3cd21` → `5f878d6`) + 사용자 결정 3개 답습 일관 + 도구 본문 / `.importlinter` config / CI workflow 변경 0건 보존.

---

## 2. local `pre-commit run --all-files` actual run evidence 충분성 평가 (검토 영역 #2)

### 2.1 actual run 결과 매트릭스

| # | 검증 항목 | 결과 | 비고 |
|---|--------|------|------|
| 1 | pre-commit 4.6.0 격리 venv 답습 | ✅ | option (b)=ii 답습 — `language: python` venv 자동 install |
| 2 | secret-scanner hook | ✅ PASS | scope = src + .github 한정 (fix 답습) |
| 3 | workflow-secret-usage-check hook | ✅ PASS | `.github/workflows/*.yml` 대상 |
| 4 | workflow-permissions-check hook | ✅ PASS | `.github/workflows/*.yml` 대상 |
| 5 | provider-import-scanner hook | ✅ PASS | `src/` 대상 |
| 6 | provider-url-model-scanner hook | ✅ PASS | url-endpoint + model-name 2 mode |
| 7 | import-linter hook | ✅ PASS | `import-linter==2.11` venv 자동 install 정상 |
| 8 | warm runtime 합산 | ✅ 0.482초 | < 30초 충족 (R-MVP1-G3-PC4-T2-INTG-3 발화 0건) |
| 9 | hook PASS 합산 | ✅ 6/6 | 1/6 fail 검출 0건 |
| 10 | 사용자 결정 3개 (α/ii/(가)) 답습 | ✅ | §1.2 답습 |
| 11 | Trigger 발화 처리 | ✅ fix 1회 통합 | INTG-8 (`python3` 대체) + INTG-4 (scope src/.github) 통합 — fix commit `3d3cd21` |

### 2.2 본 evidence 의 *범위*

| 영역 | 본 evidence cover |
|------|----------------|
| `.pre-commit-config.yaml` config 자체 schema 유효성 | ✅ (`pre-commit run --all-files` 정상 가동 = schema 유효) |
| 6 hook entry 명령 가동 가능성 | ✅ (6/6 hook 정상 호출) |
| 6 hook PASS 결과 (현 시점 repo 본문 기준) | ✅ (6/6 PASS) |
| warm runtime < 30초 권고 충족 | ✅ (0.482초 = 0.16% 사용) |
| import-linter venv 격리 install 가동성 | ✅ (option (b)=ii 답습 venv 정상) |
| 사용자 결정 3개 답습 일관 | ✅ |
| opt-in 본질 보존 | ✅ (`pre-commit install` 의무화 0건 / `default_install_hook_types` 0건 / `fail_fast` 0건 / README 강제 install 0건) |
| 도구 본문 변경 0건 | ✅ (Cycle 5 도구 신설 0건 답습) |
| CI workflow 변경 0건 | ✅ (PC-3 본문 채택 답습 그대로) |
| FP / FN 검출 (Tier-1 답습 패턴) | ⚠️ 본 actual run = 현 시점 repo 본문 기준 6/6 PASS 한정 — 의도된 fail fixture 검증 = ❌ 영역 외 (각 도구 PoC actual run 답습 답습) |

### 2.3 본 evidence 의 *범위 외* (사후 영역)

- 의도된 fail fixture 검출 검증 (각 도구 PoC actual run 답습 — Group D `25623028888` + Group A 1차/2차/3차 actual run + Stage 5)
- cold install runtime 측정 (warm 측정 0.482초 한정)
- branch protection 강제 / pre-commit install 강제 / dev 환경 install 시연 (T3 영역)
- multi-host 운영 시뮬레이션 (Operational Readiness — Layer E 영역)
- Hermes PMO 격상 의무 cross-vendor blind 의뢰 (Layer F 영역)

### 2.4 §2 판정

✅ **actual run evidence 충분 — Cycle 4 본문 작성 + opt-in 보조 장치 가동성 검증 한정** — `.pre-commit-config.yaml` config 정의 영역 (T2 sub) cover 완료. T3 영역 / Layer E / Layer F evidence 0건 (의도된 보존).

---

## 3. ADR-011 §2.1 (a)~(e) 5조건 답습 매핑 (검토 영역 #3)

### 3.1 ADR-011 §2.1 5조건 매트릭스

| # | 조건 | 본 evidence 매핑 |
|---|------|--------------|
| (a) | 동등 이상의 보안 결과 | ✅ PC-3 (CI gating) 위 opt-in defense in depth 추가 (강제 효과 0건) — 양 GP PC-3 본문 채택 답습 (`55c5b4b`) 보존 + local hook = 사전 알림 보조 한정 |
| (b) | 격리 환경 PoC 실증 | ✅ local repo 격리 환경 `pre-commit run --all-files` 가동 + 6 hook 동작 시연 (warm 0.482초) — pre-commit 4.6.0 격리 venv 답습 |
| (c) | ADR / SDD 권위 명시 | ✅ mvp1.md §4.3 + §5.5.1 + §5.5.2 + ADR-011 §2.4 + 선행 brief chain (`11d7ebb` + `e9614a6` + `c292c9d` + `611aab3` + `1efb75d` + `edf1f89` + `3c0a1c1` + 본 brief) 답습 |
| (d) | 자동 회귀 검증 경로 확보 | ✅ (i) `.pre-commit-config.yaml` schema 자체 검증 (pre-commit 가동 시) + (ii) opt-in 한정 동작 검증 (재현 가능) + (iii) CI gating 답습 (PC-3 강제 — 도구 본문 단일 source-of-truth 유지) |
| (e) | 합의 APPROVE | ⏳ 본 brief = 준비안 — 후속 합의 보고서 (§C-5c + §C-6 부분 Satisfied 갱신) 영역 |

### 3.2 §3 판정

✅ **ADR-011 §2.1 (a)~(d) 4/4 충족** — (e) 합의 APPROVE = 본 brief 후속 합의 보고서 영역.

---

## 4. §C-5c (PC-4 local pre-commit framework) 갱신 적격성 검토 (검토 영역 #4)

### 4.1 §C-5c 현 상태 (`5f878d6` 후 시점)

```
C-5c (PC-4 local pre-commit framework) = ⏳ Deferred
   사유 (이전): Backlog #1 + #2 공유 영역 (T2 + T3 혼합) — 미진입
   사유 (현 시점): T2 sub 영역 = Cycle 4 완료 + actual run 6/6 PASS — T3 sub 영역 = 미진입 그대로
```

### 4.2 PC-4 sub-영역 분해 매트릭스

| Sub-영역 | T2/T3 분류 | 본 Cycle 4 cover | Backlog 분리 |
|--------|--------|----------|------------|
| **T2 sub** = `.pre-commit-config.yaml` config 정의 (1 entry `repo: local` + 6 hook 정의 + opt-in 보조 가동) | T2 (사용자 명시 결정 한정) | ✅ Cycle 4 완료 + actual run 6/6 PASS | Backlog #1 + #2 공유 — 본 brief 영역 |
| **T3 sub** = `pre-commit install` 의무화 / dev 환경 강제 / branch protection / required check / `default_install_hook_types` / `fail_fast` / commit-msg / pre-push stage 추가 | T3 (Hermes upstream / branch protection / 사용자 명시 + 외부 LLM 1+ 의무) | ❌ 0건 (의도된 보존) | Backlog #3 T3 영역 — *별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시* 의무 |

### 4.3 §C-5c 갱신 후보 표기

| 후보 | 의미 | 본 evidence 적합성 |
|------|-----|----------------|
| (i) `Satisfied` (전체) | T2 + T3 sub 모두 충족 | ❌ **부적합** — T3 sub 영역 (Backlog #3) 미진입 + 본 brief 사용자 명시 4 금지 #4 답습 |
| (ii) `Partially Satisfied (T2 sub only)` | T2 sub 한정 충족 + T3 sub 보존 | ✅ **적합** — Cycle 4 evidence 6/6 PASS + T3 sub 보존 + sibling 패턴 답습 |
| (iii) `Deferred` 그대로 유지 | 갱신 없음 | ⚠️ Cycle 4 evidence *행사* 안 함 — 보존 가치 낮음 |

### 4.4 sibling 패턴 답습 검증

| Condition | 분리 패턴 |
|----------|----------|
| C-5a (ST-2) | Satisfied 갱신 — `6fa87dc` A-1 답습 (Layer D 본문 변경 0건) |
| **C-5c 본 brief** | **Partially Satisfied (T2 sub only) 권고** — A-1 패턴 답습 + ST-2 C-5a 직전 sibling 답습 |
| C-5b (ST-1) | Deferred 그대로 유지 (Backlog #3 T3 영역 미진입) |

### 4.5 §4 판정

✅ **§C-5c = `Partially Satisfied (T2 sub only)` 갱신 권고 적격** — T2 sub Cycle 4 evidence 6/6 PASS + T3 sub 영역 (Backlog #3) 보존 + sibling 패턴 답습 (C-5a) + A-1 패턴 답습 (Layer D 본문 변경 0건).

---

## 5. §C-6 (GP-5 1.5차 보강) 갱신 적격성 검토 (검토 영역 #5)

### 5.1 §C-6 현 상태 (`5f878d6` 후 시점)

```
C-6 (GP-5 1.5차 보강 — Backlog #2) = ⏳ Deferred
   사유 (이전): GP-5 Layer 1 보강 영역 (T-1/T-3/T-4/T-5 단독/PC-4/AR-3 분리)
   사유 (현 시점): PC-4 T2 sub 한정 cover — 나머지 sub-수단 보존
```

### 5.2 GP-5 1.5차 보강 영역 분해 매트릭스 (mvp1.md §5.5.2 답습)

| Sub-수단 | 본 Cycle 4 cover | 본 evidence 적용 |
|---------|--------------|--------------|
| **PC-4 T2 sub** (`.pre-commit-config.yaml` GP-5 hook 3개 — provider-import-scanner / provider-url-model-scanner / import-linter) | ✅ Cycle 4 본문 정의 + actual run 3/3 PASS (GP-5 hook 한정) | ✅ 본 brief 영역 |
| **T-1 단독** (별도 Layer 1 정적 검출 도구 추가 — DRAFT 영역) | ❌ 0건 (분리 보존) | Backlog #2 별도 영역 |
| **T-3 단독** (Layer 1 정적 검출 보강 — DRAFT 영역) | ❌ 0건 (분리 보존) | Backlog #2 별도 영역 |
| **T-4 단독** (Layer 1 정적 검출 보강 — DRAFT 영역) | ❌ 0건 (분리 보존) | Backlog #2 별도 영역 |
| **T-5 단독 강화** (현 시점 도구 본문 변경 — Tier-2/3 catalog 확장 등) | ❌ 0건 (사용자 명시 답습 — 도구 본문 변경 0건) | Backlog #2 별도 영역 |
| **PC-4 T3 sub** (`pre-commit install` 의무화 / dev 환경 강제) | ❌ 0건 (T3 영역) | Backlog #3 T3 영역 |
| **AR-3** (PR auto-reject runtime — branch protection 영역) | ❌ 0건 (T3 영역) | Backlog #3 T3 영역 |

### 5.3 §C-6 갱신 후보 표기

| 후보 | 의미 | 본 evidence 적합성 |
|------|-----|----------------|
| (i) `Satisfied` (전체) | GP-5 1.5차 보강 전체 sub-수단 충족 | ❌ **부적합** — T-1/T-3/T-4 단독 + T-5 단독 강화 + PC-4 T3 sub + AR-3 모두 미진입 |
| (ii) `Partially Satisfied (PC-4 T2 sub only)` | PC-4 T2 sub 한정 충족 + 나머지 sub-수단 보존 | ✅ **적합** — Cycle 4 evidence GP-5 hook 3/3 PASS + 나머지 sub-수단 보존 |
| (iii) `Deferred` 그대로 유지 | 갱신 없음 | ⚠️ Cycle 4 evidence *행사* 안 함 — 보존 가치 낮음 |

### 5.4 §C-6 ↔ §C-5c 동시 부분 갱신 권고

| 영역 | 권고 |
|------|-----|
| 단일 합의 보고서 | ✅ 권고 (1 파일 = 1 합의 = 양 GP 동시 부분 갱신) — 구현 진입 brief §14.3 답습 |
| 갱신 표기 | (a) §C-5c = `Partially Satisfied (T2 sub only)` + (b) §C-6 = `Partially Satisfied (PC-4 T2 sub only)` + 양쪽 evidence source = 동일 (`b2f99f4` + `3d3cd21` + `5f878d6` + 합의 commit) |

### 5.5 §5 판정

✅ **§C-6 = `Partially Satisfied (PC-4 T2 sub only)` 갱신 권고 적격** — Cycle 4 evidence GP-5 hook 3/3 PASS + 나머지 sub-수단 (T-1/T-3/T-4 단독, T-5 강화, PC-4 T3 sub, AR-3) 보존 + §C-5c 와 동시 단일 합의 권고.

---

## 6. §C-5 전체 표기 갱신 후보 검토 (검토 영역 #6)

### 6.1 §C-5 전체 현 상태 (`6fa87dc` 후 + `5f878d6` 후 시점, 변경 0건)

```
C-5 전체 = ⏳ Partially Satisfied (C-5a only)
   C-5a (ST-2 inotify sidecar)        = ✅ Satisfied (`6fa87dc`)
   C-5b (ST-1 entrypoint stat)        = ⏳ Deferred (Backlog #3 T3 영역)
   C-5c (PC-4 local pre-commit)       = ⏳ Deferred (현 시점 — 본 brief 후속 갱신 권고)
```

### 6.2 §C-5c 갱신 시 §C-5 전체 표기 후보

| 후보 | 표기 | 의미 |
|------|-----|-----|
| (i) | `Partially Satisfied (C-5a only)` 그대로 유지 | C-5c 부분 Satisfied = "전체 Satisfied" 카운트 부족 — 보수적 |
| (ii) | `Partially Satisfied (C-5a + C-5c partial)` | C-5a 완전 + C-5c 부분 명시 — 정밀한 표기 |
| (iii) | `Satisfied` (전체) | ❌ 부적합 — C-5b (ST-1) Deferred + C-5c T3 sub 보존 |

### 6.3 권고 = (ii) — sibling 표기 패턴 답습

본 brief 권고: **(ii) `Partially Satisfied (C-5a + C-5c partial)`** — 양쪽 sub-condition 상태 명시 + Layer D 본문 변경 0건 (A-1 답습) + 합의 보고서 권위 source.

### 6.4 §6 판정

✅ **§C-5 전체 = `Partially Satisfied (C-5a + C-5c partial)` 갱신 권고** — sibling 표기 패턴 답습 + sub-condition 상태 명시 + C-5b Deferred 보존 명확.

---

## 7. MVP-1 PASS *재선언 없이* §C-5c + §C-6 만 갱신 가능 여부 (검토 영역 #7) ⭐

### 7.1 A-1 패턴 답습 (`1dd1036` + `6fa87dc` 답습)

`1dd1036` 합의 보고서 본문 답습:

> "**A-1 보수적 반영 답습**: Layer D 합의 보고서 (`docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md`) **본문 변경 0건** (역사적 기록 보존) + 본 합의 보고서가 §C-1 갱신 권위 source."

`6fa87dc` 합의 보고서 본문 답습:

> "본 합의 = §C-5a *상태 표기* 갱신 한정 — Layer D 합의 보고서 본문 변경 0건 + C-2~C-5b/C-5c/C-6~C-8 자동 변경 0건 + Layer E/F 미진입 + ADR-012 영향 0건 + 다른 backlog 자동 진입 0건."

### 7.2 §C-5c + §C-6 갱신에 동일 A-1 패턴 적용 가능성

| 항목 | C-1 (K-2 fix) 갱신 | C-5a (ST-2) 갱신 | **C-5c + C-6 부분 갱신 (본 brief)** |
|------|------------------|---------------|------------------------------|
| 상태 변경 형태 | Deferred → Satisfied | Deferred → Satisfied | Deferred → Partially Satisfied (양쪽) |
| Layer D 본문 변경 | 0건 (A-1 답습) | 0건 (A-1 답습) | 0건 (A-1 답습 권고) |
| 합의 보고서 권위 source | `1dd1036` 자체 | `6fa87dc` 자체 | 본 brief 후속 합의 보고서 자체 |
| 영향 외 condition | C-2~C-8 모두 | C-1/C-2/C-3/C-4/C-5b/C-5c/C-6/C-7/C-8 모두 | C-1/C-2/C-3/C-4/C-5a/C-5b/C-7/C-8 모두 |
| **MVP-1 PASS *재선언*** | 0건 | 0건 | **0건 (Layer D 판정 = APPROVE WITH CONDITIONS 그대로 유지)** |
| **Operational Readiness PASS (Layer E)** | 0건 | 0건 | **0건 (MVP-6 + Backlog #7 별도 영역)** |
| **Hermes PMO 격상 (Layer F)** | 0건 | 0건 | **0건 (MVP-6 + 외부 LLM 의무)** |
| **T3 영역 자동 진입** | 0건 | 0건 | **0건 (Backlog #3 T3 영역 보존)** |
| 다른 backlog 자동 진입 | 0건 | 0건 | 0건 |
| ADR 본문 자동 갱신 | 0건 | 0건 | 0건 |
| evidence 형태 | K-2 fix 적용 (3 commit) | ST-2 Cycle 1~6 (8 commit) + actual run | Cycle 4 + fix + 메타 (3 commit) + local actual run 6/6 PASS |

### 7.3 §7 판정 ⭐

✅ **MVP-1 PASS *재선언 없이* §C-5c + §C-6 만 부분 갱신 가능** — A-1 패턴 답습 (`1dd1036` + `6fa87dc` 답습) + §C-5c·§C-6 상태 표기 한정 갱신 + Layer D 본문 변경 0건 + C-1/C-2/C-3/C-4/C-5a/C-5b/C-7/C-8 자동 변경 0건 + MVP-1 PASS *재선언* 0건 + Layer E·F 미진입 + T3 영역 자동 진입 0건.

### 7.4 §C-5 / §C-6 표기 갱신 후보 (Layer D 본문 외부 권위 source 한정)

본 brief 후속 합의 보고서가 §C-5 / §C-6 표기 갱신 권위 source — 후보 표기:

```
C-5 (GP-3 1.5차 보강 — Backlog #1) = Partially Satisfied (C-5a + C-5c partial)
  C-5a (ST-2 inotify sidecar)         = Satisfied (`6fa87dc`)
  C-5b (ST-1 entrypoint stat)         = Deferred (Backlog #3 T3 영역)
  C-5c (PC-4 local pre-commit)        = Partially Satisfied — T2 sub only (`<consensus-commit>`)
                                          T2 sub (.pre-commit-config.yaml + opt-in)  = Satisfied
                                          T3 sub (pre-commit install / dev 강제)      = Deferred (Backlog #3)

C-6 (GP-5 1.5차 보강 — Backlog #2) = Partially Satisfied — PC-4 T2 sub only (`<consensus-commit>`)
  PC-4 T2 sub (provider-import + provider-url-model + import-linter)  = Satisfied
  T-1 / T-3 / T-4 단독                                                  = Deferred (Backlog #2 별도)
  T-5 단독 강화 (도구 본문 / Tier-2/3 catalog 확장)                       = Deferred (Backlog #2 별도)
  PC-4 T3 sub / AR-3                                                    = Deferred (Backlog #3)
```

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거 검증 (검토 영역 #8)

### 8.1 합의 형태 권고

| 영역 | 권고 형태 | 사유 |
|------|----------|------|
| 본 brief 자체 (DRAFT) | 사용자 명시 승인 한정 | 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의** | A-1 패턴 답습 (`1dd1036` + `6fa87dc` chain) + §5.5 9 sub-수단 본문 채택 변경 0건 + 사용자 명시 4 금지 + 추가 답습 + Cycle 4 evidence 결정적 (외부 추론 의존성 0건) |

### 8.2 7/7 풀 3+1 승격 트리거 검증

| # | 트리거 | 본 brief 발화 |
|---|----|---------|
| 1 | 9 sub-수단 외 수단 *재결정* | ❌ 0건 (PC-3 본문 채택 답습 변경 0건 — 영역 *상태 갱신* 한정) |
| 2 | **T3 영역 자동 진입** | ❌ 0건 (사용자 명시 4 금지 #4 답습 + Backlog #3 보존 + `pre-commit install` 의무화 0건) |
| 3 | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | ❌ 0건 (Cycle 4 답습 한정) |
| 4 | Provider Liquidity 5-way 약화 | ❌ 0건 (`repo: local` + option (b)=ii pre-commit venv 격리 답습 + 외부 repo 의존 0건) |
| 5 | 5 영구 핵심 제약 약화 | ❌ 0건 (Hermes ≠ root of trust 보존 + 수단/목적 분리 보존 + 메타포 강제 금지 보존) |
| 6 | **MVP-1 PASS 재선언 / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상)** | ❌ 0건 (사용자 명시 4 금지 #1 + #2 + #3 답습) |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ❌ 0건 (T3 결정 0건 — 사용자 명시 4 금지 #4 답습) |

**합산 = 7/7 0건 발화** → **Reviewer-only 단축 합의 적격 확정**.

### 8.3 합의 보고서 진입 시 의무 영역

| 영역 | 의무 |
|------|------|
| 합의 보고서 경로 | `docs/review/3plus1-consensus-2026-05-14-c5c-c6-pc4-t2-satisfaction.md` (가칭, 사용자 명시 영역) |
| 갱신 영역 | §C-5c + §C-6 상태 표기 갱신 한정 (양쪽 Deferred → Partially Satisfied) — A-1 답습 |
| Layer D 본문 | 본문 변경 0건 (A-1 답습) — 본 합의 보고서가 §C-5c + §C-6 갱신 권위 source |
| §C-5 전체 표기 | `Partially Satisfied (C-5a + C-5c partial)` 갱신 권고 |
| C-1 / C-2 / C-3 / C-4 / C-5a / C-5b / C-7 / C-8 | 자동 변경 0건 |
| MVP-1 PASS *재선언* | 0건 |
| Operational Readiness PASS (Layer E) | 0건 |
| Hermes PMO 격상 (Layer F) | 0건 |
| T3 영역 자동 진입 (Backlog #3) | 0건 |
| 외부 LLM cross-vendor blind 의뢰 | 0건 (7/7 트리거 발화 0건 답습) |

---

## 9. 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 검토 범위 답습 (`.pre-commit-config.yaml` 6 hook local validation 근거 + C-5c·C-6 Satisfied/Partially Satisfied 갱신 검토) | ✅ §1~§7 |
| 사용자 명시 4 금지 답습 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) | ✅ §0.3 + §7.2 + §8.2 + 부록 B |
| Cycle 4 + fix + 메타 chain 완료 확인 | ✅ §1 |
| local `pre-commit run --all-files` actual run evidence 충분성 | ✅ §2 (11/11 + warm 0.482초 < 30초) |
| ADR-011 §2.1 (a)~(d) 4/4 충족 | ✅ §3 |
| §C-5c = `Partially Satisfied (T2 sub only)` 권고 적격 | ✅ §4 |
| §C-6 = `Partially Satisfied (PC-4 T2 sub only)` 권고 적격 | ✅ §5 |
| §C-5 전체 = `Partially Satisfied (C-5a + C-5c partial)` 권고 | ✅ §6 |
| MVP-1 PASS 재선언 없이 §C-5c + §C-6 만 부분 갱신 가능 (A-1 패턴 답습) | ✅ §7 |
| 7/7 풀 3+1 승격 트리거 0건 발화 → Reviewer-only 단축 적격 | ✅ §8.2 |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| Layer D 본문 변경 0건 (`210c98f` 그대로 유지) | ✅ (A-1 답습) |
| MVP-1 PASS *재선언* 0건 | ✅ |
| Operational Readiness PASS (Layer E) 선언 0건 | ✅ |
| Hermes PMO 격상 (Layer F) 0건 | ✅ |
| T3 영역 자동 진입 0건 (Backlog #3 보존) | ✅ |
| 다른 backlog (#3/#4/#7) 자동 진입 0건 | ✅ |
| ADR 본문 자동 갱신 0건 | ✅ |
| ADR-012 §2.2 enum 정식 등록 0건 (`pre_commit_config_local_definition_unified` candidate-only 유지) | ✅ |
| 도구 본문 / `.importlinter` config / `.pre-commit-config.yaml` 본문 변경 0건 | ✅ |
| CI workflow 변경 0건 | ✅ |
| Tier-2 / Tier-3 catalog 자동 확장 0건 | ✅ |
| 외부 LLM 자동 호출 0건 | ✅ |
| 합의 보고서 *작성* / commit / push 0건 (본 brief = 준비안) | ✅ |

---

## 10. 본 brief 요약 (한 단락)

본 brief 는 **PC-4 T2 sub Cycle 4 chain (`b2f99f4` Cycle 4 + `3d3cd21` fix + `5f878d6` 메타) + local `pre-commit run --all-files` actual run = 6/6 PASS (warm 0.482초, < 30초 충족) 결과를 *근거*로, §C-5c (PC-4 local pre-commit framework) + §C-6 (GP-5 1.5차 보강) 를 *부분 Satisfied* 갱신할 수 있는지 검토하는 *합의 준비안* (DRAFT)** 이다. 사용자 명시 검토 범위 답습 + 사용자 명시 4 금지 (MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입) 답습. 본 brief 8 영역 검토 결과: (§1) Cycle 4 + fix + 메타 chain = 완료 확정 / (§2) actual run evidence 충분 (11/11 + warm 0.482초) / (§3) ADR-011 §2.1 (a)~(d) 4/4 충족 / (§4) **§C-5c = `Partially Satisfied (T2 sub only)` 권고 적격** (T3 sub Backlog #3 보존) / (§5) **§C-6 = `Partially Satisfied (PC-4 T2 sub only)` 권고 적격** (T-1/T-3/T-4/T-5 단독 + AR-3 보존) / (§6) §C-5 전체 = `Partially Satisfied (C-5a + C-5c partial)` 권고 / (§7) MVP-1 PASS *재선언 없이* §C-5c + §C-6 만 부분 갱신 가능 — A-1 패턴 답습 (`1dd1036` + `6fa87dc` chain) / (§8) **7/7 풀 3+1 승격 트리거 0건 발화 → Reviewer-only 단축 합의 적격**. 단일 합의 보고서 권고 (양 GP 동시 부분 갱신). **본 brief ≠ §C-5c·§C-6 Satisfied 갱신 발효** — 합의 보고서 권위 갖지 않음 + Layer D 본문 변경 0건 + C-1/C-2/C-3/C-4/C-5a/C-5b/C-7/C-8 자동 변경 0건 + MVP-1 PASS *재선언* 0건 + Operational Readiness PASS (Layer E) 선언 0건 + Hermes PMO 격상 (Layer F) 0건 + T3 영역 자동 진입 0건 + 다른 backlog (#3/#4/#7) 자동 진입 0건 + ADR 본문 자동 갱신 0건 + ADR-012 §2.2 enum 정식 등록 0건 + 도구 본문 / `.importlinter` config / `.pre-commit-config.yaml` 변경 0건 + CI workflow 변경 0건 + Tier-2/3 catalog 자동 확장 0건 + 외부 LLM 자동 호출 0건. 다음 단계 = 사용자 결정 영역 (부록 A 옵션 A~D).

---

## 부록 A. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성** (`docs/review/3plus1-consensus-2026-05-14-c5c-c6-pc4-t2-satisfaction.md` 가칭) → §C-5c + §C-6 부분 Satisfied 갱신 (Layer D 본문 변경 0건, A-1 답습) → 메타 commit → push | 3-commit chain (brief 파일화 + 합의 + 메타) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 그대로 승인 → 합의 보고서 작성 → 메타 + push 보류 | 2 commit 한정 |
| (D) | 본 brief 그대로 승인 → 파일화 + commit *까지만* | 1 commit 한정 |
| (E) | 본 brief 보류 → 다른 backlog 우선 (Backlog #2 GP-5 1.5차 / Backlog #3 T3 / MVP-2) | 별도 진입 |
| (F) | 본 brief 보류 → 세션 종료 | — |

### A.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 시작 명령 후보: "옵션 (A) 로 진행해주세요. 본 brief 그대로 승인하고, `docs/review/3plus1-consensus-2026-05-14-c5c-c6-pc4-t2-satisfaction.md` 작성 → 메타 + push 까지 3-commit chain 으로 진행."

---

## 부록 B. 금지 사항 (사용자 명시 4 금지 + 추가 답습)

### B.1 사용자 명시 4 금지 답습 (이번 진입 명령)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | **MVP-1 PASS *재선언*** | 0건 (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| 2 | **Operational Readiness PASS** (Layer E) 선언 | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 3 | **Hermes PMO 격상** (Layer F) | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| 4 | **T3 영역 자동 진입** | 0건 (`pre-commit install` 의무화 / dev 환경 강제 / branch protection / commit signing / required check / `default_install_hook_types` / `fail_fast` / commit-msg / pre-push stage 모두 0건 — Backlog #3 보존) |

### B.2 추가 금지 (본 brief 자체)

- ❌ §C-5c / §C-6 *Satisfied 자동 갱신* 0건 (본 brief = 준비안 — 합의 보고서 = 별도 단계)
- ❌ §C-5 전체 *Satisfied 자동 갱신* 0건 (C-5b ST-1 Deferred 보존 + C-5c T3 sub 보존)
- ❌ Layer D 합의 보고서 *본문 변경* 0건 (A-1 답습)
- ❌ C-1 / C-2 / C-3 / C-4 / C-5a / C-5b / C-7 / C-8 자동 변경 0건
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건 (양 GP PC-3 본문 채택 유지)
- ❌ ADR 본문 자동 갱신 0건
- ❌ ADR-012 §2.2 `event` enum 정식 등록 0건 (`pre_commit_config_local_definition_unified` candidate-only 유지)
- ❌ 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `tools/workflow_secrets_usage_check.py` / `tools/workflow_permissions_check.py`) 변경 0건
- ❌ `.importlinter` config 본문 변경 0건
- ❌ `.pre-commit-config.yaml` 본문 *변경* 0건 (본 brief = 검토 준비안, 본문 작성/수정 0건)
- ❌ CI workflow 본문 변경 0건 (PC-3 본문 채택 답습 그대로)
- ❌ 강제 commit blocking 정책 (`fail_fast` / `default_install_hook_types` / commit-msg / pre-push stage 추가) 0건
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건
- ❌ 다른 backlog (#3 / #4 / #7) 자동 진입 0건
- ❌ Cycle 5 도구 신설 0건 (사용자 결정 (가) 답습 — 기존 Stage 5 `.py` reuse)
- ❌ Production `docker-compose.yml` 변경 0건
- ❌ Hermes upstream Dockerfile 변경 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화 0건
- ❌ 합의 보고서 *작성* 0건 (본 brief = 준비안 — 합의 보고서 = 별도 단계)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리)
- ❌ git commit / push 0건 (본 brief 파일화 + commit = 사용자 명시 후속)

---

**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**다음 단계**: 사용자 명시 결정 영역 (부록 A 옵션 A~F)
**주요 결정 필요 영역**:
- (a) **§C-5c 갱신 표기** = `Partially Satisfied (T2 sub only)` 적절성 확인
- (b) **§C-6 갱신 표기** = `Partially Satisfied (PC-4 T2 sub only)` 적절성 확인
- (c) **§C-5 전체 갱신 표기** = `Partially Satisfied (C-5a + C-5c partial)` 적절성 확인
- (d) **합의 보고서 경로** = `docs/review/3plus1-consensus-2026-05-14-c5c-c6-pc4-t2-satisfaction.md` (가칭) 또는 사용자 명시 영역
- (e) **합의 형태** = Reviewer-only 단축 합의 (7/7 트리거 0건 발화 답습) 확인
- (f) **단일 합의 보고서 vs 분리** = §C-5c + §C-6 단일 합의 권고 (구현 진입 brief §14.3 답습) 확인
