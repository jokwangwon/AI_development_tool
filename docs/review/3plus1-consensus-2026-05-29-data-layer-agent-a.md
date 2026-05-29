# 3+1 합의 — Agent A (구현 분석가) 리뷰: 통합 데이터 레이어 brief

> 검토 대상: `docs/phase0/jarvis-unified-data-layer-design-brief.md` (DRAFT v1)
> 관점: **"실제로 동작하는가?"** (기술적 구현 가능성, 의존성, 성능)
> 날짜: 2026-05-29 / 환경: Python 3.12.3, stdlib `sqlite3` 사용 가능, 외부 ORM 0

---

## 판정: **APPROVE WITH CONDITIONS**

방향(StorageProvider 추상화 + swappable backing + SQLite 1차 + Postgres trigger 보류)은
**기존 코드 구조 위에 깔끔히 구현 가능**하다. facade.py 가 이미 동형 선례(injection +
lazy import + hermetic test)를 입증했고, LedgerLog/MemoryLog 는 이미 "얇은 repository"
형태라 추상화 흡수가 자연스럽다. 다만 **SQLite 멀티스레드 모델**과 **conversation 영속
경로의 현 인라인 구현**, **마이그레이션 idempotency 키 부재**에서 구체적 BLOCKING 이
있어 무조건 APPROVE 는 못 한다. 아래 조건 충족 시 구현 진입 가능.

---

## BLOCKING (구현 진입 전 반드시 해소)

### B-A1. SQLite write 경로 = `asyncio.create_task(asyncio.to_thread(...))` fire-and-forget 위에 얹힘 — connection-per-write + WAL 명문화 필수

근거 (`server.py:420`):
```python
asyncio.create_task(asyncio.to_thread(board.run_task, task_id))
```
dispatch 는 fire-and-forget 백그라운드 스레드다. `max_concurrent=8`
(`jarvis_tasks.py:126`) → **최대 8개 dispatch 스레드가 동시 생존** 가능하고, 각 스레드는
run_task 내부에서 레저 `_record` 를 여러 번 호출한다(`created`/`awaiting`/`resolved`).
계열 B(대화)도 SQLite 로 가면 동일 thread pool 에서 write 가 일어난다.

Python `sqlite3` 의 default threading mode 는 `serialized`(모듈 레벨 동시성 허용)지만,
**connection 객체는 기본 `check_same_thread=True`** 라 생성 스레드 외에서 쓰면
`ProgrammingError` 가 난다. to_thread 는 default ThreadPoolExecutor 의 **임의 워커
스레드**에 디스패치하므로 "어느 스레드가 잡을지" 가 비결정적이다 → **단일 공유
connection 을 보관하면 거의 확실히 깨진다.**

→ BLOCKING 해소 조건: brief §6 Q3 를 "**열린 쟁점**" 이 아니라 **결정**으로 고정해야
구현 가능. 권장 결정 = **connection-per-operation (`with sqlite3.connect(path) as conn:`
호출마다 열고 닫기) + `PRAGMA journal_mode=WAL` + `PRAGMA busy_timeout=5000`**. 이유:
- connection-per-operation 은 `check_same_thread` 문제를 원천 제거(어느 스레드든 자기
  connection). LedgerLog 가 이미 `with open(...)` 을 호출마다 여는 패턴(`ledger.py:75`)
  과 동형 — 추상화에 자연스럽다.
- WAL 은 reader 가 writer 를 막지 않게 해 HUD 의 `tasks`(GET snapshot)/`history` 조회가
  dispatch write 와 병행될 때 `database is locked` 를 줄인다.
- busy_timeout 은 동시 write 직렬화 시 즉시 실패 대신 대기시킨다.

connection pool 이나 단일 long-lived connection 은 이 코드 구조(임의 to_thread 워커)에서
**오히려 더 위험**하므로 채택하지 말 것을 명기.

### B-A2. conversation 영속은 현재 server.py 인라인 함수 — repository 추출이 마이그레이션의 *전제*다 (brief 가 이를 단계로 명시 안 함)

근거: 대화 저장/조회/삭제/export 는 모듈이 아니라 `server.py` 안에 인라인으로 흩어져
있다 — `_save_conversation_entry`(`server.py:211`), `conversation_history_handler`
(전체 파일 스캔 `:300`), `conversation_delete_entry_handler`(**전체 JSONL 재작성**
`:343~363`), export/canvas 도 각자 파일을 연다. 즉 "ConversationRepo" 라는 호출부가
**아직 존재하지 않는다.** brief §10-3 은 "ConversationRepo SQLite 구현 + 다중 대화" 를
한 단계로 묶었지만, 그 전에 **현 인라인 6개 핸들러를 sync Repo 인터페이스로 추출
(refactor, 동작 불변)** 하는 0.5 단계가 빠져 있다.

이게 BLOCKING 인 이유: 추상화의 G1("호출부는 backing 을 모른다")은 호출부가
*인터페이스를 통해 호출* 할 때만 성립한다. 현재처럼 핸들러가 직접 `open()` 하면
backing swap 시 6곳을 다 고쳐야 해서 "코드 변경 0"(G2)이 깨진다.

→ 해소 조건: §10 에 "3-0 단계: conversation 인라인 핸들러 → sync Repo 인터페이스 추출
(backing=현 JSONL 유지, 동작·테스트 불변 refactor)" 를 명시. 그 후에 backing 만
SQLite 로 교체하면 핸들러 무수정.

### B-A3. 마이그레이션 idempotency 키가 정의돼 있지 않다 — 현 데이터에 안정 식별자 부재

근거: brief §7 은 "idempotent(재실행 안전) + 전/후 카운트 검증" 을 요구하지만, **현
데이터 상당수에 안정적 primary key 가 없다**:
- 대화 entry id = `f"user-{ts}-{hash(message) & 0xfffff}"` (`server.py:265`). `hash()`는
  **PYTHONHASHSEED 로 프로세스마다 달라지는** 문자열 해시 → 동일 메시지라도 재실행 시
  다른 id 생성 가능. 또 같은 초(`ts` 초 단위)에 같은 메시지 두 번이면 충돌.
- 레저는 task_id(uuid) 가 있어 안전하나, 대화/측정 JSON 은 그렇지 않다.

idempotent importer 는 "이미 적재된 행인가" 를 판정할 키가 있어야 성립한다. 키가
불안정하면 재실행 시 **중복 적재** 또는 **카운트 검증 통과하지만 실제 중복** 이 난다.

→ 해소 조건: 마이그레이션 설계 시 (a) 대화는 `(ts, role, content)` 복합 자연키 또는
import 시 신규 안정 id 재발급 + 원본↔신규 매핑 보존 중 하나를 명시, (b) SQLite 스키마에
`UNIQUE` 제약 + `INSERT OR IGNORE` 로 DB 레벨 idempotency 보강. "카운트 검증" 만으로는
idempotency 가 보장 안 됨을 brief §7 에 반영.

---

## 권고 (BLOCKING 아님, 강하게 권장)

### R-A1. sync 베이스 + to_thread 래핑 = 정답. async 인터페이스는 채택하지 말 것 (Q2 결정)

근거: 코드베이스 전체가 이미 이 패턴으로 수렴해 있다 — `_ollama_chat_sync` +
`asyncio.to_thread`(`server.py:35,161,239,527`), board.run_task/cancel/pane 전부
to_thread 래핑(`jarvis_tasks.py:420,445,463`). `src.jarvis` 는 전부 sync(LedgerLog,
MemoryLog, Orchestrator). 여기에 async storage 인터페이스(aiosqlite 등)를 넣으면:
- src.jarvis(sync) 호출부가 storage 를 못 부른다(sync→async 호출 불가).
- aiosqlite = 새 외부 의존(N3 stdlib 우선 위반).
- 76 entry 의 "이벤트 루프 비차단" 교훈은 to_thread 로 이미 해결됨 — SQLite write 는
  ms 단위라 to_thread 로 충분.

→ Q2 = **sync 베이스 인터페이스 단일안**으로 고정 권고. HUD 는 기존처럼 to_thread 로 감싼다.

### R-A2. 계열 A 는 JSONL 유지 (Q1) — event-sourcing fold 의미론과 read-only 불변식을 SQLite 가 더 잘 못 한다

근거: LedgerLog.fold()(`ledger.py:99~131`)와 MemoryLog 는 **append-only +
변경 API 부재**가 핵심 안전 속성(CB-1/B5/Layer0 read-only 발효, MEMORY.md). JSONL 파일은
`open(..., "a")` 자체가 이 불변식을 물리적으로 강제한다. SQLite 테이블로 옮기면
UPDATE/DELETE 가 *물리적으로 가능* 해져 "변경 불가" 를 코드 규율로만 지켜야 한다 →
안전 등급 후퇴. 이벤트량도 append-only 스트림이라 쿼리 이득이 작다. → 계열 A = JSONL
유지, 계열 B 만 SQLite 권고(brief §6 1차안 지지).

### R-A3. 추상화는 facade.py injection 선례를 그대로 답습 (Q6 과설계 방지)

근거: facade.py 가 이미 "Provider Liquidity 를 코드로 구현한" 검증된 선례다 — lazy
import(litellm 미설치도 hermetic) + Router 주입 + frozen dataclass 출력. StorageProvider
도 동일하게 **backing 을 생성자 주입**(brief §5 이미 명시)하고 backing import 는 lazy 로
하면 hermetic test(JSONLBacking) + 교체(SQLiteBacking) 둘 다 성립. repository 는
LedgerLog 만큼만 얇게(record/read/fold 3 메서드 수준) — 범용 query DSL 금지. JarvisTaskBoard
가 이미 `ledger=` 주입(`jarvis_tasks.py:127`, `server.py:570`)을 받고 있어 seam 도 존재.

### R-A4. 동시 write 직렬화는 개인 툴 규모에서 실제 문제 아님 (성능 현실성)

근거: 단일 사용자 localhost. write trigger = (1) 사용자가 채팅 1건 보낼 때, (2) dispatch
스레드가 task 이벤트 기록할 때. 사람이 만드는 write rate 는 초당 수 건 미만. SQLite WAL +
busy_timeout 5s 면 8개 dispatch 스레드가 동시에 기록해도 직렬화 대기는 ms~수십ms.
대화 데이터량도 export 가 "last 200/100"(`server.py:315,509`)으로 이미 작다. → 성능은
SQLite 로 차고 넘침. Postgres trigger("다중 프로세스 동시 write" = 프라이데이)까지 보류는
타당. **단, B-A1 의 connection-per-op + WAL 이 전제** — 잘못 구현하면 규모와 무관하게
`database is locked` 로 깨진다(규모 문제가 아니라 구현 문제).

### R-A5. 영속 위치(Q4) `~/.jarvis/` = 구현상 문제 없음, 단 server.py 의 9개 하드코딩 경로 동시 정리 필요

근거: 현재 경로가 `server.py` 와 `jarvis_tasks.py` 에 문자열 리터럴로 산재
(`CONVERSATIONS_PATH="/tmp/..."` `server.py:177`, `LedgerLog("/tmp/jarvis-stone0-tasks.jsonl")`
`server.py:570`, layer0/layer1/measurement 경로 `:51,78,90`). `~/.jarvis/` 이동은
`Path.home()/".jarvis"` + `mkdir(parents=True, exist_ok=True)`(LedgerLog 가 이미
parent mkdir 함 `ledger.py:73`)로 자명. 다만 경로 결정을 **단일 설정 모듈**로 모아야
"하드코딩 산재"(brief §1 문제 ②) 재발 안 함. 환경+Docker 컨벤션(하드코딩 금지) 답습.

---

## NOTE

- **N-A1**: 현 `conversation_delete_entry_handler` 는 매 삭제마다 **전체 JSONL 재작성**
  (`server.py:343~363`)이라 데이터 증가 시 O(N) 비용 — SQLite 이전의 부수 이득(DELETE
  WHERE id=? 한 줄)으로 자연 해소. 마이그레이션 정당화에 이 점 추가 권고.
- **N-A2**: 대화 entry 에 `conversation_id` 가 없다(brief §1 명시)는 점은 추상화가 아니라
  **스키마 설계** 이슈 — §10-3 "다중 대화" 가 conversation_id 컬럼 도입을 포함해야
  의미가 있다. 다중 대화 = 단순 컬럼 추가가 아니라 새 그룹핑 키 + 마이그레이션 시 기존
  평면 turn 을 어느 conversation 에 귀속시킬지(전부 "default" 대화로) 결정 필요.
- **N-A3**: Q5(모델 비교 스키마)는 측정 JSON 구조(`server.py:88~106` 의
  `stats.decode_tok_per_s.mean` 등 중첩)가 이미 복잡 → 이번에 평면 테이블로 강제
  정규화하면 ceremony. **측정 데이터는 계열 A(이벤트/append) 처럼 JSON blob 컬럼 +
  인덱스용 소수 컬럼**(model, ts, decode_mean) 만 발췌 권고. 전면 정규화는 별도.
- **N-A4**: `sqlite3` 는 Python 3.12 stdlib 확인(별도 설치 0). N3(stdlib 우선) 충족.
  외부 의존 추가 0으로 구현 가능 = Provider Liquidity/비례성과 정합.
- **N-A5**: brief 가 "코드/DB설치/마이그레이션 0건"(line 3) 을 명시 — 본 리뷰도 코드
  read-only 로 수행, 실 변경 0건임을 확인.

---

## 요약 한 줄

방향은 구현 가능하고 코드 선례(facade injection, LedgerSQL-friendly fold 패턴)가 받쳐주나,
**(B-A1) SQLite connection-per-op + WAL 을 쟁점이 아닌 결정으로 고정**, **(B-A2)
conversation 인라인 핸들러의 Repo 추출 단계를 §10 에 명시**, **(B-A3) 마이그레이션
idempotency 키를 정의**해야 "실제로 동작" 한다 → **APPROVE WITH CONDITIONS**.
