# 3+1 합의 보고서 — Jarvis claude code 워커 네트워크 egress 격리 (레벨 3)

**일자**: 2026-05-30
**대상 brief**: `docs/phase0/jarvis-claude-net-egress-isolation-design-brief.md` (v1)
**프로토콜**: CLAUDE.md §3 (보안 변경 = 3+1 필수). 4 source = Agent A(구현)·B(품질/안전)·C(대안) 병렬 독립 + codex cross-vendor blind. Reviewer = 메인 컨텍스트.

---

## Phase 2 — 독립 판정 집계

| Source | 판정 | 핵심 |
|--------|------|------|
| **Agent A** | **REVISE** | 실측 정정: netns/iptables = **매 실행 root**(일회성 아님) / api.anthropic.com = **안정 IP**(CDN 회전 아님) + **IPv6 누락 fail-open** / docker resolv 스텁 미상속(DNS 모델 다름). docker만 무-sudo. apiKeyHelper=토큰모델 교체 |
| **Agent B** | **REVISE** | ⭐ **"bounded" 단정 = 미검증 over-claim**(비례성 단일 지렛목). 토큰 scope/과금/데이터·2부복제 미실측. docker=root-동치 비용 §3 누락 |
| **Agent C** | **REVISE** | ⭐ **패러다임 미스매치** — §3 "정당채널 exfil 불가차단" 자인 → prevention 자기모순. **(a)DESIGN-DEFER + (b)apiKeyHelper 제한토큰** 주력 승격, (c)풀구현 강등 |
| **codex** | **REVISE** | "bounded" 근거부족 / §0.1 "net exfil 차단" 과함 / 머신 = docker 그룹 경로뿐(root-동치) / IPv6·DNS·프록시 TCB blocking / Q1 경량완화+DEFER |

**종합 판정: REVISE — 단, "brief 고쳐서 풀구현"이 아니라 ⭐ 풀구현(레벨 3 prevention) 자체를 보류(DESIGN-DEFER)하고 경량 완화(apiKeyHelper 제한/단명 토큰)로 전환** 이 4-source 만장일치 권고.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus — 4/4 또는 강한 다수)
- **C-1 ⭐ 풀구현 비례성 미달 → DESIGN-DEFER + 경량완화**(A·B·C·codex 전원): brief §3 가 "정당 채널(api.anthropic.com) exfil 은 원리상 불가차단"을 자인 → prevention(채널 차단) 패러다임이 잔여(bounded 토큰)에 부적합. root/docker/프록시 최대 비용 치르고도 핵심 위험 잔존 = 자기모순(C BL-C1).
- **C-2 ⭐ "bounded" = 미검증 over-claim**(B BL-B1·codex·C·A R-A3): §2/§4/Q1 의 비례성 논증 단일 지렛목인데 근거 0. OAuth 토큰의 계정권한/과금모델(사용량 과금이면 금전 unbounded)/대화·프로젝트 접근 미실측. **토큰 2부 복제**(ADR-014 §3 Q3 복사)로 "가짜홈 한정"도 깨짐(진짜 홈 토큰 동일 자격). → Q1 결정의 *선행 조건* = 토큰 scope 실측.
- **C-3 ⭐ 머신 제약 정정**(A BL-A1·codex·C): A/C/D = root 필요(netns/iptables 비root 조회조차 거부, sudo 비번 → 자동화 불가). **docker(B)만 무-sudo 자동 가능, 단 docker 그룹 = root-동치**. brief §1 표 "자동화 ✅/후 자동" 칼럼이 이를 흐림.
- **C-4 ⭐ §0.1 "net exfil 차단" over-claim**(B·C·codex): "차단"→**"비허가 egress 채널 축소"**로 목표 문구 하향. §3 정직 단서(정당채널 잔여·Landlock 포트만)는 모범적이나 §0.1/§2 표현이 과함([[feedback_pass_scope_overclaim]]).
- **C-5 CONNECT 프록시 = 새 TCB**(A R-A2·B R-B4·codex Q4): env `HTTPS_PROXY` 는 untrusted 워커가 무시 가능 → **직접 egress DROP+REDIRECT 결합해야 강제**. 프록시 = 단일 신뢰점(SNI/CONNECT 검증·fail-closed·워커가 못 건드리는 별 신뢰도메인 필수).

### ② 추가 발견 (단일 source — 중요)
- **A**: ⭐ **IPv6 dual-stack 전면 누락**(anthropic 이 IPv6 반환 → ip6tables 없으면 즉시 fail-open) / **Tailscale 공존**(`tailscale0` UP, exit-node egress 우회로) / docker resolv = 실 upstream 직접(스텁 미상속 → DNS-tunnel 채널) / 컨테이너 내 Landlock 중복·claude atomic write bind-mount PoC 미검증([[reference_claude_landlock_isolation]] 답습).
- **B**: docker 그룹 root-동치 = "격리 강화"이면서 **더 큰 권한 표면 신설**(docker.sock 도달 시 격리 전부 우회) — §3/§4 대칭 계상 누락 / fail-closed = 테스트 아닌 *설계 불변식* 격상 / netns·iptables 재부팅 휘발 → root 자동화 회귀(P-PRIV) / DNS exfil 채널 미열거.
- **C**: ⭐ **F=apiKeyHelper 제한·단명 토큰**(scope·rate cap·즉시 revoke·TTL)을 주력 결론 승격 + **G=egress detection** closed-loop(revoke trigger) / 풀구현 DEFER 시 신규 ADR 불필요(ceremony).

### ③ 불일치 (Divergence)
- **Q8 ADR**: C = ADR-014 보강(풀구현 DEFER 시 신규 ADR = ceremony 인플레이션 [[feedback_ceremony_inflation]]) / codex = 신규 ADR-015(net = 권한·운영·TCB 다른 별 축). → 사용자 결정(아래).

---

## Phase 4 — 합의 도출 → brief v1.1 흡수 BLOCKING 6 + 권고

### 🔴 BLOCKING (v1.1 흡수 — 단, v1.1 의 귀결은 "풀구현 보류")
- **BL-1 ⭐ "bounded" 미검증 정정**(C-2): §2/§4/Q1 의 "bounded claude 토큰" → "**blast radius 미검증 — OAuth 토큰 scope/과금모델/데이터접근/2부복제 실측 전 bounded 단정 금지**". Q1 결정의 선행 조건.
- **BL-2 ⭐ Q1 결론 명문화**(C-1): (c)풀구현 **강등** + **(a)DESIGN-DEFER 기본 + (b)apiKeyHelper 제한/단명 토큰 = 유일 즉시 작업**. "prevention 패러다임이 정당채널-exfil-불가차단 위험에 부적합"을 §4 핵심 판단으로 격상.
- **BL-3 ⭐ over-claim 정정**(C-4): §0.1 "net exfil 차단" → "비허가 egress 채널 축소". §1 표 "자동화" 칼럼 정정(A/C/D root, B 무-sudo+root-동치).
- **BL-4 머신 사실 정정**(A·codex): IPv6 dual-stack(미처리=fail-open) + Tailscale egress 우회로 + api.anthropic.com 안정 IP(D 재평가) + docker DNS 스텁 미상속(DNS-tunnel 채널).
- **BL-5 새 TCB 대칭 계상**(B·C·codex): docker=root-동치 비용 §3/§4 명시(장점만 표기 금지) + CONNECT 프록시 TCB 조건(직접 DROP 강제·fail-closed·별 신뢰도메인) + DNS exfil 채널 열거.
- **BL-6 fail-closed 불변식 + 휘발 회귀**(B): fail-closed = 설계 원칙(setup/프록시 실패 시 워커 거부, egress full-open fallback 0). netns/iptables 재부팅 휘발 → 매 부팅 root 재실행 = 자동화 회귀 명시.

### 🟡 권고
- R-1 F(apiKeyHelper) + G(egress detection) **closed-loop**(비정상 egress → revoke). 단 G 는 trigger 까지 DEFER 가능(과투자 주의).
- R-2 구현 *고집* 시 메커니즘 = **B(docker, root-동치 경고 명시) 또는 A(일회성 sudo setup 수용 시)**. C(exec-root)·D(brittle)·E(포트만) 부적합.

### 열린 질문 — 합의 권고 + 사용자 결정
| # | 합의 | 비고 |
|---|------|------|
| **Q1 ⭐** | ✅ **(a)DESIGN-DEFER + (b)apiKeyHelper 제한/단명 토큰** | 4/4. 단 BL-1 토큰 scope 실측 선행. (c)풀구현 반대 |
| Q2 | 구현 시 B(docker)>A(sudo). DEFER 이므로 **미고정** | docker=root-동치 경고 |
| Q3 | apiKeyHelper 경로 = 개입 0 | [[project_minimize_user_intervention]] 정합 |
| Q4 | CONNECT 프록시(IP-pinning 반대), TCB 조건 명문 | 구현 시 |
| Q5 | 격리 내 resolver(스텁 재사용 = 경계 흐림) | 구현 시 |
| Q6 | 별도 uid = A 택할 때만 | |
| Q7 | ✅ 정당채널 exfil 명문 수용 + 목표 "비허가 egress 차단"으로 | 4/4 |
| **Q8** | ⚖️ 갈림 → 사용자 | DEFER 시 ADR-014 보강(C, ceremony 방지) vs 신규 ADR-015(codex, 별 축) |

---

## 부록 — source agentId
A=`a76554ba370f1e982` · B=`a5a065a5f38934477` · C=`aeb47c5ed898b254c` · codex=cross-vendor(blind, `--output-last-message`).
