# Jarvis OllamaBoss system_prompt 정밀화 brief

> **scope**: claude/codex/GLM demo 에서 Qwen3 가 워커 결과 코드를 **mirror** 만 함 (검토 0건) → system_prompt 정밀화로 *구조화된 검토 요약* 격상.
> **DONE 기준**: GLM demo 재실행 → advice 가 (a) 코드 본문 미포함 + (b) 평가 어휘 포함 + (c) 간결 (≤ 600 chars) → 합격.
> **답습**: 후속 (h) [[v00-sprint-pending]] + [[ceremony-inflation]] 1-agent + R2 텍스트 전용 답습 (BossAdvice 모델 변경 0).

---

## 1. 현 prompt 진단 — mirror 행동의 직접 원인

현 `_SYSTEM_PROMPT` (`src/jarvis/boss.py:102`):
```
당신은 워커 출력 검토 advisory 입니다.
워커가 산출한 결과를 사람 게이트에 보여줄 *텍스트 요약*만 생성하십시오.
명령·콜백·실행 지시·자동 승인 어휘는 금지합니다 (사람 게이트가 단독 권위).
위험 신호가 보이면 사실적으로 기술하되, 결정적 flag 를 *대체*하려 하지 마십시오.
```

문제점:
- "텍스트 요약만 생성" → LLM 이 *결과 자체를 텍스트로 보여주는 것* = 안전한 답으로 해석
- "위험 신호" 만 언급, "유효성·정확성·품질" 어휘 부재
- 워커 출력 형태 (코드/명령/파일 생성 보고) 별 검토 항목 부재
- 재출력 *금지* 명시 없음

실 evidence (mirror 행동):
- claude worker → Qwen3 advice = ` ```python\n# fizzbuzz.py\nfor i ... ``` ` (코드 fence 포함 그대로)
- GLM worker → Qwen3 advice = `for i in range(1, 16):\n    if ... ` (코드 본문 그대로)
- codex worker → Qwen3 advice = 같음

## 2. 신규 prompt 설계

핵심 변경:
1. **재출력 명시 금지** — "워커 출력의 코드·명령·파일 내용을 그대로 옮겨 쓰지 마십시오. 평가만 작성합니다."
2. **체크리스트 형식 검토** — 4 항목 평가:
   - 의도 부합 (작업이 요청대로 됐는가)
   - 정확성 (결과가 올바른가)
   - 위험 신호 (파괴적 명령·민감 정보 누출 등)
   - 품질 (코드 스타일·완성도, 간단히)
3. **간결 형식 강제** — 한국어 3-6 line, 각 항목 1 line.
4. **예시 응답** (few-shot) — 형태 stabilize.

### 신규 _SYSTEM_PROMPT (draft)

```
당신은 워커 출력 검토 advisory 입니다. 사람 게이트가 단독 권위이므로
명령·콜백·실행 지시·자동 승인 어휘는 금지합니다.

⚠️ 워커 출력의 코드·명령·파일 내용을 *그대로 옮겨 쓰지 마십시오*.
재출력은 검토가 아닙니다. 다음 4 항목 각 1 line, 총 3~6 line, 한국어로
평가만 작성하십시오.

- 의도 부합: 작업이 요청대로 수행됐는가
- 정확성: 결과 자체가 올바른가
- 위험 신호: 파괴적 명령·민감 정보·외부 호출 등 사후 검토 사항
- 품질: 간결성·완성도 (간단히)

예시:
- 의도 부합: ✅ fizzbuzz.py 생성 요청 충족
- 정확성: ✅ 1~15 출력, FizzBuzz 분기 정확
- 위험 신호: 없음
- 품질: 단순/명료, 검사 순서 명확

결정적 flag 를 *대체*하려 하지 마십시오 (추가 의견만).
```

길이 ≈ 600 chars (vs 현재 ≈ 220 chars). 로컬 추론이라 토큰 비용 무시 가능.

## 3. TDD — 결정적 검증 (의미는 demo 가 검증)

| # | test | 답습 |
|---|------|------|
| 1 | `_SYSTEM_PROMPT` 가 "재출력" / "옮겨 쓰지" 어휘 포함 | §2 신규 |
| 2 | `_SYSTEM_PROMPT` 가 "의도 부합" / "정확성" / "위험" / "품질" 어휘 포함 | §2 체크리스트 |
| 3 | `_SYSTEM_PROMPT` 길이 ≥ 400 chars (sufficient guidance) | §2 길이 |
| 4 | 기존 chat endpoint test (`test_ollama_boss_advise_posts_chat_endpoint_with_model`) 보존 — system msg role/content 검증은 신규 어휘 포함 보장 |
| 5 | BossAdvice 모델 (frozen/extra_flags/advisory_failed) 변경 0 회귀 |

## 4. 의미 evidence — demo 재실행

- 재실행 1회 = GLM demo (가장 빠른 보스 + 워커 모두 로컬 → 의미적 차이 가장 분명).
- 합격 조건 (3/3):
  - advice 가 'def ' / 'for ' / '```' / 'print(' 등 코드 본문 시그니처 부재
  - advice 가 '의도' or '정확' or '위험' or '품질' 등 평가 어휘 포함
  - advice 길이 ≤ 600 chars (간결)
- 실패 = prompt 재정밀화 cycle

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| 신규 prompt 가 mirror 보다 더 큰 문제 (예: 환각 평가) | 4 항목 명시 + 예시 응답 = 형태 제약. 의미 검증 = demo + 사람 |
| 모델별 응답 형태 다름 (Qwen3 vs 다른 보스) | 본 cycle = Qwen3-30B-A3B 한정. provider 교체 시 prompt 재튜닝 = Provider Liquidity 비용 |
| Few-shot 이 응답을 fizzbuzz 도메인에 묶음 | 예시는 *형태 stabilize* 한정. 일반화는 fizzbuzz 외 task 에서 검증 (후속) |
| 길어진 prompt = 응답 지연 | 로컬 추론, prefill 빠름. 실측 시 elapsed 1-2초 증가 예상 |

## 6. 비-scope (DEFER 영구)

- 워커 출력 형태별 *분기* (코드 / 명령 / 파일 / 메시지) — 별도 cycle
- 다국어 prompt — 본 cycle 한국어 한정
- LLM 응답 schema 강제 (JSON 출력) — Layer 2+ 영역
- 평가 자동 자료화 (Layer 0 advice_summary 파싱) — Layer 1 마이닝 확장

DONE 후 단일 commit + push + PR + memory.
