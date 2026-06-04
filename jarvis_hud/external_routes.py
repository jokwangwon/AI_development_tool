"""외부 관제형 HTTP 라우트 — 읽기측 링크 허브(`/api/jarvis/external`) + 제어측 slice-1a probe.

답습:
  docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md (v2.1 §4 패턴1)
  docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md (REVISE 읽기측)
  docs/phase0/jarvis-control-side-general-executor-brief.md v2 §5 (제어측 slice-1a)
  docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1.md (REVISE, B-1~B-6)

external_registry(순수 로직)를 HTTP 로 노출하는 얇은 레이어:
  - `GET /api/jarvis/external` — 읽기 전용 링크 허브(이름·URL·아이콘). provenance(origin)는
    내부 게이트라 응답 비노출(레지스트리가 origin != jarvis 를 이미 거름).
  - `GET /api/jarvis/external/probe?name=X` — **제어측 slice-1a**: 카드 대상 상태 probe(health,
    저위험·자율). `ProcessController.propose()` 경유(B-1 seam). **localhost 카드만**(B-4 SSRF
    차단) — 외부 호스트는 probeable=false. provenance = registry 가 유일 출처(B-2).
  - registry_file/controller 주입 = hermetic test seam(server 가 실 경로·controller 배선).
"""
from __future__ import annotations

from urllib.parse import urlparse

from starlette.responses import JSONResponse
from starlette.routing import Route

from src.jarvis.external_registry import discover_external
from src.jarvis.process_control import ControlTarget, ProcessController, is_localhost


def make_external_routes(
    *, registry_file: str, controller: ProcessController | None = None
) -> list:
    """외부 관제형 routes. registry_file/controller 주입 = hermetic test seam."""
    ctrl = controller if controller is not None else ProcessController()

    async def external_list(request):
        out = [
            {"name": e.name, "title": e.title, "url": e.url, "icon": e.icon}
            for e in discover_external(registry_file)
        ]
        return JSONResponse({"external": out})

    async def external_probe(request):
        # provenance: registry 가 유일 출처(B-2) — 임의 대상 probe 불가.
        name = request.query_params.get("name", "")
        entries = {e.name: e for e in discover_external(registry_file)}
        entry = entries.get(name)
        if entry is None:
            return JSONResponse({"error": "not found"}, status_code=404)

        parsed = urlparse(entry.url)
        host = parsed.hostname or ""
        # B-4: localhost 카드만 제어 대상. 외부 호스트 = probe 미지원(점 없음).
        if not is_localhost(host):
            return JSONResponse({"name": name, "probeable": False})

        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        # origin = entry.origin(레지스트리가 jarvis 로 강제) → ControlTarget provenance 충족.
        target = ControlTarget(
            name=entry.name, host=host, port=port, origin=entry.origin, health_path=""
        )
        decision = ctrl.propose("health", target)  # B-1: propose-only seam 경유
        body = {
            "name": name,
            "probeable": True,
            "outcome": decision.outcome,
            "grade": decision.grade.name,
        }
        if decision.result is not None:
            body["listening"] = decision.result.listening
            body["http_ok"] = decision.result.http_ok
        return JSONResponse(body)

    return [
        Route("/api/jarvis/external", external_list, methods=["GET"]),
        Route("/api/jarvis/external/probe", external_probe, methods=["GET"]),
    ]
