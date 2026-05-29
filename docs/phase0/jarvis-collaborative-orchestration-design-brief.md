# Jarvis 협업 오케스트레이션 설계 brief — plan-then-execute + contract-first (디딤돌0→L3) (DRAFT v2)

> **본 brief = 설계 정리 한정.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 설치·모델 다운로드·격리/sandbox 구현·게이트 신설·레저 영속화** 를 발생시키지 않는다. 본 brief = *토의 + 3+1 합의 결과의 SDD 정리* — 실 변경 0건. staged: brief v1 → 3+1 합의(REVISE) → **brief v2(본 문서)** → 사용자 승인 → **디딤돌0 TDD 구현**. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-29
**Status**: **DRAFT v2 — 3+1 합의 REVISE 흡수(BLOCKING 6 + 권고 6) + 사용자 결정 반영(plan-then-execute 전환 + 디딤돌0 분리). 사용자 승인 → 디딤돌0 구현 대기**
**진입 단위**: jarvis 본체 확장 — 단발 단일 워커 → 협업 오케스트레이션(워커 간 계약 고정까지). 통제+히스토리 토대 분리 선행.
**근거**: `project_jarvis_local_boss_direction` · `project_jarvis_controlled_child_then_friday` (jarvis 확장 — 사용자 2026-05-29) · `feedback_provider_liquidity` (헌법 5조) · `feedback_proportionate_security_personal_tool` (비례성) · `feedback_pass_scope_overclaim` (over-claim 차단) · ADR-011 (수단/목적 분리) · CLAUDE.md §2 (Agent=Model+Harness) · Claude Code subagent 안전경계 참고조사 · [[3plus1-consensus-2026-05-29-jarvis-collaborative-orchestration]] (REVISE) · 기존 코드 `src/jarvis/{orchestrator,boss,worker,approval,memory}.py` + `jarvis_hud/jarvis_tasks.py`

---

## v2 변경 이력 (3+1 합의 REVISE 흡수)

| # | v1 → v2 | 출처 |
|---|---------|------|
| 🔴 B1 | §3 **RT-1 redaction = injection 방어 서술 삭제** — RedactionFilter 는 secret 값·key 마스킹 한정(redaction.py:52-60), NL injection payload 통과. injection 방어는 *제어 모델 구조(루프 부재)* + 능력 경계가 책임 | A,B,C,codex 4/4 |
| 🔴 B2 | §4 **"결정적 매핑" 정직화** — boss schema 가 worker_kind enum 출력(ends) → harness 가 enum→argv 결정적 룩업(means). "워커 종류 선택 주체=boss" 인정 | A,codex,B |
| 🔴 B3 | §1 **제어 모델 = plan-then-execute** — boss 계획 1회(untrusted proposal) → 사람 1회 승인 → 결정적 controller. 워커출력→boss 제어 루프 *제거* | C,codex,A,B + 사용자 결정 |
| 🔴 B4 | §6 **산출물 전달 = typed artifact contract** — raw NL 전달 금지, NL=untrusted commentary 분리 | codex,B,C |
| 🔴 B5 | §5 **scrub 모순 해소** — raw 전달 vs scrub 영속의 권위·생명주기·injection 검사 시점 명문화 | B |
| 🔴 B6 | §5 **MemoryLog 재사용 불가 → LedgerLog 분리**(event-sourcing) | A |
| R1~R6 | §4 R2 정직 서술 / §3 exfil 위험 / ADR-011 (a)~(d) 보강 / boss 호출 비용·GPU 점유 / 단계화 디딤돌0 분리 / 통제 형태전환 명문화 | B,A,C |

---

## §0 배경 — 왜 이 brief 인가

사용자 두 질문(2026-05-29): (1) **상생 협업** — 회사처럼 업무 분담 + 백엔드↔프론트 인터페이스 조율, (2) **전체 맥락 이해** — 각 워커가 전체 흐름을 알고 작업.

**코드 실측 = 둘 다 현재 0.** 현 `Orchestrator.dispatch(prompt 1개, alias 1개)` = 단발 단일 워커(orchestrator.py:120-156). 워커는 `mkdtemp` 개별 디렉터리 독립 실행(격리=고립), 워커 간 통신 0, 공유 맥락 0. `Boss`=사후 advisory 만(boss.py R2: 텍스트 전용, 제어권 0).

→ 두 질문 = 빠진 "협업 오케스트레이션 레이어". **히스토리(영속 레저)=공유 맥락 저장소**이므로 통제+히스토리가 1층 공사.

## §1 핵심 결정 — 제어 모델 = plan-then-execute (v2 재정의)

### D-1. boss 는 **계획 1회 제안**, 제어는 **결정적 controller** (3+1 합의 + 사용자 결정)

v1 의 "boss 직접 제어"는 3+1 합의에서 **약한 로컬 boss + 안전망 부재 환경에 부적합**으로 판정(C·codex 독립 수렴). 채택 모델:

```
boss (untrusted planner):  작업그래프(목적/의존성) + 워커 간 인터페이스 계약을
                           schema 로 *1회* 제안.  ← proposal 일 뿐, 권위 0
                                  │
사람 게이트:                계획·계약 전체를 *1회* 승인  (게이트=계획 1회, 피로 최소)
                                  │
결정적 controller:          schema validation + capability allowlist + dependency
                           validation + budget/step limit + worker mapping table 적용
                           → 의존성 해소·재시도·중단·산출물 전달 수행
                           ← 중간 boss 호출 0, 워커 간 직접 통신 0
                                  │
boss advisory (격리):       워커 출력 검토는 *사람용 advisory*(현 _advise 패턴)로만.
                           제어 결정에 환류 0 (control loop 재진입 경로 부재)
```

**이 단일 결정이 4대 위험을 동시에 닫는다**: D-3(제어루프 injection)은 *루프가 없어 발생하지 않음* / 게이트 피로는 계획 1회로 축소 / 산출물 전달은 typed contract(§6) / R2 불변식은 boss 가 제어루프 밖이라 **글자 그대로 연장**. v1 이 "직접제어를 유지하며 §3~§6 다층 방어로 위험을 메우려던" 구조보다, **위험을 애초에 발생시키지 않는다**(CLAUDE.md §2 "잘못하는 것이 불가능하게 만들어라").

### D-2. boss = jarvis(로컬 LLM), **Claude 아님**

본 시스템 boss = jarvis(ollama 등, 교체 가능, 헌법 5조). 개발에 쓰는 Claude 는 jarvis 를 *만드는 도구*일 뿐. **핵심**: jarvis boss 는 frontier 보다 약하고 Anthropic 서버사이드 injection 프로브가 없다. 사용자가 참고한 직접제어 하네스(Claude Code 등)는 *frontier boss*라 안전하나, **약한 로컬 boss 에 같은 직접제어를 적용하면 위험** — 이것이 D-1 전환의 근본 이유.

### D-3. injection 안전은 boss 의 똑똑함이 아니라 **구조(루프 부재) + harness 경계**가 책임

plan-then-execute 로 제어루프가 없으므로 "워커출력→boss→제어결정" injection 재진입 경로가 부재. 남는 표면(계획 입력·산출물 전달)은 §3·§6 의 구조적 경계로 닫는다. **RT-1 redaction 은 injection 방어가 아님**(secret-only) — 이 역할을 redaction 에 귀속하지 않는다(B1).

## §2 단계 경로 — 디딤돌0 → 디딤돌1(L2+L3 압축) (v2 재구성)

3+1 합의(C)대로 L1 을 쪼개 **협업 무관 통제·히스토리를 먼저 독립 출하**:

| 단계 | 능력 | 협업 | 규모 | 비고 |
|---|---|---|---|---|
| **디딤돌0** | 영속 레저(LedgerLog) + 공유 맥락 read + 취소 + 고아 `interrupted` 마킹 | 0 | 중간 | **첫 구현. 즉시 가치(재시작 유실 해소), 위험 최소. 기존 dispatch 보존 + 주변 확장** |
| **디딤돌1** | boss 계획 1회 + 사람 승인 + 결정적 controller + **contract-first 계약 고정** | L2 분해 + L3 계약 | 큰 | plan-then-execute 로 L2·L3 압축. contract-first 라 워커 간 통신 0 |
| (범위 밖) | 자율 재계획·동적 재분배 | L4 | — | 프라이데이 영역(`project_friday_separate_evolution_direction`) |

**L3 "협상" → "계약 고정"(contract-first)**: boss 가 인터페이스 계약(API schema 등)을 명시 산출물로 *먼저 고정* → 백엔드/프론트 워커 *양쪽 입력*으로 결정적 주입. 워커 간 직접 통신 0. OpenAPI 우선설계와 동형 — "협상"보다 안정적, injection 표면 대폭 축소.

## §3 안전 경계 (v2 — RT-1 격하, 구조 우선)

| # | 경계 | jarvis 현황 | 역할 |
|---|---|---|---|
| 1 | **제어루프 부재(D-1 plan-then-execute)** | 신규 | **injection 제어흐름 장악의 1차 방어 — 루프가 없어 재진입 불가** |
| 2 | 도구 화이트리스트 | ✅ WorkerRegistry, OllamaWorker(fs 경로부재), CliWorker(argv 고정) | boss 가 워커를 발명 불가, enum→argv 결정적 룩업(§4) |
| 3 | OS sandbox | ✅ LandlockIsolation, mkdtemp (v4 Landlock 단독충분 실증) | 공간 fs 격리. **단 데이터흐름은 못 막음 → §6 typed contract 가 보완** |
| 4 | permission 게이트 | ✅ ApprovalGate (반영 전) | 계획 승인 게이트로 위치 이동(D-1) |
| 5 | RT-1 redaction | ✅ RedactionFilter | **secret exfil 축소 보조에 한정 — injection payload(NL) 미차단(B1 명시)** |

### exfil 위험 (R2 신규)
워커가 RO 경로(LandlockIsolation DEFAULT_RO_PATHS `/etc` 등, isolation.py:66-73)의 **비-secret 민감데이터**(내부 URL/경로/사용자명)를 응답으로 빼낼 수 있고, scrub(secret-only) 통과 → 레저 영속·advisory 환류로 전파. **대응**: 협업 시 `ro_paths` 를 명시적 *축소* 주입(isolation.py:75-83 인자 활용), 프로젝트 비밀이 RO/RW 경로에 노출되지 않음을 결정적 보장. 영속 전 exfil 검사(secret 외 민감 경로/URL).

## §4 boss 역할 — untrusted planner + means/ends (v2 정직화)

boss 는 **목적(ends)** 만 제안, **수단(means)** 은 harness 가 결정. 단 v1 의 "subtask→워커 결정적 매핑"은 부정확했으므로(B2) 정밀화:

```
boss schema (untrusted proposal):
  {subtasks: [{desc: "백엔드 REST API", worker_kind: "code", depends_on: []},
              {desc: "그 계약으로 프론트 폼", worker_kind: "code", depends_on: [0]}],
   contracts: [{name: "api_schema", produced_by: 0, consumed_by: [1]}]}
  ← worker_kind = 허용 enum(code|shell|file). argv·경로·명령 필드 schema 에 *부재*
        │
harness controller (deterministic):
  - schema validation (ollama `/api/chat` body 에 "format":<JSON schema> grammar 강제,
    최상위 object wrapping. 문법 준수 ≠ 의미 타당 → DAG 인덱스/사이클 결정적 검증 + 재시도 1회)
  - worker mapping = worker_kind enum → worker_alias *table* 룩업 (NL inference 아님)
  - capability allowlist + dependency validation + budget/step limit
```

**means/ends 경계 정밀화(B2)**: "워커 *종류 선택*(worker_kind)"은 ends 에 가까워 boss 의 *제약된 enum 선택*이고, "argv·경로·격리 backend"는 means 로 harness table 룩업. 자연어 subtask→워커를 "결정적"이라 부르지 않는다.

### R2 불변식 — 정직 서술 (R1)
원 R2 안전 = (i) 필드부재 + (ii) 사후위치(제어권 0). plan-then-execute 에서 **boss 는 제어루프 밖**이므로 (ii) 사후위치가 *유지된다*(boss output 이 제어결정에 환류 0). (i) 은 schema(수단 필드 부재)로 보존. → v1 처럼 "(ii) 폐기 후 정신 연장" over-claim 이 아니라, **plan-then-execute 덕에 R2 두 축 모두 글자 그대로 연장**. (이것이 직접제어 대비 plan-then-execute 의 핵심 이점.)

### ADR-011 인용 (R3)
means/ends 틀 차용. ADR-011 §2.1 의 (a)~(d) 4조건/검증 의무 답습 — "본 schema 가 원 R2 안전 결과를 동등 이상 보존함"을 디딤돌1 진입 전 (a)~(d) 패턴으로 실증(§8). means/ends 원맥락(redaction 수단 대체)과 본 역할분담 적용은 구분.

## §5 통제 + 히스토리 = 디딤돌0 (v2 — LedgerLog 분리, scrub 모순 해소)

### 영속 레저 = LedgerLog (B6)
- 현 `JarvisTaskBoard._cards` = in-memory, 재시작 = 전유실 + 고아(R-7).
- **`MemoryLog`(memory.py, read-only 관찰 누적) 직접 재사용 불가** — 카드 상태(running→awaiting→applied)는 가변. **별도 `LedgerLog`(append-only event-sourcing, 같은 fail-soft JSONL *패턴* 답습, 모듈은 별개)** 신설. 상태 = 이벤트 fold 결과.
- 재시작 고아: "마지막 상태=running/awaiting 인 task = `interrupted`" fold. 자동 복구 없음(정직·단순).

### 영속 vs 전달 scrub 모순 해소 (B5)
- **영속(레저)**: scrub 된 카드 메타 + exfil 검사 통과분만. raw 워커 출력 미영속(CB-1 보존).
- **전달(워커 간, 디딤돌1)**: raw NL 직접 전달 *금지* — **typed artifact contract**(§6)로 controller 가 추출·검증한 bounded fields 만. NL output 은 untrusted commentary 로 분리.
- **권위·시점 명문화**: 워커 raw 출력은 controller 메모리에서 *전달용 추출 + injection 검사* 직후 폐기(영속 안 됨). 레저엔 scrub 메타만. injection 검사 = **전달 시점**(controller 가 artifact 추출할 때) + 영속 시점(exfil 검사).

### 통제 (3시점)
| 시점 | 현 상태 | 디딤돌0 |
|---|---|---|
| 실행 *전* | 게이트 없음 | (디딤돌1: 계획 승인 게이트로 부활 — D-1) |
| 실행 *중* | 취소 0 | **취소 신설** — TmuxWorker=실 kill(세션 보관 jarvis_tasks.py:148) / OllamaWorker=포기 마킹(단 백그라운드 ollama 추론은 timeout 까지 GPU 점유 = 자원 회수 한계, R4) |
| 반영 *전* | ApprovalGate | 유지 |
| 재시작 후 | 고아 | `interrupted` 마킹 |

### 통제 형태전환 명문화 (R6)
plan-then-execute 는 "인간 통제"를 *매단계 승인*이 아니라 **계획 1회 승인 + harness 능력 봉쇄 + 제어루프 부재**로 구현. 이는 `project_jarvis_controlled_child_then_friday`("인간 통제 하 협력자")의 *형태 전환*이지 약화가 아님 — 오히려 제어루프 부재로 자율 폭주 표면이 직접제어보다 작다.

## §6 열린 쟁점 (v2 — 대부분 plan-then-execute + contract-first 로 해소)

| # | 쟁점 | v2 해소 | 잔여 |
|---|---|---|---|
| ① | 격리 vs 협업 | 파일시스템 직접 공유 금지 유지. 공간 격리는 데이터흐름 못 막으므로 **②의 typed contract 가 보완** | — |
| ② | 산출물 전달 신뢰 | **typed artifact contract**(raw NL 금지, controller 추출 bounded fields). contract-first 라 워커 간 직접 통신 0 → injection 전파면 대폭 축소(B4) | artifact schema 정의는 디딤돌1 상세 |
| ③ | 재조정 게이트 피로 | plan-then-execute = 게이트 계획 1회로 축소 → **쟁점 대부분 소멸**. L4 자율 재계획은 범위 밖 | — |
| ④ | exfil (R2 신규) | ro_paths 축소 + 영속 전 검사(§3) | 검사 catalog 디딤돌1 |

## §7 비례성 — 무엇을 *안* 하는가

- **L4(동적 재분배·자율 재계획) = 범위 밖** — 프라이데이 영역.
- **첫 구현 = 디딤돌0 한정** — 영속 레저 + 공유 맥락 read + 취소/고아. 협업(디딤돌1)은 후속 cycle.
- **"boss → 워커 실행 직결 경로" 영원히 부재** — 항상 결정적 controller 경유. 단일 사용자 localhost 비례 방어.

## §8 다음 단계 (staged)

1. **brief v2 → 사용자 승인** ← 현재 (3+1 합의 REVISE 흡수 완료)
2. **디딤돌0 TDD 구현** (별도 브랜치) — LedgerLog(event-sourcing JSONL) + JarvisTaskBoard 영속화 + 재시작 interrupted fold + 취소(tmux kill/ollama 포기) + 공유 맥락 read API. 협업 0.
3. 디딤돌0 구현 후 → CONTEXT/SESSION 반영 + 본 brief 디딤돌1 상세화(별도 합의 — contract-first artifact schema + worker_kind table + ADR-011 (a)~(d) 실증).

---

## 부록 — 변경 영향

- 디딤돌0 구현 영향: `jarvis_hud/jarvis_tasks.py`(영속화), 신규 `src/jarvis/ledger.py`(LedgerLog), `src/jarvis/worker.py`(취소 hook). `memory.py`(MemoryLog)는 *패턴 참조*만(재사용 아님 — B6).
- 디딤돌1(후속) 영향: `src/jarvis/{orchestrator,boss}.py`(controller + boss plan 판단지점), worker_kind table.
- 답습 교차: ADR-011 §2.1 (a)~(d) / 헌법 5조 / CLAUDE.md §2·§3 / [[3plus1-consensus-2026-05-29-jarvis-collaborative-orchestration]].
