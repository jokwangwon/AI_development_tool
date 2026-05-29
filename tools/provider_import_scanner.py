#!/usr/bin/env python3
"""Provider Adapter Enforcement — AST-based import scanner.

답습 출처:
  - docs/architecture/llm-providers-design.md §9.1 (위반 패턴 #1)
  - docs/architecture/llm-providers-design.md §9.4 (AST 동적 import 차단)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §5 (Provider Liquidity Layer 1 모법)
  - docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md (1차 PoC 사양)

본 scanner 는 Layer 1 (Entry) 형식 차단 1차 시제.
Runtime 차단 (Layer 2) 은 R-2/R-4.1 답습 별도 PoC.
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

FORBIDDEN_PROVIDERS: frozenset[str] = frozenset(
    {
        "openai",
        "anthropic",
        "litellm",
        "google.generativeai",
        "ollama",
    }
)

MODEL_PATTERN_REGEX = re.compile(r"^(claude-opus-|claude-sonnet-|gpt-|gemini-)")

# facade allow-path (3+1 합의 2026-05-29 MT-1~MT-3, docs/review/3plus1-consensus-2026-05-29-facade-scanner.md)
#   - ADR-009 §2.2 #1 + PoC §2.4 white-list + design §9.3 `pathNot:facade`:
#     facade = Provider Liquidity(헌법 5조-2) 단일 통로 → litellm.Router 위임이 정당.
#     import-linter 는 이미 facade 를 ignore. 본 scanner 의 facade 예외 누락이 결함이었음.
#   - 면제 범위 = **정적 litellm direct/from-import 만** (MT-1 토큰 한정).
#     facade 내 litellm 외 provider(openai 등)·동적 import(importlib/__import__)는 계속 검출(MT-3).
_FACADE_LITELLM_ALLOW_PATH = "src/adapters/llm/facade.py"


def _rel_posix(path: Path, repo_root: Path | None = None) -> str:
    """repo-root 상대 posix 경로 (정확 경로 매칭용, MT-2). 실패 시 원본 posix."""
    root = (Path(repo_root) if repo_root else Path.cwd()).resolve()
    try:
        return Path(path).resolve().relative_to(root).as_posix()
    except ValueError:
        return Path(path).as_posix()


@dataclass(frozen=True)
class Violation:
    file: Path
    line: int
    pattern: str
    detail: str

    def format(self) -> str:
        return f"{self.file}:{self.line}:{self.pattern}:{self.detail}"


def _matches_forbidden(module: str) -> str | None:
    """Return the forbidden token if `module` (or its top-level package) matches."""
    if module in FORBIDDEN_PROVIDERS:
        return module
    top = module.split(".")[0]
    if top in {p.split(".")[0] for p in FORBIDDEN_PROVIDERS}:
        for p in FORBIDDEN_PROVIDERS:
            if module == p or module.startswith(p + "."):
                return p
        # google 단독은 google.generativeai 의 top-level — 차단 (보수적)
        if top == "google":
            return "google"
    return None


class _Visitor(ast.NodeVisitor):
    def __init__(self, file: Path, allow_litellm: bool = False) -> None:
        self.file = file
        self.allow_litellm = allow_litellm  # facade allow-path (MT-1, 정적 litellm 한정)
        self.violations: list[Violation] = []

    def _exempt(self, hit: str) -> bool:
        return hit == "litellm" and self.allow_litellm

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            hit = _matches_forbidden(alias.name)
            if hit and not self._exempt(hit):
                self.violations.append(
                    Violation(self.file, node.lineno, "direct-import", hit)
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module:
            hit = _matches_forbidden(node.module)
            if hit and not self._exempt(hit):
                self.violations.append(
                    Violation(self.file, node.lineno, "from-import", hit)
                )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        # importlib.import_module("openai")
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "importlib"
            and node.func.attr == "import_module"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            hit = _matches_forbidden(node.args[0].value)
            if hit:
                self.violations.append(
                    Violation(self.file, node.lineno, "dynamic-importlib", hit)
                )
        # __import__("openai")
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "__import__"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            hit = _matches_forbidden(node.args[0].value)
            if hit:
                self.violations.append(
                    Violation(self.file, node.lineno, "double-underscore-import", hit)
                )
        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant) -> None:
        if isinstance(node.value, str) and MODEL_PATTERN_REGEX.match(node.value):
            self.violations.append(
                Violation(self.file, node.lineno, "model-name-branch", node.value)
            )
        self.generic_visit(node)


def scan_source(source: str, path: Path | str, repo_root: Path | None = None) -> list[Violation]:
    """소스 문자열 검사 (테스트 oracle, MT-5). facade allow-path 판정 포함."""
    p = Path(path)
    try:
        tree = ast.parse(source, filename=str(p))
    except SyntaxError:
        # 문법 오류 파일은 본 scanner 책무 외 — fail-closed 위해 위반으로 보고하지 않음
        return []
    allow_litellm = _rel_posix(p, repo_root) == _FACADE_LITELLM_ALLOW_PATH
    visitor = _Visitor(p, allow_litellm=allow_litellm)
    visitor.visit(tree)
    return visitor.violations


def scan_file(path: Path, repo_root: Path | None = None) -> list[Violation]:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    return scan_source(source, path, repo_root)


def iter_python_files(root: Path) -> Iterator[Path]:
    if root.is_file() and root.suffix == ".py":
        yield root
        return
    for p in root.rglob("*.py"):
        if p.is_file():
            yield p


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Provider Adapter Enforcement scanner (G2 GP-5 Layer 1)"
    )
    parser.add_argument(
        "target",
        type=Path,
        help="검사 대상 디렉터리 또는 .py 파일",
    )
    args = parser.parse_args(argv)

    if not args.target.exists():
        print(f"[ERROR] target not found: {args.target}", file=sys.stderr)
        return 2

    all_violations: list[Violation] = []
    for py_file in iter_python_files(args.target):
        all_violations.extend(scan_file(py_file))

    if not all_violations:
        print(f"[PASS] No violations found in: {args.target}")
        return 0

    for v in all_violations:
        print(v.format())
    print(f"[FAIL] {len(all_violations)} violation(s) found.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
