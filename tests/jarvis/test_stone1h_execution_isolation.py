"""디딤돌1h — requires_execution 실행 격리 갭 (발견#1) 테스트.

답습: docs/phase0/jarvis-stone1h-execution-isolation-gap-design-brief.md (v1.1)
  [[3plus1-consensus-2026-05-31-jarvis-stone1h-execution-isolation]] (REVISE, CL-1~6).

발견#1: claude Bash 도구의 `2>/dev/null` 쓰기가 격리 RO 세트(/dev 부재)에 차단 →
requires_execution 실 실행 불가 → LLM 추론 폴백. 해소 = `/dev/null` 등 무해
캐릭터 디바이스를 단일 파일 RW allowlist 로 노출(CL-2 명시 means 레버).

트랙 A(격리 없이) = wrap 조립 + CL-4 노드 검증. 통합(sandbox-built) = 실 ll_sandbox.
"""
from __future__ import annotations

import os
import stat
import subprocess

import pytest

from src.jarvis.isolation import _DEFAULT_SANDBOX_BIN, LandlockIsolation
from src.jarvis.worker_setup import CLAUDE_RW_DEVICES

_sandbox_built = os.path.isfile(_DEFAULT_SANDBOX_BIN) and os.access(
    _DEFAULT_SANDBOX_BIN, os.X_OK
)
_has_devnull = stat.S_ISCHR(os.stat("/dev/null").st_mode)
_has_sda = os.path.exists("/dev/sda")


# --- CL-3: 시작 allowlist = /dev/null 단일 리터럴 ---


def test_rw_devices_is_devnull_only() -> None:
    """CL-3: 시작 RW 디바이스 allowlist = /dev/null 단일(터미널/블록 디바이스 미포함)."""
    assert CLAUDE_RW_DEVICES == ("/dev/null",)


# --- CL-1/CL-2: wrap 이 검증된 RW 디바이스를 ll_sandbox 인자에 포함 ---


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_wrap_includes_safe_rw_device(tmp_path) -> None:
    """rw_files 의 /dev/null 이 wrap 출력 인자에 포함(드롭 금지 — CL-1)."""
    iso = LandlockIsolation(
        ro_paths=["/usr"],
        rw_root=str(tmp_path),
        rw_files=["/dev/null"],
    )
    out = iso.wrap(["echo", "hi"], workdir=str(tmp_path))
    assert "/dev/null" in out


# --- CL-4: 노드 검증 (심링크 거부 / /dev prefix / S_ISCHR only, BLK 거부) ---


def test_safe_rw_device_accepts_chr_devnull() -> None:
    from src.jarvis.isolation import _safe_rw_device

    assert _safe_rw_device("/dev/null") == "/dev/null"


def test_safe_rw_device_rejects_non_dev(tmp_path) -> None:
    from src.jarvis.isolation import _safe_rw_device

    f = tmp_path / "regular.txt"
    f.write_text("x")
    assert _safe_rw_device(str(f)) is None  # /dev/ 밖 거부


def test_safe_rw_device_rejects_symlink(tmp_path) -> None:
    from src.jarvis.isolation import _safe_rw_device

    link = tmp_path / "null-link"
    link.symlink_to("/dev/null")
    assert _safe_rw_device(str(link)) is None  # 심링크 거부(우회 차단)


def test_safe_rw_device_rejects_missing() -> None:
    from src.jarvis.isolation import _safe_rw_device

    assert _safe_rw_device("/dev/does-not-exist-xyz") is None


@pytest.mark.skipif(not _has_sda, reason="/dev/sda 없음")
def test_safe_rw_device_rejects_block_device() -> None:
    """CL-4: 블록 디바이스(/dev/sda)는 S_ISCHR 아니므로 거부(위험 디바이스 차단)."""
    from src.jarvis.isolation import _safe_rw_device

    assert _safe_rw_device("/dev/sda") is None


# --- 통합 (sandbox-built): 실 ll_sandbox 커널 강제 ---


def _wrap_run(tmp_path, argv, rw_files):
    work = tmp_path / "work"
    work.mkdir(exist_ok=True)
    iso = LandlockIsolation(
        ro_paths=["/usr", "/lib", "/bin", "/sbin", "/etc", "/run/systemd/resolve"],
        rw_root=str(tmp_path),
        rw_files=rw_files,
    )
    cmd = iso.wrap(argv, workdir=str(work))
    return subprocess.run(cmd, cwd=str(work), capture_output=True, text=True)


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_devnull_rw_restores_execution(tmp_path) -> None:
    """[발견#1 회귀방지] /dev/null RW 노출 → 2>/dev/null 쓰기 + 실행 성공."""
    proc = _wrap_run(
        tmp_path,
        ["bash", "-c", 'echo HI 2>/dev/null && echo WROTE_OK; python3 -c "print(40+2)"'],
        rw_files=["/dev/null"],
    )
    assert "HI" in proc.stdout
    assert "WROTE_OK" in proc.stdout  # /dev/null 쓰기 성공
    assert "42" in proc.stdout  # 실 실행 복구


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_without_devnull_execution_blocked(tmp_path) -> None:
    """대조: /dev/null 미노출 시 2>/dev/null 쓰기 실패(발견#1 재현)."""
    proc = _wrap_run(tmp_path, ["bash", "-c", "echo HI 2>/dev/null && echo WROTE_OK"], rw_files=[])
    assert "WROTE_OK" not in proc.stdout  # 쓰기 차단


@pytest.mark.skipif(not _sandbox_built, reason="ll_sandbox 미빌드 (make 필요)")
def test_other_dev_node_still_blocked(tmp_path) -> None:
    """음성: /dev/null 만 노출 → /dev/zero 는 여전히 차단(선별 노출)."""
    proc = _wrap_run(
        tmp_path,
        ["bash", "-c", "head -c1 /dev/zero >/dev/null 2>&1 && echo ZERO_OK || echo ZERO_BLOCKED"],
        rw_files=["/dev/null"],
    )
    assert "ZERO_BLOCKED" in proc.stdout


@pytest.mark.skipif(not (_sandbox_built and _has_sda), reason="ll_sandbox 미빌드 또는 /dev/sda 없음")
def test_block_device_rejected_by_sandbox(tmp_path) -> None:
    """음성(CL-4): ll_sandbox 에 /dev/sda 직접 전달 시 거부(C 레벨 BLK 방어).

    wrap 은 _safe_rw_device 로 이미 거름 → 여기선 ll_sandbox 직접 호출로 C 방어 검증.
    """
    work = tmp_path / "work"
    work.mkdir(exist_ok=True)
    # ll_sandbox <rw> /dev/sda -- echo : 블록 디바이스 RW 규칙 추가 시도 → 거부(비0)
    proc = subprocess.run(
        [_DEFAULT_SANDBOX_BIN, str(tmp_path), "/dev/sda", "--", "echo", "X"],
        cwd=str(work), capture_output=True, text=True,
    )
    assert proc.returncode != 0, "블록 디바이스가 RW 노출됨 — C 방어 실패"


# --- E-3 산출 계약 센서 (발견#2 — did_act 우회 silent semantic) ---

import json  # noqa: E402
from dataclasses import replace  # noqa: E402

from src.jarvis.approval import ApprovalGate  # noqa: E402
from src.jarvis.boss import BossPlan, PlanSubtask  # noqa: E402
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry  # noqa: E402
from src.jarvis.plan_controller import _EXEC_SENTINEL, PlanController, PlanStatus  # noqa: E402
from src.jarvis.review import ReviewGuard  # noqa: E402
from src.jarvis.worker import WorkerResult  # noqa: E402


class _ExecWorker:
    """output·did_act 를 제어하는 FakeWorker + 마지막 prompt 캡처(feedforward 검증)."""

    def __init__(self, alias: str, output: str, did_act: bool | None = True) -> None:
        self.alias = alias
        self._out = output
        self._did = did_act
        self.last_prompt = ""

    def run(self, prompt: str, workdir: str) -> WorkerResult:
        self.last_prompt = prompt
        base = WorkerResult.from_cli(
            0, json.dumps({"result": self._out, "is_error": False})
        )
        return replace(base, did_act=self._did)


def _exec_ctrl(worker: _ExecWorker) -> PlanController:
    reg = WorkerRegistry()
    reg.register(worker)
    orch = Orchestrator(
        registry=reg, guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: True),
        workdir_factory=lambda t: f"/tmp/ws/{t}",
    )
    return PlanController(
        dispatcher=orch.dispatch, kind_table={"code": worker.alias},
        registry=reg, plan_approver=lambda req: True, implicit_contracts=False,
    )


def _exec_plan() -> BossPlan:
    return BossPlan(subtasks=(
        PlanSubtask(desc="gcd(48,36) 실행해 출력", worker_kind="code",
                    requires_execution=True),
    ))


def test_e3_feedforward_injects_sentinel_instruction() -> None:
    """requires_execution 작업 desc 에 산출 계약 sentinel 지시 주입(feedforward)."""
    w = _ExecWorker("code-w", output=f"{_EXEC_SENTINEL}\n12", did_act=True)
    _exec_ctrl(w).run(_exec_plan(), task_id="t1")
    assert _EXEC_SENTINEL in w.last_prompt  # 워커에게 마커 지시 전달


def test_e3_warns_when_sentinel_absent_despite_did_act_true() -> None:
    """발견#2: did_act=True(도구 씀) 인데 sentinel 부재 → exec_contract 경고(추론 폴백)."""
    w = _ExecWorker("code-w", output="논리적으로 결과는 12입니다", did_act=True)
    out = _exec_ctrl(w).run(_exec_plan(), task_id="t2")
    assert out.status is PlanStatus.COMPLETED            # 경고-only(차단 아님)
    assert out.noop_warnings == ()                       # 1g 채널 불변(did_act=True)
    assert len(out.exec_contract_warnings) == 1          # E-3 별도 채널 발화
    assert "추론 폴백" in out.exec_contract_warnings[0].reason


def test_e3_no_warning_when_sentinel_present() -> None:
    """정상 실행(sentinel 산출) → exec_contract 경고 0."""
    w = _ExecWorker("code-w", output=f"실행함\n{_EXEC_SENTINEL}\n12", did_act=True)
    out = _exec_ctrl(w).run(_exec_plan(), task_id="t3")
    assert out.exec_contract_warnings == ()


def test_e3_no_warning_when_requires_execution_false() -> None:
    """requires_execution=False → sentinel 무관 경고 0(생성/분석 작업 오탐 0)."""
    w = _ExecWorker("code-w", output="코드만 생성", did_act=True)
    plan = BossPlan(subtasks=(
        PlanSubtask(desc="코드 생성만", worker_kind="code", requires_execution=False),
    ))
    out = _exec_ctrl(w).run(plan, task_id="t4")
    assert out.exec_contract_warnings == ()


def test_e3_did_act_false_uses_1g_channel_not_e3() -> None:
    """did_act=False → 1g noop 채널(강한 신호) 우선, E-3 중복 발화 안 함."""
    w = _ExecWorker("code-w", output="되묻기만", did_act=False)
    out = _exec_ctrl(w).run(_exec_plan(), task_id="t5")
    assert len(out.noop_warnings) == 1          # 1g 채널
    assert out.exec_contract_warnings == ()     # E-3 중복 없음(elif)
