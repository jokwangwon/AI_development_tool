# MVP-1 GitHub Actions Node.js 20 → 24 마이그레이션 sub-cycle brief

> **scope**: 46번째 entry D-6 workflow re-run log 발견 — GitHub Actions Node.js 20 deprecation 경고 (**2026-06-16** 강제 Node.js 24 default — v1.1 정정 codex N-1 답습, 공식 source 답습 본 brief 작성 시점 + 20일). 12 workflow 의 3 종 actions (checkout v4 / setup-python v5 / upload-artifact v4) 최신 major version (v6 / v6 / v7) upgrade — Node.js 24 호환성 보장.
>
> **본 brief 자체에서 실 코드 변경 0건 의무**.
>
> **합의 형태 (사용자 결정 영역)**: §6 매트릭스 답습 — 권고 = 단축 + 외부 LLM 1+ cross-validation.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **GitHub Actions deprecation 공지** | https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ | **2026-06-16** 강제 Node.js 24 default + 2026-09-16 Node.js 20 runner 제거 (v1.1 정정 — codex cross-vendor 공식 source 답습) |
| **46번째 entry CI log (실 발견 source)** | run 26508931246 log (D-6 workflow re-run) | "Node.js 20 actions are deprecated... actions/checkout@v4, actions/setup-python@v5..." |
| **12 workflow audit (현 상태)** | `.github/workflows/*.yml` (12 file) | `actions/checkout@v4` × 12 + `actions/setup-python@v5` × 11 + `actions/upload-artifact@v4` × 8 |
| **upload-artifact v4 → v5 breaking change** | https://github.com/actions/upload-artifact/blob/main/docs/MIGRATION.md | artifact name uniqueness required (동일 name 중복 불가) — 본 audit 결과 8 workflow 모두 unique → 영향 0 ✅ |
| **R-7(b) PC1-2 차등 답습** | 24번째 entry 합의 line 94 | catalog 본문 변경 = 풀 3+1 자격 / version pin update = 단축 자격. 본 cycle = action version pin update (의존성 update) |

---

## §1 scope

### 1.1 본 sub-cycle 본질

| 항목 | 내용 |
|---|---|
| scope | 12 workflow 의 3 종 actions major version upgrade (`@v4`/`@v5` → `@v6`/`@v7`) — Node.js 24 호환성 보장 |
| 합의 형태 권고 | §6 매트릭스 답습 |
| 변경 영역 | `.github/workflows/*.yml` 12 file 31 위치 (action `uses:` line update) |
| 변경 0건 의무 | workflow job/step 로직 본문 0, tools/ 0, src/ 0, branch protection rule 0, `.pre-commit-config.yaml` 0, `.githooks/` 0, ADR 0, 헌법 0, roadmap 본문 0, MVP-1 Implementation Evidence PASS 재선언 0, Operational Readiness PASS 0, Hermes PMO 격상 0, adapters/llm/facade.py 0, Tier-2/3 catalog 확장 0 |

### 1.2 본 sub-cycle 하지 *않는* 것

| # | 항목 | 자격 |
|---|---|---|
| 1 | workflow job/step 로직 변경 | 0건 (action version pin update 한정) |
| 2 | branch protection contexts 갱신 | 0건 (8 contexts 답습 유지) |
| 3 | secret-scanner / .pre-commit-config / hook 본문 | 0건 |
| 4 | Hermes PMO 격상 | 0건 |
| 5 | MVP-2 자동 진입 | 0건 |

---

## §2 upgrade 매트릭스 (12 workflow 31 위치)

### 2.1 action upgrade

| Action | 현 | 목표 | release 시점 |
|---|---|---|---|
| `actions/checkout` | v4 | **v6** (v6.0.2) | 2026-01-09 |
| `actions/setup-python` | v5 | **v6** (v6.2.0) | 2026-01-22 |
| `actions/upload-artifact` | v4 | **v7** (v7.0.1) | 2026-04-10 |

### 2.2 workflow 별 변경 매트릭스

| Workflow | checkout | setup-python | upload-artifact | 총 |
|---|---|---|---|---|
| boundary-guard.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| evidence-pass-gate.yml | v4→v6 | v5→v6 | — | 2 |
| g4-hash-chain.yml | v4→v6 | v5→v6 | — | 2 |
| history-anchor-verifier.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| memory-skill-migration-feasibility.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| pre-commit-bypass-detection.yml | v4→v6 | v5→v6 | — | 2 |
| provider-adapter-enforcement.yml | v4→v6 | v5→v6 | — | 2 |
| provider-url-scanner.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| r2-canary.yml | v4→v6 | — | v4→v7 | 2 |
| rewrite-defense.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| schema-validation.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| secret-hygiene-egress-redaction.yml | v4→v6 | v5→v6 | v4→v7 | 3 |
| **합계** | **12** | **11** | **8** | **31** |

---

## §3 breaking change audit + 영향 검증

### 3.1 actions/checkout v4 → v6

- v4 → v5: SSH/Git handling 개선 등 + Node.js 24 호환 (2025-09)
- v5 → v6: Node.js 24 default + 추가 안정성 (2026-01-09)
- **본 cycle 영향**: 0 (기본 fetch 동작 유지, fetch-depth 0 옵션 호환)

### 3.2 actions/setup-python v5 → v6

- Node.js 24 마이그레이션 위주 (2026-01-22)
- python-version `"3.11"` 답습 호환 ✅
- **본 cycle 영향**: 0

### 3.3 actions/upload-artifact v4 → v7

- **v4 → v5 breaking change**: artifact name uniqueness required (동일 workflow run 안 동일 name 중복 불가) — **본 audit 결과 8 workflow 모두 unique name 사용 → 영향 0 ✅**:
  - `r2-r4-canary-evidence`, `provider-url-scanner-evidence`, `schema-validation-evidence`, `memory-skill-migration-feasibility-evidence`, `rewrite-defense-evidence`, `history-anchor-verifier-evidence`, `boundary-guard-evidence`, `secret-hygiene-egress-redaction-evidence`
- v5 → v6 / v6 → v7: 추가 안정성 + Node.js 24 호환
- **본 cycle 영향**: 0 (name uniqueness 보장 ✅, path 옵션 답습 호환)

### 3.4 종합 audit

→ **3 종 actions 모두 breaking change 영향 0건** ✅. (A) major version upgrade 안전 진행 가능.

---

## §4 R-7(b) PC1-2 차등 자격 + 합의 형태 결정

### 4.1 R-7(b) 답습 분류

| 변경 종류 | R-7(b) 답습 자격 |
|---|---|
| workflow job/step 로직 본문 변경 | catalog 영역 변경 = 풀 3+1 자격 |
| action version pin update (의존성 update) | catalog 본문 변경보다 가벼움 = 단축 자격 가능 |
| **본 cycle** | action version pin update 한정 + GitHub 공식 actions + breaking change audit 통과 + 12 workflow scope |

### 4.2 합의 형태 후보

| # | 후보 | 적정성 |
|---|---|---|
| (1) 풀 3+1 + 외부 LLM 1+ | R-7(b) 보수적 답습 + 12 workflow scope (모든 CI 영향) | △ ceremony 충분 단 의존성 update 의 본질 < |
| **(2) 단축 + 외부 LLM 1+ cross-validation** | action version pin update + GitHub 공식 검증 + breaking change audit 통과 + CI verify 자체 강 evidence | **◎ 권고** |
| (3) Reviewer-only 단축 | 1-agent 검증 + CI verify | △ external cross-vendor 보강 없음 |
| (4) 1-agent 직접 (ceremony-inflation 차단) | lint·framing 답습 유사 단 12 workflow + CI 영향 | ✗ 권고 하향 |

---

## §5 ADR-011 §2.1 (a)~(e) 매트릭스

| 조건 | 본 cycle 자격 |
|---|---|
| (a) 사용자 명시 | ✅ (A) major version upgrade + 합의 형태 사용자 결정 |
| (b)(d) 격리 PoC + 자동 회귀 | ⏳ → ✅ 실 구현 후 = 12 workflow CI re-run + 모든 PASS verify |
| (c) stateless network-free | ✅ GitHub 공식 actions (provider-agnostic CI infra) |
| (e) APPROVE | ⏳ 합의 발효 시점 |

---

## §6 R-MVP1-PASS-{1~10} trigger 발화 0건 + 사용자 결정 영역

### 6.1 trigger 발화 검증

| trigger | 발화 |
|---|---|
| R-MVP1-PASS-1 (헌법 본문 변경) | ❌ 0 |
| R-MVP1-PASS-2 (ADR-008 본문 변경) | ❌ 0 (workflow action version update = ADR 무관) |
| R-MVP1-PASS-3~10 | ❌ 0 (action 의존성 update 한정, 다른 영역 답습 유지) |

### 6.2 사용자 결정 영역

| # | 결정 항목 | 권고 |
|---|---|---|
| D-NJ-1 | 합의 형태 (§4.2 매트릭스) | **(2) 단축 + 외부 LLM 1+ cross-validation** |
| D-NJ-2 | 외부 LLM method | (P) Claude tmux + codex bypass sandbox (46 entry pattern 답습) |
| D-NJ-3 | CI verify 범위 | 12 workflow 모두 push trigger 발화 + PASS verify 의무 |

---

## §7 carry-over

- (b1-PC1-D6-ast-context) AST SAFE_CONTEXT (42 entry 답습, 별도 풀 3+1)
- (codex N-3, 46 entry) docs scan 정책 분리 (별도 cycle)
- (b1-PC1-D6-evidence) E-D6-1/2/3 evidence file (자율 영역)
- (b1-AR3 develop) develop branch 생성 시점 8 contexts 적용 (사용자 영역)

---

## §8 다음 단계

1. ✅ 본 brief commit
2. ⏳ 사용자 결정 D-NJ-1/2/3
3. ⏳ 합의 진입 (D-NJ-1 채택에 따라)
4. ⏳ 실 구현 (12 workflow 31 위치 sed-batch 또는 file-by-file)
5. ⏳ CI verify (12 workflow 모두 push trigger 발화 PASS)
6. ⏳ SESSION + INDEX + commit + push

## §9 자기진단 (5/5)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 답습 출처 5 source + GitHub deprecation 공지 + 46 entry log source 정확 | ✅ |
| 2 | scope (action version upgrade 한정) + 변경 0건 의무 5 항목 | ✅ |
| 3 | upgrade 매트릭스 12 workflow 31 위치 + breaking change audit 3/3 통과 | ✅ |
| 4 | R-7(b) 차등 자격 + 합의 형태 매트릭스 + ADR-011 매트릭스 | ✅ |
| 5 | R-MVP1-PASS 0건 + 사용자 결정 D-NJ-1~3 + carry-over + 다음 단계 | ✅ |
