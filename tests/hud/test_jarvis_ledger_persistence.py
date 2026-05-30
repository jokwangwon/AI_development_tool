"""JarvisTaskBoard 디딤돌0 — 영속(LedgerLog) + 재시작 restore + 취소 (hermetic).

답습: docs/phase0/jarvis-collaborative-orchestration-design-brief.md (v2) §5
  - 영속 레저(LedgerLog) + 재시작 고아 interrupted 마킹 + 실행 중 취소.
  - B5: 영속 = scrub 된 카드 메타만. raw 워커 출력 미영속(CB-1 보존).
  - 취소: tmux=실 kill / ollama=포기 마킹. cancel = 반영 안 함(default-deny).
실 ollama/tmux 0 — worker_builder 주입(fake) + 실 디스크 레저(tmp_path).
"""
from __future__ import annotations

import time
from pathlib import Path

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.jarvis_tasks import JarvisTaskBoard, make_jarvis_routes
from src.jarvis.ledger import LedgerLog
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


# 기본 approver_timeout_s 를 넉넉히(30s) — 본 파일 테스트는 모두 명시적
# decision/cancel/dismiss 를 보내고 default-deny *timeout 발화* 를 검증하지 않는다.
# 작은 값(이전 2.0s)이면 부하(전체 스위트 교차 실행) 시 awaiting→action 창이
# timeout 을 넘겨 default-deny 가 먼저 발화 → denied(terminal) → cancel no-op 으로
# 간헐 실패(wall-clock race). 큰 timeout = race window 제거(액션은 항상 먼저 옴),
# 진짜 hang 시 30s 내 실패. timeout 발화 자체를 보려면 개별 짧은 timeout 명시.
def _board(ledger_path: Path, *, output="done", is_error=False, session=None,
           timeout=30.0, tmux_runner=None) -> JarvisTaskBoard:
    def builder(opts, on_session, cancel_check):
        return _FakeWorker(output=output, is_error=is_error, session=session, on_session=on_session)
    return JarvisTaskBoard(
        worker_builder=builder, boss_builder=lambda opts: None,
        approver_timeout_s=timeout, ledger=LedgerLog(ledger_path), tmux_runner=tmux_runner,
    )


def _client(board: JarvisTaskBoard) -> TestClient:
    return TestClient(Starlette(routes=make_jarvis_routes(board)))


def _wait_status(client, task_id, target, tries=100, delay=0.05) -> dict:
    card = None
    for _ in range(tries):
        cards = client.get("/api/jarvis/tasks").json()["tasks"]
        card = next((c for c in cards if c["id"] == task_id), None)
        if card and card["status"] == target:
            return card
        time.sleep(delay)
    raise AssertionError(f"task {task_id} 가 '{target}' 미도달 (마지막={card})")


def _submit(client, **opts) -> str:
    opts.setdefault("prompt", "do something")
    r = client.post("/api/jarvis/task", json=opts, headers=_SAME_ORIGIN)
    assert r.status_code == 200, r.text
    return r.json()["task_id"]


# ── 영속 (LedgerLog 기록) ──────────────────────────────────────────────────────
def test_create_records_created_event(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    board = _board(path)
    tid = board.create({"prompt": "task X", "worker_type": "ollama"})
    events = list(LedgerLog(path).read())
    assert any(e["event"] == "created" and e["task_id"] == tid for e in events)


def test_lifecycle_persisted_to_ledger(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "applied")
    assert LedgerLog(path).fold()[tid]["status"] == "applied"


def test_raw_worker_output_not_persisted(tmp_path: Path) -> None:
    """B5/CB-1: raw 워커 출력은 레저에 안 들어감 — scrub 된 preview 만."""
    path = tmp_path / "ledger.jsonl"
    secret = "sk-ant-LEAKSECRET1234567890"
    with _client(_board(path, output=f"begin {secret} end")) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "applied")
    assert secret not in path.read_text(encoding="utf-8")  # 평문 secret 영속 0


# ── 재시작 restore ─────────────────────────────────────────────────────────────
def test_restart_restores_terminal_card(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        tid = _submit(client, prompt="survive restart")
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "applied")
    # "재시작" = 같은 레저 경로로 새 board
    board2 = _board(path)
    restored = next((c for c in board2.snapshot() if c["id"] == tid), None)
    assert restored is not None
    assert restored["status"] == "applied"
    assert restored["prompt"] == "survive restart"


def test_restart_orphan_marked_interrupted(tmp_path: Path) -> None:
    """미완 상태로 crash → 재시작 fold = interrupted (자동 복구 없음).

    crash = resolved 이벤트가 *기록되기 전* 프로세스 종료 = 레저에 created/awaiting 만.
    (정상 timeout 종료는 resolved(denied) 가 기록되므로 interrupted 아님 — crash 와 구분).
    """
    path = tmp_path / "ledger.jsonl"
    seed = LedgerLog(path)
    seed.record("t-orphan", "created", prompt="mid-flight", worker_type="ollama", status="running")
    seed.record("t-orphan", "awaiting", status="awaiting", flags=[])  # resolved 부재 = crash
    board2 = _board(path)
    restored = next((c for c in board2.snapshot() if c["id"] == "t-orphan"), None)
    assert restored is not None
    assert restored["status"] == "interrupted"
    assert restored["status_label"] == "중단됨"
    assert restored["prompt"] == "mid-flight"


def test_no_ledger_no_restore_backward_compat(tmp_path: Path) -> None:
    """ledger=None = 기존 동작(영속 0, restore 0)."""
    board = JarvisTaskBoard(
        worker_builder=lambda opts, on_session, cancel_check: _FakeWorker(),
        boss_builder=lambda opts: None,
    )
    assert board.snapshot() == []


# ── 취소 (실행 중 취소 = 반영 안 함) ────────────────────────────────────────────
def test_cancel_while_awaiting_marks_cancelled(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        r = client.post(f"/api/jarvis/task/{tid}/cancel", json={}, headers=_SAME_ORIGIN)
        assert r.status_code == 200 and r.json()["ok"] is True
        card = _wait_status(client, tid, "cancelled")
        assert card["decision"] in (False, None)   # 반영 안 됨(default-deny)
        assert card["status_label"] == "취소"
    assert LedgerLog(path).fold()[tid]["status"] == "cancelled"


def test_cancel_route_csrf_rejected(tmp_path: Path) -> None:
    with _client(_board(tmp_path / "l.jsonl")) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        r = client.post(f"/api/jarvis/task/{tid}/cancel", json={},
                        headers={"origin": "http://evil.example", "host": "localhost:8765"})
        assert r.status_code == 403


def test_cancel_unknown_task_404(tmp_path: Path) -> None:
    with _client(_board(tmp_path / "l.jsonl")) as client:
        r = client.post("/api/jarvis/task/nope/cancel", json={}, headers=_SAME_ORIGIN)
        assert r.status_code == 404


def test_cancel_terminal_is_noop(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "applied")
        # 이미 완결 → 취소 no-op
        r = client.post(f"/api/jarvis/task/{tid}/cancel", json={}, headers=_SAME_ORIGIN)
        assert r.json()["ok"] is False
        cards = client.get("/api/jarvis/tasks").json()["tasks"]
        assert next(c for c in cards if c["id"] == tid)["status"] == "applied"


# ── 제거 (dismissed — append-only 존중, fold 제외) ──────────────────────────────
def test_dismiss_terminal_removes_from_board_and_ledger(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "applied")
        r = client.post(f"/api/jarvis/task/{tid}/dismiss", json={}, headers=_SAME_ORIGIN)
        assert r.status_code == 200 and r.json()["ok"] is True
        cards = client.get("/api/jarvis/tasks").json()["tasks"]
        assert all(c["id"] != tid for c in cards)        # 보드에서 제거
    assert tid not in LedgerLog(path).fold()             # fold 제외
    assert any(e["event"] == "dismissed" for e in LedgerLog(path).read())  # 기록 보존


def test_dismiss_running_protected(tmp_path: Path) -> None:
    """진행중/승인대기 = 제거 불가(보호) — 완결만 제거."""
    with _client(_board(tmp_path / "l.jsonl")) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        r = client.post(f"/api/jarvis/task/{tid}/dismiss", json={}, headers=_SAME_ORIGIN)
        assert r.status_code == 404 and r.json()["ok"] is False
        cards = client.get("/api/jarvis/tasks").json()["tasks"]
        assert any(c["id"] == tid for c in cards)         # 카드 유지


def test_dismiss_route_csrf_rejected(tmp_path: Path) -> None:
    with _client(_board(tmp_path / "l.jsonl")) as client:
        r = client.post("/api/jarvis/task/x/dismiss", json={},
                        headers={"origin": "http://evil.example", "host": "localhost:8765"})
        assert r.status_code == 403


def test_dismiss_completed_bulk(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        # 2 완결(applied) + 1 미완(awaiting)
        done = []
        for _ in range(2):
            t = _submit(client)
            _wait_status(client, t, "awaiting")
            client.post(f"/api/jarvis/task/{t}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
            _wait_status(client, t, "applied")
            done.append(t)
        live = _submit(client)
        _wait_status(client, live, "awaiting")
        r = client.post("/api/jarvis/tasks/dismiss-completed", json={}, headers=_SAME_ORIGIN)
        assert r.status_code == 200 and r.json()["count"] == 2
        ids = {c["id"] for c in client.get("/api/jarvis/tasks").json()["tasks"]}
        assert ids == {live}                              # 완결만 제거, 미완 유지


def test_dismissed_not_restored_on_restart(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    with _client(_board(path)) as client:
        tid = _submit(client)
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/decision", json={"decision": "accept"}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "applied")
        client.post(f"/api/jarvis/task/{tid}/dismiss", json={}, headers=_SAME_ORIGIN)
    board2 = _board(path)                                 # 재시작
    assert all(c["id"] != tid for c in board2.snapshot())  # 제거 영속


def test_cancel_kills_tmux_session(tmp_path: Path) -> None:
    """tmux 세션 보유 task 취소 → 실 kill-session(자원 회수)."""
    path = tmp_path / "ledger.jsonl"
    calls: list[list[str]] = []

    def spy_runner(argv):
        calls.append(list(argv))
        return 0, "", ""

    board = _board(path, session="jarvis-deadbeef", tmux_runner=spy_runner)
    with _client(board) as client:
        tid = _submit(client, worker_type="tmux")
        _wait_status(client, tid, "awaiting")
        client.post(f"/api/jarvis/task/{tid}/cancel", json={}, headers=_SAME_ORIGIN)
        _wait_status(client, tid, "cancelled")
    assert any(a[:2] == ["tmux", "kill-session"] and "jarvis-deadbeef" in a for a in calls)
