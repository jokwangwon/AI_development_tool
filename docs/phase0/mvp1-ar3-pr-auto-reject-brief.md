# MVP-1 AR-3 통합 PR auto-reject 실 구현 sub-cycle brief

> **scope**: MVP-1 1.5차 보강 entry 합의 (24번째 entry, commit `9638521`) 의 **AR-3 (AR-1 + AR-2 통합 PR auto-reject) 실 구현 sub-cycle**. 본 sub-cycle = entry 합의 결정 *집행* + **check name catalog 본문 채택 + 사용자 admin web UI 안내 명문 한정** (실 branch protection rule 적용 = 사용자 GitHub admin 수동 의무, Claude scope 외).
>
> **본 brief 자체에서 branch protection rule 변경 0건 의무** — brief 합의 발효 *후* (1) Claude scope = check name catalog 본문 채택 + (a) Markdown evidence 권고 + 사용자 명령 안내, (2) 사용자 scope = GitHub web UI/gh CLI 수동 적용.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **24번째 entry brief v1.1** | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (`9638521`) | §2.4 AR-3 정의 (line 215~245) + §3 ADR-011 (b)(d) AR-3 cell (line 259/261) + §4 합의 형태 (line 290) + §5.1 R-MVP1-1.5-AR3-{1,2,3} (line 332~334) + §6 Evidence + §4 line 113 시점 선차 변경 |
| **24번째 entry 합의 보고서** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | R-3 BLOCKING (check name mapping verify) + R-7(c) (R-MVP1-1.5-AR3-2 차등 분리: 도구 변경 vs T3 정책 신규 check) |
| **Backlog #2 합의** | `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` | AR-3 = Deferred 유지 + Backlog #3 이관 명시 → 본 cycle = 시점 선차 변경 (MVP-1 1.5차 동시 진입) |
| **roadmap-mvp1** | §4.7.3 line 480 | "AR-2 / AR-3 진입 (branch protection rule 변경) \| **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** \| T3 영역" |
| **11 workflow 발효** | `.github/workflows/*.yml` | AR-1 (CI step fail-closed) 부분 발효 답습 — 11 workflow 모두 `name:` 명시 + jobs 정의 |
| **PC-1/S-3/ST-2 sub-cycle 답습** | `3a63a5b` + `4451716` + `1edc5bb` | Reviewer-only 단축 합의 패턴 + 변경 0건 의무 매트릭스 + 6단계 cycle 답습 |
| **현 상태** | `gh api repos/jokwangwon/AI_development_tool/branches/main/protection` | "Branch not protected" (HTTP 404) — main + develop 모두 unprotected |

---

## §1 scope (AR-3 sub-cycle 한정)

### 1.1 본 sub-cycle 의 본질 (Claude scope vs 사용자 admin scope)

| 항목 | 내용 |
|---|---|
| **scope** | AR-3 (AR-1 + AR-2 통합 PR auto-reject) 실 구현 sub-cycle |
| **영역** | GP-3 + GP-5 T3 정책 (branch protection rule 본문 변경) |
| **합의 형태 권고** | **단축 합의 + 사용자 명시** (PC-1/S-3/ST-2 sub-cycle 패턴 답습) |
| **Claude scope** | (1) R-3 BLOCKING 흡수 = 11 workflow check name catalog 본문 채택 + (2) 사용자 admin 수동 적용 명령 안내 명문 + (3) AR-1 + AR-2 통합 효과 명문 |
| **사용자 admin scope** | (1) GitHub web UI: Settings → Branches → Add rule (`main` + `develop`) — Require status checks + Restrict pushes + Do not allow bypassing + (2) 또는 `gh api -X PUT repos/.../branches/main/protection` 호출 (admin token 필수) |
| **변경 0건 의무** | branch protection rule 실 적용 = Claude 영역 외 / `.github/workflows/` 11 workflow 본문 0건 / src/ 0건 / tools/ 0건 / docker/ 0건 |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | `.github/workflows/` 11 workflow 본문 변경 | 0건 (AR-1 답습 유지) |
| 2 | `.pre-commit-config.yaml` 본문 변경 | 0건 |
| 3 | `.githooks/` 본문 변경 | 0건 |
| 4 | src/ 본문 변경 | 0건 |
| 5 | tools/ 본문 변경 | 0건 |
| 6 | docker/ 본문 변경 | 0건 |
| 7 | branch protection rule 실 적용 (Claude 영역 외) | 0건 (사용자 admin 수동 의무) |
| 8 | MVP-1 영역 외 *다른* branch protection rule (예: feature/* 패턴 등) | 0건 (N-6 권고 답습, 별도 합의) |
| 9 | Backlog #3 *전체* 진입 (ST-4 Vault HSM / commit signing 강제 / Tier-2/3 catalog 등) | 0건 (N-3 권고 답습, AR-3 단독 시점 변경 한정) |
| 10 | ADR / 헌법 / roadmap 본문 변경 | 0건 |
| 11 | MVP-1 Implementation Evidence PASS 발효 | 0건 ((c) carry-over 영역) |
| 12 | `adapters/llm/facade.py` placeholder → real | 0건 ((d) carry-over 영역) |

---

## §2 24번째 entry BLOCKING + 권고 흡수 매트릭스

| ID | 항목 | 본 brief 흡수 위치 |
|---|---|---|
| **R-3** BLOCKING | AR-3 check name mapping verify — required check 단위 = workflow file명 ≠ 실제 check name (GitHub branch protection = job name 또는 workflow_run.conclusion 단위 mapping) | §3.2 11 workflow check name catalog 본문 채택 + §3.3 GitHub 인식 형식 verify 절차 |
| **R-7(c)** BLOCKING | R-MVP1-1.5-AR3-2 분리 — (a) 도구 변경 (R-MVP1-1.5-AR3-2a) vs (b) T3 정책 신규 check (R-MVP1-1.5-AR3-2b) | §6 Rollback Trigger 본 sub-cycle 적용 형태 (2a + 2b 차등) |
| **권고** | AR-3 APPROVE w/ COND 격상 — 본 sub-cycle = COND 해소 (R-3 흡수 + AR-1 + AR-2 통합 명문) | 본 brief 전체 |

---

## §3 현 상태 audit

### 3.1 이미 발효 (답습 영역, 변경 0건 의무)

| 자료 | 상태 | source |
|---|---|---|
| 11 workflow (AR-1 부분 발효) | ✅ 발효 | `boundary-guard.yml` / `evidence-pass-gate.yml` / `g4-hash-chain.yml` / `history-anchor-verifier.yml` / `memory-skill-migration-feasibility.yml` / `provider-adapter-enforcement.yml` / `provider-url-scanner.yml` / `r2-canary.yml` / `rewrite-defense.yml` / `schema-validation.yml` / `secret-hygiene-egress-redaction.yml` (24 step, S-3 3 step + ST-2 step + nightly schedule 포함) |
| 모든 workflow name + job 정의 | ✅ 발효 | §3.2 catalog 답습 |

### 3.2 11 workflow check name catalog 본문 채택 (R-3 BLOCKING 흡수)

> ⚠️ **R-MVP1-1.5-AR3-2a 발효 정정 (단계 7 적용 시점, 2026-05-27)**: 본 §3.2 의 11 후보 (workflow name + job name 조합) 은 brief v1 작성 시점 추측. **GitHub 실 check_run name = job name 만** (workflow name 미포함). 적용 시점 실 verify 결과 = **8 unique job name** (아래 §3.2.1 답습). brief v1 의 11 후보 = R-MVP1-1.5-AR3-2a 답습 정정 영역 — 본 §3.2 = historical 기록 보존, §3.2.1 = 적용 정확 catalog. 정확한 본 evidence = `docs/phase0/mvp1-ar3-branch-protection-applied-evidence.md` (`7f57323` 직후 commit) 답습.

| # | workflow file | workflow name | job id | job name | brief v1 후보 (정정 대상 — historical) |
|---|---|---|---|---|---|
| 1 | `boundary-guard.yml` | `G3 + G4 Boundary Guard` | guard | `guard` | ~~"G3 + G4 Boundary Guard / guard"~~ → `guard` |
| 2 | `evidence-pass-gate.yml` | `Evidence / PASS Gate` | enforce | `enforce` | ~~"Evidence / PASS Gate / enforce"~~ → `enforce` (중복) |
| 3 | `g4-hash-chain.yml` | `G4 Hash Chain + JCS` | enforce | `enforce` | ~~"G4 Hash Chain + JCS / enforce"~~ → `enforce` (중복) |
| 4 | `history-anchor-verifier.yml` | `G4 History Anchor Verifier (Layer 5)` | verify | `verify` | ~~"G4 History Anchor Verifier (Layer 5) / verify"~~ → `verify` |
| 5 | `memory-skill-migration-feasibility.yml` | `G2 GP-6 Memory/Skill Feasibility` | feasibility | `feasibility` | ~~"G2 GP-6 Memory/Skill Feasibility / feasibility"~~ → `feasibility` |
| 6 | `provider-adapter-enforcement.yml` | `Provider Adapter Enforcement` | enforce | `enforce` | ~~"Provider Adapter Enforcement / enforce"~~ → `enforce` (중복) |
| 7 | `provider-url-scanner.yml` | `G2 GP-5 3차 Provider URL Scanner` | scan | `scan` | ~~"G2 GP-5 3차 Provider URL Scanner / scan"~~ → `scan` (중복) |
| 8 | `r2-canary.yml` | `Redaction Canary Regression` | canary-regression | `R-4.1 Tier-1 42 canary regression` | ~~"Redaction Canary Regression / R-4.1 Tier-1 42 canary regression"~~ → `R-4.1 Tier-1 42 canary regression` |
| 9 | `rewrite-defense.yml` | `G4 Rewrite Defense (Layer 2/3/4)` | defense | `defense` | ~~"G4 Rewrite Defense (Layer 2/3/4) / defense"~~ → `defense` |
| 10 | `schema-validation.yml` | `G2 GP-4 + G4 Schema Validation` | validate | `validate` | ~~"G2 GP-4 + G4 Schema Validation / validate"~~ → `validate` |
| 11 | `secret-hygiene-egress-redaction.yml` | `G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction` | scan | `scan` | ~~"G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction / scan"~~ → `scan` (중복) |

#### 3.2.1 적용 정확 catalog (8 unique job name)

`gh api -X PUT repos/.../branches/main/protection` 적용 시 사용된 `required_status_checks.contexts` (단계 7, `7f57323` 직후):

```
[
  "guard",
  "verify",
  "feasibility",
  "scan",
  "enforce",
  "R-4.1 Tier-1 42 canary regression",
  "defense",
  "validate"
]
```

→ 11 workflow → 8 unique job name. 중복:
- `scan` x2 (provider-url-scanner + secret-hygiene-egress-redaction)
- `enforce` x3 (evidence-pass-gate + g4-hash-chain + provider-adapter-enforcement)

> **중복 동작 검증 미완** = 첫 PR 시 verify 의무 (carry-over, evidence §1.3 답습). mismatch 발견 시 workflow job name unique 화 별도 sub-cycle.

### 3.3 GitHub 인식 형식 verify 절차 (R-3 BLOCKING 답습)

본 catalog (§3.2) 의 required check 후보는 GitHub UI 의 실 표시 형식과 일치 검증 의무. 절차:

1. main branch 에 push 또는 PR open → 11 workflow 모두 actual run 발화
2. GitHub Settings → Branches → Add rule → "Require status checks to pass before merging" 활성화
3. "Status checks" 검색창에 catalog 후보 string 입력 → dropdown 표시 형식 확인
4. dropdown 표시 string 을 정확 답습하여 required check list 등록

**제약**: dropdown 표시 string 이 catalog 후보와 차이 시 = brief 채택 catalog 정정 의무 (별도 sub-cycle 또는 본 sub-cycle in-place 수정)

### 3.4 branch protection rule 현 상태

| 항목 | 현 상태 | 본 sub-cycle 후속 |
|---|---|---|
| `main` branch protection | ✅ unprotected ("Branch not protected" HTTP 404) | 사용자 admin 적용 의무 — Settings → Branches → Add rule |
| `develop` branch protection | (verify 의무) | 동일 |

### 3.5 R-MVP1-1.5-AR3-{1,2a,2b,3} Rollback Trigger 답습 (R-7(c) 차등 분리)

| ID | trigger | 본 sub-cycle 발효 형태 |
|---|---|---|
| **R-MVP1-1.5-AR3-1** | branch protection rule 우회 / admin bypass 발견 | 단축 합의 + 사용자 명시 재검토 + bypass detection evidence |
| **R-MVP1-1.5-AR3-2a** | 11 workflow 본문 변경 — 기존 도구 변경 영향 분석 (job 추가/제거/name 변경) | 단축 합의 + 사용자 명시 + check name catalog (§3.2) 정정 의무 |
| **R-MVP1-1.5-AR3-2b** | 신규 status check 추가 — T3 정책 영역 신규 check | **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** (T3 영역 답습) |
| **R-MVP1-1.5-AR3-3** | branch protection rule = MVP-1 영역 외 *다른* rule (feature/* / PR review required / signed commits 등) | 별도 합의 영역 (N-6 권고 답습) |

---

## §4 실 구현 항목 (Claude scope = 2 + 사용자 admin scope = 1)

### 4.1 Claude scope — check name catalog 본문 채택 (본 brief §3.2)

본 brief 합의 발효 시 = §3.2 catalog 본문 채택 발효. 별도 file 추가 0건 (brief 본문 자체가 catalog source).

### 4.2 Claude scope — 사용자 admin 수동 적용 명령 안내 (brief 본문 + commit 시점 보고)

#### (A) web UI 절차 (권고 — 사용자 직관 ↑)

1. https://github.com/jokwangwon/AI_development_tool/settings/branches
2. "Add branch protection rule" 클릭
3. **Branch name pattern**: `main` (이후 동일 절차로 `develop`)
4. ☑️ **Require a pull request before merging** (PR 의무화)
   - ☑️ Required approvals: 0 (단독 개발, 비례성 답습)
5. ☑️ **Require status checks to pass before merging**
   - ☑️ Require branches to be up to date before merging
   - **Status checks**: §3.2 catalog 11 check 모두 추가 (dropdown 표시 형식 답습)
6. ☑️ **Do not allow bypassing the above settings** (admin bypass 0건 — 사용자 명시 의무)
7. ❌ Restrict pushes that create matching branches (단독 개발, 비례성 답습)
8. "Create" 클릭

#### (B) gh CLI 절차 (대안 — admin token 필수, 사용자 OAuth scope `repo:admin` 확인 의무)

```bash
gh api -X PUT repos/jokwangwon/AI_development_tool/branches/main/protection \
  --input - <<'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "G3 + G4 Boundary Guard / guard",
      "Evidence / PASS Gate / enforce",
      "G4 Hash Chain + JCS / enforce",
      "G4 History Anchor Verifier (Layer 5) / verify",
      "G2 GP-6 Memory/Skill Feasibility / feasibility",
      "Provider Adapter Enforcement / enforce",
      "G2 GP-5 3차 Provider URL Scanner / scan",
      "Redaction Canary Regression / R-4.1 Tier-1 42 canary regression",
      "G4 Rewrite Defense (Layer 2/3/4) / defense",
      "G2 GP-4 + G4 Schema Validation / validate",
      "G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction / scan"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 0
  },
  "restrictions": null
}
EOF
```

→ 동일 절차로 `branches/develop/protection` 호출

> **R-3 답습**: contexts list = §3.2 catalog 후보. GitHub 이 dropdown 에 표시하는 실 string 과 mismatch 시 API 호출 실패 또는 검증 누락 risk → first actual run 후 dropdown verify + 정정 의무.

### 4.3 사용자 admin scope — 실 branch protection rule 적용 (Claude 영역 외)

위 (A) 또는 (B) 절차 사용자 직접 수행. 적용 후 evidence 보고 (`gh api repos/.../branches/main/protection` 응답 = 적용된 rule body) → 본 brief carry-over evidence 등록.

### 4.4 AR-1 + AR-2 통합 효과 명문 (Defense in depth)

| 계층 | 수단 | 발효 |
|---|---|---|
| **CI step level (AR-1)** | 11 workflow 모두 fail-closed (job rc=1 → workflow conclusion=failure) | ✅ 이미 발효 답습 (기존 11 workflow + S-3 3 step + ST-2 step 모두 fail-closed) |
| **PR merge level (AR-2)** | branch protection rule "Require status checks to pass" + "Do not allow bypassing" | ⏳ 본 sub-cycle 발효 → 사용자 admin 적용 시점 발효 |
| **통합 효과 (AR-3)** | PR 의 모든 commit 이 11 workflow 모두 PASS 의무 + admin bypass 0건 = **PR auto-reject runtime** | ⏳ 본 sub-cycle 발효 + 사용자 admin 적용 시점 발효 |

→ **PC-1 + PC-3 + AR-3 결합 (`3a63a5b` 답습)**: PC-1 (dev 환경 hook) 우회 시 PC-3 (CI step) 차단 / PC-3 우회 시 AR-3 (branch protection) 차단 = 3 계층 Defense in depth.

---

## §5 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (AR-3 본 sub-cycle 한정)

| 조건 | 본 sub-cycle 충족 |
|---|---|
| **(a)** 사용자 명시 결정 | ⏳ 본 brief 사용자 승인 + D-1~D-4 결정 + 사용자 admin 적용 시 충족 |
| **(b)** 격리 환경 PoC 실증 | ⏳ 사용자 admin 적용 후 = 첫 PR 시 11 workflow 모두 PASS 의무 + admin bypass 시도 evidence (또는 0 시도 명문) |
| **(c)** 도구/리소스 stateless · network-free | ✅ GitHub branch protection rule = GitHub 자체 정책 (외부 의존 0, Provider Liquidity 5-way 답습 영역 외) |
| **(d)** 자동 회귀 검증 경로 | ⏳ 사용자 admin 적용 후 = 매 PR 자동 status check verify + admin bypass 0 시도 audit |
| **(e)** 합의 APPROVE 운영조건 | ⏳ 본 brief 합의 APPROVE 시 발효 |

→ **현 시점 충족 = (c) 만** → 본 sub-cycle 합의 발효 (단축 합의 APPROVE) = (a)(e) 추가 충족 / 사용자 admin 적용 + 첫 PR evidence = (b)(d) 추가 충족 → (a)~(e) 5/5 충족 (AR-3 영역 한정)

---

## §6 Rollback Trigger (본 sub-cycle 적용 형태)

§3.5 답습 — R-MVP1-1.5-AR3-{1,2a,2b,3} 4 trigger 본문 채택. R-7(c) 차등 분리 (2a 도구 변경 단축 합의 + 2b T3 정책 풀 3+1) 본 brief 발효 시 본문 채택 발효.

---

## §7 Evidence

| Evidence | 형식 | 본 sub-cycle 발효 |
|---|---|---|
| **(a) Markdown report** | `docs/phase0/g2-gp3-mvp1-evidence.md` + `docs/phase0/g2-gp5-mvp1-evidence.md` 보강 (AR-3 영역 추가) | 별도 sub-cycle (D-3 답습, (b1) 4 sub-cycle 완료 후 일관 보강) |
| **(b) PoC 실증** | branch protection rule 적용 후 첫 PR 시 11 workflow PASS evidence | 사용자 admin 적용 + 첫 PR 실 발화 시 |
| **(c) Docker isolation log** | N/A (GitHub 자체 정책 영역) | (c) 답습 발효 자격 |
| **(d) GitHub Actions run** | 적용된 branch protection rule body (`gh api repos/.../branches/main/protection`) + 첫 PR check status report | 사용자 admin 적용 후 |
| **(e) 합의 보고서** | 본 sub-cycle 합의 보고서 (단축 합의 권고) | 본 brief 합의 발효 |

---

## §8 사용자 결정 항목 (brief 합의 진입 전 의무)

| # | 항목 | 후보 | 권고 |
|---|---|---|---|
| **D-1** | 합의 형태 | (i) 단축 합의 (Reviewer-only) / (ii) 풀 3+1 / (iii) 풀 3+1 + 외부 LLM 1+ | **(i) 단축 합의 (Reviewer-only)** — PC-1/S-3/ST-2 sub-cycle 패턴 답습 + entry cycle 에서 AR-3 채택 + Backlog #3 시점 선차 변경 + R-3 BLOCKING 흡수 자체 완료, 본 sub-cycle = 결정 *집행* (Claude scope = catalog 본문 + 안내 명문) |
| **D-2** | 적용 절차 | (A) web UI (사용자 직관 ↑) / (B) gh CLI (admin token 의무) / (C) 둘 다 안내 | **(C) 둘 다 안내** — 사용자 선택 자율, brief 본문 §4.2 (A) + (B) 모두 답습 |
| **D-3** | 보호 branch 범위 | (i) `main` 만 / (ii) `main` + `develop` / (iii) `main` + `develop` + `feature/**` (또는 feature/jarvis-*) | **(ii) `main` + `develop`** — entry brief line 113 답습 ("`main` + `develop` 보호 + status check 의무"), feature/** = R-MVP1-1.5-AR3-3 별도 합의 영역 |
| **D-4** | required approvals | (i) 0 (단독 개발, 비례성 답습) / (ii) 1 (자가 review 의무화) / (iii) 사용자 명시 | **(i) 0** — 단독 개발 + 메모리 "비례 보안 — 개인 툴" 답습 (자가 review = `pre-commit run --all-files` + local CI 검증 답습, PR review 절차 과잉) |

---

## §9 합의 형태 권고 + 다음 단계

### 9.1 합의 형태 권고

**단축 합의 (Reviewer-only)** 권고 — 근거 (PC-1/S-3/ST-2 sub-cycle 패턴 답습):

| 근거 | 내용 |
|---|---|
| **entry brief line 290** | "단축 합의 + 사용자 명시" framing |
| **entry cycle 완료** | AR-3 채택 결정 + APPROVE w/ COND (R-3 BLOCKING 흡수) 자체는 24번째 entry cycle (`9638521`) 에서 완료. Backlog #3 시점 선차 변경도 entry cycle 발효. 본 sub-cycle = 결정 *집행* (catalog 본문 + 안내) |
| **변경 0건 의무** | 11 workflow 본문 / src / tools / docker / .pre-commit-config.yaml 모두 0건. 변경 = brief + 합의 + (Claude scope 안내) 한정 |
| **풀 3+1 승격 trigger** | 5/5 모두 발화 0건 (① 새 권위 결정 0 [AR-3 채택 = entry cycle] / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0) |
| **PC-1/S-3/ST-2 답습** | PC-1 (`3a63a5b`) + S-3 (`4451716`) + ST-2 (`1edc5bb`) Reviewer-only 단축 합의 패턴 답습 |
| **Claude scope 한계** | branch protection rule 실 적용 = Claude 영역 외 (사용자 admin 수동 의무) → 본 sub-cycle 의 "수단 결정" 영역 = catalog 본문 + 안내 한정 (자체 risk ≈ 0) |

### 9.2 다음 단계 (단계별 합의 cycle 6단계 답습)

1. ✅ **brief 작성** (본 단계, 본 commit)
2. ⏳ **사용자 승인** — §8 D-1~D-4 사용자 결정 의무
3. ⏳ **단축 합의** — Reviewer-only 합의 보고서 작성 (5/5 풀 3+1 승격 trigger 발화 검증 + R-3 + R-7(c) 흡수 cross-check)
4. ⏳ **Claude scope 실 구현** — brief 본문 §3.2 catalog + §4.2 안내 명문 답습 (별도 file 추가 0건)
5. ⏳ **commit** — 본 sub-cycle 정리 commit (SESSION + INDEX + 본 commit)
6. ⏳ **push** — SSH 답습 (`reference_git_remote_ssh.md` 메모리 답습)
7. ⏳ **사용자 admin scope 실 적용** (commit 후) — web UI 또는 gh CLI (D-2 답습)

---

## §10 본 brief 자기진단 (8/8 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 본 brief 자체 branch protection rule / 11 workflow / src / tools / docker 본문 변경 0건 | ✅ brief 작성 한정 |
| 2 | Claude scope vs 사용자 admin scope 명문 분리 | ✅ §1.1 + §4.3 |
| 3 | R-3 BLOCKING 흡수 — 11 workflow check name catalog 본문 채택 (§3.2) + GitHub 인식 형식 verify 절차 (§3.3) | ✅ §2 + §3.2 + §3.3 |
| 4 | R-7(c) 차등 분리 흡수 — R-MVP1-1.5-AR3-2a 도구 변경 (단축) vs 2b T3 정책 신규 check (풀 3+1) | ✅ §3.5 |
| 5 | AR-1 + AR-2 통합 효과 명문 (Defense in depth) + PC-1 + PC-3 + AR-3 결합 답습 | ✅ §4.4 |
| 6 | MVP-1 영역 외 다른 rule + Backlog #3 전체 진입 0건 명문 (N-6 + N-3 답습) | ✅ §1.2 #8 + #9 |
| 7 | ADR-011 (a)~(e) 매트릭스 발효 자격 명시 ((c) 1/5 + 합의 시점 + 사용자 적용 시점) | ✅ §5 |
| 8 | 사용자 결정 항목 명시 (D-1~D-4) + 합의 형태 권고 명시 + 6단계 + 사용자 admin 적용 단계 (7) 명문 | ✅ §8 + §9 |

---

> **본 brief 발효 시점** = 사용자 승인 (§8 D-1~D-4 결정) + Reviewer-only 단축 합의 APPROVE + 본 brief commit. 본 brief 자체 = **catalog 본문 채택 + 안내 명문 발효 자격** 한정. 실 branch protection rule 적용 = 사용자 admin 수동 영역 (commit 후 carry-over).
