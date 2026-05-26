#!/bin/sh
# ST-2 PoC fixture runner — Cycle 3 test/scaffold (RED state)
#
# 본 script 는 Cycle 2 fixture (tests/fixtures/gp3_st2/) 를 ST-2 PoC docker-compose
# 환경에서 시연하는 local helper.
#
# Cycle 3 feat commit (docker-compose.gp3-st2.yml + sidecar Dockerfile + watch-secrets.sh)
# 발효 후 실행 가능. 본 commit (test/scaffold) 시점에는 docker-compose 미작성 상태
# → 실행 시 명확한 ERROR 출력 후 exit 3 (RED state — TDD 답습).
#
# 사용:
#   ./scripts/run-poc-fixture.sh <fixture_relative_path>
#
# 예시:
#   ./scripts/run-poc-fixture.sh pass/normal_operation
#   ./scripts/run-poc-fixture.sh fail/chmod_644
#
# 기대 결과 (Cycle 3 feat commit 후):
#   pass/* → hermes-mock = healthy, sidecar status empty
#   fail/* → simulate.sh 실행 → hermes-mock = unhealthy, sidecar status "UNHEALTHY: <event> ..."
#
# 사용자 명시 9 결정 답습:
#   - F-A 비채택: docker socket 접근 0건 (본 script + docker-compose 양쪽)
#   - 사용자 #8: init grace 10초 — 대기 시간에 반영
#   - 사용자 #9: healthcheck interval 5초 — fail-closed 전파 대기 시간에 반영
#
# 영구 강제 안전 원칙:
#   - production docker-compose 변경 0건 (본 script 가 사용하는 compose file = PoC 격리)
#   - Hermes upstream Dockerfile 변경 0건
#   - sidecar 가 secret 본문 logging / hashing / export 0건 (Cycle 3 feat commit 강제)
#   - status content 본문 출력 0건 (event metadata 만 표시)
#
# Cycle 영역:
#   - Cycle 3 = 본 script scaffold (commit 1) + docker-compose + sidecar (commit 2)
#   - Cycle 4 = 본 script 의 CI 호출 wrapper (`tools/docker_secret_inotify_sidecar_check.sh`)
#   - Cycle 6 = actual run 시연 (GitHub Actions workflow)

set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
POC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$POC_DIR/../.." && pwd)"

COMPOSE_FILE="$POC_DIR/docker-compose.gp3-st2.yml"
FIXTURE_BASE="$REPO_ROOT/tests/fixtures/gp3_st2"

# Args validation
FIXTURE="${1:-}"
if [ -z "$FIXTURE" ]; then
    cat <<'USAGE' >&2
Usage: run-poc-fixture.sh <fixture_relative_path>

Available fixtures (Cycle 2 답습):
  pass/normal_operation
  pass/init_phase
  fail/chmod_644
  fail/content_modified
  fail/file_deleted
USAGE
    exit 2
fi

FIXTURE_DIR="$FIXTURE_BASE/$FIXTURE"
if [ ! -d "$FIXTURE_DIR" ]; then
    echo "ERROR: fixture directory not found: $FIXTURE_DIR" >&2
    exit 2
fi

RUN_SECRETS_DIR="$FIXTURE_DIR/run-secrets"
if [ ! -d "$RUN_SECRETS_DIR" ]; then
    echo "ERROR: fixture run-secrets/ not found: $RUN_SECRETS_DIR" >&2
    exit 2
fi

# Cycle 3 feat commit 의존성 확인 (RED state — commit 2 미진입 시 명확한 안내 후 종료)
if [ ! -f "$COMPOSE_FILE" ]; then
    cat <<MSG >&2
ERROR: docker-compose file not found: $COMPOSE_FILE

This is expected in Cycle 3 test/scaffold commit (RED state).
Run after Cycle 3 feat commit lands:
  - docker/gp3-st2-poc/Dockerfile
  - docker/gp3-st2-poc/watch-secrets.sh
  - docker/gp3-st2-poc/docker-compose.gp3-st2.yml
MSG
    exit 3
fi

# docker / docker compose 확인
if ! command -v docker >/dev/null 2>&1; then
    echo "ERROR: docker command not found" >&2
    exit 4
fi

echo "[run-poc-fixture] fixture = $FIXTURE"
echo "[run-poc-fixture] fixture dir = $FIXTURE_DIR"
echo "[run-poc-fixture] compose file = $COMPOSE_FILE"

# Export fixture path for docker-compose bind mount
export SIDECAR_FIXTURE_DIR="$FIXTURE_DIR"

# Cleanup any previous state
echo "[run-poc-fixture] pre-cleanup (down --volumes)"
docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans 2>/dev/null || true

# Start docker-compose
echo "[run-poc-fixture] docker compose up -d (build + start)"
docker compose -f "$COMPOSE_FILE" up -d --build

# Wait for init grace + buffer (사용자 #8 결정: 10초 + start_period 여유)
INIT_WAIT=18
echo "[run-poc-fixture] waiting init grace + startup (${INIT_WAIT}s)..."
sleep "$INIT_WAIT"

# Branch on fixture type
case "$FIXTURE" in
    pass/*)
        echo "[run-poc-fixture] PASS scenario — no simulate.sh execution"
        # Wait additional time to confirm no event fires
        EXTRA_WAIT=8
        echo "[run-poc-fixture] waiting ${EXTRA_WAIT}s to confirm no spurious events..."
        sleep "$EXTRA_WAIT"
        ;;
    fail/*)
        SIMULATE_IN_CONTAINER="/fixtures/$FIXTURE/simulate.sh"
        echo "[run-poc-fixture] FAIL scenario — executing $SIMULATE_IN_CONTAINER inside hermes-mock"
        docker compose -f "$COMPOSE_FILE" exec -T hermes-mock "$SIMULATE_IN_CONTAINER" || \
            echo "[run-poc-fixture] simulate.sh exit non-zero (may be expected depending on fixture)" >&2
        # Wait for fail-closed signal propagation:
        # inotify event → status file (immediate)
        # healthcheck interval 5s × retries 2 = ~10s
        # buffer 5s
        FAIL_WAIT=15
        echo "[run-poc-fixture] waiting fail-closed signal propagation (${FAIL_WAIT}s)..."
        sleep "$FAIL_WAIT"
        ;;
    *)
        echo "ERROR: unknown fixture type: $FIXTURE (expected pass/* or fail/*)" >&2
        docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans
        exit 2
        ;;
esac

# Report state — event metadata 만 출력 (status content 본문 노출 회피)
echo ""
echo "===== sidecar status (event metadata only) ====="
docker compose -f "$COMPOSE_FILE" exec -T inotify-sidecar /bin/sh -c \
    'if [ -s /var/sidecar-status/status ]; then echo "STATUS: $(cat /var/sidecar-status/status)"; else echo "STATUS: (empty - healthy)"; fi' \
    2>/dev/null || echo "(could not read sidecar status)"

echo ""
echo "===== hermes-mock health ====="
docker inspect gp3-st2-hermes-mock --format='{{.State.Health.Status}}' 2>/dev/null || \
    docker compose -f "$COMPOSE_FILE" ps hermes-mock

echo ""
echo "===== inotify-sidecar health ====="
docker inspect gp3-st2-inotify-sidecar --format='{{.State.Health.Status}}' 2>/dev/null || \
    docker compose -f "$COMPOSE_FILE" ps inotify-sidecar

# Cleanup
echo ""
echo "[run-poc-fixture] cleanup (down --volumes)"
docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans

echo "[run-poc-fixture] done"
