"""자비스(하나) 읽어주기 합성 — 외부 voice_lab(Qwen3 디자인) 연계 (연계형).

내부 F5-TTS 를 제거하고, 읽어주기를 **외부 관제형 voice_lab** 의 음성 *생성*(Qwen3 디자인)
으로 연계한다. 음성 *비교* 랩(voice_lab)이 외부에 독립 존재하므로, 자비스는 그 생성 능력을
연계해 쓰고 내부에 합성 엔진을 중복 보유하지 않는다.

설계:
  - **고정 페르소나**: instruct + seed 고정 → 매 호출 일관된 '하나' 목소리(친근 여성 비서).
  - **Provider Liquidity**: voice_lab 위치(design_url)는 주입(호출측이 env 로 배선) — 하드코딩 0.
  - **hermetic seam**: http_json/fetch_bytes 주입 → 실 voice_lab 호출 없이 테스트.
  - voice_lab 다운/오류 = 예외 전파 → 호출측(핸들러)이 502, 프론트가 Web Speech 폴백(speakBrowser).

흐름: POST design_url {text, instruct, language, seed} → {url: ".../outputs/X.wav"} → wav fetch → bytes.
"""
from __future__ import annotations

import json as _json
import urllib.request
from typing import Callable

# 고정 '하나' 페르소나 — 친근 여성 비서(세션 실측 사람급 0.71σ). seed 고정 = 음색 재현.
HANA_INSTRUCT = "a warm, friendly female personal assistant speaking calmly and kindly"
HANA_SEED = 424242
HANA_LANGUAGE = "Korean"


class ReadAloudError(Exception):
    """읽어주기 합성 실패(응답 형식 등). 전송 오류(OSError 등)는 그대로 전파."""


def _default_http_json(url: str, payload: dict, timeout: float = 60) -> object:
    req = urllib.request.Request(
        url, data=_json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (localhost voice_lab)
        return _json.loads(resp.read().decode("utf-8"))


def _default_fetch_bytes(url: str, timeout: float = 30) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as resp:  # noqa: S310 (localhost voice_lab)
        return resp.read()


def synth_via_voicelab(
    text: str,
    *,
    design_url: str,
    http_json: Callable[..., object] = _default_http_json,
    fetch_bytes: Callable[..., bytes] = _default_fetch_bytes,
    instruct: str = HANA_INSTRUCT,
    seed: int = HANA_SEED,
    language: str = HANA_LANGUAGE,
) -> bytes:
    """text → voice_lab 디자인 합성 → wav bytes. 고정 페르소나로 일관된 '하나' 목소리.

    design_url = voice_lab Qwen3 디자인 엔드포인트(주입). 전송 오류는 전파(폴백 trigger).
    """
    payload = {"text": text, "instruct": instruct, "language": language, "seed": seed}
    data = http_json(design_url, payload)
    if not isinstance(data, dict) or not isinstance(data.get("url"), str):
        raise ReadAloudError("voice_lab design 응답에 url 없음")
    return fetch_bytes(data["url"])
