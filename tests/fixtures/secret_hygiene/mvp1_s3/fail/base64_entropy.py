# S-3 detect-secrets FAIL fixture — Base64HighEntropyString plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — high entropy Base64 string (decoded = random bytes, not real secret)

# High entropy Base64 string (>4.5 bits/char) — Base64HighEntropyString 검출 대상
# 본 string = "0123456789abcdef..." 의 random base64 encoded, 실 secret 0
HIGH_ENTROPY_BASE64 = "Zk5xN3JZb1ZwUjVYbU5oQjJBdEdpc09qVEFmS3o0R3Q3Sg=="

# 추가 high entropy fixture
ANOTHER_BASE64 = "VGhpc0lzRkFLRVMzTm90QVJlYWxTZWNyZXRCYXNlNjRYWA=="
