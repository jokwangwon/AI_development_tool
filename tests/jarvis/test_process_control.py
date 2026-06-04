"""Jarvis 제어측 slice-1a — 프로세스 제어 controller 골격 + capability 등급 + 포트 LISTEN probe.

답습:
  docs/phase0/jarvis-control-side-general-executor-brief.md v2 §5 (slice-1a)
  docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1.md (REVISE, BLOCKING B-1~B-6)

slice-1a 범위(읽기성·자율, 가장 안전한 동작 먼저):
  - 포트 LISTEN probe = capability `probe`, 등급 = 저(자율). voice_lab `/health` 부재(실측) →
    포트 LISTEN 확인 + HTTP 선택적(주입형). (B-4)
  - ProcessController **propose-only seam**(B-1): boss 는 propose() 만, 집행은 등급 통과 시 내부에서.
  - capability → 등급 **코어 고정** 매핑(B-5): probe=저 / spawn·signal=중 / 미등재·unknown=고(fail-closed).
  - provenance 상속(B-2): 제어 대상 origin == jarvis 아니면 거부.
  - localhost 한정(B-4): 127.0.0.1/localhost 외 host 거부(SSRF 차단).
  - controller 자격증명 0(B-6).
lifecycle(start/stop/restart = 중위험·게이트)은 **slice-1b** — 본 슬라이스 범위 밖(미등록).
"""
from __future__ import annotations

import pytest

from src.jarvis.process_control import (
    CONTROL_ACTIONS,
    Action,
    Capability,
    ControlDecision,
    ControlError,
    ControlTarget,
    Grade,
    ProcessController,
    ProbeStatus,
    grade_for,
    parse_target,
    probe_target,
)


def _target_data(name="voice_lab", host="127.0.0.1", port=8777, origin="jarvis", health_path=""):
    return {"name": name, "host": host, "port": port, "origin": origin, "health_path": health_path}


def _good_target():
    return parse_target(_target_data())


# ── capability → 등급 코어 고정 매핑 (B-5, X-3) ────────────────────────────
def test_grade_probe_is_low():
    assert grade_for(frozenset({Capability.PROBE})) is Grade.LOW


def test_grade_spawn_and_signal_are_medium():
    assert grade_for(frozenset({Capability.SPAWN})) is Grade.MEDIUM
    assert grade_for(frozenset({Capability.SIGNAL})) is Grade.MEDIUM
    assert grade_for(frozenset({Capability.SPAWN, Capability.SIGNAL})) is Grade.MEDIUM


def test_grade_empty_is_high_fail_closed():
    """capability 없음 = 미상 = 보수적 고위험(fail-closed)."""
    assert grade_for(frozenset()) is Grade.HIGH


def test_grade_unknown_capability_is_high_fail_closed():
    assert grade_for(frozenset({"deploy_to_prod"})) is Grade.HIGH
    assert grade_for(frozenset({Capability.PROBE, "spend_money"})) is Grade.HIGH


def test_grade_mixed_read_write_takes_max():
    """읽기+쓰기 혼합 = 더 높은 등급(max). probe+spawn → 중."""
    assert grade_for(frozenset({Capability.PROBE, Capability.SPAWN})) is Grade.MEDIUM


def test_grade_for_is_pure_independent_of_target():
    """Provider Liquidity(CO-5): 등급은 capability에만 의존 — 대상·boss·모델 무관."""
    caps = frozenset({Capability.PROBE})
    assert grade_for(caps) is grade_for(caps)


# ── CONTROL_ACTIONS 코어 고정 allowlist (1a 범위) ─────────────────────────
def test_health_action_registered_as_probe():
    assert "health" in CONTROL_ACTIONS
    assert CONTROL_ACTIONS["health"].capabilities == frozenset({Capability.PROBE})


def test_lifecycle_actions_not_in_slice_1a():
    """start/stop/restart(중위험·게이트)은 slice-1b — 1a 코어 allowlist에 없어야(정직 범위)."""
    for name in ("start", "stop", "restart"):
        assert name not in CONTROL_ACTIONS


# ── parse_target: provenance(B-2) + localhost(B-4) + 안전성 ────────────────
def test_parse_target_valid():
    t = parse_target(_target_data())
    assert isinstance(t, ControlTarget)
    assert t.name == "voice_lab"
    assert t.host == "127.0.0.1"
    assert t.port == 8777
    assert t.origin == "jarvis"
    with pytest.raises(Exception):
        t.port = 1  # type: ignore  # frozen


def test_parse_target_rejects_non_jarvis_origin():
    """B-2 provenance 상속: origin != jarvis 거부(읽기측 external_registry와 동일 fail-closed)."""
    for bad in ("third_party", "external", "user", "", "JARVIS", "jarvis ", None):
        data = _target_data(origin=bad)
        with pytest.raises(ControlError):
            parse_target(data)


def test_parse_target_rejects_non_localhost_host():
    """B-4 SSRF 차단: localhost 외 host 거부."""
    for bad in ("evil.com", "0.0.0.0", "192.168.1.5", "10.0.0.1", "", "example.com"):
        data = _target_data(host=bad)
        with pytest.raises(ControlError):
            parse_target(data)


def test_parse_target_accepts_localhost_forms():
    for ok in ("127.0.0.1", "localhost"):
        assert parse_target(_target_data(host=ok)).host == ok


def test_parse_target_rejects_bad_port():
    for bad in (0, -1, 70000, "8777", None, 3.14):
        data = _target_data(port=bad)
        with pytest.raises(ControlError):
            parse_target(data)


def test_parse_target_rejects_unsafe_name():
    for bad in ("../etc", "a/b", "UPPER", "", "has space", ".."):
        with pytest.raises(ControlError):
            parse_target(_target_data(name=bad))


# ── probe_target: 포트 LISTEN + HTTP 선택적 (B-4) ─────────────────────────
def test_probe_listening_port():
    t = _good_target()
    status = probe_target(t, connector=lambda h, p, timeout: True)
    assert isinstance(status, ProbeStatus)
    assert status.listening is True


def test_probe_not_listening():
    t = _good_target()
    status = probe_target(t, connector=lambda h, p, timeout: False)
    assert status.listening is False


def test_probe_connector_error_is_not_listening():
    """연결 예외 = LISTEN 아님(fail 안전, crash 아님)."""
    def boom(h, p, timeout):
        raise OSError("refused")
    assert probe_target(_good_target(), connector=boom).listening is False


def test_probe_http_optional_only_when_health_path():
    t = parse_target(_target_data(health_path="/api/speakers"))
    status = probe_target(
        t,
        connector=lambda h, p, timeout: True,
        http_get=lambda url, timeout: True,
    )
    assert status.listening is True
    assert status.http_ok is True


def test_probe_no_health_path_skips_http():
    """health_path 없으면 HTTP probe 생략(http_ok=None) — voice_lab /health 부재 대응."""
    t = _good_target()
    called = []
    probe_target(t, connector=lambda h, p, timeout: True,
                 http_get=lambda url, timeout: called.append(url) or True)
    # health_path 빈값이므로 http_get 미호출
    assert called == []


# ── ProcessController.propose: B-1 seam + 등급 라우팅 ──────────────────────
def test_propose_health_low_auto_executes():
    calls = []
    ctrl = ProcessController(prober=lambda t: calls.append(t) or ProbeStatus(listening=True))
    decision = ctrl.propose("health", _good_target())
    assert isinstance(decision, ControlDecision)
    assert decision.grade is Grade.LOW
    assert decision.outcome == "executed"
    assert isinstance(decision.result, ProbeStatus)
    assert len(calls) == 1  # probe 1회 집행


def test_propose_rejects_non_jarvis_target():
    """B-2: provenance 위반 대상 = 거부, 집행 0."""
    calls = []
    ctrl = ProcessController(prober=lambda t: calls.append(t) or ProbeStatus(listening=True))
    # parse_target이 막으므로 ControlError로 직접 만든 비-jarvis 대상을 우회 주입 방어 확인
    bad = ControlTarget(name="x", host="127.0.0.1", port=8777, origin="evil", health_path="")
    decision = ctrl.propose("health", bad)
    assert decision.outcome == "rejected"
    assert calls == []  # 집행 안 됨


def test_propose_rejects_non_localhost_target():
    calls = []
    ctrl = ProcessController(prober=lambda t: calls.append(t) or ProbeStatus(listening=True))
    bad = ControlTarget(name="x", host="evil.com", port=80, origin="jarvis", health_path="")
    decision = ctrl.propose("health", bad)
    assert decision.outcome == "rejected"
    assert calls == []


def test_propose_unregistered_action_high_fail_closed():
    """B-5: 미등재 동작 = 고위험 fail-closed → 거부, 집행 0."""
    calls = []
    ctrl = ProcessController(prober=lambda t: calls.append(t) or ProbeStatus(listening=True))
    decision = ctrl.propose("delete_everything", _good_target())
    assert decision.grade is Grade.HIGH
    assert decision.outcome == "rejected"
    assert calls == []


def test_propose_non_low_action_never_auto_executes_b1_seam():
    """B-1 핵심: 비-저위험(중/고) 동작은 propose로도 자동 집행 0 (게이트는 slice-1b).

    SPAWN(중) capability 동작을 코어 allowlist에 주입해도 propose는 집행하지 않고 거부한다.
    boss가 propose만 호출 → 등급 게이팅을 우회해 _execute에 도달할 수 없음을 증명.
    """
    calls = []
    actions = {"rogue_spawn": Action("rogue_spawn", frozenset({Capability.SPAWN}))}
    ctrl = ProcessController(
        actions=actions,
        prober=lambda t: calls.append(t) or ProbeStatus(listening=True),
    )
    decision = ctrl.propose("rogue_spawn", _good_target())
    assert decision.grade is Grade.MEDIUM
    assert decision.outcome == "rejected"  # 1a엔 게이트/집행 경로 없음 → fail-closed
    assert calls == []  # 집행 절대 안 됨


def test_propose_audits_every_decision():
    """GP-7: 모든 dispatch 결정을 감사 sink에 기록(Rollback Trigger 검출)."""
    audit_log = []
    ctrl = ProcessController(
        prober=lambda t: ProbeStatus(listening=True),
        audit=audit_log.append,
    )
    ctrl.propose("health", _good_target())
    ctrl.propose("unknown", _good_target())
    assert len(audit_log) == 2
    assert all(isinstance(d, ControlDecision) for d in audit_log)


def test_decision_is_frozen():
    d = ControlDecision(action="health", target_name="voice_lab",
                        grade=Grade.LOW, outcome="executed", result=None, reason="")
    with pytest.raises(Exception):
        d.outcome = "x"  # type: ignore


# ── B-6: controller 자격증명 0 ─────────────────────────────────────────────
def test_controller_holds_no_credentials():
    """controller는 어떤 자격증명도 보유하지 않는다(slice-4 자격 미끄럼 방지 센서)."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    suspicious = ("secret", "token", "password", "credential", "apikey", "cookie")
    for attr in vars(ctrl):
        low = attr.lower()
        assert not any(s in low for s in suspicious), f"의심 속성: {attr}"


def test_controller_constructor_takes_no_credential_param():
    """생성자 시그니처에 자격증명 파라미터가 없어야(C-β: 자비스 본체 자격 보유 0)."""
    import inspect
    params = set(inspect.signature(ProcessController.__init__).parameters)
    suspicious = ("secret", "token", "password", "credential", "apikey")
    for p in params:
        assert not any(s in p.lower() for s in suspicious)
