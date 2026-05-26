#!/usr/bin/env python3
"""Jarvis v0.0 실 개발 작업 demo — pre-commit 검증을 jarvis 가 실행.

v0.0 sprint evidence 격상: hello-world(`echo`) → 실 개발 워크플로 1건.
시나리오: 개발자가 commit 전 일상적으로 돌리는 검증(pytest + lint-imports)을
jarvis 가 실 명령으로 실행 → boss(Ollama) 가 결과를 한국어로 요약 → 사람 게이트.

⚠️ 실 Ollama 호출 + 실 tmux session + 실 pytest/lint-imports 실행.
사용:
    python examples/jarvis_v00_dev_task.py
    python examples/jarvis_v00_dev_task.py --check        # 검증 미실행, 회로만
"""
from __future__ import annotations

import argparse
import os
import shlex
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import OllamaBoss, boss_prompt_for
from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import TmuxWorker

DEFAULT_MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV_ACTIVATE = os.path.join(PROJECT_ROOT, ".venv", "bin", "activate")

DEV_TASK = (
    f"source {shlex.quote(VENV_ACTIVATE)} && "
    "python -m pytest tests/jarvis/ --tb=line -q 2>&1 | tail -25 && "
    "echo '--- lint-imports ---' && "
    "lint-imports --config .importlinter 2>&1 | tail -8"
)

TMUX_RAW_PATH = "/tmp/jarvis-v00-dev-task-tmux-raw.log"
OLLAMA_RAW_PATH = "/tmp/jarvis-v00-dev-task-ollama-raw.log"


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis v0.0 실 dev task demo")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Ollama 모델")
    ap.add_argument("--prompt", default=DEV_TASK, help="실행 shell 명령")
    args = ap.parse_args()

    worker = TmuxWorker(
        alias="tmux-bash",
        argv=["bash", "-lc"],
        isolation=PassthroughIsolation(),
        poll_attempts=60,
        poll_interval_s=1.0,
    )
    registry = WorkerRegistry()
    registry.register(worker)

    # (m) shell 도메인 prompt 주입 — pytest+lint 명령 실행 검토 (코드 도메인 부적합).
    boss = OllamaBoss(
        model=args.model,
        timeout_s=180.0,
        system_prompt=boss_prompt_for("shell"),
    )

    def approver(req: ApprovalRequest) -> bool:
        return True   # demo = 자동 승인 (게이트 *경로* 보존, 의사결정만 자동)

    orch = Orchestrator(
        registry,
        ReviewGuard(),
        ApprovalGate(approver=approver),
        workdir_factory=lambda task_id: PROJECT_ROOT,
        boss=boss,
    )

    print("=== Jarvis v0.0 실 개발 작업 demo ===")
    print(f"workdir : {PROJECT_ROOT}")
    print(f"worker  : {worker.alias} (TmuxWorker)")
    print(f"boss    : {boss.name}")
    print(f"task    : pytest + lint-imports (pre-commit 검증)")
    print("dispatch …")

    t0 = time.monotonic()
    report = orch.dispatch(prompt=args.prompt, task_id="v00-dev-task")
    elapsed = time.monotonic() - t0

    tmux_raw = report.result.output or ""
    advice = report.advice
    advice_raw = advice.summary if advice else ""
    advisory_failed = bool(advice and advice.advisory_failed)

    with open(TMUX_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(tmux_raw)
    with open(OLLAMA_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(advice_raw)

    print("\n=== OutcomeReport ===")
    print(f"  status   : {report.status.value}")
    print(f"  worker   : {report.worker_alias}")
    print(f"  exit     : {report.result.exit_code}")
    print(f"  elapsed  : {elapsed:.2f}s")
    print(f"  verdict  : ok={report.verdict.ok} flags={report.verdict.flags}")
    print(f"  applied  : {report.applied}")

    print("\n--- (b) tmux capture-pane raw (마지막 60줄) ---")
    tail = "\n".join(tmux_raw.splitlines()[-60:])
    print(tail)
    print("--- end (b) ---")
    print(f"\n--- (a) Ollama 한국어 요약 raw ({len(advice_raw)} chars) ---")
    print(advice_raw)
    print("--- end (a) ---")

    print(f"\n[evidence] tmux raw → {TMUX_RAW_PATH}")
    print(f"[evidence] ollama raw → {OLLAMA_RAW_PATH}")

    checks = {
        "exit 0":           report.result.exit_code == 0,
        "tmux non-empty":   bool(tmux_raw.strip()),
        "advice non-empty": bool(advice_raw.strip()),
        "advisory not failed": not advisory_failed,
        "applied":          report.applied,
        "tests passed signal (passed/failed 토큰 in output)":
            ("passed" in tmux_raw or "PASS" in tmux_raw)
            and ("KEPT" in tmux_raw or "kept" in tmux_raw),
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nDEV-TASK: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
