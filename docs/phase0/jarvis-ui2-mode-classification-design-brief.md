# 설계 brief — #UI-2 백엔드 통합 모드 판정 (detectMode 키워드 폐기)

> **상태**: v2 (3+1 합의 REVISE + PoC 반영, TDD 진입) · **출처**: 119 발견 #UI-2 + 120 측정/PoC
> **상위**: `jarvis-conversation-task-routing-design-brief.md`(#UI-1, BL-4가 이 충돌 예측)
> **합의**: `docs/review/3plus1-consensus-2026-06-01-jarvis-ui2-mode-classification.md` (REVISE)
> **핵심 명제**: 프론트 `detectMode` 키워드 게이트를 **백엔드 LLM 문맥 분류**로 대체
> **다음 단계**: TDD (자동 진입 0)

---

## 0. v1 → v2 변경 (3+1 합의 + PoC)

| 항목 | v1 | v2 | 근거 |
|---|---|---|---|
| 호출 구조 | 단일 결합(사용자 결정) | **2-pass 분류-우선** | ⭐PoC: 단일결합 svg **88~99초**(사용 불가) vs 분류-전용 1.1초·91% |
| 명시 버튼 | 추가 | **transient**(1회 후 auto 복귀) | BL-ζ, 사용자 결정 |
| 혼합의도 | 미정 | **task 우선 + 나머지 후속** | 사용자 결정 |
| §1 framing | "100% 측정됨" | **task 라우팅 한정** 명시 | over-claim 정정(B) |
| 프론트 범위 | "raw만 전송" | + **렌더 분기를 서버 `data.mode` 기반 재작성** | BL-η(Reviewer 신규) |
| task valid mode | 암묵 | **MODE_PROMPTS 화이트리스트 밖 처리** | BL-ε |
| proposal.prompt | 암묵 | **원본 message 고정**(LLM 재작성 금지) | BL-δ |

**PoC 결과 (실 ollama 11케이스)**: 단일결합 분류 100%·null누수0 but **latency 12~99초(svg 재앙)**. 분류-전용 91%(1.1초)·**note/svg 회귀 4/4 보존**. 유일 오분류("계산기 만들어줘 정리 노트에서")는 `looks_like_task("만들어줘")` 규칙 필터가 보완. → **2-pass 규칙1차 하이브리드 확정**(#UI-1 A3 패턴 4-way 확장).

## 1. 배경 + 측정 증거 (before-state)

119 dogfooding에서 "계산기 만들어줘 … *정리* 노트에서 쓸 수 있게"(개발 작업)가 프론트
`detectMode`의 키워드 `정리`에 걸려 **note 모드로 빼돌려짐** → 작업 라우팅 스킵(#UI-2).

**120 세션 정확성 측정 (실 ollama 8모델, 12케이스 배터리)**:
| 계층 | 정확도 | 비고 |
|---|---|---|
| **백엔드 라우팅 브레인**(`looks_like_task`+`classify_for_routing`) | **12/12 = 100%** | #UI-2 함정 2건 포함 전부 정확. 라우팅 *판단력*은 견고 |
| **end-to-end**(프론트 detectMode + 백엔드) | **10/12 = 83%** | 작업 2건이 detectMode에서 note로 빠져 라우터 미도달 |

→ **약한 고리는 라우팅 브레인이 아니라 프론트 detectMode 키워드 게이트**. 정량 확인.
⚠️ 12케이스 수기 배터리 = 통계적 일반화 아님(이 배터리 기준). 실 영향은 작업 요청에
해당 명사 빈도에 의존 — `정리/노트/메모/요약/그림` 흔한 단어라 비무시.
⚠️ **over-claim 정정(합의 B)**: 위 "100%"는 **task 라우팅 판정 한정** 측정. **note/svg
분류 정확도는 별개** — PoC-2(아래)가 측정. 4-way 근거로 "100%"를 확장하면 over-claim.

**PoC-1/PoC-2 측정 (실 ollama 11케이스, `/tmp/poc_ui2_classification.py`)**:
| 방식 | 분류 정확도 | latency | note/svg 회귀 |
|---|---|---|---|
| 단일 결합(분류+생성) | 11/11=100%·null누수0 | ⚠️**svg 88~99초·note 12초·chat 20초** | 4/4 |
| **분류-전용(2-pass stage1)** | 10/11=91% | **평균 1.1초** | **4/4 보존** |
- 분류-전용 유일 오분류("계산기 만들어줘 정리 노트에서")는 `looks_like_task` 규칙이 보완.
- chat 품질: 결합 reply ≈ 평문 baseline(품질 OK, 문제는 결합 latency뿐). → **2-pass 확정.**

## 2. 현 구조 진단 (실측)

```
[프론트] detectMode(text) 키워드 정규식 (index.html:1202-1207)
  /정리|노트|메모|요약/ → note   /그림|그려|도식|.../ → svg   else → chat
    ↓ mode 확정
[POST /api/respond {message, mode}] (server.py:234 respond_handler)
    ↓ MODE_PROMPTS[mode] 로 생성 (1 ollama 호출)
    ↓ mode==chat 한정: looks_like_task → classify_for_routing(boss.plan 1회) → proposal
[프론트] mode==chat → 메시지(+proposal) / note·svg → 캔버스 카드
```

- **명시 모드 버튼 없음** — mode는 오직 detectMode 자동 판정(사용자 deterministic 제어 0).
- **task = 4번째 암묵 카테고리** — chat 모드 안의 proposal로만 표출(별도 mode 아님).
- detectMode = 키워드 정규식(문맥 0) → 명사/명령 구분 불가 = #UI-2 근본 원인.

## 3. 핵심 명제 — 백엔드 통합 판정

```
[현재] 프론트 키워드 detectMode → mode 확정 → 백엔드 생성
[개선] 프론트는 raw message만 → 백엔드 LLM이 {chat, note, svg, task} 문맥 분류 → 분기
```

- 분류를 **문맥 이해가 되는 LLM**(이미 있는 boss/ollama)로 이전 → "정리 노트"(명사) vs
  "정리해줘"(명령) 구분 가능.
- `classify_for_routing`(이미 task 판정 중)을 **4-way 분류로 확장** → detectMode + 2-stage를
  하나의 분류 결정으로 통합.

## 4. 목표 / 비목표

**목표**
- detectMode 키워드 정규식 폐기 → 백엔드 문맥 분류로 mode 결정.
- chat/note/svg/task 4-way 통합 판정 + 기존 라우팅 신뢰 경계(BL-1 부작용 0, fail-CLOSED) 보존.
- #UI-2 오분류 해소 — 명사 포함 작업 요청이 작업으로 도달.

**비목표 (이번 범위 밖)**
- note/svg 생성 프롬프트·렌더링 자체 변경(분류만 이전, 생성 로직 유지).
- 대화 라우팅(#UI-1) 재설계(분류 진입부만 교체, proposal 흐름 유지).
- 새 모드 추가(4-way 고정).

## 5. 설계 — 통합 분류

### 5-1. 분류 계약 (2-pass 분류-우선, PoC 확정)
- **Pass 1 — 분류**: raw message → `classify_mode(text, classifier)` → `mode ∈ {chat,note,svg,task}`.
  규칙 1차(`looks_like_task` 류) 우선 + LLM 분류-전용 호출(format=mode enum, ~1.1초).
  fail-CLOSED: 분류 실패·모호·enum 밖 → **chat**.
- **Pass 2 — 생성**: 분류된 mode로 **기존 생성 경로 그대로**(MODE_PROMPTS[note/svg], CHAT_PROMPT).
  → 비목표("생성 프롬프트 변경 안 함") 진짜 보존. **단일 결합 폐기**(PoC svg 88~99초).
- **task 처리(갈림길2=a)**: task/chat 둘 다 **conversational 경로**(chat 답변 생성 + 기존
  `looks_like_task`→`classify_for_routing`→proposal). **BL-ε**: task는 MODE_PROMPTS 화이트리스트
  *밖*에서 chat 생성으로 매핑(현 `if mode not in MODE_PROMPTS: chat` 검증 보존). **BL-δ**:
  proposal.prompt = **원본 message 고정**(현 `decision.prompt=text` 불변식).
- **프론트(BL-η)**: detectMode 폐기, 기본 `mode="auto"` 전송. **렌더 분기를 로컬 mode →
  서버 응답 `data.mode`/`data.entry.type` 기반으로 재작성**.

### 5-2. 갈림길 — 합의/PoC 확정 상태
| # | 갈림길 | 확정 |
|---|---|---|
| 1 호출 구조 | **2-pass 분류-우선** (PoC: 단일결합 svg 88~99초 사용불가) |
| 2 task 처리 | **(a) chat답변+proposal 동반** (합의 만장일치) |
| 3 명시 override | **명시 모드 버튼(chat/노트/도식) + transient**(1회 후 auto 복귀, BL-ζ) |
| 4 프론트 hint | **완전 raw**(detectMode 폐기), auto=백엔드 분류 |
| 5 신뢰도 임계 | **이진 fail-CLOSED**(파싱실패/enum밖→chat), 수치 threshold **고정 0건** |
| 혼합의도 | **task 우선 + 나머지 후속**(복합 라벨 후속 분리) |

## 6. 보안 / 신뢰 경계
- **BL-1 보존**: 분류는 순수 판정(부작용 0). board.create/run 직접 호출 0 — task면 proposal
  페이로드만, 실 제출은 프론트 same-origin 재호출(#UI-1 답습).
- **fail-CLOSED**: 분류 실패→chat. fail-open(불확실→task/note/svg) 금지.
- **잔여 BL-3**: 대화 입력→claude argv redaction 미적용(플러그인 세션과 동일, 비례 평가).

## 7. 합의 권고

CLAUDE.md §3 **3+1 합의 필수**(기존 note/svg 동작 변경 = 큰 변경 + 분류 의사결정):
- **Agent A** 구현가능성: 단일 결합 호출 structured output 실현성, classify_for_routing 확장,
  latency 실측.
- **Agent B** 안전/신뢰경계: fail-CLOSED 4-way, BL-1 부작용 0 보존, note/svg 회귀 위험.
- **Agent C** 대안: 백엔드 LLM 분류 vs 규칙+LLM 하이브리드 vs detectMode 보강(최소 변경) vs
  명시 모드 버튼(분류 회피).
- **Reviewer**: 교차 비교 + BLOCKING + latency/회귀 트레이드오프.

## 8. 다음 단계
검토 → (필요 시 갈림길 사용자 선결) → 3+1 합의 → TDD. before-state 측정(§1)은 수정 후
대조 기준. 자동 진입 0.
