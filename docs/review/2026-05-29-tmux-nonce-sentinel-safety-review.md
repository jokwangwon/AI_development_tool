# TmuxWorker nonce sentinel — 1-agent 경량 안전 재점검

> **검토자**: 안전 reviewer (1-agent 경량, lens = "위조 표면이 실제로 제거/축소되는가? nonce 설계가 견고한가?")
> **일자**: 2026-05-29 (74번째 entry cycle, 세션 #4)
> **대상**: `docs/phase0/tmux-nonce-sentinel-brief.md` (v1) — **brief 단계 재점검**(코드는 아직 구 고정 sentinel)
> **근거**: 직접 read — `worker.py`(현 구현, 구 고정 `_SENTINEL_RE`), `tests/jarvis/test_tmux_worker.py`(9 test, 구 `_done`), `docs/review/2026-05-29-jarvis-cli-tmux-worker-safety-review.md`(B-2 원본) + `.venv` regex/nonce 실측
> **합의 형태**: 1-agent 경량 (풀 3+1 아님, 사용자 명시) — B-2 후속 *구현 brief* 재점검, 핵심 안전 집중
> **vendor**: Anthropic Claude

---

## 판정: **APPROVE WITH CONDITIONS**

brief 의 위조-표면 framing 은 정직하고 nonce 설계는 견고하다. B-2(73 안전 점검) 가 식별한 *사전/외부* 위조 표면(구 고정 `__JARVIS_DONE_0__` · 다른 run nonce)을 per-run 무작위 nonce 로 **실제로 제거**하며, 동일-run 자기-nonce-echo 잔존 한계를 §2 D4 + §4 에서 **정직 명문**(over-claim 차단). regex 정합·exit code·strip 모두 실측 통과. 단 **BLOCKING 2건**(D4 nonce 노출 윈도우 + 음수/strip leak 안전 명문 누락 1건, T-FORGE 위조 저항 입증 정밀화 1건)을 brief v1.1 에 흡수 후 TDD 진입 조건.

---

## 위조 표면 제거 범위 — 독립 판단 (선)

**B-2 의 핵심 위협(거짓 완료 + exit code 위조)은 *사전/외부* 벡터에 한해 실제로 제거된다.** 현 구현(`worker.py:127`)의 `_SENTINEL_RE = __JARVIS_DONE_(-?\d+)__` 은 nonce 가 없어 *어떤* run 의 어떤 출처든 `__JARVIS_DONE_<숫자>__` 만 echo 하면 pane 전역 search(`worker.py:217`)에 매칭 → 거짓 완료. 즉 위조에 **사전 지식 0** 이 필요(고정 상수). brief D2/D4 의 per-run nonce(`__JARVIS_DONE_{nonce}_{code}__`) 는 이 진입 장벽을 **0 → 122-bit 예측 비용**으로 올린다.

실측 확인(`.venv`, uuid4().hex 32-char):
- 구 고정 `__JARVIS_DONE_0__` → per-run regex **불일치**(미완료 판정 유지) ✅
- 다른 nonce `__JARVIS_DONE_deadbeef_0__` → **불일치** ✅
- 정상 `__JARVIS_DONE_{현 nonce}_0__` → 매칭, group=0 ✅
- 음수 `__JARVIS_DONE_{nonce}_-9__` → group=`-9` → int=-9 ✅ (`(-?\d+)` 보존)
- `re.escape(nonce)` = nonce 동일(hex 라 메타문자 0 → regex 인젝션 표면 부재) ✅
- sub strip → nonce 포함 sentinel 제거, cleaned 에 `__JARVIS_DONE_` 잔존 0 ✅

**제거되는 표면**: (a) 비협조 *사전* 명령이 우연/의도로 구 고정 패턴 echo, (b) *다른 run* / 외부 프로세스가 과거·타 run nonce echo, (c) prompt injection 체인이 sentinel 문자열을 *현 run nonce 모르고* 출력. 셋 다 차단.

**제거되지 *않는* 표면**(브리프가 정직 명문, §2 D4 line 58 + §4 line 80): 명령이 **현 run 동안 pane 에 노출된 자기 nonce 를 읽어 echo**. 이는 (i) 자해적이고 (ii) 명령 = 사용자 authority 이므로 위협 모델상 무의미. 단 이 경계가 *정확*하려면 BLOCKING B-1 의 노출 윈도우 명문이 필요(아래).

결론: **"위조 표면 *축소*(사전/외부 차단)"** 주장은 정확하다. **"완전 위조 불가"가 아니다** — brief 가 이를 §4 over-claim 차단 절에 명시(line 80)한 것은 PASS scope over-claim 보수성(MEMORY) 답습이다. ✅

---

## BLOCKING

### B-1 (nonce 노출 윈도우 + 음수/leak 안전 경계 — D4 명문 정밀화)
**brief §2 D4 (line 57~58) + 대응 코드 `worker.py:170~173, 188`**

D4 는 "nonce 가 *현 run 동안* pane 에 노출(send-keys 명령 라인)"이라 1줄 명문하나, **노출의 정확한 메커니즘·시점·불가피성**이 모호하다. 실 코드(현 구현 기준 동형)에서 nonce 는 `full_cmd = ...; echo __JARVIS_DONE_{nonce}_$?__`(brief D2 line 45) 로 구성되어 `send-keys`(`worker.py:188`) 로 **pane 에 타이핑됨과 동시에 capture-pane(`worker.py:215`) 로 다시 읽힌다.** 즉 nonce 는 명령 echo 라인 + 완료 sentinel 라인 **양쪽에 평문 노출**되며, 이는 sentinel 메커니즘상 **불가피**(send-keys 로 명령을 주입하는 이상 nonce 는 항상 pane 텍스트에 존재). 따라서:

1. **예측 불가성의 실제 의미는 "사전(pre-run) 예측 불가"** 이지 "run 중 비밀 유지"가 아니다. nonce 의 안전 가치 = *명령이 작성/디스패치되는 시점에 nonce 가 아직 미정·무작위* 라는 점에 전적으로 의존한다. brief D4 는 이 본질("nonce 는 비밀이 아니라 *사전 예측 불가한 per-run salt* — 명령이 nonce 를 *읽기 전에* 이미 dispatch 됨")을 명문해야, "동일 run echo 잔존"이 *축소된 잔여 위험*임이 정확해진다.

2. **음수 exit code group 의 위조 의미**: `(-?\d+)` 는 음수를 허용하고 실측상 `__JARVIS_DONE_{nonce}_-9__` → int(-9) 로 처리된다(정상). 단 이는 안전상 무해(여전히 현 nonce 필요) — brief 가 group 의미를 D2 에 1줄 명문(음수 exit code 보존, 위조 표면 무관)하면 회귀 검토자가 group 변경을 안전 영향 0 으로 판단 가능.

3. **nonce leak 후처리**: `cleaned = sentinel_re.sub("", pane_text).rstrip()`(brief D2 line 49)는 sentinel 라인의 nonce 를 제거하나, **명령 echo 라인(`send-keys` 가 타이핑한 `... ; echo __JARVIS_DONE_{nonce}_$?__`)은 pane 에 그대로 남아 `cleaned` 에 leak 될 수 있다**(구 `_SENTINEL_RE.sub` 도 sentinel *발화*만 제거, 명령 라인은 미제거 — `worker.py:202` 동형). nonce 자체는 비밀이 아니므로(위 1) **보안 영향 0** 이나, 사용자 출력에 `__JARVIS_DONE_{nonce}_$?` 명령 잔재가 노출되면 위생(hygiene) 저하. brief 는 (a) "nonce 비밀 아님 → leak 안전 영향 0" 명문 또는 (b) 명령 echo 라인도 strip 범위에 포함할지 결정해야 한다.

**조건**: brief v1.1 §2 D4 에 (a) nonce = *사전 예측 불가 per-run salt*(비밀 아님) 정정 명문, (b) `(-?\d+)` group 의 음수 보존 + 위조 무관 1줄, (c) nonce leak(명령 echo 라인 잔재) 의 안전 영향 0 명문 또는 strip 범위 결정.

### B-2 (T-FORGE 위조 저항 입증 정밀화 — 테스트 dead-assert 위험)
**brief §3 T-FORGE (line 66) + 대응 test `tests/jarvis/test_tmux_worker.py` 마이그레이션**

T-FORGE 는 "위조 sentinel(`__JARVIS_DONE_0__` + `__JARVIS_DONE_wrongnonce_0__`) 포함 + 정상 nonce sentinel 부재 → 불일치 → missing → is_error=True" 를 검증한다. 설계는 타당하나 **결정성/입증 정밀도에 2개 함정**:

1. **nonce_factory 주입이 위조 저항을 *우회* 입증할 위험**: T-FORGE 가 `nonce_factory=lambda: _NONCE`(고정) 를 주입하고 pane 에 `__JARVIS_DONE_wrongnonce_0__` 를 넣으면, 위조가 실패하는 이유가 "nonce 예측 불가"가 아니라 단지 "`wrongnonce` ≠ `_NONCE`"여서다 — 이는 **구 고정 패턴 불일치 검증과 동치**이지 *무작위성* 입증이 아니다. T-FORGE 는 위조 *문자열이 현 run nonce 와 다름* → 불일치를 입증할 뿐이며, 이는 **올바른 입증 범위**(per-run regex 가 타 nonce 거부)다. 단 brief 는 "T-FORGE 는 *regex per-run 격리*를 입증 — 무작위성(예측 불가)은 default `uuid4().hex` 선택의 속성이지 test 가 입증하는 게 아님"을 명문해야 거짓 안전감(test 가 무작위성을 보장한다는 오인)을 차단한다(over-claim 차단). 별도 무작위성 검증(예: default factory 가 2회 호출 시 상이 + len/hex 형식)은 권고(R-1).

2. **위조 sentinel 이 정상 sentinel 과 *공존* 하는 케이스 누락**: T-FORGE 는 "정상 nonce sentinel **부재**"만 다룬다. 그러나 실 위협(B-2 원본 `review.md:46` prompt injection)에서는 위조 sentinel 이 pane 에 **먼저 등장**하고 *이후* 정상 sentinel 도 등장할 수 있다(또는 위조만 등장). per-run regex 는 정상 nonce 만 매칭하므로 위조 선행은 무시되어야 하나, **`search` 가 위조 라인을 건너뛰고 정상 nonce 라인을 찾는지** = 위조+정상 공존 케이스가 입증되지 않으면, "위조 선행이 정상 완료를 가리지 않는다"가 미검증으로 남는다(실측상 `search` 는 nonce 일치 라인만 매칭하므로 안전하나 test 부재). brief 는 T-FORGE 에 **위조 + 정상 nonce 공존 → 정상 매칭** 케이스를 추가하거나 별도 test(T-FORGE-COEXIST)로 분리 권고.

**조건**: brief v1.1 §3 에 (a) T-FORGE 입증 범위 = "per-run regex 타-nonce 거부"이지 무작위성 입증 아님 명문, (b) 위조+정상 nonce 공존 → 정상 매칭 케이스 추가(또는 별도 test).

---

## 권고 (non-blocking)

### R-1 default nonce_factory 무작위성 별도 검증
B-2(1) 답습 — T-FORGE/T-NONCE-MATCH 는 고정 nonce 주입(결정성)이라 *무작위성*을 입증하지 않는다. default `uuid4().hex` 의 속성(2회 호출 상이 + 32-char hex 형식 + 주입 미지정 시 default 적용)을 검증하는 **경량 test 1개** 권고. nonce 충돌 확률(2^-122) 은 무시 가능 — 검증 불요(NOTE N-1).

### R-2 _poll_for_sentinel 시그니처 변경 회귀 표면
brief D3: `_poll_for_sentinel(session, sentinel_re)` 로 per-run regex 를 인자 전달(모듈 상수 미사용). 현 9 test 는 `_poll_for_sentinel` 을 직접 호출하지 않고 `run()` 경유 — 시그니처 변경은 내부 메서드라 test 회귀 표면 0(점검 통과). 단 모듈 `_SENTINEL_RE` **제거**(brief D2 line 51) 시 이 상수를 import/참조하는 타 모듈이 없는지 확인 권고(grep `_SENTINEL_RE` → worker.py 내부 한정이면 안전).

### R-3 빈/비정상 nonce_factory 방어
brief 는 default `uuid4().hex` 이나 주입 factory 가 **빈 문자열**(`lambda: ""`) 또는 정규식 메타 포함 문자열을 반환하면 → `__JARVIS_DONE__{code}__`(빈 nonce) 또는 regex 왜곡. `re.escape` 는 메타를 무해화하나(B-1 검증 동형), **빈 nonce 는 구 고정 패턴에 근접**(위조 표면 부분 복원)한다. default 경로는 안전하나, brief 가 "주입 factory 의 무작위성/비공백은 호출자 책임" 1줄 명문 또는 빈 nonce assert 권고(방어적, 영향 낮음).

### R-4 실 tmux smoke 위조 케이스 미포함 — 점검 통과
brief §3 verify 의 실 tmux smoke(`echo SMOKE_OK`)는 *정상* 경로만 검증한다. 위조 저항은 SpyTmuxRunner test(T-FORGE)가 결정적으로 입증하므로 실 smoke 에 위조 케이스 추가는 불요(점검 통과 — 위조 저항은 계산적 검증 우선 원칙 답습).

---

## NOTE

- **N-1 nonce 충돌**: 2^-122(uuid4) — 단일 사용자 자비스 동시 세션 수 고려 시 무시 가능. session 이름 자체도 `uuid4().hex[:8]`(`worker.py:170`)로 이미 분리되어 동일 시점 동일 nonce 두 run 이 같은 pane 을 공유할 경로 부재. 검증 불요.
- **N-2 73 B-2 후속 정합**: 본 brief 는 73 안전 review(`review.md:48`)가 "향후 강화 후보(nonce sentinel = `__JARVIS_DONE_<uuid>_<code>__`)" 로 정확히 예고한 형태와 일치. B-2 NOTE → 구현 brief 의 추적성(traceability) 명확.
- **N-3 scope 보존**: brief §1 "하지 않는 것"(lifecycle/CLI/타 워커/완료 판정 방식 변경 0)은 B-2 완화가 "TmuxWorker 본문 변경 0 원칙"(`review.md:48`) 을 *깨지 않고* sentinel 메커니즘만 강화함을 보장. bounded 정확.
- **N-4 9 test 마이그레이션 의도 보존**: `_done(exit_code, body, nonce=_NONCE)` + 각 `TmuxWorker(nonce_factory=lambda:_NONCE)` 주입으로 lifecycle 순서(`test_run_invokes_tmux_lifecycle_in_order`) · pane-minus-sentinel(`test_run_returns_pane_text_minus_sentinel`, `__JARVIS_DONE_ not in output`) · nonzero(`test_nonzero_sentinel_marks_error`) · missing→error(`test_missing_sentinel_is_failure_not_silent_success`) · kill-on-fail(`test_kill_session_runs_even_when_capture_fails`) · isolation wrap · new-session fail · passthrough 모두 보존 가능. missing-sentinel(nonce 없는 pane → 불일치 → timeout → is_error) 은 nonce 도입 후에도 **동일 의미**(오히려 강화 — nonce 부재 = 위조 sentinel 과 동치 처리). brief §3 마이그레이션 매핑 타당.
- **N-5 over-claim 점검**: brief §4(line 80) "완전한 위조 불가 0", "사전/외부 위조 차단 한정", "동일 run 자기 nonce echo 잔존(정직 명문)" 모두 코드/실측과 정합. PASS scope over-claim 보수성(MEMORY) + detection≠prevention 류 framing 분리 답습됨. ✅

---

## 결론

위조 표면 제거 framing 은 정직하고 nonce 설계는 견고하다. **사전/외부 위조(구 고정 패턴 · 타 run nonce)는 실제로 제거**되며(실측 확인), 동일-run 자기-echo 잔존은 §2 D4 + §4 에 정직 명문(over-claim 차단). regex 정합(`re.escape` 무해 · 음수 group · strip)도 실측 통과. **APPROVE WITH CONDITIONS** — BLOCKING 2건(B-1 nonce 노출 윈도우/leak 안전 경계 명문 정밀화, B-2 T-FORGE 위조 저항 입증 범위 + 위조·정상 공존 케이스)을 brief v1.1 에 흡수 후 TDD 진입. 권고 4건 + NOTE 5건은 정직성·회귀 방어 강화용(non-blocking).

**1-agent 경량 안전 재점검 끝.**
