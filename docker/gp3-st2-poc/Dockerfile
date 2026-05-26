# GP-3 ST-2 inotify sidecar Dockerfile (Cycle 3 feat commit)
#
# 사용자 명시 9 결정 답습:
#   - 사용자 #1: F-A 비채택 → docker socket 미마운트, privileged 미사용
#                (volumes / cap_add 항목 모두 0건)
#   - 사용자 #3: 감시 경로 = /run/secrets/* (entrypoint env var SIDECAR_WATCH_DIR)
#   - 사용자 #5: inotify watch = inotifywait (alpine + inotify-tools)
#   - 사용자 #8: init grace period = 10초 (watch-secrets.sh 답습)
#
# 영구 강제 안전 원칙:
#   - non-root user (uid 자동 할당, ~1000)
#   - cap_drop ALL (docker-compose level)
#   - secret 본문 logging / hashing / export 0건 (watch-secrets.sh 답습)
#   - production Hermes 영향 0건 (PoC 격리)

FROM alpine:3.20

# 패키지 설치
# - inotify-tools: 사용자 #5 결정 답습 (inotifywait)
# - procps: F-C 보조 답습 (pgrep inotifywait — sidecar healthcheck)
RUN apk add --no-cache inotify-tools procps

# Non-root user 생성 (uid 자동 할당)
RUN addgroup -S sidecar && \
    adduser -S -G sidecar -h /home/sidecar sidecar

# Status file 디렉토리 (named volume mount 시점 ownership 보존)
RUN mkdir -p /var/sidecar-status && \
    chown sidecar:sidecar /var/sidecar-status && \
    chmod 755 /var/sidecar-status

# Watch script 설치
COPY watch-secrets.sh /usr/local/bin/watch-secrets.sh
RUN chmod +x /usr/local/bin/watch-secrets.sh

USER sidecar

ENTRYPOINT ["/usr/local/bin/watch-secrets.sh"]
