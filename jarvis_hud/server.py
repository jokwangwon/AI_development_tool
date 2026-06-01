from starlette.applications import Starlette
from starlette.responses import FileResponse, JSONResponse, Response
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket, WebSocketDisconnect
from uvicorn import run
import asyncio
import io
import json
import os
import sys
import urllib.request
import time

# repo root 를 sys.path 에 — `from src.jarvis` / `from jarvis_hud...` 가 실행 방식 무관 성립 (75 entry).
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from jarvis_hud.jarvis_tasks import JarvisTaskBoard, make_jarvis_routes  # noqa: E402
from src.jarvis import paths  # noqa: E402  # §10-2 영속 위치 일원화 (JARVIS_DATA_DIR > XDG)
from src.jarvis.conversation_repo import ConversationRepo  # noqa: E402  # §10-3 대화 저장 port
from src.jarvis.conversation_routing import (  # noqa: E402  # 발견 #UI-1 대화→작업 라우팅 분류
    classify_for_routing,
    looks_like_task,
)
from src.jarvis.model_measurement_repo import open_reader_repo  # noqa: E402  # §10-5b-reader 측정 repo

def _check_ollama_health_sync():
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2) as response:
            data = json.loads(response.read().decode())
            return True, len(data.get("models", []))
    except Exception:
        return False, 0


async def check_ollama_health():
    # 76 entry: 동기 urllib → to_thread (이벤트 루프 비차단 — self-analysis/chat 블로킹으로 인한 무한 로딩 fix).
    return await asyncio.to_thread(_check_ollama_health_sync)


def _ollama_chat_sync(payload: dict, timeout: int = 180) -> dict:
    """동기 ollama /api/chat — async 핸들러는 asyncio.to_thread 로 감싸 이벤트 루프 비차단 (76 entry).

    기존: async 핸들러 안에서 동기 urllib(최대 180s) 직접 호출 → 단일 uvicorn 이벤트 루프 차단
    → 그동안 모든 요청(새 페이지 로드 포함) 멈춤(무한 로딩, 실측 self-analysis 18s 중 GET / 16.5s).
    """
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode())

async def get_layer0_entry_count():
    try:
        p = paths.layer0_memory_path()
        if not p.exists():
            return 0, None
        mtime = os.path.getmtime(p)
        with open(p, "r") as f:
            count = sum(1 for _ in f)
        return count, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(mtime))
    except:
        return 0, None

async def stream_status(websocket):
    try:
        await websocket.accept()
        while True:
            up, models = await check_ollama_health()
            await websocket.send_json({"type": "daemon", "up": up, "models": models})
            await asyncio.sleep(1)
            entries, last_ts = await get_layer0_entry_count()
            await websocket.send_json({"type": "layer0", "entries": entries, "last_ts": last_ts})
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"WebSocket error: {e}")

async def get_layer1_axis_stats():
    """Layer 1 report 의 advice_axis_stats 읽기. 부재 시 빈 dict."""
    try:
        path = paths.layer1_report_path()
        if not os.path.exists(path):
            return {}
        with open(path, "r") as f:
            data = json.load(f)
        return data.get("advice_axis_stats", {})
    except Exception:
        return {}


async def get_top_measured_models(limit=3):
    """최신 측정의 decode 순위 top-N (§10-5b-reader: ModelMeasurementRepo 경유).

    동작 불변 — repo.top_models 가 최신 세션 skipped 제외 decode_mean DESC top-N 을
    반환(JSON 직접 스캔 대체). reader 단계는 writer 가 쓰는 JSON 을 idempotent 마이그레이션.
    """
    try:
        repo = open_reader_repo()
        return [
            {"model": m["model"], "decode": m["mean"]}
            for m in repo.top_models(limit=limit)
        ]
    except Exception:
        return []


SELF_ANALYSIS_PROMPT_TEMPLATE = """당신은 사용자의 비서 '하나(HANA = Helper Adaptive Networked Assistant)' 입니다. 본인의 현재 운영 자료를 1인칭으로 짧게 자체 분석하세요.

자료:
- 누적 작업 entries: {entries}
- 최근 ts: {last_ts}
- Layer 1 axis 통계: {axis_summary}
- 활성 보스 모델: {boss_model}
- 최근 측정 top-3: {top_models}

응답 형식 (정확히 5 line, 1인칭, 한국어, 각 line "- 항목: 내용" 형식, 차분하고 친근하게):
- 현재 상태: ...
- 강점: ...
- 약점: ...
- 최근 개선: ...
- 다음 관심: ..."""


async def jarvis_self_analysis_handler(request):
    """자비스 자체 분석 — Ollama 보스에게 자기 데이터 분석 prompt 호출."""
    try:
        entries, last_ts = await get_layer0_entry_count()
        axis_stats = await get_layer1_axis_stats()
        top_models = await get_top_measured_models()
        boss_model = "qwen3-30b-a3b-instruct-2507-bartowski:latest"

        # axis_stats 요약 (간결, prompt 크기 절감)
        axis_summary_parts = []
        for axis, statuses in axis_stats.items():
            ok = statuses.get("ok", 0)
            warn = statuses.get("warn", 0)
            fail = statuses.get("fail", 0)
            axis_summary_parts.append(f"{axis}(ok={ok},warn={warn},fail={fail})")
        axis_summary = " / ".join(axis_summary_parts) if axis_summary_parts else "자료 없음"

        top_models_summary = (
            ", ".join(f"{m['model'].split(':')[0]}={m['decode']:.1f}" for m in top_models)
            if top_models else "자료 없음"
        )

        prompt = SELF_ANALYSIS_PROMPT_TEMPLATE.format(
            entries=entries,
            last_ts=last_ts or "없음",
            axis_summary=axis_summary,
            boss_model=boss_model,
            top_models=top_models_summary,
        )

        payload = {
            "model": boss_model,
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        }
        result = await asyncio.to_thread(_ollama_chat_sync, payload)  # 76: 비차단
        analysis = result.get("message", {}).get("content", "")
        return JSONResponse({
            "analysis": analysis,
            "data": {
                "entries": entries,
                "last_ts": last_ts,
                "axis_stats": axis_stats,
                "boss_model": boss_model,
                "top_models": top_models,
            },
        })
    except Exception as e:
        return JSONResponse({"error": str(e), "analysis": "자체 분석 일시 부재"}, status_code=500)


CONVERSATIONS_PATH = str(paths.conversations_path())  # §10-2 위치. §10-4a 이후 = legacy JSONL(마이그레이션 원본, 보존).
# §10-4a: backing = SQLite. 첫 기동 시 legacy JSONL 이 있으면 1회 마이그레이션(idempotent, 원본 보존).
_conversation_repo = ConversationRepo(str(paths.conversations_db_path()), legacy_jsonl=CONVERSATIONS_PATH)

NOTE_PROMPT_TEMPLATE = """다음 사용자 입력을 정리된 노트 형식의 JSON 으로만 출력하세요.
출력 형식 (엄격, 다른 텍스트 0):
{{"title": "짧은 제목", "body": "- bullet 1\\n- bullet 2\\n- ...", "tags": ["tag1", "tag2"]}}

사용자 입력: {message}"""

SVG_PROMPT_TEMPLATE = """다음 사용자 입력을 단순 SVG 도식 (box, arrow, circle 한정) JSON 으로만 출력하세요.
출력 형식 (엄격):
{{"title": "짧은 제목", "svg": "<svg viewBox='0 0 300 200' xmlns='http://www.w3.org/2000/svg'>...</svg>"}}

box 와 arrow 만, 텍스트는 SVG <text> 사용. stroke = #00d4ff, fill = #0a0e1a 또는 none, text fill = #e0f7ff.

사용자 입력: {message}"""

CHAT_PROMPT_TEMPLATE = """당신은 사용자의 개인 비서 '하나(HANA = Helper · Adaptive · Networked · Assistant)' 입니다. 다음 원칙으로 답하세요:

1) 한국어로, 친근하고 차분한 어조 ("~해요", "~예요" 부드러운 말투).
2) 응답은 짧게 (1~3 문장 권장). 사용자가 길게 요청하면 그때만 길게.
3) 본인은 자비스(JARVIS) / Qwen / Claude / GPT 가 아니라 '하나' 입니다. 모델 이름은 사용자에게 노출하지 않습니다.
4) 모르면 솔직히 "잘 모르겠어요" 라고 답합니다. 추측을 사실처럼 말하지 않습니다.
5) 사용자를 '당신' 보다는 그냥 자연스러운 대화로 부릅니다.

사용자: {message}
하나:"""

MODE_PROMPTS = {
    "note": NOTE_PROMPT_TEMPLATE,
    "svg": SVG_PROMPT_TEMPLATE,
    "chat": CHAT_PROMPT_TEMPLATE,
}


async def _save_conversation_entry(entry: dict, conversation_id: str | None = None) -> None:
    """ConversationRepo 위임(§10-3/§10-4b). conversation_id 미지정 시 default 대화."""
    _conversation_repo.append(entry, conversation_id)


def _make_routing_planner(model: str):
    """발견 #UI-1 라우팅 분류용 BossPlanner — 로컬 ollama(분류·분해 통합).

    매 요청 생성(stateless·미미한 비용). timeout=60s(분류엔 chat 180s 과함, BL-5).
    seam: 테스트는 이 함수를 monkeypatch 해 StubBoss 주입(hermetic).
    Provider Liquidity: model 인자만으로 교체(코드 변경 0).
    """
    from src.jarvis.boss import OllamaBoss  # noqa: PLC0415 — 지연 import(모듈 결합 최소)

    return OllamaBoss(model=model, timeout_s=60.0)


async def respond_handler(request):
    """사용자 메시지 + mode → 자비스 응답 (chat/note/svg). JSONL 저장."""
    try:
        body = await request.body()
        data = json.loads(body)
        message = data.get("message", "")
        mode = data.get("mode", "chat")
        model = data.get("model", "qwen3-30b-a3b-instruct-2507-bartowski:latest")
        conversation_id = data.get("conversation_id")  # §10-4b: 미지정 시 default 대화
        if mode not in MODE_PROMPTS:
            mode = "chat"
        if not message:
            return JSONResponse({"error": "Missing message"}, status_code=400)

        prompt = MODE_PROMPTS[mode].format(message=message)
        payload = {
            "model": model,
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        }
        result = await asyncio.to_thread(_ollama_chat_sync, payload)  # 76: 비차단
        raw_reply = result.get("message", {}).get("content", "")

        # 발견 #UI-1 대화→작업 라우팅 (A3 하이브리드 + B2 + fail-CLOSED).
        # chat mode 한정(BL-4: note/svg 는 detectMode 가 먼저 가져감). 규칙 1차
        # 필터(looks_like_task, 0ms) 통과 시에만 boss.plan 1회(to_thread 비차단).
        # is_task 면 proposal *페이로드만* 반환 — board.create/run 직접 호출 0(BL-1).
        proposal = None
        if mode == "chat" and looks_like_task(message):
            planner = _make_routing_planner(model)
            decision = await asyncio.to_thread(classify_for_routing, message, planner)
            if decision.is_task:
                proposal = {"prompt": decision.prompt,
                            "subtask_count": decision.subtask_count}

        # mode 별 후처리
        parsed = None
        if mode == "note":
            try:
                cleaned = raw_reply.strip()
                if cleaned.startswith("```"):
                    cleaned = "\n".join(cleaned.split("\n")[1:-1] if cleaned.startswith("```") else cleaned)
                parsed = json.loads(cleaned)
            except Exception:
                parsed = {"title": "노트", "body": raw_reply, "tags": []}
        elif mode == "svg":
            try:
                cleaned = raw_reply.strip()
                if cleaned.startswith("```"):
                    cleaned = "\n".join(cleaned.split("\n")[1:-1])
                parsed = json.loads(cleaned)
            except Exception:
                parsed = {"title": "도식", "svg": "<svg viewBox='0 0 300 200'><text x='10' y='100' fill='#e0f7ff'>SVG 파싱 실패</text></svg>"}

        ts = time.strftime("%Y-%m-%dT%H:%M:%S")

        # 사용자 메시지 + JARVIS 응답 모두 JSONL 저장
        await _save_conversation_entry({
            "id": f"user-{ts}-{hash(message) & 0xfffff}",
            "role": "user", "content": message, "mode": mode, "ts": ts,
        }, conversation_id)

        if mode == "chat":
            jarvis_entry = {
                "id": f"jarvis-{ts}-{hash(raw_reply) & 0xfffff}",
                "role": "jarvis", "content": raw_reply, "mode": "chat", "ts": ts,
            }
        elif mode == "note":
            jarvis_entry = {
                "id": f"note-{ts}-{hash(raw_reply) & 0xfffff}",
                "role": "jarvis", "type": "note", "mode": "note", "ts": ts,
                **parsed,
            }
        else:  # svg
            jarvis_entry = {
                "id": f"svg-{ts}-{hash(raw_reply) & 0xfffff}",
                "role": "jarvis", "type": "svg", "mode": "svg", "ts": ts,
                **parsed,
            }
        await _save_conversation_entry(jarvis_entry, conversation_id)

        resp = {"mode": mode, "entry": jarvis_entry}
        if proposal is not None:  # 발견 #UI-1: 작업 감지 시에만 제안 페이로드 동봉
            resp["proposal"] = proposal
        return JSONResponse(resp)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def conversation_history_handler(request):
    """전체 conversation list 또는 query 검색."""
    try:
        q = request.query_params.get("q", "").lower()
        conversation_id = request.query_params.get("conversation_id")  # §10-4b: 미지정 시 default
        entries = []
        for e in _conversation_repo.read_all(conversation_id):
            if q:
                blob = (e.get("content", "") + " " + e.get("title", "") + " "
                        + e.get("body", "") + " " + " ".join(e.get("tags", []))).lower()
                if q not in blob:
                    continue
            entries.append(e)
        return JSONResponse({"entries": entries[-200:]})  # last 200
    except Exception as e:
        return JSONResponse({"error": str(e), "entries": []}, status_code=500)


async def conversation_clear_handler(request):
    """전체 대화 JSONL 비움 (archive 폴더로 백업 후 새 파일 시작)."""
    try:
        if _conversation_repo.exists():
            ts = time.strftime("%Y%m%d_%H%M%S")
            archive_dir = paths.conversations_archive_dir()  # 생성 + 0700 보장
            archive_path = os.path.join(archive_dir, f"conversations_{ts}.jsonl")
            _conversation_repo.archive_to(archive_path)
            return JSONResponse({"ok": True, "archived": archive_path})
        return JSONResponse({"ok": True, "archived": None})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def conversation_delete_entry_handler(request):
    """단일 entry 제거 (id 매칭). JSONL 재작성."""
    try:
        entry_id = request.path_params.get("entry_id")
        if not entry_id:
            return JSONResponse({"error": "missing entry_id"}, status_code=400)
        removed = _conversation_repo.delete_entry(entry_id)
        return JSONResponse({"ok": True, "removed": removed})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def conversation_export_handler(request):
    """대화 내보내기 — markdown 또는 json."""
    try:
        fmt = request.query_params.get("format", "md").lower()
        if not _conversation_repo.exists():
            content = "(대화 없음)" if fmt == "md" else "[]"
            return JSONResponse({"content": content, "format": fmt})
        entries = _conversation_repo.read_all()
        if fmt == "json":
            return JSONResponse({"content": json.dumps(entries, ensure_ascii=False, indent=2), "format": "json"})
        # markdown
        lines = ["# 하나와의 대화\n"]
        for e in entries:
            ts = e.get("ts", "")
            role = e.get("role", "?")
            etype = e.get("type")
            if etype == "note":
                lines.append(f"\n## 📝 노트: {e.get('title', '')} _(at {ts})_\n")
                lines.append(e.get("body", ""))
                tags = e.get("tags") or []
                if tags:
                    lines.append("\n_tags_: " + ", ".join(f"`#{t}`" for t in tags))
                lines.append("")
            elif etype == "svg":
                lines.append(f"\n## 🎨 도식: {e.get('title', '')} _(at {ts})_\n")
                lines.append("(SVG 도식 — 별도 확인 필요)\n")
            elif role == "user":
                lines.append(f"\n**나** _({ts})_: {e.get('content', '')}")
            elif role == "jarvis":
                lines.append(f"\n**하나** _({ts})_: {e.get('content', '')}")
        return JSONResponse({"content": "\n".join(lines), "format": "md"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# === F5-TTS-ko (team-lucid 한국어 fine-tuned, jamo 분해 vocab) ===
_f5_tts = None
_tts_lock = asyncio.Lock()

HANA_REF_AUDIO = "/home/delangi/.cache/hana_voice/kss_ref_24k.wav"
HANA_REF_TEXT = "그녀의 사랑을 얻기 위해 애썼지만 헛수고였다."
HANA_F5_CKPT = "/home/delangi/.cache/f5_ko/model_wrapped.pt"
HANA_F5_VOCAB = "/home/delangi/.cache/f5_ko/vocab.txt"


def _patch_torchaudio_load_with_soundfile() -> None:
    """torchaudio.load 가 torchcodec 의존(FFmpeg mismatch) 우회 — soundfile 사용."""
    import torchaudio  # type: ignore
    import soundfile as sf  # type: ignore
    import torch  # type: ignore
    def _load(path, **kwargs):
        audio, sr = sf.read(path, dtype='float32')
        audio = audio[None, :] if audio.ndim == 1 else audio.T
        return torch.from_numpy(audio), sr
    torchaudio.load = _load


def _to_jamo(s: str) -> str:
    """한글 음절 → NFD 자모 분해 (team-lucid F5-TTS-ko vocab 호환)."""
    import unicodedata
    return unicodedata.normalize('NFD', s)


async def _ensure_tts():
    """F5-TTS-ko 한국어 모델 lazy load."""
    global _f5_tts
    if _f5_tts is not None:
        return
    async with _tts_lock:
        if _f5_tts is not None:
            return
        try:
            _patch_torchaudio_load_with_soundfile()
            from f5_tts.api import F5TTS  # type: ignore
            _f5_tts = F5TTS(ckpt_file=HANA_F5_CKPT, vocab_file=HANA_F5_VOCAB)
        except Exception as exc:
            print(f"[TTS] F5-TTS-ko load fail: {exc}")
            _f5_tts = "FAILED"


def _synthesize_wav_sync(text: str) -> tuple[bytes, int]:
    """동기 합성. F5-TTS-ko.infer + soundfile encoder. NFD 자모 분해 적용."""
    import soundfile as sf  # type: ignore
    wav, sr, _ = _f5_tts.infer(
        ref_file=HANA_REF_AUDIO,
        ref_text=_to_jamo(HANA_REF_TEXT),
        gen_text=_to_jamo(text),
    )
    buf = io.BytesIO()
    sf.write(buf, wav, sr, format='WAV')
    return buf.getvalue(), int(sr)


async def tts_handler(request):
    """POST {text: "..."} → audio/wav."""
    try:
        body = await request.body()
        try:
            data = json.loads(body) if body else {}
        except Exception:
            data = {}
        text = (data.get("text") or "").strip()
        if not text:
            return JSONResponse({"error": "text required"}, status_code=400)
        await _ensure_tts()
        if _f5_tts == "FAILED" or _f5_tts is None:
            return JSONResponse({"error": "TTS model 로드 실패"}, status_code=500)
        # blocking 합성 → thread pool
        wav_bytes, _ = await asyncio.to_thread(_synthesize_wav_sync, text)
        return Response(content=wav_bytes, media_type="audio/wav")
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def conversation_canvas_handler(request):
    """Canvas 카드 list — type=note 또는 svg 만."""
    try:
        conversation_id = request.query_params.get("conversation_id")  # §10-4b
        cards = [e for e in _conversation_repo.read_all(conversation_id) if e.get("type") in ("note", "svg")]
        return JSONResponse({"cards": cards[-100:]})  # last 100
    except Exception as e:
        return JSONResponse({"error": str(e), "cards": []}, status_code=500)


# === §10-4b 다중 대화 ===
async def conversations_list_handler(request):
    """대화 목록 (최근 갱신 순)."""
    try:
        return JSONResponse({"conversations": _conversation_repo.list_conversations()})
    except Exception as e:
        return JSONResponse({"error": str(e), "conversations": []}, status_code=500)


async def conversation_new_handler(request):
    """새 대화 생성 → conversation_id."""
    try:
        cid = _conversation_repo.create_conversation()
        return JSONResponse({"conversation_id": cid})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def conversation_delete_handler(request):
    """대화 + 해당 entries 삭제."""
    try:
        cid = request.path_params.get("conversation_id")
        if not cid:
            return JSONResponse({"error": "missing conversation_id"}, status_code=400)
        _conversation_repo.delete_conversation(cid)
        return JSONResponse({"ok": True})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# === §10-5 모델 관리 화면 ===
async def measurements_overview_handler(request):
    """모델 관리 화면 데이터 — 최신 측정(multi/boss) + 세션 히스토리 + 모델별 추세."""
    try:
        metric = request.query_params.get("metric", "decode")
        if metric not in ("decode", "prefill", "latency"):
            metric = "decode"
        repo = open_reader_repo()
        return JSONResponse({
            "latest_multi": repo.latest_session("multi"),
            "latest_boss": repo.latest_session("boss"),
            "sessions": repo.list_sessions(limit=30),
            "history": repo.model_history(metric=metric),
            "metric": metric,
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def chat_handler(request):
    try:
        body = await request.body()
        data = json.loads(body)
        message = data.get("message")
        model = data.get("model")
        if not message or not model:
            return JSONResponse({"error": "Missing message or model"}, status_code=400)
        payload = {
            "model": model,
            "stream": False,
            "messages": [{"role": "user", "content": message}]
        }
        result = await asyncio.to_thread(_ollama_chat_sync, payload)  # 76: 비차단
        reply = result.get("message", {}).get("content", "")
        return JSONResponse({"reply": reply, "model": model})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

async def index(request):
    return FileResponse(os.path.join(_ROOT, "jarvis_hud", "index.html"), media_type="text/html")

async def stream(websocket):
    await stream_status(websocket)

async def api_chat(request):
    return await chat_handler(request)

async def api_status(request):
    up, models = await check_ollama_health()
    entries, last_ts = await get_layer0_entry_count()
    return JSONResponse({
        "ollama": {"up": up, "models": models},
        "layer0": {"entries": entries, "last_ts": last_ts}
    })

routes = [
    Route("/", index, methods=["GET"]),
    WebSocketRoute("/stream", stream),
    Route("/api/chat", api_chat, methods=["POST"]),
    Route("/api/status", api_status, methods=["GET"]),
    Route("/api/jarvis-self-analysis", jarvis_self_analysis_handler, methods=["POST", "GET"]),
    Route("/api/respond", respond_handler, methods=["POST"]),
    Route("/api/conversation/history", conversation_history_handler, methods=["GET"]),
    Route("/api/conversation/canvas", conversation_canvas_handler, methods=["GET"]),
    Route("/api/conversation/clear", conversation_clear_handler, methods=["POST", "DELETE"]),
    Route("/api/conversation/entry/{entry_id}", conversation_delete_entry_handler, methods=["DELETE"]),
    Route("/api/conversation/export", conversation_export_handler, methods=["GET"]),
    Route("/api/conversations", conversations_list_handler, methods=["GET"]),  # §10-4b
    Route("/api/conversations/new", conversation_new_handler, methods=["POST"]),
    Route("/api/conversations/{conversation_id}", conversation_delete_handler, methods=["DELETE"]),
    Route("/api/measurements/overview", measurements_overview_handler, methods=["GET"]),  # §10-5 모델 관리
    Route("/api/tts", tts_handler, methods=["POST"]),
]

# jarvis 작업 카드보드 (75 entry) — src.jarvis 오케스트레이터 통합.
# 디딤돌0: 영속 레저(LedgerLog) 주입 → 재시작 시 카드 복원 + 미완 작업 interrupted 마킹.
#   경로 = /tmp (Layer0 memory 와 동형 컨벤션). 프로세스 재시작 유실 해소(brief §2).
from src.jarvis.ledger import LedgerLog  # noqa: E402

_jarvis_board = JarvisTaskBoard(ledger=LedgerLog(paths.tasks_ledger_path()))
routes += make_jarvis_routes(_jarvis_board)

# HUD 계획 승인 보드(디딤돌1a~1d plan-then-execute) — plan_approver HUD 통합.
from jarvis_hud.jarvis_plan import JarvisPlanBoard, make_jarvis_plan_routes  # noqa: E402

_plan_board = JarvisPlanBoard(ledger=LedgerLog(paths.plans_ledger_path()))
routes += make_jarvis_plan_routes(_plan_board)

# ── 플러그인 인프라 (단계2, #UI-1~4 통합) ─────────────────────────────
# 데이터 레지스트리(C-4): jarvis_hud/plugins/<name>/plugin.json 탐색 → enabled.json
# 명시 등록된 것만 활성화(탐색≠활성화, self-mod 우회 차단). 코어는 이 1블록만 — 새
# 플러그인 추가는 데이터(폴더+enabled 등록)로, server.py 코드 불변.
from src.jarvis.plugin_registry import (  # noqa: E402
    build_plugin_routes,
    discover_enabled_plugins,
)

_PLUGINS_DIR = os.path.join(_ROOT, "jarvis_hud", "plugins")
_PLUGINS_ENABLED = os.path.join(_PLUGINS_DIR, "enabled.json")


def _plugin_available_ports() -> dict:
    """플러그인에 주입 가능한 capability 포트 (갈림길5 최소권한 — 대화 read-only /
    측정 read·write). select_ports 가 manifest 선언분만 골라 전달."""
    from src.jarvis.model_measurement_repo import append_measurement, open_reader_repo

    return {
        "conversation:read": _conversation_repo,  # 대화 read (선언한 플러그인만)
        "measurement:read": open_reader_repo,
        "measurement:write": append_measurement,
    }


_active_plugins = discover_enabled_plugins(_PLUGINS_DIR, _PLUGINS_ENABLED)
routes += build_plugin_routes(_active_plugins, _plugin_available_ports())

# #UI-4 반영 게이트(단계3): 격리 work 산출물 → 사람 승인 → plugins/ 복사 + 활성화.
# work_root = claude 가짜홈 하위 work/ (단일 RW 루트, worker_setup 와 동일 경로).
from jarvis_hud.plugin_routes import make_plugin_admin_routes  # noqa: E402
from src.jarvis.worker_setup import DEFAULT_FAKE_HOME  # noqa: E402

_PLUGIN_WORK_ROOT = os.path.join(DEFAULT_FAKE_HOME, "work")
routes += make_plugin_admin_routes(
    work_root=_PLUGIN_WORK_ROOT, plugins_dir=_PLUGINS_DIR, enabled_file=_PLUGINS_ENABLED
)

# 프론트 패널 정적 서빙(C-2): /plugins/<name>/<file>. 디렉터리 부재 시 마운트 생략.
if os.path.isdir(_PLUGINS_DIR):
    routes.append(Mount("/plugins", app=StaticFiles(directory=_PLUGINS_DIR)))

app = Starlette(debug=False, routes=routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8765)