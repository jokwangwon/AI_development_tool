# 설계 brief — #UI-2 백엔드 통합 모드 판정 (detectMode 키워드 폐기)

> **상태**: v1 (사용자 검토 대기) · **출처**: 119 발견 #UI-2 + 120 세션 정확성 측정
> **상위**: `jarvis-conversation-task-routing-design-brief.md`(#UI-1, BL-4가 이 충돌 예측)
> **핵심 명제**: 프론트 `detectMode` 키워드 게이트를 **백엔드 LLM 문맥 분류**로 대체
> **다음 단계**: 검토 → 3+1 합의(기존 note/svg 동작 변경 = 큰 변경) → TDD (자동 진입 0)

---

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

### 5-1. 분류 계약
- 입력: raw message. 출력: `{mode: chat|note|svg|task, (task면) prompt, subtask_count}`.
- 위치: 백엔드(`conversation_routing` 확장 또는 신규 `classify_mode`). 프론트는 hint 없이 raw 전송.
- fail-CLOSED: 분류 실패·모호 → **chat**(가장 안전 — 원치 않는 작업/캔버스 부작용 0).

### 5-2. 핵심 갈림길 (검토/합의 결정)
1. **호출 수 / latency** ⭐ → **▶ 사용자 결정: (a) 단일 결합 호출**(1회 LLM이 분류+생성
   동시, structured output `{mode, content/parsed}`). note/svg latency 회귀 0. 합의 안건 =
   결합 프롬프트 설계 실현성(분류+4-way 생성 한 호출에 + structured output 파싱 견고성).
2. **task 처리**: task 분류 시 (a) chat 답변 생성+proposal 동반(현 동작 유지) vs (b) 생성
   스킵하고 proposal만. 현재는 chat 답변 안에 proposal. (단일 결합 호출 채택 → task도 한
   호출에서 분류+chat답변+proposal 산출 형태 검토.)
3. **명시 override** → **▶ 사용자 결정: 명시 모드 버튼 추가**. 백엔드 자동 분류가 기본,
   chat/노트/도식 버튼으로 사용자 강제 가능(분류 오류 시 deterministic 탈출구). 버튼 지정 시
   해당 mode 고정(분류 스킵). 합의 안건 = 버튼 UX + "auto" 기본 상태 표현.
4. **프론트 hint 잔존 여부**: 완전 raw vs 약한 prior(detectMode를 hint로만, 백엔드가 최종).
   (명시 버튼 채택 → 버튼 미지정=auto는 완전 백엔드 분류, detectMode 정규식 폐기.)
5. **분류 신뢰도/임계**: LLM 분류의 fail-safe 방향 + 저신뢰 시 chat 강등 임계.

**▶ 사용자 결정 요약 (검토 시)**: 갈림길1 = 단일 결합 호출 / 갈림길3 = 명시 모드 버튼
추가(auto 기본). 나머지(2·4·5)는 합의에서 결정.

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
