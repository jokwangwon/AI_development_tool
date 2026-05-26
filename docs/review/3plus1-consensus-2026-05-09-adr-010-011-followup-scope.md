# ADR-010 / ADR-011 후속 보강 필요 여부 검토 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 ("우선 Reviewer-only 단축 검토로 진행 ... 6 트리거 1+ 발화 시 풀 3+1 승격")
**합의 일자**: 2026-05-09 (후속 14 — ADR-010 / ADR-011 후속 보강 필요 여부 확인)
**검토 대상**: ADR-010 (`docs/decisions/ADR-010-sqlcipher-vault-key-management.md`) + ADR-011 (`docs/decisions/ADR-011-means-vs-ends-redaction.md`) — **추가 보강 필요 여부 검토** (본 검토 = 검토만, 본문 수정 X)
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — 분기 A 채택: ADR-010 / ADR-011 추가 보강 *불필요*. 후속 10 cross-reference 갱신 + ADR-008 부록 C (후속 13) 신설로 충족 — Implementation/Runtime PASS 작업 진입 적격**

---

## 0. 사전 점검

### 0.1 가동 사유

ADR-008 부록 C 신설 (2026-05-09 후속 13) 완료 후속 — Implementation/Runtime PASS 작업 진입 *전* ADR-010 / ADR-011 정렬 검증. 사용자 명시 작업명 = "ADR-010 / ADR-011 후속 보강 필요 여부 확인 (후보 #2)".

**사용자 명시 결정 답습** (2026-05-09 후속 13 후속):
- 작업명 = "ADR-010 / ADR-011 후속 보강 필요 여부 확인"
- 목적 = "Implementation/Runtime 작업 진입 *전* ADR-010 / ADR-011 정렬 검증"
- 작업 단계 = **본문 수정 X, 보강 필요 여부 검토만**
- 검토 형태 = Reviewer-only 단축 검토 우선 — 6 풀 3+1 승격 트리거 1+ 발화 시 풀 3+1 승격
- 분기:
  - A. 보강 불필요 → Implementation/Runtime PASS 작업 착수
  - B. 경미한 cross-reference 보강 필요 → 보강 commit 후 Implementation/Runtime 작업 착수
  - C. 원칙 변경 필요 → 풀 3+1 합의로 승격

### 0.2 단축 채택 사유

본 검토는 다음 단축 합의 충분 조건 모두 충족:

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (검토만, 본문 수정 X) | ✅ 사용자 명시 답습 |
| 직전 합의 (ADR-008 부록 C 신설, 후속 13) 패턴 답습 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **6 풀 3+1 승격 트리거 발화 0건** | ✅ §3 답습 |

### 0.3 메타 편향 인지 (G3 §4.7 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-010 / ADR-011 작성자 + 후속 10 / 후속 13 갱신 검토자와 동일 패밀리. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘**:
1. 사후 외부 LLM 충족 — P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업
2. 격상 전 면제 — Hermes PMO 격상 *전*
3. 합의 권위 내부 변경 — 본 검토 = 후속 10 + 후속 13 답습 = *권위 내부* 작업
4. 자기 작성 한계 명시 — 본 §0.3 + §4 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ |
| Implementation/Runtime PASS 선언 | ❌ |
| G2 / G3 / G4 Implementation PASS 선언 | ❌ |
| **ADR-010 / ADR-011 본문 자동 수정** | ❌ 사용자 명시 금지 (본 검토 = 보강 필요 여부 검토만) |
| 실 runtime code / migration script / hook 구현 | ❌ |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |

---

## 1. ADR-010 5 확인 항목 평가

### 1.1 항목 1 — Evidence Ledger DB 가 SQLCipher / Vault HSM 보호 범위에 명확히 포함되어 있는가

**현 권위 출처**: ADR-010 §관련 문서 영역 — **Evidence Ledger DB Secret 처리 주의 사항** (후속 10 A13 신설, 2026-05-09 후속 10):

> 본 ADR-010 의 SQLCipher Vault 보호 범위는 다음을 *명시 포함* 의무:
> - Hermes SQLite (FTS5 학습루프 DB)
> - Memory DB (Global / Project — G4 §2 답습)
> - Skill DB (G4 §3 답습)
> - **Evidence Ledger DB** (`docs/evidence/ledger.jsonl` 또는 후속 SQLite migration 시점 — ADR-012 §원칙 5 답습)

→ **명확히 포함됨** (후속 10 A13 명시). **충족**.

### 1.2 항목 2 — Hermes SQLite / Memory DB / Skill DB / Evidence Ledger DB 의 secret 처리 범위가 충분한가

**현 권위 출처**: ADR-010 후속 10 A13 + ADR-012 §1.4 cross-reference + 외부 LLM 2 C-1 권고 답습 — Evidence Ledger entry 가 redacted secret evidence (예: secret_scan event 의 redacted secret pattern) 포함 가능 시 본 ADR-010 GP-1 보호 범위에 ledger DB 명시 포함 의무.

**보호 범위 매트릭스**:

| DB | SQLCipher 암호화 | Vault HSM 키 관리 | 권위 |
|----|----|----|----|
| Hermes SQLite (FTS5 학습루프) | ✅ | ✅ | ADR-010 §결정 §핵심 메커니즘 |
| Memory DB (Global / Project) | ✅ | ✅ | ADR-010 §관련 문서 §A11 (G4 §2 답습) |
| Skill DB | ✅ | ✅ | ADR-010 §관련 문서 §A11 (G4 §3 답습) |
| **Evidence Ledger DB** | ✅ | ✅ | ADR-010 §관련 문서 §A13 + ADR-012 §원칙 5 답습 |

→ **4 DB 모두 보호 범위 명시 충족**. **추가 보강 불필요**.

### 1.3 항목 3 — key rotation / backup / export / JSONL artifact 와 충돌이 없는가

**현 권위 출처**:
- ADR-010 §결정: Vault HSM + Shamir SSS 3-of-3 + **90일 자동 회전 + dual-key 운영** + PGP 봉인 백업 + 시간별 incremental + 일일 full + sample restore 분기 1회
- G4 §4.2 JSONL 11 필드 schema (export format)
- G4 §4.5 변환 스크립트 사양 (`scripts/hermes-migration/*.py`)
- ADR-012 §2.10 JSONL Export/Import 무결성 + Migration 검증 실패 rollback

**충돌 검증**:

| 영역 | ADR-010 | G4 / ADR-012 | 충돌 |
|----|----|----|----|
| Key rotation 90일 + dual-key | ADR-010 §결정 | (해당 없음 — G4 / ADR-012 는 형식 차원, 키 차원 무관) | ❌ 0 |
| Backup (시간별 incremental + 일일 full + PGP 봉인) | ADR-010 §결정 | G4 §4.4 hash chain + git append-only branch (Layer 2) — 보완 (ADR-010 키 백업 + Layer 2 history 백업) | ❌ 0 (보완 관계) |
| Export (JSONL artifact) | (해당 없음 — 키는 export 대상 아님) | G4 §4.1 JSONL 표준 + ADR-012 §2.10 Export 무결성 | ❌ 0 |
| JSONL artifact 와 SQLCipher 디스크 암호화 책임 경계 | ADR-010 = 디스크 암호화 (DB 파일) | G4 / ADR-012 = export 형식 (JSONL) | ❌ 0 (책임 경계 명확) |

→ **충돌 0건**. **추가 보강 불필요**.

### 1.4 항목 4 — ADR-012 hash chain / Evidence Ledger 와 ADR-010 의 암호화 책임 경계가 명확한가

**책임 경계 매트릭스**:

| 책임 영역 | ADR-010 (SQLCipher Vault) | ADR-012 (Evidence Ledger Protection) |
|----|----|----|
| 디스크 암호화 (DB 파일) | ✅ Primary | ❌ (해당 없음) |
| 키 관리 (Vault HSM + Shamir SSS) | ✅ Primary | ❌ |
| Hash chain (sha256 + canonical JSON) | ❌ | ✅ Primary |
| Append-only (git layer) | ❌ | ✅ Primary (Layer 2) |
| Signed commit (GPG/SSH) | ❌ | ✅ Primary (Layer 3) |
| Canonical JSON (RFC 8785 JCS) | ❌ | ✅ Primary |
| prev_hash 검증 실패 BLOCK | ❌ | ✅ Primary |
| Full Rewrite 5 Layer 방어 | ❌ | ✅ Primary |
| External anchor (RECOMMENDED) | ❌ | ✅ Primary (Layer 5) |
| Provider Liquidity 5-way Layer 5 (Evidence 형식) | ❌ | ✅ Primary (§원칙 6) |
| Evidence Ledger DB *secret 평문 저장 차단* (P1 변종) | ✅ Primary (GP-1 SQLCipher trigger 보호 범위 ledger DB 명시 포함) | ❌ (해당 없음 — 형식적 무결성 까지) |
| Hermes 변조 차단 매트릭스 4항목 | ❌ | ✅ Primary (§2.12) |

→ **책임 경계 매우 명확**. ADR-010 = *디스크 암호화 + 키 관리*, ADR-012 = *형식적 무결성*. 후속 10 A13 명시로 *Evidence Ledger DB secret 처리 책임 경계* 도 명확. **추가 보강 불필요**.

### 1.5 항목 5 — Implementation/Runtime PASS 로 오해될 문구가 없는가

ADR-010 §결정 본문 + 후속 10 A10~A13 cross-reference 갱신 검증:

| 영역 | Implementation PASS 오해 위험 |
|----|----|
| ADR-010 §결정 §핵심 메커니즘 (Vault HSM + Shamir SSS 등) | ❌ 0 (Implementation PASS 명시 부재 — *결정* 까지만) |
| ADR-010 §관련 문서 (후속 10 A10~A13 cross-reference) | ❌ 0 (P2 v2 Archived / P2 v3 Adopted / ADR-012 / Evidence Ledger DB Secret 처리 모두 *cross-reference 한정*) |
| ADR-010 §운영 인프라 요구사항 | ❌ 0 (Vault 인프라 *요구사항* 까지, 실 deploy 명시 부재) |

→ **오해 표현 0건**. **추가 보강 불필요**.

### 1.6 ADR-010 종합 평가

**5/5 항목 모두 충족** — **추가 보강 *불필요***. 후속 10 A10~A13 cross-reference 갱신 + ADR-012 §원칙 5 + 외부 LLM 2 C-1 권고 답습으로 충분.

---

## 2. ADR-011 5 확인 항목 평가

### 2.1 항목 1 — 수단/목적 분리 원칙이 ADR-012 / ADR-009 C-N / P2 v3 Adopted 이후에도 충분히 최신인가

**현 권위 출처**: ADR-011 §2.1 (a)~(d) 4조건 + (e) 합의 APPROVE 5조건 패턴.

**최신성 검증** (후속 10 A20 / A21 / A23 답습):

| 후속 작업 | ADR-011 §2.1 (a)~(e) 답습 |
|----|----|
| ADR-012 발행 (2026-05-09 후속 3 PR-2) | ✅ 직접 답습 — ADR-012 §4 (a)~(e) 5조건 명시 답습 |
| ADR-009 C-N 갱신 (2026-05-09 후속 4) | ✅ §5 Provider Liquidity 5-way Multi-layer Defense Layer 1 모법 ADR — ADR-011 §2.1 (a)~(d) 패턴 답습 |
| P2 v3 정식 채택 (2026-05-09 후속 6) | ✅ §3.3 G1b / §4.3 G2 / §5.4 G3 / §6.4 G4 Exit (a)~(e) 5조건 패턴 답습 |
| G2 §1.2.6 P10 (2026-05-09 후속 5) | ✅ ADR-012 §1.4 + Hermes 변조 차단 매트릭스 4항목 답습 |
| ADR-008 부록 C (2026-05-09 후속 13) | ✅ §C.4 자동 격상 절대 금지 (5 layer 다중 차단) — ADR-011 §2.4 T3 답습 |

→ **수단/목적 분리 원칙 = 모든 후속 작업의 모법 권위로 영구 답습**. **최신성 충족**. **추가 보강 불필요**.

### 2.2 항목 2 — 권위 위계가 P2 v2 archive / prequel archive 이후에도 명확한가

**현 권위 출처**: ADR-011 §2.3 (Hermes ≠ root of trust 영구 권위) + system-identity-prequel §3 → ADR-011 §2.3 영구 승격 답습 (직접 명시: "prequel 폐기 후에도 보존").

**Archive 이후 권위 검증** (후속 10 A14 + 후속 7/8 답습):

- P2 v2 Archived (2026-05-09 후속 7) → ADR-008 부록 B Amendment + 본 ADR-011 §2.3 권위 *외부* 보존 (ADR-011 §6.2 + §8.5 + §8.1 명시)
- system-identity-prequel Archived (2026-05-09 후속 8) → 본 ADR-011 §2.3 / §2.4 영구 권위 승격 *직접 명시* 답습으로 archive 후 권위 보존 (후속 10 A14 명시)
- 옵션 A 최소 침습 채택 (path 변경 0건) → cross-reference 깨짐 0건

→ **권위 위계 = archive 이후에도 영구 명확**. **추가 보강 불필요**.

### 2.3 항목 3 — T1/T2/T3 정책이 ADR-008 부록 C / ADR-012 / G2/G3/G4 와 충돌하지 않는가

**T1/T2/T3 정책 충돌 검증**:

| 후속 작업 | T1/T2/T3 정책 답습 | 충돌 |
|----|----|----|
| ADR-008 부록 C §C.4 자동 격상 절대 금지 | T3 자동 변경 금지 직접 답습 | ❌ 0 |
| ADR-012 §원칙 9 (prev_hash 검증 실패 = BLOCK + manual, 자동 revert 금지) | T3 답습 | ❌ 0 |
| ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) + §3.0 (v2.0 트리거 vs MVP) | T2 사용자 승인 + T3 자동 금지 답습 | ❌ 0 |
| G2 §1.2.6 P10 정식 등록 | T3 영역 (Evidence Forgery — 자동 정책 변경 위장) | ❌ 0 |
| G3 §1.3 + §5 (Evidence decision principle: PASS 성립 4 요건) | T2 사용자 명시 승인 답습 | ❌ 0 |
| G3 §2 권한 22 항목 (T1 8 / T2 2 / T3 12) | 본 ADR-011 §2.4 T1/T2/T3 직접 답습 | ❌ 0 |
| G4 §2.5 promotion T2 강제 + §3.4 Skill 자동 승격 금지 + §5.2 4 금지 | T2 사용자 승인 + T3 영역 답습 | ❌ 0 |

→ **T1/T2/T3 정책 = 모든 후속 작업과 충돌 0건**. **추가 보강 불필요**.

### 2.4 항목 4 — Hermes PMO 격상 절차가 ADR-011 원칙과 연결되어 있는가

**현 권위 출처**: ADR-008 부록 C §C.6 (8 권위 layer 답습) — ADR-011 §2.3 (Hermes ≠ root of trust) + §2.4 (T1/T2/T3) 영구 권위 직접 답습.

**연결 검증**:

- ADR-008 부록 C §C.4 5 layer 다중 차단 매트릭스 — ADR-011 §2.4 T3 자동 금지 (Layer 1) 직접 답습
- ADR-008 부록 C §C.5 분리 매트릭스 — ADR-011 §2.3 (Hermes ≠ root of trust) 답습
- ADR-008 부록 C §C.6 ADR-013 보류 사유 8 권위 layer — ADR-011 §2.3 + §2.4 명시 (#6 + #7)
- ADR-008 부록 C §C.7 cross-reference 매트릭스 — ADR-011 §2.3 + §2.4 직접 답습

→ **Hermes PMO 격상 절차 ↔ ADR-011 원칙 연결 명확**. **추가 보강 불필요**.

### 2.5 항목 5 — 자동 정책 변경 금지 원칙이 Implementation/Runtime 작업 진입 *전*에 충분히 강제되어 있는가

**현 권위 출처**: ADR-011 §2.4 T3 + ADR-012 §원칙 9 + ADR-008 부록 C §C.4 5 layer 다중 차단 매트릭스 + G3 §2.5 #11 / §4.5 / §2.2 #20.

**5 layer 다중 차단 매트릭스** (ADR-008 부록 C §C.4 답습):

| Layer | 차단 매커니즘 | 권위 |
|----|----|----|
| 1 | ADR-011 §2.4 T3 (Constitution / ADR / Harness Gates 정의 자체 변경 자동 금지) | ADR-011 영구 |
| 2 | ADR-012 §원칙 9 (prev_hash 검증 실패 = BLOCK, 자동 복구/자동 revert 금지) | ADR-012 영구 |
| 3 | ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 — 자기 격상 시도 차단) | ADR-009 영구 |
| 4 | ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목 — Hermes-originated commit auto-reject) | ADR-012 영구 |
| 5 | G3 §2.5 #11 + §4.5 + §2.2 #20 (filesystem ACL + audit log + commit auto-reject) | G3 영구 |

**Implementation/Runtime 작업 진입 *전* 자동 정책 변경 금지 강제 영역**:

| 영역 | 강제 매커니즘 |
|----|----|
| G2 GP-2 ~ GP-6 PoC + CI 강제 | Layer 1 (T3) + Layer 5 (G3 §2.5 #11 — `governance-preconditions.md` filesystem ACL) |
| G3 runtime hook / wrapper | Layer 1 (T3) + Layer 5 (G3 §2.5 #11 — `hermes-not-root-of-trust-runtime.md` filesystem ACL) |
| G4 migration script + round-trip PoC | Layer 1 (T3) + Layer 4 (Hermes 변조 차단) + Layer 5 (G3 §2.5 #11 — `provider-agnostic-memory-skill-design.md` filesystem ACL) |
| ADR-012 CI enforcement | Layer 2 (prev_hash BLOCK) + Layer 4 (Hermes-originated commit auto-reject) |
| ADR-009 T1~T4 trigger detection task | Layer 1 (T3) + Layer 3 (Hermes PMO ↔ provider 분리) |

→ **5 layer 다중 차단 매트릭스 = Implementation/Runtime 작업 진입 *전* 자동 정책 변경 금지 영구 강제**. **추가 보강 불필요**.

### 2.6 ADR-011 종합 평가

**5/5 항목 모두 충족** — **추가 보강 *불필요***. 후속 10 A14~A25 cross-reference 갱신 + ADR-008 부록 C §C.4~§C.7 cross-reference + 후속 작업 모두 ADR-011 §2.1 (a)~(e) + §2.3 + §2.4 답습으로 충분.

---

## 3. 6 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **ADR-010 키 관리 원칙 변경 필요** | ADR-010 5/5 항목 충족 (§1.6) — 보강 *불필요*. 키 관리 원칙 (Vault HSM + Shamir SSS / 90일 회전 / dual-key) 변경 0건 | ❌ 0 |
| 2 | **ADR-011 수단/목적 분리 원칙 변경 필요** | ADR-011 5/5 항목 충족 (§2.6) — 보강 *불필요*. (a)~(d) 4조건 + (e) 합의 APPROVE 패턴 변경 0건 | ❌ 0 |
| 3 | **T1/T2/T3 정책 변경 필요** | §2.3 T1/T2/T3 정책 = 모든 후속 작업과 충돌 0건 — 정책 변경 0건 | ❌ 0 |
| 4 | **5 영구 핵심 제약 약화 가능성** | 본 검토 = 보강 필요성 검토만. 5 영구 핵심 제약 약화 0건 (cross-reference 충족 점검 한정) | ❌ 0 |
| 5 | **Evidence Ledger / SQLCipher / Vault HSM 책임 경계 충돌** | §1.4 (책임 경계 매트릭스) — ADR-010 = 디스크 암호화 + 키 관리, ADR-012 = 형식적 무결성. 후속 10 A13 명시로 책임 경계 명확. 충돌 0건 | ❌ 0 |
| 6 | **Hermes PMO 격상 오해 표현** | 본 검토 = 보강 필요 여부 검토만, 본문 수정 0건. ADR-008 부록 C §C.1 (의미 명시) + §C.4 (자동 격상 절대 금지) 답습 — 격상 오해 0건 | ❌ 0 |

→ **6/6 트리거 0건 발화** → **단축 합의 적격** 확정.

---

## 4. 메타 편향 자기진단

### 4.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-010 / ADR-011 작성자 + 후속 10 / 후속 13 갱신 검토자와 동일 컨텍스트 패밀리. 자기 작성 산출 자기 검토 한계 인지.

### 4.2 본 한계의 청산 (G3 §4.7 답습)

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 — 본 검토 = *보강 필요 여부 검토만*, 별도 외부 LLM 회수 *불필요* |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 검토 자체가 *Implementation/Runtime 작업 진입 전 정렬 검증* |
| 3 | 합의 권위 내부 변경 | 본 검토 = 후속 10 + 후속 13 + ADR-008 부록 C §C.4 답습 = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §4 명시 |

### 4.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 ADR-010 5 항목 + ADR-011 5 항목 + 6 트리거 + 분기 A/B/C 모두 §0 + §1 + §2 + §3 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 5 항목 (ADR-010) + §2 5 항목 (ADR-011) + §3 6 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §2.3 T1/T2/T3 충돌 검증 |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §2.1 (a)~(e) 5조건 답습 검증 |
| 5 | 본 검토가 *하지 않는* 것 명시 (§0.4 + §5.2) | ✅ 명시 |

### 4.4 본 단축 합의가 *하지 않는* 것

§5.2 답습.

---

## 5. 결론

```
✅ APPROVE (단축 합의, Reviewer-only) — 분기 A 채택: ADR-010 / ADR-011 추가 보강 *불필요*
```

본 결론은 **ADR-010 / ADR-011 후속 보강 필요 여부** 의 *추가 보강 불필요 + Implementation/Runtime PASS 작업 진입 적격* 한정. **본 검토 = 보강 필요 여부 검토만, 본문 수정 X**.

### 5.1 본 합의가 *발생시키는* 것

- ✅ ADR-010 5/5 항목 충족 평가 (Evidence Ledger DB 보호 범위 / secret 처리 / key rotation·backup·export 충돌 / 책임 경계 / Implementation PASS 오해 표현)
- ✅ ADR-011 5/5 항목 충족 평가 (수단/목적 분리 최신 / 권위 위계 archive 후 명확 / T1/T2/T3 충돌 / Hermes PMO 격상 절차 연결 / 자동 정책 변경 금지 강제)
- ✅ 6/6 풀 3+1 승격 트리거 0건 발화 — 단축 합의 적격
- ✅ **분기 A 채택**: ADR-010 / ADR-011 추가 보강 *불필요*
- ✅ **Implementation/Runtime PASS 작업 진입 적격** — 후속 10 cross-reference 갱신 + ADR-008 부록 C 신설로 충족
- ✅ ADR-010 책임 경계 매트릭스 명시 (디스크 암호화 + 키 관리) vs ADR-012 (형식적 무결성)
- ✅ 5 layer 다중 차단 매트릭스 — Implementation/Runtime 작업 진입 *전* 자동 정책 변경 금지 영구 강제 명시

### 5.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ G2 / G3 / G4 Implementation PASS 자동 선언
- ❌ **ADR-010 / ADR-011 본문 자동 수정** (사용자 명시 금지)
- ❌ 실 runtime code / migration script / hook 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 분기 B (경미 cross-reference 보강) 자동 채택
- ❌ 분기 C (원칙 변경 풀 3+1 승격) 자동 채택

### 5.3 다음 진입점 (사용자 결정 영역)

본 검토 APPROVE → 분기 A 채택 → **Implementation/Runtime PASS 작업 착수 적격** (사용자 결정 영역):

1. **G2 GP-2 ~ GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수** (다음 진입점) — 각 별도 합의 (ADR-011 §2.1 (a)~(e) 5조건 + R-2/R-4.1 PoC 패턴 답습)
2. **Hermes PMO 격상 적격성 검토** = **4 게이트 Implementation/Runtime PASS 이후로 보류** (사용자 명시 답습)
3. **외부 LLM cross-vendor 추가 의뢰** (예: 다른 비-Claude vendor) — Implementation/Runtime PASS PoC 후속 영역

**권고 시작 명령**:
- "G2 GP-2 ~ GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수해주세요"
- 또는 사용자 결정에 따라 G2 / G3 / G4 별 우선순위 분리 (예: "G2 GP-2 PoC 진입해주세요" / "G3 runtime hook 설계 진입해주세요" / "G4 migration script PoC 진입해주세요")

---

**합의 commit 권위**: 본 commit (`docs(review): record ADR-010/011 followup scope short consensus APPROVE — branch A`)
**본 commit + housekeeping commits = 본 세션 후속 14 (ADR-010/011 후속 보강 검토) 완료**
**다음 세션 진입점**: G2 GP-2~GP-6 / G3 / G4 Implementation/Runtime PASS 작업 착수 (분기 A 답습)
