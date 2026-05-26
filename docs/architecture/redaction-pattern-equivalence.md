# Redaction Pattern Equivalence (R-4)

> **ADR-011 §2.1 (a) "동등 이상 보장" 검증 의무의 직접 충족 작업 — 코드 변경 없는 패턴 비교 + gap 식별 + 보충 권고 문서화**

**상태**: 작성 (R-4 단축 검증 — 코드 수정 미포함)
**날짜**: 2026-05-06
**상위 권위**: ADR-011 §2.1 (a) (대체 수단 동등 이상 보장 검증 의무), §3 R-4 매핑
**모법 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
**갱신 대상**: ADR-008 부록 B B.6 R-4 항목 ⏳ → 본 문서 발행 시 ✅
**산출 의도**: trigger UDF 보충 권고 카탈로그 — 실제 보충 코드 작성은 별도 작업 (보충 자체도 ADR-011 §2.1 (a)~(d) 4조건 적용 대상)

---

## 1. 작업 정의

### 1.1 본 R-4의 본질 (사용자 명시)

> **이번 단계의 핵심은 "코드 수정"이 아니라 "패턴 추출 → 비교 → gap 식별 → 보충 권고 문서화"이다.**

본 문서는 다음 4단계를 산출한다:

| # | 단계 | 산출 §  |
|---|------|--------|
| 1 | **추출** — Hermes / P1_REDACTOR / R-2 trigger UDF 패턴 카탈로그 | §2 / §3 / §4 |
| 2 | **비교** — 3-way 동등성 매트릭스 | §5 |
| 3 | **gap 식별** — Tier 1/2/3 분류 | §6 |
| 4 | **보충 권고** — trigger UDF 확장 카탈로그 (코드 미작성) | §7 |

### 1.2 ADR-011 §2.1 (a) 충족 의무

> **(a) 동등 이상의 보안 결과 — 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장)**

본 문서 §5의 3-way 비교표가 (a) 직접 충족 산출이다. 본 문서는 보안 결과를 *선언*하지 않으며, 비교 사실과 gap을 *기록*한다 — gap이 미보충 상태에서 G1b 정식 충족 (ADR-008 부록 B.6) 진입 불가.

### 1.3 본 문서가 *하지 않는* 것

- ❌ trigger UDF 패턴 코드 수정 — 본 문서는 *권고 카탈로그*이며 보충 작업은 별도 작업으로 분리 (ADR-011 §2.1 (b) "격리 환경 PoC 실증" 의무 별도 적용)
- ❌ Hermes redaction 우회 가능성 평가 — base64 우회 등은 R-2 PoC §6 향후 검증 항목 + R-7 SOP 영역
- ❌ Hermes 안전성 선언 — ADR-011 §7.3 "본 ADR은 Hermes 안전성을 선언하지 않는다" 위반 금지
- ❌ P1_REDACTOR ↔ R-2 trigger UDF 직접 비교의 우선시 — P1_REDACTOR는 P1 facade 호출 경로 한정 (LiteLLM callback). DB INSERT 차단의 기준선은 Hermes 패턴 카탈로그 (광역 수단)

---

## 2. Hermes 패턴 카탈로그 추출

**출처**: `/tmp/hermes-phase0/hermes-agent/agent/redact.py` (v0.12.0 main HEAD, 401 LOC)
**docstring 명시 (line 1-2)**: "Regex-based secret redaction for logs and tool output"
**적용 범위**: 로그/도구 출력/LLM 송신 — DB INSERT 미적용 (R-1 FAIL 확정, ADR-011 §2.2 G1a)

### 2.1 `_PREFIX_PATTERNS` (35종, line 67-103)

| # | Vendor / Type | Regex | 출처 라인 |
|---|------|------|------|
| 1 | OpenAI / OpenRouter / Anthropic (`sk-ant-*`) | `sk-[A-Za-z0-9_-]{10,}` | 68 |
| 2 | GitHub PAT (classic) | `ghp_[A-Za-z0-9]{10,}` | 69 |
| 3 | GitHub PAT (fine-grained) | `github_pat_[A-Za-z0-9_]{10,}` | 70 |
| 4 | GitHub OAuth access token | `gho_[A-Za-z0-9]{10,}` | 71 |
| 5 | GitHub user-to-server | `ghu_[A-Za-z0-9]{10,}` | 72 |
| 6 | GitHub server-to-server | `ghs_[A-Za-z0-9]{10,}` | 73 |
| 7 | GitHub refresh token | `ghr_[A-Za-z0-9]{10,}` | 74 |
| 8 | Slack tokens | `xox[baprs]-[A-Za-z0-9-]{10,}` | 75 |
| 9 | Google API keys | `AIza[A-Za-z0-9_-]{30,}` | 76 |
| 10 | Perplexity | `pplx-[A-Za-z0-9]{10,}` | 77 |
| 11 | Fal.ai | `fal_[A-Za-z0-9_-]{10,}` | 78 |
| 12 | Firecrawl | `fc-[A-Za-z0-9]{10,}` | 79 |
| 13 | BrowserBase | `bb_live_[A-Za-z0-9_-]{10,}` | 80 |
| 14 | Codex encrypted tokens | `gAAAA[A-Za-z0-9_=-]{20,}` | 81 |
| 15 | AWS Access Key ID | `AKIA[A-Z0-9]{16}` | 82 |
| 16 | Stripe secret key (live) | `sk_live_[A-Za-z0-9]{10,}` | 83 |
| 17 | Stripe secret key (test) | `sk_test_[A-Za-z0-9]{10,}` | 84 |
| 18 | Stripe restricted key | `rk_live_[A-Za-z0-9]{10,}` | 85 |
| 19 | SendGrid API key | `SG\.[A-Za-z0-9_-]{10,}` | 86 |
| 20 | HuggingFace token | `hf_[A-Za-z0-9]{10,}` | 87 |
| 21 | Replicate API token | `r8_[A-Za-z0-9]{10,}` | 88 |
| 22 | npm access token | `npm_[A-Za-z0-9]{10,}` | 89 |
| 23 | PyPI API token | `pypi-[A-Za-z0-9_-]{10,}` | 90 |
| 24 | DigitalOcean PAT | `dop_v1_[A-Za-z0-9]{10,}` | 91 |
| 25 | DigitalOcean OAuth | `doo_v1_[A-Za-z0-9]{10,}` | 92 |
| 26 | AgentMail API key | `am_[A-Za-z0-9_-]{10,}` | 93 |
| 27 | ElevenLabs TTS key | `sk_[A-Za-z0-9_]{10,}` | 94 |
| 28 | Tavily search API | `tvly-[A-Za-z0-9]{10,}` | 95 |
| 29 | Exa search API | `exa_[A-Za-z0-9]{10,}` | 96 |
| 30 | Groq Cloud API key | `gsk_[A-Za-z0-9]{10,}` | 97 |
| 31 | Matrix access token | `syt_[A-Za-z0-9]{10,}` | 98 |
| 32 | RetainDB API key | `retaindb_[A-Za-z0-9]{10,}` | 99 |
| 33 | Hindsight API key | `hsk-[A-Za-z0-9]{10,}` | 100 |
| 34 | Mem0 Platform API key | `mem0_[A-Za-z0-9]{10,}` | 101 |
| 35 | ByteRover API key | `brv_[A-Za-z0-9]{10,}` | 102 |

**경계 강제 (line 182-184)**: `(?<![A-Za-z0-9_-])(...)(?![A-Za-z0-9_-])` — 앞뒤 단어 경계 부정 lookahead로 부분 매칭 회피.

### 2.2 추가 Regex 패턴 (12종)

| # | 이름 | 용도 | 출처 라인 |
|---|------|------|------|
| H-A | `_ENV_ASSIGN_RE` | `OPENAI_API_KEY=value` 형태 ENV 대입 | 107-109 |
| H-B | `_JSON_FIELD_RE` | `"apiKey": "..."` JSON 필드 (12 키) | 113-116 |
| H-C | `_AUTH_HEADER_RE` | `Authorization: Bearer <token>` | 119-122 |
| H-D | `_TELEGRAM_RE` | `bot<digits>:<token>` Telegram bot | 126-128 |
| H-E | `_PRIVATE_KEY_RE` | `-----BEGIN ... PRIVATE KEY-----` 블록 | 131-133 |
| H-F | `_DB_CONNSTR_RE` | `postgres/mysql/mongodb/redis/amqp://user:pass@host` | 137-140 |
| H-G | `_JWT_RE` | `eyJ...` JWT (1/2/3-part) | 144-147 |
| H-H | `_DISCORD_MENTION_RE` | `<@<snowflake>>` (privacy) | 151 |
| H-I | `_SIGNAL_PHONE_RE` | E.164 `+<country><number>` (privacy) | 155 |
| H-J | `_URL_WITH_QUERY_RE` | URL 쿼리 스트링 — `_SENSITIVE_QUERY_PARAMS` 16종 redact | 160-166 |
| H-K | `_URL_USERINFO_RE` | `https://user:pass@host` (DB 외 스킴) | 171-173 |
| H-L | `_FORM_BODY_RE` | `k=v&k=v` 폼 바디 — `_SENSITIVE_BODY_KEYS` 14종 redact | 177-179 |

### 2.3 Sensitive Key Frozenset (2종)

#### `_SENSITIVE_QUERY_PARAMS` (16개, line 19-36)
```
access_token, refresh_token, id_token, token, api_key, apikey, client_secret,
password, auth, jwt, session, secret, key, code, signature, x-amz-signature
```

#### `_SENSITIVE_BODY_KEYS` (14개, line 41-56)
```
access_token, refresh_token, id_token, token, api_key, apikey, client_secret,
password, auth, jwt, secret, private_key, authorization, key
```

#### `_JSON_KEY_NAMES` (line 112)
```
api_?[Kk]ey, token, secret, password, access_token, refresh_token,
auth_token, bearer, secret_value, raw_secret, secret_input, key_material
```
(`re.IGNORECASE` 적용)

### 2.4 Hermes 측 총 카탈로그 요약

| 카테고리 | 수 | 적용 게이트 |
|---------|---|----------|
| Prefix patterns | **35** | 단어 경계 강제 |
| 추가 regex | **12** | 카테고리별 별도 정규식 |
| Sensitive frozenset | **2** (16+14 키) | URL/form 키 매칭 |

**기본값**: `HERMES_REDACT_SECRETS=false` (line 64) — opt-in. v0.12.0 breaking change로 default ON → OFF 전환됨 (Day 1 보고서 §2 기록).

---

## 3. P1_REDACTOR 패턴 카탈로그 추출

**출처**: `docs/architecture/llm-providers-design.md` §8.2 (line 521-536)
**적용 범위**: P1 facade의 LiteLLM `success_callback` / `failure_callback` (메트릭/메시지 — DB INSERT 미적용 + Day 1 §218 명시 "P1 facade 레벨 → 영향 없음")
**상태**: P1 v2 *설계 명세* 단계 — 구현 코드 미존재

### 3.1 `RedactionFilter.PATTERNS` (4종)

| # | Vendor / Type | Regex |
|---|------|------|
| P-1 | OpenAI API key | `sk-[a-zA-Z0-9]{20,}` |
| P-2 | Anthropic API key | `sk-ant-[a-zA-Z0-9]{20,}` |
| P-3 | Bearer token | `Bearer [a-zA-Z0-9._-]+` |
| P-4 | JSON field with secret keys | `"(api_key\|token\|auth\|secret\|password\|credential)"\s*:\s*"[^"]+"` |

### 3.2 `KEY_BLACKLIST` (6개)
```
api_key, token, secret, auth, credential, authorization
```

### 3.3 P1_REDACTOR 측 총 카탈로그 요약

| 카테고리 | 수 |
|---------|---|
| Patterns | **4** |
| KEY_BLACKLIST | **6** 키 |

P-1과 Hermes #1 모두 `sk-` prefix를 다루나 **문자 클래스 차이 존재** — Hermes는 `[A-Za-z0-9_-]` (`_`/`-` 허용), P1은 `[a-zA-Z0-9]` (`_`/`-` 미허용). Hermes가 **더 광범위**.

---

## 4. R-2 PoC trigger UDF 패턴 카탈로그 (현 baseline)

**출처**: `docs/phase0/day3-r2-sqlite-trigger-poc.md` line 110-122 + `docker/r2-poc/r2_poc.py`
**적용 범위**: SQLCipher BEFORE INSERT trigger (DB INSERT 직전, REGEXP UDF로 Python `re.search`)
**작동 방식**: 매칭 시 `RAISE(ABORT, 'secret-pattern-detected: ...')` — 마스킹 미시도, INSERT 자체 거부 (사용자 선호 명시)
**에러 메시지 고정 문자열**: `NEW.content` echo 안 함 → C6 만족 (에러 평문 미노출)

### 4.1 현 trigger UDF 패턴 (5종)

| # | Vendor / Type | Regex | Hermes 매핑 |
|---|------|------|------|
| T-1 | Anthropic | `sk-ant-[A-Za-z0-9_-]{10,}` | #1 (sk-) 부분집합 — 명시적 분리 |
| T-2 | OpenAI / OpenRouter / Anthropic | `sk-[A-Za-z0-9_-]{10,}` | #1 동일 |
| T-3 | GitHub PAT classic | `ghp_[A-Za-z0-9]{10,}` | #2 동일 |
| T-4 | AWS Access Key ID | `AKIA[A-Z0-9]{16}` | #15 동일 |
| T-5 | Slack tokens | `xox[baprs]-[A-Za-z0-9-]{10,}` | #8 동일 |

### 4.2 R-2 trigger UDF 측 총 카탈로그 요약

| 카테고리 | 수 |
|---------|---|
| Prefix patterns | **5** |
| 추가 regex | **0** |
| Sensitive frozenset | **0** |

R-2 PoC는 *원리 실증*을 목표로 한 PoC였고, 패턴 5종은 canary 5종에 대응하는 최소 검증 세트. **본 R-4의 출발점은 이 5종이 G1b 정식 충족 기준선이 아님을 확정하는 데 있다.**

---

## 5. 3-way 동등성 비교 매트릭스

### 5.1 Prefix patterns (35종 기준)

| # | 패턴 | Hermes | P1_REDACTOR | R-2 trigger | gap 분류 |
|---|------|------|------|------|------|
| 1 | `sk-` (OpenAI/Anthropic/etc) | ✅ | ✅ (P-1, P-2) | ✅ (T-1, T-2) | — |
| 2 | `ghp_` (GitHub PAT) | ✅ | ❌ | ✅ (T-3) | — |
| 3 | `github_pat_` | ✅ | ❌ | ❌ | **Tier-1** |
| 4 | `gho_` | ✅ | ❌ | ❌ | **Tier-1** |
| 5 | `ghu_` | ✅ | ❌ | ❌ | **Tier-1** |
| 6 | `ghs_` | ✅ | ❌ | ❌ | **Tier-1** |
| 7 | `ghr_` | ✅ | ❌ | ❌ | **Tier-1** |
| 8 | `xox[baprs]-` (Slack) | ✅ | ❌ | ✅ (T-5) | — |
| 9 | `AIza` (Google) | ✅ | ❌ | ❌ | **Tier-1** |
| 10 | `pplx-` (Perplexity) | ✅ | ❌ | ❌ | **Tier-1** |
| 11 | `fal_` | ✅ | ❌ | ❌ | **Tier-1** |
| 12 | `fc-` (Firecrawl) | ✅ | ❌ | ❌ | **Tier-1** |
| 13 | `bb_live_` (BrowserBase) | ✅ | ❌ | ❌ | **Tier-1** |
| 14 | `gAAAA` (Codex) | ✅ | ❌ | ❌ | **Tier-1** |
| 15 | `AKIA` (AWS) | ✅ | ❌ | ✅ (T-4) | — |
| 16 | `sk_live_` (Stripe) | ✅ | ❌ | ❌ | **Tier-1** |
| 17 | `sk_test_` (Stripe) | ✅ | ❌ | ❌ | **Tier-1** |
| 18 | `rk_live_` (Stripe) | ✅ | ❌ | ❌ | **Tier-1** |
| 19 | `SG.` (SendGrid) | ✅ | ❌ | ❌ | **Tier-1** |
| 20 | `hf_` (HuggingFace) | ✅ | ❌ | ❌ | **Tier-1** |
| 21 | `r8_` (Replicate) | ✅ | ❌ | ❌ | **Tier-1** |
| 22 | `npm_` | ✅ | ❌ | ❌ | **Tier-1** |
| 23 | `pypi-` | ✅ | ❌ | ❌ | **Tier-1** |
| 24 | `dop_v1_` (DigitalOcean PAT) | ✅ | ❌ | ❌ | **Tier-1** |
| 25 | `doo_v1_` (DigitalOcean OAuth) | ✅ | ❌ | ❌ | **Tier-1** |
| 26 | `am_` (AgentMail) | ✅ | ❌ | ❌ | **Tier-1** |
| 27 | `sk_` (ElevenLabs) | ✅ | ❌ | ❌ | **Tier-1** |
| 28 | `tvly-` (Tavily) | ✅ | ❌ | ❌ | **Tier-1** |
| 29 | `exa_` | ✅ | ❌ | ❌ | **Tier-1** |
| 30 | `gsk_` (Groq) | ✅ | ❌ | ❌ | **Tier-1** |
| 31 | `syt_` (Matrix) | ✅ | ❌ | ❌ | **Tier-1** |
| 32 | `retaindb_` | ✅ | ❌ | ❌ | **Tier-1** |
| 33 | `hsk-` (Hindsight) | ✅ | ❌ | ❌ | **Tier-1** |
| 34 | `mem0_` | ✅ | ❌ | ❌ | **Tier-1** |
| 35 | `brv_` (ByteRover) | ✅ | ❌ | ❌ | **Tier-1** |

**소계**: Hermes 35종 / P1_REDACTOR 1종 (sk- 계열만) / R-2 trigger 5종 → **trigger gap 31종 (Tier-1)**.

### 5.2 추가 regex 패턴 (12종)

| # | 패턴 | Hermes | P1_REDACTOR | R-2 trigger | gap 분류 |
|---|------|------|------|------|------|
| H-A | ENV assignment (`KEY=value`) | ✅ | ❌ | ❌ | **Tier-1** |
| H-B | JSON field (`"apiKey": "..."`) | ✅ (12 키) | ✅ (P-4, 6 키) | ❌ | **Tier-1** |
| H-C | Authorization header (Bearer) | ✅ | ✅ (P-3 부분 — Bearer 외 형식 미커버) | ❌ | **Tier-1** |
| H-D | Telegram bot token | ✅ | ❌ | ❌ | **Tier-2** (vendor specific) |
| H-E | Private key block (BEGIN/END) | ✅ | ❌ | ❌ | **Tier-1** |
| H-F | DB connstr password (postgres/mysql/...) | ✅ | ❌ | ❌ | **Tier-1** |
| H-G | JWT (`eyJ...`) | ✅ | ❌ | ❌ | **Tier-1** |
| H-H | Discord mention (privacy) | ✅ | ❌ | ❌ | **Tier-3** (privacy, not secret) |
| H-I | E.164 phone (privacy) | ✅ | ❌ | ❌ | **Tier-3** (privacy, not secret) |
| H-J | URL query secrets (16 키) | ✅ | ❌ | ❌ | **Tier-1** |
| H-K | URL userinfo (non-DB schemes) | ✅ | ❌ | ❌ | **Tier-1** |
| H-L | Form body (14 키) | ✅ | ❌ | ❌ | **Tier-1** |

**소계**: Hermes 12 / P1_REDACTOR 2 (부분) / R-2 trigger 0 → **trigger gap 12종 (Tier-1: 9 + Tier-2: 1 + Tier-3: 2)**.

### 5.3 비교 결과 합산

| 차원 | Hermes | P1_REDACTOR | R-2 trigger (현 baseline) |
|---|---|---|---|
| Prefix patterns | 35 | 1 (sk- 계열만) | 5 |
| 추가 regex | 12 | 2 (Bearer 부분 + JSON field) | 0 |
| Sensitive frozenset | 2 (16+14 키) | 1 (6 키) | 0 |
| **합계 카테고리** | **47 + 2 frozenset** | **3 + 1 frozenset** | **5** |

**핵심 관찰**:

1. **Hermes ⊇ P1_REDACTOR** — Hermes 카탈로그가 P1_REDACTOR를 거의 완전히 포괄. P1_REDACTOR sk- 패턴은 Hermes #1 (sk-) 의 더 좁은 변종 (`[a-zA-Z0-9]{20,}` vs `[A-Za-z0-9_-]{10,}`).
2. **R-2 trigger ⊊ Hermes** — 현 R-2 baseline 5종은 Hermes 35 prefix의 14% (5/35), 추가 regex 0% (0/12).
3. **ADR-011 §2.1 (a) 불충족** — R-2 trigger UDF가 Hermes 대비 동등 이상 보장 불가. 본 R-4 종료 시점에 G1b 정식 충족 진입 불가 — 보충 권고(§7) 후 별도 작업으로 trigger UDF 확장 + R-2 PoC 재실행 (ADR-011 §2.1 (b) 격리 환경 PoC 실증) 필요.

---

## 6. Gap 분석 (Tier 분류)

### 6.1 Tier 정의

| Tier | 정의 | ADR-011 §2.1 (a) 영향 |
|------|------|----------------|
| **Tier-1** | 비밀값 누출 직접 위험 (헌법 제8조 본질) | 보충 **필수** — 미보충 시 G1b 정식 충족 불가 |
| **Tier-2** | vendor-specific secret (도입 빈도 낮음, 본질 인접) | 보충 **권고** — 향후 패턴 등록 시점 단축 합의 |
| **Tier-3** | privacy 카테고리 (secret 아님, GDPR/CCPA 영역) | 보충 **별도 합의** — 헌법 제8조 본질 외 영역, 별도 정책 결정 필요 |

### 6.2 Tier-1 gap 카탈로그 (보충 필수)

#### 6.2.1 Prefix patterns (31종)
```
github_pat_, gho_, ghu_, ghs_, ghr_, AIza, pplx-, fal_, fc-, bb_live_,
gAAAA, sk_live_, sk_test_, rk_live_, SG\., hf_, r8_, npm_, pypi-, dop_v1_,
doo_v1_, am_, sk_ (ElevenLabs), tvly-, exa_, gsk_, syt_, retaindb_, hsk-,
mem0_, brv_
```
(31개 중 1개는 `sk_` ElevenLabs로 `sk_live_`/`sk_test_`/`rk_live_` 와 별도 — Hermes 카탈로그 line 94 코멘트 "sk_ underscore, not sk- dash" 명시)

#### 6.2.2 추가 regex (9종)
```
ENV assignment, JSON field (12 키), Authorization header (Bearer + 임의 형식),
Private key block, DB connstr password, JWT, URL query secrets (16 키 frozenset),
URL userinfo (non-DB), Form body (14 키 frozenset)
```

#### 6.2.3 Sensitive key frozenset (2종)
- URL query: 16 키 (Hermes `_SENSITIVE_QUERY_PARAMS`)
- Body/form: 14 키 (Hermes `_SENSITIVE_BODY_KEYS`)

### 6.3 Tier-2 gap (vendor specific, 보충 권고)

| 패턴 | 출처 | 사유 |
|------|------|------|
| Telegram bot token (`bot<digits>:<token>`) | Hermes H-D | Telegram bot 운영은 본 프로젝트 직접 통합 가능성 낮음. 그러나 R-7 SOP 작성 시점에 Tier-1 승격 검토 권고 |

### 6.4 Tier-3 gap (privacy, 별도 합의)

| 패턴 | 출처 | 사유 |
|------|------|------|
| Discord mention (`<@snowflake>`) | Hermes H-H | snowflake ID는 secret 아님. privacy 영역 — GDPR/CCPA 정책 결정 후 trigger 보충 별도 합의 |
| E.164 phone (`+<country><number>`) | Hermes H-I | 전화번호는 secret 아님. 동일 |

본 Tier-3 항목은 **본 R-4 보충 권고에 미포함** — 헌법 제8조 본질(=비밀값 평문 저장 차단)에 직접 해당 안 됨.

---

## 7. trigger UDF 보충 권고 카탈로그

### 7.1 권고 범위 (코드 미작성)

본 §7은 **카탈로그 권고만 제시**. 실제 SQL trigger / REGEXP UDF 코드 작성은 별도 작업으로 분리 — 보충 작업 자체도 ADR-011 §2.1 (a)~(d) 4조건 적용 대상이며, 본 권고를 입력으로 격리 환경 PoC (ADR-011 §2.1 (b)) 재실행 필요.

### 7.2 Tier-1 보충 패턴 42종 (Prefix 31 + 추가 regex 9 + alternation 2)

#### 7.2.1 Prefix patterns 31종 (Hermes #3~#7, #9~#14, #16~#35)

R-2 PoC trigger 구조 (`docs/phase0/day3-r2-sqlite-trigger-poc.md` line 110-122) 의 `OR NEW.content REGEXP '...'` 체인에 30 패턴 추가 권고. 정확한 정규식 문자열은 §2.1 표의 "Regex" 컬럼 그대로 사용.

#### 7.2.2 추가 regex 9종

| # | 패턴 | trigger 적용 형태 |
|---|------|----------|
| H-A | ENV assignment | `_ENV_ASSIGN_RE` (line 107-109) 패턴 그대로 — `_SECRET_ENV_NAMES` (line 106) 를 trigger REGEXP 인자에 직접 노출 |
| H-B | JSON field (12 키) | `_JSON_FIELD_RE` (line 113-114) — `re.IGNORECASE` 동등성 보장 위해 trigger UDF에서 case-insensitive 모드 활성화 권고 |
| H-C | Authorization header | `_AUTH_HEADER_RE` (line 119-121) — Bearer 외 형식까지 포함 (P1_REDACTOR P-3는 Bearer만 — Hermes 보강 채택) |
| H-E | Private key block | `_PRIVATE_KEY_RE` (line 131-132) — 멀티라인 매칭 (`[\s\S]*?`) 이므로 SQLite REGEXP UDF의 `re.search` 다중 라인 동작 검증 필요 (`re.DOTALL` 묵시적 적용 여부) |
| H-F | DB connstr password | `_DB_CONNSTR_RE` (line 137-139) — postgres/postgresql/mysql/mongodb/mongodb+srv/redis/amqp |
| H-G | JWT | `_JWT_RE` (line 144-147) — `eyJ` prefix + `(?:\.[A-Za-z0-9_=-]{4,}){0,2}` 1/2/3-part |
| H-J | URL query secrets | `_URL_WITH_QUERY_RE` (line 160-166) — REGEXP만으로 sub 불가하므로 trigger 단계는 *매칭 차단*만 가능 (마스킹은 별도 단계). `_SENSITIVE_QUERY_PARAMS` 16 키 alternation regex로 변환 권고 |
| H-K | URL userinfo (non-DB) | `_URL_USERINFO_RE` (line 171-172) — `https?\|wss?\|ftp` 스킴 한정 |
| H-L | Form body | `_FORM_BODY_RE` + `_SENSITIVE_BODY_KEYS` 14 키 alternation regex 변환 권고 |

#### 7.2.3 Sensitive frozenset alternation 2종

- **URL query alternation regex**: `(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+`
- **Body/form alternation regex**: `(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+`

### 7.3 trigger 마스킹 vs 차단 정책

R-2 PoC §3 (line 30-34) 사용자 명시:

> "trigger가 secret을 자동 마스킹하는 것보다, 우선은 secret 포함 INSERT를 확실히 차단하는 방향" — `RAISE(ABORT, ...)` 채택.

본 권고는 **차단 정책 유지**. 마스킹 채택 시 다음 위험:
- 마스킹된 값이 의미 있는 데이터로 오해되어 다운스트림 worker가 작동 (false-positive 데이터)
- 마스킹 우회 시도 (e.g. base64) 의 회귀 테스트 부담 증가

**예외**: H-J / H-L (URL query / form body) 의 경우, 전체 URL/body를 차단하면 정상 데이터 손실 위험 — 별도 합의 시점에 부분 마스킹 vs 전체 차단 결정 필요. 본 R-4는 **차단 권고**로 통일하되 ADR-011 §2.1 (a) 추가 검증을 후속 합의에 위임.

### 7.4 patterns 일관성 유지 메커니즘

Hermes 측 패턴은 upstream 변경으로 silent 깨짐 가능성 있음. 본 권고는 다음 메커니즘과 결합:

1. **R-5 (canary 재검증)**: 주기적 inject로 trigger 차단 동작 살아있음 검증
2. **R-6 (CI/nightly 회귀)**: Hermes 의존성 업그레이드 시 자동 R-2 재실행 — Hermes 측 `_PREFIX_PATTERNS` diff 검출 가능 시 본 §7 권고 카탈로그 갱신 PR 트리거
3. **ADR-011 §2.4 T3**: trigger UDF 변경 자체는 자동 정책 변경 금지 — 단축/풀 합의 후 PR

---

## 8. ADR-011 (a)~(d) 4조건 적용 결과

### 8.1 본 R-4 종료 시점 충족 상태

| 조건 | 의무 | 본 R-4 충족 여부 | 잔여 작업 |
|---|------|------|------|
| **(a) 동등 이상의 보안 결과** | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) | ✅ §5 3-way 매트릭스 / ❌ Hermes ⊋ R-2 trigger gap 42종 식별 — 동등 이상 미충족 | **§7 보충 권고 적용 → trigger UDF 확장 코드 작성 → 별도 작업** |
| **(b) 격리 환경 PoC로 실증** | Docker isolation + 자동 검증 항목 | ⏳ 본 R-4는 코드 작성 미포함 — R-2 PoC 5종 patterns에 한정된 PASS evidence만 존재 | **§7 보충 후 R-2 PoC 재실행 (Tier-1 42종 전수 자동 검증)** |
| **(c) ADR 권위로 명시** | 본 ADR 또는 후속 ADR | ✅ 본 문서가 ADR-011 §3 R-4 매핑 산출 — ADR-008 부록 B.6 R-4 ✅ 처리 가능 | — |
| **(d) 자동 회귀 검증 경로 확보** | CI/nightly 재실행 (R-6) | ⏳ R-6 작성 대기 중 | **R-6 작업에 본 §7.4 메커니즘 직접 인용 필수** |

### 8.2 G1b 정식 충족 진입 조건 (ADR-008 부록 B.6 / ADR-011 §2.2)

본 R-4 종료 시점 5단계 진행 상태:

```
R-3 ✅ ADR-011 발행 + ADR-008 Amendment (2026-05-06)
R-4 ✅ 패턴 동등성 비교 + gap 식별 + 보충 권고 (본 문서, 2026-05-06)
       ⚠️ 보충 코드 작성 → 별도 작업 (R-4.1로 분리 권고)
R-5 ⏳ canary 재검증 트리거 설계
R-6 ⏳ CI/nightly 회귀 검증
R-7 ⏳ Phase 1 합격 SOP
```

**R-4 → R-4.1 분기 권고**: ADR-011 §2.1 (a) 충족 의무는 본 R-4에서 *비교 + 권고 산출*까지. (b) 격리 환경 PoC 실증은 R-4.1 (trigger UDF 코드 보충 + R-2 PoC 재실행) 로 분리. 본 R-4 범위는 §8.3 참조.

### 8.3 R-4 범위 정리 (4항)

| # | 항목 | 본 문서 § |
|---|------|------|
| 1 | **R-4는 코드 수정 없는 문서화 작업이다** — Hermes / P1_REDACTOR / R-2 trigger 패턴 비교, 동등성 gap 식별, 보충 권고 문서화 | §1.1 / §2~§4 / §5 / §6 / §7 |
| 2 | **ADR-011 §2.1 (a) 현재 미충족 판단** — R-2 trigger baseline은 Hermes 대비 동등 이상 보장을 제공하지 못함 (Tier-1 gap 42종) | §5.3 / §8.1 |
| 3 | **ADR-011 §2.1 (b) 격리 환경 PoC 재실증은 R-4.1에서 수행** — trigger UDF 코드 보충 / Tier-1 42종 반영 / R-2 PoC 재실행 / PASS evidence 재생성 | §9.1 |
| 4 | **R-4.1 없이 P2 v3에서 기존 R-2 PASS evidence를 인용하면 ADR-011 §2.1 (a) 위반 위험** — P2 v3 작성 시점에 R-4.1 완료 확인 의무 | §10.3 |

본 4항은 사용자 명시 R-4 범위 (2026-05-06) 의 직접 흡수이며, 본 문서는 항목별 § 매핑으로 R-4 본질 추적성을 보장한다.

---

## 9. 후속 작업 매핑

### 9.1 R-4.1 (신규 권고 — trigger UDF 코드 보충 + R-2 재실행)

**산출 대상**:
- `docker/r2-poc/r2_poc.py` 갱신 (REGEXP UDF + trigger SQL 확장)
- `docker/r2-poc/canary_extended.py` 신규 (Tier-1 42종 canary 카탈로그)
- R-2 재실행 보고서 갱신 (`docs/phase0/day3-r2-sqlite-trigger-poc.md` Amendment 또는 신규 보고서)

**진입 조건**: 본 R-4 문서 사용자 검토 통과.
**ADR-011 적용**: §2.1 (a) ↔ §2.1 (b) 양방향.

### 9.2 R-5 (canary 재검증 트리거 설계 — 본 §7.4 1번)

**산출 대상**: `docs/architecture/canary-recheck-design.md`

본 R-4 §7.4의 권고 1번을 R-5의 입력으로 사용. canary 패턴은 본 §6.2.1 Tier-1 31종 prefix + §6.2.2 9종 regex + §6.2.3 2종 frozenset 의 부분집합으로 구성 (전수 inject는 R-2 PoC 재실행 영역 — R-4.1).

### 9.3 R-6 (CI/nightly 회귀 — 본 §7.4 2번)

**산출 대상**: `.github/workflows/r2-canary.yml`

본 R-4 §7.4 권고 2번을 R-6의 핵심 트리거 조건으로 직접 인용 — Hermes 의존성 업그레이드 시 `agent/redact.py` diff 검출 + 본 §2.1 / §2.2 / §2.3 표 자동 비교 + 본 §7 권고 카탈로그 자동 갱신 PR 트리거.

### 9.4 R-7 (Phase 1 합격 SOP — 본 §7.2 + §7.4 3번)

**산출 대상**: `docs/phase0/redaction-verification-sop.md`

본 R-4 §7.2 Tier-1 42종을 R-7 SOP의 PASS 기준 카탈로그로 직접 인용. SOP는 다음을 포함:
- canary inject 패턴 카탈로그 = §7.2 Tier-1 42종
- PASS 기준 = 42종 모두 trigger 차단 + DB 평문 부재 + 에러 평문 미노출 + ADR-011 §2.4 T3 위반 감지 0건
- FAIL 처리 = ADR-011 §2.1 (b) 재실증 요구 + 단축 합의 트리거

### 9.5 Tier-2 / Tier-3 후속 의사결정

| 항목 | 권고 |
|------|------|
| Tier-2 (Telegram bot token) | R-7 SOP 작성 시점에 Tier-1 승격 검토 — 단축 합의 |
| Tier-3 (Discord, E.164 phone) | privacy 정책 별도 합의 — 헌법 제8조 외 영역, GDPR/CCPA 등장 시점에 별도 ADR 권고 |

---

## 10. 결과 (Consequences)

### 10.1 긍정적

- ADR-011 §2.1 (a) 충족 의무가 본 R-4에서 명시적 카탈로그로 산출 — 미래 G1b 정식 충족 진입 조건이 *수치로 검증 가능*
- gap 42종 (Tier-1) 이 R-4.1 / R-5 / R-6 / R-7 작업의 입력으로 그대로 인용 가능 — 작업 분기 시 의사결정 비용 0
- Hermes upstream 변경 시 자동 회귀 검출 메커니즘(§7.4)이 ADR-011 §2.4 (자동 학습 vs 자동 정책 변경 분리) 와 정합

### 10.2 부정적

- 본 R-4 종료 시점 trigger UDF 5종 → R-4.1 (코드 보충) 진입 의무 — G1b 정식 충족 5단계 중 R-4 ✅ 표시는 보충 권고 단계까지이며, 실제 동등 이상 보장은 R-4.1 종료 후
- Hermes 측 `_PREFIX_PATTERNS` 수가 vendor 추가에 따라 증가 — 본 §7.2 카탈로그도 R-6 자동 회귀로 정기 갱신 필요 (의도된 비용)
- Tier-3 (privacy) 항목은 본 R-4 범위 외 — 별도 합의 미진행 시 trigger 미보호 (헌법 제8조 본질 외이므로 G1b 정식 충족 진입에 무관, 그러나 미래 정책 결정 의무 잔여)

### 10.3 주의사항

- 본 문서는 **trigger UDF 동등성을 선언하지 않는다** — 보충 권고 카탈로그이며, 실제 동등 이상 보장 검증은 R-4.1 PoC 재실행 후 ADR-011 §2.1 (b) 충족 시점에 확정
- **R-4.1 없이 P2 v3에서 기존 R-2 PASS evidence를 인용하면 ADR-011 §2.1 (a) 위반 위험** — §7.2 Tier-1 42종 카탈로그를 미보충 상태의 R-2 PoC PASS evidence (현 baseline 5 patterns) 를 인용하는 행위가 해당. P2 v3 작성 시점에 R-4.1 완료 확인은 의무이며, 미완료 인용은 단축/풀 합의로만 예외 처리 가능. §8.3 4항 참조.
- §7.3 차단 정책 (마스킹 미시도) 은 R-2 PoC 결정과 일관 — 변경 시 ADR-011 §2.4 T3 적용

---

## 11. 관련 문서

### 11.1 상위 권위
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a) 동등 이상 보장 검증 의무, §3 R-4 매핑)
- `docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B (B.6 R-4 ⏳ → ✅ 처리 대상)

### 11.2 출처 자료
- `/tmp/hermes-phase0/hermes-agent/agent/redact.py` (Hermes v0.12.0 main HEAD, 401 LOC)
- `docs/architecture/llm-providers-design.md` §8.2 (P1_REDACTOR 명세)
- `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PoC trigger UDF baseline 5종)
- `docker/r2-poc/r2_poc.py` (R-2 PoC 구현)

### 11.3 후속 작업 입력
- R-4.1 (권고 — 신규): trigger UDF 코드 보충 + R-2 PoC 재실행
- R-5: `docs/architecture/canary-recheck-design.md` (작성 예정)
- R-6: `.github/workflows/r2-canary.yml` (작성 예정)
- R-7: `docs/phase0/redaction-verification-sop.md` (작성 예정)

### 11.4 evidence 인용
- Day 1: `docs/phase0/day1-environment-and-fact-check.md` (Hermes 클론 위치 + v0.12.0 사실 확인)
- Day 2: `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL — Hermes redaction DB INSERT 미적용 확정, 본 §1.3 / §2 docstring 인용)
- Day 3: `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PASS — trigger UDF 5종 baseline)

---

**본 문서 발행 시점**: 2026-05-06
**다음 진입점**: **R-4.1** (사용자 결정, 2026-05-06) — Tier-1 42종 trigger UDF 확장 + R-2 PoC 격리 환경 재실행 + ADR-011 §2.1 (b) 직접 충족 evidence 생성. Tier-2 (Telegram bot) / Tier-3 (Discord, E.164) 는 R-4.1 범위 외 — 별도 합의 또는 R-7 SOP 작성 시 처리. R-5 (canary 재검증 트리거 설계) 는 R-4.1 완료 후 진행.
