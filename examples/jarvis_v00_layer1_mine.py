#!/usr/bin/env python3
"""Jarvis Layer 1 demo — Layer 0 JSONL 읽어 패턴 보고서 산출.

답습: docs/phase0/jarvis-layer1-pattern-mining-brief.md §5
  - mine(MemoryLog.read()) → PatternReport
  - format_report() 사람 가독 텍스트
  - 별도 JSON dump = /tmp/jarvis-v00-layer1-report.json
  - Layer 0 자체 수정 0 (read-only)

⚠️ 실 디스크 read (Layer 0 JSONL) + JSON 쓰기 (/tmp).
사용:
    python examples/jarvis_v00_layer1_mine.py
    python examples/jarvis_v00_layer1_mine.py --memory /path/to/jsonl
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.layer1 import format_report, mine
from src.jarvis.memory import MemoryLog
from src.jarvis import paths

DEFAULT_MEMORY = str(paths.layer0_memory_path())
REPORT_JSON_PATH = str(paths.layer1_report_path())


def _report_to_dict(report) -> dict:
    """frozen dataclass → JSON-encodable dict (tuple→list 변환)."""
    d = dataclasses.asdict(report)
    d["workers"] = [dataclasses.asdict(w) for w in report.workers]
    d["recent_failures"] = list(report.recent_failures)
    return d


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis Layer 1 패턴 마이닝")
    ap.add_argument("--memory", default=DEFAULT_MEMORY,
                    help="Layer 0 JSONL 경로")
    ap.add_argument("--limit", type=int, default=5,
                    help="recent_failures 상한")
    args = ap.parse_args()

    if not os.path.exists(args.memory):
        print(f"[error] Layer 0 JSONL 파일 없음: {args.memory}")
        print("        먼저 examples/jarvis_v00_layer0_memory.py 실행 후 재시도.")
        return 1

    log = MemoryLog(path=args.memory)
    entries = list(log.read())
    report = mine(entries, recent_failure_limit=args.limit)

    print(format_report(report))

    # JSON dump (Layer 2 입력 candidate — 다만 본 demo 는 사람 보고만)
    with open(REPORT_JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(_report_to_dict(report), fh, ensure_ascii=False, indent=2)

    print(f"\n[evidence] JSON report → {REPORT_JSON_PATH}")

    checks = {
        "Layer 0 file exists":      os.path.exists(args.memory),
        "entries > 0":              report.total_entries > 0,
        "workers 집계 ≥ 1":          len(report.workers) >= 1,
        "format_report non-empty":  bool(format_report(report).strip()),
        "JSON report 기록":          os.path.exists(REPORT_JSON_PATH),
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nLAYER 1 DONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
