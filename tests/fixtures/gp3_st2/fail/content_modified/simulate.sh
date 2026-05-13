#!/bin/sh
# fail/content_modified simulate — runtime secret 본문 변경 시뮬레이션
#
# 본 스크립트는 mock secret 파일의 본문에 변조 문자열을 append 하여
# inotify IN_MODIFY event 발화를 유도함.
#
# 사용자 명시 답습:
#   - F-A (docker socket) 비채택
#   - production 영역 영향 0건 (sidecar PoC container 내부 한정)
#   - 실 secret 0건 (fake canary 의무 답습)
#   - sidecar 가 변조된 본문 logging / hashing / export 0건 (영구 금지)
#
# 사용:
#   docker exec <hermes-mock-or-sidecar> /fixtures/fail/content_modified/simulate.sh
#
# 기대 결과:
#   - sidecar inotifywait 가 IN_MODIFY event 발화
#   - sidecar status file = "UNHEALTHY: IN_MODIFY /run/secrets/mock_api_key <ts>"
#   - hermes-mock healthcheck (5초 interval) 가 status read → unhealthy

set -e

TARGET="${1:-/run/secrets/mock_api_key}"

if [ ! -f "$TARGET" ]; then
    echo "ERROR: target file not found: $TARGET" >&2
    exit 2
fi

echo "[simulate] before size: $(wc -c < "$TARGET")"
# append (overwrite 0건 — 변조 흔적 보존)
echo " # tampered_by_simulate_$(date -u +%Y%m%dT%H%M%SZ)" >> "$TARGET"
echo "[simulate] after size:  $(wc -c < "$TARGET")"
echo "[simulate] expected sidecar IN_MODIFY event within 5 seconds"
