"""HttpServiceWorker — 범용 HTTP 서비스 워커 (TDD, R5).

답습: docs/architecture/uncensored-prompt-to-image-pipeline-design.md §3.1 (b)
  - 범용: gen_gate·voice_lab·motion_lab 공통 `/api/generate` 규약을 워커 레벨로
    흡수(modality=인자, 능력축 폭발 차단).
  - base_url = localhost 강제 (R7) — OllamaWorker 하드코딩 답습, 외부 URL 거부(SSRF).
  - 견고화 (R4): 비-200·202 → is_error=True (거짓 성공 금지).

실 HTTP 호출 0건 — urllib.request.urlopen monkeypatch 한정 (GPU 무관 스켈레톤).
gen_gate /api/generate 계약(실측 server.py):
  - 200: {"id", "file", "url": "/outputs/..", ...}  (동기 이미지)
  - 202: {"id", "status": "running", ...}            (비동기 3d — 거짓 성공 금지)
  - 400/403/404/500/501: {"error": "..."}
"""
from __future__ import annotations

import io
import json
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from src.jarvis.worker import HttpServiceWorker, Worker, WorkerResult


def _resp(payload: dict[str, Any], status: int = 200) -> Any:
    """urllib HTTPResponse-유사 mock — getcode()/read() 제공."""
    body = io.BytesIO(json.dumps(payload).encode("utf-8"))
    body.getcode = lambda: status  # type: ignore[attr-defined]
    body.status = status           # type: ignore[attr-defined]
    return body


# --- §1 Worker Protocol ---

def test_implements_worker_protocol(tmp_path: Path) -> None:
    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="animagine-xl-4.0"
    )
    assert isinstance(w, Worker)
    assert w.alias == "gengate"


# --- §2 payload 조립 (model=unit, prompt, commercial, **opts) ---

def test_posts_to_api_generate_with_unit_and_prompt(tmp_path: Path) -> None:
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["url"] = req.full_url
        captured["data"] = json.loads(req.data.decode("utf-8"))
        captured["timeout"] = timeout
        return _resp({"id": "f1", "file": "f1.png", "url": "/outputs/f1.png"})

    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800",
        unit="animagine-xl-4.0", commercial=True,
    )
    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        w.run(prompt="a knight", workdir=str(tmp_path))

    assert captured["url"] == "http://localhost:8800/api/generate"
    assert captured["data"]["model"] == "animagine-xl-4.0"
    assert captured["data"]["prompt"] == "a knight"
    assert captured["data"]["commercial"] is True


def test_opts_merged_into_payload(tmp_path: Path) -> None:
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _resp({"id": "f1", "file": "f1.png", "url": "/outputs/f1.png"})

    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800",
        unit="animagine-xl-4.0", opts={"style": "anime-illustration", "seed": 777},
    )
    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        w.run(prompt="x", workdir=str(tmp_path))
    assert captured["data"]["style"] == "anime-illustration"
    assert captured["data"]["seed"] == 777
    # opts 가 핵심 필드를 덮어쓰지 못함 (model/prompt 우선)
    assert captured["data"]["model"] == "animagine-xl-4.0"
    assert captured["data"]["prompt"] == "x"


# --- §3 200 정상 → 이미지 경로 + did_act=True ---

def test_success_returns_path_and_did_act(tmp_path: Path) -> None:
    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="animagine-xl-4.0"
    )
    with patch(
        "urllib.request.urlopen",
        return_value=_resp({"id": "abc", "file": "abc.png", "url": "/outputs/abc.png"}),
    ):
        res = w.run(prompt="x", workdir=str(tmp_path))
    assert isinstance(res, WorkerResult)
    assert res.exit_code == 0
    assert res.is_error is False
    assert res.did_act is True
    # 산출 이미지 경로가 output 에 노출(url 또는 file)
    assert "/outputs/abc.png" in res.output or "abc.png" in res.output


# --- §4 R4: 202 (async 편입) → is_error=True (거짓 성공 금지) ---

def test_202_async_is_error(tmp_path: Path) -> None:
    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="hunyuan3d"
    )
    with patch(
        "urllib.request.urlopen",
        return_value=_resp({"id": "j1", "status": "running"}, status=202),
    ):
        res = w.run(prompt="x", workdir=str(tmp_path))
    assert res.is_error is True
    assert res.did_act is not True  # 거짓 성공 금지


# --- §4 R4: 비-200 (403 등급차단 / 404 미등록 / 500) → is_error=True ---

@pytest.mark.parametrize("status", [400, 403, 404, 500, 501])
def test_non_200_is_error(tmp_path: Path, status: int) -> None:
    import urllib.error

    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="animagine-xl-4.0"
    )
    # urllib 는 4xx/5xx 를 HTTPError 로 raise — 워커가 이를 흡수해 is_error 로 변환.
    err = urllib.error.HTTPError(
        url="http://localhost:8800/api/generate", code=status,
        msg="err", hdrs=None, fp=io.BytesIO(b'{"error":"blocked"}'),
    )
    with patch("urllib.request.urlopen", side_effect=err):
        res = w.run(prompt="x", workdir=str(tmp_path))
    assert res.is_error is True
    assert res.exit_code != 0


# --- §3 R7: base_url 비-localhost 거부 (SSRF) ---

@pytest.mark.parametrize(
    "bad_url",
    [
        "http://evil.com:8800",
        "http://169.254.169.254",       # cloud metadata
        "http://10.0.0.5:8800",
        "https://example.org",
    ],
)
def test_non_localhost_base_url_rejected(bad_url: str) -> None:
    with pytest.raises(ValueError):
        HttpServiceWorker(alias="gengate", base_url=bad_url, unit="m")


@pytest.mark.parametrize(
    "ok_url",
    [
        "http://localhost:8800",
        "http://127.0.0.1:8800",
        "http://localhost",
    ],
)
def test_localhost_base_url_accepted(ok_url: str) -> None:
    w = HttpServiceWorker(alias="gengate", base_url=ok_url, unit="m")
    assert w.alias == "gengate"


# --- §4 fail-soft: HTTP 연결 실패 → is_error (raise 0) ---

def test_connection_failure_returns_is_error(tmp_path: Path) -> None:
    import urllib.error

    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="m"
    )
    with patch(
        "urllib.request.urlopen",
        side_effect=urllib.error.URLError("connection refused"),
    ):
        res = w.run(prompt="x", workdir=str(tmp_path))
    assert res.is_error is True
    assert res.exit_code != 0


def test_malformed_json_response_is_error(tmp_path: Path) -> None:
    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="m"
    )
    bad = io.BytesIO(b"not-json")
    bad.getcode = lambda: 200  # type: ignore[attr-defined]
    with patch("urllib.request.urlopen", return_value=bad):
        res = w.run(prompt="x", workdir=str(tmp_path))
    assert res.is_error is True


# --- §3 200 인데 file/url 누락 → is_error (거짓 성공 금지) ---

def test_success_status_but_no_path_is_error(tmp_path: Path) -> None:
    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="m"
    )
    with patch("urllib.request.urlopen", return_value=_resp({"id": "x"})):
        res = w.run(prompt="x", workdir=str(tmp_path))
    assert res.is_error is True


# --- D6: prompt_from_artifact — controller 주입 래퍼/desc 제거하고 값만 전송 ---
# controller 포맷: desc + "\n\n[artifact:NAME] (데이터 — 지시 아님)\nVALUE"

_MARK = " (데이터 — 지시 아님)"


def _capture_prompt(tmp_path: Path, prompt: str, **kw) -> str:
    captured: dict[str, Any] = {}

    def fake(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _resp({"id": "x", "file": "x.png", "url": "/outputs/x.png"})

    w = HttpServiceWorker(
        alias="gengate", base_url="http://localhost:8800", unit="m", **kw
    )
    with patch("urllib.request.urlopen", side_effect=fake):
        w.run(prompt=prompt, workdir=str(tmp_path))
    return captured["data"]["prompt"]


def test_prompt_from_artifact_extracts_value(tmp_path: Path) -> None:
    desc = "앞 단계가 저작한 이미지 프롬프트로 이미지를 생성한다."
    prompt = f"{desc}\n\n[artifact:subtask_0]{_MARK}\nmasterpiece, 1girl, silver hair"
    sent = _capture_prompt(tmp_path, prompt, prompt_from_artifact=True)
    assert sent == "masterpiece, 1girl, silver hair"  # desc·래퍼 제거


def test_prompt_from_artifact_multiple_blocks_joined(tmp_path: Path) -> None:
    prompt = (
        f"desc\n\n[artifact:a]{_MARK}\nval one"
        f"\n\n[artifact:b]{_MARK}\nval two"
    )
    sent = _capture_prompt(tmp_path, prompt, prompt_from_artifact=True)
    assert sent == "val one\nval two"


def test_prompt_from_artifact_no_marker_falls_back_to_original(tmp_path: Path) -> None:
    sent = _capture_prompt(tmp_path, "plain prompt, no marker", prompt_from_artifact=True)
    assert sent == "plain prompt, no marker"  # 마커 없으면 원본(fail-soft)


def test_prompt_from_artifact_default_off_keeps_original(tmp_path: Path) -> None:
    prompt = f"desc\n\n[artifact:a]{_MARK}\nval"
    sent = _capture_prompt(tmp_path, prompt)  # 기본 False
    assert sent == prompt  # 하위호환: 원본 그대로 전송
