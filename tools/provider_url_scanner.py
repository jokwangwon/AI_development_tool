#!/usr/bin/env python3
"""Provider URL/model scanner — Group A 3차 PoC (G2 GP-5 Layer 1c).

답습 출처:
  - docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md (본 PoC 사양)
  - docs/architecture/llm-providers-design.md §9.3 (depcruise rule —
    `no-llm-via-httpx` + `no-model-name-in-code` *grep 보조* 영역)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md C-N §5
    (Layer 1 모법 ADR — Provider Liquidity 5-way Multi-layer Defense)
  - docs/decisions/ADR-008-hermes-adoption-decision.md 차단조건 #4
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
  - tools/provider_import_scanner.py (Group A 1차 — Layer 1a AST scanner)
  - tools/secret_scanner.py (Group D — Tier-1 catalog 정적 grep 답습 패턴)

Layer 책무 분리 (G2 GP-5 모법):
  - Layer 1a (Group A 1차): AST 5종 패턴 — `provider_import_scanner.py`
  - Layer 1b (Group A 2차): Transitive import — `.importlinter` (T-2)
  - Layer 1c (본 PoC, Group A 3차): URL endpoint + model name 직접 사용

핵심 강제 조건 (사용자 명시 답습):
  - stdlib `re` + `dataclasses` 단독 (외부 의존성 0건)
  - Tier-1 catalog 한정 (URL 10 + model 19+) — Tier-2/3 확장 0건
  - extension allowlist (yaml/yml/json/jsonl/toml/cfg/ini/md = config/docs)
  - comment line 부분 회피 (`#` / `//`) — multi-line block / docstring 별도 합의
  - 실 API key / 실 endpoint 호출 / production data 0건

Mode (사용자 명시):
  --mode url-endpoint : E-1 — provider API endpoint URL 직접 사용 차단
  --mode model-name   : E-2 — provider 모델 ID 하드코딩 차단 (yaml만 허용)

종료 코드:
  0 = 위반 0건 (PASS)
  1 = ≥1 위반 검출 (FAIL)
  2 = 입력 오류 (path 부재 등)
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# ============================================================================
# E-1 — URL Endpoint Tier-1 catalog (10 providers, llm-providers-design.md §9.3 답습)
# ============================================================================

URL_ENDPOINT_PATTERNS: tuple[tuple[str, str, re.Pattern[str]], ...] = (
    ("anthropic", "Anthropic API", re.compile(r"\bapi\.anthropic\.com\b")),
    ("openai", "OpenAI API", re.compile(r"\bapi\.openai\.com\b")),
    ("azure-openai", "Azure OpenAI", re.compile(r"\b[\w-]+\.openai\.azure\.com\b")),
    ("google-ai", "Google AI / Gemini", re.compile(r"\bgenerativelanguage\.googleapis\.com\b")),
    ("replicate", "Replicate", re.compile(r"\bapi\.replicate\.com\b")),
    ("perplexity", "Perplexity", re.compile(r"\bapi\.perplexity\.ai\b")),
    ("cohere", "Cohere", re.compile(r"\bapi\.cohere\.(?:ai|com)\b")),
    ("huggingface", "HuggingFace Inference",
     re.compile(r"\b(?:api-inference\.huggingface\.co|huggingface\.co/api)\b")),
    ("together", "Together AI", re.compile(r"\bapi\.together\.xyz\b")),
    ("openrouter", "OpenRouter", re.compile(r"\bopenrouter\.ai/api\b")),
)
"""(provider_id, vendor_label, regex) — 10 patterns. CI step 6 3 패턴 cover grep
   대상 = (anthropic / openai / google-ai)."""

# ============================================================================
# E-2 — Model Name Tier-1 catalog (19+ patterns, §9.3 "yaml만 허용" 답습)
# ============================================================================

MODEL_NAME_PATTERNS: tuple[tuple[str, str, re.Pattern[str]], ...] = (
    # Anthropic (5)
    ("anthropic-claude-opus", "Anthropic Claude Opus", re.compile(r"\bclaude-opus-[\w.-]+")),
    ("anthropic-claude-sonnet", "Anthropic Claude Sonnet", re.compile(r"\bclaude-sonnet-[\w.-]+")),
    ("anthropic-claude-haiku", "Anthropic Claude Haiku", re.compile(r"\bclaude-haiku-[\w.-]+")),
    ("anthropic-claude-3", "Anthropic Claude 3", re.compile(r"\bclaude-3-[\w.-]+")),
    ("anthropic-claude-2", "Anthropic Claude 2", re.compile(r"\bclaude-2[\w.-]*")),
    # OpenAI (5)
    ("openai-gpt-4", "OpenAI GPT-4", re.compile(r"\bgpt-4[\w.-]*")),
    ("openai-gpt-3-5", "OpenAI GPT-3.5", re.compile(r"\bgpt-3\.5[\w.-]*")),
    ("openai-gpt-4o", "OpenAI GPT-4o", re.compile(r"\bgpt-4o[\w.-]*")),
    ("openai-o1", "OpenAI o1", re.compile(r"\bo1-[\w.-]+")),
    ("openai-o3", "OpenAI o3", re.compile(r"\bo3-[\w.-]+")),
    # Google (3)
    ("google-gemini-1-5", "Google Gemini 1.5", re.compile(r"\bgemini-1\.5-[\w.-]+")),
    ("google-gemini-2", "Google Gemini 2.x", re.compile(r"\bgemini-2\.[\w.-]+")),
    ("google-gemini-pro", "Google Gemini Pro", re.compile(r"\bgemini-pro[\w.-]*")),
    # Meta (3)
    ("meta-llama", "Meta Llama (v1)", re.compile(r"\bllama-[\w.-]+")),
    ("meta-llama2", "Meta Llama 2", re.compile(r"\bllama2-[\w.-]+")),
    ("meta-llama3", "Meta Llama 3", re.compile(r"\bllama3-[\w.-]+")),
    # Mistral (3)
    ("mistral-mistral", "Mistral Mistral", re.compile(r"\bmistral-[\w.-]+")),
    ("mistral-mixtral", "Mistral Mixtral", re.compile(r"\bmixtral-[\w.-]+")),
    ("mistral-codestral", "Mistral Codestral", re.compile(r"\bcodestral-[\w.-]+")),
)
"""(model_id, vendor_label, regex) — 19 patterns. CI step 8 4 패턴 cover grep
   대상 = (claude / gpt / gemini / llama)."""

# ============================================================================
# Allowlist 정책 (사양 §6 답습)
# ============================================================================

URL_ENDPOINT_ALLOWLIST_EXT: tuple[str, ...] = (
    ".yaml", ".yml", ".json", ".jsonl", ".toml", ".cfg", ".ini", ".md",
)
"""8 ext — yaml/json/toml/ini/md = config/docs 허용."""

MODEL_NAME_ALLOWLIST_EXT: tuple[str, ...] = (
    ".yaml", ".yml", ".json", ".jsonl", ".md",
)
"""5 ext — §9.3 'yaml만 허용' 답습 (json/jsonl/md 도 config/docs 허용 확장)."""

# Source code extensions to scan (allowlist 외 위치)
SCAN_TARGET_EXT: tuple[str, ...] = (
    ".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".rb",
    ".java", ".kt", ".cpp", ".c", ".swift", ".scala", ".sh", ".bash",
)
"""src 코드 검출 대상 extension."""

# Comment line prefix (부분 회피)
COMMENT_PREFIXES: tuple[str, ...] = ("#", "//")
"""line-by-line comment 회피. multi-line block / docstring = 별도 합의."""


@dataclass(frozen=True)
class Violation:
    """Single hardcoding violation (Group A 1차 + Group D 답습)."""

    file: Path
    line: int
    pattern_id: str
    vendor: str
    matched_text: str

    def format_short(self) -> str:
        return (
            f"{self.file}:{self.line}:{self.pattern_id}:{self.vendor}: "
            f"{self.matched_text[:60]!r}"
        )


def is_comment_line(line: str) -> bool:
    """라인 단위 코멘트 회피 (Python `#` / JS·Go·Rust `//`)."""
    stripped = line.lstrip()
    return any(stripped.startswith(prefix) for prefix in COMMENT_PREFIXES)


def scan_text_for_patterns(
    text: str,
    file_path: Path,
    patterns: tuple[tuple[str, str, re.Pattern[str]], ...],
) -> list[Violation]:
    """Apply Tier-1 patterns to text; skip comment-prefixed lines."""
    vios: list[Violation] = []
    lines = text.split("\n")
    for line_no, line in enumerate(lines, start=1):
        if is_comment_line(line):
            continue
        for pid, vendor, regex in patterns:
            for m in regex.finditer(line):
                vios.append(Violation(
                    file=file_path, line=line_no,
                    pattern_id=pid, vendor=vendor,
                    matched_text=m.group(0),
                ))
    return vios


def iter_target_files(root: Path, allowlist_ext: tuple[str, ...]) -> list[Path]:
    """Recursive iterator — exclude allowlist extensions, include scan targets."""
    if root.is_file():
        if root.suffix in allowlist_ext:
            return []
        if root.suffix in SCAN_TARGET_EXT:
            return [root]
        return []
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix in allowlist_ext:
            continue
        if p.suffix in SCAN_TARGET_EXT:
            out.append(p)
    return out


def scan_path(root: Path, mode: str) -> list[Violation]:
    if mode == "url-endpoint":
        allowlist = URL_ENDPOINT_ALLOWLIST_EXT
        patterns = URL_ENDPOINT_PATTERNS
    elif mode == "model-name":
        allowlist = MODEL_NAME_ALLOWLIST_EXT
        patterns = MODEL_NAME_PATTERNS
    else:
        raise ValueError(f"unknown mode: {mode!r}")

    vios: list[Violation] = []
    for f in iter_target_files(root, allowlist):
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"READ_ERROR: {f}: {e}", file=sys.stderr)
            continue
        vios.extend(scan_text_for_patterns(text, f, patterns))

    # Also scan files in allowlist extensions if directly targeted (PASS fixture
    # detection: confirm allowlist 효과 — allowlist files contain patterns but
    # are NOT scanned, so violations=0 is expected).
    return vios


def list_catalogs() -> int:
    """`--list-catalogs` self-check (사용자 명시 검증 5 답습)."""
    print(f"url_endpoint_catalog={len(URL_ENDPOINT_PATTERNS)}", file=sys.stderr)
    for pid, vendor, _ in URL_ENDPOINT_PATTERNS:
        print(f"  {pid}\t{vendor}", file=sys.stderr)
    print(f"model_name_catalog={len(MODEL_NAME_PATTERNS)}", file=sys.stderr)
    for pid, vendor, _ in MODEL_NAME_PATTERNS:
        print(f"  {pid}\t{vendor}", file=sys.stderr)
    print(f"url_endpoint_allowlist_ext={len(URL_ENDPOINT_ALLOWLIST_EXT)}", file=sys.stderr)
    print(f"  ext={list(URL_ENDPOINT_ALLOWLIST_EXT)}", file=sys.stderr)
    print(f"model_name_allowlist_ext={len(MODEL_NAME_ALLOWLIST_EXT)}", file=sys.stderr)
    print(f"  ext={list(MODEL_NAME_ALLOWLIST_EXT)}", file=sys.stderr)
    print(f"scan_target_ext={len(SCAN_TARGET_EXT)}", file=sys.stderr)
    print(f"  ext={list(SCAN_TARGET_EXT)}", file=sys.stderr)
    print(f"comment_prefixes={list(COMMENT_PREFIXES)}", file=sys.stderr)
    print(f"url_endpoint_count_compliant={len(URL_ENDPOINT_PATTERNS) == 10}",
          file=sys.stderr)
    print(f"model_name_count_compliant={len(MODEL_NAME_PATTERNS) >= 19}",
          file=sys.stderr)
    print(f"url_endpoint_allowlist_compliant={len(URL_ENDPOINT_ALLOWLIST_EXT) >= 8}",
          file=sys.stderr)
    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Provider URL/model scanner — Group A 3차 PoC (G2 GP-5 Layer 1c)"
    )
    p.add_argument("path", type=str, nargs="?", default=None,
                   help="대상 파일/디렉토리 경로. --list-catalogs 시 생략.")
    p.add_argument("--mode", choices=("url-endpoint", "model-name"), default=None,
                   help="url-endpoint = E-1 (api.* URL) / model-name = E-2 (모델 ID)")
    p.add_argument("--list-catalogs", action="store_true",
                   help="Tier-1 catalog enumerate + count 자기 검증")
    p.add_argument("--max-lines", type=int, default=20)
    args = p.parse_args()

    if args.list_catalogs:
        return list_catalogs()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-catalogs 단독 외)", file=sys.stderr)
        return 2

    root = Path(args.path)
    if not root.exists():
        print(f"PATH_NOT_FOUND: {root}", file=sys.stderr)
        return 2

    vios = scan_path(root, args.mode)

    if not vios:
        print(f"[PASS] mode={args.mode} target={root} violations=0", file=sys.stderr)
        return 0

    print(f"[FAIL] mode={args.mode} target={root} violations={len(vios)}",
          file=sys.stderr)
    seen_pattern_ids: set[str] = set()
    seen_vendors: set[str] = set()
    for v in vios:
        seen_pattern_ids.add(v.pattern_id)
        seen_vendors.add(v.vendor)
    for v in vios[: args.max_lines]:
        print(v.format_short(), file=sys.stderr)
    if len(vios) > args.max_lines:
        print(f"  ... and {len(vios) - args.max_lines} more", file=sys.stderr)
    print(f"  pattern_ids_cover={sorted(seen_pattern_ids)}", file=sys.stderr)
    print(f"  vendors_cover={sorted(seen_vendors)}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
