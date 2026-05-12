# MVP-1 entry coverage — D-1 FAIL fixture
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.1 sub-step 1.1
#
# 본 fixture 는 기존 fail/ fixture 가 baseline 5 prefix (sk- / sk-ant- / ghp_ / AKIA / xoxb-) 만
# cover 하는 한계를 MVP-1 entry 시점 회귀 보강. Tier-1 prefix 31 中 6 vendor sample cover.
# 답습 변경 0건 — Tier-1 catalog 자동 확장 0건 (R-4.1 §4.1 답습 한정).
#
# fake canary 의무 답습 (사용자 명시 — F-금지 #1):
#   모든 fake secret 은 FAKE / NOTAREAL / fakecanary / R41T marker 포함.

# T1-002 (gho_ — GitHub OAuth access token)
GITHUB_OAUTH = "gho_FAKEMVP1ENTRYNOTAREALOAUTHXX"

# T1-006 (AIza — Google API key)
GOOGLE_API = "AIzaFAKEMVP1ENTRYNOTAREALGOOGLEKEY1234"

# T1-016 (hf_ — HuggingFace token)
HF_TOKEN = "hf_FAKEMVP1ENTRYNOTAREALHUGGINGFACE"

# T1-019 (pypi- — PyPI API token)
PYPI_TOKEN = "pypi-FAKEMVP1ENTRYNOTAREALPYPIAPI"

# T1-024 (tvly- — Tavily search API)
TAVILY = "tvly-FAKEMVP1ENTRYNOTAREALTAVILY"

# T1-026 (gsk_ — Groq Cloud API key)
GROQ = "gsk_FAKEMVP1ENTRYNOTAREALGROQCLOUD"
