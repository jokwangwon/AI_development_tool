# 3+1 합의 보고서 — #UI-2 `_STRONG_TASK_RE` "만들" 과오버라이드

> **일자**: 2026-06-02 (세션 122)
> **대상 brief**: `docs/phase0/jarvis-ui2-strong-verb-overtrigger-design-brief.md`
> **답습**: `docs/review/3plus1-consensus-2026-06-01-jarvis-ui2-mode-classification.md` (121 합의)
> **형태**: **REVISE** (조건부) — 최종 옵션 결정은 사용자 회부
> **에이전트**: A(구현)·B(품질/안전)·C(대안) 병렬 독립 + Reviewer 교차

---

## 0. 요약

세 에이전트 모두 **현 규칙의 "만들"이 문제이고 옵션 C(svg/note denylist)는 구조 실패로 탈락**에 일치. 권고는 갈림 — **A·B = 옵션 B(regex allowlist)**, **C = Alt-1(프롬프트 개선 + 규칙 제거)**. Reviewer가 핵심 주장 3개를 코드/실측 재확인 → **전부 사실**. 단 단일 정답 미수렴 → **결정성 포기 여부(B vs Alt-1)는 사용자 결정 영역**.

Reviewer 검증:
- **B 회귀 (사실)**: regex 시뮬 — A=L122 **1 FAIL**, D=L122+L140 **2 FAIL**, B=**0 FAIL**. brief 옵션표가 D의 L140(mixed-intent) 회귀 누락.
- **A의 `_TASK_KEYWORD_RE` 분리 (사실)**: L28-30 `_TASK_KEYWORD_RE`에 "만들" 독립 존재(L56-58 `_STRONG_TASK_RE`와 별개). server.py L305 proposal 경로는 `mode=="chat"` 후 `looks_like_task`로 별도. `_STRONG_TASK_RE` 수정이 자동 전파 안 됨.
- **C의 Alt-1 실측 (재현 성공)**: ALT1=6/6(BASE=5/6 함정 fail), 함정 3/3 안정, 신규 변형 2개 각 3/3. **단** "일반화 6/6"=신규 입력 *2개* × 3회(6개 아님), 전부 SW명사 명시 케이스. 함정 ALT1 latency=3676ms(BASE 1977ms). → **B를 같은 배터리로 안 돌린 비대칭 비교라 Alt-1 우위 미입증**(둘 다 같은 케이스 통과).

---

## 1. 교차 비교

### ① 일치 (Consensus)
- 옵션 C(svg/note denylist) **구조 실패** → 제외 (함정에 "노트" 포함 → 제외 → LLM → note).
- "만들"이 문제 핵심.
- fail-CLOSED 3중(예외/enum밖/빈값→chat) 세 옵션 보존 (L83-86).
- 명시 모드 버튼 = transient 결정적 탈출구 (server.py L283-289).
- 소표본 정직 — 통계 일반화 아님.

### ② 부분 일치 (Partial)
- 권고: A·B = 옵션 B / C = Alt-1.
- A/D 함정 회귀: 3개 동의. A가 이유 보강(함정은 LLM이 note 분류 → proposal 진입 차단 → `_TASK_KEYWORD_RE` 부분회수로도 못 구함).

### ③ 불일치 (Divergence)
- **계산적 regex(B) vs 추론적 프롬프트(Alt-1)** 경계 판단:
  - B(품질): regex 결정적·테스트 고정·회귀0. 잘못-task가 더 observable.
  - C(대안): 본질 추론적(목적어 명사 의미의도) → regex 과적합 취약, CLAUDE.md "진정 모호→추론적 허용"에 Alt-1 부합.
  - A(구현): B가 latency도 유리(SW명사 task 직행 → proposal 더블LLM 회피).
- Alt-2(사후 하이브리드): C만 제시(규칙을 LLM 뒤로 → 덮어쓰기 0). A·B 미평가.

### ④ 누락 (Gap)
- **A만**: `_TASK_KEYWORD_RE` 별개 + proposal 더블 LLM(classify→plan 2회). (검증)
- **B만**: B의 "노트앱/메모앱→task"(SW명사 "앱"이 note명사 이김)=설계결정이지 자명 fail-safe 아님 → 테스트+합의 명시 필요. brief "~100%" over-claim. 라우팅 brief v3 BL-4(혼합의도)와 동일 문제. (검증)
- **C만**: Alt-1 실측 + Alt-2 대안. (재현)

---

## 2. 핵심 쟁점 판정 — B vs Alt-1 vs Alt-2

**판정: 옵션 B 1순위 합의 권고, Alt-1 동급 후보로 사용자 회부.**

1. C의 Alt-1 실측은 진짜이나 **B 대비 우위 미입증** — 신규 일반화 입력 2개 전부 SW명사 명시 → B regex도 동일 100%. 비대칭 비교.
2. **결정성 트레이드오프는 사용자 영역**: B=regex 결정적(Provider 교체 영향0, 테스트 고정) / Alt-1=`_MODE_CLASSIFY_SYS` 의존(모델 교체 재검증, 121 결정적 차단 supersede). CLAUDE.md "계산적>추론적" vs "진정 모호→추론적" 경계는 가치 판단 → 단정 불가.
3. B의 명사 allowlist 유지보수 약점은 fail-safe로 비례 수용 가능. 단 "노트앱→task"는 설계결정 → 테스트+합의 명시.
4. Alt-2는 A·B 독립 검토 부재 + allowlist 부담 잔존 + LLM 뒤 배치로 SW명사 직행 latency 이점 상실 → 3순위 보류.

---

## 3. 통합 BLOCKING

### 옵션 무관 (어느 것을 택하든)
- **BL-1 `_TASK_KEYWORD_RE` 분리 인지**: `_STRONG_TASK_RE` 수정이 `_TASK_KEYWORD_RE`(L29) + proposal 경로(server.py L305)에 자동 전파 안 됨. 두 regex 별개 책임(분류 vs 라우팅). A/D 선택 시 proposal "만들" 거동 별도 결정.
- **BL-2 over-claim 정정**: brief "~100%"(L62,67) → "측정 22+소수 케이스 한정, detection≠prevention, 통계 일반화 아님". Alt-1 "100%"도 동일(신규 입력 2개·SW명사 명시 한정).
- **BL-3 문서 연쇄**: 라우팅 brief v3 BL-4(혼합의도 우선순위)를 v4에서 함께 해소. A/D 선택 시 121 합의 §1·§6-3 supersede 주석. CLAUDE.md §7 의존테이블엔 conversation_routing 부재(연쇄 의무 없음).

### 옵션별
- **B 선택**: BL-B1 2-트랙 분리(구현|개발|배포|디버그|컴파일|짜줘=무조건 task / 만들=SW명사 동반 시만, 함수 `any(n in text)` 권장) · BL-B2 SW명사 set/regex 모듈 로드 1회 compile(try 앞단 예외=fail-CLOSED 우회 방지) · BL-B3 "노트앱/메모앱→task" 동작 테스트 고정+합의 명시.
- **A 선택**: L122 테스트 삭제 금지 = 합의 안건(1건 회귀).
- **D 선택**: L122+L140 **2건 회귀** 명시 = 합의 안건 + proposal 더블 LLM 거동 인정.
- **Alt-1 선택**: 121 결정적 차단 supersede 명시 + 모델 교체 시 `_MODE_CLASSIFY_SYS` 재검증 의무 + 함정 latency 증가(~3.7s) 인정.

---

## 4. 합의 형태 — REVISE

**REVISE 조건**: BL-1~BL-3(옵션 무관) 반영 + brief 옵션표 "D=2건 회귀" 명기 + over-claim 정정.

**사용자 결정 회부**:
1. **B(결정적 regex) vs Alt-1(추론적 프롬프트)** — 실측 우위 미입증. 결정성·Provider 무영향(B) vs 유지보수·일반화·원칙부합(Alt-1) + 121 결정적 차단 supersede 여부. **합의 1순위=B**, 사용자가 "진정 모호→추론적" 우선 시 Alt-1.
2. (B·Alt-1 둘 다 회피 시) Alt-2 사후 하이브리드 추가 검토 여부.
3. 추가 측정 배터리(영문 표본 0, "만드는/제작" 활용형 미탐) 보강 여부.

**핵심 파일**: `src/jarvis/conversation_routing.py`(L28-30·L56-58·L68-87) · `jarvis_hud/server.py`(L241-247·L284-310) · `tests/jarvis/test_conversation_routing.py`(L122·L138-140).

**검증 evidence**: `/tmp/dogfood_auto_classify.py`·`/tmp/dogfood_llm_only_classify.py`·`/tmp/agentc_alt1.py`·`/tmp/agentc_stab.py`.
