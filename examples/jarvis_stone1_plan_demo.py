#!/usr/bin/env python3
"""Jarvis 디딤돌1a+1b E2E dogfooding — 실 ollama plan-then-execute + artifact contract.

지금까지 plan-then-execute(PlanController)·boss.plan·artifact contract 는 모두
StubBoss/FakeWorker 트랙 A 테스트로만 검증됐다. 본 데모는 *실 ollama*로:
  1. OllamaBoss.plan() — 실 `/api/chat` format JSON schema grammar 가 valid BossPlan
     (subtasks DAG + contracts)을 내는지 (디딤돌1a §2 트랙 B PoC, brief 미수행분).
  2. PlanController.run_from_planner — 실 plan → 결정적 검증 → 사람 승인 → 위상정렬
     순차 dispatch(실 OllamaWorker, file=LLM-only consume) → artifact 추출·주입.
  3. 능력 경계(Q7): consume 워커 = file(OllamaWorker, fs 실행 부재) → 기본 허용.

⚠️ 실 ollama(localhost:11434) 필요. 토큰 비용 0(로컬). 모델은 --boss-model/
--worker-model 로 교체(Provider Liquidity, 헌법 5조).

사용:
    python examples/jarvis_stone1_plan_demo.py            # 대화형 계획 승인
    python examples/jarvis_stone1_plan_demo.py --yes      # 자동 승인
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import OllamaBoss
from src.jarvis.orchestrator import Orchestrator, WorkerRegistry
from src.jarvis.plan_controller import PlanApprovalRequest, PlanController, PlanStatus
from src.jarvis.review import ReviewGuard
from src.jarvis.worker import OllamaWorker

_DEFAULT_BOSS = "qwen3-30b-a3b-instruct-2507-bartowski:latest"
_DEFAULT_WORKER = "qwen3-coder-next:latest"


def main() -> int:
    ap = argparse.ArgumentParser(description="디딤돌1 plan-then-execute dogfooding")
    ap.add_argument("--yes", action="store_true", help="계획 자동 승인(비대화형)")
    ap.add_argument("--boss-model", default=_DEFAULT_BOSS)
    ap.add_argument("--worker-model", default=_DEFAULT_WORKER)
    ap.add_argument("--planner", default="ollama", choices=["ollama", "codex"],
                    help="plan 공급원: ollama(약한 로컬 boss) | codex(frontier CLI, 디딤돌1d)")
    ap.add_argument(
        "--prompt",
        default="작은 작업 2개로 나눠줘: (1) 'add(a,b)' 파이썬 함수 한 줄 작성, "
        "(2) 그 함수를 호출해 2+3 을 출력하는 한 줄 작성. (2)는 (1)에 의존.",
    )
    args = ap.parse_args()

    # plan 공급원(IN-2): ollama(약한 로컬) 또는 codex(frontier CLI, 디딤돌1d)
    if args.planner == "codex":
        import tempfile

        from src.jarvis.planner import CliPlanner
        # BL-4 실측: codex stdout=추론 로그 혼재 → --output-last-message 파일 추출이 정답.
        # 실측 결과 positional prompt + EOF stdin 이 안정(schema flag/stdin-mode 는 exit 1).
        _codex_out = tempfile.mktemp(suffix=".json", prefix="codex-plan-")
        _codex_prompt = (
            "작업을 실행 가능한 subtask 목록으로 분해해 JSON 으로만 출력하라"
            "(설명·코드블록·마크다운 없이 순수 JSON). worker_kind 는 'file'. "
            "depends_on 은 선행 subtask 인덱스 배열. 한 subtask 산출물을 다른 "
            "subtask 가 쓰면 contracts 에 {name, produced_by} 추가."
        )
        # ⚠️ codex 자동 통합은 *실험적*(dogfooding 발견): codex CLI 출력 형태·schema
        # flag·stdin 모드·sandbox·파일 생성이 prompt/플래그 조합마다 변동 → 안정 미달.
        # probe(직접 실측)에서 codex 가 contract 포함 valid plan JSON 생성 확인(IN-2 실증)
        # 했으나 데모 자동 파이프라인은 후속 안정화 필요. claude 경로(from_cli envelope)는
        # 결정적 검증됨(test_cli_planner.py). 약한 boss 대비는 --planner ollama 로.
        planner = CliPlanner(
            ["codex", "exec",
             "--output-last-message", _codex_out,  # BL-4 파일 추출
             "-s", "read-only"],                   # BL-2 native RO sandbox
            output_file=_codex_out,
            plan_prompt=_codex_prompt,              # positional + EOF stdin(probe 동형)
            timeout_s=300.0,
        )
    else:
        planner = OllamaBoss(model=args.boss_model, plan_kinds=("file",))
    worker = OllamaWorker(alias="ollama-file", model=args.worker_model)
    registry = WorkerRegistry()
    registry.register(worker)
    orch = Orchestrator(registry, ReviewGuard(), ApprovalGate(approver=lambda r: True))

    def plan_approver(req: PlanApprovalRequest) -> bool:
        print("\n── 계획 승인 게이트 (디딤돌1a, default-deny) ──")
        for i, st in enumerate(req.subtasks):
            dep = f" depends_on={list(st.depends_on)}" if st.depends_on else ""
            print(f"  [{i}] ({st.worker_kind}→{req.mapped_aliases[i]}){dep}: {st.desc}")
        if req.contracts:
            print("  명시 contracts (boss 선언):")
            for c in req.contracts:
                print(f"    - {c.name} produced_by={c.produced_by}")
        if req.implicit_contracts:
            print("  암묵 contracts (controller 가 depends_on 에서 합성 — 디딤돌1c):")
            for c in req.implicit_contracts:
                print(f"    - {c.name} produced_by={c.produced_by}")
        print(f"  실행 순서(위상정렬): {list(req.order)}")
        if args.yes:
            print("  --yes → 자동 승인")
            return True
        return input("  계획을 승인합니까? [y/N] ").strip().lower() == "y"

    ctrl = PlanController(
        dispatcher=orch.dispatch,
        kind_table={"file": "ollama-file"},
        registry=registry,
        plan_approver=plan_approver,
        max_steps=5,
        allow_code_consume=False,  # Q7 능력 경계 — file consume 만(기본)
    )

    planner_desc = (f"codex (frontier CLI, 디딤돌1d)" if args.planner == "codex"
                    else f"ollama {args.boss_model} (약한 로컬 boss)")
    print("=== 디딤돌1 plan-then-execute E2E (실 LLM) ===")
    print(f"planner      : {planner_desc}")
    print(f"worker(file) : {args.worker_model}")
    print(f"작업         : {args.prompt}")
    print(f"plan() 호출 중 ({args.planner}) …")

    out = ctrl.run_from_planner(planner, args.prompt, "stone1-demo")

    print("\n=== PlanOutcome ===")
    print(f"  status : {out.status.value}")
    print(f"  reason : {out.reason}")
    print(f"  subtask reports: {len(out.subtask_reports)}")
    for i, r in enumerate(out.subtask_reports):
        prev = (r.result.output or "")[:120].replace("\n", " ")
        print(f"    [{i}] applied={r.applied} exit={r.result.exit_code} | {prev}")
    return 0 if out.status == PlanStatus.COMPLETED else 1


if __name__ == "__main__":
    raise SystemExit(main())
