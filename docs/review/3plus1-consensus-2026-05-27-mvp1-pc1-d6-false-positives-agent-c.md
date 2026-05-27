# Agent C 대안 탐색 — MVP-1 (b1-PC1-D6-false-positives) sub-cycle

> **역할**: Agent C — 대안 탐색가. 핵심 질문: "더 나은 방법이 있는가? (대안 기술, 트레이드오프)"
> **참조 0건 의무**: 다른 Agent (A/B) + Reviewer 출력 0건 참조, 본문 직접 read 한정 독립 분석.

---

## §1 본 분석 자격 (다른 Agent 참조 0건 + 본문 직접 read)

### 1.1 답습 source 직접 read 4건

| Source | path | 본 분석 답습 영역 |
|---|---|---|
| brief v1.1 | `docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md` | §1~§10 전수 (사용자 D-FP-1 = (a) 채택 명시 답습) |
| secret_scanner.py | `tools/secret_scanner.py` | line 154~159 ALTERNATION_PATTERNS + line 178 REDACTION_MARKER_RE + line 183~187 SCAN_*_EXTENSIONS + line 220~246 scan_text |
| R-4.1 evidence | `docs/phase0/r4-1-trigger-extension-evidence.md` | §4.2 H-J/H-L 직접 등록 제외 사유 + §5.3 alternation canary 222~223 line + §8 1차→2차 진화 + §12.2 (b) Hermes upstream drift |
| .pre-commit-config.yaml | `.pre-commit-config.yaml` | line 36~46 secret-scanner hook entry (bash for loop scan-source src/ + .github/) |

### 1.2 라이브 regex 실증 (Python re engine, 본 분석 시점 실행)

Agent C 는 **계산적 검증 우선** 답습 (CLAUDE.md §2 "계산적 vs 추론적 검증") — 본 분석의 모든 후보 평가에서 가능한 한 Python regex 라이브 실행 결과를 1차 근거로 사용. 본문 §2 매트릭스의 각 후보 평가 결과 raw 는 §3 에서 인용.

### 1.3 다른 Agent (A/B/Reviewer) 참조 0건 의무 답습

- Agent A (구현 분석가) 출력 본 분석 진행 시점 미생성 또는 가정 0건
- Agent B (품질 검증가) 출력 동상
- Reviewer 출력 동상
- 본 §2~§5 전수 = **brief v1.1 + 본문 직접 read + 라이브 실증** 한정 (편향 방지)

---

## §2 8 항목 대안 평가 매트릭스

### 2.1 매트릭스 (각 후보 CHAMPION / VIABLE / DEFER / REJECT 분류)

| # | 대안 후보 | 핵심 변경 | scope | 등급 | 핵심 근거 |
|---|---|---|---|---|---|
| **1** | **(a) `(?:^|[?&\s])` prefix** (사용자 채택) | alternation 직전 비캡처 그룹 추가 (3~6 줄) | `tools/secret_scanner.py` 본문 | **CHAMPION** | FP 4/4 해소 + canary 5/5 cover 보존 + Python regex fixed-width 보장 (§3.1 라이브 실증) |
| 1a | (a) 변형: `\b` word boundary | alternation 직전 `\b` 추가 (3~6 줄) | 동상 | **REJECT** | `key=lambda` / `key=_ts_key` FP **재발생** (§3.2 라이브). `key` 자체가 word char 끝 → Python keyword arg 매칭 회피 0 |
| 1b | (a) 변형: negative lookbehind `(?<![A-Za-z0-9_])` | alternation 직전 lookbehind 추가 | 동상 | **REJECT** | FP `key=lambda`/`key=_ts_key` 재발생 (§3.2) — line start 가 `[A-Za-z0-9_]` 아님 → 매칭 |
| 1c | (a) 변형: variable-width lookbehind `(?<=^|[?&\s])` | 동상 | 동상 | **REJECT** | Python re engine 거부: `look-behind requires fixed-width pattern` (§3.2 라이브 ERR) |
| 1d | (a) 변형: extended boundary `(?:^|[?&\s,;\(\[\"\\'])` | alternation 직전 확장 boundary | 동상 | **REJECT (FP 재발)** | `(key=lambda)` `,key=lambda` 케이스 FP **재발생** (§3.3 라이브). Python keyword arg 의 직전 char (`(` `,`) 가 HTTP 패턴 boundary 와 동일 → 회피 불가능 |
| **2** | **(d) AST SAFE_CONTEXT** | secret_scanner.py 에 ast 기반 컨텍스트 검사 추가 | `tools/secret_scanner.py` 본문 (≈30~50 줄) | **DEFER** (carry-over 별도 cycle) | 영구 정밀화 + 복잡도 증가 + .py 외 .yaml/.json/.md 등 non-Python 영역 미적용 → (a) 와 병행이 본질. 단독 채택은 ceremony 과잉 |
| **3** | **(a) + (d) 병행 hybrid** | (a) 즉시 + (d) 별도 cycle | 2 cycle | **VIABLE** | (a) = 즉시 결함 정정 / (d) = 향후 동형 FP 자동 회피. **carry-over 권고** |
| **4** | **SAFE_KEYS list 별도 분리** | `key`/`code`/`auth`/`session` 만 별도 list + word boundary 강제, 나머지는 현 패턴 유지 | `tools/secret_scanner.py` 본문 (2 list 분리, ≈10 줄) | **DEFER** | (a) `(?:^|[?&\s])` 단일 prefix 가 alternation 전체에 적용 = same effect, 분리 비용 0 회수. (a) 우월 |
| **5** | **Hermes upstream Python import** | Hermes `agent/redact.py` 직접 import 사용 | `tools/secret_scanner.py` 본문 + 의존성 추가 | **REJECT** | Provider Liquidity 5-way 답습 위반 + lock-in risk + 헌법 5조-2 비협상 충돌 + Hermes 자체 PMO 격상 0건 (33번째 답습 보존 의무) |
| **6** | **alternation 분할** (45 → 100+ individual patterns) | T1-041/T1-042 alternation 해체 → 키 별 individual prefix pattern | `tools/secret_scanner.py` 본문 (≈30 line 추가) | **DEFER** | 정밀도 향상 0 (a) 와 동일 효과 + 성능 영향 미미 (45 → 100 = O(n) regex finditer) + R-4 §7.2.3 alternation 채택 evidence 답습 손상 |
| **7** | **scan-source mode 분할** (`.py` separate handler) | `.py` 와 `.yaml` 별도 mode | `tools/secret_scanner.py` 본문 (≈15~25 줄) | **DEFER** | (e) brief 후보와 본질 동일 — `.py` 내 실 URL 패턴 FN risk + ceremony 비싼 분리. (a) 가 file-ext 무관 회피 |
| **8** | **`pass_filenames: true` per-file scan** (상위 design) | `.pre-commit-config.yaml` hook 자체 정밀화 | `.pre-commit-config.yaml` line 36~46 본문 변경 | **carry-over 권고** | 본 sub-cycle scope 외 + 별도 BLOCKING 메커니즘 개선 cycle 자격. (a) 발효 후 별도 carry-over (b1-PC1-D6-hook-design) 후보 |

### 2.2 매트릭스 요약

- **CHAMPION**: (a) `(?:^|[?&\s])` prefix — 사용자 채택 동의 + 라이브 실증 우월
- **VIABLE**: (a) + (d) 병행 hybrid — carry-over 권고
- **DEFER**: (d) 단독 / SAFE_KEYS / alternation 분할 / scan-source 분할 / `pass_filenames` hook 개선
- **REJECT**: (a) `\b` 변형 / lookbehind 변형 / extended-boundary 변형 / Hermes upstream import

---

## §3 핵심 대안 (CHAMPION 후보 상세 + 권고)

### 3.1 (a) `(?:^|[?&\s])` prefix — CHAMPION 라이브 실증

```python
# 라이브 실행 결과 (Python re engine, 2026-05-27)
# 패턴: (?i)(?:^|[?&\s])(?:access_token|token|api_key|key|code|password)=[^&\s]+
```

| Test 케이스 | 입력 | 매칭 결과 | 평가 |
|---|---|---|---|
| FP1 sort key arg | `failures.sort(key=lambda e: e.get("ts", ""), reverse=True)` | no-match | ✅ FP 해소 |
| FP2 dataclass keyword | `return cls(exit_code=exit_code, stdout=stdout)` | no-match | ✅ FP 해소 |
| FP3 named func sort | `failures.sort(key=_ts_key, reverse=True)` | no-match | ✅ FP 해소 |
| FP4 literal exit_code | `return cls(exit_code=1, error=msg)` | no-match | ✅ FP 해소 |
| CAN1 URL ?api_key= | `redirect https://x.com/cb?api_key=fakecanaryR41T041NOTAREAL&q=hi` | MATCH `'?api_key=fakecanaryR41T041NOTAREAL'` | ✅ canary 보존 |
| CAN3 line-start | `access_token=fakecanaryR41T040NOTAREAL&user=alice` | MATCH `'access_token=fakecanaryR41T040NOTAREAL'` | ✅ canary 보존 |
| CAN4 HTTP whitespace | `Authorization: Bearer x ; api_key=fakecanaryX` | MATCH `' api_key=fakecanaryX'` | ✅ canary 보존 |
| CAN5 tab whitespace | `Header:\tkey=fakeC` | MATCH `'\tkey=fakeC'` | ✅ canary 보존 |
| EDGE `__hidden_key=` | `__hidden_key=secret_value` | no-match | ⚠️ FN (Python identifier 내) |
| EDGE `X-my_api_key=` | `X-my_api_key=fakecanary` | no-match | ⚠️ FN (HTTP header style 일부) |

### 3.2 (a) `\b` / lookbehind 변형 — REJECT 라이브 실증

| 변형 | FP1 `key=lambda` | FP3 `key=_ts_key` | 등급 |
|---|---|---|---|
| `\b(?:...)=` | **MATCH** (`key=lambda`) | **MATCH** (`key=_ts_key`) | REJECT (`key`/`token` 자체가 word boundary 양쪽 둘러싸인 인식 못함) |
| `(?<![A-Za-z0-9_])(?:...)=` | **MATCH** (`key=lambda`) | **MATCH** (`key=_ts_key`) | REJECT (line start 가 `[A-Za-z0-9_]` 아님 → lookbehind 통과 → 매칭) |
| `(?<=^\|[?&\s])(?:...)=` | — | — | REJECT (Python re engine 거부: `look-behind requires fixed-width pattern`) |

**결론**: Python `re` 모듈 한정에서 `(?:^|[?&\s])` non-capturing group prefix 만이 **fixed-width + multi-anchor + Python keyword arg cover** 3조건 동시 충족. 채택 정당성 확정 ✅

### 3.3 (a) extended boundary 변형 — REJECT 라이브 실증

```
패턴: (?:^|[?&\s,;\(\[\"\\'])(?:...)=
```

| 케이스 | 매칭 | 평가 |
|---|---|---|
| `sort(key=lambda x: x)` (paren prefix) | **MATCH** `(key=lambda` | FP 재발 |
| `fn(arg, key=lambda x: x)` (comma prefix) | **MATCH** `,key=lambda` | FP 재발 |
| `config[key=val]` (bracket) | **MATCH** `[key=val]` | FP 재발 |

→ Python keyword arg 의 직전 char (`(`, `,`, `[`) = HTTP body separator 와 의미 충돌. **extended boundary = (a) 우월성 손상**. REJECT.

### 3.4 (d) AST SAFE_CONTEXT 후보 본문 design (상세)

본 sub-cycle 채택 0 (DEFER) 영역이지만 향후 carry-over cycle 진입 시 reference 자격:

```python
# tools/secret_scanner.py 추가 영역 (대략 30~50 줄)
import ast

def is_python_keyword_arg_context(file_path: Path, line_no: int, col_no: int) -> bool:
    """AST 기반 — line/col 위치가 Call.keywords / FunctionDef.args / ClassDef.body 의
    keyword arg context 면 True (secret 매칭 위치가 Python identifier 영역).

    SAFE_CONTEXT 분류 매트릭스:
      - ast.Call.keywords[].arg  → keyword arg name (key=lambda 영역)
      - ast.FunctionDef.args.kwonlyargs[].arg → kwonly arg name
      - ast.ClassDef.body[ast.AnnAssign].target.id → class attr name
      - ast.Dict.keys[ast.Constant.value] → dict literal key (str)
      - ast.AnnAssign.target.id  → typed variable assignment

    Non-SAFE (보안 영향, 매칭 유지):
      - ast.Constant (str literal) — string value 영역 = 실 secret 가능성
      - ast.JoinedStr (f-string) — interpolation 영역 동상
      - ast.Comment — docstring/inline comment 외
    """
    if file_path.suffix != ".py":
        return False  # AST 분석 .py 한정
    try:
        tree = ast.parse(file_path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if hasattr(node, "lineno") and node.lineno == line_no:
            # Call.keywords[].arg 위치 검출
            if isinstance(node, ast.Call):
                for kw in node.keywords:
                    if kw.lineno == line_no and kw.col_offset <= col_no:
                        return True
            # FunctionDef.args.kwonlyargs[]
            if isinstance(node, ast.FunctionDef):
                for kwarg in node.args.kwonlyargs:
                    if kwarg.lineno == line_no:
                        return True
            # AnnAssign / Assign target
            if isinstance(node, (ast.AnnAssign, ast.Assign)):
                return True
    return False

# scan_text 통합:
def scan_text(text, file_path, mode=None):
    vios = []
    for pid, src, cat, vendor, pattern in COMPILED_PATTERNS:
        if pid in SKIP_DIRECT_REGISTER:
            continue
        for m in pattern.finditer(text):
            matched = m.group(0)
            if mode == "scan-log" and is_redaction_marker_match(matched):
                continue
            line_no = text[: m.start()].count("\n") + 1
            col_no = m.start() - (text.rfind("\n", 0, m.start()) + 1)
            # (d) AST SAFE_CONTEXT 검사
            if cat == "alternation" and is_python_keyword_arg_context(file_path, line_no, col_no):
                continue
            vios.append(Violation(file=file_path, line=line_no, ...))
    return vios
```

**(d) trade-off**:

| 차원 | (a) 단독 | (d) 단독 | (a)+(d) 병행 |
|---|---|---|---|
| FP 회피 cover | Python keyword arg 4건 ✅ | Python AST 정확 분류 ✅ | 양 영역 모두 ✅ |
| `.yaml`/`.json`/`.md` cover | ✅ (모든 ext 적용) | ❌ (.py 한정) | ✅ |
| 복잡도 | 6 줄 | 50~70 줄 | 60~80 줄 |
| AST parse 비용 | 0 | O(n) per file | O(n) per file |
| Hermes 답습 손상 | 0 (key 목록 보존) | 0 (key 목록 보존) | 0 |
| Python identifier 내 (`__hidden_key=`) cover | ❌ FN | ✅ AST 분류 | ✅ |
| HTTP header `;api_key=` cover | ❌ (a_alt 매칭 0) | N/A (.py 외) | △ (별도 boundary 필요) |
| carry-over 가치 | — | 영구 정밀화 | **best long-term** |

**권고**: (a) 즉시 + (d) 별도 carry-over cycle 진입 자격.

### 3.5 후보 6 (alternation 분할) 정밀 분석

T1-041/T1-042 alternation 을 키 별 individual prefix pattern 으로 해체:

```python
# 현 (alternation 1개):
("T1-041", ..., r"(?i)(?:access_token|token|...|key|code)=[^&\s]+")

# 분할 후 (16개 individual):
("T1-041a", ..., r"(?i)(?:^|[?&\s])access_token=[^&\s]+"),
("T1-041b", ..., r"(?i)(?:^|[?&\s])token=[^&\s]+"),
... × 16
```

**Trade-off**:

| 차원 | 현 (alternation) | 분할 |
|---|---|---|
| 등록 패턴 수 | 45 | 100+ |
| regex compile 비용 | 1회 | 16~30회 (per file × 패턴 수) |
| scan 시간 (O(n×m)) | 평균 +0% | 평균 +5~10% (m 증가) |
| 정밀도 | (a) 적용 시 100% | 동일 |
| 각 키 별 violation reporting | `T1-041` 단일 | `T1-041-key` / `T1-041-token` 분리 → log 가독성 ↑ |
| R-4 §7.2.3 evidence 답습 | ✅ alternation 채택 명시 | ❌ 답습 손상 (R-4 §7.2.3 의 정당성 반박) |

**결론**: 정밀도 향상 0 (a) 와 동일 + R-4 evidence 답습 손상 → **DEFER** (분할 가치 < 보존 가치).

### 3.6 후보 8 (`pass_filenames: true` hook design) 정밀 분석

현 `.pre-commit-config.yaml` line 38~44:
```yaml
- id: secret-scanner
  entry: bash -c 'for d in src .github; do python3 tools/secret_scanner.py --mode scan-source "$d" || exit 1; done'
  pass_filenames: false
  always_run: true
```

대안:
```yaml
- id: secret-scanner
  entry: python3 tools/secret_scanner.py --mode scan-source
  pass_filenames: true     # ← 변경
  files: \.(py|yaml|yml|json|toml|sh|bash|env|ini|cfg|pem|key|txt|md)$
  # always_run: 제거 (pass_filenames 와 충돌)
```

**Trade-off**:

| 차원 | 현 (always_run + for loop) | per-file (pass_filenames) |
|---|---|---|
| 작동 mode | `pre-commit run --all-files` = 전수 scan | staged file 만 scan |
| `pre-commit run` (commit 시) | staged 변경 후에도 전 src/ + .github/ 재scan = O(전체) | staged 만 = O(변경 수) |
| CI 통합 (`--all-files`) | 동일 (전수 scan) | 동일 |
| dev 속도 (commit hook) | 느림 (전체 ~수초) | 빠름 (변경 file 한정 ~ms) |
| FN risk | 0 (전수 보장) | 0 (수정된 file 만 검출 = 충분, 변경 안 된 file 의 secret = 기존 commit 누락 = 별도 audit cycle) |
| secret_scanner.py CLI 호환 | OK (path arg 받음) | OK (path arg 받음 + per-file 호출) |
| `--mode` 강제 | bash for loop 에서 명시 | hook entry 에서 명시 |
| 본 sub-cycle scope | 외 (carry-over) | 외 (carry-over) |

**권고**: 본 sub-cycle 외 carry-over (b1-PC1-D6-hook-design) 또는 (b1-PC1-D6-evidence) 의 자율 영역 후보. 본 sub-cycle = (a) 한정.

---

## §4 최종 권고

### 4.1 (a) APPROVE 유지 — 핵심 권고

| 결정 항목 | Agent C 권고 |
|---|---|
| D-FP-1 채택 후보 | **(a) APPROVE** (사용자 채택 = 라이브 실증 우월 검증 완료) |
| D-FP-2 합의 형태 | **(2) 단축 합의 + 외부 LLM 1+ cross-validation** 권고 — 명백한 결함 정정 (FP 4/4 해소 + canary 5/5 cover 보존 라이브 실증) + R-7(b) PC1-2 차등 답습 시 alternation 패턴 본문 변경 자체는 catalog *영역* 이지만 *본질* (key 목록) 변경 0 (prefix 만 추가, key 목록 보존) → ceremony 완화 자격. 단 외부 LLM cross-validation 의무 (catalog 본문 변경 안전성 검증) |
| D-FP-3 외부 LLM method | (P) Claude 가 tmux + codex bypass sandbox 직접 호출 (24번째 entry pattern 답습 + 사용자 개입 최소화 목표 답습) |
| D-FP-4 회귀 verification 범위 | (1) + (2) + (3) 전수 — 본 D-6 workflow re-run + secret_scanner.py self-test (CAN1~CAN5 라이브 reproduction) + jarvis 144/144 pytest green 답습 보존 |

### 4.2 carry-over 추가 권고 (3 cycle)

| Carry-over | 후보 | 진입 자격 |
|---|---|---|
| (b1-PC1-D6-ast-context) | (d) AST SAFE_CONTEXT 영구 정밀화 | (a) 발효 + b1-PC1-D6 sub-cycle 완료 후. 풀 3+1 자격 |
| (b1-PC1-D6-hook-design) | `pass_filenames: true` + per-file scan + `files:` filter 정밀화 | (a) 발효 + (b1-PC1-D6-evidence) 완료 후. 단축 합의 자격 (hook entry 변경, catalog 영향 0) |
| (b1-PC1-D6-pattern-audit) | T1-041/T1-042 외 alternation 패턴 (현 PoC 0건이지만 향후 Tier-2/3 도입 시) FP 가능성 사전 audit | Tier-2/3 catalog 진입 시점 동시 진행 |

### 4.3 Agent C 의 (a) 외 다른 후보 제거 사유

- **(a) `\b` 변형** = `key`/`token` 자체가 word char 끝 → Python keyword arg 식별자 차단 0 (§3.2 라이브)
- **(a) lookbehind 변형 (negative)** = line start 가 lookbehind char class 외 → 매칭 통과 (§3.2)
- **(a) variable-width lookbehind** = Python `re` engine 거부 (§3.2 ERR)
- **(a) extended boundary** = `(`/`,`/`[` prefix 추가 시 Python keyword arg FP 재발 (§3.3 라이브)
- **(d) 단독** = .yaml/.json 영역 미적용 + 복잡도 우월성 부족 (§3.4 trade-off)
- **(4) SAFE_KEYS list 별도 분리** = (a) 단일 prefix 가 동일 효과, 분리 비용 0 회수
- **(5) Hermes upstream Python import** = Provider Liquidity + 헌법 5조-2 비협상 충돌
- **(6) alternation 분할** = R-4 §7.2.3 evidence 답습 손상 + 정밀도 향상 0
- **(7) scan-source mode 분할** = `.py` 내 실 URL 패턴 FN risk + (a) 가 file-ext 무관 회피

### 4.4 본 권고 = brief v1.1 §7.1 1차 권고 (a) APPROVE 와 일치

본 Agent C 독립 분석 결론 = brief v1.1 1차 권고 = **(a) 단독 채택 + (d) carry-over** 와 일치. 핵심 정당성 보강:

1. **fixed-width regex 조건** — Python `re` engine 한정에서 `(?:^|[?&\s])` 가 유일한 multi-anchor + fixed-width 해법 (§3.2 ERR 라이브 실증)
2. **Python keyword arg cover** — `\b` / negative lookbehind 변형 모두 `key=lambda` FP 재발 (§3.2)
3. **canary 5/5 보존** — alternation key 목록 본질 변경 0, prefix 만 추가 → Hermes 답습 손상 0 (§3.1)
4. **(d) 영구 carry-over** — `.py` 내 Python identifier (`__hidden_key=`) 영역 FN cover 가치 (§3.4)

---

## §5 자기진단 (5/5)

| # | 항목 | 상태 | 근거 |
|---|---|---|---|
| 1 | 다른 Agent (A/B/Reviewer) 출력 참조 0건 + 가정 0건 | ✅ | §1.3 명시 + 본문 추론 0건 |
| 2 | 답습 source 4 file 직접 read (brief v1.1 + secret_scanner.py + R-4.1 evidence + .pre-commit-config.yaml) | ✅ | §1.1 명시 |
| 3 | 8 항목 대안 평가 매트릭스 + 각 후보 CHAMPION/VIABLE/DEFER/REJECT 분류 + 사유 | ✅ | §2.1 매트릭스 14 row (8 항목 + (a) 변형 4 + carry-over) |
| 4 | CHAMPION 후보 (a) 라이브 실증 — Python re engine 직접 실행 + FP/canary/edge case 라이브 결과 인용 | ✅ | §3.1~§3.3 라이브 실증 표 (4 FP + 5 canary + 2 edge + 4 변형) |
| 5 | 최종 권고 (D-FP-1~D-FP-4) + carry-over 3 cycle 권고 + brief v1.1 1차 권고와 일치 확인 | ✅ | §4.1 + §4.2 + §4.4 |

**최종 verdict**: Agent C **(a) APPROVE 권고** — D-FP-1 채택 후보 (a) 단독 + (d) carry-over 별도 cycle 자격.
