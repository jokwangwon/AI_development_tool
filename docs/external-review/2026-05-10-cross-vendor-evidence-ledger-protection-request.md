# Cross-vendor Blind 검토 의뢰 — Evidence Ledger 보호 모델 (ADR-012 §2.8 5 Layer 답습 5/5 완결) 후 진입점 결정 사전 검토

> **이 문서를 통째로 ChatGPT (GPT-5.x), Gemini, 또는 다른 *비-Claude* vendor 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 평가 가능하도록 작성되었습니다.
>
> **본 의뢰의 *blind 강도* 는 가장 높습니다. 본 자료에는 다음이 *의도적으로 포함되지 않습니다*:**
> - ❌ 본 프로젝트의 내부 Agent A / B / C 분석 결과
> - ❌ 본 프로젝트의 Reviewer 종합 결론
> - ❌ 의뢰자 (사용자) 가 원하는 결론 / 방향 / 선호
> - ❌ APPROVE 유도 표현 / 답안 제시 / 결론 시사
>
> 본 의뢰는 vendor 다양성 (cross-vendor) 을 통해 진정한 *제3자* 의 독립 판단을 확보하기 위함입니다. 응답은 `docs/external-review/2026-05-10-cross-vendor-evidence-ledger-protection-response{,-gemini,-claude}.md` 에 저장될 예정입니다.

---

## 0. 검토 의뢰자의 입장 + 본 검토의 6 질문

### 0.1 검토 의뢰자

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트 (주로 Claude Code) 가 SDD + TDD 로 자동 개발하도록 설계된 메타-템플릿**" 을 만들고 있습니다. 본 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다.

본 프로젝트의 메인 작업 컨텍스트는 Claude (Anthropic) 입니다. 따라서 본 cross-vendor 의뢰는 *비-Claude vendor* 의 의견을 확보하는 것이 핵심 목적입니다.

### 0.2 본 검토의 6 질문

본 검토는 단일 질문이 아니라 **6 질문 묶음** 입니다. 각 질문에 독립적으로 근거 기반 판정을 요청합니다:

1. **5 Layer 타당성**: ADR-012 §2.8 의 5 Layer 구조가 Evidence Ledger 보호 모델로 충분히 *타당한가*? (구조적 결함 / 누락된 attack surface / 중복된 layer 가 있는가?)
2. **Group H 진입 가부**: Layer 1~5 가 모두 fixture/CI PoC 로 검증된 현 상태에서 *Group H ADR-014 발행* 으로 넘어가도 되는가? (PoC 시제 → ADR 발행 전이가 정당화되는가?)
3. **운영 적용 시점**: 실 branch protection / signed commit / external timestamping / multi-host 적용은 *ADR-014 이전* 에 필요한가, *이후* Implementation 영역으로 미뤄도 되는가? (현재는 모두 fixture 시제만 존재 — 운영 적용 0건)
4. **순서 결정**: Group H ADR-014 와 Group I G3 22 권한 분해 중 *무엇을 먼저* 진행하는 것이 안전한가? (둘 다 풀 3+1 + 외부 LLM 1+ 합의 영역)
5. **거버넌스 적정성**: 현재까지의 PoC 들이 "복잡성은 높지만 안전성은 충분한 구조" 인지, 아니면 *과도한 거버넌스* 인지? (1인 개발자 동일 호스트 SPOF 환경에서 17 PoC 산출물 + 59 commits 가 적절한 비례인지)
6. **최종 판정**: 위 1~5 종합 시, 본 시점 진입점 결정에 대한 최종 판정은 **APPROVE** / **APPROVE WITH CONDITIONS** / **PARTIAL** / **BLOCK** 중 무엇인가?

본 질문은 다음을 *묻지 않습니다*:
- ❌ 의뢰자가 무슨 답을 원하는지 (의뢰자는 답을 미리 제시하지 않음)
- ❌ 다른 LLM 이 어떤 답을 했는지 (본 자료는 다른 LLM 응답을 *포함하지 않음*)
- ❌ 내부 Agent 가 어떤 결론에 도달했는지 (본 자료에 *포함되지 않음*)

**본 의뢰자는 어느 판정도 사전에 선호하지 않습니다.** APPROVE 가 안전한 답이 아닙니다. BLOCK 도 안전한 답이 아닙니다. *근거에 의해 도출된 판정* 이 안전한 답입니다.

### 0.3 본 검토의 *메타* 목적

자기참조 편향 통제. 본 프로젝트의 모든 합의 산출은 Claude 패밀리 컨텍스트에서 작성되었습니다. ADR-012 §2.8 5 Layer 답습 5/5 완결 = *Evidence Ledger 보호 구조 성숙* 분기점이므로, 다음 진입점 (ADR-014 발행 / G3 22 권한 분해 / 운영 적용) 결정 *전* vendor 다양성 확보가 결정적입니다.

본 의뢰는 그 vendor 다양성을 확보하기 위한 의도적 *blind* 의뢰입니다.

---

## 1. 시스템 목적 (요약)

### 1.1 프로젝트 정체성

- **이름**: AI Development Tool Template
- **사용자**: 1인 개발자 (동일 호스트, SPOF 의도적 수용 — ADR-012 §2.8 명시)
- **저장소**: 코드 0줄 (PoC 도구 ~17개 = 산출물 시제 한정), 약 75+ 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 60+ 합의/외부검토 보고서 + 가이드 + Phase0 사양 + 세션 로그)
- **사용 방식**: 새 프로젝트 → 템플릿 복사 → Phase 0 (질문지) → Phase 1 (스택/에셋 합의) → Phase 2-3 (SDD → TDD)
- **메타-슬로건**: "에이전트에게 하라고 말하지 말고, 잘못하는 것이 *불가능*하게 만들어라."

### 1.2 핵심 방법론 (4축)

- **SDD** (Specification-Driven Development): 코드 변경 전 설계 문서 우선
- **TDD** (RED → GREEN → REFACTOR, 70% 커버리지 목표)
- **하네스 엔지니어링**: 8-Layer 피드백 루프 (CLAUDE.md / 검토 질문지 / PostToolUse / PreCommit / git pre-commit / CI / 3+1 합의 / Human review)
- **3+1 멀티에이전트 합의**: Agent A (구현) + Agent B (안전성) + Agent C (대안) → Reviewer 종합

### 1.3 권위 위계 (영구)

```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

본 위계는 **ADR-011 §2.3** 에 영구 권위로 명시. **Hermes 는 시스템의 root of trust 가 아니라 검증 대상**.

### 1.4 Hermes PMO 의 역할

- **Hermes** = Project Memory Organism (계획-기억-규율 통합 인격)
- **PMO** (Project Management Officer) 격상 = 운영적 권한 행사 단계 (현재 *DRAFT 시제* 한정 — 격상 미선언)
- **격상 조건** (영구 핵심 제약 5건):
  1. ADR-008 + ADR-011 모순 0건
  2. R-4 ~ R-7 영구 제약 5/5 충족
  3. G1b + G2 + G3 + G4 Design/Governance PASS
  4. **G2/G3/G4 Implementation/Runtime PASS** (현재 *부분 충족 시제* 만)
  5. cross-vendor + Reviewer 종합 합의

---

## 2. G1b / G2 / G3 / G4 Design/Governance PASS 상태 (2026-05-10 시점)

### 2.1 4 게이트 정의 + 현 상태

| 게이트 | 정의 | Design/Governance PASS | Implementation/Runtime PASS |
|--------|------|----------------------|---------------------------|
| **G1b** | Provider Liquidity (모델/구독 교체 자유) | ✅ Phase 1 PASS (`3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md`) | — |
| **G2** | Governance Preconditions (보안/거버넌스 사전 조건 6건 GP-1 ~ GP-6) | ✅ Draft PASS (`3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md`) → 정식 합의 (`3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`) | **부분 충족 시제** (GP-2/GP-3 형식 layer / GP-4 형식 layer / GP-5 Layer 1a/1b/1c / GP-6 feasibility) |
| **G3** | Root of Trust Runtime (22 권한 분해 + Skill escalation + 합의 자기참조 차단) | ✅ Draft PASS (`3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md`) → 정식 합의 (`3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`) | **부분 충족 시제** (Hermes-originated marker / Skill escalation / 합의 자기참조) |
| **G4** | Provider-agnostic Memory/Skill + Evidence Ledger Protection | ✅ Draft PASS (`3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md`) → 정식 합의 (`3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`) | **부분 충족 시제** (17-field schema / 11-field JSONL / Memory/Skill boundary / Full Rewrite 5 Layer 5/5) |

### 2.2 Design/Governance PASS = *영구 합의 발행 권한 0건*

**중요 설계 명시**: G1b/G2/G3/G4 *Design/Governance PASS* 는 *설계 수준 합의 도달* 을 의미하며, *Implementation/Runtime PASS = 운영 적용* 권한을 자동 부여하지 *않음*. ADR-011 §2.1 (a)~(e) 5 조건 모두 충족 후 별도 합의 필요.

---

## 3. Implementation/Runtime Groups A~CFF 완료 요약 (2026-05-10 시점)

### 3.1 PoC 시제 (현재) vs 운영 적용 (미진입)

본 프로젝트는 *현재* 모든 Implementation/Runtime 영역에서 **fixture 기반 정적 검출 PoC 시제** 한정 진행. 다음은 *모두 미진입*:

- ❌ 실 branch protection 변경 (GitHub repo settings)
- ❌ 실 git hook 활성화 (`.git/hooks/pre-commit`)
- ❌ 실 signed commit 강제
- ❌ 실 external timestamping service 연동 (RFC 3161 / Sigstore)
- ❌ 실 GitHub API 호출 (Octokit / gh API)
- ❌ Multi-host external service (anchor mirror)
- ❌ Hermes PMO 격상

### 3.2 완료 Group 매트릭스 (10 Groups, 2026-05-10 시점, 누적 59+ commits `35cbf4b → 1d7b9e0`)

| Group | 영역 | actual run | 산출물 핵심 |
|-------|------|------|------------|
| **A 1차** | G2 GP-5 Layer 1a — Provider Adapter Enforcement (AST 5종 패턴) | `25599xxx` PASS | `tools/provider_import_scanner.py` (~AST 기반) + 1차 fixture (PASS×1+FAIL×5) + CI workflow + Reviewer-only 단축 합의 |
| **A 2차** | G2 GP-5 Layer 1b — Transitive import (import-linter 2.11 + grimp 3.14, RA-9 §B.3 사전 검증 PASS) | `25602xxx` PASS | `.importlinter` (4종 forbidden + facade ignore + `include_external_packages = True`) + `requirements-dev.txt` + `src/` placeholder + transitive_import.py fixture + CI 양방향 step + Reviewer-only 단축 합의. **풀 3+1 합의** = T-2 import-linter 채택 (T-1 Python 미지원, RA-9 사전 검증 의무) |
| **A 보완** | G-1 (CI probe cleanup `if: always()`) + G-2 (`.gitignore` 4 패턴) + G-3 (C-9 venv 정리) | — | 보조 작업 — 별도 합의 미발화 |
| **B** | G3 — Hermes-originated marker + Evidence 없는 PASS 차단 | `25605665191` PASS 8s | `tools/evidence_pass_gate.py` (~165줄 / 3 검사) + fixture (PASS×2+FAIL×4 / 3 패턴 cover) + CI workflow + Reviewer-only 단축 합의. ADR-011 §2.1 5/5 + 8 PASS / 6 BLOCK / 7 금지 0/7 |
| **C** | G4 — JSONL hash chain + RFC 8785 JCS + round-trip (Layer 1) | `25618490324` PASS 33s 14/14 step | `tools/canonical_json.py` (CrossCheckMode 4종 + jq fallback) + `tools/jsonl_hash_chain.py` (11 필드 schema + Genesis hash + chain violation 4 패턴 + monotonicity) + `tools/jsonl_roundtrip.py` (T2 strict + T3 lossy + 3 ledger entry) + corpus 24 + reject 2 + PoC 6 영역. **풀 3+1 합의** = rfc8785 + jcs(titusz) 병렬 cross-check + 17 조건 (Q1) + 단축 합의 (Q2/Q3 6 조건). 양방향 38/38 PASS |
| **F** | G2 GP-6 Memory/Skill Migration *Feasibility* | `25620376305` PASS 14s 16/16 step | `tools/memory_skill_roundtrip.py` (245줄, Group C 3 모듈 import 직접 + 토이 매핑 3 함수 + `--feasibility-mode hermes-to-claude` CLI) + fixture 4건 (Memory PASS + Skill PASS 17 필드 + LOSSY hermes_to_claude with `_hermes_internal_id` + FAIL chain_violation `prev_hash_mismatch`) + CI workflow + Reviewer-only 단축 합의. F-범위 10/10 |
| **F 후속** | workflow artifact path 개선 (Option B `.group-f-logs/` → `group-f-logs/` rename, leading dot 미사용 정책) | `25621470142` PASS 9s 16/16 step | tools/ 변경 0건 의무 답습 + 보조 작업 (별도 합의 미발화) |
| **D** | G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction | `25623028888` PASS | `tools/secret_scanner.py` (261줄, **R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns**) + 2 mode CLI (scan-source/scan-log) + `--list-patterns` self-check + `is_redaction_marker_match()` (FP 회피) + fixture 9건 (PASS 2 + FAIL 4 + REDACTION_PASS 1 + REDACTION_FAIL 2) + CI workflow + Reviewer-only 단축 합의. F-범위 5/5 + 12 금지 0/12 + ADR-011 §2.1 5/5 |
| **E** | G2 GP-4 External Input Validation + G4 Memory/Skill schema validation | `25624970577` PASS 10s 16/16 step | `tools/schema_validator.py` (~520줄) + 2 mode CLI (external-input/skill-schema) + `--list-skill-fields` self-check + 17-field 정의 (G4 §3.1 직접 복사) + 11-field 검증 (Group C `validate_schema` import 직접) + injection canary 26 patterns (12 + 8 + 6) + ENUM (allowed_actions 7 / promotion_status 5 / scope 4) + fixture 9건. PASS 6/6 + 0/10 금지 |
| **G** | G3 Skill escalation + 합의 자기참조 차단 + G4 Memory/Skill boundary 4 금지 | `25626591894` PASS 5s 17/17 step | `tools/boundary_guard.py` (~445줄) + 3 mode CLI (skill-escalation / consensus-self-reference / memory-skill-boundary) + `--list-boundaries` self-check (4 boundaries + 3 modes + 13 합의 매트릭스 row) + Group C `validate_schema` + Group E `ALLOWED_ACTIONS_ENUM` import 직접 + Group B Hermes-originated marker 6 + fixture 9건. PASS 8/8 + 0/11 금지 |
| **A 3차** | G2 GP-5 Layer 1c — URL endpoint + model name 직접 사용 차단 | `25629390384` PASS 6s 16/16 step | `tools/provider_url_scanner.py` (~210줄) + 2 mode CLI (url-endpoint/model-name) + `--list-catalogs` self-check + URL Tier-1 catalog 10 + Model Tier-1 catalog 19 + extension allowlist + fixture 9건. PASS 6/6 + 0/8 금지. **Layer 1a/1b/1c 분리 답습 완결** |
| **CF** (C 후속) | G4 History Rewrite Layer 5 — External Anchor Verifier | `25630561391` PASS | `tools/history_anchor_verifier.py` (~310줄) + 2 mode CLI (chain-only / anchor-verify) + `--list-attack-models` self-check (5 attack scenarios + 11 anchor fields + Layer 1 inadequacy demo supported) + Group C `jsonl_hash_chain` import 직접 + 11-field anchor schema + 5 attack model 검출 + fixture 10건 (PASS 4 + FAIL 5 + chain_only_demo 1) + CI workflow 16 step. PASS 10/10 + 0/7 금지 + 0/5 trigger. **Layer 1 inadequacy demo + Layer 5 의무성 evidence** |
| **CFF** (C 후속 후속) | G4 Rewrite Defense Layer 2/3/4 — append-only + dangerous git command + line regression | `25631422222` PASS | `tools/rewrite_defense_check.py` (~340줄) + 3 mode CLI (append-only L2 / rewrite-command L3 / line-regression L4) + `--list-defenses` self-check (5 layers + 4 commands + 3 regression types) + Group C `parse_jsonl` import 직접 + commit history diff (L2) + dangerous command catalog 4 (rebase / filter-branch / reset-hard / push-force-or-amend) + line regression detector 3 types + fixture 17 files / 8 logical. PASS 10/10 + 0/9 금지 + 0/5 trigger. **본 PoC 종료 = ADR-012 §2.8 5 Layer 답습 5/5 완결 milestone** |

### 3.3 모든 산출물 공통 제약 (사용자 명시 답습)

- **stdlib 단독 또는 의존 1~2개 한정** (rfc8785 + jcs 본 프로젝트 전 영역 공통). 외부 의존 0건 또는 최소화
- **실 git command / 실 GitHub API / 실 git hook / 실 production data 호출 0건** (모두 fixture 기반)
- **신규 ADR 본문 변경 0건** (cross-reference 답습 한정)
- **신규 정책 발명 0건**
- **각 PoC 형식**: scanner + fixture (PASS + FAIL × N) + CI workflow + 사양 + Reviewer-only 단축 합의
- **artifact path 정책**: `group-X-logs/` (leading dot 미사용 — Group F 후속 답습)

---

## 4. ADR-012 §2.8 *Full Rewrite 5 Layer* 답습 5/5 완결 현황

### 4.1 Layer 매트릭스

ADR-012 §2.8 (Evidence Ledger Protection) 의 *Full Rewrite 5 Layer* 모델은 다음 책무 분담:

| Layer | 차단 영역 | 책무 분류 | 답습 시점 | actual run | 도구 | PoC 한계 |
|-------|----------|---------|---------|----------|------|---------|
| **L1** | Single entry tampering (1개 entry 의 hash 변조) | *사후 검출* | Group C (`5fd69af`) | `25618490324` PASS | `tools/jsonl_hash_chain.py` | rfc8785+jcs 의존 / 실 ledger 적용 미진입 |
| **L2** | History 재작성 (force-push / commit reorder) | *사전 차단* | Group C 후속 후속 (`f754511 → 95fc8aa`) | `25631422222` PASS | `tools/rewrite_defense_check.py --mode append-only` | 실 branch protection 미진입 / 실 GitHub API 호출 0건 |
| **L3** | Dangerous git command 사용 (rebase / filter-branch / reset --hard / push --force / commit --amend) | *사전 차단* | Group C 후속 후속 | `25631422222` PASS | `tools/rewrite_defense_check.py --mode rewrite-command` | 실 git hook 활성화 미진입 / `git filter-repo` Tier-2 미통합 / `git reset --soft/--mixed` Tier-2 미통합 |
| **L4** | Line deletion / in-place rewrite (CI 회귀 검증) | *사전 차단* | Group C 후속 후속 | `25631422222` PASS | `tools/rewrite_defense_check.py --mode line-regression` | 실 CI base branch fetch 미진입 / Reflog 통합 미진입 |
| **L5** | External anchor mismatch (substitution / full rewrite) | *사후 검출* | Group C 후속 (`cfc48ae`) | `25630561391` PASS | `tools/history_anchor_verifier.py` | 실 external timestamping (RFC 3161 / Sigstore) 미진입 / signed_tag·external_snapshot 메서드 미진입 / Anchor metadata 자체 signing 미진입 / Anchor nightly cron 미진입 / Multi-host external service 미진입 / Commit signature verification 미진입 |

### 4.2 7 Attack 시나리오 cover

| Attack | Cover Layer |
|--------|-----------|
| 단일 entry hash 변조 | L1 + L5 |
| Force-push | L2 + L5 |
| `git rebase` / `filter-branch` / `reset --hard` | L3 + L5 |
| Line deletion | L4 + L5 |
| In-place rewrite | L1 + L4 + L5 |
| Substitution | L5 |
| Full rewrite | L2 + L3 + L4 + L5 |

L1/L5 = *사후 검출* (변조 후 hash chain / anchor mismatch 발견)
L2/L3/L4 = *사전 차단* (변조 시도 시점에 차단)

### 4.3 본 5 Layer 가 *해결한 영역* vs *해결하지 않은 영역*

#### 해결한 영역 (정적 검출 시제)

- ✅ Single entry tampering 정적 검출
- ✅ History 재작성 (force-push / reorder) fixture 기반 검출
- ✅ Dangerous git command catalog (Tier-1 4종) 정적 검출
- ✅ Line deletion / in-place rewrite fixture 기반 검출
- ✅ External anchor 11-field schema 정적 검증
- ✅ 5 attack scenario fixture 검출

#### 해결하지 않은 영역 (운영 적용 미진입)

- ❌ 실 branch protection rule (`receive.denyNonFastForwards true` / GitHub branch protection rule)
- ❌ 실 git pre-commit hook 활성화 (`.git/hooks/pre-commit`)
- ❌ 실 signed commit 강제 (`git commit -S` / GPG / SSH key)
- ❌ 실 external timestamping service (RFC 3161 / Sigstore / OpenTimestamps)
- ❌ Multi-host external anchor mirror
- ❌ Anchor metadata 자체 signing
- ❌ Anchor nightly cron / 자동 발행
- ❌ Commit signature verification (Layer 5 영역 의무 trigger)
- ❌ Tier-2 dangerous command (`git filter-repo` modern alt / `git reset --soft/--mixed`)
- ❌ Reflog 통합

### 4.4 1인 동일 호스트 SPOF 한계 (ADR-012 §2.8 명시 답습)

본 프로젝트의 모든 Layer 1~5 PoC 는 *동일 호스트 동일 사용자* 환경 한정. ADR-012 §2.8 본문에 다음 명시:

- **현재**: 1인 사용자 = 본 PoC + 본 프로젝트 전체 사용자
- **한계**: external anchor 도 *동일 호스트* 에 저장 시 *동일 신뢰 도메인 내 다중 앵커* 상태
- **multi-host 전환 trigger**: 외부 LLM / 다른 호스트 / 다른 git remote 합류 시 Layer 1~5 모두 *MANDATORY 발동* 격상 필요

**현재 프로젝트는 multi-host 미전환** — 모든 Layer = ADVISORY 시제.

---

## 5. 미선언 상태 (의도적 답습)

### 5.1 G2/G3/G4 전체 Implementation/Runtime PASS 미선언

**현재 상태**:
- G2 GP-5: Layer 1a/1b/1c 분리 답습 *정적 검출* 시제 한정 (실 src/ 적용 미진입)
- G2 GP-2/GP-3: *형식적 검출 layer* 시제 한정 (R-4.1 42 catalog 정적 답습만)
- G2 GP-4: *형식적 검증 layer* 시제 한정 (외부 input 정적 schema 검증만)
- G2 GP-6: *feasibility* 시제 한정 (실 migration script 0건)
- G3: *부분 충족 시제* (Hermes-originated marker + Skill escalation + 합의 자기참조 형식 차단만)
- G4: *부분 충족 시제* (17-field schema + 11-field JSONL + Memory/Skill boundary + Full Rewrite 5 Layer 5/5 정적)
- **22 권한 분해**: 미진입 (Group I 영역, 별도 풀 3+1 + 외부 LLM 1+ 합의 필요)

### 5.2 Hermes PMO 격상 미선언

격상 조건 5/5 (§1.4 답습) 中:
1. ✅ ADR-008 + ADR-011 모순 0건
2. ✅ R-4 ~ R-7 영구 제약 5/5 충족
3. ✅ G1b + G2 + G3 + G4 Design/Governance PASS
4. ❌ **G2/G3/G4 Implementation/Runtime PASS** (현재 *부분 충족 시제* 만)
5. ❌ cross-vendor + Reviewer 종합 합의 (본 의뢰 = 그 첫 시제)

### 5.3 ADR-014 미발행

**ADR-014 = Memory/Skill Runtime / Migration / Round-trip 관련 상위 결정** (Group H 영역)
- trigger: ADR-013 (`docs/decisions/ADR-013-...`) 발행 후 + Group F GP-6 feasibility 종료 후
- 합의 형식: 풀 3+1 + 외부 LLM 1+ (`3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` 답습)
- 현재: 미발행 (본 의뢰 = 발행 *전* 사전 검토)

### 5.4 운영 적용 영역 (별도 합의 + 풀 3+1 + 외부 LLM 1+)

§4.3 *해결하지 않은 영역* 8건 모두 별도 합의 영역 — 본 5 Layer PoC 완결 후 진입 후보 中 하나.

---

## 6. 산출물 evidence 매트릭스 (10 Groups, fixture-based 정적 검출 시제)

| 영역 | Group | actual run | 산출물 / 한계 evidence |
|------|-------|------------|------------------------|
| Layer 1a | A 1차 | `25599xxx` | AST 5종 패턴 / 의미적 lock-in 미진입 |
| Layer 1b | A 2차 | `25602xxx` | import-linter 2.11 + grimp 3.14 / google.generativeai 1차 단독 책무 분리 (각주 1) |
| Layer 1c | A 3차 | `25629390384` | URL+Model Tier-1 catalog 10+19 / Tier-2 vendor 미진입 / 실 src 적용 FP 영역 |
| G3 marker | B | `25605665191` | Hermes-originated marker 6 + governance PASS anchor 9 / code block 미회피 / 실 git history 외부 |
| L1 entry | C | `25618490324` | 11 필드 schema + Genesis hash + chain violation 4 패턴 / 실 ledger 적용 미진입 |
| GP-6 feasibility | F | `25620376305` | 토이 매핑 3 함수 / 실 migration script 0건 |
| GP-3+GP-2 | D | `25623028888` | R-4.1 Tier-1 42 + baseline 5 = 45 patterns / Tier-2/3 catalog 미진입 / base64 evasion = Hermes upstream R2-6 영역 |
| GP-4+G4 schema | E | `25624970577` | 17-field 정의 + 11-field 검증 + injection canary 26 / 재귀 JSON Schema 의미 검증 미진입 / pydantic·jsonschema 미도입 |
| G3+G4 boundary | G | `25626591894` | 4 boundaries + 13 합의 매트릭스 row / Skill wrapper runtime 미진입 / Docker cap_drop 미진입 / sandbox syscall 미진입 |
| L5 anchor | CF | `25630561391` | 5 attack scenarios + 11 anchor fields / signed_tag·external_snapshot 메서드 미진입 / Multi-host external service 미진입 |
| L2/L3/L4 rewrite | CFF | `25631422222` | 3 modes + 4 dangerous commands + 3 regression types / 실 branch protection·git hook·CI base branch fetch 미진입 / `git filter-repo` Tier-2 미진입 |

### 6.1 산출물 의존 그래프

```
Group C (canonical_json + jsonl_hash_chain + jsonl_roundtrip)
   │
   ├── Group F (memory_skill_roundtrip — import 직접)
   ├── Group E (schema_validator — validate_schema import 직접)
   ├── Group G (boundary_guard — validate_schema + ENUMs import 직접)
   ├── Group CF (history_anchor_verifier — parse_jsonl + validate_chain import 직접)
   └── Group CFF (rewrite_defense_check — parse_jsonl import 직접)
```

Group C = *Layer 0 코어 모듈*. 5 의존 그룹 모두 stdlib + Group C 단독 의존.

---

## 7. 의뢰자가 선호하지 않는 답안 사전 차단

### 7.1 의뢰자가 선호하지 않는 답안 패턴

본 의뢰자는 다음 패턴의 답안을 *선호하지 않습니다* (이는 *바라지 않는 답* 이 아니라 *공정성을 위해 미리 인지 요청*):

- ❌ "지금까지 잘 진행됨, 그대로 ADR-014 발행" (검토 없는 PASS)
- ❌ "복잡성이 너무 높음, BLOCK" (구조적 결함 명시 없는 BLOCK)
- ❌ "1인 개발자에게 과도한 거버넌스, 단순화 권고" (현재 ADR-012 §2.8 5 Layer 모델의 *책무 분리* 시연을 평가 없이 단순화 권고)
- ❌ "외부 LLM 의 검증을 받지 않은 모든 Group 산출물에 대한 정합성 의문" (개별 Group 합의 시제 답습 명시되지 않음)

본 의뢰자는 *근거에 의해 도출된 판정* 을 선호합니다.

### 7.2 검토 가능한 답안 패턴

다음은 *근거 기반 답안* 의 예시 (의뢰자 선호 표명 아님 — 형식 예시):

- "Layer 4 의 line regression 검출은 head append-only 가정 위반 시 false positive 가능 — fixture §X 한계 명시"
- "Layer 5 의 external anchor 가 *동일 호스트* 에 저장 시 root of trust 분리 부재 — multi-host 전환 trigger 명시"
- "Group H ADR-014 발행은 G3 22 권한 분해 (Group I) 후 진행이 안전 — 권한 분해 결과가 Memory/Skill Runtime 정의에 영향"
- "Group I 가 먼저 — Memory/Skill Runtime 권한이 22 분해 영역에 포함되므로 정의 충돌 회피"
- "ADR-014 와 G3 22 권한 분해는 독립 영역 — 병렬 가능"

---

## 8. 응답 형식 권고 (선택적)

다음 형식의 응답을 *권장* 하지만 *강제하지 않습니다*. 응답 길이 / 깊이는 자유롭게 결정하십시오.

```markdown
# Cross-vendor 응답 — Evidence Ledger 보호 모델 사전 검토 (2026-05-10)

## 0. 응답자 vendor / 모델
- vendor: (예: OpenAI / Google / Anthropic / 기타)
- 모델: (예: GPT-5.x / Gemini 2.x / Claude 4.x / 기타)

## 1. 5 Layer 타당성 (질문 1)
[근거 + 판정]

## 2. Group H 진입 가부 (질문 2)
[근거 + 판정]

## 3. 운영 적용 시점 (질문 3)
[근거 + 판정]

## 4. 순서 결정 (질문 4)
[근거 + 판정]

## 5. 거버넌스 적정성 (질문 5)
[근거 + 판정]

## 6. 최종 판정 (질문 6)
**판정**: APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK
[종합 근거]
[조건 또는 부분 영역 명시 — APPROVE WITH CONDITIONS / PARTIAL 시]
[결함 + 후속 조치 권고 — BLOCK 시]

## 7. 추가 우려 / 누락 영역 (선택)
[본 의뢰 자료에 누락된 영역 / 추가 검토 권고]
```

---

## 9. 본 의뢰가 *수용하지 않는* 영역

다음은 본 의뢰 자료의 *책무 외* 영역입니다. 응답에 다음을 포함해도 의뢰자가 *수용하지 않습니다*:

1. **Hermes PMO 격상 권고** — 본 의뢰자는 PMO 격상을 사전 차단하고 있으며, 본 의뢰 결과로 PMO 격상이 발생하지 않음
2. **G2/G3/G4 전체 Implementation/Runtime PASS 자동 선언 권고** — 본 의뢰자는 이 자동 선언을 사전 차단
3. **ADR-014 자동 발행 권고** — 본 의뢰는 ADR-014 발행 *여부* 의 사전 검토이며, 자동 발행 trigger 가 아님
4. **실 branch protection / 실 git hook / 실 signed commit / 실 external timestamping 자동 활성화 권고** — 본 의뢰자는 이를 사전 차단
5. **ADR 본문 자동 갱신 권고** — 본 의뢰는 cross-reference 답습 한정이며, ADR 본문 변경은 별도 풀 3+1 합의 영역

위 영역은 응답이 권고해도 자동 발생하지 않습니다. 응답자가 위 영역에 대한 *권고* 를 포함하는 것은 자유이나, 의뢰자의 후속 합의 영역으로 분리됩니다.

---

## 10. 본 의뢰의 *영구 권한* 한정

본 의뢰의 응답은 다음 권한 *한정*:
- ✅ 6 질문 각각에 대한 *근거 기반 판정* 제시
- ✅ 추가 우려 / 누락 영역 / 후속 조치 권고
- ✅ 응답 형식 자유 (한국어 / 영어 / 혼합)

본 의뢰의 응답은 다음 권한 *비한정*:
- ❌ 본 프로젝트의 ADR / SDD / 합의 본문 자동 변경
- ❌ 본 프로젝트의 권위 위계 변경
- ❌ Hermes PMO 격상 / G2/G3/G4 전체 Implementation/Runtime PASS / ADR-014 발행 / 운영 적용 자동 활성화

응답은 *의뢰자 + 내부 Reviewer 종합 합의* 의 *입력* 으로 사용되며, *출력* 또는 *결정* 으로 사용되지 *않습니다*.

---

## 11. 검토 요청 마무리

본 의뢰는 자기참조 편향 통제 + vendor 다양성 확보 의 *수단* 입니다. 응답자의 vendor 가 의뢰자의 메인 컨텍스트 (Claude) 와 다르다면, 본 의뢰의 *목적* 이 충족됩니다.

응답자의 판정이 의뢰자가 사전에 도달한 결론 (의뢰자는 사전 결론을 *명시하지 않음*) 과 다르더라도, 그것은 *오답* 이 아니라 *vendor 다양성의 evidence* 입니다.

**감사합니다.**

---

## 부록 A. 참조 문서 (의뢰 자료 외부 — 응답에 인용 *불필요*)

본 의뢰 자료는 본 문서 *단독* 으로 평가 가능하도록 작성되었습니다. 다음은 *내부 참조용* 이며 응답자가 인용 *불필요*:

- `docs/CONTEXT.md` — 본 프로젝트 현재 상태
- `docs/INDEX.md` — 본 프로젝트 문서 인덱스
- `docs/sessions/SESSION_2026-05-10.md` — 본 세션 로그
- `docs/decisions/ADR-008-hermes-adoption-decision.md` — Hermes 채택 결정
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` — 수단/목적 분리 + R-4 ~ R-7 영구 제약
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (가정) — 본 의뢰 §4 의 5 Layer 모델 출처
- `docs/architecture/multi-agent-system-design.md` — 3+1 합의 설계
- `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-request.md` — 본 의뢰 형식 답습 출처

응답자는 위 참조 문서를 *읽지 않아도* 본 의뢰 자료 §1 ~ §10 만으로 평가 가능합니다.

---

## 부록 B. 본 의뢰의 *영원 격리* 보장

본 의뢰의 응답은 별도 합의 입력으로만 사용되며, 다음은 자동 발생 *불가*:
- ❌ 본 프로젝트의 자동 운영 적용
- ❌ Hermes PMO 격상
- ❌ G2/G3/G4 전체 Implementation/Runtime PASS 선언
- ❌ ADR 본문 자동 갱신

응답자가 본 의뢰 응답에서 *어떤 권고도* 표명하더라도, 위 자동 발생은 격리됩니다. 의뢰자는 응답을 *입력* 으로만 사용하며, 후속 합의 형식 (Reviewer-only 또는 풀 3+1) 에서만 결정됩니다.

---

**의뢰 자료 종료. 응답을 부탁드립니다.**
