"""ConversationRepo — 통합 데이터 레이어 §10-3 (0.5단계) 테스트.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §10-3: server.py 인라인 conversation 핸들러 6곳 → sync ConversationRepo
    추출(동작 불변 refactor). 안 하면 다중대화 SQLite swap 시 6곳 변경.
  - §5: repo별 얇은 port (sqlite3/JSONL 직접, Backing 추상화 없이 Rule of Three).
  - Q7 해소: 대화 raw 저장(저장 redaction 없음).

동작 불변 계약(server.py 기존 동작 캡처):
  - append = fail-soft JSONL (잘못된 부모 디렉터리면 조용히 실패).
  - read_all = parse, 깨진 줄은 skip, 파일 부재 시 [].
  - delete_entry = id 매칭 제거 후 rewrite, **깨진 줄은 raw 보존**(read_all 과 다름).
  - export 의 "파일 부재" 특수 분기를 위해 exists() 분리.
  - archive_to = 파일 있으면 rename(이동), 없으면 no-op.
"""
from __future__ import annotations

import json
from pathlib import Path

from src.jarvis.conversation_repo import ConversationRepo


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def test_append_then_read_all_preserves_order(tmp_path):
    repo = ConversationRepo(tmp_path / "conv.jsonl")
    repo.append({"id": "a", "role": "user", "content": "first"})
    repo.append({"id": "b", "role": "jarvis", "content": "second"})
    entries = repo.read_all()
    assert [e["id"] for e in entries] == ["a", "b"]


def test_append_writes_jsonl_lines(tmp_path):
    p = tmp_path / "conv.jsonl"
    repo = ConversationRepo(p)
    repo.append({"id": "x", "content": "한글"})
    # ensure_ascii=False — 한글 그대로
    assert "한글" in p.read_text(encoding="utf-8")
    assert len(_read_jsonl(p)) == 1


def test_read_all_absent_returns_empty(tmp_path):
    repo = ConversationRepo(tmp_path / "nope.jsonl")
    assert repo.read_all() == []


def test_read_all_skips_broken_lines(tmp_path):
    p = tmp_path / "conv.jsonl"
    p.write_text('{"id": "ok"}\n!!not json!!\n{"id": "ok2"}\n', encoding="utf-8")
    repo = ConversationRepo(p)
    assert [e["id"] for e in repo.read_all()] == ["ok", "ok2"]


def test_append_fail_soft_on_missing_parent(tmp_path):
    # 부모 디렉터리가 없으면 조용히 실패(현 _save_conversation_entry 동작).
    repo = ConversationRepo(tmp_path / "no_such_dir" / "conv.jsonl")
    repo.append({"id": "a"})  # raises 안 함
    assert repo.read_all() == []


def test_exists(tmp_path):
    p = tmp_path / "conv.jsonl"
    repo = ConversationRepo(p)
    assert repo.exists() is False
    repo.append({"id": "a"})
    assert repo.exists() is True


def test_delete_entry_removes_matching_id(tmp_path):
    p = tmp_path / "conv.jsonl"
    repo = ConversationRepo(p)
    repo.append({"id": "a", "content": "keep"})
    repo.append({"id": "b", "content": "drop"})
    repo.append({"id": "c", "content": "keep"})
    removed = repo.delete_entry("b")
    assert removed == 1
    assert [e["id"] for e in repo.read_all()] == ["a", "c"]


def test_delete_entry_preserves_broken_lines_raw(tmp_path):
    p = tmp_path / "conv.jsonl"
    p.write_text('{"id": "a"}\n!!broken!!\n{"id": "b"}\n', encoding="utf-8")
    repo = ConversationRepo(p)
    removed = repo.delete_entry("a")
    assert removed == 1
    raw = p.read_text(encoding="utf-8")
    assert "!!broken!!" in raw  # 깨진 줄 raw 보존
    assert '"id": "b"' in raw
    assert '"id": "a"' not in raw


def test_delete_entry_absent_file_returns_zero(tmp_path):
    repo = ConversationRepo(tmp_path / "nope.jsonl")
    assert repo.delete_entry("anything") == 0


def test_archive_to_moves_file(tmp_path):
    p = tmp_path / "conv.jsonl"
    repo = ConversationRepo(p)
    repo.append({"id": "a"})
    dest = tmp_path / "archive" / "conv_20260529.jsonl"
    dest.parent.mkdir(parents=True, exist_ok=True)
    moved = repo.archive_to(str(dest))
    assert moved is True
    assert dest.exists()
    assert repo.exists() is False  # 원본 이동됨


def test_archive_to_noop_when_absent(tmp_path):
    repo = ConversationRepo(tmp_path / "nope.jsonl")
    assert repo.archive_to(str(tmp_path / "dest.jsonl")) is False


def test_path_property(tmp_path):
    p = tmp_path / "conv.jsonl"
    repo = ConversationRepo(p)
    assert str(repo.path) == str(p)
