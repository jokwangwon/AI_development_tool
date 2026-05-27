# 단축 합의 보고서 (Reviewer-only) — MVP-1 ST-2 inotify sidecar 실 구현 sub-cycle

> **본 합의 = Reviewer-only 단축 합의**. 24번째 entry brief v1.1 (`9638521`) + 합의 보고서 (`3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md`) 의 ST-2 sub-cycle 합의 형태 권고 (entry brief line 290 framing) 답습. PC-1-T3 sub-cycle (`3a63a5b`) + S-3 sub-cycle (`4451716`) Reviewer-only 단축 합의 패턴 답습. 23번째 entry (`51aa964`) audit 한정 cycle 패턴 답습.

---

## §1 본 합의 자격 검증 (Reviewer-only 단축 합의)

### 1.1 풀 3+1 승격 trigger 5/5 발화 검증

| # | trigger | 본 sub-cycle 발화 |
|---|---|---|
| **①** | 새 권위 결정 (수단 결정 / threshold 고정 / Tier-2/3 catalog 확장 / ADR 본문 변경 / 헌법 변경) | ❌ 0건 — ST-2 채택 결정 + R-5 BLOCKING 흡수 자체는 24번째 entry cycle 에서 APPROVE w/ COND 완료. R-7(a) framing 정정도 entry brief v1.1 (`9638521`) line 326 흡수 완료. 본 sub-cycle = 결정 *집행* (nightly schedule 1 항 + R-5 명문 cross-check) |
| **②** | Tier-2/3 catalog 자동 확장 | ❌ 0건 — ST-2 = GP-3 런타임 감시 영역 (catalog 영역 외) |
| **③** | Implementation Evidence PASS 자동 선언 | ❌ 0건 — (c) carry-over 영역 |
| **④** | 후속 합의 본문 변경 (24번째 entry 합의 + 후속 backlog1/2 합의) | ❌ 0건 — 본 sub-cycle = entry 합의 결정 집행, 후속 합의 본문 변경 0건 |
| **⑤** | ADR-011 §2.1 5조건 자동 충족 선언 | ❌ 0건 — brief §5 매트릭스 (a)~(e) 5/5 = 본 brief 합의 발효 + nightly schedule 추가 시 충족, 자동 선언 0 |

→ **5/5 발화 0건 = Reviewer-only 단축 합의 자격 충족**

### 1.2 entry 합의 cross-check (verbatim 답습)

| Source | 위치 | verbatim |
|---|---|---|
| entry brief v1.1 line 290 | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` | "ST-2 ... 단축 합의 + 사용자 명시 (사용자 명시 결정 1회)" framing |
| entry 합의 보고서 §1 line 36 | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | "ST-2 ... APPROVE w/ COND" — 본 sub-cycle = COND 해소 (R-5 3 단계 evidence 명문 cross-check) |
| entry 합의 보고서 §6 R-5 | line 88 + §13.2 line 534 | "3 단계 evidence 의무 추가: (1) event 인지 + (2) sidecar → 메인 정지 signal + (3) **메인 workload fail-closed 확인**" — 본 sub-cycle §3.2 cross-check 흡수 |
| entry brief v1.1 line 326 | line 326 | R-7(a) 흡수 완료 — "합의된 threshold 초과 (threshold 후보 = <1초 / <500ms 등, 별도 합의 영역, R-7 BLOCKING 흡수)" |
| entry brief §3 line 261 ST-2 cell | line 261 | "docker-compose sidecar nightly run + `tools/docker_secret_inotify_sidecar_check.sh` nightly workflow 통합 + 메인 workload exit status assertion" — 본 sub-cycle §4 nightly schedule 추가 + §3.2 cross-check |

→ **entry 합의 답습 정확**

### 1.3 ST-2 인프라 발효 cross-check (23번째 entry audit 한정 패턴 답습)

| 인프라 | 발효 commit | 본 sub-cycle 변경 |
|---|---|---|
| `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` (137줄) | Cycle 3 답습 | ❌ 0건 |
| `docker/gp3-st2-poc/watch-secrets.sh` (73줄) | Cycle 3 답습 | ❌ 0건 |
| `docker/gp3-st2-poc/Dockerfile` (sidecar image, inotify-tools) | Cycle 3 답습 | ❌ 0건 |
| `docker/gp3-st2-poc/hermes-mock/{Dockerfile, healthcheck.sh}` | Cycle 3 답습 | ❌ 0건 |
| `tests/fixtures/gp3_st2/{pass/{normal_operation, init_phase}, fail/{chmod_644, content_modified, file_deleted}}` (5 fixture) | Cycle 2 답습 | ❌ 0건 |
| `tools/docker_secret_inotify_sidecar_check.sh` (258줄, 5 fixture verify + status tag + health 비교) | Cycle 4 답습 | ❌ 0건 |
| `.github/workflows/secret-hygiene-egress-redaction.yml` ST-2 step (line 663) | Cycle 4 답습 | ❌ 0건 |
| `on.push.paths` 필터 (tests/fixtures/gp3_st2/** + tools/docker_secret_inotify_sidecar_check.sh + docker/gp3-st2-poc/**) | 발효 답습 | ❌ 0건 (paths 본문 변경 0건) |

→ **인프라 8/8 발효 답습 + 변경 0건 검증**

---

## §2 본 brief §8 사용자 결정 답습 (D-1~D-3)

| # | 항목 | 사용자 결정 | 본 합의 답습 |
|---|---|---|---|
| **D-1** | 합의 형태 | 단축 합의 (Reviewer-only) (권고 채택) | 본 합의 = Reviewer-only 단축 합의 발효 |
| **D-2** | nightly cron 시간 | `0 3 * * *` (UTC 03:00 = KST 12:00) (권고 채택) | 실 구현 단계 = `.github/workflows/secret-hygiene-egress-redaction.yml` `on:` 에 `schedule: [{cron: "0 3 * * *"}]` 추가 |
| **D-3** | (a) Markdown report 보강 시점 | 별도 sub-cycle (권고 채택) | 본 sub-cycle scope = `docs/phase0/g2-gp3-mvp1-evidence.md` 보강 0건 (별도 sub-cycle 답습) |

→ **3/3 사용자 결정 명시** (D-1~D-3 모두 권고 채택)

---

## §3 R-5 BLOCKING 3 단계 evidence 발효 cross-check (본 합의 본문 채택)

| 단계 | R-5 요구 | 현 발효 source |
|---|---|---|
| **(1) event 인지** | inotify event 감지 (attrib/modify/delete/move/delete_self/move_self) | ✅ `docker/gp3-st2-poc/watch-secrets.sh` line 63~67 `inotifywait -m -e attrib,modify,delete,move,delete_self,move_self` (Cycle 3 답습) |
| **(2) sidecar → 메인 정지 signal** | sidecar status file write → hermes-mock healthcheck fail | ✅ `watch-secrets.sh` line 70 `echo "UNHEALTHY: $event $path $ts" > "$STATUS_FILE"` + `docker-compose.gp3-st2.yml` line 122~127 `hermes-mock healthcheck = /usr/local/bin/healthcheck.sh interval 5s timeout 3s retries 2` (Cycle 3 답습) |
| **(3) 메인 workload fail-closed 확인** | hermes-mock unhealthy 상태 verify (메인 workload exit status check 또는 healthcheck fail) | ✅ `tools/docker_secret_inotify_sidecar_check.sh` line 199~212 `docker inspect gp3-st2-hermes-mock --format='{{.State.Health.Status}}'` 비교 + 5 fixture 모두 expected health (`healthy` / `unhealthy`) assertion (Cycle 4 답습) |

→ **R-5 BLOCKING 3 단계 evidence 모두 이미 발효 자격 충족** (본 합의 명문 cross-check 발효, 추가 인프라 변경 0건)

---

## §4 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (본 합의 발효 시점)

| 조건 | 본 합의 발효 자격 |
|---|---|
| **(a)** 사용자 명시 결정 | ✅ 본 합의 시점 충족 (D-1~D-3 3/3 사용자 결정) |
| **(b)** 격리 환경 PoC 실증 | ✅ **이미 발효** (5 fixture + tool 5/5 verify + R-5 3 단계 evidence §3 모두 발효) |
| **(c)** 도구/리소스 stateless · network-free | ✅ docker-compose 격리 영역 한정 (named volume + cap_drop ALL + no-new-privileges + F-A 비채택 / docker socket 0건) — Hermes upstream 0건, production docker-compose 0건 |
| **(d)** 자동 회귀 검증 경로 | ⏳ 실 구현 단계 = nightly schedule 추가 → `tools/docker_secret_inotify_sidecar_check.sh` nightly run id evidence (현재 = push trigger 한정) |
| **(e)** 합의 APPROVE 운영조건 | ✅ 본 합의 APPROVE 시점 충족 |

→ **본 합의 발효 시점 = (a)(b)(c)(e) 4/5 충족** → **실 구현 단계 완료 시점 = (a)~(e) 5/5 충족** (ST-2 영역 한정)

---

## §5 변경 0건 의무 cross-check (brief §1.2 답습)

| # | 항목 | 본 합의 검증 |
|---|---|---|
| 1 | `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` 본문 | ❌ 0건 (사용자 명시 9 결정 답습) |
| 2 | `docker/gp3-st2-poc/Dockerfile` 본문 | ❌ 0건 |
| 3 | `docker/gp3-st2-poc/watch-secrets.sh` 본문 | ❌ 0건 |
| 4 | `docker/gp3-st2-poc/hermes-mock/` 본문 | ❌ 0건 |
| 5 | `tools/docker_secret_inotify_sidecar_check.sh` 본문 (258줄 답습) | ❌ 0건 |
| 6 | `tests/fixtures/gp3_st2/` 본문 (5 fixture) | ❌ 0건 |
| 7 | Hermes upstream Dockerfile | ❌ 0건 (R-MVP1-1.5-ST2-2 풀 3+1 trigger 답습) |
| 8 | workflow 기존 22 step + ST-2 step (line 663) 본문 | ❌ 0건 (보강 = `on:` schedule 추가 한정) |
| 9 | inotify event 응답 시간 *threshold 고정* | ❌ 0건 (R-MVP1-1.5-ST2-1 답습) |
| 10 | sidecar production 적용 (Hermes runtime 통합) | ❌ 0건 (R-MVP1-1.5-ST2-3 Operational Readiness PASS 영역) |
| 11 | branch protection rule | ❌ 0건 (AR-3 sub-cycle 영역) |
| 12 | ADR / 헌법 / roadmap 본문 | ❌ 0건 |
| 13 | MVP-1 Implementation Evidence PASS 발효 | ❌ 0건 ((c) carry-over 영역) |
| 14 | `adapters/llm/facade.py` placeholder → real | ❌ 0건 ((d) carry-over 영역) |

→ **14/14 변경 0건 의무 답습**

---

## §6 결론

✅ **APPROVE (Reviewer-only 단축 합의)** — 본 sub-cycle 실 구현 단계 진입 권한 발효.

### 6.1 발효 효과

- ST-2 inotify sidecar 실 구현 단계 진입 권한 발효 (nightly schedule 추가 1 항 한정)
- R-5 BLOCKING 3 단계 evidence 명문 cross-check 발효 (인프라 추가 0건, 명문 본문 채택 한정)
- 실 file 수정 자격:
  - `.github/workflows/secret-hygiene-egress-redaction.yml` `on:` 에 `schedule: [{cron: "0 3 * * *"}]` 추가
- COND 해소 자격: R-5 BLOCKING (§3 cross-check 본문 채택) + R-7(a) (entry brief v1.1 line 326 이미 흡수 완료 답습)
- (a)(b)(c)(e) 4/5 충족 / (d) = 실 구현 단계 nightly schedule 추가 완료 시 충족 자격 발효

### 6.2 본 합의가 *하지 않는* 것

- (d) 자동 충족 선언 0건 (nightly schedule 추가 + actual run id evidence 답습 의무)
- Implementation Evidence PASS 발효 0건 ((c) carry-over 영역)
- 다른 sub-cycle (AR-3) 발효 권한 0건 (PC-1-T3 = `3a63a5b` 발효 / S-3 = `4451716` 발효 완료)
- ST-2 인프라 본문 변경 권한 0건 (Cycle 3 + Cycle 4 답습 영역)
- Hermes upstream Dockerfile 변경 권한 0건 (R-MVP1-1.5-ST2-2 영구 의무)
- sidecar production 적용 권한 0건 (R-MVP1-1.5-ST2-3 Operational Readiness PASS 영역)
- inotify event 응답 시간 threshold 고정 권한 0건 (R-MVP1-1.5-ST2-1 답습, threshold 후보 framing 보존)
- branch protection rule 변경 권한 0건 (AR-3 sub-cycle 영역)
- `docs/phase0/g2-gp3-mvp1-evidence.md` 보강 권한 0건 (D-3 별도 sub-cycle 답습)

### 6.3 다음 단계

1. ✅ **본 합의 (단계 3 완료)**
2. ⏳ **단계 4 — 실 구현** (brief §4 `on:` schedule 추가 1 항)
3. ⏳ **단계 5 — commit + SESSION + INDEX**
4. ⏳ **단계 6 — push** (사용자 명시 의무 답습, workflow scope = Claude OAuth 거부 S-3 답습)

---

## §7 본 합의 자기진단 (8/8 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 풀 3+1 승격 trigger 5/5 발화 0건 검증 | ✅ §1.1 |
| 2 | entry 합의 verbatim cross-check | ✅ §1.2 (5 source) |
| 3 | ST-2 인프라 8/8 발효 답습 + 변경 0건 검증 (23번째 entry audit 한정 패턴) | ✅ §1.3 |
| 4 | 사용자 결정 D-1~D-3 3/3 답습 | ✅ §2 |
| 5 | R-5 BLOCKING 3 단계 evidence 발효 cross-check 명문 (본 합의 본문 채택) | ✅ §3 |
| 6 | ADR-011 (a)~(e) 매트릭스 발효 자격 명시 (4/5 본 합의 + 1/5 실 구현 단계) | ✅ §4 |
| 7 | 변경 0건 의무 14/14 cross-check | ✅ §5 |
| 8 | Reviewer-only 단축 합의 자격 명시 (entry brief line 290 답습 + PC-1/S-3 + 23번째 entry audit 패턴 답습) | ✅ §1 + §2 D-1 |
