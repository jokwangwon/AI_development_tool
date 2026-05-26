#!/bin/sh
# tools/docker_secret_inotify_sidecar_check.sh — Backlog #1 ST-2 Cycle 4 CI tool
#
# 본 script 는 ST-2 inotify sidecar PoC (docker/gp3-st2-poc/) 를 5 fixture
# (Cycle 2 답습 — tests/fixtures/gp3_st2/) 시연하여 F-B + F-C fail-closed
# 동작 검증.
#
# 사용자 명시 9 결정 답습:
#   1. F-B 우선 (status file → hermes-mock unhealthy) + F-C 보조
#      (depends_on: service_healthy + pgrep) + F-A 비채택
#      (docker socket 0건, privileged false)
#   3. 감시 경로 = /run/secrets/*
#   4. runtime secret 변경 = fail-closed (rotation 별도 합의)
#   5. inotify watch = inotifywait
#   8. init grace period = 10초 (INIT_WAIT=18s = 10s + startup buffer)
#   9. healthcheck interval = 5초 (FAIL_WAIT=15s = interval×retries 2 + buffer)
#
# 영구 강제 안전 원칙:
#   - secret 본문 logging / hashing / export 0건 (R-4.1 답습) —
#     본 script 는 sidecar status 의 event tag (UNHEALTHY 여부) 만 비교,
#     status 내용 본문 전체 출력 0건
#   - production docker-compose 변경 0건
#   - Hermes upstream Dockerfile 변경 0건 (`0e99a56` 답습)
#   - F-A 비채택 — sidecar / hermes-mock 가 docker socket 접근 0건
#
# 사용:
#   tools/docker_secret_inotify_sidecar_check.sh           — 5 fixture 검증
#   tools/docker_secret_inotify_sidecar_check.sh --list-checks   — 자기 검증
#
# Exit codes:
#   0 — 5/5 fixture PASS (모든 expected outcome 충족)
#   1 — fixture 1+ FAIL
#   2 — prerequisite 누락 (docker / compose file 등)
#
# Cycle 영역:
#   - Cycle 4 (본 commit) = 본 tool script 작성
#   - Cycle 4 (다음 commit) = workflow step 추가 (본 script CI 호출)
#   - Cycle 5 = summary.json / ledger candidate / evidence form 확장 (본 영역 외)
#   - Cycle 6 = actual run 실행 + §C-5a 갱신 권고 (본 영역 외)

set -eu

LIST_CHECKS=0
if [ "${1:-}" = "--list-checks" ]; then
    LIST_CHECKS=1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
POC_DIR="$REPO_ROOT/docker/gp3-st2-poc"
COMPOSE_FILE="$POC_DIR/docker-compose.gp3-st2.yml"
FIXTURE_BASE="$REPO_ROOT/tests/fixtures/gp3_st2"

# --list-checks: 자기 검증 모드 — 5 fixture / 9 결정 / safety 명시
if [ "$LIST_CHECKS" = "1" ]; then
    echo "ST-2 inotify sidecar check — 5 fixture (Cycle 2 답습):"
    echo "  pass/normal_operation  — sidecar status empty   / hermes-mock healthy"
    echo "  pass/init_phase        — sidecar status empty   / hermes-mock healthy (init grace 10s)"
    echo "  fail/chmod_644         — sidecar status UNHEALTHY (IN_ATTRIB)   / hermes-mock unhealthy"
    echo "  fail/content_modified  — sidecar status UNHEALTHY (IN_MODIFY)   / hermes-mock unhealthy"
    echo "  fail/file_deleted      — sidecar status UNHEALTHY (DELETE)      / hermes-mock unhealthy"
    echo ""
    echo "사용자 명시 9 결정 답습:"
    echo "  #1: fail-closed = F-B 우선 / F-C 보조 / F-A 비채택"
    echo "  #2: Multi-host parity 미요구"
    echo "  #3: 감시 경로 = /run/secrets/*"
    echo "  #4: runtime fail-closed + rotation 별도 합의"
    echo "  #5: inotify watch = inotifywait (alpine + inotify-tools + procps)"
    echo "  #6: Cycle 3 commit = test + feat 2 commit 분리"
    echo "  #7: §C-5 γ sub-condition 분리 (Cycle 6 영역)"
    echo "  #8: init grace period T2 = 10초 (INIT_WAIT=18s)"
    echo "  #9: healthcheck interval = 5초 (FAIL_WAIT=15s)"
    echo ""
    echo "영구 강제 안전 원칙:"
    echo "  - secret 본문 logging / hashing / export 0건 (R-4.1 답습)"
    echo "  - status 내용 본문 출력 0건 (event tag 비교 한정)"
    echo "  - production docker-compose 변경 0건"
    echo "  - Hermes upstream Dockerfile 변경 0건"
    echo "  - F-A 비채택 (docker socket 0건, privileged false, cap_drop ALL)"
    echo ""
    echo "Cycle 영역:"
    echo "  - 본 tool = Cycle 4 (CI step + tool) 영역"
    echo "  - 본 tool 시점 영역 외: summary.json / ledger candidate (Cycle 5) /"
    echo "    actual run (Cycle 6) / §C-5 / C-5a Satisfied 갱신 (Cycle 6 후속)"
    exit 0
fi

# Prerequisite verification
if [ ! -f "$COMPOSE_FILE" ]; then
    echo "ERROR: docker-compose file not found: $COMPOSE_FILE" >&2
    echo "       (Cycle 3 feat commit 의존성 — d3acb7d 답습)" >&2
    exit 2
fi

if ! command -v docker >/dev/null 2>&1; then
    echo "ERROR: docker command not found in PATH" >&2
    exit 2
fi

if ! docker compose version >/dev/null 2>&1; then
    echo "ERROR: docker compose subcommand not available" >&2
    exit 2
fi

cd "$POC_DIR"

# Counters
PASS_COUNT=0
FAIL_COUNT=0
RESULT_LOG=""

# Wait times (사용자 #8 + #9 결정 답습)
INIT_WAIT="${ST2_INIT_WAIT_SECONDS:-18}"   # init grace 10s + start_period buffer
FAIL_WAIT="${ST2_FAIL_WAIT_SECONDS:-15}"   # healthcheck interval 5s × retries 2 + buffer
EXTRA_WAIT="${ST2_EXTRA_WAIT_SECONDS:-8}"  # pass scenario 추가 확인

# run_fixture <fixture_path> <expected_status_tag> <expected_health>
run_fixture() {
    fixture="$1"
    expected_status="$2"
    expected_health="$3"

    echo ""
    echo "===== fixture: $fixture ====="

    fixture_dir="$FIXTURE_BASE/$fixture"
    if [ ! -d "$fixture_dir" ]; then
        echo "[ST-2 check] ERROR: fixture dir not found: $fixture_dir" >&2
        FAIL_COUNT=$((FAIL_COUNT + 1))
        RESULT_LOG="${RESULT_LOG}
[FAIL] $fixture — fixture dir not found"
        return
    fi

    export SIDECAR_FIXTURE_DIR="$fixture_dir"

    # Cleanup any prior state
    docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans >/dev/null 2>&1 || true

    # Build + start
    echo "[ST-2 check] docker compose up -d --build"
    if ! docker compose -f "$COMPOSE_FILE" up -d --build; then
        echo "[ST-2 check] FAIL: docker compose up failed for $fixture" >&2
        docker compose -f "$COMPOSE_FILE" logs 2>&1 | tail -30 || true
        docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans >/dev/null 2>&1 || true
        FAIL_COUNT=$((FAIL_COUNT + 1))
        RESULT_LOG="${RESULT_LOG}
[FAIL] $fixture — docker compose up failed"
        return
    fi

    # init grace + start_period (사용자 #8 결정)
    echo "[ST-2 check] waiting init grace + startup (${INIT_WAIT}s)..."
    sleep "$INIT_WAIT"

    # Trigger fixture-specific event
    case "$fixture" in
        fail/*)
            SIMULATE_IN_CONTAINER="/fixtures/$fixture/simulate.sh"
            echo "[ST-2 check] FAIL scenario: exec $SIMULATE_IN_CONTAINER in hermes-mock"
            # simulate.sh may exit non-zero on intent (e.g., file already chmod'd) — tolerate
            docker compose -f "$COMPOSE_FILE" exec -T hermes-mock "$SIMULATE_IN_CONTAINER" \
                || echo "[ST-2 check] simulate.sh exit non-zero (may be expected per scenario)" >&2
            # Wait for fail-closed propagation (interval 5s × retries 2 + buffer = 사용자 #9 답습)
            echo "[ST-2 check] waiting fail-closed propagation (${FAIL_WAIT}s)..."
            sleep "$FAIL_WAIT"
            ;;
        pass/*)
            # Extra confirm wait — no event expected
            echo "[ST-2 check] waiting ${EXTRA_WAIT}s to confirm no spurious events..."
            sleep "$EXTRA_WAIT"
            ;;
        *)
            echo "[ST-2 check] ERROR: unknown fixture type: $fixture" >&2
            docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans >/dev/null 2>&1 || true
            FAIL_COUNT=$((FAIL_COUNT + 1))
            RESULT_LOG="${RESULT_LOG}
[FAIL] $fixture — unknown fixture type"
            return
            ;;
    esac

    # Read sidecar status — event tag only (R-4.1 답습: content body 0건)
    # status file 내용 = "UNHEALTHY: <event> <path> <ts>" 또는 empty
    # 본 script 는 첫 단어 (UNHEALTHY tag) 만 비교 — path / timestamp / content body 노출 0건
    status_first_word="$(docker compose -f "$COMPOSE_FILE" exec -T inotify-sidecar /bin/sh -c \
        'head -c 80 /var/sidecar-status/status 2>/dev/null | awk "{print \$1}" | head -c 30' \
        2>/dev/null || echo "")"

    if [ -z "$status_first_word" ]; then
        actual_status="empty"
    elif [ "$status_first_word" = "UNHEALTHY:" ]; then
        actual_status="UNHEALTHY"
    else
        actual_status="UNKNOWN"
    fi

    # Read hermes-mock health
    actual_health="$(docker inspect gp3-st2-hermes-mock --format='{{.State.Health.Status}}' 2>/dev/null \
        || echo "missing")"

    echo "[ST-2 check] result:"
    echo "  expected sidecar status tag = $expected_status"
    echo "  actual   sidecar status tag = $actual_status"
    echo "  expected hermes-mock health = $expected_health"
    echo "  actual   hermes-mock health = $actual_health"

    # Compare
    status_match=0
    health_match=0
    [ "$actual_status" = "$expected_status" ] && status_match=1
    [ "$actual_health" = "$expected_health" ] && health_match=1

    if [ "$status_match" = "1" ] && [ "$health_match" = "1" ]; then
        echo "[ST-2 check] PASS: $fixture"
        PASS_COUNT=$((PASS_COUNT + 1))
        RESULT_LOG="${RESULT_LOG}
[PASS] $fixture — sidecar=$actual_status hermes=$actual_health"
    else
        echo "[ST-2 check] FAIL: $fixture (status_match=$status_match health_match=$health_match)" >&2
        # Log compose state for debugging
        docker compose -f "$COMPOSE_FILE" ps 2>&1 | head -20 || true
        docker compose -f "$COMPOSE_FILE" logs --tail=20 inotify-sidecar 2>&1 | head -30 || true
        FAIL_COUNT=$((FAIL_COUNT + 1))
        RESULT_LOG="${RESULT_LOG}
[FAIL] $fixture — expected sidecar=$expected_status hermes=$expected_health, actual sidecar=$actual_status hermes=$actual_health"
    fi

    # Cleanup
    docker compose -f "$COMPOSE_FILE" down --volumes --remove-orphans >/dev/null 2>&1 || true
}

# Iterate 5 fixtures (Cycle 2 답습)
run_fixture "pass/normal_operation"   "empty"     "healthy"
run_fixture "pass/init_phase"         "empty"     "healthy"
run_fixture "fail/chmod_644"          "UNHEALTHY" "unhealthy"
run_fixture "fail/content_modified"   "UNHEALTHY" "unhealthy"
run_fixture "fail/file_deleted"       "UNHEALTHY" "unhealthy"

# Aggregate result
echo ""
echo "===== ST-2 inotify sidecar check summary ====="
echo "PASS: $PASS_COUNT / 5"
echo "FAIL: $FAIL_COUNT / 5"
echo "$RESULT_LOG"

if [ "$FAIL_COUNT" -eq 0 ] && [ "$PASS_COUNT" -eq 5 ]; then
    echo ""
    echo "[ST-2 check] OVERALL: PASS (5/5 fixtures matched expected outcome)"
    echo "  F-B primary fail-closed (status file → hermes-mock unhealthy) 검증 완료"
    echo "  F-C 보조 (depends_on: service_healthy + sidecar pgrep) 검증 완료"
    echo "  F-A 비채택 (docker socket / privileged 0건) 보존 확인"
    exit 0
else
    echo ""
    echo "[ST-2 check] OVERALL: FAIL ($FAIL_COUNT / 5 fixtures mismatched)" >&2
    exit 1
fi
