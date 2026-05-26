# Jarvis GLM(Ollama) 워커 추가 brief — 로컬 LLM 워커 확장

> **scope**: claude(외부 CLI) + codex(외부 CLI) → **glm-4.7-flash(Ollama 로컬) 워커 추가**. 외부 토큰 비용 0건 fallback 워커.
> **DONE 기준**: GLM 이 동일 fizzbuzz 작업 1건 완수 → 파일 검증 + Layer 0 누적.
> **답습**: [[jarvis-local-boss-direction]] "GLM 등 fallback 워커" + [[provider-liquidity]] 활용 2차 확장 + [[ceremony-inflation]] 1-agent.

---

## 1. 새 워커 패턴 — `OllamaWorker` (LLM-only)

claude/codex 와 *다른* 책임 모델:

| 워커 패턴 | LLM 책무 | 파일 쓰기 책무 |
|----------|---------|--------------|
| `CliWorker(claude/codex)` | 응답 + 자체 fs 행동 (외부 CLI 가 파일 작성) | 워커 (격리 안) |
| **`OllamaWorker(GLM)`** | **응답 텍스트만** (Ollama 는 fs 행동 능력 없음) | **orchestrator → demo helper 가 결정적으로 파일 쓰기** |

→ **안전성 ↑**: LLM 은 임의 명령 실행 *경로 부재*. fs 행동 = orchestrator 결정적 코드만. prompt injection 으로 LLM 이 "rm -rf" 출력해도 실 명령 실행 0건 (텍스트로 워크플로 통과).

## 2. demo 구조

```python
# OllamaWorker class = example 내부 정의 (src/ 변경 0, v0.0 한정)
class OllamaWorker:
    alias: str
    model: str
    output_filename: str | None    # workdir/<filename> 에 LLM 응답 텍스트 저장
    
    def run(self, prompt, workdir) -> WorkerResult:
        # 1. Ollama /api/chat 호출 (system + user prompt)
        # 2. 응답 텍스트 추출
        # 3. output_filename 지정 시 workdir 안에 파일 작성 (결정적)
        # 4. WorkerResult(exit_code=0, output=텍스트, is_error=False)
```

- Worker Protocol 충족 (`alias` + `run(prompt, workdir) -> WorkerResult`)
- src/jarvis/worker.py 변경 0 (v0.0 한정, 정착 후 src 이동 검토)
- fs 행동 = `output_filename` 강제 한정 (그 외 fs 변경 0)

## 3. 모델 + prompt 설계

- **모델**: `glm-4.7-flash:latest` (Q4, 19GB, Ollama 로컬)
- **prompt 구조**: GLM 에게 *코드만 반환* 요청 (마크다운 fence 제거 후처리)
  ```
  Write ONLY the Python code (no markdown fences, no explanation) for
  fizzbuzz that prints 1-15 with Fizz/Buzz/FizzBuzz substitution.
  ```
- **응답 후처리**: `_strip_code_fences()` = 응답에서 ` ```python ... ``` ` 마크다운 fence 제거.

## 4. 비용 + 격리

- **외부 API 비용 = 0건** (로컬 GPU 추론). claude $0.077 vs codex 구독 vs **GLM $0**.
- **격리**: Ollama HTTP 호출만 = fs 접근 0건 = LandlockIsolation 적용 자체가 무의미. PassthroughIsolation 한정 + orchestrator 가 결정적 fs 쓰기.
- prompt injection 이 GLM 출력에 위험 명령 포함해도 = 실행 경로 0 = 안전.

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| GLM 응답에 마크다운 fence 포함 | `_strip_code_fences()` 후처리 |
| GLM 응답이 코드 외 설명 포함 | system prompt = "ONLY code, no explanation" 강제 |
| 응답이 비파이썬·손상 코드 | DONE 합격 = 파일 내 'fizz' 키워드 = 느슨한 의미 검증 (코드 동작 자체 = 사람) |
| Ollama timeout | timeout 180s (Qwen3 boss 와 동일) |
| 모델 미다운로드 | precheck = `/api/tags` 에 glm-4.7-flash 존재 확인 |

## 6. 합격 조건 (8/8)

- exit 0
- Ollama 응답 non-empty
- fizzbuzz.py 존재 (workdir 안, orchestrator 결정적 작성)
- 코드에 'fizz' 키워드 포함
- advice non-empty (Qwen3 검토)
- advisory not failed
- Layer 0 entry 1건
- Layer 0 alias = 'glm'

## 7. 비-scope (DEFER 영구)

- `OllamaWorker` src/ 이동 (정착 후 cycle)
- 다중 파일 작성 / 임의 fs 행동 — Layer 2+ 영역 (사람 게이트 신설)
- prompt-driven 명령 실행 — *명시적 비-scope* (안전 본질)
- GLM 모델 라우팅 (task 특성 별 자동 선택) — Layer 2+
- 코드 fence 외 형식 (XML, JSON 응답 schema) — 별도 cycle

DONE 후 단일 commit + push + PR comment + memory 갱신.
