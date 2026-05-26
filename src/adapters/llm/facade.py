"""LLMFacade — Provider-agnostic facade (G2 GP-5 placeholder).

본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다 (§4.1 답습).
현 시점은 **placeholder** — real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화.

답습 출처:
  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.3 (Hermes PMO ↔ provider 영구 권위)
  - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.4 TR-1
  - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §2.1
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LLMRequest:
    alias: str
    messages: list[dict[str, str]]
    metadata: dict[str, Any] | None = None


@dataclass(frozen=True)
class LLMResponse:
    content: str
    metadata: dict[str, Any]


class LLMFacade:
    """Placeholder — real LiteLLM import + Router 위임은 TR-1 발화 시 작성."""

    def __init__(self, registry_path: str) -> None:
        self._registry_path = registry_path

    def complete(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")

    async def health(self) -> dict[str, bool]:
        return {}
