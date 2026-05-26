# ADR-010: SQLCipher 키 관리 — Vault HSM + Shamir SSS

**상태**: 승인 (P2 3+1 합의 D-4 결정 + Reviewer 권고)
**날짜**: 2026-05-04
**의사결정자**: 사용자 + 3+1 에이전트 합의

---

## 맥락 (Context)

P2 (`hermes-adoption-design.md` v2, **Archived 2026-05-09 후속 7** — 후속 권위 = `hermes-adoption-design-v3.md` (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6**)) 의 차단조건 #1 SQLCipher 암호화에서 키 관리 방식 결정 필요.

P2 3+1 합의에서 Agent B가 단독 발견한 **CRITICAL 위험 B-N2**: "SQLCipher 키 유출 시 redaction된 모든 과거 데이터 노출". 1일 데이터 손실 수용은 **키 자체 분실** 시나리오만 고려하며, **키 유출** 시나리오는 미커버.

3+1 합의 D-4 미해결 결정:
- (a) `ssss` 라이브러리만
- (b) **Vault HSM** ⭐ Reviewer 권고
- (c) 자체 회피 (LUKS 디스크 암호화만)

사용자 결정: **(b) Vault HSM 채택**. 단 Reviewer는 "외부 의존 추가 → 별도 ADR 권장"이라 본 ADR 작성.

## 결정 (Decision)

**SQLCipher 키 관리에 Vault HSM (또는 동등 secret manager) 채택 + Shamir's Secret Sharing 3-of-3 분할**.

### 핵심 메커니즘

1. **Vault HSM**: 키 저장·접근 제어·감사 로그·회전 자동화
2. **Shamir's Secret Sharing 3-of-3**: 마스터 키를 3분할 — 단일 분실 시 즉시 손실 방지 (3-of-3은 모든 분할 필요, 더 안전. 운영 부담 시 2-of-3 검토 가능)
3. **90일 자동 회전 + dual-key 운영**: 회전 중 무중단 (구 키 + 신 키 동시 유효 24시간)
4. **PGP 봉인 백업**: 별도 저장소에 봉인된 분할 키 (Vault 자체 장애 대비)
5. **시간별 incremental + 일일 full 백업** (P2 §2.2.1)
6. **Sample restore 검증**: 분기 1회 의무화 (백업 무결성 확인)

### 키 라이프사이클

```
[생성]
  Vault에서 256-bit 마스터 키 생성
  → Shamir SSS 3-of-3 분할 (3개 share)
  → share 1: Vault 저장
  → share 2: PGP 봉인 → 별도 저장소 (예: 외부 S3 + 별도 권한)
  → share 3: PGP 봉인 → 오프라인 (예: 물리 매체)

[사용]
  Hermes 컨테이너 시작 시:
    → Vault에 인증 (App Role 또는 Kubernetes Auth)
    → share 1 fetch
    → share 2 fetch (PGP 복호 — 운영자 GPG 키 필요)
    → share 3는 일상 사용 안 함 (재해 복구용)
    → 3-of-3 결합 → 마스터 키 → SQLCipher key

[회전 (90일)]
  Day 0: 신 마스터 키 생성 + Shamir 분할 + dual-key 운영 시작
  Day 1: SQLCipher PRAGMA rekey (구 → 신)
  Day 1: dual-key 24시간 (롤백 가능)
  Day 2: 구 키 폐기 + 백업 마이그레이션
  Day 90: 다음 회전

[백업]
  시간별: incremental (현재 키로 암호화)
  일일: full (현재 키로 암호화)
  분기: 일일 백업 1개 무작위 복구 시연 (sample restore)

[키 분실 복구]
  Step 1: PGP 봉인 share 2 복원
  Step 2: 오프라인 share 3 복원
  Step 3: Vault share 1 (가능하면) 또는 백업 share 1
  Step 4: 3-of-3 결합 → 마스터 키 복원
  Step 5: Vault 재초기화
  Step 6: 시간별 incremental로 최신 상태 (최대 1시간 손실)

[키 유출 (B-N2)]
  Step 1: 즉시 회전 (90일 주기 무관)
  Step 2: 구 키 즉시 폐기
  Step 3: 모든 백업 신 키로 재암호화
  Step 4: Vault audit log 분석 (누가 언제 접근했는가)
  Step 5: 사고 보고서 + 헌법 8조 사고 처리
```

## 선택지 (Options Considered)

### A. ssss 라이브러리만 (D-4 옵션 a)
- **장점**: 외부 의존 0, 단순
- **단점**: 키 저장·접근 제어·감사 로그·회전 자동화 모두 자체 구현 필요. Vault 수준 보안 어려움
- **결과**: B-N2 (키 유출) 위험에 대한 운영 도구 부재. 부적합

### B. Vault HSM + Shamir SSS ⭐ 채택
- **장점**:
  - 키 저장·접근 제어·감사 로그·회전 자동화 모두 Vault 자체 제공
  - Shamir SSS로 단일 분실/유출 즉시 손실 방지
  - HSM (Hardware Security Module) 옵션으로 키 자체가 메모리에 노출되지 않음
  - PGP 봉인 백업으로 Vault 자체 장애 대비
- **단점**:
  - Vault 운영 부담 (별도 인프라)
  - PGP 키 관리 부담 (운영자 GPG 등록·회전)
  - 3-of-3 결합 부담 (자동화 필요)
- **결과**: B-N2 위험 충분 완화 + ADR-008 차단조건 #1 강화

### C. 자체 회피 — LUKS 디스크 암호화만 (D-4 옵션 c)
- **장점**: 외부 의존 0, 운영 단순
- **단점**:
  - 디스크 단위 보호만 (메모리/스왑 노출 가능)
  - 컨테이너 내부에서는 평문 → Hermes 코드 결함 시 노출
  - 헌법 제8조 보안 우선 원칙 부분 위반 가능
- **결과**: 키 분실은 막으나 키 유출 미해결. 부적합

## 근거 (Rationale)

3+1 합의에서 Agent B가 단독 발견한 CRITICAL B-N2가 본 ADR의 핵심 동기. P2의 "1일 데이터 손실 수용"은 키 분실만 고려, 키 유출은 별도 처리 필요. Vault HSM + Shamir 조합이 다음을 동시 충족:
- 단일 분실 즉시 손실 방지 (Shamir 3-of-3)
- 키 유출 시 즉시 회전 + 감사 로그 (Vault)
- Vault 자체 장애 대비 (PGP 봉인)
- 헌법 제8조 보안 우선 원칙 강화

운영 부담은 자동화 + Phase 1 작업 일정 (3~4주)에 흡수 가능 (P2 §4.2 Week 1).

## 3+1 에이전트 합의 결과

P2 합의 D-4 결정 사항. 별도 ADR 작성 의무는 Reviewer 권고.

| 출처 | 핵심 |
|------|------|
| Agent B | "SQLCipher 키 유출 → 학습루프 전체 평문화 (CRITICAL B-N2). Shamir 분할, HSM/vault 의존, 키 사용 감사 로그 의무" |
| Reviewer | "Vault 채택 시 외부 의존 추가 → 별도 ADR 권장" |

## 결과 (Consequences)

### 긍정적
- B-N2 (CRITICAL) 위험 충분 완화
- ADR-008 차단조건 #1 강화 (단순 SQLCipher → Vault HSM + Shamir)
- 헌법 제8조 보안 우선 원칙 강화
- 키 회전·감사 자동화 (운영 부담 ↓)
- Vault 자체 장애에도 PGP 봉인으로 복구 경로 보존

### 부정적
- Vault 운영 인프라 추가 (vault.internal endpoint, 인증 정책)
- PGP 키 관리 부담 (운영자 GPG 등록·회전)
- 3-of-3 결합 자동화 코드 필요 (~100 LOC)
- Sample restore 분기 의무화 → 운영 시간 +2시간/분기
- Vault 자체가 새 단일 실패 지점 가능성 (단 PGP 봉인으로 완화)

### 주의 사항
- **Vault 자체 보안**: Vault root token 관리, App Role 정책, audit log 모니터링 필수
- **PGP 운영자 키**: 운영자 변경 시 PGP 키 재봉인 필요 (절차 별도 정의)
- **3-of-3 vs 2-of-3 트레이드오프**: 3-of-3은 더 안전(모든 분할 필요)이나 운영 부담 ↑. 운영 시작 후 2-of-3 검토 가능
- **HSM 옵션**: Vault Enterprise는 HSM 지원, OSS는 software backed. 사용자 환경에 따라 선택
- **백업 sample restore 미수행 시**: 본 ADR 위반 → 분기 감사에서 자동 알림

## 운영 인프라 요구사항

| 항목 | 사양 |
|------|------|
| Vault 인스턴스 | 1개 (production) + 1개 (dev/test) 권장 |
| 백엔드 | Consul/integrated storage |
| 인증 | App Role (Hermes 컨테이너용) + Userpass (운영자) |
| 감사 로그 | Sink: 별도 디스크 또는 SIEM |
| PGP 키 등록 | 최소 2명 운영자 (단일 의존 회피) |
| 백업 저장소 (PGP 봉인) | 별도 권한 영역 (예: AWS S3 + IAM 분리) |

→ Phase 1 Week 1 작업 (P2 §4.2)에 Vault 통합 명시 추가됨.

---

**관련 문서** (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only):

### Hermes 도입 설계 (P2)

- `docs/architecture/hermes-adoption-design.md` (P2 v2 §2.1.2 본 ADR 위임 — **Archived 2026-05-09 후속 7**)
- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — §2 Hermes PMO 구조 사전 정의 + §10.1 Normative Constraints + §10.2 Archive Migration Note 답습. P2 v2 §2.1.2 본 ADR 위임의 후속 권위 본문

### 상위 ADR

- `docs/decisions/ADR-008-hermes-adoption-decision.md` (차단조건 #1 상위 — Hermes 도입 결정 Option B)
- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-010 Vault HSM 키 관리는 ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 가능 영역. 본 ADR-008 부록 B Amendment 답습)
- **`docs/decisions/ADR-012-evidence-ledger-protection.md`** (Evidence Ledger Protection — Evidence Ledger DB 가 redacted secret evidence 포함 가능 시 본 ADR-010 의 SQLCipher Vault 보호 범위 확장 의무. ADR-012 §원칙 5 (Provider Liquidity 5-way Layer 5 — Evidence 형식 차원) + §1.4 cross-reference 답습 — Evidence Ledger entry 가 *형식적 무결성* (hash chain / canonical / append-only / signed) 까지 보호하나, *secret 평문 포함* 시 본 ADR-010 GP-1 SQLCipher trigger 보호 범위에 ledger DB 명시 포함 의무 — 외부 LLM 2 C-1 답습)

### 합의 / 헌법

- `docs/review/3plus1-consensus-2026-05-04-p2-hermes-adoption.md` (B-N2 발견 출처)
- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 관용 (Provider Liquidity, 비협상)

### 4 게이트 정식 산출 (2026-05-09 Design/Governance Gate PASS Bundled)

- `docs/architecture/governance-preconditions.md` (G2 — GP-1 = G1b PASS evidence 흡수, 본 ADR-010 SQLCipher Vault 키 관리는 GP-1 의 키 관리 측면)
- `docs/architecture/provider-agnostic-memory-skill-design.md` (G4 — §4.2 11 필드 schema + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차) — Evidence Ledger DB 형식 정합

### Evidence Ledger DB Secret 처리 주의 사항 (ADR-012 §1.4 + 외부 LLM 2 C-1 답습)

본 ADR-010 의 SQLCipher Vault 보호 범위는 다음을 *명시 포함* 의무:

- Hermes SQLite (FTS5 학습루프 DB)
- Memory DB (Global / Project — G4 §2 답습)
- Skill DB (G4 §3 답습)
- **Evidence Ledger DB (`docs/evidence/ledger.jsonl` 또는 후속 SQLite migration 시점 — ADR-012 §원칙 5 답습)**: Evidence Ledger entry 가 redacted secret evidence (예: secret_scan event 의 redacted secret pattern) 포함 가능 시 본 ADR-010 GP-1 보호 범위에 명시 포함 의무. *Evidence Ledger entry 자체* 가 secret 평문 INSERT 경로 (P1 변종) 가능성 차단 — ADR-012 §1.4 cross-reference + 외부 LLM 2 C-1 권고 답습 (G2 GP-1 SQLCipher trigger 보호 범위 ledger DB 명시 포함)

본 cross-reference 추가는 *결정 내용 변경 0건* — Vault HSM + Shamir SSS 3-of-3 + 90일 회전 + dual-key + PGP 백업 + sample restore 분기 1회 모두 변경 없음. **본 ADR-010 의 보호 *대상 범위* 가 P2 v3 §3.1.2 + ADR-012 §1.4 cross-reference 로 명시 확대된 것 한정** (cross-reference 갱신).
