# Backlog #1 ST-2 inotify sidecar 실 구현 진입 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 (옵션 (A) brief 그대로 승인 + 신규 5 결정 명시: `inotifywait` / Cycle 3 = test + feat 2 commit 분리 / §C-5 = γ sub-condition 분리 / init grace 10초 / healthcheck interval 5초)
**합의 일자**: 2026-05-13 후속 26
**검토 대상**: **Backlog #1 ST-2 (inotify sidecar) *실 구현* 진입 *적격성 권위 권고*** — 선행 4 결정 (`0e99a56`) + 신규 5 결정 답습 + 6 Cycle 분할안 + 11 신규 파일 후보 + Cycle 1 한정 진입 + Cycle 2~6 자동 진입 0건 + §C-5 γ sub-condition 분리 적절성
**보조 참조**:
- 본 합의 대상 brief = `docs/phase0/backlog1-st2-implementation-brief.md` (commit `997ca18`, DRAFT 16 섹션)
- ST-2 단독 우선 진입 적격성 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md` (commit `0e99a56`, APPROVE — 선행 4 결정 권위 source)
- ST-2 단독 진입 적격성 brief = `docs/phase0/backlog1-st2-inotify-sidecar-brief.md` (commit `d9ae98b`)
- Backlog #6 구현 진입 합의 패턴 답습 = `docs/review/3plus1-consensus-2026-05-12-runtime-ci-hook-implementation-entry.md` (commit `c50e6a0`)
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, APPROVE WITH CONDITIONS, §C-5 GP-3 1.5차 보강 Backlog #1 Deferred 정의)
- ADR-008 §A.2 R1-2 + §2.6.2 R2-1 + GP-3 §5.3 + ADR-011 §2.1 (a)~(e) + §2.4 + mvp1.md §3.3 + §3.4.2 + §3.6.1

**검토 목적**: Backlog #1 ST-2 *실 구현* 진입 *계획 적격성* 권위 권고 + 신규 5 결정 답습 적절성 + Cycle 1 한정 진입 적격성 확정. **본 합의 = ST-2 실 구현 *계획 적격성* 권위 권고 한정 + Cycle 1 진입 *발효* 적격성 한정 ≠ Cycle 2~6 자동 진입 / ST-2 자체 실 구현 완료 발효 / §C-5a Satisfied 자동 갱신 / Layer D 본문 변경 / Layer E / Layer F 격상**.

**판정**: ✅ **APPROVE — Backlog #1 ST-2 *실 구현* 진입 *계획 적격성* 권위 확정 + Cycle 1 진입 적격 (Reviewer-only 단축 합의, 사용자 명시 9 결정 답습)**

⚠️ **본 합의 = 실 구현 *계획 적격성 권위 권고* + Cycle 1 진입 한정** — Cycle 2~6 자동 진입 0건 + sidecar Dockerfile / inotify 스크립트 / docker-compose / CI workflow / actual run / §C-5 자동 갱신 모두 0건.

⚠️ **본 합의 ≠ MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / Layer D 본문 변경 / C-1~C-8 자동 변경** — 모두 그대로 유지.

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-13 후속 26):

> "옵션 (A)로 진행해주세요. 본 텍스트 brief를 그대로 승인하고, 파일화한 뒤 Reviewer-only 단축 합의 보고서 작성, 이후 Cycle 1로 진입하겠습니다."

> "(a) inotifywait 방식 / (b) Cycle 3 test + feat 2 commit 분리 / (c) §C-5 γ sub-condition 분리 (C-5a/b/c) / (d) init grace period 10초 / (e) healthcheck interval 5초"

> "Cycle 1은 PoC 격리 디렉토리 구조 설계 + README 까지만 진행. Cycle 2 이후는 Cycle 1 완료 후 사용자 결정 대기."

### 0.2 사용자 명시 9 결정 답습

**선행 4 결정 (`0e99a56` 답습 — 변경 0건)**:
1. fail-closed = F-B 우선 / F-C 보조 / F-A 비채택
2. Multi-host parity = 미요구
3. inotify 감시 경로 = `/run/secrets/*`
4. runtime secret 변경 = fail-closed + secret rotation 별도 합의

**신규 5 결정 (본 합의 권위 확정)**:
5. inotify watch 구현 = **`inotifywait`** (inotify-tools 패키지, sidecar Dockerfile PoC 범위 내 한정)
6. Cycle 3 commit = **`test` + `feat` 2 commit 분리**
7. §C-5 갱신 방식 = **γ sub-condition 분리** (C-5a = ST-2 / C-5b = ST-1 / C-5c = PC-4)
8. init grace period T2 = **10초**
9. healthcheck interval = **5초**

### 0.3 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 합의 = brief §1~§14 답습 한정 + 사용자 명시 9 결정 답습 한정 — Layer D 본문 변경 0건 + §5.5 9 sub-수단 본문 채택 변경 0건 + C-1~C-8 상태 변경 0건 + ADR 본문 갱신 0건) | ✅ |
| 직전 합의 chain (Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독 진입 모두 Reviewer-only) 패턴 답습 | ✅ |
| brief §14 본문 명시 답습 — "**Reviewer-only 단축 합의 적격**" (7/7 풀 3+1 트리거 0건 발화) | ✅ |
| Backlog #6 `c50e6a0` 구현 진입 계획 합의 동일 패턴 답습 (실 runtime 구현 *계획 적격성 권위 권고* 발효 — 단축 합의 Reviewer-only) | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — 새 도구 등록 영역, T1 deterministic 0 + T3 영역 침범 0) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 (옵션 (A) + 9 결정 명시 + Cycle 1 한정 진입 명시) | ✅ §0.1 답습 |
| **7/7 풀 3+1 승격 트리거 0건 발화** | ✅ §2 답습 |
| Cycle 1 한정 진입 + Cycle 2~6 자동 진입 0건 | ✅ §0.1 답습 |

### 0.4 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독 진입 / ST-2 단독 진입 brief / ST-2 실 구현 brief 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

**청산 매커니즘**:
1. **사후 외부 LLM 충족 보존** — 누적 cross-vendor blind 의뢰 5건 답습 (Stage 5 entry / Layer C / Layer D / Backlog #5 / K-2 fix 권위 chain)
2. **격상 전 면제 보존** — Hermes PMO 격상 *전 단계*. 본 검토 = 실 구현 *계획 적격성* + Cycle 1 한정 진입 적격성 한정 — Layer E / Layer F 미진입
3. **합의 권위 내부 변경 한정** — 본 검토 = brief §1~§14 + 사용자 명시 9 결정 답습 한정 — 새 권위 결정 0건
4. **자기 작성 한계 명시** — 본 §0.4 + §5 명시
5. **Cycle 1 한정 진입 + Cycle 2~6 자동 진입 0건 보존** (사용자 명시 답습)
6. **T3 자동 진입 0건 보존** — brief §1.2 답습 + 10/10 T3 침범 후보 0건
7. **외부 LLM cross-vendor blind 의뢰 미진입** — 7/7 단축 합의 적격 트리거 0건 발화

### 0.5 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| **Cycle 2~6 자동 진입** | ❌ (사용자 명시 답습 — Cycle 1 한정 진입) |
| **ST-2 *실 구현 완료 발효*** | ❌ (본 합의 = 계획 적격성 + Cycle 1 한정) |
| **sidecar Dockerfile / inotify 스크립트 / docker-compose 작성** | ❌ (Cycle 3 영역, 본 합의 시점 0건) |
| **CI workflow 변경** | ❌ (Cycle 4 영역) |
| **actual run 실행** | ❌ (Cycle 6 영역) |
| **§C-5 / C-5a *Satisfied 자동 갱신*** | ❌ (Cycle 6 후속 별도 합의 영역) |
| **MVP-1 PASS *재선언*** | ❌ (Layer D `210c98f` 그대로 유지) |
| Operational Readiness PASS (Layer E) | ❌ (MVP-6, Backlog #7) |
| Hermes PMO 격상 (Layer F) | ❌ (MVP-6, 외부 LLM + 사람 리뷰 의무) |
| **ST-1 자동 진입** | ❌ (T3 영역, Backlog #3) |
| **PC-4 자동 진입** | ❌ (Backlog #1 + #2 분리) |
| **T3 영역 자동 진입** | ❌ |
| **production `docker-compose.yml` 변경** | ❌ (PoC 격리 한정) |
| **Hermes upstream 변경** | ❌ (`0e99a56` 답습) |
| **사용자 명시 9 결정 *재변경*** | ❌ (본 합의 = 9 결정 답습 한정) |
| C-2~C-4, C-6~C-8 자동 변경 | ❌ |
| §5.5 9 sub-수단 본문 채택 변경 | ❌ |
| ADR 본문 자동 갱신 | ❌ |
| 다른 backlog (#2/#3/#4/#7) 자동 진입 | ❌ |
| Tier-2/3 catalog 자동 확장 | ❌ |
| 외부 LLM 자동 호출 | ❌ |

---

## 1. 검토 기준 충족 분석 (9/9 적절)

### 1.0 사용자 명시 9 결정 답습 검증

| # | 결정 | 본 brief 반영 | 판정 |
|---|------|------------|------|
| 1 | fail-closed = F-B 우선 / F-C 보조 / F-A 비채택 | brief §2 + §3 + §10 답습 (`0e99a56` 권위 답습 변경 0건) | ✅ 적절 |
| 2 | Multi-host parity 미요구 | brief §1.2 답습 (`0e99a56` 답습) | ✅ 적절 |
| 3 | inotify 감시 경로 = `/run/secrets/*` | brief §4 답습 | ✅ 적절 |
| 4 | runtime secret 변경 fail-closed + rotation 별도 합의 | brief §6 + §7 답습 | ✅ 적절 |
| 5 | inotify watch = `inotifywait` | brief §5.2 답습 — `inotifywait -m -e attrib,modify,move_self,delete_self` + sidecar Dockerfile alpine + inotify-tools (PoC 범위 한정) | ✅ 적절 |
| 6 | Cycle 3 commit = test + feat 2 commit 분리 | brief §9.2 답습 — TDD RED/GREEN + 추적성 + 실패 시 격리 권고 | ✅ 적절 |
| 7 | §C-5 γ sub-condition 분리 | brief §13 답습 — C-5a (ST-2) + C-5b (ST-1) + C-5c (PC-4) | ✅ 적절 |
| 8 | init grace period T2 = 10초 | brief §6.2 답습 — `sleep 10` 후 inotifywait 시작 | ✅ 적절 |
| 9 | healthcheck interval = 5초 | brief §2.1 + §10.2 답습 — docker-compose healthcheck `interval: 5s` | ✅ 적절 |

**합산 = 9/9 적절** — 사용자 명시 9 결정 모두 brief 본문 반영 + 답습 권위 근거 충실.

### 1.1 추가 검토 기준 (`c50e6a0` Backlog #6 구현 진입 합의 패턴 답습)

| # | 항목 | 판정 |
|---|------|------|
| 1 | 6 Cycle 분할 적절성 | ✅ 적절 (의존성 그래프 + 각 Cycle 신규 파일 + commit 형태 권고 명시, brief §9 답습) |
| 2 | 신규 11 파일 + 기존 확장 1 + 변경 0건 7+ 분리 적절 | ✅ 적절 (PoC 격리 디렉토리 + production 분리 + sibling `gp3-st3-poc/` 패턴 답습) |
| 3 | ADR-011 §2.1 (a)~(e) 5조건 evidence 매핑 | ✅ 적절 (brief §10.1 답습) |
| 4 | Rollback Trigger 13 후보 (R-ST2-1~R-ST2-13) | ✅ 적절 (`d9ae98b` 8 + 본 brief 신규 5) |
| 5 | actual run 검증 9 항목 + SUCCESS 기준 명시 | ✅ 적절 (brief §12 답습 — 9/9 충족 → §C-5a 갱신 합의 진입 적격) |
| 6 | Cycle 1 한정 진입 + Cycle 2~6 자동 진입 0건 | ✅ 적절 (사용자 명시 답습 — brief §9.4 답습) |
| 7 | T3 자동 진입 0건 (10/10 침범 후보) | ✅ 적절 (brief §1.2 + §0.4 답습) |
| 8 | §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ 적절 |
| 9 | Layer D 본문 변경 0건 + C-1~C-8 상태 변경 0건 | ✅ 적절 (§C-5 = Deferred 그대로 유지 — γ 분리 = Cycle 6 후속 별도 합의) |

**합산 = 9/9 추가 기준 적절**.

### 1.2 9/9 검토 기준 + 9/9 추가 기준 = 18/18 충족

본 brief 의 ST-2 실 구현 *계획 적격성* + 사용자 명시 9 결정 답습 + 6 Cycle 분할 + Cycle 1 한정 진입 + T3 자동 진입 0건 모두 권위 근거 충실 (Layer D / Backlog #1 진입 직전 정비 / ST-2 단독 진입 / Backlog #6 패턴 / mvp1.md §3 / §5.5 / ADR-008 / ADR-011 답습).

---

## 2. 풀 3+1 승격 트리거 검증 (7/7 0건 발화)

| # | 트리거 | 본 합의 검토 결과 |
|---|----|------------|
| 1 | 본 합의가 9 sub-수단 *외* 수단 *재결정* 권고 | ❌ 0건 발화 (본 합의 = ST-2 실 구현 *계획* + Cycle 1 진입 한정) |
| 2 | 본 합의가 T3 영역 *자동 진입* 권고 | ❌ 0건 발화 (10/10 T3 침범 후보 0건 보존) |
| 3 | 본 합의가 사용자 명시 9 결정 *재변경* 권고 | ❌ 0건 발화 (선행 4 + 신규 5 모두 답습 한정) |
| 4 | 본 합의가 Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 발화 (GP-3 저장 경로 영역) |
| 5 | 본 합의가 5 영구 핵심 제약 약화 포함 | ❌ 0건 발화 (Hermes ≠ root of trust 보존 — F-A 비채택 답습 + T3 분리 보존 + 수단/목적 분리 보존) |
| 6 | 본 합의가 MVP-1 PASS *재선언* / Layer E / Layer F 격상 포함 | ❌ 0건 발화 (사용자 명시 답습 §0.5) |
| 7 | 본 합의가 외부 LLM *없이* T3 영역 결정 권고 | ❌ 0건 발화 (T3 자동 진입 0건) |

**합산 = 7/7 0건 발화** → Reviewer-only 단축 합의 적격 확정.

---

## 3. 본 합의 발효 범위

### 3.1 본 합의가 *발생시키는* 것

| # | 영역 |
|---|------|
| 1 | Backlog #1 ST-2 *실 구현* 진입 *계획 적격성* 권위 확정 |
| 2 | 사용자 명시 9 결정 답습 (선행 4 + 신규 5) 권위 확정 |
| 3 | 6 Cycle 분할 + 의존성 그래프 + 각 Cycle commit 형태 권고 권위 확정 |
| 4 | 11 신규 파일 + 1 기존 확장 + 7+ 변경 0건 영역 분리 권위 확정 |
| 5 | Rollback Trigger 13 후보 (R-ST2-1~R-ST2-13) 권위 권고 |
| 6 | actual run 검증 9 항목 + SUCCESS 기준 권위 권고 |
| 7 | §C-5 γ sub-condition 분리 (C-5a/b/c) 권위 권고 + C-5a Satisfied 갱신 조건 정리 |
| 8 | **Cycle 1 진입 *적격성* 권위 확정** (`docker/gp3-st2-poc/README.md` 작성 진입 적격) |
| 9 | Reviewer-only 단축 합의 chain 답습 (Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 단독 진입 / 본 합의) |

### 3.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

| # | 영역 | 본 합의 발효 시점 위반 |
|---|------|------------------|
| 1 | Cycle 2~6 *자동 진입* | 0건 (사용자 명시 답습) |
| 2 | ST-2 *실 구현 완료 발효* (sidecar Dockerfile / inotify 스크립트 / docker-compose / hermes-mock 작성) | 0건 (Cycle 3 영역) |
| 3 | CI workflow 변경 | 0건 (Cycle 4 영역) |
| 4 | actual run 실행 | 0건 (Cycle 6 영역) |
| 5 | §C-5 / C-5a *Satisfied 자동 갱신* | 0건 (Cycle 6 후속 별도 합의) |
| 6 | Layer D 본문 *자동 변경* (γ sub-condition 분리 = Cycle 6 후속 합의에서 권위 확정) | 0건 |
| 7 | MVP-1 PASS *재선언* | 0건 (`210c98f` 그대로 유지) |
| 8 | Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) | 0건 (MVP-6 영역) |
| 9 | ST-1 / PC-4 / T3 영역 *자동 진입* | 0건 |
| 10 | C-2~C-4 / C-6~C-8 상태 *자동 변경* | 0건 |
| 11 | §5.5 9 sub-수단 본문 채택 *변경* | 0건 |
| 12 | ADR 본문 *자동 갱신* | 0건 |
| 13 | 다른 backlog (#2/#3/#4/#7) *자동 진입* | 0건 |
| 14 | 사용자 명시 9 결정 *재변경* | 0건 |
| 15 | Production `docker-compose.yml` 변경 | 0건 (PoC 격리 한정) |
| 16 | Hermes upstream Dockerfile 변경 | 0건 (`0e99a56` 답습) |
| 17 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 18 | 외부 LLM 자동 호출 | 0건 |
| 19 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 20 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 21 | Provider Liquidity 5-way / 5 영구 핵심 제약 약화 | 0건 |
| 22 | CONTEXT / INDEX / SESSION 메타 갱신 (별도 commit 분리 답습) | 0건 |

### 3.3 본 합의 발효 후 *즉시* 진입 영역 = Cycle 1 한정

| 영역 | 진입 |
|------|------|
| **Cycle 1**: `docker/gp3-st2-poc/README.md` 작성 + commit | ✅ **본 합의 발효 직후 진입 적격** (사용자 명시 답습 — 옵션 (A) Cycle 1 진입) |
| Cycle 2~6 | ❌ **자동 진입 0건** (사용자 명시 답습 — "Cycle 2 이후는 Cycle 1 완료 후 사용자 결정 대기") |

### 3.4 본 합의 발효 후 *다음* 단계 (Cycle 1 완료 후, 사용자 결정 영역)

| 후보 | 영역 |
|------|------|
| (1) Cycle 2 진입 (fixture 5 개) | 사용자 명시 결정 후 |
| (2) Cycle 1 commit + CONTEXT / INDEX / SESSION 메타 갱신 commit | 별도 commit 분리 답습 |
| (3) push (전체 commit chain) | 사용자 결정 |
| (4) 보류 → 다른 backlog 우선 | 사용자 결정 |

---

## 4. 발효 영향 매트릭스

### 4.1 Layer + Backlog 분리 매트릭스 (본 합의 발효 시점)

```
Layer A : Backlog #6 entry 기준 정의                       — APPROVE (f1e0b23)
Layer B : 9 sub-수단 본문 채택 + 시작 권한                 — APPROVE (f40423f + 55c5b4b)
Layer B 행사: Stage 1+3 / 2 / 4 / 5                        — 발효 (5 runs PASS)
Layer C : MVP-1 Implementation Evidence PASS              — APPROVE (6973935)
Layer D : MVP-1 PASS                                      — APPROVE WITH CONDITIONS (210c98f, 본문 변경 0건)
Backlog #5 ADR-012 event enum 정식 등록                   — APPROVE (b705370) — §C-2 Satisfied
K-2 baseline fix + §C-1 갱신                              — APPROVE (1dd1036 + 56da31f) — §C-1 Satisfied
Backlog #1 진입 *직전* 사전 정비                          — APPROVE AS BRIEF (43b898c + 6b15070 + 45de393)
Backlog #1 ST-2 단독 우선 진입 적격성                     — APPROVE (d9ae98b + 0e99a56 + 6199c92)
■ Backlog #1 ST-2 실 구현 진입 계획 적격성 + Cycle 1 진입 — APPROVE (브리프 997ca18 + 본 합의 + Cycle 1 commit 후속) ← 본 단계
■ Backlog #1 ST-2 실 구현 완료                            — 아직 아님 (Cycle 1~6 진행 필요)
■ §C-5 / C-5a Satisfied 갱신                              — 아직 아님 (Cycle 6 후속 별도 합의)
Layer E : Operational Readiness PASS                      — 아직 아님 (C-3, MVP-6, Backlog #7)
Layer F : Hermes PMO 격상                                 — 아직 아님 (C-4, MVP-6, 외부 LLM + 사람 리뷰 의무)
```

### 4.2 C-1~C-8 상태 (본 합의 발효 후)

| Condition | 상태 | 본 합의 영향 |
|----------|------|----------|
| C-1 (K-2 baseline 후속 fix) | ✅ Satisfied (`1dd1036`) | 변경 0건 |
| C-2 (event enum 정식 등록) | ✅ Satisfied (Backlog #5 `b705370`) | 변경 0건 |
| C-3 (Operational Readiness parity) | ⏳ Deferred (MVP-6, Backlog #7) | 변경 0건 |
| C-4 (Hermes PMO 격상) | ⏳ Deferred (MVP-6) | 변경 0건 |
| **C-5 (GP-3 1.5차 보강 — Backlog #1)** | ⏳ **Deferred** (γ sub-condition 분리 권고 확정, **상태 변경 0건** — C-5a Satisfied 갱신 = Cycle 6 후속) | **분리 권고 확정 한정** |
| C-6 (GP-5 1.5차 보강 — Backlog #2) | ⏳ Deferred (Backlog #2) | 변경 0건 |
| C-7 (T3 영역 — Backlog #3) | ⏳ Requires separate full 3+1 (Backlog #3) | 변경 0건 |
| C-8 (P1 v2 facade MVP — Backlog #4) | ⏳ Deferred (Backlog #4) | 변경 0건 |

**핵심**: 본 합의 = ST-2 실 구현 *계획 적격성* + Cycle 1 진입 한정 — **§C-5 상태 변경 0건** (Deferred 그대로 유지, γ sub-condition 분리는 *권고* 한정 — C-5a Satisfied 갱신 합의 = Cycle 6 후속).

### 4.3 본 합의 행사 의무 (사용자 명시 답습)

| 항목 | 의무 |
|------|------|
| commit 분리 (3 commit) | ✅ Commit 1 (brief `997ca18`) + Commit 2 (본 합의 — 본 commit) + Commit 3 (Cycle 1 — 후속) |
| CONTEXT / INDEX / SESSION 메타 갱신 분리 | ✅ 별도 commit (사용자 명시 답습) |
| Cycle 2~6 자동 진입 금지 | ✅ Cycle 1 한정 진입 |
| 사용자 명시 9 결정 보존 | ✅ §1.0 답습 |

---

## 5. 메타 검증

| 메타 검증 | 본 합의 |
|---------|--------|
| 사용자 명시 진입 명령 답습 (옵션 (A) + 9 결정 + Cycle 1 한정 + Reviewer-only 단축 합의) | ✅ |
| 9 검토 기준 + 9 추가 기준 = 18/18 충족 | ✅ |
| 7 풀 3+1 승격 트리거 0건 발화 | ✅ |
| 사용자 명시 9 결정 답습 보존 | ✅ |
| §5.5 9 sub-수단 본문 채택 변경 0건 | ✅ |
| C-1~C-8 상태 답습 (§C-5 Deferred 그대로 유지) | ✅ |
| Layer D 본문 변경 0건 (`210c98f` 그대로 유지) | ✅ |
| ADR-011 §2.4 T1/T2/T3 분류 답습 (T3 침범 10/10 0건) | ✅ |
| ADR-008 §A.2 R1-2 + §2.6.2 R2-1 답습 | ✅ |
| 5 영구 핵심 제약 보존 | ✅ |
| 7 backlog 분리 매트릭스 답습 | ✅ |
| Cycle 1 한정 진입 + Cycle 2~6 자동 진입 0건 | ✅ |
| 합의 권위 자기 내부 변경 한정 (외부 LLM 미진입) | ✅ |

---

## 6. 본 합의 요약 (한 단락)

본 합의 는 **Backlog #1 ST-2 (inotify sidecar) *실 구현* 진입 *계획 적격성* 권위 확정 + Cycle 1 진입 적격성 + 사용자 명시 9 결정 답습 적절성 확정 (Reviewer-only 단축 합의)** 이다. 사용자 명시 9 결정 (선행 4 + 신규 5) — (1) F-B 우선 / F-C 보조 / F-A 비채택 / (2) Multi-host parity 미요구 / (3) `/run/secrets/*` / (4) runtime fail-closed + rotation 별도 합의 / (5) `inotifywait` / (6) Cycle 3 test+feat 2 commit / (7) §C-5 γ sub-condition (C-5a/b/c) / (8) init grace 10초 / (9) healthcheck interval 5초 — 모두 brief 본문 반영 + 답습 권위 근거 충실 (9/9 적절). 9 추가 기준 (6 Cycle 분할 / 11 신규 파일 + 1 확장 + 7+ 변경 0건 분리 / ADR-011 §2.1 (a)~(e) evidence 매핑 / Rollback Trigger 13 후보 / actual run 검증 9 항목 / Cycle 1 한정 진입 + Cycle 2~6 자동 진입 0건 / T3 침범 10/10 0건 / §5.5 변경 0건 / Layer D 본문 변경 0건) 모두 9/9 적절. 합산 18/18 적절 + 7/7 풀 3+1 트리거 0건 발화 → Reviewer-only 단축 합의 적격 확정. **본 합의 발효 후 *즉시* 진입 = Cycle 1 한정** (`docker/gp3-st2-poc/README.md` 작성). **Cycle 2~6 = 사용자 명시 결정 후 별도 진입** (자동 진입 0건 보존). **본 합의 ≠ ST-2 실 구현 완료 발효 / sidecar Dockerfile / inotify 스크립트 / docker-compose / CI workflow / actual run / §C-5·C-5a Satisfied 자동 갱신 / Layer D 본문 변경 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 다른 backlog 자동 진입 / production docker-compose 변경 / Hermes upstream 변경** (사용자 명시 답습). 다음 단계 = Cycle 1 진입 (별도 commit) + 메타 갱신 (별도 commit) + push (사용자 결정).

---

**합의 일자**: 2026-05-13 후속 26
**판정**: ✅ **APPROVE — Backlog #1 ST-2 *실 구현* 진입 *계획 적격성* + Cycle 1 진입 적격 (Reviewer-only 단축 합의, 사용자 명시 9 결정 답습)**
**다음 단계**: Cycle 1 진입 (`docker/gp3-st2-poc/README.md` 작성 + commit) — 본 합의 직후 진입 적격, Cycle 2~6 = 사용자 명시 결정 영역

**금지 (사용자 명시 답습 — 본 합의 영역 + 본 합의 발효 후 단계 양쪽)**:
- ❌ Cycle 2~6 *자동 진입* (Cycle 1 완료 후 사용자 결정 영역)
- ❌ ST-2 *실 구현 완료 발효* (Cycle 3 영역)
- ❌ sidecar Dockerfile / inotify 스크립트 / docker-compose / hermes-mock 작성
- ❌ CI workflow 변경 (Cycle 4 영역)
- ❌ actual run 실행 (Cycle 6 영역)
- ❌ §C-5 / C-5a *Satisfied 자동 갱신* (Cycle 6 후속 별도 합의)
- ❌ Layer D 본문 *자동 변경* (γ sub-condition 분리도 Cycle 6 후속 합의에서 권위 확정)
- ❌ MVP-1 PASS *재선언*
- ❌ Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F)
- ❌ ST-1 / PC-4 / T3 영역 *자동 진입*
- ❌ Production `docker-compose.yml` 변경
- ❌ Hermes upstream Dockerfile 변경
- ❌ C-2~C-4 / C-6~C-8 자동 변경
- ❌ §5.5 9 sub-수단 본문 채택 *변경*
- ❌ ADR 본문 *자동 갱신*
- ❌ 다른 backlog (#2/#3/#4/#7) *자동 진입*
- ❌ 사용자 명시 9 결정 *재변경*
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 (본 commit ≠ 메타 갱신 — 별도 commit 분리 답습)
