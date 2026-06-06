"""반영 게이트 HTTP 라우트 — slice-app-1 (#반영 루프, 갭1).

답습: docs/review/3plus1-consensus-2026-06-06-output-application-loop.md
  docs/phase0/jarvis-output-application-loop-brief.md (invariant I1~I7)

output_application 게이트(src.jarvis)를 HTTP 로 노출하는 얇은 레이어:
  - same-origin 가드(CSRF, 기존 jarvis 라우트 답습) — preview/commit (CB-6).
  - preview ≠ commit: preview 는 dry-run(do_apply=False)으로 적용 가능 여부 + diff(scrub)
    표시만, commit 은 confirmed=True 명시 시에만 실 apply (I1 자동반영 금지).
  - diff 텍스트는 RedactionFilter.scrub 후 노출 (CB-5).
  - work_root/registry_file/git_runner 주입(test seam) — server 가 실 경로 배선.

신뢰 경계: source = work_root 하위 단일 폴더명(traversal 차단). 대상 repo = registry
화이트리스트(CB-2). patch 의미검증·repo clean·apply --check fail-closed 는
output_application 게이트가 재검증(CB-1/CB-3/CB-4).
"""
from __future__ import annotations

import json

from starlette.responses import JSONResponse
from starlette.routing import Route

from jarvis_hud.jarvis_tasks import same_origin
from jarvis_hud.plugin_routes import _safe_source_component
from src.adapters.llm.redaction import RedactionFilter
from src.jarvis.external_registry import discover_apply_targets
from src.jarvis.output_application import (
    OutputApplicationError,
    apply_patch,
    extract_workdir_diff,
    resolve_target,
)
import os


def make_apply_routes(*, work_root: str, registry_file: str, git_runner=None) -> list:
    """반영 게이트 routes. 경로/runner 주입 = hermetic test seam."""
    redactor = RedactionFilter()
    _runner_kw = {"git_runner": git_runner} if git_runner is not None else {}

    async def _json(request):
        try:
            return json.loads(await request.body())
        except Exception:
            return None

    async def targets(request):
        names = sorted(discover_apply_targets(registry_file).keys())
        return JSONResponse({"targets": names})

    async def sources(request):
        """work_root 하위 산출물 폴더명 목록(숨김·파일 제외). 반영 source 후보."""
        try:
            entries = os.listdir(work_root)
        except OSError:
            return JSONResponse({"sources": []})
        out = sorted(
            e for e in entries
            if not e.startswith(".") and os.path.isdir(os.path.join(work_root, e))
        )
        return JSONResponse({"sources": out})

    def _run_gate(data, *, do_apply):
        """preview/commit 공통: source/target 검증 → diff 추출 → apply_patch.

        반환: (JSONResponse | None 에러, ApplyResult | None, scrubbed_diff). 에러면 첫 값만.
        """
        source = _safe_source_component(data.get("source") if isinstance(data, dict) else None)
        target = data.get("target") if isinstance(data, dict) else None
        if source is None:
            return JSONResponse({"error": "invalid source"}, status_code=400), None, ""
        if not isinstance(target, str) or not target:
            return JSONResponse({"error": "invalid target"}, status_code=400), None, ""
        whitelist = discover_apply_targets(registry_file)
        try:
            repo_real = resolve_target(target, whitelist)
        except OutputApplicationError as exc:
            return JSONResponse({"error": str(exc)}, status_code=400), None, ""
        src_path = os.path.join(work_root, source)
        patch, err = extract_workdir_diff(src_path, **_runner_kw)
        if err is not None:
            return JSONResponse({"error": err}, status_code=400), None, ""
        result = apply_patch(patch or "", repo_real, do_apply=do_apply, **_runner_kw)
        return None, result, redactor.scrub(patch or "")

    async def preview(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        data = await _json(request)
        err, result, diff = _run_gate(data, do_apply=False)
        if err is not None:
            return err
        return JSONResponse({
            "outcome": result.outcome,
            "reason": result.reason,
            "diff": diff,
            "violations": [
                {"kind": v.kind, "path": v.path, "detail": v.detail}
                for v in (result.validation.violations if result.validation else [])
            ],
        })

    async def commit(request):
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        data = await _json(request)
        if not (isinstance(data, dict) and data.get("confirmed") is True):
            return JSONResponse({"error": "confirmed=true required"}, status_code=400)
        err, result, _diff = _run_gate(data, do_apply=True)
        if err is not None:
            return err
        return JSONResponse({
            "outcome": result.outcome,
            "reason": result.reason,
            "applied": result.applied,
        })

    return [
        Route("/api/jarvis/apply/targets", targets, methods=["GET"]),
        Route("/api/jarvis/apply/sources", sources, methods=["GET"]),
        Route("/api/jarvis/apply/preview", preview, methods=["POST"]),
        Route("/api/jarvis/apply/commit", commit, methods=["POST"]),
    ]
