# Agent A — 구현/운영 가능성 분석 (G2 + G3 + G4 통합)

**작성일**: 2026-05-09
**Agent 역할**: 구현/운영 가능성 (Implementation / Operability)
**검토 범위**: G2 + G3 + G4 정식 PASS 승격 + P2 v3 정식 채택 진입 합의 (Phase 2)
**관점 기준 질문**: "실제로 동작하는가? 운영 가능한가?"
**상위 권위**: ADR-011 §2.1 (수단/목적 분리, (a)~(d) 4조건) + (e) 합의 APPROVE = Exit 5조건 패턴, ADR-011 §2.3 권위 위계, ADR-011 §2.4 T1/T2/T3
**금지 (사용자 명시 답습)**: ❌ Hermes PMO 격상 / ❌ P2 v3 정식 채택 자동 선언 / ❌ ADR 본문 자동 갱신 / ❌ archive 처리 / ❌ 실 runtime code / ❌ 다른 Agent 출력 참조 / ❌ 메타포 강제

---

## 0. 요약 (Executive Summary)

본 Agent A 분석은 G2 (governance-preconditions) / G3 (hermes-not-root-of-trust-runtime) / G4 (provider-agnostic-memory-skill) 3 DRAFT 의 **운영 가능성 (Operability)** 만을 본다 (보안/품질은 Agent B, 대안은 Agent C 영역). 결론은 다음과 같다.

1. **3 게이트는 Phase 2 (PoC + Exit (a)~(e) 충족 검증) 진입을 위한 *설계 명세* 수준에서는 충분히 명확하다** — GP-1~GP-6 / G3 22 권한 / G4 17 schema 필드 / JSONL hash chain 모두 ambiguous 한 자리표시(placeholder)가 거의 없고 직접 인계 가능 (구현 task ticket 으로 분해 가능).
2. **그러나 본 합의가 "정식 PASS 승격" 을 의미한다면 7 항목의 운영 부담이 의도된 것이라는 사실을 사용자가 명시적으로 채택해야 PASS 가능** (특히 G2 5 GP × PoC + R-6 workflow 확장 4건 + JSONL hash chain implementation + JCS 표준 준수 + depcruise 룰 셋업).
3. **G2/G3/G4 의존 그래프는 한쪽이 일방적으로 블록되는 형태가 아니다** — 통합 PASS 시 자체참조 위험이 §9 / §4 / §6 으로 다중 보호되며 PoC 진입은 병행 가능. 단, GP-1 은 G1b 흡수로 사실상 즉시 PASS 가능, 나머지 5 GP + G3 7 § + G4 8 Exit 조건은 모두 후속 PoC 의무.
4. **1인 개발자 메타-템플릿 스케일 대비 거버넌스 부담은 *경계선 (boundary)* 수준** — 본 Agent A 의 판정은 "초기 운영 비용은 명백히 무겁지만, 문서가 메타-템플릿 답습용이며 *실 부담은 이 템플릿을 사용하는 새 프로젝트* 에 분산된다는 P2 v3 §1 가정이 유지될 때만 정당".
5. **판정**: **APPROVE WITH CONDITIONS** — 3 게이트 통합 풀 3+1 합의 (옵션 3) 진입 적격. 단, 7 조건 충족 필요 (§7 참조).

---

## 1. G2 (governance-preconditions.md) 분석

### 1.1 GP-1 ~ GP-6 운영 가능성

| GP | 핵심 메커니즘 | 직접 인계 가능? | 운영 부담 | 의존 |
|----|------------|------------|--------|-----|
| GP-1 DB-level Secret Persistence 차단 | SQLCipher BEFORE INSERT trigger + Tier-1 42 catalog | ✅ G1b PASS 시점에 이미 충족 (R-2 / R-4.1 / R-6 actual run) | **0 (이미 운영 중)** | 없음 |
| GP-2 Egress Redaction | Hermes native redaction + P1 facade RedactionFilter + log canary | ✅ Hermes `agent/redact.py` 존재 + Tier-1 42 catalog 적용 | **중 (medium)** — log canary inject step + R-6 확장 PoC 1건 | P1 v2 facade MVP |
| GP-3 Credential / Secret Hygiene | docker secret + chmod 600 + entrypoint stat + inotify + gitleaks pre-commit + CI step | ✅ 기성 도구 조합 — gitleaks / detect-secrets / inotify 모두 production-ready | **중** — entrypoint script + docker-compose.yml + pre-commit + CI step 4 산출 | docker-compose 권위 |
| GP-4 외부 입력 검증 | pydantic schema + regex sanitizer + escape (shlex.quote / SQL bind) + Reviewer LLM 보조 | ✅ pydantic + 표준 escape 라이브러리 | **중** — Worker / tool wrapper 입출력 schema 정의 + injection canary CI step | wrapper 인터페이스 정의 |
| GP-5 Provider Adapter 강제 | depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject | ✅ depcruise 표준 — 정적 분석 충분 | **중** — depcruise config + P1 facade MVP 의존 + CI step | **P1 v2 facade MVP (강한 의존)** |
| GP-6 Memory / Skill Migration | JSONL schema 검증 + 변환 스크립트 자동 테스트 + 라운드트립 검증 | ⚠️ JSONL schema 는 G4 §4 가 정의 — *형식*까지 G4 / *마이그레이션 가능성* GP-6 분리 명확 | **고 (high)** — `scripts/hermes-migration/` 4 스크립트 + 라운드트립 PoC + CI step | **G4 §4 의존 (강한 의존)** |

**합산**:
- 즉시 충족 1/6 (GP-1)
- Phase 2 PoC 작업 5/6 (GP-2 ~ GP-6)
- 강한 의존 2건 (GP-5 → P1 v2 facade, GP-6 → G4 §4)
- 본질적으로 *모두 직접 구현 인계 가능* — placeholder ("TBD" / "별도 합의로 결정") 0건

**핵심 발견**: GP-1 ~ GP-5 의 강제 메커니즘은 *기성 production-grade 도구* 의 조합이며 (SQLCipher + Hermes redaction + docker secret + pydantic + depcruise + gitleaks), 신규 발명이 거의 없다. 운영 가능성 측면에서 매우 강한 점수.

### 1.2 강제 메커니즘 분류 매트릭스 검증 (§2.2)

§2.2 매트릭스가 주장하는 합산 (계산적 6/6, 추론적 보조 4/6, 자동 롤백 6/6) 을 본 Agent A 가 재검증:

- **계산적 6/6 ✅** — GP-3 / GP-5 는 정적 분석 + 권한 체크로 *완전 결정적*. GP-1 / GP-2 / GP-6 의 추론적 보조는 *G2 범위 외* 명시되어 합산에 포함하지 않음. GP-4 의 추론적 (Reviewer prompt injection 감지) 도 *보조* 명시. 분류 정직.
- **자동 롤백 6/6 ✅** — 각 GP 가 R-7 SOP §5 ROLLBACK trigger 또는 PR auto-reject 또는 inotify 즉시 정지 등 *시점-명시된 자동 롤백 경로* 보유. *추론적 판단 없이 발화 가능* (= 운영 가능성 강함).

**원칙 답습 평가**: CLAUDE.md "계산적 검증 우선" 답습 정확. ADR-011 §2.3 운영 함의 #1 ("Hermes 출력은 Tools 로 검증") 패턴 일관.

### 1.3 Entry / Exit 기준 충분성

- **Entry 기준은 모두 명시적 evidence 인용 형태** — "G1b PASS (2026-05-07, 충족됨)" / "ADR-011 §2.3 권위 확정 (충족됨)" / "P1 v2 facade MVP" / "G4 작업 진입 또는 병행" 등. 추상적 "충분히 안전" 같은 추론적 기준 0건. **검증 가능 (verifiable) 강함**.
- **Exit 기준 (a)~(e) 5조건은 ADR-011 §2.1 (a)~(d) + 합의 (e) 패턴 일관** — (a) "동등 이상의 보안 결과" 는 약간의 모호성 (Provider Liquidity 측면 "lock-in 차단" 의 *증명 부담* 이 G4 / GP-5 / GP-6 에서 *최소 2 provider 재해석 가능* 으로 정량화됨). (b) "격리 환경 PoC 실증" 은 R-2 / R-4.1 PoC 패턴 답습 — Docker-First 답습 가능. (c) ADR / SDD 권위 명시 = 문서 작업. (d) 자동 회귀 검증 = R-6 workflow 확장 또는 신규 workflow. (e) 합의 보고서.

**잠재 Gap**: GP-2 의 Exit (a) "동등 이상의 보안 결과" — Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade RedactionFilter 검증 *둘 다* 필요. *어느 쪽이 fail 시 GP-2 fail* 인지 명시 모호. 운영상 둘 *모두* PASS 강제로 해석하는 것이 자연.

### 1.4 §9 메타 안전장치 G3 의존성

§9 는 *interface* 까지만 명시 — 본격 운영 구현은 G3 §5.2 #5 / §5.5 위임. 이는 *G2 PASS 가 G3 PASS 와 결합되지 않으면 무력화* 가능성을 의미. 단, §9.4 "본 §9 가 *지금 강제하는* 것" 4 항목 (사용자 명시 변경 권위 / Hermes 본문 자동 변경 시도 자동 reject 권위 / 풀 3+1 합의 + ADR Amendment 절차 / G2 PASS 의 전제) 은 DRAFT 상태에서도 *권위로* 작동.

**운영 가능성 평가**: *interface 한정* 명시는 정직하나, **G2 PASS 가 G3 PASS 동시 합의 없이 단독 PASS 시 §9 의 본격 운영 구현 (filesystem read-only mount + Hermes-originated commit auto-reject + audit log + T3 변경 감지 hook) 부재로 fox-guarding-the-henhouse 위험**. → 옵션 3 (G2 + G3 + G4 통합 풀 3+1) 채택 시 자연 해결.

---

## 2. G3 (hermes-not-root-of-trust-runtime.md) 분석

### 2.1 22 권한 (T1 8 / T2 2 / T3 12) 분류 운영 가능성

§2.1 허용 8 + §2.2 금지 14 = 22 권한 enumeration 의 운영 가능성:

| 분류 | 항목 수 | 강제 메커니즘 typology | 운영 가능성 |
|------|------|--------------------|---------|
| T1 자동 (#1~#8) | 8 | orchestration log + Tier-1 catalog match + read 권한 | ✅ 모두 *기성 logging + 기존 Hermes 동작 답습* — 신규 구현 부담 거의 없음 |
| T2 사용자 승인 (#15, #16 — Memory promotion / Skill 등록) | 2 | promotion hook 차단 + 사용자 명시 결정 강제 | ✅ pre-commit hook + git layer + 사용자 commit 검증 — 표준 패턴 |
| T3 절대 금지 (#9~#14, #17~#22) | 12 | filesystem read-only + git pre-commit + depcruise + audit log + read-only catalog + override 거부 audit | ✅ 모두 *기성 OS-level + git + 정적 분석 도구* 조합 — 운영 가능 |

**검증 결과**:
- **§2.4 "계산적 22/22, 추론적 보조 6/22, 자동 롤백 14/22"** 매트릭스 (G3 검토 §3.1 P-1 에 따르면 "15/22" 가 정확) — 본 Agent A 도 동일 산술 발견. 단, *해석 위험 0* (T1 #1~#7 외 전부) — 정정 권고 등록.
- **22 항목 중 ambiguous placeholder 0건** — 각 항목에 *권위 근거* (ADR-011 §X / system-identity-prequel §Y / 헌법 Z조) + *강제 메커니즘* (filesystem ACL / git hook / depcruise / audit log) 양쪽 명시. 직접 구현 task 분해 가능.
- **§2.4 합산**: 계산적 22/22 (= "8 중 7 계산적 가능" 합의 §31 보다 강함). 사유는 G3 가 Path-level (P1~P8) 보다 Permission-level 추상화이기 때문.

**운영 부담 평가**:
- 22 권한 enforcement 의 누적 비용 = *filesystem ACL 정책* + *git pre-commit hook 7~8개* + *depcruise config 룰 5~6개* + *audit log JSONL append-only writer* + *T3 변경 감지 hook* + *ROLLBACK trigger R5 등* — **중~고 (medium~high)** 의 일회성 셋업 비용.
- 일단 셋업 후 *운영 비용은 매우 낮음* — 자동 발화, 사람 개입 거의 없음.

### 2.2 권위 위계 운영 + Evidence 결정 5 운영 규칙

§1 충돌 해결 매트릭스 + §5 Evidence 결정 원칙 운영 규칙화 모두 *런타임 동작* 정의:

- **§1.2 충돌 해결 매트릭스** — Hermes vs ADR/SDD / Worker 출력 vs Hermes / Layer 1~6 fail vs Hermes 완료 — 13 시나리오 × 4 측면 (처리 / 권위 / Evidence 요구) 명시. 운영 가능 (각 시나리오 실패 시 어떻게 행동하는지 명확).
- **§1.3 Hard Rule "Evidence 없는 PASS 금지"** — Layer 1~2 hook + Layer 4 CI + Layer 5 합의 의 다층 강제 (4 layer). Evidence Ledger schema 는 system-identity-prequel §6.3 → P2 v3 또는 신규 ADR 영역. *G3 본문은 운영 규칙* 한정 — 형식 정의 위임 명확.
- **§5 5 운영 규칙 + §5.3 PASS 성립 4 요건** — (i) Tools 검증 + (ii) ledger entry + (iii) 사용자 명시 (T2/T3) + (iv) 합의 보고서. 매 PASS 판정 시점에 *4 자동 체크* 가능 — 운영 가능.

**핵심 발견**: §5.3 의 4 요건은 "checked at runtime" 식 자동 검증 가능 — Layer 1~2 hook + ledger 검증 step + git commit author 검증 + commit body 합의 보고서 cross-reference 검증. *전부 계산적*. 운영 가능성 매우 강함.

**잠재 Gap (운영)**: §5.3 (iii) 사용자 명시 승인의 *기술적 검증* — git commit author 가 사용자 GPG 서명 또는 알려진 ID 인지 검증하는 메커니즘이 G3 본문에 명시 안됨. PoC 시점에 도입 필요 (예: GitHub PR review 강제 + branch protection rule).

### 2.3 자기참조 차단 (§4) 적용 한계

§4 "합의 인프라 순환 권위 해결" 은 본 G3 의 **핵심 흡수** (Agent B 단독 발견 합의 §90):

- **§4.3 매트릭스** — 13 결정 유형 × Hermes 단독 가능? + 합의 형태 + 외부 LLM 필요? + 사용자 승인 + 분류. 운영 가능 (각 결정 유형마다 합의 형태 명시).
- **§4.4 Reviewer-only / 외부 LLM / 사용자 승인 조건** — §4.4.2 외부 LLM 필요 조건 4 영역 (Hermes PMO 격상 *필수* / Hermes 정책 변경 *권장* / Constitution / ADR 갱신 *권장* / 자기 작성 산출 검증).
- **§4.5 Hermes 의 합의 결과 처리 권한** — Hermes 는 *기록*만 가능, *승인 주체*가 될 수 없음. 6 처리 권한 표 명시.

**적용 한계 (G3 검토 §5.1 자체 명시 답습)**:
- 본 G3 §4 자체가 *원안* — Reviewer 가 자기 검증하기 어려움. **G3 PASS 합의 시점 외부 LLM 의견 권장 (사실상 필수)**.
- 본 합의 (G2+G3+G4 통합 풀 3+1) 자체가 G3 §4 적용 대상 — 옵션 3 채택 시 외부 LLM 1+ 필수가 G3 §4.4.2 영구 권위. **본 합의 자체에서 외부 LLM 의견 미수집 시 G3 PASS 부적격**.

**운영 가능성 평가**: §4 의 메커니즘 자체는 운영 가능 (git pre-commit hook on Hermes-originated commit + Hermes-originated commit author 검증 + audit log + Reviewer 의 git commit 우회 보존). 단, **본 합의의 외부 LLM 1+ 충족 여부가 PASS 적격성의 binary 조건** 이라는 점 사용자 명시 필요.

### 2.4 합의 인프라 순환 권위 해결 (§5.5)

§5.5 위치 명시 (G2 §9 위임 답습) 의 본문 흐름:
- §4 합의 인프라 순환 권위 해결 본문 자체 → §5.5 (Evidence 결정 원칙) 와 결합
- **운영 메커니즘**: Reviewer 출력은 git commit 으로 Hermes 우회 보존 + 격상/강등 결정은 사용자 명시 commit 만 권위 인정 + Hermes-originated commit 자동 거부

**핵심 운영 가능성**: 본 메커니즘은 *git infrastructure 자체의 권위* 에 의존 — 사용자 GPG 서명 / branch protection rule / PR review 강제 / commit author 검증 모두 GitHub / GitLab 표준 기능으로 운영 가능. **신규 발명 0건**. 운영 가능성 매우 강함.

---

## 3. G4 (provider-agnostic-memory-skill-design.md) 분석

### 3.1 Memory scope 4 단계 (MVP Global+Project) 운영 가능성

§2 Memory scope 4 단계 (Global / Project / Session / Team-Agent) + MVP Global + Project:

- **MVP scope 명시 정확** — Global (`~/.claude/global/`) + Project (`<project>/.claude/project/`) — filesystem 분리 (1차 boundary) + 환경변수 `CLAUDE_MEMORY_SCOPE` (2차 boundary). 운영 가능 (Claude Code 와 OS-level filesystem 동작에 직접 매핑).
- **Session / Team-Agent 보류 사유 정량 트리거** — "파생 프로젝트 ≥ 3건 + LiteLLM 등 외부 도구로 부족한 기능 명확 식별" 명시. *언제 후속 진입할지* 검증 가능 기준. **메타포 강제 금지 답습 정확** (system-identity-prequel §7).
- **Promotion 조건** — Project → Global = manual only (T2). Hermes 자동 promotion 절대 금지 (T3 위반). G3 §2.2 #15 직접 매핑.
- **Boundary 5-layer 강제** — Filesystem / 환경변수 / Plugin scope 검증 / Promotion manual / Filesystem ACL. 모두 *기성 OS + filesystem 동작* — 운영 가능.

**잠재 운영 위험 (G4 검토 §3.1 P-5 답습)**:
- `~/.claude/global/` 디렉토리는 Claude Code 가 향후 표준 명명 사용 시 충돌 가능. 현 시점 미발생. implementation 시점에 `CLAUDE_GLOBAL_MEMORY_PATH` 환경변수 override 도입 검토 권고. **운영 가능성에는 영향 없음** (DRAFT 단계 → implementation 단계 사이에 흡수 가능).

### 3.2 Skill schema 17 필드 운영 가능성

§3.1 17 필드 + §3.2 필드별 검증 규칙 + §3.3 5 상태 전이 + §3.4 자동 생성 vs 자동 승격 분리 + §3.5 `provider_bindings` Provider Lock-in 차단 핵심:

- **17 필드 모두 표준 타입** — string / enum / array / JSON Schema / ISO 8601 — *발명 0건*. 운영 가능.
- **필수 9건 + 권장 8건 분리** — 필수만 충족하면 Skill 동작 가능, 권장은 운영 강화 영역. 점진 도입 가능.
- **`promotion_status` 5 상태 전이** — `proposed` → `approved` → `promoted` → `revoked` / `archived`. 각 전이의 권한 분류 (T1 / T2 / T3) 매트릭스 명확. 운영 가능 (state machine 구현 가능).
- **§3.4 핵심 원칙 "Skill 은 자동 생성될 수 있지만, 자동 승격되어서는 안 된다"** — Hermes 자동 추출 (T1) 분리 + 사용자 승인 강제 (T2) 분리 + Tools + Evidence 강제 (T2) 분리 + 자동 revoke (T3 자동 안전) 분리. **5 단계 권한 매트릭스 매우 명확**. 운영 가능.
- **§3.5 `provider_bindings` 검증 규칙** — `required` / `exclusive` 금지, 모든 binding 은 *optional optimization* 한정, 최소 2 provider 재해석 가능. **명시 가능 verifiable 규칙**. depcruise + 자동 schema 검증으로 운영 가능.

**핵심 발견**: 17 필드 schema 는 본 초안 *원안* 이지만, *실제 schema 구조는 표준 패턴 답습* (UUID + semver + JSON Schema + enum + ISO 8601). 신규 발명 거의 없음. 운영 가능성 매우 강함.

### 3.3 JSONL export hash chain 운영 가능성

§4 JSONL Export/Import 형식 + §4.4 Hash Chain 변조 방지:

- **§4.2 schema** — 1 줄 = 1 entry, 10 필드 (`type`, `scope`, `id`, `schema_version`, `ts`, `agent`, `content`, `evidence_refs`, `prev_hash`, `hash`). 표준 JSON parse + sha256. **`jq` + sha256sum + 표준 도구로 검증 가능** — 운영 가능.
- **§4.3 Hermes 의존 0 보장** — 4 검증 항목 (depcruise / `jq` / schema_version declaration / 외부 오케스트레이터 import). 모두 검증 가능.
- **§4.4 Canonical JSON 정의** — key 정렬 lexicographic + whitespace 제거 + numeric 정규화 + RFC 8259 escape. **G4 검토 §3.1 P-1 (RFC 8785 JCS 인용 부재) 자체 발견** — 본 4 항목 자체로 결정성 충분, JCS 인용은 *권고 보강*. 운영 가능.
- **§4.6 라운드트립 검증 절차** — 5단계 (export → 변환 → 재변환 → canonical sha256 비교) + PASS 조건 (hash 일치 또는 의미 보존 검증). R2-5 답습 — *실제로 동작하는 패턴*. 운영 가능.
- **§4.5 Migration script 사양** — 4 후보 스크립트 (`hermes_to_claude.py` / `hermes_to_openai.py` / `hermes_to_ollama.py` / `import.py`) + 5 사양 요건 (Hermes 의존 0 / 표준 라이브러리 / 라운드트립 검증 / schema_version 명시 / `--dry-run`). **사양까지 — 실 구현은 본 초안 외 (§0.2 #8)**. 운영 가능 (사양만으로 task ticket 분해 가능).

**잠재 운영 위험 (G4 검토 §3.2 P-2 답습)**: schema 진화 정책에서 *필드 추가* (MINOR) 만 명시, *필드 제거* / *변경* 정책 부재. PoC 시점에 정밀화 필요 권고. **운영 가능성 자체에는 영향 없음** (semver 표준 답습으로 흡수 가능).

### 3.4 Memory/Skill boundary 4 금지 강제 메커니즘

§5.2 4 금지:
1. Memory 가 policy 를 대체 — G3 §2.2 #9 #11 (T3) + Memory write 권한 0 (사용자만)
2. Skill 이 ADR / Constitution 우회 — G3 §2.2 #10 #11 (T3) + `allowed_actions` 에 `policy_write` 미포함
3. Session memory 가 Global 자동 승격 — §2.5 promotion T2 강제 + filesystem ACL
4. Hermes 가 skill 을 자기 승인 — G3 §2.2 #16 (T2) + promotion hook 차단 + 사용자 명시 강제

**강제 메커니즘 모두 G3 / G4 / OS-level 권한 조합** — 운영 가능. 4 금지는 *구조적* 보호 (Hermes 가 단독으로 시도 시 hook 차단). 메커니즘이 인계 가능.

**잠재 Gap**: §5.2 #1 "Memory write 권한 0 (사용자만)" — 사용자가 *Hermes 를 통해* Memory write 를 명령하는 시나리오에서 권한 분리 필요. (사용자가 Hermes 에 명령 → Hermes 가 사용자 대리로 write 시도 → hook 이 *commit author = 사용자* 인지 검증?) **G4 본문에서 위 시나리오 처리 절차 명시 약함** — PoC 시점에 정밀화 필요. *운영 가능성에는 영향 없음* (git commit author 검증으로 자연 흡수).

---

## 4. 3 게이트 상호 의존성 / 일관성

### 4.1 의존 그래프

```
G1b PASS (충족) ─┐
                  │
ADR-011 §2.3 ────┤
ADR-011 §2.4 ────┼─ G2 (governance-preconditions)
                  │     │
P1 v2 facade ────┘     │
                        ├──→ GP-1 (G1b 흡수 즉시 충족)
                        ├──→ GP-2 ~ GP-5 (PoC + 합의)
                        └──→ GP-6 ──→ G4 §4 (의존)
                                    │
G3 (hermes-not-root-of-trust) ─────┤
   §6 G2 인터페이스 (5 GP × G3 책임) │
   §7 G4 경계                       │
                                    │
G4 (provider-agnostic-memory-skill)─┘
   §6 G3 인터페이스 (5 항목)
   §7 G2 GP-6 인터페이스
```

**핵심 발견**:
- **3 게이트는 *순환 의존* 이 아닌 *상호 보완* 관계** — G2 GP-6 ↔ G3 §6.5 ↔ G4 §6.5 의 3-way 인터페이스가 책임 분리 명확 (가능성 / 권한 / 형식).
- **G2 §9 메타 안전장치 → G3 §5.2 #5 / §5.5 위임** — 단방향 의존 (G2 가 G3 의 운영 구현에 의존). G3 PASS 없이 G2 PASS 단독 시 §9 본격 운영 부재로 무력화 위험.
- **GP-5 → P1 v2 facade MVP 의존** (강한 의존) — P1 v2 facade MVP 작성이 G2 PASS 의 prerequisite. 본 합의 진행 시 P1 v2 작업 진입 trigger 명시 필요.
- **GP-6 → G4 §4 의존** (강한 의존) — JSONL hash chain 형식 정의가 GP-6 마이그레이션 PoC 의 prerequisite. *G4 PASS 와 G2 GP-6 PASS 는 사실상 함께 합의해야 정합*.

### 4.2 일관성 점검

본 Agent A 가 발견한 일관성 항목:

| 항목 | G2 | G3 | G4 | 일관 여부 |
|------|-----|----|----|---------|
| 권위 위계 (Constitution > ADR > SDD > Harness Gates > Hermes > Worker) | §11 | §1.1 + §11 | §1.3 | ✅ 일관 |
| Hermes ≠ root of trust | §11 | 본 G3 자체 | §11 | ✅ 일관 |
| 자동 정책 변경 금지 (T3) | §9 + §11 | §2.2 #9 #11 #17 #19 #21 + §11 | §5.2 + §11 | ✅ 일관 |
| 수단/목적 분리 ((a)~(e) 5조건) | 각 GP §X.5 | §8.2 | §8.1 (a)~(e) | ✅ 일관 |
| Provider Liquidity | §11 + GP-5 + GP-6 | §11 + §2.2 #18 + §6.4 | §11 + §3.5 + §4.3 + §6.4 | ✅ 일관 |
| 메타포 강제 금지 | §11 | §11 | §11 + §2.4 (Team/Agent 보류) | ✅ 일관 |
| Evidence Ledger (Markdown + JSONL append-only + hash chain) | (G3 위임) | §1.3 + §5.3 | §4.2 + §4.4 | ✅ 일관 |
| 외부 LLM 필요 조건 (PASS 합의 시) | (간접) | §4.4.2 (필수 영역 4건) | §11.1 메타 한계 + §10 변경 절차 | ✅ 일관 |

**합산**: 8/8 일관. 3 게이트 통합 진행 가능 (옵션 3) 의 일관성 토대 충분.

### 4.3 잠재 일관성 위험

- **G2 §8.5 (e) Exit 기준에 G3 §6.5 cross-reference 부재** — G3 검토 §3.2 P-2 답습. G3 §6.5 가 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 명시했으나 G2 §8.5 는 2-way (G2 + G4) 만. 본 합의 PR 묶음 진입 시 cross-reference 갱신 권고. **운영 가능성에는 영향 없음** (단순 cross-ref 갱신).

---

## 5. P2 v3 연결 가능성

### 5.1 P2 v3 §9.2 옵션 A/B/C 매핑

P2 v3 §9.2 는 정식 채택 합의 형태 3 옵션 (A 단축 / B 풀 3+1 / C 보류) 을 명시. 본 합의 (옵션 3 = G2/G3/G4 통합 풀 3+1) 채택 시:

- P2 v3 옵션 B 영역에 직접 매핑 — "G2 / G3 / G4 병행 작성 시작 → 작성 완료 후 v3 정식 채택과 함께 묶음" 답습.
- 본 합의 진입 = P2 v3 §9.2 옵션 B 의 *완성 단계* (G2/G3/G4 모두 DRAFT 적격 검토 APPROVE 완료).

### 5.2 P2 v3 §6 G4 정의 vs G4 통합 문서 정합성

P2 v3 §6 (G4 정의 본문) 은 *분리 작성* 후보 (`memory-scope-design.md` + `skill-format-design.md`) 를 산출 후보로 명시. 그러나 G4 작업은 *옵션 B (Memory + Skill 통합 단일 문서)* 채택 — 사용자 명시 결정 답습.

**연결 가능성**: 정식 채택 합의 시점에 **P2 v3 §6.6 산출 후보 갱신 필요** — 분리 후보 → 통합 단일 문서로. 본 합의 PR 묶음에 흡수 가능.

### 5.3 P2 v3 §7 동시 갱신 ADR 매트릭스

P2 v3 §7 은 정식 채택 시점 ADR-008 / 009 / 010 / 011 cross-reference 갱신 항목 명시. **본 합의는 *cross-reference 갱신* 자체를 트리거하지 않으나** (사용자 명시 답습), PR 묶음 진입 시점에 매핑이 정확. 신규 ADR-014 (Provider-agnostic Memory/Skill Format) 후보 검토는 별도 결정.

### 5.4 P2 v3 정식 채택 진입 가능성 평가

**가능** — 단, 본 합의 (G2+G3+G4 통합 PASS) 가 *동일 PR 묶음* 또는 *순차 PR* 로 진행하는 사용자 명시 결정 후. P2 v3 정식 채택은 본 합의 *결과 흡수 후* 자연 진입 가능 (단순 헤더 DRAFT 제거 + INDEX/CONTEXT 갱신 + ADR cross-reference PR 묶음).

---

## 6. 1인 개발자 메타-템플릿 스케일 거버넌스 부담 평가

### 6.1 정량 부담 추정

본 합의 PASS 후 *Phase 2 (PoC + Exit (a)~(e) 충족 검증)* 진입 시 발생하는 작업 추정:

| 작업 | 추정 부담 | 의존 |
|-----|--------|-----|
| GP-1 PoC | 0 (G1b 흡수) | 없음 |
| GP-2 PoC (log canary inject + R-6 확장) | 1~2일 | 기존 R-6 workflow |
| GP-3 PoC (gitleaks + entrypoint stat + inotify + chmod check) | 2~3일 | docker-compose + Hermes container |
| GP-4 PoC (pydantic schema + injection canary + Reviewer integration) | 3~5일 | Worker / tool wrapper 인터페이스 정의 |
| GP-5 PoC (depcruise config + P1 v2 facade MVP) | **5~10일** (P1 v2 facade MVP 의존) | P1 v2 작업 |
| GP-6 PoC (Hermes JSONL → Claude / OpenAI 변환 스크립트 + 라운드트립 PoC) | **5~10일** (G4 §4 + script 4건) | G4 §4 |
| G3 §1~§7 운영 메커니즘 PoC (filesystem ACL + git pre-commit hook 7~8개 + audit log JSONL writer + 22 권한 enforcement + ROLLBACK trigger) | **10~15일** | 다양 |
| G4 §4 JSONL hash chain implementation + canonical JSON serializer | 3~5일 | 표준 라이브러리 |
| G4 §3 Skill schema implementation + state machine | 3~5일 | pydantic 또는 dataclass |
| 외부 LLM 의견 의뢰 + 풀 3+1 합의 진행 | 5~10일 | GPT/Gemini/Local LLM 접근 |
| PR 묶음 작성 + cross-reference 갱신 | 2~3일 | git workflow |

**합산 추정**: **40~70일 작업량** (1인 개발자, full-time 가정 — 메타-템플릿 자체 작업)

### 6.2 부담 정당성 평가

| 평가 차원 | 결과 |
|---------|-----|
| *현 1인 개발자 스케일* 대비 | **무거움** — 40~70일은 명백히 큰 부담 |
| *메타-템플릿 답습용 가정* 대비 | **합리적** — 본 부담은 *한 번* 발생, 메타-템플릿 사용 새 프로젝트마다 분산 |
| *Hermes PMO 격상 후 자동화 가치* 대비 | **장기적으로 정당** — Layer 1~6 강제 + 자동 회귀 + Memory/Skill 마이그레이션 가능성 = 향후 모든 프로젝트의 기반 |
| *현 v1.0.0 릴리스 + Phase 0 완료 시점* 대비 | **비례 적정** — Phase 0 완료 후 격상 전 단계로서 적절한 부담 |

**핵심 결론**: 본 부담은 *메타-템플릿 답습* 가정이 유지될 때만 정당. 만약 사용자가 *이 프로젝트를 단일 production 프로젝트* 로 사용한다면 부담이 *과대* 가능. P2 v3 §1 + system-identity-prequel "메타-템플릿" 정체성 가정의 유지가 본 합의 PASS 의 *implicit 전제*.

### 6.3 단순화 가능성 (Agent A 자체 발견)

본 Agent A 는 다음 *단순화* 가능 영역을 발견:

- GP-3 의 inotify 사이드카 — 표준 도구 (예: `fsmonitor` 또는 `watchman`) 또는 단순 polling 대체 가능. 운영 부담 감소 가능.
- G3 §2.2 22 권한 enforcement 중 일부 (#14 Hermes PMO 자기 격상 / #21 catalog 자동 확장 등) 는 *현 시점 Hermes 가 권한 자체가 없음* (격상 미발생) — 격상 후 진입 시점에 enforcement 강제. 본 Phase 2 에서 *부분 PoC* 정당.
- G4 §4.5 migration script 4 후보 중 MVP 는 1 (예: `hermes_to_claude.py` 만) 로 시작 가능. 라운드트립 검증 PoC 1회 시연으로 GP-6 (a)~(e) (b) 충족 가능. 나머지 3 스크립트는 후속 진화.

본 단순화는 본 합의 PASS *이후* PoC 진입 시점의 사용자 명시 결정 영역. **본 합의 자체에서 단순화 권고 트리거 금지** — 사용자 명시 답습.

---

## 7. 식별된 위험 / Gap

본 Agent A 가 운영 가능성 관점에서 식별한 risk / gap:

| # | 위험 / Gap | 등급 | 처리 권고 |
|---|---------|----|--------|
| R-1 | GP-5 의 P1 v2 facade MVP 의존 — 본 합의 PASS 시점에 P1 v2 작업 진입 trigger 명시 필요 | MEDIUM | 본 합의 PR 묶음에 P1 v2 진입 결정 포함 |
| R-2 | GP-6 의 G4 §4 의존 — G4 PASS 와 GP-6 PASS 는 사실상 동시 합의 영역 | LOW | 옵션 3 채택으로 자연 해결 |
| R-3 | G2 §8.5 (e) Exit 기준에 G3 §6.5 cross-reference 부재 (G3 검토 §3.2 P-2 답습) | LOW | PR 묶음 cross-reference 갱신 |
| R-4 | G3 §2.4 자동 롤백 합산 산술 14/22 → 15/22 (G3 검토 §3.1 P-1 답습) | VERY LOW | PR 묶음 정정 |
| R-5 | G4 §4.4 RFC 8785 JCS 미인용 (G4 검토 §3.1 P-1 답습) | VERY LOW | PR 묶음 인용 추가 |
| R-6 | G4 §10 schema 진화 정책 (필드 제거 / 변경) 미명시 (G4 검토 §3.2 P-2 답습) | LOW | G4 PASS 합의 시점 정밀화 |
| R-7 | G3 §5.3 (iii) 사용자 명시 승인의 *기술적 검증 메커니즘* (예: GPG 서명 / branch protection) 약함 | MEDIUM | PoC 시점 도입 (GitHub branch protection rule + PR review 강제) |
| R-8 | §9 (G2) 본격 운영 구현이 G3 §5.2 #5 / §5.5 위임 — G2 단독 PASS 시 무력화 | HIGH | **옵션 3 (3 게이트 통합) 채택 필수 조건** |
| R-9 | 외부 LLM 1+ 충족 여부가 본 합의 PASS 적격성의 binary 조건 (G3 §4.4.2) | HIGH | **본 합의에서 외부 LLM 의견 의뢰 + 수집 의무화** |
| R-10 | 메타-템플릿 가정 유지 여부가 거버넌스 부담 정당성의 implicit 전제 | MEDIUM | 본 합의 보고서 헤더 또는 §X 에 명시 |

**HIGH 위험 2건 (R-8, R-9)** 은 본 합의 PASS 의 *binary 조건* — 두 가지 모두 충족 시에만 G2/G3/G4 통합 PASS 적격. **MEDIUM 3건 (R-1, R-7, R-10)** 은 PASS 후 흡수 가능. **LOW/VERY LOW 5건 (R-2~R-6)** 은 PR 묶음 갱신으로 동시 처리 가능.

---

## 8. Agent A 판정

```
APPROVE WITH CONDITIONS
```

### 8.1 판정 근거

**G2 + G3 + G4 정식 PASS 승격은 운영 가능성 측면에서 다음 7 조건 충족 시 PASS 적격**:

1. **옵션 3 (G2 + G3 + G4 통합 풀 3+1 합의 + PR 묶음) 채택** — 단독 PASS 시 §9 (G2) / §6.5 (G4) 의존 무력화 위험 (R-8) 회피 필수.
2. **외부 LLM 1+ 의견 수집** — G3 §4.4.2 영구 권위에 따라 본 합의 자체에서 외부 LLM 1+ 의견 의무화 (R-9).
3. **P1 v2 facade MVP 작업 진입 trigger 명시** — GP-5 PASS 의 prerequisite (R-1). 본 합의 PR 묶음에 P1 v2 진입 결정 포함.
4. **메타-템플릿 가정 명시** — 본 합의 보고서 헤더 또는 §X 에 "본 부담은 메타-템플릿 답습 가정 유지 시 정당, 단일 production 프로젝트 사용 시 재평가" 명시 (R-10).
5. **Phase 2 PoC 진입 trigger 의 사용자 명시 결정 답습** — 각 GP / 각 G3 § / 각 G4 § PoC 진입은 본 합의 PASS *후* 사용자 명시 결정 의무 (자동 진입 절대 금지). ADR-011 §2.4 T2 답습.
6. **5 LOW/VERY LOW 위험 (R-2~R-6) PR 묶음 동시 흡수** — G2 §8.5 cross-ref + G3 §2.4 산술 정정 + G4 §4.4 JCS 인용 + G4 §10 schema 진화 정책 + 본 Agent A 의 본문 매핑 표 cross-ref.
7. **G3 §5.3 (iii) 기술적 검증 메커니즘 PoC 시점 도입 의무** — GitHub branch protection rule + PR review 강제 + GPG 서명 권장 (R-7). PoC 진입 시점에 별도 합의 가능.

### 8.2 운영 가능성 종합 점수 (Agent A 자체 평가)

| 차원 | 점수 (0~10) | 사유 |
|------|---------|-----|
| Ambiguous placeholder 부재 | **9/10** | 거의 0건. G2 §8.5 cross-ref 등 minor only. |
| 직접 구현 인계 가능 (task ticket 분해) | **9/10** | 22 권한 + 17 schema + 8 Exit 조건 모두 구체적. |
| 기성 도구 답습 (신규 발명 0) | **9/10** | SQLCipher / Hermes redaction / depcruise / pydantic / gitleaks / git pre-commit / sha256 / JSON Schema 모두 production-ready. |
| Verifiable Entry/Exit 기준 | **8/10** | (a)~(e) 5조건 패턴 일관. 단, GP-2 (a) "Hermes redaction *과* P1 facade *둘 다* PASS" 명시 약함. |
| 거버넌스 부담 비례성 | **7/10** | 메타-템플릿 가정 시 정당, 단일 프로젝트 시 과대. R-10 명시 필요. |
| 의존 일관성 | **8/10** | 3 게이트 일관 + 의존 그래프 명확. R-8 (옵션 3 필수) 조건 충족 시 8/10. |
| 합의 자기참조 차단 작동 | **7/10** | §4 (G3) 흡수 정확하나 본 합의 자체가 적용 대상 — 외부 LLM 1+ 충족 시 8/10. |

**평균**: 8.1 / 10 — **운영 가능성 "강함" (수준)**.

### 8.3 본 판정의 한계

- 본 Agent A 는 *다른 Agent (B, C) 출력 미참조* — 보안 / 품질 / 대안 측면 미평가. Reviewer 종합 시 보강.
- 본 Agent A 는 *자기 작성 산출 자기 검토* (G2/G3/G4 작성 컨텍스트와 동일). 외부 LLM 의견은 본 Agent A 대체 불가.
- 운영 부담 추정 (40~70일) 은 *메타-템플릿 작성 자체* 한정 — 메타-템플릿 사용 새 프로젝트마다 발생하는 운영 비용은 별도 계산.

---

## 9. P2 v3 정식 채택 진입 가능 여부 판정

```
가능 — 단, 본 Agent A 판정 §8.1 7 조건 충족 + Reviewer / Agent B / Agent C / 외부 LLM 1+ 종합 합의 APPROVE 후
```

### 9.1 P2 v3 정식 채택의 운영 가능성 측면 진입 조건

본 Agent A 의 운영 가능성 관점에서 P2 v3 정식 채택 진입은 다음 4 조건 모두 충족 시 가능:

1. **G2 + G3 + G4 통합 PASS** — 본 합의 결과
2. **P2 v3 §9.2 옵션 B 완성 단계 진입** (G2/G3/G4 작성 완료 후 v3 정식 채택 묶음)
3. **P2 v3 §6.6 G4 산출 후보 갱신** (분리 → 통합 단일 문서) — PR 묶음에 흡수
4. **P2 v3 §7 동시 갱신 ADR 매트릭스 PR 진행** — ADR-008 / 009 / 010 / 011 cross-reference 갱신 + ADR-014 신규 후보 검토

### 9.2 본 진입이 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 — P2 v3 정식 채택 ≠ Hermes PMO 격상. 격상은 별도 합의 + 사용자 명시 결정 + 외부 LLM 1+ 필수
- ❌ ADR-008/009/010/011 본문 자동 갱신 — cross-reference 만, 본문은 별도 PR
- ❌ system-identity-prequel.md / P2 v2 자동 archive — P2 v3 정식 채택 *시점* 에 발생 가능, 단 별도 사용자 명시 결정
- ❌ INDEX / CONTEXT 자동 갱신 — 별도 housekeeping
- ❌ Phase 1 / Phase 2 자동 진입 — 별도 합의

### 9.3 운영 가능성 측면 권고 표현

본 Agent A 권고: **옵션 3 (G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 1+ + PR 묶음) 채택 후 P2 v3 정식 채택 합의는 *별도 단축 합의* 또는 *옵션 3 합의에 묶음* 으로 진행 가능**. 단, *권고 단정 금지* (G2 §10.2 / G3 §8.2 / G4 §8.3 답습) — 사용자 명시 결정 영역.

---

**작성일**: 2026-05-09
**작성자**: Agent A (구현/운영 가능성 분석가)
**판정**: ✅ **APPROVE WITH CONDITIONS** (7 조건 — §8.1)
**P2 v3 정식 채택 진입 판정**: ✅ **가능** — 단, Reviewer / Agent B / Agent C / 외부 LLM 1+ 종합 합의 APPROVE 후
**상위 Reviewer 인계 사항**:
- HIGH 위험 2건 (R-8 옵션 3 필수, R-9 외부 LLM 1+ 필수) 은 본 합의 PASS 의 binary 조건
- MEDIUM 3건 (R-1 P1 v2 진입 trigger, R-7 GitHub branch protection, R-10 메타-템플릿 가정 명시) 은 PASS 후 흡수 가능
- LOW/VERY LOW 5건 (R-2~R-6) 은 PR 묶음 동시 흡수 가능
- 본 Agent A 는 *운영 가능성* 측면 한정 — 보안 (Agent B) / 대안 (Agent C) / 외부 LLM 검증 종합 의무
