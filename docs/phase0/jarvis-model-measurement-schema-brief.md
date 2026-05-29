# Jarvis 모델 측정 스키마 설계 brief — Q5 (§10-5 ModelMeasurementRepo) — DRAFT v1.1

> **본 brief = 설계 정리 한정.** 어떤 §도 그 자체로 코드 작성·DB 생성·마이그레이션 실행을 발생시키지 않는다. staged: brief v1 → 사용자 승인 → **3+1 합의(+codex cross-vendor)** → (흡수) → 구현(TDD). 코드 전 문서 먼저(SDD). 실 변경 0건.

**Status**: **DRAFT v1.1 — 3+1 합의(+codex) APPROVE WITH CONDITIONS 흡수 완료**(2026-05-29). 4 source(A/B/C+codex) 전원 APPROVE WITH CONDITIONS → BLOCKING 8(C1~C8) + 채택 권고 흡수. 흡수 매트릭스 = §11. 모(母) brief = [[jarvis-unified-data-layer-design-brief]] §10-5 + Q5. 데이터 레이어 §10-2~§10-4b 구현 완료 상태에서 §10-5 진입 *직전* 스키마 정비. 구현 자동 진입 0.

**계기**: 데이터 레이어 brief §11 Q5 = "모델 비교 스키마 = 별도 cycle". §10-5 = "모델 비교/측정 `ModelMeasurementRepo` 이관 (모델 관리 화면 토대)". 사용자 "§10-5 진행, Q5 스키마부터".

---

## §1 사용자 결정 3건 (2026-05-29 확정 — 수단 결정 = 사용자 명시 영역)

| # | 결정점 | 확정 | 근거(사용자 채택) |
|---|---|---|---|
| D1 | 히스토리 모델 | **append-only 히스토리** | 모델별 추세/회귀 추적·날짜별 비교 = "모델 관리 화면"의 본래 목적. 계열 B(쿼리/관계형) DB 이득 실현. |
| D2 | 정규화 수준 | **정규화 3테이블** (session + model + run) | per-run ns 메트릭까지 컬럼화 → 강한 SQL 쿼리력. 관리 화면 확장 유연. |
| D3 | boss/multi 통합 | **통합 (kind 판별자)** | boss = 사실상 단일 모델 측정, per-model/per-run 구조 multi-model 과 동일. repo 1개로 양쪽 처리. |

## §2 현 데이터 형태 (이관 대상)

현 2 파일 모두 **스냅샷 덮어쓰기**(`open(path,"w")` — 매 실행 직전 측정 소실, 히스토리 0). 내부 타임스탬프·고유 id **없음**(파일 mtime 만 시간 단서).

- **multi-model** (`paths.multi_model_measurement_path()`): `{n_runs_per_model, models[], ranking[], total_elapsed_s}`
  - per-model 정상: `{model, warmup_s, runs[], stats{}, n_valid, n_total}`
  - per-model skipped **2변종**(C1): ① **미설치** = `{model, skipped:true, reason}` (`runs` 키 **없음**, `multi_model:46`) / ② **전 run 실패** = `{model, skipped:true, reason, runs:[{error:"..."}, ...]}` (`multi_model:61-62`; error run = `_extract_metrics` 에러 시 `{"error":...}` 단일 키, `boss:87-88`)
- **boss** (`paths.boss_measurement_path()`): `{model, runs[], stats{}, n_valid, n_total}` (래퍼=단일 모델, `warmup_s`/`ranking`/`n_runs_per_model`/`total_elapsed_s` **없음**)
- **per-run**(정상): `total_duration_ns, load_duration_ns, prompt_eval_count, prompt_eval_duration_ns, eval_count, eval_duration_ns, decode_tok_per_s, prefill_tok_per_s, latency_s` (writer `_extract_metrics` 가 정확히 이 9필드만 투영 — Ollama raw 의 잔여 필드는 버림 → **JSON 파일 = 9필드(+error) 한정** = 컬럼 매핑이 파일 기준 무손실)
- **per-metric stats**(metric ∈ {decode_tok_per_s, prefill_tok_per_s, latency_s}): `{mean, p50, std, min, max}`

**콜사이트**:
- Writer: `examples/jarvis_v00_boss_measurement.py`, `examples/jarvis_v00_multi_model_measurement.py` (전체 덮어쓰기).
- Reader: `jarvis_hud/server.py:get_top_measured_models`(skipped 제외, `stats.decode_tok_per_s.mean` 정렬 top-N) / `dashboards/jarvis_dashboard.py:79`(**skipped 포함 전체 models[] 순회**, mean 없으면 0) / `dashboards/streamlit_dashboard.py:83`.

## §3 스키마 (DDL — D1/D2/D3 + 합의 흡수)

```sql
-- 측정 세션 1건 = 한 번의 측정 실행 (append-only 히스토리: 매 실행 새 row)
CREATE TABLE IF NOT EXISTS measurement_session (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id        TEXT,            -- idempotent 키 (RB-3). legacy:{kind}:{sha8} / live=NULL. UNIQUE partial.
    kind             TEXT NOT NULL CHECK (kind IN ('boss','multi')),  -- C4/codex
    measured_ts      REAL NOT NULL,   -- 측정 시각(epoch). 마이그레이션 시 = 파일 mtime(추정치, C6).
    n_runs_per_model INTEGER,         -- multi: n_runs_per_model / boss: NULL(원본에 키 없음, C2)
    total_elapsed_s  REAL,            -- multi only (boss=NULL)
    ranking_json     TEXT,            -- multi: JSON array(모델명 순위) / boss=NULL
    created_ts       REAL NOT NULL    -- 레코드 삽입 시각 (mtime fallback 정렬 키, C6)
);

-- 세션 내 모델별 1건 (boss=1행, multi=N행). 삽입 순서(id ASC)=writer 입력 models[] 순서 보존(C8).
CREATE TABLE IF NOT EXISTS measurement_model (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id   INTEGER NOT NULL REFERENCES measurement_session(id),
    model        TEXT NOT NULL,
    warmup_s     REAL,                -- multi per-model / boss=NULL
    skipped      INTEGER NOT NULL DEFAULT 0 CHECK (skipped IN (0,1)),  -- codex
    reason       TEXT,                -- skipped 사유 (미설치/전run실패 공통)
    n_valid      INTEGER,
    n_total      INTEGER,
    -- stats: metric 3종 × {mean,p50,std,min,max} = 15 컬럼 (skipped 시 NULL)
    decode_mean REAL,  decode_p50 REAL,  decode_std REAL,  decode_min REAL,  decode_max REAL,
    prefill_mean REAL, prefill_p50 REAL, prefill_std REAL, prefill_min REAL, prefill_max REAL,
    latency_mean REAL, latency_p50 REAL, latency_std REAL, latency_min REAL, latency_max REAL,
    UNIQUE (session_id, model)        -- 세션 내 모델 중복 방어 (codex/B-R4)
);

-- per-run 메트릭. 정상 run = 메트릭 채움/error=NULL. error run(전run실패) = 메트릭 NULL/error 채움(C1).
-- 미설치 skipped = 0행 / 전run실패 skipped = error run N행.
CREATE TABLE IF NOT EXISTS measurement_run (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id                INTEGER NOT NULL REFERENCES measurement_model(id),
    run_idx                 INTEGER NOT NULL,  -- 0-based 순서
    error                   TEXT,              -- C1: error run 보존 (정상 run=NULL)
    total_duration_ns       INTEGER,
    load_duration_ns        INTEGER,
    prompt_eval_count       INTEGER,
    prompt_eval_duration_ns INTEGER,
    eval_count              INTEGER,
    eval_duration_ns        INTEGER,
    decode_tok_per_s        REAL,
    prefill_tok_per_s       REAL,
    latency_s               REAL,
    UNIQUE (model_id, run_idx)        -- 중복 child insert 방어 (codex)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_session_source_id
    ON measurement_session(source_id) WHERE source_id IS NOT NULL;  -- NULL(live) 무한 append 허용(C5)
CREATE INDEX IF NOT EXISTS idx_model_session ON measurement_model(session_id);
CREATE INDEX IF NOT EXISTS idx_model_model   ON measurement_model(model);
CREATE INDEX IF NOT EXISTS idx_run_model     ON measurement_run(model_id);
CREATE INDEX IF NOT EXISTS idx_session_kind_ts ON measurement_session(kind, measured_ts);
```

**설계 노트**:
- stats = **flat 15 컬럼**(EAV 미채택, 4 source 동의) — metric 3종 고정(실측 2파일 확인) → flat 이 단순+쿼리 직관. 신규 metric = 컬럼 추가(드묾).
- **무손실 근거(C1/codex over-claim 해소)**: writer `_extract_metrics` 가 정확히 9 ns 필드(+error)만 JSON 에 투영 → 컬럼 9 + `error` = **파일 기준 무손실**(Ollama raw 잔여 필드는 애초에 파일에 없음). `raw_json` 보조 컬럼 = **DEFER**(YAGNI — 향후 writer 가 필드 추가 시 재검토, §9 Q5-e).
- **per-run 정규화 정직 표기(C 대안3)**: per-run SQL 집계를 소비하는 콜사이트 = **현재 0건**(reader 전부 stats.mean 소비). measurement_run 정규화 = 관리 화면 확장 *미래 투자*(D2 결정 존중). row 비용은 개인 툴 규모(세션당 N모델×R런)에서 사소.
- FK = 논리적 표기(SQLite 기본 FK off — ConversationRepo 동형). 무결성은 repo 트랜잭션(§5)이 보장.

## §4 repo port (얇은 port — RB-5, *필요 메서드만*)

`src/jarvis/model_measurement_repo.py` 신설. stdlib `sqlite3` 직접(Backing 추상화 0, Rule of Three). **kind 분기는 repo 내부 dict↔row 매퍼 1곳에 격리**(C 리스크3 — 메서드 시그니처에 kind 흩뿌리지 않음).

| 메서드 | 용도 | 계약(합의 흡수) |
|---|---|---|
| `append_session(measurement: dict, *, kind: str) -> int` | writer — JSON dict 그대로 받아 3테이블 분해 적재 | **단일 트랜잭션**(원자성, C3). models[] 순서대로 INSERT(C8). skipped 2변종 처리(C1). stats 계산은 writer 유지 |
| `latest_session(kind: str) -> dict \| None` | reader — 최신(`MAX(measured_ts)`) 세션을 **현 JSON 형태로 재구성** | **kind별 원본 키 집합 정확 재현**(C2): boss=`{model,runs,stats,n_valid,n_total}` / multi=`{n_runs_per_model,models[],ranking,total_elapsed_s}`. models[] = id ASC 순서 + skipped 포함(C8). 라운드트립 동등성(원본→append→latest==원본) |
| `top_models(*, kind="multi", limit=3, metric="decode") -> list[dict]` | `server.get_top_measured_models` 대체 | **최신 세션 1건 내** skipped 제외 `{metric}_mean DESC`(C7). metric ∈ **화이트리스트**{decode,prefill,latency}→컬럼명 매핑(SQL injection 방지, C7). 전부 skipped→`[]`(현 동작 불변) |
| `model_history(*, models: list[str] \| None=None, metric="decode") -> list[dict]` | 모델 관리 화면 — 모델별 추세 + **다중 모델 동일시점 비교**(C 대안4) | measured_ts ASC, models=None→전체. 1쿼리로 여러 모델(request path 다중쿼리 회피) |
| `list_sessions(*, kind=None, limit=50) -> list[dict]` | 관리 화면 — 세션 목록 | measured_ts DESC |
| `migrate_legacy(*, multi_path, boss_path) -> dict` | 기존 스냅샷 1회 import | §6. idempotent. report 반환 |

원칙: request path 긴 scan 금지 — `limit/sort/filter` 는 SQL 종료(§5 RR-4 답습).
**후속 예약(자동 0)**: `delete_session`(수동 cascade run→model→session, ConversationRepo `delete_conversation` 동형 — 관리 화면 오측정 삭제 수요 시, B-R5).

## §5 threading + 원자성 (RB-1 답습 + C3)

ConversationRepo 동형: **connection-per-operation + `PRAGMA journal_mode=WAL` + `busy_timeout` + short transaction**, `closing()` leak 방지, pool/long-lived 금지. HUD reader 는 이미 `to_thread` 경계 보유 → sync repo 그대로(§5 RR-4).
- **append_session 원자성(C3)**: session→model→run 적재 전체를 1 `with conn:` 트랜잭션 → 부분 세션/orphan 방지. idempotency 는 "기존 source_id 세션 존재 확인 → child insert 전체 skip(no-op)"(트랜잭션 내, INSERT OR IGNORE 단독 의존 금지).

## §6 마이그레이션 (RB-3 답습 — 무손실·idempotent + 합의 흡수)

- **원본 보존**: 기존 스냅샷 JSON **읽기만**(삭제 0 = 롤백). fail-soft(실패가 기동/측정 차단 0). 손상 JSON skip + report.
- **idempotency**: `source_id = f"legacy:{kind}:{sha256(file_bytes)[:8]}"` (**kind 포함**, C4) + "세션 존재 확인 후 child 전체 skip"(C3). 동일 파일 내용 재import 0. ⚠️ 재직렬화(indent/key순서 변경)로 바이트 변하면 다른 해시 → 중복 세션 → **원본 파일은 1회 import 후 불변 전제**(B-R2).
- **measured_ts = 파일 mtime(C6, 추정치)**: 내부 타임스탬프 부재로 불가피. mtime 은 "마지막 쓰기 시각"이며 복사·rsync·`/tmp`→XDG 이동 시 오염 가능 → **legacy import 한정 근사값**, mtime 이 비현실적(미래)이면 `created_ts`(import 시각) fallback.
- **seed-1점 의미(C 리스크2)**: 현 스냅샷은 덮어쓰기로 **과거 측정 이미 소실** → 마이그레이션 = 모델별 추세 **seed 1점**. 실제 히스토리 축적은 **§10-5b writer 전환 후부터**.
- **live writer(5b) source_id = NULL**(C5): UNIQUE partial(`WHERE source_id IS NOT NULL`)이 NULL 무한 허용 → 매 측정 = 의도적 새 세션(append-only 본질, 중복=두 추세점). 스키마가 이미 지원.

## §7 통합 단계화 (§10-5a / §10-5b — 동작 불변 우선 + 선례 입도)

§10-3→4a→4b staging 입도 답습(C 대안5):
- **§10-5a (동작 불변 + 신규 capability)**: `ModelMeasurementRepo` + 스키마 + `migrate_legacy` + `paths.measurement_db_path()`. reader/writer **미변경**.
  - **5a 수용 기준(TDD RED 케이스 의무)**: ① 라운드트립 동등성(multi/boss 각각 원본 JSON→append→latest_session==원본, C2) ② skipped 2변종(미설치=runs키없음 / 전run실패=error run, C1) ③ 전부 skipped multi→top_models `[]`(B-R3) ④ models[] 순서+skipped 보존(C8) ⑤ migrate idempotency(2회 호출 동일, C3) ⑥ **DB 파일·WAL sidecar 0600**(신규 생성 — `paths.data_file`은 기존 파일만 chmod, 신규 DB=umask 0644 결함, B). repo `_ensure_schema` 직후 chmod 0600(`.db`+`-wal`+`-shm`).
- **§10-5b (이관 — 더 잘게 분할, C 대안5)**:
  - **5b-reader**: `server.get_top_measured_models`→`repo.top_models`, 대시보드→`repo.latest_session`. writer 는 여전히 JSON, repo 가 JSON import. **히스토리 미발효, reader 동등성 검증**.
  - **5b-writer**: writer→`repo.append_session`(매 실행 append=히스토리 발효) + **JSON 병기**(안전망, Q5-b). reader 전부 repo 전환 확인 후 JSON write 제거(점진).
- (선택·후속) 모델 관리 화면 UI = `model_history`/`list_sessions` 소비. 별도 cycle(자동 진입 0).

각 단계 = 별도 commit. **ConversationRepo 동일 0600 결함**(B) = 별도 후속(본 cycle 자동 흡수 0 — 동일 픽스 묶을지 사용자 결정).

## §8 비례성 — 무엇을 *안* 하는가

- Postgres 0(모 brief §6 trigger 전). 무거운 ORM 0(stdlib `sqlite3` 직접). Backing 추상화 0(Rule of Three). EAV/동적 metric 0(flat 컬럼). raw_json 0(DEFER, §9 Q5-e).
- 모델 관리 화면 UI 0(스키마/repo 토대만). 기존 JSON 삭제 0(원본 보존). 통계 계산 로직(`_summarize`) 변경 0(sink 만 교체).
- **retention/pruning 0**(C 리스크1, 명시적 DEFER) — 실측 trigger 전, 개인 툴 측정 빈도 낮음. append-only 무한 증가는 measurement_run 이 최속(세션당 N×R) but 규모 미달. [[feedback_proportionate_security_personal_tool]].
- **측정 데이터 redaction 불요**(B) — 모델명+메트릭만(PII/secret 0, 사용자 입력 없음). 모 brief §8 RB-2(대화 redaction)는 측정에 비적용.

## §9 쟁점 — 합의 후 상태

- **Q5-a**: stats flat vs EAV → **해소**(flat, 4 source). §3.
- **Q5-b**: 5b writer JSON 병기 → **해소**(5b-writer 초기 병기 → reader 전환 확인 후 제거, C/A/B). §7.
- **Q5-c**: warmup_s 위치 → **해소**(measurement_model.warmup_s, boss=NULL). §3.
- **Q5-d**: 마이그레이션 자동 시점 → 생성자 옵션(`legacy_*` 인자, ConversationRepo 동형) + fail-soft + manifest(변경 없으면 sha skip, A-R3) 권고. 5a 구현 시 확정.
- **Q5-e (신규)**: `raw_json` 보조 컬럼 = **DEFER**(writer 9필드 투영이 무손실 보장 → 현 불요. writer 필드 추가 시 재검토).
- **Q5-f (신규)**: ConversationRepo 0600 결함 동시 수정 여부 = 별도 후속(사용자 결정).

## §10 v1.1 → 구현 경로

1. brief v1 → 사용자 승인 ✅
2. 3+1 합의(+codex) → APPROVE WITH CONDITIONS → **v1.1 흡수** ✅ ← *현 단계*
3. **사용자 구현 go** → §10-5a 구현(TDD, 동작 불변, 수용기준 §7) → commit → push
4. §10-5b-reader → §10-5b-writer(이관+히스토리) → commit → push

## §11 v1.1 흡수 매트릭스 (3+1 합의 + codex)

| 항목 | source | 등급 | 흡수 위치 |
|---|---|---|---|
| C1 error-run/skipped 2변종 (measurement_run.error) | A·B·codex (3) | BLOCKING | §2, §3, §7 수용기준 |
| C2 latest_session kind별 키 정확 재현 + 라운드트립 | A·codex (2) | BLOCKING | §4, §7 |
| C3 append/migrate 원자성(트랜잭션) | B·codex·A (3) | BLOCKING | §5, §6 |
| C4 source_id에 kind 포함 | codex·C (2) | BLOCKING | §6 |
| C5 live writer source_id=NULL | 4 source | BLOCKING | §6, §9 Q5-b |
| C6 measured_ts=mtime 추정치+fallback | A·C·codex (3) | BLOCKING | §6 |
| C7 top_models metric 화이트리스트+최신세션 정의 | A·codex·C (3) | BLOCKING | §4 |
| C8 models[] 순서+skipped 보존 | A (강근거) | BLOCKING | §3, §4 |
| 신규 DB·WAL 0600 chmod | B | 채택(BLOCKING) | §7 수용기준 ⑥ |
| compare_models 다중 모델 비교 | C | 채택 | §4 model_history |
| UNIQUE/CHECK 제약 | codex·B | 채택 | §3 |
| 5b reader/writer 미세분할 | C | 채택 | §7 |
| retention DEFER 명시 | C | 채택(gap) | §8 |
| 측정 redaction 불요 명시 | B | 채택(gap) | §8 |
| per-run 정규화 실수요 0 정직 표기 | C | 채택(gap) | §3 노트 |
| raw_json DEFER / delete_session 후속 / ConversationRepo 0600 | codex/B | 채택(예약) | §9, §4, §7 |

---

## 부록 — cross-reference

- 모 brief: [[jarvis-unified-data-layer-design-brief]] §10-5, §11 Q5, §5(RB-5 얇은 port), §6(RB-1 threading), §7(RB-3 마이그레이션).
- 답습: 헌법 5조(Provider Liquidity = backing swappable) / [[feedback_proportionate_security_personal_tool]] / [[feedback_ceremony_inflation]] / [[feedback_pass_scope_overclaim]](무손실 over-claim 해소) / [[reference_codex_verify_tooling]](codex verify) / `src/jarvis/conversation_repo.py`(threading·마이그레이션 동형 선례).
- 구현 영향(후속): `src/jarvis/model_measurement_repo.py`(신규), `src/jarvis/paths.py`(measurement_db_path), `jarvis_hud/server.py`(reader=5b), `examples/jarvis_v00_*_measurement.py`(writer=5b), `jarvis_hud/dashboards/*`(reader=5b).
