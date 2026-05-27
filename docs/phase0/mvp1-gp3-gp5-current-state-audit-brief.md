# MVP-1 GP-3 + GP-5 현 상태 audit + 다음 진입점 권고 brief

> **scope**: 2026-05-27 시점 MVP-1 GP-3 + GP-5 진입 합의 상태 + 실 구현 상태 + DRAFT 잔재 + deferred 영역 audit. **본 brief = read-only audit + 다음 진입점 권고 한정. 수단 결정 0 / threshold 고정 0 / 실 구현 0 / PASS 발효 0**.
> **답습**: [[implementation-runtime-roadmap-mvp1]] §8 다음 진입점 / [[ADR-011-means-vs-ends-redaction]] §2.1 / [[ceremony-inflation]] 1-agent 직접 audit (수단 결정 *아님*).
> **DONE 기준**: 합의 / 구현 / 문서 매핑표 + 다음 진입점 4 후보 권고. 사용자 결정 = brief 외 영역.

---

## 1. 진입 합의 완료 상태 (3 합의)

| 합의 | 일자 | 판정 | conditions |
|------|------|------|-----------|
| `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` | 2026-05-12 | ✅ APPROVE w/ COND (단축, Reviewer-only) | C-1 G3-7 부분 분리 / C-2 1.5차 보강 풀 3+1 / C-3 T3 별도 풀 3+1 / C-4 O-2 GP-5 후속 |
| `3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` | 2026-05-12 | ✅ APPROVE w/ COND (단축, Reviewer-only) | C-1 1.5차 분리 / C-2 T3 별도 풀 3+1 / C-3 G5-4 facade real 별도 / C-4 O-2 §5.4 신설 |
| `3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` | 2026-05-12 | ✅ APPROVE (단축, Reviewer-only) | 9 sub-수단 본문 채택, runtime code/CI/hook 시작 권한 발효 |

→ **MVP-1 본문 채택 commit**: `f40423f` (push 완료, Layer B 발효 결과 행사).

---

## 2. 실 구현 상태 audit (2026-05-27 grep)

### 2.1 도구 (`tools/` = 21 개)

| 도구 | 답습 합의 | 상태 |
|------|----------|------|
| `secret_scanner.py` (368줄) | GP-3 S-1 (coverage 기반 코드 본문 secret 검출) | 실 구현 |
| `provider_import_scanner.py` (178줄) | GP-5 T-1 (AST 5 패턴) | 실 구현 |
| `provider_url_scanner.py` | GP-5 T-3 (URL Tier-1 10 + Model Tier-1 19) | 실 구현 |
| `boundary_guard.py` | T2 정책 경로 boundary | 실 구현 |
| `evidence_pass_gate.py` | Evidence Ledger gate | 실 구현 |
| `jsonl_hash_chain.py` | Evidence chain integrity (P10) | 실 구현 |
| `history_anchor_verifier.py` | G4 history anchor | 실 구현 |
| `rewrite_defense_check.py` | G4 rewrite defense | 실 구현 |
| `schema_validator.py` | Schema 검증 | 실 구현 |
| `workflow_permissions_check.py` / `_secrets_reference_check.py` / `_secrets_usage_check.py` / `_fork_pr_secret_policy_check.py` | CI workflow 검증 4 도구 | 실 구현 |
| `mvp1_pc3_ar1_integration_check.py` | PC-3 + AR-1 통합 검증 | 실 구현 |
| `docker_secret_image_layer_check.sh` / `_inotify_sidecar_check.sh` / `_restart_recovery.sh` | GP-3 ST-1~ST-5 docker secret | 실 구현 (shell) |
| `canonical_json.py` | sha256 canonical 직렬화 | 실 구현 |
| `jsonl_roundtrip.py` / `memory_skill_roundtrip.py` | Roundtrip 검증 | 실 구현 |

### 2.2 CI workflows (`.github/workflows/` = 11 개)

| workflow | 답습 합의 | 상태 |
|---------|----------|------|
| `provider-adapter-enforcement.yml` | GP-5 PC-3 + AR-1 | 실 구현 |
| `provider-url-scanner.yml` | GP-5 T-3 | 실 구현 |
| `secret-hygiene-egress-redaction.yml` | GP-3 S-1 + redaction | 실 구현 |
| `boundary-guard.yml` | T2 boundary | 실 구현 |
| `evidence-pass-gate.yml` | Evidence gate | 실 구현 |
| `g4-hash-chain.yml` | Evidence chain | 실 구현 |
| `history-anchor-verifier.yml` | G4 anchor | 실 구현 |
| `rewrite-defense.yml` | G4 rewrite | 실 구현 |
| `schema-validation.yml` | Schema | 실 구현 |
| `r2-canary.yml` | Canary | 실 구현 |
| `memory-skill-migration-feasibility.yml` | Memory→Skill migration | 실 구현 |

### 2.3 Config + adapters

| 파일 | 답습 | 상태 |
|------|------|------|
| `.pre-commit-config.yaml` | PC-4 T2 (Backlog #1 + #2 통합 local pre-commit framework, opt-in) | 실 구현 |
| `.importlinter` | GP-5 T-2 (4 vendor 차단: openai/anthropic/litellm/ollama, transitive include_external_packages=True) | 실 구현 |
| `src/adapters/llm/facade.py` (41줄) | GP-5 §4.1 facade *유일* LiteLLM 직접 import 경로 | **placeholder** (real 본문 = TR-1 풀 3+1 trigger 발화 시점) |

---

## 3. DRAFT 잔재 + deferred 영역

### 3.1 문서 권위 잔재

| 문서 | 현 상태 | 권고 |
|------|--------|------|
| `implementation-runtime-roadmap-mvp1.md` line 826 | `DRAFT — Reviewer-only 단축 합의 진행 예정` | Reviewer-only 단축 합의 진행 → APPROVED 권위 발효 |

→ 단 line 819~821 변경 이력 = 후속 3 합의 (gp3 / gp5 / backlog6) 본문 흡수 *완료*. 본문 권위는 사실상 합의됨. `DRAFT` 표시만 잔재.

### 3.2 1.5차 보강 deferred (수단 결정 0)

| sub-수단 | GP | 영역 | 합의 형태 권고 |
|---------|----|------|---------------|
| S-3 detect-secrets 부분 통합 | GP-3 | Tier-2/3 catalog 확장 | 풀 3+1 + 외부 LLM 1+ (Group D §2.1 (D)) |
| ST-2 inotify sidecar | GP-3 | 저장 경로 실시간 감지 | 풀 3+1 |
| PC-1 pre-commit framework 의무화 | GP-3/GP-5 | T3 dev 환경 강제 | 풀 3+1 + 사용자 명시 |
| AR-3 통합 PR auto-reject | GP-3/GP-5 | branch protection rule | 풀 3+1 + 외부 LLM 1+ |
| ST-1 / ST-2 / ST-5 (Hermes upstream) | GP-3 | Hermes upstream 변경 | 풀 3+1 + Hermes upstream PR |
| ST-4 (Vault HSM) | GP-3 | T3 + Multi-host 인프라 | ADR-010 §X 진입 합의 + 외부 LLM 1+ |
| T-1 / T-3 / T-4 / T-5 단독 진입 | GP-5 | 도구 변경 영향 분석 | 풀 3+1 |
| URL / 모델 Tier-2/3 vendor 추가 | GP-5 | catalog 확장 | 풀 3+1 |

### 3.3 placeholder → real 본문

| 파일 | 현 상태 | trigger |
|------|--------|--------|
| `src/adapters/llm/facade.py` (41줄) | placeholder | real 본문 작성 = TR-1 풀 3+1 자동 trigger (G5-4) |

---

## 4. ADR-011 §2.1 (a)~(e) 5조건 충족 매트릭스 (현 시점 audit)

| # | 조건 | GP-3 충족 상태 | GP-5 충족 상태 |
|---|------|---------------|----------------|
| (a) | 동등 이상의 보안 결과 | ✅ Tier-1 42 catalog 답습 + secret_scanner.py 실 구현 | ✅ Tier-1 URL 10 + Model 19 + provider_import/url_scanner 실 구현 |
| (b) | 격리 환경 PoC 실증 | ✅ docker_secret_*.sh 3 + PoC Group D | ✅ depcruise/import-linter PR auto-reject + Group A 1/2/3 |
| (c) | ADR / SDD 권위 명시 | ✅ ADR-008 §A.2 + ADR-010 + R-4 + GP-3 §5 + roadmap-mvp1 §3 | ✅ ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + GP-5 §7 + roadmap-mvp1 §4 |
| (d) | 자동 회귀 검증 경로 | ✅ `secret-hygiene-egress-redaction.yml` + `evidence-pass-gate.yml` + nightly | ✅ `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` + 매 PR + nightly |
| (e) | 합의 APPROVE | ✅ gp3-mvp1-entry APPROVE w/ COND | ✅ gp5-mvp1-entry APPROVE w/ COND |

→ **5/5 충족 (양 GP)**, 단 (e) 의 conditions (C-1~C-4) 미해소 영역 = 1.5차 보강 / T3 / O-2 후속 = deferred.

→ **Implementation Evidence PASS 발효 자격** = "조건 (a)~(e) 5/5 + conditions 해소" 의 후자가 미충족 = **현재 PASS 발효 미적격, 1.5차 보강 cycle 필요**.

---

## 5. 다음 진입점 4 후보 권고

| # | 진입점 | scope | 합의 형태 | 비용 |
|---|--------|------|----------|------|
| (a) | `implementation-runtime-roadmap-mvp1.md` DRAFT → APPROVED 권위 발효 합의 | 본 문서 권위 발효, 본문 변경 0건 (cross-reference 답습 한정) | **Reviewer-only 단축 합의** (line 287 답습) | 낮음, 본 cycle 직접 연속 가능 |
| (b) | MVP-1 1.5차 보강 합의 (S-3 / ST-2 / PC-1 / AR-3 1 이상) | conditions C-2 (gp3) + C-1 (gp5) 해소 | **풀 3+1 합의 + 외부 LLM 1+** | 높음, 별도 brief + cycle |
| (c) | MVP-1 Implementation Evidence PASS 발효 합의 | (a)+(b) 후, ADR-011 5/5 + conditions 해소 + 사용자 명시 | **별도 합의 + 사용자 명시 결정** | 최고, 1.5차 보강 선행 필수 |
| (d) | facade.py placeholder → real 본문 진입 (TR-1 풀 3+1 자동 trigger) | LiteLLM 통합 실 본문 + 라운드트립 (P2-5 의미적 lock-in 검증) | **TR-1 자동 풀 3+1** (G5-4 답습) | 높음, MVP-1 PASS 외 영역 (별도 시점) |

**권고 진입 순서**: (a) → (b) → (c). (d) 는 다른 trajectory (TR-1 trigger 별도 시점).

---

## 6. 본 brief 의 권위 한계

- ❌ 수단 결정 0 (S-3 채택 / ST-2 채택 등 *결정* 없음)
- ❌ threshold 고정 0
- ❌ 실 코드 / CI / hook 변경 0
- ❌ PASS 발효 0
- ❌ ADR 본문 갱신 0
- ❌ DRAFT → APPROVED 권위 변경 0 (옵션 (a) 합의 후 별도)
- ✅ 권고 한정 (4 후보 진입점 + 합의 형태 추천)
- ✅ 본 brief = audit, ceremony-inflation 회피 1-agent 직접

---

## 7. 다음 단계 (사용자 결정 영역)

본 brief 검토 후 사용자 선택:
- (a) "(a) Reviewer-only 단축 합의 진행" → `roadmap-mvp1.md` 권위 발효 cycle
- (b) "(b) 1.5차 보강 풀 3+1 진입" → S-3/ST-2/PC-1/AR-3 중 어느 1 이상 brief 작성
- (c) "(c) MVP-1 PASS 발효 합의" → (a)+(b) 선행 후 진입
- (d) "(d) facade real 본문 TR-1 trigger" → 별도 풀 3+1
- (e) 본 brief 만으로 충분, 다른 작업

→ 본 brief 자체의 권위 발효 합의는 *없음* (audit + 권고 한정).

---

## 8. 답습 참조

- [[implementation-runtime-roadmap-mvp1]] §8 다음 진입점
- [[ADR-011-means-vs-ends-redaction]] §2.1 (a)~(e)
- `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` C-1~C-4
- `docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` C-1~C-4
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` 9 sub-수단 본문 채택
- commit `f40423f` (Layer B 발효)
- [[ceremony-inflation]] 1-agent 직접 audit 정당화
