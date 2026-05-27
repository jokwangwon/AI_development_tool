# Backlog #3 Group γ-1 (C-5b ST-1 — Hermes upstream chmod 600) 단독 풀 3+1 합의 보고서

> **본 합의 = Backlog #3 (T3 영역) 中 Group γ-1 (C-5b ST-1 — Hermes upstream Dockerfile entrypoint `~/.hermes/auth.json` chmod 600 강제) *수단 결정 적격성 권위 권고* 발행 한정** — Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) Phase 2 (Independent Analysis, 병렬 독립 분석) + Reviewer (검토 에이전트) Phase 3-4 (교차 비교 + 합의 도출) 통합. **3/3 만장일치 = APPROVE WITH CONDITIONS**.
>
> 본 합의의 어떤 §도 그 자체로 (i) **Hermes upstream Dockerfile *본문* 변경** (entrypoint stat 추가 / chmod 강제 / image 빌드 / perm 검증 코드 작성), (ii) **Hermes upstream PR 발송 / fork+downstream patch 적용 / downstream wrapper·entrypoint preflight·CI container test·init container *실 구현***, (iii) **chmod 600 능동 강제 / 위반 시 동작 fail-closed *고정* / 수단 *최종 결정***, (iv) **Hermes PMO 격상 (Layer F) 선언 / Operational Readiness PASS (Layer E) 선언**, (v) Group γ-2 (Vault HSM ST-4) / Group β / Backlog #1 ST-2 sidecar 자동 진입, (vi) Backlog #4 / #6 / #7 자동 진입, (vii) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (viii) Layer B (`f40423f`) ST-3 docker secret 본문 채택 변경, (ix) Layer D (`210c98f`) 본문 변경, (x) follow-up brief / Group α·β 합의 / γ-1 brief / prep brief 계보 본문 변경, (xi) 외부 LLM 응답 (Gemini + GPT) *결론 강제 채택* (응답 = 입력 한정), (xii) 외부 LLM *추가 자동 호출* / 재의뢰, (xiii) 실 API key / provider SDK / 외부 API 호출 / 실 secret material 처리, (xiv) ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012), (xv) **MVP-1 exit 발효 / MVP-2 자동 진입**, (xvi) 도구 본문 (`tools/*.py`) / CI workflow 변경 / actual run / Production `docker-compose.yml` / `requirements*.txt` 변경, (xvii) **Phase α defer-lockdown 변경**, (xviii) 5 영구 핵심 제약 (특히 Hermes ≠ root of trust) / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (Group γ-1 풀 3+1 합의 진입 — γ-1 brief 옵션 (A) 답습)
**상태**: APPROVED WITH CONDITIONS — Phase 5 (Report) 완료 + 사용자 명시 승인 *전*, commit 0건
**합의 판정**: **APPROVE WITH CONDITIONS** (Agent A + Agent B + Agent C **3/3 만장일치**)
**합의 영역**: Group γ-1 (C-5b ST-1) **수단 결정 적격성 권위 권고 한정** — Hermes upstream 본문 변경 / upstream PR 발송 / 수단 최종 결정 0건
**상위 권위**:
- 진입 brief (본 합의 직접 source) = `docs/phase0/backlog3-groupgamma1-st1-full-3plus1-brief.md` (`79c8ad6` 이후 untracked, §1~§9 + 옵션 (A))
- Group β 합의 = `docs/review/3plus1-consensus-2026-05-20-backlog3-groupbeta-catalog-policy.md` (`aa8a29a`, 잔여 진입 단위 분리 + 풀 3+1 형식 답습)
- Group α 합의 = `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (3/3 만장일치 형식 + γ-1/γ-2 분리 표기)
- 외부 LLM 응답 = `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gemini.md` (Q13/Q15/Q17) + `...-gpt.md` (Q13/Q15/Q17) — 양 vendor 종합 (C) PARTIAL (γ-1 = downstream 형태 진입 가능 수렴)
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (entrypoint stat) + P3 (Credential/OAuth 파일 권한 노출, governance §104) + line 128 (`~/.hermes/auth.json`) / ADR-012 §원칙 9 + §2.8 (single-host SPOF 면책) / ADR-011 §2.1 (a)~(e) + §2.3 권위 위계 (Hermes ≠ root of trust) + §2.4 T3 영역 / governance-preconditions §1.2.7 P11 (Supply-chain Compromise)
- 5 영구 핵심 제약 (특히 #1 Hermes ≠ root of trust) + Provider Liquidity 5-way

---

## 0. 본 합의의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "a 로 진행해주세요" (= γ-1 brief §9 옵션 (A) = Group γ-1 풀 3+1 합의 진입 — Agent A/B/C + Reviewer, 외부 LLM 응답 입력 답습)

선행 명령 답습: "옵션 (D)로 진행 — Group γ-1 풀 3+1 진입 brief" → γ-1 brief 작성 → 옵션 (A) 합의 진입. T3 영역 = 보안 enforcement → CLAUDE.md §3 풀 3+1 의무 (Reviewer-only 단축 부적격, §5 답습).

### 0.2 본 합의가 *하는* 것

1. Phase 1 (Distribution) — γ-1 brief + 3 Agent 관점 분배 답습 (§1)
2. Phase 2 (Independent Analysis) — Agent A / B / C 병렬 독립 분석 결과 요약 (§2)
3. Phase 3 (Cross-Comparison) — 일치 / 부분 / 불일치 / 누락 분류 (§3)
4. Phase 4 (Consensus Resolution) — 최종 판단 + 12 합의 조건 (§4)
5. Phase 5 (Report) — 6 결정 영역 *최종 합의 권고* (§5)
6. Hermes ≠ root of trust 보존 + cross-reference (§6)
7. Rollback Trigger 통합 매트릭스 (Agent C 신규 trigger 흡수) (§7)
8. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§8)
9. 메타 검증 (§9) / 합의 요약 한 단락 (§10) / 부록 A·B

### 0.3 본 합의가 *하지 않는* 것 (사용자 명시 영구 답습)

| # | 금지 | 본 합의 위반 |
|---|------|------------|
| 1 | **Hermes upstream Dockerfile 본문 변경** (entrypoint stat / chmod / image 빌드 / perm 검증 코드) | 0건 (수단 적격성 권고 한정) |
| 2 | **Hermes upstream PR 발송 / fork+downstream patch / downstream wrapper·preflight·CI container test·init container 실 구현** | 0건 (실 구현 = Backlog #6 + downstream evidence + 사용자 명시) |
| 3 | **chmod 600 능동 강제 / 위반 시 동작 fail-closed *고정* / 수단 *최종 결정*** | 0건 (옵션 *적격성* 권고 — chmod 능동 강제 = 기술 BLOCKING 비권고 §2.1) |
| 4 | **Hermes PMO 격상 (Layer F) / Operational Readiness PASS (Layer E) 선언** | 0건 |
| 5 | **MVP-1 exit 발효 / MVP-2 자동 진입** | 0건 |
| 6 | **Group γ-2 (Vault HSM ST-4) / Group β / Backlog #1 ST-2 자동 진입** | 0건 |
| 7 | **§C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경 / Layer D 본문 변경** | 0건 |
| 8 | **CI workflow 변경 / actual run / 도구 본문 / Production `docker-compose.yml` / `requirements*.txt` 변경** | 0건 (Agent A read-only 실행) |
| 9 | **Phase α defer-lockdown 변경** | 0건 (별개 트랙 — 충돌 0건) |
| 10 | 외부 LLM 응답 *결론 강제 채택* / 추가 자동 호출 | 0건 (입력 한정 — Q17 차이 = 평가 대상) |
| 11 | follow-up brief / Group α·β 합의 / γ-1 brief / prep brief 계보 본문 변경 | 0건 |
| 12 | ADR 본문 자동 갱신 / 5 영구 핵심 제약 (특히 Hermes ≠ root of trust)·Provider Liquidity 5-way 약화 | 0건 |

### 0.4 본 합의의 권위 한계

- 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** (Group α / β 합의 패턴 답습).
- 본 합의 발효 ≠ 실 구현 / Hermes upstream 변경 / upstream PR. 실 구현 = **downstream evidence 확보 (Implementation Evidence) + Backlog #6 (Runtime + CI-hook) + 사용자 명시**.
- 외부 LLM 응답 (Gemini + GPT) = *입력* 한정 — 결론 강제 채택 0건 (Q17 차이 = 본 합의 평가 대상).
- Group γ-1 외 영역 (Group γ-2 Vault HSM ST-4) = 별도 합의 영역 (양 vendor MVP-6 보류 권고).

---

## 1. Phase 1 (Distribution) — γ-1 brief + 3 Agent 관점 분배

### 1.1 본 합의 진입 source

| 영역 | 답습 |
|------|------|
| 진입 brief | `backlog3-groupgamma1-st1-full-3plus1-brief.md` (§2 6 결정 영역 + §3 ST 책무 분담 + §4 Hermes≠root of trust + PMO 경계 + §6 Agent 분배) |
| 합의 단위 | **Group γ-1 단독** (C-5b ST-1) — Group γ-2 (Vault HSM ST-4) 분리 (GPT γ-1/γ-2 분리 권고 흡수) |
| 합의 형태 | 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 (T3 영역 의무) |
| 6 결정 영역 | ST-1 진입 시점 / Hermes upstream PR 절차 / chmod 강제 형태 / 위반 시 동작 / ST-2·ST-3 통합 / ST-4 책무 분담 |

### 1.2 3 Agent 관점 분배 + 외부 LLM 응답 (입력 한정)

| Agent | 관점 | 분석 영역 |
|-------|------|----|
| **Agent A** | 구현 분석가 ("실제로 동작하는가?") | entrypoint stat / chmod 기술 구현 + 실 PoC 자산 + downstream wrapper vs upstream PR + 환경 분기 + 기술 한계 (read-only fs / non-root / volume perm) |
| **Agent B** | 품질/안전성 검증가 ("안전하고 견고한가?") | Hermes ≠ root of trust + 5 영구 핵심 제약 + 위험·엣지케이스 + PMO 경계 안전성 + ADR-008 P3 / ADR-012 §원칙 9 / ADR-011 §2.3 정합 |
| **Agent C** | 대안 탐색가 ("더 나은 방법이 있는가?") | downstream-only / perm-by-construction / Evidence Ledger / ST-1↔ST-4 직교 + 신규 6 영역 (NC-1~6) + single-host SPOF 위협모델 |
| Reviewer | 검토 에이전트 | 3 출력 교차 비교 + 일치/부분/불일치/누락 + 6 결정 영역 최종 합의 + Hermes ≠ root of trust 보존 검증 |

| Vendor | 종합 판정 (입력) |
|------|----|
| Gemini 3 Flash | (C) PARTIAL — entrypoint chmod 600 검증 (실패 시 중지) + Dockerfile layer 추가 대안 (1인 부담↓) + PMO 격상 동시·이후 + 외부 LLM 2인 |
| GPT-5.5 Thinking | (C) PARTIAL — downstream wrapper/preflight/CI test 우선 + dev=warn/CI=fail-closed + Hermes 자기 검증 = root of trust 약화 / 외부 harness 검증 + PMO 격상 자동 연결 금지 |
| **양 vendor 수렴** | downstream 형태 진입 가능 + Hermes ≠ root of trust 보존 + 위반 시 환경 분리 + ST-1~ST-4 역할 분담 + ST-4 단독 대체 금지 |
| **차이 영역 (1건)** | Q17 ST-1 ↔ PMO 격상 경계 — Gemini 동시·이후 / GPT preflight = PMO 전 가능 + 자동 연결 금지 |

---

## 2. Phase 2 (Independent Analysis) 결과 요약

### 2.1 Agent A (구현 분석가) — APPROVE WITH CONDITIONS

| 영역 | Agent A 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | entrypoint `stat` permission preflight = repo 내 ST-2/ST-3 PoC 로 *이미 입증* (신규 기술 위험 0) / 수단 형태 = downstream wrapper/preflight/CI test 우선 (기술·1인 부담·root of trust 3축 우월) |
| **결정적 기술 발견** | (1) `docker/gp3-st2-poc/watch-secrets.sh` (`stat -c %a` + chmod 644 fixture) + `gp3-st3-poc` (`mode: 0400` docker secret + `read_only: true` + non-root) = ST-1 stat preflight 답습 자산 / (2) **`chmod 600` *능동 강제* = 기술 BLOCKING 비권고** — read-only rootfs(`EROFS`) / non-root user 가 root-owned `/run/secrets/*` chmod(`EPERM`) / 멱등성·root of trust 침범 → **stat *읽기 검증* 으로 한정** / (3) ST-1 실효 대상 = docker secret 미사용 일반 파일 경로 (`~/.hermes/auth.json` volume/bind) — docker secret 은 ST-3 `mode:0400` 책무 (redundant) |
| 환경 분기 구현 | `HERMES_PERM_ENFORCE={warn\|fail-closed}` 명시 env var 1순위 + `CI` 자동 감지 fallback (build arg 비권고 — single image 원칙, image build↔runtime check 분리) |
| 기술 한계 | non-root user chmod 불가 / read-only fs `EROFS` / docker secret tmpfs perm 이미 고정 / volume·bind mount host perm 상속 (ST-1 주 대상 시나리오) / symlink (`stat -L` 명시) / Hermes upstream image 접근성 불확실 |
| 성능 | entrypoint stat preflight = µs 단위, 컨테이너 시작 시간 영향 **negligible 확정** |
| 진입 조건 | C-Aγ1-1~7 |

### 2.2 Agent B (품질/안전성 검증가) — APPROVE WITH CONDITIONS

| 영역 | Agent B 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | downstream 형태 진입 적격 / **Hermes upstream Dockerfile 본문 직접 변경 + PMO 격상 자동 연결 = 분리 차단** (Hermes 가 자기 secret 안전성 *판단 주체* 화 = ADR-011 §2.3 권위 위계 + ADR-012 §원칙 9 약화) |
| 5 영구 핵심 제약 | **① Hermes ≠ root of trust HIGH (blocking)** — 외부 harness 가 container behavior 검증 (Hermes = 검증 *대상*) + image build↔runtime 분리 + Hermes 자기 검증 금지 / ② 수단-목적 분리 HIGH (ST-1=수단, ADR-008 P3 secret 평문 노출 차단=목적) / ④ 단일 source-of-truth MEDIUM (환경별 canonical secret source) / ③⑤ 영향 없음 |
| 위험 9 영역 | HIGH 5 (R-γ1-1 upstream 본문 변경 root 침범 / R-γ1-2 PMO 자동 연결 / R-γ1-3 fail-closed dev 차단 / R-γ1-4 upstream PR 부담 / R-γ1-5 ST-1+ST-4 책무 중첩) — **완화 불가 HIGH = 0** (upstream 본문 직접 변경만 분리 차단) |
| 엣지케이스 | E-γ1-1 644 위반 / **E-γ1-2 symlink 우회 (lstat vs stat 명시 — 신규 발굴)** / E-γ1-3 volume mount override / E-γ1-5 read-only fs chmod 불가 / E-γ1-7 fail-closed dev 차단 / **E-γ1-9 P11 image 변조 ↔ Hermes≠root 보존책 = 동일 외부 harness 메커니즘 (신규 발굴)** |
| ADR 정합 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + P3 (entrypoint stat = P3 enforcement, downstream 명시 보강) / ADR-012 §원칙 9 (자동 복구 금지 → chmod 강제(b)보다 stat 검증(a) 우선) / ADR-011 §2.1 (a)~(e) 조건부 (수단 최종 결정 = downstream PoC Evidence 후) + §2.3 + §2.4 |
| 진입 조건 | C-B-1~7 (blocking = C-B-1 downstream 형태 / C-B-2 Hermes≠root / C-B-6 PMO 자동 연결 금지) |

### 2.3 Agent C (대안 탐색가) — APPROVE WITH CONDITIONS

| 영역 | Agent C 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 진입 적격 / 수단 *최종 결정* 부적격 (적격성+대안 권고) / **현 brief + 양 vendor 가 *공통으로* "stat 검증 후 정지" + "upstream 을 언젠가 건드린다" 두 전제에 갇혀 우월 대안 누락** |
| 대안 우월 4건 | **AU-1 downstream-only 영구** (upstream PR 0건 — root of trust 침범 *구조적 0*) / **AU-2 perm-by-construction** (read-only fs / tmpfs 0600 mount / init container — feedforward "위반 불가" > feedback "검증 후 정지", CLAUDE.md §2) / **AU-3 위반 시 Evidence Ledger tamper-evident 기록** (Q17 외부 harness 보존책 강화) / **AU-4 ST-1↔ST-4 책무 직교** (분담 아닌 독립 — ST-4 MVP-6 보류가 ST-1 진입 안 막음) |
| Agent C 신규 6건 | NC-1 perm-by-construction (`R-ST1-PERM-CONSTRUCT`) / NC-2 upstream PR 미수락 fallback fork-pin (`R-ST1-UPSTREAM-REJECT-FALLBACK`) / NC-3 Evidence Ledger 기록 (`R-ST1-AUDIT-LEDGER`) / NC-4 ST-3 redundancy (`R-ST1-ST3-REDUNDANCY`) / **NC-5 single-host SPOF ST-1 위협모델 한계** (ADR-012 §2.8 — ST-1 은 644 우발 오설정만 막고 host 전체 침해 미방어) / NC-6 build↔runtime 분리 구현 |
| 위반 시 동작 | **auto-chmod (자동 교정) = 명시 BLOCK** (위반 *은폐* = 안전 결과 목적 위반) + dev=warn/CI=fail-closed + Evidence Ledger |
| PMO 경계 대안 | **downstream-only 로 Q17 차이 자체 우회** — upstream 미접촉 시 Hermes 자기 검증 주체화 여지 0 → root of trust 구조적 보존 |
| 진입 조건 | C-C-γ1-1~8 |

### 2.4 3 Agent 일치 영역 (사전 식별)

| 영역 | A | B | C | 일치 |
|------|----|----|----|----|
| 종합 판정 = APPROVE WITH CONDITIONS | ✅ | ✅ | ✅ | **3/3 만장일치** |
| downstream wrapper/preflight/CI test 형태 진입 적격 (upstream 본문 직접 변경 분리 차단) | ✅ | ✅ | ✅ | 3/3 |
| **Hermes ≠ root of trust 보존 (자기 검증 금지, 외부 harness 검증)** | ✅ | ✅ | ✅ | 3/3 (blocking) |
| **chmod 600 능동 강제 비권고 / stat 검증 우선** | ✅ (EROFS/EPERM 기술 불가) | ✅ (ADR-012 자동복구금지) | ✅ (perm-by-construction 우월) | 3/3 |
| 위반 시 dev=warn / CI·production-like=fail-closed 분리 | ✅ | ✅ | ✅ | 3/3 |
| **PMO 격상 자동 연결 금지 (downstream preflight = PMO 전 가능)** | ✅ | ✅ | ✅ | 3/3 (blocking) |
| ST-1~ST-4 역할 분담 (ST-3 주 injection / ST-1 preflight / ST-2 drift / ST-4 multi-host), 단독 대체 금지 | ✅ | ✅ | ✅ | 3/3 |
| ST-1 ↔ ST-4 책무 분리/직교 (γ-2 MVP-6 보류와 ST-1 진입 독립) | ✅ | ✅ | ✅ | 3/3 |
| **ST-1 docker secret 환경 redundancy** (ST-3 `mode:0400` 책무) | ✅ (C-Aγ1-4) | ✅ (R-γ1-9) | ✅ (NC-4) | 3/3 |
| symlink 처리 명시 (lstat vs stat) | ✅ | ✅ (E-γ1-2) | (포함) | 3/3 |
| image build ↔ runtime check 분리 + rollback 가능 | ✅ | ✅ | ✅ (NC-6) | 3/3 |
| 외부 LLM Q17 차이 = downstream(PMO 전)/upstream(PMO 동시·이후) 분리 정합 | ✅ (GPT 우월) | ✅ (분리 정합) | ✅ (downstream-only 로 우회) | 3/3 |
| 5 영구 핵심 제약 ① HIGH(blocking) ② HIGH ④ MEDIUM / ③⑤ 영향 없음 | ✅ | ✅ | ✅ | 3/3 |
| Provider Liquidity 5-way 영향 없음 | ✅ | ✅ | ✅ | 3/3 |
| 외부 LLM 응답 = 입력 한정 (강제 채택 0건) + 양 vendor (C) PARTIAL 수렴 | ✅ | ✅ | ✅ | 3/3 |
| 수단 적격성 권고 한정 (upstream 본문 변경 / 수단 최종 결정 / fail-closed 고정 0건) | ✅ | ✅ | ✅ | 3/3 |
| 풀 3+1 의무 (Reviewer-only 단축 부적격) | ✅ | ✅ | ✅ | 3/3 |

---

## 3. Phase 3 (Cross-Comparison) — 일치 / 부분 / 불일치 / 누락

### 3.1 일치 (Consensus, 3개 모두 동의) — 16 영역

§2.4 답습 — **16/16 일치 영역**. 본 합의의 핵심 권위 source. 특히 **3 Agent 가 *독립적으로* (i) chmod 능동 강제 비권고 + (ii) ST-1 docker secret 환경 redundancy + (iii) Hermes ≠ root of trust 외부 harness 검증을 동시 도출** — 합의 권위 강화.

### 3.2 부분 일치 (Partial, 2개 동의 / 1개 확장) — 3 영역

| # | 영역 | A | B | C | 분석 |
|---|------|----|----|----|----|
| P-1 | chmod 강제 형태 상위 계층 | stat 검증 + 보고 (chmod 능동 강제 BLOCKING) | stat 검증 우선 + lstat 명시 | **perm-by-construction** (read-only fs/tmpfs 0600/init container) — feedforward > feedback | **부분 — A/B = stat 검증(feedback) / C = 위반 불가 구조(feedforward) 상위 계층 신규** |
| P-2 | upstream PR 절차 범위 | downstream 우선 → evidence 후 최소 patch | downstream 형태 한정, upstream 본문 분리 차단 | **downstream-only 영구 (upstream PR 0건) 도 적격 옵션** (AU-1) | **부분 — A/B = upstream PR을 *언젠가* 전제 / C = upstream 미접촉 영구 경로 추가** |
| P-3 | Q17 PMO 경계 해소 | GPT 우월 (preflight PMO 전, 비결합) | downstream/upstream 분리 정합 | **downstream-only 로 차이 자체 우회** | **부분 — 셋 다 downstream preflight = PMO 전 동의 / C = 차이 소멸 경로 제시** |

#### 3.2.1 P-1 분석 (perm-by-construction)
**Reviewer 평가**: Agent C 의 perm-by-construction (read-only fs / tmpfs 0600 mount / init container) 은 Agent A/B 의 "stat 검증 후 정지" 와 *충돌하지 않는 상위 계층* — CLAUDE.md §2 "feedforward (사전 조향) > feedback (사후 검증)" + 메타 슬로건 ("잘못이 *불가능*하게") 직접 정합. 단 Agent A 의 기술 한계 답습 (Hermes 가 `~/.hermes/`에 write 하는 경우 read-only fs 비호환 = FU-1) → **합의 도출: perm-by-construction 을 *우선 평가 옵션* 으로 추가 + stat 검증을 호환 fallback (Hermes write 요구 시) — 평가 옵션 집합 확장**.

#### 3.2.2 P-2 분석 (downstream-only 영구)
**Reviewer 평가**: Agent C 의 "downstream-only 영구 (upstream PR 0건)" = Agent B 의 "upstream 본문 직접 변경 분리 차단" 의 *극단 강화* — upstream 미접촉 시 Hermes 자기 검증 주체화 여지 *구조적 0* → ① Hermes ≠ root of trust 보존 최강. Agent A 의 기술 비교 (downstream wrapper = upstream image 접근성 불요 + rollback 용이) 도 정합. **합의 도출: downstream-only 영구를 *적격 옵션* 으로 명시 + upstream PR 은 downstream evidence 확보 후 *최후* (그것도 미수락 시 fork-pin fallback NC-2)**.

#### 3.2.3 P-3 분석 (Q17 PMO 경계 해소)
**Reviewer 평가**: 3 Agent 모두 downstream preflight = PMO 격상 *전* 가능 동의 (Gemini 의 PMO 동시·이후 = *upstream 직접 수정* 한정 해석). Agent C 의 downstream-only 가 차이 자체를 우회 (upstream 미접촉 = PMO 경계 논의 불요). **합의 도출: downstream preflight = PMO 전 진입 적격 + upstream 본문 변경 시에만 PMO 경계 논의 (Gemini 외부 LLM 2인) + PMO 자동 연결 금지 (R-ST1-PMO-BOUNDARY)**.

### 3.3 불일치 (Divergence, 3개 모두 다른 의견) — 0 영역

3 Agent 모두 동일하거나 부분 일치 (3/3 만장일치 + 3 부분 일치, C 가 상위 계층/극단 강화). **불일치 0건**.

### 3.4 누락 (Gap, 특정 에이전트만 언급) — 9 영역

| # | 영역 | 출처 | 처리 |
|---|------|----|----|
| G-1 | repo 내 ST-2/ST-3 PoC = ST-1 stat preflight 답습 자산 (구현 HIGH) | A | 흡수 — §2.1 + Implementation Evidence 데이터 |
| G-2 | chmod 능동 강제 기술 불가 (EROFS/EPERM/멱등성) | A | 흡수 — C-Gγ1-3 (stat 검증 한정) |
| G-3 | env var (`HERMES_PERM_ENFORCE`) 1순위 + build arg 비권고 (single image) | A | 흡수 — C-Gγ1-4 |
| G-4 | symlint lstat vs stat 명시 (E-γ1-2) | B | 흡수 — C-Gγ1-3 |
| G-5 | P11 image 변조 ↔ Hermes≠root = 동일 외부 harness 메커니즘 (E-γ1-9) + image digest 고정 | B | 흡수 — C-Gγ1-9 |
| G-6 | ADR-012 §원칙 9 자동 복구 금지 → chmod 강제보다 stat 우선 + ADR-008 P3 권위 | B | 흡수 — §6 + C-Gγ1-3 |
| G-7 | AU-1~4 (downstream-only / perm-by-construction / Evidence Ledger / ST-1↔ST-4 직교) | C | 흡수 — §5 + C-Gγ1-2/5/8/10 |
| G-8 | NC-1~6 신규 (perm-construct / fork-pin fallback / Evidence Ledger / ST-3 redundancy / single-host SPOF 위협모델 / build↔runtime 분리) | C | 흡수 — §7 Rollback Trigger + C-Gγ1-7/11 |
| G-9 | auto-chmod 자동 교정 = 위반 은폐 BLOCK + fail-closed 비상 탈출구 (FU-4) | C | 흡수 — C-Gγ1-6 + C-Gγ1-12 |

**누락 흡수 결론**: 9 누락 영역 모두 흡수 — 충돌 0건. A 실측·기술 / B 안전·ADR 정합 / C 상위 대안·위협모델 = 합의 풍부도 증대.

### 3.5 Phase 3 매트릭스 합산

| 분류 | 영역 수 | 처리 |
|----|----|----|
| 일치 (Consensus) | 16 | 그대로 채택 |
| 부분 일치 (Partial) | 3 | 통합 (§3.2.1~§3.2.3) |
| 불일치 (Divergence) | 0 | — |
| 누락 (Gap) | 9 | 흡수 (§3.4) |

**합산**: 28 영역 모두 합의 도달. **3/3 만장일치 = APPROVE WITH CONDITIONS** 권위 강화.

---

## 4. Phase 4 (Consensus Resolution) — 최종 판단

### 4.1 최종 판정 = **APPROVE WITH CONDITIONS** (3/3 만장일치)

| 영역 | 판정 |
|------|------|
| 종합 판정 | **APPROVE WITH CONDITIONS** (Agent A + B + C 3/3) |
| 합의 단위 | Group γ-1 단독 (C-5b ST-1) — Group γ-2 (Vault HSM ST-4) 분리 |
| 합의 형태 | 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 |
| 진입 적격 범위 | **downstream wrapper / entrypoint preflight / CI container test / init container / perm-by-construction 형태** + 외부 harness 가 container behavior 검증 |
| **분리 차단 범위** | **Hermes upstream Dockerfile 본문 직접 변경 (downstream evidence 후 최소 PR 별도 합의) + chmod 600 능동 강제 + auto-chmod + PMO 격상 자동 연결** (3/3 BLOCKING) |
| 외부 LLM 결론 강제 채택 | ❌ 0건 (입력 한정 — Q17 차이 = downstream-only 로 해소 평가) |

### 4.2 본 합의 조건 (Conditions, 통합 12건) — C-Gγ1-1 ~ C-Gγ1-12

| # | 조건 | 출처 |
|---|------|----|
| **C-Gγ1-1** | **진입 = downstream wrapper / entrypoint preflight / CI container test / init container 형태 한정. Hermes upstream Dockerfile *본문* 직접 변경 = 분리 차단** (downstream evidence 확보 후 최소 upstream PR = 별도 합의). 외부 *harness* 가 container behavior 검증 (Hermes = 검증 *대상*, 판단 주체 아님) | A C-Aγ1-1 + B C-B-1 + C AU-1 (3/3 BLOCKING) |
| **C-Gγ1-2** | **downstream-only 영구 (upstream PR 0건) 도 적격 옵션 — root of trust 침범 *구조적 0*.** upstream PR 미수락 시 fork-pin (commit SHA 고정) fallback (NC-2) | C AU-1 + NC-2 + A §4 + B C-B-1 |
| **C-Gγ1-3** | **chmod 형태 = `stat` *읽기 검증* 우선. `chmod 600` 능동 강제 = read-only fs(`EROFS`) / non-root(`EPERM`) / 멱등성·root of trust 침범 → BLOCKING 비권고. ADR-012 §원칙 9 (자동 복구 금지) 정합. symlink = `lstat` vs `stat` 명시 (E-γ1-2)** | A C-Aγ1-2/5 + B C-B-5 + C (3/3 BLOCKING) |
| **C-Gγ1-4** | **위반 동작 = 환경 분기 (`HERMES_PERM_ENFORCE` 명시 env var 1순위 + `CI` 자동 감지 fallback, dev=warn / CI·production-like=fail-closed). build arg 분기 비권고 (single image, image build↔runtime check 분리). *고정 0건*** | A C-Aγ1-3 + B C-B-4 + C |
| **C-Gγ1-5** | **perm-by-construction 우선 평가 옵션 추가 (AU-2)** — read-only fs / tmpfs 0600 mount / init container = "위반 불가" (feedforward) > "검증 후 정지" (feedback, CLAUDE.md §2 + 메타 슬로건). stat 검증 = Hermes write 요구 시 호환 fallback (FU-1) | C AU-2/NC-1 + P-1 통합 |
| **C-Gγ1-6** | **auto-chmod (자동 교정) = 명시 BLOCK** (위반 *은폐* = 안전 결과 목적 위반, 수단-목적 분리 #2). 위반 사실 = dev=warn/CI=fail-closed + Evidence Ledger tamper-evident 기록 (AU-3) | C AU-3/C-C-γ1-4 + B ② |
| **C-Gγ1-7** | **ST-1 실효 대상 명시 = `~/.hermes/auth.json` 등 일반 파일 경로 (volume/bind/COPY). docker secret `/run/secrets/*` = ST-3 `mode:0400` 책무 → ST-1 redundant 영역 명시** (단일 source-of-truth #4) | A C-Aγ1-4 + B R-γ1-9 + C NC-4 (3/3 독립 도출) |
| **C-Gγ1-8** | **ST-1~ST-4 환경별 canonical secret source 역할 분담** (ST-3 주 injection 전 환경 / ST-1 file perm preflight guard / ST-2 runtime drift Backlog #1 / ST-4 multi-host root γ-2 MVP-6). 단독 대체 금지. **ST-1 ↔ ST-4 책무 *직교*** (ST-4 MVP-6 보류가 ST-1 진입 안 막음, AU-4) | A C-Aγ1-* + B C-B-4 + C AU-4 (3/3) |
| **C-Gγ1-9** | **Hermes ≠ root of trust 보존 (① HIGH blocking)**: "Hermes 자기 검증으로 안전" 금지. ADR-011 §2.3 운영함의 #1 (Hermes 출력은 Tools 로 검증) — secret perm 검증 주체 = Harness Gates 계층 (Hermes 외부). **P11 image 변조 방어 ↔ Hermes≠root 보존 = *동일* 외부 harness 검증 메커니즘** (E-γ1-9) + image digest 고정 (`FROM ...@sha256:<digest>`, P11 (iv)) | A §8 + B C-B-2/C-B-7 + C AU-3 (3/3 BLOCKING) |
| **C-Gγ1-10** | **PMO 격상 자동 연결 금지 (R-γ1-2 HIGH blocking)**: downstream preflight = PMO 격상 *전* 진입 적격. upstream 본문 변경 시에만 PMO 경계 논의 (별도 풀 3+1 + 외부 LLM 2+, Gemini Q17). image build↔runtime check 분리 + rollback 가능 (R-ST1-PMO-BOUNDARY) | A §8 + B C-B-6 + C §5 (3/3 BLOCKING) |
| **C-Gγ1-11** | **single-host SPOF ST-1 위협모델 한계 명시 (NC-5)** — ST-1 은 644 *우발 오설정* 방어, host 전체 침해 미방어 (ADR-012 §2.8 면책 정합). "ST-1 로 안전" 과신 차단 | C NC-5 |
| **C-Gγ1-12** | **본 합의 = 수단 결정 적격성 권위 권고 + DRAFT 한정.** Hermes upstream 본문 변경 / upstream PR 발송 / downstream wrapper·CI test·init container 실 구현 / chmod 능동 강제 / 위반 동작 fail-closed 고정 / 수단 최종 결정 / Hermes PMO 격상 / Operational Readiness PASS / MVP-1 exit / actual run / CI workflow / Phase α defer-lockdown 변경 모두 0건. fail-closed 비상 탈출구 (perm 검증 버그로 정상 0600 차단 시 복구 경로, FU-4) = hard-enforce 진입 *전* 동시 설계 | A C-Aγ1-7 + B + C C-C-γ1-1/7 (3/3) |

**합의 조건 합산**: **12 조건 충족 시 = 본 합의 진입 적합** + 본 합의 = "옵션 채택 권위 권고" 한정. blocking = C-Gγ1-1 (downstream 형태) + C-Gγ1-3 (chmod 능동 강제 비권고) + C-Gγ1-9 (Hermes≠root) + C-Gγ1-10 (PMO 자동 연결 금지).

---

## 5. Final Consensus 6 결정 영역 — 최종 합의 권고

| # | 결정 | **최종 합의 옵션** | 사유 (3/3 만장일치 + 부분 흡수) |
|---|------|----|----|
| 1 | ST-1 진입 시점 | **(a) MVP-1.5 downstream preflight (즉시 적격)** + 수단별 분리 (downstream=즉시 / upstream PR=evidence 후) | downstream 형태 = Hermes 미접촉 = PMO 전 적격 (3/3) — Agent C 수단별 분리 흡수 |
| 2 | Hermes upstream PR 절차 | **(c) downstream wrapper/preflight/CI test/init container 우선** + **(d) downstream-only 영구 (upstream PR 0건) 적격 옵션** ⭐ + upstream PR = evidence 후 최소 patch (미수락 시 fork-pin fallback) | P-2 통합 — upstream 미접촉 = root of trust 침범 구조적 0 (AU-1/NC-2) |
| 3 | chmod 강제 형태 | **(a) `stat` 읽기 검증 우선** + **perm-by-construction (read-only fs/tmpfs 0600/init container) 상위 평가 옵션** ⭐ / **chmod 600 능동 강제 + auto-chmod = BLOCK** | A 기술 불가(EROFS/EPERM) + B ADR-012 자동복구금지 + C feedforward 우월 (3/3 BLOCKING) + P-1 통합 |
| 4 | 위반 시 동작 | **dev=warn / CI·production-like=fail-closed 분리** (`HERMES_PERM_ENFORCE` env var) + **Evidence Ledger tamper-evident 기록** + 위반 메시지 (어떤 파일 어떤 perm 명시) | 양 vendor 수렴 (GPT 우월) + AU-3 흡수 (3/3) |
| 5 | ST-2 / ST-3 통합 | **Defense in depth 역할 분담** (ST-3 주 injection / ST-1 startup preflight / ST-2 runtime drift) + **docker secret 환경 ST-1 redundancy 명시** | 3 시점 비중첩 (inject/boot/runtime) + 3 Agent 독립 redundancy 도출 (C-Gγ1-7) |
| 6 | ST-4 책무 분담 | **ST-1=file system perm / ST-4=HSM secret source *직교*** (분담 아닌 독립) — ST-4 단독 대체 금지 + ST-4 MVP-6 보류와 ST-1 진입 독립 | AU-4 흡수 (γ-1/γ-2 분리 진입 적격성 강화, 3/3) |

**합산**: 6 결정 영역 모두 합의 도달 — **3/3 만장일치 + P-1/P-2/P-3 부분 통합 + G-1~G-9 누락 흡수**. 모든 권고 = *적격성 권고* 한정 (실 구현 = downstream evidence + Backlog #6 + 사용자 명시).

---

## 6. Hermes ≠ root of trust 보존 + cross-reference

### 6.1 Hermes ≠ root of trust 보존 (핵심 안전 쟁점, 5 영구 핵심 제약 #1)

> **Hermes upstream 변경 = root of trust 침범 위험.** Hermes 가 "자기 자신의 secret 안전성을 판단하는 주체" 가 되면 ADR-011 §2.3 권위 위계 (Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents) + ADR-012 §원칙 9 약화. **보존책 (3/3 합의)**: (i) downstream-only 우선 (upstream 미접촉 = 자기 검증 주체화 여지 구조적 0) + (ii) 외부 harness 가 container behavior 검증 (Hermes 자기 검증 ≠ 안전 근거) + (iii) image build↔runtime check 분리 + rollback 가능 + (iv) P11 image 변조 방어 = 동일 외부 harness 메커니즘 + image digest 고정.

### 6.2 기타 cross-reference

| 영역 | 답습 |
|------|----|
| **ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + P3** (Credential/OAuth 파일 권한 노출) | ST-1 = P3 enforcement 직접 구현 후보 — entrypoint stat 가 *downstream wrapper* 인지 명시 보강 (C-Gγ1-1) |
| **ADR-012 §원칙 9 (자동 복구/revert 금지) + §2.8 (single-host SPOF 면책)** | chmod 강제(b)보다 stat 검증(a) 우선 (C-Gγ1-3) + ST-1 위협모델 한계 (C-Gγ1-11) |
| **ADR-011 §2.1 (a)~(e)** | 정책/downstream preflight = 충족 가능 / 수단 *최종 결정* = downstream PoC Implementation Evidence (실 container 측정) 후 별도 합의 |
| **governance-preconditions §1.2.7 P11** (Supply-chain Compromise) | image digest 고정 + 외부 harness 재검증 = Enforcement Tool Self-protection (C-Gγ1-9) |
| **Layer B ST-3 docker secret** (`f40423f` 본문 채택) | ST-3 = 주 injection / docker secret 환경 ST-1 redundant — 본문 변경 0건 (C-Gγ1-7) |
| **Backlog #1 ST-2 inotify sidecar** | ST-2 = runtime drift 책무 — 별도 영역 (C-Gγ1-8) |
| **Group γ-2 (Vault HSM ST-4)** | ST-4 = multi-host root secret source — 책무 직교 + MVP-6 보류 (γ-2 별도 합의, AU-4) |
| **Backlog #6** (Runtime + CI-hook) | downstream wrapper / CI container test 실 구현 = Backlog #6 영역 |
| **Group C Evidence Ledger** (`jsonl_hash_chain.py`) | ST-1 검증 결과 tamper-evident 기록 (C-Gγ1-6, AU-3) |

---

## 7. Rollback Trigger 통합 매트릭스 (Agent C 신규 trigger 흡수)

### 7.1 Group γ-1 진입 Rollback Trigger (답습)

| Trigger | 발화 조건 | 발화 시 행동 |
|----|----|----|
| **ADR-011 §2.4** | T3 영역 (Hermes upstream 변경) 진입 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
| **C-5b ST-1** | Hermes upstream Dockerfile *본문* 변경 결정 | 풀 3+1 + Hermes ≠ root of trust 검토 |
| **R-ST1-UPSTREAM-PR** | Hermes upstream PR 발송 결정 | downstream evidence 확보 후 + 최소 패치 + 별도 합의 |
| **R-ST1-PMO-BOUNDARY** | ST-1 ↔ Hermes PMO 격상 연결 | PMO 자동 연결 금지 — 별도 풀 3+1 + 외부 LLM 2+ (Gemini Q17) |

### 7.2 신규 Rollback Trigger (Agent C NC 흡수 — 구조 한정, 수단 고정 0건)

| Trigger | 영역 | 발화 조건 | 후속 합의 |
|----|----|----|----|
| **R-ST1-PERM-CONSTRUCT** (NC-1) | perm-by-construction 채택 | read-only fs / tmpfs 0600 mount 도입 결정 | 별도 합의 (Hermes write 호환 FU-1 검토) |
| **R-ST1-UPSTREAM-REJECT-FALLBACK** (NC-2) | upstream PR 미수락 | upstream maintainer PR 거부 | fork-pin (commit SHA 고정) fallback |
| **R-ST1-AUDIT-LEDGER** (NC-3) | ST-1 검증 결과 Evidence Ledger 기록 | tamper-evident audit 도입 | Group C Evidence Ledger 연계 별도 합의 |
| **R-ST1-ST3-REDUNDANCY** (NC-4) | docker secret 환경 ST-1 redundancy | ST-3 적용 환경에서 ST-1 중복 측정 | Implementation Evidence 후 별도 합의 |

### 7.3 후속 단계 Rollback Trigger (본 합의 영역 외)

| 영역 | 후속 Rollback Trigger | 분리 사유 |
|----|----|----|
| 실 Hermes upstream Dockerfile 본문 변경 | downstream evidence + 별도 풀 3+1 + 사용자 명시 | Hermes upstream 영역 |
| downstream wrapper / preflight / CI container test / init container 실 구현 | Backlog #6 Runtime + CI-hook 연결 | Backlog #6 영역 |
| ST-4 (Vault HSM) 책무 분담 결정 | Group γ-2 풀 3+1 (MVP-6 보류 권고) | Group γ-2 영역 |
| ST-2 (inotify sidecar) 책무 분담 | Backlog #1 영역 | Backlog #1 영역 |

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | 본 합의 그대로 승인 → 파일화 + commit + push (γ-1 brief + 본 합의 별도 2 commit chain) | commit + push |
| (B) | 본 합의 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 합의 그대로 승인 → 파일화 + commit *까지만* (push 보류) | commit |
| (D) | 본 합의 승인 + push → **Group γ-2 (Vault HSM ST-4 MVP-6 보류 확정) 풀 3+1 진입 brief** (3순위, 양 vendor BLOCK/DEFER 답습) | γ-2 brief |
| (E) | 본 합의 승인 + push → **GP-3 C-3 / GP-5 C-2 condition row 갱신 합의** (해소 선언 — α+β 발효 답습, γ-1 = Vault HSM 외 secret source 부분 진입) | GP entry 갱신 |
| (F) | 본 합의 승인 + push → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief** | Group I |
| (G) | 본 합의 보류 → 세션 종료 | — |

### 8.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 후보: "옵션 (A)로 진행 — 본 합의 그대로 승인하고 γ-1 brief + 합의 별도 2 commit chain commit + push."
- (D) 후보: "옵션 (D)로 진행 — 본 합의 답습 + Group γ-2 (Vault HSM ST-4 MVP-6 보류 확정) 풀 3+1 진입 brief 작성."

---

## 9. 메타 검증

| 검증 영역 | 결과 |
|--------|----|
| Phase 1~5 완수 | ✅ Distribution + Independent Analysis (A/B/C 병렬 독립) + Cross-Comparison + Consensus Resolution + Report |
| 풀 3+1 의무 영역 (T3 보안 enforcement) | ✅ Agent A/B/C + Reviewer 4 역할 (Reviewer-only 단축 부적격 답습) |
| Agent 독립성 (편향 방지) | ✅ A/B/C 상호 비참조 (각 출력에 "다른 Agent 미참조" 명시) |
| 외부 LLM 응답 = 입력 한정 | ✅ 강제 채택 0건 (Q17 차이 = downstream-only 로 해소 평가) |
| 3/3 만장일치 | ✅ APPROVE WITH CONDITIONS (불일치 0건) |
| 12 합의 조건 (C-Gγ1-1~12) | ✅ 등록 (blocking 4건) |
| 사용자 명시 금지 12건 (§0.3) | ✅ 모두 0건 (Hermes upstream 본문 변경 0 / upstream PR 0 / chmod 능동 강제 0 / Hermes PMO 격상 0 / Operational Readiness PASS 0 / MVP-1 exit 0 / actual run 0 / CI workflow 0 / Phase α defer-lockdown 변경 0 / 수단 최종 결정 0) |
| 합산 합의 조건 | 707 → 719 (27 합의 — 본 합의 C-Gγ1-1~C-Gγ1-12 신규 12 등록) — *commit 시 발효* |
| 실 변경 0건 | ✅ Hermes Dockerfile / 도구 본문 / CI workflow / docker-compose 변경 0건 (Agent A read-only 실행 — 기존 PoC 확인) |

---

## 10. 합의 요약 (한 단락)

Backlog #3 T3 영역 中 Group γ-1 (C-5b ST-1 — Hermes upstream Dockerfile entrypoint `~/.hermes/auth.json` chmod 600 강제) 단독 풀 3+1 합의 (Agent A 구현 분석가 + Agent B 품질/안전성 검증가 + Agent C 대안 탐색가 병렬 독립 분석 + Reviewer 교차 비교·합의 도출) 결과 = **APPROVE WITH CONDITIONS (3/3 만장일치)**. 진입 적격 범위 = **downstream wrapper / entrypoint preflight / CI container test / init container / perm-by-construction 형태** + 외부 harness 가 container behavior 검증. 분리 차단 범위 (3/3 BLOCKING) = **Hermes upstream Dockerfile 본문 직접 변경 (downstream evidence 후 최소 PR 별도 합의) + chmod 600 능동 강제 (Agent A 실측 — read-only fs `EROFS` / non-root `EPERM` 기술 불가) + auto-chmod (위반 은폐) + PMO 격상 자동 연결**. 12 합의 조건 (C-Gγ1-1~C-Gγ1-12) = downstream 형태 한정 / downstream-only 영구 적격 (root of trust 침범 구조적 0) / stat 검증 우선·chmod 능동 강제 비권고·symlink lstat 명시 / dev=warn·CI=fail-closed 환경 분기 / perm-by-construction 상위 평가 옵션 (feedforward > feedback) / auto-chmod BLOCK + Evidence Ledger 기록 / ST-1 docker secret 환경 redundancy (ST-3 책무) / ST-1~ST-4 역할 분담 + ST-1↔ST-4 직교 / Hermes ≠ root of trust 보존 (외부 harness 검증 + P11 image 변조 동일 메커니즘) / PMO 격상 자동 연결 금지 / single-host SPOF ST-1 위협모델 한계 / 수단 적격성 권고+DRAFT 한정. 핵심 안전 쟁점 = Hermes upstream 변경 = root of trust 침범 위험 (5 영구 핵심 제약 #1 HIGH blocking) → Agent C 의 downstream-only 영구 경로가 upstream 미접촉으로 Hermes 자기 검증 주체화 여지를 *구조적 0* 으로 만들어 외부 LLM Q17 차이 (Gemini PMO 동시·이후 / GPT preflight PMO 전 가능)를 해소. 결정적 발견 = repo 내 ST-2/ST-3 PoC (`docker/gp3-st2-poc` stat + `gp3-st3-poc` `mode:0400`) 가 ST-1 stat preflight 를 이미 실증 (구현 HIGH, 신규 기술 위험 0) + 3 Agent 가 *독립적으로* chmod 능동 강제 비권고 + ST-1 docker secret 환경 redundancy + Hermes≠root 외부 harness 검증을 동시 도출. 5 영구 핵심 제약 ①(HIGH blocking)·②(HIGH)·④(MEDIUM) 모두 condition 보존 가능 (③⑤ 영향 없음). 외부 LLM 양 vendor (C) PARTIAL 수렴 = 입력 한정 (강제 채택 0건). 본 합의 = 수단 결정 적격성 권위 권고 발행 한정 — Hermes upstream Dockerfile 본문 변경 / upstream PR 발송 / downstream wrapper·CI test·init container 실 구현 / chmod 능동 강제 / 위반 동작 fail-closed 고정 / 수단 최종 결정 / Hermes PMO 격상 / Operational Readiness PASS / MVP-1 exit / actual run / CI workflow / Phase α defer-lockdown 변경 / 외부 LLM 강제 채택 모두 0건이며, 모든 *결정* 은 별도 풀 3+1 합의 (downstream Implementation Evidence + 사용자 명시 후). 합산 합의 조건 707 → 719 (27 합의 — commit 시 발효).

---

## 부록 A — 다음 단계 옵션 (사용자 결정 영역)

§8 답습. 본 합의 = Phase 5 (Report) 완료 + 사용자 명시 승인 *전* 상태 (commit 0건). staged cycle (brief → 승인 → 합의 → commit → push) 답습 — commit / push = 사용자 명시 승인 후 별도 단계.

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
Hermes upstream Dockerfile 본문 변경 (entrypoint stat / chmod / image 빌드 / perm 검증 코드) / Hermes upstream PR 발송 / fork+downstream patch 적용 / downstream wrapper·entrypoint preflight·CI container test·init container 실 구현 / chmod 600 능동 강제 / auto-chmod 자동 교정 / 위반 시 동작 fail-closed 고정 / 수단 최종 결정 / Hermes PMO 격상 (Layer F) 선언 / Operational Readiness PASS (Layer E) 선언 / Group γ-2·Group β·Backlog #1 ST-2 자동 진입 / Backlog #4/#6/#7 자동 진입 / §C-5b 상태 표기 재변경 / Layer B ST-3 docker secret 본문 채택 변경 / Layer D 본문 변경 / follow-up brief·Group α·β 합의·γ-1 brief·prep brief 계보 본문 변경 / MVP-1 exit 발효 / MVP-2 자동 진입 / actual run / CI workflow 변경 / Production docker-compose 변경 / `requirements*.txt` 변경 / Phase α defer-lockdown 변경 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / ADR 본문 자동 갱신 (ADR-008/010/011/012) / 5 영구 핵심 제약 (특히 Hermes ≠ root of trust)·Provider Liquidity 5-way 약화.
