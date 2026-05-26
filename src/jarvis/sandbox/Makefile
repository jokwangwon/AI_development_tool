# Jarvis MVP-0 트랙 B — ll_sandbox 빌드
#
# 답습: docs/phase0/jarvis-safety-layer-poc-findings.md §6 (V-2: gcc 13.3.0, Landlock ABI 7)
#   - 검증된 Landlock fs sandboxer. 산출 바이너리는 gitignore(머신 의존, 재빌드 가능).
#   - LandlockIsolation 이 src/jarvis/sandbox/ll_sandbox 를 기본 탐색.
#
# 사용: make -C src/jarvis/sandbox    (빌드)
#       make -C src/jarvis/sandbox clean
CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra

ll_sandbox: ll_sandbox.c
	$(CC) $(CFLAGS) -o $@ $<

.PHONY: clean
clean:
	rm -f ll_sandbox
