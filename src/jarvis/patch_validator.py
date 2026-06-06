"""CB-1 patch 의미 검증 — git apply 의 "문법만 검증" 갭 보완 (leaf).

답습: docs/review/3plus1-consensus-2026-06-06-output-application-loop.md (CB-1 비협상)
  docs/phase0/jarvis-output-application-loop-brief.md (slice-app-1, invariant I1~I7)

`git apply --check` 는 patch 가 *적용 가능한가*(문법)만 본다. *무엇을 건드리는가*(의미)는
보지 않는다 → 이 모듈이 patch 텍스트에서 대상 경로/모드를 추출해 fail-closed 거부한다:
  - traversal: repo 밖 경로 (a/../../etc/x, 절대경로)
  - dotgit: .git/ 메타데이터(refs/objects/hooks/config) 수정
  - symlink: symlink 생성/전환 (mode 120000)
  - sensitive: 민감 파일명 (.env, id_rsa, *.pem … — plugin_install denylist 재사용)

순수 텍스트 검증(부작용 0, hermetic). 모호하면 거부(fail-closed).
"""
from __future__ import annotations

import posixpath
from dataclasses import dataclass, field

from src.jarvis.plugin_install import _is_sensitive

_SYMLINK_MODE = "120000"


@dataclass(frozen=True)
class PatchViolation:
    """patch 위반 1건. kind ∈ {traversal, dotgit, symlink, sensitive}."""

    kind: str
    path: str
    detail: str = ""


@dataclass(frozen=True)
class PatchValidation:
    ok: bool
    violations: list[PatchViolation] = field(default_factory=list)
    paths: list[str] = field(default_factory=list)


def _strip_ab_prefix(token: str) -> str | None:
    """git diff 경로 토큰 → repo 상대경로. /dev/null = 대상 아님(None)."""
    token = token.split("\t", 1)[0].strip()
    if not token or token == "/dev/null":
        return None
    if token.startswith(("a/", "b/")):
        return token[2:]
    # a//b/ prefix 없는 경로(절대경로 등) = 비정상 → 그대로 반환(검증서 traversal 로 포착)
    return token


def _check_path(path: str) -> list[PatchViolation]:
    """단일 대상 경로의 traversal/.git/sensitive 검증."""
    out: list[PatchViolation] = []
    if path.startswith("/"):
        out.append(PatchViolation("traversal", path, "절대경로(repo 밖)"))
        return out  # 절대경로는 더 볼 것 없음
    parts = path.split("/")
    norm = posixpath.normpath(path)
    if ".." in parts or norm.startswith("..") or norm.startswith("/"):
        out.append(PatchViolation("traversal", path, "상위 경로 탈출(..)"))
        return out
    if norm == ".git" or norm.startswith(".git/"):
        out.append(PatchViolation("dotgit", path, ".git 메타데이터 수정 금지"))
    if _is_sensitive(posixpath.basename(norm)):
        out.append(PatchViolation("sensitive", path, "민감 파일명"))
    return out


def _split_blocks(patch: str) -> list[list[str]]:
    """patch 를 `diff --git` 단위 블록으로 분리(헤더 전 preamble 무시)."""
    blocks: list[list[str]] = []
    current: list[str] | None = None
    for line in patch.splitlines():
        if line.startswith("diff --git "):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def _block_paths(block: list[str]) -> list[str]:
    """블록에서 대상 경로 후보 수집(---, +++, rename from/to)."""
    paths: list[str] = []
    for line in block:
        if line.startswith("--- ") or line.startswith("+++ "):
            p = _strip_ab_prefix(line[4:])
            if p is not None:
                paths.append(p)
        elif line.startswith("rename from "):
            paths.append(line[len("rename from "):].strip())
        elif line.startswith("rename to "):
            paths.append(line[len("rename to "):].strip())
    return paths


def validate_patch(patch: str, *, repo_real: str) -> PatchValidation:
    """patch 텍스트를 의미 검증. 위반 없으면 ok=True.

    repo_real 은 향후 절대 containment 재검증용(현재는 상대경로 traversal 차단으로 충분).
    """
    violations: list[PatchViolation] = []
    seen_paths: list[str] = []
    for block in _split_blocks(patch):
        block_paths = _block_paths(block)
        symlink = any(_SYMLINK_MODE in ln for ln in block if "mode" in ln)
        # 대표 경로(symlink 보고용) — 마지막 +++ 측 경로 우선, 없으면 첫 경로
        rep = block_paths[-1] if block_paths else "<unknown>"
        if symlink:
            violations.append(
                PatchViolation("symlink", rep, "symlink 생성/전환(mode 120000) 금지")
            )
        for p in block_paths:
            if p not in seen_paths:
                seen_paths.append(p)
            violations.extend(_check_path(p))
    # 중복 위반 제거(같은 kind+path)
    deduped: list[PatchViolation] = []
    for v in violations:
        if v not in deduped:
            deduped.append(v)
    return PatchValidation(ok=not deduped, violations=deduped, paths=seen_paths)
