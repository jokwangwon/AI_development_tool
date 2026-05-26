"""MVP-1 entry coverage — FAIL fixture (aliased import variant).

답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.3 sub-step 3.2.
본 fixture 는 `import openai as oai` 형식 (alias 사용) 가 AST scanner
visit_Import 답습 적용 시에도 검출됨을 MVP-1 entry 회귀 cover. 답습 변경 0건.

기대 결과: scanner 가 'direct-import:openai' 보고 (alias 무관 module name 답습).
"""
import openai as oai  # noqa: F401 (의도적 위반 — alias 사용해도 검출 기대)


def call_via_alias() -> None:
    _ = oai
    raise NotImplementedError
