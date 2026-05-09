# Agent C — 대안/단순화 분석 (PR-2: ADR-012 신규 발행 + G4 §4.4/§4.6 hash chain 사양 보강)

**작성일**: 2026-05-09
**Agent 역할**: 대안/단순화 탐색 (Alternatives & Simplification)
**검토 범위**: P1 조건 C-C (Evidence Ledger 보호 강화) + C-G (G4 §4.4/§4.6 hash chain 사양 보강) — 통합 PR-2
**관점**: "더 나은 방법이 있는가? — ADR-012 별도 발행이 정당한가? 11 필드는 적정한가? RFC 8785 JCS 외 대안은? 더 단순한 보호 매커니즘?"
**금지 사항 답습** (사용자 명시): Hermes PMO 격상 / P2 v3 자동 채택 / ADR-008/009/010/011 본문 자동 갱신 / P2 v2 / system-identity-prequel archive 자동 처리 / 실 runtime code / migration script / Tier-2 / Tier-3 catalog 자동 확장 — 모두 본 분석 범위 외
**메타 명시**: 본 Agent C 도 메인 컨텍스트와 *동일 Claude 패밀리* 자기 작성 산출 — G3 §4 자기참조 차단의 적용 대상. 외부 LLM 1+ 의견으로 통제 가정.

---

## 0. 요약

본 Agent C 는 PR-2 의 *대안 합의 형태* 와 *단순화 가능성* 을 평가했다. 핵심 발견:

1. **ADR-012 별도 발행 (대안 A) 은 *조건부 정당*** — system-identity-prequel §6.4 가 이미 "Phase 1 종료 시 ADR-012 (Evidence Ledger Schema) 발행" 을 *예고* 하고 있으므로, 신규 ADR 번호 ADR-012 = *예고 답습*. 단, "Phase 1 종료 시" 트리거 미충족 (현 4 게이트 모두 *Design/Governance Gate PASS Bundled*, Implementation/Runtime PASS 미진입) → **트리거 시점 재해석 권고**: prequel §6.4 의 "Phase 1 종료" 가 *Phase 1 진입 후 운영 3~4주* 가 아닌 *4 게이트 Design/Governance PASS + 본 PR-1/PR-2 묶음 안정화 시점* 으로 재해석 필요.
2. **11 필드 중 11번째 필드 = `event` 권고** — 현 G4 §4.2 = 10 필드 (type / scope / id / schema_version / ts / agent / content / evidence_refs / prev_hash / hash). prequel §6.3 schema 도 10 필드 (event 포함, type/scope 미포함). **양쪽 모두 (event + type + scope) 통합 시 12 필드** 가 더 합리적이지만, 사용자 명시 11 필드 = `event` 추가가 단순화 우선. (a)/(c)/(d) 후보 (signature / chain_id / parent_event_id) 는 *후속 격상 영역*.
3. **RFC 8785 JCS 채택 = 옵션 1 권고** — 1인 개발자 메타-템플릿 스케일에서 IETF 표준 + 라이브러리 가용성 (Python `rfc8785`, JS `canonicalize` 등) 이 *자체 표준* 보다 *유지보수 비용* 낮음. 단, *전체 JCS 사양 인용* 보다 *사양 답습 + JCS 우선 호환 명시* 권고 (JCS lib 미존재 환경 fallback).
4. **Signed commit + git append commit *둘 중 하나 의무* (옵션 C, 사용자 명시) 적정** — 1인 개발자 + 동일 호스트 SPOF 현실에서 *둘 다 동시 의무* (옵션 D) 는 과잉. 단, **hash chain 은 *항상* 의무 + signed/append-commit 은 *둘 중 하나*** 명시 권고 (즉 *3 layer 중 hash + (signed | append-commit) = 2 layer 항상 충족*).
5. **PR-2 통합 묶음 정당** — C-C + C-G 동시 묶음은 *PR-1 6건 흡수 패턴* 답습. 분리 (PR-2a + PR-2b) 시 풀 3+1 *2배 비용*. **단, ADR-012 발행 자체는 *옵션 1 단축 합의 + 외부 LLM 1+* 도 가능** — 본 PR-2 의 *합의 형태* 는 사용자 결정 영역.
6. **영구 핵심 제약 5건 답습 *충분*** — Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / 자동 정책 변경 금지 (T3) / 수단/목적 분리. 본 PR-2 는 (a) Hermes ≠ root of trust 의 *Evidence Ledger 차원 보강* (Hermes 가 Evidence 생성 가능 *형식*, 그러나 forgery 차단 *형식 메커니즘* 추가) 으로 **답습 강화**.

**판정** (Agent C 단독, Reviewer 종합 대상):

```
APPROVE WITH CONDITIONS
```

PR-2 진행 적격이나, 다음 4 조건 권고:
(i) ADR-012 발행 트리거 = "prequel §6.4 Phase 1 종료" 재해석 명시 (현 시점 정당화)
(ii) 11번째 필드 = `event` 채택 (사용자 명시 후보 #1) + (a)~(d) 다른 후보는 *후속 격상 영역* 명시
(iii) RFC 8785 JCS *우선* 채택 + *사양 답습 + JCS 호환 명시* (전체 JCS 본문 ADR-012 인용 부담 회피)
(iv) hash chain *항상* 의무 + signed/append-commit *둘 중 하나* (3 layer 중 2 layer 항상 충족) 명시

---

## 1. PR-2 핵심 산출 6 항목 — 대안 비교

### 1.1 차원 1: ADR-012 별도 발행 vs 대안 (4 옵션)

| 옵션 | 정의 | 장점 | 단점 | 정당 시점 |
|-----|-----|-----|-----|---------|
| **대안 A** (사용자 명시) — ADR-012 별도 발행 | 신규 ADR-012 = "Evidence Ledger Protection Principle" 단독 발행 | (1) prequel §6.4 예고 답습 / (2) 본문 = Evidence Ledger 보호 *영구 권위* / (3) 후속 R-X / Phase X 작업의 *모법* 역할 가능 (ADR-011 R-4~R-7 패턴 답습) | (1) 트리거 = "Phase 1 종료" 미충족 — *재해석* 부담 / (2) ADR-012 인벤토리 한 번 발행 시 *간격* 대비 ADR-013 (G3 §4 자기참조 차단 영구화 후보, G2 §1.1 §9) / ADR-014 (Provider-agnostic Memory/Skill, G4 §0.2 #5) 와의 *순서 / 번호 충돌* 위험 | Evidence Ledger 보호 = *권위 영구화 필요* + 후속 작업 *모법 인용* 발생 시 |
| **대안 B** — ADR-008 부록 C (Evidence Ledger 부록) 추가 | ADR-008 본문에 부록 C *추가* (부록 B Amendment 패턴 답습) | (1) 새 ADR 번호 미발행 (충돌 회피) / (2) Hermes 도입 결정 ↔ Evidence 무결성 *한 ADR 묶음* — Hermes 도입 시 Evidence Ledger 가 *root of trust 외부 보강* 임을 명시 강화 | (1) ADR-008 = "Hermes 도입 결정" 본문 → 부록 C 가 *Evidence Ledger 일반 원칙* 을 담는 것은 *부록 형식 위반* (ADR-011 옵션 B 단점 답습 — "Amendment / 부록에 일반 원칙 = 비표준") / (2) 후속 작업이 ADR-008 부록 C 인용 시 *원본 ADR 본문 의도* 와 혼선 / (3) Hermes 도입 결정 = 차단조건 6 (비협상) 의 *수단* 차원, Evidence Ledger 보호 = *원칙* 차원 → *수준 mismatch* | Evidence Ledger 보호 영역이 *Hermes 도입 결정 specific 보강* 영역일 때만. **현 PR-2 범위는 *일반 원칙* → 대안 B 부적절** |
| **대안 C** — G3 §1.3 + §5.3 본문 보강 단독 | G3 본문 (Evidence-based PASS 5 운영 규칙) 에 hash chain + 11 필드 추가, 신규 ADR 미발행 | (1) 새 ADR 0건 / (2) 의사결정 비용 최소 / (3) ADR-011 §2.4 답습 외 새 권위 0건 (사용자 명시 답습 강화) | (1) G3 = "Hermes ≠ root of trust runtime" *runtime 측면* 본문 → Evidence Ledger 보호 = *형식 / 무결성* 측면 ≠ runtime 권한 → **G3 본문 _범위 초과_** / (2) Evidence Ledger 보호가 *G3 가 PASS / DRAFT 변경 시 자동 변경* 위험 (ADR 권위 부재) / (3) prequel §6.4 "ADR-012 발행" 예고 답습 미충족 | Evidence Ledger 가 *G3 runtime 강제* 영역 한정일 때만. 영구 권위 미필요 시 |
| **대안 D** — G4 §4.4 / §4.6 본문 보강 + 신규 ADR 미발행 | G4 hash chain *형식 사양* 만 보강, ADR-012 발행 안 함 | (1) 새 ADR 0건 / (2) G4 = *형식 / schema* 차원이라 §4.4 보강이 *자연스러움* | (1) G4 = DRAFT 상태 (Design/Governance Gate PASS Bundled, 정식 채택 미완) → **G4 *DRAFT* 가 Evidence Ledger 보호의 _영구 권위_ 가 되는 것은 _권위 mismatch_** / (2) G4 변경 시 (수정 / 폐기 가능성) Evidence Ledger 보호도 동시 변경 → 권위 안정성 부족 / (3) prequel §6.4 ADR-012 예고 답습 미충족 | G4 가 *PASS* + *영구 권위 안정* 시점에만. 현 시점 부적절 |

**Agent C 평가**:
- **대안 A 가 *유일하게* 영구 권위 + prequel 예고 답습 + 후속 작업 모법 인용 가능** — 사용자 명시 옵션 정당.
- 단, 대안 A 의 *단점 #1 (트리거 재해석)* 은 본 PR-2 합의 보고서 §X 명시 필요 — "Phase 1 종료" 가 *4 게이트 Design/Governance PASS + PR-1/PR-2 묶음 안정화 시점* 으로 재해석 (또는 prequel §6.4 본문 자체 갱신 — 별도 합의 영역).
- 대안 A 의 *단점 #2 (ADR 번호 순서)* 는 ADR-012 / ADR-013 / ADR-014 후보 *우선순위 결정* 별도 합의 영역 (g2g3g4 Agent C §4.3 답습).

### 1.2 차원 2: 11 필드 vs 단순화 후보

**현 G4 §4.2 schema = 10 필드**: type / scope / id / schema_version / ts / agent / content / evidence_refs / prev_hash / hash
**현 prequel §6.3 schema = 10 필드** (다른 조합): ts / task_id / event / agent / result / ref / summary / evidence_md / prev_hash / hash

**겹침 분석**: 양쪽 합집합 = 16 필드, 교집합 = 4 필드 (ts / agent / prev_hash / hash). 즉 **G4 와 prequel schema 가 *비대칭 정의***.

| 11번째 필드 후보 | 단순성 | 무결성 강화 | Provider Liquidity | 1인 개발자 비용 | 권고 우선순위 |
|------------|------|-------|------|---------|------|
| **(a) `event`** (memory_write / skill_promotion / roundtrip_lossy / gate_pass / external_llm_received / evidence_forgery_detected) | ✅ 단순 (string enum) | ✅ 강 (이벤트 분류 = forgery 검출 핵심) | 0 (provider 무관) | 0 (string enum 추가만) | **#1 (사용자 명시 후보) 권고** |
| (b) `signature` (signed commit signature 또는 GPG/SSH 서명) | 🟡 중간 (서명 도구 필요) | ✅✅ 매우 강 (signed = forgery 차단의 *암호적* 근거) | 0 | 🟡 GPG/SSH 키 관리 + 서명 자동화 필요 | **#3 후속 격상 영역** |
| (c) `chain_id` (다중 chain 분리 — Memory/Skill/Gate 별도 chain) | ⚠️ 복잡 (chain 관리 다중화) | 부분 강 (chain isolation) | 0 | ⚠️ chain enumeration 합의 + 관리 비용 ↑ | **#4 후속 격상 영역** (Tier-2/3 catalog 확장과 연동, 본 PR-2 범위 외) |
| (d) `parent_event_id` (event 간 cross-reference) | 🟡 중간 (id 관리) | 🟡 중간 (cross-reference forgery 검출) | 0 | 🟡 id management 부담 | **#5 후속 격상 영역** |
| (e) 추가 안 함 (10 필드 유지, hash chain 만 강화) | ✅ 가장 단순 | 부분 강 (chain only) | 0 | 0 | **#2 차순위 — 사용자 명시 결정 시 정당** |

**Agent C 권고**:
1. **(a) `event` 채택** = 사용자 명시 #1 후보. 이유:
   - prequel §6.3 schema 에 `event` 가 *이미 존재* → G4 §4.2 도입은 prequel 답습 + schema 통합
   - forgery 검출의 *분류 차원* 핵심 (`evidence_forgery_detected` 자체가 한 event type)
   - 1인 개발자 비용 0 (string enum 추가만)
2. **다른 (b)/(c)/(d) 후보는 *후속 격상 영역*** — 본 PR-2 범위 외. ADR-012 본문에 *후속 진입 사양 예고* 한정 (G4 §2.3/§2.4 Session/Team Memory 패턴 답습).
3. **단, *G4 §4.2 + prequel §6.3 schema 통합 매트릭스*** 명시 권고 — 양쪽이 비대칭 정의이므로, 본 PR-2 가 prequel §6.3 답습이라면 G4 §4.2 *를* 통합 schema 로 *갱신* (즉 G4 §4.2 → 11 필드 = G4 10 + `event`).
4. **분량 트레이드오프 — 13 / 9 / 7 필드 검토**:
   - **13 필드**: 11 + (b) signature + (d) parent_event_id 동시 추가 → 1인 개발자 *비용 격증* (서명 자동화 + id management). **부적절**.
   - **9 필드**: 10 - (`agent` 또는 `evidence_refs` 제거) → forgery 검출 약화 + 출처 추적 손실. **부적절**.
   - **7 필드**: 미니멀 — type / id / ts / content / hash / prev_hash + 1 차원만. **PoC 차원 정당하나 ADR-012 권위 본문에는 부적절**.
   - **11 필드 = 적정 균형점**. 사용자 명시 결정 답습.

### 1.3 차원 3: Canonical JSON 표준 채택

| 옵션 | 정의 | 장점 | 단점 | 1인 개발자 적합성 |
|-----|-----|-----|-----|--------|
| **옵션 1** — RFC 8785 JCS 정식 인용 (사용자 명시 후보 #1) | RFC 8785 JSON Canonicalization Scheme 인용 + 라이브러리 의존 | (1) IETF 표준 / (2) Python `rfc8785` / JS `canonicalize` / Go 라이브러리 가용 / (3) cross-language 호환 / (4) JCS = ECDSA + Ed25519 등 서명 표준과 정렬 | (1) lib 의존성 (1 dep) / (2) JCS 본문 = 11 페이지 RFC, 본 ADR-012 인용 시 본문 부담 | **권고** ✅ — 외부 lib 1 dep 비용 ≪ 자체 표준 유지보수 비용 |
| 옵션 2 — 현 G4 §4.4 단순 정의 유지 (lex sort + RFC 8259) | 현 G4 §4.4 4 항목 (key 정렬 lex / whitespace separator / numeric 정규화 / RFC 8259 escape) 유지 | (1) 외부 lib 0 / (2) 사양 단순 (4 줄) | (1) edge case 미커버 (NaN / Infinity / 큰 정수 / 유니코드 정규화 NFC 등) / (2) cross-language 호환 *사용자 책임* / (3) 향후 *발견된 edge case* 마다 G4 §4.4 갱신 부담 | 부적절 — *사용자 책임* = 1인 개발자에게 *최악*. JCS lib 의존이 더 단순 |
| 옵션 3 — JCS 외 단순 자체 표준 (DigitalBazaar canonicalize-json / Olivine Labs JCS / 기타) | 비-IETF 자체 표준 인용 | (1) 일부는 lib 가용 / (2) JCS 보다 단순한 사양 가능 | (1) IETF 표준 미아님 → 호환성 보장 약 / (2) maintenance 책임 *원작자* / (3) JCS 도입 후 *재인용* 시 비용 발생 | 부적절 — JCS 가 *기존 산업 표준* |
| 옵션 4 — Cryptographic JSON (CJSON) | 비주류 표준 | (1) hash 안정성 보강 가능 | (1) 비주류 = lib 부족 / (2) JCS 와 sub-set 관계 불명확 | 부적절 — JCS 우선 |

**Agent C 권고 — 옵션 1 (RFC 8785 JCS) + 사양 답습 명시**:

```
ADR-012 §X (Canonical JSON):
- 본 §X 는 RFC 8785 JCS 채택을 권고한다.
- ADR-012 본문은 JCS 사양 *전체* 를 인용하지 않으며, RFC 8785 reference 만 제시한다.
- 구현 시 라이브러리 우선순위:
  (1) Python: `rfc8785` (PyPI)
  (2) JS / TS: `canonicalize` (npm)
  (3) Go: `github.com/cyberphone/json-canonicalization`
  (4) 기타: RFC 8785 §3 사양 직접 구현
- JCS lib 미존재 환경 fallback: 현 G4 §4.4 4 항목 (lex sort + whitespace separator + numeric 정규화 + RFC 8259 escape) 적용 + ledger entry `event: canonical_json_fallback` 기록 (사용자 alert)
```

**근거**: 1인 개발자 + 메타-템플릿 스케일에서 *외부 lib 1 dep 비용 ≪ 자체 표준 maintenance 비용*. JCS = IETF RFC 8785 (April 2020 standard track) + multi-language 지원. Fallback 명시로 *환경 의존* 미스 회피.

### 1.4 차원 4: Signed commit vs Git append commit vs 둘 다

| 옵션 | 정의 | 강도 | 1인 개발자 비용 | SPOF 통제 | 권고 |
|-----|-----|----|------|------|----|
| 옵션 A — signed commit 단독 의무 | GPG / SSH 서명 commit 만 | 강 (암호적 근거) | 🟡 GPG 키 관리 + 자동화 | 부분 강 — 동일 호스트 키 노출 시 SPOF | 부적절 (signed 단독 = SPOF) |
| 옵션 B — git append commit 단독 의무 | append-only branch + history rewrite 차단 | 부분 강 (git history 의존) | ✅ 0 (git 자체 기능) | 부분 약 — `git push --force` / `git filter-branch` 가능 | 부적절 (append 단독 = local rewrite 가능) |
| **옵션 C** (사용자 명시 후보) — 둘 중 하나 의무 | hash chain + (signed | append-commit) | 강 + flexibility | 🟡 중간 (선택지 부담) | 강 — 2 layer 중 1 layer 만 강제 시 SPOF 한 부분 통제 | **권고** ✅ — *둘 중 하나* 명시 |
| 옵션 D — 둘 다 동시 의무 | hash chain + signed + append-commit (3 layer 모두) | 매우 강 | 🔴 GPG 키 + append branch + 자동화 동시 | 강 | **부적절** — 1인 개발자 + 메타-템플릿 = 과잉 (YAGNI 위반) |
| 옵션 E — hash chain + signed 전용 (또는 보조) | hash chain *항상* + signed *옵션* | 중간 | 0 (signed 옵션) | 부분 약 (signed 미적용 시 hash chain only) | 부적절 — append-commit 미명시 시 *git history rewrite* 위험 |

**Agent C 권고 — 옵션 C 정당, 단 *3 layer 중 2 layer 항상 충족* 명시 보강**:

```
ADR-012 §X (변조 방지):
1. **Layer 1 — Hash Chain (항상 의무)**:
   - 모든 entry 는 prev_hash + hash (canonical JSON sha256) 필수
   - genesis_hash = sha256("genesis:<scope>:<schema_version>")
   - prev_hash 검증 실패 시 = 변조 또는 손실 → 사용자 alert + ledger event "hash_chain_break"

2. **Layer 2 — Signed Commit OR Git Append Commit (둘 중 하나 의무)**:
   - **옵션 2A** — signed commit: GPG 또는 SSH 서명 (`git commit -S`). signature 검증 자동화 의무.
   - **옵션 2B** — git append commit: append-only branch (`evidence/*`) + branch protection (history rewrite 차단)
   - 사용자는 PR-2 채택 시점에 옵션 2A 또는 2B 명시 결정 (명시 미결정 시 옵션 2A 기본값)

3. **Layer 3 (후속 격상 영역, 본 PR-2 범위 외)**:
   - signed + append-commit *동시* 의무 (옵션 D 패턴) — Phase 2 + Tier-3 catalog 확장 시점에 진입 검토
```

**근거**: hash chain = *형식* 차원 항상 의무 (G4 §4.4 답습). signed | append-commit = *git history* 차원 *둘 중 하나* (사용자 명시 결정). 옵션 D *둘 다* 는 1인 개발자 비용 ↑↑ + YAGNI 위반.

### 1.5 차원 5: Round-trip Lossy 검출의 단순화

**현 G4 §4.6 = hash 일치 OR 의미 보존** (사용자 review 시 손실 허용 ledger entry `event: roundtrip_lossy`).

| 옵션 | 정의 | 장점 | 단점 | 권고 |
|-----|-----|-----|-----|----|
| (a) hash 일치 *only* (strict) | 의미 보존 미허용. round-trip lossy = FAIL | (1) 결정적 / (2) 자동화 단순 | (1) Hermes ↔ Claude/OpenAI/Ollama 변환 시 *형식 차이* (예: yaml ↔ json key 순서) → 자동 hash 일치 *불가능* / (2) 모든 변환 = FAIL → 정상 운영 불가 | **부적절** — 변환 형식 차이 = 정상 |
| (b) 의미 보존 *only* | hash 검증 없이 사용자 review | (1) 변환 자유 | (1) 자동화 0 / (2) forgery 위험 ↑↑ | **부적절** — 자동화 부재 |
| (c) tier-별 (T2 = hash 일치 / T3 = 의미 보존) | T 분류 별 다른 검증 | (1) 차원 분리 | (1) tier 정의 부담 (Tier-2/3 catalog 확장 = PR-2 범위 외) / (2) 2026-05-09 시점 Tier 정의 미확정 | **부적절** — 본 PR-2 범위 외 |
| **(d) 현 *OR* 유지 + 정제** (사용자 명시 후보) | hash 일치 OR 의미 보존 + 손실 영역 ledger entry 의무 | (1) hash 일치 *기본 자동* / (2) 의미 보존 fallback / (3) ledger entry 의무 = forgery 견제 | (1) "의미 보존" 사용자 review 의무 — *주관적 판정* 영역 / (2) ledger entry 정의 *형식 정련* 필요 | **권고** ✅ |

**Agent C 권고 — (d) 정제**:

```
ADR-012 §X (Round-trip 검증):
1. 1차 검증: canonical JSON sha256 일치 (자동, 결정적)
   - 일치 시 = round-trip PASS (자동 ledger entry "roundtrip_pass")
2. 2차 검증 (1차 실패 시): 의미 보존 review (사용자 명시)
   - PASS 시 = round-trip lossy with semantic preservation (ledger entry "roundtrip_lossy" + 손실 영역 명시)
   - FAIL 시 = round-trip FAIL (ledger entry "roundtrip_fail" + 사용자 alert)
3. ledger entry 형식:
   - `event: roundtrip_pass | roundtrip_lossy | roundtrip_fail`
   - `lossy_fields: [<field_name>, ...]` (lossy 일 때 명시)
   - `semantic_preservation_review: <user_id + ts>` (사용자 review 시점)
```

**migration script 미작성 시점 PoC 의무성 평가**: 본 PR-2 범위에서 *PoC 의무 미강제* — migration script 자체가 G4 §0.2 #8 답습으로 본 초안 외 영역. ADR-012 본문에 *사양만* 명시 + Implementation/Runtime PASS 시점 PoC 의무 (별도 합의).

### 1.6 차원 6: PR-2 범위 축소 후보 (C-C + C-G 통합 vs 분리)

| 옵션 | 정의 | PR-1 6건 흡수 패턴 답습 | 합의 비용 | 권고 |
|-----|-----|------|------|----|
| **PR-2 통합 (현 사용자 명시)** — C-C (ADR-012) + C-G (G4 §4.4/§4.6) 동시 묶음 | 풀 3+1 1회 | ✅ PR-1 6건 흡수 패턴 답습 | 풀 3+1 × 1 + 외부 LLM 1+ × 1 | **권고** ✅ |
| 분리 — PR-2a (ADR-012 만) + PR-2b (G4 §4.4/§4.6 만) | 풀 3+1 2회 | ❌ — PR-1 패턴과 비대칭 | 풀 3+1 × 2 + 외부 LLM 1+ × 2 | 부적절 — 2배 비용 + ADR-012 ↔ G4 *cross-reference* 비대칭 누락 위험 |
| 통합 + P2 v3 정식 채택 동시 | PR-2 범위 확대 | ⚠️ — 사용자 명시 결정 외 영역 | 풀 3+1 × 1 (확대) | 부적절 — 사용자 명시 *PR-2 범위* 외 (P2 v3 정식 채택은 별도 결정) |

**Agent C 권고 — 통합 묶음 정당**. 분리 시 (a) ADR-012 본문이 G4 §4.4 *현 정의* 를 참조 → G4 §4.4 보강 시점 ADR-012 *재갱신* 발생, (b) 2배 합의 비용. 통합이 *cross-reference 동시 명시* + *PR-1 패턴 답습* 측면 우월.

### 1.7 차원 7: Provider Liquidity / Hermes ≠ root of trust 보호 측면 단순화

**영구 핵심 제약 5건** (G4 §9 답습):
1. Provider Liquidity (헌법 5조)
2. Hermes ≠ root of trust (ADR-011 §2.3)
3. 메타포 강제 금지 (prequel §7)
4. 자동 정책 변경 금지 T3 (ADR-011 §2.4)
5. 수단/목적 분리 (ADR-011 §2.1)

| 제약 | 본 PR-2 보호 위치 | 답습 강도 | 과잉/부족 평가 |
|-----|----------|----|----------|
| 1. Provider Liquidity | ADR-012 §X (canonical JSON = JCS = vendor-neutral) + Hermes 의존 0 (G4 §4.3 답습) | 답습 (강) | 적정 — JCS = IETF 표준 = vendor-neutral |
| 2. **Hermes ≠ root of trust** | ADR-012 §X (Evidence Ledger forgery 차단 = Hermes 가 entry 생성 가능, 그러나 hash chain + signed/append = forgery 검출) | **답습 강화** | **적정** — Hermes 가 Evidence 생성 *가능* 하지만 *변조 불가* = root of trust 외부 보강 |
| 3. 메타포 강제 금지 | (해당 없음 — Evidence Ledger 영역) | — | 해당 없음 |
| 4. 자동 정책 변경 금지 (T3) | ADR-012 §X (ADR / Constitution / Harness Gate 변경 시 ledger entry 의무 — `event: policy_change_attempted`) | 답습 보강 | 적정 — T3 위반 시도의 *ledger 기록 의무* = automatic detection 강화 |
| 5. 수단/목적 분리 | ADR-012 §X (목적 = Evidence 무결성, 수단 = hash chain + signed | append-commit) | 답습 (a)~(d) 4 조건 + (e) 합의 패턴 | 적정 — 수단 (JCS / signed / append) 변경 시 (a)~(d) 4 조건 적용 |

**Agent C 권고 — ADR-011 §2.1 (a)~(d) 4 조건 + (e) 합의 APPROVE 5 조건 답습 강도**:

| 답습 강도 | 적용 영역 |
|------|------|
| 전체 5 조건 | ADR-012 본문 *수단 변경 절차* 차원 — (a) 동등 보안 결과 / (b) 격리 PoC / (c) ADR 권위 / (d) CI 회귀 / (e) 합의 APPROVE |
| 부분 (4 조건만) | 부적절 — (e) 합의 APPROVE 누락 시 권위 안정성 약 |
| 없음 | 부적절 — ADR-011 모법 답습 안 됨 |

**권고**: ADR-012 §X (변경 절차) = ADR-011 §2.1 (a)~(d) + (e) 5 조건 답습. *수단 변경* (예: JCS → 자체 표준) 시 5 조건 모두 충족 의무.

### 1.8 차원 8: 외부 LLM 추가 의견의 적정성

**G3 §4.4.2 답습**: 자기 작성 산출 검증 시 외부 LLM 1+ 의견 = *권장* (현 시점) → *필수* (Hermes PMO 격상 통합 합의 시점).

| 본 PR-2 합의 형태 | 외부 LLM 1+ 의견 | 정당화 |
|-----|-----|-----|
| 풀 3+1 + 외부 LLM 1+ 권장 | ✅ 권장 | g2g3g4 옵션 3 패턴 답습 |
| 풀 3+1 + 외부 LLM 1+ 필수 | ✅ 필수 | ADR-012 = *영구 권위 발행* + Evidence Ledger = *forgery 검출 핵심* → 필수 격상 정당 |
| 풀 3+1 + 외부 LLM 미요청 | 부적절 | 자기참조 한계 통제 부족 |

**Agent C 권고 — 외부 LLM 1+ *필수* 격상**:

근거:
1. ADR-012 = *영구 권위 ADR* (R-X 모법 가능)
2. Evidence Ledger = *forgery 검출* = *root of trust 외부 보강* 핵심
3. 자기참조 위험: 본 PR-2 = 동일 Claude 컨텍스트 (Agent A/B/C + Reviewer) → 외부 LLM 1+ 필수 통제

**Cross-vendor 추가 (Gemini 등) 시점**:
- P2 v3 정식 채택 진입 *전* (사용자 결정 3 답습) — 사용자 명시 결정 영역
- 본 PR-2 시점 = 외부 LLM 1+ 호출 (gpt-4 또는 gemini 또는 다른 vendor 단일) 으로 *충분*
- cross-vendor *복수* 호출 (gpt-4 + gemini 동시) = P2 v3 정식 채택 시점 격상 영역

---

## 2. 8 차원 평가 요약 매트릭스

| 차원 | 사용자 명시 옵션 | Agent C 평가 | 권고 |
|-----|---------|--------|----|
| 1. ADR-012 별도 발행 vs 대안 | 대안 A (별도 발행) | ✅ 정당 (조건부) | 트리거 재해석 명시 |
| 2. 11 필드 vs 단순화 | 11 필드 (event 추가) | ✅ 적정 균형 | (a) `event` 채택 + (b)/(c)/(d) 후속 격상 |
| 3. Canonical JSON 표준 | 옵션 1 (RFC 8785 JCS) | ✅ 적정 | JCS *우선* + fallback (G4 §4.4) 명시 |
| 4. Signed vs Append vs 둘 다 | 옵션 C (둘 중 하나) | ✅ 적정 | hash chain *항상* + signed | append *둘 중 하나* 명시 |
| 5. Round-trip lossy 검출 | 옵션 (d) (현 *OR* 유지) | ✅ 적정 | ledger entry 형식 정련 |
| 6. PR-2 범위 축소 | 통합 (C-C + C-G) | ✅ 정당 | PR-1 6건 흡수 패턴 답습 |
| 7. 영구 5 제약 보호 | (사용자 명시 미세분화) | ✅ 답습 강화 | ADR-011 (a)~(e) 5 조건 답습 |
| 8. 외부 LLM 추가 의견 | (사용자 명시 미세분화) | ⚠️ *권장 → 필수* 격상 권고 | 필수 격상 (영구 권위 ADR 발행 사유) |

**8 차원 통합 평가**: 사용자 명시 옵션 = *7/8 차원 정당 + 1/8 차원 (8번 외부 LLM 권장 → 필수) 격상 권고*.

---

## 3. 단순화 / 대안 권고 (Alt-N enumeration)

### Alt-1 (권고 채택, 사용자 명시 답습)

- ADR-012 별도 발행 + G4 §4.4/§4.6 보강 동시 묶음 (PR-2 통합)
- 11 필드 (10 + `event`)
- RFC 8785 JCS *우선* + G4 §4.4 fallback
- hash chain 항상 + signed | append-commit 둘 중 하나
- 풀 3+1 + 외부 LLM 1+ **필수**

### Alt-2 (대안, 사용자 결정 시 정당)

- 본 PR-2 범위 동일하나 **단축 합의 (Reviewer-only) + 외부 LLM 1+ 필수** 형태
- 정당 사유: ADR-012 본문 = prequel §6.4 + system-identity-prequel §6.3 + G4 §4.4 답습 → *새 권위 결정* = "11번째 필드 = event" 한정. 단축 합의 적격성 가능
- 단점: ADR-012 = 영구 권위 ADR → 풀 3+1 의 *권위 강화* 효과 손실

### Alt-3 (대안, 부분 PASS)

- ADR-012 발행 *우선* (풀 3+1) → G4 §4.4/§4.6 보강 *후속* (단축 합의)
- 정당 사유: ADR-012 = 영구 권위 우선 발행 + G4 §4.4 = 사양 보강 (cross-reference 답습 가능)
- 단점: 2 합의 (1 풀 + 1 단축). 합의 비용 1.3배. cross-reference 누락 위험

### Alt-4 (대안, 보류)

- PR-2 *발생 보류* + Evidence Ledger PoC 우선 (실 hash chain + signed commit + canonical JSON 자동화 PoC)
- 정당 사유: PoC 후 ADR-012 *evidence-driven* 발행 → 권위 강화
- 단점: PoC 작성 비용 + 진행 지연. PR-1 6건 흡수 패턴 답습 안 됨 (PR 묶음 일관성 손실)

**Agent C 권고**: **Alt-1 (사용자 명시 답습)** + 차원 8 외부 LLM *필수 격상*. Alt-2 / Alt-3 / Alt-4 모두 사용자 결정 시 정당하나, *비용 대비 효과* 측면 Alt-1 우월.

---

## 4. 권고 조건

### 4.1 권고 조건 enumeration (Alt-1 채택 시)

| # | 조건 | 처리 시점 |
|---|----|------|
| C-1 | ADR-012 발행 트리거 = "prequel §6.4 Phase 1 종료" 재해석 명시 | 본 PR-2 합의 보고서 §X |
| C-2 | 11번째 필드 = `event` enum 정의 (memory_write / skill_promotion / roundtrip_lossy / gate_pass / external_llm_received / evidence_forgery_detected / canonical_json_fallback / hash_chain_break / policy_change_attempted / roundtrip_pass / roundtrip_lossy / roundtrip_fail) — **12 enum 후보** | ADR-012 §X (enum 본문) |
| C-3 | RFC 8785 JCS *우선* + G4 §4.4 4 항목 fallback 명시 + lib 3 가지 (Python/JS/Go) reference | ADR-012 §X (canonical JSON) |
| C-4 | hash chain *항상* + signed | append-commit *둘 중 하나* + 사용자 PR-2 채택 시점 명시 결정 (signed 또는 append 기본값) | ADR-012 §X (변조 방지) |
| C-5 | round-trip 1차 (hash 일치) + 2차 (의미 보존) + ledger entry 3 형식 (`roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail`) | ADR-012 §X (round-trip 검증) + G4 §4.6 보강 |
| C-6 | ADR-011 §2.1 (a)~(d) + (e) 합의 APPROVE 5 조건 답습 (*수단 변경 절차*) | ADR-012 §X (변경 절차) |
| C-7 | 외부 LLM 1+ *필수* (영구 권위 ADR 발행 사유) | 본 PR-2 합의 절차 |
| C-8 | G4 §4.2 schema → 11 필드 갱신 (10 + `event`) + prequel §6.3 schema 와의 *통합 매트릭스* 명시 | G4 §4.2 보강 + ADR-012 cross-reference |
| C-9 | (b) signature / (c) chain_id / (d) parent_event_id = *후속 격상 영역* 명시 (ADR-012 §X 본문에 후속 진입 사양 *예고만*) | ADR-012 §X (후속 진입) |
| C-10 | ADR-013 (G3 §4 자기참조 차단 영구화) / ADR-014 (Provider-agnostic Memory/Skill) 후보와의 *번호 충돌* 사용자 명시 결정 | 본 PR-2 시점 또는 후속 별도 |

### 4.2 권고 조건 — 추가 사용자 결정 영역

- **D-1**: signed commit (옵션 2A) 또는 git append commit (옵션 2B) 기본값 결정 — 사용자 명시
- **D-2**: 외부 LLM 1+ 호출 vendor (gpt-4 / gemini / 기타) 결정 — 사용자 명시
- **D-3**: ADR-012 / 013 / 014 우선순위 + 동시/순차 발행 결정 — 사용자 명시 (g2g3g4 Agent C §4.3 답습)

---

## 5. 영구 핵심 제약 5건 본 PR-2 답습 충분성 평가

| # | 제약 | 본 PR-2 답습 위치 | 강도 | 평가 |
|---|----|------|----|----|
| 1 | Provider Liquidity (헌법 5조) | ADR-012 §X (JCS = vendor-neutral) + G4 §4.3 답습 (Hermes 의존 0) | 강 | ✅ 충분 |
| 2 | **Hermes ≠ root of trust** (ADR-011 §2.3) | ADR-012 §X (Evidence forgery 차단 = Hermes 가 entry 생성 가능, 변조 불가) | **강 (답습 강화)** | ✅ **충분 + 강화** |
| 3 | 메타포 강제 금지 (prequel §7) | (해당 없음 — Evidence Ledger 영역) | — | ✅ 무관 |
| 4 | 자동 정책 변경 금지 T3 (ADR-011 §2.4) | ADR-012 §X (T3 위반 시도 ledger entry 의무 — `event: policy_change_attempted`) | 보강 | ✅ 충분 + 보강 |
| 5 | 수단/목적 분리 (ADR-011 §2.1) | ADR-012 §X (목적 = Evidence 무결성, 수단 = hash chain + signed | append) + (a)~(e) 5 조건 답습 | 강 (답습) | ✅ 충분 |

**Agent C 평가**: **5건 모두 답습 충분 + 2건 (#2 / #4) 보강**. 본 PR-2 가 영구 핵심 제약 5건 중 *어느 하나도 약화하지 않으며*, **Hermes ≠ root of trust** 와 **자동 정책 변경 금지 T3** 의 *Evidence Ledger 차원 답습 강화* 효과 명시.

---

## 6. 본 입력이 *하지 않는* 것

본 Agent C 분석은 다음을 *발생시키지 않으며* 발생 권한 없음:

- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 자동
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
- ❌ P2 v2 (`hermes-adoption-design.md`) 자동 archive
- ❌ system-identity-prequel.md 자동 archive
- ❌ 실 runtime code 작성 (hash chain 검증 / canonical JSON / signed commit 자동화 등)
- ❌ migration script 작성 (`scripts/hermes-migration/*.py`)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ ADR-012 본문 자체 작성 (본 분석 = *권고 사양*까지, 본문 작성은 Reviewer 종합 + 사용자 결정 후 별도)
- ❌ G4 §4.2 / §4.4 / §4.6 본문 자동 갱신 (보강 *권고 사양*까지, 본문 변경은 PR-2 합의 통과 후)
- ❌ Reviewer 종합 *대체* (본 입력 = Agent C 단독, Reviewer 종합 입력 한정)
- ❌ PR-2 합의 형태 (풀 3+1 vs 단축) 자동 결정 (사용자 명시 결정 영역)
- ❌ 다른 Agent (A, B) 출력 참조 (본 입력 = 동시 독립 분석 패턴 답습)
- ❌ 외부 LLM 1+ 의견 자동 호출 (외부 LLM 호출은 사용자 명시 결정 영역)
- ❌ ADR-013 / ADR-014 후보 자동 발행 결정
- ❌ 메타포 강제

본 Agent C 판정 (APPROVE WITH CONDITIONS) 은 *오직* "Alt-1 (사용자 명시 옵션) 진행 적격 + 4 조건 권고" 의미. 다른 Agent / Reviewer / 사용자 결정 *우선*.

---

## 7. 최종 판정

### 7.1 판정

```
APPROVE WITH CONDITIONS
```

### 7.2 권장 합의 형태

**Alt-1 (사용자 명시 답습)** — PR-2 통합 (C-C + C-G) + 풀 3+1 + 외부 LLM 1+ **필수**, 다음 4 조건 충족 시:

1. **C-1 (트리거 재해석)**: ADR-012 발행 트리거 = "prequel §6.4 Phase 1 종료" 를 *4 게이트 Design/Governance PASS + PR-1/PR-2 묶음 안정화 시점* 으로 재해석 명시 (본 PR-2 합의 보고서 §X 또는 prequel §6.4 본문 갱신 — 별도 합의 영역).
2. **C-3 (JCS + fallback)**: RFC 8785 JCS 정식 인용 + G4 §4.4 4 항목 fallback 명시 + Python `rfc8785` / JS `canonicalize` / Go `cyberphone/json-canonicalization` 3 lib reference.
3. **C-4 (3 layer 명시)**: hash chain *항상* 의무 + signed | append-commit *둘 중 하나* (사용자 PR-2 채택 시점 명시 결정 D-1) + 둘 다 동시 의무 (옵션 D) = *후속 격상 영역* 명시.
4. **C-7 (외부 LLM 필수 격상)**: 본 PR-2 = 영구 권위 ADR 발행 + Evidence Ledger forgery 차단 핵심 → 외부 LLM 1+ *권장 → 필수* 격상 (사용자 결정 D-2).

### 7.3 대안 (사용자 결정 시 정당)

- **Alt-2 정당**: 단축 합의 (Reviewer-only) + 외부 LLM 1+ 필수. ADR-012 *권위 강화 효과 손실* 단점 인지 시.
- **Alt-3 정당**: ADR-012 우선 (풀) + G4 §4.4/§4.6 후속 (단축). 2 합의 비용 + cross-reference 누락 위험 인지 시.
- **Alt-4 정당**: 보류 + Evidence Ledger PoC 우선. PR-1 패턴 답습 손실 + 진행 지연 인지 시.

### 7.4 BLOCK 사유 부재

다음 사유로 BLOCK 권고 *하지 않음*:
- 사용자 명시 옵션 = 7/8 차원 정당 + 1/8 차원 (외부 LLM 격상) 권고
- 영구 핵심 제약 5건 모두 답습 충분 + 2건 (#2 / #4) 보강
- prequel §6.4 ADR-012 발행 예고 답습 (트리거 재해석 한정)
- 11 필드 = 적정 균형 (사용자 명시)
- RFC 8785 JCS = IETF 표준 + lib 가용 (1인 개발자 적합)
- Hash chain + signed | append-commit *둘 중 하나* = SPOF 통제 + 1인 개발자 비용 관리

---

## 8. 본 Agent C 분석의 메타 편향 자기진단

본 Agent C 분석은 다음 5 통제 답습:

1. **사용자 명시 절차 답습**: Hermes PMO 격상 / P2 v3 자동 채택 / ADR-008/009/010/011 본문 자동 갱신 / archive / 실 runtime 코드 / migration script / Tier-2/3 catalog 자동 확장 모두 본 분석 *범위 외* 명시.
2. **다른 Agent (A/B) 출력 미참조**: 본 분석은 G4 §3 / §4 / §6 / §11 + ADR-011 + ADR-008 + ADR-000 template + system-identity-prequel §6.3 + 2026-05-09 g2g3g4 Agent C 보고서만 참조. Agent A/B 출력 본 분석 시점 *부재* (병렬 독립 분석 패턴 답습).
3. **자기참조 한계 명시**: 본 분석 자체가 동일 Claude 패밀리 컨텍스트 — Reviewer 종합 + 외부 LLM 1+ *필수* 권고 (§7.2 C-7) 로 통제.
4. **APPROVE WITH CONDITIONS 판정의 *조건* 명시**: 4 조건 (C-1 트리거 재해석 / C-3 JCS + fallback / C-4 3 layer / C-7 외부 LLM 필수) + 보조 조건 (C-2 / C-5 / C-6 / C-8 / C-9 / C-10) 모두 *후속 합의 또는 사용자 결정* 영역.
5. **본 분석이 *하지 않는* 것 명시 (§6)**: 14건 명시 부정.

본 5 통제는 g2g3g4 Agent C 보고서 5 통제 + PR-1 6건 흡수 5 통제 답습 — PR-1 → PR-2 → 후속 합의 동일 패턴 유지.

### 8.1 본 분석의 한계

- 본 Agent C 분석은 *Claude Opus 4.7 (1M context)* 단독 — 외부 LLM 의견 없음. *대안 탐색* 의 범위가 본 모델의 시야 한정.
- 본 분석은 *DRAFT 본문 + ADR 권위 본문 기반* — 실 hash chain / signed commit / canonical JSON PoC 미수행 → *실제 구현 시 발견 가능 edge case* 평가 불가.
- 본 분석은 *Reviewer 종합 대상* — Agent A (구현 가능성) / Agent B (품질·안전성) 의견과 교차 비교 후 Reviewer 가 합의 보고서 작성.
- §1.2 11 필드 평가는 *G4 §4.2 + prequel §6.3 schema 통합 매트릭스 추정* — 사용자 명시 통합 결정 미존재 → 본 추정은 권고 후보 한정.
- §1.3 RFC 8785 JCS lib 가용성 평가 (Python/JS/Go) 는 *2026-05 시점 PyPI/npm/go.dev 추정* — 본 분석 시점 lib 직접 verify 안 함.

### 8.2 본 분석이 *PASS 판정 트리거하지 않는 것*

- ❌ ADR-012 발행 자동
- ❌ G4 §4.4/§4.6 본문 자동 갱신
- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 자동
- ❌ ADR-008/009/010/011 본문 자동 갱신
- ❌ archive 자동 처리
- ❌ 실 runtime 코드 / migration script 작성
- ❌ Reviewer 종합 *대체*
- ❌ Alt-1 / Alt-2 / Alt-3 / Alt-4 자동 결정 (사용자 명시 결정 영역)
- ❌ ADR-013 / ADR-014 후보 자동 발행

본 Agent C 판정 (APPROVE WITH CONDITIONS) 은 *오직* "Alt-1 진행 적격 + 4 조건 권고" 의미.

---

**작성일**: 2026-05-09
**Agent**: C (대안/단순화 탐색)
**판정**: APPROVE WITH CONDITIONS
**권장 합의 형태**: Alt-1 (사용자 명시 답습) — PR-2 통합 (C-C + C-G) + 풀 3+1 + 외부 LLM 1+ **필수** + 4 조건 충족 시
**핵심 단순화 권고 1줄**: hash chain *항상* + signed | append-commit *둘 중 하나* (옵션 C) + RFC 8785 JCS *우선* + G4 §4.4 fallback + 11 필드 = 10 + `event` (prequel §6.3 schema 통합).
**Reviewer 종합 대상**: Agent A (구현 가능성) + Agent B (품질·안전성) + 본 Agent C
**금지 사항 답습 (변동 없음)**:
- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 자동
- ❌ ADR-008/009/010/011 본문 자동 갱신
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ 실 runtime code / migration script 작성
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 다른 Agent (A, B) 출력 참조 (본 분석 시점)
- ❌ 메타포 강제
