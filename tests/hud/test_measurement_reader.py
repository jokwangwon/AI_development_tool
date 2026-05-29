"""측정 reader 동작 불변 검증 — §10-5b-reader (ModelMeasurementRepo 경유).

답습: docs/phase0/jarvis-model-measurement-schema-brief.md §7 (5b-reader).
  server.get_top_measured_models 가 JSON 직접 스캔 → repo.top_models 경유로 전환되어도
  반환 shape([{"model","decode"}])·랭킹(skipped 제외, decode_mean DESC)·빈 케이스 불변.
  writer 가 아직 JSON 을 쓰는 단계 → open_reader_repo 가 JSON 을 idempotent 마이그레이션 후 읽음.
"""
from __future__ import annotations

import asyncio
import json
import os
import tempfile

os.environ.setdefault("JARVIS_DATA_DIR", tempfile.mkdtemp(prefix="jarvis-meas-reader-"))

from jarvis_hud import server  # noqa: E402
from src.jarvis import paths  # noqa: E402


def _stats(mean: float) -> dict:
    def s(x):
        return {"mean": x, "p50": x, "std": 0.0, "min": x, "max": x}
    return {
        "decode_tok_per_s": s(mean),
        "prefill_tok_per_s": s(mean * 100),
        "latency_s": s(mean * 10),
    }


def _write_multi(models, ranking):
    with open(paths.multi_model_measurement_path(), "w", encoding="utf-8") as f:
        json.dump(
            {"n_runs_per_model": 1, "models": models, "ranking": ranking, "total_elapsed_s": 1.0},
            f, ensure_ascii=False,
        )


def test_get_top_measured_models_ranks_via_repo(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path))
    _write_multi(
        [
            {"model": "slow:1", "warmup_s": 1.0, "runs": [], "stats": _stats(3.0),
             "n_valid": 1, "n_total": 1},
            {"model": "fast:1", "warmup_s": 1.0, "runs": [], "stats": _stats(9.0),
             "n_valid": 1, "n_total": 1},
            {"model": "skip:1", "skipped": True, "reason": "미설치"},
        ],
        ["fast:1", "slow:1"],
    )
    out = asyncio.run(server.get_top_measured_models(limit=3))
    # skipped 제외 + decode_mean DESC (동작 불변)
    assert [m["model"] for m in out] == ["fast:1", "slow:1"]
    assert out[0]["decode"] == 9.0
    # 반환 shape 불변: {"model","decode"}
    assert set(out[0].keys()) == {"model", "decode"}


def test_get_top_measured_models_limit(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path))
    _write_multi(
        [
            {"model": f"m{i}", "warmup_s": 1.0, "runs": [], "stats": _stats(float(i)),
             "n_valid": 1, "n_total": 1}
            for i in range(5)
        ],
        [f"m{i}" for i in range(5)],
    )
    out = asyncio.run(server.get_top_measured_models(limit=2))
    assert len(out) == 2
    assert [m["model"] for m in out] == ["m4", "m3"]  # 상위 2


def test_get_top_measured_models_empty_when_no_file(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path))
    assert asyncio.run(server.get_top_measured_models()) == []


def test_get_top_measured_models_empty_when_all_skipped(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path))
    _write_multi(
        [{"model": "a", "skipped": True, "reason": "x"},
         {"model": "b", "skipped": True, "reason": "y"}],
        [],
    )
    assert asyncio.run(server.get_top_measured_models()) == []
