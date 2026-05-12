# MVP-1 entry coverage — E-1 FAIL fixture (remaining 6 vendors)
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.3 sub-step 3.3
#
# 본 fixture 는 기존 url_endpoint/fail/ (anthropic / openai / google) 가 cover 하지
# 않는 Tier-1 URL endpoint 6 vendor (replicate / perplexity / cohere / huggingface /
# together / openrouter) 를 MVP-1 entry 회귀 cover. 답습 변경 0건 —
# tools/provider_url_scanner.py URL Tier-1 10 catalog 변경 0건.

REPLICATE_URL = "https://api.replicate.com/v1/predictions"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
COHERE_URL = "https://api.cohere.com/v1/generate"
HUGGINGFACE_URL = "https://api-inference.huggingface.co/models/some-model"
TOGETHER_URL = "https://api.together.xyz/inference"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def list_vendor_endpoints() -> list[str]:
    return [
        REPLICATE_URL,
        PERPLEXITY_URL,
        COHERE_URL,
        HUGGINGFACE_URL,
        TOGETHER_URL,
        OPENROUTER_URL,
    ]
