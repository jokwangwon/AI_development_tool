# 3+1 합의 보고서 — 디딤돌1g headless 워커 no-op silent pass (발견#3)

**작성**: Reviewer (검토 에이전트) | 2026-05-31
**대상**: `docs/phase0/jarvis-stone1g-headless-noop-design-brief.md` (v1)
**입력 3 source**: Agent A(구현) + Agent B(품질/안전) + Agent C(대안)
**최종 합의 판정**: **REVISE** (brief v1.1 로 BL-1~7 흡수 후 구현 진입 — 핵심 신호설계 재정렬 필요)

---

## 0. 코드 직접 검증 (Reviewer 독립 확인 — 방향 가르는 5개)

| # | 주장 (출처) | 검증 위치 | 결과 |
|---|------|-----------|------|
| V-1 | orchestrator workdir ≠ claude 실제 cwd (A BLOCK-1) | `worker_setup.py:133` `work=os.path.join(home,"work")` + `:135-141` runner 가 `workdir` 인자 **무시**하고 `cwd=work` 사용. orchestrator.py:124 `workdir=self._workdir_factory(task_id)` → 기본 `tempfile.mkdtemp`(:61) = `/tmp/jarvis-…`. | ✅ **사실** — runner 클로저가 workdir 파라미터를 받기만 하고 안 씀. claude 실 cwd = `~/.jarvis/claude-home/work` |
| V-2 | Landlock RW 루트 = 가짜홈(workdir 아님) | `worker_setup.py:185` `LandlockIsolation(rw_root=home)` + `isolation.py:100` `rw=self._rw_root or workdir` | ✅ **사실** — rw_root 지정 시 workdir 무시. 워커는 `/tmp` workdir 에 **쓸 권한조차 없음** |
| V-3 | requires_execution=True ∧ stdout 출력 → fs-delta=0 정상 오탐 (B BL-B1 / FP-5) | boss.py:424 prompt: req_exec=True = "코드/명령을 *실제 실행*", false="생성·작성만". 1f §7(brief line 128): dogfooding run1 `[F,T]`·run2 `[F,T,T]`·run3 `[F,T,T,T]` — "함수 정의=False, **실행/출력=True**" | ✅ **사실** — req_exec 의 의미 = "실행"이지 "fs 변형" 아님. 실측 회문 task("결과 출력")가 req_exec=True 인데 파일 미생성이면 정상인데도 fs-delta=0 |
| V-4 | OllamaWorker(file) 가 fs 를 씀 (A-3 ③: brief "file=텍스트만" 부정확) | worker.py:358-359·375-393 `_write_workdir_file` 가 `output_filename` 설정 시 `workdir` 에 실제 파일 작성 | ✅ **사실** — 현 실 배선은 `output_filename=None`(미작성)이나 설정 시 fs 변형. brief §3 "(i) file 종류는 fs-delta=0 정상" 은 *현 배선 한정* 참 |
| V-5 | shell kind 미배선 dead path (A-3 ⑤) | plan_controller.py:56 `EXECUTING_KINDS={code,shell}` vs worker_setup.py:196 `kind_table={"code":"claude","file":"ollama-file"}` — shell alias 부재 | ✅ **사실** — shell 은 EXECUTING_KINDS 에 있으나 기본 실 배선서 라우팅 불가. Q1 의 "kind∈{code,shell}" 조건에서 shell 은 실질 dead |

**추가 검증**:
- **did_act 가 G2-b 의 단순 이동인가** (C): claude did_act 를 채우려면 `WorkerResult.raw`(worker.py:42, 파싱된 claude JSON)에서 tool-use/num_turns 를 읽어야 함 — 이는 claude JSON shape 의존(provider-specific). **단** 이 로직이 `CliWorker`(worker.py:82 "provider 교체 단위") *안*에 살면, provider-neutral 한 controller 는 `did_act: bool|None` 만 봄 → **G2-b 를 워커 경계 *안*으로 격리한 것**이지 controller 에 provider 분기를 넣는 것이 아님. 헌법5조 정합 측면에서 G2-b(controller 가 claude JSON 직접 파싱)와 **다름**. 단 C 자인대로 claude JSON 의 tool-use 노출 실재성은 **미실측**(추측).
- **WorkerResult 인터페이스 변경 비용**: `@dataclass(frozen=True)`(worker.py:34) — `did_act` 추가 = additive(default None) → 기존 시그니처 미파괴.
- **baseline**: SESSION/CONTEXT 는 **463 passed**(feat/stone1f HEAD `d361a27`)로 기록. 그러나 Reviewer 현 working-tree 실행(`.venv/bin/python -m pytest`) = **462 passed in 183s**(d361a27 머지 이력 포함). 1건 차이 = flaky 110 cancel-race deselect/xfail 추정(CONTEXT "flaky=110 cancel race"). → **A-3 ⑥(brief 463 vs 462)은 *양쪽 다 출처 있음***: brief §6 "463 유지"는 문서 기록 답습(틀림 아님), Reviewer 실측은 462. **결론: 숫자 자체는 비-load-bearing — brief v1.1 은 "회귀 0(현 실측 기준선)"로 표기 권고**(고정 숫자 인용 대신 실행 시점 기준).

→ **종합**: A 의 BLOCK-1/BLOCK-2 는 **코드로 확증**. brief 의 fs-delta 신호 1순위 + Q6 "orchestrator dispatch 스냅샷" 권고는 **현 실 배선에서 100% 무효**(아래 BL-1). B 의 BL-B1(req_exec 게이트 부적합)도 **코드+1f실측으로 확증**.

---

## 1. 3 source 판정 요약

| Source | 판정 | 핵심 권고 |
|--------|------|----------|
| Agent A (구현) | (조건부 가능) | fs-delta 발상 건전하나 **스냅샷 위치를 worker/runner 실 cwd(=work/)로** 이동 필수(BLOCK-1), home/rw_root 금지(BLOCK-2). Q6 dispatch 단일권위 폐기 |
| Agent B (품질/안전) | **REJECT(현 1순위 신호)** | req_exec 게이트(Q1 ⓒ)는 부적합 — 실행≠fs변형, FP-5(stdout 출력)=1f happy-path 오탐. 차단 금지(경고-only), fail-OPEN, over-claim 금지 |
| Agent C (대안) | **REVISE** | 신호를 `did_act` 추상으로(fs-delta=fallback), 적용조건=req_exec 1차게이트(kind 추측 제거), means 레버(워커 argv 봉쇄) 별건 등재 |

3 source 모두 **brief 의 "fs-delta 단독 1순위 신호 + orchestrator dispatch 스냅샷"을 거부**(A=위치오류, B=신호자체 부정확, C=신호를 fallback 으로 강등). → **REVISE 합의**: brief 의 발상(효과 부재 결정적 관측)은 살리되 *신호 설계*와 *측정 위치*를 재정렬.

---

## 2. 교차 비교

### ① 일치 (Consensus 3/3)
| 항목 | 근거 |
|---|---|
| brief 의 "orchestrator dispatch 스냅샷"(Q6) = 무효 | A(BLOCK-1, 실 cwd≠workdir) · B(B-3 ③ symlink/경계는 스냅샷 위치 무관 별개지만 "dispatch 정답"은 V-1 로 반박) · C(C-1, 신호 자체 이동) — **Reviewer 코드 V-1/V-2 로 확정: dispatch workdir 는 claude 가 안 씀** |
| fs-delta 발상(효과 부재 결정적 관측)은 건전 | A(발상 건전) · B(injection 표면 0, G2-a 강점) · C(fallback 으로 보존) — NL 판단 0 + provider-무관(claude/ollama/tmux 동형)은 3/3 인정 |
| G2-b(provider JSON num_turns) 단독 채택 기각 | A(A-2 Q4) · B(B-4 ② 헌법5조-2.2 위반) · C(did_act 추상 뒤로 흡수). brief Q4 권고와 일치 |
| 차단(SUBTASK_FAILED) 즉시 도입 = 시기상조 | A(req_exec 면 차단·아니면 경고로 *제한*) · B(경고-only, 차단 반대) · C(차단 *후보*이나 req_exec∧no-op 한정). **차단 무조건 도입은 0/3** |
| "no-op 결정적 탐지"는 양방향 부정확(over-claim 위험) | B(BL-B5 touch 위조 fn + FP fp) · C(C-4 means 가 구조적 해법, fs-delta=사후탐지) · A(묵시). detection≠prevention |

### ② 부분 일치 (Partial — 2 동의 1 이견)
- **P-1 스냅샷 측정 위치**: A=worker/runner 실 cwd(work/) / C=did_act(워커 자기보고) / B=dispatch(B-3 ④ "워커 자기채점=신뢰경계 위반"). → **갈림**. Reviewer 판단: B-3 ④ 의 "워커 자기채점" 우려는 *fs 스냅샷*(외부 os.walk)과 *did_act*(워커 선언)를 구분해야 함. **fs 스냅샷은 워커 *바깥* 코드가 work/ 를 walk → 자기채점 아님**(워커 출력 untrusted 와 무관, B-3 ① 도 "권한상승 아님" 자인). did_act 는 워커 자기선언 → B 우려 타당. → **fs 스냅샷을 runner 클로저가 실 cwd 대상으로 측정**(A-H1)이 B 의 신뢰경계 우려도 만족(클로저는 harness 소유 worker_setup.py, 워커 프로세스 아님).
- **P-2 적용 조건 ⓒ(requires_execution)**: B=부적합(FP-5) / C=1차 게이트로 *승격* / A=차단강도 가중에만. → **갈림**. Reviewer: V-3 으로 **B 가 옳다** — req_exec=True ∧ stdout-출력 작업은 fs-delta=0 이 정상. req_exec 를 fs-delta 게이트로 쓰면 1f 가 검증한 happy-path(`[F,T]`)를 오탐. **그러나** C 가 req_exec 를 "1차 게이트"로 쓰자는 것은 *fs-delta 의 조건*이 아니라 *did_act 와 곱한 매트릭스*(req_exec=True ∧ did_act=False)이며, 이때 fs-delta 는 did_act=None 일 때만 fallback → B 의 FP-5 가 발생하는 "fs-delta 를 req_exec 로 직접 게이팅"과 다름. → **C-2 대안B(req_exec × did_act 매트릭스)가 B 의 FP-5 를 구조적으로 회피**.
- **P-3 producer 무작업(되물음 텍스트가 artifact)**: A·C(G2-a/did_act 로 커버, `_extract_artifact` 보강 과잉) / B(file-producer 무작업은 미검출 영역 인정). → **동의에 가까움**: producer 텍스트 산출은 fs-delta 무관(정상 fs-delta=0) → fs-delta 로 못 잡음은 3/3 인정. did_act(ollama=content 비어있음 판정)면 잡힐 수 있음(C). `_extract_artifact` 보강은 별건.

### ③ 불일치 (Divergence — 3 다름)
| 쟁점 | A | B | C | Reviewer 판단 + 코드근거 |
|---|---|---|---|---|
| **1순위 신호** | fs-delta(위치만 수정) | fs-delta 부적합 → TOOL_USE>0 이 진짜 신호(단 Read-only면 0) | did_act(워커별 결정적 효과 인지), fs-delta=fallback | **C 채택(조건부)**: did_act 가 #3 을 *원본대로* 잡음(claude TOOL_USE=0 = did_act False). fs-delta 는 work/ 대상이면 안전망. 단 did_act claude 구현(JSON tool-use 파싱) 실재성 **미실측 → brief v1.1 에 PoC 선행 명기**. B 의 "TOOL_USE 가 진짜 신호" = did_act(claude)의 실 구현과 *동일 통찰*(tool-use 부재) |
| **차단 vs 경고** | req_exec 면 차단 | 경고-only(이중신호만 차단) | req_exec∧no-op→SUBTASK_FAILED | **경고-only(MVP)**: 2/3 이 무조건 차단 반대. C 의 차단도 "did_act=False ∧ req_exec" 한정. → MVP=경고(1f CapabilityWarning 동형), 차단은 오탐률 실측 후 별건(B-2 절충 = 이중신호) |
| **measurement 신뢰경계** | runner 클로저(실 cwd) | dispatch(워커 밖) | 워커 did_act(자기선언) | **fs=runner 클로저(work/) + did_act=워커**: fs 스냅샷은 harness 소유 클로저가 walk(워커 자기채점 아님), did_act 는 워커 선언(보조) |

### ④ 누락 (Gap — 단일 source)
- **G-1** ⭐ (A-3 ④ + B-3 ③): 스냅샷 루트가 home/rw_root 면 claude `.claude/` 캐시·세션 쓰기가 **항상 delta≠0** → no-op 을 *못 잡는* **false negative**. + symlink/거대파일 hash DoS/escape 관측(B-3 ③). → **스냅샷 루트 = work/ 전용**(claude 가 산출물을 쓰는 곳, 캐시 노이즈 제외) + `followlinks=False` + realpath 경계 + 엔트리/크기 상한. **반드시 brief 에 명문화**(BL-2).
- **G-2** (A-3 ⑤ / V-5): shell ∈ EXECUTING_KINDS 이나 실 배선 미라우팅 = dead. Q1 의 "kind∈{code,shell}" 조건은 실질 code 만 — **조건 단순화 근거**(C 의 kind 추측 제거 지지).
- **G-3** (B-4 ③): "fs-delta=0 ∧ stdout 0" 이중신호(B-2 절충)가 *stdout 내용 판단*으로 미끄러지면 1f BL-2(NL-blocking 기각) **재위반**. → 길이/존재까지만, 내용 NL 판단 금지. **명문화**(BL-5).
- **G-4** (C-6): 더 구조적 해법 = 워커 argv/env(`--append-system-prompt` 류 means, worker_setup.py:46 harness 소유)로 "되묻지 말고 즉시 실행" 봉쇄. desc 아님 = PLAN-INV 위반 아님, G1(feedforward)과 다른 층위(워커 argv). **단 claude `-p` 가 이를 강제하는지 실재 미확인(추측)**. → §5 non-goal 에 means 레버 **별건 등재**(BL-7).
- **G-5** (B-3 ① / C): touch 빈파일로 fs-delta 위조 가능(false negative) — 단 워커 출력 이미 untrusted, 권한상승 아님 → 보안 등급 낮음, 정직 단서로만.

---

## 3. 핵심 통합 통찰

**brief 의 오류 = 두 겹.**
1. **측정 위치 오류**(A 가 코드로 잡음): orchestrator 가 만든 `/tmp` workdir 는 claude 가 **안 쓴다**(V-1/V-2). 실 cwd = 가짜홈 `work/`. → Q6 의 "dispatch 권위" 폐기, 스냅샷은 runner 클로저(worker_setup.py)가 work/ 대상으로.
2. **신호 의미 오류**(B 가 의미+실측으로 잡음): `requires_execution` 은 "**실행**"이지 "**fs 변형**"이 아니다(V-3, boss.py:424). req_exec=True ∧ stdout-출력 작업(1f 회문 `[F,T]`)은 fs-delta=0 이 정상 → req_exec 를 fs-delta 게이트로 쓰면 **1f happy-path 오탐**.

**해소 = C 의 did_act 추상이 두 오류를 동시에 푼다**: 각 워커가 자기 효과를 *자기 cwd 에서* 결정적으로 앎(ollama=content/파일 작성 여부, claude=tool-use 여부, tmux=exit). controller 는 provider-무관하게 `did_act` 만 본다.
- ollama did_act: 이미 worker.py:353·358-359 로직으로 결정 가능(content 비어있음 / 파일 작성 여부) — 추측 0.
- claude did_act: `raw`(worker.py:42) JSON tool-use 파싱 — provider-specific 이나 **CliWorker 경계 안**(provider 교체 단위) → controller 에 분기 0 = 헌법5조 정합. **단 tool-use 노출 실재성 미실측(PoC 선행)**.
- fs-delta 는 did_act=None(미상 워커)일 때 **fallback 안전망**(work/ 전용, 캐시 제외).

이 구조에서 **B 의 FP-5 가 사라진다**: stdout-출력 claude 작업은 did_act=True(tool-use 로 Bash 실행)이므로 발화 안 함. #3 회문 되묻기는 did_act=False(tool-use 0)로 정확히 발화.

**정직성**: did_act 도 "효과를 냈다"만 알지 "*올바른* 효과"는 모름(§3 결정 불가 유지). 보고 문구 = "효과 미관측"(중립), "아무것도 안 함"(단정) 금지(BL-6).

---

## 4. 권고 신호 설계 (최종)

| 층 | 신호 | 측정 위치 | 성격 |
|---|---|---|---|
| **1순위** | `did_act: bool\|None` (WorkerResult 추상 필드) | **각 워커 내부**(ollama=content/파일, claude=raw JSON tool-use, tmux=None) | 결정적, provider-무관 인터페이스(구현은 워커별) |
| **2순위(fallback)** | work/ fs-delta(경로+st_mtime_ns+size) | **runner 클로저**(worker_setup.py, harness 소유 — 워커 자기채점 아님) | did_act=None 일 때만. work/ 전용(캐시 제외), followlinks=False, 엔트리/크기 상한, fail-OPEN |
| **판정** | `did_act is False AND requires_execution` → CapabilityWarning(경고) | **PlanController**(plan_controller.py, 기존 capability_warnings 재사용) | provider-무관, 차단 아님(MVP) |
| **기각** | G2-b(controller 가 claude JSON 직접 파싱) | — | 헌법5조-2.2 위반. did_act 워커 경계로 대체 |

**우선순위(§2 계산적 우선)**: did_act(결정적, 워커 자명) > fs-delta(fallback) > 경고 표시(G3 정직). 차단·means 레버는 별건.

---

## 5. BLOCKING 목록 (brief v1.1 흡수)

| # | BLOCKING | 출처 | 흡수 방향 |
|---|----------|------|----------|
| **BL-1** | **측정 위치 오류** — orchestrator dispatch workdir(`/tmp`)는 claude 가 안 씀(실 cwd=가짜홈 work/) | A BLOCK-1 (Reviewer V-1/V-2 코드 확정) | Q6 "dispatch 권위" 폐기. 스냅샷/did_act 측정 = **worker/runner**(실 cwd). brief §2 "(전역) workdir 미관측" 표 + §3 G2-a + Q6 전면 재작성 |
| **BL-2** | 스냅샷 루트 = home/rw_root 면 claude 캐시 쓰기로 **항상 delta≠0 → no-op false negative** + symlink/DoS/escape | A-3 ④ · B-3 ③ | 스냅샷 루트 = **work/ 전용**(산출물 디렉터리), 캐시 제외. `followlinks=False` + realpath 경계 + 엔트리/크기 상한 + fail-OPEN |
| **BL-3** | **신호 의미 오류** — req_exec="실행"≠"fs변형". Q1 ⓒ(req_exec→fs-delta 게이트)는 1f happy-path(`[F,T]` stdout 출력) 오탐 | B BL-B1 (Reviewer V-3 코드+1f실측 확정) | fs-delta 를 req_exec 로 직접 게이팅 금지. **신호를 did_act 추상으로**(C), req_exec 는 did_act 와 곱한 매트릭스(req_exec=True ∧ did_act=False)에서만 발화. fs-delta=did_act None fallback |
| **BL-4** | 차단(SUBTASK_FAILED) MVP 도입 = 시기상조 | B BL-B2 (2/3 반대) | **MVP=경고-only**(1f CapabilityWarning 동형, plan_controller.py:97/101 재사용). 차단은 오탐률 실측 후 별건(B-2 이중신호 절충 후보) |
| **BL-5** | fail-OPEN 의무 + "이중신호" 가 stdout 내용 NL 판단으로 미끄러지면 1f BL-2 재위반 | B BL-B4 · B-4 ③ | 스냅샷/did_act 실패 = **통과**(센서=보조신호, ApprovalGate 만 fail-closed). 이중신호는 길이/존재까지만, 내용 NL 판단 금지 |
| **BL-6** | over-claim 금지 — "no-op 결정적 탐지"는 양방향 부정확(touch 위조 fn + producer/stdout fp) | B BL-B5 · C-4 | 보고 문구 = "fs/효과 미관측 — 효과 미확인"(중립). "아무것도 안 함" 단정 금지. detection≠prevention §7 명기 |
| **BL-7** | did_act claude 구현(JSON tool-use 노출) 실재성 미실측 + means 레버(워커 argv 봉쇄) 별건 | C-1·C-6 (Reviewer: 추측 명시) | brief v1.1 에 **claude raw JSON tool-use PoC 선행** 명기(미확인 시 fs-delta fallback 만). means 레버(`--append-system-prompt` 류, PLAN-INV 위반 아님)는 §5 non-goal 별건 등재 |

**부가 정정**: A-3 ⑥(baseline 숫자) = **양쪽 출처 있음** — 문서 기록 463 vs Reviewer 실측 462(flaky 1건 추정). 비-load-bearing → brief v1.1 은 고정 숫자 대신 "회귀 0(실행 시점 기준)" 권고. A-3 ① brief 자기모순(§3 우려 vs Q6 권고)은 BL-1 흡수로 해소.

---

## 6. 사용자 결정 후보 (§6 — A/B/C 가 좁힌 후)

| Q | 질문 | Reviewer 권고 | 후보 |
|---|------|--------------|------|
| **Q1** | 1순위 신호 = did_act(C) vs work/ fs-delta(A) | **did_act 추상 + fs-delta fallback**(BL-3) | (a) did_act 1순위·fs-delta fallback / (b) fs-delta 만(did_act 미구현 시 — but FP-5 잔존) / (c) did_act 만 |
| **Q2** | did_act claude 구현 PoC 선행 여부 | **선행 필수**(BL-7) — tool-use 노출 미실측 | (a) PoC 후 결정 / (b) fs-delta fallback 만으로 MVP, did_act 후속 |
| **Q3** | 발화 조건 | **did_act is False ∧ requires_execution**(BL-3) | (a) did_act∧req_exec / (b) did_act 만 / (c) fs-delta∧kind∈{code} |
| **Q4** | 차단 vs 경고 | **경고-only(MVP)**(BL-4, 1f 동형) | (a) 경고-only / (b) req_exec∧no-op 차단 / (c) 이중신호만 차단 |
| **Q5** | fs-delta fallback 측정 위치/루트 | **runner 클로저 + work/ 전용**(BL-1/BL-2) | (확정 권고 — 변경 시 false negative) |
| **Q6** | means 레버(워커 argv 봉쇄) 등재 | **§5 non-goal 별건 등재**(BL-7) | (a) 별건 등재 / (b) 이번 범위 포함 |
| **Q7** | G2-b(provider JSON) | **기각**(헌법5조, 3/3 + brief Q4) | 확인 |

---

## 7. 정직 단서 (합의 자체의 한계)

- **검증 범위**: 방향 가르는 5곳(worker_setup runner cwd · isolation rw_root · boss req_exec 의미 · 1f §7 실측 패턴 · shell dead path)을 Reviewer 직접 재확인(V-1~V-5). plan_controller/worker.py 전문 통독. 나머지 라인은 source 신뢰.
- ⚠️ **did_act claude 구현 미검증**: claude headless JSON 이 tool-use/num_turns 를 신뢰성 있게 노출하는지 **미실측**(C 자인). 미확인이면 1순위 신호가 fs-delta fallback 으로 강등됨 → 그땐 B 의 FP-5(stdout 출력 오탐)가 부분 재발 → 발화 조건을 did_act 없이 짤 때 work/ fs-delta + req_exec 만으로는 stdout-출력 작업 오탐. **PoC 가 신호 설계를 가른다(Q2)**.
- **means 레버 추측**: claude `-p` 가 "되묻지 말고 즉시 실행"을 강제하는지(C-6) **실재 미확인** — 추측. 별건 PoC 필요.
- **fs-delta 양방향 부정확**: touch 빈파일 위조(false negative, 단 권한상승 아님) + producer/stdout 정상 fs-delta=0(false positive, did_act 로 완화). "결정적 no-op 탐지"로 부르면 over-claim — "효과 미관측의 결정적 *관측·가시화*"가 정확.
- **"해결" 아님**: did_act+fs-delta 전부 채택해도 "워커가 *의미적으로 옳은* 일 했는가"는 결정 불가(§3 유지). #3 의 *근본*("모호하면 되묻는다")은 means 레버(워커 argv)가 더 직접 예방하나 사용자가 G1/means 를 이번 범위 제외 → 센서를 "구조적 해법"으로 부르면 over-claim(C-4).
- **shell dead path**: EXECUTING_KINDS={code,shell} 이나 실 배선 미라우팅(V-5) → Q1 의 shell 조건은 현재 실질 무의미. 향후 shell 워커 배선 시 재검토.
- 합의는 **방향**만 정함. TDD 구현·커버리지·회귀(463 유지)는 별도 단계.
