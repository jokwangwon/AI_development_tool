"""Boss LLM 추상 — 로컬 사장의 판단 지점(결과 검토 advisory).

답습: docs/phase0/jarvis-mvp1-local-boss-design-brief.md (v2) §3·§4·§5
  [[3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss]] (풀 3+1, APPROVE w/ COND)
  - §3: Boss = provider 추상(헌법 5조 동형). 순수 추론(부작용 0) — Worker(외부
    바이너리, 부작용 有)와 대칭. OpenAI-호환 endpoint 로 통일(트랙 B).
  - §4 R2: BossAdvice = 텍스트 전용 frozen — 콜백·경로·명령 필드 *금지*. "Boss
    출력 실행 권한 0"을 산문이 아니라 데이터 모델 제약으로 강제. R6: confidence 삭제.
  - §4 R1(fail-safe): advisory 는 결정적 flag 를 *추가*(union)만 — 감산 불가.
    합집합 강제는 호출측(orchestrator)에서. 의미적 green washing(summary 오도)은
    불변식이 막지 못함 → 결정적 flag 분리표시·raw diff·ReviewGuard 권위로 한정.
  - §5 R3: advisory 실패는 게이트 진행(비차단) + 명시 경고. 본 모듈은 advise 가
    실패를 *던지게* 두고, 누락→경고 변환은 orchestrator(가용성 정책)에서.

본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(트랙 B 에서 stdlib urllib).
트랙 A = StubBoss 주입으로 결정적 — 실 호출·HTTP·설치 0건.
트랙 B = OllamaBoss(stdlib urllib.request 단독, `ollama` python SDK import 0건 —
`.importlinter` 답습 + 신규 dep 0).
"""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable

from src.adapters.llm.redaction import RedactionFilter  # SDK 아님 — 송신 redaction (RT-1, 70 entry)


@dataclass(frozen=True)
class AdviceRequest:
    """Boss 가 검토할 입력 — 모두 untrusted(워커 출력 포함, prompt injection 표적).

    Boss 는 이 입력으로 *텍스트만* 생성한다. 실행·게이트 통과·workdir·argv 에
    대한 어떤 제어 정보도 여기서 도출되지 않는다(§5 신뢰 경계).
    """

    prompt: str
    worker_alias: str
    output: str
    deterministic_flags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class BossAdvice:
    """Boss advisory 결과 — *텍스트 전용*(R2). 제어 흐름 필드 금지.

    - summary: 사람에게 보여줄 자연어 검토 요약(표시용 — 게이트 결정에 자동 반영 0).
    - extra_flags: 결정적 flag 에 *추가*할 위험 태그(union, 감산 불가 = R1 fail-safe).
    - advisory_failed: advisory 가 실패(누락)했는지 표지(R3 명시 경고용 *상태* — 게이트
      통과를 좌우하지 않는 표시 메타데이터). confidence 없음(R6).
    """

    summary: str
    extra_flags: list[str] = field(default_factory=list)
    advisory_failed: bool = False


@dataclass(frozen=True)
class PlanSubtask:
    """작업그래프 1개 노드 — boss(untrusted planner)의 제안 (디딤돌1a §2).

    PLAN-INV (a): means 의 *틀*(argv·alias·isolation backend·workdir) 필드 *부재*.
    boss 는 아래 3개만 제안하고, argv prefix·worker alias·격리 backend 는 harness
    table(§5)이 소유한다 — 이 dataclass 에 표현할 수 없다(구조적 means 봉쇄).

    - desc: = 해당 워커에 전달되는 *실행 prompt*(untrusted instruction text).
      "표시용"이 아니다(BL-1 정직화) — dispatch 의 prompt 인자로 흘러 워커 argv
      tail 이 된다. 위험은 계획 승인 게이트(desc 전문 표시) + subtask 반영
      게이트가 방어한다(redaction 아님).
    - worker_kind: 허용 enum(§5 table 키) — boss 의 "워커 종류" 제약 선택(ends).
    - depends_on: 선행 subtask 인덱스(DAG edge). 1a 에선 *실행 순서* 제약일 뿐
      데이터 전달 아님(산출물 전달은 1b).
    """

    desc: str
    worker_kind: str
    depends_on: tuple[int, ...] = ()
    # 디딤돌1f F2: 이 subtask 가 실제 *실행*(테스트·결과 출력·명령)을 요구하는지의
    # boss 구조 선언(ends 속성 — argv 같은 means 틀 아님, PLAN-INV 위반 아님).
    # controller 가 "requires_execution=True AND 비실행 worker_kind"를 결정적으로
    # 검출(F2). 누락 시 False(보수적 — silent pass 면 F1/구성 invariant/F4 가 방어).
    requires_execution: bool = False


@dataclass(frozen=True)
class Contract:
    """워커 간 산출물 전달 계약 — 디딤돌1b (boss 의 산출 *선언*, 권위 0).

    답습: jarvis-stone1b-artifact-contract-design-brief.md (v1.1) §2 (Q8 대안1).
    - name: artifact 식별자(주입 라벨). controller 가 regex 검증 + 고정 prefix 부여.
    - produced_by: 산출 subtask 인덱스. **consumed_by 는 *유추*(depends_on 역방향)** —
      consume subtask = produced_by 를 transitive depends_on 하는 subtask(controller
      결정적 유추). boss 출력 표면↓ + depends_on/contract 정합 불일치 구조적 제거.
    - means 틀 필드 부재(PLAN-INV) — 추출 방법·argv·경로 *없음*(means = controller).
    """

    name: str
    produced_by: int


@dataclass(frozen=True)
class BossPlan:
    """boss 가 1회 제안하는 작업그래프 — proposal, 권위 0 (controller 검증 전).

    PLAN-INV: (a) means 틀 필드 부재 (b) controller 결정적 검증을 거쳐야만 소비
    (c) non-adaptive(워커 결과가 plan 을 갱신하는 경로 없음). 실행·승인 권위는
    controller + 사람 게이트(§3·§4).
    """

    subtasks: tuple[PlanSubtask, ...]
    contracts: tuple[Contract, ...] = ()  # 디딤돌1b 산출물 전달. 1a 하위호환=빈 tuple


@runtime_checkable
class BossLLM(Protocol):
    """로컬 사장 추상 — provider 교체 단위(헌법 5조). 순수 추론(부작용 0).

    name = 교체 키. advise() = MVP-1 유일 판단 지점(결과 검토). 실패 시 예외를
    던질 수 있다(R3: 호출측이 누락→경고로 처리).
    """

    name: str

    def advise(self, req: AdviceRequest) -> BossAdvice:
        ...


@runtime_checkable
class BossPlanner(Protocol):
    """plan 공급원 추상 — advise(BossLLM)와 *별개* Protocol (IN-2).

    plan() 은 작업그래프(BossPlan)를 1회 제안하는 두 번째 판단 지점. advise 와
    분리한 이유(IN-2): **plan 공급원은 boss 로 고정되지 않는다** — 약한 로컬
    boss / 사람 / 더 똑똑한 frontier worker 모두 BossPlanner 를 구현해 plan 을
    공급할 수 있다("사장≠가장 똑똑한 자"). 누가 공급하든 PLAN-SOURCE 불변식:
    controller 검증(§3) + 사람 승인(§4)을 거친다 — 똑똑함≠신뢰.

    실패 시 예외(거짓 진행 금지) — controller 가 "계획 부재 → 중단"으로 변환(§2).
    """

    def plan(self, prompt: str) -> BossPlan:
        ...


class StubBoss:
    """결정적 테스트용 Boss — scripted advice/plan 반환(트랙 A, 실 호출 0).

    advise(BossLLM) + plan(BossPlanner) 둘 다 구현 — 통합 stub(IN-2: 한 객체가
    두 역할). fail=True 면 advise 예외(R3), plan_fail=True 면 plan 예외(§2).
    calls/plan_calls 로 호출 관찰(R8 미호출 확인 / plan 호출 검증).
    """

    def __init__(
        self,
        name: str,
        advice: BossAdvice | None = None,
        fail: bool = False,
        plan: BossPlan | None = None,
        plan_fail: bool = False,
    ) -> None:
        self.name = name
        self._advice = advice if advice is not None else BossAdvice(summary="")
        self._fail = fail
        self._plan = plan if plan is not None else BossPlan(subtasks=())
        self._plan_fail = plan_fail
        self.calls: list[AdviceRequest] = []
        self.plan_calls: list[str] = []

    def advise(self, req: AdviceRequest) -> BossAdvice:
        self.calls.append(req)
        if self._fail:
            raise RuntimeError("boss endpoint 실패(모사)")
        return self._advice

    def plan(self, prompt: str) -> BossPlan:
        self.plan_calls.append(prompt)
        if self._plan_fail:
            raise RuntimeError("boss plan 실패(모사)")
        return self._plan


# 사람이 ```json 으로 감싼 plan.json 흡수용 — worker._strip_code_fences 와 동등
# 로직을 *로컬 복제*(boss 가 worker[부작용 모듈]를 import 하지 않아 "순수 추론"
# 서술 보존, 디딤돌1e §4 CN-3). 사람이 raw JSON 을 주면 fence 없어 원문 그대로.
_PLAN_FENCE_RE = re.compile(r"^```[a-zA-Z0-9_+-]*\n?|\n?```$", re.MULTILINE)


def _strip_plan_fences(text: str) -> str:
    """plan 텍스트의 마크다운 코드 fence 제거. fence 없으면 원문 그대로."""
    stripped = _PLAN_FENCE_RE.sub("", text).strip()
    return stripped or text.strip()


class HumanPlanner:
    """사람이 작성한 작업그래프(BossPlan)를 공급하는 plan 공급원 — 디딤돌1e.

    답습: docs/phase0/jarvis-stone1e-human-planner-design-brief.md (v1.1)
      [[3plus1-consensus-2026-05-30-jarvis-stone1e-human-planner]] (만장일치 AWC).

    BossPlanner Protocol 의 세 번째 구현 — plan 공급원의 극단(사람 = 통제 위치).
    약한 boss(94 dogfooding: contract 미생성) / frontier CLI(1d) 외 사람이 직접
    desc/worker_kind/depends_on/contracts 를 명시한다. 추론·subprocess·네트워크
    실행면 0 — 파일 read(또는 객체) 뿐이라 plan 공급원 중 *가장 안전*(Q2: boss.py
    의 OllamaBoss HTTP IO 와 같은 '공급원 본체 IO', planner.py 의 subprocess
    실행면과 이질).

    - PLAN-SOURCE 불변식: 사람이 짠 plan 이라도 controller 결정적 검증(§3) + 사람
      승인(§4)을 거친다 — *정확성≠보장*(오타·미허용 worker_kind·DAG 사이클도
      controller 가 reject). PLAN-INV (a): means 틀(argv/alias/isolation) 필드
      부재(BossPlan 구조) — 사람도 means 를 못 정한다.
    - ≠ StubBoss(boss.py:142, 테스트 stub·관찰필드 plan_calls/fail 보유)
      — HumanPlanner 는 관찰필드 *부재* = 프로덕션 plan 공급원(CN-5).
    - 두 진입(CN-4): HumanPlanner(plan) 직접 / HumanPlanner.from_file(path) 파일.
    - 게이트 *존재* ≠ *실효*(CN-6): rubber-stamp approver 주입은 구조적으로 못
      막는다(비례성상 허용). 게이트 자체 우회 경로는 0(controller default-deny).
    """

    def __init__(self, plan: BossPlan) -> None:
        self._plan = plan

    @classmethod
    def from_file(cls, path: str) -> "HumanPlanner":
        """사람이 작성한 plan.json(_PLAN_JSON_SCHEMA 와 동일 shape) → HumanPlanner.

        CN-3: 모든 IO/파싱 실패(파일없음·빈/공백·malformed JSON·디코딩)를
        RuntimeError 로 단일 수렴 → run_from_planner 가 PLAN_UNAVAILABLE 로 변환.
        CN-1: _parse_bossplan 은 *방어 파서*(타입·구조만, unknown field 무시) —
        schema strict 검증이 아니다. 의미검증(enum/DAG/범위)은 controller §3.
        파일 크기 상한 미적용(자기 파일 비례성, CN-6 단서).
        """
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            raise RuntimeError(f"HumanPlanner plan 파일 읽기 실패: {exc}") from exc
        except UnicodeDecodeError as exc:
            raise RuntimeError(f"HumanPlanner plan 파일 디코딩 실패: {exc}") from exc
        if not text.strip():
            raise RuntimeError("HumanPlanner plan 파일 비어있음 — 거짓 진행 금지")
        # fence 흡수(CN-3) 후 방어 파싱. malformed JSON 은 _parse_bossplan 이
        # RuntimeError 로 던짐(단일 타입 수렴 충족).
        return cls(_parse_bossplan(_strip_plan_fences(text)))

    def plan(self, prompt: str) -> BossPlan:
        """사전 작성 plan 반환. prompt 는 서명 호환용이며 반영하지 않는다(Q5).

        사람 공급원은 plan 을 이미 손에 들고 있다 — prompt(작업 지시)를 무시하고
        고정 plan 을 낸다. 관찰필드(plan_calls) 부재 = StubBoss 와 구분(CN-5).
        """
        return self._plan


# Ollama 직결 — endpoint 하드코딩(SSRF 회피, 외부 host 주입 경로 0).
_OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
_DEFAULT_TIMEOUT_S = 60.0

# 시스템 prompt 골격 — Boss 출력 책무 (R2 텍스트 전용 + 게이트 비-자동통과 +
# 재출력 금지 + 체크리스트 형식). 답습: jarvis-boss-prompt-refinement-brief.md
# (h) 및 jarvis-boss-prompt-branching-brief.md (m). 4 도메인 (code/shell/file/
# general) 모두 동일 골격 + 도메인 어휘만 교체.

# 도메인별 4 평가 항목 + few-shot 예시. mirror 차단 + R2 권위 = 답습 보존.
_DOMAIN_TEMPLATES: dict[str, tuple[tuple[str, str, str, str], tuple[str, str, str, str]]] = {
    # (4 axis labels), (4 few-shot examples)
    "code": (
        ("의도 부합: 작업이 요청대로 수행됐는가",
         "정확성: 결과 자체가 올바른가",
         "위험 신호: 파괴적 명령·민감 정보·외부 호출 등 사후 검토 사항",
         "품질: 간결성·완성도 (간단히)"),
        ("의도 부합: ✅ fizzbuzz.py 생성 요청 충족",
         "정확성: ✅ 1~15 출력, FizzBuzz 분기 정확",
         "위험 신호: 없음",
         "품질: ✅ 단순/명료, 검사 순서 명확"),
    ),
    "shell": (
        ("의도 부합: 요청한 명령이 실행됐는가",
         "결과·로그 의미: 출력 로그가 성공·실패 어디를 가리키는가",
         "위험 신호: 파괴적 명령 흔적·민감 정보 누출·예기치 못한 부작용",
         "품질: 명령 형태·실행 시간 (간단히)"),
        ("의도 부합: ✅ pytest + lint 실행 요청 충족",
         "결과·로그 의미: ✅ 75 passed / Contracts 1 kept 0 broken",
         "위험 신호: 없음 (sudo·rm 흔적 0)",
         "품질: ✅ 명령 chain 명료, 실행 ~2초"),
    ),
    "file": (
        ("의도 부합: 요청한 파일이 생성·수정됐는가",
         "내용 일치: 파일 내용이 요구 사항을 충족하는가",
         "위험 신호: 민감 정보·외부 URL·credential 누출 흔적",
         "품질: 포맷·스키마 정합 (간단히)"),
        ("의도 부합: ✅ hello.txt 생성 요청 충족",
         "내용 일치: ✅ 'JARVIS_E2E_OK' 본문 정확",
         "위험 신호: 없음",
         "품질: ✅ UTF-8 평문, 줄바꿈 일관"),
    ),
    "general": (
        ("의도 부합: 요구·요청이 반영됐는가",
         "사실 정확: 진술이 사실과 일치하는가",
         "위험 신호: 오해 소지·민감 정보·검증되지 않은 주장",
         "품질: 명료성·간결성 (간단히)"),
        ("의도 부합: ✅ 사용자 요구 핵심 반영",
         "사실 정확: ✅ 출처·근거 명시",
         "위험 신호: 없음",
         "품질: ✅ 단락 구조 명료"),
    ),
}


def _render_prompt(axes: tuple[str, str, str, str],
                   shots: tuple[str, str, str, str]) -> str:
    return (
        "당신은 워커 출력 검토 advisory 입니다. 사람 게이트가 단독 권위이므로 "
        "명령·콜백·실행 지시·자동 승인 어휘는 금지합니다.\n\n"
        "⚠️ 워커 출력의 코드·명령·파일 내용을 *그대로 옮겨 쓰지 마십시오*. "
        "재출력은 검토가 아닙니다. 다음 4 항목 각 1 line, 총 3~6 line, "
        "한국어로 평가만 작성하십시오.\n\n"
        + "\n".join(f"- {a}" for a in axes) + "\n\n예시:\n"
        + "\n".join(f"- {s}" for s in shots) + "\n\n"
        "결정적 flag 를 *대체*하려 하지 마십시오 (추가 의견만)."
    )


def boss_prompt_for(task_kind: str) -> str:
    """워커 출력 형태별 system prompt — code/shell/file/general 4 도메인.

    답습: docs/phase0/jarvis-boss-prompt-branching-brief.md §2·§3
      - 4 도메인 모두 동일 골격 (mirror 차단 + 4 항목 + few-shot + R2 권위).
      - 미지 kind → 'general' fallback (silent error 차단).
      - caller 가 명시 = OllamaBoss(system_prompt=boss_prompt_for("shell")).
    """
    template = _DOMAIN_TEMPLATES.get(task_kind) or _DOMAIN_TEMPLATES["general"]
    return _render_prompt(*template)


# 기본 prompt = code 도메인 (회귀 0 — 기존 _SYSTEM_PROMPT 상수 답습).
_SYSTEM_PROMPT = boss_prompt_for("code")


# ── 디딤돌1a plan() — untrusted planner (트랙 B, format grammar) ──────────────
# Q1 결정: 기본 허용 worker_kind = code/file (shell 은 opt-in — boss prompt 에서
# 기본 제외). controller(§3)가 enum 을 재검증하므로 boss prompt 의 허용 집합은
# best-effort 안내일 뿐(grammar 는 문법만, 의미검증 = controller 권위, R4).
_PLAN_KINDS_DEFAULT: tuple[str, ...] = ("code", "file")

# 디딤돌1f F1: worker_kind 별 능력 한 줄(feedforward). boss 가 실행 작업을 무능력
# 워커로 분류하는 silent semantic failure 예방. 실행 능력 경계는 controller F2 가
# 결정적으로 재검증(가이드≠집행). file=LLM 텍스트 생성만, code=실 실행.
# dict() 튜플 형태 — 리터럴 `"code": "..."` 은 secret_scanner T1-041(code: 값) false
# positive 유발(메모리 reference_codex_verify_tooling gotcha 답습, 패턴 회피).
_KIND_CAPABILITY_HINT: dict[str, str] = dict([
    ("file", "코드·텍스트를 *생성*만 함(실행·테스트·명령 불가)."),
    ("code", "코드를 생성하고 *실제 실행*할 수 있음(테스트·결과 출력 가능)."),
    ("shell", "셸 명령을 *실제 실행*할 수 있음."),
])

# ollama `/api/chat` "format" 에 실을 JSON schema — grammar-constrained decoding.
# PLAN-INV (a): argv·alias·workdir·isolation 필드 *부재*(means 틀 봉쇄).
# additionalProperties=false (R3 강건성) — 모르는 필드 주입 차단.
_PLAN_JSON_SCHEMA: dict = {
    "type": "object",
    "properties": {
        "subtasks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "desc": {"type": "string"},
                    "worker_kind": {"type": "string"},
                    "depends_on": {"type": "array", "items": {"type": "integer"}},
                    # 디딤돌1f F2: 실행 요구 구조 선언(ends 속성). controller 결정적 검증.
                    "requires_execution": {"type": "boolean"},
                },
                "required": ["desc", "worker_kind", "depends_on", "requires_execution"],
                "additionalProperties": False,
            },
        },
        # 디딤돌1b: 산출물 전달 계약(선택 — 없으면 전달 0, 1a 동작). consumed_by 유추(Q8).
        "contracts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "produced_by": {"type": "integer"},
                },
                "required": ["name", "produced_by"],
                "additionalProperties": False,
            },
        },
    },
    # OpenAI strict schema(codex --output-schema)는 required 에 모든 properties 포함 요구.
    # contracts 도 required(빈 배열 허용 — 1c 암묵 contract 가 흡수, _parse_bossplan get).
    "required": ["subtasks", "contracts"],
    "additionalProperties": False,
}


def boss_plan_prompt(allowed_kinds: tuple[str, ...] = _PLAN_KINDS_DEFAULT) -> str:
    """plan() system prompt — 작업을 subtask DAG 로 분해(목적만, means 금지).

    boss 는 desc(작업 내용)·worker_kind(허용 enum)·depends_on(선행 인덱스)만 낸다.
    argv·명령·경로·alias 출력 금지(means 틀 = harness 소유, §5). controller 재검증.
    """
    kinds = " | ".join(allowed_kinds)
    # 디딤돌1f F1: worker_kind 능력 feedforward — boss 가 "file=실행 불가"를 모른 채
    # 실행 작업을 file 로 분류하는 silent semantic failure 의 1차 트리거를 예방(가이드).
    cap_lines = "".join(
        f"    · {k}: {_KIND_CAPABILITY_HINT[k]}\n"
        for k in allowed_kinds if k in _KIND_CAPABILITY_HINT
    )
    cap_block = (
        f"- 각 worker_kind 의 능력:\n{cap_lines}"
        "  실행·테스트·결과 출력이 *실제로* 필요한 작업은 실행 가능한 종류로 지정하십시오.\n"
        if cap_lines else ""
    )
    return (
        "당신은 작업 계획가입니다. 사용자 작업을 실행 가능한 subtask 목록으로 "
        "분해해 JSON 으로만 출력하십시오.\n"
        f"- worker_kind 는 다음 중 하나: {kinds}\n"
        f"{cap_block}"
        "- depends_on 은 *선행 subtask 의 인덱스 배열*(없으면 빈 배열)\n"
        "- requires_execution 은 그 subtask 가 코드/명령을 *실제 실행*해야 하면 true, "
        "생성·작성만이면 false (실행 능력 없는 종류로 실행 작업을 보내면 막힙니다).\n"
        "- desc 는 해당 작업 내용(한국어). 명령어·경로·argv·도구 이름·alias 를 "
        "지정하지 마십시오 — 그것은 시스템이 정합니다.\n"
        "- **한 subtask 의 산출물(코드·데이터·스키마)을 다른 subtask 가 입력으로 "
        "써야 하면, contracts 에 {name: 산출물 이름, produced_by: 산출 subtask "
        "인덱스} 를 추가하십시오.** 산출 subtask 를 depends_on 하는 subtask 들이 그 "
        "산출물을 자동으로 받습니다. (전달이 필요 없으면 contracts 는 빈 배열.)\n"
        "- 사이클·자기참조 금지. 불필요하게 잘게 쪼개지 마십시오."
    )


class OllamaBoss:
    """Ollama HTTP `/api/chat` 직결 BossLLM — stdlib urllib 단독.

    답습: docs/phase0/jarvis-v00-working-sprint-brief.md §2
      - `name` = 모델 식별자(헌법 5조 provider 교체 키).
      - endpoint = localhost:11434 하드코딩(생성자에 url 인자 0건 — SSRF 회피).
      - HTTP 실패·malformed JSON·content 누락 → RuntimeError (R3: 호출측 누락→경고).
      - BossAdvice(summary, extra_flags=[], advisory_failed=False) — R2 텍스트 전용.

    extra_flags 자동 추출 0건 = "boss 출력은 결정적 flag 를 *대체* 못 한다" 답습.
    flag 합집합은 호출측(orchestrator merge_flags)이 결정적 flag 위주로 수행.
    """

    def __init__(
        self,
        model: str,
        timeout_s: float = _DEFAULT_TIMEOUT_S,
        system_prompt: str | None = None,
        redactor: RedactionFilter | None = None,
        plan_kinds: tuple[str, ...] = _PLAN_KINDS_DEFAULT,
    ) -> None:
        self.name = model
        self._timeout = timeout_s
        # None = 기본 code 도메인 (회귀 0). caller = boss_prompt_for(kind) 주입.
        self._system_prompt = system_prompt or _SYSTEM_PROMPT
        # 송신 redaction (RT-1, 70 entry (나)) — optional default 로 호환 보존.
        self._redactor = redactor or RedactionFilter()
        # 디딤돌1a plan() system prompt (allowed worker_kind 안내, best-effort).
        self._plan_prompt = boss_plan_prompt(plan_kinds)

    def advise(self, req: AdviceRequest) -> BossAdvice:
        user_blob = (
            f"[task prompt]\n{req.prompt}\n\n"
            f"[worker alias] {req.worker_alias}\n\n"
            f"[worker output]\n{req.output}\n\n"
            f"[deterministic flags]\n" + ", ".join(req.deterministic_flags)
        )
        # RT-1: 송신 전 redaction (untrusted worker output 의 secret strip — GP-2 prevention).
        messages = self._redactor.redact_messages(
            [
                {"role": "system", "content": self._system_prompt},
                {"role": "user", "content": user_blob},
            ]
        )
        body = {
            "model": self.name,
            "stream": False,
            "messages": messages,
        }
        data = json.dumps(body).encode("utf-8")
        request = urllib.request.Request(
            _OLLAMA_CHAT_URL,
            data=data,
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as resp:
                raw = resp.read()
        except (urllib.error.URLError, OSError) as exc:
            raise RuntimeError(f"Ollama 호출 실패: {exc}") from exc

        try:
            payload = json.loads(raw)
        except (ValueError, TypeError) as exc:
            raise RuntimeError(f"Ollama 응답 JSON 파싱 실패: {exc}") from exc

        # Ollama `/api/chat` 응답 schema = {"message": {"role": ..., "content": "..."}}
        message = payload.get("message") if isinstance(payload, dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str) or not content:
            raise RuntimeError(
                "Ollama 응답에 message.content 누락 — silent empty advice 차단"
            )
        return BossAdvice(summary=content, extra_flags=[], advisory_failed=False)

    def plan(self, prompt: str) -> BossPlan:
        """작업 prompt → BossPlan 제안(format grammar). 실패 = RuntimeError(§2).

        controller 가 RuntimeError 를 PLAN_UNAVAILABLE(계획 부재 → 중단)로 변환한다.
        grammar 는 문법만 강제 — 의미 타당성(DAG·enum)은 controller 재검증(R4).
        """
        messages = self._redactor.redact_messages(
            [
                {"role": "system", "content": self._plan_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        body = {
            "model": self.name,
            "stream": False,
            "messages": messages,
            "format": _PLAN_JSON_SCHEMA,  # grammar-constrained decoding
        }
        data = json.dumps(body).encode("utf-8")
        request = urllib.request.Request(
            _OLLAMA_CHAT_URL, data=data, method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as resp:
                raw = resp.read()
        except (urllib.error.URLError, OSError) as exc:
            raise RuntimeError(f"Ollama plan 호출 실패: {exc}") from exc

        try:
            payload = json.loads(raw)
        except (ValueError, TypeError) as exc:
            raise RuntimeError(f"Ollama plan 응답 JSON 파싱 실패: {exc}") from exc

        message = payload.get("message") if isinstance(payload, dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str) or not content.strip():
            raise RuntimeError("Ollama plan 응답에 message.content 누락")
        return _parse_bossplan(content)


def _parse_bossplan(content: str) -> BossPlan:
    """grammar 응답(JSON 문자열) → BossPlan. 구조 위반 = RuntimeError(거짓 진행 금지).

    grammar 가 보통 schema 를 강제하나, provider liquidity(grammar 미지원 provider)
    + 방어적 파싱을 위해 구조를 *재검증*한다 — controller 의 의미검증과 별개로
    데이터 모델 적합성만 본다.
    """
    try:
        obj = json.loads(content)
    except (ValueError, TypeError) as exc:
        raise RuntimeError(f"plan content JSON 파싱 실패: {exc}") from exc
    if not isinstance(obj, dict) or not isinstance(obj.get("subtasks"), list):
        raise RuntimeError("plan content 에 subtasks 배열 없음")
    subtasks: list[PlanSubtask] = []
    for item in obj["subtasks"]:
        if not isinstance(item, dict):
            raise RuntimeError("subtask 항목이 object 아님")
        desc = item.get("desc")
        kind = item.get("worker_kind")
        dep = item.get("depends_on", [])
        if not isinstance(desc, str) or not isinstance(kind, str):
            raise RuntimeError("subtask desc/worker_kind 타입 위반")
        if not isinstance(dep, list) or not all(isinstance(d, int) for d in dep):
            raise RuntimeError("subtask depends_on 은 정수 배열이어야 함")
        # 디딤돌1f F2-1: 실행 요구 구조 선언 read(누락→False 보수적). bool() 로 정규화.
        req_exec = bool(item.get("requires_execution", False))
        subtasks.append(PlanSubtask(desc=desc, worker_kind=kind, depends_on=tuple(dep),
                                    requires_execution=req_exec))
    # 디딤돌1b contracts(선택) — 없으면 빈 tuple(전달 0, 1a 동작).
    contracts: list[Contract] = []
    raw_contracts = obj.get("contracts", [])
    if not isinstance(raw_contracts, list):
        raise RuntimeError("contracts 는 배열이어야 함")
    for item in raw_contracts:
        if not isinstance(item, dict):
            raise RuntimeError("contract 항목이 object 아님")
        cname = item.get("name")
        cpb = item.get("produced_by")
        if not isinstance(cname, str) or not isinstance(cpb, int) or isinstance(cpb, bool):
            raise RuntimeError("contract name/produced_by 타입 위반")
        contracts.append(Contract(name=cname, produced_by=cpb))
    return BossPlan(subtasks=tuple(subtasks), contracts=tuple(contracts))


def merge_flags(deterministic: list[str], extra: list[str]) -> list[str]:
    """결정적 flag ∪ advisory flag — *추가만*, 감산 불가(R1 fail-safe 불변식).

    결정적 flag 는 전부 보존되고, extra 중 새것만 뒤에 덧붙는다(중복 없음).
    advisory 가 결정적 flag 를 줄이는 경로는 구조적으로 존재하지 않는다.
    """
    return [*deterministic, *(f for f in extra if f not in deterministic)]
