"""TTS 비교 플러그인 — 백엔드 라우트 (첫 사례, 단계4).

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §6)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (첫 사례 TTS).

플러그인 인터페이스를 끝까지 밟는 첫 사례: make_routes(ports) 빌더 + 음성 카드
그리드 패널(panel.js) + manifest(plugin.json). 단계1 PoC 실증(ref voice
파라미터화 PASS, 702MB/176모델) — 다중 음성(1모델 + N voice) 중심.

seam: synth/voices 주입으로 hermetic 테스트(실 F5 로드 0). 실 배선은 default
synth(F5-TTS-ko lazy) + default voices(~/.cache/hana_voice). 최소권한:
measurement:write 포트가 있으면 음성별 측정 기록(fail-soft).
"""
from __future__ import annotations

import base64
import io
import os
import time
import unicodedata
from dataclasses import dataclass

from starlette.responses import JSONResponse
from starlette.routing import Route

MEASUREMENT_KIND = "tts_compare"


@dataclass(frozen=True)
class VoiceSpec:
    key: str
    label: str
    ref_file: str
    ref_text: str


# 기본 음성 레지스트리 — ref voice 디렉터리는 env 로 override 가능(하드코딩 회피).
_VOICE_DIR = os.environ.get(
    "JARVIS_TTS_VOICE_DIR", os.path.expanduser("~/.cache/hana_voice")
)

_DEFAULT_VOICE_SPECS = (
    ("kss", "KSS", "kss_ref_24k.wav", "그녀의 사랑을 얻기 위해 애썼지만 헛수고였다."),
    ("hana", "Hana", "hana_ref.wav", "지하철에서 다리를 벌리고 앉지 마라."),
    ("hana_short", "Hana(short)", "hana_shorts.wav", "지하철에서 다리를 벌리고 앉지 마라."),
    ("hana_v2", "Hana v2", "hana_shorts_v2.wav", "지하철에서 다리를 벌리고 앉지 마라."),
)


def _default_voices() -> dict[str, VoiceSpec]:
    """ref_file 이 실재하는 음성만 노출(파일 부재 = 환경별 미설치 → 조용히 제외)."""
    out: dict[str, VoiceSpec] = {}
    for key, label, fname, text in _DEFAULT_VOICE_SPECS:
        path = os.path.join(_VOICE_DIR, fname)
        if os.path.isfile(path):
            out[key] = VoiceSpec(key=key, label=label, ref_file=path, ref_text=text)
    return out


# ── 실 합성 (F5-TTS-ko lazy, server.py 패치 답습 — 플러그인 자족) ──────
_f5_tts = None


def _to_jamo(s: str) -> str:
    return unicodedata.normalize("NFD", s)


def _ensure_model():
    global _f5_tts
    if _f5_tts is not None:
        return _f5_tts
    import torch  # type: ignore
    import soundfile as sf  # type: ignore
    import torchaudio  # type: ignore

    def _load(path, **kwargs):
        audio, sr = sf.read(path, dtype="float32")
        audio = audio[None, :] if audio.ndim == 1 else audio.T
        return torch.from_numpy(audio), sr

    torchaudio.load = _load
    from f5_tts.api import F5TTS  # type: ignore

    ckpt = os.environ.get("JARVIS_F5_CKPT", os.path.expanduser("~/.cache/f5_ko/model_wrapped.pt"))
    vocab = os.environ.get("JARVIS_F5_VOCAB", os.path.expanduser("~/.cache/f5_ko/vocab.txt"))
    _f5_tts = F5TTS(ckpt_file=ckpt, vocab_file=vocab)
    return _f5_tts


def _default_synth(text: str, voice: VoiceSpec) -> dict:
    """실 F5-TTS-ko 합성 — ref voice 파라미터화(단계1 PoC). 메트릭 동봉."""
    import numpy as np  # type: ignore
    import soundfile as sf  # type: ignore

    model = _ensure_model()
    t0 = time.time()
    wav, sr, _ = model.infer(
        ref_file=voice.ref_file,
        ref_text=_to_jamo(voice.ref_text),
        gen_text=_to_jamo(text),
    )
    ms = int((time.time() - t0) * 1000)
    buf = io.BytesIO()
    sf.write(buf, wav, sr, format="WAV")
    arr = np.asarray(wav, dtype="float32")
    rms = float(np.sqrt(np.mean(arr ** 2))) if arr.size else 0.0
    return {"audio": buf.getvalue(), "sample_rate": int(sr),
            "samples": int(arr.size), "rms": rms, "ms": ms}


def make_routes(ports: dict, *, synth=None, voices=None) -> list:
    """TTS 비교 플러그인 라우트. ports = select_ports 결과(최소권한)."""
    synth_fn = synth or _default_synth
    voice_map = voices if voices is not None else _default_voices()
    writer = ports.get("measurement:write")

    async def list_voices(request):
        return JSONResponse({
            "voices": [{"key": v.key, "label": v.label} for v in voice_map.values()]
        })

    async def synthesize(request):
        import asyncio

        try:
            data = await request.json()
        except Exception:
            data = {}
        text = (data.get("text") or "").strip() if isinstance(data, dict) else ""
        sel = data.get("voices") if isinstance(data, dict) else None
        if not text:
            return JSONResponse({"error": "text required"}, status_code=400)
        if not isinstance(sel, list) or not sel:
            return JSONResponse({"error": "voices required"}, status_code=400)
        unknown = [k for k in sel if k not in voice_map]
        if unknown:
            return JSONResponse({"error": f"unknown voice: {unknown}"}, status_code=400)

        results = []
        for key in sel:
            voice = voice_map[key]
            out = await asyncio.to_thread(synth_fn, text, voice)  # 합성 비차단
            results.append({
                "voice": key,
                "label": voice.label,
                "audio_b64": base64.b64encode(out["audio"]).decode("ascii"),
                "sample_rate": out["sample_rate"],
                "samples": out["samples"],
                "rms": out["rms"],
                "ms": out["ms"],
            })
            if writer is not None:
                try:  # fail-soft: 측정 기록 실패가 합성을 깨지 않음
                    writer({"voice": key, "text_len": len(text), "ms": out["ms"],
                            "rms": out["rms"], "samples": out["samples"]},
                           kind=MEASUREMENT_KIND)
                except Exception:
                    pass
        return JSONResponse({"results": results})

    return [
        Route("/api/plugins/tts_compare/voices", list_voices, methods=["GET"]),
        Route("/api/plugins/tts_compare/synthesize", synthesize, methods=["POST"]),
    ]
