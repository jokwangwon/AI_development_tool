# 풀 3+1 합의 보고서: 시스템 정체성 재정의 + Hermes 역할 재정의

**날짜**: 2026-05-05
**검증 대상**: GPT 외부 검토 결과 (12개 항목) + 사용자 선호 결론 (MVP만 부분 채택)
**상위 결정**: ADR-008 (Hermes 도입 Option B), 6 차단조건 비협상
**관련 합의**: `3plus1-consensus-2026-05-04-hermes.md`, `3plus1-consensus-2026-05-04-p1-llm-providers.md`, `3plus1-consensus-2026-05-04-p2-hermes-adoption.md`, `3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`
**합의 형태**: **풀 3+1 (병렬 3 Agent + Reviewer + GPT 외부 4번째 의견)**

---

## 사전 점검

**Liquidity 영향**: 본 안건은 Provider Liquidity (헌법 5조 비협상 영구기억) 에 직접 충돌 가능. GPT 풀스펙 (8 Agent + 4단계 Memory + Evidence DB) 은 Worker 모델 응답 패턴 fossilize 위험. Hermes를 PMO+Memory+Skill 관리자로 격상시키는 순간 Hermes 자체가 새 lock-in 후보. **어떤 채택안이든 "메모리/Skill 저장 형식은 Provider-agnostic" + "Hermes ≠ root of trust"가 동시 강제되어야 함**.

**헌법 정합성**: 헌법 6조(외부 SDK 우선)는 Hermes를 "후보 중 하나"로 평가하라고 명령. ADR-008은 사용자 의지로 Option B(Hermes) 선택. Phase 0 R-1 미완 + redaction default OFF + plugin 가정 흔들림 상태에서 PMO/Memory/Skill 격상은 단일 도구 의존 면적의 정당성 미증명 확장.

**합의 가동 정당성**: 3가지 큰 결정 묶음 (정체성 재정의 + ADR-008 의지 부분 수정 + P2 문서 처리). CLAUDE.md §3 기준 풀 3+1 필수. GPT 외부 4번째 의견은 메타-편향 보정 목적으로 적절 포함.

---

## Phase 2 — 3 Agent + GPT 독립 분석 요약

### Agent A (구현/복잡도) — 결론: MVP만 부분 채택 + Phase 0 이후 재검토
- GPT 풀스펙 26~37일 + 14~22h/월 유지 vs 사용자 MVP 8~12일 — 1인 메타-템플릿 환경에서 50~80% 문서 폭증
- P2 v3 신규 작성 권고 (변경 폭 600~900줄 vs 1.5k~2k줄, 비용 차이 작음)
- 4 Agent 최소 안정선, Memory 2단계 충분, Evidence는 Markdown + JSONL 둘 다
- 단독 위험 5건 (R-A1~R-A5): plugin lock-in, Agent 명칭 충돌, R-1 적용 지점 재확인, JSONL git diff 폭증, 메타-템플릿 복사 시 Memory 오염

### Agent B (안전/거버넌스) — 결론: MVP만 부분 채택 + 6 거버넌스 사전조건 강제
- Hermes PMO 격상 시 헌법 8조·5조 위반 경로 8건 (P1~P8)
- 권위 위계 강제 매트릭스: Hermes 금지 8가지 × {계산적/추론적/자동 롤백}, 8 중 7 계산적 가능
- 자동 학습 3-tier: T1 (자동 OK) / T2 (사용자 승인) / T3 (절대 금지). 새 검증 단계 추가/제거는 T2
- Role Contract 25건 금지 행동 (PM 5 + Architect 5 + Implementation 5 + Reviewer 5 + 공통 5)
- 단독 위험 6건: 합의 인프라 순환 권위 역설, Phase 0 미완 + 비전 확정, Memory 2단계 leak, 운영 구현 부재, Evidence 변조 방지, R-7 시점 충돌

### Agent C (대안/제품성) — 결론: MVP만 부분 채택 + Hermes 도입 조건부 보류
- 부분 채택 라인업 4개: ① 정체성+위계만 / ② ① + 2 Agent (Impl+Reviewer) [C 권장] / ③ Role Contract만 / ④ 사용자 MVP 그대로
- 4 Agent도 1인에게 과도, 2~3 Agent 시작 가능
- Hermes 도입 6~12개월 보류 시나리오 진지 검토 + 정량 트리거 4건 (2건+ 충족 시 재평가)
- 메타포 활용 (이름 부여) vs 강제 (실 구조 늘림) 분리, **메타포 강제 금지** 조항 권고
- 단독 위험 6건: Phase 0 동시 진행, 메타포 인플레이션, 의지 vs ROI 충돌, SPOF, P2 v3 동반 갱신 비용, GPT 외부 메타-편향

### GPT (외부 4번째 의견) — 풀스펙 제안
1. 정체성 "AI Development Company OS"
2. Hermes 역할: PMO + 기억/Skill/합의 실행기 (root of trust 아님)
3. 8 Worker Agent
4. Role Contract (역할 + 출력 + 금지)
5. Memory Scope 4단계
6. 자동 학습 OK / 자동 정책 변경 금지
7. "Agent proposes / Tools verify / Evidence decides / Human overrides"
8. 권위 위계 `Constitution > ADR > SDD > Harness > Hermes > Worker`
9. Hermes 금지 8가지

---

## Phase 3 — 교차 비교

### 일치 (4자 또는 3자 동의)

1. **AI Development Company OS 정체성 방향성 자체는 수용** — 4자 동의 (단 채택 범위·시점에서 갈림)
2. **"Hermes ≠ root of trust" 명문화** — 4자 동의
3. **권위 위계 도입** (`Constitution > ADR > SDD > Harness > Hermes > Worker`) — 4자 동의
4. **자동 학습 ≠ 자동 정책 변경** — 4자 동의 (B가 T1/T2/T3로 정밀화)
5. **MVP만 부분 채택 결론 자체** — 3 Agent 명시 + GPT 침묵 = 합의
6. **Evidence Ledger 변조 방지/감사 가능성** — 3자 동의

### 부분 일치 (2~3자 동의)

1. **MVP Agent 수**: A·B = 4 / C = 2~3 / GPT = 8 → **4 채택, 단 "Worker Agent는 1인 개발자 메타포의 외형이며 컨텍스트 분기 강제 아님" 명문화** (C 우려 흡수)
2. **Memory 단계**: A·B·C = 2 / GPT = 4 → **2 채택, Team/Session은 미래 ADR**
3. **P2 처리**: A·B = v3 신설 / C = 비용 경고 / GPT 침묵 → **P2 v3 신규 작성**, 단 ADR-008/009/010 동시 갱신을 동일 PR로 묶음 (C 비용 분산)
4. **Hermes 도입 시점**: GPT 즉시 / A·B 중간 / C 보류 → **Phase 0 R-1 + 6 거버넌스 사전조건 충족 후 격상**
5. **Role Contract 강제 수준**: GPT·A·B 동의 / C 인플레이션 경계 → **B의 25건 채택 + C의 메타포 강제 금지 조항 동시 명문화**

### 불일치 (모두 다른 의견)

1. **현 P2 v2의 거취**: A(부분 무효 → v3 대체) vs B(R-7 후 v3 시점 잠금, 그동안 v2 유지) vs C(Hermes 보류 시 v2/v3 무의미) vs GPT(미언급) → **A의 결론 + B의 시점 잠금 결합. C 보류 시나리오는 v3 작성 시점 재평가 트리거로 흡수**
2. **자동 학습 "검증 단계 추가/제거" 분류**: B만 T2 명시, A·C는 침묵 → **B의 T1/T2/T3 채택, "제거 자동화 비대칭 위험" 강조**
3. **Worker Agent 명칭 충돌 처리**: A 단독 발견 → **흡수**

### 누락 (단독 발견 → 합의안 흡수)

| Agent | 단독 발견 | 흡수 결정 |
|-------|---------|---------|
| A | R-A1 plugin lock-in | ✅ 흡수 (B-P5/P7과 보강) |
| A | R-A2 Agent 명칭 충돌 | ✅ 흡수 ("Worker:" / "Consensus:" 접두사) |
| A | R-A3 R-1 적용 지점 재확인 | ✅ 흡수 (v3 명시) |
| A | R-A4 JSONL git diff 폭증 | ✅ 흡수 (`merge=union` + 별도 branch) |
| A | R-A5 메타-템플릿 복사 시 Memory 오염 | ✅ 흡수 (`.gitignore` + init script) |
| B | 합의 인프라 순환 권위 역설 | ✅ **핵심 흡수** (Reviewer 결과 git commit + UI 직접 전달) |
| B | Phase 0 미완 + 비전 확정 위험 | ✅ 흡수 (선언과 구현 분리) |
| B | Memory 2단계 leak (manual promotion) | ✅ 흡수 |
| B | "Hermes ≠ root of trust" 운영 구현 부재 | ✅ 흡수 (v3 별도 섹션) |
| B | Evidence 변조 방지 | ✅ 흡수 (hash chain or git append commit) |
| B | R-7 시점 충돌 | ✅ 흡수 (v3 시점 잠금) |
| C | Phase 0 동시 진행 위험 | ✅ 흡수 |
| C | 메타포 인플레이션 | ✅ **핵심 흡수** ("메타포 강제 금지" 조항 신설) |
| C | 사용자 의지 vs ROI 충돌 | ✅ 흡수 (의지 존중 + 미증명 단계 보류) |
| C | 외부 도구 우회 안티패턴 (SPOF) | ✅ 흡수 (Hermes 4 역할 동시 부여 거부) |
| C | P2 v3 동반 갱신 비용 | ✅ 흡수 (PR 묶음) |
| C | GPT 외부 의견 메타-편향 | ✅ 메타 점검에 반영 (GPT 가중치 절대화 X) |
| GPT | 8 Worker Agent | ❌ 불채택 (메타포 인플레이션 + 거버넌스 폭증) |
| GPT | Memory 4단계 | ❌ 불채택 (2단계로 시작) |
| GPT | Skill 자동 추출 자동성 | ⚠️ 부분 채택 (T1 한정) |

---

## Phase 4 — 최종 합의

### 합의 결론 (한 문장)

**MVP만 부분 채택 + Phase 0(R-1) 완료 및 6 거버넌스 사전조건 충족 후 Hermes PMO 격상 활성화** — 사용자 선호와 일치하되, A·B·C의 단독 위험 17건과 GPT 풀스펙의 핵심 원칙 4건(권위 위계, Hermes ≠ root of trust, 자동 학습 ≠ 자동 정책 변경, "Agent proposes / Tools verify / Evidence decides / Human overrides")을 동반 흡수.

### 4가지 판단에 대한 구체 권고

#### 1. 정체성 재정의 — **채택 (선언적 수준만, 즉시)**

- "AI Development Company OS" 메타포는 P2 v3 §1에 선언
- 메타포 = "기존 구조에 이름 부여" (C 정의)
- 사용자 = 창업자, Hermes = PMO, Worker Agent = 사원, Constitution/ADR = 회사 규칙
- **메타포 강제 금지 조항 동시 명문화**: "메타포 정합성을 위해 실제 Agent/Memory/Skill 구조를 늘려서는 안 된다"
- 시점: 즉시 채택 가능 (비전 선언과 구현 분리)

#### 2. Hermes 역할 재정의 — **Phase 0 완료 + 6 거버넌스 사전조건 충족 후 (조건부 활성화)**

- 즉시 채택 거부, 완전 보류(C-③안)도 거부 — 타협안
- **타협안 게이트 (전부 충족 시 PMO 격상 활성화)**:
  - **G1**: Phase 0 R-1 (canary 검증) 완료 및 hook 기반 redaction 동작 확인
  - **G2**: B의 6 거버넌스 사전조건 충족 (8 위반 경로 P1~P8 강제 메커니즘 매핑)
  - **G3**: "Hermes ≠ root of trust" 운영 구현 (read-only on Constitution/ADR/SDD, 합의 결과 git commit 강제, user-facing UI 직접 전달)
  - **G4**: Provider-agnostic Memory/Skill 저장 형식 확정 (Hermes plugin lock-in 회피)
- 그 사이 Hermes는 현 ADR-008 합의 자동화 책임만 유지

#### 3. P2 v2 Amendment vs P2 v3 — **P2 v3 신규 작성 (R-7 완료 후 시점 잠금)**

- 근거: A의 분석 (§2.1.3 부재 확정으로 v2 30% 미만 유효, Amendment는 권위 위계 부재를 패치로 무마)
- **시점 잠금**: P2 v3 작성은 R-1~R-7 보강 완료 후
- **동반 갱신 묶음**: P2 v3 작성 PR에 ADR-008/009/010 갱신 동시 묶음 (C 비용 분산)
- v3 §1: 권위 위계 / §2: "Hermes ≠ root of trust" / §3: 자동 학습 3-tier / §4: 메타포 강제 금지

#### 4. MVP 범위

**Agent 수: 4** (PM/Orchestrator + Architect + Implementation + Reviewer)
- C의 2~3안 거부, 우려 흡수: "Worker Agent는 1인 개발자 메타포의 외형이며 컨텍스트 분기 강제 아님" 명시
- A의 R-A2: 합의 시 "Worker:" / "Consensus:" 접두사로 명칭 충돌 방지
- B의 25건 Role Contract 채택 (역할 + 출력 + 금지 5건/Agent)

**Memory 단계: 2** (Global + Project)
- 파일시스템 분리: `~/.claude/global/` vs `<project>/.claude/project/`
- 환경변수: `CLAUDE_MEMORY_SCOPE`
- **Project → Global 승격 manual only** (B 흡수)
- Team/Session은 미래 ADR (3건+ 파생 프로젝트 누적 시 재평가)
- `.gitignore` + init script 의무화 (A-R-A5)

**Evidence 형식: Markdown + JSONL 둘 다**
- 사람 검토 = Markdown task별 1파일, 자동화 = JSONL append-only
- **JSONL hash chain or git append commit으로 변조 방지** (B-단독 5)
- JSONL git diff 폭증 방지: `merge=union` + 별도 branch (A-R-A4)
- Schema: `ts/task_id/event/agent/result/ref/summary/evidence_md`

### 필수 보강 항목

- **B의 25건 Role Contract 전건 채택** (PM 5 + Architect 5 + Implementation 5 + Reviewer 5 + 공통 5)
- **B의 6 거버넌스 사전조건 전건 채택** (Hermes 격상 게이트 G2 구성)
- **A의 5 단독 위험 전건 흡수** (R-A1~R-A5)
- **C의 6 단독 위험 중 5건 흡수** (Phase 0 동시 진행, 메타포 인플레이션, 의지 vs ROI, SPOF, P2 v3 동반 갱신). GPT 외부 의견 메타-편향은 본 메타 점검에 반영
- **자동 학습 3-tier 명문화** (T1/T2/T3, "제거 자동화 비대칭 위험" 명시)
- **합의 인프라 순환 권위 해결**: Reviewer 결과 Hermes 우회 git commit + user-facing UI 직접 전달

### 사용자 결정 옵션

#### (1) Reviewer 권고 채택 [권장]
- MVP만 부분 채택 + Hermes 격상 4 게이트(G1~G4) + P2 v3 R-7 후 시점 잠금
- 즉시 작업: 정체성 메타포 선언 (가벼움), Role Contract 25건 작성, Phase 0 R-1 진행
- 장점: 사용자 선호 + 3 Agent 합의 + GPT 핵심 원칙 동시 충족
- 단점: 게이트 4건 충족까지 시간 소요 (예상 2~4주)

#### (2) 대안 1: C-③안 변형 (Hermes PMO 격상 6~12개월 완전 보류)
- 정체성·권위 위계·Role Contract·Memory 2단계·Evidence 즉시 도입
- Hermes는 현 ADR-008 합의 자동화만 유지. PMO/Memory/Skill 격상은 정량 트리거 4건 중 2+ 충족 시 재평가 ADR
- 장점: 헌법 6조 외부 SDK 우선 + LiteLLM 등 대안 비교 시간 확보
- 단점: 사용자 ADR-008 의지와 거리. Hermes 가치 입증 지연
- **자동 적용 조건**: Phase 0 R-1에서 Hermes hook 가정이 추가로 무너지면 자동 전환

#### (3) 대안 2: GPT 풀스펙 단계적 도입 (8 Agent + Memory 4단계 + Evidence DB)
- 6~12개월에 걸쳐 4→6→8 Agent / 2→3→4 Memory 단계 확장
- 장점: GPT 원안 정합성 최대
- 단점: A의 26~37일 + 14~22h/월 유지비, C의 메타포 인플레이션, B의 8 위반 경로 모두 8 Agent×4 단계로 폭증
- **Reviewer 비권장**

---

## 메타 편향 자기진단 (Reviewer)

본 평가에서 의식적으로 통제한 편향은 세 갈래:

1. **A·B·C 모두 Claude이므로 텍스트 친화적·문서 친화적 결론 동조 위험** — P2 v3 신규 작성 결정은 "1.5k~2k줄 신규 문서 작성"이라는 Claude 친화 작업. 자기 점검 결과: A의 정량 근거 + C의 동반 갱신 비용 PR 분산 보강이 가능하므로 채택 정당. 단 Phase 0 R-1에서 hook 가정 추가 흔들림 시 v3 작성 재검토 단서 명시.

2. **사용자 선호 결론 동조 편향 위험** — 3 Agent 모두 독립적으로 MVP만 부분 채택 권고 (GPT 즉시 거부 안 함). B는 거버넌스 사전조건 6건, C는 정량 트리거 4건이라는 정량적 보강 제시 → 단순 사용자 동조 아닌 다관점 수렴 확인. C의 보수 의견(6~12개월 보류)을 down-weight 하지 않고 대안 1로 별도 옵션화하여 사용자 선택지 보존.

3. **GPT 외부 의견 가중치 vs 메타-편향 충돌** — GPT 8개 핵심 원칙(권위 위계, root of trust 부정, 자동 학습 분리, 검증 원칙)은 4자 합의로 채택, GPT 풀스펙(8 Agent + 4 Memory)은 3 Agent 명시 거부에 따라 불채택. **GPT 의견을 "원칙은 강하게, 양적 풀스펙은 약하게" 비대칭 가중치 적용**해 메타-편향 양면 동시 통제.

---

## 다음 단계 (옵션 (1) 채택 시)

| 단계 | 작업 | 시점 |
|------|------|------|
| 1 | 정체성 메타포 + 권위 위계 + 메타포 강제 금지 조항 선언 (P2 v2 짧은 prequel 또는 ADR-011 Pre) | 즉시 |
| 2 | Phase 0 Day 2~5 진행 (R-1 + 단축 합의 7건 R-1~R-7 보강) | 1~2주 |
| 3 | 6 거버넌스 사전조건 매트릭스 작성 (B-P1~P8 강제 메커니즘) | R-7과 병행 |
| 4 | Role Contract 25건 작성 (`docs/roles/AGENT_<NAME>.md`) | R-7과 병행 |
| 5 | Memory boundary 메커니즘 (파일시스템 + 환경변수) 설계 | R-7과 병행 |
| 6 | Evidence Ledger 최소 schema (Markdown + JSONL) 설계 | R-7과 병행 |
| 7 | P2 v3 신규 작성 (R-7 완료 후 시점 잠금) + ADR-008/009/010 갱신 PR 묶음 | R-7 완료 직후 |
| 8 | 4 게이트(G1~G4) 충족 검증 후 Hermes PMO 격상 활성화 | 2~4주 후 |

---

**합의 완료 시각**: 2026-05-05
**Reviewer 평가 정합성**: HIGH (메타 편향 통제 명시 + 3 Agent + GPT 4자 입장 모두 흡수 + 단독 위험 17건 처리 + 정량 게이트 4건 명시)
**다음 진입점**: 사용자 결정 (옵션 1/2/3) → 권고 채택 시 정체성 + 권위 위계 선언 즉시 진행
