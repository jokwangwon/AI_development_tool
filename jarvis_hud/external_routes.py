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

import json as _json
from datetime import datetime, timezone
from urllib.parse import urlparse

from starlette.responses import JSONResponse
from starlette.routing import Route

from jarvis_hud.jarvis_tasks import same_origin  # CSRF 가드(기존 라우트 답습)
from src.jarvis.external_registry import discover_control_specs, discover_external
from src.jarvis.process_control import ControlTarget, ProcessController, is_localhost


def make_lifecycle_wiring(ledger):
    """LedgerLog → (cumulative_count, audit). CB-2 누적 파생 + CB-4 감사(intent fail-closed).

    - cumulative_count(name): ledger 의 executed lifecycle 이벤트 count = 누적 영속(CB-2).
      controller in-memory 가 아니라 append-only ledger 에서 파생 → controller 재시작 우회 차단.
    - audit(decision): intent = **fail-closed**(디스크 실패 시 예외 전파 → controller referred,
      CB-4 감사가 유일 센서). 결과(executed/referred/rejected) = fail-soft sink. cmdline 미기록
      (action/grade/pid/outcome 만 → NB-2 secret 누출 표면 0).
    """
    def cumulative_count(name: str) -> int:
        n = 0
        for ev in ledger.read():
            if (ev.get("event") == "lifecycle" and ev.get("target") == name
                    and ev.get("outcome") == "executed"):
                n += 1
        return n

    def audit(decision) -> None:
        task_id = f"{decision.target_name}:{decision.action}"
        if decision.outcome == "intent":
            # CB-4 fail-closed: silent 흡수 우회 — 직접 append(예외 전파)
            ledger.path.parent.mkdir(parents=True, exist_ok=True)
            entry = {
                "ts": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                "task_id": task_id, "event": "lifecycle_intent",
                "action": decision.action, "grade": decision.grade.name,
            }
            with open(ledger.path, "a", encoding="utf-8") as fh:
                fh.write(_json.dumps(entry, ensure_ascii=False) + "\n")
        else:
            ledger.record(task_id, "lifecycle", target=decision.target_name,
                          action=decision.action, outcome=decision.outcome,
                          grade=decision.grade.name, pid=decision.pid)

    return cumulative_count, audit

# slice-1b lifecycle 동작(코어 allowlist 와 일치). adopt = cutover 인수(HIGH).
_LIFECYCLE_ACTIONS = ("start", "stop", "restart", "adopt")


def _target_for(entry, spec) -> ControlTarget:
    """registry entry(읽기측) + ControlSpec(제어측 분리) → ControlTarget(L-10 결합)."""
    parsed = urlparse(entry.url)
    host = parsed.hostname or ""
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    return ControlTarget(
        name=entry.name, host=host, port=port, origin=entry.origin, health_path="",
        launch_argv=spec.launch_argv if spec is not None else (),
        cwd=spec.cwd if spec is not None else "",
    )


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

    async def external_lifecycle(request):
        """slice-1b lifecycle(start/stop/restart/adopt) — POST, propose() 경유(B-1 seam).

        1-클릭 게이트(C-2): `confirmed` 없으면 집행 0(프론트 모달 표시용 메타만 반환).
        confirmed=true(사람이 모달 승인) + same-origin(CSRF) 일 때만 propose. localhost 카드만.
        """
        if not same_origin(request):
            return JSONResponse({"error": "cross-origin forbidden"}, status_code=403)
        try:
            body = await request.json()
        except Exception:
            body = {}
        name = body.get("name", "")
        action = body.get("action", "")
        confirmed = bool(body.get("confirmed"))
        if action not in _LIFECYCLE_ACTIONS:
            return JSONResponse({"error": "unknown action"}, status_code=400)

        entry = {e.name: e for e in discover_external(registry_file)}.get(name)
        if entry is None:
            return JSONResponse({"error": "not found"}, status_code=404)
        if not is_localhost(urlparse(entry.url).hostname or ""):
            # B-4: 외부 호스트 = 제어 불가(lifecycle 은 로컬 프로세스만).
            return JSONResponse({"name": name, "controllable": False})

        spec = discover_control_specs(registry_file).get(name)
        target = _target_for(entry, spec)
        if not confirmed:
            # C-2 1-클릭 게이트: 미확인 = 집행 0. 프론트가 승인 모달을 띄운다.
            return JSONResponse({"name": name, "controllable": True,
                                 "needs_confirm": True, "action": action})

        decision = ctrl.propose(action, target)  # B-1: propose-only seam
        return JSONResponse({
            "name": name, "controllable": True, "action": action,
            "outcome": decision.outcome, "grade": decision.grade.name,
            "reason": decision.reason, "pid": decision.pid,
        })

    return [
        Route("/api/jarvis/external", external_list, methods=["GET"]),
        Route("/api/jarvis/external/probe", external_probe, methods=["GET"]),
        Route("/api/jarvis/external/lifecycle", external_lifecycle, methods=["POST"]),
    ]
