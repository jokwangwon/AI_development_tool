"""CliWorker — headless subprocess 워커 백엔드 테스트.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md
  - §3/D-2: headless subprocess(`claude -p --output-format json`) 1급.
  - Q-4: Worker(spawn/send/capture/done) — CLI 백엔드.
  - §5 v3-1: isolation backend 주입(트랙 A=passthrough).

subprocess runner 를 주입하여 실제 claude 호출 없이 검증(테스트 결정성).
"""
from __future__ import annotations

import json

from src.jarvis.isolation import PassthroughIsolation
from src.jarvis.worker import CliWorker


def _runner(record: dict[str, object], exit_code: int = 0, stdout: str | None = None):
    """주입용 가짜 runner — 호출 인자를 record 에 캡처."""

    def run(cmd: list[str], workdir: str) -> tuple[int, str, str]:
        record["cmd"] = cmd
        record["workdir"] = workdir
        payload = stdout if stdout is not None else json.dumps(
            {"result": "ok", "is_error": False, "total_cost_usd": 0.01}
        )
        return exit_code, payload, ""

    return run


def test_run_passes_prompt_to_command() -> None:
    rec: dict[str, object] = {}
    w = CliWorker(alias="claude", argv=["claude", "--output-format", "json", "-p"],
                  isolation=PassthroughIsolation(), runner=_runner(rec))
    w.run(prompt="build feature X", workdir="/tmp/ws")
    assert rec["cmd"] == ["claude", "--output-format", "json", "-p", "build feature X"]


def test_run_uses_workdir() -> None:
    rec: dict[str, object] = {}
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  isolation=PassthroughIsolation(), runner=_runner(rec))
    w.run(prompt="hi", workdir="/tmp/ws-42")
    assert rec["workdir"] == "/tmp/ws-42"


def test_run_applies_isolation_wrap() -> None:
    rec: dict[str, object] = {}

    class SpyIso:
        name = "spy"

        def __init__(self) -> None:
            self.called_with: tuple[list[str], str] | None = None

        def wrap(self, cmd: list[str], workdir: str) -> list[str]:
            self.called_with = (list(cmd), workdir)
            return ["SBX", *cmd]

    spy = SpyIso()
    w = CliWorker(alias="claude", argv=["claude", "-p"], isolation=spy,
                  runner=_runner(rec))
    w.run(prompt="hi", workdir="/tmp/ws")
    assert spy.called_with == (["claude", "-p", "hi"], "/tmp/ws")
    assert rec["cmd"] == ["SBX", "claude", "-p", "hi"]  # 격리 wrap 결과가 실행됨


def test_run_parses_success_result() -> None:
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  isolation=PassthroughIsolation(), runner=_runner({}))
    r = w.run(prompt="hi", workdir="/tmp/ws")
    assert r.succeeded is True
    assert r.output == "ok"
    assert r.cost_usd == 0.01


def test_run_nonzero_exit_is_error() -> None:
    w = CliWorker(alias="claude", argv=["claude", "-p"],
                  isolation=PassthroughIsolation(), runner=_runner({}, exit_code=2))
    r = w.run(prompt="hi", workdir="/tmp/ws")
    assert r.exit_code == 2
    assert r.is_error is True


def test_alias_exposed_for_routing() -> None:
    w = CliWorker(alias="codex", argv=["codex", "exec"],
                  isolation=PassthroughIsolation(), runner=_runner({}))
    assert w.alias == "codex"


def test_default_subprocess_runner_executes(tmp_path) -> None:
    # default runner(실 subprocess) 경로 — echo 로 claude json 모사
    payload = '{"result": "hi", "is_error": false, "total_cost_usd": 0.0}'
    w = CliWorker(alias="sh", argv=["sh", "-c", f"echo '{payload}' #"])
    r = w.run(prompt="ignored", workdir=str(tmp_path))
    assert r.exit_code == 0
    assert r.succeeded is True
    assert r.output == "hi"
