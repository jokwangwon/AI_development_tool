# BI-3 Credential 격리 brief — 4축 공통 선결 전제 심화 (DRAFT v1)

> **본 brief = Group I 구현 entry 합의(`f29c772`, R-I-IMPL-BOUNDARY)의 *최강 BLOCKING* BI-3("credential 격리 = 4축 공통 선결 전제")를 *단독 심화* 하는 brief 한정.** 본 brief 의 어떤 §도 그 자체로 실 hook(pre-commit / pre-receive) / GitHub ruleset·branch protection / CI provenance step / filesystem ACL·`read_only` mount·`cap_drop` / **credential isolation(사람 키 Hermes 미주입) 실 구성** / audit sink 구현 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 을 발생시키지 않는다. 본 brief = **격리 대상·수단 후보·구조적 흡수·single-host 한계·진입 gate·합의 형태 정비** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v1** (BI-3 단독 심화 — 실 구현 미진입, 수단 결정 0건)
**진입 단위**: Group I 구현 entry 합의 후속 #1 (`f29c772` 합의 §2.2 BI-3 = 우선순위 **1**·최강 BLOCKING / §2.4 credential 축 수단 권고 / §0 종합판정 (2)(3))
**선행 발효 답습**: `8e57f7b` Group I 구현 entry 합의 발효 (APPROVE WITH CONDITIONS, BI-1~BI-10 + CBI-1~CBI-4) + `596f866` Group I 구현 경계 brief (R-I-IMPL-BOUNDARY) + `708bc0e` G3 provenance check 4축 DESIGN + γ-1 `9b1f8cd`(ST-1) · γ-2 `2e9d46b`(ST-4 DEFER) + GP-3 §5 (Credential/Secret Hygiene) + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **`f29c772` BI-3 + CBI-1 + §2.4 credential 행 + §4 거짓 안전감 차단 + §1.4 N-2/N-7** + boundary brief §3 credential 행·§4 경계 + γ-1/γ-2 결정 + GP-3 §5 P3 저장 경로
**합의 권위 한계**: 본 brief = BI-3 *심화* DRAFT — 격리 수단 *결정 고정*·hardware key 채택 *결정*·백업 키 정책 *고정*·실 구성(env scrub / socket 미마운트 / cap_drop / docker secret)은 별도 구현 entry 발효(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "BI-3 credential 격리 brief"

본 brief = 위 명령 답습 — **BI-3(credential 격리) 단독 심화** = (i) 격리 *대상* enumeration (무엇을 Hermes 에서 떼는가) + (ii) 격리 *수단 후보* 비교(means/ends, 결정 0건) + (iii) ⭐ hardware-backed key 구조적 흡수 + 부작용(1인 lock-out → 백업 키) + (iv) single-host 한계(동일 침해 경계 = 거짓 안전감 차단) + (v) GP-3 §5 / ST-1·ST-3·ST-4 정합 + N-2 citation 정밀화 + (vi) 미격리 시 4축 붕괴(순이득 0) + (vii) 진입 gate + 합의 형태 — **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 — 구현 entry 합의(후속 69)에서 BI-3 = 우선순위 1·최강 BLOCKING (§1)
2. BI-3 정의 재확인 — credential 격리 = 4축 공통 선결 전제 (§2)
3. 격리 *대상* enumeration — 무엇을 Hermes 환경에서 떼어내는가 (§3)
4. ⭐ 격리 *수단 후보* 비교 (means/ends — 결정 = entry 발효, CN-6) (§4)
5. ⭐ hardware-backed key 구조적 흡수 분석 + 부작용(1인 lock-out SPOF → 백업 키 BI-9) (§5)
6. ⭐ single-host 한계 = 동일 침해 경계 = "충족=안전 확정 아님, 수용된 SPOF 위 최선" (§6)
7. GP-3 §5 정합 + ST-1/ST-3/ST-4 경계 + chmod 능동강제 비권고(γ-1) + **N-2 citation 정밀화** (§7)
8. 미격리 시 4축 붕괴 = 순이득 0 (축별 분석) (§8)
9. audit write credential 재귀 (BI-5 인터페이스) (§9)
10. 영구 핵심 제약 보존 (§10)
11. 진입 gate + Rollback Trigger (§11)
12. 합의 형태 (풀 3+1 의무) (§12)
13. 다음 단계 (§13)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **credential isolation 실 구성** (사람 signing key·token·SSH/GPG agent socket Hermes 미주입 / env scrub / socket 미마운트 / `cap_drop` / docker secret 정의 / chmod·entrypoint stat 본문)
- ❌ **hardware-backed key 채택 *결정*** / 토큰 종류(YubiKey/FIDO2 등) 고정 / **백업 키 정책 고정** (개수·등록 절차 — CBI-1/BI-9, 결정 = entry 발효)
- ❌ **실 hook 구현** (pre-commit / pre-receive / CI provenance step 본문)
- ❌ **GitHub ruleset / branch protection 변경** / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / paths 필터 — [[feedback_actual_run_trigger_paths_filter]] 답습 의무)
- ❌ **filesystem ACL / `read_only` mount / audit sink 실 구성**
- ❌ Hermes runtime / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR — ST-1/ST-5 진입 = 풀 3+1 trigger)
- ❌ **Vault HSM ST-4 진입** (γ-2 BLOCK/DEFER MVP-6 답습)
- ❌ **수단 *결정 고정*** (격리 방식·키 매체·secret source — CN-6/means-ends, 결정 = entry 발효)
- ❌ threshold 고정 (observe mode 기간 등)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)**
- ❌ Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경
- ❌ G3 본문 재변경 (특히 line 360/784/805 4축) / GP-3 본문 변경 / ADR·합의 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경
- ❌ 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. 격리 대상·수단 후보·구조적 흡수·한계·gate 는 *심화/정비/권고* 이며, 격리 수단 *결정*·hardware key *채택*·백업 키 *정책 고정*·실 구성 *발효* 는 구현 entry 합의(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다. `f29c772` 합의가 이미 (i) BI-3 = 최강 BLOCKING, (ii) credential 격리 = 4축 공통 선결 전제, (iii) hardware-backed key 흡수 + 백업 키 부작용, (iv) single-host = 수용된 SPOF 위 최선 을 **권고로 확정**했으므로, 본 brief 는 그 권고를 *BI-3 단독 결정 공간으로 환원* 하는 심화일 뿐 *결정* 하지 않는다.

---

## 1. 진입 맥락 — BI-3 = 우선순위 1 · 최강 BLOCKING

```
후속 68 (708bc0e) ─ G3 provenance check 4축 DESIGN 발효
        ▼
후속 69 (8e57f7b) ─ Group I 구현 entry 합의 (APPROVE WITH CONDITIONS, BI-1~BI-10)
        │              · BI-3 = 우선순위 1 (credential > anchor > … )
        │              · 3 Agent 독립 수렴: credential 격리 = 4축 공통 선결 전제
        ▼
⭐ 본 brief ─ BI-3 *단독 심화* (격리 대상·수단 후보·구조적 흡수·한계, 실 변경 0건)
        ▼ (승인)
구현 entry 발효 합의 (풀 3+1) ─ credential 수단 *결정* (BI-3 충족 검증) + 나머지 BLOCKING 통합
        ▼ (승인)
실 구성 + Evidence ─ 미주입/env scrub/socket/cap_drop/docker secret (Implementation Evidence PASS)
```

- **BI-3 우선순위 = 1** (`f29c772` §2.2: `credential(BI-3) > anchor(BI-4) > BI-1/BI-2 > BI-5 > BI-9 > BI-6/7/8/10`). 순서(만장일치): **credential(hardware 흡수) → allow-list 정의 → external anchor → audit**.
- **왜 최강인가**: 합의 §0 (2)(3) — 나머지 3축(positive allow-list / external anchor / audit sink)이 *모두* "Hermes 환경에 사람/admin credential 미주입"에 **독립 수렴**. 즉 credential 격리는 다른 축의 *상위 전제* 이며, 미격리 시 다른 축을 *구현해도* 명목화된다.
- 본 brief = BI-3 을 *먼저* 심화하여, 후속 allow-list/anchor/audit 심화의 *공통 기반* 을 정비하는 단위 (합의 권고 순서 답습).

---

## 2. BI-3 정의 재확인 (`f29c772` 답습, 본문 변경 0건)

> **BI-3 (원문):** "credential 격리 = 4축 공통 선결 전제 — 사람 signing key·token·SSH/GPG agent Hermes 미주입(env scrub + socket 미마운트 + cap_drop). 미격리 시 4축 명목화 + 순이득 0 + 거짓 안전감. host 침해 한계 명시. GP-3 §6.2 권위(N-2)."

핵심 명제 3개:

1. **선결 전제성**: credential 격리는 4축 중 하나가 *아니라* 나머지 3축이 작동하기 위한 *상위 전제* 다. (positive allow-list 가 검증하는 "사람 권위 신호"를 Hermes 가 위조할 수 없어야 = 사람 키가 Hermes 손에 없어야 함.)
2. **미격리 = 순이득 0**: credential 미격리 시 4축 전부 명목화하며, **metadata-기반 single-author detection(G3 결함의 출발점) 대비 순이득이 0** 이다 (오히려 "4축이 있으니 안전"이라는 *거짓 안전감* 만 추가 = 음의 순이득).
3. **host 침해 한계**: single-host 에서 사용자 호스트 = Hermes 호스트 = 동일 침해 경계. 격리는 *Hermes 프로세스 내부* 로부터의 추출은 막지만 *host 전체 침해* 는 막지 못한다 → 한계 명시 의무 (§6).

---

## 3. 격리 *대상* enumeration — 무엇을 Hermes 환경에서 떼는가

> credential 격리는 추상어가 아니라 *구체 대상* 의 집합이다. 아래는 격리 대상 후보의 enumeration (실 구성 0건 — 무엇을 떼는지의 *식별* 만).

| # | 격리 대상 | 떼지 않으면 발생하는 위조 경로 | 4축 중 무력화 대상 |
|---|----------|------------------------------|-------------------|
| T-1 | **사람 signing key** (GPG private / SSH signing private) | Hermes 가 사람 서명을 직접 생성 → positive allow-list 통과 = "사람 권위 신호" 위조 | positive allow-list |
| T-2 | **git host token / PAT / OAuth credential** (push·ruleset·CI 권한) | Hermes 가 ruleset 끄기·required check 우회·force push → external anchor 무력 | external anchor |
| T-3 | **SSH agent socket / GPG agent socket** (forwarded·mounted) | 키 파일이 없어도 agent 를 통해 *서명 요청* 가능 → T-1 우회 | positive allow-list |
| T-4 | **audit sink write credential** (append-only remote 쓰기 token) | Hermes 가 audit 위조/삭제 → tamper-evidence 무력 (BI-5 재귀, §9) | audit sink |
| T-5 | **CI/runner 환경 내 위 credential 의 잔존** (env var·`~/.ssh`·`~/.gnupg`·keychain) | CI step 이 Hermes 와 동일 신뢰 경계면 T-1~T-4 재유입 (BI-1 workflow read-only 의존) | 전 축 |

> ⚠️ **T-1 ≠ GP-3 P3 일반 secret**: GP-3 §5 P3(저장 경로)은 "Hermes *앱이 쓰는* secret(API 키 등)"의 위생이다. BI-3 의 핵심은 그보다 좁고 결정적인 **사람의 *권위 신호* 생성 키**(T-1/T-3)다 — 이것이 Hermes 에 있으면 allow-list 자체가 무의미하므로 4축 전체의 선결 전제가 된다. 둘은 *겹치되 동일하지 않다* (§7 정합).

---

## 4. ⭐ 격리 *수단 후보* 비교 (means/ends — 결정 0건, CN-6)

> 본 §4 = 수단 *후보 비교* 한정. 어느 수단을 *채택* 할지 = 구현 entry 발효(CN-6). 본문 고정 = §0.3 금지. 후보 = `f29c772` §2.4 credential 행 + boundary brief §3 + γ-1/γ-2 답습.

| 수단 후보 | 격리 범위 (T-1~T-5) | single-host 적격 | 부작용 / 한계 | MVP 경계 |
|----------|---------------------|------------------|---------------|----------|
| **(M1) Hermes 컨테이너 사람 키 미주입** (env scrub + agent socket 미마운트 + `cap_drop`) | T-1/T-3 부분 (파일·socket 미제공) | ✅ (ST-3 docker secret + ST-1 file perm, γ-1) | host 침해 시 host 의 키에 접근 가능 = 동일 침해 경계 한계 (§6). 키가 *어딘가 host* 에 존재 | **single-host canonical** |
| **(M2) hardware-backed key** (YubiKey / FIDO2 — 키가 물리 토큰 밖 미이탈) | **T-1/T-3 구조적 흡수** (§5) | ✅ (토큰 = 사용자 물리 보유) | **1인 lock-out 가용성 SPOF** → 백업 키 의무(BI-9/CBI-1) | single-host 적격 (흡수) |
| **(M3) secrets vault** (런타임 secret 중개) | T-1~T-4 (vault 가 키 보관·중개) | △ (single-host = vault·Hermes 동일 호스트면 약화) | vault unseal 자격 = credential 재귀 | 부분 (single-host 제한적) |
| **(M4) Vault HSM / KMS-backed (ST-4)** | T-1~T-4 (외부 HSM) | ❌ (γ-2: single-host 무력 — external root/auto-unseal 동일 침해 경계, 안전 순이득 음수) | 인프라 운영 비용 高 | **MVP-6 DEFER** (γ-2 `2e9d46b`) |

**조합 권고 (`f29c772` §2.4, 권고 한정)**: **hardware-backed key(M2) + ST-3 docker secret + ST-1 file perm** = single-host 1순위. M3/M4 = MVP-6 / multi-host 전환 시.

> **means/ends 경계**: 위 표의 *어느 행도* 본문 고정이 아니다. "사람 키가 Hermes 손에 없다"(ends)는 G3 DESIGN 에 고정되었고, *무엇으로 그것을 달성하는가*(M1~M4)는 means = entry 발효 결정. [[feedback_provider_liquidity]] — 특정 토큰 벤더(YubiKey 등) 하드코딩 금지, 후보 열거 유지.

---

## 5. ⭐ hardware-backed key 구조적 흡수 + 부작용

> `f29c772` 가장 무게 있는 교차 발견 (C 명시 / A harness 원칙 수렴 / B 안전 우선순위 수렴 — P1/CBI-1).

### 5.1 왜 "구조적 흡수"인가

- M1(미주입)은 *행위 규칙* 에 가깝다: "사람 키를 컨테이너에 넣지 *말라*". 그러나 single-host 에서 사람 키는 여전히 *host 어딘가*(keychain / `~/.ssh` / agent socket)에 존재하며, 동일 호스트의 Hermes 가 그 경로를 공유·접근할 *gap* 이 남는다.
- M2(hardware-backed key)는 **개인키가 물리 토큰(YubiKey/FIDO2) 밖으로 *원천적으로 나오지 않는다*.** 서명은 토큰 내부에서 일어나고 결과 서명만 반환된다. 따라서 "동일 호스트 keychain/agent socket 공유 gap" *자체가 소멸* 한다 — 행위 규칙이 아니라 *물리 구조* 가 격리를 보장.
- 이는 하네스 원칙("에이전트에게 하라고 말하지 말고, 잘못하는 것이 불가능하게 만들어라")의 정확한 구현 — Hermes 가 사람 키를 *추출하려 해도 불가능* (feedforward 를 물리 매체에 못박음).

### 5.2 부작용 = 1인 lock-out 가용성 SPOF (BI-9 / N-7)

- single-host = 1인 운영. hardware token 이 *분실·파손·도난* 되면 **유일한 사람이 자기 저장소에서 lock-out** 된다 (서명 불가 → 모든 commit 가 allow-list 미통과 → default-deny).
- 보안 격리(기밀성)를 올리면서 *가용성* SPOF 를 새로 만든다 = 트레이드오프.
- **완화 = 백업 키 의무** (BI-9): 2개+ hardware token 등록 (주 토큰 + 백업 토큰). 백업 키 *개수·등록 절차·복구 SOP* = 구현 결정 (§13 #4, 본 brief 결정 0건).

### 5.3 흡수의 한계 (거짓 안전감 차단)

- hardware key 는 **T-1/T-3(서명 키)** 를 구조적으로 흡수하나 **T-2(host token)·T-4(audit write)** 는 자동으로 흡수하지 않는다 — 이들은 별도 격리(§3) 필요.
- 또한 host 전체 침해 시 공격자가 *물리 토큰 보유자에게 서명을 시키는* 경로(touch-to-sign 우회·악성 prompt)는 별개 위협 — hardware key 는 *키 추출* 을 막지 *서명 오용* 전체를 막지 않는다. → §6 한계로 흡수.

---

## 6. ⭐ single-host 한계 = 동일 침해 경계 = 거짓 안전감 차단

> `f29c772` §4 (B 핵심 → Reviewer 격상) 답습. **본 §6 = BI-3 의 가장 중요한 *비결과* 명시.**

- **"single-host 충족 = 안전 *확정* 아니라 수용된 SPOF 위 *최선*."**
- single-host 에서 사용자 호스트 = Hermes 호스트 = **동일 침해 경계**. credential 격리(M1~M2)는 *Hermes 프로세스 내부로부터의 추출* 을 막지만, *host 전체가 침해* 되면 (사용자 계정 탈취·물리 접근) 격리는 명목화된다.
- G3 §5.5 SPOF 는 **의도적 수용**(1인 MVP)이며, 본 BI-3 구현은 그 SPOF *안에서의* 최선이다. multi-host / Vault(ST-4, MVP-6)는 §5.5.3 trigger 충족 시에만 진입 (γ-2 DEFER).
- ⚠️ **금지**: BI-3 충족(또는 본 brief 승인)이 "single-host = 안전 확정"으로 오용되는 것을 명시 차단. 진입 적격 ≠ 안전 확정. (이 한계 자체가 BI-3 의 발효 본문에 명문화될 후보.)

---

## 7. GP-3 §5 정합 + ST 경계 + chmod 비권고 + ⭐ N-2 citation 정밀화

### 7.1 GP-3 §5 (Credential / Secret Hygiene) 정합

- GP-3 = governance-preconditions.md **§5** "Credential / Secret Hygiene (저장 + 코드)". 위반 경로 = **P3(저장 경로)** + **P4(코드 본문)**.
- BI-3 의 격리 대상 T-1/T-3(사람 *서명 키*)는 GP-3 §5 P3(저장 경로) 위생의 *특수·결정적 부분집합* 이다. ST-1~ST-5(아래)는 GP-3 P3 저장 경로 격리의 *수단* — BI-3 은 그중 사람 권위 신호 키에 초점.

### 7.2 ⭐ N-2 citation 정밀화 (provenance 정확성)

> **발견**: `f29c772` §1.4 N-2 와 BI-3 원문이 인용한 **"GP-3 §6.2"** 는 governance-preconditions.md 의 실제 구조와 *불일치* 한다 — 그 문서의 **§6.2 는 GP-4(외부 입력 검증)의 위반 경로 "P5"** 이며, GP-3(Credential/Secret Hygiene)는 **§5** 다.

- BI-3 의 실제 권위 출처 = **GP-3 §5** (특히 §5 P3 저장 경로 + §5.3 강제 메커니즘[docker secret / chmod 600 / entrypoint stat / inotify]).
- 본 brief 는 이 citation 을 *전파하지 않고 정밀화* — 구현 entry 발효 시 "GP-3 §6.2" → **"GP-3 §5 (P3 저장 경로)"** 로 정정 권고 (합의 본문 자동 갱신 0건, §0.3 금지; 정정은 entry 합의 또는 합의 정오 단계의 권한).
- (참고: "G2 노출 차단 / G3 변경 권한 차단" 이라는 N-2 부기는 GP-3 이 G2 게이트 소속이고 G3 변경 권한과 인터페이스한다는 *개념* 은 유효하나, *§번호* 가 부정확.)

### 7.3 ST-1 / ST-3 / ST-4 경계 (γ-1 / γ-2 답습, 결정 변경 0건)

| ST | 내용 | BI-3 관련 | 경계 |
|----|------|-----------|------|
| **ST-1** | Hermes Dockerfile entrypoint stat 검증 (chmod 600 강제) | file perm 격리 (single-host) | ⚠️ Hermes upstream Dockerfile 변경 = 풀 3+1 trigger (R-MVP1-G3-7) |
| **ST-3** | docker secret 직접 사용 (file system 노출 회피) | **single-host canonical** | docker-compose.yml 갱신 (entry 발효) |
| **ST-4** | Vault HSM 통합 (ADR-010) | M4 | **MVP-6 DEFER** (γ-2 `2e9d46b` — single-host 무력, 안전 순이득 음수) |

> **chmod 능동강제 비권고 (γ-1 `9b1f8cd` 답습)**: γ-1(ST-1)은 chmod 를 *능동 강제* 하기보다 entrypoint **stat 검증(passive)** 을 권고 — 능동 chmod 는 Hermes 가 perm 을 *조작* 하는 권한을 갖는 역설 위험. 본 brief 는 이 γ-1 결정을 *재확인* 만 (변경 0건).

---

## 8. 미격리 시 4축 붕괴 = 순이득 0 (축별)

> BI-3 의 "미격리 시 4축 명목화 + 순이득 0 + 거짓 안전감"을 축별로 분해 (`f29c772` C2/P2).

| 축 | credential 미격리 시 붕괴 양상 | metadata detection 대비 |
|----|-------------------------------|------------------------|
| positive allow-list | Hermes 가 사람 키(T-1)로 직접 서명 → "사람 권위 신호" 위조 → default-deny 통과. allow-list 가 *통과시키는* 신호를 공격자가 생성 가능 = FN | **순이득 0** (metadata 비교와 동일한 FN, 위조 난이도만 명목 상승) |
| external anchor | Hermes 가 host token(T-2)으로 ruleset off / required check 우회 = anchor 무력 | 순이득 0 (anchor 가 명목) |
| audit sink | Hermes 가 audit write credential(T-4)로 위조/삭제 = tamper-evidence 무력 (BI-5 재귀) | 순이득 0 (audit 가 명목) |
| (전체) | 4축이 *구현되어 있으나* 모두 우회 가능 → "4축이 있으니 안전"이라는 **거짓 안전감** | **음의 순이득** (잘못된 신뢰 추가) |

> 결론: credential 격리 없이 allow-list/anchor/audit 를 구현하는 것은 *순이득 0~음수* — 따라서 BI-3 = **발효 전 BLOCKING** (선 격리, 후 나머지 축).

---

## 9. audit write credential 재귀 (BI-5 인터페이스)

- T-4(audit sink write credential)는 BI-3 와 BI-5 의 *교집합* 이다 — audit sink 가 "Hermes 쓰기 불가"(BI-5)이려면 *audit write 자격증명* 이 Hermes 에 없어야 하고(credential 격리 = BI-3 재귀), 동시에 sink 매체가 append-only/tamper-evident 여야 한다(BI-5 고유).
- 본 brief 는 T-4 를 BI-3 격리 대상에 *포함* 시키되, sink 매체 구성(append-only git remote / 외부 read-only mount)은 **BI-5 심화 단위** 로 분리 (silent scope expansion 차단). 본 brief 범위 = T-4 의 *credential 측면* 만.

---

## 10. 영구 핵심 제약 보존

| 제약 | BI-3 guardrail |
|------|---------------|
| **Hermes ≠ root of trust** (#1) | 사람 키·token·audit write credential 모두 Hermes 미주입. Hermes 가 *어느 격리 대상이든* 획득하면 = root of trust 화 = BLOCKING |
| **Provider Liquidity** (5-way) | 격리 *수단*(토큰 벤더·secret source·git host)을 하드코딩 금지 — M1~M4 후보 열거 유지, 환경 종속(local/CI/Docker, GHES≠GitHub.com). [[feedback_provider_liquidity]] |
| **means/ends (ADR-011 §2.1)** | "사람 키가 Hermes 손에 없다"=ends(G3 DESIGN 고정), 격리 *방식*=means(entry 발효 결정) |
| **단일 source-of-truth** (#4) | credential 격리가 무너지면 4축이 명목화 = source-of-truth(사람 권위)가 위조 가능 → 격리 = SoT 보존의 물리 기반 |

---

## 11. 진입 gate + Rollback Trigger

### 11.1 진입 gate (BI-3 심화 → credential 수단 결정)

| # | gate | 충족 | 비고 |
|---|------|------|------|
| BG-1 | BI-3 = 합의 확정 (최강 BLOCKING, 4축 선결 전제) | ✅ | `f29c772` §2.2 |
| BG-2 | 격리 대상 enumeration (T-1~T-5) | ✅ (본 brief §3) | — |
| BG-3 | 격리 수단 후보 비교 (M1~M4) | ✅ (본 brief §4) | 결정 = entry 발효 |
| BG-4 | single-host canonical(ST-3+ST-1) 적격 / ST-4 DEFER | ✅ | γ-1 / γ-2 |
| BG-5 | hardware key 흡수 + 백업 키 부작용 식별 | ✅ (본 brief §5) | 백업 키 정책 = 구현 결정 |
| BG-6 | 실 구성(env scrub/socket/cap_drop/docker secret) | ⏳ | **구현 entry 발효 + Evidence** (본 brief 범위 밖) |

> **결론(권고)**: BI-3 의 *결정 공간*(대상·수단 후보·흡수·한계)이 정비됨 → credential 수단 *결정* 은 구현 entry 발효 합의(풀 3+1)의 권한. 본 brief = 그 입력 정비 한정.

### 11.2 Rollback Trigger (R-I-IMPL-BOUNDARY 답습)

구현 중 다음 발견 시 rollback + 사용자 alert: (i) Hermes 가 사람 키/host token/audit write credential 획득 (Hermes≠root 위반) / (ii) hardware key 채택 후 백업 키 부재로 lock-out 위험 방치 (BI-9 미충족) / (iii) 격리 수단 본문 고정(CN-6 위반) / (iv) single-host 한계가 "안전 확정"으로 오용(거짓 안전감, §6) / (v) chmod 능동강제로 Hermes 가 perm 조작 권한 획득(γ-1 위반).

---

## 12. 합의 형태 (풀 3+1 의무)

- **credential 수단 결정 = 풀 3+1 *의무*, Reviewer-only 부적격** — Group I = T3 보안 enforcement, BI-3 = 최강 BLOCKING + 핵심 제약 #1 직결 (`f29c772` §2.1 답습). 본 brief 승인 후 credential 결정은 구현 entry 발효 합의에 *통합* 되거나 BI-3 단독 합의로 분리 가능 — 형태 결정 = 사용자 명시.
- **2차 vendor**: trigger #7 = Group I 외부 GPT-5.5 1건 기 충족. BI-3 단계 추가 vendor = 사용자 결정(의무 아님).

---

## 13. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 |
|------|------|------|
| **(A)** | 본 brief 승인 → **credential 수단 결정 합의 진입** (풀 3+1 — M1~M4 中 결정 + BI-3 충족 검증 + 백업 키 정책) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 → v2 | v2 작성 |
| (C) | 본 brief 승인 → commit *까지만* | 1 commit |
| (D) | 보류 → 다른 BLOCKING 심화 (BI-4 anchor / BI-1 CI fingerprint / BI-5 audit) 또는 GitHub plan·ruleset 가용성 확인 brief | 별도 brief |
| (E) | 보류 → 다른 backlog (tmux 도입 / G1 PR·approval auto-reject / 2차 vendor / GP-5 C-2 Backlog #4) | 별도 brief |
| (F) | 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). credential 수단 결정 / hardware key 채택 / 백업 키 정책 / 실 구성 = 사용자 명시 승인 후 별도 단계. 구현 = **R-I-IMPL-BOUNDARY → Backlog #6 + 별도 풀 3+1**.

---

## 14. 한 단락 요약

`8e57f7b` Group I 구현 entry 합의의 **최강 BLOCKING BI-3("credential 격리 = 4축 공통 선결 전제", 우선순위 1)** 를 단독 심화한 brief — (§2) BI-3 = 나머지 3축(positive allow-list·external anchor·audit sink)이 모두 "사람/admin credential Hermes 미주입"에 독립 수렴하는 *상위 전제* 이며 미격리 시 4축 명목화 + metadata detection 대비 순이득 0 + 거짓 안전감(음의 순이득), (§3) 격리 *대상* = 사람 signing key(T-1)·host token(T-2)·SSH/GPG agent socket(T-3)·audit write credential(T-4)·CI 잔존(T-5)으로 enumeration(특히 T-1 = 사람 *권위 신호 생성 키* = GP-3 일반 secret 보다 좁고 결정적), (§4) 격리 *수단 후보* = M1(미주입=ST-3+ST-1 single-host canonical)·M2(hardware-backed key 구조적 흡수)·M3(vault)·M4(Vault HSM ST-4 = MVP-6 DEFER, γ-2)로 means/ends 비교(결정 0건, CN-6), (§5) ⭐ hardware-backed key(YubiKey/FIDO2)가 개인키를 물리 토큰 밖에 두지 않아 "동일 호스트 keychain/socket 공유 gap"을 *구조적으로 흡수*(harness 원칙)하나 부작용으로 1인 lock-out 가용성 SPOF → 백업 키 의무(BI-9/CBI-1)이며 T-2/T-4 는 자동 흡수 안 됨, (§6) ⭐ single-host = 동일 침해 경계 = "충족=안전 확정 아니라 수용된 SPOF 위 최선"(거짓 안전감 차단), (§7) GP-3 §5(P3 저장 경로) 정합 + **N-2 인용 "GP-3 §6.2"가 실제로는 GP-4 §6.2(P5)이고 GP-3 은 §5 임을 발견·정밀화 권고** + ST-1/ST-3/ST-4 경계 + chmod 능동강제 비권고(γ-1) 재확인, (§8) 미격리 시 4축 붕괴 축별 분석, (§9) audit write credential(T-4) = BI-3∩BI-5 재귀(sink 매체는 BI-5 분리), (§11) 진입 gate(BG-1~BG-5 충족, BG-6 실 구성 = entry 발효) + Rollback Trigger, (§12) 풀 3+1 의무로 정비. 본 brief 는 결론을 *선취하지 않으며* — 격리 수단 *결정*·hardware key *채택*·백업 키 *정책 고정*·실 구성(env scrub/socket/cap_drop/docker secret)·실 hook·ruleset·CI·audit sink·Vault ST-4 진입·Operational Readiness PASS·Hermes PMO 격상·commit·push = **모두 0건** 이며 사용자 명시 + 별도 단계다.

---

## 부록 A — 답습 출처

| 출처 | 답습 영역 |
|------|----------|
| **`3plus1-consensus-2026-05-21-group-i-provenance-check-implementation-entry.md` (`8e57f7b`/`f29c772`) BI-3 + CBI-1 + §2.4 + §4 + §1.4 N-2/N-7** | BI-3 정의·수단 권고·거짓 안전감·hardware 흡수·백업 키 (§2·§4·§5·§6) |
| `group-i-provenance-check-implementation-boundary-brief.md` (`596f866`) §3 credential 행·§4 경계 | 4축 매핑·single-host vs MVP-6 경계 (§4·§7) |
| `hermes-not-root-of-trust-runtime.md` (`708bc0e`) provenance check 4축 + §5.5 SPOF | DESIGN 입력·동일 침해 경계 (§2·§6) |
| `governance-preconditions.md` §5 (GP-3 Credential/Secret Hygiene, P3/P4) | GP-3 정합·N-2 citation 정밀화 (§7) |
| `backlog3-groupgamma1-st1-...` (`9b1f8cd`, ST-1) / `backlog3-groupgamma2-st4-vault-hsm` (`2e9d46b`, ST-4 DEFER) | ST-1 chmod 비권고 / ST-4 MVP-6 DEFER (§4·§7) |
| `implementation-runtime-roadmap-mvp1.md` §(ST-1~ST-5 enumeration) | ST 경계 (§7) |
| ADR-011 §2.1 (means/ends) + [[feedback_provider_liquidity]] | §4·§10 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**credential isolation 실 구성** (사람 signing key·token·SSH/GPG agent socket 미주입 / env scrub / socket 미마운트 / `cap_drop` / docker secret 정의 / chmod·entrypoint stat 본문) / **hardware-backed key 채택 결정·토큰 벤더 고정·백업 키 정책 고정** (CBI-1/BI-9) / **실 hook 구현** (pre-commit / pre-receive / git server-side / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / paths 필터) / **filesystem ACL·`read_only` mount·audit sink 실 구성** / **Hermes runtime·upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR / ST-1·ST-5 진입) / **Vault HSM ST-4 진입** (γ-2 DEFER MVP-6) / 수단 결정 고정 (격리 방식·키 매체·secret source — CN-6) / threshold 고정 (observe mode 기간) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 재변경 (특히 line 360/784/805 4축) / GP-3 본문 변경 / ADR 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경 (N-2 citation 정밀화 = 권고 한정, 자동 갱신 0건) / GP entry 합의 본문 변경 / 다른 BLOCKING(BI-1/2/4~10) 자동 진입 / G1 (PR·approval auto-reject) 신규 단위 자동 진입 (Group α C-2 별도 단위) / Backlog #4 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
