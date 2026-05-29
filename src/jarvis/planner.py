"""CliPlanner — 디딤돌1d frontier CLI planner (plan 공급원 유연, IN-2).

답습: docs/phase0/jarvis-stone1d-frontier-planner-design-brief.md (v1.1)
  [[3plus1-consensus-2026-05-30-jarvis-stone1d-frontier-planner]] (REVISE→AWC).

  frontier CLI(codex/claude)를 `BossPlanner` 로 감싸 plan 공급 — 약한 로컬 boss
  (94 entry dogfooding 한계) 외 더 똑똑한 공급원. argv 교체 = planner 교체(헌법 5조).

  - IN-2: plan 공급원은 boss 로 고정 안 됨. frontier 도 *untrusted* — 낸 plan 은
    controller 검증(schema/DAG/table/능력 경계)+사람 승인 그대로(PLAN-SOURCE,
    run_from_planner→run). 똑똑함≠신뢰.
  - BL-1: plan *데이터* 신뢰 경로는 기존 재사용(전파면 0). 단 plan *생성* = frontier
    CLI subprocess 신규 실행면(fs 쓰기·명령 실행 능력). → RO 격리(BL-2).
  - BL-2: CLI native read-only sandbox(codex `--sandbox read-only`) argv 로 plan
    생성 fs 쓰기 차단(harness 구성 책임). net egress 미차단 잔여.
  - BL-3: schema flag(codex `--output-schema`/claude `--json-schema`)로 _PLAN_JSON_
    SCHEMA 강제 + `_parse_bossplan` 방어 2층(grammar 부재 아님 — 사실 정정).
  - BL-4: per-CLI extractor(codex stdout, claude from_cli result envelope).
  - BL-5: runner timeout(hang → RuntimeError → PLAN_UNAVAILABLE).

본 모듈은 boss.py(_parse_bossplan·boss_plan_prompt) + worker.py(_strip_code_fences·
WorkerResult) 를 import — subprocess+격리 의존을 boss.py "순수 추론" 서술과 분리(Q4).
외부 LLM SDK import 0(CLI 바이너리 실행).
"""
from __future__ import annotations

import subprocess
from typing import Callable

from src.jarvis.boss import (
    _PLAN_JSON_SCHEMA,
    BossPlan,
    _parse_bossplan,
    boss_plan_prompt,
)
from src.jarvis.worker import WorkerResult, _strip_code_fences

# runner(cmd, timeout_s, stdin) -> (exit_code, stdout, stderr). 주입으로 테스트 결정성.
PlannerRunner = Callable[[list[str], float, str], "tuple[int, str, str]"]

# extractor(exit_code, stdout, stderr) -> plan JSON 텍스트. CLI 별 envelope 처리(BL-4).
PlanExtractor = Callable[[int, str, str], str]

_DEFAULT_TIMEOUT_S = 120.0


def _default_planner_runner(
    cmd: list[str], timeout_s: float, stdin: str = ""
) -> tuple[int, str, str]:
    """frontier CLI subprocess 실행 — timeout 강제(BL-5) + stdin 항상 제공.

    [[reference_codex_verify_tooling]] gotcha: codex 는 prompt 를 *stdin* 으로 받는다
    (positional 만 주면 "Reading additional input from stdin" 으로 hang/exit 1).
    stdin 을 항상 닫아(빈 문자열 = EOF) hang 방지하고, stdin_prompt 모드면 prompt 전달.
    """
    try:
        proc = subprocess.run(  # noqa: S603 (cmd = 신뢰된 argv)
            cmd, capture_output=True, text=True, timeout=timeout_s, input=stdin
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"CLI planner timeout({timeout_s}s)") from exc
    return proc.returncode, proc.stdout, proc.stderr


def _stdout_extractor(exit_code: int, stdout: str, stderr: str) -> str:
    """기본 extractor — stdout 직접(codex 등 plan JSON 을 stdout 으로 내는 CLI)."""
    return stdout


def claude_extractor(exit_code: int, stdout: str, stderr: str) -> str:
    """claude `-p --output-format json` envelope 추출(BL-4 2단 파싱).

    stdout = {"result": "<plan JSON>", "is_error": ...} → WorkerResult.from_cli 로
    envelope 해석(exit≠0/파싱불가/is_error = 거짓 성공 금지) → result(.output) 반환.
    """
    res = WorkerResult.from_cli(exit_code, stdout, stderr)
    if res.is_error:
        raise RuntimeError(f"claude planner 실패(exit={exit_code}, is_error)")
    return res.output


class CliPlanner:
    """frontier CLI 를 BossPlanner 로 감싸는 어댑터.

    argv = CLI 호출 prefix(native RO sandbox·schema flag 포함, 사용자 구성 — BL-2/BL-3).
    예: ["codex","exec","-s","read-only","--output-schema","/tmp/plan-schema.json"].
    extractor = per-CLI envelope 처리(기본 stdout, claude=claude_extractor).
    """

    def __init__(
        self,
        argv: list[str],
        *,
        runner: PlannerRunner | None = None,
        extractor: PlanExtractor | None = None,
        timeout_s: float = _DEFAULT_TIMEOUT_S,
        plan_prompt: str | None = None,
        output_file: str | None = None,
        stdin_prompt: bool = False,
    ) -> None:
        self._argv = list(argv)
        self._runner = runner or _default_planner_runner
        self._extractor = extractor or _stdout_extractor
        self._timeout = timeout_s
        self._plan_prompt = plan_prompt or boss_plan_prompt()
        # codex 등 prompt 를 stdin 으로 받는 CLI 용([[reference_codex_verify_tooling]]).
        # True 면 argv 에 prompt 미포함, stdin 으로 전달. False(claude 등)=positional.
        self._stdin_prompt = stdin_prompt
        # codex `--output-last-message <file>` 처럼 최종 메시지를 *파일*로 내는 CLI 용
        # (BL-4 실측: codex stdout=추론 로그 혼재 → 파일 추출이 정답). 주어지면 실행 후
        # 이 파일을 읽어 plan 텍스트로 사용(extractor 무시). argv 에도 동일 경로 포함 필요.
        self._output_file = output_file

    def plan(self, prompt: str) -> BossPlan:
        """frontier CLI 호출 → BossPlan. 실패 = RuntimeError(PLAN_UNAVAILABLE 유발).

        plan 은 *untrusted proposal* — controller 검증+사람 승인이 권위(IN-2).
        """
        full_prompt = f"{self._plan_prompt}\n\n[작업]\n{prompt}"
        if self._stdin_prompt:
            cmd = list(self._argv)         # prompt = stdin (codex gotcha)
            stdin = full_prompt
        else:
            cmd = [*self._argv, full_prompt]  # prompt = positional (claude 등)
            stdin = ""
        exit_code, stdout, stderr = self._runner(cmd, self._timeout, stdin)
        if exit_code != 0:
            raise RuntimeError(f"CLI planner exit {exit_code}: {stderr[:200]}")
        if self._output_file is not None:
            try:
                with open(self._output_file, encoding="utf-8") as fh:
                    text = fh.read()
            except OSError as exc:
                raise RuntimeError(f"CLI planner output_file 읽기 실패: {exc}") from exc
        else:
            text = self._extractor(exit_code, stdout, stderr)
        if not text or not text.strip():
            raise RuntimeError("CLI planner empty result — 거짓 진행 금지")
        # BL-3 방어 2층: schema flag 가 1차 강제, _parse_bossplan 이 구조 재검증.
        # grammar 미강제 CLI 의 fence 흡수(_strip_code_fences) 후 파싱.
        return _parse_bossplan(_strip_code_fences(text))


# 임시 schema/output 파일 경로 생성기 — Date/random 미사용(결정성 무관, OS 제공).
def _mktemp(prefix: str) -> str:
    import tempfile
    return tempfile.mktemp(suffix=".json", prefix=prefix)


def codex_planner(
    *,
    timeout_s: float = 300.0,
    sandbox: str = "read-only",
    plan_prompt: str | None = None,
) -> CliPlanner:
    """codex CLI 를 plan 공급원으로 구성하는 팩토리(디딤돌1d 안정화).

    dogfooding 실측: codex 는 `--output-schema` 로 `_PLAN_JSON_SCHEMA` 를 *강제*해야
    정확한 형식({subtasks:[{desc,worker_kind,depends_on}], contracts:[]})을 낸다.
    schema 없이 prompt 만 주면 자기 식 형식(배열 직접·task 키)으로 흘러 파싱 실패.
    (OpenAI strict schema: required 에 모든 properties 포함 — boss.py _PLAN_JSON_SCHEMA
    가 contracts 도 required, 빈 배열 허용 → 1c 암묵 contract 가 흡수.)

    - `--output-schema <file>`: strict 형식 강제(BL-3).
    - `--output-last-message <file>`: 최종 메시지 파일 추출(BL-4 — stdout 은 추론 로그).
    - `-s read-only`: plan 생성 단계 fs 쓰기 차단(BL-2 native RO sandbox).
    - positional prompt + EOF stdin(codex gotcha 방어, [[reference_codex_verify_tooling]]).
    """
    import json

    schema_path = _mktemp("plan-schema-")
    with open(schema_path, "w", encoding="utf-8") as fh:
        json.dump(_PLAN_JSON_SCHEMA, fh, ensure_ascii=False)
    out_path = _mktemp("codex-plan-")
    argv = [
        "codex", "exec",
        "--output-schema", schema_path,
        "--output-last-message", out_path,
        "-s", sandbox,
    ]
    return CliPlanner(
        argv, output_file=out_path, timeout_s=timeout_s, plan_prompt=plan_prompt
    )
