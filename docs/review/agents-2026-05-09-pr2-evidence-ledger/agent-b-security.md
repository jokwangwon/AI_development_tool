# Agent B — 보안/거버넌스 분석 (PR-2: ADR-012 신규 발행 + G4 §4.4/§4.6 hash chain 사양 보강)

**작성일**: 2026-05-09
**Agent 역할**: 보안/거버넌스 검증가 (3+1 풀 합의 — Phase 2 독립 분석)
**검토 범위**: PR-2 최소 필수 산출 — ADR-012 신규 발행 (Evidence Ledger 보호) + G4 §4.4/§4.6 hash chain / canonical JSON / round-trip 사양 보강
**검토자 컨텍스트**: 본 분석은 메인 컨텍스트와 동일 클로드 인스턴스가 작성 — 자기참조 + 메타 편향 위험 인지하며 §0.3 / §6 / §7 에서 통제
**격상 범위 외**: Hermes PMO 격상 선언 / P2 v3 자동 채택 / ADR-008/009/010/011 본문 자동 갱신 / archive 자동 처리 / 실 runtime code / migration script 구현 / Tier-2/3 catalog 자동 확장 — 본 PR-2 영구 답습

---

## 0. 본 입력의 입장 + 메타 한계

### 0.1 핵심 입장 (한 문장)

PR-2 가 명시한 6 항목 + G4 §4.4/§4.6 보강은 **Evidence Ledger 변조 방지의 *형식·절차* 권위화 측면에서 적격** 이지만, 영구 핵심 제약 5건 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) 중 **Hermes ≠ root of trust** 와 **수단/목적 분리** 두 영역에서 *명시 답습* 이 ADR-012 본문 차원에서 형식화되어야 한다. 또한 **chain 재계산 위조 (full rewrite) 차단의 *외부 anchor*** 가 단일 host SPOF (G3 §5.5) 와 결합 시 **MEDIUM 잔여 위험** 으로 식별 — 본 PR-2 는 *설계 권위화* 까지 적격, *실 hook 구현* 은 별도 영역.

### 0.2 본 분석의 *판정하지 않는* 것

- ❌ Hermes PMO 격상 자동 권유
- ❌ P2 v3 정식 채택 자동 발화
- ❌ ADR-008/009/010/011 본문 자동 갱신 (cross-reference 권고만 가능)
- ❌ ADR-012 본문 자동 작성 (본 분석은 *Reviewer 종합 판정 입력* 한정)
- ❌ G4 §4.4/§4.6 본문 자동 갱신
- ❌ 실 runtime / migration / hash chain 검증 hook 코드
- ❌ Tier-1/2/3 catalog 자동 확장
- ❌ 다른 Agent (A, C) 출력 참조
- ❌ archive 자동 처리

### 0.3 본 분석의 메타 한계 (강조)

본 입력은 메인 컨텍스트와 **동일 클로드 인스턴스**. 자기참조 + 메타 편향 위험 인지. 외부 LLM 1+ 검증은 PR-2 풀 3+1 합의 시점에 별도 흡수 (G3 §4.4.2 답습) — 본 분석은 *Agent B 관점에서의 판정* 한정.

본 분석에서 자체 식별한 메타 한계 5건:

1. ADR-012 본문 자체가 *본 PR-2 이전 시점에는 미작성* — 본 분석은 *PR-2 6 항목의 *충분성* 평가* 까지, ADR-012 본문 *적격성* 평가는 ADR-012 본문 작성 후 별도 검토 필요
2. RFC 8785 JCS 표준의 보안적 충실성 평가는 IETF 권위 영역 — 본 분석은 *채택 여부 + 운영 함의* 한정
3. Hash chain "full rewrite" 차단의 *외부 anchor* 후보 (git tag / external timestamp / signed commit) 의 trade-off 평가는 **외부 LLM 의견 권고** 영역
4. 본 분석이 *G4 §4.4 의 현 본문* (단순 hash chain + git append commit 양자택일) 을 평가하나, *외부 anchor 강제 여부* 는 ADR-012 본문 결정 권한 영역
5. SPOF Accepted Risk (G3 §5.5) 는 *의도적 수용* 이지만, 본 PR-2 가 SPOF 강화 또는 약화 양 방향 모두 영향 가능 — 본 분석은 *PR-2 가 SPOF 영향 어느 방향인지* 만 평가

---

## 1. PR-2 핵심 산출 6 항목 의 보안/거버넌스 평가

### 1.1 6 항목 enumeration 답습 (사용자 명시)

| # | PR-2 산출 항목 | 보안/거버넌스 차원 |
|---|-------------|--------------|
| 1 | ADR-012 신규 발행 — Evidence Ledger 보호 원칙 | 권위 격상 |
| 2 | 11 필드 구조 (현 G4 §4.2 = 10 필드, +1 확장) | schema 보안 |
| 3 | append-only 원칙 + hash chain + signed/append commit (둘 중 하나 의무) | 변조 방지 |
| 4 | RFC 8785 JCS canonicalization 채택 여부 | hash 일관성 보안 |
| 5 | Genesis hash 정의 / prev_hash 검증 실패 처리 / full rewrite 방어 / round-trip lossy 검출 | 무결성 운영 |
| 6 | JSONL export/import 무결성 + Evidence forgery 방지 | 출구 + 형식 보안 |

추가 보강 (G4 §4.4 / §4.6):
- canonical JSON 규칙 명확화 (key 정렬 / whitespace / numeric / RFC 8259 → RFC 8785 JCS 채택 여부 결정)
- §4.6 round-trip 검증 절차 보강
- migration / export / import 검증 실패 시 rollback 조건

### 1.2 6 항목 보안/거버넌스 견고성 (개별)

| # | 항목 | 견고성 판정 | 근거 |
|---|----|--------|----|
| 1 | ADR-012 신규 발행 | **APPROVE** | system-identity-prequel §6.4 "Phase 1 종료 시 schema 고정 + ADR-012 (Evidence Ledger Schema) 발행" 권위 답습. PR-2 가 *prequel 명시 후속 작업* 의 정식 ADR화 — Hermes ≠ root of trust 권위 위계 (ADR-011 §2.3) 와 *영구 권위* 동급으로 격상 |
| 2 | 11 필드 (10+1) | **APPROVE WITH CONDITIONS** | 현 system-identity-prequel §6.3 schema = 10 필드 (`ts/task_id/event/agent/result/ref/summary/evidence_md/prev_hash/hash`) + G4 §4.2 schema = 10 필드 (`type/scope/id/schema_version/ts/agent/content/evidence_refs/prev_hash/hash`). PR-2 +1 확장은 *어느 schema 기준* 인지 명시 부재 — Gap-1 (§3) |
| 3 | append-only + hash chain + signed/append commit (양자택일) | **APPROVE WITH GAPS** | system-identity-prequel §6.3 + G4 §4.4 답습. 단 "둘 중 하나 의무" *양자택일* 이 **chain 재계산 (full rewrite) 위조** 차단을 한쪽만으로는 보장하지 못함 — 양쪽 동시 필수 또는 외부 anchor 추가 권고 (Gap-2, §3) |
| 4 | RFC 8785 JCS 채택 여부 | **APPROVE WITH CONDITIONS** | G4 §11.1 self-disclosure ("JCS 직접 인용 안 함") + G4 §11.4 P-1 ("PR-2 풀 3+1 시 §4.4 본문에 RFC 8785 JCS 명시 인용") 답습 = PR-2 가 정확히 P-1 처리 시점. JCS 채택 자체는 *보안 차원 PASS* (canonical 일관성 표준화) — 단 IETF 권위 인용 방식 (RFC 8785 본문 인용 vs 표준 ID 한정 인용) 의 *권위 강도* 차이 평가 필요 (Gap-3, §3) |
| 5 | Genesis / prev_hash 실패 / full rewrite / round-trip lossy | **APPROVE WITH GAPS** | Genesis hash = `sha256("genesis:<scope>:<schema_version>")` 결정적 → 외부 anchor 부재 시 *원본 chain 전체 재구성 가능* (G3 §5.5 SPOF 와 결합 시 MEDIUM 위험). prev_hash 검증 실패 처리는 4 후보 (BLOCK / 자동 revert / 원본 보존+새 entry / dual write) 명시 필요 — Gap-4 (§3, §2 차원 2). full rewrite 방어 = 외부 anchor 권고 (Gap-2). round-trip lossy 검출 = G4 §4.6 "손실 영역 ledger entry (`event: roundtrip_lossy`)" 답습이지만 *그 entry 자체가 T2/T3 트리거* 인지 명시 부재 (Gap-5, §2 차원 4) |
| 6 | JSONL export/import 무결성 + Evidence forgery 방지 | **APPROVE WITH CONDITIONS** | G4 §4.3 "Hermes 의존 0 보장" + §4.6 round-trip + §3.5 provider-neutral 답습 정합. forgery 방지는 §1.2.5 P10 신규 등록 (Evidence Ledger 변조 시도 = 헌법 8조 신규 위반 경로 P10) 가 G2 본문에 명시되어야 함 — Gap-6 (§2 차원 1, 7) |

### 1.3 6 항목 종합

- **APPROVE 직접** 1건 (#1 ADR-012 발행)
- **APPROVE WITH CONDITIONS** 3건 (#2, #4, #6)
- **APPROVE WITH GAPS** 2건 (#3, #5)
- **PARTIAL/BLOCK** 0건

**판정**: 6 항목 모두 본 PR-2 차단 사유 *아님* — 단, 6 Gap (§3) 흡수 권고. 격상 통합 합의 시점 외부 LLM 1+ 권장 (G3 §4.4.2 답습).

---

## 2. 8 차원 평가

### 2.1 차원 1 — Evidence Forgery 방어 (G2 §1.2.5 P10 cross-reference)

#### 2.1.1 11 필드 구조 + hash chain + signed/append commit 의 forgery 방어 견고성

11 필드 (10+1) 구조 자체가 forgery 방어의 *형식 입력*. 검증 가능성 측면:
- `ts` ISO 8601 → 시간 역순 삽입 검출 (단일 layer)
- `agent` provider-neutral identifier → "user/Hermes/<worker>" 구분으로 author 위조 1차 검출
- `prev_hash` + `hash` (sha256) → chain 끊어짐 검출 (단일 entry 위조)
- `event` enum → 정의 외 이벤트 → schema 검증 실패
- (+1 확장) — 후보: `signature` (signed commit 시) / `external_anchor_ref` (외부 timestamp) / `policy_change_required` flag — *명시 결정 권한 = ADR-012 본문 영역*

**판정**: 형식 입력 *충실*. 단 **+1 확장 후보 필드의 미결정** = Gap-1 (§3). 외부 anchor 후보 필드 부재 시 full rewrite 방어 잔여 위험 (§2.3).

#### 2.1.2 공격 모델별 PR-2 산출 방어 유효성

| 공격 모델 | 본 PR-2 산출 방어 | 판정 |
|--------|-----------|----|
| (a) **1인 개발자 호스트 침해** | hash chain + git author 검증 + signed commit (옵션). Genesis hash 결정적 → SPOF (G3 §5.5 의도적 수용) | **WEAK** — 호스트 침해 시 git config / SSH key / GPG key 모두 침해 가능. 외부 anchor (예: GitHub remote signed tag) 권고 |
| (b) **Hermes container compromise** | filesystem read-only on `.git/` (G3 §2.5 #1) + Hermes-originated commit auto-reject (§2.2 #20) + ledger entry append-only | **PASS** — Hermes container 침해 → 정책 파일 변경 시도 → §2.5 #11 (Evidence Ledger T3) hook 차단 + audit log. 단 *implementation pending* (G3 §0.2 #7) |
| (c) **git history rewrite (force push, rebase, filter-branch)** | git append-only 강제 (signed commit option) + branch protection rule (사용자 명시) + Hermes-originated rewrite auto-reject | **WEAK** — 1인 개발자 = branch protection 우회 가능 (사용자 자체가 force push 권한). 외부 anchor (GitHub Actions run ID + artifact + signed manifest) 권고 |
| (d) **JSONL middle entry tampering** | hash chain 끊어짐 즉시 검출 (single entry 위조) + canonical JSON sha256 비교 | **PASS** — RFC 8785 JCS 채택 시 *결정적 hash* 강화. canonical JSON 규칙 비-JCS 채택 시 (G4 §4.4 현 본문) lex sort + RFC 8259 도 검출 가능하나 *구현 다양성 위험* |
| (e) **External LLM response 위조** | system-identity-prequel §3.3 #2 (사용자 명시 commit 강제) + G3 §2.5 #9 (`docs/external-review/` T3 append-only + Hermes-originated 변경 자동 reject) + 본 §4 외부 LLM 자기참조 차단 | **PASS** (조건부) — G3 §2.5 #9 가 본 항목을 *enumeration 명시* 흡수. 단 *외부 LLM 응답 hash 검증* 자체 hook 0건 (별도 합의) |

**종합 공격 모델 판정**:
- **PASS 2건** ((b), (d))
- **PASS 조건부 1건** ((e))
- **WEAK 2건** ((a), (c)) — 외부 anchor 권고

#### 2.1.3 T1 → T2 lateral movement 위험

Worker 학습 (T1) → Memory promotion (T2) 경로에서 evidence forgery 가 lateral movement 로 이어질 위험:
- Worker T1 학습 결과는 Memory write 권한 0 (G3 §2.2 #15) → *직접* 위조 불가
- 단 Worker 가 "*제안*" 으로 Skill `proposed` 등록 (G3 §2.1 #3, T1) → 사용자 명시 승인 시 T2 전이 → 이 시점 evidence (`required_evidence`) 위조 시 promoted 까지 escalation 가능
- G4 §3.4 답습: Skill `proposed → approved` (T2 사용자 명시) + `approved → promoted` (T2 + Evidence) 두 layer
- 본 PR-2 ADR-012 가 **`required_evidence` ledger entry 자체의 변조 방지** 를 명시 흡수 시 lateral movement 차단

**판정**: lateral movement *2 layer 차단 강함* — 단 ADR-012 본문이 "Skill `promoted` 진입 시 ledger entry hash 검증 의무" 를 명시 흡수 의무 (Gap-7, §3).

### 2.2 차원 2 — prev_hash 검증 실패 처리의 안전성

#### 2.2.1 4 후보 처리 방식 보안 트레이드오프

| 후보 | 처리 방식 | 보안 트레이드오프 | 권고 |
|----|------|----------|----|
| (1) BLOCK + manual review | chain 끊어짐 즉시 BLOCK + 사용자 검토 의무 | **HIGH 보안 + 운영 부담 高** — 정상 케이스 (예: rebase 후 chain 재계산 정상화) 도 BLOCK | **권고** (T3 영역, ADR-011 §2.4 답습) |
| (2) 자동 revert | chain 끊어짐 검출 시 직전 정상 entry 로 자동 revert | **MEDIUM 보안 + T3 위반 위험** — Hermes 가 자동 revert 를 *정책 변경* 으로 활용 가능 (silent drift) | 비권고 (T3 자동 변경 우회 위험) |
| (3) 원본 보존 + 새 entry | 끊어짐 entry 보존 + 검증 실패 entry 새로 append | **MEDIUM 보안 + ledger 부풀림** — append-only 답습이지만 "검증 실패 entry 가 정상 entry 옆에 누적" 으로 forgery vs 정상 구별 어려움 | 조건부 권고 (failure entry 자체에 `event: chain_validation_failed` flag 의무) |
| (4) Dual write | chain 끊어짐 시 별도 backup chain 으로 dual write | **HIGH 보안 + 복잡도 高** — backup chain 자체가 forgery 대상 가능 (이중 위조) | 비권고 (복잡도 대비 보안 증가 marginal) |

**보안 권고**: **후보 (1) BLOCK + manual review** 채택 권고 — ADR-011 §2.4 T3 (자동 정책 변경 금지) 답습. 단 *prev_hash 검증 실패* 자체가 *T1 학습 결과 → T3 silent 변경* 의 *암시적 검출 신호* 이므로 자동 BLOCK + 사용자 명시 검토 의무.

#### 2.2.2 Silent failure 위험 — Layer 1~6 hook 어디에서 BLOCK?

| Layer | 책임 | BLOCK 시점 | 본 PR-2 흡수 |
|-----|----|--------|-------|
| 0 | CLAUDE.md (가이드) | (해당 없음 — 권고만) | (위임) |
| 0.5 | 검토 질문지 (가이드) | (해당 없음) | (위임) |
| 1 | PostToolUse hook (자동 lint) | ledger entry 작성 시 hash chain 검증 → 끊어짐 시 BLOCK | **권고** (ADR-012 본문 명시 의무) |
| 2 | PreCommit hook | git commit 시 ledger 파일 hash chain 재검증 → 끊어짐 시 commit reject | **권고** (G3 §2.5 #11 답습 강화) |
| 3 | git pre-commit hook | (Layer 2 와 동일 — local hook) | (위임) |
| 4 | CI pipeline | nightly + PR 시 hash chain 전체 재검증 → FAIL 시 build reject | **권고** (R-6 workflow 답습 확장) |
| 5 | 3+1 합의 | 합의 보고서 commit 시 ledger entry 동시 append (§5.3 (iv)) | (G3 §1.3 답습) |
| 6 | Human review | 최종 BLOCK 결정 권한 | (T3 사용자 명시 영역) |

**판정**: **Layer 1, 2, 4, 5 4중 보호** 권고. 본 PR-2 ADR-012 본문에 "**hash chain 검증 실패는 4 layer 중 어느 layer 에서든 BLOCK 가능, 우회 시 다음 layer 가 backup**" 명시 권고 (Gap-8, §3).

#### 2.2.3 T3 (자동 정책 변경 금지) 위반 가능성

후보 (2) 자동 revert 채택 시:
- Hermes 가 검증 실패 → 자동 revert → *정책 silent 변경 우회 경로* 가능
- ADR-011 §2.4 T3 위반 (자동 학습 결과의 자동 정책 반영 금지)
- G3 §2.2 #17 (자체 학습 결과의 자동 정책 반영 = T3) 직접 침해

**판정**: 후보 (2) 채택 시 T3 위반. **후보 (1) BLOCK + manual review** 가 ADR-011 §2.4 답습 정합. ADR-012 본문에 *후보 (1) 채택* 명시 의무 (Gap-9, §3).

### 2.3 차원 3 — Full rewrite 방어

#### 2.3.1 git history 통째 재작성 차단 매커니즘

| 시도 | 차단 매커니즘 | 강도 |
|----|----------|----|
| `git push --force` | branch protection rule (사용자 명시) | **MEDIUM** (1인 개발자 = 사용자 자체가 권한 보유) |
| `git rebase -i` 후 force push | branch protection + signed commit verification (각 commit signature 검증) | MEDIUM |
| `git filter-branch` / `git filter-repo` | (`.git/` filesystem read-only on Hermes container 답습) + branch protection + GitHub Actions audit | MEDIUM (Hermes 차단 가능, 사용자 host 침해 시 우회) |

**판정**: 1인 개발자 + 단일 호스트 SPOF (G3 §5.5) 와 결합 → **모든 차단 매커니즘이 사용자 호스트 침해 시 우회 가능**. 외부 anchor 필수.

#### 2.3.2 외부 anchor 후보 비교

| 후보 | 보안 효과 | 운영 부담 | 권고 |
|----|------|------|----|
| **Signed tag (GPG)** | tag signature → external verification 가능 | 사용자 GPG key 관리 부담 | 권고 |
| **Signed commit** | 각 commit signature → 위조 검출 | GPG key 관리 + commit 빈도 부담 | 권고 (옵션) |
| **External snapshot (S3 / IPFS)** | 외부 immutable storage | 외부 인프라 비용 + 1인 개발자 운영 부담 | **비권고** (Hermes PMO 격상 후 multi-host 전환 시점, G3 §5.5.3 (3) 트리거 답습) |
| **Append-only filesystem (chattr +a)** | OS-level append-only | 1인 개발자 host 침해 시 우회 가능 | 보조 |
| **GitHub Actions run ID + artifact (R-6 답습)** | external timestamp + GitHub infrastructure 권위 | 이미 구축됨 (R-6) | **강력 권고** |
| **GitHub branch protection + multi-author** | (G3 §5.5.3 (1) 트리거 답습) | multi-author 진입 시점 | 권고 (multi-host 전환 후) |

**보안 권고**: **GitHub Actions run ID + artifact + Signed tag (GPG) 양자 동시** 채택 — 본 PR-2 ADR-012 본문에 "**chain 재계산 위조 차단을 위한 외부 anchor (GitHub Actions run ID + signed tag) 의무 또는 강력 권고**" 명시 권고 (Gap-2, §3).

#### 2.3.3 1인 개발자 + 단일 호스트 SPOF 와의 결합

G3 §5.5 (SPOF accepted risk) 답습:
- 현 모델: 단일 사용자 + 단일 호스트 = SPOF *의도적 수용*
- 본 PR-2 ADR-012 가 SPOF 영향: **SPOF 강화도 약화도 *아님*** — chain 재계산 위조 차단은 SPOF 외부 anchor 권고로 *부분 약화*, Genesis hash 결정적은 SPOF 강화 측면

**판정**: 본 PR-2 가 SPOF 약화에 *기여 가능* — 단 G3 §5.5.3 multi-host 전환 트리거 (5건) 충족 시점에 *추가 layer 발동* 명시. ADR-012 본문에 G3 §5.5 cross-reference 권고 (Gap-10, §3).

#### 2.3.4 Multi-host 전환 트리거 (G3 §5.5.3) 와의 cross-reference

G3 §5.5.3 5 트리거:
1. 두 번째 사용자 commit → multi-author 룰
2. Hermes container 분산 → mutual TLS + signed manifest
3. Production 환경 전환 → secrets vault + KMS
4. 외부 LLM 자동화 → API key 분리 + signed manifest
5. Hermes PMO 격상 → multi-layer 전환 동시 충족

**본 PR-2 ADR-012 영향**: 트리거 (4) 외부 LLM 자동화 시 *외부 LLM 응답 hash 검증* 의무 — 본 PR-2 ADR-012 본문에 "외부 LLM 응답도 ledger entry 의무 + hash 검증" 명시 권고 (Gap-11, §3 — Gap-10 와 통합 가능).

### 2.4 차원 4 — Round-trip Lossy 검출의 거버넌스 강도

#### 2.4.1 의미 보존 검증의 사용자 review 의무

G4 §4.6 답습:
> hash 일치 (정확 round-trip) **또는** 의미 보존 검증 (사용자 명시 review — 손실 허용 영역 명시)
> 손실 발생 시 손실 영역 ledger entry (`event: roundtrip_lossy`)

**자기참조 위험**: G3 §4.7 메타-순환 청산 답습 — 사용자 review 자체가 단일 사용자 = 자기 검증. 외부 LLM 1+ 의견 보충 권고.

**판정**: 의미 보존 review 의 *형식 명시* 충실, *외부 검증 layer* 부재. ADR-012 본문에 "**의미 보존 review 시 외부 LLM 1+ 권장 (T2 영역, G3 §4.4.2 답습)**" 명시 권고 (Gap-12, §3).

#### 2.4.2 `event: roundtrip_lossy` 가 T2/T3 트리거가 되어야 하는가?

| 시나리오 | 적정 분류 | 사유 |
|------|------|----|
| 손실 영역이 *단순 메타데이터* (예: timestamp precision) | **T1 자동 (informational)** | 의미 보존 OK |
| 손실 영역이 *Skill 본문 일부* (예: provider_bindings 손실) | **T2 사용자 명시 review** | Provider Liquidity 영향 (헌법 5조) |
| 손실 영역이 *evidence_refs / hash chain* | **T3 자동 BLOCK** | Evidence Ledger 무결성 직접 침해 (헌법 8조 본질) |
| 손실 영역이 *정책성 필드* (`required_evidence` / `allowed_actions`) | **T3 자동 BLOCK** | 정책 변경 silent 우회 가능 |

**판정**: `event: roundtrip_lossy` 자체가 *단일 분류* 아닌 *손실 영역별 차등 분류* 가 적정. ADR-012 본문에 "**loss 영역 분류 매트릭스 + 분류별 T1/T2/T3 처리**" 명시 권고 (Gap-13, §3).

#### 2.4.3 Migration script Hermes 의존 0건 (depcruise) 의 ADR-012 보호 위치

G4 §4.5.2 + §4.3 답습:
- migration script Hermes 의존 0건 (depcruise 검증)
- 표준 라이브러리만 사용 (provider SDK 직접 import 금지 — §6.4 답습)

**ADR-012 보호 위치**: 본 PR-2 가 ADR-012 본문에 "**migration script Hermes 의존 0건 강제 메커니즘 (depcruise)** + Provider Liquidity 4-way Multi-layer Defense 답습" cross-reference 명시 권고 — Gap-14 (§3).

### 2.5 차원 5 — RFC 8785 JCS 채택의 보안 함의

#### 2.5.1 비-JCS canonical JSON (현 G4 §4.4) vs JCS 의 보안 차이

현 G4 §4.4 본문:
- key 정렬: lexicographic
- whitespace 제거
- numeric 정규화 (integer / float IEEE 754)
- string escape: RFC 8259

RFC 8785 JCS 추가:
- Number 표현 표준 (ECMAScript Number.prototype.toString 답습)
- Unicode normalization 명시 (NFC)
- Object key 정렬 = Unicode code point order
- Empty object / array 표현 명시

**보안 차이**:
| 영역 | 비-JCS | JCS | 보안 함의 |
|----|------|----|------|
| Number edge case (`1.0` vs `1` vs `1e0`) | 정의 모호 | NFC 명시 | **MEDIUM** — 비-JCS 시 implementation 차이로 *동일 의미, 다른 hash* 발생 가능 → forgery 가능성 |
| Unicode (한국어 / emoji) | RFC 8259 만 | NFC 명시 | **MEDIUM** — 한국어 합성/분해 글자 (NFC vs NFD) 차이로 hash 차이 |
| Empty / null | 정의 모호 | 명시 | **LOW** — 일반 케이스 영향 적음 |

**판정**: JCS 채택이 보안 측면 *명백 우위* (위 3 영역 결정성 강화). 본 PR-2 ADR-012 / G4 §4.4 보강에 **RFC 8785 JCS 채택 + IETF RFC 본문 인용 + 위반 검출 hook** 명시 권고 (Gap-3, §3).

#### 2.5.2 Canonical 위반 검출 가능성 (CI 회귀 검증)

CI 회귀 검증 (R-6 workflow 답습 확장):
- canonical JSON 검증 step: ledger entry 의 `hash` 필드 → `content` 본문 canonical JSON 재계산 → 일치 검증
- 위반 시 build FAIL
- nightly 전체 ledger 재검증

**판정**: 검출 가능성 **높음** — JCS 표준 라이브러리 (npm `canonicalize`, Python `json-canonicalize`) 활용. 본 PR-2 ADR-012 / G4 §4.4 보강에 *CI 회귀 검증 step* 명시 권고 (Gap-15, §3 — Gap-8 의 Layer 4 와 통합).

#### 2.5.3 JCS 표준 자체의 신뢰성 (RFC 8785 status, IETF 권위)

- RFC 8785 (Anders Rundgren et al, 2020) — Informational track (Standards Track 아님)
- IETF Informational ≠ 비표준 — 단 Informational 권위는 Standards Track 보다 약함
- 단, **JCS 가 JSON canonicalization 영역의 *사실상 표준***

**보안 권고**: ADR-012 본문에 "**JCS = Informational 트랙, 그러나 JSON canonicalization 의 사실상 표준** + 라이브러리 가용성" 명시. 미래 JCS 가 부족 시 fallback 절차 명시 (Gap-16, §3).

### 2.6 차원 6 — Hermes ≠ root of trust 답습 (ADR-011 §2.3)

#### 2.6.1 본 ADR-012 가 Hermes 자체를 ledger 변조 주체로 명시 차단하는가?

**ADR-011 §2.3 영구 권위**:
> Hermes 는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.

**본 PR-2 ADR-012 가 강제해야 할 차단 매트릭스**:

| 항목 | 차단 메커니즘 | ADR-012 본문 명시 의무 |
|----|--------|------------|
| Hermes 가 ledger entry 본문 작성 | `agent` 필드에 `hermes` 가 가능하나, *Hermes-originated ledger entry* 자체가 audit log 의무 | **명시 의무** |
| Hermes 가 ledger 파일 자체 변조 | filesystem read-only on `docs/evidence/` (Hermes container) — G3 §2.5 #11 답습 | **명시 의무** (cross-reference) |
| Hermes 가 git append commit 으로 ledger 갱신 | Hermes-originated commit auto-reject (G3 §4.5 + §2.2 #20) | **명시 의무** (cross-reference) |
| Hermes 가 외부 LLM 응답을 ledger 에 위조 | `docs/external-review/` T3 + 외부 LLM 응답 hash 검증 | **명시 의무** |

**판정**: ADR-012 가 Hermes 변조 차단을 **명시 매트릭스** 로 흡수해야 함 — Gap-17 (§3, 차원 6 종합).

#### 2.6.2 G3 §2.2 #11 / #20 와 cross-reference 정합

G3 §2.2 답습:
- #11 Constitution 우회 → T3, filesystem ACL
- #20 합의 결과 silent override → T3, git append-only

G3 §2.5 #11 답습:
> Evidence Ledger (`docs/phase0/*-evidence.md`, JSONL ledger 파일, R-6 artifact) — T3 (append-only) + hash chain 또는 git append commit + Hermes-originated 수정 자동 reject + signed commit (PR-2 ADR-012 후보)

**G3 §2.5 #11 가 본 PR-2 ADR-012 를 *명시 후보* 로 선언** — 정합. ADR-012 가 G3 §2.5 #11 cross-reference 명시 의무.

#### 2.6.3 ADR-012 가 *Hermes 안전성 선언하지 않는* 답습 (ADR-011 §7.3)

ADR-011 §7.3 답습:
> 본 ADR 은 Hermes 안전성을 선언하지 않는다 — Hermes 는 검증 대상이며, 본 ADR 은 검증 외부화의 권위 근거이다.

**본 PR-2 ADR-012 에 동등 답습 의무**:
> ADR-012 는 Hermes 안전성을 선언하지 않는다. Evidence Ledger 의 변조 방지 *형식·절차* 권위화일 뿐, Hermes 자체의 ledger 작성 권한 부여가 아니다.

**판정**: ADR-012 본문에 "Hermes 안전성 선언 부재" 명시 답습 의무 (Gap-18, §3).

### 2.7 차원 7 — 헌법 5조 (Provider Liquidity) + 헌법 8조 (보안) cross-impact

#### 2.7.1 본 ADR-012 가 헌법 8조 위반 경로 P1~P5 의 어느 경로와 연결?

| 경로 | 본 PR-2 ADR-012 영향 | 분류 |
|----|------------|----|
| P1 DB INSERT 평문 | (해당 없음 — G1b SQLCipher trigger 영역) | 무관 |
| P2 로그/LLM 송신 평문 | (해당 없음 — Hermes redaction + P1 facade) | 무관 |
| P3 Credential 파일 권한 | ledger 파일 권한 (filesystem ACL on `docs/evidence/`) | **간접 강화** |
| P4 비밀값 하드코딩 | (해당 없음) | 무관 |
| P5 외부 입력 미검증 | 외부 LLM 응답 → ledger entry 시 검증 | **직접 강화** |
| **P10 Evidence Ledger 변조 (신규)** | 본 PR-2 ADR-012 의 *주 대상* | **신규 등록 영역** |

**판정**: 본 PR-2 가 **P10 신규 위반 경로 (Evidence Ledger 변조 = 헌법 8조 본질 침해)** 를 *명시 등록* 권고. G2 본문에 P10 신규 row 추가 = Gap-19 (§3) — 단 G2 본문 변경은 PR-2 범위 외 (사용자 명시 답습) — 따라서 ADR-012 본문에 "**P10 신규 위반 경로 명시 + G2 후속 합의 권고**" 형태로 흡수.

#### 2.7.2 Provider Liquidity 영향 (provider-neutral evidence 형식 보장)

G4 §3.5 + §4.3 답습:
- `provider_bindings` provider-neutral 강제
- JSONL Hermes 의존 0 (depcruise)
- 최소 2 provider 재해석 가능

**본 PR-2 ADR-012 가 Provider Liquidity 보호에 추가 강화**:
- 11 필드 (10+1) 의 *어느 필드도* provider 종속 금지 명시
- canonical JSON (RFC 8785 JCS) = provider-neutral 표준
- migration script Hermes 의존 0 답습

**판정**: Provider Liquidity 무결성 *PR-2 가 강화 기여* — 약화 영향 0. 단 ADR-012 본문에 "**11 필드 모두 provider-neutral 강제**" 명시 권고 (Gap-20, §3).

#### 2.7.3 ADR-011 §2.1 (a)~(d) 4조건 충족 검증

본 PR-2 ADR-012 가 *대체 수단 도입* 인가? 답: **부분적** — 현 G4 §4.4 의 단순 hash chain → 본 PR-2 의 강화 chain 으로의 *수단 강화*. 4조건 적용:

| 조건 | 충족 평가 | 근거 |
|----|------|----|
| **(a) 동등 이상의 보안 결과** | **조건부 충족** | 현 G4 §4.4 = lex sort + RFC 8259 단순 chain ↔ 본 PR-2 = JCS + signed/append commit + 외부 anchor (옵션) — *명백 강화*. 단 *비교표 본문* ADR-012 에 명시 의무 (Gap-21, §3) |
| **(b) 격리 환경 PoC** | **미충족 (격리 PoC 0건)** | R-2 답습은 G1b SQLCipher 영역 — Evidence Ledger PoC 별도 의무. 본 PR-2 는 *설계 권위화* 까지, PoC 는 별도 합의 (Implementation/Runtime PASS 영역) |
| **(c) ADR 권위 명시** | **본 PR-2 ADR-012 자체로 충족** | system-identity-prequel §6.4 ADR-012 발행 답습 |
| **(d) 자동 회귀 검증 경로** | **조건부 충족** | R-6 workflow 답습 확장 (CI canonical JSON 검증 + nightly chain 재검증) — ADR-012 본문에 명시 의무 (Gap-22, §3) |

**판정**: 4 조건 중 (c) 충족, (a)/(d) 조건부, (b) 미충족 (Implementation 영역). PR-2 *설계 PASS 적격*, Implementation/Runtime PASS 는 별도 영역.

### 2.8 차원 8 — 영구 핵심 제약 5건 보호 검증

본 차원은 §5 에서 별도 enumeration. 본 §2.8 은 *간략 매트릭스* 한정.

| 핵심 제약 | 본 PR-2 ADR-012 보호 위치 (예상) | 보호 강도 |
|--------|----------------------|------|
| Provider Liquidity (헌법 5조) | 11 필드 provider-neutral + JSONL provider-neutral + JCS provider-neutral | **HIGH** |
| Hermes ≠ root of trust (ADR-011 §2.3) | "Hermes 안전성 선언 부재" 답습 + Hermes-originated audit + filesystem ACL cross-reference | **HIGH** (조건부 — Gap-17, 18 흡수 시) |
| 메타포 강제 금지 (system-identity-prequel §7) | Evidence Ledger 형식·절차 권위화는 *기존 구조의 ADR화* — 메타포 인플레이션 0 | **HIGH** (영향 무관 — Evidence Ledger 는 메타포 영역 외) |
| 자동 정책 변경 금지 (T3, ADR-011 §2.4) | prev_hash 실패 = BLOCK + manual 권고 (후보 (1)) + chain 재계산 = T3 위반 검출 | **HIGH** (조건부 — Gap-9 흡수 시) |
| 수단/목적 분리 (ADR-011 §2.1) | 4 조건 (a)~(d) 적용 가능 — 수단 강화 정합, 단 비교표 명시 의무 | **MEDIUM-HIGH** (Gap-21 흡수 시) |

**종합**: 5 제약 중 4 = HIGH, 1 = MEDIUM-HIGH. 모두 본 PR-2 차단 사유 *아님* — Gap 흡수 시 HIGH 5/5 가능.

---

## 3. 식별된 Gap (Gap-N enumeration)

### 3.1 종합 Gap 매트릭스

| # | Gap | 영역 | 심각도 | 권고 처리 |
|---|----|----|------|--------|
| **Gap-1** | +1 확장 필드의 *명시 결정 부재* — `signature` / `external_anchor_ref` / `policy_change_required` 후보 중 어느 것을 채택? | ADR-012 §11 schema | **MEDIUM** | ADR-012 본문에 +1 확장 필드 명시 + 후보별 trade-off 비교 |
| **Gap-2** | Hash chain "둘 중 하나 의무" 양자택일이 *full rewrite (chain 재계산) 위조* 차단 부족 — 외부 anchor (GitHub Actions run ID + signed tag) 의무 또는 강력 권고 부재 | ADR-012 + G4 §4.4 | **MEDIUM** | "둘 중 하나" → "양쪽 동시 + 외부 anchor 권고" 강화 |
| **Gap-3** | RFC 8785 JCS 채택 시 IETF 권위 인용 방식 + 위반 검출 hook 명시 부재 | ADR-012 + G4 §4.4 | **LOW-MEDIUM** | ADR-012 본문에 RFC 8785 본문 인용 + JCS 라이브러리 명시 + 위반 검출 hook 사양 |
| **Gap-4** | prev_hash 검증 실패 4 후보 중 채택 부재 + 운영 절차 부재 | ADR-012 §prev_hash | **MEDIUM** | 후보 (1) BLOCK + manual review 채택 + 운영 절차 명시 |
| **Gap-5** | `event: roundtrip_lossy` 자체가 T1/T2/T3 트리거 인지 명시 부재 — 손실 영역별 차등 분류 매트릭스 부재 | ADR-012 §round-trip | **MEDIUM** | 손실 영역별 분류 매트릭스 + 분류별 T1/T2/T3 처리 |
| **Gap-6** | P10 신규 위반 경로 (Evidence Ledger 변조 = 헌법 8조 본질) 의 *G2 본문 등록* 권고 부재 | G2 §1.2 + ADR-012 cross-reference | **MEDIUM** | ADR-012 본문에 P10 명시 + G2 후속 합의 권고 (G2 본문 변경은 PR-2 범위 외 답습) |
| **Gap-7** | Skill `promoted` 진입 시 ledger entry hash 검증 의무 명시 부재 (T1 → T2 lateral movement 차단) | ADR-012 + G4 §3.4 | **LOW** | ADR-012 본문에 "Skill `promoted` 진입 시 ledger entry hash 검증" 명시 |
| **Gap-8** | Hash chain 검증 BLOCK 의 *Layer 1, 2, 4, 5 4중 보호* 명시 부재 | ADR-012 §검증 | **LOW-MEDIUM** | ADR-012 본문에 4 layer enumeration 명시 |
| **Gap-9** | prev_hash 실패 자동 revert 채택 시 T3 위반 위험 — 후보 (1) BLOCK 채택 명시 의무 | ADR-012 §prev_hash + ADR-011 §2.4 | **MEDIUM** | ADR-012 본문에 "후보 (1) BLOCK + manual review 채택" 명시 + ADR-011 §2.4 cross-reference |
| **Gap-10** | G3 §5.5 SPOF accepted risk 와의 cross-reference + 외부 anchor 권고 명시 부재 | ADR-012 + G3 §5.5 | **LOW-MEDIUM** | ADR-012 본문에 G3 §5.5 cross-reference + 외부 anchor 권고 |
| **Gap-11** | 외부 LLM 응답 ledger entry 의무 + hash 검증 명시 부재 (G3 §5.5.3 (4) 트리거 답습) | ADR-012 + G3 §2.5 #9 | **MEDIUM** | ADR-012 본문에 외부 LLM 응답 ledger entry 의무 명시 |
| **Gap-12** | 의미 보존 review 시 외부 LLM 1+ 권장 명시 부재 (자기참조 위험) | ADR-012 §round-trip + G3 §4.4.2 | **LOW-MEDIUM** | ADR-012 본문에 G3 §4.4.2 cross-reference |
| **Gap-13** | round-trip lossy 손실 영역별 T1/T2/T3 분류 매트릭스 부재 (Gap-5 와 통합) | (Gap-5 통합) | (Gap-5 통합) | (Gap-5 통합) |
| **Gap-14** | migration script Hermes 의존 0 강제 메커니즘 (depcruise) cross-reference 명시 부재 | ADR-012 + G4 §4.5.2 | **LOW** | ADR-012 본문에 G4 §4.5.2 cross-reference |
| **Gap-15** | CI 회귀 검증 step (canonical JSON 검증 + nightly chain 재검증) 사양 부재 (Gap-8 의 Layer 4 와 통합) | (Gap-8 통합) | (Gap-8 통합) | (Gap-8 통합) |
| **Gap-16** | JCS = Informational 트랙, fallback 절차 명시 부재 | ADR-012 §canonical | **LOW** | ADR-012 본문에 JCS Informational 명시 + 미래 fallback 절차 |
| **Gap-17** | Hermes 변조 차단 매트릭스 (Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조) 명시 부재 | ADR-012 §Hermes ≠ root | **HIGH** | ADR-012 본문에 4 항목 매트릭스 명시 (G3 §2.5 #11 cross-reference) |
| **Gap-18** | "Hermes 안전성 선언 부재" 답습 명시 의무 (ADR-011 §7.3 답습) | ADR-012 §주의사항 | **MEDIUM** | ADR-012 본문에 ADR-011 §7.3 직접 답습 명시 |
| **Gap-19** | P10 Evidence Ledger 변조 신규 등록 영역 — G2 본문 후속 합의 권고 (Gap-6 와 통합) | (Gap-6 통합) | (Gap-6 통합) | (Gap-6 통합) |
| **Gap-20** | 11 필드 모두 provider-neutral 강제 명시 부재 | ADR-012 §schema | **LOW** | ADR-012 본문에 "11 필드 모두 provider-neutral 강제" 명시 |
| **Gap-21** | 수단/목적 분리 4 조건 (a) 비교표 (현 G4 §4.4 ↔ 본 PR-2 강화 chain) 본문 부재 | ADR-012 §근거 | **MEDIUM** | ADR-012 본문에 비교표 명시 |
| **Gap-22** | 수단/목적 분리 4 조건 (d) 자동 회귀 검증 경로 명시 부재 | ADR-012 §검증 (Gap-8 보강) | **LOW-MEDIUM** | ADR-012 본문에 R-6 workflow 답습 확장 명시 |
| **Gap-23** | ADR-012 발행 자체가 *동일 클로드 컨텍스트 자기 작성 산출* — 외부 LLM 1+ 의견 권장 (PR-2 풀 3+1 합의 시점) | PR-2 합의 형태 자체 | **MEDIUM** | PR-2 풀 3+1 합의 시점 외부 LLM 1+ 강력 권장 (사용자 명시 결정 영역) |

### 3.2 Gap 통합 정리 (중복 제거 후)

원 23건 → Gap-13/15/19 가 Gap-5/8/6 과 통합 → **유효 Gap 20건**.

심각도 분포:
- **HIGH 1건** (Gap-17 — Hermes 변조 차단 매트릭스)
- **MEDIUM 9건** (Gap-1, 2, 4, 5, 6, 9, 11, 18, 21, 23 — 23 별도 카운트)
- **LOW-MEDIUM 5건** (Gap-3, 8, 10, 12, 22)
- **LOW 5건** (Gap-7, 14, 16, 20)

### 3.3 본 PR-2 차단 사유 여부 종합

- **HIGH 1건 (Gap-17)** = ADR-012 본문 작성 시점 *본문 의무 흡수* — PR-2 차단 사유 가능, 단 *PR-2 산출 명시 6 항목 자체* (사용자 enumeration 답습) 는 차단 0건. ADR-012 본문 충실성 영역.
- **MEDIUM 9건** = 격상 통합 합의 시점 외부 LLM 의견 또는 ADR-012 본문 보강으로 흡수
- **LOW-MEDIUM / LOW 10건** = 후속 갱신 권고

**종합 판정**: 본 PR-2 산출 6 항목 자체는 **APPROVE WITH CONDITIONS** — Gap-17 + Gap-23 이 풀 3+1 합의 시점 외부 LLM 1+ 의견으로 보강 권고.

---

## 4. 권고 조건 (격상 통합 합의 또는 ADR-012 본문 작성 시점 흡수)

### 4.1 본 PR-2 PASS 진입 권고 조건 (4건 강조)

| # | 권고 | 근거 Gap | 심각도 |
|---|---|------|----|
| **C-1** | ADR-012 본문에 **Hermes 변조 차단 매트릭스 4항목** (Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조) 명시 + G3 §2.5 #11 / §4.5 / §2.2 #20 cross-reference | Gap-17 | **HIGH** |
| **C-2** | PR-2 풀 3+1 합의 시점 **외부 LLM 1+ 강력 권장** (G3 §4.4.2 답습) — ADR-012 가 동일 클로드 컨텍스트 자기 작성 산출이므로 자기참조 통제 필수 | Gap-23 | **MEDIUM** |
| **C-3** | ADR-012 본문에 **prev_hash 실패 후보 (1) BLOCK + manual review 채택 명시** + ADR-011 §2.4 T3 cross-reference (자동 revert = T3 위반 차단) | Gap-9 + Gap-4 | **MEDIUM** |
| **C-4** | ADR-012 본문에 **chain 재계산 (full rewrite) 차단 외부 anchor 권고 (GitHub Actions run ID + signed tag)** + G3 §5.5 SPOF cross-reference | Gap-2 + Gap-10 | **MEDIUM** |

### 4.2 보강 권고 (LOW-MEDIUM / LOW Gap, 후속 흡수)

5. **C-5** (Gap-1): +1 확장 필드 명시 + 후보별 trade-off 비교
6. **C-6** (Gap-3): RFC 8785 JCS 본문 인용 + 라이브러리 명시 + 위반 검출 hook
7. **C-7** (Gap-5/13): `event: roundtrip_lossy` 손실 영역별 T1/T2/T3 분류 매트릭스
8. **C-8** (Gap-6/19): P10 신규 위반 경로 명시 + G2 후속 합의 권고
9. **C-9** (Gap-7): Skill `promoted` 진입 시 ledger entry hash 검증 명시
10. **C-10** (Gap-8/15): Layer 1, 2, 4, 5 4중 보호 enumeration + CI 회귀 검증 step 사양
11. **C-11** (Gap-11): 외부 LLM 응답 ledger entry 의무 + hash 검증 명시
12. **C-12** (Gap-12): 의미 보존 review 시 외부 LLM 1+ 권장 (G3 §4.4.2 cross-reference)
13. **C-13** (Gap-14): migration script Hermes 의존 0 강제 메커니즘 cross-reference
14. **C-14** (Gap-16): JCS Informational 트랙 명시 + 미래 fallback 절차
15. **C-15** (Gap-18): "Hermes 안전성 선언 부재" 답습 (ADR-011 §7.3 직접 답습)
16. **C-16** (Gap-20): 11 필드 모두 provider-neutral 강제 명시
17. **C-17** (Gap-21): 수단/목적 분리 4 조건 (a) 비교표 본문 (현 G4 §4.4 ↔ 본 PR-2 강화 chain)
18. **C-18** (Gap-22): 수단/목적 분리 4 조건 (d) 자동 회귀 검증 경로 명시 (R-6 workflow 답습 확장)

---

## 5. 영구 핵심 제약 5건 보호 점검

> 본 §5 는 사용자 명시 답습 5 제약을 본 PR-2 ADR-012 본문 *예상 보호 위치* 와 함께 enumeration. 본 §5 자체는 *합의 보고서 입력* 까지 — ADR-012 본문 작성 권한 영역 *아님*.

### 5.1 Provider Liquidity (헌법 5조 관용)

**본 PR-2 보호 위치**:
- ADR-012 §schema — 11 필드 모두 provider-neutral 강제 (Gap-20 흡수 시)
- ADR-012 §canonical — RFC 8785 JCS = provider-neutral 표준
- ADR-012 §migration — Hermes 의존 0 (depcruise, G4 §4.5.2 cross-reference, Gap-14)

**보호 강도**: **HIGH** (Provider Liquidity 4-way Multi-layer Defense 답습 + ADR-012 가 layer 5 추가 — Evidence 형식 차원)

### 5.2 Hermes ≠ root of trust (ADR-011 §2.3)

**본 PR-2 보호 위치**:
- ADR-012 §Hermes 변조 차단 매트릭스 (Gap-17 흡수 시 — HIGH)
- ADR-012 §주의사항 — "Hermes 안전성 선언 부재" 답습 (Gap-18 흡수 시)
- ADR-012 §검증 — Hermes-originated ledger entry audit log 의무 + G3 §4.5 cross-reference

**보호 강도**: **HIGH** (조건부 — Gap-17, 18 흡수 시)

### 5.3 메타포 강제 금지 (system-identity-prequel §7)

**본 PR-2 보호 위치**:
- Evidence Ledger 는 *기존 구조* (system-identity-prequel §6.3 + G4 §4) 의 ADR 권위화 — *메타포 인플레이션 0건*
- 11 필드 (10+1) 도 *기존 schema 확장* — 메타포 강제 무관

**보호 강도**: **HIGH** (영향 무관 — Evidence Ledger 는 회사 메타포 영역 외)

### 5.4 자동 정책 변경 금지 (T3, ADR-011 §2.4)

**본 PR-2 보호 위치**:
- ADR-012 §prev_hash — 후보 (1) BLOCK + manual review 채택 (Gap-9 흡수 시)
- ADR-012 §검증 — chain 재계산 = T3 위반 검출 + 자동 BLOCK
- ADR-012 §round-trip — 손실 영역별 T1/T2/T3 분류 매트릭스 (Gap-5 흡수 시)

**보호 강도**: **HIGH** (조건부 — Gap-9, Gap-5 흡수 시)

### 5.5 수단/목적 분리 (ADR-011 §2.1 (a)~(d) 4조건)

**본 PR-2 보호 위치**:
- ADR-012 §근거 — (a) 동등 이상 보안 결과 비교표 (현 G4 §4.4 ↔ 본 PR-2 강화 chain) — Gap-21 흡수 시
- (b) 격리 환경 PoC — 본 PR-2 *설계 권위화* 까지, PoC 별도 합의 (Implementation/Runtime PASS 영역)
- (c) ADR 권위 명시 — 본 PR-2 ADR-012 자체로 충족
- (d) 자동 회귀 검증 — R-6 workflow 답습 확장 (Gap-22 흡수 시)

**보호 강도**: **MEDIUM-HIGH** (조건부 — Gap-21, Gap-22 흡수 시. (b) 는 별도 Implementation 영역)

### 5.6 5 제약 종합 매트릭스

| 제약 | 본 PR-2 보호 강도 | 조건 |
|---|----|---|
| Provider Liquidity | HIGH | Gap-20 흡수 |
| Hermes ≠ root of trust | HIGH | Gap-17, 18 흡수 |
| 메타포 강제 금지 | HIGH | (영향 무관) |
| T3 자동 정책 변경 금지 | HIGH | Gap-9, 5 흡수 |
| 수단/목적 분리 | MEDIUM-HIGH | Gap-21, 22 흡수 (b 는 별도) |

**종합**: 5 제약 모두 본 PR-2 *PASS 적격* — 단 Gap 흡수 시 HIGH 5/5 가능.

---

## 6. 본 입력이 *하지 않는* 것

- ❌ Hermes PMO 격상 자동 권유
- ❌ P2 v3 정식 채택 자동 발화
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 권유 (cross-reference 권고 한정)
- ❌ ADR-012 본문 자동 작성 (본 분석은 *Reviewer 종합 판정 입력* 한정)
- ❌ G4 §4.4 / §4.6 본문 자동 갱신 (PR-2 본문 작성 권한 영역)
- ❌ G2 §1.2 P10 신규 row 자동 추가 (G2 본문 변경 = PR-2 범위 외, 사용자 명시 답습)
- ❌ archive 자동 처리 (P2 v2 / system-identity-prequel)
- ❌ 실 runtime 코드 / migration script / hash chain 검증 hook 코드
- ❌ Tier-1/2/3 catalog 자동 확장
- ❌ 다른 Agent (A, C) 출력 참조
- ❌ Reviewer 종합 합의 결과 발화 (본 분석은 *Phase 2 독립 분석* 한정)
- ❌ 외부 LLM 의견 위조 또는 모방
- ❌ 본 분석 자체의 자기 검증 (자기참조 위험 통제는 *외부 LLM 1+ 의견* 영역, Gap-23)

---

## 7. 최종 판정

### 7.1 종합 판정

**APPROVE WITH CONDITIONS**

### 7.2 판정 근거

#### APPROVE 영역 (조건 없이 적격)

1. **ADR-012 신규 발행 자체** — system-identity-prequel §6.4 명시 후속 작업 + Hermes ≠ root of trust 권위 위계 (ADR-011 §2.3) 와 동급 격상의 *권위 격상 자체는 정당*
2. **Provider Liquidity 보호 무결성** — 11 필드 + JCS + migration 모두 provider-neutral 강제로 4-way Multi-layer Defense 에 layer 5 추가 (Evidence 형식 차원)
3. **메타포 강제 금지 답습** — Evidence Ledger = 기존 구조 ADR 권위화, 메타포 인플레이션 0건
4. **수단/목적 분리 4 조건 (c) ADR 권위 명시 충족** — 본 PR-2 ADR-012 자체로 정합
5. **G4 §4.4 / §4.6 보강 자체 정합성** — G4 §11.4 P-1 "PR-2 풀 3+1 시 §4.4 본문에 RFC 8785 JCS 명시 인용" 명시 답습 = PR-2 가 정확히 P-1 처리

#### CONDITIONS (격상 통합 합의 또는 ADR-012 본문 작성 시점 흡수 권고)

**HIGH 1건**:
1. **C-1 (Gap-17)**: ADR-012 본문에 **Hermes 변조 차단 매트릭스 4항목** 명시 + G3 §2.5 #11 / §4.5 / §2.2 #20 cross-reference

**MEDIUM 3건**:
2. **C-2 (Gap-23)**: PR-2 풀 3+1 합의 시점 **외부 LLM 1+ 강력 권장** (G3 §4.4.2 답습) — *사용자 명시 결정 영역*
3. **C-3 (Gap-9 + Gap-4)**: ADR-012 본문에 **prev_hash 실패 후보 (1) BLOCK + manual review 채택 명시** + ADR-011 §2.4 T3 cross-reference
4. **C-4 (Gap-2 + Gap-10)**: ADR-012 본문에 **chain 재계산 차단 외부 anchor (GitHub Actions run ID + signed tag) 권고** + G3 §5.5 SPOF cross-reference

#### NOTES (LOW-MEDIUM / LOW Gap, 후속 권고 — C-5 ~ C-18, §4.2 enumeration)

14건 (Gap-1, 3, 5, 6, 7, 8, 11, 12, 14, 16, 18, 20, 21, 22) — 격상 통합 합의 또는 정식 채택 시점 흡수 권고.

### 7.3 본 판정의 *발화하지 않는* 것

- ❌ ADR-012 발행 자동 발화 (Reviewer 종합 합의 + 사용자 명시 결정 영역)
- ❌ G4 §4.4 / §4.6 본문 자동 갱신 (PR-2 본문 작성 권한 영역)
- ❌ Hermes PMO 격상 자동 발화
- ❌ P2 v3 정식 채택 자동 발화
- ❌ G2 §1.2 P10 신규 row 자동 추가
- ❌ ADR-008 / ADR-011 본문 자동 갱신
- ❌ archive 자동 처리
- ❌ 실 hook / migration / runtime code 작성

본 판정은 **Reviewer 의 종합 합의 보고서 입력** 한정. 최종 PR-2 합의 형태 + 외부 LLM 1+ 의견 형식 + ADR-012 본문 작성 + G4 §4.4/§4.6 본문 보강은 **사용자 명시 결정 + Reviewer 종합 + ADR-012 본문 작성 합의** 영역.

### 7.4 핵심 Gap 1줄 요약

**Gap-17 (HIGH)**: ADR-012 본문에 Hermes 변조 차단 매트릭스 4항목 (Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조) 명시 + G3 §2.5 #11 / §4.5 / §2.2 #20 cross-reference 의무.

---

**작성일**: 2026-05-09
**Agent B 판정**: **APPROVE WITH CONDITIONS** (4 CONDITIONS — C-1 HIGH / C-2~C-4 MEDIUM, 14 NOTES)
**다음 단계 (Agent B 권고)**: Reviewer 가 Agent A / C 출력 종합 + 본 판정 + 20 Gap + PR-2 풀 3+1 합의 시점 외부 LLM 1+ 강력 권장 (G3 §4.4.2 답습) — 본 PR-2 합의 형태 결정 + ADR-012 본문 작성 권한은 사용자 명시 결정 영역
**금지 (본 분석 영구 답습)**:
- ❌ Hermes PMO 격상 자동 권유
- ❌ P2 v3 정식 채택 자동 발화
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
- ❌ ADR-012 본문 자동 작성
- ❌ G4 §4.4 / §4.6 본문 자동 갱신
- ❌ G2 §1.2 P10 신규 row 자동 추가
- ❌ archive 자동 처리
- ❌ 실 runtime code / migration script 작성
- ❌ Tier-1/2/3 catalog 자동 확장
- ❌ 다른 Agent (A, C) 출력 참조
