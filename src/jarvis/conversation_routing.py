"""대화→작업 라우팅 분류 — 발견 #UI-1 (디딤돌, 119 세션).

답습: docs/phase0/jarvis-conversation-task-routing-design-brief.md (v3)
  [[3plus1-consensus-2026-06-01-jarvis-conversation-task-routing]] (REVISE).

확정 설계(§7):
  - A3 하이브리드: 규칙 1차 필터(`looks_like_task`, 0ms·결정적) → 작업 의심
    시에만 boss.plan 1회 호출. 잡담은 boss 호출 0 (latency 불변식).
  - B2 항상 plan: single/multi 구분 없음. boss.plan() 결과 subtasks≥1 이면 작업.
  - fail-CLOSED(BL-2): boss.plan 예외(호출 실패·파싱 실패·timeout) 또는 빈
    subtasks → is_task=False(chat). fail-open(불확실 시 task 라우팅) 금지.

이 모듈은 **순수 분류 로직**(부작용 0). `BossPlanner` 주입으로 트랙 A 테스트
가능(BL-5 seam). board.create/run 을 호출하지 않는다 — 신뢰 경계(BL-1)상
실제 plan 제출은 프론트가 same-origin `POST /api/jarvis/plan` 을 재호출한다.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from src.jarvis.boss import BossPlanner

# A3-1 규칙 1차 필터 — 작업 의도 키워드(명령형 동사). 약한 신호(false positive
# 허용): 통과해도 boss.plan 2차가 빈 plan 으로 거른다(fail-safe). 미통과 = 확정
# 잡담(boss 호출 0). 우선순위(BL-4): note/svg mode 판정은 프론트 detectMode 가
# *먼저* 하므로, 이 필터는 mode=='chat' 입력에만 적용된다(호출측 책임).
_TASK_KEYWORD_RE = re.compile(
    r"(해줘|해 줘|만들어|만들|작성|구현|실행|돌려|고쳐|짜줘|짜 줘|생성|추가|수정|리팩터|리팩토링|배포|테스트.*작성)"
)


def looks_like_task(text: str) -> bool:
    """규칙 1차 필터(A3-1) — 작업 의도 키워드가 있으면 True. 0ms·결정적."""
    return bool(_TASK_KEYWORD_RE.search(text or ""))


@dataclass(frozen=True)
class RoutingDecision:
    """분류 결과 — is_task=True 면 프론트가 제안 버튼 렌더. prompt = plan 입력."""

    is_task: bool
    prompt: str
    subtask_count: int


# #UI-2 백엔드 통합 모드 판정 — 2-pass Pass1 (detectMode 키워드 폐기).
# 합의 REVISE + PoC: 단일 결합 호출은 svg 88~99초로 사용 불가 → 분류-전용(1.1초)
# 후 기존 생성 경로 재사용(2-pass). VALID_MODES 화이트리스트 밖/실패 → chat(fail-CLOSED).
VALID_MODES = ("chat", "note", "svg", "task")

# 규칙 1차(브리프 §5-1 + PoC): 강한 *소프트웨어 생성* 동사 = 명확한 task. note/svg
# 요청엔 안 나타남("회의 정리해줘"·"흐름도 그려줘"엔 없음) → 이 동사가 있으면 LLM 분류
# 전에 task 확정(PoC 분류-전용 유일 오분류 "계산기 만들어줘 정리 노트에서"=#UI-2 함정
# 보완 + 혼합의도 task 우선 결정). 약한 동사(해줘/정리)는 LLM 문맥 판단에 위임.
_STRONG_TASK_RE = re.compile(
    r"(만들|구현|짜줘|짜 줘|개발|배포|리팩터|리팩토링|디버그|컴파일|스크립트.*작성)"
)


@dataclass(frozen=True)
class ModeDecision:
    """4-way 모드 분류 결과. mode ∈ VALID_MODES."""

    mode: str


def classify_mode(text: str, classifier) -> ModeDecision:
    """raw message → 4-way mode (chat/note/svg/task). 2-pass Pass1.

    classifier(text)->str 주입(seam) = LLM 분류-전용 호출(format=mode enum). 순수 로직:
    빈 입력 → chat(classifier 미호출, latency). 예외/enum 밖/빈값 → chat(BL-2 fail-CLOSED,
    BL-ε 화이트리스트). detectMode 키워드 정규식을 대체 — 명사/명령 문맥 구분(#UI-2).
    """
    text = (text or "").strip()
    if not text:
        return ModeDecision("chat")
    # 규칙 1차: 강한 생성 동사 → task 확정(LLM 호출 0, #UI-2 함정·혼합의도 task 우선).
    if _STRONG_TASK_RE.search(text):
        return ModeDecision("task")
    try:
        mode = classifier(text)
    except Exception:  # noqa: BLE001 — fail-CLOSED: 분류 실패 → chat(부작용 0 안전)
        return ModeDecision("chat")
    if mode not in VALID_MODES:
        return ModeDecision("chat")
    return ModeDecision(mode)


def classify_for_routing(text: str, planner: BossPlanner) -> RoutingDecision:
    """대화 텍스트 → 라우팅 결정 (A3 + B2 + fail-CLOSED).

    1. 규칙 미통과(확정 잡담) → boss 호출 0, is_task=False.
    2. 작업 의심 → planner.plan(text) 1회. 예외 → fail-CLOSED(chat).
    3. subtasks≥1 → is_task=True. 빈 subtasks → chat(fail-safe).
    """
    text = (text or "").strip()
    if not text or not looks_like_task(text):
        return RoutingDecision(is_task=False, prompt=text, subtask_count=0)
    try:
        plan = planner.plan(text)
    except Exception:  # noqa: BLE001 — fail-CLOSED(BL-2): 어떤 실패든 chat 로
        return RoutingDecision(is_task=False, prompt=text, subtask_count=0)
    count = len(plan.subtasks)
    return RoutingDecision(is_task=count >= 1, prompt=text, subtask_count=count)
