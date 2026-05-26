# GP-3 ST-2 hermes-mock Dockerfile (Cycle 3 test/scaffold commit)
#
# 본 container = ST-2 PoC mock target — 실 Hermes 영향 0건 (Hermes upstream
# Dockerfile 변경 0건 답습).
#
# 사용자 명시 9 결정 답습:
#   - 사용자 #1: F-A 비채택 → docker socket 미마운트 (volumes 항목에 없음)
#   - 사용자 #9: healthcheck interval 5초 → docker-compose level
#
# 영구 강제 안전 원칙:
#   - cap_drop ALL (docker-compose level)
#   - status content logging / hashing / export 0건 (healthcheck.sh 답습)

FROM alpine:3.20

# healthcheck script 설치
COPY healthcheck.sh /usr/local/bin/healthcheck.sh
RUN chmod +x /usr/local/bin/healthcheck.sh

# 본 container 는 sleep infinity — 정지 시뮬레이션은 docker-compose healthcheck
# unhealthy 처리 통해 발생 (F-B 우선 답습)
ENTRYPOINT ["sleep", "infinity"]
