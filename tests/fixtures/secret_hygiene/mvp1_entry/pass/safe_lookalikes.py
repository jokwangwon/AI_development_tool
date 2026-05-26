# MVP-1 entry coverage — D-1 PASS fixture (FP-resistance 회귀 보강)
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.1 sub-step 1.1
#
# 본 fixture 는 Tier-1 패턴 lookalike (정상 식별자 / 변수명 / docstring) 가
# FP 를 일으키지 않음을 MVP-1 entry 시점 회귀 보강. 답습 변경 0건.
#
# 본 fixture 위반 = 0건 의무 (D-1 PASS scan rc=0 + violations=0 답습).

# 정상 docstring (자주 sk / api / token 단어 사용)
"""Example module docstring.

This file demonstrates safe identifiers using sk and api token concepts
without any fake secret prefix patterns that should trigger detection.
"""

# 변수명 only (값 없음) — sk_ / ghp_ 등 prefix 어떤 변수명도 사용하지 않음
mock_placeholder = None
empty_value = ""
identifier_documentation = "see docs/architecture/* for identifier model definitions"

# 짧은 식별자 (prefix 패턴 길이 미만 → 미발화)
short_id = "sk-x"
short_aws = "AKIA0001"  # only 4 digits, 16자 미만 → AKIA[A-Z0-9]{16} 미발화

# 정상 URL (userinfo 없음)
DOC_URL = "https://docs.example.com/path?ref=normal"
API_BASE = "https://api.example.com/v1"

# 정상 JSON-like (sensitive key 없음)
NORMAL_CONFIG = {"name": "example", "version": "0.1", "max_retries": 3}
