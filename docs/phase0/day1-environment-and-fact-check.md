# Phase 0 — Day 1 보고서: 환경 준비 + 사실 확인

> **작성일**: 2026-05-05
> **브랜치**: `feature/hermes-phase0`
> **상태**: 1차 사실 확인 완료, **§3.4 폴백 검토 필요**

---

## 1. 결론 요약

| 항목 | 결과 | 비고 |
|------|------|------|
| Hermes v0.12.0 실재성 | **PASS** | 2026-04-30 "Curator release" GitHub 릴리스 확인 |
| PyPI `hermes-agent==0.12.0` 패키지 | **FAIL** | PyPI 미존재 — P2 v2 §2.6.1 Dockerfile 가정 정정 필요 |
| 공식 설치 방식 | curl 또는 git clone + install.sh, 공식 Dockerfile 존재 |
| 기술 스택 | Python 88% + TypeScript 8.5% — Phase 0 가정 일치 |
| Pre-record hook 공식 지원 (P2-N1 사전 평가) | **사실상 미존재** | `pre_llm_call/post_llm_call/on_session_*` 4종만 존재. v0.12.0에서 "BOOT.md 빌트인 hook 제거" |
| Sessions export 공식 명령 (P2-N2 사전 평가) | **PARTIAL** | `hermes sessions export OUT` 존재, `hermes profile export` 별도 존재. skills/memory 전용 export 미문서화 |
| SQLite 단일 백엔드 (sqlite 호환 검증 사전 평가) | **POSITIVE** | `~/.hermes/state.db` 단일 파일 + `SessionDB` 클래스 (Python) → monkey-patch 가능성 존재 |
| **Redaction default OFF** (P2 신규 발견) | **CRITICAL** | v0.12.0 breaking change: `redaction.enabled: true` 명시 필요. P1·P2 가정 재검토 |

→ **Phase 0 §3.3 통과 기준 사전 평가**: P2-N1 FAIL 가능성 높음 → **§3.4 폴백 트리거 가능성 매우 높음**

---

## 2. 환경 준비

### 2.1 브랜치 + 디렉토리

```
git switch -c feature/hermes-phase0
mkdir -p docs/phase0/
```

산출:
- `docs/phase0/day1-environment-and-fact-check.md` (본 문서)

### 2.2 시스템 환경 확인

```
docker version: 29.1.3
docker compose version: v5.0.1
git: clean except .claude/settings.local.json (Task #16 잔여)
```

PoC docker-compose 파일은 본 보고서 검토 후 작성 (잘못된 PyPI 가정 수정 후).

---

## 3. Hermes v0.12.0 사실 확인

### 3.1 공식 저장소 (확인됨)

- **GitHub**: https://github.com/NousResearch/hermes-agent
- **공식 문서**: https://hermes-agent.nousresearch.com/docs
- **v0.12.0 (2026-04-30)** "The Curator release" — 자율 백그라운드 큐레이터 도입
- v0.11.0 (2026-04-23) "The Interface release" — React/Ink TUI 풀 재작성
- v0.9.0 (2026-04-13) "everywhere release" — Termux/Android, iMessage/WeChat, Fast Mode

### 3.2 기술 스택 (확인됨)

```
hermes-agent/
├── run_agent.py          # AIAgent 코어 (~12k LOC, Python)
├── model_tools.py        # Tool orchestration
├── cli.py                # Interactive CLI (~11k LOC)
├── hermes_state.py       # SessionDB (SQLite + FTS5)
├── agent/                # Provider adapters, memory, caching
├── hermes_cli/           # CLI subcommands, plugins loader
├── tools/                # Tool implementations
├── gateway/              # Messaging platform adapters
├── plugins/memory/       # honcho, mem0, supermemory 등 (MemoryProvider ABC)
├── skills/               # Built-in skills (default-on)
├── optional-skills/      # Heavier/niche skills (default-off)
├── ui-tui/               # React/Ink terminal UI
└── tests/                # ~15k 테스트, ~700 파일
```

- **언어 비율**: Python 88.0% / TypeScript 8.5% / Shell 등
- **DB**: SQLite (FTS5) — `~/.hermes/state.db`
- **Config**: `~/.hermes/config.yaml`, `~/.hermes/.env`
- **Logs**: `~/.hermes/logs/`

### 3.3 설치 방식 (확인됨, P2 v2 정정 필요)

**공식 권장**:
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**Docker**:
- 저장소에 `Dockerfile`, `docker-compose.yml`, `.dockerignore` 존재
- 터미널 백엔드 옵션: local / SSH / Daytona / Singularity / Modal / **Docker**

**PyPI 패키지**:
- `pip install hermes-agent` → **404 Not Found**
- `pypi.org/pypi/hermes-agent/json` 직접 조회로 확인

→ **P2 v2 §2.6.1 Dockerfile 정정 필요**: `pip install hermes-agent==0.12.0` 라인을 다음 중 하나로 교체
  - (a) `git clone --branch v0.12.0 https://github.com/NousResearch/hermes-agent.git && cd hermes-agent && bash scripts/install.sh`
  - (b) 공식 `Dockerfile`을 base로 하는 multi-stage 빌드
  - (c) `curl | bash` (빌드 reproducibility 손상 — 비추천)

---

## 4. P2-N1 사전 평가 — Pre-record hook

### 4.1 P2 v2 §2.1.3의 가정

```python
# hermes_redaction_hook.py (P2 v2 §2.1.3 가정)
def pre_record_hook(session_event):
    return P1_REDACTOR.scrub(session_event)

hermes.session_storage.add_pre_record_hook(pre_record_hook)
```

### 4.2 실제 v0.12.0 Hook 시스템

공식 문서 (https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks) 기준:

**존재하는 hook**:
- `pre_llm_call` — LLM 호출 **직전**
- `post_llm_call` — LLM 호출 **직후**
- `on_session_start`
- `on_session_end`

**부재하는 hook**:
- `pre_record` 또는 `before_record` — DB 기록 직전 hook **공식 API 미존재**
- `session_storage.add_pre_record_hook` 메서드 **미존재** (코드 grep 필요, 그러나 문서·릴리스노트 부재)

### 4.3 추가 정황

- v0.12.0 릴리스 노트: **"BOOT.md built-in hook removed"** — 빌트인 hook 시스템이 축소되는 추세
- Hook은 이벤트 매처(regex) + shell 명령어 기반 — Python 콜백 직접 등록이 아닌 **외부 프로세스 호출** 패러다임
- `SessionDB.append_message()` 는 SessionDB 클래스 메서드 직접 호출 (Python API)

### 4.4 우회 가능성 (Phase 0 Day 2에서 검증 대상)

| 우회 | 가능성 | 헌법 정합성 |
|-----|------|------------|
| `SessionDB.append_message` monkey-patch | HIGH (Python) | △ 비공식, 업데이트 시 깨짐 위험 |
| SQLite trigger (DB 레벨 redaction) | MEDIUM | ○ DB 레벨 강제 |
| `pre_llm_call` hook으로 LLM 입출력 정화 | HIGH | △ 메시지 저장 자체는 막지 못함 |
| `redaction.enabled: true` (Hermes 자체 redaction) | HIGH | ○ 공식 지원, 단 v0.12.0 default OFF |

→ **§4 핵심**: P2 v2 §2.1.3 코드는 **그대로 동작 불가**. 그러나 우회로 다수 존재. P2 v2의 "공식 지원" 요구사항을 어떻게 정의하느냐에 따라 PASS/FAIL 분기.

### 4.5 Day 2 검증 계획

1. Hermes 소스 clone → `grep -r "pre_record\|add_pre_record_hook\|before_record"` 실행
2. `SessionDB` 클래스 정의 확인 → `append_message` 메서드 시그니처 + monkey-patch 가능성
3. `pre_llm_call` hook으로 우회 시 헌법 8조 정합성 평가 (메시지 저장 자체는 평문이므로 §2.1 SQLCipher 의존도 증가)

---

## 5. P2-N2 사전 평가 — Sessions/Skills/Memory Export

### 5.1 확인된 명령

| 명령 | 출력 | 포함 항목 |
|------|------|---------|
| `hermes sessions export OUT` | JSONL | 세션 메시지 |
| `hermes profile export NAME` | tar.gz | 프로필 (config + 추정: state) |

### 5.2 미확인 항목

- Skills 단독 export 명령 (예: `hermes skills export`)
- Memory 단독 export 명령 (예: `hermes memory export`)
- `hermes sessions export`가 skills 정의를 포함하는지 (FTS5 인덱스 + 스킬 바이너리 포함 여부)

### 5.3 우회 가능성

- Skills는 `skills/` 디렉토리 파일 시스템 기반 → tar로 백업 가능 (코드 + SKILL.md)
- Memory는 plugin별로 다름 (honcho/mem0/supermemory) → 각 plugin의 자체 export 메커니즘 사용
- `~/.hermes/state.db` 자체를 SQLCipher 백업으로 처리 (가장 안전)

### 5.4 Day 3 검증 계획

1. 격리 환경에서 Hermes 부팅 → 인위 skill 1개 + memory 1개 생성
2. `hermes sessions export test.jsonl` 실행
3. `jq` 로 JSONL 파싱 → skills/memory 포함 여부 확인
4. 미포함 시 `hermes profile export` 또는 `state.db` 직접 백업 검토

---

## 6. sqlite import 호환 사전 평가

### 6.1 긍정 신호

- Python 88% 코드베이스 → monkey-patch 가능
- 단일 `~/.hermes/state.db` 파일 → SQLCipher 적용 대상 명확
- `SessionDB` 클래스가 `import sqlite3` 사용 추정 → `pysqlcipher3.dbapi2 as sqlite3` 치환 가능

### 6.2 우려 신호

- TypeScript/React (UI-TUI) 비중 8.5% — UI가 별도 sqlite 사용 시 monkey-patch 불완전
- `agent/`, `gateway/` 등 다수 모듈이 독립적으로 sqlite import 가능성

### 6.3 Day 4 검증 계획

1. Hermes 소스 grep: `import sqlite3` / `from sqlite3` 호출 위치 전수
2. `pysqlcipher3` Docker 이미지 빌드
3. `sys.modules['sqlite3'] = pysqlcipher3.dbapi2` 적용 후 Hermes 부팅
4. `~/.hermes/state.db` 강제 sqlite3로 열기 → 거부 (암호화 동작 확인)

---

## 7. 신규 발견 — Redaction Default OFF (CRITICAL)

### 7.1 사실

v0.12.0 RELEASE_v0.12.0.md:
> Secret redaction "default flipped to off" (now requires explicit `redaction.enabled: true` opt-in)

### 7.2 영향

- P1 v2 §8.2 RedactionFilter는 P1 facade 레벨 → **영향 없음** (Hermes 자체 redaction과 별개)
- P2 v2 §2.1.3 pre-record redaction → 우리는 어차피 facade 경유이므로 별개
- 그러나 **Hermes 자체 redaction을 추가 안전망으로 사용하려면** `redaction.enabled: true` 명시 필요

### 7.3 권고

- P2 v2 §2.1.3 또는 §2.6.2에 "Hermes config: `redaction.enabled: true` 강제" 항목 추가
- 이중 redaction (P1 facade + Hermes 자체) 으로 안전망 강화

---

## 8. P2 v2 정정 필요 항목 (Day 5 ADR 정리 시 반영)

| 항목 | 현 P2 v2 | 정정 |
|------|---------|------|
| §2.6.1 Dockerfile | `pip install hermes-agent==0.12.0` | git clone + install.sh 또는 공식 Dockerfile base |
| §2.1.3 pre-record hook | `add_pre_record_hook` (가정) | Day 2 검증 후 결정: monkey-patch / SQLite trigger / pre_llm_call / redaction.enabled |
| §2.6.2 docker-compose | hermes 자체 build | 공식 Dockerfile 참조 후 격리 6항목 오버레이 |
| 신규 §X | 없음 | Hermes config `redaction.enabled: true` 강제 |

---

## 9. §3.4 폴백 트리거 사전 평가

### 9.1 P2 v2 §3.3 통과 기준 (재인용)

| 검증 | PASS 기준 | Day 1 사전 평가 |
|-----|----------|--------------|
| P2-N1 | pre-record hook 공식 지원 + 호출 동작 확인 | **사실상 FAIL** (공식 hook 미존재) |
| P2-N2 | sessions/skills/memory 모두 export 포함 | **PARTIAL** (sessions ○, skills/memory 별도 처리 필요) |
| sqlite | monkey-patch 정상 동작 + 부팅 + 암호화 | **잠정 PASS 가능성** (Day 4 검증) |

### 9.2 의사결정 옵션

**옵션 A — Day 2~4 그대로 진행하여 실측 확인**
- 장점: 우회 가능성 (monkey-patch / SQLite trigger / pre_llm_call) 정확 평가
- 단점: P2-N1 "공식 지원" 부재가 확실시되면 Day 2~4 작업이 헛수고

**옵션 B — 즉시 §3.4 폴백 검토 (ADR-011 작성)**
- 장점: 잘못된 가정 위에 PoC 환경 구축 회피
- 단점: 우회 가능성을 검증하지 않은 결정 (P2 v2 \"공식 지원\" 요구의 강도가 불명확)

**옵션 C — P2 v2 \"공식 지원\" 요구사항 재정의 (사용자 결정 필요)**
- "공식 지원" = 공식 hook API 존재만 인정 → P2-N1 FAIL → §3.4 폴백
- "공식 지원" = monkey-patch/trigger 등 우회 포함 → Day 2 실측 후 결정
- 이 결정은 헌법 정합성 + 유지보수성 트레이드오프

### 9.3 권고

> **옵션 C → 사용자 결정 → 옵션 A 또는 B 진입**
>
> P2-N1의 "공식 지원" 요구는 ADR-008 부록 A (3+1 합의 시 작성)에서 도출된 비협상 조건. 이를 완화할지 여부는 **합의 수준의 결정** — 단독 결정 부적절. 사용자 답변 후 재진입.

---

## 10. 다음 단계 후보

### 10.1 사용자 결정 후

**A안 (공식 지원 = 엄격)**:
1. 즉시 §3.4 폴백 → ADR-011 작성 (P2-N1 FAIL 명시)
2. Option A (LiteLLM 우선) 또는 C-대안2 (Claude Code 메모리 + LiteLLM 3~5일 PoC) 선택
3. Phase 0 Task #2~5 폐기, Phase 1 진입 보류

**B안 (공식 지원 = 우회 포함)**:
1. P2 v2 §2.1.3 정정안 작성 (4개 우회 옵션 중 선정)
2. Day 2 실측: SessionDB 코드 grep + monkey-patch PoC
3. Day 3~4 그대로 진행
4. Day 5 종합 결정

**C안 (사실 더 모음)**:
1. Hermes 저장소 clone + 코드 직접 grep으로 hook API 정밀 조사
2. 1~2시간 추가 후 A/B 재선택

---

## 11. 산출 파일 (본 세션)

- `docs/phase0/day1-environment-and-fact-check.md` (본 보고서)
- 브랜치: `feature/hermes-phase0` (생성 완료, 미커밋)

## 12. 미해결 결정 (사용자 답변 대기)

| ID | 안건 | 옵션 |
|----|------|------|
| P0-D1 | P2-N1 "공식 지원" 정의 | (A) 엄격 — 공식 hook API만 / (B) 우회 포함 / (C) 사실 더 수집 |
| P0-D2 | Day 1 산출 커밋 시점 | 즉시 / 사용자 결정 후 |

---

**Day 1 종료 시각**: 2026-05-05
**다음 세션 진입점**: P0-D1 결정 후 Day 2 진행 또는 §3.4 폴백

---

## 13. 옵션 C 검증 결과 — 코드 직접 grep + 공식 docs 정밀 (2026-05-05 추가)

### 13.1 검증 방법

- Hermes main HEAD clone: `/tmp/hermes-phase0/hermes-agent` (1390 Python 파일, v0.12.0 실효 동등)
- 공식 docs 풀 fetch: Event Hooks / Session Storage / Architecture
- 코드 grep: 결정적 키워드 4종

### 13.2 P2-N1 (pre-record hook) — **FAIL 확정**

#### 코드 grep 결과
```
$ grep -rn "pre_record\|add_pre_record_hook\|before_record" --include="*.py"
0건
```

#### `VALID_HOOKS` 권위 정의 (`hermes_cli/plugins.py:78`)

```python
VALID_HOOKS: Set[str] = {
    "pre_tool_call", "post_tool_call",
    "transform_terminal_output", "transform_tool_result",
    "pre_llm_call", "post_llm_call",
    "pre_api_request", "post_api_request",     # ← docs에 없던 신규 hook 발견
    "on_session_start", "on_session_end",
    "on_session_finalize", "on_session_reset",
    "subagent_stop",
    "pre_gateway_dispatch",                     # auth 전, DB 저장 훨씬 전
    "pre_approval_request", "post_approval_response",
}
```

**핵심**: 15종 hook 중 **DB 기록 직전 가로채기 hook은 0개**. `SessionDB.append_message`는 직접 SQL INSERT를 실행하며 콜백 등록 인자가 없음 (`hermes_state.py:1222`).

#### `SessionDB.append_message` 시그니처 확인 (`hermes_state.py:1222`)

```python
def append_message(self, session_id, role, content=None, tool_name=None,
                   tool_calls=None, ..., codex_message_items=None) -> int:
    # JSON 직렬화 → INSERT INTO messages (...) VALUES (...)
    # 콜백/hook 등록 메커니즘 부재
```

→ **결론**: P2 v2 §2.1.3 코드 (`hermes.session_storage.add_pre_record_hook(...)`) **공식 API 미존재 확정**

### 13.3 결정적 신규 발견 — Hermes 자체 redaction 시스템

#### 사실
- `cli.py:585` `redact = security_config.get("redact_secrets")` — 자체 redaction 활성화 분기
- `tests/hermes_cli/test_redact_config_bridge.py` — config + 환경변수 두 경로 모두 동작 검증
- 활성화 방법:
  - `~/.hermes/config.yaml` → `security.redact_secrets: true`
  - 또는 환경변수 `HERMES_REDACT_SECRETS=true` (config 우선)
- **v0.12.0 default OFF** (breaking change) — 명시 활성화 필수

#### 의미
P2 v2 §2.1.3의 본래 요구는 **"DB에 평문 비밀 저장 차단"**. 외부 hook 형태에 집착하지 않는다면, Hermes 자체 redaction이 이를 충족한다. 즉, P2-N1은 "외부 hook 형태"가 아니라 **"redaction 메커니즘 공식 지원"** 으로 재해석 가능.

### 13.4 P2-N2 (export skills/memory) — **PARTIAL 확정**

#### 코드 확인 (`hermes_state.py:1981`)
```python
def export_session(self, session_id) -> Dict:
    return {**session, "messages": messages}   # 세션+메시지만

def export_all(self, source=None) -> List[Dict]:
    return [{**session, "messages": messages} for session in sessions]
```

→ `export_all`은 sessions+messages 한정, **skills/memory 미포함 확정**

#### 우회 (Day 3에서 검증 예정)
- Skills: `~/.hermes/skills/` 또는 `skills.config.<key>` 디렉토리 백업 (파일 시스템 기반)
- Memory: plugin별 자체 export (honcho/mem0/supermemory) 또는 `state.db` raw 백업
- 또는 `hermes profile export NAME` (tar.gz) — 검증 대상

### 13.5 sqlite import 호환 — **잠정 PASS, 단 대량 patch 필요**

#### 코드 grep 결과 (18개 파일)
```
hermes_state.py:21:                          import sqlite3   ← 핵심 (SessionDB)
hermes_cli/backup.py:15:                     import sqlite3
hermes_cli/kanban_db.py:78:                  import sqlite3
gateway/platforms/api_server.py:34:          import sqlite3
plugins/memory/retaindb/__init__.py:28:      import sqlite3
plugins/memory/holographic/store.py:7:       import sqlite3
plugins/kanban/dashboard/plugin_api.py:33:   import sqlite3
optional-skills/mcp/.../database_server.py:5: import sqlite3
+ 10개 (대부분 tests/, scripts/)
```

→ **모두 `import sqlite3` 형태** → `sys.modules['sqlite3'] = pysqlcipher3.dbapi2` 단일 patch로 처리 가능 가설.
→ **단, 가장 이른 import 시점 전 적용 필수** (sitecustomize.py 또는 entry-point pre-import).
→ Day 4 실측 시: cli entry point + sitecustomize 조합 PoC.

### 13.6 종합 — P2-N1 재해석에 따른 분기

#### 옵션 A (엄격 — P2 v2 §2.1.3 그대로 요구)
- 결과: **P2-N1 FAIL 확정**
- 다음: §3.4 폴백 → ADR-011 작성 → Option A (LiteLLM 우선) 또는 C-대안2 (Claude Code 메모리 + LiteLLM)
- 비용: P2 작업 폐기, 1~2주 손실

#### 옵션 B (본질 — "DB 평문 저장 차단" 충족)
- 경로: **Hermes 자체 redaction (`security.redact_secrets: true`) + SQLCipher + 보조 monkey-patch**
- 정정안 (P2 v2 §2.1.3):
  ```yaml
  # ~/.hermes/config.yaml (Docker secret 또는 마운트)
  security:
    redact_secrets: true   # v0.12.0 breaking change 대응 (default OFF)
  ```
  + 검증: 환경변수 echo LLM 호출 → DB에 평문 저장 안 됨 (Hermes 자체 redaction)
  + 보조 (선택): `SessionDB.append_message` monkey-patch (안전망, 비공식)
- 추가 충족 조건:
  - Phase 1 회귀 테스트에 "redaction 활성화 강제" 검증 추가
  - Phase 1 차단조건 #1 검증 항목에 "Hermes config redact_secrets=true 확인" 추가
  - 자동 롤백 트리거 T11 신설: redact_secrets 비활성화 감지 시 자동 정지
- 의미: ADR-008 부록 A의 "비협상 조건 R1" 해석 갱신 → **3+1 합의 재가동 필요 가능성**

### 13.7 권고

**옵션 B로 진입 + 옵션 B의 변경 자체에 대한 단축 3+1 합의 (Reviewer-only) 가동**

근거:
1. P2 v2 §2.1.3의 본래 의도는 "DB 평문 저장 차단"이지 "외부 hook 형태"가 아님 (ADR-008 부록 A 재독)
2. Hermes 자체 redaction이 동등하거나 우월 (공식 지원, 업데이트 안전성)
3. 단, "비협상 조건 해석 갱신"은 단독 결정 부적절 — 단축 합의로 검증
4. 옵션 A (즉시 폴백)는 검증 없이 P2 폐기 — 정보 손실

### 13.8 갱신된 미해결 결정

| ID | 안건 | 옵션 |
|----|------|------|
| P0-D1 (갱신) | P2-N1 결정 — 외부 hook 형태 vs 본질 충족 | (A) 엄격 → §3.4 폴백 / **(B) 본질 → 정정안 + 단축 합의** |
| P0-D2 | Day 1 산출 커밋 시점 | 즉시 / P0-D1 결정 후 일괄 |
| P0-D3 (신규) | 옵션 B 진입 시 단축 3+1 합의 가동 여부 | 가동 / 사용자 단독 결정 |
