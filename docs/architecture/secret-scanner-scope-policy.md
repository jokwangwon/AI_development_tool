# secret-scanner scope 정책

> **발효 시점**: 2026-05-27 (49번째 entry, codex N-3 carry-over 집행, Reviewer-only 단축 합의 APPROVE).
>
> **본 정책 = scope 변경 0건 한정** (현 hardcoded scope 명시 + 향후 확장 의무 절차 정의).

---

## §1 현 scope (영구 분리 원칙)

### 1.1 scan 영역 매트릭스

| Layer | 영역 | scope | 발효 source |
|---|---|---|---|
| `.pre-commit-config.yaml` `secret-scanner` hook | source code 정합성 | **`src + .github`** | 본 hook entry (`for d in src .github; do ...`) |
| `secret-hygiene-egress-redaction.yml` workflow | fixture 회귀 검증 | **`tests/fixtures/secret_hygiene/`** (pass/fail/redaction_pass/redaction_fail) | D-1 PASS + D-1 FAIL + D-2 PASS + D-2 FAIL steps |
| `pre-commit-bypass-detection.yml` (D-6, 40 entry) | dev 환경 hook bypass 검출 | hook entry 답습 → **`src + .github` 한정** | hook entry hardcoded scope |

### 1.2 docs/ 영역 영구 금지

- **`docs/` 영역 scan 진입 영구 금지** (현 hook entry hardcoded scope 답습)
- 사유: docs/ 본문에 합법 evidence 예시 다수 포함 (fake canary `fakecanary...`, redaction 예시, codex 응답 sample, brief 본문 패턴 예시 등)
- 잠재 매칭 audit (정책 미적용 가상 scan): **~800+ violations** (모두 false positive)

### 1.3 secret_scanner.py 자체 scope

- `SCAN_SOURCE_EXTENSIONS` = `.py / .json / .yaml / .yml / .toml / .sh / .bash / .env / .ini / .cfg / .pem / .key / .txt / .md` (14 ext)
- `.md` 포함 = 기술적으로 markdown scan 가능, 단 hook entry hardcoded scope 답습으로 docs/ 진입 0
- `SCAN_LOG_EXTENSIONS` = `.txt / .log / .json / .jsonl / .md / .pem` (scan-log mode 전용)
- `REDACTION_MARKER_RE` = `[REDACTED] / [FILTERED] / [MASKED] / <REDACTED> / <MASKED> / <<masked>> / *****` (scan-log mode 전용, scan-source 미적용)

---

## §2 scope 확장 의무 절차 (향후)

scope 확장 시 (예: full repo scan 요구, `docs/` 진입, 신 영역 추가):

### 2.1 의무 절차 6단계

1. **별도 sub-cycle brief 작성** (`docs/phase0/...scope-extension-brief.md`)
2. **풀 3+1 자격 검토** (R-7(b) PC1-2 차등 답습, 단순 version pin 가능 시 단축 + cross-validation 자격)
3. **allowlist file convention 정의** (`tests/fixtures/secret_hygiene/` pattern 답습)
4. **docs/ 영역 evidence 예시 fake canary marker convention 의무화** (§3 답습)
5. **scope 확장 적용** + 12 workflow CI 회귀 verify
6. **R-MVP1-PASS-{1~10} 발화 검증** (특히 R-MVP1-PASS-9 Provider Liquidity bypass 영향 0 확인)

### 2.2 풀 3+1 승격 trigger (scope 확장 시점)

다음 중 하나 이상 발화 시 풀 3+1 + 외부 LLM 1+ 의무:
- 새 권위 결정 (수단/threshold/Tier-2/3 catalog/ADR/헌법)
- 12+ workflow 영향
- Hermes upstream 답습 본질 손상
- secret-scanner Tier-1 catalog 본문 변경 (alternation key 목록 변경)

scope 확장 자체 만으로는 자동 발화 0건 가능 (단순 path filter 확장 한정 시).

---

## §3 docs/ 영역 evidence 예시 convention (선택, 향후 의무화 자격)

### 3.1 현 답습 (선택, 강제 0건)

- **fake canary prefix**: `fakecanary...` 답습 (R-4.1 trigger extension evidence 답습)
  - 예: `?api_key=fakecanaryR41T041NOTAREAL`
  - secret pattern + canary marker = scanner 가 인식 시 정상 evidence 분류 가능
- **redaction marker wrapping** (선택): `[REDACTED] / [MASKED] / <<masked>>` 답습 (REDACTION_MARKER_RE 답습)

### 3.2 향후 의무화 자격 (scope 확장 시점)

scope 확장 시점 = 본 convention 의무화 + scanner `scan-source` mode 에 REDACTION_MARKER_RE 적용 확장 자격 검토. 본 cycle scope 외.

---

## §4 본 정책 변경 0건 의무 (영구)

| 항목 | 변경 자격 |
|---|---|
| `.pre-commit-config.yaml` hook entry scope (`src + .github`) | scope 확장 사용자 명시 + 풀 3+1 합의 발효 시점만 |
| `secret-hygiene-egress-redaction.yml` workflow scope (`tests/fixtures/secret_hygiene/`) | 동일 |
| `secret_scanner.py` `SCAN_SOURCE_EXTENSIONS` | catalog 본문 변경 자격 = R-7(b) PC1-2 차등 답습 |
| docs/ 영역 본문 (현 evidence 예시 답습) | 답습 유지 (본 정책 발효 = 변경 0건 명시) |
| 12 workflow 본문 | 본 정책 발효 = 변경 0건 |

---

## §5 cross-reference

- 발효 source: 49 entry SESSION + Reviewer-only 단축 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-secret-scanner-docs-scope-policy.md`) + brief (`docs/phase0/mvp1-secret-scanner-docs-scope-policy-brief.md`)
- 46 entry codex N-3 carry-over 집행 (`docs/external-review/2026-05-27-mvp1-pc1-d6-fp-edge-extensions-codex-response.md` §3 N-3)
- 47 entry codex 응답 동형 (`docs/external-review/2026-05-27-mvp1-actions-nodejs-24-migration-codex-response.md` 답습)
- 33 entry MVP-1 Implementation Evidence PASS 답습 (`docs/phase0/mvp1-implementation-evidence-pass.md`)
- R-7(b) PC1-2 차등 답습 (24 entry 합의)
- R-MVP1-PASS-{1~10} 영구 금지 답습
