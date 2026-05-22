"""Orchestrator(사장) — 결정적 배관 + 라우팅 + 완료감지.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §5 MVP-0 트랙 A
  - D-1: 사장 = 결정적 오케스트레이터. 판단 지점(작업 분해·품질 평가) LLM 은
    트랙 A 범위 밖(후속) — 본 골격은 *결정적 배관*만(증명 ①②③④).
  - 흐름: 워커 선택(라우팅) → workdir 준비 → worker.run(headless) →
    guard.review(무비판 수용 금지) → gate.request("반영 전" 사람 게이트) → 보고.
  - Q-5: 라우팅 = MVP 수동/설정(alias). 자동 감지는 후속.
"""
from __future__ import annotations

import tempfile
from dataclasses import dataclass
from enum import Enum
from typing import Callable

from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.review import ReviewGuard, ReviewVerdict
from src.jarvis.worker import Worker, WorkerResult


class OutcomeStatus(str, Enum):
    APPLIED = "applied"          # 사람 승인 → 반영
    DENIED = "denied"            # 사람 게이트 거부(또는 default-deny)
    WORKER_FAILED = "worker_failed"  # 워커 실패(exit≠0/파싱불가) — 게이트 미진입


@dataclass(frozen=True)
class OutcomeReport:
    task_prompt: str
    worker_alias: str
    result: WorkerResult
    verdict: ReviewVerdict
    approved: bool
    applied: bool
    status: OutcomeStatus


class WorkerRegistry:
    """alias → Worker 매핑. 첫 등록 워커 = 기본(Q-5 수동/설정)."""

    def __init__(self) -> None:
        self._workers: dict[str, Worker] = {}

    def register(self, worker: Worker) -> None:
        self._workers[worker.alias] = worker

    def select(self, alias: str | None = None) -> Worker:
        if alias is None:
            if not self._workers:
                raise KeyError("no workers registered")
            return next(iter(self._workers.values()))
        return self._workers[alias]  # 미등록 alias = KeyError


def _default_workdir_factory(task_id: str) -> str:
    """기본 작업디렉터리 — 워커당 격리 경로(트랙 B 격리 backend 의 mount 대상)."""
    return tempfile.mkdtemp(prefix=f"jarvis-{task_id}-")


class Orchestrator:
    def __init__(
        self,
        registry: WorkerRegistry,
        guard: ReviewGuard,
        gate: ApprovalGate,
        workdir_factory: Callable[[str], str] | None = None,
    ) -> None:
        self._registry = registry
        self._guard = guard
        self._gate = gate
        self._workdir_factory = workdir_factory or _default_workdir_factory

    def dispatch(
        self, prompt: str, task_id: str, worker_alias: str | None = None
    ) -> OutcomeReport:
        worker = self._registry.select(worker_alias)
        workdir = self._workdir_factory(task_id)
        result = worker.run(prompt, workdir)
        verdict = self._guard.review(result)

        # 완료감지 = exit code(결정적). 실패 워커 결과는 반영 후보가 아님 → 게이트 미진입.
        if result.is_error:
            return OutcomeReport(prompt, worker.alias, result, verdict,
                                 approved=False, applied=False,
                                 status=OutcomeStatus.WORKER_FAILED)

        req = ApprovalRequest(
            summary=f"반영 승인 요청: worker={worker.alias} task={task_id}",
            worker_alias=worker.alias,
            flags=verdict.flags,
            output_preview=result.output[:200],
        )
        approved = self._gate.request(req)
        status = OutcomeStatus.APPLIED if approved else OutcomeStatus.DENIED
        return OutcomeReport(prompt, worker.alias, result, verdict,
                             approved=approved, applied=approved, status=status)
