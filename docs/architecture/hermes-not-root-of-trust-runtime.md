# Hermes ≠ Root of Trust Runtime (G3) — Design/Governance Gate PASS (Bundled, 2026-05-09)

> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 G3 — "Hermes ≠ root of trust" 원칙 (ADR-011 §2.3 영구 권위) 의 *운영 가능 메커니즘 설계 문서*. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
>
> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 권위 위계 운영 / 22 권한 분류 (T1 8 / T2 2 / T3 12) / 3 위험 5 측면 / 합의 인프라 자기참조 차단 / Evidence 결정 5 운영 규칙 / G2·G4 인터페이스의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — 실 hook / wrapper / sidecar / CI step / depcruise 룰 코드 구현 + Evidence Ledger enforcement + .git/ + .github/workflows/ + pre-commit + CI config + external-review 보호 강제는 *별도 합의* 로만 발생.
>
> **G3 운영 구현 상태 (P0 조건 C-B, 5/5 입력 일치)**: **DESIGN PASS / IMPLEMENTATION PENDING** (§1 ~ §7 모든 § 의 (a)~(e) 5조건 중 (b) 격리 환경 PoC + (d) 자동 회귀 검증 경로 미충족, 합의 보고서 §6 갱신 권고 흡수 시점에 별도 합의).
>
> **Hermes PMO 격상 / G3 운영 구현 PASS / P2 v3 정식 채택 / ADR 본문 자동 갱신 / archive 자동 처리는 본 PASS 에 포함되지 않는다** (사용자 명시 답습).

**작성일**: 2026-05-07
**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G2 + G4)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 관용 (Provider Liquidity), ADR-011 §2.3 (권위 위계 + 운영 함의 5항목, 영구 권위), ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리)
**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-011 (수단/목적 분리)
**관련 설계**: `hermes-adoption-design-v3.md` §5 (G3 정의), `governance-preconditions.md` (G2 — GP-2~GP-6 인터페이스 의존), `system-identity-prequel.md` §3 (권위 위계 prequel — ADR-011 §2.3로 승격), `canary-recheck-design.md` (R-5), `redaction-pattern-equivalence.md` (R-4)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Agent B 단독 발견 "합의 인프라 순환 권위 역설" + GPT 핵심 원칙 "Agent proposes / Tools verify / Evidence decides / Human overrides"), `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (ADR-011 §2.3 권위 승격), `docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md` (G2 §9 메타 안전장치 G3 위임), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G3 정식 PASS 합의)
**관련 evidence**: G1b PASS (R-7 SOP §7.3 단축 합의, 2026-05-07), G2 DRAFT 단축 검토 APPROVE (`957cddc`)

---

## 0. 본 초안의 범위

### 0.1 본 초안이 *하는* 것 (사용자 명시 7 항목 답습)

1. **권위 위계의 운영 구현** — Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents 가 *런타임 충돌 시* 어떻게 처리되는지 (§1)
2. **Hermes 권한 제한** — 허용 / 금지 권한 분리 + 강제 메커니즘 (§2)
3. **Silent drift / Upstream breakage / Skill escalation 대응** — 3 위험 각각 5 측면 정의 (§3)
4. **합의 인프라 순환 권위 해결** — Hermes-originated 합의의 자기참조 차단 (§4)
5. **Evidence 결정 원칙 운영 규칙화** — "Agent proposes / Hermes orchestrates / Tools verify / Evidence decides / Human overrides" 5단계를 운영 규칙으로 (§5)
6. **G2 인터페이스** — GP-2 ~ GP-6 각각과 G3의 연결점 (§6, **G2 PASS 선언 금지**)
7. **G4 경계** — 신뢰/권한(G3) vs 형식/schema(G4) 분리 (§7)

### 0.2 본 초안이 *하지 않는* 것 (사용자 명시 답습)

1. ❌ **G3 PASS 선언** — 본 초안은 *설계*까지만, (a)~(e) Exit 기준 충족 검증은 후속
2. ❌ **G2 / G4 PASS 선언**
3. ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 통과 + 사용자 명시 결정 후 별도
4. ❌ **P2 v3 정식 채택 선언** — `hermes-adoption-design-v3.md` 헤더 DRAFT 그대로 유지
5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음
6. ❌ **P2 v2 / system-identity-prequel.md archive 처리** — v3 정식 채택 시점에
7. ❌ **실 런타임 코드 구현** — 본 초안은 *운영 구현 설계 문서* 한정. 실 hook / wrapper / sidecar / CI step / depcruise 룰 코드 작성은 후속
8. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
9. ❌ **Hermes 단독 합의 자기참조** — 본 §4 자체가 이를 차단
10. ❌ **Tier-2 / Tier-3 catalog 확장** — 별도 합의

### 0.3 본 초안의 단계별 정식화 절차 (예정)

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | 본 초안 작성 (현 단계) | 본 문서 (DRAFT) | 2026-05-07 |
| 2 | 사용자 검토 + Reviewer-only 단축 검토 (DRAFT 적격) | 검토 보고서 별도 commit | 사용자 명시 결정 후 |
| 3 | 각 §의 PoC + (a)~(e) Exit 기준 충족 검증 | 운영 메커니즘 PoC 산출 + evidence | §별 순차 또는 병행 |
| 4 | G3 PASS 합의 가동 (단축 또는 풀 3+1, **본 §4 자기참조 차단 답습**) | `docs/review/3plus1-consensus-YYYY-MM-DD-g3.md` | 단계 3 완료 후 |
| 5 | G3 PASS 선언 + ADR cross-reference 갱신 (G2/G4와 묶음 가능) | 별도 PR | 단계 4 후 |

본 초안 자체는 단계 1까지만 처리. 단계 2~5는 본 초안 범위 외.

---

## 1. 권위 위계의 운영 구현

### 1.1 위계 (영구 권위 인용)

```
Constitution
  > ADR
  > SDD
  > Harness Gates (Layer 0~6)
  > Hermes
  > Worker Agents
```

본 위계는 **ADR-011 §2.3** 영구 권위로 승격되어 있으며, system-identity-prequel.md archived 후에도 보존된다 (ADR-011 §2.3 prequel과의 관계). 본 §1 은 위 위계를 *런타임 충돌 시* 어떻게 작동하는지 정의한다.

### 1.2 충돌 해결 매트릭스

#### 1.2.1 Hermes 판단 vs ADR / SDD 충돌

| 시나리오 | 처리 | 권위 근거 | Evidence 요구 |
|---------|-----|---------|----------|
| Hermes 가 ADR/SDD 와 모순되는 결정 제안 | **자동 reject** + 사용자 alert | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력) | 모순 detection log + Hermes 결정 본문 + ADR/SDD 인용 |
| Hermes 가 ADR/SDD 본문을 자동 수정 시도 | **filesystem read-only로 차단** + audit log + 컨테이너 정지 | ADR-011 §2.4 T3 (자동 정책 변경 금지) + system-identity-prequel §3.3 #1 | filesystem ACL 거부 log + audit log entry |
| Hermes 가 새 ADR 작성 제안 | 제안은 가능, **작성·승인은 사용자 명시 only** | ADR-011 §2.4 T2 | 제안 본문 (제안 한정 evidence) |
| ADR 갱신 PR (사용자 발의) 에 Hermes 가 자동 승인/merge 시도 | **CI step 으로 차단** (ADR PR 은 사용자 명시 결정 only) | ADR-011 §2.4 T3 | PR 차단 log |

#### 1.2.2 Worker Agent 출력 vs Hermes 판단 충돌

| 시나리오 | 처리 | 권위 근거 | Evidence 요구 |
|---------|-----|---------|----------|
| Worker 가 Hermes 와 다른 결론 도출 | **Tools 검증 결과 우선** — Hermes 출력은 Tools 위에 위치 안 함 | ADR-011 §2.3 운영 함의 #1 | Worker 출력 + Tools 검증 결과 + Hermes 결론 모두 보존 |
| Worker 출력을 Hermes 가 *내부* 처럼 신뢰 (검증 우회) | **GP-4 외부 입력 검증으로 차단** | G2 GP-4 + ADR-011 §2.3 운영 함의 #1 | 검증 layer 통과 evidence |
| 3+1 합의에서 Reviewer 결과 vs Hermes orchestration 결과 | **Reviewer 결과 우선** (Hermes 는 *기록* 만, *승인* 불가, §4 답습) | system-identity-prequel §3.3 #2 (합의 결과 git commit 강제) | Reviewer 보고서 + git commit hash |
| Worker 가 Tools 검증 우회 시도 | **wrapper layer 에서 BLOCK** | G2 GP-4 | BLOCK log |

#### 1.2.3 Harness Gate 실패 vs Hermes 완료 처리

| 시나리오 | 처리 | 권위 근거 | Evidence 요구 |
|---------|-----|---------|----------|
| Layer 1 (PostToolUse hook) 실패 시 Hermes 가 다음 단계 진행 시도 | **hook 실패 → Hermes 작업 큐 차단** | CLAUDE.md §피드백 루프 계층 + ADR-011 §2.3 | hook 실패 log + 큐 상태 |
| Layer 2 (PreCommit hook) / Layer 3 (git pre-commit) 실패 시 Hermes 가 commit 강제 시도 | **git layer 자체 차단** (Hermes 권한 외) | 헌법 9조 + 시스템 권한 분리 | hook 실패 log |
| Layer 4 (CI) 실패 시 Hermes 가 PASS 처리 시도 | **CI 결과 evidence 기반 PASS 거부** + 사용자 alert | §5 Evidence 결정 원칙 | CI run ID + 실패 step + evidence ledger |
| Layer 5 (3+1 합의) BLOCK / ROLLBACK 결과를 Hermes 가 silent override | **Hermes 단독 override 금지** + audit log + 자동 reject | system-identity-prequel §3.3 #2 + ADR-011 §2.4 T3 | 합의 결과 commit + Hermes override 시도 log |
| Layer 6 (사용자 review) 미완료 시 Hermes 가 다음 단계 진행 | **사용자 명시 승인 필요 영역에서는 Hermes 단독 진행 금지** | ADR-011 §2.4 T2 | 사용자 승인 evidence |

### 1.3 Evidence 없는 PASS 금지 (Hard Rule)

**원칙**: 모든 PASS 판정은 Evidence Ledger 기록 의무. Evidence 없는 PASS 시도 → **자동 reject**.

| 영역 | PASS 성립 요건 (모두 충족) | 검증 방식 |
|-----|--------------------|--------|
| 코드 변경 | 린터 PASS + 타입체크 PASS + 테스트 PASS + (Evidence Ledger entry 존재) | Layer 1~4 hook + ledger 검증 step |
| Harness Gate (G1b 등) | (a)~(e) Exit 기준 모두 충족 + 합의 보고서 + ledger entry | 본 G3 §5.3 + 각 GP §X.5 |
| 보안 변경 | 헌법 8조 #4 (3+1 합의) + ledger entry | Layer 5 + ledger |
| Skill 등록 / Memory promotion | T2 사용자 명시 승인 + ledger entry | §6.5 + ledger |
| Hermes 격상 (G2/G3/G4 PASS 후) | 4 게이트 모두 PASS + 통합 풀 3+1 합의 + 사용자 명시 결정 + ledger entry | 본 G3 §4.3 + 격상 합의 |

**Evidence Ledger 기록 의무**:
- Markdown (`docs/evidence/<task-id>.md`) — 사람 검토 대상
- JSONL (`docs/evidence/ledger.jsonl`) — append-only, hash chain 또는 git append commit 변조 방지

**Evidence 없는 PASS 자동 reject 메커니즘**:
- Layer 1~2 hook: PASS 판정 발화 시 ledger entry 존재 검증, 없으면 hook FAIL
- Layer 4 CI: PASS verdict 추출 시 ledger entry hash 일치 검증
- Layer 5 합의: 합의 보고서 commit 자체가 ledger 보충 (system-identity-prequel §3.3 #2)

### 1.4 본 §1 이 *하지 않는* 것

- ❌ 위계 자체의 변경 (T3 영역)
- ❌ Layer 1~6 hook 실 코드 작성 (본 초안은 설계까지)
- ❌ Evidence Ledger schema 본문 정의 (system-identity-prequel §6.3 → P2 v3 §X 또는 신규 ADR-012 영역)

---

## 2. Hermes 권한 제한

### 2.1 허용 권한 (Whitelist)

다음은 Hermes 가 단독 권한으로 실행 가능 (ADR-011 §2.4 **T1 자동**):

| # | 권한 | 범위 | Evidence 요구 |
|---|------|-----|----------|
| 1 | **작업 분배 (오케스트레이션)** | Worker Agent 호출 + 작업 큐 관리 + 우선순위 정렬 | orchestration log |
| 2 | **Memory 조회** | Global / Project Memory **read-only** (write 는 §2.2 #15 으로 제한) | read log (선택) |
| 3 | **Skill 후보 제안** | 반복 작업 패턴 → Skill 후보 추출 + 사용자 alert (등록은 §2.2 #16) | 후보 본문 + 추출 사유 |
| 4 | **합의 실행 보조 (orchestrate)** | 3+1 합의 프로토콜 실행 — Agent A/B/C/Reviewer 호출 + 결과 수집 (승인은 §4) | 합의 progress log |
| 5 | **Evidence 위치 정리** | Evidence Markdown / JSONL 파일 위치 정리 + INDEX 갱신 제안 (실 갱신은 사용자 명시) | 정리 제안 본문 |
| 6 | **다음 작업 제안** | 작업 분해 + 다음 단계 추천 (실 진입은 사용자 명시 또는 T1 영역만) | 제안 본문 |
| 7 | **자체 학습 (T1 한정)** | 도구 사용 빈도 누적 + 실패 회피 휴리스틱 (적용은 §2.2 #17) | 학습 log (audit 가능) |
| 8 | **Hermes 자체 redaction (로그/송신 한정)** | Tier-1 catalog 적용 — DB INSERT 차단은 G1b SQLCipher trigger 책임 (보조) | redaction log |

### 2.2 금지 권한 (Blacklist)

다음은 Hermes 가 단독으로 시도 시 **자동 reject + audit log + 사용자 alert** (ADR-011 §2.4 **T3 절대 금지** 또는 **T2 사용자 승인 필수**):

| # | 금지 행위 | 분류 | 권위 근거 | 강제 메커니즘 |
|---|---------|-----|---------|----------|
| 9 | **정책 자동 변경** (Constitution / ADR / SDD / Harness Gate 정의) | T3 | ADR-011 §2.4 + system-identity-prequel §3.3 #1 | filesystem read-only mount + T3 변경 감지 hook |
| 10 | **ADR 자동 수정 / 자동 승인** | T3 | ADR-011 §2.4 + 헌법 7조 | filesystem read-only on `docs/decisions/ADR-*.md` + git pre-commit hook |
| 11 | **Constitution 우회** | T3 | 헌법 자체 + ADR-011 §2.3 위계 | Constitution write 권한 0 + audit log |
| 12 | **Harness Gate 실패 무시** | T3 | §1.2.3 Layer 1~6 답습 | hook 실패 시 자동 큐 차단 (§1.2.3) |
| 13 | **G2 / G3 / G4 PASS 자동 선언** | T3 | ADR-011 §2.4 + 본 G3 §4 (자기참조 차단) | git commit 본문 검증 hook + 합의 보고서 강제 |
| 14 | **Hermes PMO 자기 격상** | T3 | system-identity-prequel §4.2 + 본 §4.3 | 격상 명령 실행 권한 0 + audit log |
| 15 | **Memory write (Project → Global 자동 promotion)** | T2 (자동 금지) | system-identity-prequel §8.4 ("manual only") | promotion 명령 hook 차단 + 사용자 명시 결정 강제 |
| 16 | **Skill 자동 등록** | T2 | system-identity-prequel §8 + ADR-011 §2.4 | Skill 등록 hook 차단 + 사용자 명시 승인 강제 |
| 17 | **자체 학습 결과의 자동 정책 반영** | T3 | ADR-011 §2.4 (자동 학습 vs 정책 변경 분리) | 정책 파일 read-only + T3 변경 감지 hook |
| 18 | **Provider lock-in 유도** (Hermes 자체 SDK 직접 import 또는 모델명 분기 코드 생성) | T3 | 헌법 5조 (관용 — Provider Liquidity) + ADR-008 차단조건 #4 + G2 GP-5 | depcruise 룰 + PR auto-reject |
| 19 | **Secret redaction 정책 완화** | T3 | ADR-011 §2.1 (수단/목적 분리) + G2 GP-1 / GP-2 | redaction-policy.yaml read-only + T3 변경 감지 hook |
| 20 | **합의 결과 silent override 또는 수정** | T3 | system-identity-prequel §3.3 #2 + 본 §4 | 합의 보고서 git commit 보존 + Hermes-originated 수정 자동 reject |
| 21 | **Tier-1 / Tier-2 / Tier-3 canary catalog 자동 확장** | T3 | ADR-011 §2.4 + R-7 SOP §3.4 | catalog 파일 read-only + 별도 합의 강제 |
| 22 | **사용자 override 자동 reject 시도** | T3 | ADR-011 §2.3 운영 함의 #5 ("Human overrides") + §5.4 | override 거부 시도 자체가 audit log + 사용자 alert |

### 2.3 강제 메커니즘 분류

§2.1 허용 8건 + §2.2 금지 14건 = 총 22 권한 항목. ADR-011 §2.4 분류:

```
T1 (자동 허용)        : 8 건  (§2.1 #1 ~ #8)
T2 (사용자 승인 필수) : 2 건  (§2.2 #15, #16)
T3 (절대 금지)        : 12 건 (§2.2 #9~#14, #17~#22)
```

### 2.4 강제 메커니즘 매트릭스 (계산적 / 추론적 / 자동 롤백)

| 권한 항목 | 계산적 | 추론적 보조 | 자동 롤백 |
|---------|------|---------|--------|
| #1~#7 (T1 자동) | ✅ orchestration log | ❌ 불필요 | ❌ 롤백 대상 아님 |
| #8 (T1 redaction) | ✅ Tier-1 catalog match | ⚠️ 보조 | ✅ ROLLBACK trigger R5 |
| #9~#11 (T3 정책/ADR/Constitution) | ✅ filesystem ACL + git hook | ❌ 불필요 | ✅ 자동 reject |
| #12 (T3 Gate 실패 무시) | ✅ hook 실패 → 큐 차단 | ❌ 불필요 | ✅ 자동 큐 차단 |
| #13 (T3 PASS 자동 선언) | ✅ commit 본문 검증 | ⚠️ 보조 (Reviewer) | ✅ 합의 부재 시 PASS reject |
| #14 (T3 자기 격상) | ✅ 격상 명령 권한 0 | ❌ 불필요 | ✅ audit log + 사용자 alert |
| #15, #16 (T2 Memory/Skill 자동) | ✅ promotion hook 차단 | ❌ 불필요 | ✅ 사용자 승인 부재 시 reject |
| #17 (T3 학습→정책) | ✅ 정책 파일 read-only | ⚠️ 보조 (drift detection) | ✅ ROLLBACK §3.1 |
| #18 (T3 Provider lock-in) | ✅ depcruise 룰 | ❌ 불필요 | ✅ PR auto-reject |
| #19 (T3 redaction 완화) | ✅ policy read-only | ❌ 불필요 | ✅ ROLLBACK §3.1 |
| #20 (T3 합의 override) | ✅ git commit 보존 | ⚠️ 보조 | ✅ Hermes-originated 수정 reject |
| #21 (T3 catalog 확장) | ✅ catalog read-only | ❌ 불필요 | ✅ ROLLBACK §3.2 |
| #22 (T3 사용자 override reject) | ✅ override 거부 시도 audit | ⚠️ 보조 | ✅ 사용자 alert |

**합산**: 계산적 22/22, 추론적 보조 6/22, 자동 롤백 14/22 (T1 #1~#7 외 전부).

### 2.5 보호 대상 파일·디렉토리 enumeration (T3, C-D 흡수 — 2026-05-09 후속 2)

> **본 §2.5 는 합의 보고서 §11.2 P1 조건 C-D 흡수** (출처: GPT 조건 4 + B Gap-3 + B Gap-6). §2.2 #9~#11 (정책 자동 변경 / ADR 자동 수정 / Constitution 우회) 의 *대상 파일·디렉토리 범위* 를 명시 enumeration 한다.

다음은 Hermes / Worker Agent / Hermes-originated automation 이 **자동 변경 시도 시 자동 reject + audit log + 사용자 alert** (T3) 대상:

| # | 보호 대상 | 분류 | 강제 메커니즘 | 권위 근거 |
|---|---------|-----|----------|---------|
| 1 | `.git/` (HEAD, config, hooks, packed-refs, refs/) | T3 | filesystem ACL: Hermes container `read_only` mount + `:ro` bind / `cap_drop=ALL` | system-identity-prequel §3.3 #1 + 본 §2.2 #20 |
| 2 | `.github/workflows/*.yml` (GitHub Actions workflow) | T3 | git pre-commit hook on `.github/workflows/` + Hermes-originated commit auto-reject | 본 §2.2 #9 (정책 자동 변경) + R-6 actual run 권위 |
| 3 | `.pre-commit-config.yaml` / `.husky/` / Layer 1~2 hook config | T3 | filesystem read-only on hook config + git pre-commit hook | 본 §2.2 #12 (Harness Gate 실패 무시) + 헌법 1~4조 |
| 4 | `.github/CODEOWNERS` / branch protection 정의 | T3 | filesystem read-only + GitHub branch protection API audit | 본 §2.2 #20 (합의 결과 silent override) |
| 5 | `docs/decisions/ADR-*.md` (ADR 본문 전체) | T3 | filesystem read-only + git pre-commit hook | 본 §2.2 #10 (ADR 자동 수정) + ADR-011 §2.3 |
| 6 | `docs/architecture/governance-preconditions.md` / `hermes-not-root-of-trust-runtime.md` / `provider-agnostic-memory-skill-design.md` (G2/G3/G4 정의 문서) | T3 | filesystem read-only on Hermes container + 본 §4 자기참조 차단 | 본 §2.2 #13 (G2/G3/G4 PASS 자동 선언) + G2 §9.2 |
| 7 | `docs/architecture/hermes-adoption-design-v3.md` (P2 v3) / SDD 명세 본문 | T3 | filesystem read-only + git pre-commit hook | 본 §2.2 #9 (정책 자동 변경) + 헌법 1조 (SDD) |
| 8 | `docs/constitution/*.md` (헌법 본문) | T3 | filesystem read-only + git pre-commit hook | 본 §2.2 #11 (Constitution 우회) + 헌법 자체 |
| 9 | `docs/external-review/*.md` (외부 LLM 의뢰·응답 자료) | T3 | filesystem append-only + Hermes-originated 변경 자동 reject + 본 §4 외부 LLM 자기참조 차단 | 본 §2.2 #20 (합의 결과 silent override) + 본 §4.4.2 |
| 10 | `docs/review/3plus1-consensus-*.md` (합의 보고서) | T3 (작성 후 immutable) | git append-only (수정은 별도 commit + 사용자 명시) + Hermes-originated 수정 자동 reject | 본 §2.2 #20 + system-identity-prequel §3.3 #2 |
| 11 | Evidence Ledger (`docs/phase0/*-evidence.md`, JSONL ledger 파일, R-6 artifact) | T3 (append-only) | hash chain 또는 git append commit + Hermes-originated 수정 자동 reject + signed commit (PR-2 ADR-012 후보) | system-identity-prequel §6.3 + 본 §5.2.4 |
| 12 | `docs/phase0/redaction-verification-sop.md` / R-7 SOP | T3 | filesystem read-only + 본 §2.2 #19 (redaction 정책 완화) | R-7 SOP §3.4 |
| 13 | `redaction-policy.yaml` / Tier-1 catalog / `skill-permissions.yaml` / `canary-catalog/` (정책성 파일) | T3 | filesystem read-only on Hermes container + R-5 canary recheck + 본 §3.1 (Learning silent drift) | ADR-011 §2.4 + 본 §2.2 #19, #21 |
| 14 | `hermes-version.yaml` + dependency lock (`requirements.txt` / `pyproject.toml` / `poetry.lock`) | T2 (사용자 명시 PR merge) | R-6 workflow 의존성 변경 감지 + 사용자 명시 PR merge | ADR-008 차단조건 #3 + 본 §3.2 |
| 15 | `.claude/settings.json` / `.claude/commands/` / `claude-code` 하네스 정의 | T3 | filesystem read-only on Hermes container + 사용자 명시 결정 강제 | system-identity-prequel §3.3 #1 |

**enumeration 의 의미**:
- 본 §2.5 는 §2.2 #9~#11 의 *대상 범위* 를 *명시* (silent expansion 차단)
- 신규 보호 대상 추가 = T3 변경 절차 (풀 3+1 합의 + ADR Amendment + 사용자 명시 결정)
- 본 enumeration 자체도 본 §2.5 의 보호 대상 (#6: G3 정의 문서)

**G2 §9.2 와의 인터페이스**: G2 §9.2 #1 ("filesystem read-only on `docs/architecture/governance-preconditions.md`") 의 *대상 범위* 가 본 §2.5 #1~#15 로 확장. G2 §9.2 본문 *변경 없이* 본 §2.5 가 대상 enumeration 을 흡수.

**Implementation 상태**: 본 §2.5 는 *enumeration 명시* 까지. 실 hook / filesystem ACL / pre-commit / CI step 구현은 **DESIGN PASS / IMPLEMENTATION PENDING** (별도 합의, Implementation/Runtime PASS 영역).

---

## 3. Silent Drift / Upstream Breakage / Skill Escalation 대응

> **본 §3 은 G2 단축 검토 §3.1 P-1 ("§1.2.4 추가 위반 경로 후보 명시 권고") 답습** — 3 위험을 G3 운영 구현으로 흡수.

### 3.1 Learning Silent Drift (학습 silent 변경)

#### 3.1.1 정의

Hermes 자체 학습 결과 (T1 자동 학습) 가 **redaction 정책 / canary catalog / Skill 권한 등급 / Memory boundary** 등 *정책성* 파일을 silent 변경. ADR-011 §2.4 (자동 학습 vs 정책 변경 분리) 직접 위반.

#### 3.1.2 감지 방법 (Detection)

| 감지 channel | 메커니즘 | 시점 |
|------------|--------|-----|
| **CI nightly diff** | 정책 파일 (redaction-policy.yaml / Tier-1 catalog / skill-permissions.yaml 등) git diff 자동 점검 | nightly |
| **Hermes-originated commit detection** | git commit author / committer + Hermes audit log cross-reference | every commit |
| **R-5 canary recheck (T13 강화)** | canary 패턴 변경 감지 시 alert | 6 trigger 시점 (R-5 §X) |
| **Redaction 동작 회귀 (R-6 actual run)** | Tier-1 42 catalog 동작 변경 감지 | nightly + push/PR |

#### 3.1.3 차단 방법 (Blocking)

| layer | 메커니즘 | 권위 |
|------|--------|-----|
| 파일시스템 | 정책 파일 read-only mount on Hermes container | system-identity-prequel §3.3 #1 |
| Git | pre-commit hook on 정책 파일 — Hermes-originated commit 자동 reject | §2.2 #20 + system-identity-prequel §3.3 #2 |
| CI | nightly diff 발견 시 build FAIL | 본 §3.1.2 #1 |
| Runtime | 정책 파일 변경 시 Hermes 컨테이너 자동 정지 | system-identity-prequel §3.3 #4 (권위 등급 위반 자동 reject) |

#### 3.1.4 Evidence 요구사항

- Markdown report: 변경 본문 + Hermes 학습 log 인용 + diff
- JSONL ledger entry: `{"event": "drift_detected", "agent": "Hermes", "result": "BLOCK", "ref": "<file_path>", "summary": "<diff summary>"}`
- audit log: Hermes-originated 변경 시도 본문 (별도 audit JSONL)

#### 3.1.5 Rollback Trigger

- ADR-011 §2.4 T3 위반 검출 → **Hermes 컨테이너 정지 + 변경 reject + 사용자 alert**
- R-7 SOP §5 ROLLBACK trigger 답습 (R5 패턴 — Hermes 학습 평문 검출 확장)
- Rollback 후: 정책 파일 git revert + Hermes 학습 log 보존 + 사용자 명시 검토 (T2 → 정식 변경 또는 폐기)

#### 3.1.6 사용자 승인 필요 여부

- T3 변경은 **사용자도 ADR Amendment 절차 거쳐야** (자동 변경 금지)
- 사용자 명시 결정 + 풀 3+1 합의 (T3 변경) 통과 후만 정책 변경 가능
- Rollback 자체는 자동 (T3 위반 차단 = 자동 안전 동작)

### 3.2 Upstream Silent Breakage (의존성 업그레이드 silent 깨짐)

#### 3.2.1 정의

Hermes / Hermes-agent / pysqlcipher3 / litellm 등 의존성 업그레이드로 **redaction / SQLCipher trigger / P1 facade / canary catalog** 동작이 silent 깨짐. ADR-011 §2.3 운영 함의 #4 ("Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증") 직접 침해.

#### 3.2.2 감지 방법 (Detection)

| 감지 channel | 메커니즘 | 시점 |
|------------|--------|-----|
| **R-6 workflow trigger 확장** | `hermes-version.yaml` 변경 시 자동 R-2 / R-4.1 PoC 재실행 | every PR / push 정책 파일 변경 |
| **R-6 nightly cron** | 정책 파일 변경 없어도 nightly canary 재실행 | nightly |
| **dependency lock 변경 감지** | `requirements.txt` / `pyproject.toml` / `pip-tools` lock diff | every commit |
| **Hermes 자체 telemetry endpoint 차단 회귀 검증** | egress whitelist 자동 검증 (DoH / NousResearch 분석 서버) | nightly |

#### 3.2.3 차단 방법 (Blocking)

| layer | 메커니즘 | 권위 |
|------|--------|-----|
| Version pin | `hermes-version.yaml` v0.12.0 명시 + checksum 검증 | ADR-008 차단조건 #3 |
| PR | dependency 변경 PR 자동 R-2 / R-4.1 PoC 재실행 → FAIL 시 merge 차단 | §3.2.2 #1 |
| CI | R-6 actual run PASS 후만 merge 가능 | R-6 workflow + branch protection rule (사용자 명시) |
| Runtime | 의존성 업그레이드 후 컨테이너 재시작 시 canary 자동 재실행 PASS 후만 부팅 | runtime healthcheck (G3 산출 후보) |

#### 3.2.4 Evidence 요구사항

- GitHub Actions run ID + verdict PASS evidence
- Artifact `r2-r4-canary-evidence` (canary-output.log + canary-evidence.json)
- JSONL ledger: `{"event": "upstream_recheck", "agent": "Hermes", "result": "PASS"|"FAIL", "ref": "<run_id>"}`
- 의존성 변경 본문 (lock diff)

#### 3.2.5 Rollback Trigger

- R-7 SOP §5 ROLLBACK trigger R6 (upstream breakage) — `hermes-version.yaml` 변경 PR 의 R-6 actual run FAIL 시
- Rollback 후: 이전 버전 핀 복귀 + canary catalog 재검증 + 사용자 명시 검토
- 의존성 업그레이드는 **사용자 명시 PR merge 결정 + R-6 PASS** 양쪽 충족 시만 진행

#### 3.2.6 사용자 승인 필요 여부

- 의존성 업그레이드 PR merge 는 **사용자 명시 결정** (T2)
- Hermes 가 자동 PR 생성은 가능 (T1 학습 결과 알림), **자동 merge 는 절대 금지** (T3)
- Rollback 자체는 자동 (FAIL 시 차단 = 자동 안전 동작)

### 3.3 Skill Permission Escalation (Skill 권한 상승)

#### 3.3.1 정의

Skill 이 정의된 권한 등급 (read / write / shell / network / DB 등) 을 *넘어* 작동. 예: read-only Skill 이 write 시도 / sandbox Skill 이 shell escape 시도.

#### 3.3.2 감지 방법 (Detection)

| 감지 channel | 메커니즘 | 시점 |
|------------|--------|-----|
| **Skill wrapper 권한 검증** | Skill 실행 wrapper layer 가 매 호출 시 권한 등급 확인 | every Skill 호출 |
| **Audit log 분석 (T1 학습 결과)** | Skill 호출 패턴이 정의 권한 등급을 *암시적으로* 우회하는지 nightly 분석 | nightly |
| **Sandbox escape 검출** | Docker container / OS-level sandbox 의 syscall 추적 | every Skill 호출 (옵션 — runtime 비용) |

#### 3.3.3 차단 방법 (Blocking)

| layer | 메커니즘 | 권위 |
|------|--------|-----|
| Wrapper | Skill 실행 wrapper 가 권한 등급 외 호출 즉시 BLOCK | §6.5 (G3 ↔ G4 인터페이스) |
| Sandbox | Docker container cap_drop ALL + read_only + tmpfs noexec | ADR-008 §2.6 R1-1 |
| Audit | escalation 시도 본문 audit JSONL + 사용자 alert | system-identity-prequel §3.3 #3 |
| Runtime | escalation 검출 시 해당 Skill 자동 비활성화 | §3.3.5 |

#### 3.3.4 Evidence 요구사항

- Skill 정의 (`<skill>.yaml` 권한 등급 명시)
- Skill 실행 audit log (호출 인자 + 출력 + 권한 등급)
- escalation 시도 본문 (BLOCK 사유 + diff)
- JSONL ledger: `{"event": "skill_escalation", "agent": "<skill_name>", "result": "BLOCK", "ref": "<call_id>", "summary": "..."}`

#### 3.3.5 Rollback Trigger

- escalation 검출 시 **해당 Skill 자동 비활성화** + 사용자 alert
- Skill 등록 자체가 T2 (사용자 명시 승인 — §2.2 #16) 이므로, 비활성화도 사용자 명시 재활성화 결정 후만 복귀
- 반복 escalation 시도 시 Skill 자체 archive (T2 → 정식 폐기 또는 권한 등급 재검토)

#### 3.3.6 사용자 승인 필요 여부

- Skill 등록 자체 = **T2 사용자 명시 승인** (§2.2 #16)
- Skill 권한 등급 변경 = **T2** (등록과 동급)
- 비활성화 자동 (T3 위반 차단 = 자동 안전 동작), 재활성화는 T2

### 3.4 본 §3 통합 매트릭스

| 위험 | 감지 | 차단 | Evidence | Rollback | 사용자 승인 |
|------|------|-----|--------|--------|---------|
| 3.1 Learning silent drift | CI nightly diff + Hermes-originated detection + R-5 canary + R-6 actual run | filesystem read-only + git pre-commit + CI FAIL + 컨테이너 정지 | Markdown + JSONL ledger + audit | T3 위반 → 자동 정지 + revert | T3 변경 (자동 금지, 사용자도 ADR Amendment) |
| 3.2 Upstream silent breakage | R-6 workflow trigger 확장 + nightly cron + lock diff + telemetry 차단 회귀 | version pin + PR PoC 재실행 + R-6 PASS branch protection + runtime healthcheck | GH run + artifact + JSONL + lock diff | R-7 SOP R6 (이전 버전 복귀) | PR merge T2 (Hermes 자동 PR 생성 OK / 자동 merge 금지) |
| 3.3 Skill permission escalation | wrapper 권한 검증 + audit T1 분석 + sandbox syscall 추적 | wrapper BLOCK + Docker cap_drop + audit log + 자동 비활성화 | skill 정의 + audit log + escalation 본문 + JSONL | 자동 비활성화 + 반복 시 archive | Skill 등록 T2 + 재활성화 T2 |

---

## 4. 합의 인프라 순환 권위 해결

### 4.1 문제 정의 (자기참조 역설)

**문제**: Hermes 가 3+1 합의 *실행 인프라* 라면, *Hermes 자기 격상 / Hermes 정책 변경 / G2/G3/G4 PASS 등* Hermes 관련 결정을 Hermes 가 실행한 합의로 결정 → **자기참조 역설**.

**합의 §90 (Agent B 단독 발견)** 답습: "합의 인프라 순환 권위 역설" — 본 §4 가 핵심 흡수 (system-identity-prequel §3.3 #2 답습).

### 4.2 자기참조 차단 원칙

| 원칙 | 근거 |
|------|-----|
| 1. Hermes 관련 결정은 Hermes 단독 합의 금지 | system-identity-prequel §3.3 #2 + 본 §4.3 매트릭스 |
| 2. Reviewer-only 또는 외부 LLM 의견이 Hermes 관련 결정의 합의에 필수 | 본 §4.4 + 합의 §201 (GPT 의견 메타-편향 통제) |
| 3. 사용자 승인이 모든 T2 / T3 결정의 *최종* 권위 | ADR-011 §2.4 T2/T3 + ADR-011 §2.3 운영 함의 #5 |
| 4. Hermes 는 합의 결과 *기록*만 가능, *승인 주체*가 될 수 없음 | system-identity-prequel §3.3 #2 |

### 4.3 Hermes 관련 결정의 합의 형태 매트릭스

| 결정 유형 | Hermes 단독 가능? | 합의 형태 | 외부 LLM 필요? | 사용자 승인 | 분류 |
|---------|-------------|--------|----------|---------|------|
| Worker Agent 작업 분배 | ✅ Hermes 단독 | 합의 불필요 | ❌ | ❌ | T1 |
| Worker 출력 검증 (Tools 통해) | ✅ Tools 자동 | 합의 불필요 | ❌ | ❌ | T1 (Tools 영역) |
| Skill 후보 제안 | ✅ Hermes 제안 | 합의 불필요 | ❌ | ❌ (제안 한정) | T1 |
| **Skill 등록** | ❌ 단독 불가 | 합의 불필요 (T2 직접) | ❌ | ✅ 명시 결정 | T2 |
| **Memory promotion (Project → Global)** | ❌ 단독 불가 | 합의 불필요 (T2 직접) | ❌ | ✅ 명시 결정 | T2 |
| 일반 합의 (예: 패턴 동등성, 설계 선택) | ✅ orchestrate | 단축 또는 풀 3+1 | 선택 (외부 검증 권장) | ✅ 합의 결과 채택 | T2 |
| **G1b PASS 승격** | ✅ orchestrate | 단축 (Reviewer-only) — R-7 SOP §7.3 | ❌ (단축 한정) | ✅ 명시 결정 | T2 (이미 발생, 2026-05-07) |
| **G2 / G3 / G4 PASS** | ✅ orchestrate | 단축 또는 풀 3+1 | 권장 (메타 편향 통제) | ✅ 명시 결정 | T2 |
| **Hermes PMO 격상 (4 게이트 통합)** | ❌ Hermes 자기참조 영역 | **풀 3+1 합의 + 외부 LLM 1+ 필수** | ✅ 필수 (메타 편향 통제) | ✅ 명시 결정 | T2 (단, 외부 검증 강화) |
| **Hermes 정책 변경** (redaction-policy.yaml 등) | ❌ 단독 불가 | **풀 3+1 합의 + 외부 LLM 1+ 권장** | ✅ 권장 | ✅ 명시 결정 + ADR Amendment | T3 영역 (정책 자체 변경) |
| **Constitution / ADR 본문 갱신** | ❌ 작성 불가 | 풀 3+1 합의 | 권장 | ✅ 명시 결정 + ADR Amendment | T3 |
| **Harness Gate 정의 자체 변경** | ❌ 단독 불가 | 풀 3+1 합의 | 권장 | ✅ 명시 결정 + ADR Amendment | T3 |
| **본 §4 / §9 본문 변경** | ❌ 단독 불가 | 풀 3+1 합의 + ADR Amendment | 권장 | ✅ 명시 결정 | T3 |

### 4.4 Reviewer-only / 외부 LLM / 사용자 승인 조건

#### 4.4.1 Reviewer-only 단축 합의 충분 조건

다음 모두 충족 시 Reviewer-only 단축 합의 적격:
- 새 *권위 결정* 0건 (evidence 흡수 / 정의 + 매핑 작업)
- 직전 합의 (R-3 / G1b PASS / P2 v3 DRAFT / G2 DRAFT) 패턴 답습 가능
- ADR-011 §2.4 분류 T2 (사용자 승인 기반)
- 사용자 명시 결정으로 단축 합의 형태 채택

#### 4.4.2 외부 LLM (비-Claude) 의견 필요 조건

다음 시 외부 LLM 의견 필수 또는 강력 권장:
- **Hermes PMO 격상 통합 합의** (필수 — 메타 편향 통제)
- **Hermes 정책 변경** (redaction-policy / catalog 등 — 권장)
- **Constitution / ADR 본문 갱신** (권장)
- **자기 작성 산출 검증** (현 Reviewer-only 패턴이 외부 검증으로 강화)

외부 LLM 의견은 다음 형식 중 하나:
- 별도 LLM 호출 결과 (GPT / Gemini / Local LLM 등)
- 외부 검토 의뢰 자료 (`docs/external-review/` 패턴 답습)
- 외부 Reviewer 또는 다른 사용자 검토

#### 4.4.3 사용자 승인 필요 조건

다음 시 사용자 명시 승인 필수 (자동 진행 절대 금지):
- T2 모든 결정 (Skill 등록 / Memory promotion / 합의 결과 채택 / 격상)
- T3 모든 변경 (정책 / ADR / Constitution / Harness Gate)
- 의존성 업그레이드 PR merge (§3.2.6)
- 합의 형태 결정 (단축 vs 풀)

### 4.5 Hermes 의 합의 결과 처리 권한

**원칙**: Hermes 는 합의 결과를 **기록**만 가능, **승인 주체**가 될 수 없음.

| 처리 권한 | Hermes 단독 가능? | 메커니즘 |
|---------|-------------|--------|
| 합의 진행 orchestrate | ✅ | Layer 5 Hermes 책임 |
| 합의 결과 본문 보존 | ❌ Hermes 가 *수정 가능 형태* 보존 금지 | git commit 으로 immutable 보존 (system-identity-prequel §3.3 #2) |
| 합의 결과 commit author | ❌ Hermes-originated commit auto-reject (Hermes 관련 결정 한정) | git pre-commit hook + audit log |
| 합의 결과 적용 (예: G1b PASS status 갱신) | ❌ 사용자 명시 commit 만 권위 인정 | filesystem read-only + 사용자 명시 결정 강제 |
| 합의 결과 사용자에게 전달 | ✅ user-facing UI 직접 전달 가능 | system-identity-prequel §3.3 #2 |
| 합의 결과를 다음 작업에 *참조* | ✅ read-only 참조 가능 | Hermes Memory read |

### 4.6 본 §4 가 *하지 않는* 것

- ❌ 모든 합의의 풀 3+1 강제 (단축 합의도 본 §4.4.1 조건 충족 시 적격)
- ❌ 외부 LLM 모든 합의 필수 (격상 통합 합의 + 정책 변경 시만 필수)
- ❌ Hermes 합의 orchestration 자체 금지 (orchestration 은 §2.1 #4 허용 권한)

### 4.7 본 §4 의 메타-순환 청산 (C-E 흡수 — 2026-05-09 후속 2)

> **본 §4.7 은 합의 보고서 §11.2 P1 조건 C-E 흡수** (출처: Claude C-5). 본 §4 ("합의 인프라 순환 권위 해결") 의 *자기 적용 한계* 를 *메타-순환* 으로 명시 기록한다. **§4 자체가 §4 적용 대상이 될 때 어떤 한계가 발생하는지** 정직 노출.

#### 4.7.1 메타-순환 사례

본 G3 정의 문서 (현 본문) 가 *DRAFT 작성 + Reviewer-only 단축 검토 (2026-05-07) → 풀 3+1 정식 PASS 합의 (2026-05-09)* 절차로 정식 PASS 되었다. 이 절차에서 다음 *메타-순환* 이 발생:

| # | 메타-순환 | 발생 시점 | 청산 방법 |
|---|---------|--------|--------|
| (a) | **§4.4.2 외부 LLM 권장/필수** 자체가 본 §4.4.2 가 *작성된* 시점에 외부 LLM 검증 없이 작성됨 (G2 / G3 / G4 DRAFT 모두 단일 사용자 + Claude 패밀리 컨텍스트) | 2026-05-07 ~ 2026-05-09 DRAFT 작성 단계 | 2026-05-09 정식 PASS 합의 시점에 GPT (cross-vendor) + Claude (인접 컨텍스트) **2건 수령 후** PASS 발생 — *사후 외부 LLM 충족* 으로 청산 |
| (b) | **§4.3 매트릭스 "Hermes 관련 결정 = 풀 3+1 + 외부 LLM 권장"** 자체가 Hermes-orchestrated 합의 *없이* 결정됨 (Hermes PMO 미격상 시점) | 2026-05-07 §4 작성 시점 | 격상 *전* 합의는 Hermes-orchestrated 가 아니므로 §4.3 자기적용 대상 *아님* (사용자 + Claude 메인 컨텍스트 합의) — 본 §4.3 은 격상 *후* 적용 |
| (c) | **§4.4.1 단축 합의 적격 조건** 자체가 §4.4.1 패턴으로 결정됨 — *circular* | 2026-05-07 §4 작성 시점 | 본 G3 정식 PASS 시점에 풀 3+1 + 외부 LLM 2건으로 *재검증* — §4.4.1 패턴 사용 적격성 사후 확인 |
| (d) | **본 §4.7 자체** 가 본 G3 정의 문서 정식 PASS *후* 작성되며, 이는 G3 PASS 후 본문 변경에 해당 — `governance-preconditions.md` §10.2 G2 PASS 후 *변경 0건* 명시와의 정합성 점검 필요 | 2026-05-09 후속 2 | 본 §4.7 변경은 P1 조건 C-E (PASS 합의 §11.2) 흡수로 PASS 합의 권위 *내부* 변경 — 합의 보고서 권위 답습 (별도 §4 전체 재합의 *불필요*) |

#### 4.7.2 메타-순환의 청산 원칙

본 §4 자기 적용의 메타-순환은 다음 4 원칙으로 *허용·청산* 된다:

1. **사후 외부 LLM 충족**: §4.4.2 적용 시점은 *DRAFT* 까지 면제, *정식 PASS* 시점에 외부 LLM 의무 강제 (본 §4 정식 PASS = 2026-05-09 GPT + Claude 2건 충족)
2. **격상 전 면제**: §4.3 / §4.5 의 "Hermes 관련 결정" 은 *Hermes PMO 격상 후* 만 적용 (격상 전 합의는 사용자 + Claude 메인 컨텍스트로 충분)
3. **합의 권위 내부 변경**: 합의 보고서가 *변경을 합의로 권위화* 한 경우 (현 §4.7 = C-E 흡수), 합의 보고서 권위 답습으로 별도 §4 전체 재합의 *불필요* — 단, 본 변경 자체가 다음 합의 (PR-2) 에서 점검 대상
4. **자기 작성 한계 명시 의무**: 본 §4.7 처럼 *자기 적용 메타-순환* 은 명시 기록 — 묵시 통과 금지

#### 4.7.3 본 §4.7 이 *하지 않는* 것

- ❌ 본 §4 무력화 (메타-순환은 *청산* 이지 §4 폐기 아님)
- ❌ 향후 모든 합의에서 외부 LLM 면제 (§4.4.2 본문은 그대로 유효)
- ❌ Hermes 자기 격상 / 자기 PASS 의 정당화 (§4.3 매트릭스 그대로 유효)

#### 4.7.4 본 §4.7 의 외부 LLM 검증 한계 (자기 명시)

본 §4.7 자체는 **PR-1 단축 합의 (Reviewer-only)** 시점에 작성됨 — 외부 LLM 0건. 이는 *PR-1 본문 보강 = 단축 합의 적격* (사용자 결정 2: 본문 = 단축) 답습. 본 §4.7 의 외부 LLM 검증은 **PR-2 풀 3+1** 또는 **P2 v3 정식 채택 합의 (cross-vendor 추가)** 시점에 사후 충족 가능 (본 §4.7.2 원칙 #1 답습).

---

## 5. Evidence 결정 원칙 운영 규칙화

### 5.1 5단계 명제 (영구 권위 인용)

```
Agent proposes.    (에이전트가 제안한다)
Hermes orchestrates. (Hermes는 조율한다 — 격상 후)
Tools verify.      (도구가 검증한다 — 계산적 우선)
Evidence decides.  (증거가 결정한다 — 기록 없으면 PASS 미성립)
Human overrides.   (사람이 최종 방향을 선택한다)
```

본 5단계는 **system-identity-prequel §6.1** 명제이며, 합의 §112 풀 3+1 합의로 GPT 핵심 원칙 4건에 흡수. 본 §5 는 이를 *운영 규칙*으로 변환.

### 5.2 운영 규칙 (5단계 → 5 운영 규칙)

#### 5.2.1 규칙 #1 (Agent proposes)

- Worker Agent 가 작업 결과 / 결론 / PASS 판정을 **제안**할 수 있다
- 제안 자체는 PASS 가 아니며, **§5.3 PASS 성립 요건 충족 후만 PASS** 가 된다

#### 5.2.2 규칙 #2 (Hermes orchestrates — 격상 후)

- Hermes 는 합의 진행 + Worker 호출 + Evidence 위치 정리를 **orchestrate** 할 수 있다 (§2.1 #1, #4, #5)
- Hermes 는 PASS 를 **제안** 할 수 있다 (§2.1 #6 답습)
- Hermes 는 PASS 를 *결정* 할 수 없다 (§5.3 답습)
- 격상 전 (현 시점) Hermes 의 orchestrate 책임은 ADR-008 합의 자동화 + R-6 CI 자동 회귀 검증으로 한정 (P2 v3 §2.4 답습)

#### 5.2.3 규칙 #3 (Tools verify)

- 모든 PASS 판정은 **Tools 검증 통과** 가 의무 (Layer 1~4)
- Tools 검증 실패 시 PASS 미성립 + 자동 reject
- Tools 종류: 린터 / 타입체커 / 테스트 / canary / SQLCipher trigger / depcruise / gitleaks / hook 결과 등

#### 5.2.4 규칙 #4 (Evidence decides)

- **Harness Gate 와 Evidence 가 없으면 PASS 는 성립하지 않는다** (§1.3 답습)
- Evidence Ledger 기록 의무 (Markdown + JSONL append-only)
- Evidence 변조 방지: hash chain 또는 git append commit (system-identity-prequel §6.3)
- Evidence 없는 PASS 시도 → 자동 reject (§1.3 + §2.2 #13)

#### 5.2.5 규칙 #5 (Human overrides)

- **사용자는 최종 격상 / 정책 변경을 승인한다** (T2 / T3 결정 권한)
- 사용자는 Tools / Evidence 결과를 override 가능 (단 ADR Amendment 절차)
- Hermes 는 사용자 override 를 자동 reject 시도 금지 (§2.2 #22)
- 사용자 override 자체도 audit log 기록 의무 (system-identity-prequel §3.3 #3)

### 5.3 PASS 성립 요건 (Hard Rule, §1.3 강화)

**모든 PASS 판정은 다음을 *모두* 충족해야 한다**:

| # | 요건 | 검증 |
|---|------|-----|
| (i) | Tools 검증 통과 | Layer 1~4 hook + CI 결과 |
| (ii) | Evidence Ledger entry 존재 | JSONL append-only + hash chain |
| (iii) | (T2/T3 영역) 사용자 명시 승인 | 사용자 commit author 또는 명시 결정 |
| (iv) | (해당 시) 합의 보고서 commit | `docs/review/` git commit |

**미충족 시**:
- (i) 미충족 → Layer 1~4 hook 자동 차단
- (ii) 미충족 → ledger 검증 step 자동 차단
- (iii) 미충족 → T2/T3 영역에서 자동 reject + 사용자 alert
- (iv) 미충족 (해당 영역) → PASS verdict 본문에 합의 cross-reference 부재로 본 §5.3 위반

### 5.4 사용자 Override 절차

| 시나리오 | 절차 | Evidence |
|---------|-----|--------|
| Tools 검증 결과를 override | 사용자 명시 결정 + audit log + Evidence Ledger entry (`event: override`) | override commit + audit |
| Evidence 없는 PASS 를 override (예: 비상 상황) | 사용자 명시 결정 + 사후 ADR Amendment 절차 | override commit + 사후 ADR |
| 합의 결과를 override | 사용자 명시 결정 + 사후 풀 3+1 합의 (T3 영역) | override commit + 사후 합의 보고서 |

**Hermes 의 사용자 override 처리**:
- Hermes 는 사용자 override 를 자동 reject 시도 금지 (§2.2 #22)
- Hermes 는 사용자 override 본문을 *기록* 만 가능
- Hermes 는 사용자 override 결과를 다음 작업에 *반영* (T1 자동 학습)

### 5.5 SPOF Accepted Risk — 1인 동일 호스트 권한 모델 의도적 수용 (C-F 흡수 — 2026-05-09 후속 2)

> **본 §5.5 는 합의 보고서 §11.2 P1 조건 C-F 흡수** (출처: Claude C-6). 본 §5 운영 규칙의 *전제 조건* 인 "사용자 = 단일 인격 + 단일 호스트" 의 SPOF (Single Point of Failure) 위험을 **의도적으로 수용** 하고, *multi-host / 다인 운영 전환 시 추가 layer 의무 발동 트리거* 를 명시 기록한다.

#### 5.5.1 현 SPOF 의 형태

본 G3 + G2 + G4 + Constitution + ADR 의 권위 위계 운영은 다음 단일 인격·단일 호스트 모델을 *전제* 한다:

| 층 | 현 모델 | SPOF 위험 |
|----|------|--------|
| Constitution / ADR / SDD 변경 권한 | 단일 사용자 (`jokwangwon` git author) | 사용자 호스트 침해 시 모든 권위 위계 우회 가능 |
| 합의 보고서 commit author | 동일 사용자 | Hermes-originated commit auto-reject (§2.2 #20) 의 *기준* 자체가 단일 author 비교 |
| 사용자 명시 결정 (T2 / T3) | 단일 사용자 명시 | 사용자 호스트의 키체인 / SSH key / GPG key 침해 시 자동 승인 위장 가능 |
| Evidence Ledger 보존 | 단일 git 저장소 + 단일 GitHub remote | 저장소 탈취 시 ledger 변조 가능 (hash chain 보강 후에도 origin replace 위험) |
| 외부 LLM 의뢰·응답 회수 | 단일 사용자 → 외부 LLM 직접 의뢰 | 사용자 호스트 침해 시 외부 LLM 응답 위조 가능 |
| Hermes container 호스트 | 단일 호스트 (현 시점) | 호스트 침해 시 filesystem read-only mount 우회 가능 |

#### 5.5.2 의도적 수용 사유

본 SPOF 는 **의도적으로 수용** 된다. 사유:

1. **프로젝트 성격**: 본 프로젝트는 "AI Development Company OS 메타-템플릿" — 1인 개발자 / 소규모 팀 시작 전제 (CONTEXT.md 답습)
2. **MVP 범위**: 4 Worker Agent + 2 Memory + 단일 호스트 가 MVP 범위 (system-identity-prequel §8 답습)
3. **운영 단순성**: multi-host / 다인 권한 분리 = 운영 부담 增 (Hermes PMO 격상 합의의 R-8 위험과 동일 카테고리)
4. **점진 전환**: SPOF → multi-layer 전환은 *Hermes PMO 격상 후* 별도 합의로 추진 (Implementation/Runtime PASS 영역)

#### 5.5.3 Multi-host / 다인 전환 트리거 (의무 발동 조건)

다음 *조건 중 하나* 충족 시 본 SPOF 모델은 *자동 무효화* 되고, 추가 layer 의무 발동:

| # | 트리거 | 의무 발동 layer | 시점 |
|---|------|----------|-----|
| (1) | 두 번째 사용자 (다른 git author) 가 본 저장소에 commit 시도 | 사용자별 GPG signed commit 강제 + branch protection multi-author 룰 + ADR Amendment 절차 | 즉시 |
| (2) | Hermes container 가 두 번째 호스트로 분산 | 분산 host 간 mutual TLS + 정책 파일 distributed read-only (예: signed manifest) + audit log 분산 sync | 분산 진입 시점 |
| (3) | Production 환경 (단일 사용자 노트북 → 클라우드 / 공용 인프라) 전환 | secrets vault (Hashicorp / AWS Secrets Manager 등) + KMS-backed encryption + multi-stakeholder 승인 | 환경 전환 시점 |
| (4) | 외부 LLM 의뢰·응답 자동화 (사용자 직접 회수 → API 자동) | API key 분리 보관 + 응답 signed manifest + 외부 LLM 응답 hash 검증 | 자동화 진입 시점 |
| (5) | Hermes PMO 격상 (4 게이트 모두 Implementation/Runtime PASS) | 격상 합의 자체에 본 §5.5 multi-layer 전환 PASS 동시 충족 의무 (Claude C-3 + C-6 답습) | 격상 합의 시점 |

**조건 미충족 시 (현 시점)**: 본 §5.5 의 5 트리거 *중 어느 것도 충족 안 됨* → 현 SPOF 모델 *유효*. 단, 본 §5.5 자체가 "의도적 수용" 의 *명시 기록* 으로 책무 분리 (Claude C-6 권고 답습).

#### 5.5.4 본 §5.5 가 *하지 않는* 것

- ❌ SPOF 정당화 (본 §5.5 는 *수용 + 트리거 명시* 까지, 정당화는 §5.5.2 사유 한정)
- ❌ Multi-host 전환 의무 강제 (본 §5.5 는 *의무 발동 조건* 명시까지, 실 multi-layer 구현은 별도 합의)
- ❌ 사용자 호스트 침해 자동 감지 (현 시점 hook 미구현)
- ❌ Hermes PMO 격상 자동 활성화 (격상은 사용자 명시 + 별도 합의)

#### 5.5.5 G2 §9.5 / 본 §4.7 와의 인터페이스

- **G2 §9.5**: 본 SPOF 의 *6 GP 무결성 보호 측면* 인터페이스 (자기참조 차단의 제한 = 단일 사용자 의존)
- **본 §4.7**: 본 SPOF 의 *합의 인프라 순환 권위 측면* (자기 작성 + 외부 LLM 사후 충족 모델은 단일 사용자 모델 전제)
- **본 §5.5**: 본 SPOF 의 *Evidence + override + Tools verify 운영 측면* (현 §5.5)

3 §은 동일 SPOF 의 *3 측면* — 어느 하나만 보강해도 SPOF 자체는 완전 해소되지 않음. 본 §5.5.3 트리거 5건 *전부* 또는 별도 합의로만 SPOF 해소.

---

## 6. G2 인터페이스 (GP-2 ~ GP-6)

> **본 §6 은 G2 (GP-2 ~ GP-6) 의 *형식·메커니즘* 을 G3 의 *권한·신뢰* 책임과 연결한다.** 본 §6 은 **G2 PASS 선언을 트리거하지 않는다** (사용자 명시 답습).

### 6.1 GP-2 Egress Redaction ↔ G3 정책 무결성

**G2 GP-2 책임** (`governance-preconditions.md` §4): 로그 / LLM 송신 경로의 redaction *동작* (Hermes native + P1 facade 보조).

**G3 책임** (본 §6.1): redaction *정책* 자체의 *변경* 차단 (T3 영역).

| 측면 | G2 GP-2 | G3 |
|------|--------|----|
| Redaction 동작 | ✅ Tier-1 catalog 적용 + base64 evasion test | (위임) |
| Redaction 정책 변경 차단 | (위임) | ✅ §3.1 Learning silent drift + §2.2 #19 |
| 자동 회귀 검증 | ✅ R-6 workflow + log canary inject step (GP-2 산출 후보) | (위임) |
| 정책 변경 감지 hook | (위임) | ✅ filesystem read-only on `redaction-policy.yaml` + T3 변경 감지 hook |

**인터페이스**: GP-2 가 redaction *작동*, G3 가 redaction *정책 무결성*. 두 인터페이스 모두 충족 시 redaction 차단의 *완결성* 확보.

### 6.2 GP-3 Credential / Secret Hygiene ↔ G3 권한 변경 차단

**G2 GP-3 책임** (`governance-preconditions.md` §5): credential 노출 차단 (저장 docker secret + chmod 600 + entrypoint stat + inotify, 코드 gitleaks + pre-commit hook).

**G3 책임** (본 §6.2): credential 변경 *권한* 자체의 차단 + Hermes-originated 변경 audit.

| 측면 | G2 GP-3 | G3 |
|------|--------|----|
| Credential 노출 차단 (런타임) | ✅ docker secret + chmod + inotify | (위임) |
| Credential 노출 차단 (코드) | ✅ gitleaks + pre-commit | (위임) |
| Credential *변경 권한* 차단 | (위임) | ✅ §2.2 #9 (정책 자동 변경) + audit log |
| 사용자 승인 강제 | (위임) | ✅ §4.4.3 + §5.2.5 (Human overrides) |

**인터페이스**: GP-3 가 credential *노출* 차단, G3 가 credential *변경 권한* 차단. 두 인터페이스 모두 충족 시 credential hygiene 의 *완결성* 확보.

### 6.3 GP-4 외부 입력 검증 ↔ G3 검증 권위 강제

**G2 GP-4 책임** (`governance-preconditions.md` §6): Hermes / Worker 출력 + LLM 응답 + tool output 을 외부 입력으로 분류 + sanitizer / schema validation / escape 강제.

**G3 책임** (본 §6.3): "Hermes 출력은 Tools 로 검증된다" *권위 자체* 강제 (ADR-011 §2.3 운영 함의 #1).

| 측면 | G2 GP-4 | G3 |
|------|--------|----|
| 검증 메커니즘 (sanitizer / schema / escape) | ✅ tool wrapper + pydantic | (위임) |
| Reviewer prompt injection 감지 | ✅ Layer 5 보조 | (위임) |
| 검증 *권위* 강제 (Hermes 출력은 Tools 위에 위치 안 함) | (위임) | ✅ §1.2.2 + §2.2 #22 |
| 검증 우회 시도 차단 | (위임) | ✅ §1.2.2 wrapper layer BLOCK + audit |

**인터페이스**: GP-4 가 검증 *메커니즘*, G3 가 검증 *권위*. 두 인터페이스 모두 충족 시 외부 입력 검증의 *완결성* 확보.

### 6.4 GP-5 Provider Adapter ↔ G3 Hermes-originated lock-in 변경 차단

**G2 GP-5 책임** (`governance-preconditions.md` §7): Hermes / litellm / anthropic / openai 직접 import + 모델명 분기 코드 *생성* 차단 (depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject).

**G3 책임** (본 §6.4): Hermes-originated lock-in *변경 시도* 자체 차단 (Hermes plugin / Worker code 의 P1 facade 우회 PR 자동 reject).

| 측면 | G2 GP-5 | G3 |
|------|--------|----|
| 코드 lock-in 차단 (depcruise) | ✅ depcruise 룰 + PR auto-reject | (위임) |
| P1 facade 단일 진입점 강제 | ✅ P1 v2 + depcruise | (위임) |
| Hermes-originated lock-in 변경 시도 차단 | (위임) | ✅ §2.2 #18 + git pre-commit hook on Hermes-originated commit |
| 사용자 명시 결정 강제 (P1 facade 우회 시) | (위임) | ✅ §4.4.3 |

**인터페이스**: GP-5 가 *모든 lock-in* 차단 (코드 작성 주체 무관), G3 가 *Hermes-originated lock-in* 차단 (작성 주체 = Hermes 한정). 두 인터페이스 모두 충족 시 Provider Liquidity 의 *완결성* 확보.

### 6.5 GP-6 Memory / Skill Migration ↔ G3 권한 + Promotion + Escalation 차단

**G2 GP-6 책임** (`governance-preconditions.md` §8): Memory / Skill 의 *마이그레이션 가능성* (JSONL 표준 + 변환 스크립트 + 라운드트립 검증).

**G3 책임** (본 §6.5):
1. Memory / Skill *신뢰 boundary* 정의 — 누가 신뢰할 수 있는가
2. Memory / Skill *promotion 권한* — 누구에게 있는가
3. Skill *권한 escalation 차단* (§3.3 답습)

| 측면 | G2 GP-6 (Migration) | G3 (권한 + Promotion + Escalation) | G4 (형식 + Schema, 본 G3 §7 위임) |
|------|------------|------|------|
| JSONL 형식 + 변환 스크립트 | ✅ | (위임) | (G4 와 공동) |
| 라운드트립 검증 | ✅ R2-5 답습 | (위임) | (G4 와 공동) |
| Memory promotion (Project → Global) **manual only** | (위임) | ✅ §2.2 #15 | (위임) |
| Skill 등록 **T2 사용자 명시 승인** | (위임) | ✅ §2.2 #16 | (위임) |
| Skill 권한 escalation 차단 | (위임) | ✅ §3.3 답습 | (위임) |
| Memory / Skill schema 정의 | (위임) | (위임) | ✅ G4 책임 |
| Memory / Skill export / import 구조 | ✅ Migration 측면 | (위임) | ✅ Schema 측면 |

**인터페이스**: GP-6 = Migration *가능성*, G3 = *권한* + *Promotion* + *Escalation*, G4 = *형식* + *Schema*. **3-way 인터페이스** — 모두 충족 시 Memory/Skill 의 *완결성* 확보. (본 §7 G4 경계도 답습)

### 6.6 §6 통합 — G2 ↔ G3 책임 분리 매트릭스

| 영역 | G2 (메커니즘 / 동작) | G3 (권한 / 신뢰 / 무결성) |
|------|------------------|------------------|
| Redaction | GP-2 동작 | §6.1 정책 무결성 |
| Credential | GP-3 노출 차단 | §6.2 변경 권한 차단 |
| 외부 입력 검증 | GP-4 sanitizer / schema | §6.3 검증 권위 강제 |
| Provider Adapter | GP-5 코드 lock-in 차단 (모든 작성 주체) | §6.4 Hermes-originated 변경 차단 |
| Memory / Skill | GP-6 마이그레이션 가능성 | §6.5 권한 + Promotion + Escalation |

→ G2 와 G3 는 *동작/메커니즘* vs *권한/신뢰/무결성* 의 보완 관계. 두 게이트 모두 PASS 시 (4 게이트 통합 합의 후) 격상 충분 조건 일부 충족.

### 6.7 본 §6 이 *하지 않는* 것

- ❌ G2 PASS 선언 (사용자 명시 답습)
- ❌ G2 GP-2 ~ GP-6 의 *형식*까지 본 §6 에서 정의 (각 GP 본문은 `governance-preconditions.md` 에 위임)
- ❌ G4 책임 영역 본문 (본 §7 + G4 작성 시점)

---

## 7. G4 경계

### 7.1 G3 책임 (본 문서)

| 책임 | 본 G3 위치 |
|------|----------|
| 누가 memory / skill 을 신뢰할 수 있는가 (trust boundary) | §1.2 + §2.1 #2 + §6.5 |
| Skill promotion 권한은 누구에게 있는가 | §2.2 #16 + §4.3 (T2) + §6.5 |
| Memory promotion 권한은 누구에게 있는가 | §2.2 #15 + §4.3 (T2) + §6.5 |
| Skill 권한 escalation 을 어떻게 막는가 | §3.3 |
| Memory / Skill 변경의 audit log | §1.2.1 + §2.2 #20 |
| 사용자 override 처리 | §5.4 |

### 7.2 G4 책임 (별도 문서, 본 G3 범위 외)

| 책임 | G4 산출 후보 |
|------|----------|
| Memory / Skill 데이터 형식 (Markdown / JSONL / YAML) | `docs/architecture/memory-scope-design.md` |
| Skill 정의 schema (`skill.yaml`) | `docs/architecture/skill-format-design.md` |
| Export / import 구조 | `scripts/hermes-migration/*` 사양 |
| Provider-agnostic schema | 신규 ADR 후보 (ADR-014, P2 v3 §6.7 등록) |
| 다른 오케스트레이터로의 변환 형식 | G4 + GP-6 공동 |

### 7.3 G3 ↔ G4 공동 인터페이스

| 항목 | G3 측면 | G4 측면 |
|------|--------|--------|
| Memory boundary | ✅ Project → Global manual only (권한) | ✅ Project / Global 디렉토리 형식 + 환경변수 |
| Skill 등록 | ✅ T2 사용자 명시 승인 (권한) | ✅ skill.yaml schema (형식) |
| Skill 권한 등급 | ✅ wrapper 검증 + escalation 차단 (권한) | ✅ skill.yaml `permissions` 필드 (형식) |
| Memory / Skill 변경 audit | ✅ audit log JSONL append-only (권한) | ✅ log entry schema (형식) |
| 메타-템플릿 복사 시 오염 방지 | ✅ promotion manual only (권한) | ✅ `.gitignore` + init script (형식) |

**원칙**: G3 = *누가/무엇을 할 수 있는가* (권한 / 신뢰 / 무결성). G4 = *어떻게 표현되는가* (형식 / schema / export-import). 두 게이트는 **권한 ↔ 형식** 보완 관계.

### 7.4 본 §7 이 *하지 않는* 것

- ❌ G4 PASS 선언 (사용자 명시 답습)
- ❌ G4 산출 (`memory-scope-design.md` / `skill-format-design.md` / ADR-014) 본문 작성 — G4 작업 시점
- ❌ G4 형식 결정 (G3 책임 외)

---

## 8. 통합 Entry / Exit 기준

### 8.1 G3 통합 Entry

- ✅ ADR-011 §2.3 권위 확정 (2026-05-06, 충족됨)
- ✅ G1b PASS (2026-05-07, 충족됨)
- ✅ G2 DRAFT 적격 검토 APPROVE (2026-05-07, 충족됨)
- ⏳ 사용자 명시 G3 작업 진입 결정 (현 단계 — 본 초안 작성)

### 8.2 G3 통합 Exit (본 §1 ~ §7 (a)~(e) 충족)

각 §의 Exit 기준 (a)~(e) 패턴은 ADR-011 §2.1 (a)~(d) + 합의 APPROVE (e) 답습:

| § | 운영 메커니즘 | (a) 동등 결과 | (b) PoC | (c) ADR / SDD 권위 | (d) 자동 회귀 | (e) 합의 |
|---|------------|----------|--------|----------------|------------|--------|
| §1 권위 위계 운영 | 충돌 해결 매트릭스 + Evidence 없는 PASS 차단 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| §2 Hermes 권한 제한 | 22 권한 항목 + 분류 매트릭스 + 강제 메커니즘 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| §3 Silent drift / breakage / escalation | 3 위험 × 5 측면 정의 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| §4 합의 인프라 순환 권위 | 매트릭스 + 외부 LLM 조건 + 사용자 승인 조건 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| §5 Evidence 결정 원칙 | 5 운영 규칙 + PASS 성립 요건 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| §6 G2 인터페이스 | 5 GP × G3 책임 분리 매트릭스 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| §7 G4 경계 | 권한 ↔ 형식 분리 매트릭스 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

**G3 PASS 조건**:
- §1 ~ §7 모든 Exit 기준 (a)~(e) 충족
- G2 / G4 와의 통합 합의 (단축 또는 풀 3+1, **본 §4 자기참조 차단 답습** — 외부 LLM 의견 권장)
- 합의 보고서 (격상 통합 합의 시 외부 LLM 1+ 필수)

**G3 PASS 합의 형태 후보** (사용자 결정, 본 초안은 *권고 단정 금지*):
- 옵션 1: §1 ~ §7 각각 별도 단축 합의 → 7 합의 보고서 + G3 통합 합의 1건
- 옵션 2: §1 ~ §7 통합 풀 3+1 합의 1건 (외부 LLM 권장)
- 옵션 3: G2 + G3 + G4 통합 풀 3+1 합의 1건 + 외부 LLM 1+ (PR 묶음, **격상 통합 합의 답습**)

**참고**: 옵션 3 은 P2 v3 §9.2 옵션 A / G2 §10.2 옵션 3 답습. 사용자 결정 시 정당.

### 8.3 G3 통합 Exit *선언* 절차 (사용자 명시 답습)

본 G3 PASS 합의 APPROVE 시점에 다음이 *발생*:
- ✅ G3 status: ADR-011 §2.3 권위 확정 + 운영 구현 미작성 → PASS (CONTEXT.md 4 게이트 진행 상태 갱신)
- ✅ 본 문서 헤더 "DRAFT" 제거 + 합의 보고서 cross-reference 추가
- ✅ ADR-008 / ADR-011 cross-reference 갱신 (별도 PR)

본 G3 PASS 합의 APPROVE 시점에 *발생하지 않는* 것:
- ❌ G2 / G4 자동 PASS
- ❌ Hermes PMO 격상 자동 활성화
- ❌ P2 v3 정식 채택 자동
- ❌ system-identity-prequel.md / P2 v2 자동 archive
- ❌ ADR-011 §2.3 본문 자동 갱신 (cross-reference 만)

---

## 9. 영구 핵심 제약 (변동 없음)

본 G3 작업 + G3 PASS + Hermes PMO 격상(미래) 전 과정에서 다음은 **무조건 영구 유지**:

| 제약 | 권위 근거 | 본 G3 보호 위치 |
|------|---------|----------|
| **Provider Liquidity** | 헌법 5조 (관용) + `feedback_provider_liquidity.md` + ADR-008 본문 | §2.2 #18 + §6.4 |
| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위) | 본 G3 전체 (특히 §1 + §4 + §5) |
| **메타포 강제 금지** | system-identity-prequel §7 (P2 v3 §10 흡수) | 본 §0.2 + §10 변경 절차 |
| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 | §2.2 #9 #11 #14 #17 #19 #21 등 |
| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) → 본 §8.2 (a)~(e) 패턴 답습 | §8.2 |

본 5건 제약은 본 §2.2 22 금지 권한 + §3 3 위험 차단 + §4 자기참조 차단 + §5 Evidence 결정 원칙으로 **다중 보호**.

---

## 10. 본 초안의 변경 절차

본 G3 운영 구현 설계 초안은 DRAFT 상태에서 다음 절차를 따른다:

| 변경 유형 | 절차 |
|---------|------|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 |
| §1 ~ §7 본문 갱신 (운영 구현 정의) | 단축 합의 (Reviewer-only) |
| §2.2 22 금지 권한 표 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |
| §4.3 합의 형태 매트릭스 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 자기참조 차단의 핵심) |
| §5 Evidence 결정 원칙 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — system-identity-prequel §6.1 영구 명제) |
| §6 / §7 G2 / G4 인터페이스 갱신 | 단축 합의 (Reviewer-only) — G2 / G4 진행 상태 변경 시 |
| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** + 각 § (a)~(e) Exit 기준 충족 검증. **본 §4 자기참조 차단 답습 — 외부 LLM 의견 권장** |
| §9 영구 핵심 제약 변경 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |

---

## 11. 메타 편향 자기진단

본 초안은 다음 5 통제 수단을 명시 답습한다:

1. **사용자 명시 절차 답습**: G3 PASS 선언 / G2·G4 PASS 선언 / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 런타임 코드 구현 모두 본 초안 범위 외 (§0.2).
2. **R-7 SOP §0 핵심 선언 답습**: 각 § Exit 기준 (a)~(e) 5조건은 ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e) 패턴 답습 — 본 초안이 새 권위 구조 트리거하지 않음.
3. **ADR-011 §2.4 T1/T2/T3 답습**: §2.3 권한 항목 분류 (T1 8 / T2 2 / T3 12), §3 3 위험 사용자 승인 조건, §4.3 매트릭스 모두 T1/T2/T3 분류 답습.
4. **수단/목적 분리 원칙 답습**: §2.4 강제 메커니즘 매트릭스 (계산적 22/22 우선) + 각 § (a)~(e) Exit 기준 모두 *본질=결과* 우선, *수단*은 (a)~(e) 검증 후 채택.
5. **본 초안이 *하지 않는* 것 명시 (§0.2 + §8.3 + §11.3)**: 9건 명시 부정.

본 5 통제는 P2 v3 DRAFT 검토 5 통제 + G1b PASS 단축 합의 5 통제 + G2 DRAFT 검토 5 통제 답습 — G2 → G3 → G4 → Hermes PMO 격상 전 과정 동일 패턴 유지.

### 11.1 본 초안의 메타 한계

- 본 초안은 *자기 작성 산출* (P2 v3 / G2 / G3 모두 동일 컨텍스트). 외부 Reviewer 검토는 본 초안 대체 불가. **특히 G3 는 합의 인프라 순환 권위 자체를 다루므로 외부 LLM 의견 권장 (§4.4.2)**.
- §2.2 22 금지 권한 enumeration 은 *본 초안 원안* — 합의 §52 ("Hermes 금지 8가지") 의 8 항목 enumeration 도 합의 보고서에 명시되지 않아, 본 §2.2 22 항목이 *원안*. 후속 합의에서 분류 / 매핑 적정성 검증 대상.
- §3 3 위험 차단 메커니즘은 *본 초안 원안* — G2 단축 검토 §3.1 P-1 권고를 답습했으나 *각 위험의 5 측면 정의*는 본 초안이 처음. 후속 합의 검증 대상.
- §4.3 합의 형태 매트릭스는 *본 초안 원안* — system-identity-prequel §3.3 #2 + ADR-011 §2.3 / §2.4 권위 인용은 정확하나 *결정 유형별 합의 형태 매트릭스*는 본 초안이 처음. 후속 합의 검증 대상.

### 11.2 본 초안의 *PASS 판정 트리거하지 않는 것*

본 초안은 G3 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*. 다음 모두 본 초안 범위 외:
- ❌ G3 PASS 선언
- ❌ G2 / G4 PASS 선언
- ❌ Hermes PMO 격상
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신
- ❌ P2 v2 / system-identity-prequel archive
- ❌ INDEX / CONTEXT 갱신
- ❌ Phase 진입 결정
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ 실 런타임 코드 구현 (hook / wrapper / sidecar / CI step)

본 초안 정식 채택 (§10 절차) 도 *G3 PASS* 가 아니라 *G3 운영 구현 설계 문서* 의 채택 한정.

### 11.3 본 초안이 *지금 강제하는* 것 (DRAFT 상태에서도)

본 초안 자체는 *임시 권위* (DRAFT) 이지만, 다음을 *즉시 강제* 한다:

1. ADR-011 §2.3 권위 위계 + §2.4 T1/T2/T3 분류 답습 (현 시점 Hermes 책임 한정에 적용)
2. system-identity-prequel §3.3 4 강제 메커니즘 후보를 본 G3 §1 + §2 + §6 으로 흡수 (prequel archived 후에도 본 G3 권위로 보존)
3. 합의 §90 (Agent B "합의 인프라 순환 권위 역설") 흡수 (system-identity-prequel §3.3 #2 답습)
4. 메타포 강제 금지 답습 (P2 v3 §10 + 본 §0.2)

본 4건 즉시 강제는 **본 G3 가 정식 채택되지 않더라도** 현 시점에서 유효 — *Hermes 가 4 게이트 통과 전 ADR-008 합의 자동화 + R-6 CI 회귀 검증* 책임 한정으로 작동하는 현 상태에 적용.

---

**작성일**: 2026-05-07
**상태**: DRAFT (초안)
**다음 진입점**: 사용자 결정 — Reviewer-only 단축 검토 (DRAFT 적격 판정) → DRAFT 보고서 별도 commit → G4 작업 시작
**금지 (사용자 명시 답습, 변동 없음)**:
- ❌ G3 PASS 선언 자동
- ❌ G2 / G4 PASS 선언 자동
- ❌ Hermes PMO 격상 선언 자동
- ❌ P2 v3 정식 채택 자동
- ❌ ADR 본문 자동 갱신
- ❌ P2 v2 / prequel archive 자동 처리
- ❌ 실 런타임 코드 구현 (본 초안은 설계 문서까지)
