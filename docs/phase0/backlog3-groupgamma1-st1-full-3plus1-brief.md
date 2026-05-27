# Backlog #3 Group γ-1 (C-5b ST-1 — Hermes upstream chmod 600) 단독 풀 3+1 합의 *준비* Brief (DRAFT)

> **본 brief = Backlog #3 (T3 영역) 中 *Group γ-1 (C-5b ST-1 — Hermes upstream Dockerfile entrypoint chmod 600 강제) 단독* 풀 3+1 합의 *진입 전* 정비를 위한 *준비안* (DRAFT)** — follow-up brief (`backlog3-t3-zone-followup-brief.md` `79c8ad6` §3.2 / §6.1 2순위) + Group β 합의 발효 (`aa8a29a`) 이후 잔여 진입 단위 中 **Group γ-1 영역만 추출 + 외부 LLM 응답 Q13/Q15/Q17 흡수 + Agent A/B/C 분배 + Reviewer 검토 의무 영역 정비** 한정. GPT γ-1/γ-2 분리 권고 흡수 (Group γ = γ-1 + γ-2 분리 진입 단위).
>
> 본 brief 의 어떤 §도 그 자체로 (i) **내부 Agent A/B/C + Reviewer 풀 3+1 합의 보고서 *작성* / commit / push**, (ii) **Group γ-1 실제 진입** (T3 영역), (iii) **Hermes upstream Dockerfile *본문* 변경** (entrypoint stat 추가 / chmod 강제 / image 빌드 / `~/.hermes/auth.json` perm 검증 코드), (iv) **Hermes upstream PR 발송 / fork+downstream patch 적용 / downstream wrapper·entrypoint preflight·CI container test *실 구현***, (v) **Hermes PMO 격상 (Layer F) 선언**, (vi) **Operational Readiness PASS (Layer E) 선언**, (vii) Group γ-2 (Vault HSM ST-4) / Group β / Backlog #1 ST-2 sidecar 자동 진입, (viii) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (ix) Layer B (`f40423f`) ST-3 docker secret 본문 채택 변경, (x) Layer D 합의 보고서 (`210c98f`) 본문 변경, (xi) follow-up brief / Group β 합의 / prep brief 계보 (`ad9a02d`/`2a9d02d`/`db0e3ac`) 본문 변경, (xii) 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정), (xiii) 외부 LLM 추가 자동 호출 / 재의뢰, (xiv) 실 API key / provider SDK / 외부 API 호출 / 실 secret material 처리, (xv) ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012), (xvi) MVP-1 exit 발효 / MVP-2 자동 진입, (xvii) 도구 본문 (`tools/*.py`) / CI workflow 변경 / actual run / Production `docker-compose.yml` / `requirements*.txt` 변경, (xviii) **Phase α defer-lockdown 변경**, (xix) 5 영구 핵심 제약 (특히 Hermes ≠ root of trust) / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (follow-up brief 옵션 (D) 답습 — Group γ-1 풀 3+1 진입 brief)
**상태**: DRAFT (사용자 명시 승인 *전*, 합의·commit·push 0건)
**관계**: follow-up brief (`79c8ad6`) §3.2 / §6.1 2순위 + Group β 합의 (`aa8a29a`) 후속 — 본문 변경 0건 + Group γ-1 단독 합의 진입 *직전* 정비
**상위 권위**:
- follow-up brief = `docs/phase0/backlog3-t3-zone-followup-brief.md` (`79c8ad6`, §3.2 Group γ-1 정비 + §5 풀 3+1 의무 + §6.1 2순위 + §6.2 그룹화)
- Group β 합의 = `docs/review/3plus1-consensus-2026-05-20-backlog3-groupbeta-catalog-policy.md` (`aa8a29a`, 잔여 진입 단위 분리 답습)
- Group α 합의 = `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (3/3 만장일치 형식 답습 + §6.1 Group γ-2 cross-reference)
- 외부 LLM 응답 = `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gemini.md` (Q13/Q15/Q17) + `...-gpt.md` (Q13/Q15/Q17) — 양 vendor 종합 (C) PARTIAL (γ-1 = downstream preflight 진입 가능 수렴)
- prep brief 계보 = v1 `ad9a02d` (§3.4 (4) C-5b ST-1 정의) / v2 `2a9d02d` / Group α brief `db0e3ac`
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (entrypoint stat) + §2.6.2 R2-1 (docker secret) + `~/.hermes/auth.json` (line 128) / ADR-012 §원칙 9 (Hermes ≠ root of trust) / ADR-011 §2.4 T3 영역
- 5 영구 핵심 제약 (특히 #1 Hermes ≠ root of trust) + Provider Liquidity 5-way

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "옵션 (D)로 진행 — Group γ-1 풀 3+1 진입 brief"

선행 답습: follow-up brief §8 옵션 (D) = "Group γ-1 (C-5b ST-1 Hermes upstream chmod) 풀 3+1 합의 진입 brief (downstream preflight)". T3 영역 = 보안 enforcement → CLAUDE.md §3 풀 3+1 의무 영역 (Reviewer-only 단축 부적격, §5 답습).

### 0.2 본 brief 가 *하는* 것

1. Group γ-1 (C-5b ST-1) 범위 + 책무 정의 (§1) — prep brief §3.4 답습 + Group γ-2 / β / Backlog #1 ST-2 분리 명시
2. C-5b ST-1 6 결정 영역 통합 검토 (§2) — 외부 LLM Q13 6 결정 영역 답습
3. ST-1 ↔ ST-2 ↔ ST-3 ↔ ST-4 *책무 분담* 매트릭스 (§3) — 외부 LLM Q15 답습 (Defense in depth 역할 분담)
4. **Hermes ≠ root of trust 보존 + Hermes upstream 변경 경계 vs Hermes PMO 격상 경계** (§4) — 외부 LLM Q17 답습
5. 합의 *단위* + 합의 *형태* 권고 (§5) — Group γ-1 *단독* + 풀 3+1 의무 (Reviewer-only 부적격)
6. 풀 3+1 Agent A / B / C 관점 분배 + Reviewer 검토 의무 영역 (§6)
7. 외부 LLM 양 vendor 수렴 / 차이 영역 합산 (§7) — γ-1 영역만 추출 (입력 한정)
8. Rollback Trigger 통합 매트릭스 — Group γ-1 한정 (§8)
9. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

- ❌ **풀 3+1 합의 보고서 작성 / commit / push** (본 brief = untracked DRAFT 한정)
- ❌ **Hermes upstream Dockerfile *본문* 변경** (entrypoint stat / chmod 강제 / image 빌드 / perm 검증 코드)
- ❌ **Hermes upstream PR 발송 / fork+downstream patch 적용 / downstream wrapper·entrypoint preflight·CI container test 실 구현**
- ❌ **Hermes PMO 격상 (Layer F) / Operational Readiness PASS (Layer E) 선언**
- ❌ **수단 *최종 결정* / 위반 시 동작 fail-closed *고정* / chmod 600 강제 형태 *고정*** (옵션 *적격성 권고* 한정)
- ❌ **Group γ-2 (Vault HSM ST-4) / Group β / Backlog #1 ST-2 sidecar 자동 진입**
- ❌ **§C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경**
- ❌ **MVP-1 exit 발효 / MVP-2 자동 진입 / actual run / CI workflow 변경**
- ❌ **Phase α defer-lockdown 변경** (별개 트랙 — 충돌 0건)
- ❌ **외부 LLM 응답 결론 강제 채택 / 추가 자동 호출**
- ❌ ADR 본문 자동 갱신 / 5 영구 핵심 제약 (특히 Hermes ≠ root of trust) 약화
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계 — staged cycle)

### 0.4 본 brief 의 권위 한계

본 brief = **Group γ-1 단독 풀 3+1 합의 *진입 전 정비* DRAFT 한정**. 본 brief 가 발생시키는 *유일한* 효과 = **Group γ-1 합의 진입 정비 답습 한정** (Layer 0.5 가이드). 모든 *결정* 은 *별도 풀 3+1 합의* (사용자 명시 승인 후).

---

## 1. Group γ-1 (C-5b ST-1) 범위 + 책무 정의

### 1.1 정의 (prep brief §3.4 답습)

| 영역 | 정의 |
|----|----|
| 정의 | Hermes upstream Dockerfile entrypoint 시점에 `~/.hermes/auth.json` (또는 동등 credential) 의 `stat` 검증 (chmod 600 강제) — 644 등 위반 시 컨테이너 정지 |
| 현 상태 | C-5b (ST-1) = Deferred (`78483c5` 답습) — Backlog #3 T3 영역 = 본 brief 영역 |
| 책무 영역 | secret source / Hermes upstream (file system perm) |
| T3 진입 속성 | Hermes upstream Dockerfile *본문* 변경 ✅ HIGH / **Hermes ≠ root of trust 검토 의무 ✅ HIGH** / Hermes upstream PR 의무 ⚠️ HIGH / sidecar (ST-2) 와 책무 분담 결정 의무 ⚠️ MEDIUM |
| ADR 권위 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (entrypoint stat) + `~/.hermes/auth.json` (line 128 credential 저장 경로) |

### 1.2 ST 군 (secret hygiene) 답습 — γ-1 위치

| ST | 영역 | 현 상태 | 본 brief 와의 관계 |
|----|----|----|----|
| ST-1 | Hermes upstream entrypoint stat chmod 600 | Deferred — Backlog #3 T3 | ✅ **본 brief 영역 (Group γ-1)** |
| ST-2 | inotify sidecar (runtime drift detection) | Backlog #1 영역 | 책무 분담 결정 의무 (§3) |
| ST-3 | docker secret (현 주 secret injection) | Layer B 본문 채택 (`f40423f`) | 책무 분담 결정 의무 (§3) — 본문 변경 0건 |
| ST-4 | Vault HSM (multi-host root secret source) | Group γ-2 (MVP-6 보류 권고) | 책무 분담 + cross-reference (§3 + §4) |
| ST-5 | Defense in depth 통합 | MVP-2 이후 영역 | 별도 영역 |

### 1.3 잔여 Backlog #3 T3 진입 단위 中 γ-1 위치 (follow-up brief §1.1)

| 진입 단위 | status |
|----|----|
| Group α (AR-3 + PC-4 T3 sub) | ✅ 풀 3+1 발효 (`2026-05-14`) |
| Group β (T-5 β + Tier-2/3 catalog 일반) | ✅ 풀 3+1 발효 (`2026-05-20`, `aa8a29a`) |
| **Group γ-1 (C-5b ST-1)** | ⏳ **본 brief 진입 정비 (2순위)** |
| Group γ-2 (Vault HSM ST-4) | ⏳ 미진입 (양 vendor BLOCK/DEFER to MVP-6 — 3순위) |

---

## 2. C-5b ST-1 6 결정 영역 통합 검토 (외부 LLM Q13 답습)

| # | 결정 영역 | 옵션 후보 | T3 진입 속성 / 외부 LLM 입력 (§7 답습) |
|---|----|----|----|
| 1 | **ST-1 진입 시점** | (a) MVP-1.5 downstream preflight 형태 / (b) MVP-6 Operational Readiness / (c) Hermes PMO 격상 후 | GPT = downstream 검증은 PMO 격상 *전* 가능 / Gemini = upstream 직접 수정은 PMO 동시·이후 |
| 2 | **Hermes upstream PR 절차** | (a) Hermes upstream 직접 PR / (b) fork + downstream patch / (c) **downstream wrapper / entrypoint preflight / CI container test 우선** | 양 vendor = downstream 검증 우선 + upstream PR = downstream evidence 확보 *후* 최소 패치 |
| 3 | **chmod 강제 형태** | (a) entrypoint `stat` 검증 / (b) `chmod 600` 강제 적용 / (c) 검증 + 위반 보고만 | Gemini = entrypoint chmod 600 검증 로직 / GPT = 어떤 파일이 어떤 permission이어야 하는지 명시 메시지 |
| 4 | **위반 시 동작** | (a) 컨테이너 정지 (fail-closed) / (b) warning / (c) **dev=warn / CI·production-like=fail-closed 분리** | 양 vendor = 환경별 분리 (dev warning / CI fail-closed) |
| 5 | **ST-2 / ST-3 와 통합** | (a) ST-1 단독 / (b) ST-1+ST-3 결합 / (c) **Defense in depth 역할 분담** (§3) | GPT Q15 = ST-3 주 injection / ST-1 permission preflight guard / ST-2 runtime drift |
| 6 | **ST-4 와 책무 분담** | (a) ST-1 = file system perm / ST-4 = HSM secret source 분리 / (b) ST-4 단독 대체 | GPT Q15 = ST-4 단독 대체 부적절 + 환경별 canonical secret source 명시 |

> 본 §2 = 6 결정 영역 *옵션 후보 + 입력 정리* 한정. *결정* 0건 — 풀 3+1 시 Agent A/B/C 평가 대상.

---

## 3. ST-1 ↔ ST-2 ↔ ST-3 ↔ ST-4 책무 분담 매트릭스 (외부 LLM Q15 답습)

### 3.1 Defense in depth vs 단일 source-of-truth 역할 분담 (GPT Q15 입력)

| ST | 역할 (입력 한정) | 환경 |
|----|----|----|
| **ST-3 docker secret** | 현 주 secret injection 방식 | 전 환경 (Layer B 본문 채택) |
| **ST-1 chmod/stat check (본 brief)** | 파일 permission preflight guard | dev=warn / CI=fail-closed |
| **ST-2 inotify sidecar** | runtime drift detection | Backlog #1 영역 |
| **ST-4 Vault HSM** | multi-host / production-grade root secret source | Group γ-2 (MVP-6) |

### 3.2 책무 분담 결정 의무 (위험 답습 — prep brief §5.3.1)

| # | 책무 분담 위험 | 강도 |
|---|----|----|
| 1 | ST-1 (file system perm) + ST-4 (HSM secret source) **책무 중첩** | ⚠️ HIGH |
| 2 | ST-2 inotify sidecar (Backlog #1) 와 책무 분담 | ⚠️ MEDIUM |
| 3 | ST-3 docker secret (Layer B 본문 채택) 와 책무 분담 | ⚠️ MEDIUM |

> **합의 도출 의무 (풀 3+1)**: ST-1 단독으로 모든 것을 대체하지 않음 + ST-4 단독으로 ST-1 대체하지 않음 + **환경별 canonical secret source 명시** (GPT Q15). Defense in depth (ST-1/2/3 우선) > 단일 source (ST-4 후순위) — Gemini Q15.

---

## 4. Hermes ≠ root of trust 보존 + upstream 변경 경계 vs Hermes PMO 격상 경계 (외부 LLM Q17 답습)

### 4.1 핵심 안전 쟁점 (5 영구 핵심 제약 #1)

> **Hermes upstream 변경 = root of trust 침범 위험.** 특히 Hermes 가 "자기 자신의 secret 안전성을 판단하는 주체" 가 되면 **Hermes ≠ root of trust 원칙이 약화** (GPT Q17). → "Hermes 가 자기 자신을 검증하니 안전하다" 가 되면 안 됨 (GPT Q13). **외부 harness 가 Hermes container behavior 를 검증** 하는 형태가 보존책.

### 4.2 upstream 변경 경계 vs PMO 격상 경계 (입력 한정)

| 항목 | Gemini (입력) | GPT (입력) |
|----|----|----|
| ST-1 chmod preflight 진입 시점 | PMO 격상 *동시 또는 이후* (upstream = 시스템 근간) | **ST-1 같은 최소 permission preflight = PMO 격상 *전*에도 가능** |
| upstream 변경 검증 의무 | root of trust 침범 위험 방지 → 외부 LLM 2인 이상 교차 검증 필수 | upstream 변경 *전* downstream wrapper 로 evidence 확보 + 외부 harness 검증 |
| PMO 격상 연결 | upstream 변경 = PMO 격상 논의와 병행 | **PMO 격상과 *자동 연결 금지*** |

### 4.3 5 영구 핵심 제약 영향 (prep brief §5.3.2 답습)

| 제약 | 영향 | 보존책 (입력) |
|----|----|----|
| **Hermes ≠ root of trust** | ✅ **HIGH** | downstream wrapper preflight + 외부 harness 검증 + "Hermes 자기 검증으로 안전" 금지 + image build ↔ runtime check 분리 + rollback 가능 |
| 수단-목적 분리 | ⚠️ HIGH | ST-1 = 수단, 안전 결과 (secret 평문 보호) = 목적 (수단 변경 시 목적 보존 검증) |
| 메타포 강제 금지 | ❌ 영향 없음 | — |
| 단일 source-of-truth | ⚠️ MEDIUM | 환경별 canonical secret source 명시 (ST-1~ST-4 역할 분담) |
| Provider Liquidity 5-way | ❌ 영향 없음 | secret source 영역 (vendor 의존 0건) |

---

## 5. 합의 단위 + 합의 형태 권고

### 5.1 합의 단위 = Group γ-1 *단독*

GPT γ-1/γ-2 분리 권고 흡수 (follow-up brief §1.1) — ST-1 = 비교적 작은 file permission guard / ST-4 = 인프라·운영·비용·PMO 경계가 모두 걸린 큰 결정 → 별도 합의 단위. **Group γ-1 단독 진입** (γ-2 = 별도 합의, 양 vendor MVP-6 보류 권고).

### 5.2 합의 형태 = 풀 3+1 *의무* (Reviewer-only 단축 *부적격*)

| 트리거 | γ-1 발화 |
|----|----|
| #2 T3 영역 자동 진입 | ✅ **HIGH (BLOCKING)** — ST-1 = Hermes upstream 본문 변경 = T3 영역 |
| #5 5 영구 핵심 제약 약화 | ✅ **HIGH** — Hermes ≠ root of trust (upstream 변경 = root of trust 영역 침범 위험) |
| #7 외부 LLM cross-vendor blind 없는 T3 결정 | ✅ HIGH — 응답 2건 (Gemini + GPT) 회수 完 → 풀 3+1 *입력* 답습 |

**합산**: 트리거 #2 (BLOCKING) + #5 (HIGH) → **풀 3+1 (Agent A/B/C + Reviewer) + 외부 LLM 1+ (입력 답습) + 사용자 명시 의무 확정. Reviewer-only 단축 부적격.** (CLAUDE.md §3 보안 enforcement 영역 답습.)

---

## 6. 풀 3+1 Agent A / B / C 관점 분배 + Reviewer 검토 의무 영역

| Agent | 관점 | 분석 영역 (γ-1) |
|----|----|----|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | entrypoint stat / chmod 600 검증 기술 구현 + downstream wrapper vs upstream PR 기술 비교 + dev/CI 환경 분기 구현 + image build ↔ runtime check 분리 + 컨테이너 정지 (fail-closed) 동작 + 기술 한계 (read-only fs / non-root user / volume mount perm) |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | **Hermes ≠ root of trust 보존** (자기 검증 위험) + 5 영구 핵심 제약 영향 + 엣지케이스 (644 위반 / symlink / volume perm override / rollback) + ST-1~ST-4 책무 중첩 안전성 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 정합 + PMO 격상 경계 |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | downstream wrapper vs Dockerfile layer 추가 vs upstream PR 트레이드오프 (Gemini 대안 답습) + ST-1~ST-4 역할 분담 대안 + 환경별 canonical secret source 형태 + 신규 영역 발굴 (예: rollback 절차 / evidence 형태 / 외부 harness 검증 구조) |
| Reviewer | "최선의 합의는?" | 3 출력 교차 비교 + 일치/부분/불일치/누락 + 6 결정 영역 최종 합의 권고 + Hermes ≠ root of trust 보존 검증 |

---

## 7. 외부 LLM 양 vendor 수렴 / 차이 영역 (γ-1 추출, 입력 한정)

### 7.1 수렴 영역

| 영역 | Gemini | GPT | 수렴 |
|----|----|----|----|
| 종합 (γ-1) | ST-1 = entrypoint chmod 600 검증 (실패 시 중지) | ST-1 = downstream wrapper/preflight/CI test 후 upstream | ✅ **downstream 검증 우선 진입 가능** |
| Hermes ≠ root of trust | 실행 환경 스스로 권한 무결성 검증 타당 | Hermes 자기 검증 = root of trust 약화 / 외부 harness 검증 | ✅ 보존 의무 (자기 검증 ≠ 안전 근거) |
| 위반 시 동작 | 실패 시 즉시 중지 | dev=warn / CI=fail-closed 분리 | ✅ 환경별 분리 (GPT 우월 — dev friction 회피) |
| upstream 변경 부담 | Dockerfile layer 추가 대안 (1인 관리 부담↓) | downstream wrapper 우선 + upstream PR = evidence 후 | ✅ upstream 직접 수정 최소화 |
| ST-1~ST-4 책무 | Defense in depth (ST-1/2/3 우선) > ST-4 후순위 | ST-3 주 injection / ST-1 preflight / ST-4 multi-host | ✅ 역할 분담 (단독 대체 금지) |

### 7.2 차이 영역 (1건)

| 영역 | Gemini | GPT | 본 brief 정비 (입력 한정) |
|----|----|----|----|
| ST-1 진입 시점 ↔ PMO 격상 경계 (Q17) | PMO 격상 *동시·이후* + 외부 LLM 2인 교차 검증 | **ST-1 최소 preflight = PMO 격상 *전* 가능** (자동 연결 금지) | 풀 3+1 평가 대상 — downstream preflight (PMO 전) vs upstream PR (evidence 후) 분리 정비 |

> 외부 LLM 응답 = *입력 한정* (강제 채택 0건). 차이 1건 (Q17) = 풀 3+1 Agent A/B/C 독립 평가 대상.

---

## 8. Rollback Trigger 통합 매트릭스 (Group γ-1 한정)

| Trigger | 발화 조건 | 발화 시 행동 |
|----|----|----|
| **ADR-011 §2.4** | T3 영역 (Hermes upstream 변경) 진입 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
| **C-5b ST-1** | Hermes upstream Dockerfile *본문* 변경 결정 | 풀 3+1 + **Hermes ≠ root of trust 검토** |
| **R-ST1-UPSTREAM-PR** (신규 후보) | Hermes upstream PR 발송 결정 | downstream evidence 확보 후 + 최소 패치 + 별도 합의 |
| **R-ST1-PMO-BOUNDARY** (신규 후보) | ST-1 ↔ Hermes PMO 격상 연결 | PMO 격상과 자동 연결 금지 — 별도 풀 3+1 + 외부 LLM 2+ (Gemini Q17) |

### 8.1 후속 단계 Rollback Trigger (본 brief 영역 외)

| 영역 | 후속 Rollback Trigger | 분리 사유 |
|----|----|----|
| 실 Hermes upstream Dockerfile 본문 변경 | downstream evidence 확보 후 + 별도 풀 3+1 + 사용자 명시 | Hermes upstream 영역 |
| downstream wrapper / preflight / CI container test 실 구현 | Backlog #6 Runtime + CI-hook 연결 | Backlog #6 영역 |
| ST-4 (Vault HSM) 책무 분담 결정 | Group γ-2 풀 3+1 (MVP-6 보류 권고) | Group γ-2 영역 |
| ST-2 (inotify sidecar) 책무 분담 | Backlog #1 영역 | Backlog #1 영역 |

---

## 9. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|----|----|----|
| **(A)** | 본 brief 그대로 승인 → **Group γ-1 풀 3+1 합의 진입** (Agent A/B/C + Reviewer, 외부 LLM 응답 입력 답습) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 brief 승인 → commit (`docs/phase0/backlog3-groupgamma1-st1-full-3plus1-brief.md`) *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (D) | 본 brief 보류 → **Group γ-2 (Vault HSM ST-4 MVP-6 보류 확정) 풀 3+1 진입 brief** (3순위) | 양 vendor BLOCK/DEFER 답습 |
| (E) | 본 brief 보류 → **GP-3 C-3 / GP-5 C-2 condition row 갱신 합의** (해소 선언, α+β 발효 답습) | GP entry 갱신 |
| (F) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 합의 / commit / push = 사용자 명시 승인 후 별도 단계. T3 영역 합의 = **풀 3+1 의무** (§5).

---

## 10. 한 단락 요약

Backlog #3 T3 영역 中 Group γ-1 (C-5b ST-1 — Hermes upstream Dockerfile entrypoint `~/.hermes/auth.json` chmod 600 강제) 단독 풀 3+1 합의 *진입 전 정비* DRAFT. Group α (`2026-05-14`) + Group β (`2026-05-20` `aa8a29a`) 풀 3+1 발효 이후 잔여 진입 단위 中 2순위 (GPT γ-1/γ-2 분리 권고 흡수 — γ-2 Vault HSM 은 3순위, 양 vendor MVP-6 보류 권고). 6 결정 영역 = ST-1 진입 시점 / Hermes upstream PR 절차 / chmod 강제 형태 / 위반 시 동작 / ST-2·ST-3 통합 / ST-4 책무 분담. 외부 LLM 응답 2건 (Gemini + GPT, 2026-05-13) 은 γ-1 에 대해 **downstream wrapper / entrypoint preflight / CI container test 형태 진입 가능** 으로 수렴 (Hermes upstream 직접 수정 최소화 + Hermes ≠ root of trust 보존 = "Hermes 자기 검증으로 안전" 금지 + 외부 harness 가 container behavior 검증 + dev=warn / CI=fail-closed 분리). 차이 1건 = ST-1 ↔ Hermes PMO 격상 경계 (Gemini PMO 동시·이후 + 외부 LLM 2인 교차 / GPT ST-1 최소 preflight = PMO 전 가능 + 자동 연결 금지) → 풀 3+1 평가 대상. 핵심 안전 쟁점 = **Hermes upstream 변경 = root of trust 침범 위험** (5 영구 핵심 제약 #1 HIGH) → downstream evidence 확보 + image build↔runtime check 분리 + rollback 가능 + PMO 격상 자동 연결 금지가 보존책. ST-1~ST-4 = 환경별 canonical secret source 역할 분담 (ST-3 주 injection / ST-1 permission preflight / ST-2 runtime drift / ST-4 multi-host) — 단독 대체 금지. T3 영역 = 보안 enforcement → **풀 3+1 (Agent A/B/C + Reviewer) 의무, Reviewer-only 단축 부적격** (트리거 #2 BLOCKING + #5 Hermes ≠ root of trust HIGH). 본 brief = 진입 정비 DRAFT 한정 — 합의 보고서 작성 / commit / push / Hermes upstream Dockerfile 본문 변경 / upstream PR 발송 / downstream wrapper 실 구현 / 수단 최종 결정 / fail-closed 고정 / Hermes PMO 격상 / Operational Readiness PASS / MVP-1 exit / actual run / CI workflow 변경 / Phase α defer-lockdown 변경 / 외부 LLM 강제 채택 모두 0건이며, 모든 *결정* 은 별도 풀 3+1 합의 (사용자 명시 승인 후).

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|----|----|
| `backlog3-t3-zone-followup-brief.md` (`79c8ad6`) | §3.2 Group γ-1 정비 + §5 풀 3+1 의무 + §6.1 2순위 + §6.2 그룹화 |
| `3plus1-consensus-2026-05-20-backlog3-groupbeta-catalog-policy.md` (`aa8a29a`) | 잔여 진입 단위 분리 + 풀 3+1 형식 답습 |
| `3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` | Group α 3/3 만장일치 형식 + §6.1 Group γ-2 cross-reference |
| `2026-05-13-backlog3-t3-zone-review-response-gemini.md` | Q13 / Q15 / Q17 (입력 한정) |
| `2026-05-13-backlog3-t3-zone-review-response-gpt.md` | Q13 / Q15 / Q17 (입력 한정) |
| prep brief v1 `ad9a02d` §3.4 | (4) C-5b ST-1 정의 |
| ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + line 128 (`~/.hermes/auth.json`) / ADR-012 §원칙 9 | entrypoint stat + Hermes ≠ root of trust |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
풀 3+1 합의 보고서 작성 / commit / push / Hermes upstream Dockerfile 본문 변경 (entrypoint stat / chmod / image 빌드 / perm 검증 코드) / Hermes upstream PR 발송 / fork+downstream patch 적용 / downstream wrapper·entrypoint preflight·CI container test 실 구현 / 수단 최종 결정 / 위반 시 동작 fail-closed 고정 / chmod 600 강제 형태 고정 / Hermes PMO 격상 (Layer F) 선언 / Operational Readiness PASS (Layer E) 선언 / Group γ-2·Group β·Backlog #1 ST-2 자동 진입 / §C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경 / Layer D 합의 보고서 본문 변경 / follow-up brief·Group β 합의·prep brief 계보 본문 변경 / MVP-1 exit 발효 / MVP-2 자동 진입 / actual run / CI workflow 변경 / Production docker-compose 변경 / `requirements*.txt` 변경 / Phase α defer-lockdown 변경 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / ADR 본문 자동 갱신 (ADR-008/010/011/012) / 5 영구 핵심 제약 (특히 Hermes ≠ root of trust)·Provider Liquidity 5-way 약화.
