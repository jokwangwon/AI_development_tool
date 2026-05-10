# Group A 3차 PoC — E-1 FAIL fixture (Google AI / Gemini URL hardcoding)
# 답습: 사양 §7.2 — Tier-1 URL endpoint 가 src/ 코드 (.py) 에 직접 사용 시 violation

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def gemini_endpoint(model: str) -> str:
    return f"{GEMINI_BASE_URL}/{model}:generateContent"
