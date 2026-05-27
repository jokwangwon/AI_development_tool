OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6874-b41b-7c63-832d-63f39d460587
--------
user
당신은 외부 LLM cross-vendor reviewer 입니다 (OpenAI vendor, Anthropic 가 작성한 brief 의 cross-validation 역할).

## 본 cycle scope

MVP-1 (b1-PC1-D6-false-positives) sub-cycle — secret-scanner 도구의 T1-041/T1-042 alternation 정규식 패턴이 Python source code 의 keyword arg `key=lambda` / `code=exit_code` 등 10건을 false positive 검출. CI 영구 RED 상태 해소 목적.

## 답습 본문

brief 파일: `docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` (10장, v1.1)

핵심 패턴 본문 (tools/secret_scanner.py line 155~158):

현 패턴:
```python
T1-041: (?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+
T1-042: (?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+
```

채택 후보 (a) 정정 후 패턴 (사용자 D-FP-1 채택):
```python
T1-041: (?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+
T1-042: (?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+
```

핵심 변경: alternation 직전 word boundary `(?:^|[?&\s])` prefix 추가.

## verification 7 시나리오 (brief §4.2 답습)

| # | 시나리오 | 현 매칭 | (a) 정정 후 매칭 |
|---|---|---|---|
| 1 | `failures.sort(key=lambda e: e.get(...))` (Python sort FP) | FP | **OK (매칭 0)** — Python keyword arg `(` 직전 |
| 2 | `failures.sort(key=_ts_key, ...)` (named function FP) | FP | **OK** |
| 3 | `WorkerResult(exit_code=exit_code, ...)` (Python dataclass FP) | FP | **OK** |
| 4 | `?api_key=fakecanary...` (T1-038 URL query canary) | BLOCK | **BLOCK** — `?` prefix 매칭 |
| 5 | `&password=fakecanary&...` (URL query 추가 secret) | BLOCK | **BLOCK** — `&` prefix 매칭 |
| 6 | `password=fakecanary&...` (line start, T1-040 form body) | BLOCK | **BLOCK** — `^` prefix 매칭 |
| 7 | `Authorization: Bearer ... ; api_key=xxx` (HTTP header whitespace 후) | BLOCK | **BLOCK** — `\s` prefix 매칭 |

## 답습 의무 (cross-validation 요청 항목)

본 cycle 합의 자격 검토 시 다음 7 항목 평가 의무:

1. **정규식 정정 정확성** — `(?:^|[?&\s])` prefix 가 의도한 false positive 해소 + canary cover 보존 모두 충족하는가? Python regex engine 다른 edge case 있는가?
2. **Hermes upstream 답습 본질 유지** — Hermes `_SENSITIVE_QUERY_PARAMS` (16 keys) + `_SENSITIVE_BODY_KEYS` (14 keys) 답습 본질 (= 키 목록 보존) 손상 0건 여부.
3. **T1-038/T1-040 canary cover 보존** — `docs/phase0/r4-1-trigger-extension-evidence.md` §5.3 답습 — canary 차단 자격 유지 검증.
4. **추가 edge cases / FN risk** — (a) 정정으로 *놓치는* 실 secret 패턴 발견 여부. 예: HTTP body multipart / nested URL / 등.
5. **ADR-011 §2.1 (a)~(e) 5조건 영향** — 본 cycle = PC-1-T3 (b)(d) 회귀 자격 보강 한정 답습 적정성.
6. **R-7(b) PC1-2 차등 자격** — 24번째 entry 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` line 94) "신규 hook = 풀 3+1 / version pin = 단축 합의" — alternation 패턴 본문 변경 자격 분류 정확성.
7. **더 나은 대안** — (b) exclude / (c) src 회피 / (d) AST SAFE_CONTEXT / (e) `.py` ext skip 외 추가 후보 또는 권고 변경 의견.

## 응답 형식

다음 구조로 200~400줄 응답 의무:

```
# (cycle-name) Codex (OpenAI) cross-validation 응답

## §1 자격 검증 (brief 답습 정확성)
## §2 (a) 정정 정확성 평가
## §3 7 항목 평가 매트릭스
## §4 추가 발견 (있을 시) — BLOCKING / 권고 / NOTE 분류
## §5 최종 권고 (APPROVE / REVISE / REJECT + 근거)
## §6 자기진단
```

답변 한국어 + 코드 블록은 영어 답습.
codex
요청하신 brief와 관련 근거 파일을 직접 확인해서, 패턴 변경이 실제 repo 맥락에서 어떤 의미인지 검증하겠습니다. 먼저 scanner 구현과 언급된 문서 근거를 읽겠습니다.
exec
/bin/bash -lc "sed -n '130,180p' tools/secret_scanner.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     r"mem0_[A-Za-z0-9]{10,}"),
    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
     r"brv_[A-Za-z0-9]{10,}"),
]

# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2"),
    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
    ("T1-035", "Hermes H-E", "regex", "Private key block",
     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----"),
    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)"),
    ("T1-037", "Hermes H-G", "regex", "JWT token",
     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}"),
    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@"),
]

# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
     r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
     r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
]

ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
)
"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""

# Compiled regex objects (모듈 import 시 1회 컴파일)
COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
    (pid, src, cat, vendor, re.compile(rgx))
    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
]

# 본 PoC 직접 등록 제외 (R-4.1 §4.2 답습 — alternation 채택, H-J/H-L 직접 등록 false-positive 회피)
SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})

# Redaction marker exclusion (scan-log mode 전용 — GP-2 D-2 contract 답습).
# 사양 §0 — D-2 = "redaction 후 잔존 secret 검증". 본 marker 가 매칭 substring 전체를
# 차지하면 *정상 redacted output* 로 분류, 위반 미카운트 (FP 회피).
REDACTION_MARKER_RE: re.Pattern[str] = re.compile(
    r"(?i)(\[REDACTED\]|\[FILTERED\]|\[MASKED\]|<REDACTED>|<MASKED>|<<masked>>|\*{5,})"
)

exec
/bin/bash -lc "sed -n '1,260p' docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

### 4.1 (a) 채택 시 패턴 정정 본문

**현 패턴 (tools/secret_scanner.py line 155~158)**:
```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
```

**(a) 정정 후 패턴 (word boundary prefix 추가)**:
```python
("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
 r"(?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
 r"(?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
```

**핵심 변경**: alternation 직전 `(?:^|[?&\s])` 추가 — match prefix = line start 또는 `?` (URL query 시작) 또는 `&` (URL query separator / body separator) 또는 whitespace (HTTP header / multiline body)

### 4.2 (a) 정정 효과 verification

| 시나리오 | 현 매칭 | (a) 정정 후 매칭 | 검증 결과 |
|---|---|---|---|
| `failures.sort(key=lambda e: e.get(...))` (FP) | FP | **OK (매칭 0)** | Python keyword arg = 직전 `(` (paren) → 매칭 0 ✅ |
| `failures.sort(key=_ts_key, ...)` (FP) | FP | **OK** | 동형 ✅ |
| `WorkerResult(exit_code=exit_code, ...)` (FP) | FP | **OK** | 동형 ✅ |
| `?api_key=fakecanary...` (T1-038 canary) | BLOCK | **BLOCK** | `?` prefix 매칭 유지 ✅ |
| `&password=fakecanary&...` (URL query 추가) | BLOCK | **BLOCK** | `&` prefix 매칭 유지 ✅ |
| `password=fakecanary&...` (line start, T1-040 form body) | BLOCK | **BLOCK** | `^` prefix 매칭 유지 ✅ |
| `Authorization: Bearer ... ; api_key=xxx` (HTTP header, whitespace 후) | BLOCK | **BLOCK** | `\s` prefix 매칭 유지 ✅ |

→ **(a) 정정 = false positive 해소 + canary cover 보존** ✅

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

## §8 carry-over (본 sub-cycle 외)

1. **(d) AST SAFE_CONTEXT 추가** = 향후 영구 정밀화 (별도 풀 3+1 cycle 자격, 사용자 결정 영역)
2. **(b1-PC1-D6-contexts)** branch protection contexts 갱신 = 본 sub-cycle 완료 후 진입 (admin scope, 사용자 영역)
3. **(b1-PC1-D6-evidence)** E-D6-1/2/3 evidence capture = 본 sub-cycle CI PASS 후 capture
4. **secret-scanner 패턴 정합성 audit** = 다른 alternation 패턴 (T1-041/T1-042) 외 false positive 가능 검출 분류 audit (자율 영역, 별도 sub-cycle 자격)

---

## §9 자기진단 (8/8)

| # | 항목 | 상태 |
|---|---|---|

exec
/bin/bash -lc "sed -n '80,115p' docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
| **R-S1** | brief §2.2.1 + §1.2 + §9.1 의 "ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011" 권위 인용 = ADR-008 본문에 부재 (§A.2 = "Hermes JSONL Export 검증", R1-2 / R2-1 / chmod 600 / entrypoint stat / inotify 모두 ADR-008 본문 0건). 다중 source 권위 chain 손상 확정 | B-5 단독 + Reviewer raw line-level verify (ADR-008 §A.2 line 136 = "Hermes JSONL Export 검증" + ADR-008 §2 line 17~23 = 6 차단조건 본문 한정 + sub-section §2.1 / §2.6 / §2.6.2 / §2.6.4 전부 부재 + R1-2/R2-1 식별자 0건) | (1) brief v1.1 §2.2.1 + §1.2 + §9.1 인용 정정 = "ADR-008 6 차단조건 #1 (SQLCipher) + #6 (Docker 격리 + egress 화이트리스트) cross-reference + governance-preconditions §X 답습 (X 위치 확인 별도 sub-cycle 영역)" (또는 R1-2 식별자 실 source 확인 후 정확한 source 인용) — (2) governance-preconditions / backlog1 합의 자체의 정정 = **본 cycle scope 외** (cross-reference 별도 commit 영역). (3) ADR-008 본문 변경 0건 의무 답습 |

⚠️ **R-S1 = 본 합의의 가장 큰 finding** — Agent A / Agent C / codex 모두 미발견, Agent B 단독 + Reviewer raw line-level verify 시점 확정. 권위 chain 다중 source 손상 = 본 cycle 정정 자격 한정 + cross-reference 정정 별도 sub-cycle 영역.

### 2.4 1-Agent BLOCKING 1개 (Agent A 단독)

| # | BLOCKING | 출처 | 흡수 영역 | 사유 |
|---|---------|------|----------|------|
| **R-6** | R-MVP1-1.5-PC1-1 "미실행 commit 발견" 탐지 경로 명시 | A-4 단독 + codex §4.4 권고 | brief §5.1 R-MVP1-1.5-PC1-1 본문 정정 — "미실행 commit 발견 → dev 환경 강제 메커니즘 재검토" → "미실행 commit 발견 (탐지 경로: (i) hook marker grep / (ii) `pre-commit run --all-files` 결과 CI 비교 / (iii) setup audit log) → dev 환경 강제 메커니즘 재검토 (단축 합의 + 사용자 명시)" | "미실행 commit 발견" 의 탐지 경로 부재 = trigger 발화 자격 0 = trigger 본문 의미 약화 |

### 2.5 Rollback Trigger MINOR REVISE BLOCKING (Agent B 단독)

| # | BLOCKING | 출처 | 흡수 영역 | 사유 |
|---|---------|------|----------|------|
| **R-7** | brief §5.1 Rollback Trigger 3 본문 정정 | B-4 단독 + codex §4 권고 | (a) **R-MVP1-1.5-ST2-1**: ">1초" → "합의된 threshold 초과" (threshold 후보 framing 보존, brief §0.3 #9 답습) / (b) **R-MVP1-1.5-PC1-2**: `.pre-commit-config.yaml` 변경 = 항상 풀 3+1 → "신규 hook = Tier-2/3 catalog / provider policy / security gate 변경 시 풀 3+1, 단순 version pin = 단축 합의" 차등 / (c) **R-MVP1-1.5-AR3-2**: "11 workflow 본문 변경 + 신규 status check 추가" → "11 workflow 본문 변경" (도구 변경 영향 분석) ↔ "신규 status check 추가" (T3 정책 영역) 분리 | 본 brief threshold 후보 framing 보존 정합성 + Rollback Trigger 발화 자격 차등 + 단일 trigger ≠ 다중 영역 |

→ **Reviewer 통합 BLOCKING 7건** (R-1 ~ R-7).

---

## 3. 권고 통합 (12 항목 — 중복 제거)

### 3.1 Defense in depth 결합 영역

| # | 권고 | 출처 |
|---|------|------|
| **N-1** | PC-1 단독 = 우회 가능 (codex §7.2). brief §2.3.3 + §2.3.4 = "PC-1 + PC-3 + AR-3 결합 의무화 시점 발효" 명문 강화 (단, BLOCKING R-2 와 별도, 의미 강화 한정) | A-권고 + B-권고 + C-권고 + codex §7.2 |
| **N-2** | PC-1-T3 mandatory enforcement 명칭 일관 — brief 본문 "PC-1" 단일 명칭 → "PC-1-T3 mandatory enforcement" 또는 "PC-1 (T3 의무화)" 명칭 일관 | A-권고 + codex §1 |
| **N-3** | AR-3 boundary 명문 반복 — brief §2.4.4 + §6.2 = "AR-3 = Backlog #3 의 *AR-3 sub-수단 단독 시점 변경*, Backlog #3 다른 항목 (ST-4 Vault HSM / commit signing / Tier-2/3 catalog 등) 자동 진입 0건" 명문 반복 강화 | A-권고 + C-권고 |

### 3.2 단축 합의 자격 차단 + Evidence 단서

| # | 권고 | 출처 |
|---|------|------|
| **N-4** | brief §4.2 "실 구현 sub-cycle = 단축 합의 + 사용자 명시" → "실 구현 sub-cycle = (b)(d) evidence 충족 시 단축 합의 + 사용자 명시. evidence 미충족 시 단축 자격 0, 풀 3+1 재진입 의무" 단서 추가 | B-권고 + codex §5.1 |
| **N-5** | brief §6.2 "branch protection rule 변경 = 코드 변경 0건과 별개 운영 정책" 직접 명문 묶기 | B-권고 + codex §5.2 |

exec
/bin/bash -lc "rg -n \"T1-038|T1-040|5\\.3|SENSITIVE_QUERY|SENSITIVE_BODY|ADR-011|PC-1-T3|R-7\\(b\\)|PC1-2\" docs tools -S" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tools/workflow_fork_pr_secret_policy_check.py:2:# Stage 5 Cycle 3 — 5.3 fork PR secret 접근 차단 default 정책 검증 도구
tools/workflow_fork_pr_secret_policy_check.py:207:    print("  5.3 fork PR secret 접근 차단 default 정책 검증")
docs/decisions/ADR-008-hermes-adoption-decision.md:89:> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S3 답습]**: 본 line 86 표기 "제5조 관용 (Provider Liquidity, 비협상)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") 中 ADR-008 정정 자격 직접 발효 (R-S3 CRITICAL). ADR-008 = ADR-011 직접 모법 (ADR ↔ ADR 부록 B Amendment 패턴). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 87/98/107/274/329/366/370 (P2 cross-ref + P3 본문) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
docs/decisions/ADR-008-hermes-adoption-decision.md:104:- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-008 부록 B Amendment R1 specific 갱신의 권위 근거. §2.1 (a)~(d) 4조건 + §2.2 G1a/G1b 분리 + §2.3 Hermes ≠ root of trust 영구 권위 + §2.4 T1/T2/T3 영구 권위)
docs/decisions/ADR-008-hermes-adoption-decision.md:159:**근거 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
docs/decisions/ADR-008-hermes-adoption-decision.md:167:본 Amendment 이전 부록 A R1 텍스트는 "외부 pre-record hook"을 수단으로 가정한 표현을 포함했다. 본 Amendment는 그 가정을 ADR-011 §2.1 수단/목적 분리 원칙에 따라 갱신한다.
docs/decisions/ADR-008-hermes-adoption-decision.md:178:정식 충족 조건은 ADR-011 §2.2 G1b 정식 충족 조건 표를 따른다.
docs/decisions/ADR-008-hermes-adoption-decision.md:182:이 해석은 **ADR-011 Means-vs-Ends Redaction Principle**에 의해 권위화된다. 본 Amendment는 ADR-011 §2.1~§2.3을 ADR-008 R1 specific 갱신으로 적용한 것이며, 일반 원칙 본문 해석은 ADR-011을 우선 참조한다.
docs/decisions/ADR-008-hermes-adoption-decision.md:190:3. **Hermes는 root of trust가 아니다** (ADR-011 §2.3 권위 위계 명문화).
docs/decisions/ADR-008-hermes-adoption-decision.md:202:차단조건 #2~#6은 변경 없음. 6 차단조건 자체의 비협상성은 유지된다 — 본 Amendment는 #1 충족 *수단*을 ADR-011 (a)~(d) 4조건 하에 재정의한 것이다.
docs/decisions/ADR-008-hermes-adoption-decision.md:206:차단조건 #1 정식 exit 기준은 다음 6단계 완료를 요한다 (R-4.1 은 R-4 추가 격리 PoC 분기로 ADR-011 §2.1 (b) 직접 충족 산출):
docs/decisions/ADR-008-hermes-adoption-decision.md:222:- ✅ R-7 SOP §7.3 단축 합의 (Reviewer-only, ADR-011 §2.4 T2) APPROVE — `docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` (13 Reviewer 항목 + 8 PASS 조건 + 5 통제 수단 명시)
docs/decisions/ADR-008-hermes-adoption-decision.md:226:본 ADR-008 부록 B.6 갱신은 ADR-011 §2.4 T2 절차 (사용자 승인 + Reviewer-only 단축 합의) 답습. **자동 승격 아님**.
docs/decisions/ADR-008-hermes-adoption-decision.md:228:R-4 / R-4.1 / R-5 / R-6 / R-7 진행 상태는 본 Amendment 가 아니라 ADR-011 §2.2 표 또는 `docs/CONTEXT.md` 의 4 게이트 진행 상태에서 추적한다.
docs/decisions/ADR-008-hermes-adoption-decision.md:242:- ADR-011 §2.3 (Hermes ≠ root of trust) + §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리)
docs/decisions/ADR-008-hermes-adoption-decision.md:255:> 본 부록 C 는 P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 의 *Hermes PMO 격상 조건 cross-reference 강화* 한정. 8 권위 layer 중첩 답습으로 *영구 권위 정착 가능* 하나, *현 시점 격상 발생 0건*.
docs/decisions/ADR-008-hermes-adoption-decision.md:260:2. 본 부록 C 는 *Hermes PMO 격상 조건* 명시 강화 + ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 + P2 v3 *cross-reference* 매트릭스 제공
docs/decisions/ADR-008-hermes-adoption-decision.md:296:> **Hermes PMO 격상은 *자동 발생 절대 금지*** (ADR-011 §2.4 T3 위반).
docs/decisions/ADR-008-hermes-adoption-decision.md:310:| 1 | ADR-011 §2.4 T3 (Constitution / ADR / Harness Gates 정의 자체의 변경 = 자동 금지) | 영구 권위 |
docs/decisions/ADR-008-hermes-adoption-decision.md:353:6. ADR-011 §2.3 (Hermes ≠ root of trust 영구 권위)
docs/decisions/ADR-008-hermes-adoption-decision.md:369:| **ADR-011 §2.3** (Hermes ≠ root of trust 영구 권위) | 본 §C.4 권위 위계 + §C.6 ADR-013 보류 사유 #6 |
docs/decisions/ADR-008-hermes-adoption-decision.md:370:| **ADR-011 §2.4** (T1/T2/T3 자동 학습 vs 정책 변경 분리) | 본 §C.4 #1 (T3 자동 금지) |
docs/decisions/ADR-008-hermes-adoption-decision.md:386:- ✅ ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 + P2 v3 cross-reference 보강
docs/decisions/ADR-008-hermes-adoption-decision.md:405:본 부록 C 발행은 ADR-011 §2.4 T2 절차 (사용자 승인 + Reviewer-only 단축 합의) 답습 — *자동 격상 아님*. 본 부록 C 자체가 *Hermes PMO 격상 조건* 명시 강화 한정.
tools/provider_url_scanner.py:11:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
tools/schema_validator.py:9:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 + §2.3 운영 함의 #1 (Tools verify Hermes 출력)
docs/decisions/ADR-010-sqlcipher-vault-key-management.md:175:- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-010 Vault HSM 키 관리는 ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 가능 영역. 본 ADR-008 부록 B Amendment 답습)
tools/history_anchor_verifier.py:8:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
tools/jsonl_hash_chain.py:20:  - T3 자동 정책 변경 금지 (ADR-011 §2.4) — 자동 revert 0건, BLOCK + manual
docs/decisions/ADR-012-evidence-ledger-protection.md:6:**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity, 관용), ADR-011 §2.1 (수단/목적 분리), §2.3 (Hermes ≠ root of trust), §2.4 (T1/T2/T3)
docs/decisions/ADR-012-evidence-ledger-protection.md:7:**모법 ADR**: ADR-011 (Means-vs-Ends Redaction Principle)
docs/decisions/ADR-012-evidence-ledger-protection.md:12:**[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S4 답습 + R-1 (P4) 신설 *기각* 답습]**: 본 ADR-012 line 6 (상위 권위) + line 61 (§1.4 cross-ref 표 cell) + line 579 (영구 핵심 제약 표) + line 665 (관련 문서) 표기 "헌법 제5조 (Provider Liquidity, 관용)" / "헌법 제5조 관용" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. **line 61 = (P2) cross-ref 표 cell 처리** ((P4) 신규 verbatim 유형 신설 *기각* — R-1 + 기각-2 답습, Reviewer 권한 한계 (11) sub-boundary 신설 *기각*). 본 cycle = gov §1.1 line 78 verbatim 명문 4 source *외* 추가 동형 source 자격 식별 (R-S4 HIGH, ADR-012 = 명문 4 source 외 추가 동형 매핑 자격 강함). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 62/455/513/552/555/561/583/597 (P2 ADR-011 cross-ref + P3 "Provider Liquidity 4-way → 5-way" 본문 다수) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
docs/decisions/ADR-012-evidence-ledger-protection.md:40:**PASS 성립 4 요건** (G3 §5.3):
docs/decisions/ADR-012-evidence-ledger-protection.md:64:| **ADR-011 §2.1 (수단/목적 분리)** | 본 ADR 자체가 Evidence 무결성 = 목적, hash chain + signed/append commit + JCS = 수단. (a)~(d) + (e) 5조건 답습 (§4) |
docs/decisions/ADR-012-evidence-ledger-protection.md:65:| **ADR-011 §2.3 (Hermes ≠ root of trust)** | Hermes 는 ledger entry 생성 가능 (T1 자동 학습), 단 promotion / approval 은 사용자 명시 (T2). Hash chain + signed/append commit = Hermes 변조 차단 운영 매커니즘. **본 ADR-012 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 직접 답습 — 외부 LLM 2 C-15 / Agent B Gap-18) |
docs/decisions/ADR-012-evidence-ledger-protection.md:66:| **ADR-011 §2.4 (T1/T2/T3)** | prev_hash 검증 실패 자동 revert = T3 위반 위험 → BLOCK + manual review 채택 (외부 LLM 2 C-3 / Agent B C-3) |
docs/decisions/ADR-012-evidence-ledger-protection.md:69:| **G3 §1.3 + §5.3** | Evidence 결정 5 운영 규칙 + PASS 성립 4 요건 |
docs/decisions/ADR-012-evidence-ledger-protection.md:99:**원칙 8**: Evidence Ledger 는 *append-only* — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4).
docs/decisions/ADR-012-evidence-ledger-protection.md:180:- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)
docs/decisions/ADR-012-evidence-ledger-protection.md:255:5. **자동 revert 금지** (T3 위반 — ADR-011 §2.4)
docs/decisions/ADR-012-evidence-ledger-protection.md:286:| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) 정책/권한/증거 손실 BLOCK |
docs/decisions/ADR-012-evidence-ledger-protection.md:298:- `semantic_diff` 판단 = 사용자 명시 review (ADR-011 §2.4 T2/T3 사용자 승인)
docs/decisions/ADR-012-evidence-ledger-protection.md:354:**4 항목 모두 본 ADR 권위로 차단**. ADR-011 §2.3 (Hermes ≠ root of trust) 운영 매커니즘 흡수.
docs/decisions/ADR-012-evidence-ledger-protection.md:412:ADR-011 §7.3 답습 패턴 ("본 ADR-011 은 Hermes 안전성을 선언하지 않는다 — Hermes 는 검증 대상이며, 본 ADR-011 은 검증 외부화의 권위 근거이다").
docs/decisions/ADR-012-evidence-ledger-protection.md:436:## 4. ADR-011 §2.1 (a)~(d) + (e) 5조건 답습 (Means-vs-Ends Pattern)
docs/decisions/ADR-012-evidence-ledger-protection.md:438:본 ADR-012 는 ADR-011 §2.1 5조건 패턴 답습 (수단/목적 분리):
docs/decisions/ADR-012-evidence-ledger-protection.md:467:본 ADR-012 자체로 충족. ADR-011 §2.3 + §2.4 cross-reference 명시 (§1.4).
docs/decisions/ADR-012-evidence-ledger-protection.md:497:### 5.3 옵션 C (비채택): G3 §1.3 + §5.3 본문 보강 단독 (ADR 신규 0건)
docs/decisions/ADR-012-evidence-ledger-protection.md:499:- 장점: 새 권위 0건, ADR-011 §2.4 답습
docs/decisions/ADR-012-evidence-ledger-protection.md:513:G3 §1.3 + §5.3 의 PASS 성립 4 요건 중 (ii) Evidence Ledger entry 가 부재하면 PASS 자체가 성립 불가. Evidence Ledger 변조 가능성 = G3 root-of-trust 직접 훼손 → 본 ADR 권위로 보호 의무.
docs/decisions/ADR-012-evidence-ledger-protection.md:522:ADR 신규 발행 = T3 변경 (ADR-011 §2.4) → 풀 3+1 + 외부 LLM 1+ 의무 (G3 §4.4.2). 본 PR-2 = 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) 충족. C-14 cross-vendor (P2 v3 정식 채택 진입 전) 추가 의무 (외부 LLM 2 C-14 답습).
docs/decisions/ADR-012-evidence-ledger-protection.md:557:- ADR-011 §2.1 (a)~(d) + (e) 5조건 패턴 답습 — 미래 다른 비협상 조항 해석에도 적용 가능
docs/decisions/ADR-012-evidence-ledger-protection.md:571:- **본 ADR 은 Hermes 안전성을 선언하지 않는다** — Hermes 는 검증 대상이며, 본 ADR 은 검증 외부화의 권위 근거이다 (ADR-011 §7.3 직접 답습)
docs/decisions/ADR-012-evidence-ledger-protection.md:582:| Hermes ≠ root of trust | ADR-011 §2.3 영구 권위 | §2.12 (Hermes 변조 차단 매트릭스 4항목) + 원칙 3 + 원칙 7 + Hermes-originated commit auto-reject + ADR-011 §7.3 답습 | **HIGH** |
docs/decisions/ADR-012-evidence-ledger-protection.md:584:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | §2.7 (BLOCK + manual review, 자동 revert 금지) + 원칙 7 (External LLM agent="user" 강제) + §2.12 (Hermes 변조 차단) + Hermes T1 자동 학습 vs T2 사용자 승인 분리 | **HIGH** |
docs/decisions/ADR-012-evidence-ledger-protection.md:585:| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + (e) | §4 (a)~(e) 5조건 답습 — (a) 비교표 / (b) Implementation 영역 / (c) ADR-012 자체 / (d) R-6 답습 확장 / (e) 본 합의 APPROVE | **HIGH** ((b) 별도) |
docs/decisions/ADR-012-evidence-ledger-protection.md:655:4. ADR-011 §2.1 + §2.3 + §2.4 cross-reference 답습
docs/decisions/ADR-012-evidence-ledger-protection.md:668:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 / §2.3 / §2.4 / §7.3 (모법)
tools/secret_scanner.py:10:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
tools/secret_scanner.py:155:    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
tools/secret_scanner.py:157:    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
tools/secret_scanner.py:173:SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})
tools/pre_commit_install_audit.sh:2:# pre_commit_install_audit.sh — PC-1-T3 bypass detection (3 탐지 경로 통합 verify)
tools/pre_commit_install_audit.sh:15:#   0 = 3 탐지 경로 모두 PASS (PC-1-T3 발효 자격 정상)
tools/pre_commit_install_audit.sh:16:#   1 = 1 이상 탐지 경로 FAIL (PC-1-T3 bypass 의심 → Rollback Trigger R-MVP1-1.5-PC1-1 발화 자격)
tools/pre_commit_install_audit.sh:20:echo "=== PC-1-T3 mandatory enforcement audit ==="
tools/pre_commit_install_audit.sh:68:    echo "[OK] 3 탐지 경로 모두 PASS — PC-1-T3 발효 자격 정상"
tools/pre_commit_install_audit.sh:71:    echo "[FAIL] $FAIL_COUNT/3 탐지 경로 FAIL — PC-1-T3 bypass 의심"
docs/decisions/ADR-011-means-vs-ends-redaction.md:1:# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)
docs/decisions/ADR-011-means-vs-ends-redaction.md:87:| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
docs/decisions/ADR-011-means-vs-ends-redaction.md:120:본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.
docs/decisions/ADR-011-means-vs-ends-redaction.md:156:### 옵션 A: ADR-011 단독 (Amendment 없음)
docs/decisions/ADR-011-means-vs-ends-redaction.md:159:- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.
docs/decisions/ADR-011-means-vs-ends-redaction.md:161:### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)
docs/decisions/ADR-011-means-vs-ends-redaction.md:169:### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**
docs/decisions/ADR-011-means-vs-ends-redaction.md:172:  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
docs/decisions/ADR-011-means-vs-ends-redaction.md:173:  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
docs/decisions/ADR-011-means-vs-ends-redaction.md:174:  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
docs/decisions/ADR-011-means-vs-ends-redaction.md:190:system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.
docs/decisions/ADR-011-means-vs-ends-redaction.md:192:### 5.3 G1a/G1b 분리의 영구화 필요성
docs/decisions/ADR-011-means-vs-ends-redaction.md:268:- R-4: ✅ **완료** — `docs/architecture/redaction-pattern-equivalence.md` (Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교 + gap 식별 + 보충 권고, ADR-011 §2.1 (a) 충족, 2026-05-06)
docs/decisions/ADR-011-means-vs-ends-redaction.md:269:- R-4.1: ✅ **완료** — `docs/phase0/r4-1-trigger-extension-evidence.md` + `docker/r4-1-poc/` (Tier-1 42종 trigger UDF 확장 + Docker 격리 환경 PoC PASS, ADR-011 §2.1 (b) 충족, 2026-05-06)
docs/decisions/ADR-011-means-vs-ends-redaction.md:271:- R-6: ✅ **완료** — `.github/workflows/r2-canary.yml` (CI/nightly canary regression workflow, ADR-011 §2.1 (d) 자동 회귀 검증 경로, 2026-05-06) + R-6 GitHub Actions actual run `25482284523` PASS (24초, verdict=PASS, 42/42 BLOCK, leak 0, 2026-05-07)
tools/evidence_pass_gate.py:9:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
tools/boundary_guard.py:10:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 + §2.4 T1/T2/T3
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:6:**상위 권위**: 헌법 제5조-2 관용 (Provider Liquidity, 비협상), ADR-004 (외부 SDK 우선), ADR-008 (Hermes 도입 Option B), **ADR-011 §2.3 (Hermes ≠ root of trust)**, **ADR-012 §원칙 5 (Provider Liquidity 5-way Multi-layer Defense)**
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:16:2. **Hermes PMO ≠ provider 직접 소유** (§2.3 신설) — Hermes PMO (활성화 후 후보 시점) 가 provider SDK 직접 import / 모델명 분기 코드 *금지*. P1 facade 단일 진입점 강제 (ADR-011 §2.3 + Provider Liquidity 5-way Layer 1 답습).
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:89:| Provider 추가 / 제거 / 교체 | ❌ (자기 격상 금지 — ADR-011 §2.4 T3) | ✅ (config 변경 + 사용자 명시 승인 — T2) |
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:92:- ADR-011 §2.3 (Hermes ≠ root of trust) — Hermes 권한 위계 답습
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:186:- v2.0 진입 = *수단 변경* (LiteLLM → 자체 Adapter), *목적 보존* (Provider Liquidity 비협상) — ADR-011 §2.1 (a)~(e) 5조건 답습 의무
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:228:| Hermes PMO ↔ provider 분리 (§2.3) | **PASS** | ADR-011 §2.3 + ADR-008 차단조건 #4 + ADR-012 §원칙 6 + 헌법 5조 답습 |
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:261:- **본 ADR §2.3 Hermes PMO ↔ provider 분리는 영구 유지** — Hermes PMO 격상 시점에도 provider 소유 권한 부여 *금지* (T3 영역, ADR-011 §2.4 답습).
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:262:- **본 ADR §5 Provider Liquidity 5-way 모법 ADR 권위는 영구 유지** — 자체 Adapter v2.0 진입 시에도 5 Layer 모두 보존 의무 (ADR-011 §2.1 (a)~(e) 5조건 답습).
docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:273:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.3 (Hermes ≠ root of trust 영구 권위)
tools/rewrite_defense_check.py:9:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
docs/CONTEXT.md:5:**최종 업데이트**: **2026-05-27 세션 — ⭐⭐⭐ 24번째 entry: MVP-1 1.5차 보강 entry brief 풀 3+1 + 외부 LLM 1+ APPROVE w/ COND (BLOCKING 7 + 권고 12) + ⭐⭐ 23번째 entry: roadmap-mvp1 DRAFT → APPROVED + ⭐⭐ 22번째 entry: Layer 2 설계 cycle**. 24번째 entry: MVP-1 GP-3 + GP-5 1.5차 보강 4 sub-수단 (S-3 detect-secrets 부분 통합 + ST-2 inotify sidecar + PC-1-T3 mandatory enforcement + AR-3 통합 PR auto-reject) **진입 합의 entry brief**. brief v1 506줄 → 사용자 승인 → (B) carry-over verbatim 변경 (Claude 가 tmux + codex bypass sandbox 직접 호출, OpenAI vendor cross-vendor 충족) → codex (gpt-5.5) 응답 capture 270줄 (REVISE AS ENTRY BRIEF INPUT + 3 필수 + 5 권고) → §7.3 자격 검증 7/7 통과 → 풀 3+1 합의 (Agent A 313 + Agent B 337 + Agent C 262 + Reviewer 통합 305 = APPROVE WITH CONDITIONS BLOCKING 7 + 권고 12) → brief v1.1 1pass 흡수 (506 → 570줄, +64, ceremony-inflation 차단) → 본 commit `9638521` (8 파일 +2149 줄) → push 완료 (`c2bcb19..9638521`). ⭐⭐⭐ **R-S1 Reviewer 단독 격상 + raw line-level verify**: ADR-008 §A.2 = "Hermes JSONL Export 검증" + §2.6 sub-section 부재 + R1-2 / §2.6.4 식별자 ADR-008 본문 0건 (Agent B 단독 식별, codex 미언급, Agent A/C 미언급), 다중 source 권위 chain 손상 확정 — brief v1.1 인용 정정 한정 (ADR-008 6 차단조건 #1 SQLCipher + #6 Docker 격리 cross-reference), governance-preconditions 5 위치 + backlog1 합의 본문 + 정확 R1-2 source 일관 정정 = **본 cycle scope 외 cross-reference 별도 commit 영역 (N-9 권고)**. **3-way 일치 BLOCKING 3** (R-1 ADR-011 (a)~(d) + 합의 APPROVE 운영조건 (e) 정정 + R-2 PC-1 (b)(d) T3 mandatory PoC 미충족 재분류 + R-3 AR-3 required status check = workflow 파일명 ≠ 실제 check name GitHub branch protection job-level mapping). **2-way 격상 BLOCKING 2** (R-4 S-3 plugin identifier 정확화 `AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` + `--baseline` 미사용 CI assertion + R-5 ST-2 evidence 3 단계 = event 인지 + signal 전달 + 메인 workload fail-closed 확인). **1-Agent BLOCKING 2** (R-6 R-MVP1-1.5-PC1-1 탐지 경로 명시 (hook marker / pre-commit run / setup audit) + R-7 Rollback Trigger 3 정정 ST2-1 threshold framing / PC1-2 차등 / AR3-2 분리). **권고 12 (N-1~N-12)**: PC-1 결합 효과 명문 / PC-1-T3 명칭 일관 / AR-3 boundary 반복 / 단축 자격 차단 단서 / branch protection 직접 묶기 / FP 기준 / cross-reference 별도 commit 2 / 외부 LLM 2+ 향후 / 옵션 (B) 권고 / 사용자 명시 묶기. **cross-vendor 일치 매트릭스**: codex 14 finding 모두 흡수 (BLOCKING 격상 6 + 권고 답습 4 + 형식 차이 통합 4). **메타 자기진단 8/8 통과** (3 Agent 병렬 독립 + cross-vendor + Reviewer 격상 자격 + ceremony-inflation 차단 + meta-cycle 차단 + 단계별 합의 cycle + Provider Liquidity + 본 합의 진행 0건 의무). **원칙 준수 14/14**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 변경 0 / ADR 본문 갱신 0 / 헌법 0 / roadmap 본문 변경 0 / MVP-1 PASS 재선언 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / Tier-2/3 catalog 확장 0 / threshold 고정 0 / 자동 진입 0 (단계별 합의 cycle 답습). **carry-over (다음 세션 사용자 명시 의무, 자동 진입 0건)**: (b1) MVP-1 1.5차 보강 실 구현 sub-cycle 4개 (S-3 / ST-2 / PC-1 / AR-3 각각 별도 단축 합의 + 사용자 명시, 진입 순서 자유) / (b2) R-S1 권위 chain 정정 sub-cycle (governance-preconditions 5 위치 + backlog1 합의 본문 + 정확 R1-2 source 일관 정정, cross-reference 별도 commit) / (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 sub-cycle / (c) MVP-1 Implementation Evidence PASS 발효 합의 (4 sub-cycle 완료 + ADR-011 §2.1 (a)~(d) + (e) 5/5 + conditions 해소 + 사용자 명시 별도) / (d) `src/adapters/llm/facade.py` placeholder → real 본문 (TR-1 별도 trajectory) / (e) untracked dashboard 3 파일 (jarvis_dashboard.{html,py} + streamlit_dashboard.py) 처리 (채택/폐기/이동 사용자 결정 영역). **23번째 entry**: audit brief (21 도구 + 11 workflow + .pre-commit + .importlinter + adapters/llm placeholder 실 구현 완료 확인) → (a) Reviewer-only 단축 합의 (5/5 풀 3+1 승격 trigger 0건 발화) → roadmap-mvp1 line 826/827 갱신 (본문 §1~§8 변경 0건). carry-over (b) scope 명시: 4 sub-수단 모두 + 풀 3+1 + 외부 LLM 1+ = 본 24번째 entry 의 *발효 결과*. **22번째 entry**: Jarvis 자가진화 Layer 2 (제안 생성) 설계 cycle + 보조 jarvis_hud TTS team-lucid/F5-TTS-ko 한국어 발효. HEAD = `9638521` (push 완료). ▼ **이전 세션 (carry-over)**: **2026-05-25 세션 — ⭐⭐⭐ (g1-N-3') HIGH 통합 cycle (10번째 entry, 5 후속 cycle 통합 결합 cycle, R-13 (4-c) 동형 패턴 직접 적용 — Reviewer 권한 한계 (8) "결합 cycle 진입 자격 평가 자격 0" 예외 자격 발효 시점, brief v1 `cc9c0a0` 639줄 → 풀 3+1 합의 `fea84bf` 309줄 APPROVE w/ COND BLOCKING 14 + Reviewer 단독 격상 R-S1~R-S6 + 권고 11 + NOTE 22 + 기각 5 → brief v1.1 + 5 명문 정정 (γ-2) chain commit 6 commit chain `2633539` brief v1.1 (보강) + `0d72799` (g1-N-3-hermes) hermes v3 line 13/377/709 (P1)(P2) + `ab96e30` (g1-N-3-pamsd) pamsd line 27 (P2) + §11.4.2 cross-ref + `717ab00` (g1-N-3-gov) gov line 3/26/78 (P1) + §1.1 cross-ref + `394e4ec` (g1-N-3-adr-009-010) ADR-009 line 6/270 + ADR-010 line 181 (P2) + 본 정리 commit. 실 정정 = 10 위치 + 2 cross-ref block (5 파일). Reviewer 권한 한계 (10) 신규 격상 7→11 sub-boundary 확장 (10-a~10-k) + §10.6 영구화 차단 4→7 조건 확장. 1회 한정 + 영구화 0건 의무. (g1-N-3-adr-008+sip+adr-012') HIGH 신규 carry-over 권고. ⭐⭐⭐ **본 후속 세션 (g1-N-3-adr-008+sip+adr-012') HIGH cycle 11번째 entry chain 영구 종결 완료**: MEMORY.md cleanup (38KB → 1.3KB, 97% 감소) → brief v1 `b55e0c9` 561줄 → 풀 3+1 합의 `209f04d` 235줄 APPROVE w/ COND BLOCKING 11 + ⭐⭐⭐ R-S1 CRITICAL (hermes-not-root-of-trust-runtime.md line 23/176/1040 = gov §1.1 line 78 명문 4 source *외 유일* 추가 동형 source 신규 식별, Agent C 단독 + Reviewer raw cross-check 강화) + R-S2 헌법 line 80 self-inconsistency ((g1-O') carry-over) + R-S3 gov §1.1 정의 범위 정합성 + 권고 9 + NOTE 18 + 기각 4 → brief v1.1 `c9493c0` (+337/-381, R-S1 흡수 + 4 source 확장 + (P4)/(11)/(g1-N-4) 기각 + chain 영구 종결 의무) → 4 source cross-ref block 1 commit `f20fce3` (sip §2.3 + ADR-008 §관련 문서 + ADR-012 header + hermes-not-root §header, **(f) cross-ref block 만 채택**, (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, 4 source 본문 verbatim 변경 0건) + 본 정리 commit. **(g1-N-3) chain 영구 종결 명문 의무 발효** (R-10 + R-rec-8 답습) + Reviewer 권한 한계 (11) sub-boundary 신설 *기각* 본 합의 발효 (R-1 + 기각-3 답습) + §10.6 7→9 조건 확장 ((10.6-h) (11) 신설 차단 + (10.6-i) chain 영구화 차단). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" 채택 (R-rec-3 + 사용자 명시 직접 확인). 본 cycle 머신 변경 0건, `tests/jarvis/` 59 green 불변**. ▼ **이전 세션 (carry-over)**: **2026-05-24 세션 — Phase 2 EXECUTED(`c66756b`) + M3·M4 단독 미충족 합의(`d2d7bf9`) + Phase 3 entry brief v1(`cc145fd`)/v1.1(`25eb008`) + 풀 3+1 합의(`e76acc8`) + 1차 정리(`3729997`) + ⭐ Phase 3 실 빌드 cycle EXECUTED(`7209743`) + ⭐ Provider Liquidity deep-dive 합의 cycle (`9ed376a` → `a9e1e88` → `8ae1ab6`) + 3차 정리(`2b456f8`) + ⭐ format 가족별 분류 cycle (`f305174` → `d75dceb` → `eca4cf5`) + 4차 정리(`7bbc2e3`) + ⭐ (g1-A) 채택 cycle (`fc6731e` → `d0f516d` → `bdcc3a6`) + 5차 정리(`2ff09d6`) + ⭐ (g1-N) 헌법 5조-2 신설 자격 평가 cycle (6차 entry, `6f64491` → `1ec9c5e` BLOCKING 22 + Reviewer 격상 5 → `58e06d5`) + 6차 정리(`7a4b574`) + ⭐⭐⭐ (g1-N-1) 헌법 5조-2 본문 변경 commit cycle (7차 entry, `5b0c0ab` → `77f36cf` BLOCKING 14 + Reviewer 격상 4 → `148fbbe` = 본 세션 + 본 프로젝트 최초 + 유일 헌법 본문 변경 commit, R-19 단계 (4) 직접 적용) + ⭐⭐⭐ (g1-N-2) ADR-011 line 6/245 매핑 정정 cycle (8차 entry, `8207f55` → `07cd3f4` BLOCKING 10 + Reviewer 격상 3 → `3bdb1be` = 본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit, Reviewer 권한 한계 (1) 예외 자격 발효 시점) + 7-8차 통합 정리(`3f84c26`) + ⭐⭐ **(g1-N-3) CLAUDE.md / roadmap.md 정합 정정 자격 평가 cycle (9차 entry, 사용자 "(g1-N-3)" + (β) CLAUDE.md+roadmap.md + 정공법 + (g1-N-3') 통합 평가 명시) 진입 → entry brief v1(`19b0f76`, 522줄, (g1-A) 합의 §7.1 (g1-N-3) + (g1-N-2) §12.2 #5 carry-over 직접 발효) → 풀 3+1 합의(`386c552`, 423줄, APPROVE w/ COND, BLOCKING 12 + 권고 16 + NOTE 10 신규, 기각 0, Reviewer 단독 격상 4 R-S1~R-S4 raw line-level direct cross-check: §2.3 line 143~146 라벨 ↔ §4.1 (i)~(iv) 매트릭스 내부 모순 / CLAUDE.md grep "Provider Liquidity"/"5조-2"/"제5조" verbatim 0 matches 정량 / 헌법 line 80 + ADR-011 line 212 + hermes v3 line 13 3-way trade-off carry-over 영구 / provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 (g1-N-3-pamsd) 신규 분리 HIGH, 4-way 일치 BLOCKING 1 R-1 §1.4 ↔ §6.3 분해 매핑 표) → brief v1.1 + CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 단일 atomic commit(`afd1a65`, 522→608줄 + 3 파일 변경, R-19 답습 단계 (4) 직접 적용, Reviewer 권한 한계 8 → 9 격상 + (9) 신규 CLAUDE.md/roadmap.md 본문 정정 자격 boundary 발효 + (9-a)~(9-d) sub-boundary 직접 적용 완료, R-13 (4-c) 동형 패턴 + (1)(4) chain 답습)**. HEAD = 본 9차 정리 commit (commit 별도 명시 의무).
docs/CONTEXT.md:7:**본 세션 핵심**: SESSION_05-23 미포함 carry-over 3 commit + 본 세션 1차(Phase 3 합의 + brief v1.1) + ⭐ 2차(Phase 3 실 빌드 cycle) + ⭐ 3차 (Provider Liquidity deep-dive cycle) + ⭐ 4차 (format 가족별 분류 cycle f-K) + ⭐ 5차 ((g1-A) 채택 cycle) + ⭐ **6차 ((g1-N) 헌법 5조-2 신설 자격 평가 cycle, 헌법급 변경 R-9 답습 영구 의무 cycle)** 통합. **(g1-N) cycle 합의 BLOCKING 22 핵심**: 🔴 **Reviewer 단독 격상 5 (raw line-level direct cross-check)** — ⭐⭐⭐ **R-S1 (A-B1 + C-S3 격상, 가장 큰 finding)**: 헌법 `PROJECT_CONSTITUTION.md` line 95~98 verbatim — line 97 "**이 헌법은 프로젝트의 모든 활동에 우선한다.**" + **line 98 "헌법 수정은 반드시 3+1 에이전트 합의를 거쳐야 한다."** = **본 cycle 직접 모법** (헌법 자체 수정 절차 명문). brief v1 §1.4 R-9 7 항목 (2)·(7) 출처 chain 에 line 98 직접 모법 인용 0건 + §2.2 verbatim 인용 line 40~46 만, line 95~98 미인용 → brief v1.1 §1.4 (2) + §2.2 verbatim 추가 답습 의무. / ⭐⭐ **R-S2 (B-B1 + B-S2 격상)**: ADR-011 line 245 verbatim "제5조 **관용** (Provider Liquidity, 비협상)" + line 212 "Provider Liquidity 영향 | **무관**" — "관용" = "무관" 동의어 = ADR-011 *자체* stance 단어, 헌법 5조-2 *비협상* 본문 단어 아님. brief 후보 (iii) verbatim "## 제5조-2: Provider Liquidity 원칙 (**관용**, **비협상**)" = **제목 동시 명문 = 의미 자체 충돌** → 후보 (iii) = **위험한 후보** 분류, Provider Liquidity 본질 약화 risk 강함 (R-4 답습 영구 위반 risk). / ⭐⭐ **R-S3 (B-B3 + B-S1 + A-B2 + B-B4 격상)**: (1) 헌법 line 67~73 verbatim "## 제8-2조: 환경 관리 원칙" — **헌법 본문에 *이미* "X조-#" 패턴 선례 존재** → 본 cycle 5조-2 신설 = ADR-011 §2.1 (e) 후속 패턴 답습 **강한 evidence**. (2) ADR-008 부록 B line 153~228 verbatim — **부록 B = ADR-008 본문 §6 차단조건 #1 충족 *수단* amendment, ADR-011 권위화 → ADR-008 본문 갱신 = ADR ↔ ADR amendment 패턴 모법** (A-B2 정확). brief framing "헌법 ↔ 헌법 amendment 모법" **부정확** — 정확한 framing = "ADR ↔ ADR 모법, 헌법 ↔ 헌법 amendment 모법 *≠*". 본 cycle 답습 자격 3 패턴: line 155 "단축 합의 — Reviewer-only" + line 224 "자동 승격 아님" + line 228 "별도 결정". / ⭐ **R-S4 (C-S4 + C-B5 격상)**: 본 cycle 진입 시점 system reminder verbatim "**WARNING: MEMORY.md is 26.7KB (limit: 24.4KB)**" → MEMORY.md 24.4KB limit 이미 초과 (+2.3KB). brief §9 정직성 20 항목 중 MEMORY.md limit 명문 0건. 본 cycle 합의 결과 메모리 신규 entry 등재 자격 = 사용자 명시 + 별도 cycle + index entry 200 chars + topic 파일 분리 의무. / ⭐⭐ **R-S5 (A-S3 + B-B7 + B-S3 3-way 격상, 가장 강한 정합성 evidence)**: brief §0 #11 "**§3·§4**" vs §10.1 #11 "**§3·§4·§5·§8**" *직접 비대칭* → R-15 = R-S3 답습 영구 의무 직접 위반. (g1-A) 합의 Reviewer 단독 격상 R-S3 답습 영구 위반. 🔴 **2+ Agent 일치 BLOCKING 4**: R-1 (A-B2 + B-B4) ADR-008 framing + verbatim 인용 부재 / R-2 (B-B5 + B-S4) "우선한다" 본 cycle 범위 초과 / R-8 (A-S1 + C-B3) 본문 후보 4→7 확장 ((v)(vi)(vii) 신규) / R-9 (A-S2 + C-B4) 위치 후보 3→4 확장 ((d) ADR 신설 우회). 🔴 **3-way 일치 BLOCKING 1**: R-5 (A-S3 + B-B7 + B-S3) §0 ↔ §10.1 비대칭. 🔴 **Reviewer 권한 한계 7 → 8 항목 격상** (R-7 답습 신규): (8) 결합 cycle 진입 자격 평가 자격 0 — (g1-N) 단독 vs (g1-O) 단독 vs (g1-N+O) 결합 3 형태 합의 input 자격 평가 only. **권고 17 (R-23~R-39)** + **NOTE 54 (29 carry-over + 본 cycle 신규 25 N-30~N-54)**. **본 cycle 자체 진행**: 측정·빌드·다운로드·설치·sudo·M3·M4 결정 고정·runtime backend 코드·헌법·ADR-011·ADR-008·MVP-1·메모리 본문 자동 정정·Provider Liquidity 본질 약화·4 가족 분류 + 6축 framing 영구 정착·(g1-N) 자체 영구화 정착·자동 채택/자동 기각·결합 cycle 자동 진입 모두 0건. **다음 세션 (사용자 명시 — 자동 진입 0건)**: (g1-N) 채택 후 별도 단계 (g1-N-1) 실 헌법 본문 변경 commit (**trigger 정확한 form R-19 답습 — 사용자 명시 + (g1-N-1) entry brief v1 별도 작성 + 사용자 명시 + (g1-N-1) entry brief v1.1 보강 + PROJECT_CONSTITUTION.md 본문 변경 commit 동시**) / (g1-N-2) ADR-011 매핑 정정 = (g1-O) cycle / (g1-N-3) CLAUDE.md + roadmap 답습 / (gN-D1) (g1-N) 기각 / (gN-D2) DEFER / (g1-O) 단독 / (g1-N+O) 결합 cycle / (g1-A) carry-over + (f-) + Phase 3 (g)~(n). ▼ **이전 5차 정리 시점 핵심 (carry-over)**: **(g1-A) 채택 cycle 합의 BLOCKING 16 핵심**: 🔴 **Reviewer 단독 격상 3 (raw line-level direct cross-check)** — ⭐⭐⭐ **R-S1 (C-S4 격상, 가장 큰 finding)**: 메모리 `feedback_provider_liquidity` 실제 line 14 verbatim = "단일 provider 의존 시스템 금지 — **최소 2 provider always-on 원칙**". 본 (g1-A) brief v1 line 169 §3.3 + 선행 format brief v1.1 §3.4 + format 합의 보고서 R-13 모두 "line 13 '최소 2 provider always-on'" 인용 = line offset 부정합 chain. 정정 chain carry-over 의무 (선행 brief + format 합의 R-13 정정은 별도 cycle). / ⭐⭐ **R-S2 (B-B1 + B-S1 격상)**: 헌법 5조 line 40~46 verbatim = "**제5조: 코드 품질 원칙**" + 5 항목 (Provider Liquidity 직접 본문 부재). ADR-011 line 6/245 *매핑* 의존. format 합의 R-S2 (ADR-011 *내부* 비대칭) 의 **상위 단계 비대칭**. Reviewer 권한 한계 (헌법 본문 정정 자격 0) 답습 = 매핑 자격 인정 only + 별도 cycle (g1-N) 의무 명문. / ⭐⭐ **R-S3 (B-B8 격상)**: §0 #12 NOTE 합산 오류. format 합의 NOTE 24 = Provider Liquidity 12 *내포 합산*. 정확 = format 24 (Provider Liquidity 12 내포) + Phase 3 NOTE 11 = **35 비중복 항목**. 🔴 **2+ Agent 일치 BLOCKING 2**: R-1 (A-B1 + B-B2 + C-B1 **3-way 일치**) (g1-A) 추가 산출 boundary 모호·자명성·재서술 self-위반 risk / R-2 (A-B2 + C-B2) §7 매트릭스 비대칭 + (g1-N)/(g1-O) 권위 본문 미세 보강 옵션 누락. 🔴 **Agent 단독 BLOCKING 11**: R-4 boundary 결정 자격 0 명문 부재 (B-B3) / R-5 메모리 stale "19일+" → "20일" + line offset 균질화 (B-B4) / R-6 (g1-A) 영구화 risk 차단 메커니즘 layer (iv) 추가 (B-B5) / R-7 Reviewer 권한 한계 7 항목 재서술 vs by-reference boundary (B-B6) / R-8 "자동 (기본값)" R-30 답습 + 차단 발효 vs 다음 단계 진입 boundary (B-B7 + A-S4 + C-S2 통합) / R-10 §11 변경 일람 표 본문 의무 분리 (A-B3) / R-11 §6.2 source 본 brief 자체 부재 (A-B4) / R-12 §10 NOTE 형식 분기 미명문 (C-B3) / R-14 자기-부정 risk + 권위 chain 등재 risk 통합 (B-S5 + C-S1) / R-15 Phase 3 R-5 ↔ (g1-A) 동형 boundary (A-S2) / R-16 §0 #2 (ii) 6축 framing 이중 의미 (A-S3). **권고 18 (R-17~R-34)** + **NOTE 35 비중복 carry-over + 본 cycle 신규 5 = 40 by-reference only**. **3 Agent 정합성 evidence**: APPROVE w/ COND 3-way 일치, 정면 충돌 0건. **본 cycle 자체 진행**: 측정·빌드·다운로드·설치·sudo·M3·M4 결정 고정·OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss 코드·메모리·헌법·MVP-1·ADR-011 본문 자동 정정·Provider Liquidity 본질 약화·4 가족 분류 + 6축 framing 영구 정착·(g1-A) 자체 영구화 정착·자동 채택/자동 기각 모두 0건. **다음 세션 (사용자 명시 — 자동 진입 0건)**: brief v1.1 §7.1 후속 옵션 (g1-B/C/D3/D4/E/F~M/**N/O**) + (f-) carry-over + Phase 3 carry-over (g)~(n) 중 선택. **(g1-N)/(g1-O) ⭐ 신규 옵션** = 헌법 5조 / ADR-011 line 212 본문 미세 보강 (R-9 헌법급 변경, 별도 cycle). 모든 옵션 자동 진입 0건, 단계별 명시 의무 답습. ▼ **이전 4차 정리 시점 핵심 (carry-over)**: **format 가족별 분류 cycle 합의 BLOCKING 16 핵심**: 🔴 **Reviewer 단독 격상 3건** — **R-S1 (A-S1 격상)**: Phase 3 raw `2026-05-24T04-32-phase3-measure-attempt-blocked.log` line 25~32 결론 verbatim cross-check → "Ollama 다운로드 GGUF = 더 오래된 conversion (`.ssm_dt.bias` 미저장) + llama.cpp `c0c7e147` master = `.dt_bias` → `.dt_proj.bias` rename + `.bias` flag=0 required 강제" → P3-F1 = **시점 부정합** finding 확정 (≠ "GGUF 가족 본질 부정"). 가족 본질 부정 자격 = 다른 conversion lineage + 다른 sub-차원 + 다른 시점 측정 3 차원 모두 충족 후 도래. / **R-S2 (C-B3 격상)**: ADR-011 line 6 + line 212 + line 245 verbatim 직접 cross-check → ADR-011 *내부* 비대칭 (line 6/245 = 권위 위계 의존 / line 212 = 주제 범위 한정). 본 cycle 답습 의무 = 두 차원 모두 명문. ADR-011 *내부* line 212 본문 정정 자격 0. / **R-S3 (B-S5 ⭐⭐ 격상)**: brief v1 §0 "하지 않는 것" 12 항목 vs §9.1 차단 6 항목 1:1 매핑 부재 = brief self-consistency 약화 정직성 risk. 🔴 **2 Agent 일치 BLOCKING 3**: R-1 분류 *기준* (분류 축) 단일축 명시 부재 — ktransformers "부분" fuzzy membership 시사 (A-B1 + C-B1 + C-S1) / R-2 self-citation anchor risk 후속 cycle 답습 매핑 부재 (B-B4 + C-S4) / R-3 Phase 3 합의 R-5 (framing 약화) 답습 의무 명시 누락 (B-B6 + C-R5). 🔴 **Agent 단독 BLOCKING 10**: R-4 §4.3 (α) 본질 약화 risk 차단 (B-B1) / R-5 ADR-011 §2.1 "(a)~(d) 4조건" vs brief "(a)~(e) 5조건" carry-over (B-B2) / R-6 MVP-1 R4 해석 명확화 vs 본문 정정 boundary (B-B3) / R-7 abstraction layer 교차 자격 + 차원 폭발 (C-B2 + C-S2) / R-9 가족 내부 호환성 수학적 표현 (A-B3) / R-11 framing β'~ε' 비교표 (C-B4) / R-12 중첩 후보 처리 5 자격 (C-B5) / R-13 메모리 line 13 "최소 2 provider always-on" 인용 부재 (B-B5) / R-14 Reviewer 권한 한계 7 항목 boundary (B-B7) / R-16 진단 의무 enum (B-S6). **권고 21 (R-17~R-37)** + **NOTE 24 (Provider Liquidity 합의 12 + 본 cycle 신규 12)**. **본 cycle 자체 진행**: 측정·빌드·다운로드·설치 0건 / sudo 0회 / M3·M4 결정 고정 0건 / runtime backend 코드 0건 / 메모리·헌법·MVP-1 합의·ADR-011 본문 자동 정정 0건 / Provider Liquidity 본질 약화 0건 (binary 본질 유지, spectrum 화는 framing 도구 한정) / 4 가족 분류 영구 framing 정착 0건 (R-12 답습) / 보안 거버넌스 자동 재개 0. **다음 세션 (사용자 명시 — 자동 진입 0건)**: format 가족별 분류 cycle brief v1.1 §7 옵션 (A)~(M) + DEFER (D1)~(D4) 중 선택 또는 carry-over 옵션 (f-A·f-C·f-D3·f-D4·f-E·f-F + Phase 3 carry-over g~n). 모든 옵션 자동 진입 0건, 단계별 명시 의무 답습. ▼ **이전 세션 핵심 (3차 정리 시점, carry-over)**: SESSION_05-23 미포함 carry-over 3 commit + 본 세션 1차(Phase 3 합의 + brief v1.1) + ⭐ 2차(Phase 3 실 빌드 cycle) + ⭐ **3차 (Provider Liquidity deep-dive cycle)** 통합. **Provider Liquidity 합의 BLOCKING 13 핵심**: 🔴 **R-13 ⭐ Reviewer 단독 (가장 강한 reframing)** — ADR-011 line 6 verbatim `**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), ...` + line 245 verbatim `제5조 **관용** (Provider Liquidity, 비협상)` 직접 권위 매핑 발견 → brief §1.4 "헌법 5조 = 동형 해석" 진단 = ADR-011 *해석 권위* 비참조 = **부정확**. 헌법 본문 (5조 = 코드 품질) 외 ADR-011 의 "관용 매핑" 정착. / 🔴 **R-3 ⭐ 3 에이전트 일치** — 4 수준 framing self-citation anchor (ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재) + **시간축 missing dimension** (P3-F1 evidence 강도 = 특정 시점 변환 GGUF `30e51a7c` vs 특정 시점 llama.cpp `c0c7e147` 시간 의존 호환성 그라데이션) + 비교 자격 1/4 (4 수준 중 model loading sub-차원 (1) 만 양쪽 측정·자격 충족). / 🔴 **R-7** — model loading 5 sub-차원 (tensor naming / MoE routing / tokenizer / chat template / quantization) 분해. / 🔴 **R-11** — evidence GGUF 가족 한정 (다른 format 가족 입력 자격 0). / 🔴 **R-4 (A-S1)** — case A/B 양자택일 → case C (means + ends 양면) 분기. / 🔴 **R-9** — ADR-011 amendment 옵션화 = 헌법급 변경 본문 권위 간접 압력 (사용자 명시 + 풀 3+1 + Reviewer 권한 한계 답습 별도 cycle 의무). / 🔴 **R-12** — §7 옵션 (D) cycle-specific framing 영구화 risk, (D3)(D4) 분기 추가. **권고 17 (R-14~R-30)**: ADR-011 §2.1 (a)~(d) + (e) 후속 패턴 정합화 / 헌법 5조 "내부 신뢰" 추가 / ADR-011 line 245 verbatim / R4 verbatim / P3-F1 3-source cross-validation / 진단 의무 enum 5 / 메모리 19일 stale / Reviewer 권한 한계 강화 / Phase 3 BLOCKING 7 답습 의무 / raw line-level cross-check / format 가족별 분류 / ADR-008 부록 B Amendment 패턴 / de facto 압력·자동 기각 차단. **NOTE 12 (N-1~N-12)** carry-over. **3 에이전트 전원 기각 0건, 정면 충돌 0건 = 강한 정합성 evidence**. **본 cycle 자체 진행**: 측정·빌드·다운로드·설치 0건 / sudo 0회 / M3·M4 결정 고정 0 / OllamaBoss·LlamaCppBoss 코드 0 / 메모리·헌법·MVP-1 합의·ADR-011 본문 자동 정정 0 / Provider Liquidity 본질 약화 0 (binary 본질 유지, spectrum 화는 framing 도구 한정) / 보안 거버넌스 자동 재개 0. **다음 세션 (사용자 명시 — f 진입 예정)**: brief v1.1 §7 옵션 (A)~(M) 중 선택. 핵심 후보 = (f-A) MVP-1 합의 R4 진술 수준 분리 보강 / (f-C) 헌법 5조 + ADR-011 line 6/245 관용 매핑 권위 답습 명문 / (f-D3) framing 비교 본문 포함 ADR / (f-D4) ADR DEFER + MVP-1 합의 보강만 / (f-K) format 가족별 분류 cycle / (f-E)/(f-F) ADR-011 amendment cycle (헌법급, 별도 합의). / **Phase 3 carry-over**: ⭐ Phase 3 실 빌드 cycle 핵심 발견 7 (Provider Liquidity 강화 / sm_120a+sm_121a SASS 모두 포함 / R-1 anchor 8회 일치 / Phase 1 prompt detokenize / Ollama API FROM 경로 부정확 / docker-proxy 11434 / OLLAMA_KEEP_ALIVE=-1). Phase 3 합의 BLOCKING 7 답습 유지. **Phase 3 합의 BLOCKING 7**: R-1 Qwen3-Next verify 강화 / R-2 repo URL `ggml-org` canonical(A-S1 ⭐) / R-3 R-1 mid-cycle anchor + window bias(B-S1 ⭐) / R-4 분기점 라벨 anchor effect 제거 / R-5 #6 framing 약화 + Qwen3-30B-A3B 대조군(C-S1 ⭐) / R-6 compute_cap 실측 + cuobjdump sm_121 SASS verify / R-7 빌드 egress 사전 차단. **⭐ Phase 3 실 빌드 cycle 핵심 발견**: (1) 🎯 **Provider Liquidity 강화** — Ollama 보유 GGUF (오래된 conversion, `.ssm_dt` only) ≠ llama.cpp `c0c7e147` master 요구 format (`.ssm_dt.bias` flag=0 required). 모델 교체 = GGUF 변환 호환성 비협상 의무 (헌법 5조 함의). (iii)(iv) 직접 측정 차단 → 본 finding 자체가 강한 evidence. (2) 🎯 **sm_120a + sm_121a SASS 모두 포함** verbatim (cuobjdump libggml-cuda.so.0.12.0 102MB) — 가설 #6 sm_120/121 미지원 *후보 약화*. (3) 🎯 **R-1 anchor 누계 8회 일치 확정** (Phase 1 5회 + Phase 3 시작/mid/end 3회). (4) 🎯 **Phase 1 prompt 정확 detokenize** (GGUFReader + GPT-2 ByteLevel + Qwen3 chat template) — 4종 prompt text 파일 보존 (Phase 3.5/4 답습 자격). (5) 🟡 Ollama API `/api/show` FROM 경로 부정확 (`/root/.ollama/` stale → 실제 `/home/delangi/.../bootcamp_game/ollama-data/`). (6) 🟡 Port 11434 listening = docker-proxy (pid 4218, Ollama Docker wrapper 가능성). (7) 🟡 OLLAMA_KEEP_ALIVE=-1 무한 (`/api/generate` keep_alive: 0 명시 unload 의무). **Phase 3 종합**: 빌드 4.6분 100% (예상 30분-2시간 대비 8-30× 빠름) / 측정 0건 / (iii)(iv) 차단 / 가설 #6 약화 / R-1 8회 일치 / raw 17 파일. **다음(자동 진입 0건)**: (a) Phase 3 cycle commit + push / (b) Phase 3.5 brief (new GGUF HF community ~50GB) / (c) Phase 3.5 brief (Qwen3-30B-A3B 대조군) / (d) **Provider Liquidity finding deep-dive 합의 cycle** / (e) llama.cpp 이전 commit checkout / (f) B hybrid prebuilt fallback / (g) advisory wall-clock 측정 / (h) M3·M4 결정 고정 합의 (Phase 1+2+3 부분) / (i) MVP-1 트랙 B / (j) §12 옵션 E (R-1 8회 evidence 약화) / (k) brief v1.2 보강 (Phase 3 finding 반영) / (l) 다른 inference engine 외부 식별. 본 세션 2차 자체 진행: ccache + numpy 신규 설치 (사용자 명시) / llama.cpp 빌드 (sudo 0) / sudo ~6회 사용자 명시 (read-only) / 측정 시도 (즉시 차단) / Ollama runner unload (`keep_alive: 0`) / M3·M4 결정 고정 0 / OllamaBoss·LlamaCppBoss 코드 0 / 보안 거버넌스 자동 재개 0.
docs/CONTEXT.md:25:6. **⭐⭐ 비례성 DEFER** (사용자 제기·명시): solo 개인 개발 툴엔 하드웨어 서명·touch-per-commit **비례 초과**(위협=에이전트 실수+공급망=review/test/git로 충분, "내 머신 root 공격자"=한계이득 0). means/ends(ADR-011): 하드웨어 서명=MEANS, 현 비용>이득. **서명 격리 발효 DEFER, 청사진 commit 보존, 서명 생략.**
docs/CONTEXT.md:40:**이전 후속 73 상세** (참고용 보존): 2026-05-21 새 세션 후속 73 (**BI-4 GitHub plan·ruleset 가용성 brief 전체 cycle + push**). HEAD = 메타 commit (origin push 발효 — 직전 보류 5 commit + 후속 73 신규 3 = **총 8 commit push**). 후속 73 산출 = brief v1 작성 → **(B) repo public/private 사실 확인**(비인증 API: `jokwangwon/AI_development_tool` = **`public` 확정**, personal account) → brief v2(plan worst-case 소거, 쟁점 self-bypass/token 이동) → **(A) BI-4 검증 풀 3+1 합의** (`bb661f0`, **APPROVE WITH CONDITIONS**, BLOCKING 5 BI4C-1~5 + 권고 6 BI4R-1~6, 교차 일치3/부분4/불일치0/누락7) → brief v3(`9492193`, BLOCKING 반영) → 메타 → push. **⭐ BLOCKING 5**: **BI4C-1** §11.3 citation stale("G3 §5.5"=SPOF Accepted Risk 오지목·문구 0건 → `f29c772` line 118 + BI-7, **후속 72 N-2 동형**, Reviewer grep 확정) / **BI4C-2 ⭐거짓안전감 핵심** = BI-3 CD-5("수단 라벨 ≠ 입증, 적대적 침투시연 binary")를 anchor 에 대칭 미적용 → "anchor observe=binary" 종료 조건 명문(token→ruleset off 실패 / `--no-verify`→server reject / origin replace→audit alert, enforcement status 라벨 ≠ 충족, ADR-011 §2.1(b) 동형) / **BI4C-3** CI required check = *merge* 게이트 → **직접 push(PR 미경유) 우회** gap → restrict direct push 결합 전제 + gate G-BI4-6 / **BI4C-4 ⚠️현존 노출** = 개인 이메일 `<redacted>` 이 public repo `docs/review/3plus1-consensus-2026-05-13-{mvp1-pass-c1-k2,adr-012-event-enum,k2-permissions}.md` 3파일에 plaintext commit (Reviewer grep 확정) → entry 선결 점검 격상(gate G-BI4-7, redaction = git history rewrite 별도 단계) / **BI4C-5** Sigstore Rekor transparency log(제3자 append-only = self-bypass·origin replace 구조적 강함)을 §3.1 anchor 후보표 (E) 행 병치(채택 아님, BI-3 §4 M5 대칭). **권고 6**: BI4R-1 plan 표 entry 재확인 / BI4R-2 anchor 집행(vendor)⊕신뢰기준(`allowed_signers` 중립) 분리(BI-3 cross-ref 답습) / BI4R-3 anchor 2층(기준×집행) 직교 추상화 + GitHub App token / BI4R-4 self-bypass 재귀 닫힘+origin replace↔CBI-2+Rollback Trigger+workflow yaml 우회 / BI4R-5 외부 미러 cross-check / BI4R-6 제목 v1→v3 정합. **public 확정 함의**: ruleset = 모든 plan(Free 포함) 가용 → plan worst-case(private+Free) 소거, 쟁점 = **self-bypass(1인=repo owner=ruleset off 가능)+token 분리**로 이동. **부수: Obsidian 도입 질의** → 개인 vault(repo 밖) = 프로젝트 영향 0건·결정 절차 불필요(즉시 가능) / docs 관리 scope = tmux 선례대로 별도 brief 권장(soft lock-in 경계). **신규 합의 누적 36 → 37**(73 +1). **⭐ 다음 세션 추천 (사용자 명시, 자동 진입 0건)**: (1) **BI4C-4 redaction** (개인 이메일 public 노출 정리 — git history rewrite 얽힘) / (2) 다른 BLOCKING 심화(BI-1 CI fingerprint / BI-5 audit) / (3) credential 수단 *발효*(BI-3 후속, host OS 확인 후) / (4) 세션 종료. **금지 유지 (영구 답습, 모두 0건)**: GitHub ruleset·branch protection·CI·bypass 실 변경 / plan 업그레이드·org 전환·GHES 도입 결정 / anchor·credential token 실 분리 / audit sink 구현 / 수단 결정 고정 / sigstore·Rekor 실 도입 / Vault ST-4 / Operational Readiness PASS / Hermes PMO 격상 / 원 합의 본문(`f29c772`) 자동 정정 / Obsidian docs-scope 도입 결정.
docs/CONTEXT.md:54:**이전 후속 65 상세** (참고용 보존): 2026-05-20 후속 65 (**⭐ G3 line 448/784 metadata-기반 single-author detection 결함 교정 풀 3+1 합의 *완료* — brief 작성 + commit + Agent A/B/C 병렬 독립 + Reviewer 교차 비교 + 합의 보고서 파일화 + commit + 메타 갱신 + push**). 본 새 세션 산출 = **3 commit**: (1) `afb92de docs(phase0): add G3 metadata detection defect correction brief` (`docs/phase0/g3-line448-784-metadata-detection-defect-correction-brief.md`, 293줄, DRAFT v1) / (2) `92d74be docs(review): G3 metadata detection defect correction full 3+1 consensus APPROVE WITH CONDITIONS` (`docs/review/3plus1-consensus-2026-05-20-g3-metadata-detection-defect-correction.md`, 190줄) / (3) 본 commit (메타 갱신). **사용자 명시 cycle 답습**: brief 작성 → (A) 승인 → brief commit → 풀 3+1 합의 보고서 → 메타 갱신 → push (brief → 승인 → 합의 → commit → push). **합의 판정**: **APPROVE WITH CONDITIONS** — Group I 합의에서 발견·기록된 G3 본문 결함(line 448 "author/committer + audit log cross-reference" / line 784 "auto-reject §2.2 #20 의 *기준* 자체가 단일 author 비교")을 교정 *방향* 승인 + 9+1 조건. 단 Agent A·B 일치 = **"단순 텍스트 정정"이 아니라 §2.2 #20 auto-reject *판정 기준 변경* = T3 (R-I-CONFIG-CHANGE)** → Reviewer-only 부적격. **교정 방향 (만장일치)**: positive allow-list ⊕ credential boundary (allow-list 의 *선결 전제*) ⊕ external enforcement (runtime=sensor / 최종 reject=Hermes 밖 anchor) ⊕ **audit sink integrity** (G2 — Agent C 가 line 448 "audit log cross-reference" 직결로 사실상 4번째 축 격상). **9+1 조건 CN-1~CN-10** (CN-1 positive allow-list 중심 / CN-2 credential boundary 본문 명시 [누락 시 metadata 보다 위험한 거짓 안전감] / CN-3 runtime=sensor·최종 reject=Hermes 밖 / CN-4 host 밖 실 anchor + detection 설정 변경=R-I-CONFIG-CHANGE T3 / CN-5 `.git/`=filesystem ACL 책무 commit detection 범위 밖 명시 / CN-6 수단 본문 고정 금지 [후보 열거 허용] / CN-7 audit sink integrity 별개 요소 / CN-8 author 메타 "판정 경로 제외·audit 보조 전용" 비대칭 / CN-9 observe≠발효·FN 우선 / **CN-10 framing — G3 채널명 재명명 옵션 개방** [detection→"provenance sensor" 역할 어휘 = means 고정 아님, brief 의 Group I N1 무비판 답습 *수정*]). **교차 비교**: 일치 8 / 부분 2 / 누락 5 / 불일치 2 (D1 framing / D2 수단 표기). **⭐ 핵심 교차 발견**: Agent C = **brief touch-point 표 누락 line 457 (§3.1.3 차단표) 발견** + audit sink = 4번째 축 + framing N2'(채널명 재명명) 우월 / Agent A = **line 230(signed commit ADR-012 후보)·805(GPG signed commit 강제) = 이미 positive 서명 방향 내부 선례** → 결함 정체 = "G3 가 multi-host/Evidence Ledger 에선 positive 서명을 알면서 single-host commit detection 에서만 metadata 비교에 머문 비대칭" + 448/784만 고치면 360/1122 가정 잔존 → 본문 내부 불일치 / Agent B = HIGH 구조적 결함(수용된 약점→enforcement 권위 승격 모순) + 5 BLOCKING. **교정 범위 (검토만, 실 수정 0건)**: 1차 4줄 (448/784/457/648) + 가정 잔존 교정 2줄 (360/1122) + 정합 참조만 2줄 (230/805). **형태 권고**: brief §5.3 "본문 반영 한정 합의 + 4 결정 항목(문구·범위·author 어휘·채널명) scope 명문 고정" (식별 frame 은 Group I `f6c6d5a` 만장일치 확정 → 풀 3+1 frame 재투표 중복 제거). **신규 합의 1건** (30 → 31). **합의 = 추론적 검증(권고) 한정** — G3 본문 *문구* 확정·실 수정·채널명·수단 후보·실 구현 = 사용자 명시 + 별도 단계 (본문 교정 단계 R-I-CONFIG-CHANGE T3 + Backlog #6 Runtime + CI-hook). **사용자 명시 금지 영구 답습 (모두 0건)**: G3 본문 실제 수정 (line 448/784/457/648/360/1122/230/805) / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Hermes runtime 변경 / Hermes upstream 변경 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / 수단 결정 고정 / threshold 고정 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화. **MVP-0 ✅ / MVP-1 진입 4/5 / Phase α defer-lockdown 영향 0건**. **⭐ 다음 단계 (사용자 결정 영역 — 자동 진입 0건)**: (1) **G3 본문 교정 patch brief** (line 448/784/457/648/360/1122 *문구* 교정안, R-I-CONFIG-CHANGE T3) / (2) G3 touch-point별 수정안 작성 / (3) **Group I implementation boundary brief** (Backlog #6 Runtime + CI-hook 연결, R-I-IMPL-BOUNDARY) / (4) 다른 backlog 전환 (Hermes PR·approval auto-reject G1 / Group I 2차 vendor / GP-5 C-2 = facade real P1 v2 Backlog #4) / (5) 세션 종료.
docs/CONTEXT.md:56:**이전 후속 64 상세** (참고용 보존): 2026-05-20 후속 64 (**⭐ Group I (Hermes-originated commit auto-reject) 풀 3+1 합의 *완료* — 외부 GPT-5.5 응답 회수 + brief v2 보강 + Agent A/B/C 병렬 독립 + Reviewer 교차 비교 + 합의 보고서 파일화 + commit + push**). 본 새 세션 산출 = **2 commit**: (1) `f6c6d5a docs(review): Group I Hermes-originated commit autoreject full 3+1 consensus` (3 files, +543/−15 — 외부 응답 기록 `docs/external-review/2026-05-20-...-review-response-gpt.md` + brief v2 보강 + 합의 보고서 `docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md`) / (2) 본 commit (메타 갱신). **사용자 명시 cycle 답습**: 외부 응답 paste → (응답 기록 + brief v2 보강 후 재승인) → (A) brief v2 승인 → 풀 3+1 합의 진입 → (합의 보고서 파일화 + commit) → push → 세션 종료 프로토콜 → 메타 commit → push → 세션 종료. **합의 판정**: **Group I = T3 보안 enforcement 영역 → 풀 3+1 (Agent A/B/C + Reviewer) *의무*, Reviewer-only 단축 *부적격* (만장일치)** (trigger #2 T3 BLOCKING + #5 핵심 제약 #1 *Hermes ≠ root of trust* / #4 단일 source-of-truth 직결 + #7 외부 GPT-5.5 1건 회수로 충족 + §4 self-reference 구조). **외부 GPT-5.5 5 보강점 5/5 채택** (positive allow-list·runtime=sensor·`.git/`=filesystem ACL 책무 = BLOCKING / GHES pre-receive ≠ GitHub.com 기본 = 채택 / FP통제 observe·quarantine = 조건부). **BLOCKING 6**: B-1 식별 = metadata negative detection 아닌 **positive allow-list** (사람 전용 hardware-backed key 서명, author/committer/trailer = 참고 신호 한정) / B-2 **runtime = sensor·audit producer 한정, 최종 reject = Hermes 밖** (external enforcement = ruleset / container ACL / hardware key) / B-3 **credential/process boundary 실분리가 전제** (동일 credential 공유 시 FN > FP 위험) / B-4 **host 밖 anchor 최소 1개 의무** (single-host 3-layer 명목화 방지) / B-5 **R-I-CONFIG-CHANGE = T3** (Hermes는 ruleset/CI/audit 수정 token 미보유) / B-6 **`.git/` 직접 변조 = filesystem ACL(§2.5 #1) 책무** (commit layer 사각). **조건부 3**: CB-1 observe mode ≠ enforcement 발효·FN 우선 / CB-2 **negative-control-only** (PASS = positive evidence 오용 금지) / CB-3 **framing = N1 (명칭 유지 + 중심 명제 명시)** — 외부 제안 명칭 "Human-authorized T3 change enforcement with Hermes credential isolation" 은 *수단(credential isolation)* 을 명칭에 고정 → ADR-011 §2.1 means/ends 저촉 → 전면 재정의 *보류*, 중심 명제 ("credential boundary + external enforcement + audit 결합, metadata 판별기 아님") 만 명시 권고. **⭐ 핵심 발견**: Agent A·B 독립 + Reviewer 원문 검증 = **현 G3 본문 line 448 ("author/committer + audit log cross-reference") / line 784 ("기준 자체가 단일 author 비교") 가 정확히 외부가 약하다고 지적한 metadata 기반 single-author negative detection 을 명시** → positive allow-list 권고는 신규 제안이 아니라 *현 G3 설계 결함 교정*. 단 G3 본문 교정은 별도 단계로 분리 (brief 금지 G3 본문 변경 0건과 양립 — 결함은 합의 권고로 *기록만*). **신규 합의 1건 (Group I 풀 3+1, 29 → 30 합의)** — 권위 조건 = 6 BLOCKING + 3 조건부 (14 일치 / 1 불일치 D1 / 6 Gap). **합의 = 추론적 검증(권고) 한정** — 식별 방법·차단 지점·framing·G3 본문 교정의 실 *결정/구현* = 사용자 명시 + 별도 단계 (Backlog #6 Runtime + CI-hook 연결). **사용자 명시 금지 영구 답습 (모두 0건)**: G3 본문 교정 자동 진입 / Hermes-originated commit 차단 구현 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Hermes runtime 변경 / Hermes upstream 변경 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / 수단 결정 / threshold 고정 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 / Group α·β·γ-1·γ-2 합의 본문 변경 / Hermes PR·approval auto-reject 신규 단위 자동 진입 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화. **MVP-0 ✅ / MVP-1 진입 4/5 / Phase α defer-lockdown 영향 0건**. **⭐ 미해소 쟁점 (자동 진입 0건)**: (1) **G3 line 448/784 metadata 기반 single-author detection 결함 교정 필요** (별도 G3 개정 단위, T3 풀 3+1 + 사용자 명시) / (2) **Hermes PR·approval auto-reject 신규 단위 G1 분리 필요** (Group α C-2 직표적 = commit 아닌 approval — Group α 결합 vs 신규 단위 사용자 결정) / (3) **Group I 2차 vendor (Gemini 등) 입력 가능성** (trigger #7 1건 충족, 추가 입력 바람직하나 의무 아님) / (4) **GP-5 C-2 완전 해소 trigger = facade real 본문 P1 v2 (Backlog #4) 연결**. **다음 세션 추천 시작점 (사용자 명시)**: G3 line 448/784 metadata 기반 single-author detection 결함 교정 brief 작성 — Group I 합의 발견 G3 본문 결함을 positive allow-list / credential boundary / external enforcement 중심으로 교정 가능한지 *검토* (G3 본문 수정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 = 0건).
docs/CONTEXT.md:88:**이전 후속 26 상세** (참고용 보존): 2026-05-17 후속 26 (**Phase α-4 R-1 *실 진입 여부* brief (Stage 3 framing) + Reviewer-only 단축 합의 APPROVE AS BRIEF (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("1 번 작업으로 진행" → "Stage 3 실 진입 여부 brief 작성 (DRAFT — 5 금지 모두 보존)" → "옵션 (A)로 진행 — brief 그대로 승인 → brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 CI workflow 통합은 아직 하지 않음."). **3 commit chain**: (1) `27351ce docs(phase0): add Phase alpha-4 R1 actual entry decision brief` (722줄, 13 섹션 — DRAFT — `docs/phase0/phase-alpha-4-r1-actual-entry-decision-brief.md`) / (2) `d3f6d59 docs(review): approve Phase alpha-4 R1 actual entry decision brief` (540줄, 13 섹션 — Reviewer-only 단축 합의 APPROVE AS BRIEF + 36 합의 조건 C-τ-1~C-τ-36 — `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-actual-entry-decision.md`) / (3) 메타 commit (본 commit). **핵심 framing**: Phase α-4 R-1 LVE 합의 (`b264580`, 31 조건 C-σ) 발효 후속 Phase α-4 Stage 3 (R-1 CI workflow 통합 *실 진입* (Stage 4) *여부 검토 영역*) 한정 — Step Division §1.3 답습 명시한 Stage 3 framing ("*Should* we enter Phase α-4 R-1 actual implementation (Stage 4) now?"). **사용자 명시 5 금지 위반 영구 답습**: CI workflow 변경 0건 / runtime code 변경 0건 / actual run 재실행 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건. **R-1 영역 현재 상태**: 7 artifacts × 1593줄 본문 = 이미 구현 완료 + 4 prerequisite runs 4/4 SUCCESS + local 51/51 PASS + α-1+2+3 evidence 12/12 PASS = **technical pre-conditions 모두 충족**. **Stage 4 작업 후보 W-1~W-10 enumerate 채택**: W-1 (3 MVP-1 workflow 본문 step 추가/수정) + W-2 (integration tool 본문 step 추가/수정) + W-3 (3 fixture 본문 추가/수정) + W-4 (신규 actual GitHub Actions run trigger) + W-5 (permissions 보강) + W-6 (Required check) + W-7 (PC-4 pre-commit) + W-8 (AR-2 branch protection) + W-9 (AR-3 revert bot) + W-10 (Stage 5 G3-7). **Stage 4 최소 영역 권고 채택**: W-1~W-4 한정 (5 금지 #1 + #3 해소). **Stage 4 최대 영역 *비*권고 채택**: W-5~W-10 (영역 경계 불명확 → T-10+T-13+T-6 발화 → 풀 3+1 + 외부 LLM 1+ + 인간 리뷰 의무 필요). **5 금지 해소 매트릭스 (실 진입 시점 권고)**: #1 (CI workflow 변경) + #3 (actual run 재실행) 해소 필수 + #2 (runtime code) + #4 (Operational Readiness PASS) + #5 (Hermes PMO 격상) 영구 보존 — **본 합의 시점 0/5 해소 영구 답습**. **Pro 9 (technical readiness P-1~P-9: R-1 본문 + α-1+2+3 evidence + Stage 4 합의 + ADR-011 + 5 진입 적격성 + Step Division + 353 합의 조건 + 5 영구 핵심 제약 + Provider Liquidity) / Con 9 (governance + 5 금지 해소 + human review risk C-1~C-9)** 균형 분석. **Rollback Trigger 28 (Layer B 18 + TR-1~TR-5 + Step Division 신규 후보 5) × 본 합의 시점 0/28 발화 영구 답습 + Stage 4 W-1+W-2 시 5 발화 가능성** (신중 영역). **합의 형태 권고**: 본 합의 자체 = (a) Reviewer-only 단축 합의 적격 (16/16 풀 3+1 트리거 0건 발화) / Stage 4 시점 = W-1~W-4 풀 3+1 합의 (필수) / W-5~W-10 풀 3+1 + 외부 LLM 1+ blind 의뢰 + 인간 리뷰 의무. **R-1 영역 7 artifacts × 1593줄 본문 변경 0건** + **R-4/R-5/R-7 1192줄 변경 0건** + **`src/` 변경 0건** + **α-1+2+3 evidence (`7b3d40a`) + LVE (`4ce5a0b`+`b264580`) + Step Division (`52a05cb`) + α-4 진입 조건 점검 (`1c365e7`) + 직전 α-4 (`e59a565`) 본문 변경 0건** + **PC-4/AR-2/AR-3/Stage 5 진입 0건** + **Layer C/D 재발효/재선언 0건** + **MVP-1 PASS 재선언 0건** + **branch protection 변경 0건 + dev 환경 강제 0건 + `pre-commit install` 의무화 0건** + **신규 workflow 신설 0건 + `pull_request_target` 도입 0건** + **GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)** + **Hermes upstream Dockerfile 변경 0건**. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **합산 353 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31) + **본 합의 36 신규 조건 (C-τ-1~C-τ-36)**. **본 brief + 본 합의 ≠ Phase α-4 Stage 4 (실 구현) 자동 진입 / W-1~W-10 작업 실 발효 / CI workflow 변경 / 신규 actual run trigger / 실 진입 여부 결정 최종 확정** — 실 진입 여부 권위 권고 한정. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-4 Stage 4 진입 brief 작성 — W-1~W-4 최소 영역 한정 (풀 3+1 합의 필수, 외부 LLM 1+ 없이) (**권고 시작점**) / (2) Stage 4 진입 brief — W-1~W-10 최대 영역 (풀 3+1 + 외부 LLM 1+ + 인간 리뷰 의무) / (3) Backlog #1 / (4) Backlog #3 (T3) / (5) Phase α-1~α-4 통합 구현 완료 조건 재평가 / (6) Group α 조건 재평가 / (7) Layer C/D 후속 상태 재평가 / (8) 세션 종료. **이전 (2026-05-17 후속 25)**: Phase α-4 R-1 Stage 3 Local Validation Evidence + Reviewer-only 단축 합의 APPROVE (`4ce5a0b` + `b264580` + `22b5c1c`).
docs/CONTEXT.md:92:**이전 후속 24 상세** (참고용 보존, 이전 entry): 2026-05-17 후속 24 (**Phase α-4 R-1 *실 진입 Step 분할* brief + Reviewer-only 단축 합의 APPROVE AS BRIEF (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-4 R-1 실 진입 step 분할 brief를 작성해주세요. 범위는 R-1 CI workflow 통합을 실제 구현하기 전에 step 분할, 수정 범위, 테스트 범위, rollback trigger, evidence 기준을 정리하는 것입니다. 아직 CI workflow 변경, runtime code 변경, actual run 재실행, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요." → "옵션 (A)로 진행"). **3 commit chain**: (1) `ed1d1b6` Phase α-4 R-1 step division brief (871줄, 14 섹션 — DRAFT — `docs/phase0/phase-alpha-4-r1-step-division-brief.md`) / (2) `52a05cb` Reviewer-only 단축 합의 보고서 (471줄, 12 섹션 — APPROVE AS BRIEF + 38 합의 조건 C-ρ-1~C-ρ-38 — `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-step-division.md`) / (3) `da57bdd` 메타 commit. **핵심 framing**: Phase α-4 R-1 진입 조건 점검 합의 (`1c365e7`, 33 조건 C-π) 발효 후속 Phase α-4 자체의 **Stage 2 등가 framing** — Step 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 영역 한정. **Step 0 ~ Step 6 분할 매트릭스 채택** + **cycle 옵션 (i) 직렬 권고** + **R-1 1593줄 본문 변경 0건** + **R-4/R-5/R-7 1192줄 변경 0건** + **`src/` 변경 0건** + **Rollback Trigger 28 × 0건 발화** + **ADR-011 §2.1 (a)~(e) × R-1 = 5/5 답습 충족** + **Step 0~6 × 5 금지 = 35/35 충돌 0** + **16/16 풀 3+1 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 확정**. **사용자 명시 5 금지 위반 영구 답습**. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **합산 284 합의 조건 변경 0건** + **본 합의 38 신규 조건 (C-ρ-1~C-ρ-38)**. **본 합의 ≠ Phase α-4 어느 Step 도 실 진입 / CI workflow 변경 / Step 분할·수정 범위·테스트 범위·Rollback Trigger·Evidence 기준 최종 확정** — Phase α-4 R-1 실 진입 Step 분할 권위 권고 한정. **이전 (2026-05-17 후속 23)**: Phase α-4 R-1 진입 조건 점검 brief + Reviewer-only 단축 합의 APPROVE AS BRIEF (`7a289fa` + `1c365e7` + `149898f`).
docs/CONTEXT.md:98:**이전 후속 21 상세** (참고용 보존): 2026-05-16 후속 21 (**Phase α-1 + α-2 + α-3 1순위 병렬 *실제 구현 진입 여부* brief + Reviewer-only 단축 합의 APPROVE (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 + α-2 + α-3 실제 병렬 구현 진입 brief를 작성해주세요. 범위는 R-4 도구 본문, R-5 .importlinter 본문, R-7 docker secret block의 실제 구현 진입 여부를 검토하는 것입니다. 아직 실제 파일 수정, CI workflow 변경, runtime code 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요." → "옵션 (A)로 진행해주세요"). **3 commit chain**: (1) `faae826 docs(phase0): add Phase alpha 1-3 parallel actual entry brief` (920줄, 14 섹션 — DRAFT brief) / (2) `7917e4a docs(review): approve Phase alpha 1-3 parallel actual entry` (446줄, 15 섹션 + Reviewer-only 단축 합의 APPROVE + 25 합의 조건 C-ξ-1~C-ξ-25) / (3) 메타 commit (본 commit). **framing 차이 핵심**: Stage 2 (`88ccf79` "How to plan 1순위 parallel?") → **Stage 3 (`7917e4a` "Should we enter 1순위 parallel actual implementation now?")** → Stage 4 (사용자 명시 결정 영역, 실 구현). **합의 효력**: Phase α-1 + α-2 + α-3 parallel actual implementation entry **— 실제 파일 수정 *직전* 의 진입 권한으로 한정** (Stage 4 자동 진입 0건). **합의 판정 = APPROVE (Reviewer-only 단축 합의 적격 — 8/8 풀 3+1 트리거 0건 발화)**. **4 결정 영역 채택**: D-1 (i) cycle 옵션 답습 한정 단축 + D-2 (a) Reviewer-only 단축 합의 + D-3 (5) 3 Phase 동시 진입 + D-4 (α) 통합 합의 1건. **96/96 Prerequisite 충족 매트릭스**: G1 9 상위 합의 답습 9/9 PASS + G2 5 사용자 명시 금지 5/5 위반 0건 + G3 27 추가 분리 27/27 + G4 8 풀 3+1 트리거 0/8 발화 + G5 5 영구 핵심 제약 5/5 보존 + G6 Provider Liquidity 5-way 5/5 보존 + G7 F-금지 #1 0/1 위반 + G8 13 actual run+evidence 답습 + G9 23 Rollback Trigger 0/23 발화 = **96/96 충족 ✅**. **사용자 명시 5 금지 위반 영구 답습**: #1 실제 파일 수정 = 0건 (합산 1192줄 답습 보존) / #2 CI workflow 변경 = 0건 (3 MVP-1 + 8 G2/G3/G4 PoC workflow 답습) / #3 runtime code 변경 = 0건 (`src/` + facade.py 41줄 placeholder 답습 보존) / #4 Operational Readiness PASS (Layer E) = 0건 / #5 Hermes PMO 격상 (Layer F) = 0건. **3 Phase 본문 변경 0건**: R-4 829 + R-5 35 + R-7 328 = 1192줄 답습 보존 (13 file). **추가 27 분리 영역 위반 0건**. **25 합의 조건 (C-ξ-1 ~ C-ξ-25)** + **합산 222 조건 영구 답습** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + 본 합의 25). **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습**. **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`210c98f` + 후속 18) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 (`1b3090b`) / α-2 (`6a79247`) / α-3 (`3f6306d`) / α-4 (`e59a565`) / Stage 2 / Stage 4 / Group A 1차/2차/3차 / Group D / §5.5 9 sub-수단 (`55c5b4b`) / mvp1.md §0 / Stage 1 (`542e77e`) / Stage 2 (`88ccf79`) 본문 변경 0건** + **ADR-011 §2.1 (a)~(e) 재정의 0건**. **추가 0건**: Phase α-1 / α-2 / α-3 실 진입 자체 / 합산 1192줄 본문 변경 / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Layer E / Layer F 진입 / Phase α-4 자동 진입 / Stage 4 실 구현 자동 진입 / 9 evidence 재생성 / 4 actual run 재실행 / 신규 actual run trigger / R-4.1/URL/Model catalog 변경 / `.importlinter` forbidden/facade/google.generativeai/URL 흡수 / R-7 docker secret 변경 / 3 MVP-1 + 8 G2/G3/G4 PoC workflow 변경 / PC-3 / AR-1 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 / Stage 5 자동 진입 / Tier-2/3 확장 / threshold *고정* / Rollback Trigger / TR-1~TR-5 발화 / Group α 14 결정 영역 / §5.5 9 sub-수단 변경 / Group I / token rotation / GitHub plan / event enum / ADR 갱신 / 신규 ADR / commit signing / `pull_request_target` / GitHub Actions secrets / Hermes upstream / Production docker-compose / 실 secret material / 실 API/SDK / 외부 LLM 자동 호출 / 실 docker build / docker run / docker history 자동 실행 / 인간 리뷰 의무 자동 발화 / facade real 본문 / Layer 2 runtime / 의미적 lock-in / 17 항목 우선순위 *재고정* / MVP-2 ~ MVP-6 deepening 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-1 + α-2 + α-3 실제 병렬 구현 시작 / (2) α-1 단독 / (3) α-2 단독 / (4) α-3 단독 / (5) Phase α-4 조건 점검 / (6) 세션 종료. **이전 (2026-05-16 후속 20)**: Phase α-1+2+3 1순위 병렬 구현 *계획* brief + APPROVE AS BRIEF (`2e36592` + `88ccf79` + `96a8d14`).
docs/CONTEXT.md:100:**이전 후속 20 상세** (참고용 보존): 2026-05-16 후속 20 (**Phase α-1 + α-2 + α-3 1순위 병렬 구현 brief + Reviewer-only 단축 합의 (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 + α-2 + α-3 1순위 병렬 구현 brief를 작성해주세요. 범위는 R-4 도구 본문, R-5 .importlinter 본문, R-7 docker secret block을 실제 구현하기 전 cycle 분할, 수정 범위, 테스트 범위, rollback trigger, evidence 기준을 정리하는 것입니다. 아직 실제 파일 수정, CI workflow 변경, runtime code 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요." → "옵션 (A)로 진행해주세요"). **3 commit chain**: (1) `2e36592 docs(phase0): add Phase alpha 1-3 parallel implementation brief` (950줄, 13 섹션 — DRAFT brief) / (2) `88ccf79 docs(review): approve Phase alpha 1-3 parallel implementation brief` (359줄, 15 섹션 + Reviewer-only 단축 합의 APPROVE AS BRIEF + 25 합의 조건 C-ν-1~C-ν-25) / (3) 메타 commit (본 commit). **본 합의 framing**: Phase α 통합 실제 구현 계획 합의 (`542e77e` 후속 19) cycle 옵션 (i) 답습 — 1순위 병렬 부분 (α-1 + α-2 + α-3) *cycle 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정 DRAFT → APPROVE AS BRIEF 격상*. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 8/8 풀 3+1 트리거 0건 발화)**. **사용자 명시 5 금지 위반 영구 답습**: #1 실제 파일 수정 = 0건 (합산 1192줄 답습 보존) / #2 CI workflow 변경 = 0건 / #3 runtime code 변경 = 0건 (`src/` + facade.py 41줄 placeholder 답습 보존) / #4 Operational Readiness PASS = 0건 / #5 Hermes PMO 격상 = 0건. **3 Phase 본문 합산**: R-4 829 + R-5 35 + R-7 328 = **1192줄 답습 보존** (3 Phase × 13 artifact + 4 sub-수단 S-1 + T-2 + T-2 import-linter + T-5 + ST-3, Phase α-4 PC-3 + AR-1 = 2순위 의존 분리, 5+ sub-수단 PC-4 + AR-2 + AR-3 + S-2 + ST-1/2/4/5 = Backlog 분리). **의존성 토폴로지**: α-1 ↔ α-2 부분 의존 (T-6) / α-1 ↔ α-3 독립 / α-2 ↔ α-3 독립 / 3 Phase → α-4 선행 의존 (Phase α-4 별도 brief 영역). **cycle 분할 답습**: Step 0 사전 점검 / Step 1 1순위 병렬 진입 (1.α-1 / 1.α-2 / 1.α-3 sub-step) / Step 2 actual run PASS 답습 / Step 3 합의 형태 결정 [사용자 명시 결정 의무] / Step 4 옵션 외부 LLM / Step 5 합의 보고서 / Step 6 메타 commit push. **4 cycle 옵션 권고** (i 답습 한정 단축 / ii minor 인터페이스 정렬 / iii 3 Phase 분리 / iv 풀 3+1) — 모두 사용자 결정 영역. **3 Phase 별 수정 범위**: 1192줄 답습 한정 + α-1 + α-3 minor CLI 인터페이스 정렬 후보. **3 Phase 별 테스트 범위**: fixture 답습 검증 + unit test dry-run + actual run regression (재실행 0건). **3 Phase 별 Rollback Trigger**: Layer B 18 trigger 中 1순위 직접 7 + 간접 1 + 영역 외 10 + TR-1~TR-5 5 = **발화 0건** + threshold 후보 한정. **3 Phase 별 Evidence 기준**: ADR-011 §2.1 (a)~(e) × 3 Phase = **15/15 PASS** Layer C 답습. **actual run 답습 4/4 PASS**: `25728590939` + `25728590916` + `25728590977` + `25731846625` (재실행 0건). **추가 27 분리 영역 위반 0건**: Phase α-4 / branch protection / dev 환경 / `pre-commit install` 의무화 / PC-3+4 + AR-1+2+3 / ST-1/2/4/5 / S-2 / Tier-2/3 / commit signing / `pull_request_target` / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 모두 분리. **25 합의 조건 (C-ν-1 ~ C-ν-25)** 답습 + **합산 197 조건 영구 답습** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Phase α 통합 계획 25 + 본 합의 25). **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습**. **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`210c98f` + 후속 18) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 (`1b3090b`) / α-2 (`6a79247`) / α-3 (`3f6306d`) / α-4 (`e59a565`) / Stage 2 / Stage 4 / Group A 1차/2차/3차 / Group D / §5.5 9 sub-수단 (`55c5b4b`) / mvp1.md §0 / Phase α 통합 계획 (`542e77e`) 본문 변경 0건** + **ADR-011 §2.1 (a)~(e) 재정의 0건**. **추가 0건**: Phase α-1 / α-2 / α-3 실 진입 / 합산 1192줄 본문 변경 / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Layer E / Layer F 진입 / Phase α-4 자동 진입 / Phase β / γ 자동 진입 / 9 evidence 파일 재생성 / 4 prerequisite actual run 재실행 / 신규 actual run trigger / R-4.1/URL/Model catalog 변경 / `.importlinter` forbidden/facade/google.generativeai/URL 흡수 / R-7 docker secret 변경 / 3 MVP-1 + 8 G2/G3/G4 PoC workflow 변경 / PC-3 / AR-1 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 / Stage 5 자동 진입 / Tier-2/3 확장 / threshold *고정* / Rollback Trigger / TR-1~TR-5 발화 / Group α 14 결정 영역 재결정 / §5.5 9 sub-수단 변경 / Group I 자동 진입 / token rotation / GitHub plan 자동 확인 / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR / P / GP 발행 / commit signing / `pull_request_target` / GitHub Actions secrets / Hermes upstream Dockerfile / Production docker-compose / 실 secret material / 실 API/SDK / 외부 LLM 자동 호출 / 실 docker build / docker run / docker history 자동 실행 / 인간 리뷰 의무 자동 발화 / `src/adapters/llm/facade.py` real 본문 / Layer 2 runtime / 의미적 lock-in / 17 항목 우선순위 *재고정* / MVP-2 ~ MVP-6 deepening / cycle 옵션 / 합의 형태 / step 분할 자동 결정 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-1 + α-2 + α-3 실제 병렬 구현 진입 / (2) Phase α-1 단독 구현 / (3) Phase α-2 단독 구현 / (4) Phase α-3 단독 구현 / (5) Phase α-4 진입 조건 점검 / (6) cycle 옵션 (ii) minor 인터페이스 정렬 brief / (7) cycle 옵션 (iii) 3 Phase 분리 brief / (8) 풀 3+1 + 외부 LLM 진입 brief / (9) 다른 Backlog 진입 / (10) 세션 종료. **이전 (2026-05-16 후속 19)**: Phase α-1 ~ α-4 통합 실제 구현 계획 brief + Reviewer-only 단축 합의 (옵션 (A)) + 3 commit chain (`96891eb` + `542e77e` + `b7d3415`).
docs/CONTEXT.md:102:**이전 후속 19 상세** (참고용 보존): 2026-05-16 후속 19 (**Phase α-1 ~ α-4 통합 실제 구현 계획 brief + Reviewer-only 단축 합의 (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 ~ α-4 통합 실제 구현 계획 brief를 작성해주세요. 범위는 R-4 도구 본문, R-5 .importlinter, R-7 docker secret block, R-1 CI workflow 통합을 실제 구현하기 전 단계 분할로 정리하는 것입니다. 아직 실제 파일 수정, CI workflow 변경, runtime code 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요." → "옵션 (A)로 진행해주세요"). **3 commit chain**: (1) `96891eb docs(phase0): add Phase alpha integrated implementation plan brief` (949줄, 11 섹션 — DRAFT brief) / (2) `542e77e docs(review): approve Phase alpha integrated implementation plan brief` (367줄, 11 섹션 + Reviewer-only 단축 합의 APPROVE AS BRIEF + 25 합의 조건 C-μ-1~C-μ-25) / (3) 메타 commit (본 commit). **본 합의 framing**: Layer C 발효 (`eb01bc4` 2026-05-16) + Layer D 권위 답습 (`210c98f` + 후속 18) 後 — Phase α 4 단계 (α-1 R-4 도구 본문 / α-2 R-5 `.importlinter` / α-3 R-7 docker secret block / α-4 R-1 CI workflow 통합) 의 *통합 실제 구현 단계 분할 정리 한정 준비안 (DRAFT) → APPROVE AS BRIEF 격상*. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 8/8 풀 3+1 트리거 0건 발화)**. **사용자 명시 5 금지 위반 영구 답습**: #1 실제 파일 수정 = 0건 (합산 2785줄 답습 보존) / #2 CI workflow 변경 = 0건 (3 MVP-1 + 8 G2/G3/G4 PoC workflow 답습 보존) / #3 runtime code 변경 = 0건 (`src/` 본문 + `facade.py` 41줄 placeholder 답습 보존) / #4 Operational Readiness PASS (Layer E) 선언 = 0건 / #5 Hermes PMO 격상 (Layer F) = 0건. **4 영역 본문 합산 매트릭스**: R-4 829 + R-5 35 + R-7 328 + R-1 1593 = **2785줄 답습 보존** (4 Phase × 20 artifact + 6 sub-수단 S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1, Layer B §5.5 9 sub-수단 中 3 sub-수단 PC-4 + AR-2 + AR-3 = 본 합의 영역 외 분리 명시). **의존성 토폴로지** = **1순위 병렬 (α-1 + α-2 + α-3)** + **2순위 의존 (α-4 = Stage 4 prerequisite actual run PASS 4/4 선행 evidence 의무)**. **통합 실제 구현 단계 분할** = α-1 11 sub-step + α-2 6 항목 + α-3 4 sub-step + α-4 4 sub-step (단, 4.3 PC-4 + 4.4 AR-2 = 본 합의 영역 외 분리 명시). **통합 cycle 옵션 권고**: (i) 1순위 병렬 — 2순위 의존 / (ii) 단일 cycle / (iii) 4 cycle 분리 — 모두 *권고 한정* 사용자 명시 결정 영역. **actual run 답습 4/4 PASS**: `25728590939` + `25728590916` + `25728590977` + `25731846625` (재실행 0건). **통합 진입 적격성 5/5 (C-π-1 ~ C-π-5) 충족** (C-π-1 5 금지 충돌 0/5 + C-π-2 Layer C evidence 답습 100% + C-π-3 Layer D 권위 답습 100% + C-π-4 Provider Liquidity 5-way 100% + C-π-5 5 영구 핵심 제약 5/5) + **의존성 의무 검토 통과** (4 prerequisite actual run PASS 100% 答) + **8/8 풀 3+1 트리거 0건 발화**. **추가 24 분리 영역 위반 0건 영구 답습**: branch protection / dev 환경 강제 / `pre-commit install` 의무화 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 / Tier-2/3 / commit signing / `pull_request_target` / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 등 모두 분리 명시. **25 합의 조건 (C-μ-1 ~ C-μ-25)** 답습 — Phase α 4 단계 영역 합산 정의 + 의존성 토폴로지 + 통합 cycle 옵션 + actual run 답습 + 5 금지 영역 분리 + 적격성 검토 + Rollback Trigger 의존성 + 합산 합의 조건 답습 (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 29 + Layer C 30 + Layer D 25 + 본 합의 25 = **합산 201 조건** 영구 답습). **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (4 Phase = enforcement / config / docker secret / workflow 영역 = catalog / provider 영역과 직교) + **F-금지 #1 영구 답습 — GitHub Actions secrets 사용 도입 0건**. **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`210c98f`) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 (`1b3090b`) / α-2 (`6a79247`) / α-3 (`3f6306d`) / α-4 (`e59a565`) / Stage 2 / Stage 4 / Group A 1차/2차/3차 / Group D / §5.5 9 sub-수단 (`55c5b4b`) / mvp1.md §0 3-layer PASS framework 본문 어느 줄도 변경 0건** + **ADR-011 §2.1 (a)~(e) 5 조건 재정의 0건**. **추가 0건**: Phase α-1 / α-2 / α-3 / α-4 어느 것도 실 진입 / 합산 2785줄 본문 변경 / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Layer E / Layer F 진입 / 9 evidence 파일 재생성 / 4 prerequisite actual run 재실행 / 신규 actual run 자동 trigger / R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 / `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경 / R-7 docker secret block 변경 / 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 변경 / PC-4 / AR-2 / AR-3 / ST-1 / ST-2 / ST-4 / ST-5 / S-2 진입 / Stage 5 자동 진입 / Tier-2 / Tier-3 catalog 자동 확장 / threshold *고정* / Rollback Trigger / TR-1~TR-5 자동 발화 / Group α 14 결정 영역 재결정 / §5.5 9 sub-수단 본문 채택 변경 / Group I (Hermes-originated commit auto-reject) 자동 진입 / token rotation 정책 자동 결정 / GitHub plan / ruleset 가용성 자동 확인 / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR / 신규 P / 신규 GP 발행 / commit signing / `pull_request_target` workflow / Hermes upstream Dockerfile / Production docker-compose / 실 secret material commit / 실 API key / provider SDK / 외부 API 호출 / 외부 LLM 자동 호출 / 인간 리뷰 의무 자동 발화 / `src/adapters/llm/facade.py` real 본문 작성 / Layer 2 runtime block (G5-5) 진입 / 의미적 lock-in 검사 진입 / 17 항목 우선순위 자동 *재고정* / MVP-2 ~ MVP-6 본문 deepening / 실 cycle 옵션 / 실 합의 형태 / 실 step 분할 자동 결정 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-1 + α-2 + α-3 1순위 병렬 구현 진입 brief / (2) Phase α-1 단독 구현 진입 brief / (3) Phase α-2 단독 구현 진입 brief / (4) Phase α-3 단독 구현 진입 brief / (5) Phase α-4 진입 조건 점검 brief / (6) cycle 옵션 (ii) 단일 cycle 통합 실 진입 brief / (7) cycle 옵션 (iii) 4 cycle 분리 진입 brief / (8) 다른 Backlog 진입 (C-5b ST-1 / C-5c PC-4 T3 / C-6 잔여 sub-수단 / C-7 T3 / C-8 facade / Group I / token rotation / GitHub plan 등) / (9) 세션 종료. **이전 (2026-05-16 후속 18)**: Layer D — MVP-1 PASS *재진입 가능성 검토* brief + Reviewer-only 단축 합의 (옵션 (A) — Existing Layer D authority preserved) + 3 commit chain (`d286f87` + `951a5b1` + `ce344e3`).
docs/CONTEXT.md:104:**이전 후속 18 상세** (참고용 보존): 2026-05-16 후속 18 (**Layer D — MVP-1 PASS *재진입 가능성 검토* brief + Reviewer-only 단축 합의 (옵션 (A) — Existing Layer D authority preserved) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Layer D MVP-1 PASS 선언 합의 진입 brief를 작성해주세요. 범위는 Layer C 발효 완료 후, MVP-1 PASS Layer D 선언에 들어갈 수 있는지 검토하는 것입니다." → "옵션 (A)로 진행해주세요" + "C-1~C-8 상태는 최신 CONTEXT 기준으로 재검증"). **3 commit chain**: (1) brief commit (`docs/phase0/layer-d-mvp1-pass-declaration-entry-brief.md`, 721+줄, 13 섹션 — DRAFT + C-1~C-8 satisfaction cross-reference 답습 정확화) / (2) 합의 보고서 commit (`docs/review/3plus1-consensus-2026-05-16-layer-d-reentry-assessment.md` — APPROVE AS BRIEF + Existing Layer D authority preserved + 25 합의 조건 C-λ-1~C-λ-25) / (3) 메타 commit (본 commit). **핵심 framing 발견**: **Layer D 는 이미 `210c98f` (2026-05-13) APPROVE WITH CONDITIONS 으로 발효 완료** — 본 brief = Layer C 재발효 (`eb01bc4` 2026-05-16) 후속 *재진입 가능성 검토* (Layer C 재발효 = Layer D 의 근거 *강화*, 재선언 요구 0건). **5 핵심 발효 문구**: (1) **Layer D MVP-1 PASS = 기존 `210c98f` 권위 유지** / (2) **Layer C 재발효 = Layer D 근거 *강화* (재선언 요구 0건)** / (3) **Layer D 본문 변경 = 0건** / (4) **MVP-1 PASS 재선언 = 0건** / (5) **Layer E / Layer F 진입 = 0건**. **C-1 ~ C-8 8 조건 현 satisfaction 매트릭스 (Layer D 원문 변경 0건 + 후속 합의 권위 source cross-reference 답습)**: ✅ **Satisfied = 2** (C-1 K-2 baseline `1dd1036` + C-2 event enum 정식 등록 Backlog #5 `4221646`+`2ece90a`+`b705370`) / ⚠️ **Partially Satisfied = 2** (C-5 전체 = C-5a+C-5c partial `78483c5` + C-6 PC-4 T2 sub only `78483c5`) / ⏳ **Deferred = 3** (C-3 Layer E / C-4 Layer F / C-8 P1 v2 facade) / ⏳ **Requires separate full 3+1 = 1** (C-7 T3 영역 + Group α 진전 `4880e88`). **C-5 sub-condition (γ 분리 답습 `6c616a8`)**: C-5a Satisfied (`6fa87dc`) / C-5b Deferred / C-5c Partially Satisfied PC-4 T2 sub only (`78483c5`). **3 framing 옵션 매트릭스 (§4)**: (A) 기존 Layer D 답습 한정 — **권고 후보 (사용자 명시 채택)** / (B) Layer D 재발효 합의 — 선택 후보 / (C) Layer D *de novo* 신규 발효 — 비권고. **Layer D 재진입 적격성 5 조건 (C-κ-1 ~ C-κ-5) 5/5 충족** + **27/27 풀 3+1 트리거 0건 발화** + **Layer C + Layer D 합산 60/60 트리거 0건 발화** + **합의 형태 = Reviewer-only 단축 합의** (옵션 (A) 답습). **25 합의 조건 (C-λ-1 ~ C-λ-25)**. **사용자 명시 5 금지 위반 영구 답습**: #1 Operational Readiness PASS (Layer E) 선언 = 0건 / #2 Hermes PMO 격상 (Layer F) = 0건 / #3 actual run 재실행 = 0건 / #4 evidence 재생성 = 0건 / #5 R-4 (829줄) + R-5 (35줄) + R-7 (328줄) + R-1 (1593줄) 합산 2785줄 본문 어느 줄도 변경 = 0건. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습**. **기존 Layer D (`210c98f`) 본문 변경 0건** + **8 조건 (C-1 ~ C-8) 본문 정의 변경 0건** + **본 합의 추가 satisfaction 갱신 0건** (모든 satisfaction 갱신 = 이전 후속 합의 권위 source 답습). **Layer C 진입 가능성 합의 (`c13c011`) 30 조건 (C-η) / Layer C 실 발효 합의 (`eb01bc4`) 30 조건 (C-ι) / Phase α-1 (`1b3090b`) / α-2 (`6a79247`) / α-3 (`3f6306d`) / α-4 (`e59a565`) 합의 본문 변경 0건** + **C-β / C-γ / C-δ / C-ε 자동 변경 0건** + **Group α (`4880e88`) C-1~C-12 / Backlog #6 (`c7ddfdd`) C-α-1~C-α-11 / Layer A (`f1e0b23`) / Layer B (`f40423f`) / §5.5 9 sub-수단 (`55c5b4b`) 본문 변경 0건** + **ADR-011 §2.1 (a)~(e) 5 조건 재정의 0건** + **mvp1.md §0 3-layer PASS framework 본문 변경 0건**. **추가 0건**: Layer D 재발효 / Layer D *de novo* 신규 발효 / MVP-1 PASS 재선언 / Layer E 선언 / Layer F 격상 / 외부 LLM 자동 호출 / blind 의뢰서 작성 / vendor 자동 선택 / 응답 결론 강제 채택 / 신규 actual run 자동 trigger / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / runtime code 변경 / Hermes upstream Dockerfile 변경 / Production `docker-compose.yml` 변경 / 실 secret material commit / 실 API key / provider SDK / 외부 API 호출 / 인간 리뷰 의무 자동 발화 / Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 / Phase α-1 / α-2 / α-3 / α-4 실 진입 자동 진입 / PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 / Layer 2 runtime block (G5-5) 진입 / `src/adapters/llm/facade.py` real 본문 작성 / MVP-2 ~ MVP-6 본문 deepening / token rotation 정책 자동 결정 / GitHub plan / ruleset 가용성 자동 확인 / commit signing / `pull_request_target` workflow / Tier-2 / Tier-3 catalog 자동 확장 / threshold *고정* / event enum 추가 등록 / ADR 본문 자동 갱신 / 신규 ADR / 신규 P / 신규 GP 발행 / Group I / Group β / γ-1 / γ-2 자동 진입 / Phase β / γ 자동 진입 / 17 항목 우선순위 자동 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) push (사용자 명시 결정 시) / (2) C-5b ST-1 entrypoint stat 진입 brief (Backlog #1 1.5차 보강) / (3) C-5c PC-4 T3 sub 진입 brief (Backlog #3 + 사용자 명시 5 금지 영역 분리 — 사용자 명시 결정 의무) / (4) C-6 잔여 sub-수단 진입 brief (Backlog #2) / (5) C-7 T3 영역 실 적용 단계 (Group α 답습) / (6) C-8 P1 v2 facade real 본문 작성 brief (Backlog #4) / (7) Phase α-1 ~ α-4 실 진입 step 분할 brief / (8) Phase α-1 ~ α-4 통합 실제 구현 계획 brief / (9) Group I 별도 합의 / (10) token rotation 정책 별도 합의 / (11) GitHub plan / ruleset 가용성 확인 / (12) 세션 종료. **이전 (2026-05-16 후속 17)**: Layer C — MVP-1 Implementation Evidence PASS *실 발효* + GP-3 / GP-5 PASS 발효 — Reviewer-only 단축 합의 APPROVE + 2 commit chain (`eb01bc4` 합의 보고서 + `24caa53` 메타) — Step 0~6 cycle 완료.
docs/CONTEXT.md:106:**이전 후속 17 상세** (참고용 보존): 2026-05-16 후속 17 (**Layer C — MVP-1 Implementation Evidence PASS *실 발효* + GP-3 / GP-5 PASS 발효 — Reviewer-only 단축 합의 APPROVE + 2 commit chain (Step 5 합의 보고서 + Step 6 메타)**). 사용자 명시 진입 명령 답습 ("Step 5 진입으로 진행해주세요" → "(A) Step 6 진입으로 진행해주세요" — Step 0~2 사전 점검 + Step 3 합의 형태 결정 (옵션 A 단축) + Step 4 Skip + Step 5 실 발효 + Step 6 메타+push). **2 commit chain**: (1) `eb01bc4 docs(review): approve Layer C implementation evidence pass actual entry` (610줄, 12 섹션 + Reviewer-only 단축 합의 APPROVE + 30 합의 조건 C-ι-1~C-ι-30) / (2) 메타 commit (본 commit). **종합 판정 = APPROVE — MVP-1 Implementation Evidence PASS (Layer C) + GP-3 PASS + GP-5 PASS 발효**. **Step 0 사전 점검 통과** (11/11 답습 commit chain 변경 0건 — Layer C 진입 가능성 합의 `c13c011` + Layer C 실 진입 brief `0862f74` + Phase α-1 `1b3090b` + α-2 `6a79247` + α-3 `3f6306d` + α-4 `e59a565` + Group α `4880e88` + Backlog #6 `c7ddfdd` + Layer A `f1e0b23` + Layer B `f40423f` + §5.5 9 sub-수단 `55c5b4b`). **Step 1 양 GP × 5 조건 evidence 답습 검증 통과** (10/10 적격성 + 8 evidence file line count 정확 일치 + 9/9 재생성 0건 — GP-3 `tools/secret_scanner.py` 368줄 + `docker/gp3-st3-poc/` 93줄 + `.github/workflows/secret-hygiene-egress-redaction.yml` 694줄 / GP-5 `tools/provider_import_scanner.py` 178줄 + `.importlinter` 35줄 + `tools/provider_url_scanner.py` 283줄 + `.github/workflows/provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 + `src/adapters/llm/facade.py` 41줄 placeholder). **Step 2 4 prerequisite actual runs PASS 답습 확정** (Stage 1 `25728590939` + Stage 3 `25728590916` + `25728590977` commit `72622409` + Stage 2 `25731846625` commit `6c6b208` 모두 SUCCESS — 5 source cross-reference 일관 + 재실행 0건 + 신규 trigger 0건). **Step 3 합의 형태 = Reviewer-only 단축 합의** (옵션 A — 사용자 명시 결정 2026-05-16 — brief §3.4 답습 — 신규 판단 영역 아님). **Step 4 = Skip** (단축 흐름 답습 — 외부 LLM blind 의뢰 0건 / vendor 자동 선택 0건 / 외부 LLM 자동 호출 0건). **Step 5 Layer C 실 발효 완료** (eb01bc4 합의 보고서 발효 — GP-3 + GP-5 동시 발효). **Step 6 메타 갱신 + commit + push 완료** (본 commit + push). **33/33 풀 3+1 승격 트리거 0건 발화** (c13c011 §5 15 + brief §5.2 18). **30 합의 조건 C-ι-1 ~ C-ι-30 enumerate**. **혼동 방지 (영구 답습)**: **MVP-1 PASS (Layer D) = 아직 아님** (Layer C 발효 후 별도 합의 영역 분리) / **Operational Readiness PASS (Layer E) = 아직 아님** (MVP-6 영역 분리) / **Hermes PMO 격상 (Layer F) = 아직 아님** (ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 분리). **사용자 명시 7 금지 위반 영구 답습**: #1 (실 Layer C 발효) = **본 합의 = 사용자 명시 Step 5 결정 답습** (사용자 명시 결정 권한) / #2 (CI workflow 변경) = **0건** / #3 (branch protection 변경) = **0건** / #4 (dev 환경 강제) = **0건** / #5 (`pre-commit install` 의무화) = **0건** / #6 (Operational Readiness PASS) = **0건** / #7 (Hermes PMO 격상) = **0건**. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (Layer C = evidence verification = catalog / provider 영역과 직교) + **F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건)**. **C-β-1 ~ C-β-15 / C-γ-1 ~ C-γ-26 / C-δ-1 ~ C-δ-28 / C-ε-1 ~ C-ε-29 / C-η-1 ~ C-η-30 / C-θ-1 ~ C-θ-5 / C-1 ~ C-12 / C-α-1 ~ C-α-11 자동 변경 0건** + **ADR-011 §2.1 (a)~(e) 5 조건 재정의 0건**. **추가 0건**: MVP-1 PASS (Layer D) 자동 선언 / Operational Readiness PASS 선언 / Hermes PMO 격상 / 외부 LLM 자동 호출 / actual run 재실행 / evidence 재생성 / 신규 actual run trigger / R-4 (829줄) / R-5 `.importlinter` (35줄) / R-7 docker secret block (328줄) / R-1 CI workflow 통합 (1593줄) 본문 어느 줄도 변경 (합산 2785줄 답습 보존) / CI workflow 변경 / branch protection 변경 / runtime code 변경 / Phase α-1 / α-2 / α-3 / α-4 자동 재진입 / Phase β / γ 자동 진입 / 7 금지 영역 *추가 해소* / Group I / Group β / γ-1 / γ-2 자동 진입 / Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 / token rotation 정책 자동 결정 / GitHub plan 가용성 자동 확인 / commit signing 도입 / `pull_request_target` workflow 도입 / Tier-2 / Tier-3 catalog 자동 확장 / threshold *고정* / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR / 신규 P / 신규 GP 발행 / 실 API key / provider SDK / 외부 API 호출 / 인간 리뷰 의무 자동 발화 / Hermes upstream Dockerfile 변경 / Production `docker-compose.yml` 변경 / 실 secret material commit / PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 / Layer 2 runtime block (G5-5) 진입 / `src/adapters/llm/facade.py` real 본문 작성 / MVP-2 ~ MVP-6 본문 deepening / 17 항목 우선순위 자동 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Layer D MVP-1 PASS 선언 합의 진입 brief / (2) Phase α-1 R-4 829줄 실 진입 step 분할 brief / (3) Phase α-2 R-5 35줄 실 진입 step 분할 brief / (4) Phase α-3 R-7 328줄 실 진입 step 분할 brief / (5) Phase α-4 R-1 1593줄 실 진입 step 분할 brief / (6) Phase α-1 ~ α-4 통합 실제 구현 계획 brief / (7) Group α 조건 재평가 / (8) Group I 별도 합의 / (9) token rotation 정책 별도 합의 / (10) GitHub plan 가용성 확인 / (11) 세션 종료. **이전 (2026-05-14 후속 16)**: Layer C 발효 합의 *실 진입 단계 분할* brief — APPROVE AS BRIEF + 3 commit chain (`0862f74` brief / `aba6ce0` 합의 / `d2213c0` 메타).
docs/CONTEXT.md:108:**이전 후속 16 상세** (참고용 보존): 2026-05-14 후속 16 (**Layer C 발효 합의 (Implementation Evidence PASS) *실 진입 단계 분할* brief 작성 + Reviewer-only 단축 합의 발효 — APPROVE AS BRIEF + 3 commit chain**). 사용자 명시 진입 명령 답습 ("옵션 A로 진행해주세요" + Phase α-1 / α-2 / α-3 / α-4 / Layer C 진입 가능성 검토 패턴 답습 — brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실 Layer C 발효는 아직 하지 않음). **3 commit chain**: (1) `0862f74 docs(phase0): add Layer C implementation evidence pass actual entry brief` (744줄, 11 섹션 — DRAFT brief) / (2) `aba6ce0 docs(review): approve Layer C implementation evidence pass actual entry` (521줄, 11 섹션 + Reviewer-only 단축 합의 APPROVE AS BRIEF + 36 합의 조건 C-ι-1~C-ι-36) / (3) 메타 commit (본 commit). **본 합의 영역** = **수단 결정 적격성 권위 권고 발행 한정** (Layer C 진입 가능성 검토 합의 (`c13c011`) 발효 후속 — 실 진입 *단계 분할 한정* + 적격성 *해소* 0건) — 실 변경 0건. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 18/18 풀 3+1 트리거 0건 발화 검증)**. **본 brief framing 차이** = 진입 *가능성 검토* (`c13c011`, "Can we enter?") 가 아닌, **실 진입 *단계 분할 + 결정 지점 + cycle commit chain*** ("How do we enter step-by-step?") — **Stage 2 / Stage 4 합의 패턴 답습**. **7 Step 분할안 채택 권고**: Step 0 (사전 점검) / Step 1 (양 GP × 5 조건 evidence 답습 검증 — 재생성 0건) / Step 2 (4 prerequisite actual runs PASS 답습 확정 — 재실행 0건) / **Step 3 (합의 형태 결정 — 단축 vs 풀 3+1 + 외부 LLM 1+ — 사용자 명시 결정 의무 영역)** / Step 4 (옵션 — 외부 LLM 1+ blind 의뢰, Step 3 풀 3+1 선택 시) / **Step 5 (Layer C 발효 합의 보고서 작성 + Implementation Evidence PASS *실 발효 선언* — 사용자 명시 결정 의무 영역)** / Step 6 (메타 갱신 + commit + push). **분할 옵션 매트릭스**: 단축 흐름 (5 step, 권고 후보 — Phase α-1/2/3/4 + 진입 가능성 합의 패턴 답습) / 풀 3+1 흐름 (7 step, 선택 후보). **각 Step 결정 지점 매트릭스** (Step 0~2 자동 검증 + Step 3~6 사용자 명시 결정 의무 영역). **cycle commit chain 후보 매트릭스** (단축 = 3 commit / 풀 3+1 = 다중 commit). **실 진입 단계 분할 적격성 5 조건 (C-θ-1 ~ C-θ-5) 5/5 충족 검증** (C-θ-1 7 금지 충돌 0/7 + C-θ-2 Layer C 진입 가능성 합의 30 조건 답습 + C-θ-3 7 Step 분할 일관성 + C-θ-4 각 Step 결정 지점 명시 + C-θ-5 5 영구 핵심 제약 5/5 보존) + **18/18 풀 3+1 승격 트리거 0건 발화** + **합의 형태 결정 단계 분할** (Step 3 단축 권고 후보 / 풀 3+1 + 외부 LLM 1+ 선택 후보) + **Rollback Trigger 단계별 옵션 답습** (Step 0 ~ Step 6 각 단계별 rollback 옵션). **사용자 명시 7 금지 7/7 답습**: **실 Layer C 발효 = 0건** / **CI workflow 변경 = 0건** / **branch protection 변경 = 0건** / **dev 환경 강제 = 0건** / **`pre-commit install` 의무화 = 0건** / **Operational Readiness PASS (Layer E) = 0건** / **Hermes PMO 격상 (Layer F) = 0건**. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (Layer C 발효 합의 = consensus step = catalog / provider 영역과 직교) + **F-금지 #1 영구 답습 — GitHub Actions secrets 사용 도입 0건**. **Layer C 진입 가능성 합의 (`c13c011`) 본문 변경 0건** + C-η-1 ~ C-η-30 자동 변경 0건 + **Phase α-4 합의 (`e59a565`) / Phase α-3 합의 (`3f6306d`) / Phase α-2 합의 (`6a79247`) / Phase α-1 합의 (`1b3090b`) 본문 변경 0건** + C-β / C-γ / C-δ / C-ε 자동 변경 0건 + **Backlog #6 우선 진입 합의 (`c7ddfdd`) / Group α 합의 (`4880e88`) / Layer A / Layer B / §5.5 9 sub-수단 / GP-3 MVP-1 진입 / GP-3 Stage 2 / GP-5 MVP-1 진입 / Stage 4 / 5 Stage 분할안 (`c50e6a0`) / Group A 2차 풀 3+1 합의 본문 변경 0건** + **ADR-011 §2.1 (a)~(e) 5 조건 재정의 0건**. **추가 0건**: Layer C 실 발효 / GP-3 / GP-5 PASS 발효 / MVP-1 PASS (Layer D) 선언 / 어느 Step (Step 0 ~ Step 6) 자동 진입 / 합의 형태 자동 결정 / Step 4 외부 LLM 자동 호출 / blind 의뢰 자동 발송 / Step 5 합의 보고서 자동 작성 + 실 발효 선언 자동 진입 / Step 6 메타 갱신 + commit + push 자동 진입 / 양 GP × 5 조건 evidence 재생성 / 4 prerequisite actual runs 자동 재실행 / 신규 actual run 자동 trigger / R-4 (829줄) / R-5 (35줄) / R-7 (328줄) / R-1 (1593줄) 본문 어느 줄도 변경 (합산 2785줄 답습) / Phase α-1 / α-2 / α-3 / α-4 자동 재진입 / step 분할안 자동 재설계 / Phase β / γ 자동 진입 / 7 금지 영역 *해소* / Group I / Group β / γ-1 / γ-2 자동 진입 / Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 / token rotation 정책 자동 결정 / GitHub plan 가용성 자동 확인 / commit signing / `pull_request_target` workflow / Tier-2 / Tier-3 catalog 자동 확장 / threshold *고정* / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR / 신규 P / 신규 GP 발행 / 실 API key / provider SDK / 외부 API 호출 / 인간 리뷰 의무 자동 발화 / Hermes upstream Dockerfile 변경 / Production `docker-compose.yml` 변경 / 실 secret material commit / PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 / Layer 2 runtime block (G5-5) 진입 / `src/adapters/llm/facade.py` real 본문 작성 / MVP-2 ~ MVP-6 본문 deepening / 17 항목 우선순위 자동 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Step 0 ~ Step 2 진입 (사전 점검) / (2) Step 3 합의 형태 결정 (단축 vs 풀 3+1) / (3) **Step 5 Layer C 발효 합의 보고서 작성 직진 (단축 흐름)** / (4) Step 3 풀 3+1 + Step 4 외부 LLM 1+ blind 의뢰 진입 / (5) Phase α-4 실 진입 step 분할 brief / (6) Phase α-1 ~ α-4 통합 실제 구현 계획 brief / (7) Phase α-1 / α-2 / α-3 실 진입 step 분할 brief / (8) Group α 조건 재평가 / (9) Group I 별도 합의 / (10) token rotation 정책 별도 합의 / (11) GitHub plan 가용성 확인 / (12) 세션 종료. **이전 (2026-05-14 후속 15)**: Layer C 발효 합의 진입 가능성 brief — APPROVE AS BRIEF + 3 commit chain (`1073593` brief / `c13c011` 합의 / `dc19885` 메타).
docs/CONTEXT.md:110:**이전 후속 15 상세** (참고용 보존): 2026-05-14 후속 15 (**Layer C 발효 합의 (Implementation Evidence PASS) 진입 brief 작성 + Reviewer-only 단축 합의 발효 — APPROVE AS BRIEF + 3 commit chain**). 사용자 명시 진입 명령 답습 ("옵션 A로 진행해주세요" + Phase α-1 / α-2 / α-3 / α-4 패턴 답습 — brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실 Layer C 발효는 아직 하지 않음). **3 commit chain**: (1) `1073593 docs(phase0): add Layer C implementation evidence pass entry brief` (712줄, 11 섹션 — DRAFT brief) / (2) `c13c011 docs(review): approve Layer C implementation evidence pass entry` (554줄, 11 섹션 + Reviewer-only 단축 합의 APPROVE AS BRIEF + 30 합의 조건 C-η-1~C-η-30) / (3) 메타 commit (본 commit). **본 합의 영역** = **수단 결정 적격성 권위 권고 발행 한정** (Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone 후속 — Layer C 발효 합의 *진입 가능성 검토 한정* + 적격성 *해소* 0건) — 실 변경 0건. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 15/15 풀 3+1 트리거 0건 발화 검증)**. **Layer C = Implementation Evidence PASS 발효** — 발효 조건 = (GP-3 5/5 + GP-5 5/5) 양 GP 모두 충족 + 사용자 명시 결정. **ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습 채택** ((a) 동등 이상의 보안 결과 / (b) 격리 환경 PoC 실증 / (c) ADR/SDD 권위 명시 / (d) 자동 회귀 검증 경로 / (e) 합의 APPROVE). **GP-3 + GP-5 양 GP × 5 조건 evidence 매트릭스 채택**: **GP-3 × 5/5 적격** (Group D 368줄 + Stage 2 ST-3 PoC 93줄 + ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + Layer B §5.5.1 (37번째 entry R-S1 정정 답습) + `secret-hygiene-egress-redaction.yml` 694줄 + GP-3 MVP-1 진입 합의 + Stage 2 합의 + Phase α-3 합의 — (a)~(d) 4/4 현 충족 + (e) Layer C 시점 발효) + **GP-5 × 5/5 적격** (Group A 1차/2차/3차 829줄+35줄 + ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + P2 v3 §10.1 + Layer B §5.5.2 + Group A 2차 풀 3+1 합의 + `provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 + GP-5 MVP-1 진입 합의 + Stage 4 합의 + Phase α-1/α-2/α-4 합의 — (a)~(d) 4/4 현 충족 + (e) Layer C 시점 발효) = **양 GP × 5 조건 = 10/10 evidence 적격성 권위 권고**. **4 prerequisite actual runs PASS 답습** (Stage 1 `25728590939` + Stage 2 `25731846625` + Stage 3 `25728590916` + `25728590977` 모두 SUCCESS). **Layer C 발효 합의 진입 적격성 5 조건 (C-ζ-1 ~ C-ζ-5) 5/5 충족 검증** + **15/15 풀 3+1 승격 트리거 0건 발화** + **18 Rollback Trigger 분류** (직접 영향 8 + 간접 영향 1 + 영향 0 9 — 발화 0건). **외부 LLM 1+ 요구사항 검토** — 권고 한정 (mvp1.md 본문 explicit 의무 명시 0건 + Group α C-11 답습 응답 = 입력 한정 + 사용자 명시 결정 영역). **합의 형태 권고 = Reviewer-only 단축 합의 적격 후보** (Phase α-1/2/3/4 패턴 답습, 사용자 명시 결정 시 풀 3+1 + 외부 LLM 1+ 옵션 권위 영역). **사용자 명시 7 금지 7/7 답습**: **실 Layer C 발효 = 0건** / **CI workflow 변경 = 0건** / **branch protection 변경 = 0건** / **dev 환경 강제 = 0건** / **`pre-commit install` 의무화 = 0건** / **Operational Readiness PASS (Layer E) = 0건** / **Hermes PMO 격상 (Layer F) = 0건**. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (Layer C = evidence verification = catalog / provider 영역과 직교) + **F-금지 #1 영구 답습 — GitHub Actions secrets 사용 도입 0건**. **Phase α-4 합의 (`e59a565`) 본문 변경 0건** + C-ε-1 ~ C-ε-29 자동 변경 0건 + **Phase α-3 합의 (`3f6306d`) / Phase α-2 합의 (`6a79247`) / Phase α-1 합의 (`1b3090b`) / Backlog #6 우선 진입 합의 (`c7ddfdd`) / Group α 합의 (`4880e88`) / Layer A / Layer B / §5.5 9 sub-수단 본문 채택 / GP-3 MVP-1 진입 / GP-3 Stage 2 / GP-5 MVP-1 진입 / Stage 4 / 5 Stage 분할안 / Group A 2차 풀 3+1 합의 본문 변경 0건** + **ADR-011 §2.1 (a)~(e) 5 조건 재정의 0건**. **추가 0건**: Layer C 실 발효 / GP-3 / GP-5 PASS 발효 / MVP-1 PASS (Layer D) 선언 / 양 GP × 5 조건 evidence 재생성 / 4 prerequisite actual runs 자동 재실행 / 신규 actual run 자동 trigger / 외부 LLM 자동 호출 / blind 의뢰 자동 발송 / R-4 (829줄) / R-5 (35줄) / R-7 (328줄) / R-1 (1593줄) 본문 어느 줄도 변경 (합산 2785줄 답습) / Phase α-1 / α-2 / α-3 / α-4 자동 재진입 / Phase β / γ 자동 진입 / 7 금지 영역 *해소* / Group I / Group β / γ-1 / γ-2 자동 진입 / Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 / token rotation 정책 자동 결정 / GitHub plan 가용성 자동 확인 / commit signing / `pull_request_target` workflow / Tier-2 / Tier-3 catalog 자동 확장 / threshold *고정* / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR / 신규 P / 신규 GP 발행 / 실 API key / provider SDK / 외부 API 호출 / 인간 리뷰 의무 자동 발화 / Hermes upstream Dockerfile 변경 / Production `docker-compose.yml` 변경 / 실 secret material commit / PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 / Layer 2 runtime block (G5-5) 진입 / `src/adapters/llm/facade.py` real 본문 작성 / MVP-2 ~ MVP-6 본문 deepening / 17 항목 우선순위 자동 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Layer C 발효 합의 실 진입 brief 작성 (실 Layer C 발효 단계 분할안) / (1') Layer C 발효 합의 풀 3+1 + 외부 LLM 1+ 진입 brief / (2) Phase α-4 실 진입 step 분할 brief / (3) Phase α-1 ~ α-4 통합 실제 구현 계획 brief / (4) Phase α-1 / α-2 / α-3 실 진입 step 분할 brief / (5) Group α 조건 재평가 / (6) Group I 별도 합의 / (7) token rotation 정책 별도 합의 / (8) GitHub plan 가용성 확인 / (9) 세션 종료. **이전 (2026-05-14 후속 14)**: Phase α-4 R-1 CI workflow 통합 진입 brief 작성 + Reviewer-only 단축 합의 발효 — APPROVE AS BRIEF + 3 commit chain (`f91ef4b` brief / `e59a565` 합의 / `569711a` 메타) — Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료.
docs/CONTEXT.md:114:**이전 후속 13 상세** (참고용 보존): 2026-05-14 후속 13 (**Phase α-3 R-7 docker secret block 진입 brief 작성 + Reviewer-only 단축 합의 발효 — APPROVE AS BRIEF + 3 commit chain**). 사용자 명시 진입 명령 답습 ("옵션 A로 진행해주세요" + Phase α-1 / α-2 패턴 답습 — brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실 R-7 docker secret block 수정은 아직 하지 않음). **3 commit chain**: (1) `8da3273 docs(phase0): add Phase alpha-3 R7 docker secret block entry brief` (748줄, 11 섹션 — DRAFT brief) / (2) `3f6306d docs(review): approve Phase alpha-3 R7 docker secret block entry` (562줄, 10 섹션 + Reviewer-only 단축 합의 APPROVE AS BRIEF + 28 합의 조건 C-δ-1~C-δ-28) / (3) 메타 commit (본 commit). **본 합의 영역** = **수단 결정 적격성 권위 권고 발행 한정** (Backlog #6 우선 진입 합의 §6.1 1순위 §5.2 α-3 답습 — Phase α-3 = R-7 docker secret block 영역 *진입 가능성 검토 한정* + 적격성 *해소* 0건) — 실 변경 0건. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 12/12 풀 3+1 트리거 0건 발화 검증)**. **R-7 = docker secret block 본문 정의 채택 권고**: 9 artifacts × 328줄 답습 — (1) `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` 34줄 (sub-step 2.1) / (2) `Dockerfile` 12줄 / (3) `app.py` 46줄 / (4) `secrets/api_key.placeholder` 1줄 (FAKE_TEST_SECRET marker) / (5) `tools/docker_secret_image_layer_check.sh` 99줄 (sub-step 2.2) / (6) `tools/docker_secret_restart_recovery.sh` 118줄 (sub-step 2.3) / (7) `tests/fixtures/gp3_st3/pass/Dockerfile` 9줄 / (8) `fail/Dockerfile` 8줄 / (9) `fail/baked_secret.txt` 1줄 — **본문 어느 줄도 변경 0건**. **ST-3 단독 답습 채택** (ST-1 entrypoint stat / ST-2 inotify sidecar 258줄 = Backlog #1 분리 / ST-4 Vault HSM = Backlog #7 + MVP-6 이후 / ST-5 Defense in depth = MVP-2 이후 분리). **Layer B §5.5.1 GP-3 4 sub-수단 中 ST-3 답습** (S-1 = R-4 영역 / PC-3 + AR-1 = Stage 4 영역 분리). **Phase α-3 진입 적격성 5 조건 (C-α3-1 ~ C-α3-5) 5/5 충족 검증** + **12/12 풀 3+1 승격 트리거 0건 발화** + **18 + 4 Rollback Trigger 분류** (Layer B 18 trigger: 직접 영향 2 + 간접 영향 1 + 영향 0 15 / ST-1/2/4/5 별도 backlog 4 trigger 분리) + **9 sub-step 분할 매트릭스**. **사용자 명시 7 금지 7/7 답습**: **실 R-7 docker secret block 수정 = 0건** / **CI workflow 변경 = 0건** / **branch protection 변경 = 0건** / **dev 환경 강제 = 0건** / **`pre-commit install` 의무화 = 0건** / **Operational Readiness PASS (Layer E) = 0건** / **Hermes PMO 격상 (Layer F) = 0건**. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (R-7 = file-system secret isolation Layer = catalog / provider 영역과 직교, docker secret = vendor-agnostic 표준) + **ADR-008 차단조건 #6 (Docker 격리) + 부록 B + ADR-011 답습 — Hermes upstream Dockerfile 변경 0건 (37번째 entry R-S1 정정 답습)**. **Phase α-2 합의 (`6a79247`) 본문 변경 0건** + C-γ-1 ~ C-γ-26 자동 변경 0건 + **Phase α-1 합의 (`1b3090b`) 본문 변경 0건** + C-β-1 ~ C-β-15 자동 변경 0건 + **Backlog #6 우선 진입 합의 (`c7ddfdd`) 본문 변경 0건** + C-α-1 ~ C-α-11 자동 변경 0건 + **GP-3 MVP-1 진입 합의 (`6dc5bdc`) 본문 변경 0건** + **GP-3 Stage 2 합의 본문 변경 0건** + Group α 합의 (`4880e88`) / Layer A (`f1e0b23`) / Layer B (`f40423f`) / §5.5.1 ST-3 본문 채택 (`55c5b4b`) / Layer D (`210c98f`) / `backlog6-runtime-ci-hook-priority-entry-brief.md` / `phase-alpha-1-r4-tools-body-entry-brief.md` / `phase-alpha-2-r5-importlinter-body-entry-brief.md` 본문 변경 0건. **추가 0건**: Phase α-3 실 진입 / Phase α-1 / α-2 / α-4 자동 진입 / Phase β / γ 자동 진입 / Backlog #6 실 진입 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 / R-MVP1-G3-3 자동 발화 / G3-7 자동 흡수 / 7 금지 영역 *해소* / Layer C 발효 / Layer D 재선언 / Layer E / Layer F 발효 / Group I / Group β / γ-1 / γ-2 자동 진입 / Backlog #1 / #2 / #4 / #5 / #7 자동 진입 / token rotation 정책 자동 결정 / GitHub plan 가용성 자동 확인 / commit signing 도입 / `pull_request_target` workflow / Tier-2 / Tier-3 catalog 자동 확장 / threshold *고정* / R-7 영역 9 artifacts 변경 / Production `docker-compose.yml` 변경 / Hermes upstream Dockerfile 변경 / 실 secret material commit / `secrets/.gitignore` 변경 / `secret-hygiene-egress-redaction.yml` Stage 2 entry step 변경 / R-4 도구 변경 / R-5 `.importlinter` 변경 / R-1 CI workflow 변경 / `.pre-commit-config.yaml` 본문 작성 / 실 hook 구현 / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR / 신규 P / 신규 GP 발행 / 외부 LLM 자동 호출 / 외부 LLM 응답 결론 강제 채택 / 실 API key / provider SDK / 외부 API 호출 / 실 docker build / docker run / docker history 자동 실행 / 인간 리뷰 의무 자동 발화 / MVP-2 ~ MVP-6 본문 deepening / Layer 2 runtime block (G5-5) 진입 / 17 항목 우선순위 자동 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-4 R-1 CI workflow 통합 brief / (2) Phase α 4 단계 통합 진입 brief / (3) Phase α-3 실 R-7 운영 단계 분할 brief / (4) Phase α-1 ~ α-3 병렬 실제 구현 계획 brief / (5) Phase α-1 R-4 / Phase α-2 R-5 실 진입 step 분할 brief / (6) Group α 조건 재평가 / (7) Group I 별도 합의 / (8) token rotation 정책 별도 합의 / (9) GitHub plan 가용성 확인 / (10) 세션 종료. **이전 (2026-05-14 후속 12)**: Phase α-2 R-5 `.importlinter` 본문 진입 brief 작성 + Reviewer-only 단축 합의 발효 — APPROVE AS BRIEF + 3 commit chain (`608a046` brief / `6a79247` 합의 / `877d4ef` 메타).
docs/CONTEXT.md:128:- **Group C 후속 후속 통합 PoC** (G4 Rewrite Defense Layer 2/3/4 — commits `f754511 → 95fc8aa`, GitHub Actions actual run `25631422222` SUCCESS): 산출물 8건 + fixture 17 files — `tools/rewrite_defense_check.py` (~340줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 / 실 git command 호출 0건 / 실 GitHub API 호출 0건 / 실 branch protection·git hook·signed commit 미진입) + 3 mode CLI (`--mode append-only` L2 / `--mode rewrite-command` L3 / `--mode line-regression` L4) + `--list-defenses` self-check (5 layers + dangerous command catalog 4 + line regression types 3 + 3 compliant flags) + Group C `jsonl_hash_chain.parse_jsonl` import 직접 답습 + commit history diff (L2 non_fast_forward + history_reorder) + dangerous command catalog 4 (rebase / filter-branch / reset-hard / push-force-or-amend) + line regression detector 3 types (line_deletion / line_rewrite / line_reorder) + violation reporter + fixture 17 files / 8 logical (L2 PASS append_only/pass + FAIL force_push + FAIL reorder / L3 PASS safe + FAIL rebase + FAIL filter_branch + FAIL reset_hard + FAIL push_force / L4 PASS head_extends_base + FAIL line_deletion + FAIL line_rewrite) + CI workflow `rewrite-defense.yml` 15 step (rfc8785+jcs install + artifact path = `group-cff-logs/` Group F 후속 답습) + 사양 (451줄 17 섹션) + Reviewer-only 단축 합의 (314줄). **로컬 10/10 + actual run 11/11 step PASS** (L2 PASS rc=0 + L2 FAIL rc=1 force-push 3 + reorder 1 cover / L3 PASS rc=0 + L3 FAIL rc=1 4 patterns cover (rebase + filter-branch + reset-hard + push-force-or-amend) / L4 PASS rc=0 + L4 FAIL rc=1 line_deletion 1 + line_rewrite 3 cover / `--list-defenses` 5 layers + 4 commands + 3 regression types + 3 compliant flag True / F-금지 grep 0/9). **10/10 PASS 기준 + 0/9 금지 위반 + 0/5 풀 3+1 trigger 발화 + ADR-011 §2.1 5/5 충족**. **본 PoC 핵심 evidence = ADR-012 §2.8 *Full Rewrite 5 Layer* 답습 5/5 완결 milestone** (Layer 1 Group C / Layer 2 + Layer 3 + Layer 4 본 PoC / Layer 5 Group C 후속). Layer 2/3/4 = *사전 차단* layer ; Layer 1/5 = *사후 검출* layer 책무 분리 시연. 7 attack 시나리오 cover (단일 entry 변조 / force-push / dangerous command 4 / line deletion / in-place rewrite / substitution / full rewrite). **알려진 한계 11건** (실 branch protection·git hook·CI base branch fetch 미진입 / 실 git command·repo rewrite·GitHub API 호출 미진입 / `git filter-repo` Tier-2 / `git reset --soft/--mixed` Tier-2 / Reflog 통합 미진입 / Commit signature verification Layer 5 영역 / 1인 동일 호스트 SPOF ADR-012 §2.8 답습 / markdown 본문 자기 검출 — 모두 분리 영역 명시). **G4 *Layer 2/3/4 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + 실 branch protection·git hook·signed commit·external service 미진입**.
docs/CONTEXT.md:134:- **Group C 후속 통합 PoC** (G4 History Rewrite Layer 5 External Anchor Verifier — commits `fd25cbe → cfc48ae`, GitHub Actions actual run `25630561391` SUCCESS): 산출물 8건 — `tools/history_anchor_verifier.py` (~310줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 / signed commit·branch protection·external timestamping 미진입) + 2 mode CLI (`--mode chain-only` Layer 1 baseline 답습 / `--mode anchor-verify` Layer 5 검출) + `--list-attack-models` self-check (5 attack scenarios + 11 anchor fields + Layer 1 inadequacy demo supported) + Group C `jsonl_hash_chain` import 직접 (`parse_jsonl` + `validate_chain` + `compute_entry_hash` + `compute_genesis_hash` + ENUMs) + 11-field anchor schema validation (anchor_id/anchor_ts/anchor_method/ledger_path/expected_entry_count/expected_tail_hash/expected_genesis_hash/schema_version/external_run_id/external_run_url/notes) + 5 attack model 검출 (full_rewrite / tail_truncation / middle_deletion / substitution / anchor_tampered) + appended_only mode (Layer 5 정상 운영 시제) + violation reporter + fixture 10건 (PASS 4 = original_ledger + anchor + extended_ledger + anchor / FAIL 5 = 4 ledger 변조 + 1 anchor 변조 / chain_only_demo 1 = Layer 1 inadequacy demo) + CI workflow 16 step (rfc8785+jcs install + artifact path = `group-c-followup-logs/` Group F 후속 답습) + 사양 (410줄 14 섹션) + Reviewer-only 단축 합의 (323줄). **로컬 10/10 + actual run 10/10 PASS** (Anchor PASS×2 + FAIL×5 + Layer 1 inadequacy demo + list-attack-models + F-금지 grep). artifact 19 파일 정상 업로드 (18 logs + summary.json, 6265 bytes, 30일 retention). **10/10 PASS 기준 + 0/7 금지 위반 + 0/5 풀 3+1 trigger 발화 + ADR-011 §2.1 5/5 충족**. **본 PoC 핵심 evidence = Layer 1 inadequacy demo** (chain-only mode 시 full rewrite *의도된 PASS* 처리됨 → ADR-012 §2.8 5 Layer 中 Layer 5 anchor 의무성 직접 시연). **알려진 한계 11건** (Layer 2/3/4 미진입 / `anchor_method` `signed_tag`+`external_snapshot` 미진입 / Anchor metadata 자체 signing 미진입 / 실 GitHub API 호출 미진입 / Anchor nightly cron 미진입 / Multi-host external service 미진입 / 1인 동일 호스트 SPOF 한계 ADR-012 §2.8 답습 / markdown 자기 검출 / Group G hermes-originated anchor 책무 분리 / signed_tag/external_snapshot 부재 / RFC 3161 미통합 — 모두 분리 영역 명시). **G4 *Layer 5 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Layer 2~4 미진입 + signed commit·branch protection·external service 미진입**.
docs/CONTEXT.md:136:- **Group A 3차 통합 PoC** (G2 GP-5 Layer 1c URL endpoint + model name 직접 사용 차단 — commits `2a2c986 → bbc9684`, GitHub Actions actual run `25629390384` SUCCESS 6초 16/16 step ✓): 산출물 8건 — `tools/provider_url_scanner.py` (~210줄, **stdlib `re` + `dataclasses` 단독** 외부 의존 0건 / gitleaks·depcruise·AST 통합 미진입) + 2 mode CLI (`--mode url-endpoint` E-1 / `--mode model-name` E-2) + `--list-catalogs` self-check + URL Tier-1 catalog 10 (Anthropic/OpenAI/Azure-OpenAI/Google-AI/Replicate/Perplexity/Cohere/HuggingFace/Together/OpenRouter) + Model Tier-1 catalog 19 (Anthropic 5 + OpenAI 5 + Google 3 + Meta 3 + Mistral 3) + extension allowlist (URL: 8 ext / Model: 5 ext = §9.3 "yaml만 허용" 답습) + comment line 부분 회피 (`#` / `//`) + fixture 9건 (E-1 PASS 1 = `safe_config.yaml` (yaml allowlist 통과) + FAIL 3 = anthropic/openai/google / E-2 PASS 1 = `safe_model_config.yaml` (yaml allowlist 통과) + FAIL 4 = anthropic/openai/gemini/llama) + CI workflow 12 step (artifact path = `group-a3-logs/` Group F 후속 답습) + 사양 (387줄 14 섹션) + Reviewer-only 단축 합의 (310줄). **로컬 6/6 + actual run 6/6 PASS** (E-1 PASS rc=0 + E-1 FAIL rc=1 4 violations + 4 pattern_ids cover (anthropic/azure-openai/google-ai/openai) + E-2 PASS rc=0 + E-2 FAIL rc=1 13 violations + **11 pattern_ids cover (4 vendor 모두)** + `--list-catalogs` url=10 model=19 allowlist=8/5 + 3 compliant flag True + F-금지 grep 0/8). artifact 11 파일 정상 업로드 (10 logs + summary.json, 3299 bytes, 30일 retention). **6/6 PASS 기준 + 0/8 금지 위반 + 0/6 풀 3+1 trigger 발화 + ADR-011 §2.1 5/5 충족**. **Group A 2차 합의 §5.5 #C-8 답습 의무 충족 — *3차 분리 영역* 책무 해소** (Layer 1c 모법 답습). **알려진 한계 11건** (depcruise rule 통합 / pre-commit hook / PR auto-reject / 의미적 분석 / Multi-line block comment 완전 회피 / docstring 완전 회피 / Tier-2 vendor / 모델 ID 세부 version / URL fragment Group D 분리 / 실 src 적용 FP / markdown 본문 자기 검출 — 모두 분리 영역 명시). **G2 GP-5 *Layer 1c 정적 검출 시제* 한정 — G2 GP-5 / G2 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Tier-2/3 catalog 확장 0건**. **Layer 1a/1b/1c 분리 답습 완결** (Group A 1차 = 1a AST 5종 / Group A 2차 = 1b transitive import / 본 PoC = 1c URL+model name).
docs/CONTEXT.md:138:- **Group G 통합 PoC** (G3 Skill escalation + 합의 자기참조 차단 + G4 Memory/Skill boundary 4 금지 — commits `0cd03c9 → da48ba5`, GitHub Actions actual run `25626591894` SUCCESS 5초 17/17 step ✓): 산출물 8건 — `tools/boundary_guard.py` (~445줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 / runtime hook 0건 / Docker SDK·git2·pyyaml 미도입) + 3 mode CLI (`--mode skill-escalation` G-1 G3 §3.3 / `--mode consensus-self-reference` G-2 G3 §4 / `--mode memory-skill-boundary` G-3 G4 §5.2) + `--list-boundaries` self-check (4 boundaries + 3 modes + 13 합의 매트릭스 row) + Group C `jsonl_hash_chain` (`validate_schema` + ENUMs `ALLOWED_TYPES`/`ALLOWED_AGENTS`/`ALLOWED_SCOPES`) import 직접 + Group E `schema_validator` (`ALLOWED_ACTIONS_ENUM` + `parse_yaml_v2`) import 직접 + Group B Hermes-originated marker 6 패턴 답습 + governance PASS anchor 9 + reviewer/외부 LLM marker + Hermes PMO/policy decision 3 + policy expression 6 + scope transition 검출 + agent=hermes × event 매트릭스 + fixture 9건 (G-1 PASS 1 = `valid_skill_within_allowed.yaml` Group E 답습 + FAIL 2 = yaml-invalid-action + audit-log-escalation / G-2 PASS 1 = proper_reviewer_consensus + FAIL 2 = hermes-self-consensus + hermes-pmo-self-promotion / G-3 PASS 1 = `safe_memory_skill_chain.jsonl` Group F skill_project.jsonl 직접 답습 + FAIL 3 = memory-replaces-policy + session-to-global + hermes-self-approves) + CI workflow 13 step (artifact path = `group-g-logs/` Group F 후속 답습) + 사양 (399줄 14 섹션) + Reviewer-only 단축 합의 (350줄). **로컬 8/8 + actual run 7/7 PASS** (G-1/G-2/G-3 PASS rc=0 + FAIL rc=1 + 7 pattern_ids cover (yaml-invalid-action/audit-log-escalation/hermes-self-consensus/hermes-pmo-self-promotion/memory-replaces-policy/session-to-global/hermes-self-approves) + `--list-boundaries` total_boundaries=4 + total_modes=3 + consensus_matrix_rows=13 + boundary_4_rules_compliant=True + F-금지 grep 0건). artifact 15 파일 정상 업로드 (14 logs + summary.json, 4537 bytes, 30일 retention). **8/8 PASS 기준 + 0/11 금지 위반 + 0/6 풀 3+1 trigger 발화 + ADR-011 §2.1 5/5 충족**. **알려진 한계 15건** (Skill wrapper runtime / Docker cap_drop / sandbox syscall / escalation 자동 비활성화 runtime / 실 git commit author / 외부 LLM 자동 호출 / PR auto-reject / Memory write blocker runtime / promotion hook 차단 runtime / P12 정식 등록 / G3 22 권한 분해 (Group I) / Hermes PMO 격상 자동화 / G4 §5.2 #2 단독 fixture (G-1 통합 답습) / 도구 도입 / markdown 본문 자기 검출 — 모두 분리 영역 명시). **G3 + G4 *형식적 검출 layer 시제* 한정 — G3 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + runtime hook 0건 + 실 git commit author 검사 0건 + 외부 LLM 자동 호출 0건**.
docs/CONTEXT.md:140:- **Group E 통합 PoC** (G2 GP-4 External Input Validation + G4 Memory/Skill schema validation — commits `8f96009 → 8176235`, GitHub Actions actual run `25624970577` SUCCESS 10초 16/16 step ✓): 산출물 8건 — `tools/schema_validator.py` (~520줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 / pydantic·jsonschema·pyyaml 미도입) + 2 mode CLI (`--mode external-input` E-1 GP-4 / `--mode skill-schema` E-2 G4) + `--list-skill-fields` self-check + 17-field 정의 (G4 §3.1 직접 복사 변경 0건) + 11-field 검증 (`jsonl_hash_chain.validate_schema` import 직접 Group C 답습) + injection canary 26 patterns (12 prompt-injection + 8 unauthorized-policy + 6 injection-payload) + ENUM (allowed_actions 7 / promotion_status 5 / scope 4) + transition 매트릭스 (G4 §3.3 답습) + provider lock-in marker (`required: true` / `exclusive: true`) + custom YAML mini-parser (stdlib 단독) + fixture 9건 (E-1 PASS 1 = `safe_worker_output.json` + E-1 FAIL 4 = prompt_injection / unauthorized_policy / malformed_json / injection_payload + E-2 PASS 1 = `valid_skill.yaml` Group F skill_project.jsonl 17-field content YAML 재구성 답습 + E-2 FAIL 4 = missing_required / invalid_action / invalid_promotion_status / provider_lockin) + CI workflow `schema-validation.yml` (12 step, artifact path = `group-e-logs/` Group F 후속 답습) + 사양 (495줄 14 섹션) + Reviewer-only 단축 합의 (310줄). **로컬 6/6 + actual run 6/6 PASS** (E-1 PASS rc=0 + E-1 FAIL rc=1 22 violations 4 카테고리 cover + E-2 PASS rc=0 17/17 fields 통과 + E-2 FAIL rc=1 16 violations 4 pattern_ids cover + 17-field count total=17 required=12 mvp_recommended=5 + F-금지 grep 0건). artifact 11 파일 정상 업로드 (10 logs + summary.json, 3691 bytes, 30일 retention). **6/6 PASS 기준 + 0/10 금지 위반 + 0/6 풀 3+1 trigger 발화 + ADR-011 §2.1 5/5 충족**. **알려진 한계 11건** (Memory boundary 4 금지 runtime 강제 / Skill wrapper escalation 차단 / 재귀 JSON Schema 의미 검증 / Reviewer Agent 추론 layer / runtime escape 통합 / 실 LLM API 호출 / pydantic·jsonschema 도구 / pyyaml / P9~P12 정식 등록 / provider_bindings lint 룰 / markdown 본문 자기 검출 — 모두 Group G 또는 별도 합의 영역 분리). **G2 GP-4 / G4 *형식적 검증 layer 시제* 한정 — G2 GP-4 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Memory boundary hook 0건 + Skill wrapper 0건**.
docs/CONTEXT.md:142:- **Group D 통합 PoC** (G2 GP-3 + GP-2 — commits `1719a01 → 3a8c8d5`, GitHub Actions actual run `25623028888` SUCCESS): 산출물 8건 — `tools/secret_scanner.py` (261줄, **R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습** — Prefix 36 + regex 7 + alternation 2, 변경 0건 / 외부 의존 0건 / gitleaks·detect-secrets 미도입) + 2 mode CLI (`--mode scan-source` D-1 / `--mode scan-log` D-2) + `--list-patterns` self-check + `is_redaction_marker_match()` (scan-log 전용 FP 회피) + fixture 9건 (PASS 2 + FAIL 4 + REDACTION_PASS 1 + REDACTION_FAIL 2, fake canary 의무 답습) + CI workflow `secret-hygiene-egress-redaction.yml` (12 step, artifact path = `group-d-logs/` Group F 후속 답습) + 사양 (`docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` 351줄, 12 섹션) + Reviewer-only 단축 합의 (291줄). **로컬 6/6 + actual run 6/6 PASS** (D-1 PASS rc=0 + D-1 FAIL rc=1 14 violations 4 패턴 cover incl. private-key T1-035 + D-2 PASS rc=0 + D-2 FAIL rc=1 partial leak 검출 + Tier-1 count 45 + F-금지 grep 0건). artifact 11 파일 (10 logs + summary.json, 3817 bytes, 30일 retention). **F-범위 5/5 + 12 금지 0/12 위반 + 풀 3+1 trigger 0/7 발화 + ADR-011 §2.1 5/5 + PASS 기준 7/7 충족**. **알려진 한계 11건** (#1 base64 evasion = Hermes upstream R2-6 영역 / #2~#8 책무 분리 / #9~#11 markdown 자기 검출 등). **G2 GP-2 / GP-3 *형식적 검출 layer 시제* 한정 — G2 GP-2 / GP-3 / G2 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Tier-2/3 catalog 확장 0건 + 실 API key / provider SDK / 외부 API 호출 0건**.
docs/CONTEXT.md:146:- **Group F 통합 PoC** (G2 GP-6 Memory/Skill Migration *Feasibility* — commits `c675e98 → 8acbe18`, GitHub Actions actual run `25620376305` SUCCESS 14초 16/16 step ✓): 산출물 8건 — `tools/memory_skill_roundtrip.py` (245줄, Group C 3 모듈 `canonical_json` + `jsonl_hash_chain` + `jsonl_roundtrip` **import 직접** + 토이 매핑 3 함수 (`hermes_to_canonical` / `canonical_to_claude` / `claude_to_canonical`) + `--feasibility-mode hermes-to-claude` CLI + `build_feasibility_lossy_entry` ledger entry 자동) + fixture 4건 (PASS Memory + PASS Skill 17 필드 + LOSSY hermes_to_claude with `_hermes_internal_id` + FAIL chain_violation `prev_hash_mismatch`) + CI workflow `.github/workflows/memory-skill-migration-feasibility.yml` (12 step) + 사양 (`docs/phase0/g2-gp6-memory-skill-migration-feasibility-poc.md` 315줄, 11 섹션) + Reviewer-only 단축 합의 (`docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md` 315줄). **로컬 4/4 + GitHub Actions 4/4 PASS** (Memory PASS rc=0 + Skill PASS rc=0 + LOSSY rc=1 + lost_fields=2 + FAIL rc=2 + chain_violation_detected). **F-범위 10/10 + F-금지 0/9 위반 + 풀 3+1 승격 trigger 0/6 발화 + ADR-011 §2.1 5/5 + PASS 기준 9/9 충족**. **F-사전 결정 1순위 충족** = 공유 모듈 import 직접 (리팩토링 0건 / 복제 0건 / 신규 ~80줄). **알려진 한계 8건** (특히 #8 — actual run 발견: artifact upload empty, `.group-f-logs/` hidden dir + `include-hidden-files: false` default. 검증 영향 0건, evidence 는 CI run log + `$GITHUB_STEP_SUMMARY` + summary.json stdout 보존. 후속 수정 후보 = (A) `include-hidden-files: true` / (B) `.group-f-logs/` → `group-f-logs/` rename — 사용자 권고 = B, 본 세션 미수정 후속 작업 등록). **G2 GP-6 *feasibility 시제* 한정 — G2 GP-6 / G2 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + 실 migration script 0건 + 실 provider SDK 호출 0건**.
docs/CONTEXT.md:243:- **`docs/decisions/ADR-011-means-vs-ends-redaction.md` (R-3 신규 — 수단/목적 분리 원칙, R-4~R-7 모법)**
docs/CONTEXT.md:246:- **`docs/architecture/redaction-pattern-equivalence.md` (R-4 — 패턴 동등성 비교 + gap 식별 + 보충 권고, ADR-011 §2.1 (a) 충족)**
docs/CONTEXT.md:247:- **`docs/phase0/r4-1-trigger-extension-evidence.md` (R-4.1 — Tier-1 42종 trigger UDF 확장 PoC PASS evidence, ADR-011 §2.1 (b) 충족)**
docs/CONTEXT.md:249:- **`docs/architecture/canary-recheck-design.md` (R-5 — canary 재검증 트리거 설계, ADR-011 §2.4 운영 메커니즘)**
docs/CONTEXT.md:250:- **`.github/workflows/r2-canary.yml` (R-6 — CI/nightly canary regression workflow, ADR-011 §2.1 (d) 자동 회귀 검증 경로)**
docs/CONTEXT.md:279:- **권위 위계**: `Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents` — **ADR-011 §2.3 영구 권위화**
docs/CONTEXT.md:280:- **Hermes ≠ root of trust** — **ADR-011 §2.3 영구 권위화** (prequel §3 → ADR 승격, prequel 폐기 후에도 보존)
docs/CONTEXT.md:281:- **자동 학습 ≠ 자동 정책 변경** (T1 자동 / T2 사용자 승인 / T3 절대 금지) — **ADR-011 §2.4 영구 권위화**
docs/CONTEXT.md:282:- **수단/목적 분리 원칙** — **ADR-011 §2.1 신설** (헌법 8조 본질 = "DB 평문 저장 차단 결과", 수단 대체에 (a)~(d) 4조건 강제)
docs/CONTEXT.md:312:| ~~G1a~~ | Hermes native redaction → DB | ❌ FAIL 확정 (폐기) — **ADR-011 §2.2 / ADR-008 부록 B 권위 명시** |
docs/CONTEXT.md:315:| **G3** | **"Hermes ≠ root of trust" 운영 구현** | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-07 원 합의 + 2026-05-09 후속 reaffirmation + 2026-05-12 Gate Enforcement Layer 보호 보강)** — `hermes-not-root-of-trust-runtime.md` 헤더 갱신 + 통합 합의 보고서 (2026-05-07 4/4 만장일치) + 후속 합의 보고서. ADR-011 §2.3 권위 확정 + G3 §1~§7 설계 승인 + §2.4 산술 오류 정정 (14/22 → 15/22, 통합 합의 C-11) + **2026-05-12 §2.6 신설 (10 보호 항목 + Gate 자체 5 기준 + Layer 0~6 5 기준 + 위협 모델 TM-1~TM-8 + 강제 메커니즘 매트릭스 + Rollback Trigger 발화 매트릭스 + G4 인터페이스) / §10 변경 절차 row 추가 / §11.4 신설 (Gate Enforcement Layer 보호 보강 작업 흡수 기록 10 항목 RESOLVED)**. **운영 구현 = DESIGN PASS / IMPLEMENTATION PENDING**. 외부 LLM 1+ 충족 (2026-05-07 GPT-5.5 Thinking + 2026-05-09 후속 GPT cross-vendor + Claude 인접 컨텍스트) |
docs/CONTEXT.md:316:| **G4** | **Provider-agnostic Memory/Skill 형식** | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-07 원 합의 + 2026-05-09 후속 reaffirmation + 2026-05-11 P-1/P-2/P-3 본문 흡수 RESOLVED + 2026-05-11 Permission Granularity 세분화 보강 + 2026-05-12 Gate Enforcement Layer 보호 cross-reference)** — `provider-agnostic-memory-skill-design.md` 헤더 갱신 + 통합 합의 보고서 + 후속 합의 보고서 + 2026-05-11 §4.4 헤더 / §10.2 신설 / §4.5.3 신설 / §11.4 RESOLVED 표기 + 2026-05-11 §3.7 신설 (12 카테고리 T1/T2/T3 매트릭스) / §3.8 신설 (Self-Permission Escalation + Revocation Chain) / §11.5 신설 (Permission Granularity 작업 흡수 기록 7 항목 RESOLVED) + **2026-05-12 §3.7 헤더 (T3 7→8 / 12→13 카테고리) / §3.7.3 #18 신설 (`GATE_ENFORCEMENT_LAYER_MODIFY` T3 cross-reference) / §3.7.4 권위 한계 / §3.8.2 #10 신설 (`gate_enforcement_bypass_detected` rollback_trigger cross-reference) / §3.8.2 헤더 (9→10) / §3.8.3 권위 한계 / §6.1 매트릭스 row + 인터페이스 본문 (3-layer → 4-layer Permission Defense + Gate Enforcement Layer) / §11.6 신설 (Gate Enforcement Layer 보호 cross-reference 흡수 기록 4 영역 RESOLVED) / 헤더 부속 명시**. **라운드트립 + migration script + Skill wrapper runtime + Schema validator runtime + rollback_trigger 자동 검출 runtime + Memory write boundary runtime + Gate Enforcement Layer 자동 차단 runtime = DESIGN PASS / IMPLEMENTATION PENDING**. hash chain 사양 보강 + provider_bindings lint 룰 강제 + 실 import / migration runtime 코드 + 실 permission validator / wrapper / revoke runtime + 실 Gate enforcement filesystem ACL / pre-commit hook / CI step 모두 별도 합의 (Implementation/Runtime PASS 영역) |
docs/CONTEXT.md:322:- ✅ **R-3 (2026-05-06): ADR-011 발행 + ADR-008 부록 B Amendment, 단축 합의 APPROVE**
docs/CONTEXT.md:323:- ✅ **R-4 (2026-05-06): 패턴 동등성 비교 + gap 식별 + 보충 권고 (ADR-011 §2.1 (a) 충족)**
docs/CONTEXT.md:324:- ✅ **R-4.1 (2026-05-06): Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS (ADR-011 §2.1 (b) 충족, 1차 PARTIAL → 2차 PASS 진화)**
docs/CONTEXT.md:345:13. ~~**system-identity-prequel.md Archive 적격성 검토 + Archive 전환**~~ ✅ 완료 (2026-05-09 후속 8, 단축 합의 APPROVE Reviewer-only — 8/8 검토 기준 PASS + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 A 채택. system-identity-prequel.md 헤더 = Archived. 16 영역 이관 매트릭스 (12 완전 흡수 + 4 부분/분산) + AI Dev Company OS 정체성 보존 HIGH (§2 본문 영구 보존) + prequel §1.2 자체 archive 예고 정합. ADR-011 §2.3 / §2.4 영구 권위 승격 + ADR-012 §6.4 트리거 실현 답습)
docs/CONTEXT.md:346:14. ~~**ADR-008 / 010 / 011 본문 갱신 PR 묶음 *범위 결정* 검토**~~ ✅ 완료 (2026-05-09 후속 9, 단축 합의 APPROVE Reviewer-only — 6 항목 분류 + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 1 (3 ADR 단일 PR 묶음) 권고. 25 cross-reference 갱신 항목 (A1~A25 — ADR-008 9 + ADR-010 4 + ADR-011 12). **본 검토 = 범위 결정만, 본문 수정 X**. 결정 내용 변경 0건 (Option B / Vault HSM / 수단/목적 분리 모두 변경 없음). 다음 진입점: 본 검토 APPROVE 후 별도 PR/commit 으로 ADR 본문 갱신)
docs/CONTEXT.md:347:15. ~~**ADR-008 / 010 / 011 본문 갱신 단일 PR 묶음 commit**~~ ✅ 완료 (2026-05-09 후속 10, 옵션 1 답습 — 25 cross-reference 갱신 항목 (A1~A25) 모두 반영. ADR-008 §관련 문서 9 항목 (P2 v2 Archived / P2 v3 Adopted / ADR-009 C-N / ADR-011 / ADR-012 / G2/G3/G4 / 차단조건 #2 #4 / 부록 B §B.6) + ADR-010 §맥락 + §관련 문서 4 항목 (P2 v2 Archived / P2 v3 Adopted / ADR-012 / Evidence Ledger DB secret 처리 주의 사항) + ADR-011 §8.1/§8.2/§8.5 12 항목 (prequel Archived / P2 v2 Archived / P2 v3 Adopted / R-4~R-7 ✅ 완료 / G1b PASS / G2/G3/G4 PASS / ADR-012 / ADR-009 C-N / G2 §1.2.6 P10 / P2 v3 / Archive / 본 후속 9 등록). 결정 내용 변경 0건 + 6 풀 3+1 승격 트리거 0건 발화 (재확인) + 6 금지 사항 위반 0건)
docs/CONTEXT.md:348:16. ~~**G2 / G3 / G4 헤더 P2 v3 cross-reference 갱신 단축 PR**~~ ✅ 완료 (2026-05-09 후속 11, 3 게이트 헤더 영역 cross-reference 보강 — G2 = §1.2.6 P10 정식 등록 + P2 v3 §4 답습 권위 + 후속 권위 표기. G3 = Hermes 변조 차단 매트릭스 4항목 (ADR-012 §2.12 답습) + P2 v3 §5 답습 권위 + ADR-011 §2.3/§2.4 영구 권위 명시. G4 = ADR-012 Mandatory Reference + Provider Liquidity 5-way Layer 매트릭스 + ADR-009 C-N §5 모법 ADR + P2 v3 §6 답습. Design/Governance PASS ↔ Implementation Pending 분리 강화. 5 풀 3+1 승격 트리거 0건 발화 (Design vs Implementation 분리 / PMO 격상 오해 / P2 v3 의미 변경 / ADR 충돌 / 5 제약 약화). 헤더 본문 변경 0건 — cross-reference 갱신만)
docs/CONTEXT.md:351:19. ~~**ADR-010 / ADR-011 후속 보강 필요 여부 확인**~~ ✅ 완료 (2026-05-09 후속 14, 단축 합의 APPROVE Reviewer-only — **분기 A 채택: 추가 보강 *불필요***. ADR-010 5/5 항목 충족 (Evidence Ledger DB 보호 범위 / secret 처리 / key rotation·backup·export 충돌 0건 / 책임 경계 매트릭스 명확 / Implementation PASS 오해 0건) + ADR-011 5/5 항목 충족 (수단/목적 분리 최신 / 권위 위계 archive 후 명확 / T1/T2/T3 충돌 0건 / Hermes PMO 격상 절차 연결 / 자동 정책 변경 금지 5 layer 다중 차단 강제) + 6/6 풀 3+1 승격 트리거 0건 발화. **본 검토 = 보강 필요 여부 검토만, 본문 수정 X**. **Implementation/Runtime PASS 작업 진입 적격**)
docs/CONTEXT.md:352:20. ~~**Implementation/Runtime PASS Roadmap 작성**~~ ✅ 완료 (2026-05-09 후속 15, 단축 합의 APPROVE Reviewer-only — `implementation-runtime-roadmap.md` DRAFT 권위 권고 발행. 17 항목 분해 (G2 5 + G3 5 + G4 7) + 9 그룹 동시 진행 분류 + 사용자 명시 8 우선순위 유지 + Claude 추가 3 항목 (Order 9~11). ADR-011 §2.1 (a)~(e) 5조건 답습 + Rollback Trigger 9 + Evidence 5 형식. 5/5 풀 3+1 승격 트리거 0건 발화. 그룹 A~G = 단축 합의 / 그룹 H (ADR-014 발행) + I (G3 22 권한 분해) = 풀 3+1 + 외부 LLM 1+ 의무. **roadmap 우선순위 자동 *고정* 0건**)
docs/CONTEXT.md:353:21. ~~**Group A 1차 PoC — AST scanner 기반 Layer 1 형식 차단**~~ ✅ 완료 (2026-05-09 후속, Group A 진입, commits `a3693a0` + `0f503a4`. `tools/provider_import_scanner.py` (~165줄, 5종 패턴 — direct/from/dynamic-importlib/__import__/model-name) + fixture 6건 (PASS × 1 + FAIL × 5) + CI workflow 양방향 검증 + Reviewer-only 단축 합의 APPROVE WITH CONDITIONS. 양방향 검증 5/5 패턴 정확 매칭. ADR-011 §2.1 5/5 + 6 금지목록 0/6 위반)
docs/CONTEXT.md:357:25. ~~**Group B 통합 PoC — G3 Hermes-originated marker + Evidence 없는 PASS 차단**~~ ✅ 완료 (2026-05-10, commits `ecf9da3` + `4872a11` + `df4de14`. GitHub Actions actual run `25605665191` PASS 8초 conclusion=success. `tools/evidence_pass_gate.py` 3 검사 (Hermes marker × governance 공동 / PASS × evidence / Implementation PASS scope 분리) + fixture (PASS × 2 + FAIL × 4, 3 패턴 cover) + CI workflow (PASS rc=0 / FAIL rc=1 ≥4 + 3 패턴 cover step + Evidence summary 6 항목) + 사양 + Reviewer-only 단축 합의 APPROVE WITH CONDITIONS. 양방향 검증 5/5 PASS (로컬 + actual run, FP 0 / FN 0). ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 8 PASS / 6 BLOCK / 7 금지 0/7 위반 + TR-B-1~TR-B-4 0/4 발화 + Group A 답습 충실 + 알려진 한계 4건 명시. 본 PoC = G3 *부분 충족 시제* 한정 (G3 전체 PASS 권한 0건))
docs/CONTEXT.md:359:28. ~~**G4 Permission Granularity 세분화 작업**~~ ✅ 완료 (2026-05-11, P-1/P-2/P-3 push 후속, 사용자 명시 7 항목 답습. `provider-agnostic-memory-skill-design.md` §3.1 / §3.2 #9 #10 / §3.4.2 신설 / §3.4.3 신설 / §3.7 신설 / §3.8 신설 / §6.1 갱신 / §11.5 신설. **§3.7 12 카테고리 semantic enum** — coarse 7 종 (`read` / `write` / `shell` / `network` / `db` / `git` / `docker`) → **12 카테고리** (T1 5 = READ_ONLY / SUGGEST_ONLY / WRITE_DRAFT / WRITE_DOCS 일부 / RUN_TESTS 일부 + T2 5 = WRITE_CODE / RUN_LOCAL_TOOLS / NETWORK_ACCESS / PROVIDER_SPECIFIC_OPTIMIZATION / SKILL_PROMOTION + T3 7 = SECRET_ACCESS / POLICY_CHANGE / ADR_CHANGE 자동수행 / SELF_PROMOTION / PROVIDER_LOCK_IN_ENFORCE / REDACTION_POLICY_RELAX / CONSTITUTION_BYPASS). **§3.2 #10 forbidden_actions T3 자동 포함 강제 + 사용자 명시 override 불가** (T3 영역, ADR-011 §2.4). **§3.4.2 promotion_status × 권한 범위 매트릭스** — proposed=T1 only / approved=T1+T2 일부 / promoted=T1+T2 전체 / revoked·archived=READ_ONLY only. **§3.4.3 `promoted` 진입 5/5 검증 조건** — required_evidence 전체 + required_tests 전체 + schema 통과 + §3.8 self-escalation 통과 + Evidence ledger entry append. **§3.8.1 Self-Permission Escalation 6 차단 메커니즘** — 자기 본문 수정 / 권한 확장 patch / Forbidden override / 자기 promotion / Memory 우회 / Skill chain 우회. **§3.8.2 Rollback Triggers 9 종 × 자동 revoke 매트릭스 + Revocation Chain 자동 전이** (escalation_detected / evidence_missing / t3_violation / test_failure / secret_leak_detected / provider_lockin_detected / consensus_self_reference_detected / chain_violation_detected / policy_drift_detected). **§6.1 G3 인터페이스 3-layer Permission Defense** — Layer 1 schema-level (§3.7 + §3.2 #9/#10) + Layer 2 self-escalation (§3.8.1 + §3.8.2) + Layer 3 runtime (G3 §3.3). **§11.5 7 항목 흡수 매트릭스 RESOLVED** (allowed_actions 권한 category 분류 / forbidden_actions T3 명시 / provider_bindings lock-in 제한 / promotion_status 별 권한 범위 / self-escalation 차단 / required_evidence·required_tests 강화 / rollback_triggers ↔ permission revocation 연결). **0/N 위반 검증 7/7** (runtime code 구현 0건 / migration script 0건 / Hermes PMO 격상 0건 / Operational Readiness PASS 0건 / Implementation/Runtime PASS 0건 / G4 전체 PASS 재선언 0건 / ADR 본문 갱신 0건). **합의 형태 = 단축 합의 (Reviewer-only) 적격 영역** — §10.1 §2~§4 본문 갱신 + §3.1 17 필드 schema 본문 갱신 영역. 별도 단축 합의 보고서 작성은 후속 사용자 명시 결정 영역)
docs/CONTEXT.md:365:34. ~~**Condition C-4 흡수 — MVP-1 roadmap §5.4 GP-3 + GP-5 Integrated Risk Matrix 신설** (Observation O-2 흡수)~~ ✅ 완료 (2026-05-12 후속 6, 사용자 명시 진입 명령 답습 — "MVP-1 roadmap §5.4 통합 위험 sub-section 신설"). `implementation-runtime-roadmap-mvp1.md` §5.4 신설 + §5.2 cross-reference 갱신 + §9 변경 이력 1행 추가 (110 line 추가, 632 → 741 line). **3 통합 위험** (IR-1 Provider key adapter bypass / IR-2 Direct SDK + secret leakage 결합 / IR-3 Local/CI/Docker mismatch) + **3 신규 evidence enum 후보** (`provider_key_adapter_bypass_risk_detected` / `direct_sdk_with_secret_leakage_detected` / `secret_handling_environment_mismatch_detected`) + **MVP-1 Handling vs Deferred Handling 분리** + **§5.4.4 *범위 한계*** (실 combined check 도구 0건 / enum 정식 등록 0건 / Runtime enforcement 0건 / Operational parity 0건 / Provider key auto revoke 0건 / Combined fail PR auto-reject 0건). 본 흡수 *범위 한계* = §5.4 신설 + §5.2 cross-reference + 변경 이력 한정 — §3 / §4 / §5.1 / §5.3 / §6 / §7 본문 변경 0건. **0/N 위반 검증 8/8** (runtime code 0 / CI-hook 0 / 실 scanner 0 / GP-3 PASS 0 / GP-5 PASS 0 / MVP-1 PASS 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0))
docs/CONTEXT.md:373:30. ~~**MVP-1 roadmap Reviewer-only 단축 합의 보고서 작성**~~ ✅ 완료 (2026-05-12 후속 2, 사용자 명시 진입 명령 답습. `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` 신설 (393줄). 검토 대상 = `implementation-runtime-roadmap-mvp1.md` (DRAFT, 630줄, commit `cddd22f`) 의 DRAFT 적격성 + GP-3/GP-5 MVP-1 진입 합의 진입 가능 여부. **12 검토 기준 평가 매트릭스** (1 MVP-1 정의 / 2 3-layer PASS 분리 / 3 Layer 2 1차 표현 / 4 PoC vs MVP-1 차이 / 5 GP-3 구체성 / 6 GP-5 구체성 / 7 통합 위험 / 8 수단 후보 한정 / 9 ADR-011 매핑 / 10 Evidence Ledger enum / 11 MVP-2 진입 / 12 0/N 금지 사항). **판정 = APPROVE AS DRAFT — MVP-1 roadmap DRAFT 권위 권고 발행 적격 + GP-3 / GP-5 MVP-1 진입 합의 진입 적격, Observation O-1 (CI secret 관리 sub-section 부재) + O-2 (GP-3 + GP-5 통합 위험 sub-section 부재) — 모두 DRAFT 적격성 영향 0건, GP-3/GP-5 진입 합의 시점 보강 권고**. **5/5 풀 3+1 승격 트리거 0건 발화** → 단축 합의 적격 확정. 본 합의 = DRAFT 적격성 + GP-3/GP-5 진입 합의 진입 가능 여부 한정 — GP-3 진입 승인 / GP-5 진입 승인 / 수단 확정 / Implementation Evidence PASS / Operational Readiness PASS / Hermes PMO 격상 모두 *불가*)
docs/CONTEXT.md:375:29. ~~**Implementation/Runtime PASS Roadmap MVP-1 Deepening 작성**~~ ✅ 완료 (2026-05-12 후속, 사용자 명시 범위 답습 — 실 runtime code 구현 / CI workflow 수정 / hook 구현 / Hermes PMO 격상 / Operational Readiness PASS 선언 모두 본 작업 범위 외. `docs/architecture/implementation-runtime-roadmap-mvp1.md` 신설 (630줄, DRAFT, 9 섹션). **MVP-1 = G2 GP-3 + GP-5** (외부 LLM 응답 line 242 + 합의 보고서 §C-7 line 378 답습 — GP-2 = MVP-2 분리 사유 §1.3 답습). **3-layer PASS 분리** (Design Gate / **Implementation Evidence ← MVP-1 = Layer 2 1차** / Operational Readiness) 재명시. **§3 GP-3 deepening** = PoC → MVP-1 gap 6건 (G3-1 저장 / G3-2 코드 / G3-3 PR auto-reject + G3-4/5/6 분리) + 코드 본문 5 수단 (S-1~S-5: custom 답습 / gitleaks / detect-secrets / trufflehog / 병행) + 저장 5 수단 (ST-1~ST-5: entrypoint stat / inotify / docker secret / Vault HSM / 통합) + 측정 metric + Rollback Trigger 8개 + Evidence 5형식 + 합의 형태 권고. **§4 GP-5 deepening** = PoC → MVP-1 gap 7건 (G5-1 Layer 1 / G5-2 pre-commit / G5-3 branch protection + G5-4/5/6/7 분리) + Layer 1 정적 6 수단 (T-1~T-6: depcruise / **import-linter PoC 채택** / grimp / ruff / custom AST / **T-6 = T-2+T-5 병행 권고**) + 책무 분담 매트릭스 + pre-commit 4 수단 (PC-1~PC-4) + PR auto-reject 3 수단 (AR-1~AR-3) + 측정 metric + Rollback Trigger 10개 + Evidence 5형식 + 합의 형태 권고. **§5 통합 PASS 기준** = ADR-011 §2.1 (a)~(e) 5/5 매트릭스 + Evidence Ledger 4 enum 후보 (`secret_scan_layer1_implementation` / `secret_storage_isolation_implementation` / `provider_adapter_enforcement_layer1_static` / `mvp1_gate_pass`). **§6 MVP-1 → MVP-2 진입 5 조건** + MVP-2 영역 미리 보기 (GP-2 + G4 §4.4 Layer 4, C-7 line 379 답습). **§7 발생/미발생** = 발생 14건 / 미발생 16건. **§8 다음 진입점** = (a) Reviewer-only 단축 합의 / (b) GP-3 진입 합의 (S-1+ST-3+PC-3+AR-1) / (c) GP-5 진입 합의 (T-6+PC-3+AR-1) / (d) MVP-1 1.5차 보강 / (e) MVP-2 영역 deepening. **0/N 위반 검증 16/16** (실 runtime code 0건 / CI/hook 0건 / Hermes PMO 0건 / Operational Readiness PASS 0건 / Implementation/Runtime PASS 자동 선언 0건 / G2/G3/G4 일괄 PASS 0건 / ADR 본문 갱신 0건 / 수단 결정 0건 / Tier-2/3 자동 확장 0건 / threshold 고정 0건 / MVP-2~6 deepening 0건 / 17 항목 우선순위 자동 재고정 0건 / 신규 ADR/P/GP 발행 0건 / `event` enum 정식 등록 0건 / 외부 LLM 자동 호출 0건 / 실 API·SDK 호출 0건). **합의 형태 = 단축 합의 (Reviewer-only) 적격** — 17 항목 우선순위 답습 + 새 권위 결정 0건. 후속 단축 합의 보고서 작성 = 사용자 명시 결정 영역 (`docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` 후속))
docs/CONTEXT.md:377:27. ~~**G4 P-1/P-2/P-3 본문 흡수 작업**~~ ✅ 완료 (2026-05-11, 사용자 명시 범위 한정. `provider-agnostic-memory-skill-design.md` §4.3 / §4.4 헤더 / §4.5.2 / §4.5.3 신설 / §4.6.5 / §10 → §10.1 / §10.2 신설 / §11.1 / §11.4 / §11.4.4 본문 갱신. **P-1 (RFC 8785 JCS 인용 보강)** — §4.4 헤더 P-1 흡수 완료 명시 + RFC 8785 IETF 직접 인용 + ADR-012 §2.5 권위 + fallback 동등성 의무 cross-reference + §11.1 자기 명시 한계 strikethrough. **P-2 (§10 schema 진화 정책 보강)** — §10 → §10.1 (일반 변경 절차) + §10.2 신설 (7 행 매트릭스: 필드 추가 MINOR-호환 / 추가-비호환 MAJOR / 제거 MAJOR / 이름 변경 MAJOR + alias 1 release / 타입 변경 MAJOR / 검증 규칙 강화 MINOR-호환·MAJOR-비호환 / hash_algo MAJOR + 새 chain + 외부 LLM 의무 + T1/T2/T3 발급 권한 + import 호환 매트릭스 cross-reference + 본 §10.2 가 *하지 않는* 것 4건). **P-3 (§4.3/§4.5 import schema_version 절차 정밀화)** — §4.3 #3 schema_version 호환성 행 T2 + §10.2 + §4.5.3 cross-reference / §4.5.2 `--declare-schema-version <version>` flag 신설 + canonical JSON RFC 8785 의무 / §4.5.3 신설 (Step 1~4 정밀 절차 + 5 ledger entry 형식 + 4 금지 사항 + 4 본 §가 *하지 않는* 것) / §4.6.5 cross-reference + Step 5 ledger entry 의무. §11.4 매트릭스 RESOLVED 표기 (P-1/P-2/P-3 본 세션 + P-4 2026-05-09 PR-1 + P-5 PENDING Implementation/Runtime PASS 영역) + §11.4.4 strikethrough 갱신 + 부속 명시 갱신. **사용자 명시 범위 답습 5/5** (RFC 8785 JCS 인용 / schema 진화 정책 / import schema_version 절차 / Hermes PMO 격상 *제외* / Operational Readiness PASS·runtime 구현 *제외*). **G4 본 흡수 0/N 위반** (Hermes PMO 격상 0건 / Operational Readiness PASS 0건 / runtime 코드 자동 구현 0건 / ADR 본문 자동 갱신 0건 / P2 v3·G2·G3·G4 PASS 자동 격상 0건 / schema_version 자동 증가 0건 / 호환성 매트릭스 내용 자동 생성 0건 / 자동 declaration 발급 0건). 별도 Reviewer-only 단축 합의 보고서 작성 = 후속 결정 (사용자 명시 답습))
docs/CONTEXT.md:382:12. **ADR PR 묶음 (P2 v3 정식 채택 후)**: ADR-008 / ADR-009 / ADR-010 / ADR-011 cross-reference 갱신 + 신규 ADR-013 (Git·CI·external-review 보호) / ADR-014 (Provider-agnostic Memory/Skill Format) 후보 검토
docs/architecture/system-identity-prequel.md:7:> **본 prequel 본문 인용은 *역사적 사실 추적 + AI Dev Company OS 정체성 직접 권위 출처* 한정** — 새 작업은 P2 v3 본문 + ADR-011 / ADR-012 / ADR-009 C-N + G3 + G4 본문을 권위 우선 인용 의무.
docs/architecture/system-identity-prequel.md:10:> - §3 권위 위계 (`Constitution > ADR > SDD > Harness > Hermes > Worker`) → **ADR-011 §2.3 영구 권위 승격** ("prequel 폐기 후에도 보존" 직접 명시) ✅
docs/architecture/system-identity-prequel.md:13:> - §5 T1/T2/T3 분류 → **ADR-011 §2.4 영구 권위 승격** ("prequel §6의 3-tier 선언을 ADR 권위로 승격") ✅
docs/architecture/system-identity-prequel.md:21:> - §9 Phase 0 R-1 처리 → ADR-011 §1.1 (P2 v2 가정의 붕괴 명시) + §2.2 (G1a FAIL 확정) + P2 v3 §1.1 + §3.2 G1a (폐기) ✅
docs/architecture/system-identity-prequel.md:22:> - **§2.1 정체성 선언** ("이 도구는 단일 AI 모델을 잘 쓰는 도구가 아니라...") / **§2.2 메타포 매핑** (회사 메타포 5 row) / **§2.3 핵심 명제** ("사원 AI는 자주 바뀔 수 있다") → 부분/분산 흡수 (P2 v3 §2.1 부분 + ADR-011 §2.3 + ADR-009 C-N §5 분산) — **옵션 A 채택으로 prequel §2 본문 보존, 직접 권위 출처 영구 보존** (AI Development Company OS 정체성 보존 강도 HIGH)
docs/architecture/system-identity-prequel.md:35:> **본 archive 후 5 영구 핵심 제약 보호 강도 = HIGH 5/5** (P2 v3 §10.1 + §10.2 + ADR-011 §2.3/§2.4 + ADR-012 §원칙 5/6/9 + ADR-009 §5 영구 권위 답습) — **메타포 강제 금지 (#3) 의 *모법* 인 prequel §7 본문 보존 (옵션 A) 으로 권위 출처 약화 0건**.
docs/architecture/system-identity-prequel.md:45:**후속 권위 (Active)**: `hermes-adoption-design-v3.md` (P2 v3, **Adopted — Design Adoption only**, 2026-05-09 후속 6) + `ADR-011-means-vs-ends-redaction.md` §2.3 + §2.4 (영구 권위 승격) + `ADR-012-evidence-ledger-protection.md` (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행) + `ADR-009-self-adapter-v2-entry-conditions.md` C-N (2026-05-09 후속 4 갱신)
docs/architecture/system-identity-prequel.md:46:**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-009 C-N, ADR-010, **ADR-011 (영구 권위 — prequel §3 / §5 승격)**, **ADR-012 (Evidence Ledger Protection — prequel §6.4 트리거 실현)**
docs/architecture/system-identity-prequel.md:49:> **이하 본문 (§1 ~ §10) = 2026-05-05 임시 선언 시점 사실 보존** (옵션 A — 최소 침습 채택, 본문 변경 0건). 본 §2 정체성 선언 / §3 권위 위계 / §6 Evidence 기반 검증 / §7 메타포 강제 금지 / §8 MVP 범위 / §9 R-1 처리 등 모든 본문은 *역사적 사실 + AI Dev Company OS 정체성 직접 권위 출처* 로 영구 보존. 새 작업은 P2 v3 + ADR-011 / ADR-012 / ADR-009 C-N + G3 + G4 본문을 권위 우선 인용 의무.
docs/architecture/system-identity-prequel.md:65:- ADR-011 등 신규 ADR 발행 (P2 v3 PR과 묶음 처리)
docs/architecture/system-identity-prequel.md:95:**[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S2 답습]**: 본 §2.3 line 93 표기 "헌법 5조 (Provider Liquidity)" + §4.2 line 152/154 "헌법 8조·5조" / "헌법 5조" + §5.2 line 175 "Provider Liquidity 일부 면제" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") 中 system-identity-prequel 정정 자격 직접 발효 (R-S2 CRITICAL). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인), (P3) 약식 통일 cycle DEFER carry-over. (P4) 신규 verbatim 유형 신설 *기각* + Reviewer 권한 한계 (11) sub-boundary 신설 *기각* + (g1-N-3) chain 영구 종결 명문 의무 답습 영구. 본 cycle 합의 = `209f04d`. **본 §1.1 line 94 (`note: prequel = Archived 2026-05-09 후속 8` 답습 vs ADR-011 §2.3 영구 권위 승격 답습)** = archive 후에도 권위 보존 명문 답습 ((ii-b) 헌법-직접-매핑 강도 보존).
docs/architecture/system-identity-prequel.md:179:### 5.3 비대칭 위험
docs/architecture/system-identity-prequel.md:355:| 8 | ADR-008/009/010 갱신 PR 묶음 | ADR 3건 갱신 + 신규 ADR-011 (정체성) + ADR-012 (Evidence Ledger Schema, Phase 1 후) | #7과 동일 PR |
docs/architecture/idea-driven-stack-decision-design.md:222:### 5.3 사용자 지정 스택 처리
docs/sessions/SESSION_2026-05-21.md:35:- **답**: 금지 아님. 3+1 프로토콜 Phase 2 "독립 병렬 분석(편향 방지)"와 정합 (세션 격리 우월). 단 *수단* → 4 경계: (1) Layer 1~5 결정적 검증·합의 산출물 보존 우회 금지 / (2) means/ends (ADR-011, tmux 못박지 않음) / (3) Provider Liquidity (모델/CLI 하드코딩 금지) / (4) Hermes ≠ root of trust (신뢰 격상 금지).
docs/sessions/SESSION_2026-05-21.md:369:- ⭐ C 단독 = **결정 구조 대안**(환경 분기 + 추상 인터페이스 ADR-011 (a) + 단계적 채택, CD-8).
docs/sessions/SESSION_2026-05-21.md:486:## 75.3 수행
docs/sessions/SESSION_2026-05-06.md:1:# Session: 2026-05-06 — Phase 0 R-3 + R-4 + R-4.1 + R-5 + R-6 + R-7 (ADR-011 + 패턴 동등성 + Tier-1 42종 격리 PoC PASS + canary 재검증 트리거 + CI/nightly workflow + Phase 1 acceptance SOP)
docs/sessions/SESSION_2026-05-06.md:3:> **이전 세션 잔여(R-3 진입 대기) → R-3 ADR-011 + ADR-008 Amendment → R-4 패턴 동등성 비교 → R-4.1 Tier-1 42종 trigger UDF 확장 격리 PoC PASS → R-4 §7.2 산술 정정 + ADR-008 B.6 갱신 → .gitignore 정리 → R-5 canary 재검증 트리거 설계 → R-6 CI/nightly canary regression workflow → R-7 Phase 1 acceptance SOP**
docs/sessions/SESSION_2026-05-06.md:7:**합의 실행**: 단축 합의 1회 (Reviewer-only, R-3 ADR-011 + ADR-008 부록 B)
docs/sessions/SESSION_2026-05-06.md:10:- 신규: `ADR-011-means-vs-ends-redaction.md`, `3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`, `redaction-pattern-equivalence.md` (R-4), `r4-1-trigger-extension-evidence.md` (R-4.1), `canary-recheck-design.md` (R-5), `.github/workflows/r2-canary.yml` (R-6), 본 세션 로그
docs/sessions/SESSION_2026-05-06.md:22:- **선택**: 옵션 C (ADR-011 신규 + ADR-008 Amendment)
docs/sessions/SESSION_2026-05-06.md:35:### 1. ADR-011 본문 작성 (266줄)
docs/sessions/SESSION_2026-05-06.md:37:`docs/decisions/ADR-011-means-vs-ends-redaction.md` 신규 작성.
docs/sessions/SESSION_2026-05-06.md:60:- B.3 권위화 출처 (ADR-011)
docs/sessions/SESSION_2026-05-06.md:65:일반 원칙은 ADR-011 우선, 부록 B는 R1 specific 갱신 한정.
docs/sessions/SESSION_2026-05-06.md:81:  - 디렉토리 트리에 ADR-011 추가
docs/sessions/SESSION_2026-05-06.md:85:  - §7 의존 관계에 ADR-011 ↔ ADR-008 부록 B 교차 확인 라인 2건 추가
docs/sessions/SESSION_2026-05-06.md:89:  - 합의·검증 산출에 ADR-011, 부록 B, 단축 합의 보고서 3건 추가
docs/sessions/SESSION_2026-05-06.md:104:복구 단계에서 추가 작업 없이 산출물 무결성만 확인. 단절 직전 작성된 ADR-011 (266줄) / ADR-008 부록 B (65줄 추가) / 단축 합의 보고서 (144줄) 모두 의도한 형태대로 디스크에 보존됨을 확인.
docs/sessions/SESSION_2026-05-06.md:112:3. **Hermes ≠ root of trust ADR 권위화** — prequel §3 (R-7 후 폐기) → ADR-011 §2.3 (영구) 승격
docs/sessions/SESSION_2026-05-06.md:114:5. **R-4~R-7 모법 제공** — 후속 작업이 ADR-011 §2 항목을 명시 인용 가능
docs/sessions/SESSION_2026-05-06.md:115:6. **ADR-008 표면 모순 제거** — R1 specific 갱신 + ADR-011 cross-ref로 표면 텍스트 정합
docs/sessions/SESSION_2026-05-06.md:127:  - ADR-011 §2.1 (a) 충족 — 명시적 비교표 산출
docs/sessions/SESSION_2026-05-06.md:154:### ADR-011 §2.1 (a)~(d) 충족 결과
docs/sessions/SESSION_2026-05-06.md:160:| (c) ADR 권위로 명시 | ✅ ADR-011 §2.1 (b) 직접 인용 |
docs/sessions/SESSION_2026-05-06.md:175:- 권위 근거: ADR-011 §2.4 (자동 학습 vs 자동 정책 변경 분리) + §3 R-5 매핑
docs/sessions/SESSION_2026-05-06.md:205:- 권위 근거: ADR-011 §2.1 (d) 자동 회귀 검증 경로 확보 + §3 R-6 매핑
docs/sessions/SESSION_2026-05-06.md:238:- PARTIAL/FAIL/ROLLBACK 처리는 ADR-011 §2.4 + R-5 §8 절차 (CI 외)
docs/sessions/SESSION_2026-05-06.md:247:- 권위 근거: ADR-008 부록 B.6 6단계 마지막 + ADR-011 §3 R-7 매핑
docs/sessions/SESSION_2026-05-06.md:286:   - **FAIL** → R-7 SOP § 5 ROLLBACK trigger 매핑 → 단축/풀 합의 + ADR-011 §2.4 T3 절차
docs/sessions/SESSION_2026-05-06.md:308:- **Hermes ≠ root of trust** (ADR-011 §2.3, prequel §3에서 ADR 권위로 승격됨)
docs/sessions/SESSION_2026-05-06.md:310:- **자동 정책 변경 금지 (T3)** (ADR-011 §2.4 — Constitution / ADR / Harness Gates / Hermes 설정 변경은 단축 또는 풀 합의 거쳐야 함)
docs/architecture/redaction-pattern-equivalence.md:3:> **ADR-011 §2.1 (a) "동등 이상 보장" 검증 의무의 직접 충족 작업 — 코드 변경 없는 패턴 비교 + gap 식별 + 보충 권고 문서화**
docs/architecture/redaction-pattern-equivalence.md:7:**상위 권위**: ADR-011 §2.1 (a) (대체 수단 동등 이상 보장 검증 의무), §3 R-4 매핑
docs/architecture/redaction-pattern-equivalence.md:8:**모법 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
docs/architecture/redaction-pattern-equivalence.md:10:**산출 의도**: trigger UDF 보충 권고 카탈로그 — 실제 보충 코드 작성은 별도 작업 (보충 자체도 ADR-011 §2.1 (a)~(d) 4조건 적용 대상)
docs/architecture/redaction-pattern-equivalence.md:29:### 1.2 ADR-011 §2.1 (a) 충족 의무
docs/architecture/redaction-pattern-equivalence.md:37:- ❌ trigger UDF 패턴 코드 수정 — 본 문서는 *권고 카탈로그*이며 보충 작업은 별도 작업으로 분리 (ADR-011 §2.1 (b) "격리 환경 PoC 실증" 의무 별도 적용)
docs/architecture/redaction-pattern-equivalence.md:39:- ❌ Hermes 안전성 선언 — ADR-011 §7.3 "본 ADR은 Hermes 안전성을 선언하지 않는다" 위반 금지
docs/architecture/redaction-pattern-equivalence.md:48:**적용 범위**: 로그/도구 출력/LLM 송신 — DB INSERT 미적용 (R-1 FAIL 확정, ADR-011 §2.2 G1a)
docs/architecture/redaction-pattern-equivalence.md:105:| H-J | `_URL_WITH_QUERY_RE` | URL 쿼리 스트링 — `_SENSITIVE_QUERY_PARAMS` 16종 redact | 160-166 |
docs/architecture/redaction-pattern-equivalence.md:107:| H-L | `_FORM_BODY_RE` | `k=v&k=v` 폼 바디 — `_SENSITIVE_BODY_KEYS` 14종 redact | 177-179 |
docs/architecture/redaction-pattern-equivalence.md:111:#### `_SENSITIVE_QUERY_PARAMS` (16개, line 19-36)
docs/architecture/redaction-pattern-equivalence.md:117:#### `_SENSITIVE_BODY_KEYS` (14개, line 41-56)
docs/architecture/redaction-pattern-equivalence.md:265:### 5.3 비교 결과 합산
docs/architecture/redaction-pattern-equivalence.md:278:3. **ADR-011 §2.1 (a) 불충족** — R-2 trigger UDF가 Hermes 대비 동등 이상 보장 불가. 본 R-4 종료 시점에 G1b 정식 충족 진입 불가 — 보충 권고(§7) 후 별도 작업으로 trigger UDF 확장 + R-2 PoC 재실행 (ADR-011 §2.1 (b) 격리 환경 PoC 실증) 필요.
docs/architecture/redaction-pattern-equivalence.md:286:| Tier | 정의 | ADR-011 §2.1 (a) 영향 |
docs/architecture/redaction-pattern-equivalence.md:311:- URL query: 16 키 (Hermes `_SENSITIVE_QUERY_PARAMS`)
docs/architecture/redaction-pattern-equivalence.md:312:- Body/form: 14 키 (Hermes `_SENSITIVE_BODY_KEYS`)
docs/architecture/redaction-pattern-equivalence.md:335:본 §7은 **카탈로그 권고만 제시**. 실제 SQL trigger / REGEXP UDF 코드 작성은 별도 작업으로 분리 — 보충 작업 자체도 ADR-011 §2.1 (a)~(d) 4조건 적용 대상이며, 본 권고를 입력으로 격리 환경 PoC (ADR-011 §2.1 (b)) 재실행 필요.
docs/architecture/redaction-pattern-equivalence.md:353:| H-J | URL query secrets | `_URL_WITH_QUERY_RE` (line 160-166) — REGEXP만으로 sub 불가하므로 trigger 단계는 *매칭 차단*만 가능 (마스킹은 별도 단계). `_SENSITIVE_QUERY_PARAMS` 16 키 alternation regex로 변환 권고 |
docs/architecture/redaction-pattern-equivalence.md:355:| H-L | Form body | `_FORM_BODY_RE` + `_SENSITIVE_BODY_KEYS` 14 키 alternation regex 변환 권고 |
docs/architecture/redaction-pattern-equivalence.md:372:**예외**: H-J / H-L (URL query / form body) 의 경우, 전체 URL/body를 차단하면 정상 데이터 손실 위험 — 별도 합의 시점에 부분 마스킹 vs 전체 차단 결정 필요. 본 R-4는 **차단 권고**로 통일하되 ADR-011 §2.1 (a) 추가 검증을 후속 합의에 위임.
docs/architecture/redaction-pattern-equivalence.md:380:3. **ADR-011 §2.4 T3**: trigger UDF 변경 자체는 자동 정책 변경 금지 — 단축/풀 합의 후 PR
docs/architecture/redaction-pattern-equivalence.md:384:## 8. ADR-011 (a)~(d) 4조건 적용 결과
docs/architecture/redaction-pattern-equivalence.md:392:| **(c) ADR 권위로 명시** | 본 ADR 또는 후속 ADR | ✅ 본 문서가 ADR-011 §3 R-4 매핑 산출 — ADR-008 부록 B.6 R-4 ✅ 처리 가능 | — |
docs/architecture/redaction-pattern-equivalence.md:395:### 8.2 G1b 정식 충족 진입 조건 (ADR-008 부록 B.6 / ADR-011 §2.2)
docs/architecture/redaction-pattern-equivalence.md:400:R-3 ✅ ADR-011 발행 + ADR-008 Amendment (2026-05-06)
docs/architecture/redaction-pattern-equivalence.md:408:**R-4 → R-4.1 분기 권고**: ADR-011 §2.1 (a) 충족 의무는 본 R-4에서 *비교 + 권고 산출*까지. (b) 격리 환경 PoC 실증은 R-4.1 (trigger UDF 코드 보충 + R-2 PoC 재실행) 로 분리. 본 R-4 범위는 §8.3 참조.
docs/architecture/redaction-pattern-equivalence.md:415:| 2 | **ADR-011 §2.1 (a) 현재 미충족 판단** — R-2 trigger baseline은 Hermes 대비 동등 이상 보장을 제공하지 못함 (Tier-1 gap 42종) | §5.3 / §8.1 |
docs/architecture/redaction-pattern-equivalence.md:416:| 3 | **ADR-011 §2.1 (b) 격리 환경 PoC 재실증은 R-4.1에서 수행** — trigger UDF 코드 보충 / Tier-1 42종 반영 / R-2 PoC 재실행 / PASS evidence 재생성 | §9.1 |
docs/architecture/redaction-pattern-equivalence.md:417:| 4 | **R-4.1 없이 P2 v3에서 기존 R-2 PASS evidence를 인용하면 ADR-011 §2.1 (a) 위반 위험** — P2 v3 작성 시점에 R-4.1 완료 확인 의무 | §10.3 |
docs/architecture/redaction-pattern-equivalence.md:433:**ADR-011 적용**: §2.1 (a) ↔ §2.1 (b) 양방향.
docs/architecture/redaction-pattern-equivalence.md:453:- PASS 기준 = 42종 모두 trigger 차단 + DB 평문 부재 + 에러 평문 미노출 + ADR-011 §2.4 T3 위반 감지 0건
docs/architecture/redaction-pattern-equivalence.md:454:- FAIL 처리 = ADR-011 §2.1 (b) 재실증 요구 + 단축 합의 트리거
docs/architecture/redaction-pattern-equivalence.md:469:- ADR-011 §2.1 (a) 충족 의무가 본 R-4에서 명시적 카탈로그로 산출 — 미래 G1b 정식 충족 진입 조건이 *수치로 검증 가능*
docs/architecture/redaction-pattern-equivalence.md:471:- Hermes upstream 변경 시 자동 회귀 검출 메커니즘(§7.4)이 ADR-011 §2.4 (자동 학습 vs 자동 정책 변경 분리) 와 정합
docs/architecture/redaction-pattern-equivalence.md:481:- 본 문서는 **trigger UDF 동등성을 선언하지 않는다** — 보충 권고 카탈로그이며, 실제 동등 이상 보장 검증은 R-4.1 PoC 재실행 후 ADR-011 §2.1 (b) 충족 시점에 확정
docs/architecture/redaction-pattern-equivalence.md:482:- **R-4.1 없이 P2 v3에서 기존 R-2 PASS evidence를 인용하면 ADR-011 §2.1 (a) 위반 위험** — §7.2 Tier-1 42종 카탈로그를 미보충 상태의 R-2 PoC PASS evidence (현 baseline 5 patterns) 를 인용하는 행위가 해당. P2 v3 작성 시점에 R-4.1 완료 확인은 의무이며, 미완료 인용은 단축/풀 합의로만 예외 처리 가능. §8.3 4항 참조.
docs/architecture/redaction-pattern-equivalence.md:483:- §7.3 차단 정책 (마스킹 미시도) 은 R-2 PoC 결정과 일관 — 변경 시 ADR-011 §2.4 T3 적용
docs/architecture/redaction-pattern-equivalence.md:490:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a) 동등 이상 보장 검증 의무, §3 R-4 매핑)
docs/architecture/redaction-pattern-equivalence.md:513:**다음 진입점**: **R-4.1** (사용자 결정, 2026-05-06) — Tier-1 42종 trigger UDF 확장 + R-2 PoC 격리 환경 재실행 + ADR-011 §2.1 (b) 직접 충족 evidence 생성. Tier-2 (Telegram bot) / Tier-3 (Discord, E.164) 는 R-4.1 범위 외 — 별도 합의 또는 R-7 SOP 작성 시 처리. R-5 (canary 재검증 트리거 설계) 는 R-4.1 완료 후 진행.
docs/sessions/SESSION_2026-05-12.md:82:| §2 | MVP-1 Entry 5 조건 (현 4/5 충족) / Exit = Implementation Evidence PASS 진입 (ADR-011 §2.1 (a)~(e) 5/5) | ~30줄 |
docs/sessions/SESSION_2026-05-12.md:85:| §5 | 통합 PASS 기준 (ADR-011 5/5 + Evidence Ledger 4 enum 후보 + Rollback 통합 매트릭스) | ~40줄 |
docs/sessions/SESSION_2026-05-12.md:162:| (e) | MVP-1 PASS 발효 — GP-3 + GP-5 양쪽 ADR-011 §2.1 (a)~(e) 5/5 충족 + Implementation Evidence PASS 발효 합의 | 별도 합의 + 사용자 명시 결정 |
docs/sessions/SESSION_2026-05-12.md:317:| 본 흡수 *범위 한계* | §5.4 신설 + §5.2 cross-reference 갱신 + 변경 이력 추가 한정. **§3 GP-3 / §4 GP-5 / §5.1 / §5.3 / §6 / §7 본문 변경 0건 (cross-reference 답습 한정)** |
docs/sessions/SESSION_2026-05-12.md:355:| (2) | **MVP-1 implementation entry 최종 합의 준비** | 별도 합의 + 사용자 명시 + ADR-011 §2.1 (a)~(e) 5/5 evidence 준비 |
docs/sessions/SESSION_2026-05-12.md:420:| 6 | Runtime enforcement / CI-hook implementation | 별도 합의 + ADR-011 5/5 evidence + 사용자 명시 |
docs/sessions/SESSION_2026-05-12.md:495:| **1** | (#6) Runtime enforcement / CI-hook implementation | Implementation Evidence PASS 발효 시점 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
docs/sessions/SESSION_2026-05-12.md:559:| (1) | **Implementation Evidence PASS 발효 합의 *준비*** (Backlog #6 권고 우선순위 1) — Runtime enforcement / CI-hook implementation 영역 | 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
docs/sessions/SESSION_2026-05-12.md:608:| 8 검토 기준 | 8/8 모두 충족 (1 ADR-011 §2.1 (a)~(e) 5조건 evidence 기준 매트릭스 정의 양 GP × 5조건 10/10 / 2 9 sub-수단 적격성 기준 정의 9/9 + lock-in 위험 평가 9/9 / 3 7 backlog blocker 0/7 + 후속 6/7 + 본 합의 영역 1/7 / 4 5 영구 핵심 제약 보존 기준 정의 5/5 / 5 12/12 위반 0건 / 6 IR-1/IR-2/IR-3 evidence 요구 기준 정의 3/3 / 7 6-layer 분리 명확 / 8 Reviewer-only 단축 채택) |
docs/sessions/SESSION_2026-05-12.md:609:| 5 풀 3+1 승격 트리거 | 0/5 발화 (1 수단 본문 채택 lock-in 위험 기준 미정의 0 / 2 Runtime evidence 요구 기준 미정의 0 / 3 ADR-011 §2.1 5조건 中 1+ 기준 정의 불가 0 / 4 Operational Readiness 영역 침범 0 / 5 Hermes PMO 격상 영역 침범 0) → 단축 합의 적격 확정 |
docs/sessions/SESSION_2026-05-12.md:628:- ✅ ADR-011 §2.1 (a)~(e) 5조건 evidence 기준 매트릭스 정의 가능성 권위 권고 (10/10 양 GP × 5조건)
docs/sessions/SESSION_2026-05-12.md:646:- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정 — ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
docs/sessions/SESSION_2026-05-12.md:835:### 15.3 brief 핵심 구성 (11 섹션)
docs/sessions/SESSION_2026-05-12.md:842:- §5 Evidence 기준 (ADR-011 §2.1 (a)~(e) 5조건 + Layer B §1.8 7 evidence 형태 + JSONL ledger 7 enum 후보)
docs/sessions/SESSION_2026-05-12.md:899:| Implementation Evidence PASS (Layer C) | 0건 (별도 합의 + ADR-011 §2.1 5/5 evidence) |
docs/sessions/SESSION_2026-05-12.md:1113:- **8/8 검토 기준 충족** (1 actual run PASS 선행 / 2 독립 진입 적격성 / 3 4 sub-step 분할안 / 4 GP-3 진입 합의 답습 / 5 ADR-008 + ADR-011 답습 / 6 Hermes upstream 0 / 7 F-금지 0 / 8 5 트리거 0/5)
docs/sessions/SESSION_2026-05-12.md:1147:| 5 | ADR-011 T3 영역 침범 0건 (Vault HSM ST-4 / AR-2 branch protection / Tier-2/3 catalog = Backlog 분리) | ❌ 0 |
docs/sessions/SESSION_2026-05-12.md:1151:- ❌ Implementation Evidence PASS (별도 합의 영역 — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시)
docs/sessions/SESSION_2026-05-12.md:1280:- ❌ Implementation Evidence PASS *선언* 금지 (별도 합의 영역 — Backlog #6, ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정)
docs/sessions/SESSION_2026-05-12.md:1306:| (4) | Implementation Evidence PASS 발효 합의 brief 준비 (Backlog #6) | 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence |
docs/sessions/SESSION_2026-05-12.md:1597:- ❌ Implementation Evidence PASS *선언* 금지 (별도 합의 영역 — Backlog #6, ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정)
docs/sessions/SESSION_2026-05-12.md:1623:| (3) | Implementation Evidence PASS 발효 합의 brief 준비 (Backlog #6, 권고 우선순위 1) | 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence |
docs/sessions/SESSION_2026-05-12.md:1653:본 진입 = Stage 5 G3-7 영역 4 항목 (5.1 secrets 사용 0건 + 5.2 secrets.* 참조 감지 + 5.3 fork PR secret 정책 + 5.4 workflow permissions: contents: read).
docs/sessions/SESSION_2026-05-12.md:1700:`secret-hygiene-egress-redaction-evidence` 업로드 완료 — Stage 5 4 cycle × 4 log (`stage5-5.1-*` + `stage5-5.2-*` + `stage5-5.3-*` + `stage5-5.4-*`) 17개 신규 + 기존 Stage 1~4 log 22개 = 총 39개 + summary.json, 30 day retention.
docs/sessions/SESSION_2026-05-12.md:1749:| (1) | Implementation Evidence PASS 발효 합의 *준비 brief* | Stage 1~5 remote validation 결과 취합 + GP-3/GP-5 ADR-011 §2.1 (a)~(e) 매핑 + event enum 후보 vs 정식 등록 구분 + Implementation Evidence PASS vs MVP-1 PASS 구분 — Backlog #6 권고 우선순위 1 |
docs/sessions/SESSION_2026-05-12.md:1815:#### 22.3.2 GP-3 ADR-011 §2.1 (a)~(e) 5/5 매핑
docs/sessions/SESSION_2026-05-12.md:1819:- (c) ADR 권위 명시 = ADR-011 §2.1 + ADR-008 차단조건 #6 + 부록 B + ADR-012 §2.2 + GP-3 §5 + roadmap §3 + GP-3 진입 합의 `6dc5bdc`
docs/sessions/SESSION_2026-05-12.md:1823:#### 22.3.3 GP-5 ADR-011 §2.1 (a)~(e) 5/5 매핑
docs/sessions/SESSION_2026-05-12.md:1827:- (c) ADR 권위 명시 = ADR-009 §5 모법 + ADR-008 차단조건 #4 + ADR-011 §2.1 + GP-5 §7 + roadmap §4 + GP-5 진입 `6808d17`
docs/sessions/SESSION_2026-05-12.md:2236:### 25.3 Actual run 양쪽 SUCCESS (후속 22)
docs/sessions/SESSION_2026-05-12.md:2545:| 1 | ST-1 T3 영역 분류 적절성 | ✅ 적절 (ADR-011 §2.4 + mvp1.md §3.5 + §3.6.3 답습) |
docs/sessions/SESSION_2026-05-12.md:2546:| 2 | ST-2 T2 영역 분류 적절성 | ✅ 적절 (ADR-011 §2.4 + mvp1.md §3.3 답습) |
docs/sessions/SESSION_2026-05-12.md:2694:| **4** | **runtime secret 변경 = fail-closed + secret rotation 정책 별도 합의 분리** | 보안 우선 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 답습 + 연결 가능 후속 (Operational Readiness / Vault HSM ST-4 / rotation 자체 정책 별도 P) |
docs/sessions/SESSION_2026-05-12.md:2700:| 1 | ST-2 T2 영역 분류 | ✅ ADR-011 §2.4 + mvp1.md §3.3 + Backlog #1 진입 직전 정비 답습 |
docs/sessions/SESSION_2026-05-12.md:2706:| 7 | runtime fail-closed 처리 적절 | ✅ 보안 우선 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 (사용자 #4 결정 답습) |
docs/sessions/SESSION_2026-05-12.md:3946:### 35.3 판정
docs/sessions/SESSION_2026-05-12.md:3973:| 2 | actual run success evidence 충분성 | ✅ 11/11 + ADR-011 §2.1 (a)~(d) 4/4 |
docs/sessions/SESSION_2026-05-12.md:4224:- ❌ ADR 본문 *자동 갱신* 금지 (ADR-008 / ADR-010 / ADR-011 / ADR-012)
docs/sessions/SESSION_2026-05-12.md:4275:| 12 | Evidence 기준 | ✅ 적절 (ADR-011 §2.1 (a)~(e) 답습) |
docs/sessions/SESSION_2026-05-12.md:4335:| (iv) ADR-011 §2.1 (a)~(d) 4/4 충족 + (e) 합의 APPROVE | ⏳ 별도 합의 |
docs/sessions/SESSION_2026-05-12.md:4432:| 11 | Evidence / artifact 기준 (ADR-011 §2.1 (a)~(e)) | ✅ |
docs/sessions/SESSION_2026-05-12.md:4635:| (vii) ADR-011 §2.1 (a)~(e) 5/5 충족 + 합의 APPROVE | ⏳ **별도 합의 영역** |
docs/sessions/SESSION_2026-05-12.md:4674:- ❌ **ADR 본문 *자동 갱신*** 0건 (ADR-008 / ADR-010 / ADR-011 / ADR-012)
docs/sessions/SESSION_2026-05-12.md:4708:| ADR-011 §2.1 (a)~(d) | 4/4 충족 (e 합의 APPROVE = 본 합의 자체) |
docs/sessions/SESSION_2026-05-12.md:5129:- ❌ ADR 본문 *자동 갱신* (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
docs/sessions/SESSION_2026-05-12.md:5359:- ❌ ADR 본문 *자동 갱신* (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
docs/sessions/SESSION_2026-05-12.md:5496:- 수단/목적 분리: ADR-011 §2.1 (a)~(e) 5조건 답습 ✅
docs/sessions/SESSION_2026-05-12.md:5553:- ❌ ADR 본문 *자동 갱신* (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
docs/sessions/SESSION_2026-05-14.md:257:### 3-quater.3 ST-3 단독 답습 채택 (mvp1.md §5.3 — MVP-1 1차)
docs/sessions/SESSION_2026-05-14.md:376:### 3-sex.2 Layer C 정의 + ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습
docs/sessions/SESSION_2026-05-14.md:382:| ADR-011 §2.1 5 조건 | (a) 동등 이상의 보안 결과 / (b) 격리 환경 PoC 실증 / (c) ADR/SDD 권위 명시 / (d) 자동 회귀 검증 경로 / (e) 합의 APPROVE |
docs/sessions/SESSION_2026-05-14.md:389:| **GP-3** | ✅ Group D 368줄 (R-4.1 Tier-1 45) | ✅ Stage 2 ST-3 PoC 93줄 + actual run `25731846625` | ✅ ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + ADR-010 + R-4 + Layer B §5.5.1 | ✅ `secret-hygiene-egress-redaction.yml` 694줄 + actual runs `25728590939` + `25731846625` | ⏳ Layer C 시점 | **5/5 적격** |
docs/sessions/SESSION_2026-05-14.md:410:| C-ζ-2 | ADR-011 §2.1 (a)~(e) 5 조건 양 GP 충족 적격성 | ✅ **10/10 evidence 적격** |
docs/sessions/SESSION_2026-05-14.md:585:| 3 | 수단/목적 분리 (ADR-011 답습) | ✅ 보존 |
docs/sessions/SESSION_2026-05-10.md:43:- ADR-011 §2.1 (a)~(e) 5/5 충족
docs/sessions/SESSION_2026-05-10.md:177:### 5.3 산출물 6건 (Group A 1차 시제 직접 답습)
docs/sessions/SESSION_2026-05-10.md:205:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (Reviewer 합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:237:### 5.5.3 Q2/Q3 단축 합의 (corpus + PoC 범위)
docs/sessions/SESSION_2026-05-10.md:343:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:508:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:618:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:740:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:858:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:984:| ADR-011 §2.1 (a)~(e) | 5/5 충족 (합의 §2.1) |
docs/sessions/SESSION_2026-05-10.md:1369:| 2026-05-10 | Group C 후속 후속 통합 PoC 추가 | **Group C 후속 후속 (G4 Rewrite Defense Layer 2/3/4 정적 검출)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 5 = 0/5 발화). 산출물 8건 + fixture 17 files — `tools/rewrite_defense_check.py` (~340줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 / 실 git command 호출 0건 / 실 GitHub API 호출 0건 / 실 branch protection·git hook·signed commit 미진입) + 3 mode CLI (`--mode append-only` L2 / `--mode rewrite-command` L3 / `--mode line-regression` L4) + `--list-defenses` self-check (5 layers + dangerous command catalog 4 + line regression types 3 + 3 compliant flags) + Group C `jsonl_hash_chain.parse_jsonl` import 직접 답습 + commit history diff (L2 non_fast_forward + history_reorder) + dangerous command catalog 4 (rebase / filter-branch / reset-hard / push-force-or-amend) + line regression detector 3 types + violation reporter + fixture 17 files / 8 logical (L2 PASS append_only/pass + FAIL force_push + FAIL reorder / L3 PASS safe + FAIL rebase + FAIL filter_branch + FAIL reset_hard + FAIL push_force / L4 PASS head_extends_base + FAIL line_deletion + FAIL line_rewrite) + CI workflow `rewrite-defense.yml` 15 step (rfc8785+jcs install + artifact path = `group-cff-logs/` Group F 후속 답습) + 사양 (451줄 17 섹션) + 합의 보고서 (314줄). **로컬 10/10 + GitHub Actions actual run `25631422222` SUCCESS + 11/11 step PASS** (L2 PASS rc=0 + L2 FAIL rc=1 force-push 3 + reorder 1 cover / L3 PASS rc=0 + L3 FAIL rc=1 4 patterns cover / L4 PASS rc=0 + L4 FAIL rc=1 line_deletion 1 + line_rewrite 3 cover / `--list-defenses` 5 layers + 4 commands + 3 regression types + 3 compliant flag True / F-금지 grep 0/9). **10/10 PASS 기준 + 0/9 금지 위반 + 0/5 trigger 발화 + ADR-011 §2.1 5/5 충족**. **본 PoC 종료 = ADR-012 §2.8 *Full Rewrite 5 Layer* 답습 5/5 완결 milestone** — Layer 1 (Group C `25618490324`) + Layer 2/3/4 (본 PoC `25631422222`) + Layer 5 (Group C 후속 `25630561391`). **알려진 한계 11건** (실 branch protection·git hook·CI base branch fetch 미진입 / 실 git command·repo rewrite·GitHub API 호출 미진입 / `git filter-repo` Tier-2 / `git reset --soft/--mixed` Tier-2 / Reflog 통합 미진입 / Commit signature verification Layer 5 영역 / 1인 동일 호스트 SPOF / markdown 본문 자기 검출 — 모두 분리 영역 명시). 누적 commit 55+ → 59+ (`f754511 → 95fc8aa` + meta, +5 commits: feat + ci + docs/phase0 + docs/review + meta). **G4 *Layer 2/3/4 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + 실 branch protection·git hook·signed commit·external service 미진입**. |
docs/sessions/SESSION_2026-05-10.md:1370:| 2026-05-10 | Group C 후속 통합 PoC 추가 | **Group C 후속 (G4 History Rewrite Layer 5 External Anchor Verifier)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 5 = 0/5 발화). 산출물 8건 — `tools/history_anchor_verifier.py` (~310줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 + signed commit·branch protection·external timestamping 미진입) + 2 mode CLI (`--mode chain-only` Layer 1 baseline 답습 / `--mode anchor-verify` Layer 5 검출) + `--list-attack-models` self-check (5 attack scenarios + 11 anchor fields + Layer 1 inadequacy demo supported) + Group C `jsonl_hash_chain` import 직접 (`parse_jsonl` + `validate_chain` + `compute_entry_hash` + `compute_genesis_hash` + ENUMs) + 11-field anchor schema validation + 5 attack model 검출 (full_rewrite + tail_truncation + middle_deletion + substitution + anchor_tampered) + appended_only mode (Layer 5 정상 운영) + fixture 10건 (PASS 4 + FAIL 5 + chain_only_demo 1) + CI workflow 16 step (rfc8785+jcs install + artifact path = `group-c-followup-logs/`) + 사양 (410줄 14 섹션) + 합의 보고서 (323줄). **로컬 10/10 + GitHub Actions actual run `25630561391` SUCCESS + 10/10 검증 gate PASS** (Anchor PASS×2 + FAIL×5 + Layer 1 inadequacy demo + list-attack-models + F-금지 grep). 첫 시도 (`25630544425`) FAIL — rfc8785 미설치 → install step 추가 (`cfc48ae`) → 두 번째 시도 PASS. artifact 19 파일 정상 업로드 (18 logs + summary.json, 6265 bytes). **10/10 PASS + 0/7 금지 + 0/5 trigger + ADR-011 §2.1 5/5**. **본 PoC 핵심 evidence = Layer 1 inadequacy demo** (chain-only mode 시 full rewrite *의도된 PASS* 처리 → ADR-012 §2.8 5 Layer 中 Layer 5 anchor 의무성 직접 시연). **알려진 한계 11건** (Layer 2/3/4 미진입 / signed_tag·external_snapshot 메서드 미진입 / Anchor metadata 자체 signing 미진입 / 실 GitHub API 호출 미진입 / Anchor nightly cron 미진입 / Multi-host external service 미진입 / 1인 동일 호스트 SPOF 한계 / markdown 자기 검출 / Group G hermes-originated anchor 책무 분리 / signed_tag·external_snapshot 부재 / RFC 3161 미통합 — 모두 분리 영역 명시). 누적 commit 49 → 55+ (`cfc48ae` + meta, +6 commits: scanner+fixture+CI+사양+합의+CI fix+meta). **G4 *Layer 5 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Layer 2~4 미진입**. **ADR-012 §2.8 5 Layer 답습 진행 = Layer 1 (Group C) + Layer 5 (본 PoC) = 2/5 완결**. |
docs/sessions/SESSION_2026-05-10.md:1371:| 2026-05-10 | Group A 3차 통합 PoC 추가 | **Group A 3차 (G2 GP-5 Layer 1c URL endpoint + model name 직접 사용 차단)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 6 = 0/6 발화). 산출물 8건 — `tools/provider_url_scanner.py` (~210줄, **stdlib `re` + `dataclasses` 단독** 외부 의존 0건 + gitleaks·depcruise·AST 통합 미진입) + 2 mode CLI (`--mode url-endpoint` E-1 / `--mode model-name` E-2) + `--list-catalogs` self-check + URL Tier-1 catalog 10 (Anthropic/OpenAI/Azure-OpenAI/Google-AI/Replicate/Perplexity/Cohere/HuggingFace/Together/OpenRouter) + Model Tier-1 catalog 19 (Anthropic 5 + OpenAI 5 + Google 3 + Meta 3 + Mistral 3) + extension allowlist (URL 8 / Model 5 = §9.3 "yaml만 허용" 답습) + comment line 부분 회피 + fixture 9건 (E-1 PASS 1 + FAIL 3 (anthropic/openai/google) / E-2 PASS 1 + FAIL 4 (anthropic/openai/gemini/llama)) + CI workflow 12 step (artifact path = `group-a3-logs/` Group F 후속 답습) + 사양 (387줄 14 섹션) + 합의 보고서 (311줄). **로컬 6/6 + GitHub Actions actual run `25629390384` SUCCESS 6s 16/16 step ✓ + 6/6 검증 gate PASS** (E-1 PASS rc=0 + E-1 FAIL rc=1 4 + 4 pattern_ids cover + E-2 PASS rc=0 + E-2 FAIL rc=1 13 + 11 pattern_ids cover (4 vendor 모두) + `--list-catalogs` url=10 model=19 allowlist=8/5 + 3 compliant flag True + F-금지 grep 0/8). artifact 11 파일 정상 업로드 (10 logs + summary.json, 3299 bytes). **6/6 PASS + 0/8 금지 + 0/6 trigger + ADR-011 §2.1 5/5**. **Group A 2차 합의 §5.5 #C-8 답습 의무 충족 — 3차 분리 영역 책무 해소** (Layer 1c 모법 답습). **Layer 1a/1b/1c 분리 답습 완결**. **알려진 한계 11건** (depcruise rule 통합 / pre-commit / PR auto-reject / 의미적 분석 / Multi-line block / docstring / Tier-2 vendor / 모델 ID 세부 version / URL fragment Group D 분리 / 실 src FP / markdown 본문 자기 검출 — 모두 분리 영역 명시). 누적 commit 44 → 49+ (`bbc9684` + meta, +5 commits). **G2 GP-5 *Layer 1c 정적 검출 시제* 한정 — G2 GP-5 / G2 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Tier-2/3 catalog 확장 0건**. |
docs/sessions/SESSION_2026-05-10.md:1372:| 2026-05-10 | Group G 통합 PoC 추가 | **Group G (G3 Skill escalation 차단 + 합의 자기참조 차단 + G4 Memory/Skill boundary 4 금지)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 6 = 0/6 발화). 산출물 8건 — `tools/boundary_guard.py` (~445줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 + runtime hook 0건 + Docker SDK·git2·pyyaml 미도입) + 3 mode CLI (skill-escalation G-1 / consensus-self-reference G-2 / memory-skill-boundary G-3) + `--list-boundaries` self-check (4 boundaries + 3 modes + 13 합의 매트릭스 row + boundary_4_rules_compliant=True) + Group C `jsonl_hash_chain.validate_schema` + ENUMs import 직접 + Group E `ALLOWED_ACTIONS_ENUM` + `parse_yaml_v2` import 직접 + Group B Hermes-originated marker 6 패턴 답습 + governance PASS anchor 9 + reviewer/외부 LLM marker + Hermes PMO/policy decision 3 + policy expression 6 + scope transition 검출 + agent=hermes × event 매트릭스 + audit log × allowed_actions 매트릭스 + fixture 9건 (G-1 PASS 1 = `valid_skill_within_allowed.yaml` Group E 답습 + FAIL 2 / G-2 PASS 1 + FAIL 2 / G-3 PASS 1 = `safe_memory_skill_chain.jsonl` Group F 직접 복사 + FAIL 3) + CI workflow 13 step (artifact path = `group-g-logs/` Group F 후속 답습) + 사양 (399줄 14 섹션) + 합의 보고서 (350줄). **로컬 8/8 + GitHub Actions actual run `25626591894` SUCCESS 5s 17/17 step ✓ + 7/7 검증 gate PASS** (G-1/G-2/G-3 PASS rc=0 + FAIL rc=1 + 7 pattern_ids cover (yaml-invalid-action/audit-log-escalation/hermes-self-consensus/hermes-pmo-self-promotion/memory-replaces-policy/session-to-global/hermes-self-approves) + `--list-boundaries` total_boundaries=4 + total_modes=3 + consensus_matrix_rows=13 + boundary_4_rules_compliant=True + F-금지 grep 0건). artifact 15 파일 정상 업로드 (14 logs + summary.json, 4537 bytes, 30일 retention). **8/8 PASS 기준 + 0/11 금지 위반 + 0/6 trigger 발화 + ADR-011 §2.1 5/5 충족**. **알려진 한계 15건** (Skill wrapper runtime / Docker cap_drop / sandbox syscall / escalation 자동 비활성화 / 실 git commit author / 외부 LLM 자동 호출 / PR auto-reject / Memory write blocker / promotion hook / P12 정식 등록 / G3 22 권한 분해 (Group I) / Hermes PMO 격상 자동화 / G4 §5.2 #2 (G-1 통합) / 도구 도입 / markdown 본문 자기 검출 — 모두 분리 영역 명시). 누적 commit 38 → 43+ (`da48ba5` + meta). **G3 + G4 *형식적 검출 layer 시제* 한정 — G3 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + runtime hook 0건 + 실 git commit author 검사 0건 + 외부 LLM 자동 호출 0건**. |
docs/sessions/SESSION_2026-05-10.md:1373:| 2026-05-10 | Group E 통합 PoC 추가 | **Group E (G2 GP-4 External Input Validation + G4 Memory/Skill schema validation)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 6 = 0/6 발화). 산출물 8건 — `tools/schema_validator.py` (~520줄, **stdlib `re` + `json` + `dataclasses` 단독** 외부 의존 0건 / pydantic·jsonschema·pyyaml 미도입) + 2 mode CLI (external-input / skill-schema) + `--list-skill-fields` self-check + 17-field 정의 (G4 §3.1 직접 복사 변경 0건, 필수 12 + MVP-권장 5) + 11-field 검증 (`jsonl_hash_chain.validate_schema` import 직접 Group C 답습) + injection canary 26 patterns (12 + 8 + 6) + ENUM (allowed_actions 7 / promotion_status 5 / scope 4) + transition 매트릭스 + provider lock-in marker + custom YAML mini-parser + fixture 9건 (E-1 PASS 1 + FAIL 4 + E-2 PASS 1 (Group F skill_project.jsonl YAML 재구성) + FAIL 4) + CI workflow 12 step (artifact path = `group-e-logs/` Group F 후속 답습) + 사양 (495줄) + 합의 보고서 (310줄). **로컬 6/6 + GitHub Actions actual run `25624970577` SUCCESS 10s 16/16 step ✓ + 6/6 검증 gate PASS** (E-1 PASS rc=0 + E-1 FAIL rc=1 22 + 4 카테고리 + E-2 PASS rc=0 17/17 + E-2 FAIL rc=1 16 + 4 pattern_ids + 17-field count total=17 + F-금지 grep 0건). artifact 11 파일 정상 업로드 (10 logs + summary.json, 3691 bytes). **6/6 PASS + 0/10 금지 + 0/6 trigger + ADR-011 §2.1 5/5**. **알려진 한계 11건** (Memory boundary 4 금지 runtime / Skill wrapper escalation = Group G 영역 분리 / 재귀 JSON Schema / Reviewer Agent 추론 / runtime escape / 실 LLM API / pydantic·jsonschema / pyyaml / P9~P12 정식 등록 / provider_bindings lint 룰 / markdown 본문 자기 검출). 누적 commit 33 → 37+ (`8176235` + meta, +5 commits). **G2 GP-4 / G4 *형식적 검증 layer 시제* 한정 — G2 GP-4 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + Memory boundary hook 0건 + Skill wrapper 0건**. |
docs/sessions/SESSION_2026-05-10.md:1374:| 2026-05-10 | Group D 통합 PoC 추가 | **Group D (G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 7 = 0/7 발화). 산출물 8건 — `tools/secret_scanner.py` (261줄, **R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습** Prefix 36 + regex 7 + alternation 2, 변경 0건 + 외부 의존 0건 + gitleaks/detect-secrets 미도입 + Tier-2/3 catalog 확장 0건) + 2 mode CLI (scan-source D-1 / scan-log D-2) + `--list-patterns` Tier-1 catalog count self-check + `is_redaction_marker_match()` (FP 회피) + fixture 9건 (PASS 2 + FAIL 4 + REDACTION_PASS 1 + REDACTION_FAIL 2, fake canary 의무 답습) + CI workflow 12 step (artifact path = `group-d-logs/` Group F 후속 답습) + 사양 (351줄) + 합의 보고서 (291줄). **로컬 6/6 + GitHub Actions actual run `25623028888` SUCCESS 6/6 검증 gate PASS** (D-1 PASS rc=0 + D-1 FAIL rc=1 violations=14 + 4 패턴 cover incl. private-key T1-035 + D-2 PASS rc=0 + D-2 FAIL rc=1 partial leak 검출 + Tier-1 count 45 + tier1_42_catalog_compliant=True + F-금지 grep 0건 + base64 미검출 known limitation 답습). artifact 11 파일 정상 업로드 (10 logs + summary.json, 3817 bytes, 30일 retention). **F-범위 5/5 + 12 금지 0/12 위반 + 풀 3+1 trigger 0/7 발화 + ADR-011 §2.1 5/5 + PASS 기준 7/7 충족**. **알려진 한계 11건** (특히 #1 base64 evasion = Hermes upstream R2-6 영역 / #7 Tier-2/3 catalog 확장 / #11 markdown 본문 자기 검출 — Group B `evidence_pass_gate.py` 답습). 누적 commit 28 → 32+ (`3a8c8d5` + meta, +5 commits: scanner + fixtures + CI + 사양 + 합의 + meta). **G2 GP-2 / GP-3 *형식적 검출 layer 시제* 한정 — G2 GP-2 / GP-3 / G2 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건**. |
docs/sessions/SESSION_2026-05-10.md:1376:| 2026-05-10 | Group F 통합 PoC 추가 | **Group F (G2 GP-6 Memory/Skill Migration *Feasibility*)** — Reviewer-only 단축 합의 APPROVE WITH CONDITIONS (풀 3+1 승격 trigger 6 = 0/6 발화). 산출물 8건 (validator + 4 fixture + CI workflow + 사양 + 합의) — Group C 3 모듈 (`canonical_json` + `jsonl_hash_chain` + `jsonl_roundtrip`) **import 직접** (리팩토링 0 / 복제 0 / 신규 ~80줄, F-사전 결정 1순위 충족). **로컬 4/4 + GitHub Actions actual run `25620376305` SUCCESS 14s 16/16 step ✓** (Memory PASS + Skill PASS + Hermes→Claude LOSSY rc=1 lost_fields=2 + Chain violation FAIL rc=2 chain_violation_detected). **F-범위 10/10 + F-금지 0/9 위반 + 풀 3+1 승격 trigger 0/6 발화 + ADR-011 §2.1 5/5 + PASS 기준 9/9 충족**. **알려진 한계 8건** (특히 #8 — actual run 발견: artifact upload empty, `.group-f-logs/` hidden dir + `include-hidden-files: false` default → 0 바이트 zip. 검증 영향 0건, evidence 는 CI run log + `$GITHUB_STEP_SUMMARY` + summary.json stdout 보존. 후속 수정 후보 = (A) `include-hidden-files: true` / (B) `.group-f-logs/` → `group-f-logs/` rename — 사용자 권고 = B, 본 세션 미수정 후속 작업 등록). 누적 commit 19 → 23+ (`c675e98 → 8acbe18` + meta 갱신, +4 commits: PoC 본문 + .gitignore + 사양 + 합의). **G2 GP-6 *feasibility 시제* 한정 — G2 GP-6 / G2 / G4 전체 Implementation/Runtime PASS 권한 0건 + Hermes PMO 격상 0건 + ADR 본문 변경 0건 + 실 migration script 0건 + 실 provider SDK 호출 0건**. |
docs/sessions/SESSION_2026-05-05.md:230:   - ADR-011 또는 ADR-008 Amendment
docs/sessions/SESSION_2026-05-05.md:233:   - 산출: `docs/decisions/ADR-011-means-vs-ends-redaction.md` (또는 ADR-008 Amendment)
docs/sessions/SESSION_2026-05-05.md:297:2. ADR-011 (수단/목적 분리) 또는 ADR-008 Amendment 형식 사용자 결정 요청
docs/sessions/SESSION_2026-05-05.md:322:**권고**: 옵션 A. R-3는 단축 합의 + 풀 합의 모두에서 가장 우선 보강 항목으로 식별되었고, ADR-011 작성이 후속 R-4~R-7의 권위 근거가 됨.
docs/sessions/SESSION_2026-05-05.md:363:**다음 세션 권장 시작점**: 옵션 A (R-3 직접 진입) — `ADR-011 또는 ADR-008 Amendment 형식 사용자 결정` 부터
docs/sessions/SESSION_2026-05-19.md:390:| 2 | 권고 시작점 = (α) defer 본 brief 시점 + (β) `push` event 1 run 실 발화 사용자 결정 후 + 발화 방식 = (β-1) empty commit + push | brief §4 + §5.3 | §2.1 + §2.2 명시 (C-A1-26) |
docs/sessions/SESSION_2026-05-19.md:643:### 15.3 (E) defer 영구 발효 핵심 의미
docs/sessions/SESSION_2026-05-19.md:761:| 7 | W-5~W-10 / PC-4 / AR-2 / AR-3 / Stage 5 / Backlog #1~#6 / Group I / MVP-2~6 자동 진입 0건 | brief §0.4 + §5.3.2 + §8.2 | §0.3 + §0.4 명시 (C-A3-13) |
docs/architecture/provider-agnostic-memory-skill-design.md:28:**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리), **ADR-012 (Evidence Ledger Protection — 본 G4 §4 권위 출처)**
docs/architecture/provider-agnostic-memory-skill-design.md:53:5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음 (ADR-014 신규 후보 포함)
docs/architecture/provider-agnostic-memory-skill-design.md:57:9. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
docs/architecture/provider-agnostic-memory-skill-design.md:114:**위계 답습** (ADR-011 §2.3 영구 권위):
docs/architecture/provider-agnostic-memory-skill-design.md:269:| 10 | `forbidden_actions` | array\<permission_category\> | MVP-권장 | (i) `allowed_actions` 와 disjoint (ii) **T3 7-category 자동 포함 강제** — `SECRET_ACCESS` / `POLICY_CHANGE` / `ADR_CHANGE` (자동 수행) / `SELF_PROMOTION` / `PROVIDER_LOCK_IN_ENFORCE` / `REDACTION_POLICY_RELAX` / `CONSTITUTION_BYPASS` 모두 *명시 작성 여부 불문 강제 포함* (§3.7.3 답습) (iii) 사용자 명시 override 불가 (T3 영역, ADR-011 §2.4) | 0 (T3 강제 차단) |
docs/architecture/provider-agnostic-memory-skill-design.md:312:| Skill `approved` → `promoted` | ❌ Hermes 자동 금지 — **Tools 검증 + Evidence ledger entry** 필수 + 사용자 명시 가능 | T2 + Evidence (G3 §5.3 답습) |
docs/architecture/provider-agnostic-memory-skill-design.md:324:| `promoted` | **T1 + T2 전체** (T2 5 카테고리 전부 — `WRITE_CODE` / `RUN_LOCAL_TOOLS` / `NETWORK_ACCESS` / provider-specific optimization / skill promotion) | T3 전체 차단 (§3.7.3 + §3.8 답습) | (i) `required_evidence` 모두 통과 (§5.3 답습) (ii) `required_tests` 모두 통과 (iii) Evidence ledger entry append 의무 (`event: skill_promoted` + §4.2 답습) (iv) `last_verified_at` 갱신 (v) §3.8 self-escalation 검증 통과 |
docs/architecture/provider-agnostic-memory-skill-design.md:342:- `required_evidence` 의 하나라도 stale (예: test 실패 / lint 위반 / secret 검출) → **rollback_trigger 매치** → §3.4.2 `revoked` 자동 전이 (T3 자동 안전 동작 — ADR-011 §2.4)
docs/architecture/provider-agnostic-memory-skill-design.md:398:| **MVP-필수** | MVP 범위 내 강제, 후속 *완화 불가* | (11) required_evidence (Skill `promotion_status: promoted` 진입 시 ledger entry 의무, §3.4 답습) — **1 건** | `promoted` 상태 전이 시점 (T2 + Evidence §5.3 답습) |
docs/architecture/provider-agnostic-memory-skill-design.md:407:| (11) `required_evidence` | 권장 | MVP-필수 (`promoted` 진입 시) | Evidence Ledger (system-identity-prequel §6.3) 권위 답습 — Skill `promotion_status: promoted` 는 §5.3 PASS 성립 요건 (i)~(iv) 충족 의무. evidence enumeration 의 *형식* 부재는 검증 불가 |
docs/architecture/provider-agnostic-memory-skill-design.md:435:- `WRITE_DOCS` (일부) — `docs/decisions/` / `docs/constitution/` 진입 시 *자동 T3 분류* (ADR-011 §2.4 + ADR-008 부록 C §C.2 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:440:> Hermes / Worker / Skill 사용 *전* 사용자 명시 승인 의무 (ADR-011 §2.4 T2 답습). Skill `promotion_status: promoted` 진입 후 활성화 가능.
docs/architecture/provider-agnostic-memory-skill-design.md:457:> **모든 Skill 의 `forbidden_actions` 자동 포함 강제** (§3.2 #10 답습). 사용자 명시 override *불가* (T3 영역, ADR-011 §2.4). `allowed_actions` 에 T3 카테고리 진입 시 schema validation 즉시 BLOCK.
docs/architecture/provider-agnostic-memory-skill-design.md:463:| 11 | `SECRET_ACCESS` | API key / credential / private key / token 직접 접근 | 보안 헌법 (ADR-010 + ADR-011 §2.4) + R-1~R-7 redaction 정책 답습 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_secret_access_attempt` |
docs/architecture/provider-agnostic-memory-skill-design.md:464:| 12 | `POLICY_CHANGE` | Constitution / ADR / SDD / Harness Gates 본문 변경 | 권위 위계 (ADR-011 §2.3) — Constitution > ADR > SDD > Harness Gates > Hermes > Workers | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_policy_change_attempt` |
docs/architecture/provider-agnostic-memory-skill-design.md:465:| 13 | `ADR_CHANGE` (자동 수행) | `docs/decisions/ADR-*` 본문 *자동* 변경 (수동 사용자 명시 결정은 T2) | ADR Amendment 절차 강제 (ADR-008 부록 C §C.2 + ADR-011 §2.4 T3) — 풀 3+1 합의 + 외부 LLM 의견 의무 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_adr_change_attempt` |
docs/architecture/provider-agnostic-memory-skill-design.md:468:| 16 | `REDACTION_POLICY_RELAX` | R-4.1 Tier-1 42 catalog / baseline 5 redaction 정책 완화 / 우회 | ADR-011 §2.1 본질 (DB 평문 저장 차단 결과) + R-1~R-7 redaction 6단계 답습 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_redaction_relax_attempt` |
docs/architecture/provider-agnostic-memory-skill-design.md:469:| 17 | `CONSTITUTION_BYPASS` | Constitution 본문 우회 (memory / skill 로 정책 이전 시도) | G4 §5.2 #1 Memory 가 policy 대체 / §5.2 #2 Skill 이 ADR 우회 위반 + 권위 위계 (ADR-011 §2.3) 위반 | `allowed_actions` 진입 시 즉시 BLOCK + Memory/Skill boundary §5.2 검증 BLOCK + `event: t3_constitution_bypass_attempt` |
docs/architecture/provider-agnostic-memory-skill-design.md:470:| 18 | `GATE_ENFORCEMENT_LAYER_MODIFY` (**G3 §2.6 cross-reference — 2026-05-12**) | Gate enforcement layer 변경 시도 — Gate 정의 본문 (`docs/architecture/governance-preconditions.md` / `hermes-not-root-of-trust-runtime.md` / `provider-agnostic-memory-skill-design.md`) / Gate verdict 본문 / Evidence Ledger `event: gate_pass` / `event: gate_fail` entry 위조 / CI workflow / hook 설정 변경 / Gate 순서 skip 시도 *모두 포함*. **Skill permission 이 `WRITE_CODE` 또는 `RUN_LOCAL_TOOLS` (T2) 를 갖더라도 본 카테고리는 자동 포함 강제** (Gate enforcement layer 변경 권한 *분리*) | 권위 위계 (ADR-011 §2.3) + Gate enforcement layer = ADR-011 §2.3 운영 함의 1~5 + Hermes ≠ root of trust (ADR-011 §2.3 영구 권위) + ADR-008 부록 C §C.2 + G3 §2.6 (권위 정의) | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_gate_enforcement_modify_attempt` + G3 §2.6.5 rollback_trigger 발화 (`gate_enforcement_bypass_detected`, §3.8.2 #10 답습) |
docs/architecture/provider-agnostic-memory-skill-design.md:476:- **자동 비활성화**: T3 attempt 검출 시 Skill `promotion_status: revoked` 자동 전이 (T3 자동 안전 동작 — ADR-011 §2.4 + §6.5 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:502:| Forbidden override 차단 | Skill A 가 Skill A 의 `forbidden_actions` 에서 T3 카테고리 제거 시도 시 BLOCK + T3 영역 (ADR-011 §2.4) | schema-level + T3 절대 강제 |
docs/architecture/provider-agnostic-memory-skill-design.md:517:5. 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
docs/architecture/provider-agnostic-memory-skill-design.md:530:| 3 | `t3_violation` | T3 카테고리 attempt 검출 (§3.7.3) | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + ADR-011 §2.4 책임 분석 |
docs/architecture/provider-agnostic-memory-skill-design.md:539:**Revocation Chain 자동 전이** (T3 자동 안전 동작 — ADR-011 §2.4):
docs/architecture/provider-agnostic-memory-skill-design.md:570:- ❌ 외부 Reviewer (사용자 / 외부 LLM) 자동 호출 (T3 영역, ADR-011 §2.4)
docs/architecture/provider-agnostic-memory-skill-design.md:618:| schema_version 호환성 | 본 `0.1` 이외 버전은 **명시 declaration 후만 import 가능** (T2 사용자 승인 + §10.2 합의 절차 충족 + §4.5.3 import 검증 절차 통과 의무) | §4.5 + §10.2 + §4.6.5 답습 |
docs/architecture/provider-agnostic-memory-skill-design.md:621:**P-3 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-3 (자기 발견 잠재 위험 — "§4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재") 흡수 완료. **schema_version declaration 절차 = T2 사용자 명시 승인 + §10.2 합의 절차 + §4.5.3 정밀 import 검증 단계**. 본 절차 충족 *전* import = BLOCK (§4.6.5 #1~#3 답습).
docs/architecture/provider-agnostic-memory-skill-design.md:636:- JSONL append-only — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4)
docs/architecture/provider-agnostic-memory-skill-design.md:647:- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:710:2. **기존 원본 JSONL 보존** — 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
docs/architecture/provider-agnostic-memory-skill-design.md:755:- **schema_version 명시 의무** — 변환 input / output 양쪽 모두 `schema_version` 필드 존재 확인 (§4.5.3 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:757:- **`--declare-schema-version <version>` flag 지원** — 비표준 `schema_version` import 시 사용자 명시 declaration 통로 (§4.5.3 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:760:#### 4.5.3 Import 시 schema_version 검증 절차 (**P-3 흡수 — 2026-05-11**)
docs/architecture/provider-agnostic-memory-skill-design.md:762:> **본 §4.5.3 는 G4 DRAFT 검토 §3.1 P-3 흡수** (출처: `3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` §3.1 P-3 — "§4.5 외부 형식 import 시 schema_version declaration 절차 약함"). §4.3 #3 + §4.6.5 와 결합하여 *정밀 검증 절차* 본문화. **본 §4.5.3 = *절차 사양*까지 — 실 import 코드 구현 = Implementation/Runtime PASS 영역 별도 합의**.
docs/architecture/provider-agnostic-memory-skill-design.md:792:**금지 사항** (T3 영역 — ADR-011 §2.4 + ADR-012 §3.2 답습):
docs/architecture/provider-agnostic-memory-skill-design.md:796:- ❌ Step 1~3 통과 ledger entry 부재 상태에서 PASS 선언 (G3 §1.3 + §5.3 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:798:**본 §4.5.3 가 *하지 않는* 것**:
docs/architecture/provider-agnostic-memory-skill-design.md:832:| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) **정책 / 권한 / 증거 손실 BLOCK** |
docs/architecture/provider-agnostic-memory-skill-design.md:845:- `semantic_diff` 판단 = **사용자 명시 review** (ADR-011 §2.4 T2/T3 사용자 승인)
docs/architecture/provider-agnostic-memory-skill-design.md:855:**Import 의무 검증** (**§4.5.3 정밀 절차 답습 — 2026-05-11 P-3 흡수**):
docs/architecture/provider-agnostic-memory-skill-design.md:856:1. `schema_version` 필드 존재 확인 (없으면 BLOCK — ADR-012 §2.10 + §4.5.3 Step 1)
docs/architecture/provider-agnostic-memory-skill-design.md:857:2. 호환성 매트릭스 조회 — 현 MVP 0.1 only, 외부 형식 매핑은 별도 (Implementation 영역, §4.5.3 Step 2)
docs/architecture/provider-agnostic-memory-skill-design.md:858:3. 미일치 시 BLOCK + 사용자 명시 manual approval 요구 (§4.5.3 Step 4 declaration 절차 — T2 사용자 승인 + §10.2 합의 절차)
docs/architecture/provider-agnostic-memory-skill-design.md:859:4. Hash chain 검증 (§4.4.4 답습, §4.5.3 Step 3)
docs/architecture/provider-agnostic-memory-skill-design.md:860:5. **Step 1~4 결과 ledger entry 의무** — `event: import_pass` / `import_block_*` / `schema_version_declared` (§4.5.3 답습)
docs/architecture/provider-agnostic-memory-skill-design.md:867:2. **원본 보존** — 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
docs/architecture/provider-agnostic-memory-skill-design.md:881:| (b) 자동 revert | T3 위반 위험 (ADR-011 §2.4) | ❌ 비채택 |
docs/architecture/provider-agnostic-memory-skill-design.md:913:### 5.3 본 §5 가 *하지 않는* 것
docs/architecture/provider-agnostic-memory-skill-design.md:964:| `promoted` 진입 시 Tools 검증 + Evidence 강제 | (위임) | ✅ G3 §5.3 (i)~(iv) |
docs/architecture/provider-agnostic-memory-skill-design.md:970:**G3 §1.3 + §5.3 답습**: 모든 PASS 판정 = Evidence Ledger 기록 의무.
docs/architecture/provider-agnostic-memory-skill-design.md:977:| Evidence Ledger entry 생성 강제 | (위임) | ✅ G3 §1.3 + §5.3 |
docs/architecture/provider-agnostic-memory-skill-design.md:978:| Promotion 시 ledger entry 존재 검증 | (위임) | ✅ G3 §5.3 (ii) |
docs/architecture/provider-agnostic-memory-skill-design.md:1144:| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위) | §2 (Memory 사용자 owner) + §3.4 (Skill 사용자 승인) + §5.2 (4 금지) + §6 (G3 인터페이스) |
docs/architecture/provider-agnostic-memory-skill-design.md:1146:| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 | §2.5 promotion T2 강제 + §3.4 Skill 자동 승격 금지 + §5.2 4 금지 |
docs/architecture/provider-agnostic-memory-skill-design.md:1147:| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) → 본 §8.1 (a)~(e) 패턴 답습 | §8.1 |
docs/architecture/provider-agnostic-memory-skill-design.md:1186:**schema_version 발급 권한** (ADR-011 §2.4 T1/T2/T3 답습):
docs/architecture/provider-agnostic-memory-skill-design.md:1208:2. **R-7 SOP §0 핵심 선언 답습**: §8.1 8 Exit 조건 + §8 (a)~(e) 추가 G4 PASS 조건 — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 패턴 답습.
docs/architecture/provider-agnostic-memory-skill-design.md:1209:3. **ADR-011 §2.4 T1/T2/T3 답습**: §2.5 Memory promotion T2, §3.4 Skill 자동 생성 T1 / 자동 승격 T2 / Tools 검증 T2+Evidence, §5.2 4 금지 (T3 영역).
docs/architecture/provider-agnostic-memory-skill-design.md:1230:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신
docs/architecture/provider-agnostic-memory-skill-design.md:1246:3. ADR-011 §2.4 T1/T2/T3 답습 — 본 G4 §2.5 + §3.4 + §5.2 모두 T 분류 강제
docs/architecture/provider-agnostic-memory-skill-design.md:1262:| **P-3** | §4.5 외부 형식 import 시 schema_version declaration 절차 약함 | §4.3 #3 단순 명시 → **2026-05-11 §4.3 #3 보강 + §4.5.2 보강 + §4.5.3 신설 + §4.6.5 cross-reference 보강** | §4.3 #3 schema_version 호환성 행 T2 + §10.2 + §4.5.3 cross-reference 명시 + §4.5.2 `--declare-schema-version` flag + canonical JSON RFC 8785 의무 + §4.5.3 신설 (Step 1~4 정밀 절차 + 5 ledger entry 형식 + 4 금지 사항 + 4 본 §4.5.3 가 *하지 않는* 것) + §4.6.5 Step 1~5 답습 cross-reference 보강 | ✅ **RESOLVED** (2026-05-11) |
docs/architecture/provider-agnostic-memory-skill-design.md:1302:**[Cross-reference Block — (g1-N-3-pamsd) HIGH carry-over, R-7 (vi-γ) 답습]**: 본 §11.4.2 "Provider Liquidity 4-way Multi-layer Defense" 명명 = 헌법-동급 권위 (R-S4 (g1-N-3) 답습). (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2 (Provider Liquidity, 비협상) line 75~80** 직접 모법 발효 — Layer 1~4 모두 헌법 제5조-2 line 80 "본 원칙은 비협상 — ADR-011 line 6 상위 권위 매핑 답습" 답습 형식 직접 활용 자격. 본문 verbatim 변경 0건 (R-7 (vi-α) 사전 기각 + (vi-β) DEFER 양립, (vi-γ) cross-reference 추가만 채택).
docs/architecture/provider-agnostic-memory-skill-design.md:1323:- ~~❌ P-3 (§4.5 import schema_version 검증) 자동 구현 (PR-2 또는 별도 합의)~~ **✅ *사양*까지 흡수 완료** (2026-05-11 §4.5.3 신설 — 실 import 코드 구현은 여전히 Implementation/Runtime PASS 영역 별도 합의)
docs/architecture/provider-agnostic-memory-skill-design.md:1356:#### 11.5.3 본 §11.5 가 *하지 않는* 것 (사용자 명시 답습 7 영역)
docs/architecture/provider-agnostic-memory-skill-design.md:1364:- ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신** — Permission Granularity 와 ADR 본문 cross-reference 가 깨지지 않음 (본 작업 = G4 본문 보강 한정)
docs/architecture/provider-agnostic-memory-skill-design.md:1414:- ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — cross-reference 보강만, 본문 갱신은 별도 PR 묶음
docs/sessions/SESSION_2026-05-16.md:71:| (c) | ADR/SDD 권위 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + ADR-010 + R-4 + mvp1.md §3 + Layer B §5.5.1 ST-3 | — | ✅ 답습 한정 |
docs/sessions/SESSION_2026-05-16.md:246:| 수단/목적 분리 | ✅ 보존 (ADR-011 §2.1 (a)~(e) 5 조건 모법 답습) |
docs/sessions/SESSION_2026-05-16.md:266:| ADR-011 §2.1 (a)~(e) 5 조건 | 모법 | 재정의 0건 |
docs/sessions/SESSION_2026-05-16.md:333:본 세션 = **Layer C 발효 합의 실 진입 brief (`0862f74` APPROVE AS BRIEF, 후속 16) 발효 후속 Step 0~6 cycle 완료** — 2 commit chain. **Step 0 사전 점검** (11/11 commit chain 변경 0건 — Layer C 진입 가능성 합의 + Layer C 실 진입 brief + Phase α-1/2/3/4 + Group α + Backlog #6 + Layer A + Layer B + §5.5). **Step 1 양 GP × 5 조건 evidence 답습 검증** (10/10 적격성 + 8 evidence file line count 정확 일치 + 9/9 재생성 0건). **Step 2 4 prerequisite actual runs PASS 답습 확정** (`25728590939` + `25728590916` + `25728590977` commit `72622409` + `25731846625` commit `6c6b208` 모두 SUCCESS + 5 source cross-reference 일관 + 재실행 0건 + 신규 trigger 0건). **Step 3 합의 형태 = 옵션 A Reviewer-only 단축 합의** (사용자 명시 결정 — brief §3.4 답습 — 신규 판단 영역 아님). **Step 4 = Skip** (단축 흐름 — 외부 LLM blind 의뢰 0건). **Step 5 Layer C 실 발효 완료** (`eb01bc4` 합의 보고서 610줄 12 섹션 + Reviewer-only 단축 합의 APPROVE + 30 합의 조건 C-ι-1 ~ C-ι-30 + GP-3 + GP-5 동시 발효). **Step 6 메타 갱신 + commit + push 완료** (CONTEXT.md 후속 17 entry + INDEX.md 후속 17 entry + SESSION_2026-05-16.md 신설). **종합 판정 = APPROVE — MVP-1 Implementation Evidence PASS (Layer C) + GP-3 PASS + GP-5 PASS 발효**. **혼동 방지 영구 답습**: MVP-1 PASS (Layer D) = 아직 아님 / Operational Readiness PASS (Layer E) = 아직 아님 / Hermes PMO 격상 (Layer F) = 아직 아님. **사용자 명시 7 금지 위반 영구 답습**: #1 (실 Layer C 발효) = 사용자 명시 Step 5 결정 답습 / #2 ~ #7 모두 0건. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습**. **156 합의 조건 + ADR-011 §2.1 모법 자동 변경 0건**. **추가 0건**: 외부 LLM 자동 호출 / actual run 재실행 / evidence 재생성 / 신규 actual run trigger / R-4 + R-5 + R-7 + R-1 합산 2785줄 본문 변경 / CI workflow 변경 / branch protection 변경 / runtime code 변경 / Phase α-1 ~ α-4 자동 재진입 / Phase β / γ 자동 진입 / Group I / Group β / γ-1 / γ-2 자동 진입 / Backlog #1 ~ #7 자동 진입 / token rotation / GitHub plan 확인 / commit signing / `pull_request_target` / Tier-2/3 확장 / threshold 고정 / event enum 정식 등록 / ADR 본문 자동 갱신 / 신규 ADR 발행 / 실 API/SDK 호출 / Hermes upstream Dockerfile 변경 / Production docker-compose 변경 / 실 secret material commit / 인간 리뷰 의무 자동 발화 / 17 항목 우선순위 자동 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): Layer D / Phase α-1 ~ α-4 실 진입 step 분할 / Phase α 통합 실제 구현 계획 / Group α 재평가 / Group I / token rotation / GitHub plan 가용성 확인 / 세션 종료.
docs/sessions/SESSION_2026-05-16.md:633:| α-1 (R-4) | 829줄 답습 한정 + minor CLI 정렬 후보 | 3 도구 fixture + dry-run + `25728590939/916/977` 답습 | G3-1 + G3-4 + G5-1 + G5-2 + G5-3 (직접 5) | ADR-011 §2.1 (a)~(e) 5/5 PASS Layer C 답습 |
docs/sessions/SESSION_2026-05-16.md:634:| α-2 (R-5) | 35줄 답습 한정 (변경 0건) | Group A 2차 fixture + `lint-imports` dry-run + `25728590916` 답습 | G5-1 + G5-3 + G5-4 + TR-1~TR-5 (직접 3 + TR 5) | ADR-011 §2.1 (a)~(e) 5/5 PASS Layer C 답습 |
docs/sessions/SESSION_2026-05-16.md:635:| α-3 (R-7) | 9 file × 328줄 답습 한정 + α-3.2/3.3 shell CLI 정렬 후보 | GP-3 Stage 2 fixture + shell dry-run + `25731846625` 답습 | G3-3 (직접 1) | ADR-011 §2.1 (a)~(e) 5/5 PASS Layer C 답습 |
docs/sessions/SESSION_2026-05-16.md:744:| 합산 합의 조건 답습 | 222 조건 + ADR-011 §2.1 모법 변경 0건 |
docs/sessions/SESSION_2026-05-16.md:791:T-1 새 권위 결정 / T-2 5 영구 핵심 제약 약화 / T-3 Provider Liquidity 영향 / T-4 ADR-011 §2.1 영향 / T-5 197 합의 조건 변경 / T-6 Hermes ≠ root of trust 영향 / T-7 F-금지 #1 도입 / T-8 합의 영역 변경 — **8/8 발화 0건**.
docs/sessions/SESSION_2026-05-16.md:801:- **C-ξ-6**: 197 합의 조건 답습 + ADR-011 §2.1 모법 변경 0건
docs/sessions/SESSION_2026-05-16.md:953:Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 = **222 조건 변경 0건 영구 답습** + ADR-011 §2.1 모법 변경 0건.
docs/sessions/SESSION_2026-05-16.md:962:- 수단/목적 분리 (ADR-011) ✅
docs/sessions/SESSION_2026-05-16.md:1161:| ADR-011 §2.1 (a)~(e) × R-1 evidence 답습 | ✅ 5/5 답습 충족 (Layer C 답습 한정 — 재검증 0건) |
docs/sessions/SESSION_2026-05-16.md:1384:### 25.3 핵심 framing
docs/sessions/SESSION_2026-05-07.md:70:사용자 단축 합의 (Reviewer-only, ADR-011 §2.4 T2):
docs/sessions/SESSION_2026-05-07.md:87:**금지 범위**: `docker/r4-1-poc/r4_1_poc.py` / Tier-1 42 catalog / trigger UDF regex / redaction config / ADR-011 / ADR-008 / R-7 SOP 본문 / P2 v3 모두 변경 금지.
docs/sessions/SESSION_2026-05-07.md:160:| 4 | R-3 ADR-011 / ADR-008 Amendment 완료 | ✅ |
docs/sessions/SESSION_2026-05-07.md:173:### 5.3 메타 편향 자기진단
docs/sessions/SESSION_2026-05-07.md:242:- 동시 갱신: ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신 PR 묶음
docs/sessions/SESSION_2026-05-07.md:247:- G3: "Hermes ≠ root of trust" 운영 구현 (ADR-011 §2.3 운영 함의 5항목)
docs/sessions/SESSION_2026-05-07.md:256:- ❌ 자동 정책 변경 — ADR-011 §2.4 T3
docs/sessions/SESSION_2026-05-07.md:265:- **Hermes ≠ root of trust** (ADR-011 §2.3, prequel §3 → ADR 권위 승격)
docs/sessions/SESSION_2026-05-07.md:267:- **자동 정책 변경 금지 (T3)** (ADR-011 §2.4)
docs/sessions/SESSION_2026-05-07.md:268:- **수단/목적 분리 원칙** (ADR-011 §2.1 — 본 세션 G1b PASS 도 §2.1 (a)~(d) 4조건 모두 충족 후 승격)
docs/sessions/SESSION_2026-05-07.md:295:- 동시 갱신 후보: ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신 PR 묶음
docs/sessions/SESSION_2026-05-07.md:300:- G3: "Hermes ≠ root of trust" 운영 구현 (ADR-011 §2.3 운영 함의 5항목)
docs/sessions/SESSION_2026-05-07.md:308:- ❌ 추가 정책 변경 금지 (ADR-011 §2.4 T3)
docs/sessions/SESSION_2026-05-07.md:477:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
docs/sessions/SESSION_2026-05-07.md:528:| Hermes ≠ root of trust | ADR-011 §2.3 (영구 권위) | G3 전체 + G2 §9 + G4 §2 + §6 |
docs/sessions/SESSION_2026-05-07.md:530:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | G3 §2.2 (12 T3 항목) + G2 §9 + G4 §5.2 |
docs/sessions/SESSION_2026-05-07.md:531:| 수단/목적 분리 원칙 | ADR-011 §2.1 (a)~(d) → 각 § Exit 기준 (a)~(e) 패턴 | G2 / G3 / G4 모두 답습 |
docs/sessions/SESSION_2026-05-07.md:643:| Hermes ≠ root of trust | ADR-011 §2.3 (영구 권위) | G2+G3+G4 통합 PASS 자체가 ADR-011 §2.3 운영 메커니즘화 답습 |
docs/sessions/SESSION_2026-05-07.md:644:| 메타포 강제 금지 | system-identity-prequel §7 + ADR-011 §2.3 영구 권위 승격 | G4 §2.4 Team/Agent 보류 유지 |
docs/sessions/SESSION_2026-05-07.md:645:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | 12 통합 조건 자체가 T3 차단 답습 (§4 자기참조 차단 + §2.5 보호 대상 등) |
docs/sessions/SESSION_2026-05-07.md:646:| 수단/목적 분리 원칙 | ADR-011 §2.1 (a)~(e) | 본 합의 §6.2 판정 사유 = (a)~(e) 5조건 패턴 답습 |
docs/sessions/SESSION_2026-05-11.md:63:- **T1/T2/T3 발급 권한** (ADR-011 §2.4 답습): T1 (자동) = 본 §10.2 적용 = 본 G4 PASS 후 가능 / T2 (사용자 승인) = schema_version MINOR / MAJOR 증가 시 / T3 (금지) = 자동 증가 / Hermes-originated 증가 / silent drift
docs/sessions/SESSION_2026-05-11.md:79:- **§4.3 #3 행 보강**: schema_version 호환성 행에 `T2 사용자 승인 + §10.2 합의 절차 + §4.5.3 import 검증 절차 통과 의무` cross-reference 추가
docs/sessions/SESSION_2026-05-11.md:82:- **§4.5.3 신설 (Import 시 schema_version 검증 절차 — P-3 흡수)**: Step 1~4 정밀 절차 본문화
docs/sessions/SESSION_2026-05-11.md:83:- **§4.6.5 Import 의무 검증 보강**: §4.5.3 정밀 절차 cross-reference 추가 + Step 5 ledger entry 의무 추가
docs/sessions/SESSION_2026-05-11.md:85:### 3.2 §4.5.3 Step 1~4 정밀 절차
docs/sessions/SESSION_2026-05-11.md:92:### 3.3 §4.5.3 금지 사항 (T3 영역)
docs/sessions/SESSION_2026-05-11.md:97:- ❌ Step 1~3 통과 ledger entry 부재 상태에서 PASS 선언 (G3 §1.3 + §5.3 답습)
docs/sessions/SESSION_2026-05-11.md:99:### 3.4 §4.5.3 본 §가 *하지 않는* 것
docs/sessions/SESSION_2026-05-11.md:108:- ✅ §4.3 / §4.5.2 / §4.5.3 / §4.6.5 본문 정밀 절차 *사양* 본문화
docs/sessions/SESSION_2026-05-11.md:121:- **P-3**: ✅ RESOLVED (2026-05-11) — §4.3 #3 + §4.5.2 + §4.5.3 + §4.6.5 본문 정밀화
docs/sessions/SESSION_2026-05-11.md:145:- ~~❌ P-3 (§4.5 import schema_version 검증) 자동 구현~~ ✅ *사양*까지 흡수 완료 (2026-05-11 §4.5.3 신설 — 실 import 코드 구현은 Implementation/Runtime PASS 영역 별도 합의)
docs/sessions/SESSION_2026-05-11.md:162:| 3 | import schema_version 절차 보강 | ✅ §4.3 #3 + §4.5.2 + §4.5.3 신설 + §4.6.5 + §11.4 P-3 RESOLVED |
docs/sessions/SESSION_2026-05-11.md:177:### 5.3 합의 형식 적정성
docs/sessions/SESSION_2026-05-11.md:182:  - §4.5.3 신설 = §2~§4 본문 갱신 영역 (단축 합의 권고) — *권고 사양* 본문화 자체는 §11.4 P-3 처리 방법 답습
docs/sessions/SESSION_2026-05-11.md:217:- `POLICY_CHANGE` — 권위 위계 (ADR-011 §2.3) Constitution > ADR > SDD > Harness Gates > Hermes
docs/sessions/SESSION_2026-05-11.md:221:- `REDACTION_POLICY_RELAX` — ADR-011 §2.1 본질 + R-4.1 Tier-1 42 catalog
docs/sessions/SESSION_2026-05-11.md:275:- §11.5.3 — 본 §11.5 가 *하지 않는* 것 7 영역 (runtime code / migration script / Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS / G4 전체 PASS 재선언 / ADR 본문 갱신)
docs/sessions/SESSION_2026-05-11.md:288:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신 0건 (cross-reference 깨짐 0건)
docs/sessions/SESSION_2026-05-11.md:390:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 0건
docs/sessions/SESSION_2026-05-11.md:466:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신 0건
docs/sessions/SESSION_2026-05-11.md:475:- 본 작업 = **본문 흡수 한정** — G2 §1.2.3 합산 갱신 + §1.2.5 P11 row strikethrough + §1.2.5.3 갱신 + §1.2.7 신설 (7 sub-section) + 헤더 부속 명시
docs/sessions/SESSION_2026-05-11.md:487:| `docs/architecture/provider-agnostic-memory-skill-design.md` | **§4.3 / §4.4 헤더 / §4.5.2 / §4.5.3 (신설) / §4.6.5 / §10 → §10.1 / §10.2 (신설) / §11.1 / §11.4 / §11.4.4 본문 갱신** (P-1/P-2/P-3 흡수, commit `fd7d625`) + **§3.1 / §3.2 #9 #10 / §3.4.2 (신설) / §3.4.3 (신설) / §3.7 (신설) / §3.8 (신설) / §6.1 갱신 / §11.5 (신설)** (Permission Granularity 세분화 — commits `f0079f2` G4 본문 + `65bfb0c` context) + **§3.7 헤더 / §3.7.3 #18 (신설) / §3.7.4 / §3.8.2 #10 (신설) / §3.8.3 / §6.1 매트릭스 row + 인터페이스 본문 / §11.6 (신설) / 헤더 부속 명시** (Gate Enforcement Layer 보호 cross-reference — commits `3e46440` + `fa2cbdb`) |
docs/sessions/SESSION_2026-05-11.md:489:| `docs/architecture/governance-preconditions.md` | **§1.2.3 합산 갱신 (9 → 10건, P11 추가) / §1.2.5 P11 row strikethrough + cross-reference / §1.2.5.3 갱신 / §1.2.7 (신설 — 7 sub-section, P11 Supply-chain Compromise 정식 등록) / 헤더 부속 명시** (P11 정식 등록 — 2026-05-12 본 작업) |
docs/sessions/SESSION_2026-05-11.md:522:- 2026-05-11: §4.3 #3 + §4.5.2 + §4.5.3 신설 + §4.6.5 P-3 흡수 완료
docs/sessions/SESSION_2026-05-11.md:534:- 2026-05-12: G2 §1.2.3 합산 갱신 (9 → 10건, P11 추가) + §1.2.5 P11 row strikethrough + cross-reference + §1.2.5.3 갱신 + §1.2.7 신설 (7 sub-section — P11 정식 row + 5 Layer enforcement 매핑 + 5 기준 (감지/차단/Evidence/Rollback/사용자 승인) + 처리 범위 + 합의 권위 + 하지 않는 것 13 영역 + G3 §2.6 / G4 §3.7.3 #18 / G4 §3.8.2 #10 cross-reference) + 헤더 부속 명시
docs/architecture/hermes-adoption-design.md:7:> **본 v2 본문 인용은 *역사적 사실 추적* 한정** — 새 작업은 P2 v3 본문을 권위 우선 인용 의무 (P2 v3 §8 carry-over 매트릭스 답습). P2 v2 carry-over 23 영역 = 22 carry-over (변경 없음 — 본 v2 §1.4 ~ §9 본문 그대로 유지) + 1 갱신 (§2.1.3 Pre-Record Redaction Hook 가정 = ADR-011 §2.2 + P2 v3 §1.1 + §3.2 G1a FAIL 권위로 *영구 폐기* — 본 §2.1.3 본문은 *역사적 가정* 으로 보존, 새 작업 *인용 금지*).
docs/architecture/hermes-adoption-design.md:19:> **본 archive 후 5 영구 핵심 제약 보호 강도 = HIGH 5/5** (P2 v3 §10.1 + §10.2 Archive Migration Note 직접 답습) — 5 제약 보호의 모든 권위 출처는 본 v2 *외부* (ADR-011 / ADR-012 / ADR-009 C-N / 헌법 / G2 / G3 / G4 / system-identity-prequel + P2 v3 §10.1) 에 영구 보존.
docs/architecture/hermes-adoption-design.md:31:**관련 ADR**: ADR-009 C-N (자체 Adapter v2.0 진입조건 + P1 facade MVP + Hermes PMO ↔ provider 분리, 2026-05-09 후속 4 갱신), **ADR-010 (SQLCipher Vault HSM 키 관리)**, **ADR-011 (수단/목적 분리 원칙 — 본 v2 §2.1.3 Pre-Record Redaction Hook 가정 영구 폐기 권위)**, **ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 발행)**
docs/architecture/hermes-adoption-design.md:34:> **이하 본문 (§1 ~ §10) = 2026-05-04 v2 확정 시점 사실 보존** (본 archive 처리는 *옵션 A 최소 침습* — 본문 변경 0건). 본 §2.1.3 Pre-Record Redaction Hook 가정은 *역사적 가정* 으로 보존되며, 새 작업의 권위 인용 *금지* (ADR-011 §2.2 + P2 v3 §3.2 G1a FAIL 답습).
docs/architecture/hermes-adoption-design.md:499:  ✓ 미통과 시 §3.4 폴백 ADR 작성 (ADR-011 또는 ADR-008 갱신)
docs/architecture/hermes-adoption-design.md:515:Phase 0 미통과 → ADR-011 작성:
docs/architecture/hermes-adoption-design.md:573:| 5 | OAuth 직결 호출 수 | **0건** (R2-4: Phase 1은 API 키만이므로 자동 PASS — Phase 2 도입 시 §5.3 #6 재검증) | 호출 로그 |
docs/architecture/hermes-adoption-design.md:626:### 5.3 Phase 3 진입 조건
docs/architecture/hermes-adoption-design.md:690:| 1 | Phase 2 exit 조건 모두 | §5.3 |
docs/architecture/hermes-adoption-design.md:716:| **T12 (추가)** | **Phase 진입 전 검증 실패** | Phase 0 또는 Phase N exit 검증 실패 | ADR 재평가 트리거 (§3.4 또는 ADR-011) |
docs/architecture/hermes-adoption-design.md:914:| P2-N4 | 다중 LLM 합의 품질 편차 | MEDIUM | R1-4 메트릭 분리 + §5.3 #1 평가 게이트 |
docs/sessions/SESSION_2026-05-25.md:17:**합계 실 정정 = 10 위치 + 2 cross-ref block (5 파일)**. 본 cycle 머신 변경 0건 (= 측정·빌드·다운로드·설치·sudo·M3·M4 결정 고정·OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss 코드·헌법 본문·ADR-011 본문·MVP-1 합의 본문·메모리 본문·llm-providers (iv-α 자동 제외)·ADR-001~007 (0건)·(P3) 약식 통일·system-identity-prequel·ADR-008·ADR-012·자동 채택·자동 기각·결합 cycle 자동 진입 모두 0건). `tests/jarvis/` 59 green, `src/jarvis/` 커버리지 100% (불변).
docs/sessions/SESSION_2026-05-25.md:45:  4. **항목 4 본문 *근본적* 변경** (실제 line 80 = "본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ... 다른 권위 위계 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무" / brief = "다른 조항과 충돌 시 본 조항이 우선한다." — *commit 148fbbe 후 변경된 실제 본문* 미반영)
docs/sessions/SESSION_2026-05-25.md:50:- gov §1.1 line 78 verbatim "ADR-008 / ADR-011 / system-identity-prequel / 본 v3 모두" 명문 4 source 직접 답습 → system-identity-prequel = (ii-b) 헌법-직접-매핑 범위 *내* 자격 강함
docs/sessions/SESSION_2026-05-25.md:61:**🔴 R-S6 MEDIUM — brief §3.2 ADR-011 line 6 verbatim 순서 부정확 + system-identity-prequel.md §3 참조 *누락***:
docs/sessions/SESSION_2026-05-25.md:67:- **C-1**: 본 cycle 결합 진입 자격 = (g1-N-2) (1) 예외 발효 시점 동형 패턴 (R-13 (4-c) 답습). 단 **단일 차원 (ADR-011 §6) → 결합 차원 (5 후속 cycle 통합) 확장 비대칭** 명문 의무 (B-B1 답습) — N=1 evidence 약함, 본 cycle 강화 결과 = N=2 → 차후 cycle R-13 (4-c) *재* 답습 자격 boundary 명문 의무 (R-12 답습)
docs/sessions/SESSION_2026-05-25.md:126:| `(g1-O)` ADR-011 §6 line 212 본문 정정 | MEDIUM | (g1-N-3) R-S3 답습 영구 의무, ADR-011 본문 추가 정정 = 헌법급 변경 R-9 답습 |
docs/sessions/SESSION_2026-05-25.md:156:**핵심 ⭐⭐⭐ Reviewer 단독 격상 R-S1 (CRITICAL)**: Agent C 단독 발견 + Reviewer raw cross-check 직접 verify — **hermes-not-root-of-trust-runtime.md line 23/176/1040** = gov §1.1 line 78 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") *외* **유일 추가 동형 source** 신규 식별. bash grep verify (`"헌법 제5조 (Provider Liquidity\|헌법 제5조 관용 (Provider Liquidity"`) = ADR-012 + hermes-not-root 단 2 파일. 본 cycle 범위 = **3 → 4 source 확장 발효**.
docs/sessions/SESSION_2026-05-25.md:173:= 측정/빌드/다운로드/설치/sudo/M3·M4 결정/runtime 코드/헌법 본문/ADR-011 본문/ADR-008 본문/ADR-012 본문/sip 본문/hermes-not-root 본문/MVP-1 합의 본문/메모리 본문/(P4) 자동 신설/(11) sub-boundary 자동 신설/결합 cycle 자동 채택/(g1-N-4) framing 진입/(g1-N-3) chain 자동 연장 모두 0건. `tests/jarvis/` 59 green 불변, `src/jarvis/` 커버리지 100% 불변.
docs/sessions/SESSION_2026-05-25.md:186:**🔴 R-S2 HIGH — 헌법 line 80 self-inconsistency**: line 75 "제5조-2" vs line 80 인용 "제5조" = ADR-011 line 6 실제 본문 ("제5조-2") *구 표기 답습*. 본 cycle 범위 외 (Reviewer 권한 한계 (1) 답습 영구), **(g1-O') 별도 cycle carry-over**.
docs/sessions/SESSION_2026-05-25.md:195:- **C-4**: 정정 후 형식 = ADR-011 line 245 "제5조-2 관용 (Provider Liquidity, 비협상)" 모법 (사용자 명시 직접 확인)
docs/sessions/SESSION_2026-05-25.md:229:| (g1-O) ADR-011 §6 line 212 본문 정정 | MEDIUM | 헌법급 변경 R-9 답습 |
docs/sessions/SESSION_2026-05-25.md:230:| **(P3) 약식 통일 cycle** (R-rec-3 답습) | MEDIUM | 본 cycle 채택 형식 = ADR-011 line 245 모법, 다른 source 형식 통일 자격 평가 별도 cycle |
docs/sessions/SESSION_2026-05-25.md:286:| (g1-O) ADR-011 §6 line 212 본문 정정 | MEDIUM | 동상 |
docs/sessions/SESSION_2026-05-25.md:390:> **본 5차 세션 흐름**: (g) entry brief v1 작성·commit (`0867fee`, 311줄) → 사용자 명시 "풀 3+1 합의 + (B) bartowski" → **풀 3+1 합의 (Agent A/B/C 병렬 독립 + Reviewer 통합, `2dad32a`, 423줄, APPROVE w/ COND + BLOCKING 11 + R-S1~R-S4 + 권고 7 + NOTE 11 + 기각 5)** → brief v1.1 보강·commit (`c4457fa`, 311→370줄, BLOCKING 11 verbatim 100% + R-S1~R-S4 흡수) → 사용자 명시 "사전 verify + 다운로드 진행" → HF API verify (repo ID 정정 `Qwen_` prefix + Q4_K_M 45.38 GiB + lfs.sha256 None + imatrix variant 4 발견) → §3.1 사전 조건 (R-1 anchor 9회) → wget 다운로드 (29m22s @ 26.4 MB/s) → §3.3 GGUF tensor verify (843 tensors, ssm_dt.bias ✓ / ssm_beta_alpha ❌ / ssm_ba ✓ / ssm_conv ❌ = 부분 호환) → **측정 시도 + ⭐⭐⭐ 측정 성공** (decode-161tok: prompt 177.9 / decode 32.3 / prefill-2k: prompt 971.9 / decode 31.5 t/s) → R-1 anchor 12회 4 회 모두 일치 ✓ + R-7 격리 확정 → raw artifacts 20 files 정리 → 본 정리 commit.
docs/sessions/SESSION_2026-05-25.md:417:- ✅ /home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf (~45.38 GiB, 새 다운로드)
docs/sessions/SESSION_2026-05-25.md:468:- Q4_K_M 실 크기: 45.38 GiB / 48,727,677,408 bytes
docs/sessions/SESSION_2026-05-25.md:601:- (g) Qwen3-Next 80B 45.38 GiB = 29m22s @ 26.4 MB/s
docs/sessions/SESSION_2026-05-25.md:1118:| 5 | `docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` | 63 (R4 행) | "llama.cpp ↔ Ollama 동급 (MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개)" | "llama.cpp > Ollama" + 49.6/32.3/14.7~15.3 + ~3.24~3.38× + prefill ~24× + Ollama MoE 공개 confirmed + ~4% 정합 + (k) 별도 |
docs/sessions/SESSION_2026-05-25.md:1128:| **헌법 / ADR-011 / 다른 ADR / 다른 architecture / guides / CLAUDE.md 본문 변경 0건 (R-9 답습 영구)** | ✓ `git diff` empty |
docs/sessions/SESSION_2026-05-25.md:1139:- 헌법 / ADR-011 본문 변경 0건 의무 답습 영구 ✓
docs/sessions/SESSION_2026-05-25.md:1238:⭐⭐⭐ **R-S2 CRITICAL** (5 위치): Boss 신뢰 경계 §9.3.2 신규 = Boss 입력 untrusted (R10 + R8) + Boss 출력 텍스트 전용 (R2) + Boss = root of trust 아님 (ADR-011 §2.1 + MVP-1 brief v2 §5) + 워커 실패 advise 미호출 (R8) + advisory failure ≠ health_check failure 분리.
docs/sessions/SESSION_2026-05-25.md:1289:| **헌법 / ADR-011 / 다른 ADR / 다른 architecture (단 boss-abstraction-design.md 신규 제외) / guides / CLAUDE.md 본문 변경 0건 (R-9 답습 영구)** | ✓ |
docs/sessions/SESSION_2026-05-25.md:1314:- Boss = root of trust 아님 (ADR-011 §2.1 + MVP-1 brief v2 §5): 결정적 flag + raw diff + ReviewGuard 권위만 게이트 좌우
docs/sessions/SESSION_2026-05-25.md:1492:| 헌법 / ADR-011 / 다른 ADR / 다른 architecture / guides / CLAUDE.md 본문 변경 0건 (R-9 답습 영구) | ✓ |
docs/architecture/llm-providers-design.md:373:### 5.3 명시 vs 자동
docs/architecture/canary-recheck-design.md:7:**상위 권위**: ADR-011 §2.4 (자동 학습 vs 자동 정책 변경 분리), ADR-011 §3 R-5 매핑
docs/architecture/canary-recheck-design.md:62:**중요 — ADR-011 §2.3 운영 함의 #2 답습**: Hermes redaction (config 체크 #1, #2) 은 *로그/송신* 방어 수단. **DB INSERT 차단 책임은 trigger UDF (R-4.1)** 이다. 따라서 redaction config 체크는 *보조*, *primary* 는 trigger 등록 상태 (#4, #5) 검증.
docs/architecture/canary-recheck-design.md:74:주기 변경은 ADR-011 §2.4 T2 (사용자 승인) — 자동 변경 금지.
docs/architecture/canary-recheck-design.md:84:| **Trigger UDF drift** | `r4_1_poc.py` 또는 운영 환경 trigger SQL 의 패턴 catalog | R-4.1 evidence 갱신 PR + ADR-011 §2.4 T3 절차 |
docs/architecture/canary-recheck-design.md:103:**Catalog 갱신 정책**: ADR-011 §2.4 T3 — Tier-1 catalog 변경은 단축/풀 합의 필수. 본 R-5 는 *catalog 재사용*만 정의, *catalog 변경 정책*은 ADR-011 §2.4 권위 답습.
docs/architecture/canary-recheck-design.md:139:| 5 | **Trigger UDF 변경** | `r4_1_poc.py` / 운영 trigger SQL diff 시 | Tier-1 catalog 또는 alternation regex 변경 PR | pre-commit hook + ADR-011 §2.4 T3 절차 강제 |
docs/architecture/canary-recheck-design.md:150:| #5 trigger UDF | PR merge 차단 + ADR-011 §2.4 T3 절차 강제 |
docs/architecture/canary-recheck-design.md:180:### 5.3 PARTIAL
docs/architecture/canary-recheck-design.md:186:- 단축 합의 trigger (ADR-011 §2.4 T2)
docs/architecture/canary-recheck-design.md:198:- 단축/풀 합의 trigger (ADR-011 §2.4 T3 적용 — Hermes 자체 정책 변경 금지)
docs/architecture/canary-recheck-design.md:213:ROLLBACK 후에는 ADR-011 §2.4 T3 절차로 trigger UDF / hermes 버전 / config 변경 재검토 (단축 또는 풀 합의 의무).
docs/architecture/canary-recheck-design.md:246:ADR-011 §2.3 + system-identity-prequel §3 — Hermes PMO 격상은 4 게이트 통과 필수.
docs/architecture/canary-recheck-design.md:254:본 §6.4 는 R-5 trigger 의 *방어선* 역할. 격상 결정 자체는 ADR-011 §2.4 T3 (자동 정책 변경 금지) 적용 — 자동 격상 금지.
docs/architecture/canary-recheck-design.md:330:## 8. 자동 정책 변경 금지 (ADR-011 §2.4 운영 적용)
docs/architecture/canary-recheck-design.md:346:| Code level | `r4_1_poc.py` (또는 운영 trigger SQL) 의 변경은 git commit + 단축/풀 합의 거쳐야만 적용 (ADR-011 §2.4 T3) |
docs/architecture/canary-recheck-design.md:348:| Config level | `HERMES_REDACT_SECRETS=false` 자동 설정 시도 감지 → ADR-011 §2.4 T3 위반 alert + 단축/풀 합의 의무 |
docs/architecture/canary-recheck-design.md:356:| Tier-1 catalog 기존 vendor 제거 | **풀 3+1 합의** (보안 약화 가능성) | recheck 재실행 + ADR-011 amendment |
docs/architecture/canary-recheck-design.md:361:| Hermes redaction config 변경 | **ADR-011 §2.4 T3 절대 금지** — 단축/풀 합의 필수 | ADR-011 amendment |
docs/architecture/canary-recheck-design.md:365:## 9. ADR-011 §2.4 / §3 R-5 매핑 결과
docs/architecture/canary-recheck-design.md:375:> ADR-011 §3 R-5 매핑: "Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현"
docs/architecture/canary-recheck-design.md:377:| ADR-011 §3 R-5 의무 | 본 R-5 § |
docs/architecture/canary-recheck-design.md:396:| #5 UDF 변경 | pre-commit + Actions push trigger on `r4_1_poc.py` change + ADR-011 §2.4 T3 강제 |
docs/architecture/canary-recheck-design.md:428:- ADR-011 §2.4 자동 학습 vs 자동 정책 변경 분리의 *운영 메커니즘* 설계 완료
docs/architecture/canary-recheck-design.md:434:- §8 정책 변경 매트릭스로 ADR-011 §2.4 T1/T2/T3 운영 적용 절차 정의
docs/architecture/canary-recheck-design.md:448:- §8 정책 변경 매트릭스는 ADR-011 §2.4 답습 — 본 R-5 가 정책 변경의 *분류 기준* 변경하지 않음. 분류 자체 변경은 ADR-011 amendment
docs/architecture/canary-recheck-design.md:450:- **본 R-5 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 답습) — Hermes 는 검증 대상이며 본 R-5 는 검증 외부화의 trigger 메커니즘 정의
docs/architecture/canary-recheck-design.md:457:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 (자동 학습 vs 자동 정책 변경 분리), §3 R-5 매핑
docs/sessions/SESSION_2026-05-24.md:1:# SESSION 2026-05-24 — V-1 PoC Phase 2 cycle + M3·M4 단독 미충족 합의(3+1) + Phase 3 entry brief v1·합의(3+1)·v1.1 + **Phase 3 실 빌드 cycle (정공법, 측정 차단)** + **Provider Liquidity deep-dive 합의 cycle (3+1, APPROVE w/ COND BLOCKING 13)** + **format 가족별 분류 cycle (f-K, 3+1, APPROVE w/ COND BLOCKING 16, Reviewer 단독 격상 3)** + **(g1-A) 채택 cycle (5차 entry, 3+1, APPROVE w/ COND BLOCKING 16, Reviewer 단독 격상 3 R-S1·R-S2·R-S3)** + **(g1-N) 헌법 5조-2 신설 자격 평가 cycle (6차 entry, 3+1, APPROVE w/ COND BLOCKING 22, Reviewer 단독 격상 5 R-S1~R-S5)** + ⭐⭐⭐ **(g1-N-1) 헌법 5조-2 본문 변경 commit cycle (7차 entry, 3+1, APPROVE w/ COND BLOCKING 14, Reviewer 단독 격상 4 R-S1~R-S4, R-19 답습 단계 (4) 직접 적용 = 본 세션 + 본 프로젝트 최초 + 유일 헌법 본문 변경 commit `148fbbe`)** + ⭐⭐⭐ **(g1-N-2) ADR-011 line 6/245 매핑 정정 cycle (8차 entry, 3+1, APPROVE w/ COND BLOCKING 10, Reviewer 단독 격상 3 R-S1~R-S3, R-19 답습 단계 (4) 직접 적용 = 본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit `3bdb1be`, Reviewer 권한 한계 (1) 예외 자격 발효 시점)** + ⭐⭐ **(g1-N-3) CLAUDE.md / roadmap.md 정합 정정 자격 평가 cycle (9차 entry, 3+1, APPROVE w/ COND BLOCKING 12, Reviewer 단독 격상 4 R-S1~R-S4, R-19 답습 단계 (4) 직접 적용 = (i) 최소 정정 채택 CLAUDE.md line 244 + roadmap.md line 64/65 단일 atomic commit `afd1a65`, Reviewer 권한 한계 8 → 9 격상 + (9) 신규 CLAUDE.md / roadmap.md 본문 정정 자격 boundary 발효)**
docs/sessions/SESSION_2026-05-24.md:7:**V-1 PoC Phase 2 EXECUTED → M3·M4 결정 *고정* 자격 풀 3+1 단독 미충족 합의 (BLOCKING 5) → Phase 3 정공법 entry brief v1 → 풀 3+1 합의 (APPROVE w/ COND, BLOCKING 7 + 권고 25 + NOTE 11) → brief v1.1 보강 → 세션 1차 정리 → ⭐ Phase 3 실 빌드 cycle (정공법) 진입 → 빌드 100% 성공 4.6분 (sm_120a+sm_121a SASS 모두 포함 verify) → 측정 §2.5 분기 발동 (`missing tensor 'blk.0.ssm_dt.bias'`, GGUF format 호환성 차단) → (iii)(iv) 직접 측정 0건 → 본 cycle 종료, raw 17 파일 보존 → 세션 2차 정리·commit·push → ⭐ Provider Liquidity deep-dive 합의 cycle 진입 (사용자 "(d)") → entry brief v1 (407줄, `9ed376a`) → 풀 3+1 합의 (`a9e1e88`, APPROVE w/ COND, BLOCKING 13 + 권고 17 + NOTE 12, 기각 0) → brief v1.1 보강 (407→518줄, `8ae1ab6`, BLOCKING 13 verbatim 100% + 권고 17 본문 직접 반영) → 세션 3차 정리 → ⭐ **format 가족별 분류 cycle (f-K) 진입 (사용자 "(f-K)") → brief v1 (`f305174`, 556줄, Provider Liquidity 합의 R-26 + R-11 답습 후속) → 풀 3+1 합의 (`d75dceb`, 397줄, APPROVE w/ COND, BLOCKING 16 + 권고 21 + NOTE 24, 기각 0, Reviewer 단독 격상 3) → brief v1.1 보강 (556→710줄, `eca4cf5`, BLOCKING 16 verbatim 100% + 권고 21 본문 직접 반영 + NOTE 12→24 + 6축 framing) → 세션 4차 정리** → ⭐ (g1-A) 채택 cycle (5차 entry, brief v1 `fc6731e` → 합의 `d0f516d` BLOCKING 16 + Reviewer 격상 3 → brief v1.1 `bdcc3a6` → 5차 정리 `2ff09d6`) → ⭐ **(g1-N) 헌법 5조-2 신설 자격 평가 cycle (6차 entry, 사용자 "(g1-N)" + 정공법 + 범위 "5조-2 신설 분리" 선택, 헌법급 변경 R-9 답습 영구 의무 cycle) → brief v1 (`6f64491`, 542줄, (g1-A) 합의 §7.1 (g1-N) 옵션 채택 자격 평가) → 풀 3+1 합의 (`1ec9c5e`, 401줄, APPROVE w/ COND, BLOCKING 22 + 권고 17 + NOTE 25, 기각 0, Reviewer 단독 격상 5 R-S1 = 헌법 line 97~98 자기-구속 명문 누락 / R-S2 = 후보 (iii) "관용" 의미 충돌 위험 후보 / R-S3 = ADR-008 부록 B framing 정정 (ADR↔ADR 모법, 헌법↔헌법 아님) + 헌법 8-2조 패턴 선례 / R-S4 = MEMORY.md 24.4KB → 26.7KB 초과 / R-S5 = §0 ↔ §10.1 §3·§4 vs §3·§4·§5·§8 비대칭 R-S3 답습 영구 위반) → brief v1.1 보강 (542→780줄, `58e06d5`, +487/-249, BLOCKING 22 verbatim 100% + 권고 17 본문 직접 반영 + NOTE 29 → 54 by-reference + §2.5 ADR-008 부록 B verbatim 신규 + §3.5 7×6=42 cell 매트릭스 신규 + §4 본문 후보 4→7 확장 + §4.8 위치 후보 3→4 확장 + §5 긴장 4→5 + §6.3 Reviewer 권한 한계 7→8 격상 + §8.0 4 cycle chain trace 신규 + §9 정직성 18→22) → 세션 6차 정리**. HEAD = 본 6차 정리 commit (commit 별도 명시 의무). `tests/jarvis/` 59 green, `src/jarvis/` 커버리지 100% (불변). **머신 변경 0건 (본 (g1-N) cycle = 헌법급 변경 *제안* + 자격 평가 cycle, 측정·빌드·다운로드·설치·sudo·M3·M4 결정 고정·OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss 코드·헌법·ADR-011·ADR-008·MVP-1·메모리 본문 자동 정정·Provider Liquidity 본질 약화·4 가족 분류 + 6축 framing 영구 정착·(g1-N) 자체 영구화 정착·자동 채택/자동 기각·결합 cycle 자동 진입 모두 0건 R-S1~R-S5 답습. 실 헌법 본문 변경 = (g1-N-1) 별도 단계 + 사용자 명시 의무).**
docs/sessions/SESSION_2026-05-24.md:25:| ⭐ **Provider Liquidity deep-dive entry brief v1** (사용자 "(d)" 명시) | 분석 대상 = Phase 1+1.5+2+3 통합, 권고 자격 = 진단+권고 옵션 매트릭스 (결정 *고정* 0). §0 자격 / §1 동기 (Phase 3 finding trigger + MVP-1 R4·C-2 긴장 + 헌법 본문 매핑 + ADR-011 §2.1 적용) / §2 evidence 통합 (P1-F1~F4 / P1.5-F1~F3 / P2-F1~F3 / P3-F1~F7) / §3 SDD 정합성 매트릭스 / §4 4축 / §5 분담안 / §6 출력 형식 / §7 (A)~(M) 13 옵션 / §8 정직성 한계 / §9 차단 조건 / §10 NOTE / §11 다음 단계. 407줄 | `9ed376a` |
docs/sessions/SESSION_2026-05-24.md:26:| ⭐ **Provider Liquidity deep-dive 풀 3+1 합의** (사용자 "(A)" 명시) | Agent A (구현 분석가) / B (품질·안전성) / C (대안 탐색가) 병렬 독립 → Reviewer 통합. **APPROVE w/ COND, BLOCKING 13 + 권고 17 + NOTE 12 (기각 0)**. 3 에이전트 단독 발견 9 + Reviewer 단독 R-S1 ⭐ ADR-011 line 6/245 verbatim "헌법 제5조 (Provider Liquidity)" 직접 권위 매핑 발견 → brief §1.4 진단 의무 1 ("동형 해석") 부정확 → reframing 의무. R-3 ⭐ 3 에이전트 일치 = 4 수준 framing self-citation anchor + 시간축 missing dimension + 비교 자격 1/4. 301줄 | `a9e1e88` |
docs/sessions/SESSION_2026-05-24.md:27:| ⭐ **Provider Liquidity deep-dive brief v1.1 보강** | BLOCKING 13 verbatim 본문 직접 반영 100% + 권고 17 본문 직접 반영 (R-14~R-30) + NOTE 12 §10 표 carry-over + §11 변경 일람 표 신규. R-13 reframing — §1.4 "동형 해석" → ADR-011 line 6/245 "관용 매핑" 권위 답습. R-3 reframing — §4 머리 framing 임시성 + §4.5 시간축 5번째 축 신규. R-7 — model loading 5 sub-차원 분해. R-11 — GGUF 가족 한정 evidence 명문. R-4 — case C (means+ends 양면) 분기 추가. 407 → 518줄 (+243 / -132) | `8ae1ab6` |
docs/sessions/SESSION_2026-05-24.md:29:| ⭐ **format 가족별 분류 cycle entry brief v1** (사용자 "(f-K)" 명시) | Provider Liquidity 합의 R-26 (C-R2) + R-11 답습 후속. §0 자격 (하는 것 13 + 하지 않는 것 11) / §1 동기 (R-26 + R-11 + R-13 + ADR-011 §2.1) / §2 evidence (Phase 3 raw + Provider Liquidity 합의 + 4 가족 외부 식별 추정) / §3 SDD 정합성 매트릭스 / §4 5축 framing (가족 내부 / 가족 간 / 분리 자격 / 시간축 / 본 framing 임시성) / §5 분담안 (Q-A1~4 + Q-B1~5 + Q-C1~5) / §6 출력 형식 / §7 옵션 (A)~(M) + DEFER (D1)~(D4) / §8 정직성 한계 16 / §9 차단 / §10 NOTE / §11 다음 단계. 556줄 | `f305174` |
docs/sessions/SESSION_2026-05-24.md:30:| ⭐ **format 가족별 분류 cycle 풀 3+1 합의** (사용자 "(A)" 명시) | Agent A (구현 분석가) / B (품질·안전성) / C (대안 탐색가) 병렬 독립 → Reviewer 통합. **APPROVE w/ COND, BLOCKING 16 + 권고 21 + NOTE 24 (기각 0)**. 3 Agent 모두 REVISE 일치, 정면 충돌 0건 = 강한 정합성. **Reviewer 단독 격상 3건 ⭐**: R-S1 (A-S1 격상, Phase 3 raw `conversion/qwen.py:299-300` cross-check → P3-F1 = 시점 부정합 finding ≠ "GGUF 가족 본질 부정") + R-S2 (C-B3 격상, ADR-011 §6 line 212 "Provider Liquidity 영향 무관" vs line 6/245 직접 권위 매핑 내부 비대칭) + R-S3 (B-S5 ⭐⭐ 격상, §0 "하지 않는 것" 12 항목 vs §9.1 차단 6 항목 비대칭 self-consistency 정직성 risk). **2 Agent 일치 BLOCKING 3**: R-1 분류 *기준* 단일축 부재 (A+C) / R-2 self-citation 후속 매핑 (B+C) / R-3 Phase 3 R-5 답습 누락 (B+C). 397줄 | `d75dceb` |
docs/sessions/SESSION_2026-05-24.md:33:| ⭐ **(g1-A) 채택 cycle entry brief v1** (사용자 "(g1-A)" + 정공법 선택, 5차 entry) | format 합의 §7.1 (A) 옵션 채택 자격 평가 entry brief. §0 *하는 것* 12 ↔ *하지 않는 것* 12 1:1 매핑 (R-15 = R-S3 답습) / §1 trigger + 핵심 질문 Q1~Q4 / §2 evidence — 합의 결과 by-reference + (g1-A) 의미 5 차원 분해 + brief v1.1 framing 임시성 *기존* 명문 6 위치 매핑 + 답습 의무 6 항목 / §3 SDD 정합성 매트릭스 (헌법/ADR-011/MVP-1 R4/메모리 본문 변경 0건) / §4 4축 분석 — (1) 적용 자격 / (2) 임시성 *재* 강화 / (3) 비-결정성 / (4) (g1-A) 자체 영구화 risk / §5 3+1 분담안 + Reviewer 권한 한계 7 항목 / §7 후속 carry-over 옵션 매트릭스 / §8 정직성 한계 16 / §9 차단 §0 1:1 매핑 + §9.5 6축 framing self-citation anchor 차단 / §10 NOTE 36 by-reference only (재서술 0건). 397줄 | `fc6731e` |
docs/sessions/SESSION_2026-05-24.md:34:| ⭐ **(g1-A) 채택 cycle 풀 3+1 합의** (사용자 "(A)" 명시) | Agent A (구현 분석가) / B (품질·안전성) / C (대안 탐색가) 병렬 독립 → Reviewer 통합. **APPROVE w/ COND, BLOCKING 16 + 권고 18 + NOTE 29 (기각 0)**. 3 Agent 모두 APPROVE w/ COND 일치, 정면 충돌 0건 = 강한 정합성. **Reviewer 단독 격상 3 (raw line-level direct cross-check)**: ⭐⭐⭐ **R-S1 (C-S4 격상)** — 메모리 line offset 부정합. 실제 line 14 verbatim = "단일 provider 의존 시스템 금지 — 최소 2 provider always-on 원칙". brief v1 + brief v1.1 + format 합의 R-13 모두 "line 13" 인용 오류, 정정 chain carry-over 의무. ⭐⭐ **R-S2 (B-B1 + B-S1 격상)** — 헌법 5조 line 40~46 verbatim = "코드 품질 원칙" + 5 항목 (Provider Liquidity 직접 본문 부재). ADR-011 line 6/245 *매핑* 의존 = format 합의 R-S2 의 *상위 단계* 비대칭. Reviewer 권한 한계 (헌법 본문 정정 자격 0) 답습. ⭐⭐ **R-S3 (B-B8 격상)** — §0 #12 NOTE 합산 오류. format 합의 NOTE 24 = Provider Liquidity 12 *내포 합산*. 정확 = 24 + Phase 3 11 = **35 비중복**. **2+ Agent 일치 BLOCKING 2**: R-1 (A-B1 + B-B2 + C-B1 **3-way** 일치) 추가 산출 boundary 모호·자명성·재서술 self-위반 risk / R-2 (A-B2 + C-B2 2-way) §7 매트릭스 비대칭 + (g1-N)/(g1-O) 권위 본문 미세 보강 옵션 누락. 343줄 | `d0f516d` |
docs/sessions/SESSION_2026-05-24.md:35:| ⭐ **(g1-A) 채택 cycle brief v1.1 보강** | BLOCKING 16 verbatim 본문 직접 반영 100% (R-21 답습) + 권고 18 본문 직접 반영 또는 §10 NOTE carry-over + NOTE 24 → **35 비중복 + 본 cycle 신규 5 (N-25~N-29) = 40 by-reference only** (R-9 = R-S3 답습 정정 36 → 35) + §7.1 **(g1-N)/(g1-O) 헌법/ADR-011 본문 미세 보강 옵션 신규** (R-2) + §9.6 신규 — 후속 cycle 본 brief 인용 자격 by-reference *진술* only (R-6) + §7.5 우선순위 권고 자격 신규 (R-29) + §11 위치 분리 (§11.1 변경 일람 표 + §11.2 다음 단계, R-10) + §3.3 메모리 line 12~17 verbatim 6 행 신규 (R-S1 정정 chain) + §3.1 ADR-011 매핑 4 차원 분리 (R-S2) + §0 #12 + §10 NOTE 36 → 35 (R-S3). 397 → 537줄 (+255 / -115) | `bdcc3a6` |
docs/sessions/SESSION_2026-05-24.md:42:| ⭐⭐⭐ **(g1-N-2) ADR-011 line 6/245 매핑 정정 cycle (8차 entry, 사용자 "(g1-N-2)" + 정공법 + 단독 범위 명시)** | (g1-N-1) commit 후속 carry-over cycle. R-9 답습 영구 의무 (g1-N-2) carry-over 직접 발효 + Reviewer 권한 한계 (1) "ADR-011 §6 본문 정정 자격 0" 예외 자격 발효 시점 (R-13 (4-c) 동형 패턴 적용) | (g1-N-2) cycle commits 아래 |
docs/sessions/SESSION_2026-05-24.md:44:| (g1-N-2) 풀 3+1 합의 (단계 (3)) | **APPROVE w/ COND, BLOCKING 10 + 권고 10 + NOTE 11, 기각 0**. 정면 충돌 0건. 2+ Agent 일치 BLOCKING 2 (R-1 + R-3). **Reviewer 단독 격상 3 ⭐ R-S1~R-S3** (raw line-level direct cross-check): R-S1 ⭐⭐⭐ (line 245 entire verbatim 부분 추출 — bullet + path + 8조 prefix 포함, 가장 큰 finding) + R-S2 ⭐⭐ (헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off 신규 발효 — (g1-N-3') 별도 cycle 의무 carry-over 영구) + R-S3 ⭐⭐ ("비협상" 명문 추가 boundary = 매핑 정정 *및* 헌법 line 75 verbatim 직접 답습 한정). 303줄 | `07cd3f4` |
docs/sessions/SESSION_2026-05-24.md:45:| ⭐⭐⭐ **(g1-N-2) brief v1.1 + ADR-011 line 6/245 매핑 정정 단일 atomic commit (단계 (4) 직접 적용 완료)** ⭐⭐⭐ | **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit (Reviewer 권한 한계 (1) 예외 자격 발효 시점)**. ADR-011 line 6: "헌법 제5조 (Provider Liquidity)" → "헌법 제5조-2 (Provider Liquidity, 비협상)" + ADR-011 line 245: "제5조 관용" → "제5조-2 관용" 2 위치 정정. brief v1.1 (488 → 519줄, 보강): BLOCKING 10 verbatim 100% (R-21 답습) + 권고 10 본문 반영 + NOTE 11 (N-70~N-80) + §11.1 chain trace 7번째 cycle entry + §2.4 임시 stale 양방향 trade-off 표 신설 (R-S2). commit message: `docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)` (Conventional Commits + 단일 atomic commit 2 파일) | `3bdb1be` |
docs/sessions/SESSION_2026-05-24.md:47:| ⭐ **(g1-N) 헌법 5조-2 신설 자격 평가 cycle entry brief v1** (사용자 "(g1-N)" + 정공법 + 범위 "5조-2 신설 분리" 선택, 6차 entry, 헌법급 변경 R-9 답습 영구 의무 cycle) | (g1-A) 합의 §7.1 (g1-N) 옵션 채택 자격 평가 entry brief. §0 *하는 것* 12 ↔ *하지 않는 것* 12 1:1 매핑 (R-15 = R-S3 답습) / §1 trigger + 핵심 질문 Q1~Q4 / **§1.4 R-9 헌법급 변경 답습 영구 의무 7 항목 명문** / §2 evidence — (g1-A) 합의 carry-over + 헌법 5조 line 40~46 verbatim + ADR-011 line 6/212/245 + 메모리 line 7/14 + **§2.5 ADR-008 부록 B Amendment 패턴 답습 자격** / §3 SDD 정합성 매트릭스 — 헌법/ADR-011/MVP-1/메모리 + **ADR-008 부록 B 답습 자격** + **ADR-011 §2.1 (a)~(e) 답습 자격** / §4 **5조-2 본문 *후보 4 multiple* + *위치 후보 3 multiple*** / §5 4 긴장 분석 / §6 3+1 분담안 + Reviewer 권한 한계 7 항목 영구 답습 (4 cycle carry-over chain) / §7 합의 출력 형식 + raw cross-check 8 source / §8 후속 매트릭스 — **(g1-N-1) 실 헌법 본문 변경 commit (별도 단계, 사용자 명시 의무)** + (g1-N-2) (g1-O) cycle + (g1-N-3) CLAUDE.md/roadmap + DEFER/기각 / §9 정직성 한계 20 / §10 차단 12 + §10.5/§10.6 신규 / §11 NOTE 40 by-reference + R-S1 정정 chain carry-over 의무 / §12 §12.1 변경 일람 + §12.2 다음 단계 (7 단계, 7번째 = 실 헌법 본문 변경 별도 단계). 542줄 | `6f64491` |
docs/sessions/SESSION_2026-05-24.md:48:| ⭐ **(g1-N) 헌법 5조-2 신설 자격 평가 cycle 풀 3+1 합의** (사용자 "(A)" 명시) | Agent A (구현 분석가) / B (품질·안전성) / C (대안 탐색가) 병렬 독립 → Reviewer 통합. **APPROVE w/ COND, BLOCKING 22 + 권고 17 + NOTE 25 (기각 0)**. 3 Agent 모두 APPROVE w/ COND 일치, 정면 충돌 0건 = 강한 정합성. **Reviewer 단독 격상 5 (raw line-level direct cross-check)**: ⭐⭐⭐ **R-S1 (A-B1 + C-S3 격상)** — 헌법 line 97~98 자기-구속 명문 누락 (line 97 "이 헌법은 프로젝트의 모든 활동에 우선한다" + line 98 "헌법 수정은 반드시 3+1 에이전트 합의를 거쳐야 한다" = 본 cycle 직접 모법). ⭐⭐ **R-S2 (B-B1 + B-S2 격상)** — 후보 (iii) "관용" + "비협상" 동시 제목 의미 충돌 = Provider Liquidity 본질 약화 risk 강함 = 위험한 후보 분류. ADR-011 §6 line 212 "무관" 동의어 = ADR-011 *자체* stance. ⭐⭐ **R-S3 (B-B3 + B-S1 + A-B2 + B-B4 격상)** — ADR-008 부록 B framing 정정 (ADR ↔ ADR amendment 패턴 모법, 헌법 ↔ 헌법 모법 *아님*) + 헌법 line 67~73 "제8-2조" 패턴 선례 = (e) 후속 패턴 강한 evidence. ⭐ **R-S4 (C-S4 + C-B5 격상)** — MEMORY.md system reminder verbatim "26.7KB (limit: 24.4KB)" 답습 명문 부재 + 본 cycle 결과 메모리 신규 entry 등재 자격 평가 명문 부재. ⭐⭐ **R-S5 (A-S3 + B-B7 + B-S3 3-way 격상)** — §0 #11 ↔ §10.1 #11 §3·§4 vs §3·§4·§5·§8 비대칭 = R-15 = R-S3 답습 영구 의무 직접 위반. **2+ Agent 일치 BLOCKING 4**: R-1 (ADR-008 framing + verbatim 인용 부재) / R-2 ("우선한다" 본 cycle 범위 초과) / R-8 (본문 후보 (v)~(vii) 추가 식별) / R-9 (위치 후보 (d) ADR 신설 우회 식별). **3-way 일치 BLOCKING 1**: R-5 (§0 ↔ §10.1 비대칭, A-S3 + B-B7 + B-S3). 401줄 | `1ec9c5e` |
docs/sessions/SESSION_2026-05-24.md:49:| ⭐ **(g1-N) cycle brief v1.1 보강** | BLOCKING 22 verbatim 본문 직접 반영 100% (R-21 답습) + 권고 17 본문 직접 반영 또는 §11 NOTE carry-over + NOTE 29 → **54 by-reference only** (carry-over 29 + 본 cycle 신규 25 N-30~N-54, R-29 답습 강한 변형) + **§2.5 ADR-008 부록 B verbatim 신규** (R-S3 답습, B.1~B.6 line 153/155/157/180/224/228) + **§3.5 후보 7×ADR-011+ADR-008 = 42 cell 매트릭스 신규** (R-24 답습) + **§4 본문 후보 4 → 7 확장** ((v) ADR-011 line 6 답습 / (vi) 1 줄 / (vii) 메모리 line 12~17 7 항목 답습, R-8 답습) + **§4.8 위치 후보 3 → 4 확장** ((d) ADR 신설 우회, R-9 답습) + **§5 긴장 4 → 5** ((g1-N+O) 결합 + cycle 자체 대안 + Phase 3 R-5 동형, R-6 + R-7 + R-15) + **§6.3 Reviewer 권한 한계 7 → 8 격상** ((8) 결합 cycle 진입 자격 평가 자격 0, R-7 신규) + **§8.0 4 cycle chain trace 신규** (R-23 답습) + **§9 정직성 18 → 22 항목** (R-S4 MEMORY.md + R-17 verify 자격 0 신규) + §10.1 §0 1:1 매핑 R-S5 정합화 (§3·§4 → §3·§4·§5·§8) + §12 위치 분리 (§12.1 변경 일람 + §12.2 다음 단계). 542 → 780줄 (+487 / -249) | `58e06d5` |
docs/sessions/SESSION_2026-05-24.md:53:| (g1-N-3) 풀 3+1 합의 (단계 (3)) | **APPROVE w/ COND, BLOCKING 12 + 권고 16 + NOTE 10 신규, 기각 0**. 3 Agent 모두 APPROVE w/ COND 일치, 정면 충돌 0건 = 강한 정합성. **4-way 일치 BLOCKING 1 (R-1 = §1.4 ↔ §6.3 분해 매핑 표 본문 부재, A-B1 + B-B3 + B-S2 + C-B3)**. **Reviewer 단독 격상 4 ⭐ R-S1~R-S4 (raw line-level direct cross-check)**: R-S1 ⭐⭐⭐ (A-S2 격상, §2.3 line 143~146 라벨 ↔ §4.1 (i)~(iv) 매트릭스 내부 모순, line 143/144/145 (i) → (iii)/(ii)/(iii) 라벨 정정 의무) + R-S2 ⭐⭐ (A-S1 격상, CLAUDE.md grep "Provider Liquidity"/"5조-2"/"제5조" verbatim **0 matches** 정량 evidence — 본 commit 후 line 244 1 위치만 reference 추가) + R-S3 ⭐⭐ (헌법 line 80 + ADR-011 line 212 + hermes v3 line 13 3-way trade-off carry-over 영구 — (g1-N-3') / (g1-O) / (g1-N-3-hermes) 3 후속 cycle 의무) + R-S4 ⭐⭐⭐ (C-S1 격상, provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 "Provider Liquidity 4-way Multi-layer Defense" 헌법-동급 권위 → (g1-N-3-pamsd) 신규 분리 HIGH carry-over). **2+ Agent 일치 BLOCKING 2**: R-10 (B-B4 + B-S5 + C-S4 2+ 일치, anchor depth limit 9-cycle entry 비추론 차단) / R-11 (B-S4 + C-B1 부분 일치, framing "8 → 9 격상" vs "9 항목 영구 답습" 통일). 423줄 | `386c552` |
docs/sessions/SESSION_2026-05-24.md:54:| ⭐⭐ **(g1-N-3) brief v1.1 + CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 단일 atomic commit (단계 (4) 직접 적용 완료)** | **사용자 명시 "(i) 최소 정정" 채택 (Reviewer R-rec-15 권고 답습)**. 본 commit 변경 3 파일: (1) **CLAUDE.md line 244**: "헌법 8조 본질" → "**헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질 ... 상위 권위 매핑 답습 (ADR-011 line 6/245 + 헌법 line 75~80)**" + (2) **roadmap.md line 64** (GP-5): "HIGH (Provider Liquidity 5-way Layer 1 모법)" → "HIGH (**헌법 5조-2 Provider Liquidity 5-way Layer 1 모법**)" + (3) **roadmap.md line 65** (GP-6): "MEDIUM (P8 + Provider Liquidity Layer 4 — Provider 교체 자유)" → "MEDIUM (P8 + **헌법 5조-2 Provider Liquidity Layer 4 — Provider 교체 자유**)" + (4) brief v1.1 (522 → 608줄, +86줄): BLOCKING 12 verbatim 100% (R-21 답습) + R-S1~R-S4 verbatim 영구 + (i) 채택 적용 결과 + §1.4.1 분해 매핑 표 본문 신설 (R-1) + §10.5/§10.6 본문 신설 (R-2) + §10.1 의미적 한계 인정 (R-12) + §2.3 라벨 정정 (R-3 + R-S1) + §1.5 framing 통일 (R-11) + §6.3 (9-d) 차단 메커니즘 본문 (R-9) + §2.7/§8.2 (g1-N-3-pamsd) HIGH + (g1-N-3-hermes) MEDIUM → HIGH 격상 + MEMORY.md cleanup depth 4 cycle 누적. Reviewer 권한 한계 (9) 신규 예외 자격 발효 직접 적용 완료 (R-13 (4-c) 동형 패턴 + (1)(4) chain). commit message: `docs(claude/roadmap): (g1-N-3) CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 — 헌법 5조-2 reference 추가` (Conventional Commits + 단일 atomic commit 3 파일) | `afd1a65` |
docs/sessions/SESSION_2026-05-24.md:68:- **NOTE 11 (N-1~N-11)**: ADR-011 §2.1 5조건 carry-over / M3 결정 문구 "Gated DeltaNet" verbatim / OllamaBoss·LlamaCppBoss 0건 / R-15 gap-pull SOP carry-over / B hybrid fallback SOP 미수립 / github.com redirect chain ss 한정 / toolchain 변경 carry-over / 옵션 E trigger 자격 별도 / Provider Liquidity 후속 cycle / PTX forward-compat boundary 추정 한정 / anchor 회차 번호 검증.
docs/sessions/SESSION_2026-05-24.md:110:- 🔴 **R-13 ⭐ Reviewer 단독 (가장 강한 reframing)**: **ADR-011 line 6 verbatim** = `**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), ...` + **line 245 verbatim** = `제5조 **관용** (Provider Liquidity, 비협상)` 직접 권위 매핑 발견. brief v1 §1.4 "헌법 5조 매핑은 동형 해석, 직접 매핑은 8-2조" 진단 = ADR-011 *해석 권위* 비참조 → **부정확**. 헌법 본문 (5조 = 코드 품질) 외 ADR-011 의 "관용 매핑" 으로 정착됨. brief v1.1 §1.4·§3.1·§7.1 (C) reframing 의무.
docs/sessions/SESSION_2026-05-24.md:111:- 🔴 **R-3 ⭐ 3 에이전트 일치 (다른 입구 동일 식별)**: 4 수준 framing self-citation anchor + 시간축 missing dimension + 비교 자격 1/4 명시 결여. A-B3 = 비교 자격 1/4 / B-B1 = self-citation anchor (ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재) / C-B1 + C-S1 = 시간축 (변환·빌드 시점 의존) missing dimension, P3-F1 evidence 강도가 단순 "model loading 부정" 보다 정확히 "*특정 시점 변환* GGUF (`30e51a7c`) vs *특정 시점* llama.cpp (`c0c7e147`) 시간 의존 호환성 그라데이션". brief v1.1 §4 framing 임시성 명문 + §4.5 시간축 5번째 축 신규 + §2.5 비교 자격 1/4 명문.
docs/sessions/SESSION_2026-05-24.md:115:- 🔴 **R-9**: ADR-011 amendment 옵션화 자체가 헌법급 본문 권위에 *간접 압력*. ADR-011 = 헌법급 ADR (§2.3 Hermes ≠ root of trust + R-4~R-7 모법). 본 cycle 합의 자격 X (헌법급 변경 = 사용자 명시 + 풀 3+1 + Reviewer 권한 한계 답습 별도 cycle 의무).
docs/sessions/SESSION_2026-05-24.md:117:- **권고 17 (R-14~R-30)**: ADR-011 §2.1 (a)~(d) 4조건 + (e) 후속 패턴 정합화 / 헌법 5조 "내부 신뢰" 부분 인용 추가 / ADR-011 line 245 verbatim / R4 verbatim 보존 / P3-F1 3-source cross-validation 명문 / 진단 의무 enum 5 항목 / 메모리 19일 stale / Reviewer 권한 한계 (ADR-011 §6 정정 자격 0 + Provider Liquidity 본질 약화 자격 0 + MVP-1 합의 본문 정정 자격 0) / Phase 3 BLOCKING 7 답습 의무 / raw line-level cross-check / 성능 수준 "미검증" 보강 / 본질 회피 framing 차단 / format 가족별 분류 / ADR-008 부록 B Amendment 패턴 답습 자격 / layered 모델 진화 자격 / de facto 압력 차단 / 자동 기각 차단.
docs/sessions/SESSION_2026-05-24.md:118:- **NOTE 12 (N-1~N-12)**: SSM 명명법 정정 부분 적용 / runtime 별 implementation 차이 어법 약점 / P3-F1 일반화 자격 3 차원 한정 / ADR-011 §2.1 (e) 모법 인용 자격 / 메모리 19일 stale 명문 / 옵션 (K) R4 범위 확장 자격 / LiteLLM 인터페이스 한정 / ADR-008 부록 B Amendment 패턴 / 라이센스 차원 / 비용 차원 / 한국어 모델 호환성 / 외부 표준화 동향 (GGUF v3·MLA·LiteLLM·MCP) + supply chain opacity.
docs/sessions/SESSION_2026-05-24.md:119:- **Reviewer 정직성**: brief v1 본문 + 3 에이전트 보고서 + 선행 답습 8 문서 + Phase 3 raw 17 파일 + 헌법·ADR-011·메모리 cross-check. 결정 *고정* 0건 / 자동 정정 0건 / Provider Liquidity 본질 약화 자격 0 (binary 본질 유지, spectrum 화는 framing 도구 한정).
docs/sessions/SESSION_2026-05-24.md:125:- 🔴 **R-S2 ⭐⭐ Reviewer 격상 (B-B1 + B-S1 격상)**: 헌법 5조 line 40~46 verbatim = "**제5조: 코드 품질 원칙**" + 5 항목 (읽기 쉬움 / SRP / 중복 제거 / 외부 입력 검증 / 린터). "Provider Liquidity" **직접 본문 부재**. ADR-011 line 6 verbatim "**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)" + line 245 verbatim "제5조 **관용** (Provider Liquidity, 비협상)" 가 헌법 line 40~46 (코드 품질 원칙) 을 "관용" 으로 *해석* 하는 **ADR-011 *내부* 매핑** 자격. 본 finding = format 합의 R-S2 (ADR-011 *내부* line 6/212/245 비대칭) 의 **상위 단계 비대칭** — 헌법 5조 본문 ↔ ADR-011 line 6/245 매핑 *자체* 의 *내부 비대칭*. Reviewer 권한 한계 (헌법 본문 정정 자격 0) 답습 — 매핑 자격 인정 only, 매핑 자체 변경 자격 0 + 별도 cycle (g1-N) 헌법 5조 본문 미세 보강 의무 명문화 (R-2 = §7.1 (g1-N)/(g1-O) 신규 옵션 추가).
docs/sessions/SESSION_2026-05-24.md:128:- 🔴 **R-2 (A-B2 + C-B2 2-way 부분 일치)**: §7 후속 옵션 매트릭스 비대칭 — (1) 진입 자격 형식 통일 부족 ((a) "별도 brief + 풀 3+1" / (b) "별도 cycle" / (c) "별도 합의 cycle" / (d) "별도 brief" 4 형태 비균질) + (2) 옵션 방향성 비대칭 — (g1-N) 헌법 5조 본문 미세 보강 + (g1-O) ADR-011 line 212 본문 미세 보강 *권위 본문 미세 보강 중간 옵션 누락*. brief v1.1 §7.1 표 머리에 4 *방향성* 평가 + 진입 자격 단일 형태 통일 + (g1-N)/(g1-O) 2 행 신규 추가.
docs/sessions/SESSION_2026-05-24.md:131:- **Reviewer 정직성**: brief v1 본문 397줄 + 3 Agent 출력 (Agent A BLOCKING 4 + Agent B BLOCKING 8 + Agent C BLOCKING 3) + Reviewer raw line-level direct cross-check (메모리 line 1~19 verbatim / 헌법 line 35~89 verbatim / format 합의 brief v1.1 §10 line 635~671 verbatim / format 합의 보고서 NOTE 수 grep 24). **7 권한 한계 영구 답습** — ADR-011·Provider Liquidity·MVP-1·헌법·메모리 본문 정정 자격 0 + 4 가족 + 6축 framing 영구 정착 자격 0 + 자동 다음 단계 진입 자격 0. **R-S1 정정 = brief 본문 인용 line offset 정정 only, 메모리 본문 자체 변경 0건. R-S2 = 매핑 자격 인정 only, 헌법 본문 정정 자격 0. R-S3 = NOTE 합산 정정 only**.
docs/sessions/SESSION_2026-05-24.md:137:- 🔴 **R-S2 ⭐⭐ Reviewer 격상 (B-B1 + B-S2 통합)**: ADR-011 line 245 verbatim "제5조 **관용** (Provider Liquidity, 비협상)" + ADR-011 §6 line 212 verbatim "Provider Liquidity 영향 | **무관**" — **"관용"** = ADR-011 §6 line 212 "무관" 동의어 = ADR-011 *자체* 의 Provider Liquidity 본질 stance ("본 ADR 이 Provider Liquidity 본질에 *관용적/무관* 입장") 단어. 헌법 5조-2 *본문 단어* 로 "관용" 직접 채택 시 Provider Liquidity *비협상* 본질 (메모리 line 7 + line 9 verbatim "**시스템 설계의 비협상 원칙**") 과 **의미 충돌**. brief §4.3 후보 (iii) verbatim "## 제5조-2: Provider Liquidity 원칙 (**관용**, **비협상**)" = **제목 동시 명문 = 의미 자체 충돌**. 후보 (iii) = **위험한 후보** 분류, Provider Liquidity 본질 약화 risk 강함 (R-4 답습 영구 위반 risk).
docs/sessions/SESSION_2026-05-24.md:138:- 🔴 **R-S3 ⭐⭐ Reviewer 격상 (B-B3 + B-S1 + A-B2 + B-B4 통합)**: (1) 헌법 line 67~73 verbatim "## 제8-2조: 환경 관리 원칙" — **헌법 본문에 *이미* "X조-#" (제8-2조) 패턴 선례 존재** → 본 cycle 5조-2 신설 = "조-숫자" 패턴 후속 답습 = ADR-011 §2.1 (e) "후속 패턴" 답습 **강한 evidence** (brief §3.3 (e) "강함" 의 직접 evidence). (2) ADR-008 부록 B line 153~228 verbatim — **부록 B = ADR-008 본문 §6 차단조건 #1 충족 *수단*** 의 amendment, ADR-011 권위화 → ADR-008 본문 갱신 = **ADR ↔ ADR amendment 패턴 모법** (A-B2 정확). brief §1.4 (5) + §3.4 framing "헌법급 ADR 의 후속 amendment 패턴 모법" + "헌법 ↔ 헌법 amendment 패턴 모법" 자격 framing **부정확** — 정확한 framing = "ADR ↔ ADR amendment 패턴 모법 (by-reference 패턴 유사성), 헌법 ↔ 헌법 amendment 모법 ≠". 본 cycle 답습 자격 3 패턴: line 155 "단축 합의 — Reviewer-only" / line 224 "자동 승격 아님" / line 228 "별도 결정".
docs/sessions/SESSION_2026-05-24.md:143:- 🔴 **R-8 (A-S1 + C-B3 통합, 2-way)**: 본문 후보 4 → 7 확장 — (v) ADR-011 line 6 verbatim 답습 / (vi) 1 줄 ((g1-A) brief v1.1 §7.1 (g1-N) 기본 범위 답습) / (vii) 메모리 line 12~17 7 항목 verbatim 답습. brief v1.1 §4 신규 행 추가.
docs/sessions/SESSION_2026-05-24.md:148:- **Reviewer 정직성**: brief v1 본문 542줄 + 3 Agent 출력 (Agent A BLOCKING 4 + Agent B BLOCKING 14 + Agent C BLOCKING 5) + Reviewer raw line-level direct cross-check (헌법 line 1~98 verbatim / ADR-011 line 6 + line 212 + line 245 / **ADR-008 부록 B line 153~228 verbatim 직접 확인** / 메모리 line 1~19 verbatim / 본 cycle entry brief 약 30 line offset). **8 권한 한계 영구 답습** — ADR-011·Provider Liquidity·MVP-1·헌법·메모리 본문 정정 자격 0 + 4 가족 + 6축 framing 영구 정착 자격 0 + 자동 다음 단계 진입 자격 0 + **결합 cycle 진입 자격 평가 자격 0 (R-7 답습 (8) 신규)**. **R-S1~R-S5 모두 본 brief 본문 인용·line offset·verbatim 답습 정정 자격 only, 실 헌법·ADR-008·메모리 본문 변경 자격 0**.
docs/sessions/SESSION_2026-05-24.md:166:- **(g1-N-3')** ⭐⭐ (R-S2 carry-over 영구) **헌법 line 80 임시 stale 정정 cycle** — (g1-N-2) commit `3bdb1be` 후 ADR-011 line 6 변경 결과 ↔ 헌법 line 80 "ADR-011 line 6 ... 헌법 제5조 (Provider Liquidity)" 인용 verbatim 미정합 = 임시 stale 신규 발효. 정정 의무 = "헌법 제5조-2 (Provider Liquidity, 비협상)" reference. **헌법 본문 변경 cycle = R-9 답습 영구 의무 + Reviewer 권한 한계 (4) 예외 자격 발효 (R-13 (4-c) 동형)**
docs/sessions/SESSION_2026-05-24.md:167:- **(g1-N-3)** CLAUDE.md §1 SDD + **§7 의존 표 + §8 참조 표** + roadmap.md 답습 추가 (R-15 답습 — 3 영역 모두). ADR-011 §2.1 (e) 후속 패턴 답습 강한 후보
docs/sessions/SESSION_2026-05-24.md:168:- **(g1-O)** ADR-011 line 212 본문 미세 보강 (가족 차원 적용 boundary, R-S2 답습). (g1-N-2) 와 분리 진입 자격
docs/sessions/SESSION_2026-05-24.md:179:- **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit** ((g1-N-2) `3bdb1be`) — line 6 + line 245 매핑 정정
docs/sessions/SESSION_2026-05-24.md:181:- **Reviewer 권한 한계 8 항목 + (4) 헌법 본문 + (1) ADR-011 §6 예외 자격 발효 시점 (R-13 (4-c) 동형 패턴 적용) chain carry-over 영구**
docs/sessions/SESSION_2026-05-24.md:189:- **(g1-N-2)** ⭐ ADR-011 line 6 + line 245 매핑 "헌법 제5조 (Provider Liquidity)" → "헌법 제5조-2 (Provider Liquidity, 비협상)" 정정 = (g1-O) cycle 자동 trigger. 사용자 명시 + 별도 cycle (g1-O) (R-9 답습)
docs/sessions/SESSION_2026-05-24.md:190:- **(g1-N-3)** CLAUDE.md §1 SDD 답습 의무에 "5조-2 답습" + roadmap.md 답습 추가 (ADR-011 §2.1 (e) 후속 패턴 답습). 사용자 명시 + 별도 cycle
docs/sessions/SESSION_2026-05-24.md:197:- **(g1-O)** ⭐ ADR-011 line 212 본문 미세 보강 (가족 차원 적용 boundary 1 줄 명문 추가, R-S2 답습) — **(g1-N) 채택 후 (g1-N-2) 와 분리 가능**. 사용자 명시 + 별도 brief + 풀 3+1 (R-9 헌법급 변경)
docs/sessions/SESSION_2026-05-24.md:203:- **N-44 carry-over**: ADR-011 line 245 "관용" 단어 ↔ 헌법 본문 "비협상" 본질 정합성 평가 별도 cycle (R-25 + R-S2 통합)
docs/sessions/SESSION_2026-05-24.md:212:- **(g1-O)** ⭐ 본 cycle 결과 → **ADR-011 line 212 본문 미세 보강** (가족 차원 적용 boundary 1 줄 명문 추가, R-S2 답습) — 사용자 명시 + 별도 brief + 풀 3+1 (R-9 헌법급 변경)
docs/sessions/SESSION_2026-05-24.md:225:- **N-28 carry-over**: 후속 cycle Reviewer-only 단축 합의 자격 평가 (memory `feedback_staged_consensus_workflow` 답습 트리거 enum 의무, ADR-011 line 3 모법 답습)
docs/sessions/SESSION_2026-05-24.md:245:- **(f-C)** 헌법 5조 + ADR-011 line 6/245 "관용 매핑" 권위 답습 명문 — R-13 reframing 답습
docs/sessions/SESSION_2026-05-24.md:248:- **(f-E)/(f-F)** ADR-011 amendment cycle — 헌법급 변경 (R-9 답습)
docs/sessions/SESSION_2026-05-24.md:302:### ⭐⭐⭐ 본 세션 (g1-N-2) ADR-011 line 6/245 매핑 정정 cycle (8차 entry, 3 commit + 통합 정리, **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit, Reviewer 권한 한계 (1) 예외 자격 발효 시점**)
docs/sessions/SESSION_2026-05-24.md:303:- ⭐⭐⭐ `docs/phase0/jarvis-mvp1-g1-n-2-adr-011-mapping-correction-consensus-entry-brief.md` (v1 신규 `8207f55`, 488줄 → v1.1 519줄 + **ADR-011 line 6/245 매핑 정정 동시 atomic commit** `3bdb1be`)
docs/sessions/SESSION_2026-05-24.md:305:- ⭐⭐⭐ `docs/decisions/ADR-011-means-vs-ends-redaction.md` (line 6 "헌법 제5조 (Provider Liquidity)" → "헌법 제5조-2 (Provider Liquidity, 비협상)" + line 245 "제5조 관용" → "제5조-2 관용", **본 commit 변경 결과**, `3bdb1be` atomic 동시)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:30:8. ❌ **헌법 / ADR-011 / 다른 ADR / 다른 문서 본문 변경** (R-9 답습 영구)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:156:### 3.3 Boss = root of trust 아님 (ADR-011 §2.1 + MVP-1 brief v2 §5 답습)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:261:### 5.3 추가 backend 후보 (LOW carry-over, NOTE-6)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:415:| R-9 답습 영구 (헌법/ADR/다른 문서 본문 변경 0건) | ✓ 본 doc 자체 = 신규 architecture doc, 헌법 5조-2 + ADR-011 §2.1 (a)~(e) 본문 변경 0건 |
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:424:| ADR-011 §2.1 5조건 (a)~(e) 답습 정합 | ✓ §3.3 Boss = root of trust 아님 + §1.2 본 doc scope 외 명문 |
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:9:**상위 권위**: ADR-011 §2.1 (a)~(e), ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), 외부 LLM GPT-5.5 Thinking 응답 §6 (3-layer PASS 분리)
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:14:- `docs/architecture/implementation-runtime-roadmap.md` §6 (PASS 기준 통합 매트릭스 + ADR-011 §2.1 5조건)
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:26:5. ADR-011 §2.1 (a)~(e) 5조건 = 모든 MVP 단계 의무 답습 명시
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:87:각 GP 별 Implementation Evidence PASS = **ADR-011 §2.1 (a)~(e) 5 조건 답습 모두 충족 의무**:
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:93:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + `roadmap-mvp1.md` §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + `roadmap-mvp1.md` §4 (36번째 entry R-S1 정정 답습) |
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:165:| 2 | G3 §5.5.3 트리거 5건 자동 검출 hook 구현 완료 | C-9 답습 (`roadmap-mvp1.md` 외 영역) |
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:170:### 5.3 deepening 미진행 영역 명시
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:222:| 5 | **외부 LLM 1+ blind 의뢰 PASS** (T-6 / T-10 / T-13 발화 시) | C-7 답습 + ADR-011 §2.1 (e) 답습 |
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:235:- PMO 격상 후 Hermes ≠ root of trust 답습 영구 보존 (ADR-011 §2.1 (d) 답습)
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:267:## 9. ADR-011 §2.1 (a)~(e) 5 조건 = 모든 MVP 단계 의무 답습
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:287:- ADR-011 §2.1 (a)~(e) 5 조건 = 모든 MVP 단계 의무 답습
docs/sessions/SESSION_2026-05-20.md:77:- C-A5-11 ~ C-A5-15: 외부 LLM line 242 vs C-7 line 378 = C-7 답습 영구 / 3-layer ↔ 6 MVP 매핑 영구 / ADR-011 §2.1 모든 MVP 의무 / 본 brief 후속 합의 자동 진입 금지 / Phase α defer lockdown 영향 0건
docs/sessions/SESSION_2026-05-20.md:283:- 그러나 명칭이 *수단(credential isolation)* 을 박음 → **ADR-011 §2.1 means/ends 저촉** (목적 = "Hermes가 T3 변경 권위 주체 불가", credential isolation = 수단의 하나)
docs/sessions/SESSION_2026-05-20.md:362:1차 4줄 (448/784/457/648) + 가정 잔존 교정 2줄 (360/1122) + 정합 참조만 2줄 (230/805). **형태 권고**: brief §5.3 "본문 반영 한정 합의 + 4 결정 항목(문구·범위·author 어휘·채널명) scope 명문 고정" (식별 frame 은 Group I `f6c6d5a` 만장일치 확정 → 풀 3+1 frame 재투표 중복 제거).
docs/sessions/SESSION_2026-05-27.md:28:| **Layer 2 brief v1 작성** ⭐ | scope (Layer 1 PatternReport → Proposal) + safety class (게이트 신설 = 풀 3+1 필수, Layer 1 답습 line 4 직접) + 안전 등급 표 + 제안 5종 (WORKER_RELIABILITY_LOW / FLAG_FREQUENCY_RISING / ADVICE_ENDPOINT_DEGRADED / RECENT_FAILURE_CLUSTER / INPUT_DROUGHT) + threshold 후보 (N/θ/K/오래됨, 값 고정 0, ADR-011 §2.1) + API 설계 (frozen + tuple, severity 매트릭스, source_report_signature) + fail-soft + 발효 정책 (DEFER, 재진입 = MVP-1 후 실 trigger) + 3+1 합의 기준 + carry-over + 의존 참조 | `docs/phase0/jarvis-layer2-proposal-generation-brief.md` (v1) |
docs/sessions/SESSION_2026-05-27.md:53:테스트 0건 변경, `src/jarvis/` 0건 변경, `src/jarvis/layer1.py` 0건 변경 (Layer 0/1 read-only 답습), 헌법 0건, ADR-011 0건, MVP-1 합의 0건, threshold 고정 0건, severity 임계 고정 0건, Layer 3 신설 0건, MVP-1 진입 0건. **본 cycle = 설계만, 코드 0, 발효 DEFER**.
docs/sessions/SESSION_2026-05-27.md:66:- (a) Reviewer-only 단축 합의: 5/5 풀 3+1 승격 trigger 0건 발화 검증 + 후속 3 합의 본문 흡수 cross-check + ADR-011 §2.1 (a)~(e) 답습 정확
docs/sessions/SESSION_2026-05-27.md:78:| audit brief 작성 | `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (진입 합의 / 실 구현 / DRAFT 잔재 / deferred / ADR-011 5/5 매트릭스 / 4 진입점 권고 / 합의 형태 추천) | (본 commit) |
docs/sessions/SESSION_2026-05-27.md:80:| ⭐ Reviewer-only 단축 합의 | 5/5 풀 3+1 승격 trigger 0건 발화 검증 + 후속 3 합의 본문 흡수 cross-check (gp3 line 821 / gp5 line 820 / backlog#6 line 819) + ADR-011 답습 정확 → APPROVE 단축 합의 | `docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md` |
docs/sessions/SESSION_2026-05-27.md:96:**(c) MVP-1 Implementation Evidence PASS 발효 합의** — (a)+(b) 선행 후, ADR-011 §2.1 (a)~(e) 5/5 + conditions 해소 + 사용자 명시 결정
docs/sessions/SESSION_2026-05-27.md:124:⭐⭐⭐ **MVP-1 1.5차 보강 진입 합의 entry cycle 발효**. 본 cycle = MVP-1 GP-3 + GP-5 1.5차 보강 4 sub-수단 (S-3 detect-secrets 부분 통합 + ST-2 inotify sidecar + PC-1-T3 mandatory enforcement + AR-3 통합 PR auto-reject) **진입 합의 entry brief** 발효. 4 sub-수단 *채택 결정 발효 자격* + 실 구현 sub-cycle 4개 진입 권한 발효 자격 충실. 본 cycle 합의 발효 시점 = brief v1.1 commit + 합의 보고서 commit + 본 정리 commit.
docs/sessions/SESSION_2026-05-27.md:126:- brief v1 작성 (`docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`, 506줄, scope/답습/DONE/4 sub-수단 진입 자격/선차 변경 매트릭스/ADR-011 매트릭스/합의 형태/Rollback Trigger 12/Evidence 5/금지 사항/외부 LLM 자격 검증 7/다음 단계/자기진단)
docs/sessions/SESSION_2026-05-27.md:167:**(c) MVP-1 Implementation Evidence PASS 발효 합의** — (b1) 4 sub-cycle 완료 + ADR-011 §2.1 (a)~(d) + (e) 5/5 + conditions 해소 + 사용자 명시 별도 합의 영역
docs/sessions/SESSION_2026-05-27.md:242:## 26번째 entry — MVP-1 PC-1-T3 mandatory enforcement 실 구현 sub-cycle (b1 첫 sub-cycle, Reviewer-only 단축 합의)
docs/sessions/SESSION_2026-05-27.md:244:> **흐름**: 25번째 entry chore 종결 (db688b6 push) → 사용자 "PC-1 진입" → PC-1 현 상태 audit (`.pre-commit-config.yaml` T2 opt-in 발효 + `.githooks/` Layer 3 발효 + CONTRIBUTING/bin/Makefile 부재 + `pre-commit` 패키지 미설치 + audit log 0 + bypass detection 0) → PC-1 sub-cycle brief 작성 (288줄, 24번째 entry BLOCKING R-2/R-6/R-7(b) + N-1/N-2 흡수, D-1~D-6 사용자 결정 항목 명시) → 사용자 D-1~D-4 결정 (권고 4/4 채택) + D-5/D-6 default 권고 답습 (병렬 유지 + CI 통합 별도 sub-cycle) → Reviewer-only 단축 합의 보고서 작성 (5/5 풀 3+1 승격 trigger 0건 발화 + entry 합의 verbatim cross-check 7 source) → 실 구현 5 file (README 보강 + CONTRIBUTING.md 신규 + bin/setup.sh 신규 + requirements-dev.txt pre-commit==4.0.1 추가 + tools/pre_commit_install_audit.sh 신규) → SESSION + INDEX + 본 정리 commit.
docs/sessions/SESSION_2026-05-27.md:248:⭐⭐⭐ **MVP-1 PC-1-T3 mandatory enforcement 실 구현 sub-cycle 발효 — (b1) 4 sub-cycle 중 첫 진입 + 완료**. 본 cycle = T3 채택 결정 *집행* (T3 결정 자체는 24번째 entry cycle 에서 APPROVE WITH CONDITIONS 완료). PC-1 (dev 환경 hook) **1차 방어 발효** — 2차 (PC-3 CI) + 3차 (AR-3 branch protection) = 별도 영역 답습 (Defense in depth N-1 답습).
docs/sessions/SESSION_2026-05-27.md:250:- PC-1 sub-cycle brief 작성 (`docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md`, 288줄) — 24번째 entry BLOCKING R-2 (PC-1 (b)(d) 재분류) + R-6 (PC1-1 탐지 경로 (i)(ii)(iii)) + R-7(b) (PC1-2 차등) + N-1 (PC-1 단독 우회 가능, 결합 효과 명문) + N-2 (T3 명칭 일관) 흡수 매트릭스 + 현 상태 audit + 실 구현 5 항목 + ADR-011 (a)~(e) 5/5 매트릭스 + Rollback Trigger + Evidence + D-1~D-6 사용자 결정 + 합의 형태 권고 + 8/8 자기진단
docs/sessions/SESSION_2026-05-27.md:252:- Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md`) — APPROVE. 5/5 풀 3+1 승격 trigger 발화 0건 검증 + entry 합의 verbatim cross-check 7 source (line 292 / §1 line 38 / §6 R-2 line 66 / §6 R-6 line 88 / §6 R-7(b) line 94 / §10 N-1 line 106 / §10 N-2 line 107) + 변경 0건 의무 10/10 cross-check + ADR-011 (a)(c)(e) 3/5 본 합의 발효 + (b)(d) 2/5 실 구현 단계 발효 + 8/8 자기진단
docs/sessions/SESSION_2026-05-27.md:255:  - `CONTRIBUTING.md` 신규 (134줄, 6장: onboarding workflow + PC-1-T3 명문 + PR workflow + 합의 cycle 답습 + TDD 답습 + 참조 문서)
docs/sessions/SESSION_2026-05-27.md:276:**(b1-PC1 후속 — PoC evidence 단계)**: ADR-011 (b)(d) 충족 = 실 evidence 수집 의무
docs/sessions/SESSION_2026-05-27.md:298:| `CONTRIBUTING.md` | 신규 (134줄, 6장: onboarding + PC-1-T3 명문 + PR workflow + 합의 cycle + TDD + 참조 문서) |
docs/sessions/SESSION_2026-05-27.md:300:| `requirements-dev.txt` | `pre-commit==4.0.1` 추가 (PC-1-T3 PoC 자격 충족) |
docs/sessions/SESSION_2026-05-27.md:307:`.pre-commit-config.yaml` 본문 0건 (T2 opt-in 답습 유지 — `repos: local` 6 hook 정의 모두 변경 0건), `.githooks/pre-commit` 본문 0건 (Layer 3 답습), `.githooks/setup.sh` 본문 0건, `src/` 0건, `tools/` 기존 21 도구 본문 0건 (`pre_commit_install_audit.sh` 신규 = bypass detection 메커니즘 발효, 신규 추가 ≠ 본문 변경), `.github/workflows/` 0건 (D-6 별도 sub-cycle), `.importlinter` 0건, branch protection rule 0건 (AR-3 영역), ADR 0건, 헌법 0건, roadmap 본문 0건, governance-preconditions 0건, 후속 backlog1/2 합의 본문 0건, 24번째 entry 합의 본문 0건, MVP-1 Implementation Evidence PASS 0건 ((c) carry-over 영역), Hermes PMO 0건, 수단 결정 본 cycle = entry 결정 *집행* (T3 채택 결정 자체 = 24번째 entry cycle 발효), threshold 0건 고정, Tier-2/3 catalog 0건 확장, adapters/llm/facade.py 0건 ((d) carry-over 영역), 풀 3+1 합의 0건 발효 (Reviewer-only 단축 합의 답습). **본 cycle = PC-1-T3 1차 방어 실 구현 + brief + 합의 한정**.
docs/sessions/SESSION_2026-05-27.md:313:> **흐름**: 26번째 entry PC-1-T3 종결 (3a63a5b push) → 사용자 "b1-S3 진입" → S-3 현 상태 audit (`detect-secrets` 0 패키지, secret-hygiene-egress-redaction.yml 694줄 24 step 발효 + detect-secrets 언급 line 692 = "0건 명시" 한정, `tools/secret_scanner.py` S-1 발효 유지) → S-3 sub-cycle brief 작성 (303줄, 24번째 entry R-4 BLOCKING + R-MVP1-1.5-S3-1/2/3 Rollback Trigger + Tier-1 답습 plugin 5종 hardcoded list 본문 채택) → 사용자 D-1~D-4 결정 (권고 4/4 채택) + D-5 default 권고 답습 → Reviewer-only 단축 합의 보고서 작성 (5/5 풀 3+1 승격 trigger 0건 + entry 합의 verbatim cross-check 5 source) → 실 구현 5 file (`requirements-dev.txt` detect-secrets==1.5.0 추가 + `tests/fixtures/secret_hygiene/mvp1_s3/` 6 testfile 신규 + workflow `on.push.paths` 2 entry 추가 + workflow S-3 install/scan/baseline-assertion 3 step 신규) → SESSION + INDEX + 본 정리 commit.
docs/sessions/SESSION_2026-05-27.md:319:- S-3 sub-cycle brief 작성 (`docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md`, 303줄) — 24번째 entry R-4 BLOCKING (plugin identifier 5종 정확 mapping + `--baseline` 미사용 CI assertion) 흡수 매트릭스 + 현 상태 audit + 실 구현 5 항목 + ADR-011 (a)~(e) 5/5 매트릭스 + Rollback Trigger 3 본 sub-cycle 적용 + Evidence + D-1~D-5 사용자 결정 + 합의 형태 권고 + 자기진단 8/8
docs/sessions/SESSION_2026-05-27.md:321:- Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md`) — APPROVE. 5/5 풀 3+1 승격 trigger 발화 0건 검증 + entry 합의 verbatim cross-check 5 source (line 290 / §1 line 36 / §6 R-4 line 73 / §5.1 line 323~325 / roadmap §3.6.3 line 289) + 변경 0건 의무 12/12 cross-check + ADR-011 (a)(c)(e) 3/5 본 합의 발효 + (b)(d) 2/5 실 구현 단계 발효 + 자기진단 8/8
docs/sessions/SESSION_2026-05-27.md:335:| 26번째 entry PC-1-T3 종결 + push (3a63a5b) + 사용자 "b1-S3 진입" | (대화) | — |
docs/sessions/SESSION_2026-05-27.md:346:**(b1-S3 후속 — PoC evidence 단계)**: ADR-011 (b)(d) 충족 = 실 actual run evidence 수집 의무
docs/sessions/SESSION_2026-05-27.md:390:- ST-2 sub-cycle brief 작성 (`docs/phase0/mvp1-st2-inotify-sidecar-brief.md`, 227줄, 10장) — 23번째 entry audit 한정 패턴 답습 + 인프라 8/8 발효 cross-check + R-5 BLOCKING 3 단계 evidence 현 발효 cross-check 명문 (1) event 인지 = watch-secrets.sh inotifywait 6 event / (2) sidecar→메인 signal = status file + hermes-mock healthcheck / (3) 메인 fail-closed = docker inspect Health.Status 비교 / R-7(a) framing 정정 entry brief v1.1 line 326 이미 흡수 답습 (본 sub-cycle 추가 정정 0건) + R-MVP1-1.5-ST2-{1,2,3} Rollback Trigger 답습 유지 + ADR-011 (a)~(e) 매트릭스 ((b)(c) 이미 발효 + (a)(e) 합의 시점 + (d) nightly schedule 추가 시) + D-1~D-3 사용자 결정 + 합의 형태 권고 + 자기진단 8/8
docs/sessions/SESSION_2026-05-27.md:392:- Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-27-mvp1-st2-inotify-sidecar.md`, 7장) — APPROVE. 5/5 풀 3+1 승격 trigger 발화 0건 + entry 합의 verbatim cross-check 5 source (line 290 / §1 line 36 / §6 R-5 / §13.2 line 534 / entry brief v1.1 line 326) + 인프라 8/8 발효 cross-check (23번째 entry audit 한정 패턴 답습) + R-5 BLOCKING 3 단계 evidence 발효 source 명문 본문 채택 + 변경 0건 의무 14/14 + ADR-011 (a)(b)(c)(e) 4/5 본 합의 발효 + (d) 1/5 실 구현 단계 발효 + 자기진단 8/8
docs/sessions/SESSION_2026-05-27.md:412:**(b1-ST2 후속 — PoC evidence 단계)**: ADR-011 (d) 충족 = nightly actual run id evidence 수집 의무
docs/sessions/SESSION_2026-05-27.md:457:- evidence 파일 신규 (`docs/phase0/mvp1-ar3-branch-protection-applied-evidence.md`, 5장) — 적용 시점 + 권한 + R-MVP1-1.5-AR3-2a catalog 정정 매트릭스 (11 후보 → 8 unique) + 적용 응답 body + ADR-011 충족 상태 (3/5 본 적용 + 2/5 부분 충족 첫 PR 발화 시) + develop carry-over + 다음 단계 4
docs/sessions/SESSION_2026-05-27.md:459:- ADR-011 (a)~(e) 충족 상태 갱신 — **(a)(c)(e) 3/5 완전 충족** + **(b)(d) 부분 충족** (적용 evidence 발효, 첫 PR run evidence 추가 의무)
docs/sessions/SESSION_2026-05-27.md:473:| evidence file 작성 ⭐ | `docs/phase0/mvp1-ar3-branch-protection-applied-evidence.md` (5장, 적용 evidence + catalog 정정 매트릭스 + ADR-011 충족 갱신) | (본 정리 commit) |
docs/sessions/SESSION_2026-05-27.md:480:- 첫 PR open (feature/jarvis-mvp0 → main) 시 11 workflow 모두 status check 발화 + 모든 PASS 의무 + admin bypass 0 시도 evidence (ADR-011 (b)(d) 완전 충족)
docs/sessions/SESSION_2026-05-27.md:499:| `docs/phase0/mvp1-ar3-branch-protection-applied-evidence.md` | 신규 (5장, 적용 evidence + R-MVP1-1.5-AR3-2a catalog 정정 매트릭스 + ADR-011 충족 갱신 + develop carry-over + 다음 단계 4) |
docs/sessions/SESSION_2026-05-27.md:517:⭐⭐⭐ **(b1-AR3 첫 PR evidence) 수집 완료 — ADR-011 (a)~(e) 5/5 완전 충족 (AR-3 영역 한정)**. PR #2 draft (`7c294bb..73ed20d`) 의 11 check_runs 모두 SUCCESS + mergeable CLEAN. **중복 동작 검증 핵심 결과**: `enforce` x3 + `scan` x3 모두 분리 처리 + 모든 동명 PASS 의무 답습 = **race condition 0 확정** (GitHub branch protection = 모든 동명 check 의 PASS 의무, 안전 처리). **paths-aware risk 발견 및 조치**: r2-canary.yml `on.pull_request.paths` 매치 0 PR 에서 미발화 = required check "Expected" 영원 대기 → merge 차단 risk → contexts 에서 제거 (가장 단순 + 비례성, 다른 paths-aware workflow audit carry-over). **(c) MVP-1 Implementation Evidence PASS 발효 합의 진입 자격 자격** = (b1) 4 sub-cycle 완료 + 본 evidence.
docs/sessions/SESSION_2026-05-27.md:529:- evidence file 신규 (`docs/phase0/mvp1-ar3-first-pr-evidence.md`, 6장): 시점/PR + 첫 발화 결과 (1 FAIL + 1 미발화) + 조치 (fixture 정정 + contexts 갱신) + 재발화 (11/11 SUCCESS) + R-MVP1-1.5-AR3 검증 매트릭스 (중복 동작 + admin bypass 0 + paths-aware 발견) + ADR-011 5/5 완전 충족 + carry-over 6
docs/sessions/SESSION_2026-05-27.md:548:| evidence file 작성 ⭐ | `docs/phase0/mvp1-ar3-first-pr-evidence.md` (6장, ADR-011 5/5 완전 충족 매트릭스 + 중복 동작 race 0 확정 + paths-aware risk 발견 + carry-over 6) | (본 정리 commit) |
docs/sessions/SESSION_2026-05-27.md:571:| `docs/phase0/mvp1-ar3-first-pr-evidence.md` | 신규 (6장, ADR-011 5/5 완전 충족 매트릭스 + 중복 동작 race 0 + paths-aware risk + carry-over 6) |
docs/sessions/SESSION_2026-05-27.md:580:11 workflow 본문 0 (R-4.1 paths 필터 widen 0건, contexts 제거 답습), `.pre-commit-config.yaml` 0, `.githooks/` 0, `src/` 0, `tools/` 본문 0, `docker/` 0, ADR 0, 헌법 0, roadmap 본문 0, governance-preconditions 0, 후속 합의 본문 0, 24번째 entry 합의 본문 0, MVP-1 Implementation Evidence PASS 0 ((c) carry-over 영역, **AR-3 영역 (a)~(e) 5/5 완전 충족 발효 = (c) 진입 자격 자격 자격**), Hermes PMO 0, 수단 결정 본 cycle = 30번째 entry 결정 *집행* (catalog v2 = 7 unique 정정, R-4.1 제거), threshold 0 고정, Tier-2/3 catalog 확장 0, adapters/llm/facade.py 0 ((d) carry-over 영역), 풀 3+1 합의 0 (사용자 명시 + 직접 실행 + evidence 수집 답습), develop branch 신규 생성 0 (carry-over 답습), workflow job name unique 화 0 (중복 동작 race 0 확정 = 본 evidence verify), MVP-1 영역 외 다른 rule 0 (N-6 답습), Backlog #3 전체 진입 0 (N-3 답습), fix commit `73ed20d` 본문 = 1 file 8/-6 fixture 정확화 한정 (fixture 본문 변경 = 단순 fix, 영구 의무 R-MVP1-1.5-S3-3 영향 0건). **본 cycle = 첫 PR evidence 수집 + 중복 동작 race 0 검증 + paths-aware risk 발견 + ADR-011 (a)~(e) 5/5 완전 충족 (AR-3 영역) 한정** (외부 effect = PR #2 draft + branch protection contexts v2, git tree 변경 = evidence file 신규 + fix commit + SESSION/INDEX).
docs/sessions/SESSION_2026-05-27.md:592:- AR-3 sub-cycle brief 작성 (`docs/phase0/mvp1-ar3-pr-auto-reject-brief.md`, 281줄, 10장) — R-3 BLOCKING (check name mapping verify) 흡수 매트릭스 + 11 workflow 실 check name catalog 본문 채택 (§3.2, workflow name + job name 조합, `Evidence / PASS Gate` workflow name `/` 포함 verify 의무 명문) + R-7(c) 차등 분리 (R-MVP1-1.5-AR3-2a 도구 변경 = 단축 / 2b T3 정책 신규 check = 풀 3+1 + 외부 LLM 1+) + Claude scope vs 사용자 admin scope 명문 분리 (§1.1) + 사용자 admin 적용 절차 (A) web UI + (B) gh CLI 안내 (§4.2) + AR-1 + AR-2 통합 효과 명문 + PC-1 + PC-3 + AR-3 결합 Defense in depth (§4.4) + ADR-011 (a)~(e) 매트릭스 (3/5 합의 시점 + 2/5 사용자 admin 적용 시점) + D-1~D-4 사용자 결정 + 자기진단 8/8 + 7단계 cycle (6 + 사용자 admin 적용)
docs/sessions/SESSION_2026-05-27.md:594:- Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-27-mvp1-ar3-pr-auto-reject.md`, 7장) — APPROVE. 5/5 풀 3+1 승격 trigger 발화 0건 + entry 합의 verbatim cross-check 5 source (line 290 / line 113 / §2.4 line 229 / R-3 / R-7(c)) + 인프라 발효 cross-check (AR-1 부분 발효 + main/develop unprotected HTTP 404) + R-3 BLOCKING 11 catalog 본문 채택 (§3 표) + 변경 0건 의무 12/12 + ADR-011 (a)(c)(e) 3/5 본 합의 + (b)(d) 2/5 사용자 admin 적용 시점 + 자기진단 8/8
docs/sessions/SESSION_2026-05-27.md:613:**(b1-AR3 사용자 admin scope 실 적용 — 즉시 진입 가능)**: ADR-011 (b)(d) 충족 = 사용자 admin 적용 + 첫 PR evidence 의무
docs/sessions/SESSION_2026-05-27.md:623:| PC-1-T3 | `3a63a5b` | dev 환경 hook 의무화 + bin/setup.sh + CONTRIBUTING.md + audit log + bypass detection |
docs/sessions/SESSION_2026-05-27.md:628:**(c) MVP-1 Implementation Evidence PASS 발효 합의** — (b1) 4 sub-cycle 완료 = 진입 자격 자격 충족 → **다음 cycle 후보** (ADR-011 §2.1 (a)~(d)+(e) 5/5 + conditions 해소 + 사용자 명시 별도 합의)
docs/sessions/SESSION_2026-05-27.md:659:- entry brief 작성 (`docs/phase0/friday-separate-evolution-tool-entry-brief.md`, ~280줄, 13장) — §1 본 brief 자격 + §2 동기/Marvel narrative + §3 프라이데이 scope ((P) 자체 코드 vs (Q) Hermes 도입) + §4 격리 메커니즘 사전 정의 (5 layer: filesystem ACL + workdir + endpoint + 메모리 + commit) + §5 진입 시점 stage gate (자비스 MVP-1 완료 후) + §6 Rollback Trigger 5건 (R-Friday-1 ~ R-Friday-5) + §7 Evidence 의무 + §8 ADR-011 (a)~(e) 매트릭스 (2/5 본 brief 시점 충족 + 3/5 별도 cycle) + §9 사용자 결정 항목 D-1 ~ D-8 + §10 합의 형태 권고 (풀 3+1 + 외부 LLM 1+, 5/5 trigger 中 3/5 발화) + §11 carry-over + §12 자기진단 8/8 + §13 답습 영구 권위
docs/sessions/SESSION_2026-05-27.md:664:**원칙 준수**: 헌법 본문 변경 0 / ADR 본문 변경 0 / `src/jarvis/` + `tests/jarvis/` 본문 0 / `.github/workflows/` 0 / `.pre-commit-config.yaml` 0 / `.githooks/` 0 / branch protection rule 변경 0 / 자비스 4 invariant (헌법 8조 + ADR-011 §2.4 T3 + Boss = root of trust 아님 + Provider Liquidity 5조-2) 침범 0 / 본 cycle 자동 다음 단계 진입 0 (brief 발효 후 합의 cycle + D-1~D-8 결정 = 사용자 명시 의무) / ceremony-inflation 회피 (1-agent 직접 brief 작성, 본 brief 합의 = 별도 cycle 자비스 MVP-1 완료 후) — **10/10 유지**.
docs/sessions/SESSION_2026-05-27.md:716:`src/jarvis/` + `tests/jarvis/` 본문 0건, `tools/` 0건, `.github/workflows/` 0건, `.pre-commit-config.yaml` 0건, `.githooks/` 0건, `docker/` 0건, `bin/` 0건, `CONTRIBUTING.md` 0건, `README.md` 0건, ADR 본문 0건 (ADR-008 + ADR-011 + 다른 ADR 모두 보존), 헌법 본문 0건, roadmap 본문 0건, governance-preconditions 0건, 자비스 4 invariant 침범 0건 (헌법 8조 + ADR-011 §2.4 T3 + Boss = root of trust 아님 + Provider Liquidity 5조-2 모두 영구 보존), Hermes 자체 도입 0건 ((Q) 형태 = D-2 결정 영역), Layer 3 자비스 신설 0건 ((B) 경로 = 본 cycle 의도적 회피), threshold 고정 0건, Tier-2/3 catalog 확장 0건, branch protection rule 변경 0건, MVP-1 Implementation Evidence PASS 발효 0건 ((c) carry-over 영역), 풀 3+1 합의 0건 (본 cycle = 1-agent brief 작성 한정, 합의 = 별도 cycle 자비스 MVP-1 완료 후), 자비스 carry-over 진행 0건 (별도 cycle 영역), Layer 2 발효 결정 0건 (별도 cycle 영역), 프라이데이 MVP-0 설계 0건 (D-1 ~ D-8 결정 후 별도 cycle). **본 cycle = 프라이데이 방향 결정 + entry brief 작성 + 메모리 저장 한정**.
docs/sessions/SESSION_2026-05-27.md:728:본 entry 가 가지는 *유일성*: (1) 본 프로젝트 최초 메인 권위 PASS 발효 / (2) 본 세션 32번째 entry chain (22번째 Layer 2 → 31번째 첫 PR evidence) 의 **메인 권위 격상 정점** / (3) ADR-011 §2.1 (a)~(e) 5/5 완전 적용 (cross-cover 답습 + Defense in depth + multi-source 답습 모두 발효) / (4) (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2 + AR-3) 누적 + AR-3 사용자 admin scope 단계 7 적용 + 첫 PR evidence (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS 모두 발효 source.
docs/sessions/SESSION_2026-05-27.md:730:- brief 작성 (`docs/phase0/mvp1-implementation-evidence-pass-activation-brief.md`, v1 267줄 → v1.1 보강) — 24번째 entry carry-over (c) verbatim + (b1) 4 sub-cycle ADR-011 (a)~(e) 매트릭스 (17/20 완전 + 3/20 부분) + GP-3 5/5 + GP-5 5/5 매트릭스 + PASS 발효 형태 (α/α′/β/γ) + Rollback Trigger 10건 (v1 5건 + v1.1 5건 신규) + ADR-011 (a)~(e) 매트릭스 + D-1~D-5 사용자 결정 + 합의 형태 권고 + 자기진단 10/10
docs/sessions/SESSION_2026-05-27.md:745:  - R-3 정정 (§3.1 GP-3 (c) + §3.2 GP-5 (c)): multi-source 재기술 (ADR-008 차단조건 #1/#4/#6 + 부록 B + ADR-010 + ADR-011 + R-4 + roadmap §3/§4 + (b1) 4 sub-cycle)
docs/sessions/SESSION_2026-05-27.md:789:- PC-1-T3 PoC evidence: `bash bin/setup.sh` + `bash tools/pre_commit_install_audit.sh` + `pre-commit run --all-files` 실 실행
docs/sessions/SESSION_2026-05-27.md:812:11 workflow 본문 0 (AR-1 답습 유지), `.pre-commit-config.yaml` 0, `.githooks/` 0, `src/` 0, `tools/` 0, `docker/` 0, `bin/` 0, `CONTRIBUTING.md` 0, `README.md` 0, ADR 본문 0 (ADR-008 + ADR-011 + ADR-010 + ADR-009 + ADR-012 모두 0건, R-MVP1-PASS-2 영구 금지 답습), 헌법 본문 0 (5조-2 Provider Liquidity 비협상 답습 영구 유지), governance-preconditions 0, 후속 합의 본문 0, 24번째 entry 합의 본문 0, (b1) 4 sub-cycle 본문 0 (PC-1-T3 + S-3 + ST-2 + AR-3 brief + 합의 본문 모두 0건), branch protection rule 변경 0 (31번째 entry 발효 답습), MVP-2 자동 발효 0 (R-MVP1-PASS-5 영구 금지), Operational Readiness PASS 발효 0, Hermes PMO 격상 0, 4 게이트 일괄 PASS 0, adapters/llm/facade.py 0 ((d) carry-over), 수단 결정 변경 0 ((b1) 4 sub-cycle 결정 답습), threshold 0 고정, Tier-2/3 catalog 0 확장, (b2) R-S1 정정 적용 0 (별도 sub-cycle), paths-aware audit 적용 0 (별도 sub-cycle, R-6 답습), (b3) framing 정정 적용 0 (별도 sub-cycle). **변경 영역 = roadmap-mvp1.md §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 한정 + brief v1.1 보강 + 합의 보고서 신규 한정**. **본 cycle = MVP-1 Implementation Evidence PASS 완전 발효 + 합의 의사록 + brief v1.1 흡수 한정** (외부 effect 0건, git tree 변경 = 5 § 본문 + brief 보강 + 합의 보고서 신규).
docs/sessions/SESSION_2026-05-27.md:881:  - `docs/architecture/governance-preconditions.md` 6 위치: line 106 (P3 row) + 343 (GP-3 row) + 488 (docker secret) + 498 (OAuth credentials) + 508 ((c) cell) + 523 (cross-reference 추가) — 모두 `ADR-008 §A.2 R1-2 / §2.6.4 R1-2 / §2.6.2 R2-1` → `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011` multi-source 재기술
docs/sessions/SESSION_2026-05-27.md:887:**원칙 준수**: ADR-008 본문 변경 0건 (R-MVP1-PASS-2 영구 금지 답습) / ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0 / 헌법 0 (5조-2 답습) / 11 workflow 본문 0 (34번째 entry audit 답습) / branch protection rule 0 (31번째 entry 답습) / (b1) 4 sub-cycle 본문 0 / 33번째 entry PASS evidence 본문 0 / roadmap-mvp1 §2.2 / §3.5 / §4.5 / §4.7.3 / §5.1 / §9 본문 0 (§3.6.3 line 290 framing 한정) / src 0 / tools 0 / docker 0 / `.pre-commit-config.yaml` 0 / `.githooks/` 0 / MVP-2 자동 발효 0 / adapters/llm/facade.py 0 / 32번째 entry 프라이데이 brief 본문 0 / 풀 3+1 합의 0 (Reviewer-only 답습) — **17/17 유지**.
docs/sessions/SESSION_2026-05-27.md:932:ADR-008 본문 0 (R-MVP1-PASS-2 영구 금지 답습 — `§A.2` / `§2.6.4` / `§2.6.2` / "R1-2" / "R2-1" 라벨 본문 추가/변경 0건), ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0, 헌법 본문 0 (5조-2 Provider Liquidity 비협상 답습), 11 workflow 본문 0 (34번째 entry audit 답습), branch protection rule 0 (31번째 entry 7 contexts 답습), (b1) 4 sub-cycle brief + 합의 본문 0, 33번째 entry PASS evidence 본문 0, roadmap-mvp1 §2.2 / §3.5 / §4.5 / §4.7.3 / §5.1 / §9 본문 0 (§3.6.3 line 290 framing 한정), src 0, tools 0, docker 0, `.pre-commit-config.yaml` 0, `.githooks/` 0, MVP-2 자동 발효 0, adapters/llm/facade.py 0, 32번째 entry 프라이데이 brief 본문 0, 풀 3+1 합의 0 (Reviewer-only 답습), R-MVP1-PASS-{1~10} trigger 발화 0건. **변경 영역 = governance-preconditions 6 위치 + backlog1 합의 3 위치 + roadmap-mvp1 §3.6.3 line 290 framing 1 위치 = 10 위치 cross-reference + brief 신규 + SESSION + INDEX 한정**.
docs/sessions/SESSION_2026-05-27.md:948:  - `docs/architecture/mvp-1-to-6-entry-conditions-brief.md` 1 위치: line 93 (§ ADR-011 (a)~(e) 매트릭스 (c) cell GP-3 + GP-5)
docs/sessions/SESSION_2026-05-27.md:950:- 정정 형태: 35번째 entry 답습 = `ADR-008 §A.2 R1-2 / §2.6.4 R1-2 / §2.6.2 R2-1` → `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011` multi-source 재기술 (R-3 BLOCKING 답습)
docs/sessions/SESSION_2026-05-27.md:957:**원칙 준수**: ADR-008 본문 0 (R-MVP1-PASS-2 영구 금지) / ADR-011 / ADR-010 / ADR-009 / ADR-012 0 / 헌법 0 (5조-2 답습) / 11 workflow 본문 0 (34번째 audit 답습) / branch protection rule 0 (31번째 답습) / (b1) 4 sub-cycle brief + 합의 본문 0 / 33번째 entry PASS evidence 본문 0 / 35번째 entry brief / 합의 본문 0 / src 0 / tools 0 / docker 0 / `.pre-commit-config.yaml` 0 / `.githooks/` 0 / MVP-2 자동 발효 0 / adapters/llm/facade.py 0 / 32번째 entry 프라이데이 brief 본문 0 / 풀 3+1 합의 0 (1-agent 직접) / hermes-adoption-design.md 본문 0 (자체 §X source-of-truth 답습) — **20/20 유지**. **변경 영역 = roadmap-mvp1 9 위치 cross-reference + mvp-1-to-6 1 위치 + 2026-05-13-mvp1-pass 1 위치 = 11 위치 정정 + evidence file 1건 신규 + SESSION + INDEX 한정** (실 정정 = 9 위치, line 137 = 2 cell 정정 = 1 line 카운트 = 9 위치 답습).
docs/sessions/SESSION_2026-05-27.md:995:| `docs/architecture/mvp-1-to-6-entry-conditions-brief.md` | 1 위치 cross-reference 정정 (line 93, §ADR-011 (a)~(e) 매트릭스 (c) cell GP-3 + GP-5) |
docs/sessions/SESSION_2026-05-27.md:1002:ADR-008 본문 0 (R-MVP1-PASS-2 영구 금지 답습), ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0, 헌법 본문 0 (5조-2 답습), 11 workflow 본문 0 (34번째 audit 답습), branch protection rule 0 (31번째 답습), (b1) 4 sub-cycle brief + 합의 본문 0, 33번째 entry PASS evidence 본문 0, 35번째 entry brief / 합의 본문 0, hermes-adoption-design.md 본문 0 (자체 §X source-of-truth 답습), roadmap-mvp1 §2.2 + §3.5 (carry-over status 외) + §4.5 + §4.7.3 + §5.1 (35+36 정정 cell 외) + §9 본문 0 (R-S1 정정 영역 한정), src 0, tools 0, docker 0, `.pre-commit-config.yaml` 0, `.githooks/` 0, MVP-2 자동 발효 0, adapters/llm/facade.py 0, 32번째 entry 프라이데이 brief 본문 0, 풀 3+1 합의 0 (1-agent 직접), R-MVP1-PASS-{1~10} trigger 발화 0건 (R-S1 정정 = R-MVP1-PASS-10 답습 = 단순 cross-reference 한정, 권위 본문 의미 변경 0건). **변경 영역 = R-S1 정정 9 위치 + evidence file 1건 신규 + SESSION + INDEX 한정**.
docs/sessions/SESSION_2026-05-27.md:1018:- 정정 형태: 35/36 답습 = multi-source 재기술 (`ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011` 또는 GP-3 영역에 따라 `차단조건 #6 + 부록 B`)
docs/sessions/SESSION_2026-05-27.md:1022:**원칙 준수**: ADR-008 본문 0 (R-MVP1-PASS-2 영구 금지) / ADR-011 / ADR-010 / ADR-009 / ADR-012 0 / 헌법 0 / 11 workflow 본문 0 / branch protection 0 / (b1) 4 sub-cycle 본문 0 / 33번째 PASS evidence 본문 0 / 35/36 brief / evidence / 합의 본문 0 / roadmap-mvp1 본문 0 (36 정정 답습 유지) / hermes-adoption-design 본문 0 (자체 §X 답습) / src 0 / tools 0 / docker 0 / `.pre-commit-config.yaml` 0 / `.githooks/` 0 / MVP-2 자동 0 / facade.py 0 / 32번째 프라이데이 brief 0 / 풀 3+1 합의 0 (1-agent 직접) — **19/19 유지**.
docs/sessions/SESSION_2026-05-27.md:1068:ADR-008 본문 0 (R-MVP1-PASS-2 영구 금지 답습), ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0, 헌법 본문 0, 11 workflow 본문 0, branch protection rule 0, (b1) 4 sub-cycle brief + 합의 본문 0, 33번째 PASS evidence 본문 0, 35/36 brief / evidence / 합의 본문 0, roadmap-mvp1 본문 0 (36 정정 답습), hermes-adoption-design 본문 0 (자체 §X), src 0, tools 0, docker 0, `.pre-commit-config.yaml` 0, `.githooks/` 0, MVP-2 자동 발효 0, adapters/llm/facade.py 0, 32번째 entry 프라이데이 brief 본문 0, 풀 3+1 합의 0 (1-agent 직접), R-MVP1-PASS-{1~10} trigger 발화 0건. **변경 영역 = R-S1 정정 19 위치 + evidence file 1건 신규 + SESSION + INDEX 한정**.
docs/sessions/SESSION_2026-05-27.md:1083:  - `ADR-008 §A.2 R1-2` → `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011`
docs/sessions/SESSION_2026-05-27.md:1090:**원칙 준수**: ADR-008 본문 변경 0건 (R-MVP1-PASS-2 영구 금지 답습) / ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0 / 헌법 본문 0 / 11 workflow 본문 0 / branch protection rule 0 / (b1) 4 sub-cycle 본문 0 / 33번째 PASS evidence 본문 0 / 자기언급 13 file 본문 0 (explanation 보존) / hermes-adoption-design 본문 0 (자체 §X 답습) / src 0 / tools 0 / docker 0 / `.pre-commit-config.yaml` 0 / `.githooks/` 0 / MVP-2 자동 발효 0 / adapters/llm/facade.py 0 / 32번째 프라이데이 brief 본문 0 / 풀 3+1 합의 0 (1-agent 직접 + sed 자동화) — **19/19 유지**.
docs/sessions/SESSION_2026-05-27.md:1129:ADR-008 본문 0 (R-MVP1-PASS-2 영구 금지 답습), ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0, 헌법 본문 0, 11 workflow 본문 0, branch protection rule 0, (b1) 4 sub-cycle brief + 합의 본문 0, 33번째 PASS evidence 본문 0, 자기언급 13 file 본문 0 (explanation 보존), hermes-adoption-design 본문 0 (자체 §X), src 0, tools 0, docker 0, `.pre-commit-config.yaml` 0, `.githooks/` 0, MVP-2 자동 발효 0, adapters/llm/facade.py 0, 32번째 프라이데이 brief 본문 0, 풀 3+1 합의 0 (1-agent 직접 + sed 자동화), R-MVP1-PASS-{1~10} trigger 발화 0건. **변경 영역 = 50 file × 160 위치 sed 일괄 cross-reference 정정 + evidence file 1건 신규 + SESSION + INDEX 한정**.
docs/sessions/SESSION_2026-05-27.md:1141:- `docs/phase0/g2-gp3-mvp1-evidence.md` 신규 (~150줄, 6장 자기진단 5/5) — GP-3 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 + (b1) 4 sub-cycle (PC-1+S-3+ST-2+AR-3) 통합 + 첫 PR evidence + R-S1 cascade 답습 + carry-over (PoC 자율 영역 + (b1-AR3 develop) + (b1-PC1-D6))
docs/sessions/SESSION_2026-05-27.md:1142:- `docs/phase0/g2-gp5-mvp1-evidence.md` 신규 (~110줄, 6장 자기진단 5/5) — GP-5 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 + AR-3 통합 (GP-3+GP-5) + 첫 PR `enforce` x3 + `scan` (provider-url-scanner) PASS evidence + R-S1 cascade R-2 답습 + carry-over ((d) facade real + MVP-2)
docs/sessions/SESSION_2026-05-27.md:1171:- PC-1-T3 PoC evidence (`bash bin/setup.sh` + `bash tools/pre_commit_install_audit.sh` 사용자 dev 환경 영역)
docs/sessions/SESSION_2026-05-27.md:1197:| 26 | (b1) 1/4 PC-1-T3 | `3a63a5b` |
docs/sessions/SESSION_2026-05-27.md:1221:- PC-1-T3 PoC evidence 수집
docs/sessions/SESSION_2026-05-27.md:1235:> **흐름**: 새 세션 시작 → 사용자 "우선순위대로 진행" → carry-over 1순위 = (b1-PC1-D6) → 현 상태 audit (`tools/pre_commit_install_audit.sh` 존재 + 11 workflow nightly 2건 = r2-canary + secret-hygiene-egress-redaction) → 사용자 결정 (A) 신규 workflow → brief v1 작성 (190줄, 10장 자기진단 8/8) → 사용자 승인 + 단축 합의 진입 명시 → Reviewer-only 단축 합의 (5/5 풀 3+1 승격 trigger 0건 발화 검증 + PC-1-T3 합의 + 24번째 entry 합의 cross-check + 사용자 결정 3/3 답습 + 변경 0건 9/9 + R-6/D-6/R-7(b) 3/3 흡수 + 실 구현 7/7 cross-check + Rollback 2 + Evidence 3 + carry-over 3) → **APPROVE 발효** → 사용자 명시 단계 4 진입 → 실 구현 (`.github/workflows/pre-commit-bypass-detection.yml` 신규 1건, YAML 문법 valid) → SESSION + INDEX + 본 정리 commit.
docs/sessions/SESSION_2026-05-27.md:1239:⭐⭐ **(b1-PC1-D6) bypass detection CI 통합 sub-cycle 완료**. 26번째 entry PC-1-T3 brief §10 D-6 carry-over (default 권고 `(ii) 별도 sub-cycle`) 집행. 본 sub-cycle = workflow 1 file 신규 한정 (기존 11 workflow 본문 변경 0 + `.pre-commit-config.yaml` 본문 변경 0 + `tools/pre_commit_install_audit.sh` 본문 변경 0).
docs/sessions/SESSION_2026-05-27.md:1241:- brief 작성 (`docs/phase0/mvp1-pc1-d6-bypass-detection-ci-brief.md`, 190줄, 10장, 자기진단 8/8): scope/답습 출처 6/R-6+D-6+R-7(b) 흡수/ADR-011 매트릭스/실 구현 1 항목/Rollback 2/Evidence 3/합의 형태 권고 (Reviewer-only)/carry-over 3/다음 단계
docs/sessions/SESSION_2026-05-27.md:1242:- Reviewer-only 단축 합의 보고서 (`docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-d6-bypass-detection-ci.md`, 175줄, 10장, 자기진단 5/5): 5/5 풀 3+1 승격 trigger 0건 발화 검증 + 사용자 결정 3/3 답습 + ADR-011 (a)(c)(e) 3/5 충족 (본 합의 시점) + 변경 0건 9/9 + R-6/D-6/R-7(b) 흡수 3/3 + 실 구현 cross-check 7/7 → **APPROVE 발효**
docs/sessions/SESSION_2026-05-27.md:1266:- ✅ 26번째 entry PC-1-T3 brief §10 D-6 carry-over 해소
docs/sessions/SESSION_2026-05-27.md:1287:- PC-1-T3 PoC evidence (`bash bin/setup.sh` + `bash tools/pre_commit_install_audit.sh` 사용자 dev 환경 영역)
docs/sessions/SESSION_2026-05-27.md:1303:`tools/pre_commit_install_audit.sh` 본문 0 (PC-1-T3 답습 유지), `.pre-commit-config.yaml` 본문 0 (R-7(b) 차등 영역), `.githooks/pre-commit` 본문 0 (Layer 3 답습), 기존 11 workflow 본문 0 (D-6 (A) 신규 workflow 사용자 명시 답습), branch protection rule contexts 0 (AR-3 admin scope, 사용자 영역 carry-over), src/ 0, tools/ 기존 21 도구 본문 0, ADR 0 (R-MVP1-PASS-2 영구 금지 답습), 헌법 0 (R-MVP1-PASS-9 답습), roadmap-mvp1 본문 0 (36 정정 답습), governance-preconditions 0, MVP-1 Implementation Evidence PASS 재선언 0 (33번째 entry 답습 유지, 본 cycle = (b)(d) 회귀 자격 *보강* 한정), Operational Readiness PASS 0, Hermes PMO 격상 0, adapters/llm/facade.py 0 ((d) carry-over 영역), 풀 3+1 합의 0 (Reviewer-only 단축 합의 답습). **변경 영역 = workflow 1 file 신규 + brief + 합의 + SESSION + INDEX 한정**.
docs/sessions/SESSION_2026-05-27.md:1343:  - 조치 후보: (a) secret-scanner 패턴 정정 (false positive 회피, 별도 합의) / (b) `.pre-commit-config.yaml` 의 secret-scanner hook에 `exclude: src/jarvis/` 추가 (R-7(b) 차등 검증 필요) / (c) src/jarvis/ 코드 회피 (`code=` → `exit_code=` 등 rename) / (d) secret-scanner whitelist 추가
docs/sessions/SESSION_2026-05-27.md:1344:  - 합의 형태 권고: **풀 3+1** (secret-scanner 패턴 변경 = G3 Tier-1 catalog 영향 가능성, R-7(b) PC1-2 차등 자격 검토 의무)
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:199:| Hermes ≠ root of trust | ADR-011 답습 |
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:319:### 5.3 hook #6 — `import-linter` (Cycle 시점 정비, 옵션 (b) ii 답습)
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:588:### 12.1 ADR-011 §2.1 (a)~(e) 5조건 답습
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:594:| (c) | ADR / SDD 권위 명시 | mvp1.md §4.3 + §5.5.1 / §5.5.2 + ADR-011 §2.4 + 선행 brief chain (`11d7ebb` + `e9614a6` + `c292c9d` + `611aab3` + `1efb75d` + 본 brief) 답습 |
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:652:| (vii) ADR-011 §2.1 (a)~(e) 5/5 충족 + 합의 APPROVE | ⏳ 별도 합의 |
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:694:### 15.3 후속 합의 보고서 후보
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:766:| 사용자 결정 3개 (α/ii/ii) 답습 | ✅ §0.2 + §6 + §7 + §4.2~4.4 + §5.3~5.4 |
docs/architecture/implementation-runtime-roadmap.md:7:**상위 권위**: ADR-011 §2.1 (a)~(d) + (e) 5조건 패턴, ADR-008 부록 C §C.5 분리 매트릭스, P2 v3 §3.1.4 Implementation Pending 표
docs/architecture/implementation-runtime-roadmap.md:23:4. R-2 / R-4.1 PoC 패턴 답습 의무 명시 (ADR-011 §2.1 (b) 5조건 답습)
docs/architecture/implementation-runtime-roadmap.md:37:본 문서는 **DRAFT** — Reviewer-only 단축 검토 후 사용자 명시 결정으로 *권고 권위* 발행. 각 항목 PASS = *별도 합의* (단축 또는 풀 3+1, ADR-011 §2.1 (a)~(e) 5조건 답습) + PoC evidence + 사용자 명시 결정.
docs/architecture/implementation-runtime-roadmap.md:61:| **G2** | **GP-2 Egress Redaction** (로그 / LLM 송신 차단) | PoC + CI | ADR-011 §2.3 운영 함의 #2, ADR-008 부록 B + §A.2, P1 v2 §8.2 RedactionFilter, R-4 patterns | (a) 동등 이상 보안 결과 (Hermes native + P1 facade redaction 비교) / (b) 격리 PoC (Docker isolation) / (c) ADR 권위 (ADR-011 §2.3 #2) / (d) 자동 회귀 (R-2 답습 nightly) / (e) 합의 APPROVE | log/송신 redaction 6 patterns BLOCK 100% + base64 evasion BLOCK + R-2 답습 PoC PASS | **HIGH** (P2 헌법 8조 위반 경로) | **5 (10/11)** |
docs/architecture/implementation-runtime-roadmap.md:63:| **G2** | **GP-4 External Input Validation** (Hermes / Worker 출력 포함) | PoC + CI + recommended Reviewer agent | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력), GP-4 §6.3, G3 §1.3 | (a) 입력 schema validation + regex sanitizer + 명시 escape (sql/shell) / (b) Reviewer Agent prompt injection 감지 PoC / (c) ADR-011 §2.3 #1 + GP-4 / (d) CI (pydantic test + escape unit test) / (e) 합의 APPROVE | input schema validation 100% + sql injection BLOCK + command injection BLOCK + path traversal BLOCK | **MEDIUM-HIGH** (P5 헌법 8조 #3) | **6 (8/11)** |
docs/architecture/implementation-runtime-roadmap.md:85:| **G3** | **Hermes 권한 22 항목 runtime enforcement** (T1 8 / T2 2 / T3 12) | hook + wrapper + sidecar + CI | ADR-011 §2.4 T1/T2/T3, G3 §2 22 권한, ADR-009 C-N §2.3 (PMO ↔ provider) | (a) 22 권한 별 enforcement matrix / (b) 격리 PoC (Docker — Hermes container 권한 검증) / (c) ADR-011 §2.4 + G3 §2 / (d) CI nightly + GitHub Actions / (e) 합의 APPROVE | T3 12 권한 100% BLOCK (CI 회귀 검증) + T2 2 권한 사용자 명시 강제 + T1 8 권한 자동 OK | **HIGH** (Hermes ≠ root of trust 핵심 운영) | 11 (분리 권고 — 22 권한 각자 PoC 부담 ↑) |
docs/architecture/implementation-runtime-roadmap.md:89:| **G3** | **합의 자기참조 차단** (Hermes 가 합의 인프라 자기 격상 차단) | governance hook | G3 §4 합의 인프라 순환 권위 + ADR-011 §2.3 + ADR-009 C-N §2.3 | (a) Hermes 단독 합의 차단 (Reviewer-only 또는 외부 LLM 의견 의무) / (b) 격리 PoC (Hermes 단독 합의 시도 → BLOCK) / (c) G3 §4 / (d) CI step (commit author + Reviewer 체크) / (e) 합의 APPROVE | Hermes 단독 합의 100% BLOCK + Reviewer-only 또는 외부 LLM 의견 강제 검증 | **HIGH** (메타-순환 권위 침해) | **9 (7/11)** — 합의 보고서 검증 영역, 부분 수동 |
docs/architecture/implementation-runtime-roadmap.md:172:### 5.3 PoC 동시 진행 가능 영역 (병렬 작업 효율 ↑)
docs/architecture/implementation-runtime-roadmap.md:202:각 그룹 PASS 시 **ADR-011 §2.1 (a)~(e) 5조건 답습 의무** + Evidence Ledger entry (`event: gate_pass` 또는 `event: skill_promoted` 등) + Adoption decision commit.
docs/architecture/implementation-runtime-roadmap.md:208:### 6.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (모든 항목 의무)
docs/architecture/implementation-runtime-roadmap.md:256:- ✅ ADR-011 §2.1 (a)~(e) 5조건 답습 매트릭스
docs/architecture/implementation-runtime-roadmap-mvp1.md:11:**상위 권위**: ADR-011 §2.1 (a)~(e), ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), P2 v3 §3.1.4 (Implementation Pending), 외부 LLM GPT-5.5 Thinking 응답 §6 (3-layer PASS 분리)
docs/architecture/implementation-runtime-roadmap-mvp1.md:17:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5조건 패턴
docs/architecture/implementation-runtime-roadmap-mvp1.md:131:각 GP 별 Implementation Evidence PASS 진입 5 조건 = ADR-011 §2.1 (a)~(e) 답습 (§5 답습):
docs/architecture/implementation-runtime-roadmap-mvp1.md:137:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:143:> ⭐⭐⭐ **2026-05-27 발효 (32번째 entry)**: **GP-3 5/5 + GP-5 5/5 모두 충족 자격 자격 인정 + 사용자 명시 결정 = MVP-1 Implementation Evidence PASS *완전 발효* (α)**. 본 발효 = (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-6 답습).
docs/architecture/implementation-runtime-roadmap-mvp1.md:205:| **ST-1** | **Hermes Dockerfile entrypoint stat 검증** (chmod 600 강제) | 컨테이너 시작 시 | ✅ 필요 (Hermes upstream Dockerfile 수정) | ❌ | 低 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:206:| **ST-2** | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지) | 런타임 지속 | ❌ (sidecar 분리 가능) | ✅ | 中 (sidecar process 운영) | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:207:| **ST-3** | **docker secret 직접 사용** | 런타임 (file system 통한 노출 회피) | 부분 (docker-compose.yml 갱신) | ❌ | 低 | ADR-008 차단조건 #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:209:| **ST-5** | **ST-1 + ST-2 + ST-3 통합** (Defense in depth) | 시작 + 런타임 + file system | ✅ 필요 | ✅ | 中-高 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + GP-3 §5.3 통합 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:283:| ADR-008 cross-reference 갱신 (차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011) | ADR-008 본문 답습 (cross-reference 한정, R-MVP1-PASS-2 영구 금지 답습) | ✅ 35번째 entry (b2) gov + backlog1 + 36번째 entry (b2-roadmap) roadmap-mvp1 본문 R-S1 정정 완료 답습 |
docs/architecture/implementation-runtime-roadmap-mvp1.md:295:| Implementation Evidence PASS 발효 (GP-3 한정) | **별도 합의 + 사용자 명시 결정** + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | 본 문서 §2.2 답습 |
docs/architecture/implementation-runtime-roadmap-mvp1.md:296:| ⭐⭐⭐ **Implementation Evidence PASS *발효 완료* (GP-3 한정)** | **2026-05-27 (32번째 entry, commit `(본 commit)`)** — 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS + 사용자 명시 결정 + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | (b1) 4 sub-cycle + 31번째 entry 첫 PR (head SHA `9837298`) 11/11 SUCCESS + 본 cycle 합의 `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` |
docs/architecture/implementation-runtime-roadmap-mvp1.md:374:| **PC-1** | **pre-commit framework** (`.pre-commit-config.yaml` + `pre-commit install`) | hook 정의 통일 + dev 환경 자동 설치 | 中 (framework 도입 + dev 환경 강제) | T2 (정책 영역, ADR-011 §2.4 답습) | Group D PoC §1.2 #7 + Group A 2차 §1.2 답습 |
docs/architecture/implementation-runtime-roadmap-mvp1.md:387:본 권고는 **수단 *결정* 아님**. PC-1 (pre-commit framework) 도입 = T2 정책 영역 (ADR-011 §2.4 답습) → 단축 합의 적격 (사용자 명시 결정).
docs/architecture/implementation-runtime-roadmap-mvp1.md:483:| MVP-1 1.5차 (PC-1 pre-commit framework 도입) | **단축 합의 + 사용자 명시** | T2 정책 영역 (ADR-011 §2.4 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:487:| Implementation Evidence PASS 발효 (GP-5 한정) | **별도 합의 + 사용자 명시 결정** + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | 본 문서 §2.2 답습 |
docs/architecture/implementation-runtime-roadmap-mvp1.md:488:| ⭐⭐⭐ **Implementation Evidence PASS *발효 완료* (GP-5 한정)** | **2026-05-27 (32번째 entry, commit `(본 commit)`)** — 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS + 사용자 명시 결정 + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | (b1) 4 sub-cycle (AR-3 = GP-3+GP-5 통합) + 31번째 entry 첫 PR (head SHA `9837298`) `enforce` x3 + `scan` (provider-url) SUCCESS + 본 cycle 합의 `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` |
docs/architecture/implementation-runtime-roadmap-mvp1.md:494:### 5.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (양 GP 공통)
docs/architecture/implementation-runtime-roadmap-mvp1.md:506:> ⭐⭐⭐ **2026-05-27 발효 완료 (32번째 entry, commit `(본 commit)`)**: 본 5/5 매트릭스 양 GP 모두 충족 자격 자격 인정 + 사용자 명시 결정 + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 = **MVP-1 Implementation Evidence PASS *완전 발효 (α)***. 답습 source: (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2 + AR-3) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + 본 cycle 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 (별도 sub-cycle, ADR-008 본문 변경 0건 영구 의무 R-MVP1-PASS-2 답습) + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-MVP1-PASS-8 답습 + R-6 BLOCKING 답습 = 다음 cycle 우선순위).
docs/architecture/implementation-runtime-roadmap-mvp1.md:515:| `mvp1_gate_pass` | MVP-1 = GP-3 + GP-5 양쪽 PASS | T3 (사용자 명시 + ADR-011 §2.1 5/5 evidence) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:519:### 5.3 통합 Rollback Trigger 매트릭스
docs/architecture/implementation-runtime-roadmap-mvp1.md:653:- Layer C (Implementation Evidence PASS) 진입 (별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시)
docs/architecture/implementation-runtime-roadmap-mvp1.md:692:#### 5.5.3 본문 채택 합산 매트릭스
docs/architecture/implementation-runtime-roadmap-mvp1.md:722:- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정 — ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
docs/architecture/implementation-runtime-roadmap-mvp1.md:729:- ❌ §3 GP-3 / §4 GP-5 / §5.1 / §5.2 / §5.3 / §5.4 / §6 / §7 본문 변경 (cross-reference 답습 한정)
docs/architecture/implementation-runtime-roadmap-mvp1.md:733:- Layer C (Implementation Evidence PASS) 진입 → 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시
docs/architecture/implementation-runtime-roadmap-mvp1.md:777:- ✅ MVP-1 통합 PASS 기준 (ADR-011 §2.1 (a)~(e) 답습)
docs/architecture/implementation-runtime-roadmap-mvp1.md:810:5. **MVP-1 PASS 발효** — GP-3 + GP-5 양쪽 ADR-011 §2.1 (a)~(e) 5/5 충족 + 사용자 명시 + Implementation Evidence PASS 발효 합의
docs/architecture/implementation-runtime-roadmap-mvp1.md:826:| 2026-05-27 | 본 문서 DRAFT → APPROVED 권위 발효 (Reviewer-only 단축 합의) | `docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md` APPROVE (단축 합의 — Reviewer-only). 입력 = `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (2026-05-27 audit). **5/5 풀 3+1 승격 트리거 0건 발화 검증** (① 새 권위 결정 0 / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0). 후속 3 합의 본문 흡수 완료 cross-check (line 819~821 = gp3 + gp5 + backlog #6) + ADR-011 §2.1 (a)~(e) 답습 정확. **본 합의 = 권위 표시 격상 한정 — line 826/827 상태 표시 + §9 변경 이력 line 1건 추가 한정 — 본문 §1~§8 변경 0건 (cross-reference 답습 한정). 실 runtime code / CI / hook 변경 0건 / Implementation Evidence PASS / Operational Readiness PASS / ADR 본문 갱신 / 수단 결정 / threshold 고정 / Tier-2/3 자동 확장 모두 본 합의 영역 외 (사용자 명시 결정 의무 영역)**. |
docs/architecture/implementation-runtime-roadmap-mvp1.md:827:| 2026-05-27 (32번째 entry) | ⭐⭐⭐ **MVP-1 Implementation Evidence PASS 완전 발효 (α)** — §2.2 (line 141 영역) + §3.6.3 (GP-3 합의 형태 권고 표) + §4.7.3 (GP-5 합의 형태 권고 표) + §5.1 (통합 PASS 권고) 각 영역에 "2026-05-27 발효 완료" 행 추가 | (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 chain `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). 본 흡수 = §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 갱신 한정 — §3 GP-3 / §4 GP-5 / §5.2~§5.5 / §6 / §7 본문 변경 0건. carry-over (PASS 효과 영향 0건): (b2) R-S1 + PC-1-T3 PoC 자율 + ST-2 nightly 자율 + paths-aware audit (R-6 BLOCKING 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:828:| 2026-05-12 후속 4 | §5.5 9 sub-수단 본문 채택 매트릭스 신설 — Layer B `f40423f` 발효 결과 행사 | Backlog #6 Layer B Implementation Entry 합의 (`docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` APPROVE, commit `f40423f` push 완료) §1.1 + §1.2 + §1.7 답습 + 사용자 명시 진입 명령 (2026-05-12 열한 번째 — "9 sub-수단 본문 채택 commit 진입"). §5.5 신설 = §5.5.0 본문 채택 의미 명시 (본문 채택 ≠ runtime code 구현 / CI workflow 구현 / hook 구현 / Implementation Evidence PASS) + §5.5.1 GP-3 4 sub-수단 (S-1 + ST-3 + PC-3 + AR-1) + G3-7 row 4 항목 + §5.5.2 GP-5 3 sub-수단 (T-6 = T-2 + T-5 / PC-3 + AR-1) + Group A 1차/2차/3차 답습 + §5.5.3 합산 매트릭스 (9 = 7 unique + 2 일관성 중복) + §5.5.4 18 Rollback Trigger 본문 확정 답습 + §5.5.5 *범위 한계* (runtime code / CI workflow / hook 실 구현 0건 / Layer C 발효 0건 / 7 backlog 자동 진입 0건 / ADR 본문 갱신 0건 / Tier-2/3 자동 확장 0건 / threshold 고정 0건 / event enum 정식 등록 0건). **본 흡수 = §5.5 신설 + 변경 이력 추가 한정 — §3 GP-3 / §4 GP-5 / §5.1 / §5.2 / §5.3 / §5.4 / §6 / §7 본문 변경 0건 (cross-reference 답습 한정)**. **본문 채택 = 문서상 확정 한정 — runtime code 실 구현 / CI workflow 실 신설 / hook 실 구현 모두 본 흡수 영역 외 (사용자 명시 결정 의무 영역)**. |
docs/architecture/implementation-runtime-roadmap-mvp1.md:829:| 2026-05-12 후속 2 | §5.4 GP-3 + GP-5 Integrated Risk Matrix 신설 — Observation O-2 흡수 (GP-5 진입 합의 Condition C-4) | GP-5 MVP-1 진입 합의 (`3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` APPROVE WITH CONDITIONS) §6.3 + §7.4 답습 + 사용자 명시 진입 명령 (2026-05-12 여섯 번째). §5.4 신설 = 3 통합 위험 (IR-1 Provider key adapter bypass / IR-2 Direct SDK + secret leakage 결합 / IR-3 Local-CI-Docker mismatch) + 3 신규 evidence enum 후보 (`provider_key_adapter_bypass_risk_detected` / `direct_sdk_with_secret_leakage_detected` / `secret_handling_environment_mismatch_detected`) + MVP-1 handling vs Deferred handling 분리 + §5.4.4 *범위 한계* (실 combined check 도구 구현 0건 / enum 정식 등록 0건 / Runtime enforcement 0건 / Operational parity 0건 / Provider key auto revoke 0건 / Combined fail PR auto-reject 0건). §5.2 cross-reference 갱신 — 4 enum → 7 enum 후보 합산. **본 흡수 = §5.4 신설 + §5.2 cross-reference 갱신 + 변경 이력 추가 한정 — §3 GP-3 / §4 GP-5 / §5.1 / §5.3 / §6 / §7 본문 변경 0건**. |
docs/architecture/implementation-runtime-roadmap-mvp1.md:837:**다음 단계** (2026-05-27 32번째 entry 후): ✅ (b) MVP-1 1.5차 보강 합의 완료 (24번째 entry) → ✅ (b1) 4 sub-cycle 완료 (PC-1-T3 + S-3 + ST-2 + AR-3) → ✅ (c) **Implementation Evidence PASS 완전 발효 완료** (32번째 entry, 본 commit) → ⏳ (D-5 재조정 R-6 BLOCKING 답습): paths-aware workflow audit (R-MVP1-PASS-8 답습) → (b2) R-S1 cross-reference 정정 + (b3) framing 정정 (병렬) → Markdown evidence 통합 (D-3 carry-over) → (b1-PC1-D6) bypass detection CI 통합 → PR #2 merge 결정 (사용자 자율) → (d) facade real → MVP-2 진입 자격 검토 (별도 합의 영역)
docs/architecture/hermes-not-root-of-trust-runtime.md:3:> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 G3 — "Hermes ≠ root of trust" 원칙 (ADR-011 §2.3 영구 권위) 의 *운영 가능 메커니즘 설계 문서*. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
docs/architecture/hermes-not-root-of-trust-runtime.md:15:> **P2 v2 (`hermes-adoption-design.md`) = Archived (옵션 A 최소 침습, 2026-05-09 후속 7)** + **`system-identity-prequel.md` = Archived (옵션 A, 2026-05-09 후속 8 — 본 G3 §1 권위 위계 운영 매트릭스의 권위 출처 prequel §3 → ADR-011 §2.3 영구 권위 승격 답습으로 archive 후에도 권위 보존)** — 본 G3 cross-reference 영향 0건 (path 변경 0건).
docs/architecture/hermes-not-root-of-trust-runtime.md:23:**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 관용 (Provider Liquidity), **ADR-011 §2.3 (권위 위계 + 운영 함의 5항목, 영구 권위 — `system-identity-prequel.md` §3 → 본 ADR-011 §2.3 영구 승격, "prequel 폐기 후에도 보존" 직접 명시)**, **ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리, 영구 권위 — prequel §6 3-tier 선언 → ADR-011 §2.4 영구 승격)**, **ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목, 2026-05-09 후속 3 PR-2 신규 발행)**
docs/architecture/hermes-not-root-of-trust-runtime.md:25:> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S1 (CRITICAL) 답습]**: 본 line 23 (상위 권위) + line 176 (cross-ref 표) + line 1040 (영구 핵심 제약 표) 표기 "헌법 제5조 관용 (Provider Liquidity)" / "헌법 5조 (관용 — Provider Liquidity)" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") *외* **유일 추가 동형 source** 신규 식별 (R-S1 CRITICAL, Reviewer raw cross-check 강화 — bash grep `"헌법 제5조 (Provider Liquidity\|헌법 제5조 관용 (Provider Liquidity"` = ADR-012 + 본 source 단 2 파일 verify). Agent C 단독 발견 + Reviewer raw cross-check 직접 verify (line 176/1040 단독 추가 식별). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 7/897/1073 (P3 본문) = 본질 답습, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
docs/architecture/hermes-not-root-of-trust-runtime.md:26:**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-011 (수단/목적 분리), **ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위, 2026-05-09 후속 4 갱신)**, **ADR-012 (Evidence Ledger Protection — 본 G3 §1.3 + §5 PASS 성립 4 요건 (ii) Evidence Ledger entry 의 *형식적 무결성* 권위 출처)**
docs/architecture/hermes-not-root-of-trust-runtime.md:27:**관련 설계**: **`hermes-adoption-design-v3.md` §5 (G3 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `governance-preconditions.md` (G2 — GP-2~GP-6 인터페이스 의존 + §1.2.6 P10 Evidence Forgery 정식 등록), `provider-agnostic-memory-skill-design.md` (G4 — G3 §6.5 / §7 인터페이스 + §4 hash chain 사양), `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3 (권위 위계 prequel — ADR-011 §2.3로 영구 승격, **Archived 2026-05-09 후속 8**), `canary-recheck-design.md` (R-5), `redaction-pattern-equivalence.md` (R-4)
docs/architecture/hermes-not-root-of-trust-runtime.md:28:**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Agent B 단독 발견 "합의 인프라 순환 권위 역설" + GPT 핵심 원칙 "Agent proposes / Tools verify / Evidence decides / Human overrides"), `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (ADR-011 §2.3 권위 승격), `docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md` (G2 §9 메타 안전장치 G3 위임), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G3 정식 PASS 합의), **`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (ADR-012 발행 — 본 G3 §1.3 / §5 답습 권위)**, **`docs/review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` (P2 v3 정식 채택 — 본 G3 = P2 v3 §5 답습 권위)**
docs/architecture/hermes-not-root-of-trust-runtime.md:51:5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음
docs/architecture/hermes-not-root-of-trust-runtime.md:54:8. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
docs/architecture/hermes-not-root-of-trust-runtime.md:85:본 위계는 **ADR-011 §2.3** 영구 권위로 승격되어 있으며, system-identity-prequel.md archived 후에도 보존된다 (ADR-011 §2.3 prequel과의 관계). 본 §1 은 위 위계를 *런타임 충돌 시* 어떻게 작동하는지 정의한다.
docs/architecture/hermes-not-root-of-trust-runtime.md:93:| Hermes 가 ADR/SDD 와 모순되는 결정 제안 | **자동 reject** + 사용자 alert | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력) | 모순 detection log + Hermes 결정 본문 + ADR/SDD 인용 |
docs/architecture/hermes-not-root-of-trust-runtime.md:94:| Hermes 가 ADR/SDD 본문을 자동 수정 시도 | **filesystem read-only로 차단** + audit log + 컨테이너 정지 | ADR-011 §2.4 T3 (자동 정책 변경 금지) + system-identity-prequel §3.3 #1 | filesystem ACL 거부 log + audit log entry |
docs/architecture/hermes-not-root-of-trust-runtime.md:95:| Hermes 가 새 ADR 작성 제안 | 제안은 가능, **작성·승인은 사용자 명시 only** | ADR-011 §2.4 T2 | 제안 본문 (제안 한정 evidence) |
docs/architecture/hermes-not-root-of-trust-runtime.md:96:| ADR 갱신 PR (사용자 발의) 에 Hermes 가 자동 승인/merge 시도 | **CI step 으로 차단** (ADR PR 은 사용자 명시 결정 only) | ADR-011 §2.4 T3 | PR 차단 log |
docs/architecture/hermes-not-root-of-trust-runtime.md:102:| Worker 가 Hermes 와 다른 결론 도출 | **Tools 검증 결과 우선** — Hermes 출력은 Tools 위에 위치 안 함 | ADR-011 §2.3 운영 함의 #1 | Worker 출력 + Tools 검증 결과 + Hermes 결론 모두 보존 |
docs/architecture/hermes-not-root-of-trust-runtime.md:103:| Worker 출력을 Hermes 가 *내부* 처럼 신뢰 (검증 우회) | **GP-4 외부 입력 검증으로 차단** | G2 GP-4 + ADR-011 §2.3 운영 함의 #1 | 검증 layer 통과 evidence |
docs/architecture/hermes-not-root-of-trust-runtime.md:111:| Layer 1 (PostToolUse hook) 실패 시 Hermes 가 다음 단계 진행 시도 | **hook 실패 → Hermes 작업 큐 차단** | CLAUDE.md §피드백 루프 계층 + ADR-011 §2.3 | hook 실패 log + 큐 상태 |
docs/architecture/hermes-not-root-of-trust-runtime.md:114:| Layer 5 (3+1 합의) BLOCK / ROLLBACK 결과를 Hermes 가 silent override | **Hermes 단독 override 금지** + audit log + 자동 reject | system-identity-prequel §3.3 #2 + ADR-011 §2.4 T3 | 합의 결과 commit + Hermes override 시도 log |
docs/architecture/hermes-not-root-of-trust-runtime.md:115:| Layer 6 (사용자 review) 미완료 시 Hermes 가 다음 단계 진행 | **사용자 명시 승인 필요 영역에서는 Hermes 단독 진행 금지** | ADR-011 §2.4 T2 | 사용자 승인 evidence |
docs/architecture/hermes-not-root-of-trust-runtime.md:124:| Harness Gate (G1b 등) | (a)~(e) Exit 기준 모두 충족 + 합의 보고서 + ledger entry | 본 G3 §5.3 + 각 GP §X.5 |
docs/architecture/hermes-not-root-of-trust-runtime.md:150:다음은 Hermes 가 단독 권한으로 실행 가능 (ADR-011 §2.4 **T1 자동**):
docs/architecture/hermes-not-root-of-trust-runtime.md:165:다음은 Hermes 가 단독으로 시도 시 **자동 reject + audit log + 사용자 alert** (ADR-011 §2.4 **T3 절대 금지** 또는 **T2 사용자 승인 필수**):
docs/architecture/hermes-not-root-of-trust-runtime.md:169:| 9 | **정책 자동 변경** (Constitution / ADR / SDD / Harness Gate 정의) | T3 | ADR-011 §2.4 + system-identity-prequel §3.3 #1 | filesystem read-only mount + T3 변경 감지 hook |
docs/architecture/hermes-not-root-of-trust-runtime.md:170:| 10 | **ADR 자동 수정 / 자동 승인** | T3 | ADR-011 §2.4 + 헌법 7조 | filesystem read-only on `docs/decisions/ADR-*.md` + git pre-commit hook |
docs/architecture/hermes-not-root-of-trust-runtime.md:171:| 11 | **Constitution 우회** | T3 | 헌법 자체 + ADR-011 §2.3 위계 | Constitution write 권한 0 + audit log |
docs/architecture/hermes-not-root-of-trust-runtime.md:173:| 13 | **G2 / G3 / G4 PASS 자동 선언** | T3 | ADR-011 §2.4 + 본 G3 §4 (자기참조 차단) | git commit 본문 검증 hook + 합의 보고서 강제 |
docs/architecture/hermes-not-root-of-trust-runtime.md:176:| 16 | **Skill 자동 등록** | T2 | system-identity-prequel §8 + ADR-011 §2.4 | Skill 등록 hook 차단 + 사용자 명시 승인 강제 |
docs/architecture/hermes-not-root-of-trust-runtime.md:177:| 17 | **자체 학습 결과의 자동 정책 반영** | T3 | ADR-011 §2.4 (자동 학습 vs 정책 변경 분리) | 정책 파일 read-only + T3 변경 감지 hook |
docs/architecture/hermes-not-root-of-trust-runtime.md:179:| 19 | **Secret redaction 정책 완화** | T3 | ADR-011 §2.1 (수단/목적 분리) + G2 GP-1 / GP-2 | redaction-policy.yaml read-only + T3 변경 감지 hook |
docs/architecture/hermes-not-root-of-trust-runtime.md:181:| 21 | **Tier-1 / Tier-2 / Tier-3 canary catalog 자동 확장** | T3 | ADR-011 §2.4 + R-7 SOP §3.4 | catalog 파일 read-only + 별도 합의 강제 |
docs/architecture/hermes-not-root-of-trust-runtime.md:182:| 22 | **사용자 override 자동 reject 시도** | T3 | ADR-011 §2.3 운영 함의 #5 ("Human overrides") + §5.4 | override 거부 시도 자체가 audit log + 사용자 alert |
docs/architecture/hermes-not-root-of-trust-runtime.md:186:§2.1 허용 8건 + §2.2 금지 14건 = 총 22 권한 항목. ADR-011 §2.4 분류:
docs/architecture/hermes-not-root-of-trust-runtime.md:226:| 5 | `docs/decisions/ADR-*.md` (ADR 본문 전체) | T3 | filesystem read-only + git pre-commit hook | 본 §2.2 #10 (ADR 자동 수정) + ADR-011 §2.3 |
docs/architecture/hermes-not-root-of-trust-runtime.md:234:| 13 | `redaction-policy.yaml` / Tier-1 catalog / `skill-permissions.yaml` / `canary-catalog/` (정책성 파일) | T3 | filesystem read-only on Hermes container + R-5 canary recheck + 본 §3.1 (Learning silent drift) | ADR-011 §2.4 + 본 §2.2 #19, #21 |
docs/architecture/hermes-not-root-of-trust-runtime.md:249:> **본 §2.6 은 Gate Enforcement Layer 보호 보강 작업 신설** (사용자 명시 결정 — Gate 자체 + Layer 0~6 enforcement mechanism 양쪽 통합 보호 영역). §2.2 #12 (Harness Gate 실패 무시) / #13 (G2/G3/G4 PASS 자동 선언) / #14 (Hermes PMO 자기 격상) + §2.5 보호 대상 enumeration + §1.3 Evidence 없는 PASS 차단 + §5.3 PASS 성립 요건 의 *통합 강화* 영역. **본 §2.6 = *설계 문서 수준 보호 규칙*까지 — 실 runtime hook / CI workflow 수정 / filesystem ACL 구현 = Implementation/Runtime PASS 영역 별도 합의**.
docs/architecture/hermes-not-root-of-trust-runtime.md:272:| **TM-3 Evidence ledger forge** | Hermes 가 `event: gate_pass` ledger entry 자동 append (사용자 명시 결정 0건 + 합의 보고서 부재) | §2.6.2 (c) + §1.3 + ADR-012 §2.1 원칙 7 (`agent="user"` 강제) + §5.3 (ii) |
docs/architecture/hermes-not-root-of-trust-runtime.md:287:- *권위 근거*: 본 §2.2 #9, #10, #11, #13, #20 + ADR-011 §2.3 권위 위계 + ADR-008 부록 C §C.2
docs/architecture/hermes-not-root-of-trust-runtime.md:291:- Hermes 는 verdict 를 *제안* 가능 (§2.1 #6 답습), *승인 불가* (본 §1.3 + §4.5 + §5.3 답습)
docs/architecture/hermes-not-root-of-trust-runtime.md:293:- *권위 근거*: 본 §2.2 #13 + §4.5 합의 결과 처리 권한 + §5.3 PASS 성립 요건 (i)~(iv) + ADR-012 §2.12
docs/architecture/hermes-not-root-of-trust-runtime.md:335:- 모든 PASS 판정 = Evidence Ledger entry 존재 의무 (§1.3 + §5.3 (ii) 답습)
docs/architecture/hermes-not-root-of-trust-runtime.md:338:- *권위 근거*: 본 §1.3 + §5.3 (ii) + ADR-012 §2.2 (11 필드 schema) + 본 §5.2.4 (Evidence decides)
docs/architecture/hermes-not-root-of-trust-runtime.md:341:- JSONL Evidence Ledger append-only 강제 — entry 수정 / 삭제 / 재작성 모두 T3 영역 (ADR-011 §2.4 + ADR-012 §2.3 답습)
docs/architecture/hermes-not-root-of-trust-runtime.md:357:| 2 | Gate verdict mutation 방지 | T3 | 합의 보고서 + Evidence ledger entry 양쪽 일치 의무 + Hermes-originated verdict 변경 reject | 본 §2.2 #13, #20 + §4.5 + §5.3 |
docs/architecture/hermes-not-root-of-trust-runtime.md:364:| 9 | Gate policy 변경은 T3 또는 사용자 승인 영역 | T3 | filesystem read-only + 풀 3+1 합의 + ADR Amendment 절차 + 사용자 명시 결정 | 본 §10 변경 절차 + §2.2 #9, #11 + ADR-011 §2.4 T3 |
docs/architecture/hermes-not-root-of-trust-runtime.md:365:| 10 | Gate protection 실패 시 rollback trigger 발화 | T3 자동 안전 | Layer 1~4 결과 FAIL → Skill `revoked` 자동 전이 (G4 §3.4.2 답습) + Hermes 컨테이너 정지 (§3.1.3 답습) + 사용자 명시 alert | 본 §3.1.5 + §3.3.5 + G4 §3.8.2 + ADR-011 §2.4 T3 자동 안전 동작 |
docs/architecture/hermes-not-root-of-trust-runtime.md:424:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 (cross-reference 보강만 — 본문 갱신은 별도 PR 묶음)
docs/architecture/hermes-not-root-of-trust-runtime.md:443:Hermes 자체 학습 결과 (T1 자동 학습) 가 **redaction 정책 / canary catalog / Skill 권한 등급 / Memory boundary** 등 *정책성* 파일을 silent 변경. ADR-011 §2.4 (자동 학습 vs 정책 변경 분리) 직접 위반.
docs/architecture/hermes-not-root-of-trust-runtime.md:476:- ADR-011 §2.4 T3 위반 검출 → **Hermes 컨테이너 정지 + 변경 reject + 사용자 alert**
docs/architecture/hermes-not-root-of-trust-runtime.md:490:Hermes / Hermes-agent / pysqlcipher3 / litellm 등 의존성 업그레이드로 **redaction / SQLCipher trigger / P1 facade / canary catalog** 동작이 silent 깨짐. ADR-011 §2.3 운영 함의 #4 ("Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증") 직접 침해.
docs/architecture/hermes-not-root-of-trust-runtime.md:595:| 3. 사용자 승인이 모든 T2 / T3 결정의 *최종* 권위 | ADR-011 §2.4 T2/T3 + ADR-011 §2.3 운영 함의 #5 |
docs/architecture/hermes-not-root-of-trust-runtime.md:623:- ADR-011 §2.4 분류 T2 (사용자 승인 기반)
docs/architecture/hermes-not-root-of-trust-runtime.md:721:- 제안 자체는 PASS 가 아니며, **§5.3 PASS 성립 요건 충족 후만 PASS** 가 된다
docs/architecture/hermes-not-root-of-trust-runtime.md:727:- Hermes 는 PASS 를 *결정* 할 수 없다 (§5.3 답습)
docs/architecture/hermes-not-root-of-trust-runtime.md:750:### 5.3 PASS 성립 요건 (Hard Rule, §1.3 강화)
docs/architecture/hermes-not-root-of-trust-runtime.md:765:- (iv) 미충족 (해당 영역) → PASS verdict 본문에 합의 cross-reference 부재로 본 §5.3 위반
docs/architecture/hermes-not-root-of-trust-runtime.md:806:#### 5.5.3 Multi-host / 다인 전환 트리거 (의무 발동 조건)
docs/architecture/hermes-not-root-of-trust-runtime.md:833:3 §은 동일 SPOF 의 *3 측면* — 어느 하나만 보강해도 SPOF 자체는 완전 해소되지 않음. 본 §5.5.3 트리거 5건 *전부* 또는 별도 합의로만 SPOF 해소.
docs/architecture/hermes-not-root-of-trust-runtime.md:875:**G3 책임** (본 §6.3): "Hermes 출력은 Tools 로 검증된다" *권위 자체* 강제 (ADR-011 §2.3 운영 함의 #1).
docs/architecture/hermes-not-root-of-trust-runtime.md:989:- ✅ ADR-011 §2.3 권위 확정 (2026-05-06, 충족됨)
docs/architecture/hermes-not-root-of-trust-runtime.md:996:각 §의 Exit 기준 (a)~(e) 패턴은 ADR-011 §2.1 (a)~(d) + 합의 APPROVE (e) 답습:
docs/architecture/hermes-not-root-of-trust-runtime.md:1023:- ✅ G3 status: ADR-011 §2.3 권위 확정 + 운영 구현 미작성 → PASS (CONTEXT.md 4 게이트 진행 상태 갱신)
docs/architecture/hermes-not-root-of-trust-runtime.md:1025:- ✅ ADR-008 / ADR-011 cross-reference 갱신 (별도 PR)
docs/architecture/hermes-not-root-of-trust-runtime.md:1032:- ❌ ADR-011 §2.3 본문 자동 갱신 (cross-reference 만)
docs/architecture/hermes-not-root-of-trust-runtime.md:1043:| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위) | 본 G3 전체 (특히 §1 + §4 + §5) |
docs/architecture/hermes-not-root-of-trust-runtime.md:1045:| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 | §2.2 #9 #11 #14 #17 #19 #21 등 |
docs/architecture/hermes-not-root-of-trust-runtime.md:1046:| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) → 본 §8.2 (a)~(e) 패턴 답습 | §8.2 |
docs/architecture/hermes-not-root-of-trust-runtime.md:1075:2. **R-7 SOP §0 핵심 선언 답습**: 각 § Exit 기준 (a)~(e) 5조건은 ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e) 패턴 답습 — 본 초안이 새 권위 구조 트리거하지 않음.
docs/architecture/hermes-not-root-of-trust-runtime.md:1076:3. **ADR-011 §2.4 T1/T2/T3 답습**: §2.3 권한 항목 분류 (T1 8 / T2 2 / T3 12), §3 3 위험 사용자 승인 조건, §4.3 매트릭스 모두 T1/T2/T3 분류 답습.
docs/architecture/hermes-not-root-of-trust-runtime.md:1087:- §4.3 합의 형태 매트릭스는 *본 초안 원안* — system-identity-prequel §3.3 #2 + ADR-011 §2.3 / §2.4 권위 인용은 정확하나 *결정 유형별 합의 형태 매트릭스*는 본 초안이 처음. 후속 합의 검증 대상.
docs/architecture/hermes-not-root-of-trust-runtime.md:1095:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신
docs/architecture/hermes-not-root-of-trust-runtime.md:1108:1. ADR-011 §2.3 권위 위계 + §2.4 T1/T2/T3 분류 답습 (현 시점 Hermes 책임 한정에 적용)
docs/architecture/hermes-not-root-of-trust-runtime.md:1163:- ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — cross-reference 보강만, 본문 갱신은 별도 PR 묶음
docs/architecture/multi-agent-system-design.md:253:### 5.3 보안 변경
docs/architecture/governance-preconditions.md:27:**상위 결정**: ADR-008 (Hermes 도입 Option B) 6 차단조건, ADR-011 (수단/목적 분리, §2.3 권위 위계, §2.4 T1/T2/T3), **ADR-009 C-N (P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행)**
docs/architecture/governance-preconditions.md:28:**관련 설계**: **`hermes-adoption-design-v3.md` §4 (G2 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3.3 / §4.2 (**Archived 2026-05-09 후속 8**, 본 ADR-011 §2.3 영구 권위 승격 답습으로 권위 보존), `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
docs/architecture/governance-preconditions.md:42:5. 각 GP의 Entry / Exit 기준 (ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 + (e) 합의 APPROVE)
docs/architecture/governance-preconditions.md:53:5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음
docs/architecture/governance-preconditions.md:56:8. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
docs/architecture/governance-preconditions.md:78:**관용 표현**: ADR-008 / ADR-011 / system-identity-prequel / 본 v3 모두 "헌법 제5조-2 (Provider Liquidity, 비협상)" 표현 사용 ((g1-N-1) commit `148fbbe` 후 헌법 본문 직접 등재 완료).
docs/architecture/governance-preconditions.md:92:- 후속 작업: 헌법 본문 갱신 또는 ADR Amendment 결정은 풀 3+1 합의 영역 (T3 변경 — ADR-011 §2.4)
docs/architecture/governance-preconditions.md:105:| **P2** | **로그/LLM 송신 경로 평문 노출** | Hermes / Worker 가 secret 을 stdout / stderr / log file / LLM API request body 에 노출 | 8조 #2 | Hermes native redaction 보조 (ADR-011 §2.3 운영 함의 #2) |
docs/architecture/governance-preconditions.md:106:| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + entrypoint stat 검증 (35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:141:- ADR-011 §2.4 T3 (자동 정책 변경) 위반 자체 — **G3** ("Hermes ≠ root of trust" 운영 구현) 범위. 본 G2 §9 메타 안전장치에서 *interface*만 명시
docs/architecture/governance-preconditions.md:168:##### 1.2.5.3 본 §1.2.5 가 *하지 않는* 것
docs/architecture/governance-preconditions.md:272:| **사용자 승인 (User Approval)** | (i) 의존성 업그레이드 PR merge = **T2 사용자 명시 결정** (G3 §3.2.6 답습 — Hermes 자동 PR 생성 OK, 자동 merge 금지) (ii) `hermes-version.yaml` 신규 핀 등록 = T2 사용자 명시 + 사후 R-6 actual run PASS 의무 (iii) Action `@<sha>` 신규 등록 = T2 사용자 명시 (iv) Docker base image digest 변경 = T2 사용자 명시 + canary catalog 자동 재검증 (v) **Rollback 자체는 자동** (FAIL 시 차단 = 자동 안전 동작, ADR-011 §2.4 T3 자동 안전) | G3 §3.2.6 + ADR-011 §2.4 T2/T3 |
docs/architecture/governance-preconditions.md:312:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신
docs/architecture/governance-preconditions.md:341:| **GP-1** | DB-level Secret Persistence 차단 | P1 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | G1b PASS (이미 충족) + ADR-011 §2.1 |
docs/architecture/governance-preconditions.md:342:| **GP-2** | Egress Redaction (로그/LLM 송신) | P2 | Hermes native redaction (보조 — ADR-011 §2.3 #2) + LLM facade redaction filter (P1) | ADR-008 차단조건 #1 보조 + ADR-011 §2.3 |
docs/architecture/governance-preconditions.md:343:| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | (저장) docker secret + chmod 600 + entrypoint stat + inotify, (코드) gitleaks / detect-secrets pre-commit hook + CI step | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 (35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:344:| **GP-4** | 외부 입력 검증 (Hermes/Worker 출력 포함) | P5 | Hermes / Worker Agent 출력을 *외부 입력*으로 분류 + 검증 layer 강제 (헌법 5조 #4 + 8조 #3) | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력) |
docs/architecture/governance-preconditions.md:403:| (c) | ADR / SDD 권위 명시 | ADR-011 §2.1 + ADR-008 부록 B Amendment |
docs/architecture/governance-preconditions.md:413:- ADR-011 §2.1: 본문 변경 없음, §8.5 후속 작업에 G2 GP-1 흡수 등록 (G2 PASS 시점)
docs/architecture/governance-preconditions.md:424:**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
docs/architecture/governance-preconditions.md:438:| 자동 회귀 | Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4) | R-6 workflow trigger 확장 |
docs/architecture/governance-preconditions.md:453:| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #2 cross-reference + 본 §4 권위 |
docs/architecture/governance-preconditions.md:465:- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
docs/architecture/governance-preconditions.md:484:### 5.3 강제 메커니즘
docs/architecture/governance-preconditions.md:508:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5 (35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:532:Hermes 출력 + Worker Agent 출력 + LLM 응답 + tool output 모두를 *외부 입력*으로 분류하여 명시 검증 layer 를 거친다. ADR-011 §2.3 운영 함의 #1 ("Hermes 출력은 Tools 로 검증된다") 의 *입력 검증 측면* 구체화.
docs/architecture/governance-preconditions.md:562:| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #1 + 헌법 8조 #3 + 헌법 5조 #4 + 본 §6 |
docs/architecture/governance-preconditions.md:575:- ADR-011 §2.3 운영 함의 #1 cross-reference
docs/architecture/governance-preconditions.md:699:| 1 | filesystem read-only on `docs/architecture/governance-preconditions.md` (Hermes container mount ro) | ADR-011 §2.4 T3 + system-identity-prequel §3.3 #1 | G3 §5.2 #5 |
docs/architecture/governance-preconditions.md:702:| 4 | T3 변경 감지 hook → 자동 reject + 사용자 alert | ADR-011 §2.4 T3 | G3 §5.2 #5 |
docs/architecture/governance-preconditions.md:733:본 SPOF 는 **의도적으로 수용** (1인 개발자 + 단일 호스트 MVP 범위 답습). 의무 발동 트리거는 **G3 §5.5.3** 답습 (5 조건). 본 G2 §9.5 는 *보호 대상 무결성 측면* 만 명시:
docs/architecture/governance-preconditions.md:735:| # | 트리거 (G3 §5.5.3 답습) | G2 §9 측면 의무 발동 |
docs/architecture/governance-preconditions.md:743:#### 9.5.3 본 §9.5 가 *하지 않는* 것
docs/architecture/governance-preconditions.md:757:- ✅ ADR-011 §2.3 권위 확정 (2026-05-06, 충족됨)
docs/architecture/governance-preconditions.md:789:- ✅ ADR-008 / ADR-011 cross-reference 갱신 (별도 PR)
docs/architecture/governance-preconditions.md:806:| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위) |
docs/architecture/governance-preconditions.md:808:| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 |
docs/architecture/governance-preconditions.md:809:| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) 4조건 → 본 §3~§8 Exit 기준 (a)~(e) 패턴 답습 |
docs/architecture/governance-preconditions.md:835:2. **R-7 SOP §0 핵심 선언 답습**: 각 GP Exit 기준 (a)~(e) 5조건은 ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e) 패턴 답습 — 본 초안이 새 권위 구조 트리거하지 않음.
docs/architecture/governance-preconditions.md:836:3. **ADR-011 §2.4 T1/T2/T3 답습**: 본 §3~§8 산출 후보는 모두 사용자 명시 결정 (T2) 후 진입. §9 메타 안전장치는 T3 변경 절차 명시.
docs/phase0/jarvis-mvp1-v1-poc-phase2-entry-brief.md:202:| (D) | Phase 2 결과 후 → Phase 3 진입 (C-e llama.cpp 빌드·측정) | 별도 brief + 사용자 명시 (M3·M4 §5.3) |
docs/phase0/jarvis-mvp1-v1-poc-phase2-entry-brief.md:380:| (J) | brief v2 commit 후 → **Phase 3 entry brief** (C-e llama.cpp 빌드·측정) — (iii)(iv) 미해소 입력 | M3·M4 §5.3 답습 |
docs/phase0/mvp1-r-s1-b2-massive-correction-evidence.md:47:| `ADR-008 §A.2 R1-2` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011` |
docs/phase0/mvp1-r-s1-b2-massive-correction-evidence.md:48:| `ADR-008 §2.6.4 R1-2` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011` |
docs/phase0/mvp1-r-s1-b2-massive-correction-evidence.md:55:  -e 's/ADR-008 §A\.2 R1-2/ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011/g' \
docs/phase0/mvp1-r-s1-b2-massive-correction-evidence.md:56:  -e 's/ADR-008 §2\.6\.4 R1-2/ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011/g' \
docs/phase0/mvp1-r-s1-b2-massive-correction-evidence.md:120:- ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0
docs/architecture/hermes-adoption-design-v3.md:12:**상위 결정**: ADR-008 (Option B), ADR-011 (수단/목적 분리 — R-3 모법)
docs/architecture/hermes-adoption-design-v3.md:14:**관련 ADR**: ADR-009 (자체 Adapter v2.0 진입조건), ADR-010 (SQLCipher Vault HSM 키 관리), ADR-011 (수단/목적 분리)
docs/architecture/hermes-adoption-design-v3.md:31:6. 동시 갱신 ADR 매트릭스 (ADR-008 본문 / ADR-009 / ADR-010 / ADR-011 cross-reference 후보)
docs/architecture/hermes-adoption-design-v3.md:38:3. ❌ ADR-008 본문 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 (별도 PR 묶음으로 처리)
docs/architecture/hermes-adoption-design-v3.md:41:6. ❌ 자동 정책 변경 (ADR-011 §2.4 T3 — 절대 금지)
docs/architecture/hermes-adoption-design-v3.md:73:### 1.2 G1 단일 게이트 → G1a / G1b 분리 (ADR-011 §2.2 인용)
docs/architecture/hermes-adoption-design-v3.md:79:[v3 — ADR-011 §2.2 권위]
docs/architecture/hermes-adoption-design-v3.md:96:| Hermes native redaction | 로그 / LLM 송신 / 도구 출력 | Primary (DB INSERT 경로 가정) | **보조** (DB 차단 책임 없음, ADR-011 §2.3 운영 함의 #2) |
docs/architecture/hermes-adoption-design-v3.md:98:| canary 재검증 트리거 (R-5 설계, T13 강화) | CI / nightly / Hermes 업그레이드 / catalog 갱신 / dev local | (가정 외) | **운영 메커니즘** (ADR-011 §2.4 T1 자동) |
docs/architecture/hermes-adoption-design-v3.md:99:| CI/nightly 자동 회귀 (R-6 workflow) | GitHub Actions | (가정 외) | **자동 회귀 검증 경로** (ADR-011 §2.1 (d) 충족) |
docs/architecture/hermes-adoption-design-v3.md:105:| # | 산출 | 본 v3 인용 위치 | ADR-011 충족 |
docs/architecture/hermes-adoption-design-v3.md:108:| R-3 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` + ADR-008 부록 B Amendment | §2 (Hermes PMO 구조 권위) + §3 (게이트 정의 권위) | (R-3 = ADR-011 자체) |
docs/architecture/hermes-adoption-design-v3.md:111:| R-5 | `docs/architecture/canary-recheck-design.md` | §3.3 G1b — 운영 메커니즘 + ADR-011 §2.4 T1/T2/T3 정책 매트릭스 | §2.4 자동 학습 vs 정책 변경 분리 |
docs/architecture/hermes-adoption-design-v3.md:171:| 1 | Constitution / ADR / SDD 본문 자동 작성 또는 수정 | ADR-011 §2.4 T3 + system-identity-prequel §3.3 #1 |
docs/architecture/hermes-adoption-design-v3.md:172:| 2 | Harness Gate 정의 자체의 변경 | ADR-011 §2.4 T3 |
docs/architecture/hermes-adoption-design-v3.md:173:| 3 | Tools 검증 결과를 우회하여 PASS 처리 | ADR-011 §2.3 권위 위계 (Tools > Hermes 출력) |
docs/architecture/hermes-adoption-design-v3.md:174:| 4 | DB INSERT 경로 차단의 *유일한* 메커니즘으로 작동 | ADR-011 §2.3 운영 함의 #2 (Hermes native redaction은 보조) |
docs/architecture/hermes-adoption-design-v3.md:176:| 6 | 자체 권위 상승을 트리거하는 결정 | ADR-011 §2.4 T3 + system-identity-prequel §3 권위 위계 |
docs/architecture/hermes-adoption-design-v3.md:178:### 2.2 권위 위계 (ADR-011 §2.3 영구 권위 인용)
docs/architecture/hermes-adoption-design-v3.md:189:본 위계는 **ADR-011 §2.3** 영구 권위로 승격되어 있으며, system-identity-prequel.md archived 후에도 보존된다. 본 v3는 위 위계를 *전제*로 한다.
docs/architecture/hermes-adoption-design-v3.md:191:### 2.3 운영 함의 (ADR-011 §2.3 5항목 인용)
docs/architecture/hermes-adoption-design-v3.md:193:본 v3는 ADR-011 §2.3 5항목을 P2 본문 운영 권위로 흡수한다:
docs/architecture/hermes-adoption-design-v3.md:199:5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.1.2 #1~#6 + ADR-011 §2.4 결합 → §3.4 G3
docs/architecture/hermes-adoption-design-v3.md:267:| **G3** | "Hermes ≠ root of trust" 운영 구현 | 🟡 **ADR-011 §2.3 권위 확정 / 운영 구현 미작성** | §5 |
docs/architecture/hermes-adoption-design-v3.md:276:| **G1a** | Hermes native redaction → DB | ❌ **FAIL 확정 (영구 폐기)** | ADR-011 §2.2 권위 |
docs/architecture/hermes-adoption-design-v3.md:323:**상태**: ADR-011 §2.2 권위로 **영구 폐기**. 이 경로로 헌법 8조 충족 시도 금지.
docs/architecture/hermes-adoption-design-v3.md:336:| R-3 | `ADR-011` + ADR-008 부록 B Amendment | 권위 확정 (수단/목적 분리) |
docs/architecture/hermes-adoption-design-v3.md:337:| R-4 | `docs/architecture/redaction-pattern-equivalence.md` | pattern equivalence + gap 식별 + 보충 권고 (ADR-011 §2.1 (a) 충족) |
docs/architecture/hermes-adoption-design-v3.md:338:| R-4.1 | `docker/r4-1-poc/` + `docs/phase0/r4-1-trigger-extension-evidence.md` | Tier-1 42 trigger UDF 격리 PoC PASS (ADR-011 §2.1 (b) 충족) |
docs/architecture/hermes-adoption-design-v3.md:340:| R-6 | `.github/workflows/r2-canary.yml` + actual run `25482284523` | 24초 PASS, verdict=PASS, 42/42 BLOCK, leak 0, ROLLBACK 미발화 (ADR-011 §2.1 (d) 충족) |
docs/architecture/hermes-adoption-design-v3.md:354:G1a = FAIL (영구 폐기)                                       ✅ ADR-011 §2.2 권위
docs/architecture/hermes-adoption-design-v3.md:387:| 1 | DB 평문 secret 저장 차단 | 헌법 8조 위반 | SQLCipher trigger (G1b) | ADR-011 §2.1 |
docs/architecture/hermes-adoption-design-v3.md:389:| 3 | Constitution / ADR / SDD 본문 자동 변경 차단 | T3 위반 | filesystem read-only + audit log + Hermes write 차단 | ADR-011 §2.4 + system-identity-prequel §3.3 |
docs/architecture/hermes-adoption-design-v3.md:392:| 6 | 자동 정책 변경 차단 (T3) | T3 위반 | Layer 1~2 hook (설정 파일 변경 감지) + CI/nightly 강제 | ADR-011 §2.4 + R-6 |
docs/architecture/hermes-adoption-design-v3.md:415:(a)~(d)는 ADR-011 §2.1 (a)~(d) 4조건 패턴을 G2에 적용한 것. (e)는 G1b 승격 절차 답습.
docs/architecture/hermes-adoption-design-v3.md:427:- ADR-011: §2 본문은 변경 없음, §8 후속 작업에 G2 산출 등록
docs/architecture/hermes-adoption-design-v3.md:436:**G3**: ADR-011 §2.3 권위 위계 + 5 운영 함의가 *운영 가능한 메커니즘*으로 구현된 상태. ADR 권위는 이미 확정(2026-05-06), 운영 구현은 미작성.
docs/architecture/hermes-adoption-design-v3.md:438:**근거**: ADR-011 §2.3 (영구 권위) + system-identity-prequel §3.3 (4 강제 메커니즘 후보).
docs/architecture/hermes-adoption-design-v3.md:442:| # | ADR-011 §2.3 운영 함의 | 운영 메커니즘 후보 | 검증 방식 |
docs/architecture/hermes-adoption-design-v3.md:450:### 5.3 system-identity-prequel §3.3 4 강제 메커니즘 흡수
docs/architecture/hermes-adoption-design-v3.md:459:§5.2의 5 메커니즘 + 본 §5.3의 4 메커니즘은 G3 작성 시 통합 매트릭스로 정리. 본 초안은 *후보 식별*까지만.
docs/architecture/hermes-adoption-design-v3.md:465:- ✅ ADR-011 §2.3 권위 확정 (2026-05-06, 충족됨)
docs/architecture/hermes-adoption-design-v3.md:499:- ADR-011: §2.3 본문 변경 없음, §8.5 후속 작업에 G3 산출 등록
docs/architecture/hermes-adoption-design-v3.md:556:- T2 등록 (사용자 승인 강제, ADR-011 §2.4)
docs/architecture/hermes-adoption-design-v3.md:616:| **ADR-011** | §2.2 G1b 정식 충족 조건 표 → R-7 SOP §4.2 PASS 갱신 결과 cross-reference 추가 | §3.3 | 별도 PR |
docs/architecture/hermes-adoption-design-v3.md:617:| **ADR-011** | §8.5 후속 작업 → G2 / G3 / G4 산출 등록 + ADR-012 + ADR-009 C-N + G2 §1.2.6 P10 cross-reference | §4.4, §5.6, §6.6 + §3.1.3 Δ-1~Δ-7 | 별도 PR |
docs/architecture/hermes-adoption-design-v3.md:665:- ❌ ADR-008 / ADR-010 / ADR-011 본문 자동 갱신 (cross-reference 만 가능, 본문 변경 = 본 v3 정식 채택 *후* 별도 PR — §7 답습)
docs/architecture/hermes-adoption-design-v3.md:682:| 5 | ADR-011 본문 갱신 (§8.5 후속 작업 answer) | 별도 PR (단축) | §7 답습 |
docs/architecture/hermes-adoption-design-v3.md:710:| 2 | **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위), system-identity-prequel §3 → ADR 승격, **ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목, 2026-05-09 후속 3 PR-2)**, **ADR-009 §2.3 (Hermes PMO ↔ provider 분리, 2026-05-09 후속 4 C-N)**, G3 §1.3 + §5 (Evidence decision principle), G3 §2.5 #11 / §4.5 / §2.2 #20 (Hermes-originated commit auto-reject) | 5 layer (ADR-011 권위 + ADR-012 변조 매트릭스 + ADR-009 PMO-provider 분리 + G3 evidence + G3 hook) |
docs/architecture/hermes-adoption-design-v3.md:712:| 4 | **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 (T1/T2/T3 분류), 본 v3 §0.2 #6 + §11 변경 절차, **ADR-012 §원칙 9 (prev_hash 검증 실패 = 즉시 BLOCK, 자동 복구 / 자동 revert 금지)**, ADR-009 §2.3 (Hermes provider 소유 = T3 영역) | T1 (자동 학습 OK) / T2 (사용자 승인 필수) / T3 (자동 변경 절대 금지) 3 tier |
docs/architecture/hermes-adoption-design-v3.md:713:| 5 | **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e), **ADR-012 §4 (a)~(e) 5조건 답습**, 본 v3 §3.3 / §4.3 / §5.4 / §6.4 의 exit 기준 패턴 | (a) 동등 이상 + (b) 격리 PoC + (c) ADR 권위 + (d) 자동 회귀 + (e) 합의 APPROVE — 5 조건 모두 본 v3 4 게이트 Exit 기준 답습 |
docs/architecture/hermes-adoption-design-v3.md:719:> Archiving P2 v2 (`hermes-adoption-design.md`) or `system-identity-prequel.md` does not weaken, supersede, or delete the five permanent constraints listed in §10.1. If any archived document contains stronger wording, the stronger constraint remains preserved through ADR-011, ADR-012, ADR-009 (C-N), and this section §10.1.
docs/architecture/hermes-adoption-design-v3.md:721:> P2 v2 또는 system-identity-prequel.md 의 archive 처리는 §10.1 의 5 영구 핵심 제약을 *약화 / 폐기 / 우회* 시키지 않는다. archive 대상 문서에 더 강한 문구가 있다면, 더 강한 제약은 ADR-011 / ADR-012 / ADR-009 (C-N) / 본 §10.1 을 통해 영구 보존된다. **5 영구 핵심 제약 보호 = HIGH 5/5 (조건부 — 본 §10.1 + §10.2 흡수 후)**.
docs/architecture/hermes-adoption-design-v3.md:770:3. **ADR-011 §2.4 T1/T2/T3 답습**: 본 v3 §4 / §5 / §6 의 산출 후보는 모두 사용자 명시 결정(T2) 후 진입.
docs/architecture/hermes-adoption-design-v3.md:771:4. **수단/목적 분리 원칙 답습**: §4.3 / §5.4 / §6.4 의 Exit 기준 (a)~(e) 는 ADR-011 §2.1 (a)~(d) 4조건 패턴 답습.
docs/architecture/hermes-adoption-design-v3.md:788:- ❌ 추가 정책 변경 자동 (ADR-011 §2.4 T3)
docs/sessions/SESSION_2026-05-22.md:23:- **⭐⭐ 비례성 (사용자 제기)**: solo·single-host·**본인용 개인 개발 툴**에 하드웨어 서명·touch-per-commit·서명 사용자는 실 위협 모델(에이전트 실수·공급망 = review/test/git로 충분)에 **비례 초과**. "내 머신에 root 잡은 공격자"는 이미 게임 끝 → 서명 격리 한계이득 0. **means/ends(ADR-011): 하드웨어 서명=MEANS, 현 비용>이득.**
docs/sessions/SESSION_2026-05-09.md:141:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 + ADR-014 신규 자동
docs/sessions/SESSION_2026-05-09.md:191:| Hermes ≠ root of trust | ADR-011 §2.3 (영구 권위) | G4 검토 §1.3 + §5.1 (G3 §4 자기참조 차단의 적용 대상) |
docs/sessions/SESSION_2026-05-09.md:193:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | G4 검토 §2.5 (Promotion T2 강제) + §2.6 (4 금지 T3 영역) |
docs/sessions/SESSION_2026-05-09.md:194:| 수단/목적 분리 원칙 | ADR-011 §2.1 (a)~(d) | G4 §8.1 (a)~(e) 패턴 답습 + G4 검토 §2.10 |
docs/sessions/SESSION_2026-05-09.md:269:| Hermes ≠ root of trust | ADR-011 §2.3 (영구 권위) | 합의 보고서 §0.3 + §1.5 + §6 (G3 정식 PASS 자체가 본 원칙의 운영 구현 승인) |
docs/sessions/SESSION_2026-05-09.md:271:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | 합의 보고서 §9.6 (T3 위반 0건 명시) |
docs/sessions/SESSION_2026-05-09.md:272:| 수단/목적 분리 원칙 | ADR-011 §2.1 (a)~(d) | 합의 보고서 §6 (각 GP/§ Exit (a)~(e) 5조건 패턴 답습) |
docs/sessions/SESSION_2026-05-09.md:352:| C-C | Evidence Ledger 보호 강화 (11 필드 + hash chain/signed commit) | (3) 신규 ADR-012 + (1) G3 §1.3/§5.3 보강 | 신규 ADR-012 발행 (PR-2) | C-G |
docs/sessions/SESSION_2026-05-09.md:512:| Hermes ≠ root of trust | ADR-011 §2.3 영구 권위 | ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목 — Gap-17) + 원칙 3 + 원칙 7 + ADR-011 §7.3 답습 |
docs/sessions/SESSION_2026-05-09.md:514:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | ADR-012 §2.7 (BLOCK + manual, 자동 revert 금지) + §2.12 (Hermes 변조 차단) + §2.10 (Migration 자동 revert 금지) |
docs/sessions/SESSION_2026-05-09.md:515:| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + (e) | ADR-012 §4 (a)~(e) 5조건 답습 |
docs/sessions/SESSION_2026-05-09.md:578:| 2 | Hermes PMO ↔ provider 분리 | §2.3 신설 (7 영역 권한 매트릭스, ADR-011 §2.3 + ADR-008 차단조건 #4 + ADR-012 §원칙 6 + 헌법 5조 답습) |
docs/sessions/SESSION_2026-05-09.md:648:| Hermes ≠ root of trust | ADR-011 §2.3 영구 권위 | ADR-009 §2.3 (Hermes PMO ↔ provider 분리, 격상 후에도 영구 유지) |
docs/sessions/SESSION_2026-05-09.md:650:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | ADR-009 §2.3 (Hermes provider 소유 = T3 영역 + Hermes-originated commit auto-reject 답습) |
docs/sessions/SESSION_2026-05-09.md:651:| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + (e) | ADR-009 §5.1 (자체 Adapter v2.0 진입 = *수단 변경*, *목적 보존* — Provider Liquidity 비협상 5조건 답습) |
docs/sessions/SESSION_2026-05-09.md:686:| 2 | §1.2.5 P10 deferred row 갱신 | "deferred (GPT 조건 7 + Claude C-4)" → "✅ 정식 등록 완료 (§1.2.6 답습, 2026-05-09 후속 5)" + 정식 등록 시점 = "✅ 2026-05-09 후속 5 — PR-2 ADR-012 발행 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록" + §1.2.5.3 *하지 않는* 것에 "P10 은 §1.2.6 답습 정식 등록 완료" 명시 |
docs/sessions/SESSION_2026-05-09.md:750:| Hermes ≠ root of trust | ADR-011 §2.3 영구 권위 | G2 §1.2.6.2 Hermes 변조 차단 매트릭스 4항목 답습 (ADR-012 §2.12 cross-reference) |
docs/sessions/SESSION_2026-05-09.md:752:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | §1.2.6.4 4 풀 3+1 승격 트리거 검증 #4 (T3 변경의 권위 내부 분류 + 자동 정책 변경 발생 0건) |
docs/sessions/SESSION_2026-05-09.md:753:| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + (e) | §1.2.6.2 enforcement layer = *수단*, Evidence integrity = *목적* (ADR-011 답습) |
docs/sessions/SESSION_2026-05-09.md:801:### 15.3 P2 v3 본문 갱신 8 영역 (본 합의 §5.2 답습)
docs/sessions/SESSION_2026-05-09.md:822:| 5 | ADR-011 본문 갱신 (§8.5 후속 작업) | 별도 PR (단축) |
docs/sessions/SESSION_2026-05-09.md:871:| Hermes ≠ root of trust | ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 §2.3 + G3 §1.3/§5 | P2 v3 §10.1 #2 + §2 Non-Activation Clause + §2.3 운영 함의 5항목 + §11.1 인간 리뷰 |
docs/sessions/SESSION_2026-05-09.md:873:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 + ADR-012 §원칙 9 + ADR-009 §2.3 | P2 v3 §10.1 #4 + §11 변경 절차 (T3 = 풀 3+1 + ADR Amendment) + §2.1.2 Hermes 가 *하지 않는* 것 6항목 |
docs/sessions/SESSION_2026-05-09.md:874:| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + ADR-012 §4 (a)~(e) | P2 v3 §10.1 #5 + §3.3/§4.3/§5.4/§6.4 Exit (a)~(e) 5조건 |
docs/sessions/SESSION_2026-05-09.md:918:| 3 | P2 v2 폐기 가정 명확 표시 (5 권위 위치) | ✅ PASS (ADR-011 §1.1 / §2.2 / §65 + ADR-008 부록 B + P2 v3 §1.1 / §3.2 / §8) |
docs/sessions/SESSION_2026-05-09.md:997:| Hermes ≠ root of trust | ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 §2.3 + G3 §1.3/§5 | P2 v2 archive 영향 0건 |
docs/sessions/SESSION_2026-05-09.md:999:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 + ADR-012 §원칙 9 | P2 v2 archive = T3 변경 영역 (문서 상태) — 단축 합의 + ADR-012 §605 권위 *내부* 작업, 자동 변경 0건 |
docs/sessions/SESSION_2026-05-09.md:1000:| 수단/목적 분리 | ADR-011 §2.1 + ADR-012 §4 | P2 v2 archive = *수단* (옵션 A 헤더 갱신) / *목적* (P2 v3 권위 우선 + 5 영구 제약 보존) — (a)~(e) 5조건 답습 |
docs/sessions/SESSION_2026-05-09.md:1079:- §3 권위 위계 → ADR-011 §2.3 영구 권위 승격
docs/sessions/SESSION_2026-05-09.md:1082:- §5 T1/T2/T3 → ADR-011 §2.4 영구 권위 승격
docs/sessions/SESSION_2026-05-09.md:1090:- §9 Phase 0 R-1 → ADR-011 §1.1 + §2.2 + P2 v3 §1.1 + §3.2
docs/sessions/SESSION_2026-05-09.md:1104:- archive 합의 권위 cross-reference + 후속 권위 명시 (P2 v3 / ADR-011 / ADR-012 / ADR-009 C-N)
docs/sessions/SESSION_2026-05-09.md:1151:| Hermes ≠ root of trust | ADR-011 §2.3 (영구 권위 승격, "prequel 폐기 후에도 보존" 직접 명시) + ADR-012 §2.12 + ADR-009 §2.3 + G3 §1.3/§5 | prequel archive 영향 0건 (ADR-011 §2.3 영구 보존) |
docs/sessions/SESSION_2026-05-09.md:1153:| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 (영구 권위 승격, "prequel §6의 3-tier 선언을 ADR 권위로 승격") + ADR-012 §원칙 9 | prequel archive 영향 0건 (ADR-011 §2.4 영구 보존) |
docs/sessions/SESSION_2026-05-09.md:1154:| 수단/목적 분리 | ADR-011 §2.1 + ADR-012 §4 (a)~(e) | prequel 무관 |
docs/sessions/SESSION_2026-05-09.md:1183:> **결정 1 (작업)**: ADR-008 / ADR-010 / ADR-011 본문 갱신 PR 묶음 *범위 결정* (본문 수정 X)
docs/sessions/SESSION_2026-05-09.md:1195:| 1 | ADR-008 갱신 영역 | ✅ A1~A9 (9 cross-reference 갱신 — P2 v2 Archived / P2 v3 Adopted / ADR-009 C-N / ADR-011 / ADR-012 / G2/G3/G4 / 차단조건 #2 #4 / 부록 B §B.6) |
docs/sessions/SESSION_2026-05-09.md:1197:| 3 | ADR-011 갱신 영역 | ✅ A14~A25 (12 cross-reference 갱신 — prequel Archived / P2 v2 Archived / P2 v3 Adopted / R-4~R-7 ✅ 완료 표기 / G1b PASS / G2/G3/G4 / ADR-012 / ADR-009 C-N / G2 §1.2.6 P10 / P2 v3 / Archive 후속 작업 등록) |
docs/sessions/SESSION_2026-05-09.md:1206:| 3 | ADR-011 수단/목적 분리 원칙 변경 | ❌ 0 (§2.1 / §2.2 / §2.3 / §2.4 모두 영구 권위 답습) |
docs/sessions/SESSION_2026-05-09.md:1218:- 옵션 3: ADR-008+010 단일 PR + ADR-011 별도 PR — 분기 비효율
docs/sessions/SESSION_2026-05-09.md:1297:- **A4** ADR-011 (수단/목적 분리 모법) cross-reference 추가 (현재 부록 B 만 명시)
docs/sessions/SESSION_2026-05-09.md:1313:#### 19.2.3 ADR-011 갱신 (A14~A25, 12 항목)
docs/sessions/SESSION_2026-05-09.md:1315:`docs/decisions/ADR-011-means-vs-ends-redaction.md` §8 관련 문서 영역 cross-reference 12 항목 갱신 (~50 줄 추가):
docs/sessions/SESSION_2026-05-09.md:1338:| ADR-011 | §2.1 수단/목적 분리 / §2.2 G1a/G1b / §2.3 Hermes ≠ root of trust / §2.4 T1/T2/T3 | ❌ 0건 |
docs/sessions/SESSION_2026-05-09.md:1350:| 3 | ADR-011 수단/목적 분리 원칙 변경 | ❌ 0 |
docs/sessions/SESSION_2026-05-09.md:1375:   - ADR 본문 갱신 (~95 줄 = ADR-008 ~30 + ADR-010 ~15 + ADR-011 ~50)
docs/sessions/SESSION_2026-05-09.md:1394:- Hermes ≠ root of trust: ADR-008 §관련 문서 → ADR-011 + ADR-012 cross-reference 추가 + ADR-011 §8.5 ADR-012 §2.12 (변조 차단 매트릭스) 답습 등록
docs/sessions/SESSION_2026-05-09.md:1395:- 메타포 강제 금지: ADR-011 §8.1 prequel §7 archive 후 권위 보존 명시
docs/sessions/SESSION_2026-05-09.md:1396:- T3 자동 정책 변경 금지: ADR-011 §8.5 ADR-012 §원칙 9 등록
docs/sessions/SESSION_2026-05-09.md:1397:- 수단/목적 분리: ADR-011 §8.5 (a)~(d) + (e) 5조건 패턴 답습 명시 (G2/G3/G4 + ADR-012 + ADR-009 C-N + G2 §1.2.6 P10 + P2 v3 + Archive 모두)
docs/sessions/SESSION_2026-05-09.md:1438:- P2 v2 / system-identity-prequel Archived cross-reference (prequel §3 → ADR-011 §2.3 영구 승격 답습으로 archive 후 권위 보존)
docs/sessions/SESSION_2026-05-09.md:1439:- **ADR-011 §2.3 / §2.4 영구 권위 직접 명시** ("prequel 폐기 후에도 보존" 직접 인용)
docs/sessions/SESSION_2026-05-09.md:1460:| 4 | ADR-012 / ADR-009 / ADR-011 참조 충돌 | ❌ 0 (cross-reference 보강 = 권위 정합성 강화, 충돌 0건) |
docs/sessions/SESSION_2026-05-09.md:1499:cross-reference 갱신 = *권위 보강* 영역 — 5 영구 핵심 제약 약화 0건. ADR-009 C-N §5 (5-way Layer 1 모법) + ADR-012 §원칙 5/6/9 + ADR-011 §2.3/§2.4 영구 권위 + ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목) cross-reference 추가 = 보호 강화.
docs/sessions/SESSION_2026-05-09.md:1535:- 현 권위 출처 = **7 권위 layer 중첩 답습**: P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12
docs/sessions/SESSION_2026-05-09.md:1544:- **Implementation/Runtime PASS PoC 완료 *후* 발행 검토** — 현 시점 발행 = ADR-011 §2.1 (b) 격리 환경 PoC 실증 패턴 위반
docs/sessions/SESSION_2026-05-09.md:1670:| 7 | ADR-009 C-N / ADR-011 / ADR-012 / G2/G3/G4 cross-reference 보강 | ✅ §C.7 매트릭스 (12 권위) |
docs/sessions/SESSION_2026-05-09.md:1729:1. **G2 GP-2~GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수** (다음 진입점 후보 #1) — 각 별도 합의 (Implementation 영역, ADR-011 §2.1 (a)~(e) 5조건 답습)
docs/sessions/SESSION_2026-05-09.md:1730:2. **ADR-010 / ADR-011 후속 보강 필요 여부 확인** (다음 진입점 후보 #2)
docs/sessions/SESSION_2026-05-09.md:1755:## 23. 본 세션 후속 (14) — ADR-010 / ADR-011 후속 보강 필요 여부 검토 (2026-05-09 후속 14)
docs/sessions/SESSION_2026-05-09.md:1761:> **결정 1 (작업)**: ADR-010 / ADR-011 후속 보강 필요 여부 확인 (후보 #2)
docs/sessions/SESSION_2026-05-09.md:1762:> **결정 2 (이유)**: G2 GP-2~GP-6 / G3 / G4 Implementation/Runtime PASS 작업 진입 *전* ADR-010 / ADR-011 정렬 검증
docs/sessions/SESSION_2026-05-09.md:1766:> **결정 6 (사용자 명시 10 항목)**: ADR-010 5 항목 + ADR-011 5 항목
docs/sessions/SESSION_2026-05-09.md:1782:#### 23.2.2 ADR-011 5/5 항목 충족
docs/sessions/SESSION_2026-05-09.md:1787:| 2 | 권위 위계 P2 v2/prequel archive 이후 명확 | ✅ 후속 10 A14/A15 답습 (ADR-011 §2.3 영구 권위 승격 직접 명시) |
docs/sessions/SESSION_2026-05-09.md:1789:| 4 | Hermes PMO 격상 절차 ADR-011 원칙 연결 | ✅ ADR-008 부록 C §C.6 (8 권위 layer 답습) |
docs/sessions/SESSION_2026-05-09.md:1790:| 5 | 자동 정책 변경 금지 Implementation/Runtime 진입 *전* 강제 | ✅ 5 layer 다중 차단 매트릭스 명시 (ADR-011 §2.4 + ADR-012 §원칙 9 + ADR-009 §2.3 + ADR-012 §2.12 + G3 §2.5/§4.5/§2.2) |
docs/sessions/SESSION_2026-05-09.md:1797:| 2 | ADR-011 수단/목적 분리 원칙 변경 | ❌ 0 |
docs/sessions/SESSION_2026-05-09.md:1822:| ❌ **ADR-010 / ADR-011 본문 자동 수정** | **0** (사용자 명시 답습 — 검토만) |
docs/sessions/SESSION_2026-05-09.md:1832:2. **G2 GP-2 ~ GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수** (다음 진입점) — 각 별도 합의 (ADR-011 §2.1 (a)~(e) 5조건 + R-2/R-4.1 PoC 패턴 답습)
docs/sessions/SESSION_2026-05-09.md:1843:본 검토 = 보강 필요 여부 검토만 (본문 수정 X) — 5 영구 핵심 제약 약화 0건. ADR-010 + ADR-011 후속 10/13 cross-reference 갱신 + 5 layer 다중 차단 매트릭스 답습으로 권위 보강 강화 명시.
docs/sessions/SESSION_2026-05-09.md:1892:- **PASS 기준 통합 매트릭스**: ADR-011 §2.1 (a)~(e) 5조건 답습 + Rollback Trigger 9 항목 + Evidence Required 5 형식
docs/sessions/SESSION_2026-05-09.md:1901:| 3 | Implementation PASS 기준 완화 | ❌ 0 (강화 — ADR-011 §2.1 답습 + R-2/R-4.1 PoC 패턴) |
docs/sessions/SESSION_2026-05-09.md:1903:| 5 | ADR-011 §2.1 (a)~(e) 충돌 | ❌ 0 (직접 답습) |
docs/sessions/SESSION_2026-05-09.md:1912:   - roadmap 문서 (~600 줄, 17 항목 + 9 그룹 + 5 우선순위 기준 + ADR-011
docs/sessions/SESSION_2026-05-09.md:1944:본 roadmap = 권고 한정, 5 영구 핵심 제약 약화 0건. ADR-011 §2.1 (a)~(e) 5조건 답습 매트릭스 명시 + Rollback Trigger 9 항목 + Evidence Required 5 형식 = 권위 보강 강화.
docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md:6:> **상위 권위**: ADR-008 부록 C, ADR-009 C-N §2.3+§5, ADR-011 §2.1 (a)~(e)
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:22:- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:294:C-υ-44 답습 결정 영역 (Stage 4 entry brief 합의 §5.3 답습) = **3 영역 동시 발효**:
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:385:### 5.3 신규 actual run trigger 검증 매트릭스
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:555:| C-υ-19 (Actual run trigger event 권고) | ✅ §5.3 답습 (W-4 영역 외 명시) |
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:579:| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | ❌ **비권고** — W-1 단독 영역 + paths-only ≤ 15 lines 한정 → T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 |
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:610:| ADR-011 §2.4 T2 영역 | 답습 한정 — 외부 LLM 의뢰 미필수 영역 |
docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md:745:| C-φ-11 | 신규 actual run trigger 0건 영구 답습 — 본 brief = local 한정 (W-4 영역 외) | §5.3 답습 |
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:9:> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e)
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:12:> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 6 풀 3+1 승격 trigger / 6 검증 / 8 금지 / 외부 의존 0건
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:71:| pre-commit hook 활성화 | T2 정책 영역 (ADR-011 §2.4) — 별도 합의 |
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:105:| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | ✅ | ✅ | ✅ |
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:311:| 2 | pre-commit hook 활성화 미진입 | T2 정책 영역 (ADR-011 §2.4) | 별도 합의 |
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:364:| 5 | ADR-009 / ADR-011 / llm-providers-design.md §9 와 충돌 | ❌ 미발화 | cross-reference 답습 |
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:387:| 2026-05-10 | 신규 작성 (DRAFT) | Group A 3차 진입 사양 — Layer 1c 모법 답습 (Group A 2차 합의 §5.5 #C-8 답습 의무). 사용자 명시 6 검증 / 6 trigger / 8 금지 / 9 fixture / 2 mode (url-endpoint + model-name) / Tier-1 catalog (URL 10 + model 19+) / extension allowlist (8 / 5) / stdlib 단독 채택. Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F + Group G 사양 형식 직접 답습. ADR-009 C-N §5 + llm-providers-design.md §9.3 + ADR-011 §2.1 답습 (변경 0건). Reviewer-only 단축 합의 적격 (풀 3+1 trigger 0/6 발화). artifact path `group-a3-logs/` (Group F 후속 답습, leading dot 미사용). |
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:16:- ADR-011 §2.1 5조건 + 헌법 5조-2 (R-9 답습 영구)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:217:- 정정 권고 (별도 (R4-body) cycle 의무): "llama.cpp MoE 실측 — Qwen3-30B-A3B classical decode ~49.6 t/s / Qwen3-Next-80B SSM hybrid ~32.3 t/s, Ollama 동일 모델 decode ~14.7~15.3 t/s = ~3.24~3.38× llama.cpp 빠름. R4 원본 '~31 t/s' = (g) SSM hybrid model variant 정합"
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:227:- 단 **결정 *고정* 의무 = (k) 별도 cycle** (M3·M4 결정 *고정* cycle, ADR-011 §2.1 5조건 답습 영구 의무)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:257:### 5.3 4-way 통합 *분석* cycle vs (R4-body) 본문 정정 cycle 분리 명문 (R-rec-15 발효 우선 framing)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:462:| R-rec-15 (4-way 우선 framing) | 부분 | §5.3 |
docs/phase0/group-i-4axis-blocking-integration-brief.md:265:| ADR-011 §2.1 means/ends | §6·§9 |
docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md:3:> **본 brief = M3·M4 합의 §5.3 + 3+1 합의 (`d2d7bf9`) §6 권고 (A) 정공법 답습 + 3+1 합의 (`e76acc8`) BLOCKING 7 + 권고 25 + NOTE 11 반영.** brief 자체로 **빌드 실행 / 측정 / 합의 보고서 작성 / commit / push** 발생 0건. brief = **(i) 답습** + **(ii) C-e 정공법 실행 절차** + **(iii) 정직성 한계** 식별 한정.
docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md:10:**cycle 자격 근거**: 3+1 합의 `d2d7bf9` §6 BLOCKING 1 (결정 *고정* 자격 미충족, Phase 3 의무) + M3·M4 §5.3 C-e 명문 + 3+1 합의 `d2d7bf9` §3 P-1 L3·L4 Phase 3 후 재 합의 + Phase 2 §9.8 (iii)(iv) 미해소 + 3+1 합의 `e76acc8` brief v1.1 진입 자격 충족 (BLOCKING 7 verbatim 반영 후)
docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md:97:| `d2d7bf9` 5 (rollback trigger 명문) | 계층화 고정 시 ADR-011 §2.1 답습, Phase 3 결과 입력 후 |
docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md:386:- **출처**: 3+1 합의 (`d2d7bf9`) §6 권고 (A) + §3 P-1 계층화 부분 채택 + §5 G-1 hybrid 대안 carry-over + G-2 새 가설 #6 carry-over + BLOCKING 5 / 3+1 합의 (`e76acc8`) BLOCKING 7 (R-1~R-7) + 권고 25 + NOTE 11 / M3·M4 결정 합의 `9ddec1b` §5.3 / V-1 entry brief / Phase 1 결과 `2026-05-24-phase1-summary.json` / Phase 2 brief v2 `c66756b` §9 / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `feedback_provider_liquidity` / `project_jarvis_local_boss_direction` / ADR-011 §2.1 5조건 / 헌법 5조 (Provider Liquidity)
docs/phase0/mvp1-r-s1-framing-correction-brief.md:17:| 33번째 entry 합의 보고서 R-3 (multi-source 재기술) | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` §2.1 R-3 | "ADR-008 §A.2 R1-2 직접 인용 = source attribution 손상. 권고 정정: ADR-008 차단조건 #1 (SQLCipher) + #4 (어댑터 추상화) + #6 (Docker 격리 + egress 화이트리스트) + 부록 B + ADR-010 + ADR-009 + ADR-011 + roadmap-mvp1 §3 다층 답습으로 재기술" |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:34:| **변경 0건 의무** | ADR-008 본문 변경 0건 (R-MVP1-PASS-2 영구 금지 답습) / ADR-011 본문 0 / ADR-010 본문 0 / ADR-009 본문 0 / ADR-012 본문 0 / 헌법 본문 0 / 11 workflow 본문 0 / src 0 / tools 0 / docker 0 / (b1) 4 sub-cycle 본문 0 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:42:| 2 | ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 변경 | 0건 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:84:| `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리 + egress 화이트리스트) + 부록 B + ADR-010 (SQLCipher Vault) + ADR-011 (수단/목적 분리 §2.1 (a)~(d)) + 헌법 8조 #1` | `ADR-008 차단조건 #4 (어댑터 추상화) + 부록 B + ADR-009 (자체 Adapter v2.0) + ADR-011` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:92:| 1 | 106 (P3 row) | `ADR-008 §2.6.4 R1-2 + entrypoint stat 검증` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + ADR-010 + ADR-011 + entrypoint stat 검증` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:93:| 2 | 343 (GP-3 row) | `ADR-008 §2.6.4 R1-2 + R2-1 + 헌법 8조 #1` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:96:| 5 | 508 ((c) cell) | `ADR-008 §2.6.4 R1-2 + 헌법 8조 #1 + 본 §5` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:103:| 1 | 12 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 (저장 경로 secret 보호 권위)` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 권위, 35번째 entry R-S1 정정 답습)` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:104:| 2 | 84 | `Hermes upstream 변경 / 외부 LLM 자동 호출 \| ❌ (ADR-008 §2.6.2 R2-1 답습)` | `Hermes upstream 변경 / 외부 LLM 자동 호출 \| ❌ (ADR-008 차단조건 #6 답습 + ADR-011 답습)` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:138:| **D-2** | 정정 형태 | (A) multi-source 재기술 (R-3 답습) / (B) 단순 인용 정정 (governance-preconditions 자체 R1-2 정의로 변환) | **(A) multi-source 재기술** — 33번째 entry R-3 BLOCKING 답습. ADR-008 본문 실 권위 (차단조건 #1/#4/#6 + 부록 B) + ADR-010/ADR-011/ADR-009 multi-source 정확 attribution |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:156:| **풀 3+1 승격 trigger** | 5/5 발화 0건 (① 새 권위 결정 0 / ② Tier-2/3 자동 확장 0 / ③ PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 — cross-reference 정정 한정 / ⑤ ADR-011 5조건 자동 충족 선언 0) |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:14:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 (T1/T2/T3 3-tier 분류)
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:15:- ADR-011 §2.1 (a)~(e) 5조건 패턴
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:56:- ❌ **ADR 본문 자동 갱신 0건** (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:125:| **`.pre-commit-config.yaml` 본문 정의** | **T2** (정책 영역, ADR-011 §2.4 답습) | ✅ **본 brief 영역** | 사용자 명시 1 (PC-4 T2 sub 한정 검토) |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:167:| T2 영역 = 단축 합의 적격 (사용자 명시 결정) | ADR-011 §2.4 + mvp1.md §4.7.3 답습 |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:295:| (α) Backlog #1 단독 진입 (GP-3 hook 한정) | **단축 합의 + 사용자 명시 결정** | T2 정책 영역 한정 + Backlog #1 deepening brief §2.3.4 권고 답습 | mvp1.md §4.7.3 + ADR-011 §2.4 답습 |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:343:### 5.3 Evidence 기준 답습 (mvp1.md §3.6.1 + ADR-011 §2.1 (a)~(e) 답습)
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:351:| (c) ADR / SDD 권위 명시 | mvp1.md §4.3 + §5.5.1 / §5.5.2 + ADR-011 §2.4 + 본 brief 답습 | ✅ T2 sub 발효 시 |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:399:| 16 | ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경) | 0건 | cross-reference 답습 한정 |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:470:| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ (T2 sub 한정 + T3 sub 자동 진입 0건 명시) |
docs/phase0/day1-environment-and-fact-check.md:172:### 5.3 우회 가능성
docs/phase0/day1-environment-and-fact-check.md:256:**옵션 B — 즉시 §3.4 폴백 검토 (ADR-011 작성)**
docs/phase0/day1-environment-and-fact-check.md:278:1. 즉시 §3.4 폴백 → ADR-011 작성 (P2-N1 FAIL 명시)
docs/phase0/day1-environment-and-fact-check.md:412:- 다음: §3.4 폴백 → ADR-011 작성 → Option A (LiteLLM 우선) 또는 C-대안2 (Claude Code 메모리 + LiteLLM)
docs/phase0/mvp1-r-s1-b2-others-correction-evidence.md:42:| 11~19 | `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md` | 14 / 40 / 204 / 207 / 226 / 230 / 279 / 280 / 428 (총 9 위치, 10 substring 中 line 14 양쪽 multi-form 1개) | `ADR-008 §A.2 R1-2` → 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 / `ADR-008 §2.6.2 R2-1` → 차단조건 #6 + 부록 B (Edit replace_all 적용) |
docs/phase0/mvp1-r-s1-b2-others-correction-evidence.md:95:- ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 0
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:5:> 본 brief 의 어떤 §도 그 자체로 (i) **실제 T3 영역 진입**, (ii) **branch protection rule 변경** (CODEOWNERS / required check / commit signing 등), (iii) **dev 환경 강제** (`pre-commit install` 의무화 / 개발자 환경 정책), (iv) **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod 강제 / inotify 본문 흡수), (v) **Vault HSM 구현** (실 Vault 클라이언트 / 실 HSM 환경 / ADR-010 본문 변경), (vi) **Operational Readiness PASS (Layer E) 선언**, (vii) **Hermes PMO 격상 (Layer F) 선언**, (viii) Tier-2 / Tier-3 catalog *본문 확장* (URL 10 → 20+ / Model 19 → 50+ / R-4.1 42 catalog → 확장), (ix) 풀 3+1 합의 보고서 *작성* / commit / push, (x) 외부 LLM *자동 호출*, (xi) 실 API key / provider SDK / 외부 API 호출, (xii) ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012), (xiii) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (xiv) Layer D 합의 보고서 (`210c98f`) 본문 변경, (xv) §5.5 9 sub-수단 본문 채택 변경, (xvi) Backlog #1 / #2 / #4 / #6 / #7 자동 진입 을 발생시키지 않는다.
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:17:- ADR-011 §2.4 T3 영역 분리 (정책 / branch protection / Vault HSM / Tier-2/3 catalog 확장 = T3 영역 답습)
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:18:- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (entrypoint stat) + §2.6.2 R2-1 (docker secret) + R-4 catalog (R-4.1 Tier-1 42 patterns)
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:68:| (추가) | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:108:| **(3) PC-4 T3 sub** (`pre-commit install` 의무화 + dev 환경 강제) | §4.3 row PC-4 + §4.4.2 권고 (PC-4 MVP-1 1.5차 보강 영역) + ADR-011 §2.4 (dev 환경 강제 = T3) | dev 환경 정책 / `default_install_hook_types` / `fail_fast` (T3) | §2.3 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:109:| **(4) C-5b ST-1** (Hermes upstream Dockerfile entrypoint stat chmod 600 강제) | §3.3 row ST-1 + §3.5 R-MVP1-G3-7 (Hermes upstream Dockerfile 변경 = 풀 3+1 + Hermes upstream PR 검토) + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 답습 | Hermes upstream Dockerfile (T3) — repo 책무 경계 변경 | §2.4 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:218:| mvp1.md §4.3.1 PC-1 row | "pre-commit framework (`.pre-commit-config.yaml` + `pre-commit install`) — dev 환경 자동 설치 + framework 도입 + dev 환경 강제 — T2 (정책 영역, ADR-011 §2.4 답습)" |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:220:| ADR-011 §2.4 답습 | "dev 환경 강제 정책 = T3 영역" |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:227:| dev 환경 *정책* 변경 (`pre-commit install` 의무화) | ✅ HIGH (T3 — ADR-011 §2.4 답습) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:257:| mvp1.md §3.3.1 row ST-1 | "Hermes Dockerfile entrypoint stat 검증 (chmod 600 강제) — 컨테이너 시작 시 — ✅ Hermes upstream Dockerfile 수정 필요 — 비용 低 — ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 답습" |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:260:| ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 답습 | "entrypoint stat 검증 (chmod 600 강제) — Hermes upstream Dockerfile 본문 영역" |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:315:#### 2.5.3 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:340:| ADR-011 §2.4 답습 | "Tier-2/3 catalog 확장 = T3 영역" |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:390:| (3) PC-4 T3 sub | ⚠️ MEDIUM (AR-3 통합 시) | ❌ | ✅ HIGH (T3) | ❌ | ❌ | ❌ | (ADR-011 cross-reference) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:391:| (4) C-5b ST-1 | ❌ | ❌ | ❌ | ✅ HIGH (T3) | ⚠️ MEDIUM (file perm) | ❌ | (ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 cross-reference) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:393:| (6) Tier-2/3 자동 확장 일반 | ❌ | ✅ HIGH (T3) | ❌ | ❌ | ❌ | ❌ | (ADR-011 §2.4 cross-reference) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:460:| **(가) 풀 3+1 합의 + 외부 LLM 1+ cross-vendor blind + 사용자 명시** | ✅ **권고** | (i) 6 sub-영역 *모두 T3 영역* 의무 발화 — ADR-011 §2.4 답습 / (ii) R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 모두 풀 3+1 + 외부 LLM 1+ 답습 / (iii) Group α / β / γ 모두 T3 영역 진입 = 풀 3+1 의무 / (iv) Layer B `f40423f` Backlog #3 T3 영역 분리 명시 답습 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:495:| Agent B | 보안 (T3 정책 변경 = 책무 경계 변경 / fork PR 보안 / `pull_request_target` 위험 / commit signing key 관리 / `--no-verify` 우회 가능성 잔존) + 엣지케이스 (개발자 우회 / external contributor 정책 / hook stage 충돌) + 문서 정합성 (mvp1.md §4.4.2 + §4.6 + ADR-011 §2.4 답습 정합) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:498:### 5.3 Group β (T-5 (β) + Tier-2/3 일반) — Agent 관점 분배
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:511:| Agent B | 보안 (Hermes ≠ root of trust 보존 검증 / Vault HSM 보안 평가 / HSM key 관리 / Vault transit / Vault audit log 통합) + 엣지케이스 (Hermes upstream maintainer 거부 / Vault inaccessible 시 fallback / HSM SPOF) + 문서 정합성 (ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + ADR-010 §2 + ADR-011 §2.4 + 5 영구 핵심 제약 #1 답습) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:524:| ADR-011 §2.1 (a)~(e) 5 조건 발화 / 미발화 평가 | ✅ 의무 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:535:본 brief 6 sub-영역 *모두* = T3 영역 + ADR-011 §2.4 답습 → **외부 LLM 1+ cross-vendor blind 의뢰 의무 발화** (R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 답습).
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:586:#### 6.5.3 Group γ (C-5b ST-1 + Vault HSM ST-4) 의뢰 핵심 질문
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:589:2. Vault HSM ST-4 (ADR-010 통합) 의 6 결정 영역 (§2.5.3) 中 (i) Multi-host 인프라 부담 (ii) 운영 비용 (iii) 단일 source-of-truth 보존 측면에서 최선?
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:618:| (3) PC-4 T3 sub | 0 (개별 trigger 없음 — ADR-011 §2.4 + mvp1.md §4.4.2 영역) | 低-中 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:724:| ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ✅ |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:737:| ADR-011 §2.1 (a)~(e) / §2.4 답습 | ✅ |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:738:| ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 / §2.6.2 R2-1 / R-4.1 답습 | ✅ |
docs/phase0/backlog3-t3-zone-full-3plus1-brief.md:796:- ❌ ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:19:- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:63:- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 0건** — Phase α-1+2+3 evidence §5.3 답습
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:64:- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 0건** — Phase α-1+2+3 evidence §5.3 답습 (TR-1 ~ TR-5 미발화)
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:65:- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 0건** — Phase α-1+2+3 evidence §5.3 답습
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:276:| C-ε-18 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | ✅ Layer C `eb01bc4` 발효 답습 한정 (재발효 0건) | **답습 강화** |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:303:| **C-α4-2** | **PoC 답습 변경 0** | R-1 7 artifacts × 1593줄 답습 + Stage 4 합의 §1.3 답습 + Layer B §5.5.1 + §5.5.2 답습 모두 변경 0건 | **답습 강화** — α-1+2+3 evidence §5.1 git status clean + §5.2 8 금지 답습 위반 0/8 + §5.3 추가 영역 변경 0건 매트릭스 답습 | ✅ **답습 100% 보존 (추가 evidence 확정)** |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:320:| 9 | 본 brief 가 Hermes upstream root of trust 변경 권고 | 0건 | 0건 — CI workflow = upstream 분리 영역 (ADR-011 §2.1 (b) 수단/목적 분리 답습) | ❌ 0건 |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:370:### 5.3 금지 #3 — actual run 재실행 (분리 매트릭스)
docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md:5:> **v2 변경 (2026-05-20)**: 외부 cross-vendor blind 응답 1건 (GPT-5.5 Thinking, `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-response-gpt.md`) 회수 → §7 trigger #7 충족. 응답의 5개 보강점을 I-1 / I-2 / I-5 / I-7 + §3.3 + §7.2 에 *입력 한정* 반영 (강제 채택 0건 — §0.4 + ADR-011 외부 LLM 입력 원칙). 응답의 framing 권고(설계명 재정의)는 §7.3 에 *외부 입력 flag* 로만 기록 — 채택/발효는 풀 3+1 + 사용자 결정 권한.
docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md:76:| ADR-011 분류 | **T3 절대 금지의 *enforcement*** (§2.2 #20 = T3 12건 중 1건) |
docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md:199:### 5.3 ⚠️ self-reference 구조적 논점 (Reviewer-only 부적격 보강 근거)
docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md:205:**Group I = T3 보안 enforcement 영역 → 풀 3+1 (Agent A/B/C + Reviewer) *의무*, Reviewer-only 단축 *부적격*** (트리거 #2 BLOCKING + #5 HIGH (핵심 제약 #1 직결) + #7 외부 LLM 미충족 + §5.3 self-reference 구조). **외부 LLM 1+ 신규 입력 권장/의무** (§7 — 기존 응답 Group I thin). 사용자 명시 결정 = 최종 권위 (§4.4.3). 본 권고 = §0.4 권위 한계 — *발효* 는 합의/사용자 결정.
docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md:229:> ⚠️ **입력 한계 (불변)**: 외부 LLM 응답 = *입력 한정* (강제 채택 0건 — §0.4 + ADR-011). 본 brief v2 는 응답의 5 보강점을 해당 §에 *입력*으로 반영했을 뿐, 식별 방법 / 차단 지점 / framing *결정* 은 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합 + 사용자 명시 권한. 2차 vendor (Gemini 등) 추가 입력 = 사용자 결정 영역 (의무 아님 — 1건 회수로 trigger #7 충족).
docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md:273:| **ADR-011 §2.4** | T3 영역 (§2.2 #20 enforcement) 결정 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
docs/phase0/jarvis-mvp1-v1-poc-phase3-5-h-o-ollama-direct-entry-brief.md:19:- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
docs/phase0/jarvis-mvp1-v1-poc-phase3-5-h-o-ollama-direct-entry-brief.md:45:7. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
docs/phase0/jarvis-mvp1-v1-poc-phase3-5-h-o-ollama-direct-entry-brief.md:136:(g) `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` (45.38 GiB) + (h) `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` (17.353 GiB) 보존 답습 영구 (사용자 명시 (h) cycle 6차 세션 답습). 본 (h-O) cycle Ollama models cache = 별도 위치 (~/.ollama/ 가설), (g)/(h) GGUF 영향 0건. **cleanup = `rm` 자동 실행 0건** (비례 보안 답습).
docs/phase0/agent-privilege-escalation-policy-brief.md:25:**답습 입력 (1차 권위)**: ADR-011 §2.1 means/ends + Hermes ≠ root of trust / `harness-engineering-design.md` (Feedforward 가이드 vs Feedback 센서, 피드백 루프 Layer 0~6) / `ead5754` BI-3 수단 결정 (CD-3 docker socket·cap_drop 비협상 / CD-5 binary) / credential 수단 발효 합의 (H-1 docker group·H-2 tss·CMA-2 touch-to-sign 하한선·CMA-3) / R-I-CONFIG-CHANGE T3(사람 직접·Hermes 미주입) / [[project_minimize_user_intervention]] / [[feedback_provider_liquidity]]
docs/phase0/agent-privilege-escalation-policy-brief.md:141:- **ADR-011 Hermes ≠ root of trust**: P-PRIV 1·5 가 직접 구현 — agent 는 자기 권한 root 아님.
docs/phase0/agent-privilege-escalation-policy-brief.md:182:**출처**: ADR-011(Hermes≠root·means/ends) / harness-engineering-design(가이드·센서·Layer) / `ead5754` BI-3(CD-3·CD-5) / credential 수단 발효 합의(H-1·H-2·CMA-2·CMA-3) / R-I-CONFIG-CHANGE T3 / [[project_minimize_user_intervention]] / [[feedback_provider_liquidity]].
docs/phase0/credential-signing-workflow-design-brief.md:9:**⛔ 발효 DEFER 결정 (사용자 명시 2026-05-22, 비례성)**: 본 프로젝트 = solo·single-host·**본인용 개인 개발 툴**. credential 서명 격리(하드웨어 키·touch-per-commit·서명 사용자)는 실 위협 모델(에이전트 실수·공급망 = review/test/git로 충분)에 **비례 초과** → 발효 비권고. 본 brief = **DESIGN 청사진으로 보존** — 실 trigger(팀 합류 / public 배포 / 외부 의존 / 컴플라이언스) 발생 시 발효. means/ends(ADR-011): 하드웨어 서명 = MEANS, 현 비용 > 이득. [[feedback_proportionate_security_personal_tool]] 답습.
docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md:12:- ADR-011 §2.1 5조건 (a)~(e) 답습
docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md:178:### 5.3 Agent C — 대안 탐색가
docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md:213:- ADR-011 §2.1 (a)~(e) — 수단/목적 분리
docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md:242:**출처**: Stage 4 raw (`docs/phase0/v1-poc-raw/`) + findings (`jarvis-mvp1-v1-poc-findings.md` DRAFT Stage 1+2+3+4) + brief v1.1 + 합의 보고서 + MVP-1 brief v2 + ADR-011 §2.1.
docs/phase0/jarvis-mvp1-m3-m4-fixation-brief.md:51:| 1 | qwen3-30b-a3b-instruct | 30.5B (MoE 활성 ~3B) | qwen3moe | **15.35** | 4093 | 5.87 |
docs/phase0/jarvis-mvp1-m3-m4-fixation-brief.md:112:각 Agent → 본 brief + 이전 합의 (`9ddec1b`) + ADR-011 (means/ends) + 새 evidence 답습 → 독립 분석.
docs/phase0/mvp1-ar3-first-pr-evidence.md:134:## §5 ADR-011 §2.1 (a)~(e) 완전 충족 (AR-3 영역 한정)
docs/phase0/gp3-c3-gp5-c2-t3-zone-resolution-brief.md:17:- ADR-011 §2.4 T3 영역 / ADR-011 §2.1 (a)~(d) [+(e) 합의 패턴] / 5 영구 핵심 제약
docs/phase0/gp3-c3-gp5-c2-t3-zone-resolution-brief.md:146:| (나) 풀 3+1 | 가능 (보수적) | GP entry condition + ADR-011 §2.4 T3 영역 cross-reference → 신중 시. 단 본 갱신 = T3 *결정* 이 아닌 *완료 반영* → 풀 3+1 트리거 미발화 |
docs/phase0/gp3-c3-gp5-c2-t3-zone-resolution-brief.md:148:### 5.3 권고
docs/phase0/gp3-c3-gp5-c2-t3-zone-resolution-brief.md:171:| **(A)** | 본 brief 그대로 승인 → **condition row 갱신 합의 진입** (형태 = §5.3 권고 Reviewer-only 단축 또는 사용자 명시 풀 3+1) | 합의 보고서 작성 |
docs/constitution/PROJECT_CONSTITUTION.md:80:4. 본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ("헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)"). **다른 권위 위계 (예: 8-2조 환경 관리 원칙 vs 5조-2) 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무**
docs/phase0/g3-metadata-detection-correction-patch-brief.md:10:**선행 발효 답습**: `92cc9f3` patch brief 검증 풀 3+1 합의 (APPROVE WITH CONDITIONS, PC-1~PC-7) + `92d74be` 결함 교정 풀 3+1 합의 (CN-1~CN-10) + `afb92de` 교정 *검토* brief + Group I `f6c6d5a` (B-1~B-6) + ADR-011 §2.1 means/ends
docs/phase0/g3-metadata-detection-correction-patch-brief.md:45:6. ADR-011 means/ends 정합(CN-6) — 수단 후보 열거 형식 정비 (§6)
docs/phase0/g3-metadata-detection-correction-patch-brief.md:64:- ❌ ADR 본문 자동 갱신 (ADR-008 / ADR-011 / ADR-012) / Group I·α·β·γ 합의 본문 변경
docs/phase0/g3-metadata-detection-correction-patch-brief.md:116:| **정합 참조만 (G5)** | 230 / 805 | §2.5 #11 / §5.5.3 (1) |
docs/phase0/g3-metadata-detection-correction-patch-brief.md:149:> 모든 축은 *목적/원칙* 으로 문구화하고, 구체 수단은 §6 "수단 후보 열거" 블록으로 분리 (CN-6 + ADR-011 means/ends).
docs/phase0/g3-metadata-detection-correction-patch-brief.md:292:### 3.8 line 805 — §5.5.3 multi-host trigger (1) (정합 참조만, G5)
docs/phase0/g3-metadata-detection-correction-patch-brief.md:351:| **N2' (재명명)** | "Hermes-originated commit **provenance** (sensor)" | "signal/sensor" = *역할* 어휘(means 고정 아님, ADR-011 저촉 X) | "detection" 인용 의존 연쇄 갱신 (§5) |
docs/phase0/g3-metadata-detection-correction-patch-brief.md:390:## 6. ADR-011 means/ends 정합 (CN-6) — 수단 후보 열거 형식
docs/phase0/g3-metadata-detection-correction-patch-brief.md:403:> **정합 결론**: 본문 = 목적/원칙, 수단 = 후보 열거(결정 보류). 이는 ADR-011 §2.1 means/ends + Group I framing N1(수단 명칭 고정 보류) + Provider Liquidity 정합. **수단 *결정 고정* = 본 brief §0.3 금지 + Backlog #6.**
docs/phase0/g3-metadata-detection-correction-patch-brief.md:416:- **교정 형태 (합의 §5 권고)**: "단순 텍스트 정정"이 아닌 §2.2 #20 auto-reject 의 *판정 기준 변경* = **T3 (R-I-CONFIG-CHANGE) → Reviewer-only 부적격.** 단 식별 frame 은 Group I `f6c6d5a` + `92d74be` 에서 *이미* 만장일치 확정 → 본문 교정 단계 = **brief §5.3 "본문 반영 한정 합의 + 4 결정 항목(① 문구 ② 범위 ③ author 메타 어휘[CN-8] ④ 채널명[CN-10]) scope 명문 고정"** 권고 (풀 3+1 frame 재투표 중복 제거, B-5 T3 다관점 유지). 풀 3+1 전면 재실행 vs 축소 형태 *최종 결정* = 사용자 명시.
docs/phase0/g3-metadata-detection-correction-patch-brief.md:450:**(v2 = `92cc9f3` patch brief 검증 풀 3+1 합의 BLOCKING PC-1~PC-4 반영판.)** `92d74be` 가 *방향(4축)·조건(CN-1~CN-10)·범위* 를 확정한 G3 `hermes-not-root-of-trust-runtime.md` 결함 교정을 touch-point별 문구 교정안 *후보* 로 환원한 patch brief 를, `92cc9f3` 합의가 APPROVE WITH CONDITIONS 로 검증하며 낸 BLOCKING 4건을 반영한 v2. **v1 → v2 핵심 변경**: (PC-1) brief v1 의 8 touch-point 정적 열거가 **line 568(§3.4 통합 매트릭스 — "detection" 직접 인용 + "git pre-commit" CN-3 위반 차단 frame)·line 328(§2.6.3(b) — "detection" 2번째 literal + "§3.2" stale cross-ref, 실제는 §3.1.2)을 silent 누락**한 것을 보강 — **10 touch-point 로 확대 + 범위 종료 조건을 "정적 열거" → "grep 전수 잔여 'detection'/'auto-reject' 인용 0 검증" 동적 조건(§1.4)으로 전환**(line 457 누락→568·328 또 누락의 구조적 반복을 harness feedforward 로 차단); (PC-2) **CN-4 "실 anchor(명목 anchor 금지)"·CN-7 audit sink 별개성·CN-8 author 배제의 전파 비대칭 해소**(v1 = 한 touch-point 에만 → 448·648·360·1122 전파); (PC-3) **enforcement 보장 속성(ends) = "push/merge 전 차단 보장" 1구 명문**(means 후보 §6 과 분리 — "언제·어떤 속성으로 차단"은 ends·"무엇으로"는 means); (PC-4) **line 360/1122 에 "author=user 강제" 표현 제거에 그치지 않고 "author 판정 입력 아님·audit 사후 대조 전용" negative 배제 명제 부가**(회귀 통로 차단). 1차 교정 = line 448/784/457/648 **+568/328**, 가정 잔존 = 360/1122(P1 dangling 방지), 정합 참조만 = 230/805(single-host 비대칭 해소 시 정합). 채널명(CN-10/PC-④) = N1(유지) / N2'(provenance sensor) / **제3안 "provenance check"(4축 포괄 상위 역할어휘, "sensor"의 external enforcement 축 배제 부작용 회피, means 저촉 0) 삼안 확장** — 단 결정은 §1.4 cascade 재검증 후 본문 교정 단계(채널명 cascade = "detection" literal 448/328/568 한정, v1 의 #20 오지목 정정). 모든 문구안 = **목적/원칙 수준**, 수단은 **후보 열거(환경종속 4행 일관 + Backlog #6 cross-ref, CN-6/PC-7)** — ADR-011 means/ends 정합. 교정 형태 = **R-I-CONFIG-CHANGE=T3·Reviewer-only 부적격, "본문 반영 한정 합의 + 4 결정 항목 scope"** 권고. 권고 PC-5(line 354/1116/221 enumeration)·PC-6(448 거대 셀 분해)·PC-7(§5.5.2 정합·observe mode 도입처)도 반영. 본 brief v2 는 결론을 *선취하지 않으며* — 문구 *최종 확정*·채널명 *결정*·수단 *고정*·실 구현(hook/ruleset/CI/credential/sink)은 모두 사용자 명시 + 별도 단계 — **G3 본문 실제 수정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 / 채널명 결정 / ADR·합의 본문 자동 갱신 / commit / push = 모두 0건** 이다.
docs/phase0/g3-metadata-detection-correction-patch-brief.md:466:| ADR-011 §2.1 (means/ends) | 수단 후보 열거 형식 (§6) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:19:- ADR-011 §2.4 T3 영역 분리 답습
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:70:| (추가) | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:228:| **FP 비상 탈출구 (emergency escape hatch)** (Gap #2 — Gemini) | (i) `# scanner-allow: <reason>` line comment / (ii) `provider_catalog_allowlist.yaml` 파일 / (iii) ADR-011 위반 없이 긴급 bypass 정책 / **(iv) (i) + (ii) 통합 + expiry date 의무 + owner / rationale 의무** ⭐ GPT 권고 답습 |
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:333:#### 2.5.3 *추가* 결정 영역 (양 vendor 수렴 흡수)
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:588:### 5.3 Group β (T-5 (β) + Tier-2/3 일반) — v1 §5.3 + 외부 LLM 흡수
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:790:| ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ✅ |
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:883:- ❌ ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
docs/phase0/phase-alpha-integrated-completion-conditions-reassessment-brief.md:21:- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역
docs/phase0/phase-alpha-integrated-completion-conditions-reassessment-brief.md:425:### 5.3 Stage 4 *완료* 여부 평가 (3 layer 분리)
docs/phase0/phase-alpha-integrated-completion-conditions-reassessment-brief.md:429:#### 5.3.1 Layer (i) — Stage 4 *cycle* 완성 (cycle 1~4 모두 합의 발효 + lockdown 발효)
docs/phase0/phase-alpha-integrated-completion-conditions-reassessment-brief.md:439:#### 5.3.2 Layer (ii) — Stage 4 *본문 구현* 완료 (sub-step 4.1 + 4.2 본문 변경 영역)
docs/phase0/phase-alpha-integrated-completion-conditions-reassessment-brief.md:449:#### 5.3.3 Layer (iii) — Stage 4 *완료 격상* (Operational Readiness PASS / Hermes PMO 격상)
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:30:- ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — P2 v3 정식 채택 후 별도 PR
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:62:이 위계는 **ADR-011 §2.3** 에 영구 권위로 명시되어 있습니다. **Hermes 는 시스템의 root of trust 가 아니라 검증 대상** 입니다.
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:89:| ~~G1a~~ | ❌ FAIL 확정 (폐기) | Hermes v0.12.0 에 `pre_record` hook 부재 (15종 hook 중 DB 기록 직전 가로채기 0건). ADR-011 §2.2 영구 권위로 폐기 확정. G1a (Hermes native redaction → DB) 의 *목적* 은 G1b 가 DB-level fallback 으로 흡수. |
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:126:**합산**: 계산적 가능 6/6, 추론적 보조 4/6, 자동 롤백 6/6. 계산적 우선 — ADR-011 §2.1 수단/목적 분리 원칙 답습.
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:130:ADR-011 §2.1 (a)~(d) + 합의 APPROVE (e) 패턴 답습:
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:163:ADR-011 §2.3 (영구 권위) 의 *운영 가능 메커니즘* 화.
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:298:### 5.3 §3.4 핵심 원칙: Skill 자동 생성 vs 자동 승격 분리
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:423:2. **Hermes ≠ root of trust** — ADR-011 §2.3 영구 권위
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:425:4. **자동 정책 변경 금지 (T3)** — ADR-011 §2.4
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:426:5. **수단 / 목적 분리 원칙** — ADR-011 §2.1 (a)~(d) 4조건
docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md:547:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:5:> 본 brief 의 어떤 §도 그 자체로 (i) **내부 Agent A/B/C + Reviewer 풀 3+1 합의 보고서 *작성* / commit / push**, (ii) **Group α 실제 진입** (T3 영역), (iii) **branch protection rule 변경** (CODEOWNERS / required check / commit signing / merge restriction / direct push 차단 / force push 차단 / admin bypass 정책 / required reviewer / ruleset / repository ruleset / organization ruleset), (iv) **dev 환경 강제** (`pre-commit install` 의무화 / `.git/hooks` 자동 install / `default_install_hook_types` 강제 / `fail_fast` 강제 / `commit-msg` / `pre-push` stage 도입 / `minimum_pre_commit_version` 강제 / `--no-verify` 차단), (v) **Hermes PMO 격상 (Layer F) 선언**, (vi) **Operational Readiness PASS (Layer E) 선언**, (vii) Group β / γ-1 / γ-2 자동 진입, (viii) v1 (`ad9a02d`) / v2 (`2a9d02d`) 본문 변경, (ix) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (x) Layer B (`f40423f`) §5.5 9 sub-수단 본문 채택 변경, (xi) Layer D 합의 보고서 (`210c98f`) 본문 변경, (xii) 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정), (xiii) 외부 LLM 추가 자동 호출 / 재의뢰, (xiv) 실 API key / provider SDK / 외부 API 호출, (xv) ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012), (xvi) Backlog #1 / #2 / #4 / #6 / #7 자동 진입, (xvii) MVP-1 PASS *재선언* / MVP-2 자동 진입, (xviii) 도구 본문 (`tools/*.py`) / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경, (xix) Production `docker-compose.yml` / Hermes upstream Dockerfile / `requirements*.txt` 변경 을 발생시키지 않는다.
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:20:- ADR-011 §2.4 T3 영역 분리 답습
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:40:8. Rollback Trigger 통합 매트릭스 — Group α 한정 (§8) — R-MVP1-G5-9 (AR-3) + ADR-011 §2.4 (PC-4 T3)
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:68:| (추가) | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:236:| mvp1.md §4.3.1 PC-1 row | "pre-commit framework (`.pre-commit-config.yaml` + `pre-commit install`) — dev 환경 자동 설치 + framework 도입 + dev 환경 강제 — T2 (정책 영역, ADR-011 §2.4 답습)" |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:237:| ADR-011 §2.4 | "dev 환경 강제 정책 = T3 영역" |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:244:| dev 환경 *정책* 변경 (`pre-commit install` 의무화) | ✅ HIGH (T3 — ADR-011 §2.4 답습) |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:331:| **(가) 풀 3+1 합의 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시** | ✅ **권고 (v2 답습)** | (i) Group α = T3 영역 진입 의무 / (ii) R-MVP1-G5-9 (AR-3) + ADR-011 §2.4 (PC-4 T3) 답습 / (iii) 외부 LLM 응답 회수 완료 (`8b5b626`) — 응답 = 입력 한정 + 추가 발송 0건 |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:338:### 5.3 합의 발효 시점 (v2 §4.3 답습)
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:453:| **ADR-011 §2.4 답습** | Group α 전체 | T3 영역 진입 결정 | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:549:| Rollback Trigger 통합 매트릭스 — Group α 한정 (R-MVP1-G5-9 + ADR-011 §2.4) | ✅ §8 |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:556:| ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ✅ |
docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md:615:- ❌ ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:1:# MVP-1 PC-1-T3 mandatory enforcement 실 구현 sub-cycle brief
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:3:> **scope**: MVP-1 1.5차 보강 entry 합의 (24번째 entry, commit `9638521` brief v1.1 + 합의 보고서 `3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` APPROVE WITH CONDITIONS) 의 **PC-1-T3 mandatory enforcement 실 구현 sub-cycle**. 본 sub-cycle = entry 합의 결정 *집행* (T3 채택 결정 자체는 entry cycle 에서 완료).
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:13:| **24번째 entry brief v1.1** | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (commit `9638521`) | §2.3 PC-1 정의 (line 183~211) + §3 ADR-011 (a)~(e) 매트릭스 (PC-1 cell) + §4 합의 형태 권고 (line 292 "단축 합의 + 사용자 명시") + §5.1 Rollback Trigger R-MVP1-1.5-PC1-{1,2,3} (line 329~331) + §6 Evidence 행 (line 343~345) + §7.3 외부 LLM 자격 |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:14:| **24번째 entry 합의 보고서** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | R-2 BLOCKING (PC-1 (b)(d) 재분류) / R-6 BLOCKING (PC1-1 탐지 경로 (i)(ii)(iii)) / R-7(b) BLOCKING (PC1-2 차등) / N-1 권고 (PC-1 단독 우회 가능, PC-3 + AR-3 결합 효과 명문) / N-2 권고 (PC-1-T3 명칭 일관) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:15:| **ADR-011** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 (수단 결정 발효 자격) + §2.4 T3 영역 (dev 환경 정책) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:27:| **scope** | PC-1-T3 mandatory enforcement 실 구현 (entry 합의 결정 *집행*) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:37:| 1 | `.pre-commit-config.yaml` 본문 변경 (신규 hook / version pin 외 모든 변경) | 0건 (별도 cycle, R-7(b) 차등) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:56:| **R-7(b)** BLOCKING | R-MVP1-1.5-PC1-2 차등 — 신규 hook (Tier-2/3 catalog / provider policy / security gate) = 풀 3+1, 단순 version pin = 단축 합의 | §6 Rollback Trigger 본 sub-cycle 적용 형태 (PC1-2 차등 답습) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:58:| **N-2** 권고 | PC-1-T3 mandatory enforcement 명칭 일관 | 본 brief 전체 "PC-1-T3" 명칭 일관 답습 |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:89:| 2 | CONTRIBUTING.md | 부재 | 신규 작성 (dev onboarding workflow + PC-1-T3 의무화 명문) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:102:| **(β)** pre-commit framework 흡수 | `.githooks/pre-commit` 내용을 `.pre-commit-config.yaml` 의 신규 hook 으로 흡수 | 통합 ↑, 단 `.pre-commit-config.yaml` 본문 변경 = 별도 cycle (R-7(b) 차등) — **본 sub-cycle scope 외** |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:128:- PC-1-T3 mandatory enforcement 명문 (`pre-commit install` 의무, 우회 = R-MVP1-1.5-PC1-1 trigger)
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:156:# Step 3: pre-commit framework 의무화 (PC-1-T3)
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:158:echo "[OK] pre-commit framework 활성화됨 (PC-1-T3 mandatory enforcement)"
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:199:## §5 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (PC-1-T3 본 sub-cycle 한정)
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:209:→ **현 시점 충족 = (c) 만** → 본 sub-cycle 합의 발효 = (a)~(e) 5/5 충족 (PC-1-T3 영역 한정)
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:218:| **R-MVP1-1.5-PC1-2** | `.pre-commit-config.yaml` 본문 변경 — 차등 (R-7(b) 답습): (i) 신규 hook = Tier-2/3 catalog / provider policy / security gate / (ii) 단순 version pin / hook config update | (i) 풀 3+1 + 외부 LLM 1+ / (ii) 단축 합의 + 사용자 명시 |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:227:| **(a) Markdown report** | `docs/phase0/g2-gp3-mvp1-evidence.md` + `docs/phase0/g2-gp5-mvp1-evidence.md` 보강 (PC-1-T3 영역 추가) | 별도 sub-cycle 또는 본 sub-cycle 확장 결정 |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:259:| **풀 3+1 승격 trigger** | 5/5 모두 발화 0건 (① 새 권위 결정 0 / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0) |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:283:| 7 | 24번째 entry BLOCKING R-2 / R-6 / R-7(b) 흡수 + N-1 / N-2 권고 흡수 | ✅ §2 매트릭스 답습 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:3:> **본 brief = format 가족별 분류 cycle (f-K) 합의 (`d75dceb`, APPROVE w/ COND, BLOCKING 16 + 권고 21 + NOTE 24, 기각 0, Reviewer 단독 격상 3) brief v1.1 (`eca4cf5`, 710줄) §7.1 (A) 옵션 채택 자격 평가 entry brief.** v1.1 = 풀 3+1 합의 (`d0f516d`, APPROVE w/ COND, BLOCKING 16 + 권고 18 + NOTE 29, 기각 0, Reviewer 단독 격상 3 R-S1·R-S2·R-S3) verbatim 본문 직접 반영. 사용자 명시 — "(g1-A)" 선택 + 정공법 (entry brief + 풀 3+1) 형태 선택. 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 변경·모델 다운로드·측정 실행·config 변경·M3/M4 결정 *고정*·MVP-1 합의 본문 자동 정정·헌법 본문 자동 정정·ADR-011 amendment 자동 발의·메모리 자동 갱신·Provider Liquidity 본질 약화·4 가족 분류 자체의 영구 framing 정착·6축 framing 자체의 영구 정착·(g1-A) 자체의 영구화 정착** 를 발생시키지 않는다. 실 변경 0건. staged: brief v1 (`fc6731e`, 397줄) → 풀 3+1 합의 (`d0f516d`, 343줄) → **brief v1.1 (본 문서)** → 세션 정리·commit·push. 자동 다음 단계 진입 0건.
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:28:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (line 6 + line 212 + line 245 verbatim 권위 매핑, *본 cycle 본문 변경 0건*)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:29:- `docs/constitution/PROJECT_CONSTITUTION.md` (제5조 line 40~46 verbatim "코드 품질 원칙" + 제8-2조 line 67~73, *본 cycle 본문 변경 0건* — **R-S2 답습 명문 의무: 5조 본문 ≠ "Provider Liquidity" 직접, ADR-011 line 6/245 *매핑* 의존**)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:39:2. **본 (g1-A) 채택의 정확한 의미 분해** — (i) 4 가족 분류 현 상태 유지 / (ii) **6축 framing 자체의 임시성 (R-12 + R-2 답습) + 축 5 framing 임시성 *재* 명문 (R-3 + R-12 답습 강한 변형) 이중 의미 — 6축 framing 의 영구 정착 차단 (R-2) + 축 5 framing 임시성 강한 영구 답습 (R-12) 통합** (R-16 답습) / (iii) MVP-1 합의 본문 변경 0건 / (iv) 메모리 본문 변경 0건 / (v) 헌법·ADR-011 본문 변경 0건 (§2.2). **§0 #2 (ii) → §2.2 (ii) verbatim 동형 강화**: "현 상태 유지 + 임시성 *재* 명문 only — 7축 신설·축 폐기·축 우월성 단정 0건" (R-17 답습)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:43:6. SDD 정합성 매트릭스 — 헌법 + ADR-011 + MVP-1 + 메모리 본문 변경 0건 답습 명문 + **헌법 5조 본문 ↔ ADR-011 line 6/245 매핑 4 차원 분리 (R-3 = R-S2 답습)** (§3)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:45:8. 3+1 합의 분담안 — Agent A/B/C 관점·핵심 질문·출력 형식 + **각 Agent raw line-level cross-check 의무 6 차원 (brief v1.1 / format 합의 / ADR-011 / 헌법 / MVP-1 / 메모리)** (R-31 답습) (§5)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:47:10. (g1-A) 채택 *후* carry-over 옵션 매트릭스 (§7) — **권고 자격 only, 결정 *고정* 0**. **(g1-N) 헌법 5조 본문 미세 보강 + (g1-O) ADR-011 line 212 본문 미세 보강 옵션 추가 (R-2 답습)** + **옵션 진입 자격 형식 통일 + 4 *방향성* 평가** + **§7.5 우선순위 *권고* 자격 명문 (R-29 답습)**
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:59:3. ❌ **헌법 본문 자동 정정** — 5조·8-2조·ADR-011 line 6/212/245 권위 답습 명문만, **헌법 5조 본문 ↔ ADR-011 매핑 자체 변경 자격 0 (R-3 = R-S2 답습 — 매핑 자격 인정 only, 별도 cycle (g1-N) 의무)**
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:60:4. ❌ **ADR-011 amendment 자동 발의** — (g1-A) 의 가벼움 자체가 ADR amendment 발의 자격 부재 (R-9 헌법급 변경 답습)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:94:**Q5 (R-26 답습 — 신규)**: (g1-A) 채택 외 *다른 채택 형태* — (a) micro-brief 형식 / (b) 채택 자체 생략 ((g1-D2) 자동 기본값) / (c) Reviewer-only 단축 합의 (ADR-011 모법 답습) / (d) 결합 옵션 ((g1-A) + (g1-D4) 또는 (g1-A) + (g1-N)/(g1-O)) 의 식별 자격 + 본 cycle 채택 자격 평가 (Agent C 의무, 대안 탐색가). **본 cycle 합의 결과 NOTE N-26·N-27·N-28 carry-over** — 사용자 명시 "(g1-A)" + 정공법 발효 = 본 cycle 채택 자격 0건 발효.
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:96:### 1.3 헌법·ADR-011 권위 매핑 답습 (변경 0건, R-3 = R-S2 답습 영구 의무)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:98:본 cycle = format 가족별 분류 합의 brief v1.1 §1.4 의 헌법·ADR-011 권위 매핑을 *답습* only. 본문 변경 0건. (R-13 + R-10 = R-S2 통합 답습)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:100:**R-3 = R-S2 답습 (Reviewer 격상 영구 의무)**: **헌법 5조 line 40~46 verbatim** = "제5조: 코드 품질 원칙" (5 항목 — 읽기 쉬움 / SRP / 중복 제거 / 외부 입력 검증 / 린터). **'Provider Liquidity (비협상)' 명시는 ADR-011 line 6 + line 245 *내부* 권위 매핑**. 본 cycle 답습 의무 = (i) 헌법 5조 본문 verbatim ≠ Provider Liquidity 직접 본문 + (ii) ADR-011 line 6/245 *상위 권위* 명시 = ADR-011 *내부* 매핑 자격 답습 only + (iii) 헌법 5조 본문 ↔ ADR-011 line 6/245 매핑 *자체* 의 비대칭은 format 합의 R-S2 답습 *상위 단계* 비대칭. **본 cycle 답습 = 매핑 자격 인정 only, 매핑 자체 변경 자격 0** (R-9 헌법급 변경 답습, 별도 cycle (g1-N) 의무).
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:103:- ADR-011 line 6 verbatim ("**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)") — 답습 only
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:104:- ADR-011 line 212 verbatim ("Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관") — 답습 only
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:105:- ADR-011 line 245 verbatim ("제5조 **관용** (Provider Liquidity, 비협상)") — 답습 only
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:133:| (v) 헌법·ADR-011 본문 | 5조 line 40~46 + ADR-011 line 6/212/245 권위 매핑 (R-3 = R-S2 답습) | **본문 변경 0건** — 권위 답습 only, 매핑 자격 인정 only (별도 cycle (g1-N)/(g1-O) 의무) |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:159:| R-14 (Reviewer 권한 한계 7 항목 + 본 합의 R-7 by-reference vs 재서술 boundary) | format 가족별 분류 합의 BLOCKING R-14 / brief v1.1 §5.3 / 본 합의 R-7 | 본 cycle Reviewer 권한 한계 7 항목 영구 답습 의무 + **재서술 + by-reference 통합 답습 (출처 chain Provider Liquidity → format → 본 cycle, 본 cycle 신규 생성 0건, 본 합의 R-7 답습)** |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:165:### 3.1 헌법·ADR-011 권위 매핑 정합성 (변경 0건, R-3 = R-S2 답습 — 4 차원 분리)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:170:| **ADR-011 line 6 매핑 차원 ("상위 권위: 헌법 제8조, 헌법 제5조 (Provider Liquidity)")** | 답습 only, ADR-011 *내부* 매핑 | 0건 (R-9 헌법급 변경 답습) |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:171:| **ADR-011 line 212 주제 범위 한정 차원 ("redaction 수단 해석이며 모델/구독 교체 자유와 무관")** | 답습 only (R-S2 답습 영구 의무) | 0건 (별도 cycle (g1-O) 의무) |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:172:| **ADR-011 line 245 관용 매핑 차원 ("제5조 관용 (Provider Liquidity, 비협상)")** | 답습 only | 0건 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:173:| ADR-011 §2.1 (a)~(d) 4조건 + (e) 후속 패턴 | (g1-A) 진입 자격 평가 시 답습 only, (e) 후속 패턴 자격 평가 별도 cycle | 0건 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:174:| **Reviewer 권한 한계 7 항목 출처 chain** (Provider Liquidity `a9e1e88` line 365~373 → format `d75dceb` line 367~373 → 본 (g1-A) brief §5.3, 3 cycle carry-over, 본 cycle 신규 생성 0건, R-7 답습) | 답습 only | 0건 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:273:| **B (품질·안전성 검증가)** | "(g1-A) 채택이 안전·정직성·답습 의무 충족하는가?" | Q-B1 = R-12 + R-29 + R-30 + R-4 답습 의무 100% 충족. Q-B2 = MVP-1·메모리·헌법·ADR-011 본문 변경 0건 명문 정합성. Q-B3 = brief 본문 self-consistency (§0 ↔ §9.1 1:1 매핑). Q-B4 = (g1-A) 자체의 영구화 risk 차단 명문 충분성. Q-B5 = Reviewer 권한 한계 7 항목 본 cycle 답습 명문. |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:276:**각 Agent 의 raw line-level cross-check 의무** (R-31 답습, R-34 + R-35 답습): 본 §5.1 의 Q-A1~Q-C4 답변 시 모든 인용 본문 = (a) brief v1.1 line offset / (b) format 합의 보고서 line offset / (c) ADR-011 line offset / (d) 헌법 line offset / (e) MVP-1 합의 line offset / (f) 메모리 line offset **6 차원 명시 의무**. line offset 부재 인용 = BLOCKING 격상 자격 (R-S* 격상 patterns 답습).
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:285:### 5.3 Reviewer 권한 + 한계 (R-14 답습 — 7 항목 boundary 영구 명문)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:287:> **Reviewer 권한 한계 7 항목 답습 자격 boundary (R-7 답습)**: 본 §5.3 = format 합의 보고서 (`d75dceb`) line 367~373 verbatim by-reference 답습 + 본 (g1-A) cycle 의 가벼움 명문 답습 차원 **재서술 (본 brief 본문 명시 형태) + by-reference (출처 line offset 명시 형태) 통합 답습**. 본 §5.3 의 어떤 항목도 본 cycle 새 생성 자격 0 — 모두 출처 by-reference 답습 (R-22 + R-26 답습).
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:289:**Reviewer 권한 한계 7 항목 출처 chain** (R-7 답습): Provider Liquidity 합의 보고서 (`a9e1e88`) line 365~373 → format 합의 보고서 (`d75dceb`) line 367~373 → 본 (g1-A) brief §5.3 line 245~252 (3 cycle carry-over chain, 본 cycle 신규 생성 0건).
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:293:1. ADR-011 §6 본문 정정 자격 0
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:320:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` line 6 + line 212 + line 245 — verbatim 답습 only
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:345:| **(g1-O)** ⭐ | 본 cycle 결과 → ADR-011 line 212 본문 미세 보강 (가족 차원 적용 boundary 1 줄 명문 추가, R-S2 답습) | 사용자 명시 + 별도 brief + 풀 3+1 (R-9 헌법급 변경) |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:354:| **(f-C)** | 헌법 5조 + ADR-011 line 6/245 "관용 매핑" 권위 답습 명문 | 사용자 명시 + 별도 cycle |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:355:| **(f-D3)/(f-D4)/(f-E)/(f-F)** | framing 비교 ADR / DEFER / ADR-011 amendment | 사용자 명시 + 별도 cycle (R-9 헌법급) |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:379:- **본질 충돌 차단 우선 강한 후보**: (g1-D3) framing 비교 ADR (α'~ε' 5 framing + 4 가족 비교 본문) / (g1-O) ADR-011 line 212 본문 미세 보강
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:398:9. **헌법 5조 본문 ↔ ADR-011 line 6/212/245 관용 매핑 권위 답습 only** — 권위 자체 변경 자격 0 (R-13 + R-10 + R-9 답습). **헌법 5조 line 40~46 verbatim = "코드 품질 원칙" (Provider Liquidity 직접 본문 부재, ADR-011 매핑 의존, R-3 = R-S2 답습 영구 의무)**
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:399:10. **Reviewer 권한 한계 7 항목 영구 답습** (R-14 답습 영구) — §5.3 명문, 재서술 + by-reference 통합 답습 (R-7 답습)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:418:3. ❌ 헌법 본문 자동 정정 (R-9 답습) — **헌법 5조 본문 ↔ ADR-011 매핑 자체 변경 자격 0 (R-3 = R-S2 답습 — 매핑 자격 인정 only, 별도 cycle (g1-N) 의무)**
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:419:4. ❌ ADR-011 amendment 자동 발의 (R-9 답습 — 헌법급 변경)
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:435:본 §3·§4 의 표 자체가 후속 cycle 의 MVP-1 합의·헌법·ADR-011·메모리 본문 정정 *de facto* 진입 근거가 되는 흐름 차단.
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:474:| **N-28** | Reviewer-only 단축 합의 대안 (ADR-011 line 3 모법 답습 패턴) 식별 carry-over. 사용자 명시 정공법 발효 = 본 cycle 채택 자격 0. 후속 cycle 단축 합의 자격 평가 별도 cycle (memory `feedback_staged_consensus_workflow` 답습 트리거 enum 의무) | C-A3 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:497:| **§1.3 헌법·ADR-011 매핑** | R-3 = R-S2 답습 verbatim 본문 직접 반영 — 헌법 5조 line 40~46 = "코드 품질 원칙", Provider Liquidity 직접 본문 부재, ADR-011 line 6/245 매핑 의존, 매핑 자체 변경 자격 0, 별도 cycle (g1-N) 의무 + Phase 3 R-5 ↔ (g1-A) framing 동형 명문 (R-15) | R-3 + R-15 + R-17 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:502:| **§3.1 권위 매핑 정합성 표** | 4 차원 분리 행 추가 (R-3 = R-S2 — 헌법 5조 본문 차원 / ADR-011 line 6 매핑 / line 212 주제 범위 / line 245 관용 매핑) + Reviewer 권한 한계 7 항목 출처 chain 행 추가 (R-7) | R-3 + R-7 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:511:| **§5.3 Reviewer 권한 한계** | 재서술 + by-reference 통합 답습 명문 (R-7 — 출처 chain 3 cycle carry-over, 본 cycle 신규 생성 0건) + 헌법·메모리 본문 정정 자격 0 R-S2 + R-S1 답습 | R-7 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:514:| **§7.1 옵션 표** | (g1-N) + (g1-O) 2 행 신규 추가 (R-2 — 헌법/ADR-011 본문 미세 보강 옵션). 진입 자격 컬럼 "사용자 명시 + 별도 brief + 풀 3+1" 단일 형태 통일 + (g1-A) + (g1-D4) 결합 cycle 자격 명문 (R-25) | R-2 + R-25 |
docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md:537:**End of brief v1.1** (작성일 2026-05-24, format 가족별 분류 cycle (f-K) 5차 entry, 본 cycle 합의 `d0f516d` BLOCKING 16 + 권고 18 + NOTE 29 + Reviewer 단독 격상 3 (R-S1·R-S2·R-S3) verbatim 본문 직접 반영 100%, 결정 *고정* 0건, MVP-1·메모리·헌법·ADR-011 본문 변경 0건, 4 가족 분류 영구 framing 정착 0건, 6축 framing 영구 정착 0건, Provider Liquidity 본질 약화 0건, (g1-A) 자체의 영구화 정착 0건, 자동 채택·자동 기각 자격 0건, brief v1.1 본문 변경 = 본 문서 한정 답습)
docs/phase0/phase-alpha-integrated-completion-elevation-decision-brief.md:17:- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역
docs/phase0/phase-alpha-integrated-completion-elevation-decision-brief.md:375:### 5.3 본 §5 의 *핵심 정리*
docs/phase0/phase-alpha-integrated-completion-elevation-decision-brief.md:423:| 2 | **위험 안전성 上** — (B) = 4 옵션 中 위험 영역 최소 (영향 영역 매트릭스 §6 답습) + 사용자 명시 6 금지 영역 기술 + 해석 위반 위험 모두 0건 | §5.3 + §6.2 답습 |
docs/INDEX.md:5:**최종 업데이트**: **2026-05-27 세션 — 41번째 entry: ⭐ (b1-PC1-D6-fix) 본 workflow 정합 결함 정정 (1-agent 직접) + (b1-PC1-D6-false-positives) 신규 carry-over (`pre-commit-bypass-detection.yml` 첫 발화 결과 audit 시 FAIL 17초 x2 발견 → 2 종류 violation: (1) `workflow-permissions-check` 1건 = brief §4.1 정합 결함 [R-MVP1-G3-7 (v) R-6 default-deny 누락] = 1 line 정정 즉시 + (2) `secret-scanner` 10건 = `src/jarvis/{layer1,worker}.py` Python keyword arg/exit code 참조 false positives = pre-existing, **(b1-PC1-D6-false-positives) 신규 carry-over** [풀 3+1 권고, secret-scanner 패턴 변경 G3 Tier-1 catalog 영향 R-7(b) 차등]. 본 D-6 workflow가 R-6 BLOCKING 의도한 *결과 차이 검출* 메커니즘 정확 작동 검증 ✅. dev 환경 hook bypass 의심 아님 = changed files vs all-files 검사 범위 차이 = 정상 detect 효과). 40번째 entry: ⭐⭐ (b1-PC1-D6) bypass detection CI 통합 sub-cycle (Reviewer-only 단축 합의 APPROVE + 신규 workflow `pre-commit-bypass-detection.yml` 1 file 발효 — job `bypass-detect` + trigger 4종 [push+PR+nightly schedule cron `0 3 * * *` KST 12:00+workflow_dispatch] + `pre-commit==4.0.1` + `pre-commit run --all-files --show-diff-on-failure`. 5/5 풀 3+1 승격 trigger 0건 발화 + 사용자 결정 3/3 답습 ((A) 신규 workflow + Reviewer-only + contexts carry-over) + 변경 0건 9/9 + R-6/D-6/R-7(b) 흡수 3/3 + ADR-011 §2.1 (a)(c)(e) 3/5 본 합의 시점 충족 → 실 구현 완료 시 5/5 (PC-1-T3 (b)(d) 회귀 자격 보강). 26번째 entry PC-1-T3 brief §10 D-6 carry-over 해소. 신규 carry-over: (b1-PC1-D6-contexts) branch protection contexts 갱신 = admin scope 사용자 영역). 🎉 본 세션 종료 (25 → 39 entry chain, 15 entry 발효, ⭐⭐⭐⭐ MVP-1 PASS 완전 발효 milestone + R-S1 cascade 영원 종결 누적) — ⭐⭐ 39번째 entry: (iii) Markdown evidence 통합 sub-cycle (g2-gp3-mvp1-evidence + g2-gp5-mvp1-evidence 신규, 28번째 D-3 carry-over 해소) + 세션 종료 안내 (다음 세션 = facade real / MVP-2 / 프라이데이 등 큰 cycle) + ⭐⭐⭐ 38번째 entry: (b2-massive) 50 file × 160 위치 sed 일괄 R-S1 정정 (자동화, R-S1 cascade 영원 종결 ✅) — 60 file × 209 위치 audit → 자기언급 13 file + ADR-008/hermes-adoption-design 제외 → 50 file × 160 위치 sed 일괄 (3 substring multi-source 재기술) → 잔여 0건 verify ✅ + git diff stat 160/160 균형. **R-S1 cascade 누적 정정 198 위치 (35 + 36 + 37 + 38 = 10+9+19+160) 완료 ✅** + ⭐⭐ 37번째 entry: (b2-others) 합의 historical + CONTEXT.md R-S1 정정 sub-cycle (1-agent 직접, 19 위치 정정 = 36 명시 10 + cycle 안 확장 9 = st2-c5a-satisfaction 3 + alpha-123-parallel-implementation 1 + backlog3-groupgamma2-st4-vault-hsm 1 + backlog6-implementation-entry 2 + CONTEXT.md 3 + st2-inotify-sidecar-entry 9, ADR-008 본문 변경 0건 R-MVP1-PASS-2 영구 금지 답습, 신규 carry-over (b2-massive) 47 file 발견 = 대규모 정정 별도 sub-cycle 답습) + ⭐⭐ 36번째 entry: (b2-roadmap) roadmap-mvp1 본문 자체 R-S1 정정 sub-cycle (1-agent 직접, 34번째 paths-aware + 35번째 (b2)+(b3) pattern 답습, 9 위치 정정 = roadmap-mvp1 7 + mvp-1-to-6 1 + 2026-05-13-mvp1-pass 1, ADR-008 본문 변경 0건 R-MVP1-PASS-2 영구 금지 답습, hermes-adoption-design 자체 §X source-of-truth 답습 ✅, 신규 carry-over (b2-others) 10 위치 발견 = 합의 보고서 historical 7 + CONTEXT.md 3) + ⭐⭐ 35번째 entry: (b2) R-S1 cross-reference 정정 + (b3) roadmap-mvp1 §3.6.3 framing 정정 병렬 sub-cycle (단축 합의 + 사용자 명시, 10 위치 정정 = governance-preconditions 6 + backlog1 3 + roadmap §3.6.3 line 290 framing 1, R-3 multi-source 재기술 답습, ADR-008 본문 변경 0건 R-MVP1-PASS-2 영구 금지 답습, ST-2 별도 row 분리 framing 정정, roadmap-mvp1 본문 자체 R-S1 8+ 위치 추가 발견 = 별도 sub-cycle carry-over) + ⭐ 34번째 entry: (vi) paths-aware workflow audit sub-cycle (1-agent 직접, 11 workflow audit 결과 추가 risk 0건 발견 = r2-canary 단독 paths 필터 + 이미 31번째 entry contexts 제거 완료, 다른 10 workflow 모두 필터 0건 = 매 PR 발화 보장, 7 contexts 매핑 verify ✅, 31번째 entry §4.3 + 33번째 entry R-6 carry-over 해소 명문, R-MVP1-PASS-8 trigger 발화 0건, 변경 0건 = evidence file 1건 신규 + SESSION + INDEX) + ⭐⭐⭐⭐ 33번째 entry: MVP-1 Implementation Evidence PASS *완전 발효* (α) — 본 프로젝트 최초 + 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS (Agent A/B/C 3 병렬 + codex via tmux cross-vendor / BLOCKING 6 (R-1~R-6) + 권고 5 1pass 흡수 / GP-3 5/5 + GP-5 5/5 + 17/20 완전 + 3/20 부분 = Defense in depth cross-cover + 자율 영역 + cross-reference 정정 한정 / roadmap-mvp1.md §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 갱신 / brief v1.1 in-place 보강 / R-MVP1-PASS-{1~10} 10 trigger / 다음 = paths-aware audit → (b2)+(b3) 병렬 → Markdown evidence → ...) + ⭐⭐ 32번째 entry: 프라이데이 (Friday) 별도 자가진화 툴 진입 자격 평가 entry brief 작성 (1-agent 직접, brief 단계 한정, 자비스 4 invariant 영구 보존 + 5 layer 격리 + Rollback Trigger 5건 + D-1~D-8 사용자 결정 carry-over, 자비스 MVP-1 완료 후 합의 cycle 진입 자격 충족) + ⭐⭐⭐ 31번째 entry: MVP-1 AR-3 첫 PR evidence 수집 (PR #2 draft, 첫 발화 1 FAIL + 1 미발화 → aws_key.py fixture 정정 + contexts v2 7 unique → 재발화 11/11 SUCCESS + mergeable CLEAN + 중복 동작 race 0 확정 + paths-aware risk 발견, ADR-011 (a)~(e) 5/5 완전 충족 AR-3 영역, (c) MVP-1 Implementation Evidence PASS 발효 합의 진입 자격 자격) + ⭐⭐⭐ 30번째 entry: MVP-1 AR-3 사용자 admin scope 단계 7 실 적용 + R-MVP1-1.5-AR3-2a catalog 정정 (main branch protection rule 활성화 gh api PUT 발효, GitHub 실 check_run name mismatch 발견 = brief v1 "workflow + job" → 실 "job only 8 unique" 정정, scan x2 + enforce x3 중복 첫 PR verify carry-over, develop branch 부재 carry-over, 외부 effect = repo 영구 정책, ADR-011 (a)(c)(e) 3/5 완전 + (b)(d) 부분 충족 첫 PR evidence 의무) + ⭐⭐⭐ 29번째 entry: MVP-1 AR-3 통합 PR auto-reject 실 구현 sub-cycle ((b1) 4/4 마지막 sub-cycle 완료, Reviewer-only 단축 합의 APPROVE) + ⭐⭐ 28번째 entry: MVP-1 ST-2 inotify sidecar 실 구현 sub-cycle ((b1) 세번째) + ⭐⭐⭐ 27번째 entry: MVP-1 S-3 detect-secrets 부분 통합 실 구현 sub-cycle ((b1) 두번째, Defense in depth S-1+S-3) + ⭐⭐⭐ 26번째 entry: MVP-1 PC-1-T3 mandatory enforcement 실 구현 sub-cycle ((b1) 첫) + ⭐ 25번째 entry: untracked dashboard 3 파일 정리 (chore) + ⭐⭐⭐ 24번째 entry: MVP-1 1.5차 보강 entry brief 풀 3+1 + 외부 LLM 1+ APPROVE w/ COND + ⭐⭐ 22번째 entry: Layer 2 설계 cycle + ⭐⭐ 23번째 entry: MVP-1 GP-3/GP-5 현 상태 audit + roadmap-mvp1 DRAFT → APPROVED 권위 발효. **(b1) 4 sub-cycle 모두 완료 + AR-3 사용자 admin scope 적용 발효 = MVP-1 1.5차 보강 4 sub-수단 실 구현 + branch protection 발효 — (c) MVP-1 Implementation Evidence PASS 발효 합의 진입 자격 자격 (첫 PR evidence 후 완전 충족)**.** 23번째 entry: audit brief (21 도구 + 11 workflow + .pre-commit + .importlinter + adapters/llm placeholder 실 구현 완료 확인) → (a) Reviewer-only 단축 합의 (5/5 풀 3+1 승격 trigger 0건 발화) → roadmap-mvp1 line 826/827 갱신 (본문 §1~§8 변경 0건). 권위 표시 격상 + audit 한정. 실 코드 0 / CI 0 / hook 0 / PASS 발효 0 / ADR 본문 갱신 0 / 수단 결정 0 / threshold 고정 0 / Tier-2/3 자동 확장 0. carry-over: (b) 1.5차 보강 풀 3+1 + 외부 LLM 1+ / (c) MVP-1 Implementation Evidence PASS 발효 합의 / (d) facade real 본문 TR-1 별도 trajectory. 22번째 entry: Layer 0(관찰 누적) + Layer 1(패턴 마이닝, 보고만) 다음 단계 = "제안 생성". `PatternReport` → `Proposal`/`ProposalSet`. 본 cycle = **설계만, 코드 0 / 테스트 0 / 발효 DEFER**. brief v1 → 풀 3+1 합의 (Agent A REVISE / Agent B COND / Agent C COND + Reviewer **APPROVE w/ COND**) → brief v1.1 보강 (13 항목 1pass 흡수, 별도 v2 cycle 0). 합의 보고서 의사록 작성. 원칙 8/8 유지 (코드 0 / 테스트 0 / 발효 DEFER / threshold 고정 0 / 자동 적용 0 / Layer 0/1 수정 0 / 외부 호출 0 / ceremony-inflation 회피). 보조: jarvis_hud TTS team-lucid/F5-TTS-ko (1.34GB, NFD jamo) + KSS ref 발효 — "여성 한국어 인식, 음색 추후 확장 가능성 deferred". HEAD = 본 22번째 entry 정리 commit. ▼ 이전 세션 — ⭐⭐⭐ (g1-N-3') HIGH 통합 cycle (10번째 entry, 5 후속 cycle 통합 결합 cycle, Reviewer 권한 한계 (8) 예외 자격 발효 시점, brief v1 `cc9c0a0` → 합의 `fea84bf` BLOCKING 14 + R-S1~R-S6 → brief v1.1 (`2633539`) + 5 명문 정정 (γ-2) chain commit (`0d72799` hermes + `ab96e30` pamsd + `717ab00` gov + `394e4ec` adr-009-010) + 본 정리 commit). 실 정정 = 10 위치 + 2 cross-ref block (5 파일). Reviewer 권한 한계 (10) 신규 격상 11 sub-boundary 확장. 1회 한정 + 영구화 0건. (g1-N-3-adr-008+sip+adr-012') HIGH 신규 carry-over. ⭐⭐⭐ **본 후속 세션 (g1-N-3-adr-008+sip+adr-012') HIGH cycle 11번째 entry chain 영구 종결 완료** (MEMORY.md cleanup 38KB → 1.3KB → brief v1 `b55e0c9` → 합의 `209f04d` BLOCKING 11 + R-S1 CRITICAL hermes-not-root 추가 source (gov §1.1 line 78 명문 4 source 외 *유일* 추가 동형) → brief v1.1 `c9493c0` → 4 source cross-ref block 1 commit `f20fce3` ((f) cross-ref block 만 채택, (g1-N-3-pamsd) ab96e30 동형 패턴) + 본 정리 commit). (g1-N-3) chain 영구 종결 명문 의무 + Reviewer 권한 한계 (11) sub-boundary 신설 *기각* + §10.6 7→9 조건 확장**. ▼ 이전 세션 — Phase 2 EXECUTED(`c66756b`) + M3·M4 단독 미충족 합의(`d2d7bf9`) + Phase 3 entry brief v1(`cc145fd`)/v1.1(`25eb008`) + 풀 3+1 합의(`e76acc8`) + 1차 정리(`3729997`) + ⭐ Phase 3 실 빌드 cycle EXECUTED(`7209743`) + ⭐ Provider Liquidity deep-dive 합의 cycle (`9ed376a` → `a9e1e88` → `8ae1ab6`) + 3차 정리(`2b456f8`) + ⭐ format 가족별 분류 cycle (`f305174` → `d75dceb` → `eca4cf5`) + 4차 정리(`7bbc2e3`) + ⭐ (g1-A) 채택 cycle (`fc6731e` → `d0f516d` → `bdcc3a6`) + 5차 정리(`2ff09d6`) + ⭐ (g1-N) 헌법 5조-2 신설 자격 평가 cycle (6차 entry, `6f64491` → `1ec9c5e` BLOCKING 22 + Reviewer 격상 5 → `58e06d5`) + 6차 정리(`7a4b574`) + ⭐⭐⭐ (g1-N-1) 헌법 5조-2 본문 변경 commit cycle (7차 entry, `5b0c0ab` → `77f36cf` BLOCKING 14 + Reviewer 격상 4 → `148fbbe` = 본 세션 + 본 프로젝트 최초 + 유일 헌법 본문 변경 commit) + ⭐⭐⭐ (g1-N-2) ADR-011 line 6/245 매핑 정정 cycle (8차 entry, `8207f55` → `07cd3f4` BLOCKING 10 + Reviewer 격상 3 → `3bdb1be` = 본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit) + 7-8차 통합 정리(`3f84c26`) + ⭐⭐ **(g1-N-3) CLAUDE.md / roadmap.md 정합 정정 자격 평가 cycle (9차 entry, `19b0f76` brief v1 → `386c552` 합의 BLOCKING 12 + Reviewer 격상 4 R-S1~R-S4 → `afd1a65` brief v1.1 + CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 단일 atomic commit, R-19 단계 (4) 직접 적용, Reviewer 권한 한계 8 → 9 격상 + (9) 신규 CLAUDE.md/roadmap.md 본문 정정 자격 boundary + (9-a)~(9-d) sub-boundary 발효)**. HEAD = 본 9차 정리 commit (commit 별도 사용자 명시 의무).
docs/INDEX.md:22:- ⭐⭐ **`docs/phase0/mvp1-pc1-d6-bypass-detection-ci-brief.md`** (190줄, 10장, 자기진단 8/8) — D-6 sub-cycle brief (scope/답습 출처 6/R-6+D-6+R-7(b) 흡수 매트릭스/ADR-011 매트릭스/실 구현 1 항목 [`pre-commit-bypass-detection.yml`]/Rollback 2/Evidence 3/합의 형태 권고/carry-over 3)
docs/INDEX.md:27:- ✅ 26번째 entry PC-1-T3 brief §10 D-6 carry-over 해소
docs/INDEX.md:36:- ⭐⭐ **`docs/phase0/g2-gp3-mvp1-evidence.md`** (~150줄, 6장, 자기진단 5/5) — GP-3 ADR-011 §2.1 (a)~(e) 5/5 충족 evidence 통합 (S-1 + S-3 + ST-2 + PC-1 Defense in depth + 31번째 entry 첫 PR PASS + multi-source 재기술 답습 + 자동 회귀 secret-hygiene-egress-redaction.yml nightly + (b1) 4 sub-cycle 통합 + R-S1 cascade 답습 + carry-over)
docs/INDEX.md:37:- ⭐⭐ **`docs/phase0/g2-gp5-mvp1-evidence.md`** (~110줄, 6장, 자기진단 5/5) — GP-5 ADR-011 §2.1 (a)~(e) 5/5 충족 evidence 통합 (Provider Liquidity 5-way + import-linter + provider scanner + AR-3 통합 + 첫 PR enforce x3 + scan(provider-url) PASS + multi-source 재기술 답습 + R-2 BLOCKING 답습)
docs/INDEX.md:51:- (변경) 50 file sed 일괄 정정 (160 위치, multi-source 재기술 답습): `ADR-008 §A.2 R1-2 / §2.6.4 R1-2 / §2.6.2 R2-1` → `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011` (GP-3 + GP-5 OAuth) / `ADR-008 차단조건 #6 + 부록 B` (docker secret)
docs/INDEX.md:75:- (변경) **`docs/architecture/implementation-runtime-roadmap-mvp1.md`** — 7 위치 cross-reference 정정 (line 137 §5.1 (c) cell GP-3+GP-5 + 205 ST-1 + 206 ST-2 + 207 ST-3 + 209 ST-5 + 283 carry-over status + 660 ST-3 9 sub-수단 매트릭스). 정정 형태: `ADR-008 §A.2 R1-2 / §2.6.4 R1-2 / §2.6.2 R2-1` → `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011` multi-source 재기술. 기존 §2.2 + §3.5 (carry-over status 외) + §4.5 + §4.7.3 + §5.1 (35+36 정정 cell 외) + §9 본문 변경 0건
docs/INDEX.md:76:- (변경) **`docs/architecture/mvp-1-to-6-entry-conditions-brief.md`** — line 93 §ADR-011 (a)~(e) 매트릭스 (c) cell GP-3 + GP-5 cross-reference 정정 (동일 multi-source 재기술)
docs/INDEX.md:89:- (변경) **`docs/architecture/governance-preconditions.md`** — 6 위치 cross-reference 정정 (line 106 / 343 / 488 / 498 / 508 / 523). `ADR-008 §A.2 R1-2 / §2.6.4 R1-2 / §2.6.2 R2-1` → `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011` multi-source 재기술 답습 (R-3 흡수)
docs/INDEX.md:112:- ⭐⭐⭐⭐ **`docs/phase0/mvp1-implementation-evidence-pass-activation-brief.md`** (v1 267줄 → v1.1 in-place 보강) — 24번째 entry carry-over (c) verbatim + (b1) 4 sub-cycle ADR-011 (a)~(e) 매트릭스 (17/20 완전 + 3/20 부분 + Defense in depth cross-cover 답습 R-5 흡수) + GP-3 5/5 + GP-5 5/5 매트릭스 (multi-source 답습 R-3 흡수 + R-S1 cross-reference 정정 carry-over (b2) 명문) + PASS 발효 형태 (α/α′/β/γ + 권고 (α)) + Rollback Trigger 10건 (R-MVP1-PASS-{1~5} v1 + {6~10} v1.1 신규 R-4 흡수) + D-1~D-5 사용자 결정 + 합의 형태 권고 (풀 3+1 + 외부 LLM 1+) + 자기진단 10/10. **v1.1 보강 = BLOCKING 6 + 권고 5 1pass 흡수 (R-1 § 정정 + R-2 GP-5 (c) R-S1 제거 + R-3 multi-source 재기술 + R-4 Trigger 5건 추가 + R-5 partial carry-over 명문 + R-6 D-5 paths-aware 우선 추가 + N-1 α′ 후보 + N-2 cross-reference + N-4 head SHA 9837298 명시)**
docs/INDEX.md:126:**자율 영역 evidence 수집** (PASS 효과 영향 0건): PC-1-T3 PoC + ST-2 nightly + (b1-AR3 develop)
docs/INDEX.md:134:- ⭐⭐ **`docs/phase0/friday-separate-evolution-tool-entry-brief.md`** (~280줄, 13장, 자기진단 8/8) — Hermes 식 자가진화 깊이 ↔ 자비스 4 invariant (헌법 8조 + ADR-011 §2.4 T3 + Boss = root of trust 아님 + Provider Liquidity 5조-2) 보존 양립 경로 = (D) 별도 툴 격리 채택. 4 경로 (A/B/C/D) 비교 매트릭스 + 형태 후보 2 ((P) 자체 코드 vs (Q) Hermes 도입) + 5 layer 격리 메커니즘 사전 정의 (filesystem ACL + workdir + endpoint + 메모리 + commit) + 진입 시점 stage gate (자비스 MVP-1 완료 후) + Rollback Trigger 5건 (R-Friday-1 ~ R-Friday-5: 격리 침범 / HW 영향 / invariant 침범 / R1 학습루프 폭주 / cycle 비용 자비스 본업 정지) + Evidence 의무 5건 + ADR-011 (a)~(e) 매트릭스 (2/5 본 brief 시점 충족 + 3/5 별도 cycle) + 사용자 결정 항목 D-1 ~ D-8 + 합의 형태 권고 (풀 3+1 + 외부 LLM 1+, 5/5 trigger 中 3/5 발화 = Reviewer-only 단축 불가) + Marvel narrative 정합 (Jarvis 안전 + Friday 실험) + 자기진단 8/8
docs/INDEX.md:146:**2026-05-27 세션 (31번째 entry: MVP-1 AR-3 첫 PR evidence 수집 — PR #2 draft, ADR-011 5/5 완전 충족 AR-3 영역, 중복 동작 race 0 확정, paths-aware risk 발견) 신규 등록 문서 1건 + 변경 1건 (fix commit `73ed20d` 별도) + 외부 effect 2건**:
docs/INDEX.md:148:- ⭐⭐⭐ **`docs/phase0/mvp1-ar3-first-pr-evidence.md`** (6장) — 첫 PR evidence carry-over 수집 완료 결과. 시점 (2026-05-27, `7c294bb` 직후) + PR #2 draft (https://github.com/jokwangwon/AI_development_tool/pull/2) + 첫 발화 (head `7c294bb`, 10 check_runs, 1 FAIL scan = secret-hygiene S-3 step + 1 미발화 R-4.1 paths 필터) + 원인 audit (AWSKeyDetector regex 19자 vs 20자 + r2-canary paths 매치 0) + 조치 2건 (사용자 결정: fixture 정정 + contexts 제거) + 재발화 (head `73ed20d`, **11/11 SUCCESS + mergeable CLEAN**) + R-MVP1-1.5-AR3 검증 매트릭스 (중복 동작 race 0 확정 — `enforce` x3 + `scan` x3 모두 분리 처리 + 모든 동명 PASS 의무 답습 / admin bypass 0 evidence / paths-aware risk 발견 carry-over) + ADR-011 (a)~(e) **5/5 완전 충족 AR-3 영역** + carry-over 6
docs/INDEX.md:166:- ⭐⭐⭐ **`docs/phase0/mvp1-ar3-branch-protection-applied-evidence.md`** (5장) — (b1-AR3) 사용자 admin scope 단계 7 적용 evidence. 적용 시점 (2026-05-27) + method (`gh api -X PUT branches/main/protection`) + 권한 (admin=True + owner=True) + R-MVP1-1.5-AR3-2a catalog 정정 매트릭스 (11 후보 = "workflow name + job name" 형식 → 실 GitHub check_run = "job name 만 8 unique", scan x2 + enforce x3 중복) + 적용 응답 body (8 contexts + strict + enforce_admins + approval 0 + allow_force_pushes false + allow_deletions false) + ADR-011 (a)(c)(e) 3/5 완전 + (b)(d) 부분 충족 + develop carry-over + 다음 단계 4 (첫 PR evidence / 중복 검증 / develop 적용 / brief 정정 본 commit 답습)
docs/INDEX.md:171:- (b1-AR3 첫 PR evidence): 첫 PR open 시 11 workflow 모두 status check 발화 + 모든 PASS 의무 + admin bypass 0 시도 evidence = ADR-011 (b)(d) 완전 충족
docs/INDEX.md:180:- ⭐⭐⭐ **`docs/phase0/mvp1-ar3-pr-auto-reject-brief.md`** (281줄, 10장) — AR-3 sub-cycle entry brief. R-3 BLOCKING 흡수 — 11 workflow 실 check name catalog 본문 채택 (workflow name + job name 조합, `Evidence / PASS Gate` workflow name `/` 포함 verify 의무 명문). R-7(c) 차등 분리 (R-MVP1-1.5-AR3-2a 도구 변경 = 단축 합의 / 2b T3 정책 신규 check = 풀 3+1 + 외부 LLM 1+). Claude scope vs 사용자 admin scope 명문 분리 (§1.1). 사용자 admin 적용 절차 (A) web UI + (B) gh CLI 안내 (§4.2). AR-1 + AR-2 통합 효과 + PC-1 + PC-3 + AR-3 결합 Defense in depth (§4.4). ADR-011 (a)~(e) 매트릭스 (3/5 합의 시점 + 2/5 사용자 admin 적용 시점). D-1~D-4 사용자 결정 + 7단계 cycle (6 + 사용자 admin 적용)
docs/INDEX.md:181:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-27-mvp1-ar3-pr-auto-reject.md`** (Reviewer-only 단축 합의, 7장) — ✅ **APPROVE (Reviewer-only 단축 합의)**. 5/5 풀 3+1 승격 trigger 0건 발화 검증 + entry 합의 verbatim cross-check 5 source (line 290 / line 113 / §2.4 line 229 / R-3 / R-7(c)) + 인프라 발효 cross-check (AR-1 부분 발효 + main/develop unprotected HTTP 404) + R-3 BLOCKING 11 catalog 본문 채택 (§3 표) + 변경 0건 의무 12/12 + ADR-011 (a)(c)(e) 3/5 본 합의 발효 + (b)(d) 2/5 사용자 admin 적용 시점 발효 + 자기진단 8/8
docs/INDEX.md:185:- (c) **MVP-1 Implementation Evidence PASS 발효 합의** — (b1) 4 sub-cycle 완료 = 진입 자격 자격 충족. **다음 cycle 후보** (ADR-011 §2.1 (a)~(d)+(e) 5/5 + conditions 해소 + 사용자 명시 별도 합의)
docs/INDEX.md:194:- ⭐⭐ **`docs/phase0/mvp1-st2-inotify-sidecar-brief.md`** (227줄, 10장) — ST-2 inotify sidecar 실 구현 sub-cycle brief. 23번째 entry audit 한정 패턴 답습 (인프라 8/8 발효 — docker-compose 137줄 + watch-secrets.sh 73줄 + Dockerfile + hermes-mock + 5 fixture + tool 258줄 + workflow ST-2 step line 663 + on.push.paths 필터 모두 Cycle 3+4 답습). R-5 BLOCKING 3 단계 evidence 발효 cross-check 명문 (3/3 단계 모두 이미 발효 자격 검증): (1) event 인지 = watch-secrets.sh inotifywait 6 event / (2) sidecar→메인 signal = status file + hermes-mock healthcheck / (3) 메인 fail-closed = tool line 199~212 docker inspect Health.Status 비교. R-7(a) framing 정정 entry brief v1.1 line 326 이미 흡수 답습 (본 sub-cycle 추가 정정 0건). R-MVP1-1.5-ST2-{1,2,3} Rollback Trigger 답습 유지. ADR-011 (a)~(e) 매트릭스 ((b)(c) 이미 발효 + (a)(e) 합의 시점 + (d) nightly schedule 추가). D-1~D-3 사용자 결정 (3/3 권고 채택)
docs/INDEX.md:195:- ⭐⭐ **`docs/review/3plus1-consensus-2026-05-27-mvp1-st2-inotify-sidecar.md`** (Reviewer-only 단축 합의, 7장) — ✅ **APPROVE (Reviewer-only 단축 합의)**. 5/5 풀 3+1 승격 trigger 0건 발화 검증 + entry 합의 verbatim cross-check 5 source (line 290 / §1 line 36 / §6 R-5 / §13.2 line 534 / entry brief v1.1 line 326) + 인프라 8/8 발효 cross-check (23번째 entry audit 한정 패턴 답습) + R-5 BLOCKING 3 단계 evidence 발효 source 명문 본문 채택 + 변경 0건 의무 14/14 + ADR-011 (a)(b)(c)(e) 4/5 본 합의 발효 + (d) 1/5 실 구현 단계 발효 + 자기진단 8/8
docs/INDEX.md:199:- (b1-ST2 후속) PoC evidence 수집 (사용자 자율): 첫 nightly schedule 발화 (UTC 03:00 = KST 12:00 익일) → `gh run list` 또는 GitHub Actions UI nightly run id 확인 → ADR-011 (d) 충족 evidence
docs/INDEX.md:209:- ⭐⭐⭐ **`docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md`** (303줄, 10장) — S-3 detect-secrets 부분 통합 실 구현 sub-cycle entry brief. 24번째 entry R-4 BLOCKING (plugin identifier 5종 정확 mapping + `--baseline` 미사용 CI assertion) 흡수 매트릭스 + 현 상태 audit (`tools/secret_scanner.py` S-1 발효 유지 + `detect-secrets` 0 패키지) + 실 구현 5 항목 + ADR-011 (a)~(e) 5/5 + R-MVP1-1.5-S3-{1,2,3} Rollback Trigger (Tier-2/3 확장 풀 3+1 / baseline 영구 금지 / S-1 답습 영구 의무) + Evidence + D-1~D-5 사용자 결정 + 합의 형태 권고 (단축 합의 Reviewer-only) + 자기진단 8/8. 사용자 결정 5/5 답습 (D-1~D-4 권고 채택 + D-5 default 답습). plugin allowlist Tier-1 답습 5종 hardcoded list (`AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` / `HexHighEntropyString` / `PrivateKeyDetector`) 본문 채택
docs/INDEX.md:210:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md`** (Reviewer-only 단축 합의, 6장) — ✅ **APPROVE (Reviewer-only 단축 합의)**. 5/5 풀 3+1 승격 trigger 0건 발화 검증 (① 새 권위 결정 0 / ② Tier-2/3 자동 확장 0 / ③ PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 5조건 자동 충족 선언 0) + entry 합의 verbatim cross-check 5 source (line 290 / §1 line 36 / §6 R-4 line 73 / §5.1 line 323~325 / roadmap §3.6.3 line 289) + 변경 0건 의무 12/12 cross-check + ADR-011 (a)(c)(e) 3/5 본 합의 발효 + (b)(d) 2/5 실 구현 단계 발효 + 자기진단 8/8
docs/INDEX.md:228:**2026-05-27 세션 (26번째 entry: MVP-1 PC-1-T3 mandatory enforcement 실 구현 sub-cycle, (b1) 4 sub-cycle 첫 진입, Reviewer-only 단축 합의 APPROVE) 신규 등록 문서 5건 + 변경 2건**:
docs/INDEX.md:230:- ⭐⭐⭐ **`docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md`** (288줄, 10장) — PC-1-T3 mandatory enforcement 실 구현 sub-cycle entry brief. 24번째 entry BLOCKING R-2 (PC-1 (b)(d) 재분류) + R-6 (PC1-1 탐지 경로 (i)(ii)(iii)) + R-7(b) (PC1-2 차등) + N-1 (PC-1 단독 우회, 결합 효과 명문) + N-2 (T3 명칭) 흡수 매트릭스 + 현 상태 audit + 실 구현 5 항목 + ADR-011 (a)~(e) 5/5 + Rollback Trigger + Evidence + D-1~D-6 사용자 결정 + 합의 형태 권고 (단축 합의 Reviewer-only) + 자기진단 8/8. 사용자 결정 6/6 답습 (D-1~D-4 권고 채택 + D-5/D-6 default 답습)
docs/INDEX.md:231:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md`** (Reviewer-only 단축 합의, 175줄) — ✅ **APPROVE (Reviewer-only 단축 합의)**. 5/5 풀 3+1 승격 trigger 0건 발화 검증 (① 새 권위 결정 0 / ② Tier-2/3 자동 확장 0 / ③ PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 5조건 자동 충족 선언 0) + entry 합의 verbatim cross-check 7 source (line 292 / §1 line 38 / §6 R-2/R-6/R-7(b) / §10 N-1/N-2) + 변경 0건 의무 10/10 cross-check + ADR-011 (a)(c)(e) 3/5 본 합의 발효 + (b)(d) 2/5 실 구현 단계 발효 + 자기진단 8/8
docs/INDEX.md:232:- ⭐⭐⭐ **`CONTRIBUTING.md`** (신규 134줄, 6장) — dev onboarding workflow + PC-1-T3 mandatory enforcement 명문 (의무 + 우회 차단 Defense in depth 3 계층 PC-1+PC-3+AR-3) + Rollback Trigger R-MVP1-1.5-PC1-1 명문 + PR workflow + `.pre-commit-config.yaml` 본문 변경 차등 R-7(b) + 합의 cycle 답습 + TDD 답습 + 참조 문서
docs/INDEX.md:234:- ⭐⭐ **`tools/pre_commit_install_audit.sh`** (신규, chmod +x) — PC-1-T3 bypass detection 3 탐지 경로 통합 verify (R-6 BLOCKING 흡수): (i) `.git/hooks/pre-commit` framework marker grep + (ii) `pre-commit` 명령 PATH 가용 + (iii) `.git/pre-commit-audit/install.log` 존재. Exit 0 = 3/3 PASS / Exit 1 = bypass 의심 (R-MVP1-1.5-PC1-1 발화 자격)
docs/INDEX.md:236:- (변경) **`requirements-dev.txt`** — `pre-commit==4.0.1` 추가 (PC-1-T3 PoC 자격 충족). 기존 import-linter / rfc8785 / jcs / pytest / pytest-cov 본문 변경 0건
docs/INDEX.md:259:- ⭐⭐⭐ **`docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`** (v1 506줄 → v1.1 보강 570줄, +64) — MVP-1 GP-3 + GP-5 1.5차 보강 4 sub-수단 (S-3 detect-secrets 부분 통합 + ST-2 inotify sidecar + PC-1-T3 mandatory enforcement + AR-3 통합 PR auto-reject) **진입 합의 entry brief**. 본 cycle 합의 발효 = 4 sub-수단 *채택 결정 발효 자격* + 실 구현 sub-cycle 4개 진입 권한 발효 자격. v1.1 = BLOCKING 7 + 권고 12 1pass 흡수 (ceremony-inflation 차단). 본 brief 자체 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 변경 0 / ADR 본문 갱신 0 / 헌법 0 / roadmap 본문 변경 0 / Tier-2/3 catalog 확장 0 / threshold 고정 0
docs/INDEX.md:264:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md`** (Reviewer 통합 합의 305줄) — ✅ **APPROVE WITH CONDITIONS (BLOCKING 7 + 권고 12)**. 3-way 일치 BLOCKING 3 (R-1 ADR-011 (a)~(d)+(e) / R-2 PC-1 (b)(d) 재분류 / R-3 AR-3 check name mapping) + 2-way 격상 BLOCKING 2 (R-4 S-3 plugin identifier / R-5 ST-2 fail-closed) + ⭐⭐⭐ **Reviewer 단독 격상 R-S1 (B-5 + raw line-level verify — ADR-008 §A.2 = "Hermes JSONL Export 검증" + §2.6 sub-section 부재 + R1-2/§2.6.4 식별자 ADR-008 본문 0건, 다중 source 권위 chain 손상 확정)** + 1-Agent BLOCKING 2 (R-6 PC1-1 탐지 / R-7 Trigger 3 정정). cross-vendor 일치 매트릭스 (codex 14 finding 모두 흡수). 메타 자기진단 8/8 통과
docs/INDEX.md:270:- (c) MVP-1 Implementation Evidence PASS 발효 합의 (4 sub-cycle 완료 + ADR-011 §2.1 (a)~(d)+(e) 5/5 + conditions 해소 + 사용자 명시 별도)
docs/INDEX.md:276:- ⭐⭐ **`docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md`** (audit brief, 1-agent 직접 ceremony-inflation 회피) — §1 진입 합의 3건 상태 (gp3 + gp5 + backlog#6, `f40423f` push 완료) + §2 실 구현 audit (21 도구 / 11 workflow / .pre-commit / .importlinter / adapters/llm placeholder) + §3 DRAFT 잔재 + deferred 영역 (1.5차 보강 / T3 / Tier-2/3) + §4 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (양 GP 5/5 충족, 단 conditions 미해소 = PASS 발효 미적격) + §5 4 진입점 후보 (a~d) 권고 + §6 권위 한계 (수단 결정 0 / threshold 고정 0 / 실 구현 0 / PASS 발효 0)
docs/INDEX.md:277:- ⭐⭐ **`docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md`** (Reviewer-only 단축 합의 보고서) — ✅ **APPROVE (단축 합의 — Reviewer-only)**. 5/5 풀 3+1 승격 트리거 0건 발화 (① 새 권위 결정 0 / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0) + 후속 3 합의 본문 흡수 cross-check (line 819~821) + cross-check verbatim 5/5 (line 826 / 287 / 477 / §5.5 / §8) + ADR-011 답습 정확. 발효 효과 = `roadmap-mvp1.md` DRAFT → APPROVED 권위 발효 (840줄 본문 변경 0건, line 826/827 + §9 변경 이력 한정)
docs/INDEX.md:287:- ⭐⭐⭐ **`docs/phase0/jarvis-mvp1-g1-n-3-adr-008-sip-adr-012-prime-consensus-entry-brief.md`** (v1 `b55e0c9` 561줄 → **v1.1 `c9493c0` +337/-381**) — (g1-N-3-adr-008+sip+adr-012') HIGH cycle entry brief. (g1-N-3') 합의 §8.2 line 273 HIGH carry-over 직접 발효 + Reviewer 권한 한계 (10-e) 직접 발효. **v1.1 보강**: BLOCKING 11 + R-S1~R-S3 verbatim 100% + 권고 9 흡수 + NOTE 18 + 기각 4 + 결합 형식 (f) cross-ref block 만 채택 + ADR-011 line 245 형식 채택 (사용자 명시 직접 확인) + 4 source 확장 (R-S1 hermes-not-root 추가) + (P4)/(11)/(g1-N-4) 기각 + chain 영구 종결 의무 + §0/§10.1 13→15 항목 1:1 매핑 + §10.6 7→9 조건 확장 + §9 정직성 18→22
docs/INDEX.md:288:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-g1-n-3-adr-008-sip-adr-012-prime.md`** (풀 3+1 BLOCKING 11 + Reviewer 단독 격상 R-S1~R-S3 + 권고 9 + NOTE 18 + 기각 4, 235줄) — **APPROVE w/ COND**. **3-way Consensus 4** (C-1 (P4) 기각 / C-2 framing 정정 / C-3 (a) 자동 채택 차단 / C-4 ADR-011 line 245 형식 모법) + **R-S1 ⭐⭐⭐ CRITICAL** (hermes-not-root-of-trust-runtime.md line 23/176/1040 = gov §1.1 line 78 명문 4 source *외 유일* 추가 동형 source 신규 식별, Agent C 단독 + Reviewer raw cross-check 직접 verify, bash grep verify = ADR-012 + 본 source 단 2 파일) + R-S2 헌법 line 80 self-inconsistency ((g1-O') 별도 cycle carry-over) + R-S3 gov §1.1 line 78 정의 범위 자체 정합성 ((10-f) 답습 별도 cycle DEFER) + **D-1 결합 형식 권고**: (f) cross-ref block 만 최강 + (b) 4 cycle 분리 차순 + (h) [신규] NOTE 보존 + **(11) sub-boundary 신설 *기각* 본 합의 발효** ((10-k) 1회 한정 답습 직접 위반 risk 차단)
docs/INDEX.md:290:- ⭐⭐⭐ **`docs/decisions/ADR-008-hermes-adoption-decision.md`** (본 후속 세션 변경, `f20fce3`, **(ii-γ)**) — line 86 (관련 문서 § 내부) cross-ref block 추가 (R-S3 CRITICAL 답습, 본문 verbatim 변경 0건). ADR-008 = ADR-011 직접 모법 (ADR ↔ ADR 부록 B Amendment 패턴)
docs/INDEX.md:297:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-g1-n-3-prime-high-integrated-consensus.md`** (풀 3+1 BLOCKING 14 + Reviewer 단독 격상 R-S1~R-S6 + 권고 11 + NOTE 22 + 기각 5, 309줄, **본 세션 10차 ((g1-N-3') HIGH 통합 cycle)**) — **APPROVE w/ COND**. 3 Agent 모두 APPROVE w/ COND 일치, 정면 충돌 0건 = 강한 정합성. **Reviewer 단독 격상 6 (raw line-level direct cross-check)**: ⭐⭐⭐ **R-S1 (Agent A A-S1 + Agent C C-B1 통합 + Reviewer raw cross-check 직접 확인)** brief §3.1 헌법 line 80 verbatim 인용 *근본적* 부정확 (4 종류 mismatch 동시: 항목 1 본문 축약, 항목 2 완전 누락, 항목 3 본문 변경, 항목 4 *근본적* 본문 변경 — (g1-N-1) commit `148fbbe` *실제 본문* line 77~80 4 항목 vs brief 3 항목 잘못 인용) / ⭐⭐⭐ **R-S2/R-S3/R-S4** system-identity-prequel.md (line 93/175) + ADR-008.md (line 86) + ADR-012.md (line 6/61/579/665) 누락 = gov §1.1 line 78 명문 4 source 직접 답습 ↔ 본 cycle "5 파일 통합" framing 불완전 (별도 cycle DEFER 권고) / ⭐ **R-S5** ADR-010 line 176 ADR-012 cross-ref "Layer 5" 누락 ((P1)(P2)(P3) 외, (ii-b) 범위 외 명문 의무) / ⭐ **R-S6** brief §3.2 ADR-011 line 6 순서 부정확 + system-identity-prequel §3 참조 누락. **3-way Consensus 4**: 결합 진입 R-13 (4-c) / (γ-2) chain / (v-β) 명명 / gov §1.1 (ii-c). **Reviewer 권한 한계 (10) 신규 격상 본 합의 발효 — 11 sub-boundary 확장** ((10-a)~(10-k), B-B3 + C-rec-2 통합). **기각 5건**: (g1-N-4) 새 cycle 시리즈 framing + (c) (P3) 통일 즉시 + gov §1.1 (ii-a)/(ii-b)/(ii-d) + (iv-β) llm-providers 명명 보강 + (vi-α) §11.4.2 본 cycle 포함 정정
docs/INDEX.md:311:- ⭐ **`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-provider-liquidity-deepdive.md`** (풀 3+1 BLOCKING 13 + 권고 17 + NOTE 12, 기각 0, `a9e1e88`, 301줄, **본 세션 3차**) — APPROVE w/ COND, R-13 ⭐ Reviewer 단독 (ADR-011 line 6/245 verbatim "헌법 제5조 (Provider Liquidity)" / "제5조 관용 (Provider Liquidity, 비협상)" 직접 권위 매핑 발견) + R-3 ⭐ 3 에이전트 일치 (4 수준 framing self-citation anchor + 시간축 missing dimension + 비교 자격 1/4)
docs/INDEX.md:313:- ⭐ **`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md`** (풀 3+1 BLOCKING 16 + 권고 21 + NOTE 24, 기각 0, 397줄, **본 세션 4차 (f-K)**) — **APPROVE w/ COND**. 3 Agent 모두 REVISE 일치 (불일치 0). Reviewer 단독 격상 3건: R-S1 (A-S1 격상, Phase 3 raw `conversion/qwen.py:299-300` cross-check → P3-F1 = 시점 부정합 finding ≠ "GGUF 가족 본질 부정") + R-S2 (C-B3 격상, ADR-011 §6 line 212 "Provider Liquidity 영향 무관" vs line 6/245 직접 권위 매핑 내부 비대칭) + R-S3 (B-S5 ⭐⭐ 격상, brief §0 "하지 않는 것" 12 항목 vs §9.1 차단 6 항목 비대칭 self-consistency 정직성 risk). 2 Agent 일치: R-1 분류 *기준* 단일축 부재 (A+C) / R-2 self-citation 후속 매핑 (B+C) / R-3 Phase 3 R-5 답습 누락 (B+C)
docs/INDEX.md:314:- ⭐ **`docs/phase0/jarvis-mvp1-format-family-classification-option-a-adoption-consensus-entry-brief.md`** (v1 `fc6731e`, 397줄 → **v1.1 `bdcc3a6`, 537줄 +255/-115**, **본 세션 5차 ((g1-A) 채택 cycle)**) — format 합의 §7.1 (A) 옵션 채택 자격 평가 entry brief. **(g1-A) = 4 가족 분류 현 상태 유지 + framing 임시성 명문만 + MVP-1·메모리 본문 변경 0건** 의 채택 자격 평가. **v1.1 보강**: BLOCKING 16 verbatim 본문 직접 반영 100% (R-21 답습) + 권고 18 본문 직접 반영 또는 NOTE carry-over + NOTE 24 → **35 비중복 carry-over + 본 cycle 신규 5 (N-25~N-29) = 40 by-reference only** (R-9 = R-S3 정정 36 → 35) + §7.1 **(g1-N) 헌법 5조 본문 미세 보강 + (g1-O) ADR-011 line 212 본문 미세 보강 옵션 신규** (R-2) + §9.6 신규 (R-6 — 후속 cycle 본 brief 인용 by-reference *진술* only) + §7.5 우선순위 권고 신규 (R-29) + §11 위치 분리 §11.1+§11.2 (R-10) + §3.3 메모리 line 12~17 verbatim 6 행 (R-S1 정정 chain) + §3.1 ADR-011 매핑 4 차원 분리 (R-S2) + §0 #12 + §10 NOTE 36 → 35 (R-S3)
docs/INDEX.md:315:- ⭐ **`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md`** (풀 3+1 BLOCKING 16 + 권고 18 + NOTE 29, 기각 0, 343줄, **본 세션 5차 ((g1-A) 채택 cycle)**) — **APPROVE w/ COND**. 3 Agent 모두 APPROVE w/ COND 일치, 정면 충돌 0건 = 강한 정합성. **Reviewer 단독 격상 3 (raw line-level direct cross-check)**: ⭐⭐⭐ **R-S1 (C-S4 격상, 가장 큰 finding)** 메모리 `feedback_provider_liquidity` 실제 line 14 verbatim "최소 2 provider always-on 원칙", 본 brief v1 + 선행 format brief v1.1 §3.4 + format 합의 R-13 모두 "line 13" 인용 오류 = line offset 부정합 chain (정정 chain carry-over 의무) / ⭐⭐ **R-S2 (B-B1 + B-S1 격상)** 헌법 5조 line 40~46 verbatim = "코드 품질 원칙" (Provider Liquidity 직접 본문 부재), ADR-011 line 6/245 *매핑* 의존, format 합의 R-S2 (ADR-011 *내부* 비대칭) 의 *상위 단계* 비대칭 / ⭐⭐ **R-S3 (B-B8 격상)** §0 #12 NOTE 36 → **35 비중복** 정정 (Provider Liquidity 12 가 format 24 *내포 합산*). **2+ Agent 일치 BLOCKING 2**: R-1 (A-B1 + B-B2 + C-B1 **3-way**) (g1-A) 추가 산출 boundary 모호·자명성·재서술 self-위반 risk / R-2 (A-B2 + C-B2) §7 매트릭스 비대칭 + (g1-N)/(g1-O) 권위 본문 미세 보강 옵션 누락
docs/INDEX.md:316:- ⭐⭐ **`docs/phase0/jarvis-mvp1-constitution-article-5-2-provider-liquidity-new-clause-consensus-entry-brief.md`** (v1 `6f64491`, 542줄 → **v1.1 `58e06d5`, 780줄 +487/-249**, **본 세션 6차 ((g1-N) 헌법 5조-2 신설 자격 평가 cycle, 헌법급 변경 R-9 답습 영구 의무 cycle)**) — (g1-A) 합의 §7.1 (g1-N) 옵션 채택 자격 평가 entry brief. 사용자 명시 "(g1-N)" + 정공법 + 범위 **"5조-2 (Provider Liquidity 조항) 신설 분리"**. 본 cycle = 5조-2 신설 *제안 (proposal)* + 자격 평가 cycle 한정, 실 헌법 본문 변경 = (g1-N-1) 별도 단계 + 사용자 명시 의무 (R-9 답습 영구). **v1.1 보강**: BLOCKING 22 verbatim 본문 직접 반영 100% (R-21 답습) + 권고 17 본문 직접 반영 또는 §11 NOTE carry-over + NOTE 29 → **54 by-reference only** (carry-over 29 + 본 cycle 신규 25 N-30~N-54) + **§2.5 ADR-008 부록 B verbatim 신규** (R-S3 답습) + **§3.5 후보 7×ADR-011+ADR-008 = 42 cell 매트릭스 신규** (R-24 답습) + **§4 본문 후보 4 → 7 확장** ((v) ADR-011 line 6 답습 / (vi) 1 줄 / (vii) 메모리 line 12~17 7 항목 답습, R-8) + **§4.8 위치 후보 3 → 4 확장** ((d) ADR 신설 우회, R-9) + **§5 긴장 4 → 5** + **§6.3 Reviewer 권한 한계 7 → 8 격상** ((8) 결합 cycle 진입 자격 평가 자격 0, R-7) + **§8.0 4 cycle chain trace 신규** (R-23) + **§9 정직성 18 → 22** (R-S4 + R-17 신규) + §10.1 §0 1:1 매핑 R-S5 정합화 + §12 위치 분리 (§12.1 변경 일람 + §12.2 다음 단계)
docs/INDEX.md:320:- ⭐⭐⭐ **`docs/constitution/PROJECT_CONSTITUTION.md`** (본 세션 변경, `148fbbe`) — **line 75~81 5조-2 신설** (Provider Liquidity 비협상 원칙 4 항목, 메모리 line 7+12+14 + ADR-011 line 6 verbatim 답습) + line 82+ 9조 +7 line offset 이동 + line 104~105 종결 명문 +7 이동. 후속 조항 *번호* 정정 0건 (R-S3 답습 강한 후보 자격 evidence)
docs/INDEX.md:321:- ⭐⭐⭐ **`docs/phase0/jarvis-mvp1-g1-n-2-adr-011-mapping-correction-consensus-entry-brief.md`** (v1 `8207f55`, 488줄 → **v1.1 `3bdb1be`, 519줄 + ADR-011 line 6/245 매핑 정정 동시 atomic commit**, **본 세션 8차 ((g1-N-2) cycle)**) — (g1-N-1) commit 후속 carry-over cycle. R-9 답습 영구 의무 (g1-N-2) carry-over 직접 발효 + Reviewer 권한 한계 (1) "ADR-011 §6 본문 정정 자격 0" 예외 자격 발효 시점 (R-13 (4-c) 동형 패턴). **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit** (`docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)`). 임시 stale 정합 회복 cycle ((g1-N-1) commit ~ (g1-N-2) commit 사이 N-61 carry-over 답습 완료)
docs/INDEX.md:322:- ⭐⭐⭐ **`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md`** (풀 3+1 BLOCKING 10 + 권고 10 + NOTE 11, 기각 0, 303줄, **본 세션 8차 ((g1-N-2) cycle)**) — **APPROVE w/ COND**. **Reviewer 단독 격상 3 R-S1~R-S3 (raw line-level direct cross-check)**: ⭐⭐⭐ R-S1 (line 245 entire verbatim 부분 추출 — bullet + path + 8조 prefix 포함, 가장 큰 finding) + ⭐⭐ R-S2 (헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off 신규 발효 — (g1-N-3') 별도 cycle 의무 carry-over 영구) + ⭐⭐ R-S3 ("비협상" 명문 추가 boundary = 헌법 line 75 verbatim 직접 답습 한정). 2+ Agent 일치 BLOCKING 2 (R-1 + R-3)
docs/INDEX.md:323:- ⭐⭐⭐ **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (본 세션 변경, `3bdb1be`) — **line 6**: "헌법 제5조 (Provider Liquidity)" → "**헌법 제5조-2 (Provider Liquidity, 비협상)**" + **line 245** (entire verbatim): "`- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)`" → "`- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), **제5조-2 관용 (Provider Liquidity, 비협상)**`". Reviewer 권한 한계 (1) 예외 자격 발효 시점, 다른 cycle 의 ADR-011 §6 본문 정정 자격 0 영구 답습
docs/INDEX.md:325:- ⭐⭐ **`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-3-claude-md-roadmap-md-correction.md`** (풀 3+1 BLOCKING 12 + 권고 16 + NOTE 10 신규, 기각 0, 423줄, **본 세션 9차 ((g1-N-3) cycle)**) — **APPROVE w/ COND**. **Reviewer 단독 격상 4 R-S1~R-S4 (raw line-level direct cross-check)**: ⭐⭐⭐ R-S1 (A-S2 격상, brief §2.3 line 143~146 라벨 ↔ §4.1 (i)~(iv) 매트릭스 내부 모순, line 143/144/145 (i) → (iii)/(ii)/(iii) 라벨 정정 의무) + ⭐⭐ R-S2 (A-S1 격상, CLAUDE.md 본문 251줄 grep "Provider Liquidity"/"5조-2"/"제5조" verbatim **0 matches** 정량 evidence — 헌법 5조-2 신설 사실 *전무* 반영) + ⭐⭐ R-S3 (헌법 line 80 + ADR-011 line 212 + hermes-adoption-design-v3.md line 13 3-way trade-off carry-over 영구 — (g1-N-3') / (g1-O) / (g1-N-3-hermes) 3 후속 cycle 의무) + ⭐⭐⭐ R-S4 (C-S1 격상, provider-agnostic-memory-skill-design.md grep "Provider Liquidity" = **19 위치** + line 1292 "**Provider Liquidity 4-way Multi-layer Defense**" §11.4.2 헌법-동급 권위 → (g1-N-3-pamsd) 신규 분리 HIGH carry-over + MEMORY.md cleanup depth 4 cycle 누적). **4-way 일치 BLOCKING 1 (R-1 = §1.4 ↔ §6.3 분해 매핑 표 본문 부재, A-B1 + B-B3 + B-S2 + C-B3)** + 2+ 일치 BLOCKING 2 (R-10 anchor depth limit 9-cycle 비추론 차단 + R-11 framing 통일)
docs/INDEX.md:326:- ⭐⭐ **`CLAUDE.md`** (본 세션 변경, `afd1a65`) — **line 244** ADR-011 entry: "**헌법 8조 본질** = 안전 결과. R-4~R-7 모법, ..." → "**헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질** = 안전 결과 + Provider Liquidity. R-4~R-7 모법, Hermes ≠ root of trust, 자동 학습 vs 자동 정책 변경 분리(T1/T2/T3). **상위 권위 매핑 답습 (ADR-011 line 6/245 + 헌법 line 75~80)**". (i) 최소 정정 채택 = §1 SDD / §7 의존 표 / §8 line 233 변경 0건 (Reviewer 권한 한계 (9-b) 답습, (ii)/(iii) carry-over by-reference only)
docs/INDEX.md:333:- ⭐⭐⭐ **(Phase 3.5 (g) 측정 성공 cycle raw) `docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-*.{txt,log,json}` 20 파일** (본 세션 5차 14번째 entry) — **본 프로젝트 최초 측정 성공 cycle**. bartowski/Qwen_Qwen3-Next-80B-A3B-Instruct-GGUF Q4_K_M (45.38 GiB) 다운로드 (29m22s @ 26.4 MB/s) + 부분 호환 tensor name (ssm_dt.bias ✓ / ssm_ba.weight ⚠️ / ssm_conv ⚠️ / 6 중 4 일치) 에도 **model load + 측정 성공**: decode-161tok prompt 177.9 / decode 32.3 / prefill-2k prompt 971.9 / decode 31.5 t/s. **⭐⭐⭐ Ollama Phase 1 (7.83 decode mean) 대비 ~4.07× 격차 (llama.cpp 빠름) — F2 가설 ('Ollama 효율성') *역방향 강한 evidence***. R-1 anchor 12회 모두 hash `ce95c475...` 일치 (Phase 1·2·3·3.5 누적 silent 교체 0건). R-7 격리 확정 (apt 변동 0). llama.cpp fallback/graceful tensor name resolution 가설 신규 carry-over
docs/INDEX.md:347:- ⭐⭐⭐ **((R4-body) 본문 정정 4 위치 commit) `34c096c`** (**19번째 entry**) — **본 프로젝트 최초 MVP-1 합의 본문 *직접* 정정 cycle 완주**. Edit 4건 적용 역순 (R-S4 발효): (1) `docs/phase0/jarvis-mvp1-local-boss-design-brief.md` line 141 (M3 매트릭스) "llama.cpp ↔ Ollama 동급" → "llama.cpp > Ollama" + 4 차원 격차 (~3.29~3.92× / ~3.24~3.38× / ~24× / ~3.65~3.77×) + (k) 별도 + Provider Liquidity 약화 0건 / (2) 동 brief line 124~125 (🔴 R4 section, multi-line) "llama.cpp ↔ Ollama 동급 후보" + "~31 tok/s" → "llama.cpp > Ollama 확정" + Qwen3-30B-A3B 49.6 vs Ollama 14.69~15.29 + ~3.24~3.38× + Ollama MoE 공개 confirmed + prefill ~24× outlier + R4 원본 ~31 t/s = (g) Qwen3-Next-80B SSM hybrid ~4% 격차 정합 + (k) 별도 / **(3) 동 brief line 126 vLLM section verbatim 100% 보존 (Edit 0건) ⭐⭐⭐ R-S1 발효** / (4) 동 brief line 20 (R4 표) 4 차원 격차 분리 + (k) 별도 / (5) `docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` line 63 (R4 행) "llama.cpp ↔ Ollama 동급" → "llama.cpp > Ollama" + 49.6/32.3/14.7~15.3 + ~3.24~3.38× + ~4% 정합 + (k) 별도. cross-check verify: 정정 이전 framing 잔존 0건 ✓ / R4 referent 5 위치 (MVP-1 brief line 161 + MVP-1 합의 보고서 line 52/79/85) 모두 verbatim 보존 ✓ / 헌법 / ADR-011 / 다른 ADR / 다른 architecture / guides / CLAUDE.md 본문 변경 0건 (R-9 답습 영구) ✓ / 본 cycle 정정 영향 file 정확히 2개 ✓ / password literal 0건 (R-S2 발효) ✓ / Provider Liquidity (헌법 5조-2 비협상) 약화 0건 ✓ / R-1 anchor 25회 누계 일관 (sudo 1회 R-S4 발효 자격)
docs/INDEX.md:398:**이전 후속 64 상세** (참고용 보존): 2026-05-20 후속 64 (**⭐ Group I (Hermes-originated commit auto-reject) 풀 3+1 합의 *완료* — 외부 GPT-5.5 응답 회수 + brief v2 보강 + Agent A/B/C 병렬 독립 + Reviewer 교차 비교 + 합의 보고서 파일화 + commit + push + 세션 종료 메타**). **신규 등록 문서 2건**: `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-response-gpt.md` (`f6c6d5a`, GPT-5.5 응답 — 입력 한정) / `docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md` (`f6c6d5a`, 합의 보고서) + brief v2 보강 (`docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md`). **합의 판정**: Group I = T3 보안 enforcement → 풀 3+1 의무 / Reviewer-only 부적격 (만장일치). **외부 5 보강점 5/5 채택** (positive allow-list·runtime=sensor·`.git/`=ACL 책무 = BLOCKING / GHES≠GitHub.com / FP통제 조건부). **BLOCKING 6** (positive allow-list / runtime=sensor·reject=Hermes 밖 external enforcement / credential boundary 실분리 전제 / host 밖 anchor 의무 / R-I-CONFIG-CHANGE=T3 / `.git/`=filesystem ACL 책무) + 조건부 3 (observe≠발효·FN우선 / negative-control-only / framing N1). **framing N1** (외부 제안 명칭이 수단[credential isolation]을 명칭 고정 → ADR-011 means/ends 저촉 → 전면 재정의 보류). **⭐ 핵심 발견**: 현 G3 본문 line 448/784 = metadata 기반 single-author negative detection → positive allow-list = 결함 교정 (본문 교정 별도 단계, brief 금지 G3 본문 변경 0건과 양립). **신규 합의 1건 (29 → 30 합의)** — 권위 조건 = 6 BLOCKING + 3 조건부. 합의 = 추론적 검증(권고) 한정 (실 결정/구현 = 사용자 명시 + Backlog #6). **사용자 명시 금지 영구 답습 (모두 0건)**: G3 본문 교정 자동 진입 / Hermes-originated commit 차단 구현 / git hook / GitHub ruleset / CI workflow / Hermes runtime / Hermes upstream / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 / threshold 고정 / MVP-1 exit / Phase α defer-lockdown 변경. **다음 세션 추천 시작점 (자동 진입 0건)**: G3 line 448/784 metadata detection 결함 교정 brief (positive allow-list/credential boundary/external enforcement 중심 검토). 대안 = Hermes PR·approval auto-reject 신규 단위 G1 / Group I 2차 vendor 입력 / GP-5 C-2 완전 해소 = facade real P1 v2 (Backlog #4) / 세션 종료. **핵심**: Group I = G3 §2.2 #20 (합의 결과 silent override 차단) 의 *git commit 차원 enforcement* + Group α C-2 (AI agent self-approval 차단 = Group I 결합 필수) + AR-3 × Group I Defense in depth 3-layer (branch protection / commit auto-reject / filesystem ACL). **합의 형태 판정 = T3 보안 enforcement 영역 → 풀 3+1 의무 / Reviewer-only 단축 부적격** (트리거 #2 BLOCKING + #5 핵심 제약 #1 Hermes ≠ root of trust 직결 + #7 외부 LLM cross-vendor blind 미충족 + §4 self-reference 순환 권위 구조). 기존 외부 응답 2건 (`2026-05-13`) = AR-3 중심 → Group I 식별·차단 thin → **Group I 전용 외부 LLM direct review 필요** (10 질문). **풀 3+1 합의 = 외부 응답 회수 후 진입** (자동 진입 0건). **합의 신규 0건** (brief + 의뢰서 = 입력 정비, 합의 미발효 — 합산 741 유지 / 29 합의). **사용자 명시 금지 영구 답습 (모두 0건)**: Hermes runtime 실 구현 / 실 차단 hook 구현 / git hook 구현 / CI workflow 변경 / GitHub ruleset 변경 / server-side enforcement 구현 / Hermes upstream 변경 / 수단 결정 / threshold 고정 / Operational Readiness PASS / Hermes PMO 격상 / MVP-1 exit / Phase α defer-lockdown 변경. **다음 단계 (자동 진입 0건)**: 외부 LLM 응답 회수 → Agent A/B/C + Reviewer 풀 3+1 합의 → Group I 진입 여부 판단 / 또는 세션 종료.
docs/INDEX.md:438:**이전 후속 22 상세** (참고용 보존): 2026-05-16 후속 22 (**Phase α-1 + α-2 + α-3 *Local Validation Evidence* 기록 (옵션 (A)) + 2 commit chain (evidence + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 + α-2 + α-3 실제 병렬 구현을 시작해주세요. R-4 + R-5 + R-7 실제 구현. CI workflow / runtime code / Operational Readiness PASS / Hermes PMO 격상은 하지 마세요. 각 Phase 변경 commit 분리 + 구현 후 local 검증 결과 보고." → 발견: R-4+R-5+R-7 본문 = 이미 구현 + Layer C PASS 답습 → "옵션 (A)로 진행" — local 검증 결과 자체를 실 진입 완료 evidence 로 고정 + 본문 변경 0건). **2 commit chain**: (1) `7b3d40a` evidence 문서 (486줄, 11 섹션) / (2) 메타 commit. **핵심 framing**: Stage 3 (`7917e4a`) 발효 후속 — R-4+R-5+R-7 본문 = *이미 구현됨* (1192줄 13 file, brief 명세 100% 일치) → 본 evidence = local 검증 결과 12/12 PASS 기록 한정 (합의 보고서 아님). **사용자 명시 8 금지 위반 영구 답습**: R-4/R-5/R-7 본문 수정 / 새 도구 / 새 fixture / 새 docker block / CI workflow / runtime code / Operational Readiness PASS / Hermes PMO 격상 = 0/8. **합산 12/12 Local 검증 PASS** ✅: Phase α-1 R-4 = 8/8 (3 scanner × pass+fail × mode 분기 + 자기 검증) / Phase α-2 R-5 = INI 구조 8 항목 통합 PASS (lint-imports = dev-dep Layer C `25728590916` 답습) / Phase α-3 R-7 = 3/3 (image layer clean + layer leak + restart recovery sha256 일치). **3 Phase 본문 = 이미 구현됨 답습**: R-4 829 (3 file) + R-5 35 (1 file) + R-7 328 (9 file) = 1192줄 13 file. **변경 0건 검증**: `git status` clean + 8 금지 영역 위반 0/8 + 추가 catalog/forbidden/block/threshold/event enum/facade real/ADR 갱신/외부 LLM/실 API SDK/신규 actual run trigger 모두 0건. **5 영구 핵심 제약 5/5** + **Provider Liquidity 5-way 100%** + **F-금지 #1 영구 답습**. **상위 합의 본문 변경 0건** + **ADR-011 §2.1 재정의 0건** + **합산 222 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25). **본 evidence ≠ 합의 보고서 / MVP-1 PASS 재선언 / Layer C 재발효 / Layer D 재선언** — 검증 결과 기록 권위 한정. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-4 진입 조건 점검 / (2) Layer C 재평가 / (3) Group α 조건 재평가 / (4) Backlog #1 / (5) Backlog #3 T3 / (6) Backlog #4 facade real / (7) Backlog #5 event enum / (8) Backlog #7 ST-2/4/5 / (9) MVP-2~6 deepening / (10) Group I / (11) token rotation / (12) GitHub plan 확인 / (13) 세션 종료. **이전 (2026-05-16 후속 21)**: Phase α-1+2+3 1순위 병렬 *실제 구현 진입 여부* brief — APPROVE (`faae826` + `7917e4a` + `2aa13ef`).
docs/INDEX.md:440:**이전 후속 21 상세** (참고용 보존): 2026-05-16 후속 21 (**Phase α-1 + α-2 + α-3 1순위 병렬 *실제 구현 진입 여부* brief + Reviewer-only 단축 합의 APPROVE (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 + α-2 + α-3 실제 병렬 구현 진입 brief 작성. 범위는 R-4 + R-5 + R-7 실제 구현 진입 여부 검토." → "옵션 (A)로 진행해주세요"). **3 commit chain**: (1) `faae826` Phase α-1+2+3 1순위 병렬 *실제 구현 진입 여부* brief (920줄, 14 섹션 — DRAFT) / (2) `7917e4a` Reviewer-only 단축 합의 보고서 (446줄, 15 섹션 + APPROVE + 25 합의 조건 C-ξ-1~C-ξ-25) / (3) 메타 commit. **framing 차이**: Stage 2 ("How to plan?") → **Stage 3 ("Should we enter?")** → Stage 4 (실 구현 — 사용자 결정 영역). **합의 효력**: parallel actual implementation entry **— 실제 파일 수정 *직전* 의 진입 권한으로 한정**. **합의 판정 = APPROVE (Reviewer-only 단축 8/8 트리거 0건 발화)**. **4 결정 영역 채택**: D-1 (i) + D-2 (a) + D-3 (5) 3 Phase 동시 진입 + D-4 (α) 통합 합의 1건. **96/96 Prerequisite 충족**: G1 9/9 + G2 5/5 + G3 27/27 + G4 0/8 + G5 5/5 + G6 5/5 + G7 0/1 + G8 13/13 + G9 0/23. **사용자 명시 5 금지 위반 영구 답습**: 실제 파일 수정 / CI workflow 변경 / runtime code 변경 / Operational Readiness PASS / Hermes PMO 격상 모두 0건. **3 Phase 본문 변경 0건**: R-4 829 + R-5 35 + R-7 328 = 1192줄 답습 보존. **25 합의 조건 (C-ξ-1~C-ξ-25)** + **합산 222 조건 영구 답습** (Group α 12 + Backlog #6 11 + Phase α-1~α-4 98 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + 본 합의 25). **5 영구 핵심 제약 5/5** + **Provider Liquidity 5-way 100%** + **F-금지 #1 영구 답습**. **상위 합의 본문 변경 0건** + **ADR-011 §2.1 재정의 0건**. **추가 0건**: Phase α-1~α-3 실 진입 자체 / 1192줄 변경 / Layer C 재발효 / Layer D 재선언 / Phase α-4 자동 진입 / Stage 4 자동 진입 / Layer E / Layer F 진입 / R-4.1/URL/Model catalog 변경 / `.importlinter` 변경 / R-7 변경 / 3 MVP-1 + 8 PoC workflow 변경 / PC-3/4/AR-1/2/3 / ST-1/2/4/5 / S-2 진입 / Stage 5 / Tier-2/3 확장 / threshold 고정 / Rollback Trigger / TR-1~TR-5 발화 / Group α 14 결정 영역 / §5.5 9 sub-수단 변경 / Group I / token rotation / GitHub plan / event enum / ADR 갱신 / 신규 ADR / commit signing / `pull_request_target` / Hermes upstream / Production docker-compose / 실 secret material / 실 API/SDK / 외부 LLM / 실 docker build/run/history / 인간 리뷰 / facade real / Layer 2 runtime / 의미적 lock-in / 17 항목 우선순위 *재고정* / MVP-2~6 deepening 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) 실제 병렬 구현 시작 / (2) α-1 단독 / (3) α-2 단독 / (4) α-3 단독 / (5) Phase α-4 조건 점검 / (6) 세션 종료. **이전 (2026-05-16 후속 20)**: Phase α-1+2+3 1순위 병렬 *계획* brief — APPROVE AS BRIEF (`2e36592` + `88ccf79` + `96a8d14`).
docs/INDEX.md:442:**이전 후속 20 상세** (참고용 보존): 2026-05-16 후속 20 (**Phase α-1 + α-2 + α-3 1순위 병렬 구현 brief + Reviewer-only 단축 합의 (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 + α-2 + α-3 1순위 병렬 구현 brief 작성. 범위는 R-4 + R-5 + R-7 cycle 분할, 수정 범위, 테스트 범위, rollback trigger, evidence 기준 정리." → "옵션 (A)로 진행해주세요"). **3 commit chain**: (1) `2e36592` Phase α-1+2+3 1순위 병렬 구현 brief (950줄, 13 섹션 — DRAFT) / (2) `88ccf79` Reviewer-only 단축 합의 보고서 (359줄, 15 섹션 + APPROVE AS BRIEF + 25 합의 조건 C-ν-1~C-ν-25) / (3) 메타 commit. **본 합의 framing**: Phase α 통합 실제 구현 계획 (`542e77e` 후속 19) cycle 옵션 (i) 1순위 부분 (α-1 + α-2 + α-3) *cycle 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정 DRAFT → APPROVE AS BRIEF 격상*. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 8/8 트리거 0건 발화)**. **사용자 명시 5 금지 위반 영구 답습**: 실제 파일 수정 / CI workflow 변경 / runtime code 변경 / Operational Readiness PASS / Hermes PMO 격상 모두 0건. **3 Phase 본문 합산**: R-4 829 + R-5 35 + R-7 328 = **1192줄 답습 보존** (4 sub-수단 S-1 + T-2 + T-2 import-linter + T-5 + ST-3). **의존성 토폴로지**: α-1 ↔ α-2 부분 의존 (T-6) / α-1 ↔ α-3 독립 / α-2 ↔ α-3 독립 / 3 Phase → α-4 선행 의존 (별도 brief 영역). **cycle 분할**: Step 0~6 (사전 점검 / 1순위 병렬 진입 / actual run 답습 / 합의 형태 결정 / 옵션 외부 LLM / 합의 보고서 / 메타). **4 cycle 옵션 권고**: (i) 답습 한정 단축 / (ii) minor 인터페이스 정렬 / (iii) 3 Phase 분리 / (iv) 풀 3+1 — 사용자 결정 영역. **3 Phase 별 수정 범위**: 1192줄 답습 한정 + α-1 + α-3 minor CLI 정렬 후보. **3 Phase 별 테스트 범위**: fixture 답습 + unit dry-run + actual run regression (재실행 0건). **3 Phase 별 Rollback Trigger**: Layer B 18 + TR-1~TR-5 = 발화 0건 + threshold 후보 한정. **3 Phase 별 Evidence 기준**: ADR-011 §2.1 (a)~(e) × 3 Phase = **15/15 PASS** Layer C 답습. **actual run 답습 4/4 PASS**: `25728590939` + `25728590916` + `25728590977` + `25731846625` (재실행 0건). **추가 27 분리 영역 위반 0건**. **25 합의 조건 (C-ν-1~C-ν-25)** + **합산 197 조건 영구 답습** (Group α 12 + Backlog #6 11 + Phase α-1~α-4 98 + Layer C 30 + Layer D 25 + Phase α 통합 25 + 본 합의 25). **5 영구 핵심 제약 5/5** + **Provider Liquidity 5-way 100%** + **F-금지 #1 영구 답습**. **상위 합의 본문 변경 0건** + **ADR-011 §2.1 재정의 0건**. **추가 0건**: Phase α-1~α-3 실 진입 / 1192줄 변경 / Layer C 재발효 / Layer D 재선언 / Phase α-4 자동 진입 / Layer E / Layer F 진입 / R-4.1/URL/Model catalog 변경 / `.importlinter` 변경 / R-7 변경 / 3 MVP-1 + 8 PoC workflow 변경 / PC-3/4/AR-1/2/3 / ST-1/2/4/5 / S-2 진입 / Stage 5 / Tier-2/3 확장 / threshold 고정 / Rollback Trigger / TR-1~TR-5 발화 / Group α 14 결정 영역 / §5.5 9 sub-수단 변경 / Group I / token rotation / GitHub plan / event enum / ADR 갱신 / 신규 ADR / commit signing / `pull_request_target` / Hermes upstream / Production docker-compose / 실 secret material / 실 API/SDK / 외부 LLM / 실 docker build/run/history / 인간 리뷰 / facade real / Layer 2 runtime / 의미적 lock-in / 17 항목 우선순위 *재고정* / MVP-2~6 deepening / cycle 옵션 / 합의 형태 / step 분할 자동 결정 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) 실제 병렬 구현 진입 / (2) α-1 단독 / (3) α-2 단독 / (4) α-3 단독 / (5) α-4 진입 조건 점검 / (6) cycle 옵션 (ii) minor 정렬 / (7) cycle 옵션 (iii) 3 Phase 분리 / (8) 풀 3+1 진입 / (9) 다른 Backlog 진입 / (10) 세션 종료. **이전 (2026-05-16 후속 19)**: Phase α-1~α-4 통합 실제 구현 계획 brief — APPROVE AS BRIEF + 3 commit chain (`96891eb` + `542e77e` + `b7d3415`).
docs/INDEX.md:444:**이전 후속 19 상세** (참고용 보존): 2026-05-16 후속 19 (**Phase α-1 ~ α-4 통합 실제 구현 계획 brief + Reviewer-only 단축 합의 (옵션 (A)) + 3 commit chain (brief + 합의 + 메타)**). 사용자 명시 진입 명령 답습 ("Phase α-1 ~ α-4 통합 실제 구현 계획 brief를 작성해주세요. 범위는 R-4 도구 본문, R-5 .importlinter, R-7 docker secret block, R-1 CI workflow 통합을 실제 구현하기 전 단계 분할로 정리하는 것입니다. 아직 실제 파일 수정, CI workflow 변경, runtime code 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요." → "옵션 (A)로 진행해주세요"). **3 commit chain**: (1) `96891eb` Phase α 통합 실제 구현 계획 brief (949줄, 11 섹션 — DRAFT) / (2) `542e77e` Reviewer-only 단축 합의 보고서 (367줄, 11 섹션 + APPROVE AS BRIEF + 25 합의 조건 C-μ-1~C-μ-25) / (3) 메타 commit. **본 합의 framing**: Layer C 발효 (`eb01bc4` 2026-05-16) + Layer D 권위 답습 (`210c98f` + 후속 18) 後 — Phase α 4 단계 통합 실제 구현 *단계 분할 정리 한정 DRAFT → APPROVE AS BRIEF 격상*. **합의 판정 = APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 8/8 풀 3+1 트리거 0건 발화)**. **사용자 명시 5 금지 위반 영구 답습**: 실제 파일 수정 / CI workflow 변경 / runtime code 변경 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 모두 0건. **4 영역 본문 합산 매트릭스**: R-4 829 + R-5 35 + R-7 328 + R-1 1593 = **2785줄 답습 보존** (4 Phase × 20 artifact, 6 sub-수단 S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1, 3 sub-수단 PC-4 + AR-2 + AR-3 = 본 합의 영역 외 분리). **의존성 토폴로지** = **1순위 병렬 (α-1 + α-2 + α-3)** + **2순위 의존 (α-4 = Stage 4 prerequisite 4/4 PASS 의무)**. **통합 실제 구현 단계 분할** = α-1 11 sub-step + α-2 6 항목 + α-3 4 sub-step + α-4 4 sub-step (4.3 PC-4 + 4.4 AR-2 = 분리 명시). **통합 cycle 옵션**: (i) 1순위 병렬 — 2순위 의존 / (ii) 단일 cycle / (iii) 4 cycle 분리 — 모두 권고 한정. **actual run 답습 4/4 PASS**: `25728590939` + `25728590916` + `25728590977` + `25731846625` (재실행 0건). **통합 진입 적격성 5/5 (C-π-1~C-π-5) 충족** + **의존성 의무 통과** (Stage 4 prerequisite 100% 答) + **8/8 풀 3+1 트리거 0건 발화**. **추가 24 분리 영역 위반 0건**: branch protection / dev 환경 / `pre-commit install` 의무화 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 / Tier-2/3 / commit signing / `pull_request_target` / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 모두 분리. **25 합의 조건 (C-μ-1~C-μ-25)**. **합산 합의 조건 영구 답습 (Group α 12 + Backlog #6 11 + Phase α-1~α-4 98 + Layer C 30 + Layer D 25 + 본 합의 25 = 201 조건)** + **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습**. **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`210c98f`) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1~α-4 / Stage 2 / Stage 4 / Group A 1차/2차/3차 / Group D / §5.5 9 sub-수단 / mvp1.md 본문 변경 0건** + **ADR-011 §2.1 (a)~(e) 재정의 0건**. **추가 0건**: Phase α-1~α-4 실 진입 / 2785줄 본문 변경 / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Layer E / Layer F 진입 / evidence 재생성 / actual run 재실행 / R-4.1/URL/Model catalog 변경 / `.importlinter` forbidden/facade/google.generativeai/URL 흡수 변경 / R-7 docker secret 변경 / 3 MVP-1 + 8 G2/G3/G4 PoC workflow 변경 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 / Stage 5 자동 진입 / Tier-2/3 확장 / threshold *고정* / Rollback Trigger / TR-1~TR-5 발화 / Group α 14 결정 영역 재결정 / §5.5 9 sub-수단 변경 / Group I / token rotation / GitHub plan / event enum / ADR 갱신 / 신규 ADR 발행 / commit signing / `pull_request_target` / Hermes upstream / Production docker-compose / 실 secret material / 실 API/SDK / 외부 LLM 자동 호출 / 인간 리뷰 의무 / facade real 본문 / Layer 2 runtime / 의미적 lock-in / 17 항목 우선순위 *재고정* / MVP-2~MVP-6 deepening / cycle 옵션 / 합의 형태 / step 분할 자동 결정 모두 0건. **다음 단계 = 사용자 결정 영역** (자동 진입 0건): (1) Phase α-1+α-2+α-3 1순위 병렬 구현 brief / (2) Phase α-1 단독 / (3) Phase α-2 단독 / (4) Phase α-3 단독 / (5) Phase α-4 진입 조건 점검 / (6) cycle 옵션 (ii) 단일 cycle / (7) cycle 옵션 (iii) 4 cycle 분리 / (8) Backlog 진입 (C-5b / C-5c / C-6 / C-7 / C-8 / Group I / token rotation / GitHub plan 등) / (9) 세션 종료. **이전 (2026-05-16 후속 18)**: Layer D — MVP-1 PASS 재진입 가능성 검토 brief — APPROVE AS BRIEF + 3 commit chain (`d286f87` + `951a5b1` + `ce344e3`).
docs/INDEX.md:446:**이전 후속 18 상세** (참고용 보존): 2026-05-16 후속 18 (**Layer D — MVP-1 PASS *재진입 가능성 검토* brief + Reviewer-only 단축 합의 (옵션 (A) — Existing Layer D authority preserved) + 3 commit chain**). 사용자 명시 진입 명령 답습 ("Layer D MVP-1 PASS 선언 합의 진입 brief 작성" → "옵션 (A)로 진행" + "C-1~C-8 최신 CONTEXT 기준 재검증"). **3 commit chain**: (1) brief commit (`docs/phase0/layer-d-mvp1-pass-declaration-entry-brief.md` 721+줄, 13 섹션 — DRAFT + C-1~C-8 cross-reference 정확화) / (2) 합의 보고서 commit (`docs/review/3plus1-consensus-2026-05-16-layer-d-reentry-assessment.md` — APPROVE AS BRIEF + 25 합의 조건 C-λ-1~C-λ-25) / (3) 메타 commit. **핵심 framing 발견**: Layer D 이미 `210c98f` (2026-05-13) APPROVE WITH CONDITIONS 발효 완료 — 본 brief = Layer C 재발효 후속 *재진입 가능성 검토* (재선언 요구 0건). **5 핵심 발효 문구**: Layer D = 기존 `210c98f` 권위 유지 / Layer C 재발효 = 근거 *강화* (재선언 요구 0건) / Layer D 본문 변경 0건 / MVP-1 PASS 재선언 0건 / Layer E / Layer F 진입 0건. **C-1~C-8 satisfaction 매트릭스 (top-level)**: Satisfied 2 (C-1 `1dd1036` + C-2 `b705370`) / Partially Satisfied 2 (C-5 전체 + C-6 `78483c5`) / Deferred 3 (C-3 + C-4 + C-8) / Requires separate full 3+1 1 (C-7 — Group α 진전 `4880e88`). **C-5 sub-condition**: C-5a Satisfied (`6fa87dc`) / C-5b Deferred / C-5c Partially Satisfied (`78483c5`). **3 옵션 매트릭스**: (A) 기존 Layer D 답습 한정 = **권고 후보** (사용자 명시 채택) / (B) 재발효 = 선택 후보 / (C) *de novo* = 비권고. **Layer D 재진입 적격성 5/5 (C-κ-1~C-κ-5) 충족** + **27/27 풀 3+1 트리거 0건 발화** + **Layer C + Layer D 합산 60/60 트리거 0건 발화** + **25 합의 조건 (C-λ-1~C-λ-25)**. **사용자 명시 5 금지 위반 영구 답습**: Operational Readiness PASS / Hermes PMO 격상 / actual run 재실행 / evidence 재생성 / R-4+R-5+R-7+R-1 본문 변경 (2785줄) 모두 0건. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습**. **기존 Layer D (`210c98f`) 원문 변경 0건** + **C-1~C-8 본문 정의 변경 0건** + **본 합의 추가 satisfaction 갱신 0건** (모두 후속 합의 권위 source 답습). Layer C 진입 가능성 합의 30 조건 (C-η) / Layer C 실 발효 합의 30 조건 (C-ι) / Phase α-1~α-4 합의 본문 / C-β/C-γ/C-δ/C-ε / Group α C-1~C-12 / Backlog #6 C-α / Layer A / Layer B / §5.5 / ADR-011 §2.1 / mvp1.md §0 3-layer PASS framework 변경 0건. **추가 0건**: Layer D 재발효 / *de novo* 발효 / MVP-1 PASS 재선언 / Layer E / Layer F 진입 / 외부 LLM 자동 호출 / 메타 갱신 자동 진입 (사용자 결정 영역) / Backlog #1~#7 자동 진입 / Phase α-1~α-4 실 진입 자동 진입 / CI workflow / branch protection / dev 환경 강제 / `pre-commit install` 의무화 / runtime code 변경 / Hermes upstream / Production docker-compose / 실 secret material / 실 API/SDK 호출 / 인간 리뷰 의무 / commit signing / `pull_request_target` / Tier-2/3 확장 / threshold 고정 / event enum 추가 등록 / ADR 본문 자동 갱신 / 신규 ADR 발행 / Group I / Group β / γ-1 / γ-2 자동 진입 / 17 항목 우선순위 *재고정* 모두 0건. **다음 단계 = 사용자 결정 영역**: push / C-5b ST-1 / C-5c PC-4 T3 sub / C-6 잔여 / C-7 T3 실 적용 / C-8 P1 v2 facade real / Phase α-1~α-4 실 진입 / Phase α 통합 실제 구현 계획 / Group I / token rotation / GitHub plan 가용성 확인 / 세션 종료. **이전 (2026-05-16 후속 17)**: Layer C — MVP-1 Implementation Evidence PASS *실 발효* + GP-3 / GP-5 PASS 발효 — 2 commit chain (`eb01bc4` + `24caa53`).
docs/INDEX.md:448:**이전 후속 17 상세** (참고용 보존): 2026-05-16 후속 17 (**Layer C — MVP-1 Implementation Evidence PASS *실 발효* + GP-3 / GP-5 PASS 발효 — Reviewer-only 단축 합의 APPROVE + 2 commit chain (Step 5 합의 보고서 + Step 6 메타)**). 사용자 명시 진입 명령 답습 ("Step 5 진입으로 진행해주세요" → "(A) Step 6 진입으로 진행해주세요"). **2 commit chain**: (1) `eb01bc4` Layer C 실 발효 합의 보고서 (610줄, 12 섹션 + APPROVE + 30 합의 조건 C-ι-1 ~ C-ι-30) / (2)  우회 risk verify | ✅ — §2 PC-1-T3 + ST-2 자율 영역 3 risk 각 NOTE 자격 정합 + §3 branch protection 6 시나리오 (admin bypass + force push + branch deletion + fork PR + draft + paths-aware) + R-MVP1-PASS-4 trigger 정합성 |
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:3:> **본 합의는 추론적 검증(권고) 한정이며 — 본 합의의 어떤 §도 그 자체로 (i) 실 runtime code / CI workflow / hook 구현 / 변경, (ii) Implementation Evidence PASS / Operational Readiness PASS 발효, (iii) ADR 본문 갱신, (iv) 수단 *결정*, (v) threshold *고정*, (vi) Tier-2/3 catalog 자동 확장, (vii) DRAFT → APPROVED *외* 다른 권위 변경, (viii) 후속 합의 본문 변경, (ix) ADR-011 §2.1 (a)~(e) 5조건 충족 *자동* 선언, (x) 1.5차 보강 / MVP-2 진입 자동 진입 — 어떤 행위도 자동 발생시키지 않는다. 본 합의 = `implementation-runtime-roadmap-mvp1.md` 권위 표시 격상 한정 (840줄 본문 변경 0건, line 826/827 상태 표시 격상 + 변경 이력 line 추가 한정).**
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:10:**1차 권위 답습**: roadmap-mvp1 §3.6.3 / §4.7.3 line 287/477 합의 형태 권고 + audit brief 후속 3 합의 cross-check + ADR-011 §2.1 (a)~(e)
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:43:| 5 | ADR-011 §2.1 (a)~(e) 5조건 충족 *자동* 선언 | ❌ 미발화 | audit brief §4 "(e) conditions 미해소 = 1.5차 보강 cycle 필요" — 자동 충족 선언 0 |
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:61:**(c) ADR-011 §2.1 (a)~(e) 답습 정확성**: ✅
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:63:- roadmap §3.6.2 + §4.7.2 = ADR-011 5조건 본문 답습 일치
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:93:- ❌ Implementation Evidence PASS 발효 — 별도 합의 + ADR-011 5/5 evidence + conditions 해소 + 사용자 명시
docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md:101:**근거**: 5/5 풀 3+1 승격 trigger 미발화 + 후속 3 합의 본문 흡수 완료 + audit brief §3.1 권위 잔재 정합 + ADR-011 §2.1 (a)~(e) 답습 정확. roadmap-mvp1 line 287/477 명시한 합의 형태 권고 답습.
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:1:# 단축 3+1 합의 보고서 (Reviewer-only): ADR-011 수단/목적 분리 원칙 + ADR-008 Amendment
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:5:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (신규)
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:14:**사용자 명시 결정**: 옵션 C (ADR-011 신규 + ADR-008 Amendment), 단축 합의
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:41:- ADR-009 (자체 Adapter v2.0 entry): 본 ADR §2.1 (a)~(d) 4조건 미래 적용 가능성 명시 (ADR-011 §7.3 주의사항). 즉시 영향 없음.
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:50:**APPROVE** — ADR-011 본문 + ADR-008 Amendment 모두 합의 가동 사유 4건을 ADR 권위로 정착하며, R-1/R-2 evidence 인용 정합. 메타 편향 통제 명시 + (a)~(d) 4조건과 R-4~R-7 모법 역할로 자체 코드 우호 결론 회귀 견제 — Reviewer 단독 누락 위험 0건.
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:56:| 1 | **헌법 8조 본질 충족 권위화** | **PASS** | ADR-011 §2.1 — 본질을 "DB 평문 저장 차단 결과"로 명시, 수단 대체에 (a)~(d) 4조건 강제. 자의적 수단 회귀 차단 + 자의적 수단 대체 차단 양방향 견제. |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:57:| 2 | **G1a/G1b 분리 공식화** | **PASS** | ADR-011 §2.2 — R-1 FAIL evidence(`agent/redact.py` docstring + import 25개 grep + `hermes_state.py` 0건) 인용, R-2 PASS evidence(Docker 격리 + 6항목 자동 검증) 인용, G1b 정식 충족 조건 5단계 명시. |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:58:| 3 | **Hermes ≠ root of trust 권위 승격** | **PASS** | ADR-011 §2.3 — prequel §3 임시 선언을 ADR 영구 권위화, 운영 함의 5항목 명문화 (Tools 검증 / redaction 신뢰 범위 / DB 외부 보호 / 자동 R-2 회귀 / 학습 결과 자동 정책 반영 금지). |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:59:| 4 | **자동 학습 vs 정책 변경 분리** | **PASS** | ADR-011 §2.4 — T1/T2/T3 3-tier 분류 본문 흡수. R-5 (canary 재검증) / R-6 (CI 회귀) 권위 근거화. silent 깨짐 자동 차단 정당화. |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:60:| 5 | **R-4~R-7 모법 역할** | **PASS** | ADR-011 §3 — 4 작업 모두 ADR §2 항목 매핑 명시. 후속 작업이 본 ADR을 권위 근거로 인용 가능. |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:61:| 6 | **ADR-008 Amendment 정합성** | **PASS** | 부록 B B.1~B.6 — R1 specific 갱신 + ADR-011 cross-ref + 오해 방지 (Hermes 안전 선언 아님) + 6 차단조건 #1 충족 메커니즘 갱신 표 + 정식 충족 5단계. ADR-011 §2와 일관, 일반 원칙 중복 없음. |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:73:| ADR-011이 미래 다른 비협상 조항(예: ADR-009 트리거 조건, ADR-010 키 관리)에 무리하게 일반화될 위험 | **차단됨** — §7.3 주의사항에 "별도 합의로 결정" 명시 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:75:| prequel §6 자동 학습 3-tier가 ADR-011 §2.4와 표현 차이 위험 | **검증 PASS** — prequel은 R-7 후 폐기되며 ADR-011 §2.4가 영구 권위. 표현 차이는 ADR 우선 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:76:| ADR-009 / ADR-010 갱신 PR 묶음(P2 v3 작성 시) 누락 위험 | **추적 항목** — CONTEXT.md "다음 세션 TODO" 7번 (P2 v3 + ADR-008/009/010 갱신 PR 묶음) 에 본 ADR-011도 포함되도록 갱신 권고 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:77:| R-4 패턴 동등성 검증 시 gap 발견되면 trigger UDF 보충 — UDF 보충이 §2.1 (a)~(d) 4조건 검증 필요 | **명시됨** — ADR-011 §2.2 G1b 정식 충족 조건 R-4 항목 + §3 R-4 매핑 §2.1 (a) |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:82:**Reviewer 단독 누락 위험 0건**. 다만 §3.1 4번 (ADR-009/010 갱신 PR 묶음)은 CONTEXT.md 갱신 시 ADR-011 포함을 명시 권고.
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:90:본 ADR-011은 다음 의미에서 *자체 코드 친화* 결론을 권위화한다:
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:117:**APPROVE — ADR-011 + ADR-008 Amendment 즉시 발행**.
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:124:### 5.3 다음 단계 (사용자 명시 순서)
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:128:| 1 | R-4 — Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교 | `docs/architecture/redaction-pattern-equivalence.md` | ADR-011 §2.1 (a) + §3 R-4 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:129:| 2 | R-5 — canary 재검증 트리거 설계 | `docs/architecture/canary-recheck-design.md` | ADR-011 §2.4 + §3 R-5 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:130:| 3 | R-6 — CI/nightly 회귀 검증 설계 | `.github/workflows/r2-canary.yml` | ADR-011 §2.1 (d) + §2.3 + §3 R-6 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:131:| 4 | R-7 — Phase 1 합격 SOP | `docs/phase0/redaction-verification-sop.md` | ADR-011 §2.2 + §3 R-7 |
docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md:138:- CLAUDE.md §8 참조 테이블에 ADR-011 추가
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:8:**상위 권위**: R-7 SOP §7.3 절차 + ADR-011 §2.4 T2 (사용자 승인 기반)
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:30:- ADR-011 §2.4 T2 (사용자 승인) 분류 — 정책 변경 아닌 *evidence-driven status 갱신*
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:37:- ❌ Tier-2 / Tier-3 catalog 확장 — ADR-011 §2.4 + R-7 범위 외
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:59:| 2 | G1a FAIL 명시 | ✅ | ADR-011 §2.2 / ADR-008 부록 B.2 / R-7 SOP §4.1 |
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:61:| 4 | R-3 ADR-011 / ADR-008 Amendment 완료 | ✅ | `ADR-011-means-vs-ends-redaction.md` + `ADR-008` 부록 B + `3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` |
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:140:| 합의 형태 정당성 | **PASS** | ADR-011 §2.4 T2 + R-7 SOP §7.3 |
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:142:### 5.3 메인 컨텍스트 권고 (단축 합의 메타 평가)
docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md:171:- ❌ 자동 정책 변경 — ADR-011 §2.4 T3
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:31:| ADR-011 §2.4 T2 분류 (사용자 승인 기반) | ✅ |
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:71:| **권위 위계 영구화** | ADR-011 §2.3 (Hermes ≠ root of trust) + ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) + ADR-012 §2.12 (Hermes 변조 차단 매트릭스) | **불필요** — 3 ADR 영구 권위 충족 |
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:84:**현 시점 (2026-05-09 후속 12)** Hermes PMO 격상 절차 = P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 = **7 권위 layer 중첩 답습**. 추가 ADR 필요성 *낮음*.
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:113:**현 시점** G4 = Design PASS / Implementation Pending. ADR-014 = *Implementation/Runtime PASS 시점 발행 검토 영역*. 현 시점 발행 = *PoC 전 권위 정착* → ADR-011 §2.1 (b) 격리 환경 PoC 실증 *전* 의 ADR 발행은 *기존 ADR 패턴 위반*. 
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:129:| 수단/목적 분리 + G1a/G1b + Hermes ≠ root of trust + T1/T2/T3 | ADR-011 |
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:134:| 합의 인프라 (3+1 + 외부 LLM + 인간 리뷰) | ADR-011 §2.4 + P2 v3 §11 + Gemini §7.10 #3 답습 |
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:221:| 2 | 이미 ADR-008~012에서 결정된 내용의 반복 | ✅ 다수 (P2 v3 §2.6 + ADR-008 부록 B + ADR-011 + ADR-012 답습) | ✅ 다수 (G4 §4 + ADR-012 §2.10 답습) |
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:264:| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.7 (ADR-013/014 발행 시점 = T3 변경, 풀 3+1 + 외부 LLM 1+ 의무) |
docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md:301:### 5.3 다음 진입점 (사용자 결정 영역)
docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md:67:- **G-13 (B 단독)**: **M3 결정 고정 단계 = ADR-011 §2.1 (a)~(d) 답습 의무** (R-B-7). **NOTE 채택**.
docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md:105:- **R-19** (B-R-B-7): M3 *결정 고정* 단계 = ADR-011 §2.1 (a)~(d) 답습 의무. 본 합의 §6.1 "결정 *고정* = 별도 단계" 와 결합
docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md:130:**3개 Agent 출력 모두 답습 권위 (entry brief v1.1 + 합의 R-1~R-6 + brief v2 §6 + MVP-1 합의 R1~R13 + CLAUDE.md + ADR-011) 와 모순 없음.** 판정 분기 (A·B REVISE / C APPROVE w/ COND) = 표현 차이, *brief v1.1 보강 의무 + 합의 결과 채택* 으로 합치.
docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md:190:### 5.3 Phase 3 — 큰 cost, 별도 cycle
docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md:246:**출처**: Agent A 출력 (구현, 12K tokens) + Agent B 출력 (안전, 11K tokens) + Agent C 출력 (대안, 9K tokens), 모두 본 합의 entry brief v1 + V-1 findings + Stage 4 raw 30 JSON + summary + entry brief v1.1 + V-1 entry 합의 + MVP-1 brief v2 + MVP-1 합의 + CLAUDE.md + ADR-011 §2.1 기반. **편향 방지 답습**: Agent A·B·C 상호 출력 참조 0건 (병렬 독립).
docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md:248:**답습**: `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `project_minimize_user_intervention` / `project_jarvis_local_boss_direction` / ADR-011 §2.1 (a)~(d).
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:19:9. prev_hash 검증 실패 → BLOCK + manual review 정책의 ADR-011 §2.4 (T3 자동 정책 변경 금지) 정합성
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:39:- ❌ 신규 정책 발명 (ADR-012 / G4 §4 / ADR-011 본문 외)
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:66:| 3 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5조건 + §2.3 Hermes ≠ root of trust + §2.4 T1/T2/T3 | 모법 ADR (수단/목적 분리) |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:75:ADR-011 §2.1 (수단/목적 분리, (a)~(e) 5조건)
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:76:ADR-011 §2.3 (Hermes ≠ root of trust)
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:77:ADR-011 §2.4 (T1/T2/T3 자동 정책 변경 금지)
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:158:- ADR-011 §2.3 (Hermes ≠ root of trust): **간접 답습** — `jcs` 도 *root of trust 아님*, cross-check 보강 layer 로 위치
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:210:- ADR-011 §2.3 (Hermes ≠ root of trust): **간접 답습 — `rfc8785` / `jcs` 도 root of trust 아님**
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:236:- ADR-011 §2.1 (a) 동등 이상의 보안 결과: **충족** — 단일 라이브러리 대비 bug-class 회피 차원 강화
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:305:- ADR-011 §2.4 T1 분류: "자동 허용 — Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 / 승인 경로 = 자동"
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:311:| T1 audit 분류 적합성 | **HIGH** | Fallback 사용 = *자동 허용* (Primary 라이브러리 install 실패 시 자동 fallback) + *audit trail 의무* (`event` ledger entry) → ADR-011 §2.4 T1 분류 정합. 자동 허용 + 사후 audit 패턴 |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:318:- ADR-011 §2.4 T1: **충족** (자동 허용 + audit)
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:326:### 2.9 영역 9 — prev_hash 검증 실패 → BLOCK + manual review 정책의 ADR-011 §2.4 (T3 자동 정책 변경 금지) 정합성
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:330:- ADR-011 §2.4 T3: "자동 금지 (절대) — Constitution / ADR / Harness Gates 정의 자체의 변경 / 승인 경로 = 단축 또는 풀 3+1 합의"
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:332:- 본 PoC §7 답습 강제 조건: "ADR-011 §2.4 (T1/T2/T3) → T3 위반 자동 revert 금지 → chain violation = BLOCK + manual + violation entry (자동 revert 0건)"
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:338:| ADR-011 §2.4 T3 (자동 정책 변경 금지) 정합 | **HIGH** | chain violation 검출 시 *자동 revert / 자동 chain 재계산 / 자동 entry 수정* 모두 금지 → ADR-011 §2.4 T3 답습 직접 정합 |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:342:| 자동 revert 금지의 영구 권위 | **HIGH** | ADR-012 §2.7 #5 + §2.7 #6 (Dual write 금지) + ADR-011 §2.4 T3 = 영구 권위. 본 PoC = *영구 권위 답습 적격* |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:345:- ADR-011 §2.4 T3 (자동 정책 변경 금지): **충족 HIGH**
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:349:**판정**: APPROVE — ADR-011 §2.4 T3 + ADR-012 §2.7 정합 강도 **HIGH**. 단 violation_type 4종 직접 cover 부분 (Gap, §7 enumerate)
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:375:- ADR-011 §2.3 (Hermes ≠ root of trust): **간접 답습 — 본 PoC 가 Hermes-originated entry 검출 layer 강화**
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:429:- PR-2 합의 §6.3 답습: "ADR 신규 발행 = T3 변경 (ADR-011 §2.4) → 풀 3+1 + 외부 LLM 1+ 의무 (G3 §4.4.2). 본 PR-2 = 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) 충족"
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:460:| `policy_change_attempted` (#16) 미적용 — Hermes 정책 변경 시도 검출 layer 부재 | 영역 11 | **HIGH** | ADR-011 §2.4 T3 + ADR-012 §2.12 #1 답습 — 본 PoC = filesystem 변조 (§2.12 #2) cover 까지 | Gap-N #3 (§7) |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:488:| Hermes ≠ root of trust (ADR-011 §2.3 영구 권위) | ADR-011 §2.3 + ADR-012 §2.12 | 본 PoC 도구 = `import hermes_agent` 0건 + `agent` 필드 enum 검증 + chain 검증으로 Hermes-originated entry *사후 검출 layer* 제공. 단 §2.12 #1/#3/#4 미cover 영역 존재 | **HIGH** (단 §7 Gap-N 4건 통한 영구 보호 강화 의무) |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:490:| 자동 정책 변경 금지 (T3 — ADR-011 §2.4) | ADR-011 §2.4 + ADR-012 §2.7 | chain violation 검출 시 자동 revert 0건 + manual review 강제 + `chain_violation_detected` entry 자동 작성 (T1 audit) ↔ 정책 변경 (T3 BLOCK) 분리 정합. fallback 사용 = T1 audit (영역 8 답습) | **HIGH** |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:491:| 수단/목적 분리 (ADR-011 §2.1 (a)~(e)) | ADR-011 §2.1 5조건 | (a) 동등 이상 보안 결과 — 단일 라이브러리 대비 cross-check 강화 / (b) 격리 환경 PoC 실증 — 본 PoC venv `.poc-prep/jcs-ra9-venv/` (Docker 격리는 별도 권고) / (c) ADR 권위 명시 — ADR-012 §2.5 답습 / (d) 자동 회귀 검증 — `.github/workflows/g4-hash-chain.yml` / (e) 합의 APPROVE — 본 Q1 풀 3+1 진행 중 | **HIGH** ((b) Docker 격리 별도 권고 — C-B17) |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:539:| C-B17 | 본 PoC 격리 환경 보강 — 현 venv 격리 + Docker 격리 권고 (ADR-011 §2.1 (b) 답습) | 4 매트릭스 (b) | MEDIUM | 본 PoC §7 답습 강제 조건 보강 |
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:596:- ADR-011 §2.4 T3 (자동 정책 변경 금지) 운영 매커니즘 부분 발화
docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md:655:5. **ADR-011 §2.4 T3 (자동 정책 변경 금지) 정합 HIGH** — chain violation 검출 시 자동 revert 0건 + manual review 강제 + `chain_violation_detected` entry 자동 작성 (T1 audit) ↔ chain 수정 (T3 BLOCK) 분리 정합
docs/review/3plus1-consensus-2026-05-09-p1-doc-absorption.md:22:**상위 권위**: ADR-011 §2.1 (수단/목적 분리), §2.3 (권위 위계), §2.4 (T1/T2/T3) — `3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS) — `SESSION_2026-05-09.md` §11 (사용자 명시 결정 3건)
docs/review/3plus1-consensus-2026-05-09-p1-doc-absorption.md:40:| ADR-011 §2.4 분류 T2 (사용자 승인 기반) | ✅ 사용자 명시 결정 3건 (옵션 β + 본문 단축 + 외부 LLM 시점) 모두 SESSION §11.1 명시 |
docs/review/3plus1-consensus-2026-05-09-p1-doc-absorption.md:96:| Multi-host 전환 트리거 5건 (§5.5.3) | ✅ PASS — (1) 두 번째 사용자 / (2) 두 번째 호스트 / (3) Production 전환 / (4) 외부 LLM 자동화 / (5) Hermes PMO 격상 |
docs/review/3plus1-consensus-2026-05-09-p1-doc-absorption.md:167:| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ T2 (사용자 승인) / T3 (자동 정책 변경 금지) 모두 6 흡수 항목에서 명시 |
docs/review/3plus1-consensus-2026-05-09-p1-doc-absorption.md:168:| 4 | 수단/목적 분리 원칙 답습 | ✅ C-K provider_bindings 격상 = *수단* (필수 필드 strict) → *목적* (Provider Liquidity lock-in 차단), C-D enumeration = *수단* (보호 대상 명시) → *목적* (T3 정책 무결성), C-F SPOF accepted = *수단* (1인 의도적 수용) → *목적* (운영 단순성 + 점진 전환), 모두 ADR-011 §2.1 패턴 답습 |
docs/review/3plus1-consensus-2026-05-09-p1-doc-absorption.md:232:- **ADR-011 §2.4 T1/T2/T3 답습**: §1.7 8 금지 (T3) + §1.5 §1.6 (T2 사용자 승인)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:6:**상위 권위**: ADR-011 §2.3 (권위 위계 + 운영 함의 5항목, 영구 권위), ADR-011 §2.4 (T1/T2/T3) + 본 세션 사용자 명시 결정 (G4 진입 전 G3 DRAFT 적격 검토)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:25:- ADR-011 §2.3 (권위 위계 영구 권위) + §2.4 (T1/T2/T3 분류)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:39:- 본 G3 초안 작업은 *권위 흡수 + 운영 메커니즘 정의*이며 새 권위 결정 0건 (ADR-011 §2.3 / §2.4 답습 + system-identity-prequel §3 흡수)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:42:- ADR-011 §2.4 T2 분류 (사용자 승인 기반 진행)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:58:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신 적격성
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:73:| Hermes 단독 PASS 불가 | §1.3 / §5.3 (i)~(iv) | ✅ Hard Rule 명시 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:80:→ Criterion 1 PASS, "Hermes ≠ root of trust" 운영 구조 구현 충실. ADR-011 §2.3 권위 + system-identity-prequel §3 흡수 + 합의 §90 (자기참조 역설) 핵심 흡수.
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:99:→ Criterion 2 PASS, 위계 명확. ADR-011 §2.3 권위 인용 + 충돌 매트릭스 + 영구 제약 다중 보호.
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:115:| 7 | 자체 학습 (T1 한정) | (사용자 명시 추가) | ✅ ADR-011 §2.4 T1 직접 매핑 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:116:| 8 | Hermes 자체 redaction (로그/송신) | (사용자 명시 추가) | ✅ ADR-011 §2.3 운영 함의 #2 답습 (DB 차단은 G1b 책임) |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:130:| 17 | 자체 학습→자동 정책 반영 | (사용자 명시 추가) | T3 | ✅ ADR-011 §2.4 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:134:| 21 | Tier-1/2/3 catalog 자동 확장 | (사용자 명시 추가) | T3 | ✅ ADR-011 §2.4 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:135:| 22 | 사용자 override 자동 reject | (사용자 명시 추가) | T3 | ✅ ADR-011 §2.3 운영 함의 #5 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:214:| §5.3 PASS 성립 요건 (i)~(iv) | (i) Tools 검증 + (ii) ledger entry + (iii) 사용자 명시 (T2/T3) + (iv) 합의 보고서 (해당 시) | 4 요건 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:215:| §5.3 미충족 처리 | (i) hook 자동 차단 / (ii) ledger 검증 자동 차단 / (iii) T2/T3 자동 reject / (iv) 합의 cross-reference 부재 = §5.3 위반 | 자동 처리 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:287:| §8.3 *발생하지 않는 것* | G2/G4 자동 PASS / Hermes PMO 격상 자동 / P2 v3 정식 채택 자동 / archive 자동 / ADR-011 §2.3 본문 자동 갱신 |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:299:- "PASS" 단어: G1b PASS / R-6 PASS 등 *기존 권위 결정* 인용 + §1.3 §5.3 *PASS 성립 요건* 정의. *G3 PASS / 격상 PASS / 정식 채택 PASS* 인용 0건.
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:371:- §1.2 충돌 해결 매트릭스 3개 — *원안* (system-identity-prequel §3.3 + ADR-011 §2.3 인용 정확하나 *충돌 시나리오 분류*는 원안)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:372:- §5.2 5 운영 규칙 + §5.3 PASS 성립 4 요건 — *원안* (system-identity-prequel §6.1 명제 + ADR-011 §2.3 운영 함의 답습이나 *4 요건 분리*는 원안)
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:392:| 5 | ADR-008/009/010/011 본문 자동 갱신 | ❌ 위반 0건 (§0.2 #5 + §8.3 "ADR-011 §2.3 본문 자동 갱신 ❌ — cross-reference 만") |
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:411:3. 본 검토 자체가 G3 §4 자기참조 차단의 *적용 대상* — Reviewer-only 단축 합의는 ADR-011 §2.4 T2 영역에서 정당하나 *G3 PASS* 영역은 본 검토 비대상.
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:423:### 5.3 본 검토의 한계
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md:464:- **G3 §4 자기참조 차단의 *적용 대상*** 으로 본 검토 한계 명시 (§5.1 + §5.3)
docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md:5:> 본 합의의 어떤 §도 그 자체로 (i) **Hermes runtime 실 구현** (orchestrator / container / agent runtime 본문), (ii) **Hermes-originated commit 실 차단 hook 구현** (git pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문), (iii) **GitHub ruleset / branch protection 실 변경** (signed commit required / required status check / force push 차단 / bypass 정책), (iv) **Hermes upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR), (v) **수단 결정 *고정*** (식별 방법·차단 지점·보호 범위 최종 결정), (vi) **threshold 고정** (observe mode 기간 등), (vii) CI workflow 변경 / actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경, (viii) **Operational Readiness PASS (Layer E) 선언** / **Hermes PMO 격상 (Layer F) 선언**, (ix) **MVP-1 exit 발효** (GP-3 5/5 + GP-5 5/5 별도), (x) **Phase α defer-lockdown 변경**, (xi) **G3 (`hermes-not-root-of-trust-runtime.md`) §2.2 #20 / §2.5 / §2.6 / §4 / §5.5 본문 변경** (특히 line 448/784 detection 메커니즘 본문 교정 — 별도 단계), (xii) ADR 본문 자동 갱신 (ADR-008 / ADR-011 / ADR-012), (xiii) Group α / β / γ-1 / γ-2 합의 본문 변경 / GP entry 합의 본문 변경, (xiv) Backlog #4 · Backlog #6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입, (xv) 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정 + 본 합의 평가 대상) / 외부 LLM 추가 자동 호출, (xvi) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.
docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md:18:- ADR-011 §2.1 means/ends + §2.4 T3 영역 + 외부 LLM 입력 원칙 (응답 = 입력 한정)
docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md:89:- **§5.3 self-reference 구조**: Group I은 합의 인프라 순환 권위 *자체*를 대상으로 하는 결정 — Hermes orchestrated 단축(Reviewer-only) 단독은 메타-편향 통제 부족. G3 §4.2 원칙 2 ("Reviewer-only 또는 외부 LLM이 Hermes 관련 결정에 필수")와 정합.
docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md:110:**Reviewer 종합**: B의 ADR-011 means/ends 논거가 결정적이다. 외부가 제안한 명칭 "Human-authorized T3 change enforcement with Hermes credential isolation"은 *수단(credential isolation)*을 명칭에 박는다 — ADR-011 §2.1 수단/목적 분리 원칙 위반 소지. **목적(ends) = "Hermes가 T3 변경의 권위 주체가 될 수 없음"이며, credential isolation은 그 수단의 하나일 뿐.** 따라서 명칭은 유지하되, **중심 명제 = "credential boundary + external enforcement + audit의 결합 (metadata 판별기 아님)"을 합의 본문에 명시 권고.** brief 금지사항(G3 §2.2 #20 본문 변경 0건)과도 양립.
docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md:187:**Group I (Hermes-originated commit auto-reject)는 T3 보안 enforcement 영역으로 풀 3+1 (Agent A/B/C + Reviewer) 의무이며 Reviewer-only 단축은 부적격이다** (만장일치 — trigger #2 T3 BLOCKING + #5 핵심 제약 #1/#4 직결 + #7 외부 1건 충족 + §4 self-reference 구조). 세 Agent와 Reviewer의 G3 원문 검증(line 448 "author/committer + audit log cross-reference", line 784 "기준 자체가 단일 author 비교")이 일치시키는 핵심은 **현 G3 본문이 외부가 약하다고 지적한 metadata-기반 negative detection을 그대로 담고 있으며, positive allow-list 권고는 신규 제안이 아니라 이 설계 결함의 교정**이라는 점이다. 외부 5 보강점은 **전부 채택**(positive allow-list·runtime=sensor·`.git`=ACL 책무 = BLOCKING / GHES≠GitHub.com = 채택 / FP통제 = 조건부). BLOCKING 안전 조건은 **6건**(B-1 positive allow-list+신뢰등급 분리 / B-2 runtime=sensor·reject=Hermes 밖 / B-3 credential boundary 실분리 전제 / B-4 host 밖 anchor 최소 1개 의무 / B-5 R-I-CONFIG-CHANGE T3 / B-6 `.git/`=filesystem ACL 책무) + 조건부 3건(observe≠발효·FN우선 / negative-control-only / framing N1). framing은 **N1 (명칭 유지 + 중심 명제 명시)** 권고 — 외부 제안 명칭이 수단(credential isolation)을 명칭에 고정해 ADR-011 means/ends 원칙에 저촉되므로 전면 재정의 보류. C 발굴 신규 영역 중 **PR/approval auto-reject·책무 재정렬·audit tamper-resistance는 포함**(전자는 후속 단위 flag), credential isolation은 B-3으로 흡수. G3 line 448/784 결함은 **합의 권고로 기록하되 본문 교정은 별도 단계로 분리**하여 brief 금지사항(G3 본문 변경 0건)과 양립한다. 본 합의는 추론적 검증(권고) 한정 — 식별 방법·차단 지점·framing·G3 본문 교정의 실 *결정/구현*은 사용자 명시 + 별도 단계(Backlog #6 Runtime + CI-hook 연결)이며, **본 보고서는 코드/문서 본문 변경·commit·push 0건**이다.
docs/review/3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md:196:| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | FN(silent T3 위반) > FP(가시·복구가능) 비대칭 → "의심스러우면 quarantine". runtime self-reject = self-reference 역설(§4.1). single-host 3-layer 명목화 → host 밖 anchor 의무. ADR-011 means/ends로 framing 명칭 보류. 문서 정합성 검증 (과대선언·약화 없음). BLOCKING 4 + 조건부 3 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:3:> **합의 cycle (g1-A)**: format 가족별 분류 합의 (`d75dceb`, BLOCKING 16 + 권고 21 + NOTE 24, Reviewer 단독 격상 3) brief v1.1 (`eca4cf5`, 710줄) **§7.1 (A) 옵션 채택 자격 평가** cycle. brief v1 (`fc6731e`, 397줄) → 풀 3+1 합의 (Agent A/B/C 병렬 독립 → Reviewer 통합) 산출. **APPROVE w/ COND**, BLOCKING 16 + 권고 18 + NOTE 28, **기각 0**, **Reviewer 단독 격상 BLOCKING 3** (R-S1 / R-S2 / R-S3). 본 합의는 brief v1 의 진술을 BLOCKING 으로 정정하는 *권한* 을 가지나, **(1) ADR-011 §6 본문 정정 자격 0 + (2) Provider Liquidity 본질 약화 자격 0 + (3) MVP-1 합의 본문 정정 자격 0 + (4) 헌법 본문 정정 자격 0 + (5) 메모리 본문 정정 자격 0 + (6) 4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + 6축 framing 영구 정착 자격 0 (R-2 답습) + (7) 자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)** 의 **7 권한 한계 영구 답습**.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:46:- A-B4 ⭐: §6.2 raw line-level cross-check source 5 항목 (brief v1.1 / 합의 / ADR-011 / 메모리 / 헌법) 에 **본 (g1-A) brief 자체** 부재 → **R-11**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:53:- B-B1 ⭐⭐ → **R-S2 (Reviewer 격상)**: 헌법 5조 line 40~46 verbatim = "코드 품질 원칙" + 5 항목 (읽기 쉬움/SRP/중복/외부 입력/린터). "Provider Liquidity" 직접 본문 부재. ADR-011 line 6/245 *매핑* 의존 = **상위 단계 비대칭** (format 합의 R-S2 = ADR-011 *내부* 비대칭의 *상위 단계*)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:57:- B-B6: §5.3 Reviewer 권한 한계 7 항목 답습 자격 = "재서술 (강한)" vs "by-reference (약한)" boundary 명문 부재 → **R-7**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:69:- C-A3: Reviewer-only 단축 합의 대안 (ADR-011 모법 답습). **사용자 명시 정공법 발효 = 채택 자격 0**, 단 후속 cycle 단축 합의 자격 평가 별도 cycle — NOTE N-28
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:78:> Reviewer 권한 = (1) Agent 단독 발견을 BLOCKING 으로 격상 + (2) raw line-level direct cross-check 신규 BLOCKING 발의. 7 권한 한계 영구 답습 (헌법·ADR-011·MVP-1·메모리 본문 정정 자격 0 + 본질 약화 자격 0 + 영구 framing 정착 자격 0 + 자동 다음 단계 진입 자격 0).
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:94:  → 헌법 5조 본문 verbatim = "코드 품질 원칙", **"Provider Liquidity" 직접 본문 부재**. ADR-011 line 6 + line 245 의 "헌법 제5조 (Provider Liquidity)" = **ADR-011 *내부* 매핑** 자격. **상위 단계 비대칭** finding — 헌법 5조 본문 ↔ ADR-011 line 6/245 *매핑* 자체의 *내부 비대칭* (format 합의 R-S2 = ADR-011 *내부* line 6/212/245 비대칭의 *상위 단계*). B-B1 + B-S1 = Reviewer 격상 **BLOCKING R-S2**. **단 Reviewer 권한 한계 (헌법 본문 정정 자격 0) 답습** — 본 R-S2 = 매핑 자격 인정 + 매핑 자체 변경 자격 0 + 별도 cycle (헌법 amendment) 명문화 의무.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:123:**근거**: brief v1 §7.1 line 282~292 표 진입 자격 컬럼 = (a) "별도 brief + 풀 3+1" / (b) "별도 cycle" / (c) "별도 합의 cycle" / (d) "별도 brief" **4 형태 비균질** + Agent C 단독 발견 옵션 매트릭스 *방향성 비대칭* — 9 옵션이 모두 (가) cycle 가벼움 (g1-D4) 또는 (나) deep-dive (F~J/K/L/M) 양극 한정, **(g1-N) "본 cycle 결과 → 헌법 5조 본문 미세 보강 (Provider Liquidity 가족 분리 자격 1 줄 명문 추가)"** + **(g1-O) "본 cycle 결과 → ADR-011 line 212 본문 미세 보강 (가족 차원 적용 boundary 1 줄 명문 추가)"** *권위 본문 미세 보강 중간 옵션 누락*.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:130:> | **(g1-O)** | 본 cycle 결과 → ADR-011 line 212 본문 미세 보강 (가족 차원 적용 boundary 1 줄 명문 추가) — R-S2 답습 | 사용자 명시 + 별도 brief + 풀 3+1 (R-9 헌법급 변경) |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:139:본 brief v1 line 26 + line 88~94 + line 152~155 = "헌법 제5조 (Provider Liquidity, 비협상) line 40~46" 인용 = **두 차원 conflate** (line 40~46 본문 verbatim "코드 품질 원칙" ↔ "Provider Liquidity 비협상" ADR-011 매핑 의존). 본 finding = format 합의 R-S2 (ADR-011 *내부* line 6/212/245 비대칭) 의 **상위 단계 비대칭** — 헌법 5조 본문 ↔ ADR-011 line 6/245 매핑 *자체*. **Reviewer 권한 한계 영구 답습 — 헌법 본문 정정 자격 0**, 본 R-3 = 매핑 자격 인정 + 매핑 자체 변경 자격 0 + 별도 cycle (헌법 amendment, R-9) 의무 명문화.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:142:> "**헌법 5조 line 40~46 verbatim** = '제5조: 코드 품질 원칙' (5 항목 — 읽기 쉬움 / SRP / 중복 제거 / 외부 입력 검증 / 린터). **'Provider Liquidity (비협상)' 명시는 ADR-011 line 6 + line 245 *내부* 권위 매핑**. 본 cycle 답습 의무 = (i) 헌법 5조 본문 verbatim ≠ Provider Liquidity 직접 본문 + (ii) ADR-011 line 6/245 *상위 권위* 명시 = ADR-011 *내부* 매핑 자격 답습 only + (iii) 헌법 5조 본문 ↔ ADR-011 line 6/245 매핑 *자체* 의 비대칭은 format 합의 R-S2 답습 *상위 단계* 비대칭. **본 cycle 답습 = 매핑 자격 인정 only, 매핑 자체 변경 자격 0** (R-9 헌법급 변경 답습, 별도 cycle (g1-N) 의무)."
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:144:§3.1 권위 매핑 표에 "헌법 5조 본문 차원" / "ADR-011 line 6 매핑 차원" / "ADR-011 line 212 주제 범위 차원" / "ADR-011 line 245 관용 매핑 차원" **4 차원 분리 행** 신규.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:173:**근거**: brief v1 §5.3 line 245~252 = 7 항목 verbatim 재서술. format 합의 보고서 line 367~373 의 by-reference 자격 평가 부재. R-26 (NOTE carry-over by-reference only) 답습 *대칭* — 본 cycle 가벼움 명문 답습 시 *by-reference only* 자격 평가 의무.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:175:**정정 방향 (verbatim)**: brief v1.1 §5.3 본문 머리에 추가:
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:176:> "**Reviewer 권한 한계 7 항목 답습 자격 boundary**: 본 §5.3 = format 합의 보고서 (`d75dceb`) line 367~373 verbatim by-reference 답습 + 본 (g1-A) cycle 의 가벼움 명문 답습 차원 **재서술 (본 brief 본문 명시 형태) + by-reference (출처 line offset 명시 형태) 통합 답습**. 본 §5.3 의 어떤 항목도 본 cycle 새 생성 자격 0 — 모두 출처 by-reference 답습 (R-22 + R-26 답습). **Reviewer 권한 한계 7 항목 출처 chain**: Provider Liquidity 합의 보고서 (`a9e1e88`) line 365~373 → format 합의 보고서 (`d75dceb`) line 367~373 → 본 (g1-A) brief §5.3 line 245~252 (3 cycle carry-over chain, 본 cycle 신규 생성 0건)."
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:205:**근거**: 본 brief §6.2 line 268~273 = raw cross-check source 5 항목 (brief v1.1 / 본 cycle 합의 / ADR-011 / 메모리 / 헌법). 본 (g1-A) brief 자체가 source list 에 부재 — 본 cycle 합의 Agent 의 line offset 명시 의무 evidence 자격 미명문.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:275:| **R-31** | §5.1 3+1 분담안 표 직후 본문에 각 Agent raw line-level cross-check 의무 6 차원 (brief v1.1 / format 합의 / ADR-011 / 헌법 / MVP-1 / 메모리) 명시. line offset 부재 인용 = BLOCKING 격상 자격 (R-S* 격상 patterns 답습) | B-R4 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:294:### 5.3 본 cycle 신규 NOTE (N-25 ~ N-29) — 본 cycle 합의 결과 Agent + Reviewer 통합 산출
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:301:| **N-28** | Reviewer-only 단축 합의 대안 (ADR-011 line 3 모법 답습 패턴) 식별 carry-over. 사용자 명시 정공법 발효 = 본 cycle 채택 자격 0. 후속 cycle 단축 합의 자격 평가 별도 cycle (memory `feedback_staged_consensus_workflow` 답습 트리거 enum 의무) | C-A3 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:315:3. **7 권한 한계 영구 답습**: (1) ADR-011 §6 본문 정정 자격 0 / (2) Provider Liquidity 본질 약화 자격 0 (binary 본질 유지 영구) / (3) MVP-1 합의 본문 정정 자격 0 / (4) 헌법 본문 정정 자격 0 (R-S2 = 매핑 자격 인정 only, 매핑 자체 변경 자격 0) / (5) 메모리 본문 정정 자격 0 (R-S1 = brief 본문 *인용 line offset* 정정 only, 메모리 본문 자체 변경 0건) / (6) 4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + 6축 framing 영구 정착 자격 0 (R-2 답습) / (7) 자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:318:6. **R-S2 (헌법 5조 본문 비대칭) Reviewer 격상 자격 = 매핑 자격 인정 + 매핑 자체 변경 자격 0** — 본 격상 = format 합의 R-S2 (ADR-011 *내부* 비대칭) 의 *상위 단계* 비대칭 명문화 only, 헌법 본문 정정 자격 0
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification-option-a-adoption.md:343:**End of consensus report** (작성일 2026-05-24, format 가족별 분류 cycle (f-K) 5차 entry 풀 3+1 합의 산출, 결정 *고정* 0건, MVP-1·메모리·헌법·ADR-011 본문 정정 0건, 4 가족 분류 영구 framing 정착 0건, 6축 framing 영구 정착 0건, Provider Liquidity 본질 약화 0건, (g1-A) 자체의 영구화 정착 0건, brief v1.1 본문 변경 0건 명문 답습, 기각 0건, **Reviewer 단독 격상 3 (R-S1 메모리 line offset 정정 / R-S2 헌법 5조 본문 비대칭 / R-S3 NOTE 합산 정정) raw line-level direct cross-check 답습**)
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:12:> **상위 권위**: ADR-008 부록 C, ADR-008 차단조건 #4, ADR-009 §C-N §5 (Layer 1 모법 ADR), ADR-011 §2.1 (a)~(e), llm-providers-design.md §9.3 (depcruise rule grep 보조), implementation-runtime-roadmap.md §3.1 (Order 1)
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:113:### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:119:| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 부록 C / 차단조건 #4 / ADR-009 C-N §5 / ADR-011 §2.1 / llm-providers-design.md §9.3 / roadmap §3.1 cross-reference |
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:159:| 5 | ADR-009 / ADR-011 / llm-providers-design.md §9 와 충돌 | 0 | cross-reference 답습 한정 |
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:196:| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F + Group G |
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:204:| pre-commit hook 활성화 | T2 정책 영역 (ADR-011 §2.4) | 별도 합의 |
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:278:**APPROVE WITH CONDITIONS** — Group A 3차 PoC = G2 GP-5 *Layer 1c 정적 검출 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/6 발화, 8 금지 0/8 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 6/6 충족, 로컬 6/6 검증 PASS, CI workflow 12 step 형식 검증 PASS, llm-providers-design.md §9.3 + Group A 2차 #C-8 직접 답습 (변경 0건 / 외부 의존 0건 / Tier-2/3 확장 0)).
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:290:| C-A3-7 | Step 8 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §14 변경 이력 답습) | 본 합의 §5.3 #4 |
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:292:### 5.3 다음 단계 권고
docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md:311:| 2026-05-10 | 신규 작성 | Group A 3차 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 6 0/6 발화, 8 금지 0/8 위반, PASS 기준 6/6 + ADR-011 §2.1 5/5 충족, 로컬 6/6 PASS, CI workflow 12 step 형식 검증 PASS, llm-providers-design.md §9.3 + Group A 2차 #C-8 직접 답습 (변경 0건 / 외부 의존 0건 / Tier-2/3 확장 0). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group D/E/G 답습). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md:21:- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역 (CI step Entry)
docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md:374:| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md:430:| C-ε-18 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §7 답습 |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:5:> 본 합의의 어떤 §도 그 자체로 (i) **Hermes upstream Dockerfile *본문* 변경** (entrypoint stat 추가 / chmod 강제 / image 빌드 / perm 검증 코드 작성), (ii) **Hermes upstream PR 발송 / fork+downstream patch 적용 / downstream wrapper·entrypoint preflight·CI container test·init container *실 구현***, (iii) **chmod 600 능동 강제 / 위반 시 동작 fail-closed *고정* / 수단 *최종 결정***, (iv) **Hermes PMO 격상 (Layer F) 선언 / Operational Readiness PASS (Layer E) 선언**, (v) Group γ-2 (Vault HSM ST-4) / Group β / Backlog #1 ST-2 sidecar 자동 진입, (vi) Backlog #4 / #6 / #7 자동 진입, (vii) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (viii) Layer B (`f40423f`) ST-3 docker secret 본문 채택 변경, (ix) Layer D (`210c98f`) 본문 변경, (x) follow-up brief / Group α·β 합의 / γ-1 brief / prep brief 계보 본문 변경, (xi) 외부 LLM 응답 (Gemini + GPT) *결론 강제 채택* (응답 = 입력 한정), (xii) 외부 LLM *추가 자동 호출* / 재의뢰, (xiii) 실 API key / provider SDK / 외부 API 호출 / 실 secret material 처리, (xiv) ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012), (xv) **MVP-1 exit 발효 / MVP-2 자동 진입**, (xvi) 도구 본문 (`tools/*.py`) / CI workflow 변경 / actual run / Production `docker-compose.yml` / `requirements*.txt` 변경, (xvii) **Phase α defer-lockdown 변경**, (xviii) 5 영구 핵심 제약 (특히 Hermes ≠ root of trust) / Provider Liquidity 5-way 약화 를 발생시키지 않는다.
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:16:- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (entrypoint stat) + P3 (Credential/OAuth 파일 권한 노출, governance §104) + line 128 (`~/.hermes/auth.json`) / ADR-012 §원칙 9 + §2.8 (single-host SPOF 면책) / ADR-011 §2.1 (a)~(e) + §2.3 권위 위계 (Hermes ≠ root of trust) + §2.4 T3 영역 / governance-preconditions §1.2.7 P11 (Supply-chain Compromise)
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:83:| **Agent B** | 품질/안전성 검증가 ("안전하고 견고한가?") | Hermes ≠ root of trust + 5 영구 핵심 제약 + 위험·엣지케이스 + PMO 경계 안전성 + ADR-008 P3 / ADR-012 §원칙 9 / ADR-011 §2.3 정합 |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:115:| 사유 | downstream 형태 진입 적격 / **Hermes upstream Dockerfile 본문 직접 변경 + PMO 격상 자동 연결 = 분리 차단** (Hermes 가 자기 secret 안전성 *판단 주체* 화 = ADR-011 §2.3 권위 위계 + ADR-012 §원칙 9 약화) |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:119:| ADR 정합 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + P3 (entrypoint stat = P3 enforcement, downstream 명시 보강) / ADR-012 §원칙 9 (자동 복구 금지 → chmod 강제(b)보다 stat 검증(a) 우선) / ADR-011 §2.1 (a)~(e) 조건부 (수단 최종 결정 = downstream PoC Evidence 후) + §2.3 + §2.4 |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:239:| **C-Gγ1-9** | **Hermes ≠ root of trust 보존 (① HIGH blocking)**: "Hermes 자기 검증으로 안전" 금지. ADR-011 §2.3 운영함의 #1 (Hermes 출력은 Tools 로 검증) — secret perm 검증 주체 = Harness Gates 계층 (Hermes 외부). **P11 image 변조 방어 ↔ Hermes≠root 보존 = *동일* 외부 harness 검증 메커니즘** (E-γ1-9) + image digest 고정 (`FROM ...@sha256:<digest>`, P11 (iv)) | A §8 + B C-B-2/C-B-7 + C AU-3 (3/3 BLOCKING) |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:267:> **Hermes upstream 변경 = root of trust 침범 위험.** Hermes 가 "자기 자신의 secret 안전성을 판단하는 주체" 가 되면 ADR-011 §2.3 권위 위계 (Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents) + ADR-012 §원칙 9 약화. **보존책 (3/3 합의)**: (i) downstream-only 우선 (upstream 미접촉 = 자기 검증 주체화 여지 구조적 0) + (ii) 외부 harness 가 container behavior 검증 (Hermes 자기 검증 ≠ 안전 근거) + (iii) image build↔runtime check 분리 + rollback 가능 + (iv) P11 image 변조 방어 = 동일 외부 harness 메커니즘 + image digest 고정.
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:273:| **ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + P3** (Credential/OAuth 파일 권한 노출) | ST-1 = P3 enforcement 직접 구현 후보 — entrypoint stat 가 *downstream wrapper* 인지 명시 보강 (C-Gγ1-1) |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:275:| **ADR-011 §2.1 (a)~(e)** | 정책/downstream preflight = 충족 가능 / 수단 *최종 결정* = downstream PoC Implementation Evidence (실 container 측정) 후 별도 합의 |
docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md:291:| **ADR-011 §2.4** | T3 영역 (Hermes upstream 변경) 진입 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:22:- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5 조건 모법
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:65:- ❌ **ADR-011 §2.1 (a)~(e) 5 조건 *재정의* 0건**
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:163:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + ADR-010 (SQLCipher Vault) + R-4 + mvp1.md §3 + Layer B §5.5.1 ST-3 본문 채택 | — | ✅ 답습 변경 0건 | ✅ **충족** |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:276:### 5.3 15/15 + 18/18 풀 3+1 승격 트리거 0건 발화 답습
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:290:### 6.1 ADR-011 §2.1 (a)~(e) 5 조건 양 GP 충족 — GP-3 영역
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:296:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + ADR-010 + R-4 + mvp1.md §3 + Layer B §5.5.1 ST-3 — 본 합의 §3.1 (c) 검증 통과 | **본 합의 발효** |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:313:### 7.1 ADR-011 §2.1 (a)~(e) 5 조건 양 GP 충족 — GP-5 영역
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:341:| **Layer C 정의** | **MVP-1 Implementation Evidence PASS** — ADR-011 §2.1 (a)~(e) 5 조건 양 GP (GP-3 + GP-5) 충족 검증 후 발효 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:369:> **발효 근거**: ADR-011 §2.1 (a)~(e) 5 조건 × 양 GP (GP-3 + GP-5) = 10/10 evidence 충족 + 4/4 prerequisite actual runs PASS 답습 + 33/33 풀 3+1 트리거 0건 발화 답습
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:375:- ✅ ADR-011 §2.1 (a)~(e) 5 조건 × 양 GP (GP-3 + GP-5) 충족 검증 *발효*
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:400:| GP-3 PASS | ADR-011 §2.1 (a)~(e) 5 조건 충족 | ✅ **본 합의 발효** | — |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:401:| GP-5 PASS | ADR-011 §2.1 (a)~(e) 5 조건 충족 | ✅ **본 합의 발효** | — |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:463:| 26 | ADR-011 §2.1 (a)~(e) 5 조건 *재정의* | 0건 — 모법 답습 한정 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:475:| 38 | 수단/목적 분리 보존 변경 | 0건 — 영구 답습 (ADR-011 §2.1 (a)~(e) 5 조건 모법 답습) |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:532:| C-ι-12 | ADR-011 §2.1 (a)~(e) 5 조건 *재정의 0건* | 본 합의 §6 + §7 답습 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:535:| C-ι-15 | GP-3 PASS 발효 = ADR-011 §2.1 (a)~(e) 5/5 충족 + actual run `25728590939` + `25731846625` PASS 답습 | 본 합의 §6 답습 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:536:| C-ι-16 | GP-5 PASS 발효 = ADR-011 §2.1 (a)~(e) 5/5 충족 + actual run `25728590916` + `25728590977` PASS 답습 | 본 합의 §7 답습 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:546:| C-ι-26 | 풀 3+1 승격 트리거 0/33 발화 답습 (c13c011 §5 15 + brief §5.2 18) | 본 합의 §5.3 답습 |
docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md:570:본 합의 보고서는 **Layer C 발효 합의 실 진입 brief (`0862f74` APPROVE AS BRIEF, 11 섹션) 발효 후속**, **Step 0~2 사전 점검 3/3 통과 + Step 3 합의 형태 결정 = 옵션 A Reviewer-only 단축 합의 + Step 4 Skip 답습 후속**, **Step 5 *실 발효 시점* Reviewer-only 단축 합의 보고서**. **Step 0** 답습 commit chain 11/11 변경 0건 검증 통과 (Layer C 진입 가능성 합의 `c13c011` + Layer C 실 진입 brief `0862f74` + Phase α-1 ~ α-4 + Group α + Backlog #6 + Layer A + Layer B + §5.5 9 sub-수단). **Step 1** 양 GP × 5 조건 evidence 답습 검증 통과 — GP-3 × 5/5 적격 (368줄 `tools/secret_scanner.py` + 93줄 `docker/gp3-st3-poc/` + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + R-4 + Layer B §5.5.1 ST-3 + 694줄 `.github/workflows/secret-hygiene-egress-redaction.yml` + GP-3 MVP-1 진입/Stage 2/Phase α-3 합의 + Layer C 발효 시점) + GP-5 × 5/5 적격 (178+35+283줄 = 496줄 `tools/provider_*` + `.importlinter` + 3 subdir fixtures + 41줄 facade.py placeholder + ADR-008 차단조건 #4 + Layer B §5.5.2 T-6 + Group A 2차 풀 3+1 합의 + 186+326줄 = 512줄 `.github/workflows/provider-*` + GP-5 MVP-1 진입/Stage 4/Phase α-1/α-2/α-4 합의 + Layer C 발효 시점) = **10/10 evidence 적격성** + 9/9 evidence 파일 line count 정확 일치 + 변경 0건. **Step 2** 4 prerequisite actual runs PASS 답습 확정 (Stage 1 `25728590939` + Stage 3 `25728590916` + `25728590977` commit `72622409` + Stage 2 `25731846625` commit `6c6b208` 모두 SUCCESS) + 5 source cross-reference 일관 (c13c011 §3.4 + brief §3.3 + SESSION_2026-05-12 + SESSION_2026-05-14 + CONTEXT.md) + 재실행 0건 + 신규 trigger 0건. **Step 3** 합의 형태 = **옵션 A Reviewer-only 단축 합의** (사용자 명시 결정 2026-05-16 — brief §3.4 답습) + **Step 4 Skip** (단축 흐름 — brief §2.2 답습) + **풀 3+1 승격 트리거 0/33 발화 답습** (c13c011 §5 15 + brief §5.2 18). **GP-3 PASS *실 발효*** (ADR-011 §2.1 (a)~(e) 5/5 충족 + actual runs `25728590939` + `25731846625` PASS) + **GP-5 PASS *실 발효*** (ADR-011 §2.1 (a)~(e) 5/5 충족 + actual runs `25728590916` + `25728590977` PASS) + **Layer C — MVP-1 Implementation Evidence PASS *실 발효 선언*** (양 GP 동시 발효 + 사용자 명시 결정 답습). **혼동 방지 핵심**: Layer D MVP-1 PASS = 아직 아님 / Layer E Operational Readiness PASS = 아직 아님 / Layer F Hermes PMO 격상 = 아직 아님 (영구 답습). **사용자 명시 7 금지 위반**: #1 (실 Layer C 발효) = 사용자 명시 Step 5 결정 답습 / #2 ~ #7 모두 위반 **0건 영구 보존** (CI workflow / branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상). **추가 60 금지 영역 위반 0건** (MVP-1 PASS Layer D 선언 / 외부 LLM 자동 호출 / blind 의뢰서 작성 / vendor 자동 선택 / 외부 LLM 응답 결론 강제 채택 / actual run 자동 재실행 / 신규 actual run trigger / 양 GP × 5 조건 evidence 재생성 / R-4 + R-5 + R-7 + R-1 합산 2785줄 본문 어느 줄도 변경 / runtime code 변경 / Phase α-1 ~ α-4 자동 재진입 / 11 합의 본문 변경 / 8 합의 조건 enum 자동 변경 / ADR-011 §2.1 재정의 / Step 6 메타 갱신 자동 진입 / F-금지 #1 / Hermes upstream Dockerfile / Production docker-compose / 실 secret material / 실 API key / Hermes ≠ root of trust 보존 / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 보존 / Provider Liquidity 5-way 100% / Backlog #1 ~ #7 / PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 ~ ST-5 / Layer 2 runtime block / facade.py real 본문 / MVP-2 ~ MVP-6 deepening / 17 항목 재고정 / 신규 ADR / ADR 본문 자동 갱신 / event enum / threshold 고정 / Tier-2/3 catalog / commit signing / `pull_request_target` / token rotation / GitHub plan 확인 / Group I / Group β / γ-1 / γ-2 / Phase β / γ / 인간 리뷰 자동 발화 모두 0건). **종합 판정 = APPROVE — MVP-1 Implementation Evidence PASS (Layer C) + GP-3 / GP-5 PASS 발효** (Reviewer-only 단축 합의 적격 — 33/33 풀 3+1 트리거 0건 발화 답습) + **30 합의 조건 C-ι-1 ~ C-ι-30**. **본 합의는 Layer C — MVP-1 Implementation Evidence PASS (양 GP 동시 발효) 만을 *실 발효* 시키며, MVP-1 PASS (Layer D) / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 어느 것도 *발효* 시키지 않으며, R-4 / R-5 / R-7 / R-1 영역 본문 어느 줄도 *변경* 하지 않으며, CI workflow / branch protection / dev 환경 강제 / `pre-commit install` 의무화 어느 것도 *도입* 하지 않으며, Phase α-1 / α-2 / α-3 / α-4 어느 것도 *자동 재진입* 시키지 않으며, evidence 재생성 / actual run 재실행 / 신규 actual run trigger / 외부 LLM 자동 호출 어느 것도 *발생* 시키지 않으며, Step 6 메타 갱신 (CONTEXT / INDEX / SESSION) + commit + push 어느 것도 *자동 진입* 시키지 않는다**. 다음 단계는 사용자 명시 결정 영역 (§11.3 답습) — **Step 6 메타 갱신 (사용자 명시 결정 영역) / Layer D MVP-1 PASS 선언 합의 진입 brief / Phase α-1 ~ α-4 실 진입 step 분할 brief / Group α 조건 재평가 / Group I / token rotation 정책 / GitHub plan 가용성 확인 / 세션 종료**.
docs/review/3plus1-consensus-2026-05-20-gp3-c3-gp5-c2-t3-zone-resolution.md:16:- ADR-011 §2.4 T3 영역 / ADR-011 §2.1 (a)~(d) [+(e) 합의 패턴] / 5 영구 핵심 제약 / Layer D condition satisfaction 선례 (C-1/C-2 Satisfied 별도 commit)
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:12:> **상위 권위**: ADR-008 부록 C (Design/Governance ↔ Implementation/Runtime 분리), ADR-011 §2.1 (a)~(e), ADR-012 §2.9 / §2.10, G4 §4.2 / §4.6, governance-preconditions.md §8 (GP-6), implementation-runtime-roadmap.md §3.1 / §5.3 / §5.4
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:68:### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:74:| (c) ADR/SDD 권위 명시 | ✅ | 사양 + 본 합의 헤더 = ADR-008 부록 C / ADR-011 §2.1 / ADR-012 §2.9 / G4 §4.2 / §4.6 / GP §8 / roadmap §3.1 cross-reference |
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:135:| 5 | G4 / ADR-012 / ADR-011 원칙 충돌 | 0 | 답습만 (사양 §0 + §5 cross-reference) |
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:259:**APPROVE WITH CONDITIONS** — Group F PoC = G2 GP-6 *feasibility 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/6 발화, F-금지 0/9 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 9/9 충족, F-범위 10/10 충족, 로컬 4/4 PASS, CI workflow 12 step 형식 검증 PASS).
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:291:| C-F-6 | Step 9 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §11 변경 이력 답습) | 본 합의 §5.3 #4 |
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:293:### 5.3 다음 단계 권고
docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md:314:| 2026-05-10 | 신규 작성 | Group F 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 0/6 발화, F-금지 0/9 위반, F-범위 10/10 + PASS 기준 9/9 + ADR-011 §2.1 5/5 충족, 로컬 4/4 PASS, CI workflow 12 step 형식 검증 PASS, Group C 산출물 import 직접 (리팩토링 0 / 복제 0). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group B/C 답습). Step 9 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:1:# 3+1 합의 보고서 — Jarvis MVP-1 (g1-N-2) ADR-011 line 6/245 매핑 정정 commit 자격 평가 합의 cycle entry brief
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:3:> **합의 cycle (g1-N-2)**: (g1-N-1) commit (`148fbbe`, 헌법 5조-2 신설) 후속 carry-over cycle. brief v1 (`8207f55`, 488줄) → 풀 3+1 합의 산출. **APPROVE w/ COND**, BLOCKING 10 + 권고 10 + NOTE 11, **기각 0**, **Reviewer 단독 격상 BLOCKING 3** (R-S1·R-S2·R-S3). **R-9 답습 영구 의무 (g1-N-2) carry-over 직접 발효 + Reviewer 권한 한계 (1) "ADR-011 §6 본문 정정 자격 0" 영구 답습의 예외 자격 발효 시점** (R-13 (4-c) 동형 패턴 적용, ADR-011 §6 차원). 본 합의 후 단계 (4) = brief v1.1 + ADR-011 line 6/245 매핑 정정 단일 atomic commit (R-19 답습 단계 (4) 직접 적용).
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:6:**범위 (사용자 명시 — "(g1-N-2)" + 정공법 + 단독)**: ADR-011 line 6 + line 245 매핑 정정만 ((g1-O) line 212 + (g1-N-3) CLAUDE.md/roadmap 변경 0건)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:9:**Reviewer raw line-level direct cross-check**: ADR-011 line 244~246 verbatim 직접 read (line 245 = "- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)" entire verbatim, R-S1 격상 evidence 확정) / 헌법 line 75~81 + line 80 verbatim 직접 read (line 80 = "ADR-011 line 6 상위 권위 매핑 답습 (\"헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)\")" R-S2 격상 evidence 확정) / 본 brief v1 line 1~488 cross-check
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:15:**APPROVE w/ COND** — 3 에이전트 모두 APPROVE w/ COND 일치 (REJECT 0건). brief v1 의 (g1-N-2) ADR-011 매핑 정정 framework (R-9 답습 영구 의무 + Reviewer 권한 한계 (1) 예외 자격 발효 명문 + (g1-N-1) carry-over + N-61 임시 stale 정합 회복 + 단독 범위 명시) 합의 input 자격 충족.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:43:- A-B1 + A-S1 ⭐⭐ → **R-2 (R-S2 격상)**: line 6 변경 후 헌법 line 80 self-reference 임시 stale 양방향 trade-off 발생 — (g1-N-1) commit 결과 line 80 항목 4 = ADR-011 line 6 변경 *전* verbatim 직접 인용 → 본 cycle commit 후 헌법 line 80 ↔ ADR-011 line 6 실 본문 verbatim **임시 stale 신규 발효**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:47:- A-S3: ADR-011 line 1~5 메타데이터 + line 240~244 + line 246~290 변경 0건 명문 부재 → **R-5 (NOTE 또는 권고 carry-over)**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:72:- C-S1: 변형 A "Provider Liquidity, 비협상" 토큰 순서 vs 헌법 line 75 "원칙" 토큰 부분 비대칭 (ADR-011 내부 일관성 보존 우선 정합) → **NOTE N-신규**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:75:- C-S4: ADR-011 line 7 "동시 발행" 시점 명문 부재 → **NOTE N-신규**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:80:- **R-S1 (B-B1 + B-B4 + B-S1 통합 격상)** ⭐⭐⭐ — **본 합의 가장 큰 finding**: Reviewer 직접 raw cross-check — ADR-011 line 245 entire verbatim:
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:86:  > `4. 본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ("헌법 제8조 (보안), **헌법 제5조 (Provider Liquidity)**"). **다른 권위 위계 (예: 8-2조 환경 관리 원칙 vs 5조-2) 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무**`
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:88:  → 헌법 line 80 = **ADR-011 line 6 변경 *전* verbatim 직접 인용** ("헌법 제5조 (Provider Liquidity)"). 본 (g1-N-2) cycle commit 후 ADR-011 line 6 = "헌법 제5조-2 (Provider Liquidity, 비협상)" → **헌법 line 80 인용 verbatim ↔ ADR-011 line 6 실 본문 verbatim 임시 stale 양방향 trade-off 신규 발효**:
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:89:  - 본 cycle commit *전*: ADR-011 line 6 *임시 stale* (헌법 5조-2 신설 후 미정합) — 본 cycle commit 으로 종료
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:90:  - 본 cycle commit *후*: 헌법 line 80 *임시 stale* (ADR-011 line 6 변경 후 헌법 line 80 인용 verbatim 미정합) — 신규 발효
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:98:  - 정합성 자체 충족 — 헌법 line 75 verbatim "## 제5조-2: Provider Liquidity 원칙 (비협상)" 답습 + ADR-011 line 245 변경 전 "비협상" 토큰 형식 대칭화
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:107:### R-1 (= R-S1) — ADR-011 line 245 verbatim 부분 추출 → entire verbatim 명시 의무 (B-B1 + B-B4 + B-S1 + A-B2 + A-R3 통합)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:126:§2.4 line 158 표의 "ADR-011 line 245 매핑" 행 정정 — entire verbatim 명시 (bullet + path + 8조 prefix + 5조 → 5조-2 정정 부분 명확).
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:133:헌법 line 80 (5조-2 항목 4) 인용 verbatim ↔ ADR-011 line 6 실 본문 verbatim 사이 *임시 stale* 자격 신규 발효 (R-S2 격상) — 본 cycle commit 후 헌법 line 80 = "헌법 제5조 (Provider Liquidity)" 인용 (변경 *전*) ↔ ADR-011 line 6 실 본문 = "헌법 제5조-2 (Provider Liquidity, 비협상)" 정합 미일치. 헌법 본문 변경 자격 = (g1-N-3') 또는 별도 cycle 의무 (R-S4 답습 carry-over 영구).
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:138:| 시점 | ADR-011 line 6/245 stale 자격 | 헌법 line 80 stale 자격 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:150:- (ii) "비협상" 명문 추가 = 본문 의미 보강 (헌법 line 75 verbatim "## 제5조-2: Provider Liquidity 원칙 (비협상)" 답습 + ADR-011 line 245 "비협상" 토큰 형식 대칭화) — 매핑 정정 *초과* 변경
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:152:**자격 boundary**: 본 cycle 예외 자격 발효 = 단순 reference 정정 *및* 헌법 line 75 verbatim 직접 답습 한정. 본 cycle 외 ADR-011 §6 본문 *의미 변경* 자격 0 영구 답습 (Reviewer 권한 한계 (1) carry-over 영구).
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:164:### R-5 — ADR-011 line 1~5 메타데이터 + line 240~244 + line 246~290 변경 0건 명문 부재 (A-S3)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:168:| ADR-011 line 1~5 메타데이터 + line 240~244 (§8 header) + line 246~290 (§8.2/§8.3) | 본 cycle 변경 0건 | 0건 (본 cycle 단독 범위 = line 6 + line 245 only) |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:175:(7) 본 cycle = *실 본문 변경 commit 적용 cycle* | R-19 답습 trigger 정확한 form **단계 (2) 진입 (현재 brief v1 commit 시점)**, **단계 (4) 직접 적용 시점 = brief v1.1 + ADR-011 line 6/245 단일 atomic commit (예정)**. (g1-N-1) cycle 답습 패턴. **본 brief v1 commit 자체 시점 (단계 2) = (7) 답습 의무 활성화, 단계 (4) 시점 = (7) 직접 충족**
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:189:5. **brief v1.1 보강 + ADR-011 line 6/245 매핑 정정 단일 atomic commit (R-19 답습 단계 (4)) — *본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit***. **commit message** (Conventional Commits, CLAUDE.md §5 + 헌법 9조 line 83 답습): `docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)` 권고. **단일 atomic commit**: brief v1.1 (`docs/phase0/...`) + ADR-011 (`docs/decisions/...`) 2 파일 1 commit
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:208:❌ ADR-011 line 6 만 정정 + line 245 stale 유지 / 또는 line 245 만 정정 + line 6 stale 유지 (부분 정정) — 동시 정정 의무 영구 답습 (R-S2 답습 영구 의무 추가 trigger 차단)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:219:| **R-13** | §1.4 (2) "ADR-011 본문 변경 차원 *간접 모법* (R-9 답습 영구 의무 일반 확장)" 어휘 boundary 명문 강화 (헌법 line 105 = 헌법 본문 차원 직접 매핑 vs ADR-011 차원 일반 확장 boundary) | B-R1 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:222:| **R-16** | §11.1 row 7 placeholder fill 의무 명시 — brief v1 commit hash + 본 합의 commit hash + brief v1.1 + ADR-011 단일 atomic commit hash 3 fill 의무 | C-S5 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:223:| **R-17** | line 6 변경 후 "Provider Liquidity, 비협상" 토큰 순서 vs 헌법 line 75 "Provider Liquidity 원칙 (비협상)" 토큰 *부분 비대칭* 명문 ("원칙" 토큰 부재 = ADR-011 내부 일관성 보존 우선 발효) | C-S1 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:224:| **R-18** | ADR-011 line 7 "ADR-008 부록 B Amendment (동시 발행)" 의 "동시 발행" 시점 명문 — ADR-011 *최초* 발행 시점 한정 의미 (2026-05-06), 본 (g1-N-2) cycle 의 ADR-011 §6 매핑 정정과 차원 다름 명문 강화 | C-S4 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:225:| **R-19** | ADR-011 line 6 "system-identity-prequel.md §3" reference carry-over = ADR-011 §8.1 (Archived 2026-05-09 후속 8) + ADR-011 §2.3/§2.4 영구 권위 승격 명문 직접 답습 → 본 cycle 변경 0건 영구 carry-over 명시 | C-S3 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:239:| **7 (본 cycle)** | **(g1-N-2) ADR-011 line 6/245 매핑 정정** |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:246:| **N-71** | 헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off carry-over (R-S2 격상) — 본 cycle commit 후 헌법 line 80 임시 stale 신규 발효, (g1-N-3') 또는 별도 cycle 의무 영구 carry-over | R-2 + R-S2 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:251:| **N-76** | "Provider Liquidity, 비협상" 토큰 순서 vs 헌법 line 75 "원칙" 토큰 부분 비대칭 (ADR-011 내부 일관성 보존 우선) | C-S1 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:252:| **N-77** | prequel.md §3 reference carry-over = ADR-011 §8.1 (Archived 2026-05-09 후속 8) 영구 권위 승격 명문 직접 답습 carry-over | C-S3 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:253:| **N-78** | ADR-011 line 7 "동시 발행" 시점 = 최초 발행 시점 (2026-05-06) 한정, 본 cycle 매핑 정정과 차원 다름 carry-over | C-S4 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:257:### 5.3 NOTE carry-over 정정 의무 (R-S1~R-S5 답습 영구)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:269:1. **본 합의 = brief v1 (`8207f55`, 488줄) + Agent A/B/C 출력 + Reviewer raw line-level direct cross-check** (ADR-011 line 1~30 + line 200~250 + line 244~246 verbatim / 헌법 line 75~81 + line 80 + line 104~105 / 본 brief 약 30 line offset) 한정
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:270:2. **본 합의 = brief v1 *진술* BLOCKING 정정 권한 + brief v1.1 본문 정정 자격 (R-21 답습) + line 6/245 verbatim 채택 자격 평가 권한 (R-13 (4-c) 동형 패턴 적용, ADR-011 §6 차원)** 만 보유
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:271:3. **8 권한 한계 영구 답습**: (1) ADR-011 §6 본문 정정 자격 = 본 cycle 합의 채택 + 단일 atomic commit 시점 예외 자격 발효 / (2) Provider Liquidity 본질 약화 자격 0 (매핑 정정만, binary 본질 유지) / (3) MVP-1 합의 본문 정정 자격 0 / (4) 헌법 본문 정정 자격 0 ((g1-N-1) commit 결과 유지) / (5) 메모리 본문 정정 자격 0 / (6) 4 가족 분류 + 6축 framing 영구 정착 자격 0 / (7) 자동 다음 단계 진입 자격 0 / (8) 결합 cycle 진입 자격 평가 자격 0
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:281:13. **본 cycle = R-9 답습 영구 의무 (g1-N-2) carry-over 직접 발효 + Reviewer 권한 한계 (1) 예외 자격 발효 시점** — 본 합의 채택 시 (4) brief v1.1 + ADR-011 line 6/245 단일 atomic commit 진입 자격 발효
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:288:2. **사용자 검토 + 명시 대기** — 본 합의 결과 확인 + brief v1.1 보강 + ADR-011 동시 commit 진입 자격 명시. 자동 다음 단계 진입 0건
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:289:3. 사용자 명시 → **brief v1.1 보강 + ADR-011 line 6/245 매핑 정정 단일 atomic commit** (R-19 답습 단계 (4))
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:293:   - **ADR-011 본문 변경**: line 6 "헌법 제5조 (Provider Liquidity)" → "헌법 제5조-2 (Provider Liquidity, 비협상)" + line 245 "제5조 관용" → "제5조-2 관용" 2 위치 정정
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:294:   - **commit message**: `docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)` (Conventional Commits, R-8 답습)
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:295:   - **단일 atomic commit**: brief v1.1 + ADR-011 2 파일 1 commit
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md:303:**End of consensus report** (작성일 2026-05-24, (g1-N-2) ADR-011 line 6/245 매핑 정정 commit 자격 평가 합의 cycle = brief progression chain 7번째 cycle entry, R-9 답습 영구 의무 (g1-N-2) carry-over 직접 발효 + Reviewer 권한 한계 (1) 예외 자격 발효 시점 (R-13 (4-c) 동형 패턴 적용), MVP-1·메모리·헌법·ADR-008 본문 변경 자격 0, Provider Liquidity 본질 약화 자격 0 (매핑 정정만, binary 본질 유지 + 명문화 강화), 자동 채택·자동 기각·결합 cycle 자동 진입 자격 0건, **Reviewer 단독 격상 3 (R-S1 line 245 entire verbatim 부분 추출 / R-S2 헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off / R-S3 "비협상" 명문 추가 boundary) raw line-level direct cross-check 답습**)
docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md:6:> **상위 권위**: ADR-008 차단조건 #2 (Evidence Ledger Hermes 의존 0), ADR-011 §2.1 (a)~(e), ADR-012 §2.3/§2.5/§2.6/§2.7/§2.9, G4 §4.2/§4.4/§4.6, P2 v3 §6 (G4 답습 권위), `implementation-runtime-roadmap.md` §4.1 (G4 7 영역 — Order 3 tie 3건)
docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md:72:### 3.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)
docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md:147:| ADR-011 §2.1 (a)~(e) | 수단/목적 분리 5조건 | ✅ 본 합의 §3.1 5/5 충족 |
docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md:148:| ADR-011 §2.4 (T1/T2/T3) | T3 자동 정책 변경 금지 | ✅ chain violation = BLOCK + manual + violation entry (자동 revert 0건) — 사양 §4.2 검사 3 답습 |
docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md:184:- ADR-011 §2.1 (a)~(e) 5/5 충족 (본 합의 §3.1)
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-download.log:172:5210112K ........ ........ ........ ........ 11% 25.3M 25m58s
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-download.log:423:13434880K ........ ........ ........ ........ 28% 35.3M 20m59s
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-download.log:623:19988480K ........ ........ ........ ........ 42% 25.3M 17m1s
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-download.log:1060:34308096K ........ ........ ........ ........ 72% 25.3M 8m11s
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:6:**보조 참조**: `docs/architecture/implementation-runtime-roadmap-mvp1.md` §4 + §5 (commit `cddd22f` + `bbc05ca`), `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` §1.6 + §5.1 (commit `95be2e5`), `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (commit `6dc5bdc` — 답습 형식), `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` (Group A 1차), `docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md` (Group A 2차 SCOPE), `docs/phase0/g2-gp5-poc2-import-linter-implementation.md` (Group A 2차 구현), `docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md` (Group A 3차), `docs/architecture/governance-preconditions.md` §7 (GP-5 Entry/Exit), `docs/architecture/llm-providers-design.md` §9 (Liquidity 위반 패턴 차단), `docs/decisions/ADR-008-hermes-adoption-decision.md` 차단조건 #4, `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` C-N §2.3 + §5, `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.2 (event enum)
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:33:| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — 진입 적격성) | ✅ |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:43:1. **사후 외부 LLM 충족** — 본 검토 답습 출처 (Group A 1차/2차/3차 PoC + Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄, T-2 import-linter 채택) + ADR-008 + ADR-009 C-N + ADR-011 + ADR-012) 모두 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 + Group A 2차 풀 3+1 합의 (T-1 vs T-2 vs T-3 vs T-4 결정) 자체가 외부 LLM 답습 (`external-review/2026-05-09-g2g3g4-promotion-response-claude.md` L39 + L51 답습 — depcruise 본질적 한계 3종 명시)
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:47:5. **수단 조합 *진입 적격성* 한정** — 본 합의 ≠ 수단 *본문 채택* — Implementation Evidence PASS 발효 시점에 ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 별도 합의 의무 답습
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:53:| GP-5 Implementation Evidence PASS 선언 | ❌ (별도 합의 영역 — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정) |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:138:| T2 영역 적격성 | T2 (CI step) — ADR-011 §2.4 답습, T3 미진입 | ✅ |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:224:| 5 | **ADR-011 T3 영역에 닿는 경우** | 본 합의 = T-6 + PC-3 + AR-1 모두 T2 영역 (CI step + 권고 수단 채택 권위). T3 영역 진입 = 별도 합의 영역 분리 명시 (Conditions C-2) | ❌ 0 |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:247:### 5.3 5 통제 답습
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:253:| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.4 5 sub-수단 모두 T2 영역 + T3 진입 영역 분리 + Conditions C-2 |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:254:| 4 | 수단/목적 분리 원칙 답습 | ✅ §1 + §2 모두 *수단 후보 평가* (목적 = Provider Liquidity 5-way Layer 1 모법 보존) — ADR-011 §2.1 (a)~(e) 5조건 답습 + ADR-009 C-N §5 모법 ADR 답습 |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:307:- ❌ 수단 *본문 채택* commit (T-6 / PC-3 / AR-1 = 진입 *적격성* 권위 권고 한정, 본문 채택 commit = 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시)
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:326:| (b+c 통합 시점, 사용자 명시 다음 단계) | **MVP-1 roadmap §5.4 통합 위험 sub-section 신설** (Observation O-2 흡수) | 단축 합의 적격 (양 GP Rollback 답습 + ADR-011 §2.1 5/5 답습 영역) | **C-4 흡수** (Observation O-2 — 사용자 명시 처리 시점 답습) |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:334:| (e-2) | **GP-5 Implementation Evidence PASS 발효 합의** | 별도 합의 + 사용자 명시 + ADR-011 §2.1 (a)~(e) 5/5 evidence | (전체 conditions 충족 후) |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:358:| PC-4 (PC-1 + PC-3 병행) | 단축 합의 + 사용자 명시 | T2 정책 영역 (ADR-011 §2.4) |
docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md:380:| MVP-1 roadmap §5.4 통합 위험 sub-section 신설 | **본 GP-5 합의 후속 영역** (사용자 명시 답습 — "GP-5 합의 완료 후 MVP-1 roadmap §5.4 통합 위험 sub-section 신설") | 단축 합의 적격 (양 GP Rollback 답습 + ADR-011 §2.1 5/5 답습 영역) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:11:- Governance preconditions = `docs/architecture/governance-preconditions.md` §5.3 (강제 메커니즘) + §5.4 (Evidence (a)~(e))
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:12:- ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 권위, 35번째 entry R-S1 정정 답습)
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:13:- ADR-011 §2.4 T1/T2/T3 3-tier 분류 (영역 분류 권위)
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:50:| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — brief 분류 + 합의 형태 권고 한정, T1 deterministic 자동 0 + T3 영역 침범 0) | ✅ |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:81:| ADR 본문 *자동 갱신* | ❌ (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:84:| Hermes upstream 변경 / 외부 LLM 자동 호출 | ❌ (ADR-008 차단조건 #6 답습 + ADR-011 답습, 35번째 entry R-S1 정정 답습) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:111:| T2/T3 분류 | **T3** | ADR-011 §2.4 답습 — "Constitution / ADR / Harness Gates 정의 자체의 변경" |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:115:- ADR-011 §2.4 T3 정의 = "자동 금지 (절대) — Constitution / ADR / Harness Gates 정의 자체의 변경"
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:120:**판정**: ✅ **적절** — Hermes upstream 변경 = T3 영역 (ADR-011 §2.4 + mvp1.md §3.5 + §3.6.3 답습 일관성). brief §2.1.2 + §2.4 분류 권위 근거 충실.
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:130:| T2/T3 분류 | **T2** | ADR-011 §2.4 답습 — "사용자 승인 필수 — Skill/Memory promotion, 새 도구 등록, 합의 형태 결정" |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:134:- ADR-011 §2.4 T2 정의 = "사용자 승인 필수 — Skill/Memory promotion, 새 도구 등록, 합의 형태 결정"
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:137:- brief §2.2.3 = "단축 합의 + 사용자 명시 결정 (T2 정책 영역, ADR-011 §2.4 답습)" — ADR-011 §2.4 T2 답습 충실
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:139:**판정**: ✅ **적절** — Hermes upstream 변경 0건 + sidecar 분리 가능 = T2 영역 (ADR-011 §2.4 + mvp1.md §3.3 답습 일관성). brief §2.2.2 + §2.4 분류 권위 근거 충실.
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:147:| `.pre-commit-config.yaml` 본문 정의 | T2 | ADR-011 §2.4 답습 — Skill/Memory promotion / 새 도구 등록 / 합의 형태 결정 |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:155:- ADR-011 §2.4 T3 정의 = "자동 금지 (절대) — Constitution / ADR / Harness Gates 정의 자체의 변경" — dev 환경 강제 정책 = repo policy 영역 = T3 부분 중첩
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:156:- brief §2.3.3 = 2 sub-영역 분리 (T2 config 정의 + T3 dev 환경 강제) — mvp1.md §4.3.1 + ADR-011 §2.4 답습 충실
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:204:| PC-4 의 PC-1 부분 (`.pre-commit-config.yaml` 본문 정의) | 단축 합의 + 사용자 명시 결정 (T2 정책 영역, ADR-011 §2.4 답습) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:210:- ADR-011 §2.4 = T2 (사용자 승인 기반) vs T3 (자동 금지 절대) = *합의 형태 의무 차이* 발생 — T2 단축 합의 적격 / T3 풀 3+1 + 외부 LLM + 사용자 명시 의무
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:214:**판정**: ✅ **적절** — mvp1.md §4.3.1 본문 "T2 + T3" 분류와 ADR-011 §2.4 합의 형태 의무 차이를 합리적으로 흡수하는 분리. *세분화 한정* 답습 (본문 변경 0건). 단, **본 합의는 PC-4 sub 영역 진입 *발효* 를 발생시키지 않음** — 진입 시점 = 별도 합의 영역.
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:243:| 1 | ST-1 T3 영역 분류 적절성 | ✅ 적절 (ADR-011 §2.4 + mvp1.md §3.5 + §3.6.3 답습) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:244:| 2 | ST-2 T2 영역 분류 적절성 | ✅ 적절 (ADR-011 §2.4 + mvp1.md §3.3 답습) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:248:| 6 | PC-4 T2 sub / T3 sub 분리 적절성 | ✅ 적절 (mvp1.md §4.3.1 본문 + ADR-011 §2.4 합의 형태 의무 차이 흡수) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:251:**합산 = 7/7 적절** — 본 brief 의 영역 분류 + 합의 형태 + T2/T3 분리 + 4 금지 답습 모두 권위 근거 충실 (Layer D / mvp1.md §3 / §4 / §5.5 / ADR-008 / ADR-011 답습).
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:305:| 10 | ADR 본문 *자동 갱신* (ADR-008 / ADR-010 / ADR-011 / ADR-012) | 0건 (cross-reference 답습 한정) |
docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md:389:| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ (T3 영역 자동 진입 0건 / T2 영역 단축 합의 적격 명시) |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:16:P2 v3 *Design Adoption only* 한정 정식 채택은 **APPROVE WITH CONDITIONS** — 5 평가 차원 (Hermes PMO 격상 분리 / ADR-012·G4·P10 반영 / Hermes ≠ root of trust / Provider Liquidity 5-way / 자동 정책 변경 부재) 모두 *Design 권위 격상* 차원에서 적격이며 영구 핵심 제약 5건 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) 의 보호 layer 도 ADR-009 C-N + ADR-011 §2.3 + ADR-012 §원칙 5/6 + §2.12 매트릭스로 *영구 권위 layer* 가 존재하나, **P2 v3 §0.2 / §2 / §3 / §6 / §7 / §10 본문이 ADR-012 + G4 §4.2/§4.4/§4.6 + G2 §1.2.6 P10 + ADR-009 C-N + Provider Liquidity 5-way 를 *내부 답습* 으로 명시 흡수하지 않으면 archive 후 권위 layer drift (특히 Provider Liquidity 5-way Layer 5 와 Hermes 변조 차단 매트릭스 4항목) 위험이 *정식 채택 시점* 에 1회 동결된다**. C-14 응답 2건의 7+4 핵심 조건 모두 *본문 흡수 권고* 범주이며, P2 v3 본문 *현 상태* 자체가 차단 사유는 아니다 (C-14 1 §7.10 / C-14 2 §7.10 모두 APPROVE WITH CONDITIONS — 진입 승인 + 4~7 조건 흡수 의무).
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:22:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신 권유 (cross-reference 권고 한정)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:57:§1.1 ~ §1.5 5 hub 모두 *evidence chain* (R-2 ~ R-7 + R-6 actual run `25482284523`) 답습 정합. ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 (§1.4 R-4 / R-4.1 / R-5 / R-6 cross-reference). **§1.3 차단조건 #1 충족 메커니즘 갱신** = G1b PASS evidence 흡수의 *수단/목적 분리* 본문 정합 (보안 결과 = DB 평문 secret 차단, 수단 = SQLCipher trigger + REGEXP UDF + Tier-1 42 catalog).
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:67:| §2.1.1 격상 후 책임 10항목 | T1/T2/T3 권위 등급 명시 | **PASS** — ADR-011 §2.4 답습 정합 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:68:| §2.1.2 Hermes 가 *하지 않는* 것 (영구 6항목) | T3 + Hermes-originated commit auto-reject | **PASS** — ADR-011 §2.3 + §2.4 답습 정합 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:69:| §2.2 권위 위계 (Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents) | ADR-011 §2.3 영구 권위 인용 | **PASS** — system-identity-prequel §3 ADR 승격 답습 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:70:| §2.3 5 운영 함의 | ADR-011 §2.3 답습 | **PASS** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:140:| §4.3 Entry / Exit 기준 | (a)~(e) ADR-011 §2.1 패턴 답습 | **PASS** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:142:| §4.5 의존 ADR / 갱신 후보 | ADR-008 / ADR-011 + 신규 ADR-012 후보 | **PARTIAL** — ADR-012 = 2026-05-09 정식 발행, *후보* → *발행됨* 갱신 의무 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:159:| §5.1 정의 | ADR-011 §2.3 권위 위계 + 5 운영 함의 운영 가능 메커니즘 | **PASS** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:161:| §5.3 prequel §3.3 4 강제 메커니즘 | filesystem read-only / 합의 결과 git commit 우회 / audit log / 자동 reject | **PASS** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:165:| §5.7 의존 ADR / 갱신 후보 | ADR-011 §8.5 + ADR-008 부록 + 신규 ADR-013 후보 | **PASS** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:167:**ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목** (Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조) cross-reference 부재 — §5.2 또는 §5.3 에 *G3 ↔ ADR-012 §2.12 통합 매트릭스* 명시 권고. 본 매트릭스가 P2 v3 §5 본문에 직접 답습되지 않으면 archive (P2 v2 + system-identity-prequel) 후 *Hermes 변조 차단 layer* 의 *영구 권위 layer drift* 위험.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:172:- C-5 (ADR-012 §2.12 + G3 §5 답습): §5.2 / §5.3 에 Hermes 변조 차단 매트릭스 4항목 + PASS 성립 4 요건 cross-reference 흡수 의무 (Gap-6 HIGH)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:207:§7 표 (ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신 항목) 가 ADR-012 (2026-05-09 발행) + ADR-009 C-N (2026-05-09 후속 4) cross-reference 0건. 본 합의 진입 후 ADR 본문 자동 갱신 *금지* 답습이지만 **cross-reference 매트릭스 갱신** 은 P2 v3 정식 채택 합의 *내부* 작업으로 가능 (C-14 1 §7.4 + Gemini §7.4 cross-vendor 일치).
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:239:- Hermes ≠ root of trust (ADR-011 §2.3)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:241:- 자동 정책 변경 금지 (T3, ADR-011 §2.4)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:242:- 수단/목적 분리 (ADR-011 §2.1 (a)~(d) 4조건)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:249:> Archiving P2 v2 or system-identity-prequel does not weaken, supersede, or delete the five permanent constraints. If any archived document contains stronger wording, the stronger constraint remains preserved through ADR-011 / ADR-012 and this section.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:269:§12 5 통제 수단 (사용자 명시 절차 답습 / R-7 SOP 답습 / ADR-011 §2.4 답습 / 수단/목적 분리 답습 / *하지 않는* 것 명시) 모두 *영구 답습*. 본 합의 진입 시 동일 메타 편향 통제 layer 유지.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:341:| Layer 1 | ADR-011 §2.3 영구 권위 | 권위 위계 + 5 운영 함의 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:361:| ADR-011 §2.4 T3 자동 정책 변경 절대 금지 | ADR-011 §2.4 + ADR-012 §2.7 (BLOCK + manual + chain_violation_detected) | **HIGH** (T3 영역) |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:406:ADR-011 §2.4 T3 정의:
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:482:**2. Hermes ≠ root of trust (ADR-011 §2.3 영구 권위)** — **HIGH (조건부 — 흡수 시)**
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:486:| Layer 1 | ADR-011 §2.3 (영구 권위) | ✅ |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:505:**4. 자동 정책 변경 금지 (T3, ADR-011 §2.4)** — **HIGH 5/5**
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:509:| Layer 1 | ADR-011 §2.4 영구 권위 | ✅ |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:517:**5. 수단/목적 분리 (ADR-011 §2.1 (a)~(d) + (e) 5조건)** — **HIGH**
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:521:| Layer 1 | ADR-011 §2.1 영구 권위 | ✅ |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:543:**system-identity-prequel §3 (권위 위계)** → ADR-011 §2.3 영구 승격 완료 (2026-05-06). **archive 후에도 ADR-011 권위 영구 보존**.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:557:ADR-008 부록 B Amendment (2026-05-06 발행, ADR-011 동시 발행) — Hermes 도입 결정 본문 + R-1 FAIL 후 갱신 사항 cross-reference. **본 합의 후 ADR-008 본문 자동 갱신 *금지* 답습** (C-14 1 §7.4 + Gemini §7.4 cross-vendor 일치 — 별도 PR).
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:564:**ADR-011 §2.1 (a)~(d) + ADR-012 §4 답습 — Amendment 절차 영구 보존**:
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:568:| 일반 원칙 (수단/목적 분리) | ADR-011 §2.1 본문 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:569:| Amendment specific 갱신 | ADR-008 부록 B (R1 specific) + ADR-009 C-N (P1 facade MVP specific) + ADR-011 §8 후속 작업 등록 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:570:| 자동 갱신 금지 | ADR-011 §2.4 T3 + 본 합의 §0.2 #3 답습 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:612:| **Gap-6** | §5.2 / §5.3 에 Hermes 변조 차단 매트릭스 4항목 (ADR-012 §2.12) + PASS 성립 4 요건 (G3 §5) cross-reference 부재 | P2 v3 §5 | **HIGH** | C-5 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:651:| **C-5** | §5.2 / §5.3 에 ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목 + G3 §5 PASS 성립 4 요건 cross-reference 흡수 | Gap-6 | (간접 — Gemini §7.10 #2 Mandatory Reference 답습) | **HIGH** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:656:| **C-11** | §10 영구 핵심 제약 표 → (i) Normative Constraints 명시 격상 + (ii) Provider Liquidity 5-way 답습 + (iii) archive 후 보존 강화 문구 ("Archiving P2 v2 or system-identity-prequel does not weaken, supersede, or delete the five permanent constraints. If any archived document contains stronger wording, the stronger constraint remains preserved through ADR-011 / ADR-012 and this section.") + (iv) ADR-012 §9 5/5 HIGH 보호 매트릭스 cross-reference | Gap-12 | **일치** (C-14 1 §7.7 + Gemini §7.7 cross-vendor 일치 ENHANCEMENT REQUIRED) | **HIGH** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:689:### 5.2 Hermes ≠ root of trust (ADR-011 §2.3 영구 권위)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:691:**영구 권위 layer 5/5** (ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 C-N §2.3 + G3 §1.3/§5 + G3 §2.5 #11 / §4.5 / §2.2 #20 모두 정식 발행):
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:693:- Layer 1: ADR-011 §2.3 영구 권위 (system-identity-prequel §3 ADR 승격 답습)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:699:**P2 v3 본문 답습**: §2.1.2 + §2.3 + §2.5 + §5.2 + §5.3 + §10 cross-reference 흡수 권고 (C-1, C-2, C-5, C-12).
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:701:**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-011 + ADR-012 + ADR-009 C-N + G3 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:705:### 5.3 메타포 강제 금지 (system-identity-prequel §7)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:720:### 5.4 자동 정책 변경 금지 (T3, ADR-011 §2.4)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:722:**영구 권위 layer 5/5** (ADR-011 §2.4 + ADR-012 §2.7 + G2 GP-6 + G3 §2.2 #11/#20 + P2 v3 §0.2 #6 / §11 / §12 모두 정식 발행):
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:724:- Layer 1: ADR-011 §2.4 영구 권위 (T1/T2/T3 분류)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:732:**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-011 + ADR-012 + G2 + G3 + P2 v3 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:738:### 5.5 수단/목적 분리 (ADR-011 §2.1 (a)~(d) + (e) 5조건)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:740:**영구 권위 layer 5/5** (ADR-011 §2.1 + ADR-012 §4 + P2 v3 §3.3 / §4.3 / §5.4 / §6.4 + R-2 ~ R-7 + R-6 workflow 모두 정식 발행):
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:742:- Layer 1: ADR-011 §2.1 영구 권위 ((a)~(d) 4조건)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:750:**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-011 + ADR-012 + P2 v3 + Phase 0 evidence 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:773:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신 권유 (cross-reference 권고 한정)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:797:2. **Hermes ≠ root of trust 원칙 영구 권위 = 5/5 정식 발행** — ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 C-N §2.3 + G3 §1.3/§5 + G3 §2.5/§4.5/§2.2
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:799:4. **자동 정책 변경 금지 (T3) = HIGH 5/5** — ADR-011 §2.4 + ADR-012 §2.7 + G2 GP-6 + G3 §2.2 + P2 v3 §0.2 #6 / §11 / §12
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:800:5. **수단/목적 분리 = HIGH** — ADR-011 §2.1 + ADR-012 §4 + P2 v3 §3.3/§4.3/§5.4/§6.4 (a)~(e) 패턴 + R-2 ~ R-7 + R-6
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md:835:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-summary.json:28:    "file_size_GiB": 45.38,
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-summary.json:44:      "Q4_0 (42.93 GiB)", "Q4_K_L (45.60 GiB)", "Q4_K_M (45.38 GiB, 본 cycle 선택)", "Q4_K_S (43.71 GiB)"
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-summary.json:174:    "interpretation": "brief v1.1 예상 (~48GB / 84.6%) 정합 (~45.38 GiB / 84%)"
docs/phase0/v1-poc-raw/phase3-5/2026-05-25T05-46-phase3-5-summary.json:259:    "hf_egress_total_GiB": "~45.38 (Q4_K_M file) + ~수KB (API + HEAD)",
docs/review/3plus1-consensus-2026-05-21-bi-3-credential-means-decision.md:10:**1차 권위 답습**: `cc5b517` BI-3 brief 검증 합의 (BI3-1~8 + CBI3-1~4) + `f29c772` Group I 구현 entry 합의 (§2.4 수단 권고 — 본 합의가 *정제*) + GP-3 §5 + γ-1 `9b1f8cd`(ST-1)·γ-2 `2e9d46b`(ST-4 DEFER) + ADR-011 §2.1 means/ends (a)~(d) + roadmap §3.6(단계적)·§5.4(환경 분기)
docs/review/3plus1-consensus-2026-05-21-bi-3-credential-means-decision.md:17:세 Agent 는 **(1) M1(미주입)은 단독 부적격** — 행위 규칙(soft)이며 single-host 에서 키가 host 어딘가 잔존하는 gap 이 구조적으로 남으므로 *대체 수단이 아니라 모든 물리 격리 수단의 공통 전제 위생*(env scrub·socket 미마운트·cap_drop), **(2) 물리 격리(키가 칩/토큰 밖 미이탈)가 1순위**로 single-host 의 "동일 host 키 공유 gap"을 구조적으로 소멸시키며 **Hermes upstream 변경 0건**으로 달성(컨테이너가 서명 능력을 아예 미보유), **(3) M3(vault)는 single-host unseal 자격 재귀로 부적격·M4(ST-4)/M5(keyless) MVP-6 DEFER**, **(4) docker socket 미마운트 + CAP_SYS_PTRACE drop 은 *어느 수단을 택해도* 비협상 동반**(host escape·메모리 scrape 는 키 격리와 직교·최치명), **(5) BI-3 충족은 *수단 라벨* 이 아니라 *계산적/적대적 침투 시연 실패*(binary)로만 입증** 된다는 데 일치한다. 가장 무게 있는 교차 발견은 **Agent B(보안)와 Agent C(대안)가 서로 다른 입구로 "TPM/host-bound 물리 격리 1순위"에 독립 수렴** 한 점이다 — B 는 "TPM 이 M2 의 백업 키 역설(N개 등록 = CT-1 공격 표면 N배)을 *분실 SPOF 부재* 로 구조적 회피", C 는 "비용 0·운영 단순·lock-out 안전·**Provider Liquidity 우위**(토큰 벤더 lock-in > OS 종속) 5/6 축 우위" — 이는 직전 `f29c772` §2.4 의 "M2 hardware key 1순위 동급 병치" 권고를 **정제**한다. Agent A(구현)는 "플랫폼 의존 동급 병치"(macOS=Secure Enclave / Linux=YubiKey-SSH 연동 단순성 ≥ TPM PKCS#11 브리지)를 들어 약간 다른 결을 보였으나, **세 관점을 통합하면 진정한 합의 = "host-bound 물리 격리 default(플랫폼별: macOS Secure Enclave / Linux TPM·YubiKey) + M2 외장 토큰 = touch-to-sign 자동 서명 차단이 위협 모델상 필수일 때 보강"의 *비대칭 순위화 + 환경/플랫폼 분기*** 이다("동급 병치"는 두 수단의 우위 축이 *직교*[TPM=가용성/비용/PL, M2=물리 터치]함을 흐린다). 또한 C 단독으로 **결정 *구조* 대안**(단일 수단 고정 → 환경 분기[local 물리격리 / Docker M1+secret / CI ephemeral+fingerprint, roadmap §5.4 선례] + 추상 인터페이스[ADR-011 (a) 교체 경로] + 단계적 채택[roadmap §3.6 선례])을 제시 — means 편향 해소의 핵심. 본 합의 = **추론적 검증(권고) 한정 — 수단 결정·실 구현·commit·push 는 사용자 명시 + 별도 entry 발효 단계.**
docs/review/3plus1-consensus-2026-05-21-bi-3-credential-means-decision.md:61:| N-C1 ⭐ | **결정 구조 대안** (환경 분기[local/Docker/CI] + 추상 인터페이스[ADR-011 (a)] + 단계적 채택, roadmap §3.6/§5.4 선례) | C | **높음** | **CD-8** |
docs/review/3plus1-consensus-2026-05-21-bi-3-credential-means-decision.md:111:| **CD-8** ⭐ | **결정 *구조* = 단일 수단 고정 아님** — (a) 환경 분기(local 물리격리 / Docker M1+secret / CI ephemeral+fingerprint, roadmap §5.4 선례) + (b) 추상 인터페이스(`Signer`/`CredentialSource`, ADR-011 §2.1(a) 교체 경로 코드 박제) + (c) 단계적 채택(MVP-1=TPM → 1.5차 M2 보강, roadmap §3.6 선례). means 편향 해소 | C-DEC-4 단독 | 2 |
docs/review/3plus1-consensus-2026-05-21-bi-3-credential-means-decision.md:156:**BI-3 credential 격리 수단 *결정 권고* = APPROVE WITH CONDITIONS, 권고 결정 = host-bound 물리 격리(TPM/Secure Enclave) 1순위 + M2(외장 토큰) = touch-to-sign 자동 서명 차단 필수 시 보강 + M1 공통 전제 위생 + 환경 분기 결정 구조**이다. 세 Agent 는 (1) M1 단독 부적격(공통 위생이지 대체 수단 아님), (2) 물리 격리 1순위(Hermes upstream 변경 0건), (3) M3 single-host 부적격·M4/M5 MVP-6 DEFER, (4) **docker socket 미마운트 + CAP_SYS_PTRACE drop = 수단 무관 비협상**, (5) BI-3 충족 = 수단 라벨 ≠ 입증·계산적/적대적 시연(binary)으로만 에 일치했다. 가장 무게 있는 발견은 **Agent B(백업 키 역설 회피)와 Agent C(비용·운영·lock-out·Provider Liquidity 5/6 축)가 독립 수렴한 "TPM/host-bound 1순위"** 로, 직전 `f29c772` "M2 1순위 동급 병치"를 **정제** 한다(Agent A 의 "플랫폼 의존 동급 병치"[Linux YubiKey-SSH 연동 단순성]는 *우위 축 직교*[TPM=가용성/비용/PL, M2=물리 터치]로 통합 — '동급 병치' 폐기, 'host-bound default + 플랫폼/환경 분기'로 수렴). Agent C 단독으로 **결정 *구조* 대안**(환경 분기[local/Docker/CI, roadmap §5.4 선례] + 추상 인터페이스[ADR-011 (a) 교체 경로] + 단계적 채택[roadmap §3.6 선례])을 제시해 means 편향을 해소했다. 구현 발효 전 **BLOCKING 10**(CD-1 순위 정제 / CD-2 조합·공통위생 / CD-3 docker socket·ptrace 비협상 / CD-4 서명키≠ST-1 / CD-5 침투 시연 binary 종료 / CD-6 touch policy+PIN+사회공학 잔여 / CD-7 백업키 TPM 우선·offline cold / CD-8 결정 구조 / CD-9 공급망·그라데이션 수단무관 / CD-10 guardrail 동반) + 조건부 3(M5 audit축 보존 / M3 강등 / grace-period rollback)이며, 거짓 안전감 차단(수단 결정 ≠ 안전 확정·침투 시연+guardrail 한 묶음)을 Reviewer 격상했다. 교차 = 일치 10 / 부분 3 / 불일치 1(우위 축 직교) / 누락 10. 본 합의는 추론적 검증(권고) 한정 — 수단 *결정 고정*·hardware/TPM 채택·백업 키 정책 고정·실 구성·다른 BLOCKING 해소·commit·push 는 사용자 명시 + 별도 entry 발효 단계이며, **본 보고서 외 어떤 파일도 편집/생성하지 않고 commit/push 0건**이다.
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:12:> **상위 권위**: ADR-008 부록 C (Design/Governance ↔ Implementation/Runtime 분리), ADR-011 §2.1 (a)~(e) + §2.3 운영 함의 #2, ADR-010 (Vault HSM, cross-reference), ADR-012 (Evidence Ledger), governance-preconditions.md §4 (GP-2) + §5 (GP-3), redaction-pattern-equivalence.md (R-4), r4-1-trigger-extension-evidence.md §4.1 (R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns), implementation-runtime-roadmap.md §3.1 (Order 4 + 5)
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:56:  skip_direct_register=['T1-038', 'T1-040']  (R-4.1 §4.2 답습)
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:93:### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:99:| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 §A.2 + 부록 C / ADR-011 §2.1 + §2.3 / ADR-010 / ADR-012 / GP §4 + §5 / R-4 + R-4.1 / roadmap §3.1 cross-reference |
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:127:| 7 | git pre-commit hook 실 활성화 | 0 | T2 정책 영역 (ADR-011 §2.4) — 분리 |
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:146:| 7 | ADR-010 / ADR-011 / ADR-012 와 충돌 | 0 | cross-reference 답습 한정 |
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:173:| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group F |
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:256:**APPROVE WITH CONDITIONS** — Group D PoC = G2 GP-2 / GP-3 *형식적 검출 layer 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/7 발화, 12 금지 0/12 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 7/7 충족, 로컬 6/6 검증 PASS, CI workflow 12 step 형식 검증 PASS, R-4.1 직접 답습 (리팩토링 0 / 복제 0 / 외부 의존 0)).
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:268:| C-D-7 | Step 9 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §12 변경 이력 답습) | 본 합의 §5.3 #4 |
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:270:### 5.3 다음 단계 권고
docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md:291:| 2026-05-10 | 신규 작성 | Group D 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 7 0/7 발화, 12 금지 0/12 위반, PASS 기준 7/7 + ADR-011 §2.1 5/5 충족, 로컬 6/6 PASS, CI workflow 12 step 형식 검증 PASS, R-4.1 직접 답습 (리팩토링 0 / 복제 0 / 외부 의존 0). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group B/C/F 답습). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:166:| §10-β — §10 본문 5 제약 *Normative Constraints* 형식 변환 (응답 1 §7.7 옵션 1 답습) | (1) 권위 강화 | (1) 본문 형식 *변경* 분량 +20 줄 / (2) ADR-011 / ADR-012 cross-ref 만으로도 *충분* (응답 1 §7.7 옵션 2 답습) | **차순위 권고** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:167:| §10-γ — §10 본문 단축 + ADR-011 / ADR-012 / Constitution cross-ref 단독 | (1) 분량 ↓ | (1) §10 본문 *영구 권위* 약화 위험 | 부적절 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:177:> 문서에 더 강한 표현이 있다면, 더 강한 제약이 ADR-011 + ADR-012 + 본 §10 을 통해
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:335:- 정당 사유: 1인 개발자 비용 ↓ + git diff *읽기 쉬움* + ADR-011 / ADR-012 cross-ref 만으로 영구 보존 권위 *충분*
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:372:| 2 | **Hermes ≠ root of trust** (ADR-011 §2.3) | §2.2 권위 위계 + §2.3 운영 함의 5항목 + §2.4 비활성 상태 책임 한정 + §10 영구 권위 | **강 (권위 위계 본문 명시)** | ✅ **충분 + 강화** |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:374:| 4 | 자동 정책 변경 금지 T3 (ADR-011 §2.4) | §2.1.2 Hermes 가 *하지 않는* 것 6항목 + §10 영구 권위 + §11 변경 절차 (T3 = 풀 3+1 + ADR Amendment) | 강 | ✅ 충분 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:375:| 5 | 수단/목적 분리 (ADR-011 §2.1) | §3.3 G1b / §4.3 G2 / §5.4 G3 / §6.4 G4 Exit 기준 (a)~(e) 5조건 답습 + §10 영구 권위 | 강 (5조건 패턴 4 게이트 모두 답습) | ✅ 충분 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:389:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 (cross-ref 만 권고)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md:477:- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md:19:- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T3 영역
docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md:314:| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md:368:| C-γ-19 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §7 답습 |
docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md:410:| ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 | 0건 (cross-reference 답습 한정) |
docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md:18:- ADR-011 §2.1 (a)~(e) + §2.4 T2 영역
docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md:43:| 본 합의 결정 | **외부 LLM 1+ 비적용** — W-1~W-4 최소 영역 분리 명시로 T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 (Group α C-11 답습 + ADR-011 §2.4 답습 한정) |
docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md:156:- F-금지 #1 영구 답습 (GitHub Actions secrets 사용 0건 + 실 API key 0건) — LVE §5.3 답습 강화
docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md:338:| C-υ-21 | SUCCESS 조건 7 (S-1 ~ S-7) | §5.3 답습 |
docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md:353:| C-υ-36 | F-금지 #1 영구 답습 | LVE §5.3 답습 강화 |
docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md:356:### 5.3 본 합의 신규 발화 12 조건 (C-υ-38 ~ C-υ-49)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:7:**상위 권위**: ADR-011 §2.1 (수단/목적 분리, (a)~(d) 4조건 + (e) 합의 APPROVE = 5조건 패턴), ADR-011 §2.3 권위 위계 (영구), ADR-011 §2.4 T1/T2/T3, ADR-012 §원칙 1~12 (Evidence Ledger 보호), system-identity-prequel §3 / §6.3 / §7
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:28:6. **§10 (영구 핵심 제약 5건) 보존 문구 강화 의무 발생** — C-14 응답 1 §7.7 + 응답 2 §7.7 모두 "P2 v2 / system-identity-prequel archive 시 약화 방지" 명시 권고. 본 v3 §10 5 row (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) 는 이미 권위 근거 ADR cross-reference 명시. *추가 명시 권고* = "Archiving P2 v2 or system-identity-prequel does not weaken the five permanent constraints; the stronger wording remains preserved through ADR-011 / ADR-012 / Constitution"  migration note 1 단락 추가 (응답 1 §7.7 직접 인용). 운영 가능성 0.25일.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:65:**현 정합성**: ✅ **HIGH** — R-2 ~ R-7 6단계 + R-6 actual run + G1b PASS evidence 흡수 정확. §1.1 (P2 v2 §2.1.3 가정 폐기) / §1.2 (G1 → G1a/G1b 분리) / §1.3 (차단조건 #1 충족 메커니즘 갱신) / §1.4 (R-2 ~ R-7 흡수표) / §1.5 (carry-over) 모두 권위 ADR (ADR-011 §2.2) 답습.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:73:**현 정합성**: ✅ **HIGH** — DRAFT 시점 §2 첫 문단 = "본 §2는 Hermes PMO *격상 선언이 아니다*" 명시 답습. §2.1.1 (격상 후 담당 후보 10항목) + §2.1.2 (Hermes 가 *하지 않는* 것 6항목, 영구) + §2.2 (권위 위계 ADR-011 §2.3 인용) + §2.3 (운영 함의 5항목 ADR-011 §2.3 인용) + §2.4 (현 시점 비활성 책임) + §2.5 (활성화 후 책임) + §2.6 (격상 절차 7 단계) 모두 정합.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:80:**잠재 risk**: §2.1.1 (격상 후 담당 10항목) 의 권위 등급 (T1 7건 / T2 2건 / T3 후보 식별 시 escalation) 은 ADR-011 §2.4 답습이나 *현 시점* 미활성. 본 합의로 *명시* 가 활성화 신호로 오인될 위험 = 응답 1 §7.3 권고 답습으로 차단 (negative activation clause).
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:166:**현 정합성**: ❌ **DRAFT 시점 6 row (ADR-008 / ADR-009 / ADR-010 / ADR-011) vs 현 시점 ADR-012 신규 발행 + ADR-009 C-N 갱신 미반영**.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:179:| ADR-011 | (DRAFT 시점) ... | (DRAFT 시점) ... |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:180:| ADR-011 | (DRAFT 시점) ... | (DRAFT 시점) ... |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:227:> - ADR-011 §2.1 / §2.3 / §2.4 (Means-vs-Ends, Hermes ≠ root of trust, T1/T2/T3)
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:265:**현 정합성**: ✅ **HIGH** — DRAFT 시점 5 통제 수단 (사용자 명시 절차 답습 / R-7 SOP §0 답습 / ADR-011 §2.4 답습 / 수단/목적 분리 답습 / 본 초안이 *하지 않는* 것 명시) 모두 권위 답습.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:304:2. **§7 ADR 매트릭스** — DRAFT 시점 6 row (ADR-008 ~ ADR-011) / 현 시점 = ADR-009 C-N 갱신 + ADR-012 신규 발행 미반영 → §1.8 row 추가 의무.
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:406:#### 2.5.3 1인 개발자 메타-템플릿 스케일에서 P2 v3 정식 채택 후 변경 빈도 추정
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:409:- ADR 발행/갱신: ADR-011 (5/6) / ADR-009 갱신 (5/9) / ADR-012 (5/9) = 3건 / 5일
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:514:| **Hermes ≠ root of trust** (ADR-011 §2.3) | ADR-011 §2.3 영구 권위 + G3 §1 ~ §7 운영 구현 + ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목 | 본 v3 §10 1 row 보존 + §2.2 권위 위계 인용 + §2.3 운영 함의 5항목 + §5 G3 운영 구현 cross-reference | ✅ PASS — 본 v3 §2 / §5 모두 답습 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:516:| **자동 정책 변경 금지 (T3)** (ADR-011 §2.4) | ADR-011 §2.4 + 본 v3 §0.2 #6 + §11 (T3 변경 절차) + ADR-012 §원칙 9 (Hash chain 검증 실패 = 즉시 BLOCK, 자동 복구 / 자동 revert 금지) | 본 v3 §10 1 row 보존 + §11 표 + §2.6 격상 절차 7 단계 (사용자 명시 격상 결정 = T2) + §2.6.1 PMO 격상 체크리스트 | ✅ PASS — T1/T2/T3 분리 답습 |
docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md:517:| **수단/목적 분리 원칙** (ADR-011 §2.1 (a)~(d) 4조건) | ADR-011 §2.1 + 본 v3 §3.3 / §4.3 / §5.4 / §6.4 의 exit 기준 패턴 + ADR-012 §4 (a)~(e) 5조건 답습 | 본 v3 §10 1 row 보존 + §3.3 / §4.3 / §5.4 / §6.4 (a)~(e) 5조건 패턴 답습 | ✅ PASS — (a)~(e) 5조건 답습 |
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:12:> **상위 권위**: ADR-008 부록 C, ADR-011 §2.1 (a)~(e), ADR-012 §2.8 (Full Rewrite 5 Layer) + §2.12 (Hermes 변조 차단), G4 §4.4.5, Group C `parse_jsonl` import 직접, Group C 후속 cross-reference
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:108:### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:114:| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 부록 C / ADR-011 §2.1 / ADR-012 §2.8 + §2.12 / G4 §4.4.5 / Group C `parse_jsonl` cross-reference / Group C 후속 anchor verifier cross-reference |
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:200:| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A~G/A3/CF 답습 |
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:281:**APPROVE WITH CONDITIONS** — Group C 후속 후속 PoC = G4 *Layer 2/3/4 정적 검출 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/5 발화, 9 금지 0/9 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 10/10 충족, 로컬 10/10 검증 PASS, CI workflow 15 step 형식 검증 PASS, ADR-012 §2.8 + G4 §4.4.5 직접 답습 (변경 0건 / 외부 의존 0건 / 실 git command 호출 0건). **본 PoC 종료 후 = ADR-012 §2.8 5 Layer 답습 5/5 완결**).
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:293:| C-CFF-7 | Step 8 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 | 본 합의 §5.3 #4 |
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:295:### 5.3 다음 단계 권고
docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md:314:| 2026-05-10 | 신규 작성 | Group C 후속 후속 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 5 0/5 발화, 9 금지 0/9 위반, PASS 기준 10/10 + ADR-011 §2.1 5/5 충족, 로컬 10/10 PASS, CI workflow 15 step 형식 검증 PASS, ADR-012 §2.8 + §2.12 + G4 §4.4.5 직접 답습 (변경 0건 / 외부 의존 0건 / 실 git command 호출 0건). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group D/E/G/A3/CF 답습). **본 PoC 종료 후 = ADR-012 §2.8 5 Layer 답습 5/5 완결** (Layer 1 Group C + Layer 2/3/4 본 PoC + Layer 5 Group C 후속). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51:  1900K .......... .......... .......... .......... ..........  0% 35.3M 7m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:74:  3050K .......... .......... .......... .......... ..........  0% 45.3M 6m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:256: 12150K .......... .......... .......... .......... ..........  0% 45.3M 5m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359: 17300K .......... .......... .......... .......... ..........  0% 45.3M 5m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:491: 23900K .......... .......... .......... .......... ..........  0% 25.3M 5m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:504: 24550K .......... .......... .......... .......... ..........  0% 45.3M 5m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:861: 42400K .......... .......... .......... .......... ..........  0% 55.3M 5m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:980: 48350K .......... .......... .......... .......... ..........  0% 45.3M 5m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1055: 52100K .......... .......... .......... .......... ..........  0% 35.3M 5m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1129: 55800K .......... .......... .......... .......... ..........  0% 35.3M 5m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1269: 62800K .......... .......... .......... .......... ..........  0% 75.3M 5m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1338: 66250K .......... .......... .......... .......... ..........  0% 25.3M 5m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1442: 71450K .......... .......... .......... .......... ..........  0% 45.3M 5m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1521: 75400K .......... .......... .......... .......... ..........  0% 45.3M 5m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1636: 81150K .......... .......... .......... .......... ..........  0% 45.3M 5m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1664: 82550K .......... .......... .......... .......... ..........  0% 35.3M 5m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:1671: 82900K .......... .......... .......... .......... ..........  0% 45.3M 5m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2338:116250K .......... .......... .......... .......... ..........  0% 45.3M 5m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2551:126900K .......... .......... .......... .......... ..........  0% 45.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2588:128750K .......... .......... .......... .......... ..........  0% 65.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2780:138350K .......... .......... .......... .......... ..........  0% 65.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2863:142500K .......... .......... .......... .......... ..........  0% 35.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2878:143250K .......... .......... .......... .......... ..........  0% 65.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2899:144300K .......... .......... .......... .......... ..........  0% 75.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2929:145800K .......... .......... .......... .......... ..........  0% 15.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2934:146050K .......... .......... .......... .......... ..........  0% 45.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:2974:148050K .......... .......... .......... .......... ..........  0% 55.3M 5m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3311:164900K .......... .......... .......... .......... ..........  0% 55.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3344:166550K .......... .......... .......... .......... ..........  0% 35.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3448:171750K .......... .......... .......... .......... ..........  0% 35.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3532:175950K .......... .......... .......... .......... ..........  0% 25.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3789:188800K .......... .......... .......... .......... ..........  1% 45.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3797:189200K .......... .......... .......... .......... ..........  1% 45.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3833:191000K .......... .......... .......... .......... ..........  1% 35.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:3904:194550K .......... .......... .......... .......... ..........  1% 55.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4068:202750K .......... .......... .......... .......... ..........  1% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4363:217500K .......... .......... .......... .......... ..........  1% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4402:219450K .......... .......... .......... .......... ..........  1% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4578:228250K .......... .......... .......... .......... ..........  1% 65.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4753:237000K .......... .......... .......... .......... ..........  1% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4844:241550K .......... .......... .......... .......... ..........  1% 25.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:4973:248000K .......... .......... .......... .......... ..........  1% 35.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:5183:258500K .......... .......... .......... .......... ..........  1% 45.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:5540:276350K .......... .......... .......... .......... ..........  1% 75.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:5688:283750K .......... .......... .......... .......... ..........  1% 65.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:6011:299900K .......... .......... .......... .......... ..........  1% 45.3M 5m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:6047:301700K .......... .......... .......... .......... ..........  1% 35.3M 5m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:6097:304200K .......... .......... .......... .......... ..........  1% 45.3M 5m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:6568:327750K .......... .......... .......... .......... ..........  1% 95.3M 5m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:6992:348950K .......... .......... .......... .......... ..........  1% 45.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:6994:349050K .......... .......... .......... .......... ..........  1% 45.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7049:351800K .......... .......... .......... .......... ..........  1% 45.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7267:362700K .......... .......... .......... .......... ..........  1% 75.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7635:381100K .......... .......... .......... .......... ..........  2% 55.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7724:385550K .......... .......... .......... .......... ..........  2% 45.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7746:386650K .......... .......... .......... .......... ..........  2% 45.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7759:387300K .......... .......... .......... .......... ..........  2% 45.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7803:389500K .......... .......... .......... .......... ..........  2% 75.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7809:389800K .......... .......... .......... .......... ..........  2% 45.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:7902:394450K .......... .......... .......... .......... ..........  2% 25.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:8214:410050K .......... .......... .......... .......... ..........  2% 25.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:8336:416150K .......... .......... .......... .......... ..........  2% 35.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:8347:416700K .......... .......... .......... .......... ..........  2% 55.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:8473:423000K .......... .......... .......... .......... ..........  2% 35.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:8890:443850K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9095:454100K .......... .......... .......... .......... ..........  2% 55.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9151:456900K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9415:470100K .......... .......... .......... .......... ..........  2% 55.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9462:472450K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9632:480950K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9633:481000K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9697:484200K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9755:487100K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9797:489200K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9804:489550K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9843:491500K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9867:492700K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9899:494300K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:9904:494550K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10335:516100K .......... .......... .......... .......... ..........  2% 75.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10438:521250K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10517:525200K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10732:535950K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10795:539100K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10852:541950K .......... .......... .......... .......... ..........  2% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:10898:544250K .......... .......... .......... .......... ..........  2% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11055:552100K .......... .......... .......... .......... ..........  3% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11398:569250K .......... .......... .......... .......... ..........  3% 45.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11441:571400K .......... .......... .......... .......... ..........  3% 65.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11459:572300K .......... .......... .......... .......... ..........  3% 65.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11531:575900K .......... .......... .......... .......... ..........  3% 35.3M 5m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11832:590950K .......... .......... .......... .......... ..........  3% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:11895:594100K .......... .......... .......... .......... ..........  3% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12039:601300K .......... .......... .......... .......... ..........  3% 45.3M 5m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12359:617300K .......... .......... .......... .......... ..........  3% 45.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12497:624200K .......... .......... .......... .......... ..........  3% 45.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12674:633050K .......... .......... .......... .......... ..........  3% 55.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12737:636200K .......... .......... .......... .......... ..........  3% 35.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12758:637250K .......... .......... .......... .......... ..........  3% 55.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12838:641250K .......... .......... .......... .......... ..........  3% 45.3M 5m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:12954:647050K .......... .......... .......... .......... ..........  3% 45.3M 5m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:13397:669200K .......... .......... .......... .......... ..........  3% 55.3M 5m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:13552:676950K .......... .......... .......... .......... ..........  3% 35.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:13670:682850K .......... .......... .......... .......... ..........  3% 35.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:13719:685300K .......... .......... .......... .......... ..........  3% 65.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14106:704650K .......... .......... .......... .......... ..........  3% 55.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14128:705750K .......... .......... .......... .......... ..........  3% 35.3M 5m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14339:716300K .......... .......... .......... .......... ..........  3% 35.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14597:729200K .......... .......... .......... .......... ..........  4% 45.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14704:734550K .......... .......... .......... .......... ..........  4% 75.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14726:735650K .......... .......... .......... .......... ..........  4% 45.3M 5m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:14987:748700K .......... .......... .......... .......... ..........  4% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15053:752000K .......... .......... .......... .......... ..........  4% 65.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15198:759250K .......... .......... .......... .......... ..........  4% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15253:762000K .......... .......... .......... .......... ..........  4% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15316:765150K .......... .......... .......... .......... ..........  4% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15328:765750K .......... .......... .......... .......... ..........  4% 45.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15419:770300K .......... .......... .......... .......... ..........  4% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15563:777500K .......... .......... .......... .......... ..........  4% 25.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15585:778600K .......... .......... .......... .......... ..........  4% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15684:783550K .......... .......... .......... .......... ..........  4% 35.3M 5m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15732:785950K .......... .......... .......... .......... ..........  4% 35.3M 5m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:15951:796900K .......... .......... .......... .......... ..........  4% 45.3M 5m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:16399:819300K .......... .......... .......... .......... ..........  4% 35.3M 5m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:16473:823000K .......... .......... .......... .......... ..........  4% 35.3M 5m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:16560:827350K .......... .......... .......... .......... ..........  4% 65.3M 5m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:16756:837150K .......... .......... .......... .......... ..........  4% 35.3M 5m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17032:850950K .......... .......... .......... .......... ..........  4% 35.3M 5m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17117:855200K .......... .......... .......... .......... ..........  4% 35.3M 5m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17268:862750K .......... .......... .......... .......... ..........  4% 35.3M 5m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17548:876750K .......... .......... .......... .......... ..........  4% 85.3M 5m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17611:879900K .......... .......... .......... .......... ..........  4% 45.3M 5m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17764:887550K .......... .......... .......... .......... ..........  4% 25.3M 5m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:17967:897700K .......... .......... .......... .......... ..........  4% 45.3M 5m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18022:900450K .......... .......... .......... .......... ..........  4% 55.3M 5m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18250:911850K .......... .......... .......... .......... ..........  5% 65.3M 5m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18298:914250K .......... .......... .......... .......... ..........  5% 35.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18408:919750K .......... .......... .......... .......... ..........  5% 75.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18473:923000K .......... .......... .......... .......... ..........  5% 45.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18579:928300K .......... .......... .......... .......... ..........  5% 35.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18732:935950K .......... .......... .......... .......... ..........  5% 45.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18870:942850K .......... .......... .......... .......... ..........  5% 25.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:18915:945100K .......... .......... .......... .......... ..........  5% 45.3M 5m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19064:952550K .......... .......... .......... .......... ..........  5% 35.3M 5m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19176:958150K .......... .......... .......... .......... ..........  5% 45.3M 5m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19312:964950K .......... .......... .......... .......... ..........  5% 45.3M 5m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19415:970100K .......... .......... .......... .......... ..........  5% 75.3M 5m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19482:973450K .......... .......... .......... .......... ..........  5% 45.3M 5m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19763:987500K .......... .......... .......... .......... ..........  5% 45.3M 5m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:19984:998550K .......... .......... .......... .......... ..........  5% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20206:1009650K .......... .......... .......... .......... ..........  5% 45.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20244:1011550K .......... .......... .......... .......... ..........  5% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20553:1027000K .......... .......... .......... .......... ..........  5% 45.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20652:1031950K .......... .......... .......... .......... ..........  5% 45.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20712:1034950K .......... .......... .......... .......... ..........  5% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20791:1038900K .......... .......... .......... .......... ..........  5% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20803:1039500K .......... .......... .......... .......... ..........  5% 35.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:20986:1048650K .......... .......... .......... .......... ..........  5% 55.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21072:1052950K .......... .......... .......... .......... ..........  5% 85.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21164:1057550K .......... .......... .......... .......... ..........  5% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21193:1059000K .......... .......... .......... .......... ..........  5% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21286:1063650K .......... .......... .......... .......... ..........  5% 35.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21563:1077500K .......... .......... .......... .......... ..........  5% 45.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21857:1092200K .......... .......... .......... .......... ..........  6% 75.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:21917:1095200K .......... .......... .......... .......... ..........  6% 45.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22030:1100850K .......... .......... .......... .......... ..........  6% 45.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22066:1102650K .......... .......... .......... .......... ..........  6% 35.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22153:1107000K .......... .......... .......... .......... ..........  6% 45.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22268:1112750K .......... .......... .......... .......... ..........  6% 45.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22882:1143450K .......... .......... .......... .......... ..........  6% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22916:1145150K .......... .......... .......... .......... ..........  6% 65.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22960:1147350K .......... .......... .......... .......... ..........  6% 15.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:22976:1148150K .......... .......... .......... .......... ..........  6% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23008:1149750K .......... .......... .......... .......... ..........  6% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23011:1149900K .......... .......... .......... .......... ..........  6% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23089:1153800K .......... .......... .......... .......... ..........  6% 55.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23133:1156000K .......... .......... .......... .......... ..........  6% 45.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23144:1156550K .......... .......... .......... .......... ..........  6% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23203:1159500K .......... .......... .......... .......... ..........  6% 35.3M 5m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23390:1168850K .......... .......... .......... .......... ..........  6% 55.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23450:1171850K .......... .......... .......... .......... ..........  6% 35.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23477:1173200K .......... .......... .......... .......... ..........  6% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23661:1182400K .......... .......... .......... .......... ..........  6% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23665:1182600K .......... .......... .......... .......... ..........  6% 45.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:23929:1195800K .......... .......... .......... .......... ..........  6% 65.3M 5m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:24655:1232100K .......... .......... .......... .......... ..........  6% 55.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:24701:1234400K .......... .......... .......... .......... ..........  6% 45.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:24855:1242100K .......... .......... .......... .......... ..........  6% 35.3M 5m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25006:1249650K .......... .......... .......... .......... ..........  6% 45.3M 5m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25146:1256650K .......... .......... .......... .......... ..........  6% 25.3M 5m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25287:1263700K .......... .......... .......... .......... ..........  6% 35.3M 5m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25499:1274300K .......... .......... .......... .......... ..........  7% 65.3M 5m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25653:1282000K .......... .......... .......... .......... ..........  7% 75.3M 5m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25717:1285200K .......... .......... .......... .......... ..........  7% 55.3M 5m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:25962:1297450K .......... .......... .......... .......... ..........  7% 35.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26007:1299700K .......... .......... .......... .......... ..........  7% 45.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26152:1306950K .......... .......... .......... .......... ..........  7% 35.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26439:1321300K .......... .......... .......... .......... ..........  7% 45.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26458:1322250K .......... .......... .......... .......... ..........  7% 45.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26549:1326800K .......... .......... .......... .......... ..........  7% 45.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26599:1329300K .......... .......... .......... .......... ..........  7% 35.3M 5m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:26822:1340450K .......... .......... .......... .......... ..........  7% 75.3M 5m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:27363:1367500K .......... .......... .......... .......... ..........  7% 75.3M 5m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:27656:1382150K .......... .......... .......... .......... ..........  7% 55.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:27696:1384150K .......... .......... .......... .......... ..........  7% 45.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:27781:1388400K .......... .......... .......... .......... ..........  7% 35.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:27888:1393750K .......... .......... .......... .......... ..........  7% 25.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:27920:1395350K .......... .......... .......... .......... ..........  7% 35.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28167:1407700K .......... .......... .......... .......... ..........  7% 35.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28347:1416700K .......... .......... .......... .......... ..........  7% 45.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28360:1417350K .......... .......... .......... .......... ..........  7% 45.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28443:1421500K .......... .......... .......... .......... ..........  7% 35.3M 5m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28517:1425200K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28555:1427100K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28580:1428350K .......... .......... .......... .......... ..........  7% 25.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28590:1428850K .......... .......... .......... .......... ..........  7% 35.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28618:1430250K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28639:1431300K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28700:1434350K .......... .......... .......... .......... ..........  7% 35.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28721:1435400K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28881:1443400K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:28992:1448950K .......... .......... .......... .......... ..........  7% 45.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:29237:1461200K .......... .......... .......... .......... ..........  8% 25.3M 5m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:29563:1477500K .......... .......... .......... .......... ..........  8% 35.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:29691:1483900K .......... .......... .......... .......... ..........  8% 75.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:29815:1490100K .......... .......... .......... .......... ..........  8% 45.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:29817:1490200K .......... .......... .......... .......... ..........  8% 45.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:29878:1493250K .......... .......... .......... .......... ..........  8% 45.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30093:1504000K .......... .......... .......... .......... ..........  8% 35.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30122:1505450K .......... .......... .......... .......... ..........  8% 45.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30154:1507050K .......... .......... .......... .......... ..........  8% 35.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30241:1511400K .......... .......... .......... .......... ..........  8% 45.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30280:1513350K .......... .......... .......... .......... ..........  8% 45.3M 5m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30366:1517650K .......... .......... .......... .......... ..........  8% 85.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30437:1521200K .......... .......... .......... .......... ..........  8% 45.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30606:1529650K .......... .......... .......... .......... ..........  8% 45.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30797:1539200K .......... .......... .......... .......... ..........  8% 45.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30846:1541650K .......... .......... .......... .......... ..........  8% 45.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:30893:1544000K .......... .......... .......... .......... ..........  8% 45.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31080:1553350K .......... .......... .......... .......... ..........  8% 45.3M 5m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31313:1565000K .......... .......... .......... .......... ..........  8% 25.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31386:1568650K .......... .......... .......... .......... ..........  8% 65.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31412:1569950K .......... .......... .......... .......... ..........  8% 35.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31476:1573150K .......... .......... .......... .......... ..........  8% 65.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31587:1578700K .......... .......... .......... .......... ..........  8% 25.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31645:1581600K .......... .......... .......... .......... ..........  8% 45.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31694:1584050K .......... .......... .......... .......... ..........  8% 45.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31755:1587100K .......... .......... .......... .......... ..........  8% 35.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31885:1593600K .......... .......... .......... .......... ..........  8% 45.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31981:1598400K .......... .......... .......... .......... ..........  8% 25.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31989:1598800K .......... .......... .......... .......... ..........  8% 25.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:31995:1599100K .......... .......... .......... .......... ..........  8% 35.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:32255:1612100K .......... .......... .......... .......... ..........  8% 55.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:32367:1617700K .......... .......... .......... .......... ..........  8% 45.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:32873:1643000K .......... .......... .......... .......... ..........  9% 55.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:32886:1643650K .......... .......... .......... .......... ..........  9% 35.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:32898:1644250K .......... .......... .......... .......... ..........  9% 65.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:32910:1644850K .......... .......... .......... .......... ..........  9% 35.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:33071:1652900K .......... .......... .......... .......... ..........  9% 55.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:33328:1665750K .......... .......... .......... .......... ..........  9% 25.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:33450:1671850K .......... .......... .......... .......... ..........  9% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:33625:1680600K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:33656:1682150K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:33782:1688450K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:34207:1709700K .......... .......... .......... .......... ..........  9% 65.3M 5m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:34542:1726450K .......... .......... .......... .......... ..........  9% 25.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:34558:1727250K .......... .......... .......... .......... ..........  9% 15.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:34688:1733750K .......... .......... .......... .......... ..........  9% 45.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:34842:1741450K .......... .......... .......... .......... ..........  9% 35.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:34937:1746200K .......... .......... .......... .......... ..........  9% 45.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35100:1754350K .......... .......... .......... .......... ..........  9% 55.3M 4m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35296:1764150K .......... .......... .......... .......... ..........  9% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35413:1770000K .......... .......... .......... .......... ..........  9% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35450:1771850K .......... .......... .......... .......... ..........  9% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35476:1773150K .......... .......... .......... .......... ..........  9% 25.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35608:1779750K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35639:1781300K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35822:1790450K .......... .......... .......... .......... ..........  9% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35888:1793750K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:35964:1797550K .......... .......... .......... .......... ..........  9% 35.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36034:1801050K .......... .......... .......... .......... ..........  9% 55.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36371:1817900K .......... .......... .......... .......... ..........  9% 75.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36398:1819250K .......... .......... .......... .......... ..........  9% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36546:1826650K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36738:1836250K .......... .......... .......... .......... .......... 10% 55.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36812:1839950K .......... .......... .......... .......... .......... 10% 35.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:36889:1843800K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37072:1852950K .......... .......... .......... .......... .......... 10% 15.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37221:1860400K .......... .......... .......... .......... .......... 10% 35.3M 4m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37311:1864900K .......... .......... .......... .......... .......... 10% 45.3M 4m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37517:1875200K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37535:1876100K .......... .......... .......... .......... .......... 10% 35.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37697:1884200K .......... .......... .......... .......... .......... 10% 15.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:37913:1895000K .......... .......... .......... .......... .......... 10% 65.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38175:1908100K .......... .......... .......... .......... .......... 10% 35.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38242:1911450K .......... .......... .......... .......... .......... 10% 15.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38331:1915900K .......... .......... .......... .......... .......... 10% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38429:1920800K .......... .......... .......... .......... .......... 10% 55.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38451:1921900K .......... .......... .......... .......... .......... 10% 45.3M 4m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38890:1943850K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38907:1944700K .......... .......... .......... .......... .......... 10% 35.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38910:1944850K .......... .......... .......... .......... .......... 10% 35.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:38933:1946000K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39069:1952800K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39096:1954150K .......... .......... .......... .......... .......... 10% 65.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39143:1956500K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39176:1958150K .......... .......... .......... .......... .......... 10% 45.3M 4m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39663:1982500K .......... .......... .......... .......... .......... 10% 45.3M 4m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39906:1994650K .......... .......... .......... .......... .......... 10% 45.3M 4m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:39907:1994700K .......... .......... .......... .......... .......... 10% 35.3M 4m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:40061:2002400K .......... .......... .......... .......... .......... 11% 35.3M 4m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:40446:2021650K .......... .......... .......... .......... .......... 11% 35.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:40481:2023400K .......... .......... .......... .......... .......... 11% 45.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:40845:2041600K .......... .......... .......... .......... .......... 11% 35.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:40991:2048900K .......... .......... .......... .......... .......... 11% 25.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:41101:2054400K .......... .......... .......... .......... .......... 11% 35.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:41210:2059850K .......... .......... .......... .......... .......... 11% 55.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:41219:2060300K .......... .......... .......... .......... .......... 11% 45.3M 4m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:41246:2061650K .......... .......... .......... .......... .......... 11% 45.3M 4m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:41641:2081400K .......... .......... .......... .......... .......... 11% 45.3M 4m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:41754:2087050K .......... .......... .......... .......... .......... 11% 45.3M 4m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:42434:2121050K .......... .......... .......... .......... .......... 11% 35.3M 4m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:42459:2122300K .......... .......... .......... .......... .......... 11% 25.3M 4m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:42543:2126500K .......... .......... .......... .......... .......... 11% 65.3M 4m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:43298:2164250K .......... .......... .......... .......... .......... 11% 35.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:43369:2167800K .......... .......... .......... .......... .......... 11% 45.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:43401:2169400K .......... .......... .......... .......... .......... 11% 25.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:43584:2178550K .......... .......... .......... .......... .......... 11% 45.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:43698:2184250K .......... .......... .......... .......... .......... 12% 45.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44172:2207950K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44389:2218800K .......... .......... .......... .......... .......... 12% 25.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44405:2219600K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44518:2225250K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44599:2229300K .......... .......... .......... .......... .......... 12% 35.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44611:2229900K .......... .......... .......... .......... .......... 12% 35.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44761:2237400K .......... .......... .......... .......... .......... 12% 45.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:44832:2240950K .......... .......... .......... .......... .......... 12% 45.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45143:2256500K .......... .......... .......... .......... .......... 12% 35.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45300:2264350K .......... .......... .......... .......... .......... 12% 35.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45408:2269750K .......... .......... .......... .......... .......... 12% 45.3M 4m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45578:2278250K .......... .......... .......... .......... .......... 12% 85.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45659:2282300K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45761:2287400K .......... .......... .......... .......... .......... 12% 65.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45768:2287750K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45785:2288600K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45840:2291350K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:45905:2294600K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:46261:2312400K .......... .......... .......... .......... .......... 12% 35.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:46332:2315950K .......... .......... .......... .......... .......... 12% 45.3M 4m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:46430:2320850K .......... .......... .......... .......... .......... 12% 45.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:46717:2335200K .......... .......... .......... .......... .......... 12% 75.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:46919:2345300K .......... .......... .......... .......... .......... 12% 35.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47026:2350650K .......... .......... .......... .......... .......... 12% 45.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47091:2353900K .......... .......... .......... .......... .......... 12% 45.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47145:2356600K .......... .......... .......... .......... .......... 12% 65.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47157:2357200K .......... .......... .......... .......... .......... 12% 35.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47344:2366550K .......... .......... .......... .......... .......... 13% 35.3M 4m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47499:2374300K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47566:2377650K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47607:2379700K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47670:2382850K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:47817:2390200K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48060:2402350K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48149:2406800K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48306:2414650K .......... .......... .......... .......... .......... 13% 45.3M 4m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48352:2416950K .......... .......... .......... .......... .......... 13% 35.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48398:2419250K .......... .......... .......... .......... .......... 13% 45.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48500:2424350K .......... .......... .......... .......... .......... 13% 45.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48627:2430700K .......... .......... .......... .......... .......... 13% 45.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:48787:2438700K .......... .......... .......... .......... .......... 13% 75.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:49207:2459700K .......... .......... .......... .......... .......... 13% 55.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:49286:2463650K .......... .......... .......... .......... .......... 13% 35.3M 4m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:49417:2470200K .......... .......... .......... .......... .......... 13% 35.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:49561:2477400K .......... .......... .......... .......... .......... 13% 95.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:49647:2481700K .......... .......... .......... .......... .......... 13% 35.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:49912:2494950K .......... .......... .......... .......... .......... 13% 45.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:50117:2505200K .......... .......... .......... .......... .......... 13% 45.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:50146:2506650K .......... .......... .......... .......... .......... 13% 35.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:50198:2509250K .......... .......... .......... .......... .......... 13% 35.3M 4m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:50964:2547550K .......... .......... .......... .......... .......... 14% 45.3M 4m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:50966:2547650K .......... .......... .......... .......... .......... 14% 45.3M 4m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51238:2561250K .......... .......... .......... .......... .......... 14% 45.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51440:2571350K .......... .......... .......... .......... .......... 14% 95.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51609:2579800K .......... .......... .......... .......... .......... 14% 35.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51659:2582300K .......... .......... .......... .......... .......... 14% 35.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51764:2587550K .......... .......... .......... .......... .......... 14% 75.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51886:2593650K .......... .......... .......... .......... .......... 14% 35.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:51921:2595400K .......... .......... .......... .......... .......... 14% 45.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52002:2599450K .......... .......... .......... .......... .......... 14% 45.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52067:2602700K .......... .......... .......... .......... .......... 14% 45.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52137:2606200K .......... .......... .......... .......... .......... 14% 55.3M 4m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52171:2607900K .......... .......... .......... .......... .......... 14% 55.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52261:2612400K .......... .......... .......... .......... .......... 14% 85.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52613:2630000K .......... .......... .......... .......... .......... 14% 55.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52651:2631900K .......... .......... .......... .......... .......... 14% 85.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52724:2635550K .......... .......... .......... .......... .......... 14% 35.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:52795:2639100K .......... .......... .......... .......... .......... 14% 35.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53005:2649600K .......... .......... .......... .......... .......... 14% 45.3M 4m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53317:2665200K .......... .......... .......... .......... .......... 14% 35.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53604:2679550K .......... .......... .......... .......... .......... 14% 45.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53632:2680950K .......... .......... .......... .......... .......... 14% 45.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53639:2681300K .......... .......... .......... .......... .......... 14% 35.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53974:2698050K .......... .......... .......... .......... .......... 14% 45.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53985:2698600K .......... .......... .......... .......... .......... 14% 45.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:53994:2699050K .......... .......... .......... .......... .......... 14% 35.3M 4m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:54135:2706100K .......... .......... .......... .......... .......... 14% 45.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:54398:2719250K .......... .......... .......... .......... .......... 14% 45.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:54604:2729550K .......... .......... .......... .......... .......... 15% 45.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:54699:2734300K .......... .......... .......... .......... .......... 15% 75.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:54873:2743000K .......... .......... .......... .......... .......... 15% 65.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:55322:2765450K .......... .......... .......... .......... .......... 15% 45.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:55342:2766450K .......... .......... .......... .......... .......... 15% 35.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:55597:2779200K .......... .......... .......... .......... .......... 15% 55.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:55728:2785750K .......... .......... .......... .......... .......... 15% 45.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:55770:2787850K .......... .......... .......... .......... .......... 15% 45.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:55979:2798300K .......... .......... .......... .......... .......... 15% 45.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56066:2802650K .......... .......... .......... .......... .......... 15% 45.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56105:2804600K .......... .......... .......... .......... .......... 15% 45.3M 4m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56273:2813000K .......... .......... .......... .......... .......... 15% 45.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56330:2815850K .......... .......... .......... .......... .......... 15% 45.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56744:2836550K .......... .......... .......... .......... .......... 15% 55.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56814:2840050K .......... .......... .......... .......... .......... 15% 75.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:56923:2845500K .......... .......... .......... .......... .......... 15% 45.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:57099:2854300K .......... .......... .......... .......... .......... 15% 55.3M 4m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:57198:2859250K .......... .......... .......... .......... .......... 15% 45.3M 4m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:57769:2887800K .......... .......... .......... .......... .......... 15% 45.3M 4m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58063:2902500K .......... .......... .......... .......... .......... 15% 45.3M 4m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58190:2908850K .......... .......... .......... .......... .......... 15% 45.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58411:2919900K .......... .......... .......... .......... .......... 16% 35.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58607:2929700K .......... .......... .......... .......... .......... 16% 35.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58643:2931500K .......... .......... .......... .......... .......... 16% 35.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58664:2932550K .......... .......... .......... .......... .......... 16% 45.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58763:2937500K .......... .......... .......... .......... .......... 16% 35.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:58899:2944300K .......... .......... .......... .......... .......... 16% 35.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59090:2953850K .......... .......... .......... .......... .......... 16% 65.3M 4m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59377:2968200K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59382:2968450K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59508:2974750K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59553:2977000K .......... .......... .......... .......... .......... 16% 65.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59586:2978650K .......... .......... .......... .......... .......... 16% 25.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59715:2985100K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59772:2987950K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59878:2993250K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59982:2998450K .......... .......... .......... .......... .......... 16% 45.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:59987:2998700K .......... .......... .......... .......... .......... 16% 35.3M 4m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:60161:3007400K .......... .......... .......... .......... .......... 16% 45.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:60531:3025900K .......... .......... .......... .......... .......... 16% 35.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:60625:3030600K .......... .......... .......... .......... .......... 16% 55.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:60655:3032100K .......... .......... .......... .......... .......... 16% 45.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:60894:3044050K .......... .......... .......... .......... .......... 16% 55.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:60930:3045850K .......... .......... .......... .......... .......... 16% 55.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61000:3049350K .......... .......... .......... .......... .......... 16% 25.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61026:3050650K .......... .......... .......... .......... .......... 16% 45.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61040:3051350K .......... .......... .......... .......... .......... 16% 45.3M 4m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61138:3056250K .......... .......... .......... .......... .......... 16% 45.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61353:3067000K .......... .......... .......... .......... .......... 16% 45.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61509:3074800K .......... .......... .......... .......... .......... 16% 35.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61535:3076100K .......... .......... .......... .......... .......... 16% 45.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61566:3077650K .......... .......... .......... .......... .......... 16% 75.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61948:3096750K .......... .......... .......... .......... .......... 17% 75.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:61985:3098600K .......... .......... .......... .......... .......... 17% 95.3M 4m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62135:3106100K .......... .......... .......... .......... .......... 17% 25.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62206:3109650K .......... .......... .......... .......... .......... 17% 45.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62442:3121450K .......... .......... .......... .......... .......... 17% 45.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62462:3122450K .......... .......... .......... .......... .......... 17% 45.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62753:3137000K .......... .......... .......... .......... .......... 17% 45.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62826:3140650K .......... .......... .......... .......... .......... 17% 45.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:62950:3146850K .......... .......... .......... .......... .......... 17% 55.3M 4m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:63126:3155650K .......... .......... .......... .......... .......... 17% 45.3M 4m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:63173:3158000K .......... .......... .......... .......... .......... 17% 35.3M 4m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:63202:3159450K .......... .......... .......... .......... .......... 17% 45.3M 4m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:63611:3179900K .......... .......... .......... .......... .......... 17% 35.3M 4m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:63941:3196400K .......... .......... .......... .......... .......... 17% 35.3M 4m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:64091:3203900K .......... .......... .......... .......... .......... 17% 65.3M 4m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:64163:3207500K .......... .......... .......... .......... .......... 17% 45.3M 4m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:64263:3212500K .......... .......... .......... .......... .......... 17% 35.3M 4m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:64307:3214700K .......... .......... .......... .......... .......... 17% 45.3M 4m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:64403:3219500K .......... .......... .......... .......... .......... 17% 45.3M 4m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:64742:3236450K .......... .......... .......... .......... .......... 17% 45.3M 4m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65006:3249650K .......... .......... .......... .......... .......... 17% 45.3M 4m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65338:3266250K .......... .......... .......... .......... .......... 17% 75.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65384:3268550K .......... .......... .......... .......... .......... 17% 45.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65504:3274550K .......... .......... .......... .......... .......... 17% 45.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65595:3279100K .......... .......... .......... .......... .......... 18% 35.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65629:3280800K .......... .......... .......... .......... .......... 18% 25.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65922:3295450K .......... .......... .......... .......... .......... 18% 45.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:65994:3299050K .......... .......... .......... .......... .......... 18% 35.3M 4m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:66396:3319150K .......... .......... .......... .......... .......... 18% 25.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:66447:3321700K .......... .......... .......... .......... .......... 18% 75.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:66461:3322400K .......... .......... .......... .......... .......... 18% 45.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:66706:3334650K .......... .......... .......... .......... .......... 18% 35.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:66926:3345650K .......... .......... .......... .......... .......... 18% 45.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67222:3360450K .......... .......... .......... .......... .......... 18% 35.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67260:3362350K .......... .......... .......... .......... .......... 18% 45.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67297:3364200K .......... .......... .......... .......... .......... 18% 45.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67516:3375150K .......... .......... .......... .......... .......... 18% 45.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67884:3393550K .......... .......... .......... .......... .......... 18% 35.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67886:3393650K .......... .......... .......... .......... .......... 18% 75.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:67920:3395350K .......... .......... .......... .......... .......... 18% 55.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68043:3401500K .......... .......... .......... .......... .......... 18% 45.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68157:3407200K .......... .......... .......... .......... .......... 18% 25.3M 4m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68394:3419050K .......... .......... .......... .......... .......... 18% 45.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68407:3419700K .......... .......... .......... .......... .......... 18% 45.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68588:3428750K .......... .......... .......... .......... .......... 18% 25.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68649:3431800K .......... .......... .......... .......... .......... 18% 45.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68719:3435300K .......... .......... .......... .......... .......... 18% 45.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:68899:3444300K .......... .......... .......... .......... .......... 18% 25.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69006:3449650K .......... .......... .......... .......... .......... 18% 35.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69091:3453900K .......... .......... .......... .......... .......... 18% 35.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69333:3466000K .......... .......... .......... .......... .......... 19% 35.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69475:3473100K .......... .......... .......... .......... .......... 19% 55.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69566:3477650K .......... .......... .......... .......... .......... 19% 65.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69744:3486550K .......... .......... .......... .......... .......... 19% 35.3M 4m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:69988:3498750K .......... .......... .......... .......... .......... 19% 35.3M 4m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:70012:3499950K .......... .......... .......... .......... .......... 19% 55.3M 4m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:70554:3527050K .......... .......... .......... .......... .......... 19% 45.3M 4m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:70706:3534650K .......... .......... .......... .......... .......... 19% 35.3M 4m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:70780:3538350K .......... .......... .......... .......... .......... 19% 45.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71063:3552500K .......... .......... .......... .......... .......... 19% 45.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71186:3558650K .......... .......... .......... .......... .......... 19% 75.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71189:3558800K .......... .......... .......... .......... .......... 19% 45.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71213:3560000K .......... .......... .......... .......... .......... 19% 15.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71298:3564250K .......... .......... .......... .......... .......... 19% 25.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71386:3568650K .......... .......... .......... .......... .......... 19% 45.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71575:3578100K .......... .......... .......... .......... .......... 19% 45.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:71749:3586800K .......... .......... .......... .......... .......... 19% 65.3M 4m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:72811:3639900K .......... .......... .......... .......... .......... 20% 35.3M 4m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:72985:3648600K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73018:3650250K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73146:3656650K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73335:3666100K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73402:3669450K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73436:3671150K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73523:3675500K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73851:3691900K .......... .......... .......... .......... .......... 20% 35.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:73916:3695150K .......... .......... .......... .......... .......... 20% 45.3M 4m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:74675:3733100K .......... .......... .......... .......... .......... 20% 75.3M 4m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75174:3758050K .......... .......... .......... .......... .......... 20% 25.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75183:3758500K .......... .......... .......... .......... .......... 20% 35.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75189:3758800K .......... .......... .......... .......... .......... 20% 65.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75315:3765100K .......... .......... .......... .......... .......... 20% 35.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75354:3767050K .......... .......... .......... .......... .......... 20% 45.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75366:3767650K .......... .......... .......... .......... .......... 20% 45.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75381:3768400K .......... .......... .......... .......... .......... 20% 45.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75473:3773000K .......... .......... .......... .......... .......... 20% 45.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75533:3776000K .......... .......... .......... .......... .......... 20% 45.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:75561:3777400K .......... .......... .......... .......... .......... 20% 35.3M 4m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:76335:3816100K .......... .......... .......... .......... .......... 20% 35.3M 4m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:76733:3836000K .......... .......... .......... .......... .......... 21% 45.3M 4m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:76813:3840000K .......... .......... .......... .......... .......... 21% 45.3M 4m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:76834:3841050K .......... .......... .......... .......... .......... 21% 85.3M 4m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:76898:3844250K .......... .......... .......... .......... .......... 21% 45.3M 4m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:77142:3856450K .......... .......... .......... .......... .......... 21% 35.3M 4m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:77526:3875650K .......... .......... .......... .......... .......... 21% 35.3M 4m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:77546:3876650K .......... .......... .......... .......... .......... 21% 45.3M 4m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:77651:3881900K .......... .......... .......... .......... .......... 21% 55.3M 4m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:77884:3893550K .......... .......... .......... .......... .......... 21% 35.3M 4m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:77918:3895250K .......... .......... .......... .......... .......... 21% 75.3M 4m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:78360:3917350K .......... .......... .......... .......... .......... 21% 45.3M 4m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:78498:3924250K .......... .......... .......... .......... .......... 21% 45.3M 4m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:78553:3927000K .......... .......... .......... .......... .......... 21% 55.3M 4m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:78790:3938850K .......... .......... .......... .......... .......... 21% 25.3M 4m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:78822:3940450K .......... .......... .......... .......... .......... 21% 35.3M 4m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:78971:3947900K .......... .......... .......... .......... .......... 21% 45.3M 4m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:79569:3977800K .......... .......... .......... .......... .......... 21% 75.3M 4m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:79627:3980700K .......... .......... .......... .......... .......... 21% 45.3M 4m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:79973:3998000K .......... .......... .......... .......... .......... 21% 35.3M 4m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:79991:3998900K .......... .......... .......... .......... .......... 21% 75.3M 4m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80100:4004350K .......... .......... .......... .......... .......... 22% 25.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80110:4004850K .......... .......... .......... .......... .......... 22% 35.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80172:4007950K .......... .......... .......... .......... .......... 22% 25.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80185:4008600K .......... .......... .......... .......... .......... 22% 45.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80291:4013900K .......... .......... .......... .......... .......... 22% 65.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80369:4017800K .......... .......... .......... .......... .......... 22% 45.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80379:4018300K .......... .......... .......... .......... .......... 22% 25.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80401:4019400K .......... .......... .......... .......... .......... 22% 55.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80479:4023300K .......... .......... .......... .......... .......... 22% 55.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80744:4036550K .......... .......... .......... .......... .......... 22% 25.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80819:4040300K .......... .......... .......... .......... .......... 22% 65.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80849:4041800K .......... .......... .......... .......... .......... 22% 45.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80899:4044300K .......... .......... .......... .......... .......... 22% 45.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:80930:4045850K .......... .......... .......... .......... .......... 22% 25.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81119:4055300K .......... .......... .......... .......... .......... 22% 15.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81297:4064200K .......... .......... .......... .......... .......... 22% 45.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81450:4071850K .......... .......... .......... .......... .......... 22% 45.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81476:4073150K .......... .......... .......... .......... .......... 22% 55.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81531:4075900K .......... .......... .......... .......... .......... 22% 65.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81743:4086500K .......... .......... .......... .......... .......... 22% 45.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81774:4088050K .......... .......... .......... .......... .......... 22% 35.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81805:4089600K .......... .......... .......... .......... .......... 22% 75.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:81903:4094500K .......... .......... .......... .......... .......... 22% 45.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82005:4099600K .......... .......... .......... .......... .......... 22% 45.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82006:4099650K .......... .......... .......... .......... .......... 22% 65.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82204:4109550K .......... .......... .......... .......... .......... 22% 25.3M 4m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82289:4113800K .......... .......... .......... .......... .......... 22% 75.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82339:4116300K .......... .......... .......... .......... .......... 22% 65.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82348:4116750K .......... .......... .......... .......... .......... 22% 35.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82762:4137450K .......... .......... .......... .......... .......... 22% 45.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:82804:4139550K .......... .......... .......... .......... .......... 22% 35.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:83029:4150800K .......... .......... .......... .......... .......... 22% 45.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:83209:4159800K .......... .......... .......... .......... .......... 22% 45.3M 4m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:83340:4166350K .......... .......... .......... .......... .......... 22% 45.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:83993:4199000K .......... .......... .......... .......... .......... 23% 75.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84019:4200300K .......... .......... .......... .......... .......... 23% 45.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84140:4206350K .......... .......... .......... .......... .......... 23% 45.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84142:4206450K .......... .......... .......... .......... .......... 23% 45.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84146:4206650K .......... .......... .......... .......... .......... 23% 45.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84159:4207300K .......... .......... .......... .......... .......... 23% 45.3M 4m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84299:4214300K .......... .......... .......... .......... .......... 23% 55.3M 4m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84454:4222050K .......... .......... .......... .......... .......... 23% 25.3M 4m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84606:4229650K .......... .......... .......... .......... .......... 23% 25.3M 4m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:84925:4245600K .......... .......... .......... .......... .......... 23% 65.3M 4m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85235:4261100K .......... .......... .......... .......... .......... 23% 45.3M 4m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85535:4276100K .......... .......... .......... .......... .......... 23% 65.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85571:4277900K .......... .......... .......... .......... .......... 23% 45.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85606:4279650K .......... .......... .......... .......... .......... 23% 35.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85630:4280850K .......... .......... .......... .......... .......... 23% 25.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85644:4281550K .......... .......... .......... .......... .......... 23% 45.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85710:4284850K .......... .......... .......... .......... .......... 23% 85.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85789:4288800K .......... .......... .......... .......... .......... 23% 45.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85808:4289750K .......... .......... .......... .......... .......... 23% 55.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85865:4292600K .......... .......... .......... .......... .......... 23% 75.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85986:4298650K .......... .......... .......... .......... .......... 23% 45.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:85994:4299050K .......... .......... .......... .......... .......... 23% 45.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:86030:4300850K .......... .......... .......... .......... .......... 23% 75.3M 4m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:86353:4317000K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:86503:4324500K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:86671:4332900K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:86970:4347850K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87035:4351100K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87047:4351700K .......... .......... .......... .......... .......... 23% 55.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87073:4353000K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87088:4353750K .......... .......... .......... .......... .......... 23% 35.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87242:4361450K .......... .......... .......... .......... .......... 23% 45.3M 4m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87392:4368950K .......... .......... .......... .......... .......... 24% 55.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87516:4375150K .......... .......... .......... .......... .......... 24% 45.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87540:4376350K .......... .......... .......... .......... .......... 24% 45.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:87635:4381100K .......... .......... .......... .......... .......... 24% 45.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88063:4402500K .......... .......... .......... .......... .......... 24% 45.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88069:4402800K .......... .......... .......... .......... .......... 24% 35.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88144:4406550K .......... .......... .......... .......... .......... 24% 45.3M 4m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88356:4417150K .......... .......... .......... .......... .......... 24% 35.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88690:4433850K .......... .......... .......... .......... .......... 24% 45.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88692:4433950K .......... .......... .......... .......... .......... 24% 45.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88754:4437050K .......... .......... .......... .......... .......... 24% 45.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88768:4437750K .......... .......... .......... .......... .......... 24% 45.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:88809:4439800K .......... .......... .......... .......... .......... 24% 45.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:89110:4454850K .......... .......... .......... .......... .......... 24% 65.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:89129:4455800K .......... .......... .......... .......... .......... 24% 35.3M 4m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:89454:4472050K .......... .......... .......... .......... .......... 24% 45.3M 4m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:89750:4486850K .......... .......... .......... .......... .......... 24% 35.3M 4m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:89773:4488000K .......... .......... .......... .......... .......... 24% 35.3M 4m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:89946:4496650K .......... .......... .......... .......... .......... 24% 75.3M 4m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90315:4515100K .......... .......... .......... .......... .......... 24% 85.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90340:4516350K .......... .......... .......... .......... .......... 24% 55.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90382:4518450K .......... .......... .......... .......... .......... 24% 25.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90409:4519800K .......... .......... .......... .......... .......... 24% 35.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90410:4519850K .......... .......... .......... .......... .......... 24% 55.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90418:4520250K .......... .......... .......... .......... .......... 24% 45.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90435:4521100K .......... .......... .......... .......... .......... 24% 35.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90497:4524200K .......... .......... .......... .......... .......... 24% 35.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90636:4531150K .......... .......... .......... .......... .......... 24% 55.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:90828:4540750K .......... .......... .......... .......... .......... 24% 35.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91002:4549450K .......... .......... .......... .......... .......... 25% 45.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91020:4550350K .......... .......... .......... .......... .......... 25% 35.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91029:4550800K .......... .......... .......... .......... .......... 25% 85.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91118:4555250K .......... .......... .......... .......... .......... 25% 45.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91136:4556150K .......... .......... .......... .......... .......... 25% 45.3M 4m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91419:4570300K .......... .......... .......... .......... .......... 25% 35.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91421:4570400K .......... .......... .......... .......... .......... 25% 95.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91520:4575350K .......... .......... .......... .......... .......... 25% 35.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91563:4577500K .......... .......... .......... .......... .......... 25% 35.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91826:4590650K .......... .......... .......... .......... .......... 25% 45.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91846:4591650K .......... .......... .......... .......... .......... 25% 35.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:91948:4596750K .......... .......... .......... .......... .......... 25% 45.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92007:4599700K .......... .......... .......... .......... .......... 25% 35.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92072:4602950K .......... .......... .......... .......... .......... 25% 25.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92085:4603600K .......... .......... .......... .......... .......... 25% 45.3M 4m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92358:4617250K .......... .......... .......... .......... .......... 25% 25.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92374:4618050K .......... .......... .......... .......... .......... 25% 35.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92841:4641400K .......... .......... .......... .......... .......... 25% 45.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92935:4646100K .......... .......... .......... .......... .......... 25% 35.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:92954:4647050K .......... .......... .......... .......... .......... 25% 45.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93044:4651550K .......... .......... .......... .......... .......... 25% 45.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93192:4658950K .......... .......... .......... .......... .......... 25% 35.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93287:4663700K .......... .......... .......... .......... .......... 25% 55.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93319:4665300K .......... .......... .......... .......... .......... 25% 35.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93338:4666250K .......... .......... .......... .......... .......... 25% 45.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93368:4667750K .......... .......... .......... .......... .......... 25% 35.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93409:4669800K .......... .......... .......... .......... .......... 25% 35.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93533:4676000K .......... .......... .......... .......... .......... 25% 35.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93585:4678600K .......... .......... .......... .......... .......... 25% 35.3M 4m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:93985:4698600K .......... .......... .......... .......... .......... 25% 55.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:94255:4712100K .......... .......... .......... .......... .......... 25% 65.3M 4m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:94939:4746300K .......... .......... .......... .......... .......... 26% 25.3M 4m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:95083:4753500K .......... .......... .......... .......... .......... 26% 35.3M 4m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:95138:4756250K .......... .......... .......... .......... .......... 26% 35.3M 4m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:95481:4773400K .......... .......... .......... .......... .......... 26% 45.3M 4m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:95842:4791450K .......... .......... .......... .......... .......... 26% 45.3M 4m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96006:4799650K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96195:4809100K .......... .......... .......... .......... .......... 26% 35.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96205:4809600K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96348:4816750K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96363:4817500K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96376:4818150K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96416:4820150K .......... .......... .......... .......... .......... 26% 75.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96652:4831950K .......... .......... .......... .......... .......... 26% 25.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96918:4845250K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96927:4845700K .......... .......... .......... .......... .......... 26% 35.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96950:4846850K .......... .......... .......... .......... .......... 26% 45.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:96993:4849000K .......... .......... .......... .......... .......... 26% 25.3M 4m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97083:4853500K .......... .......... .......... .......... .......... 26% 25.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97424:4870550K .......... .......... .......... .......... .......... 26% 25.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97431:4870900K .......... .......... .......... .......... .......... 26% 45.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97464:4872550K .......... .......... .......... .......... .......... 26% 45.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97495:4874100K .......... .......... .......... .......... .......... 26% 25.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97513:4875000K .......... .......... .......... .......... .......... 26% 25.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97627:4880700K .......... .......... .......... .......... .......... 26% 65.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97649:4881800K .......... .......... .......... .......... .......... 26% 35.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97867:4892700K .......... .......... .......... .......... .......... 26% 45.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:97920:4895350K .......... .......... .......... .......... .......... 26% 35.3M 4m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:98123:4905500K .......... .......... .......... .......... .......... 26% 45.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:98156:4907150K .......... .......... .......... .......... .......... 26% 25.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:98292:4913950K .......... .......... .......... .......... .......... 27% 45.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:98330:4915850K .......... .......... .......... .......... .......... 27% 45.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:98721:4935400K .......... .......... .......... .......... .......... 27% 75.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99011:4949900K .......... .......... .......... .......... .......... 27% 25.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99034:4951050K .......... .......... .......... .......... .......... 27% 35.3M 4m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99339:4966300K .......... .......... .......... .......... .......... 27% 95.3M 4m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99372:4967950K .......... .......... .......... .......... .......... 27% 55.3M 4m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99409:4969800K .......... .......... .......... .......... .......... 27% 45.3M 4m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99591:4978900K .......... .......... .......... .......... .......... 27% 35.3M 4m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99775:4988100K .......... .......... .......... .......... .......... 27% 35.3M 4m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:99988:4998750K .......... .......... .......... .......... .......... 27% 35.3M 4m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:100300:5014350K .......... .......... .......... .......... .......... 27% 35.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:100421:5020400K .......... .......... .......... .......... .......... 27% 35.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:100506:5024650K .......... .......... .......... .......... .......... 27% 45.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:100516:5025150K .......... .......... .......... .......... .......... 27% 45.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:100636:5031150K .......... .......... .......... .......... .......... 27% 45.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101032:5050950K .......... .......... .......... .......... .......... 27% 45.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101034:5051050K .......... .......... .......... .......... .......... 27% 45.3M 4m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101219:5060300K .......... .......... .......... .......... .......... 27% 65.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101243:5061500K .......... .......... .......... .......... .......... 27% 35.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101352:5066950K .......... .......... .......... .......... .......... 27% 35.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101570:5077850K .......... .......... .......... .......... .......... 27% 35.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101825:5090600K .......... .......... .......... .......... .......... 27% 55.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:101967:5097700K .......... .......... .......... .......... .......... 28% 95.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102001:5099400K .......... .......... .......... .......... .......... 28% 45.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102053:5102000K .......... .......... .......... .......... .......... 28% 45.3M 4m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102199:5109300K .......... .......... .......... .......... .......... 28% 45.3M 3m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102594:5129050K .......... .......... .......... .......... .......... 28% 25.3M 3m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102815:5140100K .......... .......... .......... .......... .......... 28% 45.3M 3m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102823:5140500K .......... .......... .......... .......... .......... 28% 45.3M 3m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:102962:5147450K .......... .......... .......... .......... .......... 28% 45.3M 3m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103202:5159450K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103251:5161900K .......... .......... .......... .......... .......... 28% 35.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103314:5165050K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103493:5174000K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103521:5175400K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103614:5180050K .......... .......... .......... .......... .......... 28% 65.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103625:5180600K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:103852:5191950K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104107:5204700K .......... .......... .......... .......... .......... 28% 45.3M 3m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104220:5210350K .......... .......... .......... .......... .......... 28% 45.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104307:5214700K .......... .......... .......... .......... .......... 28% 45.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104310:5214850K .......... .......... .......... .......... .......... 28% 45.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104311:5214900K .......... .......... .......... .......... .......... 28% 45.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104493:5224000K .......... .......... .......... .......... .......... 28% 85.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104581:5228400K .......... .......... .......... .......... .......... 28% 25.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:104664:5232550K .......... .......... .......... .......... .......... 28% 45.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:105197:5259200K .......... .......... .......... .......... .......... 28% 35.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:105281:5263400K .......... .......... .......... .......... .......... 28% 35.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:105288:5263750K .......... .......... .......... .......... .......... 28% 35.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:105535:5276100K .......... .......... .......... .......... .......... 28% 35.3M 3m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:106256:5312150K .......... .......... .......... .......... .......... 29% 45.3M 3m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:106305:5314600K .......... .......... .......... .......... .......... 29% 45.3M 3m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:106420:5320350K .......... .......... .......... .......... .......... 29% 65.3M 3m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:106501:5324400K .......... .......... .......... .......... .......... 29% 35.3M 3m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:106617:5330200K .......... .......... .......... .......... .......... 29% 45.3M 3m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:107114:5355050K .......... .......... .......... .......... .......... 29% 35.3M 3m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:107285:5363600K .......... .......... .......... .......... .......... 29% 45.3M 3m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:107356:5367150K .......... .......... .......... .......... .......... 29% 35.3M 3m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:107585:5378600K .......... .......... .......... .......... .......... 29% 65.3M 3m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:107823:5390500K .......... .......... .......... .......... .......... 29% 35.3M 3m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:108166:5407650K .......... .......... .......... .......... .......... 29% 45.3M 3m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:108289:5413800K .......... .......... .......... .......... .......... 29% 75.3M 3m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:108560:5427350K .......... .......... .......... .......... .......... 29% 65.3M 3m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:108609:5429800K .......... .......... .......... .......... .......... 29% 35.3M 3m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:108771:5437900K .......... .......... .......... .......... .......... 29% 35.3M 3m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:108817:5440200K .......... .......... .......... .......... .......... 29% 45.3M 3m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:109054:5452050K .......... .......... .......... .......... .......... 29% 45.3M 3m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:109496:5474150K .......... .......... .......... .......... .......... 30% 45.3M 3m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:109535:5476100K .......... .......... .......... .......... .......... 30% 45.3M 3m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:109823:5490500K .......... .......... .......... .......... .......... 30% 45.3M 3m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:109987:5498700K .......... .......... .......... .......... .......... 30% 25.3M 3m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:110372:5517950K .......... .......... .......... .......... .......... 30% 55.3M 3m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:110426:5520650K .......... .......... .......... .......... .......... 30% 35.3M 3m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:110587:5528700K .......... .......... .......... .......... .......... 30% 15.3M 3m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:110658:5532250K .......... .......... .......... .......... .......... 30% 35.3M 3m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:110909:5544800K .......... .......... .......... .......... .......... 30% 35.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111181:5558400K .......... .......... .......... .......... .......... 30% 45.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111187:5558700K .......... .......... .......... .......... .......... 30% 45.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111215:5560100K .......... .......... .......... .......... .......... 30% 45.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111247:5561700K .......... .......... .......... .......... .......... 30% 45.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111484:5573550K .......... .......... .......... .......... .......... 30% 75.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111533:5576000K .......... .......... .......... .......... .......... 30% 65.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111539:5576300K .......... .......... .......... .......... .......... 30% 45.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111607:5579700K .......... .......... .......... .......... .......... 30% 35.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111732:5585950K .......... .......... .......... .......... .......... 30% 55.3M 3m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:111857:5592200K .......... .......... .......... .......... .......... 30% 35.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112049:5601800K .......... .......... .......... .......... .......... 30% 45.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112065:5602600K .......... .......... .......... .......... .......... 30% 25.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112179:5608300K .......... .......... .......... .......... .......... 30% 15.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112189:5608800K .......... .......... .......... .......... .......... 30% 35.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112403:5619500K .......... .......... .......... .......... .......... 30% 45.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112553:5627000K .......... .......... .......... .......... .......... 30% 65.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112554:5627050K .......... .......... .......... .......... .......... 30% 5.36M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112728:5635750K .......... .......... .......... .......... .......... 30% 15.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112742:5636450K .......... .......... .......... .......... .......... 30% 35.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:112806:5639650K .......... .......... .......... .......... .......... 30% 35.3M 3m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113063:5652500K .......... .......... .......... .......... .......... 31% 55.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113108:5654750K .......... .......... .......... .......... .......... 31% 55.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113236:5661150K .......... .......... .......... .......... .......... 31% 75.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113263:5662500K .......... .......... .......... .......... .......... 31% 85.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113339:5666300K .......... .......... .......... .......... .......... 31% 45.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113401:5669400K .......... .......... .......... .......... .......... 31% 45.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113619:5680300K .......... .......... .......... .......... .......... 31% 35.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113879:5693300K .......... .......... .......... .......... .......... 31% 45.3M 3m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:113928:5695750K .......... .......... .......... .......... .......... 31% 25.3M 3m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:114054:5702050K .......... .......... .......... .......... .......... 31% 65.3M 3m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:114157:5707200K .......... .......... .......... .......... .......... 31% 95.3M 3m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:114649:5731800K .......... .......... .......... .......... .......... 31% 55.3M 3m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:114861:5742400K .......... .......... .......... .......... .......... 31% 35.3M 3m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:114925:5745600K .......... .......... .......... .......... .......... 31% 55.3M 3m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115068:5752750K .......... .......... .......... .......... .......... 31% 25.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115217:5760200K .......... .......... .......... .......... .......... 31% 35.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115259:5762300K .......... .......... .......... .......... .......... 31% 45.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115263:5762500K .......... .......... .......... .......... .......... 31% 45.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115326:5765650K .......... .......... .......... .......... .......... 31% 35.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115533:5776000K .......... .......... .......... .......... .......... 31% 45.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115549:5776800K .......... .......... .......... .......... .......... 31% 45.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115643:5781500K .......... .......... .......... .......... .......... 31% 55.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115867:5792700K .......... .......... .......... .......... .......... 31% 15.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:115990:5798850K .......... .......... .......... .......... .......... 31% 45.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:116150:5806850K .......... .......... .......... .......... .......... 31% 35.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:116210:5809850K .......... .......... .......... .......... .......... 31% 15.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:116296:5814150K .......... .......... .......... .......... .......... 31% 35.3M 3m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:116658:5832250K .......... .......... .......... .......... .......... 32% 45.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:116684:5833550K .......... .......... .......... .......... .......... 32% 45.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117079:5853300K .......... .......... .......... .......... .......... 32% 35.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117088:5853750K .......... .......... .......... .......... .......... 32% 65.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117114:5855050K .......... .......... .......... .......... .......... 32% 65.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117171:5857900K .......... .......... .......... .......... .......... 32% 25.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117215:5860100K .......... .......... .......... .......... .......... 32% 15.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117318:5865250K .......... .......... .......... .......... .......... 32% 65.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117329:5865800K .......... .......... .......... .......... .......... 32% 45.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117426:5870650K .......... .......... .......... .......... .......... 32% 65.3M 3m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117676:5883150K .......... .......... .......... .......... .......... 32% 25.3M 3m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:117908:5894750K .......... .......... .......... .......... .......... 32% 45.3M 3m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118104:5904550K .......... .......... .......... .......... .......... 32% 35.3M 3m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118559:5927300K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118585:5928600K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118779:5938300K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118834:5941050K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118875:5943100K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118909:5944800K .......... .......... .......... .......... .......... 32% 55.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:118911:5944900K .......... .......... .......... .......... .......... 32% 75.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119047:5951700K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119066:5952650K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119152:5956950K .......... .......... .......... .......... .......... 32% 35.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119280:5963350K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119336:5966150K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119481:5973400K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119508:5974750K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119510:5974850K .......... .......... .......... .......... .......... 32% 45.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119546:5976650K .......... .......... .......... .......... .......... 32% 55.3M 3m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119613:5980000K .......... .......... .......... .......... .......... 32% 35.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119641:5981400K .......... .......... .......... .......... .......... 32% 45.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119764:5987550K .......... .......... .......... .......... .......... 32% 45.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119803:5989500K .......... .......... .......... .......... .......... 32% 65.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119896:5994150K .......... .......... .......... .......... .......... 32% 35.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119900:5994350K .......... .......... .......... .......... .......... 32% 35.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119913:5995000K .......... .......... .......... .......... .......... 32% 35.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:119998:5999250K .......... .......... .......... .......... .......... 32% 45.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120067:6002700K .......... .......... .......... .......... .......... 32% 25.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120088:6003750K .......... .......... .......... .......... .......... 32% 35.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120351:6016900K .......... .......... .......... .......... .......... 33% 45.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120442:6021450K .......... .......... .......... .......... .......... 33% 25.3M 3m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120682:6033450K .......... .......... .......... .......... .......... 33% 55.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120731:6035900K .......... .......... .......... .......... .......... 33% 35.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:120939:6046300K .......... .......... .......... .......... .......... 33% 75.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121023:6050500K .......... .......... .......... .......... .......... 33% 45.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121055:6052100K .......... .......... .......... .......... .......... 33% 45.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121156:6057150K .......... .......... .......... .......... .......... 33% 45.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121188:6058750K .......... .......... .......... .......... .......... 33% 45.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121434:6071050K .......... .......... .......... .......... .......... 33% 65.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121571:6077900K .......... .......... .......... .......... .......... 33% 45.3M 3m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121805:6089600K .......... .......... .......... .......... .......... 33% 35.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:121967:6097700K .......... .......... .......... .......... .......... 33% 55.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122172:6107950K .......... .......... .......... .......... .......... 33% 35.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122256:6112150K .......... .......... .......... .......... .......... 33% 35.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122345:6116600K .......... .......... .......... .......... .......... 33% 45.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122656:6132150K .......... .......... .......... .......... .......... 33% 35.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122702:6134450K .......... .......... .......... .......... .......... 33% 75.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122727:6135700K .......... .......... .......... .......... .......... 33% 45.3M 3m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122864:6142550K .......... .......... .......... .......... .......... 33% 55.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122896:6144150K .......... .......... .......... .......... .......... 33% 45.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122968:6147750K .......... .......... .......... .......... .......... 33% 35.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:122992:6148950K .......... .......... .......... .......... .......... 33% 75.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123266:6162650K .......... .......... .......... .......... .......... 33% 35.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123363:6167500K .......... .......... .......... .......... .......... 33% 45.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123467:6172700K .......... .......... .......... .......... .......... 33% 45.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123533:6176000K .......... .......... .......... .......... .......... 33% 35.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123537:6176200K .......... .......... .......... .......... .......... 33% 45.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123783:6188500K .......... .......... .......... .......... .......... 34% 85.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123895:6194100K .......... .......... .......... .......... .......... 34% 35.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123924:6195550K .......... .......... .......... .......... .......... 34% 35.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:123975:6198100K .......... .......... .......... .......... .......... 34% 75.3M 3m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124035:6201100K .......... .......... .......... .......... .......... 34% 55.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124065:6202600K .......... .......... .......... .......... .......... 34% 45.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124103:6204500K .......... .......... .......... .......... .......... 34% 25.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124143:6206500K .......... .......... .......... .......... .......... 34% 55.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124156:6207150K .......... .......... .......... .......... .......... 34% 65.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124248:6211750K .......... .......... .......... .......... .......... 34% 45.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124310:6214850K .......... .......... .......... .......... .......... 34% 35.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124380:6218350K .......... .......... .......... .......... .......... 34% 45.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124397:6219200K .......... .......... .......... .......... .......... 34% 45.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124409:6219800K .......... .......... .......... .......... .......... 34% 35.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124411:6219900K .......... .......... .......... .......... .......... 34% 35.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124605:6229600K .......... .......... .......... .......... .......... 34% 35.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124719:6235300K .......... .......... .......... .......... .......... 34% 45.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124834:6241050K .......... .......... .......... .......... .......... 34% 55.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:124953:6247000K .......... .......... .......... .......... .......... 34% 45.3M 3m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125133:6256000K .......... .......... .......... .......... .......... 34% 35.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125181:6258400K .......... .......... .......... .......... .......... 34% 45.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125288:6263750K .......... .......... .......... .......... .......... 34% 35.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125669:6282800K .......... .......... .......... .......... .......... 34% 55.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125888:6293750K .......... .......... .......... .......... .......... 34% 45.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125900:6294350K .......... .......... .......... .......... .......... 34% 35.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:125935:6296100K .......... .......... .......... .......... .......... 34% 25.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:126017:6300200K .......... .......... .......... .......... .......... 34% 45.3M 3m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:126254:6312050K .......... .......... .......... .......... .......... 34% 35.3M 3m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:126324:6315550K .......... .......... .......... .......... .......... 34% 55.3M 3m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:126587:6328700K .......... .......... .......... .......... .......... 34% 45.3M 3m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:127322:6365450K .......... .......... .......... .......... .......... 34% 75.3M 3m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:127324:6365550K .......... .......... .......... .......... .......... 34% 45.3M 3m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128033:6401000K .......... .......... .......... .......... .......... 35% 55.3M 3m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128099:6404300K .......... .......... .......... .......... .......... 35% 75.3M 3m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128279:6413300K .......... .......... .......... .......... .......... 35% 65.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128455:6422100K .......... .......... .......... .......... .......... 35% 45.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128480:6423350K .......... .......... .......... .......... .......... 35% 45.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128506:6424650K .......... .......... .......... .......... .......... 35% 45.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128697:6434200K .......... .......... .......... .......... .......... 35% 85.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128769:6437800K .......... .......... .......... .......... .......... 35% 35.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128807:6439700K .......... .......... .......... .......... .......... 35% 35.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128860:6442350K .......... .......... .......... .......... .......... 35% 45.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:128999:6449300K .......... .......... .......... .......... .......... 35% 55.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129233:6461000K .......... .......... .......... .......... .......... 35% 45.3M 3m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129282:6463450K .......... .......... .......... .......... .......... 35% 45.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129514:6475050K .......... .......... .......... .......... .......... 35% 35.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129715:6485100K .......... .......... .......... .......... .......... 35% 25.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129752:6486950K .......... .......... .......... .......... .......... 35% 55.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129786:6488650K .......... .......... .......... .......... .......... 35% 45.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129857:6492200K .......... .......... .......... .......... .......... 35% 45.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129860:6492350K .......... .......... .......... .......... .......... 35% 35.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:129927:6495700K .......... .......... .......... .......... .......... 35% 45.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130019:6500300K .......... .......... .......... .......... .......... 35% 45.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130043:6501500K .......... .......... .......... .......... .......... 35% 45.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130286:6513650K .......... .......... .......... .......... .......... 35% 35.3M 3m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130507:6524700K .......... .......... .......... .......... .......... 35% 55.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130576:6528150K .......... .......... .......... .......... .......... 35% 45.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130795:6539100K .......... .......... .......... .......... .......... 35% 85.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:130850:6541850K .......... .......... .......... .......... .......... 35% 55.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:131193:6559000K .......... .......... .......... .......... .......... 36% 35.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:131195:6559100K .......... .......... .......... .......... .......... 36% 45.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:131343:6566500K .......... .......... .......... .......... .......... 36% 55.3M 3m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:131440:6571350K .......... .......... .......... .......... .......... 36% 75.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:131666:6582650K .......... .......... .......... .......... .......... 36% 35.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:131960:6597350K .......... .......... .......... .......... .......... 36% 85.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132001:6599400K .......... .......... .......... .......... .......... 36% 35.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132092:6603950K .......... .......... .......... .......... .......... 36% 45.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132113:6605000K .......... .......... .......... .......... .......... 36% 45.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132135:6606100K .......... .......... .......... .......... .......... 36% 45.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132216:6610150K .......... .......... .......... .......... .......... 36% 55.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132368:6617750K .......... .......... .......... .......... .......... 36% 35.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132393:6619000K .......... .......... .......... .......... .......... 36% 45.3M 3m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132523:6625500K .......... .......... .......... .......... .......... 36% 45.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132743:6636500K .......... .......... .......... .......... .......... 36% 45.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132833:6641000K .......... .......... .......... .......... .......... 36% 35.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:132870:6642850K .......... .......... .......... .......... .......... 36% 45.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133022:6650450K .......... .......... .......... .......... .......... 36% 45.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133270:6662850K .......... .......... .......... .......... .......... 36% 45.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133368:6667750K .......... .......... .......... .......... .......... 36% 45.3M 3m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133635:6681100K .......... .......... .......... .......... .......... 36% 25.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133675:6683100K .......... .......... .......... .......... .......... 36% 45.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133708:6684750K .......... .......... .......... .......... .......... 36% 45.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:133891:6693900K .......... .......... .......... .......... .......... 36% 35.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134106:6704650K .......... .......... .......... .......... .......... 36% 45.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134197:6709200K .......... .......... .......... .......... .......... 36% 55.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134350:6716850K .......... .......... .......... .......... .......... 36% 35.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134512:6724950K .......... .......... .......... .......... .......... 36% 35.3M 3m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134694:6734050K .......... .......... .......... .......... .......... 37% 35.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134927:6745700K .......... .......... .......... .......... .......... 37% 45.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:134994:6749050K .......... .......... .......... .......... .......... 37% 65.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135048:6751750K .......... .......... .......... .......... .......... 37% 35.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135143:6756500K .......... .......... .......... .......... .......... 37% 45.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135158:6757250K .......... .......... .......... .......... .......... 37% 35.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135467:6772700K .......... .......... .......... .......... .......... 37% 65.3M 3m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135608:6779750K .......... .......... .......... .......... .......... 37% 45.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135787:6788700K .......... .......... .......... .......... .......... 37% 35.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135913:6795000K .......... .......... .......... .......... .......... 37% 25.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:135985:6798600K .......... .......... .......... .......... .......... 37% 55.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136375:6818100K .......... .......... .......... .......... .......... 37% 45.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136451:6821900K .......... .......... .......... .......... .......... 37% 35.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136466:6822650K .......... .......... .......... .......... .......... 37% 75.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136517:6825200K .......... .......... .......... .......... .......... 37% 45.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136582:6828450K .......... .......... .......... .......... .......... 37% 35.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136604:6829550K .......... .......... .......... .......... .......... 37% 55.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:136629:6830800K .......... .......... .......... .......... .......... 37% 65.3M 3m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137011:6849900K .......... .......... .......... .......... .......... 37% 45.3M 3m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137076:6853150K .......... .......... .......... .......... .......... 37% 45.3M 3m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137088:6853750K .......... .......... .......... .......... .......... 37% 45.3M 3m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137635:6881100K .......... .......... .......... .......... .......... 37% 55.3M 3m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137770:6887850K .......... .......... .......... .......... .......... 37% 35.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137799:6889300K .......... .......... .......... .......... .......... 37% 45.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:137817:6890200K .......... .......... .......... .......... .......... 37% 35.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138042:6901450K .......... .......... .......... .......... .......... 37% 35.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138218:6910250K .......... .......... .......... .......... .......... 37% 45.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138330:6915850K .......... .......... .......... .......... .......... 38% 55.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138440:6921350K .......... .......... .......... .......... .......... 38% 65.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138504:6924550K .......... .......... .......... .......... .......... 38% 65.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138611:6929900K .......... .......... .......... .......... .......... 38% 35.3M 3m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:138959:6947300K .......... .......... .......... .......... .......... 38% 35.3M 3m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:139057:6952200K .......... .......... .......... .......... .......... 38% 55.3M 3m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:139546:6976650K .......... .......... .......... .......... .......... 38% 45.3M 3m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:139554:6977050K .......... .......... .......... .......... .......... 38% 45.3M 3m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:139690:6983850K .......... .......... .......... .......... .......... 38% 45.3M 3m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:139818:6990250K .......... .......... .......... .......... .......... 38% 45.3M 3m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:139907:6994700K .......... .......... .......... .......... .......... 38% 55.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140023:7000500K .......... .......... .......... .......... .......... 38% 45.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140067:7002700K .......... .......... .......... .......... .......... 38% 45.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140189:7008800K .......... .......... .......... .......... .......... 38% 45.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140198:7009250K .......... .......... .......... .......... .......... 38% 65.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140201:7009400K .......... .......... .......... .......... .......... 38% 35.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140457:7022200K .......... .......... .......... .......... .......... 38% 85.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140459:7022300K .......... .......... .......... .......... .......... 38% 25.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140550:7026850K .......... .......... .......... .......... .......... 38% 45.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140711:7034900K .......... .......... .......... .......... .......... 38% 75.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140835:7041100K .......... .......... .......... .......... .......... 38% 45.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:140842:7041450K .......... .......... .......... .......... .......... 38% 45.3M 3m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141073:7053000K .......... .......... .......... .......... .......... 38% 75.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141328:7065750K .......... .......... .......... .......... .......... 38% 55.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141482:7073450K .......... .......... .......... .......... .......... 38% 85.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141714:7085050K .......... .......... .......... .......... .......... 38% 65.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141737:7086200K .......... .......... .......... .......... .......... 38% 45.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141785:7088600K .......... .......... .......... .......... .......... 38% 45.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:141875:7093100K .......... .......... .......... .......... .......... 38% 55.3M 3m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142099:7104300K .......... .......... .......... .......... .......... 39% 55.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142209:7109800K .......... .......... .......... .......... .......... 39% 75.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142225:7110600K .......... .......... .......... .......... .......... 39% 35.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142551:7126900K .......... .......... .......... .......... .......... 39% 55.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142591:7128900K .......... .......... .......... .......... .......... 39% 55.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142790:7138850K .......... .......... .......... .......... .......... 39% 45.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:142896:7144150K .......... .......... .......... .......... .......... 39% 45.3M 3m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143242:7161450K .......... .......... .......... .......... .......... 39% 45.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143255:7162100K .......... .......... .......... .......... .......... 39% 35.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143465:7172600K .......... .......... .......... .......... .......... 39% 35.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143632:7180950K .......... .......... .......... .......... .......... 39% 65.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143691:7183900K .......... .......... .......... .......... .......... 39% 35.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143740:7186350K .......... .......... .......... .......... .......... 39% 45.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:143745:7186600K .......... .......... .......... .......... .......... 39% 35.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144216:7210150K .......... .......... .......... .......... .......... 39% 35.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144221:7210400K .......... .......... .......... .......... .......... 39% 45.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144264:7212550K .......... .......... .......... .......... .......... 39% 35.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144284:7213550K .......... .......... .......... .......... .......... 39% 45.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144351:7216900K .......... .......... .......... .......... .......... 39% 45.3M 3m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144533:7226000K .......... .......... .......... .......... .......... 39% 45.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144542:7226450K .......... .......... .......... .......... .......... 39% 45.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144892:7243950K .......... .......... .......... .......... .......... 39% 65.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:144965:7247600K .......... .......... .......... .......... .......... 39% 95.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145072:7252950K .......... .......... .......... .......... .......... 39% 45.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145301:7264400K .......... .......... .......... .......... .......... 39% 45.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145382:7268450K .......... .......... .......... .......... .......... 39% 45.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145472:7272950K .......... .......... .......... .......... .......... 39% 45.3M 3m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145601:7279400K .......... .......... .......... .......... .......... 40% 55.3M 3m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145651:7281900K .......... .......... .......... .......... .......... 40% 45.3M 3m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:145825:7290600K .......... .......... .......... .......... .......... 40% 45.3M 3m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:146362:7317450K .......... .......... .......... .......... .......... 40% 35.3M 3m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:146552:7326950K .......... .......... .......... .......... .......... 40% 35.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:146554:7327050K .......... .......... .......... .......... .......... 40% 75.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:146799:7339300K .......... .......... .......... .......... .......... 40% 45.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:147012:7349950K .......... .......... .......... .......... .......... 40% 35.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:147402:7369450K .......... .......... .......... .......... .......... 40% 35.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:147475:7373100K .......... .......... .......... .......... .......... 40% 35.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:147477:7373200K .......... .......... .......... .......... .......... 40% 35.3M 3m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:147917:7395200K .......... .......... .......... .......... .......... 40% 35.3M 3m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:148205:7409600K .......... .......... .......... .......... .......... 40% 55.3M 3m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:148328:7415750K .......... .......... .......... .......... .......... 40% 45.3M 3m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:148432:7420950K .......... .......... .......... .......... .......... 40% 55.3M 3m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:148660:7432350K .......... .......... .......... .......... .......... 40% 75.3M 3m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:148731:7435900K .......... .......... .......... .......... .......... 40% 45.3M 3m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:149172:7457950K .......... .......... .......... .......... .......... 40% 45.3M 3m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:149726:7485650K .......... .......... .......... .......... .......... 41% 65.3M 3m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:149830:7490850K .......... .......... .......... .......... .......... 41% 75.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:149849:7491800K .......... .......... .......... .......... .......... 41% 35.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:149883:7493500K .......... .......... .......... .......... .......... 41% 65.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:150031:7500900K .......... .......... .......... .......... .......... 41% 55.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:150032:7500950K .......... .......... .......... .......... .......... 41% 45.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:150152:7506950K .......... .......... .......... .......... .......... 41% 45.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:150436:7521150K .......... .......... .......... .......... .......... 41% 35.3M 3m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:151057:7552200K .......... .......... .......... .......... .......... 41% 5.38M 3m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:151180:7558350K .......... .......... .......... .......... .......... 41% 75.3M 3m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:151274:7563050K .......... .......... .......... .......... .......... 41% 45.3M 3m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:151366:7567650K .......... .......... .......... .......... .......... 41% 65.3M 3m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:151717:7585200K .......... .......... .......... .......... .......... 41% 55.3M 3m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:151813:7590000K .......... .......... .......... .......... .......... 41% 95.3M 3m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152151:7606900K .......... .......... .......... .......... .......... 41% 25.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152169:7607800K .......... .......... .......... .......... .......... 41% 55.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152345:7616600K .......... .......... .......... .......... .......... 41% 75.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152373:7618000K .......... .......... .......... .......... .......... 41% 35.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152623:7630500K .......... .......... .......... .......... .......... 41% 25.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152698:7634250K .......... .......... .......... .......... .......... 41% 45.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:152872:7642950K .......... .......... .......... .......... .......... 42% 55.3M 3m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153068:7652750K .......... .......... .......... .......... .......... 42% 35.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153221:7660400K .......... .......... .......... .......... .......... 42% 35.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153260:7662350K .......... .......... .......... .......... .......... 42% 85.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153282:7663450K .......... .......... .......... .......... .......... 42% 25.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153347:7666700K .......... .......... .......... .......... .......... 42% 55.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153372:7667950K .......... .......... .......... .......... .......... 42% 35.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153642:7681450K .......... .......... .......... .......... .......... 42% 35.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153682:7683450K .......... .......... .......... .......... .......... 42% 35.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:153722:7685450K .......... .......... .......... .......... .......... 42% 75.3M 3m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:154428:7720750K .......... .......... .......... .......... .......... 42% 45.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:154607:7729700K .......... .......... .......... .......... .......... 42% 35.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155016:7750150K .......... .......... .......... .......... .......... 42% 35.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155041:7751400K .......... .......... .......... .......... .......... 42% 45.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155164:7757550K .......... .......... .......... .......... .......... 42% 35.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155312:7764950K .......... .......... .......... .......... .......... 42% 75.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155395:7769100K .......... .......... .......... .......... .......... 42% 45.3M 3m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155476:7773150K .......... .......... .......... .......... .......... 42% 45.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155812:7789950K .......... .......... .......... .......... .......... 42% 35.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155944:7796550K .......... .......... .......... .......... .......... 42% 45.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:155997:7799200K .......... .......... .......... .......... .......... 42% 15.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156098:7804250K .......... .......... .......... .......... .......... 42% 45.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156280:7813350K .......... .......... .......... .......... .......... 42% 45.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156441:7821400K .......... .......... .......... .......... .......... 42% 25.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156459:7822300K .......... .......... .......... .......... .......... 42% 35.3M 3m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156567:7827700K .......... .......... .......... .......... .......... 43% 65.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156666:7832650K .......... .......... .......... .......... .......... 43% 35.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156771:7837900K .......... .......... .......... .......... .......... 43% 35.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156962:7847450K .......... .......... .......... .......... .......... 43% 25.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:156993:7849000K .......... .......... .......... .......... .......... 43% 45.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:157116:7855150K .......... .......... .......... .......... .......... 43% 45.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:157147:7856700K .......... .......... .......... .......... .......... 43% 55.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:157261:7862400K .......... .......... .......... .......... .......... 43% 35.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:157425:7870600K .......... .......... .......... .......... .......... 43% 55.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:157521:7875400K .......... .......... .......... .......... .......... 43% 65.3M 3m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:157915:7895100K .......... .......... .......... .......... .......... 43% 35.3M 3m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:158408:7919750K .......... .......... .......... .......... .......... 43% 95.3M 3m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:158640:7931350K .......... .......... .......... .......... .......... 43% 55.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:158738:7936250K .......... .......... .......... .......... .......... 43% 65.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:158858:7942250K .......... .......... .......... .......... .......... 43% 45.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:158888:7943750K .......... .......... .......... .......... .......... 43% 55.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:158975:7948100K .......... .......... .......... .......... .......... 43% 35.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159099:7954300K .......... .......... .......... .......... .......... 43% 45.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159125:7955600K .......... .......... .......... .......... .......... 43% 45.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159193:7959000K .......... .......... .......... .......... .......... 43% 25.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159587:7978700K .......... .......... .......... .......... .......... 43% 45.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159677:7983200K .......... .......... .......... .......... .......... 43% 25.3M 3m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159765:7987600K .......... .......... .......... .......... .......... 43% 45.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:159868:7992750K .......... .......... .......... .......... .......... 43% 35.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160006:7999650K .......... .......... .......... .......... .......... 43% 95.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160291:8013900K .......... .......... .......... .......... .......... 44% 45.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160327:8015700K .......... .......... .......... .......... .......... 44% 45.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160387:8018700K .......... .......... .......... .......... .......... 44% 65.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160434:8021050K .......... .......... .......... .......... .......... 44% 45.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160493:8024000K .......... .......... .......... .......... .......... 44% 85.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160600:8029350K .......... .......... .......... .......... .......... 44% 45.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160626:8030650K .......... .......... .......... .......... .......... 44% 55.3M 3m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160834:8041050K .......... .......... .......... .......... .......... 44% 45.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:160949:8046800K .......... .......... .......... .......... .......... 44% 35.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161046:8051650K .......... .......... .......... .......... .......... 44% 35.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161276:8063150K .......... .......... .......... .......... .......... 44% 45.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161359:8067300K .......... .......... .......... .......... .......... 44% 35.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161396:8069150K .......... .......... .......... .......... .......... 44% 35.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161404:8069550K .......... .......... .......... .......... .......... 44% 35.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161480:8073350K .......... .......... .......... .......... .......... 44% 55.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161548:8076750K .......... .......... .......... .......... .......... 44% 35.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161630:8080850K .......... .......... .......... .......... .......... 44% 45.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161680:8083350K .......... .......... .......... .......... .......... 44% 45.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161687:8083700K .......... .......... .......... .......... .......... 44% 75.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161786:8088650K .......... .......... .......... .......... .......... 44% 45.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161798:8089250K .......... .......... .......... .......... .......... 44% 55.3M 3m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:161848:8091750K .......... .......... .......... .......... .......... 44% 45.3M 3m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:162128:8105750K .......... .......... .......... .......... .......... 44% 35.3M 3m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:162407:8119700K .......... .......... .......... .......... .......... 44% 35.3M 3m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:162721:8135400K .......... .......... .......... .......... .......... 44% 45.3M 3m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:162834:8141050K .......... .......... .......... .......... .......... 44% 35.3M 3m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163156:8157150K .......... .......... .......... .......... .......... 44% 75.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163164:8157550K .......... .......... .......... .......... .......... 44% 45.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163197:8159200K .......... .......... .......... .......... .......... 44% 45.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163493:8174000K .......... .......... .......... .......... .......... 44% 45.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163554:8177050K .......... .......... .......... .......... .......... 44% 75.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163742:8186450K .......... .......... .......... .......... .......... 44% 45.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163852:8191950K .......... .......... .......... .......... .......... 45% 45.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163874:8193050K .......... .......... .......... .......... .......... 45% 45.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:163875:8193100K .......... .......... .......... .......... .......... 45% 55.3M 3m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:164014:8200050K .......... .......... .......... .......... .......... 45% 35.3M 3m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:164040:8201350K .......... .......... .......... .......... .......... 45% 45.3M 3m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:164346:8216650K .......... .......... .......... .......... .......... 45% 45.3M 3m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:164424:8220550K .......... .......... .......... .......... .......... 45% 45.3M 3m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:164583:8228500K .......... .......... .......... .......... .......... 45% 55.3M 3m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:164639:8231300K .......... .......... .......... .......... .......... 45% 65.3M 3m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:165046:8251650K .......... .......... .......... .......... .......... 45% 45.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:165279:8263300K .......... .......... .......... .......... .......... 45% 55.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:165399:8269300K .......... .......... .......... .......... .......... 45% 75.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:165507:8274700K .......... .......... .......... .......... .......... 45% 45.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:165547:8276700K .......... .......... .......... .......... .......... 45% 35.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:165560:8277350K .......... .......... .......... .......... .......... 45% 85.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166331:8315900K .......... .......... .......... .......... .......... 45% 45.3M 3m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166381:8318400K .......... .......... .......... .......... .......... 45% 35.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166418:8320250K .......... .......... .......... .......... .......... 45% 65.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166483:8323500K .......... .......... .......... .......... .......... 45% 45.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166632:8330950K .......... .......... .......... .......... .......... 45% 35.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166772:8337950K .......... .......... .......... .......... .......... 45% 35.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166807:8339700K .......... .......... .......... .......... .......... 45% 35.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:166827:8340700K .......... .......... .......... .......... .......... 45% 55.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:167043:8351500K .......... .......... .......... .......... .......... 45% 45.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:167067:8352700K .......... .......... .......... .......... .......... 45% 45.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:167131:8355900K .......... .......... .......... .......... .......... 45% 35.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:167133:8356000K .......... .......... .......... .......... .......... 45% 45.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:167204:8359550K .......... .......... .......... .......... .......... 45% 45.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:167296:8364150K .......... .......... .......... .......... .......... 45% 45.3M 3m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:168171:8407900K .......... .......... .......... .......... .......... 46% 75.3M 2m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:168879:8443300K .......... .......... .......... .......... .......... 46% 75.3M 2m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:169129:8455800K .......... .......... .......... .......... .......... 46% 35.3M 2m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:169138:8456250K .......... .......... .......... .......... .......... 46% 45.3M 2m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:169564:8477550K .......... .......... .......... .......... .......... 46% 75.3M 2m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:169574:8478050K .......... .......... .......... .......... .......... 46% 35.3M 2m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:169706:8484650K .......... .......... .......... .......... .......... 46% 35.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170231:8510900K .......... .......... .......... .......... .......... 46% 45.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170257:8512200K .......... .......... .......... .......... .......... 46% 25.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170340:8516350K .......... .......... .......... .......... .......... 46% 35.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170432:8520950K .......... .......... .......... .......... .......... 46% 45.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170532:8525950K .......... .......... .......... .......... .......... 46% 45.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170612:8529950K .......... .......... .......... .......... .......... 46% 45.3M 2m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170663:8532500K .......... .......... .......... .......... .......... 46% 45.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170752:8536950K .......... .......... .......... .......... .......... 46% 55.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170821:8540400K .......... .......... .......... .......... .......... 46% 35.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170840:8541350K .......... .......... .......... .......... .......... 46% 45.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:170914:8545050K .......... .......... .......... .......... .......... 46% 45.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171266:8562650K .......... .......... .......... .......... .......... 47% 35.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171329:8565800K .......... .......... .......... .......... .......... 47% 85.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171357:8567200K .......... .......... .......... .......... .......... 47% 45.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171460:8572350K .......... .......... .......... .......... .......... 47% 45.3M 2m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171852:8591950K .......... .......... .......... .......... .......... 47% 35.3M 2m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171931:8595900K .......... .......... .......... .......... .......... 47% 35.3M 2m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171943:8596500K .......... .......... .......... .......... .......... 47% 35.3M 2m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:171978:8598250K .......... .......... .......... .......... .......... 47% 45.3M 2m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:172228:8610750K .......... .......... .......... .......... .......... 47% 45.3M 2m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:172808:8639750K .......... .......... .......... .......... .......... 47% 25.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:172812:8639950K .......... .......... .......... .......... .......... 47% 35.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:172943:8646500K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:172971:8647900K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173074:8653050K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173082:8653450K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173096:8654150K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173165:8657600K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173345:8666600K .......... .......... .......... .......... .......... 47% 95.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173428:8670750K .......... .......... .......... .......... .......... 47% 35.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173499:8674300K .......... .......... .......... .......... .......... 47% 25.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173537:8676200K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173542:8676450K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173564:8677550K .......... .......... .......... .......... .......... 47% 75.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173624:8680550K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173756:8687150K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173791:8688900K .......... .......... .......... .......... .......... 47% 35.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173838:8691250K .......... .......... .......... .......... .......... 47% 45.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173843:8691500K .......... .......... .......... .......... .......... 47% 35.3M 2m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:173969:8697800K .......... .......... .......... .......... .......... 47% 55.3M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:174020:8700350K .......... .......... .......... .......... .......... 47% 25.3M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:174164:8707550K .......... .......... .......... .......... .......... 47% 5.33M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:174486:8723650K .......... .......... .......... .......... .......... 47% 45.3M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:174619:8730300K .......... .......... .......... .......... .......... 47% 45.3M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:174686:8733650K .......... .......... .......... .......... .......... 47% 65.3M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:174931:8745900K .......... .......... .......... .......... .......... 48% 45.3M 2m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:175224:8760550K .......... .......... .......... .......... .......... 48% 35.3M 2m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:175285:8763600K .......... .......... .......... .......... .......... 48% 45.3M 2m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176176:8808150K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176291:8813900K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176318:8815250K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176374:8818050K .......... .......... .......... .......... .......... 48% 55.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176633:8831000K .......... .......... .......... .......... .......... 48% 25.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176695:8834100K .......... .......... .......... .......... .......... 48% 55.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:176954:8847050K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177026:8850650K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177039:8851300K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177148:8856750K .......... .......... .......... .......... .......... 48% 45.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177202:8859450K .......... .......... .......... .......... .......... 48% 35.3M 2m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177344:8866550K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177399:8869300K .......... .......... .......... .......... .......... 48% 75.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177509:8874800K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177559:8877300K .......... .......... .......... .......... .......... 48% 25.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177583:8878500K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177660:8882350K .......... .......... .......... .......... .......... 48% 25.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177706:8884650K .......... .......... .......... .......... .......... 48% 45.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177802:8889450K .......... .......... .......... .......... .......... 48% 65.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177928:8895750K .......... .......... .......... .......... .......... 48% 45.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:177974:8898050K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178030:8900850K .......... .......... .......... .......... .......... 48% 65.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178069:8902800K .......... .......... .......... .......... .......... 48% 45.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178155:8907100K .......... .......... .......... .......... .......... 48% 45.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178181:8908400K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178232:8910950K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178295:8914100K .......... .......... .......... .......... .......... 48% 35.3M 2m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178440:8921350K .......... .......... .......... .......... .......... 49% 45.3M 2m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178502:8924450K .......... .......... .......... .......... .......... 49% 25.3M 2m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:178603:8929500K .......... .......... .......... .......... .......... 49% 45.3M 2m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:179189:8958800K .......... .......... .......... .......... .......... 49% 65.3M 2m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:179263:8962500K .......... .......... .......... .......... .......... 49% 65.3M 2m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:179719:8985300K .......... .......... .......... .......... .......... 49% 95.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180002:8999450K .......... .......... .......... .......... .......... 49% 25.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180032:9000950K .......... .......... .......... .......... .......... 49% 65.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180098:9004250K .......... .......... .......... .......... .......... 49% 45.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180157:9007200K .......... .......... .......... .......... .......... 49% 45.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180265:9012600K .......... .......... .......... .......... .......... 49% 35.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180418:9020250K .......... .......... .......... .......... .......... 49% 45.3M 2m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180614:9030050K .......... .......... .......... .......... .......... 49% 35.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180707:9034700K .......... .......... .......... .......... .......... 49% 45.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180717:9035200K .......... .......... .......... .......... .......... 49% 55.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180758:9037250K .......... .......... .......... .......... .......... 49% 45.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:180810:9039850K .......... .......... .......... .......... .......... 49% 65.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181103:9054500K .......... .......... .......... .......... .......... 49% 45.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181174:9058050K .......... .......... .......... .......... .......... 49% 35.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181283:9063500K .......... .......... .......... .......... .......... 49% 35.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181380:9068350K .......... .......... .......... .......... .......... 49% 35.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181410:9069850K .......... .......... .......... .......... .......... 49% 45.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181440:9071350K .......... .......... .......... .......... .......... 49% 35.3M 2m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181746:9086650K .......... .......... .......... .......... .......... 49% 45.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181807:9089700K .......... .......... .......... .......... .......... 49% 45.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181840:9091350K .......... .......... .......... .......... .......... 49% 45.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181912:9094950K .......... .......... .......... .......... .......... 49% 35.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181926:9095650K .......... .......... .......... .......... .......... 49% 35.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181960:9097350K .......... .......... .......... .......... .......... 49% 45.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:181982:9098450K .......... .......... .......... .......... .......... 50% 35.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182023:9100500K .......... .......... .......... .......... .......... 50% 35.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182394:9119050K .......... .......... .......... .......... .......... 50% 15.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182431:9120900K .......... .......... .......... .......... .......... 50% 35.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182491:9123900K .......... .......... .......... .......... .......... 50% 45.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182657:9132200K .......... .......... .......... .......... .......... 50% 25.3M 2m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182813:9140000K .......... .......... .......... .......... .......... 50% 35.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182820:9140350K .......... .......... .......... .......... .......... 50% 35.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182829:9140800K .......... .......... .......... .......... .......... 50% 35.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:182989:9148800K .......... .......... .......... .......... .......... 50% 25.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183033:9151000K .......... .......... .......... .......... .......... 50% 45.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183147:9156700K .......... .......... .......... .......... .......... 50% 45.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183218:9160250K .......... .......... .......... .......... .......... 50% 35.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183285:9163600K .......... .......... .......... .......... .......... 50% 35.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183724:9185550K .......... .......... .......... .......... .......... 50% 55.3M 2m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183874:9193050K .......... .......... .......... .......... .......... 50% 75.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183877:9193200K .......... .......... .......... .......... .......... 50% 45.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183905:9194600K .......... .......... .......... .......... .......... 50% 45.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:183965:9197600K .......... .......... .......... .......... .......... 50% 35.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:184015:9200100K .......... .......... .......... .......... .......... 50% 45.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:184191:9208900K .......... .......... .......... .......... .......... 50% 45.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:184393:9219000K .......... .......... .......... .......... .......... 50% 45.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:184489:9223800K .......... .......... .......... .......... .......... 50% 35.3M 2m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:184953:9247000K .......... .......... .......... .......... .......... 50% 35.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185020:9250350K .......... .......... .......... .......... .......... 50% 35.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185056:9252150K .......... .......... .......... .......... .......... 50% 35.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185063:9252500K .......... .......... .......... .......... .......... 50% 45.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185322:9265450K .......... .......... .......... .......... .......... 50% 35.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185522:9275450K .......... .......... .......... .......... .......... 50% 45.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185551:9276900K .......... .......... .......... .......... .......... 50% 45.3M 2m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185977:9298200K .......... .......... .......... .......... .......... 51% 65.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:185995:9299100K .......... .......... .......... .......... .......... 51% 45.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186161:9307400K .......... .......... .......... .......... .......... 51% 45.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186262:9312450K .......... .......... .......... .......... .......... 51% 15.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186361:9317400K .......... .......... .......... .......... .......... 51% 85.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186481:9323400K .......... .......... .......... .......... .......... 51% 35.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186504:9324550K .......... .......... .......... .......... .......... 51% 75.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186575:9328100K .......... .......... .......... .......... .......... 51% 45.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186628:9330750K .......... .......... .......... .......... .......... 51% 45.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186789:9338800K .......... .......... .......... .......... .......... 51% 45.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:186884:9343550K .......... .......... .......... .......... .......... 51% 45.3M 2m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:187113:9355000K .......... .......... .......... .......... .......... 51% 95.3M 2m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:187250:9361850K .......... .......... .......... .......... .......... 51% 45.3M 2m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:187311:9364900K .......... .......... .......... .......... .......... 51% 25.3M 2m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188222:9410450K .......... .......... .......... .......... .......... 51% 45.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188299:9414300K .......... .......... .......... .......... .......... 51% 45.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188369:9417800K .......... .......... .......... .......... .......... 51% 35.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188452:9421950K .......... .......... .......... .......... .......... 51% 65.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188519:9425300K .......... .......... .......... .......... .......... 51% 45.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188523:9425500K .......... .......... .......... .......... .......... 51% 35.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188593:9429000K .......... .......... .......... .......... .......... 51% 65.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188672:9432950K .......... .......... .......... .......... .......... 51% 25.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188783:9438500K .......... .......... .......... .......... .......... 51% 45.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:188852:9441950K .......... .......... .......... .......... .......... 51% 45.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:189084:9453550K .......... .......... .......... .......... .......... 51% 45.3M 2m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:189591:9478900K .......... .......... .......... .......... .......... 52% 45.3M 2m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:189762:9487450K .......... .......... .......... .......... .......... 52% 15.3M 2m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:189844:9491550K .......... .......... .......... .......... .......... 52% 45.3M 2m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:189851:9491900K .......... .......... .......... .......... .......... 52% 35.3M 2m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:189881:9493400K .......... .......... .......... .......... .......... 52% 55.3M 2m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:190021:9500400K .......... .......... .......... .......... .......... 52% 45.3M 2m39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:190349:9516800K .......... .......... .......... .......... .......... 52% 45.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:190618:9530250K .......... .......... .......... .......... .......... 52% 45.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:190986:9548650K .......... .......... .......... .......... .......... 52% 35.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191099:9554300K .......... .......... .......... .......... .......... 52% 65.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191143:9556500K .......... .......... .......... .......... .......... 52% 55.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191200:9559350K .......... .......... .......... .......... .......... 52% 25.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191267:9562700K .......... .......... .......... .......... .......... 52% 75.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191374:9568050K .......... .......... .......... .......... .......... 52% 55.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191418:9570250K .......... .......... .......... .......... .......... 52% 75.3M 2m38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191779:9588300K .......... .......... .......... .......... .......... 52% 45.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191879:9593300K .......... .......... .......... .......... .......... 52% 35.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:191951:9596900K .......... .......... .......... .......... .......... 52% 45.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192047:9601700K .......... .......... .......... .......... .......... 52% 35.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192076:9603150K .......... .......... .......... .......... .......... 52% 45.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192163:9607500K .......... .......... .......... .......... .......... 52% 75.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192212:9609950K .......... .......... .......... .......... .......... 52% 55.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192299:9614300K .......... .......... .......... .......... .......... 52% 45.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192458:9622250K .......... .......... .......... .......... .......... 52% 35.3M 2m37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192605:9629600K .......... .......... .......... .......... .......... 52% 45.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192646:9631650K .......... .......... .......... .......... .......... 52% 65.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192654:9632050K .......... .......... .......... .......... .......... 52% 45.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192859:9642300K .......... .......... .......... .......... .......... 52% 55.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192870:9642850K .......... .......... .......... .......... .......... 52% 45.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192889:9643800K .......... .......... .......... .......... .......... 53% 35.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192975:9648100K .......... .......... .......... .......... .......... 53% 35.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:192984:9648550K .......... .......... .......... .......... .......... 53% 45.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:193000:9649350K .......... .......... .......... .......... .......... 53% 45.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:193254:9662050K .......... .......... .......... .......... .......... 53% 45.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:193533:9676000K .......... .......... .......... .......... .......... 53% 35.3M 2m36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:193851:9691900K .......... .......... .......... .......... .......... 53% 35.3M 2m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:193996:9699150K .......... .......... .......... .......... .......... 53% 45.3M 2m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:194233:9711000K .......... .......... .......... .......... .......... 53% 45.3M 2m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:194258:9712250K .......... .......... .......... .......... .......... 53% 35.3M 2m35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:194937:9746200K .......... .......... .......... .......... .......... 53% 55.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195068:9752750K .......... .......... .......... .......... .......... 53% 25.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195129:9755800K .......... .......... .......... .......... .......... 53% 65.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195190:9758850K .......... .......... .......... .......... .......... 53% 45.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195373:9768000K .......... .......... .......... .......... .......... 53% 75.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195377:9768200K .......... .......... .......... .......... .......... 53% 35.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195443:9771500K .......... .......... .......... .......... .......... 53% 35.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195547:9776700K .......... .......... .......... .......... .......... 53% 55.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195558:9777250K .......... .......... .......... .......... .......... 53% 35.3M 2m34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195879:9793300K .......... .......... .......... .......... .......... 53% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:195881:9793400K .......... .......... .......... .......... .......... 53% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196147:9806700K .......... .......... .......... .......... .......... 53% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196356:9817150K .......... .......... .......... .......... .......... 53% 95.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196468:9822750K .......... .......... .......... .......... .......... 53% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196485:9823600K .......... .......... .......... .......... .......... 53% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196587:9828700K .......... .......... .......... .......... .......... 54% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196654:9832050K .......... .......... .......... .......... .......... 54% 45.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196680:9833350K .......... .......... .......... .......... .......... 54% 75.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196795:9839100K .......... .......... .......... .......... .......... 54% 35.3M 2m33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196841:9841400K .......... .......... .......... .......... .......... 54% 45.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196855:9842100K .......... .......... .......... .......... .......... 54% 45.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:196992:9848950K .......... .......... .......... .......... .......... 54% 25.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:197075:9853100K .......... .......... .......... .......... .......... 54% 35.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:197239:9861300K .......... .......... .......... .......... .......... 54% 75.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:197376:9868150K .......... .......... .......... .......... .......... 54% 35.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:197437:9871200K .......... .......... .......... .......... .......... 54% 45.3M 2m32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:197926:9895650K .......... .......... .......... .......... .......... 54% 75.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:197962:9897450K .......... .......... .......... .......... .......... 54% 25.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198068:9902750K .......... .......... .......... .......... .......... 54% 55.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198403:9919500K .......... .......... .......... .......... .......... 54% 25.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198474:9923050K .......... .......... .......... .......... .......... 54% 25.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198480:9923350K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198539:9926300K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198585:9928600K .......... .......... .......... .......... .......... 54% 25.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198616:9930150K .......... .......... .......... .......... .......... 54% 45.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198729:9935800K .......... .......... .......... .......... .......... 54% 75.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198756:9937150K .......... .......... .......... .......... .......... 54% 55.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198775:9938100K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198787:9938700K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198798:9939250K .......... .......... .......... .......... .......... 54% 55.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198806:9939650K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198863:9942500K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:198914:9945050K .......... .......... .......... .......... .......... 54% 35.3M 2m31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199027:9950700K .......... .......... .......... .......... .......... 54% 35.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199173:9958000K .......... .......... .......... .......... .......... 54% 45.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199349:9966800K .......... .......... .......... .......... .......... 54% 35.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199435:9971100K .......... .......... .......... .......... .......... 54% 65.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199515:9975100K .......... .......... .......... .......... .......... 54% 45.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199587:9978700K .......... .......... .......... .......... .......... 54% 45.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199779:9988300K .......... .......... .......... .......... .......... 54% 45.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:199915:9995100K .......... .......... .......... .......... .......... 54% 65.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200005:9999600K .......... .......... .......... .......... .......... 54% 85.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200023:10000500K .......... .......... .......... .......... .......... 54% 35.3M 2m30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200121:10005400K .......... .......... .......... .......... .......... 54% 35.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200144:10006550K .......... .......... .......... .......... .......... 54% 45.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200480:10023350K .......... .......... .......... .......... .......... 55% 35.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200524:10025550K .......... .......... .......... .......... .......... 55% 35.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:200642:10031450K .......... .......... .......... .......... .......... 55% 95.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:201014:10050050K .......... .......... .......... .......... .......... 55% 45.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:201069:10052800K .......... .......... .......... .......... .......... 55% 35.3M 2m29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202036:10101150K .......... .......... .......... .......... .......... 55% 45.3M 2m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202201:10109400K .......... .......... .......... .......... .......... 55% 85.3M 2m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202278:10113250K .......... .......... .......... .......... .......... 55% 45.3M 2m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202363:10117500K .......... .......... .......... .......... .......... 55% 45.3M 2m28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202473:10123000K .......... .......... .......... .......... .......... 55% 15.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202540:10126350K .......... .......... .......... .......... .......... 55% 45.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202711:10134900K .......... .......... .......... .......... .......... 55% 45.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202735:10136100K .......... .......... .......... .......... .......... 55% 55.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202798:10139250K .......... .......... .......... .......... .......... 55% 45.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202801:10139400K .......... .......... .......... .......... .......... 55% 35.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202834:10141050K .......... .......... .......... .......... .......... 55% 55.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202847:10141700K .......... .......... .......... .......... .......... 55% 55.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:202919:10145300K .......... .......... .......... .......... .......... 55% 25.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203079:10153300K .......... .......... .......... .......... .......... 55% 25.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203207:10159700K .......... .......... .......... .......... .......... 55% 45.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203225:10160600K .......... .......... .......... .......... .......... 55% 35.3M 2m27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203585:10178600K .......... .......... .......... .......... .......... 55% 25.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203660:10182350K .......... .......... .......... .......... .......... 55% 55.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203664:10182550K .......... .......... .......... .......... .......... 55% 45.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:203957:10197200K .......... .......... .......... .......... .......... 56% 45.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204069:10202800K .......... .......... .......... .......... .......... 56% 65.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204166:10207650K .......... .......... .......... .......... .......... 56% 75.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204463:10222500K .......... .......... .......... .......... .......... 56% 35.3M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204558:10227250K .......... .......... .......... .......... .......... 56% 5.36M 2m26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204640:10231350K .......... .......... .......... .......... .......... 56% 35.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204683:10233500K .......... .......... .......... .......... .......... 56% 55.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204704:10234550K .......... .......... .......... .......... .......... 56% 45.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:204803:10239500K .......... .......... .......... .......... .......... 56% 35.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205064:10252550K .......... .......... .......... .......... .......... 56% 45.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205247:10261700K .......... .......... .......... .......... .......... 56% 35.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205266:10262650K .......... .......... .......... .......... .......... 56% 35.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205395:10269100K .......... .......... .......... .......... .......... 56% 85.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205463:10272500K .......... .......... .......... .......... .......... 56% 15.3M 2m25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205794:10289050K .......... .......... .......... .......... .......... 56% 45.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205819:10290300K .......... .......... .......... .......... .......... 56% 45.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205974:10298050K .......... .......... .......... .......... .......... 56% 45.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:205995:10299100K .......... .......... .......... .......... .......... 56% 5.31M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206171:10307900K .......... .......... .......... .......... .......... 56% 45.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206425:10320600K .......... .......... .......... .......... .......... 56% 55.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206455:10322100K .......... .......... .......... .......... .......... 56% 35.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206499:10324300K .......... .......... .......... .......... .......... 56% 45.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206650:10331850K .......... .......... .......... .......... .......... 56% 45.3M 2m24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206880:10343350K .......... .......... .......... .......... .......... 56% 35.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:206984:10348550K .......... .......... .......... .......... .......... 56% 35.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207184:10358550K .......... .......... .......... .......... .......... 56% 35.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207366:10367650K .......... .......... .......... .......... .......... 56% 35.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207369:10367800K .......... .......... .......... .......... .......... 56% 35.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207429:10370800K .......... .......... .......... .......... .......... 56% 55.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207545:10376600K .......... .......... .......... .......... .......... 57% 45.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207590:10378850K .......... .......... .......... .......... .......... 57% 55.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207669:10382800K .......... .......... .......... .......... .......... 57% 35.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207678:10383250K .......... .......... .......... .......... .......... 57% 45.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207788:10388750K .......... .......... .......... .......... .......... 57% 45.3M 2m23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207936:10396150K .......... .......... .......... .......... .......... 57% 45.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:207940:10396350K .......... .......... .......... .......... .......... 57% 45.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:208179:10408300K .......... .......... .......... .......... .......... 57% 45.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:208256:10412150K .......... .......... .......... .......... .......... 57% 45.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:208372:10417950K .......... .......... .......... .......... .......... 57% 55.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:208465:10422600K .......... .......... .......... .......... .......... 57% 35.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:208627:10430700K .......... .......... .......... .......... .......... 57% 55.3M 2m22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:209037:10451200K .......... .......... .......... .......... .......... 57% 35.3M 2m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:209580:10478350K .......... .......... .......... .......... .......... 57% 25.3M 2m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:209785:10488600K .......... .......... .......... .......... .......... 57% 25.3M 2m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:209971:10497900K .......... .......... .......... .......... .......... 57% 45.3M 2m21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210026:10500650K .......... .......... .......... .......... .......... 57% 35.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210088:10503750K .......... .......... .......... .......... .......... 57% 55.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210167:10507700K .......... .......... .......... .......... .......... 57% 65.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210393:10519000K .......... .......... .......... .......... .......... 57% 45.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210398:10519250K .......... .......... .......... .......... .......... 57% 45.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210410:10519850K .......... .......... .......... .......... .......... 57% 45.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210490:10523850K .......... .......... .......... .......... .......... 57% 45.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210560:10527350K .......... .......... .......... .......... .......... 57% 35.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210596:10529150K .......... .......... .......... .......... .......... 57% 45.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210754:10537050K .......... .......... .......... .......... .......... 57% 95.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:210870:10542850K .......... .......... .......... .......... .......... 57% 45.3M 2m20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211156:10557150K .......... .......... .......... .......... .......... 58% 55.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211175:10558100K .......... .......... .......... .......... .......... 58% 55.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211188:10558750K .......... .......... .......... .......... .......... 58% 25.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211353:10567000K .......... .......... .......... .......... .......... 58% 75.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211377:10568200K .......... .......... .......... .......... .......... 58% 25.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211599:10579300K .......... .......... .......... .......... .......... 58% 65.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211674:10583050K .......... .......... .......... .......... .......... 58% 45.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211675:10583100K .......... .......... .......... .......... .......... 58% 25.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211682:10583450K .......... .......... .......... .......... .......... 58% 25.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211718:10585250K .......... .......... .......... .......... .......... 58% 35.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211816:10590150K .......... .......... .......... .......... .......... 58% 45.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211858:10592250K .......... .......... .......... .......... .......... 58% 35.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211886:10593650K .......... .......... .......... .......... .......... 58% 25.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:211904:10594550K .......... .......... .......... .......... .......... 58% 35.3M 2m19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212380:10618350K .......... .......... .......... .......... .......... 58% 55.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212601:10629400K .......... .......... .......... .......... .......... 58% 45.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212695:10634100K .......... .......... .......... .......... .......... 58% 45.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212734:10636050K .......... .......... .......... .......... .......... 58% 45.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212932:10645950K .......... .......... .......... .......... .......... 58% 35.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212944:10646550K .......... .......... .......... .......... .......... 58% 65.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:212951:10646900K .......... .......... .......... .......... .......... 58% 45.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:213210:10659850K .......... .......... .......... .......... .......... 58% 35.3M 2m18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:213385:10668600K .......... .......... .......... .......... .......... 58% 55.3M 2m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:213773:10688000K .......... .......... .......... .......... .......... 58% 35.3M 2m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:213984:10698550K .......... .......... .......... .......... .......... 58% 55.3M 2m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:214281:10713400K .......... .......... .......... .......... .......... 58% 65.3M 2m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:214285:10713600K .......... .......... .......... .......... .......... 58% 35.3M 2m17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:214658:10732250K .......... .......... .......... .......... .......... 58% 45.3M 2m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:214775:10738100K .......... .......... .......... .......... .......... 59% 55.3M 2m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:214825:10740600K .......... .......... .......... .......... .......... 59% 65.3M 2m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:215308:10764750K .......... .......... .......... .......... .......... 59% 75.3M 2m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:215504:10774550K .......... .......... .......... .......... .......... 59% 45.3M 2m16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:215583:10778500K .......... .......... .......... .......... .......... 59% 65.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:215928:10795750K .......... .......... .......... .......... .......... 59% 45.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216075:10803100K .......... .......... .......... .......... .......... 59% 45.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216253:10812000K .......... .......... .......... .......... .......... 59% 45.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216504:10824550K .......... .......... .......... .......... .......... 59% 45.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216582:10828450K .......... .......... .......... .......... .......... 59% 45.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216604:10829550K .......... .......... .......... .......... .......... 59% 45.3M 2m15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216623:10830500K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:216639:10831300K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217041:10851400K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217088:10853750K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217155:10857100K .......... .......... .......... .......... .......... 59% 35.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217217:10860200K .......... .......... .......... .......... .......... 59% 55.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217291:10863900K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217583:10878500K .......... .......... .......... .......... .......... 59% 35.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217594:10879050K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217656:10882150K .......... .......... .......... .......... .......... 59% 45.3M 2m14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:217915:10895100K .......... .......... .......... .......... .......... 59% 45.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218118:10905250K .......... .......... .......... .......... .......... 59% 75.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218126:10905650K .......... .......... .......... .......... .......... 59% 45.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218204:10909550K .......... .......... .......... .......... .......... 59% 45.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218353:10917000K .......... .......... .......... .......... .......... 59% 45.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218604:10929550K .......... .......... .......... .......... .......... 60% 35.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218648:10931750K .......... .......... .......... .......... .......... 60% 45.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:218745:10936600K .......... .......... .......... .......... .......... 60% 35.3M 2m13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219051:10951900K .......... .......... .......... .......... .......... 60% 15.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219079:10953300K .......... .......... .......... .......... .......... 60% 35.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219101:10954400K .......... .......... .......... .......... .......... 60% 65.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219164:10957550K .......... .......... .......... .......... .......... 60% 45.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219255:10962100K .......... .......... .......... .......... .......... 60% 35.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219316:10965150K .......... .......... .......... .......... .......... 60% 45.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219338:10966250K .......... .......... .......... .......... .......... 60% 45.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219575:10978100K .......... .......... .......... .......... .......... 60% 55.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219697:10984200K .......... .......... .......... .......... .......... 60% 85.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219725:10985600K .......... .......... .......... .......... .......... 60% 55.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219782:10988450K .......... .......... .......... .......... .......... 60% 55.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:219809:10989800K .......... .......... .......... .......... .......... 60% 35.3M 2m12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:220043:11001500K .......... .......... .......... .......... .......... 60% 85.3M 2m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:220070:11002850K .......... .......... .......... .......... .......... 60% 35.3M 2m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:220119:11005300K .......... .......... .......... .......... .......... 60% 35.3M 2m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:220407:11019700K .......... .......... .......... .......... .......... 60% 35.3M 2m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:220642:11031450K .......... .......... .......... .......... .......... 60% 45.3M 2m11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221164:11057550K .......... .......... .......... .......... .......... 60% 25.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221223:11060500K .......... .......... .......... .......... .......... 60% 45.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221234:11061050K .......... .......... .......... .......... .......... 60% 35.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221333:11066000K .......... .......... .......... .......... .......... 60% 45.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221470:11072850K .......... .......... .......... .......... .......... 60% 55.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221533:11076000K .......... .......... .......... .......... .......... 60% 65.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221595:11079100K .......... .......... .......... .......... .......... 60% 35.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:221757:11087200K .......... .......... .......... .......... .......... 60% 45.3M 2m10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222020:11100350K .......... .......... .......... .......... .......... 61% 55.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222026:11100650K .......... .......... .......... .......... .......... 61% 35.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222453:11122000K .......... .......... .......... .......... .......... 61% 45.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222583:11128500K .......... .......... .......... .......... .......... 61% 35.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222653:11132000K .......... .......... .......... .......... .......... 61% 65.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222694:11134050K .......... .......... .......... .......... .......... 61% 35.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222884:11143550K .......... .......... .......... .......... .......... 61% 45.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:222946:11146650K .......... .......... .......... .......... .......... 61% 35.3M 2m9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223279:11163300K .......... .......... .......... .......... .......... 61% 45.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223338:11166250K .......... .......... .......... .......... .......... 61% 35.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223411:11169900K .......... .......... .......... .......... .......... 61% 55.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223486:11173650K .......... .......... .......... .......... .......... 61% 25.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223564:11177550K .......... .......... .......... .......... .......... 61% 35.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223704:11184550K .......... .......... .......... .......... .......... 61% 35.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223790:11188850K .......... .......... .......... .......... .......... 61% 45.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223802:11189450K .......... .......... .......... .......... .......... 61% 75.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:223898:11194250K .......... .......... .......... .......... .......... 61% 35.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224131:11205900K .......... .......... .......... .......... .......... 61% 45.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224135:11206100K .......... .......... .......... .......... .......... 61% 45.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224161:11207400K .......... .......... .......... .......... .......... 61% 35.3M 2m8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224504:11224550K .......... .......... .......... .......... .......... 61% 35.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224593:11229000K .......... .......... .......... .......... .......... 61% 85.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224597:11229200K .......... .......... .......... .......... .......... 61% 35.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224608:11229750K .......... .......... .......... .......... .......... 61% 45.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224640:11231350K .......... .......... .......... .......... .......... 61% 35.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224664:11232550K .......... .......... .......... .......... .......... 61% 15.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:224798:11239250K .......... .......... .......... .......... .......... 61% 55.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225081:11253400K .......... .......... .......... .......... .......... 61% 45.3M 2m7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225671:11282900K .......... .......... .......... .......... .......... 62% 55.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225686:11283650K .......... .......... .......... .......... .......... 62% 45.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225753:11287000K .......... .......... .......... .......... .......... 62% 35.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225851:11291900K .......... .......... .......... .......... .......... 62% 45.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225895:11294100K .......... .......... .......... .......... .......... 62% 35.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225941:11296400K .......... .......... .......... .......... .......... 62% 45.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:225983:11298500K .......... .......... .......... .......... .......... 62% 35.3M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:226442:11321450K .......... .......... .......... .......... .......... 62% 5.38M 2m6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:226679:11333300K .......... .......... .......... .......... .......... 62% 35.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:226722:11335450K .......... .......... .......... .......... .......... 62% 55.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:226872:11342950K .......... .......... .......... .......... .......... 62% 75.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227065:11352600K .......... .......... .......... .......... .......... 62% 55.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227083:11353500K .......... .......... .......... .......... .......... 62% 45.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227261:11362400K .......... .......... .......... .......... .......... 62% 45.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227263:11362500K .......... .......... .......... .......... .......... 62% 45.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227458:11372250K .......... .......... .......... .......... .......... 62% 45.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227511:11374900K .......... .......... .......... .......... .......... 62% 45.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227529:11375800K .......... .......... .......... .......... .......... 62% 25.3M 2m5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:227776:11388150K .......... .......... .......... .......... .......... 62% 45.3M 2m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228273:11413000K .......... .......... .......... .......... .......... 62% 75.3M 2m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228315:11415100K .......... .......... .......... .......... .......... 62% 35.3M 2m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228383:11418500K .......... .......... .......... .......... .......... 62% 45.3M 2m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228444:11421550K .......... .......... .......... .......... .......... 62% 45.3M 2m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228479:11423300K .......... .......... .......... .......... .......... 62% 45.3M 2m4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228677:11433200K .......... .......... .......... .......... .......... 62% 35.3M 2m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:228787:11438700K .......... .......... .......... .......... .......... 62% 55.3M 2m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:229086:11453650K .......... .......... .......... .......... .......... 62% 45.3M 2m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:229310:11464850K .......... .......... .......... .......... .......... 63% 55.3M 2m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:229330:11465850K .......... .......... .......... .......... .......... 63% 35.3M 2m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:229340:11466350K .......... .......... .......... .......... .......... 63% 65.3M 2m3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:229922:11495450K .......... .......... .......... .......... .......... 63% 35.3M 2m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:230098:11504250K .......... .......... .......... .......... .......... 63% 45.3M 2m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:230110:11504850K .......... .......... .......... .......... .......... 63% 85.3M 2m2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:230905:11544600K .......... .......... .......... .......... .......... 63% 95.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231047:11551700K .......... .......... .......... .......... .......... 63% 45.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231343:11566500K .......... .......... .......... .......... .......... 63% 35.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231658:11582250K .......... .......... .......... .......... .......... 63% 45.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231738:11586250K .......... .......... .......... .......... .......... 63% 35.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231841:11591400K .......... .......... .......... .......... .......... 63% 65.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231846:11591650K .......... .......... .......... .......... .......... 63% 45.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231864:11592550K .......... .......... .......... .......... .......... 63% 65.3M 2m1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:231931:11595900K .......... .......... .......... .......... .......... 63% 95.3M 2m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:232276:11613150K .......... .......... .......... .......... .......... 63% 45.3M 2m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:232279:11613300K .......... .......... .......... .......... .......... 63% 45.3M 2m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:232386:11618650K .......... .......... .......... .......... .......... 63% 45.3M 2m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:232599:11629300K .......... .......... .......... .......... .......... 63% 65.3M 2m0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:233229:11660800K .......... .......... .......... .......... .......... 64% 65.3M 1m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:233496:11674150K .......... .......... .......... .......... .......... 64% 35.3M 1m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:233529:11675800K .......... .......... .......... .......... .......... 64% 45.3M 1m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:233540:11676350K .......... .......... .......... .......... .......... 64% 45.3M 1m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:233709:11684800K .......... .......... .......... .......... .......... 64% 55.3M 1m59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234076:11703150K .......... .......... .......... .......... .......... 64% 45.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234168:11707750K .......... .......... .......... .......... .......... 64% 35.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234179:11708300K .......... .......... .......... .......... .......... 64% 35.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234251:11711900K .......... .......... .......... .......... .......... 64% 55.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234304:11714550K .......... .......... .......... .......... .......... 64% 35.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234319:11715300K .......... .......... .......... .......... .......... 64% 45.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234768:11737750K .......... .......... .......... .......... .......... 64% 35.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234868:11742750K .......... .......... .......... .......... .......... 64% 45.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:234988:11748750K .......... .......... .......... .......... .......... 64% 65.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235037:11751200K .......... .......... .......... .......... .......... 64% 55.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235038:11751250K .......... .......... .......... .......... .......... 64% 35.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235110:11754850K .......... .......... .......... .......... .......... 64% 45.3M 1m58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235476:11773150K .......... .......... .......... .......... .......... 64% 35.3M 1m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235491:11773900K .......... .......... .......... .......... .......... 64% 35.3M 1m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235744:11786550K .......... .......... .......... .......... .......... 64% 45.3M 1m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235796:11789150K .......... .......... .......... .......... .......... 64% 55.3M 1m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:235805:11789600K .......... .......... .......... .......... .......... 64% 25.3M 1m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236280:11813350K .......... .......... .......... .......... .......... 64% 35.3M 1m57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236398:11819250K .......... .......... .......... .......... .......... 64% 75.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236448:11821750K .......... .......... .......... .......... .......... 64% 25.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236456:11822150K .......... .......... .......... .......... .......... 64% 45.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236479:11823300K .......... .......... .......... .......... .......... 64% 55.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236532:11825950K .......... .......... .......... .......... .......... 64% 55.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236797:11839200K .......... .......... .......... .......... .......... 65% 45.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236914:11845050K .......... .......... .......... .......... .......... 65% 35.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236916:11845150K .......... .......... .......... .......... .......... 65% 45.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:236923:11845500K .......... .......... .......... .......... .......... 65% 45.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237116:11855150K .......... .......... .......... .......... .......... 65% 45.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237392:11868950K .......... .......... .......... .......... .......... 65% 45.3M 1m56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237499:11874300K .......... .......... .......... .......... .......... 65% 35.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237687:11883700K .......... .......... .......... .......... .......... 65% 85.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237775:11888100K .......... .......... .......... .......... .......... 65% 45.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237778:11888250K .......... .......... .......... .......... .......... 65% 45.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:237983:11898500K .......... .......... .......... .......... .......... 65% 55.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238020:11900350K .......... .......... .......... .......... .......... 65% 45.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238246:11911650K .......... .......... .......... .......... .......... 65% 55.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238455:11922100K .......... .......... .......... .......... .......... 65% 35.3M 1m55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238640:11931350K .......... .......... .......... .......... .......... 65% 45.3M 1m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238679:11933300K .......... .......... .......... .......... .......... 65% 45.3M 1m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238812:11939950K .......... .......... .......... .......... .......... 65% 45.3M 1m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238826:11940650K .......... .......... .......... .......... .......... 65% 45.3M 1m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:238884:11943550K .......... .......... .......... .......... .......... 65% 45.3M 1m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:239238:11961250K .......... .......... .......... .......... .......... 65% 75.3M 1m54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:239623:11980500K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:239667:11982700K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:239744:11986550K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:239751:11986900K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:239823:11990500K .......... .......... .......... .......... .......... 65% 35.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240042:12001450K .......... .......... .......... .......... .......... 65% 95.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240091:12003900K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240134:12006050K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240164:12007550K .......... .......... .......... .......... .......... 65% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240209:12009800K .......... .......... .......... .......... .......... 66% 35.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240352:12016950K .......... .......... .......... .......... .......... 66% 15.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240540:12026350K .......... .......... .......... .......... .......... 66% 45.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240597:12029200K .......... .......... .......... .......... .......... 66% 35.3M 1m53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:240741:12036400K .......... .......... .......... .......... .......... 66% 45.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:241086:12053650K .......... .......... .......... .......... .......... 66% 35.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:241113:12055000K .......... .......... .......... .......... .......... 66% 35.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:241307:12064700K .......... .......... .......... .......... .......... 66% 45.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:241311:12064900K .......... .......... .......... .......... .......... 66% 95.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:241332:12065950K .......... .......... .......... .......... .......... 66% 45.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:241336:12066150K .......... .......... .......... .......... .......... 66% 55.3M 1m52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:242284:12113550K .......... .......... .......... .......... .......... 66% 45.3M 1m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:242755:12137100K .......... .......... .......... .......... .......... 66% 45.3M 1m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:242851:12141900K .......... .......... .......... .......... .......... 66% 45.3M 1m51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243038:12151250K .......... .......... .......... .......... .......... 66% 45.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243100:12154350K .......... .......... .......... .......... .......... 66% 65.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243203:12159500K .......... .......... .......... .......... .......... 66% 45.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243217:12160200K .......... .......... .......... .......... .......... 66% 45.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243229:12160800K .......... .......... .......... .......... .......... 66% 45.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243351:12166900K .......... .......... .......... .......... .......... 66% 45.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243372:12167950K .......... .......... .......... .......... .......... 66% 45.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:243976:12198150K .......... .......... .......... .......... .......... 67% 35.3M 1m50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244099:12204300K .......... .......... .......... .......... .......... 67% 35.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244110:12204850K .......... .......... .......... .......... .......... 67% 35.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244206:12209650K .......... .......... .......... .......... .......... 67% 15.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244312:12214950K .......... .......... .......... .......... .......... 67% 55.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244503:12224500K .......... .......... .......... .......... .......... 67% 35.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244548:12226750K .......... .......... .......... .......... .......... 67% 65.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244805:12239600K .......... .......... .......... .......... .......... 67% 45.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244832:12240950K .......... .......... .......... .......... .......... 67% 35.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:244993:12249000K .......... .......... .......... .......... .......... 67% 45.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245043:12251500K .......... .......... .......... .......... .......... 67% 45.3M 1m49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245136:12256150K .......... .......... .......... .......... .......... 67% 25.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245190:12258850K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245212:12259950K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245252:12261950K .......... .......... .......... .......... .......... 67% 35.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245289:12263800K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245324:12265550K .......... .......... .......... .......... .......... 67% 85.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245376:12268150K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245401:12269400K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245502:12274450K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245544:12276550K .......... .......... .......... .......... .......... 67% 75.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245585:12278600K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245728:12285750K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245792:12288950K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:245943:12296500K .......... .......... .......... .......... .......... 67% 45.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:246138:12306250K .......... .......... .......... .......... .......... 67% 55.3M 1m48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:246196:12309150K .......... .......... .......... .......... .......... 67% 45.3M 1m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:246262:12312450K .......... .......... .......... .......... .......... 67% 45.3M 1m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:246304:12314550K .......... .......... .......... .......... .......... 67% 35.3M 1m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:246816:12340150K .......... .......... .......... .......... .......... 67% 45.3M 1m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:246877:12343200K .......... .......... .......... .......... .......... 67% 45.3M 1m47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:247342:12366450K .......... .......... .......... .......... .......... 67% 65.3M 1m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:247597:12379200K .......... .......... .......... .......... .......... 68% 45.3M 1m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:247812:12389950K .......... .......... .......... .......... .......... 68% 45.3M 1m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:247968:12397750K .......... .......... .......... .......... .......... 68% 45.3M 1m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248173:12408000K .......... .......... .......... .......... .......... 68% 45.3M 1m46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248463:12422500K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248528:12425750K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248603:12429500K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248605:12429600K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248675:12433100K .......... .......... .......... .......... .......... 68% 25.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:248936:12446150K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:249054:12452050K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:249092:12453950K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:249169:12457800K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:249236:12461150K .......... .......... .......... .......... .......... 68% 45.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:249443:12471500K .......... .......... .......... .......... .......... 68% 35.3M 1m45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:249885:12493600K .......... .......... .......... .......... .......... 68% 45.3M 1m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250007:12499700K .......... .......... .......... .......... .......... 68% 45.3M 1m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250012:12499950K .......... .......... .......... .......... .......... 68% 45.3M 1m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250070:12502850K .......... .......... .......... .......... .......... 68% 75.3M 1m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250251:12511900K .......... .......... .......... .......... .......... 68% 35.3M 1m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250322:12515450K .......... .......... .......... .......... .......... 68% 45.3M 1m44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250532:12525950K .......... .......... .......... .......... .......... 68% 25.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250586:12528650K .......... .......... .......... .......... .......... 68% 45.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250635:12531100K .......... .......... .......... .......... .......... 68% 55.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250730:12535850K .......... .......... .......... .......... .......... 68% 35.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250843:12541500K .......... .......... .......... .......... .......... 68% 45.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250846:12541650K .......... .......... .......... .......... .......... 68% 75.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:250968:12547750K .......... .......... .......... .......... .......... 68% 45.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251076:12553150K .......... .......... .......... .......... .......... 68% 45.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251130:12555850K .......... .......... .......... .......... .......... 69% 35.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251190:12558850K .......... .......... .......... .......... .......... 69% 45.3M 1m43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251625:12580600K .......... .......... .......... .......... .......... 69% 65.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251721:12585400K .......... .......... .......... .......... .......... 69% 45.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251737:12586200K .......... .......... .......... .......... .......... 69% 45.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:251833:12591000K .......... .......... .......... .......... .......... 69% 45.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252010:12599850K .......... .......... .......... .......... .......... 69% 45.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252153:12607000K .......... .......... .......... .......... .......... 69% 55.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252186:12608650K .......... .......... .......... .......... .......... 69% 35.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252355:12617100K .......... .......... .......... .......... .......... 69% 35.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252609:12629800K .......... .......... .......... .......... .......... 69% 45.3M 1m42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252729:12635800K .......... .......... .......... .......... .......... 69% 45.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252759:12637300K .......... .......... .......... .......... .......... 69% 65.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:252875:12643100K .......... .......... .......... .......... .......... 69% 35.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:253146:12656650K .......... .......... .......... .......... .......... 69% 25.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:253249:12661800K .......... .......... .......... .......... .......... 69% 25.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:253371:12667900K .......... .......... .......... .......... .......... 69% 45.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:253444:12671550K .......... .......... .......... .......... .......... 69% 35.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:253614:12680050K .......... .......... .......... .......... .......... 69% 55.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:253633:12681000K .......... .......... .......... .......... .......... 69% 55.3M 1m41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254122:12705450K .......... .......... .......... .......... .......... 69% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254156:12707150K .......... .......... .......... .......... .......... 69% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254182:12708450K .......... .......... .......... .......... .......... 69% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254276:12713150K .......... .......... .......... .......... .......... 69% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254285:12713600K .......... .......... .......... .......... .......... 69% 65.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254319:12715300K .......... .......... .......... .......... .......... 69% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254355:12717100K .......... .......... .......... .......... .......... 69% 25.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254489:12723800K .......... .......... .......... .......... .......... 69% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254802:12739450K .......... .......... .......... .......... .......... 70% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254872:12742950K .......... .......... .......... .......... .......... 70% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:254945:12746600K .......... .......... .......... .......... .......... 70% 45.3M 1m40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:255244:12761550K .......... .......... .......... .......... .......... 70% 35.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:255482:12773450K .......... .......... .......... .......... .......... 70% 45.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:255521:12775400K .......... .......... .......... .......... .......... 70% 35.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:255638:12781250K .......... .......... .......... .......... .......... 70% 45.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:255695:12784100K .......... .......... .......... .......... .......... 70% 35.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:255774:12788050K .......... .......... .......... .......... .......... 70% 45.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:256013:12800000K .......... .......... .......... .......... .......... 70% 35.3M 99s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:256077:12803200K .......... .......... .......... .......... .......... 70% 75.3M 98s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:256105:12804600K .......... .......... .......... .......... .......... 70% 35.3M 98s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:256560:12827350K .......... .......... .......... .......... .......... 70% 25.3M 98s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:256969:12847800K .......... .......... .......... .......... .......... 70% 35.3M 98s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257062:12852450K .......... .......... .......... .......... .......... 70% 45.3M 98s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257143:12856500K .......... .......... .......... .......... .......... 70% 15.3M 98s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257208:12859750K .......... .......... .......... .......... .......... 70% 35.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257213:12860000K .......... .......... .......... .......... .......... 70% 45.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257368:12867750K .......... .......... .......... .......... .......... 70% 55.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257399:12869300K .......... .......... .......... .......... .......... 70% 65.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257522:12875450K .......... .......... .......... .......... .......... 70% 45.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257557:12877200K .......... .......... .......... .......... .......... 70% 35.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257571:12877900K .......... .......... .......... .......... .......... 70% 35.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257749:12886800K .......... .......... .......... .......... .......... 70% 35.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257818:12890250K .......... .......... .......... .......... .......... 70% 55.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257880:12893350K .......... .......... .......... .......... .......... 70% 25.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:257985:12898600K .......... .......... .......... .......... .......... 70% 75.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258035:12901100K .......... .......... .......... .......... .......... 70% 45.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258039:12901300K .......... .......... .......... .......... .......... 70% 35.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258079:12903300K .......... .......... .......... .......... .......... 70% 45.3M 97s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258802:12939450K .......... .......... .......... .......... .......... 71% 25.3M 96s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258824:12940550K .......... .......... .......... .......... .......... 71% 25.3M 96s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258893:12944000K .......... .......... .......... .......... .......... 71% 65.3M 96s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:258909:12944800K .......... .......... .......... .......... .......... 71% 55.3M 96s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:259059:12952300K .......... .......... .......... .......... .......... 71% 35.3M 96s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:259320:12965350K .......... .......... .......... .......... .......... 71% 35.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:259541:12976400K .......... .......... .......... .......... .......... 71% 45.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:259819:12990300K .......... .......... .......... .......... .......... 71% 35.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260055:13002100K .......... .......... .......... .......... .......... 71% 65.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260131:13005900K .......... .......... .......... .......... .......... 71% 45.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260136:13006150K .......... .......... .......... .......... .......... 71% 25.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260200:13009350K .......... .......... .......... .......... .......... 71% 35.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260350:13016850K .......... .......... .......... .......... .......... 71% 45.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260388:13018750K .......... .......... .......... .......... .......... 71% 45.3M 95s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260424:13020550K .......... .......... .......... .......... .......... 71% 35.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260570:13027850K .......... .......... .......... .......... .......... 71% 55.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260825:13040600K .......... .......... .......... .......... .......... 71% 45.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:260969:13047800K .......... .......... .......... .......... .......... 71% 55.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261078:13053250K .......... .......... .......... .......... .......... 71% 45.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261140:13056350K .......... .......... .......... .......... .......... 71% 35.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261338:13066250K .......... .......... .......... .......... .......... 71% 55.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261375:13068100K .......... .......... .......... .......... .......... 71% 45.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261471:13072900K .......... .......... .......... .......... .......... 71% 75.3M 94s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261522:13075450K .......... .......... .......... .......... .......... 71% 55.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261548:13076750K .......... .......... .......... .......... .......... 71% 35.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261834:13091050K .......... .......... .......... .......... .......... 71% 45.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:261913:13095000K .......... .......... .......... .......... .......... 71% 35.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262107:13104700K .......... .......... .......... .......... .......... 72% 85.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262111:13104900K .......... .......... .......... .......... .......... 72% 45.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262131:13105900K .......... .......... .......... .......... .......... 72% 35.3M 93s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262686:13133650K .......... .......... .......... .......... .......... 72% 45.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262744:13136550K .......... .......... .......... .......... .......... 72% 45.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262783:13138500K .......... .......... .......... .......... .......... 72% 45.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262862:13142450K .......... .......... .......... .......... .......... 72% 75.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:262991:13148900K .......... .......... .......... .......... .......... 72% 15.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263049:13151800K .......... .......... .......... .......... .......... 72% 35.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263147:13156700K .......... .......... .......... .......... .......... 72% 45.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263310:13164850K .......... .......... .......... .......... .......... 72% 45.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263549:13176800K .......... .......... .......... .......... .......... 72% 35.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263631:13180900K .......... .......... .......... .......... .......... 72% 35.3M 92s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263735:13186100K .......... .......... .......... .......... .......... 72% 55.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:263948:13196750K .......... .......... .......... .......... .......... 72% 35.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264033:13201000K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264073:13203000K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264138:13206250K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264189:13208800K .......... .......... .......... .......... .......... 72% 25.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264278:13213250K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264285:13213600K .......... .......... .......... .......... .......... 72% 35.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264432:13220950K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264455:13222100K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264598:13229250K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264677:13233200K .......... .......... .......... .......... .......... 72% 45.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264775:13238100K .......... .......... .......... .......... .......... 72% 35.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264789:13238800K .......... .......... .......... .......... .......... 72% 45.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264798:13239250K .......... .......... .......... .......... .......... 72% 55.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264857:13242200K .......... .......... .......... .......... .......... 72% 65.3M 91s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264867:13242700K .......... .......... .......... .......... .......... 72% 45.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264918:13245250K .......... .......... .......... .......... .......... 72% 35.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:264983:13248500K .......... .......... .......... .......... .......... 72% 35.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:265068:13252750K .......... .......... .......... .......... .......... 72% 45.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:265141:13256400K .......... .......... .......... .......... .......... 72% 25.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:265313:13265000K .......... .......... .......... .......... .......... 72% 25.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:265562:13277450K .......... .......... .......... .......... .......... 72% 35.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:265671:13282900K .......... .......... .......... .......... .......... 73% 35.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:265748:13286750K .......... .......... .......... .......... .......... 73% 95.3M 90s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266030:13300850K .......... .......... .......... .......... .......... 73% 75.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266035:13301100K .......... .......... .......... .......... .......... 73% 35.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266055:13302100K .......... .......... .......... .......... .......... 73% 45.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266182:13308450K .......... .......... .......... .......... .......... 73% 45.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266304:13314550K .......... .......... .......... .......... .......... 73% 45.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266337:13316200K .......... .......... .......... .......... .......... 73% 95.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266558:13327250K .......... .......... .......... .......... .......... 73% 35.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266609:13329800K .......... .......... .......... .......... .......... 73% 35.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266641:13331400K .......... .......... .......... .......... .......... 73% 55.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266676:13333150K .......... .......... .......... .......... .......... 73% 45.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266713:13335000K .......... .......... .......... .......... .......... 73% 25.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:266993:13349000K .......... .......... .......... .......... .......... 73% 35.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267081:13353400K .......... .......... .......... .......... .......... 73% 75.3M 89s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267127:13355700K .......... .......... .......... .......... .......... 73% 25.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267230:13360850K .......... .......... .......... .......... .......... 73% 55.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267250:13361850K .......... .......... .......... .......... .......... 73% 35.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267303:13364500K .......... .......... .......... .......... .......... 73% 35.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267723:13385500K .......... .......... .......... .......... .......... 73% 25.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:267794:13389050K .......... .......... .......... .......... .......... 73% 85.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:268038:13401250K .......... .......... .......... .......... .......... 73% 45.3M 88s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:268325:13415600K .......... .......... .......... .......... .......... 73% 75.3M 87s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:268466:13422650K .......... .......... .......... .......... .......... 73% 25.3M 87s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:268532:13425950K .......... .......... .......... .......... .......... 73% 35.3M 87s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:268916:13445150K .......... .......... .......... .......... .......... 73% 15.3M 87s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269109:13454800K .......... .......... .......... .......... .......... 73% 55.3M 87s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269227:13460700K .......... .......... .......... .......... .......... 73% 35.3M 87s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269289:13463800K .......... .......... .......... .......... .......... 73% 25.3M 86s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269352:13466950K .......... .......... .......... .......... .......... 74% 45.3M 86s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269449:13471800K .......... .......... .......... .......... .......... 74% 55.3M 86s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269564:13477550K .......... .......... .......... .......... .......... 74% 45.3M 86s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:269783:13488500K .......... .......... .......... .......... .......... 74% 65.3M 86s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:270267:13512700K .......... .......... .......... .......... .......... 74% 45.3M 86s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:270486:13523650K .......... .......... .......... .......... .......... 74% 45.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:270506:13524650K .......... .......... .......... .......... .......... 74% 45.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:270652:13531950K .......... .......... .......... .......... .......... 74% 45.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:270687:13533700K .......... .......... .......... .......... .......... 74% 35.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:270775:13538100K .......... .......... .......... .......... .......... 74% 35.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271180:13558350K .......... .......... .......... .......... .......... 74% 45.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271256:13562150K .......... .......... .......... .......... .......... 74% 35.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271294:13564050K .......... .......... .......... .......... .......... 74% 45.3M 85s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271629:13580800K .......... .......... .......... .......... .......... 74% 35.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271679:13583300K .......... .......... .......... .......... .......... 74% 45.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271740:13586350K .......... .......... .......... .......... .......... 74% 55.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271831:13590900K .......... .......... .......... .......... .......... 74% 45.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271876:13593150K .......... .......... .......... .......... .......... 74% 45.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:271881:13593400K .......... .......... .......... .......... .......... 74% 35.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:272078:13603250K .......... .......... .......... .......... .......... 74% 45.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:272081:13603400K .......... .......... .......... .......... .......... 74% 55.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:272294:13614050K .......... .......... .......... .......... .......... 74% 65.3M 84s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:273029:13650800K .......... .......... .......... .......... .......... 75% 45.3M 83s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:273043:13651500K .......... .......... .......... .......... .......... 75% 45.3M 83s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:273124:13655550K .......... .......... .......... .......... .......... 75% 45.3M 83s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:273236:13661150K .......... .......... .......... .......... .......... 75% 75.3M 83s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:273341:13666400K .......... .......... .......... .......... .......... 75% 35.3M 83s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:273752:13686950K .......... .......... .......... .......... .......... 75% 45.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274186:13708650K .......... .......... .......... .......... .......... 75% 25.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274345:13716600K .......... .......... .......... .......... .......... 75% 65.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274578:13728250K .......... .......... .......... .......... .......... 75% 45.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274582:13728450K .......... .......... .......... .......... .......... 75% 75.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274628:13730750K .......... .......... .......... .......... .......... 75% 45.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274659:13732300K .......... .......... .......... .......... .......... 75% 35.3M 82s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274779:13738300K .......... .......... .......... .......... .......... 75% 25.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274878:13743250K .......... .......... .......... .......... .......... 75% 75.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274911:13744900K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:274919:13745300K .......... .......... .......... .......... .......... 75% 35.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275057:13752200K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275085:13753600K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275117:13755200K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275293:13764000K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275477:13773200K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275773:13788000K .......... .......... .......... .......... .......... 75% 45.3M 81s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275928:13795750K .......... .......... .......... .......... .......... 75% 95.3M 80s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275948:13796750K .......... .......... .......... .......... .......... 75% 45.3M 80s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:275959:13797300K .......... .......... .......... .......... .......... 75% 45.3M 80s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:276175:13808100K .......... .......... .......... .......... .......... 75% 65.3M 80s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:276354:13817050K .......... .......... .......... .......... .......... 75% 35.3M 80s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:276454:13822050K .......... .......... .......... .......... .......... 75% 25.3M 80s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:276971:13847900K .......... .......... .......... .......... .......... 76% 45.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:276976:13848150K .......... .......... .......... .......... .......... 76% 85.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277035:13851100K .......... .......... .......... .......... .......... 76% 45.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277074:13853050K .......... .......... .......... .......... .......... 76% 35.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277152:13856950K .......... .......... .......... .......... .......... 76% 35.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277280:13863350K .......... .......... .......... .......... .......... 76% 25.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277284:13863550K .......... .......... .......... .......... .......... 76% 35.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277297:13864200K .......... .......... .......... .......... .......... 76% 45.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277434:13871050K .......... .......... .......... .......... .......... 76% 45.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:277616:13880150K .......... .......... .......... .......... .......... 76% 25.3M 79s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:278022:13900450K .......... .......... .......... .......... .......... 76% 25.3M 78s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:278154:13907050K .......... .......... .......... .......... .......... 76% 55.3M 78s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:278428:13920750K .......... .......... .......... .......... .......... 76% 35.3M 78s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:278452:13921950K .......... .......... .......... .......... .......... 76% 65.3M 78s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:278667:13932700K .......... .......... .......... .......... .......... 76% 25.3M 78s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:278909:13944800K .......... .......... .......... .......... .......... 76% 55.3M 78s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279060:13952350K .......... .......... .......... .......... .......... 76% 35.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279222:13960450K .......... .......... .......... .......... .......... 76% 55.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279276:13963150K .......... .......... .......... .......... .......... 76% 35.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279530:13975850K .......... .......... .......... .......... .......... 76% 45.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279579:13978300K .......... .......... .......... .......... .......... 76% 55.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279731:13985900K .......... .......... .......... .......... .......... 76% 55.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279733:13986000K .......... .......... .......... .......... .......... 76% 15.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:279822:13990450K .......... .......... .......... .......... .......... 76% 75.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280033:14001000K .......... .......... .......... .......... .......... 76% 35.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280080:14003350K .......... .......... .......... .......... .......... 76% 45.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280131:14005900K .......... .......... .......... .......... .......... 76% 35.3M 77s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280371:14017900K .......... .......... .......... .......... .......... 77% 35.3M 76s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280463:14022500K .......... .......... .......... .......... .......... 77% 35.3M 76s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280493:14024000K .......... .......... .......... .......... .......... 77% 35.3M 76s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:280849:14041800K .......... .......... .......... .......... .......... 77% 35.3M 76s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:281107:14054700K .......... .......... .......... .......... .......... 77% 65.3M 76s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:281280:14063350K .......... .......... .......... .......... .......... 77% 35.3M 75s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:281415:14070100K .......... .......... .......... .......... .......... 77% 45.3M 75s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:281473:14073000K .......... .......... .......... .......... .......... 77% 45.3M 75s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:281635:14081100K .......... .......... .......... .......... .......... 77% 15.3M 75s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282079:14103300K .......... .......... .......... .......... .......... 77% 45.3M 75s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282297:14114200K .......... .......... .......... .......... .......... 77% 35.3M 75s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282472:14122950K .......... .......... .......... .......... .......... 77% 35.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282592:14128950K .......... .......... .......... .......... .......... 77% 75.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282676:14133150K .......... .......... .......... .......... .......... 77% 35.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282798:14139250K .......... .......... .......... .......... .......... 77% 45.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282811:14139900K .......... .......... .......... .......... .......... 77% 45.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282919:14145300K .......... .......... .......... .......... .......... 77% 45.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282949:14146800K .......... .......... .......... .......... .......... 77% 25.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:282964:14147550K .......... .......... .......... .......... .......... 77% 55.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283046:14151650K .......... .......... .......... .......... .......... 77% 45.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283123:14155500K .......... .......... .......... .......... .......... 77% 45.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283317:14165200K .......... .......... .......... .......... .......... 77% 45.3M 74s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283747:14186700K .......... .......... .......... .......... .......... 77% 35.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283835:14191100K .......... .......... .......... .......... .......... 77% 45.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283896:14194150K .......... .......... .......... .......... .......... 78% 45.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:283968:14197750K .......... .......... .......... .......... .......... 78% 35.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284059:14202300K .......... .......... .......... .......... .......... 78% 55.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284204:14209550K .......... .......... .......... .......... .......... 78% 85.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284293:14214000K .......... .......... .......... .......... .......... 78% 35.3M 73s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284529:14225800K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284549:14226800K .......... .......... .......... .......... .......... 78% 35.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284647:14231700K .......... .......... .......... .......... .......... 78% 75.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284734:14236050K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284756:14237150K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:284920:14245350K .......... .......... .......... .......... .......... 78% 25.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285078:14253250K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285188:14258750K .......... .......... .......... .......... .......... 78% 35.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285202:14259450K .......... .......... .......... .......... .......... 78% 95.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285274:14263050K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285384:14268550K .......... .......... .......... .......... .......... 78% 35.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285447:14271700K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285450:14271850K .......... .......... .......... .......... .......... 78% 45.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285512:14274950K .......... .......... .......... .......... .......... 78% 55.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285532:14275950K .......... .......... .......... .......... .......... 78% 35.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285602:14279450K .......... .......... .......... .......... .......... 78% 35.3M 72s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:285870:14292850K .......... .......... .......... .......... .......... 78% 45.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286439:14321300K .......... .......... .......... .......... .......... 78% 45.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286452:14321950K .......... .......... .......... .......... .......... 78% 45.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286558:14327250K .......... .......... .......... .......... .......... 78% 65.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286589:14328800K .......... .......... .......... .......... .......... 78% 45.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286605:14329600K .......... .......... .......... .......... .......... 78% 35.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286698:14334250K .......... .......... .......... .......... .......... 78% 25.3M 71s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:286951:14346900K .......... .......... .......... .......... .......... 78% 35.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287036:14351150K .......... .......... .......... .......... .......... 78% 45.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287105:14354600K .......... .......... .......... .......... .......... 78% 35.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287306:14364650K .......... .......... .......... .......... .......... 78% 65.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287340:14366350K .......... .......... .......... .......... .......... 78% 45.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287407:14369700K .......... .......... .......... .......... .......... 78% 45.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287735:14386100K .......... .......... .......... .......... .......... 79% 35.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287756:14387150K .......... .......... .......... .......... .......... 79% 35.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287760:14387350K .......... .......... .......... .......... .......... 79% 25.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287830:14390850K .......... .......... .......... .......... .......... 79% 45.3M 70s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:287885:14393600K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288025:14400600K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288153:14407000K .......... .......... .......... .......... .......... 79% 65.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288158:14407250K .......... .......... .......... .......... .......... 79% 55.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288227:14410700K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288455:14422100K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288632:14430950K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288658:14432250K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288751:14436900K .......... .......... .......... .......... .......... 79% 45.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288845:14441600K .......... .......... .......... .......... .......... 79% 65.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288927:14445700K .......... .......... .......... .......... .......... 79% 25.3M 69s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:288964:14447550K .......... .......... .......... .......... .......... 79% 45.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289125:14455600K .......... .......... .......... .......... .......... 79% 45.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289311:14464900K .......... .......... .......... .......... .......... 79% 65.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289528:14475750K .......... .......... .......... .......... .......... 79% 35.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289618:14480250K .......... .......... .......... .......... .......... 79% 75.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289634:14481050K .......... .......... .......... .......... .......... 79% 25.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289718:14485250K .......... .......... .......... .......... .......... 79% 35.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289900:14494350K .......... .......... .......... .......... .......... 79% 35.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:289950:14496850K .......... .......... .......... .......... .......... 79% 35.3M 68s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290151:14506900K .......... .......... .......... .......... .......... 79% 45.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290229:14510800K .......... .......... .......... .......... .......... 79% 45.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290246:14511650K .......... .......... .......... .......... .......... 79% 45.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290316:14515150K .......... .......... .......... .......... .......... 79% 35.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290404:14519550K .......... .......... .......... .......... .......... 79% 35.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290474:14523050K .......... .......... .......... .......... .......... 79% 35.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290923:14545500K .......... .......... .......... .......... .......... 79% 25.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290958:14547250K .......... .......... .......... .......... .......... 79% 45.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:290992:14548950K .......... .......... .......... .......... .......... 79% 45.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:291039:14551300K .......... .......... .......... .......... .......... 79% 95.3M 67s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:291281:14563400K .......... .......... .......... .......... .......... 80% 25.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:291375:14568100K .......... .......... .......... .......... .......... 80% 25.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:291715:14585100K .......... .......... .......... .......... .......... 80% 35.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:291812:14589950K .......... .......... .......... .......... .......... 80% 45.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:291924:14595550K .......... .......... .......... .......... .......... 80% 45.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292040:14601350K .......... .......... .......... .......... .......... 80% 45.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292092:14603950K .......... .......... .......... .......... .......... 80% 35.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292143:14606500K .......... .......... .......... .......... .......... 80% 45.3M 66s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292373:14618000K .......... .......... .......... .......... .......... 80% 45.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292377:14618200K .......... .......... .......... .......... .......... 80% 45.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292531:14625900K .......... .......... .......... .......... .......... 80% 45.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292809:14639800K .......... .......... .......... .......... .......... 80% 35.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:292874:14643050K .......... .......... .......... .......... .......... 80% 45.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293036:14651150K .......... .......... .......... .......... .......... 80% 35.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293062:14652450K .......... .......... .......... .......... .......... 80% 35.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293219:14660300K .......... .......... .......... .......... .......... 80% 35.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293268:14662750K .......... .......... .......... .......... .......... 80% 45.3M 65s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293444:14671550K .......... .......... .......... .......... .......... 80% 35.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293722:14685450K .......... .......... .......... .......... .......... 80% 35.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293785:14688600K .......... .......... .......... .......... .......... 80% 35.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293817:14690200K .......... .......... .......... .......... .......... 80% 45.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:293857:14692200K .......... .......... .......... .......... .......... 80% 45.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294124:14705550K .......... .......... .......... .......... .......... 80% 45.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294199:14709300K .......... .......... .......... .......... .......... 80% 45.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294230:14710850K .......... .......... .......... .......... .......... 80% 45.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294276:14713150K .......... .......... .......... .......... .......... 80% 45.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294288:14713750K .......... .......... .......... .......... .......... 80% 65.3M 64s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294527:14725700K .......... .......... .......... .......... .......... 80% 45.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294586:14728650K .......... .......... .......... .......... .......... 80% 35.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294763:14737500K .......... .......... .......... .......... .......... 80% 55.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294768:14737750K .......... .......... .......... .......... .......... 80% 85.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294777:14738200K .......... .......... .......... .......... .......... 80% 35.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:294802:14739450K .......... .......... .......... .......... .......... 81% 55.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295143:14756500K .......... .......... .......... .......... .......... 81% 45.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295153:14757000K .......... .......... .......... .......... .......... 81% 35.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295332:14765950K .......... .......... .......... .......... .......... 81% 35.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295401:14769400K .......... .......... .......... .......... .......... 81% 55.3M 63s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295743:14786500K .......... .......... .......... .......... .......... 81% 25.3M 62s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295792:14788950K .......... .......... .......... .......... .......... 81% 35.3M 62s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:295902:14794450K .......... .......... .......... .......... .......... 81% 35.3M 62s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:296053:14802000K .......... .......... .......... .......... .......... 81% 75.3M 62s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:296199:14809300K .......... .......... .......... .......... .......... 81% 35.3M 62s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:296230:14810850K .......... .......... .......... .......... .......... 81% 85.3M 62s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:296951:14846900K .......... .......... .......... .......... .......... 81% 25.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297002:14849450K .......... .......... .......... .......... .......... 81% 45.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297038:14851250K .......... .......... .......... .......... .......... 81% 35.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297188:14858750K .......... .......... .......... .......... .......... 81% 35.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297189:14858800K .......... .......... .......... .......... .......... 81% 45.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297321:14865400K .......... .......... .......... .......... .......... 81% 35.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297572:14877950K .......... .......... .......... .......... .......... 81% 45.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297573:14878000K .......... .......... .......... .......... .......... 81% 35.3M 61s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297720:14885350K .......... .......... .......... .......... .......... 81% 35.3M 60s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297896:14894150K .......... .......... .......... .......... .......... 81% 45.3M 60s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:297939:14896300K .......... .......... .......... .......... .......... 81% 45.3M 60s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:298369:14917800K .......... .......... .......... .......... .......... 81% 35.3M 60s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:298802:14939450K .......... .......... .......... .......... .......... 82% 35.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:298943:14946500K .......... .......... .......... .......... .......... 82% 35.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299020:14950350K .......... .......... .......... .......... .......... 82% 45.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299042:14951450K .......... .......... .......... .......... .......... 82% 85.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299407:14969700K .......... .......... .......... .......... .......... 82% 55.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299416:14970150K .......... .......... .......... .......... .......... 82% 85.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299680:14983350K .......... .......... .......... .......... .......... 82% 45.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299761:14987400K .......... .......... .......... .......... .......... 82% 25.3M 59s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:299907:14994700K .......... .......... .......... .......... .......... 82% 35.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300292:15013950K .......... .......... .......... .......... .......... 82% 75.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300320:15015350K .......... .......... .......... .......... .......... 82% 55.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300383:15018500K .......... .......... .......... .......... .......... 82% 35.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300460:15022350K .......... .......... .......... .......... .......... 82% 35.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300622:15030450K .......... .......... .......... .......... .......... 82% 35.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300741:15036400K .......... .......... .......... .......... .......... 82% 45.3M 58s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:300970:15047850K .......... .......... .......... .......... .......... 82% 45.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:301238:15061250K .......... .......... .......... .......... .......... 82% 35.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:301324:15065550K .......... .......... .......... .......... .......... 82% 75.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:301651:15081900K .......... .......... .......... .......... .......... 82% 95.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:301911:15094900K .......... .......... .......... .......... .......... 82% 45.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:301949:15096800K .......... .......... .......... .......... .......... 82% 45.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302046:15101650K .......... .......... .......... .......... .......... 82% 55.3M 57s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302069:15102800K .......... .......... .......... .......... .......... 83% 35.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302106:15104650K .......... .......... .......... .......... .......... 83% 35.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302383:15118500K .......... .......... .......... .......... .......... 83% 25.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302423:15120500K .......... .......... .......... .......... .......... 83% 75.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302688:15133750K .......... .......... .......... .......... .......... 83% 55.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302743:15136500K .......... .......... .......... .......... .......... 83% 45.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:302966:15147650K .......... .......... .......... .......... .......... 83% 35.3M 56s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:303198:15159250K .......... .......... .......... .......... .......... 83% 45.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:303587:15178700K .......... .......... .......... .......... .......... 83% 85.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:303961:15197400K .......... .......... .......... .......... .......... 83% 45.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304033:15201000K .......... .......... .......... .......... .......... 83% 55.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304059:15202300K .......... .......... .......... .......... .......... 83% 35.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304102:15204450K .......... .......... .......... .......... .......... 83% 45.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304104:15204550K .......... .......... .......... .......... .......... 83% 25.3M 55s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304418:15220250K .......... .......... .......... .......... .......... 83% 45.3M 54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304682:15233450K .......... .......... .......... .......... .......... 83% 45.3M 54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304814:15240050K .......... .......... .......... .......... .......... 83% 55.3M 54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:304897:15244200K .......... .......... .......... .......... .......... 83% 45.3M 54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:305323:15265500K .......... .......... .......... .......... .......... 83% 75.3M 54s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:305361:15267400K .......... .......... .......... .......... .......... 83% 35.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:305423:15270500K .......... .......... .......... .......... .......... 83% 55.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:305528:15275750K .......... .......... .......... .......... .......... 83% 45.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:305775:15288100K .......... .......... .......... .......... .......... 84% 95.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:305806:15289650K .......... .......... .......... .......... .......... 84% 35.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306042:15301450K .......... .......... .......... .......... .......... 84% 35.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306287:15313700K .......... .......... .......... .......... .......... 84% 65.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306292:15313950K .......... .......... .......... .......... .......... 84% 45.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306307:15314700K .......... .......... .......... .......... .......... 84% 45.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306318:15315250K .......... .......... .......... .......... .......... 84% 45.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306362:15317450K .......... .......... .......... .......... .......... 84% 65.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306363:15317500K .......... .......... .......... .......... .......... 84% 45.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306367:15317700K .......... .......... .......... .......... .......... 84% 25.3M 53s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306484:15323550K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306493:15324000K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306662:15332450K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306737:15336200K .......... .......... .......... .......... .......... 84% 35.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306953:15347000K .......... .......... .......... .......... .......... 84% 35.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:306995:15349100K .......... .......... .......... .......... .......... 84% 55.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307023:15350500K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307110:15354850K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307283:15363500K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307522:15375450K .......... .......... .......... .......... .......... 84% 45.3M 52s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307642:15381450K .......... .......... .......... .......... .......... 84% 65.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307715:15385100K .......... .......... .......... .......... .......... 84% 35.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307823:15390500K .......... .......... .......... .......... .......... 84% 65.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307908:15394750K .......... .......... .......... .......... .......... 84% 45.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:307927:15395700K .......... .......... .......... .......... .......... 84% 45.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:308143:15406500K .......... .......... .......... .......... .......... 84% 35.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:308199:15409300K .......... .......... .......... .......... .......... 84% 45.3M 51s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:308677:15433200K .......... .......... .......... .......... .......... 84% 85.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:308708:15434750K .......... .......... .......... .......... .......... 84% 45.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:308785:15438600K .......... .......... .......... .......... .......... 84% 45.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:309366:15467650K .......... .......... .......... .......... .......... 85% 45.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:309571:15477900K .......... .......... .......... .......... .......... 85% 55.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:309680:15483350K .......... .......... .......... .......... .......... 85% 45.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:309732:15485950K .......... .......... .......... .......... .......... 85% 45.3M 50s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:309750:15486850K .......... .......... .......... .......... .......... 85% 35.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:309824:15490550K .......... .......... .......... .......... .......... 85% 25.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310002:15499450K .......... .......... .......... .......... .......... 85% 95.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310027:15500700K .......... .......... .......... .......... .......... 85% 55.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310182:15508450K .......... .......... .......... .......... .......... 85% 45.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310324:15515550K .......... .......... .......... .......... .......... 85% 25.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310349:15516800K .......... .......... .......... .......... .......... 85% 45.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310385:15518600K .......... .......... .......... .......... .......... 85% 45.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310570:15527850K .......... .......... .......... .......... .......... 85% 35.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310601:15529400K .......... .......... .......... .......... .......... 85% 65.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310732:15535950K .......... .......... .......... .......... .......... 85% 35.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310735:15536100K .......... .......... .......... .......... .......... 85% 35.3M 49s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310936:15546150K .......... .......... .......... .......... .......... 85% 65.3M 48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:310948:15546750K .......... .......... .......... .......... .......... 85% 45.3M 48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:311140:15556350K .......... .......... .......... .......... .......... 85% 45.3M 48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:311215:15560100K .......... .......... .......... .......... .......... 85% 45.3M 48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:311282:15563450K .......... .......... .......... .......... .......... 85% 85.3M 48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:311385:15568600K .......... .......... .......... .......... .......... 85% 35.3M 48s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312119:15605300K .......... .......... .......... .......... .......... 85% 45.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312214:15610050K .......... .......... .......... .......... .......... 85% 35.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312614:15630050K .......... .......... .......... .......... .......... 85% 35.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312712:15634950K .......... .......... .......... .......... .......... 85% 35.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312761:15637400K .......... .......... .......... .......... .......... 85% 45.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312878:15643250K .......... .......... .......... .......... .......... 85% 65.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:312891:15643900K .......... .......... .......... .......... .......... 85% 45.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:313015:15650100K .......... .......... .......... .......... .......... 86% 45.3M 47s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:313059:15652300K .......... .......... .......... .......... .......... 86% 45.3M 46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:313127:15655700K .......... .......... .......... .......... .......... 86% 35.3M 46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:313145:15656600K .......... .......... .......... .......... .......... 86% 75.3M 46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:313717:15685200K .......... .......... .......... .......... .......... 86% 45.3M 46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:313762:15687450K .......... .......... .......... .......... .......... 86% 45.3M 46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:314039:15701300K .......... .......... .......... .......... .......... 86% 45.3M 46s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:314244:15711550K .......... .......... .......... .......... .......... 86% 25.3M 45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:314587:15728700K .......... .......... .......... .......... .......... 86% 45.3M 45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:314667:15732700K .......... .......... .......... .......... .......... 86% 35.3M 45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:314888:15743750K .......... .......... .......... .......... .......... 86% 25.3M 45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:314918:15745250K .......... .......... .......... .......... .......... 86% 25.3M 45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:315112:15754950K .......... .......... .......... .......... .......... 86% 45.3M 45s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:315500:15774350K .......... .......... .......... .......... .......... 86% 35.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:315726:15785650K .......... .......... .......... .......... .......... 86% 45.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:315798:15789250K .......... .......... .......... .......... .......... 86% 45.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:315826:15790650K .......... .......... .......... .......... .......... 86% 45.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:315830:15790850K .......... .......... .......... .......... .......... 86% 45.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:316013:15800000K .......... .......... .......... .......... .......... 86% 45.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:316015:15800100K .......... .......... .......... .......... .......... 86% 45.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:316072:15802950K .......... .......... .......... .......... .......... 86% 35.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:316235:15811100K .......... .......... .......... .......... .......... 86% 25.3M 44s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:316706:15834650K .......... .......... .......... .......... .......... 87% 65.3M 43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:316869:15842800K .......... .......... .......... .......... .......... 87% 35.3M 43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:317003:15849500K .......... .......... .......... .......... .......... 87% 75.3M 43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:317275:15863100K .......... .......... .......... .......... .......... 87% 25.3M 43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:317336:15866150K .......... .......... .......... .......... .......... 87% 55.3M 43s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:317469:15872800K .......... .......... .......... .......... .......... 87% 45.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:317484:15873550K .......... .......... .......... .......... .......... 87% 35.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:317990:15898850K .......... .......... .......... .......... .......... 87% 45.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:318081:15903400K .......... .......... .......... .......... .......... 87% 35.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:318304:15914550K .......... .......... .......... .......... .......... 87% 55.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:318347:15916700K .......... .......... .......... .......... .......... 87% 35.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:318509:15924800K .......... .......... .......... .......... .......... 87% 55.3M 42s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319086:15953650K .......... .......... .......... .......... .......... 87% 35.3M 41s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319616:15980150K .......... .......... .......... .......... .......... 87% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319642:15981450K .......... .......... .......... .......... .......... 87% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319697:15984200K .......... .......... .......... .......... .......... 87% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319711:15984900K .......... .......... .......... .......... .......... 87% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319784:15988550K .......... .......... .......... .......... .......... 87% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319985:15998600K .......... .......... .......... .......... .......... 87% 25.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:319994:15999050K .......... .......... .......... .......... .......... 87% 65.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320021:16000400K .......... .......... .......... .......... .......... 87% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320053:16002000K .......... .......... .......... .......... .......... 87% 25.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320176:16008150K .......... .......... .......... .......... .......... 87% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320196:16009150K .......... .......... .......... .......... .......... 87% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320237:16011200K .......... .......... .......... .......... .......... 87% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320258:16012250K .......... .......... .......... .......... .......... 88% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320395:16019100K .......... .......... .......... .......... .......... 88% 55.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320463:16022500K .......... .......... .......... .......... .......... 88% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320509:16024800K .......... .......... .......... .......... .......... 88% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320604:16029550K .......... .......... .......... .......... .......... 88% 85.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320613:16030000K .......... .......... .......... .......... .......... 88% 45.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320639:16031300K .......... .......... .......... .......... .......... 88% 35.3M 40s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320828:16040750K .......... .......... .......... .......... .......... 88% 75.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320865:16042600K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320886:16043650K .......... .......... .......... .......... .......... 88% 35.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320891:16043900K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320902:16044450K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320940:16046350K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:320968:16047750K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321052:16051950K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321102:16054450K .......... .......... .......... .......... .......... 88% 55.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321153:16057000K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321162:16057450K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321235:16061100K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321239:16061300K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321347:16066700K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321348:16066750K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321369:16067800K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321410:16069850K .......... .......... .......... .......... .......... 88% 45.3M 39s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321799:16089300K .......... .......... .......... .......... .......... 88% 45.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321886:16093650K .......... .......... .......... .......... .......... 88% 45.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:321909:16094800K .......... .......... .......... .......... .......... 88% 35.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322071:16102900K .......... .......... .......... .......... .......... 88% 65.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322131:16105900K .......... .......... .......... .......... .......... 88% 55.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322156:16107150K .......... .......... .......... .......... .......... 88% 45.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322199:16109300K .......... .......... .......... .......... .......... 88% 55.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322411:16119900K .......... .......... .......... .......... .......... 88% 55.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322483:16123500K .......... .......... .......... .......... .......... 88% 35.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322687:16133700K .......... .......... .......... .......... .......... 88% 65.3M 38s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:322877:16143200K .......... .......... .......... .......... .......... 88% 75.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323044:16151550K .......... .......... .......... .......... .......... 88% 35.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323156:16157150K .......... .......... .......... .......... .......... 88% 25.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323282:16163450K .......... .......... .......... .......... .......... 88% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323377:16168200K .......... .......... .......... .......... .......... 88% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323481:16173400K .......... .......... .......... .......... .......... 88% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323542:16176450K .......... .......... .......... .......... .......... 88% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323604:16179550K .......... .......... .......... .......... .......... 88% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323736:16186150K .......... .......... .......... .......... .......... 88% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323912:16194950K .......... .......... .......... .......... .......... 89% 45.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323950:16196850K .......... .......... .......... .......... .......... 89% 55.3M 37s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:323980:16198350K .......... .......... .......... .......... .......... 89% 35.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324045:16201600K .......... .......... .......... .......... .......... 89% 45.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324210:16209850K .......... .......... .......... .......... .......... 89% 35.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324304:16214550K .......... .......... .......... .......... .......... 89% 65.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324453:16222000K .......... .......... .......... .......... .......... 89% 25.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324614:16230050K .......... .......... .......... .......... .......... 89% 75.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324650:16231850K .......... .......... .......... .......... .......... 89% 55.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324820:16240350K .......... .......... .......... .......... .......... 89% 35.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:324868:16242750K .......... .......... .......... .......... .......... 89% 45.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:325002:16249450K .......... .......... .......... .......... .......... 89% 65.3M 36s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:325112:16254950K .......... .......... .......... .......... .......... 89% 45.3M 35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:325134:16256050K .......... .......... .......... .......... .......... 89% 45.3M 35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:325382:16268450K .......... .......... .......... .......... .......... 89% 35.3M 35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:325860:16292350K .......... .......... .......... .......... .......... 89% 45.3M 35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:326017:16300200K .......... .......... .......... .......... .......... 89% 55.3M 35s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:326600:16329350K .......... .......... .......... .......... .......... 89% 35.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:326650:16331850K .......... .......... .......... .......... .......... 89% 75.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:326704:16334550K .......... .......... .......... .......... .......... 89% 25.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:326762:16337450K .......... .......... .......... .......... .......... 89% 55.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:326866:16342650K .......... .......... .......... .......... .......... 89% 25.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327009:16349800K .......... .......... .......... .......... .......... 89% 35.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327087:16353700K .......... .......... .......... .......... .......... 89% 95.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327195:16359100K .......... .......... .......... .......... .......... 89% 35.3M 34s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327288:16363750K .......... .......... .......... .......... .......... 89% 55.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327429:16370800K .......... .......... .......... .......... .......... 89% 55.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327717:16385200K .......... .......... .......... .......... .......... 90% 75.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327722:16385450K .......... .......... .......... .......... .......... 90% 75.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327762:16387450K .......... .......... .......... .......... .......... 90% 45.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:327918:16395250K .......... .......... .......... .......... .......... 90% 35.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328040:16401350K .......... .......... .......... .......... .......... 90% 65.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328295:16414100K .......... .......... .......... .......... .......... 90% 35.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328301:16414400K .......... .......... .......... .......... .......... 90% 25.3M 33s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328356:16417150K .......... .......... .......... .......... .......... 90% 45.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328424:16420550K .......... .......... .......... .......... .......... 90% 35.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328784:16438550K .......... .......... .......... .......... .......... 90% 35.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328917:16445200K .......... .......... .......... .......... .......... 90% 65.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:328954:16447050K .......... .......... .......... .......... .......... 90% 35.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329033:16451000K .......... .......... .......... .......... .......... 90% 45.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329198:16459250K .......... .......... .......... .......... .......... 90% 45.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329326:16465650K .......... .......... .......... .......... .......... 90% 55.3M 32s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329540:16476350K .......... .......... .......... .......... .......... 90% 55.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329650:16481850K .......... .......... .......... .......... .......... 90% 35.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329696:16484150K .......... .......... .......... .......... .......... 90% 35.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329863:16492500K .......... .......... .......... .......... .......... 90% 55.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329881:16493400K .......... .......... .......... .......... .......... 90% 45.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329914:16495050K .......... .......... .......... .......... .......... 90% 55.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:329972:16497950K .......... .......... .......... .......... .......... 90% 45.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330032:16500950K .......... .......... .......... .......... .......... 90% 25.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330084:16503550K .......... .......... .......... .......... .......... 90% 35.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330109:16504800K .......... .......... .......... .......... .......... 90% 45.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330215:16510100K .......... .......... .......... .......... .......... 90% 25.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330250:16511850K .......... .......... .......... .......... .......... 90% 95.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330268:16512750K .......... .......... .......... .......... .......... 90% 45.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330375:16518100K .......... .......... .......... .......... .......... 90% 35.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330377:16518200K .......... .......... .......... .......... .......... 90% 35.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330397:16519200K .......... .......... .......... .......... .......... 90% 35.3M 31s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330658:16532250K .......... .......... .......... .......... .......... 90% 65.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330692:16533950K .......... .......... .......... .......... .......... 90% 35.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330744:16536550K .......... .......... .......... .......... .......... 90% 75.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330938:16546250K .......... .......... .......... .......... .......... 90% 65.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:330964:16547550K .......... .......... .......... .......... .......... 90% 35.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:331006:16549650K .......... .......... .......... .......... .......... 90% 55.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:331111:16554900K .......... .......... .......... .......... .......... 90% 35.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:331116:16555150K .......... .......... .......... .......... .......... 90% 45.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:331223:16560500K .......... .......... .......... .......... .......... 91% 35.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:331341:16566400K .......... .......... .......... .......... .......... 91% 55.3M 30s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:331707:16584700K .......... .......... .......... .......... .......... 91% 55.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332026:16600650K .......... .......... .......... .......... .......... 91% 95.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332043:16601500K .......... .......... .......... .......... .......... 91% 35.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332057:16602200K .......... .......... .......... .......... .......... 91% 45.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332074:16603050K .......... .......... .......... .......... .......... 91% 45.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332247:16611700K .......... .......... .......... .......... .......... 91% 45.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332317:16615200K .......... .......... .......... .......... .......... 91% 25.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332476:16623150K .......... .......... .......... .......... .......... 91% 45.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332645:16631600K .......... .......... .......... .......... .......... 91% 45.3M 29s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332849:16641800K .......... .......... .......... .......... .......... 91% 45.3M 28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:332963:16647500K .......... .......... .......... .......... .......... 91% 45.3M 28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:333399:16669300K .......... .......... .......... .......... .......... 91% 65.3M 28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:333620:16680350K .......... .......... .......... .......... .......... 91% 45.3M 28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:333672:16682950K .......... .......... .......... .......... .......... 91% 35.3M 28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:333728:16685750K .......... .......... .......... .......... .......... 91% 45.3M 28s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:334336:16716150K .......... .......... .......... .......... .......... 91% 35.3M 27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:334609:16729800K .......... .......... .......... .......... .......... 91% 45.3M 27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:334843:16741500K .......... .......... .......... .......... .......... 92% 45.3M 27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:334873:16743000K .......... .......... .......... .......... .......... 92% 45.3M 27s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335113:16755000K .......... .......... .......... .......... .......... 92% 35.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335198:16759250K .......... .......... .......... .......... .......... 92% 45.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335606:16779650K .......... .......... .......... .......... .......... 92% 35.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335747:16786700K .......... .......... .......... .......... .......... 92% 45.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335760:16787350K .......... .......... .......... .......... .......... 92% 35.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335866:16792650K .......... .......... .......... .......... .......... 92% 35.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:335966:16797650K .......... .......... .......... .......... .......... 92% 35.3M 26s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336054:16802050K .......... .......... .......... .......... .......... 92% 45.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336127:16805700K .......... .......... .......... .......... .......... 92% 35.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336377:16818200K .......... .......... .......... .......... .......... 92% 45.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336408:16819750K .......... .......... .......... .......... .......... 92% 45.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336538:16826250K .......... .......... .......... .......... .......... 92% 45.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336598:16829250K .......... .......... .......... .......... .......... 92% 35.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336640:16831350K .......... .......... .......... .......... .......... 92% 25.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336671:16832900K .......... .......... .......... .......... .......... 92% 45.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:336988:16848750K .......... .......... .......... .......... .......... 92% 35.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337006:16849650K .......... .......... .......... .......... .......... 92% 45.3M 25s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337129:16855800K .......... .......... .......... .......... .......... 92% 45.3M 24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337140:16856350K .......... .......... .......... .......... .......... 92% 45.3M 24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337206:16859650K .......... .......... .......... .......... .......... 92% 65.3M 24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337275:16863100K .......... .......... .......... .......... .......... 92% 45.3M 24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337419:16870300K .......... .......... .......... .......... .......... 92% 45.3M 24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:337885:16893600K .......... .......... .......... .......... .......... 92% 65.3M 24s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338198:16909250K .......... .......... .......... .......... .......... 92% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338242:16911450K .......... .......... .......... .......... .......... 92% 55.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338380:16918350K .......... .......... .......... .......... .......... 92% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338512:16924950K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338523:16925500K .......... .......... .......... .......... .......... 93% 25.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338545:16926600K .......... .......... .......... .......... .......... 93% 45.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338600:16929350K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338685:16933600K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338734:16936050K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338849:16941800K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338880:16943350K .......... .......... .......... .......... .......... 93% 45.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338961:16947400K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:338976:16948150K .......... .......... .......... .......... .......... 93% 25.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:339001:16949400K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:339155:16957100K .......... .......... .......... .......... .......... 93% 45.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:339186:16958650K .......... .......... .......... .......... .......... 93% 35.3M 23s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:340066:17002650K .......... .......... .......... .......... .......... 93% 45.3M 22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:340111:17004900K .......... .......... .......... .......... .......... 93% 45.3M 22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:340264:17012550K .......... .......... .......... .......... .......... 93% 35.3M 22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:340340:17016350K .......... .......... .......... .......... .......... 93% 45.3M 22s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:340742:17036450K .......... .......... .......... .......... .......... 93% 55.3M 21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:340757:17037200K .......... .......... .......... .......... .......... 93% 35.3M 21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341036:17051150K .......... .......... .......... .......... .......... 93% 85.3M 21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341173:17058000K .......... .......... .......... .......... .......... 93% 35.3M 21s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341509:17074800K .......... .......... .......... .......... .......... 93% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341512:17074950K .......... .......... .......... .......... .......... 93% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341610:17079850K .......... .......... .......... .......... .......... 93% 35.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341637:17081200K .......... .......... .......... .......... .......... 93% 25.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341731:17085900K .......... .......... .......... .......... .......... 93% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:341736:17086150K .......... .......... .......... .......... .......... 93% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342380:17118350K .......... .......... .......... .......... .......... 94% 75.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342412:17119950K .......... .......... .......... .......... .......... 94% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342433:17121000K .......... .......... .......... .......... .......... 94% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342440:17121350K .......... .......... .......... .......... .......... 94% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342482:17123450K .......... .......... .......... .......... .......... 94% 55.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342493:17124000K .......... .......... .......... .......... .......... 94% 45.3M 20s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342715:17135100K .......... .......... .......... .......... .......... 94% 45.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342804:17139550K .......... .......... .......... .......... .......... 94% 45.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342847:17141700K .......... .......... .......... .......... .......... 94% 45.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342925:17145600K .......... .......... .......... .......... .......... 94% 35.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:342971:17147900K .......... .......... .......... .......... .......... 94% 35.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343098:17154250K .......... .......... .......... .......... .......... 94% 35.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343162:17157450K .......... .......... .......... .......... .......... 94% 55.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343401:17169400K .......... .......... .......... .......... .......... 94% 45.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343409:17169800K .......... .......... .......... .......... .......... 94% 45.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343539:17176300K .......... .......... .......... .......... .......... 94% 35.3M 19s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343813:17190000K .......... .......... .......... .......... .......... 94% 45.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:343866:17192650K .......... .......... .......... .......... .......... 94% 45.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344078:17203250K .......... .......... .......... .......... .......... 94% 65.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344100:17204350K .......... .......... .......... .......... .......... 94% 35.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344210:17209850K .......... .......... .......... .......... .......... 94% 35.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344238:17211250K .......... .......... .......... .......... .......... 94% 45.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344268:17212750K .......... .......... .......... .......... .......... 94% 55.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344302:17214450K .......... .......... .......... .......... .......... 94% 45.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344605:17229600K .......... .......... .......... .......... .......... 94% 45.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344713:17235000K .......... .......... .......... .......... .......... 94% 45.3M 18s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344860:17242350K .......... .......... .......... .......... .......... 94% 45.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:344876:17243150K .......... .......... .......... .......... .......... 94% 45.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345161:17257400K .......... .......... .......... .......... .......... 94% 35.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345291:17263900K .......... .......... .......... .......... .......... 94% 65.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345469:17272800K .......... .......... .......... .......... .......... 94% 55.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345705:17284600K .......... .......... .......... .......... .......... 94% 45.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345798:17289250K .......... .......... .......... .......... .......... 95% 45.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345822:17290450K .......... .......... .......... .......... .......... 95% 45.3M 17s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:345866:17292650K .......... .......... .......... .......... .......... 95% 45.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346187:17308700K .......... .......... .......... .......... .......... 95% 45.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346217:17310200K .......... .......... .......... .......... .......... 95% 75.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346305:17314600K .......... .......... .......... .......... .......... 95% 45.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346381:17318400K .......... .......... .......... .......... .......... 95% 35.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346412:17319950K .......... .......... .......... .......... .......... 95% 45.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346550:17326850K .......... .......... .......... .......... .......... 95% 45.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346655:17332100K .......... .......... .......... .......... .......... 95% 35.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346845:17341600K .......... .......... .......... .......... .......... 95% 45.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:346935:17346100K .......... .......... .......... .......... .......... 95% 25.3M 16s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347086:17353650K .......... .......... .......... .......... .......... 95% 45.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347177:17358200K .......... .......... .......... .......... .......... 95% 55.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347250:17361850K .......... .......... .......... .......... .......... 95% 35.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347260:17362350K .......... .......... .......... .......... .......... 95% 95.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347396:17369150K .......... .......... .......... .......... .......... 95% 25.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347428:17370750K .......... .......... .......... .......... .......... 95% 45.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347642:17381450K .......... .......... .......... .......... .......... 95% 55.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347692:17383950K .......... .......... .......... .......... .......... 95% 45.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347771:17387900K .......... .......... .......... .......... .......... 95% 35.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347795:17389100K .......... .......... .......... .......... .......... 95% 45.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347885:17393600K .......... .......... .......... .......... .......... 95% 45.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:347940:17396350K .......... .......... .......... .......... .......... 95% 45.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348001:17399400K .......... .......... .......... .......... .......... 95% 35.3M 15s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348064:17402550K .......... .......... .......... .......... .......... 95% 35.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348069:17402800K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348098:17404250K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348199:17409300K .......... .......... .......... .......... .......... 95% 55.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348289:17413800K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348362:17417450K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348508:17424750K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348514:17425050K .......... .......... .......... .......... .......... 95% 35.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348780:17438350K .......... .......... .......... .......... .......... 95% 55.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348859:17442300K .......... .......... .......... .......... .......... 95% 65.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:348967:17447700K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349086:17453650K .......... .......... .......... .......... .......... 95% 45.3M 14s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349194:17459050K .......... .......... .......... .......... .......... 95% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349218:17460250K .......... .......... .......... .......... .......... 95% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349278:17463250K .......... .......... .......... .......... .......... 95% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349300:17464350K .......... .......... .......... .......... .......... 95% 65.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349360:17467350K .......... .......... .......... .......... .......... 95% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349421:17470400K .......... .......... .......... .......... .......... 96% 35.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349654:17482050K .......... .......... .......... .......... .......... 96% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349722:17485450K .......... .......... .......... .......... .......... 96% 35.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349868:17492750K .......... .......... .......... .......... .......... 96% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:349911:17494900K .......... .......... .......... .......... .......... 96% 45.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:350133:17506000K .......... .......... .......... .......... .......... 96% 35.3M 13s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:350345:17516600K .......... .......... .......... .......... .......... 96% 45.3M 12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:350424:17520550K .......... .......... .......... .......... .......... 96% 35.3M 12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:351082:17553450K .......... .......... .......... .......... .......... 96% 25.3M 12s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:351487:17573700K .......... .......... .......... .......... .......... 96% 45.3M 11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:351709:17584800K .......... .......... .......... .......... .......... 96% 45.3M 11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352192:17608950K .......... .......... .......... .......... .......... 96% 55.3M 11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352213:17610000K .......... .......... .......... .......... .......... 96% 35.3M 11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352395:17619100K .......... .......... .......... .......... .......... 96% 35.3M 11s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352446:17621650K .......... .......... .......... .......... .......... 96% 95.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352591:17628900K .......... .......... .......... .......... .......... 96% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352725:17635600K .......... .......... .......... .......... .......... 96% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352738:17636250K .......... .......... .......... .......... .......... 96% 35.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352880:17643350K .......... .......... .......... .......... .......... 96% 15.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352950:17646850K .......... .......... .......... .......... .......... 96% 25.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:352979:17648300K .......... .......... .......... .......... .......... 96% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353176:17658150K .......... .......... .......... .......... .......... 97% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353248:17661750K .......... .......... .......... .......... .......... 97% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353265:17662600K .......... .......... .......... .......... .......... 97% 35.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353307:17664700K .......... .......... .......... .......... .......... 97% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353358:17667250K .......... .......... .......... .......... .......... 97% 35.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353439:17671300K .......... .......... .......... .......... .......... 97% 45.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353456:17672150K .......... .......... .......... .......... .......... 97% 25.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353528:17675750K .......... .......... .......... .......... .......... 97% 55.3M 10s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353584:17678550K .......... .......... .......... .......... .......... 97% 35.3M 9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:353781:17688400K .......... .......... .......... .......... .......... 97% 85.3M 9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354192:17708950K .......... .......... .......... .......... .......... 97% 45.3M 9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354453:17722000K .......... .......... .......... .......... .......... 97% 45.3M 9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354497:17724200K .......... .......... .......... .......... .......... 97% 45.3M 9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354519:17725300K .......... .......... .......... .......... .......... 97% 25.3M 9s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354700:17734350K .......... .......... .......... .......... .......... 97% 25.3M 8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354781:17738400K .......... .......... .......... .......... .......... 97% 35.3M 8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:354944:17746550K .......... .......... .......... .......... .......... 97% 45.3M 8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:355051:17751900K .......... .......... .......... .......... .......... 97% 55.3M 8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:355262:17762450K .......... .......... .......... .......... .......... 97% 75.3M 8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:355331:17765900K .......... .......... .......... .......... .......... 97% 45.3M 8s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:355748:17786750K .......... .......... .......... .......... .......... 97% 35.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:355866:17792650K .......... .......... .......... .......... .......... 97% 35.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356148:17806750K .......... .......... .......... .......... .......... 97% 45.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356236:17811150K .......... .......... .......... .......... .......... 97% 55.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356611:17829900K .......... .......... .......... .......... .......... 97% 45.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356613:17830000K .......... .......... .......... .......... .......... 97% 35.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356641:17831400K .......... .......... .......... .......... .......... 97% 45.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356654:17832050K .......... .......... .......... .......... .......... 98% 45.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356790:17838850K .......... .......... .......... .......... .......... 98% 45.3M 7s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356817:17840200K .......... .......... .......... .......... .......... 98% 55.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356929:17845800K .......... .......... .......... .......... .......... 98% 45.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:356981:17848400K .......... .......... .......... .......... .......... 98% 45.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357163:17857500K .......... .......... .......... .......... .......... 98% 45.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357258:17862250K .......... .......... .......... .......... .......... 98% 75.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357272:17862950K .......... .......... .......... .......... .......... 98% 75.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357280:17863350K .......... .......... .......... .......... .......... 98% 45.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357294:17864050K .......... .......... .......... .......... .......... 98% 45.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357318:17865250K .......... .......... .......... .......... .......... 98% 55.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357404:17869550K .......... .......... .......... .......... .......... 98% 65.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357445:17871600K .......... .......... .......... .......... .......... 98% 55.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:357780:17888350K .......... .......... .......... .......... .......... 98% 45.3M 6s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358197:17909200K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358480:17923350K .......... .......... .......... .......... .......... 98% 55.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358568:17927750K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358576:17928150K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358593:17929000K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358708:17934750K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358787:17938700K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358797:17939200K .......... .......... .......... .......... .......... 98% 35.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:358825:17940600K .......... .......... .......... .......... .......... 98% 45.3M 5s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359032:17950950K .......... .......... .......... .......... .......... 98% 35.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359083:17953500K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359089:17953800K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359166:17957650K .......... .......... .......... .......... .......... 98% 35.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359246:17961650K .......... .......... .......... .......... .......... 98% 55.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359423:17970500K .......... .......... .......... .......... .......... 98% 35.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359566:17977650K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359621:17980400K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359793:17989000K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:359940:17996350K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360091:18003900K .......... .......... .......... .......... .......... 98% 45.3M 4s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360299:18014300K .......... .......... .......... .......... .......... 99% 45.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360442:18021450K .......... .......... .......... .......... .......... 99% 35.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360493:18024000K .......... .......... .......... .......... .......... 99% 35.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360532:18025950K .......... .......... .......... .......... .......... 99% 45.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360618:18030250K .......... .......... .......... .......... .......... 99% 55.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360697:18034200K .......... .......... .......... .......... .......... 99% 45.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360799:18039300K .......... .......... .......... .......... .......... 99% 65.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360850:18041850K .......... .......... .......... .......... .......... 99% 65.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360884:18043550K .......... .......... .......... .......... .......... 99% 45.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:360928:18045750K .......... .......... .......... .......... .......... 99% 65.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361182:18058450K .......... .......... .......... .......... .......... 99% 55.3M 3s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361229:18060800K .......... .......... .......... .......... .......... 99% 65.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361334:18066050K .......... .......... .......... .......... .......... 99% 65.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361343:18066500K .......... .......... .......... .......... .......... 99% 55.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361419:18070300K .......... .......... .......... .......... .......... 99% 45.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361500:18074350K .......... .......... .......... .......... .......... 99% 45.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:361940:18096350K .......... .......... .......... .......... .......... 99% 45.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362060:18102350K .......... .......... .......... .......... .......... 99% 65.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362215:18110100K .......... .......... .......... .......... .......... 99% 45.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362267:18112700K .......... .......... .......... .......... .......... 99% 35.3M 2s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362509:18124800K .......... .......... .......... .......... .......... 99% 45.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362886:18143650K .......... .......... .......... .......... .......... 99% 35.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362893:18144000K .......... .......... .......... .......... .......... 99% 55.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:362907:18144700K .......... .......... .......... .......... .......... 99% 25.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:363212:18159950K .......... .......... .......... .......... .......... 99% 45.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:363221:18160400K .......... .......... .......... .......... .......... 99% 45.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:363320:18165350K .......... .......... .......... .......... .......... 99% 45.3M 1s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:363538:18176250K .......... .......... .......... .......... .......... 99% 45.3M 0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:363687:18183700K .......... .......... .......... .......... .......... 99% 45.3M 0s
docs/phase0/v1-poc-raw/phase3-5-h/phase3-5-h-download.log:363903:18194500K .......... .......... .......... .......... .......... 99% 35.3M 0s

codex
현재 brief의 후보 (a)는 “키 목록은 유지하고 문맥 prefix만 추가”하는 형태라 Hermes 키 답습 자체는 보존되는 것으로 보입니다. 다만 `\s` prefix가 줄바꿈을 포함한다는 점과 “substring 직전 문자가 prefix에 소비된다”는 Python `re` 동작을 별도로 확인하겠습니다.
exec
/bin/bash -lc "sed -n '218,285p' docs/phase0/r4-1-trigger-extension-evidence.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
### 5.3 Alternation patterns (T1-041 ~ T1-042, 2종)

| ID | Source | Vendor | Canary Input | Expected | Actual | Result |
|---|---|---|---|---|---|---|
| T1-041 | Hermes `_SENSITIVE_QUERY_PARAMS` | URL query sensitive keys (16) | `redirect https://x.com/cb?api_key=fakecanaryR41T041NOTAREAL&q=hi` | BLOCK | BLOCK | PASS |
| T1-042 | Hermes `_SENSITIVE_BODY_KEYS` | Body/form sensitive keys (14) | `form payload password=fakecanaryR41T042NOTAREAL&user=alice` | BLOCK | BLOCK | PASS |

### 5.4 합산

- **Tier-1 PASS rate**: **42/42** (100%)
- **차단 메커니즘**: 모든 canary input 이 trigger ABORT 발화 → INSERT 거부, IntegrityError 메시지 = `secret-pattern-detected: INSERT blocked by R-4.1 trigger` (고정 문자열)

---

## 6. C4 safe sample 결과 — false-positive 회피 검증 (모두 PASS)

| Label | Sample | Result | 비고 |
|-------|--------|--------|------|
| plain-text | `hello world, this is a normal user message` | PASS | 일반 텍스트 |
| code-snippet | `def foo(): return 42` | PASS | Python 코드 |
| near-but-not-secret | `session_id_count is 5 and token_count is 100` | PASS | secret-like 변수명, 실제 secret 미포함 |
| safe-json | `{"username": "alice", "user_id": 12345, "page": 2}` | PASS | sensitive key 미포함 JSON |
| safe-url | `https://example.com/api/users` | PASS | query string 없음 |
| safe-url-with-query | `https://example.com/api?q=hello&page=2&lang=en` | PASS | sensitive key (`q`/`page`/`lang`) 미해당 |
| safe-form-no-secret | `theme=dark&lang=en&page=3` | PASS | sensitive key 미해당 form body |
| ascii-art | `+--+--+ \| x \| y \| +--+--+` | PASS | 문자열 그대로 |
| markdown-link | `see [docs](https://example.com/docs) for details` | PASS | URL + 일반 텍스트 |

**Safe sample PASS rate**: **9/9** (100%, false-positive 0건)

---

## 7. 자동 검증 6항목 결과

| Check | 정의 | Detail | Result |
|------|------|------|------|
| C1 | BEFORE INSERT trigger 등록 (45 regex registered) | trigger SQL `executescript` 성공 | PASS |
| C2 | REGEXP UDF 동작 | `'sk-ant-...' REGEXP 'sk-ant-...'` returns 1 | PASS |
| C3 | Tier-1 42종 canary INSERT 차단 | 42/42 BLOCK | PASS |
| C4 | 정상 safe message INSERT 성공 | 9/9 PASS | PASS |
| C5 | DB 평문 부재 | committed rows 9건, R41T marker 0건 / raw bytes 0건 | PASS |
| C6 | 에러 메시지에 canary 평문 미노출 | ABORT 메시지 = `secret-pattern-detected: INSERT blocked by R-4.1 trigger` (고정 문자열) | PASS |

**최종 verdict (재실행 시점 2026-05-06)**: **PASS** (exit code 0, `summary["verdict"] == "PASS"`)

---

## 8. PoC 진화 (1차 → 2차) — evidence 정직성 보존

R-4.1 PoC 는 **2차 실행 PASS** 까지 다음 진화 과정을 거쳤다. evidence 의 정직성을 위해 1차 실행의 PARTIAL 결과도 본 evidence 에 보존.

### 8.1 1차 실행 (PARTIAL)

R-4 §7.2 권고 카탈로그를 *그대로* 반영:
- Tier-1 42 + baseline 5 = 47 patterns 모두 trigger 등록 (H-J/H-L 직접 regex 포함)
- safe sample 9개 (Hermes 카탈로그 *의도된 매칭* 미고려)
- C5 leak detection 을 Hermes 정규식 자체로 수행

결과:
- Tier-1 42/42 차단 PASS
- safe sample **7/9 PASS** (2건 false-positive):
  - `safe-url-with-query` (`https://example.com/?q=hello&page=2`) ↔ H-J `_URL_WITH_QUERY_RE` (모든 URL+query 매칭)
  - `safe-cookie` (`Cookie: session=abc and lang=en`) ↔ T1-041 alternation `session=` 매칭
- C5 leak observations 있음 (false-leak — H-J/H-L 정규식이 safe sample 도 매칭)
- verdict = **PARTIAL**

### 8.2 정정 사항 (1차 → 2차)


exec
/bin/bash -lc "sed -n '1,80p' docs/decisions/ADR-011-means-vs-ends-redaction.md && sed -n '250,275p' docs/decisions/ADR-011-means-vs-ends-redaction.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)

**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
**날짜**: 2026-05-06
**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거

---

## 1. 맥락 (Context)

### 1.1 P2 v2 가정의 붕괴

ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.

Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).

### 1.2 Phase 0 R-1 / R-2 evidence

- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
  - redact 모듈 import 25개 모두 비-DB 경로
  - `hermes_state.py` (SessionDB) redact import 0건

- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.

### 1.3 ADR 권위 해석 요청 사항

위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:

> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**

본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
- G1a/G1b 게이트 분리 공식화
- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
- 자동 학습 vs 자동 정책 변경 분리

---

## 2. 결정 (Decision)

본 ADR은 다음 4가지를 권위로 선언한다.

### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)

**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**

- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:

  | # | 조건 | 검증 방식 |
  |---|------|---------|
  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.

### 2.2 G1a / G1b 게이트 분리 공식화

P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   Evidence: agent/redact.py docstring "for logs and tool output",
             redact import 25개 모두 비-DB,
             hermes_state.py redact import 0건
   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
             + 6항목 자동 검증 (C1~C6 모두 PASS)
   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습)
- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — 본 ADR §2.1 (수단/목적 분리) / §2.2 (G1a/G1b 분리) / §2.3 (Hermes ≠ root of trust) / §2.4 (T1/T2/T3) 모두 답습 권위 발행. P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §3 dual-structure + §6 G4 + §7 ADR 매트릭스 + §11 변경 절차 + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화

### 8.3 Phase 0 evidence
- `docs/phase0/day1-environment-and-fact-check.md` (Hermes v0.12.0 사실 확인)
- `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL)
- `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PASS)
- `docker/r2-poc/` (R-2 PoC Docker 격리 환경 + 6항목 자동 검증 스크립트)

### 8.4 합의 보고서
- `docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` (단축 합의 §R-3 권고)
- `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 합의 권위 위계)
- `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (본 ADR 단축 합의)

### 8.5 후속 작업 (R-4 ~ R-7 + 4 게이트 PASS + ADR 발행 + Archive 후속)

#### 8.5.1 R-4 ~ R-7 (모법 역할 — §3 답습)

- R-4: ✅ **완료** — `docs/architecture/redaction-pattern-equivalence.md` (Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교 + gap 식별 + 보충 권고, ADR-011 §2.1 (a) 충족, 2026-05-06)
- R-4.1: ✅ **완료** — `docs/phase0/r4-1-trigger-extension-evidence.md` + `docker/r4-1-poc/` (Tier-1 42종 trigger UDF 확장 + Docker 격리 환경 PoC PASS, ADR-011 §2.1 (b) 충족, 2026-05-06)
- R-5: ✅ **완료** — `docs/architecture/canary-recheck-design.md` (canary 재검증 트리거 설계, T13 강화 + R-4.1 catalog 재사용 + 6 trigger 시점 + 4 verdict + 4 안전장치 + Markdown+JSONL evidence + T1/T2/T3 정책 매트릭스, 2026-05-06)
- R-6: ✅ **완료** — `.github/workflows/r2-canary.yml` (CI/nightly canary regression workflow, ADR-011 §2.1 (d) 자동 회귀 검증 경로, 2026-05-06) + R-6 GitHub Actions actual run `25482284523` PASS (24초, verdict=PASS, 42/42 BLOCK, leak 0, 2026-05-07)
- R-7: ✅ **완료** — `docs/phase0/redaction-verification-sop.md` (Phase 1 acceptance SOP, 13 항목 checklist + 4 verdict + 9 ROLLBACK + 7 Evidence + push 전/후 작업 분리, 2026-05-06) + R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only (`docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md`, 2026-05-07) → **G1b CONDITIONALLY PASS → PASS 승격 + Phase 1 acceptance PARTIAL → PASS 선언**

#### 8.5.2 G1b PASS 이후 후속 작업 (2026-05-09 후속 1 ~ 후속 8 누적)


exec
/bin/bash -lc "python - <<'PY'
import re
old41 = re.compile(r'(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=["'^&'"\\s]+')
old42 = re.compile(r'(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=["'^&'"\\s]+')
new41 = re.compile(r'(?i)(?:"'^|[?&'"\\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=["'^&'"\\s]+')
new42 = re.compile(r'(?i)(?:"'^|[?&'"\\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=["'^&'"\\s]+')
cases = [
('sort lambda','failures.sort(key=lambda e: e.get(\"ts\", \"\"), reverse=True)'),
('sort named','failures.sort(key=_ts_key, reverse=True)'),
('dataclass','WorkerResult(exit_code=exit_code, stdout=out)'),
('query start','?api_key=fakecanary123'),
('query amp','&password=fakecanary123&x=1'),
('line form','password=fakecanary123&x=1'),
('header ws','Authorization: Bearer abc ; api_key=xxx'),
('url semicolon','https://x.test/path;api_key=abc'),
('json string','{\"api_key=abc\":\"not typical\"}'),
('multipart','Content-Disposition: form-data; name=\"api_key\"\\r\\n\\r\\nabc'),
('nested url encoded','redirect=https%3A%2F%2Fx%3Fapi_key%3Dabc'),
('inline quoted','url=\"https://x.test/?api_key=abc\"'),
]
for name, s in cases:
    print(name)
    for label, pat in [('old41',old41),('old42',old42),('new41',new41),('new42',new42)]:
        ms=[m.group(0) for m in pat.finditer(s)]
        print(' ', label, ms)
PY" in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc "rg -n \"access_token|refresh_token|id_token|api_key|apikey|client_secret|private_key|authorization|x-amz-signature|signature|session|password=|key=|code=\" docs/phase0/r4-1-trigger-extension-evidence.md tools tests src -S --glob '"'!docs/phase0/v1-poc-raw/**'"'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/phase0/r4-1-trigger-extension-evidence.md:118:  Authorization header (Bearer, IGNORECASE), Private key block,
docs/phase0/r4-1-trigger-extension-evidence.md:135:3. **canary 차단 보장**: H-J/H-L canary (T1-038, T1-040) 가 alternation T1-041/T1-042 에 의해 매칭 차단됨 (canary input 에 `access_token=` 포함, alternation 매칭 ✓).
docs/phase0/r4-1-trigger-extension-evidence.md:148:    OR NEW.content REGEXP '(?i)(?:access_token|refresh_token|...|x-amz-signature)=[^&\s]+'
docs/phase0/r4-1-trigger-extension-evidence.md:149:    OR NEW.content REGEXP '(?i)(?:access_token|refresh_token|...|key)=[^&\s]+'
docs/phase0/r4-1-trigger-extension-evidence.md:181:| T1-010 | Hermes #13 | BrowserBase | `bb_live_CANARYR41T010NOTAREAL session` | BLOCK | BLOCK | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:208:| T1-032 | Hermes H-A | ENV assignment | `export OPENAI_API_KEY=fakecanaryR41T032NOTAREAL` | BLOCK | BLOCK | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:209:| T1-033 | Hermes H-B | JSON field with secret keys | `config {"api_key": "fakecanaryR41T033NOTAREAL"} loaded` | BLOCK | BLOCK | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:210:| T1-034 | Hermes H-C | Authorization header (Bearer) | `headers Authorization: Bearer fakecanaryR41T034NOTAREAL ok` | BLOCK | BLOCK | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:214:| T1-038 | Hermes H-J | URL query secrets | `redirect https://example.com/cb?access_token=fakecanaryR41T038NOTAREAL&state=x` | BLOCK | BLOCK (via T1-041 alternation) | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:216:| T1-040 | Hermes H-L | Form-urlencoded body | `access_token=fakecanaryR41T040NOTAREAL&user=alice` | BLOCK | BLOCK (via T1-042 alternation) | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:222:| T1-041 | Hermes `_SENSITIVE_QUERY_PARAMS` | URL query sensitive keys (16) | `redirect https://x.com/cb?api_key=fakecanaryR41T041NOTAREAL&q=hi` | BLOCK | BLOCK | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:223:| T1-042 | Hermes `_SENSITIVE_BODY_KEYS` | Body/form sensitive keys (14) | `form payload password=fakecanaryR41T042NOTAREAL&user=alice` | BLOCK | BLOCK | PASS |
docs/phase0/r4-1-trigger-extension-evidence.md:238:| near-but-not-secret | `session_id_count is 5 and token_count is 100` | PASS | secret-like 변수명, 실제 secret 미포함 |
docs/phase0/r4-1-trigger-extension-evidence.md:280:  - `safe-cookie` (`Cookie: session=abc and lang=en`) ↔ T1-041 alternation `session=` 매칭
docs/phase0/r4-1-trigger-extension-evidence.md:289:| 2 | safe sample 정정: `safe-cookie` (Cookie session=) 제거, `safe-form-no-secret` (theme=&lang=&page=) 추가 | `Cookie: session=...` 의 `session=` 매칭은 Hermes 카탈로그 *의도된 매칭* — sensitive key frozenset 에 명시. safe sample 분류 자체를 정정. |
src/jarvis/worker.py:61:                exit_code=exit_code,
src/jarvis/worker.py:70:            exit_code=exit_code,
src/jarvis/worker.py:140:      - 흐름: new-session -d → send-keys(격리 wrap 된 inner cmd + sentinel) →
src/jarvis/worker.py:141:        capture-pane polling(sentinel 등장 시 종료) → kill-session(try/finally).
src/jarvis/worker.py:156:        session_prefix: str = "jarvis",
src/jarvis/worker.py:164:        self._session_prefix = session_prefix
src/jarvis/worker.py:168:        session = f"{self._session_prefix}-{uuid.uuid4().hex[:8]}"
src/jarvis/worker.py:174:            "tmux", "new-session", "-d", "-s", session, "-x", "200", "-y", "50",
src/jarvis/worker.py:178:                exit_code=new_rc or 1,
src/jarvis/worker.py:179:                output=f"tmux new-session 실패: {new_err}",
src/jarvis/worker.py:186:            self._tmux(["tmux", "send-keys", "-t", session, full_cmd, "Enter"])
src/jarvis/worker.py:187:            pane_text, sentinel_code = self._poll_for_sentinel(session)
src/jarvis/worker.py:189:            self._tmux(["tmux", "kill-session", "-t", session])
src/jarvis/worker.py:193:                exit_code=124,                            # 관행: timeout 코드
src/jarvis/worker.py:202:            exit_code=sentinel_code,
src/jarvis/worker.py:209:    def _poll_for_sentinel(self, session: str) -> tuple[str, int | None]:
src/jarvis/worker.py:213:            _, out, _ = self._tmux(["tmux", "capture-pane", "-p", "-t", session])
src/jarvis/worker.py:324:            exit_code=1, output=msg, cost_usd=None, is_error=True, raw=None,
tests/jarvis/test_ollama_worker.py:165:    sig = inspect.signature(OllamaWorker.__init__)
tests/jarvis/test_boss_advisory.py:153:    w = FakeWorker("claude", exit_code=1)
tests/jarvis/test_worker_result.py:4:1급, exit code=결정적 완료신호 + json 출력/total_cost_usd 비용신호).
tests/jarvis/test_worker_result.py:22:        "session_id": "abc",
tests/jarvis/test_worker_result.py:29:    r = WorkerResult.from_cli(exit_code=0, stdout=_claude_json())
tests/jarvis/test_worker_result.py:39:    r = WorkerResult.from_cli(exit_code=0, stdout=_claude_json(is_error=True))
tests/jarvis/test_worker_result.py:46:    r = WorkerResult.from_cli(exit_code=1, stdout=_claude_json(is_error=False))
tests/jarvis/test_worker_result.py:54:    r = WorkerResult.from_cli(exit_code=0, stdout="not-json-at-all")
tests/jarvis/test_worker_result.py:64:    r = WorkerResult.from_cli(exit_code=0, stdout=json.dumps(payload))
tests/jarvis/test_worker_result.py:70:    r = WorkerResult.from_cli(exit_code=0, stdout=_claude_json(session_id="xyz"))
tests/jarvis/test_worker_result.py:72:    assert r.raw["session_id"] == "xyz"
tests/fixtures/gp3_st2/README.md:28:| `fail/chmod_644/` | runtime `chmod 644 /run/secrets/mock_api_key` 시뮬레이션 | `IN_ATTRIB` 감지 / status `UNHEALTHY: IN_ATTRIB ...` / hermes-mock unhealthy |
tests/fixtures/gp3_st2/README.md:42:│   ├── mock_api_key     # fake canary (R-4.1 답습)
tests/jarvis/test_review_guard.py:15:    return WorkerResult(exit_code=0, output=output, cost_usd=0.0,
tools/schema_validator.py:145:ALLOWED_SCOPE_ENUM: tuple[str, ...] = ("global", "project", "session", "team")
tests/jarvis/test_tmux_worker.py:5:  - 흐름: new-session -d → send-keys → 완료 sentinel polling → capture-pane → kill-session.
tests/jarvis/test_tmux_worker.py:8:  - 세션 leak 방지: try/finally kill-session.
tests/jarvis/test_tmux_worker.py:26:                 new_session_exit: int = 0, send_keys_exit: int = 0,
tests/jarvis/test_tmux_worker.py:27:                 kill_session_exit: int = 0) -> None:
tests/jarvis/test_tmux_worker.py:31:        self._new_exit = new_session_exit
tests/jarvis/test_tmux_worker.py:33:        self._kill_exit = kill_session_exit
tests/jarvis/test_tmux_worker.py:38:        if sub == "new-session":
tests/jarvis/test_tmux_worker.py:44:        if sub == "kill-session":
tests/jarvis/test_tmux_worker.py:67:    assert subs[0] == "new-session"
tests/jarvis/test_tmux_worker.py:70:    assert subs[-1] == "kill-session"
tests/jarvis/test_tmux_worker.py:71:    assert subs.index("new-session") < subs.index("send-keys")
tests/jarvis/test_tmux_worker.py:73:    assert subs.index("capture-pane") < subs.index("kill-session")
tests/jarvis/test_tmux_worker.py:107:def test_kill_session_runs_even_when_capture_fails() -> None:
tests/jarvis/test_tmux_worker.py:108:    """capture-pane 자체가 실패해도 kill-session 발화(세션 leak 0)."""
tests/jarvis/test_tmux_worker.py:122:    assert "kill-session" in subs
tests/jarvis/test_tmux_worker.py:151:def test_new_session_failure_skips_send_and_capture() -> None:
tests/jarvis/test_tmux_worker.py:152:    """new-session 실패 시 send-keys / capture-pane 미호출 + is_error=True."""
tests/jarvis/test_tmux_worker.py:153:    spy = SpyTmuxRunner(pane_text="", new_session_exit=1)
src/jarvis/layer1.py:187:    failures.sort(key=lambda e: e.get("ts", ""), reverse=True)
src/jarvis/layer1.py:237:            report.flag_frequency.items(), key=lambda kv: (-kv[1], kv[0])
tests/jarvis/test_memory.py:40:        result=WorkerResult(exit_code=exit_code, output="ok", cost_usd=None,
tests/jarvis/test_orchestrator.py:52:    w = FakeWorker("claude", exit_code=1)
tests/jarvis/test_layer1.py:71:        _entry(status="worker_failed", applied=False, exit_code=1, is_error=True),
tests/jarvis/test_layer1.py:86:               applied=False, exit_code=1, is_error=True),
tests/jarvis/test_layer1.py:137:               status="worker_failed", applied=False, exit_code=1, is_error=True),
tests/jarvis/test_layer1.py:152:               status="worker_failed", applied=False, exit_code=1, is_error=True)
tests/fixtures/gp3_st2/fail/content_modified/README.md:9:3. `simulate.sh` 가 `/run/secrets/mock_api_key` 의 본문에 변조 문자열 append (예: ` # tampered`)
tests/fixtures/gp3_st2/fail/content_modified/README.md:11:5. status file 에 `UNHEALTHY: IN_MODIFY /run/secrets/mock_api_key <timestamp>` 기록
tests/fixtures/gp3_st2/fail/content_modified/README.md:19:| sidecar status file | `UNHEALTHY: IN_MODIFY /run/secrets/mock_api_key <ISO8601>` |
tests/fixtures/gp3_st2/fail/content_modified/README.md:33:├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_*
tools/history_anchor_verifier.py:77:    ("anchor_tampered", "Anchor 자체 변조 (signature 부재 시 한계 — known limitation)"),
tests/jarvis/test_cli_worker.py:102:                  isolation=PassthroughIsolation(), runner=_runner({}, exit_code=2))
tests/jarvis/test_ollama_boss.py:116:    sig = inspect.signature(OllamaBoss.__init__)
tests/fixtures/gp3_st2/fail/content_modified/simulate.sh:18:#   - sidecar status file = "UNHEALTHY: IN_MODIFY /run/secrets/mock_api_key <ts>"
tests/fixtures/gp3_st2/fail/content_modified/simulate.sh:23:TARGET="${1:-/run/secrets/mock_api_key}"
tests/fixtures/gp3_st2/fail/chmod_644/README.md:9:3. `simulate.sh` 가 `/run/secrets/mock_api_key` 의 권한을 644 로 변경 (`chmod 644`)
tests/fixtures/gp3_st2/fail/chmod_644/README.md:11:5. status file 에 `UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <timestamp>` 기록
tests/fixtures/gp3_st2/fail/chmod_644/README.md:19:| sidecar status file | `UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <ISO8601>` |
tests/fixtures/gp3_st2/fail/chmod_644/README.md:32:├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_* (R-4.1 답습) — 초기 권한 0600 (정상 docker secret 기본값 시뮬레이션)
tools/jsonl_hash_chain.py:61:ALLOWED_SCOPES: tuple[str, ...] = ("global", "project", "session")
tests/fixtures/gp3_st2/fail/chmod_644/simulate.sh:18:#   - sidecar status file = "UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <ts>"
tests/fixtures/gp3_st2/fail/chmod_644/simulate.sh:23:TARGET="${1:-/run/secrets/mock_api_key}"
tools/secret_scanner.py:140:     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
tools/secret_scanner.py:141:    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
tools/secret_scanner.py:142:     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
tools/secret_scanner.py:156:     r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
tools/secret_scanner.py:158:     r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
tools/secret_scanner.py:215:    예: `OPENAI_API_KEY=[REDACTED]` 의 H-A regex 매칭은 [REDACTED] marker → 위반 미카운트.
tools/boundary_guard.py:324:    # Track id → first scope seen (for #3 session→global transition detection)
tools/boundary_guard.py:340:        # #3: Session memory → Global memory 자동 승격
tools/boundary_guard.py:345:            if prev_scope == "session" and scope == "global":
tools/boundary_guard.py:347:                    file_path, idx, "session-to-global", "memory-skill-boundary",
tools/boundary_guard.py:348:                    f"entry[{idx}] id={entry_id!r} scope transition session → global (G4 §5.2 #3 위반)"
tools/boundary_guard.py:388:        ("#3", "Session memory → Global memory 자동 승격"),
tests/fixtures/gp3_st2/fail/file_deleted/README.md:9:3. `simulate.sh` 가 `/run/secrets/mock_api_key` 를 `rm` 으로 삭제
tests/fixtures/gp3_st2/fail/file_deleted/README.md:11:5. status file 에 `UNHEALTHY: IN_DELETE_SELF /run/secrets/mock_api_key <timestamp>` 기록
tests/fixtures/gp3_st2/fail/file_deleted/README.md:19:| sidecar status file | `UNHEALTHY: IN_DELETE_SELF /run/secrets/mock_api_key <ISO8601>` |
tests/fixtures/gp3_st2/fail/file_deleted/README.md:39:├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_*
tests/fixtures/gp3_st2/fail/file_deleted/simulate.sh:18:#   - sidecar status file = "UNHEALTHY: IN_DELETE_SELF /run/secrets/mock_api_key <ts>"
tests/fixtures/gp3_st2/fail/file_deleted/simulate.sh:23:TARGET="${1:-/run/secrets/mock_api_key}"
tests/fixtures/gp3_st2/pass/init_phase/README.md:34:├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_* (R-4.1 답습)
tests/fixtures/gp3_st2/pass/normal_operation/README.md:24:├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_* (R-4.1 답습)
tests/fixtures/secret_hygiene/fail/env_assignment.py:5:OPENAI_API_KEY = "sk-FAKE-GROUP-D-NOT-A-REAL-SECRET"
tests/fixtures/secret_hygiene/fail/env_assignment.py:6:ANTHROPIC_API_KEY = "sk-ant-FAKEGROUPDNOTAREALSECRETXX"
tests/fixtures/secret_hygiene/fail/json_field.json:3:  "api_key": "ghp_FAKE_GROUP_D_NOT_REAL_TOKEN",
tests/fixtures/secret_hygiene/fail/json_field.json:4:  "redirect_url": "https://example.com/oauth/cb?access_token=fakecanaryR41T-NOTAREAL&state=x",
tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt:2:OPENAI_API_KEY=[REDACTED]
tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt:3:ANTHROPIC_API_KEY=[REDACTED]
tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt:5:AWS_ACCESS_KEY=[REDACTED]
tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt:6:Authorization: [REDACTED]
tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py:5:# api_key / password / token keyword assignment — KeywordDetector 검출 대상
tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py:6:api_key = "sk-FAKES3NOTAREALSECRETXX"
tests/fixtures/secret_hygiene/redaction_fail/partial_redact.txt:2:OPENAI_API_KEY=sk-FAKE-GROUP-D-NOT-A-REAL-SECRET
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py:4:# 본 fixture 는 기존 fail/ fixture (env_assignment / json_field / prefix_aws / private_key_block)
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py:11:# H-C (T1-034) — Authorization Bearer
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py:12:AUTH_HEADER_EXAMPLE = "Authorization: Bearer FAKEBEARERMVP1ENTRYNOTAREAL123"
tests/fixtures/memory_skill_migration/lossy/hermes_to_claude_memory.jsonl:2:{"type": "memory", "scope": "project", "id": "88888888-8888-4888-8888-888888888888", "schema_version": "0.1", "ts": "2026-05-10T12:05:00Z", "agent": "user", "event": "memory_write", "content": {"key": "session_id", "value": "session-2026-05-10-a"}, "evidence_refs": ["docs/evidence/group-f-lossy.md"], "_hermes_internal_id": "h-bbb-002", "prev_hash": "3159db7dacae14f8ea53f464c55de78daab62b56c82b68f608d1025d7c1d4a4d", "hash": "e47cffb379ecc4097af59ed2290fc1d258efbb58400bc05a724cdf2cec10132e"}
tests/fixtures/memory_skill_migration/fail/chain_violation_memory.jsonl:1:{"type": "memory", "scope": "session", "id": "99999999-9999-4999-8999-999999999999", "schema_version": "0.1", "ts": "2026-05-10T13:00:00Z", "agent": "user", "event": "memory_write", "content": {"key": "first", "value": "intact"}, "evidence_refs": ["docs/evidence/group-f-fail.md"], "prev_hash": "b67a87dffb1f40fe49af46a5559f026a884f5ae37eb622ee8fbb9f1913888ae7", "hash": "28ff893d32609c518e7db0978a225f7b31233680a93db51f7a3e8f8c38ffbf96"}
tests/fixtures/memory_skill_migration/fail/chain_violation_memory.jsonl:2:{"type": "memory", "scope": "session", "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa", "schema_version": "0.1", "ts": "2026-05-10T13:05:00Z", "agent": "user", "event": "memory_write", "content": {"key": "second", "value": "tampered_chain"}, "evidence_refs": ["docs/evidence/group-f-fail.md"], "prev_hash": "0000000000000000000000000000000000000000000000000000000000000000", "hash": "4d32ee662603d1322a3130e3adc6ee42fd16fc80ba9076517440b9a9b2a2099f"}
tests/fixtures/boundary_guard/memory_skill_boundary/fail/session_to_global_promotion.jsonl:1:{"type": "memory", "scope": "session", "id": "33333333-3333-4333-8333-333333333333", "schema_version": "0.1", "ts": "2026-05-10T10:00:00Z", "agent": "user", "event": "memory_write", "content": {"key": "ephemeral_state", "value": "session-only data"}, "evidence_refs": [], "prev_hash": "fakeprev0000000000000000000000000000000000000000000000000000000a", "hash": "fakehash0000000000000000000000000000000000000000000000000000000c"}
tests/fixtures/boundary_guard/memory_skill_boundary/fail/session_to_global_promotion.jsonl:2:{"type": "memory", "scope": "global", "id": "33333333-3333-4333-8333-333333333333", "schema_version": "0.1", "ts": "2026-05-10T10:05:00Z", "agent": "user", "event": "memory_write", "content": {"key": "ephemeral_state", "value": "session-only data, auto-promoted to global"}, "evidence_refs": [], "prev_hash": "fakehash0000000000000000000000000000000000000000000000000000000c", "hash": "fakehash0000000000000000000000000000000000000000000000000000000d"}

exec
/bin/bash -lc "python3 - <<'PY'
import re
old41 = re.compile(r'(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=["'^&'"\\s]+')
old42 = re.compile(r'(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=["'^&'"\\s]+')
new41 = re.compile(r'(?i)(?:"'^|[?&'"\\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=["'^&'"\\s]+')
new42 = re.compile(r'(?i)(?:"'^|[?&'"\\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=["'^&'"\\s]+')
cases = [
('sort lambda','failures.sort(key=lambda e: e.get(\"ts\", \"\"), reverse=True)'),
('sort named','failures.sort(key=_ts_key, reverse=True)'),
('dataclass','WorkerResult(exit_code=exit_code, stdout=out)'),
('query start','?api_key=fakecanary123'),
('query amp','&password=fakecanary123&x=1'),
('line form','password=fakecanary123&x=1'),
('header ws','Authorization: Bearer abc ; api_key=xxx'),
('url semicolon','https://x.test/path;api_key=abc'),
('inline quoted','url=\"https://x.test/?api_key=abc\"'),
('multipart','Content-Disposition: form-data; name=\"api_key\"\\r\\n\\r\\nabc'),
('nested url encoded','redirect=https%3A%2F%2Fx%3Fapi_key%3Dabc'),
('cookie session','Cookie: session=abc; lang=en'),
]
for name, s in cases:
    print(name)
    for label, pat in [('old41',old41),('old42',old42),('new41',new41),('new42',new42)]:
        ms=[m.group(0) for m in pat.finditer(s)]
        print(' ', label, ms)
PY" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
sort lambda
  old41 ['key=lambda']
  old42 ['key=lambda']
  new41 []
  new42 []
sort named
  old41 ['key=_ts_key,']
  old42 ['key=_ts_key,']
  new41 []
  new42 []
dataclass
  old41 ['code=exit_code,']
  old42 []
  new41 []
  new42 []
query start
  old41 ['api_key=fakecanary123']
  old42 ['api_key=fakecanary123']
  new41 ['?api_key=fakecanary123']
  new42 ['?api_key=fakecanary123']
query amp
  old41 ['password=fakecanary123']
  old42 ['password=fakecanary123']
  new41 ['&password=fakecanary123']
  new42 ['&password=fakecanary123']
line form
  old41 ['password=fakecanary123']
  old42 ['password=fakecanary123']
  new41 ['password=fakecanary123']
  new42 ['password=fakecanary123']
header ws
  old41 ['api_key=xxx']
  old42 ['api_key=xxx']
  new41 [' api_key=xxx']
  new42 [' api_key=xxx']
url semicolon
  old41 ['api_key=abc']
  old42 ['api_key=abc']
  new41 []
  new42 []
inline quoted
  old41 ['api_key=abc"']
  old42 ['api_key=abc"']
  new41 ['?api_key=abc"']
  new42 ['?api_key=abc"']
multipart
  old41 []
  old42 []
  new41 []
  new42 []
nested url encoded
  old41 []
  old42 []
  new41 []
  new42 []
cookie session
  old41 ['session=abc;']
  old42 []
  new41 [' session=abc;']
  new42 []

codex
# (b1-PC1-D6-false-positives) Codex (OpenAI) cross-validation 응답

## §1 자격 검증 (brief 답습 정확성)

검토 대상은 `docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` v1.1 이다.

현 구현 위치는 `tools/secret_scanner.py` 의 `ALTERNATION_PATTERNS` 이다.

현재 T1-041/T1-042 는 alternation 앞에 경계 조건이 없다.

따라서 `key=lambda` 와 `code=exit_code` 를 source code 내부에서 그대로 secret-like `key=value` 로 오인한다.

brief 의 false-positive 원인 분석은 정확하다.

`key` 는 T1-041/T1-042 양쪽에 있다.

`code` 는 T1-041 에만 있다.

그래서 `layer1.py` 의 `key=lambda` 는 2개 패턴 모두에 걸리고, `worker.py` 의 `exit_code=...` 는 T1-041 에만 걸린다.

brief 가 제시한 “10건” 구조와 정합적이다.

R-4.1 evidence 의 §5.3 도 확인했다.

T1-041 canary 는 `?api_key=...` 이다.

T1-042 canary 는 whitespace 뒤 `password=...` form payload 이다.

즉 brief 의 핵심 검증 축은 “query 시작 `?` / query separator `&` / line-start body / whitespace body” 보존이다.

`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` line 94 인용 취지도 확인했다.

신규 hook, Tier catalog, provider policy, security gate 류는 풀 3+1 이고, 단순 version pin 은 단축 합의라는 차등 원칙이다.

이번 변경은 version pin 이 아니다.

또한 hook 추가도 아니다.

정확한 분류는 “기존 Tier-1 catalog 패턴 본문 정정”이다.

따라서 최소한 외부 LLM cross-validation 대상이라는 brief 판단은 타당하다.

합의 수준은 프로젝트 governance 상 풀 3+1 로 분류하는 쪽이 보수적으로 맞다.

단, 기술적 변경 폭은 매우 작고, Hermes key set 보존형 결함 정정이라는 점은 단축 합의 후보성을 일부 만든다.

결론적으로 brief 의 자격 framing 은 대체로 정확하다.

다만 “word boundary”라는 표현은 엄밀히는 부정확하다.

제안 패턴 `(?:^|[?&\s])` 는 regex word boundary `\b` 가 아니다.

정확한 표현은 “left-context delimiter prefix” 또는 “좌측 문맥 prefix” 이다.

이 용어 문제는 BLOCKING 은 아니나, 합의 문서에는 정정하는 것이 좋다.

## §2 (a) 정정 정확성 평가

제안 패턴은 다음이다.

```python
r"(?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"
r"(?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"
```

Python `re` engine 기준 문법 오류는 없다.

Inline flag `(?i)` 는 패턴 시작에 있으므로 유효하다.

Non-capturing group `(?:^|[?&\s])` 도 정상이다.

`\s` 는 Python `re` 에서 space, tab, CR, LF 등을 포함한다.

따라서 whitespace 뒤 key-value 를 잡는 의도는 충족한다.

실측 결과는 brief §4.2 의 7개 시나리오와 일치한다.

```text
failures.sort(key=lambda ...)                  -> new T1-041/T1-042 match 0
failures.sort(key=_ts_key, ...)                -> new T1-041/T1-042 match 0
WorkerResult(exit_code=exit_code, ...)         -> new T1-041/T1-042 match 0
?api_key=fakecanary123                         -> BLOCK
&password=fakecanary123&x=1                    -> BLOCK
password=fakecanary123&x=1                     -> BLOCK
Authorization: Bearer abc ; api_key=xxx        -> BLOCK
```

이 변경은 Python keyword arg 의 대표 FP 를 해소한다.

이 변경은 T1-038/T1-040 의 현재 canary cover 를 보존한다.

이 변경은 Hermes upstream key 목록을 삭제하거나 rename 하지 않는다.

그러므로 “키 목록 보존”이라는 답습 본질은 유지된다.

다만 match substring 이 바뀐다.

예: 기존은 `api_key=xxx` 만 match 했다.

변경 후는 `?api_key=xxx` 또는 ` api_key=xxx` 처럼 delimiter 를 포함해 match 한다.

현재 scanner 가 “검출 여부” 중심이면 문제 없다.

그러나 redaction 위치, reporting text, dedup key 를 match 원문에 의존한다면 prefix 포함이 side effect 가 될 수 있다.

이 repo 의 현재 secret-scanner 흐름에서는 BLOCK 여부 관점이 핵심이라 BLOCKING 으로 보지는 않는다.

하지만 regression test 에서는 “검출 여부”와 함께 “match 값에 prefix 포함 가능”을 명시해야 한다.

중요한 추가 발견이 있다.

제안 (a)는 quoted form body string 을 놓친다.

예시는 다음이다.

```python
payload = "password=fakecanary&user=alice"
body = 'api_key=fakecanary&x=1'
```

이 경우 key 직전 문자가 quote 이므로 `(?:^|[?&\s])` 에 맞지 않는다.

기존 패턴은 이를 잡았다.

새 패턴은 놓친다.

source scanner 관점에서는 실제로 중요한 FN risk 다.

`curl -d password=...` 처럼 quote 없이 whitespace 뒤에 오는 form body 는 잡는다.

하지만 `curl -d 'password=...'` 와 Python/JSON/YAML 의 quoted literal 은 새 패턴에서 빠진다.

따라서 (a) 원안은 CI RED 해소 목적에는 정확하지만, source-code hardcoded form body cover 를 일부 축소한다.

권고 대안은 (a+) 이다.

```python
r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s'\"\)]+"
r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s'\"\)]+"
```

단, 위 (a+) 는 예시 권고이며 그대로 채택 전 별도 테스트가 필요하다.

핵심은 좌측 delimiter 에 quote 를 추가하는 것이다.

우측 value terminator 에 quote 를 추가하는 것도 reporting 품질상 좋다.

`(` 를 좌측 delimiter 에 넣으면 `sort(key=...)` FP 가 재발하므로 넣으면 안 된다.

즉 원안 (a)는 “현재 7개 시나리오” 기준 PASS 이다.

그러나 source string 내 form-urlencoded secret cover 까지 보존하려면 revision 이 필요하다.

## §3 7 항목 평가 매트릭스

| # | 평가 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 정규식 정정 정확성 | PASS with NOTE | Python keyword arg FP 10건은 해소된다. `?`, `&`, `^`, `\s` canary cover 는 유지된다. 단 “word boundary”가 아니라 delimiter prefix 이다. |
| 2 | Hermes upstream 답습 본질 유지 | PASS | `_SENSITIVE_QUERY_PARAMS` 16 keys 와 `_SENSITIVE_BODY_KEYS` 14 keys 는 삭제/변경되지 않는다. |
| 3 | T1-038/T1-040 canary cover 보존 | PASS | R-4.1 §5.3 의 `?api_key=...`, `password=...` 형태는 변경 후에도 BLOCK 된다. |
| 4 | 추가 edge cases / FN risk | REVISE | quoted body string `payload = "password=..."`, shell `-d 'password=...'` 는 원안 (a) 에서 놓칠 수 있다. |
| 5 | ADR-011 §2.1 (a)~(e) 영향 | PASS | 목적은 DB/source secret persistence 차단 회귀 검증 강화이며, 본 cycle 은 PC-1-T3 (b)(d) 회귀 자격 보강 한정으로 볼 수 있다. |
| 6 | R-7(b) PC1-2 차등 자격 | PASS | version pin 이 아니라 Tier-1 scanner pattern 본문 변경이므로 단순 단축 합의로 취급하면 약하다. 풀 3+1 또는 최소 외부 LLM 포함 합의가 적정하다. |
| 7 | 더 나은 대안 | REVISE 권고 | (a) 를 기본으로 하되 quote-delimited form body 를 보존하는 (a+) 또는 focused regression test 추가가 낫다. |

## §4 추가 발견 (있을 시) — BLOCKING / 권고 / NOTE 분류

### BLOCKING

B-1. 원안 (a)는 quoted form-urlencoded body literal 을 놓칠 수 있다.

예시는 다음이다.

```python
payload = "password=fakecanaryR41T042NOTAREAL&user=alice"
payload = 'api_key=fakecanaryR41T041NOTAREAL&q=hi'
```

이 문자열들은 source scanner 가 잡아야 할 가능성이 높은 hardcoded secret 형태다.

기존 패턴은 잡는다.

원안 (a)는 key 직전이 quote 이므로 잡지 못한다.

R-4.1 §5.3 의 canary 는 unquoted text 라서 이 회귀를 드러내지 않는다.

따라서 구현 전 regression case 에 quoted literal 을 추가해야 한다.

또는 좌측 delimiter 에 `'` / `"` 를 포함하는 보강안을 채택해야 한다.

### 권고

R-1. brief 의 “word boundary” 표현을 “left-context delimiter prefix” 로 정정 권고한다.

`(?:^|[?&\s])` 는 `\b` boundary 가 아니다.

합의 문서가 regex 의미를 정확히 써야 이후 재검토 비용이 줄어든다.

R-2. 패턴 변경과 함께 최소 regression test 를 추가해야 한다.

권고 test cases 는 다음이다.

```python
# should not match
"failures.sort(key=lambda e: e.get('ts', ''), reverse=True)"
"failures.sort(key=_ts_key, reverse=True)"
"WorkerResult(exit_code=exit_code, stdout=out)"
"dict(key=value)"
"fn(code=exit_code)"

# should match
"?api_key=fakecanary"
"&password=fakecanary&x=1"
"password=fakecanary&x=1"
"Authorization: Bearer abc ; api_key=fakecanary"
"payload = \"password=fakecanary&user=alice\""
"body = 'api_key=fakecanary&q=hi'"
```

R-3. match value 에 prefix 가 포함되는 점을 test expectation 에 반영해야 한다.

예: 변경 후 `?api_key=...` 전체가 match 된다.

이것이 reporting/redaction output 에 영향을 주지 않는지 확인해야 한다.

R-4. value terminator 를 `[^&\s]+` 로 유지하면 quote, comma, closing paren 이 value 에 포함될 수 있다.

현 FP 해소에는 충분하지만 reporting 품질은 낮다.

예: 기존 테스트에서 old pattern 은 `key=_ts_key,` 처럼 comma 를 포함했다.

보강안에서는 `[^&\s'"\),]+` 같은 terminator 개선을 검토할 수 있다.

단 terminator 변경은 탐지 범위에 영향이 있으므로 별도 합의/test 가 필요하다.

R-5. semicolon delimiter 는 별도 검토 대상이다.

`https://x.test/path;api_key=abc` 또는 cookie-like `; session=abc` 는 원안 (a) 에서 일부 놓치거나 whitespace 위치에 따라 다르게 동작한다.

현 R-4.1 canary 범위 밖이므로 이번 cycle 의 BLOCKING 으로 올리지는 않는다.

다만 URL path parameter / legacy query separator / cookie header 를 어느 범주로 볼지 후속 scanner audit 에 넣는 것이 좋다.

R-6. (b) hook exclude 는 권고하지 않는다.

`src/` 또는 `.py` 를 제외하면 hardcoded URL/query/body secret 을 놓칠 수 있다.

CI RED 해소에는 빠르지만 scanner 의 본질을 약화한다.

R-7. (c) source 회피는 권고하지 않는다.

`sort(key=...)` 는 Python 의 정상 API 이고, 이를 회피하려는 변경은 코드 품질을 악화시킨다.

또 `key` keyword 자체를 피할 방법이 사실상 없다.

R-8. (d) AST SAFE_CONTEXT 는 장기적으로 가장 정밀하지만 이번 sub-cycle 에는 과하다.

Python AST 로 call keyword arg 를 skip 하는 방식은 좋지만, scanner 가 Python 외 source/doc/log 도 다루므로 복잡도와 테스트 부담이 커진다.

이번에는 regex delimiter 정정 + regression test 가 현실적이다.

R-9. (e) `.py` alternation skip 은 권고하지 않는다.

`.py` 에 hardcoded URL, form body, header sample 이 들어갈 수 있다.

source scanner 의 방어 범위를 불필요하게 줄인다.

### NOTE

N-1. `\s` 는 newline 도 포함한다.

따라서 multi-line text 에서 newline 직후 `api_key=...` 는 match 된다.

이는 대체로 의도에 맞다.

N-2. `^` 는 `re.MULTILINE` 없이 문자열 전체 시작만 의미한다.

line-by-line scan 이면 각 line 시작으로 동작한다.

whole-file scan 이면 파일 전체 첫 위치만 `^` 이다.

scanner 가 파일을 line 단위로 순회한다면 문제 없다.

whole-file scan 이면 line-start form body cover 는 `(?m:^|[?&\s])` 또는 `(?:^|(?<=\n)|[?&\s])` 관점 확인이 필요하다.

N-3. 이번 정정은 Hermes key 목록 보존형이다.

따라서 Hermes upstream 답습 본질 손상은 없다.

N-4. T1-041/T1-042 직접 등록 제외인 T1-038/T1-040 canary cover 를 alternation 으로 유지한다는 설계 자체는 보존된다.

N-5. 기존 safe-cookie 논의상 `session=` 은 Hermes catalog 에서 sensitive 로 취급된다.

따라서 cookie/session FP 여부는 이번 cycle 의 Python keyword arg FP 와 분리해야 한다.

## §5 최종 권고 (APPROVE / REVISE / REJECT + 근거)

최종 판정: **REVISE**

REJECT 는 아니다.

원안 (a)는 brief 가 제시한 7개 verification scenario 를 모두 만족한다.

CI RED 를 만든 Python keyword arg false positive 도 정확히 제거한다.

Hermes key 목록도 보존한다.

T1-038/T1-040 의 현재 canary cover 도 유지한다.

그러나 그대로 APPROVE 하기에는 quoted form-urlencoded body literal FN risk 가 있다.

특히 이 scanner 는 source code 를 scan 하므로 다음 형태는 실질적으로 중요하다.

```python
payload = "password=fakecanary&user=alice"
body = 'api_key=fakecanary&q=hi'
```

원안 (a)는 이 형태를 놓친다.

따라서 구현 전 brief 또는 구현안에 다음 중 하나를 반영하는 조건부 승인 흐름을 권고한다.

1. (a+) 로 보강: 좌측 delimiter 에 quote 를 추가한다.
2. quoted body literal regression test 를 추가하고, 원안 (a)의 FN 을 의도적 tradeoff 로 명시 승인한다.
3. 이번 cycle 은 원안 (a) 로 CI RED 만 해소하되, quoted literal cover 회귀를 별도 BLOCKING carry-over 로 즉시 등록한다.

내 권고는 1번이다.

즉 `(?:^|[?&\s'"])` 계열로 보강하고, `(` 는 delimiter 에 넣지 않는다.

이렇게 하면 `sort(key=...)` / `exit_code=...` FP 는 재발하지 않으면서 quoted body string cover 를 상당 부분 회복한다.

합의 자격은 “기존 Tier-1 alternation pattern 본문 정정”이다.

version pin 이 아니므로 R-7(b) PC1-2 상 단순 단축 합의로 낮추는 것은 약하다.

풀 3+1 + 외부 LLM 1+ 가 가장 보수적으로 정확하다.

다만 사용자 명시 + 외부 LLM cross-validation + regression evidence 가 있으면, 결함 정정 한정 단축 합의도 운영상 방어 가능하다.

## §6 자기진단

검토한 local source 는 다음이다.

`tools/secret_scanner.py` 의 T1-041/T1-042 현 패턴을 확인했다.

`docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` v1.1 의 scope, 후보, 7개 verification scenario 를 확인했다.

`docs/phase0/r4-1-trigger-extension-evidence.md` §5.3 의 T1-041/T1-042 canary 를 확인했다.

`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` line 94 주변의 R-7(b) 차등 취지를 확인했다.

`docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 의 (a)~(d), 후속 (e) 운영조건 framing 을 확인했다.

Python `re` 로 원안 (a)의 대표 case 를 직접 검증했다.

확인된 PASS 는 brief 의 7개 scenario 와 일치한다.

추가로 확인된 주요 risk 는 quoted form body literal FN 이다.

내 판정은 이 risk 를 근거로 APPROVE 가 아니라 REVISE 이다.

본 응답은 코드 변경을 수행하지 않았다.

본 응답은 cross-validation 의견 제출만 수행했다.
tokens used
55,291
# (b1-PC1-D6-false-positives) Codex (OpenAI) cross-validation 응답

## §1 자격 검증 (brief 답습 정확성)

검토 대상은 `docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` v1.1 이다.

현 구현 위치는 `tools/secret_scanner.py` 의 `ALTERNATION_PATTERNS` 이다.

현재 T1-041/T1-042 는 alternation 앞에 경계 조건이 없다.

따라서 `key=lambda` 와 `code=exit_code` 를 source code 내부에서 그대로 secret-like `key=value` 로 오인한다.

brief 의 false-positive 원인 분석은 정확하다.

`key` 는 T1-041/T1-042 양쪽에 있다.

`code` 는 T1-041 에만 있다.

그래서 `layer1.py` 의 `key=lambda` 는 2개 패턴 모두에 걸리고, `worker.py` 의 `exit_code=...` 는 T1-041 에만 걸린다.

brief 가 제시한 “10건” 구조와 정합적이다.

R-4.1 evidence 의 §5.3 도 확인했다.

T1-041 canary 는 `?api_key=...` 이다.

T1-042 canary 는 whitespace 뒤 `password=...` form payload 이다.

즉 brief 의 핵심 검증 축은 “query 시작 `?` / query separator `&` / line-start body / whitespace body” 보존이다.

`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` line 94 인용 취지도 확인했다.

신규 hook, Tier catalog, provider policy, security gate 류는 풀 3+1 이고, 단순 version pin 은 단축 합의라는 차등 원칙이다.

이번 변경은 version pin 이 아니다.

또한 hook 추가도 아니다.

정확한 분류는 “기존 Tier-1 catalog 패턴 본문 정정”이다.

따라서 최소한 외부 LLM cross-validation 대상이라는 brief 판단은 타당하다.

합의 수준은 프로젝트 governance 상 풀 3+1 로 분류하는 쪽이 보수적으로 맞다.

단, 기술적 변경 폭은 매우 작고, Hermes key set 보존형 결함 정정이라는 점은 단축 합의 후보성을 일부 만든다.

결론적으로 brief 의 자격 framing 은 대체로 정확하다.

다만 “word boundary”라는 표현은 엄밀히는 부정확하다.

제안 패턴 `(?:^|[?&\s])` 는 regex word boundary `\b` 가 아니다.

정확한 표현은 “left-context delimiter prefix” 또는 “좌측 문맥 prefix” 이다.

이 용어 문제는 BLOCKING 은 아니나, 합의 문서에는 정정하는 것이 좋다.

## §2 (a) 정정 정확성 평가

제안 패턴은 다음이다.

```python
r"(?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"
r"(?i)(?:^|[?&\s])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"
```

Python `re` engine 기준 문법 오류는 없다.

Inline flag `(?i)` 는 패턴 시작에 있으므로 유효하다.

Non-capturing group `(?:^|[?&\s])` 도 정상이다.

`\s` 는 Python `re` 에서 space, tab, CR, LF 등을 포함한다.

따라서 whitespace 뒤 key-value 를 잡는 의도는 충족한다.

실측 결과는 brief §4.2 의 7개 시나리오와 일치한다.

```text
failures.sort(key=lambda ...)                  -> new T1-041/T1-042 match 0
failures.sort(key=_ts_key, ...)                -> new T1-041/T1-042 match 0
WorkerResult(exit_code=exit_code, ...)         -> new T1-041/T1-042 match 0
?api_key=fakecanary123                         -> BLOCK
&password=fakecanary123&x=1                    -> BLOCK
password=fakecanary123&x=1                     -> BLOCK
Authorization: Bearer abc ; api_key=xxx        -> BLOCK
```

이 변경은 Python keyword arg 의 대표 FP 를 해소한다.

이 변경은 T1-038/T1-040 의 현재 canary cover 를 보존한다.

이 변경은 Hermes upstream key 목록을 삭제하거나 rename 하지 않는다.

그러므로 “키 목록 보존”이라는 답습 본질은 유지된다.

다만 match substring 이 바뀐다.

예: 기존은 `api_key=xxx` 만 match 했다.

변경 후는 `?api_key=xxx` 또는 ` api_key=xxx` 처럼 delimiter 를 포함해 match 한다.

현재 scanner 가 “검출 여부” 중심이면 문제 없다.

그러나 redaction 위치, reporting text, dedup key 를 match 원문에 의존한다면 prefix 포함이 side effect 가 될 수 있다.

이 repo 의 현재 secret-scanner 흐름에서는 BLOCK 여부 관점이 핵심이라 BLOCKING 으로 보지는 않는다.

하지만 regression test 에서는 “검출 여부”와 함께 “match 값에 prefix 포함 가능”을 명시해야 한다.

중요한 추가 발견이 있다.

제안 (a)는 quoted form body string 을 놓친다.

예시는 다음이다.

```python
payload = "password=fakecanary&user=alice"
body = 'api_key=fakecanary&x=1'
```

이 경우 key 직전 문자가 quote 이므로 `(?:^|[?&\s])` 에 맞지 않는다.

기존 패턴은 이를 잡았다.

새 패턴은 놓친다.

source scanner 관점에서는 실제로 중요한 FN risk 다.

`curl -d password=...` 처럼 quote 없이 whitespace 뒤에 오는 form body 는 잡는다.

하지만 `curl -d 'password=...'` 와 Python/JSON/YAML 의 quoted literal 은 새 패턴에서 빠진다.

따라서 (a) 원안은 CI RED 해소 목적에는 정확하지만, source-code hardcoded form body cover 를 일부 축소한다.

권고 대안은 (a+) 이다.

```python
r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s'\"\)]+"
r"(?i)(?:^|[?&\s'\"])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s'\"\)]+"
```

단, 위 (a+) 는 예시 권고이며 그대로 채택 전 별도 테스트가 필요하다.

핵심은 좌측 delimiter 에 quote 를 추가하는 것이다.

우측 value terminator 에 quote 를 추가하는 것도 reporting 품질상 좋다.

`(` 를 좌측 delimiter 에 넣으면 `sort(key=...)` FP 가 재발하므로 넣으면 안 된다.

즉 원안 (a)는 “현재 7개 시나리오” 기준 PASS 이다.

그러나 source string 내 form-urlencoded secret cover 까지 보존하려면 revision 이 필요하다.

## §3 7 항목 평가 매트릭스

| # | 평가 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 정규식 정정 정확성 | PASS with NOTE | Python keyword arg FP 10건은 해소된다. `?`, `&`, `^`, `\s` canary cover 는 유지된다. 단 “word boundary”가 아니라 delimiter prefix 이다. |
| 2 | Hermes upstream 답습 본질 유지 | PASS | `_SENSITIVE_QUERY_PARAMS` 16 keys 와 `_SENSITIVE_BODY_KEYS` 14 keys 는 삭제/변경되지 않는다. |
| 3 | T1-038/T1-040 canary cover 보존 | PASS | R-4.1 §5.3 의 `?api_key=...`, `password=...` 형태는 변경 후에도 BLOCK 된다. |
| 4 | 추가 edge cases / FN risk | REVISE | quoted body string `payload = "password=..."`, shell `-d 'password=...'` 는 원안 (a) 에서 놓칠 수 있다. |
| 5 | ADR-011 §2.1 (a)~(e) 영향 | PASS | 목적은 DB/source secret persistence 차단 회귀 검증 강화이며, 본 cycle 은 PC-1-T3 (b)(d) 회귀 자격 보강 한정으로 볼 수 있다. |
| 6 | R-7(b) PC1-2 차등 자격 | PASS | version pin 이 아니라 Tier-1 scanner pattern 본문 변경이므로 단순 단축 합의로 취급하면 약하다. 풀 3+1 또는 최소 외부 LLM 포함 합의가 적정하다. |
| 7 | 더 나은 대안 | REVISE 권고 | (a) 를 기본으로 하되 quote-delimited form body 를 보존하는 (a+) 또는 focused regression test 추가가 낫다. |

## §4 추가 발견 (있을 시) — BLOCKING / 권고 / NOTE 분류

### BLOCKING

B-1. 원안 (a)는 quoted form-urlencoded body literal 을 놓칠 수 있다.

예시는 다음이다.

```python
payload = "password=fakecanaryR41T042NOTAREAL&user=alice"
payload = 'api_key=fakecanaryR41T041NOTAREAL&q=hi'
```

이 문자열들은 source scanner 가 잡아야 할 가능성이 높은 hardcoded secret 형태다.

기존 패턴은 잡는다.

원안 (a)는 key 직전이 quote 이므로 잡지 못한다.

R-4.1 §5.3 의 canary 는 unquoted text 라서 이 회귀를 드러내지 않는다.

따라서 구현 전 regression case 에 quoted literal 을 추가해야 한다.

또는 좌측 delimiter 에 `'` / `"` 를 포함하는 보강안을 채택해야 한다.

### 권고

R-1. brief 의 “word boundary” 표현을 “left-context delimiter prefix” 로 정정 권고한다.

`(?:^|[?&\s])` 는 `\b` boundary 가 아니다.

합의 문서가 regex 의미를 정확히 써야 이후 재검토 비용이 줄어든다.

R-2. 패턴 변경과 함께 최소 regression test 를 추가해야 한다.

권고 test cases 는 다음이다.

```python
# should not match
"failures.sort(key=lambda e: e.get('ts', ''), reverse=True)"
"failures.sort(key=_ts_key, reverse=True)"
"WorkerResult(exit_code=exit_code, stdout=out)"
"dict(key=value)"
"fn(code=exit_code)"

# should match
"?api_key=fakecanary"
"&password=fakecanary&x=1"
"password=fakecanary&x=1"
"Authorization: Bearer abc ; api_key=fakecanary"
"payload = \"password=fakecanary&user=alice\""
"body = 'api_key=fakecanary&q=hi'"
```

R-3. match value 에 prefix 가 포함되는 점을 test expectation 에 반영해야 한다.

예: 변경 후 `?api_key=...` 전체가 match 된다.

이것이 reporting/redaction output 에 영향을 주지 않는지 확인해야 한다.

R-4. value terminator 를 `[^&\s]+` 로 유지하면 quote, comma, closing paren 이 value 에 포함될 수 있다.

현 FP 해소에는 충분하지만 reporting 품질은 낮다.

예: 기존 테스트에서 old pattern 은 `key=_ts_key,` 처럼 comma 를 포함했다.

보강안에서는 `[^&\s'"\),]+` 같은 terminator 개선을 검토할 수 있다.

단 terminator 변경은 탐지 범위에 영향이 있으므로 별도 합의/test 가 필요하다.

R-5. semicolon delimiter 는 별도 검토 대상이다.

`https://x.test/path;api_key=abc` 또는 cookie-like `; session=abc` 는 원안 (a) 에서 일부 놓치거나 whitespace 위치에 따라 다르게 동작한다.

현 R-4.1 canary 범위 밖이므로 이번 cycle 의 BLOCKING 으로 올리지는 않는다.

다만 URL path parameter / legacy query separator / cookie header 를 어느 범주로 볼지 후속 scanner audit 에 넣는 것이 좋다.

R-6. (b) hook exclude 는 권고하지 않는다.

`src/` 또는 `.py` 를 제외하면 hardcoded URL/query/body secret 을 놓칠 수 있다.

CI RED 해소에는 빠르지만 scanner 의 본질을 약화한다.

R-7. (c) source 회피는 권고하지 않는다.

`sort(key=...)` 는 Python 의 정상 API 이고, 이를 회피하려는 변경은 코드 품질을 악화시킨다.

또 `key` keyword 자체를 피할 방법이 사실상 없다.

R-8. (d) AST SAFE_CONTEXT 는 장기적으로 가장 정밀하지만 이번 sub-cycle 에는 과하다.

Python AST 로 call keyword arg 를 skip 하는 방식은 좋지만, scanner 가 Python 외 source/doc/log 도 다루므로 복잡도와 테스트 부담이 커진다.

이번에는 regex delimiter 정정 + regression test 가 현실적이다.

R-9. (e) `.py` alternation skip 은 권고하지 않는다.

`.py` 에 hardcoded URL, form body, header sample 이 들어갈 수 있다.

source scanner 의 방어 범위를 불필요하게 줄인다.

### NOTE

N-1. `\s` 는 newline 도 포함한다.

따라서 multi-line text 에서 newline 직후 `api_key=...` 는 match 된다.

이는 대체로 의도에 맞다.

N-2. `^` 는 `re.MULTILINE` 없이 문자열 전체 시작만 의미한다.

line-by-line scan 이면 각 line 시작으로 동작한다.

whole-file scan 이면 파일 전체 첫 위치만 `^` 이다.

scanner 가 파일을 line 단위로 순회한다면 문제 없다.

whole-file scan 이면 line-start form body cover 는 `(?m:^|[?&\s])` 또는 `(?:^|(?<=\n)|[?&\s])` 관점 확인이 필요하다.

N-3. 이번 정정은 Hermes key 목록 보존형이다.

따라서 Hermes upstream 답습 본질 손상은 없다.

N-4. T1-041/T1-042 직접 등록 제외인 T1-038/T1-040 canary cover 를 alternation 으로 유지한다는 설계 자체는 보존된다.

N-5. 기존 safe-cookie 논의상 `session=` 은 Hermes catalog 에서 sensitive 로 취급된다.

따라서 cookie/session FP 여부는 이번 cycle 의 Python keyword arg FP 와 분리해야 한다.

## §5 최종 권고 (APPROVE / REVISE / REJECT + 근거)

최종 판정: **REVISE**

REJECT 는 아니다.

원안 (a)는 brief 가 제시한 7개 verification scenario 를 모두 만족한다.

CI RED 를 만든 Python keyword arg false positive 도 정확히 제거한다.

Hermes key 목록도 보존한다.

T1-038/T1-040 의 현재 canary cover 도 유지한다.

그러나 그대로 APPROVE 하기에는 quoted form-urlencoded body literal FN risk 가 있다.

특히 이 scanner 는 source code 를 scan 하므로 다음 형태는 실질적으로 중요하다.

```python
payload = "password=fakecanary&user=alice"
body = 'api_key=fakecanary&q=hi'
```

원안 (a)는 이 형태를 놓친다.

따라서 구현 전 brief 또는 구현안에 다음 중 하나를 반영하는 조건부 승인 흐름을 권고한다.

1. (a+) 로 보강: 좌측 delimiter 에 quote 를 추가한다.
2. quoted body literal regression test 를 추가하고, 원안 (a)의 FN 을 의도적 tradeoff 로 명시 승인한다.
3. 이번 cycle 은 원안 (a) 로 CI RED 만 해소하되, quoted literal cover 회귀를 별도 BLOCKING carry-over 로 즉시 등록한다.

내 권고는 1번이다.

즉 `(?:^|[?&\s'"])` 계열로 보강하고, `(` 는 delimiter 에 넣지 않는다.

이렇게 하면 `sort(key=...)` / `exit_code=...` FP 는 재발하지 않으면서 quoted body string cover 를 상당 부분 회복한다.

합의 자격은 “기존 Tier-1 alternation pattern 본문 정정”이다.

version pin 이 아니므로 R-7(b) PC1-2 상 단순 단축 합의로 낮추는 것은 약하다.

풀 3+1 + 외부 LLM 1+ 가 가장 보수적으로 정확하다.

다만 사용자 명시 + 외부 LLM cross-validation + regression evidence 가 있으면, 결함 정정 한정 단축 합의도 운영상 방어 가능하다.

## §6 자기진단

검토한 local source 는 다음이다.

`tools/secret_scanner.py` 의 T1-041/T1-042 현 패턴을 확인했다.

`docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` v1.1 의 scope, 후보, 7개 verification scenario 를 확인했다.

`docs/phase0/r4-1-trigger-extension-evidence.md` §5.3 의 T1-041/T1-042 canary 를 확인했다.

`docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` line 94 주변의 R-7(b) 차등 취지를 확인했다.

`docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 의 (a)~(d), 후속 (e) 운영조건 framing 을 확인했다.

Python `re` 로 원안 (a)의 대표 case 를 직접 검증했다.

확인된 PASS 는 brief 의 7개 scenario 와 일치한다.

추가로 확인된 주요 risk 는 quoted form body literal FN 이다.

내 판정은 이 risk 를 근거로 APPROVE 가 아니라 REVISE 이다.

본 응답은 코드 변경을 수행하지 않았다.

본 응답은 cross-validation 의견 제출만 수행했다.
DONE
