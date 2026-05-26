# 단축 검토 보고서 (Reviewer-only): G3 Hermes ≠ Root of Trust Runtime DRAFT 채택 적격성

**날짜**: 2026-05-07
**검증 대상**: `docs/architecture/hermes-not-root-of-trust-runtime.md` (DRAFT, commit `9c488b1`)
**합의 형태**: 단축 검토 (Reviewer-only) — DRAFT 적격성 한정
**상위 권위**: ADR-011 §2.3 (권위 위계 + 운영 함의 5항목, 영구 권위), ADR-011 §2.4 (T1/T2/T3) + 본 세션 사용자 명시 결정 (G4 진입 전 G3 DRAFT 적격 검토)
**관련 evidence**:
- G3 초안 (commit `9c488b1`) — 11 섹션 + 부록, 795 insertions
- P2 v3 DRAFT 단축 검토 결과 (commit `12d7609`, APPROVE AS DRAFT)
- G2 DRAFT 단축 검토 결과 (commit `957cddc`, APPROVE AS DRAFT)
- 합의 §90 (Agent B "합의 인프라 순환 권위 역설" — G3 §4 핵심 흡수 대상)
- 합의 §201 (메타 편향 자기진단 — 외부 LLM 가중치 통제)
- G1b PASS evidence (R-7 SOP §7.3 단축 합의, 2026-05-07)
**사용자 명시 결정**:
- G3 DRAFT 적격 검토 → APPROVE 시 별도 commit → G4 진입
- G3 PASS / G2·G4 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 런타임 코드 구현 모두 자동 트리거 금지

---

## 1. 사전 점검 — 검토 가동 정당성

### 1.1 가동 사유

본 G3 초안은 다음 입력을 흡수한 신규 산출 (commit `9c488b1`):
- ADR-011 §2.3 (권위 위계 영구 권위) + §2.4 (T1/T2/T3 분류)
- system-identity-prequel §3 (권위 위계 prequel) + §3.3 (4 강제 메커니즘 후보) + §6.1 (Evidence 5단계 명제)
- 합의 §90 (Agent B "합의 인프라 순환 권위 역설" — 핵심 흡수)
- P2 v3 DRAFT §5 (G3 정의)
- G2 DRAFT §9 메타 안전장치 G3 위임 (4 메커니즘)
- G2 DRAFT 검토 §3.1 P-1 (silent drift / upstream breakage / Skill escalation 후속 권고)

본 초안은 *DRAFT 상태로 commit 완료* (`9c488b1`) 상태이며, 본 검토는 *DRAFT 적격성*을 확인하여 G4 작업 진입 가능 여부를 판정. 검토 범위 한정:
- 사용자 명시 10 기준 충족 여부
- 금지 사항 위반 0건 확인
- DRAFT 상태 적격 + G4 진입 적격 여부

### 1.2 단축 검토 채택 사유

- 본 G3 초안 작업은 *권위 흡수 + 운영 메커니즘 정의*이며 새 권위 결정 0건 (ADR-011 §2.3 / §2.4 답습 + system-identity-prequel §3 흡수)
- G3 PASS 합의는 본 검토 비대상 — 후속 PoC + (a)~(e) 충족 검증 + **격상 통합 합의 시 외부 LLM 1+ 필수** (G3 §4.4.2 답습)
- 직전 P2 v3 / G2 DRAFT 검토 (Reviewer-only, APPROVE AS DRAFT) 패턴 답습
- ADR-011 §2.4 T2 분류 (사용자 승인 기반 진행)

### 1.3 본 검토 자체의 메타 편향 인지 (선행)

**중요**: G3 는 "합의 인프라 순환 권위" (Agent B 단독 발견) 자체를 다루는 문서. 본 검토자(Reviewer)는 G3 초안 작성자와 동일 컨텍스트 → **자기참조 + 메타 편향 이중 위험**.

본 §1.3 은 이를 명시 인지하며, §5 메타 편향 자기진단에서 다음을 통제:
- 본 검토는 *DRAFT 적격성* 한정 (G3 PASS 적격성 아님)
- G3 §4.4.2 ("Hermes PMO 격상 통합 합의 시 외부 LLM 1+ 필수")는 본 검토에 적용되지 않음 — 본 검토는 G3 PASS 적격성이 아니라 *DRAFT 적격성* 한정. 단, **G3 PASS 합의 시점에 외부 LLM 의견은 본 검토와 별도 필수**.

### 1.4 검토 비대상 (본 검토가 *판정하지 않는* 것)

- ❌ G3 PASS 적격성 — §1 ~ §7 각각 (a)~(e) Exit 기준 충족 검증 + 합의 (외부 LLM 권장)
- ❌ Hermes PMO 격상 적격성 — 4 게이트 통과 후 별도 결정 (외부 LLM 1+ 필수)
- ❌ G2 / G4 PASS 적격성 — 별도 합의
- ❌ P2 v3 정식 채택 적격성 — G2/G3/G4 완료 후 별도 합의
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신 적격성
- ❌ system-identity-prequel.md / P2 v2 archive 처리 적격성
- ❌ 실 런타임 코드 (hook / wrapper / sidecar / CI step / depcruise 룰) 적격성

---

## 2. 10 기준 점검 (사용자 명시)

### 2.1 기준 #1 — "Hermes ≠ root of trust" 운영 구조 구현 충실성

**확인 결과**: ✅ PASS

| 운영 구조 측면 | G3 초안 위치 | 충실성 |
|------------|----------|------|
| Hermes 출력 ≠ 최종 권위 | §1.2.1 / §1.2.2 / §5.2.3 (Tools verify) | ✅ 충돌 매트릭스 명시 |
| Hermes 단독 PASS 불가 | §1.3 / §5.3 (i)~(iv) | ✅ Hard Rule 명시 |
| Hermes 단독 합의 자기참조 차단 | §4 전체 (§4.1~§4.5) | ✅ 핵심 흡수 |
| Hermes 자체 격상 차단 | §2.2 #14 (T3) | ✅ 절대 금지 |
| Hermes 정책 자동 변경 차단 | §2.2 #9 #11 #17 #19 #21 (T3) | ✅ 5건 T3 |
| Hermes ↔ Constitution / ADR / SDD 위계 | §1.2.1 / §2.2 #10 #11 / §11 영구 제약 | ✅ 다중 보호 |
| Hermes 합의 결과 처리 | §4.5 (기록만 가능, 승인 불가) | ✅ 권한 분리 |

→ Criterion 1 PASS, "Hermes ≠ root of trust" 운영 구조 구현 충실. ADR-011 §2.3 권위 + system-identity-prequel §3 흡수 + 합의 §90 (자기참조 역설) 핵심 흡수.

### 2.2 기준 #2 — 권위 위계 명확성

**확인 결과**: ✅ PASS

```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

| 위계 단계 | G3 초안 명시 위치 | 강제 메커니즘 |
|---------|------------|----------|
| Constitution | §1.1 + §11 영구 제약 + §2.2 #11 우회 차단 | filesystem read-only + audit log |
| ADR | §1.2.1 (Hermes vs ADR/SDD 매트릭스) + §2.2 #10 자동 수정 차단 | filesystem read-only on `docs/decisions/ADR-*.md` + git pre-commit hook |
| SDD | §1.2.1 (동일) + §11 영구 제약 | filesystem read-only |
| Harness Gates | §1.2.3 (Layer 1~6 fail → Hermes 차단) + §2.2 #12 실패 무시 차단 | hook 실패 → 큐 차단 + git layer 차단 |
| Hermes | §2 권한 22 항목 (T1 8 / T2 2 / T3 12) | 다중 강제 메커니즘 (계산적 22/22) |
| Worker Agents | §1.2.2 (Worker 출력 ≠ Hermes 위) + §6.3 GP-4 검증 권위 | wrapper layer + Tools 검증 |

→ Criterion 2 PASS, 위계 명확. ADR-011 §2.3 권위 인용 + 충돌 매트릭스 + 영구 제약 다중 보호.

### 2.3 기준 #3 — 권한 22 항목 분류 적절성

**확인 결과**: ✅ PASS

§2.1 허용 (T1 자동) 8건:

| # | 권한 | 사용자 명시 후보 | T1 분류 적절성 |
|---|------|------------|----------|
| 1 | 작업 분배 | ✅ 명시 | ✅ orchestration 영역 |
| 2 | Memory 조회 (read-only) | ✅ 명시 | ✅ read-only 한정 정당 |
| 3 | Skill 후보 제안 | ✅ 명시 | ✅ 제안 한정 (등록은 §2.2 #16) |
| 4 | 합의 실행 보조 (orchestrate) | ✅ 명시 | ✅ orchestrate 한정 (승인은 §4) |
| 5 | Evidence 위치 정리 | ✅ 명시 | ✅ 정리 제안 한정 (실 갱신은 사용자 명시) |
| 6 | 다음 작업 제안 | ✅ 명시 | ✅ 제안 한정 |
| 7 | 자체 학습 (T1 한정) | (사용자 명시 추가) | ✅ ADR-011 §2.4 T1 직접 매핑 |
| 8 | Hermes 자체 redaction (로그/송신) | (사용자 명시 추가) | ✅ ADR-011 §2.3 운영 함의 #2 답습 (DB 차단은 G1b 책임) |

§2.2 금지 14건 (T2 2 + T3 12):

| # | 금지 행위 | 사용자 명시 후보 | 분류 | 적절성 |
|---|---------|------------|------|------|
| 9 | 정책 자동 변경 | ✅ 명시 | T3 | ✅ |
| 10 | ADR 자동 수정/승인 | ✅ 명시 | T3 | ✅ |
| 11 | Constitution 우회 | ✅ 명시 | T3 | ✅ |
| 12 | Harness Gate 실패 무시 | ✅ 명시 | T3 | ✅ |
| 13 | G2/G3/G4 PASS 자동 선언 | ✅ 명시 | T3 | ✅ |
| 14 | Hermes PMO 자기 격상 | ✅ 명시 | T3 | ✅ |
| 15 | Memory 자동 promotion | (사용자 명시 추가) | T2 | ✅ system-identity-prequel §8.4 ("manual only") |
| 16 | Skill 자동 등록 | (사용자 명시 추가) | T2 | ✅ system-identity-prequel §8 |
| 17 | 자체 학습→자동 정책 반영 | (사용자 명시 추가) | T3 | ✅ ADR-011 §2.4 |
| 18 | Provider lock-in 유도 | ✅ 명시 | T3 | ✅ |
| 19 | Secret redaction 정책 완화 | ✅ 명시 | T3 | ✅ |
| 20 | 합의 결과 silent override | (사용자 명시 추가) | T3 | ✅ system-identity-prequel §3.3 #2 |
| 21 | Tier-1/2/3 catalog 자동 확장 | (사용자 명시 추가) | T3 | ✅ ADR-011 §2.4 |
| 22 | 사용자 override 자동 reject | (사용자 명시 추가) | T3 | ✅ ADR-011 §2.3 운영 함의 #5 |

**합산**: T1 8 / T2 2 / T3 12 = 22

**사용자 명시 14건 (허용 6 + 금지 8) 모두 매핑**. 추가 8건 (#7 #8 #15 #16 #17 #20 #21 #22) 모두 권위 근거 명시 + 적절한 분류.

→ Criterion 3 PASS, 분류 적절.

### 2.4 기준 #4 — T3 차단 4 항목 confirmation

**확인 결과**: ✅ PASS (4/4 모두 T3 차단)

| 사용자 명시 4 항목 | G3 위치 | 분류 | 강제 메커니즘 |
|-------------|--------|------|----------|
| Hermes 자기 격상 | §2.2 #14 | **T3** | 격상 명령 권한 0 + audit log + 사용자 alert + §4.3 (자기참조 차단) |
| 정책 자동 변경 | §2.2 #9 (+ 보강 #11 #17 #19 #21) | **T3 5건** | filesystem read-only + T3 변경 감지 hook + git pre-commit + audit log |
| Provider lock-in 유도 | §2.2 #18 | **T3** | depcruise 룰 + PR auto-reject + git pre-commit hook on Hermes-originated commit (§6.4 답습) |
| Secret redaction 정책 완화 | §2.2 #19 | **T3** | redaction-policy.yaml read-only + T3 변경 감지 hook + ROLLBACK §3.1 |

**추가 보호** (사용자 명시 4 항목 외 T3 차단):
- §2.2 #10 ADR 자동 수정/승인 (T3)
- §2.2 #11 Constitution 우회 (T3)
- §2.2 #12 Harness Gate 실패 무시 (T3)
- §2.2 #13 G2/G3/G4 PASS 자동 선언 (T3)
- §2.2 #20 합의 결과 silent override (T3)
- §2.2 #21 catalog 자동 확장 (T3)
- §2.2 #22 사용자 override 자동 reject (T3)

→ Criterion 4 PASS, 사용자 명시 4 항목 + 추가 7 항목 모두 T3 차단. 차단 메커니즘 다중 보호.

### 2.5 기준 #5 — 3 위험 5 측면 분해 충실성

**확인 결과**: ✅ PASS

| 위험 | 정의 | 감지 | 차단 | Evidence | Rollback | 사용자 승인 |
|------|------|------|-----|--------|--------|---------|
| §3.1 Learning silent drift | §3.1.1 (정책성 파일 silent 변경) | §3.1.2 (4 channel: CI nightly diff / Hermes-originated commit / R-5 canary / R-6 actual run) | §3.1.3 (4 layer: filesystem / git / CI / runtime) | §3.1.4 (Markdown + JSONL ledger + audit log) | §3.1.5 (T3 위반 → 컨테이너 정지 + revert + R-7 SOP R5 답습) | §3.1.6 (T3 변경 자동 금지, 사용자도 ADR Amendment) |
| §3.2 Upstream silent breakage | §3.2.1 (의존성 업그레이드 silent 깨짐) | §3.2.2 (4 channel: R-6 trigger 확장 / nightly cron / lock diff / telemetry 차단 회귀) | §3.2.3 (4 layer: version pin / PR PoC 재실행 / R-6 PASS branch protection / runtime healthcheck) | §3.2.4 (GH run + artifact + JSONL + lock diff) | §3.2.5 (R-7 SOP R6 - 이전 버전 복귀) | §3.2.6 (PR merge T2 — 자동 PR 생성 OK / 자동 merge 금지) |
| §3.3 Skill permission escalation | §3.3.1 (정의 권한 등급 외 작동) | §3.3.2 (3 channel: wrapper 권한 검증 / audit T1 분석 / sandbox syscall 추적) | §3.3.3 (4 layer: wrapper BLOCK / Docker cap_drop / audit log / 자동 비활성화) | §3.3.4 (skill 정의 + audit log + escalation 본문 + JSONL) | §3.3.5 (자동 비활성화 + 반복 시 archive) | §3.3.6 (Skill 등록 T2 + 재활성화 T2) |

§3.4 통합 매트릭스 — 3 위험 × 5 측면 모두 분해.

**모든 5 측면이 사용자 명시 답습**:
- 감지 방법 ✅
- 차단 방법 ✅
- Evidence 요구사항 ✅
- Rollback trigger ✅
- 사용자 승인 필요 여부 ✅

→ Criterion 5 PASS, 분해 충실. G2 단축 검토 §3.1 P-1 권고를 G3 §3 으로 흡수.

### 2.6 기준 #6 — 합의 자기참조 통제 (4 sub-criteria)

**확인 결과**: ✅ PASS (4/4 sub-criteria 충족)

| Sub-criteria | G3 위치 | 충족 |
|-----------|------|----|
| 1. Hermes 단독 합의 금지 | §4.2 원칙 1 + §4.3 매트릭스 (Hermes-originated commit auto-reject 영역 — 정책 변경 / ADR 작성 / Hermes PMO 격상 / 본 §4 §9 변경) | ✅ |
| 2. Hermes-originated commit auto-reject | §2.2 #20 (T3) + §4.5 처리 권한 표 ("합의 결과 commit author: ❌ Hermes-originated commit auto-reject") + §3.1.3 git pre-commit hook | ✅ |
| 3. 외부 LLM 또는 사용자 승인 조건 | §4.4.2 외부 LLM 필요 조건 4 영역 (격상 통합 합의 필수 / 정책 변경 권장 / ADR 갱신 권장 / 자기 작성 산출 검증) + §4.4.3 사용자 승인 필요 조건 4 영역 (T2 모두 / T3 모두 / 의존성 PR merge / 합의 형태 결정) | ✅ |
| 4. Hermes는 기록 가능, 승인 주체 불가 | §4.5 처리 권한 표 6행 (orchestrate ✅ / 본문 보존 ❌ Hermes 수정 가능 형태 / commit author ❌ / 적용 ❌ / 사용자 전달 ✅ / 참조 ✅) | ✅ |

**§4 추가 보강**:
- §4.1 문제 정의 (자기참조 역설 명시)
- §4.6 본 §4가 *하지 않는* 것 (3건)
- §10 변경 절차에서 §4.3 변경은 풀 3+1 + ADR Amendment (T3 변경)

→ Criterion 6 PASS, 4 sub-criteria 모두 충족. 합의 §90 (Agent B 단독 발견) 핵심 흡수.

### 2.7 기준 #7 — Evidence 없는 PASS 금지 강제

**확인 결과**: ✅ PASS (Hard Rule + 다층 강제)

| 강제 위치 | 내용 | 강제 layer |
|---------|------|---------|
| §1.3 Hard Rule | 모든 PASS 판정 = Evidence Ledger 기록 의무 / 자동 reject 메커니즘 / 영역별 PASS 성립 요건 표 | Hard Rule 선언 |
| §1.3 자동 reject 메커니즘 | Layer 1~2 hook + Layer 4 CI + Layer 5 합의 | 4-layer |
| §2.2 #13 | G2/G3/G4 PASS 자동 선언 차단 (T3) | T3 영역 |
| §5.2.4 운영 규칙 #4 | Harness Gate와 Evidence 없으면 PASS 미성립 | 운영 규칙 |
| §5.3 PASS 성립 요건 (i)~(iv) | (i) Tools 검증 + (ii) ledger entry + (iii) 사용자 명시 (T2/T3) + (iv) 합의 보고서 (해당 시) | 4 요건 |
| §5.3 미충족 처리 | (i) hook 자동 차단 / (ii) ledger 검증 자동 차단 / (iii) T2/T3 자동 reject / (iv) 합의 cross-reference 부재 = §5.3 위반 | 자동 처리 |
| §8 Exit (a)~(e) | 모든 § Exit 기준에 evidence + 합의 명시 | 7 § × 5 조건 |

**Evidence Ledger 변조 방지**:
- Markdown + JSONL append-only (system-identity-prequel §6.3 답습)
- hash chain 또는 git append commit 변조 방지

→ Criterion 7 PASS, 다층 강제 충실. Hard Rule + T3 + 운영 규칙 + Exit 기준 4중 보호.

### 2.8 기준 #8 — G2 ↔ G3 책임 분리 명확성

**확인 결과**: ✅ PASS

§6 G2 인터페이스 (5 GP × G3 책임 분리):

| GP | G2 책임 (메커니즘 / 동작) | G3 책임 (권한 / 신뢰 / 무결성) | §6 위치 |
|----|----------------------|----------------------------|------|
| GP-2 Egress Redaction | redaction *동작* (Tier-1 catalog 적용 + base64 evasion) | redaction *정책 무결성* (정책 변경 차단 + T3) | §6.1 |
| GP-3 Credential Hygiene | credential *노출* 차단 (docker secret + chmod + inotify + gitleaks) | credential *변경 권한* 차단 + Hermes-originated 변경 audit | §6.2 |
| GP-4 외부 입력 검증 | 검증 *메커니즘* (sanitizer / schema / escape) | 검증 *권위* 강제 (Hermes 출력 ≠ Tools 위) | §6.3 |
| GP-5 Provider Adapter | *코드 lock-in* 차단 (depcruise / 작성 주체 무관) | *Hermes-originated lock-in* 변경 차단 (작성 주체 = Hermes 한정) | §6.4 |
| GP-6 Memory/Skill | *마이그레이션 가능성* (JSONL + 변환 스크립트) | *권한 + Promotion + Escalation* | §6.5 |

§6.6 통합 매트릭스 — 5 GP × G2 vs G3 책임 분리 표

**원칙 명시** (§6.6):
- G2 = *동작/메커니즘*
- G3 = *권한/신뢰/무결성*
- 보완 관계 — 두 게이트 모두 PASS 시 격상 충분 조건 일부 충족

→ Criterion 8 PASS, 책임 분리 명확. 5 GP 모두 G2/G3 분리 매트릭스 명시 + 통합 원칙.

### 2.9 기준 #9 — G3 ↔ G4 책임 분리 명확성

**확인 결과**: ✅ PASS

§7 G4 경계:

| 측면 | G3 책임 (본 문서) | G4 책임 (별도 문서) |
|------|-------------|--------------|
| 신뢰 boundary | ✅ §1.2 + §2.1 #2 + §6.5 | (위임) |
| Skill promotion 권한 | ✅ §2.2 #16 (T2) + §4.3 + §6.5 | (위임) |
| Memory promotion 권한 | ✅ §2.2 #15 (T2) + §4.3 + §6.5 | (위임) |
| Skill 권한 escalation 차단 | ✅ §3.3 | (위임) |
| Memory/Skill 변경 audit | ✅ §1.2.1 + §2.2 #20 | (위임) |
| 사용자 override 처리 | ✅ §5.4 | (위임) |
| Memory/Skill 데이터 형식 | (위임) | ✅ `memory-scope-design.md` |
| Skill schema (`skill.yaml`) | (위임) | ✅ `skill-format-design.md` |
| Export/import 구조 | (위임) | ✅ `scripts/hermes-migration/*` 사양 |
| Provider-agnostic schema | (위임) | ✅ ADR-014 후보 (P2 v3 §6.7 등록) |
| 다른 오케스트레이터 변환 | (G4와 공동) | ✅ G4 + GP-6 공동 |

§7.3 공동 인터페이스 5 항목 (Memory boundary / Skill 등록 / Skill 권한 등급 / 변경 audit / 메타-템플릿 오염 방지)

**원칙 명시** (§7.3):
- G3 = *누가/무엇을 할 수 있는가* (권한 / 신뢰 / 무결성)
- G4 = *어떻게 표현되는가* (형식 / schema / export-import)
- **권한 ↔ 형식** 보완 관계

→ Criterion 9 PASS, 책임 분리 명확. G3 6 책임 + G4 5 책임 + 공동 5 인터페이스.

### 2.10 기준 #10 — G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 암시 부재

**확인 결과**: ✅ PASS (암시 0건, 명시 부정 다수)

**명시 부정 위치**:

| 위치 | 부정 문구 |
|------|--------|
| 헤더 첫 줄 | "**G3 PASS 선언 / G2·G4 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 런타임 코드 구현 모두 본 초안 범위 외**" |
| §0.2 #1~#10 | 10건 명시 부정 |
| §8.3 *발생* | "G3 status 갱신" — *합의 APPROVE 시점*에 (본 초안 범위 외) |
| §8.3 *발생하지 않는 것* | G2/G4 자동 PASS / Hermes PMO 격상 자동 / P2 v3 정식 채택 자동 / archive 자동 / ADR-011 §2.3 본문 자동 갱신 |
| §11.2 | "본 초안은 G3 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*" + 9건 명시 부정 |
| §11.3 즉시 강제 | "본 G3 가 정식 채택되지 않더라도" — DRAFT 상태 자체에서도 즉시 강제 4건 명시 (정식 채택은 별도) |
| 종료 줄 | 7건 명시 부정 |

**G3 PASS 합의 시점 명시 분리**:
- §8.2: PASS 조건 (본 §1~§7 (a)~(e) 충족 + 합의 + 외부 LLM 권장)
- §8.3: PASS 합의 APPROVE 시점에 *발생*하는 것 vs *발생하지 않는 것* 명시 분리
- §10 변경 절차: DRAFT → 정식 채택 = 합의 + (a)~(e) 충족 + 외부 LLM 의견 권장

**잠재 암시 검색** (Reviewer 자기 검토):
- "충족" 단어: §1.1 위계 인용 / §8.1 entry "충족됨" — *현재 충족된 selecting evidence* 명시이지 *G3 PASS 발생*이 아님. 정직.
- "PASS" 단어: G1b PASS / R-6 PASS 등 *기존 권위 결정* 인용 + §1.3 §5.3 *PASS 성립 요건* 정의. *G3 PASS / 격상 PASS / 정식 채택 PASS* 인용 0건.
- "활성화" 단어: §0.3 단계 5 (G3 PASS 선언 + ADR cross-reference 갱신, G2/G4와 묶음 가능) — *합의 APPROVE 후* 라고 시점 명시. 자동 트리거 없음.
- "격상" 단어: 모두 §0.2 #3 / §2.2 #14 / §4.3 / §8.3 / §11.2 등 *부정* 또는 *4 게이트 통과 후 별도 결정* 맥락에서 사용.

→ Criterion 10 PASS, 암시 0건, 명시 부정 다수.

---

## 3. 추가 점검 항목 (Reviewer 자기 발견)

본 §3은 사용자 명시 10 기준 외 Reviewer가 자기 발견한 잠재 위험 항목.

### 3.1 P-1 — §2.4 강제 메커니즘 매트릭스 자동 롤백 산술 오류 (소프트 관찰)

**위치**: 본 G3 §2.4 합산 마지막 줄
> "**합산**: 계산적 22/22, 추론적 보조 6/22, 자동 롤백 14/22 (T1 #1~#7 외 전부)."

**검증**:
- §2.4 표 행별 자동 롤백 ✅ 표시:
  - #1~#7 (T1 자동): 자동 롤백 ❌ (7건)
  - #8 (T1 redaction): 자동 롤백 ✅ (1건)
  - #9~#22 (T2/T3): 자동 롤백 ✅ (14건)
- **실제 합산**: 자동 롤백 ✅ = 1 + 14 = **15/22**

**현 본문**: "자동 롤백 14/22 (T1 #1~#7 외 전부)" — 사실은 "**15/22**" 가 정확.

**위험 등급**: 매우 낮음 (VERY LOW) — 산술 오류 1건, 본문 의미는 일관 ("T1 #1~#7 외 전부" = 22-7=15)

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #1** 등록 — 정식 채택 시점 또는 G4 작업 도중 §2.4 합산을 "15/22"로 정정. 본문 의미("T1 #1~#7 외 전부")는 정확하므로 *해석 위험 0*.

### 3.2 P-2 — G2 §8.5 Exit 기준에 G3 §6 인터페이스 cross-reference 부재 (소프트 관찰)

**위치**: G2 (`governance-preconditions.md`) §8.5 (e) Exit 기준
> "(e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-6 + G4 통합 가능)"

**관찰**: G2 GP-6 §8.5 는 G4 통합 가능만 명시, **G3 §6.5 (GP-6 ↔ G3 ↔ G4 3-way 인터페이스)** 미명시.

**현 갭**: G3 §6.5 가 *3-way 인터페이스* 로 정의했으나, G2 GP-6 §8.5 는 *2-way (G2 + G4)* 에 그침.

**위험 등급**: 낮음 (LOW)
- DRAFT 상태이며 G2 / G3 정식 채택 전
- G3 §6.5 본문이 3-way 명시로 G2 후속 갱신 권고로 이미 등록됨 (G2 단축 검토 §3.1 P-1 / P-2 패턴 답습)

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #2** 등록 — G2 / G3 정식 채택 시점에 G2 §8.5 Exit 기준에 G3 §6.5 cross-reference 추가 ("(e) 단축 또는 풀 3+1 합의 (G2 GP-6 + G3 §6.5 + G4 통합 가능)").

### 3.3 P-3 — §4.4.2 외부 LLM 의견의 *형식·절차* 명시 약함 (확인 사항)

**위치**: 본 G3 §4.4.2 외부 LLM 의견 형식
> "외부 LLM 의견은 다음 형식 중 하나:
> - 별도 LLM 호출 결과 (GPT / Gemini / Local LLM 등)
> - 외부 검토 의뢰 자료 (`docs/external-review/` 패턴 답습)
> - 외부 Reviewer 또는 다른 사용자 검토"

**관찰**:
- 형식 후보 3건은 명시되었으나, **각 형식의 채택 기준** + **어떤 결정에 어떤 형식이 적격인지** 매트릭스 부재
- 예: Hermes PMO 격상 통합 합의 시 *별도 LLM 호출* 충분한가, *외부 검토 의뢰 자료* 필수인가, *둘 다* 인가? 미명시.

**위험 등급**: 낮음 (LOW)
- DRAFT 상태이며 후속 합의 시점에 정밀화 가능
- §4.4.2 본문이 "필수 또는 강력 권장" 표현으로 hedge되어 있어 *최소 요건* 명시 가능

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #3** 등록 — G3 PASS 합의 시점 또는 Hermes PMO 격상 통합 합의 시점에 §4.4.2 외부 LLM 의견 형식 매트릭스 정밀화.

### 3.4 P-4 — §11 메타 한계 4건 외 추가 검증 대상 (확인 사항)

**위치**: 본 G3 §11.1 메타 한계 4건 명시:
- 자기 작성 산출 (G3 § 외부 LLM 의견 권장)
- §2.2 22 금지 권한 enumeration 원안
- §3 3 위험 차단 메커니즘 원안
- §4.3 합의 형태 매트릭스 원안

**잠재 추가 후보** (Reviewer 자기 발견):
- §1.2 충돌 해결 매트릭스 3개 — *원안* (system-identity-prequel §3.3 + ADR-011 §2.3 인용 정확하나 *충돌 시나리오 분류*는 원안)
- §5.2 5 운영 규칙 + §5.3 PASS 성립 4 요건 — *원안* (system-identity-prequel §6.1 명제 + ADR-011 §2.3 운영 함의 답습이나 *4 요건 분리*는 원안)
- §6 5 GP × G3 책임 분리 — *원안* (G2 GP-2~GP-6 본문 인용 정확하나 *5 GP × G2 vs G3 매트릭스*는 원안)
- §7 G3 6 책임 + G4 5 책임 + 공동 5 인터페이스 — *원안*

**위험 등급**: 낮음 (LOW)
- §11.1 4건 명시는 *주요* 원안 4건 한정 — 추가 4건 (위)도 메타 한계 대상
- DRAFT 상태에서 후속 합의 시 *추가 검증 대상* 으로 자동 포함 (DRAFT 자체가 미완 신호)

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #4** 등록 — G3 PASS 합의 시점에 §11.1 메타 한계에 추가 4건 (§1.2 / §5.2 / §6 / §7) 명시 권고.

---

## 4. 금지 사항 위반 점검 (사용자 명시 답습)

| # | 금지 항목 | 본 초안 위반 여부 |
|---|---------|---------------|
| 1 | G3 PASS 선언 | ❌ 위반 0건 (§2.10 기준 점검 결과 + 명시 부정 다수) |
| 2 | G2 / G4 PASS 자동 선언 | ❌ 위반 0건 (§6 / §7 인터페이스 한정 + §0.2 #2) |
| 3 | Hermes PMO 격상 선언 | ❌ 위반 0건 (헤더 + §0.2 #3 + §2.2 #14 T3 + §4.3 자기참조 차단 + 종료 줄 다중 명시 부정) |
| 4 | P2 v3 정식 채택 선언 | ❌ 위반 0건 (§0.2 #4 + §8.3 + 종료 줄 명시 부정) |
| 5 | ADR-008/009/010/011 본문 자동 갱신 | ❌ 위반 0건 (§0.2 #5 + §8.3 "ADR-011 §2.3 본문 자동 갱신 ❌ — cross-reference 만") |
| 6 | P2 v2 archive 처리 | ❌ 위반 0건 (§0.2 #6) |
| 7 | system-identity-prequel archive 처리 | ❌ 위반 0건 (§0.2 #6 + §11.3 즉시 강제 #2 "prequel archived 후에도 본 G3 권위로 보존") |
| 8 | 실 런타임 코드 구현 | ❌ 위반 0건 (§0.2 #7 + §1.4 "Layer 1~6 hook 실 코드 작성 (본 초안은 설계까지)" + §11.2 마지막 항) |

→ 8/8 금지 항목 위반 0건.

---

## 5. 메타 편향 자기진단

### 5.1 본 검토의 이중 메타 편향 위험 (G3 특수 조건)

**중요**: G3 는 "**합의 인프라 순환 권위**" 자체를 다루는 문서 (§4 — Agent B 단독 발견 핵심 흡수). 본 검토자(Reviewer)는 G3 초안 작성자와 동일 컨텍스트 → **자기참조 + 메타 편향 이중 위험**.

본 §5.1 은 G3 §4 자체에 의해 *자기 검증 대상*. 따라서 본 검토는 다음을 명시 인지:

1. 본 검토는 G3 §4.4.1 ("Reviewer-only 단축 합의 충분 조건")의 4 조건 중 *DRAFT 적격성* 한정 충족 — *G3 PASS* 합의는 G3 §4.4.2 답습으로 외부 LLM 의견 추가 필수.
2. 본 검토 *PASS 판정*은 *G3 PASS 판정*이 아님 (§1.4 답습).
3. 본 검토 자체가 G3 §4 자기참조 차단의 *적용 대상* — Reviewer-only 단축 합의는 ADR-011 §2.4 T2 영역에서 정당하나 *G3 PASS* 영역은 본 검토 비대상.

### 5.2 5 통제 답습

| # | 통제 수단 | 본 검토 적용 |
|---|---------|---------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 10 기준 §2 + 8 금지 항목 §4 + DRAFT 적격 검토 한정 |
| 2 | 직전 단축 합의 패턴 답습 | ✅ P2 v3 / G2 DRAFT 검토 §2/§3/§4/§5 구조 답습 |
| 3 | 10 항목 답습 + 8 금지 점검 | ✅ §2 10/10 + §4 8/8 점검 |
| 4 | 자기 발견 잠재 위험 명시 (§3 P-1 ~ P-4) | ✅ 4건 자기 발견, 모두 LOW/VERY LOW + BLOCK 사유 아님 |
| 5 | 본 검토가 *하지 않는* 것 명시 (§1.4) | ✅ 7건 명시 비대상 |

### 5.3 본 검토의 한계

- 본 검토는 *자기 작성 산출 자기 검토* (P2 v3 / G2 / G3 모두 동일 컨텍스트)
- **G3 §4.4.2 답습**: 자기 작성 산출 검증은 외부 LLM 의견 *권장* — 본 검토가 외부 LLM 의견 대체 불가
- **G3 PASS 합의는 외부 LLM 의견 권장 + 격상 통합 합의는 외부 LLM 1+ 필수** (G3 §4.4.2). 본 검토는 그 적격성 판정 비대상.
- §3 자기 발견 잠재 위험 4건은 본 Reviewer 의 시야 한정 — 외부 LLM 시야에서 추가 발견 가능.
- 특히 §4 자체 (자기참조 차단) 가 *원안* — 본 검토가 §4 의 *적정성*을 판정하기 어려움 (자기 검증 한계). G3 PASS 합의 시점 외부 LLM 의견 의무.

### 5.4 본 검토의 *PASS 판정이 트리거하지 않는 것*

본 §6 결론 PASS 판정은 다음을 *트리거하지 않는다*:

- ❌ G3 PASS
- ❌ G2 / G4 PASS 선언
- ❌ Hermes PMO 격상
- ❌ ADR-008/009/010/011 갱신
- ❌ P2 v2 / system-identity-prequel archive
- ❌ INDEX / CONTEXT 갱신
- ❌ Phase 진입 결정
- ❌ 실 런타임 코드 구현
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ G4 작업 자동 시작 (사용자 명시 결정 대기)

본 검토 PASS 판정은 *오직* "G3 운영 구현 설계 DRAFT 적격 + G4 작업 진입 적격" 의미.

---

## 6. 결론

### 6.1 판정

```
✅ APPROVE AS DRAFT
```

### 6.2 사유

- **10 기준 10/10 PASS** (§2.1 ~ §2.10) — 운영 구조 충실 + 위계 명확 + 22 권한 분류 적절 + T3 차단 4 항목 + 3 위험 5 측면 분해 + 합의 자기참조 4 sub-criteria + Evidence 없는 PASS Hard Rule + G2 / G4 책임 분리 + 암시 0건
- **8 금지 항목 8/8 위반 0건** (§4)
- **자기 발견 잠재 위험 4건** (§3 P-1 ~ P-4) 모두 LOW / VERY LOW 등급 + BLOCK 사유 아님 + G4 작업 도중 또는 G3 PASS 합의 시점에 흡수 가능
- **메타 편향 5 통제 답습** (§5.2)
- **G3 §4 자기참조 차단의 *적용 대상*** 으로 본 검토 한계 명시 (§5.1 + §5.3)

### 6.3 후속 권고 (DRAFT 적격성과 *분리*)

본 결론은 DRAFT 적격성 판정 한정. 후속 작업 시 다음 표현 정밀화 권고 (선택):

| # | 권고 (선택) | 위치 | 처리 시점 |
|---|---------|-----|---------|
| 1 | §2.4 자동 롤백 합산 정정 (14/22 → 15/22) | G3 §2.4 마지막 줄 | 정식 채택 시점 또는 G4 작업 도중 |
| 2 | G2 §8.5 Exit 기준에 G3 §6.5 cross-reference 추가 (3-way 인터페이스 반영) | G2 §8.5 (e) | G2 / G3 정식 채택 시점 |
| 3 | §4.4.2 외부 LLM 의견 형식 매트릭스 정밀화 (어떤 결정에 어떤 형식이 적격인지) | G3 §4.4.2 | G3 PASS 합의 시점 또는 Hermes PMO 격상 통합 합의 시점 |
| 4 | §11.1 메타 한계 추가 4건 명시 (§1.2 / §5.2 / §6 / §7 원안 명시) | G3 §11.1 | G3 PASS 합의 시점 |

본 권고 4건은 *G3 PASS 합의 또는 정식 채택 진입 시점* 에 함께 검토. 본 DRAFT 적격성 판정 단계에서는 처리 불필요.

### 6.4 G4 진입 적격성

본 G3 DRAFT 적격성 판정 결과 + 사용자 명시 결정 ("G3 DRAFT 검토 APPROVE 시 G4 작업 진입") 답습 → **G4 작업 진입 적격**.

G4 작업 진입 시점에 본 G3 §7 G4 경계 매트릭스 + §6.5 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 + §7.3 공동 5 인터페이스 답습.

### 6.5 본 검토 보고서 commit 절차

본 결론 APPROVE AS DRAFT에 따라 다음 단일 파일을 별도 commit으로 처리 가능:

```
docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md
```

commit 메시지 (사용자 예시 답습):
```
docs(review): record G3 root-of-trust draft short review
```

본 commit에 포함하지 *않는* 항목 (사용자 명시 답습):
- G3 본문 갱신
- ADR-008/009/010/011 본문 갱신
- P2 v2 / system-identity-prequel archive 처리
- INDEX / CONTEXT 갱신
- Hermes PMO 격상 선언
- G2 / G3 / G4 PASS 선언
- 실 런타임 코드 구현

---

## 7. 다음 진입점 (본 검토 *이후*)

본 검토 PASS 후 사용자 명시 4단계 순서 답습:

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | G3 초안 Reviewer-only 단축 검토 | 본 보고서 | 본 단계 (완료) |
| 2 | 검토 보고서 별도 commit | `docs(review): record G3 root-of-trust draft short review` | 본 단계 직후 |
| 3 | G4 작업 시작 | 사용자 결정 후보 — 분리 (`memory-scope-design.md` + `skill-format-design.md`) 또는 통합 (`provider-agnostic-memory-skill-design.md`) | 사용자 명시 결정 후 |
| 4 | G2/G3/G4 완료 후 P2 v3 정식 채택 합의 | 합의 보고서 + ADR PR 묶음 (외부 LLM 의견 권장 / Hermes PMO 격상 통합 합의 시 외부 LLM 1+ 필수) | G2/G3/G4 완료 후 |

본 검토 *이후* 금지 사항은 변동 없음 — §4 8 금지 항목 + 사용자 명시 답습.

---

**검토일**: 2026-05-07
**검토자**: Reviewer-only (메타 편향 자기진단 §5 명시 + G3 §4 자기참조 차단의 적용 대상 인지)
**판정**: ✅ APPROVE AS DRAFT
**다음 단계**: 본 검토 보고서 별도 commit → G4 작업 시작 (사용자 명시 결정 후)
