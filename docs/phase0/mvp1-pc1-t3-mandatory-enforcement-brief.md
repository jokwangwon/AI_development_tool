# MVP-1 PC-1-T3 mandatory enforcement 실 구현 sub-cycle brief

> **scope**: MVP-1 1.5차 보강 entry 합의 (24번째 entry, commit `9638521` brief v1.1 + 합의 보고서 `3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` APPROVE WITH CONDITIONS) 의 **PC-1-T3 mandatory enforcement 실 구현 sub-cycle**. 본 sub-cycle = entry 합의 결정 *집행* (T3 채택 결정 자체는 entry cycle 에서 완료).
>
> **본 brief 자체에서 실 코드 변경 0건 의무** — brief 합의 발효 *후* 별도 실 구현 단계에서 file 생성/수정.

---

## §0 답습 출처 (인용 source)

| Source | 위치 | 답습 내용 |
|---|---|---|
| **24번째 entry brief v1.1** | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (commit `9638521`) | §2.3 PC-1 정의 (line 183~211) + §3 ADR-011 (a)~(e) 매트릭스 (PC-1 cell) + §4 합의 형태 권고 (line 292 "단축 합의 + 사용자 명시") + §5.1 Rollback Trigger R-MVP1-1.5-PC1-{1,2,3} (line 329~331) + §6 Evidence 행 (line 343~345) + §7.3 외부 LLM 자격 |
| **24번째 entry 합의 보고서** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | R-2 BLOCKING (PC-1 (b)(d) 재분류) / R-6 BLOCKING (PC1-1 탐지 경로 (i)(ii)(iii)) / R-7(b) BLOCKING (PC1-2 차등) / N-1 권고 (PC-1 단독 우회 가능, PC-3 + AR-3 결합 효과 명문) / N-2 권고 (PC-1-T3 명칭 일관) |
| **ADR-011** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 (수단 결정 발효 자격) + §2.4 T3 영역 (dev 환경 정책) |
| **PC-4 T2 sub** | `docs/review/3plus1-consensus-2026-05-13-pc4-t2-implementation-entry.md` (commit `3c0a1c1`) | `.pre-commit-config.yaml` opt-in framework 채택 (T2 영역). 본 sub-cycle = T2 opt-in → T3 의무화 영역 상승 |
| **CLAUDE.md** | line 41 ("3. git pre-commit hook (센서) ~30s 강제 차단") | Layer 3 답습 영역 |

---

## §1 scope (PC-1 sub-cycle 한정)

### 1.1 본 sub-cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | PC-1-T3 mandatory enforcement 실 구현 (entry 합의 결정 *집행*) |
| **영역** | GP-3 + GP-5 T3 dev 환경 강제 |
| **합의 형태 권고** | **단축 합의 + 사용자 명시** (entry brief line 292 답습) |
| **변경 0건 의무** | `.pre-commit-config.yaml` 본문 변경 0건 / hook 정의 본문 0건 / src/ 0건 / tools/ 0건 / `.githooks/pre-commit` 본문 변경 0건 / CI workflow 본문 변경 0건 / ADR 0건 / 헌법 0건 / roadmap 본문 0건 |
| **변경 허용 영역** | README.md (안내 추가) + CONTRIBUTING.md (신규) + onboarding 스크립트 신규 (`bin/setup.sh` 또는 `Makefile`) + `requirements-dev.txt` (`pre-commit` 패키지 추가) + audit log + bypass detection 메커니즘 |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | `.pre-commit-config.yaml` 본문 변경 (신규 hook / version pin 외 모든 변경) | 0건 (별도 cycle, R-7(b) 차등) |
| 2 | `.githooks/pre-commit` 본문 변경 (Layer 3 grep 기반 자체 hook) | 0건 (`.githooks/` 시스템 답습 유지) |
| 3 | tools/ 본문 변경 (secret_scanner / workflow_secrets_usage_check / 등) | 0건 |
| 4 | src/ 본문 변경 | 0건 |
| 5 | CI workflow 본문 변경 | 0건 |
| 6 | branch protection rule 변경 (AR-3 sub-cycle 영역) | 0건 |
| 7 | Tier-2/3 catalog 확장 | 0건 |
| 8 | ADR / 헌법 / roadmap 본문 변경 | 0건 |
| 9 | MVP-1 Implementation Evidence PASS 발효 | 0건 ((c) carry-over 영역) |
| 10 | `adapters/llm/facade.py` placeholder → real | 0건 ((d) carry-over 영역) |

---

## §2 24번째 entry BLOCKING + 권고 흡수 매트릭스

| ID | 항목 | 본 brief 흡수 위치 |
|---|---|---|
| **R-2** BLOCKING | PC-1 (b)(d) PoC/회귀 상태 ⏳ 미충족 재분류 (T3 mandatory enforcement PoC 자격 0) | §4 실 구현 5 항목 (onboarding + install enforcement + bypass detection) 의무 → (b)(d) 충족 자격 발효 |
| **R-6** BLOCKING | R-MVP1-1.5-PC1-1 탐지 경로 (i) hook marker grep / (ii) `pre-commit run --all-files` 결과 CI 비교 / (iii) setup audit log | §4.4 audit log 메커니즘 + §4.5 bypass detection 메커니즘 = 탐지 경로 3 모두 발효 |
| **R-7(b)** BLOCKING | R-MVP1-1.5-PC1-2 차등 — 신규 hook (Tier-2/3 catalog / provider policy / security gate) = 풀 3+1, 단순 version pin = 단축 합의 | §6 Rollback Trigger 본 sub-cycle 적용 형태 (PC1-2 차등 답습) |
| **N-1** 권고 | PC-1 단독 우회 가능, PC-3 + AR-3 결합 효과 명문 | §1.3 결합 효과 명문 (PC-1 단독 보안 효과 ≈ 0) |
| **N-2** 권고 | PC-1-T3 mandatory enforcement 명칭 일관 | 본 brief 전체 "PC-1-T3" 명칭 일관 답습 |

### 1.3 PC-1 + PC-3 + AR-3 결합 효과 명문 (N-1 흡수)

PC-1 (dev 환경 hook) **단독 보안 효과 ≈ 0** — `pre-commit install` 로컬 우회 가능 (`git commit --no-verify`, `core.hooksPath` 변경, 등).

**실제 강제력 = PC-1 + PC-3 + AR-3 결합 시점 발효**:
- PC-1 (본 sub-cycle): dev 환경 `pre-commit install` 의무화 (1차 방어)
- PC-3 (이미 발효): CI step `.pre-commit-config.yaml` 검증 (2차 방어, 우회 차단)
- AR-3 (별도 sub-cycle): branch protection rule status check 의무 (3차 방어, merge 차단)

본 sub-cycle = **1차 방어 발효 한정**. 2차 방어 = PC-3 발효 답습 / 3차 방어 = AR-3 별도 sub-cycle 발효 시점.

---

## §3 현 상태 audit

### 3.1 이미 발효 (답습 영역)

| 자료 | 상태 | source |
|---|---|---|
| `.pre-commit-config.yaml` (6 hook, T2 opt-in) | ✅ 발효 (`3c0a1c1`) | secret-scanner / workflow-secret-usage / workflow-permissions / provider-import / provider-url-model / import-linter |
| `.githooks/setup.sh` | ✅ 발효 (Layer 3 자체 hook) | `git config core.hooksPath .githooks` |
| `.githooks/pre-commit` | ✅ 발효 (Layer 3 grep 기반) | 민감 정보 + 디버그 코드 자체 체크 (`.pre-commit-config.yaml` 과 별개 시스템) |
| README.md line 95~118 | ✅ 발효 (`.githooks/setup.sh` 안내) | "Git hooks 활성화" 1 줄 |

### 3.2 미충족 (본 sub-cycle 발효 대상)

| # | 항목 | 현 상태 | 본 sub-cycle 발효 |
|---|---|---|---|
| 1 | README.md `pre-commit install` 의무화 안내 | 0건 | 추가 (Layer 3 `.githooks/setup.sh` 와의 관계 명문) |
| 2 | CONTRIBUTING.md | 부재 | 신규 작성 (dev onboarding workflow + PC-1-T3 의무화 명문) |
| 3 | onboarding 스크립트 (`bin/setup.sh` 또는 `Makefile`) | 부재 | 신규 (사용자 결정: `bin/setup.sh` vs `Makefile` vs 둘 다) |
| 4 | `requirements-dev.txt` `pre-commit` 패키지 | 부재 | 추가 (PoC 자격 충족 의무) |
| 5 | `pre-commit install` enforcement audit log | 0건 | 신규 메커니즘 (사용자 결정: 후보 §4.4) |
| 6 | bypass detection evidence | 0건 | 신규 메커니즘 (사용자 결정: 후보 §4.5) |

### 3.3 `.githooks/` vs `.pre-commit-config.yaml` 관계 (사용자 결정 항목)

현 상태 = 두 시스템 **병렬** (`.githooks/pre-commit` = Layer 3 자체 grep + `.pre-commit-config.yaml` = pre-commit framework T2 opt-in). 본 sub-cycle = T3 mandatory enforcement → 두 시스템 관계 결정 필요:

| 후보 | 내용 | 트레이드오프 |
|---|---|---|
| **(α)** 병렬 유지 | `.githooks/setup.sh` + `pre-commit install` 모두 실행 의무 (onboarding 스크립트가 두 시스템 모두 활성화) | 안전성 ↑ (Defense in depth), 복잡성 ↑, hook 실행 시간 ↑ |
| **(β)** pre-commit framework 흡수 | `.githooks/pre-commit` 내용을 `.pre-commit-config.yaml` 의 신규 hook 으로 흡수 | 통합 ↑, 단 `.pre-commit-config.yaml` 본문 변경 = 별도 cycle (R-7(b) 차등) — **본 sub-cycle scope 외** |
| **(γ)** `.githooks/` 폐지 | `.githooks/pre-commit` 폐지 + `.pre-commit-config.yaml` 만 사용 | 단순화 ↑, 단 Layer 3 손실 (`.githooks/pre-commit` 본문 변경 = §1.2 #2 의무 위반) — **본 sub-cycle scope 외** |

→ **권고 = (α) 병렬 유지** (본 sub-cycle scope 안, `.pre-commit-config.yaml` 본문 변경 0건 의무 답습)

---

## §4 실 구현 5 항목

### 4.1 README.md 보강 (Layer 3 + pre-commit framework 병렬 안내)

**위치**: line 91~98 "하네스 인프라" 표 + line 113~120 "초기 설정" 영역

**변경 내용**:
- 하네스 인프라 표에 `.pre-commit-config.yaml` (T3 mandatory enforcement) 행 추가
- 초기 설정 영역에 `pre-commit install` 의무화 안내 추가
- Layer 3 (`.githooks/`) 와 Layer 2 (pre-commit framework) 관계 명문 (병렬, 둘 다 활성화 의무)

**제약**: README 본문 line 1~85 (Phase 0~4 흐름) 변경 0건. 보강 line 추가 한정 (~10 줄 예상).

### 4.2 CONTRIBUTING.md 신규 작성

**위치**: `/CONTRIBUTING.md` (루트 신규)

**내용 후보**:
- dev onboarding workflow (clone → setup → 첫 commit)
- PC-1-T3 mandatory enforcement 명문 (`pre-commit install` 의무, 우회 = R-MVP1-1.5-PC1-1 trigger)
- `pre-commit run --all-files` local 검증 사용법
- bypass detection (`git commit --no-verify` 사용 시 CI 차단 안내)
- PR workflow (CI status check 의무, AR-3 별도 sub-cycle 답습)
- 합의 cycle 답습 (CLAUDE.md §3 + 단계별 합의 cycle 6단계)

**제약**: 다른 문서 본문 참조 한정 (cross-reference 만, 본문 verbatim 인용 0건 의무).

### 4.3 onboarding 스크립트 신규 (사용자 결정 항목)

**위치 후보**:
- `bin/setup.sh` (별도 bin/ 디렉토리)
- `Makefile` (루트, `make setup` target)
- 둘 다 (Makefile 이 bin/setup.sh 호출)

**내용**:
```bash
# (예시 — bin/setup.sh)
#!/bin/bash
set -e
echo "=== AI Development Tool — dev 환경 setup ==="

# Step 1: Layer 3 (.githooks/) 활성화
bash .githooks/setup.sh

# Step 2: dev 의존성 설치
pip install -r requirements-dev.txt

# Step 3: pre-commit framework 의무화 (PC-1-T3)
pre-commit install
echo "[OK] pre-commit framework 활성화됨 (PC-1-T3 mandatory enforcement)"

# Step 4: install audit log (R-6 (iii) 답습)
mkdir -p .git/pre-commit-audit
date -Iseconds > .git/pre-commit-audit/install.log
echo "[OK] install audit log 기록됨"

echo "=== setup 완료 ==="
```

**제약**: 외부 의존성 0건 (pip + git + bash 만), Provider Liquidity 답습.

### 4.4 enforcement audit log 메커니즘 (R-6 (iii) 흡수)

**후보**:
| 후보 | 위치 | 내용 |
|---|---|---|
| **(i)** `.git/pre-commit-audit/install.log` | git-internal (gitignore 됨) | `pre-commit install` 실행 시점 ISO timestamp 기록 |
| **(ii)** `.pre-commit-audit.log` | 루트 (gitignore 의무) | 동일 |
| **(iii)** git hook 자체 logging | `.git/hooks/pre-commit` (pre-commit framework 가 자동 생성) | 매 hook 실행 시점 기록 (volume 큼) |

→ **권고 = (i)** (간단 + git-internal, 별도 gitignore 불필요)

### 4.5 bypass detection 메커니즘 (R-6 (i)(ii) 흡수)

**탐지 경로 3 (R-6 답습)**:
- **(i) hook marker grep**: `.git/hooks/pre-commit` 내부에 `pre-commit framework` 자동 생성 marker 검출 (`grep -q "pre-commit" .git/hooks/pre-commit`)
- **(ii) `pre-commit run --all-files` CI 비교**: CI step 이 항상 `pre-commit run --all-files` 실행 → 만약 dev 환경에서 install 안 했다면 PR 의 신규 commit 이 framework hook 우회 → CI 에서 fail → bypass 탐지 발효
- **(iii) setup audit log**: §4.4 답습 (`.git/pre-commit-audit/install.log` 존재 여부 = install 실행 여부 증명)

**후보 (실 구현 형태)**:
| 후보 | 위치 | 내용 |
|---|---|---|
| **(A)** `tools/pre_commit_install_audit.sh` | 별도 스크립트 | 3 탐지 경로 통합 verify, CI nightly run |
| **(B)** README + CONTRIBUTING 명문 한정 | 문서 한정 | 자동 탐지 0건, manual 의무 (사용자 자율) |
| **(C)** `.githooks/post-commit` 추가 | `.githooks/` 영역 | 매 commit 후 §4.4 audit log update — 단, `.githooks/post-commit` 신규 추가 = `.githooks/` 본문 변경 영역 (§1.2 #2 위반 검토 필요) |

→ **권고 = (A)** (자동 탐지 + CI 통합, manual 의무 0건). 단, 본 sub-cycle scope = 스크립트 신규 작성 한정 (CI workflow 본문 변경 0건 의무 답습, CI 통합 = 별도 sub-cycle 또는 PC-1 sub-cycle 확장 결정).

---

## §5 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (PC-1-T3 본 sub-cycle 한정)

| 조건 | 본 sub-cycle 충족 |
|---|---|
| **(a)** 사용자 명시 결정 | ⏳ 본 brief 사용자 승인 + 합의 형태 결정 + setup 스크립트 형식 결정 + audit log 후보 결정 + bypass detection 후보 결정 시 충족 |
| **(b)** 격리 환경 PoC 실증 | ⏳ 본 sub-cycle 발효 시 `pre-commit install` + `pre-commit run --all-files` local 격리 verify + audit log 기록 evidence |
| **(c)** 도구/리소스 stateless · network-free | ✅ pre-commit framework 자체 stateless (local hook 실행), Provider Liquidity 답습 (`repos: local` 만) |
| **(d)** 자동 회귀 검증 경로 | ⏳ 본 sub-cycle 발효 시 audit log 기록 + bypass detection 스크립트 (§4.5 (A)) 발효 |
| **(e)** 합의 APPROVE 운영조건 | ⏳ 본 brief 합의 (단축 합의 + 사용자 명시 권고) APPROVE 시 발효 |

→ **현 시점 충족 = (c) 만** → 본 sub-cycle 합의 발효 = (a)~(e) 5/5 충족 (PC-1-T3 영역 한정)

---

## §6 Rollback Trigger (본 sub-cycle 적용 형태)

| ID | trigger | 본 sub-cycle 발효 형태 |
|---|---|---|
| **R-MVP1-1.5-PC1-1** | `pre-commit install` 미실행 commit 발견 | §4.5 bypass detection 메커니즘 (3 탐지 경로) 발효 시 자동 검출 → 단축 합의 + 사용자 명시 재검토 |
| **R-MVP1-1.5-PC1-2** | `.pre-commit-config.yaml` 본문 변경 — 차등 (R-7(b) 답습): (i) 신규 hook = Tier-2/3 catalog / provider policy / security gate / (ii) 단순 version pin / hook config update | (i) 풀 3+1 + 외부 LLM 1+ / (ii) 단축 합의 + 사용자 명시 |
| **R-MVP1-1.5-PC1-3** | branch protection rule 통합 차단 (AR-3 발효 차단) | AR-3 sub-cycle 영역, 본 sub-cycle 발효 후 AR-3 sub-cycle 진입 의무 |

---

## §7 Evidence

| Evidence | 형식 | 본 sub-cycle 발효 |
|---|---|---|
| **(a) Markdown report** | `docs/phase0/g2-gp3-mvp1-evidence.md` + `docs/phase0/g2-gp5-mvp1-evidence.md` 보강 (PC-1-T3 영역 추가) | 별도 sub-cycle 또는 본 sub-cycle 확장 결정 |
| **(b) PoC 실증** | `pre-commit install` 실행 + `pre-commit run --all-files` local 결과 + audit log 기록 evidence | 본 sub-cycle 실 구현 단계 발효 |
| **(c) Docker isolation log** | pre-commit hook 격리 (stateless) 답습 | (c) 답습 발효 자격 |
| **(d) GitHub Actions run** | (별도 sub-cycle) pre-commit CI step 통합 run id | 본 sub-cycle scope 외 (CI workflow 본문 변경 0건 의무) |
| **(e) 합의 보고서** | 본 sub-cycle 합의 보고서 (단축 합의 권고) | 본 brief 합의 발효 |

---

## §8 사용자 결정 항목 (brief 합의 진입 전 의무)

| # | 항목 | 후보 | 권고 |
|---|---|---|---|
| **D-1** | 합의 형태 | (i) 단축 합의 (Reviewer-only) / (ii) 풀 3+1 / (iii) 풀 3+1 + 외부 LLM 1+ | **(i) 단축 합의 (Reviewer-only)** — entry brief line 292 답습 + entry cycle 에서 T3 결정 자체 완료, 본 sub-cycle = 결정 *집행*, 메모리 "Ceremony 인플레이션 차단" 답습 |
| **D-2** | onboarding 스크립트 형식 | (i) `bin/setup.sh` / (ii) `Makefile` (`make setup`) / (iii) 둘 다 (Makefile 이 bin/setup.sh 호출) | **(i) `bin/setup.sh`** — bash 단순, 외부 의존성 0, CLAUDE.md 답습 (`docs/architecture/environment-and-docker-design.md` 하드코딩 금지 답습, Makefile = make 의존 추가) |
| **D-3** | enforcement audit log 위치 | (i) `.git/pre-commit-audit/install.log` (git-internal) / (ii) `.pre-commit-audit.log` (루트) / (iii) git hook 자체 logging | **(i) `.git/pre-commit-audit/install.log`** — 간단 + git-internal (별도 gitignore 불필요) |
| **D-4** | bypass detection 메커니즘 | (A) `tools/pre_commit_install_audit.sh` (자동, CI 통합) / (B) README + CONTRIBUTING 명문 한정 (manual) / (C) `.githooks/post-commit` (`.githooks/` 본문 변경 영역) | **(A) `tools/pre_commit_install_audit.sh` 자동** — 단, CI workflow 통합 = 별도 sub-cycle 또는 본 sub-cycle 확장 (사용자 결정) |
| **D-5** | `.githooks/` vs `.pre-commit-config.yaml` 관계 | (α) 병렬 유지 / (β) framework 흡수 / (γ) `.githooks/` 폐지 | **(α) 병렬 유지** — 본 sub-cycle scope 안, §1.2 #2 답습 |
| **D-6** | bypass detection CI 통합 (D-4 (A) 채택 시) | (i) 본 sub-cycle 확장 (CI workflow step 추가) / (ii) 별도 sub-cycle | **(ii) 별도 sub-cycle** — CI workflow 본문 변경 0건 의무 답습 (§1.2 #5), 본 sub-cycle 종결 후 별도 단축 합의 |

---

## §9 합의 형태 권고 + 다음 단계

### 9.1 합의 형태 권고

**단축 합의 (Reviewer-only)** 권고 — 근거:

| 근거 | 내용 |
|---|---|
| **entry brief line 292** | "단축 합의 + 사용자 명시 (README + CONTRIBUTING.md + onboarding 스크립트 답습 1회)" |
| **entry cycle 완료** | T3 채택 결정 자체는 24번째 entry cycle (`9638521`) 에서 APPROVE WITH CONDITIONS 완료. 본 sub-cycle = 결정 *집행* |
| **변경 0건 의무** | `.pre-commit-config.yaml` / src / tools / CI workflow / branch protection 본문 모두 0건. 변경 = README + CONTRIBUTING + onboarding + audit log + bypass detection 메커니즘 한정 |
| **풀 3+1 승격 trigger** | 5/5 모두 발화 0건 (① 새 권위 결정 0 / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0) |
| **메모리 답습** | "Ceremony 인플레이션 차단" — 1-agent 직접 / Reviewer-only 단축 합의 영역 |

### 9.2 다음 단계 (단계별 합의 cycle 6단계 답습)

1. ✅ **brief 작성** (본 단계, 본 commit)
2. ⏳ **사용자 승인** — §8 결정 항목 D-1~D-6 사용자 결정 의무
3. ⏳ **단축 합의** — Reviewer-only 합의 보고서 작성 (5/5 풀 3+1 승격 trigger 발화 검증)
4. ⏳ **실 구현** — §4 5 항목 file 생성/수정
5. ⏳ **commit** — 본 sub-cycle 정리 commit (SESSION + INDEX + 본 commit)
6. ⏳ **push** — 사용자 명시 의무 답습

---

## §10 본 brief 자기진단 (8/8 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 본 brief 자체 실 코드 변경 0건 | ✅ brief 작성 한정 |
| 2 | `.pre-commit-config.yaml` 본문 변경 0건 | ✅ 본문 0건, 명문 답습 한정 |
| 3 | `.githooks/pre-commit` 본문 변경 0건 | ✅ Layer 3 답습 유지 |
| 4 | src / tools / CI workflow 본문 변경 0건 | ✅ 변경 영역 = README + CONTRIBUTING + onboarding + audit + bypass 한정 |
| 5 | ADR / 헌법 / roadmap 본문 변경 0건 | ✅ cross-reference 한정 |
| 6 | branch protection rule 변경 0건 (AR-3 sub-cycle 영역) | ✅ AR-3 별도 sub-cycle 답습 |
| 7 | 24번째 entry BLOCKING R-2 / R-6 / R-7(b) 흡수 + N-1 / N-2 권고 흡수 | ✅ §2 매트릭스 답습 |
| 8 | 사용자 결정 항목 명시 (D-1~D-6) + 합의 형태 권고 명시 | ✅ §8 + §9.1 답습 |

---

> **본 brief 발효 시점** = 사용자 승인 (§8 D-1~D-6 결정) + Reviewer-only 단축 합의 APPROVE (§9.1 권고 답습) + 본 brief commit. 본 brief 자체 = **실 구현 단계 진입 권한 발효 자격** 한정 (실 file 생성/수정 = 별도 단계).
