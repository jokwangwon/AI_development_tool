"""모델 측정 실행 — ollama 벤치마크 → measurement dict(multi 포맷).

답습: docs/phase0/model-measurement-run-feature-brief.md

설계:
  - 측정 *수행*만 신규(저장은 기존 model_measurement_repo.append_measurement 재사용).
    모달 5/29 고정의 뿌리 = 측정 수행 도구 부재 → 본 모듈이 그 조각.
  - 각 모델 = warmup 1회(콜드 로드 시간) + n_runs회 generate(고정 프롬프트). ollama
    /api/generate(stream=false) 응답 메트릭(ns) → decode/prefill tok/s · latency 계산.
  - 출력 dict 는 append_session(kind="multi") 입력과 정확히 일치(_RUN_FIELDS·_STATS_KEYS).
  - **generate_fn 주입** = hermetic 테스트 seam(실 ollama 없이 메트릭 계산 검증). 기본 =
    ollama HTTP. 모델 로드 실패/타임아웃 = error run/skipped(fail-soft, 기존 2변종 재사용).

이 모듈은 **leaf**(부작용 = 주입형 generate_fn). 시간 측정만 time 사용.
"""
from __future__ import annotations

import json
import statistics
import time
import urllib.request
from typing import Callable, Optional

# 통계 대상 3 메트릭(repo _STATS_KEYS 와 동일 키).
_STAT_METRICS = ("decode_tok_per_s", "prefill_tok_per_s", "latency_s")

# 기본 측정 프롬프트(고정 — decode tok/s 는 생성 속도라 내용 무관, 비교 일관성용).
DEFAULT_PROMPT = (
    "Explain in a few sentences how a hash map achieves average O(1) lookup, "
    "and mention one common collision-handling strategy."
)
DEFAULT_OLLAMA_URL = "http://localhost:11434"


def metrics_from_response(resp: dict) -> dict:
    """ollama /api/generate 응답 메트릭 → run dict 9필드. duration 0 = 0(div 안전)."""
    eval_count = int(resp.get("eval_count") or 0)
    eval_dur_ns = int(resp.get("eval_duration") or 0)
    peval_count = int(resp.get("prompt_eval_count") or 0)
    peval_dur_ns = int(resp.get("prompt_eval_duration") or 0)
    total_ns = int(resp.get("total_duration") or 0)
    load_ns = int(resp.get("load_duration") or 0)

    decode = eval_count / (eval_dur_ns / 1e9) if eval_dur_ns > 0 else 0
    prefill = peval_count / (peval_dur_ns / 1e9) if peval_dur_ns > 0 else 0
    return {
        "total_duration_ns": total_ns,
        "load_duration_ns": load_ns,
        "prompt_eval_count": peval_count,
        "prompt_eval_duration_ns": peval_dur_ns,
        "eval_count": eval_count,
        "eval_duration_ns": eval_dur_ns,
        "decode_tok_per_s": decode,
        "prefill_tok_per_s": prefill,
        "latency_s": total_ns / 1e9 if total_ns > 0 else 0,
    }


def compute_stats(runs: list) -> dict:
    """정상 run 들 → {metric: {mean,p50,std,min,max}}. repo _STATS_KEYS/_STAT_FIELDS 일치."""
    out: dict = {}
    for metric in _STAT_METRICS:
        vals = [float(r[metric]) for r in runs if metric in r and "error" not in r]
        if not vals:
            out[metric] = {"mean": 0, "p50": 0, "std": 0, "min": 0, "max": 0}
            continue
        out[metric] = {
            "mean": statistics.fmean(vals),
            "p50": statistics.median(vals),
            "std": statistics.pstdev(vals) if len(vals) > 1 else 0.0,
            "min": min(vals),
            "max": max(vals),
        }
    return out


def _ollama_generate(model: str, prompt: str, *, url: str = DEFAULT_OLLAMA_URL,
                     timeout: float = 600.0) -> dict:
    """기본 generate_fn — ollama /api/generate(stream=false). 메트릭 dict 반환."""
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(
        f"{url}/api/generate", data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (localhost ollama)
        return json.loads(resp.read().decode())


def run_benchmark(
    model_names: list,
    *,
    prompt: str = DEFAULT_PROMPT,
    n_runs: int = 3,
    generate_fn: Optional[Callable[[str, str], dict]] = None,
    on_progress: Optional[Callable[[int, int, str], None]] = None,
) -> dict:
    """모델별 warmup + n_runs 벤치 → measurement dict(multi 포맷, append_session 호환).

    generate_fn(model, prompt) -> ollama 메트릭 dict. 미주입 = 실 ollama HTTP.
    on_progress(done, total, model) = 모델 완료 시 콜백(라우트 진행 표시용).
    """
    gen = generate_fn if generate_fn is not None else _ollama_generate
    total = len(model_names)
    t_start = time.monotonic()
    models = []
    for done, name in enumerate(model_names, start=1):
        models.append(_benchmark_one(name, prompt, n_runs, gen))
        if on_progress is not None:
            on_progress(done, total, name)
    return {
        "n_runs_per_model": n_runs,
        "total_elapsed_s": time.monotonic() - t_start,
        "models": models,
    }


def _benchmark_one(name: str, prompt: str, n_runs: int, gen: Callable) -> dict:
    # warmup(콜드 로드 시간 측정) — 실패해도 본 run 시도(로드 자체가 본 run 에서 재시도됨)
    t0 = time.monotonic()
    try:
        gen(name, prompt)
    except Exception:
        pass
    warmup_s = time.monotonic() - t0

    runs = []
    for _i in range(n_runs):
        try:
            runs.append(metrics_from_response(gen(name, prompt)))
        except Exception as exc:  # 타임아웃/미설치 = error run(fail-soft)
            runs.append({"error": str(exc)})

    valid = [r for r in runs if "error" not in r]
    if not valid:
        return {
            "model": name, "warmup_s": warmup_s, "skipped": True,
            "reason": "all runs failed", "n_valid": 0, "n_total": n_runs, "runs": runs,
        }
    return {
        "model": name, "warmup_s": warmup_s,
        "n_valid": len(valid), "n_total": n_runs,
        "stats": compute_stats(valid), "runs": runs,
    }
