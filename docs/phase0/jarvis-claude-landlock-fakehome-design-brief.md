# Jarvis claude code 워커 격리 해결 — 가짜 홈(HOME 재배치) + Landlock (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(4 source, REVISE)** → **brief v1.1(본 문서, BLOCKING 6 + §6 Q 결정)** → TDD 구현. 코드 전 문서 먼저(SDD). 자동 다음 단계 진입 0([[feedback_staged_consensus_workflow]]).

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(REVISE→AWC) 흡수(BLOCKING 6) + §6 Q1~Q7 결정(2026-05-30: Q2 영속·Q3 복사·Q6 신규 ADR-014). TDD 구현 진입 승인 대기.**
**진입 단위**: 101 entry 에서 **DEFER** 된 claude code 워커 + Landlock 격리 충돌의 해결 — **레벨 2**(가짜 홈 재배치 + Landlock, 진짜 홈 차단). 사용자 비례성 판단으로 레벨 1(완전 신뢰) 대신 레벨 2 채택.
**상위 문서**: 100 entry(충돌 발견) · 101 entry(fix 조사 → DEFER) · `worker_setup.py`(CLAUDE_RO_PATHS 실 배선) · `isolation.py`(LandlockIsolation) · `ADR-013`(능력 경계)
**합의 보고서**: `docs/review/3plus1-consensus-2026-05-30-jarvis-claude-landlock-fakehome.md`
**근거**: [[reference_claude_landlock_isolation]] · [[feedback_proportionate_security_personal_tool]] · [[feedback_pass_scope_overclaim]] · [[project_minimize_user_intervention]] · [[feedback_boss_role_not_smartest]] · 헌법 8조(보안) · 헌법 5조(provider liquidity)

---

## v1.1 변경 이력 (3+1 합의 흡수, BLOCKING 6)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 ⭐ | **env allowlist 화** — `claude_runner` 의 `{**os.environ}` 전체 상속(ANTHROPIC_*/GITHUB_TOKEN/SSH_AUTH_SOCK/AWS_* 누출) → 명시 allowlist. fs 와 동등 deny-by-default. 음성테스트 추가(더미 토큰 차단) | B·codex |
| 🔴 BL-2 ⭐ | **RO 면 최소화 + 우회 음성테스트** — `/proc`(`/proc/self/environ`·`/proc/<pid>/root`)·`/run`(세션 소켓)·`/dev` RO 노출이 fs 외 우회. claude 필요 최소로 축소 + 음성테스트 [F][G][H] | B·codex |
| 🔴 BL-3 ⭐ | **over-claim 정정** — §3 "진짜 홈 전체 손 닿지 않음" → "Landlock allowlist 기준 *직접 파일 접근* 차단(실증)". 잔여 목록 "claude 토큰" → "claude 토큰+상속 env+세션 소켓+net exfil" | B·codex·A |
| 🔴 BL-4 | **HOME 주입 + RW루트 배선 확정** — `LandlockIsolation` 에 `rw_root` 인자(가짜홈), `wrap` 첫 인자=`rw_root or workdir`. HOME 주입=`claude_runner` 단독(가짜홈 클로저 캡처). v1 §2 "isolation.py HOME 전달" 오기 정정 | A |
| 🔴 BL-5 | **시드 신뢰경계 명문화** — 시드=격리 *밖* trusted provisioner. 가짜홈 0700 + credential 0600 + symlink/hardlink 방어 + realpath 검증 + 진짜홈 비오염 단방향 | B·codex |
| 🔴 BL-6 | **provision/refresh fail-closed** — 시드 실패·credential 무효·refresh 실패 시 비격리/비인증 fallback 0(워커 거부 or worker_failed). 재login/재시드만 | A·codex |
| R1~R5 | apiKeyHelper 후보 등재 / dogfooding trust 프롬프트 hang 확인 / 별도 uid=레벨3 카드 보존 / Q5 구조훅 / `--dangerously-skip-permissions`×레벨2 명시 | C·A·B |

---

## §0 배경 — 101 DEFER 의 재검토

### §0.1 막혔던 지점 (100/101 entry)
- claude code 워커를 Landlock 격리에서 실행 시 **빈 출력**(exit 0, worker_failed). 원인 = claude 2.1.x 가 홈(`~/.claude` 세션/캐시/`~/.claude.json`) **쓰기** 필요인데 `CLAUDE_RO_PATHS` 가 진짜 홈을 RO 로 막아 조용히 실패.
- 101 fix 조사: (a) ll_sandbox 다중 RW(최소 권한) → `~/.claude.json` **atomic rename**(inode 변경 실측)이 부모(홈) MAKE/REMOVE 요구 → 사실상 **진짜 홈 RW 확대**(SSH키·다른 프로젝트 오염 risk). (b) `CLAUDE_CONFIG_DIR` → config 는 redirect 되나 **인증 별도**("Not logged in"). → **양쪽 다 보안 risk → DEFER**.

### §0.2 본 세션 재검토 — 가짜 홈(HOME 통째 재배치) PoC (실측 확정)
101 은 "진짜 홈 안의 일부만 열기"를 시도했다 → atomic rename 으로 홈 전체가 열림. **발상 전환: 진짜 홈을 *건드리지 말고* claude 에게 빈 가짜 홈을 통째로 준다**(`CLAUDE_CONFIG_DIR` 이 아니라 `HOME` 자체 재배치).

- **claude 인증 = `~/.claude/.credentials.json` (파일, 528B) — OS 키체인 아님 → 복사 가능**(실측). 설정 = `~/.claude/` 디렉터리 + `~/.claude.json`.
- ✅ **PoC 1단계 (격리 없음)**: `HOME=<가짜홈>` + `.credentials.json`·`.claude.json` 복사 → `claude --output-format json -p` 정상(`"result":"OK"`, `is_error:false`, exit 0). → **101 의 "Not logged in" = 전체 HOME 재배치 + credential 복사로 해소**(CLAUDE_CONFIG_DIR 단독과 차이).
- ✅ **PoC 2단계 (Landlock)**: `ll_sandbox <가짜홈> <system RO...> -- claude ...` + `HOME=<가짜홈>`, **진짜 홈은 allowed 목록에 미포함**, 작업폴더는 가짜 홈 *안*(단일 RW 루트로 커버) → `"result":"SANDBOX_OK"`, `is_error:false`, ABI 7.
- ✅ **PoC 3단계 (음성 테스트, 5/5)**: 격리 안에서 [A] 진짜 `~/.claude/.credentials.json` 읽기 = **허가 거부** / [B] 진짜 `~/.ssh` 목록 = **허가 거부** / [C] 진짜 `~/.claude.json` 읽기 = **허가 거부** / [D] 가짜 홈 안 쓰기 = **허용** / [E] 진짜 홈 *쓰기* = **허가 거부**. → 진짜 홈 *직접 경로* 읽기·쓰기 차단 + 가짜 홈 RW 가 경험적 입증.

### §0.3 ⚠️ 정직 단서 (over-claim 방지, [[feedback_pass_scope_overclaim]]) — BL-3 흡수로 확장
- ✅ **음성 테스트(직접 경로) 해소**: PoC 3단계 5/5. 단 ***직접 경로* 한정** — 아래 우회 채널은 미실증(BL-2 가 음성테스트 [F][G][H] 로 보강).
- 🔴 **BL-1/BL-2 우회 채널 (합의 발견 — v1 누락)**: ① `claude_runner` 의 `{**os.environ}` 전체 상속 = 진짜 env 비밀(ANTHROPIC_*·GITHUB_TOKEN·SSH_AUTH_SOCK·AWS_*)이 워커에 전달 ② `/proc` RO(`/proc/self/environ`·`/proc/<pid>/root` traversal) ③ `/run` RO(D-Bus·keyring 세션 소켓, Landlock 은 소켓 connect 미차단). → fs 격리만으론 "진짜 홈 차단"이 불완전. **v1.1 = env allowlist + RO 면 최소화로 닫음.**
- 🟡 **레벨 2 ≠ 완전 해결 (잔여, BL-3 확장 목록)**: net 미차단(Landlock fs 한정)으로 **① 가짜 홈 안 claude 토큰 ② (allowlist 통과한) 잔여 env ③ 세션 소켓 credential** 의 net exfil 잔여 = 레벨 3 영역. "완전 격리" 표기 금지.
- 🟡 **근본 위험 잔존**: "신뢰 못 할 plan 을 능력 있는 워커가 실행"은 그대로(똑똑함≠신뢰 [[feedback_boss_role_not_smartest]]). 레벨 2 = **blast radius 축소**, 위험 *제거* 아님.
- 🟡 **토큰 복제 (Q3 복사 채택 결과)**: 진짜 홈 토큰을 가짜 홈에 복사 = **동일 토큰 2부** → 무효화 시 둘 다, 진짜 홈 재로그인 회전 시 가짜 홈 사본 stale(BL-6 재시드 정책으로 처리).

---

## §1 핵심 결정 — 레벨 2 (가짜 홈 + Landlock + env allowlist)

```
code(claude) 워커 실행:
  HOME = <가짜 홈 = ~/.jarvis/claude-home>   ← 진짜 홈 미사용 (Q2 영속, 0700)
  env  = allowlist 만 (BL-1)                  ← HOME·PATH·TMPDIR·LANG·SSL_CERT_* + claude 필수
                                                토큰류·SSH_AUTH_SOCK·GPG·cloud env 제거
  Landlock RW = <가짜 홈>(작업폴더 nest, Q1a)  ← claude 세션/캐시/credential refresh 쓰기
  Landlock RO = claude 필요 최소 (BL-2)        ← /usr /lib /bin /etc(git/CA). /proc·/run·/dev 재검토
  그 외 fs = deny-by-default                   ← 진짜 홈 포함 전부 차단 (커널 강제)
```

- **진짜 홈 미노출**: `CLAUDE_RO_PATHS` 의 `os.path.expanduser("~")` **제거**. 진짜 홈은 RO조차 안 줌.
- **env allowlist (BL-1)**: `claude_runner` 가 `{**os.environ}` 상속 중단 → 명시 allowlist. fs 와 동등 deny-by-default(CLAUDE.md §2 "잘못하는 것 불가능하게").
- **RW루트 = 가짜홈 (Q1a·BL-4)**: `LandlockIsolation(rw_root=<가짜홈>)`, `wrap` 첫 인자=`rw_root or workdir`. 작업폴더는 가짜홈 하위(nest). **C 변경 0**.
- **HOME 주입 = runner 단독 (BL-4)**: `build_worker_registry` 가 가짜홈 provision 후 `code_runner` 가 가짜홈 경로를 클로저/partial 로 캡처해 `env` 에 `HOME` 병합. `execvp` 가 env 보존(실측). v1 §2 "isolation.py HOME 전달"은 오기(`wrap`은 명령만 반환).
- **가짜홈 = RW**: claude 가 `.credentials.json` in-place refresh(atomic rename 도 가짜홈 안) → 진짜 홈 오염 0.
- **fail-closed (BL-6)**: sandboxer 부재·시드 실패·credential 무효·refresh 실패 시 비격리/비인증 fallback 0.

## §2 변경 영향 (합의 + Q 결정 반영)

- **worker_setup.py**: ① 가짜홈 provision/시드(Q3 복사: `.credentials.json`+`.claude.json`, BL-5 강조건) ② `claude_runner` env allowlist 화(BL-1) + `HOME=<가짜홈>` 주입 ③ `CLAUDE_RO_PATHS` 진짜 홈 제거 + `/proc`·`/run`·`/dev` 재검토(BL-2).
- **isolation.py `LandlockIsolation`**: `rw_root` 인자 추가(BL-4), `wrap` 첫 인자 분기. (HOME env 는 wrap 비관여 — v1 오기 정정.)
- **ll_sandbox.c**: **변경 0**(Q1a nest → 첫 인자 RW 그대로).
- **신규**: 가짜홈 provisioner(시드+권한+realpath 검증, BL-5) — worker_setup 또는 별도 모듈.
- 회귀 0 목표(현 422 passed). 트랙 A(주입형 runner/isolation/시드 spy)로 실 claude·토큰 없이 결정적. **주의**: 기존 `cmd[1]==workdir` 단정 테스트가 RW루트 인자로 깨질 수 있어 동반 수정(A 지적).

## §3 안전 논증 (정직 — BL-3 정정)

- **plan untrusted 불변 유지**: 레벨 2 는 *격리*만 다룸. plan 은 controller 검증(schema/DAG/table/능력 경계)+사람 승인. claude 능력 경계(ADR-013 Q7: code consume=opt-in) 유지.
- **차단되는 것(레벨 2 가치, BL-3 정직 표현)**: **Landlock allowlist 기준 진짜 홈 *직접 파일 접근*(SSH키·push 토큰·클라우드 키·다른 프로젝트) 차단**(PoC 3단계 실증) + **env allowlist 로 진짜 env 비밀 차단**(BL-1) + **RO 면 최소화로 `/proc`·`/run` 우회 축소**(BL-2). "진짜 홈 전체 손 닿지 않음" 같은 무조건 단정은 금지.
- **잔여 위험(레벨 3 영역, BL-3 확장)**: net egress 미차단 → ① claude 토큰 ② allowlist 통과 잔여 env ③ 세션 소켓의 net exfil. detection≠prevention.
- **`--dangerously-skip-permissions` 상호작용(R5)**: claude 자체 permission 게이트 off → fs 는 Landlock, env 는 allowlist 가 잡으나 net 은 양쪽 다 미차단(레벨 3 의존).
- **비용 거의 0 근거**: PoC 가 "격리 안 claude 동작" 실증 → 레벨 1(격리 해제) 편의 이득 소멸. 레벨 2 비례적([[feedback_proportionate_security_personal_tool]]).

## §4 비례성 — 무엇을 *안* 하는가

- **네트워크 egress 격리 안 함**(레벨 3, 별도 후속): Landlock net(ABI4)은 포트 단위라 claude(443)/공격자(443) 구분 불가 → netns+egress proxy allowlist 필요(무거움). **R3: 별도 uid 워커 = 레벨 3 진입 시 netns/iptables owner-match 에 유리한 카드로 보존**(현 단계 비례성 위배로 미채택).
- **컨테이너 안 함**(레벨 4): 워커당 컨테이너 = 개인 툴 과설계.
- **다중 RW C 변경 안 함**(Q1a nest).
- **provider 전 워커 일반화 *발효* 안 함**(Q5 claude 한정): 단 **R4 — `fake_home`·`seed_fn` 파라미터로 구조 여지**는 둠(헌법 5조 답습, 발효는 후속).

## §5 검증 계획

1. ✅ **음성 테스트 직접 경로 (PoC 3단계 — 완료)**: 5/5.
2. 🔴 **음성 테스트 우회 채널 (BL-1/BL-2, 구현 중 필수)**: [F] `/proc/self/environ` 으로 더미 토큰 env 읽기 차단(allowlist 후) [G] `/proc/<pid>/root/home/...` traversal 차단 [H] `/run/user/$UID/bus`·keyring 접근 차단. (토큰 0, 일반 명령/더미.)
3. 트랙 A 단위 테스트: 가짜홈 provision/시드(권한·realpath spy) + env allowlist(상속 토큰 미전달 검증) + HOME 주입 + RW루트=가짜홈 + 진짜 홈 미노출 + 시드 실패→워커 거부(BL-6). 토큰 0.
4. dogfooding(opt-in, 토큰 소량): `--real-workers` plan→code→claude end-to-end 1회 — 100 entry worker_failed 해소 확인. **R2: claude trust 프롬프트 hang(가짜홈 trust 미설정 → 빈 출력 재현 위험) 확인 포함.**

## §6 열린 질문 — ✅ 사용자 결정 (2026-05-30)

| # | 질문 | ✅ 결정 | 근거 |
|---|------|--------|------|
| Q1 | RW 토폴로지 | ✅ **(a) nest 단일 RW**(RW루트=가짜홈, BL-4) | 4/4 수렴, C 변경 0, PoC 실증 |
| Q2 | 가짜 홈 수명 | ✅ **영속 `~/.jarvis/claude-home`(0700)** | 사용자. 시드 1회·refresh 자연결합(편의). `/tmp` 금지 |
| Q3 | credential 시드 | ✅ **복사**(`.credentials.json`+`.claude.json`) + **BL-5 강조건**(0600·symlink 방어·realpath·stale 재시드) | 사용자(자동화 [[project_minimize_user_intervention]]). 잔여=토큰 복제(§0.3 명시) |
| Q4 | refresh/만료 | ✅ 가짜홈 RW in-place refresh, 실패=**fail-closed**(재시드/재login만) | 4/4 수렴(BL-6) |
| Q5 | 범위 | ✅ **claude 한정** + 구조훅(R4 `fake_home`/`seed_fn`) | 4/4 한정 권고 |
| Q6 | ADR | ✅ **신규 ADR-014**(env allowlist·proc/run 정책·credential 복제·가짜홈 격리 = ADR-013 범위 초과) | 사용자(codex 권고) |
| Q7 | 잔여 위험 수용 | ✅ **수용, 단 목록 확장 후**(BL-3: env/socket/proc/net) | B·codex·C 수렴 |
| (신설) | 시드 방식 후보 | apiKeyHelper(R1)는 후속 카드로 등재(provider liquidity), 본 진입은 Q3 복사 | C |

---

## 부록 — 답습 교차
101 DEFER 재검토 / **ADR-014(신규, Q6)** + ADR-013(능력 경계 인접) / 헌법 8조·5조 / [[reference_claude_landlock_isolation]] · [[feedback_proportionate_security_personal_tool]] · [[feedback_pass_scope_overclaim]] · [[project_minimize_user_intervention]] · [[feedback_staged_consensus_workflow]] · [[feedback_boss_role_not_smartest]](똑똑함≠신뢰, 워커 untrusted).
