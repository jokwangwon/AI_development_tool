# 외부 LLM 검토 응답 — PR-2 (ADR-012 + G4 §4.4/§4.6 보강) — Claude 인접 컨텍스트

> **회수 일자**: 2026-05-09
> **검토자**: Claude (Anthropic Opus 4.7) — 동일 모델 패밀리 면책 (선행 의뢰 §0과 동일하게 적용)
> **검토 시간**: 약 1시간 분량 추론
> **판정**: APPROVE WITH CONDITIONS (조건부 승인)
> **본 응답은 사용자가 본 세션에 직접 paste 한 원문을 보존** (구조 변경 0건). 본 프로젝트의 Reviewer 가 Agent A / B / C + GPT-5.x 또는 cross-vendor 외부 LLM 응답 (`2026-05-09-pr2-evidence-ledger-response.md`) + 본 Claude 인접 컨텍스트 응답과 종합.

---

## 0. 메타 면책 (선행 의뢰 답습 + 강화)

본 검토자는 Claude이며, DRAFT 작성자도 Claude 패밀리입니다. §11 한계 1·5에 명시된 cross-vendor (GPT-5.x / Gemini) 의무는 본 PR-2 합의 후 P2 v3 진입 전에 반드시 충족되어야 합니다. 본 응답을 동봉하지 않은 blind 의뢰가 통제 가치 더 큼은 선행 의뢰 응답에서 이미 권고했으며 본 PR-2도 동일 적용.

본 PR-2 자료는 내부 Agent A/B/C 분석을 의도적으로 배제한 점이 선행 의뢰 대비 편향 통제 강화입니다. 이는 인식 가능한 개선이며, 본 응답은 그 통제를 존중하여 독립적으로 형성되었습니다.

## 1. 차원 1·13 — 보호 원칙 + 영구 제약 답습 (Foundation)

판정: 적정 (sufficient)

ADR-012 §1 보호 원칙은 ADR-011 §2.1 (a)~(d) + (e) 5조건 패턴을 답습하며, 헌법 8조 (보안) ↔ 5조 (Provider Liquidity, 관용) ↔ §2.3 권위 위계 ↔ §2.4 T1/T2/T3 cross-reference가 골격으로 충분합니다.

필수 보강 (C-1): ADR-012 §1에 다음 cross-reference 명시 추가:

- **헌법 8조**: Evidence Ledger entry는 그 자체로 평문 secret을 포함할 수 있는 INSERT 경로 (P1 변종) — GP-1 SQLCipher trigger의 보호 범위에 ledger DB가 명시 포함되는지 확인 필요. 누락 시 P1 우회 경로 발생.
- **Provider Liquidity**: ledger 형식이 Hermes 의존 0임을 ADR-008 차단조건 #2 cross-reference로 명시 (현 §9.10 / §9.15에서 다루는 영역이지만 §1 원칙 단계에서 선언 의무).
- **메타포 강제 금지**: ADR-012 본문에서 "ledger를 *불변의 진리* 로 비유" 같은 메타포 회피. forgery 방어는 *암호학적 보장* 까지만, *진리 보장* 아님 (선행 의뢰의 자기참조 위험과 같은 메타-순환 회피).

선행 의뢰의 영구 제약 5건은 본 PR-2 §10에 보존되어 있어 답습 자체는 충분합니다.

## 2. 차원 2 — 11번째 필드 (핵심 결정)

판정: **(a) `event` 강력 권고**

이유:

- §5.1의 다른 후보 (b)~(d)는 모두 (a) `event`가 전제되어야 의미가 있습니다. `signature`는 어떤 event에 서명하는지 typed 되어야 하고, `chain_id`는 다중 chain의 유형 분리가 event semantics에 의존하며, `parent_event_id`도 typed event 사이의 cross-reference입니다.
- forgery 방어 (§9.11)의 공격 모델 (a)~(e) 모두 "어떤 종류의 entry가 위조되었는가"를 묻습니다 — `gate_pass` 위조와 `memory_write` 위조는 위협 모델이 다르며, `event` 필드 없이 이를 구분할 수 없습니다.
- 11 entry 중 하나만 추가하는 사용자 명시 제약을 가장 큰 가치로 활용하는 것은 *audit 의미론*을 부여하는 것입니다.

권고 enum 후보 (보수적 시작):

```
event ∈ {
  memory_write, skill_proposed, skill_approved, skill_promoted,
  skill_revoked, gate_pass, gate_fail,
  external_llm_received, evidence_forgery_detected,
  roundtrip_lossy, chain_violation_detected
}
```

(b) `signature`는 별도 layer (commit-level signature) 로 다루는 것이 형식 단순성 보존에 유리. 본 PR-2 §8.4 평가에 후술.

(c) `chain_id`는 1인 메타-템플릿 스케일에서 premature. 다중 chain 필요 시 `schema_version` 0.2로 후행 도입.

(d) `parent_event_id`는 (a) 도입 후 0.2에서 추가.

(e) 10 필드 유지 + hash chain만 강화 = 사용자 명시 "11 필드 구조" 요구 위반 + audit 의미론 결손.

## 3. 차원 3·7·8 — Append-only + Hash Chain 견고성

판정: 다층 강제 필요 (현 사양은 OR 약함)

### 3.1 (C-2) "둘 중 하나 의무" → "다층 동시 의무"로 변경

현 §5.2 "hash chain 또는 git append commit (둘 중 하나 의무)" 는 약합니다. 두 매커니즘은 다른 공격면을 방어합니다:

| 매커니즘 | 방어 영역 | 단독 약점 |
|--------|--------|--------|
| Hash chain (sha256 + canonical JSON) | Middle entry tampering | History 통째 재작성 (force push) 무방어 |
| Git append-only branch | History 재작성 | Middle tampering 후 재계산 (악의적 hash 재기록) 무방어 |
| Signed commit (GPG/SSH) | Host compromise 후 위조 | Key SPOF |

권고 (C-2):

- Hash chain MANDATORY (Layer 1, 모든 entry)
- Git append-only branch MANDATORY (Layer 2, force-push 차단 + pre-commit hook으로 rebase/filter-branch reject)
- Signed commit RECOMMENDED (Layer 3, 1인 동일 호스트에서는 선택, multi-host 전환 시 의무 발동 트리거)

§8.4의 옵션 E 변형 ("hash chain + signed (보조)") 에 git append-only를 추가한 형태.

### 3.2 (C-3) prev_hash 검증 실패 처리

§9.7의 4 후보 중 권고:

- **BLOCK + 새 violation entry 추가 (혼합)**
- 즉, 원본 보존 + 새로운 `event: chain_violation_detected` entry append + 합의 BLOCK + 사용자 명시 review 의무
- 자동 revert는 T3 위반 가능성 (자동 정책 변경)
- Dual write는 silent failure 위험
- BLOCK + manual 단독은 forensic 정보 손실 (어느 시점에 무엇이 깨졌는지 ledger 기록 없음)

### 3.3 (C-4) Full rewrite 방어

권고 매커니즘 조합:

- `git config receive.denyNonFastForwards true` + 보호 branch (1인 호스트에서도 자기-보호)
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
- 월 1회 external snapshot (예: 별도 외부 git remote 또는 cloud storage push) — 1인 SPOF 완화
- T3 자동 정책 변경 금지 답습: rewrite 시도 자체가 T3 violation이며, hook reject가 자동 차단 권한 (T3 *방어* 자동 OK, *변경* 자동 금지의 비대칭 활용)

### 3.4 SHA-256 vs BLAKE3/SHA-3

현 SHA-256은 견고합니다. BLAKE3/SHA-3 권고하지 않음 — 이유: (i) SHA-256 충돌 공격은 evidence ledger 위협 모델에서 무관 (length-extension 공격은 본 사용처 무관, 충돌 공격은 sha256 미발견), (ii) 라이브러리 가용성 (Python `hashlib` 표준), (iii) 1인 부담 ↑.

다만 (C-5) hash 알고리즘 agility 사양 추가: `schema_version` 0.2 이상에서 `hash_algo` 필드 도입 가능성을 ADR-012 §보강에 언급. 현 0.1은 sha256 hardcode 유지. 미래 5~10년 후 마이그레이션 trigger 정의.

## 4. 차원 5·6 — Canonical JSON + Genesis Hash

판정: RFC 8785 JCS 인용 권고 (구현 유연)

### 4.1 (C-6) §8.3 옵션 1 변형

"RFC 8785 JCS 권위 인용 + 자체 구현 허용 (test corpus 검증 의무)"

이유:

- IETF 표준 인용은 권위 명료성 ↑ (합의 시 "왜 이 canonical 정의?" 분쟁 차단)
- 라이브러리 의존 의무가 아닌 *동등성 의무* — Python stdlib `json.dumps(sort_keys=True, separators=(",",":"))` + UTF-8 + numeric 정규화로 JCS 출력과 대다수 케이스 일치
- Test corpus: `tests/canonical/` 에 RFC 8785 reference 출력 ≥ 20개 포함, CI 회귀 검증 (입력 → 자체 canonical → JCS reference output 비교). 불일치 시 BLOCK.

옵션 4 (자체 정의 minimal) 단독은 분쟁 시 권위 출처 부재로 비권고.

### 4.2 (C-7) Genesis hash 정의

현 `sha256("genesis:<scope>:<schema_version>")` 은 부족:

- `chain_id` 도입 시 (10 필드 → 0.2에서) genesis 정의 변경 의무 발생
- `event` 필드 도입 시 (11 필드 본 PR-2) 첫 entry의 `event` 의미가 `schema_version`에 포함되지 않음

권고:

```
genesis = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

이렇게 하면 genesis 자체가 canonical JSON 규칙 답습 + first entry timestamp + 작성 agent 명시. Multi-chain 도입 시 `chain_id` 추가만으로 확장 가능.

## 5. 차원 9 — Round-trip Lossy 검출

판정: §8.5 옵션 (c) 수정 권고 — Tier-based

(d) 현 OR 유지는 너무 약함 (사용자가 "의미 보존"을 자기 판단 근거로 PASS 선언 가능, 자기참조 위험 — G3 §4.7 메타-순환 답습).

권고 (C-8) Tier-based:

- T2 (Skill / Memory promoted): hash 일치 STRICT — 손실 0건. 위반 시 BLOCK.
- T3 (Cross-vendor migration): 의미 보존 허용. 단 다음 자동화 가능 검증 의무:
  - 손실 영역 enumeration (어느 필드가 변환 시 의미 변화?) 자동 추출
  - 사용자 명시 review + ADR-011 §2.4 T2/T3 분류상 사용자 승인 필수
  - `event: roundtrip_lossy` ledger entry 의무 (앞서 권고한 `event` 필드와 정합)
- 신규 chain (genesis): 본 사항 무관

`event: roundtrip_lossy` ledger entry 형식:

```jsonl
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"...","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"..."},...}
```

자동화 vs 사용자 review 분리: `lost_fields` enumeration은 자동, `semantic_diff` 판단은 사용자.

## 6. 차원 4·8·11 — Signed Commit + Forgery 방어

판정: 공격 모델별 차등 평가

§9.11의 5 공격 모델 분석:

| 공격 | 본 PR-2 방어 유효성 | 권고 보강 |
|------|---------|---------|
| (a) 1인 호스트 침해 | 약 — host에 GPG key까지 있으면 모든 layer 우회 | external snapshot (월 1회) — 침해 후 발견 가능 |
| (b) Hermes container compromise | 강 — Hermes는 ledger write 권한 0 (G3 §2 T3) | (그대로) |
| (c) Git history rewrite | 중 — append-only branch + pre-commit hook이 대부분 차단, 그러나 host 권한 상승으로 force push 가능 | (a) 동일 |
| (d) JSONL middle tampering | 강 — hash chain이 정확히 이 케이스 차단 | (그대로) |
| (e) External LLM response 위조 | 약 — vendor API key/signed response 부재 시 검증 불가 | (C-9) 권고 |

(C-9) **External LLM response 인증**: API key로 가져온 응답이 아닌 *수동 paste* 시 (현 본 PR-2 의뢰 방식 그대로) 사용자가 직접 signed commit으로 ledger 적재. ADR-012 §보강에 다음 명시:

```
External LLM response 적재 시:
- ledger entry agent = "user" (paste 주체)
- event = "external_llm_received"
- content.source_vendor = "gpt-5.x" / "gemini" / "claude-adjacent"
- content.canonical_hash = sha256(canonical(response_body))
- evidence_refs = ["docs/external-review/<file>.md"]
- 본 entry 작성 시 git commit 사용자가 git config user.email 검증 + GPG 서명 권장
```

## 7. 차원 10 — JSONL Export/Import 무결성

판정: APPROVE WITH CONDITIONS

(C-11) Import 시 schema_version declaration:

- Import script (`scripts/hermes-migration/import.py`) 의무 검증:
  1. `schema_version` 필드 존재 확인
  2. 호환성 매트릭스 조회 (현 0.1 ↔ 외부 형식 매핑)
  3. 미일치 시 BLOCK + 사용자 명시 manual approval 요구
- 호환성 매트릭스는 ADR-012 §보강에 표 형태로 (현 MVP는 0.1 only, 외부 형식은 cross-vendor 응답)

(C-12) Migration 검증 실패 = BLOCK + manual + 새 violation entry (C-3 답습)

## 8. 차원 12·15 — Migration Rollback + ADR Cross-reference

판정: APPROVE WITH CONDITIONS

(C-13) ADR cross-reference 의무:

- ADR-008 차단조건 #2: JSONL export 표준 흡수
- ADR-010: SQLCipher Vault — Evidence Ledger DB 가 secret을 포함할 수 있는 경우 (예: redacted secret evidence) GP-1 SQLCipher trigger 의 보호 대상 명시 의무
- ADR-011 §2.1·§2.3·§2.4: 본 ADR-012 의 모법

ADR-009 (Self-Adapter v2 entry) 와의 cross-reference는 본 PR-2 범위 외 (별도 PR — C-N 영역).

## 9. 차원 14 — PR-2 통합 묶음

판정: APPROVE

C-C (ADR-012) + C-G (G4 §4.4/§4.6) 의 강한 의존:

- ADR-012 §1 보호 원칙 → G4 §4.4 hash chain 사양 보강 (구체화)
- ADR-012 §11 필드 → G4 §4.2 schema 갱신 (10 필드 → 11 필드)
- ADR-012 §round-trip → G4 §4.6 절차 보강

분리 시 (PR-2a + PR-2b) 풀 3+1 합의 *2회* 비용 + cross-reference 일관성 위험. 통합 진행 정당.

## 10. 차원 16 — 메타 편향 + cross-vendor

판정: APPROVE WITH CONDITIONS

(C-14) **본 PR-2 합의 후 P2 v3 정식 채택 진입 *전* cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무**:

- 본 응답 + 의뢰 자료의 Claude 패밀리 공유는 본 PR-2 범위 내에서는 통제 가능 (5 입력 중 본 응답만 Claude, 4 입력은 다른 컨텍스트)
- 그러나 P2 v3 = 정식 권위 발행 시점이므로 cross-vendor 1+ 의무
- 사용자 명시 결정 3 (P2 v3 진입 전 외부 LLM 추가) 답습

(C-15) 본 PR-2 산출 (ADR-012 + G4 보강) 자체에 다음 메타 한계 §1.5 추가 권고:

```
본 ADR-012는 동일 모델 패밀리 (Claude) 의 자기 작성 산출이며, 본 PR-2 합의 시점
cross-vendor 외부 LLM 응답 1+ 가 권위에 포함됨. P2 v3 정식 채택 진입 전 추가
cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무. 본 한계는 영구 핵심
제약 답습이 아니라 *생성 컨텍스트 추적*에 한정.
```

## 11. 추가 차원 — Timestamp Monotonicity

판정: 본 PR-2 가 명시 권고 (의뢰 자료에 미언급)

(C-15) Timestamp monotonicity assertion:

- 각 entry `ts` 는 ISO 8601 (의뢰 답습)
- 추가 의무: 본 entry `ts` ≥ `prev_hash` 의 entry `ts` (timestamp monotonicity)
- 위반 시 `event: chain_violation_detected` (C-3 답습)
- NTP 동기화 가정 — 1인 호스트에서 silent clock drift 위험 인지 (영구 핵심 제약 #1 SPOF 답습)

## 12. 추가 차원 — Content-level Forgery (의뢰 자료 미언급, 한계 명시 권고)

판정: 본 PR-2 *방어 범위 밖* 명시 의무

(C-16) ADR-012 §11 한계 명시:

```
본 ADR-012 는 ledger entry 의 *형식적 무결성* (hash chain / canonical / append-only / signed)
까지만 보호. content 자체의 *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼
ledger 에 기록) 은 본 ADR-012 방어 범위 외. 헌법 1조 (정직성) + 합의 인프라 (3+1 + 외부 LLM)
+ Reviewer 종합 + Human override 가 content-level 보장 layer.
```

본 한계는 ADR-011 §7.3 답습 ("본 ADR-011 은 Hermes 안전성을 선언하지 않는다 — Hermes 는 검증 대상이며, 본 ADR-011 은 검증 외부화의 권위 근거이다") 와 동일 패턴.

## 13. 추가 차원 — 운영 부담 명시

판정: APPROVE WITH 명시 권고

(C-17) ADR-012 §보호원칙에 운영 부담 monitoring trigger 명시. 예:

> ledger entry 작성 평균 시간 > 30초 / 일 ledger 수 > 50건 시 단순화 합의 트리거.

메타-템플릿이 과도화 되어 사용자가 우회하기 시작하는 것이 가장 큰 reality risk.

## 14. 최종 판정

**APPROVE WITH CONDITIONS**

본 PR-2는 ADR-012 신규 발행 + G4 §4.4/§4.6 보강의 방향과 통합 묶음 결정이 정당합니다. 그러나 다음 조건 충족 후 머지 권고:

### 필수 조건 (17건)

- **C-1**: §1에 헌법 8조 (P1 변종) / Provider Liquidity / 메타포 회피 cross-reference 명시
- **C-2**: "둘 중 하나" → "다층 동시 의무" (hash chain + git append-only + signed RECOMMENDED) 변경
- **C-3**: prev_hash 검증 실패 = BLOCK + 새 `chain_violation_detected` entry append
- **C-4**: Full rewrite 방어 = pre-commit hook + denyNonFastForwards + 월 1회 external snapshot
- **C-5**: hash 알고리즘 agility 후행 도입 가능성 §보강 언급 (현 SHA-256 유지)
- **C-6**: RFC 8785 JCS 권위 인용 + 자체 구현 허용 + test corpus 회귀 의무
- **C-7**: Genesis hash 재정의 (canonical JSON 답습 + 4 필드)
- **C-8**: Round-trip lossy = Tier-based (T2 strict / T3 의미 보존 + 사용자 명시 승인)
- **C-9**: External LLM response 적재 절차 §추가 (signed commit + agent: user)
- **C-10**: P10 (Evidence Forgery) 정식 등록 본 PR-2 내 동시 처리
- **C-11**: Import 시 schema_version declaration 의무화
- **C-12**: Migration 검증 실패 = BLOCK + manual + 새 violation entry
- **C-13**: ADR-008 #2 / ADR-010 / ADR-011 §2.1·§2.3·§2.4 cross-ref 의무
- **C-14**: P2 v3 정식 채택 진입 전 cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무
- **C-15**: Timestamp monotonicity assertion 추가
- **C-16**: Content-level forgery 한계 §11 명시 (방어 범위 밖)
- **C-17**: 운영 부담 monitoring trigger 명시

### 11번째 필드 권고

**`event` (enum) — (a) 후보**. 다른 후보 (b)~(e)는 비권고 (사유: §2 본문).

### 진행 가능 범위

- ✅ PR-2 본 안 머지 (C-1 ~ C-17 충족 시)
- ⏳ Implementation/Runtime PASS = PoC 후 별도 합의 (선행 의뢰 응답 답습)
- ⏳ P2 v3 정식 채택 합의 진입 = PR-2 머지 + cross-vendor (C-14) + 사용자 명시 결정 후

## 15. 메타 코멘트 — 검토자 자기 노출

본 검토는 약 1시간 분량 추론. 잠재 사각지대:

- Claude 패밀리 공유 (선행 의뢰 답습)
- Cryptography 영역 심층 검토는 본 검토자 한계 — RFC 8785 JCS 동등 구현 검증은 crypto specialist + GPT/Gemini 추가 의견 권고
- 본 PR-2 §11 한계 5의 "외부 LLM 1+로 본 PR-2 진행 결정 후보" 는 *최소* 조건 — Reviewer의 사용자 명시 결정에서 cross-vendor 1+ 추가 가치 재평가 권고

본 응답을 단일 evidence가 아닌 multi-LLM 평가의 한 입력으로 다루기 권합니다.

---

**원문 보존 종료** — Reviewer 가 본 응답 + GPT/cross-vendor 응답 + Agent A/B/C 와 종합.
