"""CliPlanner — 디딤돌1d frontier CLI planner 불변식 고정 테스트.

답습: docs/phase0/jarvis-stone1d-frontier-planner-design-brief.md (v1.1)
  [[3plus1-consensus-2026-05-30-jarvis-stone1d-frontier-planner]] (REVISE→AWC).
  - IN-2: BossPlanner 의 frontier 구현(plan 공급원 유연). run_from_planner 무변경.
  - BL-3 schema flag + _parse_bossplan 방어 2층. BL-4 per-CLI extract.
  - BL-5 timeout(hang→RuntimeError→PLAN_UNAVAILABLE). frontier 도 untrusted.

트랙 A — 실 CLI 0건(runner mock). 실 codex 검증은 dogfooding 데모.
"""
from __future__ import annotations

import json

import pytest

from src.jarvis.boss import BossPlanner, Contract
from src.jarvis.planner import CliPlanner, claude_extractor


def _runner_factory(stdout: str, exit_code: int = 0, stderr: str = ""):
    calls: list = []

    def runner(cmd, timeout_s, stdin=""):
        calls.append((cmd, timeout_s, stdin))
        return exit_code, stdout, stderr

    runner.calls = calls  # type: ignore[attr-defined]
    return runner


def test_cliplanner_satisfies_bossplanner_protocol() -> None:
    p = CliPlanner(["codex", "exec"], runner=_runner_factory("{}"))
    assert isinstance(p, BossPlanner)


def test_cliplanner_parses_plan_from_stdout() -> None:
    plan_json = json.dumps({
        "subtasks": [
            {"desc": "백엔드", "worker_kind": "file", "depends_on": []},
            {"desc": "프론트", "worker_kind": "file", "depends_on": [0]},
        ],
        "contracts": [{"name": "api", "produced_by": 0}],
    })
    p = CliPlanner(["codex", "exec"], runner=_runner_factory(plan_json))
    out = p.plan("앱 만들어줘")
    assert len(out.subtasks) == 2
    assert out.subtasks[1].depends_on == (0,)
    assert out.contracts == (Contract(name="api", produced_by=0),)


def test_cliplanner_passes_prompt_and_timeout() -> None:
    runner = _runner_factory('{"subtasks": []}')
    p = CliPlanner(["codex", "exec", "-s", "read-only"], runner=runner, timeout_s=99.0)
    p.plan("작업")
    cmd, timeout, stdin = runner.calls[0]  # type: ignore[attr-defined]
    assert cmd[:4] == ["codex", "exec", "-s", "read-only"]  # argv prefix 보존
    assert "작업" in cmd[-1]          # positional 기본: prompt 가 argv tail
    assert timeout == 99.0            # BL-5 timeout 전달


def test_cliplanner_stdin_prompt_mode() -> None:
    """codex gotcha: stdin_prompt=True → prompt 가 stdin, argv 엔 prompt 부재."""
    runner = _runner_factory('{"subtasks": []}')
    p = CliPlanner(["codex", "exec"], runner=runner, stdin_prompt=True)
    p.plan("작업XYZ")
    cmd, _timeout, stdin = runner.calls[0]  # type: ignore[attr-defined]
    assert cmd == ["codex", "exec"]   # prompt 가 argv 에 없음
    assert "작업XYZ" in stdin          # prompt 는 stdin 으로


def test_cliplanner_exit_nonzero_raises() -> None:
    """BL-5/BL-1: CLI 실패(exit≠0) → RuntimeError(PLAN_UNAVAILABLE 유발)."""
    p = CliPlanner(["codex"], runner=_runner_factory("", exit_code=1, stderr="boom"))
    with pytest.raises(RuntimeError):
        p.plan("x")


def test_cliplanner_empty_result_raises() -> None:
    """empty result reject(거짓 진행 금지)."""
    p = CliPlanner(["codex"], runner=_runner_factory("   "))
    with pytest.raises(RuntimeError):
        p.plan("x")


def test_cliplanner_strips_code_fences() -> None:
    """grammar 부재 흡수 — CLI 가 ```json fence 붙여도 파싱."""
    fenced = "```json\n" + json.dumps({"subtasks": [
        {"desc": "a", "worker_kind": "file", "depends_on": []}]}) + "\n```"
    p = CliPlanner(["codex"], runner=_runner_factory(fenced))
    out = p.plan("x")
    assert len(out.subtasks) == 1


def test_cliplanner_malformed_raises() -> None:
    p = CliPlanner(["codex"], runner=_runner_factory("not json at all"))
    with pytest.raises(RuntimeError):
        p.plan("x")


# --- per-CLI extractor (BL-4) ---

def test_claude_extractor_unwraps_result_envelope() -> None:
    """claude --output-format json = {result: "<plan JSON>"} → result 추출(2단)."""
    plan_inner = json.dumps({"subtasks": [
        {"desc": "a", "worker_kind": "file", "depends_on": []}]})
    envelope = json.dumps({"result": plan_inner, "is_error": False, "total_cost_usd": 0.0})
    p = CliPlanner(["claude", "-p"], runner=_runner_factory(envelope),
                   extractor=claude_extractor)
    out = p.plan("x")
    assert len(out.subtasks) == 1


def test_claude_extractor_error_envelope_raises() -> None:
    """claude envelope is_error/exit≠0 → from_cli is_error → RuntimeError."""
    p = CliPlanner(["claude", "-p"],
                   runner=_runner_factory("garbage", exit_code=1),
                   extractor=claude_extractor)
    with pytest.raises(RuntimeError):
        p.plan("x")


# --- output_file (codex --output-last-message, BL-4 실측) ---

def test_cliplanner_reads_output_file(tmp_path) -> None:
    """codex 처럼 최종 메시지를 *파일*로 내는 CLI — output_file 읽기(stdout 무시)."""
    out = tmp_path / "codex_last.json"
    out.write_text(json.dumps({"subtasks": [
        {"desc": "a", "worker_kind": "file", "depends_on": []}],
        "contracts": [{"name": "x", "produced_by": 0}]}), encoding="utf-8")
    # stdout 에는 추론 로그(비-JSON)가 와도 무시 — 파일이 권위
    p = CliPlanner(["codex", "exec", "--output-last-message", str(out)],
                   runner=_runner_factory("...추론 로그...\nDone."),
                   output_file=str(out))
    res = p.plan("x")
    assert len(res.subtasks) == 1
    assert res.contracts == (Contract(name="x", produced_by=0),)


def test_cliplanner_output_file_missing_raises(tmp_path) -> None:
    p = CliPlanner(["codex"], runner=_runner_factory("log"),
                   output_file=str(tmp_path / "nonexistent.json"))
    with pytest.raises(RuntimeError):
        p.plan("x")


# --- codex_planner 팩토리 (디딤돌1d 안정화) ---

def test_codex_planner_factory_builds_bossplanner() -> None:
    """codex_planner = schema flag + output-last-message + RO sandbox 캡슐화."""
    from src.jarvis.planner import codex_planner

    p = codex_planner(timeout_s=10.0)
    assert isinstance(p, BossPlanner)
    # argv 에 schema flag(strict)·output-last-message·RO sandbox 포함
    argv = p._argv  # noqa: SLF001 (테스트 — 팩토리 조립 검증)
    assert "--output-schema" in argv
    assert "--output-last-message" in argv
    assert argv[argv.index("-s") + 1] == "read-only"
    assert p._output_file is not None  # noqa: SLF001
