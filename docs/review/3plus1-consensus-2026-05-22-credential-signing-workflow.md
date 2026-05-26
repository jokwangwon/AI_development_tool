# 3+1 합의 보고서 — Credential 서명 워크플로우 (W-1) brief

> **본 합의 = 추론적 검증(권고) 한정.** TPM 키 생성·tpm2-pkcs11 설치·sudoers·git 서명 구성·broker 구현·발효 = 0건. 실 결정/구현 = 사용자 명시 + 별도 단계.

---

**작성일**: 2026-05-22
**합의 형태**: 풀 3+1 (A 구현/정합 · B 보안 · C 대안 + Reviewer) — **의무** (서명 = T-trust-boundary 보안 + 핵심 제약 #1)
**합의 입력**: `docs/phase0/credential-signing-workflow-design-brief.md` (DRAFT v1, W-1~W-4)
**1차 권위 답습**: P-PRIV(AP-1~5) / credential 발효 합의(CMA-1~7) / `ead5754`(CD-6·CD-8) / [[project_minimize_user_intervention]]
**판정**: ⚠️ **REVISE** (A REVISE + B REVISE + C APPROVE WITH CONDITIONS) — **W-1 은 (i) 구현상 현 명세대로 동작하지 않고 (ii) 핵심 안전 주장(PIN backstop)이 root-동치 host 에서 거짓**. 조건 보강(APPROVE WITH CONDITIONS)이 아니라 워크플로우·선결 재설계 필요. **키 생성 *진입 금지* — 본 REVISE 해소 전 S-3 발효 중단.** **BLOCKING 8(SW-1~8) + 권고 6.**

---

## 0. 종합 판정 (한 문단)

세 Agent 중 **A·B 가 REVISE**(C 만 APPROVE WITH CONDITIONS)로, 종합 = **REVISE**. 이는 W-1 의 *방향*(좁은 helper·pattern A·W-2 비권고)이 틀려서가 아니라, **W-1 이 의존하는 단일 안전 주장과 구현 기반이 둘 다 무너졌기 때문**이다. 가장 무게 있는 발견은 **Agent B·C 가 독립 수렴한 "PIN backstop 은 root-동치 host 에서 backstop 이 아니다"** — delangi 가 `docker`(=root-동치) **+ `sudo` 그룹**(실측 `27(sudo)`) 둘 다 보유한 상태에서, root 는 (a) signer 서명 프로세스 **ptrace/메모리 scrape** 로 PIN 탈취 (b) **pinentry hook/키로깅** (c) **helper 교체**(`root:root` 도 root 가 수정) (d) tpm2-pkcs11 store·**`setuid(1001)` 직접** 으로 PIN 을 *자동* 무력화한다. **TPM+PIN 과 YubiKey 물리 터치의 본질 차이가 정확히 여기서 드러난다** — PIN 은 *메모리에 진입하는 비밀*이라 root 가 scrape 가능하나, 물리 터치는 *메모리에 진입하지 않는 인간 행위*라 불가하다. 즉 brief 는 합의 CMA-2 의 *결론*("backstop 존재")을 인용하면서 그 *전제*(touch=메모리 미진입)를 PIN(메모리 진입)으로 치환해 결론만 남겼다(거짓 안전감, AP-5). 두 번째 무게 발견은 **Agent A 단독의 "W-1 은 git 인터페이스와 두 군데 어긋난다"** — (i) `ssh-keygen -Y sign` 은 PKCS#11 키를 `-D provider` 로 직접 못 받아 **ssh-agent 필수**(W-1 이 "영속 socket 없음"으로 W-2 를 제친 근거 무효), (ii) git 은 서명 데이터를 **stdin 이 아니라 0600 delangi-소유 임시 *파일 경로***로 넘기고 `<buffer>.sig` 회수를 기대 → `sudo -u signer` helper 는 그 파일을 **읽지도 쓰지도 못함**(cross-user 단절). 세 번째는 **Agent C 단독의 "systemd socket activation broker(W-1.5) 누락"** — broker *패턴*(AP-2 4속성)을 커스텀 코드 없이 systemd 가 제공하므로 W-3 DEFER 근거("구현 비용 최대")가 미적용. ⭐ **전략 함의**: 이 REVISE 는 **수단(TPM)+O-5(delangi docker 유지)+W-1 조합이 서명 backstop 을 갖지 못함**을 드러낸다 → **fork: (a) H-1 *완전* 해소(delangi 를 docker *및* sudo 에서 분리)로 host-key 에 실 backstop 부여, 또는 (b) YubiKey 물리 터치(root 도 scrape 불가)로 수단 재고**(CMA-1 = flip 아닌 대칭 병치 재고). 본 합의 = 추론적 검증(권고) 한정.

---

## 1. 교차 비교

### 1.1 일치 (3 Agent 모두)

| # | 합의 항목 | A | B | C |
|---|----------|---|---|---|
| C1 | **PIN backstop 은 root-동치(delangi=docker+sudo) host 에서 무력** | ✅ (AR-d) | ✅ (B-1) | ✅ (C-2) |
| C2 | **TPM+PIN ≠ YubiKey 물리 터치** (PIN=메모리 진입·scrape 가능 / touch=미진입) = CMA-2 본질 | (정합) | ✅ (B-1 핵심) | ✅ (C-2 핵심) |
| C3 | **W-1 은 현 명세로 부족** — 키 생성 전 재설계 필요 | ✅ REVISE | ✅ REVISE | ✅ (조건) |
| C4 | **수단 재고 trigger** (재결정 아님 — CMA-1 flip 거부 답습) | (AR-d) | ✅ (B-2) | ✅ (C-2) |

### 1.2 부분 일치 (2 동의, 1 강조)

| # | 항목 | 분류 |
|---|------|------|
| P1 ⭐ | **PIN backstop 거짓** — root 무력화 경로 전수 | **B 강하게(5경로) + C 강하게(독립)** 수렴 / A(delangi sudo 보유 AR-d 로 보강) |
| P2 ⭐ | **systemd socket broker = sudoers 보다 좁은 표면 대안** (AR-3 답습) | C 강하게(C-1 W-1.5) + B(B-4 AR-3 언급) / A(AR-b W-3 재평가) |
| P3 | **재귀 닻(AR-4) 무효** — delangi=root 면 `root:root` helper 도 수정 | A(AR-d) + B(B-1 c, B-3) 수렴 |

### 1.3 불일치 (Divergence)

| # | 항목 | A | B | C | Reviewer |
|---|------|---|---|---|----------|
| D1 | **판정 강도** | REVISE | REVISE | APPROVE w/ COND | **REVISE 채택** — C 도 "PIN backstop 약함(C-2)·W-1.5 누락(C-1)"을 BLOCKING 으로 들었고, A 가 *구현 불능*(A-1/2/3)을, B 가 *안전 주장 거짓*(B-1)을 입증 → 조건 보강 범위 초과. C 의 APPROVE w/ COND 는 "방향은 맞다"는 평가이나 그 조건들이 W-1 골격 재작성을 요구하므로 실질 REVISE 와 수렴 |

### 1.4 누락 (단독 발견, Reviewer 중요도)

| # | 항목 | 언급 | 중요도 | 처리 |
|---|------|-----|-------|------|
| N-A1 ⭐ | **W-1 구현 불능 3건**: `ssh-keygen -Y sign` PKCS#11 = ssh-agent 필수(`-D` 없음) / git = file-path(stdin 아님)·`<buffer>.sig` / 0600 delangi 파일 = signer 미접근 | A | **높음(결정적)** | **SW-2** |
| N-C1 ⭐ | **systemd socket activation broker(W-1.5)** = W-2~W-3 사이 사각. SO_PEERCRED·lifecycle·`User=signer` 무료(systemd 255 실측) | C | **높음** | **SW-3** |
| N-C2 | **Provider Liquidity 미배선** — W-1 이 TPM/tpm2-pkcs11 hard-bind. `Signer` 추상 인터페이스(helper 호출 규약 고정·매체 교체) 부재 = CD-8/AR-6 CP-10 재발 | C | 중-높음 | **SW-7** |
| N-A2 | tpm2-pkcs11 = **미설치**(가용일 뿐) / CMA-4(서명 경로 분기) 답습 누락 / CMA-1(수단 보류) vs "TPM 확정" 충돌 / "물리 터치 아님" 출처 불명 | A·B | 중-높음 | **SW-6** |
| N-B1 | AP-5 PoC 종료조건 = **root 경로·중간 면책·owner self-bypass 누락** | B | 중-높음 | **SW-8** |
| N-C3 | W-4 squash-merge = 트리 무결성까지(각 commit provenance 아님) / lease 위치=broker 내부 TTL > ssh-agent 캐시 / AR-5 4축 일반화 | C | 중 | 권고 |

---

## 2. 발효 전 BLOCKING 통합 (SW-1~8)

> A 5(+AR) + B 5 + C 3 → 중복 제거 + Reviewer 격상 = **8건**. **우선: SW-1(PIN backstop 거짓) > SW-2(구현 불능) > SW-4(재귀 닻 무효) > SW-3(systemd broker) > SW-5(AP-4 재설계) > SW-6(사실/citation) > SW-7(PL) > SW-8(PoC).**

| # | BLOCKING | 출처 | 우선 |
|---|----------|------|------|
| **SW-1** ⭐⭐ | **PIN backstop 은 root-동치 host 에서 backstop 아님** — delangi=docker+sudo=root → ptrace/메모리 scrape·pinentry hook·helper 교체·setuid(1001) 로 PIN 자동 탈취. **TPM+PIN(메모리 진입) ≠ YubiKey 터치(미진입)**. brief line 58 backstop 단정 **삭제/재서술**. PIN→backstop 성립 조건 = **(i) H-1 *완전* 해소(delangi 를 docker *및* sudo 에서 분리) ∧ (ii) ptrace 차단(`Yama ptrace_scope`) 또는 (iii) 물리 터치(YubiKey)**. CMA-3(H-1↔H-2)을 워크플로우 안전 *선결*로 명시 | C1/P1 (B-1+C-2 수렴) | **1** |
| **SW-2** ⭐ | **W-1 구현 불능 3건**: (a) `ssh-keygen -Y sign` 은 PKCS#11 `-D provider` 미수용 → **ssh-agent 필수**(W-1 "영속 socket 없음" 근거 무효) (b) git = 서명 데이터 **0600 delangi 임시 *파일 경로*** 전달·`<buffer>.sig` 회수(stdin 아님 → AP-4 "stdin only" 전제 오류) (c) signer(uid 1001) = 0600 delangi 파일 **미접근** → cross-user 왕복 단절. W-1 = **delangi-wrapper(파일↔pipe 변환) + signer-helper + agent lifecycle 2~3계층** 필요 → W-3 broker 와 복잡도 격차 축소 | N-A1 (A 단독) | **1** |
| **SW-3** ⭐ | **systemd socket activation broker(W-1.5) = §1 표 추가** — broker 패턴(AP-2 SO_PEERCRED·lifecycle·`User=signer`)을 커스텀 코드 없이 systemd(255 실측) 제공. W-3 DEFER 근거("구현 비용 최대")는 *커스텀 broker 코드*에만 적용·socket activation 무관. **W-1 sudoers 표면 vs W-1.5 socket 표면 재평가** (argv 미노출 = AR-3) | N-C1 (C 단독) | 2 |
| **SW-4** | **재귀 닻(AR-4) 무효** — delangi = `sudo` *및* `docker` 보유(실측) → `root:root` helper·sudoers 도 수정 가능. AR-4("delangi≠root" 전제) 붕괴 = IB-2 owner self-bypass 의 credential 인스턴스. 닻 성립 = SW-1 (i) H-1 완전 해소 전제 | P3 (A AR-d + B-1c) | **1** |
| **SW-5** | **AP-4 escape-equivalence 재설계** — (a) helper *교체* 위협(SW-1/SW-4) (b) **서명 *대상* 제약**(commit object 형식 검증 — 임의 내용 정당 서명 차단) (c) sudoers `env_reset`·`secure_path`·env 화이트리스트(LD_PRELOAD/SSH_ASKPASS 누수) (d) `/usr/local/bin/hermes-sign` + 부모 디렉토리 = `root:root`·group/other 쓰기 0·TOCTOU + sudo 바이너리 CVE 표면. "stdin only" → "고정 prefix argv + 가변 경로 canonical 검증"(SW-2 반영) | B-3+B-4 + A-2 | 2 |
| **SW-6** | **사실/citation 정정**: (a) tpm2-pkcs11 = **미설치**(가용일 뿐, dpkg 0·`.so` 0) → 머리말 "확정" 오류 (b) **CMA-4(서명 경로 분기)** 답습 누락 — W-1 이 W-2 agent socket 재도입하는지 미해소 (c) **CMA-1(수단 결정 보류)** vs brief "TPM 2.0 확정" 충돌 (d) "TPM CMA-2=물리 터치 아님" 출처(사용자 명시? consensus?) 명시 | N-A2 (A+B) | 2 |
| **SW-7** | **Provider Liquidity — `Signer` 추상 인터페이스** (CD-8/AR-6). helper 호출 규약(stdin 서명데이터·stdout 서명·exit) 고정 ⊥ 내부 매체(tpm2-pkcs11/sk-ssh/keyless) 교체 가능. `gpg.ssh.program`=git↔helper 배선이지 매체 결정 아님. broker 축 미적용 = CP-10 재발 | N-C2 (C 단독) | 3 |
| **SW-8** | **AP-5 PoC 종료조건 확장** — (a) **root 경로 PoC**(root 가 ptrace/helper 교체/setuid 로 PIN 없이 서명 → 차단 통과는 SW-1 (i) 선결, 미해소 시 *반드시 FAIL* = R-5/PEN-5 동형) (b) **CMA-7 중간 상태 면책 라벨**("helper 설치·H-1 미해소" = 보장 0) (c) owner self-bypass(IB-2) 수용 SPOF 명문 | N-B1 (B 단독) | 3 |

---

## 3. 권고 항목 (비차단)

| # | 권고 | 출처 |
|---|------|------|
| R-1 | **lease(AP-3) 위치 = broker 내부 TTL > ssh-agent 캐시**(W-2 약점 재현 회피). H-1 잔존 하 PIN 캐시 = scrape 윈도우 확대 = 비권고. FIDO2 cached presence = YubiKey 채택 시 자연 구현 | C R-1 + B R-4 |
| R-2 | **W-4 빈도 축소**: squash-merge 단일 서명 = 트리 무결성까지(각 commit provenance 아님). 비서명 commit = BI-1 fingerprint 판정 입력 부재 → audit(BI-5) 사후 대조만. **MVP=전 commit 서명 시작 권고 정확** | C R-2 |
| R-3 | 동기 서명(W-1, present-time 사람 의도=CMA-2 전제) 유지. hook 서명 = `.git/hooks` 재귀 표면(AP-1 T). CI 서명=keyless=CMA-2 상실(비권고) | C R-3 |
| R-4 | CMA-6 revoke-before-register 윈도우 + `allowed_signers` 갱신 = BI-1 self-bypass·CP-1 owner 경로 동일 표면 (brief line 70 보강) | B R-1 |
| R-5 | AR-5 4축 일반화 — 본 워크플로우 패턴(helper/socket broker)을 anchor·audit 권한 작업에 재사용 명문(DRY·CP-10 차단) | C R-5 |
| R-6 | `git verify-commit` = allowed_signers 공개키 검증·signer fingerprint = BI-1 판정 입력(author≠판정, 정합) §3 명문 | A AR-a |

---

## 4. ⭐ 전략 함의 — 수단/H-1 fork (Reviewer 격상, 사용자 결정)

본 REVISE 의 근본 원인 = **수단(TPM PIN) + O-5(delangi docker 유지) + delangi sudo 보유** 가 함께 **서명 backstop 을 무효화**. 워크플로우(W-1)는 이를 우회 못 함. 해소 fork (CMA-1 = 수단 flip 거부·대칭 병치 답습, 사용자 명시 권한):

| 경로 | 내용 | trade-off |
|----|----|----|
| **(A) H-1 *완전* 해소** | delangi 를 docker **및** sudo 에서 분리(별도 admin 계정) + ptrace 차단(`Yama=2`) → TPM+PIN 이 실 backstop | 라이브 oracle-game 스택·일상 sudo 워크플로우 영향(O-5 가 피하려던 것) — O-5 의 "delangi docker 유지" 전제와 충돌 |
| **(B) YubiKey 물리 터치** | 수단 = YubiKey `sk-`(host-side ready, CMA-1 host 실측 우위) → 터치=메모리 미진입 → root 도 자동 서명 불가 | 토큰 조달 + 백업키 2개. **delangi 가 docker/sudo 유지해도 backstop 성립**(터치 scrape 불가) |
| **(C) 둘 다(defense-in-depth)** | H-1 해소 + YubiKey | 최강, 비용 최대 |

- ⭐ **관찰**: **(B) YubiKey 가 O-5(delangi docker 유지)와 *양립***한다 — 물리 터치는 root 가 scrape 못 하므로 delangi 가 root-동치여도 backstop 유지. 반면 (A)는 O-5 를 사실상 철회(delangi docker/sudo 제거). 즉 **"개입 최소화 + delangi 편의 유지"([[project_minimize_user_intervention]])를 살리려면 (B) YubiKey 가 (A)보다 정합적**. 이는 합의 CMA-1 의 "host 실측 YubiKey 우위"를 워크플로우 층위에서 *재확인*(C-2/B-1).

---

## 5. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 |
|----|----|
| (A) | **수단/H-1 fork 결정** (§4 — YubiKey 재고 / H-1 완전 해소 / 둘 다) → 그에 맞춰 워크플로우 brief v2 |
| (B) | brief 를 SW-1~8 반영 v2 (현 TPM 유지 시 SW-1 (i) H-1 완전 해소 선결 명시) |
| (C) | systemd socket broker(W-1.5) 중심 재설계 |
| (D) | 합의 보고서 commit |
| (E) | 세션 종료 |

- ⚠️ **키 생성·S-3 발효 = 본 REVISE(특히 SW-1) 해소 전 *진입 금지***. S-0+S-2(signer+tss)는 유효·무해(어느 수단이든 재사용).
- 권고: **(A) fork 결정 먼저** — 수단/H-1 이 워크플로우 전체를 좌우(키 생성 전 확정이 재작업 방지).

---

## 6. 합의 한 문단 요약

**Credential 서명 워크플로우 W-1 = REVISE** (A·B REVISE + C 조건부). W-1 은 (i) **구현 불능**(ssh-keygen -Y sign=PKCS#11 ssh-agent 필수·git=0600 delangi 파일 전달·signer 미접근, A-1/2/3) (ii) **핵심 안전 주장 거짓**(PIN backstop 은 delangi=docker+sudo=root-동치 host 에서 ptrace/scrape/helper교체/setuid 로 무력, B-1·C-2 수렴). **TPM+PIN(메모리 진입) ≠ YubiKey 터치(미진입)** 가 합의 CMA-2(touch=유일 방어)를 워크플로우 층위에서 재확인. 추가: **systemd socket broker(W-1.5) 누락**(C-1, broker 패턴 MVP 비용 제공) / **재귀 닻(AR-4) 무효**(delangi sudo 보유) / Provider Liquidity `Signer` 추상 미배선(C-3) / 사실 오류(tpm2-pkcs11 미설치·CMA-4 누락·CMA-1 충돌). 발효 전 **BLOCKING 8(SW-1~8)** + 권고 6. ⭐ **전략 fork(§4)**: 수단(TPM)+O-5(delangi docker 유지)가 backstop 무효화 → **(B) YubiKey(터치=root scrape 불가, O-5 와 양립) 또는 (A) H-1 완전 해소(delangi docker+sudo 분리, O-5 철회)**. **(B) 가 개입 최소화·delangi 편의 유지와 정합** = CMA-1 host 실측 YubiKey 우위 재확인. 교차 = 일치 4 / 부분 3 / 불일치 1(판정 강도→REVISE) / 누락 6. **키 생성·S-3 = SW-1 해소 전 진입 금지**(S-0+S-2 는 유효). 본 합의 = 추론적 검증(권고) 한정 — 수단/H-1 결정·구현·commit = 사용자 명시 + 별도 단계, **본 보고서 외 파일 미편집·commit/push 0건**.

---

## 7. 풀 3+1 관점 분배

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **A** (구현/정합) | "동작하는가?" | **REVISE**. SW-2: ssh-keygen -Y sign=ssh-agent 필수 / git=file-path(stdin 아님) / 0600 cross-user 단절. SW-6: tpm2-pkcs11 미설치·CMA-4 누락. AR-d: delangi sudo 보유=재귀 닻 무효. citation stale 0 |
| **B** (보안) | "안전한가?" | **REVISE**. SW-1⭐: PIN backstop 거짓(root 5경로 무력화)·TPM+PIN≠터치(메모리 진입). SW-5 AP-4 helper 교체·서명대상. SW-8 PoC root 경로. CMA-1/2 충돌 |
| **C** (대안) | "더 나은 방법?" | **APPROVE w/ COND**. SW-3⭐: systemd socket broker(W-1.5). SW-1 재확인(PIN 약함→수단 재고). SW-7: Signer 추상(PL). W-4·lease·4축 일반화 |
| **Reviewer** | "최선의 합의는?" | A 구현불능 + B 안전거짓 + C 조건 = **REVISE**. **전략 fork(§4): YubiKey(O-5 양립) vs H-1 완전 해소**. 키 생성 진입 금지. BLOCKING 8 + 권고 6 |

---

## 부록 — 금지 (영구 답습)

TPM/YubiKey 키 생성 / tpm2-pkcs11·opensc 설치 / helper·wrapper·broker·systemd unit 작성 / sudoers·`/etc/sudoers.d/` 변경 / git 서명 구성 / `allowed_signers` 작성 / **delangi docker/sudo 분리 발효**(§4 (A) = 별도 결정·발효) / YubiKey 조달·수단 재결정 발효 / PIN 캐시·lease 구성 / S-3 이후 발효 / sigstore·gitsign·Rekor / Operational Readiness PASS / Hermes PMO 격상 / Vault ST-4 / git history rewrite / 합의·brief 본문 자동 갱신 / 원 합의(`ead5754`/credential 발효 합의) 자동 정정 / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화.
