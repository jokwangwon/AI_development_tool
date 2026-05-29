"""TmuxWorker — tmux 패널 실 spawn + send-keys + capture-pane 워커 (TDD).

답습: docs/phase0/jarvis-v00-working-sprint-brief.md §3 + docs/phase0/tmux-nonce-sentinel-brief.md (74)
  - Worker Protocol 충족(alias + run(prompt, workdir) -> WorkerResult).
  - 흐름: new-session -d → send-keys → 완료 sentinel polling → capture-pane → kill-session.
  - 완료 sentinel = `__JARVIS_DONE_<nonce>_<exit_code>__` (per-session 무작위 nonce, 74 B-2 위조 표면 차단).
  - 세션 leak 방지: try/finally kill-session.

본 test 는 실 tmux 호출 0건 — runner 주입(SpyTmuxRunner) 한정. nonce_factory 주입으로 결정성.
"""
from __future__ import annotations

import re

import pytest

from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.worker import TmuxWorker, Worker, WorkerResult

# 테스트 고정 nonce (default uuid4 factory 를 주입 대체 — 결정성). 무작위성은 R test 별도.
_NONCE = "n0nceabcd1234"


class SpyTmuxRunner:
    """tmux subprocess 호출 캡처용. capture-pane 응답 스크립팅 가능."""

    def __init__(self, pane_text: str = "", capture_exit: int = 0,
                 new_session_exit: int = 0, send_keys_exit: int = 0,
                 kill_session_exit: int = 0) -> None:
        self.calls: list[list[str]] = []
        self._pane_text = pane_text
        self._capture_exit = capture_exit
        self._new_exit = new_session_exit
        self._send_exit = send_keys_exit
        self._kill_exit = kill_session_exit

    def __call__(self, argv: list[str]) -> tuple[int, str, str]:
        self.calls.append(list(argv))
        sub = argv[1] if len(argv) > 1 else ""
        if sub == "new-session":
            return self._new_exit, "", ""
        if sub == "send-keys":
            return self._send_exit, "", ""
        if sub == "capture-pane":
            return self._capture_exit, self._pane_text, ""
        if sub == "kill-session":
            return self._kill_exit, "", ""
        return 0, "", ""


def _done(exit_code: int = 0, body: str = "hello world", nonce: str = _NONCE) -> str:
    """완료 sentinel(nonce 포함) 포함 pane text 생성."""
    return f"$ run-command\n{body}\n__JARVIS_DONE_{nonce}_{exit_code}__\n$ "


def _mk(spy: SpyTmuxRunner, **kw) -> TmuxWorker:
    """고정 nonce 주입 TmuxWorker (테스트 결정성)."""
    kw.setdefault("alias", "t")
    kw.setdefault("argv", ["bash", "-lc"])
    return TmuxWorker(tmux_runner=spy, nonce_factory=lambda: _NONCE, **kw)


def test_implements_worker_protocol() -> None:
    w = _mk(SpyTmuxRunner(pane_text=_done()), alias="tmux-bash")
    assert isinstance(w, Worker)
    assert w.alias == "tmux-bash"


def test_run_invokes_tmux_lifecycle_in_order() -> None:
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    _mk(spy).run(prompt="echo hi", workdir="/tmp/ws-42")
    subs = [c[1] for c in spy.calls]
    assert subs[0] == "new-session"
    assert "send-keys" in subs
    assert "capture-pane" in subs
    assert subs[-1] == "kill-session"
    assert subs.index("new-session") < subs.index("send-keys")
    assert subs.index("send-keys") < subs.index("capture-pane")
    assert subs.index("capture-pane") < subs.index("kill-session")


def test_run_returns_pane_text_minus_sentinel() -> None:
    spy = SpyTmuxRunner(pane_text=_done(0, "result body line"))
    res = _mk(spy).run(prompt="echo hi", workdir="/tmp/ws")
    assert isinstance(res, WorkerResult)
    assert res.exit_code == 0
    assert res.is_error is False
    assert "result body line" in res.output
    assert "__JARVIS_DONE_" not in res.output     # nonce sentinel 가 사용자 출력에 leak 0
    assert res.cost_usd is None
    assert res.raw is None


def test_nonzero_sentinel_marks_error() -> None:
    spy = SpyTmuxRunner(pane_text=_done(2, "fail body"))
    res = _mk(spy).run(prompt="false", workdir="/tmp/ws")
    assert res.exit_code == 2
    assert res.is_error is True


def test_missing_sentinel_is_failure_not_silent_success() -> None:
    """sentinel 미발화 = pane 캡처 시점 미완료/타임아웃 → is_error=True(거짓 성공 금지)."""
    spy = SpyTmuxRunner(pane_text="some incomplete output\n$ ")
    res = _mk(spy, poll_attempts=2, poll_interval_s=0.0).run(prompt="hang", workdir="/tmp/ws")
    assert res.is_error is True
    assert res.exit_code != 0


def test_kill_session_runs_even_when_capture_fails() -> None:
    """capture-pane 자체가 실패해도 kill-session 발화(세션 leak 0)."""
    class BombRunner(SpyTmuxRunner):
        def __call__(self, argv: list[str]) -> tuple[int, str, str]:
            self.calls.append(list(argv))
            if len(argv) > 1 and argv[1] == "capture-pane":
                raise RuntimeError("capture-pane 폭발")
            return 0, "", ""

    spy = BombRunner()
    w = _mk(spy, poll_attempts=1, poll_interval_s=0.0)
    with pytest.raises(RuntimeError):
        w.run(prompt="hi", workdir="/tmp/ws")
    subs = [c[1] for c in spy.calls]
    assert "kill-session" in subs


def test_isolation_wrap_applied_to_inner_command() -> None:
    """격리 backend 의 wrap 이 tmux 패널 내 명령에 적용된다."""
    class SpyIso:
        name = "spy"

        def __init__(self) -> None:
            self.called_with: tuple[list[str], str] | None = None

        def wrap(self, cmd: list[str], workdir: str) -> list[str]:
            self.called_with = (list(cmd), workdir)
            return ["WRAPPED", *cmd]

    iso = SpyIso()
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    _mk(spy, isolation=iso).run(prompt="echo hi", workdir="/tmp/ws")
    assert iso.called_with is not None
    inner_cmd, wd = iso.called_with
    assert inner_cmd == ["bash", "-lc", "echo hi"]
    assert wd == "/tmp/ws"
    send_call = next(c for c in spy.calls if len(c) > 1 and c[1] == "send-keys")
    assert "WRAPPED" in " ".join(send_call)


def test_new_session_failure_skips_send_and_capture() -> None:
    """new-session 실패 시 send-keys / capture-pane 미호출 + is_error=True."""
    spy = SpyTmuxRunner(pane_text="", new_session_exit=1)
    res = _mk(spy).run(prompt="hi", workdir="/tmp/ws")
    subs = [c[1] for c in spy.calls]
    assert "send-keys" not in subs
    assert "capture-pane" not in subs
    assert res.is_error is True
    assert res.exit_code != 0


def test_default_passthrough_isolation() -> None:
    """isolation 미주입 시 PassthroughIsolation = inner cmd 변경 0."""
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    _mk(spy).run(prompt="echo X", workdir="/tmp/ws")
    send_call = next(c for c in spy.calls if len(c) > 1 and c[1] == "send-keys")
    payload = " ".join(send_call)
    assert "bash" in payload and "echo X" in payload


# ── T-FORGE (74 B-2): 위조 sentinel(구 고정 + 다른 nonce) → per-run regex 불일치 → is_error ──
def test_forged_sentinel_rejected_not_silent_success() -> None:
    forged = (
        "$ run-command\n"
        "attacker output __JARVIS_DONE_0__ and __JARVIS_DONE_wrongnonce_0__\n$ "
    )  # 구 고정 + 다른 nonce — 정상 nonce sentinel 부재
    spy = SpyTmuxRunner(pane_text=forged)
    res = _mk(spy, poll_attempts=2, poll_interval_s=0.0).run(prompt="x", workdir="/tmp/ws")
    assert res.is_error is True       # 위조로 거짓 완료 0
    assert res.exit_code != 0


# ── T-NONCE-MATCH (제어): 정상 nonce sentinel → 매칭 ──────────────────────────
def test_correct_nonce_sentinel_matches() -> None:
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    res = _mk(spy).run(prompt="x", workdir="/tmp/ws")
    assert res.exit_code == 0 and res.is_error is False


# ── T-COEXIST (74 B-2): 위조 + 정상 nonce 공존 → 정상 nonce 만 매칭(위조 무시) ──
def test_forged_and_real_coexist_real_wins() -> None:
    pane = (
        "$ run-command\n"
        "noise __JARVIS_DONE_99__ noise\n"          # 위조(구 고정, exit 99)
        f"__JARVIS_DONE_{_NONCE}_0__\n$ "            # 정상 nonce sentinel (exit 0)
    )
    spy = SpyTmuxRunner(pane_text=pane)
    res = _mk(spy).run(prompt="x", workdir="/tmp/ws")
    assert res.exit_code == 0          # 위조 99 무시, 정상 nonce(0) 권위
    assert res.is_error is False


# ── R 무작위성 (74 B-2): default factory(주입 0) → 2 run nonce 상이 ───────────
def test_default_nonce_factory_is_random_across_runs() -> None:
    def _nonce_in_send_keys(spy: SpyTmuxRunner) -> str:
        send = next(c for c in spy.calls if len(c) > 1 and c[1] == "send-keys")
        m = re.search(r"__JARVIS_DONE_([0-9a-f]+)_\$\?__", " ".join(send))
        assert m is not None
        return m.group(1)

    spy1, spy2 = SpyTmuxRunner(), SpyTmuxRunner()
    # default nonce_factory (주입 X) — pane 무 sentinel → missing(무시), nonce 캡처만 목적.
    TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy1,
               poll_attempts=1, poll_interval_s=0.0).run(prompt="x", workdir="/tmp/ws")
    TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy2,
               poll_attempts=1, poll_interval_s=0.0).run(prompt="x", workdir="/tmp/ws")
    n1, n2 = _nonce_in_send_keys(spy1), _nonce_in_send_keys(spy2)
    assert n1 != n2 and len(n1) >= 16   # uuid4 hex = 32 — 사전 예측 불가


# ── 빈 nonce 방어 (74 권고): nonce_factory 가 빈 문자열 → ValueError ──────────
def test_empty_nonce_rejected() -> None:
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=SpyTmuxRunner(),
                   nonce_factory=lambda: "")
    with pytest.raises(ValueError):
        w.run(prompt="x", workdir="/tmp/ws")


# ── 디딤돌0 취소 hook (brief §5 실행 중 취소 = 실 kill) ────────────────────────
def test_cancel_check_breaks_poll_and_kills_session() -> None:
    """cancel_check True → sentinel 미발화여도 poll 조기 종료 + kill-session(실 kill)."""
    spy = SpyTmuxRunner(pane_text="incomplete\n$ ")  # sentinel 부재(미완)
    w = _mk(spy, poll_attempts=999, poll_interval_s=0.0, cancel_check=lambda: True)
    res = w.run(prompt="long task", workdir="/tmp/ws")
    assert res.is_error is True
    assert res.exit_code == 130           # 취소 관행(128+SIGINT) — timeout(124)과 구분
    subs = [c[1] for c in spy.calls]
    assert subs[-1] == "kill-session"     # 실 kill = 자원 회수
    # poll_attempts=999 이나 cancel 로 capture-pane 호출 최소(<=1) — 폭주 0
    assert subs.count("capture-pane") <= 1


def test_cancel_distinct_from_timeout() -> None:
    """취소(130) 와 타임아웃(124) 은 다른 exit_code(원인 구분)."""
    spy_to = SpyTmuxRunner(pane_text="no sentinel\n$ ")
    res_to = _mk(spy_to, poll_attempts=1, poll_interval_s=0.0).run(prompt="x", workdir="/tmp/ws")
    assert res_to.exit_code == 124        # timeout

    spy_cx = SpyTmuxRunner(pane_text="no sentinel\n$ ")
    res_cx = _mk(spy_cx, poll_attempts=999, poll_interval_s=0.0,
                 cancel_check=lambda: True).run(prompt="x", workdir="/tmp/ws")
    assert res_cx.exit_code == 130        # cancel


def test_cancel_check_none_completes_normally() -> None:
    """cancel_check 미주입(default None) = 기존 동작 그대로(하위 호환)."""
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    res = _mk(spy).run(prompt="x", workdir="/tmp/ws")
    assert res.exit_code == 0 and res.is_error is False


def test_cancel_check_false_does_not_break() -> None:
    """cancel_check 가 계속 False → 정상 완료(취소 아님)."""
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    res = _mk(spy, cancel_check=lambda: False).run(prompt="x", workdir="/tmp/ws")
    assert res.exit_code == 0 and res.is_error is False
