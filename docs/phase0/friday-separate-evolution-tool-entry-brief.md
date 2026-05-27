# 프라이데이 (Friday) 별도 자가진화 툴 진입 자격 평가 brief

**일자**: 2026-05-27
**유형**: Phase 0 Entry Brief (진입 자격 평가 한정)
**선행 답습**:
- 자비스 MVP-1 1.5차 보강 4 sub-cycle 완료 (PC-1 + S-3 + ST-2 + AR-3)
- ADR-008 Hermes Adoption (Option B, PMO 격상 0건 = Design Adoption only)
- ADR-011 §2.1 (a)~(e) + §2.3 (Hermes ≠ root of trust) + §2.4 (T1/T2/T3 분리)
- 헌법 5조-2 (Provider Liquidity, 비협상) + 8조 (보안)
- 메모리 `project_jarvis_local_boss_direction` (자가진화 깊이: 깊게 지향, 무리면 중간 타협)
- 메모리 `feedback_proportionate_security_personal_tool` (비례성, 개인 툴엔 과잉)
- 직전 대화 §3 4 경로 비교 (A/B/C/D) + §6 (D) 프라이데이 권고

**scope**: 프라이데이 = 별도 자가진화 툴 진입 *자격 평가* 한정 — 실 진입 결정 0건, 자비스 본문 변경 0건, 헌법 변경 0건

---

## 1. 본 brief 의 자격

### 1.1 본 brief 의 목적

- 자가진화 깊이 (Hermes 수준) ↔ 자비스 4 invariant 보존 양립 경로 = (D) 별도 툴 (프라이데이) **진입 자격 평가** 한정
- (D) 형태 후보 2 ((P) 자체 코드 vs (Q) Hermes 도입) 비교 매트릭스
- 격리 메커니즘 사전 정의 (filesystem ACL + workdir + endpoint + 메모리 + commit 분리)
- Rollback Trigger 사전 등록 (R-Friday-1 ~ R-Friday-5)
- 자비스 MVP-1 단계 완료 → 프라이데이 진입 stage gate 명문
- 사용자 결정 항목 D-1 ~ D-8

### 1.2 본 brief 가 *하지 않는 것* (답습 영구)

1. ❌ 프라이데이 실 진입 결정 (본 brief 후 합의 + 사용자 명시 결정)
2. ❌ 자비스 본문 변경 (`src/jarvis/` + `boss.py` + `worker.py` + `orchestrator.py` 등 변경 0건)
3. ❌ 헌법 변경 (5조-2 + 8조 모두 보존)
4. ❌ ADR-011 §2.4 T3 변경 (자비스 영역 영구 보존, 프라이데이 영역 = 별도 설계 cycle)
5. ❌ Hermes 자체 도입 결정 ((Q) vs (P) 선택 = D-2 결정 영역)
6. ❌ 자비스 MVP-1 carry-over 영향 ((b1-AR3 첫 PR evidence) + (c) MVP-1 PASS 우선 진행 답습)
7. ❌ HW 자원 배분 결정 (D-5 결정 영역)
8. ❌ Layer 3 직접 설계 (별도 brief)
9. ❌ 비례성 메모리 갱신 결정 (D-6 결정 영역)
10. ❌ 코드·테스트·CI·hook·branch protection·ADR·헌법·roadmap 본문 변경 0건

---

## 2. 동기 + Marvel narrative 정합

### 2.1 본 프로젝트 narrative

| 갈래 | 역할 | 자가진화 깊이 | 안전 결과 우선순위 |
|---|---|---|---|
| **자비스 (Jarvis)** | 본업 prod, 개인 개발 작업 보조 | Layer 0/1 발효 + Layer 2 설계 DEFER + Layer 3 영구 차단 | ⭐⭐⭐ (4 invariant 영구 보존) |
| **프라이데이 (Friday)** | 별도 실험 영역, 자가진화 깊이 분담 | Layer 3 자동 적용 자격 (격리 안) | ⭐⭐ (자비스 침범 0 보장, 자기 격리 안 R1 risk 수용) |

### 2.2 Marvel 메타포 정합 (기능 봉사 한정)

- Jarvis = 토니 스타크 안전한 비서, 4 본질 보수적 보존
- Friday = Jarvis 다음 후속, 적극적 확장 + 실험적 자율성
- 본 프로젝트 채택 의미: 자비스 = "중간 타협" 답습 영구 + 프라이데이 = "깊게 지향" 분담 = 메모리 `project_jarvis_local_boss_direction` 두 갈래 동시 실현

### 2.3 4 경로 재평가 답습

| 경로 | 헌법 변경 | 자비스 영향 | 자가진화 깊이 | 1인 개발 부담 | 현실성 |
|---|---|---|---|---|---|
| (A) Layer 2 발효 | 0 | 0 | "절반" | 낮음 | ⭐⭐⭐ |
| (B) Layer 3 신설 (자비스) | **필수 (8조 + ADR-011 §2.4)** | 직접 | "전체" | 매우 높음 | ⭐ |
| (C) Hermes PMO 격상 (자비스 옆) | (조건 충족) | 직접 | "Hermes 수준" | 매우 높음 | ⭐ |
| **(D) 프라이데이 별도 툴** ⭐ | **0 (자비스 격리)** | **0 (격리)** | "실험적 깊이" | 중간 | **⭐⭐⭐** |

**(D) 본질 우월성**: 자비스 4 invariant 보존 + 자가진화 깊이 실험 *양립*. 분리 자체가 Provider Liquidity 직접 입증 강화.

---

## 3. 프라이데이 scope 정의

### 3.1 형태 후보 2

| 형태 | 설명 | 장점 | 단점 |
|---|---|---|---|
| **(P) 자체 코드 별도 worktree** | `feature/friday-experimental` 또는 별도 repo. `src/friday/` 신설. 자비스 답습 + Layer 3 추가 | 자체 통제 강함, 외부 의존 0, lock-in risk 0 | 1인 개발 부담 ~10-15 cycle (Layer 3 자체 설계 + 구현) |
| **(Q) Hermes 자체 도입 + 격리** | Hermes 를 별도 worktree (`~/friday-hermes/`) 또는 별도 Docker container. 자비스 메모리 접근 0 강제 | Hermes 검증된 framework 활용, 12 조건 체크리스트 답습 가능 | lock-in 우려 = 프라이데이 한정 (자비스 무관), R1 risk = 프라이데이 격리 안 수용 |

### 3.2 공통 의무 (양 형태 동일)

1. **자비스 4 invariant 보존**: 헌법 8조 + ADR-011 §2.4 T3 + Boss = root of trust 아님 + Provider Liquidity 5조-2 — 본 brief 발효 후도 영구 보존
2. **격리 메커니즘 사전 정의**: §4 답습
3. **Rollback Trigger 사전 등록**: §6 답습
4. **Evidence 수집 의무**: §7 답습
5. **자비스 144/144 test green 답습**: 자비스 회귀 0건 보장

### 3.3 자비스와의 권위 관계

- 자비스 = **prod 권위**, 본업 의사결정 우선
- 프라이데이 = **실험 영역**, 자비스 결과 충돌 시 자비스 우선
- 두 툴 동일 task 결과 차이 시 = 자비스 답습 + 프라이데이 결과 = 참고 한정
- 프라이데이 자기 자율 학습 결과 = 자비스 본문 *제안*도 금지 (사용자 명시 결정 후 자비스 cycle 별도 진입 의무)

---

## 4. 격리 메커니즘 사전 정의

### 4.1 코드 격리 (D-3 결정 영역)

| 옵션 | 설명 | trade-off |
|---|---|---|
| (a) 같은 repo 별도 브랜치 | `feature/friday-experimental` 신규, `src/friday/` 신설. 자비스 brach (`feature/jarvis-mvp0` + `main`) 보호 | git history 통합, branch protection rule 별도 의무 |
| (b) 별도 repo | `friday/` 별도 git repo, 자비스 repo 와 무관 | 완전 격리, 권위 분리 명확, 단 cross-reference 불편 |
| (c) 같은 repo 같은 브랜치 + 디렉토리 격리 | `friday/` 디렉토리 신설, 자비스 main에서 진행 | 가장 가벼움, 단 격리 약함 (실수로 자비스 본문 변경 risk) |

**권고**: (a) 별도 브랜치 (자비스 main branch protection rule 침범 0 + git history 통합 + 권위 분리 명확)

### 4.2 메모리 격리

- 자비스 메모리 위치: `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/`
- 프라이데이 메모리 위치 후보:
  - (i) 자비스 메모리에 `friday_*` prefix 신설 (격리 약함)
  - (ii) 별도 폴더 `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/friday/` (격리 강함)
  - (iii) 완전 별도 디렉토리 `~/.claude/projects/.../friday-memory/` (격리 최강)

**권고**: (ii) 별도 폴더 (Claude Code 동일 프로젝트 내 격리)

### 4.3 workdir 격리

- 자비스 workdir prefix: `/tmp/jarvis-v00-*`, `/tmp/jarvis-mvp0-*`
- 프라이데이 workdir prefix: `/tmp/friday-*`
- Landlock 격리 = 자비스 동일 패턴 답습 (ll_sandbox 재사용)

### 4.4 endpoint 격리

- 자비스 사장 LLM: Ollama localhost:11434 (Qwen3-30B-A3B)
- 프라이데이 사장 LLM 후보:
  - (a) 별도 Ollama 포트 (`localhost:11435`) + 별도 모델 (예: glm-4.7-flash 또는 별도 fine-tuned)
  - (b) 같은 Ollama, 다른 모델 (포트 공유)
  - (c) Hermes 자체 endpoint ((Q) 형태 채택 시)

### 4.5 filesystem ACL (자비스 침범 0 보장)

- 프라이데이 워커가 자비스 `src/jarvis/`, `tests/jarvis/`, 자비스 MEMORY 폴더, ADR/헌법/roadmap 본문 변경 시도 시 **fail-closed**
- Landlock 격리 = workdir RO + 자비스 source 차단 (자비스 ll_sandbox 답습)
- audit log = 프라이데이가 자비스 영역 접근 시도 evidence 기록

### 4.6 commit 격리

- 프라이데이 commit = `feature/friday-experimental` 브랜치 한정
- 자비스 `main` branch protection rule = 11 workflow status check 의무 답습 → 프라이데이 commit 의 main 진입 = 동일 PR 자격 (단, 본 brief = 진입 자격 평가 한정, 실 적용 별도)

### 4.7 권위 분리 명문

| 영역 | 자비스 권위 | 프라이데이 권위 |
|---|---|---|
| 헌법 변경 | 자비스 cycle 의무 | **0** (프라이데이 변경 시도 = R-Friday-3 ROLLBACK trigger) |
| ADR-011 §2.4 변경 | 자비스 cycle 의무 | **0** (동일) |
| 자비스 본문 변경 제안 | 자비스 cycle | **0** (프라이데이 = 참고 한정, 자비스 cycle 별도 진입 의무) |
| 프라이데이 본문 변경 | (참고 한정) | 프라이데이 cycle |
| HW 자원 충돌 | **우선** | 후위 (자비스 idle 시점 운영) |

---

## 5. 진입 시점 stage gate

### 5.1 자비스 MVP-1 단계 완료 = 진입 자격 충족 시점

```
현재
  │
  ▼
자비스 carry-over 우선 진행 (자동 진입 0건, 사용자 명시 의무):
  ├─ (b1-AR3 첫 PR evidence) — 첫 PR open + 11 workflow PASS + admin bypass 0
  ├─ (b1-AR3 develop branch protection 적용)
  ├─ (c) MVP-1 Implementation Evidence PASS 발효 합의
  ├─ Layer 2 발효 결정 — (A) 채택 여부
  ├─ (b2) R-S1 권위 chain 정정
  ├─ (b3) framing 정정
  │
  ▼
자비스 MVP-1 단계 완료 = 자비스 설계 완료 시점
  │
  ▼  (사용자 명시 진입 의무, 자동 진입 0건)
프라이데이 진입 자격 평가 합의 cycle (본 brief 발효 자격)
  │
  ▼  풀 3+1 합의 + 외부 LLM 1+ (헌법 변경 인접 영역)
  │
  ▼  사용자 명시 (P)/(Q) 결정 + D-1 ~ D-8 결정
  ▼
프라이데이 MVP-0 설계 brief (별도 cycle)
```

### 5.2 진입 자격 *충족* ≠ 진입 *결정*

- 본 brief = 진입 자격 평가 한정
- 자비스 MVP-1 완료 후 = 진입 *자격* 충족
- 실 진입 *결정* = 사용자 명시 결정 + 합의 cycle 의무 (자동 진입 0건 영구)

---

## 6. Rollback Trigger 사전 등록

### R-Friday-1: 프라이데이 격리 침범

- **trigger**: 프라이데이가 자비스 `src/jarvis/`, `tests/jarvis/`, `MEMORY.md`, ADR/헌법/roadmap 본문 1건이라도 변경
- **대응**: 즉시 ROLLBACK + 격리 메커니즘 강화 별도 cycle 의무
- **답습**: filesystem ACL + audit log

### R-Friday-2: HW 자원 자비스 영향

- **trigger**: 프라이데이 사장 LLM 이 자비스 워커 OOM 유발 또는 자비스 응답 지연 ≥ 2배
- **대응**: 프라이데이 endpoint 정지 + HW 자원 분할 재설계 별도 cycle

### R-Friday-3: 자비스 4 invariant 침범

- **trigger**: 프라이데이가 헌법 8조 / ADR-011 §2.4 T3 / Boss = root of trust 아님 / Provider Liquidity 5조-2 4 invariant 1건이라도 침범 (제안 포함)
- **대응**: 즉시 프라이데이 정지 + 권위 분리 재명문 + 메모리 갱신

### R-Friday-4: R1 학습루프 폭주

- **trigger**: 프라이데이 격리 안 R1 평문 누적 ≥ 10MB 또는 민감 정보 평문 1건이라도 검출
- **대응**: 격리 강화 (SQLCipher 또는 동등) 또는 프라이데이 폐기

### R-Friday-5: cycle 비용 자비스 본업 정지

- **trigger**: 프라이데이 cycle 부담이 자비스 본업 (MVP-2+ 진행) 정지 ≥ 1주
- **대응**: 프라이데이 우선순위 강제 강등 + carry-over DEFER

---

## 7. Evidence 의무

| Evidence | 수집 시점 | 형태 |
|---|---|---|
| E-Friday-1: 자비스 4 invariant 보존 | 본 brief 발효 후 + 프라이데이 진입 후 매 cycle | git diff (헌법 / ADR / Protocol 본문 변경 0건) |
| E-Friday-2: 격리 메커니즘 작동 | 프라이데이 진입 후 첫 격리 PoC | filesystem ACL + workdir + endpoint 별도 작동 evidence |
| E-Friday-3: 자비스 144 tests green 답습 | 매 프라이데이 cycle 후 | `pytest tests/jarvis/` 144/144 PASS |
| E-Friday-4: 프라이데이 R1 차단 | 프라이데이 진입 후 첫 학습루프 cycle | SQLCipher 또는 동등 메커니즘 작동 evidence |
| E-Friday-5: 권위 분리 명문 | 본 brief 발효 후 | 프라이데이 cycle 결과 = 참고 한정, 자비스 본문 변경 제안 0건 |

---

## 8. ADR-011 §2.1 (a)~(e) 매트릭스

| 조건 | 본 brief 시점 | 충족 자격 |
|---|---|---|
| (a) 동등 이상 안전 결과 | 자비스 invariant 0건 변경 = 자비스 안전 결과 보존 | ✅ 본 brief 시점 충족 |
| (b) 격리 환경 PoC 실증 | 프라이데이 진입 후 별도 cycle 의무 | ⏳ 별도 cycle |
| (c) 회귀 검증 경로 | 자비스 144 tests green + 자비스 본문 변경 0건 의무 | ✅ 본 brief 시점 충족 |
| (d) 자동 회귀 검증 | 프라이데이 실 진입 후 별도 CI 검증 의무 | ⏳ 별도 cycle |
| (e) 운영 조건 | 사용자 명시 별도 cycle | ⏳ 별도 cycle |

**합산**: 본 brief 시점 = 2/5 충족 (a + c), 3/5 별도 cycle (b + d + e) = 진입 자격 평가 brief 답습 정합

---

## 9. 사용자 결정 항목 D-1 ~ D-8

| # | 결정 영역 | 권고 옵션 | 비고 |
|---|---|---|---|
| **D-1** | 진입 시점 | 자비스 MVP-1 단계 완료 후 | 사용자 framing 답습 |
| **D-2** | 형태 = (P) 자체 코드 vs (Q) Hermes 도입 vs 추후 결정 | (P) 권고 (lock-in 0 + 자체 통제 강) | (Q) = Hermes lock-in 우려 = 프라이데이 한정 격리 |
| **D-3** | 코드 격리 = (a) 같은 repo 별도 브랜치 vs (b) 별도 repo vs (c) 같은 repo 디렉토리 | (a) 권고 | branch protection rule 별도 의무 |
| **D-4** | 메모리 격리 = (i) prefix vs (ii) 별도 폴더 vs (iii) 별도 디렉토리 | (ii) 권고 | Claude Code 동일 프로젝트 내 격리 |
| **D-5** | HW 자원 = 동시 운영 vs 자비스 idle 시점만 | 자비스 idle 시점만 권고 (R-Friday-2 risk 회피) | 별도 endpoint 포트 의무 |
| **D-6** | 비례성 메모리 처리 | 자비스 한정 명문 갱신 (`feedback_proportionate_security_personal_tool` body 에 "자비스 한정" 추가) + 프라이데이 별도 메모리 신설 | 메모리 충돌 해소 |
| **D-7** | 합의 형태 | 풀 3+1 + 외부 LLM 1+ 권고 | 큰 결정 + 헌법 인접 영역 |
| **D-8** | 본 brief commit 시점 | 사용자 검토 후 | 단계별 합의 cycle 답습 |

---

## 10. 합의 형태 권고

### 10.1 풀 3+1 + 외부 LLM 1+ 권고

- **CLAUDE.md §3 매트릭스 답습**:
  - 큰 결정 (자가진화 깊이 + 자비스 invariant 보존 양립) = 풀 3+1 필수
  - 헌법 인접 영역 (ADR-011 §2.4 T3 인접) = 외부 LLM 1+ 의무
- **5/5 풀 3+1 승격 trigger 검증** (Reviewer-only 단축 불가):
  - ① 새 권위 결정 발생 = ✅ (프라이데이 신규 툴 권위)
  - ② Tier-2/3 자동 확장 영향 = (해당 없음)
  - ③ PASS 자동 선언 = (해당 없음)
  - ④ 후속 합의 본문 변경 = ✅ (자비스 MVP-1 carry-over 흡수)
  - ⑤ ADR-011 5조건 자동 충족 = ✅ (격리 메커니즘 자동 충족 선언 risk)

→ **5/5 중 3/5 발화 = 풀 3+1 필수 + 외부 LLM 1+ 권고**

### 10.2 외부 LLM 1+ method 후보

- (B) Claude 가 tmux + codex bypass sandbox 직접 호출 (24번째 entry 답습)
- (α) 또는 사용자 직접 외부 LLM 호출 + 응답 첨부

---

## 11. carry-over

### 11.1 본 brief 발효 후 (사용자 명시 의무, 자동 진입 0건)

1. **자비스 carry-over 우선 진행**:
   - (b1-AR3 첫 PR evidence) — 첫 PR open 시 11 workflow PASS
   - (b1-AR3 develop branch protection 적용)
   - (c) MVP-1 Implementation Evidence PASS 발효 합의
   - Layer 2 발효 결정 — (A) 채택 여부
   - (b2) R-S1 권위 chain 정정 + (b3) framing 정정
2. **자비스 MVP-1 단계 완료 후** = 프라이데이 진입 자격 충족
3. **본 brief 합의 cycle** (풀 3+1 + 외부 LLM 1+, 사용자 명시 진입)
4. **합의 후 D-1 ~ D-8 사용자 명시 결정**
5. **프라이데이 MVP-0 설계 brief** (별도 cycle, 자동 진입 0건)

### 11.2 메모리 저장 의무

- 본 결정 = `project_friday_separate_evolution_direction` 신규 메모리 저장 자격 (project type, 사용자 명시 방향 결정)
- 비례성 메모리 갱신 = D-6 결정 후 별도 cycle

---

## 12. 자기진단 8/8

| # | 자기진단 항목 | 결과 |
|---|---|---|
| 1 | 헌법 본문 변경 0건 | ✅ |
| 2 | ADR 본문 변경 0건 | ✅ |
| 3 | `src/jarvis/` + `tests/jarvis/` 본문 변경 0건 | ✅ |
| 4 | `.github/workflows/` + `.pre-commit-config.yaml` 본문 변경 0건 | ✅ |
| 5 | branch protection rule 변경 0건 | ✅ |
| 6 | 자비스 4 invariant (헌법 8조 + ADR-011 §2.4 T3 + Boss = root of trust 아님 + Provider Liquidity) 침범 0건 | ✅ |
| 7 | 본 cycle 자동 다음 단계 진입 0건 (브리프 작성 후 사용자 명시 의무 답습) | ✅ |
| 8 | ceremony-inflation 회피 (본 brief = entry brief 한정, 별도 cycle 명문 분리) | ✅ |

---

## 13. 답습 영구 권위

- ⭐⭐⭐ **자비스 4 invariant 영구 보존** (헌법 8조 + ADR-011 §2.4 T3 + Boss = root of trust 아님 + Provider Liquidity 5조-2)
- ⭐⭐⭐ **프라이데이 = 자비스 *침범 0* 격리** (filesystem ACL + workdir + endpoint + 메모리 + commit 5 layer 격리)
- ⭐⭐ **본 brief = 진입 자격 평가 한정** (실 진입 결정 0건, 자동 진입 0건)
- ⭐⭐ **자비스 MVP-1 단계 완료 후 진입 자격 충족** (사용자 framing 답습)
- ⭐⭐ **풀 3+1 + 외부 LLM 1+ 합의 의무** (5/5 trigger 3/5 발화)
- ⭐ **R-Friday-1 ~ R-Friday-5 Rollback Trigger 사전 등록**
- ⭐ **Marvel narrative 정합 = 두 갈래 동시 (Jarvis 보수적 + Friday 실험적)**
- ⭐ **본 brief 자체 머신 변경 0건** (코드 / 테스트 / CI / hook / branch protection / ADR / 헌법 / roadmap 본문 모두 변경 0건)

---

**본 brief 종결** (진입 자격 평가 한정. 실 진입 = 자비스 MVP-1 완료 후 + 풀 3+1 + 외부 LLM 1+ 합의 + D-1 ~ D-8 사용자 명시 결정 의무. 자동 진입 0건 영구 답습.)
