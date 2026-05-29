# TmuxWorker nonce sentinel 구현 brief (v1.1)

> **작성**: 2026-05-29 (74번째 entry 진입 cycle — 세션 #4)
>
> **v1 → v1.1 흡수 (1 agent 안전 재점검, `docs/review/2026-05-29-tmux-nonce-sentinel-safety-review.md`, APPROVE WITH CONDITIONS, BLOCKING 2 + 권고 4)**:
> - **B-1**: nonce = *비밀이 아니라 per-run salt*(사전 예측 불가). send-keys 명령 echo 라인 + sentinel 양쪽에 평문 노출 불가피 → 안전 가치 = **"사전 예측 불가"에만** 의존. nonce leak(명령 echo 라인 잔재)은 **안전 영향 0**(이미 노출 전제) + 음수 exit code group(`-?\d+`) 의미 명문. (§2 D4)
> - **B-2**: T-FORGE 는 *per-run regex 의 타-nonce 거부*만 입증(무작위성 아님 — 고정 nonce 도 통과) → **default factory 무작위성 별도 test**(R) + **위조 sentinel + 정상 nonce sentinel 공존 → 정상 매칭**(T-COEXIST) 케이스 추가. (§3)
> - **권고 흡수**: default factory 무작위성 test / verify 에 `_SENTINEL_RE` 제거 회귀 grep / 빈 nonce 방어(run 에서 `if not nonce: raise`). 실 smoke 위조 미포함 = 점검 통과.
>
> **배경**: 73 안전 점검 B-2 — `TmuxWorker` 완료 판정 `_SENTINEL_RE = __JARVIS_DONE_(-?\d+)__`(고정, worker.py:127)를 pane 텍스트 *전역* search(:217). 실행 명령/하위 프로세스가 동일 문자열을 echo 하면 **거짓 완료 + exit code 위조** 가능 → "exit code = 결정적 완료 권위"가 *비적대적 명령* 전제에서만 성립. 73에서 한계 명문 + nonce sentinel 후속 권고. 본 cycle = nonce 적용으로 **위조 표면 제거**.
>
> **scope**: per-session **무작위 nonce** 를 sentinel 에 embed (`__JARVIS_DONE_<nonce>_<code>__`) → 명령이 nonce 를 *예측 불가* → echo 로 위조 불가. `TmuxWorker` 본문 변경(sentinel 생성/매칭/strip) + `nonce_factory` 주입(테스트 결정성) + 기존 9 test 마이그레이션 + 위조 저항 test.
>
> **합의 형태**: (확인 대상) 경량(brief + 직접 TDD) 권고 — 73 안전 점검이 *이미 식별·권고한 B-2* 구현, bounded(TmuxWorker sentinel 한정), test 충실. 단 완료-권위 메커니즘 변경이라 사용자 확인.
>
> **선행 답습**: `src/jarvis/worker.py`(TmuxWorker run/_poll_for_sentinel/_SENTINEL_RE) + `tests/jarvis/test_tmux_worker.py`(9 test, SpyTmuxRunner/_done) + `docs/review/2026-05-29-jarvis-cli-tmux-worker-safety-review.md` B-2.

---

## §1 범위

### 하는 것
1. sentinel = `__JARVIS_DONE_<nonce>_<exit_code>__` (per-session 무작위 nonce) (§2)
2. `nonce_factory: Callable[[], str]` 주입 (default `uuid.uuid4().hex`) — 테스트 결정성 (§2)
3. per-run regex(`__JARVIS_DONE_<nonce>_(-?\d+)__`) — 생성/매칭/strip 일관 (§2)
4. 기존 9 test nonce 마이그레이션 + 위조 저항 test (§3)

### 하지 않는 것
| # | 영역 | 본 cycle |
|---|------|----|
| 1 | TmuxWorker lifecycle(new-session/send-keys/capture/kill) 변경 | 0 (sentinel 메커니즘만) |
| 2 | CLI(__main__) 변경 | 0 (nonce 는 TmuxWorker 내부 — CLI 투명) |
| 3 | OllamaWorker/CliWorker/isolation 변경 | 0 |
| 4 | sentinel 외 완료 판정 방식 변경(예: tmux wait-for) | 0 (nonce sentinel 한정) |
| 5 | 자동 후속 | 0 |

---

## §2 설계 (`worker.py` TmuxWorker)

### D1. nonce_factory 주입
- `TmuxWorker.__init__(..., nonce_factory: Callable[[], str] | None = None)` → `self._nonce_factory = nonce_factory or (lambda: uuid.uuid4().hex)`.
- default = uuid4 hex(예측 불가, per-call 호출). 테스트는 고정 nonce 주입.

### D2. run() — per-run nonce + regex
```
nonce = self._nonce_factory()
sentinel_re = re.compile(rf"__JARVIS_DONE_{re.escape(nonce)}_(-?\d+)__")
...
full_cmd = f"cd {shlex.quote(workdir)} && {inner_shell}; echo __JARVIS_DONE_{nonce}_$?__"
...
pane_text, sentinel_code = self._poll_for_sentinel(session, sentinel_re)
...
cleaned = sentinel_re.sub("", pane_text).rstrip()
```
- 모듈 `_SENTINEL_RE`(고정) **제거** — per-run regex 로 대체.

### D3. _poll_for_sentinel(session, sentinel_re)
- 시그니처에 per-run `sentinel_re` 추가(모듈 상수 미사용). 나머지 polling 로직 동일(capture-pane → search → 등장 시 즉시 반환 / 미발화 → None=timeout).

### D4. 위조 저항 보장
- nonce 는 uuid4 hex(122-bit 무작위) → 명령/하위프로세스가 *현 run 의 nonce 를 예측·echo 불가*. 따라서 명령 출력에 `__JARVIS_DONE_0__`(구 고정) 또는 다른 nonce 가 있어도 per-run regex 불일치 → 무시(완료 판정 0). 정상 완료(echo `$?` 해소) 만 매칭.
- ⭐ **B-1 nonce 본질 (정직)**: nonce 는 **비밀이 아니라 per-run salt**(사전 예측 불가). send-keys 명령 echo 라인 + sentinel 양쪽에 *평문 노출 불가피* → 안전 가치는 **"사전 예측 불가"에만** 의존(기밀성 아님). nonce 가 pane/로그에 잔존해도 **안전 영향 0**(이미 노출 전제 — 보호는 *사전* 위조 차단). exit code group `(-?\d+)` = 음수 코드(신호 종료 등) 보존.
- ⚠️ 한계 잔존(정직): 동일 run 내에서 명령이 *자기 run 의* nonce 를 읽어 echo 하면 위조 가능하나 — (a) 명령=사용자 authority (b) 자기 nonce echo = 자해적·무의미. 외부/하위 명령의 *사전* 위조(다른 run/고정 패턴/nonce 모르는 injection)는 차단. → **"위조 표면 *축소*(사전/외부 차단)" — "완전 차단" 아님**. (완전 OOB 채널 = tmux wait-for 등 별도 영역.)

---

## §3 TDD 계획

`tests/jarvis/test_tmux_worker.py` 마이그레이션 + 신규:
- **마이그레이션 (9 test)**: `_NONCE` const 도입 + `_done(exit_code, body, nonce=_NONCE)` → `__JARVIS_DONE_{nonce}_{exit_code}__` + 각 `TmuxWorker(...)` 에 `nonce_factory=lambda: _NONCE` 추가. 기존 assertion 의도 보존(lifecycle 순서 / pane minus sentinel / nonzero error / missing→error / kill on capture fail / isolation wrap / new-session fail / passthrough). `"__JARVIS_DONE_" not in res.output`(strip) 유지.
- **신규 T-FORGE (위조 저항, B-2)**: worker(nonce_factory=lambda:_NONCE) + pane_text 에 **위조 sentinel**(`__JARVIS_DONE_0__` 구 고정 + `__JARVIS_DONE_wrongnonce_0__` 다른 nonce) 포함 + 정상 nonce sentinel **부재** → per-run regex 불일치 → **missing → is_error=True**(거짓 완료 0). poll_attempts 작게.
- **신규 T-NONCE-MATCH (제어)**: 정상 `__JARVIS_DONE_{_NONCE}_0__` 포함 → 매칭 → applied/exit 0.
- **신규 T-COEXIST (B-2)**: 위조 `__JARVIS_DONE_99__`(구 고정, 위조 exit 99) + 정상 `__JARVIS_DONE_{_NONCE}_0__` **공존** → per-run regex 가 정상 nonce 만 매칭 → exit 0(위조 99 무시). 공존 시에도 정상 완료 권위.
- **신규 R 무작위성 (B-2)**: default factory(주입 0) — `TmuxWorker(...)` 2회 생성/run 시 send-keys payload 의 nonce 가 *상이*(고정 nonce 통과 ≠ 무작위 입증 — 거짓 안전감 차단). SpyTmuxRunner 가 send-keys nonce 캡처 → 2 run nonce 불일치 assert.
- ⚠️ **`_SENTINEL_RE` 제거 회귀 grep**(verify) — 모듈 상수 dangling 참조 0.

### GREEN
- `worker.py`: TmuxWorker nonce_factory + run nonce/regex + _poll 시그니처 + 모듈 _SENTINEL_RE 제거.

### verify
- `.venv/bin/python -m pytest tests/ -q`(회귀 0, tmux 9→마이그레이션 + 신규 2) + 커버리지 + grimp 0 + scan 0.
- ⭐ **실 tmux smoke**: `python -m src.jarvis --worker-type tmux "echo SMOKE_OK" --yes --no-boss --no-memory` → 실 nonce sentinel 생성·매칭 → applied + exit 0 (실 tmux lifecycle nonce 동작 검증).

---

## §4 금지 / over-claim
- 금지: TmuxWorker lifecycle 변경 0 / CLI 변경 0 / 다른 워커 변경 0 / 자동 후속 0.
- over-claim 차단: "완전한 위조 불가" 0 — nonce 는 *사전/외부* 위조(고정 패턴·다른 run) 차단. 동일 run 내 자기 nonce echo(자해적·사용자 authority)는 잔존(§2 D4 정직 명문). "sentinel 위조 표면 *축소*(사전/외부 차단)" 한정.

---

## §5 다음 단계
사용자 승인(합의 형태) → TDD → verify + 실 tmux smoke → commit + push + 74 entry. 자동 진입 0.

**본 brief v1 끝.**
