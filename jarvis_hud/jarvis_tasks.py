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
from src.jarvis.ledger import LedgerLog
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
    "cancelled": "취소",       # 디딤돌0: 실행 중 취소(반영 안 함)
    "interrupted": "중단됨",   # 디딤돌0: 재시작 고아(자동 복구 없음)
}

# 재시작 fold 시 살아있는 task 로 오인하면 안 되는 완결 상태(LedgerLog._TERMINAL 동형).
_TERMINAL = frozenset({"applied", "denied", "failed", "cancelled", "interrupted"})


def _default_worker_builder(
    opts: dict[str, Any],
    on_session: Callable[[str], None],
    cancel_check: Callable[[], bool],
):
    """opts → OllamaWorker(텍스트) 또는 TmuxWorker(명령 실행 + isolation + 세션 hook + 취소).

    cancel_check = 디딤돌0 실행 중 취소(brief §5). TmuxWorker poll 루프가 확인 → 실 kill.
    OllamaWorker 는 HTTP 추론 in-flight 취소 경로 부재(R4) — board 가 포기 마킹만.
    """
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
            cancel_check=cancel_check,
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


def _card_skeleton(
    task_id: str, prompt: str = "", worker_type: str = "ollama", now: str = "",
) -> dict[str, Any]:
    """카드 기본 필드 — create() 신규 + _restore() fold 병합 공통 골격.

    UI 가 기대하는 키 전부 보장 → 복원 카드도 누락 없이 렌더(restore 시 fold 필드가 override).
    """
    return {
        "id": task_id,
        "prompt": prompt,
        "worker_type": worker_type,
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
        ledger: LedgerLog | None = None,
        tmux_runner: Callable[[list[str]], tuple] | None = None,
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
        # 디딤돌0: 영속 레저(append-only event-sourcing) + 취소 신호 + tmux kill runner.
        self._ledger = ledger
        self._cancels: dict[str, threading.Event] = {}
        self._tmux_runner = tmux_runner or _capture_runner
        self._restore()

    # ── 영속 레저 (디딤돌0) ─────────────────────────────────────────────────────
    def _record(self, task_id: str, event: str, **fields: Any) -> None:
        """레저 1 이벤트 적재 (fail-soft, ledger 부재=no-op). 호출측은 이미 scrub 된 메타만.

        raw 워커 출력은 절대 전달하지 않는다(redacted_output_preview = scrub 완료분, CB-1).
        """
        if self._ledger is None:
            return
        try:
            self._ledger.record(task_id, event, **fields)
        except Exception:
            return  # 두 겹 fail-soft — 레저 부재가 dispatch 차단 0건.

    def _restore(self) -> None:
        """재시작 시 레저 fold → _cards 복원. 비완결(running/awaiting) = interrupted(고아).

        복원 카드는 *역사적* 상태(완결/중단) — 라이브 Event/취소 신호 없음(재배선 안 함).
        """
        if self._ledger is None:
            return
        folded = self._ledger.fold()
        with self._lock:
            for task_id, card in folded.items():
                merged = {**_card_skeleton(task_id), **card}
                merged["status_label"] = _STATUS.get(merged["status"], merged["status"])
                self._cards[task_id] = merged

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
        wtype = opts.get("worker_type", "ollama")
        with self._lock:
            if self._running_count() >= self._max_concurrent:
                raise RuntimeError(f"동시 작업 상한({self._max_concurrent}) 초과")
            self._events[task_id] = threading.Event()   # CB-4: dispatch 전 선생성
            self._cancels[task_id] = threading.Event()  # 디딤돌0 취소 신호(선생성, race 0)
            card = _card_skeleton(task_id, prompt[:200], wtype, now)
            # opts 는 카드에 노출 안 함(민감 가능) — run_task 만 사용.
            card["_opts"] = opts
            self._cards[task_id] = card
        # 레저 created 이벤트 — prompt 는 사용자 입력이라 scrub(B5 영속=scrub 메타만).
        self._record(task_id, "created", prompt=self._scrub(prompt[:200]),
                     worker_type=wtype, status="running", created_at=now)
        return task_id

    def _is_cancelled(self, task_id: str) -> bool:
        ev = self._cancels.get(task_id)
        return ev is not None and ev.is_set()

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
            preview = self._scrub(req.output_preview)
            self._update(
                task_id,
                status="awaiting",
                flags=list(req.flags),
                advice=advice_summary,
                redacted_output_preview=preview,
            )
            # 레저 awaiting 이벤트 (scrub 메타만 — raw 미영속, CB-1/B5).
            self._record(task_id, "awaiting", status="awaiting", flags=list(req.flags),
                         advice=advice_summary, redacted_output_preview=preview)
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

    # ── 취소 (실행 중, brief §5) ──────────────────────────────────────────────
    def cancel(self, task_id: str) -> bool:
        """실행 중 취소 — tmux=실 kill / ollama=포기 마킹. 반영 안 함(default-deny).

        완결(terminal) task 는 no-op(False). cancel 신호로 워커 poll 조기 종료(tmux),
        awaiting approver 를 deny 로 깨움, tmux 세션 실 kill(자원 회수). OllamaWorker 는
        HTTP 추론 in-flight 취소 경로 부재(R4) → 백그라운드 추론은 timeout 까지 GPU 점유
        (자원 회수 한계) — 카드만 cancelled 마킹.
        """
        with self._lock:
            card = self._cards.get(task_id)
            if card is None or card["status"] in _TERMINAL:
                return False
            self._decisions[task_id] = False        # 반영 안 함(default-deny)
            cancel_ev = self._cancels.get(task_id)
            approve_ev = self._events.get(task_id)
            session = self._sessions.get(task_id)
        if cancel_ev is not None:
            cancel_ev.set()                          # 워커 poll 루프 조기 종료(tmux)
        if approve_ev is not None:
            approve_ev.set()                         # awaiting approver 를 deny 로 깨움
        if session:                                  # tmux 실 kill(ollama=세션 부재 skip)
            try:
                self._tmux_runner(["tmux", "kill-session", "-t", session])
            except Exception:
                pass
        self._update(task_id, status="cancelled", decision=False)
        self._record(task_id, "cancelled", status="cancelled", decision=False)
        return True

    # ── dispatch (백그라운드 thread 에서 실행) ────────────────────────────────
    def run_task(self, task_id: str) -> None:
        try:
            with self._lock:
                card = self._cards.get(task_id)
                opts = card.get("_opts", {}) if card else {}
            if card is None:
                return
            worker = self._worker_builder(
                opts,
                lambda s: self._set_session(task_id, s),
                lambda: self._is_cancelled(task_id),   # 디딤돌0 취소 hook(tmux poll 조기 종료)
            )
            registry = WorkerRegistry()
            registry.register(worker)
            gate = ApprovalGate(approver=self._make_approver(task_id))
            boss = self._boss_builder(opts)
            orch = Orchestrator(registry, ReviewGuard(), gate, boss=boss, memory=self._memory)
            report = orch.dispatch(card["prompt"], task_id, _WORKER_ALIAS)
            if self._is_cancelled(task_id):
                return  # 취소 마킹 승리 — 워커 결과로 cancelled 덮어쓰지 않음
            status = {
                OutcomeStatus.APPLIED: "applied",
                OutcomeStatus.DENIED: "denied",
                OutcomeStatus.WORKER_FAILED: "failed",
            }.get(report.status, "failed")
            advice = self._scrub(report.advice.summary) if report.advice else None
            preview = self._scrub(report.result.output[:400])
            self._update(
                task_id,
                status=status,
                flags=list(report.verdict.flags),
                advice=advice,
                redacted_output_preview=preview,
                decision=report.applied,
            )
            # 레저 resolved 이벤트 (scrub 메타만 — raw 미영속, CB-1/B5).
            self._record(task_id, "resolved", status=status, flags=list(report.verdict.flags),
                         advice=advice, redacted_output_preview=preview, decision=report.applied)
        except Exception as exc:  # fail-soft (서버 무중단)
            if self._is_cancelled(task_id):
                return  # 취소 후 예외 = cancelled 보존
            err = self._scrub(str(exc))
            self._update(task_id, status="failed", error=err)
            self._record(task_id, "resolved", status="failed", error=err)

    # ── 제거 (UI dismiss — append-only 존중) ─────────────────────────────────
    def dismiss(self, task_id: str) -> bool:
        """완결(terminal) 카드를 보드에서 제거 + `dismissed` 이벤트 기록.

        진행중/승인대기 = 제거 불가(False, 보호 — 라이브 작업 유실 방지). 레저는
        append-only 라 *삭제* 안 함 — `dismissed` 이벤트로 fold 제외(재시작해도 안 돌아옴).
        """
        with self._lock:
            card = self._cards.get(task_id)
            if card is None or card["status"] not in _TERMINAL:
                return False
            self._cards.pop(task_id, None)
            self._events.pop(task_id, None)
            self._cancels.pop(task_id, None)
            self._sessions.pop(task_id, None)
            self._decisions.pop(task_id, None)
        self._record(task_id, "dismissed")
        return True

    def dismiss_completed(self) -> int:
        """완결 카드 일괄 제거. 제거 개수 반환(진행중/승인대기는 유지)."""
        with self._lock:
            targets = [tid for tid, c in self._cards.items() if c["status"] in _TERMINAL]
        return sum(1 for tid in targets if self.dismiss(tid))

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
        runner = tmux_runner or self._tmux_runner  # cancel() 과 동일 injection seam(기본=_capture_runner)
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

    async def cancel(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        task_id = request.path_params.get("task_id")
        # cancel = tmux kill 포함(subprocess) → to_thread (이벤트 루프 비차단, 76 답습).
        ok = await asyncio.to_thread(board.cancel, task_id)
        return JSONResponse({"ok": ok}, status_code=200 if ok else 404)

    async def dismiss(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        task_id = request.path_params.get("task_id")
        ok = board.dismiss(task_id)
        return JSONResponse({"ok": ok}, status_code=200 if ok else 404)

    async def dismiss_completed(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        count = board.dismiss_completed()
        return JSONResponse({"count": count})

    async def pane(request):
        task_id = request.path_params.get("task_id")
        pane_text = await asyncio.to_thread(board.pane, task_id)
        return JSONResponse({"pane": pane_text})

    return [
        Route("/api/jarvis/task", submit, methods=["POST"]),
        Route("/api/jarvis/tasks", tasks, methods=["GET"]),
        Route("/api/jarvis/tasks/dismiss-completed", dismiss_completed, methods=["POST"]),
        Route("/api/jarvis/task/{task_id}/decision", decision, methods=["POST"]),
        Route("/api/jarvis/task/{task_id}/cancel", cancel, methods=["POST"]),
        Route("/api/jarvis/task/{task_id}/dismiss", dismiss, methods=["POST"]),
        Route("/api/jarvis/task/{task_id}/pane", pane, methods=["GET"]),
    ]
