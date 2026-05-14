# PC-4 T2 sub 통합 *진입 직전* 합의 *준비안* Brief (DRAFT)

> **본 brief = §C-5c (PC-4 local pre-commit framework) 中 T2 sub-영역 (`.pre-commit-config.yaml` config 정의) 의 *Backlog #1 + #2 통합 실 진입 직전* 합의 준비안 (DRAFT)** — 통합 검토 결과 (`c292c9d` APPROVE AS BRIEF) 위에서 *실 진입* 결정 합의 직전 의사결정 입력 정비.
>
> 본 brief 의 어떤 §도 그 자체로 (i) 실 진입 합의 발효, (ii) `.pre-commit-config.yaml` 실 본문 작성, (iii) hook 구현 / actual run, (iv) `pre-commit install` 의무화 / dev 환경 강제, (v) branch protection 변경, (vi) CI workflow 변경, (vii) §C-5c / §C-6 Satisfied 자동 갱신, (viii) MVP-1 PASS 재선언 / Layer E·F 격상, (ix) T3 영역 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 2
**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 commit 후 합의 보고서 + 메타 + push 단계로 chain)
**상위 권위**:
- 통합 검토 합의 = `c292c9d docs(review): approve integrated PC-4 T2 sub` (Reviewer-only 단축, APPROVE AS BRIEF) — **본 brief = c292c9d 위 *실 진입* 합의 준비**
- 통합 brief = `e9614a6` (DRAFT 11 섹션, 696 lines)
- 선행 Backlog #1 단독 brief = `11d7ebb` (DRAFT 9 섹션, 516 lines)
- 메타 commit = `520ae0f` (CONTEXT/INDEX/SESSION §36 — Backlog #1 + #2 통합 검토 = APPROVE AS BRIEF)
- §C-5a 갱신 합의 = `6fa87dc` — §C-5 = `Partially Satisfied (C-5a only)` / C-5b·C-5c·C-6 Deferred 보존
- MVP-1 PASS (Layer D) = `210c98f` (APPROVE WITH CONDITIONS)
- §5.5 본문 채택 = `f40423f` + `55c5b4b` (양 GP PC-3 일관 채택)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 2)

> "(1) PC-4 T2 sub 통합 진입 직전 합의 brief를 작성해주세요. 이번 작업은 PC-4 T2 sub 통합 진입 직전 합의 brief 작성입니다. 목표: Backlog #1 + #2 공유 PC-4 T2 sub를 실제 진입시킬 수 있는지, 즉 `.pre-commit-config.yaml` config 정의 영역으로 한정해 진행 가능한지 검토한다."

> 13 검토 항목 + T2/T3 명확 분리 + 12 금지 + 텍스트 한정 산출 → 사용자 옵션 (A) 결정 후 파일화 + commit + 합의 + 메타 + push 4-commit chain.

### 0.2 본 brief 가 *하는* 것

1. PC-4 T2 sub 합의 범위 명시 (§2)
2. `.pre-commit-config.yaml` config 정의 범위 명시 (§3)
3. GP-3 3 hook 후보 *진입 직전* 정비 (§4)
4. GP-5 3 hook 후보 *진입 직전* 정비 (§5)
5. `repo: local` hooks 구조 *진입 직전* 정비 (§6)
6. CI single source-of-truth 유지 방식 (§7)
7. local pre-commit = 보조 장치 한정 (§8)
8. runtime 합산 < 30초 기준 *진입 직전* 정비 (§9)
9. false positive / false negative 위험 매트릭스 (§10)
10. T2 / T3 분리 *명확화* (§11)
11. Rollback trigger 정비 (§12)
12. Evidence 기준 정비 (§13)
13. §C-5c / §C-6 갱신 조건 (§14)
14. 합의 형태 권고 + 7/7 트리거 검증 (§15)
15. 금지 사항 (§16)
16. 다음 단계 결정 옵션 (§17)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 12 금지 답습)

- ❌ **`.pre-commit-config.yaml` 실 본문 작성 0건**
- ❌ **hook 구현 0건** (실 hook 본문 / actual run / 통합 시연)
- ❌ **`pre-commit install` 의무화 0건** (T3 영역)
- ❌ **dev 환경 강제 0건** (T3 영역)
- ❌ **branch protection 변경 0건** (Backlog #3 T3 영역)
- ❌ **CI workflow 변경 0건** (`secret-hygiene-egress-redaction.yml` / `provider-adapter-enforcement.yml` / `provider-url-scanner.yml` 본문 변경 0건 — PC-3 본문 채택 답습 변경 0건)
- ❌ **§C-5c Satisfied 자동 갱신 0건** (Deferred 그대로 유지)
- ❌ **§C-6 Satisfied 자동 갱신 0건** (Deferred 그대로 유지)
- ❌ **MVP-1 PASS *재선언* 0건** (Layer D `210c98f` 그대로 유지)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건** (MVP-6 영역, Backlog #7)
- ❌ **Hermes PMO 격상 (Layer F) 0건** (MVP-6 영역, 외부 LLM cross-vendor blind + 사람 리뷰 의무)
- ❌ **T3 영역 *자동 진입* 0건** (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 / `pre-commit install` 의무화)

### 0.4 본 brief 가 *하지 않는* 것 (추가 답습)

- ❌ §5.5 9 sub-수단 본문 채택 변경 0건 (양 GP PC-3 본문 채택 유지)
- ❌ Backlog #1 / #2 진입 합의 *발효* 0건 (본 brief = 진입 *직전* 정비 한정)
- ❌ PC-4 *수단 결정* 변경 0건 (PC-1 ~ PC-4 채택 변경)
- ❌ threshold *고정* 0건 (commit_block_rate / hook_runtime / FP_rate 모두 후보 한정)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건
- ❌ ADR 본문 자동 갱신 0건
- ❌ ADR-012 §2.2 enum 정식 등록 0건 (`pre_commit_config_local_definition_unified` 가칭 = candidate-only)
- ❌ 다른 backlog (#3/#4/#7) 자동 진입 0건
- ❌ C-2 / C-3 / C-4 / C-5a / C-5b / C-7 / C-8 자동 변경 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건

### 0.5 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 본 brief 의 어떤 §도:

- (i) 실 진입 합의를 *시작* 시키지 않으며,
- (ii) `.pre-commit-config.yaml` 실 본문 작성을 발생시키지 않으며,
- (iii) hook 구현 / actual run 을 발생시키지 않으며,
- (iv) §C-5c / §C-6 Satisfied 갱신을 발생시키지 않으며,
- (v) MVP-1 PASS 재선언 / Layer E·F 격상을 발생시키지 않으며,
- (vi) T3 sub-영역 (`pre-commit install` 의무화 / dev 환경 강제 / branch protection) 진입을 *허용* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **실 진입 합의 *직전* 의사결정 입력 정비 — T2 sub 한정 진입 적격성 + 6 hook *진입 시점* 정비 + Rollback / Evidence 기준 + §C-5c / §C-6 갱신 조건 + 합의 형태 권고**.

---

## 1. 진입 컨텍스트 답습 (`c292c9d` APPROVE AS BRIEF 후 상태)

### 1.1 4-commit chain 답습

```
선행 Backlog #1 단독 brief (11d7ebb)
   ↓ (사용자 결정 옵션 β)
Backlog #1 + #2 통합 brief (e9614a6, DRAFT 11 섹션)
   ↓
통합 검토 합의 (c292c9d, APPROVE AS BRIEF, Reviewer-only 단축 합의)
   ↓
메타 commit (520ae0f, CONTEXT/INDEX/SESSION §36)
   ↓ (origin push 완료, 모두 동기화)
■ 본 brief = PC-4 T2 sub 통합 *실 진입* 직전 합의 준비안 (DRAFT)         ← 현 위치
   ↓ (사용자 명시 승인 — 옵션 (A))
brief 파일화 → Reviewer-only 단축 합의 보고서 작성 → 진입 합의 발효
   ↓ (실 진입 합의 발효 후)
실 구현 진입 (Cycle 1~N + actual run + evidence)         ← 본 brief 영역 외
   ↓ (구현 + actual run SUCCESS + evidence 후)
§C-5c 부분 Satisfied 갱신 합의 (T2 sub 통합 한정 — T3 sub 보존)
또는
§C-6 부분 Satisfied 갱신 합의 (PC-4 T2 sub 통합 한정 — T-1/T-3/T-4/T-5 단독 영역 보존)
```

### 1.2 §C-5 / §C-6 상태 답습 (`520ae0f` 후 시점)

| Condition | 항목 | 상태 | 본 brief 관계 |
|-----------|------|------|------------|
| C-5a | ST-2 (inotify sidecar) | ✅ Satisfied (`6fa87dc`) | 답습 한정 |
| C-5b | ST-1 (Hermes Dockerfile entrypoint stat) | ⏳ Deferred (Backlog #3 T3) | 답습 한정 |
| **C-5c** | **PC-4 (local pre-commit framework)** | ⏳ **Deferred** | **본 brief = T2 sub 통합 *실 진입* 직전 정비** |
| C-5 전체 | (3 sub-condition 합산) | ⏳ Partially Satisfied (C-5a only) | 답습 한정 |
| **C-6** | **GP-5 1.5차 보강 (T-1/T-3/T-4/T-5 / PC-4)** | ⏳ **Deferred** | **본 brief = PC-4 부분 영향 답습** |

### 1.3 통합 검토 합의 결과 답습 (`c292c9d`)

| 영역 | 결과 |
|------|------|
| 판정 | APPROVE AS BRIEF (통합 검토 결과 권위 source 한정) |
| 8/8 검토 기준 | 모두 적절 |
| 11/11 금지 | 0건 위반 |
| 7/7 풀 3+1 트리거 | 0건 발화 |
| 양 GP PC-3 일관 채택 답습 | ✅ (`55c5b4b`) |
| 다음 단계 | 사용자 결정 영역 |

→ **본 brief 의 *진입 적격 토대* 충족 답습**.

---

## 2. PC-4 T2 sub 합의 범위 (검토 항목 #1)

### 2.1 합의 *범위 안*

본 brief 가 합의로 진입시키려는 *유일한* 범위:

```
PC-4 T2 sub-영역 (Backlog #1 + #2 통합)
   = repo-local `.pre-commit-config.yaml` 1 파일 본문 정의
   = 6 hook 후보 (GP-3 3 + GP-5 3) 본문 정의
   = repo-local hook 정의 — 사용자가 *선택적으로 실행 가능* 한 local check
   = CI workflow 와의 *동등 명령* 사용 (단일 source-of-truth)
```

### 2.2 합의 *범위 외*

| 영역 | 사유 |
|------|------|
| `pre-commit install` 의무화 | T3 또는 별도 정책 (사용자 명시 12 금지 中 #3) |
| dev 환경 강제 (모든 dev 환경 hook 강제 동작) | T3 (사용자 명시 12 금지 中 #4) |
| branch protection (AR-2 / AR-3 / commit signing / required check) | T3, Backlog #3 (사용자 명시 12 금지 中 #5) |
| 강제 commit blocking 정책 | T3 (간접 강제 회피, 사용자 명시 답습) |
| CI workflow *본문 변경* | PC-3 본문 채택 답습 변경 0건 (사용자 명시 12 금지 中 #6) |
| `.pre-commit-config.yaml` 실 본문 *작성* | 본 brief = 진입 *직전* 정비 한정, 작성 = 진입 합의 발효 *후* 별도 단계 (사용자 명시 12 금지 中 #1) |
| hook *구현* (실 도구 본문 변경 / 신규 도구) | 본 brief = 진입 *직전* 정비 한정 (사용자 명시 12 금지 中 #2) |

### 2.3 합의 발효 시 효과

| 효과 | 결과 |
|------|------|
| 진입 합의 발효 | ✅ — 실 구현 진입 *권한 확정* (Cycle 1~N 진입 가능) |
| `.pre-commit-config.yaml` *작성 권한* 확정 | ✅ — 단, 작성 자체 = 별도 commit 단계 (Cycle 1) |
| §C-5c 즉시 Satisfied 갱신 | ❌ — 실 구현 + actual run + evidence 후 별도 합의 |
| §C-6 즉시 Satisfied 갱신 | ❌ — 동상 |
| Layer D 본문 변경 | ❌ |
| 양 GP PC-3 본문 채택 변경 | ❌ |
| dev 환경 강제 | ❌ (T3 영역) |

---

## 3. `.pre-commit-config.yaml` config 정의 범위 (검토 항목 #2)

### 3.1 정의 범위 안

| 영역 | 본 brief 정의 |
|------|------------|
| 파일 위치 | `/.pre-commit-config.yaml` (repo root) |
| 형식 | [pre-commit framework](https://pre-commit.com) 표준 yaml 사양 답습 |
| 본문 정의 영역 | `repos[*].repo` + `repos[*].hooks[*]` 6 hook entry 정의 |
| `repo` 값 한정 | `local` 한정 — 외부 repo 의존 0건 (Provider Liquidity 5-way 답습 + ADR-008 §A.2 답습) |
| `language` 값 한정 | `system` 한정 (Hermes ≠ root of trust 답습 + Python venv 의존성 회피) — 단 `import-linter` 의존성 별도 정비 (§5.4 답습) |
| `stages` 값 한정 | `[pre-commit]` 한정 — `commit-msg` / `pre-push` / `post-commit` 등 추가 stage 0건 (branch protection 회피 답습) |

### 3.2 정의 범위 외

| 영역 | 사유 |
|------|------|
| `pre-commit install` 명시적 의무화 (예: README 강제 install 표기) | T3 영역 (사용자 명시 답습) |
| `default_install_hook_types` 변경 | T3 영역 (간접 강제) |
| dev 환경 install 비율 측정 hook (CI 가 dev install 검증) | T3 간접 강제 (사용자 명시 답습) |
| `commit-msg` stage hook (commit signing) | T3 영역 (branch protection 답습) |
| 외부 repo (`repo: https://github.com/...`) 사용 | Provider Liquidity 5-way 약화 위험 답습 — 외부 의존성 0건 한정 |

### 3.3 본문 정의 *후보* 형태 (실 본문 작성 0건 — 형식 enumerate 한정)

```yaml
# 본 brief = 형식 enumerate 한정, 실 본문 작성 0건 — 사용자 승인 후 별도 commit 영역
repos:
  - repo: local
    hooks:
      - id: <hook-id>          # §4 / §5 답습 6 후보 中 1
        name: <name>
        entry: <command>       # CI step 동등 명령 (§7 답습)
        language: system
        files: <pattern>       # §4 / §5 답습 후보
        stages: [pre-commit]
        pass_filenames: true   # default — git diff 변경 파일 한정 전달
        always_run: false      # default — 변경 파일 없으면 skip
```

### 3.4 정의 *불가능* 영역 (T3 sub 자동 진입 회피)

| 영역 | 본 brief 정의 |
|------|------------|
| `pre-commit install` 자동 실행 hook | ❌ (T3 영역) |
| `default_install_hook_types: [pre-commit, commit-msg, pre-push]` | ❌ (T3 간접 강제) |
| `fail_fast: true` (전체 강제) | ❌ (개별 hook fail 시 자체 차단 — 강제 효과 0건 답습) |
| `minimum_pre_commit_version` 강제 | ❌ (dev 환경 강제 답습) |

---

## 4. GP-3 hook 후보 *진입 직전* 정비 (검토 항목 #3)

### 4.1 hook #1 — `secret-scanner`

| 항목 | 진입 시점 정비 |
|------|----------|
| hook id | `secret-scanner` |
| name | "Secret Scanner (R-4.1 Tier-1 45 patterns)" |
| 도구 entry 후보 | `python tools/secret_scanner.py` |
| 도구 답습 | `tools/secret_scanner.py` (Group D PoC + Layer B `55c5b4b` 본문 채택 S-1, 261줄) |
| files 패턴 | `\.(py|js|ts|md|yml|yaml|sh|toml|env\.example)$` (단 R-4.1 Tier-1 답습 한정 — 실제 패턴 = Cycle 1 작성 시점 결정) |
| stages | `[pre-commit]` |
| pass_filenames | true |
| always_run | false |
| pass 기준 | exit 0 + Tier-1 45 patterns 매칭 0건 |
| fail 기준 | exit ≠ 0 |
| runtime 후보 | < 5초 (Group D actual run `25623028888` SUCCESS 답습) |
| FP 위험 후보 | < 0.5건 / 1000 line (mvp1.md §4.5.2 답습) |
| FN 위험 후보 | 0건 (Tier-1 45 patterns 답습 — Tier-2/3 catalog 자동 확장 0건 = 의도된 한계) |
| CI step 답습 | `secret-hygiene-egress-redaction.yml` 의 secret scanner step 동등 명령 |
| 본문 채택 권위 | S-1 본문 채택 답습 (`55c5b4b` §5.5.1) |
| 진입 적격 | ✅ — 도구 검증 완료 + 본문 채택 답습 |

### 4.2 hook #2 — `workflow-secret-usage-check`

| 항목 | 진입 시점 정비 |
|------|----------|
| hook id | `workflow-secret-usage-check` |
| name | "Workflow Secret Usage Check (G3-7 (i)+(ii) F-금지)" |
| 도구 entry 후보 | grep 기반 inline shell 또는 `tools/workflow_secret_usage_check.sh` (도구 신설 여부 = Cycle 1 결정) |
| 도구 답습 | grep step 본문 (G3-7 (i) GitHub Actions secrets 사용 0건 검증 + (ii) `secrets.*` 참조 감지) |
| files 패턴 | `^\.github/workflows/.*\.(yml|yaml)$` |
| stages | `[pre-commit]` |
| pass_filenames | true |
| always_run | false |
| pass 기준 | workflow 본문 `secrets\.[A-Z_]+` 참조 0건 + GitHub Actions secrets 사용 0건 |
| fail 기준 | 1+ secrets 참조 시 |
| runtime 후보 | < 1초 (workflow 디렉토리 한정 grep) |
| FP 위험 후보 | 매우 낮음 — 단, 필요한 secret 사용 (예: `GITHUB_TOKEN`) 의 FP 가능성 = Cycle 1 작성 시점 별도 패턴 정비 의무 |
| FN 위험 후보 | 매우 낮음 (yaml 본문 grep 명확) |
| CI step 답습 | G3-7 row workflow grep step 의 local 실행 형태 |
| 본문 채택 권위 | G3-7 (i) + (ii) 추가 본문 채택 답습 (`55c5b4b` §5.5.1) |
| 진입 적격 | ✅ — 본문 채택 답습 + 도구 신설 여부 = Cycle 1 결정 영역 |

### 4.3 hook #3 — `workflow-permissions-check`

| 항목 | 진입 시점 정비 |
|------|----------|
| hook id | `workflow-permissions-check` |
| name | "Workflow Permissions Check (G3-7 (v) R-6 default-deny)" |
| 도구 entry 후보 | grep 기반 inline shell 또는 `tools/workflow_permissions_check.sh` (Cycle 1 결정) |
| 도구 답습 | grep step 본문 (G3-7 (v) workflow `permissions: contents: read` 명시 강제 — R-6 답습) |
| files 패턴 | `^\.github/workflows/.*\.(yml|yaml)$` |
| stages | `[pre-commit]` |
| pass_filenames | true |
| always_run | false |
| pass 기준 | 모든 workflow 에 `permissions:` 명시 + `contents: read` 답습 |
| fail 기준 | `permissions:` 누락 또는 `contents: write` 명시 (예외 영역 별도 합의 의무) |
| runtime 후보 | < 1초 |
| FP 위험 후보 | 매우 낮음 (yaml 구조 grep 명확) |
| FN 위험 후보 | 매우 낮음 |
| CI step 답습 | G3-7 row R-6 step 동등 명령 |
| 본문 채택 권위 | G3-7 (v) 추가 본문 채택 답습 (`55c5b4b` §5.5.1) |
| 진입 적격 | ✅ — 본문 채택 답습 |

---

## 5. GP-5 hook 후보 *진입 직전* 정비 (검토 항목 #4)

### 5.1 hook #4 — `provider-import-scanner`

| 항목 | 진입 시점 정비 |
|------|----------|
| hook id | `provider-import-scanner` |
| name | "Provider Import Scanner (Group A 1차 AST 5종 패턴)" |
| 도구 entry 후보 | `python tools/provider_import_scanner.py` |
| 도구 답습 | `tools/provider_import_scanner.py` (Group A 1차 답습 — direct / from / dynamic / double-underscore / model-name) |
| files 패턴 | `^src/.*\.py$` |
| stages | `[pre-commit]` |
| pass_filenames | true |
| always_run | false |
| pass 기준 | exit 0 + 5/5 pattern 매칭 0건 |
| fail 기준 | exit ≠ 0 |
| runtime 후보 | < 10초 (Group A 1차 actual run 답습) |
| FP 위험 후보 | < 0.5건 / 1000 line (mvp1.md §4.5.1) — 단 src/ 0건 환경 측정 불가 (P1 v2 facade real 본문 작성 후 측정) |
| FN 위험 후보 | 0건 (5 pattern 답습 한정 = 의도된 범위) |
| CI step 답습 | `provider-adapter-enforcement.yml` 의 import scanner step |
| 본문 채택 권위 | T-6 中 T-5 부분 (`55c5b4b` §5.5.2) |
| 진입 적격 | ✅ — 도구 검증 완료 + 본문 채택 답습 |

### 5.2 hook #5 — `provider-url-model-scanner`

| 항목 | 진입 시점 정비 |
|------|----------|
| hook id | `provider-url-model-scanner` |
| name | "Provider URL/Model Scanner (URL Tier-1 10 + Model Tier-1 19)" |
| 도구 entry 후보 | `python tools/provider_url_scanner.py` |
| 도구 답습 | `tools/provider_url_scanner.py` (Group A 3차 답습) |
| files 패턴 | `^src/.*\.py$` |
| stages | `[pre-commit]` |
| pass_filenames | true |
| always_run | false |
| pass 기준 | exit 0 + URL Tier-1 + Model Tier-1 매칭 0건 |
| fail 기준 | exit ≠ 0 |
| runtime 후보 | < 5초 (Group A 3차 `25629390384` SUCCESS 답습) |
| FP 위험 후보 | 매우 낮음 (URL/Model name 정확 매칭) |
| FN 위험 후보 | 0건 (Tier-1 답습 한정 — Tier-2/3 자동 확장 0건) |
| CI step 답습 | `provider-url-scanner.yml` step |
| 본문 채택 권위 | T-6 中 T-5 부분 (`55c5b4b` §5.5.2) |
| 진입 적격 | ✅ |

### 5.3 hook #6 — `import-linter`

| 항목 | 진입 시점 정비 |
|------|----------|
| hook id | `import-linter` |
| name | "Import Linter (T-2 contract TR-1~TR-5)" |
| 도구 entry 후보 | `lint-imports` (또는 `python -m importlinter`) |
| 도구 답습 | `lint-imports` (T-2 답습, Group A 2차 답습 — `.importlinter` TR-1~TR-5) |
| files 패턴 | `^src/.*\.py$` 또는 `pass_filenames: false` + `always_run: true` (전체 contract scan 답습) |
| stages | `[pre-commit]` |
| pass_filenames | false (권고 — contract = 전체 그래프 검증, 변경 파일 단위 부적합) |
| always_run | true (권고 — 단, dev 환경 영향 中 검토 의무 = Cycle 1 결정) |
| pass 기준 | exit 0 + `.importlinter` 모든 contract PASS |
| fail 기준 | exit ≠ 0 |
| runtime 후보 | < 30초 (Group A 2차 `25605665191` SUCCESS 답습) |
| FP 위험 후보 | 낮음 (TR-1~TR-5 답습 — `include_external_packages = True`) |
| FN 위험 후보 | 0건 (`.importlinter` contract 답습 한정) |
| CI step 답습 | `provider-adapter-enforcement.yml` 의 import-linter step |
| 본문 채택 권위 | T-6 中 T-2 부분 (`55c5b4b` §5.5.2) |
| 진입 적격 | ⚠️ **부분 적격** — `language: system` 한정 시 `import-linter` Python package 의존성 (dev 환경 venv) 검토 의무 — Cycle 1 작성 시점 결정 영역. **권고**: `language: python` + `additional_dependencies: [import-linter]` 형태 (단, Python venv 의존성 = dev 환경 영향 — 사용자 명시 답습 위배 위험 → §5.4 추가 검토) |

### 5.4 import-linter `language` 결정 영역 (Cycle 1 결정 의무)

| 옵션 | 형식 | 장점 | 단점 |
|-----|------|------|------|
| (i) `language: system` + 사전 install 가정 | `entry: lint-imports` | dev 환경 강제 0건 답습 | dev 환경에 `import-linter` 미설치 시 hook 실행 자체 fail (opt-in 답습 한정 일관) |
| (ii) `language: python` + `additional_dependencies` | `entry: lint-imports` + `additional_dependencies: [import-linter]` | hook 자체가 venv 자동 설치 | pre-commit framework venv 사용 → dev 환경 영향 中 (단, *opt-in* 한정 시 강제 효과 0건 — 본 brief 영역 답습 가능) |

**본 brief 권고**: 옵션 (i) 또는 (ii) 中 결정 = Cycle 1 작성 시점 결정 영역. *진입 합의* = 양 옵션 모두 사용자 명시 12 금지 위반 0건 답습 (opt-in 한정 답습 시).

---

## 6. `repo: local` hooks 구조 *진입 직전* 정비 (검토 항목 #5)

### 6.1 단일 `repo: local` 구조 답습

```yaml
# 본 brief = 형식 enumerate 한정, 실 본문 작성 0건
repos:
  - repo: local
    hooks:
      - id: secret-scanner                        # §4.1
      - id: workflow-secret-usage-check           # §4.2
      - id: workflow-permissions-check            # §4.3
      - id: provider-import-scanner               # §5.1
      - id: provider-url-model-scanner            # §5.2
      - id: import-linter                         # §5.3
```

### 6.2 `repo: local` 한정 사유

| 사유 | 답습 |
|------|------|
| 외부 repo 의존성 0건 (Provider Liquidity 5-way 답습) | ✅ 답습 |
| 본 repo 도구 한정 사용 (도구 변경 시 단일 source-of-truth 답습) | ✅ 답습 |
| Hermes ≠ root of trust 답습 (외부 hook repo 신뢰 0건) | ✅ 답습 |
| pre-commit framework 자동 update 시 외부 hook 본문 변경 위험 0건 | ✅ 답습 |

### 6.3 `repos` 배열 1 entry 한정 (구조 단순성)

| 옵션 | 평가 |
|-----|------|
| (a) `repos` 배열 1 entry (`repo: local` 단일) — 6 hook 모두 1 entry 안에 정의 | ✅ **권고** — 구조 단순 + 단일 source-of-truth |
| (b) `repos` 배열 6 entry (`repo: local` 6 entry — hook 별 분리) | ⚠️ 비권고 — 중복 + yaml 본문 중복 |

---

## 7. CI single source-of-truth 유지 방식 (검토 항목 #6)

### 7.1 도구 본문 = single source-of-truth

| 도구 | 사용 위치 | 동기화 보장 |
|------|---------|----------|
| `tools/secret_scanner.py` | CI (`secret-hygiene-egress-redaction.yml`) + local hook (`secret-scanner`) | 도구 본문 변경 시 양쪽 자동 일관 |
| 도구 신설 (`tools/workflow_secret_usage_check.sh` 등) | CI + local hook 양쪽 동시 사용 | 동상 |
| `tools/provider_import_scanner.py` | CI (`provider-adapter-enforcement.yml`) + local hook | 동상 |
| `tools/provider_url_scanner.py` | CI (`provider-url-scanner.yml`) + local hook | 동상 |
| `lint-imports` (외부 도구) + `.importlinter` (config) | CI + local hook | config 본문 변경 시 양쪽 자동 일관 |

### 7.2 hook entry = CI step 명령 *동등*

| 영역 | CI step 답습 | local hook entry 후보 |
|------|---------|----------------|
| GP-3 secret scanner | `python tools/secret_scanner.py ${changed_files}` | `python tools/secret_scanner.py` (pre-commit framework 가 변경 파일 자동 전달) |
| GP-3 workflow secret usage | grep inline | hook entry = grep inline 또는 도구 path |
| GP-3 workflow permissions | grep inline | 동상 |
| GP-5 provider import scanner | `python tools/provider_import_scanner.py ...` | `python tools/provider_import_scanner.py` |
| GP-5 provider url/model scanner | `python tools/provider_url_scanner.py ...` | `python tools/provider_url_scanner.py` |
| GP-5 import-linter | `lint-imports` | `lint-imports` |

### 7.3 단일 source-of-truth 위반 검출 trigger 답습

| Trigger | 발화 조건 | 발화 시 행동 |
|---------|---------|----------|
| **R-MVP1-G3-PC4-T2-INTG-2** (통합 brief §7.2 답습) | hook entry 와 CI step 명령 *불일치* 검출 | 합의 재진입 + hook entry 동기화 의무 |

### 7.4 CI gating = 강제 (PC-3 답습)

| 영역 | 답습 |
|------|------|
| GP-3 CI gating | `secret-hygiene-egress-redaction.yml` Stage 1+3 SUCCESS 답습 |
| GP-5 CI gating | `provider-adapter-enforcement.yml` Stage 4 SUCCESS + `provider-url-scanner.yml` Stage 5 SUCCESS 답습 |
| AR-1 CI step fail-closed | 양 GP 일관 본문 채택 답습 (`55c5b4b`) |
| 강제 효과 = CI 한정 | local hook = opt-in 한정 (강제 효과 0건) |

---

## 8. local pre-commit = 보조 장치 한정 (검토 항목 #7)

### 8.1 보조 장치 본질

| 차원 | local pre-commit (T2 sub) | CI gating (PC-3 본문 채택 답습) |
|------|------------------------|-------------------------|
| 강제 여부 | ❌ opt-in 한정 | ✅ 강제 (PR auto-reject) |
| dev 환경 영향 | ❌ 0건 (강제 install 의무 0건 답습) | ❌ 0건 (CI 한정) |
| Defense in depth | 보조 layer (개발자 자발적 사용 시 commit 전 사전 검증) | 주 layer (PR 차단) |
| 검증 우회 가능성 | ✅ (개발자가 `--no-verify` 또는 미설치 시) | ❌ (CI fail-closed) |
| 본 brief 정의 영역 | ✅ T2 sub | ❌ 본 brief 영역 외 (이미 본문 채택 답습 — 변경 0건) |

### 8.2 보조 장치 의도

본 brief = local pre-commit 을 **개발자의 *선택적* 사전 검증 도구** 로 정의:

- 개발자가 `pre-commit install` 자발적 실행 시 → commit 전 hook 자동 동작 → CI fail 전 사전 검출 가능
- 개발자가 install 0건 시 → local hook 동작 0건 → CI gating 만 동작 (현 PC-3 답습 그대로)
- 개발자가 `--no-verify` 사용 시 → local hook 우회 가능 → CI gating 만 동작

### 8.3 보조 장치 의도 *위반* 시도 검출 trigger

| Trigger | 발화 조건 | 발화 시 행동 |
|---------|---------|----------|
| **R-MVP1-G3-PC4-T2-INTG-1** (통합 brief §7.2 답습) | dev 환경 *간접 강제* 시도 검출 (예: README 강제 install 표기 / CI 가 dev install 검증 step 추가 / `default_install_hook_types` 변경 등) | T3 영역 부분 진입 거부 + 본 brief §0.3 답습 (사용자 명시 12 금지 中 #3 + #4) |

---

## 9. runtime 합산 < 30초 기준 *진입 직전* 정비 (검토 항목 #8)

### 9.1 runtime 합산 매트릭스

| hook | runtime 후보 (개별) | 답습 |
|------|---------------|------|
| `secret-scanner` | < 5초 | Group D actual run `25623028888` SUCCESS |
| `workflow-secret-usage-check` | < 1초 | grep 한정 |
| `workflow-permissions-check` | < 1초 | grep 한정 |
| `provider-import-scanner` | < 10초 | Group A 1차 actual run |
| `provider-url-model-scanner` | < 5초 | Group A 3차 `25629390384` SUCCESS |
| `import-linter` | < 30초 | Group A 2차 `25605665191` SUCCESS |
| **순차 합산** | < 52초 (worst case) | (참조 한정) |
| **병렬 합산** | < 30초 (max hook = `import-linter`) | pre-commit framework hook 병렬 default |

### 9.2 병렬 < 30초 기준 적격성

| 차원 | 평가 |
|------|------|
| pre-commit framework default 병렬 동작 답습 | ✅ |
| max hook = `import-linter` 답습 (Group A 2차 actual run) | ✅ |
| dev 환경 commit 1회 당 30초 = 일반 개발 흐름 부담 | ⚠️ 中 — 단, opt-in 한정 답습 (강제 효과 0건) → dev 환경 영향 0건 |
| threshold *고정* | ❌ — 후보 한정 (mvp1.md §4.5.2 답습) |

### 9.3 runtime 폭증 trigger 답습

| Trigger | 발화 조건 | 발화 시 행동 |
|---------|---------|----------|
| **R-MVP1-G3-PC4-T2-INTG-3** (통합 brief §7.2 답습) | hook runtime 합산 폭증 (예: > 60초 — threshold 후보) | hook 분리 / 도구 최적화 합의 |

---

## 10. false positive / false negative 위험 매트릭스 (검토 항목 #9)

### 10.1 FP 위험 매트릭스

| hook | FP 위험 후보 | 사유 | 진입 시점 의무 |
|------|---------|------|----------|
| `secret-scanner` | < 0.5건 / 1000 line | R-4.1 Tier-1 45 patterns 답습 | mvp1.md §4.5.2 답습 (정량 결정 영역 외) |
| `workflow-secret-usage-check` | 매우 낮음 | grep pattern 명확 — 단 `GITHUB_TOKEN` 등 필요 secret FP 검토 의무 | Cycle 1 작성 시점 예외 패턴 정비 의무 |
| `workflow-permissions-check` | 매우 낮음 | yaml 구조 grep 명확 | — |
| `provider-import-scanner` | < 0.5건 / 1000 line | mvp1.md §4.5.1 답습 | src/ 0건 환경 측정 불가 (P1 v2 facade real 본문 작성 후 측정) |
| `provider-url-model-scanner` | 매우 낮음 | URL/Model name 정확 매칭 | — |
| `import-linter` | 낮음 | TR-1~TR-5 답습 + `include_external_packages = True` | — |

### 10.2 FN 위험 매트릭스

| hook | FN 위험 후보 | 사유 |
|------|---------|------|
| `secret-scanner` | 0건 (Tier-1 한정) | Tier-2/3 catalog 자동 확장 0건 = 의도된 범위 (R-4.1 답습) |
| `workflow-secret-usage-check` | 매우 낮음 | grep pattern 명확 |
| `workflow-permissions-check` | 매우 낮음 | yaml 구조 grep 명확 |
| `provider-import-scanner` | 0건 (5 pattern 한정) | Group A 1차 답습 = 의도된 범위 |
| `provider-url-model-scanner` | 0건 (Tier-1 한정) | Tier-2/3 자동 확장 0건 = 의도된 범위 |
| `import-linter` | 0건 (`.importlinter` contract 답습 한정) | TR-1~TR-5 답습 |

### 10.3 FP / FN 폭증 trigger 답습

| Trigger | 발화 조건 | 발화 시 행동 |
|---------|---------|----------|
| **R-MVP1-G3-PC4-T2-INTG-4** (통합 brief §7.2 답습) | FP_rate 폭증 (예: > 5건 / 1000 line — threshold 후보) | hook pattern 재검토 합의 |
| (신규 후보) **R-MVP1-G3-PC4-T2-INTG-5** | FN 검출 (Tier-1 답습 패턴 中 의도 매칭 누락) | 도구 본문 재검토 + 합의 (단, Tier-2/3 catalog 확장 = 별도 합의) |

---

## 11. T2 / T3 분리 *명확화* (검토 항목 #10)

### 11.1 T2 sub-영역 (본 brief 진입 영역)

```
T2 sub:
- .pre-commit-config.yaml config 정의 (본 brief §3 답습)
- repo-local hook 정의 (본 brief §6 답습)
- 사용자가 *선택적으로* 실행 가능한 local check (본 brief §8 답습)
```

| 영역 | 본 brief 처리 |
|------|----------|
| `.pre-commit-config.yaml` 본문 정의 | ✅ 진입 (Cycle 1~N) |
| 6 hook entry 정의 | ✅ 진입 |
| `repo: local` 한정 + `language: system` 한정 + `[pre-commit]` stage 한정 | ✅ 진입 |
| opt-in 한정 — 개발자 자발적 사용 | ✅ 진입 |

### 11.2 T3 sub-영역 (본 brief 진입 *영역 외*)

```
T3 sub:
- pre-commit install 의무화
- dev 환경 강제
- branch protection
- 강제 commit blocking 정책
```

| 영역 | 본 brief 처리 | 사유 |
|------|----------|------|
| `pre-commit install` 의무화 | ❌ 진입 영역 외 | 사용자 명시 12 금지 #3 |
| dev 환경 강제 | ❌ 진입 영역 외 | 사용자 명시 12 금지 #4 |
| branch protection (AR-2 / AR-3 / commit signing / required check / CODEOWNERS) | ❌ 진입 영역 외 | 사용자 명시 12 금지 #5 + Backlog #3 분리 |
| 강제 commit blocking 정책 (`fail_fast: true` 강제 / `default_install_hook_types` 변경 등) | ❌ 진입 영역 외 | 사용자 명시 답습 (간접 강제 회피) |
| Hermes upstream Dockerfile 변경 통한 사전 install | ❌ 진입 영역 외 | 사용자 명시 답습 + Backlog #3 T3 |
| Vault HSM (ST-4) | ❌ | Backlog #7 분리 |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ | Backlog #3 분리 |

### 11.3 T3 영역 자동 진입 0건 의무 답습

본 brief 진입 합의 발효 후에도 위 T3 sub 영역 모두 *자동 진입 0건* 의무 (사용자 명시 답습 + ADR-011 §2.4 답습 + 통합 brief §8.2 답습 + 합의 보고서 §3.2 답습).

---

## 12. Rollback Trigger 정비 (검토 항목 #11)

### 12.1 본 진입 합의 발효 후 활성화 Trigger

| Trigger ID | 발화 조건 | 발화 시 행동 | 우선순위 |
|----------|---------|-------------|------|
| R-MVP1-G3-4 | PC-3 부분 CI runtime 폭증 (>2분) — pre-commit hook 정의 ↔ CI step 불일치 시 발화 | threshold 재결정 합의 (단축 적격) | 高 |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | T3 영역 → 풀 3+1 합의 + branch protection rule 변경 검토 (Backlog #3) | 高 |
| R-MVP1-G5-6 | T-9 (pre-commit hook PC-1) 도입 별도 합의 (Group A 2차 §8 TR-5 답습) | 본 PoC 와의 책무 분리 재합의 | 中 |
| **R-MVP1-G3-PC4-T2-INTG-1** | dev 환경 *간접 강제* 시도 검출 (README 강제 / CI 가 dev install 검증 step / `default_install_hook_types` 변경 등) | T3 영역 부분 진입 거부 + 본 brief §0.3 답습 | **高** |
| **R-MVP1-G3-PC4-T2-INTG-2** | hook entry ↔ CI step 명령 *불일치* 검출 (단일 source-of-truth 위반) | 합의 재진입 + hook entry 동기화 의무 | **高** |
| **R-MVP1-G3-PC4-T2-INTG-3** | hook runtime 합산 폭증 (예: > 60초 — threshold 후보) | hook 분리 / 도구 최적화 합의 | 中 |
| **R-MVP1-G3-PC4-T2-INTG-4** | FP_rate 폭증 (예: > 5건 / 1000 line — threshold 후보) | hook pattern 재검토 합의 | 中 |
| **(신규) R-MVP1-G3-PC4-T2-INTG-5** | FN 검출 (Tier-1 답습 패턴 의도 매칭 누락) | 도구 본문 재검토 (Tier-2/3 확장 = 별도 합의) | 中 |
| **(신규) R-MVP1-G3-PC4-T2-INTG-6** | `import-linter` `language` 옵션 (i)/(ii) 결정 후 dev 환경 영향 中 검출 | Cycle 1 결정 재합의 + 옵션 전환 검토 | 中 |

### 12.2 trigger 발화 ≠ 자동 행동 답습

본 §12 = trigger *enumerate* 한정. 실 trigger 발화 시연 = Layer C 영역 / 진입 발효 시점 별도 작업 영역. threshold *고정* = mvp1.md §4.5.2 답습 (정량 결정 영역 외 — 후보 한정).

---

## 13. Evidence 기준 정비 (검토 항목 #12)

### 13.1 ADR-011 §2.1 (a)~(e) 5조건 답습

| # | 조건 | 본 PC-4 T2 sub 통합 진입 적용 |
|---|------|--------------------|
| (a) | 동등 이상의 보안 결과 | `.pre-commit-config.yaml` 본문 정의 = PC-3 답습 (CI gating, 강제) 위에서 *opt-in defense in depth 추가* — 강제 효과 0건 명시 답습 (사용자 명시 답습) |
| (b) | 격리 환경 PoC 실증 | local repo 격리 환경에서 6 hook 정의 + opt-in 시 hook 동작 시연 (강제 환경 시연 0건) — Cycle N actual run 별도 단계 |
| (c) | ADR / SDD 권위 명시 | mvp1.md §4.3 + §5.5.1 / §5.5.2 + ADR-011 §2.4 + 선행 brief + 통합 brief + 합의 보고서 + 본 brief 답습 — ✅ |
| (d) | 자동 회귀 검증 경로 확보 | `.pre-commit-config.yaml` schema 검증 (CI step 통한 yaml syntax + hook id 중복 검출) — opt-in 답습 한정 + CI gating 답습 (PC-3 강제) |
| (e) | 합의 APPROVE | 본 brief 후속 합의 보고서 + 사용자 명시 (별도 단계) |

### 13.2 Evidence 산출물 후보 (본 brief 영역 외)

| Evidence | 형식 | 산출 시점 |
|----------|------|--------|
| Markdown report | `docs/phase0/g2-gp3-gp5-pc4-t2-evidence.md` (가칭) | Cycle N actual run 후 |
| JSONL ledger entry | `docs/evidence/ledger.jsonl` 신규 entry (`event: pre_commit_config_local_definition_unified` 가칭 = candidate-only) | Cycle N actual run 후 |
| Docker isolation log | local repo 격리 환경 hook actual run log (격리 환경 0 — pre-commit framework local 한정) | Cycle N |
| GitHub Actions run | `.pre-commit-config.yaml` schema 검증 step 통합 시 actual run id | Cycle N |
| 합의 보고서 | `docs/review/3plus1-consensus-2026-05-13-pc4-t2-entry.md` (사용자 명시 후보) — 본 brief 후속 단계 | 본 brief 승인 후 |
| §C-5c / §C-6 부분 Satisfied 갱신 합의 | `docs/review/3plus1-consensus-<date>-c5c-pc4-t2-satisfaction.md` 가칭 | actual run + evidence + 별도 합의 |

---

## 14. §C-5c / §C-6 갱신 조건 (검토 항목 #13)

### 14.1 §C-5c 갱신 조건

| 조건 | 충족 여부 |
|------|-------|
| (i) PC-4 T2 sub 통합 진입 합의 발효 | ⏳ 본 brief 후속 합의 단계 |
| (ii) `.pre-commit-config.yaml` 본문 작성 (Cycle 1) | ⏳ 본 brief 영역 외 (진입 합의 발효 후 별도 commit) |
| (iii) 6 hook 본문 정의 + actual run SUCCESS | ⏳ Cycle 2~N 영역 (본 brief 영역 외) |
| (iv) ADR-011 §2.1 (a)~(d) 4/4 충족 + (e) 합의 APPROVE | ⏳ 별도 합의 단계 |
| (v) §C-5c 부분 Satisfied 갱신 합의 (T2 sub 한정 — T3 sub 보존) | ⏳ A-1 답습 권고 (Layer D 본문 변경 0건, 본 합의 보고서가 갱신 권위 source — `1dd1036` + `6fa87dc` 답습) |

→ **§C-5c 부분 Satisfied 갱신** = T2 sub 통합 진입 + 구현 + actual run + evidence + 별도 합의 *모두 충족 후* 가능. **본 brief = (i) 단계 진입 *직전* 정비 한정**.

### 14.2 §C-6 갱신 조건

| 조건 | 충족 여부 |
|------|-------|
| (i) PC-4 T2 sub 통합 진입 발효 (Backlog #2 부분 충족) | ⏳ 본 brief 후속 합의 단계 |
| (ii) Backlog #2 의 GP-5 1.5차 *나머지* 영역 (T-1/T-3/T-4/T-5 단독 등) 별도 합의 | ⏳ Backlog #2 단독 brief 영역 (본 brief 영역 외) |
| (iii) §C-6 부분 Satisfied 갱신 합의 (PC-4 T2 sub 통합 한정) | ⏳ A-1 답습 권고 (Layer D 본문 변경 0건) |
| (iv) §C-6 전체 Satisfied 갱신 (T-1/T-3/T-4/T-5 단독 영역 충족 시) | ⏳ Backlog #2 별도 합의 영역 |

→ **§C-6 부분 Satisfied 갱신** = PC-4 T2 sub 통합 발효 후 가능 (Backlog #2 부분 충족). **§C-6 전체 Satisfied 갱신** = Backlog #2 GP-5 1.5차 *전체* 영역 (PC-4 + T-1/T-3/T-4/T-5 단독) 모두 충족 시 가능 — 별도 합의.

### 14.3 §C-5c / §C-6 동시 부분 갱신 가능성

| 영역 | 가능성 |
|------|------|
| 단일 합의 보고서로 §C-5c + §C-6 동시 부분 Satisfied 갱신 | ✅ 가능 — PC-4 T2 sub 통합 = GP-3 + GP-5 양쪽 영향 답습 (1 파일 본질) |
| 분리 합의 보고서 (§C-5c 단독 갱신 + §C-6 단독 갱신) | ✅ 가능 — 단, 합의 효율 ↓ + 일관성 검증 2 회 |
| **본 brief 권고** | ⚠️ **단일 합의 권고** (1 파일 = 1 합의 = 양 GP 동시 부분 갱신) — 단, 결정 = 사용자 명시 결정 영역 |

---

## 15. 합의 형태 권고 + 7/7 풀 3+1 트리거 검증

### 15.1 본 brief 자체의 합의 형태

| 영역 | 합의 형태 권고 | 사유 |
|------|----------|------|
| 본 brief 자체 (DRAFT) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 (`backlog1-st2-c5a-satisfaction-brief.md` + 통합 brief + 선행 brief 패턴 답습) |
| brief 승인 후 후속 합의 (실 진입 결정) | **Reviewer-only 단축 합의 + 사용자 명시 결정** | T2 영역 한정 + 양 GP PC-3 일관 채택 답습 + §5.5 변경 0건 + 통합 검토 결과 (`c292c9d`) APPROVE AS BRIEF 답습 |

### 15.2 7/7 풀 3+1 승격 트리거 검증

| # | 트리거 | 본 brief 발화 |
|---|----|---------|
| 1 | 9 sub-수단 외 수단 *재결정* | ❌ 0건 (PC-3 본문 채택 답습 변경 0건) |
| 2 | T3 영역 자동 진입 (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 / `pre-commit install` 의무화) | ❌ 0건 (사용자 명시 12 금지 답습) |
| 3 | §5.5 9 sub-수단 *재결정* | ❌ 0건 (양 GP PC-3 본문 채택 유지) |
| 4 | Provider Liquidity 5-way 약화 | ❌ 0건 (`repo: local` + `language: system` 답습 — 외부 의존성 0건) |
| 5 | 5 영구 핵심 제약 약화 | ❌ 0건 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 모두 답습) |
| 6 | MVP-1 PASS *재선언* / Layer E / Layer F 격상 | ❌ 0건 (사용자 명시 12 금지 #9·#10·#11 답습) |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ❌ 0건 (T3 결정 0건) |

**합산 = 7/7 0건 발화** → **본 brief 승인 후 합의 = Reviewer-only 단축 합의 적격**.

### 15.3 후속 합의 보고서 후보

- 경로 후보 (사용자 명시 답습): `docs/review/3plus1-consensus-2026-05-13-pc4-t2-entry.md`
- 형태: Reviewer-only 단축 합의
- 판정 후보: APPROVE AS BRIEF 또는 APPROVE WITH CONDITIONS

---

## 16. 금지 사항

### 16.1 본 brief 자체 금지 (사용자 명시 12 금지 답습)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | `.pre-commit-config.yaml` 작성 | 0건 |
| 2 | hook 구현 | 0건 |
| 3 | `pre-commit install` 의무화 | 0건 |
| 4 | dev 환경 강제 | 0건 |
| 5 | branch protection | 0건 |
| 6 | CI workflow 변경 | 0건 |
| 7 | C-5c Satisfied 자동 갱신 | 0건 |
| 8 | C-6 Satisfied 자동 갱신 | 0건 |
| 9 | MVP-1 PASS 재선언 | 0건 |
| 10 | Operational Readiness PASS 선언 | 0건 |
| 11 | Hermes PMO 격상 | 0건 |
| 12 | T3 영역 자동 진입 | 0건 |

### 16.2 본 brief 발효 *후* 진입 단계 금지 (진입 시 의무 답습)

| # | 금지 | 사유 |
|---|------|------|
| 1 | dev 환경 강제 (`pre-commit install` 의무화 / `default_install_hook_types` 변경) | 사용자 명시 12 금지 #3·#4 답습 |
| 2 | branch protection rule 변경 (AR-2 진입) | 사용자 명시 12 금지 #5 답습 |
| 3 | T3 영역 자동 진입 | 사용자 명시 12 금지 #12 답습 |
| 4 | hook entry 통한 *간접* dev 환경 강제 (예: CI 가 dev install 검증 step 추가) | R-MVP1-G3-PC4-T2-INTG-1 답습 |
| 5 | hook entry ↔ CI step 불일치 (단일 source-of-truth 위반) | R-MVP1-G3-PC4-T2-INTG-2 답습 |
| 6 | `commit-msg` / `pre-push` / `post-commit` stage hook 추가 | branch protection 회피 답습 (사용자 명시 답습) |
| 7 | 외부 repo (`repo: https://...`) 사용 | Provider Liquidity 5-way 답습 |
| 8 | Tier-2 / Tier-3 catalog 확장 (R-4.1 / URL Tier-1 / Model Tier-1 변경) | Backlog #3 별도 합의 |
| 9 | 실 secret 본문 commit | R-4.1 + Group D §1.2 #1 답습 (영구 금지) |
| 10 | F-금지 위반 (workflow secret 토큰 사용 등) | G3-7 (i) 답습 (영구 금지) |
| 11 | 실 API key / provider SDK / 외부 API 호출 | 영구 금지 |
| 12 | 외부 LLM 자동 호출 | 사용자 명시 결정 없이 0건 |
| 13 | Hermes upstream Dockerfile 변경 통한 hook 사전 install | T3 영역 + Backlog #3 |

---

## 17. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인** → brief 파일화 (`docs/phase0/backlog1-2-pc4-t2-entry-brief.md`) → commit (`docs(phase0): add integrated PC-4 T2 entry brief`) → Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-13-pc4-t2-entry.md`) → commit (`docs(review): approve PC-4 T2 entry`) → 메타 갱신 commit → push | 4-commit chain (선행 통합 검토 chain 답습) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 보류 → 다른 backlog 우선 (Backlog #2 단독 / Backlog #3 / MVP-2 / 세션 종료) | 우선 backlog 결정 |
| (D) | 본 brief 그대로 승인 → 파일화 + commit *까지만* (합의 보고서 작성 + 메타 갱신 + push 보류) | 1 commit 한정 |

### 17.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A)로 진행해주세요. 본 brief 를 파일화하고, 합의 보고서 + 메타 갱신 + push 까지 4-commit chain 으로 진행하겠습니다."
- (B): "옵션 (B)로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C)로 진행해주세요. 우선 backlog (예: Backlog #2 / Backlog #3 / MVP-2 / 세션 종료) 결정으로 전환합니다."
- (D): "옵션 (D)로 진행해주세요. 본 brief 파일화 + commit 까지만 진행합니다."

---

## 18. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 13 검토 항목 답습 | ✅ §2 ~ §14 (13/13) |
| 사용자 명시 12 금지 답습 | ✅ §0.3 + §16.1 (12/12 0건 위반) |
| T2 / T3 명확 분리 답습 | ✅ §11 (T2 진입 / T3 진입 영역 외 명시) |
| §C-5 / §C-6 답습 (모두 변경 0건) | ✅ |
| §5.5 9 sub-수단 본문 채택 답습 (변경 0건) | ✅ |
| MVP-1 PASS Layer D 본문 답습 (`210c98f` 그대로 유지) | ✅ |
| 5 영구 핵심 제약 보존 | ✅ |
| 7 backlog 분리 매트릭스 답습 (Backlog #3/#4/#7 분리 + Backlog #2 = 통합 진입 영역 답습) | ✅ |
| 양 GP PC-3 일관 채택 답습 (`55c5b4b`) | ✅ |
| 7/7 풀 3+1 승격 트리거 0건 발화 | ✅ §15.2 |
| 자동 진입 0건 (모든 다음 단계 = 사용자 명시 결정 영역) | ✅ §17 |
| 통합 검토 합의 (`c292c9d`) 답습 | ✅ §1.3 |
| 통합 brief (`e9614a6`) §1~§11 답습 | ✅ |

---

## 19. 본 brief 요약 (한 단락)

본 brief 는 **§C-5a Satisfied 갱신 (`6fa87dc`) + 선행 Backlog #1 단독 brief (`11d7ebb`) + 통합 brief (`e9614a6`) + 통합 검토 합의 (`c292c9d` APPROVE AS BRIEF) + 메타 commit (`520ae0f`) chain 후속, 사용자 결정 옵션 (1) 답습 — §C-5c (PC-4 local pre-commit framework) 中 T2 sub-영역 (`.pre-commit-config.yaml` config 정의) 의 *Backlog #1 + #2 통합 실 진입* 직전 합의 준비안 (DRAFT)** 이다. 사용자 명시 13 검토 항목 답습 (PC-4 T2 sub 합의 범위 / `.pre-commit-config.yaml` config 정의 범위 / GP-3 3 hook 후보 / GP-5 3 hook 후보 / `repo: local` hooks 구조 / CI single source-of-truth / local = 보조 장치 / runtime 합산 < 30초 / FP·FN 위험 / T2·T3 분리 / Rollback Trigger / Evidence 기준 / §C-5c·§C-6 갱신 조건). T2 sub 영역 = `.pre-commit-config.yaml` 정의 + repo-local hook 정의 + opt-in 한정 사용자 선택 가능 local check (진입 ✅) / T3 sub 영역 = `pre-commit install` 의무화 + dev 환경 강제 + branch protection + 강제 commit blocking 정책 (진입 영역 외 ❌). 양 GP PC-3 일관 채택 답습 위 6 hook 후보 모두 본문 채택 권위 답습 + 도구 검증 완료 + 진입 적격 (단 `import-linter` `language` 옵션 = Cycle 1 결정 영역). 사용자 명시 12 금지 12/12 위반 0건 + 7/7 풀 3+1 승격 트리거 0건 발화 → **Reviewer-only 단축 합의 적격**. §C-5c / §C-6 갱신 = 본 진입 합의 발효 + Cycle 1~N 구현 + actual run + evidence + 별도 합의 *모두 충족 후* 부분 Satisfied 갱신 가능 (A-1 답습 권고). **본 brief = 준비안 한정** ≠ `.pre-commit-config.yaml` 실 본문 작성 / hook 구현 / `pre-commit install` 의무화 / dev 환경 강제 / branch protection 변경 / CI workflow 변경 / §C-5c·§C-6 Satisfied 자동 갱신 / MVP-1 PASS 재선언 / Operational Readiness PASS 선언 / Hermes PMO 격상 / T3 영역 자동 진입. 다음 단계 = 사용자 명시 결정 영역 (옵션 A~D, §17 답습).

---

**작성일**: 2026-05-14 후속 2
**상태**: DRAFT (사용자 명시 승인 *전* — 옵션 (A) 4-commit chain 진입 답습)
**예상 합의 보고서** (사용자 명시 답습): `docs/review/3plus1-consensus-2026-05-13-pc4-t2-entry.md`
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~D, §17 답습)
