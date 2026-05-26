# 시스템 정체성 Prequel — AI Development Company OS — **Archived (2026-05-09 후속 8)**

> **상태: Archived (2026-05-09 후속 8 — P2 v3 (Hermes Adoption Design v3) Design Adoption only 정식 채택 (2026-05-09 후속 6) + P2 v2 Archived 전환 (2026-05-09 후속 7) 후속, 단축 합의 APPROVE)**.
>
> 본 prequel **§1.2 운명 자체 명시** ("P2 v3 작성 완료 시 → 본 문서 §2~§9가 v3 §1~§4로 정식화, 본 문서는 archived 처리") 답습 — *예고된 정상 archive 절차* 정합.
>
> **본 prequel 본문 인용은 *역사적 사실 추적 + AI Dev Company OS 정체성 직접 권위 출처* 한정** — 새 작업은 P2 v3 본문 + ADR-011 / ADR-012 / ADR-009 C-N + G3 + G4 본문을 권위 우선 인용 의무.
>
> **prequel 핵심 권위 이관 매트릭스** (16 영역 = 12 완전 흡수 + 4 부분/분산 흡수):
> - §3 권위 위계 (`Constitution > ADR > SDD > Harness > Hermes > Worker`) → **ADR-011 §2.3 영구 권위 승격** ("prequel 폐기 후에도 보존" 직접 명시) ✅
> - §3.3 Hermes 가 *하지 않는* 것 → P2 v3 §2.1.2 (6항목) ✅
> - §4 Hermes 역할 재정의 + 4 게이트 G1~G4 → P2 v3 §2 + §3 + §4 / §5 / §6 (G2 / G3 / G4 정식 산출) ✅
> - §5 T1/T2/T3 분류 → **ADR-011 §2.4 영구 권위 승격** ("prequel §6의 3-tier 선언을 ADR 권위로 승격") ✅
> - §6.1 5단계 명제 ("Agent proposes / Hermes orchestrates / Tools verify / Evidence decides / Human overrides") → G3 §5 + ADR-012 §1.2 직접 답습 ✅
> - §6.3 Evidence Ledger MVP (10 필드 schema) → G4 §4.2 (10 필드) + ADR-012 §2.2 (11 필드, `event` 추가 — **흡수 + 강화**) ✅
> - §6.4 Schema 고정 시점 ("Phase 1 종료 시 ADR-012 발행") → **ADR-012 (2026-05-09 후속 3 PR-2 신규 발행, 트리거 실현 완료)** ✅
> - §7 메타포 강제 금지 → P2 v3 §10.1 #3 (Normative Constraints) + §10.2 Archive Migration Note + ADR-012 §1.5 + §9 + P2 v3 §2.5 ✅
> - §8.1 Worker Agent 4 역할 (PM/Architect/Implementation/Reviewer) → multi-agent-system-design.md (정식 산출) + P2 v3 §2.1 cross-reference ✅
> - §8.4 Memory 2단계 (Global / Project) → G4 §2.1 (Memory Scope 4 단계) + §2.2 (MVP scope Global + Project) ✅
> - §8.5 Evidence Markdown + JSONL → G4 §4 + ADR-012 §2.2 (11 필드 schema) ✅
> - §9 Phase 0 R-1 처리 → ADR-011 §1.1 (P2 v2 가정의 붕괴 명시) + §2.2 (G1a FAIL 확정) + P2 v3 §1.1 + §3.2 G1a (폐기) ✅
> - **§2.1 정체성 선언** ("이 도구는 단일 AI 모델을 잘 쓰는 도구가 아니라...") / **§2.2 메타포 매핑** (회사 메타포 5 row) / **§2.3 핵심 명제** ("사원 AI는 자주 바뀔 수 있다") → 부분/분산 흡수 (P2 v3 §2.1 부분 + ADR-011 §2.3 + ADR-009 C-N §5 분산) — **옵션 A 채택으로 prequel §2 본문 보존, 직접 권위 출처 영구 보존** (AI Development Company OS 정체성 보존 강도 HIGH)
>
> **본 archive 가 *발생시키지 않는* 것** (P2 v3 §10.2 Archive Migration Note + ADR-012 §605 답습):
> - ❌ Hermes PMO 격상 활성화
> - ❌ Runtime Implementation PASS 선언
> - ❌ G2 / G3 / G4 Implementation PASS 선언
> - ❌ **P2 v3 정식 채택 재해석** (사용자 명시 금지)
> - ❌ ADR-008 / 009 / 010 / 011 / 012 본문 자동 갱신 (cross-reference 만 — 본 archive commit *후* 별도 PR)
> - ❌ 실 runtime code / migration script / hook 구현
> - ❌ Tier-2 / Tier-3 catalog 자동 확장
> - ❌ 5 영구 핵심 제약 약화 (§10.2 Archive Migration Note 답습)
> - ❌ AI Dev Company OS 정체성 약화 (옵션 A 채택으로 §2 본문 영구 보존)
>
> **본 archive 후 5 영구 핵심 제약 보호 강도 = HIGH 5/5** (P2 v3 §10.1 + §10.2 + ADR-011 §2.3/§2.4 + ADR-012 §원칙 5/6/9 + ADR-009 §5 영구 권위 답습) — **메타포 강제 금지 (#3) 의 *모법* 인 prequel §7 본문 보존 (옵션 A) 으로 권위 출처 약화 0건**.
>
> **본 archive 합의 권위**: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md` (Reviewer-only 단축 합의 APPROVE — 8/8 검토 기준 PASS + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 A 최소 침습 권고).
>
> **이전 상태 (2026-05-05 ~ 2026-05-09 후속 7)**: 임시 선언 (Pre-Declaration). P2 v3 정식 채택 (2026-05-09 후속 6) + P2 v2 Archived 전환 (2026-05-09 후속 7) 후 본 prequel → Archived 전환 (2026-05-09 후속 8).

**상태**: **Archived** (P2 v3 정식 채택 + P2 v2 Archived 후속, 2026-05-09 후속 8 단축 합의 APPROVE Reviewer-only)
**최종 수정**: 2026-05-05 (임시 선언) → **2026-05-09 후속 8 Archived**
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`
**Archive 합의**: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md` (2026-05-09 후속 8 Reviewer-only 단축 합의)
**후속 권위 (Active)**: `hermes-adoption-design-v3.md` (P2 v3, **Adopted — Design Adoption only**, 2026-05-09 후속 6) + `ADR-011-means-vs-ends-redaction.md` §2.3 + §2.4 (영구 권위 승격) + `ADR-012-evidence-ledger-protection.md` (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행) + `ADR-009-self-adapter-v2-entry-conditions.md` C-N (2026-05-09 후속 4 갱신)
**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-009 C-N, ADR-010, **ADR-011 (영구 권위 — prequel §3 / §5 승격)**, **ADR-012 (Evidence Ledger Protection — prequel §6.4 트리거 실현)**
**관련 문서**: `docs/architecture/hermes-adoption-design-v3.md` (P2 v3, Adopted), `docs/architecture/hermes-adoption-design.md` (P2 v2, Archived 2026-05-09 후속 7), `docs/phase0/day1-environment-and-fact-check.md`, `docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`

> **이하 본문 (§1 ~ §10) = 2026-05-05 임시 선언 시점 사실 보존** (옵션 A — 최소 침습 채택, 본문 변경 0건). 본 §2 정체성 선언 / §3 권위 위계 / §6 Evidence 기반 검증 / §7 메타포 강제 금지 / §8 MVP 범위 / §9 R-1 처리 등 모든 본문은 *역사적 사실 + AI Dev Company OS 정체성 직접 권위 출처* 로 영구 보존. 새 작업은 P2 v3 + ADR-011 / ADR-012 / ADR-009 C-N + G3 + G4 본문을 권위 우선 인용 의무.

---

## 1. 목적과 운명

### 1.1 목적
Phase 0 Day 1~2에서 발견된 P2 v2 가정 오류(`add_pre_record_hook` 공식 미존재 등)와 GPT 외부 검토 결과(시스템 정체성 재정의 제안)를 풀 3+1 합의로 종합한 결과를 즉시 반영하기 위해, P2 v3 정식 작성 시점(Phase 0 R-7 완료 후)까지 **방향성·원칙·MVP 범위만 임시 선언**하는 문서.

### 1.2 운명
본 문서는 다음 시점에 **폐기 또는 흡수**된다:
- P2 v3 작성 완료 시 → 본 문서 §2~§9가 v3 §1~§4로 정식화, 본 문서는 archived 처리
- Phase 0 R-1에서 Hermes hook 가정이 추가로 무너질 경우 → 합의 옵션 (2) C-③안 변형으로 자동 전환, 본 문서 일부 (Hermes 역할 재정의) 무효화

### 1.3 본 문서가 다루지 않는 것
- 구현 상세 (P2 v3 작성 시 정의)
- ADR-011 등 신규 ADR 발행 (P2 v3 PR과 묶음 처리)
- Role Contract 25건 본문 (별도 `docs/roles/AGENT_<NAME>.md`)
- 6 거버넌스 사전조건 매트릭스 (별도 `docs/architecture/governance-preconditions.md`)

---

## 2. 시스템 정체성 — AI Development Company OS

### 2.1 선언

> **이 도구는 단일 AI 모델을 잘 쓰는 도구가 아니라, 교체 가능한 여러 AI 모델과 도구들을 하나의 개발 조직처럼 운영하는 OS이다.**

사용자의 아이디어가 검증 가능한 설계와 테스트 가능한 코드로 자동 전환되는 자가 진화형 AI 개발 회사 OS를 만드는 것이 최종 목표.

### 2.2 메타포 매핑

| 회사 메타포 | 시스템 매핑 |
|-----------|-----------|
| 창업자 / 최종 의사결정자 | 사용자 (1인 개발자) |
| 운영 본부 / PMO | Hermes (4 게이트 충족 후 활성화) |
| 사원 (교체 가능) | Worker AI (Claude Code, GPT, Local LLM, Gemini 등) |
| 팀장/전문가 | Worker Agent (PM/Architect/Implementation/Reviewer — MVP 4 역할) |
| 회사 정관 / 규칙 / 기록 체계 | Constitution / ADR / SDD / Evidence Ledger |

### 2.3 핵심 명제

> **사원 AI는 자주 바뀔 수 있다. 하지만 회사의 원칙·의사결정 체계·검증 방식·기억 구조는 유지되어야 한다.**

→ 헌법 5조 (Provider Liquidity) 의 메타포적 표현. Claude/GPT/Gemini/Local LLM은 언제든 교체 가능, Constitution/ADR/SDD/검증 게이트/역할 계약/프로젝트 기억은 유지.

**[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S2 답습]**: 본 §2.3 line 93 표기 "헌법 5조 (Provider Liquidity)" + §4.2 line 152/154 "헌법 8조·5조" / "헌법 5조" + §5.2 line 175 "Provider Liquidity 일부 면제" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") 中 system-identity-prequel 정정 자격 직접 발효 (R-S2 CRITICAL). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인), (P3) 약식 통일 cycle DEFER carry-over. (P4) 신규 verbatim 유형 신설 *기각* + Reviewer 권한 한계 (11) sub-boundary 신설 *기각* + (g1-N-3) chain 영구 종결 명문 의무 답습 영구. 본 cycle 합의 = `209f04d`. **본 §1.1 line 94 (`note: prequel = Archived 2026-05-09 후속 8` 답습 vs ADR-011 §2.3 영구 권위 승격 답습)** = archive 후에도 권위 보존 명문 답습 ((ii-b) 헌법-직접-매핑 강도 보존).

---

## 3. 권위 위계 (Authority Hierarchy)

### 3.1 위계

```
Constitution
   > ADR
      > SDD
         > Harness Gates (Layer 0~6)
            > Hermes
               > Worker Agents
```

### 3.2 핵심 명제

> **Hermes는 root of trust가 아니다.**

Hermes의 판단만으로 작업을 PASS 처리할 수 없다. 최종 신뢰 근거는 **계산적 검증 결과 + Evidence**다.

### 3.3 운영적 강제 (P2 v3에서 상세화)

본 prequel에서는 강제 메커니즘을 다음 4가지로 선언만 하고, 구현 상세는 6 거버넌스 사전조건 매트릭스(별도 문서)에서 정의:

1. **파일시스템 read-only on Constitution/ADR/SDD**: Hermes/Worker는 `docs/constitution/`, `docs/decisions/ADR-*.md`에 write 권한 없음
2. **합의 결과는 Hermes를 우회**: Reviewer 출력은 git commit으로 직접 보존 + user-facing UI 직접 전달. Hermes는 합의 결과를 "참조"만 가능, "수정" 불가
3. **모든 Hermes-originated 변경은 audit log**: Hermes process가 발생시킨 file write·config write는 별도 로그에 기록
4. **권위 등급 위반 시 자동 reject**: 변경 대상의 권위 등급이 Hermes 이상이면 자동 차단

---

## 4. Hermes 역할 재정의 (현 미활성)

### 4.1 재정의된 역할

```
Hermes = AI 조직의 운영 본부 + 기억 관리자 + Skill 관리자 + 합의 프로토콜 실행기
```

담당 후보 (4 게이트 충족 후 활성화):
1. 사용자 아이디어를 작업 가능한 단위로 구조화
2. Phase 0 질문지 또는 브리프 생성
3. 작업 위험도 분류
4. 필요한 ADR/SDD 문서 판단
5. 3+1 멀티 에이전트 합의 프로토콜 실행
6. Worker Agent (Claude Code, GPT 등) 호출 및 조율
7. 반복되는 작업을 Skill 후보로 추출
8. 프로젝트별 Memory 관리
9. 작업 결과를 Evidence Report로 남김
10. 성공/실패 패턴을 다음 프로젝트에 재사용

### 4.2 활성화 4 게이트 (G1~G4)

**전부 충족 시 Hermes PMO 격상 활성화**:

- **G1**: Phase 0 R-1 (canary 검증) 완료 — Hermes 자체 redaction이 DB INSERT 경로에 실제 적용되는지 격리 환경 검증
- **G2**: 6 거버넌스 사전조건 충족 (`docs/architecture/governance-preconditions.md`, 별도 작성) — 헌법 8조·5조 위반 경로 P1~P8 각각 강제 메커니즘 매핑
- **G3**: "Hermes ≠ root of trust" 운영적 구현 (§3.3 4가지 + 합의 인프라 순환 권위 해결)
- **G4**: Provider-agnostic Memory/Skill 저장 형식 확정 (Hermes plugin lock-in 회피, 헌법 5조)

### 4.3 게이트 미충족 시

- 1개 이상 미충족 → Hermes는 현 ADR-008 합의 자동화 책임만 유지, PMO/Memory/Skill 격상 보류
- Phase 0 R-1 추가 흔들림 (예: hook 가정 더 무너짐) → 합의 옵션 (2) C-③안 변형 자동 전환 → Hermes PMO 격상 6~12개월 완전 보류

---

## 5. 자동 학습 ≠ 자동 정책 변경 (T1/T2/T3)

### 5.1 핵심 명제

> **자동 학습은 허용한다. 자동 정책 변경은 금지한다.**

### 5.2 3-tier 분류

| Tier | 명칭 | 예시 | 자동화 |
|------|------|------|-------|
| **T1** | 작업 패턴 학습 | "이 명령 후 보통 lint 실행", "이 에러는 보통 import 누락" | 자동 OK (Skill 후보로 등록만, 적용은 사용자 승인) |
| **T2** | 검증 단계 추가/제거 | "이 commit 전에 typecheck 추가" | **사용자 승인 강제** |
| **T3** | 정책/헌법/ADR 수정 | "redaction 강도 완화", "Provider Liquidity 일부 면제" | **절대 금지** (사용자라도 ADR 절차 거쳐야) |

### 5.3 비대칭 위험

> **새 검증 단계의 추가는 보수적이라 안전해 보이지만, 다음 단계에서 제거(반대 방향)가 자동화되면 비대칭 위험이다. 추가/제거 모두 T2로 분류한다.**

---

## 6. Evidence 기반 검증 원칙

### 6.1 5단계 명제

> **Agent proposes / Hermes orchestrates / Tools verify / Evidence decides / Human overrides**

한국어:
- 에이전트는 제안한다
- Hermes는 조율한다 (4 게이트 충족 후)
- 도구는 검증한다 (계산적 우선)
- 증거가 통과 여부를 결정한다
- 사람은 최종 방향을 선택한다

### 6.2 최종 통과 기준

다음 모두 충족 시에만 PASS:

- 테스트 통과
- 린트 통과
- 타입체크 통과
- secret scan 통과
- build 통과
- ADR/SDD 충돌 없음
- redaction canary 통과
- SQLCipher 암호화 확인 (Hermes 격상 후)
- JSONL export 가능성 확인 (Hermes 격상 후)
- Evidence 파일 존재

### 6.3 Evidence Ledger 최소 구현 (MVP)

**복잡한 DB schema는 미시작**. Phase 1 (~3개월) 까지 다음 최소 구조:

- **Markdown** (`docs/evidence/<task-id>.md`): 사람 검토 대상 (PR 검토 결과, 합의 보고서)
- **JSONL** (`docs/evidence/ledger.jsonl`): 자동화 분석 대상 (테스트/lint/secret scan 결과). append-only.
- **변조 방지**: hash chain (이전 entry hash + 현재 entry hash) 또는 git append commit. 둘 중 하나 의무.
- **Schema** (JSONL 1줄):
  ```
  {
    "ts": "2026-05-05T10:00:00Z",
    "task_id": "<id>",
    "event": "test_pass" | "test_fail" | "lint" | "secret_scan" | "consensus" | "review" | "rollback",
    "agent": "PM" | "Architect" | "Implementation" | "Reviewer" | "Hermes" | "human",
    "result": "PASS" | "FAIL" | "BLOCK" | "ROLLBACK",
    "ref": "<file_path or commit_sha or doc_path>",
    "summary": "<한 줄 요약>",
    "evidence_md": "<선택, docs/evidence/<task-id>.md 경로>",
    "prev_hash": "<이전 entry hash>",
    "hash": "<현재 entry hash>"
  }
  ```
- **git diff 폭증 방지**: `.gitattributes`에서 `ledger.jsonl merge=union` 또는 `evidence/*` 별도 branch 운영

### 6.4 Schema 고정 시점

- Phase 1 종료 시 (3~4주 운영 후) schema 고정 + ADR-012 (Evidence Ledger Schema) 발행
- 그 전까지 schema 변경 자유

---

## 7. 메타포 강제 금지 조항

### 7.1 명제

> **AI 회사 메타포는 설명 도구로만 사용한다. 설계를 강제로 부풀리는 기준으로 사용하지 않는다.**

### 7.2 활용 vs 강제 경계

**메타포 활용 (권장)** — 메타포 = "기존 구조에 이름 부여":
- 권위 위계 (`Constitution > ADR > SDD > Harness > Hermes > Worker`) — 이미 존재하는 위계에 회사 메타포 매핑
- Role Contract (역할 + 출력 + 금지) — 회사 직무기술서와 동형 구조
- 3+1 합의 (A/B/C/Reviewer) — 이미 검증된 메타포 활용 사례

**메타포 강제 (비권장)** — 메타포 정합성 위해 실 구조 늘림:
- 8 Agent 컨텍스트 분기 강제
- Memory Scope 4단계 저장소 분리 (현 단계)
- "팀 회의" 시뮬레이션을 위한 Agent 간 통신 프로토콜 신설

### 7.3 미래 확장 시점

다음 조건 충족 시 메타포 추가 활용 검토:
- 파생 프로젝트 ≥ 3건 누적 → Team Memory (모델별 강점/실패 패턴) 의미 발생
- 첫 실제 프로젝트 코드 ≥ 1000줄 → QA/Security/Documentation 분리 ROI 입증
- LiteLLM 등 외부 도구로 부족한 기능 명확히 식별 → Hermes 격상 가치 입증

위 조건 미충족 상태에서 메타포 정합성을 이유로 구조를 늘리지 말 것.

---

## 8. MVP 범위 (Phase 1 시작 기준)

### 8.1 Worker Agent — 4 역할

| Agent | 역할 | 출처 |
|-------|------|------|
| **PM / Orchestrator** | 작업 분해, 우선순위, 완료 조건, 위험도 분류 | GPT 제안 + 사용자 MVP |
| **Architect** | 시스템 구조 설계, 모듈 경계, 기술 선택 검토, ADR/SDD 충돌 확인 | GPT 제안 + 사용자 MVP |
| **Implementation** | SDD + 테스트 조건에 따라 코드 구현, 변경 보고 | GPT 제안 + 사용자 MVP |
| **Reviewer** | 종합 검토, 누락 관점 확인, PASS/BLOCK/ROLLBACK/HUMAN REVIEW 판정 | GPT 제안 + 사용자 MVP |

**보류 (미래 ADR)**: QA / Security / Documentation Agent — 각각 hook/CI/secret scanner/문서 체크리스트로 일부 대체.

### 8.2 명칭 충돌 방지

| 컨텍스트 | 접두사 | 대상 |
|---------|-------|------|
| 합의 시 | `Consensus:` | A/B/C/Reviewer (일회성 분석) |
| 상시 운영 시 | `Worker:` | PM/Architect/Implementation/Reviewer (Role Contract 보유) |

### 8.3 컨텍스트 분기 비강제

> **Worker Agent는 1인 개발자 메타포의 외형이며, 컨텍스트 분기를 강제하지 않는다.**

각 Worker Agent를 별도 LLM 호출로 분기할지, 단일 컨텍스트 내 페르소나 전환으로 처리할지는 운영 판단. MVP에서는 단일 컨텍스트 내 페르소나 전환을 default로 하고, 호출 비용/혼선이 임계 초과 시 분기 검토.

### 8.4 Memory — 2단계

| Scope | 위치 | 내용 |
|-------|------|------|
| **Global** | `~/.claude/global/` | 헌법, SDD/TDD 원칙, ADR 작성 방식, 역할 정의, 검증 원칙, 금지 사항 |
| **Project** | `<project>/.claude/project/` | 프로젝트 목표, 기술 스택, 도메인 용어, 주요 결정, 반복 버그, 테스트 전략 |

**Boundary 강제**:
- 파일시스템 분리 (1차)
- 환경변수 `CLAUDE_MEMORY_SCOPE=global|project` (2차)
- Hermes memory plugin 사용 시 plugin scope 검증 항목 (G4 의존)

**Project → Global 승격**: **manual only** (자동화 금지). 패턴이 일반화될 만한지 사용자가 판단.

**메타-템플릿 복사 시 오염 방지**:
- 본 템플릿 `.gitignore`에 `.claude/project/memory.jsonl` 추가
- 복사 후 init script (`init-project.sh`) 로 Project Memory 초기화

**보류 (Phase 2+)**: Team Memory (파생 프로젝트 ≥ 3건 누적 후), Session Memory (현 `docs/sessions/`로 충족, 별도 scope 도입 시 이중 저장).

### 8.5 Evidence — Markdown + JSONL

§6.3 참조.

---

## 9. Phase 0 R-1 처리

### 9.1 R-1 검증은 재개

Hermes가 PMO로 재정의되더라도 다음을 SQLite에 저장할 수 있으므로 redaction/SQLCipher/canary 검증 의미 유지:
- 작업 분배 기록 (PMO 메타데이터)
- 합의 결과 (3+1 합의 입력·출력)
- Memory (Global / Project)
- Skill 후보 (T1 자동 추출)
- Evidence metadata (ledger.jsonl)

### 9.2 R-1 결과의 적용

- R-1 PASS → R-2~R-7 보강 후 P2 v3 작성
- R-1 FAIL → 합의 옵션 (2) C-③안 변형 자동 전환 (Hermes PMO 격상 6~12개월 완전 보류)
- 어느 경우든 **R-1 결과만으로 P2 v2 확정 X**. R-1~R-7 보강 완료 후 P2 v3 작성 여부 최종 확정.

---

## 10. 작업 우선순위 (사용자 확정)

| # | 작업 | 산출 | 시점 |
|---|------|------|------|
| 1 | 정체성 prequel 선언 작성 | 본 문서 | **즉시 (현 단계)** |
| 2 | Phase 0 R-1 검증 재개 | R-1 결과 (PASS/FAIL) | 1주 |
| 3 | 6 거버넌스 사전조건 매트릭스 작성 | `docs/architecture/governance-preconditions.md` | R-1 후 |
| 4 | Role Contract 25건 작성 | `docs/roles/AGENT_<NAME>.md` × 4 | R-1 후 (#3과 병행) |
| 5 | Memory boundary 최소 메커니즘 작성 | `docs/architecture/memory-scope-design.md` | R-1 후 (#3·#4와 병행) |
| 6 | Evidence 최소 schema 작성 | `docs/architecture/evidence-ledger-design.md` | R-1 후 (#3·#4·#5와 병행) |
| 7 | R-7 완료 후 P2 v3 신규 작성 | `docs/architecture/hermes-adoption-design-v3.md` | R-1~R-7 완료 직후 |
| 8 | ADR-008/009/010 갱신 PR 묶음 | ADR 3건 갱신 + 신규 ADR-011 (정체성) + ADR-012 (Evidence Ledger Schema, Phase 1 후) | #7과 동일 PR |
| 9 | 4 게이트 (G1~G4) 충족 검증 후 Hermes PMO 격상 활성화 | Phase 1 진입 결정 | 2~4주 후 |

---

## 11. 본 문서가 즉시 강제하는 것

본 prequel은 정식 ADR이 아니지만, 다음을 **즉시 강제**한다 (P2 v3 정식화 전이라도):

1. ADR-008·009·010·P2 v2의 가정 중 본 prequel과 충돌하는 부분은 **본 prequel 우선**
2. 새 작업 시작 시 본 §3 권위 위계 + §5 자동 학습 3-tier + §7 메타포 강제 금지 조항을 **계산적/추론적 검증 모두에서 참조**
3. Hermes 관련 새 결정(예: 신규 plugin 사용)은 §4.2 4 게이트 미충족 상태이므로 **현 ADR-008 합의 자동화 책임 외 확장 금지**
4. Phase 0 R-1 검증은 본 §9 기준으로 재개

---

## 12. 본 문서의 변경 절차

본 prequel 자체는 임시 선언이지만, 본 문서 변경은 다음 절차를 따른다:

- **단순 오타·문구 정리**: 사용자 단독 결정 가능
- **MVP 범위 변경 (§8)**: 단축 합의 (Reviewer-only) 가동
- **권위 위계 / Hermes 게이트 / 자동 학습 분류 변경 (§3·§4·§5)**: 풀 3+1 합의 가동
- **본 문서 폐기**: P2 v3 작성 완료 시 자동 (별도 합의 불필요)

---

**작성일**: 2026-05-05
**합의 출처**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 3+1 + GPT 외부 4번째 의견)
**다음 진입점**: Phase 0 R-1 검증 재개 → 6 거버넌스 사전조건 매트릭스 → Role Contract 25건
