"""Jarvis 제어측 slice-1b — Launcher (CB-3): 프로세스 lifecycle 집행 백엔드.

답습:
  docs/phase0/jarvis-control-side-slice1b-lifecycle-brief.md (CB-3, L-3, L-8)
  docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1b.md (GP-A1·GP-C3·CB-1)

설계 (합의 BLOCKING):
  - **CB-3 non-blocking spawn**: lifecycle long-lived 서버는 기존 worker.py 의 blocking
    `subprocess.run`(run-to-completion) 과 본질이 다르다. `spawn` 은 `Popen` 으로 *즉시*
    pid 를 반환(블로킹 0). `start_new_session=True`(setsid) 로 새 세션·프로세스 그룹을
    부여해 (a) 본체 종료 시 고아화 방지 (b) killpg 종료 대상 그룹 분리.
  - **CB-3 / GP-C3 killpg 종료**: setsid 는 detach 일 뿐 *회수* 가 아니다. 종료는
    `os.killpg(getpgid(pid), sig)` 로 프로세스 *그룹* 전체에 signal — GPT-SoVITS 가 띄우는
    손자 워커까지 회수(단일 `kill(pid)` 는 손자 누수).
  - **CB-1 소유권 키**: `read_starttime` = `/proc/<pid>/stat` 22번째 필드(부팅 후 clock
    ticks). 소유권 = `(pid, starttime)` — PID 재사용(같은 번호 다른 프로세스) 결정적 구별.
  - **L-8 argv**: spawn 은 argv *리스트* 만(쉘 문자열 금지, `shell=False` 가 Popen 기본).

이 모듈은 **leaf**(부작용 = 주입형 popen/killpg). 등급·게이트·소유권 판정은 호출측
(ProcessController) 책무 — launcher 는 "어떻게 띄우고 죽이는가"의 결정적 수단만 제공.
start 성공 *판정*(LISTEN probe)도 controller 가 조율(launcher 는 spawn 만).
"""
from __future__ import annotations

import os
import subprocess
from typing import Callable, Optional, Protocol


class Launcher(Protocol):
    """프로세스 lifecycle 집행 백엔드 계약 — spawn/signal 두 원시 연산.

    주입형(SubprocessLauncher 기본, systemd-run 등 교체 가능 — Provider Liquidity).
    백엔드 주입은 registry/코어만(boss 불가): boss 가 launcher 를 갈아끼우면 공격 표면.
    """

    def spawn(self, argv: list[str], cwd: Optional[str], env: Optional[dict]) -> int:
        """argv(쉘 미경유) 프로세스를 non-blocking 기동 → pid 반환."""
        ...

    def signal(self, pid: int, sig: int) -> None:
        """pid 의 프로세스 *그룹* 에 signal(killpg). 부재 = 조용히 무시."""
        ...


class SubprocessLauncher:
    """기본 Launcher — `subprocess.Popen` + setsid / `os.killpg`.

    popen/killpg/getpgid 주입 = hermetic 테스트 seam(실 프로세스 안 띄우고 검증).
    """

    def __init__(
        self,
        popen: Callable[..., object] = subprocess.Popen,
        killpg: Callable[[int, int], None] = os.killpg,
        getpgid: Callable[[int], int] = os.getpgid,
    ) -> None:
        self._popen = popen
        self._killpg = killpg
        self._getpgid = getpgid

    def spawn(self, argv: list[str], cwd: Optional[str], env: Optional[dict]) -> int:
        """non-blocking spawn(CB-3). setsid 새 세션 → 고아화 방지 + killpg 그룹 분리.

        stdout/stderr 는 DEVNULL 로 분리(본체 파이프 점유·역류 방지). 반환 즉시 detach —
        completion 을 기다리지 않는다(서버는 끝나지 않음).
        """
        proc = self._popen(
            argv,
            cwd=cwd,
            env=env,
            start_new_session=True,  # setsid: 새 세션/프로세스 그룹(GP-C3)
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )
        return int(proc.pid)

    def signal(self, pid: int, sig: int) -> None:
        """프로세스 그룹 종료(GP-C3). 이미 죽은 프로세스 = 조용히 무시(crash 아님).

        ⭐ 자살 방지(slice-1b dogfood 발견): 대상 pgid 가 controller *자기* 그룹과 같으면
        거부 — killpg 가 자비스 본체/HUD 를 죽이는 사고 차단. controller 가 정상 spawn 한
        프로세스는 setsid 로 독립 그룹이라 가드에 안 걸린다(정상 stop 가능).
        """
        try:
            pgid = self._getpgid(pid)
            if pgid == self._getpgid(0):  # 자기 프로세스 그룹 = 자살 방지
                return
            self._killpg(pgid, sig)
        except (ProcessLookupError, PermissionError, OSError):
            # 부재/권한 = 무시(L-7 자동 롤백 없음 — 판정은 controller 의 starttime 재대조)
            return


def find_listener_pid(port: int, *, proc_root: str = "/proc") -> Optional[int]:
    """포트를 LISTEN 하는 PID 역추적 (AC-4: `/proc/net/tcp` inode = 커널 사실, cmdline 보다 강함).

    동시 1인스턴스(CB-9)·adopt(미소유 점유 PID) 판정에 사용. 외부명령(ss/lsof) 없이
    `/proc` 직접 읽기(argv injection 표면 0). 다른 UID 소유 포트는 inode→pid 매칭 실패 =
    None(자연 fail-closed — same-UID 프로세스만 제어 대상). 부재/파싱 실패 = None.
    """
    inodes = _listening_inodes(port, proc_root)
    if not inodes:
        return None
    return _pid_for_inodes(inodes, proc_root)


def _listening_inodes(port: int, proc_root: str) -> set:
    """LISTEN(st=0A) + local port 일치 소켓의 inode 집합 (tcp + tcp6)."""
    out: set = set()
    for net in ("tcp", "tcp6"):
        try:
            with open(f"{proc_root}/net/{net}", encoding="utf-8") as fh:
                lines = fh.read().splitlines()[1:]  # 헤더 1줄 skip
        except OSError:
            continue
        for line in lines:
            parts = line.split()
            if len(parts) < 10 or parts[3] != "0A":  # 0A = TCP_LISTEN
                continue
            try:
                local_port = int(parts[1].rsplit(":", 1)[1], 16)
            except (ValueError, IndexError):
                continue
            if local_port == port:
                out.add(parts[9])  # inode
    return out


def _pid_for_inodes(inodes: set, proc_root: str) -> Optional[int]:
    """소켓 inode 를 fd 로 가진 PID 검색 (/proc/<pid>/fd → socket:[inode] symlink)."""
    targets = {f"socket:[{i}]" for i in inodes}
    try:
        entries = os.listdir(proc_root)
    except OSError:
        return None
    for entry in entries:
        if not entry.isdigit():
            continue
        fd_dir = f"{proc_root}/{entry}/fd"
        try:
            for fd in os.listdir(fd_dir):
                try:
                    if os.readlink(f"{fd_dir}/{fd}") in targets:
                        return int(entry)
                except OSError:
                    continue
        except OSError:
            continue  # 권한 없는 PID(다른 UID) = skip
    return None


def read_starttime(pid: int, *, proc_root: str = "/proc") -> Optional[int]:
    """`/proc/<pid>/stat` 의 starttime(field 22, 부팅 후 clock ticks). 부재/파싱 실패 = None.

    CB-1: `(pid, starttime)` 소유권 키의 starttime. comm(field 2)은 괄호로 감싸지고 공백·
    괄호를 포함할 수 있어 마지막 ')' 이후를 split — comm 뒤 첫 토큰(state)=index 0,
    starttime(field 22)=index 19.
    """
    try:
        with open(f"{proc_root}/{pid}/stat", encoding="utf-8") as fh:
            data = fh.read()
        after_comm = data.rsplit(")", 1)[1].split()
        return int(after_comm[19])
    except (OSError, ValueError, IndexError):
        return None
