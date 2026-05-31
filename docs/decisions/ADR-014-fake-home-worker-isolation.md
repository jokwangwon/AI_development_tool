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
- 광범위 `/proc`·전체 `/run`·**전체 `/dev` 디렉터리**·진짜 홈 **미노출** — fs 외 우회 채널(`/proc/self/environ` 상속 env, `/proc/<pid>/root` traversal, `/run/user` 세션 소켓[keyring·dbus·ssh-agent]) + 위험 디바이스(`/dev/sda`·`/dev/mem`) 차단.
- 노출 = `/usr`·`/lib`·`/lib64`·`/bin`·`/sbin`·`/etc` + **`/run/systemd/resolve`**(DNS, `/etc/resolv.conf` 심볼릭 대상 — `/run/user` 소켓 미포함).
- **디딤돌1h 정정**: 초기 calibration("claude node 는 `/dev` 불요 — `getrandom()` syscall")은 **claude *Bash 도구*가 모든 명령에 `2>/dev/null` 쓰기를 붙이는 것**(shell-snapshot source)을 못 봤다 → `requires_execution` 실행이 전부 실패하고 LLM 추론 폴백으로 빠졌다(발견#1, 회귀 아닌 도입 이래 기존 갭). 해소 = 무해 캐릭터 디바이스 `/dev/null` 을 **단일 파일 RW** 로 선별 노출(`CLAUDE_RW_DEVICES`). 전체 `/dev` 디렉터리 노출이 아니므로(`/dev/sda` 등 미노출) BL-2 의 *우회 채널 차단 정신* 보존 — `/dev/null` 은 write→폐기·read→EOF 로 exfil/우회 채널 아님. CL-4 검증(`islink` 거부 + `realpath` `/dev/` prefix + `S_ISCHR`-only, 블록 디바이스 거부)을 `isolation._safe_rw_device` + `ll_sandbox.c` 2중. (이전 주석 "PATH_BENEATH 단일 파일도 EINVAL → 디렉터리만"은 PoC F5 가 반증: 파일용 access mask 로 좁히면 단일 파일 RW 노출 가능.)
- 답습: `docs/phase0/jarvis-stone1h-execution-isolation-gap-design-brief.md`, [[3plus1-consensus-2026-05-31-jarvis-stone1h-execution-isolation]].

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
- **resolution = 영향 축소 + DESIGN-DEFER**: (a) 레벨 3 풀구현은 실 trigger(토큰 오용 사고 / multi-tenant / 토큰 scope 가 broad 판명)까지 보류. (b) **apiKeyHelper 영향 축소**도 별도 3+1 합의(REVISE) + BL-1 실측 후 **DEFER**(아래).

### BL-1 토큰 scope 실측 → apiKeyHelper 도 DEFER (2026-05-30, 3+1 합의 + 실측, Q8 보강)
`docs/phase0/jarvis-claude-apikeyhelper-token-impact-reduction-brief.md` (v1.1) + `docs/review/3plus1-consensus-2026-05-30-jarvis-apikeyhelper-impact-reduction.md`. 위 "미해결 전제(bounded 미검증)"를 **실측 해소**:
- **실측(코드 변경 0, 토큰 값 미노출)**: OAuth 토큰 선언 scope = `user:inference`·`user:profile`·`user:file_upload`·`user:mcp_servers`·`user:sessions:claude_code`. subscriptionType=`max`, rateLimitTier=`default_claude_max_5x`. → **계정/결제 *관리* scope·org admin 부재 → blast 실제 bounded**(rate-limited Max 추론 + 경미 프로필).
- **결론**: apiKeyHelper(전용 API 키)는 exfil 시 *종량 $ 남용(spend cap 까지)* 으로 **영향을 줄이는지 불분명**(OAuth = rate-limited 구독 남용, $ 추가 0 — 오히려 $ 측면 악화 가능) + 구독→종량 **과금 전환**(영구) + 헬퍼/키 평문 가짜홈 RW 상주 = exfil·**변조(임의 코드 실행)** 노출면 추가. → **영향 축소 이득 < 비용 → 구현 DEFER**(증거 기반, 레벨 3 DEFER 와 일관). DESIGN 청사진은 보존, 발효 trigger = sessions scope 데이터 접근 판명 / 종량 과금 수용 / opt-in 이탈.
- 잔여 미확인: `user:sessions:claude_code` 의 대화 데이터 읽기 허용 여부(scope 이름만으론 불확정, 서버 enforcement 미검증).
- 저비용 보완재: Console 사용량 알림 + 수동 revoke **runbook**(detection) — opt-in 단계 최우선. → `docs/guides/claude-worker-credential-detection-runbook.md`(작성 완료).

### 비례성
PoC 가 "격리 안 claude 동작"을 실증 → 레벨 1(격리 해제)의 편의 이득 소멸. 레벨 2 는 무권한·결정적(커널 강제)으로 즉시 가능하며 진짜 위협 자산을 차단([[feedback_proportionate_security_personal_tool]]). 컨테이너(레벨 4)·별도 uid 는 새 권한 도입으로 현 단계 미채택(별도 uid = 레벨 3 net 격리 카드로 보존).

## 4. 구현 위치
- `src/jarvis/worker_setup.py`: `_build_claude_env`(2.2) · `provision_claude_home`(2.4) · `_make_claude_runner`(HOME 주입 클로저, 2.1) · `CLAUDE_RO_PATHS`(2.3) · `build_worker_registry`(배선).
- `src/jarvis/isolation.py`: `LandlockIsolation(rw_root=…)`(2.1).
- 검증: 트랙 A 단위(env allowlist·provision·rw_root) + 우회 음성테스트 [F][G][H](실 ll_sandbox) + calibration(실 claude `is_error:false`). 437 passed.

## 5. 답습 교차
ADR-013(능력 경계) · ADR-011 §2.1(수단/목적) · 헌법 8조·5조 · [[reference_claude_landlock_isolation]] · [[feedback_proportionate_security_personal_tool]] · [[feedback_pass_scope_overclaim]] · [[feedback_boss_role_not_smartest]] · [[project_minimize_user_intervention]].
