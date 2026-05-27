# MVP-1 AR-3 사용자 admin scope 단계 7 적용 evidence

> **본 문서 = (b1-AR3) sub-cycle (29번째 entry, commit `7f57323`) 의 사용자 admin scope 단계 7 적용 evidence**. brief §4.3 + 합의 보고서 §6.3 단계 7 답습. main branch protection rule 적용 발효 + GitHub check name catalog 정확화 (R-MVP1-1.5-AR3-2a 답습).

---

## §0 적용 시점 + 권한

| 항목 | 값 |
|---|---|
| 적용 시점 | 2026-05-27 (29번째 entry commit `7f57323` 직후) |
| 적용 method | `gh api -X PUT repos/jokwangwon/AI_development_tool/branches/main/protection` |
| 사용자 권한 | admin=True + owner=True + token scope `repo` (jokwangwon, sufficient for self-owned repo branch protection) |
| 적용 대상 | `main` branch (단독, develop branch 부재 → carry-over) |

---

## §1 R-MVP1-1.5-AR3-2a 발효 — catalog 정정 (도구 변경 단축 합의 답습)

### 1.1 brief §3.2 catalog 후보 vs 실 GitHub check_run name

| # | brief §3.2 후보 (workflow name + job name) | 실 GitHub check_run name | mismatch 처리 |
|---|---|---|---|
| 1 | "G3 + G4 Boundary Guard / guard" | **`guard`** | job name 만 채택 |
| 2 | "Evidence / PASS Gate / enforce" | **`enforce`** | job name 만 + workflow 구분 0 |
| 3 | "G4 Hash Chain + JCS / enforce" | **`enforce`** | 동일 (중복) |
| 4 | "G4 History Anchor Verifier (Layer 5) / verify" | **`verify`** | job name 만 |
| 5 | "G2 GP-6 Memory/Skill Feasibility / feasibility" | **`feasibility`** | job name 만 |
| 6 | "Provider Adapter Enforcement / enforce" | **`enforce`** | 동일 (중복, 3개 동일) |
| 7 | "G2 GP-5 3차 Provider URL Scanner / scan" | **`scan`** | job name 만 + 중복 |
| 8 | "Redaction Canary Regression / R-4.1 Tier-1 42 canary regression" | **`R-4.1 Tier-1 42 canary regression`** | job name 만 |
| 9 | "G4 Rewrite Defense (Layer 2/3/4) / defense" | **`defense`** | job name 만 |
| 10 | "G2 GP-4 + G4 Schema Validation / validate" | **`validate`** | job name 만 |
| 11 | "G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction / scan" | **`scan`** | 동일 (중복, 2개 동일) |

→ **GitHub branch protection contexts 입력 형식 = job name 만 (workflow name 미포함)**. 11 후보 → **8 unique job name**:
- `guard` (1)
- `verify` (1)
- `feasibility` (1)
- `scan` (2개 workflow 중복 — provider-url-scanner + secret-hygiene-egress-redaction)
- `enforce` (3개 workflow 중복 — evidence-pass-gate + g4-hash-chain + provider-adapter-enforcement)
- `R-4.1 Tier-1 42 canary regression` (1)
- `defense` (1)
- `validate` (1)

### 1.2 catalog 정정 자격 (R-MVP1-1.5-AR3-2a 답습)

R-MVP1-1.5-AR3-2a = "도구 변경 단축 합의 + 사용자 명시 + catalog 정정 의무". 본 적용 시점 발견 = **단축 합의 + 사용자 명시** 자격 충족 (사용자 결정 `job name 만 8 unique` 채택 직접). brief §3.2 catalog 정정 발효:

- brief §3.2 "workflow name + job name" 후보 → **본 evidence §1.1 답습 = job name 만 (8 unique)** 정확화
- 본 evidence 발효 후 brief §3.2 정정 = R-MVP1-1.5-AR3-2a 답습 영역 (별도 commit 또는 본 commit 인-place 정정 = ceremony 최소화 측면 본 commit 답습)

### 1.3 중복 job name 의 branch protection 동작 (남은 검증)

`scan` x2 + `enforce` x3 의 GitHub branch protection 동작:
- **추측 1 (안전)**: GitHub 가 동일 name 의 모든 check 가 PASS 의무
- **추측 2 (race)**: 마지막 보고 status 만 적용

→ **첫 PR 시 verify 의무** (carry-over evidence 영역). mismatch 발견 시 = workflow job name unique 화 sub-cycle 별도 진입.

---

## §2 적용된 branch protection rule body (응답)

```json
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "guard",
      "verify",
      "feasibility",
      "scan",
      "enforce",
      "R-4.1 Tier-1 42 canary regression",
      "defense",
      "validate"
    ],
    "checks": [
      {"context": "guard", "app_id": 15368},
      {"context": "verify", "app_id": 15368},
      {"context": "feasibility", "app_id": 15368},
      {"context": "scan", "app_id": 15368},
      {"context": "enforce", "app_id": 15368},
      {"context": "R-4.1 Tier-1 42 canary regression", "app_id": 15368},
      {"context": "defense", "app_id": 15368},
      {"context": "validate", "app_id": 15368}
    ]
  },
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": false,
    "require_code_owner_reviews": false,
    "require_last_push_approval": false,
    "required_approving_review_count": 0
  },
  "enforce_admins": {"enabled": true},
  "required_signatures": {"enabled": false},
  "required_linear_history": {"enabled": false},
  "allow_force_pushes": {"enabled": false},
  "allow_deletions": {"enabled": false},
  "block_creations": {"enabled": false},
  "required_conversation_resolution": {"enabled": false},
  "lock_branch": {"enabled": false},
  "allow_fork_syncing": {"enabled": false}
}
```

→ `app_id: 15368` = GitHub Actions app (모든 check 가 GitHub Actions 발 보고)

---

## §3 ADR-011 §2.1 (a)~(e) 충족 상태 갱신 (29번째 entry 합의 §4 답습)

| 조건 | 본 적용 후 충족 |
|---|---|
| **(a)** 사용자 명시 결정 | ✅ 충족 답습 (D-1~D-4 + 단계 7 적용 명시) |
| **(b)** 격리 환경 PoC 실증 | ⏳ **부분 충족** — branch protection 적용 evidence (본 응답) + 첫 PR 시 11 workflow PASS + admin bypass 0 evidence 추가 의무 |
| **(c)** 도구/리소스 stateless · network-free | ✅ 답습 |
| **(d)** 자동 회귀 검증 경로 | ⏳ **부분 충족** — branch protection rule 발효 = 매 PR 자동 status check verify 자격 발효, 첫 PR run 시 evidence 추가 의무 |
| **(e)** 합의 APPROVE 운영조건 | ✅ 답습 |

→ **본 적용 후 충족 = (a)(c)(e) 3/5 + (b)(d) 부분 충족 (적용 evidence 발효, 첫 PR run evidence 추가)** → **첫 PR 시점 = (a)~(e) 5/5 충족** (AR-3 영역 한정)

---

## §4 develop branch carry-over

| 항목 | 상태 |
|---|---|
| develop branch 존재 | ❌ HTTP 404 ("Branch not found") |
| develop branch 보호 | (develop 부재로 미적용) |
| 본 evidence carry-over | develop branch 생성 시점 별도 적용 의무 — 동일 body (`/branches/develop/protection`) PUT 답습 |

---

## §5 다음 단계 (carry-over)

1. **첫 PR open evidence** — feature/jarvis-mvp0 → main PR 시 11 workflow 모두 status check 발화 + 모든 PASS 의무 + admin bypass 0 시도 evidence (ADR-011 (b)(d) 완전 충족)
2. **R-3 verify** — 첫 PR 의 status check 보고 시 `scan` x2 / `enforce` x3 동일 name 처리 동작 검증 → mismatch 시 workflow job name unique 화 별도 sub-cycle
3. **develop branch 생성 시점** — 본 evidence body PUT 답습 적용
4. **brief §3.2 catalog 정정** — 본 evidence §1.1 매트릭스 답습 (별도 commit 또는 본 commit 인-place — ceremony 측면 본 commit 답습)
