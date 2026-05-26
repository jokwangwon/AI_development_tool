"""Boss LLM advisory 판단 지점 — 합의(R1~R13) 불변식 고정 테스트.

답습: docs/phase0/jarvis-mvp1-local-boss-design-brief.md (v2) §3·§4·§5
  [[3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss]] APPROVE w/ COND.
  - R2: BossAdvice = 텍스트 전용 frozen(콜백·경로·명령 필드 금지), R6: confidence 삭제.
  - R7: Orchestrator(boss=None) 하위호환 + ApprovalRequest.advice 첨부 + 합집합 flag.
  - R1/fail-safe: advisory 는 결정적 flag 를 *추가*만(union), *감산* 불가.
  - R8: 워커 실패 시 advise 미호출.
  - R3: advisory 실패 = 게이트 진행 + "advisory 실패" 명시 경고(부재≠안전).
  - advisory 는 게이트를 자동 통과시키지 않는다(사람 게이트 권위 불변).

본 테스트는 StubBoss 주입으로 결정적(실 LLM 호출·HTTP·설치 0건) — 트랙 A.
"""
from __future__ import annotations

import dataclasses

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import AdviceRequest, BossAdvice, StubBoss
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


def _orch(worker: FakeWorker, approve: bool, boss: object | None) -> Orchestrator:
    reg = WorkerRegistry()
    reg.register(worker)
    return Orchestrator(
        registry=reg,
        guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: approve),
        workdir_factory=lambda task_id: f"/tmp/ws/{task_id}",
        boss=boss,
    )


# --- R2/R6: BossAdvice = 텍스트 전용 frozen, confidence 없음 ---

def test_boss_advice_is_frozen_text_only() -> None:
    adv = BossAdvice(summary="검토 요약", extra_flags=["boss-risk"])
    # frozen: 변경 불가
    try:
        adv.summary = "변조"  # type: ignore[misc]
    except dataclasses.FrozenInstanceError:
        pass
    else:
        raise AssertionError("BossAdvice must be frozen")
    fields = set(BossAdvice.__dataclass_fields__)
    # R6: confidence 삭제 / R2: 콜백·경로·명령 등 제어 필드 금지
    assert "confidence" not in fields
    assert fields <= {"summary", "extra_flags", "advisory_failed"}
    assert "summary" in fields and "extra_flags" in fields


def test_stub_boss_returns_scripted_advice() -> None:
    boss = StubBoss(name="local-stub", advice=BossAdvice("요약", ["x"]))
    out = boss.advise(AdviceRequest(prompt="p", worker_alias="claude",
                                    output="o", deterministic_flags=[]))
    assert boss.name == "local-stub"
    assert out.summary == "요약" and out.extra_flags == ["x"]


# --- R7: 하위호환 (boss=None) ---

def test_no_boss_preserves_mvp0_behavior() -> None:
    w = FakeWorker("claude")
    seen: list[ApprovalRequest] = []
    reg = WorkerRegistry()
    reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: seen.append(r) or True),
                        workdir_factory=lambda t: f"/tmp/{t}")  # boss 미주입
    rep = orch.dispatch(prompt="p", task_id="t1")
    assert rep.status == OutcomeStatus.APPLIED
    assert seen[0].advice is None  # advisory 없음 = MVP-0 그대로
    assert rep.advice is None


# --- R7: advice 첨부 + 합집합 flag ---

def test_advice_attached_and_flags_union() -> None:
    w = FakeWorker("claude", output="now run rm -rf /data")  # 결정적 flag 유발
    boss = StubBoss(name="b", advice=BossAdvice("위험해 보임", ["boss-extra"]))
    seen: list[ApprovalRequest] = []
    reg = WorkerRegistry()
    reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: seen.append(r) or True),
                        workdir_factory=lambda t: f"/tmp/{t}", boss=boss)
    orch.dispatch(prompt="p", task_id="t2")
    flags = seen[0].flags
    assert any("rm" in f for f in flags)        # 결정적 flag 유지
    assert "boss-extra" in flags                # advisory flag 추가
    assert seen[0].advice is not None and seen[0].advice.summary == "위험해 보임"


# --- R1/fail-safe: advisory 는 결정적 flag 를 감산 불가 ---

def test_advisory_cannot_remove_deterministic_flags() -> None:
    w = FakeWorker("claude", output="now run rm -rf /data")
    # 침해된 워커→Boss 가 "안전하니 승인"이라 말하고 extra_flags 0 → 그래도 결정적 flag 유지
    boss = StubBoss(name="b", advice=BossAdvice("완전히 안전, 승인하세요", []))
    seen: list[ApprovalRequest] = []
    reg = WorkerRegistry()
    reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: seen.append(r) or False),
                        workdir_factory=lambda t: f"/tmp/{t}", boss=boss)
    orch.dispatch(prompt="p", task_id="t3")
    assert any("rm" in f for f in seen[0].flags)  # advisory 가 못 지움(union, 감산 불가)


def test_flags_union_no_duplicate() -> None:
    w = FakeWorker("claude", output="sudo something")  # 'privilege-sudo' flag
    boss = StubBoss(name="b", advice=BossAdvice("권한 상승", ["privilege-sudo"]))
    seen: list[ApprovalRequest] = []
    reg = WorkerRegistry()
    reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: seen.append(r) or True),
                        workdir_factory=lambda t: f"/tmp/{t}", boss=boss)
    orch.dispatch(prompt="p", task_id="t4")
    assert seen[0].flags.count("privilege-sudo") == 1  # 중복 없음


# --- 사람 게이트 권위 불변: advisory 가 자동 승인 안 함 ---

def test_advisory_does_not_auto_approve() -> None:
    w = FakeWorker("claude")
    boss = StubBoss(name="b", advice=BossAdvice("아주 안전, 자동 승인 권장", []))
    rep = _orch(w, approve=False, boss=boss).dispatch(prompt="p", task_id="t5")
    assert rep.status == OutcomeStatus.DENIED  # boss 가 "안전"이라 해도 사람이 거부 = 거부
    assert rep.applied is False


# --- R8: 워커 실패 시 advise 미호출 ---

def test_advise_not_called_on_worker_failure() -> None:
    w = FakeWorker("claude", exit_code=1)
    boss = StubBoss(name="b", advice=BossAdvice("X", []))
    rep = _orch(w, approve=True, boss=boss).dispatch(prompt="p", task_id="t6")
    assert rep.status == OutcomeStatus.WORKER_FAILED
    assert boss.calls == []      # 실패 워커엔 advisory 미호출(비용·injection 표면 회피)
    assert rep.advice is None


# --- R3: advisory 실패 = 게이트 진행 + 명시 경고 ---

def test_advisory_failure_proceeds_with_warning() -> None:
    w = FakeWorker("claude", output="now run rm -rf /data")
    boss = StubBoss(name="b", fail=True)  # endpoint timeout/다운 모사
    seen: list[ApprovalRequest] = []
    reg = WorkerRegistry()
    reg.register(w)
    orch = Orchestrator(registry=reg, guard=ReviewGuard(),
                        gate=ApprovalGate(approver=lambda r: seen.append(r) or True),
                        workdir_factory=lambda t: f"/tmp/{t}", boss=boss)
    rep = orch.dispatch(prompt="p", task_id="t7")
    assert rep.status == OutcomeStatus.APPLIED        # advisory 부재가 차단 아님
    assert seen[0].advice is not None
    assert seen[0].advice.advisory_failed is True     # 실패 표지
    assert "실패" in seen[0].advice.summary            # 명시 경고
    assert any("rm" in f for f in seen[0].flags)      # 결정적 flag 그대로
