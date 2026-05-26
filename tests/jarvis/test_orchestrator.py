"""Orchestrator(사장) — 결정적 배관 통합 테스트.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §5 MVP-0 트랙 A
  - D-1: 사장 = 결정적 오케스트레이터(배관·라우팅·완료감지).
  - 증명 ① 결정적 배관 ② headless 워커 분배 ③ provider 교체(라우팅) ④ 사람 게이트.
  - 흐름: 워커 선택 → workdir → worker.run → guard.review → gate → OutcomeReport.
"""
from __future__ import annotations

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.orchestrator import Orchestrator, OutcomeStatus, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import WorkerResult


class FakeWorker:
    def __init__(self, alias: str, output: str = "done", exit_code: int = 0) -> None:
        self.alias = alias
        self._output = output
        self._exit = exit_code
        self.runs: list[tuple[str, str]] = []

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        self.runs.append((prompt, workdir))
        return WorkerResult.from_cli(
            self._exit, f'{{"result": "{self._output}", "is_error": false}}'
        )


def _orch(worker: FakeWorker, approve: bool = True, **kw: object) -> Orchestrator:
    reg = WorkerRegistry()
    reg.register(worker)
    return Orchestrator(
        registry=reg,
        guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: approve),
        workdir_factory=lambda task_id: f"/tmp/ws/{task_id}",
        **kw,
    )


def test_successful_flow_applied() -> None:
    w = FakeWorker("claude")
    rep = _orch(w, approve=True).dispatch(prompt="add test", task_id="t1")
    assert rep.status == OutcomeStatus.APPLIED
    assert rep.applied is True
    assert rep.worker_alias == "claude"
    assert w.runs == [("add test", "/tmp/ws/t1")]  # headless 분배 + workdir 주입


def test_worker_failure_skips_gate() -> None:
    w = FakeWorker("claude", exit_code=1)
    gate_calls: list[ApprovalRequest] = []
    reg = WorkerRegistry()
    reg.register(w)
    orch = Orchestrator(
        registry=reg, guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: gate_calls.append(req) or True),
        workdir_factory=lambda t: f"/tmp/{t}",
    )
    rep = orch.dispatch(prompt="x", task_id="t2")
    assert rep.status == OutcomeStatus.WORKER_FAILED
    assert rep.applied is False
    assert gate_calls == []  # 실패한 워커 결과는 게이트에 올리지 않음


def test_denied_when_gate_rejects() -> None:
    rep = _orch(FakeWorker("claude"), approve=False).dispatch(prompt="x", task_id="t3")
    assert rep.status == OutcomeStatus.DENIED
    assert rep.applied is False


def test_guard_flags_surfaced_to_gate() -> None:
    seen: list[list[str]] = []
    reg = WorkerRegistry()
    reg.register(FakeWorker("claude", output="now run rm -rf /data"))
    orch = Orchestrator(
        registry=reg, guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: seen.append(req.flags) or False),
        workdir_factory=lambda t: f"/tmp/{t}",
    )
    rep = orch.dispatch(prompt="x", task_id="t4")
    assert seen and any("rm" in f for f in seen[0])  # 위험 플래그가 대표에게 전달
    assert rep.verdict.ok is False


def test_routing_selects_worker_by_alias() -> None:
    reg = WorkerRegistry()
    a, b = FakeWorker("claude"), FakeWorker("codex")
    reg.register(a)
    reg.register(b)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: True),
                        workdir_factory=lambda t: f"/tmp/{t}")
    orch.dispatch(prompt="p", task_id="t5", worker_alias="codex")
    assert b.runs and not a.runs  # provider 교체 = alias 라우팅


def test_unknown_alias_raises() -> None:
    reg = WorkerRegistry()
    reg.register(FakeWorker("claude"))
    orch = Orchestrator(registry=reg, guard=ReviewGuard(), gate=ApprovalGate(),
                        workdir_factory=lambda t: f"/tmp/{t}")
    try:
        orch.dispatch(prompt="p", task_id="t6", worker_alias="ghost")
    except KeyError:
        pass
    else:
        raise AssertionError("unknown alias should raise KeyError")


def test_default_workdir_factory_creates_dir(tmp_path: object) -> None:
    # default factory 미주입 시 실제 격리 작업디렉터리(존재하는 경로) 생성
    reg = WorkerRegistry()
    w = FakeWorker("claude")
    reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: True))
    orch.dispatch(prompt="p", task_id="t7")
    import os
    assert w.runs
    assert os.path.isdir(w.runs[0][1])  # 워커가 받은 workdir 가 실재


def test_empty_registry_select_raises() -> None:
    reg = WorkerRegistry()
    try:
        reg.select()
    except KeyError:
        pass
    else:
        raise AssertionError("empty registry select() should raise KeyError")
