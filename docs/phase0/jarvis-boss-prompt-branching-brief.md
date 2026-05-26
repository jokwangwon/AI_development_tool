# Jarvis 워커별 boss prompt 분기 brief — task_kind 4 도메인

> **scope**: 단일 `_SYSTEM_PROMPT` (code 도메인 fizzbuzz few-shot) → **4 도메인 prompt registry + OllamaBoss `system_prompt` override** = 워커 출력 형태별 적합한 검토.
> **DONE 기준**: `boss_prompt_for(kind)` 4 도메인 + override + TDD 가드 + shell 도메인 demo evidence 1건 = advice 가 도메인별 다른 어휘.
> **답습**: 후속 (m) [[v00-sprint-pending]] + [[ceremony-inflation]] 1-agent + R2 텍스트 전용 답습 + (h) 정밀화 prompt 보존.

---

## 1. 동기 — 현 단일 prompt 의 도메인 편향

현 `_SYSTEM_PROMPT` (`src/jarvis/boss.py`, (h) 답습):
- 4 항목 체크리스트 (의도 부합 / 정확성 / 위험 신호 / 품질)
- Few-shot 예시 = `fizzbuzz.py 생성` (code 도메인)

문제:
- TmuxWorker 가 shell 명령 실행 (예: `pytest + lint-imports`) → 출력 = 테스트 결과 + 분석 보고. "코드 정확성" 보다는 "명령 성공/실패·로그 의미" 검토 필요.
- 파일 생성 작업 (예: e2e demo `hello.txt`) → "파일 내용 vs 요구" 검토.
- 자유 텍스트 작업 (예: 문서 생성) → "내용 적합성" 검토.

단일 prompt = 모든 워커 출력을 fizzbuzz 예시에 끌어당김 (Qwen3 응답이 항상 ✅/⚠️ 패턴 출력하지만 항목 의미가 도메인 부정합).

## 2. 설계 — `boss_prompt_for(task_kind)` registry

| `task_kind` | 사용 | 4 항목 의미 |
|------------|------|----------|
| `"code"` (default) | code 생성 워커 (claude/codex/GLM fizzbuzz) | 의도 부합/정확성/위험 신호/품질 — 코드 도메인 |
| `"shell"` | shell 명령 실행 (TmuxWorker dev task) | 명령 성공/로그 의미/위험 명령 흔적/실행 시간 |
| `"file"` | 파일 생성·수정 (e2e hello.txt) | 파일 존재·내용 일치/스키마/민감 정보 누출/포맷 |
| `"general"` | 자유 텍스트 (문서 생성 등) | 요구 부합/사실 정확/오해 소지/명료성 |

각 도메인은 동일 골격 (`재출력 금지` + `4 항목 한국어 1 line` + `결정적 flag 대체 금지` + few-shot 예시) 답습 + 도메인 어휘만 교체.

## 3. API 변경

```python
# src/jarvis/boss.py
def boss_prompt_for(task_kind: str) -> str:
    """4 도메인 prompt registry. 미지 kind → 'general' fallback."""

class OllamaBoss:
    def __init__(self, model: str, timeout_s: float = 60.0,
                 system_prompt: str | None = None):
        # None = 기본 boss_prompt_for("code") (R2 답습 + (h) 정밀화 보존)
        self._system_prompt = system_prompt or boss_prompt_for("code")
```

- 기존 `_SYSTEM_PROMPT` 상수는 `boss_prompt_for("code")` 의 반환값으로 동치 보존 → 회귀 0.
- caller 가 도메인 prompt 명시 = `OllamaBoss(model, system_prompt=boss_prompt_for("shell"))`.
- 임의 prompt 도 가능 (raw string) — 단 R2 책무는 caller 가 보장.

## 4. TDD

| # | test |
|---|------|
| 1 | `boss_prompt_for("code")` = 기존 _SYSTEM_PROMPT 와 동치 (회귀 0) |
| 2 | `boss_prompt_for("shell")` 가 "명령" / "로그" 어휘 포함 |
| 3 | `boss_prompt_for("file")` 가 "파일" / "내용" 어휘 포함 |
| 4 | `boss_prompt_for("general")` 가 "요구" / "사실" 어휘 포함 |
| 5 | `boss_prompt_for("unknown_kind")` → "general" fallback |
| 6 | 4 도메인 모두 mirror 차단 어휘 ("재출력") 보존 (h) 답습 |
| 7 | 4 도메인 모두 길이 ≥ 400 chars (sufficient guidance) |
| 8 | 4 도메인 모두 R2 권위 invariant ("사람 게이트" + "대체") 보존 |
| 9 | `OllamaBoss(system_prompt=None)` → 기본 = boss_prompt_for("code") |
| 10 | `OllamaBoss(system_prompt="X")` → 실 HTTP body 의 system msg.content = "X" |

## 5. 의미 evidence

`examples/jarvis_v00_dev_task.py` (TmuxWorker pytest+lint demo) 를 갱신해 `boss_prompt_for("shell")` 주입:
- 이전 (default code prompt): Qwen3 가 "코드 정확성" 어휘 사용
- 신규 (shell prompt): Qwen3 가 "명령 성공" / "로그" / "테스트 결과" 어휘 사용

합격: shell prompt advice 가 (a) "명령" 또는 "테스트" 어휘 포함 + (b) 4 항목 형태 유지.

## 6. 비-scope (DEFER 영구)

- 워커 출력 *자동 감지* → 도메인 분기 — 휴리스틱 위험, caller 명시가 안전
- LLM 응답 schema 강제 (JSON) — Layer 2+
- 사용자별 custom kind (plugin) — 후속 cycle
- 다국어 prompt — 한국어 한정
- AdviceRequest 에 task_kind 자동 전달 — 본 cycle scope 외 (caller = OllamaBoss 생성자 한 곳)

DONE 후 단일 commit + push + PR comment + memory.
