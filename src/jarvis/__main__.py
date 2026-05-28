"""jarvis CLI entrypoint — `python -m src.jarvis "작업"`.

[[project_jarvis_controlled_child_then_friday]]: jarvis = 나와 함께하는 *통제된 자식*.
기존 orchestrator 파이프라인 배선만 (새 아키텍처 0). 통제 = ApprovalGate default-deny
+ R10 분리 표시(위험 flags / boss advisory / raw output 분리). 자동 승인은 `--yes` 명시 시에만.

답습: docs/phase0/jarvis-cli-entrypoint-brief.md
  - 워커 = OllamaWorker (트랙 B urllib + 70 송신 redaction, facade 미경유 — CC-0 회피, (나) 일관)
  - DEFAULT_MODEL = 71 ollama 실동작 검증 모델 (default + override = m3-m4 Liquidity-compliant)
"""
from __future__ import annotations

import argparse
import os
import sys
import uuid
from typing import Callable, TextIO

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import OllamaBoss
from src.jarvis.memory import MemoryLog
from src.jarvis.orchestrator import (
    Orchestrator,
    OutcomeReport,
    OutcomeStatus,
    WorkerRegistry,
)
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import OllamaWorker

DEFAULT_MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
DEFAULT_MEMORY_PATH = "~/.jarvis/memory.jsonl"

_EXIT_CODE = {
    OutcomeStatus.APPLIED: 0,
    OutcomeStatus.WORKER_FAILED: 1,
    OutcomeStatus.DENIED: 2,
}

Approver = Callable[[ApprovalRequest], bool]


def auto_approver(req: ApprovalRequest) -> bool:
    """비대화형 자동 승인 (`--yes` — 사람 명시 의도). default 아님."""
    return True


def make_interactive_approver(
    input_fn: Callable[[str], str] = input, out: TextIO | None = None
) -> Approver:
    """인터랙티브 인간 승인 게이트 — R10 분리 표시 + default-deny.

    위험 flags(결정적) / boss advisory(보조) / raw output 을 *분리* 노출 →
    advice 단독 의존 금지(green-washing 방어). `y`/`yes` 만 승인, 그 외(빈 입력 포함) 거부.
    """
    stream = out if out is not None else sys.stdout

    def approver(req: ApprovalRequest) -> bool:
        print("\n=== 반영 승인 요청 (반영 전 사람 게이트) ===", file=stream)
        print(f"worker: {req.worker_alias}", file=stream)
        print(f"위험 flags: {req.flags if req.flags else '(없음)'}", file=stream)
        if req.advice is not None:
            tag = " ⚠️(advisory 실패)" if req.advice.advisory_failed else ""
            print(f"boss 검토{tag}: {req.advice.summary}", file=stream)
        print(f"출력 미리보기:\n{req.output_preview}", file=stream)
        answer = input_fn("반영 승인? [y/N] ").strip().lower()
        return answer in {"y", "yes"}

    return approver


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="jarvis",
        description="jarvis — 통제된 로컬 사장+워커 (반영 전 사람 승인 게이트, default-deny)",
    )
    p.add_argument("prompt", help="워커에게 줄 작업 프롬프트")
    p.add_argument("--worker-alias", default="ollama", help="워커 alias (default: ollama)")
    p.add_argument("--worker-model", default=DEFAULT_MODEL, help="워커 ollama 모델")
    p.add_argument("--boss-model", default=DEFAULT_MODEL, help="boss ollama 모델")
    p.add_argument("--no-boss", action="store_true", help="boss advisory 비활성")
    p.add_argument("--yes", action="store_true", help="자동 승인 (비대화형 — 사람 명시 의도)")
    p.add_argument("--memory-path", default=DEFAULT_MEMORY_PATH, help="관찰 누적 JSONL 경로")
    p.add_argument("--no-memory", action="store_true", help="관찰 누적 비활성")
    p.add_argument("--output-filename", default=None, help="워커 산출을 workdir 안 파일로 작성")
    p.add_argument("--task-id", default=None, help="작업 ID (default: 자동 생성)")
    return p


def build_orchestrator(ns: argparse.Namespace, approver: Approver) -> Orchestrator:
    registry = WorkerRegistry()
    registry.register(
        OllamaWorker(
            alias=ns.worker_alias,
            model=ns.worker_model,
            output_filename=ns.output_filename,
        )
    )
    guard = ReviewGuard()
    gate = ApprovalGate(approver=approver)
    boss = None if ns.no_boss else OllamaBoss(model=ns.boss_model)
    memory = None if ns.no_memory else MemoryLog(os.path.expanduser(ns.memory_path))
    return Orchestrator(registry, guard, gate, boss=boss, memory=memory)


def print_report(report: OutcomeReport, out: TextIO | None = None) -> None:
    stream = out if out is not None else sys.stdout
    print("\n=== 결과 ===", file=stream)
    print(f"status : {report.status.value}", file=stream)
    print(f"worker : {report.worker_alias}", file=stream)
    print(f"flags  : {report.verdict.flags if report.verdict.flags else '(없음)'}", file=stream)
    if report.advice is not None:
        print(f"boss   : {report.advice.summary}", file=stream)
    print(f"applied: {report.applied}", file=stream)
    print(f"--- output ---\n{report.result.output}", file=stream)


def main(argv: list[str] | None = None) -> int:
    ns = build_parser().parse_args(argv)
    approver: Approver = auto_approver if ns.yes else make_interactive_approver()
    orchestrator = build_orchestrator(ns, approver)
    task_id = ns.task_id or uuid.uuid4().hex[:8]
    report = orchestrator.dispatch(ns.prompt, task_id, ns.worker_alias)
    print_report(report)
    return _EXIT_CODE.get(report.status, 0)


if __name__ == "__main__":
    raise SystemExit(main())
