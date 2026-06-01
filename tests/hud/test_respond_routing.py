"""respond_handler 대화→작업 라우팅 통합 — 발견 #UI-1 (디딤돌, 119).

답습: docs/phase0/jarvis-conversation-task-routing-design-brief.md (v3)
  [[3plus1-consensus-2026-06-01-jarvis-conversation-task-routing]] (REVISE).

검증: chat mode + 작업 의심 → boss.plan(seam) → proposal 동봉.
- 잡담 → proposal 없음 + planner 생성 0 (A3 latency 불변식).
- note/svg mode → 작업 라우팅 스킵 (BL-4 우선순위: detectMode 가 먼저).
- BL-1: respond 는 proposal *페이로드만* 반환, board.create/run 직접 호출 0.

seam(BL-5): `_make_routing_planner`(monkeypatch) + `_ollama_chat_sync` +
`_save_conversation_entry` 교체로 hermetic(실 ollama 0).
"""
from __future__ import annotations

import os
import tempfile

os.environ.setdefault("JARVIS_DATA_DIR", tempfile.mkdtemp(prefix="jarvis-respond-test-"))

from starlette.testclient import TestClient  # noqa: E402

from jarvis_hud import server  # noqa: E402
from src.jarvis.boss import BossPlan, PlanSubtask, StubBoss  # noqa: E402


def _stub_chat(*_a, **_k):
    return {"message": {"content": "네, 도와드릴게요."}}


async def _noop_save(entry, conversation_id=None):
    return None


def _patch_common(monkeypatch):
    monkeypatch.setattr(server, "_ollama_chat_sync", _stub_chat)
    monkeypatch.setattr(server, "_save_conversation_entry", _noop_save)


def test_chat_task_includes_proposal(monkeypatch):
    _patch_common(monkeypatch)
    monkeypatch.setattr(server, "_make_routing_planner",
                        lambda model: StubBoss("x", plan=BossPlan(
                            subtasks=(PlanSubtask("gcd 작성", "claude"),))))
    r = TestClient(server.app).post(
        "/api/respond", json={"message": "gcd 함수 만들어줘", "mode": "chat"})
    body = r.json()
    assert body["mode"] == "chat"
    assert body["proposal"]["prompt"] == "gcd 함수 만들어줘"
    assert body["proposal"]["subtask_count"] == 1


def test_chat_smalltalk_no_proposal_and_no_planner(monkeypatch):
    """잡담 → looks_like_task False → planner 생성 0 (latency 불변식)."""
    _patch_common(monkeypatch)
    created = []
    monkeypatch.setattr(server, "_make_routing_planner",
                        lambda model: created.append(model) or StubBoss("x"))
    r = TestClient(server.app).post(
        "/api/respond", json={"message": "오늘 날씨 어때?", "mode": "chat"})
    assert "proposal" not in r.json()
    assert created == []  # 잡담은 planner 인스턴스조차 안 만든다


def test_note_mode_skips_task_routing(monkeypatch):
    """BL-4: note mode 면 작업 라우팅 스킵 (detectMode 우선)."""
    _patch_common(monkeypatch)
    # note mode 는 MODE_PROMPTS[note] 로 ollama 호출 후 JSON 파싱 → _stub_chat 은
    # JSON 아니므로 except 폴백(title 노트). planner 는 절대 호출 안 됨.
    created = []
    monkeypatch.setattr(server, "_make_routing_planner",
                        lambda model: created.append(model) or StubBoss("x"))
    r = TestClient(server.app).post(
        "/api/respond", json={"message": "보고서 정리해줘", "mode": "note"})
    assert "proposal" not in r.json()
    assert created == []


def test_chat_task_but_empty_plan_no_proposal(monkeypatch):
    """규칙 통과했으나 boss 빈 plan → proposal 없음 (fail-safe)."""
    _patch_common(monkeypatch)
    monkeypatch.setattr(server, "_make_routing_planner",
                        lambda model: StubBoss("x", plan=BossPlan(subtasks=())))
    r = TestClient(server.app).post(
        "/api/respond", json={"message": "뭐 만들까 생각중", "mode": "chat"})
    assert "proposal" not in r.json()
