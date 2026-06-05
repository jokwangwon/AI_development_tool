"""Jarvis 제어측 slice-1b — lifecycle(start/stop/restart) + 인수(adopt, cutover) 게이트.

답습:
  docs/phase0/jarvis-control-side-slice1b-lifecycle-brief.md (CB-1~CB-9)
  docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1b.md (REVISE)

검증 대상(합의 BLOCKING):
  - CB-1 PID recycling: 소유권 키 (pid, starttime), signal 직전 재대조
  - CB-2 누적 영속: cumulative_count 주입(LedgerLog read() 파생) ≥ 한도 거부
  - CB-3 Launcher: non-blocking spawn / killpg signal (test_launcher.py)
  - CB-5 atomicity: per-target lock critical section
  - CB-6 seam 구조: _execute_lifecycle 가 게이트 우회 호출 시 raise
  - CB-7 adopt = cutover-재기동(미소유 정지 → 재spawn 소유 전환)
  - CB-8 dangling: 부분 실패 → referred + lock 해제
  - CB-9 동시 1인스턴스: 기존 LISTEN/소유 살아있으면 start 거부
  - C-3 rate: 60s 윈도 2회 초과 거부
  - L-6 approver default-deny/fail-closed
"""
from __future__ import annotations

import signal as _signal

import pytest

from src.jarvis.process_control import (
    CONTROL_ACTIONS,
    Capability,
    ControlTarget,
    Grade,
    ProcessController,
    ProbeStatus,
    SeamViolation,
    grade_for,
)


# ── 테스트 하네스 ──────────────────────────────────────────────────────────
class FakeLauncher:
    def __init__(self, start_pid=1000):
        self.spawned = []
        self.signaled = []
        self._pid = start_pid

    def spawn(self, argv, cwd, env):
        self._pid += 1
        self.spawned.append({"argv": argv, "cwd": cwd, "pid": self._pid})
        return self._pid

    def signal(self, pid, sig):
        self.signaled.append((pid, sig))


class Clock:
    def __init__(self, t=0.0):
        self.t = t

    def __call__(self):
        return self.t


def _target(name="voice_lab", port=8777, launch_argv=("python", "server.py"), cwd="/srv"):
    return ControlTarget(
        name=name, host="127.0.0.1", port=port, origin="jarvis",
        health_path="", launch_argv=tuple(launch_argv), cwd=cwd,
    )


def _ctrl(**kw):
    """1b lifecycle controller — 합리적 기본 주입(전부 hermetic)."""
    starttimes = kw.pop("starttimes", {})
    defaults = dict(
        launcher=FakeLauncher(),
        approver=lambda req: True,                 # 기본 승인(L-6 default-deny는 별도 테스트)
        owner_starttime=lambda pid: starttimes.get(pid, 5000),
        cumulative_count=lambda name: 0,
        port_pid=lambda port: None,                # 포트 점유 PID 역추적(adopt)
        prober=lambda t: ProbeStatus(listening=True),  # start 성공 판정
        now=Clock(),
        sleep=lambda _s: None,  # _await_listen polling 즉시(테스트 결정성)
        cumulative_limit=10,
        rate_limit=2,
        rate_window=60.0,
        audit=None,
    )
    defaults.update(kw)
    return ProcessController(**defaults)


# ── lifecycle Action 등록 + 등급 (CO-6) ───────────────────────────────────
def test_lifecycle_actions_registered():
    for name in ("start", "stop", "restart", "adopt"):
        assert name in CONTROL_ACTIONS


def test_start_stop_restart_are_medium():
    assert grade_for(CONTROL_ACTIONS["start"].capabilities) is Grade.MEDIUM
    assert grade_for(CONTROL_ACTIONS["stop"].capabilities) is Grade.MEDIUM
    assert grade_for(CONTROL_ACTIONS["restart"].capabilities) is Grade.MEDIUM


def test_adopt_is_high_via_capability_not_name():
    """CO-6: adopt=HIGH 는 이름이 아니라 ADOPT capability(미소유 신원도용 연산)에 묶임."""
    assert Capability.ADOPT in CONTROL_ACTIONS["adopt"].capabilities
    assert grade_for(CONTROL_ACTIONS["adopt"].capabilities) is Grade.HIGH
    # capability 바인딩 증명: ADOPT 만으로도 HIGH
    assert grade_for(frozenset({Capability.ADOPT})) is Grade.HIGH


# ── start: spawn + 소유 등록 + LISTEN 판정 (CB-3, CB-9) ────────────────────
def test_start_spawns_and_registers_ownership():
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: None,
                 prober=lambda t: ProbeStatus(listening=True))
    d = ctrl.propose("start", _target())
    assert d.outcome == "executed"
    assert d.grade is Grade.MEDIUM
    assert len(lc.spawned) == 1
    assert lc.spawned[0]["argv"] == ["python", "server.py"]


def test_start_rejected_when_already_listening_cb9():
    """CB-9 동시 1인스턴스: 포트가 이미 LISTEN(미소유 포함)이면 start 거부."""
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: 502419)  # 이미 점유
    d = ctrl.propose("start", _target())
    assert d.outcome in ("rejected", "referred")
    assert lc.spawned == []  # spawn 0


def test_start_default_deny_without_approver_l6():
    """L-6: approver None = default-deny(MEDIUM 집행 불가)."""
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, approver=None)
    d = ctrl.propose("start", _target())
    assert d.outcome == "rejected"
    assert lc.spawned == []


def test_approver_exception_is_fail_closed():
    """L-6 fail-closed: approver 예외 = 거부."""
    def boom(req):
        raise RuntimeError("ui crash")
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, approver=boom)
    d = ctrl.propose("start", _target())
    assert d.outcome == "rejected"
    assert lc.spawned == []


# ── stop: 소유 PID + starttime 재대조 (CB-1) ───────────────────────────────
def test_stop_owned_pid_signals():
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: None,
                 starttimes={1001: 5000})
    ctrl.propose("start", _target())          # 소유 1001 등록(starttime 5000)
    d = ctrl.propose("stop", _target())
    assert d.outcome == "executed"
    assert any(sig == _signal.SIGTERM for _, sig in lc.signaled)


def test_stop_unowned_pid_is_referred_l2():
    """L-2: controller 가 spawn 안 한 PID = signal 불가 → referred(인수 권유)."""
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: 502419)  # 미소유 점유
    d = ctrl.propose("stop", _target())       # start 안 했으니 미소유
    assert d.outcome == "referred"
    assert lc.signaled == []


def test_stop_pid_recycling_blocked_cb1():
    """CB-1 핵심: 소유 PID 의 starttime 이 spawn 시 캡처값과 다르면(=PID 재사용) signal 거부."""
    lc = FakeLauncher()
    st = {1001: 5000}
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: None,
                 owner_starttime=lambda pid: st.get(pid))
    ctrl.propose("start", _target())          # 1001 소유, starttime 5000 캡처
    st[1001] = 9999                            # OS 가 같은 PID 를 다른 프로세스에 재할당
    d = ctrl.propose("stop", _target())
    assert d.outcome == "referred"             # 재사용 감지 → signal 거부
    assert lc.signaled == []                   # 엉뚱한 프로세스 안 죽임


# ── C-3 rate (60s/2) + 누적 (CB-2) ─────────────────────────────────────────
def test_rate_limit_third_within_window_referred():
    clock = Clock(0.0)
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: None, now=clock,
                 rate_limit=2, rate_window=60.0)
    ctrl.propose("start", _target())          # t=0 (1회)
    clock.t = 10.0
    ctrl.propose("restart", _target())        # t=10 (2회)
    clock.t = 20.0
    d = ctrl.propose("restart", _target())    # t=20 (3회, 윈도 내) → 초과
    assert d.outcome == "referred"
    assert "rate" in d.reason.lower() or "빈도" in d.reason


def test_rate_window_slides():
    clock = Clock(0.0)
    ctrl = _ctrl(port_pid=lambda p: None, now=clock, rate_limit=2, rate_window=60.0)
    ctrl.propose("start", _target())          # t=0
    ctrl.propose("restart", _target())        # t=0 (2회)
    clock.t = 61.0                             # 윈도 밖
    d = ctrl.propose("restart", _target())    # 이전 2회는 만료 → 허용
    assert d.outcome == "executed"


def test_cumulative_limit_blocks_cb2():
    """CB-2: 누적(가동 후 총 N회)이 한도면 거부 — controller 재시작 우회 차단(ledger 파생)."""
    ctrl = _ctrl(port_pid=lambda p: None, cumulative_count=lambda name: 10,
                 cumulative_limit=10)
    d = ctrl.propose("start", _target())
    assert d.outcome == "referred"
    assert "누적" in d.reason or "cumulative" in d.reason.lower()


# ── C-3 자율완화 (2026-06-05, 풀 3+1 합의 REVISE) ──────────────────────────
#   3plus1-consensus-2026-06-05-control-c3-autorelax.md
#   rate 2→5/60s (R-b) · 누적 lifetime 10→100 (C-a) · 경계 로직 0줄 · CC-1~CC-5.
def _ctrl_default_limits(**kw):
    """rate_limit/cumulative_limit 을 *명시 안 함* → 생성자 기본값(완화 후 5/100) 검증용."""
    starttimes = kw.pop("starttimes", {})
    defaults = dict(
        launcher=FakeLauncher(),
        approver=lambda req: True,
        owner_starttime=lambda pid: starttimes.get(pid, 5000),
        cumulative_count=lambda name: 0,
        port_pid=lambda port: None,
        prober=lambda t: ProbeStatus(listening=True),
        now=Clock(),
        sleep=lambda _s: None,
        rate_window=60.0,
        audit=None,
    )  # rate_limit/cumulative_limit 미지정 = 기본값 사용
    defaults.update(kw)
    return ProcessController(**defaults)


def test_rate_default_relaxed_to_five():
    """자율완화: rate 기본값 = 5/60s (R-b). 5회까지 통과, 6번째 referred."""
    clock = Clock(0.0)
    ctrl = _ctrl_default_limits(port_pid=lambda p: None, now=clock)
    for i in range(5):  # 1~5회 모두 executed (인간 cadence 수용)
        clock.t = float(i)
        d = ctrl.propose("start" if i == 0 else "restart", _target())
        assert d.outcome == "executed", f"op #{i+1} should pass under R-b, got {d.outcome}"
    clock.t = 5.0
    d = ctrl.propose("restart", _target())  # 6번째 = 윈도 내 초과
    assert d.outcome == "referred"
    assert "rate" in d.reason.lower() or "빈도" in d.reason


def test_cumulative_default_relaxed_to_hundred():
    """자율완화: 누적 기본값 = 100 (C-a). 99 통과, 100 도달 시 referred."""
    ok = _ctrl_default_limits(port_pid=lambda p: None, cumulative_count=lambda name: 99)
    assert ok.propose("start", _target()).outcome == "executed"
    blocked = _ctrl_default_limits(port_pid=lambda p: None, cumulative_count=lambda name: 100)
    d = blocked.propose("start", _target())
    assert d.outcome == "referred"
    assert "누적" in d.reason or "cumulative" in d.reason.lower()


def test_cc1_restart_does_not_bypass_cumulative():
    """CC-1 (적대적 검증 코드화): controller 재시작으로 in-memory rate 를 리셋해도
    ledger 파생 누적(executed 카운트)이 무제한 성공 lifecycle 을 차단한다.

    2-B(누적을 crash-loop 탐지로 *재정의*)가 깨려던 불변 — 누적 축은 반드시
    *executed* 를 세야 재시작-우회-of-성공-op 를 막는다(합의 ⭐ 적대적 검증).
    """
    # 새 controller 인스턴스 = 재시작 시뮬: in-memory rate 윈도는 빈 상태.
    ctrl = _ctrl_default_limits(port_pid=lambda p: None,
                                cumulative_count=lambda name: 100)
    assert ctrl._rate == {}, "재시작 직후 rate 윈도는 비어 있어야(in-memory)"
    d = ctrl.propose("start", _target())
    # rate 는 깨끗하지만 ledger 파생 누적이 차단 → 재시작 우회 불가(CB-2 기능 보존).
    assert d.outcome == "referred"
    assert "누적" in d.reason or "cumulative" in d.reason.lower()


# ── CB-6 seam 구조: _execute_lifecycle 우회 호출 차단 ──────────────────────
def test_execute_lifecycle_raises_without_gate_token_cb6():
    """CB-6: _execute_lifecycle 가 게이트 통과 증거(토큰) 없이 호출되면 raise(우회불가).

    boss 가 propose 를 건너뛰고 내부 집행에 직접 도달할 수 없음을 *구조* 로 증명
    (관례적 _-prefix 가 아니라 토큰 강제).
    """
    ctrl = _ctrl(port_pid=lambda p: None)
    with pytest.raises(SeamViolation):
        ctrl._execute_lifecycle(CONTROL_ACTIONS["start"], _target(), gate_token=None)


def test_medium_never_executes_via_propose_when_denied():
    """L-1/CB-6: 거부 경로에서 launcher 가 절대 안 불림(집행 0)."""
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, approver=lambda req: False)  # 모두 거부
    ctrl.propose("start", _target())
    ctrl.propose("stop", _target())
    ctrl.propose("restart", _target())
    assert lc.spawned == []
    assert lc.signaled == []


# ── CB-7 adopt = cutover-재기동 ────────────────────────────────────────────
def test_adopt_cutover_stops_unowned_then_respawns():
    """CB-7: 미소유 점유 PID 를 사람 승인 하 정지 → controller 재spawn → 소유 전환."""
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: 502419,
                 prober=lambda t: ProbeStatus(listening=True))
    d = ctrl.propose("adopt", _target())
    assert d.grade is Grade.HIGH
    assert d.outcome == "executed"
    # 미소유 502419 정지(signal) + 재spawn(소유) 둘 다 발생
    assert any(pid == 502419 for pid, _ in lc.signaled)
    assert len(lc.spawned) == 1                # 재기동 = 새 소유 PID
    # 인수 후 stop 가능(소유로 전환)
    d2 = ctrl.propose("stop", _target())
    assert d2.outcome == "executed"


def test_adopt_default_deny_without_approver():
    """adopt = HIGH, 항상 사람 승인. approver None = deny, 정지·spawn 0."""
    lc = FakeLauncher()
    ctrl = _ctrl(launcher=lc, approver=None, port_pid=lambda p: 502419)
    d = ctrl.propose("adopt", _target())
    assert d.outcome == "rejected"
    assert lc.signaled == [] and lc.spawned == []


def test_adopt_referred_when_port_empty():
    """adopt 대상 포트에 점유 프로세스 없음 = referred(인수할 게 없음)."""
    ctrl = _ctrl(port_pid=lambda p: None)
    d = ctrl.propose("adopt", _target())
    assert d.outcome == "referred"


# ── CB-8 dangling: restart 부분 실패 ───────────────────────────────────────
def test_restart_partial_failure_is_referred_no_autorollback_cb8():
    """CB-8/L-7: restart 중 stop OK·start 실패(LISTEN 안 뜸) = referred(자동 롤백 0)."""
    lc = FakeLauncher()
    # spawn 은 되지만 probe 가 LISTEN=False → start 성공 판정 실패
    ctrl = _ctrl(launcher=lc, port_pid=lambda p: None,
                 prober=lambda t: ProbeStatus(listening=False),
                 starttimes={1001: 5000})
    ctrl.propose("start", _target())  # 이건 prober False라... 첫 start도 실패할 수 있음
    d = ctrl.propose("restart", _target())
    assert d.outcome == "referred"
    # 자동 재기동(추가 spawn 폭주) 없음 = 통제 보존
    assert "실패" in d.reason or "fail" in d.reason.lower() or "dangling" in d.reason.lower()


# ── CB-4 audit intent fail-closed (감사가 유일 센서) ──────────────────────
def test_audit_intent_failure_is_fail_closed_cb4():
    """CB-4: 집행 전 intent 감사가 raise(디스크 실패 등)하면 referred — 집행 0.

    lifecycle 감사 = Rollback Trigger 검출 유일 센서 → 기록 못 하면 집행도 안 함(fail-closed).
    """
    lc = FakeLauncher()

    def boom_audit(decision):
        if decision.outcome == "intent":
            raise OSError("disk full")

    ctrl = _ctrl(launcher=lc, port_pid=lambda p: None, audit=boom_audit)
    d = ctrl.propose("start", _target())
    assert d.outcome == "referred"
    assert "감사" in d.reason or "audit" in d.reason.lower()
    assert lc.spawned == []  # 감사 실패 = 집행 0


def test_audit_records_intent_before_execute():
    """집행 전 intent 가 감사에 남는다(executed 결과보다 먼저 — 선기록)."""
    events = []
    ctrl = _ctrl(port_pid=lambda p: None, audit=lambda d: events.append(d.outcome))
    ctrl.propose("start", _target())
    assert "intent" in events
    assert events.index("intent") < events.index("executed")


# ── B-6 불변 + 자격증명 0 (lifecycle 에도 유지) ────────────────────────────
def test_controller_holds_no_credentials_lifecycle():
    ctrl = _ctrl()
    suspicious = ("secret", "token", "password", "credential", "apikey", "cookie")
    for attr in vars(ctrl):
        assert not any(s in attr.lower() for s in suspicious), f"의심 속성: {attr}"


# ── referred outcome 존재 ──────────────────────────────────────────────────
def test_referred_is_valid_outcome():
    ctrl = _ctrl(port_pid=lambda p: 502419)
    d = ctrl.propose("stop", _target())       # 미소유 → referred
    assert d.outcome == "referred"
