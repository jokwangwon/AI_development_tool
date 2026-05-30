"""claude code 워커 가짜 홈 격리 (레벨 2) 트랙 A 테스트.

답습: docs/phase0/jarvis-claude-landlock-fakehome-design-brief.md (v1.1, BLOCKING 6)
  - BL-1 env allowlist: claude_runner 가 {**os.environ} 전체 상속 → 명시 allowlist.
  - BL-4 rw_root: LandlockIsolation 의 RW 루트를 가짜홈으로(작업폴더 nest).
  - BL-5 시드 신뢰경계: 가짜홈 0700 + credential 0600 + symlink 방어 + realpath.
  - BL-6 fail-closed: credential 무효/누락 시 raise.

트랙 A — 실 claude·실 토큰 0건(더미 src + 주입형 runner). 우회 음성테스트(F/G/H)는
test_isolation 의 sandbox-built gated 통합 테스트로 별도(실 ll_sandbox 필요).
"""
from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from src.jarvis.isolation import _DEFAULT_SANDBOX_BIN, LandlockIsolation
from src.jarvis.worker_setup import (
    CLAUDE_RO_PATHS,
    _build_claude_env,
    _make_claude_runner,
    provision_claude_home,
)

# 우회 음성테스트(F/G/H)는 실 ll_sandbox 커널 강제 동작이 필요 → 미빌드 시 skip.
_sandbox_built = os.path.isfile(_DEFAULT_SANDBOX_BIN) and os.access(
    _DEFAULT_SANDBOX_BIN, os.X_OK
)


# --- BL-1: env allowlist (_build_claude_env 순수 함수) ---


def test_env_allowlist_drops_secrets() -> None:
    """진짜 env 비밀(토큰/SSH/cloud)은 워커 env 에 전달되지 않는다(deny-by-default)."""
    base = {
        "PATH": "/usr/bin",
        "ANTHROPIC_API_KEY": "DUMMY_SHOULD_NOT_LEAK",
        "GITHUB_TOKEN": "DUMMY_SHOULD_NOT_LEAK",
        "SSH_AUTH_SOCK": "/run/user/1000/keyring/ssh",
        "AWS_SECRET_ACCESS_KEY": "DUMMY_SHOULD_NOT_LEAK",
        "GPG_AGENT_INFO": "x",
        "HOME": "/home/real",
    }
    env = _build_claude_env("/fake/home", "/fake/home/work", base)
    leaked = [k for k in ("ANTHROPIC_API_KEY", "GITHUB_TOKEN", "SSH_AUTH_SOCK",
                          "AWS_SECRET_ACCESS_KEY", "GPG_AGENT_INFO") if k in env]
    assert leaked == [], f"비밀 env 누출: {leaked}"
    assert "DUMMY_SHOULD_NOT_LEAK" not in env.values()


def test_env_allowlist_sets_home_and_tmpdir() -> None:
    """HOME=가짜홈, TMPDIR=작업폴더 를 명시 주입(진짜 HOME 덮어씀)."""
    env = _build_claude_env("/fake/home", "/fake/home/work", {"HOME": "/home/real"})
    assert env["HOME"] == "/fake/home"
    assert env["TMPDIR"] == "/fake/home/work"


def test_env_allowlist_keeps_required() -> None:
    """claude 실행에 필요한 변수(PATH/LANG/TLS)는 통과."""
    base = {"PATH": "/usr/bin", "LANG": "ko_KR.UTF-8",
            "SSL_CERT_FILE": "/etc/ssl/cert.pem", "IRRELEVANT": "x"}
    env = _build_claude_env("/fh", "/fh/work", base)
    assert env["PATH"] == "/usr/bin"
    assert env["LANG"] == "ko_KR.UTF-8"
    assert env["SSL_CERT_FILE"] == "/etc/ssl/cert.pem"
    assert "IRRELEVANT" not in env  # allowlist 외 = 차단


# --- BL-2: CLAUDE_RO_PATHS 최소화 (진짜홈·/proc·/run·/dev 미포함) ---


def test_ro_paths_exclude_home_proc_run_dev() -> None:
    """RO 면 최소화 — 진짜 홈·/proc·전체 /run·전체 /dev 미노출(우회 채널 차단, BL-2)."""
    home = os.path.expanduser("~")
    assert home not in CLAUDE_RO_PATHS
    # 광범위 노출 금지(특히 /run/user 세션 소켓·/proc/self/environ)
    for p in ("/proc", "/run", "/dev"):
        assert p not in CLAUDE_RO_PATHS, f"{p} 광범위 RO 노출 = 우회 채널(BL-2)"
    for p in CLAUDE_RO_PATHS:
        assert not p.startswith("/run/user"), f"{p} = 세션 소켓 노출 금지"
        assert not p.startswith("/proc"), f"{p} = /proc 우회 금지"
    # 실행에 필요한 시스템 경로는 유지
    assert "/usr" in CLAUDE_RO_PATHS and "/etc" in CLAUDE_RO_PATHS


# --- BL-5: provision_claude_home (시드 신뢰경계) ---


def _make_src_home(tmp_path: Path) -> Path:
    """더미 진짜홈 — 실 credential 없이 구조만(.claude/.credentials.json + .claude.json)."""
    src = tmp_path / "real-home"
    (src / ".claude").mkdir(parents=True)
    (src / ".claude" / ".credentials.json").write_text('{"dummy": "cred"}')
    (src / ".claude.json").write_text('{"dummy": "config"}')
    return src


def test_provision_creates_home_with_0700(tmp_path: Path) -> None:
    src = _make_src_home(tmp_path)
    home = tmp_path / "fake-home"
    provision_claude_home(str(home), src_home=str(src))
    assert home.is_dir()
    mode = stat.S_IMODE(home.stat().st_mode)
    assert mode == 0o700, f"가짜홈 권한 {oct(mode)} ≠ 0700"


def test_provision_copies_credentials_0600(tmp_path: Path) -> None:
    src = _make_src_home(tmp_path)
    home = tmp_path / "fake-home"
    provision_claude_home(str(home), src_home=str(src))
    cred = home / ".claude" / ".credentials.json"
    assert cred.is_file()
    assert cred.read_text() == '{"dummy": "cred"}'
    assert stat.S_IMODE(cred.stat().st_mode) == 0o600
    # 설정도 복사
    assert (home / ".claude.json").read_text() == '{"dummy": "config"}'


def test_provision_rejects_symlink_credential(tmp_path: Path) -> None:
    """src credential 이 symlink → 거부(symlink 공격 방어, BL-5)."""
    src = tmp_path / "real-home"
    (src / ".claude").mkdir(parents=True)
    secret = tmp_path / "elsewhere-secret"
    secret.write_text("victim")
    (src / ".claude" / ".credentials.json").symlink_to(secret)
    home = tmp_path / "fake-home"
    with pytest.raises((RuntimeError, ValueError)):
        provision_claude_home(str(home), src_home=str(src))


def test_provision_fail_closed_missing_credential(tmp_path: Path) -> None:
    """credential 누락 → raise(fail-closed, 비인증 진행 금지 BL-6)."""
    src = tmp_path / "real-home"
    (src / ".claude").mkdir(parents=True)  # credential 없음
    home = tmp_path / "fake-home"
    with pytest.raises((RuntimeError, FileNotFoundError)):
        provision_claude_home(str(home), src_home=str(src))


# --- BL-4: code_runner 클로저가 HOME=가짜홈 주입 (subprocess 격리) ---


def test_code_runner_injects_fake_home(tmp_path: Path) -> None:
    """_make_claude_runner(home) 클로저 = cwd/TMPDIR 가짜홈 하위 + HOME 주입(BL-4)."""
    home = str(tmp_path / "fh")
    captured: dict = {}

    def spy_run(cmd, *, cwd, env, capture_output, text):
        captured["cmd"] = cmd
        captured["cwd"] = cwd
        captured["env"] = env
        return SimpleNamespace(returncode=0, stdout='{"result":"ok","is_error":false}', stderr="")

    runner = _make_claude_runner(home, run=spy_run)
    rc, out, err = runner(["claude", "-p", "작업"], "/tmp/orchestrator-workdir")
    assert rc == 0
    assert captured["env"]["HOME"] == home          # 가짜홈 주입
    assert captured["cwd"].startswith(home)          # cwd 가짜홈 하위(nest)
    assert captured["env"]["TMPDIR"].startswith(home)
    # 진짜 env 비밀이 섞이지 않음(allowlist)
    assert "ANTHROPIC_API_KEY" not in captured["env"]


# --- BL-2 우회 음성테스트 [F][G][H] — 실 ll_sandbox 커널 강제 (토큰 0, 일반 명령) ---


def _run_probe(fake_home: Path, argv: list[str], env: dict[str, str]) -> subprocess.CompletedProcess:
    """가짜홈 RW + CLAUDE_RO_PATHS(최소) 격리 안에서 probe 명령 실행."""
    work = fake_home / "work"
    work.mkdir(parents=True, exist_ok=True)
    iso = LandlockIsolation(ro_paths=list(CLAUDE_RO_PATHS), rw_root=str(fake_home))
    cmd = iso.wrap(argv, workdir=str(work))
    return subprocess.run(cmd, cwd=str(work), env=env, capture_output=True, text=True)


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_neg_F_env_secret_not_present(tmp_path: Path) -> None:
    """[F] allowlist env → 격리 안 프로세스가 더미 토큰을 env 로 못 읽음 + /proc 미노출."""
    fh = tmp_path / "fh"
    fh.mkdir()
    base = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "ANTHROPIC_API_KEY": "DUMMY_SHOULD_NOT_LEAK"}
    env = _build_claude_env(str(fh), str(fh / "work"), base)
    proc = _run_probe(fh, ["sh", "-c", "env"], env)
    assert "DUMMY_SHOULD_NOT_LEAK" not in proc.stdout  # allowlist 가 비밀 제거


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_neg_G_proc_traversal_blocked(tmp_path: Path) -> None:
    """[G] /proc RO 미노출 → /proc/self/environ·/proc/1/root traversal 차단."""
    fh = tmp_path / "fh"
    fh.mkdir()
    env = _build_claude_env(str(fh), str(fh / "work"), {"PATH": os.environ.get("PATH", "/usr/bin:/bin")})
    proc = _run_probe(fh, ["sh", "-c", "cat /proc/self/environ; cat /proc/1/root/etc/hostname"], env)
    # /proc 미노출 = 읽기 실패(빈 stdout). 격리 입증.
    assert proc.stdout.strip() == "", f"/proc 우회 노출: {proc.stdout!r}"


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_neg_H_run_socket_and_real_home_blocked(tmp_path: Path) -> None:
    """[H] /run 세션 소켓 + 진짜 홈 미노출 → 접근 차단."""
    fh = tmp_path / "fh"
    fh.mkdir()
    env = _build_claude_env(str(fh), str(fh / "work"), {"PATH": os.environ.get("PATH", "/usr/bin:/bin")})
    real_ssh = os.path.expanduser("~/.ssh")
    proc = _run_probe(
        fh, ["sh", "-c", f"ls /run/user 2>/dev/null; ls {real_ssh} 2>/dev/null"], env)
    assert proc.stdout.strip() == "", f"/run·진짜홈 우회 노출: {proc.stdout!r}"


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_neg_fake_home_write_allowed(tmp_path: Path) -> None:
    """대조: 가짜 홈(RW root) 안 쓰기는 허용(claude 정상 동작 전제)."""
    fh = tmp_path / "fh"
    fh.mkdir()
    env = _build_claude_env(str(fh), str(fh / "work"), {"PATH": os.environ.get("PATH", "/usr/bin:/bin")})
    proc = _run_probe(fh, ["sh", "-c", f"echo ok > {fh}/work/w.txt && echo wrote"], env)
    assert "wrote" in proc.stdout
    assert (fh / "work" / "w.txt").read_text().strip() == "ok"
