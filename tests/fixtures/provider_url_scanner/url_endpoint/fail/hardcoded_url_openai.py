# Group A 3차 PoC — E-1 FAIL fixture (OpenAI URL hardcoding)
# 답습: 사양 §7.2 — Tier-1 URL endpoint 가 src/ 코드 (.py) 에 직접 사용 시 violation

OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
AZURE_ENDPOINT = "https://my-tenant.openai.azure.com/openai/deployments"


def get_endpoints() -> list[str]:
    return [OPENAI_ENDPOINT, AZURE_ENDPOINT]
