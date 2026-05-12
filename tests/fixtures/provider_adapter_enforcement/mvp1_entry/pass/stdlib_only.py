"""MVP-1 entry coverage — PASS fixture (FP-resistance for stdlib usage).

답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.3 sub-step 3.2.
본 fixture 는 stdlib import + provider 단어를 변수명/문자열로 사용하는 정상
코드가 AST scanner 의 FP 를 일으키지 않음을 MVP-1 entry 회귀 보강.
답습 변경 0건 — provider_import_scanner.py 변경 0건.

기대 결과: scanner 가 violation 0건 보고 (PASS).
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any


@dataclass
class ProviderRegistryEntry:
    """단순 데이터 클래스 — provider 단어는 변수명/필드명 사용 (FP 미발화 의무)."""

    alias: str
    description: str


def load_registry(path: str) -> dict[str, Any]:
    # provider / anthropic / openai / litellm / ollama 단어는 *문자열 값* 으로만 등장.
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


PROVIDER_ALIAS_PATTERN = re.compile(r"^[a-z][a-z0-9_-]+$")
