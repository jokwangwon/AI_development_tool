#!/usr/bin/env python3
"""Jarvis MVP-1 트랙 B 보스 LLM 측정 — N=3 decode/prefill/latency 통계.

답습: docs/phase0/jarvis-mvp1-track-b-boss-measurement-brief.md
  - 단일 모델 (현 OllamaBoss 기본) 한정 — 다중 모델 비교 = 후속 cycle.
  - N=3 동형 호출 + warmup 1 회 (cache 가열, 측정 외).
  - Ollama /api/chat metadata 6 필드 + 파생 metric 3 종.
  - M3·M4 결정 *고정* 0건 (측정 자료 수집만).

⚠️ 실 Ollama 호출 (warmup 1 + measure 3 = 총 4 회).
사용:
    python examples/jarvis_v00_boss_measurement.py
    python examples/jarvis_v00_boss_measurement.py --runs 5 --model llama3.3:70b
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import os
import time
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.boss import boss_prompt_for

DEFAULT_MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"
EVIDENCE_PATH = "/tmp/jarvis-v00-boss-measurement.json"

# 표준 advice prompt (실 운영 형태) — 동형 호출 N 회용 고정 input
ADVICE_USER_BLOB = (
    "[task prompt]\nCreate fizzbuzz.py for 1-15.\n\n"
    "[worker alias] claude\n\n"
    "[worker output]\n"
    "for i in range(1, 16):\n"
    "    if i % 15 == 0: print('FizzBuzz')\n"
    "    elif i % 3 == 0: print('Fizz')\n"
    "    elif i % 5 == 0: print('Buzz')\n"
    "    else: print(i)\n\n"
    "[deterministic flags]\n"
)


def _ollama_has_model(model: str) -> bool:
    try:
        with urllib.request.urlopen(OLLAMA_TAGS_URL, timeout=5) as resp:
            data = json.loads(resp.read())
    except Exception:
        return False
    return any(m.get("name") == model for m in (data.get("models") or []))


def _call_ollama(model: str, system_prompt: str, user_blob: str,
                 timeout_s: float = 180.0) -> dict:
    """단일 Ollama /api/chat 호출 → 응답 dict 전체 반환 (metadata 6 필드 포함).

    실패 시 빈 dict 반환 + caller 가 에러 처리.
    """
    body = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_blob},
        ],
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_CHAT_URL, data=data, method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            return json.loads(resp.read())
    except (urllib.error.URLError, OSError, ValueError) as exc:
        return {"_error": str(exc)}


def _extract_metrics(payload: dict) -> dict:
    """Ollama 응답에서 6 metadata + 3 파생 metric 추출."""
    if "_error" in payload:
        return {"error": payload["_error"]}

    md = {
        "total_duration_ns":     payload.get("total_duration", 0),
        "load_duration_ns":      payload.get("load_duration", 0),
        "prompt_eval_count":     payload.get("prompt_eval_count", 0),
        "prompt_eval_duration_ns": payload.get("prompt_eval_duration", 0),
        "eval_count":            payload.get("eval_count", 0),
        "eval_duration_ns":      payload.get("eval_duration", 0),
    }

    # 파생 metric (0-division 차단)
    eval_dur_s = md["eval_duration_ns"] / 1e9 if md["eval_duration_ns"] else 0.0
    prefill_dur_s = md["prompt_eval_duration_ns"] / 1e9 if md["prompt_eval_duration_ns"] else 0.0
    md["decode_tok_per_s"] = (md["eval_count"] / eval_dur_s) if eval_dur_s > 0 else 0.0
    md["prefill_tok_per_s"] = (md["prompt_eval_count"] / prefill_dur_s) if prefill_dur_s > 0 else 0.0
    md["latency_s"] = md["total_duration_ns"] / 1e9 if md["total_duration_ns"] else 0.0
    return md


def _summarize(values: list[float]) -> dict:
    """N 값 → mean/p50/std/min/max (N<2 시 std=0)."""
    if not values:
        return {"mean": 0.0, "p50": 0.0, "std": 0.0, "min": 0.0, "max": 0.0}
    mean = statistics.mean(values)
    p50 = statistics.median(values)
    std = statistics.stdev(values) if len(values) > 1 else 0.0
    return {"mean": mean, "p50": p50, "std": std, "min": min(values), "max": max(values)}


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis MVP-1 트랙 B 보스 측정")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--skip-warmup", action="store_true",
                    help="warmup 1 회 생략 (cold 측정용)")
    args = ap.parse_args()

    print("=== Jarvis MVP-1 트랙 B 보스 측정 ===")
    print(f"model    : {args.model}")
    print(f"runs     : N={args.runs} (+ warmup={'skip' if args.skip_warmup else '1'})")

    # precheck
    if not _ollama_has_model(args.model):
        print(f"\n[error] Ollama 에 {args.model} 미설치.")
        return 1
    print("precheck : PASS (Ollama daemon + 모델 가용)")

    system_prompt = boss_prompt_for("code")

    # warmup (측정 외)
    if not args.skip_warmup:
        print("warmup   : 1 회 호출 (cache 가열, 측정 외)…")
        t0 = time.monotonic()
        _call_ollama(args.model, system_prompt, ADVICE_USER_BLOB)
        print(f"  elapsed = {time.monotonic() - t0:.2f}s")

    # measurement N
    print(f"measure  : N={args.runs} 동형 호출 시작…")
    runs: list[dict] = []
    for i in range(args.runs):
        t0 = time.monotonic()
        payload = _call_ollama(args.model, system_prompt, ADVICE_USER_BLOB)
        elapsed = time.monotonic() - t0
        metrics = _extract_metrics(payload)
        runs.append(metrics)
        if "error" in metrics:
            print(f"  run {i + 1}/{args.runs}: FAIL ({metrics['error']})")
        else:
            print(
                f"  run {i + 1}/{args.runs}: "
                f"decode={metrics['decode_tok_per_s']:.2f} tok/s "
                f"prefill={metrics['prefill_tok_per_s']:.2f} tok/s "
                f"latency={metrics['latency_s']:.2f}s "
                f"eval_count={metrics['eval_count']} "
                f"elapsed={elapsed:.2f}s"
            )

    valid = [r for r in runs if "error" not in r]
    if not valid:
        print("\n[error] 모든 run 실패")
        return 1

    decode_vals = [r["decode_tok_per_s"] for r in valid]
    prefill_vals = [r["prefill_tok_per_s"] for r in valid]
    latency_vals = [r["latency_s"] for r in valid]

    decode_stats = _summarize(decode_vals)
    prefill_stats = _summarize(prefill_vals)
    latency_stats = _summarize(latency_vals)

    print("\n=== 통계 (N=" + str(len(valid)) + ") ===")
    for name, stats in (("decode  (tok/s)", decode_stats),
                        ("prefill (tok/s)", prefill_stats),
                        ("latency (s)    ", latency_stats)):
        print(
            f"  {name}: mean={stats['mean']:.2f} p50={stats['p50']:.2f} "
            f"std={stats['std']:.2f} min={stats['min']:.2f} max={stats['max']:.2f}"
        )

    # raw JSON evidence
    evidence = {
        "model": args.model,
        "runs": runs,
        "stats": {
            "decode_tok_per_s": decode_stats,
            "prefill_tok_per_s": prefill_stats,
            "latency_s": latency_stats,
        },
        "n_valid": len(valid),
        "n_total": len(runs),
    }
    with open(EVIDENCE_PATH, "w", encoding="utf-8") as fh:
        json.dump(evidence, fh, ensure_ascii=False, indent=2)
    print(f"\n[evidence] raw JSON → {EVIDENCE_PATH}")

    # 합격 조건
    checks = {
        "precheck PASS":     True,
        "N runs >= 1 valid": len(valid) >= 1,
        "decode > 0":        decode_stats["mean"] > 0,
        "prefill > 0":       prefill_stats["mean"] > 0,
        "evidence 기록":      os.path.exists(EVIDENCE_PATH),
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nBOSS-MEASUREMENT DONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
