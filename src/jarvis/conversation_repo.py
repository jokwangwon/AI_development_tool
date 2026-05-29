"""ConversationRepo (SQLite backing, 다중 대화) — 통합 데이터 레이어 §10-4a/§10-4b.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §10-4: ConversationRepo 를 sqlite3 직접 구현(Backing 추상화 없이, Rule of Three).
  - §6 RB-1: connection-per-operation + WAL + busy_timeout + short transaction. pool 금지.
  - §7 RB-3: 마이그레이션 무손실·idempotent — deterministic source id + UNIQUE +
    INSERT OR IGNORE + 원본 보존 + fail-soft + 손상 라인 skip.
  - Q7 해소: 대화 raw 저장(저장 redaction 없음). 영속 위치 권한은 paths(§10-2).

§10-4a: backing JSONL → SQLite (동작 불변).
§10-4b: 다중 대화 — conversations 테이블 + entries.conversation_id.
  - 자동 제목(첫 user 메시지), updated_ts 정렬, 대화별 read/delete.
  - 하위호환: conversation_id 없는 append/read_all 은 'default' 대화 (§10-4a 데이터 = ALTER DEFAULT).

외부 메서드: append/read_all/exists/delete_entry/archive_to (계약 유지) +
create_conversation/list_conversations/delete_conversation (§10-4b 신규). stdlib only.
"""
from __future__ import annotations

import json
import os
import sqlite3
import time
import uuid
from contextlib import closing
from pathlib import Path

_BUSY_TIMEOUT_MS = 5000
_DEFAULT_CONV = "default"  # §10-4a 단일 대화 호환 (conversation_id 미지정 시)
_TITLE_MAXLEN = 40

_SCHEMA_ENTRIES = """
CREATE TABLE IF NOT EXISTS entries (
    seq INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT,
    conversation_id TEXT NOT NULL DEFAULT 'default',
    payload TEXT NOT NULL
);
"""
_SCHEMA_CONVERSATIONS = """
CREATE TABLE IF NOT EXISTS conversations (
    id TEXT PRIMARY KEY,
    title TEXT,
    created_ts REAL,
    updated_ts REAL
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
            conn.execute(_SCHEMA_ENTRIES)
            conn.execute(_SCHEMA_CONVERSATIONS)
            conn.execute(_SOURCE_ID_INDEX)
            # §10-4a→4b: 기존 entries 에 conversation_id 컬럼 없으면 ALTER ADD (기존 행 = 'default')
            cols = [r[1] for r in conn.execute("PRAGMA table_info(entries)").fetchall()]
            if "conversation_id" not in cols:
                conn.execute(
                    "ALTER TABLE entries ADD COLUMN conversation_id TEXT NOT NULL DEFAULT 'default'"
                )

    # --- 대화 단위 (§10-4b) ---
    def create_conversation(self, title: str | None = None) -> str:
        cid = str(uuid.uuid4())
        now = time.time()
        with closing(self._connect()) as conn, conn:
            conn.execute(
                "INSERT INTO conversations(id, title, created_ts, updated_ts) VALUES(?, ?, ?, ?)",
                (cid, title, now, now),
            )
        return cid

    def list_conversations(self) -> list[dict]:
        """최근 갱신 순 [{id, title, created_ts, updated_ts}]."""
        try:
            with closing(self._connect()) as conn:
                rows = conn.execute(
                    "SELECT id, title, created_ts, updated_ts FROM conversations "
                    "ORDER BY updated_ts DESC, created_ts DESC"
                ).fetchall()
        except Exception:
            return []
        return [
            {"id": r[0], "title": r[1], "created_ts": r[2], "updated_ts": r[3]} for r in rows
        ]

    def delete_conversation(self, conversation_id: str) -> None:
        with closing(self._connect()) as conn, conn:
            conn.execute("DELETE FROM entries WHERE conversation_id = ?", (conversation_id,))
            conn.execute("DELETE FROM conversations WHERE id = ?", (conversation_id,))

    def _ensure_conversation(self, conn: sqlite3.Connection, cid: str) -> None:
        now = time.time()
        conn.execute(
            "INSERT OR IGNORE INTO conversations(id, title, created_ts, updated_ts) VALUES(?, ?, ?, ?)",
            (cid, None, now, now),
        )

    # --- entry 단위 (§10-4a 계약 유지 + conversation_id 옵션) ---
    def append(self, entry: dict, conversation_id: str | None = None) -> None:
        """JSONL append 동형 (fail-soft). conversation_id 미지정 시 'default' 대화.

        자동 제목: 대화 title 이 비었고 첫 user 메시지면 content 앞부분으로 설정.
        """
        try:
            cid = conversation_id or _DEFAULT_CONV
            source_id = entry.get("id")
            payload = json.dumps(entry, ensure_ascii=False)
            now = time.time()
            with closing(self._connect()) as conn, conn:
                self._ensure_conversation(conn, cid)
                conn.execute(
                    "INSERT OR IGNORE INTO entries(source_id, conversation_id, payload) VALUES(?, ?, ?)",
                    (source_id, cid, payload),
                )
                conn.execute("UPDATE conversations SET updated_ts = ? WHERE id = ?", (now, cid))
                if entry.get("role") == "user":
                    row = conn.execute(
                        "SELECT title FROM conversations WHERE id = ?", (cid,)
                    ).fetchone()
                    if row and not row[0]:
                        content = (entry.get("content") or "").strip()
                        if content:
                            conn.execute(
                                "UPDATE conversations SET title = ? WHERE id = ?",
                                (content[:_TITLE_MAXLEN], cid),
                            )
        except Exception:
            pass

    def read_all(self, conversation_id: str | None = None) -> list[dict]:
        """대화 entry (삽입 순서 = seq). conversation_id 미지정 시 'default' 대화."""
        cid = conversation_id or _DEFAULT_CONV
        try:
            with closing(self._connect()) as conn:
                rows = conn.execute(
                    "SELECT payload FROM entries WHERE conversation_id = ? ORDER BY seq", (cid,)
                ).fetchall()
        except Exception:
            return []
        out: list[dict] = []
        for (payload,) in rows:
            try:
                out.append(json.loads(payload))
            except Exception:
                continue
        return out

    def exists(self, conversation_id: str | None = None) -> bool:
        """대화 존재 = 행 ≥1. conversation_id 미지정 시 'default' 대화."""
        cid = conversation_id or _DEFAULT_CONV
        try:
            with closing(self._connect()) as conn:
                row = conn.execute(
                    "SELECT EXISTS(SELECT 1 FROM entries WHERE conversation_id = ?)", (cid,)
                ).fetchone()
            return bool(row[0])
        except Exception:
            return False

    def delete_entry(self, entry_id: str) -> int:
        """source_id 매칭 entry 제거 (전역 unique). removed count 반환."""
        with closing(self._connect()) as conn, conn:
            cur = conn.execute("DELETE FROM entries WHERE source_id = ?", (entry_id,))
            return cur.rowcount

    def archive_to(self, archive_path: str, conversation_id: str | None = None) -> bool:
        """대화 행을 JSONL 로 export(순서 보존) 후 비움. 없으면 no-op. 이동 여부 반환."""
        cid = conversation_id or _DEFAULT_CONV
        rows = self.read_all(conversation_id=cid)
        if not rows:
            return False
        with open(archive_path, "w", encoding="utf-8") as fh:
            for entry in rows:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        with closing(self._connect()) as conn, conn:
            conn.execute("DELETE FROM entries WHERE conversation_id = ?", (cid,))
        return True

    def _migrate_legacy(self, legacy_path: str) -> None:
        """legacy JSONL → SQLite 1회 적재 (RB-3). 'default' 대화 비어있을 때만, 원본 보존, fail-soft, 손상 라인 skip."""
        try:
            if self.exists():  # default 대화 비어있지 않으면 skip (재실행 안전)
                return
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
                    self.append(entry)  # default 대화
        except Exception:
            pass
