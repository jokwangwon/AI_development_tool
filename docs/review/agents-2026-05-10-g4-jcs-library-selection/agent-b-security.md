# Agent B — 보안/거버넌스 분석 (Q1: G4 JSONL hash chain + RFC 8785 JCS PoC — Canonical JSON 라이브러리 선정)

**작성일**: 2026-05-10
**Agent 역할**: 보안/거버넌스 검증가 (3+1 풀 합의 — Phase 2 독립 분석)
**의제**: G4 PoC 의 Canonical JSON Primary 라이브러리 선정 — 사용자 명시 결정 갱신 결과 `rfc8785` (Trail of Bits) + `jcs` (titusz) **병렬 cross-check** 채택안에 대한 보안/거버넌스 적격성 평가
**검토자 컨텍스트**: 본 분석은 메인 컨텍스트와 동일 클로드 인스턴스가 작성 — 자기참조 + 메타 편향 위험 인지하며 §0.3 / §6 / §8 에서 통제
**격상 범위 외**: G4 전체 Implementation/Runtime PASS 선언 / Hermes PMO 격상 / migration script 본 구현 / ADR 본문 자동 갱신 / 신규 정책 발명 — 본 의제 영구 답습

**검토 영역 12건 (사용자 명시 답습)**:

1. `rfc8785` (Trail of Bits) supply chain 위험 (PyPI 단일 소스 / signature / 유지보수 활성도)
2. `jcs` (titusz) supply chain 위험 (개인 maintainer / last release / signature)
3. 양 라이브러리 Apache-2.0 라이선스의 Provider Liquidity 보존 정합 (헌법 5조 비협상)
4. 양 라이브러리 모두 의존 0 → Hermes 의존 0 (ADR-008 차단조건 #2) 충족 검증
5. 병렬 cross-check 강제의 보안 이점 vs 단순성 비용
6. RFC 8785 명세 준수 검증 책임 (NaN/Infinity reject / IEEE 754 number / UTF-16 codepoint sort)
7. fallback `jq -S -c` 의 supply chain 위험 (POSIX 표준 / debian/ubuntu/brew 배포 / version drift)
8. `event: canonical_json_fallback` ledger entry 의 audit trail 적합성 (T1 audit 답습)
9. prev_hash 검증 실패 → BLOCK + manual review 정책의 ADR-011 §2.4 (T3 자동 정책 변경 금지) 정합성
10. Hermes 변조 차단 매트릭스 (ADR-012 §2.12 4항목) 와의 정합성 — 본 PoC 가 어느 항목을 cover 하는가
11. `event` 17 enum 중 본 PoC MVP 4종 한정의 보안 충분성 (`evidence_forgery_detected` / `policy_change_attempted` 등 미적용 영역의 위험)
12. `external_review/` 또는 cross-vendor LLM 검증 의무 발화 여부 (PR-2 답습 — RFC 8785 동등성 검증은 crypto specialist 권고 영역, ADR-012 §15 답습)

---

## 0. 본 입력의 입장 + 메타 한계

### 0.1 핵심 입장 (한 문장)

`rfc8785` + `jcs` **병렬 cross-check** 채택안은 — **(i) Provider Liquidity 보존 강도 HIGH**, **(ii) Hermes 의존 0 충족** (ADR-008 차단조건 #2), **(iii) Hermes 변조 차단 매트릭스 §2.12 #2 (filesystem 변조) 의 *형식 기반 검출 layer* 강화**, **(iv) 단일 라이브러리 bug-class 의존성 회피** — 이상 4 차원에서 **APPROVE WITH CONDITIONS** 적격이지만, **(α) `jcs` (titusz) 개인 maintainer supply chain HIGH 잔여 위험**, **(β) `event` 17 enum 중 MVP 4종 한정으로 인한 `evidence_forgery_detected` / `policy_change_attempted` 미발화 영역 HIGH Gap**, **(γ) RFC 8785 동등성 *crypto specialist* 검증 의무 (ADR-012 §11.3 답습) 의 본 PoC 단계 발화 부재** — 3 영역에서 조건부 흡수 의무.

### 0.2 본 분석의 *판정하지 않는* 것

- ❌ G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 권유
- ❌ ADR-012 본문 자동 갱신 (cross-reference 답습만 가능)
- ❌ ADR-008 차단조건 #2 본문 변경 (본 PoC 는 차단조건 #2 *충족 검증* 까지)
- ❌ 신규 `event` enum 추가 (ADR-012 §2.2 17 enum 답습)
- ❌ 신규 정책 발명 (ADR-012 / G4 §4 / ADR-011 본문 외)
- ❌ Q2 (corpus 24개) / Q3 (PoC 6 영역) 본문 평가 — 본 분석은 Q1 한정
- ❌ 다른 Agent (A, C) 출력 참조
- ❌ Reviewer 합의 결과 예측

### 0.3 본 분석의 메타 한계 (강조)

본 입력은 메인 컨텍스트와 **동일 Claude 인스턴스**. 자기참조 + 메타 편향 위험 인지. 외부 LLM 1+ 검증은 본 의제 풀 3+1 합의 시점 *별도 발화* (PR-2 합의 §6.3 답습) — 본 분석은 *Agent B 관점에서의 보안/거버넌스 판정* 한정.

본 분석에서 자체 식별한 메타 한계 5건:

1. RFC 8785 표준 자체의 *암호학적 보안성* 평가는 **IETF 권위 영역** + **crypto specialist 영역** — 본 분석은 *IETF 표준 채택 적격성 + 운영 함의* 한정
2. `rfc8785` 0.1.4 의 *코드 보안 audit* 평가는 **Trail of Bits 자체 권위 + 외부 audit firm** 영역 — 본 분석은 *PyPI metadata + 의존 트리 + Sanity 결과* 한정 (RA-9 §B 답습)
3. `jcs` 0.2.1 (titusz) 의 *코드 보안 audit* 는 **개인 maintainer 한정** + **외부 audit 부재 가능성 HIGH** — 본 분석은 *RA-9 §B sanity 11/11 PASS 결과* 까지, 정식 외부 audit 부재 시 *cross-check 보강 layer* 로 위치
4. RA-9 §B sanity check 11 vector 는 **본 분석 외 산출** — 본 분석은 RA-9 evidence 흡수까지, *24개 corpus 정식 회귀* 는 PoC 구현 후 격리 검증 영역
5. 본 분석이 *fallback `jq -S -c`* 의 RFC 8785 동등성을 평가하나, **fallback 동등성 정식 corpus 검증** 은 PoC 구현 시점 영역 — 본 분석은 *fallback 채택 적격성 + audit trail 적합성* 까지

---

## 1. 검토 evidence 목록 + 권위 위계 trace

### 1.1 직접 읽은 evidence (5건)

| # | 경로 | 답습 영역 |
|---|------|---------|
| 1 | `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` (전문, 본문 + §B RA-9 + 부록 A 의존 매트릭스 + 부록 C 답습 매핑) | 본 의제 PoC 사양 + RA-9 evidence 흡수 |
| 2 | `docs/decisions/ADR-012-evidence-ledger-protection.md` (전문 — 12 보호 원칙 + 4 매트릭스 + 5 추가 의무 + §2.12 Hermes 변조 차단 4 항목) | 권위 모법 (Evidence Ledger 보호) |
| 3 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5조건 + §2.3 Hermes ≠ root of trust + §2.4 T1/T2/T3 | 모법 ADR (수단/목적 분리) |
| 4 | `docs/decisions/ADR-008-hermes-adoption-decision.md` 차단조건 #2 (JSONL export 표준 — Hermes lock-in 회피) | 헌법-인접 권위 (Provider Liquidity 차단조건) |
| 5 | `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` | 헌법 5조 비협상 (Provider Liquidity 영구 기억) |

### 1.2 권위 위계 trace (본 의제 적용)

```
헌법 8조 (보안) + 헌법 5조 (Provider Liquidity, 비협상)
  ↓
ADR-011 §2.1 (수단/목적 분리, (a)~(e) 5조건)
ADR-011 §2.3 (Hermes ≠ root of trust)
ADR-011 §2.4 (T1/T2/T3 자동 정책 변경 금지)
  ↓
ADR-008 차단조건 #2 (JSONL export 표준 — Hermes 의존 0)
  ↓
ADR-012 (Evidence Ledger Protection — 12 원칙 + §2.5 RFC 8785 JCS Primary + jq fallback + §2.12 Hermes 변조 차단 매트릭스 4 항목)
  ↓
G4 §4.2 (11 필드 schema, `event` 11번째)
G4 §4.4 (hash chain 사양)
G4 §4.6 (round-trip 검증 절차)
  ↓
implementation-runtime-roadmap.md §4.1 (G4 7 영역, Order 3 tie 3건)
  ↓
g4-jsonl-hash-chain-jcs-poc-spec.md (Group C 통합 PoC — 본 의제 사양)
  ↓
Q1 = Canonical JSON 라이브러리 선정 (본 의제 한정)
```

본 의제는 **권위 위계의 가장 하위 PoC 선정 차원** — 상위 권위 모두 답습. 신규 권위 발명 0건 의무.

### 1.3 답습 시제 (Group A 2차 PR-2 답습)

본 분석은 PR-2 Agent B (`docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-b-security.md`) 597 줄 패턴 답습 — *영역별 분석* + *risk assessment* + *Provider Liquidity 보존 매트릭스* + *Gap-N (HIGH)* + *Verdict + 조건 N건*.

---

## 2. 영역별 분석 (12 영역)

### 2.1 영역 1 — `rfc8785` (Trail of Bits) supply chain 위험 평가

**사실 인용** (RA-9 §B.1 답습):
- PyPI 단일 소스 (`pip install rfc8785==0.1.4`)
- License: Apache-2.0 (LICENSE 파일 존재)
- Author: Trail of Bits (`opensource@trailofbits.com`)
- Requires: 없음 (의존 0)
- API surface: `dump`, `dumps`, `CanonicalizationError`, `FloatDomainError`, `IntegerDomainError`
- NaN/Infinity 거부: ✅ `FloatDomainError: nan is not representable in JCS`

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| Maintainer 신뢰도 | **HIGH** | Trail of Bits = 업계 표준 보안 audit firm. 자체 OSS 발행 생태 확립. organizational backing 존재 (개인 maintainer 위험 없음) |
| Supply chain 단일 소스 위험 | **MEDIUM** | PyPI 단일 source — typosquatting / namespace hijack 위험 존재. 단 **본 PoC 가 `rfc8785` *단독* 채택 아님 — `jcs` 와 *병렬 cross-check* 채택** 으로 단일 source 위험 *부분 완화* |
| Signature / package signing | **UNKNOWN** | RA-9 §B 미검증 영역 — PyPI 자체 sigstore / GPG 서명 부재 가능성 (PyPI 표준 한계). conditional C-B1 권고 |
| 유지보수 활성도 | **MEDIUM** | 0.1.4 = 초기 버전 (semver 0.x → API 안정성 미보증). 단 NaN/Infinity reject + RFC 명시 구현 = 핵심 기능 충족. conditional C-B2 권고 |
| 의존 트리 0 | **HIGH** | Requires: 없음 → Hermes 의존 0 (ADR-008 차단조건 #2) **자동 충족** |

**ADR cross-reference**:
- ADR-008 차단조건 #2 (JSONL export 표준 — Hermes lock-in 회피): **충족** (의존 0)
- ADR-012 §2.5 (JCS Primary): **충족** (RFC 8785 명시 구현)
- 헌법 5조 (Provider Liquidity): **HIGH** (Apache-2.0 + provider-neutral PyPI)

**판정**: APPROVE WITH CONDITIONS (C-B1 signature 검증 권고 + C-B2 0.x → 0.2 격상 시 RA-9 재실행 의무)

---

### 2.2 영역 2 — `jcs` (titusz, GitHub `titusz/jcs`) supply chain 위험 평가

**사실 인용** (RA-9 §B.1 답습):
- PyPI 단일 소스 (`pip install jcs==0.2.1`)
- License: Apache-2.0 (메타데이터 명시)
- Author: titusz (`tp@py7.de`, GitHub `titusz/jcs`)
- Requires: 없음 (의존 0)
- API surface: `canonicalize`, `ntoj`
- NaN/Infinity 거부: ✅ `ValueError: Invalid JSON number: nan`

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| Maintainer 신뢰도 | **MEDIUM-LOW** | **개인 maintainer** (`tp@py7.de`) — organizational backing 부재. 1인 maintainer abandonment / supply-chain compromise 위험 (PyPI account takeover 사례 답습) |
| Supply chain 단일 소스 위험 | **HIGH** | PyPI 단일 source + 개인 maintainer + namespace `jcs` (짧은 이름 — typosquat 표적 가능성). 본 PoC 가 *cross-check* 로 사용하는 것은 **단일 라이브러리 bug-class 회피 layer** 한정 — `jcs` 가 *primary 단독* 이라면 BLOCK 권고이나, *병렬 사용* 이므로 위험 완화 |
| Signature / package signing | **UNKNOWN** | RA-9 §B 미검증 영역 — 동일 PyPI sigstore 한계 적용 |
| 유지보수 활성도 | **UNKNOWN** | RA-9 §B 미검증 — last release date / commit frequency / open issues 미확인. conditional C-B3 권고 |
| 의존 트리 0 | **HIGH** | Requires: 없음 → Hermes 의존 0 (ADR-008 차단조건 #2) 충족 |
| 외부 audit 부재 위험 | **HIGH** | 개인 maintainer + 비-organizational backing → 코드 보안 audit 부재 가능성 HIGH. 단 본 PoC 는 *cross-check 보강 layer* 로 위치 — `rfc8785` (Trail of Bits) 가 primary 신뢰 source 역할, `jcs` 는 *동등성 비교 reference* 역할 |

**ADR cross-reference**:
- ADR-008 차단조건 #2: **충족** (의존 0)
- ADR-012 §2.5: **충족** (RFC 8785 구현 11/11 sanity PASS)
- 헌법 5조 Provider Liquidity: **HIGH** (Apache-2.0 + provider-neutral PyPI)
- ADR-011 §2.3 (Hermes ≠ root of trust): **간접 답습** — `jcs` 도 *root of trust 아님*, cross-check 보강 layer 로 위치

**판정**: APPROVE WITH CONDITIONS (C-B3 last release / commit frequency 검증 의무 + C-B4 `jcs` *primary 단독 격상 금지* 영구 명시 + C-B5 `jcs` 가 maintainer abandonment 시 본 PoC fallback 정책 명시)

---

### 2.3 영역 3 — Apache-2.0 라이선스의 Provider Liquidity 보존 정합 (헌법 5조 비협상)

**사실 인용**:
- `rfc8785` 0.1.4 = Apache-2.0 (LICENSE 파일 존재)
- `jcs` 0.2.1 = Apache-2.0 (메타데이터 명시)
- Provider Liquidity 비협상 (`feedback_provider_liquidity.md`): "어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 코드 변경 없이 가능해야 한다"

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| 라이선스 호환성 | **HIGH** | Apache-2.0 = permissive license, MIT/BSD/GPL 호환 (GPL with Apache exception). 본 PoC 도구가 OSS 또는 closed-source 양쪽 사용 가능 — Provider Liquidity *교체 자유* 보존 |
| Provider 락인 부재 | **HIGH** | 두 라이브러리 모두 *RFC 8785 표준 구현* — RFC 자체가 vendor-neutral IETF 표준. provider-specific (Anthropic / OpenAI / Google) 식별자 0건 |
| 라이브러리 교체 비용 | **LOW** | 두 라이브러리 모두 동일 RFC 명세 구현 → 호환 라이브러리 (npm `canonicalize`, Go `cyberphone/json-canonicalization`, `gowebpki/jcs` 등 — ADR-012 §2.5 답습) 로 교체 시 *byte-level 동등 출력 보장* (sanity 11/11 PASS 답습) |
| 복수 provider always-on (헌법 5조) | **HIGH** | `rfc8785` + `jcs` 병렬 채택 자체가 *복수 provider always-on* 패턴 — 한 라이브러리 abandonment 시 다른 라이브러리 단독 fallback 가능 + cross-check 비교 reference 손실만 발생 |

**ADR cross-reference**:
- 헌법 5조 (Provider Liquidity, 비협상): **충족 HIGH**
- ADR-008 차단조건 #5 (최소 2 provider always-on): **간접 답습 — 본 PoC 차원에서 라이브러리 2개 always-on 패턴**
- ADR-012 §2.5 (JCS Primary): **충족** (RFC 8785 표준 구현)

**판정**: APPROVE — Provider Liquidity 보존 강도 **HIGH**, 비협상 제약 위반 0건

---

### 2.4 영역 4 — 양 라이브러리 의존 0 → Hermes 의존 0 (ADR-008 차단조건 #2) 충족 검증

**사실 인용** (RA-9 §B.4 답습):
- `rfc8785` Requires = 없음
- `jcs` Requires = 없음
- ADR-008 차단조건 #2: "JSONL export 표준 + 메모리/스킬 마이그레이션 경로 정의 (Hermes lock-in 회피)"
- ADR-012 원칙 5: "Evidence Ledger 는 *Hermes 의존 0* — 모든 entry 가 표준 도구 (`jq` + `sha256sum` + 표준 라이브러리) 만으로 검증 가능"

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| 직접 의존 0 | **HIGH** | 두 라이브러리 `Requires:` 필드 모두 비어있음 → 전이 의존 0 → *Hermes 의존 자동 0* |
| 간접 의존 (Python stdlib only) | **HIGH** | 본 PoC 부록 A 답습 — `hashlib.sha256` / `json` / `subprocess` / `uuid` / `datetime` = Python stdlib only. PyPI 추가 의존 = `rfc8785` + `jcs` 한정. **Hermes (`hermes_agent` import) 0건** |
| ADR-008 차단조건 #2 충족 검증 책임 | **본 PoC 가 검증 layer** | 본 PoC = `import hermes_agent` 0건 + depcruise 검증 (G2 GP-5 영역 답습). 본 PoC 자체로 차단조건 #2 *충족 검증 evidence* 산출 |
| 표준 도구 only 검증 가능성 (ADR-012 원칙 5) | **HIGH** | `jq` + `sha256sum` + Python stdlib 만으로 ledger entry 검증 가능 — `rfc8785` / `jcs` 는 *PoC 도구* 한정 (검증 자체는 표준 도구 only) |
| escalation TR-C-5 (Hermes 의존 발견) | **미발화** | RA-9 §B.5 답습 — 두 라이브러리 모두 의존 0 |

**ADR cross-reference**:
- ADR-008 차단조건 #2: **자동 충족** + 본 PoC 가 *충족 검증 evidence* 산출
- ADR-012 원칙 5: **충족 HIGH**
- ADR-011 §2.3 (Hermes ≠ root of trust): **간접 답습 — `rfc8785` / `jcs` 도 root of trust 아님**

**판정**: APPROVE — Hermes 의존 0 강도 **HIGH**, ADR-008 차단조건 #2 위반 0건

---

### 2.5 영역 5 — 병렬 cross-check 강제의 보안 이점 vs 단순성 비용

**사실 인용** (본 PoC §3.1 답습):
- "두 라이브러리 모두 사용 — 출력 byte 동등성 + sha256 동등성 100% 검증을 corpus 24개 모든 case 에 강제. 양 라이브러리 의견 불일치 시 BLOCK + escalation (TR-C-2 trigger)"
- RA-9 §B.2 sanity 11/11 PASS (hash + 출력 byte 동일)

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| 단일 라이브러리 bug-class 회피 | **HIGH** | 단일 라이브러리 bug → 둘 다 동일 bug 일 확률 ≈ 독립 사건 곱 (assumption: 두 라이브러리가 *독립 구현*). RA-9 §B 답습 시 *서로 다른 author + 서로 다른 API surface* → *독립 구현* 가정 정합 |
| 단일 supply-chain 침해 (account takeover) 회피 | **HIGH** | `rfc8785` (Trail of Bits) + `jcs` (개인 titusz) = *서로 다른 maintainer* + *서로 다른 PyPI account*. 한 account 침해 시 cross-check 즉시 BLOCK (출력 불일치) |
| 단일 라이브러리 abandonment 회피 | **MEDIUM** | 한 라이브러리 abandonment 시 *cross-check* 손실되나 *기능 자체* 는 다른 라이브러리로 보존. 단 *abandonment 검출 자체가 외부 monitoring* 영역 (PyPI release frequency 등) — C-B6 권고 |
| 운영 비용 (단순성) | **LOW-MEDIUM** | 두 라이브러리 호출 + 동등성 비교 + corpus 24개 양쪽 회귀 = ~2x 검증 시간. 단 CI 단계에서만 발화 (run-time 추가 비용 0) — 본 PoC 형식적 검증 한정 |
| escalation TR-C-2 (corpus 동등성 실패) | **trigger 등록** | 본 PoC §9.1 답습 — `corpus 24개 중 1+ Primary ↔ Fallback 동등성 실패` 시 Q2/Q3 풀 3+1 격상. 단 본 PoC 는 *Primary ↔ Fallback* 표현인데, *Primary 1 ↔ Primary 2* 동등성 실패도 동일 trigger 발화 의무 명시 권고 — C-B7 |
| ADR-012 §2.12 #2 (filesystem 변조) cover 강화 | **HIGH** | filesystem 직접 변경으로 ledger entry 변조 시 → canonical hash 재계산 필요 → `rfc8785` ↔ `jcs` 동등성 비교 차원 cover (양쪽 동등 결과 일치 시 chain 검증 통과 가능 → 그러나 동등성 비교는 *변조 검출* 보다 *bug 검출* 영역) |

**ADR cross-reference**:
- ADR-012 §2.5 (JCS Primary + jq fallback): **답습 강화** (Primary 1 + Primary 2 + Fallback 3-tier)
- ADR-012 §11.3 (cryptography 심층 검토 한계): **부분 답습 강화** — cross-check 자체가 *crypto specialist 검증의 부분 대체* 까지는 아니나 *bug 검출 layer 강화*
- ADR-011 §2.1 (a) 동등 이상의 보안 결과: **충족** — 단일 라이브러리 대비 bug-class 회피 차원 강화

**판정**: APPROVE — 보안 이점 (단일 bug-class 회피 + supply-chain 다양화) > 단순성 비용 (CI 2x 시간). C-B7 escalation 명시 권고.

---

### 2.6 영역 6 — RFC 8785 명세 준수 검증 책임 (NaN/Infinity reject / IEEE 754 number / UTF-16 codepoint sort)

**사실 인용**:
- RFC 8785 §3.2.2.2 — NaN/Infinity reject (RA-9 §B.1 답습)
- RFC 8785 §3.2.2 — IEEE 754 number 동등 (RA-9 §B.2 #4, #5 답습 — `1` ↔ `1.0` 동일 hash)
- RFC 8785 §3.2.3 — UTF-16 codepoint sort (corpus §3.4 `key_ordering` 카테고리 답습)
- ADR-012 §11.3 직접 인용: "RFC 8785 JCS 동등 구현 검증은 본 합의 검토자 한계 — crypto specialist + cross-vendor (GPT-5.x or Gemini) 추가 의견 권고"
- 본 PoC §3.4 corpus 24개 (8 카테고리 × 3) — `unicode` / `number` / `key_ordering` / `escape` / `nested` / `array` / `hash_stability` / `lossy`

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| NaN/Infinity reject 검증 | **HIGH** | RA-9 §B.1 두 라이브러리 모두 reject 검증 완료. 본 PoC corpus `number` 카테고리 case 3 (`-0.0`) + reject case 적용 시점 추가 의무 — C-B8 권고 |
| IEEE 754 number 동등 | **HIGH** | RA-9 §B.2 #4, #5 양 라이브러리 동등 hash 결과 검증 완료 |
| UTF-16 codepoint sort | **MEDIUM** | RA-9 §B.2 #2, #10 unicode case 양 라이브러리 동등 검증 완료. 단 *non-BMP codepoint* (surrogate pair) 는 #3 (emoji `U+1F600`) 1건 만 검증 — 본 PoC corpus 24개 시 추가 surrogate pair case 권고 — C-B9 |
| 본 PoC 가 RFC 8785 명세 준수 *검증 가능* 한가 | **MEDIUM** | 본 PoC = *implementation 동등성 비교* + *corpus reference output 비교* — RFC 8785 자체의 *명세 준수* 까지는 IETF 권위 영역. `rfc8785` 라이브러리가 *RFC 명시 구현 의도* 표명 (Trail of Bits) → 권위 위계 신뢰 가능 |
| crypto specialist 추가 검토 의무 (ADR-012 §11.3) | **본 PoC 단계 발화 의무** | 본 PoC 자체가 *Implementation/Runtime 시제 직전 단계* — ADR-012 §11.3 답습 cross-vendor LLM 의뢰 + crypto specialist 추가 검토 권고 (영역 12 와 결합) — C-B10 |

**ADR cross-reference**:
- ADR-012 §2.5 (JCS Primary): **본 PoC 가 검증 layer** (corpus 24개 회귀)
- ADR-012 §11.3 (cryptography 심층 검토 한계): **본 PoC 단계 발화 의무** — cross-vendor 의뢰 권고
- 헌법 8조 (보안): **간접 답습 — Evidence 무결성의 *형식적 검증* 까지**

**판정**: APPROVE WITH CONDITIONS (C-B8 NaN/Infinity reject corpus case 추가 의무 + C-B9 non-BMP surrogate pair corpus case 추가 권고 + C-B10 cross-vendor LLM 의뢰)

---

### 2.7 영역 7 — fallback `jq -S -c` 의 supply chain 위험

**사실 인용** (본 PoC §3.2 + §6 답습):
- `jq -S -c .` (lex sort + compact + UTF-8 + RFC 8259 escape)
- POSIX 표준 도구 (debian/ubuntu/brew 배포)
- ADR-012 §2.5 명시 답습: "Fallback: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무"
- 본 PoC §6 CI workflow `setup` step: "Python 3.11 + `rfc8785` install + `jq` install"

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| Maintainer 신뢰도 | **HIGH** | `jq` (stedolan/jq) = 업계 표준 OSS, 광범위 배포 (debian/ubuntu/RHEL/brew/npm 등). organizational maintenance (jq 1.6, 1.7 등 정기 release) |
| 표준 도구 신뢰성 (ADR-012 원칙 5) | **HIGH** | "표준 도구 (`jq` + `sha256sum`) 만으로 검증 가능" 답습 — `jq` = ADR-012 명시 채택 표준 도구 |
| Version drift 위험 | **MEDIUM** | `jq` 1.6 vs 1.7 의 RFC 8259 escape 동작 차이 가능성 (예: `\u` escape 표현 미세 차이). 본 PoC corpus 24개 회귀 시 `jq` 특정 버전 pin 의무 — C-B11 권고 |
| RFC 8785 ↔ RFC 8259 차이 | **MEDIUM** | `jq -S -c` = RFC 8259 (JSON 표준) 기반 — RFC 8785 (JCS) 와 *완전 동등 보장 부재* (특히 number normalization, unicode escape 영역). ADR-012 §2.5 명시 "test corpus 검증 의무" 답습 — fallback 사용 시 corpus 24개 동등성 회귀 의무 |
| 배포 다양성 (single source 회피) | **HIGH** | debian/ubuntu/brew/npm/직접 build = 다중 distribution channel → 단일 source 침해 위험 분산 |
| CI install 시점 위험 | **MEDIUM** | `apt-get install jq` 자체가 외부 mirror 의존 (debian-security mirror 등) — air-gap 환경 시 별도 binary 보관 권고 — C-B12 |
| `event: canonical_json_fallback` audit trail | **HIGH** | 본 PoC §3.2 답습 — fallback 사용 시 자동 ledger entry 작성 → audit trail 보장 (영역 8 답습) |

**ADR cross-reference**:
- ADR-012 §2.5 (jq fallback 표준 답습): **충족**
- ADR-012 §3.5 (Fallback 사용 빈도 > 10% trigger): **본 PoC 시점 적용** — corpus 24개 동등성 100% 시 fallback 발화 빈도 0% 기대
- 헌법 5조 Provider Liquidity: **HIGH** (POSIX 표준 도구 = vendor-neutral)

**판정**: APPROVE WITH CONDITIONS (C-B11 `jq` 특정 버전 pin 의무 + C-B12 air-gap 환경 시 별도 binary 보관 권고)

---

### 2.8 영역 8 — `event: canonical_json_fallback` ledger entry 의 audit trail 적합성 (T1 audit 답습)

**사실 인용**:
- ADR-012 §2.2 enum #17: `canonical_json_fallback` — T1 audit
- ADR-012 §2.5 직접 인용: "Fallback 사용 시 의무: `event: canonical_json_fallback` ledger entry 작성 의무 + Reviewer 알림 + 사용자 review 권장"
- 본 PoC §3.2: "사용 시 `event: canonical_json_fallback` ledger entry 자동 작성 의무"
- ADR-011 §2.4 T1 분류: "자동 허용 — Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 / 승인 경로 = 자동"

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| T1 audit 분류 적합성 | **HIGH** | Fallback 사용 = *자동 허용* (Primary 라이브러리 install 실패 시 자동 fallback) + *audit trail 의무* (`event` ledger entry) → ADR-011 §2.4 T1 분류 정합. 자동 허용 + 사후 audit 패턴 |
| ADR-012 §3.5 fallback 빈도 monitoring trigger 정합 | **HIGH** | "Fallback 사용 빈도 > 10% → JCS Primary 검토 합의 trigger" 답습 — `canonical_json_fallback` ledger entry 자동 작성 → 빈도 자동 monitoring 가능 |
| audit trail 완전성 | **HIGH** | ledger entry 11 필드 schema → fallback 사용 시점 (`ts`) + agent (`agent`) + 사유 (`content`) 모두 기록. hash chain 으로 변조 차단 (Layer 1) |
| Reviewer 알림 + 사용자 review 권장 (ADR-012 §2.5) | **MEDIUM** | 본 PoC 사양은 *ledger entry 작성* 까지 — *Reviewer 알림 매커니즘* 명시 부재 (CI workflow notification step 권고 — C-B13) |
| T2/T3 escalation 시점 명시 | **MEDIUM** | "Fallback 사용 빈도 > 10%" = ADR-012 §3.5 *별도 합의 trigger* (T3 변경 = ADR 본문 갱신). 본 PoC §9.1 TR-C-4 답습 ("round-trip T2 strict 실패율 > 0%") 와 정합. fallback 빈도 trigger 발화 시 T2 (사용자 명시 결정) escalation 권고 — C-B14 |

**ADR cross-reference**:
- ADR-011 §2.4 T1: **충족** (자동 허용 + audit)
- ADR-012 §2.2 enum #17 + §2.5 fallback 의무: **충족 강화**
- ADR-012 §3.5 monitoring trigger: **충족** (fallback 빈도 자동 추적 가능)

**판정**: APPROVE WITH CONDITIONS (C-B13 CI workflow Reviewer notification step 권고 + C-B14 fallback 빈도 > 10% 시 T2 escalation 절차 명시)

---

### 2.9 영역 9 — prev_hash 검증 실패 → BLOCK + manual review 정책의 ADR-011 §2.4 (T3 자동 정책 변경 금지) 정합성

**사실 인용**:
- ADR-012 §2.7 (prev_hash 검증 실패 처리 — BLOCK + Manual Review): "1. 즉시 BLOCK / 2. 기존 원본 JSONL 보존 — 자동 revert 금지 (T3 위반 위험) / 3. 새 violation entry append / 4. 사용자 명시 review 의무 / 5. 자동 revert 금지 / 6. Dual write 금지"
- ADR-011 §2.4 T3: "자동 금지 (절대) — Constitution / ADR / Harness Gates 정의 자체의 변경 / 승인 경로 = 단축 또는 풀 3+1 합의"
- 본 PoC §4.2 검사 3: "불일치 검출 시 → BLOCK + `chain_violation_detected` ledger entry 자동 작성"
- 본 PoC §7 답습 강제 조건: "ADR-011 §2.4 (T1/T2/T3) → T3 위반 자동 revert 금지 → chain violation = BLOCK + manual + violation entry (자동 revert 0건)"

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| ADR-011 §2.4 T3 (자동 정책 변경 금지) 정합 | **HIGH** | chain violation 검출 시 *자동 revert / 자동 chain 재계산 / 자동 entry 수정* 모두 금지 → ADR-011 §2.4 T3 답습 직접 정합 |
| BLOCK + manual review 운영 매커니즘 | **HIGH** | 본 PoC `jsonl_hash_chain.py` rc=1 + `chain_violation_detected` entry 자동 작성 + 사용자 명시 review 의무. 자동화는 *검출 + 기록* 까지, 수정은 사용자 명시 결정 |
| `chain_violation_detected` entry 자동 작성의 T1/T3 분류 | **HIGH** | violation 검출 = T1 (자동 audit) / chain 수정 = T3 (자동 금지) 분리 정합. `chain_violation_detected` entry 자체는 T3 BLOCK 분류 (ADR-012 §2.2 enum #14) 답습 |
| violation_type 4종 cover (ADR-012 §2.7) | **HIGH** | 본 PoC §5.2 FAIL fixture × 4 답습 — `prev_hash_mismatch` / `hash_recalculation` / `missing_event_field` (schema BLOCK) / `roundtrip_lossy_no_entry`. 단 ADR-012 §2.7 명시 violation_type 은 `prev_hash_mismatch` / `hash_recalculation` / `history_rewrite` / `genesis_mismatch` 4종 — 본 PoC 의 `missing_event_field` / `roundtrip_lossy_no_entry` 는 *별도 schema/round-trip 영역* 에 해당. 4 violation_type 직접 cover 는 2/4 (`prev_hash_mismatch` / `hash_recalculation`) 한정 — Gap-N (§7) |
| 자동 revert 금지의 영구 권위 | **HIGH** | ADR-012 §2.7 #5 + §2.7 #6 (Dual write 금지) + ADR-011 §2.4 T3 = 영구 권위. 본 PoC = *영구 권위 답습 적격* |

**ADR cross-reference**:
- ADR-011 §2.4 T3 (자동 정책 변경 금지): **충족 HIGH**
- ADR-012 §2.7 (prev_hash 실패 처리): **충족 강화** (4 단계 답습)
- ADR-012 원칙 9: "Hash chain 검증 실패 = 즉시 BLOCK. 자동 복구 / 자동 revert 금지 (T3 위반 위험 답습)" — **충족 HIGH**

**판정**: APPROVE — ADR-011 §2.4 T3 + ADR-012 §2.7 정합 강도 **HIGH**. 단 violation_type 4종 직접 cover 부분 (Gap, §7 enumerate)

---

### 2.10 영역 10 — Hermes 변조 차단 매트릭스 (ADR-012 §2.12 4항목) 와의 정합성

**사실 인용** (ADR-012 §2.12 답습):

| # | 변조 영역 | 차단 매커니즘 |
|---|--------|---------|
| 1 | Hermes-originated ledger entry | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject |
| 2 | 파일 변조 (filesystem 직접 변경) | `evidence/<scope>.jsonl` filesystem read-only + audit log + 컨테이너 정지 |
| 3 | Git commit (Hermes 가 ledger commit 시도) | Hermes-originated commit auto-reject |
| 4 | 외부 LLM 응답 위조 | External LLM response ledger entry `agent = "user"` 강제 + signed commit 권장 |

**보안/거버넌스 평가 — 본 PoC cover 매트릭스**:

| # | 변조 영역 | 본 PoC cover | 근거 |
|---|--------|--------|----|
| 1 | Hermes-originated ledger entry | **부분 cover** (간접) | 본 PoC = *형식적 무결성 검증 도구* — write 권한 강제는 G3 §2.5 영역. 단 `agent` 필드 enum (`user` / `claude-code` / `hermes` / `external_llm`) 검증으로 *agent 식별 layer* 제공 + chain 검증으로 *Hermes-originated entry 사후 검출 가능* |
| 2 | 파일 변조 (filesystem 직접 변경) | **HIGH cover** | 본 PoC 의 핵심 cover 영역 — hash chain 검증 (Layer 1) 으로 *middle entry tampering 차단*. canonical JSON 일관성 + sha256 = filesystem 직접 변조 *결정적 검출* |
| 3 | Git commit (Hermes 가 ledger commit 시도) | **부분 cover** (간접) | git commit author 검증은 본 PoC 영역 외 (Layer 2 git append-only branch + commit author hook). 단 chain 검증 결과를 git pre-commit hook 에서 호출 가능 — 본 PoC 가 *호출 대상 도구* 제공 |
| 4 | 외부 LLM 응답 위조 | **0 cover** | `event: external_llm_received` enum #8 = 본 PoC MVP 4종 한정 외 (영역 11 답습). 본 PoC 는 *형식적 무결성* 까지 — 외부 LLM response ledger entry 의 *content 자체 위조* 는 ADR-012 §3.3 한계 답습 (content-level forgery 방어 범위 외) |

**ADR cross-reference**:
- ADR-012 §2.12 4 항목: **#2 HIGH cover + #1/#3 부분 cover (도구 제공) + #4 0 cover (별도 합의 영역)**
- ADR-011 §2.3 (Hermes ≠ root of trust): **간접 답습 — 본 PoC 가 Hermes-originated entry 검출 layer 강화**

**판정**: APPROVE — §2.12 #2 (filesystem 변조) HIGH cover. #1/#3 부분 cover (도구 제공). #4 미cover 는 별도 영역 (Gap-N §7 enumerate)

---

### 2.11 영역 11 — `event` 17 enum 중 본 PoC MVP 4종 한정의 보안 충분성

**사실 인용**:
- ADR-012 §2.2 17 enum (MVP 의무 12 + 후속 확장 5)
- 본 PoC MVP 4종: `canonical_json_fallback` (#17) / `chain_violation_detected` (#14) / `roundtrip_lossy` (#11) / `roundtrip_fail` (#12)
- 본 PoC §11 한계 L-3: "`event` 17 enum 중 MVP 4종 한정 검증 → ADR-012 §2.2 답습 — 17 enum 전체 검증은 별도 합의"
- 본 PoC §9.1 TR-C-3: "`event` 17 enum 중 본 PoC MVP 4종 외 추가 발화 → 별도 합의 + ADR-012 §2.2 cross-reference"

**보안/거버넌스 평가 — 미적용 13 enum 위험 분석**:

| # | enum (미적용) | T 분류 | 미적용 위험 |
|---|------|----|------|
| 1 | `memory_write` | T1/T2 | 본 PoC = 형식 검증 한정 → 미적용 LOW (Group E/G 영역) |
| 2 | `skill_proposed` | T1 | 동일 LOW |
| 3 | `skill_approved` | T2 | 동일 LOW |
| 4 | `skill_promoted` | T2 + Evidence | 동일 LOW |
| 5 | `skill_revoked` | T3 자동 안전 | **MEDIUM** — rollback_trigger 검출은 본 PoC 영역 외, Group G 영역 |
| 6 | `gate_pass` | T2 사용자 명시 | LOW (별도 gate 합의 영역) |
| 7 | `gate_fail` | T2 사용자 명시 | LOW (별도) |
| 8 | `external_llm_received` | T2 + agent="user" 강제 | **HIGH** — ADR-012 원칙 7 + §3.1 강제. 영역 10 #4 cover 0 답습. 본 PoC 미적용 시 *Hermes 가 외부 LLM response 를 자기 제안으로 위조 차단* 영역 부재 — Gap-N #1 (§7) |
| 9 | `evidence_forgery_detected` | T3 BLOCK | **HIGH** — P10 (Evidence Forgery) 정식 등록 trigger 답습 (ADR-012 §1.3). 본 PoC 미적용 시 *forgery 검출 layer 자체* 가 부재 — Gap-N #2 (§7) |
| 13 | `migration_failed` | T3 BLOCK + manual | LOW (Group H 영역 — 사용자 명시 금지) |
| 15 | `hash_chain_broken` | T3 BLOCK | **MEDIUM** — `chain_violation_detected` (#14) 와 의미 중첩. 본 PoC 가 #14 cover → #15 간접 cover. 단 enum 중복 정리 권고 — C-B15 |
| 16 | `policy_change_attempted` | T3 BLOCK + audit | **HIGH** — Hermes 가 정책 변경 시도 (T3 위반) 검출 enum. 본 PoC 미적용 시 *policy change 시도 검출 layer* 부재 — Gap-N #3 (§7) |

**보안/거버넌스 평가 — 본 PoC 4종 한정 충분성**:

| 차원 | 평가 | 근거 |
|----|----|----|
| 형식적 무결성 cover (본 PoC 명시 범위) | **HIGH** | 본 PoC = 형식 검증 (canonical / hash chain / round-trip) 한정. MVP 4종 = 본 PoC 영역 정확 cover |
| Evidence Forgery 검출 layer 부재 | **HIGH 위험** | `evidence_forgery_detected` (#9) 미적용 → P10 정식 등록 trigger 답습 부분 발화 (Gap-N #2) |
| Hermes 변조 차단 영역 부재 | **HIGH 위험** | `policy_change_attempted` (#16) 미적용 → Hermes 가 정책 변경 시도 검출 부재 (Gap-N #3) |
| 외부 LLM 위조 차단 영역 부재 | **HIGH 위험** | `external_llm_received` (#8) 미적용 → 영역 10 #4 cover 0 답습 (Gap-N #1) |
| 별도 합의 영역 명시 | **HIGH** | 본 PoC §11 L-3 한계 자기 명시 적격 + §9.1 TR-C-3 escalation trigger 등록 적격 |

**ADR cross-reference**:
- ADR-012 §2.2 17 enum + MVP 12 의무: **본 PoC = MVP 4종 한정 (12 의무 중 4건)**. 8건 미cover (#1, #2, #3, #4, #6, #7, #8, #9, #10) 중 #8 / #9 = HIGH 위험 영역
- ADR-012 §1.3 P10 정식 등록: **본 PoC 가 부분 발화** — `chain_violation_detected` (#14) cover 까지, `evidence_forgery_detected` (#9) 미발화

**판정**: APPROVE WITH CONDITIONS — 형식적 무결성 cover HIGH 적격. 단 **3 HIGH Gap (#8, #9, #16)** 별도 합의 영역 명시 의무 (§7 Gap-N enumerate). C-B15 enum 중복 정리 권고 (#14 ↔ #15).

---

### 2.12 영역 12 — `external_review/` 또는 cross-vendor LLM 검증 의무 발화 여부

**사실 인용**:
- ADR-012 §11.3 직접 인용: "RFC 8785 JCS 동등 구현 검증은 본 합의 검토자 한계 — crypto specialist 추가 검토 권고 (별도 합의) — 본 ADR §2.5 의 fallback `jq -S -c` 가 JCS 와 *모든 케이스 동등* 보장 부재 — test corpus 검증 의무 (별도 PR — Implementation 영역)"
- ADR-012 §11.2 C-14: "본 ADR-012 머지 후 P2 v3 정식 채택 진입 *전* cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무"
- PR-2 합의 §6.3 답습: "ADR 신규 발행 = T3 변경 (ADR-011 §2.4) → 풀 3+1 + 외부 LLM 1+ 의무 (G3 §4.4.2). 본 PR-2 = 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) 충족"
- 본 PoC §10 Evidence 5 형식 — `external_review/` 디렉토리 발화 0건

**보안/거버넌스 평가**:

| 차원 | 평가 | 근거 |
|----|----|----|
| 본 PoC 자체의 cross-vendor 의뢰 의무 발화 | **MEDIUM-HIGH** | 본 PoC = ADR-012 §2.5 *Implementation 영역 PoC* — ADR-012 §11.3 명시 "test corpus 검증 의무 (별도 PR — Implementation 영역)" 답습 시 본 PoC = *해당 별도 PR* 위치. 따라서 *cross-vendor LLM 의뢰 권고 강도 MEDIUM-HIGH* (ADR 신규 발행은 아니나 ADR-012 §11.3 명시 영역 충족 산출) |
| crypto specialist 추가 검토 권고 (ADR-012 §11.3) | **HIGH** | 본 PoC 는 *RFC 8785 동등성* 정확히 검증 — crypto specialist 추가 검토 권고 영역 직접 적중. 단 *crypto specialist* 는 외부 인적 자원 영역 — cross-vendor LLM 의뢰가 *부분 대체* (외부 LLM 1+ + crypto-aware prompt) |
| C-14 cross-vendor 의뢰 답습 적격성 | **MEDIUM** | C-14 = ADR-012 *머지 후 P2 v3 정식 채택 진입 전* 의무 — 본 PoC 는 *ADR-012 머지 후 단계* 정합. C-14 의뢰가 *본 PoC 영역 cover* 하는지 명시 부재 — Reviewer 영역 |
| `external_review/` 디렉토리 사용 권고 | **HIGH** | PR-2 답습 시 외부 LLM 응답은 `external_review/` 디렉토리 + `event: external_llm_received` ledger entry (영역 11 #8 답습). 본 PoC 가 cross-vendor 의뢰 발화 시 동일 패턴 답습 의무 |
| Q1 풀 3+1 합의 + cross-vendor 1+ 결합 권고 | **HIGH** | 본 의제 = *Q1 풀 3+1 합의* — Q1 결과 + cross-vendor 의뢰 1+ 결합 권고 (PR-2 5/5 입력 답습 패턴) — C-B16 |

**ADR cross-reference**:
- ADR-012 §11.2 C-14: **본 PoC 단계 발화 권고 (Reviewer 결정 영역)**
- ADR-012 §11.3 cryptography 심층 검토 한계: **본 PoC = 정확 적중 영역**, 외부 LLM 의뢰 권고 강도 HIGH
- PR-2 §6.3 (ADR 신규 발행 외부 LLM 1+ 의무): **간접 답습** — 본 PoC = ADR 신규 발행 아니나 *Implementation 영역 PoC* 의 보안 검증 차원에서 동일 패턴 권고

**판정**: APPROVE WITH CONDITIONS (C-B16 Q1 풀 3+1 합의 + cross-vendor LLM 1+ 의뢰 결합 권고)

---

## 3. Risk Assessment

### 3.1 위험 분류 매트릭스

| 위험 | 영역 | 분류 | 근거 | 완화 |
|---|---|---|---|---|
| `jcs` (titusz) 개인 maintainer abandonment / supply-chain compromise | 영역 2 | **HIGH** | PyPI account takeover 사례 답습 + organizational backing 부재 | C-B3 (last release 검증) + C-B4 (`jcs` primary 단독 격상 금지 영구) + C-B5 (abandonment 시 fallback 정책) |
| `event` 17 enum 중 `external_llm_received` (#8) 미적용 — Hermes 외부 LLM response 위조 차단 layer 부재 | 영역 11 | **HIGH** | ADR-012 §2.12 #4 cover 0 + 원칙 7 답습 부분 발화 | Gap-N #1 (§7) — 별도 합의 영역 명시 + 본 PoC §11 L-3 한계 흡수 |
| `evidence_forgery_detected` (#9) 미적용 — P10 (Evidence Forgery) 정식 등록 trigger 부분 발화 | 영역 11 | **HIGH** | ADR-012 §1.3 P10 정식 등록 trigger 답습 → 본 PoC = `chain_violation_detected` (#14) cover 까지 | Gap-N #2 (§7) |
| `policy_change_attempted` (#16) 미적용 — Hermes 정책 변경 시도 검출 layer 부재 | 영역 11 | **HIGH** | ADR-011 §2.4 T3 + ADR-012 §2.12 #1 답습 — 본 PoC = filesystem 변조 (§2.12 #2) cover 까지 | Gap-N #3 (§7) |
| `rfc8785` 0.1.4 = 초기 버전 (semver 0.x) 의 API 안정성 미보증 | 영역 1 | **MEDIUM** | semver 0.x convention | C-B2 (0.x → 0.2 격상 시 RA-9 재실행) |
| `jq` version drift (1.6 vs 1.7 의 escape 동작 차이) | 영역 7 | **MEDIUM** | RFC 8259 escape 표현 미세 차이 가능성 | C-B11 (`jq` 특정 버전 pin) |
| RFC 8785 ↔ RFC 8259 (jq) 동등성 부분 미보장 | 영역 7 | **MEDIUM** | ADR-012 §2.5 명시 "test corpus 검증 의무" 답습 | 본 PoC corpus 24개 회귀로 *부분 완화* + fallback 발화 빈도 monitoring (§3.5 §3.5) |
| crypto specialist 외부 검토 부재 | 영역 6, 12 | **MEDIUM** | ADR-012 §11.3 명시 권고 영역 | C-B10 + C-B16 (cross-vendor LLM 의뢰) |
| RA-9 §B `signature` 검증 미수행 (PyPI sigstore / GPG) | 영역 1, 2 | **MEDIUM** | RA-9 §B 미검증 영역 | C-B1 (signature 검증 별도 의무) |
| `jcs` last release / commit frequency 미검증 | 영역 2 | **MEDIUM** | RA-9 §B 미검증 | C-B3 |
| CI install 시점 외부 mirror 의존 (air-gap 위험) | 영역 7 | **LOW-MEDIUM** | `apt-get install jq` 의 debian mirror 의존 | C-B12 (별도 binary 보관) |
| Apache-2.0 라이선스 호환성 위험 | 영역 3 | **LOW** | Permissive license, 광범위 호환 | (완화 불필요) |
| Hermes 직접 의존 발생 위험 | 영역 4 | **LOW** | RA-9 §B.4 두 라이브러리 모두 Requires=없음 검증 | 본 PoC 자체가 *충족 검증 evidence* 산출 |
| 단순 ledger entry 17 enum 중 #14 ↔ #15 의미 중첩 | 영역 11 | **LOW** | enum 중복 정리 권고 영역 | C-B15 |

### 3.2 종합 위험 분포

- **HIGH**: 4건 (`jcs` maintainer / `external_llm_received` 미적용 / `evidence_forgery_detected` 미적용 / `policy_change_attempted` 미적용)
- **MEDIUM**: 6건
- **LOW-MEDIUM**: 1건
- **LOW**: 3건

**판정**: HIGH 4건 모두 *Gap-N 별도 합의 영역 명시 + 본 PoC §11 한계 흡수* 로 완화 가능. CRITICAL 0건 → **APPROVE WITH CONDITIONS** 적격.

---

## 4. Provider Liquidity 보존 강도 매트릭스 (5 영구 핵심 제약)

| 제약 | 권위 근거 | 본 PoC Q1 보호 위치 | 강도 |
|---|---|---|---|
| Provider Liquidity (헌법 5조 비협상) | `feedback_provider_liquidity.md` + ADR-008 차단조건 #2 | `rfc8785` + `jcs` 모두 Apache-2.0 + provider-neutral PyPI + 의존 0 + `jq` POSIX 표준 + RFC 8785 IETF 표준 (vendor-neutral) + 라이브러리 교체 비용 LOW (RFC 동등성 byte-level) | **HIGH** |
| Hermes ≠ root of trust (ADR-011 §2.3 영구 권위) | ADR-011 §2.3 + ADR-012 §2.12 | 본 PoC 도구 = `import hermes_agent` 0건 + `agent` 필드 enum 검증 + chain 검증으로 Hermes-originated entry *사후 검출 layer* 제공. 단 §2.12 #1/#3/#4 미cover 영역 존재 | **HIGH** (단 §7 Gap-N 4건 통한 영구 보호 강화 의무) |
| 메타포 강제 금지 (system-identity-prequel §7) | ADR-012 §1.5 답습 | 본 PoC = *형식적 무결성 한정 자기 명시* (§0, §11 L-5 한계) — *불변의 진리* 메타포 회피. 두 라이브러리 = *cross-check reference*, root of trust 메타포 부여 0건 | **HIGH** |
| 자동 정책 변경 금지 (T3 — ADR-011 §2.4) | ADR-011 §2.4 + ADR-012 §2.7 | chain violation 검출 시 자동 revert 0건 + manual review 강제 + `chain_violation_detected` entry 자동 작성 (T1 audit) ↔ 정책 변경 (T3 BLOCK) 분리 정합. fallback 사용 = T1 audit (영역 8 답습) | **HIGH** |
| 수단/목적 분리 (ADR-011 §2.1 (a)~(e)) | ADR-011 §2.1 5조건 | (a) 동등 이상 보안 결과 — 단일 라이브러리 대비 cross-check 강화 / (b) 격리 환경 PoC 실증 — 본 PoC venv `.poc-prep/jcs-ra9-venv/` (Docker 격리는 별도 권고) / (c) ADR 권위 명시 — ADR-012 §2.5 답습 / (d) 자동 회귀 검증 — `.github/workflows/g4-hash-chain.yml` / (e) 합의 APPROVE — 본 Q1 풀 3+1 진행 중 | **HIGH** ((b) Docker 격리 별도 권고 — C-B17) |

**5/5 HIGH 보호 적격** (단 (b) Docker 격리 + Hermes 변조 차단 §2.12 4 항목 cover 보강 의무 — §7 Gap-N).

**Provider Liquidity 5-way Multi-layer Defense (ADR-012 §6.2 답습) 답습**:
- Layer 1 GP-5 / Layer 2 G3 §6.4 / Layer 3 G4 §3.5 / Layer 4 G4 §4.3 / Layer 5 ADR-012 (Evidence 형식 layer)
- 본 PoC = **Layer 5 (Evidence 형식 차원)** 직접 강화 — 11 필드 + provider-neutral `agent` enum + Hermes 의존 0 ledger entry 도구

---

## 5. Hermes 변조 차단 매트릭스 cover 분석 (ADR-012 §2.12 4 항목 ↔ 본 PoC)

| # | 변조 영역 | 차단 매커니즘 (ADR-012 §2.12 답습) | 본 PoC cover | 강도 | Gap |
|---|--------|---------|----|----|---|
| 1 | Hermes-originated ledger entry (Hermes 자기 entry 작성 시도) | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject | **부분 cover** — `agent` 필드 enum 검증 (`hermes` 식별 가능) + chain 검증으로 사후 검출 가능. 단 *작성 차단* 매커니즘 (write 권한 0 / commit auto-reject) 본 PoC 영역 외 | MEDIUM | 작성 차단 매커니즘 = G3 §2.5 #11 + G3 §2.2 #20 영역 (별도) |
| 2 | 파일 변조 (filesystem 직접 변경) | `evidence/<scope>.jsonl` filesystem read-only + audit log + 컨테이너 정지 | **HIGH cover** — 본 PoC 핵심 영역. hash chain 검증 (Layer 1) + canonical JSON 일관성 + sha256 = filesystem 직접 변조 *결정적 검출* | **HIGH** | 0 |
| 3 | Git commit (Hermes 가 ledger commit 시도) | Hermes-originated commit auto-reject (commit author = Hermes 검출 시 차단) | **부분 cover** — chain 검증 결과를 git pre-commit hook 에서 호출 가능 (본 PoC 가 *호출 대상 도구* 제공). commit author 검증 자체는 본 PoC 영역 외 | MEDIUM | git pre-commit hook commit author 검증 = G3 §2.2 #20 영역 (별도) |
| 4 | 외부 LLM 응답 위조 (Hermes 가 외부 LLM response 를 자기 제안으로 위조) | External LLM response ledger entry `agent = "user"` 강제 + signed commit 권장 (multi-host 시 의무) | **0 cover** — `event: external_llm_received` (#8) MVP 4종 한정 외 (영역 11 답습) | 0 (HIGH Gap) | Gap-N #1 (§7) — 별도 합의 영역 명시 의무 |

**종합 판정**:
- **#2 HIGH cover** (본 PoC 핵심 영역 적중)
- **#1 / #3 부분 cover** (도구 제공 — 별도 차단 매커니즘 영역 명시)
- **#4 0 cover** (Gap-N #1 §7 enumerate)

본 PoC 는 ADR-012 §2.12 4 항목 중 **1/4 HIGH cover + 2/4 부분 cover + 1/4 0 cover**. **최소 1/4 HIGH cover 충족** → §2.12 답습 *부분 적격* 적격성. 단 1/4 0 cover 영역 (#4) 은 §7 Gap-N #1 흡수 의무.

---

## 6. 추가 권고 조건 (C-B1 ~ C-B17)

| # | 조건 | 영역 | 강도 | 처리 |
|---|---|---|---|---|
| C-B1 | `rfc8785` PyPI signature (sigstore / GPG) 검증 의무 명시 — 별도 RA-9 후속 항목 | 1 | MEDIUM | 본 PoC 외 별도 합의 |
| C-B2 | `rfc8785` 0.x → 0.2 격상 시 RA-9 재실행 의무 | 1 | MEDIUM | 본 PoC §9.1 escalation trigger 추가 (TR-C-6 권고) |
| C-B3 | `jcs` last release date / commit frequency 검증 의무 | 2 | HIGH | RA-9 §B 보강 + 본 PoC 머지 전 의무 |
| C-B4 | `jcs` *primary 단독 격상 금지 영구 명시* — `rfc8785` abandonment 시에도 단독 fallback 금지 | 2 | HIGH | 본 PoC §3.1 명시 보강 + ADR-012 §2.5 cross-reference |
| C-B5 | `jcs` maintainer abandonment 시 본 PoC fallback 정책 명시 (`rfc8785` + jq 단독 또는 다른 라이브러리 cross-check) | 2 | HIGH | 본 PoC §9.1 escalation trigger 추가 (TR-C-7 권고) |
| C-B6 | PyPI release frequency monitoring 권고 (월 1회 자동 확인) | 2 | MEDIUM | 별도 합의 |
| C-B7 | Primary 1 ↔ Primary 2 동등성 실패 escalation 명시 (TR-C-2 표현 보강) | 5 | HIGH | 본 PoC §9.1 TR-C-2 본문 명시 보강 — "Primary ↔ Fallback" → "Primary 1 ↔ Primary 2 또는 Primary ↔ Fallback" |
| C-B8 | corpus `number` 카테고리에 NaN/Infinity reject case 추가 의무 | 6 | HIGH | 본 PoC corpus 24개 + reject case 별도 (24+N 권고) |
| C-B9 | corpus `unicode` 카테고리에 non-BMP surrogate pair case 추가 권고 (현 1건 → 3건) | 6 | MEDIUM | 본 PoC §3.4 corpus 보강 |
| C-B10 | crypto specialist 추가 검토 권고 (ADR-012 §11.3 답습) — 본 PoC 머지 후 별도 의뢰 | 6 | MEDIUM-HIGH | 별도 합의 (cross-vendor LLM 의뢰로 부분 대체 가능) |
| C-B11 | `jq` 특정 버전 pin 의무 (예: `jq>=1.6,<1.8`) | 7 | MEDIUM | 본 PoC `.github/workflows/g4-hash-chain.yml` setup step 명시 보강 |
| C-B12 | air-gap 환경 시 `jq` binary 별도 보관 권고 | 7 | LOW-MEDIUM | 본 PoC §6 setup step 주석 보강 |
| C-B13 | CI workflow Reviewer notification step 권고 (`canonical_json_fallback` entry 발화 시) | 8 | MEDIUM | 본 PoC §6 + 별도 합의 |
| C-B14 | fallback 빈도 > 10% 시 T2 escalation 절차 명시 (ADR-012 §3.5 답습) | 8 | MEDIUM | 본 PoC §9.1 TR-C-4 본문 보강 ("round-trip T2 strict 실패율" → "+ fallback 빈도 > 10%") |
| C-B15 | `event` enum #14 (`chain_violation_detected`) ↔ #15 (`hash_chain_broken`) 의미 중첩 정리 권고 | 11 | LOW | 별도 합의 (ADR-012 §2.2 본문 갱신 영역) |
| C-B16 | Q1 풀 3+1 합의 + cross-vendor LLM 1+ 의뢰 결합 권고 (ADR-012 §11.2 C-14 답습) | 12 | HIGH | Reviewer 결정 영역 — `external_review/` 디렉토리 사용 + `event: external_llm_received` 패턴 답습 (별도) |
| C-B17 | 본 PoC 격리 환경 보강 — 현 venv 격리 + Docker 격리 권고 (ADR-011 §2.1 (b) 답습) | 4 매트릭스 (b) | MEDIUM | 본 PoC §7 답습 강제 조건 보강 |

**조건 17건 — HIGH 5건 / MEDIUM-HIGH 1건 / MEDIUM 7건 / LOW-MEDIUM 1건 / LOW 1건**

본 의제 *Q1* 한정 핵심 조건: **C-B3, C-B4, C-B7, C-B8, C-B16** (HIGH 5건). 그 외는 별도 합의 / PoC §9 escalation trigger 보강 / corpus 보강 영역.

---

## 7. Gap-N (HIGH) — 본 PoC 가 cover 하지 못하는 보안/거버넌스 영역

본 §7 = PR-2 Agent B Gap-17 답습 형식 — 본 의제 *Q1 한정* HIGH Gap enumerate.

### Gap-N #1 (HIGH): External LLM Response 위조 차단 layer 0 cover

**사실**:
- ADR-012 §2.12 #4 = External LLM response ledger entry `agent = "user"` 강제 + signed commit 권장
- ADR-012 원칙 7 = "External LLM response 적재 시 entry `agent = "user"` (수동 paste 주체) 강제. Hermes 가 외부 LLM response 를 자기 제안으로 위조 차단"
- 본 PoC MVP 4종 = `canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`
- `event: external_llm_received` (#8) = MVP 4종 한정 외

**위험**:
- 본 PoC 단계에서 외부 LLM 위조 차단 layer 부재
- ADR-012 §2.12 #4 cover 0 강도
- Hermes PMO 격상 전 단계에서는 *간접 위험* 이지만, P2 v3 정식 채택 진입 시 *HIGH 위험* 발화

**완화**:
- 본 PoC §11 L-3 한계 자기 명시 적격
- 별도 합의 영역 명시 의무 — *외부 LLM response ledger entry 형식 PoC* (ADR-012 §3.1 답습)
- C-B16 (Q1 cross-vendor LLM 의뢰) 결합 시 *Q1 합의 자체* 가 외부 LLM 의뢰 evidence 산출 → 부분 완화

### Gap-N #2 (HIGH): Evidence Forgery 검출 layer 부분 cover

**사실**:
- ADR-012 §1.3 = "본 ADR-012 발행 시점 = G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 *트리거*"
- ADR-012 §2.2 enum #9 = `evidence_forgery_detected` — T3 BLOCK
- 본 PoC = `chain_violation_detected` (#14) cover 까지 — `evidence_forgery_detected` (#9) 미발화

**위험**:
- 본 PoC 가 *chain violation* 검출 까지 cover, *forgery 검출 자체* 미적용
- chain violation 은 *형식적 변조 검출* — forgery 는 *의미적 변조 검출* (ADR-012 §3.3 한계 답습)
- 본 PoC = ADR-012 §3.3 한계 (content-level forgery 방어 범위 외) 자기 명시 적격

**완화**:
- 본 PoC §0 + §11 L-5 자기 명시 적격
- ADR-012 §3.3 답습 명시 — content-level forgery = 헌법 1조 + 합의 인프라 + Reviewer 종합 + Human override layer
- 본 PoC 영역 외 = 적격

### Gap-N #3 (HIGH): Policy Change Attempted 검출 layer 0 cover

**사실**:
- ADR-012 §2.2 enum #16 = `policy_change_attempted` — T3 BLOCK + audit
- ADR-012 §2.12 #1 = Hermes-originated ledger entry 차단 (`policy_change_attempted` 검출 = 핵심 매커니즘)
- 본 PoC MVP 4종 한정 외

**위험**:
- 본 PoC = filesystem 변조 (§2.12 #2) cover 까지
- Hermes 가 정책 변경 시도 시 검출 layer 부재
- ADR-011 §2.4 T3 (자동 정책 변경 금지) 운영 매커니즘 부분 발화

**완화**:
- 본 PoC = Hermes container write 권한 0 (G3 §2.5 #11) 영역 외 자기 명시
- 별도 합의 영역 명시 의무 — *Hermes 정책 변경 시도 검출 hook* (Group G 영역)

### Gap-N #4 (HIGH): `jcs` (titusz) 개인 maintainer supply chain HIGH 잔여 위험

**사실**:
- 영역 2 분석 답습
- `jcs` Author = 개인 maintainer (titusz, `tp@py7.de`)
- organizational backing 부재 + 외부 audit 부재 가능성

**위험**:
- PyPI account takeover / abandonment / malicious update 위험
- 본 PoC = cross-check 보강 layer 사용 → 단일 source 위험 *부분 완화*
- 단 `jcs` 단독 fallback 시 (예: `rfc8785` 동시 abandonment) HIGH 위험 발화

**완화**:
- C-B3 / C-B4 / C-B5 / C-B6 결합 적용 의무
- 본 PoC §3.1 명시 ("`jcs` *primary 단독 격상 금지* 영구") 권고
- escalation trigger TR-C-7 등록 권고 (C-B5)

### Gap-N #5 (MEDIUM-HIGH): RA-9 §B 미검증 영역 — signature / last release / abandonment 검출

**사실**:
- RA-9 §B = install + license + 의존 + sanity check 6 항목
- 미검증: PyPI signature (sigstore / GPG) / last release date / commit frequency / abandonment 검출

**위험**:
- supply chain compromise 사후 검출 layer 부재
- `rfc8785` / `jcs` 양쪽 모두 적용

**완화**:
- C-B1 (signature 검증 별도 의무) + C-B3 (last release 검증) + C-B6 (PyPI release frequency monitoring)
- 본 PoC 머지 *전* 의무 적용 권고

---

**Gap-N 종합**: HIGH 4건 + MEDIUM-HIGH 1건. 모두 *별도 합의 영역 명시* + *본 PoC §11 한계 흡수* + *C-B 조건 적용* 으로 완화 가능. CRITICAL Gap 0건.

---

## 8. Verdict

### 8.1 판정

**APPROVE WITH CONDITIONS** (조건 17건 — HIGH 5건 / MEDIUM-HIGH 1건 / MEDIUM 7건 / LOW-MEDIUM 1건 / LOW 1건 / Gap-N HIGH 4건 + MEDIUM-HIGH 1건)

### 8.2 핵심 사유

1. **Provider Liquidity 보존 강도 HIGH** — `rfc8785` + `jcs` 모두 Apache-2.0 + provider-neutral PyPI + 의존 0 + RFC 8785 IETF 표준 + 라이브러리 교체 비용 LOW (헌법 5조 비협상 충족)

2. **Hermes 의존 0 충족 HIGH** — 양 라이브러리 Requires=없음 → ADR-008 차단조건 #2 자동 충족, 본 PoC 자체가 *충족 검증 evidence* 산출

3. **Hermes 변조 차단 매트릭스 §2.12 #2 (filesystem 변조) HIGH cover** — hash chain (Layer 1) + canonical JSON 일관성 + sha256 결정적 검출 layer 강화

4. **단일 라이브러리 bug-class 회피** — `rfc8785` (Trail of Bits) + `jcs` (titusz) cross-check = 서로 다른 maintainer + 서로 다른 PyPI account + 서로 다른 API surface = 독립 구현 가정 정합 → 단일 supply chain 침해 시 BLOCK 자동 발화

5. **ADR-011 §2.4 T3 (자동 정책 변경 금지) 정합 HIGH** — chain violation 검출 시 자동 revert 0건 + manual review 강제 + `chain_violation_detected` entry 자동 작성 (T1 audit) ↔ chain 수정 (T3 BLOCK) 분리 정합

6. **5 영구 핵심 제약 5/5 HIGH 보호 적격** — Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리 모두 HIGH (단 (b) 격리 환경 PoC 는 Docker 격리 별도 권고 — C-B17)

### 8.3 조건 (17건 + Gap-N 5건)

본 의제 *Q1* 한정 머지 전 의무 조건 = **HIGH 5건 (C-B3, C-B4, C-B7, C-B8, C-B16)** + **Gap-N HIGH 4건 (#1, #2, #3, #4) §11 한계 흡수 + 별도 합의 영역 명시 의무**.

그 외 조건 = 본 PoC §9 escalation trigger 보강 / corpus 보강 / 별도 합의 영역.

### 8.4 격상 권한 부재 명시

본 분석은 **격상 권한 0건**:
- ❌ G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 권유
- ❌ ADR-012 본문 자동 갱신
- ❌ ADR-008 차단조건 #2 본문 변경
- ❌ 신규 `event` enum 추가
- ❌ 신규 정책 발명
- ❌ Q2 / Q3 본문 평가 (Q1 한정)
- ❌ 다른 Agent (A, C) 출력 참조
- ❌ Reviewer 합의 결과 예측

본 PoC = G4 *부분 충족 시제* 한정 (사양 §1.1 §1.2 + §8 답습). 본 분석 = Q1 한정 보안/거버넌스 검증가 입장. Reviewer 종합 합의 시점에 다른 Agent 입력 + 외부 LLM 의뢰 (C-B16) 결과 흡수 의무.

---

**작성 종료**: 2026-05-10
**Agent B 판정**: ✅ **APPROVE WITH CONDITIONS** (조건 17건 + Gap-N HIGH 4건 + MEDIUM-HIGH 1건)
**핵심 권고**: HIGH 조건 5건 (C-B3 / C-B4 / C-B7 / C-B8 / C-B16) 본 PoC 머지 전 의무 적용. Gap-N HIGH 4건 본 PoC §11 L-3 한계 흡수 + 별도 합의 영역 명시 의무.
