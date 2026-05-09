# 프로젝트 컨텍스트 (Project Context)

> **AI 에이전트가 세션 시작 시 반드시 읽어야 하는 현재 상태 문서**

**최종 업데이트**: 2026-05-09 후속 3 (**PR-2 풀 3+1 합의 + 외부 LLM 2건 APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격** (5/5 입력 일치) + ADR-012 신규 발행 + G4 §4.2 schema 11 필드 + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강 — **다음 진입점: G2 §1.2 P10 정식 등록 단축 합의 → C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 → P2 v3 정식 채택 풀 3+1 합의**)

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
8. **G2 §1.2 P10 (Evidence Forgery) 정식 row 추가** (다음 진입점, 단축 합의 가능) — ADR-012 발행 시점 트리거 답습 + ADR-012 §1.3 cross-reference 의무. P10 정식 위반 경로 등록 = G2 §1.2 본문 변경 (T3 변경, 단축 합의 적격)
9. **C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무** (P2 v3 정식 채택 진입 *전*, 사용자 명시 결정 답습 — Claude C-3 + 외부 LLM 2 C-14)
10. **C-N ADR-009 / P1 facade MVP 진입조건 명시** (별도 PR — 단축 또는 풀 3+1)
11. **P2 v3 정식 채택 합의 형태 결정** (P0/P1/PR-2 흡수 후, 사용자 명시 결정):
    - 시나리오 X: P2 v3 단독 합의 (단축 또는 풀 3+1)
    - 시나리오 Y: P2 v3 + ADR-013 / ADR-014 후보 통합 합의 (PR 묶음)
    - C-14 cross-vendor 1+ 충족 후 진입
12. **ADR PR 묶음 (P2 v3 정식 채택 후)**: ADR-008 / ADR-009 / ADR-010 / ADR-011 cross-reference 갱신 + 신규 ADR-013 (Git·CI·external-review 보호) / ADR-014 (Provider-agnostic Memory/Skill Format) 후보 검토
13. **C-H provider_bindings lint 룰 강제 합의** (Implementation/Runtime PASS 영역, 별도 합의)
14. **R-6 workflow ledger 검증 step 추가** (Implementation/Runtime PASS 영역, ADR-012 §10.2 답습)
15. **P2 v2 / system-identity-prequel.md archive 처리** (P2 v3 정식 채택 시점에)
16. **Hermes PMO 격상 후보** (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도 — Claude C-3 답습)

**권고 시작점** (2026-05-09 후속 3 종료 후): "G2 §1.2 P10 정식 등록 단축 합의를 진행합니다 (ADR-012 발행 트리거 답습)." 또는 "C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 자료를 작성합니다 (P2 v3 정식 채택 진입 전 의무)."

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
