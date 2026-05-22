# Credential 서명 워크플로우 설계 brief — delangi commit → YubiKey 물리 터치 서명 (DRAFT v2)

> **본 brief = credential 발효 (다) S-3 서명 워크플로우 설계 한정.** 본 brief 의 어떤 §도 그 자체로 **YubiKey 키 생성·git 서명 구성·sudoers/systemd unit 작성·broker 구현·발효** 를 발생시키지 않는다. 본 brief = **수단 재고(TPM→YubiKey) 기록 + 워크플로우 후보 + P-PRIV 적용 + SW-1~8 반영** — 실 변경 0건. staged: brief → 승인 → (3+1) → S-3 발효(⚠️ **YubiKey 조달 후**).

---

**작성일**: 2026-05-22
**Status**: **DRAFT v2 — ⛔ 발효 DEFER (청사진 보존)**
**⛔ 발효 DEFER 결정 (사용자 명시 2026-05-22, 비례성)**: 본 프로젝트 = solo·single-host·**본인용 개인 개발 툴**. credential 서명 격리(하드웨어 키·touch-per-commit·서명 사용자)는 실 위협 모델(에이전트 실수·공급망 = review/test/git로 충분)에 **비례 초과** → 발효 비권고. 본 brief = **DESIGN 청사진으로 보존** — 실 trigger(팀 합류 / public 배포 / 외부 의존 / 컴플라이언스) 발생 시 발효. means/ends(ADR-011): 하드웨어 서명 = MEANS, 현 비용 > 이득. [[feedback_proportionate_security_personal_tool]] 답습.
(이하 v2 내용 = 발효 시 참조용 청사진:)
**v2 이력**: v1[TPM 가정] + 서명 워크플로우 풀 3+1 합의 `3plus1-consensus-2026-05-22-credential-signing-workflow.md` **REVISE** → **수단 재고 TPM→YubiKey** + BLOCKING SW-1~8 반영
**진입 단위**: credential 발효 (다) S-3 — 서명 워크플로우 + 수단 재결정
**확정된 선행 결정**:
- S-0+S-2 발효 완료(✅ `signer` uid 1001 = tss·docker 미포함 / delangi = docker·sudo·tss 미포함)
- ⭐ **수단 = YubiKey `sk-ssh-ed25519`** (TPM 에서 *재고*, 사용자 명시 2026-05-22) — 근거: 3+1 SW-1(TPM+PIN backstop 이 root-동치 host 에서 무효) / CMA-1 host 실측 우위(`ssh-sk-helper`·`libfido2 1.14.0`·OpenSSH 9.6 `sk-` ready) / O-5·개입 최소화 양립
- **CMA-2 = 물리 터치**(touch=always) — *메모리 미진입 인간 행위* → root scrape 불가
- ⚠️ **YubiKey 토큰 미보유 → S-3 발효 = 조달 선결**

## v2 변경 이력 (TPM→YubiKey 재고 + SW-1~8)

| 항목 | v1 → v2 |
|----|----|
| **수단** | TPM 2.0(PIN) → **YubiKey sk-(물리 터치)**. SW-1 RESOLVED |
| **SW-1** ⭐⭐ (PIN backstop 거짓) | **해소**: 물리 터치 = 메모리 미진입 → root(delangi=docker+sudo)도 자동 서명 불가. backstop = 토큰+터치(메모리 비밀 아님) |
| **SW-2** (W-1 구현 불능) | sk- 키는 PKCS#11/ssh-agent *불필요*(ssh-keygen 직접) → SW-2(a) 해소. git file-path/cross-user(b)(c)는 §1 워크플로우별 처리 |
| **SW-3** (systemd socket broker) | §1 W-Y3 후보 병치 (DiD 시) |
| **SW-4** (재귀 닻 무효) | YubiKey 하 무관 — backstop 이 파일 권한 아닌 물리 터치. allowed_signers 갱신 = T3 owner 경로(잔존, IB-2) |
| **SW-5** (AP-4) | §2 — 직접 서명 시 helper 불요(escape 표면↓), DiD helper 시 §2.2 |
| **SW-6** (사실/citation) | tpm2-pkcs11 무관(YubiKey). 수단 = YubiKey 명시(CMA-1 정합·CMA-4 = sk- 경로) |
| **SW-7** (Signer 추상 PL) | §3 — `Signer` 인터페이스(매체 YubiKey↔TPM↔keyless 교체) |
| **SW-8** (PoC root 경로) | §2.3 — root 가 터치 없이 서명 *실패* binary |

---

## 0. 설계 문제 (YubiKey 로 재구성)

```
delangi (repo 작업·docker+sudo=root-동치)
    │  git commit -S
    ▼
[서명 호출] → YubiKey sk- 키 + libfido2 → ⭐ 물리 터치 요구(touch=always) → 서명
```

- ⭐ **핵심 전환**: TPM 모델은 backstop 을 *메모리 비밀(PIN)* 에 뒀고, root 가 PIN 을 scrape 해 무너졌다(SW-1). **YubiKey 모델은 backstop 을 *물리 터치* 에 둔다 — 터치는 메모리에 진입하지 않는 인간 행위라 root 도 scrape/자동화 불가.** 따라서 **격리의 본질이 "어느 사용자가 호출하나"(O-5 사용자 분리)에서 "물리 터치 존재"로 이동**한다.
- **함의**: delangi(=root-동치)가 서명을 *호출* 해도 **물리 터치 없이는 서명 불가** → backstop 이 *호출 사용자와 무관* 하게 성립. 즉 **O-5 사용자 분리는 더 이상 backstop 의 필수 조건이 아니라 옵션 defense-in-depth**(키 핸들 보호·등록 제한)가 된다.

---

## 1. 워크플로우 후보 (YubiKey)

| # | 후보 | 메커니즘 | backstop | trade-off |
|---|----|----|----|----|
| **W-Y1** ⭐ | **delangi 직접 sk- 서명** | delangi 가 sk- 키 핸들 소유, git `gpg.format=ssh`+`user.signingkey`=sk pubkey, `git commit -S` → ssh-keygen -Y sign + libfido2 + **터치** | **물리 터치**(호출자 무관) | 가장 단순·개입 최소화 정합. sudo/broker 불요. 키 핸들 = 비밀 아님(토큰에 비밀 상주) → delangi 소유 무해 |
| **W-Y2** | **signer 사용자 + sk-(DiD)** | sk- 키 핸들을 signer 소유, `sudo -u signer` 또는 broker 경유 서명 | 터치 **+** 사용자 분리(키 핸들 삭제/등록 보호) | DiD. ⚠️ SW-2(b)(c) git file-path/0600 cross-user 처리 필요(wrapper). 기존 signer 사용자 재사용 |
| **W-Y3** | **systemd socket broker(SW-3)** | signer service(socket-activated, `User=signer`, SO_PEERCRED), 서명 요청 중개 | 터치 + broker 격리 | AP-2 4속성. MVP 과함 — DiD 필요 시 |

- **SW-2 해소(YubiKey)**: sk- 키는 **PKCS#11/ssh-agent 불필요** — ssh-keygen 이 sk 키 핸들 파일 + libfido2 로 직접 서명(TPM PKCS#11 의 agent 필수 문제 없음). W-Y1 은 delangi 가 직접 서명하므로 cross-user(0600) 문제도 없음(SW-2 b/c 회피).

---

## 2. 권고 (결정 아님 — 3+1/사용자 명시)

- **MVP = W-Y1 (delangi 직접 sk- 서명)** — 물리 터치가 backstop 이므로 사용자 분리·broker 없이도 root 자동 서명 차단. 가장 단순 + [[project_minimize_user_intervention]] 정합.
  - **개입 = 서명당 1 터치**(CMA-2). AP-3 lease/batch(W-4) = N commit 1 터치(자동 아님·CMA-2 충족)로 *횟수* 축소 가능.
  - **resident vs non-resident sk 키**: resident(YubiKey 저장, 분실 시 추출 위험↓) vs non-resident(핸들 파일 필요). 백업키 2개(CD-7) = YubiKey 2개 등록.
- **W-Y2/W-Y3 = 옵션 DiD** — 키 핸들 삭제(DoS)·신규 키 등록 제한이 필요하면. 단 backstop(터치)은 W-Y1 으로 이미 성립 → MVP 비권고, 추후.
- **기존 signer 사용자(tss)**: YubiKey 는 tss 불요 → **S-2 tss 부여는 moot**(무해, 추후 정리). signer 사용자 = W-Y2 채택 시만 사용.

### 2.1 W-Y1 흐름 (구현 골격 — 발효 시, YubiKey 조달 후)
```
ssh-keygen -t ed25519-sk -O resident -O application=ssh:hermes  (터치, 키 생성 1회)
  → sk pubkey → allowed_signers (BI-1 fingerprint, R-I-CONFIG T3)
git config gpg.format ssh; user.signingkey <sk pubkey>; commit.gpgsign true
git commit -S → ssh-keygen -Y sign + libfido2 + 터치 → 서명
```

### 2.2 AP-4 (W-Y1 직접 서명 = helper 불요 → escape 표면↓)
- W-Y1 은 sudo/helper 없음 → AP-4 helper escape·sudoers 표면(SW-5) *대부분 소거*. 잔존: `allowed_signers` 갱신 = T(신규 키 등록 차단 = CMA-6 owner 경로).
- W-Y2 채택 시에만 helper escape-equivalence(stdin/파일 규약·env_reset·helper 교체) 분석 필요.

### 2.3 SW-8 PoC 종료조건 (binary)
- ① **root(delangi escalate)가 물리 터치 없이 서명 *실패*** (핵심 — 터치 backstop 입증) / ② sk pubkey fingerprint = allowed_signers + BI-1 판정 입력 / ③ 신규 키 무단 등록(allowed_signers 변조) 차단(T3) / ④ **중간 상태 면책**(키 생성 전·allowed_signers 미등록 = "보장 0", CMA-7).
- ⚠️ **owner self-bypass(IB-2) 잔존**: 같은 사람이 물리 YubiKey 보유 + allowed_signers 변경 가능 = MVP 수용 SPOF(터치는 *비의도 자동화* 차단이지 owner 의도 차단 아님).

---

## 3. P-PRIV 정합 + Provider Liquidity (SW-7)

- **R/P/T**: 서명 = T(터치). 키 생성·allowed_signers 등록 = P/T(사람). repo 작업 = R.
- **SW-7 `Signer` 추상**: git↔서명 배선(`gpg.ssh.program` 또는 직접)은 *호출 규약*이고, 매체(YubiKey sk- / TPM / keyless)는 그 뒤 교체 가능. YubiKey hard-bind 회피 — allowed_signers(pubkey 기준 중립)·`gpg.format=ssh`(매체 무관) 유지. CD-8/AR-6 답습.
- **AP-5 거짓 안전감**: W-Y1 구성만으로 완성 아님 — SW-8 PoC(root 터치 없이 서명 실패) binary 통과까지 "보장 0".
- **AR-5 4축 일반화**: 본 패턴(터치=물리 backstop)은 credential 축 인스턴스. anchor/audit 의 T 작업은 별도(터치 비해당) — 권한 처리 패턴(P-PRIV)만 공유.

---

## 4. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 |
|----|----|
| (A) | 본 v2 = **W-Y1 워크플로우 풀 3+1 재합의** (수단 변경 + SW 반영 → 권장) |
| (B) | **YubiKey 조달** 진행(하드웨어 구매) — 발효 선결 |
| (C) | W-Y2/W-Y3 DiD 필요성 형량 (resident 키·백업키 정책 포함) |
| (D) | commit 체크포인트 / 세션 정리 |

- ⚠️ **키 생성·S-3 발효 = YubiKey 조달 + 본 v2 합의 후**. S-0+S-2(signer+tss)는 유효(W-Y2 시 재사용, 아니면 tss moot).
- 수단 재고(YubiKey)가 credential 발효 (다) means 를 *확정* — credential-means-activation brief 의 "시나리오 A(TPM)"는 본 3+1(SW-1)로 "시나리오 B(YubiKey)"로 귀결.

---

## 부록 — 답습 출처 + 금지

**출처**: 서명 워크플로우 3+1(SW-1~8) / P-PRIV(AP-1~5) / credential 발효 합의(CMA-1 host 실측 YubiKey 우위·CMA-2 touch·CMA-6) / `ead5754`(CD-7 백업키·CD-8) / [[project_minimize_user_intervention]].

**금지 (영구 답습)**: YubiKey 키 생성(`ssh-keygen -sk`) / git 서명 구성(`gpg.format`/`commit.gpgsign`) / `allowed_signers` 작성 / helper·wrapper·systemd unit·broker 작성 / sudoers 변경 / **YubiKey 조달 자동화**(사용자) / signer tss 정리 발효 / S-3 이후 발효 / sigstore·gitsign·Rekor / Operational Readiness PASS / Hermes PMO 격상 / git history rewrite / 합의·brief 본문 자동 갱신 / 원 합의(`ead5754`/credential 발효 합의) 자동 정정 / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화.
