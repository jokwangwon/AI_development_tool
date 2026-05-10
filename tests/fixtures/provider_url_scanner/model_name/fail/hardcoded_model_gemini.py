# Group A 3차 PoC — E-2 FAIL fixture (Google Gemini model name hardcoding)
# 답습: 사양 §7.4 — Tier-1 model ID 가 src/ 코드 (.py) 에 직접 사용 시 violation

PRIMARY_MODEL = "gemini-1.5-pro"
FAST_MODEL = "gemini-1.5-flash"
NEXT_GEN_MODEL = "gemini-2.0-flash"


def gemini_model(use_case: str) -> str:
    return PRIMARY_MODEL if use_case == "long_context" else FAST_MODEL
