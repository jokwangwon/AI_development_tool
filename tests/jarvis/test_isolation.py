"""IsolationBackend — 워커 격리 backend 주입 인터페이스 테스트.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §5 v3-1/v4-4
  - 격리 = 교체 가능 의존성. 트랙 A = Passthrough(no-op), 트랙 B = Landlock(V-2
    실증 ll_sandbox path_beneath 패턴) 으로 *교체*.
  - 트랙 A 인터페이스가 격리 backend 를 주입받도록 설계.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from src.jarvis.isolation import (
    _DEFAULT_SANDBOX_BIN,
    IsolationBackend,
    LandlockIsolation,
    PassthroughIsolation,
)

# 통합 테스트(실제 격리 동작)는 빌드된 ll_sandbox 가 있을 때만. 없으면 skip
# (CI 등 미빌드 환경 — 바이너리는 gitignore, `make -C src/jarvis/sandbox` 로 생성).
_sandbox_built = os.path.isfile(_DEFAULT_SANDBOX_BIN) and os.access(
    _DEFAULT_SANDBOX_BIN, os.X_OK
)


def _fake_sandbox_bin(tmp_path: Path) -> str:
    """실행 가능한 가짜 ll_sandbox — wrap() 조립 단위 테스트용(실제 실행 안 함)."""
    p = tmp_path / "ll_sandbox"
    p.write_text("#!/bin/sh\nexit 0\n")
    p.chmod(0o755)
    return str(p)


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


# --- 트랙 B: LandlockIsolation (V-2 실증 ll_sandbox path_beneath 패턴) ---


def test_landlock_satisfies_protocol(tmp_path: Path) -> None:
    # 트랙 B 는 트랙 A 와 동일 인터페이스로 *교체* — 프로토콜 충족 필수
    iso: IsolationBackend = LandlockIsolation(sandbox_bin=_fake_sandbox_bin(tmp_path))
    assert callable(iso.wrap)


def test_landlock_name() -> None:
    # 감사/로그용 — 어떤 격리가 적용됐는지 passthrough 와 구별 가능해야
    assert LandlockIsolation(sandbox_bin="/nonexistent").name == "landlock"


def test_landlock_wraps_cmd_via_sandbox(tmp_path: Path) -> None:
    # wrap = [ll_sandbox, workdir(RW), *ro_paths, "--", *cmd] (ll_sandbox 사용규약)
    sb = _fake_sandbox_bin(tmp_path)
    iso = LandlockIsolation(sandbox_bin=sb, ro_paths=["/usr"])
    out = iso.wrap(["claude", "-p", "hi"], workdir=str(tmp_path))
    assert out == [sb, str(tmp_path), "/usr", "--", "claude", "-p", "hi"]


def test_landlock_workdir_is_rw_first_arg(tmp_path: Path) -> None:
    # ll_sandbox 첫 디렉터리 = RW. 워커당 작업디렉터리만 read/write(§6 B-2/B-6)
    sb = _fake_sandbox_bin(tmp_path)
    iso = LandlockIsolation(sandbox_bin=sb, ro_paths=["/usr"])
    out = iso.wrap(["x"], workdir=str(tmp_path))
    assert out[0] == sb
    assert out[1] == str(tmp_path)  # 첫 디렉터리 = RW = workdir


def test_landlock_separator_before_cmd(tmp_path: Path) -> None:
    # "--" 가 디렉터리 목록과 실행 명령을 분리 — cmd 는 separator 뒤
    sb = _fake_sandbox_bin(tmp_path)
    iso = LandlockIsolation(sandbox_bin=sb, ro_paths=["/usr", "/lib"])
    out = iso.wrap(["claude", "-p"], workdir=str(tmp_path))
    sep = out.index("--")
    assert out[sep + 1 :] == ["claude", "-p"]
    assert "/usr" in out[:sep] and "/lib" in out[:sep]


def test_landlock_does_not_mutate_input(tmp_path: Path) -> None:
    sb = _fake_sandbox_bin(tmp_path)
    iso = LandlockIsolation(sandbox_bin=sb, ro_paths=["/usr"])
    cmd = ["claude", "-p"]
    out = iso.wrap(cmd, workdir=str(tmp_path))
    out.append("MUTATED")
    assert cmd == ["claude", "-p"]  # 원본 불변


def test_landlock_fail_closed_when_binary_missing(tmp_path: Path) -> None:
    # default-deny(P-PRIV): sandboxer 없으면 *거부*. passthrough fallback 금지
    # (격리 불가 시 비격리 실행은 보안 무력화 = 거짓 안전감)
    iso = LandlockIsolation(sandbox_bin=str(tmp_path / "does-not-exist"))
    with pytest.raises(RuntimeError):
        iso.wrap(["claude", "-p"], workdir=str(tmp_path))


def test_landlock_filters_nonexistent_ro_paths(tmp_path: Path) -> None:
    # 존재하지 않는 RO 경로는 제외 — ll_sandbox open(O_PATH) 실패로 전체 거부되는 것 방지.
    # RO 누락은 더 *제한적*(워커가 못 읽음)이라 보안 약화 아님. RW workdir 는 항상 유지.
    sb = _fake_sandbox_bin(tmp_path)
    iso = LandlockIsolation(sandbox_bin=sb, ro_paths=["/usr", "/no/such/dir-xyz"])
    out = iso.wrap(["x"], workdir=str(tmp_path))
    assert "/no/such/dir-xyz" not in out
    assert "/usr" in out


def test_landlock_default_ro_paths_are_system_dirs() -> None:
    # 기본 RO = 워커 바이너리 실행에 필요한 시스템 경로(workdir 만으론 워커 자체를 못 읽음)
    assert "/usr" in LandlockIsolation.DEFAULT_RO_PATHS
    assert all(os.path.isabs(p) for p in LandlockIsolation.DEFAULT_RO_PATHS)


# --- 통합: 실제 ll_sandbox 로 커널 강제 격리 동작 (증명 ⑤, V-2 V2-3 재현) ---


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_landlock_allows_write_inside_workdir(tmp_path: Path) -> None:
    # workdir = RW: 워커가 작업디렉터리 안에는 쓸 수 있어야(정상 작업 가능)
    workdir = tmp_path / "ws"
    workdir.mkdir()
    target = workdir / "inside.txt"
    iso = LandlockIsolation()  # 실제 빌드된 바이너리
    cmd = iso.wrap(["sh", "-c", f"echo ok > {target}"], workdir=str(workdir))
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    assert target.read_text().strip() == "ok"


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_landlock_blocks_write_outside_workdir(tmp_path: Path) -> None:
    # 커널 강제: workdir 밖 쓰기는 차단(deny-by-default). 워커 침해와 무관(V-F2).
    workdir = tmp_path / "ws"
    workdir.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    pwned = outside / "PWNED.txt"
    iso = LandlockIsolation()
    # workdir 밖 절대경로로 쓰기 시도 → Landlock 이 차단해야 함
    cmd = iso.wrap(
        ["sh", "-c", f"echo pwn > {pwned} 2>/dev/null; true"], workdir=str(workdir)
    )
    subprocess.run(cmd, capture_output=True, text=True)
    assert not pwned.exists()  # 격리 입증: workdir 밖 쓰기 차단
