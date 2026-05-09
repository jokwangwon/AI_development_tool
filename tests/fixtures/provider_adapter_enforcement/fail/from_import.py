"""FAIL fixture — §9.1 패턴 #1 (from-import 변형).

기대 결과: scanner 가 line 5 에서 'from-import:anthropic' 보고.
"""
from anthropic import Anthropic  # noqa: F401  (의도적 위반)


def make_client() -> None:
    raise NotImplementedError
