"""Jarvis 제어측 slice-1a — 프로세스 제어 controller 골격 + capability 등급 + 포트 LISTEN probe.

답습:
  docs/phase0/jarvis-control-side-general-executor-brief.md v2 §5 (slice-1a)
  docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1.md (REVISE, BLOCKING B-1~B-6)

북극성: Jarvis = 사용자 명령을 (Claude 처럼) 수행하는 일반 실행 에이전트. 그 "실행 도구"의
첫 조각 = 프로세스 제어. slice-1a 는 가장 안전한 동작(읽기성 probe, 자율)만 먼저 박는다.

설계 (BLOCKING 답습):
  - **B-1 propose-only seam**: boss(untrusted)는 ProcessController.propose() 만 호출. 실제 집행
    `_execute` 는 등급 검증 통과 시 controller 내부에서만 호출 — boss 가 등급 게이팅을 우회해
    집행에 도달할 수 없다. (ApprovalGate default-deny 패턴 동형.)
  - **B-2 provenance 상속**: 제어 대상 origin == "jarvis" 아니면 거부(읽기측 external_registry
    와 동일 fail-closed). origin 불명/제3자 = 제어 대상 아님.
  - **B-4 localhost 한정 + probe**: host 는 127.0.0.1/localhost 만(SSRF 차단). voice_lab `/health`
    부재(실측) → 포트 LISTEN 확인 + HTTP 선택적(health_path 있을 때만, 주입형).
  - **B-5 등급 = capability 바인딩(코어 고정)**: 동작 *이름 문자열* 아닌 실제 원시 연산(probe/
    spawn/signal)에 등급 부착. probe=저(자율) / spawn·signal=중 / 미등재·unknown=고(fail-closed).
    대상 추가 시 코어 등급 매핑 수정 0 → Provider Liquidity 보존.
  - **B-6 자격증명 0**: controller 는 어떤 자격증명도 보유하지 않는다(C-β).

이 모듈은 **순수 로직 + 주입형 부작용**(연결/HTTP probe 는 주입). lifecycle(start/stop/restart =
중위험·게이트)은 slice-1b — 본 슬라이스 범위 밖(CONTROL_ACTIONS 미등록).
"""
from __future__ import annotations

import re
import signal as _signal_mod
import threading
import time
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Optional

from src.jarvis.external_registry import JARVIS_ORIGIN  # B-2 provenance 상속(단일 출처)
from src.jarvis.launcher import read_starttime  # CB-1 (pid, starttime) 소유권 키

# name = 소문자 영숫자 + _ - (path separator·..·공백·대문자 차단 — registry 답습)
_SAFE_NAME = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

# B-4: 제어 대상 host 는 로컬 only(SSRF·외부 시스템 접근 차단). slice-1a = localhost 프로세스.
_LOCALHOST_HOSTS = frozenset({"127.0.0.1", "localhost", "::1"})


def is_localhost(host: object) -> bool:
    """host 가 로컬 전용인지(B-4 SSRF 차단 판정 — 호출측이 probe 대상 선별에 사용)."""
    return host in _LOCALHOST_HOSTS


class ControlError(Exception):
    """제어 대상 검증 실패."""


class Capability:
    """제어 동작이 실제로 수행하는 원시 연산(등급은 *이름*이 아닌 이 연산에 묶인다 — B-5)."""

    PROBE = "probe"    # 읽기: 포트 LISTEN/health 조회 (가역·부작용 0)
    SPAWN = "spawn"    # 쓰기: 프로세스 기동 (slice-1b)
    SIGNAL = "signal"  # 쓰기: 프로세스에 시그널(stop/restart) (slice-1b)
    ADOPT = "adopt"    # 쓰기: 미소유 프로세스 신원도용 = cutover 인수 (slice-1b, HIGH)


class Grade(Enum):
    """리스크 등급(§3.5). 값은 max 비교용 순서."""

    LOW = 1     # 가역·저위험 → 자율 집행
    MEDIUM = 2  # 중 → 게이트(초기 1-클릭, slice-1b)
    HIGH = 3    # 비가역/미상 → 사람 승인(fail-closed 기본값)


# capability → 등급 코어 고정 매핑(G6(a), X-3). 미등재 capability = 고위험 fail-closed.
# adopt = 미소유 프로세스 신원도용 *연산* 이라 HIGH(이름이 아니라 capability 바인딩 — CO-6).
_CAP_GRADE = {
    Capability.PROBE: Grade.LOW,
    Capability.SPAWN: Grade.MEDIUM,
    Capability.SIGNAL: Grade.MEDIUM,
    Capability.ADOPT: Grade.HIGH,
}


def grade_for(capabilities: frozenset) -> Grade:
    """capability 집합 → 등급(코어 고정). 빈 집합·미등재 capability = 고위험(fail-closed).

    혼합 시 가장 높은 등급(max). 대상·boss·모델과 무관(Provider Liquidity).
    """
    if not capabilities:
        return Grade.HIGH  # 미상 = 보수적 고위험
    best = Grade.LOW
    for cap in capabilities:
        g = _CAP_GRADE.get(cap)
        if g is None:
            return Grade.HIGH  # 미등재 capability = fail-closed
        if g.value > best.value:
            best = g
    return best


@dataclass(frozen=True)
class Action:
    """코어가 정의한 제어 동작 = 이름 + 실제 수행 capability 집합."""

    name: str
    capabilities: frozenset


# 코어 고정 allowlist(미등재 = 고위험 fail-closed). 미등재 동작 = unknown → 고위험.
# slice-1a = health(probe, 저). slice-1b = lifecycle(spawn/signal, 중) + adopt(HIGH).
CONTROL_ACTIONS: dict[str, Action] = {
    "health": Action("health", frozenset({Capability.PROBE})),
    # slice-1b lifecycle — MEDIUM(게이트). restart = signal(정지)+spawn(재기동).
    "start": Action("start", frozenset({Capability.SPAWN})),
    "stop": Action("stop", frozenset({Capability.SIGNAL})),
    "restart": Action("restart", frozenset({Capability.SIGNAL, Capability.SPAWN})),
    # slice-1b 인수 = cutover(미소유 정지 → 재spawn). ADOPT capability 로 HIGH(CO-6).
    "adopt": Action("adopt", frozenset({Capability.SIGNAL, Capability.SPAWN, Capability.ADOPT})),
}


@dataclass(frozen=True)
class ControlTarget:
    """검증된 제어 대상(불변). 자비스가 도와 만든 로컬 프로세스 한정(B-2/B-4).

    제어 필드(launch_argv/cwd, C-4/L-10) = lifecycle 집행에 필요한 registry 주입 값.
    argv 리스트(쉘 미경유, L-8). probe-only(1a) 대상은 빈 launch_argv 로 둔다.
    """

    name: str
    host: str
    port: int
    origin: str = ""
    health_path: str = ""
    launch_argv: tuple = ()  # CB-3/L-8: registry 주입 argv(쉘 문자열 금지)
    cwd: str = ""


def parse_target(data: object) -> ControlTarget:
    """대상 dict → ControlTarget. 검증 실패 시 ControlError.

    검증: name 안전(traversal 차단) + host localhost(B-4) + port 1..65535 +
    origin == jarvis(B-2 provenance fail-closed).
    """
    if not isinstance(data, dict):
        raise ControlError("target must be an object")

    name = data.get("name")
    if not isinstance(name, str) or not _SAFE_NAME.match(name):
        raise ControlError(f"unsafe target name: {name!r}")

    host = data.get("host")
    if host not in _LOCALHOST_HOSTS:
        raise ControlError(f"host must be localhost (SSRF 차단): {host!r}")

    port = data.get("port")
    if not isinstance(port, int) or isinstance(port, bool) or not (1 <= port <= 65535):
        raise ControlError(f"port must be int 1..65535: {port!r}")

    # B-2 provenance fail-closed: origin 불명/제3자 = 제어 대상 아님(§1.5 비협상).
    if data.get("origin") != JARVIS_ORIGIN:
        raise ControlError(
            f"origin must be {JARVIS_ORIGIN!r} (provenance fail-closed): {data.get('origin')!r}"
        )

    health_path = data.get("health_path", "")
    return ControlTarget(
        name=name,
        host=host,
        port=port,
        origin=JARVIS_ORIGIN,
        health_path=health_path if isinstance(health_path, str) else "",
    )


@dataclass(frozen=True)
class ProbeStatus:
    """probe 결과: 포트 LISTEN 여부 + (health_path 있을 때) HTTP 응답 여부."""

    listening: bool
    http_ok: Optional[bool] = None


def _default_connector(host: str, port: int, timeout: float = 0.5) -> bool:
    import socket

    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _default_http_get(url: str, timeout: float = 1.0) -> bool:
    import urllib.request

    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:  # noqa: S310 (localhost only)
            return 200 <= getattr(resp, "status", 0) < 400
    except Exception:
        return False


def probe_target(
    target: ControlTarget,
    *,
    connector: Callable[..., bool] = _default_connector,
    http_get: Callable[..., bool] = _default_http_get,
) -> ProbeStatus:
    """포트 LISTEN 확인 + (health_path 있으면) HTTP 조회. localhost 한정(B-4).

    연결 예외 = LISTEN 아님(crash 아님). health_path 없으면 HTTP 생략(voice_lab /health 부재).
    """
    if target.host not in _LOCALHOST_HOSTS:
        raise ControlError(f"probe host must be localhost: {target.host!r}")

    try:
        listening = bool(connector(target.host, target.port, timeout=0.5))
    except Exception:
        listening = False

    http_ok: Optional[bool] = None
    if target.health_path:
        url = f"http://{target.host}:{target.port}{target.health_path}"
        try:
            http_ok = bool(http_get(url, timeout=1.0))
        except Exception:
            http_ok = False

    return ProbeStatus(listening=listening, http_ok=http_ok)


@dataclass(frozen=True)
class ControlDecision:
    """propose 결정(감사·반환). outcome ∈ {executed, rejected, referred}.

    referred(slice-1b) = 사람 회부(미소유 PID·PID 재사용·C-3 초과·부분 실패) — 자동
    집행도 단순 거부도 아닌 "사람이 판단해야 함". pid = 집행 대상/결과 PID(감사·HUD).
    """

    action: str
    target_name: str
    grade: Grade
    outcome: str
    result: Any = None
    reason: str = ""
    pid: Optional[int] = None


class SeamViolation(Exception):
    """CB-6: 게이트/lock 통과 증거(토큰) 없이 lifecycle 집행에 도달 = seam 우회.

    boss 가 propose 를 건너뛰고 내부 `_execute_lifecycle` 에 직접 도달하면 이 예외로
    *구조적* 차단(관례적 `_`-prefix 가 아니라 토큰 강제 — L-1/CB-6 우회불가).
    """


class _GateToken:
    """`_gated_lifecycle` 내부에서만 생성되는 게이트 통과 증거(CB-6)."""


class _LifecyclePartialFailure(Exception):
    """CB-8: lifecycle 집행 중 부분 실패. 자동 롤백 0 → referred(통제 보존, L-7)."""


class ProcessController:
    """제어 동작 결정적 집행자(B-1 seam). boss 는 propose() 만 호출.

    propose 흐름: provenance/localhost 검증(B-2/B-4) → 코어 allowlist 조회(미등재=고 fail-closed)
    → capability 등급(B-5) → 저위험(probe)만 자율 집행. 중/고위험(lifecycle/adopt)은
    per-target lock 안에서 C-3 2축 → 사전 조건 → 승인 → 감사 → 집행(CB-1~CB-9). 자격증명 0(B-6).

    슬라이스 주입(전부 hermetic 테스트 seam, Provider Liquidity):
      launcher  = lifecycle 집행 백엔드(CB-3). 없으면 lifecycle 집행 불가(fail-closed).
      approver  = 게이트 콜백(L-6). None = default-deny.
      owner_starttime(pid)->starttime  = CB-1 PID 재사용 차단(기본 /proc).
      cumulative_count(name)->int      = CB-2 누적(LedgerLog read() 파생, server 배선).
      port_pid(port)->pid|None         = 포트 점유 PID 역추적(동시1인스턴스/adopt).
      now()->float                     = rate 윈도 시계(테스트 결정성).
    """

    def __init__(
        self,
        actions: Optional[dict] = None,
        prober: Optional[Callable[[ControlTarget], ProbeStatus]] = None,
        audit: Optional[Callable[[ControlDecision], None]] = None,
        *,
        launcher: Any = None,
        approver: Optional[Callable[[dict], bool]] = None,
        owner_starttime: Optional[Callable[[int], Optional[int]]] = None,
        cumulative_count: Optional[Callable[[str], int]] = None,
        port_pid: Optional[Callable[[int], Optional[int]]] = None,
        now: Optional[Callable[[], float]] = None,
        sleep: Optional[Callable[[float], None]] = None,
        cumulative_limit: int = 100,  # C-3 자율완화(2026-06-05 합의 C-a): lifetime cap 10→100
        rate_limit: int = 5,          # C-3 자율완화(R-b): 60s 윈도 2→5(인간 cadence 수용)
        rate_window: float = 60.0,
        start_probe_attempts: int = 30,
        start_probe_interval: float = 0.1,
    ) -> None:
        self._actions = dict(CONTROL_ACTIONS if actions is None else actions)
        self._prober = prober if prober is not None else probe_target
        self._audit = audit
        self._launcher = launcher
        self._approver = approver
        self._owner_starttime = owner_starttime if owner_starttime is not None else read_starttime
        self._cumulative_count = cumulative_count
        self._port_pid = port_pid
        self._now = now if now is not None else time.monotonic
        self._sleep = sleep if sleep is not None else time.sleep
        self._cumulative_limit = cumulative_limit
        self._rate_limit = rate_limit
        self._rate_window = rate_window
        self._start_probe_attempts = start_probe_attempts
        self._start_probe_interval = start_probe_interval
        # 내부 상태(자격증명 0 — B-6): 소유권·rate·per-target lock
        self._owned: dict[str, tuple] = {}        # name -> (pid, starttime)  CB-1
        self._rate: dict[str, list] = {}          # name -> [timestamps]      C-3
        self._locks: dict[str, threading.Lock] = {}  # name -> Lock           CB-5
        self._locks_guard = threading.Lock()

    def propose(self, action_name: str, target: ControlTarget) -> ControlDecision:
        """boss-facing 단일 진입점. 결정 후 감사 기록(GP-7, fail-soft sink)."""
        decision = self._decide(action_name, target)
        if self._audit is not None:
            try:
                self._audit(decision)
            except Exception:
                pass  # 결정-후 sink 는 fail-soft. lifecycle intent 감사는 집행 전 fail-closed.
        return decision

    def _decide(self, action_name: str, target: ControlTarget) -> ControlDecision:
        tname = getattr(target, "name", "?")
        # B-2 provenance + B-4 localhost (방어적 재검증 — parse_target 우회 직접 생성 대비)
        if not isinstance(target, ControlTarget) or target.origin != JARVIS_ORIGIN:
            return ControlDecision(action_name, tname, Grade.HIGH, "rejected",
                                   None, "provenance fail-closed (origin != jarvis)")
        if target.host not in _LOCALHOST_HOSTS:
            return ControlDecision(action_name, tname, Grade.HIGH, "rejected",
                                   None, "non-localhost host (SSRF 차단)")

        action = self._actions.get(action_name)
        if action is None:
            # B-5: 미등재 동작 = 고위험 fail-closed
            return ControlDecision(action_name, tname, Grade.HIGH, "rejected",
                                   None, "unregistered action (fail-closed)")

        grade = grade_for(action.capabilities)
        if grade is Grade.LOW:
            result = self._execute(action, target)  # 1a probe — 자율
            return ControlDecision(action_name, tname, grade, "executed", result, "low-grade auto")

        # 중/고위험 = lifecycle/adopt → per-target lock critical section(CB-5 atomicity)
        with self._lock_for(tname):
            return self._gated_lifecycle(action, target, grade)

    # ── 중/고위험 게이트 (lock 안에서만 — CB-5) ────────────────────────────
    def _gated_lifecycle(self, action: Action, target: ControlTarget, grade: Grade) -> ControlDecision:
        name = target.name
        caps = action.capabilities
        is_adopt = Capability.ADOPT in caps

        # launcher 부재 = lifecycle 집행 불가(fail-closed)
        if self._launcher is None:
            return _refer(action, name, grade, "launcher 미배선 (fail-closed)")

        # CB-2 누적(LedgerLog 파생) — 2축 중 누적 먼저(controller 재시작 우회 차단)
        if self._cumulative_count is not None and self._cumulative_count(name) >= self._cumulative_limit:
            return _refer(action, name, grade, f"누적 한도 초과 (cumulative ≥ {self._cumulative_limit})")
        # C-3 rate(슬라이딩 윈도)
        if not self._rate_ok(name):
            return _refer(action, name, grade, f"rate 빈도 한도 초과 ({self._rate_limit}/{int(self._rate_window)}s)")

        # 동작별 사전 조건(CB-9 동시1 / L-2 소유권+CB-1 starttime / adopt 점유)
        pre = self._precheck(action, target, grade, is_adopt)
        if pre is not None:
            return pre

        # approver 게이트(L-6 default-deny/fail-closed, CB-7 adopt 도 항상 승인)
        if not self._approve(action, target, grade):
            return ControlDecision(action.name, name, grade, "rejected", None,
                                   "approval denied (default-deny/fail-closed)")

        # CB-4 audit intent fail-closed(감사 기록 실패 시 집행 안 함)
        try:
            self._audit_intent(action, target, grade)
        except Exception:
            return _refer(action, name, grade, "감사 기록 실패 (audit fail-closed)")

        # 집행(CB-6 토큰 강제). 부분 실패 = referred(CB-8 자동 롤백 0)
        try:
            result, pid = self._execute_lifecycle(action, target, gate_token=_GateToken())
        except _LifecyclePartialFailure as exc:
            return _refer(action, name, grade, str(exc), pid=self._owned.get(name, (None,))[0])
        self._rate_record(name)
        return ControlDecision(action.name, name, grade, "executed", result, "gated executed", pid=pid)

    def _precheck(self, action: Action, target: ControlTarget, grade: Grade,
                  is_adopt: bool) -> Optional[ControlDecision]:
        name = target.name
        caps = action.capabilities
        occupant = self._port_pid(target.port) if self._port_pid is not None else None

        if is_adopt:
            # adopt = 미소유 점유 PID cutover 인수. 점유 없으면 인수 대상 없음.
            if occupant is None:
                return _refer(action, name, grade, "포트 점유 프로세스 없음 (인수 대상 없음)")
            return None

        if Capability.SPAWN in caps and Capability.SIGNAL not in caps:
            # 순수 start: CB-9 동시 1인스턴스 — 기존 LISTEN/소유 살아있으면 거부
            if occupant is not None or name in self._owned:
                return _refer(action, name, grade, "이미 실행 중 (동시 1인스턴스, CB-9)")
            return None

        if Capability.SIGNAL in caps:
            # stop/restart: 소유 PID 필요(L-2) + starttime 재대조(CB-1 PID 재사용)
            owned = self._owned.get(name)
            if owned is None:
                return _refer(action, name, grade, "미소유 프로세스 (signal 불가 — L-2, 인수 권유)")
            pid, st0 = owned
            if self._owner_starttime(pid) != st0:
                return _refer(action, name, grade, "PID 재사용 감지 (starttime 불일치 — CB-1)", pid=pid)
            return None
        return None

    def _execute_lifecycle(self, action: Action, target: ControlTarget,
                           gate_token: Any = None) -> tuple:
        """게이트/lock 통과 후에만 도달(CB-6 토큰 강제). 우회 호출 = SeamViolation."""
        if not isinstance(gate_token, _GateToken):
            raise SeamViolation("_execute_lifecycle requires a valid gate token (CB-6 seam)")
        caps = action.capabilities
        if Capability.ADOPT in caps:
            return self._do_adopt(target)
        if Capability.SPAWN in caps and Capability.SIGNAL not in caps:
            return self._do_start(target)
        if Capability.SIGNAL in caps and Capability.SPAWN not in caps:
            return self._do_stop(target)
        if Capability.SIGNAL in caps and Capability.SPAWN in caps:
            return self._do_restart(target)
        raise SeamViolation("unsupported lifecycle capability set")

    # ── 결정적 lifecycle 절차(launcher 경유) ───────────────────────────────
    def _spawn_and_own(self, target: ControlTarget) -> int:
        pid = self._launcher.spawn(list(target.launch_argv), target.cwd or None, None)
        self._owned[target.name] = (pid, self._owner_starttime(pid))
        return pid

    def _await_free(self, target: ControlTarget) -> None:
        """정지 후 포트 해제 대기(voice_lab 교훈: bind 충돌 방지). best-effort polling.

        해제 안 돼도 spawn 시도(bind 충돌 시 _await_listen 이 dangling 으로 잡음 — CB-8).
        """
        for _i in range(self._start_probe_attempts):
            if not self._prober(target).listening:
                return
            self._sleep(self._start_probe_interval)

    def _await_listen(self, target: ControlTarget) -> bool:
        """CB-3 start 성공 판정 = LISTEN probe(1a 재사용). 실 프로세스 기동 race 방어 polling.

        spawn 즉시 probe 는 기동 전이라 거짓 실패 — 짧게 재시도(테스트는 sleep 주입으로 즉시).
        """
        for i in range(self._start_probe_attempts):
            if self._prober(target).listening:
                return True
            if i < self._start_probe_attempts - 1:
                self._sleep(self._start_probe_interval)
        return False

    def _do_start(self, target: ControlTarget) -> tuple:
        pid = self._spawn_and_own(target)
        if not self._await_listen(target):  # CB-3 start 성공 = LISTEN(기동 대기)
            raise _LifecyclePartialFailure("start 실패: 포트 LISTEN 안 됨 (dangling, 자동 롤백 0)")
        return ({"action": "start", "pid": pid, "listening": True}, pid)

    def _do_stop(self, target: ControlTarget) -> tuple:
        pid = self._owned[target.name][0]  # precheck 에서 소유+starttime 검증됨
        self._launcher.signal(pid, _signal_mod.SIGTERM)
        self._owned.pop(target.name, None)
        return ({"action": "stop", "pid": pid}, pid)

    def _do_restart(self, target: ControlTarget) -> tuple:
        old = self._owned.get(target.name)  # precheck 검증됨
        if old is not None:
            self._launcher.signal(old[0], _signal_mod.SIGTERM)
            self._owned.pop(target.name, None)
            self._await_free(target)  # 포트 해제 대기(bind 충돌 방지)
        pid = self._spawn_and_own(target)
        if not self._await_listen(target):
            raise _LifecyclePartialFailure("restart 실패: 재기동 후 LISTEN 안 됨 (dangling, 자동 롤백 0)")
        return ({"action": "restart", "pid": pid}, pid)

    def _do_adopt(self, target: ControlTarget) -> tuple:
        """CB-7 cutover-재기동: 미소유 점유 정지(사람 승인) → controller 재spawn → 소유 전환."""
        occupant = self._port_pid(target.port)  # precheck 에서 not None 확인됨
        self._launcher.signal(occupant, _signal_mod.SIGTERM)  # 미소유 정지(HIGH 승인으로 예외)
        self._await_free(target)  # 포트 해제 대기(cutover bind 충돌 방지)
        pid = self._spawn_and_own(target)  # 직접 spawn → (pid, starttime) 자기 기록
        if not self._await_listen(target):
            raise _LifecyclePartialFailure("adopt(cutover) 실패: 재기동 후 LISTEN 안 됨")
        return ({"action": "adopt", "old_pid": occupant, "pid": pid}, pid)

    # ── 게이트 helpers ──────────────────────────────────────────────────────
    def _lock_for(self, name: str) -> threading.Lock:
        with self._locks_guard:
            lk = self._locks.get(name)
            if lk is None:
                lk = threading.Lock()
                self._locks[name] = lk
            return lk

    def _rate_ok(self, name: str) -> bool:
        # CC-5 (C-3 자율완화 합의): rate 는 *executed* lifecycle 빈도만 센다(_rate_record 는
        # 집행 성공 시에만 — referred/crash-loop 미집계). 따라서 rate 는 crash-loop 를 *직접*
        # 잡지 않는다. propose 폭주의 1차 방어 = 1-클릭 게이트(C-2). rate 는 "성공 재기동 연타"
        # 2차 방어선. crash-loop 자체는 CB-9 동시1 + 누적(ledger 파생)이 막는다.
        now = self._now()
        window = [t for t in self._rate.get(name, []) if now - t < self._rate_window]
        self._rate[name] = window
        return len(window) < self._rate_limit

    def _rate_record(self, name: str) -> None:
        self._rate.setdefault(name, []).append(self._now())

    def _approve(self, action: Action, target: ControlTarget, grade: Grade) -> bool:
        if self._approver is None:
            return False  # L-6 default-deny
        try:
            req = {
                "action": action.name, "target": target.name, "grade": grade.name,
                "port": target.port, "owned": self._owned.get(target.name),
            }
            return bool(self._approver(req))
        except Exception:
            return False  # L-6 fail-closed

    def _audit_intent(self, action: Action, target: ControlTarget, grade: Grade) -> None:
        """집행 전 intent 감사(CB-4). audit 이 raise 하면 _gated_lifecycle 가 referred(fail-closed).

        audit None = 무감사(테스트/개발). production server 는 fail-closed audit 배선 필수(정직 단서).
        """
        if self._audit is None:
            return
        self._audit(ControlDecision(action.name, target.name, grade, "intent", None, "lifecycle intent"))

    def _execute(self, action: Action, target: ControlTarget) -> Any:
        """등급 검증 통과 후에만 도달(B-1). 1a probe 자율 집행."""
        if Capability.PROBE in action.capabilities:
            return self._prober(target)
        return None  # 도달 불가(비-저위험은 _decide 가 lock 분기로 보냄)


def _refer(action: Action, name: str, grade: Grade, reason: str,
           pid: Optional[int] = None) -> ControlDecision:
    """사람 회부(referred) 결정 생성 — 미소유·재사용·C-3 초과·부분 실패."""
    return ControlDecision(action.name, name, grade, "referred", None, reason, pid=pid)
