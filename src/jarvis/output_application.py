"""워커 산출물 반영 게이트 — slice-app-1 (leaf).

답습: docs/review/3plus1-consensus-2026-06-06-output-application-loop.md
  docs/phase0/jarvis-output-application-loop-brief.md (invariant I1~I7, slice-app-1)

격리 workdir 산출물(diff) → 등록 외부 repo 에 안전 반영. 흐름:
  extract_workdir_diff(workdir)  → git diff 추출(+_audit_tree 전수검사, Q-d)
  resolve_target(name, whitelist) → 반영 대상 realpath 화이트리스트(CB-2)
  apply_patch(patch, repo_real)   → CB-1 의미검증 → CB-4 repo clean → CB-3 apply --check
                                     fail-closed → (do_apply) git apply. commit/push 0(CB-7).

비협상:
  - CB-1: patch_validator.validate_patch 통과 못하면 rejected (git 미접촉).
  - CB-2: whitelist 미등록/디렉토리 아님 = 거부. **쓰기 경로 0**(이 모듈은 whitelist 를
    읽기만 — 등록은 사람 수동 편집).
  - CB-3: git apply --check 실패 = referred(3-way merge 금지). 실 apply 실패 시 정리 시도.
  - CB-4: apply 전 `git status --porcelain` clean 아니면 referred.
  - CB-7: git commit/push 호출 0 (작업트리 변경까지만, 나머지는 사람).

git 호출은 git_runner 주입(hermetic 테스트). 기본 = subprocess.
"""
from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from typing import Callable, Optional

from src.jarvis.patch_validator import PatchValidation, validate_patch
from src.jarvis.plugin_install import PluginInstallError, _audit_tree

# git_runner: (argv, cwd, stdin) -> (returncode, stdout, stderr)
GitRunner = Callable[[list[str], str, Optional[str]], "tuple[int, str, str]"]

_TIMEOUT = 30


class OutputApplicationError(Exception):
    """반영 게이트 위반(화이트리스트/대상). fail-closed."""


@dataclass(frozen=True)
class ApplyResult:
    """반영 결과. outcome ∈ {executed, referred, rejected}."""

    outcome: str
    reason: str
    applied: bool = False
    validation: PatchValidation | None = None


def _default_git_runner(argv: list[str], cwd: str, stdin: str | None = None) -> tuple[int, str, str]:
    proc = subprocess.run(  # noqa: S603 (신뢰 git argv + cwd 인자)
        argv, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=_TIMEOUT,
    )
    return proc.returncode, proc.stdout, proc.stderr


# ── CB-2 반영 대상 화이트리스트 ──────────────────────────────────────────
def resolve_target(name: str, whitelist: dict[str, str]) -> str:
    """등록 외부 repo 이름 → realpath. 미등록/디렉토리 아님 = 거부(fail-closed).

    whitelist 는 읽기만(쓰기 경로 0). realpath containment 로 symlink escape 차단.
    """
    raw = whitelist.get(name)
    if raw is None:
        raise OutputApplicationError(f"미등록 반영 대상(화이트리스트 밖): {name!r}")
    repo_real = os.path.realpath(raw)  # symlink 정규화(등록값은 사람이 명시한 신뢰 경로)
    if not os.path.isdir(repo_real):
        raise OutputApplicationError(f"대상이 디렉터리 아님: {raw!r}")
    if not os.path.isdir(os.path.join(repo_real, ".git")):
        raise OutputApplicationError(f"대상이 git repo 아님(.git 없음): {raw!r}")
    return repo_real


# ── Q-d 산출물 diff 추출 ─────────────────────────────────────────────────
def extract_workdir_diff(
    workdir: str, *, git_runner: GitRunner = _default_git_runner
) -> tuple[str | None, str | None]:
    """격리 workdir → git diff 텍스트. (patch, error). fail-soft.

    _audit_tree 전수검사(symlink/민감파일)를 git 접촉 *전* 수행 → 위반 시 git 호출 0.
    """
    work_real = os.path.realpath(workdir)
    if not os.path.isdir(work_real):
        return None, f"workdir 디렉터리 아님: {workdir!r}"
    # 전수검사(plugin_install 답습 — symlink/민감파일 fail-closed). git 접촉 전.
    try:
        _audit_tree(work_real)
    except PluginInstallError as exc:
        return None, f"산출물 전수검사 실패: {exc}"

    if not os.path.isdir(os.path.join(work_real, ".git")):
        rc, _, err = git_runner(["git", "init"], work_real, None)
        if rc != 0:
            return None, f"git init 실패: {err}"
    git_runner(["git", "config", "user.email", "jarvis@localhost"], work_real, None)
    git_runner(["git", "config", "user.name", "Jarvis Worker"], work_real, None)
    rc, _, err = git_runner(["git", "add", "-f", "."], work_real, None)
    if rc != 0:
        return None, f"git add 실패: {err}"
    rc, out, err = git_runner(["git", "diff", "--cached"], work_real, None)
    if rc != 0:
        return None, f"git diff 실패: {err}"
    return out, None


# ── CB-1/3/4/7 반영 게이트 ───────────────────────────────────────────────
def apply_patch(
    patch: str,
    repo_real: str,
    *,
    do_apply: bool = False,
    git_runner: GitRunner = _default_git_runner,
) -> ApplyResult:
    """patch 를 repo_real 에 안전 반영. commit/push 는 하지 않는다(CB-7)."""
    # CB-1: 의미 검증(git 접촉 전) — 위반 = rejected
    val = validate_patch(patch, repo_real=repo_real)
    if not val.ok:
        kinds = ", ".join(sorted({v.kind for v in val.violations}))
        return ApplyResult("rejected", f"patch 의미 위반({kinds})", False, val)
    if not patch.strip():
        return ApplyResult("rejected", "빈 patch(반영할 변경 없음)", False, val)

    # CB-4: repo clean 검증
    rc, out, err = git_runner(["git", "status", "--porcelain"], repo_real, None)
    if rc != 0:
        return ApplyResult("referred", f"repo 상태 조회 실패: {err}", False, val)
    if out.strip():
        return ApplyResult("referred", "repo 작업트리 dirty(미완 변경 위 적용 금지)", False, val)

    # CB-3: dry-run (fail-closed, 3-way merge 금지)
    rc, out, err = git_runner(["git", "apply", "--check"], repo_real, patch)
    if rc != 0:
        return ApplyResult("referred", f"git apply --check 실패(충돌): {err.strip()}", False, val)

    if not do_apply:
        return ApplyResult("executed", "dry-run 통과(미적용)", False, val)

    # 실 apply — CB-7: commit/push 없음(작업트리 변경까지만)
    rc, out, err = git_runner(["git", "apply"], repo_real, patch)
    if rc != 0:
        # 부분 적용 정리 시도(fail-closed) — 추적 파일 작업트리 복원
        git_runner(["git", "checkout", "--", "."], repo_real, None)
        return ApplyResult("referred", f"git apply 실패: {err.strip()}", False, val)
    return ApplyResult("executed", "적용 완료(commit/push 는 사람)", True, val)
