"""무검열 텍스트→이미지 파이프라인 — capability 경계 + 라우팅/DAG 불변식 (TDD).

답습: docs/architecture/uncensored-prompt-to-image-pipeline-design.md
  - R3: `service` kind 를 SAFE_CONSUME_KINDS 에 등록(텍스트 프롬프트 소비) — 단
    code/shell consume 은 여전히 allow_code_consume off 불변(회귀 차단).
  - R2: 라우팅 = worker_kind→kind_table 룩업. 무검열=전용 kind `prompt`, 서비스=
    전용 kind `service`(modality 는 워커 인자 — 능력축에 modality 미주입, R5).
  - R6: `service` step 은 requires_execution=False → _EXEC_SENTINEL/실행규약이
    이미지 프롬프트를 오염시키지 않음.
  - 사람 게이트: PlanApprovalRequest.mapped_aliases 가 매핑 alias 2개 노출,
    default-deny(plan_approver=None).

트랙 A — 실 LLM·HTTP 0건. dispatcher = 실 Orchestrator.dispatch + FakeWorker.
"""
from __future__ import annotations

from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import BossPlan, Contract, PlanSubtask
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.plan_controller import (
    EXECUTING_KINDS,
    SAFE_CONSUME_KINDS,
    PlanApprovalRequest,
    PlanController,
    PlanStatus,
    _EXEC_SENTINEL,
)
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import WorkerResult


class FakeWorker:
    """결정적 워커 — produces 비어있지 않은 텍스트(artifact 추출 통과)."""

    def __init__(self, alias: str) -> None:
        self.alias = alias
        self.runs: list[tuple[str, str]] = []

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        self.runs.append((prompt, workdir))
        return WorkerResult.from_cli(
            0, '{"result": "produced-text", "is_error": false}'
        )


def _build(
    workers: list[FakeWorker],
    kind_table: dict[str, str],
    *,
    approve: bool | None = True,
    allow_code_consume: bool = False,
    implicit_contracts: bool = True,
    capture: list | None = None,
):
    reg = WorkerRegistry()
    for w in workers:
        reg.register(w)
    orch = Orchestrator(
        registry=reg,
        guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: True),
        workdir_factory=lambda t: f"/tmp/ws/{t}",
    )

    def approver(req: PlanApprovalRequest) -> bool:
        if capture is not None:
            capture.append(req)
        return bool(approve)

    ctrl = PlanController(
        dispatcher=orch.dispatch,
        kind_table=kind_table,
        registry=reg,
        plan_approver=None if approve is None else approver,
        allow_code_consume=allow_code_consume,
        implicit_contracts=implicit_contracts,
    )
    return ctrl, reg


# ── R3: capability frozenset 내용 ────────────────────────────────────────────

def test_service_in_safe_consume_kinds() -> None:
    assert "service" in SAFE_CONSUME_KINDS
    assert "file" in SAFE_CONSUME_KINDS  # 기존 유지(회귀 차단)


def test_service_in_executing_kinds() -> None:
    assert "service" in EXECUTING_KINDS
    assert "code" in EXECUTING_KINDS and "shell" in EXECUTING_KINDS  # 회귀 차단


# ── R3: service 는 artifact consume 허용 (텍스트 프롬프트 소비) ────────────────

def test_service_kind_consumes_prompt_artifact() -> None:
    # 고정 2-step: prompt(produces) → service(consumes via depends_on).
    table = {"prompt": "ollama-uncensored", "service": "gengate"}
    ctrl, _ = _build(
        [FakeWorker("ollama-uncensored"), FakeWorker("gengate")], table
    )
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="의도→프롬프트 저작", worker_kind="prompt"),
        PlanSubtask(desc="프롬프트→이미지", worker_kind="service", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    # service 가 SAFE_CONSUME 이라 consume opt-in 없이도 통과
    assert out.status == PlanStatus.COMPLETED


# ── R3 회귀: code consume 은 여전히 off (allow_code_consume=False) ────────────

def test_code_kind_consume_still_blocked_off() -> None:
    table = {"prompt": "ollama-uncensored", "code": "claude"}
    ctrl, _ = _build(
        [FakeWorker("ollama-uncensored"), FakeWorker("claude")], table,
        allow_code_consume=False,
    )
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="텍스트 생성", worker_kind="prompt"),
        PlanSubtask(desc="코드가 소비", worker_kind="code", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    # code 는 SAFE_CONSUME 아님 → allow_code_consume off 면 거부(불변 유지)
    assert out.status == PlanStatus.VALIDATION_FAILED


# ── R2: 라우팅 = kind_table 룩업, mapped_aliases 2개 노출 ─────────────────────

def test_pipeline_routes_and_exposes_mapped_aliases() -> None:
    table = {"prompt": "ollama-uncensored", "service": "gengate"}
    captured: list[PlanApprovalRequest] = []
    ctrl, _ = _build(
        [FakeWorker("ollama-uncensored"), FakeWorker("gengate")], table,
        capture=captured,
    )
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="의도→프롬프트", worker_kind="prompt"),
        PlanSubtask(desc="프롬프트→이미지", worker_kind="service", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    assert len(captured) == 1
    req = captured[0]
    # 사람 게이트가 kind_table 룩업 결과(매핑 alias)를 노출
    assert req.mapped_aliases == ("ollama-uncensored", "gengate")


# ── default-deny: plan_approver=None → DENIED ────────────────────────────────

def test_pipeline_default_deny() -> None:
    table = {"prompt": "ollama-uncensored", "service": "gengate"}
    ctrl, _ = _build(
        [FakeWorker("ollama-uncensored"), FakeWorker("gengate")], table,
        approve=None,
    )
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="의도→프롬프트", worker_kind="prompt"),
        PlanSubtask(desc="프롬프트→이미지", worker_kind="service", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.DENIED


# ── R6: service step requires_execution=False → sentinel 미주입 ──────────────

def test_service_step_no_exec_sentinel_in_prompt() -> None:
    table = {"prompt": "ollama-uncensored", "service": "gengate"}
    svc = FakeWorker("gengate")
    ctrl, _ = _build([FakeWorker("ollama-uncensored"), svc], table)
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="의도→프롬프트", worker_kind="prompt"),
        # requires_execution 기본 False — 실행규약 텍스트 미주입(R6)
        PlanSubtask(desc="프롬프트→이미지", worker_kind="service", depends_on=(0,)),
    ))
    out = ctrl.run(plan, "t1")
    assert out.status == PlanStatus.COMPLETED
    # service 워커가 받은 프롬프트에 _EXEC_SENTINEL/실행규약 오염 없음
    svc_prompt = svc.runs[0][0]
    assert _EXEC_SENTINEL not in svc_prompt
    assert "실행 출력 규약" not in svc_prompt
    # 단, depends_on artifact 는 주입돼야(데이터 전달)
    assert "[artifact:" in svc_prompt
