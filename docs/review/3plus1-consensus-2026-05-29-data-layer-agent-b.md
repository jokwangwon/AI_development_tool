# 3+1 합의 — Agent B (품질/안전성 검증가) 리뷰

> 검토 대상: `docs/phase0/jarvis-unified-data-layer-design-brief.md` (DRAFT v1)
> 핵심 질문: **"안전하고 견고한가?"** (보안 · 엣지케이스 · 데이터 무결성 · 문서 정합성)
> 날짜: 2026-05-29 · 독립 분석(A/C/codex 미참조)

---

## 판정: **REVISE**

설계 *방향*(StorageProvider 추상화 = Provider Liquidity 저장소 적용, SQLite 1차 / Postgres trigger 보류, 이벤트 JSONL 유지)은 품질·비례성 관점에서 건전하다. 그러나 brief 가 **"무손실 마이그레이션"(G4)·"영속(재부팅 생존)"(G3)** 을 *목표로 명시*하면서, 영속화가 직접 격상시키는 **at-rest secret 노출 표면**을 전혀 다루지 않았다. 이는 헌법 제8조(보안) 변경에 해당하므로(`/tmp` 휘발 → 홈 영속 = 노출 등급 상승), brief 단계에서 **명문 결정이 필요한 BLOCKING 공백**이다. 방향 reject 가 아니라, 아래 BLOCKING 2건을 brief 에 흡수 후 합의 통과 권고.

---

## BLOCKING

### B-1. 대화 영속 경로에 redaction 부재 — at-rest 평문 secret 노출 (헌법 8조)

**근거 (실증):**
- `jarvis_hud/server.py:211-217` `_save_conversation_entry()` 는 raw user `message` 와 raw model `raw_reply` 를 **redaction 없이 그대로** JSONL append 한다. server.py 전체에 `RedactionFilter`/`scrub`/`redact` import 0 (grep 확인).
- 즉 사용자가 대화창에 붙여넣은 API key·토큰·비밀번호가 **평문으로 영속**된다. `src/adapters/llm/redaction.py` 의 GP-2 prevention(송신 strip)은 *LLM egress* 만 덮고, *저장* 경로는 덮지 않는다.
- 현재 이 위험은 `/tmp`(재부팅 소실)에 의해 *부분적으로 마스킹*되어 있다. brief §1 "문제 ①"·§8·G3 는 바로 그 휘발성을 제거하고 **홈 디렉터리 영속**으로 옮기는 것을 목표로 한다 → **노출 등급을 의도적으로 상승**시키는 변경이다.

**왜 BLOCKING:** 헌법 제8조(보안)·CLAUDE.md §3 "보안 관련 변경 = 3+1 필수". 영속 위치 이동은 보안 표면 변경이며, redaction 정책 부재 상태로 영속화하면 헌법 8조 §1("비밀값 하드코딩/평문 금지" 정신)과 충돌. brief 가 "무손실"은 명시하면서 "secret 차단"은 침묵 → **불완전한 안전 설계**.

**요구 (brief 흡수 조건):**
1. 영속 *전* redaction 적용 지점을 명문화. 후보: `_save_conversation_entry` (또는 StorageProvider write 경계)에서 `RedactionFilter().redact_text` / `scrub` 적용.
2. 단, **"means vs ends" (ADR-011)** 충돌 주의 — raw 대화 *복원성* vs secret 제거는 trade-off. 대화는 사용자 본인 데이터이므로 "송신 차단(prevention)"과 "저장 마스킹"의 정책 등급이 다를 수 있다. brief 는 *어느 등급을 택할지*를 쟁점(신규 Q7)으로 올려 사용자 결정 영역에 둘 것. (이번 cycle 결정 고정 아님, 명문 trade-off 제시 의무.)
3. LedgerLog(`ledger.py`)·MemoryLog(`memory.py`)는 이미 호출측 scrub 책무 분리(ledger §5 주석, memory `_report_to_entry` 민감 정보 제외)로 설계됨 — **대화 경로만 이 보호에서 누락**됨을 brief 가 명시할 것.

### B-2. 동시성 무결성 — Q3 가 "쟁점"으로만 남아 안전 불변식 미확정

**근거 (실증):**
- HUD 는 단일 프로세스지만 **백그라운드 thread 다수**: `asyncio.to_thread(_ollama_chat_sync)` (server.py:161/239/527), `asyncio.create_task(asyncio.to_thread(board.run_task))` (jarvis_tasks.py:420). dispatch 는 `threading.Lock`(jarvis_tasks.py:134)로 보드 상태만 보호.
- brief §6 ⚠️ / §11 Q3 가 "WAL + connection-per-thread vs 단일 connection 직렬화"를 *미해결 쟁점*으로 둠. SQLite 는 동일 connection 멀티스레드 공유 시 기본 `check_same_thread=True` 로 예외, WAL 미설정 시 writer/reader 동시 접근 `SQLITE_BUSY`/락 타임아웃 발생.

**왜 BLOCKING:** "데이터 무결성"은 본 레이어의 *존재 이유*(G3 쿼리)인데, 동시성 안전 불변식이 미정인 채로는 §10 2~3단계 구현이 부분 쓰기·락 타임아웃·silent drop 위험을 떠안는다. fail-soft(brief §7)는 *마이그레이션 실패*만 흡수하지, *런타임 write 유실*을 정당화하면 안 된다(레저·대화 유실 = 무결성 위반).

**요구 (brief 흡수 조건, 결정 고정 아님 — 안전 불변식 명문화):**
1. SQLiteBacking 의 thread 모델을 brief 에 *불변식*으로 못박을 것 — 최소: `WAL` + `busy_timeout` 설정 + connection-per-thread(thread-local) **또는** 단일 writer 직렬화 큐. "둘 중 미정"을 구현 단계로 넘기지 말 것(설계 결정).
2. write 실패 시 정책: fail-soft(레저처럼 silent) vs fail-loud(쿼리 데이터는 유실 가시화) — **계열별로 다를 수 있음**을 명시. 계열 B(대화·비교) silent drop = 사용자가 손실을 모름 → 최소 로그/카운트 필요.
3. SQLite 트랜잭션 단위 명시(append 1건 = 1 commit) → 부분 쓰기 원자성 확보.

---

## 권고 (APPROVE WITH CONDITIONS 수준 — BLOCKING 해소 후 채택)

### R-1. 마이그레이션 idempotency 키 = `hash(message)` 위험 (§7)
- 현 entry id 가 `f"user-{ts}-{hash(message) & 0xfffff}"` (server.py:265) — Python `hash()` 는 **PYTHONHASHSEED 로 프로세스마다 달라지는 비결정적** 값이며 20bit 마스킹으로 충돌 확률 높음. brief §7 "idempotent(재실행 안전)" 의 키로 이 id 를 쓰면 **재실행 시 중복 적재 또는 누락**. 마이그레이션 importer 의 idempotency 키는 결정적(예: 파일 offset 또는 정규화 entry 해시 sha256)로 정의할 것.

### R-2. 마이그레이션 중 크래시 / 부분 적재 (§7)
- brief §7 "전/후 카운트 검증"은 좋으나, **검증 실패 시 처리**(rollback? 신규 backing 폐기?)가 미정. "원본 보존 = 롤백 가능"은 *소스* 보존만 보장, *타깃의 부분 상태*는 안 다룸. 권고: 마이그레이션을 임시 파일/임시 DB 에 적재 → 카운트 검증 통과 후 atomic rename 으로 swap (crash-safe). 부분 타깃은 폐기.

### R-3. 영속 위치 권한 (§8) — 0700 / 0600 명시
- `~/.jarvis/` 이동 시 B-1 의 평문 위험과 결합 → 디렉터리 `0700`, DB/JSONL 파일 `0600` 권한 권고를 brief 에 넣을 것. `/tmp` 는 sticky bit 라도 다중 사용자 기기에서 노출 가능하므로 `~/.jarvis/` 이동은 *권한 관점에선 개선*임을 명시(이 점은 B-1 의 영속 노출 상승과 별개로 긍정).

### R-4. 영속 경로 하드코딩 — 헌법 8-2조 §1 정합 (§8)
- brief §8 이 `~/.jarvis/` 를 **권고 후보 경로로 직접 제시**. 현 코드도 `CONVERSATIONS_PATH = "/tmp/..."` 외 9개 경로 전부 하드코딩(server.py:177 등). 헌법 8-2조 §1 "하드코딩 제로(포트·URL·모델명 등)"·§2 ".env 중앙 관리" 와의 정합을 위해, 경로는 **단일 환경변수/설정**(예: `JARVIS_DATA_DIR`, 기본값 `~/.jarvis`)로 일원화할 것을 brief 가 명문화. (8-2조 vs 5조-2 위계 평가는 별도 cycle — 헌법 line 80 — 이지만, "하드코딩 회피" 자체는 양 조항 공통.)

### R-5. `entries[-200:]` 무손실 회귀 위험 (참고)
- 현 `conversation_history_handler` 는 `entries[-200:]`(server.py:315)로 잘라 반환 — 표시 한정이라 저장 자체는 보존되나, SQLite 이관 시 "쿼리 limit" 으로 재현하되 *전체 보존*을 깨지 말 것(다중 대화 §10-3 에서 conversation_id 페이지네이션으로 대체).

---

## NOTE (비차단 — over-claim 점검 / 정합)

- **N-1 (over-claim 점검):** brief §3 "교체가 코드 변경 0"·"호출부 코드 변경 0"(§6)은 *인터페이스가 충분히 일반적일 때만* 성립하는 *목표 주장*이지 *증명*이 아니다([[feedback_pass_scope_overclaim]] detection≠prevention 류). 특히 JSONL(append+iter) ↔ SQLite(query/sort/filter) ↔ Postgres 는 **쿼리 표현력·트랜잭션 시맨틱이 달라** 진짜 0-변경 교체는 추상화 누수 위험. brief §11 Q6(과설계 경계)와 연동해, "코드 변경 0"을 *불변식*이 아니라 *설계 목표 + 누수 시 명시* 로 톤다운 권고. (= Provider Liquidity 의 정신은 보존하되, 저장소는 LLM facade 보다 시맨틱 차이가 큼.)
- **N-2 (정합 — 긍정):** Postgres credential 표면 지연은 [[feedback_proportionate_security_personal_tool]]·[[project_minimize_user_intervention]]·[[project_friday_separate_evolution_direction]](다중 에이전트 = Postgres trigger)와 **정합**. 비례성 위반 없음. §9 비목표 명시도 ceremony 인플레이션 차단([[feedback_ceremony_inflation]])과 부합.
- **N-3 (정합 — Provider Liquidity):** 저장소를 인터페이스 뒤에 두는 것은 헌법 5조-2 §2("분기 코드 금지")의 저장소판으로 해석 가능 — 단 backing 선택이 *설정*에서 이뤄지도록(R-4 와 연동) 해야 진짜 정합.
- **N-4 (사항 단순):** B-1/B-2 는 "보안·동시성 결정이 brief 에서 *침묵*"이 문제이지, *틀린 결정*을 했다는 게 아님. brief 가 두 쟁점을 명문 trade-off + 신규 Q(Q7 redaction 등급, Q3 동시성 불변식 확정)로 끌어올리면 REVISE → APPROVE WITH CONDITIONS 로 상향 가능.
- **N-5:** 디스크 풀 / 손상 파일 엣지케이스 — JSONL 경로는 `_iter_lines` 가 손상 라인 skip(ledger.py:95, memory.py:104)으로 이미 견고. SQLite 손상(`SQLITE_CORRUPT`)·디스크 풀(`SQLITE_FULL`) 대응은 brief 에 한 줄이라도(fail-loud vs 무시) 명시 권고 — 무손실 목표(G4)와 직결.

---

## 요약

| 항목 | 판정 |
|---|---|
| 설계 방향(추상화·SQLite 1차·Postgres 지연·이벤트 JSONL) | 건전 ✔ |
| 데이터 무결성/마이그레이션(§7) | 보강 필요(R-1 idempotency 키, R-2 atomic swap) |
| 동시성(§6/Q3) | **BLOCKING B-2** — 안전 불변식 미확정 |
| credential/at-rest 보안 | **BLOCKING B-1** — 대화 영속 redaction 부재 + 영속화가 노출 격상 |
| 문서 정합성 | 정합(비례성·Provider Liquidity) / over-claim 톤다운 권고(N-1) + 경로 하드코딩(R-4) |

**최종: REVISE** — B-1, B-2 를 brief 에 명문 흡수(결정 고정 아님, *쟁점·불변식 명문화*) 후 합의 통과 권고.
