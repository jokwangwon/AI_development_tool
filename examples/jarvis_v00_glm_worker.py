#!/usr/bin/env python3
"""Jarvis v0.0 — GLM(Ollama 로컬) 워커 추가 demo.

답습: docs/phase0/jarvis-glm-worker-integration-brief.md
  - OllamaWorker = LLM-only worker (응답 텍스트만, fs 행동 능력 0).
  - 파일 쓰기 책무 = demo helper 가 *결정적*으로 workdir 에 작성.
  - claude/codex 와 다른 책임 모델 = prompt injection 으로 LLM 이
    위험 명령 출력해도 실행 경로 0건 = 구조적 안전.

⚠️ 실 Ollama HTTP 호출 (glm-4.7-flash 로컬, ~19GB Q4) + Qwen3 검토.
사용:
    python examples/jarvis_v00_glm_worker.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import OllamaBoss
from src.jarvis.memory import MemoryLog
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import OllamaWorker

BOSS_MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
WORKER_MODEL = "glm-4.7-flash:latest"
MEMORY_PATH = "/tmp/jarvis-v00-glm-worker-memory.jsonl"
OLLAMA_RAW_PATH = "/tmp/jarvis-v00-glm-worker-ollama-raw.log"
GLM_RAW_PATH = "/tmp/jarvis-v00-glm-worker-glm-raw.log"

DEFAULT_PROMPT = (
    "Write ONLY the Python code (no markdown fences, no explanation, no comments) "
    "for a program named fizzbuzz.py that prints fizzbuzz output for numbers 1 to 15 "
    "(multiples of 3 -> 'Fizz', multiples of 5 -> 'Buzz', multiples of both -> "
    "'FizzBuzz', otherwise the number). Output only the code."
)

def _ollama_has_model(model: str) -> bool:
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags",
                                    timeout=5) as resp:
            data = json.loads(resp.read())
    except Exception:
        return False
    return any(m.get("name") == model for m in (data.get("models") or []))


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis GLM 워커 + Qwen3 사장 demo")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    ap.add_argument("--worker-model", default=WORKER_MODEL)
    ap.add_argument("--boss-model", default=BOSS_MODEL)
    args = ap.parse_args()

    if not _ollama_has_model(args.worker_model):
        print(f"[error] Ollama 에 {args.worker_model} 미설치.")
        print(f"        다른 모델: --worker-model <name>")
        return 1

    if os.path.exists(MEMORY_PATH):
        os.remove(MEMORY_PATH)

    workdir = tempfile.mkdtemp(prefix="jarvis-v00-glm-")
    memory = MemoryLog(path=MEMORY_PATH)

    worker = OllamaWorker(
        alias="glm",
        model=args.worker_model,
        output_filename="fizzbuzz.py",   # workdir/fizzbuzz.py 결정적 작성
    )
    registry = WorkerRegistry()
    registry.register(worker)

    boss = OllamaBoss(model=args.boss_model, timeout_s=180.0)

    def approver(req: ApprovalRequest) -> bool:
        return True

    orch = Orchestrator(
        registry, ReviewGuard(), ApprovalGate(approver=approver),
        workdir_factory=lambda task_id: workdir,
        boss=boss,
        memory=memory,
    )

    print("=== Jarvis GLM 워커 추가 demo (로컬 LLM, 외부 비용 0) ===")
    print(f"workdir     : {workdir}")
    print(f"worker      : {worker.alias} (OllamaWorker, {args.worker_model})")
    print(f"isolation   : passthrough (LLM-only, fs 행동 능력 0)")
    print(f"boss        : {boss.name} (Ollama 로컬)")
    print(f"memory      : {MEMORY_PATH}")
    print(f"prompt      : {args.prompt[:100]}...")
    print("dispatch …")

    t0 = time.monotonic()
    report = orch.dispatch(prompt=args.prompt, task_id="glm-worker-v00")
    elapsed = time.monotonic() - t0

    glm_text = report.result.output or ""
    advice_raw = report.advice.summary if report.advice else ""
    with open(GLM_RAW_PATH, "w", encoding="utf-8") as fh:
        fh.write(glm_text)
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

    print(f"\n--- GLM 응답 raw ({len(glm_text)} chars) ---")
    print(glm_text[:500] + ("..." if len(glm_text) > 500 else ""))
    print("--- end ---")

    print(f"\n--- Qwen3 한국어 요약 ({len(advice_raw)} chars) ---")
    print(advice_raw)
    print("--- end ---")

    entries = list(memory.read())
    print(f"\n[Layer 0] {len(entries)} entry 누적 → {MEMORY_PATH}")
    if entries:
        e = entries[0]
        print(f"  worker_alias = {e['worker_alias']}  status = {e['status']}")

    print(f"\n[evidence] glm raw    → {GLM_RAW_PATH}")
    print(f"[evidence] ollama raw → {OLLAMA_RAW_PATH}")

    checks = {
        "exit 0":                       report.result.exit_code == 0,
        "GLM 응답 non-empty":            bool(glm_text.strip()),
        "fizzbuzz.py 존재":              fizz_exists,
        "코드에 'fizz' 키워드 포함":        "fizz" in fizz_content.lower(),
        "advice non-empty":             bool(advice_raw.strip()),
        "advisory not failed":          report.advice is not None
                                        and not report.advice.advisory_failed,
        "Layer 0 entry 1건":             len(entries) == 1,
        "Layer 0 alias = glm":           entries and entries[0]["worker_alias"] == "glm",
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nGLM-WORKER DONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
