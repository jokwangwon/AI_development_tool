# ST-2 PoC scripts — Cycle 3 test/scaffold

> Cycle 3 test/scaffold commit 영역 — sidecar 본문 (Cycle 3 feat commit) 발효 후 실행 가능.

## 1. `run-poc-fixture.sh`

ST-2 PoC fixture (Cycle 2 답습) 를 docker-compose 환경에서 시연하는 **local helper**.

### 사용

```sh
./scripts/run-poc-fixture.sh pass/normal_operation
./scripts/run-poc-fixture.sh pass/init_phase
./scripts/run-poc-fixture.sh fail/chmod_644
./scripts/run-poc-fixture.sh fail/content_modified
./scripts/run-poc-fixture.sh fail/file_deleted
```

### 기대 결과 (Cycle 3 feat commit 발효 후)

| Fixture | sidecar status | hermes-mock health |
|---------|--------------|------------------|
| pass/normal_operation | empty | healthy |
| pass/init_phase | empty | healthy |
| fail/chmod_644 | `UNHEALTHY: ATTRIB ...` | unhealthy |
| fail/content_modified | `UNHEALTHY: MODIFY ...` | unhealthy |
| fail/file_deleted | `UNHEALTHY: DELETE ...` | unhealthy |

### Cycle 3 test/scaffold (현 commit) 시점 동작

Cycle 3 feat commit 미진입 상태 (`docker-compose.gp3-st2.yml` 미작성) → 본 script 실행 시:

```
ERROR: docker-compose file not found: docker/gp3-st2-poc/docker-compose.gp3-st2.yml

This is expected in Cycle 3 test/scaffold commit (RED state).
Run after Cycle 3 feat commit lands.
```

exit code = 3 (RED state — TDD 답습).

## 2. Cycle 영역

- **Cycle 3 test/scaffold (본 commit)** = 본 script + hermes-mock scaffold
- **Cycle 3 feat (별도 commit)** = sidecar Dockerfile + watch-secrets.sh + docker-compose.gp3-st2.yml → 본 script GREEN 전환
- Cycle 4 = CI 호출 wrapper (`tools/docker_secret_inotify_sidecar_check.sh`)
- Cycle 6 = actual run 시연 (GitHub Actions workflow)

## 3. 사용자 명시 9 결정 답습 (본 script 관련)

| # | 결정 | 본 script 반영 |
|---|------|----------|
| 1 | F-A 비채택 | 본 script 가 docker socket 직접 접근 0건 (`docker compose` 명령은 호스트 docker daemon 호출 — 본 script 외부 호출 영역, sidecar/hermes-mock 내부는 0건 유지) |
| 3 | /run/secrets/* 감시 | SIDECAR_FIXTURE_DIR env var → docker-compose bind mount → /run/secrets/ |
| 8 | init grace 10초 | 본 script 의 INIT_WAIT=18s (init grace 10s + start_period 여유) |
| 9 | healthcheck interval 5초 | 본 script 의 FAIL_WAIT=15s (interval × retries 2 + buffer) |

## 4. 영구 강제 안전 원칙

- secret 본문 logging / hashing / export 0건 (R-4.1 답습) — 본 script 는 sidecar status `event metadata` 만 출력, secret content 노출 0건
- production docker-compose 변경 0건 (본 script 가 사용하는 compose file = PoC 격리)
- Hermes upstream Dockerfile 변경 0건
- ST-1 / PC-4 / T3 영역 자동 진입 0건
- 본 script 실행 시 fixture run-secrets/ 변경 가능성 = **fail/* simulate.sh 한정** — pass/* 는 변경 0건
  - fail/* simulate.sh 의 변경 = docker volume / bind mount 영역 내부 (host fixture 디렉토리 자체 보호는 Cycle 3 feat commit 의 fixture-init 답습)

## 5. 본 script 가 *하지 않는* 것

- ❌ CI workflow 변경 (Cycle 4 영역)
- ❌ actual run 자동 트리거 (Cycle 6 영역)
- ❌ §C-5 / C-5a Satisfied 자동 갱신
- ❌ Cycle 4 자동 진입
- ❌ MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상
