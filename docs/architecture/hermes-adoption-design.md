# Hermes Agent 도입 설계 v2 (Hermes Adoption Design v2)

> **Option B 단계 도입 + 6개 차단조건 + Phase 0/1/2/3 + 롤백 + 검증. 3+1 합의 TIER 0~3 보강 적용 (v2)**

**최종 수정**: 2026-05-04 (3+1 합의 통과, TIER 0+1+2+3 적용)
**상태**: 확정 (3+1 합의 완료 — `review/3plus1-consensus-2026-05-04-p2-hermes-adoption.md`)
**상위 결정**: `ADR-008-hermes-adoption-decision.md` (Option B 채택)
**관련 ADR**: ADR-009 (자체 Adapter v2.0 진입조건), **ADR-010 (SQLCipher Vault HSM 키 관리)**
**관련 설계**: `llm-providers-design.md` (P1 v2 — LiteLLM facade), `multi-agent-system-design.md`, `harness-engineering-design.md`, `environment-and-docker-design.md`

---

## 1. 개요

### 1.1 목적

ADR-008 Option B (Hermes 메인 오케스트레이터 + Claude/GPT 등 서브 LLM)의 **단계별 도입 메커니즘**을 명세. v2는 3+1 합의 결과 (TIER 0 BLOCKER 3건, TIER 1 MUST 6건, TIER 2 SHOULD 6건, TIER 3 NICE 4건)를 모두 반영.

### 1.2 범위

| 포함 | 제외 |
|------|------|
| Phase 0~3 단계 + 진입·exit 기준 | LLM Provider 추상화 (P1 위임) |
| 6개 차단조건 충족 메커니즘 (강화) | SQLCipher 키 관리 상세 (ADR-010 위임) |
| 롤백 기준 (11종 트리거) + 데이터 복구 | 신규 Hermes 스킬 작성 가이드 (별도 문서) |
| 운영 메트릭·대시보드 (정량 임계) | Phase 4+ (전면 이전) |
| 헌법 정합성 보강 메커니즘 | Hermes 자체 사용법 |

### 1.3 v2 주요 변경 사항 (3+1 합의 결과)

#### TIER 0 BLOCKER (3건, Phase 1 진입 전 100%)
- **R0-1**: §3 Phase 0 신설 (3~5일) — P2-N1·N2 + sqlite import 호환성 검증 게이트
- **R0-2**: §7.1 자동 롤백 트리거 6경로 추가 (총 11종)
- **R0-3**: §2.1 SQLCipher 키 관리 강화 → ADR-010 위임 (Vault HSM + Shamir SSS)

#### TIER 1 MUST (6건)
- R1-1 §2.6 컨테이너 격리 6항목 강화
- R1-2 §2.6.3 OAuth 권한 검증 (entrypoint stat + inotify)
- R1-3 §7.2 데이터 무결성 (BEGIN IMMEDIATE + WAL + grace period 30s)
- R1-4 §5.4 Phase 2 메트릭 분리 (다중 LLM 효과 vs Hermes 셀프-임프루빙)
- R1-5 §9.2 셀프-임프루빙 계산적 센서 (스킬 PR 정적 분석 + Reviewer 격리)
- R1-6 §4 Phase 1 기간 3~4주 현실화

#### TIER 2 SHOULD (6건)
- R2-1 API 키 env → docker secret
- R2-2 DoH 우회 차단 (egress 정책)
- R2-3 §8 정량 임계 명시 ("정성적 PASS" 제거)
- R2-4 §4.3 OAuth 자동 PASS 의미 부여
- R2-5 §7.2 변환 스크립트 1회 시연 의무
- R2-6 redaction base64 우회 테스트

#### TIER 3 NICE (4건)
- R3-1 §2.0 차단조건 "P2 자체 4 + P1 의존 2" 분리 표기
- R3-2 §9.3 Hermes 의존도 메트릭
- R3-3 §13 미해결 사항 사용자 응답 회수 단계
- R3-4 §4 회귀 슈트 일정 1주 → 2주

### 1.4 전제 조건

도입 전 다음이 충족되어야 한다:

1. **P1 (LLM Provider Facade) MVP 완료** — 모든 LLM 호출이 P1 facade 경유
2. **`llm-providers.yaml` 검증** — Min 2 active + 동일 type 강제 + redaction 활성
3. **OAuth 직결 금지 정책** — Hermes는 API 키만 (Phase 1)
4. **Docker 격리 환경 + Vault HSM 준비** — 컨테이너 + 키 관리 인프라
5. **백업 절차 확립** — 백업·복구 sample restore 검증

### 1.5 ADR-008과의 관계

ADR-008은 **무엇(What)**, 본 P2는 **어떻게(How)**, ADR-010은 키 관리의 **세부(Detail)**.

| ADR-008 결정 | P2 v2 구현 메커니즘 |
|-------------|------------------|
| Option B 채택 | §3~6 Phase 0/1/2/3 단계 |
| 6개 차단조건 비협상 | §2 차단조건별 메커니즘 (분류 §2.0 신설) |
| Phase 종료마다 재평가 | §7 롤백 기준 + §8 검증 메트릭 |
| CRITICAL R1·R2·A-meta | §2.1 (R1+ADR-010), §2.2 (R2), §2.6 (A-meta) |
| 미충족 시 Option A 자동 폴백 | §3.4 Phase 0 미통과 + §7.1 자동 트리거 |

### 1.6 P1과의 관계

본 P2는 **P1 facade를 전제**로 동작:

```
[Hermes]                           [본 P2 범위]
   ↓ LLM 호출
[P1 LLMFacade]                     [P1 v2 범위]
   ↓ litellm.Router
[Anthropic / OpenAI / Ollama / ...]
```

Hermes 자체 SDK 직접 import 금지 (P1 depcruise로 차단).

### 1.7 하네스 위치

```
Layer 0:   CLAUDE.md (가이드 — 도입 정책)
Layer 0.5: 본 P2 (가이드 — Phase 게이트·차단조건·롤백)
Layer 1~3: 기존 hooks 유지 (Phase 3까지)
Layer 4:   CI (Phase 진입 조건 자동 검증)
Layer 5:   3+1 합의 (Phase 진입·exit·롤백 결정)
Layer 6:   사용자 검토 (각 Phase 종료마다)
```

---

## 2. 6개 차단조건 충족 메커니즘

### 2.0 차단조건 분류 (R3-1 가시화)

| # | 차단조건 | 책임 | 본 P2 책임 항목 |
|---|---------|------|--------------|
| 1 | SQLCipher 암호화 | **P2 직접** | §2.1 + ADR-010 (키 관리) |
| 2 | JSONL export | **P2 직접** | §2.2 |
| 3 | v0.x 버전 핀 | **P2 직접** | §2.3 |
| 4 | provider 어댑터 1개 | **P1 위임** | §2.4 (검증·강제만) |
| 5 | Min 2 provider always-on | **P1 위임** | §2.5 (Phase별 active 명시만) |
| 6 | Docker 격리 + egress | **P2 직접** | §2.6 |

→ **P2 자체 메커니즘 4개 + P1 의존 2개**. 형식 게이트 2개 가시화로 Phase 진입 시 게이트 부담 명확화.

### 2.1 차단조건 #1 — SQLCipher + Shamir + Redaction (R0-3 → ADR-010)

**위험**: Hermes 학습루프(SQLite FTS5) 평문 영구 누적 → 헌법 8조 직접 위반

#### 2.1.1 SQLite → SQLCipher 전환

ADR-008 부록 A.2: Hermes는 SQLite + FTS5 단일, ChromaDB 미사용.

```bash
# Phase 1 진입 시 (Phase 0 sqlite import 호환 검증 통과 후)
pip install pysqlcipher3
# Hermes의 sqlite3 import 경로를 monkey-patch로 인터셉트
# Phase 0에서 호환 검증 (§3.2)
```

#### 2.1.2 Vault HSM + Shamir SSS 키 관리 (ADR-010 위임)

**전체 위임**: ADR-010 (`docs/decisions/ADR-010-sqlcipher-vault-key-management.md`) 참조.

요약:
- **Vault HSM**: 키 저장·접근 제어·감사 로그
- **Shamir's Secret Sharing 3-of-3**: 단일 분실 즉시 손실 방지
- **90일 자동 회전 + dual-key 운영**: 회전 중 무중단
- **PGP 봉인 백업**: 별도 저장소에 봉인된 분할 키
- **시간별 incremental + 일일 full 백업**
- **sample restore 검증 의무화** (분기 1회)

#### 2.1.3 Pre-Record Redaction Hook (P2-N1 의존)

P1의 `RedactionFilter`(P1 §8.2)를 Hermes 학습루프 기록 직전에 적용:

```python
# hermes_redaction_hook.py
def pre_record_hook(session_event):
    return P1_REDACTOR.scrub(session_event)

hermes.session_storage.add_pre_record_hook(pre_record_hook)
```

**P2-N1 미해결**: Hermes pre-record hook 공식 지원 여부는 §3 Phase 0에서 검증. 미지원 시 §3.4 폴백.

#### 2.1.4 Base64 우회 테스트 (R2-6)

```python
# tests/hermes/redaction/test_base64_evasion.py
def test_base64_encoded_secret_redacted():
    secret = "sk-ant-XXXXXXXXX"
    encoded = base64.b64encode(secret.encode()).decode()
    assert REDACTOR.scrub(f"data: {encoded}") != f"data: {encoded}"
```

#### 2.1.5 검증 방법

```
✅ Phase 1 exit 조건:
  1. 강제 sqlite3 열기 거부 (SQLCipher 동작)
  2. 환경변수 echo LLM 호출 → DB 평문 확인 안 됨 (redaction)
  3. Base64 인코딩된 비밀 LLM 호출 → 동일 (R2-6)
  4. 디스크 탈취 시뮬레이션 → 키 없이 열기 불가
  5. Vault 헬스체크 + Shamir 분할 키 보존 검증
  6. Sample restore 1회 성공 (분기 의무)
```

#### 2.1.6 미충족 시

```
조건 #1 미충족 → Phase 진입 자동 차단 → §7.1 자동 트리거
   → ADR-008 Option A 폴백
```

---

### 2.2 차단조건 #2 — JSONL Export + 마이그레이션 (R2)

#### 2.2.1 공식 export 명령

ADR-008 부록 A.2: `hermes sessions export backup.jsonl` 공식 지원.

```bash
# 시간별 incremental (R0-3 일관)
0 * * * * hermes sessions export ~/backups/hermes-incremental-$(date +%Y%m%d-%H).jsonl --since=1h

# 일일 full (R0-3 일관)
0 2 * * * hermes sessions export ~/backups/hermes-full-$(date +%Y%m%d).jsonl
```

#### 2.2.2 Skills/Memory Export (P2-N2 의존)

`hermes sessions export`가 sessions 외 skills/memory 포함 여부는 §3 Phase 0에서 검증.

미지원 시 우회:
- `hermes skills export` 또는 `hermes memory export` 별도 명령 탐색
- 직접 SQLite 쿼리 (Vault에서 키 복원 후)
- 모든 경로 실패 시 §3.4 폴백

#### 2.2.3 마이그레이션 시나리오 (R2-5 시연 의무)

```
Scenario A: Hermes → Claude Code 복귀 (전체 롤백)
  Step 1: hermes sessions export full-backup.jsonl
  Step 2: scripts/hermes-migration/jsonl_to_claude.py 변환
  Step 3: Claude Code import + 검증
  ※ R2-5: Phase 1 exit 시 본 시나리오 1회 시연 의무화

Scenario B: Hermes → 다른 오케스트레이터
  JSONL 표준이므로 자체 import 작성

Scenario C: Hermes 메이저 업데이트
  업데이트 전 export → 후 import + schema_version 호환성
```

#### 2.2.4 검증 방법

```
✅ Phase 1 exit:
  1. 시간별 + 일일 백업 7일 무사고
  2. **R2-5 Scenario A 1회 시연 성공** (변환 스크립트 동작)
  3. JSONL 표준 포맷 검증 (jq 파싱)
  4. Sample restore 1회 (Vault 키 복원 + DB 복원 + import)
```

---

### 2.3 차단조건 #3 — 버전 핀 + 회귀 + 카나리

#### 2.3.1 버전 핀

```yaml
# hermes-version.yaml
version: v0.12.0
checksum: sha256:abc123...
release_notes_url: https://github.com/NousResearch/hermes-agent/releases/tag/v0.12.0
last_audit: 2026-05-04
audit_status: passed
next_audit_due: 2026-08-04
```

`hermes update`, `pip install --upgrade hermes` 등은 운영 환경 **금지** (정책 + R0-2-4 자동 트리거).

#### 2.3.2 회귀 테스트 슈트 (R3-4 일정 2주)

```
tests/hermes/regression/
├── test_session_export.py        # JSONL export 무결성
├── test_skill_creation.py        # 스킬 생성·실행
├── test_oauth_flow.py            # API 키 (Phase 1) + OAuth (Phase 2+)
├── test_sqlcipher_encryption.py  # DB 암호화
├── test_redaction.py             # 비밀값 echo 차단 + base64 우회 (R2-6)
├── test_litellm_facade.py        # P1 facade 경유
├── test_3plus1_consensus.py      # Phase 2: 다중 LLM 합의
└── test_metrics_separation.py    # R1-4 다중 LLM vs 셀프-임프루빙 메트릭
```

**R3-4**: 7종 테스트 작성 일정 1주 → **2주**로 현실화.

#### 2.3.3 카나리 환경

```
production: 핀 버전 (v0.12.0)
canary:     새 버전 후보 — docker-compose profile 분리
            회귀 테스트 통과 + 1주 격리 운영 + 메트릭 비교
```

카나리 무사고 → production 승격 (PR + Reviewer-only 합의).

---

### 2.4 차단조건 #4 — P1 Facade 위임 (P2 책임: 검증)

본 P2 책임:
- Hermes의 모든 LLM 호출 P1 facade 경유 검증
- Hermes 내부 `litellm`/`anthropic`/`openai` 직접 import 금지
- Hermes 자체 LLM 라우팅 비활성화 → P1 facade 위임

```
✅ Phase 1 exit:
  1. depcruise 검사 통과 (Hermes 디렉토리 포함)
  2. 인위적 분기 코드 PR로 차단 확인
  3. Hermes 호출 로그 P1 facade 경유 흔적
```

---

### 2.5 차단조건 #5 — Min 2 Active (P1 위임)

P1 위임. 본 P2 책임:
- Phase별 active provider 구성 명시 (§4·§5·§6)
- Hermes의 단일 provider 강제 코드 검사
- 구독 취소 시뮬레이션 (§7.3)

---

### 2.6 차단조건 #6 — Docker 격리 강화 (R1-1)

#### 2.6.1 Dockerfile (R1-1 + R2-1)

```dockerfile
# Dockerfile.hermes
FROM python:3.11-slim AS builder
COPY hermes-version.yaml /etc/hermes/
RUN pip install --target=/install hermes-agent==0.12.0 pysqlcipher3

FROM python:3.11-slim AS runtime
COPY --from=builder /install /usr/local/lib/python3.11/site-packages
RUN useradd -m -s /bin/bash hermes
USER hermes
WORKDIR /home/hermes
ENTRYPOINT ["hermes"]
# 빌드 단계와 런타임 분리로 read_only vs pip install 모순 해결
```

#### 2.6.2 docker-compose (격리 6항목 + R2-1 secret)

```yaml
services:
  hermes:
    build:
      dockerfile: Dockerfile.hermes
    secrets:                            # R2-1: env → docker secret
      - anthropic_api_key
      - openai_api_key
      - hermes_db_key                   # Vault에서 주입
    volumes:
      - hermes-data:/home/hermes/.hermes
      - ${CLAUDE_CREDS_PATH}:/credentials/claude:ro,nosuid
    networks:
      - hermes-egress
    cap_drop:
      - ALL
    security_opt:                       # R1-1: seccomp 명시
      - seccomp:default
      - no-new-privileges:true          # R1-1
    read_only: true                     # R1-1 (빌드 단계 분리로 모순 해결)
    tmpfs:
      - /tmp:noexec,nosuid,size=64m     # R1-1 noexec 명시
    pids_limit: 256                     # R1-1 fork bomb 차단
    pid: container                      # R1-1 별도 namespace

# Docker socket 마운트 명시적 금지 (R1-1)
# 본 compose에 /var/run/docker.sock 마운트 없음을 정책으로 명시

networks:
  hermes-egress:
    driver: bridge

volumes:
  hermes-data:

secrets:
  anthropic_api_key:
    external: true                      # vault에서 주입
  openai_api_key:
    external: true
  hermes_db_key:
    external: true                      # Vault 통합 (ADR-010)
```

#### 2.6.3 Egress 화이트리스트 (R2-2 DoH 차단)

```
[허용 — Phase 1]
- api.anthropic.com
- api.openai.com
- localhost:11434 (Ollama)
- openrouter.ai (폴백)
- vault.internal (Vault HSM)

[차단]
- 그 외 모든 외부 통신
- Hermes 자체 텔레메트리 endpoint (NousResearch 분석 서버) 명시 차단
- **DoH 차단 (R2-2)**: 1.1.1.1, dns.google, mozilla-doh 등 DoH 엔드포인트 화이트리스트 외 차단
- DNS는 docker bridge 내장 resolver만 사용
```

iptables/ufw로 도메인 + IP 이중 화이트리스트.

#### 2.6.4 OAuth Credentials 처리 강화 (R1-2)

| 항목 | 정책 |
|-----|------|
| 경로 환경변수화 | `oauth_credentials_env: CLAUDE_CREDS_PATH` (yaml 평문 금지) |
| 파일 권한 | `chmod 600` 강제 + entrypoint `stat -c "%a"` 검증 (시작 fail-fast) |
| Docker mount | `:ro,nosuid` |
| **inotify 런타임 감시 (R1-2)** | mtime/perm 변경 시 즉시 컨테이너 정지 |
| 만료 임박 알림 (R1-2) | 토큰 만료 7일 전 알림 |
| 로그/메트릭 echo 금지 | RedactionFilter 자동 strip |
| 단위 테스트 | 토큰 echo 0건 검증 |

#### 2.6.5 호스트 파일시스템 접근

| 마운트 | 용도 | 권한 |
|--------|------|------|
| `hermes-data` (volume) | SQLCipher 암호화 데이터 | rw, **인벤토리 검증** (실행 파일 차단) |
| `${CLAUDE_CREDS_PATH}` | OAuth (Phase 2+) | ro, nosuid |
| `/tmp` (tmpfs) | 임시 작업 | rw, **noexec, nosuid, 64m** |
| 그 외 | — | 마운트 금지 |

**hermes-data 인벤토리 정책 (B-N5)**: 정기 스캔으로 .py/.sh/실행 가능 파일 검출 시 알림.

#### 2.6.6 검증 방법

```
✅ Phase 1 exit:
  1. 호스트 파일 접근 시도 → 거부
  2. 화이트리스트 외 통신 시도 → 거부 (DoH 포함)
  3. cap_drop 검증 (raw socket 거부)
  4. read_only 검증 (루트 fs 쓰기 거부)
  5. tmpfs noexec 검증 (실행 시도 거부)
  6. fork bomb 시뮬레이션 → pids_limit 차단
  7. Docker socket 미존재 검증
  8. inotify credentials 변경 시뮬레이션 → 자동 정지
```

---

## 3. Phase 0 — 사실 확인 게이트 (NEW, 3~5일) [R0-1]

### 3.1 목표

Phase 1 진입 전 비협상 가정 3가지 검증:
1. **P2-N1**: Hermes pre-record hook 공식 지원 여부
2. **P2-N2**: `hermes sessions export`의 skills/memory 포함 여부
3. **sqlite import 호환**: `pysqlcipher3` monkey-patch가 Hermes sqlite3 사용을 인터셉트 가능한가

### 3.2 작업

```
Day 1: 환경 준비
  ✓ 격리 환경에 Hermes v0.12.0 설치 (docker-compose hermes-poc)
  ✓ Hermes 소스 코드 로컬 clone (검증용)

Day 2: P2-N1 검증
  ✓ Hermes 소스에서 session_storage 모듈 grep
  ✓ pre-record hook API 존재 확인 (공식 문서 + 코드)
  ✓ 인위적 hook 등록 → 호출 동작 확인
  ✓ 결과: PASS / FAIL

Day 3: P2-N2 검증
  ✓ 인위적 skill 1개 + memory 1개 생성
  ✓ hermes sessions export → JSONL 검사
  ✓ skill·memory 포함 여부 확인
  ✓ 미포함 시: hermes skills/memory export 별도 명령 탐색
  ✓ 결과: PASS / PARTIAL / FAIL

Day 4: sqlite import 호환 검증
  ✓ pysqlcipher3 설치 + Hermes sqlite3 monkey-patch 시도
  ✓ Hermes 정상 부팅 + DB 암호화 동작 확인
  ✓ 결과: PASS / FAIL

Day 5: 종합 결과 + ADR 정리
  ✓ 3건 결과 종합
  ✓ §3.3 통과 기준 평가
  ✓ 미통과 시 §3.4 폴백 ADR 작성 (ADR-011 또는 ADR-008 갱신)
```

### 3.3 통과 기준 (Phase 1 진입 조건)

**전부 PASS**여야 Phase 1 진입 가능:

| 검증 | PASS 기준 | PARTIAL 처리 | FAIL 처리 |
|-----|----------|------------|----------|
| P2-N1 | pre-record hook 공식 지원 + 호출 동작 확인 | — (이진 판정) | §3.4 폴백 |
| P2-N2 | sessions/skills/memory 모두 export 포함 | skills/memory 별도 명령으로 가능 시 PASS, 아니면 §3.4 | §3.4 폴백 |
| sqlite | monkey-patch 정상 동작 + 부팅 + 암호화 | — | §3.4 폴백 |

### 3.4 미통과 시 폴백 (D-1=(a) Option A)

```
Phase 0 미통과 → ADR-011 작성:
  Step 1: 결과 정리 (어느 검증 FAIL)
  Step 2: P2/ADR-008 부분 무효화
  Step 3: ADR-008 Option A 자동 회귀
  Step 4: 사용자 통보 + 차후 대응 결정 (재시도 시점, 폴백 안 유지 등)
```

**대안**: 사용자가 명시 동의 시 C-대안2 (Claude Code 메모리 + LiteLLM 3~5일 PoC)로 전환 가능.

---

## 4. Phase 1 — 검증 (3~4주) [R1-6]

### 4.1 목표

- 6개 차단조건 충족 검증 (TIER 0~1 모두 적용된 환경)
- API 키 경로만 사용 (OAuth 직결 금지)
- 비핵심 작업 운영 (5건 이상 무사고)
- 메트릭 베이스라인 수집

### 4.2 작업 (3~4주, 21~28일)

```
Week 1: 핵심 인프라
  ✓ Phase 0 결과 반영 (PASS 가정)
  ✓ Docker 격리 환경 구축 (§2.6 6항목 + R2-1 secret)
  ✓ Vault HSM 통합 (ADR-010)
  ✓ Shamir SSS 키 분할 + 봉인 백업 (PGP)
  ✓ SQLCipher 통합 + redaction hook
  ✓ hermes-version.yaml v0.12.0 핀

Week 2: 회귀 테스트 + 차단조건 검증 (R3-4 일정 2주)
  ✓ 회귀 테스트 슈트 7종 작성 (test_metrics_separation 포함)
  ✓ 차단조건 #1·#2·#3·#6 검증 (§2.1.5, §2.2.4, §2.6.6)
  ✓ #4·#5 검증 (P1 facade 경유, Min 2 active 시작 검증)
  ✓ 자동 롤백 트리거 11종 동작 검증 (§7.1)

Week 3: 비핵심 작업 운영
  ✓ Hermes로 비핵심 작업 5건 이상 (문서 요약, 코드 검색 등)
  ✓ 메트릭 수집 (응답 시간·비용·에러율·폴백률·OAuth 호출 0)
  ✓ 시간별 + 일일 백업 7일 연속 무사고
  ✓ Sample restore 1회 (분기 의무)

Week 4: Phase 2 진입 준비
  ✓ 변환 스크립트 (R2-5) Scenario A 1회 시연
  ✓ Phase 1 결과 리포트 작성
  ✓ Phase 2 진입 조건 평가 (§4.3)
  ✓ 사용자 승인 회수
```

### 4.3 Phase 2 진입 조건 (Phase 1 exit) — R2-3 정량화 + R2-4 OAuth 의미

| # | 조건 | 정량 임계 (R2-3) | 검증 |
|---|------|---------------|------|
| 1 | 6 차단조건 충족 | 6/6 PASS | §2 검증 방법 |
| 2 | 회귀 테스트 통과율 | **100%** (전 7종) | CI 자동 |
| 3 | 비핵심 작업 사고율 | **0건 / 5건 이상 작업** | 작업 로그 |
| 4 | 일일 백업 성공률 | **7일 연속 100%** + sample restore 1회 | 백업 로그 |
| 5 | OAuth 직결 호출 수 | **0건** (R2-4: Phase 1은 API 키만이므로 자동 PASS — Phase 2 도입 시 §5.3 #6 재검증) | 호출 로그 |
| 6 | depcruise 검사 | **PASS** | CI |
| 7 | 자동 롤백 트리거 동작 | **11종 전부 시뮬레이션 통과** | 시뮬레이션 |
| 8 | Vault 헬스 + Shamir 분할 키 | **3-of-3 보존 + Sample restore 분기 1회** | Vault audit log |
| 9 | 변환 스크립트 시연 (R2-5) | **1회 성공** | 시연 로그 |
| 10 | 사용자 승인 | Phase 1 리포트 검토 후 명시 승인 | 사용자 |

미충족 시 Phase 1 연장 또는 Option A 폴백 (§7.1 자동).

### 4.4 Phase 1 메트릭 베이스라인

```
[수집]
- 응답 시간 P50/P95/P99 (alias별)
- 비용 provider별 누적 (월 환산)
- 에러율 전체/provider별
- 폴백 발생률 alias별
- OAuth 호출 수 (목표: 0)

[베이스라인 기록]
docs/metrics/hermes-phase1-baseline.md
```

---

## 5. Phase 2 — 병행 (2~4주)

### 5.1 목표

- Layer 5 (3+1 합의)만 Hermes 서브에이전트로 이전
- 다중 LLM: Agent A=Claude / Agent B=GPT / Agent C=Ollama
- **R1-4: 다중 LLM 효과 vs Hermes 셀프-임프루빙 효과 분리 측정**

### 5.2 작업

```
Week 1: 3+1 합의 Hermes 이식
  ✓ Hermes 서브에이전트 정의 (Agent A/B/C/Reviewer)
  ✓ P1 routing alias 매핑 (consensus_agent_a/b/c/reviewer)
  ✓ Hermes 합의 워크플로 (Phase 0~4 재현)
  ✓ Claude Code 합의와 병렬 실행 가능 구조

Week 2: 실 합의 + 비교
  ✓ 안건 5건에 대해 Claude Code + Hermes 동시 실행
  ✓ 결과 품질 비교 (사용자 평가)
  ✓ R1-4 메트릭 분리 측정 시작

Week 3~4: 안정화
  ✓ R1-4 메트릭 4주 누적
  ✓ 발견 문제 수정
  ✓ Phase 3 진입 가능성 평가
```

### 5.3 Phase 3 진입 조건

| # | 조건 | 정량 임계 (R2-3) |
|---|------|--------------|
| 1 | Hermes 합의 결과 품질 ≥ Claude Code | 사용자 평가 5건 모두 ≥ 동등 |
| 2 | 응답 시간 (전체 합의 종료) | Claude Code 대비 **±30%** 이내 |
| 3 | 비용 (전체 합의당) | Phase 1 베이스라인 **≤ 1.5배** |
| 4 | **R1-4 메트릭 분리 결과** | "다중 LLM 효과" + "Hermes 고유 효과" 모두 양의 값 (Reviewer 서면 평가) |
| 5 | Phase 1 차단조건 6개 유지 | §2 모두 |
| 6 | OAuth 사용 (Phase 2부터 검토 가능) | 사용 시 §2.5·§2.6.4 + P1 §7 모두 충족 (R2-4: §4.3 #6 자동 PASS 의미가 Phase 2에서 실 검증) |
| 7 | 운영 사고 | 0건 |
| 8 | 사용자 승인 | Phase 2 리포트 검토 |

### 5.4 Phase 2 메트릭 분리 (R1-4 핵심)

```
[메트릭 분리 측정 — 4주 누적]

A. "다중 LLM 효과" (Hermes 없이 P1 facade만으로 가능한 가치):
   - 단일 Claude 합의 vs 다중 LLM 합의 결과 다양성
   - 메타 한계 해소 효과 (편향 감소)
   - 측정: 사용자가 결과를 보고 "다중 모델로 더 풍부했다" 판정 비율

B. "Hermes 고유 셀프-임프루빙 효과":
   - Hermes 학습루프(SQLite FTS5)가 누적한 스킬·세션 활용도
   - 같은 안건 재실행 시 비용·시간 절감률
   - 새 안건에서 과거 유사 안건 자동 검색·활용

[해석 시나리오]
- A > 0, B > 0 → Hermes 도입 정당화 강함
- A > 0, B ≈ 0 → Phase 3 보류 + Hermes 셀프-임프루빙 미활용 → 의사결정: P1만 운영 또는 Hermes 활용 강화
- A ≈ 0, B > 0 → 단일 LLM + Hermes 학습루프 조합도 검토
- A ≈ 0, B ≈ 0 → ADR-008 재평가 (Hermes 도입 가치 부재)
```

→ R1-4가 옵션 3 (P2 보류) 전환 가능성을 데이터 기반으로 판단할 근거.

---

## 6. Phase 3 — 확장 (조건부)

### 6.1 목표

- Hook 계층(L1~L3) Hermes에서 재구축
- Provider 어댑터 본격 적용
- 점진 워크플로 이전

### 6.2 작업

```
Week 1~2: Hook 재구축 PoC
  ✓ Claude Code PostToolUse → Hermes 등가물 (file watcher + 스킬)
  ✓ Claude Code PreCommit → git pre-commit (L3 그대로)
  ✓ Hook 강제력 비교 (Claude Code vs Hermes)

Week 3+: 점진 전환
  ✓ 1~2개 워크플로씩 Hermes로 이전
  ✓ 각 이전 후 1주 모니터링 → 안정성 확인 후 다음
```

### 6.3 Phase 3 진입 조건 (까다롭게)

| # | 조건 | 정량 임계 |
|---|------|--------|
| 1 | Phase 2 exit 조건 모두 | §5.3 |
| 2 | Hook 재구축 PoC 성공 | watchexec 등으로 L1 강제력 **≥ 80%** Claude Code 대비 |
| 3 | OAuth 의존 제거 또는 §2.5+P1 §7 완전 충족 | 사용량 분석 |
| 4 | Phase 2 메트릭 ≥ 현 시스템 | **4주 연속** 동등 이상 |
| 5 | 6 차단조건 모든 Phase 유지 | §2 |
| 6 | 사용자 명시 승인 + 외부 검증 권장 | 외부 LLM 또는 사람 |

---

## 7. 롤백 기준

### 7.1 자동 롤백 트리거 11종 (R0-2)

| ID | 트리거 | 조건 | 동작 |
|---|--------|------|------|
| **T1** | 차단조건 미충족 | 6개 중 1개라도 운영 위반 | 즉시 정지 + Option A 폴백 + 알림 |
| **T2** | 데이터 손실 위험 | Vault 키 분실 (Shamir 복원 실패) 또는 백업 3일 연속 실패 | 즉시 정지 + 데이터 복구 (§7.3) |
| **T3** | 보안 사고 | OAuth 토큰 유출, redaction 우회 발견, **컨테이너 escape 징후 (T9 일부)** | 즉시 정지 + 토큰 회전 + 사고 분석 |
| **T4** | 의존성 비호환 | LiteLLM/Hermes 메이저 비호환 (회귀 테스트 0% 통과) | 핀 버전 유지 + 카나리 차단 |
| **T5** | 사용자 명시 정지 | "Hermes 정지" 명령 | 즉시 정지 |
| **T6 (R0-2-1)** | **메트릭 임계 초과** | P99 응답 시간 **2배** OR 비용 **3배** OR 에러율 **10%** | 자동 정지 + 알림 |
| **T7 (R0-2-2)** | **Hermes deadlock/OOM** | 컨테이너 헬스체크 **3회 연속 실패** | 자동 정지 + 재시작 시도 1회 → 미복구 시 폴백 |
| **T8 (R0-2-3)** | **SQLCipher 키 만료/회전 실패** | 시크릿 매니저 헬스 다운 OR Vault rotation API 실패 | 즉시 정지 + 키 복구 절차 |
| **T9 (R0-2-4)** | **Hermes 자동 업데이트 시도** | 컨테이너 내 `pip install --upgrade` 또는 `hermes update` 호출 감지 | 즉시 정지 + 컨테이너 재빌드 (이전 핀 버전) |
| **T10 (R0-2-5)** | **Egress 화이트리스트 위반** | 화이트리스트 외 도메인 통신 시도 (DoH 포함) | 즉시 정지 + 사고 분석 |
| **T11 (R0-2-6)** | **사용자 무응답** | Phase 진입 승인 대기 **N일 (기본 7일)** 경과 | 자동 폴백 (Option A) + 알림 |
| **T12 (추가)** | **Phase 진입 전 검증 실패** | Phase 0 또는 Phase N exit 검증 실패 | ADR 재평가 트리거 (§3.4 또는 ADR-011) |

### 7.2 수동 롤백 절차 (R1-3 transactional + grace period)

```
[수동 롤백 5단계]

Step 1: Hermes 정지 (Graceful)
  docker-compose -f docker-compose.hermes.yml stop --timeout 30  # SIGTERM grace 30s
  # 진행 중 트랜잭션 완료 대기

Step 2: 학습 데이터 export (Transactional)
  hermes pause                             # 또는
  sqlcipher state.db "BEGIN IMMEDIATE; ... ; COMMIT"  # snapshot isolation
  hermes sessions export ~/backups/rollback-$(date +%Y%m%d-%H%M).jsonl
  # WAL checkpoint 후 file-level snapshot

Step 3: 워크플로 복원
  - Phase 1 롤백: Claude Code 그대로 (영향 없음)
  - Phase 2 롤백: 3+1 합의 → Claude Code Agent tool 복귀
  - Phase 3 롤백: 이전한 워크플로 → Claude Code (사전 백업한 .claude/ 복원)

Step 4: 사고 보고서
  docs/incidents/2026-XX-XX-hermes-rollback.md

Step 5: ADR 재평가 (필요 시)
  ADR-008 재논의 또는 ADR-NNN 작성으로 결정 변경
```

### 7.3 데이터 복구

```
[Vault 키 보유 + Hermes 정상]
  hermes sessions export ~/backups/full-export.jsonl
  → scripts/hermes-migration/jsonl_to_claude.py
  → Claude Code import

[Vault 키 보유 + Hermes 비정상]
  Vault에서 Shamir 키 복원 (3-of-3)
  → sqlcipher state.db < extract.sql
  → JSONL 변환

[Vault 키 분실 (CRITICAL — Shamir 복원 절차)]
  Step 1: PGP 봉인 백업에서 분할 키 복원
  Step 2: 3-of-3 결합 → 마스터 키
  Step 3: Vault 재초기화 + 키 등록
  Step 4: 시간별 incremental 백업으로 최신 상태 복구 (최대 1시간 손실)

[Shamir 분할 + PGP 봉인 모두 분실 (재해)]
  일일 full 백업으로 복구 (최대 1일 손실)
  → 키 분실 사고 처리 절차 + 헌법 8조 사고 보고
```

---

## 8. 검증 메트릭 종합표 (R2-3 정량화)

| Phase | 메트릭 | 측정 | 정량 임계 (Phase exit) |
|-------|--------|------|------------------|
| Phase 0 | P2-N1 PASS | 인위 hook 호출 | 동작 확인 |
| Phase 0 | P2-N2 PASS | export JSONL 검사 | sessions/skills/memory 모두 포함 |
| Phase 0 | sqlite 호환 | monkey-patch 부팅 | 정상 부팅 + 암호화 동작 |
| Phase 1 | 6 차단조건 | §2 검증 | 6/6 PASS |
| Phase 1 | 회귀 테스트 | CI | **100%** |
| Phase 1 | 비핵심 사고 | 작업 로그 | **0/5+** |
| Phase 1 | 일일 백업 | 백업 로그 | **7일 연속 100%** + sample restore 분기 |
| Phase 1 | OAuth 직결 | 호출 로그 | **0** |
| Phase 1 | depcruise | CI | PASS |
| Phase 1 | 자동 롤백 11종 | 시뮬레이션 | **11/11 동작** |
| Phase 1 | Vault Shamir | audit log | **3-of-3 보존** |
| Phase 1 | 변환 스크립트 (R2-5) | 시연 | **1회 성공** |
| Phase 2 | 합의 품질 | 사용자 평가 | **5/5 ≥ 동등** |
| Phase 2 | 합의 응답 시간 | 메트릭 | **±30%** |
| Phase 2 | 합의 비용 | 메트릭 | **≤ 1.5배** |
| Phase 2 | R1-4 메트릭 분리 | 4주 누적 | A·B 모두 양의 값 (Reviewer 서면) |
| Phase 2 | 운영 사고 | 사고 로그 | **0** |
| Phase 3 | Hook 강제력 | 위반 차단 시뮬 | **≥ 80%** Claude Code 대비 |
| Phase 3 | 워크플로 이전 | 이전 로그 | **≥ 90%** (롤백 1회 허용) |
| Phase 3 | 메트릭 안정성 | 4주 측정 | Phase 2 ≥ 동등 |

---

## 9. 운영 가이드

### 9.1 일상 운영

```
[일일]
- Vault 헬스체크 + 백업 확인 (자동 cron)
- Hermes 컨테이너 헬스 (docker ps)
- 메트릭 대시보드 확인

[주간]
- 회귀 테스트 슈트 실행
- 비용 누적 (provider별)
- 사고 로그 검토
- R3-2 Hermes 의존도 메트릭 점검

[월간]
- 6 차단조건 재검증 (자동화 스크립트)
- ChatGPT Pro Codex CLI ToS 변동 모니터링
- LiteLLM·Hermes 릴리스 노트 검토
- Sample restore 1회 (분기당 최소)

[분기]
- hermes-version.yaml 감사
- ADR-009 v2.0 진입 트리거 점검 (T1~T4)
- Phase 진입 조건 재평가
- Vault Shamir 분할 키 보존 검증
- 90일 키 회전 (ADR-010)
```

### 9.2 신규 스킬 추가 (R1-5 계산적 센서)

ADR-008 R10 (poisoned skill) + 헌법 제3조(계산적 우선) + 헌법 제4조(합의):

```
Step 1: 스킬 초안 (Hermes 자동 생성 또는 수동)

Step 2: 자동 정적 분석 게이트 (R1-5 핵심)
  - import 화이트리스트 검사 (P1 facade 외 LLM SDK 직접 import 금지)
  - secret 패턴 검사 (sk-, Bearer, base64 인코딩 우회 — R2-6)
  - dangerous syscall 검사 (os.system, subprocess.run with shell=True 등)
  - 모델명 하드코딩 검사 (P1 위반 패턴 #1)

Step 3: PR 생성 → 코드 리뷰 (수동)
  - 정적 분석 결과 첨부
  - depcruise 결과 첨부

Step 4: 카나리 환경 1주 운영 (격리)
  - 메트릭 anomaly 탐지 (B-N4)

Step 5: Reviewer 격리 평가 (헌법 4조)
  - **Reviewer 에이전트는 별도 LLM 또는 별도 프로세스**
  - 동일 Hermes 인스턴스가 자기 스킬을 평가하지 않음
  - "에이전트 간 출력 비참조" 원칙 유지

Step 6: 사용자 승인 + 3+1 합의 (큰 스킬 시)

Step 7: production 배포
```

### 9.3 모니터링 대시보드 (R3-2 의존도)

```
[필수 패널 — Phase 1부터]
- provider별 호출 수·비용·에러율
- 폴백 발생률
- active provider 카운트 (Min 2)
- 백업 상태 (마지막 성공 시각)
- Vault 헬스 + Shamir 보존
- 자동 롤백 트리거 11종 활성/대기 상태

[Phase 2 추가]
- 합의 종료 시간 P50/P95
- LLM 모델별 응답 품질 (사용자 평가)
- **R1-4 다중 LLM 효과 vs Hermes 셀프-임프루빙 효과 분리 차트**

[Phase 3 추가]
- Hook 강제력 차단율
- 워크플로별 이전 상태

[R3-2 Hermes 의존도 메트릭]
- Hermes 경유 호출 / 전체 호출 비율
- Hermes 자체 코드 LOC / 전체 LOC
- Hermes 다운 시 영향받는 워크플로 수
- → 결합도 모니터링, 옵션 3 전환 의사결정 데이터
```

---

## 10. 위험 등록부

### 10.1 ADR-008 인수 (R1~R10)

| ID | 위험 | P2 v2 완화 |
|----|------|---------|
| R1 | 학습루프 평문 | §2.1 SQLCipher + Vault Shamir + redaction (ADR-010) |
| R2 | Hermes 자체 lock-in | §2.2 + §7.3 변환 스크립트 |
| R3 | v0.x API 변동 | §2.3 |
| R4 | Claude OAuth 4종 버그 | §4 Phase 1 API 키만, Phase 2부터 §2.6.4 + P1 §7 |
| R5 | Liquidity 위반 패턴 | P1 위임 |
| R6 | 다중 자격증명 표면 | §2.6.2 R2-1 docker secret + Vault |
| R7 | 모델 응답 일관성 | P1 위임 (LiteLLM 정규화) |
| R8 | 단일 구독 의존 | P1 위임 + Phase별 active 명시 |
| R9 | 컨테이너 격리 미적용 | §2.6 R1-1 6항목 강화 |
| R10 | self-improvement loop 오염 | §9.2 R1-5 정적 분석 + Reviewer 격리 |

### 10.2 P1 인수
- P1 R1~R12 모두 P1 facade 사용으로 자동 적용

### 10.3 P2 v2 신규 + B 인수

| ID | 위험 | 등급 | 완화 |
|----|------|------|------|
| P2-N1 | Hermes pre-record hook 공식 미지원 가능성 | HIGH | §3 Phase 0 게이트 검증, FAIL 시 §3.4 폴백 |
| P2-N2 | hermes export skills/memory 미포함 가능성 | HIGH | 동일 |
| P2-N3 | SQLCipher 키 분실 → 데이터 손실 | HIGH → CRITICAL | ADR-010 Vault Shamir + PGP 봉인 → 분실 시 §7.3 복구 |
| P2-N4 | 다중 LLM 합의 품질 편차 | MEDIUM | R1-4 메트릭 분리 + §5.3 #1 평가 게이트 |
| P2-N5 | Phase 3 Hook 강제력 손실 | MEDIUM | §6.3 #2 80% 임계, 미달 시 보류 |
| P2-N6 | 카나리 비교 자동화 부담 | MEDIUM | Phase 1 수동 → Python 스크립트 |
| **B-N1** | API 키 유출 | HIGH | R2-1 docker secret + Vault |
| **B-N2** | SQLCipher 키 유출 | **CRITICAL** | ADR-010 Vault HSM + Shamir + 감사 로그 |
| **B-N3** | 컨테이너 escape | HIGH | §2.6 R1-1 6항목 + seccomp + AppArmor 검토 |
| **B-N4** | poisoned skill | HIGH | §9.2 R1-5 정적 분석 + 카나리 + anomaly |
| **B-N5** | tmpfs 코드 주입 | MEDIUM | §2.6.5 tmpfs noexec,nosuid + hermes-data 인벤토리 |
| **B-N6** | DoH 우회 | MEDIUM | §2.6.3 R2-2 DoH 차단 + DNS 통제 |
| **B-N7** | OAuth perm 변경 미탐지 | HIGH | §2.6.4 R1-2 entrypoint stat + inotify |
| **B-N8** | 메트릭 임계 자동차단 부재 | MEDIUM | §7.1 T6 자동 트리거 |
| **B-N9** | partial export 무결성 | MEDIUM | §7.2 BEGIN IMMEDIATE + WAL + grace |
| **B-N10** | self-improvement 센서 부재 | HIGH | §9.2 R1-5 정적 분석 + Reviewer 격리 |

---

## 11. ADR 매핑

| 관련 문서 | 정합성 |
|---------|--------|
| **ADR-008** (상위 결정) | Option B 단계 도입 — 본 P2가 직접 구현, Phase 0 게이트 신설 |
| **ADR-009** (자체 Adapter v2.0) | LiteLLM 사용 전제 — Phase별 진입 시 ADR-009 트리거 점검 |
| **ADR-010** (SQLCipher Vault HSM) | §2.1 키 관리 위임 — Shamir SSS + 90일 회전 + sample restore |
| **P1** (LLM Provider Facade) | 차단조건 #4·#5 위임. Hermes는 P1 facade 전제 |
| **ADR-004** (생성 AI 확장성) | 외부 SDK 우선 — Hermes도 외부 도구 |
| **ADR-006** (환경 변수 + Docker) | §2.6 격리 + R2-1 docker secret 일관 |
| **multi-agent-system-design** | Phase 2 3+1 합의 Hermes 이전 |
| **harness-engineering-design** | Layer 1~3 hook 재구축은 Phase 3 |
| **PROJECT_CONSTITUTION** | 제3조 (R1-5 계산적 센서), 제4조 (Reviewer 격리), 제8조 (SQLCipher + redaction + B-N2 Vault) |

---

## 12. 검증 항목 (3+1 합의 결과 — 본 v2가 통과)

본 v2 설계는 다음 16개 검증 항목 모두 충족:

### Agent A (구현)
- [x] 6 차단조건 충족 메커니즘 실 동작 가능 (Phase 0 게이트로 P2-N1·N2 사전 검증)
- [x] Phase 0/1/2/3 단계 의존성 일관 (§3·§4·§5·§6)
- [x] Docker 격리 + egress (텔레메트리·자동 업데이트 차단 — §2.6.3 + T9)
- [x] SQLCipher 통합 (ADR-010 Vault HSM)
- [x] 카나리 vs production 분리 (§2.3.3)

### Agent B (안전)
- [x] 자동 롤백 트리거 11종 (§7.1) — 6경로 추가
- [x] SQLCipher 키 분실 완화 (ADR-010 Shamir + PGP)
- [x] OAuth credentials 권한 검증 시작+런타임 (§2.6.4 R1-2 inotify)
- [x] Hermes 권한 상승 차단 (§2.6 R1-1 6항목)
- [x] 사고 시 데이터 무결성 (§7.2 BEGIN IMMEDIATE + grace)
- [x] 헌법 정합성 (§9.2 R1-5 + §10 위험 매트릭스)

### Agent C (대안)
- [x] Phase 분할 (§3 Phase 0 신설 + §4 Phase 1 3~4주)
- [x] 6 차단조건 비현실 평가 (§2.0 P2 자체 4 + P1 의존 2)
- [x] Hermes 없이 다중 LLM 가능성 (§5.4 R1-4 메트릭 분리로 사후 평가)
- [x] 더 단순한 PoC (§3.4 폴백에 C-대안2 명시)

### Reviewer
- [x] ADR-008 차단조건 6개 충족 메커니즘 명세 (§2)
- [x] Phase 진입·exit 객관 측정 (§8 정량 임계)
- [x] 자동·수동 롤백·데이터 복구 완비 (§7)
- [x] P2-N1·N2 Phase 0 게이트 명시 (§3)
- [x] ADR-008·P1·ADR-004 정합 (§11)

---

## 13. 미해결 결정 — 사용자 응답 회수 절차 (R3-3)

| # | 안건 | 대기 기간 | 미응답 시 동작 |
|---|------|---------|------------|
| MD-1 | Phase 0 결과 PASS/FAIL 확인 | 1일 (자동 진행) | FAIL 시 자동 §3.4 폴백 |
| MD-2 | Phase 1 진입 승인 | 7일 (T11 트리거) | 자동 Option A 폴백 |
| MD-3 | Phase 2 진입 승인 | 7일 (T11) | Phase 1 유지 |
| MD-4 | Phase 3 진입 승인 | 7일 (T11) | Phase 2 유지 |
| MD-5 | 카나리 → production 승격 | 7일 | 카나리 유지 |
| MD-6 | 신규 스킬 PR 승인 | 7일 | 카나리 유지 또는 거부 |

→ R3-3 사용자 응답 회수 단계 명시. T11 자동 트리거가 모든 사용자 결정 안건을 안전하게 처리.

---

## 14. Phase 4+ 검토 (현재 미정의)

다음 항목은 본 P2 범위 외, Phase 3 안정화 후 별도 ADR:

- 전면 이전 (모든 워크플로 Hermes)
- Claude Code 제거
- 자체 Adapter v2.0 (ADR-009 트리거 충족 시)
- Hermes 자체 fork·자체 hosted

---

**이 문서는 3+1 에이전트 합의 (P2 v1) 검증을 통과했으며 v2(TIER 0+1+2+3 적용)로 확정됨.**
**Phase 0 진입 가능. Phase 0 결과에 따라 Phase 1 진입 또는 §3.4 폴백.**
