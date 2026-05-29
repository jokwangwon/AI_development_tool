#!/usr/bin/env python3
"""Jarvis (p) 다중 모델 N=3 비교 측정.

답습: docs/phase0/jarvis-multi-model-measurement-brief.md
  - 4 후보 모델 (qwen3-30b-a3b / qwen2.5-coder:32b / exaone3.5:32b /
    glm-4.7-flash) 각 N=3 + warmup 1.
  - boss_measurement.py 의 helper 재사용 (책무 동일, 모델만 교체).
  - M3·M4 결정 *고정* 0건 = 측정 자료 수집만.

⚠️ 실 Ollama 호출 (4 모델 × 4 호출 = 총 16 회, 모델 로드 포함 ~2분).
사용:
    python examples/jarvis_v00_multi_model_measurement.py
    python examples/jarvis_v00_multi_model_measurement.py \\
        --models qwen3-30b-a3b-...,llama3.3:70b
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (a) helper 재사용
from examples.jarvis_v00_boss_measurement import (  # type: ignore[import-not-found]
    ADVICE_USER_BLOB, _call_ollama, _extract_metrics,
    _ollama_has_model, _summarize,
)
from src.jarvis.boss import boss_prompt_for
from src.jarvis import paths

DEFAULT_MODELS = [
    "qwen3-30b-a3b-instruct-2507-bartowski:latest",
    "qwen2.5-coder:32b",
    "exaone3.5:32b",
    "glm-4.7-flash:latest",
]
EVIDENCE_PATH = str(paths.multi_model_measurement_path())


def measure_model(model: str, runs: int, system_prompt: str) -> dict:
    """단일 모델 warmup + measure N → 결과 dict (runs + stats)."""
    if not _ollama_has_model(model):
        return {"model": model, "skipped": True, "reason": "모델 미설치"}

    # warmup
    t0 = time.monotonic()
    _call_ollama(model, system_prompt, ADVICE_USER_BLOB)
    warmup_s = time.monotonic() - t0

    # measure
    metrics: list[dict] = []
    for _ in range(runs):
        payload = _call_ollama(model, system_prompt, ADVICE_USER_BLOB)
        metrics.append(_extract_metrics(payload))

    valid = [m for m in metrics if "error" not in m]
    if not valid:
        return {"model": model, "skipped": True, "reason": "모든 run 실패",
                "runs": metrics}

    return {
        "model": model,
        "warmup_s": warmup_s,
        "runs": metrics,
        "stats": {
            "decode_tok_per_s": _summarize([m["decode_tok_per_s"] for m in valid]),
            "prefill_tok_per_s": _summarize([m["prefill_tok_per_s"] for m in valid]),
            "latency_s": _summarize([m["latency_s"] for m in valid]),
        },
        "n_valid": len(valid),
        "n_total": len(metrics),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Jarvis 다중 모델 N=3 비교")
    ap.add_argument("--models", default=",".join(DEFAULT_MODELS),
                    help="콤마 구분 모델 list")
    ap.add_argument("--runs", type=int, default=3)
    args = ap.parse_args()

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    system_prompt = boss_prompt_for("code")

    print("=== Jarvis (p) 다중 모델 N=3 비교 ===")
    print(f"models : {len(models)}")
    for m in models:
        print(f"  - {m}")
    print(f"runs   : N={args.runs} + warmup 1 per model")
    print()

    results: list[dict] = []
    t_total = time.monotonic()
    for i, model in enumerate(models, 1):
        print(f"[{i}/{len(models)}] {model}")
        t0 = time.monotonic()
        r = measure_model(model, args.runs, system_prompt)
        elapsed = time.monotonic() - t0
        results.append(r)
        if r.get("skipped"):
            print(f"   → SKIP ({r['reason']})")
        else:
            s = r["stats"]
            print(
                f"   → decode mean={s['decode_tok_per_s']['mean']:.2f} tok/s "
                f"prefill mean={s['prefill_tok_per_s']['mean']:.0f} tok/s "
                f"latency mean={s['latency_s']['mean']:.2f}s "
                f"(warmup={r['warmup_s']:.1f}s, elapsed={elapsed:.1f}s)"
            )
    total_elapsed = time.monotonic() - t_total

    # 비교 표 (decode rate 내림차순, valid 만)
    valid_results = [r for r in results if not r.get("skipped")]
    valid_results.sort(
        key=lambda r: -r["stats"]["decode_tok_per_s"]["mean"]
    )

    print("\n=== 비교 표 (decode rate 정렬) ===")
    print(f"{'모델':<48} {'decode (tok/s)':>16} {'prefill':>12} {'latency':>10}")
    print(f"{'':<48} {'mean   p50':>16} {'mean':>12} {'mean':>10}")
    for r in valid_results:
        s = r["stats"]
        d = s["decode_tok_per_s"]
        p = s["prefill_tok_per_s"]
        lat = s["latency_s"]
        print(
            f"{r['model']:<48} "
            f"{d['mean']:6.2f} {d['p50']:6.2f}   "
            f"{p['mean']:8.0f}    "
            f"{lat['mean']:6.2f}"
        )

    # raw JSON evidence
    evidence = {
        "n_runs_per_model": args.runs,
        "models": results,
        "ranking": [r["model"] for r in valid_results],
        "total_elapsed_s": total_elapsed,
    }
    with open(EVIDENCE_PATH, "w", encoding="utf-8") as fh:
        json.dump(evidence, fh, ensure_ascii=False, indent=2)
    print(f"\n[evidence] raw JSON → {EVIDENCE_PATH}")
    print(f"[total elapsed] {total_elapsed:.1f}s")

    # 합격 조건
    checks = {
        "모델 ≥ 2 valid":   len(valid_results) >= 2,
        "각 모델 N runs":    all(r["n_valid"] >= 1 for r in valid_results),
        "decode > 0":       all(r["stats"]["decode_tok_per_s"]["mean"] > 0
                                for r in valid_results),
        "evidence 기록":     os.path.exists(EVIDENCE_PATH),
    }
    print("\n=== 합격 조건 ===")
    for name, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'} : {name}")
    all_pass = all(checks.values())
    print(f"\nMULTI-MODEL-MEASUREMENT DONE: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
