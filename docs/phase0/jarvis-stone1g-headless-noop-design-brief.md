# 디딤돌1g — headless 워커 no-op silent pass (발견#3 대화형 되묻기) 설계 brief

> **상태**: **v1.1** — 3+1 합의(3 source A/B/C + Reviewer, **REVISE**) 흡수(BL-1~7) + 사용자 §6 결정 + PoC(BL-7 해소) 반영. 구현 진입 승인 대기.
> **작성**: 2026-05-31 세션 (실 사용 dogfooding 발견 #3 후속)
> **선행**: 디딤돌1f(silent semantic failure, BL-6 에서 "#3 결정적 차단은 후속"으로 명시 스코핑) · 1a~1e · ADR-013(능력 경계)
> **합의 보고서**: `docs/review/3plus1-consensus-2026-05-31-jarvis-stone1g-headless-noop.md`
> **방법론**: SDD (코드 전 설계) + 단계별 합의 (brief → 승인 → 3+1 합의 → **brief v1.1** → PoC → TDD)
> **해결 차원(사용자 선택)**: **G2 결정적 센서 + G3 정직 보고**. G1 feedforward 및 means 레버는 §5 별건.

---

## v1.1 변경 이력 (3+1 합의 REVISE 흡수 — BL-1~7 + PoC)

> 3 source(A/B/C) 모두 brief v1 의 **"fs-delta 단독 1순위 신호 + orchestrator dispatch 스냅샷"을 거부**. Reviewer 가 코드 직접 재검증(V-1~V-5)으로 두 핵심 오류를 확정 → **신호 설계를 `did_act` 추상으로 재정렬, 측정 위치를 worker/runner 로 이동**.

| # | BLOCKING | v1 → v1.1 | 출처 |
|---|---|---|---|
| **BL-1** | **측정 위치 오류** — orchestrator 가 만든 `/tmp` workdir 를 claude 는 *안 씀*(실 cwd = 가짜홈 `work/`). dispatch 스냅샷 = 정상 작업도 100% 오탐 | Q6 "dispatch 권위" **폐기**. 측정 = **worker/runner 실 cwd**. §2/§3/Q6 재작성 | A BLOCK-1 (Reviewer V-1/V-2 코드 확정: `worker_setup.py:135-141` runner 가 workdir 인자 무시, `:185` rw_root=가짜홈) |
| **BL-2** | 스냅샷 루트 = home/rw_root 면 claude `.claude/` 캐시 쓰기로 **항상 delta≠0 → false negative** + symlink/DoS/escape | 스냅샷 루트 = **`work/` 전용**(산출물 디렉터리, 캐시 제외) + `followlinks=False` + realpath 경계 + 엔트리/크기 상한 + fail-OPEN | A-3 ④ · B-3 ③ |
| **BL-3** | **신호 의미 오류** — `requires_execution`="실행"이지 "fs 변형" 아님. fs-delta 를 req_exec 로 게이팅하면 **1f happy-path(`[F,T]` stdout 출력) 오탐(FP-5)** | fs-delta 를 req_exec 로 직접 게이팅 **금지**. 신호를 **`did_act` 추상**으로, 발화 = `did_act is False ∧ requires_execution`. fs-delta = did_act None fallback | B BL-B1 (Reviewer V-3: `boss.py:424` req_exec 의미 + 1f §7 실측 `[F,T]`) |
| **BL-4** | 차단(SUBTASK_FAILED) MVP 도입 = 시기상조 (2/3 반대) | **MVP = 경고-only**(1f `CapabilityWarning` 동형, `plan_controller.py:97/101` 재사용). 차단은 오탐률 실측 후 별건 | B BL-B2 (사용자 Q 확정: 경고-only) |
| **BL-5** | fail-OPEN 의무 + "이중신호"가 stdout 내용 NL 판단으로 미끄러지면 1f BL-2 재위반 | 스냅샷/did_act 실패 = **통과**(센서=보조신호, ApprovalGate 만 fail-closed). 신호는 길이/존재(결정적)까지만, 내용 NL 판단 금지 | B BL-B4 · B-4 ③ |
| **BL-6** | over-claim 금지 — "no-op 결정적 탐지"는 양방향 부정확(touch 위조 fn + producer/stdout fp) | 보고 문구 = **"효과 미관측"**(중립). "아무것도 안 함" 단정 금지. detection≠prevention | B BL-B5 · C-4 |
| **BL-7** | did_act claude 구현(tool-use 노출) 미실측 + means 레버 별건 | **PoC 완료(아래) — `num_turns` 가 프록시**. means 레버는 §5 별건 등재(사용자 Q 확정) | C-1·C-6 → PoC |

### PoC 결과 (BL-7 해소 — 2026-05-31 실측, claude 2.1.158)

`claude --output-format json --dangerously-skip-permissions -p <prompt>` 엔벨로프 실측:

| 케이스 | `num_turns` | 로컬 도구 | 산출 |
|--------|-------------|-----------|------|
| 파일 생성 작업 | **2** | Write 사용 | 파일 생성됨 |
| 텍스트-only ("OK") | **1** | 없음 | 없음 |
| #3 재현("회문 함수 정의") | **8** | 다수 | `palindrome.py` 생성+실행 |

- **발견 1 — did_act 신호 실재**: 엔벨로프는 로컬 tool-use(Write/Edit/Bash) 카운트를 *직접* 노출하지 **않음**(`server_tool_use` 는 web 전용). **그러나 `num_turns` 가 신뢰 가능한 프록시** — `num_turns=1` ⟺ 텍스트-only/무행동, `num_turns≥2` ⟺ 도구 행동 1회 이상. → claude `did_act = (raw["num_turns"] > 1)`. `WorkerResult.raw`(`worker.py:42`)에 이미 보존됨 → 추가 파싱 0.
- **발견 2 — #3 는 비결정적**: 동일 프롬프트가 이번엔 작업을 *정상 수행*(num_turns=8). 지난 세션엔 되묻기(tool 0, num_turns=1 추정). → **#3 되묻기는 간헐적** → **경고-only(BL-4) 강력 뒷받침**(차단했다면 동일 작업이 간헐 사망).
- ⚠️ 한계: `num_turns` 는 "도구를 한 번이라도 썼나"이지 "fs 를 바꿨나"가 아님. Read-only 도구만 쓰고 되물으면 num_turns≥2 인데 무산출(false negative 잔여). 단 순수 되묻기(#3 원형, tool 0)는 정확히 잡음.

---

## 1. 배경 / 문제 — 발견 #3 (실측 재확인)

디딤돌1f 가 발견 #1(능력 부족 silent semantic failure)을 다뤘고, 같은 dogfooding 에서 **발견 #3** 을 별건 후속으로 분리했다(1f brief BL-6). 이 brief 가 그 후속이다.

### 실측 재확인 (가짜홈 claude 워커 세션 로그)
가짜홈(`~/.jarvis/claude-home/.claude/projects/.../4ba1bc3c-….jsonl`)에 #3 가 보존돼 있었다:

```
USER(subtask desc): 회문 판별 함수를 정의한다.
ASST: 어떤 언어로 작성할까요? 별도 지정이 없으면 Python으로 작성하겠습니다.
      ```python
      def is_palindrome(s): ...
      ```
      파일로 저장이 필요하면 말씀해 주세요.
TOOL_USE count = 0   ← Write/Edit/Bash 0회 = 파일 미작성
```

- claude(`code` 워커, 레벨2 격리)가 모호한 subtask 를 받고 **작업을 *수행*하는 대신 대화형으로 되물었다**: "어떤 언어로?" + 인라인 코드 + "파일로 저장이 필요하면 말씀해 주세요".
- **TOOL_USE 0회**(=PoC 의 `num_turns=1` 신호) → workdir 에 파일을 만들지 *않았다*.
- 그럼에도 claude headless 는 `exit 0` + JSON `is_error=False` 반환 → `orchestrator.py:130` 통과 → 게이트 → `applied=True`.
- plan 의 producer subtask 였다면 `_extract_artifact` 가 이 *질문 텍스트* 를 artifact 로 추출(비어있지 않음) → 후속 subtask 로 전달 → **plan COMPLETED**.

### 핵심 문제
> **headless(비대화) 컨텍스트에서 워커가 *대화형으로* 행동(되묻기·확인 요청)하여 실제 작업을 0 으로 수행했는데, 아무도 그 질문에 답할 수 없음에도 하네스가 exit 0 만 보고 "완료"로 처리한다.**

#1(능력 부족)과 다른 종류: 여기선 워커가 **능력은 있으나**(claude 는 파일 쓸 수 있음) **execution protocol 의 부재**로 *대화 상대가 있다고 가정* 하고 작업을 미루었다. 공통점은 **exit 0 = 의미적 성공이라는 잘못된 등식**(1f 근본 원인과 동일 뿌리, 다른 발현). ⚠️ PoC 발견 2 대로 **간헐적**이다.

---

## 2. 근본 원인 (코드 실측 — Reviewer V-1~V-5 재확인)

| 위치 | 현 동작 | 갭 |
|------|---------|-----|
| `worker.py:75` | `is_error = nonzero or raw.get("is_error")` | headless 워커가 "되물음·무작업"이어도 exit 0·is_error=False → 거짓 성공 |
| `orchestrator.py:130` | 완료감지 = `if result.is_error:` 만 | "지시한 *효과*를 실제로 냈는지" 미관측 |
| `plan_controller.py:331-342` | producer = `_extract_artifact(output).strip()` 비어있지 않으면 통과 | 되물음 텍스트도 "비어있지 않은 산출물"로 인정 → 무작업이 artifact 로 둔갑 |
| **`worker_setup.py:135-141`** (V-1) | runner 클로저가 orchestrator 의 `workdir` 인자를 **무시**하고 `cwd=os.path.join(home,"work")` 사용 | **orchestrator 의 `/tmp` workdir 는 claude 가 안 씀** — 거기서 스냅샷하면 정상 작업도 delta=0 |
| **`worker_setup.py:185` + `isolation.py:100`** (V-2) | Landlock RW 루트 = 가짜홈(rw_root) | 워커는 `/tmp` workdir 에 **쓸 권한조차 없음** |
| **`boss.py:424`** (V-3) | `requires_execution=True` = "코드/명령을 *실제 실행*", false="생성·작성만" | req_exec = "**실행**"이지 "**fs 변형**" 아님. 실행 결과가 stdout 인 작업(1f `[F,T]`)은 fs-delta=0 이 *정상* |
| (전역) | 워커가 *무슨 효과를 냈는지* 결정적으로 관측 안 함 | 워커의 자기보고(exit code + 텍스트)만 신뢰 → 되물음일 때 빈틈 |

→ **설계 공백**: 하네스는 "워커가 *무엇을 했는지*(효과)"를 결정적으로 관측하지 않는다. **단 그 효과는 워커마다 다른 곳에 나타난다**(claude=가짜홈 work/ + tool-use, ollama=반환 텍스트/파일) → 측정 권위는 **워커 자신**이지 orchestrator 가 아니다(BL-1).

---

## 3. 해결 방향 — `did_act` 추상 + fs-delta fallback (합의 권고 + 사용자 결정)

> 핵심 통찰(합의): "워커가 무슨 *말*을 했는가"(NL 판단 — 1f 4/4 기각)도 아니고 "하네스가 추측한 효과(fs 변형)"도 아니라, **"워커 자신이 행동을 취했는가"를 워커가 결정적으로 보고**한다. provider-무관 인터페이스(`did_act`), 구현은 워커별.

### 권고 신호 설계 (합의 §4)

| 층 | 신호 | 측정 위치 | 성격 |
|---|---|---|---|
| **1순위** | `did_act: bool\|None` (`WorkerResult` 추상 필드) | **각 워커 내부** | 결정적, provider-무관 인터페이스 |
| **2순위(fallback)** | `work/` fs-delta(경로+`st_mtime_ns`+size) | **runner 클로저**(harness 소유, 워커 자기채점 아님) | did_act=None 일 때만. work/ 전용(캐시 제외), `followlinks=False`, 상한, fail-OPEN |
| **판정** | `did_act is False ∧ requires_execution` → `CapabilityWarning`(경고) | **PlanController**(기존 `capability_warnings` 재사용) | provider-무관, **차단 아님(MVP)** |
| **기각** | G2-b(controller 가 claude JSON 직접 파싱) | — | 헌법5조-2.2 위반. did_act 워커 경계로 대체 |

- **claude did_act**(PoC): `raw["num_turns"] > 1`. CliWorker 생성자에 `did_act_fn: Callable[[dict], bool|None]|None=None` 주입(기본 None=미상). worker_setup 이 claude 용으로 `lambda raw: raw.get("num_turns",0) > 1 if raw else None` 배선. **CliWorker 는 generic 유지**(num_turns 지식은 worker_setup wiring 에 격리) → provider-specific 이 controller 에 누출 0(헌법5조 정합).
- **ollama did_act**: `worker.py:353·358-359` 로직 재사용 — content 비어있음/파일 작성 여부로 결정(추측 0).
- **tmux did_act**: None(미상) → fs-delta fallback.
- **fs-delta fallback**: did_act=None 인 워커만. runner 클로저(worker_setup)가 자기 `work/` 를 실행 전후 스냅샷. **work/ 전용**(claude `.claude/` 캐시는 home 에 있어 제외 → false negative 회피, BL-2). `followlinks=False` + realpath 경계 + 엔트리/크기 상한 + **fail-OPEN**(실패 시 통과, BL-5).

### 왜 이 설계가 두 오류를 푸는가
- **BL-1(측정 위치)**: did_act 는 워커가 자기 cwd 에서 계산 → orchestrator 가 모르는 실 cwd 문제 소멸. fs-delta fallback 도 runner 클로저(실 cwd 아는 유일 지점)가 측정.
- **BL-3(FP-5)**: stdout-출력 정상 작업(claude 가 Bash 로 실행 → num_turns≥2 → did_act=True)은 발화 안 함. #3 순수 되묻기(num_turns=1 → did_act=False)만 발화. **req_exec 를 fs-delta 게이트로 직접 쓰지 않으므로** 1f happy-path 오탐 없음.

---

## 4. 사용자 §6 결정 (확정)

| Q | 결정 |
|---|------|
| Q1/Q2 신호+PoC | **PoC 먼저 → 결과로 결정**. PoC 완료: `num_turns` 프록시 확인 → **did_act 1순위 + fs-delta fallback** 채택 |
| Q3 발화 조건 | `did_act is False ∧ requires_execution=True` |
| Q4 차단 vs 경고 | **경고-only (MVP)** — `CapabilityWarning` 재사용, 차단 아님. (#3 비결정성이 차단을 부적절하게 함) |
| Q5 fs-delta 측정/루트 | **runner 클로저 + `work/` 전용** (변경 시 false negative) |
| Q6 means 레버 | **§5 non-goal 별건 등재** |
| Q7 G2-b | **기각** (헌법5조, 3/3 합의) |

---

## 5. Scope / Non-goal

**범위 내**: ① `WorkerResult.did_act: bool|None` 추상 필드(additive, default None) ② claude did_act (`num_turns>1`, worker_setup wiring) + ollama did_act (content/파일) ③ runner 클로저 `work/` fs-delta fallback(did_act=None 시, 보안 가드 + fail-OPEN) ④ PlanController 판정(`did_act is False ∧ requires_execution` → `CapabilityWarning`, **경고**) ⑤ G3 정직 보고(PlanOutcome/OutcomeReport/HUD plan_view — 1f F3 렌더 재사용) ⑥ ledger 이벤트(효과 미관측 관측) ⑦ 단위 테스트(주입 runner 트랙 A).

**범위 밖(non-goal)**:
- **G1 feedforward**(headless protocol system prompt) — 사용자 미선택. 별건.
- **means 레버(C-6)** — 워커 argv/env(`--append-system-prompt` 류, harness 소유 `worker_setup.py:46`)로 "되묻지 말고 즉시 실행" 봉쇄. desc 아님 = PLAN-INV 위반 아님, G1 과 다른 층위. ⚠️ claude `-p` 가 이를 강제하는지 **미실측(추측)** → 별건 PoC 필요. **이번 범위 제외, 별건 후보로 등재**.
- **차단(SUBTASK_FAILED)** — 오탐률 실측 후 별건(BL-4).
- **NL "되물음 여부" 탐지** — 1f 4/4 기각 답습(§2 위반). 효과/행동 부재만 본다.
- **"의미적 정상 동작" 일반 검증** — 결정 불가. did_act 는 "행동했나"만, "올바르게 했나"는 못 잡음.
- **인터랙티브 워커 일반 지원**(되묻기 자동 응답) — plan-then-execute human-in-loop 모델과 충돌. 별건.

---

## 6. TDD 스케치 (합의·승인 후 RED→GREEN)

- `test_workerresult_did_act_default_none`: 기존 생성 경로 did_act=None(하위호환·additive).
- `test_cliworker_did_act_fn_populates`: 주입한 did_act_fn 이 raw 로 did_act 채움(num_turns>1→True, =1→False, raw None→None).
- `test_ollama_did_act_from_content`: content 비어있음→False, 파일 작성/content 있음→True.
- `test_plan_controller_did_act_false_and_req_exec_warns`: `did_act=False ∧ requires_execution=True` → `CapabilityWarning` 발생(차단 아님 — applied 유지).
- `test_plan_controller_did_act_true_no_warn`: did_act=True 면 무경고(stdout-출력 정상작업 오탐 0, FP-5 회귀).
- `test_plan_controller_req_exec_false_no_warn`: req_exec=False 면 did_act 무관 무경고(분석/텍스트 작업 오탐 0).
- `test_fs_delta_fallback_zero_on_did_act_none`: did_act=None 워커가 work/ 미변형 → fallback 발화. 파일 생성 시 무발화.
- `test_fs_delta_root_is_work_not_home`: 스냅샷 루트=work/(home 캐시 변경은 무시 — false negative 회피).
- `test_fs_delta_fail_open`: 스냅샷 IO 실패 → 통과(fail-OPEN).
- `test_fs_delta_no_followlinks`: work/ 내 symlink 가 밖을 가리켜도 따라가지 않음(보안).
- G3: 경고 시 PlanOutcome/OutcomeReport 가 "효과 미관측"(중립) 표기 — over-claim 없음.
- 회귀: 기존 테스트 회귀 0(실행 시점 기준선) + grimp 단방향 + secret PASS.

---

## 7. 정직 단서

- **did_act 는 "행동했나"만 안다** — "*올바른* 행동"은 모름(의미 검증 결정 불가, 1f 유지). claude num_turns≥2 면 "도구를 썼다"지 "옳게 썼다" 아님.
- **잔여 false negative**: claude 가 Read-only 도구만 쓰고 되물으면 num_turns≥2(did_act=True)인데 무산출 → 미검출. 순수 되묻기(#3 원형)만 확실히 잡음. touch 빈파일로 fs-delta fallback 위조도 가능(단 권한상승 아님 — 워커 출력 이미 untrusted).
- **#3 은 비결정적**(PoC 발견 2) — 동일 프롬프트가 되묻기/정상수행을 오감. 센서는 "되묻은 그 회차"만 잡지, 되묻기 *경향*을 없애진 못함.
- **근본은 means 레버**(C-6, 별건)가 더 직접 예방 — fs-delta/did_act 는 *사후 결정적 관측·가시화*지 "구조적 불가능"이 아니다. 센서를 "구조적 해법"이라 부르면 over-claim([[feedback_pass_scope_overclaim]]).
- **shell dead path**: `EXECUTING_KINDS={code,shell}` 이나 실 배선 미라우팅(V-5) — 현재 code 만 실질. shell 워커 배선 시 재검토.
- **"해결" 아님** — 흔한 "headless 무행동 silent pass"를 결정적으로 *표시*(경고). 차단·근본 예방은 별건.
