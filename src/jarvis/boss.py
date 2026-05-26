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
import urllib.error
import urllib.request
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


# Ollama 직결 — endpoint 하드코딩(SSRF 회피, 외부 host 주입 경로 0).
_OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
_DEFAULT_TIMEOUT_S = 60.0

# 시스템 prompt — Boss 출력 책무 (R2 텍스트 전용 + 게이트 비-자동통과 +
# 재출력 금지 + 체크리스트 형식). 답습: docs/phase0/jarvis-boss-prompt-
# refinement-brief.md §2 — 이전 prompt 에서 LLM 이 워커 결과 코드를 mirror
# 하던 행동 차단. 4 항목 평가 + few-shot 예시로 응답 형태 stabilize.
_SYSTEM_PROMPT = (
    "당신은 워커 출력 검토 advisory 입니다. 사람 게이트가 단독 권위이므로 "
    "명령·콜백·실행 지시·자동 승인 어휘는 금지합니다.\n\n"
    "⚠️ 워커 출력의 코드·명령·파일 내용을 *그대로 옮겨 쓰지 마십시오*. "
    "재출력은 검토가 아닙니다. 다음 4 항목 각 1 line, 총 3~6 line, 한국어로 "
    "평가만 작성하십시오.\n\n"
    "- 의도 부합: 작업이 요청대로 수행됐는가\n"
    "- 정확성: 결과 자체가 올바른가\n"
    "- 위험 신호: 파괴적 명령·민감 정보·외부 호출 등 사후 검토 사항\n"
    "- 품질: 간결성·완성도 (간단히)\n\n"
    "예시:\n"
    "- 의도 부합: ✅ fizzbuzz.py 생성 요청 충족\n"
    "- 정확성: ✅ 1~15 출력, FizzBuzz 분기 정확\n"
    "- 위험 신호: 없음\n"
    "- 품질: 단순/명료, 검사 순서 명확\n\n"
    "결정적 flag 를 *대체*하려 하지 마십시오 (추가 의견만)."
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

    def __init__(self, model: str, timeout_s: float = _DEFAULT_TIMEOUT_S) -> None:
        self.name = model
        self._timeout = timeout_s

    def advise(self, req: AdviceRequest) -> BossAdvice:
        user_blob = (
            f"[task prompt]\n{req.prompt}\n\n"
            f"[worker alias] {req.worker_alias}\n\n"
            f"[worker output]\n{req.output}\n\n"
            f"[deterministic flags]\n" + ", ".join(req.deterministic_flags)
        )
        body = {
            "model": self.name,
            "stream": False,
            "messages": [
                {"role": "system", "content": _SYSTEM_PROMPT},
                {"role": "user", "content": user_blob},
            ],
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


def merge_flags(deterministic: list[str], extra: list[str]) -> list[str]:
    """결정적 flag ∪ advisory flag — *추가만*, 감산 불가(R1 fail-safe 불변식).

    결정적 flag 는 전부 보존되고, extra 중 새것만 뒤에 덧붙는다(중복 없음).
    advisory 가 결정적 flag 를 줄이는 경로는 구조적으로 존재하지 않는다.
    """
    return [*deterministic, *(f for f in extra if f not in deterministic)]
