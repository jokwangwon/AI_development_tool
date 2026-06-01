"""B복사 게이트 — 단계3 (#UI-4 산출물 반영, 120 세션).

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §5-3/§7)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (BLOCKING C-1·C-3 비협상).

#UI-4 "반영 메커니즘"의 안전한 형태: 격리 work 산출물 → 사람 승인 → plugins/ 복사.
이 모듈이 **복사 게이트**다. 자동 호출 금지 — auto-dispatch 경로에서 호출되지 않고,
오직 사람이 명시 트리거한 install 엔드포인트에서만 호출된다(C-1 자동복사 금지 코드강제).

보안 (비협상):
  - **C-1**: target = plugins_dir/<name> realpath 화이트리스트(traversal 차단) +
    이름 안전 + 덮어쓰기 금지(기존 존재 → 거부).
  - **C-3**: 소스 realpath 가 work_root 하위여야(밖 → 거부, symlink escape 포함) +
    트리 내 symlink 거부 + 민감 파일명 fail-closed 거부(secret 유출 차단).
  - **C-4 보존**: install = 복사만. 활성화(enabled.json)는 enable_plugin 별도 명시
    단계. 복사만으로 활성화되지 않는다(drop-in 자동활성 금지 불변식 유지).

fail-closed: 위반 시 PluginInstallError + 부분 복사물 정리(잔존 금지).
"""
from __future__ import annotations

import json
import os
import shutil

from src.jarvis.plugin_registry import (
    MANIFEST_FILENAME,
    PluginError,
    PluginManifest,
    _SAFE_NAME,
    parse_manifest,
)

# 민감 파일명 denylist — 워커 산출물에 섞이면 fail-closed 거부(skip 아닌 reject:
# 사람이 알아채도록). credential/키/환경파일.
_SENSITIVE_NAMES = frozenset({
    ".credentials.json",
    ".claude.json",
    "id_rsa",
    "id_ed25519",
    "id_ecdsa",
    "id_dsa",
    ".env",
    ".netrc",
    ".npmrc",
    ".pypirc",
})
_SENSITIVE_SUFFIXES = (".pem", ".key", ".p12", ".pfx")


class PluginInstallError(Exception):
    """B복사 게이트 위반(경로/symlink/secret/덮어쓰기). fail-closed."""


def _is_safe_name(name: object) -> bool:
    return isinstance(name, str) and bool(_SAFE_NAME.match(name))


def _is_sensitive(filename: str) -> bool:
    base = os.path.basename(filename)
    if base in _SENSITIVE_NAMES:
        return True
    return any(base.endswith(suf) for suf in _SENSITIVE_SUFFIXES)


def _within(child_real: str, parent_real: str) -> bool:
    """child_real 이 parent_real 하위(또는 동일)인지 — realpath 기반 containment."""
    if child_real == parent_real:
        return True
    return child_real.startswith(parent_real + os.sep)


def _audit_tree(src_real: str) -> None:
    """복사 전 트리 전수 검사 — symlink·민감파일 발견 시 fail-closed (C-3).

    복사를 시작하기 전에 *먼저* 전체를 검사해 부분 복사물이 남지 않게 한다.
    """
    for root, dirs, files in os.walk(src_real):
        for entry in dirs + files:
            p = os.path.join(root, entry)
            if os.path.islink(p):
                raise PluginInstallError(f"symlink 거부(C-3 symlink 방어): {p!r}")
        for f in files:
            if _is_sensitive(f):
                raise PluginInstallError(
                    f"민감 파일 거부(C-3 secret, fail-closed): {os.path.join(root, f)!r}"
                )


def install_plugin_from_work(
    source: str,
    name: str,
    *,
    work_root: str,
    plugins_dir: str,
) -> PluginManifest:
    """격리 work 산출물(source) → plugins_dir/<name> 안전 복사. 검증된 manifest 반환.

    명시 호출 전용(사람 승인 후). 위반 시 PluginInstallError(fail-closed).
    """
    # C-1: 이름 안전 (path traversal / 대문자 / 공백 차단)
    if not _is_safe_name(name):
        raise PluginInstallError(f"unsafe plugin name: {name!r}")

    # C-3: 소스가 work_root 하위여야 (symlink escape 도 realpath 로 차단)
    work_real = os.path.realpath(work_root)
    src_real = os.path.realpath(source)
    if not os.path.isdir(src_real):
        raise PluginInstallError(f"source 디렉터리 아님: {source!r}")
    if not _within(src_real, work_real):
        raise PluginInstallError(
            f"source 가 work_root 밖(C-3 범위 제한): {src_real!r} ⊄ {work_real!r}"
        )

    # C-1: target realpath 화이트리스트 (plugins_dir 하위여야)
    plugins_real = os.path.realpath(plugins_dir)
    target = os.path.join(plugins_dir, name)
    target_real = os.path.realpath(target)
    if not _within(target_real, plugins_real):
        raise PluginInstallError(f"target 이 plugins_dir 밖(C-1): {target_real!r}")
    if os.path.exists(target):
        raise PluginInstallError(f"target 이미 존재(덮어쓰기 금지): {target!r}")

    # manifest 검증 + 이름 일치 (스푸핑 차단)
    manifest_path = os.path.join(src_real, MANIFEST_FILENAME)
    if not os.path.isfile(manifest_path) or os.path.islink(manifest_path):
        raise PluginInstallError(f"manifest 없음/symlink: {manifest_path!r}")
    try:
        with open(manifest_path, encoding="utf-8") as f:
            data = json.load(f)
        manifest = parse_manifest(data, dir_name=name)
    except (PluginError, ValueError, OSError) as exc:
        raise PluginInstallError(f"manifest 검증 실패: {exc}") from exc

    # C-3: 복사 전 전수 검사 (symlink·민감파일 → fail-closed, 부분물 잔존 0)
    _audit_tree(src_real)

    # 안전 복사 — symlink 미추종(copytree 가 검사 후라 안전하나 symlinks=False 명시)
    try:
        shutil.copytree(src_real, target, symlinks=False)
    except Exception as exc:
        # 부분 복사물 정리 (fail-closed)
        shutil.rmtree(target, ignore_errors=True)
        raise PluginInstallError(f"복사 실패: {exc}") from exc

    return manifest


# ── 활성화 게이트 (C-4 — install 과 분리된 명시 단계) ──────────────────
def _read_enabled(enabled_file: str) -> list[str]:
    try:
        with open(enabled_file, encoding="utf-8") as f:
            data = json.load(f)
        names = data.get("enabled", [])
        return [n for n in names if isinstance(n, str)] if isinstance(names, list) else []
    except (ValueError, OSError):
        return []


def _write_enabled(enabled_file: str, names: list[str]) -> None:
    with open(enabled_file, "w", encoding="utf-8") as f:
        json.dump({"enabled": names}, f, ensure_ascii=False, indent=2)
        f.write("\n")


def enable_plugin(name: str, *, enabled_file: str) -> None:
    """plugins/enabled.json 에 name 등재 — **명시 활성화 게이트**(C-4).

    install(복사)과 분리. 사람이 이 단계를 밟아야 플러그인이 로드된다. idempotent.
    """
    if not _is_safe_name(name):
        raise PluginInstallError(f"unsafe plugin name: {name!r}")
    names = _read_enabled(enabled_file)
    if name not in names:
        names.append(name)
        _write_enabled(enabled_file, names)


def disable_plugin(name: str, *, enabled_file: str) -> None:
    """enabled.json 에서 name 제거(비활성화). 미존재여도 무해."""
    if not _is_safe_name(name):
        raise PluginInstallError(f"unsafe plugin name: {name!r}")
    names = _read_enabled(enabled_file)
    if name in names:
        _write_enabled(enabled_file, [n for n in names if n != name])
