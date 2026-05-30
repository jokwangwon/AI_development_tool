# Jarvis claude code 워커 네트워크 egress 격리 (레벨 3) 설계 brief (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(4 source, REVISE×4 만장일치)** → **brief v1.1(본 문서)**. ⭐ **합의 귀결 = 레벨 3 풀구현 DESIGN-DEFER + apiKeyHelper 제한/단명 토큰(영향축소)으로 전환**. 코드 전 문서 먼저(SDD). 자동 다음 단계 진입 0([[feedback_staged_consensus_workflow]]).

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(REVISE×4) 흡수. ⭐ 결론 = 풀구현(레벨 3 prevention) *보류*(DESIGN-DEFER) + apiKeyHelper 제한/단명 토큰(영향축소) 채택. §6 Q1=DEFER+apiKeyHelper, Q8=ADR-014 보강.**
**진입 단위**: ADR-014(레벨 2)가 명문 수용한 잔여 = net exfil(가짜홈 토큰·env). 본 brief 가 그 차단(레벨 3)을 설계 *탐색* 했고, **합의 결과 풀구현은 비례성 미달로 보류**, 대신 영향 축소(apiKeyHelper) 채택.
**상위 문서**: `ADR-014`(레벨 2, 잔여=net) · `docs/review/3plus1-consensus-2026-05-30-jarvis-net-egress-isolation.md` · 레벨 2 brief
**근거**: [[feedback_proportionate_security_personal_tool]](핵심 — DEFER 패턴) · [[feedback_pass_scope_overclaim]] · [[feedback_boss_role_not_smartest]] · [[project_minimize_user_intervention]] · [[feedback_ceremony_inflation]] · [[reference_claude_landlock_isolation]] · 헌법 8조·5조

---

## v1.1 변경 이력 (3+1 합의 흡수, REVISE×4 → DEFER)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 ⭐ | **"bounded" 단정 = 미검증 over-claim 정정** — OAuth 토큰 scope/과금모델/데이터접근/2부복제 실측 전 bounded 단정 금지. Q1 결정의 선행 조건 | B·codex·A·C |
| 🔴 BL-2 ⭐ | **Q1 결론 명문화** — (c)풀구현 *강등*, **(a)DESIGN-DEFER + (b)apiKeyHelper 제한/단명 토큰** 채택. prevention 패러다임이 "정당채널 exfil 불가차단" 위험에 부적합(§4 핵심) | C·codex·A·B |
| 🔴 BL-3 ⭐ | **over-claim 정정** — §0.1 "net exfil 차단" → "비허가 egress 채널 축소". §1 표 자동화 칼럼 정정 | B·C·codex |
| 🔴 BL-4 | **머신 사실 정정** — IPv6 dual-stack(미처리=fail-open) + Tailscale egress 우회로 + api.anthropic.com 안정 IP(160.79.104.0/24 자체 대역, CDN 회전 아님) + docker DNS 스텁 미상속 | A·codex |
| 🔴 BL-5 | **새 TCB 대칭 계상** — docker=root-동치 비용 명시(장점만 금지) + CONNECT 프록시 TCB 조건(직접 DROP 강제·fail-closed·별 신뢰도메인) + DNS exfil 채널 열거 | B·C·codex |
| 🔴 BL-6 | **fail-closed 불변식 + 휘발 회귀** — setup/프록시 실패 시 워커 거부(egress full-open fallback 0). netns/iptables 재부팅 휘발 → root 자동화 회귀 | B |

---

## §0 배경 — 레벨 2 의 잔여, 그리고 net 의 본질적 난이도

### §0.1 무엇을 (못) 막는가 — BL-3 정정
레벨 2(ADR-014)는 진짜 홈·SSH키·push 토큰·진짜 env 비밀을 차단했다. **잔여**: 가짜홈 안 claude OAuth 토큰 + allowlist 통과 잔여 env 가 네트워크로 빠져나갈 수 있다(Landlock = fs-only). 본 brief 는 이를 egress allowlist 로 줄이려 했으나 — **목표 문구는 "egress 차단"이 아니라 "비허가 목적지로의 채널 *축소*"가 정확**(BL-3). 핵심 한계(§3): **정당 채널(api.anthropic.com)로의 데이터 exfil 은 어떤 메커니즘으로도 원리상 불가차단**(claude 가 정당 API 를 쓰므로).

### §0.2 ⚠️ 머신 제약 실측 (BL-4 정정 반영)
- **unprivileged netns/iptables 차단**: `unshare -n`·`iptables -L`·`nft list` 비root 거부, `sudo -n` 비번 → **A/C/D 후보는 매 실행 또는 영속에 root 필요**(일회성 setup 아님, 자동화 불가).
- **docker = rootful + 사용자 docker 그룹** → 무-sudo 동작(유일 자동 경로). 단 **docker 그룹 = root-동치**(BL-5).
- **Landlock net(ABI 7) = 포트 단위만** → 도메인 allowlist 불가(over-claim 금지).
- **api.anthropic.com = 안정 IP**(`160.79.104.0/24` Anthropic 자체 대역 + IPv6 `2607:6bc0::/?`) — v1 의 "CDN 회전 brittle" 전제는 *틀림*. 단 **IPv6 미처리 시 즉시 fail-open**(ip6tables 별도 필수).
- **Tailscale 공존**(`tailscale0` UP) = egress 우회로(exit-node) 가능 — 전역 룰과 충돌/우회.
- **docker resolv = 실 upstream 직접**(127.0.0.53 스텁 *미상속*) → 컨테이너 DNS 모델이 호스트와 다름 + DNS-tunnel 채널.

### §0.3 도메인 allowlist 의 어려움
견고한 egress 제한은 **SNI/host 기반 CONNECT 프록시**가 필요(IP-pinning 은 IPv6·우회 누수). 프록시 = 새 TCB(§3).

---

## §1 후보 메커니즘 (참고 — 합의가 풀구현 보류로 귀결)

| # | 메커니즘 | 격리(토큰채널) | root | 자동화(이 머신) | 도메인 allowlist | 새 TCB |
|---|----------|:---:|:---:|:---:|:---:|:---:|
| A | uid + iptables owner-match + CONNECT 프록시 | 채널 축소 | **매 실행/영속 root** | ❌(sudo 비번) | ✅(프록시) | 프록시·uid·iptables |
| B | docker + egress 방화벽(프록시) | 채널 축소 | 불요 | ✅ | ✅(프록시) | **docker 그룹=root-동치** + 프록시 |
| C | netns + veth + nft | 채널 축소 | **매 exec root** | ❌ | △~✅ | 높음 |
| D | IP-pinned allowlist | 약(IPv6/우회 누수) | 영속 root | ❌ | ❌ | — |
| E | Landlock net(ABI4) 포트만 | ~0(443 통과) | 불요 | ✅ | ❌ | — |
| **F ⭐** | **apiKeyHelper 제한/단명 토큰**(영향축소) | **exfil 당해도 blast↓**(scope·rate·revoke·TTL) | 불요 | ✅ | N/A | 없음 |
| G | egress detection(로그→revoke) | 사후(prevention 0) | 불요 | ✅ | N/A | 없음 |

- **공통 한계**: A~E 전부 prevention(채널 차단)인데 §0.1 정당채널 exfil 잔여 → ROI 무너짐.
- **F = 패러다임 전환**: 차단 대신 *영향 축소*. 무-root·무-프록시·무-DNS(머신 제약 전부 회피) + provider liquidity 정합(env 키 교체).

## §2 ⭐ 핵심 판단 (BL-2) — 풀구현 보류, 영향축소 채택

3+1 합의(4 source 만장일치 REVISE)의 귀결:
- **(c) 풀구현(A~E) 보류(DESIGN-DEFER)**: §0.1 자인(정당채널 exfil 불가차단) → root/docker/프록시 최대 비용을 치르고도 핵심 위험 잔존 = **prevention 패러다임이 이 위험에 부적합**. 레벨 2 가 이미 고위험 자산(SSH/push/cloud/env) 차단 완료 → 남은 bounded(미검증, BL-1) 토큰에 무거운 기계장치는 불비례([[feedback_proportionate_security_personal_tool]] DEFER 패턴).
- **(a) DESIGN-DEFER**: 본 설계(A~E + 후보표)는 *보존*, 발효는 실 trigger(claude 토큰 오용 실 사고 / multi-tenant 전환 / BL-1 토큰 scope 가 broad 로 판명)까지 보류.
- **(b) apiKeyHelper 제한/단명 토큰 = 유일 즉시 작업**(F): 가짜홈에 OAuth refresh 토큰(2부 복제) 대신 scope/rate 제한·단명 API 키 주입 → exfil *당해도* blast bounded + 즉시 revoke(진짜 홈 격리). 별도 brief/구현 진입은 사용자 승인 시.

## §3 안전 논증 / 정직 단서 (BL-3·5 정정)

- **목표 = "비허가 egress 채널 *축소*"**(완전 차단 아님). 정당채널(api.anthropic.com) exfil·**DNS exfil**(쿼리 라벨 인코딩)·**SNI 위조/domain-fronting** 은 잔여 채널 — 레벨 3 도 못 막음. "egress 차단" 표기 금지.
- **docker(B) = root-동치 표면 신설**(BL-5): 격리하려다 더 큰 권한 부여. docker.sock 도달 시 격리 전부 우회 → "권한 없는 격리"가 아니라 "이미 root-상당 사용자가 컨테이너 netns 편의 사용" 모델. A/C 의 일회성 sudo 와 *대칭* 계상(상시 root-동치 vs 1회 마찰).
- **CONNECT 프록시 = 새 TCB**: env `HTTPS_PROXY` 는 untrusted 워커가 무시 가능 → **직접 egress DROP+REDIRECT 결합해야 강제**. 프록시는 워커가 못 건드리는 별 신뢰도메인(별 uid)에, fail-closed(프록시 죽으면 egress 0).
- **fail-closed = 불변식**(BL-6): setup/프록시 미적용 시 워커 실행 거부, egress full-open fallback 0. netns/iptables 재부팅 휘발 → 매 부팅 root 재실행 = 자동화 회귀(P-PRIV).
- **IPv6/Tailscale fail-open**(BL-4): IPv4 룰만이면 IPv6·tailscale exit-node 로 누수.

## §4 비례성 — 핵심 판단

- **prevention 패러다임 부적합**(§2): 제거 못 하는 위험(정당채널 exfil)에 최대 비용 = 불비례. → **영향 축소(F)** 가 합리적 패러다임.
- **자동 root 취득 안 함**(P-PRIV): docker(root-동치 상시)도 비용. apiKeyHelper(F) = 개입 0([[project_minimize_user_intervention]]).
- **신규 ADR 안 만듦**(Q8): 풀구현 DEFER → ADR-014 보강(ceremony 인플레이션 방지 [[feedback_ceremony_inflation]]).

## §5 검증 계획 (풀구현 *발효 시* 만 — 현재 보류)

1. PoC: 선택 메커니즘으로 claude api 도달 ✅ / 임의 host 차단 ✅ / IPv6·DNS·Tailscale 누수 0 / DNS 동작 (레벨 2 calibration 패턴).
2. 음성테스트: 격리 안 비-allowlist egress 차단 실증.
3. 트랙 A: setup/teardown·프록시 fail-closed.
- **apiKeyHelper(F) 발효 시**(별도 brief): 제한 키 scope/rate/TTL 동작 + exfil 시 revoke 격리 + 가짜홈 OAuth 복제 제거.

## §6 열린 질문 — ✅ 사용자 결정 (2026-05-30)

| # | 질문 | ✅ 결정 | 근거 |
|---|------|--------|------|
| **Q1 ⭐** | 지금 구현 vs DEFER vs 경량 | ✅ **(a)DESIGN-DEFER + (b)apiKeyHelper 제한/단명 토큰** | 4/4 합의. (c)풀구현 보류. BL-1 토큰 scope 실측은 apiKeyHelper 설계 시 |
| Q2 | 메커니즘 | (보류 — 발효 시 B docker[root-동치 경고] / A[sudo]) | 미고정 |
| Q3 | 사람 개입 | apiKeyHelper = 개입 0 | [[project_minimize_user_intervention]] |
| Q4 | 도메인 allowlist | (발효 시) CONNECT 프록시, IP-pinning 반대 | TCB 조건 |
| Q5 | DNS | (발효 시) 격리 내 resolver | 스텁 재사용 경계 흐림 |
| Q6 | 별도 uid | A 택할 때만 | |
| Q7 | 정당채널 exfil 수용 | ✅ 명문 수용 + 목표 "비허가 egress 차단" | 4/4 |
| **Q8** | ADR | ✅ **ADR-014 보강**(신규 ADR 안 만듦) | 사용자(C 권고, ceremony 방지) |

---

## 부록 — 답습 교차
ADR-014(레벨 2, 잔여=net — 본 brief resolution 보강 대상) / 헌법 8조·5조 / [[feedback_proportionate_security_personal_tool]](DEFER 패턴) · [[feedback_pass_scope_overclaim]](§3) · [[feedback_boss_role_not_smartest]] · [[project_minimize_user_intervention]] · [[feedback_ceremony_inflation]](Q8) · [[reference_claude_landlock_isolation]] · [[feedback_staged_consensus_workflow]].
