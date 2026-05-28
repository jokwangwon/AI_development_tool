"""LLMFacade — Provider-agnostic facade (G2 GP-5).

본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다 (§4.1 답습).

SC-1 (65 entry, TR-1 발효): **facade redaction layer real (R-2 GP-2 prevention)** —
`complete()` 가 Router 위임 *전* request body 를 RedactionFilter 통과 (송신 secret strip).
**LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred** (full facade real 아님).

답습 출처:
  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import) + §8.2 (RedactionFilter)
  - docs/architecture/governance-preconditions.md §4.1 (LLM API request body secret 차단)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.3 (Hermes PMO ↔ provider 영구 권위)
  - docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md (SC-1 scope)
  - docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md (B-1~B-4 흡수)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.adapters.llm.redaction import RedactionFilter


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
    """LLM 호출 단일 진입점. redaction layer real, Router 위임 deferred (SC-1)."""

    def __init__(self, registry_path: str, redactor: RedactionFilter | None = None) -> None:
        self._registry_path = registry_path
        self._redactor: RedactionFilter = redactor if redactor is not None else RedactionFilter()

    def _redact_request(self, request: LLMRequest) -> dict[str, Any]:
        """송신 전 request body redaction (GP-2 prevention — Router 위임 전 호출, B-4 범위 = messages + metadata)."""
        return {
            "messages": self._redactor.redact_messages(request.messages),
            "metadata": (
                self._redactor.scrub(request.metadata) if request.metadata is not None else None
            ),
        }

    def complete(self, request: LLMRequest) -> LLMResponse:
        # GP-2 prevention: 송신 전 secret strip (redaction layer operative)
        redacted = self._redact_request(request)
        # Router 위임 = Provider Liquidity sub-cycle deferred (RT-1: 실 송신 0 = 미부착 window 없음)
        raise NotImplementedError(
            "LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred "
            f"(SC-1 redaction layer operative — {len(redacted['messages'])} messages redacted)"
        )

    async def health(self) -> dict[str, bool]:
        return {}
