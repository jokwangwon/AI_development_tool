# 3+1 합의 — Jarvis 통합 데이터 레이어 설계 brief v1 (Reviewer 통합)

> 대상: `docs/phase0/jarvis-unified-data-layer-design-brief.md` (DRAFT v1)
> 일자: 2026-05-29 · 프로토콜: CLAUDE.md §3 (아키텍처 결정 = 풀 3+1 필수)
> source 4: codex(OpenAI cross-vendor) + Agent A(구현) + Agent B(안전) + Agent C(대안). 3 Agent 병렬 독립(상호 참조 0), codex 외부.

## 통합 판정: **REVISE → v1.1 흡수 (후 APPROVE WITH CONDITIONS 격상)**

| source | 판정 | BLOCKING |
|---|---|---|
| codex (외부) | APPROVE WITH CONDITIONS | 4 (Postgres trigger / SQLite threading / 대화 redaction / 마이그레이션 idempotency) |
| Agent A (구현) | APPROVE WITH CONDITIONS | 3 (SQLite multithread 고정 / 핸들러→Repo 추출 0.5단계 / idempotency hash() 비결정) |
| Agent B (안전) | **REVISE** | 2 (대화 redaction 부재 헌법8조 / 동시성 무결성 Q3) |
| Agent C (대안) | APPROVE WITH CONDITIONS | 2 (Backing 추상화 YAGNI / Postgres trigger 과민) |

**방향은 4/4 건전 합의** — 영속화 + 계열 분리(쿼리=SQLite/이벤트=JSONL) + Postgres 보류 + ORM 회피 + TDD 단계화는 개인 localhost 툴에 적합. 단 **보안(대화 redaction, 헌법8조)** 가 codex·Agent B 독립 일치로 발화 → 보수적 **REVISE**. BLOCKING은 *구현 전 brief 흡수* 대상(코드 변경 전). v1.1 1pass 흡수 후 APPROVE WITH CONDITIONS 자격.

---

## Phase 3 — 교차 비교

### ① Consensus (3~4 source 일치)

- **C1. SQLite 멀티스레드/connection 계약 못박기** (codex B2 + Agent A B-A1 + Agent B B-2 = **3 source**). HUD는 async 핸들러 `asyncio.to_thread`(server.py:239) + dispatch 백그라운드 thread(jarvis_tasks.py:285) + `max_concurrent=8`. 단일 공유 connection + 기본 `check_same_thread=True` = `ProgrammingError`로 거의 확실히 깨짐. Q3(쟁점)을 **결정/불변식**으로 격상. **수렴 결정 = connection-per-operation + WAL + busy_timeout + short transaction** (LedgerLog의 호출마다 `with open()` 동형; Agent A: pool/long-lived 금지 명기). 직렬화는 개인 툴 규모에서 실문제 아님(구현 문제이지 규모 문제 아님 — Agent A R-A4).

- **C2. 대화 영속 redaction/보안 정책 부재** (codex B3 + Agent B B-1 = **2 source 독립 일치, 헌법8조**). `_save_conversation_entry`(server.py:211/263)가 raw user+model을 redaction 없이 저장. ledger(scrub 전제)·memory(민감정보 제외)와 달리 **대화만 누락**. `/tmp`(휘발) → `~/.jarvis`(영속) 이동 = **노출 등급 의도적 상승**. 정책 명문 필요: raw 저장 허용/금지, redaction 범위, export/delete, DB 파일 권한, opt-in. raw 복원성 vs secret 제거 = **ADR-011 means/ends trade-off → 신규 Q7 사용자 결정**.

- **C3. 마이그레이션 idempotency 구체화** (codex B4 + Agent A B-A3 + Agent B R-1 = **3 source**). entry id `hash(message)`(server.py:265)는 PYTHONHASHSEED 비결정 + 20bit 마스킹 충돌 → 재실행 중복/누락. "카운트 검증"만 불충분. 필요: deterministic source id(sha256), UNIQUE 제약 + INSERT OR IGNORE/upsert, migration manifest(per-file checksum/mtime/size), dry-run, partial-failure report, atomic rename(crash-safe), 손상 라인·clear archive 복원 규칙.

- **C4. Postgres 전환 trigger 과민 수정** (codex B1 + Agent C B-2 = **2 source strong**). "프로세스≥2" 단일 기준은 과도 — **SQLite WAL은 단일 머신 다중 프로세스 read/write 상당 흡수**. GB10=단일 머신이라 프라이데이라도 SQLite 가능성. 수정: trigger를 *"다중 호스트/네트워크 접근 OR 실측 writer lock contention OR hot table 지속 다중 write OR 백업·복구·접근제어가 SQLite 한계 초과"* 로 강화.

- **C5. 추상화 비례성 — 범용 2계층 → repo별 얇은 port** (codex 권고 + Agent C B-1 + Agent B NOTE + Agent A 보강 = **4 source touch**). 범용 `StorageProvider`+`Backing` 2계층 + 공통 `append/put/get/query/delete`는 lowest-common-denominator lock-in/ceremony 위험([[feedback_ceremony_inflation]]). **repo별 최소 port**(`ConversationRepo`/`ModelMeasurementRepo`/`EventLogRepo`)가 개인 툴에 적합. Agent C: Backing 추상화 *제거* + `sqlite3` 직접 + 테스트 hermetic은 `:memory:`로 달성 + Rule of Three(2nd backing 임박 시) 사후 추출. (LedgerLog/MemoryLog는 이미 "얇은 repo" 형 — Agent A.)

- **C6. "코드 변경 0" 과장 톤다운** (codex 권고 + Agent B NOTE + Agent C NOTE = **3 source**). SQL dialect·transaction semantics·migration tooling·FTS 차이로 **adapter 내부·tests는 반드시 바뀜** → "호출부 *변경 최소화*"로 정정. §3 "Provider Liquidity 저장소 동형" = **"유추적 동기부여, 비협상 아님"** 한정 표기(헌법 5조-2 비협상 오독 방지).

### ② Unique (단일 source, 흡수 가치 높음)

- **U-1 (Agent A B-A2)**: **0.5단계 누락** — conversation 영속이 server.py 인라인 6핸들러(`_save_conversation_entry:211`, 삭제 시 전체 JSONL 재작성 :343~363). swap 전 **"인라인 → sync ConversationRepo 추출(동작 불변 refactor)"** 선행 필요. 없으면 6곳 고침 = 호출부 변경 최소화 목표 깨짐.
- **U-2 (Agent C 단계화)**: **다중 대화 SQLite 직접 먼저 구현 → Rule of Three 사후 추출**. 영속 위치 이동은 다중대화보다 *먼저* 해도 좋음(/tmp 소실은 지금도 위험).
- **U-3 (Agent B R-3/4 + codex + Agent C)**: 경로 하드코딩(현 9개 `/tmp`) → **`JARVIS_DATA_DIR` env override 필수** + DB 파일 0600 / 디렉터리 0700. repo-local `.jarvis-data`는 gitignore 누락 사고 위험 → 비권고(codex).

### ③ Divergence (해소)

- **D1. 영속 위치 기본값**: `~/.jarvis`(codex 기본+env / Agent B) vs `XDG_DATA_HOME`(Agent C, Linux 표준·백업친화). → **해소**: env override 필수는 합의. 기본값은 사용자 결정 영역(권고: XDG_DATA_HOME 우선, fallback `~/.jarvis`). repo-local 비권고는 합의.
- **D2. 추상화 시점**: Agent C(Backing 추상화 제거, 사후 추출) vs codex/Agent A(얇은 port는 OK). → **해소(C5 답습)**: v1.1에서 §5를 "repo별 얇은 port + sqlite3 직접, Backing 추상화 deferred(Rule of Three)"로 약화. 다중대화는 추상화 *없이* SQLite 직접 먼저.
- **D3. 판정**: Agent B REVISE vs 3 APPROVE w/ COND. → **REVISE 채택**(보안 C2 = 헌법8조, 보수적). v1.1 흡수 후 격상.

---

## Phase 4 — v1.1 흡수 권고 (BLOCKING 6 + 권고 5)

| # | 항목 | 출처 | brief 반영 |
|---|---|---|---|
| RB-1 | SQLite threading 계약 결정(conn-per-op+WAL+busy_timeout+short tx, pool 금지) | C1 (3src) | §6/Q3 → 결정·불변식 |
| RB-2 | 대화 영속 redaction/보안 정책 + Q7(raw vs secret) 신규 | C2 (2src, 헌법8조) | §5/§8 신규 보안 § + Q7 |
| RB-3 | 마이그레이션 idempotency(결정적 id+UNIQUE+manifest+dry-run+atomic) | C3 (3src) | §7 구체화 |
| RB-4 | Postgres trigger 강화(다중호스트/실측contention/hot-table/운영한계) | C4 (2src) | §6 trigger 수정 |
| RB-5 | 추상화 축소(repo별 얇은 port + sqlite3 직접, Backing deferred) | C5/D2 (4src) | §5 약화 |
| RB-6 | "코드 변경 0"→"호출부 변경 최소화" + Provider Liquidity "비협상 아님" | C6 (3src) | §3/§6 톤다운 |
| RR-1 | 0.5단계: 인라인 핸들러→sync ConversationRepo 추출(동작 불변) 선행 | U-1 | §10 단계 삽입 |
| RR-2 | 다중대화 SQLite 직접 먼저 + 영속이동 선행 가능 | U-2 | §10 순서 |
| RR-3 | JARVIS_DATA_DIR env + 0700/0600 + repo-local 비권고 | U-3 | §8 |
| RR-4 | sync base + async wrapper, query는 DB에서 limit/sort/filter 종료 | codex 권고 | §5 |
| RR-5 | 계열 A(레저/관찰) JSONL 유지 | 4src 동의 | §6 확인 |

**신규 쟁점 Q7** (사용자 결정): 대화 raw 저장 정책 — raw 복원성(대화 맥락 보존) vs secret/PII 제거(헌법8조). ADR-011 means/ends 영역.

## Phase 5 — 결론

- **방향 승인** (4/4): 추상화된 데이터 레이어 + 계열 분리 + SQLite/JSONL + Postgres 보류 = 개인 툴 비례 적합.
- **단 v1.1 흡수 전 구현 진입 금지**: BLOCKING 6 (특히 RB-2 보안 = 헌법8조, RB-1 멀티스레드 = 무결성). 흡수는 brief 문서 한정(코드 0).
- **격상 자격**: v1.1 1pass 흡수(BLOCKING 6 + 권고 5) 후 APPROVE WITH CONDITIONS. 수단 *결정*(엔진 고정·스키마)·Q7·기본 영속 위치 = 사용자 명시 영역(자동 진입 0).
- 4 source 모두 실 코드/파일 변경 0 (read-only 분석 + 본 리뷰 doc만).
