"""jarvis 작업 카드보드 백엔드 — 하나(jarvis_hud)에 jarvis 작업 파이프라인 통합 (75 entry).

답습: docs/phase0/jarvis-hud-task-board-integration-brief.md (v1.1)
  + docs/review/3plus1-consensus-2026-05-29-jarvis-hud-task-board.md (BLOCKING 8 흡수)

핵심 (보안 — 웹↔명령실행):
  - CB-1/CB-2: 보드/카드/pane 출력은 표시 *전* `RedactionFilter.scrub` (워커 응답 redaction 은
    파이프라인이 안 함 → 표시 경로에서 구현). 카드는 redacted_output_preview 만, raw_available=false.
  - CB-3: /task·/decision = same-origin(Origin) 체크 (cross-origin POST = 명령 실행 trigger 차단).
  - CB-4: dispatch = 백그라운드 thread, ui_approver = threading.Event.wait(timeout) (default-deny),
    Event 는 dispatch *전* 선생성 (/decision early-race 0).
  - CB-6: threading.Event (asyncio.Event 금지 — to_thread 의 sync wait ↔ async set 교차).
  - CB-7: worker_builder/boss_builder 주입 (TestClient hermetic).

승인 게이트 = "반영 전" (실행 통제 아님) — 워커는 dispatch 시 이미 실행. default-deny 보존.
"""
from __future__ import annotations

import shlex
import threading
import time
import uuid
from typing import Any, Callable

from src.adapters.llm.redaction import RedactionFilter
from src.jarvis.approval import ApprovalGate, ApprovalRequest
from src.jarvis.boss import BossAdvice, BossLLM, OllamaBoss
from src.jarvis.isolation import LandlockIsolation, PassthroughIsolation
from src.jarvis.orchestrator import Orchestrator, OutcomeStatus, WorkerRegistry
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import OllamaWorker, TmuxWorker

_PANE_MAX = 4000  # /pane 응답 길이 제한 (R: 표시 표면 축소)
_WORKER_ALIAS = "task"

_STATUS = {  # 내부 → UI 라벨
    "running": "진행중",
    "awaiting": "승인대기",
    "applied": "수락",
    "denied": "거절",
    "failed": "실패",
}


def _default_worker_builder(opts: dict[str, Any], on_session: Callable[[str], None]):
    """opts → OllamaWorker(텍스트) 또는 TmuxWorker(명령 실행 + isolation + 세션 hook)."""
    wtype = opts.get("worker_type", "ollama")
    if wtype == "tmux":
        iso = (
            LandlockIsolation()
            if opts.get("isolation") == "landlock"
            else PassthroughIsolation()
        )
        return TmuxWorker(
            alias=_WORKER_ALIAS,
            argv=shlex.split(opts.get("tmux_argv") or "bash -lc"),
            isolation=iso,
            on_session=on_session,
        )
    return OllamaWorker(
        alias=_WORKER_ALIAS,
        model=opts.get("worker_model") or "qwen3-30b-a3b-instruct-2507-bartowski:latest",
    )


def _default_boss_builder(opts: dict[str, Any]) -> BossLLM | None:
    if opts.get("no_boss"):
        return None
    return OllamaBoss(
        model=opts.get("boss_model") or "qwen3-30b-a3b-instruct-2507-bartowski:latest"
    )


class JarvisTaskBoard:
    """작업 카드 상태 보드 (in-memory, lock 보호). 재시작 = 유실 + 진행중 작업 고아(휘발성, R-7).

    worker_builder/boss_builder 주입 = TestClient hermetic (CB-7). default = 실 src.jarvis 워커.
    """

    def __init__(
        self,
        worker_builder: Callable[..., Any] | None = None,
        boss_builder: Callable[[dict[str, Any]], BossLLM | None] | None = None,
        memory: Any | None = None,
        approver_timeout_s: float = 300.0,
        max_concurrent: int = 8,
    ) -> None:
        self._worker_builder = worker_builder or _default_worker_builder
        self._boss_builder = boss_builder or _default_boss_builder
        self._memory = memory
        self._timeout = approver_timeout_s
        self._max_concurrent = max_concurrent
        self._lock = threading.Lock()
        self._redactor = RedactionFilter()
        self._cards: dict[str, dict[str, Any]] = {}
        self._events: dict[str, threading.Event] = {}
        self._decisions: dict[str, bool] = {}
        self._sessions: dict[str, str] = {}

    # ── 생성 / 상태 ───────────────────────────────────────────────────────────
    def _scrub(self, text: str) -> str:
        return self._redactor.scrub(text) if isinstance(text, str) else ""

    def _running_count(self) -> int:
        return sum(1 for c in self._cards.values() if c["status"] in ("running", "awaiting"))

    def create(self, opts: dict[str, Any]) -> str:
        prompt = (opts.get("prompt") or "").strip()
        if not prompt:
            raise ValueError("prompt required")
        task_id = uuid.uuid4().hex[:8]
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        with self._lock:
            if self._running_count() >= self._max_concurrent:
                raise RuntimeError(f"동시 작업 상한({self._max_concurrent}) 초과")
            self._events[task_id] = threading.Event()  # CB-4: dispatch 전 선생성
            self._cards[task_id] = {
                "id": task_id,
                "prompt": prompt[:200],
                "worker_type": opts.get("worker_type", "ollama"),
                "status": "running",
                "status_label": _STATUS["running"],
                "flags": [],
                "advice": None,
                "redacted_output_preview": None,
                "raw_available": False,
                "decision": None,
                "error": None,
                "created_at": now,
                "updated_at": now,
            }
            self._opts = getattr(self, "_opts", {})
        # opts 는 카드에 노출 안 함(민감 가능) — run_task 가 사용하도록 별도 보관
        with self._lock:
            self._cards[task_id]["_opts"] = opts
        return task_id

    def _update(self, task_id: str, **fields: Any) -> None:
        with self._lock:
            card = self._cards.get(task_id)
            if card is None:
                return
            card.update(fields)
            card["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            if "status" in fields:
                card["status_label"] = _STATUS.get(fields["status"], fields["status"])

    def _set_session(self, task_id: str, session: str) -> None:
        with self._lock:
            self._sessions[task_id] = session

    # ── 승인 게이트 (UI approver) ─────────────────────────────────────────────
    def _make_approver(self, task_id: str) -> Callable[[ApprovalRequest], bool]:
        def approver(req: ApprovalRequest) -> bool:
            # 표시 전 scrub (CB-1) — flags 는 패턴명(안전), advice/output 은 scrub.
            advice_summary = self._scrub(req.advice.summary) if req.advice else None
            self._update(
                task_id,
                status="awaiting",
                flags=list(req.flags),
                advice=advice_summary,
                redacted_output_preview=self._scrub(req.output_preview),
            )
            ev = self._events.get(task_id)
            if ev is None:  # 방어 (선생성 보장이나)
                return False
            got = ev.wait(timeout=self._timeout)
            if not got:  # CB-4: timeout = default-deny
                return False
            return bool(self._decisions.get(task_id, False))

        return approver

    def decide(self, task_id: str, accept: bool) -> bool:
        with self._lock:
            if task_id not in self._cards:
                return False
            self._decisions[task_id] = bool(accept)
            ev = self._events.get(task_id)
        if ev is not None:
            ev.set()
        return True

    # ── dispatch (백그라운드 thread 에서 실행) ────────────────────────────────
    def run_task(self, task_id: str) -> None:
        try:
            with self._lock:
                card = self._cards.get(task_id)
                opts = card.get("_opts", {}) if card else {}
            if card is None:
                return
            worker = self._worker_builder(opts, lambda s: self._set_session(task_id, s))
            registry = WorkerRegistry()
            registry.register(worker)
            gate = ApprovalGate(approver=self._make_approver(task_id))
            boss = self._boss_builder(opts)
            orch = Orchestrator(registry, ReviewGuard(), gate, boss=boss, memory=self._memory)
            report = orch.dispatch(card["prompt"], task_id, _WORKER_ALIAS)
            status = {
                OutcomeStatus.APPLIED: "applied",
                OutcomeStatus.DENIED: "denied",
                OutcomeStatus.WORKER_FAILED: "failed",
            }.get(report.status, "failed")
            self._update(
                task_id,
                status=status,
                flags=list(report.verdict.flags),
                advice=self._scrub(report.advice.summary) if report.advice else None,
                redacted_output_preview=self._scrub(report.result.output[:400]),
                decision=report.applied,
            )
        except Exception as exc:  # fail-soft (서버 무중단)
            self._update(task_id, status="failed", error=self._scrub(str(exc)))

    # ── 조회 (UI) ─────────────────────────────────────────────────────────────
    def snapshot(self) -> list[dict[str, Any]]:
        with self._lock:
            return [
                {k: v for k, v in c.items() if not k.startswith("_")}
                for c in sorted(self._cards.values(), key=lambda c: c["created_at"], reverse=True)
            ]

    def pane(self, task_id: str, tmux_runner: Callable[[list[str]], tuple] | None = None) -> str | None:
        """tmux 라이브 capture-pane (scrub + 길이 제한, CB-2). ollama 워커/세션 부재 = None."""
        with self._lock:
            session = self._sessions.get(task_id)
        if not session:
            return None
        runner = tmux_runner or _capture_runner
        try:
            _, out, _ = runner(["tmux", "capture-pane", "-p", "-t", session])
        except Exception:
            return None
        return self._scrub(out)[:_PANE_MAX]


def _capture_runner(argv: list[str]) -> tuple:
    import subprocess

    proc = subprocess.run(argv, capture_output=True, text=True)  # noqa: S603 (신뢰 tmux argv)
    return proc.returncode, proc.stdout, proc.stderr


# ── CSRF (CB-3) ───────────────────────────────────────────────────────────────
def same_origin(request) -> bool:
    """cross-origin POST 차단 (명령 실행 trigger 방어). Origin 있으면 host 일치 필수.

    브라우저는 cross-origin POST 에 Origin 을 보냄 → mismatch 거부. Origin 부재(비브라우저
    CLI = CSRF 벡터 아님) = 허용. localhost 단일 사용자 비례 방어.
    """
    origin = request.headers.get("origin")
    if not origin:
        return True
    host = request.headers.get("host", "")
    return host != "" and (origin.endswith("//" + host) or origin.endswith(host))


# ── Starlette routes (board 주입 = CB-7 hermetic test seam) ────────────────────
def make_jarvis_routes(board: JarvisTaskBoard) -> list:
    """주어진 board 에 바인딩된 jarvis 작업 routes. 테스트는 fake worker_builder board 주입."""
    import asyncio
    import json

    from starlette.responses import JSONResponse
    from starlette.routing import Route

    async def submit(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        try:
            data = json.loads(await request.body())
        except Exception:
            return JSONResponse({"error": "bad json"}, status_code=400)
        try:
            task_id = board.create(data)
        except (ValueError, RuntimeError) as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        # 백그라운드 dispatch (CB-4/CB-6: to_thread 로 sync dispatch, fire-and-forget).
        asyncio.create_task(asyncio.to_thread(board.run_task, task_id))
        return JSONResponse({"task_id": task_id})

    async def tasks(request):
        return JSONResponse({"tasks": board.snapshot()})

    async def decision(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        task_id = request.path_params.get("task_id")
        try:
            data = json.loads(await request.body())
        except Exception:
            data = {}
        dec = data.get("decision")
        if dec not in ("accept", "reject"):
            return JSONResponse({"error": "decision must be accept|reject"}, status_code=400)
        ok = board.decide(task_id, dec == "accept")
        return JSONResponse({"ok": ok}, status_code=200 if ok else 404)

    async def pane(request):
        task_id = request.path_params.get("task_id")
        pane_text = await asyncio.to_thread(board.pane, task_id)
        return JSONResponse({"pane": pane_text})

    return [
        Route("/api/jarvis/task", submit, methods=["POST"]),
        Route("/api/jarvis/tasks", tasks, methods=["GET"]),
        Route("/api/jarvis/task/{task_id}/decision", decision, methods=["POST"]),
        Route("/api/jarvis/task/{task_id}/pane", pane, methods=["GET"]),
    ]
