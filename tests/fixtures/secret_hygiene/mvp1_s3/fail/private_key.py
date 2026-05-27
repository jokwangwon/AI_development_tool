# S-3 detect-secrets FAIL fixture — PrivateKeyDetector plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — fake private key marker (실 key material 0)

# RSA private key marker — PrivateKeyDetector 검출 대상 (-----BEGIN... marker)
FAKE_RSA_KEY = """-----BEGIN RSA PRIVATE KEY-----
FAKES3NOTREALPRIVATEKEYBASE64ENCODEDCONTENTHEREXXXXXXXXXXXXXXXX
FAKES3NOTREALPRIVATEKEYBASE64ENCODEDCONTENTHEREXXXXXXXXXXXXXXXX
-----END RSA PRIVATE KEY-----"""

# OpenSSH private key marker
FAKE_SSH_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
FAKES3NOTREALOPENSSHPRIVATEKEYCONTENTXXXXXXXXXXXXXXXXXXXXXXXXXX
-----END OPENSSH PRIVATE KEY-----"""
