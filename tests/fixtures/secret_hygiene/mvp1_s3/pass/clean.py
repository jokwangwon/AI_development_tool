# S-3 detect-secrets PASS fixture — secret 0건 (false positive 0 evidence)
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4

import os


def get_config():
    return {
        "timeout": 30,
        "retries": 3,
        "endpoint": os.environ.get("API_ENDPOINT", "http://localhost:8080"),
    }


def main():
    config = get_config()
    print(f"config loaded: {config}")


if __name__ == "__main__":
    main()
