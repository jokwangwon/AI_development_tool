# MVP-1 (b1-PC1-D6) bypass detection workflow evidence

> **자율 영역 evidence 통합** (PASS 효과 영향 0건). 40~47번째 entry chain D-6 workflow 발효 후 누적 evidence capture. ADR-011 §2.1 (b)(d) 회귀 자격 evidence + R-MVP1-1.5-PC1-1 Rollback Trigger 메커니즘 작동 자격 답습.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **40번째 entry brief** | `docs/phase0/mvp1-pc1-d6-bypass-detection-ci-brief.md` | §6 Evidence 3 항목 (E-D6-1/2/3) 정의 |
| **40~47번째 entry SESSION 로그** | `docs/sessions/SESSION_2026-05-27.md` | 40 D-6 신규 + 41 permissions 정합 + 42 false-positives + 43 contexts + 46 fp-edge-extensions + 47 Node.js 24 마이그레이션 |
| **D-6 workflow** | `.github/workflows/pre-commit-bypass-detection.yml` | trigger 4종 (push + pull_request + schedule + workflow_dispatch) + job `bypass-detect` + `pre-commit run --all-files --show-diff-on-failure` |
| **D-6 workflow run history** | GitHub Actions API (`gh run list --workflow=pre-commit-bypass-detection.yml`) | 14 runs (2026-05-27 본 세션 내 모두 발화) |

---

## §1 E-D6-1: workflow 발화 actual run id + status timeline

### 1.1 14 runs full timeline (2026-05-27 본 세션)

| # | createdAt (UTC) | event | head_sha | run_id | status | conclusion | entry |
|---|---|---|---|---|---|---|---|
| 14 | 13:39:35 | push | ad5b875 | 26514748027 | completed | **success** | 47 (Node.js 24 마이그레이션) |
| 13 | 11:39:49 | push | d71f8a8 | 26508931246 | completed | **success** | 46 (fp-edge-extensions) |
| 12 | 11:27:23 | push | f29a34b | 26508356757 | completed | **success** | 45 (branch sync) |
| 11 | 11:24:27 | push | 505916d | 26508223968 | completed | **success** | 45 (cherry-pick HEAD) |
| 10 | 11:19:19 | push | a5d14c6 | 26507990834 | completed | **success** | 44 (PR #2 MERGED commit) |
| 9 | 11:16:55 | push | eb51284 | 26507883720 | completed | **success** | 44 (main squash, 본 branch에 도착) |
| 8 | 11:01:17 | pull_request | 6bf4321 | 26507186366 | completed | **success** | 43 (PR #2) |
| 7 | 11:01:13 | push | 6bf4321 | 26507183736 | completed | **success** | 43 (contexts 갱신 commit) |
| 6 | 10:52:19 | pull_request | a6dc51d | 26506776247 | completed | **success** | 42 (PR #2) |
| 5 | 10:52:16 | push | a6dc51d | 26506774129 | completed | **success** | 42 (false-positives 정정 first GREEN) |
| 4 | 07:36:49 | pull_request | da9a25c | 26497643238 | completed | **failure** | 41 (permissions 정합 정정, secret-scanner 여전 FAIL) |
| 3 | 07:36:46 | push | da9a25c | 26497641173 | completed | **failure** | 41 (동형) |
| 2 | 07:27:04 | pull_request | c93085c | 26497204025 | completed | **failure** | 40 (D-6 첫 발효, FAIL 2 종류) |
| 1 | 07:27:02 | push | c93085c | 26497202700 | completed | **failure** | 40 (D-6 첫 발효 push) |

### 1.2 transition timeline

```
40 (c93085c) FAIL ×2 ── (workflow permissions + secret-scanner false positives 2 종류 검출)
   ↓
41 (da9a25c) FAIL ×2 ── (permissions PASS, secret-scanner 10 FP 여전)
   ↓
42 (a6dc51d) SUCCESS ×2 ── (R-1 (a+) + (V) layer1.py 회피 = 10/10 FP 해소, **첫 GREEN**) ⭐⭐⭐⭐
   ↓
43~47 SUCCESS ×10 ── (contexts 갱신 + PR #2 merge + branch sync + fp-edge-extensions + Node.js 24 마이그레이션)
```

### 1.3 SUCCESS 자격 발효 시점

- **첫 GREEN**: 42 entry `a6dc51d` push run 26506774129 (2026-05-27 10:52:16 UTC) — R-1 BLOCKING (a+) + (V) layer1.py 회피 흡수 효과 검증
- **본 시점 (47 entry 이후)**: 10 consecutive GREEN ✅ (안정성 확정)

### 1.4 R-MVP1-1.5-PC1-1 Rollback Trigger 메커니즘 작동 검증

- 40 entry 첫 발화 = FAIL 검출 = **Rollback Trigger 메커니즘 정확 작동 ✅**
- 본 trigger 발화 자체가 dev 환경 hook bypass 의심이 아닌 결과 차이 검출 (changed files vs all-files scope 차이)
- 본 cycle 진정한 Rollback Trigger 시나리오 (= dev 환경 hook bypass commit 검출) 아직 실 발화 0건

---

## §2 E-D6-2: nightly schedule 발화 (deferred)

### 2.1 schedule trigger 정의

- cron: `0 3 * * *` (UTC) = **KST 12:00 매일** (ST-2 nightly schedule 동시간대 답습)
- 본 workflow 발효일: 2026-05-27 07:27 UTC (40 entry `c93085c` push 시점)
- 첫 schedule 발화 예상: 2026-05-28 03:00 UTC (KST 12:00)

### 2.2 본 evidence 작성 시점 (2026-05-27 ~14:00 UTC)

- nightly schedule 발화 **0건** (workflow 발효일 = 본 evidence 작성일, 첫 cron 아직 미도래)
- **carry-over**: 다음 KST 12:00 이후 nightly schedule 첫 actual run id capture (자율 영역 후속 evidence)

### 2.3 schedule 발효 자격 검증

- workflow `on.schedule.cron: "0 3 * * *"` 답습 ✅
- GitHub Actions schedule trigger 정책 = 기본 발화 (private repo + active activity 있음)
- 본 repo 활성 (47 entry 11 commits 본 세션) = schedule 발화 자격 충분

---

## §3 E-D6-3: `pre-commit run --all-files` CI 실행 결과

### 3.1 `bypass-detect` step 본질

```yaml
- name: Run pre-commit on all files (bypass detection)
  run: |
    pre-commit run --all-files --show-diff-on-failure
```

- `pre-commit==4.0.1` (`bin/setup.sh` + 47 entry Node.js 24 호환 답습)
- `--all-files` = all repo files scan (dev 환경 changed files only 와 결과 차이 검출 메커니즘)
- `--show-diff-on-failure` = FAIL 시 root cause 빠른 식별

### 3.2 실행 결과 SUCCESS 시 (42~47 entry SUCCESS runs, 10건)

`bypass-detect` step 의 `pre-commit run --all-files` 출력 (6 hooks 모두 PASS):

```
Secret Scanner (R-4.1 Tier-1 45 patterns)............................Passed
Workflow Secrets Usage Check (G3-7 (i) F-금지)......................Passed
Workflow Permissions Check (G3-7 (v) R-6 default-deny)..............Passed
Provider Import Scanner (Group A 1차 AST 5종 패턴)...................Passed
Provider URL/Model Scanner (URL Tier-1 10 + Model Tier-1 19).........Passed
Import Linter (T-2 contract TR-1~TR-5)...............................Passed
```

→ **6/6 hooks PASS** (47 entry 시점 + 본 evidence 작성 시점 답습)

### 3.3 실행 결과 FAIL 시 분석 (40~41 entry FAIL runs, 4건)

**40 entry (c93085c)**:
- `Secret Scanner` FAIL → 10 violations (src/jarvis/{layer1,worker}.py false positives)
- `Workflow Permissions Check` FAIL → 1 violation (본 workflow 자체 `permissions:` 부재 정합 결함)

**41 entry (da9a25c)**:
- `Workflow Permissions Check` **PASS** (`permissions: contents: read` 추가 정정)
- `Secret Scanner` 여전 FAIL → 10 violations (pre-existing false positives)

**42 entry (a6dc51d)**:
- `Secret Scanner` **PASS** (R-1 (a+) prefix `(?:^|[?&\s'"])` + layer1.py tuple sort 회피)
- 모든 hooks PASS = **첫 GREEN** ⭐⭐⭐⭐

---

## §4 종합 evidence 매트릭스

| Evidence ID | 영역 | 상태 | source |
|---|---|---|---|
| **E-D6-1** | workflow 발화 actual run id + status | ✅ 14 runs capture (FAIL 4 + SUCCESS 10) | §1 |
| **E-D6-2** | nightly schedule 첫 발화 | ⏳ deferred (2026-05-28 03:00 UTC 이후 capture, carry-over) | §2 |
| **E-D6-3** | `pre-commit run --all-files` CI 실행 결과 | ✅ SUCCESS time 6/6 hooks PASS + FAIL time 2 종류 violation 분류 | §3 |

→ **E-D6-1 ✅ + E-D6-3 ✅ + E-D6-2 ⏳ (carry-over)** = 2/3 evidence 즉시 capture, 1/3 시간 경과 의존 carry-over

---

## §5 ADR-011 §2.1 (b)(d) 회귀 자격 evidence

| 조건 | 충족 evidence |
|---|---|
| **(b) 격리 환경 PoC 실증** | 본 evidence §1 14 runs + §3.3 transition timeline = D-6 workflow 격리 환경 (CI runner) PoC 완전 발효 |
| **(d) 자동 회귀 검증** | 본 evidence §1.4 + §3 = R-MVP1-1.5-PC1-1 Rollback Trigger 메커니즘 작동 검증 ✅ |

→ **PC-1-T3 (b)(d) 회귀 자격 보강 evidence 답습 완전 충족** (33 entry MVP-1 PASS 전체 답습 유지, 본 cycle = 보강 한정)

---

## §6 carry-over (본 evidence 외)

- (b1-PC1-D6-evidence-nightly) nightly schedule 첫 발화 actual run id capture (자율 영역, 2026-05-28 이후)
- (b1-PC1-D6-evidence-workflow-dispatch) workflow_dispatch 수동 발화 evidence (선택, 47 entry codex 권고 1 답습)
- (b1-AR3 develop) develop branch 생성 시점 8 contexts 적용 (사용자 영역)

---

## §7 자기진단 (5/5)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 답습 출처 4 source + 40~47 entry chain 답습 | ✅ |
| 2 | E-D6-1 14 runs full timeline + transition (FAIL→GREEN 시점) | ✅ |
| 3 | E-D6-3 SUCCESS/FAIL 분류 + 6 hooks 매트릭스 + R-MVP1-1.5-PC1-1 작동 검증 | ✅ |
| 4 | E-D6-2 deferred + carry-over 명문 + schedule 발효 자격 검증 | ✅ |
| 5 | ADR-011 (b)(d) 회귀 자격 evidence 충족 + 본 evidence 자율 영역 (PASS 효과 영향 0) | ✅ |
