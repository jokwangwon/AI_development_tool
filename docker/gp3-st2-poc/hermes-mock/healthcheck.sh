#!/bin/sh
# hermes-mock healthcheck — F-B primary fail-closed signal reader (Cycle 3 test/scaffold)
#
# sidecar (F-B 우선 답습) 가 status file 에 UNHEALTHY 기록 시 본 healthcheck 가 exit 1.
# docker-compose healthcheck retries 2 초과 시 hermes-mock = unhealthy 처리.
#
# 사용자 #1 결정 답습:
#   - F-A 비채택: 본 script 는 docker socket / Hermes upstream 접근 0건
#   - status file 읽기 한정 — docker-compose level 영역
#
# 사용자 #9 결정 답습:
#   - healthcheck interval 5초 (docker-compose 정의)
#
# 영구 강제 안전 원칙:
#   - status 본문 logging / hashing / export 0건 (R-4.1 답습)
#   - 본 script 가 secret 본문 자체 접근 0건 (status file 만 read)
#   - production / Hermes upstream 영향 0건

set -e

STATUS_FILE="${SIDECAR_STATUS_FILE:-/var/sidecar-status/status}"

# File doesn't exist yet (sidecar init grace period 진행 중) → healthy
if [ ! -f "$STATUS_FILE" ]; then
    exit 0
fi

# Empty file → healthy (정상 운영)
if [ ! -s "$STATUS_FILE" ]; then
    exit 0
fi

# Non-empty → sidecar 가 fail-closed 발화
# stderr 로 fail-closed 발화 사실만 표시 — status content 자체 출력 0건 (R-4.1 답습)
echo "[hermes-mock-healthcheck] FAIL: sidecar status file non-empty (fail-closed triggered)" >&2
exit 1
