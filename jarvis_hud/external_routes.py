"""외부 관제형 읽기측 HTTP 라우트 — 패턴1 링크 허브 MVP (`/api/jarvis/external`).

답습: docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md (v2.1 §4 패턴1)
  docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md (REVISE 읽기측).

external_registry(순수 로직)를 HTTP GET 으로 노출하는 얇은 레이어:
  - **읽기 전용**: GET 만. write/제어/자격증명 0 — 제어측(§3.5)은 별도 풀3+1 + DEFER.
    same-origin 가드도 불필요(읽기 전용·민감정보 0, plugins_list GET 답습).
  - provenance(origin)는 **내부 게이트** — 응답에 노출하지 않는다(이름·URL·아이콘만).
    레지스트리가 origin != jarvis 를 이미 걸러냈으므로 노출분은 전부 자비스-origin.
  - registry_file 주입 = hermetic test seam(server 가 실 경로 배선).
"""
from __future__ import annotations

from starlette.responses import JSONResponse
from starlette.routing import Route

from src.jarvis.external_registry import discover_external


def make_external_routes(*, registry_file: str) -> list:
    """외부 관제형 읽기측 routes. registry_file 주입 = hermetic test seam."""

    async def external_list(request):
        out = [
            {"name": e.name, "title": e.title, "url": e.url, "icon": e.icon}
            for e in discover_external(registry_file)
        ]
        return JSONResponse({"external": out})

    return [
        Route("/api/jarvis/external", external_list, methods=["GET"]),
    ]
