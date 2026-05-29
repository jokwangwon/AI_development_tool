# 3+1 합의 — Agent C (대안 탐색가) 리뷰: 통합 데이터 레이어 설계 brief

> 대상: `docs/phase0/jarvis-unified-data-layer-design-brief.md` (DRAFT v1)
> 관점: "더 나은 방법이 있는가?" (대안 기술 · 트레이드오프 · 과설계 경계)
> 작성: 2026-05-29 · 독립 분석 (A/B/codex 출력 미참조)

---

## 판정: **APPROVE WITH CONDITIONS**

brief 의 *방향*(영속 위치 이동 + 쿼리형은 SQLite + 이벤트 스트림은 JSONL 유지 + Postgres 지금 도입 안 함)은 대안 탐색가 관점에서도 **거의 최적에 수렴**한다. SQLite·DuckDB·LMDB·순수 JSONL을 비교해도 jarvis 의 현 워크로드(단일 프로세스, 다중 대화 조회, 모델 비교 집계)에서 SQLite 가 우세하다. Postgres 보류 결정도 정당하다.

조건부인 이유는 **§5 StorageProvider/Repository 추상화 1건**이다. 이것이 개인 단일 사용자 툴의 *현재* 규모에 비해 ceremony(과설계) 위험이 가장 크다. Provider Liquidity 를 저장소에 동형 적용한다는 명분은 매력적이지만, 헌법 5조-2 Provider Liquidity 는 *LLM provider* 의 비협상 요구이지 저장소의 비협상 요구가 아니다. 저장소 swap 은 "코드 변경 0"이 아니라 "**1회성 마이그레이션 + 호출부 소폭 수정**"으로도 충분히 달성 가능하며, 그 편이 더 정직하다. 아래 BLOCKING/권고에서 추상화를 *얇게 강제*하는 조건을 단다.

---

## BLOCKING

### B-1. §5 추상화 = 미사용 swap 축을 위한 사전 일반화 (YAGNI 위반 위험)

**근거**: brief §6 은 backing 후보를 사실상 2개(JSONL, SQLite)로 한정하고, Postgres 는 §6 단일 trigger(프라이데이 다중 프로세스 동시 write)까지 *보류*한다. 즉 **§5 추상화가 즉시 지원해야 할 실 backing 은 종류당 1개**다 (계열 A=JSONL, 계열 B=SQLite). swap 의 두 번째 후보(Postgres)는 trigger 가 올 때까지 코드로 존재하지 않는다.

- 결과: "교체 가능"을 보장하기 위해 추상화 인터페이스를 *지금* 박지만, 그 인터페이스를 통과하는 backing 은 한동안 단 하나다. 이는 [[feedback_proportionate_security_personal_tool]] 의 비례성 원칙과 [[feedback_ceremony_inflation]] 의 ceremony 인플레이션 경고에 직접 걸린다.
- Provider Liquidity 의 LLM facade 와의 비유(§3)는 *불완전*하다. LLM facade 는 사용자가 *런타임에 실제로* 7개 모델을 교체해 쓰고 있어(MEMORY: 7모델 ranking) liquidity 가 실수요다. 저장소는 사용자가 SQLite↔Postgres 를 런타임에 토글하지 않는다 — 일생에 0~1회 마이그레이션이다. **동형 적용은 표면적 대칭일 뿐 수요 구조가 다르다.**

**해소 조건 (택1, 사용자/Reviewer 결정 영역)**:
- (a) **추상화를 "Repository만, Backing 추상화 없이"로 축소** — ConversationRepo / ModelComparisonRepo 등 종류별 모듈은 만들되(이건 응집·테스트성 이득 실재), 그 *내부*는 SQLite 를 직접 호출(`import sqlite3`). swap 은 인터페이스가 아니라 "Repo 내부 구현 교체 + 마이그레이션"으로 처리. → 인터페이스 1, 구현 1, 미래 backing 은 *그때* 추가.
- (b) brief §5 추상화를 유지하되 **JSONLBacking / SQLiteBacking 2개를 *실제로 동시에 사용*하는 호출부가 존재**할 때만 정당화 (계열 A JSONL + 계열 B SQLite 가 같은 베이스를 공유) — 단 이 경우에도 베이스 연산은 최소 교집합(append/get/query)으로 *얼리고*, Postgres 가정 메서드(트랜잭션·커넥션 풀 추상화 등)는 절대 미리 넣지 않을 것.

→ 권고는 (a). (b)는 "인터페이스 1, 구현 N" 명분을 살리지만 N=2 가 *서로 다른 계열*이라 공통 베이스가 lowest-common-denominator 로 빈약해져 추상화 이득이 작다.

### B-2. §6 Postgres 단일 trigger 의 *기술적 정확성* 재검토 — "다중 프로세스 동시 write" ≠ Postgres 필요충분조건

**근거**: brief §6/§9 는 "여러 프로세스/에이전트가 같은 저장소에 동시 write" 를 Postgres 전환의 단일 명문 trigger 로 박는다. 그러나 대안 관점에서 이 trigger 는 **너무 이르게 Postgres 로 점프**한다. SQLite 는 WAL 모드에서 **다중 프로세스 동시 *읽기* + 단일 writer 직렬화**를 견고히 지원하며, 다중 프로세스 write 도 짧은 트랜잭션 + busy_timeout 으로 상당 부분 흡수한다. 프라이데이가 "여러 에이전트"라도 **로컬 단일 머신(GB10)** 이면 Postgres 데몬·credential·드라이버 비용 대비 SQLite WAL 로 충분할 가능성이 높다.

- 더 정확한 trigger 후보: ① **write 경합으로 인한 실측 lock 타임아웃/스루풋 병목**(증거 기반), 또는 ② **네트워크 경유 다중 호스트 접근**(SQLite 가 진짜로 부적합한 지점), 또는 ③ **동시 writer 의 지속적 고빈도**. 단순 "프로세스 수 ≥ 2"는 과민 trigger다.
- 이는 [[feedback_actual_run_trigger_paths_filter]] 정신(trigger 는 실측 가능해야)과 정합. "프로세스 2개"는 선언적이지만 Postgres 비용을 정당화하는 *증거*가 아니다.

**해소 조건**: §6 trigger 문구를 "**다중 프로세스 동시 write *이면서* SQLite WAL 직렬화가 실측 병목/데이터 무결성 위반을 일으킬 때**" 또는 "**네트워크 경유 다중 호스트 공유**"로 강화. 단일 머신 다중 프로세스만으로는 Postgres 미정당. (추상화가 있다면 어차피 전환 비용 0이라는 §6 주장 자체가 — B-1 권고 (a) 채택 시 — "0이 아니라 1회 마이그레이션"으로 정직화되므로, trigger 를 보수적으로 올리는 비용이 작다.)

---

## 권고 (대안 + 트레이드오프)

### R-1. 엔진 대안 비교 — SQLite 우세 확인, 단 모델 비교(계열 B)는 DuckDB 일부 검토 여지

| 엔진 | 강점 | 약점 | jarvis 적합도 |
|---|---|---|---|
| **SQLite** (brief 제안) | stdlib 내장(드라이버0·데몬0·credential0), 다중 대화 CRUD·인덱스·조인 견고, 파일1개 백업, WAL 다중 읽기 | OLAP 집계·대규모 분석 약함, 컬럼형 아님 | **계열 B 최적**. 다중 대화 = 전형적 OLTP-ish CRUD |
| **DuckDB** | 컬럼형 OLAP, 모델 비교·측정 시계열 집계·ranking 에 강함, Pandas/Parquet/JSON 직접 쿼리, 임베디드(데몬0) | 동시 write 약함(주로 분석용), 빈번한 단일행 update 비효율, 의존성 추가 | **계열 B 중 *모델 비교 서브셋*에 한해** 매력. 단 데이터 규모(개인 7모델 측정)가 작아 SQLite 로도 집계 충분 → **현 시점 도입 불요** |
| **LMDB / 임베디드 KV** | 초저지연 read, 트랜잭션 | 쿼리·정렬·집계 없음(직접 인덱싱 구현 필요), 다중 대화 조회·모델 비교에 부적합 | **부적합** — jarvis 의 이득 지점이 정확히 "쿼리"인데 KV 는 그걸 못 줌 |
| **순수 JSONL 유지** (현 상태) | 변경0, event-sourcing 정직, 마이그레이션0 | 교차 쿼리/정렬 = 전체 스캔, 다중 대화 인덱싱 수작업, 재부팅 소실(/tmp) | **계열 A 최적, 계열 B 부적합**. brief 의 계열 분리가 정확 |

→ **결론: brief 의 SQLite(B) + JSONL(A) 분리는 엔진 선택으로 정확하다.** DuckDB 는 "모델 비교 데이터가 시계열·다축 집계로 커지면" 재검토 후보로 §11 Q5 옆에 *NOTE*로 남길 가치 있음 — 단 지금 도입은 의존성·과설계. **Postgres 를 지금 도입하는 게 나은 시나리오는 없다** (단일 머신·단일 사용자·소데이터 → 데몬/credential 비용이 순손실, [[project_minimize_user_intervention]] credential 표면 회피와도 충돌).

### R-2. 추상화 대안 — "얇은 Repository, backing 추상화 없음" (B-1 권고 (a) 상세)

가장 얇은 형태 제안:

```
src/jarvis/storage/
  conversation_repo.py   # sqlite3 직접, ConversationRepo(db_path)
  model_comparison_repo.py
  # 계열 A 는 기존 LedgerLog/MemoryLog(JSONL) 그대로 — 손대지 않음
```

- **이득(추상화 vs 직접)**: Repo 모듈화는 ① 호출부(server.py)가 SQL 을 안 봄 ② 테스트 hermetic(`:memory:` SQLite 주입 — 이건 backing 추상화 *없이도* `db_path=":memory:"` 로 달성) ③ 종류별 응집. → 이 이득은 *Backing 인터페이스 없이* Repo 클래스 + 생성자 주입만으로 100% 얻는다.
- **버리는 것**: "JSONL↔SQLite 런타임 swap" — 그러나 이건 실수요 0(B-1). swap 이 진짜 필요해지면 그때 Backing 추출(리팩토링은 테스트가 받쳐주면 저렴, TDD 정합).
- **트레이드오프**: brief §5 의 "인터페이스 1, 구현 N" 우아함을 일부 포기. 대신 YAGNI·비례성·정직성 획득. 개인 툴에선 후자가 우선([[feedback_ceremony_inflation]] doc:code=251:1 evidence 가 정확히 이 함정을 경고).

`sqlite3` 는 stdlib 라 §2 N3(무거운 ORM 금지)와도 완벽 정합 — ORM 없이 `sqlite3` 직접이 가장 얇다.

### R-3. 단계화 대안 — 다중 대화를 "얇게 먼저" vs "레이어 뒤에" 트레이드오프

brief §10 은 [추상화 인터페이스 먼저(2단계) → 그 위 다중 대화(3단계)] 순서다. 대안:

- **대안 (i) — 다중 대화 SQLite 를 *먼저* 직접 구현, 추상화는 사후 추출**: dogfooding 실수요(다중 대화)가 가장 급하므로 가치를 먼저 인도. ConversationRepo(sqlite3 직접) → 작동 → 패턴이 2개 이상 생기면 그때 공통 추출. **Rule of Three**(추상화는 3번째 중복에서) 정신. → B-1 권고 (a) 와 자연 결합.
- **대안 (ii) — brief 순서 유지(인터페이스 먼저)**: swap 보장이 1순위일 때 유리하나, B-1 에서 swap 실수요가 약하다고 판단했으므로 우선순위 낮음.

→ **권고: 대안 (i)**. "추상화 인터페이스를 먼저 박는다"는 미사용 일반화를 먼저 만드는 것 — 가치 인도 지연 + over-fit 위험. 단 *영속 위치 이동(§8)* 은 다중 대화보다 *먼저* 해도 좋다(아래 R-4): /tmp 소실은 데이터 레이어 모양과 무관하게 지금도 손실 위험.

### R-4. 영속 위치 — XDG_DATA_HOME 표준 권고 (brief §8 후보보다 우위)

brief §8 후보: `~/.jarvis/` vs `<project>/.jarvis-data/`. **제3 대안: XDG Base Directory 표준** —

- `$XDG_DATA_HOME/jarvis/`(미설정 시 `~/.local/share/jarvis/`) = 영속 사용자 데이터
- `$XDG_STATE_HOME/jarvis/`(`~/.local/state/jarvis/`) = 로그·이벤트 스트림(계열 A) 같은 재현 가능/상태성 데이터

| 후보 | 장점 | 단점 |
|---|---|---|
| `~/.jarvis/` (brief 권고) | 단순·명시·발견 쉬움 | dotfile 홈 오염, 표준 아님, 데이터/상태/캐시 미분리 |
| `<project>/.jarvis-data/` | repo 근처 | repo 이동/clone 시 데이터 분리, 다중 checkout 시 분산, .gitignore 의존 |
| **XDG_DATA_HOME** (권고) | Linux 표준, 백업 도구 친화, data/state/cache 분리, GB10 Linux 환경 정합 | 경로가 길고 약간 덜 직관적, 환경변수 fallback 처리 필요 |

→ **권고: XDG 표준** (GB10 = Linux). `~/.jarvis/` 도 수용 가능하나, 표준 준수가 미래 백업·이식·다중 데이터종류 분리에서 우위. **환경변수 override 1줄**(`os.environ.get("XDG_DATA_HOME", ...)`)이면 충족 — [[environment-and-docker-design]] 의 하드코딩 금지 원칙과도 정합(`~/.jarvis` 하드코딩보다 XDG override 가 더 비-하드코딩적). 단 최종 위치는 §8 대로 사용자 명시 영역.

### R-5. §11 쟁점에 대한 대안가 의견 (간략)

- **Q1 (계열 A 도 SQLite 통합?)**: **JSONL 유지(hybrid) 권고**. event-sourcing 의 append-only·단순성·정직성이 이득. SQLite 로 옮기면 fold 로직을 SQL 로 재작성하는 비용 + 이벤트 소싱 의미 희석. 통합 이득(교차 쿼리)은 계열 A 에선 약함(레저·관찰은 주로 시간순 read). → brief 의 hybrid 가 옳음.
- **Q2 (sync vs async)**: **sync 베이스 + `to_thread`(76 답습) 권고**. `src.jarvis` 가 sync 이고 sqlite3 가 sync 라, async 인터페이스는 위장 async(내부 블로킹)가 되기 쉬움. 정직한 sync + HUD 경계에서만 `to_thread`.
- **Q5 (모델 비교 스키마 지금 vs 별도)**: **별도 cycle 권고**. 측정 축·시계열·ranking 스키마 고정은 그 자체가 별도 결정(현 7모델 측정 JSON 구조가 이미 존재 — 그걸 먼저 관찰 후 스키마화). 지금 박으면 over-fit. DuckDB 재검토(R-1)와 함께 그 cycle 에서.

---

## NOTE

- **N-1**: brief 의 *방향성 자체*(영속화 + 계열 분리 + SQLite/JSONL + Postgres 보류)는 대안 탐색가 관점에서 견고하다. 본 리뷰의 BLOCKING 2건은 모두 "방향은 맞으나 *지금* 박는 추상화/trigger 가 한 발 이르다"는 비례성 조정이지 방향 반대가 아니다.
- **N-2**: §3 의 "Provider Liquidity 를 저장소에 동형 적용" 은 *수사적으로 강력*하나 수요 구조가 LLM 과 다름(B-1). 이 비유를 brief 에 *명문 근거*로 남기면 미래에 "저장소도 비협상 liquidity" 로 오독될 위험 — Reviewer 가 §3 문구를 "유추적 동기부여, 비협상 요구 아님"으로 한정 표기 권고.
- **N-3**: DuckDB 는 현재 도입 대상 아님이나, 모델 비교 데이터가 다축 시계열로 성장 시 SQLite 대비 명확한 이득 지점. Q5 cycle 의 후보 리스트에 *기록만* 남길 가치.
- **N-4**: B-1 권고 (a)(backing 추상화 제거) 채택 시 §2 N3(무거운 ORM 금지)와 결합해 "sqlite3 stdlib 직접 + Repo 모듈" 이 최소·최정직 형태. 이것이 [[feedback_ceremony_inflation]] 의 doc:code 비대화 경고를 코드 레이어에서 반복하지 않는 방어.
- **N-5**: 마이그레이션(§7) 의 "원본 보존 + idempotent + 전후 카운트 검증" 은 대안 없이 적절. fail-soft 도 [[memory]]/ledger 패턴 답습으로 정합.

---

### 한 줄 요약
방향(영속화·SQLite/JSONL 계열 분리·Postgres 보류)은 **APPROVE**. 단 (B-1) §5 StorageProvider/Backing 추상화는 swap 실수요 0인 미사용 일반화 → "얇은 Repo + sqlite3 직접, backing 추상화 제거" 로 축소, (B-2) Postgres trigger 는 "프로세스 ≥2"가 아니라 "WAL 실측 병목 또는 네트워크 다중 호스트"로 강화 — 두 조건 해소 시 **APPROVE WITH CONDITIONS**. 영속 위치는 XDG_DATA_HOME 표준 권고.
