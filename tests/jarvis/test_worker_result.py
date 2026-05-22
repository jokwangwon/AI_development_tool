"""WorkerResult — claude headless(`-p --output-format json`) 출력 파싱 테스트.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §3 (headless subprocess
1급, exit code=결정적 완료신호 + json 출력/total_cost_usd 비용신호).
"""
from __future__ import annotations

import json

from src.jarvis.worker import WorkerResult


def _claude_json(**over: object) -> str:
    base = {
        "type": "result",
        "subtype": "success",
        "is_error": False,
        "result": "task done",
        "total_cost_usd": 0.0123,
        "duration_ms": 4200,
        "num_turns": 3,
        "session_id": "abc",
    }
    base.update(over)
    return json.dumps(base)


def test_parse_success() -> None:
    r = WorkerResult.from_cli(exit_code=0, stdout=_claude_json())
    assert r.exit_code == 0
    assert r.output == "task done"
    assert r.cost_usd == 0.0123
    assert r.is_error is False
    assert r.succeeded is True


def test_is_error_flag_from_json() -> None:
    # exit 0 이어도 json is_error=true 면 실패로 본다
    r = WorkerResult.from_cli(exit_code=0, stdout=_claude_json(is_error=True))
    assert r.is_error is True
    assert r.succeeded is False


def test_nonzero_exit_is_authoritative() -> None:
    # exit code = 결정적 완료신호. 비0 이면 json 내용과 무관하게 실패.
    r = WorkerResult.from_cli(exit_code=1, stdout=_claude_json(is_error=False))
    assert r.exit_code == 1
    assert r.is_error is True
    assert r.succeeded is False


def test_invalid_json_preserves_raw_and_fails() -> None:
    # json 파싱 실패 = 출력 잘림/비표준 provider. raw 보존, 실패 처리(거짓 성공 금지).
    r = WorkerResult.from_cli(exit_code=0, stdout="not-json-at-all")
    assert r.is_error is True
    assert r.succeeded is False
    assert r.output == "not-json-at-all"
    assert r.raw is None


def test_cost_missing_is_none() -> None:
    payload = json.loads(_claude_json())
    del payload["total_cost_usd"]
    r = WorkerResult.from_cli(exit_code=0, stdout=json.dumps(payload))
    assert r.cost_usd is None
    assert r.succeeded is True


def test_raw_dict_exposed() -> None:
    r = WorkerResult.from_cli(exit_code=0, stdout=_claude_json(session_id="xyz"))
    assert r.raw is not None
    assert r.raw["session_id"] == "xyz"
