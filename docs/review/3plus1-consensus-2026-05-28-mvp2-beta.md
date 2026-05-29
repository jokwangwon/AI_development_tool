# 3+1 합의 통합 보고서 — (β) sub-수단 결정 entry brief (57 entry)

> **작성**: 2026-05-28 (Reviewer 통합)
>
> **대상**: `docs/phase0/mvp2-beta-submeans-decision-brief.md` (v1)
>
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) — 4 source
>
> **입력**: Agent A (구현 분석가, filesystem direct) + Agent B (품질/안전성) + Agent C (대안 탐색) + codex (OpenAI gpt-5.5, cross-vendor blind) — 3 Agent 병렬 독립 (상호 미참조) + codex 독립

---

## §1 4 source verdict 요약

| source | verdict | BLOCKING | 핵심 |
|--------|---------|---------|------|
| Agent A (구현 분석가) | APPROVE WITH CONDITIONS | 3 (R-A-1/2/3) | filesystem 17건 verify — 시제 framing 이 실 동작 범위보다 넓음 |
| Agent B (품질/안전성) | REVISE | 3 (R-B-1/2/3) | 권위 인용 전도 (R-1 MANDATORY / ADR-012 §2.1) + L-1 stdlib 불일치 |
| Agent C (대안 탐색) | REVISE | 2 (R-C-1/2) | L-1 시제 거짓 (실측) + W-A(ii) 명칭 부정확 |
| codex (cross-vendor) | REVISE | 3 (BL-1/2/3) | L 권고 전제 repo 불일치 + 외부 의존성 0 과장 + violation_type evidence |

→ **Reviewer 통합 verdict = REVISE** (3 REVISE + 1 APPROVE WITH CONDITIONS). **결정 방향 (R-4 / L 보존 / W 보존)은 4 source 전원 정합 판정** → REJECT 아님, **brief v1.1 1pass 흡수** (ceremony-inflation 차단, 52/55 entry 동형).

---

## §2 cross-validation 매트릭스

### §2.1 Consensus BLOCKING (multi-source 일치)

| # | BLOCKING | source | 근거 (Reviewer verify) | 정정 방향 |
|---|----------|--------|---------------------|---------|
| **B-1** ⭐⭐⭐ (4-way) | **L-1 stdlib 시제 충족 / 외부 의존성 0 주장 = 거짓** | R-A-2 + R-B-3 + R-C-1 + codex BL-1/BL-2 | Reviewer 직접 verify: `requirements-dev.txt:20-21` = `rfc8785==0.1.4` + `jcs==0.2.1` 고정 / `jsonl_hash_chain.py:99` runtime = `CrossCheckMode.PRIMARY_1_ONLY` (rfc8785 단독, stdlib json.dumps 미사용) / `canonical_json.py:33-42` rfc8785/jcs Primary (try-import) / `g4-hash-chain.yml:64-69` CI `pip install rfc8785 jcs`. **rfc8785/jcs = Q1 합의 2026-05-10 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`) 이미 채택**. 실 시제 = L-5 (외부 library Primary), L-4 (stdlib) 아님 | L 결정 = **"기존 rfc8785/jcs Primary PoC 보존 (Q1 합의 답습) + L-3, 본 cycle 신규 외부 library 도입 0"** 으로 정정. "외부 의존성 0 / stdlib 단독 시제 충족" 삭제. "현 PoC 외부 library 미사용" (false) vs "본 cycle 신규 도입 0" (true) 분리 |
| **B-2** ⭐⭐ (2-way) | **HISTORY_REWRITE dead enum + "4 violation_type 시제 충족" 과장** | R-A-1 + codex BL-3 | `jsonl_hash_chain.py` HISTORY_REWRITE = enum 정의만 (validate_chain emission 0). `g4-hash-chain.yml:197` FAIL 4 cover = prev_hash_mismatch + hash_recalculation + **schema_missing_field** + genesis_mismatch (history_rewrite 아님). brief §1.2 "4 violation_type 시제 충족" vs §7.1 조건 5 "history_rewrite fixture 추가" 자기모순 | "3 violation_type actual emission (PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH) + HISTORY_REWRITE enum 정의만 (fixture 추가 = 조건 6 #5 실 구현 입력)" 분리 |

### §2.2 단독 격상 BLOCKING (Reviewer raw verify 격상)

| # | BLOCKING | source | 근거 (Reviewer verify) | 정정 방향 |
|---|----------|--------|---------------------|---------|
| **B-3** ⭐⭐ | **R-1 "MANDATORY (ADR-011 §2.3 #2)" 권위 전도** | Agent B R-B-1 | Reviewer 직접 verify: ADR-011 §2.3 운영 함의 #2 (line 112) verbatim = "**Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음." = *신뢰 범위 한정* 진술, "MANDATORY" 근거 아님. R-4 채택 핵심 정당화가 모법 과장 | R-1 등급 "MANDATORY (ADR-011 §2.3 #2)" → "GP-2 송신/로그 방어 신뢰 수단 (§2.3 #2 — 저장 경로 책임 0)". R-4 정당화 = defense-in-depth (ends) 기반, "R-1 MANDATORY" 미사용 |
| **B-4** | **"ADR-012 §2.1 = 의존성 추가 PoC 재실행 trigger" misattribution** | Agent B R-B-2 | Reviewer 직접 verify: ADR-012 §2.1 (line 6/64) = "수단/목적 분리" 참조, 의존성 trigger 아님. 정확 권위 = **ADR-011 §2.3 운영 함의 #4 (line 113) "Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증 (R-6)"** + governance. brief 다수 위치 답습 | "ADR-012 §2.1 trigger" → "ADR-011 §2.3 #4 (의존성 변경 → R-2/R-6 자동 재실행)". 단 rfc8785/jcs = Q1 합의 이미 채택이므로 본 L 영역 = 신규 도입 0 (trigger 발화 0) |
| **B-5** | **"보존 우선 = W-A(ii) 변형" 명칭 부정확** | Agent C R-C-2 | W-A 본질 = *단일 통합*, 권고 실질 = *분산 보존 (신규 0)* = 정반대 framing. brief 스스로 "명칭상 W-A(ii), 실질 보존우선" 자인 → 명칭 혼선 후속 전가 | **W-F (분산 보존, 신규 통합/신설 0) 신규 라벨** 정의 또는 (통합/분리)×(신설/보존) 2축 분류 명시. 권고 = W-F + W-E 보조 |
| **B-6** | **조건 6 §7.1 표 R-3 (secret-hygiene) actual run 누락 + 조건 2 매핑 모호** | Agent A R-A-3 | 조건부 승인 조건 6 표가 R-3 (GP-2 (d) 핵심 gating) actual run 을 조건에서 누락. 조건 2 (r2-canary) = R-2 영역이라 R/W 매핑 모호 | 조건 6 표에 R-3 (secret-hygiene-egress-redaction.yml actual run) 명시 + 조건 2 r2-canary 매핑 정정 |

### §2.3 Partial / Divergence

| 영역 | divergence | Reviewer 판정 |
|------|-----------|-------------|
| **W 권고 정합성** | codex = "W-A 단일통합 권고를 repo 현실에 맞춘 정밀화로 정합" vs Agent C = "명칭 부정확 BLOCKING" | **Partial → B-5 로 해소**. 실질 권고 (기존 분산 보존, 신규 0) = 4 source 정합, *라벨* 만 W-F 로 정정 (Agent C 명칭 지적 채택 + codex 실질 정합 판정 동시 충족) |
| **R 권고 정합성** | codex/Agent A/C = "R-4 means-vs-ends 정합" vs Agent B = "R-1 MANDATORY framing 정정 필요" | **Partial → B-3 로 해소**. R-4 결정 자체 = 정합, R-1 *등급 표현* 만 정정 |

### §2.4 Consensus 정합 확인 (BLOCKING 아님 — 4 source 일치)

- ✅ `tests/canonical/` = 72 files / 8 카테고리 / 24 input cases (Agent A + codex 직접 count, B/C 확인)
- ✅ `agent/redact.py` 본 repo 부재 (R-1 upstream 주장 정확) — 4 source
- ✅ `src/adapters/llm/facade.py` placeholder (R-2 trajectory 주장 정확) — 4 source
- ✅ 5 workflow 보존 상태 (실 repo 총 12 workflow, Agent A 발견 — W 보존 권고 강화)
- ✅ `secret_scanner.py --mode scan-log` + registered 45 patterns (R-3 시제 정확) — Agent A/B/C/codex
- ✅ `receive.denyNonFastForwards` local/global 미설정 (실 구현 sub-cycle 입력 정확) — 4 source
- ✅ (γ-c) 특화 의무 4 전원 정합 (Layer subsection / "부분 답습" framing / 통합 동시 / RT-γ-6) — Agent B + codex
- ✅ scope 침입 0건 (실 구현 / 외부 library 도입 / Hermes import / facade real 침입 0) — Agent B
- ✅ R-5 base64 evasion 영구 분리 = known limitation 정당 (secret_scanner.py docstring + 모법) — Agent B
- ✅ history-anchor-verifier.yml = Layer 5 PoC 시제 존재가 Layer 5 진입 유발 0 (55 B-2 답습 정확) — Agent B

---

## §3 권고 (non-blocking, 통합)

| # | 권고 | source | v1.1 흡수 |
|---|------|--------|---------|
| N-1 | "45 = Tier-1 42 + baseline 5" 산술 혼란 → "registered 45 (Tier-1 42 catalog compliant)" | codex | §1.2 표현 정정 |
| N-2 | L-1.5 (stdlib auto-degrade) 중간 대안 추가 (현 PRIMARY_1_ONLY = degrade 없음) | Agent C | §3 대안 + 별도 실 구현 sub-cycle 선택 명시 |
| N-3 | RFC 8785 strict = interop 목적, ≠ 무결성 ends — ends/means 구분 | Agent C | §3.2 means-vs-ends 정합 보강 |
| N-4 | R-4 ≡ "R-3 단독 + R-1/R-2 deferred" framing 선택지화 | Agent C | §2.2 framing 명시 |
| N-5 | R-3 = GP-2 (d) detection 충족 / (a) prevention = R-1/R-2 의존 (facade placeholder 시 능동 redaction 0) | Agent B + Agent A NT | §2.2 + RT-R-2 보강 |
| N-6 | library 버전 drift risk + 성능 미평가 NOTE | Agent A | §7 NOTE |
| N-7 | "L-2/L-5 영구 분리" → "신규 외부 JCS library 도입/운영 승격 = 별도 cycle" | codex | §3 표현 정정 |

---

## §4 v1.1 흡수 매트릭스 (BLOCKING 6 + 권고 7 1pass)

| 흡수 영역 | brief v1.1 정정 |
|---------|---------------|
| B-1 (L stdlib 거짓) | §1.2 + §3.1 + §3.2 + §3.3 + §5.1 — L 결정 "기존 rfc8785/jcs PoC 보존 (Q1 합의 답습), 신규 도입 0" 으로 전면 정정 |
| B-2 (HISTORY_REWRITE dead enum) | §1.2 + §7.1 — "3 emission + HISTORY_REWRITE fixture = 조건 6 실 구현 입력" 분리 |
| B-3 (R-1 권위 전도) | §2.1 + §2.2 — R-1 등급 정정 (§2.3 #2 = 신뢰 범위 한정) |
| B-4 (ADR-012 §2.1 misattribution) | §0.2 #8 + §3.2 + §11 — "ADR-011 §2.3 #4" 정정 |
| B-5 (W 명칭) | §4.1 + §4.2 + §5.1 — W-F (분산 보존, 신규 0) 라벨 정의 |
| B-6 (조건 6 R-3 누락) | §7.1 — R-3 actual run 추가 + 조건 2 매핑 정정 |
| 권고 N-1~N-7 | §1.2 / §2.2 / §3 / §7 in-place |

---

## §5 메타 자기진단 (Reviewer)

| # | 위험 | 처리 |
|---|------|----|
| M-1 | 3 Agent 병렬 독립 미보장 risk | Agent A/B/C 상호 미참조 명시 (각 응답 헤더) + codex 독립 (cross-vendor blind) |
| M-2 | cross-vendor 형식 미충족 | codex = OpenAI gpt-5.5, Agent = Anthropic Claude — 헌법 5조-2 충족 |
| M-3 | Reviewer 격상 (B-3/B-4) 자체 권위 over-reach | Reviewer 직접 raw verify (ADR-011 §2.3 line 112/113 + ADR-012 §2.1 line 6/64 + requirements-dev:20 + jsonl_hash_chain:99) — single-source 격상은 verify 후만 |
| M-4 | REVISE → REJECT 회피 편향 | 4 source 전원 "결정 방향 정합" 판정 명시 (R-4/L 보존/W 보존) — 방향 타당 → 1pass 흡수 정당 |
| M-5 | ceremony-inflation (v2 cycle) | 1pass 흡수 (52/55 entry 동형), 별도 v2 cycle 0 |
| M-6 | 본 cycle 자체 진행 (수단 결정 발효를 실 구현/PASS 발효로 확대) | 본 합의 = 수단 결정 진입 자격 한정, 실 구현 0 / PASS 발효 0 / 외부 library 신규 도입 0 |

---

**본 합의 verdict = REVISE → brief v1.1 1pass 흡수 (BLOCKING 6 + 권고 7) → 수단 결정 발효 자격 충실 (R-4 + L 보존 + W-F + W-E 보조)**.

**본 합의 발효 = brief v1.1 commit + SESSION + INDEX commit + push 후** (단계별 합의 cycle 답습).
