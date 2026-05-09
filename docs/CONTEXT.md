# 프로젝트 컨텍스트 (Project Context)

> **AI 에이전트가 세션 시작 시 반드시 읽어야 하는 현재 상태 문서**

**최종 업데이트**: 2026-05-10 (**Group B 통합 PoC 종료 — G3 Hermes-originated marker + Evidence 없는 PASS 차단 Reviewer-only 단축 합의 APPROVE WITH CONDITIONS**). 본 세션 누적 12 commits (`35cbf4b → df4de14`):

- **Group A 1차 PoC** (Layer 1 형식 차단): `tools/provider_import_scanner.py` (AST 5종 패턴) + 1차 fixture (PASS×1+FAIL×5) + CI workflow + Reviewer-only 단축 합의 APPROVE
- **Group A 2차 PoC** (Layer 1 정적 그래프 강화): 풀 3+1 합의 (T-2 import-linter 채택, C-1~C-10 + TR-1~TR-5) → C-9 RA-9 사전 검증 PASS → `.importlinter` + `requirements-dev.txt` + `src/` placeholder + `transitive_import.py` fixture + CI 양방향 step + Reviewer-only 단축 합의 APPROVE WITH CONDITIONS
- **Group A 보완**: G-1 (CI probe cleanup `if: always()`) + G-2 (`.gitignore` 4 패턴 추가) + G-3 (C-9 venv 정리)
- **Group B 통합 PoC** (G3 — commits `ecf9da3` + `4872a11` + `df4de14`, GitHub Actions actual run `25605665191` PASS 8초 conclusion=success): `tools/evidence_pass_gate.py` (3 검사 — Hermes marker × governance 공동 / PASS × evidence / Implementation PASS scope 분리) + fixture (PASS × 2 + FAIL × 4, 3 패턴 cover) + CI workflow (PASS rc=0 / FAIL rc=1 ≥4 + 3 패턴 cover step + Evidence summary) + 사양 + Reviewer-only 단축 합의. 양방향 검증 5/5 PASS (로컬 + actual run, FP 0 / FN 0). ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 8 PASS / 6 BLOCK / 7 금지 0/7 위반 + escalation TR-B-1~TR-B-4 0/4 발화

**Implementation/Runtime PASS 자동 선언 미발생** + **Hermes PMO 격상 0건** + **G2 GP-5 6 금지목록 0/6 위반** + **G3 7 금지목록 0/7 위반** + **신규 정책 발명 0건** + **ADR 본문 변경 0건**. 본 세션 = G2 GP-5 *부분 충족 시제* + G3 *부분 충족 시제* 한정 (G2/G3 전체 PASS 권한 없음 — 사용자 명시 답습). 자세한 세션 로그는 `docs/sessions/SESSION_2026-05-10.md`.

**다음 진입점**: Group C (G4 JSONL hash chain + RFC 8785 JCS + round-trip PoC) — JCS 라이브러리 선정 / test corpus / PoC 범위 결정 *먼저* 진행 (사용자 명시 답습). 또는 Group A 3차 (URL/endpoint grep PoC, C-8) / Group D (G2 GP-3 + GP-2). 사용자 명시 결정.

**이전 업데이트**: 2026-05-10 (Group A 단단 종료 — G2 GP-5 1차+2차+보완 PoC 모두 APPROVE WITH CONDITIONS)

### C-14 cross-vendor 응답 7+4 핵심 조건 — P2 v3 정식 채택 합의 전 체크리스트 (사용자 명시 답습)

본 §은 **C-14 cross-vendor blind 의뢰 응답 2건 (`2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response.md` + `-response-gemini.md`) 의 11 핵심 조건** (응답 1 = 7건 + 응답 2 Gemini = 4건) 을 P2 v3 정식 채택 합의 *전* 흡수 의무 체크리스트로 추적. 본 추적은 P2 v3 정식 채택 풀 3+1 합의 §11.2 권위 내부 작업 영역.

**응답 1 (vendor 자기 명시 부재) 7 조건**:

| # | 조건 | 흡수 위치 | 상태 |
|---|----|--------|---|
| 1 | P2 v3 §3 dual-structure (DRAFT Snapshot + Adoption-time Status) | P2 v3 §3 본문 갱신 (정식 채택 합의 시점) | ⏳ |
| 2 | P2 v3 정식 채택 = "Design Adoption only" 의미 제한 | P2 v3 §0.1 또는 헤더 본문 명시 | ⏳ |
| 3 | Hermes PMO non-activation clause (§2 본문 추가) | P2 v3 §2 본문 추가 | ⏳ |
| 4 | ADR-012 + G4 §4 보강 cross-reference 반영 | P2 v3 §6 + §7 cross-reference 갱신 | ⏳ |
| 5 | 영구 핵심 제약 5건 보존 문구 강화 (archive 후에도 약화 방지) | P2 v3 §10 본문 갱신 | ⏳ |
| 6 | Implementation Pending 표 명시 | P2 v3 §3 또는 §6 본문 표 추가 | ⏳ |
| 7 | 정식 채택 합의 = 단축 합의 아님, 풀 3+1 + C-14 응답 evidence 포함 | P2 v3 정식 채택 합의 형태 결정 | ✅ (본 후속 4 결정 — 풀 3+1 권고 답습) |

**응답 2 (Gemini 사고모델) 4 조건**:

| # | 조건 | 흡수 위치 | 상태 |
|---|----|--------|---|
| 1 | §3 4-게이트 상태표 2026-05-09 동기화 | P2 v3 §3 본문 갱신 (응답 1 #1과 통합) | ⏳ |
| 2 | ADR-012 완전 통합 (G4 mandatory reference) | P2 v3 §6 본문 갱신 + 응답 1 #4 통합 | ⏳ |
| 3 | **Hermes PMO 격상 전 인간 리뷰 (Human-in-the-loop) 의무화** (§11 또는 §2.6 명문화) | P2 v3 §11 또는 §2.6 본문 추가 | ⏳ |
| 4 | system-identity-prequel archive 시 영구 제약 약화 방지 검증 | P2 v3 §10 본문 갱신 (응답 1 #5와 통합) | ⏳ |

**중복 / 통합 조건 매트릭스** (응답 1 + 2 통합):

- **상태표 동기화** (응답 1 #1 + 응답 2 #1) — P2 v3 §3 본문 갱신
- **ADR-012 통합** (응답 1 #4 + 응답 2 #2) — P2 v3 §6 + §7 갱신
- **영구 제약 보존** (응답 1 #5 + 응답 2 #4) — P2 v3 §10 갱신
- **Design Adoption 분리** (응답 1 #2 + 응답 2 #3 인간 리뷰) — P2 v3 §0.1 + §2.6 + §11 갱신
- **고유 조건**: 응답 1 #3 (PMO non-activation clause §2 본문) + 응답 1 #6 (Implementation Pending 표) + 응답 2 #3 (인간 리뷰 의무화 단독)

**합산 = 11 조건 → 통합 후 7~8 본문 갱신 영역**.

본 체크리스트 = **P2 v3 정식 채택 풀 3+1 합의 §11 사용자 명시 결정 영역** — 본 11 조건 흡수 후 P2 v3 정식 채택 합의 진입 적격.

---

## 현재 활성 의사결정 (2026-05-09 종료 시점)

**Phase 0 완료 (Part 1) + 4 게이트 DRAFT 검토 모두 APPROVE (Part 2 + 본 세션) + G2/G3/G4 통합 정식 PASS (옵션 3, 본 세션 후속)** — Part 1 (G1b PASS + Phase 1 acceptance PASS) 후 사용자 명시 결정으로 P2 v3 + G2 + G3 + G4 DRAFT 작성 진입. G2/G3/G4 DRAFT 검토 APPROVE AS DRAFT (Reviewer-only). **2026-05-09 후속**: 옵션 3 (G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 1+) 채택 → Agent A/B/C (Opus 독립) + GPT (cross-vendor) + Claude (인접 컨텍스트) **5/5 입력 APPROVE WITH CONDITIONS — Design/Governance Gate PASS (Bundled)** 합의 보고서 발행 + 3 게이트 헤더 갱신. 다음 진입점은 P0 (3건) + P1 (10건) 조건 흡수 PR 묶음 결정 + P2 v3 정식 채택 합의 형태 결정 (Gemini 등 추가 cross-vendor 적용 시점 포함).

**4 게이트 합산** (2026-05-09 후속 시점):
```
G1b = PASS                                                    ✅ 2026-05-07 Part 1 승격
G2  = Design/Governance Gate PASS (Bundled, 2026-05-09)       ✅ 본 세션 정식 승격 (GP-1 PASS + GP-2~GP-6 DESIGN PASS / IMPLEMENTATION PENDING)
G3  = Design/Governance Gate PASS (Bundled, 2026-05-09)       ✅ 본 세션 정식 승격 (운영 구현 = DESIGN PASS / IMPLEMENTATION PENDING)
G4  = Design/Governance Gate PASS (Bundled, 2026-05-09)       ✅ 본 세션 정식 승격 (라운드트립 + migration script = DESIGN PASS / IMPLEMENTATION PENDING)
─────────────────────────────────────────────────────────────
4 게이트 Design/Governance Gate PASS 합산 = 4/4 (G1b PASS + G2/G3/G4 Design/Governance Gate PASS)
4 게이트 Implementation/Runtime PASS 합산 = 1/4 (G1b 만 — GP-2~GP-6 / G3 운영 / G4 라운드트립 모두 IMPLEMENTATION PENDING)
Hermes PMO 격상 선언 = 미선언 (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도 — Claude C-3 권고 답습)
```

### 합의·검증 산출 (2026-05-05 ~ 2026-05-09 누적)
- `docs/architecture/system-identity-prequel.md` (시스템 정체성 prequel — P2 v3 정식화 전 임시 선언)
- `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 3+1 합의)
- `docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` (단축 합의)
- `docs/external-review/2026-05-05-system-summary-for-gpt.md` (GPT 검토 의뢰 자료)
- `docs/phase0/day1-environment-and-fact-check.md` (Hermes v0.12.0 사실 확인)
- `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL 확정)
- `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PASS 확정)
- `docker/r2-poc/` (R-2 PoC Docker 격리 환경 + 6항목 자동 검증 스크립트)
- `docs/sessions/SESSION_2026-05-05.md` (2026-05-05 세션 로그)
- **`docs/decisions/ADR-011-means-vs-ends-redaction.md` (R-3 신규 — 수단/목적 분리 원칙, R-4~R-7 모법)**
- **`docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B Amendment (R-3 — R1 specific 갱신, B.6 6단계로 갱신)**
- **`docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (R-3 단축 합의 APPROVE)**
- **`docs/architecture/redaction-pattern-equivalence.md` (R-4 — 패턴 동등성 비교 + gap 식별 + 보충 권고, ADR-011 §2.1 (a) 충족)**
- **`docs/phase0/r4-1-trigger-extension-evidence.md` (R-4.1 — Tier-1 42종 trigger UDF 확장 PoC PASS evidence, ADR-011 §2.1 (b) 충족)**
- **`docker/r4-1-poc/` (R-4.1 격리 환경 코드 — Dockerfile + compose + r4_1_poc.py)**
- **`docs/architecture/canary-recheck-design.md` (R-5 — canary 재검증 트리거 설계, ADR-011 §2.4 운영 메커니즘)**
- **`.github/workflows/r2-canary.yml` (R-6 — CI/nightly canary regression workflow, ADR-011 §2.1 (d) 자동 회귀 검증 경로)**
- **`docs/phase0/redaction-verification-sop.md` (R-7 — Phase 1 acceptance SOP, ADR-008 부록 B.6 마지막 단계, 2026-05-07 갱신 G1b PASS)**
- **`docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` (R-7 SOP §7.3 단축 합의 APPROVE — G1b PASS 승격 + Phase 1 acceptance PASS 선언 권위)**

#### Part 2 (2026-05-07 후속 — P2 v3 + G2 + G3 + G4 DRAFT)
- **`docs/architecture/hermes-adoption-design-v3.md` (P2 v3 DRAFT — 12 섹션, P2 v2 §2.1.3 가정 폐기 + R-2~R-7 흡수 + Hermes PMO 구조 사전 정의 + G2/G3/G4 entry/exit, commit `8f8e323`)**
- **`docs/review/3plus1-consensus-2026-05-07-p2-v3-draft.md` (P2 v3 DRAFT 단축 검토 APPROVE AS DRAFT, 7 기준 7/7 PASS, commit `12d7609`)**
- **`docs/architecture/governance-preconditions.md` (G2 DRAFT — 13 섹션, P1~P8 8 위반 경로 + GP-1~GP-6 6 사전조건 매핑 + 강제 메커니즘 분류 매트릭스 + §9 메타 안전장치 G3 인터페이스, commit `1b5bde3`)**
- **`docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md` (G2 DRAFT 단축 검토 APPROVE AS DRAFT, 10 기준 10/10 PASS, commit `957cddc`)**
- **`docs/architecture/hermes-not-root-of-trust-runtime.md` (G3 DRAFT — 11 섹션, 권위 위계 운영 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + 3 위험 5 측면 + 합의 자기참조 차단 + Evidence 결정 5 운영 규칙 + G2·G4 인터페이스, commit `9c488b1`)**
- **`docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md` (G3 DRAFT 단축 검토 APPROVE AS DRAFT, 10 기준 10/10 PASS — G3 §4 자기참조 차단의 적용 대상으로 한계 명시, commit `d42886b`)**
- **`docs/architecture/provider-agnostic-memory-skill-design.md` (G4 DRAFT — 11 섹션, 옵션 B 통합. Memory scope 4 단계 (MVP Global+Project) + Skill schema 17 필드 + JSONL export hash chain + Memory/Skill boundary 4 금지 + G3·G2 GP-6 인터페이스 + 3-way, commit `079bc6c`)**

#### 본 세션 (2026-05-09)
- **`docs/review/3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` (G4 DRAFT 단축 검토 APPROVE AS DRAFT, 10 기준 10/10 PASS + 8 금지 0건 + 5 자기 발견 잠재 위험 LOW/VERY LOW (P-1 RFC 8785 JCS / P-2 schema 진화 / P-3 schema_version declaration / P-4 §6.4 명명 / P-5 `~/.claude/global` path) — G3 §4 자기참조 차단 적용 대상 한계 명시, commit `fd10b79`)**

#### 본 세션 후속 3 (2026-05-09 후속 3 — PR-2 풀 3+1 + 외부 LLM 2건)
- **`docs/decisions/ADR-012-evidence-ledger-protection.md` (ADR-012 신규 발행 — Evidence Ledger 보호 강화. 12 보호 원칙 + 4 매트릭스 + 5 추가 의무. 11 필드 + 17 enum 후보 + Layer 1~5 다층 강제 + RFC 8785 JCS Primary + jq fallback + Genesis hash MVP+0.2 전이 + prev_hash BLOCK + manual + chain_violation_detected + Full Rewrite 5 Layer + Round-trip Tier-based + 3 ledger entry 형식 + Migration BLOCK + manual + migration_failed + Hermes 변조 차단 매트릭스 4항목 + External LLM `agent="user"` 강제 + Schema 진화 정책 + Content-level 한계 + Timestamp monotonicity + 운영 부담 monitoring trigger + Provider Liquidity 4-way → 5-way Multi-layer Defense)**
- **`docs/architecture/provider-agnostic-memory-skill-design.md` §4.2 / §4.4 / §4.6 보강 (ADR-012 동일 PR commit. schema 10 → 11 필드 + canonical RFC 8785 JCS + Genesis + prev_hash 검증 실패 + Full Rewrite + Tier-based round-trip + 3 ledger entry 형식 + Migration rollback. G4 §11.4 P-1/P-2/P-3 처리 완료)**
- **`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (PR-2 풀 3+1 + 외부 LLM 2건 합의 보고서. 5/5 입력 APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격. 16 + 4 차원 종합 판정 + 5/5 영구 핵심 제약 보호 HIGH + Gap-17 HIGH 흡수 + C-14 cross-vendor (P2 v3 진입 전) 의무 영구 답습)**
- **`docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-a-implementation.md` (Agent A 구현/운영, 481 줄, APPROVE WITH CONDITIONS 8 조건, R-6/R-7/R-11 HIGH binary)**
- **`docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-b-security.md` (Agent B 보안/거버넌스, 597 줄, APPROVE WITH CONDITIONS 4 + 14 NOTES, **Gap-17 HIGH** Hermes 변조 차단 매트릭스 4항목)**
- **`docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-c-alternatives.md` (Agent C 대안/단순화, 424 줄, APPROVE WITH CONDITIONS 4 핵심 + 6 보조)**
- **`docs/external-review/2026-05-XX-pr2-evidence-ledger-request.md` (PR-2 외부 LLM 의뢰 자료, *내부 Agent A/B/C 분석 미포함* — 의도된 편향 통제 강화)**
- **`docs/external-review/2026-05-09-pr2-evidence-ledger-response.md` (cross-vendor 외부 LLM 응답, APPROVE WITH CONDITIONS, 5 권고 + 16 차원, 11번째 = `event` + JCS primary + jq fallback)**
- **`docs/external-review/2026-05-09-pr2-evidence-ledger-response-claude.md` (Claude 인접 컨텍스트 응답, APPROVE WITH CONDITIONS 17 조건 C-1~C-17, 다층 동시 의무 + C-14 cross-vendor P2 v3 진입 전 의무)**

### 핵심 채택 사항 (R-3에서 ADR 권위로 승격)
- **정체성**: "AI Development Company OS" 메타포 (선언적, 즉시)
- **권위 위계**: `Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents` — **ADR-011 §2.3 영구 권위화**
- **Hermes ≠ root of trust** — **ADR-011 §2.3 영구 권위화** (prequel §3 → ADR 승격, prequel 폐기 후에도 보존)
- **자동 학습 ≠ 자동 정책 변경** (T1 자동 / T2 사용자 승인 / T3 절대 금지) — **ADR-011 §2.4 영구 권위화**
- **수단/목적 분리 원칙** — **ADR-011 §2.1 신설** (헌법 8조 본질 = "DB 평문 저장 차단 결과", 수단 대체에 (a)~(d) 4조건 강제)
- **Evidence 검증**: "Agent proposes / Hermes orchestrates / Tools verify / Evidence decides / Human overrides"
- **메타포 강제 금지** 조항

### MVP 범위 (Phase 1 시작 기준, 변경 없음)
- **Worker Agent 4**: PM/Orchestrator + Architect + Implementation + Reviewer
- **Memory 2단계**: Global + Project (manual promotion만)
- **Evidence**: Markdown + JSONL append-only (hash chain or git append commit으로 변조 방지)

### G1a/G1b 분리 (CRITICAL — 다음 세션 핵심 컨텍스트)

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   근거: agent/redact.py docstring "for logs and tool output", redact import 25개 모두 비-DB,
         hermes_state.py redact import 0건

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   근거: SQLCipher BEFORE INSERT trigger + REGEXP UDF로 6항목 검증 PASS
         (Docker 격리 환경, canary 5종 차단, DB 평문 부재, 에러 평문 미노출)
```

**G1b의 의미 (사용자 명시)**:
> Hermes native redaction은 로그/LLM 송신 방어로만 취급, DB INSERT 경로는 SQLCipher BEFORE INSERT trigger로 별도 차단. **Hermes를 신뢰하는 구조가 아니라 DB 레벨에서 Hermes를 보완하는 구조.**

### 4 게이트 진행 상태

| 게이트 | 정의 | 현 상태 |
|-------|------|--------|
| ~~G1a~~ | Hermes native redaction → DB | ❌ FAIL 확정 (폐기) — **ADR-011 §2.2 / ADR-008 부록 B 권위 명시** |
| **G1b** | **DB-level fallback (SQLCipher trigger)** | ✅ **PASS** (2026-05-07 Part 1 단축 합의 승격) — R-3 ~ R-7 6단계 ✅ + R-4.1 격리 PoC PASS + R-6 GitHub Actions actual run `25482284523` PASS (24초, verdict PASS, 42/42, leak 0) + Reviewer-only 단축 합의 APPROVE (`docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md`) |
| **G2** | **6 거버넌스 사전조건** | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** — `governance-preconditions.md` 헤더 갱신 + 합의 보고서 (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`, 5/5 입력 APPROVE WITH CONDITIONS). **GP-1 = PASS, GP-2~GP-6 = DESIGN PASS / IMPLEMENTATION PENDING**. Implementation/Runtime PASS 미충족 |
| **G3** | **"Hermes ≠ root of trust" 운영 구현** | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** — `hermes-not-root-of-trust-runtime.md` 헤더 갱신 + 합의 보고서. ADR-011 §2.3 권위 확정 + G3 §1~§7 설계 승인. **운영 구현 = DESIGN PASS / IMPLEMENTATION PENDING**. 외부 LLM 1+ 충족 (GPT cross-vendor + Claude 인접 컨텍스트) |
| **G4** | **Provider-agnostic Memory/Skill 형식** | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** — `provider-agnostic-memory-skill-design.md` (옵션 B 통합 문서) 헤더 갱신 + 합의 보고서. **라운드트립 + migration script = DESIGN PASS / IMPLEMENTATION PENDING**. hash chain 사양 보강 + provider_bindings lint 룰 강제는 별도 합의 |

### Phase 0 진행 상태
- ✅ Day 1 (사실 확인)
- ✅ Day 2 (R-1 FAIL)
- ✅ Day 3 (R-2 PASS, baseline 5 patterns)
- ✅ **R-3 (2026-05-06): ADR-011 발행 + ADR-008 부록 B Amendment, 단축 합의 APPROVE**
- ✅ **R-4 (2026-05-06): 패턴 동등성 비교 + gap 식별 + 보충 권고 (ADR-011 §2.1 (a) 충족)**
- ✅ **R-4.1 (2026-05-06): Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS (ADR-011 §2.1 (b) 충족, 1차 PARTIAL → 2차 PASS 진화)**
- ✅ **R-5 (2026-05-06): canary 재검증 트리거 설계 (T13 강화 + 6 trigger 시점 + 4 verdict + 4 안전장치 + Markdown+JSONL evidence + T1/T2/T3 정책 매트릭스)**
- ✅ **R-6 (2026-05-06): CI/nightly canary regression workflow (workflow_dispatch + nightly cron + push/PR + R-4.1 PoC 실행 + JSON evidence 추출 + verdict PASS 검증 + artifact 업로드, permissions: contents: read)**
- ✅ **R-7 (2026-05-06): Phase 1 acceptance SOP — 13 checklist + 4 verdict + 9 ROLLBACK + 7 Evidence + push 전/후 작업 분리**
- ✅ **R-6 actual run (2026-05-07): 1차 FAIL infra bug → fix `939125b` → 2차 run `25482284523` PASS (24초)**
- ✅ **R-7 SOP §7.3 단축 합의 (2026-05-07): Reviewer 13 항목 + 8 PASS 조건 + 5 메타 편향 통제 → APPROVE → G1b PASS 승격 + Phase 1 acceptance PASS 선언**

### 다음 세션 TODO (우선순위 순)

1. ~~**R-3 / R-4 / R-4.1 / R-5 / R-6 / R-7 + G1b PASS 승격 + Phase 1 acceptance PASS 선언**~~ ✅ 완료 (2026-05-06 ~ 2026-05-07 Part 1)
2. ~~**P2 v3 + G2 + G3 + G4 DRAFT 작성 + G2·G3 DRAFT 검토 APPROVE**~~ ✅ 완료 (2026-05-07 Part 2)
3. ~~**G4 DRAFT Reviewer-only 단축 검토 APPROVE AS DRAFT**~~ ✅ 완료 (2026-05-09, commit `fd10b79`)
4. ~~**G2/G3/G4 정식 채택 합의 (옵션 3 — 통합 풀 3+1 + 외부 LLM 1+)**~~ ✅ 완료 (2026-05-09, 5/5 입력 APPROVE WITH CONDITIONS — Design/Governance Gate PASS Bundled)
5. ~~**G2/G3/G4 헤더 갱신 + CONTEXT/INDEX 갱신 (P0 조건 C-A + C-B 흡수)**~~ ✅ 완료 (2026-05-09 후속)
6. ~~**PR-1 본문 흡수 6건 (C-D/E/F/I/K/L) + 단축 합의 보고서 (Reviewer-only)**~~ ✅ 완료 (2026-05-09 후속 2)
7. ~~**PR-2 풀 3+1 합의 (ADR-012 + G4 §4.4/§4.6 hash chain) + 외부 LLM 2건**~~ ✅ 완료 (2026-05-09 후속 3, 5/5 입력 APPROVE WITH CONDITIONS, ADR-012 발행 + G4 §4.2/§4.4/§4.6 보강)
8. ~~**C-14 cross-vendor blind 의뢰 1+ 의무**~~ ✅ 완료 (2026-05-09 후속 4, cross-vendor 응답 2건 APPROVE WITH CONDITIONS — Gemini 사고모델 + vendor 자기 명시 부재 1건. 11 핵심 조건 P2 v3 합의 전 체크리스트로 추적 — 본 §answer C-14 체크리스트)
9. ~~**C-N ADR-009 / P1 facade MVP 진입조건 명시**~~ ✅ 완료 (2026-05-09 후속 4, ADR-009 갱신 단축 합의 APPROVE — Reviewer-only. 5 영역 흡수: P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference. 자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건 + 핵심 결정 변경 0건)
10. ~~**G2 §1.2 P10 (Evidence Forgery) 정식 row 추가**~~ ✅ 완료 (2026-05-09 후속 5, 단축 합의 APPROVE Reviewer-only — 3 영역 갱신 + 4 풀 3+1 승격 트리거 0건 발화 + ADR-012 발행 권위 내부 작업)
11. ~~**P2 v3 정식 채택 풀 3+1 합의**~~ ✅ 완료 (2026-05-09 후속 6, 풀 3+1 + 외부 LLM 2건 (cross-vendor — Gemini 사고모델 + vendor 미명시) APPROVE WITH CONDITIONS — Design Adoption only 5/5 입력 일치. P2 v3 DRAFT → **Adopted** + 8 본문 영역 갱신 — §0 헤더 / §2 Non-Activation Clause / §3 dual-structure (DRAFT Snapshot + Adoption-time Status + Delta + Implementation Pending) / §6 ADR-012 Mandatory Reference / §7 ADR 매트릭스 (ADR-012 + ADR-009 C-N) / §10 Normative Constraints + §10.2 Archive Migration Note / §11 변경 절차 + §11.1 Hermes PMO 격상 전 인간 리뷰 의무화 / §2.6 격상 절차 단계 5.5 인간 전문 리뷰)
12. ~~**P2 v2 Archive 적격성 검토 + Archive 전환**~~ ✅ 완료 (2026-05-09 후속 7, 단축 합의 APPROVE Reviewer-only — 7/7 검토 기준 PASS + 5/5 풀 3+1 승격 트리거 0건 발화 + 옵션 A (최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건) 채택. P2 v2 (`hermes-adoption-design.md`) 헤더 = Archived. ADR cross-reference 깨짐 0건 + 5 영구 핵심 제약 보호 강도 HIGH 5/5 유지)
13. ~~**system-identity-prequel.md Archive 적격성 검토 + Archive 전환**~~ ✅ 완료 (2026-05-09 후속 8, 단축 합의 APPROVE Reviewer-only — 8/8 검토 기준 PASS + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 A 채택. system-identity-prequel.md 헤더 = Archived. 16 영역 이관 매트릭스 (12 완전 흡수 + 4 부분/분산) + AI Dev Company OS 정체성 보존 HIGH (§2 본문 영구 보존) + prequel §1.2 자체 archive 예고 정합. ADR-011 §2.3 / §2.4 영구 권위 승격 + ADR-012 §6.4 트리거 실현 답습)
14. ~~**ADR-008 / 010 / 011 본문 갱신 PR 묶음 *범위 결정* 검토**~~ ✅ 완료 (2026-05-09 후속 9, 단축 합의 APPROVE Reviewer-only — 6 항목 분류 + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 1 (3 ADR 단일 PR 묶음) 권고. 25 cross-reference 갱신 항목 (A1~A25 — ADR-008 9 + ADR-010 4 + ADR-011 12). **본 검토 = 범위 결정만, 본문 수정 X**. 결정 내용 변경 0건 (Option B / Vault HSM / 수단/목적 분리 모두 변경 없음). 다음 진입점: 본 검토 APPROVE 후 별도 PR/commit 으로 ADR 본문 갱신)
15. ~~**ADR-008 / 010 / 011 본문 갱신 단일 PR 묶음 commit**~~ ✅ 완료 (2026-05-09 후속 10, 옵션 1 답습 — 25 cross-reference 갱신 항목 (A1~A25) 모두 반영. ADR-008 §관련 문서 9 항목 (P2 v2 Archived / P2 v3 Adopted / ADR-009 C-N / ADR-011 / ADR-012 / G2/G3/G4 / 차단조건 #2 #4 / 부록 B §B.6) + ADR-010 §맥락 + §관련 문서 4 항목 (P2 v2 Archived / P2 v3 Adopted / ADR-012 / Evidence Ledger DB secret 처리 주의 사항) + ADR-011 §8.1/§8.2/§8.5 12 항목 (prequel Archived / P2 v2 Archived / P2 v3 Adopted / R-4~R-7 ✅ 완료 / G1b PASS / G2/G3/G4 PASS / ADR-012 / ADR-009 C-N / G2 §1.2.6 P10 / P2 v3 / Archive / 본 후속 9 등록). 결정 내용 변경 0건 + 6 풀 3+1 승격 트리거 0건 발화 (재확인) + 6 금지 사항 위반 0건)
16. ~~**G2 / G3 / G4 헤더 P2 v3 cross-reference 갱신 단축 PR**~~ ✅ 완료 (2026-05-09 후속 11, 3 게이트 헤더 영역 cross-reference 보강 — G2 = §1.2.6 P10 정식 등록 + P2 v3 §4 답습 권위 + 후속 권위 표기. G3 = Hermes 변조 차단 매트릭스 4항목 (ADR-012 §2.12 답습) + P2 v3 §5 답습 권위 + ADR-011 §2.3/§2.4 영구 권위 명시. G4 = ADR-012 Mandatory Reference + Provider Liquidity 5-way Layer 매트릭스 + ADR-009 C-N §5 모법 ADR + P2 v3 §6 답습. Design/Governance PASS ↔ Implementation Pending 분리 강화. 5 풀 3+1 승격 트리거 0건 발화 (Design vs Implementation 분리 / PMO 격상 오해 / P2 v3 의미 변경 / ADR 충돌 / 5 제약 약화). 헤더 본문 변경 0건 — cross-reference 갱신만)
17. ~~**ADR-013 / 014 후보 발행 결정 검토**~~ ✅ 완료 (2026-05-09 후속 12, 단축 합의 APPROVE Reviewer-only — 두 후보 *현 시점 발행 보류* 권고. 7 항목 분류 + 4+4 새 ADR 기준 + 5 풀 3+1 승격 트리거 0건 발화. ADR-013 (Hermes PMO Activation / Human Review / Runtime Governance) = P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008/011/012 7 권위 layer 충족, **ADR-008 본문 갱신 PR (부록 추가) 으로 대체 가능**. ADR-014 (Memory/Skill Runtime / Migration / Round-trip) = G4 + ADR-012 답습 충족 + **Implementation/Runtime PASS PoC 완료 후 발행 검토**. **본 검토 = 후보 결정만, 본문 작성 X** (사용자 명시 답습). 발행 시점 후보 enumerate (ADR-013 a/b/c + ADR-014 a/b/c) + Implementation 작업 영역 8건 + 격상 후 다뤄도 되는 영역 6건 분류)
18. ~~**ADR-008 본문 갱신 PR — 부록 C 신설 (Hermes PMO Activation Cross-Reference)**~~ ✅ 완료 (2026-05-09 후속 13, 단축 합의 APPROVE Reviewer-only — 사용자 명시 7 항목 답습 + 6 풀 3+1 승격 트리거 0건 발화. **ADR-013 신규 발행 *대체* 권위 정착**. 부록 C §C.1 의미 (오해 방지) + §C.2 12 조건 체크리스트 (P2 v3 §2.6.1 직접 답습) + §C.3 외부 LLM 2 + 인간 전문 리뷰 조건 + §C.4 자동 격상 절대 금지 (5 layer 다중 차단) + §C.5 Implementation/Runtime PASS ↔ Design/Governance PASS 분리 매트릭스 + §C.6 ADR-013 보류 사유 (8 권위 layer 답습) + §C.7 cross-reference 매트릭스 (12 권위) + §C.8 발생/미발생 enumerate. **ADR-008 §결정 본문 변경 0건**)
19. ~~**ADR-010 / ADR-011 후속 보강 필요 여부 확인**~~ ✅ 완료 (2026-05-09 후속 14, 단축 합의 APPROVE Reviewer-only — **분기 A 채택: 추가 보강 *불필요***. ADR-010 5/5 항목 충족 (Evidence Ledger DB 보호 범위 / secret 처리 / key rotation·backup·export 충돌 0건 / 책임 경계 매트릭스 명확 / Implementation PASS 오해 0건) + ADR-011 5/5 항목 충족 (수단/목적 분리 최신 / 권위 위계 archive 후 명확 / T1/T2/T3 충돌 0건 / Hermes PMO 격상 절차 연결 / 자동 정책 변경 금지 5 layer 다중 차단 강제) + 6/6 풀 3+1 승격 트리거 0건 발화. **본 검토 = 보강 필요 여부 검토만, 본문 수정 X**. **Implementation/Runtime PASS 작업 진입 적격**)
20. ~~**Implementation/Runtime PASS Roadmap 작성**~~ ✅ 완료 (2026-05-09 후속 15, 단축 합의 APPROVE Reviewer-only — `implementation-runtime-roadmap.md` DRAFT 권위 권고 발행. 17 항목 분해 (G2 5 + G3 5 + G4 7) + 9 그룹 동시 진행 분류 + 사용자 명시 8 우선순위 유지 + Claude 추가 3 항목 (Order 9~11). ADR-011 §2.1 (a)~(e) 5조건 답습 + Rollback Trigger 9 + Evidence 5 형식. 5/5 풀 3+1 승격 트리거 0건 발화. 그룹 A~G = 단축 합의 / 그룹 H (ADR-014 발행) + I (G3 22 권한 분해) = 풀 3+1 + 외부 LLM 1+ 의무. **roadmap 우선순위 자동 *고정* 0건**)
21. ~~**Group A 1차 PoC — AST scanner 기반 Layer 1 형식 차단**~~ ✅ 완료 (2026-05-09 후속, Group A 진입, commits `a3693a0` + `0f503a4`. `tools/provider_import_scanner.py` (~165줄, 5종 패턴 — direct/from/dynamic-importlib/__import__/model-name) + fixture 6건 (PASS × 1 + FAIL × 5) + CI workflow 양방향 검증 + Reviewer-only 단축 합의 APPROVE WITH CONDITIONS. 양방향 검증 5/5 패턴 정확 매칭. ADR-011 §2.1 5/5 + 6 금지목록 0/6 위반)
22. ~~**Group A 2차 PoC — depcruise rule (T-2 import-linter) 풀 3+1 합의**~~ ✅ 완료 (2026-05-10, commits `a6e82f1` + `b683e15` + `cfa0db0`. **풀 3+1 합의** — 7항목 + 4 옵션 (T-1~T-4) 분석. Agent A/B/C 독립 분석 1206줄 + Reviewer 380줄. **T-2 (import-linter) 채택** — RA-1 CRITICAL (T-1 dependency-cruiser Python 미지원 동작 불가) + RA-9 CRITICAL (grimp 외부 모듈 install 사전 검증 의무). C-1~C-10 추가 조건 + TR-1~TR-5 재합의 trigger 등록. Agent C 권고 안 #1 (보류) → 3 반박 명시 답습. APPROVE WITH CONDITIONS)
23. ~~**Group A 2차 PoC 구현**~~ ✅ 완료 (2026-05-10, commits `d7c4b05` + `4a18bcc` + `9764fd8`. **C-9 RA-9 사전 검증 PASS** — `import-linter 2.11 + grimp 3.14` 환경에서 `include_external_packages = True` 정상 동작. **핵심 발견**: `google.generativeai` 가 import-linter forbidden contract 제약 → 1차 AST scanner 단독 책무 분리 (각주 1 등재). 산출물 6건 — `.importlinter` config + `requirements-dev.txt` (TR-2 답습) + `src/` placeholder (TR-1 미발화) + `transitive_import.py` fixture + CI 갱신 + 본 PoC 사양. **양방향 검증 5/5 PASS**. Reviewer-only 단축 합의 APPROVE WITH CONDITIONS)
24. ~~**Group A 보완 — G-1/G-2/G-3 처리**~~ ✅ 완료 (2026-05-10, commit `f8018af`. CI probe cleanup `if: always()` step 분리 + `.gitignore` 4 패턴 추가 (`git check-ignore` 4/4 매치) + C-9 venv 정리. 변경 영향 0건 (도구/룰/fixture 변경 0). 보조 작업 — 별도 합의 미발화)
25. ~~**Group B 통합 PoC — G3 Hermes-originated marker + Evidence 없는 PASS 차단**~~ ✅ 완료 (2026-05-10, commits `ecf9da3` + `4872a11` + `df4de14`. GitHub Actions actual run `25605665191` PASS 8초 conclusion=success. `tools/evidence_pass_gate.py` 3 검사 (Hermes marker × governance 공동 / PASS × evidence / Implementation PASS scope 분리) + fixture (PASS × 2 + FAIL × 4, 3 패턴 cover) + CI workflow (PASS rc=0 / FAIL rc=1 ≥4 + 3 패턴 cover step + Evidence summary 6 항목) + 사양 + Reviewer-only 단축 합의 APPROVE WITH CONDITIONS. 양방향 검증 5/5 PASS (로컬 + actual run, FP 0 / FN 0). ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 8 PASS / 6 BLOCK / 7 금지 0/7 위반 + TR-B-1~TR-B-4 0/4 발화 + Group A 답습 충실 + 알려진 한계 4건 명시. 본 PoC = G3 *부분 충족 시제* 한정 (G3 전체 PASS 권한 0건))
11. **P2 v3 정식 채택 합의** (G2 §1.2 P10 정식 등록 후 진입) — **풀 3+1 합의** (C-14 응답 2건 모두 풀 3+1 권고 답습) + 본 CONTEXT C-14 체크리스트 11 조건 흡수 의무. **C-14 cross-vendor 1+ 충족 (2건) ✅** + **C-N ADR-009 갱신 ✅** 후 진입 적격
    - 시나리오 X: P2 v3 단독 합의 (풀 3+1, C-14 응답 evidence 포함)
    - 시나리오 Y: P2 v3 + ADR-013 / ADR-014 후보 통합 합의 (PR 묶음)
12. **ADR PR 묶음 (P2 v3 정식 채택 후)**: ADR-008 / ADR-009 / ADR-010 / ADR-011 cross-reference 갱신 + 신규 ADR-013 (Git·CI·external-review 보호) / ADR-014 (Provider-agnostic Memory/Skill Format) 후보 검토
13. **C-H provider_bindings lint 룰 강제 합의** (Implementation/Runtime PASS 영역, 별도 합의)
14. **R-6 workflow ledger 검증 step 추가** (Implementation/Runtime PASS 영역, ADR-012 §10.2 답습)
15. **P2 v2 / system-identity-prequel.md archive 처리** (P2 v3 정식 채택 시점에)
16. **Hermes PMO 격상 후보** (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도 — Claude C-3 답습)

**권고 시작점** (2026-05-10 Group B 종료 후): 다음 중 사용자 명시 결정 — (a) **"Group C 우선 검토 — G4 JSONL hash chain + RFC 8785 JCS + round-trip PoC"** (사용자 명시 권고, 단 JCS 라이브러리 선정 / test corpus / PoC 범위 결정 *먼저* 진행 — 바로 구현 금지) / (b) "Group A 3차 — URL/endpoint grep PoC 진입 (C-8 답습)" / (c) "Group D — G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction" / (d) "Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+)" / (e) "Group I — G3 22 권한 분해 합의 (풀 3+1)".

### 2026-05-09 후속 2 결정 사항 (사용자 명시 3건)
- **결정 1 (PR 묶음)**: 옵션 β — 2-PR 묶음 (PR-1 단축 합의 본문 보강 6건 + PR-2 풀 3+1 ADR-012 + G4 hash chain)
- **결정 2 (검토 형태)**: 본문 PR = 단축 합의 (Reviewer-only) / 신규 ADR PR = 풀 3+1 + 외부 LLM 1+
- **결정 3 (외부 LLM 추가 시점)**: P1 흡수 후 + P2 v3 정식 채택 진입 *전* (Claude C-3 권고 답습)
- **PR-1 흡수 완료** (2026-05-09 후속 2): C-D (G3 §2.2 #11) + C-E (G3 §4 메타-순환 부록) + C-F (G2 §9 + G3 §4·§5.5 SPOF) + C-I (G2 §1.2 P9~P12 부록) + C-K (G4 §3.1 + #15 격상) + C-L (G4 P-1~P-5 + G3 4건)
- **PR-2 흡수 완료** (2026-05-09 후속 3): C-C (ADR-012 신규 발행) + C-G (G4 §4.2 schema 11 필드 + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강). 5/5 입력 APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격
- **별도 후속**: C-H (Implementation PASS 영역, 별도 합의) / C-N (ADR-009 갱신 별도 PR) / **G2 §1.2 P10 정식 등록 단축 합의** (ADR-012 발행 트리거, 다음 진입점) / **C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무** (P2 v3 정식 채택 진입 *전*, 외부 LLM 2 C-14 + Claude C-3 답습)

### 잔여 (Task #16, 본 세션 미처리)
- P1 v2 minor revisions 6건 — P2 v3 작성과 병합 검토
- `.claude/settings.local.json` gitignore 처리
- 잘못된 origin/main 커밋 2개 정리

### 영구 핵심 제약
- **Provider Liquidity** (헌법 5조 비협상, `feedback_provider_liquidity.md`)
- **Hermes ≠ root of trust** (system-identity-prequel §3)
- **메타포 강제 금지** (system-identity-prequel §7)

상세: `docs/sessions/SESSION_2026-05-05.md`, `docs/architecture/system-identity-prequel.md`

---

## 프로젝트 성격

**이 프로젝트는 "AI Development Company OS 메타-템플릿"이다.**

새 아이디어로 개발을 시작할 때, 이 프로젝트의 문서/설정 파일을 가져와 적용한다.

```
사용법:
  1. 새 프로젝트 생성
  2. 이 템플릿의 파일을 복사
  3. 아이디어를 제시하면 Phase 0부터 자동화 개발 시작
```

---

## 릴리스: v1.0.0

### 포함된 설계 체계

| 문서 | ADR | 설명 |
|------|-----|------|
| 프로젝트 헌법 | — | 12개 조항 (제8-2조 환경 관리 포함) |
| 하네스 엔지니어링 설계 | — | 8-Layer 피드백 루프 |
| 3+1 멀티에이전트 설계 | — | 합의 기반 의사결정 시스템 |
| 아키텍처/코드 품질 원칙 | — | 10대 원칙 + 코드 품질 기준 |
| 자동화 검토 질문지 | ADR-001 | Phase 0: 아이디어 → 브리프 |
| 아이디어 기반 스택 결정 | ADR-002 | Phase 1: 스택 통합 결정 |
| 생성 AI 에셋 파이프라인 | ADR-003 | Guide-First 에셋 생성 |
| 생성 AI 확장성 | ADR-004 | Config 기반 모델 교체 + 학습 안내 |
| AI 백엔드 스택 가이드라인 | ADR-005 | 로컬 추론 시 Python 분리 |
| 환경 변수 + Docker-First | ADR-006 | 하드코딩 제로 + 중앙 관리 |
| 변경 영향 분석 | ADR-007 | 의존성/장애 사전 검증, 자동 분류 |
| **시스템 정체성 prequel** | — (P2 v3로 정식화 예정) | **AI Development Company OS, Hermes PMO 4 게이트, MVP 4 Agent + 2 Memory** |
| 개발 가이드 | — | SDD+TDD 워크플로우 |
| 테스트 전략 | — | 70% 커버리지 목표 |

### 개발 파이프라인 (확정)

```
Phase 0: 자동화 검토 질문지 (필수3 + 동적2)
Phase 1: 3+1 합의 (아이디어 + 스택 + 에셋 식별)
    ├── Phase 2-3: SDD → TDD (코드)
    └── 에셋 파이프라인 (비코드, Guide-First, 병렬)
Phase 4: 통합 테스트 + 배포
```

---

**이 문서는 매 세션 시작 시 반드시 읽어야 합니다.**
**상세**: `docs/sessions/SESSION_2026-05-05.md`, `docs/architecture/system-identity-prequel.md`, `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`
