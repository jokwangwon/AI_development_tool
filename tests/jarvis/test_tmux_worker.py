"""TmuxWorker — tmux 패널 실 spawn + send-keys + capture-pane 워커 (TDD).

답습: docs/phase0/jarvis-v00-working-sprint-brief.md §3
  - Worker Protocol 충족(alias + run(prompt, workdir) -> WorkerResult).
  - 흐름: new-session -d → send-keys → 완료 sentinel polling → capture-pane → kill-session.
  - 완료 sentinel = `__JARVIS_DONE_<exit_code>__` (echo $?).
  - 격리 위임: IsolationBackend.wrap(argv, workdir) 그대로(MVP-0 트랙 B 답습).
  - 세션 leak 방지: try/finally kill-session.

본 test 는 실 tmux 호출 0건 — runner 주입(SpyTmuxRunner) 한정.
"""
from __future__ import annotations

from typing import Any

import pytest

from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.worker import TmuxWorker, Worker, WorkerResult


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


def _done(exit_code: int = 0, body: str = "hello world") -> str:
    """완료 sentinel 포함 pane text 생성."""
    return f"$ run-command\n{body}\n__JARVIS_DONE_{exit_code}__\n$ "


def test_implements_worker_protocol() -> None:
    w = TmuxWorker(alias="tmux-bash", argv=["bash", "-lc"],
                   tmux_runner=SpyTmuxRunner(pane_text=_done()))
    assert isinstance(w, Worker)
    assert w.alias == "tmux-bash"


def test_run_invokes_tmux_lifecycle_in_order() -> None:
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy)
    w.run(prompt="echo hi", workdir="/tmp/ws-42")
    subs = [c[1] for c in spy.calls]
    # 시작·송신·캡처·종료 모두 1회 이상 + 순서 강제
    assert subs[0] == "new-session"
    assert "send-keys" in subs
    assert "capture-pane" in subs
    assert subs[-1] == "kill-session"
    assert subs.index("new-session") < subs.index("send-keys")
    assert subs.index("send-keys") < subs.index("capture-pane")
    assert subs.index("capture-pane") < subs.index("kill-session")


def test_run_returns_pane_text_minus_sentinel() -> None:
    spy = SpyTmuxRunner(pane_text=_done(0, "result body line"))
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy)
    res = w.run(prompt="echo hi", workdir="/tmp/ws")
    assert isinstance(res, WorkerResult)
    assert res.exit_code == 0
    assert res.is_error is False
    assert "result body line" in res.output
    assert "__JARVIS_DONE_" not in res.output     # sentinel 가 사용자 출력에 leak 0
    assert res.cost_usd is None
    assert res.raw is None


def test_nonzero_sentinel_marks_error() -> None:
    spy = SpyTmuxRunner(pane_text=_done(2, "fail body"))
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy)
    res = w.run(prompt="false", workdir="/tmp/ws")
    assert res.exit_code == 2
    assert res.is_error is True


def test_missing_sentinel_is_failure_not_silent_success() -> None:
    """sentinel 미발화 = pane 캡처 시점 미완료/타임아웃 → is_error=True(거짓 성공 금지)."""
    spy = SpyTmuxRunner(pane_text="some incomplete output\n$ ")
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy,
                   poll_attempts=2, poll_interval_s=0.0)
    res = w.run(prompt="hang", workdir="/tmp/ws")
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
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy,
                   poll_attempts=1, poll_interval_s=0.0)
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
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], isolation=iso, tmux_runner=spy)
    w.run(prompt="echo hi", workdir="/tmp/ws")
    assert iso.called_with is not None
    inner_cmd, wd = iso.called_with
    assert inner_cmd == ["bash", "-lc", "echo hi"]
    assert wd == "/tmp/ws"
    # send-keys 호출에 WRAPPED 포함
    send_call = next(c for c in spy.calls if len(c) > 1 and c[1] == "send-keys")
    payload = " ".join(send_call)
    assert "WRAPPED" in payload


def test_new_session_failure_skips_send_and_capture() -> None:
    """new-session 실패 시 send-keys / capture-pane 미호출 + is_error=True."""
    spy = SpyTmuxRunner(pane_text="", new_session_exit=1)
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy)
    res = w.run(prompt="hi", workdir="/tmp/ws")
    subs = [c[1] for c in spy.calls]
    assert "send-keys" not in subs
    assert "capture-pane" not in subs
    assert res.is_error is True
    assert res.exit_code != 0


def test_default_passthrough_isolation() -> None:
    """isolation 미주입 시 PassthroughIsolation = inner cmd 변경 0."""
    spy = SpyTmuxRunner(pane_text=_done(0, "ok"))
    w = TmuxWorker(alias="t", argv=["bash", "-lc"], tmux_runner=spy)
    w.run(prompt="echo X", workdir="/tmp/ws")
    send_call = next(c for c in spy.calls if len(c) > 1 and c[1] == "send-keys")
    payload = " ".join(send_call)
    assert "bash" in payload and "echo X" in payload
