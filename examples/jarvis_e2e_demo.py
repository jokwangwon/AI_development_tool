#!/usr/bin/env python3
"""Jarvis MVP-0 E2E 데모 — 실제 claude 워커를 가짜 홈 격리(레벨 2) 안에서 실행.

오케스트레이터 전 파이프라인의 *실동작* 입증(테스트는 mock runner):
  결정적 배관 → 격리 워커(headless claude) → 결과 파싱(exit code·cost) →
  무비판 수용 금지 검토 → "반영 전" 사람 게이트(default-deny) → 보고.

증명 ①~⑤이 실제 외부 워커로 한 번에 맞물리는지 확인한다. 워커 배선·격리는
`worker_setup.build_worker_registry` *단일 소스*를 쓴다(레벨 2 가짜 홈 격리,
ADR-014): 진짜 홈 미노출 + RO 최소화(CLAUDE_RO_PATHS) + env allowlist(토큰·SSH
차단) + 가짜 홈 HOME 재배치 + LandlockIsolation(rw_root=가짜홈). 과거 이 데모가
들고 있던 광범위 홈 RO + env 전체 상속(레벨 2 *이전* 방식)은 제거됐다(중복 해소).

⚠️ 실제 토큰 소비. claude CLI + 인증(`~/.claude/.credentials.json`) + 빌드된
sandboxer 필요:
    make -C src/jarvis/sandbox
사용:
    python examples/jarvis_e2e_demo.py            # 대화형 승인
    python examples/jarvis_e2e_demo.py --yes      # 비대화형(자동 승인)
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.orchestrator import Orchestrator
from src.jarvis.review import ReviewGuard
from src.jarvis.worker_setup import CLAUDE_RO_PATHS, build_worker_registry


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis MVP-0 E2E 데모")
    ap.add_argument("--yes", action="store_true", help="반영 자동 승인(비대화형)")
    ap.add_argument(
        "--prompt",
        default="Create a file named hello.txt in the current directory with "
        "exactly the content: JARVIS_E2E_OK . Then stop.",
        help="워커에게 줄 작업",
    )
    args = ap.parse_args()

    # 실 워커 배선 — code=claude+가짜 홈 격리(레벨 2) / file=ollama. CLAUDE_RO_PATHS·
    # runner·가짜 홈 provision·env allowlist 는 worker_setup 단일 소스(중복 제거).
    # 가짜 홈 첫 호출 시 provision(fail-closed: credential 무효 시 raise).
    registry, _kind_table = build_worker_registry()

    def approver(req: ApprovalRequest) -> bool:
        print("\n── 사람 게이트 (반영 전, default-deny) ──")
        print(f"  worker : {req.worker_alias}")
        print(f"  flags  : {req.flags or '(없음)'}")
        print(f"  미리보기: {req.output_preview}")
        if args.yes:
            print("  --yes → 자동 승인")
            return True
        return input("  반영을 승인합니까? [y/N] ").strip().lower() == "y"

    orch = Orchestrator(registry, ReviewGuard(), ApprovalGate(approver))

    print("=== Jarvis MVP-0 E2E (실제 claude 워커 + 가짜 홈 격리, 레벨 2) ===")
    print(f"격리 backend : LandlockIsolation 가짜 홈(레벨 2, ADR-014; "
          f"RO {len(CLAUDE_RO_PATHS)}개 최소, 쓰기=가짜홈만, env allowlist)")
    print("워커         : claude (headless subprocess, HOME=가짜 홈)")
    print(f"작업         : {args.prompt}")
    print("dispatch …")

    report = orch.dispatch(prompt=args.prompt, task_id="e2e-demo", worker_alias="claude")

    print("\n=== OutcomeReport ===")
    print(f"  status  : {report.status.value}")
    print(f"  worker  : {report.worker_alias}")
    print(f"  exit    : {report.result.exit_code}")
    cost = report.result.cost_usd
    print(f"  cost    : ${cost:.4f}" if cost is not None else "  cost    : n/a")
    print(f"  verdict : ok={report.verdict.ok} flags={report.verdict.flags}")
    print(f"  applied : {report.applied}")
    print(f"  output  : {report.result.output}")
    return 0 if report.result.succeeded else 1


if __name__ == "__main__":
    raise SystemExit(main())
