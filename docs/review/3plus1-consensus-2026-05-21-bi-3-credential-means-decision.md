# 3+1 합의 보고서 — BI-3 Credential 격리 수단 *결정* 권고

> **본 합의 = 추론적 검증(권고) 한정.** 4축 frame + BI-3 = 4축 공통 선결 전제는 `f6c6d5a`+`f29c772`+`cc5b517` 만장일치 확정 — 재논쟁 없음. 본 합의는 **credential 격리 수단 *결정 권고* + BI-3 충족 검증 기준 + 백업 키 정책 + 결정 구조** 만 다룬다. **수단 *결정 고정* / hardware·TPM key 채택 *결정* / credential isolation 실 구성 / 실 hook·ruleset·CI·audit sink / 다른 BLOCKING(BI-1/2/4~10) 해소 / Vault HSM ST-4 진입 / Operational Readiness PASS / Hermes PMO 격상 / commit·push 외 변경 = 모두 0건.** 실 결정/구현 = 사용자 명시 + 별도 entry 발효 단계.

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — **의무** (BI-3 = T3 보안 enforcement 최강 BLOCKING + 핵심 제약 #1 직결 + 아키텍처 의사결정). Reviewer-only 부적격
**합의 입력**: `docs/phase0/bi-3-credential-isolation-brief.md` (DRAFT v2, `bf42d0e`)
**1차 권위 답습**: `cc5b517` BI-3 brief 검증 합의 (BI3-1~8 + CBI3-1~4) + `f29c772` Group I 구현 entry 합의 (§2.4 수단 권고 — 본 합의가 *정제*) + GP-3 §5 + γ-1 `9b1f8cd`(ST-1)·γ-2 `2e9d46b`(ST-4 DEFER) + ADR-011 §2.1 means/ends (a)~(d) + roadmap §3.6(단계적)·§5.4(환경 분기)
**판정**: **APPROVE WITH CONDITIONS** — 권고 결정 = **host-bound 물리 격리(TPM/Secure Enclave) 1순위 + M2(외장 토큰) = touch-to-sign 자동 서명 차단 필수 시 보강 + M1 공통 위생 + 환경 분기 결정 구조**. ⭐ 직전 `f29c772` "M2 1순위 동급 병치" → **TPM/host-bound 1순위로 정제** (B·C 독립 수렴). 단 수단 *고정*·실 구현·다른 BLOCKING 해소 = entry 발효 별도. **BLOCKING 10(CD-1~CD-10) + 조건부 3.**

---

## 0. 종합 판정 (한 문단)

세 Agent 는 **(1) M1(미주입)은 단독 부적격** — 행위 규칙(soft)이며 single-host 에서 키가 host 어딘가 잔존하는 gap 이 구조적으로 남으므로 *대체 수단이 아니라 모든 물리 격리 수단의 공통 전제 위생*(env scrub·socket 미마운트·cap_drop), **(2) 물리 격리(키가 칩/토큰 밖 미이탈)가 1순위**로 single-host 의 "동일 host 키 공유 gap"을 구조적으로 소멸시키며 **Hermes upstream 변경 0건**으로 달성(컨테이너가 서명 능력을 아예 미보유), **(3) M3(vault)는 single-host unseal 자격 재귀로 부적격·M4(ST-4)/M5(keyless) MVP-6 DEFER**, **(4) docker socket 미마운트 + CAP_SYS_PTRACE drop 은 *어느 수단을 택해도* 비협상 동반**(host escape·메모리 scrape 는 키 격리와 직교·최치명), **(5) BI-3 충족은 *수단 라벨* 이 아니라 *계산적/적대적 침투 시연 실패*(binary)로만 입증** 된다는 데 일치한다. 가장 무게 있는 교차 발견은 **Agent B(보안)와 Agent C(대안)가 서로 다른 입구로 "TPM/host-bound 물리 격리 1순위"에 독립 수렴** 한 점이다 — B 는 "TPM 이 M2 의 백업 키 역설(N개 등록 = CT-1 공격 표면 N배)을 *분실 SPOF 부재* 로 구조적 회피", C 는 "비용 0·운영 단순·lock-out 안전·**Provider Liquidity 우위**(토큰 벤더 lock-in > OS 종속) 5/6 축 우위" — 이는 직전 `f29c772` §2.4 의 "M2 hardware key 1순위 동급 병치" 권고를 **정제**한다. Agent A(구현)는 "플랫폼 의존 동급 병치"(macOS=Secure Enclave / Linux=YubiKey-SSH 연동 단순성 ≥ TPM PKCS#11 브리지)를 들어 약간 다른 결을 보였으나, **세 관점을 통합하면 진정한 합의 = "host-bound 물리 격리 default(플랫폼별: macOS Secure Enclave / Linux TPM·YubiKey) + M2 외장 토큰 = touch-to-sign 자동 서명 차단이 위협 모델상 필수일 때 보강"의 *비대칭 순위화 + 환경/플랫폼 분기*** 이다("동급 병치"는 두 수단의 우위 축이 *직교*[TPM=가용성/비용/PL, M2=물리 터치]함을 흐린다). 또한 C 단독으로 **결정 *구조* 대안**(단일 수단 고정 → 환경 분기[local 물리격리 / Docker M1+secret / CI ephemeral+fingerprint, roadmap §5.4 선례] + 추상 인터페이스[ADR-011 (a) 교체 경로] + 단계적 채택[roadmap §3.6 선례])을 제시 — means 편향 해소의 핵심. 본 합의 = **추론적 검증(권고) 한정 — 수단 결정·실 구현·commit·push 는 사용자 명시 + 별도 entry 발효 단계.**

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3 Agent 모두)

| # | 합의 항목 | A | B | C |
|---|----------|---|---|---|
| C1 | **M1(미주입) 단독 부적격** = 행위 규칙(soft) — 모든 물리 격리 수단의 *공통 전제 위생*, 대체 수단 아님 | ✅ (골격) | ✅ (단독 부적격) | ✅ (공통 하부) |
| C2 | **물리 격리(TPM/M2)가 1순위** — 키 칩/토큰 밖 미이탈로 "동일 host 키 공유 gap" 구조적 소멸 | ✅ | ✅ | ✅ |
| C3 | **물리 격리 = Hermes upstream 변경 0건** (컨테이너가 서명 능력 미보유, 서명은 host 책무) | ✅ | (정합) | (정합) |
| C4 | M3(vault) single-host 부적격(unseal 자격 재귀) / M4(ST-4)·M5(keyless) MVP-6 DEFER | ✅ | ✅ | ✅ |
| C5 | **docker socket 미마운트 + CAP_SYS_PTRACE drop = 어느 수단 택해도 비협상 동반** (host escape·scrape = 키 격리와 직교·최치명) | ✅ | ✅ (B-DEC-4) | ✅ (환경분기) |
| C6 | touch policy=always = M2 *자동* 서명 차단 능동 메커니즘이나 *사회공학* 서명 오용은 못 막음 | ✅ (E-11) | ✅ (§3) | ✅ (§2.1) |
| C7 | **BI-3 충족 = 수단 라벨 ≠ 입증. 계산적/적대적 시연(binary)으로만** | ✅ (E-1~11) | ✅ (PEN-1~8) | ✅ (observe binary) |
| C8 | host 침해(§6 동일 침해 경계)·공급망 P11·부분 격리 = *수단 무관* 직교 잔존 → 거짓 안전감 차단 동반 | ✅ (A-DEC-4) | ✅ (전체) | ✅ |
| C9 | CT-2(host token) 격리 실효성 = BI-4(GitHub plan/ruleset 가용성) 종속 | ✅ (A-DEC-6) | ✅ (조건부) | (brief §7.4) |
| C10 | N-2 citation 사실 정확 재확인 ("GP-3 §6.2" → 실제 GP-3 = §5) — 독립 grep | ✅ | ✅ | (정합) |

### 1.2 부분 일치 (Partial — 2 동의, 1 강조/추가/이견)

| # | 항목 | 분류 |
|---|------|------|
| P1 ⭐ | **TPM/host-bound 물리 격리 1순위 (M2 동급 아님)** | **B 강하게(백업키 역설 회피) + C 강하게(5/6 축 + PL 우위) 독립 수렴** / A = "플랫폼 의존 동급 병치"(Linux YubiKey-SSH 연동 단순성) — D1 참조 |
| P2 | **백업 키 = TPM 우선으로 표면 최소화** (TPM=0개 재생성 SOP / M2=2개 offline·cold 봉인 seed + revocation SOP) | B(TPM 0개·M2 2개 air-gapped) + C(offline cold 종이 seed, hot 복제 회피) 강하게 수렴 / A(재배포·revocation = allowed_signers 편집, 경로 T3 보호) 구현 측면 |
| P3 | **결정 구조 = 단일 수단 고정 아님** (환경 분기 + 추상 인터페이스 + 단계적 채택) | C 단독 명시(C-DEC-4, roadmap §3.6/§5.4 선례) / A 부분 정합(host/컨테이너 분리 실 구성·조합) / B 미명시 — Reviewer 격상(roadmap 선례로 객관) |

### 1.3 불일치 (Divergence)

| # | 항목 | A | B | C | Reviewer |
|---|------|---|---|---|----------|
| D1 ⭐ | **TPM vs M2 순위** | 플랫폼 의존 **동급 병치** (Linux YubiKey-SSH `sk-` 연동 ≥ TPM `tpm2-pkcs11` PKCS#11 브리지 단순성) | **TPM 1순위** (백업키 역설 회피) | **TPM 1순위** (비용·운영·lock-out·PL 5/6 축) | **진정 충돌 아닌 *우위 축 직교* — TPM = 가용성/비용/운영/Provider Liquidity, M2 = touch-to-sign 자동 서명 차단 *물리성*. A 의 연동 단순성 지적은 실재(Linux TPM 브리지 한 단계 더)하나 *플랫폼 종속* 이며, B/C 의 TPM 우위 축(백업키 역설·PL)이 더 무겁고 직교. 합의 = "host-bound 물리 격리 default(플랫폼별: macOS Secure Enclave / Linux TPM·YubiKey) + M2 = touch-to-sign 필수 시 보강"의 *비대칭 순위화*. '동급 병치' 폐기, 'TPM/host-bound 1순위 + 플랫폼/환경 분기'로 수렴 (CD-1)** |

### 1.4 누락 (Gap — 단독 발견, Reviewer 중요도)

| # | 항목 | 언급 | 중요도 | 처리 |
|---|------|-----|-------|------|
| N-A1 | **서명 키 격리 ≠ ST-1(entrypoint stat)** — 서명 키 격리 = Hermes Dockerfile 변경 0건(컨테이너 서명 능력 미보유). ST-1 = 파일 권한 검증. 묶으면 R-MVP1-G3-7 upstream 풀3+1 trigger 불필요 발화 | A | **높음** (객관) | **CD-4** |
| N-A2 | E-1~E-11 계산적 PoC 골격 (컨테이너 내 키/socket/token/docker.sock/cap 0건 시연) | A | 높음 | CD-5 |
| N-B1 | **PIN 캐시 = 서명 오용 시간 창** (cache-ttl 길면 touch policy 우회) → PIN 캐시 비활성 | B | **높음** | CD-6 |
| N-B2 | **시연 image = 운영 image digest 일치** (공급망 위장 차단 — 시연 깨끗·운영 변조) | B | **높음** | CD-9 |
| N-B3 | 서명 컨텍스트 out-of-band 확인 (사회공학 차단 유일 방어, single-host 에선 확보 어려움 = 잔여 명시) | B | 중-높음 | CD-6 |
| N-C1 ⭐ | **결정 구조 대안** (환경 분기[local/Docker/CI] + 추상 인터페이스[ADR-011 (a)] + 단계적 채택, roadmap §3.6/§5.4 선례) | C | **높음** | **CD-8** |
| N-C2 | **백업 키 역설 회피 = offline·cold·물리 봉인 recovery seed** (동급 hot 복제 강등, 평상시 활성 키 1개 = 표면 증가 0) | C | 높음 | CD-7 |
| N-C3 | M5 = credential 축 DEFER ⊕ **audit 축(BI-5) 재평가 후보 cross-축 보존** (Rekor 시너지 trigger 누락 방지) | C | 중-높음 | 조건부 CD-CBI-1 |
| N-C4 | grace-period soft fallback = bypass 창 → Rollback Trigger 항목 | C | 중 | 조건부 CD-CBI-3 |
| N-A3 | M3 single-host 부적격 사유 = unseal 자격 재귀 (2순위 강등 명시) | A | 중 | 조건부 CD-CBI-2 |

---

## 2. 합의 도출

### 2.1 권고 결정 (수단 — Reviewer 종합)

> **본 §2.1 = 추론적 *권고* — 수단 *고정* 은 entry 발효 + 사용자 명시 (CN-6).**

```
[공통 전제 위생]  M1 미주입 : env scrub · agent socket 미마운트 · cap_drop[ALL + SYS_PTRACE]
                              · docker socket 미마운트(최치명) · credential helper/GIT_ASKPASS 비활성
        ⊕
[1순위: 물리 격리(host-bound)]  플랫폼별 default —
        · macOS  → Secure Enclave
        · Linux  → TPM (tpm2-pkcs11) 또는 YubiKey-SSH (sk-ssh-ed25519, 연동 단순성)
        · 선택 = host-bound(TPM/SE) 우선 (백업키 역설 회피 · 비용 0 · PL 우위)
        ⊕
[보강: M2 외장 토큰]  touch-to-sign(verify-required=always) 자동 서명 차단이
        BI3-5 위협 모델상 필수로 판정될 때 — touch policy=always + PIN 캐시 비활성 비협상
        ⊕
[저장]  ST-3 docker secret + ST-1 entrypoint stat (앱 secret P3 — 서명 키 격리와 *별개*)
```

| 수단 | 권고 | 근거 |
|----|----|----|
| **host-bound 물리 격리 (TPM/Secure Enclave)** | **1순위 (default)** | C2(구조적 흡수) + B(백업키 역설 회피) + C(비용·운영·lock-out·PL 5/6 축) |
| **M2 외장 토큰 (YubiKey/FIDO2)** | **보강 (touch-to-sign 필수 시)** | C6(자동 서명 차단 물리성) — 단 백업키 SPOF·벤더 lock-in |
| M1 미주입 | **공통 전제 위생** (대체 수단 아님) | C1 |
| M3 vault | 2순위 강등 (single-host unseal 재귀) | C4 / A-DEC-7 |
| M4 (ST-4) / M5 (keyless) | **MVP-6 DEFER** (M5 = audit 축 cross-보존) | C4 / γ-2 / CBI-4 |

### 2.2 구현 발효 전 BLOCKING 통합 (A 7 + B 6 + C 8 → 중복 제거 10건)

**우선순위: CD-1(순위 정제) > CD-3(docker socket·ptrace) > CD-5(침투 시연 종료) > CD-2(조합/공통위생) > CD-8(결정 구조) > CD-7(백업키) > CD-6(touch policy 잔여) > CD-4(서명키≠ST-1) > CD-9(공급망) > CD-10(guardrail).**

| # | BLOCKING | 출처 | 우선 |
|---|----------|------|------|
| **CD-1** ⭐ | **"M2 1순위 동급 병치" → "host-bound 물리 격리(TPM/Secure Enclave) 1순위 + M2 = touch-to-sign 필수 시 보강" *비대칭 순위화*** + 플랫폼별 default(macOS SE / Linux TPM·YubiKey, 실제 host OS 확인 = entry). 우위 축 직교 명시 | D1 (B+C 수렴, A 통합) | **1** |
| **CD-2** | **수단 = 단일 아니라 *조합*** — M1 공통 전제 위생(대체 수단 아님) ⊕ 물리 격리(CT-1/CT-3) ⊕ ST-3. brief §4 표에서 M1 = "공통 하부"로 재배치 | A-DEC-1 + C-DEC-6 | 2 |
| **CD-3** ⭐ | **docker socket 미마운트 + CAP_SYS_PTRACE drop = 어느 수단 택해도 비협상 동반** (PEN-5/PEN-1, host escape·메모리 scrape = 키 격리와 직교·최치명) | A §4 + B-DEC-4 | **1** |
| **CD-4** | **서명 키 격리 ≠ ST-1(entrypoint stat)** — 서명 키 격리 = Hermes Dockerfile 변경 0건(컨테이너 서명 능력 미보유). ST-1 = 파일 권한 검증 (별개 책무). 묶으면 upstream 풀3+1 trigger 불필요 발화 | A-DEC-3 단독 | 3 |
| **CD-5** | **BI-3 충족 = 계산적 PoC(E-1~11: 컨테이너 내 키/socket/token/`docker.sock`/cap 0건) + 적대적 침투 시연(PEN-1~8 전부 실패) + 운영 image digest 일치. binary — 부분 통과 = FAIL. 수단 라벨 ≠ 충족** | A E + B PEN 수렴 | **1** |
| **CD-6** | **touch policy=always + PIN 캐시 비활성 = M2 채택 비협상** + 사회공학 서명 오용(host 미침해서도 성립)은 *잔여 위협* 명시 (touch 만으로 미차단). out-of-band 컨텍스트 확인 = single-host 에선 확보 어려움 = 잔여 | B-DEC-3 + A E-11 + C | 2 |
| **CD-7** | **백업 키 = TPM 우선으로 표면 최소화** — TPM 채택 시 0개(재생성 SOP) / M2 채택 시 정확히 2개·offline·air-gapped·**물리 봉인 recovery seed** + revocation SOP(분실 추적·off-host 강제·audit 기록). 재배포·revocation 경로 = T3 보호(Hermes 미주입) | B-DEC-2 + C-DEC-2 + A-DEC-5 | 2 |
| **CD-8** ⭐ | **결정 *구조* = 단일 수단 고정 아님** — (a) 환경 분기(local 물리격리 / Docker M1+secret / CI ephemeral+fingerprint, roadmap §5.4 선례) + (b) 추상 인터페이스(`Signer`/`CredentialSource`, ADR-011 §2.1(a) 교체 경로 코드 박제) + (c) 단계적 채택(MVP-1=TPM → 1.5차 M2 보강, roadmap §3.6 선례). means 편향 해소 | C-DEC-4 단독 | 2 |
| **CD-9** | **공급망 P11·부분 격리 그라데이션 = 수단 무관 잔존** — 시연 image = 운영 image digest 일치 + 격리 메커니즘 자체(scrub script·touch policy 설정·docker-compose) 무결성 보호. 수단 선택이 W3/W4 완화 안 함 | B-DEC-5 + brief §8.2/8.3 | 3 |
| **CD-10** | **거짓 안전감 guardrail G-1~G-7 = 결정문 비협상 동반** (특히 G-7 자기검증 금지=Hermes≠root, G-2 SPOF 위 최선) + CT-2 격리 = BI-4 plan/ruleset 종속 cross-ref | B-DEC-6 + A-DEC-6 + C | 3 |

### 2.3 조건부 3

| # | 조건부 | 조건 |
|---|--------|------|
| CD-CBI-1 | M5(keyless) = credential 축 DEFER ⊕ **audit 축(BI-5) 심화 시 재평가 후보 cross-축 보존** (Rekor↔BI-5 시너지 trigger 누락 방지) | C-DEC-5 |
| CD-CBI-2 | M3(vault) 2순위 강등 = single-host unseal 자격 재귀 사유 명시 | A-DEC-7 |
| CD-CBI-3 | grace-period soft fallback(백업 키 대안) 채택 시 = grace 창 = bypass 창 → §11.2 Rollback Trigger 항목 동반 | C-DEC-8 |

---

## 3. 결정 vs 설계 vs 구현 경계

| 계층 | 본 합의 산출 | 발효 권한 |
|------|-------------|----------|
| **합의 권고 (본 보고서)** | TPM/host-bound 1순위 + M2 보강 + M1 공통위생 + 환경분기 결정구조 / BLOCKING 10 + 조건부 3 | Reviewer 종합 — **발효 아님** |
| **수단 결정 *고정* (DESIGN→IMPL)** | 실제 host OS 확인 후 TPM/SE/M2 *결정* + 백업 키 정책 *고정* + 추상 인터페이스 *채택* | **사용자 명시 + entry 발효** (CN-6) |
| **BI-3 충족 검증 (Evidence)** | E-1~11 PoC + PEN-1~8 침투 시연 *실 실행* + image digest 일치 | **Implementation Evidence PASS (격리 환경)** |
| **구현 (IMPLEMENTATION)** | 실 env scrub/cap_drop/docker secret/물리 키 구성 + 다른 BLOCKING(BI-1/2/4~10) | **Backlog #6 + 별도 발효** |

---

## 4. 거짓 안전감 차단 (Reviewer 격상)

본 합의의 가장 위험한 실패 양식은 *미격리* 가 아니라 **"수단을 결정·채택했으니 격리됐다고 믿는 미격리"**(거짓 안전감 = 음의 순이득, brief §8.1). 따라서: (i) 수단 결정은 **CD-5 침투 시연(PEN-1~8 binary)** + **CD-10 guardrail G-1~G-7** 과 *한 묶음으로만* 유효 — 단독 수단 결정 = 음의 순이득. (ii) **TPM/M2 채택 ≠ 서명 안전 확정** — 물리 격리는 *키 추출* 한정 흡수, *서명 오용*(사회공학)·host 침해·공급망 P11·부분 격리는 직교 잔존(수단 무관, CD-6/CD-9). (iii) 격리 검증은 **Hermes 권한 밖 anchor** 가 확인(자기검증 금지, Hermes≠root). **"single-host 충족 = 수용된 SPOF 위 최선, 안전 확정 아님"** 명시.

---

## 5. 미해소 쟁점 / 후속 (사용자 결정 영역 — 자동 진입 0건)

1. **수단 최종 결정·고정** (실제 host OS 확인 후 TPM/SE/M2) = entry 발효(CN-6, 사용자 명시).
2. **백업 키 정책 고정** (개수·보관·revocation SOP) = 구현 결정 (CD-7).
3. **추상 인터페이스·환경 분기 설계 채택** = 구현 entry (CD-8).
4. **BI-3 충족 = E-1~11 + PEN-1~8 실 실행** = Implementation Evidence PASS (격리 환경).
5. **다른 BLOCKING(BI-1/2/4~10) 해소** = 각 별도 단위 — 특히 **BI-4(GitHub plan/ruleset 가용성) = CT-2 격리 선결** (CD-10/C9).
6. **N-2 + line 번호 정정** = 원 합의 `f29c772` 본문 정오 = entry/정오 단계 (자동 갱신 0건).
7. **2차 vendor** = trigger #7 1건 충족, 추가 = 사용자 결정.

---

## 6. 합의 한 문단 요약

**BI-3 credential 격리 수단 *결정 권고* = APPROVE WITH CONDITIONS, 권고 결정 = host-bound 물리 격리(TPM/Secure Enclave) 1순위 + M2(외장 토큰) = touch-to-sign 자동 서명 차단 필수 시 보강 + M1 공통 전제 위생 + 환경 분기 결정 구조**이다. 세 Agent 는 (1) M1 단독 부적격(공통 위생이지 대체 수단 아님), (2) 물리 격리 1순위(Hermes upstream 변경 0건), (3) M3 single-host 부적격·M4/M5 MVP-6 DEFER, (4) **docker socket 미마운트 + CAP_SYS_PTRACE drop = 수단 무관 비협상**, (5) BI-3 충족 = 수단 라벨 ≠ 입증·계산적/적대적 시연(binary)으로만 에 일치했다. 가장 무게 있는 발견은 **Agent B(백업 키 역설 회피)와 Agent C(비용·운영·lock-out·Provider Liquidity 5/6 축)가 독립 수렴한 "TPM/host-bound 1순위"** 로, 직전 `f29c772` "M2 1순위 동급 병치"를 **정제** 한다(Agent A 의 "플랫폼 의존 동급 병치"[Linux YubiKey-SSH 연동 단순성]는 *우위 축 직교*[TPM=가용성/비용/PL, M2=물리 터치]로 통합 — '동급 병치' 폐기, 'host-bound default + 플랫폼/환경 분기'로 수렴). Agent C 단독으로 **결정 *구조* 대안**(환경 분기[local/Docker/CI, roadmap §5.4 선례] + 추상 인터페이스[ADR-011 (a) 교체 경로] + 단계적 채택[roadmap §3.6 선례])을 제시해 means 편향을 해소했다. 구현 발효 전 **BLOCKING 10**(CD-1 순위 정제 / CD-2 조합·공통위생 / CD-3 docker socket·ptrace 비협상 / CD-4 서명키≠ST-1 / CD-5 침투 시연 binary 종료 / CD-6 touch policy+PIN+사회공학 잔여 / CD-7 백업키 TPM 우선·offline cold / CD-8 결정 구조 / CD-9 공급망·그라데이션 수단무관 / CD-10 guardrail 동반) + 조건부 3(M5 audit축 보존 / M3 강등 / grace-period rollback)이며, 거짓 안전감 차단(수단 결정 ≠ 안전 확정·침투 시연+guardrail 한 묶음)을 Reviewer 격상했다. 교차 = 일치 10 / 부분 3 / 불일치 1(우위 축 직교) / 누락 10. 본 합의는 추론적 검증(권고) 한정 — 수단 *결정 고정*·hardware/TPM 채택·백업 키 정책 고정·실 구성·다른 BLOCKING 해소·commit·push 는 사용자 명시 + 별도 entry 발효 단계이며, **본 보고서 외 어떤 파일도 편집/생성하지 않고 commit/push 0건**이다.

---

## 7. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | **조합 권고** (M1 골격 + 물리격리[플랫폼별 TPM/SE/YubiKey] + ST-3 + docker socket 미마운트 + cap_drop). 둘 다 git 서명 *실 동작*·Hermes upstream 0건. M3 강등·M4/M5 DEFER. BI-3 충족 = E-1~11 계산적 PoC. BLOCKING 7(A-DEC-1~7), 최강 = 조합 명시·**서명키 격리≠ST-1**(A-DEC-3 단독) |
| **Agent B** (보안) | "안전하고 견고한가?" | **TPM 1순위**(백업키 역설 회피), M2 동급(touch policy=always 비협상), M1 단독 부적격. 어느 수단도 host 침해·공급망·서명오용·부분격리 직교 잔존. BI-3 충족 = PEN-1~8 침투 시연. guardrail G-1~G-7 비협상. BLOCKING 6(B-DEC-1~6). "거짓 안전감 = 음의 순이득" |
| **Agent C** (대안) | "더 나은 방법?" | **TPM 명확한 1순위**(5/6 축 + PL 우위), M2 = touch-to-sign 필수 시 보강(비대칭 순위화). **결정 구조 = 환경 분기 + 추상 인터페이스 + 단계적 채택**(roadmap 선례). 백업키 역설 = offline cold seed 로 회피. M5 = audit축 cross-보존. C-DEC-1~8 |
| **Reviewer** | "최선의 합의는?" | 교차(일치 10 / 부분 3 / 불일치 1 / 누락 10) + B·C 독립 수렴 = **TPM/host-bound 1순위 정제**(f29c772 M2 1순위 → 비대칭 순위화) + BLOCKING 통합 10 + 조건부 3 + 결정 구조(C 격상) + 거짓 안전감 차단 격상. **APPROVE WITH CONDITIONS** |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**credential isolation 실 구성** (env scrub / socket 미마운트 / `cap_drop` / docker secret / chmod·entrypoint stat 본문) / **hardware·TPM·Secure Enclave key 채택 *결정*·토큰 벤더·OS 고정·백업 키 정책 고정** / **추상 인터페이스·환경 분기 실 설계 채택** / **물리 키 생성·`allowed_signers` 작성·서명 구성** / **실 hook 구현** (pre-commit / pre-receive / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / paths 필터) / **filesystem ACL·`read_only` mount·audit sink 실 구성** / **BI-3 충족 PoC(E-1~11)·침투 시연(PEN-1~8) 실 실행** / **sigstore·Rekor 도입** (M5/CBI-4 DEFER) / **Hermes runtime·upstream 변경** (Dockerfile / `hermes-version.yaml` / ST-1·ST-5 진입) / **Vault HSM ST-4 진입** (γ-2 DEFER MVP-6) / 수단 결정 *고정* (CN-6) / threshold 고정 / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 재변경 / GP-3 본문 변경 / ADR 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** (N-2/line 번호 = 권고 한정, entry/정오 단계 권한) / Group I·α·β·γ 합의 본문 변경 / **다른 BLOCKING(BI-1/2/4~10) 자동 진입** (특히 BI-4 GitHub plan/ruleset 가용성 = CT-2 격리 선결, 별도 단위) / G1 (PR·approval auto-reject) 신규 단위 자동 진입 / Backlog #4 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 외 파일 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
