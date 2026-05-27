# CONTRIBUTING — dev workflow + PC-1-T3 mandatory enforcement

> **본 문서 = MVP-1 1.5차 보강 PC-1-T3 mandatory enforcement sub-cycle 답습**.
>
> 답습 출처:
> - `docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md`
> - `docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md` (Reviewer-only APPROVE)
> - 24번째 entry brief v1.1 §2.3 (PC-1-T3 정의)
> - CLAUDE.md (프로젝트 헌법 + 합의 cycle 답습)

---

## 1. dev onboarding workflow

### 1.1 최초 setup (필수, 1회)

```bash
git clone <repo-url>
cd AI_development_tool
bash bin/setup.sh
```

`bin/setup.sh` 가 다음을 자동 수행 (PC-1-T3 mandatory enforcement):

| 단계 | 동작 |
|---|---|
| 1/4 | Layer 3 (`.githooks/`) 활성화 — `git config core.hooksPath .githooks` |
| 2/4 | dev 의존성 설치 — `pip install -r requirements-dev.txt` (pre-commit framework 포함) |
| 3/4 | Layer 2 (`.pre-commit-config.yaml`) framework 활성화 — `pre-commit install` (T3 mandatory enforcement) |
| 4/4 | install audit log 기록 — `.git/pre-commit-audit/install.log` (R-6 (iii) 답습) |

### 1.2 setup 검증 (audit)

```bash
bash tools/pre_commit_install_audit.sh
```

3 탐지 경로 통합 verify (R-6 BLOCKING 답습):
- (i) `.git/hooks/pre-commit` 내 pre-commit framework marker grep
- (ii) `pre-commit` 명령 PATH 가용 + `pre-commit run --all-files` 실행 자격
- (iii) `.git/pre-commit-audit/install.log` 존재 여부

Exit 0 = 3/3 PASS / Exit 1 = bypass 의심 (R-MVP1-1.5-PC1-1 발화 자격)

---

## 2. PC-1-T3 mandatory enforcement 명문 (의무 + 우회 차단)

### 2.1 의무 (모든 dev 환경)

- **`pre-commit install` 의무** — 모든 dev 환경에서 `bin/setup.sh` 실행 의무 (`pre-commit install` 자동 호출)
- **commit 전 framework hook 통과 의무** — 매 `git commit` 시 `.pre-commit-config.yaml` 의 6 hook (secret-scanner / workflow-secret-usage / workflow-permissions / provider-import / provider-url-model / import-linter) 모두 PASS 의무
- **Layer 3 + Layer 2 병렬 의무** — `.githooks/pre-commit` (Layer 3 grep 기반) + `.pre-commit-config.yaml` (Layer 2 framework) 모두 활성화 의무 (D-5 (α) 병렬 유지 답습)

### 2.2 우회 차단 메커니즘 (Defense in depth)

PC-1 (dev 환경 hook) **단독 보안 효과 ≈ 0** — `pre-commit install` 로컬 우회 가능. 실제 강제력 = 3 계층 결합:

| 계층 | 수단 | 발효 |
|---|---|---|
| **1차 (dev)** | PC-1: `bin/setup.sh` + `pre-commit install` | 본 sub-cycle 발효 |
| **2차 (CI)** | PC-3: CI step 이 `.pre-commit-config.yaml` 검증 (`pre-commit run --all-files`) | 기존 발효 답습 |
| **3차 (merge)** | AR-3: GitHub branch protection rule status check 의무 | **별도 sub-cycle 답습** (carry-over (b1)) |

→ dev 환경 우회 (예: `git commit --no-verify`) 시 PC-3 CI step 에서 차단, CI 우회 시 AR-3 branch protection 에서 차단.

### 2.3 우회 발생 시 (Rollback Trigger R-MVP1-1.5-PC1-1)

`pre-commit install` 미실행 commit 발견 시:

1. `bash tools/pre_commit_install_audit.sh` 실행 → 3 탐지 경로 결과 확인
2. 본 commit 작성자 + 발생 경위 기록
3. **단축 합의 + 사용자 명시 재검토** (dev 환경 강제 메커니즘 보강 결정)

---

## 3. PR workflow

### 3.1 commit 전

```bash
pre-commit run --all-files    # local 격리 검증 (CI 와 동등 명령)
```

모든 hook PASS 확인 후 commit. **`git commit --no-verify` 사용 금지** (R-MVP1-1.5-PC1-1 발화 자격).

### 3.2 PR 제출 후

- CI status check 의무 (PC-3 답습 + AR-3 별도 sub-cycle 발효 후 의무화)
- 모든 status check PASS 후 merge 자격

### 3.3 `.pre-commit-config.yaml` 본문 변경 차등 (R-7(b) 답습)

| 변경 종류 | 합의 형태 |
|---|---|
| 신규 hook 추가 = Tier-2/3 catalog / provider policy / security gate 변경 | **풀 3+1 + 외부 LLM 1+** (R-MVP1-1.5-PC1-2 (i)) |
| 단순 version pin / hook config update | **단축 합의 + 사용자 명시** (R-MVP1-1.5-PC1-2 (ii)) |

---

## 4. 합의 cycle 답습 (CLAUDE.md §3 + 단계별 합의 cycle 6단계)

본 프로젝트의 모든 의사결정은 CLAUDE.md §3 멀티에이전트 합의 프로토콜 답습:

| 요청 유형 | 에이전트 수 | 이유 |
|---|---|---|
| 단순 코드 수정/버그 fix | 1 (직접 처리) | 오버헤드 불필요 |
| 아이디어 검증/분석 | 3+1 (필수) | 다관점 검증 필수 |
| 아키텍처 의사결정 | 3+1 (필수) | 다관점 필수 |
| SDD 명세 검토 | 3+1 (필수) | 교차 검증 필수 |
| 보안 관련 변경 | 3+1 (필수) | 보안은 다중 검증 필수 |
| 중간 규모 기능 구현 | 1~2 (복잡도에 따라) | 유연하게 판단 |

### 4.1 단계별 합의 cycle 6단계

```
1. brief 작성  →  2. 사용자 승인  →  3. 합의  →  4. 실 구현  →  5. commit  →  6. push
```

**자동 다음 단계 진입 금지** (사용자 명시 의무).

---

## 5. 코드 변경 시 의무 (TDD 답습)

- **모든 코드 작성 시 TDD 사이클 적용 필수** (RED → GREEN → REFACTOR)
- **테스트 커버리지 70% 이상**
- **언어**: 한국어 (소통) + 영어 (코드/commit message)
- **commit message**: Conventional Commits (feat / fix / docs / test / refactor / chore)

---

## 6. 참조 문서

| 문서 | 용도 |
|---|---|
| `CLAUDE.md` | 매 세션 자동 로드, 프로젝트 규칙 |
| `docs/CONTEXT.md` | 현재 프로젝트 상태 |
| `docs/INDEX.md` | 문서 전체 인덱스 |
| `docs/guides/DEVELOPMENT_GUIDE.md` | 개발 프로세스 상세 |
| `docs/guides/TEST_STRATEGY.md` | 테스트 전략 (70% 커버리지) |
| `docs/architecture/implementation-runtime-roadmap-mvp1.md` | MVP-1 로드맵 (GP-3 + GP-5) |
| `docs/decisions/ADR-011-means-vs-ends-redaction.md` | 수단/목적 분리 원칙 (Provider Liquidity 비협상) |
