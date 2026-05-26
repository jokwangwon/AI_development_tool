"""OllamaBoss — Ollama HTTP `/api/chat` 직결 BossLLM 구현 (TDD).

답습: docs/phase0/jarvis-v00-working-sprint-brief.md §2
  - BossLLM Protocol 충족(`name`, `advise(AdviceRequest) -> BossAdvice`)
  - stdlib `urllib.request` 단독(신규 dep 0, `ollama` SDK import 0 — `.importlinter` 답습)
  - endpoint = `http://localhost:11434/api/chat` 하드코딩(SSRF 회피)
  - HTTP 실패 → RuntimeError (R3 호출측 누락→경고 변환 답습)
  - 응답 → BossAdvice(summary=text, extra_flags=[], advisory_failed=False)

본 test 는 실 HTTP 호출 0건 — urllib.request.urlopen monkeypatch 한정.
"""
from __future__ import annotations

import io
import json
from typing import Any
from unittest.mock import patch

import pytest

from src.jarvis.boss import AdviceRequest, BossAdvice, BossLLM, OllamaBoss


def _fake_response(payload: dict[str, Any]) -> io.BytesIO:
    """urlopen 응답 객체 모사 — read() 가 JSON bytes 반환."""
    buf = io.BytesIO(json.dumps(payload).encode("utf-8"))
    return buf


def test_ollama_boss_implements_protocol() -> None:
    boss = OllamaBoss(model="qwen3-30b-a3b-instruct-2507-bartowski:latest")
    assert isinstance(boss, BossLLM)
    assert boss.name == "qwen3-30b-a3b-instruct-2507-bartowski:latest"


def test_ollama_boss_advise_returns_text_only_advice() -> None:
    boss = OllamaBoss(model="m1")
    payload = {"message": {"role": "assistant", "content": "검토 요약 — 위험 없음."}, "done": True}
    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
        out = boss.advise(AdviceRequest(prompt="p", worker_alias="claude",
                                        output="hello", deterministic_flags=[]))
    assert isinstance(out, BossAdvice)
    assert out.summary == "검토 요약 — 위험 없음."
    assert out.extra_flags == []        # R2 텍스트 전용 답습 — 자동 flag 추출 0건
    assert out.advisory_failed is False


def test_ollama_boss_advise_posts_chat_endpoint_with_model() -> None:
    """endpoint·모델·prompt 가 정확히 HTTP body 에 실리는가."""
    boss = OllamaBoss(model="m1")
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["url"] = req.full_url
        captured["data"] = json.loads(req.data.decode("utf-8"))
        captured["timeout"] = timeout
        return _fake_response({"message": {"content": "ok"}, "done": True})

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        boss.advise(AdviceRequest(prompt="작업 X", worker_alias="claude",
                                  output="결과 Y", deterministic_flags=["risk"]))

    assert captured["url"] == "http://localhost:11434/api/chat"
    assert captured["data"]["model"] == "m1"
    assert captured["data"]["stream"] is False
    msgs = captured["data"]["messages"]
    assert msgs[0]["role"] == "system"
    # system prompt 가 텍스트-전용 책무를 명시
    assert "텍스트" in msgs[0]["content"] or "text" in msgs[0]["content"].lower()
    # 사용자 prompt / worker 출력 / deterministic flags 가 user 메시지에 포함
    user_blob = msgs[-1]["content"]
    assert "작업 X" in user_blob
    assert "결과 Y" in user_blob
    assert "risk" in user_blob
    assert captured["timeout"] is not None and captured["timeout"] > 0


def test_ollama_boss_advise_raises_on_http_failure() -> None:
    """HTTP 예외 → RuntimeError (R3 호출측 처리 답습)."""
    import urllib.error
    boss = OllamaBoss(model="m1")
    err = urllib.error.URLError("connection refused")
    with patch("urllib.request.urlopen", side_effect=err):
        with pytest.raises(RuntimeError):
            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                      output="o", deterministic_flags=[]))


def test_ollama_boss_advise_raises_on_malformed_json() -> None:
    """응답이 JSON 아니면 RuntimeError — 부재≠안전 답습(silent empty advice 금지)."""
    boss = OllamaBoss(model="m1")
    bad = io.BytesIO(b"not-json")
    with patch("urllib.request.urlopen", return_value=bad):
        with pytest.raises(RuntimeError):
            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                      output="o", deterministic_flags=[]))


def test_ollama_boss_advise_raises_on_missing_content() -> None:
    """응답 schema 누락 → RuntimeError (silent empty 차단)."""
    boss = OllamaBoss(model="m1")
    payload = {"done": True}  # message.content 없음
    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
        with pytest.raises(RuntimeError):
            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                      output="o", deterministic_flags=[]))


def test_ollama_boss_endpoint_is_localhost_only() -> None:
    """endpoint = localhost:11434 하드코딩 (SSRF 회피 답습)."""
    boss = OllamaBoss(model="m1")
    # endpoint 인자로 외부 host 주입 불가 — 생성자 시그니처에 url 인자 없음
    import inspect
    sig = inspect.signature(OllamaBoss.__init__)
    assert "url" not in sig.parameters
    assert "host" not in sig.parameters
    assert "endpoint" not in sig.parameters
