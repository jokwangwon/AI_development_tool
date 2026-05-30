# 3+1 합의 보고서 — Jarvis claude code 워커 격리(가짜 홈 + Landlock, 레벨 2)

**일자**: 2026-05-30
**대상 brief**: `docs/phase0/jarvis-claude-landlock-fakehome-design-brief.md` (v1)
**프로토콜**: CLAUDE.md §3 (보안 변경 = 3+1 필수). 4 source = Agent A(구현)·B(품질/안전)·C(대안) 병렬 독립 + codex cross-vendor blind. Reviewer = 메인 컨텍스트 교차 비교.

---

## Phase 2 — 독립 판정 집계

| Source | 관점 | 판정 | 핵심 |
|--------|------|------|------|
| **Agent A** | 구현 분석가 | APPROVE WITH CONDITIONS | `wrap` 시그니처에 가짜홈 경로 통로 부재(RW루트=가짜홈 방향 정정) + HOME 주입 책임자(runner 단독) 미결 |
| **Agent B** | 품질/안전 | **REVISE** | ⭐ `{**os.environ}` 전체 상속(env 비밀 누출) + `/proc`·`/run` RO 우회 + over-claim |
| **Agent C** | 대안 탐색 | APPROVE WITH CONDITIONS | BLOCKING 0 — 채택안이 머신 제약상 유일 타당. Q3 apiKeyHelper 누락 + login 재고 |
| **codex** | cross-vendor | **REVISE** | env 상속(ANTHROPIC_*/GITHUB_TOKEN/SSH_AUTH_SOCK/AWS_*) + `/proc`·`/run`·`/dev` + 시드 경계 + over-claim |

**종합 판정: REVISE → v1.1(BLOCKING 6) 흡수 시 APPROVE WITH CONDITIONS.**
설계 *방향*(가짜홈 + Landlock)은 4 source 전원 견고·구현가능·타당(C 실측: 대안 mount-ns/bwrap = 이 머신 EPERM, 별도 uid/docker = 비례성 위배, claude native = 추론적 §2 위배 → 채택안이 유일하게 무권한·결정적). 그러나 **안전 논증이 fs 격리만 다루고 env/proc/run 우회 채널을 미언급한 채 "진짜 홈 차단"을 단정** = over-claim + 실효 격리 갭(B·codex 강수렴).

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)
- **C-1 방향 채택**: 가짜홈+Landlock 이 fs 격리로 견고, 이 머신에서 유일 무권한·결정적(A 구현가능·C 실측 대안배제·B fs PoC 견고·codex 방향 합리).
- **C-2 Q1 = (a) nest 단일 RW** (A·C·codex 3/3 명시): 다중 RW C 변경(보안-critical) 회피 + PoC 가 정확히 이 토폴로지 실증. 단 작업폴더가 가짜홈 credential 과 한 RW 트리인 점은 명시 리스크.
- **C-3 over-claim 정정 필수** (B·codex 명시, A 암묵): §3 "진짜 홈 전체 손 닿지 않음" → "Landlock allowlist 기준 *직접 파일 접근* 차단(실증)"으로 하향.
- **C-4 refresh 실패 = fail-closed** (A·codex): 비격리/비인증 fallback 0.

### ② ⭐ 핵심 수렴 (B + codex, A 부분) — env/proc/run 우회면
**가장 무거운 발견.** brief 의 "진짜 홈 차단" 가치가 fs 외 채널로 샌다:
- **env 상속**: `worker_setup.py:39` `env = {**os.environ, "TMPDIR": workdir}` → `ANTHROPIC_*`·`GITHUB_TOKEN`·`SSH_AUTH_SOCK`·`AWS_*`·진짜 `HOME` 등이 워커 프로세스에 그대로 전달(`/proc/self/environ` 이전에 이미 워커 권한). fs 는 deny-by-default 인데 env 는 allow-all = 비대칭 결함.
- **`/proc` RO** (`worker_setup.py:25`): `/proc/self/environ`(상속 env 덤프), `/proc/<pid>/root`·`/cwd` traversal 로 진짜 홈 우회 가능성(추정, PoC 미실증).
- **`/run` RO**: `/run/user/$UID/`의 D-Bus·gnome-keyring·gnupg 세션 소켓 — Landlock 은 소켓 connect 미차단(fs 권한만).
- → 음성테스트 [A~E]는 *직접 경로*만 실증, 이 우회면은 미검증.

### ③ 부분 일치 (Partial — 사용자 결정 대기)
- **Q2 수명**: A·C = 영속(refresh 자연결합·시드 1회) / B·codex = per-run 임시(토큰 상주 회피). **공통: `/tmp` 절대 금지**(world-writable), 영속이면 `~/.jarvis`(진짜홈 하위 0700).
- **Q3 시드**: A = 복사(개입최소) / B = 복사+강조건 or login / **C = login 1회 + apiKeyHelper 등재** / codex = login 선호. → **복사는 토큰 복제(신뢰경계 흐림) 다수 지적, login/apiKeyHelper 우세**.
- **Q6 ADR**: A·C = ADR-013 보강(ceremony 우려) / codex = 신규 ADR(env allowlist·proc 정책·credential 복제 = 범위 초과).

### ④ 누락 (Gap — 단일 source)
- **A**: workdir_factory 워커 미구분(`orchestrator.py:59`), 가짜홈 provision fail-closed 미정의, claude `--dangerously-skip-permissions` 의 trust 프롬프트 hang 가능성(100 entry 증상 재현 위험).
- **C**: Q3 apiKeyHelper(6c) 후보 누락(provider liquidity 최강), 별도 uid = 레벨3 net 격리 카드 보존, Q5 구조 일반화 훅(`fake_home`·`seed_fn` 파라미터).
- **B**: 시드 단계 = 격리 *밖* 신뢰경계, `--dangerously-skip-permissions`×레벨2 이중 무방비.
- **codex**: credential symlink/hardlink 방어 + realpath 검증, `SSL_CERT_*` env 필요.

---

## Phase 4 — 합의 도출 → v1.1 흡수 BLOCKING 6 + 권고 5

### 🔴 BLOCKING (v1.1 흡수 조건 — 설계 무효 아님, 정직성+실효 격리)
- **BL-1 ⭐ env allowlist 화** (B-3/B-4·codex): `claude_runner` 를 `{**os.environ}` 상속 → 명시 allowlist(`HOME=<가짜홈>`, `PATH`, `TMPDIR`, `LANG`, `SSL_CERT_*`, claude 필수만). 토큰류·`SSH_AUTH_SOCK`·`GPG_AGENT_INFO`·cloud env 제거. fs 와 동등 deny-by-default. **음성테스트 추가**: env 에 더미 토큰 주입 → 워커가 못 읽음.
- **BL-2 ⭐ RO 면 최소화 + 우회 음성테스트** (B-1/B-2·codex): `/proc`·`/run`·`/dev` RO 노출을 claude 필요 최소로 실측 축소. **음성테스트 추가** [F] `/proc/self/environ` 비밀 차단 [G] `/proc/<pid>/root` traversal 차단 [H] `/run/user` 소켓 접근 차단.
- **BL-3 ⭐ over-claim 정정** (C-3): §3 line 61 → "직접 파일 접근 차단(실증)". §0.3/§3/§7 잔여 목록 "claude 토큰" → **"claude 토큰 + 상속 env + 세션 소켓 + net exfil"** 확장.
- **BL-4 HOME 주입 + RW루트 배선 확정** (A B-1/B-2): `LandlockIsolation` 에 `rw_root`(가짜홈) 인자 추가, `wrap` 첫 인자 = `rw_root or workdir`. HOME 주입 = `claude_runner` 단독(가짜홈 경로 클로저/partial 캡처). brief §2 "isolation.py HOME 전달" 오기 정정. workdir_factory 무변경.
- **BL-5 시드 신뢰경계 명문화** (B·codex): 시드 = 격리 *밖* trusted provisioner. 가짜홈 `0700` + credential `0600` + symlink/hardlink 방어 + 원본 realpath 검증 + 진짜홈 비오염 단방향.
- **BL-6 provision/refresh fail-closed** (A·codex C-4): 시드 실패·credential 무효·refresh 실패 시 비격리/비인증 fallback 0 — 워커 거부(registry 빌드 raise) 또는 worker_failed. 재login/재시드만.

### 🟡 권고 (R)
- R-1 §6 Q3 후보에 **apiKeyHelper(6c)** 등재 — OAuth 토큰 복제 0 + revoke 용이 + provider liquidity (C).
- R-2 dogfooding(§5.3)에 claude **trust 프롬프트 hang** 확인 1건(가짜홈 trust 미설정 → 빈 출력 재현 위험, A).
- R-3 §4 에 **별도 uid = 레벨3 net 격리 카드 보존** 메모 1줄(C).
- R-4 Q5 **구조 일반화 훅**(`fake_home`·`seed_fn` 파라미터) — 발효 아닌 구조 여지(C, 헌법 5조).
- R-5 §3 에 `--dangerously-skip-permissions`×레벨2 상호작용 명시(B).

### 열린 질문 — 합의 권고 + 사용자 결정
| # | 합의 | 비고 |
|---|------|------|
| Q1 | ✅ **(a) nest 단일 RW** | 4/4 수렴, C 변경 0 |
| Q2 | ⚖️ 갈림 → 사용자 | 영속(A·C, 편의) vs per-run(B·codex, 보안). **/tmp 금지, 영속이면 `~/.jarvis` 0700** |
| Q3 | ⚖️ 갈림 → 사용자 | **복사보다 login 1회/apiKeyHelper 우세**(B·C·codex). 자동화 vs 토큰위생 |
| Q4 | ✅ refresh 실패 = fail-closed | 수렴 |
| Q5 | ✅ **claude 한정** + 구조훅(R-4) | 4/4 한정 권고 |
| Q6 | ⚖️ 갈림 → 사용자 | ADR-013 보강(A·C) vs 신규 ADR(codex — env/proc/credential 정책이 범위 초과) |
| Q7 | ✅ 수용 가능, **목록 확장 후**(BL-3) | env/socket/proc/net 잔여로 넓혀 명문 수용 |

---

## 부록 — source agentId
A=`a063b17b709430a54` · B=`aff82b3b1a8eaf1c9` · C=`ac2fad0fd47ccba0e` · codex=cross-vendor(blind, `--output-last-message`).
