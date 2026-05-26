# 3+1 합의 보고서 — Credential 수단 *발효* entry brief + H-1 docker group hole 해소 검토

> **본 합의 = 추론적 검증(권고) 한정.** 본 합의는 **credential 수단 발효 진입 brief + H-1 해소 검토 brief 의 정합·안전·대안 검증 + 발효 선결 BLOCKING 통합** 만 다룬다. **수단 *결정 고정*(TPM vs YubiKey)·tpm2-pkcs11 등 설치·tss/docker group 변경·rootless 전환·서명 키 생성·git 서명 구성·BI-3 충족 PoC(E-1~11)·침투 시연(PEN-1~8) 실 실행·brief 본문 수정 발효·Operational Readiness PASS·Hermes PMO 격상·commit·push = 모두 0건.** 실 결정/구현/brief 수정 발효 = 사용자 명시 + 별도 단계.

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — **의무** (BI-3 = T3 보안 enforcement 최강 BLOCKING + 핵심 제약 #1 직결 + 수단 발효 진입 = 아키텍처 의사결정). Reviewer-only 부적격
**합의 입력**: `docs/phase0/credential-means-activation-entry-brief.md` (DRAFT v1) + `docs/phase0/h1-docker-group-hole-resolution-brief.md` (DRAFT v1)
**1차 권위 답습**: `ead5754` BI-3 수단 결정 합의 (CD-1~10 + CD-CBI-1~3, 특히 CD-1 비대칭 순위화·D1 우위축 직교·CD-3 docker socket·ptrace 비협상·CD-5 binary·CD-6 touch policy·CD-7 백업키·CD-8 결정 구조) + 4축 통합 정리 brief §6/§7.2/§7.4 (IB-2 owner self-bypass 잔존·IB-4 P-5 축별·IR-4 2-track) + ADR-011 §2.1 means/ends + [[feedback_provider_liquidity]]
**판정**: **APPROVE WITH CONDITIONS** — 두 brief = *발효 진입·검토* 단계로서 범위(권고 한정·실 변경 0건) 준수, host 사실 정확(실 read-only 재검증), citation stale 0. 단 **수단 *결정 고정* 전 BLOCKING 7(CMA-1~7) 해소 필요**. ⭐ **핵심 = host 실측이 `ead5754` D1("Linux TPM 연동 단순성 ≤") 추론을 *역전* — 수단 1순위 권고를 재평가(대칭 병치) 후 결정 + touch-to-sign 을 수단 무관 비협상 하한선으로 격상.** **BLOCKING 7(CMA-1~7) + 권고 10.**

---

## 0. 종합 판정 (한 문단)

세 Agent 는 모두 **APPROVE WITH CONDITIONS** 로 수렴했고, (1) 두 brief 가 **H-1(docker group hole)을 "수단 결정 *이전* 선결"로 격상한 것이 정확하고 가장 중요한 판단** — 이 격상이 없었으면 수단 결정 자체가 거짓 안전감의 시발점(A 핵심1·B 핵심1), (2) **TPM 비추출성(키 칩 밖 미이탈)은 유지되나 서명 *능력*(서명 요청)은 root-동치 계정이 탈취 가능** = 격리의 실 경계(A-2·B R-2·C-2), (3) **citation stale 0**(CP-10 메타 답습 효과 유지, BI-3 N-2→BI-4→BI-5 3연속 stale 단절이 본 발효 entry 에서도 유지), (4) **owner self-bypass(IB-2) 4축 잔존** 에 일치했다. 가장 무게 있는 발견은 **Agent C 가 host 실측으로 `ead5754` D1 추론을 *역전* 시킨 점** — `ssh-sk-helper`(264KB, 실재)·`libfido2 1.14.0`(설치됨)·OpenSSH 9.6 `sk-` 지원으로 **YubiKey 경로 host-side 스택은 이미 준비**된 반면 **TPM 경로(`tpm2-pkcs11`/`ssh-tpm-agent`)는 0개 설치** — 즉 `ead5754` D1 시점("Linux TPM 브리지 한 단계 더, 그러나 플랫폼 종속이라 B/C 의 TPM 우위축이 더 무겁다")의 *연동 복잡도 비대칭이 실측에서 TPM 불리 방향으로 더 커졌다*(Reviewer 직접 검증 확정). 두 번째 무게 발견은 **Agent B·C 가 서로 다른 입구로 "touch-to-sign(자동 서명 차단)을 수단 무관 비협상 하한선으로 격상"에 수렴** — H-1(standing root-동치)은 O-1/O-2(구조적 분리)로도 owner 경로·완전 침해를 못 막으므로, 자동 서명 차단이 host 완전 침해 시 *유일* 잔존 방어다. 세 번째는 **Agent A·C 수렴 "H-1↔H-2 는 동일한 '서명 능력의 root-동치 귀속' 문제의 두 발현 → 단일 결정으로 묶여야"**(tss 부여 대상 = docker group 미소속 분리 서명 사용자). 본 합의 = **추론적 검증(권고) 한정 — 수단 결정·brief 수정 발효·실 구성·commit·push 는 사용자 명시 + 별도 단계.**

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3 Agent 모두)

| # | 합의 항목 | A | B | C |
|---|----------|---|---|---|
| C1 | **판정 = APPROVE WITH CONDITIONS** (발효 진입·검토 단계 적격, 결정 고정 전 조건) | ✅ | ✅ | ✅ |
| C2 | **H-1 을 "수단 결정 *이전* 선결"로 격상 = 정확·가장 중요** (없었으면 거짓 안전감 시발점) | ✅ (핵심1) | ✅ (핵심1) | ✅ (함의) |
| C3 | **TPM 비추출성 유지 ≠ 서명 *능력* 탈취 차단** — root-동치 계정이 PKCS#11/agent/signing 도달 | ✅ (A-2) | ✅ (R-2) | ✅ (C-2) |
| C4 | **citation stale 0** (CD-*/IB-2/§7.4 전수 실재, CP-10 메타 답습 효과) | ✅ (전수) | ✅ (전수) | (반박 0) |
| C5 | **owner self-bypass(IB-2) 4축 잔존** — single-host 1인 = 같은 사람 두 계정 제어 | ✅ (R-3) | ✅ (B-3) | ✅ (C-4) |
| C6 | **두 brief 모두 실 변경 0건·발효 0건·금지 답습 정확** | ✅ | ✅ | ✅ |

### 1.2 부분 일치 (Partial — 2 동의, 1 강조/추가)

| # | 항목 | 분류 |
|---|------|------|
| P1 ⭐ | **H-1↔H-2 단일 결정 결합** (tss 부여 = docker 미소속 분리 서명 사용자) — 따로 결정 시 hole | **A 강하게(A-2 핵심) + C 동형(C-3 O-5)** 독립 수렴 / B 동의(R-3) |
| P2 ⭐ | **touch-to-sign(자동 서명 차단) = 수단 무관 비협상 하한선 격상** | **B 강하게(B-2 O-2+O-4 최강) + C 강하게(C-2 핵심2)** 독립 수렴 / A 미언급 |
| P3 | **해소 옵션 보안 강도 순위 필요** (O-2 구조분리 > O-1 권한강등 ≈ O-4 자동서명차단 > O-3 감사) | B(B-2) + C(C-3 O-5 추가) / A(R-4 O-1 재검증 부담) |

### 1.3 불일치 (Divergence)

| # | 항목 | A | B | C | Reviewer |
|---|------|---|---|---|----------|
| D1 ⭐ | **TPM 1순위 권고 유지 vs host 실측 반영 재평가** | TPM 경로 *함정* 지적(A-1: ssh-agent socket 필수·CD-3 결합) + ssh-tpm-agent 대안 제시 — **순위 변경은 안 함, 경로 보강** | TPM 1순위 자체 이견 없음 (백업키 0개 우위 인정) | **host 실측이 D1 연동단순성 역전 → TPM 1순위 자동 답습 금지·대칭 병치·D1 재평가** (C-1 핵심1) | **C-1 = 사실 확인됨**(Reviewer 직접 검증: ssh-sk-helper 실재 264KB + libfido2 1.14.0 설치 + TPM 브리지 0개). 단 **해소 = "YubiKey 1순위 flip" 아님** — (i) A 의 TPM 경로 함정(A-1)·B 의 TPM 백업키 0개 우위는 *여전히 유효*, (ii) C-5 자신이 "CD-8 추상 인터페이스 채택 시 PL/순위 차이 대부분 상쇄"라 함, (iii) P2(touch-to-sign 비협상)가 순위를 *직교화*. → **CMA-1 = "TPM 1순위 자동 답습 금지 + TPM vs YubiKey *대칭 병치* + host 실측 반영 D1 재평가 명문" (brief 수정 조건). 수단 *결정* 자체는 풀 3+1·사용자 명시로 보류 — 본 합의가 순위를 flip 하지 않음**(조기 수단 고정 편향 차단, C 자기원칙) |

### 1.4 누락 (Gap — 단독 발견, Reviewer 중요도)

| # | 항목 | 언급 | 중요도 | 처리 |
|---|------|-----|-------|------|
| N-A1 ⭐ | **TPM→git commit 서명 경로 분기** = (a) git SSH 서명은 PKCS#11 직접 미수용 → ssh-agent + PKCS#11 provider 등록 = *상시 agent socket*(H-1/CD-3 탈취 표면) / (b) ssh-tpm-agent 가 더 직접적. 경로 선택이 곧 agent socket 표면·CD-8 설계 좌우 | A | **높음** (구현 결정적) | **CMA-4** |
| N-B1 ⭐ | **H-1 위협 강도 = "docker run -v 한 줄"보다 넓음** — delangi 로 실행되는 *임의 코드*(LLM 생성 스크립트·공급망 트로이)가 *별도 exploit 없이* standing root-동치 = BI-3 신뢰모델(에이전트=경계 밖) 기반 무효화 | B | **높음** (위협 인식) | **CMA-5** |
| N-B2 ⭐ | **백업키 0개의 *대가* = `allowed_signers`/fingerprint allow-list 갱신이 새 owner-쓰기 경로** = BI-1 self-bypass·CP-1 owner 경로와 *동일 표면*. 표면을 백업키→갱신경로로 *이동*. revoke-before-register 윈도우 | B | **높음** (거짓 안전감) | **CMA-6** |
| N-B3 | **credential 부분 격리 면책 라벨 부재** (BI-7 동형) — "TPM 구성했으나 H-1 미해소/touch 미설정" 중간 상태 = "서명능력 차단 보장 0" 능동 차단 장치 부재 | B | 중-높음 | **CMA-7** |
| N-C1 | **O-5 = delangi docker 유지 + 별도 비특권 서명 사용자에게만 tss + docker 미소속** — 전환 비용 0(rootless 불필요) + 구조적 분리 + H-2 동시 해결 | C | **높음** | 권고 R-1 (H-1 brief §2 표 추가) |
| N-C2 | **CP-7 gitsign = credential 의 *유일 예외*** (gitsign 도 OIDC 토큰 격리 필요 → CP-4 안 닫힘) → "Sigstore 도입 = credential 해결" 거짓 안전감 trigger 보존 | C | 중-높음 | 권고 R-2 |
| N-C3 | **PL 우위 = 수단 순위 아니라 추상 인터페이스(CD-8) 여부가 결정** — TPM vs YubiKey PL 차이 대부분 상쇄 (D1 압력 ↓) | C | 중-높음 | 권고 R-3 (CMA-1 보강) |
| N-A2 | **Signer/Verifier 책무 분리** — CI 는 서명 키 아닌 fingerprint *대조*(allow-list, BI-1) = `Verifier` 책무. 인터페이스가 서명/검증 분리해야 CD-8 교체 안 깨짐 | A | 중 | 권고 R-4 |
| N-A3 | **PEN-5 시연이 S-0 미발효 시 *반드시* FAIL** → S-0(H-1 해소)가 S-6(PoC) 선결임이 PoC 레벨에서 강제 (brief 순서 정합) | A | 중 | 권고 R-5 |
| N-B4 | touch 사회공학 잔여(host 침해자가 정당 서명 위장해 터치 유도) / O-3 audit 가치 BI-5 cross-ref / BI1C-4 cross-축 출처 부록 A 추가 | B | 중 | 권고 R-6~R-8 |

---

## 2. 합의 도출 — 발효 선결 BLOCKING 통합 (CMA-1~7)

> 세 Agent BLOCKING(A 2 + B 4 + C 2 = 8) 중복 제거 + Reviewer 격상 = **7건**. **우선순위: CMA-1(순위 재평가) > CMA-2(touch-to-sign 하한선) > CMA-3(H-1↔H-2 단일결정) > CMA-5(H-1 위협강도) > CMA-6(백업키 대가) > CMA-4(서명경로 분기) > CMA-7(면책 라벨).**

| # | BLOCKING | 출처 | 우선 |
|---|----------|------|------|
| **CMA-1** ⭐ | **TPM 1순위 *자동 답습* 금지 + TPM vs YubiKey *대칭 병치* + host 실측 반영 D1 재평가 명문** (시나리오 A: TPM 유지 근거=백업키 0개·PL / 시나리오 B: YubiKey 승격 근거=미들웨어 0단계·H-1 하 touch 즉시 가치). ⚠️ **본 합의가 순위를 flip 하지 않음** — 결정 = 풀 3+1·사용자 명시. 조기 수단 고정 편향 차단 | D1 (C-1 + Reviewer 검증) | **1** |
| **CMA-2** ⭐ | **touch-to-sign(자동 서명 차단) = 수단 무관 비협상 하한선 격상** (CD-3 동층위). TPM 택하면 PIN+presence policy 의무 / YubiKey 택하면 touch=always 의무 + PIN 캐시 비활성. H-1 완전 침해 시 *유일* 잔존 방어. 수단 순위(CMA-1)와 *직교* | P2 (B-2 + C-2 수렴) | **1** |
| **CMA-3** ⭐ | **H-1↔H-2 단일 결정** — tss group 부여 = **docker group 미소속 분리 서명 사용자에게만**(O-2/O-5), delangi/Hermes 컨테이너 제외. tss 를 root-동치 계정(delangi)에 주면 O-2 해소 효과 무효. "서명 능력을 docker-privileged 계정에서 구조적 분리" = 하나의 결정 | P1 (A-2 + C-3 + B R-3 수렴) | **1** |
| **CMA-4** | **TPM 서명 경로 분기 명시** — (a) PKCS#11+ssh-agent(상시 agent socket = H-1/CD-3 탈취 표면) vs (b) ssh-tpm-agent(더 직접적). S-3 을 "tpm2-pkcs11 고정"→"TPM 서명 경로 *선택*"으로 일반화(CD-8 실 입력). "PoC 실시"가 *어느 경로* 입증인지 명시(CP-2 라벨화 차단) | N-A1 (A 단독) | 2 |
| **CMA-5** | **H-1 위협 강도 보강** — escape = delangi 로 실행되는 *임의 코드*(LLM 생성·공급망 트로이)가 별도 exploit 없이 standing root-동치 = BI-3 신뢰모델 기반 무효화. H-1 brief §1.2 + credential §3.2 (a) 를 "delangi 세션 임의 프로세스 → docker API host root → PKCS#11/agent 도달" 2단 경로로 확장 | N-B1 (B 단독) | 2 |
| **CMA-6** | **백업키 0개의 대가 명세** — `allowed_signers`/fingerprint allow-list 갱신 = R-I-CONFIG-CHANGE T3 경유 + 그 갱신이 BI-1 self-bypass·CP-1 owner 경로와 동일 표면(anchor/audit 가 기록·검증) + revoke-before-register 윈도우 = Rollback Trigger(CD-CBI-3). 표면을 백업키→갱신경로 *이동* 가시화 | N-B2 (B 단독) | 2 |
| **CMA-7** | **credential 부분 격리 면책 라벨**(BI-7 동형) — "TPM 키 생성 ≠ 격리 충족. H-1 미해소 또는 touch policy 미설정 또는 PEN-1~8 미통과 = '서명능력 차단 보장 0'". 중간 상태 거짓 안전감 능동 차단 | N-B3 (B 단독) | 3 |

---

## 3. 권고 항목 (비차단)

| # | 권고 | 출처 |
|---|------|------|
| R-1 | **O-5 행 추가** (H-1 brief §2): delangi docker 유지 + 별도 비특권 서명 사용자에게만 tss + docker 미소속 = 전환 비용 0 + 구조적 분리 + H-2 동시 해결 | N-C1 (C) |
| R-2 | **CP-7 gitsign credential 예외 trigger** (credential §6): "Sigstore 도입해도 credential CP-4 못 닫음 — credential 발효는 Sigstore 경로와 직교 선결" 1줄 | N-C2 (C) |
| R-3 | **PL 우위 = 추상 인터페이스(CD-8) 여부가 결정** — TPM vs YubiKey PL 차이 대부분 상쇄, D1 압력 ↓ (CMA-1 보강) | N-C3 (C) |
| R-4 | **Signer/Verifier 책무 분리** — CI = fingerprint 대조 = `Verifier`, host = 서명 = `Signer`. CD-8 인터페이스가 두 책무 분리해야 교체 안 깨짐 | N-A2 (A) |
| R-5 | **PEN-5 = S-0 미발효 시 반드시 FAIL** 명문 — S-0 발효(PEN-5 통과)가 S-1 수단 결정 entry (brief 순서 PoC 레벨 강제) | N-A3 (A) |
| R-6 | touch 사회공학 잔여(host 침해자 정당 서명 위장 터치 유도) = §6 잔여 명문 | N-B4 (B) |
| R-7 | O-3 sudo = 차단 아닌 *기록* 수단 → BI-5 audit 축 cross-ref | N-B4 (B) |
| R-8 | BI1C-4 (d)(e) cross-축 인용 출처 = 부록 A 에 BI-1 합의(`4c5f5f4`) 추가 | N-B4 (B) |
| R-9 | 재생성 SOP lock-out 정량화 + SOP 실 단계 문서화 (host 디스크 교체/재설치 시도 재생성) | A R-3 |
| R-10 | 단계적 채택(CD-8 c) 순서 = CMA-2 격상 시 "자동 서명 차단을 *처음부터*"로 재서술 (TPM PIN-policy 가 YubiKey 조달 리드타임 회피 경로일 수 있음) | C-6 |

---

## 4. 거짓 안전감 차단 (Reviewer 격상)

본 합의의 가장 위험한 실패 양식 3가지: (i) **"수단 결정·발효 = 격리 확정"** — CMA-7(부분 격리 면책 라벨)·CMA-5(H-1 위협 강도)로 차단. TPM 키 생성·구성은 H-1 미해소·touch 미설정 시 "서명능력 차단 보장 0". (ii) **"백업키 0개 = 안전"** — CMA-6: 표면이 백업키에서 *갱신 경로*(`allowed_signers`)로 *이동*했을 뿐, 그 갱신이 BI-1 self-bypass·CP-1 owner 경로와 동일 표면. (iii) **"TPM 1순위 답습 = 검증된 결정"** — CMA-1: host 실측이 D1 을 역전시켰으므로 *대칭 병치 후 재결정*. ⭐ **owner self-bypass(IB-2) 잔존 = 수단 무관**: O-1/O-2 도 *비의도 침투* 경로만 닫고 owner(같은 사람) 경로는 MVP-6(Rekor) 전까지 수용된 SPOF. **"수단 발효 = 에이전트/원격 경로 차단, owner SPOF 수용 결정"** (IB-2). 자기검증 금지(Hermes ≠ root) — 격리 검증은 PEN-1~8 binary(Hermes 권한 밖).

---

## 5. 미해소 쟁점 / 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (A) | 두 brief 를 CMA-1~7 + 권고 R-1~10 반영하여 **v2 수정** (brief 본문 반영, 결정·발효 0건) | brief 수정 |
| (B) | **S-0 발효** — H-1 해소(O-1 rootless / O-2·O-5 서명 사용자 분리) 실 변경 (수단 결정 *이전*, 별도 승인) | 발효 |
| (C) | **수단 결정 고정** — ⚠️ CMA-1(대칭 병치·D1 재평가) + CMA-3(H-1↔H-2) 미반영 상태 비권고. 반영 후 풀 3+1 재확인 | 발효 (보류) |
| (D) | 합의 보고서 commit + push (현 미실시) | 메타 |
| (E) | 세션 종료 | 메타 |

- ⭐ **권고 순서**: (A) brief v2 수정 → (B) S-0 발효(PEN-5 통과) → (C) 수단 결정 고정(대칭 병치 재평가 + H-1↔H-2 단일 결정). CMA-1~3 가 수단 결정의 *직접 선결*.
- **수단 *결정* 은 본 합의가 내리지 않음** — TPM vs YubiKey 는 CMA-1 대칭 병치 + 사용자 명시 권한.

---

## 6. 합의 한 문단 요약

**Credential 수단 발효 entry brief + H-1 해소 검토 = APPROVE WITH CONDITIONS** 이다. 세 Agent 는 (1) H-1(docker group hole)을 수단 결정 *이전* 선결로 격상한 것이 정확·가장 중요, (2) TPM 비추출성 유지 ≠ 서명 능력 탈취 차단, (3) citation stale 0(CP-10 메타 답습 효과), (4) owner self-bypass(IB-2) 4축 잔존 에 일치했다. 가장 무게 있는 발견은 **Agent C 가 host 실측으로 `ead5754` D1 추론을 역전**시킨 것 — YubiKey `sk-` host-side 스택(`ssh-sk-helper` 264KB·`libfido2 1.14.0`·OpenSSH 9.6)은 이미 준비됐고 TPM 브리지(`tpm2-pkcs11`/`ssh-tpm-agent`)는 0개라, 연동 복잡도 비대칭이 TPM 불리 방향으로 실재(Reviewer 직접 검증 확정). 이어 **Agent B·C 가 "touch-to-sign(자동 서명 차단)을 수단 무관 비협상 하한선으로 격상"에 독립 수렴**(H-1 완전 침해 시 유일 잔존 방어), **Agent A·C 가 "H-1↔H-2 = 서명 능력의 root-동치 귀속 문제 두 발현 → tss 부여 = docker 미소속 분리 서명 사용자 단일 결정"에 수렴**했다. 발효(수단 결정 고정) 전 **BLOCKING 7**(CMA-1 순위 대칭 병치·D1 재평가 / CMA-2 touch-to-sign 비협상 하한선 / CMA-3 H-1↔H-2 단일결정 / CMA-4 서명경로 분기 / CMA-5 H-1 위협강도 / CMA-6 백업키 0개 대가=갱신경로 표면 이동 / CMA-7 부분격리 면책 라벨) + 권고 10이며, **본 합의는 수단 순위를 flip 하지 않고**(조기 수단 고정 편향 차단) 대칭 병치 후 풀 3+1·사용자 명시로 결정을 보류한다. 교차 = 일치 6 / 부분 3 / 불일치 1(D1, 사실 확인됨·해소=대칭 병치) / 누락 11. 거짓 안전감 차단(수단 결정 ≠ 격리 확정·백업키 0개 ≠ 안전·TPM 답습 ≠ 검증)을 Reviewer 격상했다. 본 합의는 추론적 검증(권고) 한정 — 수단 *결정 고정*·tpm2-pkcs11 설치·tss/docker group 변경·rootless 전환·서명 키 생성·brief 수정 발효·PoC 실 실행·commit·push 는 사용자 명시 + 별도 단계이며, **본 보고서 외 어떤 파일도 편집/생성하지 않고 commit/push 0건**이다.

---

## 7. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | APPROVE w/ COND. citation stale 0 + host 사실 정확. BLOCKING 2: **A-1 TPM 서명 경로 분기**(PKCS#11+ssh-agent socket vs ssh-tpm-agent, CD-3 결합) / **A-2 H-1↔H-2 단일 결정**(tss = O-2 분리 사용자). 핵심 = 서명 능력의 root-동치 귀속 + 경로 분기가 agent socket 표면 결정 |
| **Agent B** (보안) | "안전하고 견고한가?" | APPROVE w/ COND. BLOCKING 4: **B-1 H-1 위협 과소평가**(임의 코드 standing root-동치) / **B-2 옵션 보안강도 순위·O-2+O-4 최강** / **B-3 백업키 0개 대가=갱신경로 표면 이동** / **B-4 부분격리 면책 라벨**. 핵심 = H-1 = BI-3 신뢰모델 기반 무효화 |
| **Agent C** (대안) | "더 나은 방법?" | APPROVE w/ COND. BLOCKING 2: **C-1 host 실측 D1 역전**(YubiKey 미들웨어 ready·TPM 브리지 0 → 대칭 병치) / **C-2 touch-to-sign 비협상 하한선 격상**. 권고 O-5·CP-7 trigger·PL=추상화 결정. 핵심 = TPM 1순위 근거 한 축 역전 + touch-to-sign 이 H-1 핵심 안전 변수 |
| **Reviewer** | "최선의 합의는?" | 교차(일치 6 / 부분 3 / 불일치 1 / 누락 11) + C-1 직접 검증(사실 확인) + B·C 수렴(touch-to-sign) + A·C 수렴(H-1↔H-2) = **BLOCKING 7(CMA-1~7) 통합 + 거짓 안전감 차단 격상 + 수단 순위 flip 거부(대칭 병치 보류)**. **APPROVE WITH CONDITIONS** |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**수단 결정 *고정*(TPM/YubiKey 최종 확정)** / **tpm2-pkcs11·ssh-tpm-agent·libfido2 추가 등 설치** / **tss group 추가·docker group 변경·rootless docker 전환·udev rule** / **서명 사용자 생성·분리 실행** / **TPM/YubiKey 서명 키 생성·`allowed_signers` 작성·git 서명 구성**(`gpg.format`/`commit.gpgsign`) / env scrub·`cap_drop`·docker secret·entrypoint stat 실 구성 / **BI-3 충족 PoC(E-1~11)·침투 시연(PEN-1~8) 실 실행** / **brief 본문 v2 수정 발효**(CMA-1~7 반영은 별도 승인) / 실 hook(pre-commit/pre-receive/CI provenance step) / GitHub ruleset·branch protection·CI workflow 변경 / filesystem ACL·`read_only` mount·audit sink 실 구성 / **sigstore·gitsign·Rekor 도입** / Hermes runtime·upstream 변경 / **Vault HSM ST-4**(γ-2 DEFER) / threshold 고정 / **Operational Readiness PASS**(Layer E) / **Hermes PMO 격상**(Layer F) / Implementation Evidence PASS / MVP-1 exit / Phase α defer-lockdown 변경 / **git history rewrite**(후속 74, SHA 붕괴) / G3·ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`/`ead5754`) 자동 정정** / Group I·α·β·γ 합의 본문 변경 / 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / tmux·Obsidian docs-scope 도입 / 외부 LLM 응답 강제 채택 / 합의 보고서 외 파일 작성 / **commit / push** / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
