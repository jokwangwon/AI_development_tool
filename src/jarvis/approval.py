"""ApprovalGate — 사람("대표") 결정 게이트 (반영 전, default-deny).

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md Q-6 / §5 v3-2
  - "반영 전" 단일 게이트(착수마다 승인 아님 = 개입 최소화).
  - default-deny: 명시 승인 콜백 없이는 반영 불가. 자동 승인 금지(안전 기본값).
  - fail-closed: 승인 절차 오류 시 거부.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True)
class ApprovalRequest:
    """대표에게 제시되는 반영 승인 요청."""

    summary: str
    worker_alias: str
    flags: list[str] = field(default_factory=list)
    output_preview: str = ""


# approver(request) -> 승인 여부. 사람 인터페이스(CLI prompt 등)는 주입.
Approver = Callable[[ApprovalRequest], bool]


class ApprovalGate:
    def __init__(self, approver: Approver | None = None) -> None:
        self._approver = approver

    def request(self, req: ApprovalRequest) -> bool:
        if self._approver is None:
            return False  # default-deny
        try:
            return bool(self._approver(req))
        except Exception:
            return False  # fail-closed
