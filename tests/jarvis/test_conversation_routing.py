"""대화→작업 라우팅 분류 (발견 #UI-1) 테스트.

답습: docs/phase0/jarvis-conversation-task-routing-design-brief.md (v3)
  [[3plus1-consensus-2026-06-01-jarvis-conversation-task-routing]] (REVISE, BL-1~5).

확정 설계(§7): A3 하이브리드(규칙 1차 필터 → 작업 의심 시에만 boss.plan 1회) +
B2(항상 plan) + fail-CLOSED(BL-2). 분류·분해를 boss.plan() 1회로 통합 —
subtasks 공집합 / 파싱 실패 → chat(제안 미표출).

트랙 A: StubBoss 주입(실 ollama 0). boss.plan 미호출(잡담)·호출 1회(작업)
관찰로 A3 latency 불변식(잡담 boss 호출 0) 검증.
"""
from __future__ import annotations

from src.jarvis.boss import BossPlan, PlanSubtask, StubBoss
from src.jarvis.conversation_routing import (
    RoutingDecision,
    classify_for_routing,
    looks_like_task,
)


# ── 규칙 1차 필터 (A3-1) ──────────────────────────────────────────────
def test_looks_like_task_detects_command_keyword():
    assert looks_like_task("mathutil.py에 gcd 함수 만들어줘")
    assert looks_like_task("이 버그 좀 고쳐줘")
    assert looks_like_task("테스트 코드 작성해줘")


def test_looks_like_task_rejects_smalltalk():
    assert not looks_like_task("오늘 날씨 어때?")
    assert not looks_like_task("그냥 잡담이야")
    assert not looks_like_task("")


# ── 분류 통합 (A3-2 + B2 + fail-CLOSED) ───────────────────────────────
def test_smalltalk_skips_boss_call():
    """규칙 미통과 → boss.plan 호출 0 (A3 latency 불변식)."""
    boss = StubBoss("x", plan=BossPlan(subtasks=(PlanSubtask("a", "claude"),)))
    decision = classify_for_routing("오늘 날씨 어때?", boss)
    assert decision.is_task is False
    assert boss.plan_calls == []  # 잡담은 boss 호출 0


def test_task_with_subtasks_routes_and_calls_boss_once():
    boss = StubBoss("x", plan=BossPlan(subtasks=(PlanSubtask("gcd 작성", "claude"),)))
    decision = classify_for_routing("gcd 함수 만들어줘", boss)
    assert decision.is_task is True
    assert decision.subtask_count == 1
    assert decision.prompt == "gcd 함수 만들어줘"
    assert boss.plan_calls == ["gcd 함수 만들어줘"]  # 작업 의심 시 1회


def test_task_suspect_but_empty_plan_is_chat():
    """규칙은 통과했으나 boss 가 빈 subtasks → chat (오분류 fail-safe)."""
    boss = StubBoss("x", plan=BossPlan(subtasks=()))
    decision = classify_for_routing("내일 뭐 만들까 고민중", boss)  # '만들' 걸림
    assert decision.is_task is False
    assert decision.subtask_count == 0
    assert boss.plan_calls == ["내일 뭐 만들까 고민중"]  # 호출은 됨, 결과가 빈 plan


def test_boss_failure_fails_closed_to_chat():
    """★ BL-2: boss.plan 예외(파싱 실패·timeout 포함) → fail-CLOSED = chat."""
    boss = StubBoss("x", plan_fail=True)
    decision = classify_for_routing("gcd 함수 만들어줘", boss)
    assert decision.is_task is False  # fail-open(task 라우팅) 금지
    assert isinstance(decision, RoutingDecision)


def test_multi_subtask_still_single_plan_path():
    """B2: single/multi 구분 없이 동일 경로 — subtask N개여도 is_task=True."""
    boss = StubBoss("x", plan=BossPlan(subtasks=(
        PlanSubtask("파일 작성", "claude"),
        PlanSubtask("import 실행", "claude", depends_on=(0,), requires_execution=True),
    )))
    decision = classify_for_routing("mathutil 만들고 실행해줘", boss)
    assert decision.is_task is True
    assert decision.subtask_count == 2


# ── #UI-2 백엔드 통합 모드 판정 (classify_mode, 2-pass Pass1) ─────────
from src.jarvis.conversation_routing import ModeDecision, classify_mode, VALID_MODES


def test_classify_mode_returns_each_valid_mode():
    for m in ("chat", "note", "svg", "task"):
        d = classify_mode("입력", classifier=lambda t, _m=m: _m)
        assert isinstance(d, ModeDecision)
        assert d.mode == m


def test_classify_mode_frozen():
    import pytest
    d = classify_mode("x", classifier=lambda t: "chat")
    with pytest.raises(Exception):
        d.mode = "note"  # type: ignore


def test_classify_mode_empty_text_chat_no_call():
    called = []
    d = classify_mode("   ", classifier=lambda t: called.append(t) or "task")
    assert d.mode == "chat"          # fail-CLOSED
    assert called == []              # 빈 입력 = classifier 미호출(latency)


def test_classify_mode_classifier_raises_fail_closed_chat():
    def _boom(t):
        raise RuntimeError("ollama down")
    # 강한 동사 없는 입력(LLM 경로) → 실패 시 fail-CLOSED chat
    assert classify_mode("회의 정리해줘", classifier=_boom).mode == "chat"


def test_classify_mode_invalid_value_fail_closed_chat():
    # enum 밖 값(LLM이 엉뚱한 라벨) → chat (BL: 화이트리스트 fail-CLOSED)
    assert classify_mode("질문이요", classifier=lambda t: "diagram").mode == "chat"
    assert classify_mode("질문이요", classifier=lambda t: "").mode == "chat"
    assert classify_mode("질문이요", classifier=lambda t: None).mode == "chat"


# ⭐ 규칙 1차: 강한 생성 동사 → task (LLM 우회, #UI-2 함정 보완)
def test_classify_mode_strong_verb_forces_task_before_llm():
    called = []
    def _classifier(t):
        called.append(t)
        return "note"  # LLM이 note 라 해도
    # PoC 유일 오분류 케이스 — 규칙 1차가 task 로 보완
    d = classify_mode("계산기 만들어줘. 정리 노트에서 쓸 수 있게", classifier=_classifier)
    assert d.mode == "task"
    assert called == []  # 강한 동사 → LLM 호출 0


def test_classify_mode_weak_verb_trusts_llm_note():
    # "정리해줘"(약한 동사)는 LLM 문맥 판단에 위임 → 진짜 note 보존(회귀 방지)
    assert classify_mode("회의 내용 정리해줘", classifier=lambda t: "note").mode == "note"


def test_classify_mode_mixed_intent_task_priority():
    # 혼합의도("노트로 정리하고 코드도 짜줘") → 강한 동사(짜줘) task 우선(사용자 결정)
    assert classify_mode("노트로 정리하고 코드도 짜줘", classifier=lambda t: "note").mode == "task"


def test_valid_modes_constant():
    assert VALID_MODES == ("chat", "note", "svg", "task")
