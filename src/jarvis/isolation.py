"""IsolationBackend — 워커 격리 backend (주입 가능 의존성).

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §5/§6
  - 트랙 A = PassthroughIsolation(격리-직교 골격, no-op): 워커는 작업디렉터리
    (git worktree 분리)에서 비격리 실행.
  - 트랙 B = LandlockIsolation(별도, V-2 실증 ll_sandbox path_beneath 패턴):
    트랙 A 의 작업디렉터리 실행을 격리 실행으로 *교체*. 본 모듈에 추가 예정.
  - V-2: Landlock 단독 충분(무권한), 외부 강제(커널) = 워커 침해 무관.

워커 격리는 MVP 첫 실행 전제(§6 B-2/B-6)이나, 트랙 A 는 격리 backend 를
교체 가능하게 두어 V-2 통합(트랙 B) 전에도 배관/headless 골격을 TDD 가능.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class IsolationBackend(Protocol):
    """워커 명령을 격리 실행 명령으로 감싸는 backend.

    wrap() 은 원본 cmd 를 변형하지 않고 *새* 명령 리스트를 반환한다.
    """

    name: str

    def wrap(self, cmd: list[str], workdir: str) -> list[str]:
        ...


class PassthroughIsolation:
    """트랙 A no-op 격리 — 명령을 그대로 통과(격리 미적용).

    트랙 B(Landlock) 통합 전 골격 검증용. 워커는 workdir 에서 비격리 실행되며,
    격리 책임은 호출측의 작업디렉터리 분리(git worktree)에 한정된다.
    """

    name = "passthrough"

    def wrap(self, cmd: list[str], workdir: str) -> list[str]:
        return list(cmd)
