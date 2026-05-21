# 3+1 합의 보고서 — BI-3 Credential 격리 brief 검증 (4축 공통 선결 전제 심화)

> **본 합의 = 추론적 검증(권고) 한정.** 4축 frame(positive allow-list / credential boundary / external enforcement / audit sink integrity)과 BI-3 = 4축 공통 선결 전제 명제는 `f6c6d5a`+`f29c772`+후속 68(`708bc0e`) 만장일치 확정 — 재논쟁 없음. 본 합의는 **BI-3 brief(DRAFT v1)의 정합·완전성 검증 + 구현 발효 전 BLOCKING 통합 + 수단 후보 공간 보강 권고** 만 다룬다. **credential isolation 실 구성 / hardware key 채택 *결정* / 백업 키 정책 *고정* / 실 hook·ruleset·CI·audit sink 구현 / Vault HSM ST-4 진입 / Operational Readiness PASS / Hermes PMO 격상 / commit·push 외 변경 = 모두 0건.** 실 결정/구현 = 사용자 명시 + 별도 단계.

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — **의무** (BI-3 = T3 보안 enforcement 최강 BLOCKING + 핵심 제약 #1 직결, `f29c772` §2.1 답습, R-I-IMPL-BOUNDARY 별도 풀 3+1). Reviewer-only 부적격
**합의 입력**: `docs/phase0/bi-3-credential-isolation-brief.md` (DRAFT v1)
**1차 권위 답습**: `f29c772` Group I 구현 entry 합의 (BI-1~BI-10 + CBI-1~CBI-4 + N-1) + `708bc0e` G3 provenance check 4축 DESIGN + GP-3 §5 (Credential/Secret Hygiene) + γ-1 `9b1f8cd`(ST-1)·γ-2 `2e9d46b`(ST-4 DEFER) + ADR-011 §2.1 means/ends
**판정**: **APPROVE WITH CONDITIONS** — BI-3 brief 는 출처 정합·citation 정확(N-2 정밀화 = 3 Agent 독립 grep 검증)·means/ends 경계 양호로 *구현 entry 입력 정비 적격*. **단 brief v2 에서 BLOCKING 8건(BI3-1~BI3-8) + 조건부 4건 해소 후 credential 수단 결정 합의 진입 권고** (C §13 옵션 B→A 순서). **모든 BLOCKING = brief 단계 심화/명시로 해결 가능 — 수단 결정·실 구성 요구 0건.**

---

## 0. 종합 판정 (한 문단)

세 Agent 는 **(1) BI-3 brief 가 출처(`f29c772`/G3 §3.1.2·§5.5/GP-3 §5)와 정합하며 본문 변경을 유발하지 않고, (2) §7.2 N-2 citation 정밀화("GP-3 §6.2" → 실제 GP-3 = §5, §6.2 는 GP-4 의 P5)가 *사실 정확*(3 Agent 가 각각 독립 grep 으로 `governance-preconditions.md` line 468/526/534 검증), (3) M2(hardware-backed key)의 "구조적 흡수"는 *키 추출* 차원에서만 기술적으로 성립하고 *서명 오용·touch-to-sign·T-2/T-4* 는 흡수하지 못하며, (4) means/ends 분리 *선언* 자체는 모범적** 이라는 데 일치한다. 가장 무게 있는 교차 발견은 **세 Agent 가 서로 다른 입구로 같은 결론에 수렴한 "M2 흡수 서사의 과신 위험"** 이다 — B 는 "§5.1 '물리 구조가 격리를 보장'이 *서명 오용 전체 방어*로 오독될 거짓 안전감"(B-IMPL-4), C 는 "흡수 서사가 '권고' 라벨에도 entry 후보 공간을 서사적으로 좁히는 means 편향"(DV-C1), A 는 "흡수의 *능동* 메커니즘인 touch-to-sign/PIN/touch policy 가 정작 §5 에 누락"(A-REC-1)으로 동일 약점을 지적했다. 또한 세 Agent 가 각자 단독으로 *객관적·검증 가능* 한 누락을 잡았다 — A: **"T-1~T-5" 라벨이 roadmap 의 GP-5 "T-1~T-6"(Provider Adapter tools)와 충돌**(A-IMPL-3) + **docker socket mount = host escape 우회 표면 누락**(A-IMPL-2), B: **공급망 P11 ↔ credential 격리 인터페이스 누락**(B-IMPL-1) + **부분 격리 그라데이션(중간 상태 = 가장 위험한 거짓 안전감 구간)**(B-IMPL-5), C: **N-1/CBI-4(sigstore/gitsign·Rekor) 본문 누락 비대칭**(§7 에서 N-2 는 정밀화하면서 N-1 후보는 표에서 누락, C-N-1) + **TPM/Secure Enclave 후보 누락**(M2 의 lock-out SPOF 를 비용 0 으로 우회, C-N-2). Reviewer 가 종합한 결과 본 brief 는 *기반은 견고하나 정식화가 binary·host 침해 중심·후보 1축으로 협소* 하여, 중간 격리 상태·host 미침해·공급망 층·대안 후보 공간을 못 덮는다 — 이는 brief v2 에서 명시/심화로 교정 가능하며 *수단 결정·실 구성을 요구하지 않는다*. 본 합의 = **추론적 검증(권고) 한정 — 수단 결정·실 구현·commit·push 는 사용자 명시 + 별도 단계.**

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3 Agent 모두)

| # | 합의 항목 | A | B | C |
|---|----------|---|---|---|
| C1 | **N-2 citation 정밀화("GP-3 §6.2" → GP-3 §5) = 사실 정확** (3 Agent 각자 독립 grep: governance line 468 GP-3=§5 / line 526 GP-4=§6 / line 534 §6.2=P5) | ✅ | ✅ | ✅ |
| C2 | brief = 출처 정합 + 본문 변경 유발 0 + APPROVE WITH CONDITIONS 방향 | ✅ (적격) | ✅ (AWC) | ✅ (AWC) |
| C3 | M2 흡수 = *키 추출* 차원만 방어, *서명 오용*(touch-to-sign·악성 prompt)은 별개 위협 (brief §5.3 인정은 정확하나 위치/강도 부족) | ✅ (A-REC-1) | ✅ (B-IMPL-2/4) | ✅ (§3) |
| C4 | means/ends 분리 *선언* 자체는 양호 ("사람 키 Hermes 미보유"=ends / M1~M4=means) | ✅ | ✅ | ✅ (DV-C3) |
| C5 | ST-1(upstream 변경=풀 3+1 trigger)/ST-3(single-host canonical)/ST-4(MVP-6 DEFER) 경계 + chmod 능동강제 비권고(γ-1) 정확 | ✅ | ✅ | ✅ |
| C6 | 어느 수단도 "0-구현"이 아님 — 전부 실 코드/구성 필요 (단 brief §4 표가 이를 명시 안 함) | ✅ (A-IMPL-1) | (정합) | ✅ (§2) |

### 1.2 부분 일치 (Partial — 2 동의, 1 강조/추가)

| # | 항목 | 분류 |
|---|------|------|
| P1 | **M2 흡수 서사 과신 = 거짓 안전감/means 편향 위험** | B 강하게(B-IMPL-4 별도 차단) / C 강하게(DV-C1 means 편향·후보 공간 협소) / A 보강(A-REC-1 touch policy 누락 = 흡수의 능동 메커니즘) — **3 수렴, BLOCKING 격상** |
| P2 | **격리 대상 enumeration 이 추상→구체 환원 미흡** | A(A-IMPL-2 구체 우회 표면: /proc·ptrace·docker socket·bind mount·credential helper) / C(C-N-3 강제 메커니즘 축 누락: rootless/userns/seccomp) 수렴 / B(TH-5 T-5 ephemeral runner 시점) 부분 |
| P3 | **백업 키 = 양날 트레이드오프** | B(B-REC-1: 백업 키 = 새 T-1 인스턴스·revocation SOP) / C(C-N-5: 공격 표면 N배·보관처 §6 동일 침해 경계 회귀 역설) 수렴 / A(A-REC-2: lock-out 복구 SOP·가용성 측면) |

### 1.3 불일치 (Divergence — 관점차 스펙트럼)

| # | 항목 | A | B | C | Reviewer |
|---|------|---|---|---|----------|
| D1 | brief 의 *핵심* 약점 위치 | 구체 우회 표면(*깊이*) + 라벨 충돌 | 붕괴 경로 정식화(*깊이* — binary·host 중심) | 수단 후보 공간(*너비* — N-1/TPM 누락) | **진정 충돌 아닌 *축* 차이 — A/B = 주어진 후보의 격리 *완전성·정식화 깊이*, C = 후보 *공간 너비*. 상보(brief 가 "깊이도 너비도" 협소). 둘 다 v2 에서 교정 — 깊이(BI3-2/5/8) + 너비(BI3-7 + CBI3-1)** |

### 1.4 누락 (Gap — 단독 발견, Reviewer 중요도)

| # | 항목 | 언급 | 중요도 | 처리 |
|---|------|-----|-------|------|
| N-A1 | **"T-1~T-5" 라벨이 GP-5 "T-1~T-6"(Provider Adapter tools, roadmap line 653/671/689)와 충돌** → cross-ref 혼동 | A | **높음** (객관적·검증됨) | **BI3-1** (CT-n 재명명) |
| N-A2 | **docker socket(`/var/run/docker.sock`) mount = host escape** — cap_drop 무관, 가장 치명 우회 표면 | A | **높음** | BI3-2 (구체 표면 enumeration) |
| N-B1 | **공급망 P11 ↔ credential 격리 인터페이스** — env scrub/entrypoint stat/docker secret 정의가 supply-chain 변조 시 T-1~T-5 동시 재유입 | B | **높음** | **BI3-4** |
| N-B2 | **부분 격리 그라데이션** — 격리는 binary 아님, 중간 상태(T-1✅ T-4❌) = 가장 위험한 거짓 안전감 구간 | B | **높음** | **BI3-6** |
| N-B3 | **audit 완전성 FN**(기록 누락 observe FN) ≠ T-4 위조/삭제 격리 — BI-7/BI-5 소속 명시 (silent gap) | B | 중 | BI3-8 |
| N-C1 | **N-1/CBI-4(sigstore/gitsign·Rekor) 본문 누락** — §7 N-2 정밀화 비대칭 + Rekor↔BI-5 audit 시너지 누락 | C | **높음** | **BI3-7** |
| N-C2 | **TPM/Secure Enclave** 후보 누락 — M2 와 동일 물리 격리를 *비용 0·분실 SPOF 없이* | C | 중-높음 | CBI3-1 |
| N-C3 | **GitHub plan/ruleset 가용성(BI-4) = T-2 token 격리 선결** cross-ref 누락 | C | 중 | CBI3-3 |
| N-C4 | **credential observe = binary 성격** (allow-list 의 statistical observe 와 상이 — "키 접근 시도 telemetry 0건 N일" 형태) | C | 중 | 권고 (REC) |
| N-B4 | 4축 line 번호 표기(brief 가 360/784/805 인용, 실제 805 = §5.5.2 일반 SPOF 사유) | B | 낮음 | 권고 (REC) |

---

## 2. 합의 도출

### 2.1 판정 + 합의 형태

| 영역 | 판정 | 근거 |
|----|----|----|
| **BI-3 brief DRAFT v1** | **APPROVE WITH CONDITIONS** | 출처 정합·N-2 정밀화 정확·means/ends 양호 → 구현 entry 입력 정비 *적격* / 단 BLOCKING 8 + 조건부 4 = v2 해소 권고 |
| **다음 단계 순서** | **§13 옵션 B → A** (v2 → credential 수단 결정 합의) | C 권고 + Reviewer: 후보 공간(BI3-7/CBI3-1)·라벨(BI3-1)·정식화(BI3-2/5)를 v2 에서 정비 후 entry 합의가 *완전한 후보 공간* 위에서 결정 |

- **credential 수단 결정 = 풀 3+1 *의무*, Reviewer-only 부적격** (만장일치 — BI-3 = 최강 BLOCKING + 핵심 제약 #1 직결). 2차 vendor = trigger #7 기 충족(GPT-5.5 1건), 추가 = 사용자 결정.
- **모든 BLOCKING = brief 단계 심화/명시로 해결** — 수단 결정·hardware key 채택·실 구성 요구 0건 (§3 경계 보존).

### 2.2 구현 발효 전 BLOCKING 통합 (A 3 + B 5 + C 누락 → 중복 제거 8건)

**우선순위: BI3-5(M2 거짓 안전감, 3 수렴) > BI3-2(구체 표면·docker socket) > BI3-7(N-1 비대칭) > BI3-1(라벨 충돌) > BI3-4(공급망) > BI3-6(그라데이션) > BI3-3(0-구현 명시) > BI3-8(audit FN 귀속).**

| # | BLOCKING | 출처 | 우선 |
|---|----------|------|------|
| **BI3-1** | **"T-1~T-5" 라벨을 `CT-1~CT-5`(credential target) 등으로 재명명** — roadmap GP-5 "T-1~T-6"(Provider Adapter tools) 점유와 충돌, cross-ref/Evidence/ledger 혼동 차단 (brief §0.3 silent scope expansion 정신 직결) | A-IMPL-3 | 4 |
| **BI3-2** | **격리 대상 *구체 우회 표면* enumeration** — (i) `/proc/<pid>/mem`·ptrace(`CAP_SYS_PTRACE` 미차단 시) (ii) child process env 상속 (iii) `~/.gnupg`·`~/.ssh`·`SSH_AUTH_SOCK` bind mount 경로 (iv) git credential helper·`GIT_ASKPASS` (v) **`/var/run/docker.sock` mount = host escape(최치명)**. CT-1~CT-5 의 *구체 차단 표면* 없이는 "어디까지 미주입"이 미정의 = 거짓 격리 | A-IMPL-2 + C-N-3 | 2 |
| **BI3-3** | **§4 수단 표에 "0-구현 아님(필요 실 구성)" 컬럼 + "보안 결과(ends) 동등성" 컬럼 추가** — `f29c772` §C1 "구현 가능하나 0-구현 아님" 전파 + ADR-011 §2.1(a) 비교표 형식 충족(M1↔M2 동일 ends 보장 범위) | A-IMPL-1 + C-N-7 | 4 |
| **BI3-4** | **공급망 P11 ↔ credential 격리 인터페이스 명문** — env scrub/entrypoint stat/docker secret 정의가 supply-chain 변조 시 CT-1~CT-5 동시 재유입 = 4축 동시 명목화. governance §1.2.7 P11 cross-ref 흡수 | B-IMPL-1 | 4 |
| **BI3-5** ⭐ | **M2 흡수 한계 = §6 동일 강도 거짓 안전감 차단** — "hardware key 흡수 = CT-1/CT-3 *키 추출* 한정, CT-2/CT-4·서명 오용·touch-to-sign(host 미침해서도 성립)은 별개"를 §5.3→독립 명제로 격상. **+ touch-to-sign/PIN/touch policy(`always`) = 흡수의 *능동* 메커니즘 명시**(현재 누락). 흡수 서사의 means 편향 재균형 | B-IMPL-2/4 + C/DV-C1 + A-REC-1 | **1** |
| **BI3-6** | **부분 격리 그라데이션 명문** — 격리는 binary 아님, CT-1~CT-5 부분집합 상태(중간 상태)가 *가장 위험한 거짓 안전감 구간*. 격리 순서(credential→allow-list→anchor→audit)가 *중간 상태 안전*을 보장 안 함을 §8/§11 Rollback Trigger 에 명시 | B-IMPL-5 | 2 |
| **BI3-7** | **N-1/CBI-4(sigstore/gitsign keyless·Rekor) 본문 보존** — §4 에 "M5 (CBI-4, MVP-6 DEFER, audit 시너지)" 행 + §9 Rekor↔BI-5 audit sink 인프라 시너지 cross-ref (§7 N-2 정밀화 ↔ N-1 누락 비대칭 해소) | C-N-1 | 2 |
| **BI3-8** | **audit 완전성 FN 귀속 명시** — CT-4 격리 = audit *위조/삭제* 불가 한정. *기록 누락(observe FN)* = BI-7(observe 면책)/BI-5(sink) 소속임을 §9 에 명시 (BI-3↔BI-5 sliver gap 차단, "T-4 격리=audit 완전"오용 방지) | B-IMPL-3 | 4 |

### 2.3 조건부 4

| # | 조건부 | 조건 |
|---|--------|------|
| CBI3-1 | **TPM/Secure Enclave 를 M2 동급 후보 병치** (C-N-2/R-C3) | "물리 격리" = 외장 토큰(M2) ⊕ 내장 칩(TPM) 양쪽 속성. lock-out SPOF means 별 차이(M2 분실 vs TPM host-bound 소실) §5.2 표. 채택·결정 = entry 발효 (CN-6) |
| CBI3-2 | 백업 키 트레이드오프 식별 (P3 — C-N-5/B-REC-1/R-C4) | "백업 키 = 가용성↑ ⊕ 기밀성↓(공격 표면 N배) + 보관처 §6 동일 침해 경계 회귀 + revocation SOP". *식별* = brief 소관 / *정책 고정* = entry (§13 #4) |
| CBI3-3 | GitHub plan/ruleset 가용성(BI-4) cross-ref (C-N-6) | CT-2(host token) 격리 실효성 = ruleset off 권한 종속 → BI-4 plan 가용성 brief 가 선결. 부록 A cross-ref (T-2 격리가 "token 최소권한"인지 "ruleset 자체 불가"인지 종속) |
| CBI3-4 | N-2 정정 *대상* 명시 (B-REC-5) | 정정 대상 = 원 합의 본문(`f29c772` line 59/92/158). 정정 권한 = entry 합의 또는 별도 정오 단계 (자동 갱신 0건 — brief §0.3 정합) |

### 2.4 권고 (BLOCKING 아님)

- **REC-1**: credential observe = *binary* 성격(주입=즉시 violation, allow-list 의 statistical observe 와 상이) — "Hermes 키 접근 시도 telemetry 0건 N일" 전환 gate 후보 §11 명시 (threshold 고정 0건 유지). [C-N-4/R-C5]
- **REC-2**: lock-out 복구 SOP 골격 + 성능 영향(entrypoint stat 1회·서명 latency=사람 touch 의도된 설계·docker secret 시작 지연 無). [A-REC-2/3]
- **REC-3**: T-5(CT-5) ephemeral runner 보장이 BI-1 범위인지 명시 (CI step 간 env persist = CT-1~CT-4 재구성). [B-REC-2/TH-5]
- **REC-4**: §8 "순이득 음수" = 측정 가능 기준(거짓 안전감 → 침해 탐지 지연) 후보 전환 (entry threshold 입력). [B-REC-3]
- **REC-5**: 4축 line 번호 표기 정밀화 (805 = §5.5.2 일반 SPOF 사유). [N-B4]
- **REC-6**: §10 표에 단일 source-of-truth ⊕ Evidence Ledger(ADR-012 `agent="user"`) ↔ CT-4 격리 인터페이스 (audit forge 방지 G3 line 358 #3 의존). [B-REC-4]

---

## 3. 결정 vs 설계 vs 구현 경계

| 계층 | 본 합의 산출 | 발효 권한 |
|------|-------------|----------|
| **합의 권고 (본 보고서)** | brief AWC / BLOCKING 8 + 조건부 4 + 권고 6 / v2→entry 순서 / 풀 3+1 의무 | Reviewer 종합 — **발효 아님** |
| **brief v2 (DESIGN 정비)** | BI3-1~BI3-8 명시/심화 (라벨·우회 표면·0-구현·공급망·M2 균형·그라데이션·N-1 보존·audit FN 귀속) | **사용자 명시** (실 변경 = brief 문서 한정, 수단 결정 0건) |
| **수단 결정 (DESIGN→IMPL)** | M1~M5/TPM 中 credential 수단 *고정* + BI-3 충족 검증 + 백업 키 정책 | **사용자 명시 + entry 발효 합의(풀 3+1)** (CN-6) |
| **구현 (IMPLEMENTATION)** | 실 env scrub/socket/cap_drop/docker secret/hardware 구성 + Evidence | **Backlog #6 + 별도 발효 + Implementation Evidence PASS** |

---

## 4. 거짓 안전감 차단 재확인 (Reviewer 격상)

**"single-host 충족 = 안전 *확정* 아니라 수용된 SPOF 위 *최선*"**(brief §6, `f29c772` §4 답습)은 유효하며, 본 합의는 그 차단을 *두 방향으로 확장* 한다: (i) **공간 차원**(BI3-4 공급망 P11 — 격리 메커니즘 자체가 supply-chain 으로 무력화) + (ii) **시간/상태 차원**(BI3-6 부분 격리 그라데이션 — 중간 상태가 가장 위험한 거짓 안전감 구간) + (iii) **수단 차원**(BI3-5 — M2 "구조적 흡수" 서사가 *서명 오용 전체 방어*로 과신되는 별도 거짓 안전감). 즉 brief §6 이 "host 침해" 한 축만 차단했다면, 본 합의는 거짓 안전감을 *공급망·중간 상태·수단 과신* 3축으로 확장 차단한다. **이 3축 확장이 BI-3 의 "선결 전제" 명제가 binary·host 중심으로 협소화되지 않게 하는 핵심.**

---

## 5. 미해소 쟁점 / 후속 (사용자 결정 영역 — 자동 진입 0건)

1. **brief v2 작성** = BI3-1~BI3-8 + 조건부 4 + 권고 6 반영 (사용자 명시 — 실 변경 = brief 문서 한정).
2. **credential 수단 최종 결정** = entry 발효 합의(CN-6, 풀 3+1, 사용자 명시).
3. **백업 키 정책**(CBI3-2/BI-9) = 구현 결정.
4. **GitHub plan/ruleset 가용성(BI-4)** = CT-2 격리 선결, 별도 brief.
5. **N-2 + line 번호 정정**(CBI3-4/REC-5) = 원 합의 본문 정오 = entry/정오 단계 권한.
6. **2차 vendor**(Gemini 등) = trigger #7 1건 충족, 추가 = 사용자 결정.
7. **TPM/Secure Enclave·sigstore/Rekor**(CBI3-1/BI3-7) = 후보 보존, MVP 채택 여부 = entry 결정.

---

## 6. 합의 한 문단 요약

**BI-3 credential 격리 brief(DRAFT v1) 검증 = APPROVE WITH CONDITIONS** — 세 Agent 가 (1) brief 의 출처 정합·본문 변경 유발 0, (2) **§7.2 N-2 citation 정밀화("GP-3 §6.2" → 실제 GP-3 = §5, §6.2 는 GP-4 의 P5)가 사실 정확**(3 Agent 독립 grep 으로 governance line 468/526/534 검증), (3) M2(hardware-backed key) "구조적 흡수"는 *키 추출* 차원만 성립·서명 오용은 별개, (4) means/ends 분리 선언 양호 에 일치했다. 가장 무게 있는 교차 발견은 **세 Agent 가 서로 다른 입구로 수렴한 "M2 흡수 서사 과신 위험"**(B 거짓 안전감 / C means 편향·후보 공간 협소 / A touch-policy 능동 메커니즘 누락 = BI3-5 우선순위 1)이며, 각 Agent 단독 객관 누락은 A: **"T-1~T-5" 라벨이 GP-5 "T-1~T-6"와 충돌**(BI3-1)+docker socket host escape(BI3-2), B: **공급망 P11 인터페이스**(BI3-4)+**부분 격리 그라데이션**(BI3-6), C: **N-1/CBI-4 sigstore/Rekor 본문 누락 비대칭**(BI3-7)+TPM 후보(CBI3-1)다. 구현 발효 전 **BLOCKING 8건**(BI3-1 라벨 재명명 / BI3-2 구체 우회 표면·docker socket / BI3-3 0-구현+ends 동등성 명시 / BI3-4 공급망 P11 / **BI3-5 M2 거짓 안전감 차단·touch-policy** / BI3-6 부분 격리 그라데이션 / BI3-7 N-1 본문 보존 / BI3-8 audit 완전성 FN 귀속) + 조건부 4건(TPM 병치 / 백업 키 역설 / BI-4 plan cross-ref / N-2 정정 대상) + 권고 6건이며, 우선순위는 **M2 흡수 거짓 안전감(BI3-5, 3 수렴) 최강**이다. 본 합의는 거짓 안전감 차단을 brief §6 의 host 침해 1축에서 **공급망·중간 상태·수단 과신 3축으로 확장**한다. 다음 단계 = **§13 옵션 B→A**(brief v2 → credential 수단 결정 합의), credential 수단 결정 = 풀 3+1 의무. **모든 BLOCKING = brief 단계 심화/명시로 해결 — 수단 결정·hardware key 채택·실 구성 요구 0건.** 본 합의는 추론적 검증(권고) 한정 — 수단 *결정*·실 구현·commit·push 는 사용자 명시 + 별도 단계이며, **본 보고서 외 어떤 파일도 편집/생성하지 않고 commit/push 0건**이다.

---

## 7. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | brief 정합·N-2 정밀화 grep 검증 정확·M2 흡수 기술 정확(SSH sk-key/GPG card·touch policy). 단 어느 수단도 0-구현 아님. **BLOCKING 3**(A-IMPL-1 0-구현 명시 / A-IMPL-2 구체 우회 표면·docker socket / **A-IMPL-3 T-n 라벨 GP-5 충돌**). 권고 4(touch policy·lock-out SOP·성능·audit credential 분리) |
| **Agent B** (보안) | "안전하고 견고한가?" | AWC. 강점 = §6 거짓 안전감 + N-2 정밀화. **BLOCKING 5**(B-IMPL-1 공급망 P11 / B-IMPL-2 touch-to-sign 흡수 위치 오류 / B-IMPL-3 audit 완전성 FN / B-IMPL-4 M2 거짓 안전감 별도 차단 / B-IMPL-5 부분 격리 그라데이션). 정합성 모순 0·본문 변경 0. "선결 전제 명제가 binary·host 중심으로 협소화" |
| **Agent C** (대안) | "더 나은 방법?" | AWC. 강점 인정·약점 = 수단 후보 공간 빈약(저장 매체 1축). **누락**: C-N-1 N-1/CBI-4 본문 누락(비대칭) / C-N-2 TPM/Secure Enclave(M2 SPOF 비용0 우회) / C-N-3 강제 메커니즘 축(rootless/userns) / C-N-5 백업 키 역설(공격 표면 N배) / C-N-6 BI-4 plan cross-ref. DV-C1 M2 흡수 서사 = means 편향. v2→entry 순서 권고 |
| **Reviewer** | "최선의 합의는?" | 교차(일치 6 / 부분 3 / 불일치 1 / 누락 10) + BLOCKING 통합(8건, M2 거짓 안전감 BI3-5 최강) + 조건부 4 + 권고 6 + 거짓 안전감 3축 확장(공급망·중간상태·수단과신) + N-2 정밀화 3중 독립 검증 확인. **APPROVE WITH CONDITIONS, v2→entry 순서** |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**credential isolation 실 구성**(사람 signing key·token·SSH/GPG agent socket 미주입 / env scrub / socket 미마운트 / `cap_drop` / docker secret / chmod·entrypoint stat 본문) / **hardware-backed key·TPM 채택 *결정*·토큰 벤더 고정·백업 키 정책 고정**(CBI-1/BI-9/CBI3-1/CBI3-2) / 실 hook 구현(pre-commit / pre-receive / git server-side / CI provenance step) / GitHub ruleset·branch protection·required-signature·bypass 정책 실 변경 / CI workflow 변경(provenance step / actual run / workflow_dispatch / paths 필터) / filesystem ACL·`read_only` mount·audit sink 실 구성 / Hermes runtime·upstream 변경(Dockerfile / `hermes-version.yaml` / upstream PR / ST-1·ST-5 진입) / 수단 결정 *고정*(격리 방식·키 매체·secret source — CN-6) / threshold 고정(observe mode 기간) / **Operational Readiness PASS(Layer E)** / **Hermes PMO 격상(Layer F)** / Vault HSM ST-4 진입(γ-2 DEFER MVP-6) / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 재변경(특히 line 358/360/784/805 4축) / GP-3 본문 변경 / ADR 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정**(N-2/line 번호 정정 = 권고 한정, entry/정오 단계 권한) / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / G1(PR·approval auto-reject) 신규 단위 자동 진입 / Backlog #4 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / brief v2·합의 보고서 외 파일 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
