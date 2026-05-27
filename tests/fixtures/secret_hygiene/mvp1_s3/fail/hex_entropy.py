# S-3 detect-secrets FAIL fixture — HexHighEntropyString plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — high entropy Hex string (실 secret 0)

# High entropy Hex string (>3 bits/char) — HexHighEntropyString 검출 대상
# 본 string = random hex, 실 secret 0
HIGH_ENTROPY_HEX = "a3f5d8c2b9e7f1a4d6c8b5e2f9a1d4c7b3e6f8a2d5c9b4e1f7a8d3c6b9e2f5a1"

# 추가 high entropy hex fixture
ANOTHER_HEX = "fakes3notrealf1e2d3c4b5a69788776655443322110099887766554433221100"
