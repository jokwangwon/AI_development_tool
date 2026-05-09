"""FAIL fixture — §9.1 패턴 #1 (provider SDK 직접 import).

기대 결과: scanner 가 line 5 에서 'direct-import:openai' 보고.
"""
import openai  # noqa: F401  (의도적 위반)


def call_openai() -> None:
    raise NotImplementedError
