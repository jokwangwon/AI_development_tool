"""FAIL fixture — §9.4 동적 import (__import__).

기대 결과: scanner 가 'double-underscore-import:openai' 보고.
"""


def covert_load() -> object:
    return __import__("openai")  # 의도적 위반
