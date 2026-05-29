"""PlanController — 디딤돌1a 결정적 controller (plan-then-execute).

답습: docs/phase0/jarvis-stone1a-plan-then-execute-design-brief.md (v1.2) §3·§4·§6
  [[3plus1-consensus-2026-05-29-jarvis-stone1a-plan-then-execute]] (REVISE 흡수).

  - CN-2 (controller-first, 주입형): `run(plan: BossPlan, task_id)` 는 *이미
    만들어진 plan* 을 받는다. plan 공급원(boss.plan / 사람 / frontier worker)이
    controller 출하를 인질로 잡지 않는다. `run_from_planner` 는 BossPlanner 를
    호출해 plan 을 얻은 뒤 동일 검증 경로로 위임(PLAN-SOURCE: 누가 짠 plan 이든
    검증+승인 — 똑똑함≠신뢰).
  - §3 검증 순서(사람 승인 *전* 전부): schema(빈/desc/enum) → step limit → DAG
    (범위·자기참조·사이클, stdlib graphlib) → worker_kind→alias table 룩업 +
    registry 등록 확인. → 사람 승인 게이트(desc 전문 비절단, GP-3) → 위상정렬
    순차 dispatch.
  - BL-1/§6.1: boss 는 means 의 *틀*(argv prefix·alias·isolation) 을 못 정한다
    (alias = table 룩업, desc 와 무관). desc(=worker prompt, untrusted)는 boss 가
    정하며 계획 게이트 + subtask 반영 게이트가 방어(redaction 아님).
  - BL-5: 중간 control-affecting boss call 0 — dispatch 루프가 planner 를 재호출
    하지 않음(non-adaptive). 기존 dispatch 의 사람용 advise() 는 제어 환류 0.
  - BL-7: sub_task_id = f"{task_id}.{i}" 고유 파생(LedgerLog fold 병합 충돌 방지).
  - Q1 {code,file} 기본 + shell opt-in / Q4 미반영=즉시 중단 / Q3 MAX_STEPS=5 /
    Q6 별도 PlanApprovalRequest + ApprovalGate fail-closed/default-deny *패턴* 답습.

본 모듈은 외부 SDK import 0(stdlib graphlib 만). boss(planner)·orchestrator
(dispatch)에 *의존*하되 그 역방향은 없다(.importlinter 단방향 — BL-8).
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from graphlib import CycleError, TopologicalSorter
from typing import Callable

from src.jarvis.boss import BossPlan, BossPlanner, PlanSubtask
from src.jarvis.orchestrator import OutcomeReport, WorkerRegistry

# Q1 결정(2026-05-29): 기본 enum = {code, file}. shell 은 가장 위험(boss 가 shell
# prompt 에 임의 명령 텍스트) → 기본 제외, kind_table 에 명시 등록(opt-in) 시에만.
WORKER_KIND_DEFAULT: tuple[str, ...] = ("code", "file")

# Q3 결정: 순차 dispatch latency 상한 + 사람 검토 부하 + 약한 boss 과분해 방어.
DEFAULT_MAX_STEPS = 5

# dispatcher 시그니처 = Orchestrator.dispatch(prompt, task_id, worker_alias).
Dispatcher = Callable[[str, str, str], OutcomeReport]


@dataclass(frozen=True)
class PlanApprovalRequest:
    """계획 1회 승인 요청 — *반영* 게이트(ApprovalRequest)와 분리(Q6).

    GP-3: 사람이 실효 means(=각 subtask 의 desc)를 보지 못하면 게이트가 위험을
    못 거른다 → `subtasks` 의 desc 는 *비절단 전문*으로 표시(truncate 금지).
    mapped_aliases = worker_kind table 룩업 결과(boss 가 못 정하는 means 틀),
    order = 위상정렬 실행 순서, total_steps = 검토 부하.
    """

    subtasks: tuple[PlanSubtask, ...]
    mapped_aliases: tuple[str, ...]
    order: tuple[int, ...]
    total_steps: int


# plan_approver(req) -> 승인 여부. 사람 인터페이스(CLI/HUD)는 주입. None=default-deny.
PlanApprover = Callable[[PlanApprovalRequest], bool]


class PlanStatus(str, Enum):
    COMPLETED = "completed"                  # 전 subtask 반영 완료
    VALIDATION_FAILED = "validation_failed"  # schema/DAG/table/step 검증 실패
    DENIED = "denied"                        # 사람 게이트 거부 또는 default-deny
    SUBTASK_FAILED = "subtask_failed"        # 실행 중 subtask 미반영 → 즉시 중단
    PLAN_UNAVAILABLE = "plan_unavailable"    # planner.plan() 실패(거짓 진행 금지)


@dataclass(frozen=True)
class PlanOutcome:
    status: PlanStatus
    reason: str
    subtask_reports: tuple[OutcomeReport, ...] = ()


class PlanController:
    def __init__(
        self,
        dispatcher: Dispatcher,
        kind_table: dict[str, str],
        registry: WorkerRegistry,
        plan_approver: PlanApprover | None = None,
        max_steps: int = DEFAULT_MAX_STEPS,
        ledger: object | None = None,
    ) -> None:
        self._dispatch = dispatcher
        self._table = dict(kind_table)          # worker_kind → alias (harness 소유)
        self._registry = registry
        self._approver = plan_approver
        self._max_steps = max_steps
        self._ledger = ledger                   # LedgerLog | None (fail-soft, 디딤돌0)

    # ── plan 공급원 유연(IN-2) ─────────────────────────────────────────────
    def run_from_planner(
        self, planner: BossPlanner, prompt: str, task_id: str
    ) -> PlanOutcome:
        """planner(boss/사람/frontier worker)에게 plan 1회 요청 후 run() 위임.

        §2: plan 호출 실패 = 계획 부재 → 중단(거짓 진행 금지). 성공한 plan 도
        PLAN-SOURCE 불변식대로 run() 의 검증+승인을 거친다(똑똑함≠신뢰).
        """
        try:
            plan = planner.plan(prompt)
        except Exception as exc:  # noqa: BLE001 (모든 실패 = 계획 부재로 흡수)
            self._record(task_id, "plan_unavailable", error=str(exc))
            return PlanOutcome(PlanStatus.PLAN_UNAVAILABLE, f"plan 부재: {exc}")
        return self.run(plan, task_id)

    # ── 주입형 핵심(CN-2) ──────────────────────────────────────────────────
    def run(self, plan: BossPlan, task_id: str) -> PlanOutcome:
        subtasks = plan.subtasks

        # 1. schema validation (빈 plan / desc / worker_kind enum)
        if not subtasks:
            return self._reject("빈 plan — 실행할 subtask 없음")
        for st in subtasks:
            if not st.desc.strip():
                return self._reject("desc 비어있음")
            if st.worker_kind not in self._table:
                return self._reject(f"worker_kind 미허용(opt-in 필요): {st.worker_kind}")

        # 2. step limit (사람 승인 전 — 폭주·검토부하 상한)
        if len(subtasks) > self._max_steps:
            return self._reject(f"step limit 초과: {len(subtasks)} > {self._max_steps}")

        # 3. DAG 검증 (범위·자기참조 선행 가드 → graphlib 사이클)
        n = len(subtasks)
        ts: TopologicalSorter[int] = TopologicalSorter()
        for i, st in enumerate(subtasks):
            for d in st.depends_on:
                if not (0 <= d < n):
                    return self._reject(f"depends_on 범위초과: subtask {i} → {d}")
                if d == i:
                    return self._reject(f"자기참조 의존: subtask {i}")
            ts.add(i, *dict.fromkeys(st.depends_on))  # 중복 인덱스 제거
        try:
            order = tuple(ts.static_order())
        except CycleError:
            return self._reject("DAG 사이클 — 위상정렬 불가")

        # 4. worker mapping (worker_kind → alias table + registry 등록 확인)
        aliases: list[str] = []
        for st in subtasks:
            alias = self._table[st.worker_kind]
            try:
                self._registry.select(alias)
            except KeyError:
                return self._reject(f"미등록 worker alias: {alias}")
            aliases.append(alias)

        self._record(task_id, "plan_proposed", n_subtasks=n)

        # 5. 사람 승인 게이트 (계획 1회, desc 전문 비절단 — GP-3)
        req = PlanApprovalRequest(
            subtasks=subtasks,
            mapped_aliases=tuple(aliases),
            order=order,
            total_steps=n,
        )
        if not self._approve(req):
            self._record(task_id, "plan_denied")
            return PlanOutcome(PlanStatus.DENIED, "사람 게이트 거부(또는 default-deny)")
        self._record(task_id, "plan_approved")

        # 6. 위상정렬 순차 dispatch (중간 control-affecting boss call 0)
        reports: list[OutcomeReport] = []
        for idx in order:
            st = subtasks[idx]
            sub_id = f"{task_id}.{idx}"  # BL-7 고유 파생
            self._record(sub_id, "subtask_started",
                         parent=task_id, worker_kind=st.worker_kind)
            report = self._dispatch(st.desc, sub_id, aliases[idx])
            reports.append(report)
            if not report.applied:  # Q4: 미반영(실패/거부) = 즉시 중단
                self._record(sub_id, "subtask_failed", status=report.status.value)
                return PlanOutcome(
                    PlanStatus.SUBTASK_FAILED,
                    f"subtask {idx} 미반영({report.status.value}) — 중단",
                    tuple(reports),
                )
            self._record(sub_id, "subtask_applied")

        return PlanOutcome(PlanStatus.COMPLETED, "전 subtask 반영 완료", tuple(reports))

    # ── 내부 헬퍼 ─────────────────────────────────────────────────────────
    def _approve(self, req: PlanApprovalRequest) -> bool:
        """ApprovalGate fail-closed/default-deny *패턴* 답습(Q6, approval.py:41-47)."""
        if self._approver is None:
            return False  # default-deny — 명시 승인 없이는 미실행
        try:
            return bool(self._approver(req))
        except Exception:
            return False  # fail-closed

    def _reject(self, reason: str) -> PlanOutcome:
        return PlanOutcome(PlanStatus.VALIDATION_FAILED, reason)

    def _record(self, task_id: str, event: str, **fields: object) -> None:
        """LedgerLog 영속(디딤돌0). ledger=None=skip. 이중 fail-soft(부재가 차단 0)."""
        if self._ledger is None:
            return
        try:
            self._ledger.record(task_id, event, **fields)
        except Exception:
            return
