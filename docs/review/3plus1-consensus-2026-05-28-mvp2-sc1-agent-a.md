# 3+1 합의 — MVP-2 SC-1 facade RedactionFilter 구현 brief / Agent A (구현 분석가)

> **관점**: "실제로 동작하는가?" (기술적 구현 가능성, 의존성, 성능)
> **대상**: `docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md` (v1, §0~§11)
> **작성**: 2026-05-28 (세션 #3, 65번째 entry cycle)
> **방식**: filesystem direct inspection (독립 분석 — Agent B/C, 외부 LLM 응답 미참조)

---

## 1. 판정

### **APPROVE WITH CONDITIONS**

설계는 기술적으로 **구현 가능**하며 redaction layer 통합 + catalog 재사용 + TDD 모두 실현 가능하다 (filesystem 실측 검증 완료). 단, **catalog 재사용 옵션 (i)의 brief 본문 표현 정정** + **`[REDACTED]` whole-match 치환의 의미 손상 명문화** 2건이 구현 전 정정 필요하다 (BLOCKING-1, BLOCKING-2). 나머지는 권고/NOTE.

---

## 2. BLOCKING (구현 전 정정 필수)

### BLOCKING-1 — catalog 재사용 옵션 (i) 단점 표기 부정확 + import 형태 모호 (§2.1 line 71)

**근거 (line 71 인용)**:
> `(i) src → tools.secret_scanner import | RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import | ... | **src(런타임) → tools(개발도구) 역방향 의존** (아키텍처 부적절, **.importlinter root=src 밖이라 미차단이나** nonidiomatic)`

filesystem direct inspection 결과 옵션 (i)에 대해 brief가 부정확하게 서술한 2가지:

**(1-a) import 형태가 brief 내 2개로 혼재**:
- §2.1 line 71 본문 = `from tools.secret_scanner import COMPILED_PATTERNS` (package 경로)
- 그러나 §0.3 line 48 + 기존 코드 컨벤션 = 기존 test (`tests/tools/test_jsonl_hash_chain.py` line 16~18)는 `sys.path.insert(0, _ROOT/"tools")` 후 **bare `import secret_scanner`** 사용

이 둘은 **런타임 동작이 다르다** (실측):

| import 형태 | repo root만 sys.path | 동작 |
|---|---|---|
| `from tools.secret_scanner import COMPILED_PATTERNS` | ✅ | **OK** (`tools`는 PEP-420 namespace package — `tools/__init__.py` 부재해도 import 됨, 실측 45 반환) |
| bare `import secret_scanner` | ❌ | **FAILS** `No module named 'secret_scanner'` (tools/ 자체가 sys.path에 있어야 함) |

→ brief가 옵션 (i)를 채택한다면 **반드시 `from tools.secret_scanner import` (namespace package) 형태로 고정**해야 한다. bare import는 facade 런타임(repo root만 sys.path — `examples/jarvis_e2e_demo.py` line 25 패턴)에서 깨진다.

**(1-b) ".importlinter root=src 밖이라 미차단" 표현은 맞으나 단점 framing 과잉**:
- 실측: `.importlinter` forbidden_modules = `{openai, anthropic, litellm, ollama}` (line 30~33) — **`tools` 미포함**. grimp graph 직접 빌드 검증 결과 `from tools.secret_scanner import`는 contract `no-direct-llm-sdk`를 **위반하지 않음** (forbidden 목록에 tools 부재).
- 즉 옵션 (i)는 import-linter 관점에서 **완전히 합법** (단순 "미차단"이 아니라 "애초에 forbidden 대상이 아님").
- "역방향 의존(런타임→개발도구)" 우려는 타당하나, 본 프로젝트는 **packaging manifest 부재 = run-from-source** (실측: MANIFEST.in/setup.py/pyproject.toml 전무, tools/ git 추적됨). 따라서 tools/는 런타임에 항상 존재 → 배포 시 누락 위험 0. "아키텍처 부적절"은 **idiom 선호 문제이지 동작 BLOCKING이 아님**.

**정정 요구**: §2.1 옵션 (i) 본문을 (가) import 형태를 `from tools.secret_scanner import COMPILED_PATTERNS` (namespace package)로 명시 고정, (나) "미차단" → "import-linter forbidden 대상 아님 (합법)" + "run-from-source라 배포 누락 위험 0"로 정정.

---

### BLOCKING-2 — `[REDACTED]` whole-match 치환의 의미 손상 미명문 (§2.2 line 83, §3 line 101)

**근거 (line 83 / line 101 인용)**:
> line 83: `def redact_text(self, text: str) -> str: ...  # str 패턴 매칭 → [REDACTED]`
> line 101: `정상 대화 내용 손상 아님 — Tier-1 catalog는 secret 패턴 (sk-/Bearer/api_key 등) 한정 매칭.`

filesystem direct inspection — COMPILED_PATTERNS로 `re.sub('[REDACTED]', text)` 실측 결과:

| 입력 | 출력 (실측) | 문제 |
|---|---|---|
| `my key is sk-ant-abcdefghij1234567890` | `my key is [REDACTED]` | ✅ 정상 (prefix만 치환) |
| `OPENAI_API_KEY=sk-abc1234567890xyz` | `[REDACTED]` | ⚠️ **key 이름까지 소거** (H-A regex `T1-032`가 `KEY=value` 전체 매칭) |
| `{"api_key": "sk-1234567890abcdef"}` | `{[REDACTED]}` | ⚠️ **JSON key + 구조 손상** (H-B `T1-033`가 `"key":"value"` 전체 매칭) |
| `https://user:password123@host.com/path` | `[REDACTED]host.com/path` | ⚠️ **username + scheme 소거** (H-K `T1-039` userinfo 전체 매칭) |
| `Authorization: Bearer abc...token` | `[REDACTED]` | ⚠️ 헤더 라벨까지 소거 (H-C `T1-034`) |
| 정상 대화 (secret 0) | 무변경 | ✅ **false positive 0 확인** |

**핵심**: GP-2 prevention 목적(=secret이 request body로 새지 않게)은 **달성된다** (secret 평문은 100% strip — over-redaction이지 under-redaction이 아님). 그러나 brief line 101 "정상 대화 내용 손상 아님" 주장은 **부정확**하다. regex/alternation 카테고리 패턴(T1-032~039, 041~042)은 **capture group으로 key 이름·구조까지 whole-match 치환**하므로 (i) request body의 JSON 구조 손상, (ii) key 이름 컨텍스트 소실이 발생한다. secret이 *값으로* 들어간 정상 필드(예: 대화 중 사용자가 의도적으로 secret을 LLM에 보여주려는 경우는 GP-2가 막아야 하니 OK이지만, **JSON 구조가 깨지면 LLM 요청 자체가 malformed**될 수 있다).

**정정 요구**: §2.2/§3에 (가) "redaction = whole-match `[REDACTED]` 치환 → regex/alternation 카테고리는 key 이름·구조도 함께 치환됨 (over-redaction, secret leak 0이나 구조 손상 가능)" 명문화, (나) §5 TDD에 **"redaction 후 messages가 여전히 valid 구조(role/content dict 보존)인지" 검증 test 추가** (현 T-1~T-6은 content 문자열 redaction만 검증, dict 구조 무결성 미검증). secret_scanner의 `is_redaction_marker_match`(line 222)는 *검출 후 marker 인식*용이지 *치환*용이 아니므로 redaction 치환 로직은 RedactionFilter가 자체 구현해야 함 (line 89 "is_redaction_marker_match 답습"은 marker 문자열 정합 참조로 한정).

---

## 3. 권고

### 권고-1 — `tests/adapters/llm/` 디렉토리 + `__init__.py` 생성 명시 (§5.1)
실측: `tests/adapters/` **부재**. §5.1은 `tests/adapters/llm/test_redaction_filter.py`를 신규로 명시하나 디렉토리 생성 + (jarvis 컨벤션 답습) `tests/jarvis/__init__.py` 존재 패턴에 맞춰 `tests/adapters/__init__.py` + `tests/adapters/llm/__init__.py` 생성 여부를 brief에 명시 권고. (단 `tests/tools/`는 `__init__.py` 없이도 동작 — pytest rootdir 자동 발견. 어느 쪽이든 동작하나 일관성 위해 명시.)

### 권고-2 — facade import 형태를 src 컨벤션(`from src...`)과 정합
실측: `src/jarvis/*`는 전부 절대 import `from src.jarvis.X` (orchestrator line 17~21). RedactionFilter도 `src/adapters/llm/redaction.py`에 두고 facade가 `from src.adapters.llm.redaction import RedactionFilter`로 import하는 것이 컨벤션 정합. brief §5.2 line 142가 이미 이 경로를 제시 — OK, 명시 유지 권고.

### 권고-3 — redaction 적용 순서를 §4.1 line 111~113에서 try/raise 순서 명확화
§4.1: `complete()`에서 (1) redact_messages → (2) `raise NotImplementedError`. 기술적으로 **가능**(실측 facade.py complete()는 현재 즉시 raise — line 38). 단 T-6(line 138)이 "redaction *후* deferred 순서 검증"을 요구하므로, redaction이 **부작용 없는 순수 변환**(brief line 90 frozen/순수 함수)이면 raise 전 호출돼도 안전. RedactionFilter를 frozen으로 두면 redact 결과를 버려도 무방 → 순서 검증 test는 "redact_messages가 호출됐는지(spy/mock)"로 구현해야 함을 명시 권고 (단순 반환값 검증으론 raise 때문에 도달 불가).

### 권고-4 — `health()` async 시그니처 보존 (§4.1 미언급)
실측: facade.py line 40 `async def health() -> dict[str, bool]`. brief는 `complete()`만 다루므로 health() 무변경 명시 권고 (시그니처 보존, redaction 무관).

---

## 4. NOTE (filesystem direct inspection 발견)

- **N-1 (pytest baseline GREEN 확인)**: `.venv/bin/python -m pytest tests/ -q` → **152 passed in 0.10s** (실행 완료). 회귀 비교 baseline 확정. (brief §10 E-5 "jarvis pytest 회귀 0" 측정 가능.)
- **N-2 (litellm 미설치 확인)**: `import litellm` → `ModuleNotFoundError`. brief §7 line 185 "litellm import 0" + import-linter `include_external_packages=True`(line 21)로 미설치 환경에서도 검출 가능 — 정합.
- **N-3 (import-linter 환경 artifact)**: `lint-imports` CLI가 본 환경에서 `Only one live display may be active at once`로 **exit=1 크래시** (rich Live display 충돌 — Claude Code 하네스 rich 점유 추정). 이는 **contract 위반이 아니라 환경 렌더링 artifact**. grimp graph 직접 빌드(`grimp.build_graph('src', include_external_packages=True)`)로 검증 → facade 제외 src 모듈의 forbidden SDK import = **NONE → contract 실질 KEPT**. 구현 후 verify 시 동일 환경에서 lint-imports CLI가 깨질 수 있으므로 **grimp 직접 검증 또는 별도 비-rich 환경(CI) 의존 필요** — brief §5.4 line 153 "import-linter green" 측정 시 유의.
- **N-4 (secret_scanner import-safe 확인)**: `import secret_scanner` 시 **argparse/CLI 미실행** (실측 — `_cli()`는 `if __name__=="__main__"` line 378 가드 내부). 모듈 import 시 부작용 = COMPILED_PATTERNS 컴파일(line 172~175, 45 regex)뿐 — import-safe. brief §2.1 옵션 (i) 재사용에 **기술적 장애 없음**.
- **N-5 (COMPILED_PATTERNS 구조)**: `list[tuple[pid, src, cat, vendor, re.Pattern]]` (line 172). re.sub 직접 사용 가능 — RedactionFilter가 5-tuple 중 [4](Pattern)만 추출하면 됨. `SKIP_DIRECT_REGISTER`(line 178, T1-038/040)는 redaction에서도 동일 제외 필요 (scan_text line 239 답습) — brief 미언급, 구현 시 반영 필요.
- **N-6 (성능 비-이슈 실측)**: 45 패턴 × re.sub, 메시지 ~2175 chars 기준 **per-message ~211μs, full request(10 msg) ~2.1ms**. LLM 네트워크 latency(수백ms~수초) 대비 무시 가능. brief RT-5(line 205) "성능" 우려 = COMPILED_PATTERNS 사전 compile로 이미 해소 — **실측 확인**.
- **N-7 (tools namespace package)**: `import tools` → `_NamespacePath([...tools])` PEP-420 namespace package로 동작. `tools/__init__.py` 부재(실측)에도 `from tools.secret_scanner import`가 repo root sys.path 환경에서 동작.

---

## 5. catalog 재사용 (i)/(ii) 기술적 권고

### **추천: 옵션 (i) `from tools.secret_scanner import COMPILED_PATTERNS` (namespace package), 단 BLOCKING-1 정정 조건부**

**근거 (filesystem 실측)**:

| 평가축 | (i) tools import | (ii) 공유 모듈 추출 |
|---|---|---|
| secret_scanner "변경 0건" (R-4.1) | ✅ **변경 0** | ❌ secret_scanner 본문 수정 = R-7(b) 차등 |
| 런타임 동작 | ✅ namespace package OK (실측 45 반환) | ✅ OK |
| import-linter contract | ✅ tools = forbidden 아님 (실측 KEPT) | ✅ src 내부 모듈 |
| single source (detection↔prevention) | ✅ 동일 객체 참조 | ✅ 둘 다 공유 모듈 import |
| 의존 방향 | ⚠️ src→tools (run-from-source라 동작상 무해) | ✅ src 내부 정합 |
| 구현 비용 | **낮음** (import 1줄) | 높음 (추출 + secret_scanner 리팩토링 + 회귀 test) |

**결론**: 본 cycle scope가 "RedactionFilter 집중 + secret_scanner 변경 0건"(brief line 36, §0.2 #5)임을 고려할 때, **옵션 (i)가 R-4.1 "변경 0건" 답습에 가장 충실**하며 import-linter 위반 0(실측), 런타임 동작 OK(실측). brief 권고 (i) 우선과 **일치**. 단 **반드시 namespace package 형태(`from tools.secret_scanner import`)로 고정**(BLOCKING-1) — bare import는 런타임 깨짐(실측).

옵션 (ii)는 의존 방향이 더 idiomatic하나 secret_scanner 변경 = R-7(b) 차등 트리거 + 추가 회귀 비용 → **fallback 적절** (brief RT-2 line 202와 일치). "의존 방향이 진짜 BLOCKING이냐"는 **아키텍처 선호 판단**(Reviewer/사용자 영역)이지 동작 BLOCKING 아님(실측).

---

## 6. 구현 가능성 평가

### 6.1 redaction layer 통합 — **가능 (실측)**
- facade.py(41 LOC placeholder) complete()에 redact_messages 후 NotImplementedError raise = 기술적 가능. RedactionFilter frozen 순수 함수면 raise 전 redact 호출 안전. 시그니처 최소 변경(brief §4.3 line 124) = over-engineering 회피로 타당. **단 BLOCKING-2 (whole-match 의미 손상)** 명문 + dict 구조 무결성 test 필요.

### 6.2 catalog 재사용 — **가능 (실측)**
- COMPILED_PATTERNS re.sub 직접 동작 확인. secret_scanner import-safe(부작용 0, N-4). SKIP_DIRECT_REGISTER 제외 반영 필요(N-5). secret_scanner 변경 0(옵션 i). namespace package import 동작(N-7).

### 6.3 TDD — **가능, 단 보강 필요**
- pytest baseline 152 green(N-1). tests/adapters/llm/ 신규 생성 필요(권고-1). T-1~T-6 실현 가능. **보강**: (가) T-6 순서 검증은 spy/mock 필요(raise로 반환값 도달 불가, 권고-3), (나) dict 구조 무결성 test 추가(BLOCKING-2), (다) SKIP_DIRECT_REGISTER 제외 동작 test. 커버리지 70%+(brief line 148)는 RedactionFilter가 작은 순수 모듈이라 달성 용이.

### 6.4 종합
**redaction layer 통합 + catalog 재사용 + TDD 모두 기술적으로 실현 가능**. BLOCKING-1(import 형태/단점 framing 정정), BLOCKING-2(whole-match 의미 손상 명문 + 구조 무결성 test) 2건 정정 후 구현 진입 적절. 성능·import-safe·import-linter·pytest baseline 모두 실측으로 GREEN 확인.

---

**Agent A (구현 분석가) 독립 분석 끝. (Agent B/C·외부 LLM 미참조)**
