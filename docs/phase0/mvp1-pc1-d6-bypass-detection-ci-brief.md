# MVP-1 PC-1-T3 D-6 bypass detection CI 통합 sub-cycle brief

> **scope**: 26번째 entry PC-1-T3 sub-cycle (`docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md` v1 + 합의 `docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md` APPROVE Reviewer-only) 의 **D-6 carry-over 집행 sub-cycle**. 본 sub-cycle = D-6 default 권고 (`(ii) 별도 sub-cycle`) 실 구현.
>
> **본 brief 자체에서 실 코드 변경 0건 의무** — brief 합의 발효 *후* 별도 실 구현 단계에서 file 생성.

---

## §0 답습 출처 (인용 source)

| Source | 위치 | 답습 내용 |
|---|---|---|
| **PC-1-T3 brief v1** | `docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md` (commit `3a63a5b`) | §4.5 bypass detection 메커니즘 `tools/pre_commit_install_audit.sh` + D-6 결정 항목 (`(i) PR step` vs `(ii) 별도 sub-cycle` vs `(iii) nightly schedule`) + R-6 BLOCKING 흡수 (탐지 경로 (ii) `pre-commit run --all-files` CI 비교) |
| **PC-1-T3 합의** | `docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md` (commit `3a63a5b`) | Reviewer-only APPROVE (5/5 풀 3+1 승격 trigger 0건) + D-6 default 권고 `(ii) 별도 sub-cycle` 답습 |
| **24번째 entry 합의** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | R-6 BLOCKING (PC1-1 탐지 경로 (i)/(ii)/(iii) 의무) + R-7(b) (PC1-2 차등 — version pin = 단축 합의 영역) |
| **AR-3 sub-cycle** | `docs/review/3plus1-consensus-2026-05-27-mvp1-ar3-pr-auto-reject.md` + 33번째 entry MVP-1 PASS evidence | 현 main branch protection contexts 7건 (`guard / verify / feasibility / scan / enforce / defense / validate`). 신규 contexts 추가 = AR-3 admin scope 영역 (사용자 영역) |
| **`tools/pre_commit_install_audit.sh`** | commit `3a63a5b` | (i) hook marker grep — local only (.git/hooks, repo 외) / (ii) `pre-commit run --all-files` CI 통합 자격 — **본 D-6 핵심** / (iii) setup audit log — local only (.git/pre-commit-audit, repo 외) |
| **ADR-011 §2.1** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 답습 (수단 *결정 발효 자격* — D-6 = PC-1-T3 결정 *집행* 보강) |

---

## §1 scope (D-6 sub-cycle 한정)

### 1.1 본 sub-cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | bypass detection CI 통합 실 구현 (PC-1-T3 D-6 carry-over 집행) |
| **선택된 통합 방향** | **(A) 신규 workflow** (사용자 명시 2026-05-27) |
| **신규 file** | `.github/workflows/pre-commit-bypass-detection.yml` (1건) |
| **합의 형태 권고** | **단축 합의 + 사용자 명시** (Reviewer-only, PC-1-T3 sub-cycle 답습) |
| **변경 0건 의무** | `tools/pre_commit_install_audit.sh` 본문 변경 0 / `.pre-commit-config.yaml` 본문 변경 0 / `.githooks/` 본문 변경 0 / 기존 11 workflow 본문 변경 0 / branch protection rule 0 (AR-3 영역, 본 sub-cycle 외) / src/ 0 / ADR 0 / 헌법 0 / roadmap 본문 0 |
| **변경 허용 영역** | `.github/workflows/pre-commit-bypass-detection.yml` 신규 1건 한정 |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 | 영역 |
|---|---|---|---|
| 1 | `tools/pre_commit_install_audit.sh` 본문 변경 | 0건 | PC-1-T3 sub-cycle 답습 유지 |
| 2 | `.pre-commit-config.yaml` 본문 변경 | 0건 | R-7(b) 차등 영역 |
| 3 | `.githooks/pre-commit` 본문 변경 | 0건 | Layer 3 답습 |
| 4 | 기존 11 workflow 본문 변경 | 0건 | (A) 신규 workflow 사용자 명시 영역 |
| 5 | branch protection rule contexts 추가 | 0건 | AR-3 admin scope, 사용자 영역 — **carry-over** |
| 6 | Tier-2/3 catalog 확장 | 0건 | 별도 cycle |
| 7 | ADR / 헌법 / roadmap 본문 변경 | 0건 | R-MVP1-PASS-{1~10} 답습 |
| 8 | MVP-1 Implementation Evidence PASS 재선언 | 0건 | 33번째 entry 발효 답습 |
| 9 | `adapters/llm/facade.py` placeholder → real | 0건 | (d) carry-over 영역 |

---

## §2 R-6 BLOCKING 흡수 매트릭스 (24번째 entry + PC-1-T3 sub-cycle)

| ID | 항목 | 본 brief 흡수 위치 |
|---|---|---|
| **R-6** BLOCKING (24번째 entry) | R-MVP1-1.5-PC1-1 탐지 경로 (i) hook marker grep / (ii) `pre-commit run --all-files` 결과 CI 비교 / (iii) setup audit log | §4 step 설계 — (ii) CI 측 `pre-commit run --all-files` 실행 + violation 검출 |
| **D-6** carry-over (PC-1-T3 brief) | (i) PR step / (ii) **별도 sub-cycle** / (iii) nightly schedule | 본 sub-cycle = (ii) 집행. trigger = PR + push + nightly (3 모두 포함, (i)+(iii) 효과 동시 발효) |
| **PC1-2 차등** R-7(b) (24번째 entry) | 신규 hook = 풀 3+1 / version pin = 단축 합의 | 본 sub-cycle = `.pre-commit-config.yaml` 본문 변경 0 → 단축 합의 답습 |

### 2.1 (i) + (iii) 효과 동시 발효 명문

`tools/pre_commit_install_audit.sh` (i)/(iii) 탐지 경로는 `.git/hooks` + `.git/pre-commit-audit` 모두 **local-only repo 외** 영역이므로 CI 측 직접 검증 불가능. 본 D-6 신규 workflow = **(ii) `pre-commit run --all-files` CI 실행**으로 한정. 단, (ii) 결과 = dev 환경 hook 실행 결과의 *집계 검증*이므로 (i)/(iii) 우회 시도가 있었더라도 검출 가능 (hook bypass commit → CI에서 `pre-commit run --all-files` FAIL → bypass 의심).

---

## §3 ADR-011 §2.1 (a)~(e) 매트릭스 (PC-1-T3 cell 보강)

| 조건 | PC-1-T3 현 상태 (26번째 entry) | 본 D-6 sub-cycle 발효 후 |
|---|---|---|
| (a) 비-Hermes 진입 자격 | ✅ (PC-1-T3 dev 환경 정책, Hermes ≠) | ✅ 답습 유지 |
| (b)(d) PoC 충족 | ✅ (PC-1-T3 brief §4 5 file 실 구현 발효) | ✅ + bypass detection CI 자동화 강화 (PoC 회귀 자격 보강) |
| (c) 권한 격리 | ✅ (dev 환경 한정, prod 영향 0) | ✅ 답습 유지 |
| (e) 운영조건 PASS | ✅ (PC-1-T3 합의 APPROVE 발효) | ✅ + D-6 carry-over 해소 |

**본 D-6 sub-cycle = PC-1-T3 (b)(d) PoC 회귀 자격 보강 한정**. (a)/(c)/(e) 변경 0건.

---

## §4 실 구현 1 항목 (file 신규)

### 4.1 `.github/workflows/pre-commit-bypass-detection.yml` (신규)

```yaml
name: PC-1-T3 bypass detection

on:
  push:
    branches:
      - main
      - develop
      - "feature/**"
    paths:
      - ".pre-commit-config.yaml"
      - ".github/workflows/pre-commit-bypass-detection.yml"
      - "tools/pre_commit_install_audit.sh"
      - "**/*.py"
      - "**/*.yaml"
      - "**/*.yml"
      - "**/*.md"
  pull_request:
    branches:
      - main
      - develop
  schedule:
    - cron: "0 3 * * *"  # 매일 KST 12:00 (UTC 03:00) nightly
  workflow_dispatch:

jobs:
  bypass-detect:
    name: bypass-detect
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install pre-commit
        run: |
          python -m pip install --upgrade pip
          pip install pre-commit==4.0.1

      - name: Run pre-commit on all files (bypass detection)
        run: |
          # PC-1-T3 D-6 (ii): pre-commit run --all-files CI 실행
          # dev 환경 hook bypass 시 본 step 에서 violation 검출
          # FAIL 시 → R-MVP1-1.5-PC1-1 발화 자격
          pre-commit run --all-files --show-diff-on-failure
```

### 4.2 설계 결정 사항

| 항목 | 결정 | 근거 |
|---|---|---|
| job name | `bypass-detect` | 신규 context 명시 (현 7 contexts 와 중복 0) |
| trigger | `push` + `pull_request` + `schedule` (nightly) + `workflow_dispatch` | (i) PR + (iii) nightly 효과 동시 발효 (§2.1 답습) |
| schedule cron | `0 3 * * *` (UTC 03:00 = KST 12:00) | ST-2 nightly schedule 동시간대 답습 (D-3 carry-over evidence 통합 자격) |
| paths filter (push) | `.pre-commit-config.yaml` + 본 workflow + audit 도구 + 모든 코드/문서 file | `.pre-commit-config.yaml` 의 6 hook 영역 (Python + YAML + Markdown) 답습 |
| pre-commit version | `4.0.1` | `requirements-dev.txt` pin 답습 (PC-1-T3 brief §4.3) |
| `--show-diff-on-failure` flag | 채택 | FAIL 시 root cause 빠른 식별 + R-MVP1-1.5-PC1-1 발화 evidence 본문 자동 capture |
| branch protection contexts 등록 | **본 sub-cycle 외** | AR-3 admin scope, 사용자 영역 — **carry-over** |

---

## §5 Rollback Trigger

| ID | 발화 조건 | 조치 |
|---|---|---|
| **R-MVP1-1.5-PC1-1** (기존 24번째 entry 답습) | 본 workflow `bypass-detect` job FAIL = dev 환경 hook bypass commit 검출 | 즉시 commit revert + dev 환경 audit 의무 + PC-1-T3 강화 합의 재진입 |
| **R-MVP1-PASS-9** (영구 금지 답습) | 본 workflow 본문 변경 시 Provider Liquidity 영향 (예: provider-specific 의존 도입) | 즉시 revert + 풀 3+1 재합의 (R-MVP1-PASS-9 trigger 발화) |

---

## §6 Evidence (실 구현 후 capture 영역, 본 brief 0건)

| Evidence ID | 영역 | 위치 |
|---|---|---|
| E-D6-1 | 본 workflow 첫 push 발화 actual run id + status | (실 구현 후 capture, `docs/phase0/mvp1-pc1-d6-evidence.md` 신규 영역) |
| E-D6-2 | nightly schedule 첫 발화 actual run id (다음 KST 12:00 이후) | (자율 영역 carry-over, PASS 효과 영향 0건) |
| E-D6-3 | `pre-commit run --all-files` CI 실행 결과 (PASS 또는 FAIL+조치) | (실 구현 후 capture) |

---

## §7 합의 형태 권고

| 항목 | 권고 |
|---|---|
| **형태** | **Reviewer-only 단축 합의** |
| **근거** | (1) PC-1-T3 sub-cycle 합의 답습 (D-6 default = "별도 sub-cycle" 자체가 *단축 합의 형태 예상*) / (2) 본 sub-cycle scope = workflow 1 file 신규 한정 + 기존 11 workflow 본문 변경 0 / (3) 5/5 풀 3+1 승격 trigger 0건 발화 예상 (ADR / 헌법 / roadmap / branch protection 본문 변경 0) / (4) ADR-011 §2.1 (a)~(e) 영향 = (b)(d) PoC 회귀 자격 보강 한정 |
| **5/5 trigger 검증** | 본 brief §3 + §4 + §5 + §6 cross-check 의무 |

---

## §8 carry-over (본 sub-cycle 외 영역)

1. **(b1-PC1-D6-contexts)** branch protection contexts 갱신 (admin scope, **사용자 영역**)
   - 현 contexts 7 → 8 (`bypass-detect` 추가)
   - `gh api -X PUT repos/.../branches/main/protection` admin 권한 필요
   - main + develop (생성 시점 7 contexts 적용) 양쪽
   - **사용자 명시 의무** (33번째 entry MVP-1 PASS evidence AR-3 답습)

2. **(b1-PC1-D6-evidence)** evidence file 신규 (`docs/phase0/mvp1-pc1-d6-evidence.md`)
   - E-D6-1/2/3 capture 후 작성 (자율 영역, PASS 효과 영향 0건)

3. **PC-1-T3 sub-cycle D-6 carry-over 해소** (PC-1-T3 brief §10 carry-over 영역)

---

## §9 자기진단 (8/8)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 본 brief 자체 실 코드 변경 0건 (file 1 = brief 신규 한정) | ✅ |
| 2 | 답습 출처 6 source 명시 + line-level 인용 cross-check 가능 | ✅ |
| 3 | scope (D-6 sub-cycle) 명확 + 변경 0건 의무 9 항목 (§1.2) | ✅ |
| 4 | R-6 BLOCKING / D-6 default / R-7(b) 차등 흡수 매트릭스 (§2) | ✅ |
| 5 | ADR-011 §2.1 (a)~(e) 매트릭스 (PC-1-T3 cell 보강) (§3) | ✅ |
| 6 | 실 구현 1 file (§4) + Rollback Trigger 2 (§5) + Evidence 3 (§6) | ✅ |
| 7 | 합의 형태 권고 + 5/5 trigger 검증 의무 (§7) | ✅ |
| 8 | carry-over 3 항목 (§8) + (b1-PC1-D6-contexts) 사용자 영역 명시 | ✅ |

---

## §10 다음 단계 (단계별 합의 cycle 답습)

1. **본 brief commit** (file 신규 1건 한정)
2. **사용자 승인** (단축 합의 진입 자격)
3. **Reviewer-only 단축 합의** (`docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-bypass-detection-ci.md` 신규)
4. **실 구현** (`.github/workflows/pre-commit-bypass-detection.yml` 신규)
5. **SESSION + INDEX + commit + push**
6. **carry-over** (contexts 갱신 = 사용자 영역, evidence capture = 자율 영역)

**자동 다음 단계 진입 금지** (메모리 답습 — 단계별 합의 cycle 패턴).
