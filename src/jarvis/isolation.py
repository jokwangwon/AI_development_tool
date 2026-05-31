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

import os
import stat
from typing import Protocol, runtime_checkable


def _safe_rw_device(path: str) -> str | None:
    """디딤돌1h CL-4 — RW 노출 후보 디바이스 파일을 결정적 검증.

    무해 캐릭터 디바이스(`/dev/null` 등)만 RW 노출 허용. 위험 디바이스/우회 경로
    차단(합의 CL-4, [[3plus1-consensus-2026-05-31-jarvis-stone1h-execution-isolation]]):
      - `os.path.islink` 거부: `/dev/stdin`→`/proc/self/fd` 류 심링크 우회 차단.
      - `realpath` 후 `/dev/` prefix 강제: /dev 밖 경로 차단.
      - `stat.S_ISCHR` 만 허용: 블록 디바이스(`/dev/sda` = S_ISBLK)·일반 파일 거부.
    통과 시 검증된 경로 반환, 아니면 None(호출측이 드롭). ll_sandbox.c 가 2차 방어.
    """
    if os.path.islink(path):
        return None
    try:
        real = os.path.realpath(path)
        st = os.stat(real)
    except OSError:
        return None
    if not real.startswith("/dev/"):
        return None
    if not stat.S_ISCHR(st.st_mode):
        return None
    return real


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


# ll_sandbox 기본 경로 = 이 모듈 옆 sandbox/ll_sandbox (make 로 빌드, gitignore).
_DEFAULT_SANDBOX_BIN = os.path.join(os.path.dirname(__file__), "sandbox", "ll_sandbox")


class LandlockIsolation:
    """트랙 B 격리 — 워커 명령을 검증된 ``ll_sandbox`` (Landlock) 로 감싼다.

    답습: docs/phase0/jarvis-safety-layer-poc-findings.md §6 (V-2 실증, ABI 7)
      - ``ll_sandbox`` 사용규약: ``<rw_dir> [ro_dir...] -- <cmd> [args]``.
        첫 디렉터리 = read/write(워커당 작업디렉터리), 나머지 = read-only,
        그 외 fs 는 deny-by-default. 커널 강제 = 워커 침해 무관(V-F2).
      - 검증된 격리 = fs 한정(V-F4). net egress 미차단 = MVP-1+ 후속(ABI4).

    fail-closed(P-PRIV default-deny): sandboxer 가 없으면 *거부*한다. 격리 불가
    시 비격리 실행으로 fallback 하지 않는다(거짓 안전감 = 보안 무력화 금지).
    """

    name = "landlock"

    # 워커 바이너리(claude 등) 실행에 필요한 시스템 경로 — read-only 노출.
    # 작업디렉터리(RW)만으론 워커 실행 파일·런타임·인증서를 읽지 못한다.
    DEFAULT_RO_PATHS: tuple[str, ...] = (
        "/usr",
        "/lib",
        "/lib64",
        "/bin",
        "/sbin",
        "/etc",
    )

    def __init__(
        self,
        sandbox_bin: str | None = None,
        ro_paths: list[str] | tuple[str, ...] | None = None,
        rw_root: str | None = None,
        rw_files: list[str] | tuple[str, ...] | None = None,
    ) -> None:
        self._bin = sandbox_bin or _DEFAULT_SANDBOX_BIN
        self._ro_paths = (
            tuple(ro_paths) if ro_paths is not None else self.DEFAULT_RO_PATHS
        )
        # rw_root(BL-4): RW 루트를 명시 고정(가짜 홈). 미지정 시 workdir(하위호환).
        # 가짜 홈 격리 = 작업폴더를 가짜 홈 하위에 nest, 단일 RW 루트(가짜홈)로 커버.
        # 답습: docs/phase0/jarvis-claude-landlock-fakehome-design-brief.md §1 (Q1a).
        self._rw_root = rw_root
        # rw_files(디딤돌1h CL-2): 무해 캐릭터 디바이스(/dev/null 등) 단일 파일 RW.
        # ro_paths(디렉터리)와 *명시 분리* — "RO 목록의 파일이 자동 RW" silent 권한
        # 상승 차단. wrap 이 _safe_rw_device(CL-4)로 재검증한 항목만 노출.
        self._rw_files = tuple(rw_files) if rw_files is not None else ()

    def wrap(self, cmd: list[str], workdir: str) -> list[str]:
        if not (os.path.isfile(self._bin) and os.access(self._bin, os.X_OK)):
            raise RuntimeError(
                f"Landlock sandboxer 없음/실행 불가: {self._bin!r}. "
                "make -C src/jarvis/sandbox 로 빌드 필요. "
                "(fail-closed: 격리 불가 시 비격리 실행 금지)"
            )
        # 존재하는 RO 경로만 — 없는 경로는 ll_sandbox open(O_PATH) 실패로 전체
        # 거부되므로 제외. RO 누락은 더 제한적이라 안전 약화 아님(RW root 는 유지).
        # ro 는 *디렉터리만*(isdir) — 파일은 rw_files 명시 경로로만(CL-2 함정 차단).
        ro = [p for p in self._ro_paths if os.path.isdir(p)]
        # rw_files: CL-4 검증 통과한 무해 디바이스만(심링크/비-/dev/블록 디바이스 드롭).
        rwf = [d for p in self._rw_files if (d := _safe_rw_device(p)) is not None]
        rw = self._rw_root or workdir
        # ll_sandbox: 첫 인자=RW 루트, 이후 디렉터리=RO·파일=RW 파일 mask(stat 분기).
        return [self._bin, rw, *ro, *rwf, "--", *cmd]
