# ST-2 inotify sidecar 단독 우선 진입 합의 준비 Brief (DRAFT)

> **본 brief = ST-2 (inotify sidecar) *단독 우선 진입* 합의 *준비안*** — Backlog #1 진입 *직전* 사전 정비 합의 (`43b898c`, APPROVE AS BRIEF) 답습 + 사용자 명시 4 결정 답습 (fail-closed = F-B 우선 / F-C 보조 / F-A 비채택 / Multi-host parity 미요구 / `/run/secrets/*` 감시 경로 / secret rotation 정책 별도 합의 분리).
>
> 본 brief 의 어떤 §도 그 자체로 (i) ST-2 *실 구현* 을 시작시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) MVP-1 PASS *재선언* / Operational Readiness PASS / Hermes PMO 격상 / §C-5 Satisfied 자동 갱신 / 다른 backlog 자동 진입 / T3 영역 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-13 후속 25
**상태**: DRAFT (사용자 명시 4 결정 반영 + 합의 보고서 진입 *직전*)
**상위 권위**:
- Backlog #1 진입 *직전* 사전 정비 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (commit `43b898c`, APPROVE AS BRIEF — ST-2 = T2 + 단독 우선 진입 후보 권위 확정)
- Backlog #1 brief 본문 = `docs/phase0/backlog1-gp3-1.5-deepening-brief.md` (commit `6b15070`, §2.2 + §2.4 답습)
- MVP-1 deepening roadmap = `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.3 (ST-1~ST-5) + §3.4.2 (저장 경로 metric) + §3.5 R-MVP1-G3-3 + §3.6.3 (합의 형태 권고)
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호) + §2.6.2 R2-1 (docker secret)
- Governance preconditions = `docs/architecture/governance-preconditions.md` §5.3 (강제 메커니즘 — "inotify 런타임 감시 — Hermes runtime")
- ADR-011 §2.4 T1/T2/T3 분류

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "옵션 (A)로 진행해주세요. 본 텍스트 brief를 그대로 승인하고, 파일화한 뒤 Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."

> "1. fail-closed 메커니즘: F-B 우선 채택 / 2. F-C: 보조 후보로 유지 / 3. F-A: 비채택 / 4. Multi-host parity: 이번 ST-2 단독 진입 범위에서는 미요구"

> "감시 경로는 /run/secrets/*. secret rotation 정책은 별도 합의. Reviewer-only 단축 합의 보고서 작성. 구현은 아직 하지 않음."

### 0.2 본 brief 가 *하는* 것

1. ST-2 (inotify sidecar) *단독 우선* 진입 적격성 *권위 권고* 정비 (§1~§10)
2. 사용자 명시 4 결정 답습 *문서상 확정* (fail-closed F-B 우선 / F-C 보조 / F-A 비채택 / Multi-host 미요구 / `/run/secrets/*` 감시 / secret rotation 별도 합의)
3. ST-2 = T2 영역 권위 권고 (§2) + Hermes upstream 변경 0건 검증 (§3) + sidecar 분리 구조 (§4) + inotify 감시 대상 (§5) + mtime/perm 감지 기준 (§6) + fail-closed 동작 후보 3 옵션 매트릭스 (§7) + evidence 기준 (§8) + Rollback Trigger (§9) + 합의 형태 권고 (§10)
4. 합의 보고서 진입 *직전* 의사결정 입력 정비

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 — 13 금지)

- ❌ **ST-2 *실 구현* 0건** — sidecar Dockerfile 작성 / inotify 스크립트 작성 / `docker-compose.yml` service block 추가 / `/run/secrets/*` 실 volume 정의 / Hermes healthcheck file 본문 0건
- ❌ **CI workflow / hook 변경 0건** — `.github/workflows/secret-hygiene-egress-redaction.yml` 등 본문 변경 / 신규 step / 신규 workflow 0건
- ❌ **ST-1 (Hermes upstream entrypoint stat) *자동 진입* 0건** (T3 영역 — Backlog #3 와 *병합 검토* 권고 답습)
- ❌ **PC-4 *자동 진입* 0건** (T2 sub + T3 sub 모두)
- ❌ **ST-4 (Vault HSM) *자동 진입* 0건** (Operational Readiness 영역 — Backlog #7)
- ❌ **Multi-host parity *자동 진입* 0건** (사용자 명시 #2 결정 답습 — 이번 ST-2 단독 진입 범위 외)
- ❌ **T3 영역 *자동 진입* 0건** (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 / docker socket 접근 모두 0건)
- ❌ **MVP-1 PASS *재선언* 0건** (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지)
- ❌ **Operational Readiness PASS (Layer E) *선언* 0건** (MVP-6 영역, Backlog #7)
- ❌ **Hermes PMO 격상 (Layer F) 0건** (MVP-6 영역, 외부 LLM + 사람 리뷰 의무)
- ❌ **§C-5 Satisfied *자동 갱신* 0건** (본 brief 발효 후에도 §C-5 = Deferred 유지)
- ❌ **§5.5 9 sub-수단 본문 채택 *변경* 0건** (`f40423f` + `55c5b4b` 답습)
- ❌ **Tier-2 / Tier-3 catalog *자동 확장* 0건**
- ❌ **ADR 본문 자동 갱신 0건** (ADR-008 / ADR-010 / ADR-011 / ADR-012 — cross-reference 답습 한정)
- ❌ **합의 보고서 권위 0건** (본 brief = 준비안 — 합의 보고서는 별도 단계)
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건** (별도 commit 분리 답습)
- ❌ **외부 LLM 자동 호출 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**

### 0.4 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT, 사용자 명시 4 결정 반영)**. 본 brief 의 어떤 §도:

- (i) ST-2 *실 구현* 을 *시작* 시키지 않으며,
- (ii) MVP-1 PASS *재선언* / Layer E / Layer F 발효를 *발생시키지 않으며*,
- (iii) §5.5 9 sub-수단 본문 채택 + C-1~C-8 상태를 *변경* 하지 않으며,
- (iv) Backlog #3 (ST-1 T3) / Backlog #2 (GP-5 1.5차) / Backlog #4 (P1 v2 facade MVP) / Backlog #7 (Operational Readiness) 자동 진입을 *발효* 시키지 않으며,
- (v) 신규 ADR / 신규 P / 신규 GP 를 *발행* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **ST-2 단독 우선 진입 합의 보고서 진입 *직전* 의사결정 입력 정비 + 사용자 명시 4 결정 답습 문서상 확정**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. ST-2 합의 범위

### 1.1 본 brief / 합의가 *발생시키는* 것

1. ST-2 (inotify sidecar) **단독** 진입 *적격성* 권위 권고 확정
2. fail-closed 메커니즘 = **F-B 우선** 채택 권위 권고 (F-C 보조 / F-A 비채택)
3. Multi-host parity = **미요구** 권위 권고 (이번 ST-2 단독 진입 범위 한정)
4. inotify 감시 경로 = **`/run/secrets/*`** 권위 권고 (ADR-008 차단조건 #6 + 부록 B docker secret 답습)
5. secret rotation 정책 = **별도 합의 영역 분리** 권위 권고
6. sidecar 분리 구조 + inotify 감시 대상 + mtime/perm 감지 기준 + evidence 기준 + Rollback Trigger 권위 권고
7. 합의 형태 = **Reviewer-only 단축 합의** 적격 확정 (4 결정 충족 시)

### 1.2 본 brief / 합의가 *발생시키지 않는* 것

§0.3 답습 (13 금지 + 추가 영역).

---

## 2. ST-2 가 T2 인 이유

### 2.1 ADR-011 §2.4 T2 정의 답습

> "T2 = 사용자 승인 필수 — Skill/Memory promotion, 새 도구 등록, 합의 형태 결정"

ST-2 = sidecar container 추가 = **새 도구 등록 영역** (Hermes upstream 변경 0건 + repo policy 변경 0건).

### 2.2 mvp1.md §3.3.1 본문 직접 답습

| 항목 | ST-2 |
|------|------|
| 검증 시점 | 런타임 지속 |
| Hermes upstream 변경 | **❌** (sidecar 분리 가능) |
| sidecar 가능성 | **✅** |
| 운영 부담 | 中 (sidecar process 운영) |
| 권위 출처 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 답습 |

### 2.3 T3 영역 침범 0건 검증

| T3 침범 후보 | ST-2 |
|------------|------|
| Hermes upstream Dockerfile 변경 | ❌ 0건 (sidecar = 별도 container) |
| Constitution / ADR / Harness Gates 정의 변경 | ❌ 0건 (sidecar 추가 = 운영 layer, 정의 변경 0건) |
| Branch protection rule 변경 | ❌ 0건 (저장 경로 영역 한정) |
| Tier-2/3 catalog 확장 | ❌ 0건 (저장 경로 isolation = catalog 영역 외) |
| Vault HSM 통합 (ST-4) | ❌ 0건 (별도 항목, Operational Readiness 영역) |
| docker socket 접근 (F-A 비채택 답습) | ❌ 0건 (사용자 명시 #1 결정 답습 — F-A 비채택) |

**판정**: ST-2 = T2 영역 적격 (6/6 T3 침범 0건).

### 2.4 mvp1.md §3.3.2 권고 답습

> "MVP-1 1.5차 (보강) = ST-3 + **ST-2 inotify sidecar** (Hermes upstream 변경 회피 유지)"

본 권고가 ST-2 가 T2 영역 MVP-1 1.5차 보강 영역으로 직접 명시 — 별도 권위 확정 0건.

---

## 3. Hermes upstream 변경 0건 검증

### 3.1 본 sidecar 의 Hermes upstream 변경 후보

| 변경 후보 | 본 sidecar |
|---------|----------|
| Hermes Dockerfile entrypoint script 본문 변경 | ❌ 0건 (sidecar = 별도 container) |
| Hermes Dockerfile base image 변경 | ❌ 0건 |
| Hermes Dockerfile CMD / ENTRYPOINT 본문 변경 | ❌ 0건 |
| Hermes 환경 변수 / volume mount 변경 | ❌ 0건 (sidecar 가 별도 mount 보유) |
| Hermes 권한 (capability / user / privileged) 변경 | ❌ 0건 |
| Hermes upstream PR 제출 의무 | ❌ 0건 (sidecar = 본 repo 영역) |
| Hermes healthcheck *정의* (docker-compose level) | ⚠️ **healthcheck command/path 추가 가능성** — F-B 채택 시 (단, Hermes upstream Dockerfile 본문 0건 보존 — docker-compose level healthcheck) |

### 3.2 F-B 채택 시 Hermes 영향 분석 (사용자 #1 결정 답습)

**F-B 메커니즘**: sidecar 가 `/var/run/sidecar-status` 등 공유 volume 에 status file 기록 → Hermes container 의 `healthcheck` (docker-compose level) 가 해당 파일 read → unhealthy 처리.

| 영역 | F-B 영향 | T2/T3 |
|------|---------|------|
| Hermes upstream Dockerfile 본문 | ❌ 0건 변경 | T2 보존 |
| `docker-compose.yml` 의 Hermes service 정의 (healthcheck block 추가) | ✅ 추가 (repo-local 영역) | T2 (repo policy 변경 0건) |
| sidecar 가 Hermes 자체에 접근 | ❌ 0건 (sidecar = volume write 한정) | T2 보존 |
| docker socket / privileged 접근 | ❌ 0건 (F-A 비채택 답습) | T2 보존 |

**핵심**: F-B 채택 시 Hermes healthcheck *정의* 는 `docker-compose.yml` (repo-local) 에 추가 — **Hermes upstream Dockerfile 본문 변경 0건** 보존.

### 3.3 변경 발생 영역

| 영역 | 본 sidecar (구현 발효 시점, 본 brief 영역 외) |
|------|--------------------------------|
| `docker-compose.yml` (또는 동등 매니페스트) 신규 sidecar service block | ✅ 추가 |
| `docker-compose.yml` Hermes service healthcheck block 추가 (F-B 답습) | ✅ 추가 |
| `docker-compose.yml` 공유 volume 정의 (sidecar ↔ Hermes status file 공유) | ✅ 추가 |
| 신규 sidecar Dockerfile (예: `docker/inotify-sidecar/Dockerfile`) | ✅ 추가 |
| 신규 inotify 스크립트 (예: `docker/inotify-sidecar/watch.{sh,py}`) | ✅ 추가 |
| 신규 CI step (sidecar 동작 시뮬레이션 fixture) | ✅ 추가 |

**핵심**: ST-2 영향 = repo-local 신규 파일 + docker-compose 신규 service / healthcheck / volume 추가. **Hermes upstream 영역 (Dockerfile / image / PR / config) 변경 0건 보존**.

---

## 4. sidecar 분리 구조 (F-B 채택 답습)

### 4.1 권고 구조 (구현 결정 영역 — 본 brief 영역 외)

```
┌──────────────────────┐         ┌──────────────────────┐
│  Hermes container    │         │  inotify sidecar     │
│  (변경 0건)          │         │  container (신규)    │
│                      │         │                      │
│  /run/secrets/api_*  │◄────────│  inotify watch on    │
│  (read, runtime)     │  volume │  /run/secrets/*      │
└──────────────────────┘  share  │                      │
        │                        │  fail-closed action  │
        │ docker-compose         │  = status file write │
        │ healthcheck            │  /var/run/sidecar-   │
        │ reads:                 │      status          │
        │  /var/run/sidecar-     │                      │
        │      status            │                      │
        └────────────────────────┤                      │
        (F-B 답습 — docker-compose level)               │
                                 └──────────────────────┘
```

### 4.2 분리 메커니즘 (F-B 채택 답습)

| 영역 | 권한 |
|------|------|
| **sidecar volume mount** | `/run/secrets/*` = **read-only** (감시 한정 — 본문 read 권한도 sidecar = 최소화 권고, 본문 logging 영구 금지) |
| **sidecar → Hermes status 공유 volume** | sidecar = write / Hermes healthcheck = read |
| **sidecar 자체 권한** | non-root user (Dockerfile USER directive 권고), capability drop ALL + cap_add SYS_PTRACE 불필요 (inotify = unprivileged syscall) |
| **docker socket** | ❌ 미마운트 (F-A 비채택 답습) |
| **privileged flag** | ❌ false |
| **host network** | ❌ false (sidecar = bridge or none 권고) |

### 4.3 분리 *권한 한계* (사용자 명시 #1/#2 결정 답습)

- ❌ sidecar 가 Hermes 메인 container 의 process 자체에 접근하지 않음 (process namespace 분리 유지)
- ❌ sidecar 가 secret 본문 write 0건 (read-only mount 한정, 감시 = mtime/perm/존재 한정)
- ❌ sidecar 가 secret 본문 logging 금지 (R-4.1 답습 fake canary 의무)
- ❌ sidecar 가 host system 자체에 영향 미치지 않음 (host shutdown 0건)
- ❌ sidecar 가 다른 container 에 영향 미치지 않음 (cross-container kill 0건)
- ❌ sidecar 가 docker socket 접근하지 않음 (F-A 비채택 답습)
- ❌ sidecar 가 multi-host 영역 (다른 host 의 secret) 감시하지 않음 (Multi-host parity 미요구 답습)

---

## 5. inotify 감시 대상 (사용자 #3 결정 답습)

### 5.1 감시 경로 *결정* (사용자 명시 답습)

```
기본 감시 경로 = /run/secrets/*
```

| 항목 | 결정 |
|------|------|
| 경로 | **`/run/secrets/*`** |
| 사유 | docker secret 표준 mount 경로 + ST-3 docker secret 흐름과 정합 + Hermes upstream 변경 없이 sidecar 에서 감시 가능 |
| 권위 출처 | ADR-008 차단조건 #6 + 부록 B (docker secret) + mvp1.md §5.5.1 (ST-3 본문 채택 답습) |

### 5.2 감시 *제외* 영역

- ❌ Hermes container 내 일반 파일 (process / log / cache / application data) 0건
- ❌ docker-compose 외부 host filesystem 0건
- ❌ 다른 container 의 secret (cross-container 감시 0건 — Multi-host parity 미요구 답습)
- ❌ 사용자 정의 외부 경로 (현 brief = `/run/secrets/*` 한정, 사용자 정의 경로는 구현 시점 후보 — 본 brief 영역 외)

### 5.3 감시 *권한 한계*

- ❌ sidecar 가 secret 본문 read 후 logging 금지 (영구 금지 — R-4.1 답습)
- ❌ sidecar 가 secret 본문을 다른 file system / network 으로 export 금지
- ❌ sidecar 가 secret 본문 hashing 금지 (구현 결정 영역 — 본 brief 권고 = 0건)

### 5.4 사용자 정의 mount 경로 처리

| 영역 | 처리 |
|------|------|
| 사용자 정의 mount 경로 (`/var/lib/hermes/secrets/*` 등) | 구현 시점 후보로만 남기고, 이번 합의의 기본 경로는 `/run/secrets/*` 로 둠 (사용자 명시 답습) |
| 다중 경로 감시 (`/run/secrets/*` + 추가 경로) | 별도 합의 영역 — 본 brief 영역 외 |

---

## 6. mtime / permission 변경 감지 기준 + secret rotation 정책 분리 (사용자 #4 결정 답습)

### 6.1 inotify event 사용 후보

| inotify event | 발화 조건 | 본 brief 권고 |
|-------------|---------|----------|
| `IN_ATTRIB` | mtime / mode / owner 변경 | ✅ **권고** (mvp1.md §3.3.1 "mtime/perm 변경" 답습) |
| `IN_MODIFY` | 파일 내용 변경 | ✅ 권고 (secret 본문 변조 감지) |
| `IN_MOVE_SELF` / `IN_DELETE_SELF` | 파일 자체 이동/삭제 | ✅ 권고 (secret 파일 사라짐 감지) |
| `IN_CLOSE_WRITE` | write 후 close | ⚠️ 후보 (정상 init vs runtime 변조 구분 어려움 — grace period 적용 시 권고 가능) |
| `IN_ACCESS` | 읽기 access | ❌ **금지** (정상 secret read 가 매번 발화 — false positive 폭증) |

### 6.2 secret rotation 정책 *별도 합의 영역 분리* (사용자 #4 결정 답습)

| 시나리오 | sidecar 행동 (본 합의 범위) | secret rotation 정책 영역 (별도 합의) |
|---------|--------------------|---------------------------|
| **init 단계 (container 시작 시 secret 주입)** | sidecar = init 완료 후 감시 시작 (또는 grace period 적용 — 후보 5초~30초, 구현 결정 영역) | (이 단계는 정책 영역 외) |
| **runtime mtime / perm / content 변경** | **모든 runtime 변경 = fail-closed (사용자 #4 결정 답습)** | secret rotation 정책 = 별도 합의 (Operational Readiness / Multi-host / Vault HSM 와 연결 가능) |
| **외부 attack vector (chmod 644 등)** | sidecar = fail-closed (§7 F-B 답습) | (이 단계는 attack 영역, rotation 정책 영역 외) |

**핵심 결정 (사용자 #4 답습)**:

```
runtime secret 변경 = 기본적으로 fail-closed
secret rotation 정책 = 별도 합의 영역
```

연결 가능 후속 합의 영역:
- Operational Readiness (Backlog #7) — Multi-host parity 진입 시
- Vault HSM (ST-4, ADR-010) — 외부 secret rotation source 진입 시
- secret rotation 자체 정책 합의 (rotation interval / 알림 / 자동 재시작) — 별도 P 발행 가능성

### 6.3 threshold 후보 (mvp1.md §3.4.2 답습)

| Metric | 후보 정의 | threshold 후보 | 본 brief 권고 |
|--------|---------|--------------|-----------|
| `chmod_violation_detection` | chmod 644 등 644+ 권한 시 감지 비율 | 100% (PoC 격리 환경) | 100% 강제 |
| `inotify_event_response_time` | mtime/perm 변경 → status file write latency (F-B 답습) | < 1초 (mvp1.md §3.4.2 답습) | **threshold *결정* 영역 — 별도 합의** (실 환경 측정 후) |
| `secret_isolation_check` | secret 파일이 image layer 에 포함되지 않음 검증 | 0건 leak (강제) | 0건 강제 |
| `container_restart_recovery` | 컨테이너 정지 후 재시작 시 secret 재주입 정상 | 100% | 100% 강제 |
| `sidecar_uptime` | sidecar process alive (silent fail 검출) | 99%+ (PoC 격리 환경) | **threshold *결정* 영역 — 별도 합의** |
| `healthcheck_response_latency` (F-B 답습) | sidecar status file write → Hermes healthcheck read 까지 latency | < 5초 (docker-compose default healthcheck interval 30초 + retries 답습) | **threshold *결정* 영역 — 별도 합의** |

본 threshold = **후보 한정** (정량 *고정* = 별도 합의).

---

## 7. fail-closed 동작 (사용자 #1 결정 답습 — F-B 우선 / F-C 보조 / F-A 비채택)

### 7.1 3 옵션 매트릭스 + 결정

| 옵션 | 메커니즘 | 권한 부담 | T2/T3 | 6 trigger #5 발화 위험 | **사용자 결정** |
|------|---------|---------|-------|----------------|------------|
| F-A | sidecar → `docker stop <hermes-container>` via docker socket mount | 高 (root-equivalent) | T3 가능성 高 | ⚠️ 발화 | ❌ **비채택** |
| **F-B** | sidecar → status file 기록 (`/var/run/sidecar-status`) → Hermes healthcheck (docker-compose level) read 후 unhealthy 처리 | 低 (volume write 한정) | T2 | ❌ 0건 | ✅ **우선 채택** |
| F-C | sidecar → docker-compose `depends_on: condition: service_healthy` 활용 (sidecar 자체가 unhealthy 시 Hermes 정지) | 中 (docker-compose 정의 + sidecar healthcheck) | T2 | ❌ 0건 | ⚠️ **보조 후보** (F-B 외 보강 시 권고 가능) |

### 7.2 F-B 우선 채택 사유 (사용자 명시 답습)

- docker socket 접근 0건 (F-A 비채택 답습)
- 권한 부담 低 (sidecar = volume write 한정)
- T2 영역 유지
- Hermes upstream Dockerfile 변경 0건 (docker-compose level healthcheck — repo-local)
- T3 자동 진입 위험 0건
- 운영 정책 변경 영역 침범 0건

### 7.3 F-A 비채택 사유 (사용자 명시 답습)

- docker socket 접근 = root-equivalent 권한 영역
- 권한 영역 확대 = 운영 정책 변경 영역 진입
- T3 가능성 高 → 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 추가 발생
- 본 ST-2 단독 진입의 T2 영역 유지 의도와 충돌

### 7.4 F-C 보조 후보 유지 사유

- T2 영역 동일 보존
- F-B 채택 시 F-C 형태 (docker-compose depends_on) 와 *함께* 적용 가능 (F-B = primary signal / F-C = startup ordering 보강)
- F-B 단독 한계 발견 시 (예: healthcheck interval latency 지연) F-C 보강 진입 후속 합의 영역

### 7.5 fail-closed *권한 한계* (사용자 명시 #1 결정 답습)

- ❌ sidecar 가 Hermes container 의 process 자체를 kill 하지 않음 (F-A 비채택 답습)
- ❌ sidecar 가 docker socket 에 접근하지 않음 (F-A 비채택 답습)
- ❌ sidecar 가 privileged 권한 보유 0건
- ❌ sidecar 가 host system 자체에 영향 미치지 않음 (host shutdown 0건)
- ❌ sidecar 가 다른 container 에 영향 미치지 않음 (cross-container kill 0건)

### 7.6 6 escalation trigger #5 검증

| Trigger | 본 brief 발화 여부 |
|---------|--------------|
| #5 컨테이너 정지 방식이 운영 정책 변경으로 커짐 | **❌ 0건 발화** (F-A 비채택 + F-B 우선 채택 답습) |

**결론**: F-B 우선 채택 = T2 영역 유지 + 권한 영역 확대 0건 + 운영 정책 변경 영역 침범 0건 → 6 trigger #5 발화 0건.

---

## 8. evidence 기준

### 8.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (구현 발효 시점, 본 brief 영역 외)

| # | 조건 | ST-2 evidence |
|---|------|--------------|
| (a) | 동등 이상의 보안 결과 | docker secret (ST-3) + chmod 600 + **inotify 감시 (sidecar)** 동작 확인 + 통합 결과 R1-2 답습 동등 이상 + F-B status file write → Hermes unhealthy 시연 |
| (b) | 격리 환경 PoC 실증 | docker-compose isolation + chmod 644 시뮬레이션 → sidecar 감지 → F-B status file write → Hermes healthcheck unhealthy 시연 + mtime 변경 시뮬레이션 → 동상 + `IN_MODIFY` / `IN_ATTRIB` / `IN_MOVE_SELF` / `IN_DELETE_SELF` 4 event cover |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + GP-3 §5.3 + mvp1.md §3.3 + Backlog #1 brief §2.2 + 본 brief §2~§7 답습 |
| (d) | 자동 회귀 검증 경로 확보 | 신규 CI step (sidecar fixture 시뮬레이션) + actual run SUCCESS + nightly 권고 + `secret-hygiene-egress-redaction.yml` 확장 (또는 신규 workflow) |
| (e) | 합의 APPROVE | 본 합의 형태 (§10 답습) — **Reviewer-only 단축 합의 적격 확정** (4 결정 충족 시) |

### 8.2 evidence 형식 (구현 발효 시점, 본 brief 영역 외)

| Evidence | 형식 |
|----------|------|
| Markdown report | `docs/phase0/g2-gp3-mvp1-st2-evidence.md` (가칭) 또는 기존 `g2-gp3-mvp1-evidence.md` 확장 |
| JSONL ledger entry | `event:` enum 후보 = `secret_storage_inotify_isolation` (가칭) — Backlog #5 ADR-012 §2.2 별도 합의 영역 후속 등록 |
| Docker isolation log | sidecar 신규 fixture 시뮬레이션 → F-B status file write → Hermes healthcheck unhealthy evidence |
| GitHub Actions run | 신규 CI step (또는 `secret-hygiene-egress-redaction.yml` 확장) actual run id + step PASS |
| 합의 보고서 | 본 합의 (Reviewer-only 단축 합의 — `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md`) |

### 8.3 본 §8 의 *범위 한계*

- ❌ 실 evidence artifact 생성 (구현 발효 시점 별도 작업)
- ❌ event enum 정식 등록 (Backlog #5 ADR-012 §2.2 별도 합의)
- ❌ 합의 보고서 권위 발효 (본 brief = 준비안 한정)

---

## 9. Rollback Trigger

### 9.1 mvp1.md §3.5 답습 (GP-3 8 trigger 中 ST-2 영역)

| Trigger ID | 발화 조건 | 발화 시 행동 | 본 brief 발효 시점 |
|----------|---------|-------------|------------------|
| R-MVP1-G3-3 | Docker secret 도입 실패 후 보강 진입 | (이미 ST-2 진입 영역 — 본 합의 발효 후 미발화) | ❌ 미발화 |

### 9.2 ST-2 specific 신규 Rollback Trigger 후보 (본 brief 신규 권고)

| Trigger ID (가칭) | 발화 조건 | 발화 시 행동 |
|-----------------|---------|-------------|
| **R-ST2-1** | inotify kernel buffer overflow (event loss) | 풀 3+1 합의 + 버퍼 크기 재결정 또는 polling fallback 진입 |
| **R-ST2-2** | sidecar 자체 정지 (silent fail) | 풀 3+1 합의 + sidecar healthcheck 강제 + (F-C 보강 답습) Hermes 도 함께 정지 |
| **R-ST2-3** | 정상 secret rotation 시 sidecar 오탐 | secret rotation 정책 별도 합의 진입 (사용자 #4 결정 답습 — rotation = 별도 합의) |
| **R-ST2-4** | `inotify_event_response_time` threshold 미달 (> 1초) | threshold 재결정 합의 (단축 적격) |
| **R-ST2-5** | F-A (docker socket) 채택 *재검토* trigger | T3 영역 진입 → 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 (본 brief = F-A 비채택 답습) |
| **R-ST2-6** | sidecar 가 secret 본문 log / hash / export 노출 시 | 영구 금지 위반 → 즉시 합의 + 코드 수정 (R-4.1 답습) |
| **R-ST2-7** | Multi-host 환경 진입 시 sidecar parity 필요 | Operational Readiness 영역 진입 → Backlog #7 합의 (사용자 #2 결정 답습 — 본 brief 영역 외) |
| **R-ST2-8** (F-B 신규) | `healthcheck_response_latency` threshold 미달 (> 5초) | F-C 보강 진입 합의 또는 threshold 재결정 (단축 적격) |

### 9.3 본 §9 의 *범위 한계*

- ❌ 실 rollback fixture 생성 (구현 발효 시점)
- ❌ 실 trigger 발화 시연 (구현 발효 시점)
- ❌ threshold *고정* (> 1초 / > 5초 등 모두 *후보 한정* 유지)
- ❌ R-ST2-1~R-ST2-8 *정식 등록* (본 합의 발효 시 본문 채택 영역 후속)

---

## 10. 합의 형태 권고

### 10.1 6 escalation trigger 검증 매트릭스 (사용자 명시 4 결정 답습 후)

| # | 트리거 | 본 brief 발화 여부 (4 결정 답습 후) | 사유 |
|---|----|--------------|------|
| 1 | Hermes upstream Dockerfile 변경 필요 | ❌ **0건** | §3 답습 — sidecar = 별도 container, Hermes upstream 영역 0건 (F-B docker-compose level healthcheck) |
| 2 | ST-1 과 결합 필요 | ❌ **0건** | ST-1 = T3 영역, 본 합의 = ST-2 *단독* 진입 한정 + Backlog #3 병합 검토 권고 답습 |
| 3 | Vault HSM (ST-4) 와 결합 필요 | ❌ **0건** | ST-4 = Operational Readiness 영역 (ADR-010), 본 합의 = MVP-1 1.5차 영역 한정 |
| 4 | Tier-2 / Tier-3 catalog 확장 필요 | ❌ **0건** | ST-2 = 저장 경로 isolation 영역, catalog 영역 외 |
| 5 | 컨테이너 정지 방식이 운영 정책 변경으로 커짐 | ❌ **0건** | **사용자 #1 결정 답습 — F-B 우선 채택 + F-A 비채택** → docker socket 0건 + 권한 영역 확대 0건 |
| 6 | Operational Readiness 영역으로 넘어감 | ❌ **0건** | **사용자 #2 결정 답습 — Multi-host parity 미요구** → MVP-1 단일 host 영역 한정 |

**합산 = 6/6 0건 발화** (사용자 명시 4 결정 답습 후).

### 10.2 합의 형태 결정 트리 (4 결정 답습 결과)

```
ST-2 단독 진입 합의 형태 결정:

Q1. fail-closed 동작 = F-A (docker socket 접근) ?
  ├─ YES → 6 trigger #5 발화 → 풀 3+1 합의 권고
  └─ NO ── 사용자 #1 결정 답습 (F-B 우선, F-A 비채택) ✅

Q2. Multi-host parity 요구 ?
  ├─ YES → 6 trigger #6 발화 → 풀 3+1 합의 권고
  └─ NO ── 사용자 #2 결정 답습 (Multi-host 미요구) ✅

Q3. 다른 6 trigger (#1/#2/#3/#4) 발화 ?
  ├─ YES → 풀 3+1 합의 권고
  └─ NO ── §10.1 답습 (4/4 0건 발화) ✅

→ ✅ Reviewer-only 단축 합의 적격 확정
```

### 10.3 본 brief 최종 권고

**합의 형태 = Reviewer-only 단축 합의 적격 확정** (사용자 명시 4 결정 답습 후).

| 충족 조건 | 충족 여부 |
|------|-------|
| (a) fail-closed = F-B 우선 채택 (F-A 비채택) | ✅ **사용자 #1 결정 답습** |
| (b) Multi-host parity 미요구 (MVP-1 단일 host 답습) | ✅ **사용자 #2 결정 답습** |
| (c) inotify 감시 경로 = `/run/secrets/*` (ADR-008 차단조건 #6 + 부록 B 답습) | ✅ **사용자 #3 결정 답습** |
| (d) secret rotation 정책 = 별도 합의 영역 분리 | ✅ **사용자 #4 결정 답습** |
| (e) 6 trigger #1~#4 모두 0건 발화 | ✅ §10.1 답습 |
| (f) ST-2 단독 진입 (ST-1 / PC-4 / ST-4 결합 0건) | ✅ §1.2 + §10.1 #2/#3 답습 |

### 10.4 본 §10 의 *범위 한계*

- ❌ 합의 형태 *결정 발효* (본 brief = 권고 한정, 결정 발효 = 합의 보고서 영역)
- ❌ 합의 보고서 *작성* (별도 단계 — `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md`)
- ❌ 구현 진입 *발효* (별도 합의 + 사용자 명시)
- ❌ 사용자 명시 4 결정 *재변경* (본 brief = 4 결정 답습 한정)

---

## 11. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 (옵션 (A) + 4 결정) | ✅ (§0.1 + §0.2 답습) |
| 사용자 명시 금지 답습 (13 금지) | ✅ (§0.3 + 부록 A 답습) |
| ST-2 단독 진입 한정 (ST-1 / PC-4 / ST-4 결합 0건) | ✅ (§1.2 + §10.1 #2/#3 답습) |
| 사용자 #1 결정 (F-B 우선 / F-C 보조 / F-A 비채택) 답습 | ✅ (§7 답습) |
| 사용자 #2 결정 (Multi-host parity 미요구) 답습 | ✅ (§3 + §10.1 #6 답습) |
| 사용자 #3 결정 (`/run/secrets/*` 감시 경로) 답습 | ✅ (§5 답습) |
| 사용자 #4 결정 (secret rotation 정책 별도 합의 분리) 답습 | ✅ (§6.2 답습) |
| Hermes upstream Dockerfile 변경 0건 | ✅ (§3 답습) |
| T3 자동 진입 0건 | ✅ (§2.3 답습) |
| 6 escalation trigger 6/6 0건 발화 | ✅ (§10.1 답습) |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| C-1~C-8 상태 변경 0건 (§C-5 Deferred 유지) | ✅ |
| 다른 backlog (#2/#3/#4/#7) 자동 진입 0건 | ✅ |
| MVP-1 PASS 재선언 / Layer E / Layer F 격상 0건 | ✅ |
| 합의 보고서 / commit / push 0건 (본 brief = 파일 작성 한정) | ✅ |
| Provider Liquidity 5-way / 5 영구 핵심 제약 보존 | ✅ |

---

## 12. 본 brief 요약 (한 단락)

본 brief 는 **ST-2 (inotify sidecar) *단독 우선* 진입 합의 *준비안* (DRAFT)** 이다. Backlog #1 진입 *직전* 사전 정비 합의 (`43b898c`) 발효 후속, 사용자 명시 4 결정 답습 *문서상 확정* — (1) fail-closed = **F-B 우선** (sidecar → status file → Hermes healthcheck unhealthy) / F-C 보조 / **F-A 비채택** (docker socket 권한 영역 회피) / (2) **Multi-host parity 미요구** (MVP-1 단일 host 한정) / (3) inotify 감시 경로 = **`/run/secrets/*`** (ADR-008 차단조건 #6 + 부록 B docker secret 답습) / (4) **runtime secret 변경 = fail-closed + secret rotation 정책 = 별도 합의 영역 분리**. 본 brief 12 섹션 (합의 범위 / T2 사유 / Hermes upstream 변경 0건 검증 / sidecar 분리 구조 / inotify 감시 대상 / mtime·permission 감지 기준 + secret rotation 정책 분리 / fail-closed 동작 (F-B 우선 / F-C 보조 / F-A 비채택) / evidence 기준 (ADR-011 §2.1 (a)~(e) 5조건) / Rollback Trigger 8 후보 / 합의 형태 권고) 정비. **6 escalation trigger 6/6 0건 발화** (4 결정 답습 결과 — Hermes upstream 변경 / ST-1 결합 / ST-4 결합 / Tier-2-3 catalog / 컨테이너 정지 방식 / Operational Readiness 모두 0건). **최종 권고 = Reviewer-only 단축 합의 적격 확정**. **본 brief 는 ST-2 *실 구현* / docker-compose 변경 / CI workflow / hook / ST-1 / PC-4 / ST-4 / Multi-host parity 자동 진입 / T3 자동 진입 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / §C-5 Satisfied 자동 갱신 / 합의 보고서 권위 / CONTEXT-INDEX-SESSION 갱신 모두 0건** (사용자 명시 답습). 다음 단계 = 합의 보고서 작성 (별도 commit) — 본 brief commit 후속.

---

## 부록 A. 금지 사항 (사용자 명시 답습 — 13 금지)

- ❌ ST-2 *실 구현* (sidecar Dockerfile / inotify 스크립트 / docker-compose 변경 0건)
- ❌ sidecar Dockerfile 작성 0건
- ❌ inotify script 작성 0건
- ❌ docker-compose 변경 0건
- ❌ CI workflow 변경 0건
- ❌ ST-1 자동 진입 0건
- ❌ PC-4 자동 진입 0건
- ❌ ST-4 / Vault HSM 자동 진입 0건
- ❌ Multi-host parity 자동 진입 0건
- ❌ MVP-1 PASS 재선언 0건
- ❌ Operational Readiness PASS 선언 0건
- ❌ Hermes PMO 격상 선언 0건
- ❌ §C-5 Satisfied 자동 갱신 0건

추가 답습 (본 brief 자체 영역):
- ❌ 합의 보고서 *작성* 0건 (본 brief = 파일화 한정, 합의 보고서 = 별도 commit)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리)
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건
- ❌ ADR 본문 자동 갱신 0건
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화 0건

---

**상태**: DRAFT (사용자 명시 4 결정 반영 + 합의 보고서 진입 *직전*)
**다음 단계**: Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md`) — 별도 commit
**사용자 명시 답습 4 결정**:
1. fail-closed = **F-B 우선** / F-C 보조 / **F-A 비채택**
2. Multi-host parity = **미요구**
3. inotify 감시 경로 = **`/run/secrets/*`**
4. secret rotation 정책 = **별도 합의 영역 분리** (runtime 변경 = fail-closed)
