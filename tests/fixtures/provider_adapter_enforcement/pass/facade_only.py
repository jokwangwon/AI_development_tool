"""PASS fixture — 가상의 facade.py 본문 모사.

본 fixture 는 §4.1 의 허용 경로 (`src/adapters/llm/facade.py`) 본문을
*형식만* 모사한다. 실 LiteLLM SDK 는 import 하지 않으며, 본 PoC scanner
가 위반 0건을 보고해야 함을 검증.

답습 출처:
  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import)

⚠️ oracle 한계 (3+1 합의 2026-05-29 MT-5): fixture 경로(tests/fixtures/...)는
facade allow-path(`src/adapters/llm/facade.py`)가 *아니므로*, 여기에 실 litellm
import 를 넣으면 FAIL 된다 → 본 fixture 는 litellm 을 import 하지 않는다(형식 모사만).
따라서 facade allow-path(litellm 토큰 면제)의 실 검증은 본 fixture 로 불가능하며,
`tests/tools/test_provider_import_scanner.py` (MT-4 음성 3종 + MT-3 동적)가 oracle 이다.
본 fixture 는 scanner 가 import 무관 코드를 false positive 로 잡지 않는지만 확인.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LLMRequest:
    alias: str  # yaml 정의 alias 만 사용 (모델명 직접 사용 금지 — §9.1 #1)
    messages: list[dict[str, str]]
    metadata: dict[str, Any] | None = None


@dataclass(frozen=True)
class LLMResponse:
    content: str
    metadata: dict[str, Any]


class LLMFacade:
    """Provider-agnostic facade — 본 fixture 에서는 형식만 모사."""

    def __init__(self, registry_path: str) -> None:
        self._registry_path = registry_path

    def complete(self, request: LLMRequest) -> LLMResponse:
        # 실 구현은 LiteLLM Router 위임 — 본 fixture 에서는 stub
        raise NotImplementedError("PoC fixture — real impl deferred")

    async def health(self) -> dict[str, bool]:
        # §9.2 dry probe — 본 fixture 에서는 stub
        return {}
