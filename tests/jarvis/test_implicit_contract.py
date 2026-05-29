"""디딤돌1c — depends_on 암묵 contract 불변식 고정 테스트.

답습: docs/phase0/jarvis-stone1c-implicit-contract-design-brief.md (v1.1)
  [[3plus1-consensus-2026-05-30-jarvis-stone1c-implicit-contract]] (AWC).
  - 하네스 흡수: boss Contract 미생성(dogfooding)이어도 depends_on 으로 전달.
  - Q1 기본 on + opt-out(implicit_contracts=False=1b 복원).
  - Q2 transitive 통일(명시와 동일 _transitive_dependents).
  - Q3 합집합 + dedup((produced_by, consumer) 키, 명시 커버 시 암묵 suppress).
  - Q4 암묵 name = subtask_{produced_by}.
  - BL-1 능력 경계: 암묵분도 code consume = opt-in reject.
  - BL-4 계획 게이트에 합성 암묵 contract 표시(implicit_contracts 필드).

트랙 A — 실 LLM·HTTP 0건.
"""
from __future__ import annotations

import json as _json

from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import BossPlan, Contract, PlanSubtask
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.plan_controller import PlanApprovalRequest, PlanController, PlanStatus
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import WorkerResult


class FakeWorker:
    def __init__(self, alias: str, outputs: dict[str, str] | None = None) -> None:
        self.alias = alias
        self._outputs = outputs or {}
        self.runs: list[tuple[str, str]] = []

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        self.runs.append((prompt, workdir))
        first = prompt.split("\n", 1)[0]
        out = self._outputs.get(first, "ok")
        return WorkerResult.from_cli(
            0, '{"result": %s, "is_error": false}' % _json.dumps(out, ensure_ascii=False))


def _build(workers, kind_table, *, implicit=True, allow_code=False,
           approver=None, ledger=None):
    reg = WorkerRegistry()
    for w in workers:
        reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: True),
                        workdir_factory=lambda t: f"/tmp/ws/{t}")
    ctrl = PlanController(
        dispatcher=orch.dispatch, kind_table=kind_table, registry=reg,
        plan_approver=approver or (lambda r: True),
        implicit_contracts=implicit, allow_code_consume=allow_code, ledger=ledger,
    )
    return ctrl, reg


# --- 암묵 발동: contracts=() 인데 depends_on 으로 전달 (dogfooding 해결) ---

def test_implicit_injection_without_explicit_contract() -> None:
    w = FakeWorker("ollama", outputs={"백엔드": "GET /users"})
    ctrl, _ = _build([w], {"file": "ollama"})
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="백엔드", worker_kind="file"),
        PlanSubtask(desc="프론트", worker_kind="file", depends_on=(0,)),
    ))  # contracts=() — boss 가 Contract 안 냄(dogfooding)
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    # 암묵 contract 로 [0] 산출물이 [1] 에 주입(Q4 name=subtask_0)
    assert "[artifact:subtask_0]" in w.runs[1][0]
    assert "GET /users" in w.runs[1][0]
    assert "[artifact:" not in w.runs[0][0]


def test_implicit_off_restores_1b_no_injection() -> None:
    w = FakeWorker("ollama")
    ctrl, _ = _build([w], {"file": "ollama"}, implicit=False)
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="a", worker_kind="file"),
        PlanSubtask(desc="b", worker_kind="file", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    assert w.runs[1][0] == "b"  # opt-out = 1b 명시-only(주입 0)


def test_implicit_transitive() -> None:
    """Q2: 0→1→2, contracts=() → [1],[2] 모두 subtask_0 주입(transitive)."""
    w = FakeWorker("ollama", outputs={"root": "ART0"})
    ctrl, _ = _build([w], {"file": "ollama"})
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="root", worker_kind="file"),
        PlanSubtask(desc="mid", worker_kind="file", depends_on=(0,)),
        PlanSubtask(desc="leaf", worker_kind="file", depends_on=(1,)),
    ))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    assert "[artifact:subtask_0]" in w.runs[1][0]
    assert "[artifact:subtask_0]" in w.runs[2][0]  # transitive


def test_implicit_dedup_with_explicit() -> None:
    """Q3: 명시 contract 가 (0,1) 커버 → 암묵 suppress(이중 주입 0)."""
    w = FakeWorker("ollama", outputs={"산출": "DATA"})
    ctrl, _ = _build([w], {"file": "ollama"})
    plan = BossPlan(
        subtasks=(
            PlanSubtask(desc="산출", worker_kind="file"),
            PlanSubtask(desc="소비", worker_kind="file", depends_on=(0,)),
        ),
        contracts=(Contract(name="api", produced_by=0),),  # 명시
    )
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    consume = w.runs[1][0]
    assert "[artifact:api]" in consume          # 명시 name 사용
    assert "[artifact:subtask_0]" not in consume  # 암묵 dedup(중복 0)
    assert consume.count("DATA") == 1            # 이중 주입 0


# --- BL-1 능력 경계: 암묵분도 code consume opt-in ---

def test_implicit_code_consume_rejected_by_default() -> None:
    w_o = FakeWorker("ollama")
    w_c = FakeWorker("claude")
    ctrl, _ = _build([w_o, w_c], {"file": "ollama", "code": "claude"})
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="산출", worker_kind="file"),
        PlanSubtask(desc="코드 소비", worker_kind="code", depends_on=(0,)),
    ))  # 암묵 + code consume
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.VALIDATION_FAILED  # 능력 경계(opt-in 필요)


def test_implicit_code_consume_allowed_with_opt_in() -> None:
    w_o = FakeWorker("ollama", outputs={"산출": "D"})
    w_c = FakeWorker("claude")
    ctrl, _ = _build([w_o, w_c], {"file": "ollama", "code": "claude"}, allow_code=True)
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="산출", worker_kind="file"),
        PlanSubtask(desc="코드 소비", worker_kind="code", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    assert "[artifact:subtask_0]" in w_c.runs[0][0]


# --- BL-4 계획 게이트에 합성 암묵 contract 표시 ---

def test_plan_gate_shows_implicit_contracts() -> None:
    seen: list[PlanApprovalRequest] = []
    w = FakeWorker("ollama")
    ctrl, _ = _build([w], {"file": "ollama"}, approver=lambda r: seen.append(r) or True)
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="a", worker_kind="file"),
        PlanSubtask(desc="b", worker_kind="file", depends_on=(0,)),
    ))
    ctrl.run(plan, "t1")
    assert len(seen) == 1
    # 합성 암묵 contract 가 게이트에 표시(명시와 구분, BL-4)
    impl = seen[0].implicit_contracts
    assert any(c.produced_by == 0 and c.name == "subtask_0" for c in impl)
    assert seen[0].contracts == ()  # boss 명시분은 비어있음(구분)
