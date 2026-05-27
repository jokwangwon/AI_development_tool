# MVP-1 ST-2 inotify sidecar 실 구현 sub-cycle brief

> **scope**: MVP-1 1.5차 보강 entry 합의 (24번째 entry, commit `9638521`) 의 **ST-2 inotify sidecar 실 구현 sub-cycle**. 본 sub-cycle = entry 합의 결정 *집행* + **nightly schedule 보강 + R-5 3 단계 evidence 명문 cross-check 한정** (인프라 대부분 이미 발효, 23번째 entry audit 한정 패턴 답습).
>
> **본 brief 자체에서 실 코드 / docker-compose / Dockerfile / hook 본문 변경 0건 의무** — brief 합의 발효 *후* 별도 실 구현 단계에서 `.github/workflows/` 보강 + 명문 cross-check.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **24번째 entry brief v1.1** | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (`9638521`) | §2.2 ST-2 정의 (line 151~179) + §3 ADR-011 (b)(d) ST-2 cell (line 259/261) + §4 합의 형태 권고 (line 290 framing) + §5.1 R-MVP1-1.5-ST2-{1,2,3} (line 326~328, R-7(a) 정정 이미 흡수 — "합의된 threshold 초과") + §6 Evidence 행 |
| **24번째 entry 합의 보고서** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | R-5 BLOCKING (3 단계 evidence: (1) event 인지 + (2) sidecar→메인 정지 + (3) 메인 workload fail-closed) + R-7(a) (이미 entry brief v1.1 흡수) |
| **Backlog #1 합의** | `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` | ST-2 단독 우선 권고 (T3 자동 진입 0건 유일) + T2 영역 + 단축 합의 + 사용자 명시 결정 *또는* 보수적 풀 3+1 합의 |
| **ST-2 PoC 발효** | `docker/gp3-st2-poc/`, `tools/docker_secret_inotify_sidecar_check.sh`, `tests/fixtures/gp3_st2/` | Cycle 3 commit + Cycle 4 CI tool 발효 답습 (사용자 명시 9 결정 답습) |
| **현 workflow step** | `.github/workflows/secret-hygiene-egress-redaction.yml` line 663 | "Backlog #1 ST-2 inotify sidecar PoC check (Cycle 4 entry — F-B + F-C 검증)" step 이미 발효 |
| **PC-1 + S-3 sub-cycle 답습** | `3a63a5b` + `4451716` | Reviewer-only 단축 합의 패턴 + 변경 0건 의무 매트릭스 + 6단계 cycle 답습 |
| **23번째 entry 답습** | audit 한정 패턴 — 권위 표시 격상 한정 (`51aa964`) | 인프라 대부분 발효 시 sub-cycle = audit + 가벼운 보강 |

---

## §1 scope (ST-2 sub-cycle 한정)

### 1.1 본 sub-cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | ST-2 inotify sidecar nightly schedule 보강 + R-5 3 단계 evidence 명문 cross-check (entry 합의 결정 *집행*, 인프라 추가 0건) |
| **영역** | GP-3 ST-2 (런타임 secret 저장 경로 inotify 감시) |
| **합의 형태 권고** | **단축 합의 + 사용자 명시** (entry brief line 290 framing + PC-1/S-3 sub-cycle 패턴 답습) |
| **변경 0건 의무** | `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` 본문 0 / `docker/gp3-st2-poc/Dockerfile` 본문 0 / `docker/gp3-st2-poc/watch-secrets.sh` 본문 0 / `docker/gp3-st2-poc/hermes-mock/` 본문 0 / `tools/docker_secret_inotify_sidecar_check.sh` 본문 0 / `tests/fixtures/gp3_st2/` 본문 0 / `.pre-commit-config.yaml` 본문 0 / src/ 0 / Hermes upstream Dockerfile 0 / `.githooks/` 본문 0 |
| **변경 허용 영역** | `.github/workflows/secret-hygiene-egress-redaction.yml` `on:` 에 nightly schedule 추가 한정 (기존 22 step + line 663 ST-2 step 본문 변경 0건) |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` 본문 변경 (사용자 명시 9 결정 답습) | 0건 |
| 2 | `docker/gp3-st2-poc/Dockerfile` (sidecar image, inotify-tools 의존성) | 0건 (이미 발효) |
| 3 | `docker/gp3-st2-poc/watch-secrets.sh` 본문 변경 | 0건 |
| 4 | `docker/gp3-st2-poc/hermes-mock/` 본문 변경 | 0건 |
| 5 | `tools/docker_secret_inotify_sidecar_check.sh` 본문 변경 (258줄 답습) | 0건 |
| 6 | `tests/fixtures/gp3_st2/` 본문 변경 (5 fixture 답습) | 0건 |
| 7 | Hermes upstream Dockerfile 변경 | 0건 (R-MVP1-1.5-ST2-2 풀 3+1 trigger 답습) |
| 8 | `.github/workflows/secret-hygiene-egress-redaction.yml` 기존 22 step + ST-2 step (line 663) 본문 변경 | 0건 (보강 = `on:` schedule 추가 한정) |
| 9 | inotify event 응답 시간 *threshold 고정* (<1초 / <500ms 등) | 0건 (R-MVP1-1.5-ST2-1 답습 — threshold 후보 framing 보존, 별도 합의) |
| 10 | sidecar production 적용 (Hermes runtime 통합) | 0건 (R-MVP1-1.5-ST2-3 Operational Readiness PASS 영역 답습) |
| 11 | branch protection rule 변경 | 0건 (AR-3 sub-cycle 영역) |
| 12 | ADR / 헌법 / roadmap 본문 변경 | 0건 |
| 13 | MVP-1 Implementation Evidence PASS 발효 | 0건 ((c) carry-over 영역) |
| 14 | `adapters/llm/facade.py` placeholder → real | 0건 ((d) carry-over 영역) |

---

## §2 24번째 entry BLOCKING + 권고 흡수 매트릭스

| ID | 항목 | 본 brief 흡수 위치 |
|---|---|---|
| **R-5** BLOCKING | ST-2 3 단계 evidence 의무: (1) event 인지 + (2) sidecar→메인 정지 signal + (3) 메인 workload fail-closed 확인 | §3.2 현 발효 상태 cross-check 표 (3/3 단계 모두 이미 발효 자격 검증) — 본 brief 명문 cross-check 한정, 추가 인프라 변경 0건 |
| **R-7(a)** BLOCKING | R-MVP1-1.5-ST2-1 ">1초" → "합의된 threshold 초과" framing 정정 | entry brief v1.1 (`9638521`) line 326 에 이미 흡수 완료 ("합의된 threshold 초과 (threshold 후보 = <1초 / <500ms 등, 별도 합의 영역, R-7 BLOCKING 흡수)"). 본 sub-cycle 추가 정정 0건 |
| **권고** | ST-2 APPROVE w/ COND 격상 (entry 합의 §1 line 36 답습) — 본 sub-cycle = COND 해소 (R-5 명문 cross-check + nightly 보강) | 본 brief 전체 |

---

## §3 현 상태 audit (ST-2 인프라 발효 매트릭스)

### 3.1 이미 발효 (답습 영역, 변경 0건 의무)

| 자료 | 상태 | source |
|---|---|---|
| `tools/docker_secret_inotify_sidecar_check.sh` (258줄, Cycle 4 답습) | ✅ 발효 | 5 fixture 일관 verify (`run_fixture` 함수 line 117~231) + status tag + hermes-mock health 양쪽 비교 |
| `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` (137줄, Cycle 3 답습) | ✅ 발효 | 3 service (fixture-init + inotify-sidecar + hermes-mock) + F-B primary + F-C 보조 + F-A 비채택 |
| `docker/gp3-st2-poc/watch-secrets.sh` (73줄) | ✅ 발효 | inotifywait 5 event 감시 (attrib/modify/delete/move/delete_self/move_self) + status file write |
| `docker/gp3-st2-poc/hermes-mock/{Dockerfile, healthcheck.sh, README.md}` | ✅ 발효 | healthcheck = status file read → unhealthy 처리 |
| `docker/gp3-st2-poc/scripts/run-poc-fixture.sh` | ✅ 발효 | helper 스크립트 |
| `docker/gp3-st2-poc/Dockerfile` (sidecar image, inotify-tools + procps 의존성) | ✅ 발효 | Cycle 3 답습 |
| `tests/fixtures/gp3_st2/{pass/{normal_operation, init_phase}, fail/{chmod_644, content_modified, file_deleted}}` (5 fixture) | ✅ 발효 | Cycle 2 답습 |
| `.github/workflows/secret-hygiene-egress-redaction.yml` line 663 `st2_inotify_sidecar` step | ✅ 발효 | `tools/docker_secret_inotify_sidecar_check.sh` CI 호출 + self-check `--list-checks` |
| `on.push.paths` 필터에 `tests/fixtures/gp3_st2/**` + `tools/docker_secret_inotify_sidecar_check.sh` + `docker/gp3-st2-poc/**` | ✅ 발효 | line 38/41/45 답습 |

### 3.2 R-5 BLOCKING 3 단계 evidence 현 발효 cross-check

| 단계 | R-5 요구 | 현 발효 자격 (source) |
|---|---|---|
| **(1) event 인지** | inotify event 감지 (attrib/modify/delete/move/delete_self/move_self) | ✅ `watch-secrets.sh` line 63~67 `inotifywait -m -e attrib,modify,delete,move,delete_self,move_self` |
| **(2) sidecar → 메인 정지 signal** | sidecar status file write → hermes-mock healthcheck fail | ✅ `watch-secrets.sh` line 70 `echo "UNHEALTHY: $event $path $ts" > "$STATUS_FILE"` + `docker-compose.gp3-st2.yml` line 122~127 `hermes-mock healthcheck` |
| **(3) 메인 workload fail-closed 확인** | hermes-mock unhealthy 상태 verify (메인 workload exit status check 또는 healthcheck fail) | ✅ `docker_secret_inotify_sidecar_check.sh` line 199~212 `docker inspect gp3-st2-hermes-mock --format='{{.State.Health.Status}}'` 비교 + 5 fixture 모두 expected health (`healthy` / `unhealthy`) assertion |

→ **R-5 3 단계 evidence 모두 이미 발효 자격 충족** (본 brief 명문 cross-check 한정, 추가 인프라 변경 0건)

### 3.3 미충족 (본 sub-cycle 발효 대상)

| # | 항목 | 현 상태 | 본 sub-cycle 발효 |
|---|---|---|---|
| 1 | nightly schedule 발화 (workflow `on:` 에 `schedule: cron`) | 부재 (현재 = push trigger 만) | `.github/workflows/secret-hygiene-egress-redaction.yml` `on:` 에 `schedule:` 추가 (D-2 결정 — cron 시간) |
| 2 | R-5 3 단계 evidence 명문 cross-check (§3.2 표) | 0건 (인프라 발효, 명문 0건) | 본 brief §3.2 + 합의 보고서 §3.2 본문 채택 |
| 3 | ST-2 sub-cycle 발효 자격 명문 (PC-1/S-3 패턴 답습) | 0건 | 본 brief + 합의 보고서 commit |

### 3.4 R-MVP1-1.5-ST2-{1,2,3} Rollback Trigger 현 상태 답습

| ID | trigger | 현 답습 자격 |
|---|---|---|
| **R-MVP1-1.5-ST2-1** | inotify event 응답 시간 = 합의된 threshold 초과 | entry brief v1.1 line 326 답습 (R-7(a) 흡수 완료, framing "합의된 threshold 초과" — threshold 후보 = <1초 / <500ms 등, 별도 합의) |
| **R-MVP1-1.5-ST2-2** | Hermes upstream Dockerfile 변경 의무 발생 | 본 sub-cycle 영역 외 (Hermes upstream 변경 0건 영구 의무, R-7(b) 답습) |
| **R-MVP1-1.5-ST2-3** | sidecar process 운영 부담 / failure mode 발견 | 본 sub-cycle 영역 외 (Operational Readiness PASS Layer E 영역 답습, Backlog #7) |

---

## §4 실 구현 항목 (단순 — nightly schedule 추가 1건 한정)

### 4.1 `.github/workflows/secret-hygiene-egress-redaction.yml` `on:` 보강

**현 상태**:
```yaml
on:
  push:
    branches: [main, develop, "feature/**"]
    paths: [...]
  pull_request:
    branches: [main, develop]
```

**보강 후**:
```yaml
on:
  push:
    branches: [main, develop, "feature/**"]
    paths: [...]
  pull_request:
    branches: [main, develop]
  schedule:
    # nightly UTC 03:00 (KST 12:00, D-2 결정 답습)
    # ST-2 inotify sidecar PoC 일관 발화 의무 + S-3 detect-secrets 일관 발화
    # R-5 BLOCKING (b)(d) 답습 — docker-compose sidecar nightly run
    - cron: "0 3 * * *"
```

**제약**: `on.push.paths` + `on.pull_request` 본문 변경 0건 (schedule 추가 한정). 기존 22 step + ST-2 step 본문 변경 0건.

---

## §5 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (ST-2 본 sub-cycle 한정)

| 조건 | 본 sub-cycle 충족 |
|---|---|
| **(a)** 사용자 명시 결정 | ⏳ 본 brief 사용자 승인 + D-1~D-3 결정 시 충족 |
| **(b)** 격리 환경 PoC 실증 | ✅ **이미 발효** (5 fixture + tool 5/5 verify, §3.1 답습) — R-5 3 단계 evidence 모두 발효 자격 (§3.2 답습) |
| **(c)** 도구/리소스 stateless · network-free | ✅ docker-compose 격리 영역 한정 (`mock-secrets-vol` + `sidecar-status-vol` named volume + cap_drop ALL + no-new-privileges) — Hermes upstream 0건, production docker-compose 0건 |
| **(d)** 자동 회귀 검증 경로 | ⏳ 본 sub-cycle 발효 시 nightly schedule 추가 → `tools/docker_secret_inotify_sidecar_check.sh` nightly run (현재 = push trigger 한정) |
| **(e)** 합의 APPROVE 운영조건 | ⏳ 본 brief 합의 (단축 합의 + 사용자 명시 권고) APPROVE 시 발효 |

→ **현 시점 충족 = (b)(c) 2/5** → 본 sub-cycle 합의 발효 + 실 구현 (nightly schedule 추가) 완료 = (a)~(e) 5/5 충족 (ST-2 영역 한정)

---

## §6 Rollback Trigger (본 sub-cycle 적용 형태)

§3.4 답습 — 본 sub-cycle 추가 trigger 0건. R-MVP1-1.5-ST2-{1,2,3} 모두 entry brief v1.1 line 326~328 답습 유지.

---

## §7 Evidence

| Evidence | 형식 | 본 sub-cycle 발효 |
|---|---|---|
| **(a) Markdown report** | `docs/phase0/g2-gp3-mvp1-evidence.md` 보강 (ST-2 영역 추가) | 별도 sub-cycle 또는 본 sub-cycle 확장 결정 |
| **(b) PoC 실증** | 5 fixture verify + R-5 3 단계 evidence (§3.2 답습) | **이미 발효** (Cycle 3+4) |
| **(c) Docker isolation log** | docker-compose 격리 (mock-secrets-vol + sidecar-status-vol + cap_drop) | **이미 발효** |
| **(d) GitHub Actions run** | nightly actual run id (현재 = push trigger run id 만) | 본 sub-cycle 발효 시 nightly schedule actual run id 추가 |
| **(e) 합의 보고서** | 본 sub-cycle 합의 보고서 (단축 합의 권고) | 본 brief 합의 발효 |

---

## §8 사용자 결정 항목 (brief 합의 진입 전 의무)

| # | 항목 | 후보 | 권고 |
|---|---|---|---|
| **D-1** | 합의 형태 | (i) 단축 합의 (Reviewer-only) / (ii) 풀 3+1 / (iii) 풀 3+1 + 외부 LLM 1+ | **(i) 단축 합의 (Reviewer-only)** — entry brief line 290 답습 + entry cycle 에서 ST-2 채택 결정 + 3 단계 evidence 인프라 발효 완료, 본 sub-cycle = 결정 *집행* + 명문 cross-check + nightly 보강 한정. PC-1/S-3 패턴 답습 |
| **D-2** | nightly cron 시간 | (i) `0 3 * * *` (UTC 03:00 = KST 12:00) / (ii) `0 18 * * *` (UTC 18:00 = KST 03:00) / (iii) `0 0 * * *` (UTC 00:00 = KST 09:00) | **(i) UTC 03:00 = KST 12:00** — 한국 업무 시간 중 발화 (사용자 인지 + 신속 대응 자격), GitHub Actions runner 한가 시간대 (`* */6 * * *` 같은 고빈도 제외 = nightly 답습) |
| **D-3** | (a) Markdown report 보강 시점 | (A) 본 sub-cycle 확장 — `docs/phase0/g2-gp3-mvp1-evidence.md` 동시 보강 / (B) 별도 sub-cycle (evidence 통합 영역) | **(B) 별도 sub-cycle** — Ceremony 최소화 + evidence 통합 = (b1) 4 sub-cycle 완료 후 일관 보강 권고 (각 sub-cycle = scope 한정 답습) |

---

## §9 합의 형태 권고 + 다음 단계

### 9.1 합의 형태 권고

**단축 합의 (Reviewer-only)** 권고 — 근거 (PC-1/S-3 sub-cycle 패턴 답습):

| 근거 | 내용 |
|---|---|
| **entry brief line 290** | "단축 합의 + 사용자 명시 (사용자 명시 결정 1회)" framing |
| **entry cycle 완료** | ST-2 채택 결정 + APPROVE w/ COND (R-5 BLOCKING 흡수) 자체는 24번째 entry cycle (`9638521`) 에서 완료. 본 sub-cycle = 결정 *집행* + R-5 명문 cross-check |
| **인프라 발효 완료** | Cycle 3 + Cycle 4 답습 — docker-compose + watch-secrets.sh + hermes-mock + 5 fixture + CI step 모두 이미 발효. 본 sub-cycle scope = nightly schedule 1 보강 + 명문 cross-check 한정 |
| **변경 0건 의무** | docker-compose / Dockerfile / watch-secrets.sh / hermes-mock / 5 fixture / tools 본문 모두 0건. 변경 = workflow `on:` schedule 추가 1 항 한정 |
| **풀 3+1 승격 trigger** | 5/5 모두 발화 0건 (① 새 권위 결정 0 [ST-2 채택 = entry cycle] / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0) |
| **PC-1/S-3 답습** | PC-1 (`3a63a5b`) + S-3 (`4451716`) Reviewer-only 단축 합의 패턴 답습 |
| **23번째 entry 답습** | audit 한정 cycle 패턴 — 인프라 발효 완료 시 sub-cycle = audit + 가벼운 보강 (`51aa964`) |

### 9.2 다음 단계 (단계별 합의 cycle 6단계 답습)

1. ✅ **brief 작성** (본 단계, 본 commit)
2. ⏳ **사용자 승인** — §8 D-1~D-3 사용자 결정 의무
3. ⏳ **단축 합의** — Reviewer-only 합의 보고서 작성 (5/5 풀 3+1 승격 trigger 발화 검증 + R-5 3 단계 evidence cross-check 명문)
4. ⏳ **실 구현** — §4 `on:` schedule 추가 1 항
5. ⏳ **commit** — 본 sub-cycle 정리 commit (SESSION + INDEX + 본 commit)
6. ⏳ **push** — 사용자 명시 의무 답습 (workflow scope = Claude OAuth 거부, S-3 답습)

---

## §10 본 brief 자기진단 (8/8 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 본 brief 자체 실 코드 / docker-compose / Dockerfile / hook 본문 변경 0건 | ✅ brief 작성 한정 |
| 2 | ST-2 인프라 (docker-compose + watch-secrets.sh + hermes-mock + 5 fixture + tool 258줄) 본문 변경 0건 명문 | ✅ §1.2 + §3.1 |
| 3 | R-5 BLOCKING 3 단계 evidence 현 발효 cross-check 명문 | ✅ §3.2 |
| 4 | R-7(a) 정정 entry brief v1.1 흡수 완료 답습 (본 sub-cycle 추가 정정 0건) | ✅ §2 + §3.4 |
| 5 | Hermes upstream Dockerfile 변경 0건 영구 의무 답습 (R-MVP1-1.5-ST2-2) | ✅ §1.2 #7 |
| 6 | sidecar production 적용 0건 (R-MVP1-1.5-ST2-3 Operational Readiness PASS 영역 답습) | ✅ §1.2 #10 |
| 7 | ADR-011 (a)~(e) 매트릭스 발효 자격 명시 ((b)(c) 2/5 발효 + 본 sub-cycle = 5/5) | ✅ §5 |
| 8 | 사용자 결정 항목 명시 (D-1~D-3) + 합의 형태 권고 명시 + 23번째 entry audit 한정 패턴 답습 | ✅ §8 + §9.1 |

---

> **본 brief 발효 시점** = 사용자 승인 (§8 D-1~D-3 결정) + Reviewer-only 단축 합의 APPROVE + 본 brief commit. 본 brief 자체 = **nightly schedule 보강 + R-5 명문 cross-check 권한 발효 자격** 한정.
