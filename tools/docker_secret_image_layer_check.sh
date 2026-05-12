#!/usr/bin/env bash
# GP-3 Stage 2 sub-step 2.2 — docker image layer secret leak check.
#
# 답습:
#   - implementation-runtime-roadmap-mvp1.md §3.4.2 docker_secret_isolation_check
#     (secret 파일이 image layer 에 포함되지 않음 검증, 0건 leak 강제)
#   - ADR-008 §2.6.2 R2-1 (file system secret isolation)
#
# 본 script 는 주어진 Dockerfile 디렉토리를 build → docker save tar → secret
# canary string grep 으로 image layer leak 을 검출한다.
#
# Usage:
#   tools/docker_secret_image_layer_check.sh <build-context-dir> <canary-string> <expected>
#
#   <expected> = "leak" (rc=1 시 PASS — fail fixture) 또는 "clean" (rc=0 시 PASS — pass fixture)
#
# 종료 코드:
#   0 — expected 결과와 일치
#   1 — 불일치 (PASS fixture 에 leak 검출 또는 FAIL fixture 에 leak 미검출)
#   2 — 사용 오류 / docker unavailable / build 실패

set -e

usage() {
    echo "Usage: $0 <build-context-dir> <canary-string> <leak|clean>" >&2
    exit 2
}

if [ $# -ne 3 ]; then
    usage
fi

CONTEXT="$1"
CANARY="$2"
EXPECTED="$3"

case "$EXPECTED" in
    leak|clean) ;;
    *) usage ;;
esac

if [ ! -d "$CONTEXT" ]; then
    echo "ERROR: context dir not found: $CONTEXT" >&2
    exit 2
fi

if ! command -v docker >/dev/null 2>&1; then
    echo "ERROR: docker not available" >&2
    exit 2
fi

IMAGE_TAG="gp3-st3-layercheck:$(echo "$CONTEXT" | tr '/' '-' | tr -cd 'a-z0-9-')-$$"
TAR_PATH="$(mktemp --suffix=.tar)"
cleanup() {
    rm -f "$TAR_PATH"
    docker image rm -f "$IMAGE_TAG" >/dev/null 2>&1 || true
}
trap cleanup EXIT

echo "[image-layer-check] context=$CONTEXT canary=*** expected=$EXPECTED"

if ! docker build --no-cache --quiet -t "$IMAGE_TAG" "$CONTEXT" >/dev/null; then
    echo "ERROR: docker build failed for $CONTEXT" >&2
    exit 2
fi

if ! docker save -o "$TAR_PATH" "$IMAGE_TAG"; then
    echo "ERROR: docker save failed" >&2
    exit 2
fi

# grep canary in tar — 0 = found, 1 = not found
set +e
grep -q -a -F "$CANARY" "$TAR_PATH"
grep_rc=$?
set -e

case "$EXPECTED:$grep_rc" in
    leak:0)
        echo "[image-layer-check] PASS — canary FOUND in image layers (fail fixture demonstrates leak)"
        exit 0
        ;;
    leak:1)
        echo "ERROR: canary NOT found — fail fixture failed to demonstrate leak" >&2
        exit 1
        ;;
    clean:0)
        echo "ERROR: canary FOUND in image layers — pass fixture LEAKED secret" >&2
        exit 1
        ;;
    clean:1)
        echo "[image-layer-check] PASS — canary not found in image layers (pass fixture clean)"
        exit 0
        ;;
    *)
        echo "ERROR: unexpected grep rc=$grep_rc" >&2
        exit 2
        ;;
esac
