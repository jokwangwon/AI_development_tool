#!/usr/bin/env python3
"""Jarvis v0.0 — codex(OpenAI ChatGPT) 워커 추가 demo.

답습: docs/phase0/jarvis-codex-worker-integration-brief.md
  - claude 워커와 동형 통합 (CliWorker + LandlockIsolation + OllamaBoss + Layer 0).
  - 차이점: codex --json = NDJSON stream → _parse_codex_ndjson 어댑터로
    claude-shaped JSON {'result', 'is_error', 'total_cost_usd'} 정규화.
  - boundary normalization = WorkerResult.from_cli 변경 0건, CliWorker 재사용.

⚠️ 실 codex(ChatGPT) 호출 + 실 Ollama + 실 디스크 쓰기.
사용:
    python examples/jarvis_v00_codex_worker.py
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
from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.memory import MemoryLog
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import CliWorker
from src.jarvis import paths

MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
MEMORY_PATH = str(paths.data_file("jarvis-v00-codex-worker-memory.jsonl"))
OLLAMA_RAW_PATH = str(paths.worker_raw_log_path("codex", "ollama"))
CODEX_RAW_PATH = str(paths.worker_raw_log_path("codex", "codex"))
CODEX_NDJSON_PATH = str(paths.data_file("jarvis-v00-codex-worker-codex-ndjson.log"))

# claude 워커와 *동일* fizzbuzz prompt = Provider Liquidity side-by-side 입증.
DEFAULT_PROMPT = (
    "Create a Python file named fizzbuzz.py in the current directory that prints "
    "fizzbuzz output for numbers 1 to 15 (replace multiples of 3 with 'Fizz', "
    "multiples of 5 with 'Buzz', multiples of both with 'FizzBuzz'). "
    "Then stop. Do not run it."
)

# ⚠️ 격리 = PassthroughIsolation (codex 후속 cycle 사유):
#   codex 는 `~/.codex/sessions/` + `~/.codex/tmp/` 에 *쓰기* 필요.
#   현 ll_sandbox.c = 단일 RW 디렉터리만 지원 → workdir 안에서 codex 실행 불가.
#   후속 cycle = (a) ll_sandbox multi-RW 지원 OR (b) codex env path override.
#   본 demo = Provider Liquidity 활용 1차 입증 한정. 격리 hardening = 별도 cycle.


def _parse_codex_ndjson(stdout: str) -> dict:
    """codex --json NDJSON stream → claude-shaped {'result', 'is_error', 'total_cost_usd'}.

    schema 답습(2026-05-26 codex-cli 0.128.0):
      {"type":"thread.started", ...}
      {"type":"turn.started"}
      {"type":"item.completed","item":{"id":..., "type":"agent_message","text":"..."}}
      {"type":"turn.completed","usage":{...}}

    last `item.completed`(type=`agent_message`).text = result.
    부재 = is_error=True (silent success 차단, brief §3 답습).
    cost_usd = None (codex 토큰 수만 보고, USD 환산은 모델 가격표 영역).
    """
    last_text: str | None = None
    saw_completion = False
    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue                        # 손상 라인 skip
        if evt.get("type") == "item.completed":
            item = evt.get("item") or {}
            if item.get("type") == "agent_message":
                last_text = item.get("text")
        if evt.get("type") == "turn.completed":
            saw_completion = True

    if not last_text:
        return {"result": "", "is_error": True, "total_cost_usd": None}
    return {
        "result": last_text,
        "is_error": not saw_completion,    # turn.completed 부재 = 미완료
        "total_cost_usd": None,
    }


def _codex_runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
    """codex 실행 + NDJSON → claude-shaped JSON 변환.

    stdin=/dev/null 명시 (codex 가 stdin 대기 차단). NDJSON raw 는 별도 파일 보존.
    """
    env = {**os.environ, "TMPDIR": workdir}
    with open(os.devnull, "rb") as devnull:
        proc = subprocess.run(
            cmd, cwd=workdir, env=env,
            stdin=devnull, capture_output=True, text=True,
        )
    with open(CODEX_NDJSON_PATH, "w", encoding="utf-8") as fh:
        fh.write(proc.stdout)
    parsed = _parse_codex_ndjson(proc.stdout)
    return proc.returncode, json.dumps(parsed, ensure_ascii=False), proc.stderr


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis codex 워커 + Qwen3 사장 demo")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    ap.add_argument("--model", default=MODEL)
    args = ap.parse_args()

    if os.path.exists(MEMORY_PATH):
        os.remove(MEMORY_PATH)

    workdir = tempfile.mkdtemp(prefix="jarvis-v00-codex-")
    memory = MemoryLog(path=MEMORY_PATH)

    isolation = PassthroughIsolation()    # codex ~/.codex 쓰기 의존, multi-RW 후속
    worker = CliWorker(
        alias="codex",       # claude alias 와 *구분* (Layer 0/1 마이닝 자료)
        argv=["codex", "exec", "--json",
              "--dangerously-bypass-approvals-and-sandbox",
              "-C", workdir],
        isolation=isolation,
        runner=_codex_runner,
    )
    registry = WorkerRegistry()
    registry.register(worker)

    boss = OllamaBoss(model=args.model, timeout_s=180.0)

    def approver(req: ApprovalRequest) -> bool:
        return True

    orch = Orchestrator(
        registry, ReviewGuard(), ApprovalGate(approver=approver),
        workdir_factory=lambda task_id: workdir,
        boss=boss,
        memory=memory,
    )

    print("=== Jarvis codex 워커 추가 demo (Provider Liquidity) ===")
    print(f"workdir : {workdir}")
    print(f"worker  : {worker.alias} (CliWorker, codex exec --json)")
    print(f"isolation: {isolation.name} (⚠️ codex ~/.codex 쓰기 의존 → 격리 hardening = 후속)")
    print(f"boss    : {boss.name} (Ollama 로컬)")
    print(f"memory  : {MEMORY_PATH}")
    print(f"prompt  : {args.prompt[:100]}...")
    print("dispatch …")

    t0 = time.monotonic()
    report = orch.dispatch(prompt=args.prompt, task_id="codex-worker-v00")
    elapsed = time.monotonic() - t0

    codex_text = report.result.output or ""
    advice_raw = report.advice.summary if report.advice else ""
    with open(CODEX_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(codex_text)
    with open(OLLAMA_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(advice_raw)

    print("\n=== OutcomeReport ===")
    print(f"  status   : {report.status.value}")
    print(f"  exit     : {report.result.exit_code}")
    print(f"  elapsed  : {elapsed:.2f}s")
    print(f"  verdict  : ok={report.verdict.ok} flags={report.verdict.flags}")
    print(f"  applied  : {report.applied}")

    fizz_path = os.path.join(workdir, "fizzbuzz.py")
    fizz_exists = os.path.isfile(fizz_path)
    fizz_content = ""
    if fizz_exists:
        with open(fizz_path, encoding="utf-8") as fh:
            fizz_content = fh.read()

    print("\n--- 생성된 fizzbuzz.py ---")
    print(fizz_content if fizz_content else "(생성 안 됨)")
    print("--- end ---")

    print(f"\n--- codex agent_message ({len(codex_text)} chars) ---")
    print(codex_text[:500] + ("..." if len(codex_text) > 500 else ""))
    print("--- end ---")

    print(f"\n--- Qwen3 한국어 요약 ({len(advice_raw)} chars) ---")
    print(advice_raw)
    print("--- end ---")

    entries = list(memory.read())
    print(f"\n[Layer 0] {len(entries)} entry 누적 → {MEMORY_PATH}")
    if entries:
        e = entries[0]
        print(f"  worker_alias = {e['worker_alias']}  status = {e['status']}")

    print(f"\n[evidence] codex result → {CODEX_RAW_PATH}")
    print(f"[evidence] codex NDJSON  → {CODEX_NDJSON_PATH}")
    print(f"[evidence] ollama raw   → {OLLAMA_RAW_PATH}")

    checks = {
        "exit 0":                       report.result.exit_code == 0,
        "fizzbuzz.py 존재":              fizz_exists,
        "코드에 'fizz' 키워드 포함":        "fizz" in fizz_content.lower(),
        "advice non-empty":             bool(advice_raw.strip()),
        "advisory not failed":          report.advice is not None
                                        and not report.advice.advisory_failed,
        "Layer 0 entry 1건":             len(entries) == 1,
        "Layer 0 alias = codex":         entries and entries[0]["worker_alias"] == "codex",
        "applied":                      report.applied,
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nCODEX-WORKER DONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
