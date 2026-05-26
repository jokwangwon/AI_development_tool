#!/usr/bin/env python3
"""Jarvis MVP-0 E2E 데모 — 실제 claude 워커를 Landlock 격리 안에서 실행.

오케스트레이터 전 파이프라인의 *실동작* 입증(지금까지 모든 테스트는 mock runner):
  결정적 배관 → 격리 워커(headless claude) → 결과 파싱(exit code·cost) →
  무비판 수용 금지 검토 → "반영 전" 사람 게이트(default-deny) → 보고.

증명 ①~⑤이 실제 외부 워커로 한 번에 맞물리는지 확인한다. 격리 backend =
트랙 B `LandlockIsolation`(검증된 ll_sandbox). 워커는 workdir 안에서만 쓰기
가능하고 그 외 fs 쓰기는 커널이 차단(증명 ⑤, 통합 테스트로 별도 입증).

⚠️ 실제 토큰 소비. claude CLI + 인증 + 빌드된 sandboxer 필요:
    make -C src/jarvis/sandbox
사용:
    python examples/jarvis_e2e_demo.py            # 대화형 승인
    python examples/jarvis_e2e_demo.py --yes      # 비대화형(자동 승인)
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.isolation import LandlockIsolation
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import CliWorker

# claude 워커가 격리 안에서 동작하는 데 필요한 RO 경로(E2E 실측 — claude --version
# 은 시스템 경로만으로 충분하나 `-p` 실행은 홈 의존[설정·캐시·런타임]이 커서 홈 통째
# RO 가 필요했다). 쓰기는 workdir(RW) 만 — 그 외 전부 RO/미노출이라 커널이 차단.
# 워커별 RO 정밀화(민감 파일 차단)는 후속 과제(net egress 정책 B1 과 함께).
CLAUDE_RO_PATHS = [
    "/usr", "/lib", "/bin", "/sbin", "/etc", "/proc", "/dev", "/run",
    os.path.expanduser("~"),
]


def _claude_runner(cmd: list[str], workdir: str) -> "tuple[int, str, str]":
    """claude headless 실행 runner — cwd=workdir(작업 위치) + TMPDIR=workdir.

    claude 는 cwd 에 산출물을 쓰고 임시파일을 TMPDIR 에 쓴다. 둘 다 workdir(RW)로
    두어야 격리 안에서 정상 동작(그 외 경로는 RO/미노출).
    """
    env = {**os.environ, "TMPDIR": workdir}
    proc = subprocess.run(cmd, cwd=workdir, env=env, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


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

    isolation = LandlockIsolation(ro_paths=CLAUDE_RO_PATHS)
    worker = CliWorker(
        alias="claude",
        argv=["claude", "--output-format", "json", "--dangerously-skip-permissions", "-p"],
        isolation=isolation,
        runner=_claude_runner,
    )
    registry = WorkerRegistry()
    registry.register(worker)

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

    print("=== Jarvis MVP-0 E2E (실제 claude 워커 + Landlock 격리) ===")
    print(f"격리 backend : {isolation.name} (RO {len(CLAUDE_RO_PATHS)}개, 쓰기=workdir만)")
    print(f"워커         : {worker.alias} (headless subprocess)")
    print(f"작업         : {args.prompt}")
    print("dispatch …")

    report = orch.dispatch(prompt=args.prompt, task_id="e2e-demo")

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
