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

본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(트랙 B 에서 httpx/OpenAI-호환).
트랙 A = StubBoss 주입으로 결정적 — 실 호출·HTTP·설치 0건.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


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


@runtime_checkable
class BossLLM(Protocol):
    """로컬 사장 추상 — provider 교체 단위(헌법 5조). 순수 추론(부작용 0).

    name = 교체 키. advise() = MVP-1 유일 판단 지점(결과 검토). 실패 시 예외를
    던질 수 있다(R3: 호출측이 누락→경고로 처리).
    """

    name: str

    def advise(self, req: AdviceRequest) -> BossAdvice:
        ...


class StubBoss:
    """결정적 테스트용 Boss — scripted advice 반환(트랙 A, 실 호출 0).

    fail=True 면 advise 가 예외(endpoint timeout/다운 모사) → R3 경로 검증.
    calls 로 호출 여부 관찰(R8: 워커 실패 시 미호출 확인).
    """

    def __init__(
        self,
        name: str,
        advice: BossAdvice | None = None,
        fail: bool = False,
    ) -> None:
        self.name = name
        self._advice = advice if advice is not None else BossAdvice(summary="")
        self._fail = fail
        self.calls: list[AdviceRequest] = []

    def advise(self, req: AdviceRequest) -> BossAdvice:
        self.calls.append(req)
        if self._fail:
            raise RuntimeError("boss endpoint 실패(모사)")
        return self._advice


def merge_flags(deterministic: list[str], extra: list[str]) -> list[str]:
    """결정적 flag ∪ advisory flag — *추가만*, 감산 불가(R1 fail-safe 불변식).

    결정적 flag 는 전부 보존되고, extra 중 새것만 뒤에 덧붙는다(중복 없음).
    advisory 가 결정적 flag 를 줄이는 경로는 구조적으로 존재하지 않는다.
    """
    return [*deterministic, *(f for f in extra if f not in deterministic)]
