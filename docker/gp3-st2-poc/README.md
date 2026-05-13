# GP-3 ST-2 inotify sidecar PoC (격리 디렉토리)

> **Backlog #1 ST-2 inotify sidecar MVP-1 1.5차 보강 PoC** — Cycle 1 (PoC 격리 디렉토리 + README scaffold) 한정 진입.
>
> 본 디렉토리는 **PoC 격리 영역** — production `docker-compose.yml` 영향 0건, Hermes upstream Dockerfile 영향 0건.

---

## 1. 본 PoC 의 목적

GP-3 (Credential / Secret Hygiene) 저장 경로 secret 보호 영역의 **MVP-1 1.5차 보강 (ST-2)** — secret 파일의 mtime/permission 변경을 inotify 로 감시하여 fail-closed 처리하는 sidecar container 의 격리 검증.

### 1.1 권위 출처

- **상위 합의**:
  - Backlog #1 진입 *직전* 사전 정비 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (`43b898c`, APPROVE AS BRIEF)
  - ST-2 단독 우선 진입 적격성 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md` (`0e99a56`, APPROVE)
  - ST-2 실 구현 진입 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-implementation-entry.md` (`6c616a8`, APPROVE)
- **상위 brief**:
  - ST-2 단독 진입 적격성 brief = `docs/phase0/backlog1-st2-inotify-sidecar-brief.md` (`d9ae98b`)
  - ST-2 실 구현 brief = `docs/phase0/backlog1-st2-implementation-brief.md` (`997ca18`)
- **권위 문서**:
  - ADR-008 §A.2 R1-2 (저장 경로 secret 보호) + §2.6.2 R2-1 (docker secret)
  - GP-3 §5.3 (강제 메커니즘 — "inotify 런타임 감시")
  - MVP-1 deepening roadmap §3.3 (ST-1~ST-5) + §3.4.2 (metric 후보)
  - ADR-011 §2.1 (a)~(e) (5조건 패턴) + §2.4 (T1/T2/T3 분류)

---

## 2. 사용자 명시 9 결정 답습

### 2.1 선행 4 결정 (`0e99a56` 답습)

1. **fail-closed = F-B 우선 / F-C 보조 / F-A 비채택**
   - F-B = sidecar → status file (`/var/run/sidecar-status`) → hermes-mock healthcheck unhealthy (docker-compose level)
   - F-C = `depends_on: service_healthy` (sidecar healthy → hermes-mock 시작 보장)
   - F-A = docker socket → `docker stop` (root-equivalent 권한 영역) — **비채택**
2. **Multi-host parity = 미요구** (MVP-1 단일 host 한정, Backlog #7 Operational Readiness 영역 분리)
3. **inotify 감시 경로 = `/run/secrets/*`** (ADR-008 §2.6.2 R2-1 docker secret 답습, ST-3 정합)
4. **runtime secret 변경 = fail-closed + secret rotation 정책 = 별도 합의 영역 분리** (Operational Readiness / Vault HSM ST-4 / rotation 자체 정책 별도 P)

### 2.2 신규 5 결정 (`6c616a8` 답습)

5. **inotify watch 구현 = `inotifywait`** (inotify-tools 패키지, sidecar Dockerfile PoC 범위 내 한정)
6. **Cycle 3 commit = `test` + `feat` 2 commit 분리** (TDD RED/GREEN + 추적성)
7. **§C-5 갱신 = γ sub-condition 분리** (C-5a = ST-2 / C-5b = ST-1 / C-5c = PC-4)
8. **init grace period T2 = 10초**
9. **healthcheck interval = 5초**

---

## 3. PoC 격리 영역 분리 명시

### 3.1 격리 디렉토리 = 본 `docker/gp3-st2-poc/`

| 영역 | 본 PoC 영향 |
|------|----------|
| **본 디렉토리 (`docker/gp3-st2-poc/**`)** | ✅ PoC 격리 — sidecar Dockerfile / inotify 스크립트 / docker-compose / hermes-mock |
| Production `docker-compose.yml` | ❌ **변경 0건** (사용자 명시 답습) |
| Hermes upstream Dockerfile | ❌ **변경 0건** (`0e99a56` 답습) |
| 실 Hermes container | ❌ **영향 0건** (PoC = mock Hermes 한정) |
| Tier-1 / Tier-2 / Tier-3 catalog | ❌ 변경 0건 (저장 경로 isolation = catalog 영역 외) |
| ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 | ❌ 변경 0건 (cross-reference 답습 한정) |

### 3.2 Sibling PoC 디렉토리 와의 관계

| Sibling | 영역 | 본 PoC 와의 관계 |
|---------|------|--------------|
| `docker/gp3-st3-poc/` | ST-3 (docker secret 직접 사용) PoC | **상호 보완** — ST-3 (저장 경로 isolation) + ST-2 (런타임 감시) = "ST-3 + ST-2" 통합 권고 (mvp1.md §3.3.2 답습) |
| `docker/r2-poc/` | R-2 Docker isolation 검증 PoC | 격리 패턴 답습 (network_mode: none / read_only / cap_drop ALL) |
| `docker/r4-1-poc/` | R-4.1 Tier-1 catalog 검증 PoC | fake canary 의무 답습 (실 secret 본문 commit 0건) |

본 PoC 는 sibling 격리 디렉토리 패턴 답습 — production 영역 분리 보존.

---

## 4. 6 Cycle 분할안

| Cycle | 영역 | 신규 파일 | 기존 확장 | commit 형태 |
|-------|------|--------|----------|----------|
| **Cycle 1** ✅ 본 단계 | PoC 격리 디렉토리 + README scaffold | `docker/gp3-st2-poc/README.md` (본 파일) | 0건 | 1 commit (`feat(g2-gp3): scaffold ST-2 PoC isolated directory`) |
| Cycle 2 ⏳ | fixture 5개 (pass 2 + fail 3) | `tests/fixtures/gp3_st2/{pass,fail}/...` | 0건 | 1 commit (`test(g2-gp3): add ST-2 inotify sidecar fixtures`) |
| Cycle 3 ⏳ | sidecar Dockerfile + watch-secrets.sh + docker-compose + hermes-mock | 4~5 파일 | 0건 | **test + feat 2 commit 분리** (사용자 #6 결정 답습) |
| Cycle 4 ⏳ | CI step + tool 스크립트 | `tools/docker_secret_inotify_sidecar_check.sh` | `.github/workflows/secret-hygiene-egress-redaction.yml` | 2 commit (tool + step) |
| Cycle 5 ⏳ | summary.json 신규 필드 + ledger candidate + evidence form | (Cycle 4 workflow 內 통합 가능) | (Cycle 4 內) | 1 commit |
| Cycle 6 ⏳ | push + actual run 검증 + §C-5a 갱신 권고 | 0건 | 0건 | 0 commit (push + actual run + 별도 합의) |

**합산 예상**: Cycle 1~5 = 약 6~7 commit + Cycle 6 push + 메타 commit 별도.

### 4.1 의존성 그래프

```
Cycle 1 (디렉토리 + README) ←── 본 단계
   │
   ▼
Cycle 2 (fixture 5개)
   │
   ▼
Cycle 3 (sidecar 구현, test + feat 2 commit)
   │
   ▼
Cycle 4 (CI step + tool)
   │
   ▼
Cycle 5 (evidence + summary.json)
   │
   ▼
Cycle 6 (push + actual run + §C-5a 갱신 권고)
```

### 4.2 Cycle 진입 자동화 0건

- ✅ **Cycle 1 한정 진입** (본 PoC 디렉토리 + README scaffold)
- ❌ **Cycle 2~6 자동 진입 0건** — 각 Cycle = 사용자 명시 결정 후 별도 진입

---

## 5. 향후 신규 파일 후보 (Cycle 2~5 영역 — 본 단계 미작성)

본 디렉토리 內 향후 추가될 파일 (Cycle 별 작성 예정 — 본 Cycle 1 = 작성 0건):

| Cycle | 파일 | 영역 |
|-------|------|------|
| Cycle 3 | `Dockerfile` | sidecar image (alpine + inotify-tools + non-root + cap drop ALL) |
| Cycle 3 | `watch-secrets.sh` | inotifywait shell 스크립트 (init grace 10초 + status file write) |
| Cycle 3 | `docker-compose.gp3-st2.yml` | PoC 격리 docker-compose (sidecar + hermes-mock + 2 named volume + healthcheck interval 5s) |
| Cycle 3 | `hermes-mock/Dockerfile` (또는 inline 정의) | hermes-mock image (alpine + healthcheck script) |
| Cycle 2 | (별도 위치 — `tests/fixtures/gp3_st2/`) | fixture 5개 (pass 2 + fail 3) |
| Cycle 4 | (별도 위치 — `tools/docker_secret_inotify_sidecar_check.sh`) | CI step 호출 도구 |
| Cycle 4 | (별도 위치 — `.github/workflows/secret-hygiene-egress-redaction.yml` 확장) | CI workflow step |

**본 Cycle 1 시점**: 위 파일 모두 **미작성** (사용자 명시 답습 — "Cycle 1은 PoC 격리 디렉토리 구조 설계 + README 까지만 진행").

---

## 6. 안전 원칙 (영구 강제)

### 6.1 영구 금지 영역

| # | 금지 | 사유 |
|---|------|------|
| 1 | 실 secret 본문 commit | R-4.1 답습 (영구 금지) — fake canary 의무 (`FAKE_CANARY_DO_NOT_USE_*` prefix) |
| 2 | sidecar 가 secret 본문 logging / hashing / export | sidecar = mtime/perm 감시 한정, 본문 처리 0건 |
| 3 | docker socket 마운트 | F-A 비채택 답습 (사용자 #1 결정) — root-equivalent 권한 영역 회피 |
| 4 | privileged flag | 권한 부담 영역 회피 |
| 5 | host network | sidecar = bridge or none 권고 |
| 6 | 다른 container 의 secret 감시 (cross-container) | Multi-host parity 미요구 답습 (사용자 #2 결정) |
| 7 | Production `docker-compose.yml` 또는 Hermes upstream Dockerfile 변경 | PoC 격리 한정 답습 |
| 8 | 실 API key / provider SDK / 외부 API 호출 | fake canary 의무 답습 |

### 6.2 sidecar 권한 한계

- ❌ Hermes container 의 process 자체 접근 (process namespace 분리 유지)
- ❌ host system 영향 (host shutdown 0건)
- ❌ 다른 container kill (cross-container 0건)
- ❌ docker daemon 직접 통제 (docker socket 0건)

### 6.3 본문 채택 ≠ 실 구현

본 README 작성 = **PoC 격리 디렉토리 scaffold + 문서 한정**. 다음은 본 Cycle 1 영역 외:
- ❌ sidecar Dockerfile / inotify 스크립트 / docker-compose / hermes-mock 본문 작성
- ❌ fixture 작성 (Cycle 2)
- ❌ CI workflow 변경 (Cycle 4)
- ❌ actual run 실행 (Cycle 6)
- ❌ §C-5 / C-5a Satisfied 자동 갱신 (Cycle 6 후속 별도 합의)

---

## 7. 사용 가이드 (Cycle 6 후 예상 — 본 Cycle 1 시점 미가용)

```bash
# (Cycle 6 후 시점 가용 — 본 Cycle 1 시점 미가용)
# 1. PoC 환경 시작
cd docker/gp3-st2-poc/
docker-compose -f docker-compose.gp3-st2.yml up -d

# 2. 정상 운영 fixture 검증 (Cycle 2)
docker exec inotify-sidecar cat /var/run/sidecar-status
# expected: empty (정상)

# 3. fail-closed fixture 시뮬레이션 (예: chmod 644)
docker exec hermes-mock chmod 644 /run/secrets/mock_api_key
sleep 6  # healthcheck interval 5s 답습
docker exec inotify-sidecar cat /var/run/sidecar-status
# expected: "UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <ts>"
docker inspect hermes-mock --format='{{.State.Health.Status}}'
# expected: "unhealthy"

# 4. 정리
docker-compose -f docker-compose.gp3-st2.yml down
```

**경고**: 위 명령은 Cycle 3 이후 작성될 파일 (`Dockerfile`, `watch-secrets.sh`, `docker-compose.gp3-st2.yml`, `hermes-mock/`) 가 존재할 때만 동작. **본 Cycle 1 시점에서는 미가용**.

---

## 8. §C-5 Satisfied 갱신 조건 (Cycle 6 후속)

### 8.1 γ sub-condition 분리 답습 (사용자 #7 결정)

```
C-5 (GP-3 1.5차 보강 — Backlog #1) → 분리:
  C-5a = ST-2 (inotify sidecar) ← 본 PoC 영역
  C-5b = ST-1 (entrypoint stat)  ← Backlog #3 T3 영역
  C-5c = PC-4 (local pre-commit framework) ← Backlog #1 + #2 분리 영역
```

### 8.2 C-5a Satisfied 갱신 조건 (Cycle 6 후속 — 본 PoC 영역 외)

| 조건 | 충족 |
|------|------|
| (a) Cycle 6 actual run SUCCESS = 9/9 | (Cycle 6 시점 결정) |
| (b) ADR-011 §2.1 (a)~(e) 5조건 충족 | (Cycle 6 시점 결정) |
| (c) Evidence Markdown report + JSONL ledger candidate | (Cycle 5 + Cycle 6) |
| (d) 사용자 명시 9 결정 답습 보존 | (전체 cycle 강제) |
| (e) C-5a 갱신 합의 (Reviewer-only 단축 또는 풀 3+1) | (Cycle 6 후속 별도) |

### 8.3 본 Cycle 1 시점 §C-5 상태

§C-5 = **Deferred** 그대로 유지 — γ sub-condition 분리는 *권고* 한정. C-5a Satisfied 갱신 = Cycle 6 후속 별도 합의 영역.

---

## 9. 변경 0건 영역 (강제)

| 영역 | 변경 0건 사유 |
|------|------------|
| Production `docker-compose.yml` | PoC 격리 한정 (사용자 명시 답습) |
| Hermes upstream Dockerfile | `0e99a56` 답습 (Hermes upstream 변경 회피 유지) |
| `tools/secret_scanner.py` (Group D, Stage 1 영역) | ST-2 영역 외 (GP-3 코드 본문 검출 영역) |
| `tools/provider_*_scanner.py` (Group A, Stage 3 영역) | GP-5 영역 (Backlog #2) |
| `.importlinter` / `requirements-dev.txt` | GP-5 영역 |
| ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 | cross-reference 답습 한정 |
| `implementation-runtime-roadmap-mvp1.md` §3 / §4 / §5.5 본문 | 답습 한정 |
| Layer D 합의 보고서 본문 (`210c98f`) | γ sub-condition 분리도 *권고* 한정 — Cycle 6 후속 합의에서 본문 변경 |

---

## 10. 본 README 메타 검증

| 메타 검증 | 본 README |
|---------|--------|
| Cycle 1 사용자 명시 진입 범위 답습 (PoC 격리 디렉토리 + README scaffold 한정) | ✅ |
| 사용자 명시 9 결정 답습 (선행 4 + 신규 5) | ✅ |
| 6 Cycle 분할안 명시 + Cycle 1 한정 진입 | ✅ |
| Cycle 2~6 자동 진입 0건 명시 | ✅ |
| Production `docker-compose.yml` / Hermes upstream Dockerfile 변경 0건 | ✅ |
| T3 자동 진입 0건 (10/10 침범 후보 0건) | ✅ |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| §C-5 Deferred 그대로 유지 (γ sub-condition 분리 = 권고 한정) | ✅ |
| MVP-1 PASS *재선언* / Layer E / Layer F 격상 0건 | ✅ |
| sibling PoC 디렉토리 (`gp3-st3-poc/`, `r2-poc/`, `r4-1-poc/`) 패턴 답습 | ✅ |
| 실 secret 본문 commit 0건 (영구 금지) | ✅ |

---

## 11. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 Cycle 1 commit 완료 후 사용자 결정 영역:

| 옵션 | 영역 |
|------|------|
| (A) | Cycle 2 진입 (fixture 5개 작성) |
| (B) | Cycle 1 commit + CONTEXT / INDEX / SESSION 메타 갱신 commit + push (다음 cycle 전 결과 정착) |
| (C) | 보류 → 다른 backlog 우선 |
| (D) | 세션 종료 |

⚠️ **Cycle 2~6 자동 진입 금지** — 사용자 명시 결정 영역 (`6c616a8` 답습).

---

**작성일**: 2026-05-13 후속 26 (Cycle 1)
**상태**: scaffold (PoC 격리 디렉토리 + README 한정 — sidecar 구현 본문 미작성)
**다음 단계**: 사용자 명시 결정 영역 (Cycle 2 진입 또는 메타 commit + push 또는 보류 또는 세션 종료)
