#!/bin/bash
# pre_commit_install_audit.sh — PC-1-T3 bypass detection (3 탐지 경로 통합 verify)
#
# 답습 출처:
#   - docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md §4.5 (D-4 = tools/pre_commit_install_audit.sh)
#   - docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md (Reviewer-only APPROVE)
#   - 24번째 entry 합의 보고서 §6 R-6 BLOCKING (탐지 경로 (i)(ii)(iii) 의무)
#
# 본 스크립트의 본질 (R-6 흡수):
#   - 탐지 경로 (i): hook marker grep (.git/hooks/pre-commit 내 pre-commit framework marker 검출)
#   - 탐지 경로 (ii): pre-commit run --all-files CI 비교 자격 (manual + CI 통합 = D-6 별도 sub-cycle)
#   - 탐지 경로 (iii): setup audit log 존재 여부 (.git/pre-commit-audit/install.log)
#
# Exit code:
#   0 = 3 탐지 경로 모두 PASS (PC-1-T3 발효 자격 정상)
#   1 = 1 이상 탐지 경로 FAIL (PC-1-T3 bypass 의심 → Rollback Trigger R-MVP1-1.5-PC1-1 발화 자격)

set +e  # 검증 결과 누적 의무, exit 1 즉시 종료 0

echo "=== PC-1-T3 mandatory enforcement audit ==="
echo ""

FAIL_COUNT=0

# 탐지 경로 (i): hook marker grep
echo "[i/iii] hook marker grep 검증 중..."
if [ -f .git/hooks/pre-commit ]; then
    if grep -q "pre-commit" .git/hooks/pre-commit 2>/dev/null; then
        echo "  [PASS] .git/hooks/pre-commit 에 pre-commit framework marker 검출"
    else
        echo "  [FAIL] .git/hooks/pre-commit 존재하나 framework marker 부재"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
else
    echo "  [FAIL] .git/hooks/pre-commit 부재 → pre-commit install 미실행 의심"
    FAIL_COUNT=$((FAIL_COUNT + 1))
fi
echo ""

# 탐지 경로 (ii): pre-commit run --all-files 실행 자격 (manual + CI 통합 = D-6 별도 sub-cycle)
echo "[ii/iii] pre-commit run --all-files 실행 자격 검증 중..."
if command -v pre-commit > /dev/null 2>&1; then
    echo "  [PASS] pre-commit framework 명령 가용 (PATH 확인)"
    echo "  [INFO] manual: pre-commit run --all-files 직접 실행 후 CI 결과와 비교 의무"
    echo "  [INFO] CI 자동 비교 통합 = D-6 별도 sub-cycle 영역"
else
    echo "  [FAIL] pre-commit 명령 PATH 부재 → pip install 미실행 의심"
    FAIL_COUNT=$((FAIL_COUNT + 1))
fi
echo ""

# 탐지 경로 (iii): setup audit log 존재 여부
echo "[iii/iii] setup audit log 검증 중..."
AUDIT_LOG=".git/pre-commit-audit/install.log"
if [ -f "$AUDIT_LOG" ]; then
    echo "  [PASS] $AUDIT_LOG 존재 (bin/setup.sh 실행 흔적)"
    echo "  [INFO] 최근 install 시점:"
    head -n 1 "$AUDIT_LOG" | sed 's/^/    /'
else
    echo "  [FAIL] $AUDIT_LOG 부재 → bin/setup.sh 미실행 의심"
    FAIL_COUNT=$((FAIL_COUNT + 1))
fi
echo ""

# 결과 집계
echo "=== audit 결과 ==="
if [ $FAIL_COUNT -eq 0 ]; then
    echo "[OK] 3 탐지 경로 모두 PASS — PC-1-T3 발효 자격 정상"
    exit 0
else
    echo "[FAIL] $FAIL_COUNT/3 탐지 경로 FAIL — PC-1-T3 bypass 의심"
    echo ""
    echo "조치:"
    echo "  - bash bin/setup.sh 실행 (Layer 3 + Layer 2 + audit log 통합 활성화)"
    echo "  - 또는 단축 합의 + 사용자 명시 재검토 (R-MVP1-1.5-PC1-1 발화 자격)"
    exit 1
fi
