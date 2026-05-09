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
    def __init__(self, file: Path) -> None:
        self.file = file
        self.violations: list[Violation] = []

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            hit = _matches_forbidden(alias.name)
            if hit:
                self.violations.append(
                    Violation(self.file, node.lineno, "direct-import", hit)
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module:
            hit = _matches_forbidden(node.module)
            if hit:
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


def scan_file(path: Path) -> list[Violation]:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError:
        # 문법 오류 파일은 본 scanner 책무 외 — fail-closed 위해 위반으로 보고하지 않음
        return []
    visitor = _Visitor(path)
    visitor.visit(tree)
    return visitor.violations


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
