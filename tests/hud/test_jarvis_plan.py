"""JarvisPlanBoard — HUD 계획 승인 보드 트랙 A 테스트(hermetic).

답습: docs/phase0/jarvis-hud-plan-approval-design-brief.md (v1.1)
  + 3plus1-consensus-2026-05-30-jarvis-hud-plan-approval (BLOCKING 6).
  - CB-4 default-deny(Event.wait timeout) / BL-2 plan 게이트만 사람(subtask auto-accept) /
    BL-3 plan 게이트=dispatch 전 / BL-5 same_origin URL 정확 일치 / GP-3 idempotent(409) /
    CB-1 scrub + GP-3 비절단.

planner_builder/worker_builder 주입 = 실 ollama/claude 0(StubBoss + FakeWorker).
"""
from __future__ import annotations

import threading
import time

from src.jarvis.boss import BossPlan, Contract, PlanSubtask, StubBoss
from src.jarvis.orchestrator import WorkerRegistry
from src.jarvis.worker import WorkerResult

from jarvis_hud.jarvis_plan import (
    JarvisPlanBoard,
    make_jarvis_plan_routes,
    same_origin_strict,
)


class FakeWorker:
    def __init__(self, alias: str, output: str = "ok") -> None:
        self.alias = alias
        self._output = output

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        return WorkerResult.from_cli(
            0, '{"result": "%s", "is_error": false}' % self._output)


def _wait(cond, timeout: float = 5.0) -> bool:
    end = time.time() + timeout
    while time.time() < end:
        if cond():
            return True
        time.sleep(0.02)
    return False


def _board(plan: BossPlan, *, output: str = "ok", timeout: float = 5.0) -> JarvisPlanBoard:
    def planner_builder(opts):
        return StubBoss(name="stub", plan=plan)

    def worker_builder(opts):
        reg = WorkerRegistry()
        reg.register(FakeWorker("fake-file", output))
        return reg, {"file": "fake-file"}

    return JarvisPlanBoard(planner_builder=planner_builder, worker_builder=worker_builder,
                           approver_timeout_s=timeout)


_PLAN_2 = BossPlan(subtasks=(
    PlanSubtask(desc="백엔드 API", worker_kind="file"),
    PlanSubtask(desc="프론트 폼", worker_kind="file", depends_on=(0,)),
), contracts=(Contract(name="api_schema", produced_by=0),))


# --- 승인 흐름: create → run thread → awaiting → decide accept → completed ---

def test_plan_approval_completed() -> None:
    board = _board(_PLAN_2)
    plan_id = board.create_plan({"prompt": "앱 만들어줘"})
    t = threading.Thread(target=board.run_plan, args=(plan_id,))
    t.start()
    assert _wait(lambda: board._plans[plan_id]["status"] == "awaiting")  # BL-3 dispatch 전 게이트
    view = board._plans[plan_id]["plan"]
    assert len(view["subtasks"]) == 2
    assert view["contracts"] == [{"name": "api_schema", "produced_by": 0}]  # BL-6 명시 표시
    assert view["subtasks"][0]["alias"] == "fake-file"
    board.decide_plan(plan_id, True)
    t.join(timeout=5)
    assert board._plans[plan_id]["status"] == "completed"
    subs = board.snapshot()["subtasks"]
    assert len(subs) == 2 and all(s["status"] == "applied" for s in subs)  # Q5 subtask 카드 N


def test_plan_denied_no_dispatch() -> None:
    board = _board(_PLAN_2)
    plan_id = board.create_plan({"prompt": "x"})
    t = threading.Thread(target=board.run_plan, args=(plan_id,)); t.start()
    assert _wait(lambda: board._plans[plan_id]["status"] == "awaiting")
    board.decide_plan(plan_id, False)
    t.join(timeout=5)
    assert board._plans[plan_id]["status"] == "denied"
    assert board.snapshot()["subtasks"] == []  # 거부 = subtask dispatch 0


def test_default_deny_timeout() -> None:
    board = _board(_PLAN_2, timeout=0.3)  # 짧은 timeout → 미응답 default-deny
    plan_id = board.create_plan({"prompt": "x"})
    t = threading.Thread(target=board.run_plan, args=(plan_id,)); t.start()
    t.join(timeout=5)
    assert board._plans[plan_id]["status"] == "denied"  # CB-4 timeout default-deny
    assert board.snapshot()["subtasks"] == []


def test_validation_failed_no_modal() -> None:
    """빈 plan → controller VALIDATION_FAILED, 모달(awaiting) 미진입 → failed."""
    board = _board(BossPlan(subtasks=()))
    plan_id = board.create_plan({"prompt": "x"})
    t = threading.Thread(target=board.run_plan, args=(plan_id,)); t.start()
    t.join(timeout=5)
    assert board._plans[plan_id]["status"] == "failed"
    assert board._plans[plan_id]["plan"] is None  # 모달 안 뜸


# --- BL-1 scrub(secret) + GP-3 비절단 ---

def test_plan_card_scrubs_secret_untruncated() -> None:
    from src.adapters.llm.redaction_patterns import REDACTION_MARK

    secret = "sk-ant-LEAKSECRET1234567890"
    long_desc = "X" * 400 + " " + secret
    plan = BossPlan(subtasks=(PlanSubtask(desc=long_desc, worker_kind="file"),))
    board = _board(plan)
    plan_id = board.create_plan({"prompt": "x"})
    t = threading.Thread(target=board.run_plan, args=(plan_id,)); t.start()
    assert _wait(lambda: board._plans[plan_id]["status"] == "awaiting")
    board.decide_plan(plan_id, True); t.join(timeout=5)
    desc = board._plans[plan_id]["plan"]["subtasks"][0]["desc"]
    assert secret not in desc                # CB-1 secret strip
    assert REDACTION_MARK in desc            # 마스킹
    assert desc.count("X") == 400            # GP-3 비절단(truncate 0)


# --- BL-5 same_origin URL 정확 일치 ---

class _Req:
    def __init__(self, origin=None, host="localhost:8765"):
        self.headers = {}
        if origin is not None:
            self.headers["origin"] = origin
        self.headers["host"] = host


def test_same_origin_strict() -> None:
    assert same_origin_strict(_Req(origin="http://localhost:8765")) is True   # 정확 일치
    assert same_origin_strict(_Req(origin=None)) is True                       # Origin 부재 허용(잔여)
    assert same_origin_strict(_Req(origin="http://evil-localhost:8765")) is False  # suffix 우회 차단
    assert same_origin_strict(_Req(origin="http://localhost:9999")) is False   # 포트 불일치


# --- GP-3 /plan-decision idempotent (awaiting 아닌 → False=409) ---

def test_decide_non_awaiting_rejected() -> None:
    board = _board(_PLAN_2)
    plan_id = board.create_plan({"prompt": "x"})
    # planning 상태(run 전) — awaiting 아님 → decide False
    assert board.decide_plan(plan_id, True) is False
    assert board.decide_plan("nonexistent", True) is False


# --- 라우트 (same-origin 403) ---

def test_routes_cross_origin_forbidden() -> None:
    from starlette.applications import Starlette
    from starlette.testclient import TestClient

    board = _board(_PLAN_2)
    app = Starlette(routes=make_jarvis_plan_routes(board))
    client = TestClient(app)
    r = client.post("/api/jarvis/plan", json={"prompt": "x"},
                    headers={"origin": "http://evil-localhost:8765", "host": "localhost:8765"})
    assert r.status_code == 403  # BL-5 cross-origin 차단


# --- 디딤돌1f F3: 능력 경고가 HUD plan_view 에 표시 ---

def test_plan_view_exposes_capability_warnings() -> None:
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="코드 실행해 결과 출력", worker_kind="file",
                    requires_execution=True),
    ), contracts=())

    def planner_builder(opts):
        return StubBoss(name="stub", plan=plan)

    def worker_builder(opts):
        reg = WorkerRegistry()
        reg.register(FakeWorker("wf"))
        reg.register(FakeWorker("wc"))
        return reg, {"file": "wf", "code": "wc"}  # 실행워커 존재 → 거부 아닌 경고

    board = JarvisPlanBoard(planner_builder=planner_builder,
                            worker_builder=worker_builder, approver_timeout_s=5.0)
    plan_id = board.create_plan({"prompt": "x"})
    t = threading.Thread(target=board.run_plan, args=(plan_id,)); t.start()
    assert _wait(lambda: board._plans[plan_id]["status"] == "awaiting")
    view = board._plans[plan_id]["plan"]
    board.decide_plan(plan_id, True); t.join(timeout=5)
    assert view.get("capability_warnings"), "능력 경고가 plan_view 에 노출"
    assert view["capability_warnings"][0]["subtask_index"] == 0
