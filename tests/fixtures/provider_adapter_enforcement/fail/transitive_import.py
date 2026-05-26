"""FAIL fixture (2차 PoC 신규) — transitive 의존 차단.

답습 출처:
  - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.5 (Transitive A→B→openai)
  - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §5.2

본 fixture 자체는 *forbidden 모듈을 직접 import 하지 않음*. 그러나 *간접* 으로 (다른
fixture 가 forbidden 모듈을 import 하므로) transitive caller 가 됩니다.

본 fixture 는 1차 AST scanner 가 *per-file 검사* 라 *위반 미검출* 이며 (이는 정상),
2차 import-linter 가 *forbidden contract* 의 *전체 src.* 검사로 *intermediate*
(예: `tests/fixtures/.../fail/direct_import.py`) 의 위반을 보고하면 *transitive 차단
효과* 를 cascading 으로 답습합니다.

⚠️ 본 fixture 는 *1차 scanner 결과* 가 위반 1건 (자체 import 가 fixture 임포트로 보일 수 있음)
이거나 0건이거나에 따라 1차/2차 책무 분리 명시 답습 필요.
"""
from __future__ import annotations

# 의도적 — 직접 forbidden 0건. transitive 통과 시뮬레이션.
# 실제 transitive 효과는 import-linter 의 src.* graph traversal 로 검증.


def caller_using_indirect_path() -> None:
    """본 함수는 forbidden 모듈을 *직접* import 하지 않음. transitive fixture."""
    raise NotImplementedError
