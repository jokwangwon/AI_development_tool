# Agent 권한 상승(sudo/root) 처리 정책 — harness 설계 brief (DRAFT v2)

> **본 brief = "에이전트가 권한(sudo/root) 필요 작업을 만났을 때, *사용자 개입을 최소화*하면서도 *agent ≠ root*(BI-3/H-1)를 어기지 않는 정책"을 *설계 차원에서 정리*하는 brief 한정.** 본 brief 의 어떤 §도 그 자체로 sudoers 변경·broker 구현·`settings.json` 권한 정책 변경·credential 수단 재결정·BI-3 합의 본문 변경·실 발효 를 발생시키지 않는다. 본 brief = **핵심 긴장 명문 + 작업 유형 분류 + brokered capability 설계 공간 + "개입 최소화 ↔ 보안" 형량 프레임워크 + credential 수단 fork 재평가(결정 아님)** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → (별도) 설계 채택·구현**.

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (v1 + 풀 3+1 합의 `3plus1-consensus-2026-05-21-agent-privilege-escalation-policy.md` BLOCKING AP-1~6 + 권고 AR-1~9 반영 — 본문 반영, 정책 채택·발효 0건)
**진입 단위**: credential 수단 발효 (나)→(다) 중 *sudo 처리* 가 표면화 → harness 설계 질문으로 격상 (credential 발효는 본 brief 정리까지 *보류*)

## v2 변경 이력 (풀 3+1 합의 AP-1~6 + AR-1~9 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **AP-1** ⭐ (T-경계 = default-T 구조 + 누락 5건 + 매핑) | §2 — "닫힌 enumeration → default-T(미분류=보수적 T)" 구조 + 패키지/공급망·`.git/`·CI yaml·env/secret·egress 추가 + R/P/T 매핑 예시 |
| **AP-2** ⭐ (broker 강제 메커니즘) | §3 — 결정적 게이트 4속성(argv·`SO_PEERCRED`·canonical·TOCTOU) + broker 위협 4 + CD-5 binary |
| **AP-3** ⭐ (정적→동적 차원) | §4 — 단방향 ratchet + 2축 grid + capability lease(시간 차원) |
| **AP-4** (allow-list escape-equivalence) | §3 패턴 A + §4 |
| **AP-5** (거짓 안전감 별도 §) | §4.1 신설 (적대적 시연 종료조건 + 부분 적용 면책 라벨) |
| **AP-6** (credential fork 약화+대안) | §5 — 단정 약화 + batch/cached presence/정책 자동 + keyless 이중 부담 |
| AR-1 (실행 격리 패턴 E~H) | §3 표 |
| AR-2 (기존 PoC 일반화) / AR-3 (systemd+Polkit) / AR-4 (재귀 닻) | §3 |
| AR-5 ⭐ (4축 일반화 결정 항목) | §7 결정 항목 격상 |
| AR-6 (PL 인터페이스/구현 분리) / AR-7 (B fallback) / AR-8 (정기 재검토) / AR-9 | §3·§4·§6 |
**답습 입력 (1차 권위)**: ADR-011 §2.1 means/ends + Hermes ≠ root of trust / `harness-engineering-design.md` (Feedforward 가이드 vs Feedback 센서, 피드백 루프 Layer 0~6) / `ead5754` BI-3 수단 결정 (CD-3 docker socket·cap_drop 비협상 / CD-5 binary) / credential 수단 발효 합의 (H-1 docker group·H-2 tss·CMA-2 touch-to-sign 하한선·CMA-3) / R-I-CONFIG-CHANGE T3(사람 직접·Hermes 미주입) / [[project_minimize_user_intervention]] / [[feedback_provider_liquidity]]
**합의 권위 한계**: 본 brief = *설계 정리* DRAFT — 정책 *채택*·broker 구현·sudoers/`settings.json` 변경·credential 수단 재결정 은 별도 단계(풀 3+1 + 사용자 명시). **본 brief 는 "어떻게 형량할 것인가"의 *틀과 후보*를 정리할 뿐 정책을 *고정*하지 않는다.**

---

## 0. 범위

### 0.1 진입 맥락

1. credential 수단 발효 (나) S-0+S-2 실행 단계에서 **모든 발효 작업(사용자 생성·group 변경·tss 부여·패키지 설치)이 sudo/root 를 요구**함이 드러남.
2. 에이전트(`delangi` 셸)는 sudo 가 대화형(비밀번호) — 비대화형 실행 불가.
3. 이때 **"사용자 개입 최소화"가 명시 설계 목표**로 표명됨 ([[project_minimize_user_intervention]]).
4. 사용자 결정: 이 sudo 처리를 **harness 설계로 먼저 정리** + **(2) 개입 최소화를 보안과 *형량*** (비협상 입력 아님).

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**: 긴장 명문 / 작업 유형 분류 / brokered capability 설계 공간 / 형량 프레임워크 / credential 수단 fork *재평가(trade-off 제시)*.
- **하지 않는 것 (영구 답습)**: ❌ 정책 *채택·고정* / ❌ **sudoers·`/etc/sudoers.d/` 변경** / ❌ **broker/sidecar 실 구현** / ❌ `settings.json` 권한·hook 변경 / ❌ credential 수단 *재결정*(BI-3 합의 `ead5754` 본문 변경) / ❌ S-0+S-2 발효 / ❌ tpm2-pkcs11 설치·group 변경 / ❌ sigstore·gitsign·Rekor 도입 / ❌ Operational Readiness PASS / Hermes PMO 격상 / ❌ 합의 보고서 작성·commit·push(별도) / ❌ ADR·harness-engineering-design 본문 자동 갱신 / 5 영구 핵심 제약·Provider Liquidity 약화.

---

## 1. 핵심 긴장 (명문)

```
   목표 G: 사용자 개입 최소화 (자율 개발 도구)
        ⊥  (trust boundary 에서 충돌)
   제약 S: agent ≠ root (BI-3/H-1) + BI-3 격리 = 신뢰 경계에 *의도된 사람 마찰* 삽입
           (touch-to-sign CMA-2 / 사람 키 보유 / 정책 변경 사람 직접 T3)
```

- **G 를 trust boundary 까지 밀면** = 에이전트에 일반 sudo·자동 서명 부여 = **H-1 hole 그 자체**(우리가 닫으려는 것) → S 붕괴.
- **S 를 모든 작업에 적용하면** = 일상 작업마다 사람 승인 = G 완전 포기 = 자율 도구 목적 상실.
- ⭐ **(2) 형량의 본질** = "어디서 G 를 살리고(개입 최소화) 어디서 S 가 이기는가(사람 마찰=통제)"를 *작업 유형*으로 가른다. G 와 S 는 전역 충돌이 아니라 **작업 유형별로 다른 균형점**을 갖는다.

---

## 2. 작업 유형 분류 (형량의 축)

| 유형 | 정의 | 빈도 | 위험(오용 시) | 개입 최소화 가능? |
|----|----|----|----|----|
| **R-routine** | 빌드·테스트·파일 편집·샌드박스 내 네트워크·읽기 — 신뢰 root 불변 | 매우 높음 | 샌드박스 내 한정 | ✅ **최대 최소화 대상** |
| **P-provision** (1회성) | 격리 셋업·사용자 생성·group·**시스템** 패키지 설치 — 셋업 후 불변 | 매우 낮음(≈1회) | 높음(셋업 자체가 신뢰 기반) | ⚠️ 사람 1회, 이후 0 |
| **T-trust-boundary** | 서명·credential 변경·enforcement 정책·audit 정책 + ⭐ **AP-1 누락 5건**: 패키지/공급망(`apt`/`pip`/`npm`)·**`.git/` 변조**(hook·config·objects)·**CI workflow yaml**·**env/secret 노출**·**네트워크 egress/DNS** — 신뢰 root *변경* | 낮음~서명당 | 최고(신뢰 root) | ❌ **사람 마찰 = 통제 그 자체** |

- **핵심 명제**: "개입 최소화"의 정당한 타깃 = **R-routine** (그리고 P-provision 의 1회성). **T-trust-boundary 의 사람 authorization 은 *제거 대상 마찰이 아니라 보안 통제*** — 0 으로 줄이면 owner-bypass/H-1 재개방.
- ⭐ **AP-1 (default-T 구조 — "닫힌 enumeration" 폐기)**: 무엇이 T 인가의 목록은 *본질적으로 불완전*하다(누락 = silent 권한 상승). 따라서 T 를 *열거*하지 않고 **"위 R/P 에 *명시 분류되지 않은* 모든 권한 작업 = 보수적 T(default-deny)"** 의 *구조*로 정의한다. brief v1 의 자기경고("목록 완전성이 안전을 좌우")는 *경고가 아니라 구조*로만 자기충족된다. **CMA-5 답습**: 임의 코드(LLM 생성·공급망)가 별도 exploit 없이 standing root-동치 = "목록에 없는 경로가 root 직결" → default-T 가 그 경로를 자동 포섭.
- ⭐ **AP-1 R/P/T 매핑 예시** (모호 경계 해소):
  - **서명 = T / `git push` = R** 분해 (서명이 신뢰 root, push 는 전파 행위) — 단 *서명된* commit/tag push 는 T 산출물 전파.
  - **`docker run` = host 상태 의존**: H-1(docker group=root-동치) *미해소* 상태에선 docker = **T-등가**(CMA-5). H-1 해소(O-2/O-5) 후에만 샌드박스 docker = R.
  - **패키지**: *시스템* 패키지(`apt`) = P / *프로젝트 의존성*(`pip`/`npm`) = **R 중 빈발이나 공급망 위험 = T 측 검토**(default-T).
  - **모호 시 T 보수 분류** (안전 측 기본값, §4 ratchet 과 결합).

---

## 3. 설계 공간 (brokered privilege 패턴 — R/P 의 개입 최소화 수단)

> 공통 불변: **agent 는 일반 root/sudo 를 절대 미보유**(= H-1 hole 금지). 아래는 "그럼에도 R/P 작업의 사람 개입을 줄이는" 방법.

| # | 패턴 | 개입 최소화 | 보안 비용 | 비고 |
|---|----|----|----|----|
| **A** | **좁은 sudoers allow-list** (NOPASSWD = *고정·정확한* 명령 N개만) | 높음(해당 명령 0 개입) | 각 허용 명령 = 공격 표면. ⭐ **AP-4 escape-equivalence**: 정확 매칭이어도 항목 자체가 root-동치 확장(`apt install`=공급망·`tee`·`systemctl`·`cp/install`=SUID·셸 우회). **allow-list = T(정책)** → 사람 관리·재귀 보호 | wildcard·shell metachar 금지, 정확 argv 매칭. **AR-3: systemd unit+Polkit = sudoers 보다 좁은 표면 대안**(argv 미노출) |
| **B** | **사전 provision 비특권 샌드박스** (1회 셋업으로 R 작업이 권한 0으로 동작) | 최대(R 작업 권한 불필요) | 셋업 시점 사람(P) 1회 | 가장 깨끗 — R 을 권한 밖으로 *설계*. ⭐ **AR-2: 신규 설계 아님 — 기존 `r2-poc`/`gp3-st3` PoC(`cap_drop ALL`·`user 1000:1000`·docker.sock 미마운트·`network none`) 일반화** |
| **C** | **특권 broker/sidecar** (별도 특권 프로세스가 *결정적 정책*으로 검증된 작업만 수행, agent=클라이언트) | 높음(API 호출만) | broker 정책 = T·재귀 보호. ⭐ **broker 자체 = 새 신뢰 컴포넌트·단일 침해점** | "capability, not credential". **AR-6: broker 인터페이스 ⊥ 구현(sudoers/systemd vs 클라우드 IAM=lock-in)** |
| **D** | **사람만 (broker 없음)** | 없음(매번 사람) | 최고 안전 | T-trust-boundary 의 default |
| **E** (AR-1) | **rootless containers + userns-remap** | (R 격리 강화) | ARM64 rootless cgroup v2/storage 제약·전환 비용 | CMA-5 "docker API=host root" 표면 *제거*. CMA-3 O-2/O-5 보완 |
| **F** (AR-1) | **gVisor / Kata 샌드박스** (syscall 인터셉트 / 경량 VM) | (R 격리 강화) | gVisor syscall 호환·성능 / Kata=ARM64 KVM 의존(⚠️ PL) | R-routine 강격리 |
| **G** (AR-1) | **ephemeral VM/container per task** (작업당 일회용, 종료 시 폐기) | (standing 권한 0) | 셋업 레이턴시·상태 비영속 | R 작업 standing 표면 0 |
| **H** (AR-1) | **capability lease 토큰** (단명 = §4 AP-3 시간 차원 구현) | 높음(윈도우 내 자동) | TTL = 침해 기회 윈도우 = 형량 변수 | broker(C)에 *시간 차원* 부가 |

- ⭐ **AP-2 (broker/게이트 강제 메커니즘 — "결정적" 라벨 ≠ 입증)**: §3 의 "결정적 게이트"는 *원칙 선언*이 아니라 4 속성으로 강제: **(a) 고정 argv 정확 매칭**(wildcard·shell metachar 금지) **(b) IPC = `SO_PEERCRED` uid 인증 + 호출자 화이트리스트**(미인증 시 임의 프로세스[CMA-5] 호출 가능) **(c) canonical path + 정적 enum**(path traversal·symlink 차단) **(d) TOCTOU 방지(fd 기반)**. **broker 위협 4**: IPC 호출자 인증 / 요청 위조·파라미터 주입 / TOCTOU / 상시 특권 프로세스 표면. **broker 순이득 = broker 표면 < allow-list 표면일 때만**. 이 4속성 충족 = **적대적 시연(에이전트가 broker 우회·인자 주입·권한 확대 *못 함*) binary 로만 입증**(CD-5 답습, §4.1).
- **계산적 vs 추론적 (CLAUDE.md)**: broker 의 *판정*은 **결정적(deterministic)** + **입력 무결성**(에이전트가 검증 *입력*을 조작하면 계산적이어도 우회, AR-9) 둘 다.
- ⭐ **AR-4 재귀 종료 닻 (CP-3)**: A 의 allow-list·C 의 broker 정책 = "권한을 정의하는 설정" = *그 자체가 T*. **닫힘 = 정책 파일 `root:root`, 에이전트(delangi) 쓰기 미보유 → 자기 권한 확대하려면 다시 broker 필요하나 broker 가 "정책 파일 수정" 미허용 = 회귀 1단계 멈춤**(원칙 선언 아닌 *구현 속성*). broker 가 sudoers.d 편집을 한 줄이라도 allow 하면 무한후퇴 재개방.

---

## 4. 형량 프레임워크 — 제안 원칙 P-PRIV (3+1 검증 대상, 채택 아님)

> (2) "보안과 형량" 답습 = 작업 유형별 차등 + gradient.

1. **최소 권한 default**: agent = 비특권. 권한은 *예외*이며 명시적·좁음.
2. **R-routine → 최대 최소화**: 패턴 B(사전 provision) 우선, 불가피한 권한은 A/C(좁은 broker). 사람 개입 ≈ 0 목표.
3. **P-provision → 사람 1회**: 격리 셋업은 사람(sudo)이 1회, 이후 0. 에이전트는 *정확한 명령 시퀀스 artifact 생성*까지(자동 sudo 금지).
4. **T-trust-boundary → 사람 authorization = 통제**: 서명·credential·정책·audit 변경은 사람. ⭐ **단 *불필요한* 마찰은 제거**(개입 최소화는 *횟수·번거로움*에 적용, *존재*에는 미적용) — 예: touch-to-sign 은 필수(CMA-2)지만 한 번의 터치로 충분하게, 중복 확인·수동 단계는 없앤다.
5. **broker 정책·allow-list = T**: 권한 정의 변경은 사람 직접(T3), 에이전트 미도달(재귀 보호, AR-4 닻).
6. ⭐ **AP-3 (정적 분류 → 동적 차원)** — 정적 R/P/T 만으로는 부족:
   - **(a) 분류 = 단방향 ratchet**: R→T *승격*은 자유 / **T→R *강등*은 T3 사람 + 적대적 재시연**. 운영 중 편의로 T→R 미끄럼(scope-creep drift) 차단 — 안 그러면 형량이 *drift 엔진*(서명 빈도↓·broker 권한 확대·allow-list 항목 추가 → H-1 재현). drift = **Rollback Trigger 능동 감지**(정책 파일 변경·allow-list diff).
   - **(b) 2축 grid + capability lease (시간 차원)**: 폭발반경(가역↔신뢰 root 변경) × 빈도(1회↔상시) grid. T 작업도 **1회 사람 authorization → 짧은 TTL capability 발급 → 윈도우 내 동종 자동**(예: 서명 세션 N분 lease, 패턴 H) = 사람 *존재* 유지(S 불변) + *횟수* ↓(G 충족) = §4(4) 원칙의 *유일 실현 메커니즘*. ⚠️ **TTL = 형량 변수**(host 침해 기회 윈도우, 상한 = T 결정).
7. **거짓 안전감 차단**: §4.1 별도 (AP-5).

- **형량 산식(권고)**: 작업을 R/P/T 로 분류(미분류=default-T, AP-1) → R/P 는 B>A/C 로 개입↓ / T 는 D 또는 lease(불필요 마찰만 제거). 분류 모호 = T 보수. **AR-8: 정적 1회 분류 ≠ 형량 — 정기 재검토**(어떤 T 가 lease 로 G 회복 가능한가 / over-classification 마비 방지).

### 4.1 거짓 안전감 차단 (AP-5 — 별도 §)

본 정책의 실패 양식: (i) **"broker/정책 깔았으니 안전"** — 라벨 ≠ 입증(CD-5). **적대적 시연 종료조건(binary)**: ① 에이전트가 broker/sudoers 우회해 임의 root 실행 *실패* ② allow-list 항목 escape(AP-4) *실패* ③ **미분류 sudo 요구 = 자동 거부**(default-T 작동). (ii) **부분 적용 = 최대 거짓 안전감** (CMA-7 동형): 정책 일부만 깔린 중간 상태(broker 있으나 IPC 미인증·allow-list 미검토·default-T 미적용) = **"권한 통제 보장 0"** 면책 라벨. (iii) **owner 경로 잔존**: 같은 사람이 정책·allow-list 자체 변경 = MVP 수용 SPOF. (iv) **형량 = 표면 *이동*** (CMA-6 동형): 마찰을 *줄이는* 게 아니라 *어디로 옮기는지* — lease TTL·서명 빈도↓가 표면을 옮기는 곳을 본다.

---

## 5. credential 수단 fork 재평가 (balanced — trade-off 제시, 결정 0건)

(2) 형량 하에서 BI-3 credential 수단(`ead5754`)을 *개입 마찰* 축으로 재조명 (수단 재결정 아님 — 3+1 입력):

| 접근 | 개입 마찰 (G) | 보안 (S) | 위치 |
|----|----|----|----|
| **hardware key + touch-to-sign** (BI-3 현 방향, TPM/YubiKey) | 높음(서명당 사람 터치) | 높음(host 완전 침해도 자동 서명 차단, CMA-2) | T-trust-boundary 의 정당한 마찰 |
| **CI ephemeral / keyless(gitsign OIDC)** | 낮음(자동 서명) | 중(OIDC 새 신뢰축 + 자동 서명 = touch 없음 → host/CI 침해 시 서명 가능) + MVP-6 DEFER | 마찰↓이나 CMA-2 자동서명차단 *상실*. ⭐ **AP-6 이중 부담**: gitsign 도 OIDC 토큰 격리 필요 → CP-4(credential) *안 닫음* → "Sigstore=credential 해결" 거짓 안전감 차단 |

- ⭐ **형량 결론(권고, 결정 아님)**: 서명 = **T-trust-boundary** → 마찰(touch)은 *제거 대상이 아니라 통제*. 따라서 **(2) 하에서도 "개입 최소화"가 hardware+touch 를 자동으로 keyless 로 뒤집지 않는다**.
- ⭐ **AP-6 (단정 약화 + 대안 확장)**: v1 의 "서명 빈도 축소 = G+S 양립" *단정* 은 **보안 공백 동반 평가**로 약화한다:
  - ⚠️ **비서명 commit 구간 보안 공백**: R-routine commit 비서명 → (i) 에이전트 자유 생성 (ii) **BI-1 fingerprint allow-list *판정 입력 부재*** (비서명=fingerprint 없음) (iii) merge 가 서명하는 것은 *트리 상태*이지 각 commit *provenance* 아님 (iv) **CMA-2 "건당 의도 확인" 희석**(merge 1터치가 다수 비서명 commit 일괄 승인). → 빈도 축소는 G+S 양립이 아니라 *S 일부 양보*일 수 있음.
  - **CMA-2(자동 서명 차단)를 *유지하며* 마찰↓ 대안 병치** (채택 아님, 3+1 입력): **batch 서명**(N commit 1 presence — 자동 아님·CMA-2 충족·마찰 N→1, 단 batch 윈도우 일괄 의도) / **FIDO2 cached presence**(짧은 TTL — §4 AP-3 lease 의 credential 구현, TTL=침해 윈도우=형량 변수, CMA-2 *부분* 약화) / **정책 기반 자동 서명**(안전 화이트리스트만 — 단 판정 *계산적*[path-glob diff]일 때만, 화이트리스트=T 재귀보호. 추론적 판정=센서 우선 위반).
- → credential 발효 (다) 수단 결정은 본 형량 결과(서명 빈도·lease·경계)를 반영해 재개.

---

## 6. 기존 원칙 정합

- **ADR-011 Hermes ≠ root of trust**: P-PRIV 1·5 가 직접 구현 — agent 는 자기 권한 root 아님.
- **harness-engineering-design (가이드 vs 센서)**: broker 결정 = 계산적 센서(결정적). "에이전트에게 하지 말라 말고 못 하게" = agent 에 sudo 미부여(구조적 불가).
- **BI-3 / H-1 / CMA-3**: P-provision(S-0+S-2) = 사람 1회. agent 일반 sudo = H-1.
- **CMA-2 touch-to-sign**: §4(4)·§5 = T 경계 마찰은 통제, 존재 유지.
- **R-I-CONFIG-CHANGE T3**: §4(5) broker 정책 변경 = 사람 직접.
- **Provider Liquidity (AR-6)**: ⚠️ "sudoers/systemd 표준이라 *우연히* 중립"이 아니라 **broker *인터페이스*(capability 요청/응답) ⊥ *구현*(sudoers/systemd/IAM) 분리로 중립을 *강제***(CD-8/R-4 답습). broker 를 클라우드 IAM 으로 구현 시 즉시 lock-in → "정책 = 선언적 데이터, 집행 매체 교체 가능". (CD-8 교훈의 broker 축 미적용 = CP-10 재발 차단)
- **[[project_minimize_user_intervention]]**: 본 brief 가 그 목표의 *적용 범위*(R/P)와 *한계*(T)를 정의.

---

## 7. 합의 형태 + 다음 단계

- 본 brief = harness 아키텍처 + 보안 정책 → **풀 3+1 의무** (완료: `3plus1-consensus-2026-05-21-agent-privilege-escalation-policy.md`, APPROVE WITH CONDITIONS, AP-1~6 + AR-1~9). v2 = 본 합의 반영.
- 합의 = **추론적 검증(권고) 한정** — 정책 채택·broker 구현·credential 수단 재결정 = 사용자 명시 + 별도 단계.

### ⭐ AR-5 범위 결정 — **4축 일반 원칙로 확정** (사용자 명시 2026-05-22)

> **결정**: P-PRIV(R/P/T 분류 + default-T + capability lease + 거짓 안전감 차단) = **harness 일반 원칙**. credential 한정 아님.

| 항목 | 확정 내용 |
|----|----|
| 적용 범위 | **4축(credential·allow-list·anchor·audit) 권한 처리에 *재사용*** — R/P/T+lease 를 allow-list 갱신·anchor ruleset·audit 정책에 일관 적용 (DRY, 축마다 재정의 불필요·CP-10 비전파 위험 차단) |
| T 경계 목록 | **4축 합집합으로 확대** — default-T(AP-1)가 4축의 모든 미분류 권한 작업을 보수적 포섭. silent 권한 상승 차단 범위 = 4축 전체 |
| 후속 | P-PRIV = **`harness-engineering-design.md` 확장 후보** (별도 발효 — 본 결정은 *범위 확정*까지, 문서 확장 = 별도 단계) |

→ 이후 (다) credential 발효는 P-PRIV(4축 일반)를 *credential 축 인스턴스*로 적용.

### 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (가) | ✅ **본 v2** — AP-1~6 + AR 반영 (현 단계) | brief 수정 |
| (나) | ⭐ **AR-5 범위 결정** (credential 한정 vs 4축 일반) | 결정 |
| (다) | 형량 결과(AP-3 lease·AP-6 서명 빈도) 반영해 credential 발효 (다) 재개 | 발효 (보류) |
| (라) | brief + 합의 commit | 메타 |
| (마) | 세션 종료 | 메타 |

---

## 부록 — 답습 출처 + 금지

**출처**: ADR-011(Hermes≠root·means/ends) / harness-engineering-design(가이드·센서·Layer) / `ead5754` BI-3(CD-3·CD-5) / credential 수단 발효 합의(H-1·H-2·CMA-2·CMA-3) / R-I-CONFIG-CHANGE T3 / [[project_minimize_user_intervention]] / [[feedback_provider_liquidity]].

**금지 (영구 답습)**: 정책 채택·고정 / **sudoers·`/etc/sudoers.d/` 변경** / broker·sidecar·systemd unit·Polkit 실 구현 / **capability lease·TTL 실 구성** / **rootless·gVisor·Kata·ephemeral VM 전환** / `settings.json` 권한·hook 변경 / **credential 수단 재결정**(BI-3 `ead5754` 본문 변경) / AR-5 범위 *결정* 자동화(사용자 명시) / S-0+S-2 발효 / tpm2-pkcs11 설치·group·tss 변경 / sigstore·gitsign·Rekor 도입 / Hermes runtime·upstream 변경 / Operational Readiness PASS / Hermes PMO 격상 / Vault ST-4 / threshold 고정 / MVP-1 exit / **git history rewrite** / ADR·harness-engineering-design·합의 본문 자동 갱신 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화.
