# §C-5c PC-4 T2 sub 검토 *준비안* Brief (DRAFT)

> **본 brief = §C-5c (PC-4 local pre-commit framework) 中 T2 sub 영역 (`.pre-commit-config.yaml` config 정의 가능성) 한정 검토 *준비안* (DRAFT)** — Backlog #1 + Backlog #2 공유 PC-4 영역의 *T2 sub-영역* 만 범위 안에 둠.
>
> 본 brief 의 어떤 §도 그 자체로 (i) §C-5c Satisfied 갱신 / 부분 갱신을 발생시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) PC-4 T3 sub-영역 (dev 환경 강제 / `pre-commit install` 의무화 / branch protection) / Operational Readiness PASS / Hermes PMO 격상 / 다른 backlog 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-14
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위**:
- §C-5a 갱신 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-c5a-satisfaction.md` (commit `6fa87dc`, APPROVE — Reviewer-only 단축, A-1 답습 / `43f1e12` brief / `2a6d9dd` 메타) — §C-5 = `Partially Satisfied (C-5a only)` / C-5b·C-5c = `Deferred` 보존
- Backlog #1 진입 직전 사전 정비 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (commit `43b898c`)
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, APPROVE WITH CONDITIONS)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §4.3.1 (PC-1 ~ PC-4 매트릭스) + §4.3.2 (권고) + §4.5.2 (PC-1/PC-4 metric / threshold) + §4.7.3 (합의 형태 권고) + §5.5.1 / §5.5.2 (PC-3 본문 채택 답습)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 (T1/T2/T3 3-tier 분류)
- ADR-011 §2.1 (a)~(e) 5조건 패턴
- Backlog #1 deepening brief §2.3 / §2.3.3 (PC-4 T2/T3 sub-영역 분리)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "C-5c PC-4 T2 sub 검토 brief를 작성해주세요. 범위는 Backlog #1 + Backlog #2 공유 영역인 PC-4 local pre-commit framework 중, T2 sub 영역인 `.pre-commit-config.yaml` config 정의 가능성 검토까지로 제한합니다. dev 환경 강제, pre-commit install 의무화, branch protection, T3 영역, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. PC-4 T2 sub-영역 정의 답습 (deepening brief §2.3.3 답습 — `.pre-commit-config.yaml` 본문 정의 한정) (§1 ~ §2)
2. `.pre-commit-config.yaml` config *정의 가능성* 분석 (§3.1) — 기술적 가능성 / Backlog #1 + #2 공유 처리 옵션 / hook 카탈로그 후보
3. Backlog #1 + Backlog #2 공유 PC-4 영역의 T2 sub 단독 진입 적격성 검토 (§3.2)
4. 합의 형태 권고 + 풀 3+1 승격 트리거 후보 검증 (§4)
5. T2 sub 발효 *시점* 의무 정리 (Rollback Trigger / Evidence) — 본 brief 영역 외 명시 (§5)
6. 본 brief 자체 + 후속 단계 *금지 사항* enumerate (§6)
7. 다음 단계 결정 옵션 (사용자 결정 영역, §7)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 6 금지 답습)

- ❌ **dev 환경 강제 0건** — `.pre-commit-config.yaml` 가 repo 에 존재해도 dev 환경 강제 의무 부여 0건 (opt-in 한정 검토)
- ❌ **`pre-commit install` 의무화 0건** — 모든 개발자 dev 환경 install 의무 명시 0건
- ❌ **branch protection 변경 0건** — AR-2 / AR-3 / GitHub repo policy 변경 검토 0건 (Backlog #3 T3 영역)
- ❌ **T3 영역 진입 0건** — Hermes upstream Dockerfile / Vault HSM / Tier-2-3 catalog 자동 확장 / branch protection / dev 환경 강제 정책 모두 본 brief 영역 외
- ❌ **Operational Readiness PASS (Layer E) 선언 0건** — MVP-6 영역 (C-3 Deferred 답습)
- ❌ **Hermes PMO 격상 (Layer F) 0건** — MVP-6 영역 (C-4 Deferred 답습 + 외부 LLM cross-vendor blind + 사람 리뷰 의무)

### 0.4 본 brief 가 *하지 않는* 것 (추가 답습)

- ❌ **§C-5c Satisfied / 부분 Satisfied 갱신 0건** (본 brief = 준비안 한정 — 갱신 발효 = 별도 합의 보고서 영역)
- ❌ **§C-5 전체 표기 갱신 0건** (`Partially Satisfied (C-5a only)` 그대로 유지, `6fa87dc` 답습)
- ❌ **MVP-1 PASS *재선언* 0건** (Layer D `210c98f` 그대로 유지)
- ❌ **Backlog #1 / #2 진입 합의 발효 0건** (PC-4 T2 sub 진입 결정 = 별도 합의 영역)
- ❌ **PC-4 *수단 결정* 0건** (PC-1 / PC-2 / PC-3 / PC-4 채택 변경 0건 — 본 brief = 가능성 *분석* 한정)
- ❌ **§5.5 9 sub-수단 본문 채택 *변경* 0건** (PC-3 본문 채택 유지, Layer B `f40423f` + `55c5b4b` 답습)
- ❌ **threshold *고정* 0건** (commit_block_rate / dev_env_install_rate / hook_runtime 모두 *후보 한정* 유지)
- ❌ **실 runtime code / `.pre-commit-config.yaml` *본문 작성* 0건** (본 brief = 가능성 *검토* 한정 — 실 파일 작성 = 별도 단계)
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건** (R-4.1 Tier-1 45 patterns 답습)
- ❌ **ADR 본문 자동 갱신 0건** (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
- ❌ **ADR-012 §2.2 enum 정식 등록 0건** (`pre_commit_config_local_definition` 가칭 = candidate-only — Backlog #5 별도 합의 영역)
- ❌ **다른 backlog (#3/#4/#7) 자동 진입 0건** (Backlog #2 = 본 brief 의 *공유 처리* 영역, 자동 진입 0건)
- ❌ **Backlog #2 단독 진입 합의 발효 0건** (PC-4 공유 영역 답습 한정 — Backlog #2 GP-5 1.5차 단독 합의 = 별도 영역)
- ❌ **합의 보고서 작성 0건** (본 brief = 준비안 한정)
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건** (별도 commit 분리)
- ❌ **git commit / push 0건** (본 brief 파일화 + commit = 사용자 명시 후속)
- ❌ **외부 LLM 자동 호출 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**

### 0.5 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 본 brief 의 어떤 §도:

- (i) §C-5c Satisfied / 부분 Satisfied *갱신 발효* 를 발생시키지 않으며,
- (ii) MVP-1 PASS *재선언* / Layer D 본문 변경 / Layer E / Layer F 격상을 발생시키지 않으며,
- (iii) PC-4 T3 sub-영역 (dev 환경 강제 / `pre-commit install` 의무화 / branch protection) 진입을 *허용* 하지 않으며,
- (iv) §5.5 9 sub-수단 본문 채택 + C-1~C-8 상태를 *변경* 하지 않으며,
- (v) `.pre-commit-config.yaml` 실 본문을 *작성* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **§C-5c PC-4 의 T2 sub-영역 (`.pre-commit-config.yaml` config 정의 가능성) 한정 검토 + Backlog #1 + #2 공유 처리 옵션 권고 + 합의 형태 권고**. 모든 *진입 결정* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습 (§C-5a Satisfied 갱신 후 상태)

### 1.1 §C-5 sub-condition 매트릭스 답습 (`6fa87dc` 직후 시점)

| Sub-condition | 항목 | 영역 | 상태 | 본 brief 관계 |
|--------------|------|------|------|------------|
| **C-5a** | ST-2 (inotify sidecar) | GP-3 저장 경로 isolation 보강 (T2) | ✅ **Satisfied** (`6fa87dc`) | 답습 한정 |
| **C-5b** | ST-1 (Hermes Dockerfile entrypoint stat) | GP-3 저장 경로 isolation 보강 (T3) | ⏳ **Deferred** (Backlog #3 T3 영역) | 답습 한정 — 본 brief 영역 외 |
| **C-5c** | PC-4 (local pre-commit framework) | GP-3 + GP-5 공유 pre-commit hook 보강 (T2 + T3 혼합) | ⏳ **Deferred** (Backlog #1 + #2 공유) | **본 brief = T2 sub-영역 한정 검토** |
| **C-5 전체** | (3 sub-condition 합산) | — | ⏳ **Partially Satisfied (C-5a only)** | 답습 한정 — 본 brief 영역 외 |

### 1.2 본 brief 의 진입점 = §C-5a Satisfied 갱신 후 → §C-5c T2 sub-영역 *분석*

```
Layer D APPROVE (210c98f) — MVP-1 PASS (APPROVE WITH CONDITIONS)
   │
   ▼
§C-1 Satisfied (1dd1036) → ST-2 단독 합의 (0e99a56) → ST-2 실 구현 합의 (6c616a8)
   │
   ▼
ST-2 Cycle 1~6 완료 → §C-5a Satisfied 갱신 합의 (6fa87dc)
   │
   ▼ (C-5a 단독 갱신, C-5b·C-5c Deferred 보존)
§C-5 = Partially Satisfied (C-5a only) — C-5b/C-5c 보존
   │
   ▼ (사용자 명시 진입 명령)
■ 본 brief = §C-5c PC-4 T2 sub-영역 (`.pre-commit-config.yaml` config 정의 가능성) 한정 검토 *준비안* (DRAFT)        ← 현 위치
   │
   ▼ (사용자 명시 승인 후)
brief 그대로 승인 합의 보고서 작성 또는 일부 조정 또는 보류
   │
   ▼ (사용자 명시 결정 후, T2 sub 진입 결정 시)
■ §C-5c PC-4 T2 sub 진입 합의 — 단독 진입 / Backlog #2 통합 진입 / 보류 中 결정         ← 본 brief 영역 외
   │
   ▼ (T2 sub 진입 결정 후, `.pre-commit-config.yaml` 실 본문 작성)
실 구현 진입 (Cycle 1~N + actual run + evidence)                     ← 본 brief 영역 외
   │
   ▼ (구현 + actual run SUCCESS + evidence 후)
§C-5c 부분 Satisfied 갱신 합의 (T2 sub 한정 — T3 sub 보존)         ← 본 brief 영역 외
```

### 1.3 PC-4 T2/T3 sub-영역 분류 답습 (deepening brief §2.3.3 답습)

| sub-영역 | 분류 | 본 brief 처리 | 사유 |
|---------|------|------------|------|
| **`.pre-commit-config.yaml` 본문 정의** | **T2** (정책 영역, ADR-011 §2.4 답습) | ✅ **본 brief 영역** | 사용자 명시 1 (PC-4 T2 sub 한정 검토) |
| `pre-commit install` 의무 명시 (dev 환경 강제) | T3 (dev 환경 정책 강제) | ❌ 본 brief 영역 외 | 사용자 명시 6 금지 中 (1) dev 환경 강제 + (2) `pre-commit install` 의무화 |
| PC-3 부분 답습 (CI step fail-closed) | T2 (이미 본문 채택, `55c5b4b` 답습) | 답습 한정 (변경 0건) | §5.5 9 sub-수단 본문 채택 변경 0건 답습 |
| branch protection rule 변경 (AR-2) | T3 (repo policy 수준) | ❌ 본 brief 영역 외 | 사용자 명시 6 금지 中 (3) branch protection |

---

## 2. PC-4 T2 sub-영역 정의 (본 brief 한정 범위)

### 2.1 T2 sub-영역 정의

본 brief 가 *분석 범위* 안에 두는 PC-4 의 *유일한* 영역:

```
PC-4 T2 sub-영역
   = repo-local `.pre-commit-config.yaml` 파일의 *본문 정의 가능성*
   = hook 명세 (어떤 hook 이름 / 어떤 entry / 어떤 file pattern / 어떤 stage) 의 *후보 정의* 검토
```

본 brief *분석 범위 외*:

```
PC-4 T3 sub-영역 (본 brief 영역 외 — 사용자 명시 6 금지)
   = `pre-commit install` *의무화* (dev 환경 강제)
   = `.pre-commit-config.yaml` 변경 시 모든 dev *재install* 의무
   = CI 가 dev install 여부를 *검증* 하는 step 추가 (간접 강제)
   = branch protection 통한 commit signing / required check 추가 (AR-2)
```

### 2.2 T2 sub-영역의 *본질*

T2 sub = **hook 명세 정의** 한정 — 그 자체로:

- **dev 환경 강제 효과 0** — `.pre-commit-config.yaml` 파일이 repo 에 존재해도, `pre-commit install` 명시 의무가 없으면 dev 환경에서 자동 hook 동작 0건
- **CI gating 효과 0 (간접 답습 한정)** — 본 T2 sub 는 PC-3 (CI-only enforcement) 답습 위에서 *추가* 정의 한정 — `.pre-commit-config.yaml` 의 hook 정의가 CI workflow 의 별도 step 으로 reuse 될 수 있음 (CI 만 enforce)
- **opt-in 한정** — 개발자가 *자발적으로* `pre-commit install` 실행 시 한정 hook 동작 (본 brief 는 그 가능성 자체를 권고 0건 — 단순 정의 가능성 분석 한정)

### 2.3 T2 sub-영역의 *권위 출처*

| 권위 | 답습 출처 |
|------|---------|
| `.pre-commit-config.yaml` 본문 정의 = T2 정책 영역 | deepening brief §2.3.3 답습 |
| T2 영역 = 단축 합의 적격 (사용자 명시 결정) | ADR-011 §2.4 + mvp1.md §4.7.3 답습 |
| PC-3 답습 위 추가 정의 = `55c5b4b` §5.5.1 + §5.5.2 본문 채택 답습 | Layer B 답습 |

---

## 3. `.pre-commit-config.yaml` config 정의 *가능성* 검토

### 3.1 기술적 가능성 분석

#### 3.1.1 `.pre-commit-config.yaml` 형식 답습

표준 [pre-commit framework](https://pre-commit.com) 의 config 형식:

```yaml
# (예시 — 본 brief = 후보 한정, 실 본문 작성 0건)
repos:
  - repo: local
    hooks:
      - id: <hook-id>
        name: <human-readable-name>
        entry: <command>
        language: <system|python|...>
        files: <pattern>
        stages: [pre-commit]
```

본 brief = config 형식 자체 = pre-commit 도구의 표준 사양 (외부 권위, 본 brief 권위 영역 외).

#### 3.1.2 본 repo 의 기존 자산 답습 (T2 sub config 정의 시 reuse 후보)

| 자산 | 경로 | T2 sub 활용 후보 |
|------|------|-------------|
| GP-3 secret scanner | `tools/secret_scanner.py` (Group D PoC 답습 + Layer B `55c5b4b` 본문 채택 S-1) | hook entry 후보 — 동일 도구가 CI 와 local 에서 동일하게 동작 가능 (`55c5b4b` 답습) |
| GP-5 import scanner | `tools/provider_import_scanner.py` (Group A 1차 답습) | hook entry 후보 — 동일 도구 |
| GP-5 URL/모델 scanner | `tools/provider_url_scanner.py` (Group A 3차 답습) | hook entry 후보 — 동일 도구 |
| GP-5 import-linter | `.importlinter` (Group A 2차 답습) | hook entry 후보 — `lint-imports` 명령 답습 |
| GP-3 docker secret inotify check | `tools/docker_secret_inotify_sidecar_check.sh` (Cycle 6 답습) | hook entry 후보 — file-pattern 한정 (sidecar 디렉토리 변경 시 한정 동작) |
| CI workflow step 답습 | `.github/workflows/secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` | local hook 명세가 CI step 명령과 *동등* 정의 가능 (이중 정의 회피 — 단일 source-of-truth 답습) |

→ **결론 (기술적 가능성)**: ✅ **`.pre-commit-config.yaml` config 정의 자체는 기술적으로 명확히 가능** — 기존 도구 모두 stateless · network-free · CLI-callable 답습 (Group D / Group A 1·2·3차 PoC 답습) → hook entry 로 직접 reuse 적격.

#### 3.1.3 hook 카탈로그 *후보* (사용자 결정 영역, 본 brief = enumerate 한정)

본 brief = 후보 enumerate 한정 — 채택 *결정* 0건. 다음은 후보 카탈로그 (T2 sub 진입 시 합의 영역):

| # | hook id 후보 | 도구 답습 | files 패턴 후보 | 본 brief 권고 |
|---|----------|---------|------------|----------|
| 1 | `secret-scanner` | `tools/secret_scanner.py` | `\.(py|js|ts|md|yml|yaml|sh|toml)$` (Tier-1 45 patterns 답습 한정) | T2 sub 채택 시 *우선 후보* (S-1 본문 채택 답습) |
| 2 | `provider-import-scanner` | `tools/provider_import_scanner.py` | `^src/.*\.py$` | T2 sub 채택 시 *우선 후보* (Group A 1차 답습) |
| 3 | `provider-url-scanner` | `tools/provider_url_scanner.py` | `^src/.*\.py$` | T2 sub 채택 시 *우선 후보* (Group A 3차 답습) |
| 4 | `import-linter` | `lint-imports` (T-2 답습) | `^src/.*\.py$` | T2 sub 채택 시 *우선 후보* (Group A 2차 답습) |
| 5 | `secret-inotify-sidecar-check` | `tools/docker_secret_inotify_sidecar_check.sh` | `^docker/gp3-st2-poc/.*` (격리 PoC 영역 한정) | T2 sub 채택 시 *후보 한정* (Cycle 6 답습 — local 실행 의미 약함, CI 의존도 高) |

**합산 = 5 hook 후보** (GP-3 1 + GP-5 3 + GP-3/ST-2 1). 본 카탈로그 = *가능성 enumerate 한정*. 실 채택 = T2 sub 진입 합의 영역.

#### 3.1.4 정의 *불가능* 한 영역 (본 brief 명시)

| 영역 | 사유 |
|------|------|
| `pre-commit install` 자동 실행 | dev 환경 강제 — 사용자 명시 1 + 2 금지 |
| 모든 dev 환경에서 hook 자동 실행 보장 | dev 환경 강제 — 사용자 명시 1 금지 |
| commit signing 강제 (commit-msg stage hook 등 통한 간접 강제) | branch protection / signing 영역 — 사용자 명시 3 + 4 금지 |
| dev 환경 install 비율 측정 hook (CI 가 dev install 여부 검증) | dev 환경 강제 *간접* — 사용자 명시 1 금지 |
| Hermes upstream Dockerfile 변경 통한 hook 사전 install | T3 영역 + Hermes upstream 변경 — 사용자 명시 4 + 6 금지 |

### 3.2 Backlog #1 + #2 공유 처리 옵션 (T2 sub 한정)

#### 3.2.1 PC-4 의 *공유* 본질 답습

mvp1.md §4.3.1 답습 — PC-4 = GP-3 + GP-5 양쪽 pre-commit hook 통합 영역 (G3-2 부분 + G5-2 부분 공유). 따라서 `.pre-commit-config.yaml` 1 파일 = GP-3 hook + GP-5 hook 합산 정의 가능 (단일 file 통합).

#### 3.2.2 처리 옵션 매트릭스 (T2 sub 한정)

| 옵션 | 처리 형태 | 장점 | 단점 | 본 brief 권고 |
|-----|---------|------|------|----------|
| **(α) Backlog #1 단독 진입 (GP-3 hook 만 정의)** | `.pre-commit-config.yaml` 에 GP-3 hook (#1 / #5) 만 본문 정의 → Backlog #2 별도 진입 시 GP-5 hook (#2/#3/#4) 추가 | 단계적 진입 + Backlog #2 합의와 *시간적 분리* | 1 파일 2 회 변경 (변경 ledger 분산) | ⚠️ 부분 권고 (T2 sub 단독 진입 의도 보존) |
| **(β) Backlog #1 + #2 통합 진입 (GP-3 + GP-5 hook 합산 정의)** | `.pre-commit-config.yaml` 에 5 hook 후보 모두 본문 정의 (단일 합의) | 1 파일 1 회 변경 (단일 source-of-truth) + 합의 효율 | Backlog #2 합의 시점 *동시* 의무 (Backlog #2 단독 합의 권위 결합) | ⚠️ 부분 권고 (효율 高, 합의 형태 결합 의무) |
| **(γ) PC-4 T2 sub 보류** | 본 brief 후속 합의 0건 | C-5c Deferred 그대로 유지 | T2 sub 가능성 정비 결과 사용 0건 | ⚠️ 부분 권고 (다른 backlog 우선 시) |

#### 3.2.3 본 brief 권고 (수단 *결정 아님* — 옵션 enumerate 한정)

본 brief = T2 sub *가능성* 한정 검토. 옵션 (α) / (β) / (γ) 中 결정 = 사용자 명시 결정 영역.

- **(α) 권고 사유**: Backlog #1 진입 의도 보존 + 사용자 명시 진입 명령 답습 (Backlog #1 + #2 *공유 영역* 명시 = 양쪽 영향 인지 답습)
- **(β) 권고 사유**: 1 파일 본질 답습 + 변경 ledger 단일화 + 합의 효율
- **(γ) 권고 사유**: 다른 backlog 우선 (예: MVP-2 진입 / Backlog #2 단독 / Backlog #3 T3 등)

### 3.3 T2 sub 단독 진입 시 *영역 한계* 명시

본 brief 가 분석한 T2 sub 단독 진입 = *최소* 효과 영역:

| 효과 | 결과 |
|------|------|
| `.pre-commit-config.yaml` 파일 repo 추가 | ✅ 가능 |
| dev 환경 *opt-in* 사용 가능성 (개발자 자발적 `pre-commit install`) | ✅ 가능 (의무화 0건) |
| **dev 환경 강제 효과** | ❌ **0건** (사용자 명시 1 금지 답습) |
| **CI gating 강화 효과** | ❌ **0건** (PC-3 답습 그대로 — CI workflow step 이 enforce, hook 정의는 reuse-only) |
| Hermes upstream 변경 | ❌ 0건 (T2 영역) |
| ADR 본문 변경 | ❌ 0건 (cross-reference 답습 한정) |
| §5.5 9 sub-수단 본문 채택 변경 | ❌ 0건 (PC-3 본문 채택 유지) |

→ **T2 sub 단독 진입 = repo-local config 파일 *추가* 한정** — Defense in depth 효과 = opt-in 한정 (dev 환경 강제 0건 답습). *충분한* defense in depth 효과 (= 모든 dev 환경 강제) = T3 sub 진입 의무 (본 brief 영역 외).

### 3.4 본 §3 의 *범위 한계*

본 §3 = *T2 sub config 정의 가능성 분석 한정*. 다음은 본 §3 영역 외:

- ❌ T2 sub *진입 결정* (옵션 α / β / γ 결정)
- ❌ hook 카탈로그 *최종 결정* (5 후보 中 어느 hook 채택?)
- ❌ T3 sub 영역 (`pre-commit install` / dev 환경 강제 / branch protection) 권고
- ❌ Backlog #2 단독 진입 합의 (Backlog #2 GP-5 1.5차 영역 = 별도 brief)
- ❌ §C-5c 갱신 형태 (T2 sub 한정 부분 Satisfied? — T2 sub *발효 후* 별도 합의 영역)

---

## 4. 합의 형태 권고 + 풀 3+1 승격 트리거 검증

### 4.1 본 brief 자체의 합의 형태

| 영역 | 합의 형태 권고 | 사유 |
|------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 (`backlog1-st2-c5a-satisfaction-brief.md` §0.4 패턴 답습) |
| brief 승인 후 후속 합의 (T2 sub 진입 결정 시) | **사용자 명시 결정 영역** | 옵션별 합의 형태 분리 (§4.2 답습) |

### 4.2 옵션별 합의 형태 권고 (T2 sub 진입 시점)

| 옵션 | 합의 형태 권고 | 사유 | 답습 출처 |
|------|----------|------|---------|
| (α) Backlog #1 단독 진입 (GP-3 hook 한정) | **단축 합의 + 사용자 명시 결정** | T2 정책 영역 한정 + Backlog #1 deepening brief §2.3.4 권고 답습 | mvp1.md §4.7.3 + ADR-011 §2.4 답습 |
| (β) Backlog #1 + #2 통합 진입 (GP-3 + GP-5 hook 합산) | **단축 합의 + 사용자 명시 결정** (단, Backlog #2 영역 영향 인지 의무 명시) | T2 정책 영역 한정 + 양 GP 일관성 답습 (`55c5b4b` PC-3 양 GP 일관 채택 답습) | mvp1.md §4.7.3 + 양 GP 일관 답습 |
| (γ) 보류 | (합의 0건) | 보류 = 사용자 명시 결정 영역 | — |

### 4.3 풀 3+1 승격 트리거 검증 (7 트리거 답습 — 0/7 발화 권고)

본 brief 가 풀 3+1 합의로 *승격* 되어야 할 trigger 후보 (deepening brief §3.3 + c5a brief §7.2 답습):

| # | 트리거 | 본 brief 검토 결과 |
|---|----|------------|
| 1 | 본 brief 가 9 sub-수단 *외* 수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — 본 brief = PC-4 T2 sub *가능성 분석* 한정 (PC-3 본문 채택 답습 변경 0건) |
| 2 | 본 brief 가 T3 영역 (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제) 자동 진입을 권고하는 경우 | ❌ 0건 발화 — 본 brief = 사용자 명시 6 금지 답습, T3 영역 권고 0건 |
| 3 | 본 brief 가 §5.5 9 sub-수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — PC-3 본문 채택 유지 (`55c5b4b` 답습) |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | ❌ 0건 발화 — pre-commit framework 영역, Provider Liquidity 영향 0건 |
| 5 | 본 brief 가 5 영구 핵심 제약 약화를 포함하는 경우 | ❌ 0건 발화 — Hermes ≠ root of trust 보존 + T3 분리 보존 + 수단/목적 분리 보존 + 메타포 강제 금지 보존 + Provider Liquidity 보존 |
| 6 | 본 brief 가 MVP-1 PASS *재선언* / Layer E / Layer F 격상을 포함하는 경우 | ❌ 0건 발화 — 사용자 명시 5 + 6 금지 답습 |
| 7 | 본 brief 가 외부 LLM cross-vendor blind 의뢰 *없이* T3 영역 결정을 권고하는 경우 | ❌ 0건 발화 — T3 영역 권고 0건 |

**본 brief 검토 결과 = 7/7 트리거 0건 발화** → 본 brief 승인 후 후속 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 4.4 본 §4 의 *범위 한계*

본 §4 = *합의 형태 권고 한정*. 실 합의 형태 결정 + 옵션 결정 = 사용자 명시 결정 영역.

---

## 5. Rollback Trigger / Evidence 기준 (T2 sub 발효 시점 의무 — 본 brief 영역 외)

### 5.1 본 §5 의 *명확한 한계*

본 §5 = **T2 sub *발효 시점* 의무 정리 한정**. 본 brief 자체 시점에서:

- ❌ 실 `.pre-commit-config.yaml` *본문 작성* 0건
- ❌ 실 hook actual run 0건
- ❌ commit_block_rate / hook_runtime threshold *고정* 0건 (모두 *후보 한정* 유지)
- ❌ 실 evidence artifact 생성 0건
- ❌ event enum 정식 등록 0건 (`pre_commit_config_local_definition` 가칭 = candidate-only)

### 5.2 PC-4 T2 sub 별 Rollback Trigger 답습 (mvp1.md §4.6 + deepening brief §4.2 답습)

| Trigger ID | 발화 조건 (T2 sub 한정) | 발화 시 행동 | 본 brief 발효 시점 행동 |
|----------|----------------------|-------------|------------------|
| R-MVP1-G3-4 | PC-3 부분 CI runtime 폭증 (>2분) — pre-commit hook 정의가 CI step 과 *불일치* 시 발화 | threshold 재결정 합의 (단축 적격) | (현 brief = 미발화 — Stage 4 PC-3 SUCCESS 답습) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | T3 영역 → 풀 3+1 합의 + branch protection rule 변경 검토 (Backlog #3) | (현 brief = 미발화 — 본 brief = T2 sub 한정, AR-2 영역 외) |
| R-MVP1-G5-6 | T-9 (pre-commit hook PC-1) 도입 별도 합의 (Group A 2차 §8 TR-5 답습) | 본 PoC 와의 책무 분리 재합의 | (현 brief = 사용자 명시 답습 — T2 sub 단독 분석 한정) |
| **(신규 후보) R-MVP1-G3-PC4-T2** | `.pre-commit-config.yaml` 본문 정의 후 dev 환경 *간접 강제* 시도 검출 (예: 외부 LLM 권고 통한 install 의무화 압박) | T3 영역 부분 진입 거부 + 본 brief §0.3 답습 (사용자 명시 1 금지) | (현 brief = 미발화 — T2 sub 한정 분석) |
| **(신규 후보) R-MVP1-G3-PC4-T3** | `.pre-commit-config.yaml` 본문 + dev 환경 강제 진입 결정 | T3 영역 → 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 (Backlog #3 영역과 부분 중첩) | (현 brief = 미발화 — T3 영역 권고 0건) |

### 5.3 Evidence 기준 답습 (mvp1.md §3.6.1 + ADR-011 §2.1 (a)~(e) 답습)

T2 sub *발효 시점* 의무 evidence (본 brief 영역 외):

| Evidence | 형식 | T2 sub 적용 한정 |
|----------|------|--------------|
| (a) 동등 이상의 보안 결과 | `.pre-commit-config.yaml` 본문 정의가 PC-3 답습 (CI gating) 위에서 opt-in defense in depth *추가* 가능성 명시 (강제 효과 0건 명시) | ✅ T2 sub 발효 시 |
| (b) 격리 환경 PoC 실증 | local repo 격리 환경에서 `.pre-commit-config.yaml` 본문 정의 + opt-in 시 hook 동작 시연 (강제 환경 시연 0건) | ✅ T2 sub 발효 시 (opt-in 한정 시연) |
| (c) ADR / SDD 권위 명시 | mvp1.md §4.3 + §5.5.1 / §5.5.2 + ADR-011 §2.4 + 본 brief 답습 | ✅ T2 sub 발효 시 |
| (d) 자동 회귀 검증 경로 확보 | `.pre-commit-config.yaml` schema 검증 (CI step 통한 yaml syntax + hook id 중복 검출) — 본문 *opt-in* 답습 한정 | ✅ T2 sub 발효 시 (강제 install 검증 0건) |
| (e) 합의 APPROVE | 옵션 (α) / (β) 中 사용자 명시 결정 + 단축 합의 | T2 sub 발효 시 (본 brief 영역 외) |

### 5.4 JSONL Ledger entry 형식 후보 (Backlog #5 답습 — `b705370`)

T2 sub 발효 시점 evidence ledger entry *후보* (Backlog #5 ADR-012 §2.2 정식 등록 8 enum 답습 + 추가 후보):

| event enum (후보) | trigger | T1/T2/T3 | Backlog #5 등록 상태 |
|------------------|---------|---------|------------------|
| `pre_commit_config_local_definition` (가칭 — T2 sub 한정) | `.pre-commit-config.yaml` 본문 정의 발효 시 | T2 한정 | ❌ 미등록 (Backlog #5 추가 등록 별도 합의 영역) |

본 enum 후보 = **본 brief 권고 한정** — 정식 등록 = Backlog #5 ADR-012 §2.2 schema 갱신 별도 합의 영역 (`b705370` 답습 후속 추가 등록 영역).

### 5.5 본 §5 의 *범위 한계*

본 §5 = **T2 sub *발효 시점* 의무 정리 한정**. 다음은 본 §5 영역 외:

- ❌ 실 rollback fixture 생성 (T2 sub *발효 시점* 별도 작업)
- ❌ 실 trigger 발화 시연 (동상)
- ❌ Trigger threshold 정량 *고정* (commit_block_rate / hook_runtime 등 모두 *후보 한정* 유지)
- ❌ 실 evidence artifact 생성 (동상)
- ❌ 신규 event enum 정식 등록 (Backlog #5 별도 합의 영역)
- ❌ T3 sub-영역 (dev 환경 강제) 의 evidence / trigger / threshold 정리 (사용자 명시 6 금지)

---

## 6. 금지 사항

### 6.1 본 brief 자체 금지 사항 (사용자 명시 6 + 추가 답습)

| # | 금지 영역 | 본 brief 위반 | 답습 출처 |
|---|---------|------------|---------|
| 1 | **dev 환경 강제** (모든 dev 환경에 hook 강제 동작 권고) | 0건 | 사용자 명시 1 |
| 2 | **`pre-commit install` 의무화** (dev 환경 install 강제 권고) | 0건 | 사용자 명시 2 |
| 3 | **branch protection 변경** (AR-2 / AR-3 / GitHub repo policy 변경 검토) | 0건 | 사용자 명시 3 |
| 4 | **T3 영역 진입** (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 정책) | 0건 | 사용자 명시 4 |
| 5 | **Operational Readiness PASS (Layer E) 선언** | 0건 | 사용자 명시 5 |
| 6 | **Hermes PMO 격상 (Layer F)** | 0건 | 사용자 명시 6 |
| 7 | §C-5c Satisfied / 부분 Satisfied *갱신 발효* | 0건 | 본 brief = 준비안 한정 |
| 8 | §C-5 전체 표기 갱신 (`Partially Satisfied (C-5a only)` 변경) | 0건 | `6fa87dc` 답습 |
| 9 | MVP-1 PASS *재선언* (Layer D `210c98f` 본문 변경) | 0건 | 답습 |
| 10 | Backlog #1 / #2 진입 합의 발효 | 0건 | 본 brief = 가능성 분석 한정 |
| 11 | PC-4 *수단 결정* (PC-1 ~ PC-4 채택 변경) | 0건 | 본 brief = 가능성 분석 한정 |
| 12 | §5.5 9 sub-수단 본문 채택 *변경* (PC-3 본문 채택 유지) | 0건 | `f40423f` + `55c5b4b` 답습 |
| 13 | threshold *고정* (commit_block_rate / dev_env_install_rate / hook_runtime) | 0건 | 답습 |
| 14 | 실 `.pre-commit-config.yaml` *본문 작성* | 0건 | 본 brief = 가능성 검토 한정 |
| 15 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 | R-4.1 Tier-1 답습 |
| 16 | ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경) | 0건 | cross-reference 답습 한정 |
| 17 | ADR-012 §2.2 enum 정식 등록 (`pre_commit_config_local_definition` 가칭) | 0건 | candidate-only 유지 — Backlog #5 별도 |
| 18 | 다른 backlog (#3/#4/#7) 자동 진입 | 0건 | 답습 |
| 19 | Backlog #2 단독 진입 합의 발효 | 0건 | 공유 영역 답습 한정 |
| 20 | C-2 / C-3 / C-4 / C-5a / C-5b / C-6 / C-7 / C-8 자동 변경 | 0건 | C-5c T2 sub 한정 분석 |
| 21 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 | 답습 |
| 22 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 | 별도 commit 분리 |
| 23 | git commit / push (본 brief 파일화 + commit = 사용자 명시 후속) | 0건 | 답습 |
| 24 | 외부 LLM 자동 호출 | 0건 | 답습 |
| 25 | 실 API key / provider SDK / 외부 API 호출 | 0건 | 영구 금지 답습 |
| 26 | Provider Liquidity 5-way / 5 영구 핵심 제약 약화 | 0건 | 답습 |

### 6.2 본 brief 발효 *후* T2 sub 진입 단계 금지 사항 (진입 시 의무 답습)

본 §6.2 는 사용자 명시 6 금지 답습 한정 — T2 sub 진입 *결정 후* 단계에서도 위반 0건 의무:

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | dev 환경 강제 (`pre-commit install` 의무화 / 모든 dev 환경 hook 강제) | 사용자 명시 1 + 2 답습 |
| 2 | branch protection rule 변경 (AR-2 진입) | 사용자 명시 3 답습 (Backlog #3 T3 영역) |
| 3 | T3 영역 자동 진입 (Hermes upstream / Vault HSM / Tier-2-3 catalog / dev 환경 강제) | 사용자 명시 4 답습 |
| 4 | Operational Readiness PASS / Hermes PMO 격상 | 사용자 명시 5 + 6 답습 |
| 5 | hook entry 통한 *간접* dev 환경 강제 (예: CI 가 dev install 검증 step 추가) | 사용자 명시 1 답습 (간접 강제 회피) |
| 6 | commit signing / commit-msg stage hook 통한 간접 강제 | 사용자 명시 3 답습 (branch protection 영역) |
| 7 | Hermes upstream Dockerfile 변경 통한 hook 사전 install | 사용자 명시 4 답습 (T3 영역) |
| 8 | 실 secret 본문 commit | R-4.1 + Group D §1.2 #1 답습 (영구 금지) |
| 9 | F-금지 위반 (workflow 본문 secret 토큰 사용 등) | G3-7 (i) 답습 (영구 금지) |
| 10 | 외부 LLM 자동 호출 | 사용자 명시 결정 없이 외부 LLM 호출 0건 답습 |

본 §6 = **사용자 명시 6 금지 + 영구 답습 한정** — 본 brief 발효 후 T2 sub 진입 단계에서 위 10 금지 영역 위반 0건 유지 의무.

---

## 7. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성** (PC-4 T2 sub 가능성 검토 결과 권위 source — T2 sub *진입* 은 별도 합의) | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-14-c5c-pc4-t2-sub-review.md` 가칭) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 그대로 승인 → 후속 합의 보류 → 옵션 (α) Backlog #1 단독 진입 합의 brief 작성 (T2 sub *진입* 합의 준비) | T2 sub 진입 합의 brief 작성 |
| (D) | 본 brief 그대로 승인 → 후속 합의 보류 → 옵션 (β) Backlog #1 + #2 통합 진입 합의 brief 작성 | 통합 진입 합의 brief 작성 |
| (E) | 본 brief 그대로 승인 → 후속 합의 보류 → 옵션 (γ) PC-4 T2 sub 보류 → 다른 backlog 우선 (예: MVP-2 / Backlog #2 / Backlog #3) | 우선 backlog 결정 |
| (F) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 7.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A)로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B)로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C)로 진행해주세요. 옵션 (α) Backlog #1 단독 진입 합의 brief 작성으로 진입합니다."
- (D): "옵션 (D)로 진행해주세요. 옵션 (β) Backlog #1 + #2 통합 진입 합의 brief 작성으로 진입합니다."
- (E): "옵션 (E)로 진행해주세요. 우선 backlog (예: MVP-2 / Backlog #2 / Backlog #3) 결정으로 전환합니다."
- (F): "옵션 (F)로 진행해주세요. 세션 종료."

### 7.2 본 §7 의 *범위 한계*

본 §7 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 8. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 (3 영역: 범위 = PC-4 T2 sub / `.pre-commit-config.yaml` config 정의 가능성 검토 / 6 금지) | ✅ (3/3) |
| 사용자 명시 6 금지 답습 (dev 환경 강제 / `pre-commit install` 의무화 / branch protection / T3 영역 / Operational Readiness PASS / Hermes PMO 격상) | ✅ (6/6) |
| §C-5 sub-condition 답습 (C-5a Satisfied / C-5b Deferred / C-5c Deferred / 전체 Partially Satisfied) | ✅ (변경 0건 — `6fa87dc` 답습) |
| §5.5 9 sub-수단 본문 채택 답습 | ✅ (변경 0건 — PC-3 본문 채택 유지) |
| C-1~C-8 상태 답습 | ✅ (변경 0건) |
| MVP-1 PASS Layer D 본문 답습 | ✅ (`210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ (T2 sub 한정 + T3 sub 자동 진입 0건 명시) |
| 5 영구 핵심 제약 보존 | ✅ (Provider Liquidity 5-way / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 모두 답습) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #2 = 공유 영역 답습 한정 / #3/#4/#7 분리 명시 — 자동 진입 0건) |
| 풀 3+1 승격 트리거 0/7 발화 | ✅ (§4.3 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| 합의 보고서 0건 / commit 0건 / push 0건 | ✅ (본 brief = 준비안 한정) |
| 실 `.pre-commit-config.yaml` 본문 작성 0건 | ✅ (가능성 *검토* 한정) |
| 실 hook actual run 0건 | ✅ |
| ADR-012 §2.2 enum 정식 등록 0건 (candidate-only 유지) | ✅ |

---

## 9. 본 brief 요약 (한 단락)

본 brief 는 **§C-5a Satisfied 갱신 (`6fa87dc`) 발효 후속, §C-5c (PC-4 local pre-commit framework) 中 T2 sub-영역 (`.pre-commit-config.yaml` config 정의 가능성) 한정 검토 *준비안 (DRAFT)*** 이다. 사용자 명시 범위: PC-4 T2 sub 한정 (deepening brief §2.3.3 답습 — `.pre-commit-config.yaml` 본문 정의 = T2 정책 영역). 사용자 명시 6 금지 답습: dev 환경 강제 / `pre-commit install` 의무화 / branch protection / T3 영역 / Operational Readiness PASS / Hermes PMO 격상 모두 본 brief 영역 외. 기술적 가능성 = ✅ 명확 (기존 도구 모두 stateless · network-free · CLI-callable, hook entry 직접 reuse 적격) + 5 hook 후보 카탈로그 enumerate (GP-3 secret-scanner 1 / GP-5 import-scanner + URL-scanner + import-linter 3 / GP-3 ST-2 inotify 1). T2 sub 단독 진입 효과 = repo-local config 파일 *추가* + opt-in 한정 (dev 환경 강제 효과 0건 답습). Backlog #1 + #2 공유 처리 옵션 3개 enumerate (α 단독 / β 통합 / γ 보류) — 결정 = 사용자 명시 결정 영역. 합의 형태 권고 = **Reviewer-only 단축 합의 적격** (7/7 풀 3+1 트리거 0건 발화). T2 sub 발효 시점 의무 정리 (Rollback Trigger / Evidence) = 본 brief 영역 외 명시. **본 brief ≠ §C-5c 갱신 / Backlog #1 #2 진입 합의 / PC-4 수단 결정 / 실 `.pre-commit-config.yaml` 본문 작성 / dev 환경 강제 / T3 영역 진입 / MVP-1 PASS 재선언 / Layer E·F 격상 / 다른 backlog 자동 진입 / ADR 본문 자동 갱신** (사용자 명시 답습). 다음 단계 = 사용자 명시 결정 영역 (옵션 A~F, §7 답습).

---

**작성일**: 2026-05-14
**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~F, §7 답습)
**금지 (사용자 명시 6 + 추가 답습 — 본 brief 영역, 변동 없음)**:
- ❌ dev 환경 강제 (사용자 명시 1)
- ❌ `pre-commit install` 의무화 (사용자 명시 2)
- ❌ branch protection 변경 (사용자 명시 3)
- ❌ T3 영역 진입 (사용자 명시 4)
- ❌ Operational Readiness PASS (Layer E) 선언 (사용자 명시 5)
- ❌ Hermes PMO 격상 (Layer F) (사용자 명시 6)
- ❌ §C-5c Satisfied / 부분 Satisfied 갱신 발효
- ❌ §C-5 전체 표기 갱신 (`Partially Satisfied (C-5a only)` 변경)
- ❌ MVP-1 PASS *재선언*
- ❌ Backlog #1 / #2 진입 합의 발효
- ❌ PC-4 수단 결정 (PC-1 ~ PC-4 채택 변경)
- ❌ §5.5 9 sub-수단 본문 채택 변경 (PC-3 본문 채택 유지)
- ❌ threshold *고정*
- ❌ 실 `.pre-commit-config.yaml` 본문 작성
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ ADR 본문 자동 갱신
- ❌ ADR-012 §2.2 enum 정식 등록 (`pre_commit_config_local_definition` 가칭 = candidate-only)
- ❌ 다른 backlog (#3/#4/#7) 자동 진입
- ❌ Backlog #2 단독 진입 합의 발효
- ❌ C-2 / C-3 / C-4 / C-5a / C-5b / C-6 / C-7 / C-8 자동 변경
- ❌ 합의 보고서 작성
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
