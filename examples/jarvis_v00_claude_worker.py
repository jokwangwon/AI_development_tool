#!/usr/bin/env python3
"""Jarvis v0.0 — claude 워커 + OllamaBoss + Layer 0 통합 demo.

답습: docs/phase0/jarvis-claude-worker-integration-brief.md §2
  - 워커 = claude headless (실 LLM, 토큰 소비)
  - 격리 = LandlockIsolation (커널 강제, MVP-0 트랙 B 답습)
  - 사장 = OllamaBoss(Qwen3-30B-A3B) 로컬 추론 검토
  - 누적 = MemoryLog Layer 0
  - 실 코딩 작업: fizzbuzz.py 생성 + 파일 검증

⚠️ 실 claude 토큰 소비 (~$0.05 추정) + 실 Ollama 호출 + 실 디스크 쓰기.
사용:
    python examples/jarvis_v00_claude_worker.py
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import OllamaBoss
from src.jarvis.isolation import LandlockIsolation
from src.jarvis.memory import MemoryLog
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import CliWorker

MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
MEMORY_PATH = "/tmp/jarvis-v00-claude-worker-memory.jsonl"
OLLAMA_RAW_PATH = "/tmp/jarvis-v00-claude-worker-ollama-raw.log"
CLAUDE_RAW_PATH = "/tmp/jarvis-v00-claude-worker-claude-raw.log"

DEFAULT_PROMPT = (
    "Create a Python file named fizzbuzz.py in the current directory that prints "
    "fizzbuzz output for numbers 1 to 15 (replace multiples of 3 with 'Fizz', "
    "multiples of 5 with 'Buzz', multiples of both with 'FizzBuzz'). "
    "Then stop. Do not run it."
)

# claude `-p` 가 격리 안에서 동작하려면 홈 통째 RO 필요 (e2e demo 답습).
CLAUDE_RO_PATHS = [
    "/usr", "/lib", "/bin", "/sbin", "/etc", "/proc", "/dev", "/run",
    os.path.expanduser("~"),
]


def _claude_runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
    """claude headless — cwd=workdir, TMPDIR=workdir (e2e demo 답습)."""
    env = {**os.environ, "TMPDIR": workdir}
    proc = subprocess.run(cmd, cwd=workdir, env=env,
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis claude 워커 + Qwen3 사장 demo")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    ap.add_argument("--model", default=MODEL)
    args = ap.parse_args()

    # 깨끗한 evidence 를 위해 기존 memory 삭제
    if os.path.exists(MEMORY_PATH):
        os.remove(MEMORY_PATH)

    workdir = tempfile.mkdtemp(prefix="jarvis-v00-claude-")
    memory = MemoryLog(path=MEMORY_PATH)

    isolation = LandlockIsolation(ro_paths=CLAUDE_RO_PATHS)
    worker = CliWorker(
        alias="claude",
        argv=["claude", "--output-format", "json",
              "--dangerously-skip-permissions", "-p"],
        isolation=isolation,
        runner=_claude_runner,
    )
    registry = WorkerRegistry()
    registry.register(worker)

    boss = OllamaBoss(model=args.model, timeout_s=180.0)

    def approver(req: ApprovalRequest) -> bool:
        return True   # demo 자동 승인 (게이트 *경로* 보존)

    orch = Orchestrator(
        registry, ReviewGuard(), ApprovalGate(approver=approver),
        workdir_factory=lambda task_id: workdir,
        boss=boss,
        memory=memory,
    )

    print("=== Jarvis 실 LLM 워커 통합 demo ===")
    print(f"workdir : {workdir}")
    print(f"worker  : {worker.alias} (CliWorker, claude headless)")
    print(f"isolation: {isolation.name} (Landlock 커널 강제)")
    print(f"boss    : {boss.name} (Ollama 로컬)")
    print(f"memory  : {MEMORY_PATH}")
    print(f"prompt  : {args.prompt[:100]}...")
    print("dispatch …")

    t0 = time.monotonic()
    report = orch.dispatch(prompt=args.prompt, task_id="claude-worker-v00")
    elapsed = time.monotonic() - t0

    # raw evidence 기록
    claude_raw = report.result.output or ""
    advice_raw = report.advice.summary if report.advice else ""
    with open(CLAUDE_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(claude_raw)
    with open(OLLAMA_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(advice_raw)

    print("\n=== OutcomeReport ===")
    print(f"  status   : {report.status.value}")
    print(f"  exit     : {report.result.exit_code}")
    print(f"  elapsed  : {elapsed:.2f}s")
    cost = report.result.cost_usd
    print(f"  cost     : ${cost:.4f}" if cost is not None else "  cost     : n/a")
    print(f"  verdict  : ok={report.verdict.ok} flags={report.verdict.flags}")
    print(f"  applied  : {report.applied}")

    # 파일 검증
    fizz_path = os.path.join(workdir, "fizzbuzz.py")
    fizz_exists = os.path.isfile(fizz_path)
    fizz_content = ""
    if fizz_exists:
        with open(fizz_path, encoding="utf-8") as fh:
            fizz_content = fh.read()

    print("\n--- 생성된 fizzbuzz.py ---")
    print(fizz_content if fizz_content else "(생성 안 됨)")
    print("--- end ---")

    print(f"\n--- Qwen3 한국어 요약 ({len(advice_raw)} chars) ---")
    print(advice_raw)
    print("--- end ---")

    # Layer 0 entry 확인
    entries = list(memory.read())
    print(f"\n[Layer 0] {len(entries)} entry 누적 → {MEMORY_PATH}")
    if entries:
        print(json.dumps(entries[0], ensure_ascii=False, indent=2))

    print(f"\n[evidence] claude raw → {CLAUDE_RAW_PATH}")
    print(f"[evidence] ollama raw → {OLLAMA_RAW_PATH}")

    checks = {
        "exit 0":                       report.result.exit_code == 0,
        "cost_usd > 0 (실 토큰 소비)":     cost is not None and cost > 0,
        "fizzbuzz.py 존재":              fizz_exists,
        "코드에 'fizz' 키워드 포함":        "fizz" in fizz_content.lower(),
        "advice non-empty":             bool(advice_raw.strip()),
        "advisory not failed":          report.advice is not None
                                        and not report.advice.advisory_failed,
        "Layer 0 entry 1건":             len(entries) == 1,
        "applied":                      report.applied,
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nCLAUDE-WORKER DONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
