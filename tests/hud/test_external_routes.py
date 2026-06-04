"""외부 관제형 읽기측 HTTP 라우트 (`/api/jarvis/external` GET) — hermetic.

답습: docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md (v2.1 §4 패턴1)
  docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md (REVISE 읽기측).

설계: external_registry(순수 로직)를 HTTP GET 으로 노출하는 얇은 레이어. 읽기 전용 —
write/제어/자격증명 0(제어측 별도 풀3+1). registry_file 주입 = hermetic test seam.
provenance(origin) 는 내부 게이트라 응답에 비노출(이름·URL·아이콘만).
"""
from __future__ import annotations

import json

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.external_routes import make_external_routes, make_lifecycle_wiring
from src.jarvis.ledger import LedgerLog
from src.jarvis.process_control import (
    ControlDecision,
    Grade,
    ProbeStatus,
    ProcessController,
)


# ── CB-2 누적(ledger 파생) + CB-4 감사 배선 ───────────────────────────────
def test_cumulative_count_derives_from_ledger(tmp_path):
    led = LedgerLog(tmp_path / "led.jsonl")
    cum, audit = make_lifecycle_wiring(led)
    assert cum("voice_lab") == 0
    audit(ControlDecision("start", "voice_lab", Grade.MEDIUM, "executed", pid=1))
    audit(ControlDecision("restart", "voice_lab", Grade.MEDIUM, "executed", pid=2))
    audit(ControlDecision("start", "other", Grade.MEDIUM, "executed", pid=3))
    audit(ControlDecision("stop", "voice_lab", Grade.MEDIUM, "referred"))  # referred 는 미집계
    assert cum("voice_lab") == 2
    assert cum("other") == 1


def test_audit_intent_recorded_but_not_counted(tmp_path):
    """intent 는 ledger 에 남되 누적 카운트엔 안 들어감(executed 만 누적)."""
    led = LedgerLog(tmp_path / "led.jsonl")
    cum, audit = make_lifecycle_wiring(led)
    audit(ControlDecision("start", "voice_lab", Grade.MEDIUM, "intent"))
    assert cum("voice_lab") == 0
    assert "lifecycle_intent" in [e.get("event") for e in led.read()]


def _entry(name="tts_lab"):
    return {"name": name, "title": "TTS 모델 테스트",
            "url": "https://tts.example.com/x", "icon": "🔊", "origin": "jarvis"}


def _local_entry(name="voice_lab", port=8777):
    return {"name": name, "title": "음성 랩", "url": f"http://127.0.0.1:{port}",
            "icon": "🎙️", "origin": "jarvis"}


def _probe_client(tmp_path, entries, controller):
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": entries}), encoding="utf-8")
    routes = make_external_routes(registry_file=str(reg), controller=controller)
    return TestClient(Starlette(routes=routes))


def _client(tmp_path, entries):
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": entries}), encoding="utf-8")
    routes = make_external_routes(registry_file=str(reg))
    return TestClient(Starlette(routes=routes)), reg


def test_external_list_happy(tmp_path):
    client, _ = _client(tmp_path, [_entry("zebra"), _entry("alpha")])
    r = client.get("/api/jarvis/external")
    assert r.status_code == 200
    items = r.json()["external"]
    assert [x["name"] for x in items] == ["alpha", "zebra"]  # name 순
    assert items[0]["url"] == "https://tts.example.com/x"
    assert items[0]["icon"] == "🔊"


def test_external_list_hides_origin(tmp_path):
    """provenance(origin)는 내부 게이트 — 응답에 노출하지 않음."""
    client, _ = _client(tmp_path, [_entry()])
    items = client.get("/api/jarvis/external").json()["external"]
    assert "origin" not in items[0]


def test_external_list_filters_bad_provenance(tmp_path):
    """fail-closed: origin != jarvis 엔트리는 노출 0(레지스트리가 거른 결과)."""
    bad = {"name": "thirdparty", "title": "x", "url": "https://x.io", "origin": "evil"}
    client, _ = _client(tmp_path, [_entry("good"), bad])
    items = client.get("/api/jarvis/external").json()["external"]
    assert [x["name"] for x in items] == ["good"]


def test_external_list_missing_file_empty(tmp_path):
    routes = make_external_routes(registry_file=str(tmp_path / "nope.json"))
    client = TestClient(Starlette(routes=routes))
    r = client.get("/api/jarvis/external")
    assert r.status_code == 200
    assert r.json()["external"] == []


# ── 제어측 slice-1a: 상태 probe (localhost 카드만, ProcessController 경유) ──────
def test_probe_localhost_listening(tmp_path):
    """localhost 카드 = health probe(저위험·자율) → listening 반환."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    client = _probe_client(tmp_path, [_local_entry()], ctrl)
    r = client.get("/api/jarvis/external/probe?name=voice_lab")
    assert r.status_code == 200
    body = r.json()
    assert body["probeable"] is True
    assert body["listening"] is True
    assert body["grade"] == "LOW"
    assert body["outcome"] == "executed"


def test_probe_localhost_down(tmp_path):
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=False))
    client = _probe_client(tmp_path, [_local_entry()], ctrl)
    body = client.get("/api/jarvis/external/probe?name=voice_lab").json()
    assert body["probeable"] is True
    assert body["listening"] is False


def test_probe_non_localhost_not_probeable(tmp_path):
    """외부 호스트 카드 = probe 미지원(B-4 localhost 한정). 점 없음."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    client = _probe_client(tmp_path, [_entry("remote")], ctrl)
    body = client.get("/api/jarvis/external/probe?name=remote").json()
    assert body["probeable"] is False
    assert "listening" not in body


def test_probe_unknown_name_404(tmp_path):
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    client = _probe_client(tmp_path, [_local_entry()], ctrl)
    assert client.get("/api/jarvis/external/probe?name=nope").status_code == 404


def test_probe_provenance_only_registry_entries(tmp_path):
    """레지스트리에 없는 임의 대상은 probe 불가(provenance — registry가 유일 출처)."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    # bad provenance 엔트리는 registry가 이미 제외 → probe도 not found
    bad = {"name": "evil", "title": "x", "url": "http://127.0.0.1:8777", "origin": "third_party"}
    client = _probe_client(tmp_path, [bad], ctrl)
    assert client.get("/api/jarvis/external/probe?name=evil").status_code == 404


# ── 제어측 slice-1b: lifecycle 라우트 (start/stop/restart/adopt, propose 경유) ──
class _FakeLauncher:
    def __init__(self):
        self.spawned = []
        self.signaled = []
        self._pid = 1000

    def spawn(self, argv, cwd, env):
        self._pid += 1
        self.spawned.append((argv, cwd))
        return self._pid

    def signal(self, pid, sig):
        self.signaled.append((pid, sig))


def _lifecycle_ctrl(launcher, port_pid=lambda p: None):
    return ProcessController(
        launcher=launcher, approver=lambda req: True,
        owner_starttime=lambda pid: 5000, cumulative_count=lambda n: 0,
        port_pid=port_pid, now=lambda: 0.0, sleep=lambda _s: None,
        prober=lambda t: ProbeStatus(listening=True),
    )


def _ctrl_entry(name="voice_lab", port=8777):
    e = _local_entry(name, port)
    e["control"] = {"launch_argv": ["python", "server.py"], "cwd": "/srv/voice_lab"}
    return e


def test_lifecycle_unconfirmed_does_not_execute(tmp_path):
    """C-2 1-클릭 게이트: confirmed 없으면 needs_confirm 만 반환, 집행 0."""
    lc = _FakeLauncher()
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(lc))
    r = client.post("/api/jarvis/external/lifecycle", json={"name": "voice_lab", "action": "start"})
    assert r.status_code == 200
    body = r.json()
    assert body["needs_confirm"] is True
    assert lc.spawned == []  # 집행 0


def test_lifecycle_confirmed_start_executes(tmp_path):
    lc = _FakeLauncher()
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(lc))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "voice_lab", "action": "start", "confirmed": True})
    body = r.json()
    assert body["outcome"] == "executed"
    assert body["grade"] == "MEDIUM"
    assert lc.spawned == [(["python", "server.py"], "/srv/voice_lab")]


def test_lifecycle_adopt_is_high_cutover(tmp_path):
    """adopt = HIGH cutover. 미소유 점유 정지 → 재spawn."""
    lc = _FakeLauncher()
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(lc, port_pid=lambda p: 502419))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "voice_lab", "action": "adopt", "confirmed": True})
    body = r.json()
    assert body["grade"] == "HIGH"
    assert body["outcome"] == "executed"
    assert any(pid == 502419 for pid, _ in lc.signaled)  # 미소유 정지
    assert len(lc.spawned) == 1                            # 재기동


def test_lifecycle_stop_unowned_referred(tmp_path):
    """미소유(start 안 한) 프로세스 stop = referred(인수 권유)."""
    lc = _FakeLauncher()
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(lc, port_pid=lambda p: 502419))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "voice_lab", "action": "stop", "confirmed": True})
    assert r.json()["outcome"] == "referred"
    assert lc.signaled == []


def test_lifecycle_unknown_action_400(tmp_path):
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(_FakeLauncher()))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "voice_lab", "action": "rm_rf", "confirmed": True})
    assert r.status_code == 400


def test_lifecycle_unknown_name_404(tmp_path):
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(_FakeLauncher()))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "ghost", "action": "start", "confirmed": True})
    assert r.status_code == 404


def test_lifecycle_external_host_not_controllable(tmp_path):
    """B-4: 외부 호스트 카드 = 제어 불가."""
    client = _probe_client(tmp_path, [_entry("remote")], _lifecycle_ctrl(_FakeLauncher()))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "remote", "action": "start", "confirmed": True})
    assert r.json()["controllable"] is False


def test_lifecycle_cross_origin_forbidden(tmp_path):
    """CSRF: cross-origin POST 거부(same_origin 가드)."""
    client = _probe_client(tmp_path, [_ctrl_entry()], _lifecycle_ctrl(_FakeLauncher()))
    r = client.post("/api/jarvis/external/lifecycle",
                    json={"name": "voice_lab", "action": "start", "confirmed": True},
                    headers={"origin": "http://evil.com", "host": "127.0.0.1:8765"})
    assert r.status_code == 403


def test_probe_default_controller_real_socket(tmp_path):
    """controller 미주입 시 기본 ProcessController(실 socket). 죽은 포트 → listening False."""
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": [_local_entry(port=59999)]}), encoding="utf-8")
    routes = make_external_routes(registry_file=str(reg))
    client = TestClient(Starlette(routes=routes))
    body = client.get("/api/jarvis/external/probe?name=voice_lab").json()
    assert body["probeable"] is True
    assert body["listening"] is False
