"""ConversationRepo (SQLite backing) — 통합 데이터 레이어 §10-4a 테스트.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §10-4: ConversationRepo 를 sqlite3 직접 구현(Backing 추상화 없이, :memory:/파일 테스트).
  - §6 RB-1: connection-per-operation + WAL + busy_timeout + short transaction (pool 금지).
  - §7 RB-3: 마이그레이션 무손실·idempotent — deterministic source id(entry id) + UNIQUE +
    INSERT OR IGNORE + 원본 보존(롤백) + fail-soft + 손상 라인 skip.
  - Q7 해소: 대화 raw 저장(저장 redaction 없음).

§10-3(JSONL) → §10-4a(SQLite) 전환. 외부 메서드 계약(append/read_all/exists/
delete_entry/archive_to) 불변 → server 6핸들러·라우트 통합 테스트는 그대로 통과.
JSONL 특유의 "깨진 줄 raw 보존"은 SQLite 에 유입 경로가 없어(append 가 항상 valid
JSON) 무의미 → 마이그레이션 손상 라인 skip 으로 대체(RB-3).
"""
from __future__ import annotations

import json
from pathlib import Path

from src.jarvis.conversation_repo import ConversationRepo


def test_append_then_read_all_preserves_order(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    repo.append({"id": "a", "role": "user", "content": "first"})
    repo.append({"id": "b", "role": "jarvis", "content": "second"})
    assert [e["id"] for e in repo.read_all()] == ["a", "b"]


def test_append_idempotent_by_source_id(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    repo.append({"id": "a", "content": "x"})
    repo.append({"id": "a", "content": "x"})  # 같은 id → INSERT OR IGNORE
    assert len(repo.read_all()) == 1


def test_append_without_id_always_added(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    repo.append({"content": "no-id-1"})
    repo.append({"content": "no-id-2"})
    assert len(repo.read_all()) == 2  # source_id NULL → partial unique 무관


def test_append_preserves_unicode(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    repo.append({"id": "x", "content": "한글"})
    assert repo.read_all()[0]["content"] == "한글"


def test_read_all_empty_when_no_rows(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    assert repo.read_all() == []


def test_exists_by_row_count(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    assert repo.exists() is False  # 행 0 (파일 존재해도 대화 없음)
    repo.append({"id": "a"})
    assert repo.exists() is True


def test_delete_entry_removes_matching_id(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    for i in ("a", "b", "c"):
        repo.append({"id": i})
    assert repo.delete_entry("b") == 1
    assert [e["id"] for e in repo.read_all()] == ["a", "c"]


def test_delete_entry_absent_returns_zero(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    assert repo.delete_entry("anything") == 0


def test_archive_to_exports_jsonl_and_clears(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    repo.append({"id": "a", "content": "hi"})
    repo.append({"id": "b", "content": "bye"})
    dest = tmp_path / "archive" / "c.jsonl"
    dest.parent.mkdir(parents=True, exist_ok=True)
    assert repo.archive_to(str(dest)) is True
    lines = [json.loads(l) for l in dest.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert [e["id"] for e in lines] == ["a", "b"]  # JSONL export, 순서 보존
    assert repo.exists() is False  # 원본 비워짐


def test_archive_to_noop_when_empty(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    assert repo.archive_to(str(tmp_path / "d.jsonl")) is False


def test_connection_per_operation_no_shared_state(tmp_path):
    # RB-1: connection-per-operation — 연속 호출이 ProgrammingError 없이 동작
    repo = ConversationRepo(tmp_path / "c.db")
    for i in range(5):
        repo.append({"id": str(i)})
    assert len(repo.read_all()) == 5


def test_path_property(tmp_path):
    p = tmp_path / "c.db"
    repo = ConversationRepo(p)
    assert str(repo.path) == str(p)


# --- RB-3 마이그레이션 (legacy JSONL → SQLite) ---
def test_migration_from_legacy_jsonl(tmp_path):
    legacy = tmp_path / "old.jsonl"
    legacy.write_text('{"id": "a", "content": "x"}\n{"id": "b", "content": "y"}\n', encoding="utf-8")
    repo = ConversationRepo(tmp_path / "c.db", legacy_jsonl=str(legacy))
    assert [e["id"] for e in repo.read_all()] == ["a", "b"]


def test_migration_idempotent_on_rerun(tmp_path):
    legacy = tmp_path / "old.jsonl"
    legacy.write_text('{"id": "a"}\n{"id": "b"}\n', encoding="utf-8")
    ConversationRepo(tmp_path / "c.db", legacy_jsonl=str(legacy))  # 1차
    repo2 = ConversationRepo(tmp_path / "c.db", legacy_jsonl=str(legacy))  # 재실행
    assert len(repo2.read_all()) == 2  # 중복 적재 0


def test_migration_preserves_original(tmp_path):
    legacy = tmp_path / "old.jsonl"
    legacy.write_text('{"id": "a"}\n', encoding="utf-8")
    ConversationRepo(tmp_path / "c.db", legacy_jsonl=str(legacy))
    assert legacy.exists()  # 원본 보존 = 롤백 가능


def test_migration_skips_broken_lines(tmp_path):
    legacy = tmp_path / "old.jsonl"
    legacy.write_text('{"id": "a"}\n!!broken!!\n{"id": "b"}\n', encoding="utf-8")
    repo = ConversationRepo(tmp_path / "c.db", legacy_jsonl=str(legacy))
    assert [e["id"] for e in repo.read_all()] == ["a", "b"]  # 손상 라인 skip (RB-3)


def test_migration_skipped_when_db_non_empty(tmp_path):
    db = tmp_path / "c.db"
    ConversationRepo(db).append({"id": "existing"})
    legacy = tmp_path / "old.jsonl"
    legacy.write_text('{"id": "a"}\n', encoding="utf-8")
    repo = ConversationRepo(db, legacy_jsonl=str(legacy))
    ids = [e["id"] for e in repo.read_all()]
    assert "existing" in ids and "a" not in ids  # db 비어있지 않으면 마이그레이션 skip


def test_migration_absent_legacy_is_noop(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db", legacy_jsonl=str(tmp_path / "nope.jsonl"))
    assert repo.read_all() == []  # legacy 없으면 빈 채로 정상


# === §10-4b 다중 대화 (conversation_id) ===
def test_create_conversation_returns_id(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    cid = repo.create_conversation()
    assert isinstance(cid, str) and cid
    assert any(c["id"] == cid for c in repo.list_conversations())


def test_append_to_conversation_and_read_filtered(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    c1 = repo.create_conversation()
    c2 = repo.create_conversation()
    repo.append({"id": "a", "role": "user", "content": "in c1"}, conversation_id=c1)
    repo.append({"id": "b", "role": "user", "content": "in c2"}, conversation_id=c2)
    assert [e["id"] for e in repo.read_all(conversation_id=c1)] == ["a"]
    assert [e["id"] for e in repo.read_all(conversation_id=c2)] == ["b"]


def test_auto_title_from_first_user_message(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    cid = repo.create_conversation()
    repo.append({"id": "a", "role": "user", "content": "데이터 레이어 구현하자"}, conversation_id=cid)
    conv = next(c for c in repo.list_conversations() if c["id"] == cid)
    assert "데이터" in conv["title"]


def test_auto_title_only_first_message(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    cid = repo.create_conversation()
    repo.append({"id": "a", "role": "user", "content": "첫 메시지"}, conversation_id=cid)
    repo.append({"id": "b", "role": "user", "content": "둘째 메시지"}, conversation_id=cid)
    conv = next(c for c in repo.list_conversations() if c["id"] == cid)
    assert "첫" in conv["title"] and "둘째" not in conv["title"]


def test_list_conversations_recent_updated_first(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    c1 = repo.create_conversation()
    c2 = repo.create_conversation()
    repo.append({"id": "a", "role": "user", "content": "x"}, conversation_id=c1)  # c1 마지막 갱신
    convs = repo.list_conversations()
    assert convs[0]["id"] == c1  # 최근 업데이트 먼저


def test_delete_conversation_removes_conv_and_entries(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    cid = repo.create_conversation()
    repo.append({"id": "a"}, conversation_id=cid)
    repo.delete_conversation(cid)
    assert repo.read_all(conversation_id=cid) == []
    assert not any(c["id"] == cid for c in repo.list_conversations())


def test_default_conversation_backcompat(tmp_path):
    # §10-4a 호환: conversation_id 없이 append/read_all → default 대화
    repo = ConversationRepo(tmp_path / "c.db")
    repo.append({"id": "a", "content": "x"})
    repo.append({"id": "b", "content": "y"})
    assert [e["id"] for e in repo.read_all()] == ["a", "b"]


def test_delete_entry_within_conversation(tmp_path):
    repo = ConversationRepo(tmp_path / "c.db")
    cid = repo.create_conversation()
    repo.append({"id": "a"}, conversation_id=cid)
    repo.append({"id": "b"}, conversation_id=cid)
    assert repo.delete_entry("a") == 1
    assert [e["id"] for e in repo.read_all(conversation_id=cid)] == ["b"]
