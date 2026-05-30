"""jarvis 계획 승인 보드 백엔드 — PlanController plan_approver HUD 통합 (98 entry+).

답습: docs/phase0/jarvis-hud-plan-approval-design-brief.md (v1.1)
  + docs/review/3plus1-consensus-2026-05-30-jarvis-hud-plan-approval.md (BLOCKING 6 흡수)
  + jarvis_hud/jarvis_tasks.py (CB-1~7 패턴 — 상속 금지, 위임/복제 재사용).

핵심 (보안 — 웹↔plan 실행):
  - CB-1: plan 카드/모달 desc·contracts 표시 *전* scrub(secret, UI+ledger 양쪽). desc 비절단(GP-3).
  - CB-3+BL-5: /plan·/plan-decision same-origin — URL 파싱 scheme+netloc 정확 일치(suffix 우회 차단).
  - CB-4+BL-4: plan_approver = threading.Event.wait(timeout) default-deny. Event = plan thread 전
    원자 선생성. 검증 실패(VALIDATION_FAILED) = 모달 미진입, deny-resolve.
  - CB-6: threading.Event (asyncio 금지).
  - CB-7: planner_builder/worker_builder 주입 (TestClient hermetic).
  - BL-2: plan 게이트만 사람 차단(default-deny). subtask dispatch = 반영 게이트 auto-accept
    (ApprovalGate(approver=lambda r: True)) — plan-then-execute "1회 승인" 단일화.
  - BL-3: plan 게이트 = subtask *dispatch 전* 통제. planner 추론(plan 생성)은 승인 *전* 실행.
  - BL-6: 모달에 명시/암묵 contracts 구분 + allow_code_consume read-only 표시(표시≠집행).

CB-5(프론트 XSS)는 index.html(textContent/createElement) 책무 — 본 백엔드는 scrub 데이터만 제공.
"""
from __future__ import annotations

import threading
import time
import uuid
from typing import Any, Callable
from urllib.parse import urlparse

from src.adapters.llm.redaction import RedactionFilter
from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import BossPlanner, OllamaBoss
from src.jarvis.ledger import LedgerLog
from src.jarvis.orchestrator import Orchestrator, OutcomeReport, WorkerRegistry
from src.jarvis.plan_controller import (
    PlanApprovalRequest,
    PlanController,
    PlanStatus,
)
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import OllamaWorker
from src.jarvis.worker_setup import build_worker_registry

_PLAN_STATUS = {
    "planning": "계획 생성 중",
    "awaiting": "승인 대기",
    "running": "진행 중",
    "completed": "완료",
    "denied": "거부",
    "failed": "실패",
}
_TERMINAL = frozenset({"completed", "denied", "failed"})
_DEFAULT_MODEL = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
_FILE_MODEL = "qwen3-coder-next:latest"


def _default_planner_builder(opts: dict[str, Any]) -> BossPlanner:
    """opts → planner(BossPlanner). 기본 OllamaBoss(file-only plan_kinds, Q2 고정).

    codex planner 토글은 후속(Q2). real_workers 면 code+file 안내.
    """
    from src.jarvis.boss import boss_plan_prompt  # noqa: PLC0415 (지연 import, 순환 회피 불요)

    kinds = ("code", "file") if opts.get("real_workers") else ("file",)
    boss = OllamaBoss(model=opts.get("planner_model") or _DEFAULT_MODEL)
    boss._plan_prompt = boss_plan_prompt(kinds)  # noqa: SLF001 (plan_kinds 주입)
    return boss


def _default_worker_builder(opts: dict[str, Any]) -> tuple[WorkerRegistry, dict[str, str]]:
    """opts → (registry, kind_table). 기본 file-only(OllamaWorker). real_workers=code+file(Q4 opt-in)."""
    if opts.get("real_workers"):
        return build_worker_registry(file_model=opts.get("worker_model") or _FILE_MODEL)
    reg = WorkerRegistry()
    reg.register(OllamaWorker(alias="ollama-file", model=opts.get("worker_model") or _FILE_MODEL))
    return reg, {"file": "ollama-file"}


def _plan_card(plan_id: str, prompt: str = "", now: str = "") -> dict[str, Any]:
    return {
        "id": plan_id, "kind": "plan", "prompt": prompt,
        "status": "planning", "status_label": _PLAN_STATUS["planning"],
        "plan": None,          # 모달 데이터(subtasks/contracts/implicit/order/aliases/allow_code_consume)
        "reason": None, "error": None, "subtask_ids": [],
        "created_at": now, "updated_at": now,
    }


def _subtask_card(sub_id: str, plan_id: str, desc: str, alias: str, now: str) -> dict[str, Any]:
    return {
        "id": sub_id, "kind": "subtask", "plan_id": plan_id,
        "desc": desc, "alias": alias, "status": "running",
        "status_label": "진행 중", "redacted_output_preview": None,
        "created_at": now, "updated_at": now,
    }


class JarvisPlanBoard:
    """계획 카드 + subtask 카드 보드(in-memory, lock). PlanController 위임(상속 금지).

    planner_builder/worker_builder 주입 = hermetic(CB-7). plan 게이트만 사람 차단(BL-2),
    subtask dispatch = auto-accept Orchestrator.
    """

    def __init__(
        self,
        planner_builder: Callable[[dict[str, Any]], BossPlanner] | None = None,
        worker_builder: Callable[[dict[str, Any]], tuple[WorkerRegistry, dict[str, str]]] | None = None,
        ledger: LedgerLog | None = None,
        approver_timeout_s: float = 300.0,
        max_concurrent: int = 4,
    ) -> None:
        self._planner_builder = planner_builder or _default_planner_builder
        self._worker_builder = worker_builder or _default_worker_builder
        self._ledger = ledger
        self._timeout = approver_timeout_s
        self._max_concurrent = max_concurrent
        self._lock = threading.Lock()
        self._redactor = RedactionFilter()
        self._plans: dict[str, dict[str, Any]] = {}
        self._subtasks: dict[str, dict[str, Any]] = {}
        self._events: dict[str, threading.Event] = {}
        self._decisions: dict[str, bool] = {}

    def _scrub(self, text: str) -> str:
        return self._redactor.scrub(text) if isinstance(text, str) else ""

    def _record(self, plan_id: str, event: str, **fields: Any) -> None:
        if self._ledger is None:
            return
        try:
            self._ledger.record(plan_id, event, **fields)
        except Exception:
            return

    def _update_plan(self, plan_id: str, **fields: Any) -> None:
        with self._lock:
            card = self._plans.get(plan_id)
            if card is None:
                return
            card.update(fields)
            card["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            if "status" in fields:
                card["status_label"] = _PLAN_STATUS.get(fields["status"], fields["status"])

    def _running_count(self) -> int:
        return sum(1 for c in self._plans.values() if c["status"] in ("planning", "awaiting", "running"))

    def create_plan(self, opts: dict[str, Any]) -> str:
        prompt = (opts.get("prompt") or "").strip()
        if not prompt:
            raise ValueError("prompt required")
        plan_id = uuid.uuid4().hex[:8]
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        with self._lock:
            if self._running_count() >= self._max_concurrent:
                raise RuntimeError(f"동시 계획 상한({self._max_concurrent}) 초과")
            self._events[plan_id] = threading.Event()  # BL-4: plan thread 전 원자 선생성
            card = _plan_card(plan_id, self._scrub(prompt[:200]), now)
            card["_opts"] = opts
            card["_prompt"] = prompt  # 비절단 원본(planner 입력) — 카드 노출 안 함
            self._plans[plan_id] = card
        self._record(plan_id, "plan_created", prompt=self._scrub(prompt[:200]), status="planning")
        return plan_id

    def _make_plan_approver(self, plan_id: str) -> Callable[[PlanApprovalRequest], bool]:
        def approver(req: PlanApprovalRequest) -> bool:
            # CB-1 scrub(secret) + GP-3 비절단(truncate 금지). CB-5(escape)는 프론트 책무.
            subtasks = [
                {"desc": self._scrub(st.desc), "worker_kind": st.worker_kind,
                 "depends_on": list(st.depends_on), "alias": req.mapped_aliases[i]}
                for i, st in enumerate(req.subtasks)
            ]
            contracts = [{"name": self._scrub(c.name), "produced_by": c.produced_by}
                         for c in req.contracts]
            implicit = [{"name": self._scrub(c.name), "produced_by": c.produced_by}
                        for c in req.implicit_contracts]
            with self._lock:
                opts = self._plans.get(plan_id, {}).get("_opts", {})
            plan_view = {
                "subtasks": subtasks, "contracts": contracts,
                "implicit_contracts": implicit, "order": list(req.order),
                "total_steps": req.total_steps,
                # BL-6: 능력 경계 read-only 표시(표시≠집행, controller 강제).
                "allow_code_consume": bool(opts.get("allow_code_consume")),
            }
            # 디딤돌1f BL-10: plan_proposed/plan_approved/plan_denied 는 controller
            # (plan_controller.py)가 권위 단일 기록. board 가 중복 기록하면 detection
            # 기준선(107 runbook Tier A) 오염 → 여기선 in-memory 카드만 갱신, ledger 0.
            self._update_plan(plan_id, status="awaiting", plan=plan_view)
            ev = self._events.get(plan_id)
            if ev is None:
                return False
            got = ev.wait(timeout=self._timeout)
            if not got:  # CB-4: timeout = default-deny
                return False
            accepted = bool(self._decisions.get(plan_id, False))
            return accepted

        return approver

    def decide_plan(self, plan_id: str, accept: bool) -> bool:
        with self._lock:
            card = self._plans.get(plan_id)
            if card is None:
                return False
            if card["status"] != "awaiting":  # GP-3 idempotent — awaiting 만 수락
                return False
            self._decisions[plan_id] = bool(accept)
            ev = self._events.get(plan_id)
        if ev is not None:
            ev.set()
        return True

    def _dispatch_subtask(
        self, plan_id: str, auto_orch: Orchestrator, desc: str, sub_id: str, alias: str,
    ) -> OutcomeReport:
        """PlanController dispatcher 위임 — subtask 카드 N 분리(Q5) + auto-accept dispatch(BL-2)."""
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        with self._lock:
            self._subtasks[sub_id] = _subtask_card(sub_id, plan_id, self._scrub(desc), alias, now)
            parent = self._plans.get(plan_id)
            if parent is not None and sub_id not in parent["subtask_ids"]:
                parent["subtask_ids"].append(sub_id)
        report = auto_orch.dispatch(desc, sub_id, alias)  # 반영 게이트 auto-accept(BL-2)
        st = self._subtasks.get(sub_id)
        if st is not None:
            preview = self._scrub((report.result.output or "")[:400])
            st.update(status="applied" if report.applied else "failed",
                      status_label="수락" if report.applied else "실패",
                      redacted_output_preview=preview,
                      updated_at=time.strftime("%Y-%m-%dT%H:%M:%S"))
        return report

    def run_plan(self, plan_id: str) -> None:
        try:
            with self._lock:
                card = self._plans.get(plan_id)
                opts = card.get("_opts", {}) if card else {}
                prompt = card.get("_prompt", "") if card else ""
            if card is None:
                return
            planner = self._planner_builder(opts)
            registry, kind_table = self._worker_builder(opts)
            # BL-2: subtask dispatch 반영 게이트 auto-accept(plan 게이트만 사람 차단).
            auto_orch = Orchestrator(
                registry, ReviewGuard(), ApprovalGate(approver=lambda r: True))

            def dispatcher(desc: str, sub_id: str, alias: str) -> OutcomeReport:
                return self._dispatch_subtask(plan_id, auto_orch, desc, sub_id, alias)

            ctrl = PlanController(
                dispatcher=dispatcher, kind_table=kind_table, registry=registry,
                plan_approver=self._make_plan_approver(plan_id),
                allow_code_consume=bool(opts.get("allow_code_consume")),
                ledger=self._ledger,
            )
            out = ctrl.run_from_planner(planner, prompt, plan_id)
            status = {
                PlanStatus.COMPLETED: "completed",
                PlanStatus.DENIED: "denied",
                PlanStatus.VALIDATION_FAILED: "failed",
                PlanStatus.PLAN_UNAVAILABLE: "failed",
                PlanStatus.SUBTASK_FAILED: "failed",
            }.get(out.status, "failed")
            self._update_plan(plan_id, status=status, reason=self._scrub(out.reason))
            self._record(plan_id, "plan_resolved", status=status, reason=self._scrub(out.reason))
        except Exception as exc:  # fail-soft (서버 무중단)
            err = self._scrub(str(exc))
            self._update_plan(plan_id, status="failed", error=err)
            self._record(plan_id, "plan_resolved", status="failed", error=err)

    def snapshot(self) -> dict[str, list[dict[str, Any]]]:
        with self._lock:
            plans = [
                {k: v for k, v in c.items() if not k.startswith("_")}
                for c in sorted(self._plans.values(), key=lambda c: c["created_at"], reverse=True)
            ]
            subtasks = [dict(s) for s in self._subtasks.values()]
        return {"plans": plans, "subtasks": subtasks}


# ── CSRF (CB-3 + BL-5: URL 파싱 정확 일치) ───────────────────────────────────
def same_origin_strict(request) -> bool:
    """cross-origin POST 차단. Origin 있으면 URL 파싱 후 netloc(host:port) 정확 일치.

    기존 endswith(jarvis_tasks.same_origin) 의 suffix 우회(evil-host.com 가 host.com 으로
    끝남) 차단(BL-5). Origin 부재(비브라우저 CLI) = 허용 — plan trigger=토큰 소모이나
    localhost 단일 사용자 비례 수용(잔여 명시).
    """
    origin = request.headers.get("origin")
    if not origin:
        return True
    host = request.headers.get("host", "")
    if not host:
        return False
    return urlparse(origin).netloc == host


def make_jarvis_plan_routes(board: JarvisPlanBoard) -> list:
    import asyncio
    import json

    from starlette.responses import JSONResponse
    from starlette.routing import Route

    async def submit(request):
        if not same_origin_strict(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        try:
            data = json.loads(await request.body())
        except Exception:
            return JSONResponse({"error": "bad json"}, status_code=400)
        try:
            plan_id = board.create_plan(data)
        except (ValueError, RuntimeError) as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        asyncio.create_task(asyncio.to_thread(board.run_plan, plan_id))  # CB-4/CB-6
        return JSONResponse({"plan_id": plan_id})

    async def plans(request):
        return JSONResponse(board.snapshot())

    async def decision(request):
        if not same_origin_strict(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        plan_id = request.path_params.get("plan_id")
        try:
            data = json.loads(await request.body())
        except Exception:
            data = {}
        dec = data.get("decision")
        if dec not in ("accept", "reject"):
            return JSONResponse({"error": "decision must be accept|reject"}, status_code=400)
        ok = board.decide_plan(plan_id, dec == "accept")
        return JSONResponse({"ok": ok}, status_code=200 if ok else 409)  # GP-3 idempotent → 409

    return [
        Route("/api/jarvis/plan", submit, methods=["POST"]),
        Route("/api/jarvis/plans", plans, methods=["GET"]),
        Route("/api/jarvis/plan/{plan_id}/decision", decision, methods=["POST"]),
    ]
