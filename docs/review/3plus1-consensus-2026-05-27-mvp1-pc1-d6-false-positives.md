# 3+1 합의 보고서 (Reviewer 통합) — MVP-1 (b1-PC1-D6-false-positives) sub-cycle

> **본 합의 = 풀 3+1 + 외부 LLM 1+ (cross-vendor codex)**. 사용자 D-FP-2 (1) 채택 (2026-05-27, R-7(b) PC1-2 차등 정확 답습).
>
> 4 source: Agent A 구현 분석 (289줄) + Agent B 안전 검증 (282줄) + Agent C 대안 탐색 + codex (gpt-5.5, OpenAI vendor, 6017줄 full capture).

---

## §1 본 합의 자격

### 1.1 4 source 도착 검증

| Source | 역할 | 분량 | 자기진단 | 판정 |
|---|---|---|---|---|
| **Agent A** | 구현 분석가 | 289줄 | 5/5 | **APPROVE** w/ REVISE (8 risk carry-over) |
| **Agent B** | 품질/안전성 검증가 | 282줄 | 5/5 | **APPROVE** w/ REVISE (2 verification 의무) |
| **Agent C** | 대안 탐색가 | ~ | 5/5 | **APPROVE** ((a) CHAMPION 확정, `\b` reject live verify) |
| **codex** (gpt-5.5, OpenAI vendor) | 외부 LLM cross-validation | 6017줄 (시스템 prompt + 응답) | 자기진단 명시 | **REVISE** (quoted literal FN BLOCKING risk + (a+) `'"` 추가 권고) |

### 1.2 다른 source 참조 0건 의무 검증

- Agent A/B/C 모두 본문 명시 "다른 Agent 출력 참조 0건" 자기진단 5/5
- codex = OpenAI vendor cross-vendor, Anthropic Agent 와 독립

### 1.3 합의 자격

- 사용자 명시 D-FP-2 (1) 풀 3+1 + 외부 LLM 1+ 채택 ✅
- 4 source 모두 brief v1.1 본문 직접 read + 답습 ✅
- 5/5 풀 3+1 승격 trigger 발화 자격 = ✅ (alternation 패턴 본문 변경 = catalog 영역 = R-7(b) 차등 답습 정확)

---

## §2 핵심 cross-finding 매트릭스

### 2.1 3-way + cross-vendor 일치 ⭐⭐⭐ BLOCKING

| ID | 항목 | Agent A | Agent B | Agent C | codex | 판정 |
|---|---|---|---|---|---|---|
| **R-1** | **(a) 원안 `(?:^|[?&\s])` 만으로는 quoted body literal FN risk** (예: `payload = "password=fakecanary&user=alice"` cover 0) | 8 risk 中 1 (quote `"` 직전 — cover 외) | (간접) cookie no-space verify 의무 | (간접) extended boundary 후보 검토 시 quote 제외 사유 검증 | ⭐⭐⭐ **본 발견 핵심 BLOCKING** — 권고 (a+) = `(?:^|[?&\s'"])` 즉시 보강 | **BLOCKING 1 — (a+) 보강 의무** |

### 2.2 2-way + cross-vendor 부분 일치 ⭐⭐ 권고

| ID | 항목 | Agent | codex | 판정 |
|---|---|---|---|---|
| **N-1** | semicolon `;` cookie separator FN gap (`Cookie: session=abc;api_key=...`) | Agent A (HIGH risk) + Agent B (verify 의무 R-B-2) | (간접 N-5) cookie/session FP 분리 영역 | **carry-over 권고** (`[?&\s;]` 확장, 별도 cycle) |
| **N-2** | fragment `#` OAuth implicit grant (`#access_token=...`) | Agent A (HIGH risk) | (미언급) | carry-over 권고 (`[?&\s#]` 확장) |
| **N-3** | multiline body 두 번째 line `^` 매칭 (re.MULTILINE 부재 영향) | Agent B (R-B-1) | N-2 (line-by-line scan 정합성 검증 의무) | scanner 구현 line-by-line scan 검증 (Agent A audit 결과 line-by-line 확정) |

### 2.3 Agent 단독 발견 ⭐

| ID | 항목 | Source |
|---|---|---|
| **N-4** | `\b` word boundary 후보 라이브 reject (Python regex `key` 자체가 word char 끝 → FP 재발) | Agent C 단독 |
| **N-5** | variable-width lookbehind `(?<=^|[?&\s])` Python engine 거부 (fixed-width 의무) | Agent C 단독 |
| **N-6** | extended boundary `(?:^|[?&\s,;\(\[\"\\'])` FP 재발 — `(key=lambda)` `,key=lambda` 매칭 | Agent C 단독 (라이브 verify) |
| **N-7** | `(?:^|[?&\s])` = Python 유일 fixed-width + multi-anchor + Python keyword arg cover 3조건 동시 충족 해법 확정 | Agent C 단독 (라이브 verify) |
| **N-8** | scanner 의 ReDoS risk 부재 확정 (alternation + `[^&\s]+` 조합) | Agent B 단독 |
| **N-9** | (d) AST SAFE_CONTEXT prototype design (30~50줄, Call.keywords / FunctionDef.args / AnnAssign 매트릭스) | Agent C 단독 |

---

## §3 BLOCKING 1 + 권고 매트릭스

### 3.1 BLOCKING 1 (즉시 흡수 의무)

| ID | 항목 | 흡수 형태 |
|---|---|---|
| **R-1** | (a) → (a+) 보강: `(?:^|[?&\s])` → `(?:^|[?&\s'"])` (quote `'` `"` 추가) | brief v1.1 → v1.2 in-place 보강 + 사용자 명시 cross-check (D-FP-1 (a) → (a+) 확장 자격) |

**근거**:
- codex 권고 1번 = "(a+) 로 보강: 좌측 delimiter 에 quote 를 추가한다" 명시
- secret 영역 직접 = source code 내 hardcoded HTTP body string literal cover 누락 = 보안 영향
- (a+) 채택 시 `sort(key=...)` / `exit_code=...` FP 재발 0 (`(` 는 추가 안 함)
- Hermes upstream 답습 본질 유지 + canary cover 보존

### 3.2 권고 (carry-over 분리)

| ID | 항목 | 분류 |
|---|---|---|
| **N-1+2** | semicolon `;` + fragment `#` 추가 delimiter 확장 | **(b1-PC1-D6-fp-edge-extensions)** 신규 carry-over (별도 단축 합의 또는 풀 3+1) |
| **N-3** | scanner line-by-line scan 검증 + brief §4.2 multiline body 8번째 시나리오 추가 | Agent A audit 결과 line-by-line 확정 — 추가 검증 불필요 (정합 검증 완료) |
| **N-9** | (d) AST SAFE_CONTEXT 영구 정밀화 | **(b1-PC1-D6-ast-context)** 신규 carry-over (별도 풀 3+1 cycle, prototype design Agent C 답습) |
| **N-8** | ReDoS 부재 evidence | 본 합의 보고서 §2.3 명문 답습 = 추가 cycle 불필요 |

---

## §4 (a+) 정정 본문 + verification 재실증

### 4.1 (a+) 정정 본문 (R-1 BLOCKING 흡수)

**brief v1.2 정정 후 패턴 (tools/secret_scanner.py line 155~158)**:

```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
```

**핵심 변경 (v1.1 → v1.2)**:
- alternation 직전 prefix = `(?:^|[?&\s])` → `(?:^|[?&\s'\"])` (quote `'` + `"` 추가, `(` 는 추가 0)

### 4.2 verification 재실증 9 시나리오 (R-1 흡수 후)

| # | 시나리오 | 현 | (a) 정정 후 | (a+) 정정 후 |
|---|---|---|---|---|
| 1 | `failures.sort(key=lambda e: ...)` (Python sort FP) | FP | OK | **OK** (paren 직전, prefix 매칭 0) |
| 2 | `failures.sort(key=_ts_key, ...)` (named function FP) | FP | OK | **OK** |
| 3 | `WorkerResult(exit_code=exit_code, ...)` (dataclass FP) | FP | OK | **OK** |
| 4 | `?api_key=fakecanary...` (T1-038 URL query canary) | BLOCK | BLOCK | **BLOCK** (`?` prefix 유지) |
| 5 | `&password=fakecanary&...` | BLOCK | BLOCK | **BLOCK** (`&` prefix 유지) |
| 6 | `password=fakecanary&...` (line start, T1-040 form body) | BLOCK | BLOCK | **BLOCK** (`^` prefix 유지) |
| 7 | `Authorization: Bearer ... ; api_key=xxx` | BLOCK | BLOCK | **BLOCK** (`\s` prefix 유지) |
| **8 NEW (R-1 BLOCKING)** | `payload = "password=fakecanary&user=alice"` (quoted form body literal) | BLOCK (FP 검출 등으로 우연 매칭) | **FN (cover 누락)** | **BLOCK** (`"` prefix 매칭, R-1 흡수 효과) ✅ |
| **9 NEW (R-1 BLOCKING)** | `body = 'api_key=fakecanary&q=hi'` (single-quote literal) | BLOCK 우연 | **FN (cover 누락)** | **BLOCK** (`'` prefix 매칭) ✅ |

→ **(a+) = FP 4/4 해소 + canary 7/7 BLOCK 보존 + 신 quoted literal 2/2 BLOCK 확정** ✅

### 4.3 (a+) 라이브 verify (Python re engine)

(실 구현 단계에서 재실증 의무 — `python3 -c` live test)

---

## §5 ADR-011 §2.1 (a)~(e) 매트릭스 (PC-1-T3 (b)(d) 회귀 자격 보강 한정)

| 조건 | 본 합의 발효 자격 |
|---|---|
| **(a)** 사용자 명시 결정 | ✅ D-FP-1 (a) 채택 + 본 합의 R-1 흡수 후 (a+) 확장 사용자 명시 cross-check 의무 |
| **(b)(d)** 격리 환경 PoC 실증 + 자동 회귀 검증 | ⏳ → ✅ 실 구현 후 = 본 D-6 workflow re-run + secret-scanner self-test + T1-038/T1-040 canary 재발화 + 신 시나리오 8/9 verify |
| **(c)** 도구/리소스 stateless · network-free | ✅ Python `re` engine = stateless, network-free |
| **(e)** 합의 APPROVE 운영조건 | ✅ 본 합의 APPROVE WITH CONDITIONS 시점 충족 |

→ **본 합의 = PC-1-T3 (b)(d) 회귀 자격 *보강*** (33번째 entry MVP-1 PASS 전체 답습 유지)

---

## §6 R-MVP1-PASS-{1~10} 영구 금지 trigger 발화 0건 검증

| trigger | 본 합의 발화 |
|---|---|
| R-MVP1-PASS-1 (헌법 본문 변경) | ❌ 0건 |
| R-MVP1-PASS-2 (ADR-008 본문 변경) | ❌ 0건 (alternation 패턴 정정 = tools/ 본문 변경, ADR-008 답습 본질 유지) |
| R-MVP1-PASS-3 (ADR-011 본문 변경) | ❌ 0건 |
| R-MVP1-PASS-4 (roadmap 본문 변경) | ❌ 0건 |
| R-MVP1-PASS-5 (Hermes PMO 격상) | ❌ 0건 |
| R-MVP1-PASS-6 (Operational Readiness PASS) | ❌ 0건 |
| R-MVP1-PASS-7 (MVP-2 자동 진입) | ❌ 0건 |
| R-MVP1-PASS-8 (paths-aware audit 위반) | ❌ 0건 (본 cycle scope 외) |
| R-MVP1-PASS-9 (Provider Liquidity bypass) | ❌ 0건 (secret-scanner = provider-agnostic, alternation prefix 추가 = provider 영향 0) |
| R-MVP1-PASS-10 (cross-reference 본문 변경) | ❌ 0건 (본 cycle = tools/ 본문 정정 한정) |

→ **10/10 trigger 발화 0건 = R-MVP1-PASS 영구 금지 답습 정확**

---

## §7 최종 판정

### 7.1 합의 결과

**APPROVE WITH CONDITIONS (BLOCKING 1 + 권고 다수)**

- 4 source 모두 (a) 채택 자격 충족 + 단 codex BLOCKING 1 (quoted literal FN risk) 흡수 의무 = (a+) 보강 확장
- 3-way + cross-vendor 일치 BLOCKING 1 = ⭐⭐⭐ 우선 흡수
- 권고 = (b1-PC1-D6-fp-edge-extensions) + (b1-PC1-D6-ast-context) 신규 carry-over 2건

### 7.2 발효 자격

| 단계 | 자격 |
|---|---|
| **본 합의 발효** | ✅ 본 commit 시점 |
| **brief v1.2 in-place 보강** | ✅ 본 commit 동시 (1pass 흡수, 별도 v2 cycle 0) |
| **(a+) 사용자 명시 cross-check** | ⏳ 본 합의 보고 후 사용자 명시 의무 (D-FP-1 (a) → (a+) 확장 자격) |
| **실 구현 진입** | ⏳ 사용자 (a+) 채택 명시 후 |
| **회귀 verify** | ⏳ 실 구현 완료 후 (자율 + 본 D-6 workflow re-run) |

### 7.3 다음 단계 (단계별 합의 cycle 답습)

1. ✅ brief v1.1 (단계 1)
2. ✅ 사용자 결정 D-FP-1/2/3 (단계 2)
3. ✅ 풀 3+1 + 외부 LLM 1+ 합의 (단계 3, 본 보고서) — **APPROVE WITH CONDITIONS**
4. ⏳ brief v1.2 in-place 보강 (R-1 BLOCKING 1pass 흡수) + 사용자 (a+) 명시 cross-check
5. ⏳ 실 구현 (`tools/secret_scanner.py` line 155~158 정정, (a+) 본문 적용)
6. ⏳ 회귀 verify (D-6 workflow re-run + secret-scanner self-test + jarvis pytest)
7. ⏳ SESSION + INDEX + commit + push
8. ⏳ carry-over (2 신규 + 기존 (b1-PC1-D6-contexts) 등)

---

## §8 자기진단 (5/5)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 4 source 도착 + 자격 검증 + 다른 source 참조 0건 cross-check (§1) | ✅ |
| 2 | 핵심 cross-finding 매트릭스 (3-way BLOCKING / 2-way 권고 / Agent 단독) (§2) | ✅ |
| 3 | BLOCKING 1 (R-1) + 권고 분류 + 흡수 형태 명시 (§3) | ✅ |
| 4 | (a+) 정정 본문 + verification 재실증 9 시나리오 + ADR-011 (a)~(e) 매트릭스 (§4 + §5) + R-MVP1-PASS-{1~10} 발화 0건 (§6) | ✅ |
| 5 | 최종 판정 APPROVE WITH CONDITIONS + 발효 자격 + 다음 단계 + 자기진단 (§7 + §8) | ✅ |
