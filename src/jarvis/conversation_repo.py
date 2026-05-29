"""ConversationRepo (SQLite backing) — 통합 데이터 레이어 §10-4a.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §10-4: ConversationRepo 를 sqlite3 직접 구현(Backing 추상화 없이, Rule of Three).
  - §6 RB-1: connection-per-operation + WAL + busy_timeout + short transaction.
    단일 공유 connection / pool / long-lived 금지(check_same_thread 깨짐 방지).
  - §7 RB-3: 마이그레이션 무손실·idempotent — deterministic source id(entry id) +
    UNIQUE partial index + INSERT OR IGNORE + 원본 보존(롤백) + fail-soft + 손상 라인 skip.
  - Q7 해소: 대화 raw 저장(저장 redaction 없음). 영속 위치 권한은 paths(§10-2).

§10-3(JSONL) → §10-4a(SQLite) 전환. 외부 메서드 계약(append/read_all/exists/
delete_entry/archive_to) 불변 → server 6핸들러·라우트 통합 테스트 그대로 통과.
backing 교체(SQLite)는 이 클래스 내부에 격리(§10-3 추출의 보상).

stdlib only (sqlite3).
"""
from __future__ import annotations

import json
import os
import sqlite3
from contextlib import closing
from pathlib import Path

_BUSY_TIMEOUT_MS = 5000

_SCHEMA = """
CREATE TABLE IF NOT EXISTS entries (
    seq INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT,
    payload TEXT NOT NULL
);
"""
_SOURCE_ID_INDEX = (
    "CREATE UNIQUE INDEX IF NOT EXISTS idx_entries_source_id "
    "ON entries(source_id) WHERE source_id IS NOT NULL"
)


class ConversationRepo:
    def __init__(self, path: str | Path, *, legacy_jsonl: str | Path | None = None) -> None:
        self._path = str(path)
        self._ensure_schema()
        if legacy_jsonl is not None:
            self._migrate_legacy(str(legacy_jsonl))

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
            conn.execute(_SCHEMA)
            conn.execute(_SOURCE_ID_INDEX)

    def append(self, entry: dict) -> None:
        """JSONL append 동형 (fail-soft). source_id=entry.id → INSERT OR IGNORE(idempotent)."""
        try:
            source_id = entry.get("id")
            payload = json.dumps(entry, ensure_ascii=False)
            with closing(self._connect()) as conn, conn:
                conn.execute(
                    "INSERT OR IGNORE INTO entries(source_id, payload) VALUES(?, ?)",
                    (source_id, payload),
                )
        except Exception:
            pass

    def read_all(self) -> list[dict]:
        """전체 entry (삽입 순서 = seq). 파싱 실패 row skip, 비어있으면 []."""
        try:
            with closing(self._connect()) as conn:
                rows = conn.execute("SELECT payload FROM entries ORDER BY seq").fetchall()
        except Exception:
            return []
        out: list[dict] = []
        for (payload,) in rows:
            try:
                out.append(json.loads(payload))
            except Exception:
                continue
        return out

    def exists(self) -> bool:
        """대화 존재 = 행 ≥1 (파일 존재가 아님 — export 의 '대화 없음' 분기와 정합)."""
        try:
            with closing(self._connect()) as conn:
                row = conn.execute("SELECT EXISTS(SELECT 1 FROM entries)").fetchone()
            return bool(row[0])
        except Exception:
            return False

    def delete_entry(self, entry_id: str) -> int:
        """source_id 매칭 entry 제거. removed count 반환."""
        with closing(self._connect()) as conn, conn:
            cur = conn.execute("DELETE FROM entries WHERE source_id = ?", (entry_id,))
            return cur.rowcount

    def archive_to(self, archive_path: str) -> bool:
        """행이 있으면 JSONL 로 export(순서 보존) 후 전체 비움. 없으면 no-op. 이동 여부 반환."""
        rows = self.read_all()
        if not rows:
            return False
        with open(archive_path, "w", encoding="utf-8") as fh:
            for entry in rows:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        with closing(self._connect()) as conn, conn:
            conn.execute("DELETE FROM entries")
        return True

    def _migrate_legacy(self, legacy_path: str) -> None:
        """legacy JSONL → SQLite 1회 적재 (RB-3). db 비어있을 때만, 원본 보존, fail-soft, 손상 라인 skip."""
        try:
            if self.exists():
                return  # db 비어있지 않으면 skip (재실행 안전)
            if not os.path.exists(legacy_path):
                return
            with open(legacy_path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except Exception:
                        continue  # 손상 라인 skip
                    self.append(entry)
        except Exception:
            pass  # 마이그레이션 실패가 기동 차단 0
