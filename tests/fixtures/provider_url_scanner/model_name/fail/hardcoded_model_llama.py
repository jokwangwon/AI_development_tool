# Group A 3차 PoC — E-2 FAIL fixture (Meta Llama model name hardcoding)
# 답습: 사양 §7.4 — Tier-1 model ID 가 src/ 코드 (.py) 에 직접 사용 시 violation

LARGE_MODEL = "llama3-70b-instruct"
MEDIUM_MODEL = "llama3-8b-instruct"
LEGACY_MODEL = "llama2-13b-chat"


def llama_model(size: str) -> str:
    return LARGE_MODEL if size == "large" else MEDIUM_MODEL
