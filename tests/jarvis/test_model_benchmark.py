"""모델 측정 실행 — ollama 벤치마크 → measurement dict(multi 포맷).

답습: docs/phase0/model-measurement-run-feature-brief.md
  - 측정 수행만 신규(저장은 기존 append_measurement 재사용). generate_fn 주입 = hermetic.
  - 출력 dict 는 model_measurement_repo.append_session(kind="multi") 입력과 정확히 일치.
"""
from __future__ import annotations

import pytest

from src.jarvis.model_benchmark import (
    compute_stats,
    metrics_from_response,
    run_benchmark,
)
from src.jarvis.model_measurement_repo import ModelMeasurementRepo


def _resp(eval_count=60, eval_dur_ns=2_000_000_000, peval_count=300,
          peval_dur_ns=500_000_000, total_ns=3_000_000_000, load_ns=100_000_000):
    """ollama /api/generate(stream=false) 응답 메트릭(ns)."""
    return {
        "total_duration": total_ns, "load_duration": load_ns,
        "prompt_eval_count": peval_count, "prompt_eval_duration": peval_dur_ns,
        "eval_count": eval_count, "eval_duration": eval_dur_ns,
    }


# ── metrics_from_response: ollama 메트릭 → run dict 9필드 ───────────────────
def test_metrics_decode_prefill_latency():
    r = metrics_from_response(_resp())
    assert r["eval_count"] == 60
    assert r["eval_duration_ns"] == 2_000_000_000
    assert r["total_duration_ns"] == 3_000_000_000
    assert r["decode_tok_per_s"] == pytest.approx(60 / 2.0)     # 30
    assert r["prefill_tok_per_s"] == pytest.approx(300 / 0.5)   # 600
    assert r["latency_s"] == pytest.approx(3.0)


def test_metrics_zero_duration_safe():
    """eval_duration 0 = 0으로 안전(div-by-zero crash 아님)."""
    r = metrics_from_response(_resp(eval_dur_ns=0, peval_dur_ns=0))
    assert r["decode_tok_per_s"] == 0
    assert r["prefill_tok_per_s"] == 0


def test_metrics_has_all_9_run_fields():
    from src.jarvis.model_measurement_repo import _RUN_FIELDS
    r = metrics_from_response(_resp())
    assert set(_RUN_FIELDS).issubset(r.keys())


# ── compute_stats: runs → {metric: {mean,p50,std,min,max}} ─────────────────
def test_compute_stats_mean_min_max():
    runs = [
        {"decode_tok_per_s": 10, "prefill_tok_per_s": 100, "latency_s": 1.0},
        {"decode_tok_per_s": 20, "prefill_tok_per_s": 200, "latency_s": 2.0},
        {"decode_tok_per_s": 30, "prefill_tok_per_s": 300, "latency_s": 3.0},
    ]
    s = compute_stats(runs)
    assert s["decode_tok_per_s"]["mean"] == pytest.approx(20)
    assert s["decode_tok_per_s"]["min"] == 10
    assert s["decode_tok_per_s"]["max"] == 30
    assert s["decode_tok_per_s"]["p50"] == pytest.approx(20)
    assert s["decode_tok_per_s"]["std"] >= 0


# ── run_benchmark: warmup + n_runs + skipped/error ─────────────────────────
def test_run_benchmark_basic():
    calls = []

    def fake_gen(model, prompt):
        calls.append(model)
        return _resp()

    m = run_benchmark(["a", "b"], prompt="hi", n_runs=3, generate_fn=fake_gen)
    assert m["n_runs_per_model"] == 3
    assert [x["model"] for x in m["models"]] == ["a", "b"]
    m0 = m["models"][0]
    assert m0["n_valid"] == 3 and m0["n_total"] == 3
    assert "warmup_s" in m0
    assert not m0.get("skipped")
    assert m0["stats"]["decode_tok_per_s"]["mean"] == pytest.approx(30)
    assert len(m0["runs"]) == 3
    # warmup(1) + n_runs(3) = 4 호출/모델
    assert calls.count("a") == 4


def test_run_benchmark_all_runs_fail_marks_skipped():
    def boom(model, prompt):
        raise RuntimeError("model not found")

    m = run_benchmark(["x"], prompt="hi", n_runs=2, generate_fn=boom)
    m0 = m["models"][0]
    assert m0["skipped"] is True
    assert m0["reason"]


def test_run_benchmark_partial_failure_keeps_valid():
    seq = {"n": 0}

    def flaky(model, prompt):
        seq["n"] += 1
        if seq["n"] == 3:  # warmup(1)+run1(2) 성공, run2(3) 실패, run3(4) 성공
            raise RuntimeError("timeout")
        return _resp()

    m = run_benchmark(["a"], prompt="hi", n_runs=3, generate_fn=flaky)
    m0 = m["models"][0]
    assert m0["n_valid"] == 2 and m0["n_total"] == 3
    assert not m0.get("skipped")  # 일부 성공 = 측정됨
    assert any("error" in r for r in m0["runs"])


def test_run_benchmark_progress_callback():
    """진행 콜백(모델별) — 라우트가 status 표시에 사용."""
    seen = []
    run_benchmark(["a", "b"], prompt="hi", n_runs=1,
                  generate_fn=lambda mo, p: _resp(),
                  on_progress=lambda done, total, model: seen.append((done, total, model)))
    assert (2, 2, "b") in seen


# ── 라운드트립: 측정 출력 → DB → latest_session 일치 ───────────────────────
def test_benchmark_output_roundtrips_through_db(tmp_path):
    m = run_benchmark(["a"], prompt="hi", n_runs=3, generate_fn=lambda mo, p: _resp())
    repo = ModelMeasurementRepo(tmp_path / "t.db")
    repo.append_session(m, kind="multi")
    latest = repo.latest_session("multi")
    assert latest["models"][0]["model"] == "a"
    assert latest["models"][0]["stats"]["decode_tok_per_s"]["mean"] == pytest.approx(30)
    assert latest["n_runs_per_model"] == 3
