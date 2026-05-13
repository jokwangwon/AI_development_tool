#!/bin/sh
# fail/chmod_644 simulate — runtime chmod 644 시뮬레이션
#
# 본 스크립트는 Cycle 4 CI step 또는 사용자 수동 호출로 실행됨.
# 본 스크립트는 sidecar PoC container 내부 /run/secrets/* 의 권한을 644 로 변경하여
# inotify IN_ATTRIB event 발화를 유도함.
#
# 사용자 명시 답습:
#   - F-A (docker socket) 비채택 — 본 스크립트는 docker socket 접근 0건
#   - production 영역 영향 0건 (sidecar PoC container 내부 한정)
#   - 실 secret 0건 (fake canary 의무 답습)
#
# 사용:
#   docker exec <hermes-mock-or-sidecar> /fixtures/fail/chmod_644/simulate.sh
#
# 기대 결과:
#   - sidecar inotifywait 가 IN_ATTRIB event 발화
#   - sidecar status file = "UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <ts>"
#   - hermes-mock healthcheck (5초 interval) 가 status read → unhealthy

set -e

TARGET="${1:-/run/secrets/mock_api_key}"

if [ ! -f "$TARGET" ]; then
    echo "ERROR: target file not found: $TARGET" >&2
    exit 2
fi

echo "[simulate] before: $(stat -c '%a %n' "$TARGET")"
chmod 644 "$TARGET"
echo "[simulate] after:  $(stat -c '%a %n' "$TARGET")"
echo "[simulate] expected sidecar IN_ATTRIB event within 5 seconds"
