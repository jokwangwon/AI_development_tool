"""Worker 추상 — headless CLI 워커 결과 모델.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md
  - §3: headless subprocess 1급. exit code = 결정적 완료신호, json = 출력 +
    total_cost_usd(비용신호 공짜). 화면 스크래핑 함정 회피.
  - D-2: 워커 = CLI 에이전트, headless subprocess 우선.

본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(워커 = 외부 *바이너리* 실행).
Provider Liquidity(헌법 5조) 답습: 워커 교체 = 다른 바이너리 headless 호출.
"""
from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from typing import Any, Callable, Protocol, runtime_checkable

from src.jarvis.isolation import IsolationBackend, PassthroughIsolation

# runner(cmd, workdir) -> (exit_code, stdout, stderr). 주입으로 테스트 결정성 확보.
Runner = Callable[[list[str], str], "tuple[int, str, str]"]


@dataclass(frozen=True)
class WorkerResult:
    """워커 1회 실행 결과. exit_code 가 완료/성공의 *결정적* 권위."""

    exit_code: int
    output: str
    cost_usd: float | None
    is_error: bool
    raw: dict[str, Any] | None

    @property
    def succeeded(self) -> bool:
        return not self.is_error

    @classmethod
    def from_cli(cls, exit_code: int, stdout: str, stderr: str = "") -> "WorkerResult":
        """headless CLI 출력(json 우선) 파싱.

        exit code 가 최우선 권위(비0 = 실패). json 파싱 실패 시 raw 보존 +
        실패 처리(출력 잘림/비표준 provider 를 거짓 성공으로 오인 금지).
        """
        nonzero = exit_code != 0
        try:
            raw: dict[str, Any] | None = json.loads(stdout)
        except (json.JSONDecodeError, TypeError):
            raw = None

        if raw is None:
            return cls(
                exit_code=exit_code,
                output=stdout,
                cost_usd=None,
                is_error=True,  # 파싱 불가 = 거짓 성공 금지
                raw=None,
            )

        cost = raw.get("total_cost_usd")
        return cls(
            exit_code=exit_code,
            output=str(raw.get("result", "")),
            cost_usd=float(cost) if cost is not None else None,
            is_error=nonzero or bool(raw.get("is_error", False)),
            raw=raw,
        )


@runtime_checkable
class Worker(Protocol):
    """워커 추상 — provider 교체 단위(헌법 5조). alias = 라우팅 키."""

    alias: str

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        ...


def _subprocess_runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
    """기본 runner — headless subprocess 실행(완료 = 프로세스 종료 = 결정적)."""
    proc = subprocess.run(  # noqa: S603 (cmd = 신뢰된 argv + prompt)
        cmd, cwd=workdir, capture_output=True, text=True
    )
    return proc.returncode, proc.stdout, proc.stderr


class CliWorker:
    """headless CLI 워커 — `argv + prompt` 를 격리 wrap 후 subprocess 실행.

    예: argv=["claude", "--output-format", "json", "-p"] →
        실행 `claude --output-format json -p "<prompt>"`.
    runner 주입 시 실제 호출 없이 테스트 가능. 외부 LLM SDK import 0(바이너리 실행).
    """

    def __init__(
        self,
        alias: str,
        argv: list[str],
        isolation: IsolationBackend | None = None,
        runner: Runner | None = None,
    ) -> None:
        self.alias = alias
        self._argv = list(argv)
        self._isolation = isolation or PassthroughIsolation()
        self._runner = runner or _subprocess_runner

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        cmd = self._isolation.wrap([*self._argv, prompt], workdir)
        exit_code, stdout, stderr = self._runner(cmd, workdir)
        return WorkerResult.from_cli(exit_code, stdout, stderr)
