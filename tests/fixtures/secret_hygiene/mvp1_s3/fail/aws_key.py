# S-3 detect-secrets FAIL fixture — AWSKeyDetector plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — AKIA + FAKES3NOTREAL marker (사용자 명시 답습)

# AKIA prefix (16자 access key) — AWSKeyDetector 검출 대상
AWS_ACCESS_KEY_ID = "AKIAFAKES3NOTREAL01"

# ASIA prefix (temp session token) — AWSKeyDetector 검출 대상
AWS_SESSION_KEY_ID = "ASIAFAKES3NOTREAL02"
