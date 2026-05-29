"""jarvis_hud 작업 카드보드 routes (75 entry) — hermetic (Starlette TestClient + fake worker).

답습: docs/phase0/jarvis-hud-task-board-integration-brief.md (v1.1)
  + docs/review/3plus1-consensus-2026-05-29-jarvis-hud-task-board.md (CB-1~8)
실 ollama/tmux 0 — worker_builder 주입(fake). CB-7 주입 seam.
"""
from __future__ import annotations

import time

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.jarvis_tasks import JarvisTaskBoard, make_jarvis_routes
from src.adapters.llm.redaction_patterns import REDACTION_MARK
from src.jarvis.worker import WorkerResult

_SAME_ORIGIN = {"origin": "http://localhost:8765", "host": "localhost:8765"}


class _FakeWorker:
    def __init__(self, output="done", is_error=False, session=None, on_session=None):
        self.alias = "task"
        self._out = output
        self._err = is_error
        self._session = session
        self._on = on_session

    def run(self, prompt, workdir):
        if self._session and self._on:
            self._on(self._session)
        return WorkerResult(
            exit_code=1 if self._err else 0, output=self._out,
            cost_usd=None, is_error=self._err, raw=None,
        )


def _board(*, output="done", is_error=False, session=None, timeout=2.0) -> JarvisTaskBoard:
    def builder(opts, on_session):
        return _FakeWorker(output=output, is_error=is_error, session=session, on_session=on_session)
    return JarvisTaskBoard(
        worker_builder=builder, boss_builder=lambda opts: None, approver_timeout_s=timeout,
    )


def _client(board: JarvisTaskBoard) -> TestClient:
    return TestClient(Starlette(routes=make_jarvis_routes(board)))


def _wait_status(client: TestClient, task_id: str, target: str, tries=100, delay=0.05) -> dict:
    for _ in range(tries):
        cards = client.get("/api/jarvis/tasks").json()["tasks"]
        card = next((c for c in cards if c["id"] == task_id), None)
        if card and card["status"] == target:
            return card
        time.sleep(delay)
    raise AssertionError(f"task {task_id} 가 '{target}' 에 도달 못함 (마지막={card})")


def _submit(client: TestClient, **opts) -> str:
    opts.setdefault("prompt", "do something")
    r = client.post("/api/jarvis/task", json=opts, headers=_SAME_ORIGIN)
    assert r.status_code == 200, r.text
    return r.json()["task_id"]


# ── T-1: 제출 → 진행중 → 승인대기 ─────────────────────────────────────────────
def test_submit_reaches_awaiting() -> None:
    with _client(_board()) as client:
        tid = _submit(client)
        card = _wait_status(client, tid, "awaiting")
        assert card["status_label"] == "승인대기"


# ── T-3: 수락 → applied / 거절 → denied ───────────────────────────────────────
def test_decision_accept_applied() -> None:
    with _client(_board()) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        r = client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"},
                        headers=_SAME_ORIGIN)
        assert r.json()["ok"] is True
        card = _wait_status(client, tid, "applied")
        assert card["decision"] is True


def test_decision_reject_denied() -> None:
    with _client(_board()) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "reject"},
                    headers=_SAME_ORIGIN)
        _wait_status(client, tid, "denied")


# ── T-4: 워커 실패 → failed (approver 미호출) ─────────────────────────────────
def test_worker_failed() -> None:
    with _client(_board(is_error=True, output="boom")) as client:
        tid = _submit(client)
        _wait_status(client, tid, "failed")


# ── T-5 (CB-1): 출력 redaction — secret 평문 노출 0 ───────────────────────────
def test_output_redacted_in_board() -> None:
    secret = "sk-ant-LEAKSECRET1234567890"
    with _client(_board(output=f"my key {secret} done")) as client:
        tid = _submit(client)
        card = _wait_status(client, tid, "awaiting")
        prev = card["redacted_output_preview"] or ""
        assert secret not in prev          # 원본 secret 부재
        assert REDACTION_MARK in prev       # scrub 적용
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"},
                    headers=_SAME_ORIGIN)
        done = _wait_status(client, tid, "applied")
        assert secret not in (done["redacted_output_preview"] or "")


# ── T-8 (CB-3): CSRF — cross-origin POST 거부 ─────────────────────────────────
def test_csrf_cross_origin_rejected() -> None:
    with _client(_board()) as client:
        r = client.post("/api/jarvis/task", json={"prompt": "x"},
                        headers={"origin": "http://evil.example", "host": "localhost:8765"})
        assert r.status_code == 403
        # same-origin 은 정상
        assert client.post("/api/jarvis/task", json={"prompt": "x"},
                           headers=_SAME_ORIGIN).status_code == 200


# ── T-9 (CB-4): 미결정 timeout → default-deny ─────────────────────────────────
def test_timeout_default_deny() -> None:
    with _client(_board(timeout=0.3)) as client:  # 짧은 timeout
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        # 결정 미전송 → timeout → default-deny → denied
        card = _wait_status(client, tid, "denied", tries=60, delay=0.05)
        assert card["decision"] in (False, None)


# ── T-6 (CB-2): /pane scrub + ollama(세션 없음)=null ──────────────────────────
def test_pane_scrub_and_null() -> None:
    board = _board()  # ollama fake (세션 없음)
    with _client(board) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        assert client.get(f"/api/jarvis/task/{tid}/pane").json()["pane"] is None
    # board.pane scrub 직접 검증 (fake tmux_runner 주입)
    board._sessions["x"] = "sess-1"
    secret = "ghp_LEAKSECRETabcdef123456"
    out = board.pane("x", tmux_runner=lambda argv: (0, f"pane {secret} text", ""))
    assert secret not in out and REDACTION_MARK in out


# ── T-7: 동시 2 작업 보드 독립 ────────────────────────────────────────────────
def test_two_tasks_independent() -> None:
    with _client(_board()) as client:
        t1, t2 = _submit(client, prompt="task1"), _submit(client, prompt="task2")
        _wait_status(client, t1, "awaiting")
        _wait_status(client, t2, "awaiting")
        client.post(f"/api/jarvis/task/{t1}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        client.post(f"/api/jarvis/task/{t2}/decision", json={"decision": "reject"}, headers=_SAME_ORIGIN)
        assert _wait_status(client, t1, "applied")
        assert _wait_status(client, t2, "denied")
