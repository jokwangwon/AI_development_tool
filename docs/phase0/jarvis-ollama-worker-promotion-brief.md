# Jarvis OllamaWorker src 이동 정착 brief

> **scope**: GLM demo 의 example inline `OllamaWorker` 클래스 → **`src/jarvis/worker.py` 정착**. v0.0 임시 위치 해소.
> **DONE 기준**: src 클래스 + TDD 10+ test green + GLM demo 재실행 8/8 PASS 보존 + 회귀 0.
> **답습**: 후속 (k) [[v00-sprint-pending]] + [[ceremony-inflation]] 1-agent 직접 + 책무 동일 보존 (책무 *변경* 0 = 정착 단계 본질).

---

## 1. 책무 정리 (정착 전후 *동일*)

| 책무 | OllamaWorker | 비고 |
|------|-------------|------|
| Ollama HTTP `/api/chat` 호출 | ✅ | 단일 boundary call |
| 응답 텍스트 추출 | ✅ | message.content |
| 마크다운 fence 제거 | ✅ | `_strip_code_fences` private helper |
| fs 행동 (output_filename) | ✅ optional | workdir 안 단일 파일 결정적 작성 |
| path traversal 차단 | ✅ | `os.path.realpath` workdir prefix 강제 |
| 임의 명령 실행 | **❌** | LLM 능력 0 = 구조적 안전 본질 |
| Worker Protocol 충족 | ✅ | alias + run(prompt, workdir) → WorkerResult |

## 2. API 시그니처 (변경 0)

```python
class OllamaWorker:
    def __init__(
        self,
        alias: str,
        model: str,
        output_filename: str | None = None,
        timeout_s: float = 180.0,
        system_prompt: str | None = None,  # 신규: 옵션 — 기본값 = "code-only"
    ) -> None: ...

    def run(self, prompt: str, workdir: str) -> WorkerResult: ...
```

`system_prompt=None` → default `"You output only code with no explanations or markdown fences."` 보존 (GLM demo 동작 그대로).

## 3. 신규 의존 / 임포트

- `urllib.request` / `urllib.error` / `json` / `re` / `os` — 모두 stdlib (신규 dep 0).
- `WorkerResult` 동일 패키지 = 순환 import 0.
- `.importlinter` 영향 0 (외부 LLM SDK import 미발생).

## 4. fail-soft / 에러 의미론

| 경로 | 결과 |
|------|------|
| HTTP `URLError` / `OSError` | `WorkerResult(exit_code=1, output="...", is_error=True, raw=None)` |
| JSON parse 실패 | 동상 |
| `message.content` 누락 / 빈 문자열 | 동상 |
| `output_filename` path traversal 시도 | 동상 |
| 파일 쓰기 IO 실패 | `WorkerResult(exit_code=1, ..., is_error=True)` — 부분 성공 차단 |

OllamaBoss = `RuntimeError` raise (advisory pattern). **OllamaWorker = WorkerResult 반환 (worker pattern)**. 두 책무가 다르므로 에러 의미론도 다름 (R3 답습).

## 5. 테스트 설계 (TDD 10+)

| # | test | 답습 |
|---|------|------|
| 1 | Worker Protocol 충족 (isinstance Worker) | §1 |
| 2 | 정상 응답 → WorkerResult(exit 0, output=text) | §2 |
| 3 | `output_filename=None` → 파일 미생성 | §1 fs optional |
| 4 | `output_filename="x.py"` → workdir/x.py 생성 + 내용 일치 | §1 fs |
| 5 | 응답에 ` ```python ... ``` ` fence → 제거된 코드만 저장 | §1 fence |
| 6 | `output_filename="../escape"` → is_error + 파일 미생성 | §1 traversal |
| 7 | HTTP URLError → is_error=True (raise 0) | §4 |
| 8 | malformed JSON → is_error=True | §4 |
| 9 | message.content 누락 → is_error=True | §4 |
| 10 | endpoint = localhost:11434 하드코딩 (SSRF 회피) | §3 (OllamaBoss 답습) |
| 11 | system_prompt 기본값 = "code-only" 어휘 포함 | §2 |
| 12 | system_prompt 사용자 override 적용 확인 | §2 |

## 6. example 갱신

`examples/jarvis_v00_glm_worker.py`:
- `from src.jarvis.worker import OllamaWorker` 추가
- inline `class OllamaWorker:` + `_strip_code_fences` + `_FENCE_RE` 제거
- `_ollama_has_model` precheck 보존 (demo 한정 책무)
- 동작 변경 0 = DONE 8/8 PASS 보존

## 7. 비-scope (DEFER 영구)

- `output_filename` 다중 파일 / 디렉터리 작성 — Layer 2+ 영역 (사람 게이트)
- prompt-driven 명령 실행 — *명시 비-scope* (안전 본질)
- 응답 schema validation (JSON/XML 강제) — 별도 cycle
- 로컬 LLM streaming 응답 (`stream=true`) — 후속 cycle
- 워커 metrics (latency, token count) — Layer 1 마이닝 확장 영역

DONE 후 단일 commit + push + PR comment + memory 갱신.
