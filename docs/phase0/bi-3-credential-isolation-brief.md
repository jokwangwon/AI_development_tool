# BI-3 Credential 격리 brief — 4축 공통 선결 전제 심화 (DRAFT v2)

> **본 brief = Group I 구현 entry 합의(`f29c772`, R-I-IMPL-BOUNDARY)의 *최강 BLOCKING* BI-3("credential 격리 = 4축 공통 선결 전제")를 *단독 심화* 하는 brief 한정.** 본 brief 의 어떤 §도 그 자체로 실 hook(pre-commit / pre-receive) / GitHub ruleset·branch protection / CI provenance step / filesystem ACL·`read_only` mount·`cap_drop` / **credential isolation(사람 키 Hermes 미주입) 실 구성** / audit sink 구현 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 을 발생시키지 않는다. 본 brief = **격리 대상·수단 후보·구조적 흡수·single-host 한계·진입 gate·합의 형태 정비** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (BI-3 합의 `cc5b517` BLOCKING BI3-1~BI3-8 + 조건부 CBI3-1~4 + 권고 REC-1~6 반영 — 본문 미반영, 수단 결정 0건)
**진입 단위**: Group I 구현 entry 합의 후속 #1 (`f29c772` 합의 §2.2 BI-3 = 우선순위 **1**·최강 BLOCKING)
**선행 발효 답습**: `cc5b517` BI-3 brief 검증 풀 3+1 합의 (APPROVE WITH CONDITIONS, BI3-1~BI3-8) + `8e57f7b`/`f29c772` Group I 구현 entry 합의 (BI-1~BI-10 + CBI-1~CBI-4 + N-1) + `596f866` Group I 구현 경계 brief + `708bc0e` G3 provenance check 4축 DESIGN + γ-1 `9b1f8cd`(ST-1) · γ-2 `2e9d46b`(ST-4 DEFER) + GP-3 §5 (Credential/Secret Hygiene) + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **`cc5b517` 합의 BI3-1~BI3-8 + CBI3-1~4 + REC-1~6 + §4 거짓 안전감 3축 확장 + `f29c772` BI-3/CBI-1/§2.4** + boundary brief §3 + γ-1/γ-2 + GP-3 §5
**합의 권위 한계**: 본 brief = BI-3 *심화* DRAFT — 격리 수단 *결정 고정*·hardware/TPM key 채택 *결정*·백업 키 정책 *고정*·실 구성(env scrub / socket 미마운트 / cap_drop / docker secret)은 별도 구현 entry 발효(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다.

---

## v2 변경 이력 (`cc5b517` 합의 BLOCKING + 조건부 + 권고 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **BI3-1** (T-n 라벨 GP-5 충돌) | 격리 대상 라벨 **T-1~T-5 → CT-1~CT-5 (credential target)** 전수 재명명 — roadmap GP-5 "T-1~T-6"(Provider Adapter tools) 점유 충돌 회피 (§3) |
| **BI3-2** (구체 우회 표면 누락) | §3.2 신설 — CT-1~CT-5 의 *구체 차단 표면* enumeration (/proc·ptrace·CAP_SYS_PTRACE / child env 상속 / bind mount 경로 / credential helper·GIT_ASKPASS / **docker socket = host escape 최치명**) |
| **BI3-3** (0-구현 + ends 동등성 미명시) | §4 표에 **"필요 실 구성(0-구현 아님)"** 컬럼 + **"보안 결과(ends) 동등성"** 컬럼 추가 (ADR-011 §2.1(a) 비교표 형식) |
| **BI3-4** (공급망 P11 인터페이스) | §8.2 신설 — 공급망 P11 ↔ credential 격리 (격리 메커니즘 자체가 supply-chain 변조 시 CT-1~CT-5 동시 재유입) |
| **BI3-5** ⭐ (M2 거짓 안전감·touch policy) | §5.1 흡수 서사 *재균형* + §5.4 신설(흡수 한계 = §6 동일 강도 거짓 안전감 차단, 키 추출 ≠ 서명 오용) + §5.3 touch-to-sign/PIN/touch policy = *능동* 메커니즘 명시 |
| **BI3-6** (부분 격리 그라데이션) | §8.3 신설 — 격리 = binary 아님, 중간 상태(CT-1✅ CT-4❌) = 가장 위험한 거짓 안전감 구간 + §11.2 Rollback Trigger 반영 |
| **BI3-7** (N-1/CBI-4 본문 누락) | §4 표에 **M5 (keyless: sigstore/gitsign·Rekor, CBI-4 MVP-6 DEFER)** 행 + §9 Rekor↔BI-5 audit sink 시너지 cross-ref |
| **BI3-8** (audit 완전성 FN 귀속) | §9 — CT-4 격리 = audit *위조/삭제* 한정, *기록 누락(observe FN)* = BI-7/BI-5 소속 명시 |
| CBI3-1 | §4 표 + §5.5 — TPM/Secure Enclave 를 M2 동급 후보 병치 (물리 격리 = 외장 토큰 ⊕ 내장 칩) |
| CBI3-2 | §5.6 — 백업 키 역설(가용성↑ ⊕ 기밀성↓ 공격 표면 N배 + 보관처 §6 회귀 + revocation SOP) |
| CBI3-3 | §7.4 + 부록 A — GitHub plan/ruleset 가용성(BI-4) = CT-2 token 격리 선결 cross-ref |
| CBI3-4 | §7.2 — N-2 정정 *대상* = 원 합의 본문(`f29c772` line 59/92/158) 명시 + 정정 권한 = entry/정오 단계 |
| REC-1~6 | §11.3(credential observe = binary) / §5.6(lock-out SOP·성능) / §3.2(CT-5 ephemeral runner) / §8.1(순이득 음수 측정 후보) / §7.3(line 번호 정밀화) / §10(source-of-truth·Evidence Ledger ↔ CT-4) |

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "BI-3 credential 격리 brief"

본 brief = 위 명령 답습 — **BI-3(credential 격리) 단독 심화** = (i) 격리 *대상* enumeration(CT-1~CT-5) + 구체 우회 표면 + (ii) 격리 *수단 후보* 비교(M1~M5/TPM, means/ends, 결정 0건) + (iii) ⭐ hardware/TPM key 구조적 흡수 + 한계(거짓 안전감 차단) + 백업 키 역설 + (iv) single-host 한계(동일 침해 경계) + (v) GP-3 §5 / ST-1·ST-3·ST-4 정합 + N-2 citation 정밀화 + (vi) 미격리 시 4축 붕괴(순이득 0) + 공급망 P11 + 부분 격리 그라데이션 + (vii) 진입 gate + 합의 형태 — **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 — 구현 entry 합의(후속 69)에서 BI-3 = 우선순위 1·최강 BLOCKING (§1)
2. BI-3 정의 재확인 — credential 격리 = 4축 공통 선결 전제 (§2)
3. 격리 *대상* enumeration(CT-1~CT-5) + ⭐ 구체 우회 표면 (§3)
4. ⭐ 격리 *수단 후보* 비교(M1~M5/TPM, 0-구현·ends 동등성 포함 — 결정 0건, CN-6) (§4)
5. ⭐ hardware/TPM key 구조적 흡수 + 한계(거짓 안전감) + touch policy + 백업 키 역설 (§5)
6. ⭐ single-host 한계 = 동일 침해 경계 = "수용된 SPOF 위 최선" (§6)
7. GP-3 §5 정합 + N-2 정밀화(정정 대상 명시) + line 정밀화 + BI-4 cross-ref + ST 경계 (§7)
8. 미격리 시 4축 붕괴(순이득 0) + ⭐ 공급망 P11 + ⭐ 부분 격리 그라데이션 (§8)
9. audit write credential 재귀 + 완전성 FN 귀속 (BI-5/BI-7 인터페이스) (§9)
10. 영구 핵심 제약 + source-of-truth·Evidence Ledger 인터페이스 (§10)
11. 진입 gate + Rollback Trigger + credential observe binary 성격 (§11)
12. 합의 형태 (풀 3+1 의무) (§12)
13. 다음 단계 (§13)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **credential isolation 실 구성** (사람 signing key·token·SSH/GPG agent socket Hermes 미주입 / env scrub / socket 미마운트 / `cap_drop` / docker secret 정의 / chmod·entrypoint stat 본문)
- ❌ **hardware/TPM-backed key 채택 *결정*** / 토큰 종류 고정 / **백업 키 정책 고정** (개수·등록·revocation 절차 — CBI-1/BI-9/CBI3-2, 결정 = entry 발효)
- ❌ **실 hook 구현** (pre-commit / pre-receive / CI provenance step 본문)
- ❌ **GitHub ruleset / branch protection 변경** / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / paths 필터 — [[feedback_actual_run_trigger_paths_filter]] 답습 의무)
- ❌ **filesystem ACL / `read_only` mount / audit sink 실 구성** / **sigstore·Rekor 실 도입** (M5 = 후보 보존, CBI-4 DEFER)
- ❌ Hermes runtime / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR — ST-1/ST-5 진입 = 풀 3+1 trigger)
- ❌ **Vault HSM ST-4 진입** (γ-2 BLOCK/DEFER MVP-6 답습)
- ❌ **수단 *결정 고정*** (격리 방식·키 매체·secret source — CN-6/means-ends, 결정 = entry 발효)
- ❌ threshold 고정 (observe mode 기간 등)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)**
- ❌ Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경
- ❌ G3 본문 재변경 (§3.1.2/§5.5 4축) / GP-3 본문 변경 / ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** (N-2/line 번호 = 권고 한정, §7.2/§7.3) / Group I·α·β·γ 합의 본문 변경
- ❌ 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. 격리 대상·수단 후보·구조적 흡수·한계·gate 는 *심화/정비/권고* 이며, 격리 수단 *결정*·hardware/TPM key *채택*·백업 키 *정책 고정*·실 구성 *발효* 는 구현 entry 합의(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다. `f29c772`+`cc5b517` 합의가 이미 BI-3 = 최강 BLOCKING·4축 공통 선결 전제·hardware 흡수 한계·single-host = 수용된 SPOF 위 최선·BLOCKING 통합을 **권고로 확정**했으므로, 본 brief 는 그 권고를 *BI-3 단독 결정 공간으로 환원* 하는 심화일 뿐 *결정* 하지 않는다.

---

## 1. 진입 맥락 — BI-3 = 우선순위 1 · 최강 BLOCKING

```
후속 68 (708bc0e) ─ G3 provenance check 4축 DESIGN 발효
        ▼
후속 69 (8e57f7b) ─ Group I 구현 entry 합의 (BI-1~BI-10) · BI-3 = 우선순위 1
        ▼
후속 71 (cc5b517) ─ 본 brief v1 검증 풀 3+1 (APPROVE WITH CONDITIONS, BI3-1~BI3-8)
        ▼
⭐ 본 brief v2 ─ BLOCKING 8 + 조건부 4 + 권고 6 반영 심화 (실 변경 0건)
        ▼ (승인)
credential 수단 결정 합의 (풀 3+1) ─ M1~M5/TPM 中 결정 + BI-3 충족 검증 + 백업 키 정책
        ▼ (승인)
실 구성 + Evidence ─ 미주입/env scrub/socket/cap_drop/docker secret (Implementation Evidence PASS)
```

- **BI-3 우선순위 = 1** (`f29c772` §2.2: `credential(BI-3) > anchor(BI-4) > …`). 순서(만장일치): **credential(물리 흡수) → allow-list 정의 → external anchor → audit**.
- **왜 최강인가**: 나머지 3축(positive allow-list / external anchor / audit sink)이 *모두* "Hermes 환경에 사람/admin credential 미주입"에 **독립 수렴**. credential 격리 = 다른 축의 *상위 전제* 이며, 미격리 시 다른 축을 *구현해도* 명목화된다.

---

## 2. BI-3 정의 재확인 (`f29c772` 답습, 본문 변경 0건)

> **BI-3 (원문):** "credential 격리 = 4축 공통 선결 전제 — 사람 signing key·token·SSH/GPG agent Hermes 미주입(env scrub + socket 미마운트 + cap_drop). 미격리 시 4축 명목화 + 순이득 0 + 거짓 안전감. host 침해 한계 명시. GP-3 §6.2 권위(N-2 — §7.2 정밀화)."

핵심 명제 3개:

1. **선결 전제성**: credential 격리는 4축 중 하나가 *아니라* 나머지 3축이 작동하기 위한 *상위 전제* 다 (positive allow-list 가 검증하는 "사람 권위 신호"를 Hermes 가 위조 불가 = 사람 키가 Hermes 손에 없어야 함).
2. **미격리 = 순이득 0**: credential 미격리 시 4축 전부 명목화하며, metadata-기반 single-author detection(G3 결함의 출발점) 대비 순이득이 0 (오히려 *거짓 안전감* 만 추가 = 음의 순이득, §8.1).
3. **host 침해 한계**: single-host 에서 사용자 호스트 = Hermes 호스트 = 동일 침해 경계. 격리는 *Hermes 프로세스 내부* 로부터의 추출은 막지만 *host 전체 침해* 는 막지 못한다 → 한계 명시 의무 (§6).

---

## 3. 격리 *대상* enumeration (CT-1~CT-5) + 구체 우회 표면

> **BI3-1 반영**: 격리 대상 라벨을 **CT-n (credential target)** 으로 명명 — roadmap GP-5 "T-1~T-6"(Provider Adapter tools: import-linter·AST scanner 등)와 라벨 충돌·cross-ref 혼동 회피.

### 3.1 격리 대상 (무엇을 Hermes 환경에서 떼는가)

| # | 격리 대상 | 떼지 않으면 발생하는 위조 경로 | 4축 중 무력화 대상 |
|---|----------|------------------------------|-------------------|
| **CT-1** | **사람 signing key** (GPG private / SSH signing private) | Hermes 가 사람 서명 직접 생성 → positive allow-list 통과 = "사람 권위 신호" 위조 | positive allow-list |
| **CT-2** | **git host token / PAT / OAuth credential** (push·ruleset·CI 권한) | Hermes 가 ruleset 끄기·required check 우회·force push → external anchor 무력 | external anchor |
| **CT-3** | **SSH agent socket / GPG agent socket** (forwarded·mounted) | 키 파일 없어도 agent 를 통해 *서명 요청* 가능 → CT-1 우회 | positive allow-list |
| **CT-4** | **audit sink write credential** (append-only remote 쓰기 token) | Hermes 가 audit 위조/삭제 → tamper-evidence 무력 (BI-5 재귀, §9) | audit sink |
| **CT-5** | **CI/runner 환경 내 위 credential 의 잔존** (env var·`~/.ssh`·`~/.gnupg`·keychain·step 간 persist) | CI step 이 Hermes 와 동일 신뢰 경계면 CT-1~CT-4 재구성 (BI-1 workflow read-only + ephemeral runner 의존) | 전 축 |

> ⚠️ **CT-1 ≠ GP-3 §5 일반 secret**: GP-3 §5 P3(저장 경로)은 "Hermes *앱이 쓰는* secret(API 키 등)"의 위생이다. BI-3 의 핵심은 그보다 좁고 결정적인 **사람의 *권위 신호* 생성 키**(CT-1/CT-3)다 — 이것이 Hermes 에 있으면 allow-list 자체가 무의미하므로 4축 전체의 선결 전제가 된다. 둘은 *겹치되 동일하지 않다* (§7.1).

### 3.2 ⭐ 구체 우회 표면 (BI3-2 — "어디까지 미주입인가"의 정의)

> 격리는 *대상* 식별만으로 불충분하다 — 각 CT 의 *구체 차단 표면*(syscall·mount·env 상속·process 경계)이 enumeration 되어야 "미주입"의 경계가 정의된다. (G3 §3.1.3 "`.git/` 직접 변조 = filesystem ACL 책무" 의 책무 경계 명시 패턴 동형.)

| 우회 표면 | 설명 | 1차 무력화 대상 | 차단 책무 (수단 후보, §4) |
|----------|------|----------------|------------------------|
| **process memory scrape** (`/proc/<pid>/mem`, `ptrace`) | 동일 host 의 agent process 메모리·ptrace 로 복호화된 키 material·socket fd 접근 | CT-1/CT-3 | `cap_drop` 에 **`CAP_SYS_PTRACE` 포함** + PID namespace 분리 |
| **child process env 상속** | Hermes 가 spawn 하는 git subprocess 등에 token env 동적 상속 | CT-2/CT-5 | env scrub *시점·범위* 정의 (spawn 경계) |
| **bind mount 경로** | `~/.gnupg`·`~/.ssh`·`SSH_AUTH_SOCK` 가 RW mount 시 CT-3 socket 미마운트 무력 | CT-1/CT-3 | mount 경로 전수 명시 (allow-list of mounts) |
| **git credential helper / `GIT_ASKPASS`** | `store`/`cache`/`osxkeychain`·`GIT_ASKPASS` 가 token 노출 | CT-2 | helper 비활성 + token env 미주입 |
| **`/var/run/docker.sock` mount (⭐ 최치명)** | Hermes 컨테이너에 docker socket mount 시 host 전체 escape → 모든 격리 무력 (cap_drop 무관) | 전 축 | **docker socket 미마운트 (BLOCKING 최우선)** |

> 위 표면 enumeration 은 *현 시점 식별* 이며 닫힌 목록 아님 — 구현 entry 발효 시 재검토 (silent gap 차단). 차단 *책무* = 수단 후보(§4), *결정* = entry 발효 (CN-6).

---

## 4. ⭐ 격리 *수단 후보* 비교 (means/ends — 결정 0건, CN-6)

> **BI3-3 반영**: "필요 실 구성(0-구현 아님)" 컬럼 + "보안 결과(ends) 동등성" 컬럼 추가 (ADR-011 §2.1(a) 비교표 형식). **BI3-7 반영**: M5(keyless) 행 보존. **CBI3-1 반영**: TPM/Secure Enclave 를 M2 동급 병치. 어느 행도 본문 고정 아님 (means = entry 발효 결정).

| 수단 후보 | 격리 범위 (CT-1~CT-5) | 필요 실 구성 (0-구현 아님) | ends 동등성 ("사람 키 Hermes 미접근") | single-host 적격 | 부작용 / 한계 | MVP 경계 |
|----------|----------------------|---------------------------|--------------------------------------|------------------|---------------|----------|
| **(M1) 사람 키 미주입** (env scrub + socket 미마운트 + cap_drop) | CT-1/CT-3 부분 | docker-compose `secrets:`·`cap_drop:[ALL,SYS_PTRACE]`·mount 제거·env unset | 행위 규칙(soft) — host 어딘가 키 잔존 | ✅ (ST-3+ST-1) | host 침해 시 host 키 접근 (§6) | single-host 1차 |
| **(M2) hardware-backed key** (YubiKey/FIDO2 — 키 토큰 밖 미이탈) | **CT-1/CT-3 구조적 흡수** (§5) | 토큰 조달·`sk-ssh-ed25519`/`gpg --card` 등록·`allowed_signers`·CI fingerprint·**touch policy** | 물리(키 추출 불가) — *서명 오용*은 별개(§5.4) | ✅ | **1인 lock-out SPOF** → 백업 키(BI-9/§5.6) | single-host 적격 |
| **(TPM) OS-native TPM / Secure Enclave** (CBI3-1 — M2 동급 병치) | CT-1/CT-3 구조적 흡수 | TPM 키 generate·git 서명 연동 | 물리(칩 밖 미이탈) — M2 와 동일 속성 | ✅ (**비용 0, host 내장**) | host-bound(분실 SPOF 無 / host 재설치 시 소실) | single-host 적격 |
| **(M3) secrets vault** | CT-1~CT-4 | vault 설치·unseal·런타임 중개 client | vault unseal 자격 = credential 재귀 | △ (vault·Hermes 동일 호스트면 약화) | unseal 자격 관리 | 부분 |
| **(M4) Vault HSM / KMS (ST-4)** | CT-1~CT-4 (외부 HSM) | 외부 HSM·KMS·Hermes vault client (인프라 高) | 외부 root — single-host 동일 침해 경계 | ❌ (γ-2: single-host 무력) | 인프라 운영 비용 | **MVP-6 DEFER** |
| **(M5) keyless** (sigstore/gitsign·Rekor, CBI-4) | CT-1/CT-3 (장기 키 *부재*) | OIDC IdP·gitsign·Rekor 로그 | 단명 인증서 — 장기 키 문제 소거 | △ (IdP 의존 = Provider Liquidity 긴장) | **OIDC IdP 새 의존 축** + Rekor↔audit 시너지(§9) | **MVP-6 DEFER** (CBI-4) |

**조합 권고 (`f29c772` §2.4, 권고 한정)**: **물리 격리(M2 *또는* TPM) + ST-3 docker secret + ST-1 file perm** = single-host 1순위. M2 vs TPM = lock-out SPOF 트레이드오프(§5.5). M3/M4/M5 = MVP-6 / multi-host 전환 시.

> **means/ends 경계**: "사람 키가 Hermes 손에 없다"(ends)는 G3 DESIGN 고정, *무엇으로 달성*(M1~M5/TPM)은 means = entry 발효 결정. [[feedback_provider_liquidity]] — 특정 토큰 벤더·IdP 하드코딩 금지, 후보 열거 유지. ends 동등성 열은 후보가 *동일 ends* 를 어디까지 보장하는지의 비교 (§2.1(a)) — *결정* 아님.

---

## 5. ⭐ hardware/TPM key 구조적 흡수 + 한계 + 백업 키 역설

> `f29c772` 가장 무게 있는 교차 발견 (P1/CBI-1) + `cc5b517` BI3-5(흡수 서사 재균형)·CBI3-1(TPM 병치)·CBI3-2(백업 키 역설) 반영.

### 5.1 왜 "구조적 흡수"인가 (재균형 — BI3-5)

- M1(미주입)은 *행위 규칙* 에 가깝다: "사람 키를 컨테이너에 넣지 *말라*". single-host 에서 키는 여전히 *host 어딘가*에 존재하며 동일 호스트 Hermes 가 접근할 *gap* 잔존.
- 물리 격리(M2 hardware key / TPM)는 **개인키가 물리 매체(토큰/칩) 밖으로 *원천적으로 나오지 않는다*.** 서명은 매체 내부에서 일어나고 결과 서명만 반환 → "동일 호스트 공유 gap" *자체가 소멸* (행위 규칙이 아니라 *물리 구조*).
- 하네스 원칙("잘못하는 것이 불가능하게")의 구현 — Hermes 가 키를 *추출하려 해도 불가능*.
- ⚠️ **흡수의 본질 = "물리 격리" *속성* 이지 특정 제품이 아니다** — 외장 토큰(M2)과 내장 칩(TPM) 양쪽이 그 속성을 갖는다 (§5.5 병치).

### 5.2 흡수의 능동 메커니즘 = touch-to-sign / PIN / touch policy (BI3-5)

- 물리 격리는 *키 추출* 을 막지만, Hermes 가 *서명을 자동 트리거* 하는 것은 별개다. 이를 막는 *능동* 메커니즘:
  - **touch policy = `always`**: 서명마다 사람 물리 터치 강제 → Hermes 자동 서명 불가.
  - **user PIN**: 서명 전 PIN 입력 (캐시 정책 주의).
- 이 능동 메커니즘이 흡수의 *결정적* 부분인데 v1 §5 에서 누락 → v2 명시. γ-1 "passive 검증 > active 강제" 철학과 일관 (사람 물리 확인 = passive gate).

### 5.3 (구조 — 5.1 로 통합)

### 5.4 ⭐ 흡수의 한계 = 거짓 안전감 차단 (BI3-5 — §6 동일 강도)

> v1 §5.3 의 짧은 단서를 §6(single-host 한계)과 *동일 강도* 의 독립 명제로 격상.

- 물리 격리(M2/TPM)는 **CT-1/CT-3(서명 키 *추출*)** 한정 흡수. **CT-2(host token)·CT-4(audit write)·서명 *오용*·touch-to-sign 사회공학** 은 흡수하지 *않는다*.
- 특히 **악성 prompt 가 토큰 보유자에게 "정상 작업이니 터치하라"고 유도** 하는 서명 오용은 **host 미침해 상태에서도 성립** → §6(host 침해 중심)으로 흡수 불가, *독립* 위협.
- ⚠️ **금지**: "hardware key 도입 = 서명 안전 *확정*" 거짓 안전감. 물리 격리는 *키 추출 방어* 이지 *서명 오용 전체 방어* 가 아니다 (§6 의 single-host 거짓 안전감과 *별도* 차단).

### 5.5 M2 vs TPM 트레이드오프 (CBI3-1)

| 축 | M2 (YubiKey/FIDO2) | TPM / Secure Enclave |
|----|---------------------|----------------------|
| 격리 강도 | 물리(토큰 밖 미이탈) | 물리(칩 밖 미이탈) — 동일 속성 |
| 비용 | 토큰 구매(백업 포함 2개+) | **0 (host 내장)** |
| 1인 lock-out SPOF | **높음** (분실/파손/도난) | 중 (분실 위협 無 / host 재설치 시 소실) |
| 백업 | 백업 토큰(BI-9) | export 불가 → host 재설치 대비 별도 |
| Provider Liquidity | 토큰 벤더 종속 위험 | OS/하드웨어 종속 |

> M2 1순위 권고(`f29c772` §2.4)는 *기밀성* 관점 최선이나, *가용성·비용 포함 종합* 에서 TPM 이 lock-out SPOF 를 비용 0 으로 우회 — **둘은 동급 1순위 후보로 병치, 결정 = entry 발효**.

### 5.6 백업 키 역설 + lock-out SOP (CBI3-2 / REC-2)

- **lock-out SPOF**: M2 토큰 분실 시 유일 사람이 lock-out (서명 불가 → 전 commit default-deny). 완화 = 백업 키 2개+ (BI-9).
- ⚠️ **백업 키 역설**: 백업 키 N개 등록 = 사람 권위 신호 생성 매체 N개 = **CT-1 공격 표면 N배**. 백업 키 보관처(또 다른 host? 금고?)가 §6 *동일 침해 경계로 회귀* 가능. 백업 키 *분실 추적·폐기(revocation) SOP* 부재 시 도난 백업 키 = silent bypass. **백업 키 = 가용성↑ ⊕ 기밀성↓ 트레이드오프** — *식별* = brief 소관, *정책 고정*(개수·보관·revocation) = entry 결정(§13 #4).
- **성능 (REC-2)**: entrypoint stat(ST-1) = 시작 1회·無의미 지연 / 물리 키 서명 latency = 사람 touch 대기(*자동화 불가가 의도된 설계*) / docker secret(ST-3) = 시작 지연 無 — 전부 수용 가능.

---

## 6. ⭐ single-host 한계 = 동일 침해 경계 = 거짓 안전감 차단

> `f29c772` §4 (B 핵심 → Reviewer 격상) 답습. **BI-3 의 가장 중요한 *비결과* 명시.**

- **"single-host 충족 = 안전 *확정* 아니라 수용된 SPOF 위 *최선*."**
- single-host 에서 사용자 호스트 = Hermes 호스트 = **동일 침해 경계**. 격리(M1~M2/TPM)는 *Hermes 프로세스 내부로부터의 추출* 을 막지만, *host 전체 침해*(계정 탈취·물리 접근) 시 명목화.
- G3 §5.5 SPOF 는 **의도적 수용**(1인 MVP)이며, 본 BI-3 구현은 그 SPOF *안에서의* 최선이다. multi-host / Vault(ST-4, MVP-6)는 §5.5.3 trigger 충족 시에만 진입 (γ-2 DEFER).
- ⚠️ **금지**: BI-3 충족(또는 본 brief 승인)이 "single-host = 안전 확정"으로 오용되는 것을 명시 차단. 진입 적격 ≠ 안전 확정.

---

## 7. GP-3 §5 정합 + N-2 정밀화 + line 정밀화 + BI-4 cross-ref + ST 경계

### 7.1 GP-3 §5 (Credential / Secret Hygiene) 정합

- GP-3 = governance-preconditions.md **§5** "Credential / Secret Hygiene (저장 + 코드)". 위반 경로 = **P3(저장 경로)** + **P4(코드 본문)**.
- BI-3 의 CT-1/CT-3(사람 *서명 키*)는 GP-3 §5 P3(저장 경로) 위생의 *특수·결정적 부분집합* (ST-1~ST-5 = GP-3 P3 저장 격리 수단, BI-3 은 그중 사람 권위 신호 키에 초점).

### 7.2 ⭐ N-2 citation 정밀화 + 정정 대상 명시 (CBI3-4)

> **발견 (3 Agent 독립 grep 검증)**: `f29c772` §1.4 N-2 와 BI-3 원문이 인용한 **"GP-3 §6.2"** 는 governance-preconditions.md 구조와 *불일치* — 그 문서의 **§6 = GP-4(외부 입력 검증), §6.2 = 위반 경로 "P5"** 이며, GP-3(Credential/Secret Hygiene)는 **§5**(line 468).

- BI-3 실제 권위 = **GP-3 §5** (특히 §5 P3 저장 경로 + §5.3 강제 메커니즘).
- **정정 *대상*** = 원 합의 본문 **`f29c772` line 59 / 92 / 158** ("GP-3 §6.2" 3회 인용) + 본 brief §2 인용.
- **정정 권한** = entry 합의 또는 별도 정오 단계 (합의 본문 *자동 갱신 0건* — §0.3 금지). 본 brief 는 *전파하지 않고 정밀화 권고* 만.
- (참고: "G2 노출 차단 / G3 변경 권한 차단" *개념* 은 유효, *§번호* 만 부정확.)

### 7.3 4축 line 번호 표기 정밀화 (REC-5)

- BI-3 4축 DESIGN 위치는 G3 **§3.1.2(provenance check channel)** + **§5.5(SPOF accepted risk)** *섹션* 으로 참조 (line 번호는 후속 68 교정으로 이동했고 brittle — v1 이 인용한 805 는 §5.5.2 일반 SPOF 사유). 본 brief 는 섹션 참조 우선, line 번호는 보조.

### 7.4 GitHub plan/ruleset 가용성 = CT-2 격리 선결 (CBI3-3)

- **CT-2(host token) 격리 실효성**은 "token 이 ruleset 을 끌 수 있는가"에 종속 → **BI-4 (GitHub plan·ruleset 가용성) 가 선결**. CT-2 격리가 "token 최소권한"인지 "ruleset 자체가 token 으로 불가"인지는 plan 가용성(Group α C-4 미해소)에 종속. 별도 BI-4 brief cross-ref (부록 A).

### 7.5 ST-1 / ST-3 / ST-4 경계 (γ-1 / γ-2, 결정 변경 0건)

| ST | 내용 | BI-3 관련 | 경계 |
|----|------|-----------|------|
| **ST-1** | entrypoint stat 검증 (chmod 600) | file perm 격리 | ⚠️ Hermes upstream Dockerfile 변경 = 풀 3+1 trigger (R-MVP1-G3-7) |
| **ST-3** | docker secret 직접 사용 | **single-host canonical** | docker-compose.yml 갱신 (entry 발효) |
| **ST-4** | Vault HSM (ADR-010) | M4 | **MVP-6 DEFER** (γ-2 — single-host 무력, 안전 순이득 음수) |

> **chmod 능동강제 비권고 (γ-1 `9b1f8cd`)**: chmod *능동 강제* 보다 entrypoint **stat 검증(passive)** 권고 — 능동 chmod = Hermes 가 perm *조작* 권한 갖는 역설. 본 brief = γ-1 *재확인* (변경 0건).

---

## 8. 미격리 시 4축 붕괴 + 공급망 P11 + 부분 격리 그라데이션

### 8.1 미격리 시 4축 붕괴 = 순이득 0 (축별)

| 축 | credential 미격리 시 붕괴 | metadata detection 대비 |
|----|--------------------------|------------------------|
| positive allow-list | Hermes 가 CT-1 키로 직접 서명 → "사람 권위 신호" 위조 → default-deny 통과 = FN | **순이득 0** |
| external anchor | Hermes 가 CT-2 token 으로 ruleset off / required check 우회 = anchor 무력 | 순이득 0 |
| audit sink | Hermes 가 CT-4 credential 로 audit 위조/삭제 = tamper-evidence 무력 (BI-5 재귀, §9) | 순이득 0 |
| (전체) | 4축 *구현되어 있으나* 모두 우회 가능 → **거짓 안전감** | **음의 순이득** |

> **순이득 음수 측정 후보 (REC-4)**: "거짓 안전감 → 운영자 경계심 저하 → metadata 시절 대비 *침해 탐지 지연*" 을 측정 가능 기준으로 (구체 수치 = entry threshold, 본 brief 0건). 결론: credential 격리 없는 allow-list/anchor/audit = 순이득 0~음수 → BI-3 = **발효 전 BLOCKING**.

### 8.2 ⭐ 공급망 P11 ↔ credential 격리 (BI3-4)

- credential 격리 메커니즘 자체(env scrub script / entrypoint stat / docker-compose secret 정의 / cap_drop 설정)가 **공급망(악성 base image·tooling·dependency) 변조** 시 무력화 → CT-1~CT-5 *동시 재유입* = 4축 동시 명목화.
- governance §1.2.7 **P11(Supply-chain Compromise)** 의 "GP-3 무력화 위험" cross-reference 를 BI-3 발효 본문에 흡수 의무 (격리는 *공급망 층에서도* 보호되어야 = 거짓 안전감 공간 차원 차단).

### 8.3 ⭐ 부분 격리 그라데이션 (BI3-6)

- 격리는 **binary(격리/미격리)가 아니다.** CT-1~CT-5 *부분집합* 격리 상태(예: CT-1 물리 흡수 ✅ but CT-4 audit write 미격리)에서 4축이 *부분 명목화* 한다.
- **격리 순서(credential→allow-list→anchor→audit)가 *중간 상태 안전* 을 보장하지 않는다** — 오히려 중간 상태 = "일부 격리됐으니 안전"이라는 **가장 위험한 거짓 안전감 구간**. §11.2 Rollback Trigger 에 중간 상태 위험 반영.

---

## 9. audit write credential 재귀 + 완전성 FN 귀속 (BI-5/BI-7 인터페이스)

- **CT-4(audit write credential)** = BI-3 ∩ BI-5 *교집합* — audit sink "Hermes 쓰기 불가"(BI-5)이려면 CT-4 가 Hermes 에 없어야 하고(BI-3 재귀), sink 매체가 append-only/tamper-evident 여야 한다(BI-5 고유).
- ⚠️ **완전성 FN 귀속 (BI3-8)**: CT-4 격리 = audit *위조/삭제* 불가 **한정**. audit 가 *기록하지 않는* 사건(observe mode 통과 FN)은 사후 대조 시 "정상"으로 보임 — 이 **기록 누락 FN = BI-7(observe 면책) / BI-5(sink) 소속** 이지 CT-4 격리로 닫히지 *않는다*. "CT-4 격리 = audit 완전" 오용 차단.
- **Rekor 시너지 (BI3-7)**: M5(keyless) 채택 시 Rekor 투명성 로그 = append-only = BI-5 audit sink 와 *동일 인프라 시너지* (CBI-4 DEFER, 후보 보존).
- 본 brief 범위 = CT-4 의 *credential 측면* 만. sink 매체 구성 = BI-5 심화 단위 (silent scope expansion 차단).

---

## 10. 영구 핵심 제약 보존 + source-of-truth 인터페이스

| 제약 | BI-3 guardrail |
|------|---------------|
| **Hermes ≠ root of trust** (#1) | CT-1~CT-5 모두 Hermes 미주입. Hermes 가 *어느 격리 대상이든* 획득하면 = root of trust 화 = BLOCKING |
| **Provider Liquidity** (5-way) | 격리 *수단*(토큰 벤더·secret source·git host·**OIDC IdP[M5]**)을 하드코딩 금지 — M1~M5/TPM 후보 열거 유지, 환경 종속. [[feedback_provider_liquidity]] |
| **means/ends (ADR-011 §2.1)** | "사람 키가 Hermes 손에 없다"=ends(고정), 격리 *방식*=means(entry 결정). ends 동등성 비교표(§4) = (a) 충족 |
| **단일 source-of-truth** (#4) + **Evidence Ledger** (REC-6) | credential 격리 무너지면 4축 명목화 = SoT(사람 권위) 위조 가능. **CT-4 격리 ↔ Evidence Ledger `agent="user"`(ADR-012)·audit forge 방지(G3 §3.1.2)** 인터페이스 — audit 무결성이 CT-4 격리에 의존 |

---

## 11. 진입 gate + Rollback Trigger + credential observe binary

### 11.1 진입 gate

| # | gate | 충족 | 비고 |
|---|------|------|------|
| BG-1 | BI-3 = 합의 확정 (최강 BLOCKING, 4축 선결 전제) | ✅ | `f29c772` §2.2 |
| BG-2 | 격리 대상(CT-1~CT-5) + 구체 우회 표면 enumeration | ✅ (§3) | BI3-1/BI3-2 반영 |
| BG-3 | 격리 수단 후보 비교 (M1~M5/TPM, 0-구현·ends 동등성) | ✅ (§4) | 결정 = entry 발효 |
| BG-4 | single-host canonical(ST-3+ST-1) 적격 / ST-4 DEFER | ✅ | γ-1 / γ-2 |
| BG-5 | 물리 흡수 + 한계(거짓 안전감) + 백업 키 역설 식별 | ✅ (§5) | 백업 키 정책 = 구현 결정 |
| BG-6 | 실 구성(env scrub/socket/cap_drop/docker secret) | ⏳ | **구현 entry 발효 + Evidence** (본 brief 범위 밖) |

> **결론(권고)**: BI-3 *결정 공간*(대상·우회 표면·수단 후보·흡수·한계·공급망·그라데이션)이 정비됨 → credential 수단 *결정* = 구현 entry 발효 합의(풀 3+1) 권한.

### 11.2 Rollback Trigger (R-I-IMPL-BOUNDARY 답습 + BI3-6 반영)

구현 중 다음 발견 시 rollback + alert: (i) Hermes 가 CT-1~CT-5 획득 (Hermes≠root 위반) / (ii) hardware/TPM key 채택 후 백업 키 부재 lock-out 방치 (BI-9) / (iii) 격리 수단 본문 고정(CN-6) / (iv) single-host 한계·물리 흡수 한계가 "안전 확정"으로 오용(거짓 안전감, §5.4/§6) / (v) chmod 능동강제로 Hermes perm 조작 권한(γ-1) / (vi) **공급망 변조로 격리 메커니즘 무력(§8.2)** / (vii) **부분 격리 중간 상태 방치(§8.3 — 일부 격리=안전 오인)**.

### 11.3 credential observe = binary 성격 (REC-1)

- credential 격리의 observe mode 는 allow-list 의 *statistical* observe(FP_rate 관찰)와 **성격이 다르다** — 격리는 *binary*(주입=즉시 violation)다.
- 전환 gate 후보: "**Hermes 키 접근 시도 telemetry 0건 N일**" 형태 (구체 N = threshold, 본 brief 0건). allow-list observe 와 *분리* 정의 필요.

---

## 12. 합의 형태 (풀 3+1 의무)

- **credential 수단 결정 = 풀 3+1 *의무*, Reviewer-only 부적격** — BI-3 = T3 보안 enforcement 최강 BLOCKING + 핵심 제약 #1 직결 (`f29c772`/`cc5b517` §2.1). 본 brief v2 승인 후 credential 결정 = 구현 entry 발효 합의에 통합 또는 BI-3 단독 합의 분리 — 형태 결정 = 사용자 명시.
- **2차 vendor**: trigger #7 = Group I 외부 GPT-5.5 1건 기 충족. BI-3 단계 추가 = 사용자 결정(의무 아님).

---

## 13. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 |
|------|------|------|
| **(A)** | 본 brief v2 승인 → **credential 수단 결정 합의 진입** (풀 3+1 — M1~M5/TPM 中 결정 + BI-3 충족 검증 + 백업 키 정책) | 합의 보고서 작성 |
| (B) | 본 brief v2 일부 수정 → v3 | v3 작성 |
| (C) | 본 brief v2 승인 → commit *까지만* | 1 commit |
| (D) | 보류 → 다른 BLOCKING 심화 (BI-4 anchor·plan 가용성 / BI-1 CI fingerprint / BI-5 audit) | 별도 brief |
| (E) | 보류 → 다른 backlog (tmux 도입 / G1 PR·approval auto-reject / 2차 vendor / GP-5 C-2 Backlog #4) | 별도 brief |
| (F) | 세션 종료 | — |

> 본 brief v2 = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). credential 수단 결정 / hardware·TPM key 채택 / 백업 키 정책 / 실 구성 = 사용자 명시 승인 후 별도 단계. 구현 = **R-I-IMPL-BOUNDARY → Backlog #6 + 별도 풀 3+1**.

---

## 14. 한 단락 요약

**(v2 = `cc5b517` BI-3 brief 검증 풀 3+1 합의 BLOCKING BI3-1~BI3-8 + 조건부 4 + 권고 6 반영판.)** `8e57f7b` Group I 구현 entry 합의의 **최강 BLOCKING BI-3("credential 격리 = 4축 공통 선결 전제", 우선순위 1)** 를 단독 심화한 brief 의 v2 — (§2) BI-3 = 나머지 3축이 모두 "사람/admin credential Hermes 미주입"에 독립 수렴하는 *상위 전제*, 미격리 시 4축 명목화 + 순이득 0(거짓 안전감 = 음의 순이득), (§3) 격리 대상 **CT-1~CT-5(BI3-1 = GP-5 T-n 충돌 회피 재명명)** + **구체 우회 표면(BI3-2 = /proc·ptrace / child env 상속 / bind mount / credential helper / docker socket=host escape 최치명)**, (§4) 수단 후보 M1(미주입)·**M2(hardware key)·TPM(CBI3-1 동급 병치)**·M3(vault)·M4(ST-4 DEFER)·**M5(keyless sigstore/Rekor, BI3-7 보존)** 비교 + **"0-구현 아님"·"ends 동등성" 컬럼(BI3-3, ADR-011 §2.1(a))**, (§5) ⭐ 물리 격리(M2/TPM)가 키를 매체 밖에 두지 않아 구조적 흡수(harness 원칙)하되 **(BI3-5) 흡수 = CT-1/CT-3 *키 추출* 한정·서명 오용/touch-to-sign(host 미침해서도 성립)은 별개 = §6 동일 강도 거짓 안전감 차단** + touch policy 능동 메커니즘 + (CBI3-2) **백업 키 역설(가용성↑ ⊕ 기밀성↓ 공격 표면 N배·revocation SOP)**, (§6) single-host = 동일 침해 경계 = "수용된 SPOF 위 최선", (§7) GP-3 §5 정합 + **(CBI3-4) N-2 "GP-3 §6.2"→§5 정밀화 + 정정 대상 = 원 합의 `f29c772` line 59/92/158 명시(자동 갱신 0건)** + line 표기 정밀화 + **(CBI3-3) BI-4 plan 가용성 = CT-2 격리 선결 cross-ref**, (§8) 미격리 4축 붕괴 + **(BI3-4) 공급망 P11 ↔ 격리 메커니즘 무력** + **(BI3-6) 부분 격리 그라데이션(중간 상태 = 가장 위험한 거짓 안전감)**, (§9) CT-4 = BI-3∩BI-5 재귀 + **(BI3-8) audit 위조/삭제 격리 ≠ 기록 누락 FN(BI-7/BI-5 소속)** + Rekor 시너지, (§10) Hermes≠root·Provider Liquidity(IdP 포함)·means/ends·SoT·Evidence Ledger 인터페이스, (§11) 진입 gate + Rollback Trigger(공급망·중간상태 추가) + credential observe = binary 성격으로 정비. 본 brief v2 는 결론을 *선취하지 않으며* — 격리 수단 *결정*·hardware/TPM key *채택*·백업 키 *정책 고정*·실 구성·실 hook·ruleset·CI·audit sink·sigstore/Rekor 도입·Vault ST-4 진입·Operational Readiness PASS·Hermes PMO 격상·원 합의 본문 자동 정정·commit·push = **모두 0건** 이며 사용자 명시 + 별도 단계다.

---

## 부록 A — 답습 출처

| 출처 | 답습 영역 |
|------|----------|
| **`3plus1-consensus-2026-05-21-bi-3-credential-isolation.md` (`cc5b517`) BI3-1~BI3-8 + CBI3-1~4 + REC-1~6** | **v2 BLOCKING 반영 (변경 이력 + §3.2 + §4 + §5 + §7.2 + §8.2/8.3 + §9 + §11)** |
| `3plus1-consensus-2026-05-21-group-i-provenance-check-implementation-entry.md` (`8e57f7b`/`f29c772`) BI-3 + CBI-1 + N-1 + §2.4 + §4 | BI-3 정의·수단 권고·거짓 안전감·hardware 흡수·백업 키 (§2·§4·§5·§6) |
| `group-i-provenance-check-implementation-boundary-brief.md` (`596f866`) §3·§4 | 4축 매핑·single-host vs MVP-6 경계 (§4·§7) |
| `hermes-not-root-of-trust-runtime.md` (`708bc0e`) §3.1.2·§5.5 4축 | DESIGN 입력·동일 침해 경계 (§2·§6·§7.3) |
| `governance-preconditions.md` §5 (GP-3, P3/P4) + §1.2.7 P11 | GP-3 정합·N-2 정밀화·공급망 (§7·§8.2) |
| `backlog3-groupgamma1-st1` (`9b1f8cd`, ST-1) / `backlog3-groupgamma2-st4-vault-hsm` (`2e9d46b`, ST-4 DEFER) | chmod 비권고 / ST-4 DEFER (§5·§7.5) |
| `implementation-runtime-roadmap-mvp1.md` (ST-1~ST-5 + GP-5 T-1~T-6) | ST 경계 + CT-n 재명명 근거 (§3·§7.5) |
| **BI-4 GitHub plan/ruleset 가용성 brief (미작성, T-2 격리 선결, Group α C-4)** | CT-2 격리 선결 cross-ref (§7.4) |
| ADR-011 §2.1 (means/ends) + ADR-012 (`agent="user"`) + [[feedback_provider_liquidity]] | §4·§10 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**credential isolation 실 구성** (사람 signing key·token·SSH/GPG agent socket 미주입 / env scrub / socket 미마운트 / `cap_drop` / docker secret 정의 / chmod·entrypoint stat 본문) / **hardware·TPM-backed key 채택 결정·토큰 벤더·IdP 고정·백업 키 정책 고정** (CBI-1/BI-9/CBI3-1/CBI3-2) / **실 hook 구현** (pre-commit / pre-receive / git server-side / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / paths 필터) / **filesystem ACL·`read_only` mount·audit sink 실 구성** / **sigstore·Rekor 실 도입** (M5/CBI-4 DEFER) / **Hermes runtime·upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR / ST-1·ST-5 진입) / **Vault HSM ST-4 진입** (γ-2 DEFER MVP-6) / 수단 결정 고정 (격리 방식·키 매체·secret source — CN-6) / threshold 고정 (observe mode 기간) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 재변경 (§3.1.2/§5.5 4축) / GP-3 본문 변경 / ADR 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** (N-2/line 번호 = 권고 한정, entry/정오 단계 권한) / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / G1 (PR·approval auto-reject) 신규 단위 자동 진입 (Group α C-2 별도 단위) / Backlog #4 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
