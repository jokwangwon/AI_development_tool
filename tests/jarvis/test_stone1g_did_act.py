"""디딤돌1g — headless 워커 no-op silent pass (발견#3) did_act 신호 테스트.

답습: docs/phase0/jarvis-stone1g-headless-noop-design-brief.md (v1.1)
  [[3plus1-consensus-2026-05-31-jarvis-stone1g-headless-noop]] (REVISE 흡수).

  - 신호 = `did_act: bool|None` 추상(워커별 결정적 효과 보고). claude=num_turns>1
    (PoC 확인), ollama=content 산출 여부. provider 누출 0(헌법5조).
  - 발화 = `did_act is False ∧ requires_execution=True` → CapabilityWarning(경고,
    차단 아님 — BL-4 MVP). stdout-출력 정상작업(did_act=True) 오탐 0(BL-3/FP-5).
  - over-claim 금지(BL-6): "효과 미관측"(중립), "아무것도 안 함" 단정 아님.

트랙 A — 실 LLM·HTTP·subprocess 0건(runner/urlopen 주입).
"""
from __future__ import annotations

import io
import json
from pathlib import Path
from typing import Any
from unittest.mock import patch

from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import BossPlan, PlanSubtask
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.plan_controller import PlanController, PlanStatus
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import CliWorker, OllamaWorker, WorkerResult


# ── WorkerResult.did_act 추상 필드 (additive, 하위호환) ──────────────────────

def test_workerresult_did_act_default_none() -> None:
    """기존 생성 경로(from_cli)는 did_act 미상(None) — additive 하위호환."""
    r = WorkerResult.from_cli(0, '{"result": "x", "is_error": false}')
    assert r.did_act is None


# ── CliWorker did_act_fn 주입 — claude num_turns 프록시(PoC) ─────────────────

def _runner(stdout: str, exit_code: int = 0):
    def run(cmd: list[str], workdir: str) -> tuple[int, str, str]:
        return exit_code, stdout, ""
    return run


def _claude_json(**over: object) -> str:
    base: dict[str, Any] = {"result": "done", "is_error": False,
                            "total_cost_usd": 0.0, "num_turns": 2}
    base.update(over)
    return json.dumps(base)


def test_cliworker_did_act_true_when_num_turns_gt_1() -> None:
    """도구 사용(num_turns≥2) → did_act=True (PoC: 파일생성 작업 num_turns=2)."""
    def did_act_fn(raw: dict | None) -> bool | None:
        return raw.get("num_turns", 0) > 1 if raw else None
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  runner=_runner(_claude_json(num_turns=2)), did_act_fn=did_act_fn)
    r = w.run(prompt="create file", workdir="/tmp/ws")
    assert r.did_act is True


def test_cliworker_did_act_false_when_num_turns_eq_1() -> None:
    """텍스트-only/되묻기(num_turns=1) → did_act=False (PoC: #3 원형)."""
    def did_act_fn(raw: dict | None) -> bool | None:
        return raw.get("num_turns", 0) > 1 if raw else None
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  runner=_runner(_claude_json(num_turns=1)), did_act_fn=did_act_fn)
    r = w.run(prompt="회문 함수 정의", workdir="/tmp/ws")
    assert r.did_act is False


def test_cliworker_did_act_none_without_fn() -> None:
    """did_act_fn 미주입 → did_act=None(미상). 하위호환."""
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  runner=_runner(_claude_json(num_turns=1)))
    r = w.run(prompt="x", workdir="/tmp/ws")
    assert r.did_act is None


def test_cliworker_did_act_none_when_raw_unparsable() -> None:
    """raw 파싱 불가(is_error) → did_act_fn(None) → None. fail-soft."""
    def did_act_fn(raw: dict | None) -> bool | None:
        return raw.get("num_turns", 0) > 1 if raw else None
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  runner=_runner("not json", exit_code=0), did_act_fn=did_act_fn)
    r = w.run(prompt="x", workdir="/tmp/ws")
    assert r.is_error is True          # 파싱 불가 = 거짓 성공 금지(기존)
    assert r.did_act is None           # raw None → fn None


# ── OllamaWorker did_act — content 산출 여부 ─────────────────────────────────

def _fake_resp(content: str) -> io.BytesIO:
    payload = {"message": {"role": "assistant", "content": content}, "done": True}
    return io.BytesIO(json.dumps(payload).encode("utf-8"))


def test_ollama_did_act_true_on_content(tmp_path: Path) -> None:
    """ollama 성공(content 산출) → did_act=True."""
    w = OllamaWorker(alias="file", model="m")
    with patch("urllib.request.urlopen", side_effect=lambda req, timeout=None: _fake_resp("print('ok')")):
        r = w.run(prompt="write code", workdir=str(tmp_path))
    assert r.is_error is False
    assert r.did_act is True


# ── PlanController 발화 — did_act False ∧ requires_execution → 경고(차단 아님) ──

class _DidActWorker:
    """did_act 를 명시 설정하는 FakeWorker(트랙 A)."""

    def __init__(self, alias: str, did_act: bool | None) -> None:
        self.alias = alias
        self._did_act = did_act

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        base = WorkerResult.from_cli(0, '{"result": "ok", "is_error": false}')
        from dataclasses import replace
        return replace(base, did_act=self._did_act)


def _ctrl(worker: _DidActWorker) -> PlanController:
    reg = WorkerRegistry()
    reg.register(worker)
    orch = Orchestrator(
        registry=reg, guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: True),
        workdir_factory=lambda t: f"/tmp/ws/{t}",
    )
    return PlanController(
        dispatcher=orch.dispatch,
        kind_table={"code": worker.alias},
        registry=reg,
        plan_approver=lambda req: True,
        implicit_contracts=False,
    )


def test_noop_warning_when_did_act_false_and_requires_execution() -> None:
    """did_act=False ∧ requires_execution=True → noop 경고. 단 차단 아님(applied 유지, COMPLETED)."""
    ctrl = _ctrl(_DidActWorker("code-w", did_act=False))
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="회문 함수 정의하고 실행", worker_kind="code",
                    requires_execution=True),
    ))
    out = ctrl.run(plan, task_id="t1")
    assert out.status is PlanStatus.COMPLETED          # BL-4: 경고지 차단 아님
    assert len(out.noop_warnings) == 1                 # 효과 미관측 경고
    assert out.noop_warnings[0].subtask_index == 0
    assert "미관측" in out.noop_warnings[0].reason     # BL-6: 중립 문구


def test_no_warning_when_did_act_true() -> None:
    """did_act=True(도구 행동) → 무경고. stdout-출력 정상작업 오탐 0(BL-3/FP-5 회귀)."""
    ctrl = _ctrl(_DidActWorker("code-w", did_act=True))
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="테스트 실행하여 결과 stdout 출력", worker_kind="code",
                    requires_execution=True),
    ))
    out = ctrl.run(plan, task_id="t2")
    assert out.status is PlanStatus.COMPLETED
    assert out.noop_warnings == ()


def test_no_warning_when_requires_execution_false() -> None:
    """requires_execution=False → did_act 무관 무경고(분석/생성 작업 오탐 0)."""
    ctrl = _ctrl(_DidActWorker("code-w", did_act=False))
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="코드 생성만", worker_kind="code",
                    requires_execution=False),
    ))
    out = ctrl.run(plan, task_id="t3")
    assert out.status is PlanStatus.COMPLETED
    assert out.noop_warnings == ()


def test_no_warning_when_did_act_none() -> None:
    """did_act=None(미상 워커) → 경고 발화 안 함(false positive 금지). fs-delta fallback 별건."""
    ctrl = _ctrl(_DidActWorker("code-w", did_act=None))
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="실행 작업", worker_kind="code", requires_execution=True),
    ))
    out = ctrl.run(plan, task_id="t4")
    assert out.status is PlanStatus.COMPLETED
    assert out.noop_warnings == ()
