# MVP-1 (b1-PC1-D6-false-positives) secret-scanner T1-041/T1-042 alternation false positives 정정 sub-cycle brief

> **scope**: 41번째 entry (b1-PC1-D6-fix) 신규 carry-over (b1-PC1-D6-false-positives) 집행. 40번째 entry `pre-commit-bypass-detection.yml` 첫 발화 결과 검출된 `src/jarvis/{layer1,worker}.py` 10건 secret-scanner false positives 정정 sub-cycle.
>
> **본 brief 자체에서 실 코드 변경 0건 의무** — brief 합의 발효 *후* 별도 실 구현 단계에서 채택 후보 적용.

---

## §0 답습 출처 (인용 source)

| Source | 위치 | 답습 내용 |
|---|---|---|
| **40번째 entry brief + 합의 + workflow** | `docs/phase0/mvp1-pc1-d6-bypass-detection-ci-brief.md` + `docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-bypass-detection-ci.md` + `.github/workflows/pre-commit-bypass-detection.yml` | D-6 (ii) `pre-commit run --all-files` CI 통합 = 본 false positives 검출 메커니즘 발효 source |
| **41번째 entry** | `docs/sessions/SESSION_2026-05-27.md` line 1301~ (41번째 entry) | (b1-PC1-D6-false-positives) 신규 carry-over 명시 + 풀 3+1 권고 + 우선순위 1 |
| **secret-scanner Tier-1 catalog** | `tools/secret_scanner.py` line 153~159 (ALTERNATION_PATTERNS 2건) | T1-041 = `(?i)(?:access_token\|refresh_token\|id_token\|token\|api_key\|apikey\|client_secret\|password\|auth\|jwt\|session\|secret\|key\|code\|signature\|x-amz-signature)=[^&\s]+` / T1-042 = `(?i)(?:access_token\|refresh_token\|id_token\|token\|api_key\|apikey\|client_secret\|password\|auth\|jwt\|secret\|private_key\|authorization\|key)=[^&\s]+` |
| **R-4.1 trigger extension evidence** | `docs/phase0/r4-1-trigger-extension-evidence.md` §5.3 line 218~280 | T1-041/T1-042 alternation 채택 사유 = Hermes `_SENSITIVE_QUERY_PARAMS` / `_SENSITIVE_BODY_KEYS` 답습 + T1-038/T1-040 canary 차단 보장 |
| **24번째 entry R-7(b) BLOCKING** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` line 94 | PC1-2 차등: 신규 hook (Tier-2/3 catalog / provider policy / security gate) = 풀 3+1, 단순 version pin = 단축 합의 — 본 cycle 합의 형태 자격 검토 의무 |
| **33번째 entry MVP-1 PASS** | `docs/phase0/mvp1-implementation-evidence-pass.md` (commit `d398568`) | R-MVP1-PASS-2 영구 금지 (ADR-008 본문 변경 0건) + R-MVP1-PASS-{1~10} 답습 의무 |
| **ADR-011 §2.1** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 |

---

## §1 scope (false-positives 정정 sub-cycle)

### 1.1 본 sub-cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | secret-scanner T1-041/T1-042 alternation 패턴의 Python keyword arg 오인 검출 정정 (CI 영구 RED 해소) |
| **검출 위치** | `src/jarvis/{layer1.py:187/237, worker.py:61/70/178/193/202/324}` 10건 (§3 raw 답습) |
| **합의 형태 권고** | **§7 사용자 결정 영역** — 채택 후보에 따라 (c) 1-agent 직접 vs (b)/(d)/(e) 단축 합의 vs (a) 풀 3+1 자격 변동 |
| **변경 0건 의무** | 채택 후보 외 모든 영역 본문 변경 0 — `.githooks/` / 기존 11 workflow / `.pre-commit-config.yaml` 다른 hook / branch protection rule / src/ 다른 module / tools/ 다른 도구 / ADR / 헌법 / roadmap / MVP-1 Implementation Evidence PASS 재선언 / 풀 3+1 합의 본문 (33번째) / Hermes PMO 격상 / facade.py 본문 |
| **변경 허용 영역** | 채택 후보 별 §4 매트릭스 답습 (사용자 결정 영역) |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무, 채택 후보 무관)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | ADR-008 / ADR-011 / 헌법 / roadmap 본문 변경 | 0건 (R-MVP1-PASS-2 영구 금지 답습) |
| 2 | 33번째 entry MVP-1 Implementation Evidence PASS 재선언 | 0건 (33번째 답습 유지, 본 cycle = false positive 정정 한정) |
| 3 | branch protection rule contexts 갱신 | 0건 ((b1-PC1-D6-contexts) carry-over, 본 sub-cycle 외) |
| 4 | 기존 11 workflow 본문 변경 | 0건 (40번째 entry 답습) |
| 5 | tools/ 다른 도구 본문 변경 | 0건 |
| 6 | src/ 다른 module 본문 변경 | 0건 |
| 7 | Tier-2/3 catalog 확장 | 0건 |
| 8 | Hermes PMO 격상 | 0건 |
| 9 | adapters/llm/facade.py 본문 변경 | 0건 ((d) carry-over 영역) |
| 10 | Operational Readiness PASS 발효 | 0건 |

---

## §2 본질 분석 — T1-041/T1-042 alternation vs Python source code

### 2.1 T1-041/T1-042 alternation 패턴 정의 (Hermes 답습)

```python
# tools/secret_scanner.py line 154~159
T1-041 (URL query): (?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|
                          client_secret|password|auth|jwt|session|secret|key|code|
                          signature|x-amz-signature)=[^&\s]+
T1-042 (Body/form): (?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|
                          client_secret|password|auth|jwt|secret|private_key|
                          authorization|key)=[^&\s]+
```

### 2.2 패턴 채택 사유 (R-4.1 evidence 답습)

- Hermes upstream `_SENSITIVE_QUERY_PARAMS` (16 keys) + `_SENSITIVE_BODY_KEYS` (14 keys) 답습
- T1-038 (URL query secret) + T1-040 (form-urlencoded body secret) canary 차단 자격 보장 (alternation 매칭)
- HTTP URL query string + form body 영역의 sensitive key 검출 목적 (네트워크 통신 leak 방지)

### 2.3 false positive 발생 원인

- alternation에 **너무 흔한 Python identifier** 포함: `key` (T1-041 + T1-042) + `code` (T1-041만)
- `SCAN_SOURCE_EXTENSIONS` (line 183~186)에 `.py` 포함 → Python source code도 scan 대상
- HTTP URL query 패턴 `key=value` 와 Python keyword arg `key=lambda` 구문 동일 → 정규식 충돌
- **본질**: HTTP 통신 영역 패턴이 source code 영역에 over-applied

### 2.4 결과 차이 검출 메커니즘 정확 작동 검증 ✅

- dev 환경 hook = `pre-commit` 기본값 = `pass_filenames: false` + `always_run: true` (line 168~170) → 실제로는 **모든 file 항상 scan**
- 단 본 false positives 검출 시점 = **이번 D-6 workflow 첫 발화**가 처음 = `pre-commit install` 미실행 dev 환경 또는 commit 시점 외 skip 가능성 시사
- 본 D-6 workflow의 R-6 BLOCKING 의도 *결과 차이 검출* 메커니즘 = 작동 확정 ✅

---

## §3 검출 10건 raw 위치 분류

### 3.1 `src/jarvis/layer1.py` (4 detections, 2 lines × 2 patterns)

| 위치 | match | context | 정체 |
|---|---|---|---|
| line 187 | `'key=lambda'` | `failures.sort(key=lambda e: e.get("ts", ""), reverse=True)` | Python `sort()` key arg + lambda (Python sort idiom) |
| line 237 | `'key=lambda'` | (line 187 동형) | Python sort idiom |

### 3.2 `src/jarvis/worker.py` (6 detections, 6 lines × T1-041)

| 위치 | match | context | 정체 |
|---|---|---|---|
| line 61 | `'code=exit_code,'` | `return cls(exit_code=exit_code, ...)` constructor keyword arg | Python dataclass keyword arg |
| line 70 | `'code=exit_code,'` | (line 61 동형) | Python keyword arg |
| line 178 | `'code=new_rc'` | (worker process exit code 참조) | Python keyword arg |
| line 193 | `'code=124,'` | timeout exit code 상수 | Python keyword arg (literal) |
| line 202 | `'code=sentinel_code,'` | sentinel exit code 참조 | Python keyword arg |
| line 324 | `'code=1,'` | error exit code 상수 | Python keyword arg (literal) |

### 3.3 모두 **명백한 Python keyword arg / lambda** (NOT secrets)

- `key=lambda` = Python `sorted()` / `list.sort()` 표준 idiom
- `exit_code` / `rc` / `code` = OS process exit code 표준 identifier
- 모두 dataclass / function call / sort 의 keyword arg context

---

## §4 조치 후보 5 매트릭스 (a)~(e)

### ⚠️ §4 v1.1 보강 (brief v1 결함 정정)

**brief v1 §4.1 (c) "우선 권고" 결함 발견 (2026-05-27, brief v1 작성 직후 사용자 결정 D-FP-1 (c) 채택 → 실증 verify 시 결함 노출)**:

- T1-041 정규식 = `(?:...|key|code|...)=[^&\s]+` — alternation에 `key` `code` 식별자 포함 + word boundary 부재
- (c) 코드 회피 검증 결과 (Python regex live test):
  - `key=lambda` → FP (`key=lambda` 매칭) — 현 상태
  - `key=_ts_key,` → **FP** (`key=_ts_key,` 매칭, named function 추출도 회피 불가능)
  - `key=itemgetter("ts"),` → **FP** (모든 sort key arg 회피 불가능)
  - `sorted(..., key=...)` → **FP** (sort 함수 변경도 회피 불가능)
- **결론**: layer1.py 4 detections = **(c) 회피 불가능** (Python sort 의 `key=` keyword arg 자체가 매칭)
- worker.py 6 detections 만 (c) 가능:
  - `exit_status=exit_code` → **OK** (alternation 매칭 0)
  - `WorkerResult(exit_code, stdout, ...)` positional → **OK**
  - 단 dataclass field `exit_code` rename = breaking change for `src/jarvis/memory.py:50` + `tests/jarvis/*` 다수 호출자

→ **(c) 단독 = 부분 해결만 가능, layer1.py 영역 미해결**

### 4.0 신 1차 권고: (a) word boundary 추가 (사용자 D-FP-1 재선택 2026-05-27 = (a))

| # | 후보 | scope | 권위 영향 | 보안 영향 | 검증 의무 | 권고 |
|---|---|---|---|---|---|---|
| **⭐ (a) word boundary 추가** | T1-041/T1-042 alternation 직전 `[?&]\|^\|\s` prefix 추가 → URL query/body 컨텍스트 한정 | `tools/secret_scanner.py` line 155~158 본문 변경 (3~6 줄) | G3 R-4.1 Tier-1 catalog 본문 = 권위 라인 (단, 결함 정정 = R-MVP1-PASS-2 자격 영향 없음, ADR-008 본문 변경 0) + Hermes upstream 답습 본질 유지 (key 목록 보존, prefix 만 추가) | T1-038/T1-040 canary 차단 cover 유지 (T1-038 = `?api_key=...` → `?` prefix 매칭 / T1-040 = line start → `^\|\s` 매칭) | **풀 3+1 + 외부 LLM 1+** (R-7(b) PC1-2 차등 답습 — alternation 패턴 본문 변경 = catalog 영역) + T1-038/T1-040 canary 재발화 evidence 의무 | **⭐ 신 1차 권고 (사용자 D-FP-1 채택)** |
| (b) | `.pre-commit-config.yaml` secret-scanner hook entry에 src 영역 정밀화 — 예: hook level `files:`/`exclude:` 추가 | `.pre-commit-config.yaml` line 변경 (1~3 줄) | R-7(b) PC1-2 차등 영역 (hook entry 변경 = catalog 본문 변경 아니지만 hook filter 변경) | src/jarvis/ 실 secret 누락 가능성 (FN risk) | 단축 합의 자격 자체 검토 의무 | ✗ (FN risk, 권고 하향) |
| (c) | `src/jarvis/{layer1,worker}.py` 코드 회피 — `sort(key=...)` → `cmp=lambda` 우회 또는 `code=exit_code` → `exit_status=exit_code` rename | src/ 본문 변경 11 위치 rename (jarvis 기능 영향 0) | 권위 라인 영향 0 + pattern catalog 보존 | 변경 0 (pattern cover 유지) | 1-agent 직접 자격 (lint/framing 답습) + 사용자 명시 / 단축 합의 (테스트 영향 검증 의무) | ❌ **결함 — layer1.py 회피 불가능, 부분 해결만** (brief v1.1 정정) |
| (d) | secret_scanner.py 에 SAFE_CONTEXT (Python AST context) 추가 — function call keyword arg 자동 skip | `tools/secret_scanner.py` 본문 변경 (large diff, ast import + check 추가) | G3 PoC 본문 변경 (24~50 줄 추가) + Hermes 답습 유지 | Hermes pattern cover 보존 + Python source code 정밀 분리 | 풀 3+1 (도구 본문 변경, 복잡도 증가) | △ (큰 cycle, 향후 영구 정밀화 carry-over 자격) |
| (e) | scan-source mode에서 `.py` extension에 alternation 패턴 skip — `SCAN_SOURCE_EXTENSIONS` 분리 또는 alternation context별 file ext filter | `tools/secret_scanner.py` 본문 변경 (5~15 줄) | G3 PoC 본문 변경 | `.py` 의 실제 URL query string 패턴도 skip = FN risk (단, `.py` 내 URL hardcoding 자체가 R-MVP1-PASS-9 영향 가능성 = anti-pattern) | 풀 3+1 (Hermes 답습 scope 변경) | △ (scope 좁힘, 검토 의무) |

### 4.1 (a+) 채택 시 패턴 정정 본문 (brief v1.2 = 합의 R-1 BLOCKING 흡수)

**v1.1 → v1.2 보강 사유**: Reviewer 통합 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-false-positives.md`) R-1 BLOCKING 흡수 — codex (gpt-5.5, OpenAI vendor) 발견 + 3-way + cross-vendor 일치 = `(?:^|[?&\s])` 만으로는 **quoted form-urlencoded body literal FN risk** (예: `payload = "password=fakecanary&user=alice"` cover 0). 사용자 명시 cross-check 2026-05-27 = (1) (a+) 채택.

**현 패턴 (tools/secret_scanner.py line 155~158)**:
```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
```

**(a+) 정정 후 패턴 (word boundary + quote delimiter 추가)**:
```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
```

**핵심 변경 (v1.1 → v1.2)**:
- alternation 직전 prefix = `(?:^|[?&\s])` → `(?:^|[?&\s'\"])` (quote `'` + `"` 추가)
- `(` paren delimiter 추가 0 = Python keyword arg `sort(key=...)` / `WorkerResult(exit_code=...)` FP 재발 회피 (codex N-7 답습)
- semicolon `;` + fragment `#` 등 추가 delimiter = **(b1-PC1-D6-fp-edge-extensions) 신규 carry-over** (Agent A + codex N-1+2 답습)

### 4.2 (a+) 정정 효과 verification (R-1 흡수 후 9 시나리오)

| # | 시나리오 | 현 매칭 | (a) 정정 후 | **(a+) 정정 후** |
|---|---|---|---|---|
| 1 | `failures.sort(key=lambda e: e.get(...))` (Python sort FP) | FP | OK | **OK** (paren 직전, prefix 매칭 0) ✅ |
| 2 | `failures.sort(key=_ts_key, ...)` (named function FP) | FP | OK | **OK** ✅ |
| 3 | `WorkerResult(exit_code=exit_code, ...)` (dataclass FP) | FP | OK | **OK** ✅ |
| 4 | `?api_key=fakecanary...` (T1-038 URL query canary) | BLOCK | BLOCK | **BLOCK** (`?` prefix 매칭 유지) ✅ |
| 5 | `&password=fakecanary&...` (URL query 추가 secret) | BLOCK | BLOCK | **BLOCK** (`&` prefix 매칭 유지) ✅ |
| 6 | `password=fakecanary&...` (line start, T1-040 form body) | BLOCK | BLOCK | **BLOCK** (`^` prefix 매칭 유지) ✅ |
| 7 | `Authorization: Bearer ... ; api_key=xxx` (HTTP header whitespace 후) | BLOCK | BLOCK | **BLOCK** (`\s` prefix 매칭 유지) ✅ |
| **8 NEW (R-1 흡수)** | `payload = "password=fakecanary&user=alice"` (quoted form body literal) | (우연 FP 매칭) | **FN (cover 0)** | **BLOCK** (`"` prefix 매칭) ✅ |
| **9 NEW (R-1 흡수)** | `body = 'api_key=fakecanary&q=hi'` (single-quote literal) | (우연 매칭) | **FN (cover 0)** | **BLOCK** (`'` prefix 매칭) ✅ |

→ **(a+) 정정 = FP 4/4 해소 + canary 7/7 BLOCK 보존 + 신 quoted literal 2/2 BLOCK 확정** ✅

### 4.3 (a) → (a+) 보강 trade-off (사용자 명시 cross-check 답습)

| 항목 | (a) 원안 | **(a+) 보강** |
|---|---|---|
| Python keyword arg FP 해소 | ✅ | ✅ (paren 추가 0 답습) |
| canary 7/7 BLOCK 보존 | ✅ | ✅ |
| quoted body literal FN cover | ❌ (FN 2/2) | ✅ (BLOCK 2/2) |
| semicolon cookie + fragment cover | ❌ (carry-over) | ❌ (carry-over) |
| AST SAFE_CONTEXT 영구 정밀화 | ❌ (carry-over) | ❌ (carry-over) |
| Hermes upstream 답습 본질 | ✅ 유지 | ✅ 유지 (키 목록 보존, prefix 만 확장) |
| 합의 형태 자격 | 풀 3+1 (R-7(b)) | 풀 3+1 (R-7(b)) — 사용자 명시 cross-check 후 (a+) 발효 |

### 4.3 권고 비교 (재정렬)

- **(a)** = ⭐ **신 1차 권고** (사용자 D-FP-1 채택) — 명백한 결함 정정 + canary cover 보존 + Hermes 답습 본질 유지
- **(d)** = 영구 정밀화 (향후 동형 false positives 자동 회피) → **carry-over** (별도 큰 cycle 자격)
- **(c)** = ❌ 결함, layer1.py 회피 불가능
- **(b)** = FN risk
- **(e)** = `.py` 내 실 URL 패턴 FN risk

---

## §5 R-7(b) PC1-2 차등 자격 검토

### 5.1 24번째 entry R-7(b) BLOCKING 답습

| 변경 종류 | 합의 형태 |
|---|---|
| 신규 hook 추가 (Tier-2/3 catalog / provider policy / security gate) | **풀 3+1** |
| 단순 version pin | **단축 합의** |
| **본 sub-cycle의 채택 후보** | **§5.2 매트릭스 답습** |

### 5.2 본 sub-cycle 합의 형태 자격

| 채택 후보 | 합의 형태 자격 |
|---|---|
| (a) alternation 패턴 정정 | **풀 3+1 + 외부 LLM 1+** (G3 도구 본문 변경 + R-4.1 Tier-1 catalog 영향 + Hermes 답습 손상 검증) |
| (b) hook entry exclude 추가 | **단축 합의 자격 검토 의무** (hook entry 변경 = catalog 영향 아닌 filter) — 단 FN risk 권고 하향 |
| (c) src/ 코드 회피 | **1-agent 직접 또는 단축 합의** (lint/framing 답습 + 테스트 영향 검증 의무) |
| (d) AST SAFE_CONTEXT 추가 | **풀 3+1** (도구 본문 변경, 복잡도 증가) |
| (e) `.py` ext alternation skip | **풀 3+1** (Hermes 답습 scope 변경) |

---

## §6 ADR-011 §2.1 (a)~(e) 매트릭스 (PC-1-T3 회귀 자격 보강 한정)

| 조건 | 본 sub-cycle 발효 자격 |
|---|---|
| (a) 사용자 명시 결정 | ⏳ 본 brief 합의 시점 = 사용자 채택 후보 명시 |
| (b)(d) 격리 환경 PoC 실증 + 자동 회귀 검증 | ⏳ 채택 후보 실 구현 후 = 본 D-6 workflow PASS verify + (a)(d)(e) 채택 시 추가 T1-038/T1-040 canary 회귀 evidence 의무 |
| (c) 도구/리소스 stateless · network-free | ✅ 모든 채택 후보 = network-free (local Python AST + regex) |
| (e) 합의 APPROVE 운영조건 | ⏳ 본 brief 합의 발효 시점 충족 |

→ **본 sub-cycle = PC-1-T3 (b)(d) 회귀 자격 *보강*** (33번째 entry MVP-1 PASS 전체 답습 유지, false positive 정정 = secret-scanner 자동 회귀 자격 강화)

---

## §7 합의 형태 권고 + 사용자 결정 영역

### 7.1 합의 형태 권고 (사용자 결정 영역, v1.1 재정렬)

| 후보 | 권고 합의 형태 | 우선순위 |
|---|---|---|
| **⭐ (a) 단독 채택** | **풀 3+1 + 외부 LLM 1+** (R-7(b) PC1-2 차등 답습) 또는 **단축 합의 + 외부 LLM 1+ cross-validation** (명백한 결함 정정 + canary cover 보존 verify) | **신 1차 권고** (사용자 D-FP-1 채택) |
| (a) + (d) 병행 | (a) 즉시 → (d) 별도 풀 3+1 (큰 cycle, carry-over) | 2차 |
| (d) 단독 | **풀 3+1** | 3차 |
| (e) 단독 | **풀 3+1** | 4차 |
| (c) 단독 | ❌ 결함 (v1.1 정정 답습) | 권고 0 |
| (b) 단독 | (FN risk, 권고 하향) | 권고 0 |

### 7.2 사용자 결정 영역 (v1.1 재정렬)

| # | 결정 항목 | 권고 |
|---|---|---|
| **D-FP-1** | 채택 후보 5 (a)~(e) 中 1+ 선택 | **(a)** (사용자 채택 2026-05-27 brief v1.1 정정 후) |
| **D-FP-2** | 합의 형태 | (1) **풀 3+1 + 외부 LLM 1+** (R-7(b) 정확 답습, ceremony 충분) vs (2) **단축 합의 + 외부 LLM 1+ cross-validation** (명백한 결함 정정 + verification §4.2 7/7 PASS 자체 강한 evidence + ceremony 완화 자격) |
| **D-FP-3** | 외부 LLM cross-validation method | (P) Claude 가 tmux + codex bypass sandbox 직접 호출 (24번째 entry pattern 답습) / (Q) 사용자 직접 호출 + 응답 첨부 |
| **D-FP-4** | 회귀 verification 범위 | (1) 본 D-6 workflow re-run + `secret-scanner` PASS verify / (2) `tools/secret_scanner.py` self-test + T1-038/T1-040 canary 재발화 PASS / (3) jarvis 144/144 pytest green 답습 보존 (src/ 본문 변경 0 영역 = 영향 0 예상, 단 secret_scanner.py 자체는 jarvis 의존 0 = 영향 0) |

---

## §8 carry-over (본 sub-cycle 외, v1.2 합의 R-1 흡수 후 갱신)

1. ⭐ **(b1-PC1-D6-fp-edge-extensions)** 신규 carry-over (합의 R-1 비-즉시 권고 흡수) — semicolon `;` cookie separator + fragment `#` OAuth implicit grant 등 추가 delimiter 확장 (Agent A 발견 8 risk + codex N-1+2 답습). 별도 단축 합의 또는 풀 3+1 cycle 자격.
2. ⭐ **(b1-PC1-D6-ast-context)** 신규 carry-over (합의 N-9 권고 흡수) — (d) AST SAFE_CONTEXT 영구 정밀화 prototype design (Agent C 30~50줄 prototype + Call.keywords / FunctionDef.args / AnnAssign SAFE_CONTEXT 매트릭스 답습). 별도 풀 3+1 cycle 자격.
3. **(b1-PC1-D6-contexts)** branch protection contexts 갱신 = 본 sub-cycle 완료 후 진입 (admin scope, 사용자 영역)
4. **(b1-PC1-D6-evidence)** E-D6-1/2/3 evidence capture = 본 sub-cycle CI PASS 후 capture
5. **secret-scanner 패턴 정합성 audit** = 다른 alternation 패턴 외 false positive 가능 검출 분류 audit (자율 영역)

---

## §9 자기진단 (8/8)

| # | 항목 | 상태 |
|---|---|---|
| 1 | 본 brief 자체 실 코드 변경 0건 (file 1 = brief 신규 한정) | ✅ |
| 2 | 답습 출처 7 source 명시 + line-level 인용 cross-check 가능 | ✅ |
| 3 | scope (false-positives 정정) 명확 + 변경 0건 의무 10 항목 (§1.2) | ✅ |
| 4 | T1-041/T1-042 alternation 패턴 본문 본질 분석 (§2) + 검출 10건 raw 분류 (§3) | ✅ |
| 5 | 조치 후보 5 매트릭스 (a)~(e) + trade-off + 권고 (§4) | ✅ |
| 6 | R-7(b) PC1-2 차등 자격 검토 (§5) + ADR-011 매트릭스 (§6) | ✅ |
| 7 | 합의 형태 권고 + 사용자 결정 영역 D-FP-1~D-FP-4 (§7) | ✅ |
| 8 | carry-over 4 항목 (§8) | ✅ |

---

## §10 다음 단계 (단계별 합의 cycle 답습)

1. **본 brief commit** (file 신규 1건 한정)
2. **사용자 결정** D-FP-1~D-FP-4 명시 (1차 권고 = (c) 1-agent 직접 + sort key 위치 변경 + `code=` → `exit_status=` rename + `tests/jarvis/` 회귀)
3. **합의 형태 발효** (사용자 결정에 따라 1-agent 직접 / Reviewer-only / 풀 3+1)
4. **실 구현** (채택 후보 적용)
5. **자동 회귀 evidence capture** (본 D-6 workflow re-run + PASS verify + jarvis 144/144 green 답습 보존)
6. **SESSION + INDEX + commit + push**
7. **carry-over** ((b1-PC1-D6-contexts) 진입 자격 발효 + (d) 별도 cycle 자격)

**자동 다음 단계 진입 금지** (메모리 답습 — 단계별 합의 cycle 패턴).
