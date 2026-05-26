# Group A 3차 PoC — E-2 FAIL fixture (OpenAI model name hardcoding)
# 답습: 사양 §7.4 — Tier-1 model ID 가 src/ 코드 (.py) 에 직접 사용 시 violation

CHAT_MODEL = "gpt-4o"
LEGACY_MODEL = "gpt-3.5-turbo"
REASONING_MODEL = "o1-preview"


def select_model(task: str) -> str:
    if task == "reasoning":
        return REASONING_MODEL
    return CHAT_MODEL
