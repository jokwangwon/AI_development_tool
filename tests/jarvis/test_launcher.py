"""Jarvis 제어측 slice-1b — Launcher (CB-3): non-blocking spawn + killpg signal + starttime.

답습:
  docs/phase0/jarvis-control-side-slice1b-lifecycle-brief.md (CB-3)
  docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1b.md (GP-A1·GP-C3·CB-1)

CB-3: lifecycle long-lived 프로세스는 기존 blocking `subprocess.run`(worker.py, run-to-completion)
재사용 금지. `spawn(argv,cwd,env)->pid`(non-blocking Popen + start_new_session=setsid) /
`signal(pid,sig)`(os.killpg = 프로세스 그룹 종료, 손자 회수) 분리.
CB-1: 소유권 키 = (pid, starttime). read_starttime = /proc/<pid>/stat field 22.
"""
from __future__ import annotations

import os
import signal as _signal

import pytest

from src.jarvis.launcher import (
    Launcher,
    SubprocessLauncher,
    find_listener_pid,
    read_starttime,
)


# ── SubprocessLauncher.spawn = non-blocking + setsid (CB-3) ────────────────
def test_spawn_is_non_blocking_and_returns_pid():
    """spawn은 Popen으로 즉시 pid 반환 — run-to-completion 블로킹 금지(CB-3)."""
    captured = {}

    class FakePopen:
        def __init__(self, argv, cwd=None, env=None, start_new_session=False, **kw):
            captured["argv"] = argv
            captured["cwd"] = cwd
            captured["start_new_session"] = start_new_session
            self.pid = 4242

    launcher = SubprocessLauncher(popen=FakePopen)
    pid = launcher.spawn(["python", "server.py"], cwd="/tmp/x", env={"A": "1"})
    assert pid == 4242
    assert captured["argv"] == ["python", "server.py"]
    assert captured["cwd"] == "/tmp/x"
    # setsid: 본체 종료 시 고아화 방지 + killpg 대상 그룹 분리(GP-C3)
    assert captured["start_new_session"] is True


def test_spawn_uses_argv_list_not_shell():
    """L-8: argv 리스트(쉘 문자열 금지). Popen에 문자열 아닌 리스트 전달."""
    seen = {}

    class FakePopen:
        def __init__(self, argv, **kw):
            seen["argv"] = argv
            self.pid = 1

    SubprocessLauncher(popen=FakePopen).spawn(["a", "b c"], cwd="/", env=None)
    assert isinstance(seen["argv"], list)
    assert seen["argv"] == ["a", "b c"]


# ── SubprocessLauncher.signal = killpg (프로세스 그룹 종료, GP-C3) ──────────
def test_signal_uses_killpg_on_process_group():
    """종료 = os.killpg(getpgid(pid)) — setsid는 detach지 회수 아님. 손자까지 회수(GP-C3)."""
    calls = []
    launcher = SubprocessLauncher(
        getpgid=lambda pid: pid + 1000,
        killpg=lambda pgid, sig: calls.append((pgid, sig)),
    )
    launcher.signal(55, _signal.SIGTERM)
    assert calls == [(1055, _signal.SIGTERM)]


def test_signal_refuses_own_process_group():
    """⭐ 자살 방지(dogfood 발견): 대상 pgid == controller 자기 그룹이면 killpg 거부."""
    calls = []
    launcher = SubprocessLauncher(
        getpgid=lambda pid: 555,  # occupant pgid == 자기(getpgid(0)) pgid
        killpg=lambda pg, s: calls.append((pg, s)),
    )
    launcher.signal(999, _signal.SIGTERM)
    assert calls == []  # 자기 그룹 = 거부(자비스 본체 보호)


def test_signal_kills_independent_group():
    """setsid 로 독립 그룹인 정상 spawn 프로세스는 종료 가능(가드 안 걸림)."""
    calls = []
    launcher = SubprocessLauncher(
        getpgid=lambda pid: 0 if pid == 0 else 777,  # 자기=0, occupant=777 독립
        killpg=lambda pg, s: calls.append((pg, s)),
    )
    launcher.signal(42, _signal.SIGTERM)
    assert calls == [(777, _signal.SIGTERM)]


def test_signal_missing_process_is_swallowed():
    """이미 죽은 프로세스 signal = ProcessLookupError 흡수(crash 아님)."""
    def boom_pgid(pid):
        raise ProcessLookupError()
    launcher = SubprocessLauncher(getpgid=boom_pgid, killpg=lambda p, s: None)
    # 예외 전파 없이 조용히 처리
    launcher.signal(99999, _signal.SIGTERM)


# ── read_starttime: /proc/<pid>/stat field 22 (CB-1 PID recycling 키) ──────
def test_read_starttime_parses_field_22(tmp_path):
    """starttime = /proc/<pid>/stat 22번째 필드. comm(괄호, 공백 포함)은 rsplit(')')로 회피."""
    proc_root = tmp_path
    pid_dir = proc_root / "1234"
    pid_dir.mkdir()
    # comm = "(my server)" 공백·괄호 포함 — 파서가 마지막 ')' 이후로 split해야 안전.
    # field: 1=pid 2=comm 3=state ... 22=starttime. comm 뒤 첫 토큰(state)=index0.
    fields_after_comm = ["S"] + [str(i) for i in range(2, 22)]  # state + 19개 → starttime=index19
    fields_after_comm[19] = "987654"  # field 22
    stat = f"1234 (my server) {' '.join(fields_after_comm)}"
    (pid_dir / "stat").write_text(stat)
    assert read_starttime(1234, proc_root=str(proc_root)) == 987654


def test_read_starttime_missing_pid_returns_none(tmp_path):
    """프로세스 부재(/proc/<pid> 없음) = None(죽음/미상)."""
    assert read_starttime(999999, proc_root=str(tmp_path)) is None


def test_read_starttime_malformed_returns_none(tmp_path):
    pid_dir = tmp_path / "5"
    pid_dir.mkdir()
    (pid_dir / "stat").write_text("garbage no parens")
    assert read_starttime(5, proc_root=str(tmp_path)) is None


# ── find_listener_pid: /proc/net/tcp inode → pid (AC-4, CB-9/adopt) ────────
def _write_proc_listener(proc_root, port, inode, pid):
    (proc_root / "net").mkdir(parents=True, exist_ok=True)
    hexport = format(port, "04X")
    # 실 /proc/net/tcp 포맷: inode = parts[9] (sl local rem st tx:rx tr:tm retrnsmt uid timeout inode)
    (proc_root / "net" / "tcp").write_text(
        "  sl  local_address rem_address   st ...\n"
        f"   0: 0100007F:{hexport} 00000000:0000 0A 00000000:00000000 00:00000000 00000000 1000 0 {inode} 1 x\n"
    )
    (proc_root / "net" / "tcp6").write_text("  sl  local_address ...\n")
    fd = proc_root / str(pid) / "fd"
    fd.mkdir(parents=True)
    os.symlink(f"socket:[{inode}]", fd / "3")


def test_find_listener_pid_maps_port_to_pid(tmp_path):
    _write_proc_listener(tmp_path, port=8777, inode="918273", pid=502419)
    assert find_listener_pid(8777, proc_root=str(tmp_path)) == 502419


def test_find_listener_pid_none_when_port_free(tmp_path):
    _write_proc_listener(tmp_path, port=8777, inode="918273", pid=502419)
    assert find_listener_pid(9999, proc_root=str(tmp_path)) is None


def test_find_listener_pid_ignores_non_listen_state(tmp_path):
    """ESTABLISHED(01) 등 비-LISTEN 은 무시(st != 0A)."""
    (tmp_path / "net").mkdir()
    hexport = format(8777, "04X")
    (tmp_path / "net" / "tcp").write_text(
        "  sl  local_address ...\n"
        f"   0: 0100007F:{hexport} 0100007F:1234 01 00000000:00000000 00:00000000 00000000 1000 0 5 1 x\n"
    )
    assert find_listener_pid(8777, proc_root=str(tmp_path)) is None


# ── Launcher Protocol = spawn/signal 두 연산만 (계약 명세) ──────────────────
def test_launcher_protocol_surface():
    """Launcher는 spawn/signal 두 연산. 주입형 = hermetic 테스트 seam."""
    assert hasattr(SubprocessLauncher, "spawn")
    assert hasattr(SubprocessLauncher, "signal")
    # 실 spawn 없이 가짜 주입 가능(테스트가 실 프로세스 안 띄움)
    fake = SubprocessLauncher(popen=lambda *a, **k: type("P", (), {"pid": 7})())
    assert fake.spawn(["x"], cwd="/", env=None) == 7
