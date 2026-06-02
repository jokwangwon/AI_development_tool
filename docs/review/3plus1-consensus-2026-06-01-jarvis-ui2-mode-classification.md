# 3+1 합의 보고서 — #UI-2 백엔드 통합 모드 판정 (REVISE)

> **일자**: 2026-06-01 · **대상**: `docs/phase0/jarvis-ui2-mode-classification-design-brief.md` (v1)
> **프로토콜**: CLAUDE.md §3 (기존 note/svg 동작 변경 + 분류 의사결정 → 3+1 필수)
> **판정**: **REVISE** — 방향·명시버튼 ACCEPT, 단일결합/측정공백/누락BLOCKING 정정 후 진입
> **참여**: A(구현)·B(안전)·C(대안)·Reviewer(코드 재검증 포함)

---

## 1. 교차 비교 핵심

| 쟁점 | 분류 | 결론 |
|---|---|---|
| detectMode 키워드 = #UI-2 근본 원인 | Consensus | C 통찰: 라우터 키워드(`_TASK_KEYWORD_RE`)는 이미 동사형, detectMode는 순수 명사 → **우선순위 문제(BL-4)** |
| ollama `format` grammar 인프라 | Consensus | `OllamaBoss.plan` 에서 **프로덕션 실증** (추측 아님) |
| fail-CLOSED→chat, BL-1 부작용0 | Consensus | 현 코드 견고, 변경 시 보존 대상 |
| 갈림길2 task 처리 | Consensus → **(a)** | chat답변+proposal 동반 (graceful degradation, 프론트 변경 최소) |
| 갈림길4 hint 잔존 | Consensus → **완전 raw** | detectMode 정규식 폐기, hint는 백엔드 오염 |
| 갈림길5 신뢰도 임계 | Consensus → **이진 fail-CLOSED** | 수치 confidence threshold **고정 0건** (MEMORY 답습) |
| 명시 모드 버튼(사용자결정③) | Consensus 채택+강화 | 분류 오류 deterministic 탈출구 |
| **단일 결합 vs 2-pass/하이브리드** | **Divergence** | §3 중심 쟁점 |
| note/svg 회귀 | Partial (B 단독 高) | 채택 — A/C "회귀0"은 추정 |
| §1 "100%" over-claim | Partial (B 주도) | 채택 — task 한정 측정 |

## 2. 통합 BLOCKING (7건)

| # | BLOCKING | 출처 | 해결 방향 |
|---|---|---|---|
| **BL-α** | chat 생성 prompt가 structured 전환으로 재작성 불가피 → §4 비목표 침범 | A1 | 분류-우선 2-pass면 비목표 진짜 보존 |
| **BL-β** | 4-way 결합 grammar 디코딩 품질·chat 자연성 미검증 | A2 | **PoC-1 선행** |
| **BL-γ** | note/svg 회귀 미측정 (fail-CLOSED가 회귀 가속기) | B2 | **PoC-2 before-battery + 회귀0 게이트** |
| **BL-δ** | proposal.prompt = 원본 message 고정 (LLM 재작성 금지) | B1 | 현 `decision.prompt=text`(L56/62) 불변식 명문화 |
| **BL-ε** | task=4번째 valid mode 검증 재설계 | B3 | line 243 화이트리스트 밖에서 4-way 처리(LLM "task" 반환이 chat 침묵 강등됨) |
| **BL-ζ** | 명시 버튼 sticky/transient 미정의 | B5 | transient(1회 후 auto 복귀) + 활성 표시 |
| **BL-η** ⭐신규 | 프론트 렌더 분기가 **로컬 `mode` 변수 기반**(index.html:1494,1512), 서버 `data.mode` 미사용 | Reviewer 코드 재검증 | 분기를 `data.mode`/`data.entry.type` 기반 재작성 — brief 누락 작업 |

## 3. 중심 쟁점 — 단일 결합 vs 2-pass 분류-우선

**Reviewer 판정: 2-pass 분류-우선을 비례적 기본값으로 권고, 단 PoC-1 결과 의존 → 사용자 회부.**

- 단일 결합의 **숨은 비용(BL-α)**: chat 평문 응답조차 grammar schema에 종속 → 현 `CHAT_PROMPT_TEMPLATE` 평문 품질 저하 위험 + §4 비목표 충돌.
- 단일 결합의 명목 이득(latency)이 **실측 미검증**(A 본인 정직 고백).
- **2-pass 분류-우선**(분류 호출 → note/svg/task면 기존 MODE_PROMPTS 재사용, chat이면 기존 평문)이 비목표를 *진짜* 보존 + C의 D 하이브리드(`looks_like_task` 절반 구현됨) + #UI-1 A3 패턴 답습 = 비례성 최고.
- **단, PoC-1에서 결합 chat 품질이 평문과 동등·4-way 정확도 견고로 입증되면 단일 결합도 정당.** 최종은 PoC 결과로 사용자 확정.

## 4. PoC 선행 권고 (플러그인 사이클 GPU 선결검증 선례)

- **PoC-1 (BL-β)**: 실 ollama로 4-way 결합 grammar schema 단일 호출 → 디코딩 안정성 + chat 평문 자연성(structured vs 평문 비교) + null 누수. **단일결합 vs 2-pass 결정 증거.**
- **PoC-2 (BL-γ)**: 12케이스 배터리에 **note/svg 케이스 추가** → 백엔드 4-way의 note/svg 정확도 = 수정 후 회귀0 대조 기준.

근거: 계산적 검증 가능 영역 → 추론적 합의보다 우선(CLAUDE.md §2). PoC 없이 TDD 진입 시 RED 기대값을 추정으로 작성하게 됨.

## 5. brief 수정 권고 (over-claim 정정)
1. §1 "100%/측정됨" = **백엔드 라우팅 브레인(task) 한정** 명시. note/svg 정확도 미측정 → PoC-2 선결.
2. §4 비목표("생성 프롬프트 변경 안 함")가 단일 결합과 충돌 명시(2-pass면 보존).
3. §3/§5-1 **프론트 작업 범위에 렌더 분기 재작성 추가**(BL-η, 로컬 mode→data.mode).
4. §5-2 갈림길2 = "(a) 합의 완료"로 갱신.

## 6. 사용자 결정 필요 (§G)
1. **[중심] 단일 결합 vs 2-pass** — Reviewer 2-pass 권고하나 **PoC-1 결과 의존**. PoC 후 최종 확정.
2. **명시 버튼 sticky vs transient**(BL-ζ) — Reviewer transient 권고.
3. **혼합의도 정책**(Gap) — "task 우선 + note/svg 후속" 단순 정책 한정 vs 복합 라벨 후속 분리.

## 7. 최종 판정: REVISE
방향·명시버튼 = 만장일치 ACCEPT. v1 그대로 TDD 진입 불가:
- 중심 divergence(단일결합 숨은 비용) 미해소 → PoC-1 의존
- 측정 공백(BL-β/γ) → PoC-1/PoC-2 선행
- 누락 BLOCKING(BL-ε task 검증, BL-η 프론트 분기)
- over-claim 정정(§1)

**다음(자동 진입 0)**: brief v2 정정 → PoC-1/PoC-2 → 사용자 §G 확정 → 재합의/TDD. 비례성·threshold 고정 0건 답습.
