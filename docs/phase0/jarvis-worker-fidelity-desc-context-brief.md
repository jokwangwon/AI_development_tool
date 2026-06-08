# Brief — 워커 충실도: desc 요약 손실 해소 (갭6)

> **목적**: dogfood(2026-06-08)가 실증한 갭6 — boss 가 상세 설계를 한 줄 desc 로 요약하며
> 워커가 *의도와 다른* 산출물을 만드는 문제 — 를 해소하는 첫 슬라이스 설계.
> **상태**: 설계 brief(사용자 검토 대기). 보안 함의 有 → 검토 후 풀 3+1 합의 권고.

---

## 1. 문제 (갭6, dogfood 실증)

plan `97462f94`: 합의 설계(주제→LLM 해석 / 캐릭터 **페르소나** / **panels**[컷·장면·흐름역할] /
대사 생성기로 persona 연계)를 명령에 담았으나, 워커 산출물은 **동작하지만 합의와 다름**
(룰베이스 random·페르소나 누락·panels→episodes). 워커는 "동작하는 것"은 만들지만
"합의한 그것"은 아님.

## 2. 현재 흐름 (정밀)

```
사용자 prompt(상세 설계)
  → board.create_plan: card["_prompt"] = prompt (원본 보존)
  → run_from_planner(planner, prompt, id):
        plan = planner.plan(prompt)      # boss 가 prompt → subtasks[].desc 로 *요약*
        self.run(plan, id)               # ★ prompt 더이상 안 넘어감
  → run → dispatcher(desc, sub_id, alias) # ★ 워커는 desc 만 받음
  → auto_orch.dispatch(desc, ...)         # jarvis_plan.py:232
```

- **원본 prompt 는 `plan()` 입력으로만 쓰이고 dispatch 단계에서 소실**(`run()` 은 plan 만 받음).
- `PlanSubtask.desc` = "워커에 전달되는 **실행 prompt**(untrusted instruction text)"(`boss.py:69`).
  boss = **untrusted planner**(PLAN-SOURCE 불변식). 즉 워커가 받는 유일 입력이 untrusted.

## 3. ⭐ 신뢰도 비대칭 (수정 방향의 핵심 근거)

| 입력 | 출처 | 신뢰도 |
|------|------|--------|
| `desc` | boss(LLM planner) 생성 | **untrusted**(요약·비결정·주입 가능) |
| 원본 prompt | **사용자 직접 입력** | **trusted**(상대적) |

→ 원본 prompt 를 워커에 전달하는 것은 untrusted desc 보다 **신뢰도가 높은** 입력을 더하는 것.
주입면 확대 우려의 통상 논리(워커 입력 증가=위험)가 여기선 **역방향**(trusted 입력 추가).

## 4. 수정 옵션

| | 방법 | 장점 | 단점 |
|---|------|------|------|
| A | boss 프롬프트 개선(desc 충실화) | 흐름 무변 | boss untrusted+비결정 → 약함, untrusted 텍스트만 늘림 |
| **B** | **dispatch 에 원본 prompt(trusted) 컨텍스트 동봉** | trusted 입력으로 충실도↑, 구현 단순 | run()/dispatcher 시그니처 확장, 다단계 시 Q3 |
| C | 구조화 계약(스키마 필드) 전달 | 가장 정밀 | boss 비결정 의존, 복잡 |

**권고 = B**: 워커가 desc(boss 분해 지시) + "사용자 원본 명령"(trusted 의도)을 함께 받음.
구현: `run()`/`run_from_planner` 가 prompt 를 dispatch 까지 전달, 워커 프롬프트에
`[원본 사용자 명령]`(trusted) + `[이 단계 지시=desc]` 구분 제시.

## 5. 안전 함의

- 원본 prompt = 사용자 trusted 입력(외부 비신뢰 아님) → 주입면 확대 아님(오히려 신뢰 입력).
- desc(untrusted) vs 원본(trusted) 을 워커 프롬프트에서 **명시 구분** — desc 가 원본을
  덮어쓰는 주입(boss 가 원본과 다른 지시 삽입) 방어: "원본이 진실, desc 는 이 단계 범위" 명문화.
- 다단계 artifact consume(allow_code_consume) 게이트는 **무변**(원본 prompt 는 artifact 아님).

## 6. 핵심 설계 질문 (검토/합의 대상)

- **Q1**: 원본 prompt 를 *모든* subtask 에 동봉 vs 첫 subtask/관련 부분만?
- **Q2**: desc 와 원본 충돌 시 워커 우선순위? (권고: 원본=의도 진실 / desc=이 단계 범위 한정)
- **Q3 ★**: 다단계 plan 에서 각 워커가 원본 전체를 보면 "자기 부분"을 넘어 전체를 하려 들
  위험. → 단일 subtask 는 안전(원본≈desc). 다단계는 "원본은 *맥락*, 네 작업은 desc 범위로
  한정" 명문화 or 첫 슬라이스를 **단일-subtask plan 한정**으로 좁힘.

## 7. 첫 슬라이스 권고 (좁게)

- **범위**: dispatch 에 원본 prompt 컨텍스트 동봉(옵션 B). **단일 subtask plan 우선**(Q3 회피),
  다단계는 후속 슬라이스(맥락/범위 명문화 설계 별도).
- **TDD**: `run_from_planner`/`run` prompt 관통 → dispatcher context 인자 → 워커 프롬프트
  조립(원본 trusted / desc 범위 구분). 회귀: 기존 desc-only 동작 보존, context 주입 시 워커
  프롬프트에 원본 포함 검증, untrusted desc 가 원본 신뢰표식을 위조 못 함(redaction/구분 토큰).
- **검증**: 동일 만화 명령 재현 → 산출물이 페르소나/panels 합의 스키마에 근접하는지 dogfood.

## 8. 합의 권고

desc=untrusted 경계를 건드리는 변경(워커 입력 구성) → **보안 관련 = 풀 3+1 합의**(CLAUDE.md §3).
brief 사용자 검토 → 합의 → TDD(별도 feature 브랜치, develop 베이스).
