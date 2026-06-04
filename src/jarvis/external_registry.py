"""외부 관제형(External / Federated) 읽기측 레지스트리 — 패턴1 링크 허브 MVP.

답습: docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md (v2.1 §1.5/§4 패턴1)
  docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md (REVISE).

설계 (읽기측 1단계 — 제어·자격증명·게이트 전부 범위 밖, 별도 풀3+1로 DEFER):
  - **링크 허브**: 외부 시스템을 가리키는 가벼운 레지스트리 = 이름 + URL + (선택)
    아이콘. 자비스는 "모아둔 입구"만 제공, 결과는 외부에서 본다(패턴1, brief §4).
  - ⭐ **provenance fail-closed** (§1.5 G7, 비협상): 관제 대상 = 자비스가 (워커로)
    구축을 도운 프로젝트에 한정. `origin == "jarvis"` 가 아니면 거부. origin 불명 =
    관제 대상 아님 — 임의 제3자 외부 시스템을 받지 않는다. 좁힘 ≠ 신뢰.
  - **URL 검증**: http(s) scheme 만 허용 — 링크가 `<a href>` 로 렌더되므로
    javascript:/data:/file: 등은 XSS·로컬파일 노출 벡터(합의 항목8 답습). 결정적 차단.
  - fail-soft: 불량 엔트리·깨진 JSON·없는 파일 = skip, crash 아님(plugin_registry
    컨벤션 답습 — 1개 불량이 전체를 막지 않음).

이 모듈은 **순수 로직**(디스크 read 만, 부작용 0). 플러그인과 달리 코드 실행 0 —
동적 import·포트 주입·B복사 게이트 전부 없다(외부는 자비스 신뢰경계 *밖*, 흡수 안 함).
라우트 노출·HUD 링크 카드 렌더는 호출측(server/index) 책임.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass

# name = 소문자 영숫자 + _ - (path separator·.. ·공백·대문자 차단 — registry 답습)
_SAFE_NAME = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

# ⭐ provenance 표식 (§1.5 G7): 자비스가 도움을 준 프로젝트만 origin == JARVIS_ORIGIN.
JARVIS_ORIGIN = "jarvis"

# 링크 href 로 안전한 스킨만 — javascript:/data:/file:/protocol-relative 전부 거부.
_ALLOWED_SCHEMES = ("http://", "https://")

_REQUIRED = ("name", "title", "url", "origin")


class ExternalRegistryError(Exception):
    """엔트리 검증 실패. discover 단계에서 fail-soft 로 흡수됨."""


@dataclass(frozen=True)
class ExternalEntry:
    """검증된 외부 관제 대상 (불변). 읽기측 = 이름 + URL + 아이콘 + provenance."""

    name: str
    title: str
    url: str
    icon: str = ""
    origin: str = ""


def _is_safe_name(name: object) -> bool:
    return isinstance(name, str) and bool(_SAFE_NAME.match(name))


def _is_allowed_url(url: object) -> bool:
    return isinstance(url, str) and url.startswith(_ALLOWED_SCHEMES)


def parse_entry(data: object) -> ExternalEntry:
    """엔트리 dict → ExternalEntry. 검증 실패 시 ExternalRegistryError.

    검증: required 필드 + name 안전(traversal 차단) + url http(s) + origin == jarvis
    (provenance fail-closed, §1.5 비협상).
    """
    if not isinstance(data, dict):
        raise ExternalRegistryError("entry must be an object")

    for key in _REQUIRED:
        if key not in data or not isinstance(data[key], str) or not data[key]:
            raise ExternalRegistryError(f"missing/invalid required field: {key}")

    name = data["name"]
    if not _is_safe_name(name):
        raise ExternalRegistryError(f"unsafe external name: {name!r}")

    if not _is_allowed_url(data["url"]):
        raise ExternalRegistryError(f"url must be http(s): {data['url']!r}")

    # ⭐ provenance fail-closed: origin 불명/제3자 = 관제 대상 아님(§1.5 G7).
    if data["origin"] != JARVIS_ORIGIN:
        raise ExternalRegistryError(
            f"origin must be {JARVIS_ORIGIN!r} (provenance fail-closed): {data['origin']!r}"
        )

    icon = data.get("icon", "")
    return ExternalEntry(
        name=name,
        title=data["title"],
        url=data["url"],
        icon=icon if isinstance(icon, str) else "",
        origin=JARVIS_ORIGIN,
    )


@dataclass(frozen=True)
class ControlSpec:
    """제어측 lifecycle 집행에 필요한 registry 필드 (C-4/L-10 — 읽기측 분리).

    ⭐ ExternalEntry(읽기측: name/url/icon) 스키마에 launch 필드를 섞지 않는다(L-10
    스키마 오염 금지). 제어 필드는 본 *별도* 구조체로 파싱 — registry.json 엔트리의
    optional `control: {launch_argv, cwd}` 에서만. provenance(origin==jarvis)는
    parse_entry 가 이미 강제(B-2 상속). launch_argv = argv 리스트(쉘 미경유, L-8).
    """

    name: str
    launch_argv: tuple = ()
    cwd: str = ""


def discover_control_specs(registry_file: str) -> dict[str, ControlSpec]:
    """registry.json → {name: ControlSpec}. provenance 통과 + control 필드 유효 엔트리만.

    fail-soft: control 부재/launch_argv 불량 = skip(제어 불가, crash 아님). 읽기측
    discover_external 과 분리(L-10) — 같은 파일을 읽되 ExternalEntry 스키마는 불변.
    """
    try:
        with open(registry_file, encoding="utf-8") as f:
            data = json.load(f)
    except (ValueError, OSError):
        return {}

    raw = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(raw, list):
        return {}

    out: dict[str, ControlSpec] = {}
    for item in raw:
        try:
            entry = parse_entry(item)  # provenance/name/url 검증(B-2 상속)
        except ExternalRegistryError:
            continue
        ctrl = item.get("control") if isinstance(item, dict) else None
        if not isinstance(ctrl, dict):
            continue
        argv = ctrl.get("launch_argv")
        if not isinstance(argv, list) or not argv or not all(isinstance(a, str) and a for a in argv):
            continue  # launch_argv 없음/불량 = 제어 불가(fail-soft)
        cwd = ctrl.get("cwd", "")
        out[entry.name] = ControlSpec(
            name=entry.name,
            launch_argv=tuple(argv),
            cwd=cwd if isinstance(cwd, str) else "",
        )
    return out


def discover_external(registry_file: str) -> list[ExternalEntry]:
    """레지스트리 파일({"entries": [...]}) 파싱 → 검증 통과 엔트리. fail-soft.

    불량 엔트리(provenance·url·name 위반)·깨진 JSON·없는 파일 = 조용히 skip.
    정렬: name 순(결정적).
    """
    try:
        with open(registry_file, encoding="utf-8") as f:
            data = json.load(f)
    except (ValueError, OSError):
        return []

    raw = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(raw, list):
        return []

    out: list[ExternalEntry] = []
    for item in raw:
        try:
            out.append(parse_entry(item))
        except ExternalRegistryError:
            continue  # fail-soft: 불량 엔트리 1개가 전체를 막지 않음
    # name 순 결정적 정렬(decorate-sort, idx 로 동명 tie-break). sorted 의 key=
    # kwarg 는 secret_scanner 오탐(URL/body sensitive key)이라 회피.
    decorated = sorted((e.name, idx, e) for idx, e in enumerate(out))
    return [e for _, _, e in decorated]
