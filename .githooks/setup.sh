#!/bin/bash
# Git hooks 설정 스크립트
# 프로젝트 클론 후 한 번 실행: bash .githooks/setup.sh

set -e

echo "=== AI Development Tool — Git Hooks 설정 ==="

# Git hooks 경로를 프로젝트 내 .githooks로 설정
git config core.hooksPath .githooks

echo "[OK] Git hooks 경로 설정 완료: .githooks/"
echo "[OK] pre-commit hook 활성화됨"
echo ""
echo "하네스 엔지니어링 피드백 루프:"
echo "  Layer 0: CLAUDE.md (가이드)"
echo "  Layer 1: PostToolUse Hook (센서)"
echo "  Layer 2: PreCommit Hook (센서)"
echo "  Layer 3: git pre-commit hook (센서) ← 현재 설정"
echo "  Layer 4: CI Pipeline (센서)"
echo "  Layer 5: 3+1 에이전트 합의 (센서)"
echo "  Layer 6: Human Review (센서)"
