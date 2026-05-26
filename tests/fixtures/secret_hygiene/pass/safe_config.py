# Group D PoC — D-1 PASS fixture (safe ENV assignment, no secrets)
# 답습: docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md §4.1
# 본 fixture 는 Tier-1 prefix / regex / alternation 패턴 0건 의무 (FP 검증).

BASE_URL = "https://example.com"
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
USER_AGENT = "group-d-poc/0.1"
