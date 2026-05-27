#!/usr/bin/env python3
"""Secret scanner — Group D PoC (G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction).

답습 출처:
  - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양)
  - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — Tier-1 42 catalog + baseline 5)
  - docker/r4-1-poc/r4_1_poc.py line 51~213 (Tier-1 42 patterns + baseline 5 직접 답습)
  - docs/architecture/governance-preconditions.md §4 (GP-2) + §5 (GP-3)
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)

핵심 강제 조건 (사용자 명시 답습):
  - R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습 (변경 0건)
  - Prefix 36 (baseline 5 + Tier-1 prefix 31) + 추가 regex 7 (H-A/B/C/E/F/G/K) + alternation 2 (H-J/H-L key 기반)
  - H-J / H-L 직접 등록 제외 (alternation 채택, R-4.1 §4.2 답습)
  - Tier-2 / Tier-3 catalog 확장 0건
  - 외부 의존성 0건 (custom scanner 단독, gitleaks/detect-secrets 미도입)

Mode (사용자 명시):
  --mode scan-source : code-side secret 검출 (D-1 GP-3 Credential/Secret Hygiene)
  --mode scan-log    : redaction 후 잔존 secret 검출 (D-2 GP-2 Egress Redaction)

  본 PoC = 형식적 검출 layer 한정. Hermes 컨테이너 chmod / inotify (R1-2) =
  Hermes upstream 영역, 본 PoC 미진입 (사용자 명시 #6).

종료 코드:
  0 = 위반 0건 (PASS)
  1 = ≥1 위반 검출 (FAIL — D-1 secret 검출 / D-2 잔존 leak 검출)
  2 = 입력 오류 (path 부재 등)

알려진 한계 (사용자 명시 — 사양 §8):
  - base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)
"""
from __future__ import annotations

import argparse
import dataclasses
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

# ============================================================================
# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습
#
# 형식: (id, source, category, vendor, regex)
#   - id: BL-N (baseline) 또는 T1-NNN (Tier-1)
#   - source: Hermes 측 출처 식별자
#   - category: prefix-baseline / prefix / regex / alternation
#   - vendor: 사람이 읽을 수 있는 vendor/유형 라벨
#   - regex: scanner 등록용 정규식 문자열
# ============================================================================

# Baseline 5 prefix (R-2 PoC 보존 — R-4.1 §4.1)
BASELINE_PREFIX: list[tuple[str, str, str, str, str]] = [
    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
     r"sk-ant-[A-Za-z0-9_-]{10,}"),
    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
     r"sk-[A-Za-z0-9_-]{10,}"),
    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
     r"ghp_[A-Za-z0-9]{10,}"),
    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
     r"AKIA[A-Z0-9]{16}"),
    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
     r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]

# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
PREFIX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-001", "Hermes #3", "prefix", "GitHub PAT (fine-grained)",
     r"github_pat_[A-Za-z0-9_]{10,}"),
    ("T1-002", "Hermes #4", "prefix", "GitHub OAuth access token",
     r"gho_[A-Za-z0-9]{10,}"),
    ("T1-003", "Hermes #5", "prefix", "GitHub user-to-server",
     r"ghu_[A-Za-z0-9]{10,}"),
    ("T1-004", "Hermes #6", "prefix", "GitHub server-to-server",
     r"ghs_[A-Za-z0-9]{10,}"),
    ("T1-005", "Hermes #7", "prefix", "GitHub refresh token",
     r"ghr_[A-Za-z0-9]{10,}"),
    ("T1-006", "Hermes #9", "prefix", "Google API keys",
     r"AIza[A-Za-z0-9_-]{30,}"),
    ("T1-007", "Hermes #10", "prefix", "Perplexity",
     r"pplx-[A-Za-z0-9]{10,}"),
    ("T1-008", "Hermes #11", "prefix", "Fal.ai",
     r"fal_[A-Za-z0-9_-]{10,}"),
    ("T1-009", "Hermes #12", "prefix", "Firecrawl",
     r"fc-[A-Za-z0-9]{10,}"),
    ("T1-010", "Hermes #13", "prefix", "BrowserBase",
     r"bb_live_[A-Za-z0-9_-]{10,}"),
    ("T1-011", "Hermes #14", "prefix", "Codex encrypted tokens",
     r"gAAAA[A-Za-z0-9_=-]{20,}"),
    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
     r"sk_live_[A-Za-z0-9]{10,}"),
    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
     r"sk_test_[A-Za-z0-9]{10,}"),
    ("T1-014", "Hermes #18", "prefix", "Stripe restricted key",
     r"rk_live_[A-Za-z0-9]{10,}"),
    ("T1-015", "Hermes #19", "prefix", "SendGrid API key",
     r"SG\.[A-Za-z0-9_-]{10,}"),
    ("T1-016", "Hermes #20", "prefix", "HuggingFace token",
     r"hf_[A-Za-z0-9]{10,}"),
    ("T1-017", "Hermes #21", "prefix", "Replicate API token",
     r"r8_[A-Za-z0-9]{10,}"),
    ("T1-018", "Hermes #22", "prefix", "npm access token",
     r"npm_[A-Za-z0-9]{10,}"),
    ("T1-019", "Hermes #23", "prefix", "PyPI API token",
     r"pypi-[A-Za-z0-9_-]{10,}"),
    ("T1-020", "Hermes #24", "prefix", "DigitalOcean PAT",
     r"dop_v1_[A-Za-z0-9]{10,}"),
    ("T1-021", "Hermes #25", "prefix", "DigitalOcean OAuth",
     r"doo_v1_[A-Za-z0-9]{10,}"),
    ("T1-022", "Hermes #26", "prefix", "AgentMail API key",
     r"am_[A-Za-z0-9_-]{10,}"),
    ("T1-023", "Hermes #27", "prefix", "ElevenLabs TTS key",
     r"sk_[A-Za-z0-9_]{10,}"),
    ("T1-024", "Hermes #28", "prefix", "Tavily search API",
     r"tvly-[A-Za-z0-9]{10,}"),
    ("T1-025", "Hermes #29", "prefix", "Exa search API",
     r"exa_[A-Za-z0-9]{10,}"),
    ("T1-026", "Hermes #30", "prefix", "Groq Cloud API key",
     r"gsk_[A-Za-z0-9]{10,}"),
    ("T1-027", "Hermes #31", "prefix", "Matrix access token",
     r"syt_[A-Za-z0-9]{10,}"),
    ("T1-028", "Hermes #32", "prefix", "RetainDB API key",
     r"retaindb_[A-Za-z0-9]{10,}"),
    ("T1-029", "Hermes #33", "prefix", "Hindsight API key",
     r"hsk-[A-Za-z0-9]{10,}"),
    ("T1-030", "Hermes #34", "prefix", "Mem0 Platform API key",
     r"mem0_[A-Za-z0-9]{10,}"),
    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
     r"brv_[A-Za-z0-9]{10,}"),
]

# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2"),
    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
    ("T1-035", "Hermes H-E", "regex", "Private key block",
     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----"),
    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)"),
    ("T1-037", "Hermes H-G", "regex", "JWT token",
     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}"),
    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@"),
]

# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
    # (b1-PC1-D6-false-positives) 합의 2026-05-27 APPROVE WITH CONDITIONS (R-1 BLOCKING 흡수)
    # (b1-PC1-D6-fp-edge-extensions) 합의 2026-05-27 APPROVE (단축 + codex cross-vendor, semicolon + fragment 확장)
    # word boundary `(?:^|[?&\s'\";#])` prefix — Python keyword arg FP 해소 + quoted body literal cover + Cookie semicolon + OAuth fragment cover
    # `(` paren delimiter 추가 0 = `sort(key=...)` / `WorkerResult(exit_code=...)` FP 재발 회피 (codex N-4 답습)
    # carry-over: (b1-PC1-D6-ast-context) AST SAFE_CONTEXT
    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
]

ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
)
"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""

# Compiled regex objects (모듈 import 시 1회 컴파일)
COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
    (pid, src, cat, vendor, re.compile(rgx))
    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
]

# 본 PoC 직접 등록 제외 (R-4.1 §4.2 답습 — alternation 채택, H-J/H-L 직접 등록 false-positive 회피)
SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})

# Redaction marker exclusion (scan-log mode 전용 — GP-2 D-2 contract 답습).
# 사양 §0 — D-2 = "redaction 후 잔존 secret 검증". 본 marker 가 매칭 substring 전체를
# 차지하면 *정상 redacted output* 로 분류, 위반 미카운트 (FP 회피).
REDACTION_MARKER_RE: re.Pattern[str] = re.compile(
    r"(?i)(\[REDACTED\]|\[FILTERED\]|\[MASKED\]|<REDACTED>|<MASKED>|<<masked>>|\*{5,})"
)

# Scan 대상 file extension (사양 §4.1~§4.2 답습)
SCAN_SOURCE_EXTENSIONS: tuple[str, ...] = (
    ".py", ".json", ".yaml", ".yml", ".toml", ".sh", ".bash",
    ".env", ".ini", ".cfg", ".pem", ".key", ".txt", ".md",
)
SCAN_LOG_EXTENSIONS: tuple[str, ...] = (".txt", ".log", ".json", ".jsonl", ".md", ".pem")


@dataclass(frozen=True)
class Violation:
    """Single secret detection."""

    file: Path
    line: int
    pattern_id: str
    pattern_source: str
    pattern_category: str
    pattern_vendor: str
    matched_text: str

    def format_short(self) -> str:
        # Truncate matched_text to avoid leaking full canary in CI log (defensive)
        sample = self.matched_text[:30] + ("..." if len(self.matched_text) > 30 else "")
        return (
            f"{self.file}:{self.line}:{self.pattern_id}:"
            f"{self.pattern_category}:{self.pattern_vendor}: {sample!r}"
        )


def is_redaction_marker_match(matched_text: str) -> bool:
    """Scan-log mode 한정 — 매칭 텍스트가 redaction marker 만 포함하면 정상 redacted (FP 회피).

    GP-2 D-2 contract — 'redaction 후 잔존 secret 검증' (사양 §0).
    예: `OPENAI_API_KEY=[REDACTED]` 의 H-A regex 매칭은 [REDACTED] marker → 위반 미카운트.
    """
    return REDACTION_MARKER_RE.search(matched_text) is not None


def scan_text(text: str, file_path: Path, mode: str | None = None) -> list[Violation]:
    """Apply all 45 patterns to text and return violations.

    Line number = 1-indexed (file::line 표기 답습).
    mode='scan-log' 시 redaction marker 매칭은 위반 미카운트 (FP 회피, 사양 §0).
    """
    vios: list[Violation] = []
    for pid, src, cat, vendor, pattern in COMPILED_PATTERNS:
        if pid in SKIP_DIRECT_REGISTER:
            continue
        for m in pattern.finditer(text):
            matched = m.group(0)
            if mode == "scan-log" and is_redaction_marker_match(matched):
                continue
            line_no = text[: m.start()].count("\n") + 1
            vios.append(
                Violation(
                    file=file_path,
                    line=line_no,
                    pattern_id=pid,
                    pattern_source=src,
                    pattern_category=cat,
                    pattern_vendor=vendor,
                    matched_text=matched,
                )
            )
    return vios


def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:
    """Recursively iter target files under root, filtered by extension."""
    if root.is_file():
        return [root] if root.suffix in allowed_exts else []
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix in allowed_exts:
            out.append(p)
    return out


def scan_path(root: Path, mode: str) -> list[Violation]:
    """Scan all matching files under root and return aggregated violations."""
    if mode == "scan-source":
        exts = SCAN_SOURCE_EXTENSIONS
    elif mode == "scan-log":
        exts = SCAN_LOG_EXTENSIONS
    else:
        raise ValueError(f"unknown mode: {mode!r}")

    vios: list[Violation] = []
    for file_path in iter_files(root, exts):
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"READ_ERROR: {file_path}: {e}", file=sys.stderr)
            continue
        vios.extend(scan_text(text, file_path, mode=mode))
    return vios


def list_patterns() -> int:
    """Print Tier-1 catalog summary (사용자 명시 검증 5 — Tier-1 pattern count 자기 검증)."""
    n_baseline = len(BASELINE_PREFIX)
    n_prefix = len(PREFIX_PATTERNS)
    n_regex = len(REGEX_PATTERNS)
    n_alt = len(ALTERNATION_PATTERNS)
    total_registered = n_baseline + n_prefix + n_regex + n_alt
    n_active = total_registered - len(SKIP_DIRECT_REGISTER & {p[0] for p in ALL_PATTERNS})

    print(f"registered_patterns_count={total_registered}", file=sys.stderr)
    print(f"  baseline_prefix={n_baseline}", file=sys.stderr)
    print(f"  tier1_prefix={n_prefix}", file=sys.stderr)
    print(f"  tier1_regex={n_regex}", file=sys.stderr)
    print(f"  tier1_alternation={n_alt}", file=sys.stderr)
    print(f"  skip_direct_register={sorted(SKIP_DIRECT_REGISTER)}", file=sys.stderr)
    print(f"  active_patterns={n_active}", file=sys.stderr)
    print(
        f"  tier1_42_catalog_compliant={total_registered >= 42}", file=sys.stderr
    )

    for pid, src, cat, vendor, rgx in ALL_PATTERNS:
        flag = " (skipped)" if pid in SKIP_DIRECT_REGISTER else ""
        print(f"  {pid}\t{cat}\t{vendor}\t{src}{flag}", file=sys.stderr)

    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Secret scanner — Group D PoC (G2 GP-3 + GP-2, R-4.1 Tier-1 42 catalog 답습)"
    )
    p.add_argument(
        "path", type=str, nargs="?", default=None,
        help="대상 파일/디렉토리 경로 (재귀). --list-patterns 시 생략 가능."
    )
    p.add_argument(
        "--mode", choices=("scan-source", "scan-log"), default=None,
        help=(
            "scan-source = code-side secret 검출 (D-1). "
            "scan-log = redaction 후 잔존 secret 검출 (D-2)."
        ),
    )
    p.add_argument(
        "--list-patterns", action="store_true",
        help="등록된 45 patterns enumerate + Tier-1 42 catalog count 자기 검증",
    )
    p.add_argument(
        "--max-lines", type=int, default=20,
        help="violation 출력 최대 라인 수 (default 20, CI log 폭주 방지)",
    )
    args = p.parse_args()

    if args.list_patterns:
        return list_patterns()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-patterns 단독 모드 외)", file=sys.stderr)
        return 2

    root = Path(args.path)
    if not root.exists():
        print(f"PATH_NOT_FOUND: {root}", file=sys.stderr)
        return 2

    vios = scan_path(root, args.mode)

    if not vios:
        print(f"[PASS] mode={args.mode} target={root} violations=0", file=sys.stderr)
        return 0

    print(
        f"[FAIL] mode={args.mode} target={root} violations={len(vios)}",
        file=sys.stderr,
    )
    seen_categories: set[str] = set()
    for v in vios[: args.max_lines]:
        seen_categories.add(v.pattern_category)
        print(v.format_short(), file=sys.stderr)
    if len(vios) > args.max_lines:
        print(f"  ... and {len(vios) - args.max_lines} more", file=sys.stderr)
    print(
        f"  pattern_categories_cover={sorted(seen_categories)}", file=sys.stderr
    )

    return 1


if __name__ == "__main__":
    sys.exit(_cli())
