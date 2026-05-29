# MVP-1 (b1-PC1-D6-fp-edge-extensions) semicolon + fragment delimiter 확장 sub-cycle brief

> **scope**: 42번째 entry (b1-PC1-D6-false-positives) Reviewer 통합 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-false-positives.md`) §3.2 권고 N-1+2 신규 carry-over (Agent A 8 risk + codex N-1+2 답습) 집행. T1-041/T1-042 alternation prefix 추가 확장 (semicolon `;` cookie separator + fragment `#` OAuth implicit grant).
>
> **본 brief 자체에서 실 코드 변경 0건 의무** — brief 합의 발효 *후* 별도 실 구현 단계에서 적용.
>
> **합의 형태 결정 (사용자 명시 2026-05-27)**: **(2) 단축 + 외부 LLM 1+ cross-validation** (Reviewer-only + codex cross-vendor).

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **42번째 entry brief v1.2** | `docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` (commit `a6dc51d`) | §4.1 (a+) 정정 본문 `(?:^|[?&\s'\"])` + §8 carry-over #1 (semicolon + fragment 확장) |
| **42번째 entry Reviewer 통합 합의** | `docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-false-positives.md` | §3.2 N-1+2 권고: Agent A HIGH risk (cookie `;` + OAuth `#`) + codex N-1 (`\s` newline 포함 명문) |
| **secret_scanner.py 현 상태** | `tools/secret_scanner.py` line 155~158 (42 entry 정정 답습) | T1-041/T1-042 prefix `(?:^|[?&\s'\"])` 발효 |
| **R-7(b) PC1-2 차등 답습** | 24번째 entry 합의 line 94 | alternation 패턴 본문 변경 = catalog 영역 = 풀 3+1 자격 (단축 + cross-validation 보강) |
| **42번째 entry live verify 답습** | 본 audit 직전 | (a++) `(?:^|[?&\s'";#])` cover 6/6 + src/ scan 0 영향 |

---

## §1 scope

### 1.1 본 sub-cycle 본질

| 항목 | 내용 |
|---|---|
| scope | T1-041/T1-042 alternation prefix 확장 — `(?:^|[?&\s'\"])` → `(?:^|[?&\s'\";#])` (semicolon + fragment 추가) |
| 합의 형태 | **단축 합의 + 외부 LLM 1+ cross-validation** (사용자 명시) |
| 변경 영역 | `tools/secret_scanner.py` line 155~158 (2 line prefix character class 확장) |
| 변경 0건 의무 | `.pre-commit-config.yaml` 본문 0, `.githooks/` 본문 0, 12 workflow 본문 0, branch protection rule 0, ADR 0, 헌법 0, roadmap 본문 0, src/ 0 (42 entry 답습 유지), MVP-1 Implementation Evidence PASS 재선언 0, Operational Readiness PASS 0, Hermes PMO 격상 0, adapters/llm/facade.py 0, Tier-2/3 catalog 확장 0, threshold 고정 0 |

### 1.2 본 sub-cycle 하지 *않는* 것

| # | 항목 | 자격 |
|---|---|---|
| 1 | (d) AST SAFE_CONTEXT 추가 | 0건 (별도 cycle (b1-PC1-D6-ast-context) carry-over) |
| 2 | (b) exclude src/jarvis/ | 0건 (FN risk, 42 entry 답습 권고 하향) |
| 3 | src/jarvis/layer1.py 재정정 | 0건 (42 entry tuple sort 회피 답습 유지) |
| 4 | ADR-008 본문 변경 | 0건 (R-MVP1-PASS-2 영구 금지) |

---

## §2 (a++) 정정 본문

### 2.1 현 패턴 (42 entry 답습)

```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:^|[?&\s'\"])(?:access_token|...|key|code|...)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:^|[?&\s'\"])(?:access_token|...|key|...)=[^&\s]+"),
```

### 2.2 (a++) 정정 후 패턴

```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
```

**핵심 변경**: prefix character class 확장 `[?&\s'\"]` → `[?&\s'\";#]` (semicolon + fragment 추가)

### 2.3 답습 본질 유지

- key 목록 (T1-041 16 + T1-042 14) 보존 ✅ (Hermes upstream 답습)
- alternation 형식 보존 ✅ (regex structure 동형)
- character class 확장 한정 (2 char 추가) = 의미적 답습 최소 변경

---

## §3 verification 9 시나리오

### 3.1 신 cover 의무 (semicolon + fragment) — v1.1 보강 (합의 N-1 권고 흡수)

> **v1.1 정정 사유**: 합의 codex N-1 권고 흡수 — `session=abc;api_key=...` 의 `session=` 자체가 alternation 포함 → (a+) 가 이미 BLOCK 가능 → 신 cover 증명 약함. neutral cookie key (`foo=`) 사용 → semicolon prefix 추가 효과 정확 증명.

| # | 시나리오 | 현 (a+) | (a++) 정정 후 |
|---|---|---|---|
| 1 NEW (v1.1) | `Cookie: foo=abc;api_key=...` (neutral cookie key + HTTP Cookie separator) | FN (cover 0, `foo` alternation 외) | **BLOCK** (`;` prefix 매칭) ✅ |
| 2 NEW | `Set-Cookie: name=val; password=...` (response header whitespace) | BLOCK (`\s` 매칭) | **BLOCK** (`\s` 매칭 유지) ✅ |
| 3 NEW | `https://callback#access_token=fake` (OAuth implicit grant) | FN (cover 0) | **BLOCK** (`#` prefix 매칭) ✅ |

### 3.2 기존 cover 보존 (42 entry 답습)

| # | 시나리오 | 현 (a+) | (a++) 정정 후 |
|---|---|---|---|
| 4 | `?api_key=fakecanary` (T1-038 URL query canary) | BLOCK | **BLOCK** ✅ |
| 5 | `&password=fakecanary` (URL query 추가) | BLOCK | **BLOCK** ✅ |
| 6 | `password=fakecanary` (line start, T1-040 form body) | BLOCK | **BLOCK** ✅ |
| 7 | `payload = "password=fakecanary..."` (R-1 quoted body literal) | BLOCK | **BLOCK** ✅ |
| 8 | `body = 'api_key=fakecanary...'` (single-quote literal) | BLOCK | **BLOCK** ✅ |

### 3.3 FP regression 검증 (42 entry 답습 보존)

| # | 시나리오 | 현 (a+) | (a++) 정정 후 |
|---|---|---|---|
| 9 | `failures.sort(key=lambda e: e.get(...))` (Python sort) | OK (42 entry layer1.py 회피 + (a+) FP 해소) | **OK** (42 entry 답습 유지) ✅ |

### 3.4 src/ scan 영향

- live audit (본 brief 작성 전 verify): **0 matches** = (a++) prefix 추가 시 현 src/ 영역에 새 FP 발생 0건 ✅

---

## §4 FP 잠재 영역 + carry-over

### 4.1 Python 주석 + alternation 단어

`# api_key=value` 같은 Python 주석 패턴은 (a+) 이미 잠재 FP (`\s` prefix 매칭). 본 (a++) 추가로 새 FP 영향 0 (이미 잠재 발생 영역, src/ scan 0건 = 실 영향 0).

### 4.2 subprocess 명령 안 secret string

`subprocess.run("cmd;api_key=test", ...)` 같은 패턴 = (a++) 후 BLOCK. 의도된 동작 (cmd 안 secret = 실 risk). FP 아님.

### 4.3 carry-over

- **(b1-PC1-D6-ast-context)** AST SAFE_CONTEXT 영구 정밀화 (42 entry carry-over 답습 유지)
- 본 cycle scope 외 추가 delimiter (paren `(` / bracket `[` / comma `,` 등) — `(` 추가 시 Python keyword arg FP 재발 (42 entry codex N-7 답습) = REJECT

---

## §5 R-7(b) PC1-2 차등 자격 + 합의 형태 명시

| 변경 종류 | R-7(b) 답습 |
|---|---|
| alternation 패턴 본문 변경 (key 목록 변경 X, prefix character class 확장) | catalog 영역 변경 = 풀 3+1 자격 |
| 본 cycle | 단축 + cross-validation = 사용자 명시 (verification 강 evidence + 42 entry 본질 동형) |

본 단축 합의 자격 근거:
1. 42 entry pattern 본질 동형 (alternation prefix 확장, key 목록 보존)
2. verification 9 시나리오 PASS + src/ scan 0 영향
3. Hermes upstream 답습 본질 유지
4. R-7(b) PC1-2 차등 정확 답습 + 외부 LLM cross-vendor 보강

---

## §6 ADR-011 §2.1 (a)~(e) 매트릭스 (PC-1-T3 회귀 자격 보강)

| 조건 | 본 합의 자격 |
|---|---|
| (a) 사용자 명시 결정 | ✅ D-FP-1 (1) 1번 진행 + 합의 형태 (2) 단축 + LLM |
| (b)(d) 격리 PoC + 자동 회귀 | ⏳ 실 구현 후 = scan-source src+`.github` violations=0 + canary fixture BLOCK + jarvis pytest 144/144 |
| (c) stateless · network-free | ✅ Python re engine |
| (e) 합의 APPROVE | ⏳ 본 합의 발효 시점 |

---

## §7 R-MVP1-PASS-{1~10} trigger 발화 0건 검증

| trigger | 발화 |
|---|---|
| R-MVP1-PASS-1 (헌법 본문 변경) | ❌ 0 |
| R-MVP1-PASS-2 (ADR-008 본문 변경) | ❌ 0 (alternation prefix character class 확장 = tools/ 본문, ADR-008 답습 본질 유지) |
| R-MVP1-PASS-3~10 | ❌ 0 (전부 답습) |

---

## §8 다음 단계

1. ✅ 본 brief commit
2. ⏳ codex cross-vendor 호출 + 응답 capture
3. ⏳ Reviewer-only 단축 합의 보고서 (cross-validation 통합 + R-MVP1-PASS trigger 검증)
4. ⏳ 실 구현 (`tools/secret_scanner.py` line 155~158 prefix `[?&\s'\";#]` 확장)
5. ⏳ verify (scan + canary + pytest)
6. ⏳ SESSION + INDEX + commit + push

## §9 자기진단 (5/5)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 답습 출처 5 source + 42 entry carry-over 답습 정확 | ✅ |
| 2 | scope (a++) 명확 + 변경 0건 의무 4 항목 | ✅ |
| 3 | (a++) 정정 본문 + verification 9 시나리오 | ✅ |
| 4 | FP 잠재 영역 + carry-over + R-7(b) 자격 + ADR-011 매트릭스 | ✅ |
| 5 | R-MVP1-PASS trigger 0건 + 다음 단계 | ✅ |
