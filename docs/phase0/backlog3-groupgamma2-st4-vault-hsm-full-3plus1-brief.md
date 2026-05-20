# Backlog #3 Group γ-2 (Vault HSM ST-4 — MVP-6 보류 확정) 단독 풀 3+1 합의 *준비* Brief (DRAFT)

> **본 brief = Backlog #3 (T3 영역) 中 *Group γ-2 (Vault HSM ST-4 — ADR-010 통합) 단독* 풀 3+1 합의 *진입 전* 정비를 위한 *준비안* (DRAFT)** — Backlog #3 T3 영역의 *마지막 진입 단위*. follow-up brief (`79c8ad6` §3.3 / §6.1 3순위) + Group α (`2026-05-14`) + Group β (`aa8a29a`) + Group γ-1 (`9b1f8cd`) 풀 3+1 발효 이후 잔여 진입 단위 中 **Group γ-2 영역만 추출 + 외부 LLM 응답 Q14/Q16/Q18 흡수 + Agent A/B/C 분배 + Reviewer 검토 의무 영역 정비** 한정. 양 vendor 종합 = **BLOCK / DEFER to MVP-6** 수렴 — 본 합의의 *핵심 의제* = **현 시점 실 진입 부적합 + MVP-6 보류 *확정* 적격성** (단, "보류 확정" 도 T3 정책 결정 → 풀 3+1 의무, §5).
>
> 본 brief 의 어떤 §도 그 자체로 (i) **내부 Agent A/B/C + Reviewer 풀 3+1 합의 보고서 *작성* / commit / push**, (ii) **Vault HSM *구현*** (실 Vault 클라이언트 / 실 HSM 환경 / App Role / Kubernetes Auth / Shamir SSS 분할 / Multi-host 인프라 구성), (iii) **ADR-010 §X 진입 섹션 *본문* 변경 / ADR-010 채택 결정 *재변경***, (iv) **Operational Readiness PASS (Layer E) 선언**, (v) **Hermes PMO 격상 (Layer F) 선언**, (vi) **MVP-6 진입 / Multi-host 전환 결정 / MVP-1 exit 발효 / MVP-2 자동 진입**, (vii) Backlog #7 (Operational Readiness parity) / Backlog #1 ST-2 / Group I 자동 진입, (viii) §C-5 / §C-5b 상태 표기 *재변경*, (ix) Layer B (`f40423f`) ST-3 docker secret 본문 채택 변경 / Layer D (`210c98f`) 본문 변경, (x) follow-up brief / Group α·β·γ-1 합의 / prep brief 계보 본문 변경, (xi) 외부 LLM 응답 (Gemini + GPT) *결론 강제 채택* (응답 = 입력 한정), (xii) 외부 LLM *추가 자동 호출* / 재의뢰, (xiii) 실 API key / provider SDK / 외부 API 호출 / 실 secret material 처리, (xiv) ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012), (xv) 도구 본문 (`tools/*.py`) / CI workflow 변경 / actual run / Production `docker-compose.yml` / `requirements*.txt` 변경, (xvi) **Phase α defer-lockdown 변경**, (xvii) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (γ-1 합의 후 옵션 (D) 답습 — Group γ-2 풀 3+1 진입 brief)
**상태**: DRAFT (사용자 명시 승인 *전*, 합의·commit·push 0건)
**관계**: follow-up brief (`79c8ad6`) §3.3 / §6.1 3순위 + Group γ-1 합의 (`9b1f8cd`) 후속 — 본문 변경 0건 + Group γ-2 단독 합의 진입 *직전* 정비 (Backlog #3 T3 마지막 진입 단위)
**상위 권위**:
- follow-up brief = `docs/phase0/backlog3-t3-zone-followup-brief.md` (`79c8ad6`, §3.3 Group γ-2 정비 + §5 풀 3+1 의무 + §6.1 3순위)
- Group γ-1 합의 = `docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md` (`9b1f8cd`, ST-1↔ST-4 책무 직교 + §6.2 cross-reference)
- Group α 합의 = `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (3/3 만장일치 형식 + §6.1 Group γ-2 cross-reference)
- Group β 합의 = `docs/review/3plus1-consensus-2026-05-20-backlog3-groupbeta-catalog-policy.md` (`aa8a29a`)
- 외부 LLM 응답 = `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gemini.md` (Q14/Q16/Q18) + `...-gpt.md` (Q14/Q16/Q18) — 양 vendor 종합 (C) PARTIAL = **BLOCK / DEFER to MVP-6** 수렴
- **ADR-010** (`ADR-010-sqlcipher-vault-key-management.md`, Vault HSM + Shamir SSS 3-of-3 채택) — §X 진입 섹션
- ADR-012 §원칙 12 (1인 동일 호스트 SPOF 면책 — 동일 호스트 전체 침해 = 방어 범위 밖, multi-host 전환 시 Layer 3/5 의무 트리거) / ADR-011 §2.4 T3 영역
- 5 영구 핵심 제약 (특히 #4 단일 source-of-truth) + Provider Liquidity 5-way

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "옵션 (D)로 진행 — Group γ-2 풀 3+1 진입 brief"

선행 답습: γ-1 합의 §8 옵션 (D) = "Group γ-2 (Vault HSM ST-4 MVP-6 보류 확정) 풀 3+1 진입 brief (양 vendor BLOCK/DEFER 답습)". T3 영역 = 보안 enforcement → CLAUDE.md §3 풀 3+1 의무 (Reviewer-only 단축 부적격, §5 답습).

### 0.2 본 brief 가 *하는* 것

1. Group γ-2 (Vault HSM ST-4) 범위 + 책무 정의 (§1) — prep brief §3.5 + ADR-010 답습 + Group γ-1 / β / Backlog #7 분리 명시
2. Vault HSM ST-4 6 결정 영역 통합 검토 (§2) — 외부 LLM Q14 6 결정 영역 답습
3. **MVP-6 보류 확정 의제 + Operational Readiness PASS / Hermes PMO 격상 경계** (§3) — 외부 LLM Q16/Q18 답습 + ADR-012 §원칙 12 SPOF
4. ST-1~ST-4 책무 분담 內 ST-4 위치 (§4) — Group γ-1 합의 ST-1↔ST-4 직교 답습
5. 합의 *단위* + 합의 *형태* 권고 (§5) — Group γ-2 *단독* + 풀 3+1 의무 (Reviewer-only 부적격, "보류 확정" 도 T3)
6. 풀 3+1 Agent A / B / C 관점 분배 + Reviewer 검토 의무 영역 (§6)
7. 외부 LLM 양 vendor 수렴 / 차이 영역 합산 (§7) — γ-2 영역만 추출 (입력 한정)
8. Rollback Trigger 통합 매트릭스 — Group γ-2 한정 (§8)
9. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

- ❌ **풀 3+1 합의 보고서 작성 / commit / push** (본 brief = untracked DRAFT 한정)
- ❌ **Vault HSM *구현*** (실 Vault 클라이언트 / 실 HSM / App Role / Kubernetes Auth / Shamir SSS 분할 / Multi-host 인프라)
- ❌ **ADR-010 §X 진입 섹션 *본문* 변경 / ADR-010 채택 결정 재변경**
- ❌ **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언**
- ❌ **MVP-6 진입 / Multi-host 전환 결정 / MVP-1 exit 발효 / MVP-2 자동 진입**
- ❌ **"MVP-6 보류 확정" *결정 발효*** (옵션 *적격성 권고* 한정 — 보류 확정 *발효* = 풀 3+1 합의 + 사용자 명시)
- ❌ **수단 *최종 결정* / Vault 인프라 형태 *고정***
- ❌ **Backlog #7 / Backlog #1 ST-2 / Group I 자동 진입**
- ❌ **Phase α defer-lockdown 변경** (별개 트랙 — 충돌 0건)
- ❌ **외부 LLM 응답 결론 강제 채택 / 추가 자동 호출**
- ❌ ADR 본문 자동 갱신 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계 — staged cycle)

### 0.4 본 brief 의 권위 한계

본 brief = **Group γ-2 단독 풀 3+1 합의 *진입 전 정비* DRAFT 한정**. 본 brief 가 발생시키는 *유일한* 효과 = **Group γ-2 합의 진입 정비 답습 한정** (Layer 0.5 가이드). 모든 *결정* (보류 확정 발효 포함) 은 *별도 풀 3+1 합의* (사용자 명시 승인 후). ⚠️ 본 brief 는 양 vendor 의 BLOCK/DEFER 수렴을 *입력 정리* 할 뿐 결론을 *선취하지 않는다* — 진입 적격성 판정은 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합에서 도출.

---

## 1. Group γ-2 (Vault HSM ST-4) 범위 + 책무 정의

### 1.1 정의 (prep brief §3.5 + ADR-010 답습)

| 영역 | 정의 |
|----|----|
| 정의 | HashiCorp Vault + HSM (Hardware Security Module) 통합 — Hermes 가 Vault 클라이언트 호출, secret 저장 = 외부 HSM (Multi-host 환경 권고). ADR-010 = SQLCipher 키 관리 = Vault HSM + Shamir SSS 3-of-3 분할 *채택 完* (§B) — ST-4 = 그 *구현 진입* (§X) |
| 현 상태 | ST-4 = Deferred (`78483c5` 답습) — Operational Readiness 영역 (MVP-6) cross-reference / Backlog #3 T3 = 본 brief 영역 |
| 책무 영역 | secret source (외부 HSM) / Multi-host 인프라 |
| T3 진입 속성 | ADR-010 §X 진입 합의 의무 ✅ HIGH / Multi-host 인프라 의무 ✅ HIGH / 운영 비용 高 ⚠️ HIGH / **Operational Readiness PASS (MVP-6) 경계 ⚠️ HIGH** / **Hermes PMO 격상 경계 ⚠️ HIGH** / 단일 source-of-truth 영향 ⚠️ MEDIUM (HSM 단일화 시 ↑) |
| ADR 권위 | ADR-010 §B (Vault HSM + Shamir SSS 채택) + §X 진입 / ADR-012 §원칙 12 (single-host SPOF 면책 + multi-host 전환 시 Layer 3/5 의무) |

### 1.2 ST 군 (secret hygiene) 답습 — γ-2 위치 (Group γ-1 합의 답습)

| ST | 역할 (Group γ-1 합의 C-Gγ1-8 답습) | 현 상태 | 본 brief 와의 관계 |
|----|----|----|----|
| ST-1 | file perm preflight guard | Group γ-1 풀 3+1 발효 (`9b1f8cd`) | **ST-1 ↔ ST-4 책무 *직교*** (perm vs secret source) — γ-1 합의 AU-4 답습 |
| ST-2 | runtime drift detection | Backlog #1 | 별도 영역 |
| ST-3 | 주 secret injection (docker secret) | Layer B 본문 채택 (`f40423f`) | single-host canonical secret source — 본문 변경 0건 |
| **ST-4** | **multi-host / production-grade root secret source** | Deferred — Backlog #3 T3 / MVP-6 cross-ref | ✅ **본 brief 영역 (Group γ-2)** |
| ST-5 | Defense in depth 통합 | MVP-2 이후 영역 | 별도 영역 |

### 1.3 잔여 Backlog #3 T3 진입 단위 中 γ-2 위치 (마지막)

| 진입 단위 | status |
|----|----|
| Group α (AR-3 + PC-4 T3 sub) | ✅ 풀 3+1 발효 (`2026-05-14`) |
| Group β (T-5 β + Tier-2/3 catalog 일반) | ✅ 풀 3+1 발효 (`2026-05-20`, `aa8a29a`) |
| Group γ-1 (C-5b ST-1) | ✅ 풀 3+1 발효 (`2026-05-20`, `9b1f8cd`) |
| **Group γ-2 (Vault HSM ST-4)** | ⏳ **본 brief 진입 정비 (3순위 — 마지막 T3 진입 단위)** |

---

## 2. Vault HSM ST-4 6 결정 영역 통합 검토 (외부 LLM Q14 답습)

| # | 결정 영역 | 옵션 후보 | T3 진입 속성 / 외부 LLM 입력 (§7 답습) |
|---|----|----|----|
| 1 | **ST-4 진입 시점** | (a) MVP-2 조기 진입 / (b) **MVP-6 Operational Readiness 발효 시** / (c) Hermes PMO 격상 후 / (d) Multi-host 전환 시점 | 양 vendor = **MVP-6 보류** (GPT: MVP-2 조기 = 과설계 / PMO 후만 = 너무 늦음 → "PMO 조건 보이면 MVP-6 선검토") |
| 2 | **Vault 인프라 형태** | (a) self-hosted Vault / (b) HCP Vault Dedicated / (c) Vault Enterprise / (d) 동등 secret manager | GPT = Vault HSM 지원 = 외부 root key storage / automatic unseal / seal wrapping = 운영 인프라 성격 (일부 Enterprise/HCP 요구) |
| 3 | **Vault client 통합 방식** | (a) Hermes 가 Vault client 호출 / (b) App Role / (c) Kubernetes Auth (ADR-010 §X) | ADR-010 §X 답습 — multi-host 인증 형태 |
| 4 | **ADR-010 §X 본문 형태** | (a) 구현 진입 섹션 신설 / (b) 참조 유지 (구현 진입 금지) | GPT = "현재: ADR-010 참조 유지, 구현 진입 금지" |
| 5 | **다른 ST 와 통합 정책** | (a) ST-4 단독 / (b) Defense in depth 역할 분담 (ST-3 주 injection / ST-4 multi-host root) | GPT Q15 = ST-4 단독 대체 부적절 + 환경별 canonical secret source |
| 6 | **Multi-host 전환 시점** | (a) 현 single-host 유지 (SPOF 의도적 수용) / (b) MVP-6 multi-host 전환 시 | ADR-012 §원칙 12 = multi-host 전환 시 Layer 3/5 의무 트리거 |

> 본 §2 = 6 결정 영역 *옵션 후보 + 입력 정리* 한정. *결정* 0건 — 풀 3+1 시 Agent A/B/C 평가 대상.

---

## 3. MVP-6 보류 확정 의제 + Operational Readiness / Hermes PMO 격상 경계 (외부 LLM Q16/Q18 답습)

### 3.1 핵심 의제 = "현 시점 실 진입 부적합 + MVP-6 보류 확정 적격성"

> 양 vendor 종합 = **BLOCK / DEFER to MVP-6** (Q14/Q16/Q18 만장 수렴). 사유: (i) 1인 개발자 **single-host 환경에서 Vault HSM = 오버엔지니어링** (Gemini) / 실효성 낮음 (GPT) + (ii) **운영 비용 高 + Multi-host 인프라 부담** + (iii) **single-host SPOF 의도적 수용 (ADR-012 §원칙 12) 과 충돌** + (iv) **Operational Readiness PASS (Backlog #7 / MVP-6) 선행 의무**.

### 3.2 Operational Readiness PASS 경계 (Q18 입력)

| 항목 | Gemini (입력) | GPT (입력) |
|----|----|----|
| ST-4 ↔ Operational Readiness | Vault HSM 도입 *전* 필수 조건 (Backlog #7 선행) | BLOCK before MVP-6, APPROVE at/after MVP-6 |
| Operational Readiness 의미 (1인) | "운영 가능성 증명" | enterprise HA 흉내 ❌ — 1인 기준 secret rotation / backup/restore / Vault 장애 fallback / audit log / 비용·복구 감당 / single-host SPOF 수용 범위 문서화 |

### 3.3 Hermes PMO 격상 경계 + Multi-host (Q16 입력)

| 항목 | 입력 |
|----|----|
| ST-4 진입 시점 | MVP-2 조기 = 과설계 / MVP-6 Operational Readiness 또는 multi-host 전환 시점 / PMO 격상 후만 = 너무 늦음 (GPT) |
| single-host SPOF | ADR-012 §원칙 12 = 동일 호스트 전체 침해 = 방어 범위 밖. **single-host SPOF 수용 상태 → HSM 핵심 이점 약화** (GPT) — 중요한 것은 secret 파일 권한 (ST-1) / docker secret (ST-3) / audit log / backup/restore / rotation |
| Multi-host 전환 | multi-host 전환 시 ADR-012 Layer 3 (signed commit) / Layer 5 (external anchor) 의무 발동 트리거 — ST-4 필요성 재평가 |

### 3.4 ⚠️ "보류 확정" 도 T3 정책 결정 (follow-up brief §5.3 답습)

> Group α 합의 §8 옵션 (H) 는 γ-2 를 "Reviewer-only 단축 합의 적격 여부 *검토*" 로 표기. **단, 사용자 명시 (2026-05-20) 답습 — T3 영역 = 풀 3+1 의무.** Vault HSM "MVP-6 보류 확정" 도 (a) Vault HSM = T3 영역 + (b) ADR-010 §X 진입 경계 + (c) Operational Readiness (Layer E) / Hermes PMO 격상 (Layer F) 경계가 걸린 *T3 정책 결정* → **풀 3+1 의무**. "보류 확정 = 수단 결정 0건이므로 단축 적격" 여부 자체도 *풀 3+1 안에서* 판정 (사전 단축 추정 금지).

---

## 4. ST-1~ST-4 책무 분담 內 ST-4 위치 (Group γ-1 합의 답습)

| ST | 역할 | 환경 | ST-4 와의 관계 |
|----|----|----|----|
| ST-3 docker secret | 주 secret injection | single-host (현) | ST-4 = ST-3 대체 아님 (단독 대체 금지) — multi-host 전환 시 root secret source 보강 |
| ST-1 file perm | preflight guard | dev=warn/CI=fail-closed | **ST-1 ↔ ST-4 책무 *직교*** (perm vs secret source — γ-1 합의 AU-4) — ST-4 보류가 ST-1 진입 안 막음 (역도 성립) |
| ST-2 inotify | runtime drift | Backlog #1 | 별도 영역 |
| **ST-4 Vault HSM** | **multi-host root secret source** | **multi-host (MVP-6)** | 단독 대체 금지 + Defense in depth 최종 단계 (Gemini "모든 것 갖춰진 후") |

> **합의 도출 의무 (풀 3+1)**: ST-4 단독으로 ST-1/ST-3 대체 금지 + single-host 에서 ST-3 (docker secret) + ST-1 (file perm) 이 canonical secret source → ST-4 = multi-host 전환 시점의 root secret source 보강 (환경별 canonical source 명시, γ-1 합의 C-Gγ1-8 답습).

---

## 5. 합의 단위 + 합의 형태 권고

### 5.1 합의 단위 = Group γ-2 *단독* (Backlog #3 T3 마지막 진입 단위)

GPT γ-1/γ-2 분리 권고 흡수 (γ-1 합의 답습) — ST-4 = 인프라·운영·비용·PMO 경계가 모두 걸린 큰 결정 → ST-1 (γ-1, 발효) 과 별도 단위. **Group γ-2 단독 진입** = Backlog #3 T3 영역 최종 진입 단위.

### 5.2 합의 형태 = 풀 3+1 *의무* (Reviewer-only 단축 *부적격*)

| 트리거 | γ-2 발화 |
|----|----|
| #2 T3 영역 자동 진입 | ✅ **HIGH (BLOCKING)** — Vault HSM = ADR-010 §X 진입 = T3 영역 |
| #4 Provider Liquidity 5-way 약화 | ❌ 영향 없음 (secret source 영역) |
| #5 5 영구 핵심 제약 약화 | ⚠️ MEDIUM — 단일 source-of-truth (HSM 단일화 ↑ / HSM SPOF) |
| #6 Operational Readiness PASS / Hermes PMO 격상 경계 | ✅ **HIGH** — ST-4 = Layer E / Layer F 경계 직결 |
| #7 외부 LLM cross-vendor blind 없는 T3 결정 | ✅ HIGH — 응답 2건 회수 完 → 풀 3+1 *입력* 답습 |

**합산**: 트리거 #2 (BLOCKING) + #6 (HIGH) → **풀 3+1 (Agent A/B/C + Reviewer) + 외부 LLM 1+ (입력 답습) + 사용자 명시 의무 확정. Reviewer-only 단축 부적격** (보류 확정도 §3.4 답습 — T3 정책 결정).

---

## 6. 풀 3+1 Agent A / B / C 관점 분배 + Reviewer 검토 의무 영역

| Agent | 관점 | 분석 영역 (γ-2) |
|----|----|----|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | Vault HSM 실 구현 기술 요구 (App Role / Kubernetes Auth / Shamir SSS 3-of-3) + single-host 에서 Vault HSM 실효성 + 운영 비용 정량 (인프라 / unseal / seal wrapping) + Vault Enterprise/HCP 요구 + Vault 장애 fallback 기술 |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | **HSM SPOF / Vault inaccessible fallback** + single-host SPOF (ADR-012 §원칙 12) 과 충돌 + 단일 source-of-truth (HSM 단일화) + HSM key 관리 / audit log + Operational Readiness PASS 경계 안전성 + Hermes ≠ root of trust (Vault = secret source root custody) |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | single-host 대안 (ST-3 docker secret + Shamir SSS 로컬 / PGP 봉인 백업, ADR-010 §B 답습) + MVP-6 보류 vs 부분 진입 vs 전면 보류 트레이드오프 + Multi-host 전환 시점 대안 + 신규 영역 발굴 (예: secret rotation/backup/restore 1인 기준 정의 / Vault 장애 fallback 정책) |
| Reviewer | "최선의 합의는?" | 3 출력 교차 비교 + 일치/부분/불일치/누락 + 6 결정 영역 최종 합의 권고 + **MVP-6 보류 확정 적격성 판정** (보류 확정 ≠ MVP-6 진입 / Operational Readiness PASS) |

---

## 7. 외부 LLM 양 vendor 수렴 / 차이 영역 (γ-2 추출, 입력 한정)

### 7.1 수렴 영역

| 영역 | Gemini | GPT | 수렴 |
|----|----|----|----|
| 종합 (γ-2) | 현 시점 도입 보류 (MVP-6 이후) | BLOCK / DEFER until MVP-6 | ✅ **MVP-6 보류** |
| single-host 실효성 | 오버엔지니어링 (SPOF 의도적 수용 충돌) | 실효성 낮음 (SPOF 수용 시 HSM 이점 약화) | ✅ single-host 부적합 |
| 운영 비용 | 인프라 비용·관리 복잡도만 증가 | 운영 비용 큼 (Enterprise/HCP 요구) | ✅ 운영 비용 高 |
| Operational Readiness 경계 | Vault HSM 도입 전 필수 조건 (Backlog #7 선행) | BLOCK before MVP-6, APPROVE at/after | ✅ Operational Readiness PASS 선행 |
| ST 통합 | ST-4 = 모든 것 갖춰진 후 최종 단계 | ST-4 단독 대체 부적절 / multi-host root | ✅ 단독 대체 금지 + 최종 단계 |
| 진입 시점 | MVP-6 이후 재검토 | MVP-6 / multi-host 전환 / PMO 조건 보이면 MVP-6 선검토 | ✅ MVP-6 |

### 7.2 차이 영역 (경미 — 0~1건)

| 영역 | Gemini | GPT | 본 brief 정비 (입력 한정) |
|----|----|----|----|
| 메타-템플릿 상징성 | 상징성 있으나 실질 이득 낮음 | (미언급) | 경미 — 풀 3+1 평가 시 1인 환경 실 이득 기준 평가 |

> 외부 LLM 응답 = *입력 한정* (강제 채택 0건). 양 vendor 강한 수렴 (BLOCK/DEFER) — 단 본 brief 는 결론을 *선취하지 않음* (§0.4). 풀 3+1 Agent A/B/C 독립 평가 대상.

---

## 8. Rollback Trigger 통합 매트릭스 (Group γ-2 한정)

| Trigger | 발화 조건 | 발화 시 행동 |
|----|----|----|
| **ADR-011 §2.4** | T3 영역 (Vault HSM ADR-010 §X 진입) 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
| **ADR-010 §X** | Vault HSM 실 구현 진입 결정 | 풀 3+1 + Operational Readiness PASS 선행 |
| **R-ST4-MVP6-BOUNDARY** (신규 후보) | ST-4 ↔ MVP-6 Operational Readiness 연결 | MVP-6 발효 + Backlog #7 선행 + 별도 풀 3+1 |
| **R-ST4-MULTIHOST** (신규 후보) | Multi-host 전환 결정 | ADR-012 §원칙 12 Layer 3/5 의무 발동 + ST-4 필요성 재평가 |
| **R-ST4-PMO-BOUNDARY** (신규 후보) | ST-4 ↔ Hermes PMO 격상 연결 | PMO 격상 자동 연결 금지 — 별도 풀 3+1 + 외부 LLM 2+ |

### 8.1 후속 단계 Rollback Trigger (본 brief 영역 외)

| 영역 | 후속 Rollback Trigger | 분리 사유 |
|----|----|----|
| Vault HSM 실 구현 | ADR-010 §X + Operational Readiness PASS + Multi-host + 별도 풀 3+1 + 사용자 명시 | MVP-6 영역 |
| Operational Readiness PASS (Layer E) | Backlog #7 + MVP-6 | Layer E 영역 |
| Hermes PMO 격상 (Layer F) | MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 | Layer F 영역 |
| Multi-host 전환 | ADR-012 §원칙 12 Layer 3/5 의무 | Multi-host 영역 |

---

## 9. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|----|----|----|
| **(A)** | 본 brief 그대로 승인 → **Group γ-2 풀 3+1 합의 진입** (Agent A/B/C + Reviewer, 외부 LLM 응답 입력 답습 — MVP-6 보류 확정 적격성 판정) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 brief 승인 → commit (`docs/phase0/backlog3-groupgamma2-st4-vault-hsm-full-3plus1-brief.md`) *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (D) | 본 brief 보류 → **GP-3 C-3 / GP-5 C-2 condition row 갱신 합의** (해소 선언 — α+β+γ-1[+γ-2] 발효 답습) | GP entry 갱신 |
| (E) | 본 brief 보류 → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief** | Group I |
| (F) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 합의 / commit / push = 사용자 명시 승인 후 별도 단계. T3 영역 합의 = **풀 3+1 의무** (§5). 본 brief 완료 시 Backlog #3 T3 4 진입 단위 (α/β/γ-1/γ-2) brief·합의 영역 모두 정비.

---

## 10. 한 단락 요약

Backlog #3 T3 영역 中 Group γ-2 (Vault HSM ST-4 — ADR-010 SQLCipher 키 관리 Vault HSM + Shamir SSS 채택의 *구현 진입*) 단독 풀 3+1 합의 *진입 전 정비* DRAFT — Backlog #3 T3 영역의 *마지막 진입 단위* (Group α `2026-05-14` + β `aa8a29a` + γ-1 `9b1f8cd` 발효 이후). 6 결정 영역 = ST-4 진입 시점 / Vault 인프라 형태 / Vault client 통합 방식 / ADR-010 §X 본문 형태 / 다른 ST 통합 / Multi-host 전환 시점. 외부 LLM 응답 2건 (Gemini + GPT, 2026-05-13) 은 γ-2 에 대해 **BLOCK / DEFER to MVP-6** 으로 강하게 수렴 — 1인 single-host 환경에서 Vault HSM = 오버엔지니어링/실효성 낮음 + 운영 비용 高 + Multi-host 인프라 부담 + single-host SPOF 의도적 수용 (ADR-012 §원칙 12) 과 충돌 + Operational Readiness PASS (Backlog #7 / MVP-6) 선행 의무. 따라서 본 합의의 *핵심 의제* = **현 시점 실 진입 부적합 + MVP-6 보류 *확정* 적격성** (보류 확정 ≠ MVP-6 진입 / Operational Readiness PASS — single-host 에서는 ST-3 docker secret + ST-1 file perm 이 canonical secret source). ST-1 ↔ ST-4 책무 *직교* (γ-1 합의 AU-4 답습) — ST-4 보류가 ST-1 진입을 안 막고 역도 성립. ⚠️ "MVP-6 보류 확정" 도 (a) Vault HSM = T3 영역 + (b) ADR-010 §X 진입 경계 + (c) Operational Readiness (Layer E) / Hermes PMO 격상 (Layer F) 경계가 걸린 *T3 정책 결정* → **풀 3+1 (Agent A/B/C + Reviewer) 의무, Reviewer-only 단축 부적격** (트리거 #2 BLOCKING + #6 Layer E/F 경계 HIGH). 본 brief 는 양 vendor BLOCK/DEFER 수렴을 *입력 정리* 할 뿐 결론을 *선취하지 않으며*, 진입 적격성 판정은 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합에서 도출. 본 brief = 진입 정비 DRAFT 한정 — 합의 보고서 작성 / commit / push / Vault HSM 구현 / ADR-010 §X 본문 변경 / Operational Readiness PASS / Hermes PMO 격상 / MVP-6 진입 / Multi-host 전환 / MVP-1 exit / 수단 최종 결정 / actual run / CI workflow 변경 / Phase α defer-lockdown 변경 / 외부 LLM 강제 채택 모두 0건이며, 모든 *결정* (보류 확정 발효 포함) 은 별도 풀 3+1 합의 (사용자 명시 승인 후).

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|----|----|
| `backlog3-t3-zone-followup-brief.md` (`79c8ad6`) | §3.3 Group γ-2 정비 + §5 풀 3+1 의무 + §6.1 3순위 |
| `3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md` (`9b1f8cd`) | ST-1↔ST-4 책무 직교 (AU-4) + §6.2 cross-reference + 풀 3+1 형식 |
| `3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` | Group α 3/3 만장일치 형식 + §6.1 Group γ-2 cross-reference |
| `2026-05-13-backlog3-t3-zone-review-response-gemini.md` | Q14 / Q16 / Q18 (입력 한정) |
| `2026-05-13-backlog3-t3-zone-review-response-gpt.md` | Q14 / Q16 / Q18 (입력 한정) |
| prep brief v1 `ad9a02d` §3.5 | (5) Vault HSM ST-4 정의 |
| `ADR-010-sqlcipher-vault-key-management.md` §B + §X | Vault HSM + Shamir SSS 채택 + 진입 |
| ADR-012 §원칙 12 | single-host SPOF 면책 + multi-host 전환 시 Layer 3/5 의무 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
풀 3+1 합의 보고서 작성 / commit / push / Vault HSM 구현 (실 Vault 클라이언트 / 실 HSM / App Role / Kubernetes Auth / Shamir SSS 분할 / Multi-host 인프라) / ADR-010 §X 진입 섹션 본문 변경 / ADR-010 채택 결정 재변경 / "MVP-6 보류 확정" 결정 발효 / 수단 최종 결정 / Vault 인프라 형태 고정 / Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언 / MVP-6 진입 / Multi-host 전환 결정 / MVP-1 exit 발효 / MVP-2 자동 진입 / Backlog #7·Backlog #1 ST-2·Group I 자동 진입 / §C-5·§C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경 / Layer D 본문 변경 / follow-up brief·Group α·β·γ-1 합의·prep brief 계보 본문 변경 / actual run / CI workflow 변경 / Production docker-compose 변경 / `requirements*.txt` 변경 / Phase α defer-lockdown 변경 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / ADR 본문 자동 갱신 (ADR-008/010/011/012) / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
