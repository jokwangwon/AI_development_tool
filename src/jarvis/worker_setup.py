"""worker_setup — 실 워커 registry + worker_kind table 구성 빌더 (디딤돌1d 실 배선).

WORKER_KIND_TABLE 실 배선: `code` = CliWorker(claude) + Landlock 격리,
`file` = OllamaWorker(LLM-only). PlanController 의 kind_table 인자로 주입한다.

- 재사용: 데모/HUD 진입점에서 `build_worker_registry()` 1회 호출 → (registry, kind_table).
- 테스트 결정성: code_runner/code_isolation 주입으로 실 claude·sandboxer 없이 트랙 A.
- provider liquidity(헌법 5조): argv·model 교체 = 워커 교체.
- 능력 경계(ADR-013 Q7): `code` consume 은 PlanController(allow_code_consume=True)
    opt-in 시에만 — 본 빌더는 *워커 매핑*만 제공하고 능력 경계는 controller 가 강제.

가짜 홈 격리 (레벨 2, ADR-014) — 답습: docs/phase0/jarvis-claude-landlock-fakehome-design-brief.md (v1.1).
  - claude 는 홈(~/.claude 세션/캐시/~/.claude.json) 쓰기 필요 → 진짜 홈을 RO 로 막으면
    조용히 실패(100/101 entry). 해법 = 진짜 홈 미노출 + claude 에게 *빈 가짜 홈* 제공.
  - BL-1 env allowlist: 진짜 env 비밀(토큰·SSH_AUTH_SOCK·cloud)을 워커에 전달하지 않음.
  - BL-2 RO 최소화: /proc·/run·/dev·진짜 홈 미노출(우회 채널 차단).
  - BL-4 rw_root: RW 루트=가짜 홈, 작업폴더를 그 하위에 nest(단일 RW).
  - BL-5/6 시드 신뢰경계 + fail-closed: 가짜 홈 0700 + credential 0600 + symlink 방어 + realpath.
"""
from __future__ import annotations

import os
import shutil
import subprocess
from typing import Any, Callable

from src.jarvis.isolation import IsolationBackend, LandlockIsolation
from src.jarvis.orchestrator import WorkerRegistry
from src.jarvis.worker import CliWorker, OllamaWorker, Runner

# claude headless 실행에 필요한 RO 경로(BL-2 최소화). 광범위 진짜 홈·/proc·전체
# /run·전체 /dev 는 *제외* — fs 외 우회 채널(/proc/self/environ 상속 env,
# /proc/<pid>/root traversal, /run/user 세션 소켓[keyring·dbus·ssh-agent])을 닫는다.
# 대신 claude 동작에 필요한 *좁은* subpath 만 노출(calibration 실측):
#   - /run/systemd/resolve: DNS(/etc/resolv.conf 심볼릭 대상). /run/user 소켓 미노출.
# (/dev 디렉터리 통째는 미노출 — /dev/sda·/dev/mem 등 위험 노드 동시 노출 회피.
#  단 무해 디바이스는 CLAUDE_RW_DEVICES 로 *단일 파일* 선별 노출[디딤돌1h].)
# 쓰기는 가짜 홈(RW root) + CLAUDE_RW_DEVICES 만, 그 외 미노출 = 커널 deny-by-default.
CLAUDE_RO_PATHS: tuple[str, ...] = (
    "/usr", "/lib", "/lib64", "/bin", "/sbin", "/etc",
    "/run/systemd/resolve",
)

# 디딤돌1h — claude Bash 도구의 shell-snapshot source 가 모든 명령에 `2>/dev/null`
# 쓰기를 붙여, /dev 미노출 시 requires_execution 실행이 전부 실패하고 LLM 추론
# 폴백으로 빠졌다(발견#1, 회귀 아닌 레벨2 도입 이래 기존 갭). 해소 = 무해 캐릭터
# 디바이스를 *단일 파일 RW* 로 선별 노출(CL-2 명시 means 레버, harness 소유).
# CL-3: 시작 = /dev/null 단일(스냅샷 실측상 충분). /dev/tty(터미널 주입)·zero·
# urandom 은 dogfooding 신호 시 노드별 개별 판정으로만 추가. 디렉터리/glob 금지.
# CL-4 검증(심링크/realpath/S_ISCHR)은 isolation._safe_rw_device + ll_sandbox.c 2중.
# 답습: docs/phase0/jarvis-stone1h-execution-isolation-gap-design-brief.md (v1.1).
CLAUDE_RW_DEVICES: tuple[str, ...] = (
    "/dev/null",
)

# claude 기본 argv — headless json 출력(exit code·cost 결정적 권위).
CLAUDE_ARGV: tuple[str, ...] = (
    "claude", "--output-format", "json", "--dangerously-skip-permissions", "-p",
)

# 가짜 홈 기본 위치 (Q2 영속) — 진짜 홈 하위 0700. /tmp 금지(world-writable).
DEFAULT_FAKE_HOME: str = os.path.expanduser("~/.jarvis/claude-home")

# BL-1: 워커 env allowlist. 이 키들만 진짜 env 에서 통과시키고, 나머지(ANTHROPIC_*·
# GITHUB_TOKEN·SSH_AUTH_SOCK·AWS_*·GPG_AGENT_INFO 등 비밀)는 *차단*한다(deny-by-default).
# HOME·TMPDIR 는 명시 주입(allowlist 와 별개). 인증은 가짜 홈의 .credentials.json 경유
# (env API 키 미사용 — 필요 시 apiKeyHelper 후속, brief R1).
_ENV_ALLOWLIST: tuple[str, ...] = (
    "PATH", "LANG", "LC_ALL", "LC_CTYPE", "LANGUAGE", "TERM", "TZ",
    "SSL_CERT_FILE", "SSL_CERT_DIR", "NODE_EXTRA_CA_CERTS",
)

_DEFAULT_FILE_MODEL = "qwen3-coder-next:latest"


def _claude_did_act(raw: dict | None) -> bool | None:
    """디딤돌1g — claude headless did_act 프록시(PoC 2026-05-31 실측).

    claude `-p --output-format json` 엔벨로프는 로컬 tool-use(Write/Edit/Bash)를
    *직접* 노출하지 않으나(`server_tool_use` 는 web 전용), `num_turns` 가 프록시:
    num_turns=1 ⟺ 텍스트-only/무행동(되묻기 #3 원형), ≥2 ⟺ 도구 행동 1회 이상.
    raw None(파싱불가) → None(미상, fail-soft). num_turns 지식은 본 wiring 에
    격리 — CliWorker·controller 에 provider 분기 누출 0(헌법5조).
    """
    if not raw:
        return None
    return raw.get("num_turns", 0) > 1


def _build_claude_env(home: str, tmpdir: str, base_env: dict[str, str]) -> dict[str, str]:
    """BL-1 — 워커 env 를 allowlist 로 재구성(진짜 env 비밀 차단).

    base_env(보통 os.environ)에서 allowlist 키만 추려 복사하고, HOME=가짜홈·
    TMPDIR=작업폴더 를 명시 주입한다. 토큰류·SSH_AUTH_SOCK·cloud 자격은 전달 0.
    """
    env = {k: base_env[k] for k in _ENV_ALLOWLIST if k in base_env}
    env["HOME"] = home
    env["TMPDIR"] = tmpdir
    return env


def _copy_secure(src: str, dst: str, *, mode: int) -> None:
    """BL-5 — symlink/특수파일 방어 복사. src 는 일반 파일이어야(symlink 거부)."""
    if os.path.islink(src):
        raise RuntimeError(f"시드 거부: {src!r} 는 symlink (symlink 공격 방어)")
    if not os.path.isfile(src):
        raise FileNotFoundError(f"시드 원본 없음/일반 파일 아님: {src!r}")
    shutil.copyfile(src, dst)  # 메타데이터 미복사(권한은 아래 명시)
    os.chmod(dst, mode)


def provision_claude_home(home: str, *, src_home: str | None = None) -> str:
    """BL-5/6 — claude 전용 가짜 홈 provision(시드는 격리 *밖* trusted 단계).

    진짜 홈의 인증/설정을 가짜 홈에 단방향 복사:
      - 가짜 홈 디렉터리 0700, .claude/ 0700.
      - .claude/.credentials.json → 0600 (symlink 방어 + 일반 파일 검증).
      - .claude.json (있으면) → 0600.
    fail-closed(BL-6): credential 누락/무효 → raise(비인증 진행 금지). 반환 = 가짜 홈 경로.
    """
    src = src_home if src_home is not None else os.path.expanduser("~")
    cred_src = os.path.join(src, ".claude", ".credentials.json")
    # BL-5: symlink credential = 보안 거부(다른 곳을 가리키는 공격 방어).
    if os.path.islink(cred_src):
        raise RuntimeError(f"시드 거부: credential 이 symlink — {cred_src!r}")
    # fail-closed(BL-6): 원본 credential 이 없으면 진행 금지(비인증 워커 실행 금지).
    if not os.path.isfile(cred_src):
        raise FileNotFoundError(
            f"claude credential 없음: {cred_src!r}. "
            "가짜 홈 시드 불가(fail-closed: 비인증 워커 실행 금지)"
        )
    os.makedirs(home, mode=0o700, exist_ok=True)
    os.chmod(home, 0o700)
    # realpath 검증: 가짜 홈 안에 symlink 가 있어 dst 가 밖으로 새지 않도록.
    real_home = os.path.realpath(home)
    claude_dir = os.path.join(home, ".claude")
    os.makedirs(claude_dir, mode=0o700, exist_ok=True)
    os.chmod(claude_dir, 0o700)
    cred_dst = os.path.join(claude_dir, ".credentials.json")
    if not os.path.realpath(cred_dst).startswith(real_home + os.sep):
        raise RuntimeError(f"시드 거부: dst realpath 가 가짜 홈 밖 — {cred_dst!r}")
    _copy_secure(cred_src, cred_dst, mode=0o600)
    cfg_src = os.path.join(src, ".claude.json")
    if os.path.isfile(cfg_src) and not os.path.islink(cfg_src):
        _copy_secure(cfg_src, os.path.join(home, ".claude.json"), mode=0o600)
    return home


def _make_claude_runner(
    home: str, *, run: Callable[..., Any] | None = None
) -> Runner:
    """BL-4 — HOME=가짜홈 주입 runner 클로저. 작업폴더를 가짜 홈 하위(work)에 nest.

    오케스트레이터가 넘기는 workdir(/tmp)은 RW root(가짜홈) 밖이므로 code 워커는
    가짜 홈 하위 `work/` 를 cwd/TMPDIR 로 쓴다(단일 RW 루트). env=allowlist(BL-1).
    run 주입 시 실 subprocess 없이 결정적(트랙 A).
    """
    _run = run if run is not None else subprocess.run
    work = os.path.join(home, "work")

    def runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
        os.makedirs(work, exist_ok=True)
        env = _build_claude_env(home, work, dict(os.environ))
        proc = _run(  # noqa: S603 (cmd = 신뢰된 argv + prompt)
            cmd, cwd=work, env=env, capture_output=True, text=True
        )
        return proc.returncode, proc.stdout, proc.stderr

    return runner


# 하위호환 alias — 기존 진입점이 import 하던 이름. 비격리(레벨2 전) 동작은 더 이상
# 기본이 아니므로, 실 배선은 build_worker_registry 의 가짜홈 runner 를 쓴다.
def claude_runner(cmd: list[str], workdir: str) -> tuple[int, str, str]:
    """(레거시) cwd=workdir + env allowlist + HOME=workdir. 직접 호출 비권장.

    레벨2 실 배선은 build_worker_registry(가짜 홈 + LandlockIsolation(rw_root)) 사용.
    """
    env = _build_claude_env(workdir, workdir, dict(os.environ))
    proc = subprocess.run(  # noqa: S603 (cmd = 신뢰된 argv + prompt)
        cmd, cwd=workdir, env=env, capture_output=True, text=True
    )
    return proc.returncode, proc.stdout, proc.stderr


def build_worker_registry(
    *,
    file_model: str = _DEFAULT_FILE_MODEL,
    code_runner: Runner | None = None,
    code_isolation: IsolationBackend | None = None,
    fake_home: str | None = None,
    src_home: str | None = None,
) -> tuple[WorkerRegistry, dict[str, str]]:
    """실 워커 registry + worker_kind→alias table 구성.

    code = CliWorker(claude) + 가짜 홈 격리(레벨 2) / file = OllamaWorker(LLM-only).
    반환 kind_table 을 PlanController(kind_table=…)에 주입.

    실 배선(주입 미사용): fake_home(기본 ~/.jarvis/claude-home)을 provision(BL-5/6) 후
    code_runner=가짜홈 HOME 주입 클로저(BL-1/4), code_isolation=LandlockIsolation(
    rw_root=fake_home, ro_paths=CLAUDE_RO_PATHS 최소). fail-closed: credential 무효 시 raise.

    트랙 A: code_runner/code_isolation 주입 시 가짜 홈 provision 생략(실 claude·credential 0).
    """
    home = fake_home or DEFAULT_FAKE_HOME
    if code_runner is None or code_isolation is None:
        # 실 배선: 가짜 홈 provision(fail-closed) 후 runner/isolation 구성.
        provision_claude_home(home, src_home=src_home)
    real_runner = code_runner if code_runner is not None else _make_claude_runner(home)
    real_isolation = code_isolation if code_isolation is not None else LandlockIsolation(
        ro_paths=list(CLAUDE_RO_PATHS), rw_root=home, rw_files=list(CLAUDE_RW_DEVICES)
    )
    registry = WorkerRegistry()
    code_worker = CliWorker(
        alias="claude",
        argv=list(CLAUDE_ARGV),
        isolation=real_isolation,
        runner=real_runner,
        did_act_fn=_claude_did_act,  # 디딤돌1g: num_turns>1 프록시(provider 누출 0)
    )
    registry.register(code_worker)
    registry.register(OllamaWorker(alias="ollama-file", model=file_model))
    kind_table = {"code": "claude", "file": "ollama-file"}
    return registry, kind_table
