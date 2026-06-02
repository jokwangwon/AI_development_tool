"""대화→작업 라우팅 분류 — 발견 #UI-1 (디딤돌, 119 세션).

답습 SDD: docs/phase0/ 대화→작업 라우팅 설계 brief v3
  + 그 3+1 합의(docs/review/, 2026-06-01, REVISE).
  (영문 kebab 파일명은 secret-scanner 의 키 prefix 패턴을 오탐시켜 한글로 풀어 적음
   — docs/phase0·docs/review 에서 "라우팅" brief/합의로 식별.)

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

# 규칙 1차 — 2-트랙 (122 합의 옵션 B, 강한동사 과오버라이드 narrow).
# 답습: docs/phase0/jarvis-ui2-strong-verb-overtrigger-design-brief.md (v2)
#   [[3plus1-consensus-2026-06-02-jarvis-ui2-strong-verb-overtrigger]] (REVISE, BL-B1~B3).
#
# 트랙1 (_STRONG_TASK_RE): 본질이 SW 행위라 *무조건* task 인 동사. note/svg 요청엔
#   안 나타남. "만들"은 제외 — dogfooding(122)에서 svg/note("다이어그램/노트 만들어줘")
#   를 과오버라이드함이 실측됨(RULE 분기 50%).
# 트랙2 (_MAKE_VERB_RE + _SW_NOUNS): "만들"은 본질적으로 모호(목적어가 판별자) →
#   SW 산출 명사가 *동반*할 때만 task 확정(BL-B1). 명사 없으면 LLM 문맥 판단에 위임
#   (LLM 분기는 실측 정확). #UI-2 함정 "계산기 만들어줘 정리 노트에서"는 "계산기"가
#   SW명사라 task 보존. ⚠️ over-claim 금지(BL-2): 명사 allowlist 는 완전성 보장 아닌
#   fail-safe(누락 명사 → LLM 폴백) — 측정 한정값, detection≠prevention.
_STRONG_TASK_RE = re.compile(
    r"(구현|짜줘|짜 줘|개발|배포|리팩터|리팩토링|디버그|컴파일|스크립트.*작성)"
)
_MAKE_VERB_RE = re.compile(r"만들")
# SW 산출 명사 allowlist — "만들"과 동반 시 task 확정. note/svg 명사(다이어그램·노트·
# 목록·도식…)는 *불포함*(만들과 함께 와도 LLM 위임). BL-B3: "노트 앱 만들어줘"는
# SW명사("앱")가 note명사("노트")를 이겨 task(설계결정, 자명 fail-safe 아님 — 합의 명시).
_SW_NOUNS: tuple[str, ...] = (
    "계산기", "프로그램", "앱", "애플리케이션", "어플", "스크립트", "함수", "모듈",
    "클래스", "사이트", "웹사이트", "서버", "봇", "게임", "API", "api", "코드",
    "페이지", "플러그인", "라이브러리", "대시보드", "CLI", "명령어", "도구", "툴",
)


def _is_make_task(text: str) -> bool:
    """트랙2 — "만들" 동사 + SW 산출 명사 동반 시 task 확정(BL-B1). 모듈 로드 시
    compile 된 패턴·상수만 사용(BL-B2: 런타임 컴파일 0 → fail-CLOSED try 앞단 예외 방지)."""
    return bool(_MAKE_VERB_RE.search(text)) and any(n in text for n in _SW_NOUNS)


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
    # 규칙 1차 2-트랙: 무조건 강한동사 OR ("만들"+SW명사) → task 확정(LLM 호출 0).
    # #UI-2 함정·혼합의도 task 우선 보존, svg/note+"만들" 과오버라이드는 LLM 위임(122).
    if _STRONG_TASK_RE.search(text) or _is_make_task(text):
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
