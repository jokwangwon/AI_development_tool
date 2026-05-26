#!/bin/sh
# GP-3 ST-2 inotify sidecar watch script (Cycle 3 feat commit)
#
# 사용자 명시 9 결정 답습:
#   1. fail-closed = F-B 우선 (status file write → hermes-mock unhealthy)
#                  + F-A 비채택 (docker socket 접근 0건)
#   3. 감시 경로 = /run/secrets/* (SIDECAR_WATCH_DIR env var, default /run/secrets)
#   4. runtime secret 변경 = fail-closed (모든 inotify event 대상)
#   5. inotify watch = inotifywait
#   8. init grace period = 10초 (SIDECAR_INIT_GRACE_SECONDS env var)
#
# inotify event 답습 (사용자 #5 결정 + brief §5.1 답습):
#   - attrib       = IN_ATTRIB (mtime/mode/owner 변경)
#   - modify       = IN_MODIFY (파일 내용 변경)
#   - delete       = IN_DELETE (감시 디렉토리 내부 파일 삭제)
#   - move         = IN_MOVE (감시 디렉토리 내부 파일 이동)
#   - delete_self  = IN_DELETE_SELF (감시 디렉토리 자체 삭제)
#   - move_self    = IN_MOVE_SELF (감시 디렉토리 자체 이동)
#   - IN_ACCESS 미사용 (false positive 폭증 회피 — brief §5.1 답습)
#
# Note: inotifywait 의 watched-dir 모드에서 디렉토리 내부 파일 변경은
#       delete / move (without _self) 로 발화 — fixture fail/file_deleted 의
#       `IN_DELETE_SELF` 표기는 brief 답습 표현 한정, 실제 발화 event 는 `DELETE`.
#       양쪽 모두 fail-closed 처리 (event 종류 무관 — 모든 변경 = UNHEALTHY).
#
# 영구 강제 안전 원칙:
#   - secret 본문 logging / hashing / export 0건 (R-4.1 답습)
#   - status file 에는 event metadata 한정 (event name + path + timestamp) — content 0건
#   - production / Hermes upstream 영향 0건

set -eu

STATUS_FILE="${SIDECAR_STATUS_FILE:-/var/sidecar-status/status}"
WATCH_DIR="${SIDECAR_WATCH_DIR:-/run/secrets}"
INIT_GRACE="${SIDECAR_INIT_GRACE_SECONDS:-10}"

# Verify status file directory writable
STATUS_DIR="$(dirname "$STATUS_FILE")"
if [ ! -d "$STATUS_DIR" ]; then
    echo "[sidecar] FATAL: status directory not found: $STATUS_DIR" >&2
    exit 1
fi

# Initialize status file (empty = healthy)
: > "$STATUS_FILE"

# Init grace period (사용자 #8 결정 답습)
echo "[sidecar] startup — init grace period ${INIT_GRACE}s before inotify watch begins"
sleep "$INIT_GRACE"

# Verify watch directory exists
if [ ! -d "$WATCH_DIR" ]; then
    ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "UNHEALTHY: WATCH_DIR_MISSING $WATCH_DIR $ts" > "$STATUS_FILE"
    echo "[sidecar] FATAL: watch dir not found ($WATCH_DIR) — fail-closed triggered" >&2
    # Keep container alive so hermes-mock healthcheck can read status
    exec sleep infinity
fi

echo "[sidecar] init grace complete — starting inotifywait on $WATCH_DIR"

# Monitor events (사용자 #5 답습 — inotifywait)
inotifywait -m \
    -e attrib,modify,delete,move,delete_self,move_self \
    --format '%T %e %w%f' \
    --timefmt '%Y-%m-%dT%H:%M:%SZ' \
    "$WATCH_DIR" | \
while IFS=' ' read -r ts event path; do
    # status file 에 event metadata 한정 기록 (content 0건 — R-4.1 답습)
    echo "UNHEALTHY: $event $path $ts" > "$STATUS_FILE"
    echo "[sidecar] event fired: $event $path $ts" >&2
done
