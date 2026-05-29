# 3+1 합의 (Reviewer 통합) — SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief

> **cycle**: 65번째 entry — SC-1 facade RedactionFilter 실 구현 brief (세션 #3, TR-1 풀 3+1 발화)
> **대상**: `docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md` (v1)
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) — TR-1
> **4 source**: codex (OpenAI) + Agent A (구현) + Agent B (안전) + Agent C (대안) — cross-vendor 충족 (5조-2)
> **작성**: 2026-05-28

---

## §0 통합 판정

⭐ **APPROVE WITH CONDITIONS** (4 source 전원 APPROVE WITH CONDITIONS) — **BLOCKING 4 + 권고 6 → brief v1.1 흡수 후 TDD 구현**.

| source | 판정 | BLOCKING | 핵심 |
|--------|------|----------|------|
| codex (OpenAI gpt-5.5) | APPROVE WITH CONDITIONS | 2 | catalog (ii) 전환 + request body 범위 명시. 권위 인용 6/7 일치 (§8.2 부분 확장) |
| Agent A (구현) | APPROVE WITH CONDITIONS | 2 | catalog (i) 동작 실측 (namespace) but framing + [REDACTED] 구조 손상. pytest 152 green, 성능 2.1ms |
| Agent B (안전) | APPROVE WITH CONDITIONS | 3 | catalog (i) sys.path 종속 + [REDACTED] 권위 오귀속 + 송신 redaction 권위 §8.2 아님 |
| Agent C (대안) | APPROVE WITH CONDITIONS | 2 | catalog (i) 취약 → (ii)/(v) 우월 + group-aware 치환 |

→ brief *방향* (RedactionFilter 집중 / 송신 redaction / RT-1 회피 / 명칭 정직성) = 4 source 견고 판정. BLOCKING = 구현 *방식* 정정 (catalog + 치환 전략 + 권위 + 범위).

---

## §1 BLOCKING (Reviewer 독립 verify 후 흡수 의무)

### B-1 ⭐ (4 source 수렴) — catalog 재사용 기본안 (i) → (ii) 공유 모듈 추출

| source | 입장 |
|--------|------|
| codex | (ii) 추천 — src→tools 역방향 의존, .importlinter root=src 미제어 ("미차단 ≠ 승인") |
| Agent A | (i) 동작 실측 (namespace package) but 단점 framing 정정, `from tools.secret_scanner import` 고정 |
| Agent B | (i) tools/ `__init__.py`/pyproject 부재 → sys.path hack 강제 (brief 과소평가) |
| Agent C | (i) CWD/packaging 종속 취약 → (ii) 또는 (v) 데이터 외부화 우월 |

**Reviewer verify** (직접 실행):
- `from tools.secret_scanner import COMPILED_PATTERNS` → **IMPORT OK, patterns: 45** (namespace package PEP 420, repo root sys.path) — Agent A 실측 정확.
- `tools/__init__.py` 부재 + `pyproject.toml`/`setup.py`/`setup.cfg` 부재 = **run-from-source** (namespace package 의존).
- ⚠️ **(i) 동작하나 src(런타임)→tools(개발도구 PoC) 의존 방향 nonidiomatic** (Agent A도 인정, codex/B/C 지적). .importlinter root=src 밖 = 미제어.

→ **흡수 = (ii) 공유 모듈 추출 채택** (3:1 majority + codex BLOCKING): Tier-1 catalog literal을 **src 하위 공유 모듈** (예: `src/adapters/llm/redaction_patterns.py`)로 추출 → `RedactionFilter`(src) + `secret_scanner`(tools) 둘 다 import (tools→src = 도구가 런타임 참조 = 정방향, Agent C 대안). **secret_scanner 패턴 *내용* 변경 0건** (id/src/cat/vendor/regex 동일) + **equivalence test 필수** (`len(ALL_PATTERNS)==45` + snapshot + scan pass/fail fixture 유지). secret_scanner 구조 변경 (literal→import)은 패턴 내용 0이므로 detection 동작 불변 (R-4.1 충실, R-7(b) = 패턴 내용 변경 아님).

### B-2 ⭐ (3 Agent 수렴) — `[REDACTED]` whole-match 치환 → group-aware 치환

- Agent A: whole-match 치환이 prefix/regex/alternation에서 **key명·JSON 구조까지 소거** → "정상 내용 손상 아님" 주장 정정 + dict 구조 무결성 test.
- Agent B: secret_scanner는 **검출 전용 (치환 함수 0)** — catalog를 redaction에 직접 re.sub 불가.
- Agent C: catalog regex group 구조(검출용)·§8.2 key-보존 의도 충돌. 실증 JSON 구조 파괴·word-joining artifact.

→ **흡수 = group-aware 치환** (값만 마스킹, key명/구조 보존): secret_scanner 패턴은 *검출*용 (prefix 포함 매칭). redaction은 **매칭된 secret *값* 부분만** `[REDACTED]` (key명·JSON 구조 보존). detection 패턴 ≠ redaction 치환 — 별도 치환 로직 (group 분리 또는 값 추출). dict 구조 무결성 test (T-추가).

### B-3 (codex + Agent B) — 송신 redaction 권위 = §8.2 아님 (egress 중심)

- §8.2 RedactionFilter docstring = "응답·예외·메트릭" (egress). 송신(request body) redaction 실권위 = **governance §4.1 (line 422 "LLM API request body") + 64 trajectory brief**.
→ **흡수**: §0.3 + §3 권위 정정 — 송신 redaction = governance §4.1 + 64 trajectory PRIMARY, §8.2 = egress scrub 보조 (부분 확장 명시).

### B-4 (codex) — request body redaction 범위 명시

- 설계 `LLMRequest`는 messages + system + tools + tool_choice + response_format + stop_sequences + metadata_in. 현 placeholder = messages + metadata (system 없음).
→ **흡수**: §3 범위 명시 — 본 cycle 최소 = **messages + metadata** redaction (현 placeholder 기준), 설계 §4.1 full fields (system/tools/...)는 Router 위임 sub-cycle과 함께 deferred 명시.

---

## §2 권고 (흡수 — 채택)

| # | 권고 | source | 흡수 |
|---|------|--------|------|
| R-1 | 원본 request/message **불변성 test** (in-place mutate 금지, 재시도/로그 부작용) | codex 1 | T-7 추가 |
| R-2 | T-4 false positive **edge case fixture** (`sort(key=)`, `keyboard`, `monkeypatch`, URL query) | codex 2 + Agent A | §5 T-4 |
| R-3 | `scrub()` **KEY_BLACKLIST** 구현 (§8.2 정합, key 기반 redaction) | codex 3 | §2.2 |
| R-4 | T-6 **spy/fake redactor 주입** (NotImplementedError만으론 redaction 선행 미입증) | codex 4 | §5 T-6 |
| R-5 | `redact_messages()` content **list/structured 재귀** (scrub 기반, str 외) | codex 5 | §3 |
| R-6 | redaction **전략 = group-aware 값 마스킹** (B-2 연계, `sk-***last4` 부분 마스킹 평가) | Agent C | §2.2 |

---

## §3 Reviewer 독립 verify (5 source 격상)

| 항목 | verify 결과 |
|------|------|
| catalog (i) import 동작 | ✅ `from tools.secret_scanner import` OK (namespace package, 45 patterns) — Agent A 정확 |
| pyproject/setup 부재 | ✅ run-from-source (namespace package 의존) |
| src→tools 의존 방향 | ⚠️ nonidiomatic CONFIRMED (.importlinter root=src 미제어) → (ii) 채택 |
| secret_scanner 검출 전용 | ✅ 치환 함수 0 (scan_text = Violation 반환) — B-2 정확 |
| §8.2 = egress 중심 | ✅ docstring "응답·예외·메트릭" (line 521-522) — B-3 정확 |
| 명칭 정직성 | ✅ "facade redaction layer real" / "full facade real 아님" 반복 명시 (over-claim 0, 4 source 공통) |

---

## §4 합의 결론

✅ **SC-1 facade RedactionFilter 실 구현 APPROVE WITH CONDITIONS** (4 source 전원) — **brief v1.1 흡수 후 TDD 구현**:

1. **방향 견고** (4 source): RedactionFilter 집중 + 송신 redaction + RT-1 회피 + 명칭 정직성 + Provider Liquidity 보존.
2. **BLOCKING 4 흡수 (구현 설계 정정)**:
   - (B-1) catalog = **(ii) 공유 모듈 추출** (src 하위 + tools import + 패턴 내용 0 변경 + equivalence test)
   - (B-2) redaction = **group-aware 치환** (값 마스킹, 구조 보존)
   - (B-3) 송신 권위 = governance §4.1 + 64 trajectory (§8.2 egress 보조)
   - (B-4) 범위 = messages + metadata (full fields deferred 명시)
3. **권고 6 흡수** (test 강화 + scrub KEY_BLACKLIST).
4. **TDD 구현 진행** (RED→GREEN→REFACTOR) + verify (pytest + import-linter + secret_scanner equivalence + jarvis 회귀).
5. **명칭 over-claim 0** (4 source) — facade *redaction layer* real, full facade real / full GP-2 PASS 아님.

→ **brief v1.1 1pass 흡수 → TDD 구현 → verify → commit + push**.

---

## §5 메타 편향 자기진단 (Reviewer)

| # | 위험 | 처리 |
|---|------|----|
| M-1 | Reviewer = brief 작성자 (Claude) cascade | cross-vendor codex 독립 + 3 Agent BLOCKING 9 (catalog/치환/권위 작성자 미포착 포착) |
| M-2 | catalog (i)/(ii) divergence (Agent A (i) vs codex/B/C (ii)) | Reviewer 직접 실행 verify — (i) 동작하나 의존 방향 (ii) 채택 (majority + 정합) |
| M-3 | B-2 [REDACTED] 치환 = 사소 무시 risk | 3 Agent 실증 (JSON 구조 파괴) — redaction 정확성 = GP-2 prevention 핵심 |
| M-4 | (ii) secret_scanner 변경 = R-4.1 위반 risk | 패턴 *내용* 0 변경 + equivalence test (len==45 + snapshot + fixture) — detection 동작 불변 |
| M-5 | 4 source 전원 APPROVE = rubber-stamp | BLOCKING 4 실질 흡수 (구현 설계 전환: catalog 방식 + 치환 전략) |

---

**본 합의 보고서 끝.**

**다음 단계**: brief v1.1 흡수 (BLOCKING 4 + 권고 6) → TDD 구현 (RED→GREEN→REFACTOR, catalog (ii) 공유 모듈 + group-aware 치환) → verify → commit + push → **R-2 facade RedactionFilter prevention layer in-repo operative**. 후속: SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) / SC-Provider Liquidity (Router 위임) = 사용자 명시 별도.
