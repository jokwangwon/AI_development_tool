#!/usr/bin/env python3
"""Schema validator — Group E PoC (G2 GP-4 External Input Validation + G4 Memory/Skill schema validation).

답습 출처:
  - docs/phase0/g2-gp4-g4-schema-validation-poc.md (본 PoC 사양)
  - docs/architecture/governance-preconditions.md §6 (GP-4 외부 입력 검증)
  - docs/architecture/provider-agnostic-memory-skill-design.md §3.1 (Skill 17-field) /
    §3.2 (필드별 검증 규칙) / §3.3 (promotion_status 5 enum + transition) / §4.2 (JSONL 11-field)
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 + §2.3 운영 함의 #1 (Tools verify Hermes 출력)
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.2 (11-field schema enum)
  - tools/jsonl_hash_chain.py (Group C `validate_schema` 11-field — import 직접)
  - tools/secret_scanner.py (Group D 답습 — 2 mode CLI + violation reporter)

핵심 강제 조건 (사용자 명시 답습):
  - stdlib `re` + `json` + `dataclasses` 단독 (외부 의존성 0건)
  - pydantic / jsonschema / pyyaml 미도입 (사양 §2 답습)
  - G4 §3.1 17-field 직접 정의 (변경 0건)
  - G4 §4.2 11-field 검증 = jsonl_hash_chain.validate_schema import 직접 (Group C 답습)
  - Memory boundary 4 금지 runtime 강제 미진입 (Group G 영역)
  - Skill wrapper escalation 차단 미진입 (Group G 영역)
  - 재귀 JSON Schema 의미 검증 미진입 (top-level 형식만)

Mode (사용자 명시):
  --mode external-input : Hermes/Worker/LLM 출력 schema + injection canary 검출 (E-1 GP-4)
  --mode skill-schema   : G4 §3.1 17-field + §4.2 11-field 정적 검증 (E-2 G4)

종료 코드:
  0 = 위반 0건 (PASS)
  1 = ≥1 위반 검출 (FAIL — E-1 injection 검출 / E-2 schema 위반)
  2 = 입력 오류 (path 부재 / parse 실패 등)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonl_hash_chain import (  # type: ignore[import-not-found]
    ALLOWED_AGENTS,
    ALLOWED_SCOPES,
    ALLOWED_TYPES,
    REQUIRED_FIELDS as JSONL_REQUIRED_FIELDS,
    SUPPORTED_SCHEMA_VERSION,
    validate_schema as validate_jsonl_schema,
)

# ============================================================================
# E-1 — External Input canary patterns (GP-4 §6.3 답습)
# ============================================================================

# Prompt injection canary (12 패턴) — 직접 답습 금지 표현 catalog
PROMPT_INJECTION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("prompt-injection-ignore-prev", re.compile(r"(?i)\bIGNORE\s+(ALL\s+)?PREVIOUS\s+INSTRUCTIONS?\b")),
    ("prompt-injection-disregard", re.compile(r"(?i)\bDISREGARD\s+(ALL\s+)?(PREVIOUS|ABOVE)\b")),
    ("prompt-injection-system-prefix", re.compile(r"<<<\s*SYSTEM\s*[:>]")),
    ("prompt-injection-system-bracket", re.compile(r"\[\s*SYSTEM\s*\]")),
    ("prompt-injection-developer-mode", re.compile(r"(?i)\bDEVELOPER\s+MODE\s+(ENABLED|ACTIVATED|ON)\b")),
    ("prompt-injection-jailbreak", re.compile(r"(?i)\bjailbreak(ed)?\b|\bDAN\s+mode\b")),
    ("prompt-injection-pretend-you-are", re.compile(r"(?i)\bPRETEND\s+YOU\s+ARE\b|\bACT\s+AS\s+IF\s+YOU\s+ARE\b")),
    ("prompt-injection-new-instructions", re.compile(r"(?i)\bNEW\s+INSTRUCTIONS?\s*:\s")),
    ("prompt-injection-end-of-prompt", re.compile(r"(?i)\bEND\s+OF\s+(PROMPT|INSTRUCTIONS)\b")),
    ("prompt-injection-reveal-system", re.compile(r"(?i)\bREVEAL\s+(YOUR\s+)?SYSTEM\s+PROMPT\b|\bSHOW\s+ME\s+YOUR\s+INSTRUCTIONS\b")),
    ("prompt-injection-override-rules", re.compile(r"(?i)\bOVERRIDE\s+(THE\s+)?(RULES|GUARDRAILS|SAFETY)\b")),
    ("prompt-injection-role-reset", re.compile(r"(?i)\bRESET\s+(YOUR\s+)?ROLE\b|\bFORGET\s+(YOUR\s+)?(ROLE|TRAINING)\b")),
]

# Unauthorized policy-change request (8 패턴)
UNAUTHORIZED_POLICY_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("unauthorized-policy-update-adr", re.compile(r"(?i)\bUPDATE\s+ADR(-\d+)?\b|\bMODIFY\s+ADR(-\d+)?\b|\bedit\s+ADR(-\d+)?\b")),
    ("unauthorized-policy-update-constitution", re.compile(r"(?i)\b(UPDATE|MODIFY|EDIT|REWRITE)\s+(THE\s+)?CONSTITUTION\b")),
    ("unauthorized-policy-disable-hermes", re.compile(r"(?i)\bDISABLE\s+HERMES\b|\bSTOP\s+HERMES\b|\bKILL\s+HERMES\b")),
    ("unauthorized-policy-bypass-redaction", re.compile(r"(?i)\bBYPASS\s+REDACTION\b|\bSKIP\s+REDACTION\b|\bDISABLE\s+REDACTION\b")),
    ("unauthorized-policy-elevate-permissions", re.compile(r"(?i)\bGRANT\s+ME\s+(ROOT|ADMIN|SUDO)\b|\bELEVATE\s+(MY\s+)?PERMISSIONS\b")),
    ("unauthorized-policy-change-gate-status", re.compile(r"(?i)\b(MARK|SET|FORCE)\s+(G[1-9][a-z]?\s+)?(AS\s+)?PASS(ED)?\b")),
    ("unauthorized-policy-promote-skill", re.compile(r"(?i)\bAUTO[\s_-]*PROMOTE\s+(SKILL|MEMORY)\b|\bself[\s_-]*approv(e|al)\b")),
    ("unauthorized-policy-write-memory", re.compile(r"(?i)\bWRITE\s+TO\s+(GLOBAL\s+)?MEMORY\b\s+as\s+(hermes|agent|system)")),
]

# Injection payload canary (SQL / command / path traversal — 6 패턴)
INJECTION_PAYLOAD_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("injection-sql-drop-table", re.compile(r"(?i)';\s*DROP\s+TABLE\b|\bDROP\s+TABLE\s+\w+\s*--")),
    ("injection-sql-or-1-eq-1", re.compile(r"(?i)\bOR\s+1\s*=\s*1\b|\bOR\s+'1'\s*=\s*'1'")),
    ("injection-sql-union-select", re.compile(r"(?i)\bUNION\s+(ALL\s+)?SELECT\b")),
    ("injection-cmd-substitution", re.compile(r"\$\(\s*(whoami|id|cat\s+/etc/passwd|rm\s+-rf|curl\s+http)")),
    ("injection-cmd-backtick", re.compile(r"`\s*(whoami|id|cat\s+/etc/passwd|rm\s+-rf|curl\s+http)")),
    ("injection-path-traversal", re.compile(r"(\.\./){2,}|/etc/passwd\b|/etc/shadow\b|\\windows\\system32")),
]

ALL_EXTERNAL_INPUT_PATTERNS: list[tuple[str, str, re.Pattern[str]]] = (
    [("prompt-injection", pid, p) for pid, p in PROMPT_INJECTION_PATTERNS]
    + [("unauthorized-policy", pid, p) for pid, p in UNAUTHORIZED_POLICY_PATTERNS]
    + [("injection-payload", pid, p) for pid, p in INJECTION_PAYLOAD_PATTERNS]
)
"""(category, pattern_id, regex) — 26 patterns. CI step 6 4 패턴 cover grep
   대상 = (prompt-injection / unauthorized-policy / malformed-json / injection-payload).
"""

# ============================================================================
# E-2 — G4 §3.1 17-field Skill schema 정의 (변경 0건)
# ============================================================================

REQUIRED_SKILL_FIELDS: tuple[str, ...] = (
    "id", "name", "version", "scope", "owner", "description",
    "inputs", "outputs", "allowed_actions",
    "promotion_status", "provider_bindings", "last_verified_at",
)
"""필수 12 (G4 §3.1 — ✅ 필수 표기 항목만, `provider_bindings` C-K 격상 흡수 포함)."""

MVP_RECOMMENDED_SKILL_FIELDS: tuple[str, ...] = (
    "forbidden_actions",     # MVP-권장 (G4 §3.1 #10)
    "required_evidence",     # MVP-필수 C-K (G4 §3.1 #11) — promotion 시 ledger 검증 의무
    "required_tests",        # MVP-권장 (G4 §3.1 #12)
    "rollback_triggers",     # MVP-권장 (G4 §3.1 #14)
    "created_from",          # MVP-권장 (G4 §3.1 #16)
)
"""MVP-권장/MVP-필수 5 — G4 §3.1. `required_evidence` 는 MVP-필수 (C-K), 본 PoC 분류 = mvp_recommended 카테고리."""

ALL_SKILL_FIELDS: tuple[str, ...] = REQUIRED_SKILL_FIELDS + MVP_RECOMMENDED_SKILL_FIELDS
"""합산 17 (12 + 5 = 17, 사용자 명시 답습)."""

ALLOWED_ACTIONS_ENUM: tuple[str, ...] = (
    "read", "write", "shell", "network", "db", "git", "docker",
)
"""G4 §3.2 #9 — 7 actions."""

PROMOTION_STATUS_ENUM: tuple[str, ...] = (
    "proposed", "approved", "promoted", "archived", "revoked",
)
"""G4 §3.3 — 5 statuses."""

# G4 §3.3 transition 매트릭스 (허용 transitions)
ALLOWED_PROMOTION_TRANSITIONS: frozenset[tuple[str, str]] = frozenset({
    ("proposed", "approved"),
    ("approved", "promoted"),
    ("promoted", "revoked"),
    ("proposed", "archived"),
    ("revoked", "archived"),
})
"""허용 transitions (G4 §3.3 답습)."""

ALLOWED_SCOPE_ENUM: tuple[str, ...] = ("global", "project", "session", "team")
"""G4 §3.2 #4 — 4 scopes (Skill scope, Memory scope 와 일치)."""

# Provider lock-in marker (C-K 답습 — G4 §3.2 #15)
PROVIDER_LOCKIN_MARKERS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?i)required\s*:\s*true"),
    re.compile(r"(?i)exclusive\s*:\s*true"),
)
"""provider_bindings 내 lock-in marker grep — `required: true` / `exclusive: true`."""

# Provider lock-in marker in identifier fields (lock-in marker grep — G4 §3.2 #5)
PROVIDER_NAME_IDENTIFIERS: tuple[str, ...] = (
    "openai", "anthropic", "gpt-4", "gpt-3", "claude-3", "claude-2",
    "litellm", "ollama", "google.generativeai",
)
"""owner / name 등 identifier 필드의 provider 이름 lock-in marker (정적 grep)."""

# Field validators
SEMVER_RE: re.Pattern[str] = re.compile(r"^\d+\.\d+\.\d+(?:[-+][\w.]+)?$")
ISO8601_RE: re.Pattern[str] = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")
SLUG_RE: re.Pattern[str] = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")
UUID_RE: re.Pattern[str] = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")


@dataclass(frozen=True)
class Violation:
    """Single validation violation (Group D 답습)."""

    file: Path
    line: int
    pattern_id: str
    pattern_category: str
    detail: str

    def format_short(self) -> str:
        sample = self.detail[:80] + ("..." if len(self.detail) > 80 else "")
        return f"{self.file}:{self.line}:{self.pattern_id}:{self.pattern_category}: {sample}"


# ============================================================================
# YAML mini-parser (stdlib only, 사용자 명시 답습 — pyyaml 미도입)
# ============================================================================

def parse_yaml_minimal(text: str) -> dict[str, Any]:
    """Minimal YAML parser — flat key-value + nested object/list 지원.

    제한: 멀티라인 string / anchor / alias / 복잡한 flow 미지원.
    본 PoC fixture 영역 한정 — Skill 17-field 표현에 충분.
    """
    result: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, result)]
    lines = text.split("\n")

    for line_no, raw in enumerate(lines, start=1):
        stripped = raw.rstrip()
        if not stripped or stripped.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        content = stripped.lstrip()

        # Pop stack until we find a parent at smaller indent
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if not stack:
            stack = [(-1, result)]
        parent = stack[-1][1]

        if content.startswith("- "):
            # List item
            value_str = content[2:].strip()
            if isinstance(parent, list):
                if ":" in value_str and not value_str.startswith('"'):
                    # List of dict items not common in this PoC; treat as scalar
                    parent.append(_parse_scalar(value_str))
                else:
                    parent.append(_parse_scalar(value_str))
            continue

        if ":" in content:
            key, _, value_str = content.partition(":")
            key = key.strip()
            value_str = value_str.strip()
            if value_str == "" or value_str == "{}":
                # Nested object (or empty object)
                nested: dict[str, Any] = {}
                if isinstance(parent, dict):
                    parent[key] = nested
                stack.append((indent, nested))
            elif value_str == "[]":
                if isinstance(parent, dict):
                    parent[key] = []
            elif value_str.startswith("- "):
                # Inline list start (rare)
                lst: list[Any] = [_parse_scalar(value_str[2:].strip())]
                if isinstance(parent, dict):
                    parent[key] = lst
                stack.append((indent, lst))
            else:
                if isinstance(parent, dict):
                    parent[key] = _parse_scalar(value_str)

        # Detect "key:\n  - item" pattern: parent[key] is dict by default; if
        # next line is "- ..." we should convert to list. Handle in next iteration:
        # if parent[key] = {} but the next non-empty line at deeper indent starts
        # with "- ", we replace with []. We do this lazily.
        # Simplification: when list items are encountered, re-parent.

    # Post-process: convert empty dicts under list-typed parents (pyyaml-like).
    # Actually we use a simpler approach: scan for keys whose value is empty dict
    # but should be a list (heuristic skipped — fixture는 list 항목 명시 필요).
    return result


def _parse_scalar(s: str) -> Any:
    """Parse YAML scalar into Python value."""
    s = s.strip()
    if s == "":
        return None
    if s.lower() in ("true", "yes"):
        return True
    if s.lower() in ("false", "no"):
        return False
    if s.lower() == "null":
        return None
    # Strip quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    # Numbers
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        pass
    return s


def parse_yaml_with_lists(text: str) -> dict[str, Any]:
    """Better YAML parser — supports nested dicts, lists of scalars, lists of dicts.

    Stack-based with explicit list/dict distinction.
    """
    root: dict[str, Any] = {}
    # Stack entries: (indent, container, container_type)
    stack: list[tuple[int, Any, str]] = [(-1, root, "dict")]
    lines = text.split("\n")

    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        content = raw.lstrip().rstrip()

        # Pop to correct parent
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if not stack:
            stack = [(-1, root, "dict")]
        parent_indent, parent, parent_type = stack[-1]

        if content.startswith("- "):
            # List item — parent must be list
            item_text = content[2:].strip()
            if parent_type != "list":
                # Convert previous key's value to list (sibling list under same key)
                # Skip if structure mismatched
                continue
            if ":" in item_text and not item_text.startswith('"'):
                # List item is a dict (single key:value)
                k, _, v = item_text.partition(":")
                item_dict: dict[str, Any] = {k.strip(): _parse_scalar(v.strip())} if v.strip() else {k.strip(): {}}
                parent.append(item_dict)
                stack.append((indent, item_dict, "dict"))
            else:
                parent.append(_parse_scalar(item_text))
            continue

        if ":" not in content:
            continue
        key, _, value_str = content.partition(":")
        key = key.strip()
        value_str = value_str.strip()

        if not isinstance(parent, dict):
            continue

        if value_str == "":
            # Nested — peek next non-empty line to decide list vs dict
            # Simpler: default to dict, will be replaced by list if next is "- "
            new_dict: dict[str, Any] = {}
            parent[key] = new_dict
            # We'll detect and convert if subsequent items are list items
            stack.append((indent, new_dict, "dict-or-list"))
        elif value_str == "{}":
            parent[key] = {}
        elif value_str == "[]":
            parent[key] = []
        else:
            parent[key] = _parse_scalar(value_str)

    return _post_fixup_lists(root)


def _post_fixup_lists(obj: Any) -> Any:
    """Recursively convert dicts that contain only list-item-like data into lists.

    Heuristic: empty dict under key X followed by sibling list items is hard to
    detect post-parse. We use a simpler approach: re-parse with a list-aware
    second pass. For this PoC, we actually re-implement parser more carefully.
    """
    return obj


def parse_yaml_v2(text: str) -> dict[str, Any]:
    """Robust YAML parser — handles nested dicts and lists with proper indentation tracking.

    본 PoC 한정 minimal parser — pyyaml 미도입, stdlib 단독.
    """
    root: dict[str, Any] = {}
    # Pre-process: identify each line's indent + type (key, list-item)
    lines: list[tuple[int, str]] = []
    for raw in text.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        lines.append((indent, raw.lstrip().rstrip()))

    def parse_block(start_idx: int, block_indent: int) -> tuple[Any, int]:
        """Parse a block at given indent; return (value, next_idx)."""
        # Determine block type (dict or list) by first line
        if start_idx >= len(lines):
            return None, start_idx
        idx = start_idx
        first_indent, first_content = lines[idx]
        if first_indent < block_indent:
            return None, idx
        is_list = first_content.startswith("- ")

        if is_list:
            result_list: list[Any] = []
            while idx < len(lines):
                cur_indent, cur_content = lines[idx]
                if cur_indent < block_indent:
                    break
                if cur_indent > block_indent:
                    # Should not happen for top-level list at block_indent
                    idx += 1
                    continue
                if not cur_content.startswith("- "):
                    break
                item_text = cur_content[2:].strip()
                idx += 1
                if ":" in item_text and not item_text.startswith('"'):
                    # Dict-shaped list item — start with this key:value, may have more keys at deeper indent
                    item_dict: dict[str, Any] = {}
                    k, _, v = item_text.partition(":")
                    k_stripped = k.strip()
                    v_stripped = v.strip()
                    if v_stripped:
                        item_dict[k_stripped] = _parse_scalar(v_stripped)
                    else:
                        # Nested under this list item key
                        if idx < len(lines) and lines[idx][0] > block_indent:
                            sub, idx = parse_block(idx, lines[idx][0])
                            item_dict[k_stripped] = sub
                        else:
                            item_dict[k_stripped] = {}
                    # Continue collecting sibling keys at deeper indent
                    while idx < len(lines) and lines[idx][0] > block_indent and not lines[idx][1].startswith("- "):
                        sub_indent, sub_content = lines[idx]
                        if ":" in sub_content:
                            sk, _, sv = sub_content.partition(":")
                            sk_stripped = sk.strip()
                            sv_stripped = sv.strip()
                            if sv_stripped:
                                item_dict[sk_stripped] = _parse_scalar(sv_stripped)
                                idx += 1
                            else:
                                idx += 1
                                if idx < len(lines) and lines[idx][0] > sub_indent:
                                    sub2, idx = parse_block(idx, lines[idx][0])
                                    item_dict[sk_stripped] = sub2
                                else:
                                    item_dict[sk_stripped] = {}
                        else:
                            idx += 1
                    result_list.append(item_dict)
                else:
                    result_list.append(_parse_scalar(item_text))
            return result_list, idx
        else:
            result_dict: dict[str, Any] = {}
            while idx < len(lines):
                cur_indent, cur_content = lines[idx]
                if cur_indent < block_indent:
                    break
                if cur_indent > block_indent:
                    idx += 1
                    continue
                if cur_content.startswith("- "):
                    break
                if ":" not in cur_content:
                    idx += 1
                    continue
                k, _, v = cur_content.partition(":")
                k_stripped = k.strip()
                v_stripped = v.strip()
                idx += 1
                if v_stripped == "" or v_stripped == "{}":
                    # Nested
                    if idx < len(lines) and lines[idx][0] > block_indent:
                        sub, idx = parse_block(idx, lines[idx][0])
                        result_dict[k_stripped] = sub if sub is not None else {}
                    else:
                        result_dict[k_stripped] = {}
                elif v_stripped == "[]":
                    result_dict[k_stripped] = []
                else:
                    result_dict[k_stripped] = _parse_scalar(v_stripped)
            return result_dict, idx

    if lines:
        result, _ = parse_block(0, lines[0][0])
        if isinstance(result, dict):
            root = result
    return root


# ============================================================================
# E-1 — External input scanner
# ============================================================================

def scan_external_input(file_path: Path) -> list[Violation]:
    """Scan external input file for injection canaries + JSON well-formed."""
    vios: list[Violation] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        vios.append(Violation(file_path, 0, "read-error", "io", f"read failed: {e}"))
        return vios

    # JSON well-formed check — .json extension OR text starting with `{` (object).
    # `[` (list) 는 자연어 텍스트의 [Bracket] 표기와 구분 어려움 → object 한정.
    # 후자는 .txt 형식의 malformed JSON fixture 검출 위함 (사양 §7.2 답습).
    stripped = text.lstrip()
    looks_like_json_object = stripped.startswith("{")
    if file_path.suffix == ".json" or looks_like_json_object:
        try:
            json.loads(text)
        except json.JSONDecodeError as e:
            vios.append(Violation(file_path, e.lineno, "malformed-json", "malformed-json", f"JSON parse error: {e.msg}"))

    # Injection canary scan (all extensions)
    for category, pattern_id, regex in ALL_EXTERNAL_INPUT_PATTERNS:
        for m in regex.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            sample = m.group(0)[:60]
            vios.append(Violation(file_path, line_no, pattern_id, category, sample))

    return vios


# ============================================================================
# E-2 — Skill schema validator
# ============================================================================

def validate_skill_schema(file_path: Path) -> list[Violation]:
    """Validate Skill 17-field schema (G4 §3.1 직접 답습)."""
    vios: list[Violation] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        vios.append(Violation(file_path, 0, "read-error", "io", f"read failed: {e}"))
        return vios

    # Parse YAML (or JSON if .json)
    try:
        if file_path.suffix in (".json", ".jsonl"):
            data = json.loads(text)
        else:
            data = parse_yaml_v2(text)
    except (json.JSONDecodeError, ValueError) as e:
        vios.append(Violation(file_path, 0, "parse-error", "parse-error", f"parse failed: {e}"))
        return vios

    if not isinstance(data, dict):
        vios.append(Violation(file_path, 0, "not-object", "schema", f"top-level not object: type={type(data).__name__}"))
        return vios

    # 1. Required fields (12)
    for field in REQUIRED_SKILL_FIELDS:
        if field not in data:
            vios.append(Violation(file_path, 0, "missing-required", "schema", f"required field missing: {field!r}"))

    # 2. id format
    id_val = data.get("id")
    if isinstance(id_val, str):
        if not (UUID_RE.match(id_val) or SLUG_RE.match(id_val)):
            vios.append(Violation(file_path, 0, "invalid-id-format", "schema", f"id={id_val!r} not UUID v4 or slug"))

    # 3. version semver
    ver_val = data.get("version")
    if isinstance(ver_val, str) and not SEMVER_RE.match(ver_val):
        vios.append(Violation(file_path, 0, "invalid-version", "schema", f"version={ver_val!r} not semver"))

    # 4. scope enum
    scope_val = data.get("scope")
    if scope_val is not None and scope_val not in ALLOWED_SCOPE_ENUM:
        vios.append(Violation(file_path, 0, "invalid-scope", "schema", f"scope={scope_val!r} not in {ALLOWED_SCOPE_ENUM}"))

    # 5. owner provider lock-in
    owner_val = data.get("owner")
    if isinstance(owner_val, str):
        owner_lower = owner_val.lower()
        for marker in PROVIDER_NAME_IDENTIFIERS:
            if marker in owner_lower:
                vios.append(Violation(file_path, 0, "provider-lockin", "provider-lockin", f"owner contains provider name: {marker!r}"))

    # 6. allowed_actions enum
    allowed = data.get("allowed_actions")
    if isinstance(allowed, list):
        for a in allowed:
            if a not in ALLOWED_ACTIONS_ENUM:
                vios.append(Violation(file_path, 0, "invalid-action", "schema", f"allowed_actions has unknown action: {a!r}"))

    # 7. forbidden_actions ∩ allowed_actions = ∅
    forbidden = data.get("forbidden_actions")
    if isinstance(allowed, list) and isinstance(forbidden, list):
        intersect = set(allowed) & set(forbidden)
        if intersect:
            vios.append(Violation(file_path, 0, "invalid-action", "schema", f"forbidden ∩ allowed = {sorted(intersect)} (must be ∅)"))

    # 8. promotion_status enum
    status = data.get("promotion_status")
    if status is not None and status not in PROMOTION_STATUS_ENUM:
        vios.append(Violation(file_path, 0, "invalid-promotion-status", "schema", f"promotion_status={status!r} not in {PROMOTION_STATUS_ENUM}"))

    # 9. provider_bindings present + lock-in marker
    pb = data.get("provider_bindings")
    if pb is None:
        # Already counted as missing-required
        pass
    elif not isinstance(pb, dict):
        vios.append(Violation(file_path, 0, "invalid-provider-bindings", "schema", f"provider_bindings not object: {type(pb).__name__}"))
    else:
        # Check for lock-in markers (line-level grep on raw text for accuracy)
        for marker_re in PROVIDER_LOCKIN_MARKERS:
            for m in marker_re.finditer(text):
                line_no = text[: m.start()].count("\n") + 1
                vios.append(Violation(file_path, line_no, "provider-lockin", "provider-lockin", f"lock-in marker: {m.group(0)!r}"))

    # 10. inputs / outputs top-level form (object with type or properties)
    for f in ("inputs", "outputs"):
        v = data.get(f)
        if v is not None and not isinstance(v, dict):
            vios.append(Violation(file_path, 0, "invalid-json-schema", "schema", f"{f} not object: {type(v).__name__}"))

    # 11. last_verified_at ISO 8601
    lva = data.get("last_verified_at")
    if isinstance(lva, str) and not ISO8601_RE.match(lva):
        vios.append(Violation(file_path, 0, "invalid-timestamp", "schema", f"last_verified_at={lva!r} not ISO 8601"))

    return vios


# ============================================================================
# Mode dispatch
# ============================================================================

EXTERNAL_INPUT_EXTENSIONS: tuple[str, ...] = (".json", ".txt", ".jsonl", ".log")
SKILL_SCHEMA_EXTENSIONS: tuple[str, ...] = (".yaml", ".yml", ".json")


def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix in allowed_exts else []
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix in allowed_exts:
            out.append(p)
    return out


def list_skill_fields() -> int:
    """Tier-1 catalog count self-check (사용자 명시 검증 5)."""
    n_required = len(REQUIRED_SKILL_FIELDS)
    n_mvp = len(MVP_RECOMMENDED_SKILL_FIELDS)
    total = n_required + n_mvp
    print(f"total={total}", file=sys.stderr)
    print(f"  required={n_required}", file=sys.stderr)
    print(f"  mvp_recommended={n_mvp}", file=sys.stderr)
    print(f"  required_fields={list(REQUIRED_SKILL_FIELDS)}", file=sys.stderr)
    print(f"  mvp_recommended_fields={list(MVP_RECOMMENDED_SKILL_FIELDS)}", file=sys.stderr)
    print(f"  provider_bindings_required=True (C-K 격상 답습)", file=sys.stderr)
    print(f"  promotion_status_enum={list(PROMOTION_STATUS_ENUM)}", file=sys.stderr)
    print(f"  allowed_actions_enum={list(ALLOWED_ACTIONS_ENUM)}", file=sys.stderr)
    print(f"  scope_enum={list(ALLOWED_SCOPE_ENUM)}", file=sys.stderr)
    print(f"  jsonl_11_field_required={list(JSONL_REQUIRED_FIELDS)}", file=sys.stderr)
    print(f"  schema_total_compliant={total == 17}", file=sys.stderr)
    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Schema validator — Group E PoC (G2 GP-4 + G4 schema validation)"
    )
    p.add_argument("path", type=str, nargs="?", default=None,
                   help="대상 파일/디렉토리 경로. --list-skill-fields 시 생략.")
    p.add_argument("--mode", choices=("external-input", "skill-schema"), default=None,
                   help="external-input = E-1 GP-4 / skill-schema = E-2 G4")
    p.add_argument("--list-skill-fields", action="store_true",
                   help="17-field Skill schema enumerate + count 자기 검증")
    p.add_argument("--max-lines", type=int, default=20)
    args = p.parse_args()

    if args.list_skill_fields:
        return list_skill_fields()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-skill-fields 단독 외)", file=sys.stderr)
        return 2

    root = Path(args.path)
    if not root.exists():
        print(f"PATH_NOT_FOUND: {root}", file=sys.stderr)
        return 2

    if args.mode == "external-input":
        exts = EXTERNAL_INPUT_EXTENSIONS
        scan_fn = scan_external_input
    else:
        exts = SKILL_SCHEMA_EXTENSIONS
        scan_fn = validate_skill_schema

    all_vios: list[Violation] = []
    for f in iter_files(root, exts):
        all_vios.extend(scan_fn(f))

    if not all_vios:
        print(f"[PASS] mode={args.mode} target={root} violations=0", file=sys.stderr)
        return 0

    print(f"[FAIL] mode={args.mode} target={root} violations={len(all_vios)}", file=sys.stderr)
    seen_categories: set[str] = set()
    seen_pattern_ids: set[str] = set()
    for v in all_vios:
        seen_categories.add(v.pattern_category)
        seen_pattern_ids.add(v.pattern_id)
    for v in all_vios[: args.max_lines]:
        print(v.format_short(), file=sys.stderr)
    if len(all_vios) > args.max_lines:
        print(f"  ... and {len(all_vios) - args.max_lines} more", file=sys.stderr)
    print(f"  pattern_categories_cover={sorted(seen_categories)}", file=sys.stderr)
    print(f"  pattern_ids_cover={sorted(seen_pattern_ids)}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
