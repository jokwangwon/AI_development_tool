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
from src.jarvis.worker_setup import (
    build_uncensored_pipeline_registry,
    build_worker_registry,
)


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


def test_code_worker_did_act_wired_from_num_turns() -> None:
    """디딤돌1g — build_worker_registry 가 claude did_act_fn(num_turns>1) 배선."""
    reg, _ = build_worker_registry(
        code_runner=lambda cmd, wd: (
            0, '{"result": "x", "is_error": false, "num_turns": 2}', ""),
        code_isolation=PassthroughIsolation())
    assert reg.select("claude").run("작업", "/tmp/ws").did_act is True  # 도구 행동


def test_code_worker_did_act_false_when_num_turns_1() -> None:
    """num_turns=1(텍스트-only/되묻기 #3 원형) → did_act=False."""
    reg, _ = build_worker_registry(
        code_runner=lambda cmd, wd: (
            0, '{"result": "ask?", "is_error": false, "num_turns": 1}', ""),
        code_isolation=PassthroughIsolation())
    assert reg.select("claude").run("회문 함수 정의", "/tmp/ws").did_act is False


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


# ── 무검열 텍스트→이미지 파이프라인 빌더 (R2/R5/R7) ──────────────────────────
# 답습: docs/architecture/uncensored-prompt-to-image-pipeline-design.md §3.1

def test_uncensored_pipeline_table_structure() -> None:
    """전용 kind_table: prompt→ollama-uncensored, service→gengate (R2)."""
    reg, table = build_uncensored_pipeline_registry()
    assert table == {"prompt": "ollama-uncensored", "service": "gengate"}
    assert reg.select("ollama-uncensored").alias == "ollama-uncensored"
    assert reg.select("gengate").alias == "gengate"


def test_uncensored_model_default_dolphin3() -> None:
    """무검열 LLM 워커 기본 모델 = dolphin3 (수단=사용자 영역, 교체 가능)."""
    reg, _ = build_uncensored_pipeline_registry()
    w = reg.select("ollama-uncensored")
    assert w._model == "dolphin3"  # noqa: SLF001 (배선 검증)


def test_uncensored_model_overridable() -> None:
    """Provider Liquidity(헌법5조): model 교체 = 인자 1개."""
    reg, _ = build_uncensored_pipeline_registry(uncensored_model="other-uncensored")
    assert reg.select("ollama-uncensored")._model == "other-uncensored"  # noqa: SLF001


def test_gengate_base_url_default_localhost_8770() -> None:
    """gen_gate 기본 base_url = 127.0.0.1:8770 (실측 README), localhost 강제."""
    reg, _ = build_uncensored_pipeline_registry()
    w = reg.select("gengate")
    assert "127.0.0.1:8770" in w._base_url  # noqa: SLF001


def test_gengate_rejects_external_base_url() -> None:
    """R7: 외부 base_url 주입 시 빌더가 fail-fast(SSRF 차단)."""
    import pytest

    with pytest.raises(ValueError):
        build_uncensored_pipeline_registry(gengate_base_url="http://evil.com:8770")


def test_uncensored_system_prompt_injected() -> None:
    """prompt_lab 템플릿이 dolphin3 system_prompt 를 주입(무검열 저작 유도)."""
    reg, _ = build_uncensored_pipeline_registry(
        uncensored_system_prompt="You write vivid image prompts."
    )
    w = reg.select("ollama-uncensored")
    assert w._system_prompt == "You write vivid image prompts."  # noqa: SLF001


def test_image_unit_and_opts_passed_to_gengate() -> None:
    """이미지 모델(unit)·스타일 opts 교체 = 인자(Provider Liquidity, R5)."""
    reg, _ = build_uncensored_pipeline_registry(
        image_unit="illustrious-xl", image_opts={"style": "anime-illustration"}
    )
    w = reg.select("gengate")
    assert w._unit == "illustrious-xl"  # noqa: SLF001
    assert w._opts == {"style": "anime-illustration"}  # noqa: SLF001
