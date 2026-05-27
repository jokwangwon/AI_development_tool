# S-3 detect-secrets FAIL fixture — AWSKeyDetector plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — AKIA + 16자 (총 20자) marker (사용자 명시 답습)
#
# 수정 이력 (31번째 entry, 첫 PR evidence 수집 시점):
#   - v1 (4451716): "AKIAFAKES3NOTREAL01" (19자) + "ASIAFAKES3NOTREAL02" (19자, ASIA) → AWSKeyDetector regex 미충족 = check FAIL
#   - v2 (본 commit): "AKIA + 16자 정확 format" (총 20자) + ASIA 제거 (detect-secrets AWSKeyDetector regex `AKIA[0-9A-Z]{16}` 답습)

# AKIA prefix + 16자 [0-9A-Z] (총 20자) — AWSKeyDetector regex `AKIA[0-9A-Z]{16}` 정확 매치
AWS_ACCESS_KEY_ID = "AKIAFAKES3NOTREAL01X"  # 20자 (AKIA=4 + FAKES3NOTREAL01X=16)
AWS_ACCESS_KEY_ID_ALT = "AKIATESTNOTREAL02XYZ"  # 20자 (다른 fake canary, 동일 format)
