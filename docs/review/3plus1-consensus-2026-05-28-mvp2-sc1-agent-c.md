# 3+1 합의 — Agent C (대안 탐색가) — MVP-2 SC-1 facade RedactionFilter 구현 brief (v1)

> **검토 대상**: `docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md` (v1, §0~§11)
> **작성**: 2026-05-28 (65번째 entry cycle — 세션 #3, TR-1 풀 3+1)
> **관점**: "더 나은 방법이 있는가?" (대안 기술, 트레이드오프)
> **독립성**: Agent A/B 및 외부 LLM 응답 미참조 (편향 방지). brief + facade.py + secret_scanner.py + llm-providers-design §4.1/§4.4/§8.2 + .importlinter + tests 구조 직접 read + 실증 검증.

---

## 1. 판정

### **APPROVE WITH CONDITIONS**

brief 의 scope 절제(RedactionFilter 집중, Router deferred), 명칭 정직성(§0 over-claim 차단), R-4.1 "변경 0건" 보존, RT-1 window 회피(선부착) 설계는 견고하다. 그러나 **대안 탐색 관점에서 2건의 BLOCKING 정정**이 구현 전 필요하다:

1. **catalog 재사용 (i) 의 import 메커니즘이 brief 기술과 실제 코드베이스 구조 불일치** — brief 는 `from tools.secret_scanner import COMPILED_PATTERNS` 를 (i) 로 기술하나, 실제 코드베이스는 `tools/__init__.py` 부재 + pytest rootdir/CWD 의존 namespace package 로만 동작. 런타임 src→tools import 의 **취약성(CWD 종속, packaging 부재)** 이 brief 4 옵션 표에 미반영. → **B-1**
2. **redaction 전략 "`[REDACTED]` 전체 치환" 이 catalog 의 group 구조와 의미 충돌** — catalog regex 5종(T1-032/033/034/036/039)은 group 1=비-secret 컨텍스트(key 이름/prefix), group N=secret 값 으로 **detection(full-match 보고)용** 설계. 전체 치환 시 §8.2 설계 의도(`OPENAI_API_KEY=[REDACTED]` — key 이름 보존)와 불일치 + JSON 구조 파괴 + word-joining artifact. → **B-2**

조건 충족 시 구현 진입 무방. scope 자체는 본 cycle 최적에 가깝다 (§5 대안 매트릭스 scope 행 참조).

---

## 2. BLOCKING (구현 전 정정 필수)

### B-1: catalog 재사용 (i) 의 import 메커니즘 — brief 기술 vs 실제 구조 불일치 + 취약성 미반영

**근거 (실증)**:
- brief §2.1 (i) = "RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import". 단점란은 "src(런타임)→tools(개발도구) 역방향 의존(아키텍처 부적절, .importlinter root=src 밖이라 미차단이나 nonidiomatic)" 만 기재.
- **실제 코드베이스 구조 (직접 확인)**:
  - `tools/__init__.py` **부재** → `tools` 는 정규 package 아님 (PEP 420 namespace package 로만 동작).
  - 루트에 `pyproject.toml` / `setup.cfg` / `pytest.ini` / `setup.py` **전부 부재** → 어떤 packaging/install 도 없음. `src` 가 import 되는 이유는 pytest 가 rootdir(repo 루트)를 sys.path 에 넣기 때문.
  - 기존 tools 사용 선례 `tests/tools/test_jsonl_hash_chain.py` line 16: `sys.path.insert(0, str(_ROOT / "tools"))` 후 `import jsonl_hash_chain` — **tools 를 top-level 모듈로 sys.path 조작 로드** (package import 아님).
- **실증 결과**: `python3 -c "import tools.secret_scanner"` 는 repo 루트 CWD 에서 **동작함** (Python 3.12 namespace package). 그러나 이는 **CWD=repo 루트 + tools 가 sys.path[0] 의 하위** 라는 우연한 조건에 의존. jarvis 런타임(서비스/CLI entry point)이 다른 CWD 에서 실행되면 `import tools.secret_scanner` 는 **ImportError 또는 잘못된 모듈 해석** 위험.

**문제**: brief 가 권고하는 (i) 는 "변경 0건 충실" 이라는 장점만 부각하나, 실제로는 **런타임 import 가 CWD/packaging 부재에 종속되는 취약 메커니즘**. 이는 단순 "nonidiomatic" 이 아니라 **production 런타임 실패 가능성**. RedactionFilter 는 GP-2 prevention 의 핵심 런타임 경로(매 LLM 송신)이므로, import 실패 = redaction 미적용 = secret 누출(fail-open) 또는 facade crash.

**정정 요구 (택1, 풀 3+1 결정)**:
- (a) (i) 채택 시 **import 메커니즘 명시**: RedactionFilter 가 `tests/tools/*` 선례처럼 `sys.path.insert` + top-level import 를 src 런타임에 넣는 것은 **부적절**(src 가 sys.path 를 조작하는 anti-pattern). 따라서 (i) 는 **packaging 정비(`tools/__init__.py` + pyproject 추가) 선행** 없이는 채택 불가 → 별도 sub-cycle 의존 → 본 cycle scope 초과.
- (b) **catalog 데이터 외부화 (신규 옵션, §5 매트릭스 (v) 참조)**: catalog 를 `data/secret_patterns.json` (또는 yaml) 로 외부화 → secret_scanner + RedactionFilter **양쪽이 데이터 로드**. import 방향 의존 0 + single source + secret_scanner 본문 패턴 변경 0(데이터 이동만이나, R-4.1 "변경 0건" 해석은 풀 3+1). **단점: secret_scanner 의 catalog *위치* 변경 = R-7(b) 차등 평가 대상** (B-2 와 동일 R-7(b) 게이트).
- (c) **(ii) 공유 모듈 추출 채택 + R-7(b) 차등 명시적 수용**: brief 가 (ii) fallback 으로 둔 것을 본 cycle 1순위로 승격. catalog 를 `src/adapters/llm/redaction_patterns.py` (런타임 적절 위치)로 두고 secret_scanner 가 이를 import (방향 정상: tools→src 는 개발도구가 런타임 자산 참조, idiomatic). **secret_scanner 변경 = "패턴 내용 변경 0 + import 출처만 변경" → R-7(b) 차등 평가** (내용 동등성 유지 시 R-4.1 정신 보존).

**권고 방향**: 본 Agent C 는 **(c) 또는 (b)** 를 (i) 보다 우선 권고. 이유: (i) 의 "변경 0건" 은 *표면적 무변경* 일 뿐, **런타임 취약성을 도입**하는 대가. detection↔prevention single source 라는 R-2-c 목표는 (b)/(c) 가 (i) 와 동등하게 달성하면서 import 방향이 정상. R-4.1 "변경 0건" vs "런타임 건전성" 트레이드오프에서 후자가 GP-2 prevention 의 본질(런타임 secret 차단)에 더 부합. **단 R-7(b) 차등 자격 = 풀 3+1 + 사용자 결정 영역** 이므로 본 brief 가 (i) 단정 대신 4(+2)옵션을 풀 3+1 에 올린 절차는 정당.

---

### B-2: redaction 전략 "`[REDACTED]` 전체 치환" 이 catalog group 구조 및 §8.2 설계 의도와 충돌

**근거 (실증 — catalog group 구조 분석)**:

catalog 45 패턴의 capture group 구조는 **detection(full-match 보고)용** 으로 이질적:

| 분류 | 패턴 | groups | full-match = ? |
|------|------|--------|----------------|
| prefix 36 (BL-1~5, T1-001~031) | `sk-ant-...`, `ghp_...` 등 | 0 | full-match = secret 자체 ✅ 전체 치환 적절 |
| regex 컨텍스트 보존형 | T1-032 ENV(`KEY=VALUE`) | 3 | full-match = `KEY=VALUE` 전체 (key 이름 포함) |
| | T1-033 JSON(`"key":"val"`) | 2 | full-match = `"api_key":"secret"` 전체 |
| | T1-034 Bearer(`Authz: Bearer X`) | 2 | full-match = `Authorization: Bearer X` 전체 |
| | T1-036 DB connstr | 3 | full-match = `proto://user:pass@` 전체 |
| | T1-039 URL userinfo | 3 | full-match = `proto://user:pass@` 전체 |
| regex full-secret | T1-035 PEM, T1-037 JWT | 0 | full-match = secret 자체 ✅ |
| alternation | T1-041/042 | 0 | full-match = `\s key=value` (leading delimiter 포함) |

**실증 (전체 치환 결과)**:
```
IN : OPENAI_API_KEY=sk-proj-abcdefghij1234567890
OUT: [REDACTED]                          ← key 이름 OPENAI_API_KEY 통째 소실
IN : {"api_key": "secret-value-here-123456"}
OUT: {[REDACTED]}                        ← JSON 구조 파괴 (key 이름 소실, 비유효 JSON)
IN : the config has token=hunter2abcdef in the url ?token=hunter2abcdef
OUT: the config has[REDACTED] in the url [REDACTED]   ← leading space 소실 → word-joining artifact "has[REDACTED]"
IN : curl https://user:p4ssw0rdXYZ@host/path
OUT: curl [REDACTED]host/path            ← @ 경계 소실
```

**문제**:
1. **§8.2 설계 의도와 불일치**: brief §2.2 는 `is_redaction_marker_match` 답습 + §8.2 답습 주장. 그러나 §8.2 예시 (line 226) 는 `OPENAI_API_KEY=[REDACTED]` (**key 이름 보존, 값만 마스킹**). 이는 **group-preserving 치환(`\1[REDACTED]` 등)** 을 전제. brief 의 "전체 치환" 은 §8.2 의도를 미준수.
2. **secret_scanner D-2 contract 와의 정합 깨짐 가능**: secret_scanner `is_redaction_marker_match` (line 222) 는 *redaction 후 잔존 검증* 시 marker-only 매칭을 위반 미카운트. 그런데 T1-032(ENV) 가 `OPENAI_API_KEY=[REDACTED]` 를 다시 매칭하면 marker 가 group 3(값) 위치이므로 `is_redaction_marker_match` 가 정상 분류. 그러나 **전체 치환 `[REDACTED]` 단독** 은 T1-032 가 재매칭하지 않으므로 D-2 검증은 통과하나, 출력 가독성/구조 손상은 그대로.
3. **정상 내용 손상 (RT-3 / P-5 자기진단 부족)**: brief P-5 는 "Tier-1 secret 패턴 한정" 으로 false positive 를 봉쇄했다 주장하나, **false positive 가 아닌 true positive 의 over-redaction**(컨텍스트 과다 제거)은 별개 문제. JSON 구조 파괴는 응답/로그 redaction(scrub) 시 downstream parser 를 깨뜨릴 수 있음.

**정정 요구**:
- **redaction 치환을 group-aware 로 명세**: 0-group prefix/PEM/JWT/alternation → `[REDACTED]` 전체 치환 유지. **capture group 보유 패턴(T1-032/033/034/036/039) → 컨텍스트 group 보존 + secret group 만 `[REDACTED]`** (예: T1-034 → `\1[REDACTED]`, T1-032 → `\1\2[REDACTED]`). 이는 §8.2 의도 충실 + 구조 보존.
- **단, 이는 패턴별 치환 템플릿 메타데이터 필요** → catalog 가 현재 `(id, source, cat, vendor, regex)` 5-tuple 이므로 **치환 템플릿(group 인덱스)을 RedactionFilter 측에서 category 기반 매핑**(prefix/alternation→full, regex→group-aware)으로 도출 가능 (secret_scanner 변경 0 유지). category 필드가 이미 존재(§2.1 (i)/(ii) 어느 옵션이든 보존)하므로 RedactionFilter 가 category→치환전략 dispatch.
- **대안 (단순화 fallback)**: 전체 치환을 유지하되 brief 에 **"구조/컨텍스트 손상은 known behavior, 송신 차단 우선(보안 > 가독성)" 을 명문**하고 RT/Evidence 에 over-redaction case 를 T-test 로 고정. 단 §8.2 설계 불일치는 잔존하므로 **§8.2 본문과의 정합성 노트** 필요(설계는 group 보존인데 구현은 전체 치환 = 설계↔코드 drift).

**권고 방향**: **group-aware 치환** 을 1순위 권고 (§8.2 충실 + 구조 보존). 구현 복잡도가 부담이면 **category 기반 2-전략 dispatch**(full vs group1-preserving)가 최소 절충. 전체 치환 단독은 보안상 안전(secret 누출 0)하나 §8.2 drift + 출력 손상의 대가가 있음을 brief 가 명시적으로 인정해야 함.

---

## 3. 권고 (non-blocking, 채택 시 품질 향상)

### G-1: redaction 적용 지점 — facade `complete()` 직접 호출 = 본 cycle 최적, 단 callback 추상화 여지 명시
- brief §4 = facade `complete()` 내부 `redact_messages` 직접 호출. Router deferred 상황에서 callback hook(§8.1 `litellm.success_callback`)은 **litellm 미설치 + Router 미존재** 이므로 사용 불가 → 직접 호출이 **현 시점 유일하게 동작하는 적용 지점**. 채택 정당.
- **권고**: brief §4.1 에 "Router/callback 발효 시 redaction 적용 지점이 callback 으로 *이동* 하는가, 아니면 facade 직접 호출이 *유지* 되는가" 의 미래 결정을 **deferred note** 로 명문. 송신 redaction(request body)은 callback(success/failure = *응답 후*)으로는 커버 불가 — callback 은 응답/로그/메트릭(scrub) 전용. **즉 송신 redaction 은 영구히 facade complete() 직접 호출, callback 은 응답/메트릭 redaction** 으로 역할 분리됨을 명시하면 미래 RT 회피.

### G-2: 송신 vs 응답 redaction 우선순위 — brief 의 "송신 우선" 은 정당, 단 본 cycle scope 명확화
- 개념 #3 검토 결과: GP-2 prevention 의 governance §4.1 line 422 verbatim 은 "**LLM API request body 에 secret 노출 차단**" = **송신 경로**. §8.2 설계가 scrub(응답/메트릭) 중심으로 *코드 예시* 를 든 것은 **R3 보강(관측성 redaction)** 맥락이지 GP-2 prevention 의 본질이 응답이라는 의미 아님. brief 가 송신 우선으로 본 것은 **governance 본질에 정확히 부합**.
- **권고**: brief §3 line 98~99 가 이미 "송신=핵심, 응답/로그=보조" 로 구분하나, §5 TDD T-5(scrub)와 T-2/T-6(송신)의 **우선순위/필수성 차등** 을 명시. 본 cycle 필수 = 송신(redact_messages); scrub(응답/메트릭)은 **callback/Router 발효 전까지 호출처 없음** → scrub 구현은 인터페이스만 두고 *적용 통합* 은 deferred 로 둘 수 있음(over-engineering 회피, §4.3 정신 일관). 즉 **scrub 를 본 cycle 에 풀 구현할지(인터페이스+적용 vs 인터페이스만)** 를 brief 가 결정.

### G-3: scope — RedactionFilter 집중 = 본 cycle 최적 (대안 대비 우월)
- 개념 #4 검토: scope 대안 4종(매트릭스 §5 참조) 중 **RedactionFilter 집중(Router deferred)** 이 (a) Provider Liquidity sub-cycle 분리(5조-2 비협상 별도 검증 보장), (b) RT-1 선부착(window 0), (c) over-claim 차단(facade real ≠ redaction layer real) 을 동시 달성. **채택 정당, 변경 권고 없음**.

### G-4: TDD — property-based test (hypothesis) 보강 권고
- 개념 #6 검토: brief §5.1 T-1~T-6 은 example-based. **false positive 0 (T-4) 와 over-redaction(B-2) 검증** 에는 **property-based test 가 우월**:
  - **속성 1 (idempotency)**: `redact(redact(x)) == redact(x)` — 이미 redacted 된 출력 재처리 시 변화 0 (marker 재매칭 회피 검증).
  - **속성 2 (secret 부재 → 무변경)**: hypothesis 로 secret 패턴 미포함 랜덤 문자열 생성 → `redact(x) == x` (T-4 강화, false positive fuzzing).
  - **속성 3 (secret 존재 → marker 포함 + 원 secret 부재)**: catalog 대표 secret 삽입 텍스트 → 출력에 `[REDACTED]` 포함 + 원 secret substring 부재.
- **권고**: hypothesis 미설치 시 도입 비용(의존성)이 있으므로 **선택적**. 최소한 idempotency(속성 1)는 example test 로 추가 권고 — D-2 contract(`is_redaction_marker_match`)와 직접 연관.

### G-5: 성능 (RT-5) — COMPILED_PATTERNS 재사용 + 매 송신 45 패턴 검토
- brief RT-5 = COMPILED_PATTERNS 사전 compile 로 완화. 타당. **추가 권고**: 매 LLM 송신마다 message 배열 전체 × 43 active 패턴(45 - SKIP 2) 매칭은 긴 컨텍스트(수만 토큰)에서 비용 발생 가능. 본 cycle 측정 불필요(성능 회귀 sub-cycle)하나, **Evidence E-1 에 "redaction latency 측정 deferred (성능 sub-cycle)" 명문** 으로 미래 RT 회피.

---

## 4. NOTE (관찰)

- **N-1**: facade.py 현 placeholder 시그니처 `LLMRequest(alias, messages, metadata)` vs 설계 §4.1 `LLMRequest(messages, model_alias, system, ...)`. brief §4.3 가 "시그니처 전면 개편 deferred, 현 placeholder 기반 최소 변경" 결정 = over-engineering 회피로 타당. **단 `system` 필드 부재** → 설계 §4.1 의 `system` 도 redaction 대상(secret 포함 가능)인데 현 placeholder 에 없음. 본 cycle 은 `messages` redaction 만 가능(system 필드 미존재). **brief §3 line 97 "(+ `system`)" 은 현 placeholder 에 system 필드가 없으므로 적용 불가** → §4.3 deferred 와 일관되게 "system redaction = 시그니처 정비 sub-cycle 과 함께 deferred" 명문 권고 (현재 §3 와 §4.3 간 미세 불일치).
- **N-2**: import-linter 현재 KEPT (1 contract, 0 broken — 실증 확인). (i) src→tools import 는 root_packages=src 밖이라 import-linter 미차단 = brief 기술 정확. 단 B-1 의 런타임 취약성은 import-linter 가 잡지 못하는 *별개 차원*(lint 통과 ≠ 런타임 건전).
- **N-3**: secret_scanner SKIP_DIRECT_REGISTER (T1-038/040) 는 scan 에서 제외되나, RedactionFilter 가 COMPILED_PATTERNS 를 순회할 때 **동일 SKIP 적용 의무**. brief §5 GREEN 이 이를 명시하지 않음 → 구현 시 `if pid in SKIP_DIRECT_REGISTER: continue` 누락 시 false positive 도입 위험. **구현 note 로 SKIP 답습 명문 권고**.
- **N-4**: brief P-7 (작성자=64 작성자 Claude cascade) → cross-vendor codex + 본 풀 3+1 독립 검증으로 완화. 본 Agent C 검증이 그 일부. 적절.
- **N-5**: catalog 의 ElevenLabs(T1-023) regex `sk_[A-Za-z0-9_]{10,}` 와 OpenAI baseline(BL-2) `sk-...` 는 prefix 충돌 없음(`sk_` vs `sk-`). redaction 시 양쪽 다 매칭되어도 동일 `[REDACTED]` 출력이므로 무해. NOTE only.

---

## 5. 대안 매트릭스

### 5.1 catalog 재사용 (개념 #1)

| 옵션 | 방식 | single source | import 방향 | secret_scanner 변경 | 런타임 건전성 | 채택 권고 |
|------|------|:---:|:---:|:---:|:---:|---|
| (i) src→tools import | `from tools.secret_scanner import COMPILED_PATTERNS` | ✅ | ❌ 역방향 | 0 ✅ | ❌ **CWD/packaging 종속 취약** (B-1 실증) | **비채택 권고** (취약성 > 무변경 이득) |
| (ii) 공유 모듈 추출 (brief fallback) | catalog → `src/.../redaction_patterns.py`, secret_scanner import | ✅ | ⚠️ tools→src (정상이나 secret_scanner 변경) | 출처만 변경(내용 0) → R-7(b) | ✅ | **조건부 1순위** (R-7(b) 차등 통과 시) |
| (iii) 복제 | Tier-1 45 복사 | ❌ drift 위험 | 무관 | 0 | ✅ | **비채택** (single source 위반) |
| (iv) §8.2 자체 (4 패턴 + 6 키) | 설계 §8.2 직접 | ❌ 커버리지↓(45→4) | 무관 | 0 | ✅ | **비채택** (R-2-c 미달, detection↔prevention 비대칭) |
| **(v) 데이터 외부화 (신규)** | catalog → `data/secret_patterns.json`, 양쪽 로드 | ✅ | ✅ 의존 0 | 위치만(R-7(b)) | ✅ (로드 실패 fail-safe 필요) | **공동 1순위 후보** (의존 방향 0 + single source) |
| (vi) tools 하위 배치 (신규) | RedactionFilter 를 `tools/` 에 배치 | ✅ | — | 0 | ❌ 런타임 협력자를 개발도구 디렉토리에 = src facade 가 tools import = (i) 와 동일 취약 | **비채택** ((i) 와 동형 문제) |

**Agent C 종합 권고**: **(ii) 또는 (v)** 를 (i) 보다 우선. (i) 의 "변경 0건" 은 표면적이며 런타임 취약성을 도입. R-7(b) 차등 게이트(패턴 *내용* 변경 0, *위치/출처* 만 변경)는 풀 3+1 + 사용자 결정 영역 — brief 가 (i) 단정 대신 옵션을 올린 절차는 정당하나, **brief 의 "(i) 우선" 디폴트 권고는 런타임 취약성 미반영 → 재고 요구(B-1)**.

### 5.2 redaction 적용 지점 (개념 #2)

| 옵션 | 시점 | 송신 redaction 가능 | Router deferred 동작 | 채택 권고 |
|------|------|:---:|:---:|---|
| **facade complete() 직접 호출 (brief)** | 송신 *전* (Router 위임 전) | ✅ | ✅ (현 유일 동작 지점) | **채택** (G-1) |
| litellm callback (success/failure) | 응답 *후* | ❌ (응답/로그만) | ❌ (litellm 미설치) | **비채택** (송신 미커버 + Router deferred) |
| 별도 middleware/decorator | complete 래핑 | ✅ | ✅ | 비채택 (facade 단일 진입점 ADR-009 §2.2 와 중복 layer, over-engineering) |

**종합**: facade 직접 호출 채택 정당. **송신 redaction 은 영구히 facade 직접 호출**(callback 은 응답 후라 송신 커버 불가) — G-1 명문 권고.

### 5.3 redaction 전략 (개념 #5)

| 전략 | 보안(누출 차단) | 컨텍스트 보존 | §8.2 정합 | catalog group 정합 | 채택 권고 |
|------|:---:|:---:|:---:|:---:|---|
| `[REDACTED]` 전체 치환 (brief) | ✅ 강 | ❌ (구조 파괴, B-2 실증) | ❌ (§8.2 = key 보존) | ❌ (group 무시) | **조건부** (보안 우선 시, 단 §8.2 drift 명문 필요) |
| **group-aware 치환** (prefix→full, regex→`\1...[REDACTED]`) | ✅ 강 | ✅ | ✅ | ✅ | **1순위 권고** (B-2) |
| category 기반 2-전략 dispatch | ✅ 강 | ⚠️ 중 | ⚠️ 부분 | ⚠️ 부분 | **2순위** (절충, secret_scanner 변경 0) |
| 부분 마스킹 (`sk-***last4`) | ⚠️ last4 노출 | ✅ | — | — | **비채택** (GP-2 = 노출 차단, last4 도 노출. 송신엔 부적절) |
| drop (필드 삭제) | ✅ | ❌ (메시지 소실) | — | — | 비채택 (대화 내용 손상) |

**종합**: GP-2 목적 = 노출 차단이므로 **부분 마스킹(last4)은 송신엔 부적절**(아무리 적어도 노출). `[REDACTED]` 마커 치환이 옳은 방향이나, **group-aware** 로 컨텍스트 보존 + §8.2 충실(B-2). 전체 치환 단독 시 §8.2 drift 인정 + over-redaction T-test 필수.

### 5.4 scope (개념 #4)

| scope 대안 | Provider Liquidity 분리 | RT-1 window | over-claim 위험 | 본 cycle 적합 | 채택 권고 |
|------|:---:|:---:|:---:|:---:|---|
| **RedactionFilter 집중 (brief)** | ✅ (Router 별도) | 0 (선부착) | 낮음 (§0 정직성) | ✅ | **채택** (G-3) |
| facade real 전체 동시 (Router+Min2+registry+redaction) | ❌ (Liquidity 미분리 검증) | — | 높음 ("facade real 완성") | ❌ (litellm 의존+yaml+검증 대량) | 비채택 (5조-2 별도검증 손실 + over-claim) |
| RedactionFilter 독립 모듈만 (facade 미통합) | ✅ | ⚠️ (통합 시점 window 가능) | 낮음 | ⚠️ (GP-2 (a) "facade redaction filter" 미충족) | 비채택 (facade 통합 = GP-2 Exit (a) 핵심) |
| facade callback 만 | ❌ | — | 낮음 | ❌ (송신 미커버 + litellm 의존) | 비채택 (송신 redaction = GP-2 본질 미달) |

**종합**: **RedactionFilter 집중 = 본 cycle 최적**. Provider Liquidity 별도 검증 보존(5조-2) + RT-1 선부착 + GP-2 Exit (a) 충족 + over-claim 차단을 동시 달성. 변경 권고 없음.

---

## 6. 종합

| 항목 | 결론 |
|------|------|
| **판정** | **APPROVE WITH CONDITIONS** |
| **BLOCKING** | B-1 (catalog (i) import 메커니즘 취약성 + brief 기술 불일치 → (ii)/(v) 재고), B-2 (전체 치환 vs catalog group 구조/§8.2 충돌 → group-aware 권고) |
| **권고** | G-1 (적용 지점 송신=facade 영구, callback=응답 deferred), G-2 (scrub 풀 구현 vs 인터페이스만 결정), G-3 (scope 집중 채택), G-4 (property-based/idempotency test), G-5 (latency deferred 명문) |
| **NOTE** | N-1 (system 필드 부재 → §3/§4.3 미세 불일치), N-2 (import-linter ≠ 런타임 건전), N-3 (SKIP_DIRECT_REGISTER 답습 의무), N-4 (cascade 완화 적절), N-5 (sk_/sk- 무충돌) |
| **scope 평가** | RedactionFilter 집중 = 4 대안 중 최적 (변경 불요) |
| **catalog 재사용** | (i) 비채택 권고, (ii)/(v) 우선 — R-7(b) 차등 = 풀 3+1+사용자 결정 |
| **redaction 전략** | group-aware 1순위, 전체 치환은 §8.2 drift 인정 시 조건부 |

**핵심 메시지 (대안 탐색가)**: brief 의 scope·절차·명칭 정직성은 견고하다. 그러나 **(1) catalog 재사용 (i) 의 "변경 0건" 은 런타임 취약성(CWD/packaging 종속, B-1 실증)을 도입하므로 (ii)/(v) 가 우월**하고, **(2) "전체 치환" 은 catalog 가 detection 용으로 설계한 group 구조 및 §8.2 의 key-보존 의도와 충돌(B-2 실증)** 하므로 group-aware 치환이 더 낫다. 두 BLOCKING 모두 "더 나은 방법이 있는가?" 에 대한 명확한 YES 이며, 보안 안전성을 해치지 않으면서 런타임 건전성·설계 정합성을 높이는 대안이 존재한다.

---

**Agent C (대안 탐색가) 독립 분석 끝.**
