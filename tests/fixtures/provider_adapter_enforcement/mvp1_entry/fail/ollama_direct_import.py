"""MVP-1 entry coverage — FAIL fixture (ollama direct import).

답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.3 sub-step 3.2.
본 fixture 는 기존 fail/ fixture (direct/from/double_underscore/dynamic/transitive/
model_name) 가 cover 하지 않는 `ollama` forbidden 모듈 direct import 를 MVP-1 entry
회귀 cover. 답습 변경 0건 — tools/provider_import_scanner.py 본문 변경 0건.

기대 결과: scanner 가 'direct-import:ollama' 보고.
"""
import ollama  # noqa: F401 (의도적 위반)


def call_ollama() -> None:
    raise NotImplementedError
