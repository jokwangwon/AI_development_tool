# MVP-1 entry coverage — E-2 FAIL fixture (o-series + Mistral family)
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.3 sub-step 3.3
#
# 본 fixture 는 기존 model_name/fail/ (claude / gpt / gemini / llama) 가 cover 하지
# 않는 Tier-1 model 패턴 (openai-o1 / openai-o3 / mistral / mixtral / codestral) 를
# MVP-1 entry 회귀 cover. 답습 변경 0건 — Model Tier-1 19 catalog 변경 0건.

# OpenAI o-series (2 patterns: o1- / o3-)
REASONING_MODEL_LOW = "o1-mini-2024-09"
REASONING_MODEL_HIGH = "o3-pro-2025-05"

# Mistral family (3 patterns: mistral- / mixtral- / codestral-)
MISTRAL_LARGE = "mistral-large-2407"
MIXTRAL_MOE = "mixtral-8x22b-instruct"
CODE_MODEL = "codestral-22b-v0.1"


def select_reasoning_model(task: str) -> str:
    if task == "deep":
        return REASONING_MODEL_HIGH
    return REASONING_MODEL_LOW


def mistral_model_for(use_case: str) -> str:
    if use_case == "code":
        return CODE_MODEL
    if use_case == "moe":
        return MIXTRAL_MOE
    return MISTRAL_LARGE
