#!/usr/bin/env python3
"""Jarvis 자가진화 Layer 0 demo — 3회 dispatch 관찰 누적 evidence.

답습: docs/phase0/jarvis-layer0-memory-accumulation-brief.md §6
  3회 dispatch (multi-task) → JSONL 3 entry 적재 확인 (실 디스크).

⚠️ 실 Ollama 호출 (3회) + 실 tmux session (3회) + JSONL 실 디스크 쓰기.
사용:
    python examples/jarvis_v00_layer0_memory.py
"""
from __future__ import annotations

import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import OllamaBoss
from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.memory import MemoryLog
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import TmuxWorker
from src.jarvis import paths

MEMORY_PATH = str(paths.layer0_memory_path())
MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"

TASKS = [
    ("layer0-task-1", "echo TASK1 && uname -m"),
    ("layer0-task-2", "echo TASK2 && date -Is"),
    ("layer0-task-3", "echo TASK3 && python3 -c 'print(1+1)'"),
]


def main() -> int:
    # 깨끗한 누적 evidence 를 위해 기존 파일 삭제 (1회 demo).
    if os.path.exists(MEMORY_PATH):
        os.remove(MEMORY_PATH)

    memory = MemoryLog(path=MEMORY_PATH)

    worker = TmuxWorker(
        alias="tmux-bash",
        argv=["bash", "-lc"],
        isolation=PassthroughIsolation(),
        poll_attempts=30,
        poll_interval_s=0.5,
    )
    registry = WorkerRegistry()
    registry.register(worker)

    boss = OllamaBoss(model=MODEL, timeout_s=120.0)
    gate = ApprovalGate(approver=lambda req: True)

    workdir = tempfile.mkdtemp(prefix="jarvis-v00-layer0-")
    orch = Orchestrator(
        registry, ReviewGuard(), gate,
        workdir_factory=lambda task_id: workdir,
        boss=boss,
        memory=memory,
    )

    print("=== Jarvis Layer 0 자가진화 demo (관찰 누적) ===")
    print(f"workdir : {workdir}")
    print(f"memory  : {MEMORY_PATH}")
    print(f"boss    : {MODEL}")
    print(f"tasks   : {len(TASKS)}")
    print()

    for task_id, prompt in TASKS:
        print(f"[dispatch] task_id={task_id}  prompt={prompt}")
        rep = orch.dispatch(prompt=prompt, task_id=task_id)
        print(f"   → status={rep.status.value} exit={rep.result.exit_code} "
              f"applied={rep.applied}")

    print(f"\n=== 누적 evidence ({MEMORY_PATH}) ===")
    entries = list(memory.read())
    for i, e in enumerate(entries, 1):
        print(f"--- entry {i} ---")
        print(json.dumps(e, ensure_ascii=False, indent=2))

    print("\n=== 합격 조건 ===")
    checks = {
        "entries == 3":           len(entries) == 3,
        "모든 status applied":    all(e["status"] == "applied" for e in entries),
        "모든 exit 0":            all(e["exit_code"] == 0 for e in entries),
        "advice_summary 누락 0":  all(e["advice_summary"] for e in entries),
        "민감 필드 (cost_usd) 0": all("cost_usd" not in e for e in entries),
        "민감 필드 (workdir) 0":  all("workdir" not in e for e in entries),
    }
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nLAYER 0 DONE: {'PASS' if all_pass else 'FAIL'}")
    print(f"[evidence] JSONL → {MEMORY_PATH}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
