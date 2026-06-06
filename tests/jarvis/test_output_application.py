"""반영 게이트 테스트 — slice-app-1 (CB-2/CB-3/CB-4/CB-7).

답습: docs/review/3plus1-consensus-2026-06-06-output-application-loop.md
  - CB-2 반영 대상 화이트리스트(realpath, 쓰기 0) / CB-3 fail-closed(3-way 금지) /
    CB-4 apply 전 repo clean 검증 / CB-7 apply ≠ commit(commit/push는 사람)

git 호출은 git_runner 주입으로 hermetic(실 subprocess 0). FS 검사(_audit_tree)는 tmp_path.
"""
from __future__ import annotations

import os

import pytest

from src.jarvis.output_application import (
    OutputApplicationError,
    apply_patch,
    extract_workdir_diff,
    resolve_target,
)

_VALID_PATCH = (
    "diff --git a/app.py b/app.py\n"
    "--- a/app.py\n"
    "+++ b/app.py\n"
    "@@ -1 +1 @@\n"
    "-old\n"
    "+new\n"
)


class FakeGit:
    """argv prefix 매칭 fake git runner. (rc, out, err) 반환 + 호출 기록."""

    def __init__(self, responses=None):
        self.responses = responses or {}
        self.calls = []

    def __call__(self, argv, cwd, stdin=None):
        self.calls.append((tuple(argv), cwd, stdin))
        key = tuple(argv)
        for k, v in self.responses.items():
            if key[: len(k)] == k:
                return v
        return (0, "", "")

    def ran(self, *sub):
        return any(c[0][: len(sub)] == sub for c in self.calls)


# ── CB-2 화이트리스트 ────────────────────────────────────────────────────
def _git_repo(path):
    path.mkdir(parents=True, exist_ok=True)
    (path / ".git").mkdir()
    return path


def test_resolve_registered_target(tmp_path):
    repo = _git_repo(tmp_path / "voice_lab")
    wl = {"voice_lab": str(repo)}
    assert resolve_target("voice_lab", wl) == os.path.realpath(str(repo))


def test_resolve_unregistered_rejected(tmp_path):
    wl = {"voice_lab": str(tmp_path / "voice_lab")}
    with pytest.raises(OutputApplicationError):
        resolve_target("unknown", wl)


def test_resolve_nonexistent_dir_rejected(tmp_path):
    wl = {"ghost": str(tmp_path / "nope")}
    with pytest.raises(OutputApplicationError):
        resolve_target("ghost", wl)


def test_resolve_non_git_dir_rejected(tmp_path):
    plain = tmp_path / "plain"
    plain.mkdir()
    wl = {"plain": str(plain)}
    with pytest.raises(OutputApplicationError):
        resolve_target("plain", wl)


# ── CB-1 위반 = rejected (git 호출 0) ────────────────────────────────────
def test_patch_violation_rejected_no_git(tmp_path):
    bad = (
        "diff --git a/.git/config b/.git/config\n"
        "--- a/.git/config\n+++ b/.git/config\n@@ -1 +1 @@\n+x\n"
    )
    git = FakeGit()
    res = apply_patch(bad, str(tmp_path), do_apply=True, git_runner=git)
    assert res.outcome == "rejected"
    assert not git.calls  # 위반 patch 는 git 에 닿지 않음


def test_empty_patch_rejected(tmp_path):
    git = FakeGit()
    res = apply_patch("", str(tmp_path), do_apply=True, git_runner=git)
    assert res.outcome == "rejected"
    assert not git.calls


# ── CB-4 repo clean 검증 ─────────────────────────────────────────────────
def test_dirty_repo_referred(tmp_path):
    git = FakeGit({("git", "status", "--porcelain"): (0, " M other.py\n", "")})
    res = apply_patch(_VALID_PATCH, str(tmp_path), do_apply=True, git_runner=git)
    assert res.outcome == "referred"
    assert not git.ran("git", "apply")  # dirty 면 apply 시도 0


# ── CB-3 fail-closed (apply --check 실패) ────────────────────────────────
def test_apply_check_conflict_referred(tmp_path):
    git = FakeGit({
        ("git", "status", "--porcelain"): (0, "", ""),
        ("git", "apply", "--check"): (1, "", "patch does not apply"),
    })
    res = apply_patch(_VALID_PATCH, str(tmp_path), do_apply=True, git_runner=git)
    assert res.outcome == "referred"
    # --check 실패 후 실 apply 는 호출 안 됨
    assert not any(c[0] == ("git", "apply") for c in git.calls)


# ── dry-run (do_apply=False) ─────────────────────────────────────────────
def test_dry_run_passes_without_applying(tmp_path):
    git = FakeGit({
        ("git", "status", "--porcelain"): (0, "", ""),
        ("git", "apply", "--check"): (0, "", ""),
    })
    res = apply_patch(_VALID_PATCH, str(tmp_path), do_apply=False, git_runner=git)
    assert res.outcome == "executed"
    assert res.applied is False
    assert git.ran("git", "apply", "--check")
    assert not any(c[0] == ("git", "apply") for c in git.calls)


# ── 실 apply (do_apply=True) ─────────────────────────────────────────────
def test_real_apply_executes(tmp_path):
    git = FakeGit({
        ("git", "status", "--porcelain"): (0, "", ""),
        ("git", "apply", "--check"): (0, "", ""),
        ("git", "apply"): (0, "", ""),
    })
    res = apply_patch(_VALID_PATCH, str(tmp_path), do_apply=True, git_runner=git)
    assert res.outcome == "executed"
    assert res.applied is True
    assert any(c[0] == ("git", "apply") for c in git.calls)


# ── CB-7 apply ≠ commit/push ─────────────────────────────────────────────
def test_never_commits_or_pushes(tmp_path):
    git = FakeGit({
        ("git", "status", "--porcelain"): (0, "", ""),
        ("git", "apply", "--check"): (0, "", ""),
        ("git", "apply"): (0, "", ""),
    })
    apply_patch(_VALID_PATCH, str(tmp_path), do_apply=True, git_runner=git)
    assert not git.ran("git", "commit")
    assert not git.ran("git", "push")


# ── Q-d diff 추출 ────────────────────────────────────────────────────────
def test_extract_diff_returns_patch(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    (work / "app.py").write_text("new\n", encoding="utf-8")
    git = FakeGit({("git", "diff", "--cached"): (0, _VALID_PATCH, "")})
    patch, err = extract_workdir_diff(str(work), git_runner=git)
    assert err is None
    assert patch == _VALID_PATCH
    assert git.ran("git", "init")
    assert git.ran("git", "add", "-f", ".")


def test_extract_diff_rejects_symlink(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    (work / "real.py").write_text("x\n", encoding="utf-8")
    os.symlink(str(work / "real.py"), str(work / "link.py"))
    git = FakeGit()
    patch, err = extract_workdir_diff(str(work), git_runner=git)
    assert patch is None
    assert err is not None
    assert not git.calls  # 전수검사 실패 = git 호출 0


def test_extract_diff_rejects_sensitive(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    (work / ".env").write_text("placeholder\n", encoding="utf-8")  # 파일명만 검증(내용 무관)
    git = FakeGit()
    patch, err = extract_workdir_diff(str(work), git_runner=git)
    assert patch is None
    assert err is not None
    assert not git.calls
