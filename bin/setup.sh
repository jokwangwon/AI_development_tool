#!/bin/bash
# dev onboarding 통합 setup 스크립트
#
# 답습 출처:
#   - docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md §4.3 (D-2 = bin/setup.sh)
#   - docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md (Reviewer-only APPROVE)
#   - 24번째 entry brief v1.1 §2.3 (PC-1-T3 mandatory enforcement)
#
# 본 스크립트의 본질 (PC-1-T3):
#   - Layer 3 (.githooks/) + Layer 2 (.pre-commit-config.yaml framework) 병렬 활성화 (D-5 (α))
#   - pre-commit framework 의무 install (T3 mandatory enforcement)
#   - .git/pre-commit-audit/install.log 기록 (D-3 답습, R-6 (iii) 흡수)
#   - 외부 의존성 0 (bash + git + pip 만, Provider Liquidity 답습)
#
# 본 스크립트가 *하지 않는* 것:
#   - branch protection rule 변경 0건 (AR-3 별도 sub-cycle 영역)
#   - .pre-commit-config.yaml 본문 변경 0건
#   - .githooks/pre-commit 본문 변경 0건
#   - CI workflow 변경 0건 (D-6 별도 sub-cycle)

set -e

echo "=== AI Development Tool — dev 환경 통합 setup ==="
echo ""

# Step 1: Layer 3 (.githooks/) 활성화
echo "[1/4] Layer 3 (.githooks/) 활성화 중..."
bash .githooks/setup.sh
echo ""

# Step 2: dev 의존성 설치 (pre-commit framework 포함)
echo "[2/4] dev 의존성 설치 중 (requirements-dev.txt)..."
pip install -r requirements-dev.txt
echo ""

# Step 3: Layer 2 pre-commit framework 의무화 (PC-1-T3)
echo "[3/4] Layer 2 pre-commit framework 활성화 중 (PC-1-T3 mandatory enforcement)..."
pre-commit install
echo "[OK] pre-commit framework 활성화됨 (.git/hooks/pre-commit 생성)"
echo ""

# Step 4: install audit log 기록 (R-6 (iii) 답습)
echo "[4/4] install audit log 기록 중..."
mkdir -p .git/pre-commit-audit
date -Iseconds > .git/pre-commit-audit/install.log
git rev-parse HEAD 2>/dev/null >> .git/pre-commit-audit/install.log || echo "(initial commit 전)" >> .git/pre-commit-audit/install.log
echo "[OK] audit log 기록됨 → .git/pre-commit-audit/install.log"
echo ""

echo "=== setup 완료 ==="
echo ""
echo "다음 단계:"
echo "  - tools/pre_commit_install_audit.sh 실행 (bypass detection verify)"
echo "  - pre-commit run --all-files (local 격리 검증)"
echo "  - CONTRIBUTING.md 참조 (dev workflow + PC-1-T3 의무화 명문)"
