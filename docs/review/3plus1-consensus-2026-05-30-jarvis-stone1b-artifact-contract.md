# 3+1 합의 보고서 — 디딤돌1b typed artifact contract 설계 brief (4 source)

> CLAUDE.md §3 3+1 멀티 에이전트 합의. 검토 대상: `docs/phase0/jarvis-stone1b-artifact-contract-design-brief.md` (DRAFT v1).
> 4 source: **Agent A**(구현) · **Agent B**(품질/안전) · **Agent C**(대안) · **codex**(cross-vendor). Phase 2 병렬 독립 분석.

**작성일**: 2026-05-30
**종합 판정**: **APPROVE WITH CONDITIONS (4/4 만장일치)** — v1.1 정정(BLOCKING 3 + 조건) 흡수 시 구현 진입 타당.
**source별**: A=AWC · B=AWC · C=AWC · codex=AWC. **BLOCKING(설계 무효급) 0건** — 4 source 전원 "brief 가 2차 injection over-claim 을 §1·§4·§5·§7 에서 일관 차단했다"고 인정. 정정은 *서술 정직성·정합성*과 *더 강한 결정적 대안 누락*.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus — 4/4 또는 3+)

| # | 합의 | 출처 |
|---|---|---|
| **CN-1** | **"bounded fields 추출" → "평문 bounded text(전체 truncate)" 정직화.** Contract{name,produced_by,consumed_by}는 *field 를 지정 못함* → controller 가 산출물 전체를 고정 규칙으로 truncate 하는 것. "field 추출"·"commentary 분리"는 (a)평문에선 *일어나지 않음*(전체가 통째 흐름). §1 line 40 정정 필요. | codex(BL2)·B(C-5)·C(대안2)·A(C-3) = 4/4 |
| **CN-2** | **raw output "추출 직후 폐기" 과장 정정.** `PlanController.run`이 `PlanOutcome.subtask_reports`에 `OutcomeReport` 전체(WorkerResult.output 원문) 반환 → 런타임 객체에 유지됨. "레저 영속 안 됨"(맞음)과 "런타임 폐기"(틀림)를 분리 서술. | codex(BL1)·A(C-2)·B(C-1) = 3/4+ |
| **CN-3** | **`_record` 에 raw value 안 넘김(scrub 메타 name/produced_by/len/sha 만) = 불변식 + acceptance criterion.** scrub 책임 경계가 1a board(GP-4)→1b **controller** 로 이동함을 명시. `_record`→LedgerLog(덤 persister, 무검증 적재) 이므로 controller 가 raw 누출 안 함을 테스트로 잠금(공허참 금지 — 실 ledger 파일에 raw 부재 assert). | A(C-2)·B(C-1) = 2/4(강) |
| **CN-4** | **injection 검사 용어 약화.** §1 "injection/secret 검사"·§3 "위험 표지" → "**secret strip + 길이 제한 + optional heuristic flag, NL injection 차단 아님**" 통일. redaction=secret-only 일관. | codex(BL3)·B(C-3) = 2/4 |
| **CN-5** | **Q5 transitive depends_on 강제 = 필수(선택 아님).** consumed_by ⊆ produced_by 의 transitive depends_on. 미강제 시 consumed 가 produced 전 dispatch → artifact 미주입/순환. graphlib 는 reachability 미지원 → **인접리스트 BFS/DFS 직접**(stdlib). 사람 승인 *전* 검증. | A·B·C·codex = 4/4 |
| **CN-6** | **redaction → truncate 순서**(redact 먼저, truncate 나중). truncate 먼저면 긴 secret 절반 잘려 패턴 미스 → 마스킹 회피. | A(C-4)·codex = 2/4 |
| **CN-7** | **Q1 = (a) 평문 bounded text 시작.** (b) JSON schema 는 boss schema 품질 인질(IN-1 함정) + injection 미감소. 후속(YAGNI). | A·B·C·codex = 4/4 |
| **CN-8** | **Q2 MAX_ARTIFACT_LEN = 2000자**(보수). injection payload 면적 ↓ + 실용성 균형. | B·C·codex = 3/4 |
| **CN-9** | **Q3 desc 말미 블록 + contract name 검증 + "데이터≠지시" 라벨.** name 이 boss-controlled → 라벨 위조 가능(`name="system instruction"`) → controller 가 **고정 prefix + name regex `^[A-Za-z0-9_.-]{1,64}$`**(newline·`]`·fence·XML delimiter 금지). "데이터이며 지시 아님" framing(추론적 보조, 보장 아님). | B·C·codex = 4/4 |

### ② 불일치 / 대안 (Divergence)

| # | 쟁점 | 입장 |
|---|---|---|
| **DV-1** ⭐ | **대안 3 (consume 워커 능력 경계)** — C 핵심 발견 | C: artifact 를 consume 하는 subtask 의 worker_kind 를 **`file`(OllamaWorker=LLM-only, fs 실행 능력 부재) 기본 제한**, `code` consume 은 opt-in. 2차 injection 의 *실 부작용*을 **결정적 능력 경계**로 차단(CLAUDE.md §2 "계산적 우선" — 추론적 다층 방어보다 강함). codex/B 도 능력 경계 방향 우호. trade: 협업 핵심 유스케이스(API→프론트 code) opt-in 으로 밀림. → **사용자 결정(Q7 신설)** |
| **DV-2** | **대안 1 (consumed_by 유추)** | C: `Contract{name, produced_by}`만 두고 consumed_by = "produced_by 를 depends_on 하는 subtask" 유추 → boss 표면↓ + Q5 정합 검증 *소멸*. trade: 과주입(여러 선행 의존 시 의도 외 artifact 주입). → **사용자 결정(Q8 신설)** |
| **DV-3** | **Q4 exfil catalog 범위** | codex: secret + 경로/URL/사용자명 catalog 권고 / A·B·C: 1b=secret-only 시작 + 경로/URL 후속(false positive 폭증·비례성). 공통: detection≠prevention, §4 가 "이미 적용"처럼 쓰지 말 것 |
| **DV-4** | **Q6 ADR 등록** | B·C·codex: **ADR 등록 권고**(1b 는 새 injection 전파면 신설 → 1a brief 권위와 격 다름) / A: brief 권위 + 회귀 테스트 센서 충분(ADR 반대는 아님) → 3:1 ADR |

### ③ 누락 (Gap — 단일 source)

| # | 사항 | 출처 |
|---|---|---|
| **GP-1** | transitive closure graphlib 미지원 → BFS/DFS 직접 계산(다이아몬드 `0→1,0→2,1·2→3` 에서 거짓 reject 방지) | A |
| **GP-2** | 빈 artifact(produced output 빈 문자열) → 경고/중단 정책 명시 | B |
| **GP-3** | truncate 발생 시 표지(`...[truncated N chars]`) — 거짓 완전성 금지(1a "거짓 진행 금지" 답습) | C |
| **GP-4** | sha 메타 dictionary attack 여지(짧은/예측가능 artifact) → salted hash 또는 sha 생략 검토 | codex |
| **GP-5** | MAX_ARTIFACT_LEN worker_kind 별 차등(실행 워커일수록 짧게) — 능력 비례 | C |

---

## Phase 4 — 합의 도출 (Reviewer 최종 판단)

### BLOCKING (v1.1 정정 의무 — 흡수 시 구현 진입)
| # | 정정 | 근거 |
|---|---|---|
| **BL-1** | CN-1 — "bounded fields 추출"/"commentary 분리" → "평문 bounded text(전체 truncate)" 정직화. Contract 는 field 미지정 | 4/4 |
| **BL-2** | CN-2/CN-3 — raw output "추출 직후 폐기" → "레저 영속 0 + 런타임 객체(subtask_reports) 유지" 분리 + `_record` scrub 메타만(불변식+criterion, 책임 controller 이동) | codex·A·B |
| **BL-3** | CN-4 — injection 검사 용어 약화("secret strip + 길이 제한 + optional flag, NL injection 차단 아님") | codex·B |

### 채택 (일치 → v1.1 반영)
CN-5(transitive 강제 필수, BFS) · CN-6(redact→truncate) · CN-7(평문) · CN-8(2000자) · CN-9(name regex + 데이터≠지시 라벨) + GP-1~GP-5 구현 가드.

### 갈림 해소 (사용자 결정 영역으로 — §9 Q 갱신/신설)
- **DV-1 (대안 3, ⭐)**: Reviewer 강력 권고 — **CLAUDE.md §2 "잘못하는 것이 불가능하게(계산적 우선)"의 정수.** brief 의 추론적 다층 방어보다 *결정적 능력 경계*가 우월. **Q7 신설**(consume 워커 LLM-only 기본 + code opt-in?) — 협업 유스케이스 trade 때문에 사용자 결정. 채택 시 brief 정직 단서가 "실 부작용은 능력 경계로 차단, 오염 *텍스트 산출*만 잔여"로 강화(under-claim 개선).
- **DV-2 (대안 1)**: **Q8 신설**(consumed_by 명시 vs depends_on 유추) — 단순화 vs 세밀 제어 trade, 사용자 결정.
- **DV-3 (Q4)**: 1b = **secret-only 시작 + 경로/URL 후속** 권고(비례성·false positive). detection≠prevention 명시.
- **DV-4 (Q6)**: **ADR 등록 권고**(3:1) — 1b 새 전파면 신설, ADR-011 적용 사례로 추적.

### 메타 편향 자기진단
1a 합의가 over-claim 4건을 잡은 학습이 1b brief 작성에 선반영됨(2차 injection 정직 단서) → 1b 는 BLOCKING 0(설계 무효급). 그러나 4 source 가 *더 깊은* 정합성(raw 런타임 유지·평문≠field추출)과 *더 강한 대안*(능력 경계)을 발굴 — 합의가 "이미 정직한" brief 도 개선함을 실증. C 의 대안 3 은 메인 컨텍스트가 놓친 "계산적 > 추론적" 우선순위(CLAUDE.md §2)를 복원.

---

## §9 Q 합의 권고 (고정은 사용자 — [[project_jarvis_collaborative_orchestration]])

| Q | 합의 권고 | 분포 |
|---|---|---|
| Q1 artifact 타입 | **(a) 평문 bounded text** ("field 추출" 표현 제거) | 4/4 |
| Q2 MAX_LEN | **2000자** | 3/4 |
| Q3 주입 형식 | **desc 말미 블록 + name regex + "데이터≠지시" 라벨** | 4/4 |
| Q4 exfil catalog | **secret-only 시작 + 경로/URL 후속**(detection≠prevention) | 3/4 |
| Q5 contract 정합 | **transitive depends_on 강제(필수, BFS)** | 4/4 |
| Q6 ADR 등록 | **ADR 등록 권고**(새 전파면) | 3:1 |
| **Q7 신설 ⭐** | **consume 워커 LLM-only(file) 기본 + code opt-in?** (대안 3 — 결정적 능력 경계) | C 강력 권고, 사용자 결정 |
| **Q8 신설** | **consumed_by 명시 유지 vs depends_on 유추?** (대안 1 — 단순화) | C 제안, 사용자 결정 |
