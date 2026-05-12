#!/usr/bin/env bash
# GP-3 Stage 2 sub-step 2.3 — container restart secret 재주입 recovery check.
#
# 답습:
#   - implementation-runtime-roadmap-mvp1.md §3.4.2 container_restart_recovery
#     (컨테이너 정지 후 재시작 시 secret 재주입 정상, 100% 강제)
#   - ADR-008 §2.6.2 R2-1 (file system secret isolation)
#
# 본 script 는 gp3-st3-poc compose stack 을:
#   1) up + run + secret_sha256 캡처
#   2) down (컨테이너 정지)
#   3) up + run + secret_sha256 재캡처
#   4) 두 sha256 비교 — 동일 시 PASS (secret 재주입 정상), 불일치 시 FAIL
#
# Usage:
#   tools/docker_secret_restart_recovery.sh <compose-dir>
#
# 종료 코드:
#   0 — restart 후 secret 재주입 sha256 일치 + isolation_check=PASS
#   1 — restart 후 sha256 불일치 또는 PASS marker 누락
#   2 — 사용 오류 / docker 또는 compose 미가용 / build / up 실패

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <compose-dir>" >&2
    exit 2
fi

COMPOSE_DIR="$1"
COMPOSE_FILE="docker-compose.gp3-st3.yml"

if [ ! -d "$COMPOSE_DIR" ]; then
    echo "ERROR: compose dir not found: $COMPOSE_DIR" >&2
    exit 2
fi
if [ ! -f "$COMPOSE_DIR/$COMPOSE_FILE" ]; then
    echo "ERROR: $COMPOSE_FILE not found in $COMPOSE_DIR" >&2
    exit 2
fi
if ! command -v docker >/dev/null 2>&1; then
    echo "ERROR: docker not available" >&2
    exit 2
fi

# docker compose v2 sub-command 우선; v1 fallback
if docker compose version >/dev/null 2>&1; then
    DC="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
    DC="docker-compose"
else
    echo "ERROR: docker compose (v2) 또는 docker-compose (v1) 미가용" >&2
    exit 2
fi

cd "$COMPOSE_DIR"

cleanup() {
    $DC -f "$COMPOSE_FILE" down --remove-orphans >/dev/null 2>&1 || true
}
trap cleanup EXIT

run_once() {
    local label="$1"
    local logfile
    logfile="$(mktemp)"

    $DC -f "$COMPOSE_FILE" up --build --abort-on-container-exit --exit-code-from gp3-st3-poc >"$logfile" 2>&1 || {
        echo "ERROR: compose up [$label] failed — logs:" >&2
        cat "$logfile" >&2
        rm -f "$logfile"
        return 2
    }

    local sha
    sha="$(grep -oE 'secret_sha256=[0-9a-f]{64}' "$logfile" | head -1 | cut -d= -f2)"
    local marker
    marker="$(grep -c 'docker_secret_isolation_check=PASS' "$logfile" || true)"

    rm -f "$logfile"

    if [ -z "$sha" ]; then
        echo "ERROR: [$label] secret_sha256 not captured" >&2
        return 1
    fi
    if [ "$marker" -eq 0 ]; then
        echo "ERROR: [$label] docker_secret_isolation_check=PASS marker missing" >&2
        return 1
    fi

    echo "$sha"
    return 0
}

echo "[restart-recovery] phase 1 — initial up"
sha1="$(run_once initial)"
rc=$?
[ $rc -eq 0 ] || exit $rc

echo "[restart-recovery] phase 1 sha256=$sha1"

echo "[restart-recovery] phase 2 — down"
$DC -f "$COMPOSE_FILE" down --remove-orphans >/dev/null 2>&1

echo "[restart-recovery] phase 3 — restart up"
sha2="$(run_once restart)"
rc=$?
[ $rc -eq 0 ] || exit $rc

echo "[restart-recovery] phase 3 sha256=$sha2"

if [ "$sha1" != "$sha2" ]; then
    echo "ERROR: secret sha256 mismatch — sha1=$sha1 sha2=$sha2 (재주입 불일치)" >&2
    exit 1
fi

echo "[restart-recovery] PASS — secret 재주입 정상 (sha256 일치 + isolation_check=PASS 2회)"
exit 0
