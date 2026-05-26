# Jarvis codex 워커 추가 brief — Provider Liquidity 활용 첫 확장

> **scope**: claude 단일 LLM 워커 → **codex(OpenAI ChatGPT) 워커 추가**. 동일 fizzbuzz prompt 로 side-by-side = Provider Liquidity (헌법 5조) 실 입증.
> **DONE 기준**: codex 가 동일 작업 1건 완수 → 파일 검증 PASS + Layer 0 누적 + claude evidence 와 비교 가능.
> **답습**: [[provider-liquidity]] 활용 첫 확장 + [[jarvis-local-boss-direction]] 워커 교체 가능성 입증 + [[ceremony-inflation]] 1-agent 직접.

---

## 1. 출력 형식 차이 — adapter 필요

| 워커 | 출력 형식 | 후처리 |
|------|----------|--------|
| claude | 단일 JSON object (`result`, `total_cost_usd`, `is_error`) | `WorkerResult.from_cli` 직접 파싱 |
| **codex** | **NDJSON stream** (events: `thread.started`, `turn.started`, `item.completed`, `turn.completed`) | **`_codex_runner` 가 NDJSON → claude-shaped JSON 변환** |

핵심: `WorkerResult.from_cli` 변경 0건. boundary 에서 (runner 내부) 정규화 = `CliWorker` 재사용 보존.

## 2. codex argv + sandbox 책무 분리

- argv: `["codex", "exec", "--json", "--dangerously-bypass-approvals-and-sandbox", "-C", workdir, prompt]`
- `--dangerously-bypass-approvals-and-sandbox` = codex 내부 sandbox 끔.
- stdin = `/dev/null` 명시 (codex 가 stdin 대기 안 함).
- ⚠️ **격리 = `PassthroughIsolation`** (사후 발견, brief v1.1 답습):
  - codex 는 `~/.codex/sessions/` + `~/.codex/tmp/arg0/` 에 *쓰기* 필요 (Permission denied EPERM 실측 — `[ll_sandbox] restricted → codex_core::session: Failed to create session`).
  - 현 `ll_sandbox.c` = **단일 RW 디렉터리만 지원** → multi-RW 추가 = 별도 cycle.
  - 후속 격리 hardening 후보: (a) `ll_sandbox` multi-RW patch / (b) codex env path override (예: `CODEX_HOME`, 존재 여부 미확인) / (c) bwrap bind-mount (userns 권한 필요, Ubuntu 24.04 AppArmor 제한 답습 = 비현실).
  - 본 cycle = Provider Liquidity *활용* 1차 입증 한정. 격리 hardening = [[proportionate-security-personal-tool]] 답습 DEFER 단계.

## 3. 출력 파서 (`_parse_codex_ndjson`)

```python
def _parse_codex_ndjson(stdout: str) -> dict:
    """codex NDJSON → claude-shaped {'result', 'is_error', 'total_cost_usd'}.

    last item.completed (type='agent_message') 의 text = result.
    item 부재 = is_error=True (워커 실패 표지, silent success 차단).
    cost_usd = None (codex 는 토큰 수만 보고, USD 환산은 모델별 가격표 영역).
    """
```

손상 라인 = skip. 빈 출력 → `{"result": "", "is_error": True}` (거짓 성공 금지, [[ceremony-inflation]] 답습).

## 4. 비용

- codex (ChatGPT 인증 = 구독 기반) — 1회 fizzbuzz ≈ 무료~소액 (구독 잔량 사용).
- Ollama Qwen3 = 0.
- claude 와 비교 가능 (claude = $0.077, codex = 구독 cost).

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| codex NDJSON parsing 손상 | 라인별 try/except + 마지막 agent_message 만 추출, 부재=is_error=True |
| codex가 fs 외부 쓰기 시도 | ⚠️ **본 cycle 격리 부재** (PassthroughIsolation) — 후속 cycle 영역. v0.0 demo 한정. |
| codex 자체 sandbox 와 충돌 | `--dangerously-bypass-approvals-and-sandbox` 로 codex 내부 sandbox 끔. 외부 격리 = 본 cycle 부재 (후속). |
| ChatGPT 인증 만료 | precheck `codex login status` 답습 (사용자 명시 영역) |
| 모델 응답 불일관 (claude 와 다른 코드 스타일) | fizzbuzz = "fizz" 키워드 매칭 (느슨한 의미 검증, 코드 동작 자체는 사람 검토) |

## 6. 합격 조건 (8/8)

- codex exit 0
- fizzbuzz.py 존재 (Landlock workdir)
- 코드에 "fizz" 키워드 포함
- advice non-empty (Qwen3 검토)
- advisory not failed
- Layer 0 entry 1건
- applied
- **워커 alias = "codex"** (claude entry 와 구분 가능, Layer 1 마이닝 자료)

## 7. 비-scope (DEFER 영구)

- 다중 워커 *동시* 실행 (병렬·라우팅 자동화) — Layer 2+ 영역
- codex 모델 선택 자동화 (`-m` 모델 라우팅) — 별도 cycle
- opencode / GLM 등 추가 워커 — 본 brief 이후 별도 cycle
- claude vs codex 자동 비교·우열 판정 — Layer 1 패턴 마이닝 후속 영역
- **codex 격리 (ll_sandbox multi-RW 또는 env override) — 별도 cycle** ([[proportionate-security-personal-tool]] 답습)

DONE 후 단일 commit + push + PR comment + memory 갱신.
