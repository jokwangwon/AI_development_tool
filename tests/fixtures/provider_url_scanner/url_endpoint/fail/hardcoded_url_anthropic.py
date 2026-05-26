# Group A 3차 PoC — E-1 FAIL fixture (Anthropic URL hardcoding)
# 답습: 사양 §7.2 — Tier-1 URL endpoint 가 src/ 코드 (.py) 에 직접 사용 시 violation

import urllib.request

ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"


def call_anthropic(prompt: str) -> str:
    req = urllib.request.Request(ANTHROPIC_URL, data=prompt.encode())
    return req.full_url
