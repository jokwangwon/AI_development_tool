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


def test_bossplan_holds_subtasks_and_contracts() -> None:
    # 디딤돌1b: contracts 추가(1a 하위호환 기본 ()). means 틀 필드는 여전히 부재.
    fields = {f.name for f in dataclasses.fields(BossPlan)}
    assert fields == {"subtasks", "contracts"}
    forbidden = {"argv", "cmd", "command", "path", "workdir", "alias", "isolation"}
    assert fields & forbidden == set()


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


def test_ollama_boss_plan_parses_contracts() -> None:
    """디딤돌1b: plan 응답의 contracts(선택) 파싱 → BossPlan.contracts."""
    import json as _json
    from unittest.mock import patch

    from src.jarvis.boss import Contract, OllamaBoss

    boss = OllamaBoss(model="m1")
    content = _json.dumps({
        "subtasks": [
            {"desc": "백엔드", "worker_kind": "file", "depends_on": []},
            {"desc": "프론트", "worker_kind": "file", "depends_on": [0]},
        ],
        "contracts": [{"name": "api_schema", "produced_by": 0}],
    })
    with patch("urllib.request.urlopen",
               return_value=_fake_resp({"message": {"content": content}})):
        out = boss.plan("앱")
    assert out.contracts == (Contract(name="api_schema", produced_by=0),)


def test_ollama_boss_plan_no_contracts_is_empty() -> None:
    """1a 하위호환: contracts 없으면 빈 tuple(전달 0)."""
    import json as _json
    from unittest.mock import patch

    from src.jarvis.boss import OllamaBoss

    boss = OllamaBoss(model="m1")
    content = _json.dumps({"subtasks": [
        {"desc": "a", "worker_kind": "file", "depends_on": []}]})
    with patch("urllib.request.urlopen",
               return_value=_fake_resp({"message": {"content": content}})):
        out = boss.plan("x")
    assert out.contracts == ()


# --- 디딤돌1e: HumanPlanner (사람 직접 plan 공급, CN-1~6) ---

def test_human_planner_satisfies_protocol() -> None:
    """BossPlanner Protocol 의 세 번째 구현(사람 = plan 공급원 극단)."""
    from src.jarvis.boss import HumanPlanner

    assert isinstance(HumanPlanner(BossPlan(subtasks=())), BossPlanner)


def test_human_planner_returns_supplied_plan_ignoring_prompt() -> None:
    """(B) 객체 직접 + Q5 prompt 무시 — 사전 plan 그대로(서명 호환만)."""
    from src.jarvis.boss import HumanPlanner

    scripted = BossPlan(subtasks=(
        PlanSubtask(desc="백엔드 API", worker_kind="code", depends_on=()),
        PlanSubtask(desc="프론트", worker_kind="code", depends_on=(0,)),
    ))
    hp = HumanPlanner(scripted)
    assert hp.plan("아무 작업 지시") is scripted
    assert hp.plan("전혀 다른 지시") is scripted  # prompt 무관 동일(무시)


def test_human_planner_has_no_observation_fields() -> None:
    """CN-5: StubBoss(테스트 stub)와 달리 관찰필드 부재 = 프로덕션 공급원."""
    from src.jarvis.boss import HumanPlanner

    hp = HumanPlanner(BossPlan(subtasks=()))
    assert not hasattr(hp, "plan_calls")  # StubBoss 는 보유(boss.py:164)
    assert not hasattr(hp, "fail")
    assert not hasattr(hp, "plan_fail")


def test_human_planner_from_file_parses(tmp_path) -> None:
    """(A) 파일 — _PLAN_JSON_SCHEMA 동일 shape JSON → BossPlan(contracts 포함)."""
    import json as _json

    from src.jarvis.boss import Contract, HumanPlanner

    p = tmp_path / "plan.json"
    p.write_text(_json.dumps({
        "subtasks": [
            {"desc": "백엔드", "worker_kind": "code", "depends_on": []},
            {"desc": "프론트", "worker_kind": "code", "depends_on": [0]},
        ],
        "contracts": [{"name": "api_schema", "produced_by": 0}],
    }), encoding="utf-8")
    out = HumanPlanner.from_file(str(p)).plan("x")
    assert len(out.subtasks) == 2
    assert out.subtasks[1].depends_on == (0,)
    assert out.contracts == (Contract(name="api_schema", produced_by=0),)


def test_human_planner_from_file_strips_fences(tmp_path) -> None:
    """CN-3: 사람이 ```json 으로 감싼 plan 도 흡수(fence-strip 답습)."""
    from src.jarvis.boss import HumanPlanner

    p = tmp_path / "plan.json"
    p.write_text(
        '```json\n{"subtasks": [{"desc": "a", "worker_kind": "file", '
        '"depends_on": []}]}\n```',
        encoding="utf-8")
    out = HumanPlanner.from_file(str(p)).plan("x")
    assert len(out.subtasks) == 1
    assert out.subtasks[0].worker_kind == "file"


def test_human_planner_from_file_missing_raises(tmp_path) -> None:
    """CN-3: 파일 없음 → RuntimeError(run_from_planner PLAN_UNAVAILABLE 정합)."""
    from src.jarvis.boss import HumanPlanner

    with pytest.raises(RuntimeError):
        HumanPlanner.from_file(str(tmp_path / "nonexistent.json"))


def test_human_planner_from_file_empty_raises(tmp_path) -> None:
    """CN-3: 빈/공백 파일 → RuntimeError(거짓 진행 금지)."""
    from src.jarvis.boss import HumanPlanner

    p = tmp_path / "empty.json"
    p.write_text("   \n  ", encoding="utf-8")
    with pytest.raises(RuntimeError):
        HumanPlanner.from_file(str(p))


def test_human_planner_from_file_malformed_raises(tmp_path) -> None:
    """CN-3: 잘못된 JSON → RuntimeError(단일 타입 수렴, _parse_bossplan 위임)."""
    from src.jarvis.boss import HumanPlanner

    p = tmp_path / "bad.json"
    p.write_text("{not valid json", encoding="utf-8")
    with pytest.raises(RuntimeError):
        HumanPlanner.from_file(str(p))


def test_human_planner_from_file_decode_error_raises(tmp_path) -> None:
    """CN-3: UTF-8 디코딩 실패(바이너리) → RuntimeError."""
    from src.jarvis.boss import HumanPlanner

    p = tmp_path / "bin.json"
    p.write_bytes(b"\xff\xfe\x00\x01garbage")
    with pytest.raises(RuntimeError):
        HumanPlanner.from_file(str(p))
