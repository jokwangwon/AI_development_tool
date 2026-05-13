#!/bin/sh
# fail/file_deleted simulate — runtime secret 파일 삭제 시뮬레이션
#
# 본 스크립트는 mock secret 파일을 rm 으로 삭제하여
# inotify IN_DELETE_SELF event 발화를 유도함.
#
# 사용자 명시 답습:
#   - F-A (docker socket) 비채택
#   - production 영역 영향 0건 (sidecar PoC container 내부 한정)
#   - 실 secret 0건 (fake canary 의무 답습)
#   - 삭제 복원 0건 (docker-compose down 으로 cleanup)
#
# 사용:
#   docker exec <hermes-mock-or-sidecar> /fixtures/fail/file_deleted/simulate.sh
#
# 기대 결과:
#   - sidecar inotifywait 가 IN_DELETE_SELF (또는 IN_MOVE_SELF) event 발화
#   - sidecar status file = "UNHEALTHY: IN_DELETE_SELF /run/secrets/mock_api_key <ts>"
#   - hermes-mock healthcheck (5초 interval) 가 status read → unhealthy

set -e

TARGET="${1:-/run/secrets/mock_api_key}"

if [ ! -f "$TARGET" ]; then
    echo "ERROR: target file not found: $TARGET" >&2
    exit 2
fi

echo "[simulate] before: $(ls -la "$TARGET")"
rm -f "$TARGET"
if [ -e "$TARGET" ]; then
    echo "ERROR: target file still exists after rm: $TARGET" >&2
    exit 3
fi
echo "[simulate] after:  file deleted"
echo "[simulate] expected sidecar IN_DELETE_SELF event within 5 seconds"
