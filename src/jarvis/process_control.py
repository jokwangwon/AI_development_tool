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
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Optional

from src.jarvis.external_registry import JARVIS_ORIGIN  # B-2 provenance 상속(단일 출처)

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


class Grade(Enum):
    """리스크 등급(§3.5). 값은 max 비교용 순서."""

    LOW = 1     # 가역·저위험 → 자율 집행
    MEDIUM = 2  # 중 → 게이트(초기 1-클릭, slice-1b)
    HIGH = 3    # 비가역/미상 → 사람 승인(fail-closed 기본값)


# capability → 등급 코어 고정 매핑(G6(a), X-3). 미등재 capability = 고위험 fail-closed.
_CAP_GRADE = {
    Capability.PROBE: Grade.LOW,
    Capability.SPAWN: Grade.MEDIUM,
    Capability.SIGNAL: Grade.MEDIUM,
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


# 코어 고정 allowlist(미등재 = 고위험 fail-closed). slice-1a = health(probe)만.
# lifecycle(start/stop/restart = spawn/signal = 중위험)은 slice-1b 에서 추가.
CONTROL_ACTIONS: dict[str, Action] = {
    "health": Action("health", frozenset({Capability.PROBE})),
}


@dataclass(frozen=True)
class ControlTarget:
    """검증된 제어 대상(불변). 자비스가 도와 만든 로컬 프로세스 한정(B-2/B-4)."""

    name: str
    host: str
    port: int
    origin: str = ""
    health_path: str = ""


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
    """propose 결정(감사·반환). outcome ∈ {executed, rejected}. (gated 경로는 slice-1b)"""

    action: str
    target_name: str
    grade: Grade
    outcome: str
    result: Any = None
    reason: str = ""


class ProcessController:
    """제어 동작 결정적 집행자(B-1 seam). boss 는 propose() 만 호출.

    propose 흐름: provenance/localhost 검증(B-2/B-4) → 코어 allowlist 조회(미등재=고 fail-closed)
    → capability 등급(B-5) → 저위험만 자율 집행, 그 외 거부(게이트는 slice-1b). 자격증명 0(B-6).
    """

    def __init__(
        self,
        actions: Optional[dict] = None,
        prober: Optional[Callable[[ControlTarget], ProbeStatus]] = None,
        audit: Optional[Callable[[ControlDecision], None]] = None,
    ) -> None:
        self._actions = dict(CONTROL_ACTIONS if actions is None else actions)
        self._prober = prober if prober is not None else probe_target
        self._audit = audit

    def propose(self, action_name: str, target: ControlTarget) -> ControlDecision:
        """boss-facing 단일 진입점. 결정 후 감사 기록(GP-7)."""
        decision = self._decide(action_name, target)
        if self._audit is not None:
            self._audit(decision)
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
            result = self._execute(action, target)
            return ControlDecision(action_name, tname, grade, "executed", result, "low-grade auto")

        # 비-저위험: slice-1a 엔 게이트/집행 경로 없음 → fail-closed 거부(게이트 = slice-1b)
        return ControlDecision(action_name, tname, grade, "rejected", None,
                               f"grade {grade.name} requires approval gate (slice-1b)")

    def _execute(self, action: Action, target: ControlTarget) -> Any:
        """등급 검증 통과 후에만 도달(B-1). capability 별 dispatch — 1a 는 probe 만."""
        if Capability.PROBE in action.capabilities:
            return self._prober(target)
        return None  # 1a 미구현 capability(도달 불가 — 비-저위험은 _decide 가 먼저 거부)
