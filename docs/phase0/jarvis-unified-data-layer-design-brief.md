# Jarvis 통합 데이터 레이어 설계 brief — storage 추상화 + 엔진 swappable (DRAFT v1)

> **본 brief = 설계 정리 한정.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·DB 설치·마이그레이션 실행·엔진 선택 고정** 을 발생시키지 않는다. staged: brief v1 → 사용자 승인 → **3+1 합의(+codex cross-vendor)** → (합의 흡수) → 구현. 코드 전 문서 먼저(SDD). 실 변경 0건.

**Status**: **DRAFT v1.1 — 3+1 합의 REVISE 흡수 완료 (BLOCKING 6 + 권고 5)**. 4 source(codex+A/B/C) → [[3plus1-consensus-2026-05-29-data-layer]]. 격상: APPROVE WITH CONDITIONS. 구현 진입 = 사용자 명시 + Q7/엔진/위치 결정 후 (자동 진입 0). v1.1 흡수 매트릭스 = §12.

**계기**: dogfooding 중 "대화창 관리(새 대화/이전 대화 기억)" 질문 → 사용자가 관점 격상: *"앞으로 모델 작업 데이터(JSON)·모델별 비교·관리, 단순 대화 기록뿐 아니라 시스템 전반 데이터 관리가 필요"*. → 대화 저장 결정이 아니라 **시스템 데이터 레이어 아키텍처** 결정으로 재정의.

---

## §0 범위

- **대상**: jarvis 시스템 전반의 영속 데이터 — 대화, 모델 작업 출력(JSON), 모델 비교/측정, 작업 레저, 자가진화 관찰, 시스템 상태.
- **비대상(이번)**: 실 DB 설치, 마이그레이션 실행, 엔진 *고정 결정*(3+1 후 사용자 영역), 다중 사용자/분산, 무거운 ORM.

## §1 현 상태 — 흩어진 /tmp JSONL/JSON 9종

| 파일 | 성격 | 비고 |
|---|---|---|
| `/tmp/jarvis-conversations.jsonl` | 대화 turn (append) | 단일 평면, conversation_id 없음 |
| `/tmp/jarvis-conversations-archive/` | clear 시 백업 | UI 복원 경로 없음 |
| `/tmp/jarvis-stone0-tasks.jsonl` | 작업 레저(event-sourcing) | 디딤돌0 LedgerLog |
| `/tmp/jarvis-v00-layer0-memory.jsonl` | 자가진화 관찰(read-only) | MemoryLog |
| `/tmp/jarvis-v00-layer1-report.json` | 패턴 마이닝 리포트 | layer1 |
| `/tmp/jarvis-v00-multi-model-measurement.json` | 7모델 측정/ranking | 모델 비교 |
| `/tmp/jarvis-v00-boss-measurement.json` | 보스 측정 | 모델 비교 |
| `/tmp/jarvis-v00-{claude,codex,glm}-worker-memory.jsonl` | 워커별 메모리 | 워커 비교 |

**문제**: ① 위치 `/tmp` = **OS 재부팅 시 전부 소실** ② 포맷·경로 하드코딩 산재 ③ 교차 쿼리/비교 불가(파일 전체 스캔) ④ "시스템 전반 관리" 시점 없음(대화·모델·워커 데이터가 따로 놂).

## §2 목표 / 비목표

**목표**:
- (G1) 시스템 데이터를 **단일 추상화** 뒤로 통합 — 호출부는 backing engine 을 모른다.
- (G2) backing engine **swappable** (JSONL ↔ SQLite ↔ Postgres) = 코드 변경 0.
- (G3) 영속(재부팅 생존) + 모델 비교/관리 쿼리 가능.
- (G4) 기존 데이터 **무손실 마이그레이션** 경로.

**비목표**:
- (N1) 지금 Postgres 데몬 배포 (YAGNI — §6 trigger 전).
- (N2) 다중 사용자/네트워크/분산.
- (N3) 무거운 ORM(SQLAlchemy 등) 도입 — stdlib 우선.

## §3 핵심 원칙 — Provider Liquidity 를 *저장소*에 적용

> 헌법 5조 **Provider Liquidity** = "LLM provider 코드 변경 없이 교체". **이를 저장소에 *유추적으로* 적용**(RB-6: 동기부여이지 헌법 5조-2 비협상 요구 아님 — LLM은 런타임 다모델 실교체, 저장소는 일생 0~1회 마이그레이션으로 수요 구조 다름) — repo별 port 뒤에 backing 을 두면 교체 시 **호출부 변경 *최소화***(RB-6: "코드 변경 0"은 과장 — SQL dialect·transaction·FTS 차이로 adapter 내부·tests 는 변경됨).

두 함정 동시 회피:
- **YAGNI 회피**: 지금 Postgres 데몬·credential 까지 않음(과잉).
- **Lock-in 회피**: SQLite 도 하드코딩 안 함 — 인터페이스 뒤.

이는 [[feedback_proportionate_security_personal_tool]] (개인 툴 비례성) + credential 표면 의도적 지연([[project_minimize_user_intervention]]) 과 정합 — Postgres 의 credential 표면을 §6 trigger 까지 열지 않음.

## §4 데이터 분류 — 성격별 2계열

| 계열 | 데이터 | 성격 | 자연스러운 backing |
|---|---|---|---|
| **A. 이벤트 스트림** | 레저, layer0 관찰, layer1 리포트, 측정 로그 | append-only, 순서 보존, 거의 재기록 안 함 | JSONL 또는 임베디드 테이블 |
| **B. 쿼리/관계형** | 대화(다중), 모델 비교, 워커 비교, 시스템 상태 | 조회·정렬·교차참조·집계 | **SQLite (쿼리)** |

핵심: 계열 A 는 파일 JSONL 이 이미 적합(이벤트 소싱). 계열 B 가 DB 이득이 큼(모델 비교·다중 대화). **추상화는 둘을 같은 인터페이스로 덮되, backing 은 계열별로 다를 수 있다**(인터페이스 1, 구현 N).

## §5 repo별 얇은 port (RB-5 — 범용 추상화 축소)

**RB-5(4 source)**: 범용 `StorageProvider`+`Backing` 2계층 + 공통 `append/put/get/query/delete` = lowest-common-denominator lock-in/ceremony 위험([[feedback_ceremony_inflation]]). → **repo별 *최소* port 우선**:
- **repo별 port**: `ConversationRepo` / `ModelMeasurementRepo` / `EventLogRepo` 가 *각자 필요한 메서드만* (공통 베이스 강제 안 함). 이벤트류는 append+iter 한정(read-only 답습 — [[memory]] MemoryLog/LedgerLog 가 이미 "얇은 repo" 형).
- **Backing 추상화 = deferred(Rule of Three)**: 다중 대화는 추상화 *없이* `sqlite3` 직접 구현. 2nd backing(Postgres)이 *실제 임박*할 때 사후 추출. 테스트 hermetic = `db_path=":memory:"` 로 backing 추상화 없이 달성.
- **sync base + async wrapper(Q2 해소, RR-4)**: `src.jarvis`=sync, HUD 가 이미 `asyncio.to_thread` 경계 보유 → **sync repo + HUD to_thread 래핑** 확정(async 인터페이스/aiosqlite 채택 안 함, N3 stdlib 우선). request path 긴 scan 금지 — `limit/sort/filter` 는 DB(SQL)에서 종료.

## §6 엔진 매핑 + Postgres 전환 단일 trigger

| 데이터 | 1차 backing | 근거 |
|---|---|---|
| 계열 A (이벤트) | JSONL 유지(또는 SQLite 테이블) | 이미 적합, 마이그레이션 비용↓ |
| 계열 B (대화·비교) | **SQLite** | 무인프라 쿼리(데몬0·드라이버0·credential0), 파일1개 백업 |

**Postgres 정당화 trigger (RB-4 강화, 2 source)**: 기존 "프로세스≥2" 단일 기준은 **과민** — SQLite WAL 은 단일 머신 다중 프로세스 read/write 를 상당 흡수(GB10=단일 머신이라 프라이데이라도 SQLite 가능성). → **수정 trigger(OR)**: ① 다중 호스트/네트워크 접근 ② 실측 writer lock contention ③ 동일 hot table 지속 다중 write ④ 백업·복구·접근제어가 SQLite 한계 초과. [[project_friday_separate_evolution_direction]] 진입이 자동 trigger 아님(실측 기반).

**RB-1 SQLite threading 계약 = 결정/불변식(3 source, Q3 해소)**: HUD 는 async 핸들러 `to_thread`(server.py:239) + dispatch 백그라운드 thread(jarvis_tasks.py:285) + `max_concurrent=8`. 단일 공유 connection + 기본 `check_same_thread=True` = `ProgrammingError` 로 깨짐. **확정: connection-per-operation + `PRAGMA journal_mode=WAL` + `busy_timeout` + short transaction** (LedgerLog 의 호출마다 `with open()` 동형). **connection pool/long-lived 금지**(더 위험). 단일 writer 직렬화는 개인 툴 write rate 에서 실문제 아님(구현 문제이지 규모 문제 아님).

## §7 마이그레이션 전략 (무손실 — RB-3 구체화)

- **원칙**: 기존 /tmp 파일을 **읽어 새 backing 에 적재**(원본 보존 = 롤백 가능). fail-soft(마이그레이션 실패가 기동 차단 0).
- **RB-3 idempotency(3 source) — "카운트 검증"만으로 불충분**: ① **deterministic source id**(현 `hash(message)` server.py:265 = PYTHONHASHSEED 비결정 + 20bit 충돌 → sha256 등 안정 키로 교체) ② **UNIQUE 제약 + INSERT OR IGNORE/upsert** ③ migration **manifest**(per-file checksum/mtime/size) ④ **dry-run** + partial-failure report ⑤ **atomic rename**(crash-safe, 타깃 부분상태 방지) ⑥ 손상 JSONL 라인 skip + clear archive 복원 규칙.
- 레저(LedgerLog)·MemoryLog 는 *추상화 뒤로 이동 후보*지만 강제 아님 — 계열 A 는 JSONL 유지 가능(점진).

## §8 영속 위치 + 데이터 보안 (RB-2 신규 + RR-3)

**영속 위치(RR-3, U-3)**: 현 `/tmp` = 재부팅 소실 + 9개 경로 하드코딩.
- **`JARVIS_DATA_DIR` env override 필수**(헌법 8조-2 하드코딩 제로 답습) — 경로 일원화.
- 기본값(사용자 결정 영역): **XDG_DATA_HOME 우선**(Linux 표준·백업/state 분리) → fallback `~/.jarvis/`. **repo-local `.jarvis-data` 비권고**(gitignore 누락 사고 위험).
- DB 파일 `0600` / 디렉터리 `0700`.

**RB-2 대화 영속 redaction/보안 정책(2 source 독립 일치 — codex+B, 헌법 8조)**: 현 `_save_conversation_entry`(server.py:211/263)는 raw user+model 을 redaction 없이 저장. ledger(scrub 전제)·memory(민감정보 제외)와 달리 **대화만 누락**. `/tmp`(휘발) → 영속 이동 = **노출 등급 의도적 상승** → 보안 표면 변경(헌법 8조). 정책 명문 필요: raw 저장 허용/금지, redaction 적용 범위, export/delete, opt-in.
- **신규 Q7(사용자 결정)**: raw 복원성(대화 맥락 보존) vs secret/PII 제거 = **ADR-011 means/ends trade-off**. 본 brief 는 쟁점 명문화만, *결정* 은 사용자 영역.

## §9 비례성 — 무엇을 *안* 하는가

- Postgres 지금 배포 0(§6 trigger 전). 다중 사용자/분산 0. 무거운 ORM 0. 분산 캐시·메시지큐 0.
- 추상화는 **얇게** — repository + backing 2~3개 한정. 범용 데이터 플랫폼 아님(개인 툴 비례).

## §10 단계화 (디딤돌 — RR-1/RR-2 반영)

1. brief v1 → 승인 → **3+1 합의** → v1.1 흡수 ← **완료**
2. **영속 위치 이동 + `JARVIS_DATA_DIR`**(RR-2: /tmp 소실은 지금도 위험 → 선행 가능). 경로 일원화 + 권한.
3. **0.5단계(RR-1, U-1)**: server.py 인라인 conversation 핸들러 6곳 → **sync `ConversationRepo` 추출(동작 불변 refactor)**. 안 하면 swap 시 6곳 변경.
4. **다중 대화** = `ConversationRepo` 를 `sqlite3` **직접** 구현(Backing 추상화 없이, `:memory:` 테스트) + RB-1 threading 계약 + RB-3 마이그레이션 importer + RB-2 redaction 정책(Q7 결정 후).
5. 모델 비교/측정 `ModelMeasurementRepo` 이관 (모델 관리 화면 토대, 스키마 = Q5 별도).
6. 계열 A(레저·관찰) JSONL 유지(RR-5) — SQLite 이관은 선택·점진(강제 아님).
7. (Rule of Three) 2nd backing 임박 시 backing 추상화 사후 추출.

각 단계 = 별도 cycle(자동 진입 0). 수단 결정(엔진 고정·스키마)·Q7·기본 위치 = 사용자 명시 영역.

## §11 쟁점 — 3+1 후 상태

- **Q1**: 계열 A JSONL 유지 **→ 해소(RR-5, 4 source 동의)**. SQLite 이관은 선택·점진.
- **Q2**: **→ 해소(RR-4)** sync base + HUD to_thread 래핑 확정.
- **Q3**: **→ 해소(RB-1)** connection-per-operation + WAL + busy_timeout, pool 금지(§6).
- **Q4**: 영속 위치 — env override 필수는 합의, 기본값(XDG vs ~/.jarvis) = **사용자 결정**(§8).
- **Q5**: 모델 비교 스키마 = **별도 cycle**(권고, §10-5).
- **Q6**: 과설계 — **→ 해소(RB-5)** repo별 얇은 port + Backing deferred(§5).
- **Q7 (신규)**: 대화 raw 저장 정책(raw 복원성 vs secret 제거, ADR-011 means/ends) = **사용자 결정**(§8 RB-2).

## §12 v1.1 흡수 매트릭스 (3+1 합의 REVISE → BLOCKING 6 + 권고 5)

| 항목 | source | 흡수 위치 |
|---|---|---|
| RB-1 SQLite threading 계약 결정 | C1 (3src) | §6 |
| RB-2 대화 redaction/보안 + Q7 | C2 (2src, 헌법8조) | §8 + §11 Q7 |
| RB-3 마이그레이션 idempotency 구체화 | C3 (3src) | §7 |
| RB-4 Postgres trigger 강화 | C4 (2src) | §6 |
| RB-5 추상화 축소(repo별 port, Backing deferred) | C5/D2 (4src) | §5 |
| RB-6 "코드 변경 0"→최소화 + 비협상 아님 | C6 (3src) | §3 |
| RR-1 0.5단계 핸들러→Repo 추출 | U-1 | §10-3 |
| RR-2 다중대화 직접 먼저 + 위치 선행 | U-2 | §10-2/4 |
| RR-3 JARVIS_DATA_DIR env + 권한 | U-3 | §8 |
| RR-4 sync base + async wrapper + DB-side query | codex | §5 |
| RR-5 계열 A JSONL 유지 | 4src | §6/§10-6 |

---

## 부록 — 변경 영향 / cross-reference

- 구현 영향(후속): 신규 `src/jarvis/storage/`(또는 `jarvis_hud/`) StorageProvider + backings, `jarvis_hud/server.py` 대화 핸들러, `jarvis_hud/jarvis_tasks.py`(레저 이관 시), `src/jarvis/{memory,ledger}.py`(계열 A 이관 시).
- 답습 교차: 헌법 5조(Provider Liquidity) / [[ai-backend-stack-convention]] / CLAUDE.md §3(3+1) / [[feedback_proportionate_security_personal_tool]] / [[project_minimize_user_intervention]] / [[project_friday_separate_evolution_direction]](Postgres trigger) / [[reference_codex_verify_tooling]](verify).
- 비차단 답습: dogfooding 다중 대화는 본 레이어 3단계까지 보류(사용자 결정).
