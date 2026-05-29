"""boss.plan() — 디딤돌1a untrusted planner 불변식 고정 테스트.

답습: docs/phase0/jarvis-stone1a-plan-then-execute-design-brief.md (v1.2) §2
  [[3plus1-consensus-2026-05-29-jarvis-stone1a-plan-then-execute]] (REVISE 흡수).
  - PLAN-INV: BossPlan 은 (a) means 의 *틀*(argv·alias·isolation) 필드 부재
    (b) controller 검증 거쳐야만 소비 (c) non-adaptive(워커 결과 환류 0).
  - IN-2: plan() 은 advise() 와 별개 Protocol(BossPlanner) — plan 공급원 유연
    (사람/frontier worker 도 plan 공급 가능). StubBoss 는 둘 다 구현(트랙 A).
  - BL-4: plan() 은 BossAdvice(R2 텍스트 전용)가 아니라 새 판단 지점.
  - §2 실패: plan 호출 실패 = 예외(controller 가 중단으로 변환, 거짓 진행 금지).

본 테스트는 StubBoss 주입으로 결정적(실 LLM 호출·HTTP·설치 0건) — 트랙 A.
"""
from __future__ import annotations

import dataclasses

import pytest

from src.jarvis.boss import BossPlan, BossPlanner, PlanSubtask, StubBoss


# --- PLAN-INV (a): BossPlan/PlanSubtask = frozen, means 틀 필드 부재 ---

def test_plan_subtask_is_frozen() -> None:
    st = PlanSubtask(desc="백엔드 API", worker_kind="code", depends_on=())
    with pytest.raises(dataclasses.FrozenInstanceError):
        st.desc = "변조"  # type: ignore[misc]


def test_bossplan_is_frozen() -> None:
    plan = BossPlan(subtasks=(PlanSubtask(desc="x", worker_kind="code"),))
    with pytest.raises(dataclasses.FrozenInstanceError):
        plan.subtasks = ()  # type: ignore[misc]


def test_plan_subtask_has_no_means_frame_fields() -> None:
    """means 의 *틀*(argv·path·cmd·workdir·alias·isolation) 필드 부재 — PLAN-INV (a).

    boss 는 desc(=worker prompt)·worker_kind·depends_on 만 제안. argv prefix·
    alias·격리 backend 는 harness table 소유(§5) — schema 에 표현 불가.
    """
    fields = {f.name for f in dataclasses.fields(PlanSubtask)}
    assert fields == {"desc", "worker_kind", "depends_on"}
    forbidden = {"argv", "cmd", "command", "path", "workdir", "alias",
                 "isolation", "backend", "exec"}
    assert fields & forbidden == set()


def test_bossplan_only_holds_subtasks() -> None:
    fields = {f.name for f in dataclasses.fields(BossPlan)}
    assert fields == {"subtasks"}


# --- IN-2: BossPlanner Protocol, StubBoss 구현 ---

def test_stubboss_satisfies_bossplanner_protocol() -> None:
    boss = StubBoss(name="local", plan=BossPlan(subtasks=()))
    assert isinstance(boss, BossPlanner)


def test_stubboss_plan_returns_scripted() -> None:
    scripted = BossPlan(subtasks=(
        PlanSubtask(desc="백엔드 REST API", worker_kind="code", depends_on=()),
        PlanSubtask(desc="프론트 폼", worker_kind="code", depends_on=(0,)),
    ))
    boss = StubBoss(name="local", plan=scripted)
    out = boss.plan("앱 만들어줘")
    assert out is scripted
    assert boss.plan_calls == ["앱 만들어줘"]  # 호출 관찰


def test_stubboss_plan_fail_raises() -> None:
    """§2 실패: plan 호출 실패 = 예외(controller 가 중단으로 변환)."""
    boss = StubBoss(name="local", plan_fail=True)
    with pytest.raises(RuntimeError):
        boss.plan("x")


def test_stubboss_advise_and_plan_independent() -> None:
    """IN-2: advise(BossLLM) 와 plan(BossPlanner) 는 별개 — StubBoss 는 둘 다.

    plan 미주입(None)이어도 advise 는 동작 — plan 공급원 유연성(boss 고정 아님).
    """
    from src.jarvis.boss import BossAdvice, BossLLM

    boss = StubBoss(name="local", advice=BossAdvice(summary="ok"))
    assert isinstance(boss, BossLLM)      # advise 구현
    assert isinstance(boss, BossPlanner)  # plan 도 구현(StubBoss 는 통합 stub)


# --- OllamaBoss.plan() — 트랙 B(format grammar). 실 HTTP 0건(urlopen monkeypatch) ---

def _fake_resp(payload: dict) -> "object":
    import io
    import json as _json
    return io.BytesIO(_json.dumps(payload).encode("utf-8"))


def test_ollama_boss_satisfies_planner_protocol() -> None:
    from src.jarvis.boss import OllamaBoss

    assert isinstance(OllamaBoss(model="m1"), BossPlanner)


def test_ollama_boss_plan_parses_and_sends_format_schema() -> None:
    import json as _json
    from unittest.mock import patch

    from src.jarvis.boss import OllamaBoss

    boss = OllamaBoss(model="m1")
    content = _json.dumps({"subtasks": [
        {"desc": "백엔드", "worker_kind": "code", "depends_on": []},
        {"desc": "프론트", "worker_kind": "code", "depends_on": [0]},
    ]})
    captured: dict = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = _json.loads(req.data.decode("utf-8"))
        return _fake_resp({"message": {"content": content}, "done": True})

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        out = boss.plan("앱 만들어줘")

    assert isinstance(out, BossPlan)
    assert len(out.subtasks) == 2
    assert out.subtasks[1].depends_on == (0,)        # list→tuple
    assert "format" in captured["data"]              # grammar schema 송신
    assert captured["data"]["format"]["type"] == "object"


def test_ollama_boss_plan_malformed_content_raises() -> None:
    from unittest.mock import patch

    from src.jarvis.boss import OllamaBoss

    boss = OllamaBoss(model="m1")
    with patch("urllib.request.urlopen",
               return_value=_fake_resp({"message": {"content": "not json at all"}})):
        with pytest.raises(RuntimeError):
            boss.plan("x")
