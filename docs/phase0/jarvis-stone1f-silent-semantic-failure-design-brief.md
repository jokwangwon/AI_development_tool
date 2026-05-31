# 디딤돌1f — silent semantic failure (능력-의도 불일치) 설계 brief

> **상태**: **v1.1** — 3+1 합의(4 source, REVISE→AWC) 흡수(BL-1~10) + 사용자 §6 결정. 구현 진입 승인됨.
> **작성**: 2026-05-31 세션 (실 사용 dogfooding 발견 #1)
> **선행**: 디딤돌1a(plan-then-execute) · 1b(artifact contract, ADR-013 능력 경계) · 1c(암묵 contract) · 1d(frontier planner) · 1e(human planner)
> **합의 보고서**: `docs/review/3plus1-consensus-2026-05-31-jarvis-stone1f-silent-semantic-failure.md`
> **방법론**: SDD (코드 전 설계) + 단계별 합의 (brief → 승인 → 3+1 합의 → **brief v1.1** → TDD)

---

## v1.1 변경 이력 (3+1 합의 흡수 — BL-1~10)

> 4 source(A/B/C + codex). A·B·codex=AWC, C=REVISE → 종합 **REVISE→AWC**. 핵심 정정 = brief v1 이 후보 A/B/C/D 를 *상호배타 경쟁*으로 프레이밍했으나, 실제로는 **단일 원인(exit code=의미성공 가정)이 3 layer 에 걸쳐** 조치가 합산됨. → §4 를 layer 통합안(F1~F4)으로 재구성.

| # | BLOCKING | v1→v1.1 | 출처 |
|---|---|---|---|
| BL-1 | 후보 A 라벨 "file=텍스트만" 부정확 | "현 HUD file alias=writer 없는 OllamaWorker(`output_filename=None`)→파일 미작성, **배선 의존**" 명시(ADR-013 §2.2 답습) | B·codex·C (3/4) |
| BL-2 | 후보 B(NL desc 차단)=§2 위반 | B "차단" **폐기**(4/4 만장일치). 탐지는 F2 구조적 선언으로 대체. NL은 F4 표시만 | 4/4 |
| BL-3 | feedforward 누락(후보공간 편향) | §4를 F1~F4 layer 통합안으로 재구성. F1(boss_plan_prompt 능력 1줄) 신규 | C·codex |
| BL-4 | COMPLETED 정직화 범위(문서만 부족) | controller+orchestrator+HUD label/card 코드 포함 | codex |
| BL-5 | advisory 책임 분리 | ReviewGuard 불변, 기존 orchestrator.advise + HUD plan 카드 재사용 | codex·A |
| BL-6 | scope=code 워커 동형 | §3.5에 명문화 + applied 라벨 worker_kind-무관 일반화. #3 결정적 차단은 후속 | 4/4 |
| BL-7 | §1 정직 단서 — file-only 구성 기인 | dogfooding 이 file-only 구성(jarvis_plan.py:63)에도 기인 | C ⭐4 |
| BL-8 | E2(requires_execution)=ends 속성 | F2에 포함(사용자 Q1). PLAN-INV 위반 아님 | C |
| BL-9 | ADR-013 produce 사각지대 미문서화 | ADR-013 §6 보강 1줄 | B·C |
| BL-10 | 발견#2 ledger 이중기록 | 1f 선행 fix | B-3 |

---

## 1. 배경 / 문제 — 실 사용 dogfooding 이 드러낸 갭

직전까지의 dogfooding 은 모두 토이 케이스(`add(a,b)`, "실행" 요구 없음). 113 entry 정직 단서가 "복잡 케이스 미검증"을 인정. 이번 세션에서 **HUD 브라우저 end-to-end + 비-토이 작업("회문 판별 함수 + 예시 입력 판별 결과 출력")** 을 file/code 워커로 실측.

### 실측 결과 (HUD, 8769)
- **file 워커(ollama)**: 약한 boss 가 3-subtask 분해 → subtask 2 = "테스트 코드를 *실행*하여 결과 출력". file 워커는 실행 능력이 없어(ADR-013 능력 경계) 코드를 **텍스트로 재출력** → exit 0 → `applied=True` → **plan COMPLETED**. 사용자가 요청한 실제 판별 출력은 *나오지 않았는데도* "완료".
- **code 워커(claude+레벨2 격리)**: 2-subtask 분해(약한 boss 비결정). claude 는 실 실행 능력이 있어 `palindrome.py` 가짜홈/work 실제 생성 + 실행 결과 산출 → COMPLETED(의미적으로도 성공). **단 발견 #3**: subtask 0 이 "어떤 언어로?"/"저장 필요하면 말씀" 대화형 되묻기 → 헤드리스라 아무도 답 못 받는데 `applied=True`.

### ⚠️ 정직 단서 (BL-7) — 실측은 구성 오류에도 기인
HUD 기본 배선(`jarvis_plan.py:63`)은 `real_workers=False` 시 boss 에게 **`("file",)` 단일 옵션만** 제공. 즉 boss 는 실행이 필요한 작업을 받고도 file 외 선택지가 없어 file 로 "실행" subtask 를 낼 수밖에 없었다. 실측 실패는 *설계 갭(능력-의도 미검증)* + *dogfooding harness 구성(무능력 워커만 제공)* 양쪽에 기인. `real_workers=True` 구성에선 boss 가 code 를 선택할 수 있었음.

### 핵심 문제
> **워커의 *능력*과 subtask 가 요구하는 *행위*가 불일치할 때, 하네스가 이를 감지하지 못하고 "완료"로 보고한다.**

사용자 신뢰 직결 — "완료라는데 결과가 없다". detection runbook(107)·능력 경계(ADR-013)가 *부작용*(실행 위험)은 다루지만, *능력 부족으로 인한 무의미 통과*(under-capability silent pass)는 사각지대.

---

## 2. 근본 원인 (코드 실측 — 라인 재확인 완료)

| 위치 | 현 동작 | 갭 |
|------|---------|-----|
| `orchestrator.py:130` | **완료감지 = exit code 만**(`if result.is_error:` 만 게이트 미진입 분기) | "지시한 행위를 실제로 했는지" 미검증 |
| `orchestrator.py:151-153` | `status = APPLIED if approved`, `applied=approved` | applied = 승인 여부일 뿐, 의미 달성 아님 |
| `review.py:19-46` | ReviewGuard = **파괴적 명령 정규식**(rm -rf 등 10개)만 | 의미 충족 검증 0 (모듈 docstring 이 "완전성 비주장" 자인) |
| `plan_controller.py:51, 322-327` | 능력 경계(`SAFE_CONSUME_KINDS`, `_consume_ok`) = **artifact 를 *consume* 하는 워커**만 제한 | "실행 요구 produce subtask 가 무능력 워커로 라우팅"은 검증 범위 밖 |
| `plan_controller.py:307` | `PlanOutcome(COMPLETED, "전 subtask 반영 완료")` | "반영"≠"의도 달성" 미명시 |
| `jarvis_plan.py:226, 247` | subtask dispatch=auto-accept(`lambda r: True`) + `Orchestrator(...)` **boss=None**(advisory 미작동) | dispatch 의미 검증 0 + advisory 경로 미활성 |
| `boss.py:388-401` | `boss_plan_prompt` 가 worker_kind 를 **enum 이름만**(`code | file`) 안내, 능력 설명 0 | boss 가 "file=실행 불가"를 모른 채 실행 subtask 를 file 로 분류(1차 트리거) |

→ **단순 버그 아님 — 설계 공백.** worker_kind(`code`/`file`)는 ADR-013 상 "산출물 형태/consume 안전성" 의미인데 "행위 능력"(실행 가능 여부)과 우연히 1:1 일 뿐 **개념적으로 분리 안 됨**. 단일 원인(exit code=의미성공)이 feedforward·검증·보고 3 layer 에 걸침.

---

## 3. 정직성 경계 (over-claim 차단 — [[feedback_pass_scope_overclaim]])

- 이건 **silent *semantic* failure** — 보안 취약점 아님(실행 *부작용*은 능력 경계가 이미 차단). 신뢰성/UX 문제.
- "약한 boss 가 무의미 subtask 를 낸다"가 1차 트리거(94 재현)이나, frontier/human planner 도 능력-의도 불일치 plan 을 낼 수 있음 → *하네스* 가 잡아야 근본적(§2 계산적 우선).
- **완전 해결 불가** — "워커가 의미적으로 옳은 일을 했는가"는 일반적으로 결정 불가. 목표는 **흔하고 위험한 패턴(능력-의도 명백한 불일치)을 결정적으로 예방/표시 + 나머지는 정직하게 노출**. "silent failure 해결"로 부르면 over-claim.
- **F1(feedforward)는 무력하지 않다(BL-5 정정)**: brief v1 이 "planner 품질 개선만으론 부족"이라며 feedforward 를 평가절하했으나, 실제로는 feedforward 가 *시도조차 안 된 상태*(boss_plan_prompt 가 능력 안내 0). 가장 싼 layer 를 비워둔 채 비싼 센서를 논한 것 = 하네스 원칙 위반.

### 3.5 scope (BL-6) — file 한정 아님
- **file 워커 = capability absence**(실행 능력 부족) / **code 워커 = execution protocol absence**(헤드리스인데 대화형 되묻기, 발견 #3). 근본 동일 — "exit 0 = 의미 성공"이라는 `orchestrator.py:130` 단일 가정.
- F3 정직 표시는 **worker_kind 무관**하게 "applied=exit0+반영, 의미달성 미판정"으로 일반화 → #3 도 공통 커버.
- 발견 #3 의 *결정적 차단*(헤드리스 응답 불가 감지)은 **별건 후속**(사용자 Q4). 다른 종류라 scope 비대화.

---

## 4. 해결 방향 — 다층 통합안 (F1~F4, 합의 권고 + 사용자 결정)

> 단일 원인이 3 layer 에 걸치므로 조치는 *경쟁*이 아니라 *합산*. CLAUDE.md §2 피드백 루프 계층(가이드 Layer 0 ~ 센서) 정합. 우선순위(§2 계산적 우선): **F3 = F2 > F1 > F4**.

### F1 — feedforward (가이드, plan 생성 前)
`boss_plan_prompt`(`boss.py:382`)에 worker_kind 능력 1줄 추가:
> "file: 코드·텍스트를 *생성*만 함(실행·테스트 불가). code: 코드를 생성하고 *실제 실행*할 수 있음. 실행/테스트/결과 출력이 필요한 작업은 반드시 code 로 지정."

비용 ~0, dispatch 전 작동, false positive 0(차단 아님). 약한 boss 분류 품질 1차 개선.

### F2 — 결정적 검증 (센서, plan 검증 時·승인 前) — 사용자 Q1=(a)+(b)
- **(b) 구성 invariant + frozenset**: `EXECUTING_KINDS = frozenset({"code", "shell"})` 추가(`SAFE_CONSUME_KINDS` 패턴 답습). **실행 가능 워커가 registry 에 0개인데 실행류 plan 이 오면 plan 검증 단계 즉시 거부 + 사용자 안내**("실행이 필요하면 `real_workers=True` 필요"). silent failure → *시끄러운 즉시 실패*(GP-2 빈 artifact 중단 철학 동형).
- **(a) requires_execution 구조 선언**: boss schema(`_PLAN_JSON_SCHEMA`, `boss.py:345`)의 subtask 에 optional `requires_execution: bool` 추가(grammar 강제). controller 가 `requires_execution=True AND worker_kind not in EXECUTING_KINDS` → **게이트 경고**(차단 아님 — boss 자기선언 신뢰성 한계 때문). NL 마커 사전 *불요*(grammar 가 강제, 누락 시 default False 보수적). `requires_execution` 은 *ends 속성*(작업 성격)이라 PLAN-INV(means 틀 금지) 위반 아님(G-2).

### F3 — 정직 표시 (투명성, 보고 時) — BL-4, 4/4 필수
COMPLETED/applied 의미를 "exit0 + 반영, 의미 달성 아님"으로 정직화. **문서만 불가 — 코드 다지점**:
- `plan_controller.py:307` `PlanOutcome(COMPLETED, "전 subtask 반영 완료")` reason 문구
- `orchestrator.py:24-27` OutcomeStatus / `jarvis_plan.py:43-51` `_PLAN_STATUS` label
- HUD 승인 게이트(`index.html` 모달)·subtask 카드에 "file alias=실행/검증 안 함(현 배선: writer 없는 OllamaWorker, `output_filename=None`)" 라벨(BL-1 배선 의존 명시).

### F4 — advisory (추론적 보조, dispatch 後) — **구현 보류(2026-05-31)**
> 당초 사용자 Q2=채택. 보류 사유(정정됨): dogfooding(§7)상 약한 boss 의 실질 방어는 F1(라우팅 유도)+F3(정직 표시)이고, F4 advisory 도 **같은 약한 모델(boss.advise)**이라 약한 boss 갭을 못 메움(F2 무력과 동일 약점). 추가 가치 낮아 보류. HUD plan 경로 boss 주입 + 기배선 `OllamaBoss.advise`("의도 부합" 평가축) 표시 청사진은 보존 — 단 **frontier boss 를 advise 에 쓸 때** 가치 발생(약한 boss advise 아님). 발효 시 원칙: ReviewGuard 확장 금지·scrub 경유(BL-5)·차단 0·merge_flags union-only.

---

## 5. 부수 처리 (사용자 §6 결정)

- **Q3 발견#2 (ledger 이중기록) — 1f 동반(선행) fix**: `plan_controller.py:268` + `jarvis_plan.py:197` 둘 다 `plan_approved` 기록 → detection 기준선(107) 오염. 둘 중 하나 제거 또는 event 명 분리. F2~F4 검증 *전* 선행(깨끗한 ledger 위에서 검증).
- **Q4 발견#3 (code 대화형 되묻기) — 별건 후속**: execution protocol absence, 다른 종류. F3 정직표시가 공통 커버하되 결정적 차단은 후속.
- **Q5 ADR — ADR-013 §6 보강(1줄)**: "능력 경계 = consume 안전만 보장, produce 적합성(워커가 요구 행위 수행 가능 여부) 미보장 — silent semantic 사각지대"(BL-9). 신규 ADR 안 만듦([[feedback_ceremony_inflation]]). §7 의존: ADR-011 §2.1 교차확인(정직단서 추가라 영향 0).

---

## 6. 구현 결과 (TDD, 2026-05-31)
1. ✅ **BL-10 선행**: ledger 이중기록 fix (별도 PR #39, main 기반).
2. ✅ **F1**: `_KIND_CAPABILITY_HINT` + `boss_plan_prompt` 능력 안내 (커밋 d98d511).
3. ✅ **F2-1/F2-2**: requires_execution 구조필드 + schema/파싱 + EXECUTING_KINDS + 구성 invariant + CapabilityWarning (3ab9c2a, c26310e). ⚠️ 파싱 누락 버그는 ad84426 에서 fix(인터럽트 유실 — §7).
4. ✅ **F3**: COMPLETED reason 정직화 + 능력경고 HUD plan_view + index.html 모달 (16bd0de).
5. 🛑 **F4**: 보류(YAGNI) — §7 dogfooding 상 결정적 layer(F1+F2)가 실 ollama 약한 boss 에서 작동 → 추론적 보조 불요. 청사진 보존.
6. ✅ **BL-9**: ADR-013 §6.3 보강.
7. ✅ **검증**: 462 passed(회귀 0) + grimp NONE + secret PASS + dogfooding 재검증(§7 — F2 가 파싱 버그 fix 후 실 ollama 에서 정상 작동 확인).

> ⚠️ **커밋 위생 단서**: 세션 인터럽트로 F1~F3 의 *테스트* 가 깨진 중간 버전으로 커밋됨 → 정합화 커밋(e7f9a82)으로 GREEN 복구. 그 과정에서 보조 에이전트의 오진 2건(존재하지 않는 "_parse_bossplan 회귀" / 테스트 자체 IndexError 버그)을 메인이 실측으로 정정. source F1~F3 자체는 정상.

---

## 7. dogfooding 재검증 결과 (2026-05-31) — F2 실 ollama 경로 작동 확인

> ⚠️ 정직 이력(2중 정정): 본 절은 두 번 틀렸다가 실측으로 바로잡혔다. ① 초안 "약한 boss requires_execution 3/3 True 일관"(미검증 낙관) → ② "전부 False, 약한 boss 가 grammar 필드 의미 안 채움"(이것도 틀림 — 원인 오귀속) → ③ **진실**: `_parse_bossplan` 이 requires_execution 을 *읽지 않는 버그*(인터럽트로 F2-1 수정 유실)였고, 버그 수정 후 약한 boss 는 requires_execution 을 **정확히 생성**한다. [[feedback_pass_scope_overclaim]] — 실측 없이 원인 단정 금지.

- ✅ **F2-1 약한 boss 정상 작동(버그 수정 후)**: 실 ollama(qwen3-30b) 회문 작업 3회, `requires_execution` 정확 생성 — run1 `[F,T]`, run2 `[F,T,T]`, run3 `[F,T,T,T]`(함수 정의=False, 실행/출력=True). grammar-required 필드 + F1 prompt 안내가 약한 boss 에서도 작동.
- 🐛 **진짜 원인(수정됨)**: `_parse_bossplan`(boss.py)이 `requires_execution` 을 PlanSubtask 에 안 넘겨 *항상 False* 로 떨궜음(커밋 ad84426 fix). 이전 "전부 False" 관찰은 boss 약함이 아니라 **파서 버그**. 보조 에이전트의 "_parse_bossplan 회귀" 보고가 옳았음(메인 오진 정정).
- ✅ **F1 라우팅**: 3회 모두 실행 작업을 `code`(실행 kind) 라우팅 → happy path 능력-의도 불일치 0(경고 미발생 정상). F2-2 경고/구성 invariant 는 boss 가 *오라우팅*(실행요구를 비실행 kind)할 때 발동하는 안전망.
- **결론**: 결정적 layer(F1 라우팅 + F2-1 구조선언 + F2-2 검증)가 실 ollama 약한 boss 경로에서 작동. **F4(advisory) 보류 정당**(결정적 layer 충분, 추론적 보조 불요 — YAGNI).
- **잔여(정직)**: ① "의미적 정상 동작" 일반 검증은 결정 불가(완전 해결 아님 — §3). ② boss 가 requires_execution 을 *틀리게* 채우면(false negative) F2 무발동 — F1 라우팅이 보조 방어. ③ 발견#3(code 대화형 되묻기) 별건 후속.
