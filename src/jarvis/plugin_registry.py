"""플러그인 레지스트리 — 단계2 인프라 (#UI-1~4 통합, 120 세션).

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §5-2)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (REVISE).

설계 (§5-2 + BLOCKING C-4):
  - **데이터 레지스트리**: `<plugins_dir>/<name>/plugin.json` (manifest = 데이터).
    코어 코드는 불변 — `discover_enabled_plugins()` 1회 호출만으로 확장 수용.
  - ⭐ **탐색 ≠ 활성화** (C-4, self-mod 우회 차단): 폴더 drop-in 만으로는 활성화
    되지 않는다. `enabled.json`(명시 사람 등록)에 등재된 name 만 활성.
  - 보안: name 화이트리스트(path traversal 차단) + name == 폴더명(스푸핑 차단)
    + panel_js basename only + permissions 화이트리스트.
  - fail-soft: 불량 manifest/깨진 JSON/없는 파일 = skip, 절대 crash 아님
    (Layer0 fail-soft 컨벤션 답습 — 플러그인 1개 불량이 전체를 막지 않음).

이 모듈은 **순수 로직**(디스크 read 만, 부작용 0). 동적 import·라우트 조립·
StaticFiles 마운트는 호출측(server) 책임 — 레지스트리는 *무엇을 활성화할지*만
결정적으로 답한다.
"""
from __future__ import annotations

import importlib
import json
import os
import re
from dataclasses import dataclass, field
from typing import Callable

MANIFEST_FILENAME = "plugin.json"

# name = 소문자 영숫자 + _ - (path separator·.. ·공백·대문자 전부 차단)
_SAFE_NAME = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

# 플러그인 권한 화이트리스트 (§5 갈림길5 최소권한 — 대화 read-only / 측정 write).
# 코어가 주입할 수 있는 capability port 만. core:* 등 미허용.
ALLOWED_PERMISSIONS = frozenset({
    "conversation:read",
    "measurement:read",
    "measurement:write",
})

_REQUIRED = ("name", "title", "panel_js")


class PluginError(Exception):
    """manifest 검증 실패. discover 단계에서 fail-soft 로 흡수됨."""


@dataclass(frozen=True)
class PluginManifest:
    """검증된 플러그인 선언 (불변). 프론트 panel_js + 백엔드 routes_module + 권한."""

    name: str
    title: str
    panel_js: str
    icon: str = ""
    routes_module: str | None = None
    permissions: tuple[str, ...] = field(default_factory=tuple)


def _is_safe_name(name: object) -> bool:
    return isinstance(name, str) and bool(_SAFE_NAME.match(name))


def _is_safe_basename(value: object) -> bool:
    """panel_js 는 플러그인 폴더 안 단일 파일명 — 경로 분리자·.. ·절대경로 차단."""
    if not isinstance(value, str) or not value:
        return False
    if value != os.path.basename(value):  # 디렉터리 성분 존재
        return False
    if value in (".", "..") or os.sep in value or (os.altsep and os.altsep in value):
        return False
    return value.endswith(".js")


def parse_manifest(data: dict, *, dir_name: str) -> PluginManifest:
    """manifest dict → PluginManifest. 검증 실패 시 PluginError.

    C-4 보안: name 안전 + name == dir_name(스푸핑 차단) + panel_js basename
    + permissions 화이트리스트.
    """
    if not isinstance(data, dict):
        raise PluginError("manifest must be an object")

    for key in _REQUIRED:
        if key not in data or not isinstance(data[key], str) or not data[key]:
            raise PluginError(f"missing/invalid required field: {key}")

    name = data["name"]
    if not _is_safe_name(name):
        raise PluginError(f"unsafe plugin name: {name!r}")
    if name != dir_name:
        raise PluginError(f"manifest name {name!r} != dir {dir_name!r} (spoof)")

    if not _is_safe_basename(data["panel_js"]):
        raise PluginError(f"unsafe panel_js: {data['panel_js']!r}")

    routes_module = data.get("routes_module")
    if routes_module is not None and not isinstance(routes_module, str):
        raise PluginError("routes_module must be a string or absent")

    perms_raw = data.get("permissions", [])
    if not isinstance(perms_raw, list):
        raise PluginError("permissions must be a list")
    perms = tuple(perms_raw)
    unknown = set(perms) - ALLOWED_PERMISSIONS
    if unknown:
        raise PluginError(f"unknown permission(s): {sorted(unknown)}")

    return PluginManifest(
        name=name,
        title=data["title"],
        panel_js=data["panel_js"],
        icon=data.get("icon", "") if isinstance(data.get("icon", ""), str) else "",
        routes_module=routes_module,
        permissions=perms,
    )


def discover_plugins(plugins_dir: str) -> list[PluginManifest]:
    """plugins_dir 하위 각 서브폴더의 plugin.json 을 파싱. fail-soft.

    탐색만 — 활성화 여부와 무관. 불량 manifest 는 조용히 skip(crash 아님).
    정렬: name 순(결정적).
    """
    if not os.path.isdir(plugins_dir):
        return []
    out: list[PluginManifest] = []
    for entry in sorted(os.listdir(plugins_dir)):
        sub = os.path.join(plugins_dir, entry)
        manifest_path = os.path.join(sub, MANIFEST_FILENAME)
        if not os.path.isdir(sub) or not os.path.isfile(manifest_path):
            continue
        try:
            with open(manifest_path, encoding="utf-8") as f:
                data = json.load(f)
            out.append(parse_manifest(data, dir_name=entry))
        except (PluginError, ValueError, OSError):
            # fail-soft: 깨진 JSON·검증 실패·읽기 오류 → skip
            continue
    return out


def load_enabled(enabled_file: str) -> frozenset[str]:
    """명시 활성화 목록 읽기 — {"enabled": ["name", ...]}. fail-soft → 빈 집합.

    이 파일이 **활성화 게이트** (C-4). 폴더 탐색과 분리 — 사람이 여기 등재해야
    플러그인이 로드된다.
    """
    try:
        with open(enabled_file, encoding="utf-8") as f:
            data = json.load(f)
        names = data.get("enabled", [])
        if not isinstance(names, list):
            return frozenset()
        return frozenset(n for n in names if isinstance(n, str))
    except (ValueError, OSError):
        return frozenset()


def discover_enabled_plugins(plugins_dir: str, enabled_file: str) -> list[PluginManifest]:
    """⭐ 탐색 ∩ 활성화 = 실제 로드 대상.

    폴더에 있고(discover) **그리고** enabled.json 에 등재된 것만. drop-in 자동
    활성화 차단(C-4). enabled 에 있으나 manifest 없으면 조용히 제외.
    """
    enabled = load_enabled(enabled_file)
    return [m for m in discover_plugins(plugins_dir) if m.name in enabled]


def select_ports(manifest: PluginManifest, available_ports: dict) -> dict:
    """갈림길5 최소권한: 플러그인이 *선언한* permission 에 해당하는 포트만 전달.

    available_ports = {permission_str: port_obj}. manifest.permissions 에 없는
    capability 는 주입 안 됨(미선언=미접근). 코어가 제공 안 하는 포트는 조용히
    제외. board 전체 핸들 금지 — 좁은 capability 포트만.
    """
    return {
        perm: available_ports[perm]
        for perm in manifest.permissions
        if perm in available_ports
    }


def build_plugin_routes(
    manifests: list[PluginManifest],
    available_ports: dict,
    *,
    importer: Callable[[str], object] = importlib.import_module,
) -> list:
    """§5-2 동적 라우트 조립: 각 플러그인의 routes_module.make_routes(ports) 누적.

    - routes_module 없는(프론트 전용) 플러그인 → 백엔드 라우트 0.
    - 최소권한: select_ports 로 선언한 포트만 주입.
    - fail-soft: import 실패·make_routes 부재·예외 → 해당 플러그인 skip(다른
      플러그인·코어 보호). importer 주입으로 hermetic 테스트(실 import 0).
    """
    routes: list = []
    for m in manifests:
        if not m.routes_module:
            continue
        try:
            mod = importer(m.routes_module)
            make = getattr(mod, "make_routes", None)
            if make is None:
                continue
            routes += list(make(select_ports(m, available_ports)))
        except Exception:
            # fail-soft: 플러그인 1개 불량이 전체 라우트 조립을 막지 않음
            continue
    return routes
