# 3+1 합의 보고서 — 디딤돌1e HumanPlanner (사람 직접 plan 공급)

**일자**: 2026-05-30
**대상**: `docs/phase0/jarvis-stone1e-human-planner-design-brief.md` (v1)
**source**: Agent A(구현 분석가) · Agent B(품질/안전성 검증가) · Agent C(대안 탐색가) + codex(cross-vendor, gpt-5.5) — **4 source 병렬 독립 분석**
**종합 판정**: **APPROVE WITH CONDITIONS (만장일치 4/4) · BLOCKING 0**

> 설계 방향(얇은 어댑터, controller 변경 0, PLAN-SOURCE 불변식, over-claim 차단)은 4 source 전원 *구현 가능·견고* 판정. 설계 무효급 BLOCKING 0. 정정 = **서술 정합성(over/under-claim)** + **더 나은 구조**. 1b 합의(만장일치 AWC) 패턴과 동형.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus, 4/4 또는 3/4+)

| # | 합의 사항 | source |
|---|---|---|
| CS-1 | **판정 만장일치 AWC, BLOCKING 0** — 얇은 어댑터·controller 변경 0·신규 실행면(subprocess/net) 0 코드로 입증 | A·B·C·codex |
| CS-2 | **BossPlanner Protocol 만족** — `plan(prompt)->BossPlan` 단일 메서드, StubBoss 선례(boss.py:142) 동형. `run_from_planner`(plan_controller.py:143-156) 무수정 수용 | A·B·C·codex |
| CS-3 | **means/ends 참** — `BossPlan`/`PlanSubtask`/`Contract`(boss.py:60-108) means 틀(argv/alias/isolation/workdir) 필드 *물리적 부재*. `_parse_bossplan`(449-487)이 unknown field 무시 → 사람 argv 주입 무효 | A·B·C·codex |
| CS-4 | **Q1 (입력형태 A+B) 채택** — 파일 + BossPlan 객체 둘 다 | A·B·C·codex |
| CS-5 | **Q4 (승인 게이트 유지) 채택** — `_approve` fail-closed(plan_controller.py:310-317), HumanPlanner 가 게이트 우회할 코드 경로 구조적 부재 | A·B·C·codex |
| CS-6 | **Q5 (prompt 무시) 채택** — StubBoss.plan(boss.py:172-176)도 prompt 무시 선례. 불일치 검사 = 추론적/over-engineering(CLAUDE.md §2) | A·B·C·codex |
| CS-7 | **non-adaptive (c) 유지** — dispatch 루프 planner 재호출 0(plan_controller.py:273-305) | B·codex |

### ② 부분 일치 / 불일치 (Divergence) — ⭐ Q2 모듈 위치

**진짜 분기 (2:2)**:

| source | 입장 | 논거 |
|---|---|---|
| A | **planner.py** | "plan 공급원 어댑터" 군집, HumanPlanner import 추가 0, 레이어 변경 0 |
| codex | **planner.py** | CliPlanner 와 같은 어댑터 모듈, boss.py 순수 boss/파서 영역 안 키움 |
| B | **boss.py 대안 더 안전** | planner.py 는 `import subprocess`(planner.py:27) 보유 → HumanPlanner "실행면 0" 주장과 *모듈 응집성* 충돌 |
| C | **boss.py 자연 + C-2 제3안** | StubBoss(순수 plan 반환, boss.py:142-176)가 더 자연스러운 이웃. *제3안*: 클래스=boss.py 순수 / `from_file` 팩토리=planner.py(IO 분리) |

**Reviewer 판단**: B/C 의 "실행면 0 ↔ subprocess 모듈" 응집성 논거가 더 설득력 있으나, **추가 통찰로 분기 해소**: boss.py 는 *이미 순수하지 않다* — `OllamaBoss.advise/plan`(boss.py:432)이 `urllib` **HTTP IO** 를 수행한다. 즉 boss.py 의 "순수 추론(부작용 0)" 서술(boss.py:1-19)은 *외부 LLM SDK import 0·HTTP 라이브러리 미의존*을 뜻하지 파일/네트워크 IO 부재가 아니다.
- boss.py IO = **plan 공급원 본체가 plan 데이터를 가져오는 IO**(OllamaBoss=HTTP, HumanPlanner=파일 read) — 동질.
- planner.py IO = **외부 CLI 명령 실행면**(subprocess, 격리 필요한 종류) — 이질.
→ HumanPlanner(파일 read)는 OllamaBoss(HTTP read) 와 대칭이므로 **boss.py 가 더 정합**. planner.py 는 "외부 CLI 실행=격리 필요" 공급원 전용 유지. **단, 이는 사용자 결정(Q2)으로 회부** — A/codex 의 "어댑터 군집 단순성"도 유효.

### ③ 누락 (Gap) — 특정 source 만 포착

| Gap | 포착 | 평가 |
|---|---|---|
| G-1 ⭐ **Q3 "schema 검증" 과장** — `_parse_bossplan` 은 관대 파서(depends_on 누락→[], contracts 누락→[], unknown field *무시·거부 아님*). `_PLAN_JSON_SCHEMA`(additionalProperties:False)는 ollama format grammar 경로 한정 | A·B·codex (수렴) | **흡수**(CN-1) — "schema 형식 검증" → "동일 JSON shape + 방어 파싱" 정정 |
| G-2 **under-claim "외부 주입 경로 아님"** — `from_file(path)` 임의 경로 수용. HUD 후속에서 plan.json 이 워커/외부 산출 가능 | B·codex | **흡수**(CN-2) — 조건부 주장으로 정직화. subprocess/net 0 은 정확 유지 |
| G-3 **rubber-stamp approver** — 게이트 *존재* ≠ *실효*. 항상 True approver 주입은 기능적 스킵(구조적으로 못 막음) | B | **흡수**(CN-6) — 비례성상 허용하되 정직 명시 |
| G-4 **StubBoss 중복** — StubBoss(boss.py:155,172)가 이미 "객체 직접 반환 + prompt 무시" → (B) 경로와 행위 동일. 차별성=from_file + "테스트 stub 의미오염 회피" | C (codex 약하게) | **흡수**(CN-5) — §1 에 HumanPlanner≠StubBoss 명시 |
| G-5 **from_file 예외 수렴** — OSError/빈파일/malformed JSON/UnicodeDecodeError → RuntimeError 단일(PLAN_UNAVAILABLE 정합). +`_strip_code_fences` 답습 | A·C·codex (+B fence) | **흡수**(CN-3) |
| G-6 **파일 크기 상한 부재** — `fh.read()` 무제한(DoS 표면). 자기 파일 비례성상 무해 | B | **흡수**(CN-6) — 1줄 명시 |

---

## Phase 4 — 합의 도출 (v1.1 흡수 조건)

설계 무효급 0 → **흡수 조건 CN-1~CN-6** (정직성·정합성·구조). 1b 패턴(BLOCKING 0, 정정=서술+더 강한 구조) 답습.

- **CN-1 (Q3 정정 ⭐, 4/4)**: §1/§3/Q3 의 "`_PLAN_JSON_SCHEMA` 형식 *검증*" → **"동일 JSON shape + `_parse_bossplan` 방어 파싱(관대 — 누락 기본값·unknown 무시, strict 거부 아님). 의미검증(enum/DAG/범위)은 controller §3"**. A 권고2·codex 권고1·B 동일.
- **CN-2 (under-claim 정직화, B·codex)**: §2 "외부 주입 경로 아님" → **"현 1e = 사람 직접 작성 가정. `from_file` 은 임의 path 수용 — plan.json 이 워커/외부 산출이 되는 HUD 후속 시 이 가정 재검토"**. subprocess/net 실행면 0 은 정확 유지.
- **CN-3 (예외 수렴, A·C·codex·B)**: `from_file` 이 OSError·빈/공백 파일·malformed JSON·UnicodeDecodeError 를 **`RuntimeError("HumanPlanner plan 파일 읽기/파싱 실패: ...")` 단일 수렴**(run_from_planner PLAN_UNAVAILABLE 정합). `_strip_code_fences` 답습(fence 무해 흡수) — CliPlanner(planner.py:129-141) 패턴.
- **CN-4 (객체/파일 분리, A·C·codex)**: `HumanPlanner(plan: BossPlan)` + `HumanPlanner.from_file(path)` **분리**(생성자 동시 지정 구조 회피). C-2 제3안(IO 자유함수 분리)은 Q2 결정과 연동.
- **CN-5 (StubBoss 차별화, C)**: §1 에 **"HumanPlanner ≠ StubBoss: (1) from_file 실사람 경로 (2) 테스트 stub 의미오염 회피·관찰필드(plan_calls/fail) 부재 = 프로덕션 plan 공급원"** 1줄. codex 권고5(plan_calls 불요) 동조.
- **CN-6 (게이트 실효·크기 정직, B)**: §2 에 **"승인 게이트 *존재* 보장 ≠ *실효* 보장 — rubber-stamp approver 주입은 구조적으로 못 막음(비례성상 허용)" + "파일 크기 상한 미적용(자기 파일 비례성)"** 명시.

### 사용자 결정 필요
- **Q2 (모듈 위치)** — boss.py(OllamaBoss IO 대칭·StubBoss 이웃, Reviewer 약권고) vs planner.py(어댑터 군집·A/codex) vs C-2 분리. **2:2 분기 → 사용자 결정.**
- Q1/Q3/Q4/Q5 = 합의 수렴(CN 흡수).

---

## Phase 5 — 권고

**v1.1 = CN-1~CN-6 흡수 + Q2 사용자 결정 → 디딤돌1e TDD 구현 진입**. 신규 표면 최소(어댑터 1클래스 + 팩토리 1), 코어 변경 0, controller 무수정. 4 source 전원 구현 가능 동의. 정직성 정정(CN-1 over-claim, CN-2/CN-6 under-claim)이 `feedback_pass_scope_overclaim` 양방향 답습.
