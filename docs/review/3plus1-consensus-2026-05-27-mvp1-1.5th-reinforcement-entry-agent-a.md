# Agent A (구현 분석가) — MVP-1 1.5차 보강 진입 합의 분석

> **합의 cycle**: MVP-1 1.5차 보강 4 sub-수단 (S-3 + ST-2 + PC-1 + AR-3) 진입 합의 (풀 3+1 + 외부 LLM 1+ 답습)
>
> **본 분석 자격**: entry brief 입력 분석 한정. 4 sub-수단 *채택 결정 발효* 또는 실 구현 / CI / hook / config / branch protection 본문 변경 0건. 본 cycle 발효 자격은 Reviewer 통합 영역.
>
> **본 Agent A 관점**: "실제로 동작하는가?" — 기술적 구현 가능성, 의존성, 성능, 실 구현 자격
>
> **답습 자료** (직접 read 검증 완료):
> - `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` v1 (507줄)
> - `docs/external-review/2026-05-27-mvp1-1.5th-reinforcement-codex-response.md` (270줄, vendor=OpenAI, 판정=REVISE AS ENTRY BRIEF INPUT)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 / §2.3 / §2.4
> - `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.2 / §3.3 / §3.6.3 / §4.3 / §4.4 / §4.6 / §4.7.3 + line 281 (5조건 패턴 출처)
> - `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (audit 결과)
> - `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (APPROVE AS BRIEF + ST-2 단독 우선 권고)
> - `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` (APPROVE Keep Deferred + AR-3 Backlog #3 이관)
> - `tools/secret_scanner.py` (368줄, 실 구현) / `tools/docker_secret_inotify_sidecar_check.sh` (258줄, 실 구현) / `.pre-commit-config.yaml` (110줄, opt-in 답습 명시 line 18~22)
> - `.github/workflows/secret-hygiene-egress-redaction.yml` (workflow name = "G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction", job/step 다수)

---

## 0. Executive Summary

**판정: APPROVE WITH CONDITIONS (BLOCKING 4 + 권고 5)**

본 brief 는 4 sub-수단 모두를 풀 3+1 + 외부 LLM 1+ 합의 input 으로 올리는 구조와 진입 자격 framing 면에서 *대체로 정당*하다. 단, *실제로 동작하는가?* 관점에서 다음 4개 항목이 BLOCKING — 본 brief v1.1 로의 흡수 (또는 Reviewer 통합 시점 명시) 후 발효 의무.

핵심 finding 6개:
1. **ADR-011 §2.1 원문 = (a)~(d) 4조건** — brief §3 의 "ADR-011 §2.1 (a)~(e)" 표기는 원문과 불일치. repo 내 운영 패턴은 line 281 "(a)~(d) + 합의 APPROVE (e) 5조건 패턴" 으로 (e) 가 *운영 추가 조건* 임을 명시. codex finding #1 정확. **BLOCKING-1**.
2. **PC-1 의 (b) PoC 상태 표기 과대** — brief §3 (b) PC-1 row "✅ PC-4 T2 sub `78483c5` Partially Satisfied 답습" 은 *opt-in T2* 의 PoC. 본 cycle PC-1 = *의무화 T3 dev 환경 강제* — 의무화 PoC (onboarding/install enforcement/bypass detection) 미존재. codex finding #2 정확. 본 cycle (b) = **PC-1 미충족** 재분류 의무. **BLOCKING-2**.
3. **AR-3 required check mapping 추상도 과대** — brief §2.4.1 + §2.4.2 "11 workflow 모두 required status check" 는 GitHub branch protection rule 의 *실 mapping 형태* (workflow file명 ≠ job 이름 ≠ check name) 와 불일치. workflow `secret-hygiene-egress-redaction.yml` 자체는 32+ 개 step 보유 — required check 단위 = job 또는 step 또는 workflow run conclusion. codex finding #3 정확. **BLOCKING-3**.
4. **R-MVP1-1.5-PC1-1 "미실행 commit 발견" 의 탐지 경로 명시 의무** — trigger 발화 *검출 메커니즘* 미명시. codex §4.4 답습 — 탐지 후보 = (i) hook marker file commit + (ii) CI step 이 commit 별 hook 실행 흔적 검사 + (iii) `pre-commit run --all-files` ↔ commit 별 hook 비교 audit. 본 cycle 발효 시 *탐지 경로 후보* 본문 채택 의무. **BLOCKING-4**.
5. **PC-1 단독 보안 효과 ≈ 0** — `pre-commit install` 은 로컬 dev 가 임의로 우회 가능 (`git commit --no-verify` / install 자체 미실행). PC-1 단독 의무화의 *실제 강제력* 은 CI/branch protection 결합 시에만 발생. codex §7.2 답습. brief 가 PC-1 + PC-3 + AR-3 결합 효과로 명시 의무. **권고-A**.
6. **ST-2 sidecar failure-mode 명시 의무** — inotify sidecar 가 secret file event 검출 → 메인 컨테이너 정지 signal 전달 메커니즘 (PID namespace / restart policy / healthcheck / docker-compose `depends_on: condition: service_healthy` 또는 healthcheck failure) 이 brief §2.2.1 "메인 컨테이너에 정지 signal 송출 (docker-compose dependency `restart: on-failure` 또는 healthcheck fail)" 정도로만 표현. *실제 동작* 자격 확보 위한 fail-closed 확인 형식 evidence 의무. codex §7.4 답습. **권고-B**.

---

## 1. 4 sub-수단 실제 구현 자격 (각각)

### 1.1 S-3 — detect-secrets 부분 통합 — **APPROVE**

구현 분석가 관점에서 S-3 는 *실제로 동작 가능* 하다 — 단 brief §2.1.2 의 2 조건 (plugin 명시 활성화 + baseline file 금지) 충실 강제 시 한정.

| 검증 항목 | 자격 |
|----------|------|
| **의존성 확보** | `pip install detect-secrets` = Python ecosystem 내. 본 repo 의 Python 환경 (`secret_scanner.py` 와 동일 runtime) 정합 |
| **plugin 활성화 hardcoded list** | brief 권고 = Tier-1 답습 plugin (AWS / Generic / Base64). 단, *detect-secrets CLI 의 실제 plugin identifier* 와 정확 일치 의무 — `AWSKeyDetector` / `Base64HighEntropyString` / `HexHighEntropyString` 등 (codex §7.5 답습) |
| **workflow step 통합** | `.github/workflows/secret-hygiene-egress-redaction.yml` 의 32+ step 답습 위 추가 step 1개. step 위치 = S-1 (line 251 `MVP-1 entry — secret_scanner coverage check`) 후속 |
| **S-1 답습 유지** | brief §2.1.2 + R-MVP1-1.5-S3-3 영구 금지 명문 — Defense in depth 자격 충실 |
| **baseline file 금지 자격 검증 자동화** | CI step assertion = `grep -L "\-\-baseline" .github/workflows/*.yml` 또는 workflow 본문에 `--baseline` 미존재 assert. codex §7.5 답습 권고 |
| **Tier-1 catalog testfile evidence** | Group D PoC §2.1 (D) 답습 fixture (`pass/` + `fail/`) 형식 답습. 본 cycle 합의 발효 후 별도 sub-cycle 의 evidence 산출 가능 |

→ **(b)(d) 미충족 → 실 구현 sub-cycle 의무** (brief §3 매트릭스 ⏳ 정확 표기). (a)(c) 충족. 본 cycle (e) 발효 시 진입 자격 발효.

### 1.2 ST-2 — inotify sidecar — **APPROVE WITH REVISION**

구현 자격 우수 — `tools/docker_secret_inotify_sidecar_check.sh` (258줄) 가 *이미* 실 구현 답습 (audit brief §2.1 확정). 단, sidecar 운영 layer 의 *failure-mode* 명시 의무.

| 검증 항목 | 자격 |
|----------|------|
| **Hermes upstream 변경 불요** | brief §2.2.2 + roadmap §3.3.1 답습 — sidecar 분리 가능 ⇒ Hermes Dockerfile 변경 0건. **단, roadmap §3.6.3 line 290 "ST-1 / ST-2 / ST-5 진입 (Hermes upstream 변경)" framing 충돌** 은 brief §1.3 ST-2 row 가 "framing 미세 충돌 흡수" 로 인지함 — 인지 명확 |
| **inotify-tools 의존성** | sidecar image 한정 (Alpine `apk add inotify-tools` 또는 Debian `apt-get install inotify-tools`) — Hermes upstream image 미오염 |
| **mtime/perm event 인지 메커니즘** | `inotifywait -m -e modify,attrib /secrets/` 또는 동등 — `tools/docker_secret_inotify_sidecar_check.sh` 답습 |
| **메인 컨테이너 정지 signal 메커니즘** | brief §2.2.1 = "docker-compose dependency `restart: on-failure` 또는 healthcheck fail". **REVISION 의무**: 실제로 fail-closed 가 자격 확보되는지 = (i) sidecar 가 healthcheck fail → docker-compose 가 메인 컨테이너 정지 (PID namespace 공유 / `depends_on` chain) 또는 (ii) sidecar 가 signal 전송 (PID 공유 필요) 中 어느 메커니즘 채택 의무 명시. codex §7.4 답습 |
| **threshold (<1초)** | brief §2.2.2 답습 = 후보 한정 (R-MVP1-1.5-ST2-1) → 본 cycle 결정 0건 — 자격 충실 |

→ **(b)(d) 미충족** → 실 구현 sub-cycle 의무. **추가 REVISION**: brief §2.2.1 의 메인 fail-closed 메커니즘 본문 1줄 추가 (PID namespace 또는 healthcheck chain) 권고 — codex §7.4 흡수.

### 1.3 PC-1 — pre-commit framework 의무화 — **REVISE**

구현 자격 자체는 가능. 단, *실제 강제력* 의문 + brief §3 매트릭스의 (b) PoC 상태 표기 과대 = **재분류 의무**.

| 검증 항목 | 자격 |
|----------|------|
| **T2 sub (opt-in) 답습** | `.pre-commit-config.yaml` (110줄) line 17~22 = "opt-in 한정 local pre-commit framework (CI gating 보조)" + "pre-commit install 의무화 0건 (T3 영역, 사용자 명시 답습)" 명문 답습. PC-4 T2 sub `78483c5` Partially Satisfied 답습 정확 |
| **T3 (의무화) 자격** | README + CONTRIBUTING.md + `bin/setup.sh` 또는 `make setup` 본문 채택 — *문서 layer 강제*. **실제 강제력**: 로컬 dev 가 (i) setup 스크립트 미실행 + (ii) `git commit --no-verify` + (iii) `pre-commit uninstall` 中 어느 우회 가능 (codex §7.2 답습) |
| **CI/branch protection 결합 효과** | PC-1 단독 보안 효과 ≈ 0 (위 우회 가능성). PC-1 + PC-3 (CI step) + AR-3 (branch protection) 결합 시에만 *Defense in depth* 효과. brief §2.3.2 "branch protection rule 통합 — AR-3 와 *동시 진입* 효과" 명시는 정확 |
| **(b) PoC 상태** | brief §3 (b) PC-1 row "✅ PC-4 T2 sub `78483c5` Partially Satisfied 답습 + ... T3 sub = 본 cycle 발효 후 onboarding 스크립트 별도 sub-cycle" — **opt-in T2 PoC** 가 *의무화 T3 PoC* 가 아님. **재분류**: (b) PC-1 = **현 미충족** (⏳) 의무. codex §3.3 답습 |

→ **(b)(d) 재분류 + (a)(c) 유지 + (e) 본 cycle 발효 시점**. brief §3 매트릭스 (b) PC-1 row 의 "✅ ... 발효" 표현은 *T2 opt-in 발효* 한정 — *T3 의무화 발효 0건* 임을 표 본문에 명시 의무. **BLOCKING-2**.

### 1.4 AR-3 — 통합 PR auto-reject — **REVISE**

T3 영역 진입 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 = 합의 형태 자격 정확. 단, *required check mapping* 의 실 구현 자격이 추상 단위에서 명시됨 = 재구체화 의무.

| 검증 항목 | 자격 |
|----------|------|
| **AR-1 답습 유지 (11 workflow)** | `.github/workflows/` 11개 실 존재 (audit §2.2 답습) + brief §2.4.1 + §2.4.2 답습. 11 workflow 모두 fail-closed 동작은 이미 부분 발효 — 본 cycle = AR-2 통합 한정 |
| **branch protection rule mapping** | brief §2.4.2 "11 workflow 모두 required status check" 는 GitHub UI/API 의 *required status check* mapping 단위 (= job name 또는 check name) 와 단위 mismatch. 예: `secret-hygiene-egress-redaction.yml` workflow name = "G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction" — *required check 단위* 는 (i) workflow 1개 (workflow_run conclusion) 또는 (ii) job 1개 ("scan-and-verify" 등) 또는 (iii) step granularity. **REVISION 의무**: 본 cycle 합의 발효 시 *required check name* (workflow file명 ≠ job 이름) 명시 의무 = 별도 sub-cycle evidence 형식 본문 채택. codex §7.3 답습 |
| **admin bypass 0건** | brief §2.4.2 + §2.4.3 답습 = `Do not allow bypassing the above settings` + `Restrict who can push to matching branches` = 0 user. 자격 확보 가능 |
| **`main` + `develop` 두 branch** | GitHub branch protection rule pattern (e.g., `main`, `develop`, `release/*`) 적용 가능 영역. 자격 확보 가능 |
| **외부 LLM 응답 의무 답습** | roadmap §4.7.3 line 480 verbatim 답습 + codex 응답 1건 첨부 완료 (vendor=OpenAI, Anthropic Claude 와 cross-vendor 충족) |

→ **(b)(d) 미충족 + required check mapping 단위 재구체화 의무** → 실 구현 sub-cycle 의무. **BLOCKING-3**.

---

## 2. Rollback Trigger 12 본문 구현 자격 평가

본 §2 = brief §5.1 의 12 trigger 각각의 *발화 검출 메커니즘* + *발화 후 행동 자격* 평가.

| Trigger ID | sub-수단 | 발화 검출 메커니즘 자격 | 발화 후 행동 자격 | 판정 |
|-----------|---------|---------------------|----------------|------|
| **R-MVP1-1.5-S3-1** | S-3 | detect-secrets plugin 활성화 본문 변경 → CI diff 검출 ✅ | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 ✅ | APPROVE |
| **R-MVP1-1.5-S3-2** | S-3 | `--baseline` 옵션 본문 추가 → CI assertion grep ✅ | 영구 금지 (R-MVP1-G3-1 답습) ✅ | APPROVE |
| **R-MVP1-1.5-S3-3** | S-3 | `tools/secret_scanner.py` 삭제 또는 workflow step 제거 → CI diff 검출 ✅ | 영구 금지 (Defense in depth) ✅ | APPROVE |
| **R-MVP1-1.5-ST2-1** | ST-2 | inotify event 응답 시간 측정 — *문장 형식* "threshold 미달 (>1초)" 가 *고정처럼 보임*. 후보 한정 의무 답습 미흡 — codex §4.3 finding 정확 | 단축 합의 적격 ✅ | **REVISE**: "합의된 threshold 초과" 로 본문 수정 |
| **R-MVP1-1.5-ST2-2** | ST-2 | Hermes upstream Dockerfile 변경 PR diff 검출 ✅ | 풀 3+1 + Hermes upstream PR + 외부 LLM 1+ ✅ | APPROVE |
| **R-MVP1-1.5-ST2-3** | ST-2 | sidecar process 운영 부담 — *발화 형식 추상*. e.g., 메모리/CPU threshold 측정 / failure mode log audit / restart count threshold 中 어느 메커니즘? | Operational Readiness PASS (Layer E) 영역 진입 (Backlog #7) ✅ | **권고-C**: 발화 메커니즘 후보 본문 채택 |
| **R-MVP1-1.5-PC1-1** | PC-1 | "미실행 commit 발견" *탐지 경로 미명시* — codex §4.4 finding 정확. 탐지 후보: (i) hook marker file commit / (ii) CI 가 commit 별 hook 실행 흔적 audit / (iii) `pre-commit run --all-files` ↔ commit 별 hook 비교 | 단축 합의 + 사용자 명시 ✅ | **REVISE**: 탐지 경로 후보 본문 채택. **BLOCKING-4** |
| **R-MVP1-1.5-PC1-2** | PC-1 | `.pre-commit-config.yaml` 본문 변경 PR diff 검출 ✅ — 단 *모든* 변경이 풀 3+1 = 과함 (codex §4.4 답습). 분리 필요: (i) Tier-2/3 catalog / provider policy / security gate 변경 = 풀 3+1 / (ii) 단순 version pin = 단축 | 풀 3+1 (도구 변경 영향 분석) ⚠️ | **REVISE**: 변경 영역 분리 (catalog vs version pin) |
| **R-MVP1-1.5-PC1-3** | PC-1 | branch protection rule 통합 차단 — 시점 미명시 (= AR-3 발효 전 차단? 후 차단?). 명확화 의무 | 본 cycle 합의 재검토 (풀 3+1 + 외부 LLM 1+) ✅ | **권고-D**: 발화 시점 명문 |
| **R-MVP1-1.5-AR3-1** | AR-3 | branch protection rule API/UI 변경 PR diff / GitHub API audit log ✅ | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (T3 영역) ✅ | APPROVE |
| **R-MVP1-1.5-AR3-2** | AR-3 | "11 workflow 본문 변경" + "신규 status check 추가" 가 *동일 trigger 한 row* 에 묶임 — 분리 의무 (codex §4.5 답습). workflow 본문 변경 ≠ status check 변경 | 풀 3+1 (도구 변경 영향 분석) ⚠️ | **REVISE**: trigger 분리 (workflow 본문 / status check 정의) |
| **R-MVP1-1.5-AR3-3** | AR-3 | "FP" 판정 기준 미명시 — 어느 단위에서 FP? (i) 단일 PR / (ii) week-over-week rate / (iii) escalation 횟수 中? | 단축 합의 + 사용자 명시 ✅ | **권고-E**: FP 판정 기준 후보 본문 |

→ **12 trigger 中 7 APPROVE / 5 REVISE 또는 권고**. REVISE 5건 = ST2-1 / PC1-1 (BLOCKING-4) / PC1-2 / AR3-2 + 권고 4건 = ST2-3 / PC1-3 / AR3-3 + 본 cycle 합의 발효 시 본문 흡수 의무.

---

## 3. 의존성 매트릭스 (4 sub-수단 + 외부 의존)

### 3.1 4 sub-수단 내부 결합 의존성

| | S-3 | ST-2 | PC-1 | AR-3 |
|---|---|---|---|---|
| **S-3** | — | 독립 | 약 (`.pre-commit-config.yaml` 에 S-3 hook 추가 시) | 약 (S-3 workflow step 이 required check 后보) |
| **ST-2** | 독립 | — | 독립 | 약 (`docker_secret_inotify_sidecar_check.sh` nightly 가 required check 후보) |
| **PC-1** | 약 | 독립 | — | **강** — PC-1 단독 보안 효과 ≈ 0, AR-3 결합 시 강제력 발생 (codex §7.2 답습) |
| **AR-3** | 약 | 약 | **강** | — |

→ **PC-1 ↔ AR-3 결합 = 핵심 의존**. PC-1 단독 진입 시 *실제 강제력* 의문 — 본 cycle 4 sub-수단 *bundle* 진입의 합리성 정당화. codex §7.2 답습.

### 3.2 4 sub-수단 외부 의존성

| 외부 의존 | sub-수단 | 자격 |
|----------|---------|------|
| **Hermes upstream Dockerfile** | ST-2 | ❌ 의존 0건 (sidecar 분리 가능 답습) |
| **`src/adapters/llm/facade.py` real** | 4 sub-수단 모두 | ❌ 의존 0건 (G5-4 TR-1 별도 trajectory) |
| **Backlog #3 전체** | AR-3 | ⚠️ *일부* — AR-3 단독 시점 변경 외 다른 Backlog #3 항목 (ST-4 Vault HSM / commit signing / Tier-2/3 catalog) = 영역 외 (brief §6.2 #4 답습) |
| **Operational Readiness PASS (Layer E)** | ST-2 (R-MVP1-1.5-ST2-3 발화 시) | ❌ 본 cycle 의존 0건 (trigger 발화 시점에만 진입) |
| **외부 LLM 응답 1+** | 4 sub-수단 모두 | ✅ 충족 (codex 응답 270줄, OpenAI vendor, cross-vendor blind risk 차단) |
| **Python ecosystem (`pip install detect-secrets`)** | S-3 | ✅ 의존 확보 (audit `secret_scanner.py` 동일 runtime) |
| **inotify-tools binary** | ST-2 | ✅ 의존 확보 (sidecar image 한정, Linux 환경) |
| **GitHub branch protection API** | AR-3 | ✅ 의존 확보 (GitHub Plan 답습 — BI-4 영역) |
| **README + CONTRIBUTING.md + setup 스크립트** | PC-1 | ✅ 의존 확보 (별도 sub-cycle 본문 작성 영역) |

→ **모든 외부 의존 확보 가능**. 단, GitHub branch protection API = BI-4 GitHub Plan ruleset availability 답습 — Plan 자격 검증 필요 (별도 brief `bi-4-github-plan-ruleset-availability-brief.md` 영역 답습 의무).

---

## 4. 성능 / 운영 부담 risk

| sub-수단 | risk | 평가 |
|---------|------|------|
| **S-3** | CI step 시간 증가 | detect-secrets 단일 scan = 일반적으로 수~수십 초 (plugin 수에 비례). brief 의 Tier-1 답습 plugin 3개 (AWS / Generic / Base64) 한정 시 < 30초 자격 (별도 측정 의무 = 실 구현 sub-cycle). 본 workflow `secret-hygiene-egress-redaction.yml` 의 기존 32+ step 합산에 단일 step 추가 = 운영 부담 미미 |
| **ST-2** | sidecar process 운영 부담 (메모리 / CPU) | inotify watch process = 일반적으로 < 10 MB 메모리 + < 1% CPU. 운영 부담 ≈ 0. 단, R-MVP1-1.5-ST2-3 = 운영 부담 / failure mode 발견 trigger 답습 — 실 측정 evidence 의무 |
| **PC-1** | dev 환경 강제 onboarding 부담 | `pre-commit install` + setup script 1회 실행 = 부담 < 1분. 단, *우회 가능성* 차단 (= CI/branch protection 결합) 이 본질 부담. 우회 발견 시 CI feedback loop 지연 |
| **AR-3** | PR feedback loop 지연 | branch protection rule status check = 11 workflow 모두 의무 시 PR 전체 run 시간 ≈ 5-15분 (workflow 별 차이). developer experience 영향. 단, 본 답습 = AR-1 부분 발효 상태 위 AR-2 추가 한정 = 시간 증분 ≈ 0 (AR-1 이 이미 통과 의무) |

→ **모든 risk 수용 가능**. ST-2 와 AR-3 의 실 측정 evidence 의무 (별도 sub-cycle).

---

## 5. codex finding 흡수 자격

| codex finding | 본 Agent A 흡수 의견 |
|--------------|--------------------|
| **§0 / §3.1 필수 #1: ADR-011 §2.1 (a)~(e) 표기 정정** | **흡수 의무 (BLOCKING-1)**. 원문 = (a)~(d) 4조건. repo 내 line 281 + 290 답습 = "(a)~(d) + 합의 APPROVE (e) 5조건 패턴". brief §3 매트릭스 제목 + §1.3 + §10 자기진단 항목 6 모두 동일 흡수 의무. |
| **§3.3 필수 #2: PC-1 (b) 미충족 재분류** | **흡수 의무 (BLOCKING-2)**. T2 opt-in PoC ≠ T3 의무화 PoC. brief §3 매트릭스 (b) PC-1 row "✅ ... 발효" 표현 = "⏳ T3 의무화 PoC 미충족, 본 cycle 발효 후 별도 sub-cycle" 로 재분류. |
| **§7.3 / §0 필수 #3: AR-3 required check mapping 구체화** | **흡수 의무 (BLOCKING-3)**. workflow file명 → check name (job 또는 step 또는 workflow_run conclusion) mapping 단위 명시. brief §2.4.1 + §2.4.2 + §5.2 (d) AR-3 row "branch protection rule status check actual run id" → "required check (job name 단위) actual run id + check name mapping" 로 구체화. |
| **§2.1 권고 ST-2 framing**: roadmap §3.6.3 line 290 ST-2 묶음 framing 충돌 | **흡수 부분**. brief §1.3 ST-2 row 가 *이미* "framing 미세 충돌 흡수" 로 인지함. 추가 흡수 = roadmap §3.6.3 line 290 본문 분리 (ST-2 = "Hermes upstream 변경 불요" / ST-1 + ST-5 = "Hermes upstream 변경") 권고 = 별도 commit 영역 (cross-reference 갱신, brief §9.5 답습) |
| **§2.2 권고 PC-1 명칭**: "PC-1-T3 mandatory enforcement" | **흡수 의무 (권고-F)**. T2 도입 (line 479) ↔ T3 의무화 혼용 차단 명문. brief §1.3 PC-1 row + §2.3 + §5 trigger 모두 "PC-1-T3 mandatory enforcement" 또는 동등 prefix 일관 사용 권고 |
| **§2.3 권고 AR-3 일관성**: "AR-3 만 선차 변경" 반복 | **흡수 의무 (권고-G)**. brief §1.3 AR-3 row + §2.4.4 + §6.2 #4 모두 명시는 있으나, *AR-3 실 구현 sub-cycle* 시점 branch protection rule 본문에 Backlog #3 의 다른 항목 (signed commit / linear history 등) 미혼입 boundary 명문 권고 |
| **§7.2 권고 PC-1 + PC-3 + AR-3 결합 효과** | **흡수 의무 (권고-A)**. brief §2.3 + §3 매트릭스 (a) PC-1 row 에 "PC-1 단독 보안 효과 < PC-1 + PC-3 + AR-3 결합 효과" 명문 권고 |
| **§7.4 권고 ST-2 failure mode evidence** | **흡수 의무 (권고-B)**. brief §2.2.1 + §5.2 (d) ST-2 row 에 "event 감지" + *추가* "메인 workload fail-closed 확인" evidence 형식 명문 |
| **§7.5 권고 S-3 plugin allowlist 정확 이름** | **흡수 의무 (권고-H)**. brief §2.1.2 + §2.1.3 + §5.1 S3-1 의 "AWS / Generic / Base64" → "detect-secrets CLI 인식 정확 plugin identifier" (e.g., `AWSKeyDetector` / `Base64HighEntropyString`) + `--baseline` 미사용 CI assertion 권고 |
| **§5.1 우회 가능 영역**: "단축 합의" 반복의 검증 약화 risk | **흡수 의무 (권고-I)**. brief §4.2 + §8.1 의 "단축 합의 + 사용자 명시" 표현에 *조건* 추가 — "단축 합의 적격 조건 = (b)(d) evidence 충실. evidence 미충족 시 자동 풀 3+1 승격" 명문 |
| **§5.2 우회 보강**: AR-3 = repo 운영 정책 변경 ≠ 코드 변경 | **흡수 의무 (권고-J)**. brief §6.2 의 "branch protection 변경은 구현 sub-cycle 사용자 명시 + evidence 전까지 0건" 의무 추가 |

→ **codex 3 필수 모두 흡수 = BLOCKING 3건** (§0 / §3.3 / §7.3). 5 권고 中 권고-A/B/F/G/H 5건 = 본 Agent A 동의 흡수 의무. 권고-I/J = brief 운영 일관성 강화 영역 (Reviewer 통합 영역).

---

## 6. ADR-011 §2.1 (a)~(d) + 합의 APPROVE (e) 매트릭스 평가

본 §6 = brief §3 매트릭스의 *구현 자격* 평가. (a)(c) = 충족 / (b)(d) = 실 구현 sub-cycle 의무 / (e) = 본 cycle 발효 시점.

| 조건 | S-3 | ST-2 | PC-1 | AR-3 |
|------|-----|------|------|------|
| **(a) 동등 이상 보안** | ✅ 단 plugin 명시 + baseline 금지 조건 강제 시 | ✅ ST-3 위 런타임 지속 보강 | ✅ 단 PC-3 + AR-3 결합 시 (단독 ≈ 0) | ✅ AR-1 fail-closed 위 branch protection 강제 |
| **(b) 격리 환경 PoC** | ⏳ detect-secrets 설치 + plugin list + baseline 미사용 + fixture evidence 의무 | ⏳ `tools/docker_secret_inotify_sidecar_check.sh` 답습 + docker-compose sidecar 통합 PoC 의무 | ⏳ **재분류**: T2 opt-in PoC ≠ T3 mandatory PoC. onboarding / install enforcement / bypass detection evidence 의무 | ⏳ GitHub branch protection rule 시뮬레이션 또는 actual evidence 의무 |
| **(c) ADR / SDD 권위** | ✅ roadmap §3.2 / §3.6.3 + Group D + ADR-011 | ✅ ADR-008 §A.2 R1-2 + roadmap §3.3 + backlog1 | ✅ roadmap §4.3 / §4.7.3 + ADR-011 §2.4 | ✅ roadmap §4.4 / §4.7.3 + backlog2 |
| **(d) 자동 회귀 검증 경로** | ⏳ workflow step 통합 + nightly + no-baseline assertion 의무 | ⏳ sidecar nightly run + event detection assertion 의무 | ⏳ pre-commit CI step + install enforcement audit 의무 | ⏳ required check 실 mapping evidence (workflow file ≠ check name) 의무 |
| **(e) 합의 APPROVE** | ⏳ 본 cycle 발효 시점 | ⏳ 본 cycle 발효 시점 | ⏳ 본 cycle 발효 시점 | ⏳ 본 cycle 발효 시점 |

→ **(a)(c) = 4/4 / (b) = 0/4 (PC-1 재분류 후) / (d) = 0/4 / (e) = 본 cycle 발효 시 4/4** → 본 cycle 합의 발효 자격 = (e) + (a)(c) 충족 → 실 구현 sub-cycle 4개 = (b)(d) 충족 의무. brief §3 매트릭스 본문은 (b) PC-1 row 재분류 후 정확.

→ **Implementation Evidence PASS 발효** = (a)~(e) 5/5 + conditions C-1~C-4 해소 + 사용자 명시 별도 합의. 본 cycle 영역 외 — brief §0.3 #11 + §8.1 충실.

---

## 7. 본 brief §6 금지 사항 + §7.3 자격 검증 기준 cross-check

### 7.1 §6.1 20 항목 본 brief 자체 금지

본 brief 작성 시점 실 코드 / CI / hook / branch protection / `.pre-commit-config.yaml` 본문 변경 0건 자기진단 = 충실. 검증: working directory `tools/` + `.github/workflows/` + `.pre-commit-config.yaml` 모두 unchanged (audit `wc -l` 답습 = 110/368/258 모두 5월 10~14일 자 답습). ✅ 통과.

### 7.2 §6.2 8 항목 발효 후 의무

§5.1 codex finding 우회 가능 영역 답습 — *권고-I* + *권고-J* 흡수 권고 (위 §5 참조).

### 7.3 §7.3 외부 LLM 응답 자격 검증 7 기준

codex 응답 (270줄) 자격 검증:
| # | 기준 | 충족 |
|---|------|------|
| 1 | 4 sub-수단 입장 (APPROVE / REVISE / REJECT) 명시 | ✅ §1 표 명시 |
| 2 | §1.3 선차 변경 매트릭스 명시 입장 | ✅ §2 별도 절 명시 |
| 3 | ADR-011 §2.1 (a)~(e) 매트릭스 충족 평가 | ✅ §3 별도 절 명시 + 형식 정정 권고 |
| 4 | Rollback Trigger 12 본문 완전성 평가 | ✅ §4 별도 절 명시 |
| 5 | §6 금지 + §7.3 자격 검증 cross-check | ✅ §5 별도 절 명시 |
| 6 | cross-vendor blind risk 차단 (vendor 상이) | ✅ §6 명시 — OpenAI vs Anthropic Claude |
| 7 | 추가 위험 / 누락 영역 (권고) | ✅ §7 별도 절 5개 명시 |

→ codex 응답 = 7/7 충족 + 외부 LLM 응답 부재 시 본 cycle 합의 진입 자격 0건 (§7.3 verbatim) 답습 충실.

---

## 8. 의존성 / risk integrated summary

본 §8 = 위 §3 + §4 + §5 통합 결과 본 cycle 합의 input 자격 종합.

| 영역 | 자격 |
|------|------|
| **brief framing 자격** | ✅ 4 sub-수단 모두 *진입 자격 분석* 형식 충실 (수단 결정 0건 / threshold 고정 0건 / 실 구현 0건) |
| **선차 변경 매트릭스 (§1.3)** | ✅ 4 sub-수단 모두 선행 권위 vs 본 cycle 차이 명문 — S-3 일치 / ST-2 권위 상승 / PC-1 권위 상승 / AR-3 시점 선차 변경 |
| **ADR-011 표기 정확성** | ⛔ (a)~(e) → (a)~(d) + 합의 APPROVE (e) 운영조건 정정 의무 (BLOCKING-1) |
| **PC-1 (b) 상태 표기** | ⛔ T2 opt-in → T3 의무화 재분류 의무 (BLOCKING-2) |
| **AR-3 required check mapping** | ⛔ workflow file명 → check name 단위 재구체화 의무 (BLOCKING-3) |
| **R-MVP1-1.5-PC1-1 탐지 경로** | ⛔ 탐지 메커니즘 후보 본문 채택 의무 (BLOCKING-4) |
| **Rollback Trigger 본문 완전성** | ⚠️ 5건 REVISE 또는 권고 (ST2-1 / PC1-1 / PC1-2 / AR3-2 + ST2-3/PC1-3/AR3-3 권고) |
| **codex 흡수 자격** | ✅ 3 필수 흡수 + 5 권고 中 5건 동의 흡수 의무 (권고-A/B/F/G/H) |
| **합의 형태 자격** | ✅ 풀 3+1 + 외부 LLM 1+ + 사용자 명시 — carry-over + roadmap §3.6.3 + §4.7.3 + ADR-011 §2.4 + CLAUDE.md §3 모두 답습 충실 |
| **금지 사항 자격 (§6.1 + §6.2)** | ✅ 20 + 8 항목 모두 명시 + 본 brief 작성 시점 위반 0건 자기진단 통과 |
| **외부 LLM 응답 자격** | ✅ codex 270줄, vendor=OpenAI, §7.3 7/7 기준 충족 |
| **실 구현 sub-cycle 4개 진입 권한 발효 자격** | ✅ 본 cycle 합의 APPROVE 시 = (b)(d) 충족 의무 + 사용자 명시 시점 별도 합의 영역 |

---

## 9. 최종 판정

### 9.1 판정 = **APPROVE WITH CONDITIONS (BLOCKING 4 + 권고 5)**

본 brief 는 풀 3+1 + 외부 LLM 1+ 합의 input 으로 사용할 수 있는 *큰 구조* 를 갖췄다. 단, 4 BLOCKING + 5 권고 흡수 후 발효 자격 충실 — *그대로 APPROVE* 보다 *REVISE BEFORE APPROVE* 권고. (codex 응답과 일치 — REVISE AS ENTRY BRIEF INPUT)

### 9.2 BLOCKING 4건

| # | 항목 | 흡수 형태 |
|---|------|---------|
| **BLOCKING-1** | ADR-011 §2.1 표기 정정 — "§2.1 (a)~(e)" → "§2.1 (a)~(d) + 합의 APPROVE (e) 운영조건" (또는 "ADR-011 기반 5조건 매트릭스") | brief §3 매트릭스 제목 + §1.3 + §10 항목 6 모두 정정 |
| **BLOCKING-2** | PC-1 (b) 매트릭스 row 재분류 — "✅ PC-4 T2 sub Partially Satisfied 답습 ... 발효" → "⏳ T3 mandatory PoC 미충족, 본 cycle 발효 후 별도 sub-cycle" | brief §3 매트릭스 (b) PC-1 row 본문 정정 |
| **BLOCKING-3** | AR-3 required check mapping 단위 재구체화 — "11 workflow 모두 required" → "11 workflow 각 *check name* (job 또는 step 또는 workflow_run conclusion) mapping 명시 의무, 실 구현 sub-cycle evidence 형식 본문 채택" | brief §2.4.1 + §2.4.2 + §5.2 (d) AR-3 row 본문 정정 |
| **BLOCKING-4** | R-MVP1-1.5-PC1-1 "미실행 commit 발견" 탐지 경로 명시 — 후보 3개 (hook marker / CI audit / `pre-commit run --all-files` 비교) 中 하나 이상 본문 채택 | brief §5.1 PC1-1 row 본문 정정 |

### 9.3 권고 5건

| # | 항목 | 흡수 형태 |
|---|------|---------|
| **권고-A** | PC-1 단독 보안 효과 ≈ 0 명문 — PC-1 + PC-3 + AR-3 결합 시 강제력 명시 | brief §2.3 + §3 매트릭스 (a) PC-1 row |
| **권고-B** | ST-2 failure mode evidence — "event 감지" + "메인 workload fail-closed 확인" 명시 | brief §2.2.1 + §5.2 (d) ST-2 row |
| **권고-F** | PC-1 명칭 일관성 — "PC-1-T3 mandatory enforcement" 또는 동등 prefix | brief §1.3 + §2.3 + §5 trigger 일관 |
| **권고-G** | AR-3 boundary 명문 — branch protection rule 본문에 Backlog #3 다른 항목 (signed commit / linear history) 미혼입 boundary | brief §2.4.4 + §6.2 #4 |
| **권고-H** | S-3 plugin identifier 정확화 — "AWS / Generic / Base64" → "AWSKeyDetector / Base64HighEntropyString / ..." + `--baseline` 미사용 CI assertion | brief §2.1.2 + §2.1.3 + §5.1 S3-1 |

### 9.4 권고 BLOCKING 흡수 후 발효 cycle

1. **brief v1 → v1.1 보강** — BLOCKING 4건 + 권고 5건 (사용자 결정 영역, Reviewer 통합 또는 brief 본문 흡수 중 선택)
2. **풀 3+1 합의 발효** — brief v1.1 input + codex 응답 + Agent A/B/C/Reviewer 통합
3. **본 cycle 합의 APPROVE 발효 시** = (e) 충족 + 실 구현 sub-cycle 4개 진입 권한 발효 (단축 합의 + 사용자 명시 + (b)(d) evidence 충실 조건)
4. **자동 진입 0건** — 단계별 합의 cycle 패턴 답습

### 9.5 본 cycle 영역 외 (재확인)

- ❌ MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상
- ❌ Implementation Evidence PASS 자동 발효
- ❌ 실 코드 / CI / hook / branch protection / config 본문 변경
- ❌ ADR / 헌법 / roadmap 본문 자동 갱신 (cross-reference 포함)
- ❌ Backlog #3 전체 자동 진입 (AR-3 단독 시점 변경 외)
- ❌ Hermes upstream Dockerfile 변경 (ST-2 sidecar 분리 자격 답습)
- ❌ `src/adapters/llm/facade.py` real 본문 (G5-4 별도 trajectory)
- ❌ Tier-2 / Tier-3 catalog 본문 확장 (S-3 plugin / URL / 모델 vendor)

---

## 10. 자기진단

| # | 항목 | 통과 |
|---|------|------|
| 1 | 본 분석 = entry brief 입력 분석 한정 (수단 결정 0건) | ✅ |
| 2 | brief 본문 자동 변경 0건 (수정 권고 한정) | ✅ |
| 3 | 실 코드 / CI / config 본문 변경 0건 | ✅ |
| 4 | Agent B / Agent C 출력 참조 0건 (독립 분석 자격) | ✅ |
| 5 | ceremony-inflation 0건 (4 sub-수단 평가 + Rollback Trigger 평가 + codex finding 흡수 + 의존성 + 판정 한정) | ✅ |
| 6 | MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 권고 0건 | ✅ |
| 7 | 헌법 / ADR 본문 자동 갱신 권고 0건 | ✅ |
| 8 | 자동 진입 / 자동 발효 권고 0건 (단계별 합의 cycle 답습) | ✅ |
| 9 | 입력 자료 직접 read 검증 완료 (brief / codex / ADR-011 / roadmap-mvp1 / audit / 선행 합의 2건 / 실 구현 도구 3건) | ✅ |
| 10 | Agent A 관점 = "실제로 동작하는가?" — 기술적 구현 가능성 + 의존성 + 성능 + 실 구현 자격 충실 | ✅ |

→ **10/10 통과** — 본 Agent A 분석 = 풀 3+1 합의 input 자격 충족.

--- Agent A 분석 종료 ---
