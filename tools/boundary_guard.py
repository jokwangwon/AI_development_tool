#!/usr/bin/env python3
"""Boundary guard — Group G PoC (G3 + G4 통합 — Skill escalation + 합의 자기참조 차단 + Memory/Skill boundary 4 금지).

답습 출처:
  - docs/phase0/g3-g4-boundary-guard-poc.md (본 PoC 사양)
  - docs/architecture/hermes-not-root-of-trust-runtime.md §3.3 (Skill escalation) /
    §4 (합의 인프라 순환 권위) / §4.2 자기참조 차단 원칙 / §4.3 합의 형태 매트릭스
  - docs/architecture/provider-agnostic-memory-skill-design.md §5.2 (4 금지 사항)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §C-N §2.3
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 + §2.4 T1/T2/T3
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.2 (11-field schema enum) / §2.12
  - tools/jsonl_hash_chain.py (Group C — `validate_schema` + ENUMs import 직접)
  - tools/evidence_pass_gate.py (Group B — Hermes-originated marker + governance PASS anchor 패턴 답습)
  - tools/schema_validator.py (Group E — `ALLOWED_ACTIONS_ENUM` + `parse_yaml_v2` import 직접)

핵심 강제 조건 (사용자 명시 답습):
  - stdlib `re` + `json` + `dataclasses` 단독 (외부 의존성 0건)
  - pydantic / jsonschema / pyyaml / Docker SDK / git2 미도입 (사양 §2 답습)
  - runtime hook 미진입 (Skill wrapper / Memory write blocker / promotion hook 0건)
  - 실 git commit author / 외부 LLM 자동 호출 / production data 0건

Mode (사용자 명시):
  --mode skill-escalation         : G-1 — Skill yaml allowed_actions + audit log 매트릭스 (G3 §3.3)
  --mode consensus-self-reference : G-2 — Hermes-originated × governance PASS + 단독 합의 시도 (G3 §4)
  --mode memory-skill-boundary    : G-3 — G4 §5.2 4 금지 정적 검출

종료 코드:
  0 = 위반 0건 (PASS)
  1 = ≥1 위반 검출 (FAIL)
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
    parse_jsonl,
    validate_schema as validate_jsonl_schema,
)
from schema_validator import (  # type: ignore[import-not-found]
    ALLOWED_ACTIONS_ENUM,
    PROMOTION_STATUS_ENUM,
    parse_yaml_v2,
)

# ============================================================================
# G-1 — Skill Permission Escalation (G3 §3.3 답습)
# ============================================================================

# Policy-related action names that should NEVER appear in allowed_actions
# (G4 §5.2 #2 답습 — Skill 이 ADR / Constitution 우회 차단)
POLICY_WRITE_ACTIONS: tuple[str, ...] = (
    "policy_write", "adr_write", "constitution_write",
    "skill_self_approve", "memory_promote_global",
)

# ============================================================================
# G-2 — 합의 자기참조 차단 (G3 §4 답습)
# ============================================================================

# Hermes-originated marker patterns (Group B `evidence_pass_gate.py` 답습)
HERMES_ORIGINATED_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("hermes-marker-generated-by", re.compile(r"(?im)^Generated-by:\s*Hermes")),
    ("hermes-marker-agent-origin", re.compile(r"(?im)^Agent-Origin:\s*Hermes")),
    ("hermes-marker-authored-by", re.compile(r"(?im)^Authored-by:\s*Hermes")),
    ("hermes-marker-co-authored-by", re.compile(r"(?im)^Co-Authored-By:\s*Hermes")),
    ("hermes-marker-approved-by", re.compile(r"(?im)^Approved-by:\s*Hermes")),
    ("hermes-marker-signed-off-by", re.compile(r"(?im)^Signed-off-by:\s*Hermes")),
)

# Governance PASS anchor (Group B `evidence_pass_gate.py` 답습)
GOVERNANCE_PASS_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bGate\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bImplementation\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bImplementation/Runtime\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bDesign\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bDesign/Governance\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bAPPROVE\s+WITH\s+CONDITIONS\b", re.IGNORECASE),
    re.compile(r"^##\s+APPROVE\b", re.MULTILINE),
    re.compile(r"\bG[1-9]\w*\s+PASS\b"),
    re.compile(r"\bGP-\d+\s+PASS\b", re.IGNORECASE),
)

# Reviewer / 외부 LLM marker (G3 §4.4 — 단축 합의 / 풀 3+1 / 외부 LLM 의무 답습)
REVIEWER_MARKER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bReviewer-only\b", re.IGNORECASE),
    re.compile(r"풀\s*3\+1", re.IGNORECASE),
    re.compile(r"\bAgent\s+[ABC]\b"),
    re.compile(r"\b3\+1\s+합의\b", re.IGNORECASE),
)

EXTERNAL_LLM_MARKER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"외부\s*LLM", re.IGNORECASE),
    re.compile(r"\bcross-vendor\b", re.IGNORECASE),
    re.compile(r"\bGPT(-[0-9.]+)?\b", re.IGNORECASE),
    re.compile(r"\bGemini\b", re.IGNORECASE),
    re.compile(r"\bClaude\b\s*인접\s*컨텍스트", re.IGNORECASE),
)

# Hermes PMO 격상 / Hermes 정책 변경 결정 본문 (G3 §4.3 매트릭스 답습)
HERMES_POLICY_DECISION_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("hermes-pmo-promotion", re.compile(r"Hermes\s+PMO\s+격상", re.IGNORECASE)),
    ("hermes-policy-change", re.compile(r"Hermes\s+정책\s+변경", re.IGNORECASE)),
    ("redaction-policy-change", re.compile(r"redaction-policy\.yaml\s+(변경|update|modify)", re.IGNORECASE)),
)

# ============================================================================
# G-3 — Memory/Skill Boundary 4 금지 (G4 §5.2 답습)
# ============================================================================

# Boundary #1: Memory 가 policy 를 대체 — Memory entry content 의 정책 표현 grep
POLICY_EXPRESSION_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("policy-update-adr", re.compile(r"(?i)\bUPDATE\s+ADR(-\d+)?\b|\bMODIFY\s+ADR(-\d+)?\b|\bedit\s+ADR(-\d+)?\b")),
    ("policy-update-constitution", re.compile(r"(?i)\b(UPDATE|MODIFY|EDIT|REWRITE)\s+(THE\s+)?CONSTITUTION\b")),
    ("policy-disable-hermes", re.compile(r"(?i)\bDISABLE\s+HERMES\b|\bSTOP\s+HERMES\b|\bKILL\s+HERMES\b")),
    ("policy-bypass-redaction", re.compile(r"(?i)\bBYPASS\s+REDACTION\b|\bSKIP\s+REDACTION\b|\bDISABLE\s+REDACTION\b")),
    ("policy-elevate-permissions", re.compile(r"(?i)\bGRANT\s+ME\s+(ROOT|ADMIN|SUDO)\b|\bELEVATE\s+(MY\s+)?PERMISSIONS\b")),
    ("policy-force-pass", re.compile(r"(?i)\b(MARK|SET|FORCE)\s+(G[1-9][a-z]?\s+)?(AS\s+)?PASS(ED)?\b")),
)


@dataclass(frozen=True)
class Violation:
    """Single boundary violation (Group D/E 답습)."""

    file: Path
    line: int
    pattern_id: str
    pattern_category: str
    detail: str

    def format_short(self) -> str:
        sample = self.detail[:90] + ("..." if len(self.detail) > 90 else "")
        return f"{self.file}:{self.line}:{self.pattern_id}:{self.pattern_category}: {sample}"


# ============================================================================
# Mode 1: G-1 — Skill Permission Escalation
# ============================================================================

def scan_skill_yaml_for_escalation(file_path: Path) -> list[Violation]:
    """Validate skill yaml allowed_actions enum + policy_write detection."""
    vios: list[Violation] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
        data = parse_yaml_v2(text)
    except (OSError, ValueError) as e:
        vios.append(Violation(file_path, 0, "yaml-parse-error", "parse-error", f"parse failed: {e}"))
        return vios

    if not isinstance(data, dict):
        vios.append(Violation(file_path, 0, "yaml-not-object", "schema", f"top-level not object: {type(data).__name__}"))
        return vios

    allowed = data.get("allowed_actions")
    if isinstance(allowed, list):
        for a in allowed:
            if not isinstance(a, str):
                continue
            if a in POLICY_WRITE_ACTIONS:
                vios.append(Violation(
                    file_path, 0, "yaml-invalid-action", "skill-escalation",
                    f"policy-write action in allowed_actions: {a!r} (G4 §5.2 #2 답습 위반)"
                ))
            elif a not in ALLOWED_ACTIONS_ENUM:
                vios.append(Violation(
                    file_path, 0, "yaml-invalid-action", "skill-escalation",
                    f"unknown action in allowed_actions: {a!r} (not in {ALLOWED_ACTIONS_ENUM})"
                ))

    forbidden = data.get("forbidden_actions")
    if isinstance(allowed, list) and isinstance(forbidden, list):
        intersect = set(allowed) & set(forbidden)
        if intersect:
            vios.append(Violation(
                file_path, 0, "yaml-invalid-action", "skill-escalation",
                f"forbidden ∩ allowed = {sorted(intersect)} (must be ∅)"
            ))

    return vios


def scan_audit_log_for_escalation(file_path: Path) -> list[Violation]:
    """Validate audit log JSONL — each entry's `action` must be in the named skill's allowed_actions.

    Audit log fixture format (사양 §7.2 답습):
      Each line = JSON object with at least: skill_id, allowed_actions, action.
      If `action` not in `allowed_actions` → escalation violation.
    """
    vios: list[Violation] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        vios.append(Violation(file_path, 0, "read-error", "io", f"read failed: {e}"))
        return vios

    for line_no, raw in enumerate(text.split("\n"), start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            vios.append(Violation(file_path, line_no, "audit-parse-error", "parse-error", f"JSON parse: {e.msg}"))
            continue
        if not isinstance(obj, dict):
            continue
        allowed = obj.get("allowed_actions")
        action = obj.get("action")
        if not isinstance(allowed, list) or not isinstance(action, str):
            continue
        if action not in allowed:
            skill_id = obj.get("skill_id", "<unknown>")
            vios.append(Violation(
                file_path, line_no, "audit-log-escalation", "skill-escalation",
                f"skill={skill_id!r} called action={action!r} not in allowed={allowed}"
            ))

    return vios


def scan_skill_escalation(file_path: Path) -> list[Violation]:
    """Dispatch by extension."""
    if file_path.suffix in (".yaml", ".yml"):
        return scan_skill_yaml_for_escalation(file_path)
    if file_path.suffix in (".jsonl", ".json"):
        return scan_audit_log_for_escalation(file_path)
    return []


# ============================================================================
# Mode 2: G-2 — 합의 자기참조 차단
# ============================================================================

def scan_consensus_self_reference(file_path: Path) -> list[Violation]:
    """Detect Hermes-originated × governance PASS co-occurrence + Hermes-only consensus."""
    vios: list[Violation] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        vios.append(Violation(file_path, 0, "read-error", "io", f"read failed: {e}"))
        return vios

    # Find Hermes-originated markers
    hermes_hits: list[tuple[str, int]] = []
    for pid, regex in HERMES_ORIGINATED_PATTERNS:
        for m in regex.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            hermes_hits.append((pid, line_no))

    # Find governance PASS anchors
    governance_pass_present = any(p.search(text) for p in GOVERNANCE_PASS_PATTERNS)

    # Find Reviewer / external LLM markers
    reviewer_present = any(p.search(text) for p in REVIEWER_MARKER_PATTERNS)
    external_llm_present = any(p.search(text) for p in EXTERNAL_LLM_MARKER_PATTERNS)

    # Find Hermes PMO 격상 / Hermes 정책 변경 decision body
    policy_decision_hits: list[tuple[str, int]] = []
    for pid, regex in HERMES_POLICY_DECISION_PATTERNS:
        for m in regex.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            policy_decision_hits.append((pid, line_no))

    # Violation rule 1: Hermes-originated × governance PASS 공동 발생
    if hermes_hits and governance_pass_present:
        for pid, line_no in hermes_hits:
            vios.append(Violation(
                file_path, line_no, "hermes-self-consensus", "consensus-self-reference",
                f"Hermes-originated marker ({pid}) co-occurs with governance PASS"
            ))

    # Violation rule 2: Hermes-originated × Hermes PMO 격상 / Hermes 정책 변경 결정
    if hermes_hits and policy_decision_hits:
        for pid_h, line_h in hermes_hits:
            for pid_d, line_d in policy_decision_hits:
                vios.append(Violation(
                    file_path, line_d, "hermes-pmo-self-promotion", "consensus-self-reference",
                    f"Hermes-originated ({pid_h}) × policy decision ({pid_d}) = self-promotion"
                ))
                break  # one violation per Hermes marker is enough

    # Violation rule 3: Hermes-originated × Reviewer 부재 + 외부 LLM 부재 = 단독 합의 시도
    if hermes_hits and not reviewer_present and not external_llm_present:
        vios.append(Violation(
            file_path, hermes_hits[0][1], "hermes-self-consensus", "consensus-self-reference",
            "Hermes-originated marker present without Reviewer/external-LLM verification (단독 합의 시도)"
        ))

    return vios


# ============================================================================
# Mode 3: G-3 — Memory/Skill Boundary 4 금지
# ============================================================================

def scan_memory_skill_boundary(file_path: Path) -> list[Violation]:
    """JSONL ledger 의 4 금지 정적 검출."""
    vios: list[Violation] = []
    if file_path.suffix not in (".jsonl",):
        return vios

    try:
        entries, parse_vios = parse_jsonl(file_path)
    except OSError as e:
        vios.append(Violation(file_path, 0, "read-error", "io", f"read failed: {e}"))
        return vios

    for v in parse_vios:
        vios.append(Violation(
            file_path, v.entry_index + 1, "jsonl-parse-error", "parse-error",
            f"{v.violation_type}: {v.detail}"
        ))

    # Track id → first scope seen (for #3 session→global transition detection)
    id_to_scope: dict[str, str] = {}

    for idx, entry in enumerate(entries, start=1):
        # #1: Memory 가 policy 를 대체 — Memory entry content 정책 표현 grep
        if entry.get("type") == "memory":
            content = entry.get("content")
            content_text = json.dumps(content, ensure_ascii=False) if content is not None else ""
            for pid, regex in POLICY_EXPRESSION_PATTERNS:
                m = regex.search(content_text)
                if m:
                    vios.append(Violation(
                        file_path, idx, "memory-replaces-policy", "memory-skill-boundary",
                        f"entry[{idx}] memory content contains policy expr ({pid}): {m.group(0)[:60]!r}"
                    ))

        # #3: Session memory → Global memory 자동 승격
        entry_id = entry.get("id")
        scope = entry.get("scope")
        if isinstance(entry_id, str) and isinstance(scope, str):
            prev_scope = id_to_scope.get(entry_id)
            if prev_scope == "session" and scope == "global":
                vios.append(Violation(
                    file_path, idx, "session-to-global", "memory-skill-boundary",
                    f"entry[{idx}] id={entry_id!r} scope transition session → global (G4 §5.2 #3 위반)"
                ))
            id_to_scope[entry_id] = scope

        # #4: Hermes 가 skill 을 자기 승인 — agent: hermes × event: skill_approved/promoted
        agent = entry.get("agent")
        event = entry.get("event")
        if agent == "hermes" and event in ("skill_approved", "skill_promoted"):
            vios.append(Violation(
                file_path, idx, "hermes-self-approves", "memory-skill-boundary",
                f"entry[{idx}] agent=hermes × event={event!r} (G4 §5.2 #4 위반)"
            ))

    return vios


# ============================================================================
# Mode dispatch + file iteration
# ============================================================================

SKILL_ESCALATION_EXTENSIONS: tuple[str, ...] = (".yaml", ".yml", ".jsonl", ".json")
CONSENSUS_EXTENSIONS: tuple[str, ...] = (".md", ".txt")
BOUNDARY_EXTENSIONS: tuple[str, ...] = (".jsonl",)


def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix in allowed_exts else []
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix in allowed_exts:
            out.append(p)
    return out


def list_boundaries() -> int:
    """Self-check: enumerate boundaries + modes + 합의 매트릭스 (사용자 명시 검증 7)."""
    boundaries = (
        ("#1", "Memory 가 policy 를 대체"),
        ("#2", "Skill 이 ADR / Constitution 우회 (G-1 통합 답습)"),
        ("#3", "Session memory → Global memory 자동 승격"),
        ("#4", "Hermes 가 skill 을 자기 승인"),
    )
    modes = ("skill-escalation", "consensus-self-reference", "memory-skill-boundary")
    consensus_matrix = (
        ("Worker Agent 작업 분배", "T1", "Hermes 단독 OK"),
        ("Worker 출력 검증 (Tools)", "T1", "Tools 자동"),
        ("Skill 후보 제안", "T1", "Hermes 제안만"),
        ("Skill 등록", "T2", "사용자 명시 결정 필수"),
        ("Memory promotion (Project → Global)", "T2", "사용자 명시 결정 필수"),
        ("일반 합의 (패턴 동등성 등)", "T2", "단축 또는 풀 3+1"),
        ("G1b PASS 승격", "T2", "단축 (Reviewer-only) — 이미 발생"),
        ("G2 / G3 / G4 PASS", "T2", "단축 또는 풀 3+1"),
        ("Hermes PMO 격상", "T2 강화", "풀 3+1 + 외부 LLM 1+ 필수"),
        ("Hermes 정책 변경", "T3", "풀 3+1 + 외부 LLM 1+ 권장 + ADR Amendment"),
        ("Constitution / ADR 본문 갱신", "T3", "풀 3+1 + ADR Amendment"),
        ("Harness Gate 정의 자체 변경", "T3", "풀 3+1 + ADR Amendment"),
        ("G3 §4 / §9 본문 변경", "T3", "풀 3+1 + ADR Amendment"),
    )

    print(f"total_boundaries={len(boundaries)}", file=sys.stderr)
    for num, desc in boundaries:
        print(f"  {num} {desc}", file=sys.stderr)
    print(f"total_modes={len(modes)}", file=sys.stderr)
    for m in modes:
        print(f"  --mode {m}", file=sys.stderr)
    print(f"consensus_matrix_rows={len(consensus_matrix)}", file=sys.stderr)
    for decision, tier, form in consensus_matrix:
        print(f"  {decision} | {tier} | {form}", file=sys.stderr)

    print(f"hermes_originated_patterns={len(HERMES_ORIGINATED_PATTERNS)}", file=sys.stderr)
    print(f"governance_pass_anchors={len(GOVERNANCE_PASS_PATTERNS)}", file=sys.stderr)
    print(f"hermes_policy_decision_patterns={len(HERMES_POLICY_DECISION_PATTERNS)}", file=sys.stderr)
    print(f"policy_expression_patterns={len(POLICY_EXPRESSION_PATTERNS)}", file=sys.stderr)
    print(f"policy_write_actions={list(POLICY_WRITE_ACTIONS)}", file=sys.stderr)
    print(f"allowed_actions_enum={list(ALLOWED_ACTIONS_ENUM)}", file=sys.stderr)
    print(f"boundary_4_rules_compliant={len(boundaries) == 4}", file=sys.stderr)
    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Boundary guard — Group G PoC (G3 + G4 통합)"
    )
    p.add_argument("path", type=str, nargs="?", default=None,
                   help="대상 파일/디렉토리 경로. --list-boundaries 시 생략.")
    p.add_argument(
        "--mode",
        choices=("skill-escalation", "consensus-self-reference", "memory-skill-boundary"),
        default=None,
        help=("skill-escalation = G-1 (G3 §3.3) / "
              "consensus-self-reference = G-2 (G3 §4) / "
              "memory-skill-boundary = G-3 (G4 §5.2)"),
    )
    p.add_argument(
        "--list-boundaries", action="store_true",
        help="4 boundaries + 3 modes + 13 합의 매트릭스 row enumerate + count 자기 검증",
    )
    p.add_argument("--max-lines", type=int, default=20)
    args = p.parse_args()

    if args.list_boundaries:
        return list_boundaries()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-boundaries 단독 외)", file=sys.stderr)
        return 2

    root = Path(args.path)
    if not root.exists():
        print(f"PATH_NOT_FOUND: {root}", file=sys.stderr)
        return 2

    if args.mode == "skill-escalation":
        exts = SKILL_ESCALATION_EXTENSIONS
        scan_fn = scan_skill_escalation
    elif args.mode == "consensus-self-reference":
        exts = CONSENSUS_EXTENSIONS
        scan_fn = scan_consensus_self_reference
    else:
        exts = BOUNDARY_EXTENSIONS
        scan_fn = scan_memory_skill_boundary

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
