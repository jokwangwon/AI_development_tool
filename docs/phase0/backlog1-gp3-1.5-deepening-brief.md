# Backlog #1 — GP-3 1.5차 보강 진입 직전 사전 정비 Brief (준비안 — DRAFT)

> **본 문서는 MVP-1 PASS (Layer D) `210c98f` APPROVE WITH CONDITIONS + §C-1 Satisfied 갱신 (`1dd1036`) 발효 후속, Backlog #1 (GP-3 1.5차 보강 — ST-1 / ST-2 / PC-4) *진입 직전 사전 정비* 의 brief 준비안 한정.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Backlog #1 진입 합의를 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) MVP-1 PASS *재선언* / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-13 후속 24
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위**:
- `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` §3.5 (C-5 — GP-3 1.5차 보강 Backlog #1 Deferred, commit `210c98f`)
- `docs/review/3plus1-consensus-2026-05-13-mvp1-pass-c1-k2-satisfaction.md` (§C-1 Satisfied 갱신, commit `1dd1036`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.3 (ST-1 ~ ST-5 매트릭스) + §3.5 (R-MVP1-G3-7) + §4.3 (PC-1 ~ PC-4 매트릭스) + §4.7.3 (합의 형태 권고)
- `docs/architecture/governance-preconditions.md` §5.3 (강제 메커니즘) + §5.4 (Evidence (a)~(e))
- `docs/decisions/ADR-008-hermes-adoption-decision.md` §A.2 R1-2 + §2.6.2 R2-1
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 (T1/T2/T3 3-tier 분류)
- ADR-011 §2.1 (a)~(e) 5조건 패턴

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "GP-3 1.5차 보강 brief 작성을 진행해주세요. 범위는 Backlog #1, 즉 ST-1 entrypoint stat / ST-2 inotify sidecar / PC-4 framework 보강 가능성 검토입니다. MVP-1 PASS 재선언, Operational Readiness PASS, Hermes PMO 격상, T3 영역 자동 진입은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. Backlog #1 3 항목 (ST-1 / ST-2 / PC-4) 의 *보강 가능성* 사전 정비 (§2)
2. 각 항목의 *영역 분류* (T2 / T3 / 혼합) + Hermes upstream 영향 + sidecar 가능성 매트릭스 (§2.4)
3. 각 항목별 *합의 형태 권고* + 풀 3+1 승격 트리거 후보 검증 (§3)
4. 보강 발효 *시점* 의 Rollback Trigger / Evidence 기준 *정리* (§4)
5. 본 brief 자체 + 보강 발효 후 단계 *금지 사항* enumerate (§5)
6. 다음 단계 결정 옵션 (사용자 결정 영역, §6)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

- ❌ **MVP-1 PASS *재선언* 0건** (Layer D `210c98f` 판정 = APPROVE WITH CONDITIONS 그대로 유지)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건** (MVP-6 영역 — C-3 Deferred 유지)
- ❌ **Hermes PMO 격상 (Layer F) 0건** (MVP-6 영역 — C-4 Deferred 유지, 외부 LLM cross-vendor blind + 사람 리뷰 의무 답습)
- ❌ **T3 영역 *자동 진입* 0건** (Hermes upstream Dockerfile 변경 / Vault HSM / Tier-2-3 catalog 자동 확장 / branch protection rule 변경 모두 자동 진입 0건)
- ❌ **Backlog #1 진입 합의 발효 0건** (본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음)
- ❌ **실 runtime code 구현 0건** — Hermes Dockerfile entrypoint script 본문 / inotify sidecar 본문 / `.pre-commit-config.yaml` 본문 / `pre-commit install` 실행 0건
- ❌ **실 CI workflow / hook 구현 0건** — workflow 본문 변경 / hook 신설 0건
- ❌ **수단 *결정* 0건** (ST-1 / ST-2 / PC-4 *채택 결정* = 별도 합의 영역)
- ❌ **§5.5 9 sub-수단 본문 채택 *변경* 0건** (Layer B `f40423f` + `55c5b4b` 답습 — 4 sub-수단 GP-3 (S-1 + ST-3 + PC-3 + AR-1) 유지)
- ❌ **threshold *고정* 0건** (FP/FN/latency / inotify event 응답 시간 모두 *후보 한정* 유지)
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건** (R-4.1 Tier-1 45 patterns 답습)
- ❌ **ADR 본문 자동 갱신 0건** (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건 — cross-reference 답습 한정)
- ❌ **합의 보고서 작성 0건** (본 brief = 준비안 한정)
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건**
- ❌ **git commit / push 0건**
- ❌ **외부 LLM 자동 호출 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**
- ❌ **다른 backlog (#2/#3/#4/#5/#7) 자동 진입 0건**

### 0.4 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Backlog #1 진입 합의를 *시작* 시키지 않으며,
- (ii) MVP-1 PASS *재선언* / Layer E / Layer F 발효를 *발생시키지 않으며*,
- (iii) §5.5 9 sub-수단 본문 채택 + C-1~C-8 상태를 *변경* 하지 않으며,
- (iv) Hermes upstream Dockerfile 변경 / Vault HSM / branch protection rule 변경을 *발효* 시키지 않으며,
- (v) 신규 ADR / 신규 P / 신규 GP 를 *발행* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **Backlog #1 진입 합의 *직전* 의사결정 입력 정비 — ST-1 / ST-2 / PC-4 영역 분류 + 합의 형태 권고 + Rollback / Evidence 기준 + 금지 사항 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습 (MVP-1 PASS 후 상태)

### 1.1 MVP-1 PASS 발효 후 6-layer + Backlog 분리 매트릭스 (2026-05-13 후속 23 시점)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 + 시작 권한 | ✅ APPROVE (`f40423f` + `55c5b4b`) | 답습 한정 |
| Layer B 행사 | Stage 1+3 / 2 / 4 / 5 actual run SUCCESS | ✅ 발효 (5 runs PASS) | 답습 한정 |
| Layer C | MVP-1 Implementation Evidence PASS | ✅ APPROVE (`6973935`) | 답습 한정 |
| Layer D | MVP-1 PASS | ✅ APPROVE WITH CONDITIONS (`210c98f`, **본 brief = §C-5 Deferred *결과 행사 준비*** ) | 답습 + §C-5 진입 권한 *준비* |
| §C-1 갱신 | K-2 baseline fix 2단계 (Deferred → Satisfied) | ✅ APPROVE (`1dd1036`) | 답습 한정 |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 (C-3, MVP-6, Backlog #7) | **본 brief 영역 외 — 자동 진입 금지** |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 (C-4, MVP-6, 외부 LLM + 사람 리뷰 의무) | **본 brief 영역 외 — 자동 진입 금지** |
| **Backlog #1** | **GP-3 1.5차 보강 (ST-1 / ST-2 / PC-4)** | ⏳ **C-5 Deferred — 본 brief = 진입 *직전* 준비안** | **본 brief = §C-5 진입 *직전* 정비 한정** |
| Backlog #2 | GP-5 1.5차 보강 (T-1/T-3/T-4/T-5 단독 / PC-4) | ⏳ C-6 Deferred | 본 brief 영역 외 (PC-4 일부 공유 — §2.3 답습) |
| Backlog #3 | T3 영역 (AR-2 / Vault HSM / Tier-2-3 catalog 자동 확장) | ⏳ C-7 Requires separate full 3+1 | 본 brief 영역 외 |
| Backlog #4 | P1 v2 facade MVP (G5-4) | ⏳ C-8 Deferred (MVP-3 권고) | 본 brief 영역 외 |
| Backlog #5 | ADR-012 event enum 정식 등록 | ✅ APPROVE (`4221646` + `2ece90a` + `b705370`) — §C-2 Satisfied | 답습 한정 |
| Backlog #7 | Operational Readiness parity | ⏳ Deferred (MVP-6, Layer E 영역) | 본 brief 영역 외 |

### 1.2 본 brief 의 진입점 = MVP-1 PASS 후 → Backlog #1 별도 합의 *직전*

```
Layer D APPROVE (210c98f) — MVP-1 PASS (APPROVE WITH CONDITIONS)
   │
   ▼
§C-1 Satisfied 갱신 (1dd1036) — K-2 fix 2단계 결과 행사
   │
   ▼
■ 본 brief = Backlog #1 (GP-3 1.5차 보강) 진입 *준비안* (DRAFT)         ← 현 위치
   │
   ▼ (사용자 명시 승인 후)
brief 그대로 승인 합의 보고서 작성 또는 일부 조정
   │
   ▼ (사용자 명시 결정 후)
■ Backlog #1 진입 합의 — ST-1 / ST-2 / PC-4 中 어느 항목 진입?         ← 본 brief 영역 외
   │
   ▼ (진입 결정 후, 항목별 합의 형태에 따라)
실 구현 진입 (단축 합의 → 진입 / 풀 3+1 합의 → 진입)                ← 본 brief 영역 외
   │
   ▼ (구현 + actual run SUCCESS + evidence 후)
§C-5 Deferred → Satisfied 갱신 합의 또는 추가 합의                  ← 본 brief 영역 외
```

### 1.3 Backlog #1 3 항목 답습 (mvp1.md §3.3 + §4.3 답습)

| 항목 ID | 항목 | 영역 | 본문 채택 권위 (답습 한정) | 답습 출처 |
|--------|------|------|----------------------|---------|
| **ST-1** | Hermes Dockerfile entrypoint stat 검증 (chmod 600 강제) | GP-3 저장 경로 secret 검출 보강 (G3-1) | ❌ 미채택 (mvp1.md §3.3.2 + §5.5.1 답습 — Backlog #1 분리) | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 답습 |
| **ST-2** | inotify sidecar (mtime/perm 변경 → 컨테이너 정지) | GP-3 저장 경로 secret 검출 보강 (G3-1) | ❌ 미채택 (mvp1.md §3.3.2 + §5.5.1 답습 — Backlog #1 분리) | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 답습 |
| **PC-4** | PC-1 + PC-3 병행 (local pre-commit framework + CI-only enforcement, Defense in depth) | GP-3 + GP-5 공유 pre-commit hook 보강 (G3-2 / G5-2) | ❌ 미채택 (mvp1.md §4.3.2 + §5.5.1 + §5.5.2 답습 — Backlog #1 + #2 분리) | Group D PoC §1.2 #7 + Group A 2차 §1.2 답습 |

**합산 = 3 항목 (GP-3 저장 경로 강화 2 + GP-3/GP-5 공유 pre-commit framework 1)**.

---

## 2. 3 항목 보강 가능성 분석

### 2.1 ST-1 — Hermes Dockerfile entrypoint stat 검증 (chmod 600 강제)

#### 2.1.1 영역 정의

- **검증 시점**: 컨테이너 시작 시 (entrypoint script)
- **메커니즘**: `/run/secrets/*` 또는 동등 경로의 secret 파일 권한이 `0600` 인지 stat 검증, 미달 시 `exit 1` (컨테이너 정지)
- **권위 출처**: ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 ("저장 경로 secret 보호") + GP-3 §5.3 강제 메커니즘 ("chmod 600 강제 + entrypoint stat 검증 (R1-2) — Hermes Dockerfile entrypoint")

#### 2.1.2 Hermes upstream 영향

| 영역 | 영향 |
|------|------|
| Hermes upstream Dockerfile 변경 | **✅ 필요** (mvp1.md §3.3.1 답습 — ST-1 = "Hermes upstream Dockerfile 수정") |
| sidecar 분리 가능성 | ❌ (entrypoint 자체가 Hermes 컨테이너 내부 — 외부 분리 불가) |
| T2/T3 분류 | **T3** (Hermes upstream 변경 = ADR-011 §2.4 답습 — Constitution / ADR / Harness Gates 정의 자체 변경 영역) |

#### 2.1.3 본 brief 권고 (수단 *결정 아님* — 영역 분류 한정)

- **현 시점 진입 적격 = ❌** — Hermes upstream Dockerfile 변경 = **T3 영역 진입 trigger** (사용자 명시 답습 — T3 영역 자동 진입 금지)
- **진입 조건** = 풀 3+1 합의 + Hermes upstream PR 검토 + 사용자 명시 결정 (mvp1.md §3.6.3 + §3.5 R-MVP1-G3-7 답습)
- **본 brief 의 정비 범위** = 영역 분류 정비 한정 — 진입 시점 *결정* 은 별도 합의 영역

#### 2.1.4 ST-1 보강 가능성 결론

| 차원 | 평가 |
|------|------|
| 보강 *가능성 자체* | 기술적으로는 가능 (Hermes Dockerfile entrypoint script + stat 검증 step) |
| Backlog #1 1.5차 보강으로서 *진입 적격* | ❌ **T3 영역 진입 필요 — 사용자 명시 답습 (T3 자동 진입 금지)** |
| 본 brief 발효 후 처리 | **Backlog #3 (T3 영역) 와 *병합 검토* 권고** — Hermes upstream 변경 영역은 Backlog #3 T3 별도 풀 3+1 합의 영역과 자연스럽게 합쳐짐 |
| 단독 채택 시점 | 풀 3+1 합의 + Hermes upstream PR 검토 + 외부 LLM 1+ + 사용자 명시 (모든 의무 충족 시) |

### 2.2 ST-2 — inotify sidecar (mtime/perm 변경 → 컨테이너 정지)

#### 2.2.1 영역 정의

- **검증 시점**: 런타임 지속 (inotify event 기반)
- **메커니즘**: sidecar 컨테이너가 secret 파일 경로를 inotify 감시 → mtime/perm 변경 event 발생 시 메인 컨테이너에 정지 signal 송출 (또는 docker-compose dependency 통한 graceful shutdown)
- **권위 출처**: ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 ("저장 경로 secret 보호") + GP-3 §5.3 강제 메커니즘 ("inotify 런타임 감시 — Hermes runtime") + mvp1.md §3.3.1 ("inotify sidecar | 런타임 지속 | ❌ (sidecar 분리 가능) | ✅")

#### 2.2.2 Hermes upstream 영향

| 영역 | 영향 |
|------|------|
| Hermes upstream Dockerfile 변경 | **❌ 불필요** (mvp1.md §3.3.1 답습 — ST-2 = "sidecar 분리 가능") |
| sidecar 분리 가능성 | **✅ 가능** (docker-compose 또는 동등 매니페스트 sidecar 추가 형태) |
| T2/T3 분류 | **T2** (Hermes upstream 변경 0건 + sidecar = 인프라 layer 추가 운영) |

#### 2.2.3 본 brief 권고 (수단 *결정 아님* — 영역 분류 한정)

- **현 시점 진입 적격 = ⚠️ *조건부* 적격** — Hermes upstream 변경 0건 + T2 영역 + mvp1.md §3.3.2 권고 ("MVP-1 1.5차 (보강) = ST-3 + **ST-2 inotify sidecar** (Hermes upstream 변경 회피 유지)")
- **진입 조건** (다음 中 1+ 충족):
  - 단축 합의 + 사용자 명시 결정 (T2 정책 영역 — ADR-011 §2.4 답습)
  - 또는 풀 3+1 합의 (운영 부담 中 — sidecar process 운영 → 보수적 합의 형태 권고 시)
- **본 brief 의 정비 범위** = 영역 분류 정비 + 진입 조건 후보 명시 한정 — 진입 시점 *결정* 은 별도 합의 영역
- **인접 작업**:
  - Stage 2 (ST-3 docker secret) 답습 권위 위에서 진입 (mvp1.md §3.3.2 답습 — "ST-3 + ST-2" 통합 권고)
  - inotify sidecar process 운영 = 운영 부담 中 — Operational Readiness 영역 (Backlog #7) 과 일부 연결 가능 (단, Layer E 발효 의무 아님 — 본 brief 영역 외)

#### 2.2.4 ST-2 보강 가능성 결론

| 차원 | 평가 |
|------|------|
| 보강 *가능성 자체* | **✅ 기술적으로 가능 + Hermes upstream 변경 0건** |
| Backlog #1 1.5차 보강으로서 *진입 적격* | ⚠️ **조건부 적격** — T2 영역, 단축 합의 또는 풀 3+1 합의 모두 적격 |
| 본 brief 발효 후 처리 | **Backlog #1 진입 합의 시점 = ST-2 *우선 검토* 권고** (3 항목 中 T3 자동 진입 0건 조건 충족하는 유일 항목) |
| 단독 채택 시점 | 단축 합의 + 사용자 명시 결정 (T2 정책 영역) — 또는 보수적 풀 3+1 합의 |

### 2.3 PC-4 — PC-1 + PC-3 병행 (local pre-commit framework + CI-only enforcement)

#### 2.3.1 영역 정의

- **통합 형태**: dev 환경 + CI 양쪽 차단 (Defense in depth)
- **메커니즘**:
  - **PC-1 부분** = `.pre-commit-config.yaml` + `pre-commit install` 통한 local hook 강제 (dev 환경에서 commit 전 차단)
  - **PC-3 부분** = 현 MVP-1 1차 답습 (`55c5b4b` §5.5.1 + §5.5.2 본문 채택 — CI step fail-closed)
- **권위 출처**: mvp1.md §4.3.1 ("PC-4 | PC-1 + PC-3 병행 (Defense in depth) | dev 환경 + CI 양쪽 차단 | 中-高 | T2 + T3 | 본 문서 신규 후보") + §4.3.2 권고 ("MVP-1 1.5차 (보강) = PC-4 (PC-1 + PC-3 병행) — dev 환경 강제 추가 시 Defense in depth")

#### 2.3.2 Hermes upstream 영향

| 영역 | 영향 |
|------|------|
| Hermes upstream Dockerfile 변경 | **❌ 불필요** (pre-commit framework = repo-local) |
| sidecar 분리 가능성 | N/A (pre-commit = git hook layer) |
| dev 환경 영향 | **✅ 있음** (`.pre-commit-config.yaml` + `pre-commit install` 의무 — 모든 개발자 dev 환경 영향) |
| T2/T3 분류 | **T2 + T3 혼합** (mvp1.md §4.3.1 답습 — T2 정책 영역 + T3 dev 환경 강제 정책 영역) |

#### 2.3.3 PC-4 T2/T3 분류 detail

| sub-영역 | 분류 | 사유 |
|---------|------|------|
| `.pre-commit-config.yaml` 본문 정의 | T2 | 정책 영역 (ADR-011 §2.4 답습 — Skill/Memory promotion / 새 도구 등록 / 합의 형태 결정) |
| `pre-commit install` 의무 명시 (dev 환경 강제) | T3 | dev 환경 정책 강제 = repo policy 수준 (Backlog #3 T3 영역과 부분 중첩) |
| PC-3 부분 답습 (CI step fail-closed) | T2 (이미 본문 채택, `55c5b4b` 답습) | 변경 0건 — PC-4 진입 시 PC-3 답습 유지 |

#### 2.3.4 본 brief 권고 (수단 *결정 아님* — 영역 분류 한정)

- **현 시점 진입 적격 = ⚠️ *부분 적격* + T3 영역 부분 진입 trigger**
- **진입 조건**:
  - **PC-4 의 PC-1 부분 (`.pre-commit-config.yaml` 본문 정의)** = **단축 합의 + 사용자 명시 결정** (T2 정책 영역, ADR-011 §2.4 답습)
  - **PC-4 의 dev 환경 강제 부분 (`pre-commit install` 의무화)** = **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** 권고 (T3 dev 환경 정책 영역 — Backlog #3 와 부분 중첩)
- **본 brief 의 정비 범위** = PC-4 가 단일 단위 아닌 *2 sub-영역 분리* 가능함을 명시 (T2 sub-영역 우선 단축 합의 + T3 sub-영역 별도 풀 3+1 합의 권고)
- **인접 작업**:
  - Backlog #2 (GP-5 1.5차 보강) 의 PC-4 영역과 *공유* — Backlog #1 단독 진입 시 GP-3 side 만 PC-1 본문 설정, GP-5 side 와 통합 시 본문 합산

#### 2.3.5 PC-4 보강 가능성 결론

| 차원 | 평가 |
|------|------|
| 보강 *가능성 자체* | **✅ 기술적으로 가능** (pre-commit framework = 성숙한 도구, dev 환경 의존성 명확) |
| Backlog #1 1.5차 보강으로서 *진입 적격* | ⚠️ **2 sub-영역 분리 + 부분 적격** — T2 sub-영역 (config 정의) = 단축 합의 가능 / T3 sub-영역 (dev 환경 강제) = 풀 3+1 합의 권고 |
| 본 brief 발효 후 처리 | **Backlog #1 + #2 *통합 합의* 권고 또는 Backlog #1 단독 진입 시 GP-3 side 만 본문 설정 + GP-5 side 추후 통합** |
| 단독 채택 시점 | T2 sub-영역 = 단축 합의 + 사용자 명시 결정 / T3 sub-영역 = 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |

### 2.4 3 항목 영역 분류 매트릭스 (요약)

| 항목 | T2/T3 분류 | Hermes upstream 변경 | sidecar 가능 | dev 환경 영향 | T3 자동 진입 위반 위험 | 본 brief 권고 합의 형태 |
|------|----------|---------------------|------------|------------|------------------|------------------|
| **ST-1** | T3 | ✅ 필요 | ❌ | ❌ | **⚠️ 高** (Hermes upstream 변경 직접 영역) | **풀 3+1 합의 + Hermes upstream PR 검토 + 외부 LLM 1+ + 사용자 명시** — 현 시점 진입 비권고 (Backlog #3 와 병합 검토 권고) |
| **ST-2** | T2 | ❌ 불필요 | ✅ 가능 | ❌ | **✅ 0** (T3 자동 진입 위험 0건) | **단축 합의 + 사용자 명시 결정** (T2 정책 영역) — 또는 보수적 풀 3+1 합의 |
| **PC-4** | T2 + T3 혼합 | ❌ 불필요 | N/A | ✅ 있음 | **⚠️ 中** (dev 환경 강제 sub-영역 = T3 부분 중첩) | **2 sub-영역 분리** — T2 sub (config 정의) = 단축 합의 / T3 sub (dev 환경 강제) = 풀 3+1 합의 + 외부 LLM 1+ |

### 2.5 본 §2 의 *범위 한계*

본 §2 = *3 항목 보강 가능성 분석 + 영역 분류 한정*. 다음은 본 §2 영역 외:

- ❌ ST-1 / ST-2 / PC-4 *채택 결정* (수단 결정 = 별도 합의 영역)
- ❌ 진입 *순서 결정* (3 항목 진입 순서 = 별도 합의 영역)
- ❌ 통합 합의 vs 분리 합의 *결정* (Backlog #1 단독 vs Backlog #1 + #2 통합 = 별도 합의 영역)
- ❌ inotify event 응답 시간 threshold *고정* (mvp1.md §3.4.2 답습 — 후보 한정 유지)

---

## 3. 합의 형태 권고 + 풀 3+1 승격 트리거 후보

### 3.1 본 brief 자체의 합의 형태

| 영역 | 합의 형태 권고 | 사유 |
|------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 (`backlog6-implementation-step-brief.md` §8.1 패턴 답습) |
| brief 승인 후 합의 진입 | **사용자 명시 결정 영역** | 항목별 합의 형태 분리 (§3.2 답습) |

### 3.2 항목별 합의 형태 권고 (보강 발효 시점)

| 항목 | 합의 형태 권고 | 사유 | 답습 출처 |
|------|----------|------|---------|
| ST-1 | **풀 3+1 합의 + Hermes upstream PR 검토 + 외부 LLM 1+ + 사용자 명시** | T3 영역 (Hermes upstream 변경) — 사용자 명시 답습 (T3 자동 진입 금지) | mvp1.md §3.6.3 + §3.5 R-MVP1-G3-7 답습 |
| ST-2 | **단축 합의 + 사용자 명시 결정** 또는 **보수적 풀 3+1 합의** | T2 영역 + Hermes upstream 변경 0건 + sidecar 운영 부담 中 | mvp1.md §3.3.2 ("MVP-1 1.5차 보강 = ST-3 + ST-2") + §3.6.3 답습 |
| PC-4 T2 sub-영역 | **단축 합의 + 사용자 명시 결정** | T2 정책 영역 (ADR-011 §2.4 답습) | mvp1.md §4.3.2 + §4.7.3 답습 |
| PC-4 T3 sub-영역 | **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** | T3 dev 환경 정책 영역 (Backlog #3 와 부분 중첩) | mvp1.md §4.3.1 + ADR-011 §2.4 답습 |

### 3.3 본 brief 의 풀 3+1 승격 트리거 후보 (7 트리거 답습)

본 brief 가 풀 3+1 합의로 *승격* 되어야 할 trigger 후보 (backlog6-brief.md §8.2 + 직전 Reviewer-only 합의 7 트리거 답습):

| # | 트리거 | 본 brief 검토 결과 |
|---|----|------------|
| 1 | 본 brief 가 9 sub-수단 *외* 수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — 본 brief = ST-1/ST-2/PC-4 영역 *분류* 한정 (Layer B §5.5 본문 채택 4 sub-수단 GP-3 변경 0건) |
| 2 | 본 brief 가 T3 영역 (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection) 자동 진입을 권고하는 경우 | ❌ 0건 발화 — 본 brief = T3 영역 진입 시 *별도 풀 3+1 합의 + 외부 LLM + 사용자 명시* 명시, 자동 진입 0건 |
| 3 | 본 brief 가 9 sub-수단 *재결정* 을 권고하는 경우 (Layer B §5.5 본문 채택 변경 trigger) | ❌ 0건 발화 — 본 brief = §5.5 본문 채택 변경 0건 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | ❌ 0건 발화 — 본 brief = GP-3 저장 경로 + pre-commit framework 영역, Provider Liquidity 영역 영향 0건 |
| 5 | 본 brief 가 5 영구 핵심 제약 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리) 中 1+ 의 약화를 포함하는 경우 | ❌ 0건 발화 — 본 brief = Hermes ≠ root of trust 보존 + T3 분리 보존 + 수단/목적 분리 보존 |
| 6 | 본 brief 가 MVP-1 PASS *재선언* / Layer E / Layer F 격상을 포함하는 경우 | ❌ 0건 발화 — 본 brief = 사용자 명시 답습, MVP-1 PASS 재선언 / Layer E / Layer F 격상 0건 |
| 7 | 본 brief 가 외부 LLM cross-vendor blind 의뢰 *없이* T3 영역 결정을 권고하는 경우 | ❌ 0건 발화 — 본 brief = T3 영역 진입 시 풀 3+1 + 외부 LLM 1+ 권고 |

**본 brief 검토 결과 = 7/7 트리거 0건 발화** (본 brief = 보강 가능성 *영역 분류* 한정 + T3 자동 진입 0건 + 5 영구 핵심 제약 보존 답습).

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** 확정 (사용자 명시 결정 시).

### 3.4 본 §3 의 *범위 한계*

본 §3 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역.

---

## 4. Rollback Trigger / Evidence 기준 (보강 발효 시점 의무)

### 4.1 본 §4 의 *명확한 한계*

본 §4 = **Backlog #1 보강 *발효 시점* 의무 정리 한정**. 본 brief 자체 시점에서:

- ❌ 실 rollback fixture 생성 0건
- ❌ 실 trigger 발화 시연 0건
- ❌ Trigger threshold 정량 *고정* 0건 (모두 *후보 한정* 유지)
- ❌ 실 evidence artifact 생성 0건

### 4.2 ST-1 / ST-2 / PC-4 별 Rollback Trigger 답습 (mvp1.md §3.5 + §4.6 답습)

| Trigger ID | 항목 | 발화 조건 | 발화 시 행동 | 본 brief 발효 시점 행동 |
|----------|------|---------|-------------|------------------|
| R-MVP1-G3-7 | ST-1 / ST-5 진입 | Hermes upstream Dockerfile 변경 결정 | 풀 3+1 합의 + Hermes upstream PR 검토 | (현 brief = 미발화 — ST-1 진입 0건) |
| R-MVP1-G3-3 | ST-2 진입 | Docker secret 도입 실패 후 보강 진입 | 풀 3+1 합의 + Backlog #1 (ST-2 inotify) 진입 검토 | (현 brief = 미발화 — Stage 2 ST-3 SUCCESS 답습) |
| R-MVP1-G3-4 | PC-4 (PC-3 sub) | PC-3 CI runtime 폭증 (>2분) | threshold 재결정 합의 (단축 적격) | (현 brief = 미발화 — Stage 4 PC-3 SUCCESS 답습) |
| R-MVP1-G3-5 | PC-4 (AR-1 sub) | AR-1 hook 우회 시도 패턴 검출 | T3 영역 → 풀 3+1 합의 + branch protection rule 변경 검토 (Backlog #3) | (현 brief = 미발화 — Stage 4 AR-1 SUCCESS 답습) |
| R-MVP1-G3-7 (재) | PC-4 dev 환경 강제 | dev 환경 정책 강제 진입 | T3 영역 부분 진입 — 풀 3+1 합의 권고 | (현 brief = 미발화 — PC-4 진입 0건) |

### 4.3 Evidence 기준 답습 (mvp1.md §3.6.1 + ADR-011 §2.1 (a)~(e) 답습)

보강 *발효 시점* 의무 evidence (본 brief 영역 외):

| Evidence | 형식 | ST-1 적용 | ST-2 적용 | PC-4 적용 |
|----------|------|----------|----------|----------|
| (a) 동등 이상의 보안 결과 | docker secret + chmod 600 + entrypoint stat + inotify 동작 확인 (GP-3 §5.4 답습) | ✅ entrypoint stat 검증 추가 | ✅ inotify 감시 추가 | (PC-3 답습 + pre-commit framework 추가) |
| (b) 격리 환경 PoC 실증 | docker secret 누락 / chmod 644 / mtime 변경 → 컨테이너 정지 시연 | ✅ chmod 644 시뮬레이션 + entrypoint stat fail evidence | ✅ mtime 변경 시뮬레이션 + 컨테이너 정지 evidence | (의도적 violation commit → pre-commit reject 시연) |
| (c) ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + R2-1 + GP-3 §5.3 + mvp1.md §3 답습 | ✅ | ✅ | mvp1.md §4.3 + §5.5.1/.2 답습 |
| (d) 자동 회귀 검증 경로 확보 | entrypoint stat 검증 매 컨테이너 시작 시 강제 + inotify nightly 또는 매 PR 실행 | ✅ | ✅ | `.pre-commit-config.yaml` 답습 매 commit 시 강제 + CI step 통합 (PC-3 답습) |
| (e) 합의 APPROVE | 항목별 합의 형태 (§3.2 답습) | 풀 3+1 + Hermes PR | 단축 또는 풀 3+1 | T2 sub = 단축 / T3 sub = 풀 3+1 |

### 4.4 JSONL Ledger entry 형식 후보 (Backlog #5 답습 — `4221646` + `2ece90a` + `b705370`)

보강 발효 시점 evidence ledger entry 후보 (Backlog #5 ADR-012 §2.2 정식 등록 8 enum 답습 + 추가 후보):

| event enum (후보) | trigger | T1/T2/T3 | Backlog #5 등록 상태 |
|------------------|---------|---------|------------------|
| `secret_storage_isolation_enhanced` (가칭 — ST-1 / ST-2 보강 시) | ST-1 / ST-2 발효 시 | T2 + T3 | ❌ 미등록 (Backlog #5 추가 등록 별도 합의 영역) |
| `pre_commit_framework_dev_enforcement` (가칭 — PC-4 발효 시) | PC-4 발효 시 | T2 + T3 | ❌ 미등록 (Backlog #5 추가 등록 별도 합의 영역) |

본 enum 후보 = **본 brief 권고 한정** — 정식 등록 = Backlog #5 ADR-012 §2.2 schema 갱신 별도 합의 영역 (`b705370` 답습 후속 추가 등록 영역).

### 4.5 본 §4 의 *범위 한계*

본 §4 = **보강 *발효 시점* 의무 정리 한정**. 다음은 본 §4 영역 외:

- ❌ 실 rollback fixture 생성 (보강 *발효 시점* 별도 작업)
- ❌ 실 trigger 발화 시연 (보강 *발효 시점* 별도 작업)
- ❌ Trigger threshold 정량 *고정* (>2분 / inotify 응답 < 1초 등 모두 *후보 한정* 유지)
- ❌ 실 evidence artifact 생성 (보강 *발효 시점* 별도 작업)
- ❌ 신규 event enum 정식 등록 (Backlog #5 별도 합의 영역)

---

## 5. 금지 사항

### 5.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | MVP-1 PASS *재선언* (Layer D 본문 변경) | 0건 |
| 2 | Operational Readiness PASS (Layer E) 선언 | 0건 |
| 3 | Hermes PMO 격상 (Layer F) | 0건 |
| 4 | T3 영역 *자동 진입* (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제) | 0건 |
| 5 | Backlog #1 진입 합의 발효 | 0건 |
| 6 | 실 runtime code 구현 (Hermes Dockerfile / inotify sidecar / `.pre-commit-config.yaml`) | 0건 |
| 7 | 실 CI workflow / hook 구현 | 0건 |
| 8 | 수단 *결정* (ST-1 / ST-2 / PC-4 채택) | 0건 |
| 9 | §5.5 9 sub-수단 본문 채택 *변경* (4 sub-수단 GP-3 / 3 sub-수단 GP-5 유지) | 0건 |
| 10 | threshold *고정* (FP/FN/latency/inotify event 응답 시간 등) | 0건 |
| 11 | Tier-2 / Tier-3 catalog 자동 확장 (R-4.1 Tier-1 45 patterns 답습) | 0건 |
| 12 | ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경) | 0건 |
| 13 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 14 | C-1~C-8 상태 *자동 변경* (§C-5 단독 진입 *준비* 한정 — C-2~C-8 자동 변경 0건) | 0건 |
| 15 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 16 | git commit / push | 0건 |
| 17 | 외부 LLM 자동 호출 | 0건 |
| 18 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 19 | 다른 backlog (#2/#3/#4/#7) 자동 진입 | 0건 |
| 20 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 21 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 22 | Provider Liquidity 5-way 약화 가능성 | 0건 |
| 23 | 5 영구 핵심 제약 약화 (Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 / Provider Liquidity) | 0건 |

### 5.2 본 brief 발효 *후* Backlog #1 진입 단계 금지 사항 (진입 시 의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | T3 영역 *자동 진입* (사용자 명시 결정 없이) | 사용자 명시 답습 + ADR-011 §2.4 답습 |
| 2 | Hermes upstream Dockerfile 변경 *결정* (ST-1 / ST-5 진입) | 풀 3+1 합의 + Hermes upstream PR 검토 + 외부 LLM 1+ + 사용자 명시 의무 |
| 3 | PC-4 dev 환경 강제 sub-영역 *단축 진입* | T3 영역 부분 중첩 — 풀 3+1 합의 권고 |
| 4 | 본 3 항목 외 수단 *재결정* (S-3 detect-secrets / S-2 gitleaks / T-1 depcruise 등 1.5차 보강 추가 항목 자동 진입) | 별도 합의 영역 (Backlog #1 + #2 분리 매트릭스 답습) |
| 5 | Vault HSM (ST-4) 진입 | Backlog #7 Operational Readiness 영역 분리 (ADR-010 §X 진입 합의 + Multi-host 인프라 검토) |
| 6 | branch protection rule 변경 (AR-2 / AR-3) | Backlog #3 T3 영역 별도 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| 7 | Tier-2 / Tier-3 catalog 확장 (R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 변경) | Backlog #3 별도 합의 영역 |
| 8 | ADR 본문 자동 갱신 (ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 / R2-1 본문 변경) | cross-reference 답습 한정 — 보강 발효 후 별도 commit 영역 |
| 9 | event enum 정식 등록 (`event:` field 신규 추가) | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 10 | MVP-1 PASS *재선언* (Layer D 본문 변경) | 별도 합의 + 사용자 명시 결정 |
| 11 | Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) | MVP-6 영역 — 별도 합의 + 외부 LLM cross-vendor blind + 사람 리뷰 의무 |
| 12 | 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 13 | 실 secret 본문 commit | 영구 금지 (R-4.1 + Group D §1.2 #1 답습) |
| 14 | F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 15 | 외부 LLM 자동 호출 (사용자 명시 결정 없이) | T3 영역 진입 시 의무 충족 후 별도 단계 |

본 §5 = **사용자 명시 답습 한정** — 본 brief 발효 후 Backlog #1 진입 단계에서 위 15 금지 영역 위반 0건 유지 의무.

---

## 6. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** (Backlog #1 §C-5 진입 적격성 한정 — 항목별 진입 결정은 별도 합의) | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md`) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | ST-2 단독 우선 진입 (T3 자동 진입 0건 조건 충족 유일 항목) | ST-2 단독 합의 보고서 작성 (단축 합의 또는 풀 3+1) |
| (D) | PC-4 T2 sub-영역 단독 우선 진입 (config 정의 한정 — 단축 합의 적격) | PC-4 T2 sub 단독 합의 보고서 작성 |
| (E) | Backlog #1 보류 → Backlog #2 (GP-5 1.5차) 우선 brief 작성 (PC-4 공유 영역 통합 검토) | Backlog #2 brief 작성으로 전환 |
| (F) | Backlog #1 보류 → MVP-2 진입 합의 우선 (G2 GP-2 + G4 §4.4 Layer 4) | MVP-2 deepening brief 또는 진입 합의 |
| (G) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 6.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A)로 진행해주세요. 본 brief를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- **(C) 권고 (보수적)**: "옵션 (C)로 진행해주세요. ST-2 단독 우선 진입 합의 보고서 작성으로 진입합니다. (T3 자동 진입 0건 조건 충족)"
- (B): "옵션 (B)로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (D): "옵션 (D)로 진행해주세요. PC-4 T2 sub 단독 합의 보고서 작성으로 진입합니다."
- (E): "옵션 (E)로 진행해주세요. Backlog #2 brief 작성으로 전환합니다."
- (F): "옵션 (F)로 진행해주세요. MVP-2 진입 합의 단계로 전환합니다."
- (G): "옵션 (G)로 진행해주세요. 세션 종료."

### 6.2 본 §6 의 *범위 한계*

본 §6 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 7. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (5/5 — Backlog #1 범위 정비 / ST-1 / ST-2 / PC-4 보강 가능성 검토 / 4 금지 답습) |
| 사용자 명시 금지 답습 | ✅ (4/4 — MVP-1 PASS 재선언 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건 / T3 영역 자동 진입 0건) |
| §5.5 9 sub-수단 본문 채택 답습 | ✅ (변경 0건 — 4 sub-수단 GP-3 + 3 sub-수단 GP-5 + 2 공유 유지) |
| C-1~C-8 상태 답습 | ✅ (C-1 Satisfied + C-2 Satisfied + C-3~C-8 Deferred/Requires separate — 변경 0건) |
| MVP-1 PASS Layer D 본문 답습 | ✅ (`210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ (§2.4 답습 — T3 영역 자동 진입 0건 / T2 영역 단축 합의 적격 명시) |
| ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 답습 | ✅ (cross-reference 답습 한정 — 본문 변경 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Provider Liquidity 5-way / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 모두 답습) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #2 / #3 / #4 / #5 / #7 모두 분리 명시 — 자동 진입 0건) |
| 풀 3+1 승격 트리거 0/7 발화 | ✅ (§3.3 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| 합의 보고서 0건 / commit 0건 / push 0건 | ✅ (본 brief = 준비안 한정) |

---

## 8. 본 brief 요약 (한 단락)

본 brief 는 **MVP-1 PASS (Layer D) `210c98f` APPROVE WITH CONDITIONS + §C-1 Satisfied 갱신 (`1dd1036`) 발효 후속**, **Backlog #1 (GP-3 1.5차 보강 — ST-1 / ST-2 / PC-4) 진입 *직전* 의 *준비안 (DRAFT)*** 이다. 3 항목을 영역 분류 매트릭스 (ST-1 = T3 영역, Hermes upstream 변경 필요 / ST-2 = T2 영역, Hermes upstream 변경 0건 + sidecar 분리 가능 / PC-4 = T2 + T3 혼합, 2 sub-영역 분리 가능) 로 정비하고, 항목별 합의 형태 권고 (ST-1 = 풀 3+1 + Hermes upstream PR + 외부 LLM 1+ / ST-2 = 단축 합의 또는 풀 3+1 / PC-4 T2 sub = 단축 합의 / PC-4 T3 sub = 풀 3+1 + 외부 LLM 1+), 보강 발효 시점 Rollback Trigger 답습 (R-MVP1-G3-3 / G3-4 / G3-5 / G3-7) + Evidence 기준 (ADR-011 §2.1 (a)~(e) 5조건 답습), 본 brief 자체 금지 23 + Backlog #1 진입 단계 금지 15, 합의 형태 권고 (Reviewer-only 단축 — 7 풀 3+1 트리거 0/7 발화) 를 정리한다. **본 brief 는 Backlog #1 진입 합의를 *시작* 시키지 않으며, MVP-1 PASS *재선언* / Operational Readiness PASS / Hermes PMO 격상 / T3 영역 자동 진입 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외** (사용자 명시 답습). 다음 단계는 사용자 명시 결정 영역 (옵션 A~G, §6 답습).

---

**작성일**: 2026-05-13 후속 24
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~G, §6 답습)
**금지 (사용자 명시 답습 — 본 brief 영역, 변동 없음)**:
- ❌ MVP-1 PASS *재선언*
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ T3 영역 *자동 진입* (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제)
- ❌ Backlog #1 진입 합의 발효
- ❌ 실 runtime code / CI workflow / hook 구현
- ❌ 수단 *결정* (ST-1 / ST-2 / PC-4 채택)
- ❌ §5.5 9 sub-수단 본문 채택 *변경*
- ❌ threshold *고정*
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ ADR 본문 자동 갱신
- ❌ 합의 보고서 작성
- ❌ C-1~C-8 상태 *자동 변경*
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 다른 backlog (#2/#3/#4/#7) 자동 진입
