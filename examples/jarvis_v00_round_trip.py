#!/usr/bin/env python3
"""Jarvis v0.0 Round-Trip Demo — Boss(OllamaBoss) → Worker(TmuxWorker) 1회 실 통합.

v0.0 sprint DONE 기준 (docs/phase0/jarvis-v00-working-sprint-brief.md §4):
  사용자 prompt → Orchestrator → TmuxWorker 실 명령 → tmux 출력 회수
  → OllamaBoss advise(실 Ollama HTTP) → ApprovalGate(자동 승인 demo) → 보고.

raw evidence 2건:
  (a) Ollama 응답 raw text  → /tmp/jarvis-v00-ollama-raw.log
  (b) tmux capture-pane raw → /tmp/jarvis-v00-tmux-raw.log

합격 조건: exit 0 + Ollama 응답 non-empty + tmux 출력 non-empty + advice non-empty.

⚠️ 실 Ollama 호출 발생 (localhost:11434). 실 tmux session spawn 발생.
사용:
    python examples/jarvis_v00_round_trip.py
"""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import OllamaBoss
from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import TmuxWorker
from src.jarvis import paths

DEFAULT_MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
DEFAULT_PROMPT = "echo JARVIS_V00_ROUND_TRIP_OK && date -Is"
OLLAMA_RAW_PATH = str(paths.data_file("jarvis-v00-ollama-raw.log"))
TMUX_RAW_PATH = str(paths.data_file("jarvis-v00-tmux-raw.log"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis v0.0 round-trip demo")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT, help="워커에게 실행시킬 shell 명령")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Ollama 모델 이름")
    ap.add_argument("--no-boss", action="store_true",
                    help="OllamaBoss 미주입(워커-only 진단용)")
    args = ap.parse_args()

    workdir = tempfile.mkdtemp(prefix="jarvis-v00-")

    worker = TmuxWorker(
        alias="tmux-bash",
        argv=["bash", "-lc"],
        isolation=PassthroughIsolation(),
        poll_attempts=30,
        poll_interval_s=0.5,
    )
    registry = WorkerRegistry()
    registry.register(worker)

    boss = None if args.no_boss else OllamaBoss(model=args.model, timeout_s=120.0)

    def approver(req: ApprovalRequest) -> bool:
        # v0.0 demo = 자동 승인 (사람 게이트 *경로* 자체는 보존, 의사결정만 자동화).
        return True

    orch = Orchestrator(
        registry,
        ReviewGuard(),
        ApprovalGate(approver=approver),
        workdir_factory=lambda task_id: workdir,
        boss=boss,
    )

    print("=== Jarvis v0.0 Round-Trip Demo ===")
    print(f"workdir : {workdir}")
    print(f"worker  : {worker.alias} (TmuxWorker)")
    print(f"boss    : {(boss.name if boss else '(없음)')}")
    print(f"prompt  : {args.prompt}")
    print("dispatch …")

    t0 = time.monotonic()
    report = orch.dispatch(prompt=args.prompt, task_id="v00-round-trip")
    elapsed = time.monotonic() - t0

    tmux_raw = report.result.output or ""
    advice = report.advice
    advice_raw = advice.summary if advice else ""
    advisory_failed = bool(advice and advice.advisory_failed)

    # raw evidence 2건 기록 (git tracked 0건 — 답습 메타는 commit log 한정).
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

    print("\n--- (b) tmux capture-pane raw ---")
    print(tmux_raw)
    print("--- end (b) ---")
    print(f"\n--- (a) Ollama 응답 raw ({len(advice_raw)} chars) ---")
    print(advice_raw)
    print("--- end (a) ---")

    print(f"\n[evidence] tmux raw → {TMUX_RAW_PATH}")
    print(f"[evidence] ollama raw → {OLLAMA_RAW_PATH}")

    # 합격 조건 (docs/phase0/jarvis-v00-working-sprint-brief.md §4)
    checks = {
        "exit 0":         report.result.exit_code == 0,
        "tmux non-empty": bool(tmux_raw.strip()),
        "boss 주입":      boss is not None,
        "advice non-empty": bool(advice_raw.strip()),
        "advisory not failed": not advisory_failed,
        "applied":        report.applied,
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nDONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
