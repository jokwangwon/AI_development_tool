# ADR-008: Hermes Agent 도입 결정 (Option B)

**상태**: 승인 (3+1 합의 완료, 사용자 Option B 선택)
**날짜**: 2026-05-04
**의사결정자**: 사용자 + 3+1 에이전트 합의

---

## 맥락 (Context)

사용자가 "Hermes Agent를 메인 오케스트레이터로 도입, Claude Opus 4.7과 GPT-5.5를 서브 LLM으로 활용"하는 시스템 진화를 제안. 현재 시스템은 Claude Code 단일 의존이며, 사용자는 모델/구독 교체의 자유를 강하게 요구함 (Provider Liquidity 하드 제약: "Claude Max 사용중이지만 모델 성능에 따라 구독 취소나 모델 변경이 용이해야함").

## 결정 (Decision)

**Option B 채택**: Hermes를 메인 오케스트레이터로 단계 도입하되, **6개 차단조건이 모두 충족된 후에만 다음 Phase로 진입**한다.

### 6개 차단조건 (비협상)
1. **SQLCipher**로 Hermes SQLite 암호화 + redaction 필터 (헌법 제8조 준수)
2. **JSONL export 표준** + 메모리/스킬 마이그레이션 경로 정의 (Hermes lock-in 회피)
3. v0.x API **버전 핀** + 회귀 테스트 + 카나리 환경
4. **provider 어댑터 1개 추상화** + 분기 코드 금지 (depcruise로 강제)
5. **최소 2 provider always-on** (단일 구독 의존 금지)
6. Docker **격리 + egress 화이트리스트**

### 단계 마이그레이션
- **Phase 1** (1~2주): Hermes worktree 설치, **API 키만 사용**(OAuth 직결 금지), 비핵심 작업 검증
- **Phase 2** (2~4주): Layer 5(3+1 합의)만 Hermes 서브에이전트로 이전 (A=Claude / B=GPT / C=로컬)
- **Phase 3** (조건부): Hook 계층 watchexec 재구축 + provider 어댑터 본격 적용. **선결조건**: Phase 2 메트릭 ≥ 현 시스템

## 선택지 (Options Considered)

### Option A: LiteLLM 우선 + Hermes 좁은 PoC (3+1 권장 ★★★★★)
- 장점: Provider Liquidity 본업 충족, 기존 SDD/TDD 자산 100% 보존, 즉시 시작
- 단점: Hermes 셀프-임프루빙 가치 일부 늦게 확인

### Option B: Hermes 메인 + 6개 차단조건 단계 도입 ⭐ **채택**
- 장점: 사용자 원안 직접 실현, 셀프-임프루빙 빠른 체험
- 단점: 차단조건 6개 미충족 위험, v0.x 불안정, Hook 재구축 공수 미지수

### Option C: 6개월 보류
- 장점: 신생 프레임워크 리스크 회피
- 단점: 다중 LLM 활용·Liquidity 개선 지연

## 근거 (Rationale)

3+1 합의는 Option A를 1순위로 권장했으나, 사용자가 의식적으로 Option B를 선택. 사용자 의지·선호 존중. 단, 6개 차단조건은 **비협상** — 미충족 시 자동 NO-GO하며, Hermes 도입을 중단하고 Option A로 자동 폴백한다.

## 3+1 에이전트 합의 결과

| 에이전트 | 의견 | 핵심 근거 |
|---------|------|----------|
| Agent A (구현) | 조건부 GO | 8-Layer 통합 MEDIUM, Phase 1·2 즉시 가능, Phase 3는 Hook 재구축 PoC 성공 시 |
| Agent B (품질) | GO with strict conditions | R1 학습루프 평문(CRITICAL), R2 Hermes lock-in(CRITICAL), 6개 차단조건 미충족 시 HOLD |
| Agent C (대안) | LiteLLM 우선 권장 (Option A) | Liquidity는 도구 추상화 문제, Hermes만의 솔루션 아님 |
| **Reviewer** | **Option A 1순위, B는 차단조건 충족 시 가능** | 메타 한계 보정으로 C에 가중치, 사용자 선호 시 B 진행 가능 |

## CRITICAL 위험 (운영 중 상시 감시)

- **R1 학습루프 평문 누적**: Hermes SQLite FTS5에 사용자 컨텍스트·LLM 응답·환경변수 echo가 평문 영구 저장. **헌법 제8조 직접 위반**. 차단조건 #1 미구현 시 자동 NO-GO.
- **R2 Hermes 자체 lock-in**: 누적 학습 결과(스킬/메모리/프로필)는 Hermes 떠나면 손실. Provider Liquidity 정신 위반. 차단조건 #2 미정의 시 자동 NO-GO.
- **A-meta ChatGPT Pro Codex CLI OAuth ToS 위반 가능성**: 위반 시 구독 강제 해지 → 시스템 정지. **API 키 경로만 사용**.
- **R4 Claude Max OAuth race**: 다수 미해결 버그(#15080, #6475, #12905, #10575) — Hermes 동시 호출 시 무한 인증루프 가능. API 키 경로 우선.
- **R8 단일 구독 의존**: 어떤 단계에서도 single point of failure 금지. 차단조건 #5로 강제.

## 메타 한계 (사용자 인지 필요)

본 합의는 3 Claude 에이전트가 작성. Hermes(외부 도구)에 대한 평가에 친화 편향 가능. Reviewer가 Agent C 회의적 입장에 의식적 가중치 부여로 보정함. Option B 진행 중에도 외부(비-Claude) 검증 권장.

## 결과 (Consequences)

- **긍정적**: 다중 LLM 환경 구축, 셀프-임프루빙 학습루프 도입 시도, Provider Liquidity 강제 메커니즘 정착
- **부정적**: 신생 프레임워크 리스크 감수, Hook 재구축 공수 발생, v0.x API 변동 대응 부담, R1/R2 차단조건 미충족 시 전면 폴백 위험
- **주의사항**:
  - 6개 차단조건 중 1개라도 미충족 시 도입 중단 → Option A 자동 폴백
  - 진행 중에도 정기적 재평가 (Phase 종료마다)
  - 차단조건 충족 검증은 별도 SDD 문서로 명세 예정
  - Provider Liquidity 위반 패턴 6종(모델명 분기/provider별 후처리/스킬 내 모델 가정 등)은 depcruise 룰로 정적 차단

---

**관련 문서** (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only):

### 합의 보고서 / 헌법

- `docs/review/3plus1-consensus-2026-05-04-hermes.md` (3+1 합의 보고서 전문)
- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
- `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` (Provider Liquidity 영구 기억)

### Hermes 도입 설계 (P2)

- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건. archive 합의: `docs/review/3plus1-consensus-2026-05-09-p2-v2-archive-decision.md`)
- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — P2 v2 §2.1.3 가정 (외부 pre-record hook) 폐기 + R-2~R-7 evidence 흡수 + G1b PASS 권위 + Hermes PMO 구조 사전 정의 (활성화 *아님*) + G2/G3/G4 entry/exit. **본 ADR-008 의 Option B 단계 마이그레이션은 P2 v3 §2.6 + §11.1 + §2.6.1 12 조건 PMO 격상 체크리스트로 운영 절차화** (인간 전문 리뷰 의무 명문화, P2 v3 §2.6 단계 5.5)
- `docs/architecture/system-identity-prequel.md` (**Archived 2026-05-09 후속 8** — AI Dev Company OS 정체성 직접 권위 출처 영구 보존. archive 합의: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md`)

### Provider 추상화 / Adapter (차단조건 #4)

- `docs/architecture/llm-providers-design.md` (P1 v2, LiteLLM facade — Option β 채택)
- **`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`** (C-N 갱신 2026-05-09 후속 4 — P1 facade MVP 진입조건 명시 + **Hermes PMO ↔ provider 분리 영구 권위 (§2.3)** + **Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1 (§5)** + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference). 본 ADR-008 차단조건 #4 (provider 어댑터 추상화) 의 *Hermes PMO ↔ provider 분리* 권위 출처

### 차단조건 #1 충족 (수단/목적 분리)

- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-008 부록 B Amendment R1 specific 갱신의 권위 근거. §2.1 (a)~(d) 4조건 + §2.2 G1a/G1b 분리 + §2.3 Hermes ≠ root of trust 영구 권위 + §2.4 T1/T2/T3 영구 권위)
- `docs/decisions/ADR-010-sqlcipher-vault-key-management.md` (SQLCipher Vault HSM 키 관리 — 차단조건 #1 키 관리 측면)

### Evidence 무결성 (2026-05-09 후속 3 PR-2 신규 발행)

- **`docs/decisions/ADR-012-evidence-ledger-protection.md`** (Evidence Ledger Protection — 본 ADR-008 차단조건 #2 (JSONL export 표준) 의 *Evidence Ledger 무결성* 강화 권위. 12 보호 원칙 + Layer 1~5 다층 강제 + RFC 8785 JCS + Hermes 변조 차단 매트릭스 4항목 + Provider Liquidity 5-way Layer 5)
- 신규 위반 경로 P10 (Evidence Forgery) 정식 등록 (G2 §1.2.6, 2026-05-09 후속 5)

### 4 게이트 정식 산출 (2026-05-09 Design/Governance Gate PASS Bundled)

- `docs/architecture/governance-preconditions.md` (G2, **Design/Governance Gate PASS Bundled, 2026-05-09**) — 6 거버넌스 사전조건 GP-1~GP-6 + §1.2.6 P10 Evidence Forgery 정식 등록. **GP-1 = G1b PASS evidence 흡수 (Implementation/Runtime PASS), GP-2~GP-6 = Design PASS / Implementation Pending**
- `docs/architecture/hermes-not-root-of-trust-runtime.md` (G3, **Design/Governance Gate PASS Bundled**) — 권위 위계 운영 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + Hermes 변조 차단 매트릭스 4항목. **운영 구현 = Design PASS / Implementation Pending**
- `docs/architecture/provider-agnostic-memory-skill-design.md` (G4, **Design/Governance Gate PASS Bundled** + §4.2 11 필드 schema + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강 PR-2). **라운드트립 + migration script = Design PASS / Implementation Pending**
- `docs/phase0/redaction-verification-sop.md` (R-7 SOP — G1b PASS 정식 충족 절차)

### 부록 B §B.6 정식 충족 절차 cross-reference (G1b PASS + G2 GP-1 흡수)

- 부록 B §B.6 R-3 ~ R-7 6단계 ✅ 완료 (2026-05-06 ~ 2026-05-07 Part 1) + R-6 GitHub Actions actual run `25482284523` PASS (24초, 42/42, leak 0) + R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only (2026-05-07) → G1b CONDITIONALLY PASS → **PASS** 승격 + Phase 1 acceptance PARTIAL → **PASS** 선언. **G2 GP-1 = G1b PASS evidence 흡수** (Tier-1 한정, 2026-05-09 G2 정식 PASS 시점)

---

## 부록 A — 검증 결과 (2026-05-04)

Phase 1 진입 전 사실 확인 작업 2건 완료. 결과 CRITICAL 위험 2건이 다운그레이드되었으나, 차단조건 6개는 그대로 유지(방어 자세).

### A.1 ChatGPT Pro Codex CLI ToS 검증
- **공식 지원**: Hermes는 OpenAI Codex `device code` OAuth flow를 정식 지원. credentials는 `~/.hermes/auth.json`에 저장, `~/.codex/auth.json`에서 import 가능
- **개인 단일 사용자 시나리오**: ToS 위반 위험 **LOW** — Codex CLI 자체와 동등 사용
- **금지 사례**: "Reselling access" 또는 "third-party services에 ChatGPT 전력 공급". 본 프로젝트는 개인 사용이므로 해당 없음
- **정책 변동성**: OpenAI/Anthropic가 third-party 도구의 구독 집계를 최근 제한한 사례 존재 → API 키 경로 우선 정책은 그대로 유지
- **A-meta 위험 등급**: CRITICAL → **MEDIUM** (정책 변동 모니터링 필요)

### A.2 Hermes JSONL Export 검증
- **공식 명령어**: `hermes sessions export backup.jsonl` 존재. 전체/플랫폼별/단일 세션 export 지원, full message history 포함
- **데이터 저장소 정정**: ChromaDB는 사용하지 않음. **SQLite + FTS5 단일** — 암호화는 SQLCipher 단일 적용으로 충분 (차단조건 #1 단순화)
- **마이그레이션 도구**: `hermes claw migrate` (OpenClaw → Hermes) 존재. 역방향 export는 sessions 단위로 가능
- **스키마 버전 관리**: `schema_version` 테이블 존재
- **R2 위험 등급**: CRITICAL → **HIGH** (skills/memory 범위는 P1 설계 단계에서 추가 검증)
- **추가 검증 항목**: `hermes sessions export`가 sessions만 다루는지, agent-curated memory와 skills도 포함하는지 P1에서 확인 필요

### A.3 차단조건 영향
6개 차단조건은 **그대로 유지**. 검증 결과는 충족 가능성을 높였을 뿐 의무를 약화하지 않음.
- #1 SQLCipher: 적용 대상이 SQLite 단일 → 구현 단순화
- #2 JSONL export: 공식 명령어 활용. skills/memory 범위 보강 필요
- #3 버전 핀: 그대로
- #4 어댑터 추상화: 그대로 (P1 설계의 핵심)
- #5 2 provider always-on: 그대로
- #6 Docker 격리: 그대로

---

## 부록 B — Amendment (2026-05-06): R1 해석 갱신 (수단/목적 분리)

**상태**: 갱신 (단축 합의 — Reviewer-only)
**날짜**: 2026-05-06
**근거 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
**근거 Phase 0 evidence**: R-1 FAIL (`docs/phase0/day2-r1-redaction-location-verification.md`), R-2 PASS (`docs/phase0/day3-r2-sqlite-trigger-poc.md`)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`

### B.1 R1 비협상 핵심 재정의

R1의 비협상 핵심은 **특정 외부 hook 구현이 아니라, AI 학습 루프/메모리 DB에 비밀값이 평문으로 영구 저장되지 않도록 차단하는 결과**이다.

본 Amendment 이전 부록 A R1 텍스트는 "외부 pre-record hook"을 수단으로 가정한 표현을 포함했다. 본 Amendment는 그 가정을 ADR-011 §2.1 수단/목적 분리 원칙에 따라 갱신한다.

### B.2 G1a / G1b 분리 관리

Hermes native redaction이 DB INSERT 경로에 적용된다는 기존 가정은 **R-1에서 FAIL로 판정**되었다.

그러나 R-2 PoC에서 SQLCipher BEFORE INSERT trigger 기반 DB-level fallback이 plaintext secret persistence를 차단할 수 있음이 실증되었으므로, G1은 다음과 같이 분리 관리한다:

- **G1a**: Hermes native redaction applies before DB INSERT — **FAIL** (폐기)
- **G1b**: DB-level fallback prevents plaintext secret persistence — **PASS by R-2 PoC** (정식 충족은 R-3~R-7 후)

정식 충족 조건은 ADR-011 §2.2 G1b 정식 충족 조건 표를 따른다.

### B.3 권위화 출처

이 해석은 **ADR-011 Means-vs-Ends Redaction Principle**에 의해 권위화된다. 본 Amendment는 ADR-011 §2.1~§2.3을 ADR-008 R1 specific 갱신으로 적용한 것이며, 일반 원칙 본문 해석은 ADR-011을 우선 참조한다.

### B.4 본 Amendment의 의미 (오해 방지)

본 Amendment는 "Hermes가 안전하다"는 선언이 **아니다**. 정확한 의미는 다음과 같다:

1. Hermes native redaction은 DB INSERT 보호 수단으로 **신뢰하지 않는다**.
2. DB INSERT 경로는 SQLCipher trigger 기반 fallback으로 **별도 보호한다**.
3. **Hermes는 root of trust가 아니다** (ADR-011 §2.3 권위 위계 명문화).

### B.5 6 차단조건 영향

ADR-008 결정 본문 §6 차단조건 #1 (SQLCipher + redaction 필터) 의 충족 메커니즘은 다음으로 갱신된다:

| 메커니즘 | 위치 | 신뢰도 |
|---------|------|------|
| SQLCipher 암호화 (디스크) | DB 파일 | 기존대로 |
| Hermes native redaction | 로그 / LLM 송신 / 도구 출력 | 보조 (DB 차단 책임 없음) |
| **SQLCipher BEFORE INSERT trigger + REGEXP UDF** | **DB INSERT 경로** | **Primary (G1b)** |

차단조건 #2~#6은 변경 없음. 6 차단조건 자체의 비협상성은 유지된다 — 본 Amendment는 #1 충족 *수단*을 ADR-011 (a)~(d) 4조건 하에 재정의한 것이다.

### B.6 정식 충족 절차

차단조건 #1 정식 exit 기준은 다음 6단계 완료를 요한다 (R-4.1 은 R-4 추가 격리 PoC 분기로 ADR-011 §2.1 (b) 직접 충족 산출):

```
R-3   ✅ 본 Amendment 발행 (2026-05-06)
R-4   ✅ 패턴 동등성 비교 + gap 식별 + 보충 권고 — `docs/architecture/redaction-pattern-equivalence.md` (2026-05-06)
R-4.1 ✅ Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS — `docs/phase0/r4-1-trigger-extension-evidence.md` (2026-05-06)
R-5   ✅ canary 재검증 트리거 설계 — `docs/architecture/canary-recheck-design.md` (2026-05-06)
R-6   ✅ CI/nightly canary regression workflow 구현 — `.github/workflows/r2-canary.yml` (2026-05-06, commit `bbcc1af`; **GitHub Actions actual run 은 push 후 별도 검증 의무**)
R-7   ✅ Phase 1 합격 SOP — `docs/phase0/redaction-verification-sop.md` (2026-05-06)
```

**6단계 작성 완료 + R-6 actual run PASS + 단축 합의 APPROVE → G1b 정식 PASS 도달** (2026-05-07):

- ✅ R-6 GitHub Actions 실제 run PASS — run ID `25482284523` (commit `939125b` 기준 24초 완료, 모든 step ✓)
  - 1차 run (`25480443667`) FAIL 은 docker compose stdout prefix JSON parse infra bug — 보안 위반 / catalog drift / 실 secret 노출 / CI 자동 정책 변경 모두 *아님* (사용자 단축 합의 결정 답습). Fix `939125b` 는 workflow YAML 1 file 한정 (`r4_1_poc.py` / Tier-1 catalog / trigger UDF / redaction config 변경 0건)
- ✅ Artifact `r2-r4-canary-evidence` 본문 검증 통과 — verdict = "PASS", tier1_pass_rate = "42/42", Tier-1 42/42 BLOCK, Safe 9/9 PASS, leak_observations = [], rollback_triggered = false
- ✅ R-7 SOP §7.3 단축 합의 (Reviewer-only, ADR-011 §2.4 T2) APPROVE — `docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` (13 Reviewer 항목 + 8 PASS 조건 + 5 통제 수단 명시)
- ✅ G1b status: CONDITIONALLY PASS → **PASS** 승격
- ✅ Phase 1 acceptance: PARTIAL → **PASS** 선언

본 ADR-008 부록 B.6 갱신은 ADR-011 §2.4 T2 절차 (사용자 승인 + Reviewer-only 단축 합의) 답습. **자동 승격 아님**.

R-4 / R-4.1 / R-5 / R-6 / R-7 진행 상태는 본 Amendment 가 아니라 ADR-011 §2.2 표 또는 `docs/CONTEXT.md` 의 4 게이트 진행 상태에서 추적한다.

본 G1b PASS 는 *4 게이트 중 G1b 한정* — Hermes PMO 격상은 G2 / G3 / G4 추가 통과 후 별도 결정 (본 Amendment 범위 외).

---

## 부록 C — Hermes PMO Activation Cross-Reference (2026-05-09 후속 13 신설)

**상태**: 신설 (단축 합의 — Reviewer-only)
**날짜**: 2026-05-09 후속 13
**근거 합의**: `docs/review/3plus1-consensus-2026-05-09-adr-008-update-pmo-activation-cross-ref.md` (Reviewer-only 단축 합의 APPROVE — 7 항목 분류 + 6/6 풀 3+1 승격 트리거 0건 발화)
**근거 권위**:
- P2 v3 §2.6 (격상 절차 7 단계) + §2.6.1 (12 조건 PMO 격상 체크리스트) + §11.1 (Hermes PMO 격상 전 인간 전문 리뷰 의무화)
- ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위, 2026-05-09 후속 4)
- ADR-011 §2.3 (Hermes ≠ root of trust) + §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리)
- ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목, 2026-05-09 후속 3 PR-2)
- G2 §1.2.6 (P10 Evidence Forgery 정식 등록, 2026-05-09 후속 5)
- G3 §1.3 + §5 (Evidence decision principle: PASS 성립 4 요건)
- G4 §4 (Memory/Skill JSONL hash chain + Tier-based round-trip)
- 본 ADR-008 §결정 단계 마이그레이션 + 부록 B Amendment

**ADR-013 대체 권위**: 본 부록 C = ADR-013 (Hermes PMO Activation 영구 권위) 신규 발행 *대체* (`docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` §1.1.3 답습 — ADR-013 현 시점 발행 보류).

### C.1 본 부록 C 의 의미 (오해 방지)

> **본 부록 C 는 Hermes PMO 격상 *선언이 아니다*.**
>
> 본 부록 C 는 P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 의 *Hermes PMO 격상 조건 cross-reference 강화* 한정. 8 권위 layer 중첩 답습으로 *영구 권위 정착 가능* 하나, *현 시점 격상 발생 0건*.

본 부록 C 의 정확한 의미는 다음과 같다:

1. P2 v3 정식 채택 (2026-05-09 후속 6) = **Design Adoption only** — Hermes PMO Activation 미발생 (P2 v3 §2 Non-Activation Clause 답습)
2. 본 부록 C 는 *Hermes PMO 격상 조건* 명시 강화 + ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 + P2 v3 *cross-reference* 매트릭스 제공
3. **Hermes PMO 격상 자체는 §C.6 절차 답습 후 *별도 결정* 영역**

### C.2 Hermes PMO 격상 12 조건 체크리스트 (P2 v3 §2.6.1 직접 답습)

본 §C.2 는 P2 v3 §2.6.1 PMO 격상 체크리스트 (12 조건) 의 *ADR 권위 정착 cross-reference*.

| # | PMO 격상 조건 | 권위 출처 | 현 상태 (2026-05-09 후속 13) |
|---|------|----|----|
| 1 | G1b Implementation/Runtime PASS | 본 ADR-008 부록 B + R-7 SOP §7.3 | ✅ 2026-05-07 |
| 2 | GP-1 (G1b 흡수) Implementation/Runtime PASS | G2 §3 + 본 ADR-008 차단조건 #1 | ✅ 2026-05-09 (G1b evidence 흡수) |
| 3 | GP-2 ~ GP-6 Implementation/Runtime PASS | G2 §4 ~ §8 + Implementation 별도 합의 | ⏳ Pending (Design PASS 만) |
| 4 | G3 runtime hooks/wrappers + Hermes 변조 차단 매트릭스 runtime | G3 §1 ~ §7 + ADR-012 §2.12 | ⏳ Pending (Design PASS 만) |
| 5 | G4 migration round-trip PASS + JSONL writer + 11 필드 schema 활성 | G4 §4.5 + §4.6 + ADR-012 §2.10 | ⏳ Pending (Design PASS 만) |
| 6 | ADR-012 evidence protection CI | ADR-012 §10.2 별도 PR (Implementation 영역) | ⏳ Pending |
| 7 | ADR-009 T1~T4 trigger detection task | ADR-009 §3.1 ~ §3.4 분기별 별도 합의 | ⏳ Pending |
| 8 | Provider Liquidity 5-way Layer 1~5 runtime 활성 (depcruise + AST 스캐너 + pre-commit hook + CI step) | C-H 별도 합의 + ADR-009 C-N §5 (Layer 1 모법) + ADR-012 §원칙 5/6 (Layer 5) + G3 §6.4 (Layer 2) + G4 §3.5/§4.3 (Layer 3/4) | ⏳ Pending |
| 9 | 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 | 합의 시점 별도 (P2 v3 §11 변경 절차 답습) | ⏳ Pending (격상 시점) |
| 10 | **인간 전문 리뷰 (Human-in-the-loop)** | P2 v3 §11.1 + §2.6 단계 5.5 + Gemini 사고모델 §7.10 #3 cross-vendor 답습 | ⏳ Pending (격상 시점) |
| 11 | 사용자 명시 격상 결정 | 합의 시점 별도 (사용자 명시 결정 권위) | ⏳ Pending |
| 12 | **ADR-008 본문 Hermes PMO 격상 절차 추가 PR** | **본 부록 C** ← 현 발행 (2026-05-09 후속 13) | ✅ **본 부록 C 발행으로 충족** |

**합산** (2026-05-09 후속 13 시점): **2/12 충족** (조건 1 G1b PASS + 조건 12 본 부록 C). **10/12 미충족** (Implementation/Runtime PASS 영역 + 합의 시점 영역). Hermes PMO 격상 *현 시점 발생 0건*.

### C.3 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 필요 조건

> **Hermes PMO 격상은 다음 조건 모두 충족 시에만 발생**:
>
> - **외부 LLM 2개** (예: GPT-5.x + Gemini cross-vendor) **또는 외부 LLM 1개 + 인간 전문 리뷰** (P2 v3 §11 + Gemini 사고모델 §7.10 #3 답습)
> - **인간 전문 리뷰 (Human-in-the-loop)** 의무 (P2 v3 §11.1 + §2.6 단계 5.5 직접 답습)
> - **사용자 명시 격상 결정** (사용자 명시 결정 권위 — 자동 결정 절대 금지)

본 §C.3 은 P2 v3 §11 변경 절차 + §2.6.1 PMO 격상 체크리스트 + Gemini 사고모델 cross-vendor 응답 §7.10 #3 *직접 인용* 답습.

### C.4 사용자 명시 결정 없이는 PMO 격상 불가 (자동 격상 절대 금지)

> **Hermes PMO 격상은 *자동 발생 절대 금지*** (ADR-011 §2.4 T3 위반).

다음 모두 충족 시에만 발생:

1. 사용자 명시 결정 (T2 사용자 승인)
2. 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰
3. 4 게이트 모두 Implementation/Runtime PASS evidence
4. Adoption decision commit
5. Evidence Ledger entry (`event: gate_pass` × 4 + `event: external_llm_received` × N + `event: human_review_completed`)

**자동 격상 시도 차단 매커니즘** (다중 layer):

| Layer | 차단 매커니즘 | 권위 |
|------|----|----|
| 1 | ADR-011 §2.4 T3 (Constitution / ADR / Harness Gates 정의 자체의 변경 = 자동 금지) | 영구 권위 |
| 2 | ADR-012 §원칙 9 (prev_hash 검증 실패 = 즉시 BLOCK, 자동 복구 / 자동 revert 금지) | 영구 권위 |
| 3 | ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 — Hermes 가 자기 격상 시도 차단) | 영구 권위 |
| 4 | ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목 — Hermes-originated commit auto-reject) | 영구 권위 |
| 5 | G3 §2.5 #11 + §4.5 + §2.2 #20 (filesystem ACL on `governance-preconditions.md` / `hermes-not-root-of-trust-runtime.md` / `provider-agnostic-memory-skill-design.md` / `ADR-008-*.md` (본 ADR) / Evidence Ledger / 합의 보고서 등 + Hermes-originated commit auto-reject + audit log) | 영구 권위 |

→ **5 layer 다중 차단** (자동 격상 시도 모든 경로 차단).

### C.5 Implementation/Runtime PASS 와 Design/Governance PASS 분리

본 §C.5 는 P2 v3 §3.1.4 Implementation Pending 표 직접 답습 + Hermes PMO Activation 영역 추가:

| 영역 | Design/Governance PASS | Implementation/Runtime PASS |
|------|----|----|
| G1b DB-level fallback | (해당 없음) | ✅ 2026-05-07 (R-7 SOP §7.3 단축 합의) |
| G2 GP-1 (G1b 흡수) | ✅ Bundled 2026-05-09 | ✅ 2026-05-09 (G1b evidence 흡수, Tier-1 한정) |
| **G2 GP-2 ~ GP-6** | ✅ Bundled 2026-05-09 | ⏳ **Pending** |
| **G3 운영 구현** | ✅ Bundled 2026-05-09 | ⏳ **Pending** |
| **G4 migration / round-trip** | ✅ Bundled 2026-05-09 | ⏳ **Pending** |
| ADR-012 CI enforcement | (해당 없음) | ⏳ **Pending** |
| ADR-009 T1~T4 trigger detection | (해당 없음) | ⏳ **Pending** |
| Provider Liquidity 5-way Layer 1~5 runtime | (해당 없음) | ⏳ **Pending** |
| Hermes 변조 차단 매트릭스 4항목 runtime | (해당 없음) | ⏳ **Pending** |
| **Hermes PMO Activation** | ❌ **Not authorized** | ❌ **Not authorized — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM + 인간 전문 리뷰 + 사용자 명시 결정 후** |

**합산** (2026-05-09 후속 13 시점):
- Design/Governance PASS = **4/4** (G1b PASS + G2 + G3 + G4 Bundled)
- Implementation/Runtime PASS = **2/4** (G1b + GP-1 만 — G1b evidence 흡수)
- **Hermes PMO Activation = 0** (Not authorized)

P2 v3 정식 채택 = *Design Adoption only* (Implementation PASS 미발생). 본 부록 C 발행 = ADR 권위 정착 한정 (격상 발생 0건).

### C.6 ADR-013 현 시점 발행 보류 사유

> **ADR-013 (Hermes PMO Activation 영구 권위) 신규 발행은 *현 시점 보류***.

**근거**: `docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` §1.1.3 답습 — 8 권위 layer 중첩 답습 충족:

1. P2 v3 §2.6 (격상 절차 7 단계)
2. P2 v3 §11.1 (인간 전문 리뷰 의무화)
3. P2 v3 §2.6.1 (12 조건 PMO 격상 체크리스트)
4. **본 부록 C** (현 발행 — ADR-013 대체 권위)
5. ADR-008 부록 B Amendment (R-3 시점 + R1 specific 갱신)
6. ADR-011 §2.3 (Hermes ≠ root of trust 영구 권위)
7. ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위)
8. ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목)

**ADR-013 신규 발행 시점 후보** (조건부 — 별도 합의 + 풀 3+1 + 외부 LLM 1+ 의무):

- (a) **Hermes PMO 격상 적격성 검토 시점** (4 게이트 모두 Implementation/Runtime PASS 후) — 본 부록 C 답습으로 ADR-008 본문 갱신 *충분* 시 ADR-013 *불필요* 가능
- (b) **영구 ADR 권위 정착 사용자 결정 시점** — 사용자가 ADR-008 부록 vs ADR-013 신규 분리 결정
- (c) **외부 LLM 권고 발생 시** (cross-vendor 의견 추가에서 ADR-013 권위 정착 권고)

### C.7 cross-reference 매트릭스 (사용자 명시 항목 7 답습)

| 권위 | cross-reference 영역 |
|----|----|
| **ADR-009 C-N §2.3** (Hermes PMO ↔ provider 분리 영구 권위) | 본 §C.4 #3 + §C.5 |
| **ADR-009 C-N §5** (Provider Liquidity 5-way Layer 1 모법 ADR) | 본 §C.5 (Provider Liquidity 5-way Layer 1) |
| **ADR-011 §2.3** (Hermes ≠ root of trust 영구 권위) | 본 §C.4 권위 위계 + §C.6 ADR-013 보류 사유 #6 |
| **ADR-011 §2.4** (T1/T2/T3 자동 학습 vs 정책 변경 분리) | 본 §C.4 #1 (T3 자동 금지) |
| **ADR-012 §2.12** (Hermes 변조 차단 매트릭스 4항목) | 본 §C.4 #4 + §C.5 (Hermes 변조 차단 매트릭스 runtime) |
| **ADR-012 §원칙 5 / §원칙 6** (Provider Liquidity 5-way Layer 5 — Evidence 형식 차원) | 본 §C.5 (Provider Liquidity 5-way Layer 5) |
| **ADR-012 §원칙 9** (자동 정책 변경 금지) | 본 §C.4 #2 |
| **G2 §1.2.6 P10** (Evidence Forgery 정식 등록) | 본 §C.5 (P10 Evidence Forgery 정식 등록 — Evidence Integrity) |
| **G3 §1.3 + §5** (Evidence decision principle: PASS 성립 4 요건) | 본 §C.4 (Adoption decision commit + Evidence Ledger entry) |
| **G3 §2.5 #11 + §4.5 + §2.2 #20** (Hermes-originated commit auto-reject + filesystem ACL + audit log) | 본 §C.4 #5 (5 layer 다중 차단 Layer 5) |
| **G4 §4.2 (11 필드) + §4.4 (Layer 1~5 hash chain) + §4.6 (Tier-based round-trip)** | 본 §C.5 (G4 migration / round-trip — ADR-012 §2.1~§3.5 답습) |
| **P2 v3 §2** (Hermes PMO 구조) + §2.6 (격상 절차 7 단계) + §2.6.1 (12 조건 체크리스트) + §11.1 (인간 전문 리뷰 의무화) + §10.1 (Normative Constraints) + §10.2 (Archive Migration Note) | 본 부록 C 전체 (직접 답습) |

### C.8 본 부록 C 가 *발생시키는* 것 / *발생시키지 않는* 것

#### C.8.1 *발생시키는* 것 (cross-reference 강화 한정)

- ✅ ADR-008 부록 C 신설 (Hermes PMO Activation Cross-Reference)
- ✅ P2 v3 §2.6.1 12 조건 체크리스트의 ADR 권위 정착
- ✅ ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 + P2 v3 cross-reference 보강
- ✅ ADR-013 신규 발행 *대체* 권위 정착 (사용자 명시 답습)
- ✅ Hermes PMO 격상 *조건* 명시 강화 (격상 *발생* 0건)
- ✅ 5 layer 다중 차단 매트릭스 명시 (자동 격상 시도 차단)
- ✅ Implementation/Runtime PASS ↔ Design/Governance PASS 분리 매트릭스 명시

#### C.8.2 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ G2 / G3 / G4 Implementation PASS 자동 선언
- ❌ ADR-013 신규 발행 (사용자 명시 금지 — 본 부록 C 대체)
- ❌ ADR-014 신규 발행
- ❌ ADR-008 §결정 본문 변경 (Option B / 6 차단조건 / 단계 마이그레이션 모두 변경 0건)
- ❌ 부록 B Amendment 본문 변경
- ❌ P2 v3 §2.6.1 12 조건 완화 또는 강화 (변경 0건 — 직접 답습)
- ❌ 실 runtime code / migration script / hook 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장

본 부록 C 발행은 ADR-011 §2.4 T2 절차 (사용자 승인 + Reviewer-only 단축 합의) 답습 — *자동 격상 아님*. 본 부록 C 자체가 *Hermes PMO 격상 조건* 명시 강화 한정.
