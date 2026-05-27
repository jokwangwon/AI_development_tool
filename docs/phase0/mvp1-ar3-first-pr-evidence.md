# MVP-1 AR-3 첫 PR evidence — branch protection rule 동작 검증

> **본 문서 = (b1-AR3 첫 PR evidence)** carry-over 답습 결과. 30번째 entry evidence (`7c294bb` 직후 main branch protection 적용) → 31번째 entry 첫 PR draft (#2, `7c294bb..73ed20d`) → 11 check_runs 모두 SUCCESS → mergeable CLEAN.

---

## §0 시점 + PR

| 항목 | 값 |
|---|---|
| 시점 | 2026-05-27 (30번째 entry `7c294bb` 직후) |
| PR | https://github.com/jokwangwon/AI_development_tool/pull/2 (draft) |
| base ← head | main ← feature/jarvis-mvp0 |
| commit 수 | 17 (push fix 포함 = 18) |
| 변경 | 56 files, +9686/-12 (+ aws_key.py fix +8/-6) |

---

## §1 첫 발화 결과 (head `7c294bb`)

10 check_runs 발화 (1 FAIL):

| status | conclusion | name | workflow | duration |
|---|---|---|---|---|
| completed | **failure** | scan | **secret-hygiene-egress-redaction** | 12s |
| completed | success | scan | provider-url-scanner | 10s |
| completed | success | enforce | evidence-pass-gate | 17s |
| completed | success | enforce | g4-hash-chain | 8s |
| completed | success | enforce | provider-adapter-enforcement | 19s |
| completed | success | guard | boundary-guard | 12s |
| completed | success | verify | history-anchor-verifier | 15s |
| completed | success | feasibility | memory-skill-migration | 8s |
| completed | success | defense | rewrite-defense | 8s |
| completed | success | validate | schema-validation | 9s |

**미발화** (paths 필터): `R-4.1 Tier-1 42 canary regression` (r2-canary.yml) — `on.pull_request.paths` = `docker/r4-1-poc/** / docker/r2-poc/** / docs/architecture/canary-recheck-design.md / docs/phase0/r4-1-trigger-extension-evidence.md / .github/workflows/r2-canary.yml` 본 PR 변경 56 file 중 매치 0건.

### 1.1 scan FAIL 원인

`secret-hygiene-egress-redaction.yml` S-3 step `S-3 detect-secrets scan` 의 verify:

```
##[error]S-3 FAIL fixture missing detections: ['tests/fixtures/secret_hygiene/mvp1_s3/fail/aws_key.py']
detected paths: [
  'tests/fixtures/secret_hygiene/mvp1_s3/fail/base64_entropy.py',
  'tests/fixtures/secret_hygiene/mvp1_s3/fail/hex_entropy.py',
  'tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py',
  'tests/fixtures/secret_hygiene/mvp1_s3/fail/private_key.py'
]
```

**원인**: `aws_key.py` 의 fake canary 가 `AWSKeyDetector` regex 미충족:
- regex = `AKIA[0-9A-Z]{16}` (총 20자, AKIA prefix + 16자 [0-9A-Z])
- v1 fixture (4451716): `"AKIAFAKES3NOTREAL01"` (19자, 1자 부족) + `"ASIAFAKES3NOTREAL02"` (ASIA prefix 미인식)
- 27번째 entry brief §4.4 fixture 작성 시 detect-secrets regex 정확 verify 0건

### 1.2 R-4.1 Tier-1 42 canary regression 미발화 원인

`r2-canary.yml` 의 `on.pull_request.paths` 필터 = 본 PR 변경 56 file 중 매치 0건. branch protection contexts 에 등록되어도 발화 자체 0 → status check "Expected" 영원 대기 → merge 영원 차단 risk.

---

## §2 조치 (사용자 결정 + Claude 실행)

### 2.1 scan FAIL 조치 (사용자 결정: aws_key.py fixture 정정)

- v2 fixture (`73ed20d`):
  - `AWS_ACCESS_KEY_ID = "AKIAFAKES3NOTREAL01X"` (20자 정확, regex `AKIA[0-9A-Z]{16}` 매치)
  - `AWS_ACCESS_KEY_ID_ALT = "AKIATESTNOTREAL02XYZ"` (20자 정확, 다른 fake canary)
  - ASIA prefix 제거 (detect-secrets AWSKeyDetector 미인식 답습)
- local verify (python re.fullmatch): 양쪽 정확 매치 OK

### 2.2 R-4.1 Tier-1 42 canary regression 미발화 조치 (사용자 결정: contexts 에서 제거)

- `gh api -X PUT branches/main/protection` 갱신:
  - 8 contexts → **7 contexts** (`R-4.1 Tier-1 42 canary regression` 제거)
  - 유지: `guard / verify / feasibility / scan / enforce / defense / validate`
- 효과: paths-aware check 미발화 PR 에서도 merge 자격 발효 (r2-canary 발화 시점 = 해당 paths 변경 PR 에서만 별도 발효)

---

## §3 재발화 결과 (head `73ed20d`, fix commit 후)

**11 check_runs 모두 SUCCESS** (mergeStateStatus: CLEAN):

| status | conclusion | name | workflow | duration |
|---|---|---|---|---|
| completed | success | scan | secret-hygiene-egress-redaction | 5m37s |
| completed | success | scan | provider-url-scanner | 7s |
| completed | success | scan | (이전 head 잔여, 또는 다른 발화) | 5m35s |
| completed | success | enforce | evidence-pass-gate | 4s |
| completed | success | enforce | g4-hash-chain | 14s |
| completed | success | enforce | provider-adapter-enforcement | 24s |
| completed | success | guard | boundary-guard | 7s |
| completed | success | verify | history-anchor-verifier | 12s |
| completed | success | feasibility | memory-skill-migration | 14s |
| completed | success | defense | rewrite-defense | 10s |
| completed | success | validate | schema-validation | 9s |

**aggregate**: success=11 / failure=0 / other=0

---

## §4 R-MVP1-1.5-AR3 검증 매트릭스

### 4.1 중복 동작 검증 (29번째 entry brief §3.5 + 30번째 entry §1.3 carry-over)

| context | 실 check_run count | 모두 PASS? | 결론 |
|---|---|---|---|
| `enforce` x3 | 3 (evidence-pass-gate + g4-hash-chain + provider-adapter-enforcement) | ✅ 3/3 SUCCESS | GitHub branch protection = **모든 동명 check 의 PASS 의무 답습** (안전 처리) |
| `scan` x3 (paths 필터로 2~3 발화) | 3 (provider-url-scanner + secret-hygiene-egress-redaction x2) | ✅ 3/3 SUCCESS | 동일 |
| 기타 5 unique | 1 each | ✅ 모두 SUCCESS | 단일 발화 정상 |

→ **race condition 0 검증 완료**. mergeStateStatus: CLEAN = 7 contexts 모두 PASS 의무 충족 확정.

### 4.2 admin bypass 0 시도 evidence

| 항목 | 본 PR evidence |
|---|---|
| PR 작성자 | jokwangwon (admin=True + owner=True) |
| admin bypass 시도 | 0 (`enforce_admins: true` 답습, sub-cycle scope 명시) |
| force push 시도 | 0 (`allow_force_pushes: false`) |
| branch deletion 시도 | 0 (`allow_deletions: false`) |

### 4.3 paths-aware check 동작 발견 (carry-over)

- r2-canary 가 paths 필터로 미발화 = branch protection 의 required check 가 발화하지 않으면 "Expected" 영원 대기 → merge 차단
- 본 sub-cycle 조치 = contexts 에서 제거 (가장 단순 + 비례성)
- 대안 = r2-canary.yml paths 필터 widen 또는 r2-canary 발화 강제 dummy commit → 모두 ceremony ↑
- **다른 paths-aware workflow audit 의무 (carry-over)**: 다른 11 workflow 도 paths 필터 답습 시 동일 risk 발생 가능 → 본 evidence 작성 후 별도 sub-cycle 의무 명문

---

## §5 ADR-011 §2.1 (a)~(e) 완전 충족 (AR-3 영역 한정)

| 조건 | 본 evidence 후 충족 |
|---|---|
| **(a)** 사용자 명시 결정 | ✅ D-1~D-4 + 단계 7 적용 + scan fix + r2-canary 제거 모두 사용자 명시 |
| **(b)** 격리 환경 PoC 실증 | ✅ 첫 PR 11 check_runs 모두 SUCCESS + 중복 동작 검증 + admin bypass 0 evidence |
| **(c)** 도구/리소스 stateless · network-free | ✅ 답습 |
| **(d)** 자동 회귀 검증 경로 | ✅ branch protection rule 발효 + 매 PR 자동 status check 의무 + 7 contexts 답습 |
| **(e)** 합의 APPROVE 운영조건 | ✅ 29번째 entry 합의 + 30번째 entry 합의 답습 |

→ **(a)~(e) 5/5 완전 충족** (AR-3 영역). **(c) MVP-1 Implementation Evidence PASS 발효 합의 진입 자격 자격** = (b1) 4 sub-cycle 완료 + AR-3 첫 PR evidence (본 문서) + 사용자 명시 별도 합의.

---

## §6 carry-over

1. **PR #2 merge 결정** = 별도 시점 사용자 영역 (draft 답습, 본 sub-cycle scope 외)
2. **paths-aware workflow audit** = 다른 11 workflow 중 paths 필터 답습 시 동일 risk (r2-canary 와 동형) 발견 시 contexts 제거 또는 widen sub-cycle
3. **r2-canary 정상 발화 evidence** = r2-canary.yml paths 매치 PR (예: `docker/r4-1-poc/**` 변경) 발생 시점 별도 evidence
4. **(b1-AR3 develop)** = develop branch 신규 생성 시점 동일 7 contexts body PUT 답습 적용
5. **(c) MVP-1 Implementation Evidence PASS 발효 합의** = (b1) 4 sub-cycle + 본 evidence + 사용자 명시 별도 합의 진입 자격
6. **본 PR fix commit (`73ed20d`) = ad-hoc 영역** — 31번째 entry SESSION 답습 명문 + 향후 fixture regex 정확 verify 답습 (R-4.1 plugin verify ceremony 답습)
