"""GP-3 Stage 2 ST-3 PoC — runtime docker secret reader.

본 app 은 /run/secrets/api_key 에서 secret 을 *런타임* 에 읽고 sha256 hash 만 출력.
secret value 자체 출력 0건 — redaction 답습.

답습:
- ADR-008 §2.6.2 R2-1 (file system isolation)
- implementation-runtime-roadmap-mvp1.md §3.4.2 docker_secret_isolation_check
"""

import hashlib
import os
import sys

SECRET_PATH = "/run/secrets/api_key"
FAKE_MARKER = "FAKE_TEST_SECRET"


def main() -> int:
    if not os.path.exists(SECRET_PATH):
        print(f"ERROR: secret mount not found at {SECRET_PATH}", file=sys.stderr)
        return 2

    with open(SECRET_PATH, "rb") as fh:
        secret_bytes = fh.read().strip()

    if not secret_bytes:
        print("ERROR: secret file empty", file=sys.stderr)
        return 3

    if FAKE_MARKER.encode() not in secret_bytes:
        print(
            "ERROR: PoC secret missing FAKE_TEST_SECRET marker (F-금지 답습)",
            file=sys.stderr,
        )
        return 4

    digest = hashlib.sha256(secret_bytes).hexdigest()
    print(f"secret_sha256={digest}")
    print(f"secret_length={len(secret_bytes)}")
    print("docker_secret_isolation_check=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
