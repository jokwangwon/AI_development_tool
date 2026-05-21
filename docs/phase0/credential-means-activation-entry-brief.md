# Credential 수단 *발효* entry brief — host OS 확인 결과 + 수단 결정 권고 + 백업키 정책 검토 (DRAFT v2)

> **본 brief = 4축 통합 정리 §7.4 권고 진입 경로 step (1) "credential 수단 발효 (host OS 확인 → TPM/SE/M2 결정)"의 *진입 brief* 한정.** 본 brief 의 어떤 §도 그 자체로 수단 *결정 고정*·TPM/YubiKey key 채택 *결정*·credential isolation 실 구성(tpm2-pkcs11 설치·key 생성·tss group 변경·env scrub·cap_drop·docker secret)·실 hook/CI/ruleset·BI-3 충족 PoC(E-1~11)·침투 시연(PEN-1~8) 실 실행·Operational Readiness PASS·Hermes PMO 격상 을 발생시키지 않는다. 본 brief = **host OS 사실 확인 결과 + CD-1~10 답습 매핑 + 새 발효 선결 식별 + 수단 결정 *권고* + 백업키 정책 *검토* + binary PoC 매핑** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1, R-I-IMPL-BOUNDARY) → commit → push → (별도) 수단 결정 고정·실 구성**.

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (v1 + credential 수단 발효 풀 3+1 합의 `3plus1-consensus-2026-05-21-credential-means-activation.md` BLOCKING CMA-1~7 + 권고 R-1~10 반영 — 본문 반영, 수단 결정·발효 0건)
**진입 단위**: Group I 구현 entry 합의 후속 #B — **credential 수단 발효 (P-1)** = 4축 통합 정리 §7.4 권고 진입 경로 **(1) credential** 첫 단계

## v2 변경 이력 (풀 3+1 합의 CMA-1~7 + R-1~10 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **CMA-1** ⭐ (TPM 1순위 자동 답습 금지 + TPM vs YubiKey 대칭 병치 + host 실측 D1 역전) | §1.1 YubiKey 행 + §1.2 + §2.1 + §3.1 (시나리오 A/B 대칭 병치, 순위 flip 0건) |
| **CMA-2** ⭐ (touch-to-sign = 수단 무관 비협상 하한선) | §3.1 — "자동 서명 차단" 행 신설(CD-3 동층위) + §3.2 |
| **CMA-3** ⭐ (H-1↔H-2 단일 결정 = tss 부여 = docker 미소속 분리 서명 사용자) | §3.2 + §7 S-0/S-2 (단일 결정 결합) |
| **CMA-4** (TPM 서명 경로 분기 = PKCS#11+ssh-agent vs ssh-tpm-agent) | §1.3 H-3 + §5 (경로 선택 = agent socket 표면) |
| **CMA-5** (H-1 위협 강도 = 임의 코드 standing root-동치) | §3.2 (2단 경로 확장) |
| **CMA-6** (백업키 0개의 대가 = `allowed_signers` 갱신 = BI-1 self-bypass 표면) | §4.2 (표면 이동 명세) |
| **CMA-7** (credential 부분 격리 면책 라벨) | §3.2 + §5 (중간 상태 "차단 보장 0") |
| R-2 (CP-7 gitsign credential 예외) | §6 |
| R-3 (PL 우위 = 추상 인터페이스가 결정) | §3.1 결정 구조 행 |
| R-4 (Signer/Verifier 책무 분리) / R-5 (PEN-5=S-0 선결) | §5 + §7 |
| R-8 (BI1C-4 cross-축 출처) | 부록 A (BI-1 합의 `4c5f5f4` 추가) |
**선행 발효 답습**: `f303087` 후속 77(4축 통합 정리 §7.4 권고 진입 경로 + IB-1~4) + `ead5754` 후속 72(BI-3 credential 수단 결정 합의 — CD-1~10) + `bf42d0e` 후속 71(BI-3 격리 brief) + `f29c772`/`8e57f7b` Group I 구현 entry 합의 + `708bc0e` G3 4축 DESIGN
**답습 입력 (1차 권위)**: **`ead5754` BI-3 수단 결정 합의 CD-1~10 + 조건부 CD-CBI-1~3** + 4축 통합 정리 brief §6 수단표·§7.2 P-1/P-5·§7.4 readiness 판정·IB-2 owner self-bypass 잔존 + GP-3 §5 + γ-1(ST-1)·γ-2(ST-4 DEFER) + ADR-011 §2.1 means/ends
**합의 권위 한계**: 본 brief = *발효 진입 brief* DRAFT — 수단 *결정 고정*·실 구성·BI-3 충족 PoC 실 실행 은 별도 단계(풀 3+1 합의 + 사용자 명시). **본 brief 는 "어떤 수단을 결정하면 되는가/무엇이 새로 선결인가/백업키는 어떻게 가는가"를 *정리·권고* 할 뿐 수단을 *고정* 하거나 *구성* 하지 않는다.**

---

## 0. 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "credential 수단 발효로 진행해줘. 먼저 실제 host OS 확인해서 TPM/Secure Enclave/YubiKey 중 가능한 걸 보고, 그 다음 수단 결정 + 백업키 정책 검토. 단 4축 통합 정리 §7.4 권고 진입 경로 답습."

본 brief = 위 명령 답습 — **(i) host OS 확인 결과 (실 read-only 점검 완료)** + (ii) 확인 결과를 CD-1 플랫폼별 default + §7.4 권고 진입 경로에 매핑 + (iii) ⭐ host 확인에서 *새로 드러난* 발효 선결 3건 + (iv) 수단 결정 *권고* (고정 아님) + (v) 백업키 정책 *검토* (CD-7/BI-9) + (vi) binary PoC 축별 매핑 (P-5/CD-5) — **실 변경·발효 0건**.

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**: host OS 사실 보고 / 수단 후보 좁힘 / 새 발효 선결 식별 / 수단 결정·백업키 정책 *권고* / binary PoC 매핑.
- **하지 않는 것 (사용자 명시 영구 답습)**: ❌ 수단 *결정 고정* (TPM vs YubiKey 최종 확정) / ❌ **tpm2-pkcs11·ssh-tpm-agent 등 설치** / ❌ **tss group 추가·docker group 변경** / ❌ **TPM/YubiKey 서명 키 생성·`allowed_signers` 작성·git 서명 구성** / ❌ env scrub·cap_drop·docker secret·entrypoint stat 실 구성 / ❌ BI-3 충족 PoC(E-1~11)·침투 시연(PEN-1~8) 실 실행 / ❌ 실 hook·CI provenance step·GitHub ruleset 변경 / ❌ sigstore·gitsign·Rekor 도입 / ❌ Operational Readiness PASS / Hermes PMO 격상 / Vault HSM ST-4 / ❌ 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / ❌ 합의 보고서 작성·commit·push / ❌ git history rewrite / 원 합의 본문(`f29c772`) 자동 정정 / 5 영구 핵심 제약·Provider Liquidity 약화.

---

## 1. ⭐ host OS 확인 결과 (실 read-only 점검 — 2026-05-21)

CD-1 의 "실제 host OS 확인 = entry"(`ead5754` line 104)와 §7.4 권고 진입 경로 step (1) 답습. 모두 read-only 점검(파일/장치 stat·`tpm2_getcap` 시도·`dpkg -l`·`git config --get`), 변경 0건.

### 1.1 플랫폼 / 하드웨어

| 항목 | 확인값 | 수단 함의 |
|----|----|----|
| 플랫폼 | **Linux Ubuntu 24.04.4 LTS, aarch64 (ARM64)** (kernel 6.17.0-1018-nvidia, host `promaxgb10-f3c4`) | CD-1 플랫폼별 default → **Linux 분기** (macOS SE 분기 해당 없음) |
| **Secure Enclave** | ❌ **해당 없음** (macOS 전용) | CD-1 macOS SE 후보 **소거** |
| **TPM 2.0** | ✅ **하드웨어 존재** — `/dev/tpm0`·`/dev/tpmrm0`, `/sys/class/tpm/tpm0` "TPM 2.0 Device", `tpm_version_major=2`. `tpm2-tools`(`tpm2_getcap`) 설치됨 | CD-1 "Linux → TPM(tpm2-pkcs11)" host-bound 1순위 후보 **하드웨어 가용** |
| **YubiKey / FIDO2** | ⚠️ **토큰 미존재이나 host-side 스택 준비됨** — USB 토큰 없음·`ykman` 미설치이나 **`ssh-sk-helper`(`/usr/lib/openssh/ssh-sk-helper`, 264KB 실재) + `libfido2-1 1.14.0` 설치됨 + OpenSSH 9.6 `sk-ed25519` 지원** | CD-1 보강 후보 M2 = **토큰 조달만**(host-side 미들웨어 0단계 추가). ⭐ **CMA-1: TPM 브리지(§1.2)와 비대칭 — D1 역전 입력** |

### 1.2 서명 도구 / 설정 현황

| 항목 | 확인값 | 함의 |
|----|----|----|
| TPM 서명 브리지 | ❌ **전부 미설치** — `tpm2-pkcs11`·`libtpm2-pkcs11`·`tpm2-openssl`·`tpm2-abrmd`·`ssh-tpm-agent` 모두 absent | CD-1 "Linux TPM `tpm2-pkcs11` PKCS#11 브리지" 경로 = **설치 선결**(= 실 구성, 본 brief 0건). ⭐ **CMA-1 비대칭**: YubiKey host-side 미들웨어(§1.1)는 *이미 준비*된 반면 TPM 브리지는 *0개* — `ead5754` D1("Linux TPM 브리지 한 단계 더")이 *TPM 불리 방향으로* 실측 확인 |
| git 서명 설정 | ❌ **전부 unset** — `gpg.format`·`user.signingkey`·`commit.gpgsign`·`gpg.ssh.allowedSignersFile` 미설정 | clean slate — 기존 서명 키 마이그레이션 부담 0. 단 처음부터 구성 필요 |
| git user (local) | `jokwangwon` / `jokwangwon@users.noreply.github.com` | 후속 74 noreply 발효 확인됨 (정상) |
| 암호 도구 | gpg 2.4.4 / OpenSSL 3.0.13 / OpenSSH 9.6p1 | SSH 서명(`sk-`/PKCS#11) 경로 도구 가용 |

### 1.3 ⭐ host 확인에서 *새로 드러난* 발효 선결 3건 (CD-1~10 에 없던 신규)

> 이 3건은 후속 72 합의(`ead5754`) 시점엔 host 미확인이라 *드러나지 않았던* 항목 — host OS 확인의 핵심 산출. 발효 의사결정에 가시화 필수.

| # | 발견 | 위협/함의 | 연결 |
|---|----|----|----|
| **H-1** ⭐⭐ | **현 OS 사용자 `delangi` 가 `docker` group 소속** (`groups` = `adm sudo audio dip plugdev users lpadmin docker`) | docker group = `docker run -v /:/host` 로 **host filesystem 전체 root-equivalent 접근** = host escape 동치. **CD-3("docker socket 미마운트 + CAP_SYS_PTRACE drop = 어느 수단 택해도 비협상", `ead5754` line 106) + PEN-5(host escape)의 *선결 hole***. 서명 host 의 상시 사용자가 이미 host-escape-동치 권한 보유 → 아무리 TPM 으로 키를 격리해도 *그 host 에서* 키 사용 능력 우회 가능 (touch policy 없으면). | CD-3 / CD-5 PEN-5 / §6 host 침해 직교 잔존 |
| **H-2** | **`delangi` 가 `tss` group *미소속*** → `/dev/tpmrm0` 접근 시 `Permission denied` (`tpm2_getcap` 실패 확인). 단 `sudo` 보유. (실측: `tss` group 멤버 0명) | TPM 사용 = tss group 추가(또는 udev rule) = **권한/구성 변경 = 발효**(본 brief 0건). ⚠️ *누구에게* tss 를 주는지가 격리 경계. ⭐ **CMA-3: H-1 과 동일 문제의 두 발현** — tss 를 `delangi`(=docker group=root-동치)에 주면 H-1 해소(O-2) 효과 무효 → **tss 부여 = docker group 미소속 분리 서명 사용자에게만**(H-1↔H-2 단일 결정) | CD-3 / CMA-3 단일 결정 |
| **H-3** | **TPM 서명 브리지 미설치** (§1.2) | CD-1 Linux TPM 경로 = `tpm2-pkcs11` 설치 + PKCS#11 → ssh-agent/gpg 브리지 구성 선결 = **실 구성(발효)**. Agent A 의 D1 지적("Linux TPM 브리지 한 단계 더", `ead5754` line 50)이 *실측으로 확인* — 브리지 0개 상태. ⭐ **CMA-4: 경로 분기** — (a) PKCS#11+ssh-agent(상시 agent socket = H-1/CD-3 탈취 표면) vs (b) **ssh-tpm-agent**(TPM 전용 ssh-agent, git 서명에 더 직접적). 경로 선택이 곧 agent socket 표면·CD-8 설계 좌우 | CD-1 D1 / CMA-4 / CD-8 환경 분기 |

---

## 2. host 확인 → CD-1 + §7.4 매핑 (수단 후보 좁힘)

### 2.1 CD-1 플랫폼별 default 적용 (`ead5754` 권고 답습)

`ead5754` CD-1 권고 = **"host-bound 물리 격리(TPM/Secure Enclave) 1순위 + M2 = touch-to-sign 필수 시 보강 + 플랫폼별 default"**. host 확인 결과 적용:

```
[macOS Secure Enclave]  ──── 소거 (이 host = Linux ARM64)
[Linux host-bound]      ──── TPM 2.0 ✅ 하드웨어 가용 (1순위 후보)
                                 ⊕ 단 H-2(tss) + H-3(tpm2-pkcs11) 선결
[M2 외장 토큰]          ──── YubiKey/FIDO2 미보유 → touch-to-sign 보강 필요 시 *조달* (CD-6)
[M1 공통 전제 위생]     ──── 어느 수단이든 비협상 (단 H-1 docker group 선결 hole)
```

- **TPM 2.0 하드웨어 실재** → host-bound 물리 격리가 이 host 에서 *가능*. CD-7 백업키 역설 회피(TPM 0개) 근거도 적용 가능.
- ⭐ **CMA-1 (host 실측 반영 D1 재평가 — 단순 TPM 1순위 답습 *금지*)**: `ead5754` D1 Reviewer 판정("A 의 Linux TPM 연동 단순성 지적은 실재하나 *플랫폼 종속*, B/C 의 TPM 우위축[백업키·PL]이 더 무겁다")은 **host 미확인 시점 추론**이었다. host 실측은 그 D1 의 연동 복잡도 비대칭을 **TPM 불리 방향으로 확대** — TPM 경로(`tpm2-pkcs11`/`ssh-tpm-agent`) = **0개 설치**(브리지 + tss[H-2] + 권한 = 3단계 발효) vs YubiKey `sk-` 경로 = **host-side 미들웨어 이미 존재**(`ssh-sk-helper`+`libfido2`, 토큰 조달만). → **본 brief 는 수단 순위를 *고정/flip 하지 않고* 두 시나리오를 *대칭 병치*** (§3.1). 조기 수단 고정 편향 차단.

### 2.2 §7.4 권고 진입 경로 위치 (4축 통합 정리 brief 답습)

- §7.4: "권고 진입 경로 = **(1) credential 수단 발효(host OS 확인 → TPM/SE/M2 결정) → (2) allow-list → (3) anchor → (4) audit**, 각 단계 observe mode 우선 + 축별 binary PoC(P-5)".
- 본 brief = **(1) credential** 의 *host OS 확인* 부분 완료 + *결정* 부분 = 권고까지(고정은 풀 3+1 후).
- §7.4 2-track(IR-4): enforce 는 순차 / observe 는 4축 동시 조기 가능. credential 은 enforce 의 *최우선 선결*(CP-4) — observe 4축 조기 발효 전에도 credential 격리는 의미 있으나, **"부분 격리 그라데이션 = 최대 거짓 안전감"**(BI3-6) 경계 동반.

---

## 3. 수단 결정 *권고* (고정 아님 — 풀 3+1 + 사용자 명시 권한)

> **본 §3 = 추론적 *권고*. 수단 *고정* = 별도 단계 (CN-6 / `ead5754` §3).**

### 3.1 권고 (host 확인 반영 — CMA-1 대칭 병치 / CMA-2 하한선)

> ⭐ **CMA-1**: 본 §은 host-bound 물리 격리 1순위 *방향*은 유지하되, **TPM vs YubiKey 매체 선택을 *고정하지 않고* 두 시나리오를 대칭 병치**한다 (수단 순위 flip 0건 — 결정 = 풀 3+1·사용자 명시).

**(가) 매체 시나리오 대칭 병치 (CMA-1 — 결정 보류)**

| 시나리오 | 근거(우위) | 비용/리스크 | 발효 선결 |
|----|----|----|----|
| **A: TPM 2.0 (host-bound)** | 백업키 0개(CD-7 역설 회피) · 비용 0 · OS-내장(조달 0) · PL 우위(벤더 lock-in 없음) | 브리지 3단계 발효(H-2 tss + H-3 설치+브리지) · touch-to-sign 부재 시 자동 서명 무방비(→ CMA-2 PIN+presence policy 의무) | H-2 / H-3 (CMA-4 경로 분기) |
| **B: YubiKey `sk-` (외장 토큰)** | host-side 미들웨어 이미 존재(0단계, §1.1) · **H-1 하 touch-to-sign 즉시 가치**(자동 서명 차단 내장) | 토큰 조달 리드타임 · 백업키 2개 역설(CD-7) · 벤더 lock-in(CD-8 추상화로 완화) | 토큰 조달 + CD-7 백업키 2개 |

- **R-3 (PL 우위 = 추상 인터페이스가 결정)**: CD-8 추상 인터페이스(`Signer`/`CredentialSource`) 채택 시 TPM(OS 종속) vs YubiKey(벤더 lock-in) **PL 차이는 대부분 상쇄** — 둘 다 PKCS#11/SSH signer 인터페이스 뒤 교체 가능. PL 우위는 "어느 수단"이 아니라 "추상화 여부"가 결정 → D1 순위 압력 ↓.

**(나) 수단 무관 비협상 (어느 시나리오든 동반)**

| 항목 | 비협상 내용 | 근거 |
|----|----|----|
| ⭐ **자동 서명 차단 (CMA-2 하한선)** | **touch-to-sign 메커니즘 존재 = 수단 무관 비협상 하한선**(CD-3 동층위). TPM 택하면 **PIN+presence policy 의무** / YubiKey 택하면 **touch=always 의무** + PIN 캐시 비활성. H-1 완전 침해 시 *유일* 잔존 방어 — 수단 순위와 *직교* | CMA-2 (B-2+C-2 수렴) / CD-6 |
| **공통 전제 위생** | M1: env scrub·agent socket 미마운트·cap_drop[ALL+SYS_PTRACE]·docker socket 미마운트·credential helper 비활성 | CD-2 / CD-3 |
| **H-1 우선 해소** | docker group hole = 수단 결정 *이전* 선결(§3.2 / §7 S-0) | CMA-3 / CMA-5 |
| **결정 구조** | 단일 고정 아님 — 환경 분기(local 물리격리 / Docker M1+secret / CI ephemeral) + 추상 인터페이스(`Signer`/`CredentialSource`, ADR-011 §2.1(a), R-4 Signer/Verifier 분리) + 단계적 채택 | CD-8 / R-3 / R-4 |

### 3.2 ⭐ H-1 (docker group) = 수단 결정 *이전*의 선결

- 핵심: **TPM 으로 키를 칩 밖 미이탈로 격리해도(비추출성 *유지*), `delangi` 가 `docker` group 으로 host 전체에 root-equivalent 접근 가능하면 *서명 능력*(TPM 에 서명 요청)은 탈취 가능** — (a) TPM 서명을 호출하는 프로세스/agent socket 에 접근 (touch policy 없으면 무제한 서명), (b) host filesystem 의 어떤 격리 설정도 우회. **CD-3 가 "비협상"으로 못박은 바로 그 표면이 *상시 사용자 권한*으로 이미 열려 있음.**
- ⭐ **CMA-5 (위협 강도 — escape 가 "악성 명령 한 줄"보다 넓음)**: 위협은 *명시적 악성 `docker run -v`* 에 국한되지 않는다. **`delangi` 로 실행되는 *임의 코드*(LLM 이 생성·실행한 스크립트 · 공급망 트로이[악성 npm/pip postinstall] 포함)가 *별도 exploit 없이* docker API 로 host root → 그 root 가 PKCS#11/agent/signing 프로세스 도달**. 이는 BI-3 신뢰 모델(Hermes/에이전트 = 신뢰 경계 밖)의 *기반 무효화* — 에이전트가 delangi 권한으로 무언가 실행하면 곧 root. "사용자가 나쁜 명령 안 치면 됨" 수준이 아닌 *상시·수동적* 위협.
- → **수단(TPM vs YubiKey) 결정 *이전*에 H-1 이 발효 선결**: docker group 권한 모델 재검토(O-1 rootless / O-2·O-5 서명 사용자 분리 / O-3 sudo 한정 — `h1-docker-group-hole-resolution-brief.md`) + touch-to-sign(CMA-2) 비협상 하한선(H-1 잔존해도 자동 서명 차단).
- ⭐ **CMA-7 (부분 격리 면책 라벨 — 거짓 안전감 능동 차단)**: **"TPM 키 생성 완료 ≠ 격리 충족"**. H-1 미해소 *또는* touch policy 미설정 *또는* PEN-1~8 미통과 = **"서명 능력 차단 보장 0"**(BI-7 면책 라벨 동형). §5 PoC binary 통과 *전까지* 모든 중간 상태는 "라벨만 격리". "TPM 결정했으니 격리됐다"가 H-1 미해소 시 *음의 순이득*(`ead5754` §4 거짓 안전감 차단).

---

## 4. 백업키 정책 *검토* (CD-7 / BI-9 — 권고, 고정 아님)

> CD-7(`ead5754` line 110): "백업 키 = TPM 우선으로 표면 최소화 — TPM 채택 시 0개(재생성 SOP) / M2 채택 시 정확히 2개·offline·air-gapped·물리 봉인 recovery seed + revocation SOP". §7.2 P-1/IB-3 백업키 역설.

### 4.1 백업키 역설 (BI-9 / CBI3-2) 재확인

- **역설**: 가용성↑(키 분실/host 사망 시 lock-out 방지) ⊕ 기밀성↓·공격표면 N배(백업 키 N개 = CT-1 추출 표면 N배 + 보관처가 §6 회귀). hardware key 의 *비추출성*(가치의 핵심)을 백업이 *훼손*.

### 4.2 host 확인 반영 권고

| 수단 | 백업키 권고 | 근거 |
|----|----|----|
| **TPM (1순위)** | **0개 — 재생성 SOP** (키 분실 = 새 키 생성 + `allowed_signers` 갱신 + 구 키 revoke). 활성 키 1개 = 표면 증가 0 | CD-7 + N-C2 "offline cold seed, hot 복제 회피" / B "분실 SPOF 부재로 역설 회피"(P1) |
| YubiKey (보강 시) | 정확히 2개·offline·air-gapped·물리 봉인 recovery seed + revocation SOP(분실 추적·off-host 강제·audit 기록) | CD-7 / N-C2 |

- ⭐ **TPM 백업키 측면 우위 재확인**: TPM 채택 = 백업키 0개 → 역설 자체를 *구조적으로 회피*(B 수렴 근거 P1). 단 "재생성 SOP" 가 `allowed_signers` 갱신 경로 = T3 보호(Hermes 미주입, CD-7) 동반.
- ⭐ **CMA-6 (백업키 0개의 *대가* = 표면 이동, 거짓 안전감 차단)**: 백업키 0개는 안전을 *확정*하지 않고 **표면을 백업키 → `allowed_signers`/fingerprint allow-list *갱신 경로* 로 이동**시킨다. 그 갱신 = **신뢰 root 변경 = BI-1 self-bypass·CP-1 owner 경로와 *동일 표면***. 따라서: (a) 갱신은 **R-I-CONFIG-CHANGE T3**(사람 직접, Hermes 미주입) 경유 + 그 갱신을 **anchor/audit 가 기록·검증**(owner 경로 잔존 명시), (b) **revoke-before-register** 순서(구 키 revoke 전 새 키 등록 = 두 키 동시 유효 윈도우 = 표면 일시 증가 → Rollback Trigger CD-CBI-3), (c) "구 키 revoke" 강제 메커니즘 부재 시 = 표면 누적(N개 회귀).
- ⚠️ **재생성 SOP 의 잔여**: TPM/host 사망(디스크 교체·재설치 포함) 시 재생성까지 서명 불가 = 일시 lock-out. single-host 1인 환경에서 허용 가능한가? = 백업키 정책 *고정* 시 결정 항목(grace-period soft fallback 채택 시 = bypass 창, CD-CBI-3 Rollback Trigger 동반). 재생성 SOP 실 단계 = 발효 시 문서화(R-9).

---

## 5. binary 입증 PoC 축별 매핑 (P-5 / CD-5 — credential 축)

> §7.2 P-5 / CD-5(`ead5754` line 108): "BI-3 충족 = 수단 라벨 ≠ 입증. 계산적 PoC(E-1~11) + 적대적 침투 시연(PEN-1~8) binary — 부분 통과 = FAIL." **실 실행 = Implementation Evidence PASS 단계 (본 brief 0건, 매핑만)**.

| 종류 | 내용 | host 확인 반영 |
|----|----|----|
| 계산적 PoC (E-1~11) | 컨테이너 내 서명 키 0건 / agent socket 0건 / git token 0건 / `docker.sock` 0건 / `CAP_SYS_PTRACE` 0건 시연 | **H-1 docker group → E 시리즈에 "host 사용자 docker group 미접근(또는 rootless)" 항목 추가 필요** |
| 적대적 침투 (PEN-1~8) | host escape(PEN-5)·메모리 scrape(PEN-1)·credential helper 탈취 등 *전부 실패* | **H-1 → PEN-5(host escape) = docker group 경유 시연이 *반드시* 실패해야 함**. ⭐ **R-5: S-0(H-1 해소) 미발효 상태에서 PEN-5 는 *반드시 FAIL*** → S-0 가 S-6 PoC 의 선결임이 PoC 레벨에서 강제(§7 순서 정합) |
| ⭐ **TPM 서명 경로 (CMA-4)** | 채택 경로가 PKCS#11+ssh-agent 면 **상시 agent socket 미마운트/미접근** 시연 / ssh-tpm-agent 면 그 socket | "PoC 실시"가 *어느 경로* 입증인지 명시 = agent socket 표면이 경로별 다름 |
| touch policy (CD-6 / CMA-2) | **수단 무관**: TPM=PIN+presence policy / YubiKey=touch=always — PIN 캐시 비활성 → *자동* 서명 차단 능동 확인 (사회공학 오용은 잔여, R-6) | CMA-2 하한선 = 수단 결정과 무관 의무 |
| image digest (CD-9) | 시연 image = 운영 image digest 일치 (공급망 위장 차단) | 발효 시 |

- ⭐ **CP-2 라벨화 재발 차단**: "PoC 실시"가 *무엇을* 입증하는지 명시 = "컨테이너가 서명 능력 미보유 + host escape 경로(H-1 포함) 전부 차단 + 자동 서명 차단(CMA-2) 능동 확인". "TPM 켰음" 라벨 ≠ 충족.
- **R-4 (Signer/Verifier 책무 분리)**: CD-8 추상 인터페이스는 **서명(`Signer`, host 물리 격리)과 검증(`Verifier`, CI fingerprint 대조 = allow-list BI-1)을 분리**해야 한다. CI 는 서명 키가 아닌 fingerprint *대조* 책무 → 한 인터페이스에 묶으면 local↔CI 교체가 깨짐.

---

## 6. owner self-bypass 잔존 명문 (IB-2 — 발효 의사결정 가시화)

> 4축 통합 정리 §7.4 IB-2: "P-1~P-5 충족해도 owner(사람) 경로 self-bypass 는 4축 모두 잔존". credential 축 대칭 = **신뢰 키 개인 키를 사람이 Hermes 에 재주입(역경로) / 백업 키 노출**(BI1C-4 (d)(e)).

- credential 수단을 발효(TPM 결정·구성)해도, **owner(사람)가 신뢰 키를 Hermes 컨테이너에 재주입하거나 백업 경로로 키를 꺼내는 owner self-bypass 는 잔존**. 이는 single-host 1인=admin SPOF 의 필연 귀결(CP-1).
- **발효 의사결정자(사용자)는 인지해야 함**: TPM 수단 발효 = *에이전트(컨테이너) 경로* 키 추출 차단이며, *owner 경로*는 MVP-6(Rekor 제3자) 전까지 *수용된 SPOF*. "Rekor/Sigstore MVP-6 DEFER = owner self-bypass 영구 수용 결정 동치"(IB-2).
- → 본 brief 의 수단 권고 = "수용된 SPOF 위 최선"이지 "안전 확정" 아님 (`ead5754` §4 거짓 안전감 차단 / 통합 §9 IB-1).
- **R-2 (CP-7 gitsign = credential 의 *유일 예외* trigger 보존)**: 4축 통합 §6.1 CP-7(Sigstore 1회 융합)은 allow-list+anchor+audit 3축 owner 경로를 동시 해소하나 **credential(CP-4)은 못 닫는다** — gitsign keyless 도 OIDC 토큰 격리가 필요하므로. → **MVP-6 에서 "Sigstore 도입했으니 credential 도 해결됐다"는 거짓 안전감 차단**: credential 격리는 Sigstore 채택과 *직교*하게 *여전히* 선결. (도입 = MVP-6 DEFER, 본 brief 0건)

---

## 7. 발효 선결 정리 (수단 *고정* 전 필수)

| 선결 | 내용 | 상태 | 권고 순서 |
|----|----|----|----|
| **S-0** ⭐ H-1 docker group hole | 서명 host 상시 사용자 docker group = host escape 동치 → CD-3 비협상의 선결 hole. **(B) 검토 완료** (`h1-docker-group-hole-resolution-brief.md`): 컨테이너 측면 CD-3 = PoC 패턴으로 이미 충족 / 남은 구멍 = **rootful docker + delangi standing root-동치**. 해소 = O-1(rootless) 또는 O-2(서명 사용자 분리) + O-4(touch-to-sign 보강) | ⚠️ 검토 완료·발효 미실시 | **수단 결정 *이전*** |
| **S-1** 수단 결정 고정 | **TPM vs YubiKey 대칭 병치(CMA-1) 재평가 후** 매체 결정 + 자동 서명 차단(CMA-2) 메커니즘 — 풀 3+1 + 사용자 명시 | ❌ 권고만 (본 brief, 순위 flip 0건) | S-0 후 |
| **S-2** H-2 tss 권한 모델 (⭐ CMA-3: S-0 과 단일 결정) | tss 부여 = **docker group 미소속 분리 서명 사용자에게만**(delangi/Hermes 컨테이너 제외) — "서명 능력을 docker-privileged 계정에서 구조적 분리" = S-0 와 한 결정 | ❌ 미정의 | **S-0 과 결합** |
| **S-3** H-3 브리지 구성 | tpm2-pkcs11 설치 + PKCS#11→agent 브리지 (= 실 구성) | ❌ 미실시 | S-1 후 (발효) |
| **S-4** 백업키 정책 고정 | TPM=0개 재생성 SOP (§4) | ❌ 권고만 | S-1 동반 |
| **S-5** 추상 인터페이스·환경 분기 | `Signer`/`CredentialSource` + local/Docker/CI 분기 (CD-8) | ❌ 미설계 | S-1 후 |
| **S-6** binary PoC 실 실행 | E-1~11 + PEN-1~8 (H-1 포함) — Implementation Evidence PASS | ❌ 미실시 | S-3 후 |

- ⭐ **순서 권고**: **S-0+S-2(docker group hole 해소 + tss 분리 사용자 = 단일 결정, CMA-3) → S-1(수단 결정, TPM vs YubiKey 대칭 병치 재평가, 풀 3+1) → S-4(백업키) → S-3/S-5(구성·설계) → S-6(binary PoC, PEN-5 통과)**. S-0+S-2 가 수단 결정보다 앞 — H-1 미해소 시 어떤 수단도 음의 순이득(§3.2). S-0 *발효*(PEN-5 통과)가 S-1 entry(R-5).

---

## 8. 합의 형태 + 다음 단계

- 본 brief = credential 수단 *발효* 진입 = **보안 enforcement 최강 BLOCKING(BI-3) + 핵심 제약 #1 직결 + 아키텍처 의사결정** → **풀 3+1 의무**(`ead5754` line 8 답습, Reviewer-only 부적격).
- Agent A(구현/정합): host 확인 사실 정확성·TPM 브리지(H-3) 실 동작 경로·추상 인터페이스. Agent B(보안): ⭐ H-1 docker group hole 위협 평가·백업키 역설·owner self-bypass(IB-2). Agent C(대안): YubiKey vs TPM trade-off(host 확인 반영)·결정 구조·H-1 해소 대안(rootless/분리).
- 합의 = **추론적 검증(권고) 한정** — 수단 *결정 고정*·실 구성·PoC 실 실행 = 사용자 명시 + 별도 단계.

### 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

> 풀 3+1 합의(`3plus1-consensus-2026-05-21-credential-means-activation.md`) 완료 = APPROVE WITH CONDITIONS (CMA-1~7). v2 = 본 합의 반영. 이후:

| 옵션 | 내용 | 형태 |
|----|----|----|
| (가) | ✅ **본 v2** — CMA-1~7 + R 반영 (현 단계) | brief 수정 |
| (나) | ⭐ **S-0+S-2 발효** — H-1 해소(rootless/서명 사용자 분리) + tss 분리 사용자 단일 결정 (수단 결정 *이전*) | 발효 |
| (다) | 수단 결정 고정 — TPM vs YubiKey 대칭 병치(CMA-1) 재평가 후 (S-0+S-2 선결) | 발효 (보류) |
| (라) | 세션 종료 / 다른 단위 | 메타 |

---

## 부록 A — 답습 출처

| 출처 | 반영 |
|----|----|
| host OS 실 read-only 점검 (2026-05-21) | §1 |
| `ead5754` BI-3 수단 결정 합의 CD-1~10 + CD-CBI-1~3 | §2·§3·§4·§5 |
| 4축 통합 정리 brief §6·§7.2·§7.4 (IB-2/IB-3/IB-4/IR-4) | §2.2·§6·§7 |
| `f29c772` Group I 구현 entry 합의 (BI-3 우선순위·CN-6) | §3·§8 |
| ADR-011 §2.1 means/ends (a)~(d) | §3.1 결정 구조 |
| credential 수단 발효 풀 3+1 합의 (CMA-1~7 + R-1~10) | v2 변경 이력·§1~§7 |
| BI-1 합의 (`4c5f5f4`, BI1C-4 (d)(e) cross-축, R-8) | §6 owner self-bypass |
| host 추가 read-only 점검 (`ssh-sk-helper`·`libfido2`·`tss` group, 2026-05-21) | §1.1·§1.3·§2.1 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

수단 *결정 고정*(TPM/YubiKey 최종 확정) / **tpm2-pkcs11·ssh-tpm-agent 등 설치** / **tss group 추가·docker group 변경·udev rule** / **TPM/YubiKey 서명 키 생성·`allowed_signers` 작성·git 서명 구성**(`gpg.format`/`commit.gpgsign`) / env scrub·`cap_drop`·docker secret·entrypoint stat 실 구성 / **BI-3 충족 PoC(E-1~11)·침투 시연(PEN-1~8) 실 실행** / 실 hook(pre-commit/pre-receive/CI provenance step) / GitHub ruleset·branch protection·CI workflow 변경 / filesystem ACL·`read_only` mount·audit sink 실 구성 / **sigstore·gitsign·Rekor 도입** / Hermes runtime·upstream 변경(Dockerfile/`hermes-version.yaml`) / **Vault HSM ST-4**(γ-2 DEFER) / threshold 고정 / **Operational Readiness PASS**(Layer E) / **Hermes PMO 격상**(Layer F) / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / **git history rewrite**(후속 74, SHA 붕괴) / G3·ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`/`ead5754`) 자동 정정** / Group I·α·β·γ 합의 본문 변경 / 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / tmux·Obsidian docs-scope 도입 / 외부 LLM 응답 강제 채택 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
