# Backlog #3 Group α (AR-3 + PC-4 T3 sub) 단독 풀 3+1 합의 보고서

> **본 합의 = Backlog #3 (T3 영역) 中 Group α (AR-3 + PC-4 T3 sub) *수단 결정 적격성 권위 권고* 발행 한정** — Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) Phase 2 (Independent Analysis, 병렬 독립 분석) + Reviewer (검토 에이전트) Phase 3-4 (교차 비교 + 합의 도출) 통합. **3/3 만장일치 = APPROVE WITH CONDITIONS**.
>
> 본 합의의 어떤 §도 그 자체로 (i) **branch protection rule 실 변경** (CODEOWNERS 등록 / required check 등록 / commit signing 활성화 / merge restriction 설정 / direct push 차단 활성화 / force push 차단 활성화 / admin bypass 정책 변경 / required reviewer 설정 / ruleset 신설), (ii) **dev 환경 실 강제** (`pre-commit install` 의무화 실 활성화 / `.git/hooks` 자동 install 실 도입 / `default_install_hook_types` 실 추가 / `fail_fast` 실 활성화 / `commit-msg` / `pre-push` stage 실 추가 / `minimum_pre_commit_version` 실 명시 / `--no-verify` 실 차단), (iii) **Hermes PMO 격상 (Layer F) 선언**, (iv) **Operational Readiness PASS (Layer E) 선언**, (v) Group β / γ-1 / γ-2 자동 진입, (vi) Backlog #1 / #2 / #4 / #6 / #7 자동 진입, (vii) v1 (`ad9a02d`) / v2 (`2a9d02d`) / Group α brief (`db0e3ac`) 본문 변경, (viii) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (ix) Layer A (`f1e0b23`) / Layer B (`f40423f`) §5.5 9 sub-수단 본문 채택 변경, (x) Layer D (`210c98f`) 본문 변경, (xi) MVP-1 PASS *재선언* / MVP-2 자동 진입, (xii) 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정 + 본 합의 평가 대상 영역), (xiii) 외부 LLM *추가 자동 호출* / cross-vendor blind 의뢰 자동 재발송, (xiv) 실 API key / provider SDK / 외부 API 호출, (xv) ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012), (xvi) 도구 본문 (`tools/*.py`) / `.importlinter` / `.pre-commit-config.yaml` 본문 / 신규 hook 추가, (xvii) CI workflow 변경 / Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경, (xviii) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화, (xix) 인간 리뷰 의무 자동 발화 (Hermes PMO 격상 시 의무 — 본 합의 영역 외) 을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 9 (Group α 풀 3+1 합의 진입)
**상태**: APPROVED WITH CONDITIONS — Phase 5 (Report) 완료 + 사용자 명시 승인 *전*, 파일화 + commit 0건
**합의 판정**: **APPROVE WITH CONDITIONS** (Agent A + Agent B + Agent C **3/3 만장일치**)
**합의 영역**: Group α (AR-3 + PC-4 T3 sub) **수단 결정 적격성 권위 권고 한정** — 실 변경 0건
**상위 권위**:
- Group α brief (본 합의 직접 source) = `db0e3ac docs(phase0): add Backlog 3 Group α standalone full 3+1 consensus brief` (687줄)
- v1 prep brief = `ad9a02d` (828줄, 6 sub-영역 통합)
- v2 prep brief = `2a9d02d` (969줄, 8 지적 흡수 + 4 그룹화)
- 외부 LLM 응답 회수 = `8b5b626` (Gemini 3 Flash 114줄 + GPT-5.5 Thinking 390줄, 양 vendor 종합 = **(C) PARTIAL** 수렴)
- 외부 LLM 의뢰서 = `6a0ba21` (564줄, 19 질문)
- v2 후속 8 (외부 review 흡수) = `b4ae95e`
- Backlog #2 *잔여 5 항목* Deferred 유지 = `8ba5182` (AR-3 + T-5 (β) Backlog #3 이관 명시)
- PC-4 T2 sub Partially Satisfied = `78483c5` (PC-4 T3 sub Deferred → Backlog #3 T3 영역)
- MVP-1 Implementation Entry = `1eab814` (READY, Backlog 우선순위 1 = #6 Runtime+CI-hook)
- Backlog #6 Implementation Entry (Layer B) = `f40423f` (Backlog #3 T3 영역 분리 명시)
- ADR-011 §2.1 (a)~(e) + §2.4 T3 영역 + §2.3 영구 권위 위계
- ADR-008 부록 B Amendment + 부록 C (Hermes PMO Activation Cross-Reference)
- ADR-012 §원칙 9 (Hermes ≠ root of trust) + §2.8 (5 Layer)
- 5 영구 핵심 제약 + Provider Liquidity 5-way

---

## 0. 본 합의의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 8)

> "1로 진행" (= Group α 풀 3+1 합의 *진입* — Agent A/B/C 분석 + 외부 LLM 응답 답습 + Reviewer 종합 → `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-enforcement-defense.md` 경로 후보, v2 §4.1.1 답습)

선행 사용자 진입 명령 답습 (Group α brief 작성 시점):

> "Group α 단독 풀 3+1 합의 brief를 작성해주세요. 범위는 AR-3 + PC-4 T3 sub, 즉 branch protection / dev 환경 강제 / pre-commit install 의무화 관련 T3 정책을 검토하는 것입니다. 단, 실제 branch protection 변경, dev 환경 강제, pre-commit install 의무화, Hermes PMO 격상, Operational Readiness PASS는 하지 마세요."

본 합의 = 위 두 명령의 통합 답습 — Group α (AR-3 + PC-4 T3 sub) **수단 결정 적격성 권위 권고 발행** + 실 변경 0건.

### 0.2 본 합의가 *하는* 것

1. Phase 1 (Distribution) — Group α brief `db0e3ac` 답습 + 3 Agent 관점 분배 답습 (§1)
2. Phase 2 (Independent Analysis) — Agent A / B / C 병렬 독립 분석 결과 요약 (§2)
3. Phase 3 (Cross-Comparison) — 일치 (Consensus) / 부분 일치 (Partial) / 불일치 (Divergence) / 누락 (Gap) 분류 (§3)
4. Phase 4 (Consensus Resolution) — 최종 판단 + 합의 도출 (§4)
5. Phase 5 (Report) — 14 결정 영역 *최종 합의 권고* (§5)
6. Group I cross-reference 영역 + Backlog #6 의존성 명시 (§6)
7. Rollback Trigger 통합 매트릭스 (§7)
8. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§8)
9. 메타 검증 (§9)
10. 합의 요약 한 단락 (§10)
11. 부록 A (다음 단계 옵션) / B (금지 사항) / C (외부 LLM 응답 정합 매트릭스)

### 0.3 본 합의가 *하지 않는* 것 (사용자 명시 5 금지 + 추가 답습)

| # | 금지 | 본 합의 위반 |
|---|------|------------|
| 1 | **branch protection rule *실 변경*** (CODEOWNERS 등록 / required check 등록 / commit signing 활성화 / merge restriction 설정 / direct push 차단 활성화 / force push 차단 활성화 / admin bypass 정책 변경 / required reviewer 설정 / ruleset 신설) | 0건 (본 합의 = 수단 결정 권위 권고 한정 — 실 활성화 = Backlog #6 + 사용자 명시 결정 영역) |
| 2 | **dev 환경 *실 강제*** (`pre-commit install` 의무화 실 활성화 / `.git/hooks` 자동 install 실 도입 / `default_install_hook_types` 실 추가 / `fail_fast` 실 활성화 / `commit-msg` / `pre-push` stage 실 추가 / `minimum_pre_commit_version` 실 명시 / `--no-verify` 실 차단) | 0건 |
| 3 | **`pre-commit install` 의무화 *실 도입*** | 0건 (단계적 (opt-in → doctor → required) 권고 한정) |
| 4 | **Hermes PMO 격상 (Layer F) 선언** | 0건 (MVP-6 + 외부 LLM 의무 영역 — 본 합의 영역 외) |
| 5 | **Operational Readiness PASS (Layer E) 선언** | 0건 (MVP-6 + Backlog #7 영역) |
| (추가) | Group β / γ-1 / γ-2 자동 진입 | 0건 |
| (추가) | Backlog #1 / #2 / #4 / #6 / #7 자동 진입 | 0건 (Backlog #6 = 후속 단계 권고만) |
| (추가) | v1 (`ad9a02d`) / v2 (`2a9d02d`) / Group α brief (`db0e3ac`) 본문 변경 | 0건 (보존 + 본 합의 = 별도 권위 source) |
| (추가) | §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* | 0건 (`78483c5` + `8ba5182` 권위 source 보존) |
| (추가) | Layer A (`f1e0b23`) / Layer B (`f40423f`) §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| (추가) | Layer D (`210c98f`) 본문 변경 | 0건 (A-1 답습) |
| (추가) | MVP-1 PASS *재선언* / MVP-2 자동 진입 | 0건 |
| (추가) | 외부 LLM 응답 *결론 강제 채택* | 0건 (응답 = 입력 한정 + 본 합의 평가 대상 영역) |
| (추가) | 외부 LLM *추가 자동 호출* / cross-vendor blind 의뢰 자동 재발송 | 0건 |
| (추가) | 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 | 0건 |
| (추가) | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 |
| (추가) | 도구 본문 (`tools/*.py`) / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 | 0건 |
| (추가) | Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경 | 0건 |
| (추가) | 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 | 0건 |
| (추가) | 인간 리뷰 의무 자동 발화 (Hermes PMO 격상 시 의무) | 0건 |

### 0.4 본 합의의 권위 한계

- 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** (Layer A / Layer B 패턴 답습 — Layer B `f40423f` Backlog #6 implementation entry 권고 발행과 동일 형식).
- 본 합의 발효 ≠ 실 강제 적용. 실 강제 적용 = Backlog #6 (Runtime + CI-hook) 진입 + 사용자 명시 결정 영역 = 본 합의 영역 외.
- 14 결정 영역 *수단 결정* 권고 = 본 합의 권위 source — 단, 실 도입 단계별 (R-MVP1 trigger 답습) = 별도 합의 영역.
- 외부 LLM 응답 (`8b5b626`) = *입력* 한정 (본 합의 시 평가 대상) — 결론 강제 채택 0건.
- Group α 외 영역 (Group β / γ-1 / γ-2) = 별도 합의 영역.

---

## 1. Phase 1 (Distribution) 답습 — Group α brief `db0e3ac` + 3 Agent 관점 분배

### 1.1 본 합의 진입 source

| 영역 | 답습 |
|------|------|
| 진입 brief | Group α brief `db0e3ac` (687줄, 12 섹션 + 부록 A/B/C) |
| 합의 단위 | **Group α 단독** (v2 (II') 답습 — Group β / γ-1 / γ-2 분리) |
| 합의 형태 | **(가) 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시** (v2 답습 — 변경 0건) |
| 14 결정 영역 | AR-3 8건 + PC-4 T3 sub 6건 = 14건 |

### 1.2 3 Agent 관점 분배 답습 (v2 §5.2 + Group α brief §6.2~§6.4)

| Agent | 관점 | 핵심 질문 | 분석 영역 |
|-------|------|--------|----|
| **Agent A** | 구현 분석가 | "실제로 동작하는가?" | AR-3 + PC-4 T3 sub 기술 통합 + `--no-verify` 우회 차단 효과 + GitHub Actions integration + branch protection 세부 + GitHub plan + AI agent 권한 + 단계적 도입 효과 |
| **Agent B** | 품질 / 안전성 검증가 | "안전하고 견고한가?" | CODEOWNERS 1인 한계 + AI agent 서명 보안 + fork PR BLOCK + `--no-verify` 잔존 우회 + commit signing 보안 gap + 단계별 보안 강도 |
| **Agent C** | 대안 탐색가 | "더 나은 방법이 있는가?" | commit signing 시점 + `pre-commit install` 단계적 vs 즉시 + GitHub repo alternative + Group I 책무 분담 + 단계별 비용 정량 |
| Reviewer | 검토 에이전트 | "최선의 합의는?" | 3 출력 교차 비교 + 일치/부분/불일치/누락 분류 + 최종 판단 |

### 1.3 외부 LLM 응답 답습 (입력 한정)

| Vendor | 응답 | 종합 판정 |
|------|----|----|
| Gemini 3 Flash | 114줄 — Q1 (g) 전체 통합 + Q2 즉시 강제 (`fail_fast: true` + `commit-msg`/`pre-push` + `--no-verify` 차단 서버사이드) | (C) PARTIAL |
| GPT-5.5 Thinking | 390줄 — Q1 (e) CODEOWNERS + required check (단계적) + Q2 단계적 (opt-in → doctor → required) | (C) PARTIAL |
| **양 vendor 수렴** | PARTIAL + Group α 우선 진입 + commit signing MVP-6 + fork PR BLOCK + `--no-verify` = branch protection 결합 필수 + AR-3 × PC-4 = 유일 차단책 | — |
| **차이 영역 (2건)** | Q1 + Q2 — v2 = **GPT 답습 2/2** (1인 환경 균형 + 단계적 + friction 회피) | — |

---

## 2. Phase 2 (Independent Analysis) 결과 요약

### 2.1 Agent A (구현 분석가) — APPROVE WITH CONDITIONS

| 영역 | Agent A 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 기술 통합 가능 (현 PoC 답습 + Hermes upstream 변경 0건 + Provider Liquidity 영향 0건) + 결합 효과 = `--no-verify` 차단 6/8 시나리오 (옵션 (ii) force push + (iii OFF) admin bypass 결합 시 8/8 도달) + 조건 = Backlog #6 미진입 시 실 강제 적용 시점 의존성 발생 |
| 14 결정 영역 분류 | 7건 즉시 가능 + 6건 조건부 + 1건 후속 (commit signing MVP-6) |
| 차단 요인 | Backlog #6 미진입 = HIGH + GitHub plan 미확인 = MEDIUM + 외부 LLM 의뢰 미실시 = 0건 (회수 완료) |
| 14 결정 영역 권고 패턴 | GPT 답습 12 + 양 vendor 수렴 2 (commit signing MVP-6 + `--no-verify` 차단) |
| 성능 측정 | T3 sub 진입 시 runtime 증가 < 10초 (< 30초 threshold 충족) + 현 Cycle 4 warm 0.482초 답습 |
| 알려진 기술 한계 | GitHub App permission = repo-level (path-level scope 부재) — CODEOWNERS + required check 결합으로 *간접* 달성 / `--no-verify` = git native flag (pre-commit framework 자체 차단 불가) / private repo + free plan = branch protection 제한 / `fail_fast` CLI override 부재 / self-review 불가 / required deployments 배포 환경 의존 |

### 2.2 Agent B (품질/안전성 검증가) — APPROVE WITH CONDITIONS

| 영역 | Agent B 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 14 결정 영역 보안 차원 적합 (14/14 GPT 권고 답습 적합) + 5 영구 핵심 제약 5/5 보존 + Provider Liquidity 5-way 100% 보존 + 5 조건 (C-B-1~5) 충족 시 진입 적합 |
| 5 조건 (C-B-1~5) | (C-B-1) 엣지케이스 4 영역 명시 의무 / (C-B-2) commit signing MVP-6 gap 근거 명시 의무 / (C-B-3) branch protection 6 옵션 별 보안 강도 명시 의무 / (C-B-4) AI agent 권한 최소 권한 원칙 답습 의무 / (C-B-5) 본 brief = DRAFT 한정 답습 |
| 차단 요인 | Backlog #6 미진입 HIGH + AI agent self-approval 차단 미실시 HIGH + token rotation / GitHub plan / commit signing gap 근거 / 단계 승격 / 잔존 우회 완화책 (별도 합의 영역) |
| 위험 10 영역 | (R-1) Hermes self-bypass / (R-2) bot token 탈취 / (R-3) force push history 변조 / (R-4) workflow 변조 / (R-5) 1인 admin self-bypass = 모두 HIGH + 완화 가능 |
| 엣지케이스 9 영역 | 1인 admin self-bypass / bot token 탈취 / 단계 승격 dev 일관성 / AI agent self-approval / doctor 변조 / CI timeout / bot 인간 충돌 / rule 변경 시도 / GitHub plan 변경 |
| ADR cross-reference | ADR-011 §2.1 (a)~(e) 5조건 충족 가능 / ADR-008 부록 C 정합 / ADR-012 §원칙 9 + §2.8 Layer 2 force push 차단 + Layer 3 commit signing MVP-6 정합 |

### 2.3 Agent C (대안 탐색가) — APPROVE WITH CONDITIONS

| 영역 | Agent C 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 14 결정 영역 中 *대안 우월* 3건 + *현 권고 적정* 7건 + *대안 후속 검토* 4건 → 양 vendor 차이 2/2 모두 GPT 답습 = 대안 탐색 결과 = v2 패턴 적정 답습 |
| 대안 우월 3건 | commit signing (Y) MVP-6 + fork PR (3) default + `pull_request_target` BLOCK + `pre-commit install` 단계적 (GPT 답습) |
| 대안 후속 검토 4건 | AR-2 (e) → (g) 단계적 승격 trigger 명시 + branch protection 세부 + AI agent 권한 범위 + GitHub plan 가용성 |
| Agent C 신규 영역 (양 vendor 미언급) | (i) 단계 승격 trigger 7건 (R-MVP1-G5-AR3-STAGE 1~3차 + AR3-SIGNING + AR3-MERGE-RESTRICT + G3-PC4T3-STAGE 1~3차) / (ii) `.git/hooks` 자동 install alternative (Husky / lefthook BLOCK) / (iii) 1인 환경 단계별 비용 정량 (opt-in 3~6h + doctor 10~16h + required 16~26h = 즉시 강제 8~12h + friction HIGH 비대칭) / (iv) hosting provider alternative (GitLab / Bitbucket / Gitea) = Provider Liquidity 5-way 보존 별도 영역 |
| 차단 요인 | Backlog #6 미진입 HIGH + GitHub plan 미확인 HIGH + AI agent 권한 범위 미정 HIGH + 단계 승격 trigger 미명시 중 + MVP-6 cross-reference 위험 중 |
| 트레이드오프 결론 | 즉시 강제 (Gemini) = 보안 高 + friction HIGH 비대칭 / 단계적 (GPT) = 점진 + 본 분석 답습 권고 |

### 2.4 3 Agent 일치 영역 (사전 식별)

| 영역 | A | B | C | 일치 |
|------|----|----|----|----|
| 종합 판정 = APPROVE WITH CONDITIONS | ✅ | ✅ | ✅ | **3/3 만장일치** |
| 합의 단위 = Group α 단독 | ✅ | ✅ | ✅ | 3/3 |
| 합의 형태 = (가) 풀 3+1 + 외부 LLM 입력 한정 + 사용자 명시 | ✅ | ✅ | ✅ | 3/3 |
| 14 결정 영역 GPT 답습 패턴 | ✅ (12/14) | ✅ (14/14) | ✅ (대안 후속 검토 외 적정) | 3/3 |
| Backlog #6 미진입 = HIGH 차단 요인 | ✅ | ✅ | ✅ | 3/3 |
| commit signing (Y) MVP-6 | ✅ | ✅ | ✅ | 3/3 |
| fork PR (3) default + `pull_request_target` BLOCK | ✅ | ✅ | ✅ | 3/3 |
| CODEOWNERS 핵심 경로 한정 (Gap #5) | ✅ | ✅ | ✅ | 3/3 |
| `pre-commit install` 단계적 (opt-in → doctor → required) | ✅ | ✅ | ✅ | 3/3 |
| AR-3 × PC-4 결합 = 유일 차단책 | ✅ | ✅ | ✅ | 3/3 |
| 5 영구 핵심 제약 5/5 보존 | ✅ | ✅ | ✅ | 3/3 |
| Provider Liquidity 5-way 보존 | ✅ | ✅ | ✅ | 3/3 |
| v1 / v2 / Group α brief 본문 변경 0건 | ✅ | ✅ | ✅ | 3/3 |
| §C-5/§C-5b/§C-5c/§C-6 재변경 0건 | ✅ | ✅ | ✅ | 3/3 |
| 외부 LLM 응답 = 입력 한정 (결론 강제 채택 0건) | ✅ | ✅ | ✅ | 3/3 |
| 사용자 명시 5 금지 모두 0건 | ✅ | ✅ | ✅ | 3/3 |
| 양 vendor 차이 2/2 GPT 답습 | ✅ | ✅ | ✅ | 3/3 |
| Group I cross-reference 영역 명시 의무 | ✅ | ✅ | ✅ | 3/3 |
| 5 잔존 우회 영역 (admin bypass / force push / required check 미등록 / token 탈취 / workflow 변조) | ✅ | ✅ | ✅ | 3/3 |

---

## 3. Phase 3 (Cross-Comparison) — 일치 / 부분 / 불일치 / 누락 분류

### 3.1 일치 (Consensus, 3개 모두 동의) — 19 영역

§2.4 답습 — **19/19 일치 영역**. 본 합의의 핵심 권위 source.

### 3.2 부분 일치 (Partial, 2개 동의 / 1개 이견) — 3 영역

| # | 영역 | A | B | C | 분석 |
|---|------|----|----|----|----|
| P-1 | branch protection 세부 6 옵션 채택 시점 | 즉시 가능 (즉시 + admin bypass OFF + 0 reviewer) | 부분 (Apply to administrators 활성 + 긴급 fallback 절차 별도 정의) | 대안 후속 검토 (§부록 명시 + 1인 self-admin 위험 평가 후) | **부분 일치 — Agent C = 후속 검토 권고 / A + B = 즉시 채택 권고** |
| P-2 | AR-2 본문 형태 (e) → (g) 단계적 승격 | (e) 채택 + Gemini (g) 통합은 후속 | (e) 채택 (1인 환경 균형) | (e) 채택 + (e) → (g) 단계적 승격 trigger 명시 신규 | **부분 일치 — Agent C = trigger 명시 추가 신규 / A + B = (e) 채택 권고** |
| P-3 | `fail_fast` 옵션 | `fail_fast: false` (양쪽 + 변경 파일 자연 발생) | 로컬 true (Gemini) + CI false (GPT) | 로컬 true + CI 별도 전체 리포트 | **부분 일치 — Agent A = false / B + C = 로컬 true** |

#### 3.2.1 P-1 부분 일치 분석 (branch protection 세부)

**Reviewer 평가**:
- Agent A (구현) + Agent B (보안) = 즉시 채택 권고 (기술 즉시 가능 + 보안 강도 高)
- Agent C (대안) = 후속 검토 권고 (1인 self-admin 위험 평가 + 신중한 접근)
- **합의 도출 → 본 합의 = "옵션 채택 권고 한정 + 실 활성화 시점 = Backlog #6 + 사용자 명시 결정 영역"** — 양쪽 합의 (Agent C 의 후속 검토 의도 = 실 활성화 신중 + Agent A/B 의 즉시 가능 = 옵션 채택 적합) 통합 가능.
- **최종 권고**: 6 옵션 中 (i) direct push 차단 + (ii) force push 차단 = 채택 (Agent A + B + C 모두 적합) / (iii) admin bypass = OFF (1인 유연성, Agent A) vs ON (보안 강도 高 + 긴급 fallback, Agent B) → **Reviewer 종합 = (iii) OFF + 긴급 fallback 절차 별도 정의 의무** (Agent A 1인 유연성 + Agent B 긴급 fallback 매트릭스 합산) / (iv) required PR review count = 0 (Agent A + B + C 모두 적합) / (v) required linear history = 채택 (Agent A + B) — Agent C 미언급 (누락) / (vi) required deployments = MVP-6 후속 (Agent A + B + C 모두 적합).

#### 3.2.2 P-2 부분 일치 분석 (AR-2 (e) → (g) 승격 trigger 명시)

**Reviewer 평가**:
- Agent A + B = (e) 채택 권고 (Gemini (g) 통합은 MVP-6 이후)
- Agent C = (e) 채택 + 단계 승격 trigger 명시 신규 (R-MVP1-G5-AR3-STAGE 1~3차 + AR3-SIGNING + AR3-MERGE-RESTRICT) — 양 vendor 미언급 영역
- **합의 도출 → 본 합의 = (e) 채택 + Agent C 신규 trigger 명시 의무 흡수** — Agent C 의 신규 영역 = "후속 합의 부담 ↓" 효과 + Agent A/B 와 충돌 0건 (보완 영역).
- **최종 권고**: (e) 채택 + R-MVP1-G5-AR3-STAGE 1~3차 (required check 도입 / CODEOWNERS 핵심 경로 / hook stage 확장) + R-MVP1-G5-AR3-SIGNING (commit signing MVP-6) + R-MVP1-G5-AR3-MERGE-RESTRICT (Hermes PMO 격상 시) trigger 명시 의무 (Agent C 신규 흡수).

#### 3.2.3 P-3 부분 일치 분석 (`fail_fast` 옵션)

**Reviewer 평가**:
- Agent A = `fail_fast: false` (양쪽 + CLI `--files` 변경 파일 한정 자연 발생 + 전체 리포트 확보)
- Agent B = 로컬 `true` (Gemini 권고 — 빠른 피드백) + CI `false` (GPT 권고 — 전체 리포트)
- Agent C = 로컬 `true` + CI `false` (Agent B 와 동일)
- **불일치 사유**: Agent A 가 *기술 한계* (pre-commit `fail_fast` CLI override 부재) 답습 → 동일 `.pre-commit-config.yaml` 사용 시 local + CI 양쪽 동일 정책 답습 강제 → "로컬 true / CI false 분리" = 별도 config 또는 env-aware logic 필요. Agent B/C 는 정책 권고 한정.
- **합의 도출 → 본 합의 = "옵션 채택 권고 + 기술 구현 = `.pre-commit-config.yaml` `fail_fast: false` (Agent A 답습) + 로컬 빠른 피드백 = CLI `--files <changed>` 패턴 (Agent A 답습) + CI 전체 리포트 = `pre-commit run --all-files` (Agent B + C 답습)"** — 기술적 한계 답습 + 정책 의도 답습 통합.
- **최종 권고**: `fail_fast: false` (config) + 로컬 = `pre-commit run --files <changed>` 자연 빠른 피드백 + CI = `pre-commit run --all-files` 전체 리포트 (Agent A 의 기술 한계 답습 + Agent B/C 의 정책 의도 답습 = 통합 가능).

### 3.3 불일치 (Divergence, 3개 모두 다른 의견) — 0 영역

3 Agent 모두 동일하거나 부분 일치 (3/3 만장일치 + 3 부분 일치 = 22/22 합산 적합). **불일치 0건**.

### 3.4 누락 (Gap, 특정 에이전트만 언급) — 6 영역

| # | 영역 | 출처 | 분석 |
|---|------|----|----|
| G-1 | GitHub App fine-grained permission **path-level scope 부재** 기술 한계 | Agent A | 본 합의에 흡수 — (γ) 전체 write + required check 결합 CODEOWNERS 핵심 경로로 *간접* 달성 |
| G-2 | ADR-012 §2.8 5 Layer cross-reference (Layer 2 force push 차단 + Layer 3 commit signing MVP-6) | Agent B | 본 합의에 흡수 — §6 cross-reference 영역 명시 |
| G-3 | ADR-008 부록 C 정합 (Hermes PMO Activation Cross-Reference 12 조건) | Agent B | 본 합의에 흡수 — §6 cross-reference 영역 명시 |
| G-4 | 단계 승격 trigger 7건 신규 (R-MVP1-G5-AR3-STAGE / SIGNING / MERGE-RESTRICT / G3-PC4T3-STAGE) | Agent C | 본 합의에 흡수 — §7 Rollback Trigger 매트릭스 |
| G-5 | 1인 환경 단계별 비용 정량 (opt-in 3~6h / doctor 10~16h / required 16~26h vs 즉시 강제 8~12h + friction HIGH) | Agent C | 본 합의에 흡수 — §5 적정성 평가 |
| G-6 | hosting provider alternative (GitLab / Bitbucket / Gitea) = Provider Liquidity 5-way 별도 영역 | Agent C | 본 합의 영역 외 명시 (§6 cross-reference 영역) — 별도 합의 의무 |

**누락 흡수 결론**: 6 누락 영역 모두 본 합의에 흡수 — 충돌 0건. Agent 별 분석 영역 다양성 = 합의 풍부도 증대.

### 3.5 Phase 3 매트릭스 합산

| 분류 | 영역 수 | 본 합의 처리 |
|----|----|----|
| 일치 (Consensus) | 19 | 그대로 채택 |
| 부분 일치 (Partial) | 3 | 소수 의견 평가 후 통합 (§3.2.1~§3.2.3) |
| 불일치 (Divergence) | 0 | — |
| 누락 (Gap) | 6 | 흡수 (§3.4) |

**합산**: 28 영역 모두 합의 도달. **3/3 만장일치 = APPROVE WITH CONDITIONS** 권위 강화.

---

## 4. Phase 4 (Consensus Resolution) — 최종 판단

### 4.1 본 합의 최종 판정 = **APPROVE WITH CONDITIONS**

| 영역 | 판정 |
|------|------|
| 종합 판정 | **APPROVE WITH CONDITIONS** (3/3 만장일치) |
| 합의 단위 | Group α 단독 (3/3 일치) — Group β / γ-1 / γ-2 분리 |
| 합의 형태 | (가) 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 (3/3 일치) |
| 합의 보고서 경로 | `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (v2 §4.1.1 답습 — `<TBD>` = 2026-05-14) |
| 외부 LLM 응답 결론 강제 채택 | ❌ 0건 (응답 = 입력 한정 — 본 합의 평가 결과 = 양 vendor 차이 2/2 GPT 답습 = 1인 환경 균형 + 단계적 + friction 회피 일관) |

### 4.2 본 합의 조건 (Conditions, 통합)

| # | 조건 | 출처 |
|---|------|----|
| C-1 | **Backlog #6 (Runtime + CI-hook) 미진입 시 *실 강제 적용 시점* 의존성 명시** | A + B + C 일치 |
| C-2 | **AI agent self-approval 차단 = Group I (Hermes-originated commit auto-reject) 별도 합의 결합 필수** | B + C 일치 (A 부분) |
| C-3 | **token rotation 정책 별도 합의 의무** (bot token 탈취 위험 완화 — GitHub App + 최소 권한 + 회전) | B + C 일치 |
| C-4 | **GitHub plan / ruleset 가용성 확인 의무** (Gap #4 GPT 흡수 — 본 합의 발효 전 사용자 명시 확인) | A + B + C 일치 |
| C-5 | **commit signing MVP-6 gap 근거 명시 의무** (1인 키 관리 부담 + Hermes PMO 미격상 + bot 정책 미정) | B 명시 + A + C 일치 |
| C-6 | **단계 승격 trigger 7건 명시 의무** (R-MVP1-G5-AR3-STAGE 1~3차 + AR3-SIGNING + AR3-MERGE-RESTRICT + G3-PC4T3-STAGE 1~3차) | C 신규 + A + B 답습 |
| C-7 | **5 잔존 우회 영역 완화책 합산 의무** (admin bypass / force push / required check 미등록 / token 탈취 / workflow 변조) | A + B + C 일치 |
| C-8 | **엣지케이스 9 영역 명시 의무** (1인 admin self-bypass / bot token 탈취 / 단계 승격 dev 일관성 / AI agent self-approval / doctor 변조 / CI timeout / bot 인간 충돌 / rule 변경 시도 / GitHub plan 변경) | B 명시 + A + C 부분 |
| C-9 | **branch protection 6 옵션 별 보안 강도 명시 + 옵션별 채택 의무** | B 명시 + A + C 일치 |
| C-10 | **AI agent 권한 범위 = 최소 권한 원칙 (least privilege) 답습 의무** | B 명시 + A + C 일치 |
| C-11 | **외부 LLM 응답 = 입력 한정 보존** (결론 강제 채택 0건) | A + B + C 일치 |
| C-12 | **본 합의 = DRAFT 한정 + 실 강제 적용 = 별도 사용자 명시 결정 영역** | A + B + C 일치 |

**합의 조건 합산**: **12 조건 충족 시 = 본 합의 진입 적합** + 본 합의 = "옵션 채택 권위 권고" 한정 (실 적용 = Backlog #6 + 사용자 명시 결정 영역).

---

## 5. Final Consensus 14 결정 영역 — 최종 합의 권고

### 5.1 AR-3 8 결정 영역 — 최종 합의 권고

| # | 결정 | **최종 합의 옵션** | 사유 (3/3 만장일치 + 부분 흡수) |
|---|------|----|----|
| 1 | AR-2 본문 형태 (a~g) | **(e) CODEOWNERS + required status check** | 양 vendor 차이 2/2 GPT 답습 / 1인 환경 균형 (A) + 보안 차원 적합 (B) + 대안 탐색 결과 v2 패턴 적정 (C) — 3/3 일치 |
| 2 | AR-1 + AR-2 통합 형태 (i/ii/iii) | **(ii) AR-1 + AR-2 (e)** + (e) → (g) **단계적 승격 trigger 명시** | Gemini (g) 통합은 MVP-6 이후 (A + B + C 일치) + Agent C 신규 trigger 흡수 (P-2 부분 일치 통합) |
| 3 | Hermes-originated commit auto-reject 통합 (α/β) | **(β) Group I 별도 합의 분리** | 책무 영역 다름 (5 영구 핵심 제약 #4 보존) — 3/3 일치 |
| 4 | commit signing 의무화 시점 (X/Y/Z) | **(Y) Operational Readiness 발효 시 (MVP-6)** ⭐ | 양 vendor 완전 수렴 + 1인 운영 비용 高 + Hermes PMO 격상 미발생 + bot 정책 미정 = gap 근거 명시 의무 (C-5) — 3/3 일치 |
| 5 | fork PR / external contributor 정책 (1/2/3) | **(3) 현 default 정책 유지 + `pull_request_target` BLOCK** | 양 vendor 완전 수렴 + secret 노출 CRITICAL 위험 차단 — 3/3 일치 |
| 6 | branch protection 세부 6 옵션 | (i) direct push 차단 + (ii) force push 차단 + (iii) admin bypass **OFF + 긴급 fallback 절차 별도 정의 의무** + (iv) required PR review count = **0** + (v) required linear history **선택적 채택** + (vi) required deployments **MVP-6 후속** | P-1 부분 일치 통합 (A 즉시 가능 + B 보안 강도 + C 후속 검토 → 통합 = 옵션 채택 권고 한정 + 실 활성화 = Backlog #6 + 사용자 명시) |
| 7 | AI agent / bot / GitHub App 권한 범위 (a~d) + 서명 + 영역 분리 | **권한 범위 = (b) GitHub App 한정** + **서명 = (iv) 미적용 (현 시점) → MVP-6 시 (iii) GitHub App auto-sign 승격** + **영역 분리 = (α) `tools/**` write only + (β) `docs/**` write only 분리 권고** (최소 권한 원칙 답습 — C-10) | Agent B 보안 차원 + Agent A 기술 한계 (GitHub App path-level scope 부재 G-1) + Agent C 대안 탐색 통합 |
| 8 | CODEOWNERS 적용 범위 + GitHub plan (Gap #4 + #5) | **CODEOWNERS = 핵심 경로 한정 (`docs/decisions/**` + `docs/architecture/**` + `tools/**` + `.github/workflows/**` + `.github/CODEOWNERS` + `.pre-commit-config.yaml` + catalog + `.importlinter` + `pyproject.toml`)** + **GitHub plan = (d) 현 plan 확인 후 옵션 가용성 명시 (C-4)** | 양 vendor 수렴 (GPT) + Agent B 보안 강화 확장 (`docs/architecture/**` + `.github/CODEOWNERS` 자체 + `.importlinter` + `pyproject.toml`) — 3/3 일치 + Agent B 확장 흡수 |

### 5.2 PC-4 T3 sub 6 결정 영역 — 최종 합의 권고

| # | 결정 | **최종 합의 옵션** | 사유 (3/3 만장일치 + 부분 흡수) |
|---|------|----|----|
| 9 | `pre-commit install` 강제 형태 | **단계적 (opt-in → doctor warning → required check)** ⭐ + **R-MVP1-G3-PC4T3-STAGE 1~3차 trigger 명시 (C-6)** | 양 vendor 차이 = GPT 답습 (개발자 friction 회피) — 3/3 일치 + Agent C 신규 trigger 흡수 |
| 10 | `default_install_hook_types` | **`pre-commit` + `commit-msg` 중심** + `pre-push` = smoke check only (GPT 답습) | 양 vendor 수렴 + dev 환경 fast feedback — 3/3 일치 |
| 11 | `fail_fast` | **`.pre-commit-config.yaml` `fail_fast: false`** + **로컬 = `pre-commit run --files <changed>` 자연 빠른 피드백** + **CI = `pre-commit run --all-files` 전체 리포트** | P-3 부분 일치 통합 (Agent A 기술 한계 답습 + Agent B/C 정책 의도 답습 통합) |
| 12 | `minimum_pre_commit_version` | **명시 (현 4.6.0 답습)** | 양 vendor 수렴 (GPT) — 3/3 일치 + supply chain 위험 완화 (Agent B) |
| 13 | 로컬 hook 실패 시 정책 | **"빠른 실패 + 명확한 복구 명령"** (GPT 답습) | dev workflow 차단 회피 — 3/3 일치 |
| 14 | `--no-verify` 차단 | **branch protection + required CI 결합** (양 vendor 완전 수렴) — 로컬 단독 차단 BLOCK | Defense in depth 본질 + 5 잔존 우회 영역 완화책 합산 (C-7) — 3/3 일치 |

### 5.3 14 결정 영역 합의 권고 합산 — 답습 패턴

| 답습 패턴 | 영역 수 |
|----|----|
| GPT 답습 (1인 환경 균형 + 단계적 + friction 회피) | **9건** (#1 / #2 / #5 / #6 (i)+(ii) / #8 + #9 / #10 / #12 / #13) |
| 양 vendor 완전 수렴 답습 | **5건** (#3 / #4 / #5 (재인용) / #11 / #14) |
| Agent C 신규 흡수 (단계 승격 trigger / branch protection 세부 통합) | **3건** (#2 trigger 명시 / #6 P-1 통합 / #9 trigger 명시) |
| Agent B 보안 확장 흡수 (CODEOWNERS 확장 + 최소 권한 원칙) | **2건** (#7 / #8) |
| Reviewer 통합 (P-3 `fail_fast` 기술 한계 + 정책 의도 통합) | **1건** (#11) |

**합산**: 14 결정 영역 모두 합의 도달 — **3/3 만장일치 + P-1/P-2/P-3 부분 일치 통합 + G-1~G-6 누락 흡수**.

---

## 6. Group I cross-reference + Backlog #6 의존성 + 기타 cross-reference

### 6.1 Group I cross-reference 영역 (Hermes-originated commit auto-reject)

| 영역 | 답습 |
|------|----|
| Group I 정의 | Hermes-originated commit auto-reject (G3 §2.2 #20 답습) — Hermes runtime 영역 한정 |
| Group α × Group I 결합 효과 | Defense in depth 高 — `--no-verify` 우회 차단 + Hermes-originated commit 식별 차단 |
| 분리 사유 | 책무 영역 다름 (Group α = GitHub repo / Group I = Hermes runtime) + 5 영구 핵심 제약 #4 (single source-of-truth) 보존 + Hermes ≠ root of trust 보존 (5 영구 핵심 제약 #1) |
| Group I 합의 미진입 시 영향 | Group α 단독 = "유일하게 유효한 차단책" 불완전 (잔존 Hermes 경로) — Backlog #6 Runtime + CI-hook 연결 의존성과 함께 후속 영역 |
| 본 합의 권고 | Group α 합의 발효 후 **Group I 별도 합의 진입 권고** (Defense in depth 결합) — 본 합의 영역 외 |

### 6.2 Backlog #6 (Runtime + CI-hook) 의존성

| 영역 | 답습 |
|------|----|
| 본 합의 발효 자체 | ✅ 가능 (Backlog #6 미진입 무관) |
| 실 강제 적용 시점 | ✅ **Backlog #6 연결 필수** (양 vendor 권고 답습 + 3 Agent 일치) |
| 실 강제 영역 | branch protection rule 활성화 + `pre-commit install` 단계적 (doctor / required) 도입 + CI step `pre-commit run --all-files` 도입 + `tools/doctor.py` 신규 도구 = 모두 Backlog #6 영역 |
| 본 합의 권고 | Backlog #6 (Runtime + CI-hook) 진입 brief 작성 = 본 합의 발효 후 우선 진입 권고 (양 vendor 권고 답습) |

### 6.3 기타 cross-reference 영역

| 영역 | 답습 |
|------|----|
| **ADR-008 부록 C** (Hermes PMO Activation Cross-Reference 12 조건) | Group α 합의 = Hermes PMO 격상 영향 0건 (조건 미진입) + commit signing MVP-6 권고 = §C.2 조건 8/9 정합 (Agent B 흡수) |
| **ADR-011 §2.1 (a)~(e) 5조건** | 본 합의 진입 시 평가 영역 — 본 합의 = 합의 적격성 권위 권고 한정 (Layer A / Layer B 패턴 답습) |
| **ADR-011 §2.3 (영구 권위 위계) + §2.4 (T3 영역)** | T3 영역 진입 — 풀 3+1 + 사용자 명시 발화 (양 vendor 수렴) |
| **ADR-012 §원칙 9 (Hermes ≠ root of trust)** | Group α = GitHub repo enforcement layer = Hermes 자기 검증 영역 진입 0건 |
| **ADR-012 §2.8 5 Layer** | Layer 2 force push 차단 = branch protection 정합 ⭐ / Layer 3 commit signing MVP-6 정합 ⭐ / Layer 4 CI 회귀 검증 = required CI 정합 ⭐ (Agent B 흡수) |
| **Group γ-2 (Vault HSM ST-4) cross-reference** | commit signing MVP-6 + Vault HSM MVP-6 + Hermes PMO 격상 = 동시 발효 부담 평가 영역 — 별도 합의 권고 (Agent C 신규) |
| **Group β cross-reference** | T-5 (β) + Tier-2/3 일반 — 책무 영역 다름 (분리 가능) — Group α 진입과 독립적 진행 가능 (v2 §4.3 답습) |
| **hosting provider alternative** (GitLab / Bitbucket / Gitea) | Provider Liquidity 5-way 보존 별도 합의 영역 — Group α = GitHub 한정 의존 + 후속 영역 (Agent C 신규 G-6) |

---

## 7. Rollback Trigger 통합 매트릭스 — Group α 한정 + 단계 승격 trigger 7건 (Agent C 신규 흡수)

### 7.1 v1 §7 + v2 §7 답습 — Group α 영역 한정

| Trigger | sub-영역 | 발화 조건 | 발화 시 행동 |
|--------|---------|---------|----------|
| **R-MVP1-G5-9** | (1) AR-3 | branch protection rule 변경 결정 (AR-2 진입) | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 (응답 회수 완료 — 입력 답습) |
| **R-MVP1-G3-3** | (3) PC-4 T3 sub | dev 환경 강제 정책 변경 결정 | 풀 3+1 합의 + 사용자 명시 |
| **ADR-011 §2.4 답습** | Group α 전체 | T3 영역 진입 결정 | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |

### 7.2 단계 승격 Trigger 7건 (Agent C 신규 흡수)

| Trigger | 단계 | 발화 조건 | 후속 합의 |
|--------|----|----|----|
| **R-MVP1-G5-AR3-STAGE 1차** | required status check 도입 | Group α 합의 발효 + Backlog #6 연결 | 별도 합의 |
| **R-MVP1-G5-AR3-STAGE 2차** | CODEOWNERS 핵심 경로 적용 | required check 안정화 후 | 별도 합의 |
| **R-MVP1-G5-AR3-SIGNING** | commit signing 도입 | MVP-6 Operational Readiness 발효 시 | 별도 풀 3+1 + 외부 LLM 1+ |
| **R-MVP1-G5-AR3-MERGE-RESTRICT** | merge restriction 도입 | Hermes PMO 격상 시 (12 조건 충족 후) | 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 |
| **R-MVP1-G3-PC4T3-STAGE 1차** | opt-in → doctor warning | Implementation Evidence PASS 발효 | 별도 합의 |
| **R-MVP1-G3-PC4T3-STAGE 2차** | doctor → required check | dev_env_install_rate ≥ 90% 측정 후 (정량 후보 — mvp1.md §4.5 답습) | 별도 합의 |
| **R-MVP1-G3-PC4T3-STAGE 3차** | required → hook stage 확장 (`commit-msg` + `pre-push`) | MVP-6 발효 + commit signing 도입 시점과 동시 | 별도 합의 |

### 7.3 후속 단계 Rollback Trigger 영역 (본 합의 영역 외)

| 영역 | 후속 합의 Rollback Trigger | 분리 사유 |
|------|----|----|
| 실 branch protection rule 적용 | Backlog #6 Runtime + CI-hook 연결 의무 | Backlog #6 영역 |
| 실 `pre-commit install` 의무화 도입 | Backlog #6 Runtime + CI-hook 연결 의무 | Backlog #6 영역 |
| commit signing MVP-6 진입 | Operational Readiness 발효 후 별도 합의 | MVP-6 영역 |
| `pull_request_target` 도입 (BLOCK 결정 변경 시) | 별도 풀 3+1 합의 + 외부 LLM 1+ | T3 영역 |
| token rotation 정책 | 별도 합의 (GitHub App + 최소 권한 + 회전) | MVP-6 영역 / Backlog #6 |
| Hermes-originated commit auto-reject (Group I) | 별도 합의 진입 권고 | Group I 영역 |
| hosting provider alternative (GitLab / Bitbucket / Gitea) | 별도 합의 (Provider Liquidity 5-way 보존) | 별도 영역 |

---

## 8. 다음 단계 (사용자 결정 영역, 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | **본 합의 그대로 승인 → 파일화 + commit + push (`docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`) → 사용자 명시 후속 단계 결정** | 본 합의 commit + push (1 commit) |
| (B) | 본 합의 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 합의 그대로 승인 → 파일화 + commit *까지만* (push 보류) | 1 commit |
| (D) | 본 합의 승인 + push → **Backlog #6 (Runtime + CI-hook) 우선 진입 brief 작성** (실 강제 적용 의존성 해소 권고) | 양 vendor 권고 답습 + 3 Agent 일치 |
| (E) | 본 합의 승인 + push → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief 작성** (Defense in depth 결합 권고) | 3 Agent C-2 일치 |
| (F) | 본 합의 승인 + push → **Group β (T-5 β + Tier-2/3 일반) policy/audit-only 합의 진입 brief** | v2 §9.1 우선순위 2 답습 |
| (G) | 본 합의 승인 + push → **Group γ-1 (C-5b ST-1) 분리 합의 진입 brief** (downstream wrapper preflight) | v2 §9.1 우선순위 3 답습 |
| (H) | 본 합의 승인 + push → **Group γ-2 (Vault HSM ST-4) MVP-6 보류 확정 단축 합의** (Reviewer-only 단축 합의 적격 여부 검토) | v2 §9.1 우선순위 4 답습 |
| (I) | 본 합의 보류 → 세션 종료 | — |

### 8.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 시작 명령 후보: "옵션 (A) 로 진행해주세요. 본 합의 그대로 승인하고, `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` commit + push."
- (D) 시작 명령 후보 (Backlog #6 우선 진입): "옵션 (D) 로 진행해주세요. 본 합의 답습 + Backlog #6 (Runtime + CI-hook) 우선 진입 brief 작성."
- (E) 시작 명령 후보 (Group I 별도 진입): "옵션 (E) 로 진행해주세요. 본 합의 답습 + Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief 작성."

---

## 9. 메타 검증

| 메타 검증 항목 | 본 합의 |
|---------|--------|
| 사용자 명시 진입 명령 답습 ("1로 진행" + Group α brief 작성 시 5 금지) | ✅ 본 합의 = Group α 풀 3+1 합의 *진입* 결과 |
| 사용자 명시 5 금지 답습 (branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Hermes PMO 격상 / Operational Readiness PASS) | ✅ 모두 0건 (본 합의 = 수단 결정 권위 권고 한정) |
| 본 합의 = DRAFT 한정 (commit 0건 / push 0건) | ✅ 헤더 + §0.4 |
| **Group α brief (`db0e3ac`) 본문 변경 0건** (보존 + 본 합의 = 별도 권위 source) | ✅ §0.4 |
| **v1 (`ad9a02d`) / v2 (`2a9d02d`) 본문 변경 0건** | ✅ §0.4 |
| 외부 LLM 응답 (`8b5b626`) = 입력 한정 (결론 강제 채택 0건) | ✅ §0.3 + §1.3 + §4.1 |
| Phase 1 (Distribution) — Group α brief + 3 Agent 관점 분배 | ✅ §1 |
| Phase 2 (Independent Analysis) — Agent A/B/C 병렬 독립 분석 (편향 방지) | ✅ §2 (Agent A `ac77013744a824b0a` + Agent B `a96888c30f3f5fad3` + Agent C `a8614701ff15ed25d` 모두 다른 Agent / Reviewer 출력 미참조 확인) |
| Phase 3 (Cross-Comparison) — 일치 19 / 부분 일치 3 / 불일치 0 / 누락 6 | ✅ §3 |
| Phase 4 (Consensus Resolution) — 12 조건 + 최종 판단 | ✅ §4 |
| Phase 5 (Report) — 14 결정 영역 최종 권고 | ✅ §5 |
| 14 결정 영역 모두 합의 도달 | ✅ §5.1 + §5.2 (3/3 만장일치 + P-1/P-2/P-3 통합 + G-1~G-6 흡수) |
| Group I cross-reference + Backlog #6 의존성 + ADR cross-reference | ✅ §6 |
| Rollback Trigger 통합 매트릭스 (R-MVP1 7건 + 단계 승격 trigger) | ✅ §7 |
| **§C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* 0건** | ✅ (`78483c5` + `8ba5182` 권위 source 보존) |
| **Layer A (`f1e0b23`) / Layer B (`f40423f`) §5.5 9 sub-수단 본문 채택 변경 0건** | ✅ |
| **Layer D (`210c98f`) 본문 변경 0건 (A-1 답습)** | ✅ |
| `tools/*.py` / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건 | ✅ |
| ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ✅ |
| Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건 | ✅ (Backlog #6 = 후속 단계 권고만) |
| Group β / γ-1 / γ-2 자동 진입 0건 | ✅ |
| 5 영구 핵심 제약 5/5 보존 | ✅ §1.4 Agent B 검증 + §4 Reviewer 검증 |
| Provider Liquidity 5-way 보존 | ✅ §1.5 Agent B 검증 |
| Hermes upstream 변경 0건 보존 | ✅ Group α = GitHub repo 영역 한정 |
| MVP-1 PASS 재선언 0건 / MVP-2 자동 진입 0건 | ✅ |
| Operational Readiness PASS 0건 / Hermes PMO 격상 0건 | ✅ (사용자 명시 답습) |
| 외부 LLM 추가 자동 호출 0건 / 결론 강제 채택 0건 | ✅ |
| 실 API key / provider SDK / 외부 API 호출 0건 | ✅ |
| Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경 0건 | ✅ |
| 인간 리뷰 의무 자동 발화 0건 (Hermes PMO 격상 시 의무) | ✅ |

### 9.1 본 합의가 *발생시키는* 것

- Backlog #3 Group α (AR-3 + PC-4 T3 sub) *수단 결정 적격성 권위 권고 발행* (Layer A / Layer B 패턴 답습)
- 14 결정 영역 *최종 합의 권고* (§5)
- 12 합의 조건 (C-1 ~ C-12) 명시
- 단계 승격 Trigger 7건 명시 (R-MVP1-G5-AR3-STAGE 1~3차 + AR3-SIGNING + AR3-MERGE-RESTRICT + G3-PC4T3-STAGE 1~3차)
- Group I cross-reference 영역 + Backlog #6 의존성 + ADR cross-reference 명시
- Phase 2 Independent Analysis 3 Agent 보고서 통합 답습 + Phase 3 교차 비교 + Phase 4 합의 도출 + Phase 5 보고서 발행
- 양 vendor 응답 (`8b5b626`) 평가 결과 = 차이 2/2 GPT 답습 (1인 환경 균형 + 단계적 + friction 회피 일관) + 수렴 영역 채택
- 본 합의 발효 후 *다음 단계* 권고 (Backlog #6 우선 / Group I 별도 / Group β/γ-1/γ-2 별도 / 세션 종료)

### 9.2 본 합의가 *발생시키지 않는* 것 (§0.3 답습 + 추가)

- ❌ branch protection rule *실 변경* (CODEOWNERS 등록 / required check 등록 / commit signing 활성화 / merge restriction 설정 / direct push 차단 활성화 / force push 차단 활성화 / admin bypass 정책 변경 / required reviewer 설정 / ruleset 신설)
- ❌ dev 환경 *실 강제* (`pre-commit install` 의무화 실 활성화 / `.git/hooks` 자동 install 실 도입 / `default_install_hook_types` 실 추가 / `fail_fast` 실 활성화 / `commit-msg` / `pre-push` stage 실 추가 / `minimum_pre_commit_version` 실 명시 / `--no-verify` 실 차단)
- ❌ Hermes PMO 격상 (Layer F) 선언
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Group β / γ-1 / γ-2 자동 진입
- ❌ Backlog #1 / #2 / #4 / #6 / #7 자동 진입 (Backlog #6 = 후속 단계 권고만)
- ❌ v1 / v2 / Group α brief 본문 변경
- ❌ §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*
- ❌ Layer A / Layer B §5.5 9 sub-수단 본문 채택 변경
- ❌ Layer D 본문 변경
- ❌ MVP-1 PASS *재선언* / MVP-2 자동 진입
- ❌ 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정 + 본 합의 평가 대상)
- ❌ 외부 LLM 추가 자동 호출 / cross-vendor blind 의뢰 자동 재발송
- ❌ 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리
- ❌ ADR 본문 자동 갱신
- ❌ 도구 본문 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경
- ❌ Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경
- ❌ 5 영구 핵심 제약 약화 / Provider Liquidity 5-way 약화
- ❌ 인간 리뷰 의무 자동 발화 (Hermes PMO 격상 시 의무 — 본 합의 영역 외)
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 (별도 합의 영역)
- ❌ token rotation 정책 / hosting provider alternative 자동 진입 (별도 합의 영역)
- ❌ C-1 ~ C-8 자동 변경
- ❌ ADR-010 §X 신규 추가 / ADR-015 신설
- ❌ 사용자 명시 3 결정 (α/ii/(가)) 재변경

---

## 10. 본 합의 요약 (한 단락)

**Backlog #3 Group α (AR-3 + PC-4 T3 sub) 단독 풀 3+1 합의** = **APPROVE WITH CONDITIONS** (Agent A + B + C **3/3 만장일치**). Phase 1 (Distribution, Group α brief `db0e3ac` 답습 + 3 Agent 관점 분배) + Phase 2 (Independent Analysis, Agent A 구현 + Agent B 안전성 + Agent C 대안 병렬 독립 분석 — 편향 방지 의무 답습) + Phase 3 (Cross-Comparison, **일치 19 + 부분 일치 3 + 불일치 0 + 누락 6**) + Phase 4 (Consensus Resolution, **12 조건 (C-1 ~ C-12) 충족 시 진입 적합**) + Phase 5 (Report, 14 결정 영역 최종 권고) 완결. **3 부분 일치 (P-1 branch protection 세부 + P-2 AR-2 (e) → (g) 단계적 승격 trigger + P-3 `fail_fast` 옵션) 모두 통합 해결** (A 즉시 가능 + B 보안 강도 + C 후속 검토 → 옵션 채택 권고 한정 + 실 활성화 = Backlog #6 + 사용자 명시 결정 영역 답습 / Agent C 신규 trigger 명시 의무 흡수 / Agent A 기술 한계 + Agent B/C 정책 의도 통합). **6 누락 영역 모두 본 합의 흡수** (G-1 GitHub App path-level scope 부재 + G-2 ADR-012 §2.8 Layer 1~5 cross-reference + G-3 ADR-008 부록 C 정합 + G-4 단계 승격 trigger 7건 + G-5 1인 환경 단계별 비용 정량 + G-6 hosting provider alternative). **14 결정 영역 최종 권고**: AR-3 8건 (AR-2 (e) CODEOWNERS + required status check / AR-1 + AR-2 (ii) + (e) → (g) 단계적 승격 trigger 명시 / Hermes-originated commit auto-reject (β) Group I 별도 합의 분리 / commit signing (Y) MVP-6 + gap 근거 명시 / fork PR (3) default + `pull_request_target` BLOCK / branch protection 6 옵션 ((i) direct push 차단 + (ii) force push 차단 + (iii) admin bypass OFF + 긴급 fallback / (iv) 0 reviewer / (v) linear history 선택적 / (vi) deployments MVP-6 후속) / AI agent 권한 = (b) GitHub App 한정 + 서명 (iv) → MVP-6 시 (iii) auto-sign + 영역 분리 (α) `tools/**` write only + (β) `docs/**` write only / CODEOWNERS = 핵심 경로 한정 (10 경로) + GitHub plan (d) 현 plan 확인 후 가용성 명시) + PC-4 T3 sub 6건 (`pre-commit install` 단계적 (opt-in → doctor → required) + R-MVP1-G3-PC4T3-STAGE 1~3차 trigger / `default_install_hook_types` = `pre-commit` + `commit-msg` 중심 + `pre-push` smoke check only / `fail_fast: false` config + 로컬 `--files <changed>` 자연 빠른 피드백 + CI `--all-files` 전체 리포트 / `minimum_pre_commit_version` 4.6.0 명시 / "빠른 실패 + 명확한 복구 명령" / `--no-verify` 차단 = branch protection + required CI 결합). **답습 패턴**: GPT 답습 9건 + 양 vendor 완전 수렴 5건 + Agent C 신규 흡수 3건 + Agent B 보안 확장 2건 + Reviewer 통합 1건 — **1인 환경 균형 + 단계적 + friction 회피 일관성**. **양 vendor 차이 영역 2/2 모두 GPT 답습** (Q1 AR-3 옵션 + Q2 PC-4 강제 형태) = 본 합의 평가 결과 = v2 패턴 적정 답습. **양 vendor 수렴 핵심 (Group α)**: AR-3 진입 가능 (1순위) + commit signing MVP-6 + `--no-verify` = branch protection 결합 + fork PR BLOCK + `pre-commit install` 단계적 + AR-3 × PC-4 = 유일 차단책 + provider lock-in 역효과 완화 + 1인 환경 부담 최소화 답습. **차단 요인**: Backlog #6 미진입 = HIGH (실 강제 적용 시점 의존 — C-1) + AI agent self-approval 차단 미실시 = HIGH (Group I 결합 의무 — C-2) + token rotation 정책 별도 합의 = HIGH (C-3) + GitHub plan / ruleset 가용성 미확인 = HIGH (Gap #4 — C-4) + commit signing MVP-6 gap 근거 미명시 = 중 (C-5) + 단계 승격 trigger 미명시 = 중 (C-6) + 5 잔존 우회 영역 완화책 미실시 = 중 (C-7) + 엣지케이스 9 영역 미명시 = 중 (C-8). **Group I cross-reference 영역**: Hermes-originated commit auto-reject = 별도 합의 분리 (책무 영역 다름 + 5 영구 핵심 제약 #4 보존) — Group α 합의 발효 후 진입 권고 (Defense in depth 결합). **Backlog #6 의존성**: 본 합의 발효 자체 = 가능 + 실 강제 적용 시점 = Backlog #6 연결 필수 (양 vendor 권고 답습 + 3 Agent 일치) — 본 합의 발효 후 Backlog #6 우선 진입 brief 작성 권고. **5 영구 핵심 제약 5/5 보존** (Hermes ≠ root of trust + 단일 source-of-truth + 수단/목적 분리 + T1/T2/T3 분리 + SPOF 의도적 수용) + **Provider Liquidity 5-way 100% 보존** (Group α = enforcement layer = catalog / provider 영역과 직교). **본 합의 ≠ 합의 발효** (합의 자체 = 별도 사용자 명시 승인 영역 — 부록 A 옵션 (A)~(I)) + **§C-5 / §C-5b / §C-5c / §C-6 재변경 0건** + **Layer A / Layer B §5.5 9 sub-수단 본문 채택 변경 0건** + **Layer D 본문 변경 0건** + **v1 / v2 / Group α brief 본문 변경 0건** + **실 변경 0건** (branch protection rule 활성화 / dev 환경 실 강제 / `pre-commit install` 의무화 / 도구 본문 / `.importlinter` / `.pre-commit-config.yaml` / CI workflow / Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경 모두 0건) + **외부 LLM 응답 = 입력 한정 결론 강제 채택 0건** + **외부 LLM 추가 자동 호출 0건** + **ADR 본문 자동 갱신 0건** + **Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건** + **Group β / γ-1 / γ-2 자동 진입 0건** + **Group I 자동 진입 0건** + **MVP-1 PASS 재선언 0건** + **MVP-2 자동 진입 0건** + **Operational Readiness PASS 0건** + **Hermes PMO 격상 0건** + **인간 리뷰 의무 자동 발화 0건**. 다음 단계 = 사용자 결정 영역 (부록 A 옵션 (A)~(I)).

---

## 부록 A. 다음 단계 결정 옵션 (사용자 결정 영역)

§8 답습 + 추가 — 사용자 명시 결정 의무 영역 (자동 진입 0건).

| 옵션 | 영역 | 후속 단계 | 양 vendor / 3 Agent 권고 |
|-----|------|--------|----|
| (A) | 본 합의 그대로 승인 → 파일화 + commit + push | 1 commit | 표준 답습 |
| (B) | 본 합의 일부 수정 → v2 작성 | 본 합의 v2 작성 후 사용자 승인 | — |
| (C) | 본 합의 승인 → commit *까지만* (push 보류) | 1 commit | — |
| **(D)** ⭐ | 본 합의 승인 + push → **Backlog #6 (Runtime + CI-hook) 우선 진입 brief 작성** | 양 vendor 권고 + 3 Agent 일치 답습 | **권고 1순위** |
| (E) | 본 합의 승인 + push → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief 작성** | 3 Agent C-2 일치 답습 (Defense in depth 결합) | 권고 2순위 |
| (F) | 본 합의 승인 + push → **Group β (T-5 β + Tier-2/3 일반) policy/audit-only 합의 진입 brief** | v2 §9.1 우선순위 2 답습 | 권고 3순위 |
| (G) | 본 합의 승인 + push → **Group γ-1 (C-5b ST-1) 분리 합의 진입 brief** | v2 §9.1 우선순위 3 답습 | 권고 4순위 |
| (H) | 본 합의 승인 + push → **Group γ-2 (Vault HSM ST-4) MVP-6 보류 확정 단축 합의** | v2 §9.1 우선순위 4 답습 + 양 vendor 완전 수렴 | 권고 5순위 (Reviewer-only 단축 적격 가능성 검토) |
| (I) | 본 합의 보류 → 세션 종료 | — | — |

### A.1 권고 시작 명령 (사용자 명시 결정 영역)

- **(A) 시작 명령 후보**: "옵션 (A) 로 진행해주세요. 본 합의 그대로 승인하고, `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` commit + push."
- **(D) 시작 명령 후보 (Backlog #6 우선)**: "옵션 (D) 로 진행해주세요. 본 합의 답습 + Backlog #6 (Runtime + CI-hook implementation) 우선 진입 brief 작성. Group α 실 강제 적용 의존성 해소."
- **(E) 시작 명령 후보 (Group I 별도 진입)**: "옵션 (E) 로 진행해주세요. 본 합의 답습 + Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief 작성. Defense in depth 결합 (Group α + Group I)."

---

## 부록 B. 금지 사항 (사용자 명시 5 금지 + 추가 답습)

### B.1 사용자 명시 5 금지 답습 (Group α brief 작성 시점 명령)

| # | 금지 | 본 합의 위반 |
|---|------|------------|
| 1 | **branch protection 변경** (실 변경) | 0건 (수단 결정 권위 권고 한정) |
| 2 | **dev 환경 강제** (실 강제) | 0건 |
| 3 | **`pre-commit install` 의무화** (실 의무화) | 0건 (단계적 권고 한정) |
| 4 | **Hermes PMO 격상 (Layer F)** | 0건 (MVP-6 + 외부 LLM 의무 영역) |
| 5 | **Operational Readiness PASS (Layer E)** | 0건 (MVP-6 + Backlog #7 영역) |

### B.2 추가 금지 (본 합의 자체)

- ❌ Group β / γ-1 / γ-2 자동 진입 0건
- ❌ T3 영역 *수단 결정의 실 적용* / *도입* / *본문 채택 commit* 0건 (수단 결정 권위 권고 한정 — 실 적용 = Backlog #6 + 사용자 명시 결정 영역)
- ❌ Group α brief (`db0e3ac`) / v1 (`ad9a02d`) / v2 (`2a9d02d`) 본문 변경 0건 (보존 + 본 합의 = 별도 권위 source)
- ❌ Reviewer-only 단축 합의 적격성 발화 0건 (T3 영역 의무 — 풀 3+1 의무 답습)
- ❌ 외부 LLM *추가 자동 호출* / cross-vendor blind 의뢰 자동 재발송 0건
- ❌ **외부 LLM 응답 *결론 강제 채택* 0건** (응답 = 입력 한정 — 본 합의 평가 결과 = 양 vendor 권고 평가 후 채택 패턴 = 일관성)
- ❌ 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 0건
- ❌ ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
- ❌ §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* 0건 (`78483c5` + `8ba5182` 권위 source 보존)
- ❌ Layer A (`f1e0b23`) / Layer B (`f40423f`) §5.5 9 sub-수단 본문 채택 변경 0건
- ❌ Layer D (`210c98f`) 본문 변경 0건 (A-1 답습)
- ❌ 도구 본문 (`tools/*.py`) 변경 0건
- ❌ `.importlinter` / `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 0건
- ❌ CI workflow 변경 0건
- ❌ Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경 0건
- ❌ Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건 (Backlog #6 = 후속 단계 권고만)
- ❌ MVP-1 PASS *재선언* 0건
- ❌ MVP-2 자동 진입 0건
- ❌ 5 영구 핵심 제약 약화 / Provider Liquidity 5-way 약화 0건
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리)
- ❌ ADR-010 §X 본문 신규 추가 / ADR-015 신설 0건
- ❌ 인간 리뷰 의무 자동 발화 0건 (Hermes PMO 격상 시 의무 — 본 합의 영역 외)
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건 (별도 합의 영역)
- ❌ token rotation 정책 / hosting provider alternative 자동 진입 0건 (별도 합의 영역)
- ❌ 사용자 명시 3 결정 (α/ii/(가)) 재변경 0건

---

## 부록 C. 외부 LLM 응답 정합 매트릭스 + Phase 3 분류 매트릭스

### C.1 외부 LLM 양 vendor 응답 = 입력 한정 답습 (`8b5b626`)

| Vendor | 응답 | 종합 판정 |
|------|----|----|
| Gemini 3 Flash | 114줄 (Q1 (g) 전체 통합 + Q2 즉시 강제) | (C) PARTIAL |
| GPT-5.5 Thinking | 390줄 (Q1 (e) 단계적 + Q2 단계적 opt-in → doctor → required) | (C) PARTIAL |

### C.2 양 vendor 수렴 영역 (Group α 한정) — 6 영역 답습

| 영역 | 양 vendor 수렴 | 본 합의 채택 위치 |
|----|----|----|
| AR-3 진입 가능성 (Group α 우선순위 1) | 양쪽 동의 | §5.1 + §4 |
| commit signing 시점 = MVP-6 | 양쪽 동의 | §5.1 #4 |
| `--no-verify` 차단 = branch protection 결합 필수 | 양쪽 동의 | §5.2 #14 |
| fork PR `pull_request_target` BLOCK | 양쪽 동의 | §5.1 #5 |
| AR-3 × PC-4 결합 = 유일하게 유효한 차단책 | 양쪽 동의 | §5.1 + §5.2 (Defense in depth) |
| `pre-commit install` 단계적 | Gemini = 즉시 / GPT = 단계적 (v2 = GPT 답습) — 양쪽 권고 답습 | §5.2 #9 |

### C.3 양 vendor 차이 영역 (Group α 한정) — 2 영역 + 본 합의 채택 패턴

| 영역 | Gemini 권고 | GPT 권고 | v2 채택 | 본 합의 채택 | 채택 사유 |
|----|----|----|----|----|----|
| Q1 AR-3 옵션 | (g) 전체 통합 | (e) 단계적 | **GPT** | **GPT 답습** | 1인 환경 균형 (3 Agent 일치) |
| Q2 PC-4 강제 형태 | 즉시 | 단계적 | **GPT** | **GPT 답습** | 개발자 friction 회피 (3 Agent 일치) |

**패턴**: 2/2 GPT 답습 — 일관성 (1인 환경 균형 + 단계적 + friction 회피).

### C.4 Gap 흡수 매트릭스 (Group α 한정) — 4 영역

| Gap # | 지적 영역 | vendor | v2 흡수 위치 | 본 합의 흡수 위치 |
|---|----|----|----|----|
| 1 | AI agent / bot / GitHub App 권한 + 서명 방식 | Gemini | v2 §2.1.4 + §3.1.5 | §5.1 #7 |
| 3 | branch protection 세부 (direct push / force push / admin bypass) | GPT | v2 §2.1.3 + §3.1.3 | §5.1 #6 |
| 4 | GitHub plan / 권한 제약 | GPT | v2 §2.1.5 + §3.1.6 | §5.1 #8 + C-4 |
| 5 | CODEOWNERS 1인 한계 ("재확인 friction") | GPT | v2 §2.1.3 + §3.1.4 + §11 | §5.1 #8 |

### C.5 Phase 3 분류 매트릭스 (Reviewer 종합)

| 분류 | 영역 수 | 비고 |
|----|----|----|
| **일치 (Consensus)** | 19 | §2.4 매트릭스 답습 — 본 합의 핵심 권위 source |
| **부분 일치 (Partial)** | 3 | P-1 (branch protection 세부 채택 시점) + P-2 (AR-2 (e) → (g) 단계적 승격 trigger) + P-3 (`fail_fast` 옵션) — 모두 통합 해결 |
| **불일치 (Divergence)** | 0 | — |
| **누락 (Gap, 특정 에이전트만 언급)** | 6 | G-1 GitHub App path-level scope 부재 (Agent A) + G-2 ADR-012 §2.8 5 Layer cross-reference (Agent B) + G-3 ADR-008 부록 C 정합 (Agent B) + G-4 단계 승격 trigger 7건 신규 (Agent C) + G-5 1인 환경 단계별 비용 정량 (Agent C) + G-6 hosting provider alternative (Agent C) — 모두 본 합의 흡수 |

### C.6 12 합의 조건 추적 매트릭스

| # | 조건 | 출처 | 본 합의 처리 |
|---|------|----|----|
| C-1 | Backlog #6 미진입 시 실 강제 적용 시점 의존성 명시 | A + B + C 일치 | §6.2 + §8 (D) 옵션 권고 |
| C-2 | AI agent self-approval 차단 = Group I 별도 합의 결합 필수 | B + C 일치 (A 부분) | §6.1 + §8 (E) 옵션 권고 |
| C-3 | token rotation 정책 별도 합의 의무 | B + C 일치 | §6.3 cross-reference + 별도 합의 영역 명시 |
| C-4 | GitHub plan / ruleset 가용성 확인 의무 | A + B + C 일치 | §5.1 #8 + 본 합의 발효 전 사용자 명시 확인 |
| C-5 | commit signing MVP-6 gap 근거 명시 의무 | B 명시 + A + C 일치 | §5.1 #4 + Agent B §6 답습 |
| C-6 | 단계 승격 trigger 7건 명시 의무 | C 신규 + A + B 답습 | §7.2 R-MVP1 7건 매트릭스 |
| C-7 | 5 잔존 우회 영역 완화책 합산 의무 | A + B + C 일치 | §5.1 #6 + Agent B §5 답습 |
| C-8 | 엣지케이스 9 영역 명시 의무 | B 명시 + A + C 부분 | Agent B §10 답습 + 본 합의 §6 cross-reference |
| C-9 | branch protection 6 옵션 별 보안 강도 명시 + 옵션별 채택 의무 | B 명시 + A + C 일치 | §5.1 #6 |
| C-10 | AI agent 권한 범위 = 최소 권한 원칙 (least privilege) 답습 의무 | B 명시 + A + C 일치 | §5.1 #7 |
| C-11 | 외부 LLM 응답 = 입력 한정 보존 (결론 강제 채택 0건) | A + B + C 일치 | §0.3 + §1.3 + §4.1 + 부록 C |
| C-12 | 본 합의 = DRAFT 한정 + 실 강제 적용 = 별도 사용자 명시 결정 영역 | A + B + C 일치 | §0.4 + §8 + §9 |

### C.7 답습 패턴 합산 매트릭스

| 답습 패턴 | 영역 수 | 본 합의 권위 source |
|----|----|----|
| GPT 답습 (양 vendor 차이 영역 + Gap #3/#4/#5/#6 흡수) | 9건 | 1인 환경 균형 + 단계적 + friction 회피 일관성 |
| 양 vendor 완전 수렴 답습 (Q1 AR-3 / Q2 PC-4 / Q3 `--no-verify` / Q4 fork PR / Q5 commit signing) | 5건 | 양 vendor 동의 — 최강 권위 |
| Agent C 신규 흡수 (단계 승격 trigger + branch protection 세부 통합) | 3건 | 양 vendor 미언급 영역 — Phase 2 신규 발견 |
| Agent B 보안 확장 흡수 (CODEOWNERS 확장 + 최소 권한 원칙 + 5 영구 핵심 제약 답습) | 2건 | Phase 2 보안 차원 추가 |
| Reviewer 통합 (P-3 `fail_fast` 기술 한계 + 정책 의도 통합) | 1건 | Phase 3-4 통합 |

**합산**: 20 답습 영역 (일부 중복) — 14 결정 영역 + 6 cross-reference / 후속 영역.

---

**상태**: APPROVED WITH CONDITIONS — Phase 5 (Report) 완료 + 사용자 명시 승인 *전*, 파일화 + commit 0건
**다음 단계**: 사용자 명시 결정 영역 (부록 A 옵션 (A)~(I))
**합의 권위 영역**:
- (a) **수단 결정 적격성 권위 권고 발행** (Layer A / Layer B 패턴 답습)
- (b) **14 결정 영역 최종 합의 권고** (3/3 만장일치 + 부분 일치 3건 통합 + 누락 6건 흡수)
- (c) **12 합의 조건 (C-1 ~ C-12) 명시**
- (d) **단계 승격 Trigger 7건 명시** (R-MVP1-G5-AR3-STAGE 1~3차 + AR3-SIGNING + AR3-MERGE-RESTRICT + G3-PC4T3-STAGE 1~3차)
- (e) **Group I cross-reference + Backlog #6 의존성 + ADR cross-reference 명시**
- (f) **양 vendor 응답 (`8b5b626`) 평가 결과 = 차이 2/2 GPT 답습 (1인 환경 균형 + 단계적 + friction 회피 일관)**
- (g) **본 합의 발효 후 다음 단계 권고** (Backlog #6 우선 (D) / Group I 별도 (E) / Group β/γ-1/γ-2 별도 (F/G/H) / 세션 종료 (I))
