# G2 GP-3 — Credential / Secret Hygiene MVP-1 Implementation Evidence (통합)

> **본 문서 = GP-3 MVP-1 Implementation Evidence PASS 발효 (33번째 entry, 2026-05-27) evidence 통합**. ADR-011 §2.1 (a)~(e) 5 조건 + (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2) + AR-3 (GP-3+GP-5 통합) + 첫 PR evidence + R-S1 cross-reference 정정 cascade 답습.
>
> **scope**: GP-3 영역 한정 (GP-5 = `g2-gp5-mvp1-evidence.md` 별도, GP-2 = MVP-2 영역 답습). PoC evidence (Group D) = `g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` 답습.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| 33번째 entry MVP-1 PASS 발효 합의 | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` | APPROVE WITH CONDITIONS (풀 3+1 + 외부 LLM 1+, BLOCKING 6 + 권고 5 1pass 흡수) |
| 24번째 entry brief v1.1 | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` | MVP-1 1.5차 보강 entry brief (4 sub-수단 진입 합의) |
| 26번째 entry PC-1-T3 sub-cycle | `docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md` + 합의 + commit `3a63a5b` | dev 환경 hook 의무화 + bin/setup.sh + CONTRIBUTING.md + audit log + bypass detection |
| 27번째 entry S-3 sub-cycle | `docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md` + 합의 + commit `4451716` | detect-secrets Tier-1 plugin 5종 + 6 fixture + workflow 3 step + Defense in depth S-1+S-3 |
| 28번째 entry ST-2 sub-cycle | `docs/phase0/mvp1-st2-inotify-sidecar-brief.md` + 합의 + commit `1edc5bb` | inotify sidecar nightly schedule + R-5 3 단계 evidence 명문 |
| 29-31번째 entry AR-3 sub-cycle | `docs/phase0/mvp1-ar3-pr-auto-reject-brief.md` + 합의 + chain `7f57323` + `7c294bb` + `73ed20d` + `9837298` | branch protection 7 contexts 발효 + 첫 PR evidence |
| 33번째 entry PASS 발효 brief v1.1 | `docs/phase0/mvp1-implementation-evidence-pass-activation-brief.md` | GP-3 5/5 매트릭스 + Defense in depth cross-cover + R-S1 carry-over 답습 |
| 34번째 entry paths-aware audit | `docs/phase0/mvp1-paths-aware-workflow-audit-evidence.md` + commit `5f876ea` | 11 workflow 추가 paths-aware risk 0건 |
| 35-38번째 entry R-S1 cascade | `mvp1-r-s1-{framing-correction,roadmap-correction,b2-others,b2-massive}-{brief,evidence}.md` + 198 위치 정정 | R-S1 cross-reference 영원 종결 |
| roadmap-mvp1 §2.2 + §3 | `docs/architecture/implementation-runtime-roadmap-mvp1.md` | MVP-1 Exit 기준 + GP-3 영역 본문 |

---

## §1 GP-3 ADR-011 §2.1 (a)~(e) 5 조건 evidence 매트릭스

### 1.1 (a) 동등 이상의 보안 결과 ✅

**다층 발효 = Defense in depth 답습**:
- **S-1** (Group D scanner, R-4.1 Tier-1 45 patterns) — `tools/secret_scanner.py` (368줄) 발효 (R-MVP1-1.5-S3-3 영구 의무 답습)
- **S-3** (detect-secrets Tier-1 plugin 5종) — 27번째 entry sub-cycle 발효 (Defense in depth, R-MVP1-1.5-S3-1 Tier-2/3 확장 풀 3+1 trigger 답습)
- **ST-2** (inotify sidecar) — 28번째 entry sub-cycle 발효 (Cycle 3+4 인프라 답습)
- **PC-1** (pre-commit framework 의무화 T3) — 26번째 entry sub-cycle 발효

→ **R-4.1 Tier-1 42 catalog 답습 동등 이상** 충족 자격 자격.

### 1.2 (b) 격리 환경 PoC 실증 ✅

- docker secret + chmod 600 + entrypoint stat — Group D PoC 답습 (ADR-008 차단조건 #6 답습)
- ST-2 inotify (저장 경로) PoC — `docker/gp3-st2-poc/` (Cycle 3 답습)
- S-3 detect-secrets PR auto-reject (코드) PoC — `tests/fixtures/secret_hygiene/mvp1_s3/` 6 testfile 발효
- **31번째 entry 첫 PR PASS evidence** (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`):
  - `scan` (secret-hygiene-egress-redaction) 5m37s SUCCESS = S-1 + S-3 + ST-2 모든 step PASS
  - 11/11 check_runs SUCCESS + mergeable CLEAN
- Defense in depth cross-cover 답습 (33번째 entry §3.1 답습) — PC-1 PoC evidence 자율 영역 (carry-over)

### 1.3 (c) ADR / SDD 권위 명시 ✅

**multi-source 재기술 (35-38번째 R-S1 cascade 답습)**:
- ADR-008 차단조건 #1 (SQLCipher)
- ADR-008 차단조건 #6 (Docker 격리 + egress 화이트리스트)
- ADR-008 부록 B (Hermes PMO 격상 절차 + cross-reference Amendment)
- ADR-010 (SQLCipher Vault)
- ADR-011 (수단/목적 분리 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e))
- R-4 (Tier-1 42 catalog)
- roadmap-mvp1 §3 (GP-3 MVP-1 Deepening)
- 헌법 8조 #1 (보안 권위)
- (b1) 4 sub-cycle brief + 합의 본문 (PC-1 / S-3 / ST-2 / AR-3) — 모두 발효

→ R-S1 cross-reference (ADR-008 §A.2 R1-2 / §2.6.4 R1-2 / §2.6.2 R2-1 손상 인용) = 35-38번째 entry chain 정정 = **영원 종결 ✅** (198 위치 정정 완료). ADR-008 본문 변경 0건 영구 의무 답습 (R-MVP1-PASS-2).

### 1.4 (d) 자동 회귀 검증 경로 ✅

- `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄, 24 step) — S-1 11+ step + S-3 3 step (27번째 entry) + ST-2 step (line 663) + Stage 2/4/5 step
- `on:` schedule `cron: "0 3 * * *"` (28번째 entry) — UTC 03:00 = KST 12:00 nightly
- `on.push.paths` 필터 — S-3 신규 path (`tests/fixtures/secret_hygiene/mvp1_s3/**` + `requirements-dev.txt`) 추가
- 31번째 entry 첫 PR actual run id evidence (run id `26491332306` 답습)
- 34번째 entry paths-aware audit — 추가 risk 0건 ✅
- AR-3 branch protection rule (30번째 entry, 31번째 entry catalog 정정) — 7 contexts, `enforce_admins: true`, `required_status_checks: strict` 답습

### 1.5 (e) 합의 APPROVE 운영조건 ✅

- 24번째 entry brief APPROVE WITH CONDITIONS (풀 3+1 + 외부 LLM 1+, codex via tmux cross-vendor)
- (b1) 4 sub-cycle 모두 APPROVE (Reviewer-only 단축 합의, 26-29 entry)
- 33번째 entry MVP-1 PASS 발효 합의 APPROVE WITH CONDITIONS (풀 3+1 + 외부 LLM 1+, BLOCKING 6 + 권고 5 1pass 흡수)
- 34번째 entry paths-aware audit (1-agent 직접 + 단축 합의 자격)
- 35-38번째 entry R-S1 cascade 정정 (단축 합의 + 사용자 명시 + sed 일괄)

→ **GP-3 5/5 충족 자격 자격 자격 ✅** (33번째 entry MVP-1 PASS 완전 발효 (α) 답습).

---

## §2 (b1) 4 sub-cycle 영역 evidence 통합

### 2.1 PC-1-T3 (26번째 entry, `3a63a5b`)

| 항목 | 발효 |
|---|---|
| brief | `mvp1-pc1-t3-mandatory-enforcement-brief.md` (288줄, 10장 자기진단 8/8) |
| 합의 | `3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md` (Reviewer-only 단축) |
| 실 file | `README.md` (하네스 인프라 표 + 초기 설정) + `CONTRIBUTING.md` 신규 (134줄) + `bin/setup.sh` (chmod +x, 4단계) + `requirements-dev.txt` (`pre-commit==4.0.1`) + `tools/pre_commit_install_audit.sh` (chmod +x, 3 탐지 경로) |
| Defense in depth | PC-1 (dev hook) + PC-3 (CI step 답습) + AR-3 (branch protection) 3 계층 |
| carry-over | PoC evidence 자율 (사용자 dev 환경 영역) + (b1-PC1-D6) bypass detection CI 통합 |

### 2.2 S-3 (27번째 entry, `4451716`)

| 항목 | 발효 |
|---|---|
| brief | `mvp1-s3-detect-secrets-partial-integration-brief.md` (303줄, 10장 자기진단 8/8) |
| 합의 | `3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md` (Reviewer-only 단축) |
| 실 file | `requirements-dev.txt` (`detect-secrets==1.5.0`) + `tests/fixtures/secret_hygiene/mvp1_s3/` 6 testfile (1 PASS + 5 FAIL) + `.github/workflows/secret-hygiene-egress-redaction.yml` (S-3 3 step + paths 2 entry) |
| 검출 plugin (Tier-1 답습 5종 한정) | `AWSKeyDetector` + `KeywordDetector` + `Base64HighEntropyString` + `HexHighEntropyString` + `PrivateKeyDetector` (R-MVP1-1.5-S3-1 Tier-2/3 풀 3+1 trigger 답습) |
| baseline | 영구 금지 (R-MVP1-1.5-S3-2 silenceable risk, CI assertion 발효) |
| Defense in depth | S-1 (Group D 45 patterns 답습) + S-3 (Tier-1 plugin 5종) |
| 31번째 entry 첫 PR fix | `73ed20d` — `aws_key.py` fixture 19자 → 20자 정정 (AWSKeyDetector regex `AKIA[0-9A-Z]{16}` 정확화) |

### 2.3 ST-2 (28번째 entry, `1edc5bb`)

| 항목 | 발효 |
|---|---|
| brief | `mvp1-st2-inotify-sidecar-brief.md` (227줄, 10장 자기진단 8/8) |
| 합의 | `3plus1-consensus-2026-05-27-mvp1-st2-inotify-sidecar.md` (Reviewer-only 단축) |
| 인프라 (Cycle 3+4 답습) | `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` (137줄) + `watch-secrets.sh` (73줄) + `hermes-mock/` + 5 fixture + `tools/docker_secret_inotify_sidecar_check.sh` (258줄) + workflow ST-2 step (line 663) |
| 실 변경 | workflow `on:` schedule `cron: "0 3 * * *"` 추가 1 항 한정 |
| R-5 3 단계 evidence | (1) event 인지 = watch-secrets.sh inotifywait 6 event / (2) sidecar → 메인 signal = status file + hermes-mock healthcheck / (3) 메인 fail-closed = tool docker inspect Health.Status 비교 |
| Hermes upstream | 변경 0건 영구 의무 (R-MVP1-1.5-ST2-2) |
| sidecar production | 적용 0건 (R-MVP1-1.5-ST2-3 Operational Readiness PASS 영역) |
| carry-over | nightly actual run id evidence 자율 (익일 KST 12:00 첫 nightly) |

### 2.4 AR-3 (29-31번째 entry, chain `7f57323` + `7c294bb` + `73ed20d` + `9837298`)

| 항목 | 발효 |
|---|---|
| 29 brief | `mvp1-ar3-pr-auto-reject-brief.md` (281줄, 10장 자기진단 8/8) |
| 29 합의 | `3plus1-consensus-2026-05-27-mvp1-ar3-pr-auto-reject.md` (Reviewer-only 단축, R-3 check name catalog + R-7(c) 차등 분리) |
| 30 사용자 admin scope | `gh api -X PUT branches/main/protection` 적용 (8 contexts 초기) + evidence file `mvp1-ar3-branch-protection-applied-evidence.md` |
| 31 첫 PR fix | `aws_key.py` fixture 정정 + contexts v2 (8→7 unique, R-4.1 r2-canary 제거) + 11/11 SUCCESS + mergeable CLEAN |
| 7 contexts (현 발효) | `guard` / `verify` / `feasibility` / `scan` / `enforce` / `defense` / `validate` (workflow name 미포함, job name 만) |
| 중복 동작 | `enforce` x3 + `scan` x3 = 모두 분리 처리 + 모든 동명 PASS 의무 답습 = race 0 확정 |
| admin bypass | `enforce_admins: true` + 0 시도 evidence |
| Defense in depth | PC-1 + PC-3 + AR-3 3 계층 결합 |
| develop branch | 부재 = carry-over (생성 시점 동일 7 contexts body PUT) |

---

## §3 첫 PR evidence (31번째 entry)

- PR #2 draft: https://github.com/jokwangwon/AI_development_tool/pull/2
- 18 commit (17 + fix 1), 56 file, +9686/-12 + 8/-6
- 첫 발화 (head `7c294bb`): 10 check_runs, 9 SUCCESS + 1 FAIL (scan/secret-hygiene S-3 step) + 1 미발화 (R-4.1 paths)
- fix commit (`73ed20d`): aws_key.py 19→20자 정정 + contexts v2 (R-4.1 제거)
- 재발화 (head `9837298befdeda6c7e170879cc9f15e331c52bce`): **11/11 SUCCESS + mergeable MERGEABLE + mergeStateStatus CLEAN ✅**
- 중복 동작 검증: race 0 확정 ✅
- admin bypass 0 시도 evidence

---

## §4 R-S1 cross-reference 정정 cascade 답습 (35-38번째 entry, 영원 종결)

| entry | scope | 위치 | 방식 |
|---|---|---|---|
| 35 | gov 6 + backlog1 3 + roadmap §3.6.3 framing 1 | **10** | Edit individual |
| 36 | roadmap-mvp1 본문 7 + mvp-1-to-6 1 + 2026-05-13-mvp1-pass 1 | **9** | Edit individual |
| 37 | 합의 historical 5 file 7 + CONTEXT.md 3 + st2-inotify-sidecar-entry 9 | **19** | Edit + replace_all |
| 38 | 50 file (자기언급 13 제외 + ADR-008 + hermes-adoption-design 제외) | **160** | sed 일괄 자동화 |
| **누적** | | **198 위치** | |

R-MVP1-PASS-2 영구 금지 답습 (ADR-008 본문 변경 0건) + R-MVP1-PASS-10 답습 (cross-reference 한정).

---

## §5 carry-over (자율 영역 evidence)

- PC-1-T3 PoC evidence: `bash bin/setup.sh` + `bash tools/pre_commit_install_audit.sh` 실 실행 evidence (사용자 dev 환경 영역, 자율)
- ST-2 nightly actual run id evidence: 익일 KST 12:00 nightly schedule 발화 후 `gh run list` (자율)
- (b1-AR3 develop) develop branch 생성 시점 동일 7 contexts body PUT (carry-over)
- (b1-PC1-D6) bypass detection CI 통합 (단축 합의 + 사용자 명시, 별도 sub-cycle)

---

## §6 본 evidence 자기진단 (5/5 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | ADR-011 §2.1 (a)~(e) 5/5 충족 evidence 명문 | ✅ §1 |
| 2 | (b1) 4 sub-cycle (PC-1 + S-3 + ST-2 + AR-3) 통합 evidence | ✅ §2 |
| 3 | 31번째 entry 첫 PR PASS evidence (head SHA `9837298`) | ✅ §3 |
| 4 | R-S1 cross-reference 정정 cascade 답습 (35-38 = 198 위치 영원 종결) | ✅ §4 |
| 5 | carry-over 자율 영역 evidence + PASS 효과 영향 0건 답습 | ✅ §5 |
