# 3+1 합의 보고서: P2 (Hermes 도입 설계) 검증

**날짜**: 2026-05-04
**검증 대상**: `docs/architecture/hermes-adoption-design.md` (P2, ~700줄)
**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-009 (자체 Adapter v2.0 진입조건)
**관련 합의**: P1 (`3plus1-consensus-2026-05-04-p1-llm-providers.md`)

---

## 사전 점검 — Provider Liquidity 위반 여부

**판정: 위반 없음**. Hermes는 P1 LiteLLM facade의 routing alias 뒤에 위치 (#4) + Min 2 active 보장 (#5) + JSONL export (#2). 3 에이전트 #4·#5 PASS 일치.

---

## Phase 2 — 3 에이전트 독립 분석 요약

### Agent A (구현) — APPROVE with revisions
- 6 차단조건: #1 SQLCipher CONDITIONAL (Hermes sqlite import 검증 필요), #2 PASS for sessions / CONDITIONAL for skills/memory, #3 PASS, #4·#5 PASS, #6 CONDITIONAL (read_only vs pip 모순)
- **Phase 0 신설 권장** — P2-N1·N2 + sqlite import 검증 게이트
- Phase 1 기간 1~2주 비현실적 → 3~4주 권장
- 자동 롤백 트리거 카나리 메트릭 악화 누락
- SQLCipher 키 회전 절차 누락

### Agent B (안전) — APPROVE with revisions
- **6개 보강 조건** (자동 롤백 트리거 6경로, 컨테이너 격리 6항목, SQLCipher 키 관리, OAuth 권한 검증, 데이터 무결성, self-improvement 센서)
- **CRITICAL: B-N2 SQLCipher 키 유출** — Shamir SSS + 봉인 백업 + 90일 회전 + sample restore 의무
- 위험 매트릭스 10종 (B-N1~N10)
- **헌법 정합성 부분 위반** — 제3조(센서 부재), 제8조(redaction 우회 시나리오 미테스트)

### Agent C (대안) — APPROVE with revisions
- **5개 보강** (Phase 0.5 신설, Phase 2 메트릭 분리, 자동 롤백 ADR 재평가, 변환 스크립트 시연, 차단조건 분리 표기)
- **핵심 통찰**: Phase 2 다중 LLM 합의는 P1 facade만으로 즉시 가능 — Hermes 고유 가치는 셀프-임프루빙으로 좁혀짐
- 더 단순한 PoC 대안: Claude Code 메모리 + LiteLLM (3~5일)
- 메타 보정: 본인 LiteLLM 친화 편향 의식적 보정 — P2 자체 메커니즘 품질 높음

---

## Phase 3 — 교차 비교

### 일치 (3자 동의)
- U1: 결론 = APPROVE with revisions
- U2: P2-N1·N2는 검증되지 않은 가정, Phase 1 진입 전 사실 확인 필수
- U3: Phase 1 진입 전 별도 게이트 단계 신설 필요 (Phase 0 또는 0.5)
- U4: 차단조건 #4·#5 PASS
- U5: §6.1 카나리/롤백 자동 트리거 부재 — 보강 필요
- U6: 변환 스크립트 미작성 — Phase 2 exit 가능성 실증 필요
- U7: 6 차단조건의 "성실한 메커니즘화" 자체는 견고

### 부분 일치 (2자 동의)
- P1: #1 SQLCipher 충족이 P2-N1에 의존 — A·C 명시, B는 키 관리 측면 → A·C 채택 + B 보강 통합
- P2: #6 Docker 격리 추가 강화 — A·B 채택 (CRITICAL/HIGH 위험)
- P3: Phase 1 기간 비현실적 — A(3~4주) + C(2주+α) 채택, A안 우선
- P4: 셀프-임프루빙 센서 부재 — B·C 채택, 통합

### 불일치 (3자 다른 의견)
- D1 revision 범위: A(운영 디테일) vs B(보안·헌법) vs C(전략적 단순화) → **B 우선축**, A·C 보완축 (CRITICAL 단독 발견 채택 강제)
- D2 Hermes 본질 가치: A(메커니즘 견고) vs B(가치 평가 유보) vs C(Hermes 고유 = 셀프-임프루빙) → **C 통찰 채택하되 사용자 결정 옵션으로 격상** (메타 보정)
- D3 폴백 대상: A·C(Option A) vs C 추가(대안2 = Claude Code 메모리+LiteLLM) → **§6.1 폴백 명시 필요**, 사용자 결정

### 누락 (단독 발견 → 13건 채택)
- B-N2 (SQLCipher 키 유출) **CRITICAL** → 즉시 채택 (검토 규칙 #2)
- B-N5 tmpfs 코드 주입 MEDIUM → 격리 강화 일환
- B-N7 OAuth 권한 변경 미탐지 HIGH → 채택
- 헌법 3·4·6조 위반 → 채택 (P4와 통합)
- 데이터 무결성 export transactional 부재 HIGH → 채택
- A-G8 Phase 0 + sqlite import 검증 → 채택 (U3 통합)
- A-G9 OAuth 조건 모호 → 채택
- A-G10 정성적 PASS 모호 → 채택
- C-G11 Phase 2 메트릭 분리 HIGH → 채택 (메타 보정에도 의사결정 데이터 필수)
- C-G12 차단조건 분리 표기 LOW → 권장 채택
- C-G13 사용자 응답 회수 단계 → 채택

---

## Phase 4 — 최종 합의

### 합의된 결론 (한 문장)

**P2는 6 차단조건 메커니즘화가 견고하나 (a) P2-N1·N2 미검증 가정, (b) SQLCipher 키 관리 CRITICAL 공백, (c) 컨테이너 격리·자동 롤백·헌법 정합성 6건 보강, (d) Phase 2 본질 가치 측정 분리가 충족되어야 Phase 1 진입 가능 — APPROVE with revisions, 단 Phase 0 신설을 비협상 조건으로 함.**

---

### Revision 항목 통합

#### TIER 0 — BLOCKER (Phase 1 진입 전 100% 충족 필수)

| ID | 항목 | 출처 | 미충족 시 |
|----|------|------|----------|
| R0-1 | **Phase 0 신설 (3~5일)** — P2-N1·N2 + Hermes sqlite import 호환성 사실 확인 게이트 | A·C 강한 일치 | ADR-010 → Option A 폴백 또는 C-대안2 (Claude Code 메모리+LiteLLM 3~5일) |
| R0-2 | §6.1 **자동 롤백 트리거 6경로 명문화** (메트릭 임계, Hermes deadlock/OOM, SQLCipher 키 만료/회전 실패, 자동 업데이트 시도, egress 위반, 사용자 무응답) | B + A·C 일치 | Phase 1 진입 불가 |
| R0-3 | **SQLCipher 키 관리 CRITICAL 공백** — Shamir SSS 3분할 + PGP 봉인 + 90일 회전 + dual-key + 시간별 incremental + 일일 full + sample restore 검증 | B 단독, CRITICAL | Phase 1 진입 불가 (검토 규칙 #2 강제 채택) |

#### TIER 1 — MUST (Phase 1 종료 전 충족)

| ID | 항목 | 구체화 |
|----|------|--------|
| R1-1 | 컨테이너 격리 강화 6항목 | `tmpfs /tmp:noexec,nosuid,size=64m`, seccomp default profile, `no-new-privileges:true`, `--pids-limit`, pid 네임스페이스, Docker socket 마운트 금지. read_only vs pip 모순 해결 (Phase 0 install 후 read_only 전환) |
| R1-2 | OAuth 권한 검증 (B-N7) | entrypoint stat 0600 + inotify 변경 감지 + 만료 알림. §4.3 #6 OAuth 조건 모호성 해소 |
| R1-3 | 데이터 무결성 (G7) | export 시 BEGIN IMMEDIATE + WAL checkpoint 또는 hermes pause, SIGTERM grace period 30s |
| R1-4 | Phase 2 메트릭 분리 (C 통찰) | "다중 LLM 효과(P1 facade 단독)" vs "Hermes 셀프-임프루빙 효과" 독립 측정 |
| R1-5 | 셀프-임프루빙 계산적 센서 | 신규 스킬 PR 자동 정적 분석(import 화이트리스트, secret, base64 우회), Reviewer 에이전트 격리 명시 |
| R1-6 | Phase 1 기간 현실화 | **3~4주** (A 산정, R0~R1 보강 반영) |

#### TIER 2 — SHOULD (Phase 1 산출물 포함)
- R2-1 API 키 env → docker secret
- R2-2 DNS over HTTPS 우회 차단 (egress 정책)
- R2-3 §7 정량 임계 명시 ("정성적 PASS" 제거)
- R2-4 §3.3 #6 OAuth 자동 PASS 의미 부여
- R2-5 §6.3 변환 스크립트 1회 시연 의무
- R2-6 redaction base64 우회 테스트

#### TIER 3 — NICE (가시성)
- R3-1 6 차단조건 "P2 자체 4 + P1 의존 2" 분리 표기
- R3-2 Hermes 의존도 메트릭
- R3-3 §12 미해결 6건 사용자 응답 회수 명시
- R3-4 회귀 슈트 일정 1주 → 2주

---

### 미해결 결정 (사용자 입력 필요)

| # | 안건 | 옵션 | Reviewer 권장 |
|---|------|------|--------------|
| D-1 | P2-N1·N2 미지원 시 폴백 | (a) Option A 회귀 / (b) C-대안2: Claude Code 메모리+LiteLLM / (c) Hermes 부분 도입 | (a) — A·C 묵시적 전제 |
| D-2 | Hermes 본질 가치 평가 시점 | (a) Phase 1 진행 후 R1-4 메트릭 사후 평가 / (b) Phase 0에 사전 PoC 추가 / (c) 보류 + 셀프-임프루빙만 별도 PoC | (a) — 메타 한계 보정상 C 자동 채택 회피 |
| D-3 | Phase 1 기간 | (a) 3~4주 (A안) / (b) 2주+α (C안 보강 최소화) | (a) — 보안·헌법 보강 충분 시간 |
| D-4 | R0-3 SQLCipher 키 도구 | (a) ssss 라이브러리 / (b) Vault HSM / (c) 자체 구현 회피 | (b) Vault — 단 외부 의존 추가 → 별도 ADR 권장 |

---

### 위험 알림

#### CRITICAL
- B-N2 SQLCipher 키 유출 → R0-3 비협상

#### HIGH
- 헌법 8조 부분 위반 (P2-N1 미지원 시) → R0-1 Phase 0 게이트로만 해소
- 헌법 3조 부분 위반 → R1-5
- B-N3 컨테이너 escape → R1-1
- B-N7 OAuth 변경 미탐지 → R1-2
- B-N4 poisoned skill → R1-5 통합

#### 메타 위험
- 3 에이전트 모두 Claude. C의 P1 가치 강조는 직전 P1 합의에서도 반복 패턴 → D-2 자동 채택 회피
- R1-4 메트릭 분리는 메타 한계 보정 — 인간 사후 평가 가능 데이터 확보

---

## 사용자 결정 옵션

### 옵션 1: 표준 진행 (Reviewer 권장)
- D-1=(a) / D-2=(a) / D-3=(a) / D-4=(b)
- TIER 0 (3건) 충족 → Phase 0 (3~5일) → Phase 1 (3~4주) → Phase 2 (R1-4 메트릭)
- 총 소요: 약 4~5주

### 옵션 2: 보수적 진행 (C 통찰 부분 채택)
- D-2=(b): Phase 0 확장 (1주) → Hermes 고유 가치 PoC 사전 검증
- 결과 < P1 단독 가치의 20% → P2 보류
- 총 소요: 약 5~6주

### 옵션 3: 보류 및 재설계 (C 통찰 전면 채택)
- D-2=(c): P2 보류 + 셀프-임프루빙만 별도 PoC (대안2, 3~5일)
- ADR-008 재평가 필요 → ADR-010
- 검토 규칙 #4 (보류·재설계도 유효 결론) 적용

### 옵션 4: 즉시 폴백
- TIER 0 부담 과다 판단 시 Option A 즉시 회귀
- 검토 규칙 #4 적용

---

**Reviewer 권장: 옵션 1 (표준 진행)**

근거:
1. P2 메커니즘 자체 견고 (3자 일치 U7)
2. R0~R1 보강으로 6 차단조건 + CRITICAL/HIGH 위험 모두 해소 가능
3. 옵션 2 사전 PoC는 Phase 0 게이트(R0-1) 결과로 사후 결정 가능
4. 옵션 3은 메타 한계 보정상 C 가중치 자동 부여 회피
5. R1-4 메트릭 분리로 옵션 3 전환 가능성은 Phase 2 종료 시점 데이터 기반 재평가 가능
