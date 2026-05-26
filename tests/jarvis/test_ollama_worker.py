"""OllamaWorker — LLM-only Ollama HTTP /api/chat 워커 (TDD).

답습: docs/phase0/jarvis-ollama-worker-promotion-brief.md
  - §1: 책무 = LLM 응답 + 마크다운 fence 제거 + workdir 안 단일 파일 (optional).
    fs 행동 능력 0 (LLM 텍스트 한정) = prompt injection 안전 본질.
  - §3: stdlib urllib.request 단독 (신규 dep 0), endpoint localhost 하드코딩.
  - §4: HTTP/JSON/content 실패 = is_error=True (raise 0). worker pattern 답습.

실 HTTP 호출 0건 — urllib.request.urlopen monkeypatch 한정.
"""
from __future__ import annotations

import io
import json
import os
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from src.jarvis.worker import OllamaWorker, Worker, WorkerResult


def _fake_response(payload: dict[str, Any]) -> io.BytesIO:
    return io.BytesIO(json.dumps(payload).encode("utf-8"))


def _chat(content: str) -> dict[str, Any]:
    return {"message": {"role": "assistant", "content": content}, "done": True}


# --- §1 Worker Protocol ---

def test_implements_worker_protocol(tmp_path: Path) -> None:
    w = OllamaWorker(alias="glm", model="glm-4.7-flash:latest")
    assert isinstance(w, Worker)
    assert w.alias == "glm"


# --- §2 정상 응답 → WorkerResult ---

def test_returns_worker_result_with_response_text(tmp_path: Path) -> None:
    w = OllamaWorker(alias="glm", model="m1")
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("hello"))):
        res = w.run(prompt="say hello", workdir=str(tmp_path))
    assert isinstance(res, WorkerResult)
    assert res.exit_code == 0
    assert res.is_error is False
    assert "hello" in res.output


# --- §1 output_filename=None: 파일 미생성 ---

def test_no_file_written_when_output_filename_none(tmp_path: Path) -> None:
    w = OllamaWorker(alias="glm", model="m", output_filename=None)
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("ignored"))):
        w.run(prompt="p", workdir=str(tmp_path))
    assert list(tmp_path.iterdir()) == []


# --- §1 output_filename: workdir 안 작성 + 내용 일치 ---

def test_writes_response_to_output_filename(tmp_path: Path) -> None:
    w = OllamaWorker(alias="glm", model="m", output_filename="hello.py")
    with patch("urllib.request.urlopen",
               return_value=_fake_response(_chat("print('hi')"))):
        w.run(prompt="p", workdir=str(tmp_path))
    out = (tmp_path / "hello.py")
    assert out.exists()
    assert out.read_text(encoding="utf-8") == "print('hi')"


# --- §1 마크다운 fence 제거 ---

def test_strips_code_fences_before_writing(tmp_path: Path) -> None:
    fenced = "```python\nprint('x')\n```"
    w = OllamaWorker(alias="glm", model="m", output_filename="x.py")
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat(fenced))):
        res = w.run(prompt="p", workdir=str(tmp_path))
    written = (tmp_path / "x.py").read_text(encoding="utf-8")
    assert "```" not in written
    assert written.strip() == "print('x')"
    assert "```" not in res.output


def test_strips_bare_fences_without_language(tmp_path: Path) -> None:
    """언어 토큰 없는 ``` 도 제거."""
    fenced = "```\nfoo\n```"
    w = OllamaWorker(alias="glm", model="m", output_filename="x.txt")
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat(fenced))):
        w.run(prompt="p", workdir=str(tmp_path))
    assert (tmp_path / "x.txt").read_text(encoding="utf-8").strip() == "foo"


# --- §1 path traversal 차단 ---

def test_path_traversal_blocked(tmp_path: Path) -> None:
    """output_filename 이 workdir 밖으로 escape 시도 → is_error + 파일 미생성."""
    outside = tmp_path / "outside"
    outside.mkdir()
    workdir = tmp_path / "ws"
    workdir.mkdir()
    w = OllamaWorker(alias="glm", model="m", output_filename="../outside/evil.py")
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("payload"))):
        res = w.run(prompt="p", workdir=str(workdir))
    assert res.is_error is True
    assert not (outside / "evil.py").exists()
    # workdir 안에도 파일 미생성
    assert list(workdir.iterdir()) == []


def test_absolute_path_traversal_blocked(tmp_path: Path) -> None:
    """절대 경로 output_filename 도 차단."""
    workdir = tmp_path / "ws"
    workdir.mkdir()
    bad_abs = str(tmp_path / "elsewhere.py")
    w = OllamaWorker(alias="glm", model="m", output_filename=bad_abs)
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat("payload"))):
        res = w.run(prompt="p", workdir=str(workdir))
    assert res.is_error is True
    assert not os.path.exists(bad_abs)


# --- §4 fail-soft (raise 0, is_error=True) ---

def test_http_failure_returns_is_error_not_raise(tmp_path: Path) -> None:
    import urllib.error
    w = OllamaWorker(alias="glm", model="m")
    with patch("urllib.request.urlopen",
               side_effect=urllib.error.URLError("connection refused")):
        res = w.run(prompt="p", workdir=str(tmp_path))
    assert res.is_error is True
    assert res.exit_code != 0


def test_malformed_json_response_returns_is_error(tmp_path: Path) -> None:
    bad = io.BytesIO(b"not-json")
    w = OllamaWorker(alias="glm", model="m")
    with patch("urllib.request.urlopen", return_value=bad):
        res = w.run(prompt="p", workdir=str(tmp_path))
    assert res.is_error is True


def test_missing_message_content_returns_is_error(tmp_path: Path) -> None:
    payload: dict[str, Any] = {"done": True}    # message.content 없음
    w = OllamaWorker(alias="glm", model="m")
    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
        res = w.run(prompt="p", workdir=str(tmp_path))
    assert res.is_error is True


def test_empty_content_returns_is_error(tmp_path: Path) -> None:
    w = OllamaWorker(alias="glm", model="m")
    with patch("urllib.request.urlopen", return_value=_fake_response(_chat(""))):
        res = w.run(prompt="p", workdir=str(tmp_path))
    assert res.is_error is True


# --- §3 endpoint hardcoded (SSRF 회피) ---

def test_endpoint_is_localhost_hardcoded() -> None:
    """생성자에 url/host/endpoint 인자 부재 = 외부 host 주입 경로 0."""
    import inspect
    sig = inspect.signature(OllamaWorker.__init__)
    forbidden = {"url", "host", "endpoint", "base_url"}
    assert not (set(sig.parameters) & forbidden), \
        f"OllamaWorker 생성자에 {forbidden} 인자 금지 (SSRF 회피)"


def test_request_targets_localhost_chat_endpoint(tmp_path: Path) -> None:
    """실 호출 URL 이 http://localhost:11434/api/chat 인지 검증."""
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["url"] = req.full_url
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _fake_response(_chat("ok"))

    w = OllamaWorker(alias="glm", model="m-x")
    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        w.run(prompt="hi", workdir=str(tmp_path))
    assert captured["url"] == "http://localhost:11434/api/chat"
    assert captured["data"]["model"] == "m-x"
    assert captured["data"]["stream"] is False


# --- §2 system_prompt 기본값 + override ---

def test_default_system_prompt_emphasizes_code_only(tmp_path: Path) -> None:
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _fake_response(_chat("ok"))

    w = OllamaWorker(alias="glm", model="m")
    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        w.run(prompt="p", workdir=str(tmp_path))
    sys_msg = captured["data"]["messages"][0]
    assert sys_msg["role"] == "system"
    # 기본 prompt = "code-only" 어휘 (마크다운/설명 금지)
    text = sys_msg["content"].lower()
    assert "code" in text
    assert "markdown" in text or "fence" in text or "explanation" in text


def test_custom_system_prompt_overrides_default(tmp_path: Path) -> None:
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _fake_response(_chat("ok"))

    w = OllamaWorker(alias="glm", model="m",
                     system_prompt="Reply ONLY in haiku.")
    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        w.run(prompt="p", workdir=str(tmp_path))
    sys_msg = captured["data"]["messages"][0]
    assert sys_msg["content"] == "Reply ONLY in haiku."
