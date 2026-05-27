# MVP-1 1.5차 보강 진입 합의 entry brief — 4 sub-수단 (S-3 + ST-2 + PC-1 + AR-3)

> **scope**: MVP-1 GP-3 + GP-5 1.5차 보강 4 sub-수단 (S-3 detect-secrets 부분 통합 + ST-2 inotify sidecar + PC-1 pre-commit framework 의무화 + AR-3 통합 PR auto-reject) **진입 합의 entry brief**. 본 brief 발효 = 4 sub-수단 *채택 결정 발효 자격* + 실 구현 단계 진입 권한 발효 자격. **본 brief 자체에서 실 코드 / CI / hook / branch protection rule / `.pre-commit-config.yaml` 본문 변경 0건 의무**.
>
> **답습**:
> - 진입 합의 carry-over 명시 = `docs/sessions/SESSION_2026-05-27.md` 23번째 entry carry-over (b) (commit `c2bcb19` 답습, scope = 4 sub-수단 모두 + 풀 3+1 + 외부 LLM 1+)
> - 선행 1.5차 brief = [[backlog1-gp3-1.5-deepening-brief]] + [[backlog2-gp5-1.5-remaining-items-brief]] (영역 분류 한정, 수단 결정 0건)
> - 선행 1.5차 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (APPROVE AS BRIEF, ST-2 단독 우선 권고) + `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` (APPROVE Deferred 유지 + AR-3 Backlog #3 이관)
> - roadmap-mvp1 권위 = [[implementation-runtime-roadmap-mvp1]] APPROVED (`c2bcb19` line 826/827 답습) §3.2 / §3.3 / §3.6.3 / §4.3 / §4.4 / §4.7.3
> - 최상위 모법 = [[ADR-011-means-vs-ends-redaction]] §2.1 (a)~(e) 5조건 + §2.4 T1/T2/T3 분리
> - 메타 = [[ceremony-inflation]] 차단 + [[meta-cycle-warning]] (정정의 정정 자격 0 self-check 통과)
>
> **DONE 기준** (본 brief 의 *최종 산출 자격*):
> 1. 4 sub-수단 각각의 *진입 자격* 분석 + ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5/5 충족 매트릭스 (ADR-011 §3 후속 권위 답습 — R-1 BLOCKING 흡수)
> 2. 선행 1.5차 brief 합의 권위 vs 본 cycle 결정 *선차 변경 매트릭스* (3 sub-수단 권위 상승 명문)
> 3. 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ 답습 정당화 (4 sub-수단별)
> 4. Rollback Trigger 본문 / Evidence 형식 / JSONL Ledger event enum 후보 (발효 시점 의무)
> 5. 외부 LLM 응답 요구 *입력 자료* 정의 (사용자 준비 영역)
> 6. 7 풀 3+1 승격 트리거 발화 검증 (본 cycle 자체 ↔ 4 sub-수단별)
> 7. 다음 단계 결정 옵션 (사용자 결정 영역)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (carry-over from SESSION_2026-05-27 23번째 entry, commit `c2bcb19`)

> **(b) MVP-1 1.5차 보강 합의 — 사용자 명시 scope 확정 (2026-05-27)**:
> - scope = **4 sub-수단 모두 (S-3 + ST-2 + PC-1 + AR-3)** (사용자 명시 결정 답습)
>   - S-3 detect-secrets 부분 통합 (GP-3 Tier-2/3 catalog 확장)
>   - ST-2 inotify sidecar (GP-3 저장 경로 실시간 감지)
>   - PC-1 pre-commit framework 의무화 (GP-3/GP-5 T3 dev 환경 강제)
>   - AR-3 통합 PR auto-reject (GP-3/GP-5 branch protection rule 변경)
> - 합의 형태: **풀 3+1 + 외부 LLM 1+** (roadmap-mvp1 §3.6.3 line 289 + §4.7.3 line 480 답습)
> - 사용자 준비 영역: **외부 LLM 응답 1+** (Claude 가 외부 LLM 호출 못 함, 사용자 직접 호출 의무)
> - 다음 세션 진입 명령 (사용자 영역): "(b) 1.5차 보강 풀 3+1 진입 — S-3 + ST-2 + PC-1 + AR-3" + 외부 LLM 자료 첨부

### 0.2 본 brief 가 *하는* 것

1. 4 sub-수단 (S-3 + ST-2 + PC-1 + AR-3) *진입 자격* 분석 — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 (§3, ADR-011 §3 후속 권위 답습)
2. 선행 1.5차 brief 합의 권위 (2026-05-13 backlog1 / backlog2) 와의 *선차 변경 매트릭스* (§1.3)
3. 4 sub-수단 각각의 *수단 후보 비교* + threshold 후보 + Rollback Trigger 본문 후보 (§2 + §5)
4. 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ *정당화* (carry-over 답습 + roadmap-mvp1 §3.6.3/§4.7.3 답습) (§4.1)
5. 4 sub-수단 *발효 시점* 합의 형태 권고 (선행 권위 답습) (§4.2)
6. 7 풀 3+1 승격 트리거 *발화 검증* (본 cycle 자체 ↔ 4 sub-수단별) (§4.3)
7. 외부 LLM 응답 요구 *입력 자료* 정의 + *응답 자격 검증 기준* (사용자 준비 영역) (§7)
8. 본 cycle 합의 발효 후 *실 구현 sub-cycle 진입 권한* 발효 자격 명문 (§8)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 (S-3 plugin / ST-2 sidecar / PC-1 framework / AR-3 branch protection 본문 모두 0건) |
| 2 | `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 | 0건 |
| 3 | `.importlinter` config 변경 | 0건 |
| 4 | `.github/workflows/*.yml` 본문 변경 | 0건 |
| 5 | `branch protection rule` 변경 / GitHub API 호출 | 0건 |
| 6 | `pre-commit install` 실행 | 0건 |
| 7 | detect-secrets / inotify-tools 설치 | 0건 |
| 8 | Tier-2 / Tier-3 catalog 본문 확장 | 0건 (S-3 plugin 명시 활성화 후보 영역 명시 한정, 본문 확장 0건) |
| 9 | threshold *고정* (FP/FN/latency 등) | 0건 (후보 한정 유지) |
| 10 | **MVP-1 PASS *재선언*** | 0건 (Layer D `210c98f` 판정 그대로 유지) |
| 11 | **Implementation Evidence PASS 발효** | 0건 ((c) 진입점 별도 단계 답습) |
| 12 | **Operational Readiness PASS (Layer E)** | 0건 |
| 13 | **Hermes PMO 격상 (Layer F)** | 0건 |
| 14 | 외부 LLM 호출 (Claude 영역) | 0건 (사용자 명시 외부 LLM 응답 1+ 별도 첨부 영역) |
| 15 | ADR 본문 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012) | 0건 (cross-reference 한정도 0건 — 본 brief 발효 후 별도 commit 영역) |
| 16 | 헌법 본문 갱신 (`PROJECT_CONSTITUTION.md`) | 0건 |
| 17 | roadmap-mvp1 §1~§8 본문 변경 | 0건 (cross-reference 답습 한정) |
| 18 | `src/adapters/llm/facade.py` placeholder → real 본문 (G5-4) | 0건 (TR-1 자동 풀 3+1 별도 trajectory) |
| 19 | Backlog #3 / #4 / #7 *자동* 진입 | 0건 (AR-3 의 Backlog #3 이관 → 본 cycle 동시 진입 결정 = 사용자 명시 권위 변경 — Backlog #3 *전체* 진입 ≠ 본 cycle) |
| 20 | 본 brief *자체* 영구화 / 권위 chain 등재 | 0건 (본 brief = 본 cycle 합의 input 한정) |

### 0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 + 사용자 명시 결정** 3 조건 모두 충족 시점
- ✅ 본 brief 발효 결과 = 4 sub-수단 *채택 결정 발효* + 실 구현 sub-cycle 진입 권한 발효 + Rollback Trigger 본문 채택 + Evidence 형식 본문 채택
- ❌ 본 brief 자체에서 4 sub-수단 *결정* 0건 (본 brief = entry input, 결정 자격은 풀 3+1 합의 결과에 의존)
- ❌ 본 brief 자체에서 threshold *고정* 0건 (후보 한정)
- ❌ 본 brief 자체에서 실 구현 0건 (별도 sub-cycle)
- ⚠️ 본 brief 합의 후 *자동 실 구현 진입 금지* — 사용자 명시 결정 의무 (단계별 합의 cycle 패턴 답습)

---

## 1. 진입 컨텍스트 답습

### 1.1 선행 1.5차 brief 합의 권위 답습 (2026-05-13 backlog1 + backlog2)

| 합의 | 일자 | 판정 | 본 cycle 답습 영역 |
|------|------|------|------------------|
| `3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` | 2026-05-13 | ✅ **APPROVE AS BRIEF** (Reviewer-only 단축) | Backlog #1 진입 *직전* 정비 한정. ST-1/ST-2/PC-4 *채택 결정 0건*. ST-2 단독 우선 권고 (T3 자동 진입 0건 조건 충족 유일). PC-4 = T2 + T3 sub 영역 분리. |
| `3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` | 2026-05-13 | ✅ **APPROVE Keep Deferred** (Reviewer-only 단축) | T-1/T-3/T-4/T-5/AR-3 5 항목 *Deferred 유지 권위화 한정*. **AR-3 = Deferred 유지 + Backlog #3 이관 명시**. PC-4 T2 sub = 별도 합의 (`78483c5`) Partially Satisfied 완료. |
| `3plus1-consensus-2026-05-13-pc4-t2-c5c-c6-satisfaction.md` (참조) | 2026-05-13 | ✅ APPROVE (`78483c5`) | PC-4 T2 sub (`.pre-commit-config.yaml` opt-in framework) §C-5c + §C-6 Partially Satisfied 갱신. **PC-1 T2 정책 영역은 이미 부분 발효**, T3 dev 환경 강제 = Backlog #3 영역. |

### 1.2 4 sub-수단 답습 (roadmap-mvp1 §3.2 + §3.3 + §4.3 + §4.4)

| sub-수단 | GP | 영역 정의 | roadmap-mvp1 본문 line |
|---------|----|---------|----------------------|
| **S-3** | GP-3 | **detect-secrets** plugin-based (~20+ plugins, 활성화 선택). 코드 본문 secret 검출 (G3-2). Tier-2/3 catalog 확장 영역. | §3.2.1 line 180 + §3.2.2 line 189 ("plugin 명시 활성화 + baseline file 금지 2 조건 강제 시에만 채택 적격") |
| **ST-2** | GP-3 | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지). 런타임 지속 검증. 저장 경로 secret 검출 (G3-1). | §3.3.1 line 204 + §3.3.2 line 214 ("MVP-1 1.5차 (보강) = ST-3 + **ST-2 inotify sidecar**, Hermes upstream 변경 회피 유지") |
| **PC-1** | GP-3 + GP-5 | **pre-commit framework** (`.pre-commit-config.yaml` + `pre-commit install`). hook 정의 통일 + dev 환경 자동 설치. | §4.3.1 line 370 ("T2 정책 영역, ADR-011 §2.4 답습") + §4.3.2 line 380 ("MVP-1 1.5차 보강 = PC-4 = PC-1 + PC-3 병행, dev 환경 강제 추가 시 Defense in depth") |
| **AR-3** | GP-3 + GP-5 | **AR-1 (CI step fail-closed) + AR-2 (branch protection rule 강제) 통합** PR auto-reject runtime. | §4.4.1 line 393 + §4.4.2 line 400 ("MVP-1 1.5차 보강 = AR-3 (AR-1 + AR-2 통합) — T3 영역 진입 + branch protection rule 변경 + 사용자 명시 결정") |

### 1.3 ⭐ 선차 변경 매트릭스 (선행 권위 vs 본 cycle 결정)

> **본 §1.3 = 본 brief 의 *핵심 framing*** — 선행 1.5차 brief 합의 (2026-05-13) 의 권위와 본 cycle (2026-05-27) carry-over 사용자 명시 결정 사이의 *변경 차이* 를 명시. 변경 자격 정당성 = (a) 사용자 명시 권위 우선 + (b) 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 = ADR-011 §2.1 (e) + §2.4 T3 영역 답습 충실성.

| sub-수단 | 선행 권위 (2026-05-13) | roadmap-mvp1 line | 본 cycle 결정 | 권위 정당성 |
|---------|---------------------|------------------|--------------|------------|
| **S-3** | backlog1 §1.3 미언급 (Backlog #1 = ST-1/ST-2/PC-4 한정, S-3 = Group D PoC §2.1 (D) 답습 영역) | §3.6.3 **line 289** — "MVP-1 1.5차 (S-3 detect-secrets 부분 통합) \| **풀 3+1 합의 + 외부 LLM 1+** \| Tier-2/3 catalog 확장 영역 + 사용자 명시 풀 3+1 trigger #4 발화 (Group D §2.1 (D) 답습)" | **풀 3+1 + 외부 LLM 1+** | **✅ 일치 답습** (roadmap §3.6.3 line 289 verbatim 답습) |
| **ST-2** | backlog1 §1.5 + §2.2.4 — "ST-2 단독 우선 권고 (T3 자동 진입 0건 유일)" + "T2 영역, **단축 합의 + 사용자 명시 결정** *또는* **보수적 풀 3+1 합의**" | §3.6.3 **line 290** — "ST-1 / **ST-2** / ST-5 진입 (Hermes upstream 변경) \| 풀 3+1 합의 + Hermes upstream PR 검토 \| Hermes upstream 영역" | **풀 3+1 + 외부 LLM 1+** | **⚠️ 사용자 명시 상승 + framing 미세 충돌 흡수**. backlog1 권고 = T2 + 보수적 풀 3+1 옵션 → 본 cycle = 풀 3+1 + 외부 LLM 1+. roadmap §3.6.3 line 290 framing 미세 충돌 (ST-2 = "Hermes upstream 변경 ❌ 불필요", backlog1 §2.2.2 verbatim) — 단, 사용자 명시 carry-over = "GP-3 저장 경로 실시간 감지" 영역 = sidecar 운영 = 풀 3+1 + 외부 LLM 1+ 권한 영역. 본 cycle 합의 발효 시 backlog1 §2.2.4 권고 *상위 변경* 자격 발효. |
| **PC-1** | roadmap §4.7.3 **line 479** — "MVP-1 1.5차 (PC-1 pre-commit framework 도입) \| **단축 합의 + 사용자 명시** \| T2 정책 영역 (ADR-011 §2.4 답습)" + PC-4 T2 sub `78483c5` Partially Satisfied (`.pre-commit-config.yaml` opt-in framework 발효) | §4.7.3 line 479 | **풀 3+1 + 외부 LLM 1+** | **⚠️ 권위 상승 — 사용자 명시 carry-over 답습**. carry-over verbatim = "PC-1 pre-commit framework **의무화** (GP-3/GP-5 T3 dev 환경 강제)". opt-in (T2, line 479) → 의무화 (T3 dev 환경 강제) 영역 상승 = ADR-011 §2.4 T3 영역 진입 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 (roadmap §4.7.3 line 480 AR-3 = T3 영역 답습 패턴). |
| **AR-3** | backlog2 §1.6 — "**AR-3 = Deferred 유지 + Backlog #3 이관 명시**" (T3 영역 진입 BLOCKING + Backlog #3 보존 의무) | §4.7.3 **line 480** — "AR-2 / AR-3 진입 (branch protection rule 변경) \| **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** \| T3 영역" | **풀 3+1 + 외부 LLM 1+ + MVP-1 1.5차 동시 진입** | **⚠️ 선차 변경 — 사용자 명시 권위 변경**. backlog2 합의 = Deferred 유지 + Backlog #3 이관 → 본 cycle = MVP-1 1.5차 동시 진입. 합의 *형태* 자체는 roadmap §4.7.3 line 480 와 일치 답습. *시점* 변경 = backlog2 §1.6 권위의 사용자 명시 변경 자격 (ADR-011 §2.1 (e) 합의 APPROVE + §2.4 T3 영역 답습 + 사용자 명시 결정 = 정당). |

→ **요약**: 본 cycle 합의 형태 = 4 sub-수단 모두 **풀 3+1 + 외부 LLM 1+ + 사용자 명시** 일관. S-3 = 일치 답습 / ST-2 = 권위 상승 / PC-1 = 권위 상승 / AR-3 = 시점 선차 변경 (Backlog #3 이관 → MVP-1 1.5차 동시 진입). 모든 변경 자격 = 사용자 명시 + ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5/5 충족 + §2.4 T3 영역 답습 + 본 cycle 합의 APPROVE 시 발효.

---

## 2. 4 sub-수단 진입 자격 분석

### 2.1 S-3 — detect-secrets 부분 통합 (GP-3 Tier-2/3 catalog 확장)

#### 2.1.1 영역 정의

| 항목 | 내용 |
|------|------|
| **목적** | 코드 본문 secret 검출 (G3-2) Tier-2/3 catalog 확장 — plugin-based ~20+ plugins (Tier-1 42 catalog 답습 외 확장 영역) |
| **검증 시점** | CI step (매 PR + nightly) + opt-in pre-commit hook |
| **메커니즘** | `detect-secrets scan --baseline <baseline>.json --exclude-files <regex>` — plugin 활성화 선택 (Slack / GCP / Azure / Generic / Base64 / Hex 등) |
| **권위 출처** | roadmap-mvp1 §3.2 6 수단 후보 매트릭스 / Group D PoC §2.1 (D) sub-수단 #5 ("detect-secrets baseline silenceable risk 명시") |

#### 2.1.2 채택 조건 (roadmap §3.2.2 line 189 답습)

✅ **plugin 명시 활성화 한정** — Tier-1 답습 plugin 활성화 (실 plugin identifier 예: `AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` / `HexHighEntropyString` / `PrivateKeyDetector` — 실 구현 sub-cycle 정확 mapping 영역, R-4 BLOCKING 흡수). Slack / GCP / Azure 등 추가 활성화 = **별도 합의** (Tier-2/3 catalog 확장 = 풀 3+1 + 외부 LLM 1+ 의무, R-MVP1-G3-1 답습)
✅ **baseline file 금지** — `--baseline` 옵션 0건 (silenceable 위험 차단, Group D §2.1 (D) 답습)
✅ **secret_scanner.py (S-1) 답습 유지** — S-3 = *추가* layer (S-1 미대체, Defense in depth)
✅ **`.github/workflows/secret-hygiene-egress-redaction.yml` step 통합** — 현 secret_scanner.py 답습 *후속* step

#### 2.1.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **S-3 부분 통합 채택 결정 발효 자격** — 본 cycle 합의 APPROVE 시점 발효
✅ **plugin 활성화 catalog 본문 채택** — detect-secrets CLI 실 plugin identifier (예: `AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` / `HexHighEntropyString` / `PrivateKeyDetector` — Tier-1 답습 한정, 실 구현 sub-cycle 정확화 영역, R-4 BLOCKING 흡수) + **`--baseline` 미사용 CI assertion 의무** (CI step 본문 grep `--baseline` 검출 시 fail, silenceable 우회 차단)
✅ **실 구현 sub-cycle 진입 권한 발효** — 별도 commit (`pip install detect-secrets` + workflow step 추가 + S-1 답습 step 후속 + plugin 활성화 hardcoded list)

#### 2.1.4 미발효 영역 (deferred)

❌ Tier-2 / Tier-3 vendor catalog *본문 확장* (Slack / GCP / Azure 등) = 별도 풀 3+1 + 외부 LLM 1+
❌ S-3 baseline file 사용 = 영구 금지 (R-MVP1-G3-1 답습)
❌ S-3 단독 운영 (S-1 대체) = 영구 금지 (Defense in depth 답습)

### 2.2 ST-2 — inotify sidecar (GP-3 저장 경로 실시간 감지)

#### 2.2.1 영역 정의

| 항목 | 내용 |
|------|------|
| **목적** | 저장 경로 secret 검출 (G3-1) 런타임 지속 보강 — mtime / perm 변경 event 발생 시 컨테이너 정지 |
| **검증 시점** | 런타임 지속 (inotify event 기반) |
| **메커니즘** | sidecar 컨테이너가 secret 파일 경로 (`/secrets/*`) 를 inotify 감시 → mtime / perm / write event 발생 시 메인 컨테이너에 정지 signal 송출 (docker-compose dependency `restart: on-failure` 또는 healthcheck fail) |
| **권위 출처** | ADR-008 6 차단조건 #1 (SQLCipher) + #6 (Docker 격리 + egress 화이트리스트) cross-reference (line 17~23 verbatim 답습) + GP-3 §5.3 ("inotify 런타임 감시 — Hermes runtime") + roadmap-mvp1 §3.3.1 line 204 + backlog1 §2.2 — ⚠️ **R-S1 정정 답습**: ADR-008 본문 §A.2 = "Hermes JSONL Export 검증" (line 136), R1-2 / §2.6 식별자 ADR-008 본문 부재 (raw line-level verify). 본 인용 = 선행 backlog1 합의 + governance-preconditions cross-reference 답습이며 정확 R1-2 source 위치 확인 + 일관 정정 = **본 cycle scope 외 cross-reference 별도 commit 영역 (N-9 권고 답습)** |

#### 2.2.2 채택 조건 (backlog1 §2.2.2 답습)

✅ **Hermes upstream Dockerfile 변경 ❌ 불필요** — sidecar 분리 가능 (backlog1 §2.2.2 답습)
✅ **ST-3 (docker secret + chmod 600) 답습 권위 위에서 진입** (roadmap §3.3.2 답습)
✅ **inotify event 응답 시간 후보 = <1초** (threshold *고정 0건*, 후보 한정)
✅ **`tools/docker_secret_inotify_sidecar_check.sh` 실 구현 답습** (audit brief §2.1 답습) — 본 cycle 발효 시 docker-compose sidecar 본문 추가 (별도 sub-cycle)

#### 2.2.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **ST-2 inotify sidecar 채택 결정 발효 자격**
✅ **docker-compose sidecar 본문 채택 권한** (별도 sub-cycle)
✅ **inotify-tools 의존성 추가 권한** (Dockerfile 변경, sidecar image 한정 — Hermes upstream Dockerfile 변경 0건 유지)
✅ **`tools/docker_secret_inotify_sidecar_check.sh` nightly workflow 통합 권한**
✅ **3 단계 evidence 본문 채택 의무** (R-5 BLOCKING 흡수): (1) inotify event 인지 + (2) sidecar → 메인 컨테이너 정지 signal 전달 + (3) **메인 workload fail-closed 확인** (메인 workload exit status check 또는 healthcheck fail) — event 인지만으로 보안 효과 0, Defense in depth 답습

#### 2.2.4 미발효 영역 (deferred)

❌ inotify event 응답 시간 *threshold 고정* (<1초 / <500ms 등) = 별도 합의 (실 측정 후)
❌ sidecar process 운영 부담 *Operational Readiness PASS* (Layer E) = MVP-1 영역 외 (Backlog #7)
❌ ST-1 (entrypoint stat) / ST-5 (defense in depth) = Hermes upstream 변경 영역 (별도 풀 3+1 + Hermes upstream PR)

### 2.3 PC-1 — pre-commit framework 의무화 (GP-3 / GP-5 T3 dev 환경 강제)

#### 2.3.1 영역 정의

| 항목 | 내용 |
|------|------|
| **목적** | hook 정의 통일 + **dev 환경 자동 설치 의무화** (T3 영역) — opt-in (현 PC-4 T2 sub) → 의무화 (T3 dev 환경 강제) |
| **검증 시점** | dev 환경 `pre-commit install` 시점 + 매 `git commit` 시점 |
| **메커니즘** | `.pre-commit-config.yaml` (T2 부분 발효 `78483c5`) + **`pre-commit install` 의무화** (T3 dev 환경 강제) + branch protection rule 통합 (PR 의 모든 commit 이 hook 통과 검증) |
| **권위 출처** | roadmap-mvp1 §4.3.1 line 370 (T2 정책 영역) + §4.7.3 line 479 + PC-4 T2 sub `78483c5` Partially Satisfied 답습 + ADR-011 §2.4 T3 영역 답습 |

#### 2.3.2 채택 조건

✅ **PC-4 T2 sub (`.pre-commit-config.yaml` opt-in) 이미 발효** (`78483c5` 답습) — 본 cycle = T3 sub 진입
✅ **dev 환경 강제 메커니즘** — README 명문 + CONTRIBUTING.md 명문 + onboarding 자동 (`make setup` / `pre-commit install` 의무)
✅ **branch protection rule 통합** — AR-3 와 *동시 진입* 효과 (PC-1 T3 sub + AR-3 = "PR auto-reject 의 pre-commit hook 통과 검증" = Defense in depth)
✅ **`.pre-commit-config.yaml` 본문 답습 유지** — 신규 hook 추가 0건 (본 cycle), 현 hook 운영 의무화 한정

#### 2.3.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **PC-1-T3 mandatory enforcement 채택 결정 발효 자격** (T3 dev 환경 강제, N-2 권고 흡수 — 명칭 일관)
✅ **README + CONTRIBUTING.md 본문 채택 권한** (의무화 명문, 별도 sub-cycle)
✅ **onboarding 스크립트 (`make setup` / `bin/setup.sh`) 본문 채택 권한** (별도 sub-cycle)
✅ **branch protection rule 통합 정책** (AR-3 와 동시 발효)
✅ **PC-1 + PC-3 + AR-3 결합 의무화 효과 명문** (N-1 권고 흡수 — PC-1 단독 보안 효과 ≈ 0, `pre-commit install` 로컬 우회 가능. 의무화 *실제 강제력* = PC-1 (dev 환경 hook) + PC-3 (CI step) + AR-3 (branch protection rule) 결합 시점 발효 — codex §7.2 + Agent A/B/C 권고 답습)

#### 2.3.4 미발효 영역 (deferred)

❌ `.pre-commit-config.yaml` *본문 변경* (신규 hook 추가) = 별도 합의 (현 hook 본문 답습 유지)
❌ commit signing 의무화 = 별도 합의 (Backlog #3 영역, T3 강제 강화)
❌ Tier-2/3 vendor hook 추가 = 별도 합의

### 2.4 AR-3 — 통합 PR auto-reject (GP-3 / GP-5 branch protection rule 변경)

#### 2.4.1 영역 정의

| 항목 | 내용 |
|------|------|
| **목적** | AR-1 (CI step fail-closed) + AR-2 (GitHub branch protection rule 강제) **통합** = PR auto-reject runtime (T3 영역) |
| **검증 시점** | 매 PR push + 매 PR merge 시점 |
| **메커니즘** | (1) AR-1 답습 — `.github/workflows/*.yml` job `fail-closed` (이미 부분 발효 — 11 workflow 답습) + (2) AR-2 신규 — GitHub branch protection rule "**Require status checks to pass before merging**" + "**Restrict pushes that create matching branches**" + "**Do not allow bypassing the above settings**" |
| **권위 출처** | roadmap-mvp1 §4.4.1 line 393 + §4.4.2 line 400 + §4.7.3 line 480 + backlog2 §1.6 + ADR-011 §2.4 T3 영역 + roadmap §4.6 R-MVP1-G5-2 |

#### 2.4.2 채택 조건

✅ **AR-1 답습 유지** — 11 workflow 모두 `fail-closed` (현 답습 유지, 본 cycle 신규 변경 0건 — AR-2 통합 한정)
✅ **branch protection rule = `main` + `develop` 보호 + status check 의무** — required check 단위 = **workflow file명 ≠ 실제 check name** (GitHub branch protection rule = job name 또는 workflow_run.conclusion 단위 mapping, R-3 BLOCKING 흡수). 11 workflow 의 *실제 check name list* catalog 본문 채택 = 실 구현 sub-cycle 영역 (GitHub UI/API mapping verify 의무)
✅ **bypass 권한 0건** — admin / fork PR 모두 동일 강제 (`Restrict who can push to matching branches` = 0 user)
✅ **외부 LLM 응답 1+ 의무** (roadmap §4.7.3 line 480 verbatim) — branch protection rule 본문 결정 = T3 영역 = 외부 LLM cross-vendor blind risk 답습

#### 2.4.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **AR-3 (AR-1 + AR-2 통합) 채택 결정 발효 자격**
✅ **branch protection rule 본문 채택 권한** (별도 sub-cycle — GitHub API 호출 또는 web UI 변경)
✅ **`main` / `develop` 두 branch 모두 강제 적용 권한**
✅ **bypass 정책 본문 채택 권한** (admin bypass 0건 의무)

#### 2.4.4 미발효 영역 (deferred)

❌ `.github/workflows/*.yml` 본문 변경 (신규 status check 추가) = 별도 합의 (현 11 workflow 답습 유지)
❌ Backlog #3 *전체* 진입 = 본 cycle 영역 외 — **AR-3 = Backlog #3 의 *AR-3 sub-수단 단독 시점 변경* 한정**, Backlog #3 의 다른 항목 = ST-4 Vault HSM / commit signing 강제 / Tier-2/3 catalog 등 모두 별도 합의 영역 (N-3 권고 흡수, 명문 반복 강화)
❌ AR-2 branch protection rule = MVP-1 영역 외 *다른* rule = 별도 합의 (N-6 권고 흡수):
  - **force-push 차단** = 별도 합의 영역
  - **signed commit 강제** = 별도 합의 영역
  - **fork PR 처리 정책** = 별도 합의 영역
  - **linear history 강제** = 별도 합의 영역

---

## 3. ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) — 5조건 매트릭스 (4 sub-수단별)

> **본 §3 = 본 brief 의 *수단 결정 자격 검증***. ADR-011 §2.1 원문 = (a)~(d) 4조건 (verbatim, line 56~60 답습). (e) "합의 APPROVE" = ADR-011 §3 (R-4~R-7 모법) line 281+290 후속 운영조건 (5조건 패턴). brief v1 "(a)~(e) 5조건 매트릭스" 명칭 → R-1 BLOCKING 흡수 결과 "(a)~(d) + 합의 APPROVE 운영조건 (e) — 5조건 매트릭스 (ADR-011 §3 후속 권위 답습)" 정합 표기. 매트릭스 *내용* 자체는 정합 유지 (Agent B nuance + 합의 보고서 R-1 답습). 미충족 항목 = 본 cycle 합의 발효 후 *실 구현 sub-cycle* 의무 영역.

| # | 조건 | S-3 | ST-2 | PC-1 | AR-3 |
|---|------|-----|------|------|------|
| **(a)** | 동등 이상의 보안 결과 | ⚠️ **조건부** — plugin 명시 활성화 + baseline file 금지 2 조건 강제 시 충족. baseline file 사용 시 silenceable = FN 위험 (Group D §2.1 (C) 답습) → 영구 금지 명문 의무 | ✅ inotify mtime/perm event 감시 = entrypoint stat (ST-1) 대비 *런타임 지속* 보강. Defense in depth (ST-3 답습 위 추가 layer) | ✅ T2 sub (opt-in) → T3 sub (의무화) = dev 환경 자동 설치 = secret commit 사전 차단 강화. PC-3 (CI step) 답습 + Defense in depth | ✅ AR-1 (CI step fail-closed) + AR-2 (branch protection) 통합 = PR merge bypass 차단 강화. T3 영역 답습 |
| **(b)** | 격리 환경 PoC 실증 | ⏳ Group D PoC §2.1 (D) 답습 (S-3 미채택, 본 cycle 발효 후 별도 PoC 의무 — `pip install detect-secrets` + plugin 활성화 + Tier-1 catalog 적용 testfile evidence) | ⏳ `tools/docker_secret_inotify_sidecar_check.sh` (audit brief §2.1 답습, 실 구현 완료) + docker-compose sidecar 본문 추가 별도 sub-cycle (**(1) event 인지 + (2) sidecar → 메인 컨테이너 정지 signal 전달 + (3) 메인 workload fail-closed 확인 3 단계 evidence 의무**, R-5 BLOCKING 흡수) | ⏳ **T3 mandatory enforcement PoC 미충족** (R-2 BLOCKING 흡수) — PC-4 T2 sub `78483c5` Partially Satisfied = opt-in PoC (T2 정책 영역), T3 의무화 PoC 자격 0. 본 cycle 발효 후 onboarding 스크립트 + `pre-commit install` enforcement + bypass detection evidence 별도 sub-cycle | ⏳ AR-1 부분 발효 (11 workflow 답습) + AR-2 branch protection rule 시뮬레이션 별도 sub-cycle (GitHub API 호출 또는 web UI 변경 evidence + **check name mapping verify**, R-3 BLOCKING 흡수) |
| **(c)** | ADR / SDD 권위 명시 | ✅ roadmap-mvp1 §3.2 + ADR-008 6 차단조건 #1 + ADR-011 §2.1 + Group D PoC §2.1 (D) 답습 | ✅ ADR-008 6 차단조건 #1 + #6 cross-reference (R-S1 정정 답습, line 17~23) + GP-3 §5.3 + roadmap-mvp1 §3.3 + backlog1 §2.2 답습 | ✅ roadmap-mvp1 §4.3 + ADR-011 §2.4 T2/T3 분리 + roadmap §4.7.3 line 479 답습 | ✅ roadmap-mvp1 §4.4 + ADR-011 §2.4 T3 영역 + roadmap §4.7.3 line 480 + backlog2 §1.6 답습 |
| **(d)** | 자동 회귀 검증 경로 확보 | ⏳ `.github/workflows/secret-hygiene-egress-redaction.yml` step 통합 + nightly + `--baseline` 미사용 CI assertion (R-4 BLOCKING 흡수, 별도 sub-cycle) | ⏳ docker-compose sidecar nightly run + `tools/docker_secret_inotify_sidecar_check.sh` nightly workflow 통합 + **메인 workload exit status assertion** (R-5 BLOCKING 흡수, 별도 sub-cycle) | ⏳ **T3 mandatory enforcement audit 미충족** (R-2 BLOCKING 흡수) — pre-commit CI step 통합 (현 `.pre-commit-config.yaml` 답습) + `pre-commit install` enforcement audit log + bypass detection evidence 별도 sub-cycle | ⏳ branch protection rule status check actual run id evidence + **실제 check name mapping evidence** (R-3 BLOCKING 흡수, 별도 sub-cycle) |
| **(e)** | 합의 APPROVE | ⏳ 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시 합의 APPROVE 시 충족 | ⏳ 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시 합의 APPROVE 시 충족 | ⏳ 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시 합의 APPROVE 시 충족 | ⏳ 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시 합의 APPROVE 시 충족 |

→ **현 시점 충족 = (a)(c) 부분 + (b)(d)(e) 미충족** → 본 cycle 합의 발효 = (e) 충족 + (b)(d) 충족 의무 = **실 구현 sub-cycle 4개 발효 자격** (S-3 sub-cycle + ST-2 sub-cycle + PC-1 sub-cycle + AR-3 sub-cycle, 각각 별도 commit + evidence + 사용자 명시 결정).

→ **Implementation Evidence PASS 발효** (MVP-1 (c) 진입점) = 본 cycle 합의 APPROVE + 4 sub-cycle 모두 evidence (b)(d) 충족 + 사용자 명시 결정 시점 별도 합의 영역 (audit brief §5 (c) 진입점 답습).

---

## 4. 합의 형태 + 풀 3+1 승격 트리거 검증

### 4.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (carry-over 답습 정당화)

| 정당성 근거 | 답습 출처 |
|------------|----------|
| **carry-over 사용자 명시** | SESSION_2026-05-27 23번째 entry carry-over (b) verbatim — "합의 형태: **풀 3+1 + 외부 LLM 1+**" |
| **roadmap §3.6.3 line 289 (S-3 답습)** | "MVP-1 1.5차 (S-3 detect-secrets 부분 통합) \| **풀 3+1 합의 + 외부 LLM 1+**" |
| **roadmap §4.7.3 line 480 (AR-3 답습)** | "AR-2 / AR-3 진입 (branch protection rule 변경) \| **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** \| T3 영역" |
| **ADR-011 §2.4 T3 영역 답습** | T3 영역 (정책 변경 / branch protection / dev 환경 강제) = 풀 3+1 + 외부 LLM 1+ 의무 |
| **CLAUDE.md §3 적용 기준 답습** | 아키텍처 의사결정 / 보안 관련 변경 = 3+1 (필수) |
| **본 brief §1.3 선차 변경 매트릭스** | ST-2 / PC-1 권위 상승 + AR-3 시점 선차 변경 = 풀 3+1 + 외부 LLM 1+ 의무 |

### 4.2 4 sub-수단 *발효 시점* 합의 형태 권고 (선행 권위 답습)

⚠️ **N-4 권고 흡수 — 단축 자격 차단 단서**: 실 구현 sub-cycle = **(b)(d) evidence 충족 시 단축 합의 + 사용자 명시** 자격. (b)(d) evidence 미충족 시 단축 자격 0, 풀 3+1 재진입 의무. evidence 충족 = §3 매트릭스 (b)(d) cell 답습 (실 PoC + nightly workflow + actual run id + assertion).


| sub-수단 | 본 cycle 합의 형태 | 발효 후 *실 구현 sub-cycle* 합의 형태 권고 | 사유 |
|---------|-----------------|--------------------------------------|------|
| **S-3** | 풀 3+1 + 외부 LLM 1+ | **단축 합의 + 사용자 명시** (사용자 명시 결정 1회) | 본 cycle 합의 = 수단 결정 + plugin catalog 본문 채택 발효. 실 구현 sub-cycle = workflow step 추가 + plugin 활성화 hardcoded list = 본 cycle 결정 *집행*. 별도 풀 3+1 0건 |
| **ST-2** | 풀 3+1 + 외부 LLM 1+ | **단축 합의 + 사용자 명시** (docker-compose 본문 답습 1회) | 본 cycle 합의 = 수단 결정 + sidecar 운영 정책 본문 채택 발효. 실 구현 sub-cycle = docker-compose sidecar + inotify-tools 의존성 추가 = 본 cycle 결정 *집행* |
| **PC-1** | 풀 3+1 + 외부 LLM 1+ | **단축 합의 + 사용자 명시** (README + CONTRIBUTING.md + onboarding 스크립트 답습 1회) | 본 cycle 합의 = T3 의무화 결정 발효. 실 구현 sub-cycle = 문서 본문 + onboarding 스크립트 = 본 cycle 결정 *집행* |
| **AR-3** | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | **단축 합의 + 사용자 명시** (branch protection rule 본문 답습 1회) | 본 cycle 합의 = T3 영역 진입 + branch protection rule 본문 채택 발효. 실 구현 sub-cycle = GitHub API 호출 또는 web UI 변경 = 본 cycle 결정 *집행*. 추가 변경 (admin bypass 정책 / signed commit 강제 등) = 별도 풀 3+1 |

→ **본 cycle 합의 발효 자격 = "4 sub-수단 모두 *수단 결정* 발효 + 본문 채택 발효" — 즉 실 구현 sub-cycle 4개 모두 단축 합의 + 사용자 명시 자격 (별도 풀 3+1 0건) 영역 진입 권한 발효**.

### 4.3 7 풀 3+1 승격 트리거 검증 (본 cycle 자체 ↔ 4 sub-수단별)

> 본 §4.3 = 본 cycle 자체가 7 풀 3+1 승격 트리거 발화 자격 검증. 본 cycle 이 *이미* 풀 3+1 자격으로 진입 결정됨 (carry-over 사용자 명시) → 본 §4.3 = *추가* 트리거 발화 시점 확인 한정.

| # | 7 풀 3+1 승격 트리거 | 본 cycle 발화 여부 |
|---|---------------------|------------------|
| 1 | 9 sub-수단 *외* 수단 재결정 권고 | ❌ 0건 — 본 cycle = roadmap-mvp1 §5.5 9 sub-수단 본문 채택 + 1.5차 보강 영역 답습 (재결정 0건) |
| 2 | T3 영역 *자동* 진입 | ⚠️ **부분 발화** — PC-1 T3 dev 환경 강제 + AR-3 branch protection rule = T3 영역 진입. 단, **사용자 명시 carry-over** + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 합의 모두 충족 = ADR-011 §2.4 T3 영역 의무 답습 = *정당한* T3 영역 진입 (자동 진입 ≠ 사용자 명시 진입) |
| 3 | 9 sub-수단 *재결정* (roadmap §5.5 본문 채택 변경) | ❌ 0건 — 본 cycle = 9 sub-수단 답습 위에서 *보강* (재결정 0건) |
| 4 | Tier-2/3 catalog *확장* (S-3 plugin / URL / 모델 vendor 추가) | ⚠️ **부분 발화** — S-3 plugin 활성화 catalog 본문 채택. 단, **Tier-1 답습 plugin 한정** (detect-secrets CLI 실 identifier — `AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` 등, baseline file 금지, R-4 BLOCKING 흡수) → Tier-2/3 확장 0건. *Tier-1 plugin 본문 채택* = 본 cycle 합의 영역, *Tier-2/3 확장* = 별도 합의 |
| 5 | 헌법 / ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 | ❌ 0건 — 본 cycle = ADR / 헌법 본문 변경 0건 (cross-reference 한정도 별도 commit 영역) |
| 6 | MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 | ❌ 0건 — 본 cycle = MVP-1 1.5차 보강 한정 (Layer D / Layer E / Layer F 모두 영역 외) |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ❌ 0건 — 본 cycle = 외부 LLM 응답 1+ 의무 (사용자 준비 영역 답습) |

→ **본 cycle 자체 발화 = 트리거 #2 + #4 부분 발화** (T3 영역 진입 + Tier-1 plugin 본문 채택). 단, *사용자 명시 + 풀 3+1 + 외부 LLM 1+* 3 조건 모두 충족 = 정당한 발화 (자동 진입 ≠ 사용자 명시 진입) → 본 cycle 합의 *발효 자격* 충실.

---

## 5. Rollback Trigger / Evidence 기준 (본 cycle 합의 발효 시점 의무)

### 5.1 4 sub-수단별 Rollback Trigger 본문 후보

> **본 §5.1 = 본 cycle 합의 발효 시점 Rollback Trigger 본문 채택 후보**. 실 trigger 발화 = 별도 합의 (단축 또는 풀 3+1, trigger 형태에 따라).

| Trigger ID | sub-수단 | trigger 정의 | 발화 시 행동 |
|-----------|---------|------------|-------------|
| **R-MVP1-1.5-S3-1** | S-3 | detect-secrets plugin 활성화 추가 (Tier-2/3 vendor — Slack/GCP/Azure 등) | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| **R-MVP1-1.5-S3-2** | S-3 | baseline file 도입 시도 (silenceable 위험) | **영구 금지** (본 cycle 합의 발효 시 본문 채택 — 합의 변경 = 풀 3+1) |
| **R-MVP1-1.5-S3-3** | S-3 | S-1 답습 step 제거 / 대체 시도 | **영구 금지** (Defense in depth 답습) |
| **R-MVP1-1.5-ST2-1** | ST-2 | inotify event 응답 시간 측정 = 합의된 threshold 초과 (threshold 후보 = <1초 / <500ms 등, 별도 합의 영역, R-7 BLOCKING 흡수) | threshold 재결정 합의 (단축 합의 적격) |
| **R-MVP1-1.5-ST2-2** | ST-2 | Hermes upstream Dockerfile 변경 의무 발생 | 풀 3+1 합의 + Hermes upstream PR 검토 + 외부 LLM 1+ |
| **R-MVP1-1.5-ST2-3** | ST-2 | sidecar process 운영 부담 / failure mode 발견 | Operational Readiness PASS (Layer E) 영역 진입 합의 (Backlog #7) |
| **R-MVP1-1.5-PC1-1** | PC-1 | `pre-commit install` 미실행 commit 발견 (dev 환경 강제 우회) — **탐지 경로**: (i) hook marker grep / (ii) `pre-commit run --all-files` 결과 CI 비교 / (iii) setup audit log evidence (R-6 BLOCKING 흡수) | dev 환경 강제 메커니즘 재검토 (단축 합의 + 사용자 명시) |
| **R-MVP1-1.5-PC1-2** | PC-1 | `.pre-commit-config.yaml` 본문 변경 — 차등 (R-7 BLOCKING 흡수): (i) 신규 hook = Tier-2/3 catalog / provider policy / security gate 변경 / (ii) 단순 version pin / hook config update | (i) 풀 3+1 + 외부 LLM 1+ / (ii) 단축 합의 + 사용자 명시 |
| **R-MVP1-1.5-PC1-3** | PC-1 | branch protection rule 통합 차단 (AR-3 발효 차단) | 본 cycle 합의 재검토 (풀 3+1 + 외부 LLM 1+) |
| **R-MVP1-1.5-AR3-1** | AR-3 | branch protection rule 본문 변경 의무 (admin bypass 정책 / signed commit 강제 추가) | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 (T3 영역 답습) |
| **R-MVP1-1.5-AR3-2a** | AR-3 | AR-1 답습 11 workflow 본문 변경 (도구 변경 영향 분석, R-7 BLOCKING 흡수 — AR3-2 분리) | 풀 3+1 합의 (도구 변경 영향 분석) |
| **R-MVP1-1.5-AR3-2b** | AR-3 | 신규 status check 추가 (T3 정책 영역, R-7 BLOCKING 흡수 — AR3-2 분리) | 풀 3+1 + 외부 LLM 1+ |
| **R-MVP1-1.5-AR3-3** | AR-3 | branch protection rule status check actual run 실패 (FP) — **판정 기준**: (i) 동일 PR 재실행 PASS / (ii) 다른 PR cross-check / (iii) workflow log evidence (N-7 권고 흡수) | 단축 합의 + 사용자 명시 (rule 본문 fine-tuning) |

### 5.2 Evidence Required (5 형식 답습 — roadmap §6.3 + ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 답습)

| Evidence | 형식 | S-3 | ST-2 | PC-1 | AR-3 |
|----------|------|-----|------|------|------|
| **(a) Markdown report** | `docs/phase0/g2-gp3-mvp1-evidence.md` + `docs/phase0/g2-gp5-mvp1-evidence.md` 답습 (1.5차 보강 evidence 통합) | ✅ S-3 plugin 활성화 + testfile evidence | ✅ inotify event 인지 evidence | ✅ pre-commit install 강제 evidence | ✅ branch protection rule evidence |
| **(b) JSONL Ledger entry** | `docs/evidence/ledger.jsonl` (ADR-012 §2.2 답습) — event enum 후보 §5.3 답습 | ✅ `secret_scan_layer1_implementation` 답습 + S-3 plugin 명시 field | ✅ `secret_storage_isolation_enhanced` (가칭, 본 cycle 발효 시 등록) | ✅ `precommit_framework_mandatory_enforcement` (가칭, 본 cycle 발효 시 등록) | ✅ `pr_auto_reject_branch_protection_enforced` (가칭, 본 cycle 발효 시 등록) |
| **(c) Docker isolation log** | docker secret + sidecar 시뮬레이션 evidence (격리 환경) | ✅ S-3 scanner stateless · network-free | ✅ inotify sidecar 격리 시뮬레이션 | ✅ pre-commit hook 격리 (`stateless`) | ✅ branch protection rule 시뮬레이션 (격리 0 — GitHub API 영역) |
| **(d) GitHub Actions run** | actual run id + nightly run id | ✅ secret-hygiene-egress-redaction.yml + S-3 step 통합 run id | ✅ docker_secret_inotify_sidecar_check.sh nightly run id | ✅ pre-commit CI step 통합 run id | ✅ branch protection rule status check run id |
| **(e) 합의 보고서** | `docs/review/3plus1-consensus-<date>-mvp1-1.5th-reinforcement-entry.md` (본 cycle) + 실 구현 sub-cycle 별도 합의 보고서 4개 | ✅ 본 cycle 합의 보고서 (S-3 영역 §) | ✅ 본 cycle 합의 보고서 (ST-2 영역 §) | ✅ 본 cycle 합의 보고서 (PC-1 영역 §) | ✅ 본 cycle 합의 보고서 (AR-3 영역 §) |

### 5.3 JSONL Ledger event enum 후보 (본 cycle 합의 발효 시점 신규 등록 영역)

| event enum (신규 후보) | trigger | T1/T2/T3 | 등록 자격 |
|----------------------|---------|---------|----------|
| `s3_detect_secrets_partial_integration_enforced` (또는 `secret_scan_layer1_implementation` field 확장) | S-3 plugin 활성화 + Tier-1 catalog scan PASS | T2 (CI step) | 본 cycle 합의 발효 시점 (ADR-012 §2.2 + G4 §10.2 답습 별도 합의) |
| `st2_inotify_sidecar_runtime_enforced` (또는 `secret_storage_isolation_enhanced`) | ST-2 sidecar 인지 event nightly PASS | T2 (Hermes runtime sidecar) | 본 cycle 합의 발효 시점 |
| `pc1_precommit_framework_mandatory_enforcement` | PC-1 의무화 dev 환경 강제 evidence | T3 (dev 환경 정책) | 본 cycle 합의 발효 시점 |
| `ar3_pr_auto_reject_branch_protection_enforced` | AR-3 branch protection rule status check PASS | T3 (branch protection rule) | 본 cycle 합의 발효 시점 |

→ 본 4 enum 후보 = **본 cycle 합의 발효 시점 정식 등록 자격 영역**. 단, *정식 등록 commit* = ADR-012 §2.2 + G4 §10.2 답습 별도 commit (본 cycle 합의 발효 후 별도 sub-cycle).

---

## 6. 금지 사항

### 6.1 본 brief 자체 금지 사항 (사용자 명시 답습 + 본 brief 영역 한계)

§0.3 매트릭스 20 항목 답습. 본 brief 작성 시점 위반 0건 자기진단.

### 6.2 본 brief 발효 *후* 실 구현 sub-cycle 진입 시점 금지 사항 (의무 답습)

| # | 영역 | 의무 |
|---|------|------|
| 1 | 본 cycle 합의 발효 직후 *자동 실 구현* 진입 | 0건 (사용자 명시 결정 + sub-cycle 별 별도 합의 의무) |
| 2 | 4 sub-수단 *외* 수단 자동 진입 (S-1 대체 / ST-1 / ST-5 / PC-2 / AR-2 단독 등) | 0건 (별도 합의 영역) |
| 3 | Tier-2 / Tier-3 catalog *본문 확장* (Slack / GCP / Azure / URL Tier-2/3 vendor 등) | 0건 (별도 풀 3+1 + 외부 LLM 1+) |
| 4 | Backlog #3 *전체* 진입 (AR-3 단독 시점 변경 외 다른 항목) | 0건 (별도 합의) |
| 5 | Hermes upstream Dockerfile 변경 | 0건 (ST-2 = sidecar 분리 가능 답습) |
| 6 | facade real 본문 (G5-4) 동시 진입 | 0건 (TR-1 별도 trajectory) |
| 7 | 헌법 / ADR 본문 갱신 (cross-reference 포함) | 0건 (별도 commit + 별도 합의) |
| 8 | Implementation Evidence PASS *자동* 발효 | 0건 ((c) 진입점 별도 합의) |
| 9 | **branch protection rule 변경** (AR-3 실 구현) = 코드 변경 0건과 *별개* 운영 정책 변경 — 사용자 명시 결정 의무 직접 묶기 (N-5 권고 흡수) | 0건 (구현 sub-cycle 사용자 명시 + evidence 전까지) |
| 10 | AR-3 외 branch protection 정책 변경 (force-push / signed commit / fork PR / linear history) | 0건 (각각 별도 합의 영역, N-6 권고 흡수) |

---

## 7. 외부 LLM 응답 요구 영역 (사용자 준비 자료)

### 7.1 외부 LLM 응답 1+ 의무 답습 출처

| 출처 | verbatim 답습 |
|------|--------------|
| **carry-over (b) 사용자 명시** | "사용자 준비 영역: **외부 LLM 응답 1+** (Claude 가 외부 LLM 호출 못 함, 사용자 직접 호출 의무)" |
| **roadmap §3.6.3 line 289 (S-3)** | "**풀 3+1 합의 + 외부 LLM 1+**" |
| **roadmap §4.7.3 line 480 (AR-3)** | "**풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시**" |
| **ADR-011 §2.4 T3 영역 답습** | T3 영역 = 외부 LLM cross-vendor blind 차단 의무 |

### 7.2 외부 LLM 응답 *입력 자료* 정의 (사용자 준비 영역)

외부 LLM (GPT-5 / Gemini 2.5 / 다른 vendor 1+) 에게 *직접 제출* 의무 자료:

1. **본 brief 본문 전체** (`docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` v1)
2. **선행 권위 답습 자료**:
   - `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(e) + §2.4)
   - `docs/architecture/implementation-runtime-roadmap-mvp1.md` (§3.2 + §3.3 + §3.6.3 + §4.3 + §4.4 + §4.7.3)
   - `docs/phase0/backlog1-gp3-1.5-deepening-brief.md`
   - `docs/phase0/backlog2-gp5-1.5-remaining-items-brief.md`
   - `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md`
   - `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md`
   - `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (audit 결과 답습)
3. **본 cycle 합의 형태** = 풀 3+1 + 외부 LLM 1+ (carry-over verbatim 답습)

### 7.3 외부 LLM 응답 *자격 검증* 기준 (Reviewer 검토 영역)

| # | 검증 기준 | 통과 의무 |
|---|---------|----------|
| 1 | 외부 LLM 응답이 4 sub-수단 모두에 대한 *입장* (APPROVE / REVISE / REJECT) 명시 | ✅ 의무 |
| 2 | 외부 LLM 응답이 본 brief §1.3 선차 변경 매트릭스 (3 sub-수단 권위 상승) 에 대한 *명시적 입장* | ✅ 의무 |
| 3 | 외부 LLM 응답이 ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 (§3) 에 대한 *충족 평가* | ✅ 의무 |
| 4 | 외부 LLM 응답이 본 brief §5.1 Rollback Trigger 본문 후보 (12 trigger) 에 대한 *완전성 평가* | ✅ 의무 |
| 5 | 외부 LLM 응답이 본 brief §6 금지 사항 + §7.3 자격 검증 기준 자체에 대한 *cross-check* | ✅ 의무 |
| 6 | 외부 LLM cross-vendor blind risk 차단 (응답 vendor = 본 cycle 풀 3+1 Agent A/B/C/Reviewer 의 vendor 와 *다른 vendor*) | ✅ 의무 (cross-vendor 답습) |
| 7 | 외부 LLM 응답이 *추가 위험 / 누락 영역* 제시 | ✅ 권고 (필수 0건, 권고 한정) |

→ **외부 LLM 응답 *부재 시* 본 cycle 합의 진입 자격 0건** — 풀 3+1 합의 진입 *전* 외부 LLM 응답 1+ 첨부 사용자 명시 의무 답습.

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 brief 작성 후 사용자 결정:

| 옵션 | 다음 단계 | 비고 |
|------|---------|------|
| **(A)** | 본 brief v1 검토 후 **승인** → 외부 LLM 응답 1+ 자료 첨부 → 풀 3+1 합의 진입 | **권고** (carry-over 답습) |
| **(B)** | 본 brief v1 *수정 요구* → brief v1.1 재작성 → (A) 진입 | 본 brief framing / scope 조정 필요 시 |
| **(C)** | 본 brief 영역 *축소* (4 → 1~3 sub-수단 한정) → brief 재작성 → 풀 3+1 합의 | carry-over scope (4 sub-수단 모두) 와 충돌 가능 |
| **(D)** | 본 brief 영역 *확장* (4 → +ST-1 / +S-2 / +Backlog #3 등) → brief 재작성 → 풀 3+1 합의 | carry-over scope 외 영역 추가 = 사용자 명시 재결정 의무 |
| **(E)** | 본 brief *기각* — MVP-1 1.5차 보강 전체 영역 미진입 → 다른 carry-over 항목 (c)(d) 또는 다른 작업 | carry-over (b) 명시 폐기 = 사용자 명시 의무 |
| **(F)** | 본 brief *부분 승인* (특정 sub-수단 결정 1~3개 한정) → 부분 풀 3+1 합의 | 4 sub-수단 *결합* 효과 (PC-1 + AR-3 = Defense in depth) 손실 risk |

⚠️ **본 brief APPROVE 직후 자동 다음 단계 진입 금지** — 사용자 명시 결정 의무 (단계별 합의 cycle 패턴 답습).

⚠️ **사용자 권고 진입 = (A)** — carry-over (b) 답습 충실성.

### 8.1 본 brief 발효 *후* (= 본 cycle 합의 APPROVE 시점) 다음 단계 (사용자 결정 영역)

본 cycle 합의 APPROVE *후* 다음 sub-cycle 4개:

1. **S-3 실 구현 sub-cycle** — `pip install detect-secrets` + workflow step 추가 + plugin 활성화 hardcoded list + Tier-1 catalog testfile evidence + 단축 합의 + 사용자 명시
2. **ST-2 실 구현 sub-cycle** — docker-compose sidecar + inotify-tools 의존성 추가 + `tools/docker_secret_inotify_sidecar_check.sh` nightly workflow 통합 + 단축 합의 + 사용자 명시
3. **PC-1 실 구현 sub-cycle** — README + CONTRIBUTING.md + `bin/setup.sh` 또는 `make setup` + dev 환경 강제 evidence (audit log 형식) + 단축 합의 + 사용자 명시
4. **AR-3 실 구현 sub-cycle** — GitHub branch protection rule (`main` + `develop`) + status check 의무 + admin bypass 0건 + GitHub API 호출 또는 web UI 변경 evidence + 단축 합의 + 사용자 명시

→ 4 sub-cycle 모두 *별도* commit + *별도* evidence + *별도* 사용자 명시 결정. 자동 진입 0건.

→ 4 sub-cycle 완료 후 **Implementation Evidence PASS 발효 합의** ((c) 진입점, audit brief §5 답습) = ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5/5 + conditions 해소 + 사용자 명시 별도 합의 영역.

---

## 9. 답습 참조

### 9.1 상위 권위

- [[ADR-011-means-vs-ends-redaction]] §2.1 (a)~(e) 5조건 + §2.4 T1/T2/T3 분리
- [[implementation-runtime-roadmap-mvp1]] APPROVED (`c2bcb19` line 826/827) §3.2 / §3.3 / §3.6.3 / §4.3 / §4.4 / §4.7.3
- [[PROJECT_CONSTITUTION]] 제8조 (보안) + 제5조-2 (Provider Liquidity, 비협상)
- [[ADR-008]] 6 차단조건 #1 (SQLCipher) + #6 (Docker 격리 + egress 화이트리스트) + #4 (provider adapter) — R-S1 정정 답습 (cross-reference 별도 commit 영역, N-9 권고)

### 9.2 직접 선행 자료

- [[backlog1-gp3-1.5-deepening-brief]] (ST-1 / ST-2 / PC-4 영역 분류)
- [[backlog2-gp5-1.5-remaining-items-brief]] (T-1 / T-3 / T-4 / T-5 / AR-3 영역 분류)
- `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` (APPROVE Keep Deferred)
- `docs/review/3plus1-consensus-2026-05-13-pc4-t2-c5c-c6-satisfaction.md` (PC-4 T2 sub Partially Satisfied)
- [[mvp1-gp3-gp5-current-state-audit-brief]] (audit 결과 답습)
- `docs/sessions/SESSION_2026-05-27.md` 23번째 entry carry-over (b) verbatim
- commit `c2bcb19` (carry-over scope 명시)

### 9.3 메타 영역

- [[ceremony-inflation]] — 본 brief = 실 결정 cycle, ceremony-inflation 0건
- [[meta-cycle-warning]] — 본 brief 진입 3-질문 self-check 통과 (정정 차수 0, 본업 진입)
- [[staged-consensus-workflow]] — brief → 승인 → 합의 → commit → push 6단계 답습
- [[provider-liquidity]] — 본 cycle T3 영역 (PC-1 / AR-3) provider 의존 0건 (CI / branch protection / dev 환경 영역)

### 9.4 관련 도구 / workflow (audit brief §2 답습)

- `tools/secret_scanner.py` (S-1 답습) + `tools/docker_secret_inotify_sidecar_check.sh` (ST-2 실 구현) + `.pre-commit-config.yaml` (PC-4 T2 sub) + `.github/workflows/*.yml` (11 workflow, AR-1 답습)
- `src/adapters/llm/facade.py` (G5-4 placeholder, TR-1 별도 trajectory — 본 cycle 영역 외)

### 9.5 본 brief 발효 후 cross-reference 갱신 영역 (별도 commit)

- ADR-008 6 차단조건 #1 + #6 cross-reference (ST-2 발효 시점, R-S1 권위 chain 정정 별도 sub-cycle 영역 — N-9 권고)
- ADR-010 cross-reference (Vault HSM 영역 외 유지)
- ADR-012 §2.2 event enum 정식 등록 (§5.3 4 enum 후보)
- roadmap-mvp1 §3.6.3 + §4.7.3 변경 이력 (본 cycle 합의 보고서 cross-reference)
- `docs/CONTEXT.md` 24번째 entry 등재
- `docs/INDEX.md` 본 brief + 본 cycle 합의 보고서 등재

---

## 10. 본 brief v1 작성 자격 자기진단

| # | 자기진단 항목 | 통과 |
|---|-------------|------|
| 1 | 본 brief 작성 시점 실 코드 / CI / hook / branch protection / `.pre-commit-config.yaml` 본문 변경 0건 | ✅ |
| 2 | 본 brief 작성 시점 ADR / 헌법 본문 변경 0건 | ✅ |
| 3 | 본 brief 작성 시점 MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 0건 | ✅ |
| 4 | 본 brief 영역 = 4 sub-수단 *진입 합의 entry* 한정 (수단 결정 0건 — 결정은 풀 3+1 합의 결과에 의존) | ✅ |
| 5 | 본 brief §1.3 선차 변경 매트릭스 = 선행 권위 vs 본 cycle 차이 명문 | ✅ |
| 6 | 본 brief §3 ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 4 sub-수단 별 명시 (R-1 BLOCKING 흡수) | ✅ |
| 7 | 본 brief §4.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화 (6 답습 출처) | ✅ |
| 8 | 본 brief §4.3 7 풀 3+1 승격 트리거 발화 검증 | ✅ |
| 9 | 본 brief §5 Rollback Trigger 12 본문 후보 + Evidence 5 형식 + JSONL event 4 enum 후보 | ✅ |
| 10 | 본 brief §6 금지 사항 + §7 외부 LLM 응답 요구 영역 + §7.3 자격 검증 기준 | ✅ |
| 11 | 본 brief §8 다음 단계 옵션 (사용자 결정 영역) | ✅ |
| 12 | 본 brief 자체 권위 chain 등재 / 영구화 0건 (본 cycle 합의 input 한정) | ✅ |
| 13 | ceremony-inflation 차단 + meta-cycle 자기진단 통과 (정정 차수 0, 본업 진입) | ✅ |

→ **13/13 통과** — 본 brief v1 = 풀 3+1 합의 input 자격 충족. 다음 단계 = 사용자 승인 + 외부 LLM 응답 1+ 자료 첨부 (§8 (A) 권고).

---

## 11. v1.1 보강 매트릭스 (BLOCKING 7 + 권고 12 흡수)

> **본 §11 = v1.1 보강 변경 매트릭스**. brief v1 (풀 3+1 합의 input) → 본 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md`) APPROVE WITH CONDITIONS (BLOCKING 7 + 권고 12) → 본 v1.1 보강 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 회피, `feedback_ceremony_inflation` memory 답습).

### 11.1 BLOCKING 7 흡수 매트릭스

| BLOCKING ID | 흡수 위치 | 변경 요약 |
|------------|---------|----------|
| **R-1** (3-way 일치 + cross-vendor) | §0.2 DONE 기준 #1 / §0.2 *하는 것* #1 / §1.3 요약 / §3 매트릭스 제목 + 서문 / §5.2 Evidence 제목 / §7.3 검증 기준 #3 / §8.1 #4 / §10 자기진단 #6 (8 위치) | "ADR-011 §2.1 (a)~(e) 5조건" → "ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) — 5조건 매트릭스 (ADR-011 §3 후속 권위 답습)" 정합 표기. 매트릭스 *내용* 자체 정합 유지 (Agent B nuance 답습) |
| **R-2** (3-way 일치) | §3 매트릭스 (b) PC-1 cell + (d) PC-1 cell | "✅ PC-4 T2 sub `78483c5` Partially Satisfied 답습" → "⏳ T3 mandatory enforcement PoC 미충족 — opt-in PoC (T2) ≠ T3 의무화 PoC, 본 cycle 발효 후 onboarding + install enforcement + bypass detection evidence 별도 sub-cycle" |
| **R-3** (3-way 일치 + cross-vendor) | §2.4.2 채택 조건 + §3 매트릭스 (b)(d) AR-3 cell | "11 workflow 모두 required status check" → "required check 단위 = workflow file명 ≠ 실제 check name (GitHub branch protection = job name 또는 workflow_run.conclusion 단위 mapping). 실제 check name list catalog 본문 채택 = 실 구현 sub-cycle 영역" |
| **R-4** (2-way 격상 + cross-vendor) | §2.1.2 채택 조건 + §2.1.3 catalog 본문 + §4.3 트리거 #4 | "AWS / Generic / Base64" → "detect-secrets CLI 실 plugin identifier 예: `AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` / `HexHighEntropyString` / `PrivateKeyDetector`" + `--baseline` 미사용 CI assertion 의무 |
| **R-5** (2-way 격상 + cross-vendor) | §2.2.3 채택 결정 + §3 매트릭스 (b)(d) ST-2 cell | 3 단계 evidence 의무 추가: (1) event 인지 + (2) sidecar → 메인 정지 signal + (3) **메인 workload fail-closed 확인** |
| **R-S1** ⭐⭐⭐ (Reviewer 단독 격상, raw line-level verify) | §1.2 ST-2 권위 출처 + §2.2.1 권위 출처 + §3 매트릭스 (c) row + §9.2 답습 참조 + §9.5 cross-reference (4 위치) | "ADR-008 §A.2 R1-2 ('저장 경로 secret 보호')" → "ADR-008 6 차단조건 #1 (SQLCipher) + #6 (Docker 격리 + egress 화이트리스트) cross-reference (line 17~23 verbatim 답습). ADR-008 본문 §A.2 = 'Hermes JSONL Export 검증' (line 136), R1-2 / §2.6 식별자 ADR-008 본문 부재 (raw line-level verify). 정확 R1-2 source 위치 + 일관 정정 = **본 cycle scope 외 cross-reference 별도 commit 영역 (N-9 권고 답습)**" |
| **R-6** (1-Agent) | §5.1 R-MVP1-1.5-PC1-1 trigger 본문 | "탐지 경로: (i) hook marker grep / (ii) `pre-commit run --all-files` 결과 CI 비교 / (iii) setup audit log evidence" 명시 |
| **R-7** (1-Agent) | §5.1 R-MVP1-1.5-ST2-1 + PC1-2 + AR3-2 (3 trigger 정정) | (a) ST2-1 ">1초" → "합의된 threshold 초과" (threshold 후보 framing 보존) / (b) PC1-2 차등 (신규 hook vs version pin) / (c) AR3-2 분리 (R-MVP1-1.5-AR3-2a 도구 변경 + R-MVP1-1.5-AR3-2b T3 정책 신규 check) |

### 11.2 권고 12 흡수 매트릭스

| 권고 ID | 흡수 위치 | 변경 요약 |
|---------|---------|----------|
| **N-1** (PC-1 결합 효과) | §2.3.3 채택 결정 | "PC-1 + PC-3 + AR-3 결합 의무화 효과 명문" 추가 (PC-1 단독 보안 ≈ 0, 결합 시점 발효) |
| **N-2** (PC-1-T3 명칭 일관) | §2.3.3 + §11 본문 | "PC-1-T3 mandatory enforcement" 명칭 일관 도입 |
| **N-3** (AR-3 boundary 명문 반복) | §2.4.4 미발효 영역 | "AR-3 = Backlog #3 의 *AR-3 sub-수단 단독 시점 변경* 한정" 명문 반복 강화 |
| **N-4** (단축 자격 차단 단서) | §4.2 발효 시점 합의 형태 | "(b)(d) evidence 충족 시 단축 합의 + 사용자 명시" 단서 추가 |
| **N-5** (branch protection 직접 묶기) | §6.2 #9 (신규) | "branch protection rule 변경 = 코드 변경 0건과 별개 운영 정책 — 사용자 명시 결정 의무 직접 묶기" |
| **N-6** (AR-3 외 정책 별도) | §2.4.4 + §6.2 #10 (신규) | force-push / signed commit / fork PR / linear history = 별도 합의 명문 |
| **N-7** (AR3-3 FP 기준) | §5.1 R-MVP1-1.5-AR3-3 trigger 본문 | "판정 기준: (i) 동일 PR 재실행 PASS / (ii) 다른 PR cross-check / (iii) workflow log evidence" 명시 |
| **N-8** (roadmap §3.6.3 framing) | (본 cycle scope 외, 별도 cross-reference commit 영역) | 본 brief 명문 0건, 본 cycle 합의 발효 후 별도 sub-cycle 영역 답습 |
| **N-9** (R-S1 권위 chain 정정) | (본 cycle scope 외, 별도 cross-reference commit 영역) | §1.2 + §2.2.1 + §9.2 + §9.5 의 R-S1 정정 답습 *명문*, governance-preconditions / backlog1 합의 본문 정정 = 별도 sub-cycle |
| **N-10** (외부 LLM 2+ 향후) | (본 cycle 자격 충족 1+, 추후 다양화 권고 한정) | 본 brief 명문 0건, §7 답습 |
| **N-11** (옵션 (B) 권고 = 본 합의 결과 흡수) | §8 옵션 선택 = 본 cycle 합의 = (B) 진입 후 발효 | 본 §11 자체 = (B) 진입 답습 결과 |
| **N-12** (사용자 명시 묶기) | §6.2 #9 답습 + §7.3 자격 검증 + §8.1 (4) AR-3 sub-cycle | "branch protection 변경 = 사용자 명시 결정 직접 묶기" 답습 강화 |

### 11.3 본 v1.1 보강 자체 진행 정직성

| # | 본 v1.1 보강 자체 진행 | 통과 |
|---|---------------------|------|
| 1 | 본 cycle scope *외* 영역 변경 0건 (governance-preconditions / backlog1 합의 / ADR 본문 / roadmap-mvp1 본문 모두 변경 0건) | ✅ |
| 2 | BLOCKING 7 모두 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단) | ✅ |
| 3 | 권고 12 흡수 (핵심 8 명문, scope 외 4 명문 0 + 답습 cross-reference) | ✅ |
| 4 | R-1 정정 = 명칭만 변경, 매트릭스 *내용* 정합 유지 (Agent B nuance 답습) | ✅ |
| 5 | R-S1 정정 = brief 인용 한정 + 본 cycle scope 외 명문 (cross-reference 정정은 별도 sub-cycle) | ✅ |
| 6 | 4 sub-수단 *채택 결정 발효 자격* (brief §0.4 답습) — 본 v1.1 commit 시점 = 본 cycle 합의 발효 시점 | ✅ |
| 7 | 실 코드 / CI / hook / branch protection / config 본문 변경 0건 | ✅ |
| 8 | ADR / 헌법 / roadmap 본문 변경 0건 | ✅ |
| 9 | 자동 진입 / 자동 발효 0건 (다음 단계 = 사용자 명시 결정 의무, 단계별 합의 cycle 답습) | ✅ |

→ **9/9 통과** — brief v1.1 = 본 cycle 합의 발효 자격 충실. 다음 단계 = 본 cycle commit (brief v1.1 + 합의 보고서 + 3 Agent 출력 + codex 응답 + SESSION + INDEX) + 사용자 명시 push.
