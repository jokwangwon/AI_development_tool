# H-1 docker group hole 해소 검토 brief — credential 수단 결정 *선결*(S-0) (DRAFT v1)

> **본 brief = credential 수단 발효 entry brief 의 발효 선결 S-0(H-1 docker group hole)을 *수단 결정 이전*에 검토하는 brief 한정** (사용자 명시 "(B)→(A) 순서"). 본 brief 의 어떤 §도 그 자체로 **docker group 멤버십 변경·rootless docker 전환·사용자 분리·tss group 변경·daemon 재구성** 을 발생시키지 않는다. 본 brief = **H-1 위협 grounded 평가 + 해소 옵션 비교 + 권고** — 실 변경 0건. staged: brief → 승인 → (필요 시) 합의 → 발효.

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (v1 + credential 수단 발효 풀 3+1 합의 반영 — CMA-5 위협 강도 / B-2 보안 강도 순위 + O-5 / CMA-2 touch-to-sign 하한선 / CMA-3 H-1↔H-2)
**진입 단위**: credential 수단 발효 entry brief §7 S-0 — **수단 결정 *이전* 선결**
**답습 입력**: credential 수단 발효 brief §1.3 H-1/H-2/H-3 + §3.2 + §7 S-0 / `ead5754` CD-3(docker socket·ptrace 비협상)·CD-5(PEN-5 host escape)·CD-6(touch-to-sign) / 4축 통합 §9 거짓 안전감

---

## 1. H-1 grounded 평가 (실 read-only 조사 결과)

### 1.1 실측 사실 (2026-05-21)

| 항목 | 확인값 |
|----|----|
| docker 모드 | **rootful** (Server 29.2.1, daemon active) — rootless 아님 |
| docker socket | `/run/docker.sock` = `root:docker`, 0660 (group `docker` write 가능) |
| docker group | gid 988, **유일 멤버 = `delangi`** |
| userns-remap | ❌ 없음 (security opt = `cgroupns` 만) |
| 컨테이너 위생 (PoC 패턴) | ✅ **이미 실천** — `docker.sock 미마운트`("F-A 비채택"), `cap_drop: ALL`, `user: 1000:1000`, `read_only: true`, `no-new-privileges`, `privileged: false` |

### 1.2 ⭐ H-1 의 정확한 범위 = *컨테이너* 아닌 *host 사용자 상시 권한*

- **CD-3 의 *컨테이너* 측면은 이미 충족**: 기존 PoC docker-compose 들이 docker.sock 미마운트 + cap_drop ALL + 비특권 사용자(1000:1000) + read_only 를 답습 → Hermes 컨테이너는 이미 host escape 표면이 닫혀 있음.
- **남은 구멍 = host 사용자 `delangi` 의 standing 권한**: rootful docker + docker group 멤버 → `delangi`(또는 delangi 로 실행되는 임의 프로세스)가 `docker run -v /:/host --privileged ...` 한 줄로 **host root 동치 escape**. group write 가능한 `/run/docker.sock` 직접 호출도 동일.
- ⭐ **CMA-5 (위협 강도 — *상시·수동적*)**: escape 는 *명시적 악성 명령*에 국한되지 않는다. **`delangi` 로 실행되는 *임의 코드*(LLM 이 생성·실행한 스크립트 · 공급망 트로이[악성 npm/pip postinstall] 포함)가 *별도 exploit 없이* docker API 로 host root 획득**. 즉 delangi 권한으로 도는 *어떤* 코드든 곧 root → BI-3 신뢰 모델(에이전트 = 신뢰 경계 밖)과 정면 충돌. "사용자가 나쁜 명령 안 치면 됨"이 아니라 *구조적 신뢰 기반 결함*.
- → **H-1 = "컨테이너가 탈출하느냐"가 아니라 "서명 키가 놓일 host 의 상시 사용자 계정이 이미 root 동치냐"**. 답 = **예**.

### 1.3 credential 격리에 대한 함의 (왜 수단 결정 *이전* 선결인가)

- BI-3 모델 = 서명 키는 *host* 에 (사람이 서명), Hermes 컨테이너는 서명 능력 미보유. 그런데 **그 host 의 상시 사용자가 root 동치**이면:
  - TPM 의 **비추출성**(키가 칩 밖 미이탈)은 *유지* — 공격자가 root 라도 키 raw material 추출 불가.
  - 그러나 **서명 *능력* (TPM 에 서명 요청)은 탈취 가능** — root 는 PKCS#11 브리지·ssh-agent·signing 프로세스에 도달 → **touch/PIN policy 가 없으면 무제한 자동 서명**.
- → **"TPM 결정했으니 격리됐다"가 H-1 미해소 시 음의 순이득**(거짓 안전감, `ead5754` §4 / 4축 통합 §9). H-1 이 수단 선택(TPM vs YubiKey)보다 *앞선* 이유 = H-1 이 **touch-to-sign(M2/CD-6) 보강의 필요성을 직접 결정**하기 때문.

---

## 2. 해소 옵션 비교 (권고 — 발효 아님)

| # | 옵션 | 효과 | 비용/마찰 | Provider Liquidity |
|---|----|----|----|----|
| **O-1** | **rootless docker 전환** (delangi 가 rootless daemon 실행) | docker escape 가 host root 아닌 **delangi 권한**까지로 한정 → host 전체 root 동치 소멸 | 전환 작업 + 일부 기능 제약(특정 network/mount). PoC 들 재검증 필요 | 중립(표준 docker 기능) |
| **O-2** | **서명 사용자 분리** — 전용 비특권 사용자(docker group 미소속)가 서명, TPM tss 권한을 *그 사용자에게만*. dev/Hermes = delangi | 서명 능력이 docker-privileged 계정에서 *구조적 분리* | 사용자/세션 관리 복잡도 ↑ | 중립 |
| **O-3** | **delangi docker group 제거 + `sudo docker`** | standing 권한 제거, docker 사용은 sudo 감사 게이트 경유 | 일상 마찰 ↑ (매 docker 호출 sudo) | 중립 |
| **O-4** | **touch-to-sign 보강** (YubiKey M2 / TPM PIN+presence policy) | host root 라도 *물리 터치/PIN 없이 서명 불가* — defense-in-depth (H-1 잔존해도 자동 서명 차단) | YubiKey 조달(M2) 또는 TPM policy 구성. CD-6 PIN 캐시 비활성 동반 | M2=벤더 lock-in 주의(CD-7) |
| **O-5** ⭐ (R-1) | **전용 비특권 서명 사용자** — delangi docker group *유지*(dev 편의) + 별도 서명 사용자에게만 tss group(H-2) 부여 + 서명 사용자 docker group **미소속** | 서명 능력이 docker-privileged 계정과 *구조적 분리* + **H-2(tss 부여 대상) 동시 해결**(CMA-3) | rootless 재구성 *불필요* = **전환 비용 0** / 서명 시 사용자 전환(`su signer`/systemd user service) | 중립 |

### 2.1 권고 (조합 — 단일 아님) — ⭐ 보안 강도 순위 (B-2)

> **서명 능력 탈취 차단 기준 순위**: **O-2 (구조적 분리) ≈ O-5 (전용 서명 사용자, 전환비용 0) > O-1 (권한 강등, 단 서명 사용자=delangi 면 잔존) ≈ O-4 (자동 서명 차단, 단 escape 잔존) > O-3 (감사만)**. 각 옵션 잔존 표면이 *비대칭* — 평면 비교 금지.

- **1차(구조적 분리): O-2 / O-5** — 서명 능력을 docker-privileged 계정에서 *구조적 분리*(서명능력 탈취 관점 **최강**). O-5 = 전환 비용 0 + H-2 동시 해결(CMA-3 H-1↔H-2 단일 결정).
- **O-1(rootless)의 잔존**: escape 를 delangi 권한으로 강등하나, **서명 키·agent socket 이 delangi 소유면 delangi 침투 = 서명능력 여전히 탈취** → O-1 단독은 "서명 사용자를 별도 비특권 계정으로"(=O-5) 보강 조건.
- ⭐ **2차 = 비협상 하한선 (CMA-2)**: **O-4 touch-to-sign(자동 서명 차단)을 "2차 defense-in-depth"가 아니라 *수단 무관 비협상 하한선*으로 격상**. O-1/O-2/O-5(구조적)는 **owner self-bypass(IB-2)·host 완전 침해를 못 막으나**, 자동 서명 차단은 host 가 완전히 침해돼도 *물리 터치/PIN 없이는 서명 불가* = O-1/O-2 가 못 막는 잔존 표면을 닫는 *유일* 메커니즘. TPM=PIN+presence policy / YubiKey=touch=always (CD-3 동층위). → **O-2/O-5 + O-4 조합이 최강**.
- ⚠️ **O-3 단독은 미흡**: sudo docker 도 결국 root daemon 호출 → escape 표면 잔존. 단 **모든 docker 호출이 sudo 로그 = BI-5 audit 축과 시너지**(차단 아닌 *기록* 수단, R-7) → O-1/O-2/O-5 병용 시 보강.

### 2.2 거짓 안전감 차단

- O-1~O-4 *채택 라벨* ≠ 해소 입증. **PEN-5(host escape) 침투 시연**(credential brief §5)이 docker group 경유로 *실패* 해야 H-1 해소 확인. "rootless 켰음" ≠ "escape 차단됨".
- single-host 1인 = O-2 사용자 분리해도 *같은 사람*이 두 계정 모두 제어 → owner self-bypass(IB-2) 잔존. H-1 해소 = *비의도 프로세스/원격 침해* 경로 차단이지 owner 경로 차단 아님.

---

## 3. 수단 결정(A)으로의 입력

| H-1 결론 | credential 수단 결정(A) 영향 |
|----|----|
| 컨테이너 측면 CD-3 = 이미 충족 (PoC 패턴) | TPM/YubiKey 어느 쪽이든 컨테이너 격리 추가 작업 최소 |
| host 사용자 standing root-동치 (H-1) | **O-2/O-5 = 수단 결정 *이전* 선결**(tss 부여 = 분리 서명 사용자 = CMA-3 단일 결정). 미해소 시 어느 수단도 음의 순이득 |
| H-1 잔존·owner 경로 | ⭐ **CMA-2: touch-to-sign(자동 서명 차단) = 수단 무관 비협상 하한선** — "YubiKey 보강 시에만"이 아니라 TPM 택해도 PIN+presence policy 의무. H-1(standing root-동치)·owner 완전 침해 시 *유일* 잔존 방어. 수단 순위(TPM vs YubiKey)와 *직교* |

---

## 4. 다음 단계

- 본 brief = H-1 *검토*(권고). **docker group/rootless/사용자 분리 실 변경 = 발효(별도, 본 brief 0건)**.
- (B) 완료 → **(A) credential 수단 발효 풀 3+1 합의** 진입 (H-1/S-0 결론을 합의 입력에 반영).

## 부록 — 금지 (영구 답습)

docker group 멤버십 변경 / rootless docker 전환 실행 / 서명 사용자 생성·분리 실행 / tss group 변경 / daemon 재구성 / YubiKey 조달·TPM policy 구성 / PEN-5 침투 시연 실 실행 / 수단 결정 고정 / 실 hook·CI·ruleset / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화.
