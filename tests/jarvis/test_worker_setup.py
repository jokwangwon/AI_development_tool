"""worker_setup — 실 워커 registry + kind_table 빌더 트랙 A 테스트.

답습: docs/sessions/SESSION_2026-05-30.md (디딤돌1d 실 워커 배선).
  - code=CliWorker(claude)+Landlock / file=OllamaWorker. kind_table 주입.
  - 능력 경계(ADR-013 Q7): code consume = PlanController(allow_code_consume) opt-in.

트랙 A — 실 claude·sandboxer 0건(code_runner/code_isolation 주입).
"""
from __future__ import annotations

from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import BossPlan, PlanSubtask
from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.orchestrator import Orchestrator
from src.jarvis.plan_controller import PlanController, PlanStatus
from src.jarvis.review import ReviewGuard
from src.jarvis.worker_setup import build_worker_registry


def _claude_json(result: str) -> str:
    return '{"result": %s, "is_error": false, "total_cost_usd": 0.0}' % (
        '"%s"' % result.replace('"', '\\"'))


def test_build_registry_structure() -> None:
    reg, table = build_worker_registry(
        code_runner=lambda cmd, wd: (0, _claude_json("ok"), ""),
        code_isolation=PassthroughIsolation(),
    )
    assert table == {"code": "claude", "file": "ollama-file"}
    assert reg.select("claude").alias == "claude"       # code worker 등록
    assert reg.select("ollama-file").alias == "ollama-file"  # file worker 등록


def test_code_worker_runner_isolation_injected() -> None:
    """code_runner/code_isolation 주입 = 실 claude·sandboxer 없이 결정적."""
    calls: list = []
    reg, _ = build_worker_registry(
        code_runner=lambda cmd, wd: calls.append(cmd) or (0, _claude_json("done"), ""),
        code_isolation=PassthroughIsolation(),
    )
    res = reg.select("claude").run("작업", "/tmp/ws")
    assert res.succeeded and res.output == "done"
    # CliWorker 가 CLAUDE_ARGV + prompt 로 호출(Passthrough = 변형 0)
    assert calls[0][0] == "claude" and calls[0][-1] == "작업"


def test_plan_controller_routes_code_via_table() -> None:
    """kind_table 주입 → PlanController 가 code subtask 를 claude 로 라우팅(트랙 A)."""
    seen: list = []

    def code_runner(cmd, wd):
        seen.append(cmd[-1])
        return 0, _claude_json("code-done"), ""

    reg, table = build_worker_registry(
        code_runner=code_runner, code_isolation=PassthroughIsolation())
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: True),
                        workdir_factory=lambda t: f"/tmp/ws/{t}")
    ctrl = PlanController(
        dispatcher=orch.dispatch, kind_table=table, registry=reg,
        plan_approver=lambda r: True, implicit_contracts=False,
    )
    plan = BossPlan(subtasks=(PlanSubtask(desc="코드 작성", worker_kind="code"),))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    assert seen == ["코드 작성"]  # code subtask 가 claude(code_runner)로 라우팅됨


def test_unregistered_kind_rejected_by_controller() -> None:
    """kind_table 에 없는 worker_kind(shell) → controller reject(미등록)."""
    reg, table = build_worker_registry(
        code_runner=lambda c, w: (0, _claude_json("x"), ""),
        code_isolation=PassthroughIsolation())
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: True),
                        workdir_factory=lambda t: f"/tmp/{t}")
    ctrl = PlanController(dispatcher=orch.dispatch, kind_table=table, registry=reg,
                          plan_approver=lambda r: True, implicit_contracts=False)
    plan = BossPlan(subtasks=(PlanSubtask(desc="x", worker_kind="shell"),))
    assert ctrl.run(plan, "t1").status == PlanStatus.VALIDATION_FAILED
