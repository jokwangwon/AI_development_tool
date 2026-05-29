"""conversation 라우트 동작 불변 검증 — §10-3 ConversationRepo 추출 후.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md §10-3
  (server.py 인라인 6핸들러 → ConversationRepo 위임 = 동작 불변 refactor).

핸들러는 모듈 전역 `_conversation_repo` 를 참조하므로 monkeypatch 로 교체.
respond_handler 는 ollama 의존이라 제외(repo.append 는 test_conversation_repo 단위 커버).
import 부작용(모듈 레벨 repo 생성) 격리를 위해 import 전 JARVIS_DATA_DIR 설정.
"""
from __future__ import annotations

import json
import os
import tempfile

os.environ.setdefault("JARVIS_DATA_DIR", tempfile.mkdtemp(prefix="jarvis-route-test-"))

from starlette.testclient import TestClient  # noqa: E402

from jarvis_hud import server  # noqa: E402
from src.jarvis.conversation_repo import ConversationRepo  # noqa: E402


def _repo_with(tmp_path, entries):
    repo = ConversationRepo(tmp_path / "c.jsonl")
    for e in entries:
        repo.append(e)
    return repo


def test_history_returns_entries(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo",
                        _repo_with(tmp_path, [{"id": "a", "role": "user", "content": "hello"}]))
    r = TestClient(server.app).get("/api/conversation/history")
    assert r.status_code == 200
    assert [e["id"] for e in r.json()["entries"]] == ["a"]


def test_history_query_filter(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo",
                        _repo_with(tmp_path, [{"id": "a", "content": "apple"},
                                              {"id": "b", "content": "banana"}]))
    r = TestClient(server.app).get("/api/conversation/history?q=banana")
    assert [e["id"] for e in r.json()["entries"]] == ["b"]


def test_history_absent_empty(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo", ConversationRepo(tmp_path / "absent.jsonl"))
    r = TestClient(server.app).get("/api/conversation/history")
    assert r.json()["entries"] == []


def test_canvas_only_note_svg(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo", _repo_with(tmp_path, [
        {"id": "u", "role": "user", "content": "x"},
        {"id": "n", "type": "note", "title": "t"},
        {"id": "s", "type": "svg", "svg": "<svg/>"},
    ]))
    r = TestClient(server.app).get("/api/conversation/canvas")
    assert [card["id"] for card in r.json()["cards"]] == ["n", "s"]


def test_export_absent_special(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo", ConversationRepo(tmp_path / "absent.jsonl"))
    client = TestClient(server.app)
    assert client.get("/api/conversation/export?format=md").json()["content"] == "(대화 없음)"
    assert client.get("/api/conversation/export?format=json").json()["content"] == "[]"


def test_export_json_entries(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo",
                        _repo_with(tmp_path, [{"id": "a", "role": "user", "content": "hi"}]))
    r = TestClient(server.app).get("/api/conversation/export?format=json")
    assert json.loads(r.json()["content"])[0]["id"] == "a"


def test_delete_entry_route(monkeypatch, tmp_path):
    repo = _repo_with(tmp_path, [{"id": "a"}, {"id": "b"}])
    monkeypatch.setattr(server, "_conversation_repo", repo)
    r = TestClient(server.app).delete("/api/conversation/entry/a")
    assert r.json() == {"ok": True, "removed": 1}
    assert [e["id"] for e in repo.read_all()] == ["b"]


def test_clear_route_archives(monkeypatch, tmp_path):
    repo = _repo_with(tmp_path, [{"id": "a"}])
    monkeypatch.setattr(server, "_conversation_repo", repo)
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "data"))  # archive_dir 격리
    r = TestClient(server.app).post("/api/conversation/clear")
    body = r.json()
    assert body["ok"] is True
    assert body["archived"] is not None
    assert repo.exists() is False


def test_clear_route_noop_when_absent(monkeypatch, tmp_path):
    monkeypatch.setattr(server, "_conversation_repo", ConversationRepo(tmp_path / "absent.jsonl"))
    r = TestClient(server.app).post("/api/conversation/clear")
    assert r.json() == {"ok": True, "archived": None}
