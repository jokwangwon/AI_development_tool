# Hermes Agent 도입 설계 (Hermes Adoption Design)

> **Option B (Hermes 메인 오케스트레이터 + 다중 LLM 서브) 단계 도입. 6개 차단조건 충족 메커니즘 + Phase 1/2/3 마이그레이션 + 롤백 기준 + 검증 메트릭**

**최종 수정**: 2026-05-04
**상태**: 초안 (3+1 합의 대기)
**상위 결정**: `ADR-008-hermes-adoption-decision.md` (Option B 채택)
**관련 ADR**: ADR-009 (자체 Adapter v2.0 진입조건)
**관련 설계**: `llm-providers-design.md` (P1 v2 — LiteLLM facade), `multi-agent-system-design.md`, `harness-engineering-design.md`, `environment-and-docker-design.md`
**관련 합의**: `review/3plus1-consensus-2026-05-04-hermes.md`, `review/3plus1-consensus-2026-05-04-p1-llm-providers.md`

---

## 1. 개요

### 1.1 목적

ADR-008에서 채택한 **Option B (Hermes 메인 오케스트레이터 + Claude/GPT 등 서브 LLM)**의 **단계별 도입 메커니즘**을 명세한다. 본 문서는 Hermes를 안전하게 도입하는 **운영 매뉴얼**이며, 6개 차단조건 충족 방법·Phase 진입 조건·롤백 기준·검증 메트릭을 모두 포함한다.

### 1.2 범위

| 포함 | 제외 |
|------|------|
| Hermes 설치·구성·운영 메커니즘 | LLM Provider 추상화 (P1 위임) |
| 6개 차단조건 충족 검증 | 신규 Hermes 스킬 작성 가이드 (별도 문서) |
| Phase 1/2/3 단계 + 진입·exit 기준 | Phase 4+ (전면 이전) — 본 문서 범위 외 |
| 롤백 기준 + 데이터 복구 절차 | Hermes 자체 사용법 (Hermes 공식 문서 참조) |
| 운영 메트릭·대시보드 | 비-Claude LLM 자체 운영 (P1 위임) |

### 1.3 전제 조건

도입 전 다음이 충족되어야 한다:

1. **P1 (LLM Provider Facade) MVP 완료** — Hermes의 모든 LLM 호출이 P1 facade를 거쳐야 함
2. **`llm-providers.yaml` 검증 통과** — Min 2 active + 동일 type 강제 + redaction 필터 활성화
3. **OAuth 직결 금지 정책 확정** — Hermes는 API 키 경로만 사용 (Phase 1)
4. **Docker 격리 환경 준비** — Hermes는 컨테이너 격리 환경에서만 실행
5. **백업 절차 확립** — Phase 진입 전 현재 시스템 상태(Claude Code 설정·CLAUDE.md·.claude/) 백업

### 1.4 ADR-008과의 관계

ADR-008은 **무엇을(What)** 결정했고, 본 P2는 **어떻게(How)**를 명세한다.

| ADR-008 결정 | P2 구현 메커니즘 |
|-------------|----------------|
| Option B 채택 | §3~5 Phase 1/2/3 단계 |
| 6개 차단조건 비협상 | §2 차단조건별 충족 메커니즘 |
| Phase 종료마다 재평가 | §6 롤백 기준 + §7 검증 메트릭 |
| R1·R2·A-meta CRITICAL 위험 | §2.1 (R1), §2.2 (R2), §2.6 (A-meta), §9 위험 등록부 |
| 미충족 시 Option A 자동 폴백 | §6.1 자동 롤백 트리거 |

### 1.5 P1과의 관계

본 P2는 **P1 facade를 전제**로 동작한다:

```
[Hermes]                           [본 P2 범위]
   ↓ LLM 호출
[P1 LLMFacade]                     [P1 범위]
   ↓ litellm.Router
[Anthropic / OpenAI / Ollama / ...]
```

Hermes 자체 SDK 호출(`anthropic`, `openai` 등)을 직접 import하면 안 된다 — P1의 depcruise 룰로 차단됨. Hermes 내부에서 LLM이 필요할 때 **반드시 P1 facade 경유**.

### 1.6 하네스 위치

```
Layer 0:   CLAUDE.md (가이드 — 도입 정책)
Layer 0.5: 본 P2 (가이드 — 단계·차단조건·롤백 기준)
Layer 1~3: 기존 hooks 유지 (Phase 3까지)
Layer 4:   CI (Phase 진입 조건 자동 검증)
Layer 5:   3+1 합의 (Phase 진입·exit·롤백 결정)
Layer 6:   사용자 검토 (각 Phase 종료마다)
```

---

## 2. 6개 차단조건 충족 메커니즘

각 차단조건은 **비협상**이며, 미충족 시 해당 Phase 진입 자동 차단 (§6.1 자동 롤백).

### 2.1 차단조건 #1 — SQLCipher 암호화 + redaction 필터 (R1 차단)

**위험**: Hermes 학습루프(SQLite FTS5)에 사용자 코드/응답/환경변수가 평문 영구 누적 → 헌법 제8조 직접 위반

**충족 메커니즘**:

#### 2.1.1 SQLite → SQLCipher 전환

ADR-008 부록 A.2 검증 결과: Hermes는 ChromaDB 미사용, SQLite + FTS5 단일. 암호화 단순화.

```bash
# Phase 1 진입 시 자동 실행 스크립트 (개략)

# Step 1: Hermes 설치 (격리된 worktree)
cd /isolated/hermes-poc
git clone https://github.com/NousResearch/hermes-agent.git
# 버전 핀 (§2.3)
git checkout v0.12.0

# Step 2: SQLCipher 빌드 (Hermes는 표준 sqlite3 의존 — 패치 필요)
# 옵션 A: pysqlcipher3 wrapper로 sqlite3 인터셉트
pip install pysqlcipher3
# 옵션 B: LUKS 볼륨에 ~/.hermes 마운트 (전체 디스크 암호화 의존)

# Step 3: HERMES_DB_KEY 환경변수로 암호화 키 주입
export HERMES_DB_KEY=$(openssl rand -hex 32)
# 키는 시크릿 매니저 (vault/sops) 관리 — Phase 1은 평문 env 허용 단 .env에 저장 금지
```

#### 2.1.2 Redaction 필터 (Hermes 기록 시점)

P1의 `RedactionFilter`(P1 §8.2)를 Hermes의 LLM 호출 callback에 적용. 단 Hermes 자체가 직접 디스크에 기록하는 경로(예: `hermes sessions`)는 **별도 redaction 훅 필요**:

```python
# hermes_redaction_hook.py — Hermes 학습루프 기록 직전 호출
def pre_record_hook(session_event):
    # P1 RedactionFilter 재사용
    return P1_REDACTOR.scrub(session_event)

# Hermes 설정에 등록
hermes.session_storage.add_pre_record_hook(pre_record_hook)
```

**미해결 검증**: Hermes가 pre-record hook을 공식 지원하는지 검증 필요 (ADR-008 부록 A.2의 "skills/memory export 범위" 추가 검증과 같이 Phase 1 진입 직전 확인).

#### 2.1.3 검증 방법

```
✅ Phase 1 exit 조건:
  1. ~/.hermes/state.db를 강제로 sqlite3로 열어 보면 거부됨 (SQLCipher 동작 확인)
  2. 의도적으로 환경변수 echo를 포함한 LLM 호출 후 sqlcipher3로 db 검사 — echo가 redaction 처리됨
  3. 전체 디스크 탈취 시뮬레이션 (db 파일을 다른 머신으로 복사) → 키 없이 열기 불가
```

#### 2.1.4 미충족 시 동작

```
조건 #1 미충족 → Phase 진입 자동 차단
   → 로그: "차단조건 #1 SQLCipher 미충족 → Hermes 도입 NO-GO → Option A 자동 폴백"
   → ADR-008 자동 폴백 절차 트리거
```

---

### 2.2 차단조건 #2 — JSONL export 표준 + 마이그레이션 경로 (R2 차단)

**위험**: Hermes 자체가 새 lock-in 레이어 — 누적 학습 결과 Hermes 떠나면 손실

**충족 메커니즘**:

#### 2.2.1 공식 export 명령 활용

ADR-008 부록 A.2 검증 결과: `hermes sessions export backup.jsonl` 공식 지원.

```bash
# 정기 백업 — cron으로 매일 실행
hermes sessions export ~/backups/hermes-$(date +%Y%m%d).jsonl
```

#### 2.2.2 Skills/Memory export 검증 (미해결 → Phase 1 진입 직전 확인)

`hermes sessions export`가 sessions 외에 **skills**와 **agent-curated memory**까지 포함하는지 명확하지 않음. Phase 1 진입 직전 다음 검증:

```
✅ 검증 작업 (Phase 1 진입 직전):
  1. 인위적으로 skill 1개 + memory 1개 생성
  2. hermes sessions export → JSONL 검사
  3. skill·memory 포함 여부 확인
  4. 미포함이면:
     a. hermes 추가 명령 탐색 (예: hermes skills export, hermes memory export)
     b. 직접 SQLite 쿼리 (~/.hermes/state.db에서 추출)
     c. 모든 경로 실패 시 차단조건 #2 NO-GO → Option A 폴백
```

#### 2.2.3 마이그레이션 경로 정의

```
[Hermes에서 빠져나갈 시나리오 — 사전 정의]

Scenario A: Hermes → Claude Code 복귀 (전체 롤백)
  Step 1: hermes sessions export full-backup.jsonl
  Step 2: 변환 스크립트 (jsonl → CLAUDE.md/.claude/sessions/)
  Step 3: Claude Code에서 import + 검증

Scenario B: Hermes → 다른 오케스트레이터 (예: 자체 Python)
  Step 1: hermes sessions export
  Step 2: JSONL 표준이므로 다른 도구가 자체 import 작성

Scenario C: Hermes 메이저 업데이트 (Hermes 유지하나 데이터 보존)
  Step 1: 업데이트 전 export
  Step 2: 업데이트 후 import (Hermes schema_version 호환성 확인)
```

각 시나리오의 변환 스크립트는 `scripts/hermes-migration/` 하위에 작성.

#### 2.2.4 검증 방법

```
✅ Phase 1 exit 조건:
  1. 매일 자동 백업 동작 확인 (3일 연속)
  2. Scenario A 시뮬레이션: 임시 데이터 → export → Claude Code 복원 → 검증
  3. JSONL 파일이 표준 JSON Lines 포맷 준수 (jq 등으로 파싱 가능)
```

#### 2.2.5 미충족 시 동작

```
조건 #2 미충족 (export 누락 또는 마이그레이션 스크립트 실패)
  → 학습 데이터 잠금 위험 → Hermes 도입 자동 NO-GO → Option A 폴백
```

---

### 2.3 차단조건 #3 — v0.x 버전 핀 + 회귀 테스트 + 카나리 환경 (R3 차단)

**위험**: Hermes 7-10일 릴리스 주기 → 매주 깨짐 가능성

**충족 메커니즘**:

#### 2.3.1 버전 핀

```yaml
# hermes-version.yaml (단일 진실 원천)
version: v0.12.0                # 절대 floating 금지
checksum: sha256:abc123...      # 다운로드 무결성
release_notes_url: https://github.com/NousResearch/hermes-agent/releases/tag/v0.12.0
last_audit: 2026-05-04          # 마지막 감사 일자
audit_status: passed            # passed | pending | failed
next_audit_due: 2026-08-04      # 분기마다 갱신
```

설치 스크립트는 본 yaml만 신뢰. `hermes update`, `pip install --upgrade hermes` 같은 명령은 운영 환경에서 **금지** (정책으로 강제).

#### 2.3.2 회귀 테스트 슈트

```
tests/hermes/regression/
├── test_session_export.py        # JSONL export 무결성
├── test_skill_creation.py        # 스킬 생성·실행
├── test_oauth_flow.py            # API 키 경로 (OAuth는 Phase 2+)
├── test_sqlcipher_encryption.py  # DB 암호화
├── test_redaction.py             # 비밀값 echo 차단
├── test_litellm_facade.py        # P1 facade 경유 검증
└── test_3plus1_consensus.py      # Phase 2: 다중 LLM 합의
```

각 테스트는 **현재 핀 버전에 대한 기대 동작**을 명세. 버전 업데이트 시 모든 테스트 통과해야 카나리 진입.

#### 2.3.3 카나리 환경

```
[Hermes 환경 분리]

production: 현재 핀 버전 (v0.12.0) — 사용자가 일상 사용
canary:     새 버전 후보 (v0.13.0) — 회귀 테스트 통과 후 1주 격리 운영
                                    + 메트릭 비교 (응답 시간·비용·에러율)
```

카나리에서 1주 무사고 → production으로 승격 (별도 `hermes-version.yaml` 갱신 PR + 3+1 합의 또는 Reviewer-only).

#### 2.3.4 미충족 시 동작

```
조건 #3 미충족 (회귀 테스트 미작성 또는 카나리 환경 미구성)
  → Phase 진입 자동 차단
  → 또는 운영 중 발견 시 Hermes 사용 즉시 정지 → Option A 폴백
```

---

### 2.4 차단조건 #4 — provider 어댑터 1개 추상화 (P1 위임)

본 차단조건은 **P1 (`llm-providers-design.md`)에 위임**되어 있다. P1의 `LLMFacade`가 정확히 1개의 어댑터로 동작하며, depcruise 룰로 우회 차단.

본 P2의 책임:
- Hermes의 모든 LLM 호출이 P1 facade를 경유함을 검증
- Hermes 내부에 `litellm`/`anthropic`/`openai` SDK가 직접 import되지 않는지 검사
- Hermes의 자체 LLM 라우팅 로직(예: Hermes Router) 비활성화 → P1 facade로 위임

```
✅ Phase 1 exit 조건:
  1. depcruise 검사 통과 (Hermes 디렉토리 포함)
  2. 인위적 분기 코드 PR을 만들어 차단 확인
  3. Hermes 호출 로그에 P1 facade 경유 흔적 확인
```

---

### 2.5 차단조건 #5 — 최소 2 provider always-on (P1 위임)

본 차단조건도 **P1에 위임**. P1의 시작 시점 fail-fast + 런타임 재검증 + degraded 모드가 충족 메커니즘.

본 P2의 책임:
- Phase 1·2·3 각각의 active provider 구성 명시 (§3~5)
- Hermes가 단일 provider만 사용하도록 강제하는 코드/설정이 없는지 검사
- 구독 취소 시나리오를 Phase별로 시뮬레이션 (§6.3)

---

### 2.6 차단조건 #6 — Docker 격리 + egress 화이트리스트 (R9 차단)

**위험**: Hermes가 셸 실행/파일 쓰기 권한으로 동작 → 호스트 권한 노출

**충족 메커니즘**:

#### 2.6.1 Docker 컨테이너 격리

```dockerfile
# Dockerfile.hermes
FROM python:3.11-slim

# Hermes 설치 (버전 핀)
COPY hermes-version.yaml /etc/hermes/
RUN pip install hermes-agent==0.12.0

# 비-root 사용자
RUN useradd -m -s /bin/bash hermes
USER hermes
WORKDIR /home/hermes

# SQLCipher 의존성
RUN pip install pysqlcipher3

ENTRYPOINT ["hermes"]
```

```yaml
# docker-compose.hermes.yml
services:
  hermes:
    build:
      dockerfile: Dockerfile.hermes
    volumes:
      - hermes-data:/home/hermes/.hermes  # SQLCipher 암호화된 데이터
      - ${CLAUDE_CREDS_PATH}:/credentials/claude:ro  # OAuth는 Phase 2+에서, ro 마운트
    environment:
      - HERMES_DB_KEY=${HERMES_DB_KEY}    # SQLCipher 키
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    networks:
      - hermes-egress                     # 격리된 egress 네트워크
    cap_drop:
      - ALL                               # 모든 capability 제거
    read_only: true                       # 루트 파일시스템 읽기 전용
    tmpfs:
      - /tmp                              # 임시 작업 공간

networks:
  hermes-egress:
    driver: bridge
    # iptables/ufw로 egress 화이트리스트 (§2.6.2)

volumes:
  hermes-data:
```

#### 2.6.2 Egress 화이트리스트

```
[허용 도메인 — Phase 1]
- api.anthropic.com    (Claude API)
- api.openai.com       (OpenAI API)
- localhost:11434      (Ollama 로컬, 호스트 측)
- openrouter.ai        (OpenRouter, 폴백)

[차단]
- 그 외 모든 외부 통신
- 특히 Hermes 자체 텔레메트리 endpoint (NousResearch 자체 분석 서버) — 명시 차단
```

iptables 또는 호스트 방화벽으로 컨테이너 egress 제한.

#### 2.6.3 호스트 파일시스템 접근 최소화

| 마운트 | 용도 | 권한 |
|--------|------|------|
| `hermes-data` (volume) | SQLCipher 암호화 데이터 | rw (컨테이너 내부) |
| `${CLAUDE_CREDS_PATH}` | OAuth (Phase 2+) | ro |
| `/tmp` (tmpfs) | 임시 작업 공간 | rw, 컨테이너 종료 시 소멸 |
| 그 외 호스트 디렉토리 | — | 마운트 금지 |

#### 2.6.4 검증 방법

```
✅ Phase 1 exit 조건:
  1. 컨테이너 내부에서 호스트 파일 접근 시도 → 거부
  2. 화이트리스트 외 도메인 통신 시도 → 거부 (예: curl https://example.com)
  3. cap_drop 검증 (예: ping 같은 raw socket 작업 거부)
  4. read_only 검증 (루트 파일시스템 쓰기 시도 → 거부)
```

#### 2.6.5 미충족 시 동작

```
조건 #6 미충족 (격리 미구성 또는 화이트리스트 누락)
  → Phase 진입 자동 차단
```

---

## 3. Phase 1 — 검증 (1~2주)

### 3.1 목표

- Hermes 설치·구성·기본 동작 검증
- 6개 차단조건 충족 검증
- **API 키 경로만** 사용 (OAuth 직결 금지)
- **비핵심 작업**으로만 사용 (예: 문서 요약, 코드 검색)
- 메트릭 베이스라인 수집 (응답 시간·비용·에러율)

### 3.2 작업

```
Phase 1 작업 목록:

[Day 1~3: 설치·구성]
  ✓ 별도 worktree에 Hermes 격리 환경 준비
  ✓ Dockerfile.hermes + docker-compose.hermes.yml 작성
  ✓ hermes-version.yaml v0.12.0 핀
  ✓ HERMES_DB_KEY 생성 + 시크릿 매니저 등록
  ✓ SQLCipher 통합 (pysqlcipher3 또는 LUKS)
  ✓ 회귀 테스트 슈트 초안 작성 (§2.3.2)

[Day 4~7: 차단조건 검증]
  ✓ #1 SQLCipher 암호화 동작 확인 (§2.1.3)
  ✓ #2 hermes sessions export 동작 확인 + skills/memory 범위 검증 (§2.2.2)
  ✓ #3 회귀 테스트 슈트 통과 (§2.3.2)
  ✓ #4 P1 facade 경유 검증 (§2.4)
  ✓ #5 active provider 3종 검증 (Anthropic API + OpenAI API + Ollama)
  ✓ #6 컨테이너 격리 검증 (§2.6.4)

[Day 8~14: 비핵심 작업 운영]
  ✓ Hermes로 비핵심 작업 수행 (예: 문서 요약 5건, 코드 검색 10건)
  ✓ 메트릭 수집 (응답 시간·비용·에러율·폴백 발생률)
  ✓ 일일 자동 백업 동작 확인 (§2.2.1)
  ✓ Phase 1 결과 리포트 작성
```

### 3.3 Phase 2 진입 조건 (Phase 1 exit 기준)

다음 모두 충족해야 Phase 2 진입 가능:

| # | 조건 | 검증 방법 |
|---|------|---------|
| 1 | 6개 차단조건 모두 충족 | §2.1~2.6 검증 방법 |
| 2 | 회귀 테스트 100% 통과 | CI 자동 |
| 3 | 비핵심 작업 5건 이상 무사고 완료 | 작업 로그 |
| 4 | 일일 백업 7일 연속 무사고 | 백업 로그 |
| 5 | 메트릭 베이스라인 수집 (응답·비용·에러) | 대시보드 |
| 6 | OAuth 직결 0건 (API 키 경로만 사용) | 호출 로그 분석 |
| 7 | depcruise 검사 통과 (P1 facade 경유) | CI 자동 |
| 8 | 사용자 수동 승인 | Phase 1 결과 리포트 검토 후 |

미충족 시 Phase 1 연장 또는 Option A 폴백.

### 3.4 Phase 1 메트릭

```
[수집 항목]
- 응답 시간: P50/P95/P99 (alias별)
- 비용: provider별 누적 (월 환산)
- 에러율: 전체/provider별
- 폴백 발생률: alias별
- OAuth 호출 수 (목표: 0)
- 카나리 vs production 차이 (있다면)

[베이스라인 기록 위치]
docs/metrics/hermes-phase1-baseline.md (Phase 종료 시 작성)
```

---

## 4. Phase 2 — 병행 (2~4주)

### 4.1 목표

- **Layer 5 (3+1 합의)만 Hermes 서브에이전트로 이전** — 가장 가치 높고 위험 낮은 워크플로
- 다중 LLM 활용: Agent A=Claude / Agent B=GPT / Agent C=Ollama
- Phase 1 메트릭과 비교하여 동등 이상 품질 확인
- 기존 Claude Code의 다른 워크플로(L0~L4, L6)는 그대로 유지

### 4.2 작업

```
Phase 2 작업 목록:

[Week 1: 3+1 합의 Hermes 이식]
  ✓ Hermes 서브에이전트 정의 (Agent A/B/C/Reviewer)
  ✓ 각 에이전트의 LLM alias 매핑 (P1 routing)
  ✓ Hermes 합의 워크플로 작성 (Phase 0~4 재현)
  ✓ Claude Code 합의 워크플로와 병렬 실행 가능 구조

[Week 2: 실 합의 수행 + 비교]
  ✓ 실제 안건 5개에 대해 Claude Code 합의 + Hermes 합의 동시 실행
  ✓ 결과 품질 비교 (사용자 평가)
  ✓ 다중 LLM의 메타 한계 해소 효과 측정

[Week 3~4: 안정화]
  ✓ 발견된 문제점 수정 (스킬 보강, 라우팅 조정)
  ✓ Phase 2 메트릭 수집
  ✓ Phase 3 진입 가능성 평가
```

### 4.3 Phase 3 진입 조건 (Phase 2 exit 기준)

| # | 조건 | 임계값 |
|---|------|-------|
| 1 | Hermes 합의 결과 품질 ≥ Claude Code 합의 | 사용자 평가 5건 모두 ≥ 동등 |
| 2 | 응답 시간 (전체 합의 종료까지) | Claude Code 대비 ±30% 이내 |
| 3 | 비용 (전체 합의당) | 측정값 ≤ Phase 1 베이스라인의 1.5배 (다중 LLM 사용으로 일부 증가 허용) |
| 4 | 메타 한계 해소 효과 측정 | 다중 LLM이 단일 Claude 합의 대비 더 풍부한 대안 제시 (정성적, 사용자 평가) |
| 5 | Phase 1 차단조건 6개 유지 | §2 모두 |
| 6 | OAuth 사용 (Phase 2부터 standby → active 검토 가능) | 사용 시 §2.5 + P1 §7 조건 충족 |
| 7 | 운영 중 사고 0건 | 사고 로그 |
| 8 | 사용자 수동 승인 | Phase 2 결과 리포트 검토 |

### 4.4 Phase 2 메트릭

Phase 1 메트릭에 추가:

```
- 합의 결과 품질 (사용자 평가 1~5점)
- 합의 종료까지 응답 시간 (Phase 0~4 전체)
- LLM 모델별 응답 시간·비용·에러율 (다중 LLM)
- 메타 한계 해소 정성 평가 (Reviewer가 단일 모델 vs 다중 모델 결과 비교)
```

---

## 5. Phase 3 — 확장 (조건부)

### 5.1 목표

- **Hook 계층 (L1~L3)을 Hermes에서 재구축** — Claude Code의 PostToolUse/PreCommit hook을 Hermes 환경으로 이전
- Provider 어댑터 본격 적용 (P1 facade의 활용 폭 확대)
- 기존 Claude Code 워크플로 일부를 Hermes로 점진 전환

### 5.2 작업

```
Phase 3 작업 목록:

[Week 1~2: Hook 재구축 PoC]
  ✓ Claude Code PostToolUse → Hermes 등가물 (file watcher 외부 + Hermes 스킬)
  ✓ Claude Code PreCommit → git pre-commit (Layer 3 그대로 유지)
  ✓ Hook 강제력 비교 (Claude Code vs Hermes 환경)
  ✓ 강제력 손실분 보완 메커니즘

[Week 3+: 점진 전환]
  ✓ 한 번에 1~2개 워크플로씩 Hermes로 이전
  ✓ 각 이전 후 1주 모니터링 → 안정성 확인 후 다음 이전
```

### 5.3 Phase 3 진입 조건

매우 까다롭게 게이팅:

| # | 조건 | 임계값 |
|---|------|-------|
| 1 | Phase 2 exit 조건 모두 충족 | §4.3 |
| 2 | Hook 재구축 PoC 성공 | watchexec 또는 등가 도구로 Layer 1 강제력 ≥ 80% 재현 |
| 3 | OAuth 의존 제거 또는 §2.5 + P1 §7 완전 충족 | 사용량 분석 |
| 4 | Phase 2 메트릭 ≥ 현 시스템 | 4주 연속 메트릭 동등 이상 |
| 5 | 6개 차단조건 모든 Phase에서 유지 | §2 |
| 6 | 사용자 명시 승인 + 외부 검증 권장 (메타 한계) | 외부 LLM 또는 사람 |

### 5.4 Phase 3 메트릭

```
- Hook 강제력 (위반 차단율) — Claude Code 기준 대비
- 워크플로별 이전 성공률
- 운영 중 사고 발생률
- 롤백 횟수 (각 이전 시도)
```

---

## 6. 롤백 기준

### 6.1 자동 롤백 트리거

다음 발생 시 **즉시 자동 롤백** (Hermes 사용 정지 + Option A 폴백):

| 트리거 | 조건 | 동작 |
|--------|------|------|
| **차단조건 미충족** | 6개 중 1개라도 운영 중 위반 | Hermes 즉시 정지 + Option A 자동 폴백 + 알림 |
| **데이터 손실 위험** | SQLCipher 키 분실, 백업 3일 연속 실패 | 즉시 정지 + 데이터 복구 절차 (§6.3) |
| **보안 사고** | OAuth 토큰 유출, redaction 우회 발견 | 즉시 정지 + 토큰 회전 + 사고 분석 |
| **의존성 비호환** | LiteLLM/Hermes 메이저 비호환 (회귀 테스트 0% 통과) | 핀 버전 유지 + 카나리 차단 |
| **사용자 명시 정지** | 사용자가 "Hermes 정지" 명령 | 즉시 정지 |

### 6.2 수동 롤백 절차

```
[수동 롤백 절차]

Step 1: Hermes 사용 정지
  docker-compose -f docker-compose.hermes.yml down

Step 2: 학습 데이터 export (가능하면)
  hermes sessions export ~/backups/rollback-$(date +%Y%m%d).jsonl
  (단, SQLCipher 키 또는 컨테이너 접근이 가능한 경우만)

Step 3: 워크플로 복원
  - Phase 1 롤백: Claude Code 그대로 사용 (Hermes는 별도 worktree에 격리되어 있어 영향 없음)
  - Phase 2 롤백: 3+1 합의를 Claude Code Agent tool로 복귀
  - Phase 3 롤백: 이전한 워크플로를 Claude Code로 복귀 (이전 전 백업한 .claude/ 복원)

Step 4: 사고 보고서 작성
  docs/incidents/2026-XX-XX-hermes-rollback.md

Step 5: ADR-008 재평가 (필요 시 ADR-010 작성으로 결정 변경)
```

### 6.3 데이터 복구 (학습루프 export)

```
[Hermes 학습루프 데이터를 Claude Code 또는 다른 도구로 이관]

Scenario A: SQLCipher 키 보유 + Hermes 정상
  hermes sessions export ~/backups/full-export.jsonl
  → 변환 스크립트 (scripts/hermes-migration/jsonl_to_claude.py)
  → Claude Code의 sessions/memories에 import

Scenario B: SQLCipher 키 보유 + Hermes 비정상
  sqlcipher ~/.hermes/state.db < extract-sql-script.sql
  → JSONL 변환 → 동일 파이프라인

Scenario C: SQLCipher 키 분실 (CRITICAL — 백업으로만 복구 가능)
  ~/backups/ 의 일일 백업 사용
  최대 1일치 데이터 손실 가능
```

---

## 7. 검증 메트릭 종합표

| Phase | 메트릭 | 측정 방법 | 임계값 (Phase exit) |
|-------|--------|---------|--------------------|
| Phase 1 | 6개 차단조건 충족 | §2 검증 | 6/6 PASS |
| Phase 1 | 회귀 테스트 통과율 | CI | 100% |
| Phase 1 | 비핵심 작업 사고율 | 작업 로그 | 0건 / 5건 이상 작업 |
| Phase 1 | 일일 백업 성공률 | 백업 로그 | 7일 연속 100% |
| Phase 1 | OAuth 직결 호출 수 | 호출 로그 | 0 |
| Phase 1 | depcruise 검사 | CI | PASS |
| Phase 2 | 합의 결과 품질 | 사용자 평가 | 5/5 ≥ 동등 |
| Phase 2 | 합의 응답 시간 | 메트릭 | Claude Code 대비 ±30% |
| Phase 2 | 합의 비용 | 메트릭 | Phase 1 베이스라인 ≤ 1.5배 |
| Phase 2 | 메타 한계 해소 효과 | Reviewer 평가 | 정성적 PASS |
| Phase 2 | 운영 사고 | 사고 로그 | 0건 |
| Phase 3 | Hook 강제력 | 위반 차단 시뮬레이션 | ≥ 80% Claude Code 대비 |
| Phase 3 | 워크플로 이전 성공률 | 이전 로그 | ≥ 90% (롤백 1회 허용) |
| Phase 3 | 메트릭 안정성 | 4주 연속 측정 | Phase 2 ≥ 동등 |

---

## 8. 운영 가이드

### 8.1 일상 운영 (Phase 1+)

```
[일일]
- ~/backups/ 백업 확인 (cron 자동)
- Hermes 컨테이너 헬스체크 (docker ps)
- 메트릭 대시보드 확인

[주간]
- 회귀 테스트 슈트 실행 (CI 또는 수동)
- 비용 누적 확인 (provider별)
- 사고 로그 검토

[월간]
- 6개 차단조건 재검증 (자동화 스크립트)
- ChatGPT Pro Codex CLI ToS 변동 모니터링 (ADR-008 부록 A.1)
- LiteLLM·Hermes 릴리스 노트 검토

[분기]
- hermes-version.yaml 감사 (next_audit_due 도달 시)
- ADR-009 v2.0 진입 트리거 점검 (T1~T4)
- Phase 진입 조건 재평가 (현 Phase 메트릭이 다음 Phase 진입 조건 충족 시 사용자에게 진입 제안)
```

### 8.2 신규 스킬 추가

```
Hermes 스킬 추가는 ADR-008 R10 (self-improvement loop 오염) 위험으로 PR화·인간 게이트 필수:

Step 1: 스킬 초안 작성 (Hermes 자동 생성 또는 수동)
Step 2: PR 생성 → 코드 리뷰 (특히 모델 가정·provider 분기 검사)
Step 3: 카나리 환경에서 1주 운영
Step 4: 사용자 승인 + 3+1 합의 (큰 스킬일 경우)
Step 5: production 환경 배포
```

### 8.3 모니터링 대시보드

```
[필수 패널 — Phase 1부터]
- provider별 호출 수·비용·에러율
- 폴백 발생률
- active provider 카운트 (Min 2 검증)
- 백업 상태 (마지막 성공 시각)
- SQLCipher 키 보존 상태 (시크릿 매니저 헬스)

[Phase 2 추가]
- 합의 종료까지 시간 (P50/P95)
- LLM 모델별 응답 품질 (사용자 평가 평균)

[Phase 3 추가]
- Hook 강제력 차단율
- 워크플로별 이전 상태
```

---

## 9. 위험 등록부

### 9.1 ADR-008에서 인수한 위험

| ID | 위험 | 본 P2의 완화 |
|----|------|------------|
| R1 | 학습루프 평문 누적 | §2.1 SQLCipher + redaction |
| R2 | Hermes 자체 lock-in | §2.2 JSONL export + 마이그레이션 시나리오 |
| R3 | v0.x API 변동 | §2.3 버전 핀 + 회귀 테스트 + 카나리 |
| R4 | Claude OAuth 4종 버그 | §3 Phase 1은 API 키만, Phase 2부터 §2.5 + P1 §7 |
| R5 | Liquidity 위반 패턴 (모델명 하드코딩) | P1 위임 (depcruise) |
| R6 | 다중 자격증명 표면 확대 | §2.6.3 mount :ro + 시크릿 매니저 |
| R7 | 모델 간 응답 일관성 | P1 위임 (LiteLLM 정규화) |
| R8 | 단일 구독 의존 | P1 위임 (Min 2 active) + Phase별 active 명시 |
| R9 | Hermes 컨테이너 격리 미적용 | §2.6 Docker 격리 + egress 화이트리스트 |
| R10 | self-improvement loop 오염 | §8.2 스킬 추가 PR화 + 인간 게이트 |

### 9.2 P1 합의에서 인수한 위험

| 출처 | 위험 | 본 P2의 완화 |
|------|------|------------|
| P1 R1 | LLMRequest 스키마 결손 | P1 §4.1 (이미 적용) |
| P1 R2 | metadata raw dict | P1 §4.1, §4.2 (이미 적용) |
| P1 R3~R12 | redaction·single-flight·dry probe 등 | P1 (이미 적용), 본 P2는 P1 facade 사용 |

### 9.3 본 P2에서 신규 식별

| ID | 위험 | 등급 | 완화 |
|----|------|------|------|
| P2-N1 | Hermes pre-record hook이 공식 지원 안 될 수 있음 (§2.1.2) | HIGH | Phase 1 진입 직전 검증, 미지원 시 SQLCipher만으로 대응 또는 NO-GO |
| P2-N2 | hermes sessions export가 skills/memory 미포함 가능성 | HIGH | Phase 1 진입 직전 검증 (§2.2.2) |
| P2-N3 | SQLCipher 키 분실 → 데이터 영구 손실 | HIGH | 시크릿 매니저 + 일일 export 백업 (§2.2.1, §6.3) |
| P2-N4 | Phase 2에서 다중 LLM 합의 결과 품질 편차 | MEDIUM | 사용자 평가 게이트 (§4.3 #1) + 부분 롤백 가능 |
| P2-N5 | Phase 3 Hook 재구축 강제력 손실 | MEDIUM | §5.3 #2 80% 임계값, 미달 시 Phase 3 보류 |
| P2-N6 | 카나리 vs production 메트릭 비교 자동화 부담 | MEDIUM | Phase 1에서 수동 비교, 이후 자동화 검토 |

---

## 10. ADR 매핑

| 관련 문서 | 정합성 |
|---------|--------|
| **ADR-008** (상위 결정) | Option B 단계 도입 메커니즘 — 본 P2가 직접 구현 |
| **ADR-009** (자체 Adapter v2.0) | LiteLLM 사용 전제 (P1) — Phase 진입마다 ADR-009 트리거 점검 |
| **P1** (`llm-providers-design.md`) | 차단조건 #4·#5 위임. 본 P2는 P1 facade 전제 |
| **ADR-004** (생성 AI 확장성) | 외부 SDK 우선 — Hermes도 외부 도구로 채택 (자체 작성 아님) |
| **ADR-006** (환경 변수 + Docker) | §2.6 Docker 격리 + 환경 변수 정책 일관 |
| **multi-agent-system-design** | Phase 2의 3+1 합의 Hermes 이전 시 그대로 따름 |
| **harness-engineering-design** | Layer 1~3 hook 재구축은 Phase 3 — 그 전에는 그대로 유지 |
| **environment-and-docker-design** | §2.6 Docker 격리가 본 문서 원칙 따름 |
| **PROJECT_CONSTITUTION 제8조** | §2.1 SQLCipher + redaction이 헌법 준수 보장 |

---

## 11. 검증 항목 (3+1 합의용)

### Agent A (구현)
- [ ] 6개 차단조건 충족 메커니즘이 실제로 동작 가능한가? 특히 P2-N1, P2-N2 검증 가능성
- [ ] Phase 1/2/3 단계 의존성 그래프가 일관되는가?
- [ ] Docker 격리 + egress 화이트리스트가 Hermes 자체 텔레메트리·자동 업데이트 모두 차단하는가?
- [ ] SQLCipher 통합 (pysqlcipher3 또는 LUKS)이 실제로 구현 가능한가?
- [ ] 카나리 vs production 분리가 실 운영에서 유지 가능한가?

### Agent B (안전·품질)
- [ ] 자동 롤백 트리거 (§6.1) 5종이 모든 위험을 커버하는가? 빠진 경로?
- [ ] SQLCipher 키 분실 시나리오 (P2-N3) 완화책이 충분한가?
- [ ] OAuth credentials 마운트 권한 검증이 시작 시점·런타임 모두에서 이루어지는가?
- [ ] Hermes 자체가 가진 권한 상승 경로(예: 컨테이너 내부 셸 실행)가 §2.6.3 mount 정책으로 모두 차단되는가?
- [ ] 사고 발생 시 데이터 무결성 보존 절차가 충분한가?
- [ ] 헌법 정합성 (제3조 하네스, 제4조 합의, 제6조 모듈 독립성, 제8조 보안)

### Agent C (대안)
- [ ] Phase 1을 더 작게 쪼갤 수 있는가? (예: 차단조건 검증만 1주, 비핵심 작업 운영 1주)
- [ ] 6개 차단조건 충족 자체가 비현실적이라면 부분 도입 또는 결정 보류 옵션 재평가 필요
- [ ] Phase 2의 3+1 합의 다중 LLM 이전을 Hermes 없이 (P1 facade만으로) 달성 가능한가?
- [ ] Hermes 대신 더 단순한 도구(예: 단순 Python 스크립트 + LiteLLM)로 셀프-임프루빙 영역만 PoC 가능한가?

### Reviewer
- [ ] ADR-008 차단조건 6개 모두 본 P2에서 충족 메커니즘 명세 — PASS/FAIL
- [ ] Phase별 진입·exit 조건이 객관적으로 측정 가능 — PASS/FAIL
- [ ] 자동 롤백·수동 롤백·데이터 복구 절차 완비 — PASS/FAIL
- [ ] P2-N1·N2 (검증 미완) 항목이 Phase 진입 직전 게이트로 명시 — PASS/FAIL
- [ ] ADR-008·P1·ADR-004와 정합 — PASS/FAIL
- [ ] 메타 한계 보정 (3 Claude 에이전트 → Hermes 친화 가능성) 적용 후 평가

---

## 12. 미해결 결정 (사용자 입력 필요)

1. **SQLCipher 통합 방법**: pysqlcipher3 wrapper vs LUKS 볼륨 — 운영 환경 (개인 머신 vs 서버)에 따라 결정
2. **시크릿 매니저 선택**: vault / sops / 평문 .env (개발용만) — 보안 요구 수준에 따라
3. **카나리 vs production 환경 분리 수준**: 별도 호스트 / 별도 컨테이너 / 별도 worktree만
4. **Phase 진입 승인 주체**: 사용자 단독 / 사용자 + 3+1 합의
5. **Hermes 텔레메트리 차단 정책**: §2.6.2 egress 화이트리스트 외 추가 차단 (예: localhost 외부 통신 일체 금지)
6. **ChatGPT Pro Codex CLI ToS 검증 주기**: 월 1회 / 분기 1회

---

## 13. Phase 4+ 검토 (현재 미정의)

다음 항목은 본 P2에서 정의하지 않으며, Phase 3 안정화 후 별도 ADR로 다룬다:

- 전면 이전 (모든 워크플로 Hermes로)
- Claude Code 제거
- LiteLLM 외 추가 SDK 통합 (예: 자체 Adapter v2.0 — ADR-009 트리거 충족 시)
- Hermes 자체 fork·자체 hosted

---

**이 문서는 3+1 에이전트 합의 검증을 통과해야 확정됩니다.**
