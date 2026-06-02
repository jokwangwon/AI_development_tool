# 설계 brief — #UI-2 강한동사 규칙 과오버라이드 narrow (v2, REVISE 반영)

> **상태**: 3+1 합의 REVISE 완료 → 최종 옵션 *결정* 사용자 회부 (`docs/review/3plus1-consensus-2026-06-02-jarvis-ui2-strong-verb-overtrigger.md`)
> **답습**: `docs/phase0/jarvis-conversation-task-routing-design-brief.md` (v3, #UI-1·#UI-2)
>   `docs/review/3plus1-consensus-2026-06-01-jarvis-ui2-mode-classification.md` (121 합의)
> **트리거**: 세션 122 [121 후속] dogfooding — auto 분류 RULE 분기 50% 정확도 발견
> **영향**: 분류 동작 변경 → CLAUDE.md §3 3+1 합의 필수 (note/svg 라우팅 회귀 위험)

---

## 1. 문제 (dogfooding 실측, 122 세션)

세션 121이 `classify_mode`에 도입한 **규칙 1차**(`_STRONG_TASK_RE`)는 강한 생성 동사가
있으면 LLM 호출 *전에* `task`로 확정한다(0ms, 결정적). 설계 가정(121 주석):
> "강한 생성 동사 = 명확한 task. note/svg 요청엔 안 나타남"

**이 가정이 dogfooding 으로 반증됨.** `_STRONG_TASK_RE` 의 `"만들"` 이 너무 광범위 —
svg/note 요청도 "만들어줘"를 흔히 쓴다.

### 실측 (`/tmp/dogfood_auto_classify.py`, 22 케이스, 실 ollama qwen3-30b)

| 분기 | 정확도 | latency |
|------|--------|---------|
| **LLM 분류** | **10/10 = 100%** | 평균 1044ms (첫 호출 워밍업 1893ms, 이후 ~0.9~1.0s) |
| **RULE (강한동사)** | **6/12 = 50%** | 0ms |
| 전체 | 16/22 = 73% | |

RULE 분기 오분류 6건 (전부 `"만들"`이 svg/note 의도를 task 로 강제):
- `다이어그램/흐름도/조직도 만들어줘` → task (svg 여야)
- `회의 내용 노트로 만들어줘` · `할 일 목록 만들어줘` · `요약 노트 만들어줘` → task (note 여야)

### ⭐ 핵심 통찰 — 판별자는 동사가 아니라 *목적어 명사*

규칙을 우회한 LLM-only 측정(`/tmp/dogfood_llm_only_classify.py`, 함정/엣지 3회 반복):

| 입력 | LLM-only 결과 | 자연 기대 | |
|------|---------------|-----------|---|
| `계산기 만들어줘. 정리 노트에서 쓸 수 있게` | **note (3/3 안정)** | task | ❌ LLM 실패 (규칙이 보완하던 #UI-2 함정) |
| `회의록 정리 노트 양식 만드는 프로그램 짜줘` | task | task | ✅ ("프로그램"·"짜줘"가 신호) |
| `다이어그램/흐름도 만들어줘` | svg (안정) | svg | ✅ LLM 정확 |
| `회의 내용 노트로/할 일 목록 만들어줘` | note (안정) | note | ✅ LLM 정확 |

→ **순수 규칙도(50%) 순수 LLM도(#UI-2 함정 안정 실패) 단독으론 불충분.**
`"만들"` 은 본질적으로 모호 — 판별자는 **목적어 명사**다:
- `계산기·프로그램·앱·스크립트 + 만들` = task
- `다이어그램·흐름도·노트·목록 + 만들` = svg/note

규칙이 *정확한 LLM 을 덮어쓰며* 정확도를 깎는 동시에, LLM 이 *못 잡는* 함정 1건은
규칙만 잡는다. 즉 둘의 강점이 상보적 — 단순 제거/유지가 아니라 **경계 재설정** 문제.

### latency (부수 발견)
"+1.1초"는 **강한동사 미포함 입력에만** 적용(LLM 분기). 강한동사 케이스는 0ms 즉답.
121 "분류-전용 1.1초"는 LLM 분기 한정으로 재확인 — 전체 평균은 RULE 단축으로 더 낮음.

---

## 2. 옵션 (합의 REVISE 반영 — 회귀 정량·over-claim 정정 + Alt 추가)

> ⚠️ **over-claim 정정(BL-2)**: 아래 정확도는 *측정 22+소수 케이스 한정* — detection≠prevention,
> 통계 일반화 아님. "100%"는 해당 배터리 한정값.

| 옵션 | 규칙 | #UI-2 함정 | svg/note 엣지 | 기존 테스트 회귀 | 비용 |
|------|------|-----------|--------------|---------------|------|
| **A** 명확동사만 | `"만들"` 제거, 구현/디버그/컴파일/짜줘/개발/배포/리팩터만 | ❌ LLM→note (함정 회귀) | ✅ | **1 FAIL** (L122) | 단순. 함정 1건 희생 |
| **B** 만들+SW명사 allowlist | `"만들"` 은 SW 산출 명사(계산기·프로그램·앱·스크립트·함수·모듈·사이트·서버·봇·게임…) 동반 시만 task. **2-트랙**(명확동사=무조건/만들=명사조건) | ✅ (계산기) | ✅ (명사 없음→LLM) | **0 FAIL** | 22케이스 회귀0. open-ended 명사목록 유지 부담(누락 시 LLM 폴백=대개 정확, fail-safe). "노트앱→task"는 설계결정(BL-B3) |
| **C** svg/note 명사 denylist | `"만들"` task 강제하되 svg/note 명사 동반 시 제외 | ❌ (함정에 "노트" 포함→제외→note) | ✅ | — | **구조 실패 → 탈락** |
| **D** 규칙 제거 | LLM 전적 신뢰 | ❌ note (함정 회귀) | ✅ | **2 FAIL** (L122+L140 mixed-intent) | 가장 단순. 명시 버튼 탈출구. LLM 88%(소표본). proposal 경로 더블 LLM |
| **Alt-1** 프롬프트 개선+규칙 제거 | `_STRONG_TASK_RE` 제거 + `_MODE_CLASSIFY_SYS`에 "판단=목적어 명사" 원리+함정 few-shot | ✅ (실측 3/3) | ✅ (실측) | 2 FAIL→테스트 재설계 | 유지보수 우위(명사목록 소멸). **함정 latency↑(~3.7s)**. 모델 교체 시 프롬프트 재검증. C가 실 ollama 검증(단 B 대비 우위 미입증=같은 케이스) |
| **Alt-2** 사후 하이브리드 | LLM 1차 → note/svg인데 강한동사+SW명사 공존 시만 규칙이 task로 덮음 | ✅ (추정) | ✅ (규칙이 LLM 정답 못 덮음) | 보존 추정 | 규칙 덮어쓰기 구조적 0. allowlist 부담 잔존. A·B 미평가 → 3순위 |

### 합의 권고 (REVISE)
**1순위 = 옵션 B** (결정성·테스트 고정·Provider 교체 영향0·22케이스 회귀0). C의 Alt-1
실측은 사실이나 신규 일반화 입력 2개가 전부 SW명사 명시라 **B 대비 우위 미입증**(둘 다 통과).
**B vs Alt-1(결정적 regex vs 추론적 프롬프트)은 121처럼 가치 판단 → 사용자 결정**(아래 §3).
옵션 C 탈락. A/D 는 121 합의가 결정적으로 막은 #UI-2 함정을 재회귀(supersede 안건).

---

## 3. 합의 결과 + 사용자 결정 회부

> 3+1 합의 완료(REVISE) — `docs/review/3plus1-consensus-2026-06-02-jarvis-ui2-strong-verb-overtrigger.md`.
> 통합 BLOCKING(BL-1 `_TASK_KEYWORD_RE` 분리·BL-2 over-claim 정정·BL-3 문서연쇄 v3 BL-4 +
> 옵션별 BL-B1~B3)은 합의 보고서 §3 참조. 사용자 결정 회부: **① B vs Alt-1 vs Alt-2
> ② 추가 측정 배터리 보강 여부**.

### (이하 합의 전 작성한 쟁점 원문 — 합의에서 다룬 것)

1. **B 명사 allowlist 완전성**: 어느 명사까지? 누락 시 fail-safe 인가(LLM 폴백 정확도 의존)?
2. **A/D 의 #UI-2 함정 재회귀 수용 가능성**: 명시 모드 버튼(transient)이 충분한 탈출구인가?
   121 합의는 함정을 *결정적으로* 막기로 했는데, 그 결정을 뒤집는가?
3. **혼합 의도 우선순위**: "노트로 만들어줘"는 task 인가 note 인가 — 설계 의도(혼합=task 우선)
   vs 사용자 자연 기대(note)의 충돌. 121 정직 단서가 예고한 지점.
4. **regex 유지보수 vs LLM 위임 경계**: 결정적 규칙을 어디까지 넓히고 어디서 LLM 에 맡길지
   (CLAUDE.md 계산적>추론적 원칙 vs 과적합 regex 의 취약성).
5. **측정 표본 한계**: 22+8 수기 케이스 — 통계 일반화 아님. 합의가 추가 배터리 권고할지.

---

## 4. 검증 계획 (합의 후 TDD)

- RED: `classify_mode` 가 svg/note + "만들" 엣지를 task 로 강제하지 않음 + #UI-2 함정은
  여전히 task (선택 옵션의 불변식) 테스트 추가.
- GREEN: 선택 옵션대로 `_STRONG_TASK_RE`(또는 분기 로직) 수정.
- REGRESSION: 기존 #UI-2 11 tests + 신규 엣지 배터리 green. 실 ollama e2e 대조 재실행.
- grimp 단방향 / secret PASS 유지.

## 5. 산출 (예정)
- 수정: `src/jarvis/conversation_routing.py` (`_STRONG_TASK_RE` 또는 규칙 분기).
- 테스트: `tests/jarvis/test_conversation_routing.py` 엣지 배터리.
- 문서: 본 brief + 합의 보고서 + 라우팅 brief v4 반영.
- evidence: `/tmp/dogfood_auto_classify.py`·`/tmp/dogfood_llm_only_classify.py`.
