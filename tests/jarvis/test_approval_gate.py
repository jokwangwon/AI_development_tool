"""ApprovalGate — 사람("대표") 결정 게이트 테스트.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md Q-6 / §5 v3-2
  - 게이트 위치 = "반영 전"(착수마다 아님 — 개입 최소화).
  - default-deny: 명시 승인 없이는 반영 불가(안전 기본값, 자동 승인 금지).
답습: project_minimize_user_intervention(반영 직전 1회) / §8 self-change 게이트 동형.
"""
from __future__ import annotations

from src.jarvis.approval import ApprovalGate, ApprovalRequest


def _req(**over: object) -> ApprovalRequest:
    base = dict(summary="apply worker patch", worker_alias="claude",
                flags=[], output_preview="edited foo.py")
    base.update(over)
    return ApprovalRequest(**base)  # type: ignore[arg-type]


def test_default_deny_without_approver() -> None:
    # approver 미주입 = 자동 승인 금지 = 거부(안전 기본값)
    gate = ApprovalGate()
    assert gate.request(_req()) is False


def test_approver_grants() -> None:
    gate = ApprovalGate(approver=lambda req: True)
    assert gate.request(_req()) is True


def test_approver_denies() -> None:
    gate = ApprovalGate(approver=lambda req: False)
    assert gate.request(_req()) is False


def test_request_context_passed_to_approver() -> None:
    seen: dict[str, object] = {}

    def approver(req: ApprovalRequest) -> bool:
        seen["summary"] = req.summary
        seen["flags"] = req.flags
        seen["alias"] = req.worker_alias
        return True

    ApprovalGate(approver=approver).request(
        _req(summary="merge feature", flags=["force-push"], worker_alias="codex")
    )
    assert seen == {"summary": "merge feature", "flags": ["force-push"], "alias": "codex"}


def test_approver_exception_is_deny() -> None:
    # 승인 콜백 오류 = 반영 금지(fail-closed)
    def boom(req: ApprovalRequest) -> bool:
        raise RuntimeError("approver crashed")

    assert ApprovalGate(approver=boom).request(_req()) is False
