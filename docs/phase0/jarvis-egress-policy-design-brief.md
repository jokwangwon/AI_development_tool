# Jarvis B1 워커 net egress 정책 설계 brief (DRAFT v1)

> **본 brief = egress 정책 설계 한정.** 어떤 §도 그 자체로 코드 작성·런타임 설치·sandbox 변경·sudo/방화벽 구성을 발생시키지 않는다. 실 변경 0건(머신 수단 실측 = read-only probe). staged: brief v1 → 검토(3+1/직접/DEFER) → (승인 시) PoC/구현. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-22 (세션 4 후속, A1 E2E 완료 후)
**Status**: **v1 — ✅ DEFER 확정 (M1 포함 *전체* 보류, 2026-05-22 사용자 결정). 청사진 보존, 실 trigger 시 발효. §8 참조.**
**진입 단위**: MVP-0 트랙 B(fs 격리) 후속 = 워커 net egress 빈틈(V-F4)
**근거**: [[jarvis-safety-layer-poc-findings]] §6 V-F4 (검증 격리=fs-only) · [[jarvis-orchestrator-mvp-design-brief]] §0 B-3 / §6 / Q-9(net 정책=후속 ABI4) · `feedback_proportionate_security_personal_tool` (비례성) · ADR-011 (means/ends)

## 0. 한 줄 요약

**무권한 환경(이 머신)에서 *호스트 단위* egress allow-list를 강제할 수단이 사실상 없고, 클라우드 워커는 provider API가 본질적으로 필요하다. → egress "차단"은 means이며, 그 한계이득 대비 비용·실효를 비례성으로 판정해야 한다.**

## 1. 위협 모델 (무엇을 막으려는가)

- **T-E1 — 워커 코드/비밀 유출**: 격리된 워커(claude/codex 등 클라우드 CLI)가 작업 중 접근한 코드·시크릿을 **provider API 외 임의 호스트로 전송**. 트리거 = prompt injection 으로 탈취된 워커, 또는 악성/오염 워커 바이너리.
- **T-E2 — 비전 정합**: brief §0 "인터넷 비종속" 비전 — 클라우드 워커 단계에선 *부분적*으로만 성립(이미 B-3 인정). egress 정책은 "최소한 어디로 나가는지 통제/가시화".

### 1.1 본질적 긴장 (means/ends, ADR-011)
- 클라우드 워커는 **정의상** 코드(프롬프트)를 provider 클라우드로 보낸다(api.anthropic.com 등). 이는 brief §0 B-3가 이미 인정한 *수용된* 데이터 흐름 — egress 정책의 차단 대상이 *아니다*.
- 따라서 egress 정책의 실제 목적(ends) = **"승인된 provider endpoint *외* 추가 유출 차단"** (provider allow-list). "완전 net 차단"은 클라우드 워커를 못 돌게 하므로 MVP-0 목적과 충돌(완전 차단은 로컬 워커 = MVP-1+).

## 2. 현 상태

- 트랙 B `LandlockIsolation` = **fs-only 격리**(V-F4). net 무제한 → 워커는 임의 호스트로 egress 가능.
- A1 E2E 에서 claude 워커가 api.anthropic.com 으로 정상 통신(격리가 net 미간섭) — 정상 동작 입증인 동시에 egress 빈틈 노출.

## 3. 머신 수단 실측 (2026-05-22, read-only probe)

| 수단 | 무권한 가능 | 호스트 단위 차단 | 비고 |
|------|:-:|:-:|------|
| network namespace (unshare --net) | ❌ | — | `apparmor_restrict_unprivileged_userns=1` → `uid_map: 허용 안 됨`(bwrap과 동일). user+net ns 무권한 불가 |
| nftables / iptables | ❌ | ✅ | `nft`/`iptables` 존재하나 **root(CAP_NET_ADMIN)** 필요 |
| **Landlock net (ABI4)** | ✅ | ❌ | 커널 6.17 ABI 7 = net 지원, 헤더 매크로 존재. **TCP bind/connect 포트만** 제한 — 443/53 허용 시 모든 https/DNS 통과 = 호스트 무관. 데이터 유출 미차단 |
| seccomp connect() 필터 | △ | △ | connect syscall 인자(sockaddr) 필터 가능하나 IP 추출·IPv6·DNS-우회·getaddrinfo 등 복잡·부분적. BPF 유지비 |
| egress proxy 강제 (HTTP(S)_PROXY) | ✅ | ✅(allow-list proxy) | 워커가 env 무시·직접 connect 시 **우회 가능**(netns 로 직접 egress 막을 수 없으니 강제력 약함) |
| DNS allow-list (resolv.conf) | △ | △ | IP 직접 연결로 우회. 약함 |

**핵심**: 이 머신 무권한에서 *강제력 있는* 호스트 단위 allow-list 수단 = **없음**. netns/nft 는 권한(sudo) 전제. Landlock net 은 포트 차단만(유출엔 무력). proxy/DNS 는 우회 가능.

## 4. 수단 후보 (비교 — 결정 아님, 검토용)

| # | 수단 | 실효(T-E1) | 비용/마찰 | 권한 | 비례성 코멘트 |
|---|------|-----------|-----------|------|--------------|
| M1 | **Landlock net 포트 제한**(443/53만 허용, 그 외 차단) | 낮음(유출은 443으로 가능) | 낮음(ll_sandbox 확장 ~20줄) | 무권한 | 비표준 포트 백도어만 차단. "약한 보강" |
| M2 | **egress 감사/로깅**(연결 대상 기록 → 사후 탐지) | 차단 0, 탐지만 | 중(수단 자체가 어려움 — strace/eBPF 권한) | 부분 권한 | 탐지는 사람 게이트와 중복 가능 |
| M3 | **egress proxy allow-list**(provider만 통과) | 중(우회 가능 시 무력) | 중(proxy 구동+설정) | 무권한이나 강제력 약 | netns 없이는 강제 불가 = 거짓 안전감 위험 |
| M4 | **sudo nftables allow-list**(provider IP만 outbound) | 높음 | 높음(root·IP 관리·CDN IP 변동) | **root 전제** | 개인 툴에 root 방화벽 = 비례 초과 가능(credential DEFER 선례) |
| M5 | **DEFER**(현 fs-only 유지, egress=수용된 한계로 명문화) | — | 0 | — | 신뢰된 provider CLI·개인 툴·강제 수단 부재 → 한계이득<비용 가능 |

## 5. 비례성 판단 틀 (사용자 결정 지원 — 답을 강요하지 않음)

- **위협 현실성**: 워커 = 신뢰된 provider CLI(claude/codex). T-E1 트리거 = prompt injection 탈취. 개인 툴·단일 사용자·로컬 코드 — 유출 표적 가치? (credential DEFER 때 "내 머신 root 공격자=게임 끝"과 평행: 신뢰 CLI가 탈취되면 fs 작업으로도 이미 위험).
- **강제 수단 부재**: 무권한에서 강한 차단(M4 외) 불가 → M1/M3 은 *부분/거짓 안전감* 위험(직전 세션 교훈: "적용 안 되는 위협에 보안 극장 = 실패 양식").
- **means/ends**: egress 차단=means. ends(추가 유출 방지)의 한계이득이 무권한 수단으로 작고, M4(root)는 비례 초과 → **DEFER 또는 최소 M1**이 비례적일 수 있음.
- **실 trigger 시 발효**: 팀/공유/외부 의존/민감 코드베이스 → M4(권한 방화벽) 재평가. credential 트랙과 동일 패턴.

## 6. 권고 (검토 입력 — 확정 아님)

1. **1순위 후보 = M5(DEFER) + M1 경량 보강 옵션**: egress 강한 차단은 무권한 수단 부재 + 비례성으로 DEFER(청사진 보존), 단 **M1(Landlock net 포트 제한)**은 비용 ~20줄로 낮아 "비표준 포트 백도어 차단" 정도의 경량 보강으로 *선택적* 채택 검토.
2. **명문화**: 어느 쪽이든 "워커→provider egress = 수용된 데이터 흐름(B-3), 추가 유출 강제 차단은 무권한 한계로 DEFER"를 brief §0/§6 + findings 에 확정 기재.
3. **금지**: M3(proxy)를 강제력 없이 채택해 "egress 통제됨"으로 표기 = 거짓 안전감(금지). M4(root nftables)를 비례성 검토 없이 발효(금지).

## 7. 결정 지점 (사용자)

- **(A) 3+1 합의** — 보안 변경이므로 다관점 교차검증(수단 실효·비례성·means/ends).
- **(B) 직접 검토** — 사용자가 M1~M5 중 직접 선택(비례성은 사용자 고유 판단 영역).
- **(C) DEFER 확정** — credential 선례대로 청사진 보존, 실 trigger 시 발효. (이 경우 M1 경량 보강 채택 여부만 별도 결정.)

**답습 금지(본 brief 0건)**: 코드/ll_sandbox 변경 / sudo·nftables·proxy 구동 / netns 시도 / egress 수단 실 발효 / 보안 거버넌스(credential/4축/BI-*) 자동 재개.

## 8. 결정 (2026-05-22, 사용자)

- **egress 정책 = 전체 DEFER 확정** (C). 강한 차단(M4 root nftables)은 비례 초과, 무권한 수단(M1/M3)은 실효 부족·거짓 안전감 위험. **M1(Landlock net 포트 제한)도 보류** — 443으로 유출 가능 → 포트 제한 한계이득 ≈ 0 + "egress 통제됨" 거짓 신호(직전 세션 "보안 극장도 실패" 교훈 일관 적용). **수단 채택 0건.**
- **fs-only 격리 정직 유지**: 워커→provider egress = brief §0 B-3가 인정한 *수용된 데이터 흐름*. "추가 유출 강제 차단은 무권한 한계로 DEFER"를 본 brief·findings V-F4 에 확정 기재. 거짓 안전감 추가하지 않음.
- **실 trigger 시 발효**: 팀/공유/외부 의존/민감 코드베이스 → M4(권한 방화벽) 또는 로컬 워커(MVP-1+) 재평가. credential 트랙과 동일 DEFER 패턴.
- means/ends(ADR-011): egress 차단=MEANS, 현 무권한 비용·실효 < 이득 → DEFER. 청사진(§1~§7) 보존.
