"""MVP-1 entry coverage — FAIL fixture (google.generativeai from-import).

답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.3 sub-step 3.2.
본 fixture 는 scanner 의 `google.generativeai` 특수 처리 분기 (`_matches_forbidden`
top-level google 차단 — line 56) 를 MVP-1 entry 회귀 cover. 답습 변경 0건.

기대 결과: scanner 가 'from-import:google' 보고.
"""
from google.generativeai import GenerativeModel  # noqa: F401 (의도적 위반)


def make_gemini() -> None:
    raise NotImplementedError
