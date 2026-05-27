# Backlog #3 Group γ-2 (Vault HSM ST-4 — MVP-6 보류 확정) 단독 풀 3+1 합의 보고서

> **본 합의 = Backlog #3 (T3 영역) 中 Group γ-2 (Vault HSM ST-4 — ADR-010 SQLCipher 키 관리 Vault HSM + Shamir SSS 채택의 *구현 진입*) *수단 결정 적격성 권위 권고* 발행 한정** — Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) Phase 2 (Independent Analysis, 병렬 독립 분석) + Reviewer (검토 에이전트) Phase 3-4 (교차 비교 + 합의 도출) 통합. **3/3 만장일치 = BLOCK / DEFER — MVP-6 보류 (trigger 기반 조건부 진입 등록) APPROVE WITH CONDITIONS**. Backlog #3 T3 영역의 *마지막 진입 단위* (α/β/γ-1/γ-2 4 단위 완료).
>
> 본 합의의 어떤 §도 그 자체로 (i) **Vault HSM *구현*** (실 Vault 클라이언트 / 실 HSM / App Role / Kubernetes Auth / Shamir SSS 분할 / Multi-host 인프라), (ii) **ADR-010 §X 진입 섹션 *본문* 변경 / ADR-010 채택 결정 (§B) *재변경***, (iii) **"MVP-6 보류 확정" *결정 발효* (보류 형태·trigger 등록 포함)**, (iv) **Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언**, (v) **MVP-6 진입 / Multi-host 전환 결정 / MVP-1 exit 발효 / MVP-2 자동 진입**, (vi) 수단 *최종 결정* / Vault 인프라 형태 *고정*, (vii) Backlog #7 / Backlog #1 ST-2 / Group I 자동 진입, (viii) §C-5 / §C-5b 상태 표기 *재변경*, (ix) Layer B (`f40423f`) ST-3 docker secret 본문 채택 변경 / Layer D (`210c98f`) 본문 변경, (x) follow-up brief / Group α·β·γ-1 합의 / γ-2 brief / prep brief 계보 본문 변경, (xi) 외부 LLM 응답 (Gemini + GPT) *결론 강제 채택* (응답 = 입력 한정), (xii) 외부 LLM *추가 자동 호출* / 재의뢰, (xiii) 실 API key / provider SDK / 외부 API 호출 / 실 secret material 처리, (xiv) ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012), (xv) 도구 본문 (`tools/*.py`) / CI workflow 변경 / actual run / Production `docker-compose.yml` / `requirements*.txt` 변경, (xvi) **Phase α defer-lockdown 변경**, (xvii) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (Group γ-2 풀 3+1 합의 진입 — γ-2 brief 옵션 (A) 답습)
**상태**: APPROVED WITH CONDITIONS (BLOCK/DEFER) — Phase 5 (Report) 완료 + 사용자 명시 승인 *전*, commit 0건
**합의 판정**: **BLOCK / DEFER — MVP-6 보류 (trigger 기반 조건부 진입 등록) APPROVE WITH CONDITIONS** (Agent A + Agent B + Agent C **3/3 만장일치 보류 수렴**)
**합의 영역**: Group γ-2 (Vault HSM ST-4) **수단 결정 적격성 권위 권고 + MVP-6 보류 확정 적격성 판정 한정** — Vault HSM 구현 / ADR-010 §X 본문 변경 / 보류 발효 0건
**상위 권위**:
- 진입 brief (본 합의 직접 source) = `docs/phase0/backlog3-groupgamma2-st4-vault-hsm-full-3plus1-brief.md` (`9b1f8cd` 이후 untracked, §1~§9 + 옵션 (A))
- Group γ-1 합의 = `docs/review/3plus1-consensus-2026-05-20-backlog3-groupgamma1-st1-hermes-perm.md` (`9b1f8cd`, ST-1↔ST-4 직교 AU-4 + Hermes ≠ root of trust 답습)
- Group α 합의 (`2026-05-14`) + Group β 합의 (`aa8a29a`) — 풀 3+1 형식 답습
- 외부 LLM 응답 = `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gemini.md` (Q14/Q16/Q18) + `...-gpt.md` (Q14/Q16/Q18) — 양 vendor 종합 (C) PARTIAL = **BLOCK / DEFER to MVP-6** 수렴
- **ADR-010** (`ADR-010-sqlcipher-vault-key-management.md`, Vault HSM + Shamir SSS 3-of-3 채택 §B + 운영 인프라 + §부정적 "Vault = 신규 SPOF" 자인) — §X 진입
- ADR-012 §원칙 12 (1인 동일 호스트 SPOF 면책 + multi-host 전환 시 Layer 3/5 의무 트리거) / ADR-011 §2.1 (a)~(d) 4조건 [+ (e) 합의 APPROVE 패턴] + §2.4 T3 영역 / ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + P3 (37번째 entry R-S1 정정 답습)
- 5 영구 핵심 제약 (특히 #1 Hermes ≠ root of trust + #4 단일 source-of-truth) + Provider Liquidity 5-way

---

## 0. 본 합의의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "옵션 (A)로 진행 — Group γ-2 풀 3+1 합의 진입"

선행 명령: "옵션 (D)로 진행 — Group γ-2 풀 3+1 진입 brief" → γ-2 brief 작성 → 옵션 (A) 합의 진입. T3 영역 = 보안 enforcement → CLAUDE.md §3 풀 3+1 의무 (Reviewer-only 단축 부적격, §5 답습 — "보류 확정" 도 T3 정책 결정).

### 0.2 본 합의가 *하는* 것

1. Phase 1 (Distribution) — γ-2 brief + 3 Agent 관점 분배 답습 (§1)
2. Phase 2 (Independent Analysis) — Agent A / B / C 병렬 독립 분석 결과 요약 (§2)
3. Phase 3 (Cross-Comparison) — 일치 / 부분 / 불일치 / 누락 분류 (§3)
4. Phase 4 (Consensus Resolution) — 최종 판단 + 12 합의 조건 (§4)
5. Phase 5 (Report) — 6 결정 영역 *최종 합의 권고* (§5)
6. single-host SPOF (ADR-012 §원칙 12) + Operational Readiness / PMO 경계 + cross-reference (§6)
7. Rollback Trigger 통합 매트릭스 (Agent C 신규 trigger 흡수) (§7)
8. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§8)
9. 메타 검증 (§9) / 합의 요약 한 단락 (§10) / 부록 A·B

### 0.3 본 합의가 *하지 않는* 것 (사용자 명시 영구 답습)

| # | 금지 | 본 합의 위반 |
|---|------|------------|
| 1 | **Vault HSM 구현** (실 Vault 클라이언트 / 실 HSM / App Role / Kubernetes Auth / Shamir SSS 분할 / Multi-host 인프라) | 0건 (수단 적격성 권고 한정) |
| 2 | **ADR-010 §X 진입 섹션 본문 변경 / ADR-010 채택 결정 (§B) 재변경** | 0건 (참조 유지, §B 유효) |
| 3 | **"MVP-6 보류 확정" *결정 발효* (보류 형태·trigger 등록 포함)** | 0건 (보류 적격성 *판정* — 발효 = 풀 3+1 + 사용자 명시 별도 단계) |
| 4 | **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언** | 0건 |
| 5 | **MVP-6 진입 / Multi-host 전환 결정 / MVP-1 exit 발효 / MVP-2 자동 진입** | 0건 |
| 6 | **수단 *최종 결정* / Vault 인프라 형태 *고정*** | 0건 (옵션 적격성 권고) |
| 7 | **Backlog #7 / Backlog #1 ST-2 / Group I 자동 진입** | 0건 |
| 8 | **§C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경 / Layer D 본문 변경** | 0건 |
| 9 | **CI workflow 변경 / actual run / 도구 본문 / Production `docker-compose.yml` / `requirements*.txt` 변경** | 0건 (Agent A read-only 실행) |
| 10 | **Phase α defer-lockdown 변경** | 0건 (별개 트랙) |
| 11 | 외부 LLM 응답 *결론 강제 채택* / 추가 자동 호출 | 0건 (입력 한정 — 본 합의는 결론 선취 0건, 독립 평가) |
| 12 | follow-up brief / Group α·β·γ-1 합의 / γ-2 brief / prep brief 계보 본문 변경 / ADR 본문 자동 갱신 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화 | 0건 |

### 0.4 본 합의의 권위 한계

- 본 합의 = **수단 결정 적격성 권위 권고 + MVP-6 보류 확정 적격성 *판정* 한정** (Group α/β/γ-1 합의 패턴 답습).
- 본 합의 발효 ≠ 실 구현 / Vault HSM 도입 / 보류 *발효*. 보류 확정 *발효* = 풀 3+1 + 사용자 명시 별도 단계. 실 진입 = **multi-host 전환 + Operational Readiness PASS (Layer E) 선행 + ADR-010 §X 합의 + 사용자 명시**.
- 외부 LLM 응답 (Gemini + GPT) = *입력* 한정 — 결론 강제 채택 0건. 본 합의는 양 vendor BLOCK/DEFER 를 *맹종하지 않고* 3 Agent 독립 분석에서 동일 결론 도출.
- Group γ-2 = Backlog #3 T3 마지막 진입 단위 — 본 합의로 4 진입 단위 (α/β/γ-1/γ-2) brief·합의 영역 모두 정비 완료.

---

## 1. Phase 1 (Distribution) — γ-2 brief + 3 Agent 관점 분배

### 1.1 본 합의 진입 source

| 영역 | 답습 |
|------|------|
| 진입 brief | `backlog3-groupgamma2-st4-vault-hsm-full-3plus1-brief.md` (§2 6 결정 영역 + §3 MVP-6 보류·경계 + §4 ST 책무 + §6 Agent 분배) |
| 합의 단위 | **Group γ-2 단독** (Vault HSM ST-4) — Backlog #3 T3 마지막 진입 단위 |
| 합의 형태 | 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 ("보류 확정" 도 T3 → 풀 3+1 의무) |
| 6 결정 영역 | ST-4 진입 시점 / Vault 인프라 형태 / Vault client 통합 방식 / ADR-010 §X 본문 형태 / 다른 ST 통합 / Multi-host 전환 시점 |

### 1.2 3 Agent 관점 분배 + 외부 LLM 응답 (입력 한정)

| Agent | 관점 | 판정 |
|-------|------|----|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | **DEFER to MVP-6** (+ multi-host) |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | **BLOCK / DEFER + 보류 확정 APPROVE WITH CONDITIONS** |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | **DEFER — trigger 기반 조건부 진입 등록 (중간안)** |
| Reviewer | 검토 에이전트 | 3 출력 교차 비교 + 최종 합의 + MVP-6 보류 확정 적격성 판정 |

| Vendor | 종합 판정 (입력) |
|------|----|
| Gemini 3 Flash | (C) PARTIAL — 현 시점 도입 보류 (MVP-6 이후) + single-host 오버엔지니어링 + SPOF 충돌 + 운영 비용 증가 + Operational Readiness 도입 전 필수 |
| GPT-5.5 Thinking | (C) PARTIAL — BLOCK/DEFER until MVP-6 + single-host SPOF 수용 시 HSM 이점 약화 + Enterprise/HCP 요구 + Operational Readiness PASS 선행 |
| **양 vendor 수렴** | **BLOCK / DEFER to MVP-6** + single-host 부적합 + 운영 비용 高 + Operational Readiness 선행 + ST-4 단독 대체 금지 |
| **차이 영역** | 경미 (0~1) — Gemini "메타-템플릿 상징성" 언급 (실 이득 낮음) |

---

## 2. Phase 2 (Independent Analysis) 결과 요약

### 2.1 Agent A (구현 분석가) — DEFER to MVP-6

| 영역 | Agent A 분석 |
|------|----|
| 종합 판정 | **DEFER (to MVP-6 Operational Readiness / multi-host 전환)** — MVP-6 보류 확정 적격성 = 기술 APPROVE |
| 사유 | single-host 에서 Vault HSM = 기술 ROI 음수 + ADR-010 운영 인프라 (Vault 2 인스턴스 + Consul + audit sink + PGP 운영자 2명 + 별도 권한 백업) 가 현 src/ 0줄 + single-host 와 정면 미스매치 |
| **결정적 기술 발견** | (1) **통합 대상 부재** — Hermes 컨테이너 / Vault client 코드 0줄 (현 src/ = LLM facade 1개) / (2) **single-host HSM 3대 기능 무력화** — external root key storage / automatic unseal / seal wrapping 모두 동일 침해 경계로 무력 / (3) **PGP 운영자 2명 전제 (ADR-010 §운영) = 1인 환경 구조적 불충족** |
| 운영 비용 정량 | Vault 2 인스턴스 + unseal + Shamir 3-of-3 (~100 LOC) + PGP 운영자 2명 (불충족) + audit sink + 90일 rotation + 분기 sample restore + Enterprise/HCP 라이선스 = 1인 운영 부담 HIGH |
| 기술 차단 요인 | 완화 불가 HIGH 3건 (통합 대상 부재 / single-host HSM 실효 무력화 / PGP 2명 전제) → 현 시점 실 진입 기술 부적합 확정 |
| 진입 조건 | C-Aγ2-1~7 |

### 2.2 Agent B (품질/안전성 검증가) — BLOCK / DEFER + 보류 확정 APPROVE WITH CONDITIONS

| 영역 | Agent B 분석 |
|------|----|
| 종합 판정 | **BLOCK / DEFER (현 시점 실 진입 부적합) + MVP-6 보류 확정 적격성 APPROVE WITH CONDITIONS** |
| 사유 | single-host SPOF 의도적 수용 (ADR-012 §원칙 12) 상태에서 Vault HSM = secret 보호 목적 *추가 달성 없이* 신규 SPOF + root key custody 위계 모호 + 운영 부담 → **안전 순이득 음수**. 단 ST-3+ST-1 이 single-host canonical → 보호 목적 약화 0건 |
| 5 영구 핵심 제약 | **① Hermes ≠ root of trust HIGH (blocking)** — Vault root token/unseal 보유 시 Hermes root 격상 (App Role short-lived + unseal 미보유 명시) / **② 수단-목적 분리 HIGH** — single-host 에서 ST-3 가 목적 달성 → ST-4 가 ST-3 대비 우월 X (ADR-011 §2.1 (a) 비교표) / **④ 단일 source-of-truth MEDIUM 양방향** — HSM 단일화 ↑ vs Vault 자체 신규 SPOF ↓ / ③ LOW / ⑤ 무영향 |
| 위험 7 영역 | HIGH 6 + MEDIUM — **완화 불가 HIGH = R-γ2-3 (single-host 구조적 한계, multi-host 로만 해소) 1건** |
| 엣지케이스 | HSM SPOF / Vault inaccessible fallback (1인 3-of-3 SSS 분산 효과 0) / audit log 1인 attribution 제한 / 3-of-3→2-of-3 트레이드오프 / dual-key 회전 중 침해 |
| 문서 정합성 지적 | **ADR-011 §2.1 본문 = (a)~(d) 4조건 / "5조건" = (e) 합의 APPROVE 패턴 포함분** — 진입 합의 작성 시 "4조건(본문) + (e) 합의 패턴" 구분 명시 권고 (Group β 합의 G-4 답습) |
| 진입 조건 | C-B-1~9 (blocking = C-B-1 Hermes≠root / C-B-2 수단-목적 / C-B-3 multi-host 시점 / C-B-4 Operational Readiness 선행) |

### 2.3 Agent C (대안 탐색가) — DEFER (trigger 기반 조건부 진입 등록 중간안)

| 영역 | Agent C 분석 |
|------|----|
| 종합 판정 | **DEFER to MVP-6 — 단 "보류 *확정*" (이진 결론) 보다 "ADR-010 §X 진입 *trigger 명시* + 구현 보류" *중간안* 우월** |
| 사유 | 진입 시점 보류는 정당 / "시점 (MVP-6)" 이 아니라 "*trigger* (multi-host 전환)" 가 ST-4 의 본질 진입 조건 — feedforward (진입 조건 미리 박음) > 시점 보류 (CLAUDE.md §2) |
| 대안 우월 4건 | **AU-1 trigger 기반 진입** (multi-host = primary trigger, MVP-6 = 상관 시점) / **AU-2 single-host 경량 대안** (ST-3 + ST-1 + `ssss` 로컬 분할 + PGP 봉인 / 또는 `age` — Vault 없이 ADR-010 목적 달성) / **AU-3 secret manager Provider Liquidity** (OpenBao/age = lock-in 0, HCP/Enterprise/KMS lock-in 회피) / **AU-4 single-host 영구 유지 = 정당 종착** (ST-4 영원히 미진입 적격) |
| Agent C 신규 6건 | NC-1 Operational Readiness 1인 정량 PASS 임계 / NC-2 Vault 장애 fallback 트리 구조 / NC-3 secret manager liquidity lock-in trigger / NC-4 ADR-010 §A sosf single-host fallback 재활용 / **NC-5 보류 무한 표류 차단 `R-ST4-DEFER-REVISIT` (의무 재평가)** / NC-6 single-host SPOF 수용 문서화 의무 |
| MVP-6 보류 형태 | (가) 전면 보류 (시점 동결) ⚠️ + (나) 순수 참조 유지 ⚠️ vs **(다) 참조 유지 + trigger 구조 명시 ⭐ 우월** (무한 표류 차단) |
| 진입 조건 | C-Cγ2-1~10 |

### 2.4 3 Agent 일치 영역 (사전 식별)

| 영역 | A | B | C | 일치 |
|------|----|----|----|----|
| **현 시점 실 진입 부적합 (DEFER/BLOCK)** | ✅ | ✅ | ✅ | **3/3 만장일치** |
| MVP-6 보류 (영구 폐기 아님 — 재검토 시점) | ✅ | ✅ | ✅ | 3/3 |
| **single-host 에서 Vault HSM 실효 무력화** (HSM 핵심 이점 = multi-host 격리) | ✅ | ✅ | ✅ | 3/3 |
| ADR-012 §원칙 12 (single-host SPOF 의도적 수용) 정합 — multi-host 전환이 ST-4 trigger | ✅ | ✅ | ✅ | 3/3 |
| Operational Readiness PASS (Layer E, Backlog #7) 선행 | ✅ | ✅ | ✅ | 3/3 |
| Hermes PMO 격상 (Layer F) 자동 연결 금지 | ✅ | ✅ | ✅ | 3/3 |
| ADR-010 §B 채택 유효 + §X 본문 변경 0건 (참조 유지) | ✅ | ✅ | ✅ | 3/3 |
| single-host canonical = ST-3 docker secret + ST-1 file perm (보호 목적 약화 0건) | ✅ | ✅ | ✅ | 3/3 |
| ST-1 ↔ ST-4 직교 (보류가 ST-1 진입 안 막음, γ-1 AU-4) | ✅ | ✅ | ✅ | 3/3 |
| ST-4 단독 대체 금지 (Defense in depth) | ✅ | ✅ | ✅ | 3/3 |
| Hermes ≠ root of trust (Vault root token/unseal 보유 금지, App Role short-lived) | ✅ | ✅ | ✅ | 3/3 |
| Vault 자체 = 신규 SPOF (ADR-010 §부정적 자인) | ✅ | ✅ | ✅ | 3/3 |
| 운영 비용 高 (Vault 인프라 / Enterprise·HCP 요구) | ✅ | ✅ | ✅ | 3/3 |
| 보류 확정도 T3 정책 결정 → 풀 3+1 (Reviewer-only 부적격) | ✅ | ✅ | ✅ | 3/3 |
| 수단 적격성 권고 한정 (구현 / §X 본문 변경 / 발효 0건) | ✅ | ✅ | ✅ | 3/3 |
| 외부 LLM 양 vendor BLOCK/DEFER = 입력 한정 (강제 채택 0건) | ✅ | ✅ | ✅ | 3/3 |

---

## 3. Phase 3 (Cross-Comparison) — 일치 / 부분 / 불일치 / 누락

### 3.1 일치 (Consensus, 3개 모두 동의) — 16 영역

§2.4 답습 — **16/16 일치 영역**. 본 합의의 핵심 권위 source. 특히 **3 Agent 가 *독립적으로* (i) single-host HSM 실효 무력화 + (ii) MVP-6 보류 + (iii) ST-3+ST-1 canonical 보호 목적 약화 0건을 동시 도출** — 보류 합의 권위 강화.

### 3.2 부분 일치 (Partial, 2개 동의 / 1개 확장) — 3 영역

| # | 영역 | A | B | C | 분석 |
|---|------|----|----|----|----|
| P-1 | 판정 라벨 | DEFER | BLOCK/DEFER + 보류확정 APPROVE WITH CONDITIONS | DEFER (form refinement) | **부분 — 셋 다 보류 수렴 / 라벨 강도 상이 → 통합 = BLOCK/DEFER + 보류확정 APPROVE WITH CONDITIONS** |
| P-2 | 보류 *형태* | MVP-6 보류 (재검토 시점) | MVP-6 재검토 (영구 폐기 아님) | **trigger 기반 조건부 진입 등록** (multi-host=primary trigger, R-ST4-DEFER-REVISIT 무한 표류 차단) | **부분 — A/B = 시점 기반 / C = trigger 기반 (feedforward 우월)** |
| P-3 | single-host 종착 | multi-host 전환 시 진입 (전환 전제) | multi-host 전환 시 진입 | **single-host 영구 유지 = 정당 종착** (ST-4 영원히 미진입 적격, AU-4) | **부분 — A/B = 전환 전제 / C = 영구 미진입도 적격** |

#### 3.2.1 P-1 분석 (판정 라벨)
**Reviewer 평가**: 3 Agent 모두 *보류* 수렴 — Agent A "DEFER" + Agent B "BLOCK/DEFER + 보류확정 APPROVE WITH CONDITIONS" + Agent C "DEFER". 라벨 강도 차이는 *형태* 차이일 뿐 *방향* 은 만장일치. **합의 도출 → 최종 판정 = BLOCK / DEFER — MVP-6 보류 (trigger 기반 조건부 진입 등록) APPROVE WITH CONDITIONS** (Agent B 의 가장 구체적 라벨 채택 + Agent C 형태 흡수).

#### 3.2.2 P-2 분석 (보류 형태 — Agent C trigger 기반)
**Reviewer 평가**: Agent C 의 "trigger 기반 조건부 진입 등록" 은 Agent A/B 의 "MVP-6 보류 (재검토 시점)" 와 *충돌하지 않는 정교화* — "시점 (MVP-6)" 은 외부 캘린더이고 "trigger (multi-host 전환)" 는 목적 인과 (HSM 이점 = multi-host 격리). CLAUDE.md §2 feedforward (진입 조건 미리 박음) + 무한 표류 차단 (R-ST4-DEFER-REVISIT). **합의 도출 → 보류 형태 = trigger 기반 (multi-host 전환 = primary trigger, MVP-6 = 상관 시점) + R-ST4-DEFER-REVISIT 의무 재평가 + 영구 폐기 아님 (ADR-010 §B 유효)**. 단 ADR-010 §X 본문 변경은 별도 합의 (본 합의 0건).

#### 3.2.3 P-3 분석 (single-host 영구 유지 종착)
**Reviewer 평가**: Agent C 의 "single-host 영구 유지 = 정당 종착 (ST-4 영원히 미진입 적격)" 은 ADR-012 §원칙 12 (SPOF 의도적 수용) 의 논리적 종착 — 1인 메타-템플릿이 영원히 single-host 일 수 있고, multi-host 는 규모 변화의 *결과* 이지 목표 아님. Agent A/B 의 "multi-host 전환 시 진입" 과 정합 (전환이 *발생하면* 진입, 안 하면 미진입). **합의 도출 → single-host 영구 유지 = 적격 종착 옵션 명시 (ST-4 영구 미진입 = 부적합 아님)**.

### 3.3 불일치 (Divergence, 3개 모두 다른 의견) — 0 영역

3 Agent 모두 보류 수렴 (3/3 만장일치 방향 + 3 부분 일치 형태). **불일치 0건**.

### 3.4 누락 (Gap, 특정 에이전트만 언급) — 9 영역

| # | 영역 | 출처 | 처리 |
|---|------|----|----|
| G-1 | 통합 대상 부재 (Hermes 컨테이너/Vault client 0줄) | A | 흡수 — §2.1 + C-Gγ2-1 |
| G-2 | PGP 운영자 2명 전제 1인 구조적 불충족 (ADR-010 §운영) | A | 흡수 — C-Gγ2-5 |
| G-3 | single-host HSM 3대 기능 (external root/auto-unseal/seal wrapping) 무력화 | A | 흡수 — §6.1 |
| G-4 | 안전 순이득 음수 (신규 SPOF + root custody 모호) | B | 흡수 — §6.1 |
| G-5 | 1인 환경 3-of-3 SSS 분산 효과 0 (share 동일 주체) | B | 흡수 — C-Gγ2-5 |
| G-6 | ADR-011 §2.1 4조건(본문) vs 5조건(합의 패턴) 정합성 지적 | B | 흡수 — §6.3 (Group β G-4 답습) |
| G-7 | AU-1~4 (trigger 재프레임 / single-host 경량 대안 ssss+age / secret manager liquidity / single-host 영구 유지) | C | 흡수 — §5 + C-Gγ2-2/3/9/10 |
| G-8 | NC-1~6 (Operational Readiness 1인 정량 / Vault fallback 트리 / secret manager liquidity / ssss fallback / DEFER-REVISIT / SPOF 문서화) | C | 흡수 — §7 Rollback Trigger + C-Gγ2-6/7/8 |
| G-9 | secret manager lock-in = liquidity 차원 (brief §5.2 "#4 영향 없음" 보정) | C (NC-3) | 흡수 — C-Gγ2-9 |

**누락 흡수 결론**: 9 누락 영역 모두 흡수 — 충돌 0건. A 기술 ROI·운영 정량 / B 안전 순이득·정합성 / C 대안·trigger·표류 차단 = 합의 풍부도 증대.

### 3.5 Phase 3 매트릭스 합산

| 분류 | 영역 수 | 처리 |
|----|----|----|
| 일치 (Consensus) | 16 | 그대로 채택 |
| 부분 일치 (Partial) | 3 | 통합 (§3.2.1~§3.2.3) |
| 불일치 (Divergence) | 0 | — |
| 누락 (Gap) | 9 | 흡수 (§3.4) |

**합산**: 28 영역 모두 합의 도달. **3/3 만장일치 보류 수렴 = BLOCK / DEFER — MVP-6 보류 APPROVE WITH CONDITIONS** 권위 강화.

---

## 4. Phase 4 (Consensus Resolution) — 최종 판단

### 4.1 최종 판정 = **BLOCK / DEFER — MVP-6 보류 (trigger 기반 조건부 진입 등록) APPROVE WITH CONDITIONS** (3/3 만장일치 보류)

| 영역 | 판정 |
|------|------|
| 종합 판정 | **BLOCK / DEFER — MVP-6 보류 APPROVE WITH CONDITIONS** (Agent A + B + C 3/3 보류 수렴) |
| 합의 단위 | Group γ-2 단독 (Vault HSM ST-4) — Backlog #3 T3 마지막 진입 단위 |
| 합의 형태 | 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 (보류 확정도 T3) |
| 보류 형태 | **trigger 기반 조건부 진입 등록** (multi-host 전환 = primary trigger, MVP-6 = 상관 시점) + 영구 폐기 아님 (ADR-010 §B 유효) + R-ST4-DEFER-REVISIT 의무 재평가 |
| 진입 부적합 사유 | single-host HSM 실효 무력화 + 통합 대상 부재 + 안전 순이득 음수 + Operational Readiness 미선행 (3/3) |
| 외부 LLM 결론 강제 채택 | ❌ 0건 (입력 한정 — 본 합의는 3 Agent 독립 분석에서 동일 결론 도출, 맹종 아님) |

### 4.2 본 합의 조건 (Conditions, 통합 12건) — C-Gγ2-1 ~ C-Gγ2-12

| # | 조건 | 출처 |
|---|------|----|
| **C-Gγ2-1** | **현 시점 Vault HSM 실 진입 = 부적합 (BLOCK).** 통합 대상 (Hermes 컨테이너/Vault client) 부재 + single-host HSM 실효 무력화 + 안전 순이득 음수. 실 진입 = multi-host 전환 + Operational Readiness PASS (Layer E) 선행 + ADR-010 §X 합의 + 사용자 명시 | A C-Aγ2-1 + B C-B-1/3 + C (3/3 BLOCKING) |
| **C-Gγ2-2** | **보류 형태 = trigger 기반 조건부 진입 등록** — multi-host 전환 = primary trigger (HSM 이점 = multi-host 격리, ADR-012 §원칙 12 SPOF 면책 해제 시점), MVP-6 = 상관 시점. 시점 동결 ❌ + 영구 폐기 ❌ (ADR-010 §B 유효). ADR-010 §X 본문 변경은 별도 합의 (본 합의 0건) | C AU-1/P-2 통합 (3/3 보류 + C 형태) |
| **C-Gγ2-3** | **single-host canonical secret source = ST-3 docker secret (`mode:0400`+read-only+non-root) + ST-1 file perm** (γ-1 발효) — 보호 목적 (ADR-008 P3 secret 평문 노출 차단) 약화 0건. **경량 B-N2 fallback 후보** = `ssss` 로컬 분할 + PGP 봉인 백업 / 또는 `age` (Vault 없이 ADR-010 목적 달성, AU-2/NC-4) | A C-Aγ2-4 + B C-B-2 + C AU-2 (3/3) |
| **C-Gγ2-4** | **ST-4 ↔ ST-1/ST-3 직교** (γ-1 AU-4) — ST-4 보류가 ST-1 진입 안 막음 (역도 성립). ST-4 = multi-host root secret source 보강 (단독 대체 금지, Defense in depth) | A C-Aγ2-4 + B C-B-2 + C AU-4 (3/3) |
| **C-Gγ2-5** | **ADR-010 §운영 인프라 (PGP 운영자 2명) = 1인 환경 구조적 미충족** + **1인 single-host 에서 3-of-3 SSS 분산 효과 0** (share 동일 주체). Operational Readiness 단계에서 1인 기준 운영 절차 (rotation/backup/restore/fallback/audit) 재정의 선행 (ADR-010 §B 본문 변경 0건 — 1인 보정은 별도 합의) | A C-Aγ2-5 + B C-B-5/E-1 + C NC-2 |
| **C-Gγ2-6** | **Operational Readiness PASS (Layer E, Backlog #7) = ST-4 진입 hard precondition.** 1인 기준 정량 PASS 임계 정의 (sample restore 분기 1회 / 회전 1회 실증 / Vault 장애 fallback < N시간) — enterprise HA 흉내 ❌ | B C-B-4 + C NC-1 + A §6 (3/3) |
| **C-Gγ2-7** | **Hermes ≠ root of trust 보존 (① HIGH blocking)** — ST-4 진입 시 Hermes 는 Vault root token/unseal 미보유 + App Role short-lived token + 최소 권한. secret fetch·3-of-3 결합 주체가 Hermes 자신이 되어 root 격상 금지 (외부 harness 검증, γ-1 답습) | A C-Aγ2-6 + B C-B-1 (3/3 BLOCKING) |
| **C-Gγ2-8** | **Hermes PMO 격상 (Layer F) 자동 연결 금지** — ST-4 ↔ PMO 격상 자동 연결 금지. PMO 격상 = 외부 LLM 2 또는 1+사람 리뷰 의무 (P2 v3 §11.1). 보류 확정이 PMO 격상 트리거하지 않음 | B C-B-6 + A + C (3/3 BLOCKING) |
| **C-Gγ2-9** | **secret manager Provider Liquidity (lock-in 회피, NC-3)** — Vault 인프라 형태 결정 시 OpenBao/age 동등 대체 보존 (HCP/Enterprise/KMS lock-in 주의). LLM Provider Liquidity 5-way 와 별개 차원 — brief §5.2 "#4 영향 없음" 보정 | C AU-3/NC-3 + B ④ |
| **C-Gγ2-10** | **single-host 영구 유지 = 적격 종착 옵션** (AU-4) — ST-4 영원히 미진입 = 부적합 아님 (ADR-012 §원칙 12 SPOF 의도적 수용). multi-host 전환은 규모 변화의 결과이지 목표 아님 + single-host SPOF 수용 = 명시 문서화 의무 (NC-6) | C AU-4/NC-6 |
| **C-Gγ2-11** | **보류 무한 표류 차단 `R-ST4-DEFER-REVISIT` (NC-5)** — multi-host 전환 또는 MVP-6 도달 시 *의무* 재평가 (ST-4 가 "MVP-6 → PMO 후 → multi-host 후" 로 무한 표류 방지). + Vault 장애 fallback 트리 구조 (NC-2) | C NC-5/NC-2 |
| **C-Gγ2-12** | **본 합의 = 수단 결정 적격성 권위 권고 + MVP-6 보류 확정 적격성 판정 + DRAFT 한정.** Vault HSM 구현 / ADR-010 §X 본문 변경·§B 재변경 / 보류 확정 *발효* / 수단 최종 결정 / Operational Readiness PASS / Hermes PMO 격상 / MVP-6 진입 / Multi-host 전환 / MVP-1 exit / actual run / CI workflow / Phase α defer-lockdown 변경 모두 0건. ⚠️ 문서 정합성: ADR-011 §2.1 본문 = (a)~(d) 4조건, "5조건" = +(e) 합의 APPROVE 패턴 (구분 명시, Group β G-4 답습) | A C-Aγ2-7 + B C-B-8/9 + C C-Cγ2-10 (3/3) |

**합의 조건 합산**: **12 조건 충족 시 = 보류 확정 적격** + 본 합의 = "보류 확정 적격성 판정 + 수단 적격성 권고" 한정. blocking = C-Gγ2-1 (현 진입 BLOCK) + C-Gγ2-7 (Hermes≠root) + C-Gγ2-8 (PMO 자동 연결 금지).

---

## 5. Final Consensus 6 결정 영역 — 최종 합의 권고

| # | 결정 | **최종 합의 옵션** | 사유 (3/3 만장일치 보류 + 부분 흡수) |
|---|------|----|----|
| 1 | ST-4 진입 시점 | **trigger 기반 — multi-host 전환 = primary trigger (MVP-6 = 상관 시점)** ⭐ + MVP-2 조기 = 과설계 BLOCK | P-2 통합 (AU-1) — HSM 이점 = multi-host 격리, ADR-012 §원칙 12 정합 |
| 2 | Vault 인프라 형태 | **결정 보류 + Provider Liquidity lock-in 회피 명시** (OpenBao/age 동등 대체 보존, HCP/Enterprise/KMS lock-in 주의) | AU-3/NC-3 흡수 (secret manager liquidity, 3/3 보류) |
| 3 | Vault client 통합 방식 | **multi-host 진입까지 결정 deferred + Hermes ≠ secret custody root 명시** (App Role short-lived, K8s Auth = single-host 비현실) | A + B C-B-1 + C AC-3 (Hermes≠root) |
| 4 | ADR-010 §X 본문 형태 | **참조 유지 + 진입 trigger 구조 명시 권고 (중간안)** — 순수 참조 유지(미정의 표류) vs 시점 동결 보다 우월 / 단 본 합의 §X 본문 변경 0건 | P-2 통합 (C AU-1/AC-4) — feedforward |
| 5 | 다른 ST 통합 정책 | **환경별 canonical source** (single-host = ST-3+ST-1 / multi-host = ST-4 root) — ST-4 단독 대체 금지, ST-1↔ST-4 직교 | 3 시점 비중첩 + γ-1 AU-4 (3/3) |
| 6 | Multi-host 전환 시점 | **single-host 영구 유지 = 적격 종착** (ST-4 영원히 미진입 정당) + multi-host 전환 시 ADR-012 Layer 3/5 의무 + ST-4 재평가 | P-3 통합 (AU-4) — SPOF 의도적 수용 종착 |

**합산**: 6 결정 영역 모두 합의 도달 — **3/3 만장일치 보류 + P-1/P-2/P-3 부분 통합 + G-1~G-9 누락 흡수**. 모든 권고 = *적격성 권고* 한정 (실 진입 = multi-host + Operational Readiness PASS + ADR-010 §X 합의 + 사용자 명시).

---

## 6. single-host SPOF + Operational Readiness / PMO 경계 + cross-reference

### 6.1 single-host SPOF (ADR-012 §원칙 12) vs Vault HSM 안전성 (핵심 보류 근거)

> **single-host SPOF 의도적 수용 (ADR-012 §원칙 12) 과 Vault HSM 도입 = 위협 모델 정합성 충돌.** single-host 에서 Vault·unseal 키·App Role token·SSS share 1 이 모두 동일 host → **host 침해 = Vault 침해 = SQLCipher 키 침해 (격리 효과 0)**. HSM 3대 기능 (external root key storage / automatic unseal / seal wrapping) 모두 동일 침해 경계로 무력화 (Agent A) → **안전 순이득 음수** (신규 SPOF + root custody 위계 모호 + 운영 부담, Agent B). **정합적 결론**: Vault HSM = multi-host 전환 시점 (SPOF 면책 해제 + Layer 3/5 의무 발동) 에 secret root source 격리가 비로소 의미 (3/3). single-host 에서 중요한 것은 HSM 이 아니라 ST-1 (file perm) + ST-3 (docker secret) + audit + backup/restore + rotation.

### 6.2 Operational Readiness (Layer E) / Hermes PMO 격상 (Layer F) 경계

| 경계 | 합의 |
|----|----|
| Operational Readiness PASS (Layer E) | ST-4 진입 hard precondition — rotation/backup/restore/Vault 장애 fallback/audit/비용 감당 1인 기준 검증 선행 (Backlog #7). 1인 정량 PASS 임계 정의 (C-Gγ2-6) |
| Hermes PMO 격상 (Layer F) | ST-4 ↔ PMO 격상 자동 연결 금지. Vault root custody → Hermes root 격상 위험 (① 약화). PMO 격상 = 외부 LLM 2 또는 1+사람 리뷰 (C-Gγ2-8) |

### 6.3 기타 cross-reference

| 영역 | 답습 |
|------|----|
| **ADR-010 §B / §X / §부정적** | Vault HSM + Shamir SSS 3-of-3 + 90일 회전 + dual-key + PGP 봉인 백업 채택 *유지* (재변경 0건). §X 진입 = 별도 풀 3+1. §부정적 "Vault = 신규 SPOF" 자인 = 보류 근거 |
| **ADR-012 §원칙 12** | single-host SPOF 면책 + multi-host 전환 시 Layer 3 (signed commit) / Layer 5 (external anchor) 의무 트리거 = ST-4 진입 정합 시점 |
| **ADR-011 §2.1 (a)~(d) 4조건 [+ (e) 합의 패턴]** | ST-4 진입 = (a) 동등 이상 보안 결과 비교표 (ST-3 ↔ ST-4) 충족을 multi-host 전제 하 실증 후 적격. ⚠️ 4조건(본문) vs 5조건(합의 패턴) 구분 명시 (C-Gγ2-12) |
| **ADR-011 §2.4 T3** | Vault HSM ADR-010 §X 진입 = T3 → 풀 3+1 + 외부 LLM 1+ + 사용자 명시. 보류 확정도 T3 |
| **γ-1 합의 AU-4** (ST-1↔ST-4 직교) | 보류가 ST-1 진입 봉인 0건 (C-Gγ2-4) |
| **Group C Evidence Ledger** | Vault audit log ↔ Evidence Ledger 연계 (1인 attribution 의미 재정의) |

---

## 7. Rollback Trigger 통합 매트릭스 (Agent C 신규 trigger 흡수)

### 7.1 Group γ-2 진입 Rollback Trigger (답습)

| Trigger | 발화 조건 | 발화 시 행동 |
|----|----|----|
| **ADR-011 §2.4** | T3 영역 (Vault HSM ADR-010 §X 진입) 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
| **ADR-010 §X** | Vault HSM 실 구현 진입 결정 | 풀 3+1 + Operational Readiness PASS 선행 |

### 7.2 신규 Rollback Trigger (Agent C NC 흡수 — 구조 한정, 발효 0건)

| Trigger | 영역 | 발화 조건 | 후속 합의 |
|----|----|----|----|
| **R-ST4-MULTIHOST** | ST-4 primary trigger | Multi-host 전환 결정 | ADR-012 §원칙 12 Layer 3/5 의무 발동 + ST-4 필요성 재평가 |
| **R-ST4-OPSREADY-CRITERIA** (NC-1) | Operational Readiness 1인 PASS 임계 | ST-4 진입 검토 | 1인 기준 정량 정의 (sample restore/회전/fallback) |
| **R-ST4-VAULT-FALLBACK** (NC-2) | Vault 장애 fallback | Vault inaccessible | PGP share 복원 / degraded / fail-closed 트리 |
| **R-ST4-SECRETMGR-LIQUIDITY** (NC-3) | secret manager lock-in | Vault 인프라 형태 결정 | OpenBao/age 동등 대체 보존 |
| **R-ST4-DEFER-REVISIT** (NC-5) | 보류 무한 표류 차단 | multi-host 전환 또는 MVP-6 도달 | *의무* 재평가 (표류 차단) |
| **R-ST4-PMO-BOUNDARY** | PMO 자동 연결 | ST-4 ↔ Hermes PMO 격상 연결 | 자동 연결 금지 — 별도 풀 3+1 + 외부 LLM 2+ |

### 7.3 후속 단계 Rollback Trigger (본 합의 영역 외)

| 영역 | 후속 Rollback Trigger | 분리 사유 |
|----|----|----|
| Vault HSM 실 구현 | ADR-010 §X + Operational Readiness PASS + Multi-host + 별도 풀 3+1 + 사용자 명시 | MVP-6 영역 |
| Operational Readiness PASS (Layer E) | Backlog #7 + MVP-6 | Layer E 영역 |
| Hermes PMO 격상 (Layer F) | MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 | Layer F 영역 |
| ADR-010 §X 1인 보정 정책 (PGP 2명 / 3-of-3 → 2-of-3) | 별도 합의 | ADR-010 영역 |

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | 본 합의 그대로 승인 → 파일화 + commit + push (γ-2 brief + 본 합의 별도 2 commit chain) | commit + push |
| (B) | 본 합의 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 합의 그대로 승인 → 파일화 + commit *까지만* (push 보류) | commit |
| (D) | 본 합의 승인 + push → **GP-3 C-3 / GP-5 C-2 condition row 갱신 합의** (해소 선언 — α+β+γ-1+γ-2 발효 답습, Backlog #3 T3 4 단위 완료) | GP entry 갱신 |
| (E) | 본 합의 승인 + push → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief** | Group I |
| (F) | 본 합의 보류 → 세션 종료 | — |

### 8.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 후보: "옵션 (A)로 진행 — 본 합의 그대로 승인하고 γ-2 brief + 합의 별도 2 commit chain commit + push."
- (D) 후보: "옵션 (D)로 진행 — GP-3 C-3 / GP-5 C-2 condition row 갱신 합의 (해소 선언)." ⭐ Backlog #3 T3 4 진입 단위 (α/β/γ-1/γ-2) 모두 발효 완료 → 두 condition 완전 해소 vehicle 충족.

---

## 9. 메타 검증

| 검증 영역 | 결과 |
|--------|----|
| Phase 1~5 완수 | ✅ Distribution + Independent Analysis (A/B/C 병렬 독립) + Cross-Comparison + Consensus Resolution + Report |
| 풀 3+1 의무 영역 (T3 보안 enforcement) | ✅ Agent A/B/C + Reviewer 4 역할 (보류 확정도 T3 → Reviewer-only 단축 부적격 답습) |
| Agent 독립성 (편향 방지) | ✅ A/B/C 상호 비참조 (각 출력에 "다른 Agent 미참조" 명시) |
| brief 결론 선취 회피 | ✅ brief §0.4 "결론 선취 0건" 답습 — 3 Agent 독립 분석에서 보류 동일 도출 (외부 LLM 맹종 아님) |
| 3/3 만장일치 보류 | ✅ BLOCK / DEFER — MVP-6 보류 APPROVE WITH CONDITIONS (불일치 0건) |
| 12 합의 조건 (C-Gγ2-1~12) | ✅ 등록 (blocking 3건) |
| 사용자 명시 금지 12건 (§0.3) | ✅ 모두 0건 (Vault HSM 구현 0 / ADR-010 §X 본문 변경 0 / 보류 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / MVP-6 진입 0 / Multi-host 전환 0 / MVP-1 exit 0 / actual run 0 / CI workflow 0 / Phase α defer-lockdown 변경 0 / 수단 최종 결정 0) |
| 합산 합의 조건 | 719 → 731 (28 합의 — 본 합의 C-Gγ2-1~C-Gγ2-12 신규 12 등록) — *commit 시 발효* |
| 실 변경 0건 | ✅ Vault / ADR-010 / 도구 본문 / CI workflow 변경 0건 (Agent A read-only 실행 — 기존 PoC 확인) |
| **Backlog #3 T3 4 진입 단위 완료** | ✅ α (`2026-05-14`) + β (`aa8a29a`) + γ-1 (`9b1f8cd`) + γ-2 (본 합의) — brief·합의 영역 모두 정비 |

---

## 10. 합의 요약 (한 단락)

Backlog #3 T3 영역 中 Group γ-2 (Vault HSM ST-4 — ADR-010 SQLCipher 키 관리 Vault HSM + Shamir SSS 채택의 *구현 진입*) 단독 풀 3+1 합의 (Agent A 구현 분석가 + Agent B 품질/안전성 검증가 + Agent C 대안 탐색가 병렬 독립 분석 + Reviewer 교차 비교·합의 도출) 결과 = **BLOCK / DEFER — MVP-6 보류 (trigger 기반 조건부 진입 등록) APPROVE WITH CONDITIONS (3/3 만장일치 보류 수렴)** — Backlog #3 T3 영역의 *마지막 진입 단위*. 진입 부적합 사유 (3/3) = (i) single-host 에서 Vault HSM 실효 무력화 (external root key storage / automatic unseal / seal wrapping = 동일 침해 경계로 무력, HSM 핵심 이점 = multi-host 격리) + (ii) 통합 대상 부재 (Hermes 컨테이너/Vault client 코드 0줄, Agent A 실측) + (iii) 안전 순이득 음수 (신규 SPOF + Hermes root custody 위계 모호, Agent B) + (iv) ADR-010 §운영 PGP 운영자 2명 전제가 1인 환경 구조적 불충족 + 1인 single-host 3-of-3 SSS 분산 효과 0 + (v) Operational Readiness PASS (Layer E, Backlog #7) 미선행. single-host SPOF 의도적 수용 (ADR-012 §원칙 12) 과 Vault HSM 도입 = 위협 모델 정합성 충돌 → multi-host 전환 시점 (SPOF 면책 해제 + Layer 3/5 의무 발동) 이 ST-4 의 본질 trigger. 보류 형태 = Agent C 의 **trigger 기반 조건부 진입 등록** (multi-host 전환 = primary trigger, MVP-6 = 상관 시점, 시점 동결 ❌ + 영구 폐기 ❌ + R-ST4-DEFER-REVISIT 의무 재평가로 무한 표류 차단) — single-host 영구 유지 = 적격 종착 옵션 (ST-4 영원히 미진입 정당). single-host canonical secret source = ST-3 docker secret + ST-1 file perm (γ-1 발효) 로 보호 목적 (ADR-008 P3) 약화 0건 + 경량 B-N2 fallback 후보 (ssss 로컬 분할 + PGP / age, Vault 없이 ADR-010 목적 달성) + secret manager Provider Liquidity lock-in 회피 (OpenBao/age 동등 대체 보존). ST-1 ↔ ST-4 직교 (γ-1 AU-4) — ST-4 보류가 ST-1 진입 안 막음. 12 합의 조건 (C-Gγ2-1~C-Gγ2-12, blocking 3: 현 진입 BLOCK / Hermes≠root / PMO 자동 연결 금지). 외부 LLM 양 vendor (Gemini + GPT) BLOCK/DEFER 수렴 = 입력 한정 (강제 채택 0건 — 본 합의는 3 Agent 독립 분석에서 동일 결론 도출, 맹종 아님). 본 합의 = 수단 결정 적격성 권위 권고 + MVP-6 보류 확정 적격성 판정 한정 — Vault HSM 구현 / ADR-010 §X 본문 변경·§B 재변경 / 보류 확정 발효 / 수단 최종 결정 / Operational Readiness PASS / Hermes PMO 격상 / MVP-6 진입 / Multi-host 전환 / MVP-1 exit / actual run / CI workflow / Phase α defer-lockdown 변경 / 외부 LLM 강제 채택 모두 0건이며, 모든 *결정* (보류 확정 발효 포함) 은 별도 풀 3+1 합의 (사용자 명시 승인 후). 합산 합의 조건 719 → 731 (28 합의 — commit 시 발효). **Backlog #3 T3 4 진입 단위 (α/β/γ-1/γ-2) brief·합의 영역 모두 정비 완료.**

---

## 부록 A — 다음 단계 옵션 (사용자 결정 영역)

§8 답습. 본 합의 = Phase 5 (Report) 완료 + 사용자 명시 승인 *전* 상태 (commit 0건). staged cycle (brief → 승인 → 합의 → commit → push) 답습 — commit / push = 사용자 명시 승인 후 별도 단계. 본 합의 발효 시 Backlog #3 T3 4 진입 단위 완료 → GP-3 C-3 / GP-5 C-2 해소 선언 (condition row 갱신 합의) 적격.

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
Vault HSM 구현 (실 Vault 클라이언트 / 실 HSM / App Role / Kubernetes Auth / Shamir SSS 분할 / Multi-host 인프라) / ADR-010 §X 진입 섹션 본문 변경 / ADR-010 채택 (§B) 재변경 / "MVP-6 보류 확정" 결정 발효 (보류 형태·trigger 등록 포함) / 수단 최종 결정 / Vault 인프라 형태 고정 / Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언 / MVP-6 진입 / Multi-host 전환 결정 / MVP-1 exit 발효 / MVP-2 자동 진입 / Backlog #7·Backlog #1 ST-2·Group I 자동 진입 / §C-5·§C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경 / Layer D 본문 변경 / follow-up brief·Group α·β·γ-1 합의·γ-2 brief·prep brief 계보 본문 변경 / actual run / CI workflow 변경 / Production docker-compose 변경 / `requirements*.txt` 변경 / Phase α defer-lockdown 변경 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / ADR 본문 자동 갱신 (ADR-008/010/011/012) / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
