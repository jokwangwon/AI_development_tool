"""ModelMeasurementRepo (SQLite backing) — 통합 데이터 레이어 §10-5a 테스트.

답습: docs/phase0/jarvis-model-measurement-schema-brief.md (v1.1, 3+1 합의 흡수)
  - §3 정규화 3테이블(session+model+run) + flat 15 stats 컬럼 + measurement_run.error(C1).
  - §4 repo port: append_session/latest_session/top_models/model_history/list_sessions/migrate_legacy.
  - §5 RB-1 threading(connection-per-op + WAL) + append 원자성(단일 트랜잭션, C3).
  - §6 마이그레이션 idempotent(source_id=legacy:{kind}:{sha8}, C4) + 원본 보존 + fail-soft.
  - §7 5a 수용기준 ①~⑥: 라운드트립 / skipped 2변종 / 전부 skipped→[] / 순서·skipped 보존
    / migrate idempotency / 신규 DB 0600.
"""
from __future__ import annotations

import json
import os
import stat

import pytest

from src.jarvis import paths
from src.jarvis.model_measurement_repo import ModelMeasurementRepo, append_measurement


# --- 샘플 데이터 빌더 (실측 형태 §2 모사) ---
def _run(seed: int) -> dict:
    """정상 per-run 9필드(실측 형태). error 키 없음."""
    return {
        "total_duration_ns": 1000 + seed,
        "load_duration_ns": 100 + seed,
        "prompt_eval_count": 369,
        "prompt_eval_duration_ns": 400 + seed,
        "eval_count": 60 + seed,
        "eval_duration_ns": 900 + seed,
        "decode_tok_per_s": 2.5 + seed,
        "prefill_tok_per_s": 800.0 + seed,
        "latency_s": 25.0 + seed,
    }


def _stats(base: float) -> dict:
    def s(x):
        return {"mean": x, "p50": x, "std": 0.1, "min": x - 1, "max": x + 1}
    return {
        "decode_tok_per_s": s(base),
        "prefill_tok_per_s": s(base * 100),
        "latency_s": s(base * 10),
    }


def _multi_measurement() -> dict:
    """multi-model: 정상 1 + skipped 미설치 + skipped 전run실패(error runs)."""
    return {
        "n_runs_per_model": 2,
        "models": [
            {
                "model": "m1",
                "warmup_s": 1.5,
                "runs": [_run(1), _run(2)],
                "stats": _stats(9.0),
                "n_valid": 2,
                "n_total": 2,
            },
            {"model": "m2", "skipped": True, "reason": "모델 미설치"},
            {
                "model": "m3",
                "skipped": True,
                "reason": "모든 run 실패",
                "runs": [{"error": "boom1"}, {"error": "boom2"}],
            },
        ],
        "ranking": ["m1"],
        "total_elapsed_s": 123.4,
    }


def _boss_measurement() -> dict:
    """boss: 단일 모델 래퍼(warmup_s/ranking/n_runs_per_model/total_elapsed_s 없음)."""
    return {
        "model": "boss1",
        "runs": [_run(3), _run(4)],
        "stats": _stats(15.0),
        "n_valid": 2,
        "n_total": 2,
    }


# --- ① 라운드트립 동등성 (C2) ---
def test_multi_roundtrip_exact(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    original = _multi_measurement()
    repo.append_session(original, kind="multi")
    assert repo.latest_session("multi") == original


def test_boss_roundtrip_exact(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    original = _boss_measurement()
    repo.append_session(original, kind="boss")
    got = repo.latest_session("boss")
    assert got == original
    # boss 재구성은 multi 전용 키를 끼우지 않음 (C2)
    assert "n_runs_per_model" not in got
    assert "ranking" not in got
    assert "warmup_s" not in got


def test_latest_session_none_when_empty(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    assert repo.latest_session("multi") is None
    assert repo.latest_session("boss") is None


def test_latest_session_returns_most_recent(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    older = _boss_measurement()
    newer = _boss_measurement()
    newer["model"] = "boss2"
    repo.append_session(older, kind="boss", measured_ts=100.0)
    repo.append_session(newer, kind="boss", measured_ts=200.0)
    assert repo.latest_session("boss")["model"] == "boss2"


# --- ② skipped 2변종 (C1) ---
def test_skipped_variants_roundtrip(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    m = _multi_measurement()
    repo.append_session(m, kind="multi")
    models = repo.latest_session("multi")["models"]
    # 미설치: runs 키 없음
    assert models[1] == {"model": "m2", "skipped": True, "reason": "모델 미설치"}
    # 전run실패: error runs 보존
    assert models[2] == {
        "model": "m3",
        "skipped": True,
        "reason": "모든 run 실패",
        "runs": [{"error": "boom1"}, {"error": "boom2"}],
    }


# --- ③ 전부 skipped → top_models [] (B-R3) ---
def test_top_models_all_skipped_returns_empty(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(
        {
            "n_runs_per_model": 1,
            "models": [
                {"model": "a", "skipped": True, "reason": "x"},
                {"model": "b", "skipped": True, "reason": "y"},
            ],
            "ranking": [],
            "total_elapsed_s": 1.0,
        },
        kind="multi",
    )
    assert repo.top_models() == []


def test_top_models_none_when_no_session(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    assert repo.top_models() == []


def test_top_models_orders_by_decode_desc_skips_skipped(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(
        {
            "n_runs_per_model": 1,
            "models": [
                {"model": "slow", "warmup_s": 1.0, "runs": [_run(1)],
                 "stats": _stats(3.0), "n_valid": 1, "n_total": 1},
                {"model": "fast", "warmup_s": 1.0, "runs": [_run(1)],
                 "stats": _stats(9.0), "n_valid": 1, "n_total": 1},
                {"model": "skip", "skipped": True, "reason": "z"},
            ],
            "ranking": ["fast", "slow"],
            "total_elapsed_s": 1.0,
        },
        kind="multi",
    )
    top = repo.top_models(limit=3)
    assert [t["model"] for t in top] == ["fast", "slow"]
    assert top[0]["mean"] == 9.0


def test_top_models_metric_whitelist_rejects_unknown(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(_multi_measurement(), kind="multi")
    with pytest.raises(ValueError):
        repo.top_models(metric="decode_mean; DROP TABLE measurement_run")


# --- ④ models[] 순서 + skipped 포함 보존 (C8) ---
def test_models_order_and_skipped_preserved(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(_multi_measurement(), kind="multi")
    models = repo.latest_session("multi")["models"]
    assert [m["model"] for m in models] == ["m1", "m2", "m3"]  # 입력 순서
    assert [bool(m.get("skipped")) for m in models] == [False, True, True]


# --- ⑤ migrate idempotency + 원본 보존 (C3/C4/§6) ---
def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def test_migrate_legacy_imports_both(tmp_path):
    multi_p = tmp_path / "multi.json"
    boss_p = tmp_path / "boss.json"
    _write_json(multi_p, _multi_measurement())
    _write_json(boss_p, _boss_measurement())
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    report = repo.migrate_legacy(multi_path=str(multi_p), boss_path=str(boss_p))
    assert report["imported"] == 2
    assert repo.latest_session("multi") == _multi_measurement()
    assert repo.latest_session("boss") == _boss_measurement()


def test_migrate_legacy_idempotent(tmp_path):
    multi_p = tmp_path / "multi.json"
    _write_json(multi_p, _multi_measurement())
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    r1 = repo.migrate_legacy(multi_path=str(multi_p), boss_path=None)
    r2 = repo.migrate_legacy(multi_path=str(multi_p), boss_path=None)
    assert r1["imported"] == 1
    assert r2["imported"] == 0
    assert r2["skipped_existing"] == 1
    # 2회 호출에도 세션 1개만
    assert len(repo.list_sessions(kind="multi")) == 1


def test_migrate_legacy_preserves_original(tmp_path):
    multi_p = tmp_path / "multi.json"
    _write_json(multi_p, _multi_measurement())
    before = multi_p.read_bytes()
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.migrate_legacy(multi_path=str(multi_p), boss_path=None)
    assert multi_p.read_bytes() == before  # 원본 보존(롤백 가능)


def test_migrate_legacy_fail_soft_missing_file(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    report = repo.migrate_legacy(
        multi_path=str(tmp_path / "nope.json"), boss_path=None
    )
    assert report["imported"] == 0
    assert report["errors"] == []


def test_migrate_legacy_corrupt_json_reported(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{ not json", encoding="utf-8")
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    report = repo.migrate_legacy(multi_path=str(bad), boss_path=None)
    assert report["imported"] == 0
    assert len(report["errors"]) == 1


def test_constructor_legacy_option_migrates(tmp_path):
    multi_p = tmp_path / "multi.json"
    _write_json(multi_p, _multi_measurement())
    repo = ModelMeasurementRepo(tmp_path / "m.db", legacy_multi=str(multi_p))
    assert repo.latest_session("multi") == _multi_measurement()


def test_migrate_uses_file_mtime_as_measured_ts(tmp_path):
    multi_p = tmp_path / "multi.json"
    _write_json(multi_p, _multi_measurement())
    os.utime(multi_p, (500.0, 500.0))
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.migrate_legacy(multi_path=str(multi_p), boss_path=None)
    sess = repo.list_sessions(kind="multi")[0]
    assert sess["measured_ts"] == 500.0


# --- ⑥ 신규 DB 0600 (B) ---
def test_new_db_file_is_0600(tmp_path):
    db = tmp_path / "m.db"
    ModelMeasurementRepo(db)
    mode = stat.S_IMODE(os.stat(db).st_mode)
    assert mode == 0o600


# --- append 원자성 (C3): 잘못된 run → 세션 미적재(롤백) ---
def test_append_atomic_rollback_on_bad_run(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    with pytest.raises(Exception):
        repo.append_session(
            {"n_runs_per_model": 1, "models": [{"model": "x", "runs": ["not-a-dict"]}],
             "ranking": [], "total_elapsed_s": 1.0},
            kind="multi",
        )
    assert repo.latest_session("multi") is None  # 부분 세션 없음


# --- live append (source_id=None) = 매번 새 세션 (C5 append-only) ---
def test_live_append_creates_new_session_each_time(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(_boss_measurement(), kind="boss")
    repo.append_session(_boss_measurement(), kind="boss")
    assert len(repo.list_sessions(kind="boss")) == 2  # NULL source_id 무한 append


# --- model_history (추세 + 다중 모델 비교, C 대안4) ---
def test_model_history_trend_ascending(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    for ts, base in [(100.0, 3.0), (200.0, 9.0)]:
        repo.append_session(
            {"n_runs_per_model": 1,
             "models": [{"model": "m1", "warmup_s": 1.0, "runs": [_run(1)],
                         "stats": _stats(base), "n_valid": 1, "n_total": 1}],
             "ranking": ["m1"], "total_elapsed_s": 1.0},
            kind="multi", measured_ts=ts,
        )
    hist = repo.model_history(models=["m1"])
    assert [h["measured_ts"] for h in hist] == [100.0, 200.0]  # ASC
    assert [h["mean"] for h in hist] == [3.0, 9.0]


def test_model_history_all_models_when_none(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(_multi_measurement(), kind="multi")
    hist = repo.model_history()  # models=None → 전체(skipped 제외)
    assert {h["model"] for h in hist} == {"m1"}  # m2/m3 skipped 제외


# --- list_sessions ---
def test_list_sessions_desc_by_measured_ts(tmp_path):
    repo = ModelMeasurementRepo(tmp_path / "m.db")
    repo.append_session(_boss_measurement(), kind="boss", measured_ts=100.0)
    repo.append_session(_multi_measurement(), kind="multi", measured_ts=200.0)
    sessions = repo.list_sessions()
    assert [s["measured_ts"] for s in sessions] == [200.0, 100.0]  # DESC
    assert {s["kind"] for s in sessions} == {"boss", "multi"}
    by_kind = {s["kind"]: s["n_models"] for s in sessions}
    assert by_kind == {"multi": 3, "boss": 1}  # n_models (skipped 포함)


# --- §10-5b-writer: append_measurement (기본 DB 경로, 히스토리 누적) ---
def test_append_measurement_default_path_roundtrip(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path))
    sid = append_measurement(_boss_measurement(), kind="boss")
    assert isinstance(sid, int)
    repo = ModelMeasurementRepo(paths.measurement_db_path())
    assert repo.latest_session("boss") == _boss_measurement()


def test_append_measurement_accrues_history(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path))
    append_measurement(_multi_measurement(), kind="multi")
    append_measurement(_multi_measurement(), kind="multi")
    repo = ModelMeasurementRepo(paths.measurement_db_path())
    assert len(repo.list_sessions(kind="multi")) == 2  # append-only 히스토리
