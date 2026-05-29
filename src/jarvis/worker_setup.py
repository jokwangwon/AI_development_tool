"""worker_setup — 실 워커 registry + worker_kind table 구성 빌더 (디딤돌1d 실 배선).

WORKER_KIND_TABLE 실 배선: `code` = CliWorker(claude) + Landlock 격리,
`file` = OllamaWorker(LLM-only). PlanController 의 kind_table 인자로 주입한다.

- 재사용: 데모/HUD 진입점에서 `build_worker_registry()` 1회 호출 → (registry, kind_table).
- 테스트 결정성: code_runner/code_isolation 주입으로 실 claude·sandboxer 없이 트랙 A.
- provider liquidity(헌법 5조): argv·model 교체 = 워커 교체.
- 능력 경계(ADR-013 Q7): `code` consume 은 PlanController(allow_code_consume=True)
    opt-in 시에만 — 본 빌더는 *워커 매핑*만 제공하고 능력 경계는 controller 가 강제.

답습: examples/jarvis_e2e_demo.py (claude headless + Landlock CLAUDE_RO_PATHS 실측).
"""
from __future__ import annotations

import os
import subprocess

from src.jarvis.isolation import IsolationBackend, LandlockIsolation
from src.jarvis.orchestrator import WorkerRegistry
from src.jarvis.worker import CliWorker, OllamaWorker, Runner

# claude headless 실행에 필요한 RO 경로(jarvis_e2e_demo 실측 — `-p` 는 홈 의존[설정·
# 캐시·런타임]이 커 홈 통째 RO 필요). 쓰기는 workdir(RW)만, 그 외 RO/미노출=커널 차단.
CLAUDE_RO_PATHS: tuple[str, ...] = (
    "/usr", "/lib", "/lib64", "/bin", "/sbin", "/etc", "/proc", "/dev", "/run",
    os.path.expanduser("~"),
)

# claude 기본 argv — headless json 출력(exit code·cost 결정적 권위).
CLAUDE_ARGV: tuple[str, ...] = (
    "claude", "--output-format", "json", "--dangerously-skip-permissions", "-p",
)

_DEFAULT_FILE_MODEL = "qwen3-coder-next:latest"


def claude_runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
    """claude headless runner — cwd=workdir + TMPDIR=workdir(격리 안 정상 동작)."""
    env = {**os.environ, "TMPDIR": workdir}
    proc = subprocess.run(  # noqa: S603 (cmd = 신뢰된 argv + prompt)
        cmd, cwd=workdir, env=env, capture_output=True, text=True
    )
    return proc.returncode, proc.stdout, proc.stderr


def build_worker_registry(
    *,
    file_model: str = _DEFAULT_FILE_MODEL,
    code_runner: Runner | None = None,
    code_isolation: IsolationBackend | None = None,
) -> tuple[WorkerRegistry, dict[str, str]]:
    """실 워커 registry + worker_kind→alias table 구성.

    code = CliWorker(claude) + Landlock(기본 CLAUDE_RO_PATHS, fail-closed) /
    file = OllamaWorker(LLM-only). 반환 kind_table 을 PlanController(kind_table=…)에 주입.

    code_runner/code_isolation 주입 시 실 claude·sandboxer 없이 결정적(트랙 A 테스트).
    """
    registry = WorkerRegistry()
    code_worker = CliWorker(
        alias="claude",
        argv=list(CLAUDE_ARGV),
        isolation=code_isolation or LandlockIsolation(ro_paths=list(CLAUDE_RO_PATHS)),
        runner=code_runner or claude_runner,  # 실 claude = TMPDIR=workdir 필요
    )
    registry.register(code_worker)
    registry.register(OllamaWorker(alias="ollama-file", model=file_model))
    kind_table = {"code": "claude", "file": "ollama-file"}
    return registry, kind_table
