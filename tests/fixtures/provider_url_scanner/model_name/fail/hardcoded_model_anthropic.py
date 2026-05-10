# Group A 3차 PoC — E-2 FAIL fixture (Anthropic model name hardcoding)
# 답습: 사양 §7.4 — Tier-1 model ID 가 src/ 코드 (.py) 에 직접 사용 시 violation

PRIMARY_MODEL = "claude-opus-4-1-20250805"
FALLBACK_MODEL = "claude-sonnet-4-5"
LEGACY_MODEL = "claude-3-5-sonnet-20241022"


def get_model_for(use_case: str) -> str:
    return PRIMARY_MODEL if use_case == "complex" else FALLBACK_MODEL
