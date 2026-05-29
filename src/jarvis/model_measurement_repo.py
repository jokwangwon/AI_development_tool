"""ModelMeasurementRepo (SQLite backing, 모델 측정 히스토리) — 통합 데이터 레이어 §10-5a.

답습: docs/phase0/jarvis-model-measurement-schema-brief.md (v1.1, 3+1 합의 흡수)
  - §1 D1/D2/D3: append-only 히스토리 + 정규화 3테이블(session+model+run) + boss·multi 통합(kind).
  - §3 스키마: flat 15 stats 컬럼 + measurement_run.error(C1) + UNIQUE/CHECK 제약.
  - §4 port: append_session/latest_session/top_models/model_history/list_sessions/migrate_legacy.
    kind 분기는 dict↔row 매퍼 1곳에 격리(C 리스크3).
  - §5 RB-1: connection-per-operation + WAL + busy_timeout + short transaction. pool 금지.
    append_session = 단일 트랜잭션(원자성, C3).
  - §6 RB-3: 마이그레이션 무손실·idempotent — source_id=legacy:{kind}:{sha8}(C4) + 세션 존재
    확인 후 child skip(C3) + 원본 보존(롤백) + fail-soft + 손상 JSON report. measured_ts=mtime(추정치, C6).
  - §7 5a: 신규 DB·WAL sidecar 0600(B) — paths.data_file 이 기존 파일만 chmod 하는 결함 보완.

§10-5a = 동작 불변 + 신규 capability(repo 단독 추가, reader/writer 미변경). stdlib only.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import time
from contextlib import closing
from pathlib import Path

_BUSY_TIMEOUT_MS = 5000
_FILE_MODE = 0o600

# metric 화이트리스트(C7) — 외부 metric 이름 → flat 컬럼 prefix. SQL injection/오타 방지.
_METRIC_COLUMN = {"decode": "decode", "prefill": "prefill", "latency": "latency"}
# stats nested 키 ↔ flat 컬럼 prefix
_STATS_KEYS = (("decode", "decode_tok_per_s"), ("prefill", "prefill_tok_per_s"),
               ("latency", "latency_s"))
_STAT_FIELDS = ("mean", "p50", "std", "min", "max")
# per-run 9 메트릭 필드(정상 run). error run 은 {"error": ...} 단일 키.
_RUN_FIELDS = (
    "total_duration_ns", "load_duration_ns", "prompt_eval_count",
    "prompt_eval_duration_ns", "eval_count", "eval_duration_ns",
    "decode_tok_per_s", "prefill_tok_per_s", "latency_s",
)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS measurement_session (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id        TEXT,
    kind             TEXT NOT NULL CHECK (kind IN ('boss','multi')),
    measured_ts      REAL NOT NULL,
    n_runs_per_model INTEGER,
    total_elapsed_s  REAL,
    ranking_json     TEXT,
    created_ts       REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS measurement_model (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id   INTEGER NOT NULL,
    model        TEXT NOT NULL,
    warmup_s     REAL,
    skipped      INTEGER NOT NULL DEFAULT 0 CHECK (skipped IN (0,1)),
    reason       TEXT,
    n_valid      INTEGER,
    n_total      INTEGER,
    decode_mean REAL,  decode_p50 REAL,  decode_std REAL,  decode_min REAL,  decode_max REAL,
    prefill_mean REAL, prefill_p50 REAL, prefill_std REAL, prefill_min REAL, prefill_max REAL,
    latency_mean REAL, latency_p50 REAL, latency_std REAL, latency_min REAL, latency_max REAL,
    UNIQUE (session_id, model)
);
CREATE TABLE IF NOT EXISTS measurement_run (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id                INTEGER NOT NULL,
    run_idx                 INTEGER NOT NULL,
    error                   TEXT,
    total_duration_ns       INTEGER,
    load_duration_ns        INTEGER,
    prompt_eval_count       INTEGER,
    prompt_eval_duration_ns INTEGER,
    eval_count              INTEGER,
    eval_duration_ns        INTEGER,
    decode_tok_per_s        REAL,
    prefill_tok_per_s       REAL,
    latency_s               REAL,
    UNIQUE (model_id, run_idx)
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_session_source_id
    ON measurement_session(source_id) WHERE source_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_model_session ON measurement_model(session_id);
CREATE INDEX IF NOT EXISTS idx_model_model   ON measurement_model(model);
CREATE INDEX IF NOT EXISTS idx_run_model     ON measurement_run(model_id);
CREATE INDEX IF NOT EXISTS idx_session_kind_ts ON measurement_session(kind, measured_ts);
"""


class ModelMeasurementRepo:
    def __init__(
        self,
        path: str | Path,
        *,
        legacy_multi: str | Path | None = None,
        legacy_boss: str | Path | None = None,
    ) -> None:
        self._path = str(path)
        self._ensure_schema()
        self._chmod()  # 신규 DB·WAL sidecar 0600 (B)
        if legacy_multi is not None or legacy_boss is not None:
            try:  # 생성자 옵션 마이그레이션 = fail-soft (Q5-d)
                self.migrate_legacy(multi_path=legacy_multi, boss_path=legacy_boss)
            except Exception:
                pass

    @property
    def path(self) -> str:
        return self._path

    def _connect(self) -> sqlite3.Connection:
        # connection-per-operation (RB-1): 호출마다 새 connection, short transaction.
        conn = sqlite3.connect(self._path, timeout=_BUSY_TIMEOUT_MS / 1000)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute(f"PRAGMA busy_timeout={_BUSY_TIMEOUT_MS}")
        return conn

    def _ensure_schema(self) -> None:
        with closing(self._connect()) as conn, conn:
            conn.executescript(_SCHEMA)

    def _chmod(self) -> None:
        # 신규 DB 는 sqlite3.connect 가 umask(통상 0644)로 생성 → 명시 0600.
        # paths.data_file 은 기존 파일만 chmod 하므로 신규 DB·WAL sidecar(-wal/-shm) 누락(B).
        for suffix in ("", "-wal", "-shm"):
            p = Path(self._path + suffix)
            if p.is_file():
                try:
                    os.chmod(p, _FILE_MODE)
                except OSError:
                    pass

    # --- 내부 매퍼 (kind 분기 격리) ---
    @staticmethod
    def _stats_columns(stats: dict | None) -> dict:
        """nested stats → flat 15 컬럼 값."""
        out: dict = {}
        for prefix, key in _STATS_KEYS:
            s = (stats or {}).get(key) or {}
            for field in _STAT_FIELDS:
                out[f"{prefix}_{field}"] = s.get(field)
        return out

    @staticmethod
    def _stats_from_row(row: dict) -> dict:
        """flat 15 컬럼 → nested stats(원본 형태)."""
        return {
            key: {field: row[f"{prefix}_{field}"] for field in _STAT_FIELDS}
            for prefix, key in _STATS_KEYS
        }

    def _insert_model(self, conn: sqlite3.Connection, session_id: int, m: dict) -> None:
        """모델 1건 + per-run 적재. skipped 2변종(미설치=runs키없음 / 전run실패=error runs) 처리(C1)."""
        skipped = 1 if m.get("skipped") else 0
        cols = self._stats_columns(m.get("stats"))
        cur = conn.execute(
            "INSERT INTO measurement_model("
            "session_id, model, warmup_s, skipped, reason, n_valid, n_total, "
            "decode_mean, decode_p50, decode_std, decode_min, decode_max, "
            "prefill_mean, prefill_p50, prefill_std, prefill_min, prefill_max, "
            "latency_mean, latency_p50, latency_std, latency_min, latency_max) "
            "VALUES(?,?,?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?)",
            (
                session_id, m["model"], m.get("warmup_s"), skipped, m.get("reason"),
                m.get("n_valid"), m.get("n_total"),
                cols["decode_mean"], cols["decode_p50"], cols["decode_std"],
                cols["decode_min"], cols["decode_max"],
                cols["prefill_mean"], cols["prefill_p50"], cols["prefill_std"],
                cols["prefill_min"], cols["prefill_max"],
                cols["latency_mean"], cols["latency_p50"], cols["latency_std"],
                cols["latency_min"], cols["latency_max"],
            ),
        )
        model_id = cur.lastrowid
        for idx, run in enumerate(m.get("runs", [])):
            if "error" in run:  # error run (전run실패 변종)
                conn.execute(
                    "INSERT INTO measurement_run(model_id, run_idx, error) VALUES(?,?,?)",
                    (model_id, idx, run["error"]),
                )
            else:  # 정상 run 9필드
                conn.execute(
                    "INSERT INTO measurement_run(model_id, run_idx, " + ",".join(_RUN_FIELDS) + ") "
                    "VALUES(?,?," + ",".join("?" * len(_RUN_FIELDS)) + ")",
                    (model_id, idx, *[run.get(f) for f in _RUN_FIELDS]),
                )

    # --- writer ---
    def append_session(
        self,
        measurement: dict,
        *,
        kind: str,
        source_id: str | None = None,
        measured_ts: float | None = None,
    ) -> int:
        """측정 dict 를 3테이블로 분해 적재(단일 트랜잭션, C3). session_id 반환.

        source_id 가 주어지고 이미 존재하면 child 적재 없이 기존 id 반환(idempotent).
        source_id=None(live writer) = 매번 새 세션(append-only, C5).
        """
        if kind not in ("boss", "multi"):
            raise ValueError(f"unknown kind: {kind}")
        now = time.time()
        ts = measured_ts if measured_ts is not None else now
        with closing(self._connect()) as conn, conn:
            if source_id is not None:
                row = conn.execute(
                    "SELECT id FROM measurement_session WHERE source_id = ?", (source_id,)
                ).fetchone()
                if row is not None:
                    return int(row[0])  # 기존 세션 → child skip(원자성)
            if kind == "multi":
                n_runs = measurement.get("n_runs_per_model")
                total_elapsed = measurement.get("total_elapsed_s")
                ranking_json = (
                    json.dumps(measurement["ranking"]) if "ranking" in measurement else None
                )
                models = measurement.get("models", [])
            else:  # boss = 단일 모델 래퍼
                n_runs = None
                total_elapsed = None
                ranking_json = None
                models = [measurement]  # 래퍼 자체가 모델
            cur = conn.execute(
                "INSERT INTO measurement_session("
                "source_id, kind, measured_ts, n_runs_per_model, total_elapsed_s, "
                "ranking_json, created_ts) VALUES(?,?,?,?,?,?,?)",
                (source_id, kind, ts, n_runs, total_elapsed, ranking_json, now),
            )
            session_id = int(cur.lastrowid)
            for m in models:
                self._insert_model(conn, session_id, m)
            return session_id

    # --- reader (동작 불변 재구성) ---
    def latest_session(self, kind: str) -> dict | None:
        """최신(measured_ts DESC) 세션을 현 JSON 형태로 재구성(C2 — kind별 원본 키 정확)."""
        with closing(self._connect()) as conn:
            conn.row_factory = sqlite3.Row
            srow = conn.execute(
                "SELECT * FROM measurement_session WHERE kind = ? "
                "ORDER BY measured_ts DESC, id DESC LIMIT 1",
                (kind,),
            ).fetchone()
            if srow is None:
                return None
            mrows = conn.execute(
                "SELECT * FROM measurement_model WHERE session_id = ? ORDER BY id",
                (srow["id"],),
            ).fetchall()
            model_dicts = []
            for mrow in mrows:
                runs = conn.execute(
                    "SELECT * FROM measurement_run WHERE model_id = ? ORDER BY run_idx",
                    (mrow["id"],),
                ).fetchall()
                model_dicts.append((mrow, runs))
        if kind == "boss":
            mrow, runs = model_dicts[0]
            return {
                "model": mrow["model"],
                "runs": [self._run_to_dict(r) for r in runs],
                "stats": self._stats_from_row(mrow),
                "n_valid": mrow["n_valid"],
                "n_total": mrow["n_total"],
            }
        # multi
        out = {"n_runs_per_model": srow["n_runs_per_model"]}
        out["models"] = [self._model_to_dict(m, runs) for m, runs in model_dicts]
        out["ranking"] = json.loads(srow["ranking_json"]) if srow["ranking_json"] is not None else None
        out["total_elapsed_s"] = srow["total_elapsed_s"]
        return out

    @staticmethod
    def _run_to_dict(r: sqlite3.Row) -> dict:
        if r["error"] is not None:
            return {"error": r["error"]}
        return {f: r[f] for f in _RUN_FIELDS}

    def _model_to_dict(self, m: sqlite3.Row, runs: list) -> dict:
        """multi per-model 재구성. skipped 2변종(C1) + 정상 모델 키 집합 정확."""
        if m["skipped"]:
            d = {"model": m["model"], "skipped": True, "reason": m["reason"]}
            if runs:  # 전run실패 변종 = error runs 보존
                d["runs"] = [self._run_to_dict(r) for r in runs]
            return d
        d = {"model": m["model"]}
        if m["warmup_s"] is not None:
            d["warmup_s"] = m["warmup_s"]
        d["runs"] = [self._run_to_dict(r) for r in runs]
        d["stats"] = self._stats_from_row(m)
        d["n_valid"] = m["n_valid"]
        d["n_total"] = m["n_total"]
        return d

    def top_models(self, *, kind: str = "multi", limit: int = 3, metric: str = "decode") -> list[dict]:
        """최신 세션 1건 내 skipped 제외 {metric}_mean DESC top-N. metric 화이트리스트(C7)."""
        prefix = _METRIC_COLUMN.get(metric)
        if prefix is None:
            raise ValueError(f"unknown metric: {metric}")
        col = f"{prefix}_mean"
        with closing(self._connect()) as conn:
            srow = conn.execute(
                "SELECT id FROM measurement_session WHERE kind = ? "
                "ORDER BY measured_ts DESC, id DESC LIMIT 1",
                (kind,),
            ).fetchone()
            if srow is None:
                return []
            rows = conn.execute(
                f"SELECT model, {col} FROM measurement_model "
                f"WHERE session_id = ? AND skipped = 0 AND {col} IS NOT NULL "
                f"ORDER BY {col} DESC LIMIT ?",
                (srow[0], limit),
            ).fetchall()
        return [{"model": r[0], "mean": r[1]} for r in rows]

    def model_history(self, *, models: list[str] | None = None, metric: str = "decode") -> list[dict]:
        """모델별 추세(measured_ts ASC) + 다중 모델 비교(C 대안4). skipped 제외."""
        prefix = _METRIC_COLUMN.get(metric)
        if prefix is None:
            raise ValueError(f"unknown metric: {metric}")
        col = f"{prefix}_mean"
        sql = (
            f"SELECT mm.model, ms.measured_ts, mm.{col} FROM measurement_model mm "
            "JOIN measurement_session ms ON mm.session_id = ms.id "
            f"WHERE mm.skipped = 0 AND mm.{col} IS NOT NULL"
        )
        params: list = []
        if models is not None:
            sql += " AND mm.model IN (" + ",".join("?" * len(models)) + ")"
            params.extend(models)
        sql += " ORDER BY ms.measured_ts ASC, mm.model ASC"
        with closing(self._connect()) as conn:
            rows = conn.execute(sql, params).fetchall()
        return [{"model": r[0], "measured_ts": r[1], "mean": r[2]} for r in rows]

    def list_sessions(self, *, kind: str | None = None, limit: int = 50) -> list[dict]:
        """세션 목록(measured_ts DESC)."""
        sql = "SELECT id, kind, measured_ts, created_ts FROM measurement_session"
        params: list = []
        if kind is not None:
            sql += " WHERE kind = ?"
            params.append(kind)
        sql += " ORDER BY measured_ts DESC, id DESC LIMIT ?"
        params.append(limit)
        with closing(self._connect()) as conn:
            rows = conn.execute(sql, params).fetchall()
        return [
            {"id": r[0], "kind": r[1], "measured_ts": r[2], "created_ts": r[3]} for r in rows
        ]

    # --- 마이그레이션 (RB-3, §6) ---
    def _session_exists(self, source_id: str) -> bool:
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT 1 FROM measurement_session WHERE source_id = ?", (source_id,)
            ).fetchone()
        return row is not None

    def migrate_legacy(
        self,
        *,
        multi_path: str | Path | None,
        boss_path: str | Path | None,
    ) -> dict:
        """기존 스냅샷 JSON → DB 1회 import. idempotent + 원본 보존 + fail-soft + 손상 report."""
        report = {"imported": 0, "skipped_existing": 0, "errors": []}
        for path, kind in ((multi_path, "multi"), (boss_path, "boss")):
            if path is None:
                continue
            path = str(path)
            if not os.path.exists(path):
                continue
            try:
                raw = Path(path).read_bytes()
                sha = hashlib.sha256(raw).hexdigest()[:8]
                source_id = f"legacy:{kind}:{sha}"  # kind 포함(C4)
                if self._session_exists(source_id):
                    report["skipped_existing"] += 1
                    continue
                data = json.loads(raw)
                mtime = os.path.getmtime(path)  # measured_ts 추정치(C6)
                self.append_session(data, kind=kind, source_id=source_id, measured_ts=mtime)
                report["imported"] += 1
            except Exception as e:  # 손상 JSON 등 — fail-soft + report
                report["errors"].append({"path": path, "error": str(e)})
        return report
