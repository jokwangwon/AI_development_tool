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
from src.jarvis.boss import AdviceRequest, BossAdvice, BossLLM, merge_flags
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
    advice: BossAdvice | None = None  # MVP-1 advisory(boss 주입 시), 미주입=None


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
        boss: BossLLM | None = None,
    ) -> None:
        self._registry = registry
        self._guard = guard
        self._gate = gate
        self._workdir_factory = workdir_factory or _default_workdir_factory
        # R7: boss=None 이면 advisory 없이 MVP-0 동작 그대로 보존(하위 호환).
        self._boss = boss

    def _advise(
        self, prompt: str, worker: Worker, result: WorkerResult, verdict: ReviewVerdict
    ) -> BossAdvice:
        """판단 지점(MVP-1 유일) — 결과 검토 advisory. R3: 실패는 누락+경고로 흡수.

        ApprovalGate.request 의 fail-closed try/except 와 동형으로, Boss endpoint
        timeout/다운/비정상은 advisory *부재*로 처리하되 사람에게 명시 경고한다
        (부재를 안전으로 오해 금지). advisory 는 보조이므로 부재가 차단은 아니다.
        """
        req = AdviceRequest(
            prompt=prompt,
            worker_alias=worker.alias,
            output=result.output,
            deterministic_flags=list(verdict.flags),
        )
        try:
            return self._boss.advise(req)  # type: ignore[union-attr]
        except Exception:
            return BossAdvice(
                summary="⚠️ Boss advisory 실패 — 결정적 flag 만으로 판단",
                extra_flags=[],
                advisory_failed=True,
            )

    def dispatch(
        self, prompt: str, task_id: str, worker_alias: str | None = None
    ) -> OutcomeReport:
        worker = self._registry.select(worker_alias)
        workdir = self._workdir_factory(task_id)
        result = worker.run(prompt, workdir)
        verdict = self._guard.review(result)

        # 완료감지 = exit code(결정적). 실패 워커 결과는 반영 후보가 아님 → 게이트 미진입.
        # R8: 실패 워커엔 advise 미호출(비용·injection 표면 회피) — early-return 위.
        if result.is_error:
            return OutcomeReport(prompt, worker.alias, result, verdict,
                                 approved=False, applied=False,
                                 status=OutcomeStatus.WORKER_FAILED)

        # MVP-1 판단 지점: boss 주입 시에만 advisory(결정적 가드 *뒤*, 사람 게이트 *앞*).
        advice = self._advise(prompt, worker, result, verdict) if self._boss else None
        # R1/fail-safe: 결정적 flag 에 advisory flag 를 union(추가만, 감산 불가).
        flags = (merge_flags(list(verdict.flags), advice.extra_flags)
                 if advice else list(verdict.flags))

        req = ApprovalRequest(
            summary=f"반영 승인 요청: worker={worker.alias} task={task_id}",
            worker_alias=worker.alias,
            flags=flags,
            output_preview=result.output[:200],
            advice=advice,
        )
        approved = self._gate.request(req)
        status = OutcomeStatus.APPLIED if approved else OutcomeStatus.DENIED
        return OutcomeReport(prompt, worker.alias, result, verdict,
                             approved=approved, applied=approved, status=status,
                             advice=advice)
