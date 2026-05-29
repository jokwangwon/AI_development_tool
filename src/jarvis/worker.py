"""Worker 추상 — headless CLI 워커 결과 모델.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md
  - §3: headless subprocess 1급. exit code = 결정적 완료신호, json = 출력 +
    total_cost_usd(비용신호 공짜). 화면 스크래핑 함정 회피.
  - D-2: 워커 = CLI 에이전트, headless subprocess 우선.

본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(워커 = 외부 *바이너리* 실행 또는
stdlib HTTP 호출). Provider Liquidity(헌법 5조) 답습: 워커 교체 = 다른 바이너리
headless 호출 또는 OllamaWorker model 인자 교체.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Protocol, runtime_checkable

from src.adapters.llm.redaction import RedactionFilter  # SDK 아님 — 송신 redaction (RT-1, 70 entry)

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


# tmux subprocess runner = argv → (exit_code, stdout, stderr). 주입으로 테스트 결정성.
TmuxRunner = Callable[[list[str]], "tuple[int, str, str]"]


def _default_tmux_runner(argv: list[str]) -> tuple[int, str, str]:
    """기본 tmux runner — `tmux <subcommand> ...` subprocess 실행."""
    proc = subprocess.run(  # noqa: S603 (argv = 신뢰된 tmux 호출 + workdir 인자)
        argv, capture_output=True, text=True
    )
    return proc.returncode, proc.stdout, proc.stderr


class TmuxWorker:
    """tmux 패널 실 spawn 워커 — 사용자가 관전 가능한 워커 모델 입증용.

    답습: docs/phase0/jarvis-v00-working-sprint-brief.md §3
      - 흐름: new-session -d → send-keys(격리 wrap 된 inner cmd + sentinel) →
        capture-pane polling(sentinel 등장 시 종료) → kill-session(try/finally).
      - 완료 sentinel = `__JARVIS_DONE_<exit_code>__` (echo $?).
      - sentinel 미발화 = is_error=True(타임아웃·hang 거짓 성공 금지).
      - tmux 패널 출력은 JSON 아님 → WorkerResult.from_cli 미경유, 직접 구성.
      - cost_usd = None(headless JSON 경유 아님).
    """

    def __init__(
        self,
        alias: str,
        argv: list[str],
        isolation: IsolationBackend | None = None,
        tmux_runner: TmuxRunner | None = None,
        poll_attempts: int = 60,
        poll_interval_s: float = 1.0,
        session_prefix: str = "jarvis",
        nonce_factory: Callable[[], str] | None = None,
        on_session: Callable[[str], None] | None = None,
    ) -> None:
        self.alias = alias
        self._argv = list(argv)
        self._isolation = isolation or PassthroughIsolation()
        self._tmux = tmux_runner or _default_tmux_runner
        self._poll_attempts = max(1, poll_attempts)
        self._poll_interval = max(0.0, poll_interval_s)
        self._session_prefix = session_prefix
        # 완료 sentinel = per-session 무작위 nonce (위조 표면 사전/외부 차단, 74 entry B-2).
        # nonce = 비밀 아닌 per-run salt(사전 예측 불가) — 평문 노출 무관, 안전가치=예측불가만.
        self._nonce_factory = nonce_factory or (lambda: uuid.uuid4().hex)
        # 75 entry: new-session 성공 직후 session 명 통지(라이브 capture-pane 용). lifecycle 변경 0.
        self._on_session = on_session

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        inner = self._isolation.wrap([*self._argv, prompt], workdir)
        session = f"{self._session_prefix}-{uuid.uuid4().hex[:8]}"
        # per-run nonce sentinel — 명령이 nonce 예측 불가 → 사전/외부 위조 차단(B-2).
        nonce = self._nonce_factory()
        if not nonce:
            raise ValueError("nonce_factory 가 빈 nonce 반환 — sentinel 위조 방어 무력화 금지")
        sentinel_re = re.compile(rf"__JARVIS_DONE_{re.escape(nonce)}_(-?\d+)__")
        # sentinel 포함 shell 한 줄 — exit code 보존(`$?`).
        inner_shell = shlex.join(inner)
        full_cmd = f"cd {shlex.quote(workdir)} && {inner_shell}; echo __JARVIS_DONE_{nonce}_$?__"

        new_rc, _, new_err = self._tmux([
            "tmux", "new-session", "-d", "-s", session, "-x", "200", "-y", "50",
        ])
        if new_rc != 0:
            return WorkerResult(
                exit_code=new_rc or 1,
                output=f"tmux new-session 실패: {new_err}",
                cost_usd=None,
                is_error=True,
                raw=None,
            )

        # 75 entry: 세션 생성 성공 후 통지 (보드가 라이브 capture-pane 가능). fail-soft.
        if self._on_session is not None:
            try:
                self._on_session(session)
            except Exception:
                pass

        try:
            self._tmux(["tmux", "send-keys", "-t", session, full_cmd, "Enter"])
            pane_text, sentinel_code = self._poll_for_sentinel(session, sentinel_re)
        finally:
            self._tmux(["tmux", "kill-session", "-t", session])

        if sentinel_code is None:
            return WorkerResult(
                exit_code=124,                            # 관행: timeout 코드
                output=pane_text,
                cost_usd=None,
                is_error=True,                            # 거짓 성공 금지
                raw=None,
            )

        cleaned = sentinel_re.sub("", pane_text).rstrip()
        return WorkerResult(
            exit_code=sentinel_code,
            output=cleaned,
            cost_usd=None,
            is_error=sentinel_code != 0,
            raw=None,
        )

    def _poll_for_sentinel(
        self, session: str, sentinel_re: "re.Pattern[str]"
    ) -> tuple[str, int | None]:
        """capture-pane polling — per-run nonce sentinel 등장 시 즉시 반환."""
        pane_text = ""
        for _ in range(self._poll_attempts):
            _, out, _ = self._tmux(["tmux", "capture-pane", "-p", "-t", session])
            pane_text = out
            m = sentinel_re.search(pane_text)
            if m is not None:
                return pane_text, int(m.group(1))
            if self._poll_interval > 0:
                time.sleep(self._poll_interval)
        return pane_text, None


# ─── OllamaWorker (LLM-only) ──────────────────────────────────────────────
# 답습: docs/phase0/jarvis-ollama-worker-promotion-brief.md
#   - LLM 응답 텍스트만 수신. fs 행동 능력 *경로 부재* (구조적 안전 본질).
#   - 결정적 fs 쓰기 = workdir 안 단일 파일 한정 + realpath traversal 차단.
#   - claude/codex(CliWorker) 와 다른 책임 모델 = prompt injection 으로 LLM 이
#     위험 명령 출력해도 실행 0건.
# 헌법 5조: model 인자 교체 = provider 교체 = Provider Liquidity 답습.

_OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
_OLLAMA_WORKER_DEFAULT_TIMEOUT_S = 180.0

# 기본 system prompt — "코드 외 출력 차단" 어휘. 사용자 override 가능.
_DEFAULT_SYSTEM_PROMPT = (
    "You output only code with no explanations or markdown fences."
)

# 마크다운 fence 제거 — `` ```python ... ``` `` 또는 ``` ... ``` 모두 처리.
_FENCE_RE = re.compile(r"^```[a-zA-Z0-9_+-]*\n?|\n?```$", re.MULTILINE)


def _strip_code_fences(text: str) -> str:
    """LLM 응답에서 마크다운 코드 fence 제거. fence 없으면 원문 그대로."""
    stripped = _FENCE_RE.sub("", text).strip()
    return stripped or text.strip()


class OllamaWorker:
    """Ollama HTTP /api/chat LLM-only 워커.

    답습: docs/phase0/jarvis-ollama-worker-promotion-brief.md §1·§4
      - 책무 = LLM 응답 + fence 제거 + (option) workdir 안 단일 파일 작성.
      - LLM 임의 명령 실행 *경로 부재* → prompt injection 안전 본질.
      - fail-soft (HTTP/JSON/content 실패 → WorkerResult is_error=True, raise 0).
      - endpoint = localhost:11434 하드코딩 (SSRF 회피).

    fs 행동:
      - output_filename=None → 파일 미작성 (텍스트만 반환).
      - output_filename="x.py" → workdir/x.py 결정적 작성 (realpath traversal 차단).
      - 절대 경로 / .. escape → is_error=True + 파일 미생성.
    """

    def __init__(
        self,
        alias: str,
        model: str,
        output_filename: str | None = None,
        timeout_s: float = _OLLAMA_WORKER_DEFAULT_TIMEOUT_S,
        system_prompt: str | None = None,
        redactor: RedactionFilter | None = None,
    ) -> None:
        self.alias = alias
        self._model = model
        self._output_filename = output_filename
        self._timeout = timeout_s
        self._system_prompt = system_prompt or _DEFAULT_SYSTEM_PROMPT
        # 송신 redaction (RT-1, 70 entry (나)) — optional default 로 호환 보존.
        self._redactor = redactor or RedactionFilter()

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        # RT-1: 송신 전 redaction (prompt 의 secret strip — GP-2 prevention).
        messages = self._redactor.redact_messages(
            [
                {"role": "system", "content": self._system_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        body = {
            "model": self._model,
            "stream": False,
            "messages": messages,
        }
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            _OLLAMA_CHAT_URL, data=data, method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=self._timeout) as resp:
                raw = resp.read()
        except (urllib.error.URLError, OSError) as exc:
            return self._error(f"Ollama 호출 실패: {exc}")

        try:
            payload = json.loads(raw)
        except (ValueError, TypeError) as exc:
            return self._error(f"Ollama 응답 JSON 파싱 실패: {exc}")

        message = payload.get("message") if isinstance(payload, dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str) or not content.strip():
            return self._error("Ollama 응답에 message.content 누락 — silent 차단")

        code = _strip_code_fences(content)

        if self._output_filename:
            written = self._write_workdir_file(code, workdir)
            if written is not None:
                return written      # path traversal 또는 IO 실패 → 조기 종료

        # WorkerResult.from_cli 가 기대하는 claude-shaped JSON 으로 정규화
        result_blob = json.dumps(
            {"result": code, "is_error": False, "total_cost_usd": 0.0},
            ensure_ascii=False,
        )
        return WorkerResult.from_cli(0, result_blob)

    def _error(self, msg: str) -> WorkerResult:
        return WorkerResult(
            exit_code=1, output=msg, cost_usd=None, is_error=True, raw=None,
        )

    def _write_workdir_file(self, code: str, workdir: str) -> WorkerResult | None:
        """workdir 안 결정적 fs 쓰기. 성공 = None / 실패 = WorkerResult(is_error)."""
        path = os.path.join(workdir, self._output_filename)  # type: ignore[arg-type]
        # path traversal 차단: realpath 가 workdir 안인지 검증
        try:
            real_workdir = os.path.realpath(workdir)
            real_path = os.path.realpath(path)
        except OSError as exc:
            return self._error(f"realpath 실패: {exc}")
        if not real_path.startswith(real_workdir + os.sep):
            return self._error(
                f"path traversal 차단: {self._output_filename} → {real_path}"
            )
        try:
            with open(real_path, "w", encoding="utf-8") as fh:
                fh.write(code)
        except OSError as exc:
            return self._error(f"파일 쓰기 실패: {exc}")
        return None
