# Backlog #6 Layer B 발효 후 — Runtime Code / CI Workflow / Hook 구현 진입 Brief (준비안 — DRAFT)

> **본 문서는 Backlog #6 Layer B Implementation Entry 합의 (`docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md`, commit `f40423f` APPROVE) 발효 + 9 sub-수단 본문 채택 (`implementation-runtime-roadmap-mvp1.md` §5.5, commit `55c5b4b`) 발효 후속, *실 구현 단계 진입 준비* 의 brief 준비안 한정.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) 실 구현 진입을 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) Layer C (Implementation Evidence PASS) 발효를 발생시키지 않는다.

**작성일**: 2026-05-12 후속
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위**:
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-12-mvp1-implementation-entry.md` (MVP-1 Implementation Entry READY, commit `1eab814`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "runtime code / CI workflow / hook 구현 진입 brief 준비안 작성으로 시작해주세요. 범위는 Layer B에서 본문 채택된 9 sub-수단을 실제 구현 단계로 어떻게 나눌지, 구현 순서, 파일 범위, evidence 기준, rollback trigger, 금지 사항을 정리하는 것까지로 제한하고, 아직 runtime code 구현, CI workflow 구현, hook 구현, Implementation Evidence PASS 선언은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. Layer B 발효 + §5.5 본문 채택 답습 후속의 *실 구현 단계 진입 준비* 사전 정비
2. 9 sub-수단을 실제 구현 단계로 *어떻게 나눌지* 분할안 권고 (§2)
3. 구현 *순서* 권고 (의존성 + 동시 진입 가능성, §3)
4. 실 구현 시 영향 *파일 범위* 후보 enumeration (§4)
5. Layer C (Implementation Evidence PASS) 진입 시점 *evidence 기준* 정리 (§5)
6. *Rollback trigger* 18개 본문 확정 답습 + 실 구현 단계 발화 시연 적격 영역 정리 (§6)
7. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§7)
8. 본 brief 의 *합의 형태 권고* + 풀 3+1 승격 트리거 후보 (§8)
9. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

- ❌ **실 runtime code 구현 (0건)** — `tools/secret_scanner.py` 본문 변경 / `tools/provider_import_scanner.py` 본문 변경 / `tools/provider_url_scanner.py` 본문 변경 / `src/adapters/llm/facade.py` 본문 작성 / inotify sidecar 본문 / chmod 600 entrypoint script 본문 0건
- ❌ **실 CI workflow 구현 (0건)** — `.github/workflows/secret-scan.yml` 신설 / `.github/workflows/provider-*.yml` 본문 변경 / `.github/workflows/combined-check.yml` 신설 / `secret-hygiene-egress-redaction.yml` 본문 변경 0건
- ❌ **실 hook 구현 (0건)** — `.pre-commit-config.yaml` 신설 / `.git/hooks/pre-commit` 본문 작성 / `.importlinter` 본문 변경 0건
- ❌ **Implementation Evidence PASS (Layer C) 발효 0건**
- ❌ **MVP-1 PASS (Layer D) 선언 0건**
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ **ADR 본문 자동 갱신 0건** (cross-reference 답습 한정)
- ❌ **수단 *재결정* 0건** (Layer B §5.5 본문 채택 답습 한정 — 9 sub-수단 변경 0건)
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건**
- ❌ **threshold *고정* 0건** (FP/FN/latency 모두 *후보 한정* 유지)
- ❌ **합의 보고서 작성 0건** (본 brief = *준비안 한정* — 합의 보고서 = 사용자 명시 승인 후속 영역)
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건** (사용자 명시 단계 분리 영역)
- ❌ **git commit / push 0건**
- ❌ **외부 LLM 자동 호출 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**

### 0.4 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) 실 구현을 *시작* 시키지 않으며,
- (ii) Layer C 진입을 *발효* 시키지 않으며,
- (iii) 9 sub-수단 본문 채택 §5.5 를 *변경* 하지 않으며,
- (iv) 신규 ADR / 신규 P / 신규 GP 를 *발행* 하지 않으며,
- (v) MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **실 구현 단계 진입 *직전* 의사결정 입력 정비 — 구현 단계 분할 + 순서 + 파일 범위 + evidence 기준 + rollback trigger + 금지 사항 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습 (Layer B 발효 결과)

### 1.1 6-layer 분리 매트릭스 현 상태 (2026-05-12 후속 10)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| **Layer B** | **9 sub-수단 본문 채택 격상 + 구현 시작 권한 발효 적격성** | ✅ **APPROVE (`f40423f` + §5.5 본문 채택 `55c5b4b`)** | **본 brief = Layer B 발효 결과 *행사 준비*** |
| Layer C | Implementation Evidence PASS 발효 | ⏳ 아직 아님 | 본 brief = Layer C 진입 *준비* 한정 (Layer C 발효 아님) |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 |

### 1.2 본 brief 의 진입점 = Layer B → Layer C 사이 *실 구현* 진입 *직전*

본 brief 의 진입점:

```
Layer A APPROVE (f1e0b23)
   │
   ▼
Layer B APPROVE (f40423f) — 시작 권한 발효 적격성 권위 권고
   │
   ▼
§5.5 9 sub-수단 본문 채택 (55c5b4b) — 문서상 확정 한정
   │
   ▼
■ 본 brief = 실 구현 단계 진입 *준비안* (DRAFT)         ← 현 위치
   │
   ▼ (사용자 명시 승인 후)
brief 그대로 승인 합의 보고서 작성
   │
   ▼ (사용자 명시 결정 후)
■ 실 구현 진입 (runtime code / CI workflow / hook)    ← 본 brief 영역 외
   │
   ▼ (구현 + actual run SUCCESS + evidence 5/5 후)
Layer C 발효 합의 — Implementation Evidence PASS      ← 본 brief 영역 외
```

### 1.3 9 sub-수단 본문 채택 답습 (Layer B §1.1 + §1.2 + mvp1.md §5.5 답습)

| GP | sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) |
|----|----------|------|----------------------|
| **GP-3** | **S-1** | 코드 본문 secret 검출 (custom regex, R-4.1 Tier-1 45 patterns) | Group D PoC `tools/secret_scanner.py` 261줄 답습 |
| **GP-3** | **ST-3** | 저장 경로 (docker secret) | ADR-008 §2.6.2 R2-1 답습 |
| **GP-3** | **G3-7 (i)** | GitHub Actions secrets 사용 0건 검증 (F-금지 grep step) | Layer A §1.2 답습 |
| **GP-3** | **G3-7 (ii)** | `secrets.*` 참조 감지 (workflow grep step or S-1 확장) | 동상 |
| **GP-3** | **G3-7 (iv)** | fork PR secret 접근 차단 default 정책 보존 | 동상 |
| **GP-3** | **G3-7 (v)** | workflow `permissions: contents: read` 명시 강제 (R-6 답습) | 동상 |
| **GP-5** | **T-6 (T-2 + T-5)** | Layer 1 정적 차단 (import-linter + custom AST 병행) | Group A 1차/2차/3차 PoC 답습 + `.importlinter` TR-1~TR-5 답습 |
| **공유** | **PC-3** | CI-only enforcement (pre-commit) | 양 GP 일관성 답습 |
| **공유** | **AR-1** | CI step fail-closed (PR auto-reject) | 양 GP 일관성 답습 |

**합산 = 9 sub-수단 (GP-3 단독 6 + GP-5 단독 1 + 공유 2)**.

> mvp1.md §5.5.3 의 합산 매트릭스는 G3-7 4 항목을 단일 본문 채택 단위로 집계하여 "9 sub-수단 (7 unique + 2 공유 중복)" 으로 기록함. 본 brief §1.3 은 G3-7 4 항목을 *구현 step 분할 단위* 로 풀어 표시 — 동일 본문 채택 답습, 표현 단위 차이만 존재 (mvp1.md §5.5 답습 권위 변경 0건).

---

## 2. 9 sub-수단 → 실 구현 단계 분할안

### 2.1 구현 단계 분할 (5 단계 권고)

본 brief 권고 = 9 sub-수단을 **5 구현 단계 (Stage 1~5)** 로 분할:

| Stage | 영역 | 포함 sub-수단 | 기존 PoC 답습 vs 신규 작업 |
|-------|------|----------|-----------------------|
| **Stage 1** | **GP-3 코드 본문 검출 확장** | S-1 | Group D `tools/secret_scanner.py` 261줄 답습 + MVP-1 entry 확장 (CI workflow 호환 + ledger entry 형식) |
| **Stage 2** | **GP-3 저장 경로 isolation** | ST-3 | ADR-008 §2.6.2 답습 + `docker-compose.yml` (또는 동등 매니페스트) docker secret 정의 + Hermes upstream 변경 0건 |
| **Stage 3** | **GP-5 Layer 1 정적 차단** | T-6 (T-2 + T-5) | Group A 1차/2차/3차 답습 + `.importlinter` 본문 확정 + `tools/provider_import_scanner.py` + `tools/provider_url_scanner.py` MVP-1 entry 확장 |
| **Stage 4** | **공유 — PC-3 + AR-1 통합** | PC-3 + AR-1 | 양 GP 일관성 답습 — CI step 통합 / fail-closed 통합 / 단일 CI workflow 또는 cross-workflow cross-reference |
| **Stage 5** | **G3-7 — CI secret 관리 4 항목** | G3-7 (i)+(ii)+(iv)+(v) | 신규 CI step 4 항목 또는 기존 workflow 확장 (S-1 활용 가능성) |

### 2.2 각 Stage 의 sub-step 분할

#### 2.2.1 Stage 1 — GP-3 S-1 (코드 본문 검출 확장)

| sub-step | 영역 | 답습 출처 | 본 brief 권고 (구현 *시* — 본 brief 영역 외) |
|---------|------|---------|---------------------------------------|
| 1.1 | `tools/secret_scanner.py` 본문 답습 검증 | Group D PoC §2.1 (A) | 261줄 답습 변경 0건 + R-4.1 Tier-1 45 patterns 답습 변경 0건 |
| 1.2 | MVP-1 entry CI 통합 — `.github/workflows/secret-hygiene-egress-redaction.yml` 확장 | Group D 12 step 답습 | step 추가 또는 step 통합 (Stage 4 PC-3 + AR-1 통합과 함께) |
| 1.3 | ledger entry 형식 — `event: secret_scan_layer1_implementation` 사용 | mvp1.md §5.2 enum 후보 답습 | enum 후보 → *후보 한정* 유지 (정식 등록 = Layer C 시점 권고, Backlog #5 분리) |
| 1.4 | Evidence Artifact 생성 — Markdown report + JSONL entry + actual run SUCCESS URL | Layer B §1.8 (a) 답습 | Layer C 진입 시점 의무 (본 brief 영역 외) |

#### 2.2.2 Stage 2 — GP-3 ST-3 (저장 경로 isolation)

| sub-step | 영역 | 답습 출처 | 본 brief 권고 |
|---------|------|---------|-----------|
| 2.1 | `docker-compose.yml` (또는 동등 매니페스트) docker secret 정의 | ADR-008 §2.6.2 R2-1 답습 | docker secret block 추가 + Hermes upstream Dockerfile 변경 0건 |
| 2.2 | docker secret 파일 *image layer* 미포함 검증 | mvp1.md §3.4.2 `docker_secret_isolation_check` 답습 | image layer 검증 step 추가 (CI 또는 별도 docker build check) |
| 2.3 | 컨테이너 재시작 시 secret 재주입 정상 검증 | mvp1.md §3.4.2 `container_restart_recovery` 답습 | restart fixture 추가 (PoC 격리 환경) |
| 2.4 | Evidence — Docker isolation log | Layer B §1.8 (a) 답습 | chmod 644 / mtime 변경 시뮬레이션 + 컨테이너 정지 evidence (Layer C 시점) |

**분리 영역** (Stage 2 영역 외):
- ST-1 entrypoint stat / ST-2 inotify sidecar = Backlog #1 1.5차 보강 영역 (본 brief 영역 외)
- ST-4 Vault HSM = Backlog #7 Operational Readiness 영역 (본 brief 영역 외)
- Hermes upstream Dockerfile 변경 = T3 영역 (별도 합의)

#### 2.2.3 Stage 3 — GP-5 T-6 (Layer 1 정적 차단)

| sub-step | 영역 | 답습 출처 | 본 brief 권고 |
|---------|------|---------|-----------|
| 3.1 | `.importlinter` 본문 확정 (TR-1~TR-5 답습) | Group A 2차 합의 §5.5 답습 | 5-vendor 차단 rule 답습 변경 0건 (anthropic / openai / litellm / google.generativeai / ollama) |
| 3.2 | `tools/provider_import_scanner.py` 본문 답습 검증 | Group A 1차 PoC 답습 | AST 5 패턴 답습 변경 0건 |
| 3.3 | `tools/provider_url_scanner.py` 본문 답습 검증 | Group A 3차 PoC 답습 | URL Tier-1 10 + Model Tier-1 19 답습 변경 0건 |
| 3.4 | `.github/workflows/provider-adapter-enforcement.yml` 통합 확장 (Layer 1a + 1b + 1c 통합 또는 cross-workflow) | Group A 2차 CI workflow 답습 | 통합 형태 권고 — 단일 workflow 또는 cross-workflow cross-reference (구현 *시* 결정) |
| 3.5 | ledger entry — `event: provider_adapter_enforcement_layer1_static` | mvp1.md §5.2 enum 후보 답습 | enum 후보 → *후보 한정* 유지 |
| 3.6 | Evidence Artifact | Layer B §1.8 (a) 답습 | Layer C 시점 의무 (5-vendor + URL Tier-1 10 + Model Tier-1 19 cover) |

**분리 영역**:
- P1 v2 facade real 본문 (`src/adapters/llm/facade.py`) = Backlog #4 영역 (본 brief 영역 외 — `.importlinter` ignore_imports 검증 trigger 발화 시 별도 합의)
- Layer 2 runtime block (G5-5) = MVP-3 영역
- 의미적 lock-in (G4 §4.6) = MVP-3 영역

#### 2.2.4 Stage 4 — 공유 PC-3 + AR-1 (CI-only enforcement + fail-closed)

| sub-step | 영역 | 답습 출처 | 본 brief 권고 |
|---------|------|---------|-----------|
| 4.1 | PC-3 CI step 통합 — Stage 1 + Stage 3 의 CI step 을 단일 또는 cross-workflow 형태로 통합 | Layer B §1.1 + §1.2 답습 | 통합 형태 = 단일 workflow vs cross-workflow 결정 (구현 *시* 결정) |
| 4.2 | AR-1 fail-closed — 각 step exit code 1 시 PR check failure | Group D + Group A 답습 | Group D + Group A PoC actual run 답습 변경 0건 |
| 4.3 | local pre-commit framework PC-4 = 미진입 | Backlog #1 + #2 1.5차 보강 영역 분리 | 본 brief 영역 외 |
| 4.4 | branch protection rule AR-2 = 미진입 | Backlog #3 T3 영역 별도 풀 3+1 분리 | 본 brief 영역 외 |

#### 2.2.5 Stage 5 — G3-7 CI secret 관리 4 항목

| sub-step | 영역 | 답습 출처 | 본 brief 권고 |
|---------|------|---------|-----------|
| 5.1 | G3-7 (i) — GitHub Actions secrets 사용 0건 grep step | mvp1.md §3.1.2 G3-7 row 답습 | F-금지 grep step 답습 — workflow 본문에서 `secrets.` 토큰 0건 검증 (생성 *시* 실 패턴 결정) |
| 5.2 | G3-7 (ii) — `secrets.*` 참조 감지 (workflow grep step or S-1 확장) | 동상 | S-1 확장 vs workflow 별도 grep step 결정 (구현 *시*) |
| 5.3 | G3-7 (iv) — fork PR secret 접근 차단 default 정책 보존 | 동상 | GitHub Actions default 정책 답습 검증 (변경 0건) |
| 5.4 | G3-7 (v) — workflow `permissions: contents: read` 명시 강제 | R-6 답습 | 모든 신규/기존 workflow 헤더 `permissions:` block 확인 |

**분리 영역**:
- G3-7 (iii) CI 로그 secret 노출 방지 = MVP-2 (GP-2 송신 redaction 영역)
- `pull_request_target` workflow 도입 = 별도 합의 영역 (T2/T3)

### 2.3 분할 합산 매트릭스

| Stage | sub-수단 | sub-step 수 | 신규 작업 비율 | 기존 PoC 답습 비율 |
|-------|----------|------------|------------|---------------|
| Stage 1 | S-1 | 4 | 中 (CI 통합 + ledger) | 高 (scanner 본문 답습) |
| Stage 2 | ST-3 | 4 | 中-高 (docker secret + 검증 step) | 中 (ADR-008 답습) |
| Stage 3 | T-6 (T-2 + T-5) | 6 | 中 (CI 통합) | 高 (3 PoC 답습) |
| Stage 4 | PC-3 + AR-1 | 4 | 中 (CI step 통합) | 高 (Group D + Group A PoC 답습) |
| Stage 5 | G3-7 4 항목 | 4 | 中-高 (4 grep step 신규) | 中 (R-6 + Group D 부분 답습) |
| **합산** | **9 sub-수단** | **22 sub-step** | — | — |

본 §2 = *분할안 권고 한정*. 실 분할 결정 = 사용자 명시 결정 영역.

---

## 3. 구현 순서 권고

### 3.1 의존성 그래프

```
Stage 1 (S-1) ──────┐
                    ├──→ Stage 4 (PC-3 + AR-1 통합)
Stage 3 (T-6) ──────┘            │
                                 ▼
Stage 2 (ST-3) ──────────────→ Stage 5 (G3-7)
   (선후 독립)                   │
                                 ▼
                          전체 통합 + Evidence
                          (Layer C 진입 준비)
```

**의존성 요약**:
- Stage 1 + Stage 3 = 양 GP 본문 검출 — 양쪽 독립 진행 가능 (PoC 답습 변경 0건)
- Stage 4 = Stage 1 + Stage 3 *완료 후* 통합 가능
- Stage 2 (ST-3) = Stage 1 / Stage 3 / Stage 4 와 *독립* — 양쪽 동시 진행 가능
- Stage 5 (G3-7) = Stage 1 (S-1 확장) + Stage 4 (CI step 통합) *후* 권고

### 3.2 권고 순서 옵션 (3 옵션)

| 옵션 | 순서 | 동시 진입 영역 | 예상 소요 | 권고 |
|-----|------|------------|--------|------|
| **순서 A (병렬 권고)** | (Stage 1 + Stage 3) 병렬 → Stage 2 → Stage 4 → Stage 5 → Evidence 통합 | Stage 1 + Stage 3 동시 | 中 | 권고 (양 GP 독립성 답습 + PoC 답습 비율 高) |
| **순서 B (순차)** | Stage 1 → Stage 3 → Stage 2 → Stage 4 → Stage 5 → Evidence 통합 | 0 | 高 | 비권고 (동시 진입 가능성 활용 X) |
| **순서 C (Stage 2 우선)** | Stage 2 → (Stage 1 + Stage 3) 병렬 → Stage 4 → Stage 5 → Evidence 통합 | Stage 1 + Stage 3 동시 | 中 | 비권고 (Stage 2 = docker secret 정의가 Stage 1/3 의 secret 활용 의존성 없음) |

**본 brief 권고 = 순서 A** (병렬 — Stage 1 + Stage 3 동시).

### 3.3 동시 진입 vs 순차 진입

- Stage 1 (S-1) + Stage 3 (T-6) = **동시 진입 적격** (PoC 답습 변경 0건 + 의존성 0)
- Stage 2 (ST-3) = **독립 진입 적격** (Stage 1 / Stage 3 / Stage 4 와 의존성 0)
- Stage 4 (PC-3 + AR-1 통합) = **Stage 1 + Stage 3 *완료 후* 의존**
- Stage 5 (G3-7) = **Stage 4 후속 권고** (G3-7 (i) = workflow 검증, Stage 4 통합 결과에 영향)

### 3.4 본 §3 의 *범위 한계*

본 §3 = *순서 권고 한정*. 실 구현 시 순서 결정 = 사용자 명시 결정 영역.

---

## 4. 파일 범위 (실 구현 영역 — 본 brief 영역 외)

### 4.1 본 §4 의 *명확한 한계*

본 §4 = **실 구현 진입 *후* 영향 받을 *후보* 파일 범위 enumeration**. 본 brief 자체는 **이 파일들을 변경하지 않음 (0건)**.

### 4.2 신규 파일 후보 (실 구현 시점 — 본 brief 영역 외)

| 파일 후보 | 영역 | Stage | 답습 출처 | 본 brief 영향 |
|---------|------|-------|---------|----------|
| `.github/workflows/mvp1-secret-scan.yml` (또는 `secret-hygiene-egress-redaction.yml` 확장) | Stage 1 + Stage 4 | Stage 1/4 | Group D `secret-hygiene-egress-redaction.yml` 답습 | 0건 (본 brief 영역 외) |
| `.github/workflows/mvp1-provider-enforcement.yml` (또는 `provider-adapter-enforcement.yml` 확장) | Stage 3 + Stage 4 | Stage 3/4 | Group A 2차 `provider-adapter-enforcement.yml` 답습 | 0건 |
| `.github/workflows/mvp1-combined-check.yml` (또는 별도 통합 step) | Stage 4 | Stage 4 | mvp1.md §5.4 통합 위험 매트릭스 답습 | 0건 |
| `docker-compose.yml` 또는 동등 매니페스트 docker secret block | Stage 2 | Stage 2 | ADR-008 §2.6.2 R2-1 답습 | 0건 |
| `docs/phase0/g2-gp3-mvp1-evidence.md` (Evidence Artifact) | Evidence 통합 | Layer C 시점 | mvp1.md §3.6.1 답습 | 0건 (Layer C 시점) |
| `docs/phase0/g2-gp5-mvp1-evidence.md` (Evidence Artifact) | Evidence 통합 | Layer C 시점 | mvp1.md §4.7.1 답습 | 0건 (Layer C 시점) |

### 4.3 기존 파일 확장 후보 (실 구현 시점 — 본 brief 영역 외)

| 파일 | 영역 | Stage | 답습 출처 | 본 brief 영향 |
|------|------|-------|---------|----------|
| `tools/secret_scanner.py` (Group D PoC 261줄) | Stage 1 | Stage 1 | Group D PoC 답습 | 0건 — 본 brief 는 답습 검증 한정 |
| `tools/provider_import_scanner.py` (Group A 1차 PoC) | Stage 3 | Stage 3 | Group A 1차 답습 | 0건 |
| `tools/provider_url_scanner.py` (Group A 3차 PoC) | Stage 3 | Stage 3 | Group A 3차 답습 | 0건 |
| `.importlinter` (Group A 2차 PoC) | Stage 3 | Stage 3 | Group A 2차 답습 | 0건 |
| `requirements-dev.txt` (import-linter + jcs + rfc8785) | Stage 3 | Stage 3 | Group A 2차 답습 | 0건 |
| `.github/workflows/secret-hygiene-egress-redaction.yml` (Group D, 12 step) | Stage 1 + Stage 4 | Stage 1/4 | Group D 답습 | 0건 |
| `.github/workflows/provider-adapter-enforcement.yml` (Group A 2차) | Stage 3 + Stage 4 | Stage 3/4 | Group A 2차 답습 | 0건 |
| `docs/evidence/ledger.jsonl` (실 evidence ledger) | Evidence 통합 | Layer C 시점 | ADR-012 §2.2 답습 | 0건 (Layer C 시점) |

### 4.4 변경 0건 영역 (사용자 명시 답습 — 본 brief + 본 brief 발효 후 단계 양쪽)

| 영역 | 변경 0건 사유 |
|------|------------|
| ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 | cross-reference 답습 한정 — 본 brief 영역 외 |
| `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3 / §4 / §5.1 / §5.2 / §5.3 / §5.4 / §6 / §7 본문 | §5.5 본문 채택 답습 한정 — 본 brief 영역 외 |
| `docs/architecture/implementation-runtime-roadmap.md` 17 항목 우선순위 | 17 항목 우선순위 *재고정* 0건 |
| Hermes upstream Dockerfile | Backlog #1 1.5차 보강 영역 분리 (ST-1 / ST-5 진입 시 풀 3+1 합의) |
| `src/adapters/llm/facade.py` (P1 v2 facade real) | Backlog #4 영역 분리 (P1 v2 facade MVP 합의) |
| GitHub branch protection rule (Web UI 또는 settings) | Backlog #3 T3 영역 분리 (별도 풀 3+1 합의 + 외부 LLM 1+) |
| Vault HSM 통합 | Backlog #7 Operational Readiness 영역 분리 |
| Tier-1 catalog (R-4.1 / URL Tier-1 10 / Model Tier-1 19) | 답습 한정 — 본 brief 영역 외 (Backlog #3 별도 합의 시 확장) |

### 4.5 본 §4 의 *범위 한계*

본 §4 = *파일 범위 후보 enumeration 한정*. 실 파일 변경 = 사용자 명시 결정 후 별도 commit 영역.

---

## 5. Evidence 기준 (Layer C 진입 시점 의무)

### 5.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (양 GP 공통)

본 §은 **Layer B §1.8 7 evidence 형태 답습** + **mvp1.md §5.1 답습**. Layer C 진입 시점 의무:

| # | 조건 | GP-3 evidence | GP-5 evidence |
|---|------|--------------|--------------|
| (a) | 동등 이상의 보안 결과 | S-1 결과 R-4.1 Tier-1 45 patterns 동등 이상 + ST-3 docker secret isolation 검증 PASS | T-6 (T-2 + T-5) 결과 §9.3 답습 동등 이상 + 5-vendor 동등 차단 |
| (b) | 격리 환경 PoC 실증 | docker secret 격리 + chmod 644 시뮬레이션 + 컨테이너 정지 시뮬레이션 + PR auto-reject 시뮬레이션 | import-linter + custom AST PR auto-reject 시뮬레이션 + facade single entry 시뮬레이션 |
| (c) | ADR / SDD 권위 명시 | ADR-008 §A.2 + ADR-010 + R-4 + GP-3 §5 + mvp1.md §3 + Layer B §1.1 | ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + GP-5 §7 + mvp1.md §4 + Layer B §1.2 |
| (d) | 자동 회귀 검증 경로 확보 | `mvp1-secret-scan.yml` (또는 통합) actual run SUCCESS + 매 PR + nightly 권고 | `mvp1-provider-enforcement.yml` (또는 통합) actual run SUCCESS + 매 PR + nightly 권고 |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 — Layer C 시점 별도 합의 + 사용자 명시 | 동상 |

### 5.2 Layer B §1.8 7 evidence 형태 답습

| Evidence | 형식 (Layer C 진입 시점) | 권고 |
|----------|---------------------|------|
| (a) GP-3 Implementation Evidence | `tools/secret_scanner.py` 확장 + workflow 확장 + 실행 log + actual run SUCCESS URL + 코드 diff + 4 patterns cover (alternation/prefix-baseline/regex/private-key T1-035) | Markdown report 형태 |
| (b) GP-3 Rollback Evidence | 8 rollback trigger 발화 시연 fixture + rollback artifact (CI run + summary.json + 30일 retention) | fixture + JSONL ledger entry |
| (c) GP-5 Implementation Evidence | `tools/provider_import_scanner.py` + `tools/provider_url_scanner.py` 확장 + `.importlinter` 본문 + workflow + 실행 log + actual run SUCCESS URL + 5-vendor + URL Tier-1 10 + Model Tier-1 19 cover | Markdown report 형태 |
| (d) GP-5 Rollback Evidence | 10 rollback trigger 발화 시연 fixture + rollback artifact | fixture + JSONL ledger entry |
| (e) Independent Verification | Reviewer-only 단축 또는 풀 3+1 합의 보고서 (Layer C 시점, ADR-010 + ADR-009 답습) | `docs/review/3plus1-consensus-<date>-mvp1-implementation-evidence.md` |
| (f) Permanent Constraint Preservation | 5 영구 핵심 제약 보존 검증 본문 + Provider Liquidity 5-way + Hermes ≠ root of trust + 메타포 강제 금지 + T3 분리 + 수단/목적 분리 | Markdown report 형태 |
| (g) No Auto-Promotion | Layer C 발효 후에도 MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 0건 유지 evidence (Layer D/E/F 별도 합의) | 0/N 위반 검증 |

### 5.3 JSONL Ledger entry 형식 (ADR-012 §2.2 답습)

| event enum (mvp1.md §5.2 후보) | trigger | T1/T2/T3 | Layer C 시점 정식 등록 |
|----------------------------|---------|---------|--------------------|
| `secret_scan_layer1_implementation` | Stage 1 (S-1) 완료 시 | T2 (CI step) | ⏳ Backlog #5 별도 합의 |
| `secret_storage_isolation_implementation` | Stage 2 (ST-3) 완료 시 | T2 (docker secret) | ⏳ Backlog #5 별도 합의 |
| `provider_adapter_enforcement_layer1_static` | Stage 3 (T-6) 완료 시 | T2 (CI step) | ⏳ Backlog #5 별도 합의 |
| `mvp1_gate_pass` | Layer D (MVP-1 PASS) 발효 시 | T3 (사용자 명시 + ADR-011 §2.1 5/5 evidence) | ⏳ Layer D 시점 |
| `provider_key_adapter_bypass_risk_detected` (IR-1) | Stage 4 combined check 시 | T2 + T3 | ⏳ Backlog #5 별도 합의 |
| `direct_sdk_with_secret_leakage_detected` (IR-2) | Stage 4 combined check 시 | T2 + T3 | ⏳ Backlog #5 별도 합의 |
| `secret_handling_environment_mismatch_detected` (IR-3) | Stage 5 (G3-7) 완료 시 | T2 + T3 | ⏳ Backlog #5 별도 합의 |

본 7 enum = **후보 한정** (정식 등록 = Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 영역).

### 5.4 본 §5 의 *범위 한계*

본 §5 = **Layer C 진입 시점 evidence *기준 정리* 한정**. 다음은 본 §5 영역 외:
- ❌ 실 evidence artifact 생성 (Markdown report / JSONL ledger / Docker isolation log / GitHub Actions run) — Layer C 시점 별도 작업
- ❌ enum 정식 등록 — Backlog #5 별도 합의
- ❌ Layer C 발효 — 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence + 사용자 명시
- ❌ Rollback trigger 발화 시연 — §6 답습 (실 시연 = Layer C 시점)

---

## 6. Rollback Trigger (18 trigger 본문 확정 답습 + 발화 시연 적격 영역)

### 6.1 GP-3 8 Rollback Trigger 답습 (mvp1.md §3.5 + Layer B §1.7 답습)

| Trigger | 발화 조건 | 발화 시 행동 | 발화 시연 (Layer C 시점) |
|--------|---------|-------------|--------------------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | 풀 3+1 합의 + threshold 재결정 | fixture: 정상 코드 1000 line 입력 → FP=0건 |
| R-MVP1-G3-2 | S-2 gitleaks 라이선스 변경 또는 maintenance 중단 | 풀 3+1 합의 + 도구 재선택 | (현 MVP-1 = S-1 단독, S-2 미진입 — trigger 미발화 사유) |
| R-MVP1-G3-3 | ST-3 Docker secret 도입 실패 | 풀 3+1 합의 + Backlog #1 (ST-2 inotify) 진입 검토 | fixture: docker secret block 누락 시 컨테이너 시작 실패 |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | threshold 재결정 합의 (단축 적격) | actual run latency 측정 + < 2분 cover |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | T3 영역 → 풀 3+1 합의 + branch protection rule 변경 검토 (Backlog #3) | fixture: bypass attempt log + AR-1 fail-closed 검증 |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | 풀 3+1 합의 + 외부 LLM 1+ | (Tier-1 답습 한정 — Backlog #3 별도 합의 시 발화) |
| R-MVP1-G3-7 | Tier-2 확장 필요 (1.5차 보강 trigger) | Backlog #1 1.5차 보강 합의 (S-3 detect-secrets 부분 통합) | (1.5차 보강 시점 발화 — 본 MVP-1 1차 영역 외) |
| R-MVP1-G3-8 | Operational Readiness parity 필요 trigger | Backlog #7 Operational Readiness parity check 합의 | (Operational Readiness 단계 발화) |

### 6.2 GP-5 10 Rollback Trigger 답습 (mvp1.md §4.6 + Layer B §1.7 답습)

| Trigger | 발화 조건 | 발화 시 행동 | 발화 시연 (Layer C 시점) |
|--------|---------|-------------|--------------------|
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | 풀 3+1 합의 + threshold 재결정 | fixture: 정상 facade 코드 → FP=0건 |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | 풀 3+1 합의 + T-2 보강 + Backlog #2 1.5차 진입 | fixture: 의도된 fail fixture 0건 미검출 |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 결과 불일치) | 책무 분담 재합의 (Group A 2차 §8 TR-4 답습) | fixture: 통합 결과 reconcile 검증 |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 (TR-1~TR-5 갈등) | 풀 3+1 합의 + rule 재정의 | fixture: rule conflict detection |
| R-MVP1-G5-5 | PC-3 hook 우회 시도 | T3 영역 → 풀 3+1 합의 (Backlog #3) | fixture: bypass attempt log |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 (실 src/ 도입 후) | threshold 재결정 합의 | fixture + actual run statistics |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 (`.importlinter` ignore_imports 검증 trigger) | Backlog #4 P1 v2 facade MVP 합의 진입 | (현 MVP-1 = facade placeholder 답습 — trigger 미발화 사유) |
| R-MVP1-G5-8 | branch protection 필요 trigger | Backlog #3 T3 영역 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | (T3 영역 진입 시점 발화) |
| R-MVP1-G5-9 | 의미적 lock-in 검출 (특정 모델 출력 가정) | MVP-3 진입 검토 (라운드트립 영역) | (현 MVP-1 = Layer 1 정적 한정 — trigger 미발화 사유) |
| R-MVP1-G5-10 | Layer 2 runtime 진입 필요 trigger | MVP-3/4 진입 검토 (G5-5 영역) | (현 MVP-1 = Layer 1 정적 한정 — trigger 미발화 사유) |

### 6.3 합산: 18 trigger 본문 확정 + 시연 적격 영역

- **본문 확정**: 18/18 (Layer B §1.7 답습 — 본 brief = 답습 변경 0건)
- **MVP-1 1차 시점 발화 시연 적격**: 8 trigger (G3-1, G3-3, G3-4, G3-5, G5-1, G5-2, G5-3, G5-4, G5-6) — fixture + actual run 시연 가능
- **MVP-1 1.5차 / Backlog 별도 진입 시 발화**: 10 trigger (나머지) — 별도 합의 영역 시점

### 6.4 본 §6 의 *범위 한계*

본 §6 = **Rollback Trigger *본문 확정 답습* 한정**. 다음은 본 §6 영역 외:
- ❌ 실 rollback fixture 생성 — Layer C 시점 별도 작업
- ❌ 실 trigger 발화 시연 — Layer C 시점 별도 작업
- ❌ Trigger threshold 정량 *고정* (>5% / >2분 등 모두 *후보 한정* 유지)
- ❌ 신규 trigger 추가 — 별도 합의 영역

---

## 7. 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | 실 runtime code 구현 | 0건 |
| 2 | 실 CI workflow 구현 | 0건 |
| 3 | 실 hook 구현 | 0건 |
| 4 | Implementation Evidence PASS (Layer C) 발효 | 0건 |
| 5 | MVP-1 PASS (Layer D) 선언 | 0건 |
| 6 | Operational Readiness PASS (Layer E) 선언 | 0건 |
| 7 | Hermes PMO 격상 (Layer F) | 0건 |
| 8 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 9 | 9 sub-수단 *재결정* (Layer B §5.5 답습 한정) | 0건 |
| 10 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 11 | threshold *고정* (FP / FN / latency 등 = 후보 한정) | 0건 |
| 12 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 13 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 14 | git commit / push | 0건 |
| 15 | 외부 LLM 자동 호출 | 0건 |
| 16 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 17 | MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 18 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 19 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |

### 7.2 본 brief 발효 *후* 실 구현 단계 금지 사항 (구현 진입 시 의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | 본 9 sub-수단 외 수단 도입 (예: gitleaks / detect-secrets / trufflehog / depcruise / grimp / ruff 등) | Backlog #1 + #2 1.5차 보강 영역 분리 |
| 2 | `src/adapters/llm/facade.py` real 본문 작성 | Backlog #4 P1 v2 facade MVP 합의 영역 분리 |
| 3 | branch protection rule 변경 (AR-2 / AR-3) | Backlog #3 T3 영역 별도 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| 4 | Hermes upstream Dockerfile 변경 (ST-1 / ST-2 / ST-5) | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의) |
| 5 | Vault HSM 통합 (ST-4) | Backlog #7 Operational Readiness 영역 분리 |
| 6 | Tier-2 / Tier-3 catalog 확장 (R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 변경) | Backlog #3 별도 합의 영역 |
| 7 | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 8 | event enum 정식 등록 (`event:` field) | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 9 | `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 (G3-7 (iii) 영역 답습 분리) |
| 10 | local pre-commit framework (PC-1 / PC-4) | Backlog #1 + #2 1.5차 보강 영역 분리 |
| 11 | Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 12 | 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 13 | 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 14 | 실 secret 본문 commit | 영구 금지 (R-4.1 + Group D §1.2 #1 답습) |
| 15 | F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 16 | Layer C (Implementation Evidence PASS) 자동 발효 (사용자 명시 결정 미충족 시) | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 실 구현 단계에서 위 16 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의** | Layer B §0.2 단축 채택 사유 답습 + 본 brief = Layer B 발효 결과 *행사 준비* 한정 + 9 sub-수단 본문 채택 §5.5 답습 |
| Layer C (Implementation Evidence PASS) 발효 합의 | **별도 합의 — 단축 또는 풀 3+1 + 외부 LLM 1+** | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 (Layer C 발효 trigger 발화 시 풀 3+1 권고) |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

본 brief 가 풀 3+1 합의로 *승격* 되어야 할 trigger 후보:

| # | 트리거 | 발화 시 합의 형태 |
|---|----|--------------|
| 1 | 본 brief 가 9 sub-수단 *외* 수단 도입을 권고하는 경우 (예: gitleaks 도입 / ST-1 entrypoint stat 진입 등) | 풀 3+1 합의 + 외부 LLM 1+ |
| 2 | 본 brief 가 ADR-011 §2.4 T3 영역 (branch protection rule 변경 / Vault HSM / Tier-2/3 catalog 확장) 에 진입하는 경우 | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| 3 | 본 brief 가 9 sub-수단 *재결정* 을 권고하는 경우 (Layer B §5.5 본문 채택 변경 trigger) | 풀 3+1 합의 + Layer B 재합의 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | 풀 3+1 합의 + 외부 LLM 1+ + [[feedback_provider_liquidity]] 답습 |
| 5 | 본 brief 가 5 영구 핵심 제약 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리) 中 1+ 의 약화를 포함하는 경우 | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |

**본 brief 검토 결과 = 5/5 트리거 0건 발화** (본 brief = 9 sub-수단 답습 한정 + Layer B 발효 결과 행사 준비 한정 + T3 영역 진입 0건 + Provider Liquidity 보존 + 5 영구 핵심 제약 보존 답습).

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** 확정 (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-step.md`) |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 (예: Backlog #4 P1 v2 facade MVP / Backlog #1 GP-3 1.5차 등) |
| (E) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (F) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A)로 진행해주세요. 본 brief를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B)로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C)로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D)로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (E): "옵션 (E)로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (F): "옵션 (F)로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (6/6 — 9 sub-수단 분할 / 구현 순서 / 파일 범위 / evidence 기준 / rollback trigger / 금지 사항) |
| 사용자 명시 금지 답습 | ✅ (4/4 — runtime code 0건 / CI workflow 0건 / hook 0건 / Implementation Evidence PASS 0건) |
| Layer B §5.5 본문 채택 답습 | ✅ (9 sub-수단 답습 변경 0건) |
| ADR-011 §2.1 (a)~(e) 5조건 답습 | ✅ (§5.1 답습) |
| Layer B §1.7 18 Rollback Trigger 답습 | ✅ (§6 답습 변경 0건) |
| Layer B §1.8 7 evidence 형태 답습 | ✅ (§5.2 답습 변경 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Provider Liquidity 5-way / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 모두 답습) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/5 발화 | ✅ (§8.2 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #6 Layer B Implementation Entry 합의 (`f40423f` APPROVE) + 9 sub-수단 본문 채택 (`55c5b4b`) 발효 후속**, *실 runtime code / CI workflow / hook 구현 진입* 직전의 *준비안 (DRAFT)* 이다. 9 sub-수단을 5 Stage (Stage 1 GP-3 S-1 코드 본문 / Stage 2 GP-3 ST-3 저장 / Stage 3 GP-5 T-6 Layer 1 정적 / Stage 4 공유 PC-3 + AR-1 통합 / Stage 5 G3-7 4 항목) × 22 sub-step 으로 분할하고, 구현 순서 권고 (순서 A — Stage 1 + Stage 3 병렬), 파일 범위 후보 (신규 6 + 기존 확장 8 + 변경 0건 영역 8), Layer C 진입 시점 evidence 기준 7 형태 + JSONL ledger 7 enum 후보 + ADR-011 §2.1 (a)~(e) 5조건, 18 Rollback Trigger 본문 확정 답습 + 시연 적격 영역, 본 brief 자체 금지 19 + 구현 단계 금지 16, 합의 형태 권고 (Reviewer-only 단축 — 5 풀 3+1 트리거 0/5 발화) 를 정리한다. **본 brief 는 실 구현을 *시작* 시키지 않으며, Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~F, §9 답습).

---

**작성일**: 2026-05-12 후속
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~F, §9 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ 실 runtime code 구현
- ❌ 실 CI workflow 구현
- ❌ 실 hook 구현
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 9 sub-수단 재결정 (Layer B §5.5 답습 변경 0건)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
