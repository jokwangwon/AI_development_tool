# 3+1 합의 보고서 — BI-5 audit sink integrity brief (DRAFT v1)

**일자**: 2026-05-21
**대상**: `docs/phase0/bi-5-audit-sink-integrity-brief.md` (DRAFT v1)
**진입 단위**: Group I 구현 entry 합의(`f29c772`) 후속 #3 — BI-5(audit sink integrity, 4축 마지막) 단독 심화 검증
**합의 형태**: **풀 3+1** (Agent A 구현 / B 품질·안전성 / C 대안 + Reviewer 교차) — 보안 BLOCKING + Evidence Ledger(ADR-012) 정합 → Reviewer-only 부적격
**판정**: **APPROVE WITH CONDITIONS** (BLOCKING 4 = BI5C-1~4 + 권고 5 = BI5R-1~5)
**합의 권위**: 추론적 검증(권고) 한정 — citation 정정·owner self-bypass 명문·AE write 주체 명세·수단표 보강·수단 결정·실 변경·commit·push = 모두 사용자 명시 + 별도 단계. 본 보고서는 어떤 코드/설정도 변경하지 않음.

---

## 0. 검토 대상 및 권위

- 대상 = BI-5 brief v1 (audit sink integrity = G3 4축 마지막). 합의 = 권고 한정. audit sink 실 구성·Evidence Ledger 변경·sigstore/Rekor 도입·credential/audit token 분리·hook·CI·commit/push = 0건.

---

## 1. 핵심 재검증 결과 (Reviewer 직접 grep/read 확정)

### BI5C-1 — "ADR-012 차단조건 #2" citation stale → **사실 확정 (BLOCKING)**
- brief §7 line 162 / §12.1 G-BI5-5 line 217 / 부록 A line 258: "ADR-012 차단조건 #2 = Evidence Ledger = Hermes 의존 0".
- 직접 grep: ADR-012 에 **"차단조건 #2"라는 자체 항목 부재**. 매트릭스 line 65 = "**ADR-008** 차단조건 #2(JSONL export) … 본 ADR §2.10 흡수". "Hermes 의존 0" = ADR-012 **원칙 5**(line 91), BI-5 (a)/(c)와 정합하는 건 **원칙 3**("Hermes 가 승인/수정 불가", line 87).
- → 정정 = **"ADR-012 원칙 5 (Hermes 의존 0) + 원칙 3 (Hermes 승인/수정 불가) — 모두 ADR-008 차단조건 #2 답습"**. **BI-4 §11.3(BI4C-1)·BI-3 N-2 와 동형 stale 패턴** (citation 정밀화 의무 답습).

### BI5C-2 — owner self-bypass 거짓 안전감 미전파 → **사실 확정 (BLOCKING, B·C 통합)**
- §10 binary 4시연(line 187-191)·§12.2 Rollback Trigger(line 222-225) = **전부 "에이전트" 주어**. owner 경로는 §9 line 178 한 줄 인정뿐.
- **B = 명문 누락**(owner self-bypass 가 binary/Rollback 에 전파 안 됨) / **C = 해소 수단 평가절하**(Rekor=제3자=owner 구조적 삭제 불가 = §9 가 포기한 그 지점을 audit 축에서 닫는 유일 후보인데, MVP-6 DEFER 의 인과["audit self-bypass 영구 수용 결정과 동치"]가 미명문).
- → **동일 쟁점의 두 측면** → 통합 BLOCKING. (B·C 가 서로 다른 입구로 동일 지점 수렴.)

### AE-3 "BI-4 §6.2" citation → **재검증 결과 정확 (기각)**
- BI-4 brief §6.2(line 227) = "ruleset 변경 = R-I-CONFIG-CHANGE = T3" **실재** → brief AE-3 citation 정확, 조치 불요. (A BI5-A4·B BR-3 가 권고로만 분류한 점 정합 — BLOCKING 아님.)

---

## 2. 교차 비교

| # | 항목 | A | B | C | 분류 |
|---|------|---|---|---|------|
| 1 | §2 BI-5 3속성 = `f29c772` line 94 정확 | ✅ | — | — | 일치(단독·미반박) |
| 2 | §4 수단 후보 실현 가능 | ✅ | — | ✅ | **일치** |
| 3 | §5 CT-4 재귀 닫힘 타당 | ✅ | ✅ | ✅ | **일치** |
| 4 | §6 완전성 FN(audit≠완전, BI-7) 모범 | ✅ | ✅ | — | **일치** |
| 5 | §10 binary 입증 선제 적용 | ✅ | ✅ | — | 일치(단, 결함 #8) |
| 6 | **"ADR-012 차단조건 #2" citation stale** | ✅ | ✅ | — | **일치(BLOCKING BI5C-1)** |
| 7 | §8 origin replace = BI-4 §8 cross-ref 정확 | ✅ | ✅ | — | **일치** |
| 8 | **owner self-bypass §10/§12 누락** | △ | ✅ | ✅ | **부분→통합 BLOCKING BI5C-2** |
| 9 | AE-3 "BI-4 §6.2" 재검증 | 권고 | 권고 | — | **불일치→기각(실재)** |
| 10 | §7 Evidence Ledger 통합 vs 분리 | ✅ | ✅ | — | 부분(권고) |
| 11 | AE-4/AE-6 write 주체 미명세 | ✅ | — | — | 누락(A 단독)→BI5C-3 |
| 12 | AE-5 격리위반 기록 재귀 의존 | — | ✅ | — | 누락(B 단독)→권고 |
| 13 | TSA backdating 차단(hash chain 못막음) | — | — | ✅ | 누락(C 단독, 중요) |
| 14 | 다중 vendor 미러 §4 1급 격상 | — | — | ✅ | 누락(C 단독, 중요)→BI5C-4 |
| 15 | Merkle/per-entry signing/WORM | — | — | ✅ | 누락(C 단독, MVP-6) |
| 16 | audit 매체 2층 추상화 미적용(PL) | — | — | ✅ | 누락(C 단독, 중요) |
| 17 | Rekor = audit self-bypass 유일 해소 | — | — | ✅ | 부분(→#8 통합) |

**집계: 일치 6 / 부분 3 / 불일치 1 / 누락 7**

---

## 3. 최종 판정 — APPROVE WITH CONDITIONS

### BLOCKING 4건 (BI5C-1~4)

| # | 조건 |
|---|----|
| **BI5C-1** | §7 line 162 / §12.1 line 217 / 부록 A line 258 "ADR-012 차단조건 #2" → **"ADR-012 원칙 5 (Hermes 의존 0) + 원칙 3 (Hermes 승인/수정 불가) — ADR-008 차단조건 #2 답습"** 정정. BI-4 §11.3·BI-3 N-2 동형 (정정 = 별도 단계, 본 합의는 지목까지) |
| **BI5C-2** ⭐ | **owner self-bypass 거짓 안전감 전파** — (a) §10 에 "owner 경로 = binary 입증 범위 밖"(에이전트 경로만 binary, owner 경로 = §9 수용된 SPOF) 명문 / (b) §12.2 Rollback Trigger 에 "owner 가 append-only 정책 off·hash chain 검증 off" 추가 / (c) **BI-4 self-bypass 역설("1인=admin=ruleset off")의 audit 대칭("1인=audit admin=정책 off")** 동일 강도 명문 / (d) §9 에 "Rekor(제3자) = audit self-bypass 를 audit 축에서 닫는 유일 구조적 후보, MVP-6 DEFER = audit self-bypass 잔여 수용 결정" 인과 명문 |
| **BI5C-3** | §3 AE-4(observe 통과)·AE-6(origin replace) **audit write 주체·포착 메커니즘** 명세 + §5 CT-4 격리 재귀와의 정합 확인 (write 경로가 CT-4 요구 시 충돌) |
| **BI5C-4** | §4 수단표에 **"owner 경로 방어 여부" 컬럼**(Rekor✅ / append-only remote·mount❌) + **다중 vendor remote 미러 cross-check 를 §8→§4 1급 후보 격상**(2 vendor 동시 침해 강제·무료·single-host 즉시 — Rekor OIDC 의존 없이 owner 경로 부분 완화) |

### 권고 5건 (BI5R-1~5)

| # | 권고 |
|---|----|
| **BI5R-1** | audit 매체 2층 추상화(BI-4 §7.1 동형) — 층1 신뢰 기준 중립(JSONL+JCS+sha256 이미 확보) ⊕ 층2 집행 매체 vendor(remote/WORM/Rekor/미러 후보 다수, 하드코딩 금지). audit 매체 lock-in 이 anchor 보다 무거움(과거 기록 전체+genesis+SHA 참조, 후속 74 history rewrite 금지와 충돌) 명문 |
| **BI5R-2** | RFC 3161/Roughtime TSA = hash chain backdating(genesis 재생성) 차단 후보(무료 공개 TSA, MVP-6) — §4 추가 |
| **BI5R-3** | Merkle tree(inclusion proof, MVP-6) / per-entry signing(Hermes 서명 시 CT-4 회귀 주의) / WORM Object Lock(root 삭제 불가) 후보 보존 |
| **BI5R-4** | AE-5(격리위반 탐지 기록) 무결성이 §5 CT-4 격리에 재귀 의존(sink 자기참조) 명문 |
| **BI5R-5** | Evidence Ledger 통합/분리 결정 시 ADR-012 §2.2 enum #9/#16 중첩 + §3.2 schema 진화 절차 의존성 + "단일 sink = blast radius 확대" trade-off entry gate 명문 |

### 거짓 안전감 차단 (핵심 평가)
**BI5C-2 가 본 brief 의 핵심 결함.** §6 완전성 FN(audit≠완전, BI-7 귀속)은 다층 명문되어 모범적이나, **§9 single-host self-bypass(owner 경로) 거짓 안전감이 §10 binary·§12 Rollback Trigger 까지 전파되지 않은 비대칭** — §10 4시연·§12 4 Trigger 가 전부 에이전트 주어인 탓에 "에이전트 시연 통과 = audit 무결성 확정"으로 미끄러질 표면 잔존. B(명문 누락)·C(Rekor=유일 해소·DEFER=수용 결정)가 서로 다른 입구로 동일 지점 수렴 = 후속 71~72 "수단 라벨 ≠ 입증, 침투 시연 + guardrail 한 묶음" 원칙의 audit 축 적용.

---

## 4. 종합 결론

BI-5 brief v1 은 audit sink 의 3 무결성 속성·CT-4 재귀 닫힘·완전성 FN 경계·binary 선제 적용을 출처(`f29c772`·ADR-012·G4·BI-3/BI-4 brief)와 정확히 정합시킨 견고한 심화 문서로 **APPROVE WITH CONDITIONS** 가 타당하다. 가장 무게 있는 발견 둘: ① "ADR-012 차단조건 #2" citation 이 직접 grep 결과 ADR-008 소속이고 "Hermes 의존 0"은 ADR-012 원칙 5 임이 확정되어 BI-4 §11.3·BI-3 N-2 와 동형의 반복 stale 패턴(BI5C-1), ② §6 완전성 FN 거짓 안전감은 모범적으로 차단됐으나 §9 owner self-bypass 거짓 안전감이 §10 binary·§12 Rollback Trigger 까지 전파되지 않아 "에이전트 경로 시연 통과 = audit 안전 확정"으로 미끄러지는 비대칭(BI5C-2, B 명문 누락 + C Rekor=유일 구조적 해소·DEFER=수용 결정 통합)이다. AE-4/AE-6 audit write 주체 미명세(BI5C-3)와 §4 owner 경로 방어 컬럼 + 다중 vendor 미러 1급 격상(BI5C-4)을 더해 BLOCKING 4건, 권고 5건이다. AE-3 "BI-4 §6.2" citation 은 재검증 결과 실재로 기각. 교차 = 일치 6 / 부분 3 / 불일치 1 / 누락 7. 본 합의는 추론적 검증(권고) 한정이며 citation 정정·owner self-bypass 명문·AE write 주체 명세·수단표 보강·수단 결정·실 변경·commit·push 는 모두 사용자 명시 + 별도 단계이고, 본 보고서는 어떤 파일도 편집/생성하지 않았다.

---

## 부록 — Agent 관점 요약

| Agent | 관점 | 핵심 |
|------|------|------|
| **A** (구현) | "동작하는가?" | 골격 기술 정확(3속성·hash chain ⊥ 매체·CT-4 닫힘·SHA 10/10). BI5C-1 citation stale / AE-4·AE-6 write 주체 미명세 |
| **B** (안전성) | "견고한가?" | §6 완전성 FN·§10 binary 선제 모범. BI5C-1 citation / **BI5C-2 owner self-bypass §10·§12 미전파** / §4 owner 방어 컬럼 / AE-5 재귀 |
| **C** (대안) | "더 나은 방법?" | **Rekor=audit self-bypass 유일 구조적 해소(DEFER=수용 결정)** / 다중 미러·WORM·TSA·Merkle 누락 / audit 2층 추상화 미적용(PL) |
| **Reviewer** | "최선 합의?" | 직접 grep 재검증(citation 확정·AE-3 기각·BB-2≡C 통합 판정) → APPROVE WITH CONDITIONS, BLOCKING 4 + 권고 5 |
