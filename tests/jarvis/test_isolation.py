"""IsolationBackend — 워커 격리 backend 주입 인터페이스 테스트.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §5 v3-1/v4-4
  - 격리 = 교체 가능 의존성. 트랙 A = Passthrough(no-op), 트랙 B = Landlock(V-2
    실증 ll_sandbox path_beneath 패턴) 으로 *교체*.
  - 트랙 A 인터페이스가 격리 backend 를 주입받도록 설계.
"""
from __future__ import annotations

from src.jarvis.isolation import IsolationBackend, PassthroughIsolation


def test_passthrough_returns_cmd_unchanged() -> None:
    iso = PassthroughIsolation()
    cmd = ["claude", "-p", "--output-format", "json"]
    assert iso.wrap(cmd, workdir="/tmp/ws") == cmd


def test_passthrough_does_not_mutate_input() -> None:
    iso = PassthroughIsolation()
    cmd = ["claude", "-p"]
    out = iso.wrap(cmd, workdir="/tmp/ws")
    out.append("MUTATED")
    assert cmd == ["claude", "-p"]  # 원본 불변


def test_passthrough_satisfies_protocol() -> None:
    # 주입 가능 의존성: PassthroughIsolation 은 IsolationBackend 프로토콜 충족
    iso: IsolationBackend = PassthroughIsolation()
    assert callable(iso.wrap)


def test_passthrough_name() -> None:
    # 감사/로그용 식별자 — 어떤 격리가 적용됐는지 결과에 기록 가능해야
    assert PassthroughIsolation().name == "passthrough"
