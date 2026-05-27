# ST-2 inotify sidecar 실 구현 진입 Brief (DRAFT)

> **본 brief = ST-2 *실 구현* 진입 *준비안*** — ST-2 단독 진입 적격성 합의 (`0e99a56` APPROVE) 결과 *행사 준비*. 사용자 명시 9 결정 답습 *문서상 확정* (선행 4 결정 + 신규 5 결정).
>
> 본 brief 의 어떤 §도 그 자체로 (i) ST-2 *실 구현* 을 *시작* 시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) MVP-1 PASS *재선언* / Layer E / Layer F / §C-5 Satisfied 자동 갱신 / 다른 backlog 자동 진입 / T3 영역 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-13 후속 26
**상태**: DRAFT (사용자 명시 9 결정 반영 + 합의 보고서 진입 *직전* + Cycle 1 진입 *직전*)
**상위 권위**:
- ST-2 단독 우선 진입 적격성 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md` (commit `0e99a56`, APPROVE — Reviewer-only 단축 합의)
- ST-2 단독 진입 적격성 brief = `docs/phase0/backlog1-st2-inotify-sidecar-brief.md` (commit `d9ae98b`, 12 섹션)
- Backlog #6 구현 진입 brief 패턴 답습 = `docs/phase0/backlog6-implementation-step-brief.md` (commit `c50e6a0`)
- MVP-1 deepening roadmap = `implementation-runtime-roadmap-mvp1.md` §3.3 + §3.4.2 + §3.6.1
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + GP-3 §5.3 + ADR-011 §2.1 (a)~(e) + §2.4

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "옵션 (A)로 진행해주세요. 본 텍스트 brief를 그대로 승인하고, 파일화한 뒤 Reviewer-only 단축 합의 보고서 작성, 이후 Cycle 1로 진입하겠습니다."

> "(a) inotify watch = inotifywait / (b) Cycle 3 = test + feat 2 commit 분리 / (c) §C-5 갱신 = γ sub-condition 분리 / (d) init grace period = 10초 / (e) healthcheck interval = 5초"

### 0.2 사용자 명시 9 결정 답습 (선행 4 + 신규 5)

**선행 4 결정 (`0e99a56` 답습)**:
1. fail-closed = **F-B 우선** / F-C 보조 / **F-A 비채택**
2. Multi-host parity = **미요구** (MVP-1 단일 host 한정)
3. inotify 감시 경로 = **`/run/secrets/*`**
4. secret rotation 정책 = **별도 합의 영역 분리** (runtime 변경 = fail-closed)

**신규 5 결정 (본 brief 진입 명령)**:
5. inotify watch 구현 = **`inotifywait`** (inotify-tools 패키지, sidecar Dockerfile PoC 범위 내 설치)
6. Cycle 3 commit 분할 = **`test` + `feat` 2 commit 분리** (fixture / sidecar 구현 분리, 추적성 확보)
7. §C-5 갱신 방식 = **γ sub-condition 분리** (C-5a = ST-2 / C-5b = ST-1 / C-5c = PC-4)
8. init grace period T2 = **10초** (sidecar startup 후 inotify event 처리 시작 지연)
9. healthcheck interval = **5초** (sidecar status file → Hermes mock healthcheck 반응 측정 주기)

### 0.3 본 brief 가 *하는* 것

1. ST-2 실 구현 진입 *계획 적격성* 권위 권고 정비 (16 섹션)
2. 사용자 명시 9 결정 답습 *문서상 확정*
3. 6 cycle 분할 + 각 cycle commit 형태 + 파일 범위 + evidence 기준 + Rollback Trigger + actual run 검증 계획 권위 권고
4. §C-5 *Satisfied 갱신 조건* 정리 (γ sub-condition 분리 — C-5a Satisfied 갱신 후속 의무)
5. Cycle 1 진입 *직전* 의사결정 입력 정비

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습 — 11 금지)

- ❌ **ST-2 *실 구현* 0건** (Cycle 1 한정 진입 — Cycle 2~6 는 본 brief 영역 외)
- ❌ **sidecar Dockerfile 작성 0건** (Cycle 3 영역)
- ❌ **inotify 스크립트 작성 0건** (Cycle 3 영역)
- ❌ **docker-compose 작성 0건** (Cycle 3 영역, PoC 격리 한정)
- ❌ **production `docker-compose.yml` 변경 0건** (사용자 명시 답습)
- ❌ **Hermes upstream Dockerfile 변경 0건** (`0e99a56` 답습)
- ❌ **CI workflow 변경 0건** (Cycle 4 영역)
- ❌ **actual run 실행 0건** (Cycle 6 영역)
- ❌ **§C-5 *Satisfied 자동 갱신* 0건** (γ C-5a Satisfied 갱신 = Cycle 6 후속 별도 합의 영역)
- ❌ **MVP-1 PASS *재선언* / Operational Readiness PASS / Hermes PMO 격상 0건**
- ❌ **ST-1 / PC-4 / T3 영역 자동 진입 0건**
- ❌ **사용자 명시 9 결정 *재변경* 0건**
- ❌ **§5.5 9 sub-수단 본문 채택 *변경* 0건**

### 0.5 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정 + Cycle 1 진입 *직전***. 본 brief 의 어떤 §도 Cycle 2~6 자동 진입 / ST-2 실 구현 자동 발효 / §C-5 자동 갱신 / 합의 보고서 권위 발효 / Layer E·F 격상을 발생시키지 않는다.

---

## 1. ST-2 구현 범위

### 1.1 구현 범위 = ST-2 PoC 격리 환경 한정

| 항목 | 영역 |
|------|------|
| **PoC 격리 디렉토리** | `docker/gp3-st2-poc/` (sibling `docker/gp3-st3-poc/` + `docker/r2-poc/` + `docker/r4-1-poc/` 패턴 답습 — production docker-compose 와 분리) |
| **inotify sidecar 구현** | non-root + cap drop ALL + read-only mount + docker socket 0건 (F-A 비채택 답습) + **`inotifywait` 사용 (사용자 #5 결정 답습)** |
| **fail-closed 메커니즘** | **F-B 우선** (status file → Hermes mock healthcheck unhealthy) + **F-C 보조** (docker-compose `depends_on: service_healthy`) |
| **inotify 감시 경로** | **`/run/secrets/*`** (PoC 영역에서는 mock secret 경로) |
| **init grace period T2** | **10초** (사용자 #8 결정 답습) |
| **healthcheck interval** | **5초** (사용자 #9 결정 답습) |
| **CI 통합** | `secret-hygiene-egress-redaction.yml` 확장 (신규 step 1~2 개) — Cycle 4 영역 |

### 1.2 구현 범위 *제외* 영역

§0.4 답습 + 추가:

- ❌ Production `docker-compose.yml` 변경 0건 (사용자 명시 답습)
- ❌ Hermes upstream Dockerfile 변경 0건 (`0e99a56` 답습)
- ❌ 실 Hermes container 영향 0건 (PoC = mock Hermes 한정)
- ❌ ST-1 / ST-4 / PC-4 / docker socket 접근 / Multi-host parity / secret rotation 정책 모두 0건
- ❌ T3 영역 자동 진입 0건 (10/10 침범 후보 0건 보존)

---

## 2. F-B fail-closed 구조 상세 (사용자 #1 결정 답습)

### 2.1 메커니즘 흐름

```
[inotify-sidecar container]                  [hermes-mock container]
        │                                            │
        │ inotifywait -m -e attrib,modify,           │
        │   move_self,delete_self /run/secrets       │
        │                                            │
        │ (init grace period = 10초 답습)            │
        │                                            │
        ├─► event 발생 후:                            │
        │   echo "UNHEALTHY: <event> <path>          │
        │         <timestamp>" >                     │
        │         /var/run/sidecar-status            │
        │                                            │
                                                     ▼
                                          docker-compose healthcheck:
                                          test: ["CMD-SHELL",
                                                 "test -z \"$(cat /var/run/sidecar-status 2>/dev/null)\""]
                                          interval: 5s (사용자 #9 답습)
                                          retries: 2
                                          timeout: 3s
                                          ▼
                                          → unhealthy 처리
                                          → hermes-mock 정지 시뮬레이션
```

### 2.2 F-B 구성 요소

| 구성 요소 | 위치 | 권한 |
|---------|------|------|
| sidecar inotifywait process | sidecar container 내부 | non-root + cap drop ALL |
| status file write 위치 | 공유 named volume `sidecar-status-vol` → `/var/run/sidecar-status` | sidecar = write / hermes-mock = read |
| `/run/secrets/*` mount | 공유 named volume `mock-secrets-vol` (PoC 격리) | sidecar = read-only / hermes-mock = read-only |
| hermes-mock healthcheck | `docker-compose.gp3-st2.yml` 의 hermes-mock service 정의 | docker-compose level (repo-local) — **interval 5s** |
| docker socket | ❌ 미마운트 (F-A 비채택 답습) | 0건 |
| privileged flag | ❌ false | 0건 |
| inotify-tools 패키지 | sidecar Dockerfile `apt install inotify-tools` 한정 (PoC 범위) | 격리 |

### 2.3 status file 내용 형식

| 상태 | 내용 |
|------|------|
| 정상 (init grace + 정상 운영) | empty file (또는 `OK`) |
| 비정상 (event 발화) | `UNHEALTHY: <event_type> <path> <ISO8601_timestamp>` |

예시:
```
UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key 2026-05-13T15:30:00Z
```

---

## 3. F-C 보조 후보 유지 방식 (사용자 #1 결정 답습)

### 3.1 F-C 보조 메커니즘

```yaml
services:
  inotify-sidecar:
    healthcheck:
      test: ["CMD-SHELL", "pgrep -f inotifywait > /dev/null"]
      interval: 5s
      retries: 2
  hermes-mock:
    depends_on:
      inotify-sidecar:
        condition: service_healthy   # F-C 보조 (sidecar healthy 후 hermes-mock 시작)
    healthcheck:
      test: ["CMD-SHELL", "test -z \"$(cat /var/run/sidecar-status 2>/dev/null)\""]
      interval: 5s   # F-B primary signal
      retries: 2
```

### 3.2 본 brief 구현 결정

| 결정 | 영역 |
|------|------|
| **F-B 우선 구현** = primary fail-closed signal | sidecar status file → hermes-mock healthcheck unhealthy |
| **F-C 보조 함께 구현** = sidecar silent fail 방지 + startup ordering 보강 | sidecar healthy → hermes-mock 시작 보장 |
| F-A 비채택 보존 = docker socket 0건 | (사용자 #1 답습) |

---

## 4. `/run/secrets/*` 감시 구조 (사용자 #3 결정 답습)

### 4.1 PoC 격리 mount 구조

| 구성 요소 | mount 형태 | 권한 |
|---------|---------|------|
| **mock-secrets-vol** (named volume) | sidecar `/run/secrets:ro` + hermes-mock `/run/secrets:ro` | 공유 read-only |
| **sidecar-status-vol** (named volume) | sidecar `/var/run:rw` + hermes-mock `/var/run/sidecar-status:ro` | sidecar = write / hermes-mock = read |
| Cycle 2 fixture mount | `./tests/fixtures/gp3_st2/<pass\|fail>/<scenario>/run-secrets/` bind mount → mock-secrets-vol initial content | bind mount read-only |

### 4.2 PoC mock secret 파일 (Cycle 2 영역)

| 파일 | 내용 (fake canary 의무 — R-4.1 답습) |
|------|--------------------------------|
| `/run/secrets/mock_api_key` | `FAKE_CANARY_DO_NOT_USE_K1FU-2GH7-A20W-X9JL` |
| `/run/secrets/mock_provider_key` | `FAKE_CANARY_DO_NOT_USE_OP-5BCD-EFGH-1234-IJKL` |
| `/run/secrets/mock_db_password` | `FAKE_CANARY_DO_NOT_USE_PG-9XYZ-MNOP-QRST` |

**원칙**: 실 secret 본문 commit 0건 (영구 금지) + sidecar 가 secret 본문 read 후 logging / hash / export 0건.

---

## 5. inotify event 감시 대상 + 구현 (사용자 #5 결정 답습)

### 5.1 `inotifywait` 사용 결정

**사용자 #5 결정 답습**: `inotifywait` (inotify-tools 패키지) 사용.

사유:
- sidecar 목적에 가장 단순함
- shell script 기반으로 PoC 검증이 쉬움
- Python package 의존성보다 동작이 명확함
- C syscall 직접 구현보다 유지보수 부담이 낮음

### 5.2 inotifywait 호출 형태 (Cycle 3 구현)

```bash
inotifywait -m \
    -e attrib,modify,move_self,delete_self \
    --format '%T %e %w%f' \
    --timefmt '%Y-%m-%dT%H:%M:%SZ' \
    /run/secrets/
```

| inotify event | inotifywait flag | 발화 조건 | Cycle 2 fixture 시연 |
|-------------|-----------------|---------|------------------|
| `IN_ATTRIB` | `attrib` | mtime / mode / owner 변경 | `fail/chmod_644/` |
| `IN_MODIFY` | `modify` | 파일 내용 변경 | `fail/content_modified/` |
| `IN_MOVE_SELF` | `move_self` | 파일 이동 | (fail/file_deleted/ 와 통합 가능) |
| `IN_DELETE_SELF` | `delete_self` | 파일 삭제 | `fail/file_deleted/` |
| `IN_ACCESS` | — (미사용) | 읽기 access | ❌ 미사용 (false positive 폭증 회피) |

### 5.3 sidecar Dockerfile base image 후보 (Cycle 3 영역)

| 후보 | 장점 | 단점 |
|------|------|------|
| **alpine:3 + apk add inotify-tools** | 이미지 크기 ↓ (< 10MB) + 보안 수면 적음 | musl libc 호환성 (대부분 OK) |
| **debian:bookworm-slim + apt install inotify-tools** | 호환성 ↑ | 이미지 크기 ↑ (~ 80MB) |

**Cycle 3 권고**: alpine 우선 (이미지 크기 + 보안 수면) — 구현 시점 사용자 명시 결정 영역.

---

## 6. runtime secret 변경 fail-closed 처리 (사용자 #4 + #8 결정 답습)

### 6.1 fail-closed 흐름

```
[event 발생]                          [sidecar 행동]                  [hermes-mock 행동]
  │                                       │                                  │
  IN_ATTRIB / IN_MODIFY /                 │                                  │
  IN_MOVE_SELF / IN_DELETE_SELF           │                                  │
  발화 (init grace period 10초 후)        │                                  │
                ─────────────────────────►│                                  │
                                          ▼                                  │
                              echo "UNHEALTHY: <event>                       │
                                <path> <ts>" >                                │
                                /var/run/sidecar-status                       │
                                          │                                  │
                                          ─────────────────────────────────►│
                                                                               ▼
                                                                docker-compose healthcheck:
                                                                interval 5s 답습
                                                                test -z $(cat) → false
                                                                → exit 1 → unhealthy
                                                                              │
                                                                              ▼
                                                                docker-compose retries 2 →
                                                                정지 시뮬레이션
```

### 6.2 init grace period 처리 (사용자 #8 결정 답습 — T2 = 10초)

| 단계 | sidecar 행동 | 시간 |
|------|---------|--------|
| sidecar startup | `inotifywait` *미시작* | 0 ~ T1 (T1 < 5초, PoC 격리 환경) |
| init grace period | inotifywait 시작 + event 무시 (sleep 10초) | T1 ~ T1+10 |
| 운영 시작 | inotifywait event 처리 (status file write) | T1+10 이후 |

**Cycle 3 구현 후보** (`watch-secrets.sh` 또는 `watch_secrets.py`):

```bash
#!/bin/sh
set -e
# Init grace period (사용자 #8 결정 답습 — 10초)
sleep 10
# Start inotifywait
inotifywait -m -e attrib,modify,move_self,delete_self \
    --format '%T %e %w%f' --timefmt '%Y-%m-%dT%H:%M:%SZ' \
    /run/secrets/ | \
while read -r line; do
    echo "UNHEALTHY: $line" > /var/run/sidecar-status
done
```

### 6.3 fixture 시연 시나리오 (Cycle 2 영역)

| fixture | 시나리오 | 예상 결과 |
|---------|--------|--------|
| `pass/normal_operation/` | init grace 후 mtime 변경 0건 | sidecar status = empty + hermes-mock healthy |
| `pass/init_phase/` | init grace 내 normal secret 주입 | event 무시 + hermes-mock healthy |
| `fail/chmod_644/` | runtime chmod 644 | `UNHEALTHY: IN_ATTRIB` + hermes-mock unhealthy |
| `fail/content_modified/` | runtime mock secret 본문 변경 | `UNHEALTHY: IN_MODIFY` + hermes-mock unhealthy |
| `fail/file_deleted/` | runtime mock secret unlink | `UNHEALTHY: IN_DELETE_SELF` + hermes-mock unhealthy |

---

## 7. secret rotation 정책 분리 (사용자 #4 결정 답습)

### 7.1 본 ST-2 실 구현 = runtime 변경 모두 fail-closed

모든 runtime mtime / perm / content 변경 = fail-closed. secret rotation 시나리오 포함 (본 ST-2 구현 범위 외 — 별도 합의 영역).

### 7.2 별도 합의 영역 연결 가능

| 후속 합의 영역 | 영역 |
|-----------|------|
| secret rotation 자체 정책 | 별도 P 발행 가능성 |
| Operational Readiness parity | Backlog #7 — Multi-host + Vault HSM ST-4 |
| Vault HSM (ST-4, ADR-010) | 외부 secret rotation source |

### 7.3 ST-2 PoC 영역 처리

- ❌ rotation 시뮬레이션 fixture 0건
- ❌ rotation 시 fail-closed *예외* 처리 0건
- ❌ rotation 정책 본문 작성 0건

### 7.4 R-ST2-3 Rollback Trigger 답습 (정상 rotation 오탐 → 별도 합의 진입)

---

## 8. 구현 파일 후보

### 8.1 신규 파일 후보 (`docker/gp3-st2-poc/` PoC 격리 디렉토리 + 부속)

| # | 파일 후보 | Cycle | 영역 |
|---|--------|-------|------|
| 1 | `docker/gp3-st2-poc/README.md` | **Cycle 1** | PoC 격리 영역 설명 + 사용 가이드 + production 영역 분리 명시 + 9 결정 답습 + 6 cycle 분할안 + sibling `gp3-st3-poc/` 와의 관계 |
| 2 | `docker/gp3-st2-poc/Dockerfile` | Cycle 3 | sidecar image (alpine + inotify-tools + non-root + cap drop) |
| 3 | `docker/gp3-st2-poc/watch-secrets.sh` | Cycle 3 | inotifywait shell 스크립트 (`inotifywait` + init grace 10초 + status file write) |
| 4 | `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` | Cycle 3 | PoC 격리 docker-compose (sidecar + hermes-mock + 2 named volume + healthcheck interval 5s + F-B + F-C) |
| 5 | `docker/gp3-st2-poc/hermes-mock/Dockerfile` 또는 inline image | Cycle 3 | hermes-mock image (alpine + healthcheck script, 실 Hermes 영향 0건) |
| 6 | `tools/docker_secret_inotify_sidecar_check.sh` | Cycle 4 | CI step 호출 도구 (docker-compose up + fixture 시뮬레이션 + status 검증 + exit code) |
| 7 | `tests/fixtures/gp3_st2/pass/normal_operation/run-secrets/mock_api_key` (+ provider + db) | Cycle 2 | 정상 운영 fixture |
| 8 | `tests/fixtures/gp3_st2/pass/init_phase/run-secrets/...` | Cycle 2 | init grace fixture |
| 9 | `tests/fixtures/gp3_st2/fail/chmod_644/run-secrets/...` + `simulate.sh` | Cycle 2 | chmod 644 시뮬레이션 |
| 10 | `tests/fixtures/gp3_st2/fail/content_modified/run-secrets/...` + `simulate.sh` | Cycle 2 | 본문 변경 시뮬레이션 |
| 11 | `tests/fixtures/gp3_st2/fail/file_deleted/run-secrets/...` + `simulate.sh` | Cycle 2 | 파일 삭제 시뮬레이션 |

### 8.2 기존 파일 확장 후보

| # | 파일 | Cycle | 영역 |
|---|------|-------|------|
| 12 | `.github/workflows/secret-hygiene-egress-redaction.yml` | Cycle 4 | paths trigger 확장 + `gp3_st2_sidecar_integration` step 1 개 + summary.json 신규 필드 (Cycle 5 통합 가능) |

### 8.3 변경 0건 영역 (사용자 명시 답습)

- Production `docker-compose.yml` (PoC 격리 한정)
- Hermes upstream Dockerfile (`0e99a56` 답습)
- `tools/secret_scanner.py` (Group D, Stage 1 영역)
- `tools/provider_*_scanner.py` (Group A, Stage 3 영역)
- `.importlinter` / `requirements-dev.txt` (GP-5 영역)
- ADR-008 / ADR-010 / ADR-011 / ADR-012 본문
- `implementation-runtime-roadmap-mvp1.md` §3 / §4 / §5.5 본문

### 8.4 합산

11 신규 파일 + 1 기존 확장 + 7+ 변경 0건 영역.

---

## 9. Cycle 분할안 (사용자 #6 결정 답습)

### 9.1 6 Cycle 권고 (각 cycle 별 commit 형태 결정 답습)

| Cycle | 영역 | 신규 파일 | 기존 확장 | commit 형태 |
|-------|------|--------|------------|----------|
| **Cycle 1** | PoC 격리 디렉토리 + README | `docker/gp3-st2-poc/README.md` | 0건 | **1 commit** (`feat(g2-gp3): scaffold ST-2 PoC isolated directory`) |
| **Cycle 2** | fixture 5개 (pass 2 + fail 3) | `tests/fixtures/gp3_st2/{pass,fail}/...` | 0건 | **1 commit** (`test(g2-gp3): add ST-2 inotify sidecar fixtures`) |
| **Cycle 3** | sidecar Dockerfile + watch script + docker-compose + hermes-mock | 4~5 파일 | 0건 | **`test` + `feat` 2 commit 분리 (사용자 #6 결정 답습)** |
| **Cycle 4** | CI step + tool 스크립트 | `tools/docker_secret_inotify_sidecar_check.sh` | `secret-hygiene-egress-redaction.yml` | 2 commit (`feat(g2-gp3): add ST-2 integration check tool` + `feat(g2-gp3): add ST-2 CI step`) |
| **Cycle 5** | summary.json 신규 필드 + ledger candidate + evidence form | (Cycle 4 workflow 內 통합 시 0건 — 또는 별도 1 파일) | (Cycle 4 workflow 확장 內) | 1 commit (`feat(g2-gp3): add ST-2 summary.json ledger candidate + evidence form`) |
| **Cycle 6** | push + actual run + §C-5a 갱신 권고 | 0건 | 0건 | 0 commit (push + actual run + 별도 합의 영역) |

**합산 = 7 commit** (Cycle 1 한정 1 commit + Cycle 2~5 6 commit + Cycle 6 push) + 메타 commit 별도.

### 9.2 Cycle 3 commit 분할 상세 (사용자 #6 결정 답습)

| Sub-commit | 영역 | 파일 |
|---------|------|------|
| Cycle 3.1 `test` | sidecar 동작 검증 위한 추가 fixture / 통합 test 데이터 | (Cycle 2 fixture 보강 필요 시) — 또는 Cycle 2 와 통합 가능 |
| Cycle 3.2 `feat` | sidecar 실 구현 본문 | `docker/gp3-st2-poc/Dockerfile` + `watch-secrets.sh` + `docker-compose.gp3-st2.yml` + `hermes-mock/` |

**Cycle 3 권고 형태** (사용자 #6 결정 답습):
- 분리 1 (TDD 답습): Cycle 2 fixture 가 sidecar 미구현 상태에서 RED 검증 → Cycle 3.2 feat 으로 GREEN
- 분리 2 (추적성 답습): test 와 feat 분리 = 실패 시 원인 격리 쉬움

### 9.3 의존성 그래프

```
Cycle 1 (디렉토리 + README) ──► Cycle 2 (fixture) ──► Cycle 3 (sidecar) ──► Cycle 4 (CI step) ──► Cycle 5 (evidence) ──► Cycle 6 (actual run + §C-5a)
```

### 9.4 Cycle 1 진입 *범위 한정*

본 brief 발효 후 진입 = **Cycle 1 한정**:
- `docker/gp3-st2-poc/README.md` 작성 (PoC 격리 영역 설명 + 사용자 9 결정 답습 + 6 cycle 분할안 + production 영역 분리 + sibling PoC 와의 관계)
- Cycle 2~6 = **사용자 명시 결정 후 별도 진입** (자동 진입 0건)

---

## 10. evidence / artifact 기준

### 10.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (Cycle 6 시점)

| # | 조건 | ST-2 evidence |
|---|------|--------------|
| (a) | 동등 이상의 보안 결과 | docker secret (ST-3) + chmod 600 + inotify 감시 (sidecar) + F-B fail-closed (5초 interval) + 통합 결과 ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 답습 동등 이상 |
| (b) | 격리 환경 PoC 실증 | `docker/gp3-st2-poc/docker-compose.gp3-st2.yml` + Cycle 2 의 3 fail fixture 모두 fail-closed action 시연 + 2 pass fixture 정상 운영 시연 |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + GP-3 §5.3 + mvp1.md §3.3 + `0e99a56` + `d9ae98b` + 본 brief 답습 |
| (d) | 자동 회귀 검증 경로 확보 | `secret-hygiene-egress-redaction.yml` 확장 + actual run SUCCESS + nightly 권고 + paths trigger 확장 |
| (e) | 합의 APPROVE | `0e99a56` (진입 적격성) + Cycle 6 후속 §C-5a 갱신 합의 (별도 단계) |

### 10.2 summary.json 신규 필드 후보 (Cycle 5 영역)

| 필드 | 값 후보 |
|------|------|
| `gp3_st2_sidecar_integration` | `PASS` / `FAIL` |
| `gp3_st2_fixture_count` | 5 (2 pass + 3 fail) |
| `gp3_st2_fail_closed_action_count` | 3 (fail fixture 모두 fail-closed 발화) |
| `gp3_st2_init_grace_period_seconds` | 10 (사용자 #8 답습) |
| `gp3_st2_healthcheck_interval_seconds` | 5 (사용자 #9 답습) |
| `gp3_st2_inotify_implementation` | "inotifywait" (사용자 #5 답습) |
| `gp3_st2_ledger_event_candidate` | `secret_storage_inotify_isolation` (candidate-only) |
| `gp3_st2_evidence_form` | "F-B status file → hermes-mock healthcheck unhealthy (5s interval)" |
| `gp3_st2_scope` | "MVP-1 1.5차 PoC (ST-2 단독 진입), Hermes upstream 0건, docker socket 0건, Multi-host 미요구, secret rotation 별도 합의" |
| `gp3_st2_known_baseline` | (Cycle 6 단계 사용자 명시 시점 결정) |

### 10.3 Evidence 형식 (Cycle 5 + Cycle 6 시점)

| Evidence | 형식 |
|----------|------|
| Markdown report | `docs/phase0/g2-gp3-mvp1-st2-evidence.md` (가칭) 또는 기존 evidence 확장 |
| JSONL ledger entry | `secret_storage_inotify_isolation` (Backlog #5 ADR-012 §2.2 별도 합의 후속 등록 — candidate-only) |
| Docker isolation log | docker-compose up + 5 fixture 시뮬레이션 → fail-closed action + status file write + hermes-mock unhealthy evidence |
| GitHub Actions run | `secret-hygiene-egress-redaction.yml` (확장) actual run id + 신규 step PASS |
| 합의 보고서 | Cycle 6 후속 §C-5a 갱신 합의 |

---

## 11. Rollback Trigger (`d9ae98b` brief §9 + 신규 권고)

### 11.1 기존 8 trigger 답습 (R-ST2-1 ~ R-ST2-8, `d9ae98b` brief §9.2)

답습 변경 0건.

### 11.2 본 brief 신규 5 trigger (구현 영역 specific)

| Trigger ID | 발화 조건 | 행동 |
|-----------|---------|------|
| **R-ST2-9** | Cycle 2 fixture 중 1+ expected behavior 미달 (예: `fail/chmod_644/` fail-closed 미발화) | 풀 3+1 합의 + fixture / sidecar 재검토 |
| **R-ST2-10** | Cycle 6 actual run 회귀 (기존 Stage 1~5 step 영향) | 풀 3+1 합의 + 회귀 fix + 재 actual run |
| **R-ST2-11** | sidecar Dockerfile base image 보안 취약점 발견 (CVE) | 단축 합의 + base image 변경 + 재빌드 |
| **R-ST2-12** | docker-compose `depends_on` (F-C) 동작 환경 불일치 (v1 vs v2) | 단축 합의 + 호환성 조정 (F-C 보조 한정 — F-B 단독 운영 가능) |
| **R-ST2-13** | production 영역 영향 detection (production docker-compose.yml 또는 Hermes container 변경) | 즉시 합의 + 격리 영역 복원 |

---

## 12. actual run 검증 계획 (Cycle 6 영역)

### 12.1 검증 항목 (`d9ae98b` brief 답습)

| # | 항목 | 기대 |
|---|------|------|
| 1 | 기존 Stage 1~5 step 회귀 0건 | 모든 step PASS 유지 |
| 2 | Cycle 4 신규 step PASS | `gp3_st2_sidecar_integration=PASS` |
| 3 | 5 fixture 모두 expected behavior | 2 pass + 3 fail 시연 정상 |
| 4 | F-B status file write latency < 5초 (interval 답습) | `inotify_event_response_time` 측정 |
| 5 | summary.json 신규 필드 정상 생성 | `gp3_st2_*` 필드 모두 출력 |
| 6 | artifact upload 완료 | sidecar status log + docker-compose log + summary.json |
| 7 | F-A (docker socket) 미발화 검증 | `docker.sock` mount 0건 + privileged 0건 |
| 8 | Hermes upstream Dockerfile 변경 0건 검증 | git log 확인 |
| 9 | 사용자 명시 9 결정 답습 보존 | F-B 우선 / F-C 보조 / F-A 비채택 / Multi-host 미요구 / `/run/secrets/*` / runtime fail-closed + rotation 분리 / inotifywait / Cycle 3 test+feat 분리 / init grace 10초 / healthcheck interval 5초 |

### 12.2 SUCCESS 기준 = 9/9 충족 → Cycle 6 완료 → §C-5a 갱신 합의 진입 적격

---

## 13. §C-5 Satisfied 갱신 조건 (사용자 #7 결정 답습 — γ sub-condition 분리)

### 13.1 γ sub-condition 분리 결정 (사용자 #7 답습)

```
C-5  → C-5a (ST-2 inotify sidecar)
       C-5b (ST-1 entrypoint stat)
       C-5c (PC-4 local pre-commit framework)
```

### 13.2 C-5a Satisfied 갱신 조건 (Cycle 6 후속)

| 조건 | 충족 |
|------|------|
| (a) Cycle 6 actual run SUCCESS = 9/9 (§12.1 답습) | (Cycle 6 시점 결정) |
| (b) ADR-011 §2.1 (a)~(e) 5조건 충족 (§10.1 답습) | (Cycle 6 시점 결정) |
| (c) Evidence Markdown report 작성 + JSONL ledger candidate 기록 | (Cycle 5 + Cycle 6 시점) |
| (d) 사용자 명시 9 결정 답습 보존 | (전체 cycle 동안 강제) |
| (e) C-5a 갱신 합의 (Reviewer-only 단축 또는 풀 3+1) | (Cycle 6 후속 별도 단계) |

### 13.3 §C-5 전체 vs sub-condition 상태 표 (Cycle 6 후속 시점)

| Condition | Cycle 6 SUCCESS 후 상태 |
|----------|-------------------|
| C-5a (ST-2) | ✅ Satisfied (본 진입 영역) |
| C-5b (ST-1) | ⏳ Deferred (Backlog #3 + T3 영역 별도 합의) |
| C-5c (PC-4) | ⏳ Deferred (Backlog #1 + #2 PC-4 sub-영역 별도 합의) |
| **§C-5 전체** | ⏳ **Partially Satisfied (C-5a only)** |

### 13.4 본 §13 의 *범위 한계*

- ❌ §C-5 / C-5a / C-5b / C-5c 자동 갱신 0건 (Cycle 6 후속 별도 합의 영역)
- ❌ Layer D 본문 자동 변경 0건 (γ sub-condition 분리도 Cycle 6 후속 합의에서 권위 확정)
- ❌ MVP-1 PASS 재선언 0건 + Layer E / Layer F 격상 0건

---

## 14. 합의 형태 권고

### 14.1 본 brief 의 합의 형태

| 영역 | 합의 형태 |
|------|------|
| 본 brief 자체 (DRAFT) | 사용자 명시 승인 한정 |
| brief 파일화 후 합의 진입 | **Reviewer-only 단축 합의** (`0e99a56` chain + 9 sub-수단 본문 채택 변경 0건 + 사용자 명시 9 결정 답습) |

### 14.2 풀 3+1 승격 트리거 검증

| # | 트리거 | 발화 |
|---|----|-----|
| 1 | 9 sub-수단 외 수단 재결정 | ❌ 0건 |
| 2 | T3 자동 진입 | ❌ 0건 |
| 3 | 사용자 명시 9 결정 재변경 | ❌ 0건 |
| 4 | Provider Liquidity 약화 | ❌ 0건 |
| 5 | 5 영구 핵심 제약 약화 | ❌ 0건 |
| 6 | MVP-1 PASS 재선언 / Layer E·F 격상 | ❌ 0건 |
| 7 | 외부 LLM 없는 T3 결정 | ❌ 0건 |

**합산 = 7/7 0건 발화** → Reviewer-only 단축 합의 적격.

---

## 15. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 (13 섹션) | ✅ |
| 사용자 명시 11 금지 답습 | ✅ |
| 사용자 명시 9 결정 답습 (선행 4 + 신규 5) | ✅ |
| 사용자 권장 6 cycle 분할 답습 + Cycle 3 test+feat 분리 | ✅ |
| ST-2 진입 적격성 합의 (`0e99a56`) 답습 | ✅ |
| Hermes upstream Dockerfile 변경 0건 | ✅ |
| T3 자동 진입 0건 (10/10 침범 후보) | ✅ |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| C-1~C-8 상태 변경 0건 (§C-5 Deferred 유지 — γ 분리 = Cycle 6 후속) | ✅ |
| MVP-1 PASS *재선언* / Layer E / Layer F 격상 0건 | ✅ |
| Cycle 1 한정 진입 (Cycle 2~6 자동 진입 0건) | ✅ |
| 합의 보고서 / commit / push (본 brief 영역 외) | ✅ (별도 commit 단계) |

---

## 16. 본 brief 요약 (한 단락)

본 brief 는 **ST-2 (inotify sidecar) *실 구현* 진입 *준비안* (DRAFT) + Cycle 1 진입 *직전* 의사결정 입력 정비** 이다. ST-2 단독 진입 적격성 합의 (`0e99a56` APPROVE — 사용자 명시 4 결정 답습) 발효 후속, 사용자 명시 추가 5 결정 답습 *문서상 확정* — (5) **inotify watch = `inotifywait`** (alpine + inotify-tools, PoC 범위 한정) / (6) **Cycle 3 commit = `test` + `feat` 2 commit 분리** / (7) **§C-5 갱신 = γ sub-condition 분리 (C-5a/b/c)** / (8) **init grace period T2 = 10초** / (9) **healthcheck interval = 5초**. 16 섹션 (구현 범위 / F-B 구조 상세 / F-C 보조 유지 / `/run/secrets/*` 감시 구조 / inotifywait 사용 + event 매트릭스 / runtime fail-closed (init grace 10초) / secret rotation 분리 / 구현 파일 후보 (11 신규 + 1 확장) / 6 Cycle 분할 (각 commit 형태 결정) / evidence·artifact (summary.json 신규 10 필드) / Rollback Trigger 13 후보 / actual run 검증 9 항목 / §C-5a Satisfied 갱신 조건 / 합의 형태 권고) 정비. **풀 3+1 승격 트리거 7/7 0건 발화** → Reviewer-only 단축 합의 적격. **본 brief 발효 후 진입 = Cycle 1 한정** (`docker/gp3-st2-poc/README.md` 작성). Cycle 2~6 = 사용자 명시 결정 후 별도 진입. **본 brief 는 sidecar Dockerfile / inotify 스크립트 / docker-compose / CI workflow / actual run / §C-5 자동 갱신 / Layer D 본문 변경 / Layer E·F 격상 / 다른 backlog 자동 진입 / production docker-compose 변경 / Hermes upstream 변경 모두 0건** (사용자 명시 답습).

---

**상태**: DRAFT (사용자 명시 9 결정 반영 + 합의 보고서 진입 *직전* + Cycle 1 진입 *직전*)
**다음 단계**: (1) 본 brief 파일화 commit 완료 → (2) Reviewer-only 단축 합의 보고서 commit → (3) Cycle 1 commit (PoC 디렉토리 + README) → 메타 commit 후속 분리 영역 → push
**사용자 명시 9 결정 답습**:
1. fail-closed = F-B 우선 / F-C 보조 / F-A 비채택
2. Multi-host parity = 미요구
3. inotify 감시 경로 = `/run/secrets/*`
4. runtime secret 변경 = fail-closed + secret rotation 정책 별도 합의 분리
5. inotify watch 구현 = `inotifywait`
6. Cycle 3 commit = `test` + `feat` 2 commit 분리
7. §C-5 갱신 방식 = γ sub-condition 분리 (C-5a/b/c)
8. init grace period T2 = 10초
9. healthcheck interval = 5초

**금지 (사용자 명시 답습)**:
- ❌ Cycle 2~6 자동 진입
- ❌ ST-2 실 구현 (Cycle 3 영역)
- ❌ sidecar Dockerfile / inotify 스크립트 / docker-compose / CI workflow / actual run / §C-5 자동 갱신 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / ST-1·PC-4·T3 자동 진입 / production docker-compose 변경 / Hermes upstream 변경 모두 0건
