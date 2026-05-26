# PC-4 T2 sub 구현 진입 *준비안* Brief (DRAFT)

> **본 brief = §C-5c (PC-4 local pre-commit framework) 中 T2 sub-영역 (`.pre-commit-config.yaml` config 정의) 의 *Backlog #1 + #2 통합 실 구현* 직전 합의 준비안 (DRAFT)** — 진입 권한 발효 (`1efb75d` APPROVE) 위에서 Cycle 분할 + hook 구성 + evidence/rollback 기준 *사전 정비*. **사용자 결정 3개 확정 반영**: (a) Cycle 분할 = α (한 번에) / (b) `import-linter` `language` = ii (python + additional_dependencies) / (c) GP-3 도구 신설 = ii (`tools/workflow_*.sh` 신설, 단 CI workflow 변경 0건 답습 — local hook 보조 도구 한정).
>
> 본 brief 의 어떤 §도 그 자체로 (i) `.pre-commit-config.yaml` 실 본문 작성, (ii) hook 본문 작성, (iii) `pre-commit install` 의무화 / dev 환경 강제, (iv) branch protection / CI workflow 변경, (v) §C-5c / §C-6 Satisfied 자동 갱신, (vi) MVP-1 PASS 재선언 / Layer E·F 격상, (vii) T3 영역 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 3
**상태**: DRAFT (사용자 명시 승인 *전* — 옵션 (A) 4-commit chain 진입 답습 + 사용자 결정 3개 확정 반영)
**상위 권위**:
- 진입 권한 발효 합의 = `1efb75d docs(review): approve PC-4 T2 entry` (Reviewer-only 단축, APPROVE — 진입 권한 발효 한정)
- 진입 직전 brief = `611aab3` (DRAFT 19 섹션, 785 lines)
- 진입 권한 메타 = `476a70f` (CONTEXT/INDEX/SESSION §37)
- 통합 검토 합의 = `c292c9d` (APPROVE AS BRIEF) / 통합 brief = `e9614a6` / 선행 단독 brief = `11d7ebb`
- §C-5a 갱신 = `6fa87dc` (§C-5 = `Partially Satisfied (C-5a only)`)
- MVP-1 PASS (Layer D) = `210c98f` (APPROVE WITH CONDITIONS)
- §5.5 본문 채택 = `f40423f` + `55c5b4b` (양 GP PC-3 일관 채택)
- 도구 검증 답습: `tools/secret_scanner.py` (Group D `25623028888`) / `tools/provider_import_scanner.py` (Group A 1차) / `tools/provider_url_scanner.py` (Group A 3차 `25629390384`) / `lint-imports` + `.importlinter` (Group A 2차 `25605665191`)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 3)

> "(1) PC-4 T2 sub 구현 진입 brief를 작성해주세요. 목표: `.pre-commit-config.yaml`을 작성하기 전에, 구현 범위, hook 구성, cycle 분할, evidence 기준, rollback 기준을 정리한다."

> 13 검토 항목 + 10 금지 답습 + 텍스트 한정 산출 → 사용자 옵션 (A) + 결정 3개 (α/ii/ii) 확정 후 파일화 + commit + 합의 + 메타 + push 4-commit chain.

### 0.2 사용자 결정 3개 *확정* 반영 (2026-05-14 후속 3 진입 결정)

| # | 결정 영역 | 사용자 결정 | 사유 |
|---|---------|---------|------|
| (a) | **Cycle 분할 정책** | **α (6 hook 한 번에 통합 정의)** | PC-4 T2 sub = `.pre-commit-config.yaml` config 정의 영역 → GP-3 / GP-5 hook 1 config 구조 통합 적절 |
| (b) | **`import-linter` `language` 옵션** | **ii (`language: python` + `additional_dependencies`)** | pre-commit 환경 재현성 + system 환경 의존성 ↓ + `.importlinter` 본문 변경 0건 |
| (c) | **GP-3 도구 신설 옵션** | **ii (`tools/workflow_secret_usage_check.sh` + `tools/workflow_permissions_check.sh` 신설)** | 추적성 / 재사용성 / evidence 생성 유리 — **단 CI workflow 변경 0건** (CI = inline grep 유지, 본 도구 = local hook 보조 한정) |

### 0.3 본 brief 가 *하는* 것

1. `.pre-commit-config.yaml` 작성 *범위* 정비 (§2)
2. `repo: local` hooks 구조 (Cycle 시점 기준) 정비 (§3)
3. GP-3 3 hook 후보 *Cycle 시점* 정비 + GP-3 도구 신설 (option (c)=ii 답습) (§4)
4. GP-5 3 hook 후보 *Cycle 시점* 정비 + `import-linter` language ii 답습 (§5)
5. Cycle 분할 정책 = α 답습 (§6)
6. `import-linter` `language` 옵션 = ii 답습 (§7)
7. runtime 합산 < 30초 *검증 방식* (§8)
8. local pre-commit = opt-in 보조 장치 명시 (§9)
9. CI single source-of-truth 유지 방식 (§10)
10. T3 영역과의 경계 (§11)
11. Evidence / artifact 기준 (§12)
12. Rollback Trigger (§13)
13. §C-5c / §C-6 갱신 조건 (§14)
14. 합의 형태 권고 + 7/7 트리거 검증 (§15)
15. 금지 사항 (§16)
16. 다음 단계 결정 옵션 (§17)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 10 금지 답습)

- ❌ **`.pre-commit-config.yaml` 실 본문 작성 0건**
- ❌ **hook 본문 작성 0건** (실 hook 본문 / actual run / 통합 시연)
- ❌ **`pre-commit install` 의무화 0건** (T3 영역)
- ❌ **dev 환경 강제 0건** (T3 영역)
- ❌ **branch protection 변경 0건** (Backlog #3 T3)
- ❌ **CI workflow 변경 0건** (PC-3 본문 채택 답습 변경 0건 + 옵션 (c)=ii 답습 시 CI step inline grep 유지)
- ❌ **§C-5c / §C-6 Satisfied 자동 갱신 0건**
- ❌ **MVP-1 PASS *재선언* 0건** (Layer D `210c98f` 그대로 유지)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**

### 0.5 본 brief 가 *하지 않는* 것 (추가 답습)

- ❌ T3 영역 자동 진입 0건
- ❌ 강제 commit blocking 정책 0건 (`fail_fast: true` / `default_install_hook_types` / `commit-msg` 추가 stage 모두 0건)
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건
- ❌ Backlog #1 / #2 외 영역 진입 합의 발효 0건
- ❌ PC-4 *수단 결정* 변경 0건
- ❌ threshold *고정* 0건
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건
- ❌ ADR 본문 자동 갱신 0건
- ❌ ADR-012 §2.2 enum 정식 등록 0건 (`pre_commit_config_local_definition_unified` candidate-only 유지)
- ❌ 도구 본문 변경 0건 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `.importlinter` 모두 변경 0건)
- ❌ 다른 backlog (#3/#4/#7) 자동 진입 0건
- ❌ C-2 / C-3 / C-4 / C-5a / C-5b / C-7 / C-8 자동 변경 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건

### 0.6 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 어떤 §도 (i) 실 구현 합의 *발효*, (ii) `.pre-commit-config.yaml` 본문 작성, (iii) hook 본문 작성, (iv) §C-5c·§C-6 Satisfied 갱신, (v) MVP-1 PASS 재선언 / Layer E·F 격상, (vi) T3 sub 진입을 발생시키지 않는다.

본 brief 가 발생시키는 *유일한* 효과 = **실 구현 합의 *직전* 의사결정 입력 정비 — Cycle 분할 = α / `import-linter` `language` = ii / GP-3 도구 신설 = ii 확정 + Cycle 시점 hook 정비 + Evidence/Rollback 기준 + §C-5c·§C-6 갱신 조건**.

---

## 1. 진입 컨텍스트 답습 (`1efb75d` APPROVE 후 상태)

### 1.1 chain 답습

```
선행 단독 brief (11d7ebb) → 통합 brief (e9614a6) → 통합 검토 합의 (c292c9d, APPROVE AS BRIEF)
   → 통합 검토 메타 (520ae0f)
   → 진입 직전 brief (611aab3) → 진입 권한 합의 (1efb75d, APPROVE — 진입 권한 발효)
   → 진입 권한 메타 (476a70f)
   ↓
■ 본 brief = PC-4 T2 sub 구현 진입 준비안 (DRAFT, 사용자 결정 α/ii/ii 확정)         ← 현 위치
   ↓ (사용자 명시 옵션 (A))
brief 파일화 → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push
   ↓ (구현 진입 합의 발효 후)
Cycle (사용자 결정 α 답습 = 1 Cycle 통합) — `.pre-commit-config.yaml` 작성 + GP-3 2 도구 신설
   ↓ (Cycle 완료 + actual run SUCCESS + evidence 후)
§C-5c / §C-6 부분 Satisfied 갱신 합의 (단일 합의 권고)
```

### 1.2 §C-5 / §C-6 상태 답습 (`476a70f` 후 시점, 변경 0건)

| Condition | 항목 | 상태 |
|-----------|------|------|
| C-5a | ST-2 (inotify sidecar) | ✅ Satisfied (`6fa87dc`) |
| C-5b | ST-1 | ⏳ Deferred (Backlog #3 T3) |
| **C-5c** | **PC-4** | ⏳ **Deferred** (진입 권한 발효 ≠ Satisfied 갱신) |
| C-5 전체 | — | ⏳ Partially Satisfied (C-5a only) |
| **C-6** | **GP-5 1.5차** | ⏳ **Deferred** |

### 1.3 진입 권한 합의 (`1efb75d`) 결과 답습

| 영역 | 결과 |
|------|------|
| 판정 | APPROVE — T2 sub 한정 진입 권한 발효 |
| 13/13 검토 항목 | 적절 |
| 12/12 금지 | 0건 위반 |
| 7/7 풀 3+1 트리거 | 0건 발화 |
| Rollback Trigger 활성화 | 9개 |
| `import-linter` `language` Cycle 1 결정 | 명시 |

→ **본 brief = 구현 진입 적격 토대 + 사용자 결정 3개 확정 영역 명시**.

---

## 2. `.pre-commit-config.yaml` 작성 *범위* 정비 (검토 항목 #1)

### 2.1 작성 범위 안 (Cycle 작성 대상, α 답습)

| 영역 | Cycle 작성 (α 1 Cycle 통합) |
|------|----------|
| 파일 위치 | `/.pre-commit-config.yaml` (repo root) |
| 파일 형식 | yaml — pre-commit framework 표준 |
| `repos` 배열 1 entry (`repo: local`) | ✅ |
| 6 hook entry 본문 (α 답습 — 한 번에 통합 정의) | ✅ |
| 각 hook 의 id / name / entry / language / files / stages / pass_filenames / always_run | ✅ |
| `import-linter` hook 의 `language: python` + `additional_dependencies: [import-linter==X.Y.Z]` (옵션 ii 답습) | ✅ |
| schema 자체 검증 (yaml syntax + pre-commit framework spec 준수) | ✅ (Cycle 자체 검증 의무) |

### 2.2 작성 범위 외

| 영역 | 사유 |
|------|------|
| `pre-commit install` 자동 실행 / 의무 표기 | 사용자 명시 10 금지 #3 |
| `default_install_hook_types` 변경 | T3 간접 강제 |
| `commit-msg` / `pre-push` / `post-commit` stage hook | branch protection 회피 답습 |
| 외부 repo (`repo: https://...`) hook | Provider Liquidity 5-way 답습 |
| `fail_fast: true` (전체 강제) | 강제 효과 0건 답습 |
| `minimum_pre_commit_version` 강제 | dev 환경 강제 답습 |
| README 강제 install 표기 | R-MVP1-G3-PC4-T2-INTG-1 답습 |
| dev install 비율 측정 hook | T3 간접 강제 |

### 2.3 작성 *부수* 영역 (Cycle 시점 결정 영역)

| 영역 | Cycle 작성 |
|------|--------|
| `.gitignore` 에 `.pre-commit-config.yaml` 추가 여부 | ❌ — 본문 commit 의도 답습 (gitignore 미포함) |
| `requirements-dev.txt` 에 `pre-commit` 추가 여부 | Cycle 결정 영역 — opt-in 일관 답습 시 추가 가능 |
| `requirements-dev.txt` 에 `import-linter` 추가 여부 | 옵션 ii 답습 시 — `additional_dependencies` 가 venv 자동 install 보장 → 별도 추가 불필요. 단 dev 환경 직접 사용 시 참고용 추가 가능 (강제 의무 0건) |
| README *참고용* opt-in 사용법 표기 (강제 의무 0건) | Cycle 결정 영역 — 강제 표기 0건 + 단순 *참고 정보* 한정 적격 |

---

## 3. `repo: local` hooks 구조 (Cycle 시점 기준) 정비 (검토 항목 #2)

### 3.1 1 entry 구조 답습 (α 1 Cycle 통합)

```
# 본 brief = 형식 enumerate 한정 + Cycle 작성 0건
repos:
  - repo: local
    hooks:
      - id: secret-scanner                      # GP-3
      - id: workflow-secret-usage-check         # GP-3 (도구 신설 답습 — 옵션 (c) ii)
      - id: workflow-permissions-check          # GP-3 (도구 신설 답습 — 옵션 (c) ii)
      - id: provider-import-scanner             # GP-5
      - id: provider-url-model-scanner          # GP-5
      - id: import-linter                       # GP-5 (language: python + additional_dependencies — 옵션 (b) ii)
```

### 3.2 단일 entry 권고 사유 (재답습)

| 사유 | 답습 |
|------|------|
| 외부 repo 의존성 0건 | Provider Liquidity 5-way 답습 |
| 단일 source-of-truth | yaml 본문 중복 회피 |
| Hermes ≠ root of trust | ADR-011 답습 |
| pre-commit framework 자동 update 위험 0건 | 외부 repo 미사용 답습 |

### 3.3 Cycle 작성 시점 yaml 본문 *유효성* 의무

| Cycle | yaml 본문 유효성 |
|-------|-----------|
| Cycle 1 (α 통합) | yaml syntax PASS + pre-commit framework spec 준수 + hook id 중복 0건 + `repo: local` 한정 + `[pre-commit]` stage 한정 + 5 hook = `language: system` + 1 hook = `language: python` + `additional_dependencies` (옵션 (b) ii 답습) |

---

## 4. GP-3 hook 후보 *Cycle 시점* 정비 + GP-3 도구 신설 (옵션 (c) ii 답습)

### 4.1 hook #1 — `secret-scanner` (Cycle 시점 정비)

| 항목 | Cycle 시점 정비 |
|------|----------|
| Cycle 작성 시점 | Cycle 1 (α 통합) |
| hook id | `secret-scanner` |
| name | "Secret Scanner (R-4.1 Tier-1 45 patterns)" |
| 도구 entry | `python tools/secret_scanner.py` |
| 도구 본문 변경 | ❌ 0건 (Layer B `55c5b4b` S-1 본문 채택 답습) |
| files 패턴 | `\.(py|js|ts|md|yml|yaml|sh|toml|env\.example)$` (Cycle 작성 시점 R-4.1 ↔ files 패턴 일관성 검증 의무) |
| stages | `[pre-commit]` |
| language | `system` |
| pass_filenames | true |
| always_run | false |
| pass / fail 기준 | 도구 본문 답습 (exit 0 / ≠ 0) |
| Cycle 자체 검증 | hook id 중복 0건 + entry 명령 = CI step 동등 + files 패턴 일관성 |
| 본문 채택 권위 | ✅ S-1 (`55c5b4b` §5.5.1) |

### 4.2 hook #2 — `workflow-secret-usage-check` (Cycle 시점 정비, 옵션 (c) ii 답습)

| 항목 | Cycle 시점 정비 |
|------|----------|
| Cycle 작성 시점 | Cycle 1 (α 통합) |
| hook id | `workflow-secret-usage-check` |
| 도구 entry | `bash tools/workflow_secret_usage_check.sh` |
| **도구 신설 (Cycle 1 작성 영역)** | ✅ **`tools/workflow_secret_usage_check.sh` 신설** (옵션 (c) ii 답습 — 추적성/재사용성/evidence 생성 유리) |
| 도구 본문 (Cycle 1 신설 시) | grep wrapper — G3-7 (i) GitHub Actions secrets 사용 0건 + (ii) `secrets.*` 참조 감지 답습. 본 brief = 본문 작성 0건 (Cycle 1 단계). |
| 필요 secret FP 패턴 (예: `GITHUB_TOKEN`) | Cycle 1 작성 시점 정비 의무 (도구 본문 grep exclusion 패턴) |
| files 패턴 | `^\.github/workflows/.*\.(yml|yaml)$` |
| stages | `[pre-commit]` |
| language | `system` |
| pass_filenames | true |
| always_run | false |
| pass / fail 기준 | `secrets\.[A-Z_]+` 참조 0건 (필요 secret 예외 답습) + GitHub Actions secrets 사용 0건 |
| **CI workflow 변경 (옵션 (c) ii 답습)** | ❌ **0건** (CI step = 기존 inline grep 유지 — 사용자 명시 답습 "CI single source-of-truth는 기존 inline grep / 기존 workflow 구조를 유지하고, 이번 PC-4 T2 sub 의 local hook 보조 도구로만 둡니다") |
| Cycle 자체 검증 | 도구 신설 본문 grep pattern = CI step inline grep pattern 동등 검증 (단일 source-of-truth 보존 의무) |
| 본문 채택 권위 | ✅ G3-7 (i) + (ii) (`55c5b4b` §5.5.1 추가) |

### 4.3 hook #3 — `workflow-permissions-check` (Cycle 시점 정비, 옵션 (c) ii 답습)

| 항목 | Cycle 시점 정비 |
|------|----------|
| Cycle 작성 시점 | Cycle 1 (α 통합) |
| hook id | `workflow-permissions-check` |
| 도구 entry | `bash tools/workflow_permissions_check.sh` |
| **도구 신설 (Cycle 1 작성 영역)** | ✅ **`tools/workflow_permissions_check.sh` 신설** (옵션 (c) ii 답습) |
| 도구 본문 (Cycle 1 신설 시) | grep wrapper — G3-7 (v) workflow `permissions: contents: read` 명시 강제 (R-6 답습). 본 brief = 본문 작성 0건. |
| files 패턴 | `^\.github/workflows/.*\.(yml|yaml)$` |
| stages | `[pre-commit]` |
| language | `system` |
| pass / fail 기준 | 모든 workflow `permissions:` 명시 + `contents: read` 답습 |
| **CI workflow 변경** | ❌ 0건 (CI step = 기존 inline grep 유지 — 옵션 (c) ii 답습) |
| Cycle 자체 검증 | 도구 신설 본문 grep pattern = CI step inline grep pattern 동등 검증 + 예외 영역 (`contents: write` 정당 사용 시) 별도 합의 의무 |
| 본문 채택 권위 | ✅ G3-7 (v) R-6 (`55c5b4b` §5.5.1 추가) |

### 4.4 GP-3 3 hook 합산 작성 영역 (Cycle 1 α 통합)

| 영역 | Cycle 1 작성 |
|------|----------|
| `.pre-commit-config.yaml` GP-3 hook entry 3 신설 | ✅ |
| **도구 신설 2개 (옵션 (c) ii 답습)** | ✅ `tools/workflow_secret_usage_check.sh` + `tools/workflow_permissions_check.sh` |
| 기존 도구 본문 변경 | ❌ 0건 (`tools/secret_scanner.py` 답습) |
| **CI workflow 변경 (옵션 (c) ii 답습)** | ❌ **0건** (사용자 명시 답습 — local hook 보조 도구 한정) |

### 4.5 옵션 (c) ii 답습 부수 영역 — 단일 source-of-truth 정합성

| 영역 | 답습 |
|------|------|
| CI step (기존 inline grep 유지) ↔ local hook 신설 도구 본문 grep pattern | ⚠️ 부분 위반 인지 명시 — grep pattern 변경 시 양쪽 변경 의무 (CI inline grep + 도구 본문 grep) |
| 변경 ledger 추적성 | ✅ — 도구 신설 = pattern 1 곳 명시 (CI inline 추가 변경 시 git diff 통합 추적 가능) |
| 사용자 명시 "evidence 생성 유리" 답습 | ✅ — 도구 path 통한 evidence 산출 (도구 자체 actual run log + exit code 명확) |
| R-MVP1-G3-PC4-T2-INTG-2 trigger 해석 | hook entry ↔ CI step 본질 동등 (도구 본문 grep pattern = CI inline grep pattern) — 부분 위반 ≠ 동등 명령 위반 |

---

## 5. GP-5 hook 후보 *Cycle 시점* 정비 + `import-linter` `language` ii 답습

### 5.1 hook #4 — `provider-import-scanner` (Cycle 시점 정비)

| 항목 | Cycle 시점 정비 |
|------|----------|
| Cycle 작성 시점 | Cycle 1 (α 통합) |
| hook id | `provider-import-scanner` |
| 도구 entry | `python tools/provider_import_scanner.py` |
| 도구 본문 변경 | ❌ 0건 (Group A 1차 답습 + T-5 부분 본문 채택 답습) |
| files 패턴 | `^src/.*\.py$` |
| stages | `[pre-commit]` |
| language | `system` |
| pass / fail 기준 | 도구 본문 답습 (5/5 pattern 매칭 0건) |
| Cycle 자체 검증 | hook entry = CI step 동등 + src/ 0건 환경 hook 동작 0건 (FP/FN 측정 별도 단계) |
| 본문 채택 권위 | ✅ T-6 中 T-5 부분 (`55c5b4b` §5.5.2) |

### 5.2 hook #5 — `provider-url-model-scanner` (Cycle 시점 정비)

| 항목 | Cycle 시점 정비 |
|------|----------|
| Cycle 작성 시점 | Cycle 1 (α 통합) |
| hook id | `provider-url-model-scanner` |
| 도구 entry | `python tools/provider_url_scanner.py` |
| 도구 본문 변경 | ❌ 0건 (Group A 3차 답습) |
| files 패턴 | `^src/.*\.py$` |
| stages | `[pre-commit]` |
| language | `system` |
| pass / fail 기준 | 도구 본문 답습 (URL Tier-1 + Model Tier-1 매칭 0건) |
| Cycle 자체 검증 | hook entry = CI step 동등 |
| 본문 채택 권위 | ✅ T-6 中 T-5 부분 (`55c5b4b` §5.5.2) |

### 5.3 hook #6 — `import-linter` (Cycle 시점 정비, 옵션 (b) ii 답습)

| 항목 | Cycle 시점 정비 |
|------|----------|
| Cycle 작성 시점 | Cycle 1 (α 통합) |
| hook id | `import-linter` |
| 도구 entry | `lint-imports` |
| 도구 본문 변경 | ❌ 0건 (T-2 답습) |
| **`.importlinter` config 본문 변경** | ❌ **0건** (사용자 명시 답습 — "기존 .importlinter 본문은 변경하지 않습니다" + Group A 2차 답습) |
| files 패턴 | (생략 — `pass_filenames: false` + `always_run: true` 권고) |
| stages | `[pre-commit]` |
| pass_filenames | false |
| always_run | true |
| **`language` 옵션 (사용자 결정 (b) ii 답습)** | **`language: python`** |
| **`additional_dependencies` (옵션 (b) ii 답습)** | **`additional_dependencies: [import-linter==<Group A 2차 actual run 답습 버전>]`** (Cycle 1 작성 시점 버전 pin 결정 의무) |
| pass / fail 기준 | 도구 본문 답습 (모든 contract PASS) |
| Cycle 자체 검증 | `language: python` + `additional_dependencies` 본문 정의 + pre-commit framework venv 자동 install 동작 검증 (격리 환경) |
| 본문 채택 권위 | ✅ T-6 中 T-2 부분 (`55c5b4b` §5.5.2) |

### 5.4 옵션 (b) ii 답습 부수 영역

| 영역 | 답습 |
|------|------|
| pre-commit framework venv 격리 (dev 환경 venv 영향 0건) | ✅ |
| `requirements-dev.txt` 에 `import-linter` 추가 여부 | 옵션 — 추가 시 dev 환경 직접 `lint-imports` 사용 가능 (참고용, 강제 0건). 미추가 시 hook 자체 venv 한정 사용 (가장 격리). 권고 = 미추가 (가장 명확한 opt-in 답습) |
| pre-commit framework 자체의 `requirements-dev.txt` 추가 | 권고 (단, opt-in 한정 — 강제 의무 0건) |
| 사용자 명시 "재현성 / system 환경 의존성 ↓" 답습 | ✅ — venv 자동 install + 버전 pin |

### 5.5 GP-5 3 hook 합산 작성 영역 (Cycle 1 α 통합)

| 영역 | Cycle 1 작성 |
|------|----------|
| `.pre-commit-config.yaml` GP-5 hook entry 3 신설 | ✅ |
| 도구 본문 변경 | ❌ 0건 (3 도구 모두 답습) |
| `.importlinter` config 변경 | ❌ 0건 (사용자 명시 답습 + Group A 2차 답습) |
| `import-linter` `additional_dependencies` 버전 pin 결정 | Cycle 1 작성 시점 결정 (Group A 2차 actual run 답습 버전) |

---

## 6. Cycle 분할 정책 = α 답습 (검토 항목 #5) ⭐ 사용자 결정 확정

### 6.1 사용자 결정 (a) α 답습

> "α — 6개 hook 을 한 번에 통합 정의. 이유: PC-4 T2 sub 는 `.pre-commit-config.yaml` config 정의 영역이므로, GP-3 / GP-5 hook 을 하나의 config 구조로 통합해서 보는 것이 적절합니다."

**확정**: **α (1 Cycle 통합)** — 6 hook 모두 `.pre-commit-config.yaml` 1 회 작성에 통합 정의.

### 6.2 사용자 명시 commit 분리 정책 답습

사용자 명시 답습:

> "단, 실제 구현 단계에서는 commit 을 다음처럼 나눠도 됩니다.
> 1. brief 파일화
> 2. 합의 보고서
> 3. `.pre-commit-config.yaml` 작성
> 4. GP-3 보조 도구 신설
> 5. 메타 갱신"

**확정 commit 분리 (Cycle 영역)**:

| commit # | 영역 | 본 brief 영역 | Cycle 영역 |
|---------|------|---------|---------|
| 1 | brief 파일화 (`docs(phase0): add PC-4 T2 implementation brief`) | ✅ 본 단계 | — |
| 2 | 합의 보고서 (`docs(review): approve PC-4 T2 implementation entry`) | ✅ 본 단계 | — |
| 3 (Cycle 후) | 메타 갱신 (`docs(context): record PC-4 T2 implementation entry status`) | ✅ 본 단계 | — |
| (Cycle 4) | `.pre-commit-config.yaml` 작성 (`feat(g2-gp3-gp5): add .pre-commit-config.yaml ...`) | ❌ Cycle 영역 외 (사용자 명시 후속 결정) | Cycle 4 |
| (Cycle 5) | GP-3 보조 도구 신설 (`feat(g2-gp3): add workflow-secret-usage-check + workflow-permissions-check tools`) | ❌ Cycle 영역 외 | Cycle 5 |
| (Cycle 6) | (Cycle 갱신 메타 — actual run + evidence 후) | ❌ Cycle 영역 외 | Cycle 6 |

본 brief = commit 1~3 한정. commit 4~6 = Cycle 진입 후 별도 commit 단계 (사용자 명시 후속 결정 영역).

### 6.3 Cycle 4~5 분리 시 정합성 (α 본질 답습)

α = "6 hook 한 번에 통합 정의" = `.pre-commit-config.yaml` 1 파일에 6 hook 동시 정의. commit 4 (`.pre-commit-config.yaml` 작성) + commit 5 (GP-3 도구 신설) 분리 = α 답습 (단일 config) + 변경 ledger *세분화* 답습. 정합성 적격:

- commit 4 = `.pre-commit-config.yaml` 본문 6 hook 모두 정의 (config 1 회 변경)
- commit 5 = GP-3 도구 2개 신설 (config 변경 0건 — entry 명령은 commit 4 시점에서 이미 도구 path 명시)
- 단, commit 4 직후 hook actual run 시 GP-3 2 hook = 도구 미존재로 fail → commit 5 직후 actual run 정상 동작
- → commit 4 + 5 = 1 PR 통합 권고 (변경 ledger 분리 + 동시 actual run 검증)

### 6.4 Cycle 4 작성 후 self-audit 의무

| 검증 | 의무 |
|------|------|
| yaml syntax PASS | ✅ |
| pre-commit framework spec 준수 | ✅ |
| hook id 중복 0건 | ✅ |
| `repo: local` 한정 | ✅ |
| `[pre-commit]` stage 한정 | ✅ |
| `default_install_hook_types` / `fail_fast` / `minimum_pre_commit_version` 0건 (§9.2 답습) | ✅ |
| `import-linter` `language: python` + `additional_dependencies` 정의 (옵션 (b) ii) | ✅ |
| GP-3 hook entry = `bash tools/workflow_*.sh` (commit 5 도구 신설 답습) | ✅ |

---

## 7. `import-linter` `language` 옵션 = ii 답습 (검토 항목 #6) ⭐ 사용자 결정 확정

### 7.1 사용자 결정 (b) ii 답습

> "ii — `python` + `additional_dependencies`. 이유: pre-commit 환경에서 `import-linter` 실행 재현성이 좋고, system 환경 의존성을 줄일 수 있습니다. 단, 기존 `.importlinter` 본문은 변경하지 않습니다."

**확정**: **`language: python`** + **`additional_dependencies: [import-linter==<버전>]`** + **`.importlinter` 본문 변경 0건**.

### 7.2 옵션 ii 답습 형식

```
# 본 brief = 형식 enumerate 한정 + Cycle 작성 0건
- id: import-linter
  name: "Import Linter (T-2 contract TR-1~TR-5)"
  entry: lint-imports
  language: python
  additional_dependencies:
    - import-linter==<Group A 2차 actual run 답습 버전>
  pass_filenames: false
  always_run: true
  stages: [pre-commit]
```

### 7.3 옵션 ii 답습 보존 의무

| 영역 | 보존 의무 |
|------|---------|
| `.importlinter` config 본문 변경 0건 | ✅ (사용자 명시 + Group A 2차 답습) |
| pre-commit framework venv 격리 (dev 환경 venv 영향 0건) | ✅ |
| 버전 pin (Group A 2차 답습 버전) | ✅ Cycle 4 작성 시점 결정 |
| 강제 install 의무 0건 (opt-in 한정) | ✅ |

---

## 8. runtime 합산 < 30초 *검증 방식* (검토 항목 #7)

### 8.1 검증 *방식* 매트릭스

| 검증 시점 | 검증 방식 | 측정 형태 |
|--------|--------|--------|
| **Cycle 4~5 작성 직후** | local repo `pre-commit run --all-files` time 측정 | wall clock (`time pre-commit run --all-files`) |
| **opt-in dev 환경 측정 (자발적)** | 개발자가 `pre-commit run --all-files` 직접 실행 | 사용자 자발적 측정 |
| **CI workflow 추가 (별도 합의 영역)** | (CI workflow 변경 0건 답습 — 본 brief 영역 외) | (영역 외) |

### 8.2 본 brief 권고 (검증 방식)

- **권고 = Cycle 4~5 작성 직후 *local 측정* 한정** — 사유:
  - CI workflow 변경 0건 답습 (사용자 명시 10 금지 #6)
  - `pre-commit run --all-files` = local 격리 환경 + wall clock 측정
  - 측정 결과 = Evidence (Markdown report) 산출 영역

- **검증 결과 충족 기준**:
  - 병렬 합산 < 30초 (max hook = `import-linter` 한정)
  - 30초 초과 시 = R-MVP1-G3-PC4-T2-INTG-3 발화

### 8.3 검증 *결과 사용* 영역

| 결과 | 사용 |
|-----|-----|
| 30초 미만 | Evidence (a)~(d) 4/4 충족 → §C-5c·§C-6 부분 Satisfied 갱신 합의 진입 가능 |
| 30초 초과 ~ 60초 미만 | threshold 후보 재검토 합의 (단축 적격) |
| 60초 초과 (R-MVP1-G3-PC4-T2-INTG-3 발화) | hook 분리 / 도구 최적화 합의 |

### 8.4 옵션 (b) ii 답습 시 첫 실행 비용

옵션 (b) ii (pre-commit framework venv 자동 install) 답습 시 **첫 `pre-commit run --all-files` 실행** 은 venv 자동 install 비용 추가 (Group A 2차 답습 버전 + 의존성 download). 첫 실행 시 30초 초과 가능성 존재. 검증 의무:

- **첫 실행 (cold)** = venv 자동 install + hook 동작 — runtime 측정 영역 외 (warm-up 비용)
- **2회 차 실행 (warm)** = venv cache 답습 + hook 동작 — 본 brief §8.2 검증 대상 ⭐

---

## 9. local pre-commit = opt-in 보조 장치 명시 (검토 항목 #8)

### 9.1 opt-in 본질 답습 (진입 권한 brief §8 답습)

| 차원 | local pre-commit (T2 sub) |
|------|---------------------|
| 강제 여부 | ❌ opt-in 한정 |
| dev 환경 영향 | ❌ 0건 (강제 install 의무 0건) |
| Defense in depth | 보조 layer (CI 가 주 layer — PC-3 답습) |
| 검증 우회 가능성 | ✅ (`--no-verify` / 미설치) |

### 9.2 Cycle 4 작성 시 opt-in 보존 의무 5 영역

| 영역 | Cycle 4 작성 0건 의무 |
|------|----------------|
| (a) `default_install_hook_types` 명시 0건 | ✅ |
| (b) `fail_fast: true` 0건 | ✅ |
| (c) `minimum_pre_commit_version` 강제 0건 | ✅ |
| (d) README 강제 install 표기 0건 | ✅ |
| (e) `pre-commit install` 자동 실행 hook 0건 | ✅ |

### 9.3 opt-in 보존 검증 trigger 답습

| Trigger | 발화 조건 |
|---------|---------|
| R-MVP1-G3-PC4-T2-INTG-1 | dev 환경 *간접 강제* 시도 검출 (§9.2 (a)~(e) 1+ 위반) |

→ Cycle 4 작성 직후 self-audit 의무: §9.2 (a)~(e) 모두 0건 검증.

---

## 10. CI single source-of-truth 유지 방식 (검토 항목 #9)

### 10.1 동기화 보장 매트릭스 (옵션 (c) ii 답습 갱신)

| 도구 | CI step | local hook entry | 동기화 보장 |
|------|--------|-----------|----------|
| `tools/secret_scanner.py` | `secret-hygiene-egress-redaction.yml` | `python tools/secret_scanner.py` | ✅ 도구 본문 = 단일 source-of-truth |
| **`tools/workflow_secret_usage_check.sh` (Cycle 5 신설)** | **CI step inline grep (변경 0건 답습)** | `bash tools/workflow_secret_usage_check.sh` | ⚠️ **부분 위반 인지** — grep pattern 변경 시 양쪽 변경 의무 (CI inline + 도구 본문 grep) |
| **`tools/workflow_permissions_check.sh` (Cycle 5 신설)** | **CI step inline grep (변경 0건 답습)** | `bash tools/workflow_permissions_check.sh` | ⚠️ **동상** |
| `tools/provider_import_scanner.py` | `provider-adapter-enforcement.yml` | `python tools/provider_import_scanner.py` | ✅ |
| `tools/provider_url_scanner.py` | `provider-url-scanner.yml` | `python tools/provider_url_scanner.py` | ✅ |
| `lint-imports` + `.importlinter` | `provider-adapter-enforcement.yml` | `lint-imports` (옵션 ii venv) | ✅ config 본문 = 단일 source-of-truth |

### 10.2 옵션 (c) ii 답습 시 부분 위반 명시 (사용자 명시 결정 답습)

사용자 명시 답습:

> "단, CI workflow 는 변경하지 않습니다. CI single source-of-truth 는 기존 inline grep / 기존 workflow 구조를 유지하고, 이번 PC-4 T2 sub 의 local hook 보조 도구로만 둡니다."

**해석**:
- CI step inline grep (현재 본문 채택 답습) = 권위 source 유지 ⭐
- local hook 신설 도구 본문 grep pattern = CI inline grep pattern 답습 (도구 본문 = 추적성/재사용성/evidence 생성 보조 한정)
- grep pattern 변경 시 의무 = (a) CI inline grep 변경 (별도 합의) + (b) 도구 본문 변경 (Cycle N 별도 commit) 2개 동기화

### 10.3 CI workflow 변경 0건 답습

본 brief = CI workflow 본문 *변경 0건* 답습 (사용자 명시 10 금지 #6). 옵션 (c) ii 답습 시 부분 위반 인지 명시 + R-MVP1-G3-PC4-T2-INTG-2 trigger *재해석*:

| Trigger | 본 옵션 (c) ii 답습 시 발화 조건 |
|---------|------------------------|
| R-MVP1-G3-PC4-T2-INTG-2 | (i) 도구 본문 grep pattern ↔ CI inline grep pattern 명백 *불일치* (의도 변경 후 양쪽 동기화 누락) — *발화 조건* / (ii) 단순 표현 차이 (예: 공백 / 인용부호) — *발화 0건* |

→ Cycle 5 작성 직후 self-audit 의무: GP-3 2 도구 본문 grep pattern ↔ CI inline grep pattern 본질 동등 검증.

---

## 11. T3 영역과의 경계 (검토 항목 #10)

### 11.1 T2 / T3 경계 명확화 답습 (진입 권한 brief §11 답습)

```
T2 sub (본 brief 진입 영역, Cycle 4~5 작성 영역):
- .pre-commit-config.yaml config 정의 (Cycle 4)
- repo-local hook 정의 6개 (Cycle 4)
- opt-in local check (강제 효과 0건)
- 도구 신설 2개 (Cycle 5 — option (c) ii 답습)

T3 sub (본 brief 진입 영역 외, Cycle 4~5 작성 0건 의무):
- pre-commit install 의무화
- dev 환경 강제
- branch protection (AR-2 / AR-3 / commit signing / required check / CODEOWNERS)
- 강제 commit blocking 정책 (commit-msg / pre-push stage hook / fail_fast / default_install_hook_types)
- Hermes upstream Dockerfile 변경 통한 사전 install
- Vault HSM (ST-4)
- Tier-2 / Tier-3 catalog 자동 확장
```

### 11.2 Cycle 4~5 작성 시 T3 자동 진입 검출 self-audit

| Cycle 작성 영역 | T3 자동 진입 위험 검증 |
|--------------|--------------|
| Cycle 4 (`.pre-commit-config.yaml`) | §9.2 (a)~(e) 모두 0건 검증 |
| Cycle 5 (도구 신설 2) | 도구 본문 dev 환경 install 검증 추가 0건 / 도구 본문 강제 commit blocking 0건 |
| README 갱신 | 강제 install 표기 0건 |
| CI workflow 변경 (0건 답습) | 0건 |
| `requirements-dev.txt` 변경 | opt-in 한정 (강제 0건) — T2 영역 |

---

## 12. Evidence / artifact 기준 (검토 항목 #11)

### 12.1 ADR-011 §2.1 (a)~(e) 5조건 답습

| # | 조건 | Cycle 충족 형태 |
|---|------|-------------|
| (a) | 동등 이상의 보안 결과 | `.pre-commit-config.yaml` 본문 정의 = PC-3 (CI gating) 위 opt-in defense in depth 추가 (강제 효과 0건) |
| (b) | 격리 환경 PoC 실증 | local repo 격리 환경 `pre-commit run --all-files` 실행 + 6 hook 동작 시연 — Cycle 4~5 actual run log |
| (c) | ADR / SDD 권위 명시 | mvp1.md §4.3 + §5.5.1 / §5.5.2 + ADR-011 §2.4 + 선행 brief chain (`11d7ebb` + `e9614a6` + `c292c9d` + `611aab3` + `1efb75d` + 본 brief) 답습 |
| (d) | 자동 회귀 검증 경로 확보 | (i) `.pre-commit-config.yaml` schema 자체 검증 + (ii) opt-in 한정 동작 검증 + (iii) CI gating 답습 (PC-3 강제) |
| (e) | 합의 APPROVE | 본 brief 후속 합의 보고서 + Cycle 완료 후 §C-5c·§C-6 부분 Satisfied 갱신 합의 |

### 12.2 Evidence 산출물 후보 (Cycle 4~5 별도 단계)

| Evidence | 형식 | 산출 시점 | 본 brief 영역 |
|----------|------|--------|----------|
| Markdown report | `docs/phase0/g2-gp3-gp5-pc4-t2-evidence.md` (가칭) | Cycle 4~5 + actual run 후 | ❌ 영역 외 |
| JSONL ledger entry | `docs/evidence/ledger.jsonl` 신규 entry (`event: pre_commit_config_local_definition_unified` 가칭 = candidate-only) | Cycle 4~5 후 | ❌ 영역 외 |
| local actual run log | `pre-commit run --all-files` time + pass/fail log (warm 측정) | Cycle 4~5 자체 검증 | ❌ 영역 외 |
| 합의 보고서 (구현 진입) | `docs/review/3plus1-consensus-2026-05-13-pc4-t2-implementation-entry.md` | 본 brief 후속 단계 | ✅ 후속 영역 |
| §C-5c / §C-6 부분 Satisfied 합의 | `docs/review/3plus1-consensus-<date>-c5c-c6-pc4-t2-satisfaction.md` 가칭 | Cycle 4~5 + Evidence 후 | ❌ 영역 외 |

---

## 13. Rollback Trigger (검토 항목 #12)

### 13.1 본 구현 진입 후 활성화 Trigger (진입 권한 brief §12 답습 + 신규 보강 — 옵션 (b)/(c) ii 답습)

| Trigger ID | 발화 조건 | 발화 시 행동 | 우선순위 |
|----------|---------|-------------|------|
| R-MVP1-G3-4 | PC-3 부분 CI runtime 폭증 (>2분) | threshold 재결정 합의 | 高 |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | T3 영역 → 풀 3+1 합의 | 高 |
| R-MVP1-G5-6 | T-9 (PC-1) 도입 별도 합의 | 본 PoC 책무 분리 재합의 | 中 |
| **R-MVP1-G3-PC4-T2-INTG-1** | dev 환경 *간접 강제* 시도 검출 (§9.2 (a)~(e) 1+ 위반 / README 강제 / CI dev install 검증 등) | T3 영역 부분 진입 거부 + Cycle revert | **高** |
| **R-MVP1-G3-PC4-T2-INTG-2** | 도구 본문 grep pattern ↔ CI inline grep pattern *본질 불일치* 검출 (옵션 (c) ii 답습 부분 위반 명시 시 — 의도 변경 후 양쪽 동기화 누락) | 합의 재진입 + grep pattern 동기화 | **高** |
| **R-MVP1-G3-PC4-T2-INTG-3** | hook runtime 합산 폭증 (warm 측정 > 60초 후보) | hook 분리 / 도구 최적화 합의 | 中 |
| **R-MVP1-G3-PC4-T2-INTG-4** | FP_rate 폭증 (> 5건 / 1000 line 후보) | hook pattern 재검토 합의 | 中 |
| **R-MVP1-G3-PC4-T2-INTG-5** | FN 검출 (Tier-1 답습 패턴 의도 매칭 누락) | 도구 본문 재검토 (Tier-2/3 확장 = 별도 합의) | 中 |
| **R-MVP1-G3-PC4-T2-INTG-6** | 옵션 (b) ii (`language: python` + `additional_dependencies`) 답습 후 dev 환경 영향 中 검출 | 옵션 (b) i ↔ ii 전환 합의 | 中 |
| **R-MVP1-G3-PC4-T2-INTG-7** | Cycle 4 작성 후 yaml schema fail 검출 | Cycle 4 즉시 revert + 재작성 합의 | **高** |
| **R-MVP1-G3-PC4-T2-INTG-8** | `pre-commit run --all-files` actual run = fail 검출 (도구 본문 변경 0건 답습 위반 또는 entry 명령 오류 또는 venv install fail) | Cycle 즉시 revert + entry 재정비 합의 | **高** |
| **(신규) R-MVP1-G3-PC4-T2-INTG-9** | 옵션 (b) ii 답습 시 `additional_dependencies` 버전 ↔ Group A 2차 actual run 답습 버전 불일치 검출 | 버전 pin 재검토 합의 | 中 |
| **(신규) R-MVP1-G3-PC4-T2-INTG-10** | 옵션 (c) ii 답습 시 도구 본문 grep pattern ↔ CI inline grep pattern *단순 표현 차이* (의도 동등) 검출 | 발화 0건 (단순 표현 차이 = 발화 조건 외) | — |

### 13.2 Cycle 시점 trigger 발화 시 *즉시 행동* 매트릭스

| Cycle 시점 | trigger 발화 시 행동 |
|--------|----------------|
| Cycle 4 작성 직후 (yaml fail / hook fail / cold venv install fail) | 즉시 revert (commit revert) + 합의 재진입 |
| Cycle 5 작성 직후 (도구 신설 본문 grep pattern fail / hook fail) | 동상 |
| Cycle 4~5 actual run (warm 측정 runtime 폭증 / FP/FN 폭증) | hook 분리 / pattern 재검토 합의 (단축 적격) |

---

## 14. §C-5c / §C-6 갱신 조건 (검토 항목 #13)

### 14.1 §C-5c 갱신 조건 (Cycle 단계 명시)

| 조건 | 충족 단계 |
|------|-------|
| (i) PC-4 T2 sub 통합 진입 권한 발효 | ✅ 충족 (`1efb75d`) |
| (ii) PC-4 T2 sub 구현 진입 합의 발효 | ⏳ 본 brief 후속 합의 |
| (iii) Cycle 4 (`.pre-commit-config.yaml` 작성) | ⏳ 별도 commit |
| (iv) Cycle 5 (GP-3 도구 신설 2개) | ⏳ 별도 commit |
| (v) `pre-commit run --all-files` actual run SUCCESS (warm 측정) | ⏳ Cycle 자체 검증 |
| (vi) Evidence (Markdown report + actual run log) 산출 | ⏳ Cycle 후 별도 commit |
| (vii) ADR-011 §2.1 (a)~(e) 5/5 충족 + 합의 APPROVE | ⏳ 별도 합의 |
| (viii) §C-5c 부분 Satisfied 갱신 합의 (T2 sub 한정) | ⏳ A-1 답습 권고 |

### 14.2 §C-6 갱신 조건 (동상)

| 조건 | 충족 단계 |
|------|-------|
| (i)~(vii) | §14.1 동일 (PC-4 T2 sub 통합 발효 = Backlog #2 부분 충족) |
| (viii) §C-6 부분 Satisfied 갱신 합의 (PC-4 T2 sub 통합 한정) | ⏳ A-1 답습 권고 |
| (ix) §C-6 전체 Satisfied (T-1/T-3/T-4/T-5 단독 영역 충족 시) | ⏳ Backlog #2 별도 영역 |

### 14.3 §C-5c / §C-6 동시 부분 갱신 권고

| 영역 | 권고 |
|------|-----|
| 단일 합의 보고서 | ✅ 권고 (1 파일 = 1 합의 = 양 GP 동시 부분 갱신) |

---

## 15. 합의 형태 권고 + 7/7 풀 3+1 트리거 검증

### 15.1 본 brief 자체의 합의 형태

| 영역 | 합의 형태 권고 | 사유 |
|------|----------|------|
| 본 brief 자체 (DRAFT) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 준비안 한정 |
| brief 승인 후 후속 합의 (실 구현 진입) | **Reviewer-only 단축 합의 + 사용자 명시 결정** | T2 영역 한정 + 양 GP PC-3 일관 + §5.5 변경 0건 + 진입 권한 합의 (`1efb75d`) APPROVE 답습 + 사용자 결정 3개 (α/ii/ii) 확정 |

### 15.2 7/7 풀 3+1 승격 트리거 검증

| # | 트리거 | 본 brief 발화 |
|---|----|---------|
| 1 | 9 sub-수단 외 수단 *재결정* | ❌ 0건 (PC-3 본문 채택 답습 변경 0건 + 도구 신설 = PC-3 답습 *내부* 영역) |
| 2 | T3 영역 자동 진입 | ❌ 0건 (사용자 명시 10 금지 답습 + §11.2 self-audit 의무) |
| 3 | §5.5 9 sub-수단 *재결정* | ❌ 0건 (양 GP PC-3 본문 채택 유지) |
| 4 | Provider Liquidity 5-way 약화 | ❌ 0건 (`repo: local` + 옵션 (b) ii pre-commit framework venv 격리) |
| 5 | 5 영구 핵심 제약 약화 | ❌ 0건 (모든 제약 답습) |
| 6 | MVP-1 PASS *재선언* / Layer E·F 격상 | ❌ 0건 (사용자 명시 답습) |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ❌ 0건 (T3 결정 0건) |

**합산 = 7/7 0건 발화** → **Reviewer-only 단축 합의 적격**.

### 15.3 후속 합의 보고서 후보

- 경로 (사용자 명시 답습): `docs/review/3plus1-consensus-2026-05-13-pc4-t2-implementation-entry.md`
- 형태: Reviewer-only 단축 합의
- 판정 후보: **APPROVE — PC-4 T2 sub implementation entry** (사용자 명시 답습)

---

## 16. 금지 사항

### 16.1 본 brief 자체 금지 (사용자 명시 10 금지 답습)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | `.pre-commit-config.yaml` 작성 | 0건 |
| 2 | hook 본문 작성 | 0건 |
| 3 | `pre-commit install` 의무화 | 0건 |
| 4 | dev 환경 강제 | 0건 |
| 5 | branch protection 변경 | 0건 |
| 6 | CI workflow 변경 | 0건 (옵션 (c) ii 답습 — local hook 보조 도구 한정) |
| 7 | 강제 commit blocking 정책 | 0건 |
| 8 | C-5c / C-6 Satisfied 자동 갱신 | 0건 |
| 9 | MVP-1 PASS 재선언 | 0건 |
| 10 | Operational Readiness PASS 선언 | 0건 |
| (추가) | Hermes PMO 격상 | 0건 |
| (추가) | T3 영역 자동 진입 | 0건 |

### 16.2 본 brief 발효 *후* 구현 진입 단계 (Cycle 4~5) 금지

| # | 금지 | 사유 |
|---|------|------|
| 1 | `default_install_hook_types` / `fail_fast: true` / `minimum_pre_commit_version` 강제 | dev 환경 강제 답습 |
| 2 | `commit-msg` / `pre-push` / `post-commit` stage hook 추가 | branch protection 회피 답습 |
| 3 | 외부 repo (`repo: https://...`) 사용 | Provider Liquidity 답습 |
| 4 | README 강제 install 표기 | R-MVP1-G3-PC4-T2-INTG-1 답습 |
| 5 | CI workflow 본문 변경 (CI step inline grep → 도구 path 변경 등) | 사용자 명시 10 금지 #6 |
| 6 | 도구 본문 변경 (`tools/secret_scanner.py` / `tools/provider_*.py`) | Layer B `55c5b4b` 본문 채택 답습 |
| 7 | `.importlinter` config 본문 변경 | 사용자 명시 답습 + Group A 2차 답습 |
| 8 | 도구 본문 grep pattern ↔ CI inline grep pattern 본질 *불일치* | R-MVP1-G3-PC4-T2-INTG-2 답습 |
| 9 | dev install 검증 step 추가 (CI 또는 hook) | T3 간접 강제 답습 |
| 10 | Tier-2 / Tier-3 catalog 확장 | Backlog #3 별도 합의 |
| 11 | Hermes upstream Dockerfile 변경 통한 사전 install | T3 영역 + Backlog #3 |
| 12 | 실 secret 본문 commit | R-4.1 + Group D §1.2 #1 답습 (영구 금지) |
| 13 | F-금지 위반 (workflow secret 토큰 사용 등) | G3-7 (i) 답습 (영구 금지) |
| 14 | 실 API key / provider SDK / 외부 API 호출 | 영구 금지 |
| 15 | 외부 LLM 자동 호출 | 사용자 명시 결정 없이 0건 |
| 16 | §C-5c / §C-6 Satisfied 자동 갱신 (Cycle 완료 전) | Cycle + Evidence + 별도 합의 후 가능 |
| 17 | 옵션 (b) ii 답습 시 `additional_dependencies` 버전 ≠ Group A 2차 actual run 답습 버전 | R-MVP1-G3-PC4-T2-INTG-9 답습 |

---

## 17. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인** → brief 파일화 → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 commit → push | 3-commit chain (brief + 합의 + 메타) — 사용자 명시 답습 |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 그대로 승인 → 합의 보고서 작성 → 메타 + push 보류 | 2 commit 한정 |
| (D) | 본 brief 그대로 승인 → 파일화 + commit *까지만* | 1 commit 한정 |

### 17.1 권고 시작 명령

- **(A) 권고 (사용자 명시 답습)**: "옵션 (A)로 진행해주세요. 사용자 결정 (α/ii/ii) 답습 + brief 파일화 + Reviewer-only 단축 합의 보고서 작성 + 메타 갱신 + push 까지 3-commit chain 으로 진행하겠습니다."

---

## 18. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 13 검토 항목 답습 | ✅ §2 ~ §14 (13/13) |
| 사용자 명시 10 금지 답습 | ✅ §0.4 + §16.1 (10/10 + Hermes PMO + T3 자동 진입 1+1 추가 = 12/12 0건 위반) |
| 사용자 결정 3개 (α/ii/ii) 답습 | ✅ §0.2 + §6 + §7 + §4.2~4.4 + §5.3~5.4 |
| §C-5 / §C-6 답습 (변경 0건) | ✅ |
| §5.5 9 sub-수단 본문 채택 답습 (변경 0건) | ✅ |
| MVP-1 PASS Layer D 본문 답습 | ✅ |
| 5 영구 핵심 제약 보존 | ✅ |
| 7 backlog 분리 매트릭스 답습 | ✅ |
| 양 GP PC-3 일관 채택 답습 (`55c5b4b`) | ✅ |
| 7/7 풀 3+1 승격 트리거 0건 발화 | ✅ §15.2 |
| 자동 진입 0건 | ✅ §17 |
| 진입 권한 합의 (`1efb75d`) 답습 | ✅ §1.3 |
| Cycle 분할 정책 = α 확정 | ✅ §6 |
| `import-linter` `language` 옵션 = ii 확정 | ✅ §7 |
| GP-3 도구 신설 옵션 = ii 확정 (CI 변경 0건) | ✅ §4.2~4.4 + §10 |
| Rollback Trigger 12개 활성화 (기존 11 + 신규 INTG-9 + INTG-10) | ✅ §13 |

---

## 19. 본 brief 요약 (한 단락)

본 brief 는 **§C-5a Satisfied 갱신 (`6fa87dc`) + 통합 검토 합의 (`c292c9d`) + 진입 권한 합의 (`1efb75d` APPROVE — T2 sub 한정 진입 권한 발효) + 메타 commit (`476a70f`) chain 후속, 사용자 결정 옵션 (1) + (A) + 3개 결정 (α/ii/ii) 확정 답습 — §C-5c (PC-4 local pre-commit framework) 中 T2 sub-영역 (`.pre-commit-config.yaml` config 정의) 의 *Backlog #1 + #2 통합 실 구현 진입* 직전 합의 준비안 (DRAFT)** 이다. 사용자 결정 3개 확정 반영: (a) Cycle 분할 = **α (1 Cycle 통합 — 단 commit 분리 = brief / 합의 / `.pre-commit-config.yaml` 작성 / GP-3 도구 신설 / 메타)** / (b) `import-linter` `language` = **ii (`language: python` + `additional_dependencies` + `.importlinter` 본문 변경 0건)** / (c) GP-3 도구 신설 = **ii (`tools/workflow_secret_usage_check.sh` + `tools/workflow_permissions_check.sh` 신설 — 단 CI workflow 변경 0건, local hook 보조 도구 한정)**. 사용자 명시 13 검토 항목 답습 + 10 금지 + 추가 (Hermes PMO + T3 자동 진입) = 12/12 위반 0건 + 7/7 풀 3+1 트리거 0건 발화 → Reviewer-only 단축 합의 적격. Cycle 영역 = Cycle 4 `.pre-commit-config.yaml` 작성 (6 hook 통합 정의 + 옵션 ii 답습 `language: python` + `additional_dependencies`) + Cycle 5 GP-3 2 도구 신설 (CI workflow 변경 0건 답습). 도구 본문 / `.importlinter` config 변경 0건 답습. 옵션 (c) ii 답습 시 단일 source-of-truth 부분 위반 인지 명시 + R-MVP1-G3-PC4-T2-INTG-2 trigger 재해석 (단순 표현 차이 = 발화 0건 / 본질 불일치 = 발화). Rollback Trigger 12개 활성화 (기존 11 + 신규 INTG-9 버전 불일치 + INTG-10 단순 표현 차이 발화 0건). **본 brief = 준비안 한정** ≠ `.pre-commit-config.yaml` 실 본문 작성 / hook 본문 작성 / `pre-commit install` 의무화 / dev 환경 강제 / branch protection 변경 / CI workflow 변경 / §C-5c·§C-6 Satisfied 자동 갱신 / MVP-1 PASS 재선언 / Operational Readiness PASS 선언 / Hermes PMO 격상 / T3 영역 자동 진입. 다음 단계 = 사용자 명시 결정 영역 (옵션 A~D, §17 답습).

---

**작성일**: 2026-05-14 후속 3
**상태**: DRAFT (사용자 명시 승인 *전* — 옵션 (A) 3-commit chain 진입 답습 + 사용자 결정 3개 (α/ii/ii) 확정 반영)
**예상 합의 보고서** (사용자 명시 답습): `docs/review/3plus1-consensus-2026-05-13-pc4-t2-implementation-entry.md`
**예상 판정**: **APPROVE — PC-4 T2 sub implementation entry**
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~D, §17 답습)
