"""jarvis CLI entrypoint (python -m src.jarvis) test — hermetic (실 ollama 0).

답습: docs/phase0/jarvis-cli-entrypoint-brief.md
  - 통제 핵심: ApprovalGate default-deny + R10 분리 표시(flags/advice/output) + --yes 명시.
  - main 통합 = OllamaWorker/OllamaBoss monkeypatch 주입 (실 urllib/ollama 0).
"""
from __future__ import annotations

import io

import pytest

from src.jarvis import __main__ as cli
from src.jarvis.approval import ApprovalRequest
from src.jarvis.boss import BossAdvice, StubBoss
from src.jarvis.orchestrator import OutcomeReport, OutcomeStatus
from src.jarvis.review import ReviewVerdict
from src.jarvis.worker import WorkerResult


def _req(flags=None, advice=None, preview="out") -> ApprovalRequest:
    return ApprovalRequest(
        summary="s", worker_alias="ollama",
        flags=flags or [], output_preview=preview, advice=advice,
    )


# ── T-1: auto_approver (--yes) ────────────────────────────────────────────────
def test_auto_approver_true() -> None:
    assert cli.auto_approver(_req()) is True


# ── T-2: interactive approver default-deny ────────────────────────────────────
@pytest.mark.parametrize(
    "ans,expected",
    [("y", True), ("yes", True), ("Y", True), ("YES", True), (" y ", True),
     ("", False), ("n", False), ("no", False), ("nope", False), ("yeah", False)],
)
def test_interactive_approver_default_deny(ans: str, expected: bool) -> None:
    out = io.StringIO()
    approver = cli.make_interactive_approver(input_fn=lambda _p: ans, out=out)
    assert approver(_req()) is expected


# ── T-3: R10 분리 표시 (flags/advice/output 각각 노출, advice 단독 의존 아님) ──
def test_interactive_approver_separates_flags_advice_output() -> None:
    out = io.StringIO()
    approver = cli.make_interactive_approver(input_fn=lambda _p: "n", out=out)
    approver(_req(flags=["privilege-sudo"], advice=BossAdvice(summary="위험없음"),
                  preview="RAW_OUTPUT_XYZ"))
    text = out.getvalue()
    assert "privilege-sudo" in text   # (1) 위험 flags 별도
    assert "위험없음" in text          # (2) advice 보조
    assert "RAW_OUTPUT_XYZ" in text    # (3) output raw — advice와 분리


# ── T-4: arg parse ────────────────────────────────────────────────────────────
def test_build_parser_flags() -> None:
    ns = cli.build_parser().parse_args(
        ["do X", "--yes", "--no-boss", "--no-memory", "--worker-model", "m1"]
    )
    assert ns.prompt == "do X"
    assert ns.yes is True and ns.no_boss is True and ns.no_memory is True
    assert ns.worker_model == "m1"


# ── T-5: print_report ─────────────────────────────────────────────────────────
def test_print_report_applied() -> None:
    out = io.StringIO()
    wr = WorkerResult(exit_code=0, output="hello out", cost_usd=None, is_error=False, raw=None)
    rep = OutcomeReport("p", "ollama", wr, ReviewVerdict(ok=False, flags=["force-push"]),
                        approved=True, applied=True, status=OutcomeStatus.APPLIED,
                        advice=BossAdvice(summary="검토 ok"))
    cli.print_report(rep, out=out)
    t = out.getvalue()
    assert "applied" in t and "hello out" in t and "force-push" in t and "검토 ok" in t


# ── T-6: main 통합 (fake worker/boss 주입 — 실 ollama 0) ───────────────────────
class _FakeWorker:
    def __init__(self, **kw) -> None:
        self.alias = kw.get("alias", "ollama")

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        return WorkerResult(exit_code=0, output=f"done: {prompt}", cost_usd=None,
                            is_error=False, raw=None)


class _FailWorker:
    def __init__(self, **kw) -> None:
        self.alias = kw.get("alias", "ollama")

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        return WorkerResult(exit_code=1, output="boom", cost_usd=None, is_error=True, raw=None)


def test_main_applied(monkeypatch) -> None:
    monkeypatch.setattr(cli, "OllamaWorker", _FakeWorker)
    monkeypatch.setattr(cli, "OllamaBoss",
                        lambda model, **kw: StubBoss(name=model, advice=BossAdvice(summary="ok")))
    code = cli.main(["build fizzbuzz", "--yes", "--no-memory"])
    assert code == 0  # APPLIED


def test_main_worker_failed(monkeypatch) -> None:
    monkeypatch.setattr(cli, "OllamaWorker", _FailWorker)
    code = cli.main(["bad task", "--yes", "--no-boss", "--no-memory"])
    assert code == 1  # WORKER_FAILED


def test_main_denied(monkeypatch) -> None:
    monkeypatch.setattr(cli, "OllamaWorker", _FakeWorker)
    monkeypatch.setattr("builtins.input", lambda _p: "n")  # default-deny
    code = cli.main(["some task", "--no-boss", "--no-memory"])
    assert code == 2  # DENIED


# ── T-8 (73 entry): worker-type 분기 (build_orchestrator) ─────────────────────
def test_build_orchestrator_worker_type_tmux() -> None:
    from src.jarvis.worker import OllamaWorker, TmuxWorker

    ns_tmux = cli.build_parser().parse_args(
        ["t", "--worker-type", "tmux", "--tmux-argv", "bash -lc", "--no-boss", "--no-memory"]
    )
    orch = cli.build_orchestrator(ns_tmux, cli.auto_approver)
    assert isinstance(orch._registry.select("ollama"), TmuxWorker)  # default alias

    ns_ollama = cli.build_parser().parse_args(["t", "--no-boss", "--no-memory"])
    orch2 = cli.build_orchestrator(ns_ollama, cli.auto_approver)
    assert isinstance(orch2._registry.select("ollama"), OllamaWorker)


# ── T-9 (73): arg parse — tmux 옵션 ───────────────────────────────────────────
def test_build_parser_tmux_flags() -> None:
    ns = cli.build_parser().parse_args(
        ["fix bug", "--worker-type", "tmux", "--tmux-argv", "claude -p",
         "--isolation", "landlock", "--poll-attempts", "10", "--poll-interval", "0.5"]
    )
    assert ns.worker_type == "tmux"
    assert ns.tmux_argv == "claude -p"
    assert ns.isolation == "landlock"
    assert ns.poll_attempts == 10 and ns.poll_interval == 0.5


# ── T-10 (73): main 통합 tmux (fake TmuxWorker 주입 — 실 tmux 0) ──────────────
def test_main_tmux_applied(monkeypatch) -> None:
    monkeypatch.setattr(cli, "TmuxWorker", _FakeWorker)  # 실 tmux spawn 0
    code = cli.main(["echo hi", "--worker-type", "tmux", "--yes", "--no-boss", "--no-memory"])
    assert code == 0  # APPLIED


# ── T-11 (73, B-1): landlock fail-closed → main RuntimeError catch → exit 1 ───
def test_main_landlock_fail_closed(monkeypatch) -> None:
    class _RaisingIsolation:
        name = "landlock"

        def wrap(self, cmd, workdir):
            raise RuntimeError("Landlock sandboxer 없음 — make -C src/jarvis/sandbox 필요")

    # 실 TmuxWorker + 부재 sandboxer 모사 isolation → wrap 이 run 첫 줄에서 raise (tmux 미spawn).
    monkeypatch.setattr(cli, "LandlockIsolation", _RaisingIsolation)
    code = cli.main(
        ["do x", "--worker-type", "tmux", "--isolation", "landlock", "--yes", "--no-boss", "--no-memory"]
    )
    assert code == 1  # 워커 실행 중단 (fail-closed, 무격리 fallback 0)
