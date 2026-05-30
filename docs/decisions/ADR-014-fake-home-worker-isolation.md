# ADR-014: 가짜 홈 워커 격리 (claude code 워커 + Landlock 레벨 2)

**상태**: 승인 (3+1 합의 4 source REVISE→AWC — 2026-05-30. BLOCKING 6 흡수 후 구현)
**날짜**: 2026-05-30
**의사결정자**: 사용자 + 3+1 합의 — `docs/review/3plus1-consensus-2026-05-30-jarvis-claude-landlock-fakehome.md`
**상위 권위**: 헌법 제8조 (보안) · CLAUDE.md §2 (Agent=Model+Harness, 계산적 우선 — "잘못하는 것이 불가능하게") · 헌법 제5조-2 (Provider Liquidity) · `ADR-013` (능력 경계 — 인접 축)
**설계 문서**: `docs/phase0/jarvis-claude-landlock-fakehome-design-brief.md` (v1.1)

---

## 1. 맥락 (Context)

`code` worker_kind = 실 claude CLI 를 Landlock 격리에서 실행한다(디딤돌1d 실 배선). 그러나 claude 2.1.x 는 홈(`~/.claude` 세션/캐시/`~/.claude.json`) **쓰기**가 필요한데, 기존 `CLAUDE_RO_PATHS` 가 진짜 홈을 RO 로 막아 claude 가 **조용히 빈 출력으로 실패**했다(100 entry dogfooding 발견). 101 entry 의 fix 조사는 두 경로 모두 보안 risk(① ll_sandbox 다중 RW → `~/.claude.json` atomic rename 이 사실상 진짜 홈 RW 강제 ② `CLAUDE_CONFIG_DIR` → 인증 별도 "Not logged in")로 **DEFER** 했다.

핵심 긴장: claude code 워커는 **신뢰할 수 없는 plan/content 를 실행**(prompt injection)하므로, 격리를 풀어 claude 를 동작시키면 진짜 홈의 SSH 키·push 토큰·클라우드 자격이 주입된 워커의 피해 범위에 들어간다. "혼자 쓰는 개인 머신"이라는 사실은 *multi-user* 위협만 없앨 뿐, "untrusted content 가 능력 있는 워커를 조종"하는 위협(이 시스템의 진짜 위협 모델)은 그대로다([[feedback_boss_role_not_smartest]] 똑똑함≠신뢰).

## 2. 결정 (Decision) — 레벨 2: 가짜 홈 + Landlock + env allowlist

진짜 홈을 *건드리지 말고* claude 에게 **빈 가짜 홈을 통째로** 준다(`HOME` 재배치). 진짜 홈은 RO조차 미노출.

### 2.1 가짜 홈 (HOME 재배치, Q2 영속)
- `~/.jarvis/claude-home`(0700)에 claude 전용 홈을 provision. claude 는 여기에 세션/캐시/credential refresh 를 수행(atomic rename 도 가짜 홈 안 → 진짜 홈 오염 0).
- Landlock RW 루트 = 가짜 홈, 작업폴더를 그 하위(`work/`)에 nest → **단일 RW 루트**로 커버(Q1a, ll_sandbox C 변경 0).

### 2.2 env allowlist (BL-1 — 결정적 deny-by-default)
- 워커 env 는 `{**os.environ}` 전체 상속을 **중단**하고 명시 allowlist(`PATH`·`LANG`·`LC_*`·`TERM`·`TZ`·`SSL_CERT_*`·`NODE_EXTRA_CA_CERTS`)만 통과. `HOME`·`TMPDIR` 는 명시 주입.
- 차단: `ANTHROPIC_*`·`GITHUB_TOKEN`·`SSH_AUTH_SOCK`·`AWS_*`·`GPG_AGENT_INFO` 등 진짜 env 비밀. **fs 격리와 동등한 deny-by-default**(CLAUDE.md §2).
- 인증은 가짜 홈의 `.credentials.json` 경유(env API 키 미사용 — 필요 시 `apiKeyHelper` 후속).

### 2.3 RO 면 최소화 (BL-2 — calibration 실측)
- 광범위 `/proc`·전체 `/run`·전체 `/dev`·진짜 홈 **미노출** — fs 외 우회 채널(`/proc/self/environ` 상속 env, `/proc/<pid>/root` traversal, `/run/user` 세션 소켓[keyring·dbus·ssh-agent]) 차단.
- 노출 = `/usr`·`/lib`·`/lib64`·`/bin`·`/sbin`·`/etc` + **`/run/systemd/resolve`**(DNS, `/etc/resolv.conf` 심볼릭 대상 — `/run/user` 소켓 미포함). calibration: claude 가 이 최소 세트로 동작(`/dev` 불요 — node 는 `getrandom()` syscall).

### 2.4 시드 신뢰경계 + fail-closed (BL-5/6)
- 시드 = 격리 *밖* trusted provisioner(`provision_claude_home`). 가짜 홈 0700 + `.credentials.json` 0600 + **symlink 거부**(공격 방어) + **realpath 검증**(dst 가 가짜 홈 밖으로 새지 않음) + 진짜 홈으로의 단방향(비오염).
- fail-closed: credential 누락/symlink/무효 시 **raise**(비인증 워커 실행 금지). refresh 실패 시 비격리/비인증 fallback 0.

### 2.5 Q3 credential 복사 (사용자 결정 — 자동화 우선)
- 진짜 홈 `.credentials.json`·`.claude.json` 을 가짜 홈에 복사(개입 최소 [[project_minimize_user_intervention]]). `claude login`/`apiKeyHelper` 대안은 후속 카드.

## 3. 결과 (Consequences)

### 차단되는 것 (레벨 2 가치, 정직 표현 — BL-3)
**Landlock allowlist 기준 진짜 홈 *직접 파일 접근*(SSH 키·push 토큰·클라우드 키·다른 프로젝트) 차단**(PoC 음성테스트 5/5 + 우회 [F][G][H] 실증) + env allowlist 로 진짜 env 비밀 차단 + RO 최소화로 `/proc`·`/run/user` 우회 차단. 커널 강제 = 워커 침해 무관.

### 잔여 위험 (레벨 3 영역, 명문 수용 — Q7)
- **net egress 미차단**(Landlock = fs 한정): ① 가짜 홈 안 claude 토큰 ② allowlist 통과 잔여 env ③ (노출된) resolver 소켓 의 net exfil 잔여. → 레벨 3(netns + egress allowlist) 후속.
- **토큰 복제**(Q3 복사): 진짜 홈 토큰을 가짜 홈에 복사 = 동일 토큰 2부 → 무효화 시 둘 다, 진짜 홈 재로그인 회전 시 가짜 홈 사본 stale(재시드 정책).
- **근본 위험**: untrusted plan 실행은 그대로(레벨 2 = blast radius 축소, 제거 아님).

### 잔여(net exfil) resolution — 레벨 3 탐색 결과 (3+1 합의 2026-05-30, REVISE×4 만장일치, Q8 보강)
위 net exfil 잔여를 egress 격리(레벨 3)로 차단하려 설계 탐색(`docs/phase0/jarvis-claude-net-egress-isolation-design-brief.md` + `docs/review/3plus1-consensus-2026-05-30-jarvis-net-egress-isolation.md`)했으나, 4 source 만장일치로 **풀구현 보류** 결정:
- **prevention 패러다임 부적합**: 정당 채널(api.anthropic.com)로의 데이터 exfil 은 어떤 egress 메커니즘으로도 *원리상 불가차단* → root/docker/프록시 최대 비용을 치르고도 핵심 위험 잔존.
- **머신 제약**: netns/iptables = root 필요(자동화 불가), docker = root-동치, Landlock net = 포트만(도메인 allowlist 불가).
- **resolution = 영향 축소 + DESIGN-DEFER**: (a) 레벨 3 풀구현은 실 trigger(토큰 오용 사고 / multi-tenant / 토큰 scope 가 broad 판명)까지 보류. (b) **apiKeyHelper 제한/단명 토큰**(scope·rate·TTL·즉시 revoke)으로 가짜홈 OAuth refresh 토큰(2부 복제) 대체 = exfil 당해도 blast bounded(별도 brief/구현 진입은 사용자 승인 시). prevention 대신 *영향 축소*.
- 미해결 전제: claude OAuth 토큰의 실제 blast radius(scope/과금/데이터접근)는 *미검증* — "bounded" 단정 금지(3+1 BL-1, [[feedback_pass_scope_overclaim]]).

### 비례성
PoC 가 "격리 안 claude 동작"을 실증 → 레벨 1(격리 해제)의 편의 이득 소멸. 레벨 2 는 무권한·결정적(커널 강제)으로 즉시 가능하며 진짜 위협 자산을 차단([[feedback_proportionate_security_personal_tool]]). 컨테이너(레벨 4)·별도 uid 는 새 권한 도입으로 현 단계 미채택(별도 uid = 레벨 3 net 격리 카드로 보존).

## 4. 구현 위치
- `src/jarvis/worker_setup.py`: `_build_claude_env`(2.2) · `provision_claude_home`(2.4) · `_make_claude_runner`(HOME 주입 클로저, 2.1) · `CLAUDE_RO_PATHS`(2.3) · `build_worker_registry`(배선).
- `src/jarvis/isolation.py`: `LandlockIsolation(rw_root=…)`(2.1).
- 검증: 트랙 A 단위(env allowlist·provision·rw_root) + 우회 음성테스트 [F][G][H](실 ll_sandbox) + calibration(실 claude `is_error:false`). 437 passed.

## 5. 답습 교차
ADR-013(능력 경계) · ADR-011 §2.1(수단/목적) · 헌법 8조·5조 · [[reference_claude_landlock_isolation]] · [[feedback_proportionate_security_personal_tool]] · [[feedback_pass_scope_overclaim]] · [[feedback_boss_role_not_smartest]] · [[project_minimize_user_intervention]].
