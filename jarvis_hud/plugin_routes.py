"""플러그인 관리 HTTP 라우트 — 단계3 #UI-4 install 엔드포인트 (120 세션).

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §5-3/§7)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (C-1·C-3·C-4).

B복사 게이트(src.jarvis.plugin_install)를 HTTP 로 노출하는 얇은 레이어:
  - same-origin 가드(CSRF, 기존 jarvis 라우트 답습) — install/enable/disable.
  - install ≠ enable (C-4 분리): 복사 후에도 사람이 enable 을 별도 호출해야 활성.
  - preview: 복사 *전* 사람 diff 검토용. 텍스트는 scrub(RedactionFilter) 후 노출.
  - work_root/plugins_dir/enabled_file 주입(test seam) — server 가 실 경로 배선.

신뢰 경계: source 는 work_root 하위 단일 폴더명만(traversal 차단). 실 복사 안전은
plugin_install 게이트가 재검증(소스 containment·symlink·secret·덮어쓰기).
"""
from __future__ import annotations

import json
import os

from starlette.responses import JSONResponse
from starlette.routing import Route

from jarvis_hud.jarvis_tasks import same_origin
from src.adapters.llm.redaction import RedactionFilter
from src.jarvis.plugin_install import (
    PluginInstallError,
    disable_plugin,
    enable_plugin,
    install_plugin_from_work,
)
from src.jarvis.plugin_registry import discover_plugins, load_enabled

# preview 텍스트 노출 한도(폭주·바이너리 방지)
_PREVIEW_MAX_BYTES = 64 * 1024
_TEXT_SUFFIXES = (".js", ".json", ".html", ".css", ".md", ".txt", ".py", ".svg")


def _safe_source_component(source: object) -> str | None:
    """source = work_root 하위 단일 폴더명만 허용 (traversal/절대경로 차단)."""
    if not isinstance(source, str) or not source:
        return None
    if source != os.path.basename(source) or source in (".", "..") or os.sep in source:
        return None
    if os.altsep and os.altsep in source:
        return None
    return source


def make_plugin_admin_routes(*, work_root: str, plugins_dir: str, enabled_file: str) -> list:
    """플러그인 관리 routes (#UI-4 반영 게이트). 경로 주입 = hermetic test seam."""
    redactor = RedactionFilter()

    async def _json(request):
        try:
            return json.loads(await request.body())
        except Exception:
            return None

    async def install(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        data = await _json(request)
        if not isinstance(data, dict):
            return JSONResponse({"error": "bad json"}, status_code=400)
        source = _safe_source_component(data.get("source"))
        name = data.get("name")
        if source is None:
            return JSONResponse({"error": "invalid source"}, status_code=400)
        src_path = os.path.join(work_root, source)
        try:
            manifest = install_plugin_from_work(
                src_path, name if isinstance(name, str) else "",
                work_root=work_root, plugins_dir=plugins_dir,
            )
        except PluginInstallError as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        return JSONResponse({"name": manifest.name, "title": manifest.title})

    async def enable(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        data = await _json(request)
        name = data.get("name") if isinstance(data, dict) else None
        try:
            enable_plugin(name if isinstance(name, str) else "", enabled_file=enabled_file)
        except PluginInstallError as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        return JSONResponse({"ok": True})

    async def disable(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        data = await _json(request)
        name = data.get("name") if isinstance(data, dict) else None
        try:
            disable_plugin(name if isinstance(name, str) else "", enabled_file=enabled_file)
        except PluginInstallError as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        return JSONResponse({"ok": True})

    async def plugins_list(request):
        enabled = load_enabled(enabled_file)
        out = [
            {"name": m.name, "title": m.title, "icon": m.icon,
             "enabled": m.name in enabled}
            for m in discover_plugins(plugins_dir)
        ]
        return JSONResponse({"plugins": out})

    async def preview(request):
        source = _safe_source_component(request.query_params.get("source"))
        if source is None:
            return JSONResponse({"error": "invalid source"}, status_code=400)
        src_real = os.path.realpath(os.path.join(work_root, source))
        work_real = os.path.realpath(work_root)
        if not (src_real == work_real or src_real.startswith(work_real + os.sep)) \
                or not os.path.isdir(src_real):
            return JSONResponse({"error": "source not found"}, status_code=400)
        files = []
        for root, _dirs, fnames in os.walk(src_real):
            for fn in sorted(fnames):
                p = os.path.join(root, fn)
                rel = os.path.relpath(p, src_real)
                is_link = os.path.islink(p)
                entry = {"path": rel, "symlink": is_link}
                # 텍스트만 scrub 후 노출. symlink/바이너리/대용량 = 내용 생략(플래그만).
                if (not is_link and fn.endswith(_TEXT_SUFFIXES)
                        and os.path.getsize(p) <= _PREVIEW_MAX_BYTES):
                    try:
                        with open(p, encoding="utf-8") as f:
                            entry["content"] = redactor.scrub(f.read())
                    except (OSError, UnicodeDecodeError):
                        entry["content"] = None
                files.append(entry)
        return JSONResponse({"source": source, "files": files})

    return [
        Route("/api/jarvis/plugin/install", install, methods=["POST"]),
        Route("/api/jarvis/plugin/enable", enable, methods=["POST"]),
        Route("/api/jarvis/plugin/disable", disable, methods=["POST"]),
        Route("/api/jarvis/plugins", plugins_list, methods=["GET"]),
        Route("/api/jarvis/plugin/preview", preview, methods=["GET"]),
    ]
