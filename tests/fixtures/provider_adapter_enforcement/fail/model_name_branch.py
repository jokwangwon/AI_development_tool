"""FAIL fixture — §9.1 #1 보조 (모델명 분기 코드).

기대 결과: scanner 가 'model-name-branch:claude-opus-4-7' 보고.
"""


def branch_by_model(model: str) -> str:
    if model == "claude-opus-4-7":  # 의도적 위반 — yaml alias 만 허용
        return "anthropic"
    return "default"
