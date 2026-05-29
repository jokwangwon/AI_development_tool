# MVP-1 secret-scanner docs scope 정책 분리 sub-cycle brief

> **scope**: 46번째 entry (b1-PC1-D6-fp-edge-extensions) codex 응답 §3 N-3 권고 carry-over 집행 — secret-scanner 의 `docs/` 영역 scan 정책 명시 + 향후 확장 절차 정의. 47 entry codex 신규 carry-over 동형.
>
> **본 brief 자체에서 실 코드 변경 0건 의무**. **합의 형태 (사용자 결정 D-N3-2)**: (1) Reviewer-only 단축.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **46 entry codex 응답 N-3** | `docs/external-review/2026-05-27-mvp1-pc1-d6-fp-edge-extensions-codex-response.md` | "docs scan 정책을 명확히 분리하라. 현재 brief 자체에 `#access_token=...`, `;api_key=...` 예시 포함. scanner 대상이 docs까지 포함되면 의도된 evidence 문서가 violation. 지금 scope = `src/ scan 0 matches` 문제 없음. 향후 full repo scan 요구하면 allowlist/test fixture convention 필요" |
| **46 entry Reviewer 통합 합의** | `docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-fp-edge-extensions.md` | §2.3 N-3 권고 = carry-over (별도 cycle) |
| **현 `.pre-commit-config.yaml` secret-scanner hook entry** | `.pre-commit-config.yaml` line 답습 | `for d in src .github; do python3 tools/secret_scanner.py --mode scan-source "$d" || exit 1; done` (hardcoded scope) |
| **현 `tools/secret_scanner.py`** | 47 entry secret_scanner.py 답습 유지 | `SCAN_SOURCE_EXTENSIONS` 에 `.md` 포함 = docs/ markdown 모두 scan 대상 자격 (기술적) |
| **`tests/fixtures/secret_hygiene/`** | `secret-hygiene-egress-redaction.yml` 답습 | pass/fail/redaction_pass/redaction_fail fixture convention 발효 |

---

## §1 audit 결과 답습

### 1.1 현 scope (hardcoded)

| Layer | 영역 | scope |
|---|---|---|
| `.pre-commit-config.yaml` hook | `secret-scanner` | `src + .github` 한정 |
| `secret-hygiene-egress-redaction.yml` workflow | `secret-scanner` | `tests/fixtures/secret_hygiene/` 한정 |
| D-6 workflow (`pre-commit-bypass-detection.yml`) | `pre-commit run --all-files` | hook entry 답습 → secret-scanner 만 `src + .github` (file 전체 list 무관) |

→ **현 scope = docs/ 영역 진입 0 ✅** (자연 분리)

### 1.2 docs/ 영역 잠재 매칭 (audit, 본 정책 미적용 가상 scan)

- `python3 tools/secret_scanner.py --mode scan-source docs` = **~800+ violations** 검출
- 모두 합법 evidence 예시 (fake canary `fakecanary...`, redaction 예시, codex 응답 sample, brief 본문 예시 등)

→ 향후 (1) full repo scan 요구 / (2) hook entry scope 확장 / (3) 신 workflow docs scan 진입 시 = **모두 false positive risk**

---

## §2 정책 정의

### 2.1 scope 영구 분리 원칙

1. **현 scope = `src + .github + tests/fixtures/secret_hygiene/`** 한정 (hardcoded)
2. **`docs/` 영역 = scan 진입 영구 금지** (정책 영역)
3. **scope 확장 = 별도 cycle (풀 3+1 자격 검토 의무, R-7(b) PC1-2 차등 답습)**

### 2.2 docs/ 영역 evidence 예시 convention (선택, carry-over 자격)

- fake canary prefix `fakecanary...` 답습 (R-4.1 trigger extension evidence 답습)
- redaction marker wrapping `[REDACTED] / [MASKED] / <<masked>>` 선택 (REDACTION_MARKER_RE 답습)
- ⏳ 본 sub-cycle scope 외 (향후 docs scan 진입 시점 의무화)

### 2.3 scope 확장 의무 절차 (향후)

scope 확장 (예: full repo scan 요구) 시:
1. 별도 sub-cycle brief 작성
2. 풀 3+1 자격 검토 (R-7(b) 차등 답습)
3. allowlist file convention 정의 (`tests/fixtures/secret_hygiene/` pattern 답습)
4. docs/ 영역 fake canary marker convention 의무화
5. scope 확장 적용 + 회귀 verify

---

## §3 본 cycle 변경 영역

| 항목 | 변경 자격 |
|---|---|
| 정책 문서 신규 (`docs/architecture/secret-scanner-scope-policy.md`) | ✅ 신규 1 file |
| `.pre-commit-config.yaml` 주석 1~2줄 (현 scope 명시) | ✅ comment 추가 (entry 본문 변경 0) |
| `tools/secret_scanner.py` 주석 1~2줄 (정책 문서 cross-reference) | ✅ comment 추가 (code 본문 변경 0) |
| **변경 0건 의무** | docs/ 영역 본문 0 (현 evidence 예시 답습 유지), 12 workflow 본문 0, branch protection rule 0, ADR 0, 헌법 0, roadmap 본문 0, src/ 0, MVP-1 Implementation Evidence PASS 재선언 0, Operational Readiness PASS 0, Hermes PMO 격상 0, adapters/llm/facade.py 0, Tier-2/3 catalog 0 |

---

## §4 R-MVP1-PASS-{1~10} trigger 발화 0건 검증

| trigger | 발화 |
|---|---|
| R-MVP1-PASS-1 (헌법) | ❌ 0 |
| R-MVP1-PASS-2 (ADR-008) | ❌ 0 (정책 문서 + 주석 한정, ADR 본문 0) |
| R-MVP1-PASS-3 (ADR-011) | ❌ 0 |
| R-MVP1-PASS-4 (roadmap) | ❌ 0 |
| R-MVP1-PASS-5~10 | ❌ 0 |

→ **10/10 trigger 발화 0건** ✅

---

## §5 ADR-011 §2.1 (a)~(e) 매트릭스

| 조건 | 본 cycle 자격 |
|---|---|
| (a) 사용자 명시 | ✅ D-N3-1 (A) + D-N3-2 (1) |
| (b)(d) 격리 PoC + 자동 회귀 | ✅ 본 cycle = 정책 명시 + 주석 한정 = 회귀 영향 0 (scope 자체는 47 entry 답습 유지) |
| (c) stateless network-free | ✅ |
| (e) APPROVE | ⏳ 합의 발효 |

---

## §6 합의 형태 (사용자 D-N3-2 답습)

**Reviewer-only 단축** — 사용자 명시 채택.

### 6.1 풀 3+1 승격 trigger 발화 검증

| # | trigger | 발화 |
|---|---|---|
| ① | 새 권위 결정 | ❌ 0 (정책 명시 + 주석 한정, scope 변경 0) |
| ② | Tier-2/3 catalog 자동 확장 | ❌ 0 |
| ③ | PASS 자동 선언 | ❌ 0 |
| ④ | 후속 합의 본문 변경 | ❌ 0 |
| ⑤ | ADR-011 5조건 자동 충족 | ❌ 0 |

→ **5/5 발화 0건** = Reviewer-only 자격 충족

---

## §7 carry-over

- (선택) docs/ 영역 evidence 예시 fake canary marker convention 의무화 (§2.2, 향후 scope 확장 시점)
- (선택) allowlist file convention 정의 (§2.3, 향후 scope 확장 시점)
- (b1-PC1-D6-evidence-nightly) E-D6-2 nightly schedule 첫 발화 (48 entry 답습, 2026-05-28 이후)
- (b1-PC1-D6-ast-context) AST SAFE_CONTEXT (42 entry, 별도 풀 3+1)
- FORCE_JAVASCRIPT_ACTIONS_TO_NODE24 사전 evidence (47 entry, 선택)
- (b1-AR3 develop) develop branch 생성 시점 8 contexts 적용 (사용자 영역)

---

## §8 다음 단계

1. ✅ 본 brief commit
2. ⏳ Reviewer-only 단축 합의 (자체 검증)
3. ⏳ 정책 문서 작성 (`docs/architecture/secret-scanner-scope-policy.md`)
4. ⏳ `.pre-commit-config.yaml` + `tools/secret_scanner.py` 주석 추가
5. ⏳ verify (현 scope 답습 검증)
6. ⏳ SESSION + INDEX + commit + push

## §9 자기진단 (5/5)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 답습 출처 5 source + 46 codex N-3 정확 cross-reference | ✅ |
| 2 | audit 결과 (현 scope hardcoded + docs/ 잠재 ~800 violations) | ✅ |
| 3 | 정책 정의 (영구 분리 원칙 + convention 선택 + 확장 의무 절차) | ✅ |
| 4 | 변경 영역 매트릭스 + R-MVP1-PASS 0건 + ADR-011 매트릭스 + 합의 형태 자격 | ✅ |
| 5 | carry-over + 다음 단계 | ✅ |
