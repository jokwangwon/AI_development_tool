"""CB-1 patch_validator 테스트 — git apply 의 "문법만 검증" 갭 보완.

답습: docs/review/3plus1-consensus-2026-06-06-output-application-loop.md (CB-1 비협상)
  docs/phase0/jarvis-output-application-loop-brief.md (§2 invariant, slice-app-1)

핵심: git apply --check 는 patch 의 *문법*만 검증하고 *의미*(어떤 파일을 건드리는가)는
검증하지 않는다 → 이 validator 가 patch 텍스트에서 대상 경로를 추출해 아래를 fail-closed 거부:
  (a) repo 밖 traversal (a/../../etc/x)
  (b) .git/ 메타데이터 수정
  (c) symlink 생성 (mode 120000)
  (d) 민감 파일 (.env, id_rsa, *.pem 등 — plugin_install denylist 재사용)
"""
from __future__ import annotations

import pytest

from src.jarvis.patch_validator import PatchViolation, validate_patch


def _diff(*body: str) -> str:
    return "\n".join(body) + "\n"


# ── happy path ──────────────────────────────────────────────────────────
def test_valid_patch_passes():
    patch = _diff(
        "diff --git a/src/app.py b/src/app.py",
        "index 1111111..2222222 100644",
        "--- a/src/app.py",
        "+++ b/src/app.py",
        "@@ -1 +1 @@",
        "-old",
        "+new",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is True
    assert result.violations == []
    assert "src/app.py" in result.paths


def test_new_file_passes():
    patch = _diff(
        "diff --git a/docs/new.md b/docs/new.md",
        "new file mode 100644",
        "--- /dev/null",
        "+++ b/docs/new.md",
        "@@ -0,0 +1 @@",
        "+hello",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is True


def test_empty_patch_is_ok_no_paths():
    result = validate_patch("", repo_real="/home/u/repo")
    assert result.ok is True
    assert result.paths == []


# ── (a) traversal 거부 ──────────────────────────────────────────────────
def test_path_traversal_rejected():
    patch = _diff(
        "diff --git a/../../etc/passwd b/../../etc/passwd",
        "--- a/../../etc/passwd",
        "+++ b/../../etc/passwd",
        "@@ -1 +1 @@",
        "+pwned",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "traversal" for v in result.violations)


def test_absolute_path_rejected():
    patch = _diff(
        "diff --git a/tmp/x b/tmp/x",
        "--- /dev/null",
        "+++ /tmp/pwned",
        "@@ -0,0 +1 @@",
        "+x",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "traversal" for v in result.violations)


# ── (b) .git/ 거부 ──────────────────────────────────────────────────────
def test_dotgit_path_rejected():
    patch = _diff(
        "diff --git a/.git/hooks/pre-commit b/.git/hooks/pre-commit",
        "--- a/.git/hooks/pre-commit",
        "+++ b/.git/hooks/pre-commit",
        "@@ -1 +1 @@",
        "-#!/bin/bash",
        "+rm -rf /",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "dotgit" for v in result.violations)


# ── (c) symlink 거부 ────────────────────────────────────────────────────
def test_symlink_creation_rejected():
    patch = _diff(
        "diff --git a/link b/link",
        "new file mode 120000",
        "--- /dev/null",
        "+++ b/link",
        "@@ -0,0 +1 @@",
        "+/etc/passwd",
        "\\ No newline at end of file",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "symlink" for v in result.violations)


def test_mode_change_to_symlink_rejected():
    patch = _diff(
        "diff --git a/file b/file",
        "old mode 100644",
        "new mode 120000",
        "--- a/file",
        "+++ b/file",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "symlink" for v in result.violations)


# ── (d) 민감 파일 거부 ──────────────────────────────────────────────────
@pytest.mark.parametrize("name", [".env", "id_rsa", "secret.pem", ".netrc"])
def test_sensitive_file_rejected(name):
    patch = _diff(
        f"diff --git a/{name} b/{name}",
        "--- /dev/null",
        f"+++ b/{name}",
        "@@ -0,0 +1 @@",
        "+leak",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "sensitive" for v in result.violations)


def test_sensitive_file_in_subdir_rejected():
    patch = _diff(
        "diff --git a/config/.env b/config/.env",
        "--- a/config/.env",
        "+++ b/config/.env",
        "@@ -1 +1 @@",
        "-A=1",
        "+A=2",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "sensitive" for v in result.violations)


# ── multi-violation: 여러 위반 모두 보고 ────────────────────────────────
def test_multiple_violations_all_reported():
    patch = _diff(
        "diff --git a/.git/config b/.git/config",
        "--- a/.git/config",
        "+++ b/.git/config",
        "@@ -1 +1 @@",
        "+x",
        "diff --git a/.env b/.env",
        "--- a/.env",
        "+++ b/.env",
        "@@ -1 +1 @@",
        "+y",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    kinds = {v.kind for v in result.violations}
    assert "dotgit" in kinds
    assert "sensitive" in kinds


# ── rename 도 양쪽 경로 검증 ────────────────────────────────────────────
def test_rename_target_validated():
    patch = _diff(
        "diff --git a/ok.py b/.git/evil",
        "similarity index 100%",
        "rename from ok.py",
        "rename to .git/evil",
    )
    result = validate_patch(patch, repo_real="/home/u/repo")
    assert result.ok is False
    assert any(v.kind == "dotgit" for v in result.violations)
