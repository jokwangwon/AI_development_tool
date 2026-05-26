# 3+1 Consensus — Phase 3.5-OM (h-OM) Ollama Modelfile (h) bartowski GGUF 등록 cycle entry brief v1

> **본 합의 = (h-OM) brief v1 (`3d02edb`, 469줄) 에 대한 풀 3+1 멀티 에이전트 합의**. Agent A (구현 분석가) + Agent B (품질·안전성 검증가) + Agent C (대안 탐색가) 병렬 독립 분석 후 Reviewer 통합. 3 Agent 모두 **APPROVE w/ COND** 일치 (정면 충돌 0건 = 강한 정합성). **Reviewer 단독 격상 R-S1~R-S5 raw line-level direct cross-check + 외부 raw evidence (Ollama issue #1450 + docs.ollama.com/import)** + BLOCKING 15 (3-way 일치 2 + 2+ Agent 일치 4 + Agent 단독 9) + Reviewer 권고 16 + NOTE 18 + 기각 5. 본 합의 = brief v1.1 보강 input 영구 권위, 본문 변경 0건. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5-O (h-O) cycle 정리 commit `9685ae3` + (h-OM) brief v1 commit `3d02edb` 직후, 본 cycle 단계 (2) 풀 3+1 합의)
**카테고리**: Phase 3.5-OM (h-OM) entry brief v1 합의 보고서 (Reviewer 통합)
**범위**: brief v1.1 보강 의무 BLOCKING 15 + R-S 5 + 권고 16 + NOTE 18 + 기각 5 매트릭스. 본 합의 자체 머신 변경 0건.

**답습 권위**:
- (h-OM) brief v1 (`3d02edb`, 469줄, 검토 대상)
- (h-O) Phase 3.5-O cycle 합의 (`37bcd40`, 459줄, BLOCKING 14 + R-S1~R-S5) — 본 합의 구조 답습 source 영구
- (h-O) cycle 정리 commit (`9685ae3`, 16번째 entry, S1 confirmed Ollama < llama.cpp ~3.24~23.89×)
- (h-O) brief v1.1 (`e77e8d7`, 476줄)
- (h-O) raw summary (`docs/phase0/v1-poc-raw/phase3-5-h-o/2026-05-25T21-03-phase3-5-h-o-summary.json`)
- (h) Phase 3.5-B cycle 정리 commit (`fccec6a`, 15번째 entry)
- (g) Phase 3.5 cycle 정리 commit (`b3d4164`, 14번째 entry)
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- **외부 raw evidence (Reviewer 통합 cross-check)**: Ollama issue #1450 (closed-as-not-planned) + docs.ollama.com/import + Markaicode guide

---

## 0. 본 합의가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. 3 Agent 독립 출력 통합 매트릭스 (§2) + Reviewer 단독 격상 R-S1~R-S5 raw line-level direct cross-check + 외부 raw evidence 통합 (§3)
2. BLOCKING 15 통합 (3-way 일치 2 + 2+ Agent 일치 4 + Agent 단독 9) — brief v1.1 보강 verbatim 100% 의무 명문 (§4·§5)
3. 권고 16 매트릭스 (§6) + NOTE 18 carry-over (§7) + 기각 5 (§8)
4. Reviewer 권한 한계 답습 영구 (§9) + 본 합의 차단 조건 (§10)
5. brief v1.1 보강 의무 (§11) + 다음 단계 carry-over (§12)
6. 본 합의 자체 영구 권위 (§13)

### 하지 않는 것 (영구 답습)

1. ❌ **본 합의 자체로 brief v1.1 보강 / Modelfile / ollama create / 측정 / sudo 실행**
2. ❌ **Ollama daemon 상태 변경**
3. ❌ **brief v1 본문 직접 변경**
4. ❌ **기존 (g)/(h)/(h-O) brief / 합의 본문 자동 정정**
5. ❌ **MVP-1 합의 / 헌법 / ADR 본문 자동 정정** (R-9 답습 영구)
6. ❌ **본 합의 BLOCKING 추가 격상 또는 새 R-S 자동 신설** (Reviewer 권한 한계 (1) 답습 영구)
7. ❌ **새 verbatim 인용 신설 자격 0** (Reviewer 권한 한계 (10-i) 답습 영구)
8. ❌ **본 합의 후속 자동 진입 0**
9. ❌ **메모리 자동 갱신**
10. ❌ **chain 영구 종결 의무 답습 영구**

---

## 1. 합의 결과 요약

### 1.1 종합 평가

**APPROVE w/ COND** (3 Agent 일치, 정면 충돌 0건 = 강한 정합성).

- Agent A: APPROVE w/ COND, BLOCKING 8 + 권고 6 + R-S 4 + NOTE 4
- Agent B: APPROVE w/ COND, BLOCKING 9 + 권고 8 + R-S 2 + NOTE 6
- Agent C: APPROVE w/ COND, BLOCKING 3 + 권고 8 + R-S 3 + NOTE 7

### 1.2 핵심 finding 5 (Reviewer 단독 격상 R-S 통합)

⭐⭐⭐ **R-S1 CRITICAL** = **3-way 일치 (A-B2 + B-S1 + C-S1) + 외부 raw evidence**: brief 의 가장 강한 정량적 단언 **"hard link 동일 inode = 디스크 추가 0건"** 이 외부 raw evidence (Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "**ollama create performs a regular copy of the .gguf file ... first step of a GGUF import is copying the binary to the model directory with a hashed name**") 와 **정면 충돌**. Ollama `ollama create` 표준 동작 = FROM local file 시 자체 blob storage 으로 copy 강한 가능성 → **디스크 +17.3 GiB 추가 risk 강한 시사** (본 cycle 자체 차단 0, 단 framing 정정 의무).

⭐⭐ **R-S2 HIGH** = Agent A direct verify (A-B1/A-S1) + Reviewer raw cross-check: (h-O) summary `"cumulative_total": 19` ↔ brief §0 #2 "19회" + §2.2 "(h-O) 19 + 본 4 = 23" + §3.1 Step 5 "**누계 20 + 1 = 21**" — **3 위치 self-inconsistency**. 본 cycle 첫 anchor = **20x** (not 21x), 마지막 = **23x** verbatim 정정 의무.

⭐⭐ **R-S3 HIGH** = **3-way 일치 (A 부분 + B-B6/B-S2 + C-B2/C-S2)**: brief §1.1 "**inference engine *진짜* 단독 분리**" + §0 #31 + §9.3 "*진짜* 단독 분리 시도" framing = (h-O) R-S5 답습 영구 R-4 framing (PASS/FAIL 금지) 위반 risk. 4 미통제 변수 (§6 #3) + R-S1 발효 source conversion 변수 *추가* 미통제 (Modelfile 처리 모드 unknown) → "*진짜* 단독" 단언 약화 의무.

⭐ **R-S4 MEDIUM** = A-B5 + B-B3 + C-B3 통합 (`ollama create` FROM 처리 모드 3종): (1) 그대로 참조 / (2) 자체 blob 으로 copy 후 sha256 (content-addressable) / (3) re-quantize. 사전 평가 자격 0, post-create `ollama show --modelfile` + `stat -c '%i %s' <blob>` + (h) sha256 cross-check 의무 + Ollama embedded llama.cpp version verify step 부재 ((h-O) R-S4 답습).

⭐ **R-S5 MEDIUM** = Agent A 단독 (A-B4/A-S2): Modelfile LICENSE block 답습 부재 ((h-O) `ollama show` raw line 61~86 = `LICENSE """ Apache License Version 2.0 ...` 답습 미반영) + Modelfile 명칭 `qwen3-30b-a3b-instruct-2507-bartowski` `:latest` tag 자동 부여 명문 부재 + Hard link 후 file 권한 verify 절차 부재 ((h) GGUF `delangi:delangi 0664` ↔ ollama-data `root:root 0755` 격차).

### 1.3 본 cycle 진행 자격 평가

- ✅ 본 cycle 핵심 가치 (source conversion 통제 *시도* + 3-way 비교 framing) = framing 정합 강함
- ❌ R-S1 발효 = "디스크 0건" 단언 약화 의무 (B4 분기 강화 + framing 약화) — 본 cycle 자체 차단 0, framing 정정만
- ❌ R-S2 발효 = R-1 anchor 산술 모순 다중 위치 정정 의무
- ❌ R-S3 발효 = "진짜 단독 분리" 단언 약화 의무
- ❌ R-S4 발효 = §3.1 + §3.3 verify step 보강
- → **brief v1.1 보강 (BLOCKING 15 + R-S 5 + 권고 16 + 기각 5) 후 진입 자격 강함**

---

## 2. 3 Agent 출력 요약 표

| 차원 | Agent A | Agent B | Agent C |
|---|---|---|---|
| 종합 평가 | APPROVE w/ COND | APPROVE w/ COND | APPROVE w/ COND |
| 핵심 강점 | raw direct verify (`df -T` + `ls -la` + inode) | §0 ↔ §7 1:1 매핑 + sudo 정합성 | 외부 raw evidence (Ollama issue #1450 + docs) |
| 핵심 발견 | R-1 anchor 산술 모순 (A-B1) | source 100% 통제 framing 약화 (B-B6) | hard link Ollama #1450 closed (C-S1) |
| BLOCKING 수 | 8 | 9 | 3 |
| 권고 수 | 6 | 8 | 8 |
| R-S | 4 | 2 | 3 |
| NOTE | 4 | 6 | 7 |
| 직접 raw verify | (h) GGUF inode/permission + (h-O) cumulative_total | (h-O) brief v1.1 line-level + sudo 5~7회 답습 | Ollama issue #1450 + docs.ollama.com WebSearch |
| 단언 강도 약화 framing 답습 | ✓ | ✓ | ✓ |
| PASS/FAIL framing 금지 답습 | ✓ | ✓ | ✓ |

---

## 3. Reviewer 단독 격상 R-S1~R-S5 (raw line-level direct cross-check + 외부 raw evidence)

### 🔴 R-S1 ⭐⭐⭐ CRITICAL — hard link "디스크 추가 0건" 가정 약화 의무 (3-way 일치 + Ollama 공식 evidence)

**raw evidence (Agent A + Agent B + Agent C 3-way 일치 + Reviewer 외부 evidence 통합)**:

1. **brief 단언 위치**:
   - §1.1 line 74 verbatim: "본 cycle 비용: egress **0건** (host (h) GGUF 답습 hard link) + 디스크 **0건** (hard link 동일 inode, 동일 filesystem `/dev/nvme0n1p2 ext4` 답습) + Ollama models cache blob storage 증가 가능성 verify 의무"
   - §0 #16 + §3.0.1 line 137 + §6 #7 "디스크 추가 0건 답습 — hard link 동일 inode" 답습
2. **외부 raw evidence (Agent C WebSearch + Reviewer 통합)**:
   - **Ollama GitHub issue #1450** ("Use hard link to import GGUF on the same host to save disk space") = **closed as not planned**
   - **docs.ollama.com/import** verbatim: "ollama create performs a **regular copy** of the .gguf file ... first step of a GGUF import is copying the binary to the model directory with a hashed name"
   - Markaicode guide 답습 동일 정합
3. **결과**: Ollama `ollama create` FROM local file 시 자체 blob storage 으로 **standard copy** 강한 가능성. hard link 후 ollama create → `blobs/sha256-<rehash>` 신규 blob ~17.3 GiB 추가 발생 강한 시사
4. **단 sha256 = content-addressable**: 동일 content (h) sha256 = `382b4f5a164d...` → Ollama blob sha256 답습 자격 강함 (content 동일 시 sha256 동일). 단 *디스크는* 두 곳 (host hard link inode + Ollama blob copy inode) 발생 → 17.3 GiB 추가 risk

**격상 사유**:
- 3-way 일치 + 외부 Ollama 공식 evidence = 매우 강한 confidence
- brief 의 가장 강한 정량적 단언 자체가 falsify risk
- 본 cycle 자체 차단 0 (디스크 251G free 답습, 17 GiB 추가 = ~234G 가용), 단 framing 정정 의무

**brief v1.1 정정 의무 위치 (5 곳)**:
1. §1.1 line 74 정정 = "egress **0건** (host (h) GGUF 답습 hard link) + 디스크 **0건 또는 ~17.3 GiB 추가 (Ollama 자체 blob copy 동작 시, Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import 'regular copy' 답습, 사전 평가 0)**"
2. §0 #16 정정 = 동상
3. §3.0.1 line 137 정정 = 동상
4. §6 #7 강화 = "Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import 표준 'regular copy' 답습 영구 — `ollama create` 시 자체 blob copy 강한 가능성. content-addressable sha256 답습 시 (h) sha256 일치 자격 강함, 단 디스크 두 곳 발생 정직성 명문"
5. §5 B4 분기 강화 = "디스크 부족 또는 **`ollama create` 후 ~17.3 GiB 추가 발생**" trigger + raw report + B4 분기 발효 의무

### 🔴 R-S2 ⭐⭐ HIGH — R-1 anchor 산술 내부 모순 (A-S1 raw verify)

**raw evidence (Agent A direct verify + Reviewer cross-check)**:

1. **(h-O) summary line 100 verbatim**: `"cumulative_total": 19`
2. **brief 단언 위치 (3 곳 모순)**:
   - §0 #2 line 39 verbatim: "(19회 누계 답습 영구)"
   - §2.2 line 126 verbatim: "**(h-O) 4회 추가 = 누계 19회** + 본 cycle (h-OM) 4회 추가 = 23회 누계 종료 시점"
   - §3.1 Step 5 line 148 verbatim: "**R-1 anchor 21회 추가** — `sudo sha256sum /proc/3375/exe` (**누계 20회 + 본 cycle 1회 = 21회**, hash baseline `ce95c475...878b10` 일관 답습 영구)"
3. **모순 분석**:
   - (h-O) cumulative_total = 19 → 본 cycle 첫 anchor = 19+1 = **20x** (not 21x)
   - 본 cycle 종료 시점 = 19+4 = **23x** (line 126 정합)
   - 단 line 148 "20 + 1 = 21" = 1회 over 표기
4. **다중 위치 정정 의무**: line 39 "19회" + line 148 "21회" + 모든 후속 21·22·23·24 표현 → **20·21·22·23** verbatim 정정

**brief v1.1 정정 의무 위치 (6+ 곳)**:
1. §0 #2 line 39 = "19회 → 20회 누계 답습 영구"
2. §3.1 Step 5 line 148 = "R-1 anchor 20회 추가 — (h-O) 누계 19회 + 본 cycle 1회 = 20회"
3. §3.3 Step 5 line 245 = "R-1 anchor 21회"
4. §4.1 line 258 = "R-1 anchor 22회"
5. §4.3 line 304 = "R-1 anchor 23회"
6. §2.2 line 126 framing simplify

### 🔴 R-S3 ⭐⭐ HIGH — "진짜 단독 분리" 단언 framing (h-O) R-S5 답습 R-4 위반 risk

**raw evidence (Agent A 부분 + Agent B-B6/B-S2 + Agent C-B2/C-S2 3-way 일치)**:

1. **brief 단언 위치**:
   - §1.1 line 66 verbatim: "**source conversion lineage 100% 통제 + inference engine *진짜* 단독 분리**"
   - §0 #1 verbatim: "inference engine 변수 *진짜* 단독 분리"
   - §9.3 line 451 verbatim: "본 cycle = source conversion 100% 통제 + inference engine *진짜* 단독 분리 시도"
2. **(h-O) R-S5 답습 영구**: "본 프로젝트 최초 단일 변수 분리" → "*부분* 변수 분리 시도" 약화 답습 영구 R-4 framing (PASS/FAIL 금지) 답습
3. **본 cycle 미통제 변수**: §6 #3 4 항목 (측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이) + **R-S1 발효 Modelfile FROM 처리 모드 미해소 (5번째 미통제 변수)** + §6 #18 Ollama Modelfile vs library internal pipeline 차이 (6번째 미통제 변수)
4. **격차**: §9.3 "시도" 표현 = R-S5 답습 부분 정합, §1.1/§0 "*진짜*" 강조 표현 = R-4 framing 약화 의무

**brief v1.1 정정 의무 위치 (3 곳)**:
1. §1.1 line 66 약화 = "source conversion 통제 *최대화* + inference engine **부분 단독 분리 시도**"
2. §0 #1 (하는 것) 약화 = "inference engine 변수 *부분* 단독 분리 시도"
3. §9.3 line 451 강화 = "본 cycle = source 통제 최대화 + inference engine *부분* 단독 분리 시도 — **5+ 미통제 변수 잔존** (§6 #3 4 + R-S1 Modelfile 처리 모드 1 + §6 #18 Ollama internal pipeline 1)"

### 🔴 R-S4 ⭐ MEDIUM — `ollama create` FROM 처리 모드 3종 사전 평가 0 + embedded version verify step 부재

**raw evidence (A-B5 + B-B3 + C-B3 통합)**:

1. **Ollama `ollama create` FROM local file 처리 모드 3종**:
   - (1) 그대로 참조 (host hard link inode 답습) — 가능성 낮음 (Ollama 비표준)
   - (2) **자체 blob 으로 copy 후 sha256 (content-addressable)** — Ollama 표준 동작 (R-S1 답습)
   - (3) re-quantize — quant scheme 변경 시 (본 cycle 미적용 가설, FROM = GGUF Q4_K_M 답습)
2. **sha256 content-addressable**: Ollama 가 blob 을 byte-by-byte hash → 동일 content 동일 sha256 → (h) bartowski sha256 `382b4f5a164d...` 답습 자격 강함 (단 verify 의무)
3. **§3.1 사전 조건 step 부재 (B-B3 답습)**: Ollama embedded llama.cpp version verify step 부재 ((h-O) brief v1.1 §3.1 Step 7 답습 강화 의무)

**brief v1.1 정정 의무 위치 (3 곳)**:
1. §6 #4 강화 = "Ollama `ollama create` FROM local file 처리 모드 3종 — (1) 그대로 참조 / (2) 자체 blob 으로 copy 후 sha256 답습 (content-addressable, R-S1 답습 표준) / (3) re-quantize. 사전 평가 0, post-create 직접 verify 의무"
2. §3.1 신규 Step (Step 7 추가) = "Ollama embedded llama.cpp version verify — `curl -s http://127.0.0.1:11434/api/version` + `sudo docker exec oracle-game-ollama ollama --version` 답습 (사용 가능 시) 명문 ((h-O) brief v1.1 §3.1 Step 7 답습)"
3. §3.3 Step 3 강화 = "Ollama Modelfile blob digest verify + **`stat -c '%i %s' <blob>` 답습 inode 비교** (host (h) GGUF inode 와 동일 시 hard link 실효 ✓ / 다름 시 standard copy 답습 + 디스크 추가 정직성 명문)"

### 🔴 R-S5 ⭐ MEDIUM — Modelfile LICENSE 답습 부재 + tag 자동 부여 + 권한 verify

**raw evidence (Agent A-A2/A-A3/A-B4/A-B7/A-S2/A-S3)**:

1. **Modelfile LICENSE block 답습 부재** ((h-O) `phase3-5-h-o-show.txt` line 61~86 = `LICENSE """ Apache License Version 2.0...` 답습 source) — brief §3.2 Step 3 line 172~228 = LICENSE 0건 (의도적 부분 답습 명문 0)
2. **tag 자동 부여 명문 부재** = `ollama create qwen3-30b-a3b-instruct-2507-bartowski` 후 Ollama 가 `:latest` 자동 부여 자격 강함, §3.3 Step 1 verify 명문 0
3. **Hard link 권한 verify 절차 부재** = (h) GGUF `delangi:delangi 0664` ↔ ollama-data `root:root 0755`, hard link 후 권한 = inode 답습 `delangi:delangi 0664` → Ollama daemon (Docker root) read 가능 자격 강함 (o+r=4), 단 명문 verify 부재

**brief v1.1 정정 의무 위치 (4 곳)**:
1. §1.3 line 92 명문 = "Modelfile TEMPLATE + 6 PARAMETER 답습 (의도적 부분 답습, **LICENSE block 의도적 0건** = Ollama Modelfile create 시 optional 답습)"
2. §3.2 Step 4 명문 = "tag 자동 부여 시 (`:latest`) 정확 식별자 §3.3 Step 1 verify 의무"
3. §3.3 Step 1 강화 = "tag 자동 부여 (e.g., `:latest`) 정확 식별자 확인 + §4.2 model name 일치성 verify 의무"
4. §3.2 Step 2 후속 신규 verify = "Hard link 후 권한 verify — `ls -li <link_path>` + 권한·소유자·inode 출력 + `sudo docker exec oracle-game-ollama stat /root/.ollama/imports/<file>` 답습 container 내 read 가능성 직접 verify"

---

## 4. BLOCKING — 3-way Consensus + 2+ Agent 일치 (6건)

### 🔴 R-1 ⭐⭐⭐ CRITICAL [3-way Consensus] — hard link "디스크 0건" 가정 약화 + Ollama issue #1450 evidence
- **답습**: A-B2 + B-S1 + C-S1 통합 → **R-S1 발효** (위 §3.1 답습)
- **정정 방향**: §3.1 답습 (5 곳 verbatim 정정 의무)

### 🔴 R-2 ⭐⭐ HIGH [3-way Consensus] — "진짜 단독 분리" 단언 (h-O) R-S5 답습 R-4 위반
- **답습**: A 부분 + B-B6/B-S2 + C-B2/C-S2 통합 → **R-S3 발효** (위 §3.3 답습)
- **정정 방향**: §3.3 답습 (3 곳 약화)

### 🔴 R-3 ⭐⭐ HIGH [2+ Agent, A-B5 + B-B3 + C-B3] — `ollama create` FROM 처리 모드 + embedded version verify
- **답습**: → **R-S4 발효** (위 §3.4 답습)
- **정정 방향**: §3.4 답습 (3 곳)

### 🔴 R-4 ⭐⭐ HIGH [Agent A 단독 + Reviewer raw verify] — R-1 anchor 산술 모순 (3 위치 self-inconsistency)
- **답습**: → **R-S2 발효** (위 §3.2 답습)
- **정정 방향**: §3.2 답습 (6+ 곳 verbatim 정정)

### 🔴 R-5 ⭐ MEDIUM [2+ Agent, A-B4/A-S2 + B] — Modelfile LICENSE 답습 부재 + tag 자동 부여 + 권한 verify
- **답습**: → **R-S5 발효** (위 §3.5 답습)
- **정정 방향**: §3.5 답습 (4 곳)

### 🔴 R-6 ⭐ MEDIUM [2+ Agent, A-B8 + B] — egress baseline mid/post 측정 명문 부재
- **위치**: brief §3.1 Step 1 + §4 측정 종료 후
- **(h-O) raw 답습**: pre/mid/post 3회 baseline (cumulative line 109~111)
- **정정 방향**: §3.1 + §4 측정 종료 후 step 추가 = egress baseline post 측정 + delta 산출 + intentional egress = 0건 verify

---

## 5. BLOCKING — Agent 단독 (Reviewer raw verify 인정, 9건)

### 🔴 R-7 [Agent B 단독] — §5 B2 sub-trigger 3 묶음 self-inconsistency
- **답습**: B-B2 ((h-O) brief v1.1 R-10 답습)
- **정정 방향**: §5 B2 = FROM path 미발견 / GGUF parse / Ollama internal 검증 sub-trigger 별도 행 분리

### 🔴 R-8 [Agent A 단독 + Reviewer raw] — Ollama `ollama create` FROM 처리 모드 사전 평가 0 (R-S4 통합)
- **답습**: → R-3 (R-S4 발효) 통합

### 🔴 R-9 [Agent B 단독] — §5 B4 sub-trigger 분리 (hard link 0건 vs Ollama blob copy +17.3 GiB)
- **답습**: → R-1 (R-S1 발효) 통합 (B4 분기 강화)

### 🔴 R-10 [Agent A 단독] — Modelfile LICENSE block 답습 부재 (R-S5 통합)
- **답습**: → R-5 (R-S5 발효) 통합

### 🔴 R-11 [Agent B 단독] — §0 ↔ §6 cross-check (§0 *하는* 것 8 항목 ↔ §6 정직성 18 항목)
- **위치**: brief §0 "하는 것" 8 항목 vs §6 정직성 18 항목
- **정정 방향**: §0 *하는* 것 8 항목 명문이 §6 정직성 한계 18 항목 답습 1:1 매핑 강화 의무 명문

### 🔴 R-12 [Agent B 단독] — password 누출 grep verify 명문 부재
- **(h-O) raw 답습**: line 124 `grep -r 'epffkddl' ... → 0건 적중 ✓`
- **정정 방향**: §3.3 / §4 verify step 명문 추가 ((h-O) 답습 영구)

### 🔴 R-13 [Agent B 단독] — model name conflict pre-verify 부재
- **위치**: brief §3.2 Step 4 + §3.3 Step 1
- **정정 방향**: §3.3 신규 Step = `ollama list | grep -i bartowski` pre-verify 추가 (기존 model 명칭 충돌 risk)

### 🔴 R-14 [Agent A 단독] — Hard link 후 권한 verify 절차 부재 (R-S5 통합)
- **답습**: → R-5 (R-S5 발효) 통합

### 🔴 R-15 [Agent C 단독] — §8.2 (h-OL) llama.cpp Ollama blob 직접 측정 cycle 신규 carry-over 누락
- **위치**: brief §8.2 carry-over 매트릭스
- **정정 방향**: §8.2 신규 carry-over = "(h-OL) llama.cpp Ollama blob 직접 측정 cycle" MEDIUM (egress 0 + 시간 ~30분 + source 통제 차원 *역방향* 단독 분리)

---

## 6. 권고 매트릭스 (16 권고, R-rec-1~R-rec-16)

| # | 권고 | source | 흡수 위치 |
|---|---|---|---|
| R-rec-1 | §3.1 사전 Step 7 신규 (Ollama embedded llama.cpp version verify) | A-rec-1 + B-rec-1 + R-S4 통합 | §3.1 신규 step |
| R-rec-2 | §5 B2 sub-trigger 3 묶음 분리 | A-rec-2 + B-rec-2 + R-7 | §5 B2 행 분리 |
| R-rec-3 | §6 #2 단언 강도 약화 framing | A-rec-4 + B-rec-3 + C-rec-5 + R-S3 통합 | §6 #2 + §1.1/§0/§9.3 |
| R-rec-4 | §3.3 Step 6 또는 신규 Step Ollama blob storage 자체 변환 verify command 명문 | A-rec-6 + B-rec-4 + R-S4 통합 | §3.3 Step 3·6 강화 |
| R-rec-5 | §3.3 신규 Step model 명칭 conflict pre-verify (`ollama list \| grep`) | A-rec-5 + B-rec-5 + R-13 | §3.3 신규 step |
| R-rec-6 | §4 / §3.3 password 누출 grep verify 명문 | B-rec-6 + R-12 | §4 / §3.3 명문 |
| R-rec-7 | §3.2 sudo 필요성 근거 명문 강화 | B-rec-7 | §3.2 Step 1·2 |
| R-rec-8 | §5 신규 분기 (hard link permission / Ollama daemon access 거부) | B-rec-8 | §5 분기 매트릭스 |
| R-rec-9 | §3.0 sudo "6~8회" → "8~10회" (egress post + 권한 verify 추가) | A-rec-2 (확장) | §3.0 line 134 |
| R-rec-10 | §5 B4 = "디스크 부족 또는 ollama create 후 ~17 GiB 추가" | A-rec-3 + R-rec-9 + R-S1 | §5 B4 강화 |
| R-rec-11 | §3.3 Step 1 tag 자동 부여 (`:latest`) 확인 | A-rec-5 + R-S5 | §3.3 Step 1 강화 |
| R-rec-12 | §6 #18 강화 = Modelfile FROM 처리 모드 3종 사전 평가 0 | A-rec-6 + R-S4 | §6 #18 |
| R-rec-13 | §1.1 framing 약화 = "*진짜* 단독" → "*최대화* 시도" | C-rec-5 + R-S3 | §1.1 line 66 |
| R-rec-14 | §2.1 OM-direct-blob 신규 후보 추가 (Ollama manifest 우회) | C-rec-6 | §2.1 표 신규 행 |
| R-rec-15 | §8.2 신규 carry-over = "(h-OL) llama.cpp Ollama blob 직접 측정 cycle" MEDIUM | C-rec-7 + R-15 | §8.2 신규 |
| R-rec-16 | §8.2 4-way 통합 *분석* cycle scope 명문 4 차원 | C-rec-8 | §8.2 강화 |

권고 우선순위 = R-rec-1 / R-rec-2 / R-rec-3 / R-rec-4 / R-rec-10 / R-rec-13 / R-rec-15 (강함) > 다른 (중간 / 약함, by-reference).

---

## 7. NOTE (carry-over, 18건, 본 cycle 외)

| # | NOTE | source | 우선순위 |
|---|---|---|---|
| N-1 | 본 brief commit + push 자동 진입 0건 영구 | A-N 답습 | 영구 |
| N-2 | (h-OM) ≈ (h-O) 시 source conversion 차이 무관 → MVP-1 R4 framing 정정 강한 input | A-N-1 부분 | MEDIUM |
| N-3 | "최초 source conversion 100% 통제" 단언 약화 의무 검토 (R-S3 답습) | A-N-2 + R-S3 | NOTE |
| N-4 | §6 #7 디스크 추가 0건 self-consistency 위반 (R-S1 통합 정정) | A-N-3 + R-S1 | (정정) |
| N-5 | Ollama 가 GGUF tokenizer 사용 자격 강함 가설 (bartowski GGUF 내장 tokenizer 답습) | A-N-4 | NOTE |
| N-6 | §0 ↔ §6 cross-check 영역 (R-11 통합) | B-N-1 + R-11 | NOTE |
| N-7 | "최초 source conversion 100% 통제 cycle" 단언 R-S5 답습 평가 (R-S3 통합) | B-N-2 + R-S3 | NOTE |
| N-8 | §3.1 R-1 anchor 21회 framing 복잡 simplify (R-S2 통합) | B-N-3 + R-S2 | (정정) |
| N-9 | §6 18 항목 vs (h-O) 20 항목 정합 (R-S4/R-S5 별도 framing 답습) | B-N-4 | NOTE |
| N-10 | §9.2 6 시나리오 vs (h-O) 10 시나리오 통합 simplify 정합 | B-N-5 | NOTE |
| N-11 | §8.1 본 cycle 결과 분기 S4 (≈ h) 시나리오 누락 framing | B-N-6 | LOW |
| N-12 | §8.2 (g)+(h)+(h-O)+(h-OM) 4-way 통합 *분석* cycle ≠ 통합 *본문 정정* cycle ((h-O) N-12 답습 정합) | C-N-1 + B-N | 영구 |
| N-13 | 본 cycle = 본 프로젝트 최초 egress 0 + Ollama 측정 cycle 자격 강함 | C-N-2 | NOTE |
| N-14 | sudo 6~8회 (h-O) sudo_count 7 답습 정합 (단 R-S5 권한 verify 추가 시 7~10회) | C-N-3 + R-S5 | NOTE |
| N-15 | (h-O) raw manifest_digest + model_blob_sha256 답습 (§3.3 Step 3 답습 정합) | C-N-4 | NOTE |
| N-16 | §4.3 prompt_eval_count 161 가설 (h-O 답습) 정합 | C-N-5 | NOTE |
| N-17 | 본 cycle 단일 측정 trial (R-17 답습) — Phase 1 N=3 carry-over ((h-O) C-S2 답습 영구) | C-N-6 | MEDIUM |
| N-18 | §9.2 S4 "(h-OM) ≈ (h)" 가능성 매우 낮음 framing 강화 자격 ((h-O) ratios decode 3.24×) | C-N-7 | LOW |

---

## 8. 기각 (5건)

### 기각-1 (자동 다음 단계 진입)
- chain 영구 종결 의무 답습 영구 + 사용자 명시 의무 답습 영구

### 기각-2 (Reviewer 권한 한계 (11) sub-boundary 신설)
- (g1-N-3-adr-008+sip+adr-012') 기각-2 답습 영구 + (10-k) "1회 한정, 영구 패턴화 0건" 답습 영구 위반 risk

### 기각-3 (chain 영구 종결 의무 약화 + (h-OM-X) prime 자동 진입 자격 신설)
- (g1-N-3-adr-008+sip+adr-012') (10.6-i) 답습 영구

### 기각-4 ((g)/(h)/(h-O) brief / 합의 본문 정정 자격)
- 본 (h-OM) cycle = 기존 cycle 와 *독립* 답습 영구. R-S1 발효가 기존 brief 본문 정정 trigger 자격 0

### 기각-5 (Reviewer 단독 BLOCKING R-S 추가 격상 자격)
- Reviewer 권한 한계 (1) 답습 영구. 본 합의 R-S1~R-S5 5건 발효 = Reviewer 단독 raw line-level direct cross-check + 외부 raw evidence 한정

---

## 9. Reviewer 권한 한계 답습 영구 (11 sub-boundary 답습)

(10-a)~(10-k) 11 sub-boundary 답습 영구. 본 합의 답습 적용:
- (10-a) ✓ 사용자 명시 (h-OM) + 4 명확화
- (10-b) ✓ 단계 (1)~(7)
- (10-c) ✓ Agent A/B/C 병렬 독립 + Reviewer 통합
- (10-d) ✓ 본 합의 1회 한정, 영구 패턴화 0건
- (10-e) ✓ R-S1 외부 raw evidence (Ollama issue #1450) = 추가 source 별도 자격 평가
- (10-f) ✓ §1.1/§9.3 framing *부분* 재구성 자격 한정 (R-S3 발효)
- (10-g) ✓ verbatim 유형 신설 0
- (10-h) ✓ 헌법·ADR 본문 정정 자격 0
- (10-i) ✓ 새 verbatim 인용 신설 0
- (10-j) ✓ (h-OM) 명명 = Phase 3.5-OM 답습
- (10-k) ✓ 본 합의 Reviewer 단독 sub-boundary 신설 0

§10.6 9 조건 답습 영구.

---

## 10. 본 합의 차단 조건 (§0 1:1 매핑 답습)

본 §0 10 항목 답습.

---

## 11. brief v1.1 보강 의무 (사용자 명시 후 별도 단계)

### 11.1 BLOCKING 15 verbatim 100% 흡수 의무 (R-21 답습 영구)

R-1 (R-S1) / R-2 (R-S3) / R-3 (R-S4) / R-4 (R-S2) / R-5 (R-S5) / R-6 ~ R-15 — 모두 §4·§5 답습 verbatim 100% 흡수 의무.

### 11.2 Reviewer 단독 격상 R-S1~R-S5 흡수 의무

- R-S1 ⭐⭐⭐ CRITICAL → 5 곳 (§1.1 + §0 #16 + §3.0.1 + §6 #7 + §5 B4)
- R-S2 ⭐⭐ HIGH → 6+ 곳 (모든 R-1 anchor 회차 표현)
- R-S3 ⭐⭐ HIGH → 3 곳 (§1.1 + §0 + §9.3)
- R-S4 ⭐ MEDIUM → 3 곳 (§6 #4 + §3.1 신규 step + §3.3 Step 3)
- R-S5 ⭐ MEDIUM → 4 곳 (§1.3 + §3.2 + §3.3 + §3.2 Step 2 후속)
- **총 21+ 곳 정정**

### 11.3 권고 16 흡수 (선택)

강한 권고 (R-rec-1·2·3·4·10·13·15) 우선 흡수.

### 11.4 NOTE 18 by-reference

§7 답습.

### 11.5 §11 v1 → v1.1 변경 일람 신규 작성 의무

### 11.6 brief v1.1 길이 예상

brief v1 469줄 → v1.1 ~570~620줄 예상.

---

## 12. 다음 단계 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 12.1 본 cycle 자체 단계

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `3d02edb`, 469줄 | 명시 완료 |
| **(2) 본 합의 commit (본 단계)** | 본 보고서 단일 commit | **본 단계** |
| (3) brief v1.1 보강 + commit | BLOCKING 15 verbatim 100% + R-S 5 흡수 21+곳 + 권고 16 + §11 신규 | **사용자 명시 의무** |
| (4) Modelfile 작성 + ollama create (~5분) | hard link + Modelfile + `ollama create` | 사용자 명시 직접 의무 |
| (5) verify + 측정 실행 (~30분) | §3.3 + §4 절차 (cold 측정 우선) | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (h-O) 패턴 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

### 12.2 본 cycle 외 carry-over (변경 0건 답습)

| 후보 cycle | 우선순위 | source |
|---|---|---|
| **MVP-1 합의 R4 framing 정정 evidence 별도 cycle** | HIGH | (g)/(h)/(h-O)/(h-OM) 4-way 종합 |
| **(g)+(h)+(h-O)+(h-OM) 4-way 통합 *분석* cycle** | HIGH ⭐⭐ | N-12 + C-N-1 + 사용자 비전 |
| **(h-OL) llama.cpp Ollama blob 직접 측정 cycle (R-15 발효 신규)** | MEDIUM | C-rec-7 (egress 0, 시간 ~30분, source 통제 역방향) |
| **Ollama prefill 처리 framework overhead 검증 cycle** | MEDIUM | (h-O) F-2 23.89× outlier |
| **Phase 1 N=3 repetitions Ollama 답습 cycle** | MEDIUM | C-S2 답습 |
| **Ollama embedded llama.cpp version verify cycle** | MEDIUM | R-S4 답습 |
| **Ollama Modelfile vs library internal pipeline cross-check cycle** | MEDIUM | §6 #18 답습 |
| **(j) advisory wall-clock 측정 cycle** | MEDIUM | 자비스 비전 |
| **`llama-bench` carry-over (R-rec-12 격상)** | MEDIUM | (h) F-8 + (h-O) F-7 답습 |
| **bartowski conversion lineage cross-check cycle** | MEDIUM | C-N-3 답습 |
| **Modelfile PARAMETER 변경 단독 cycle** | LOW | C-rec |
| **OM-direct-blob 신규 source 등록 방식 cycle** | LOW | R-rec-14 |
| **GGUF tokenizer.chat_template 직접 read cycle** | LOW | C-S3 답습 |
| **(k) M3·M4 결정 *고정*** | DEFER | 변수 분리 input 강화 후 |
| **(l) MVP-1 트랙 B 구현** | DEFER | (k) 통과 의무 답습 영구 |
| **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정 cycle** | DEFER | 기존 본문 변경 0건 |
| **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 |

---

## 13. 본 합의 자체 영구 권위

- 본 합의 = (h-OM) brief v1 (`3d02edb`) BLOCKING 15 + R-S 5 + 권고 16 + NOTE 18 + 기각 5 통합 단일 보고서
- ⭐⭐⭐ **R-S1 CRITICAL = hard link 가정 falsified** (Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy") = 3-way Consensus + 외부 raw evidence
- ⭐⭐ **R-S2 HIGH = R-1 anchor 산술 모순** (3 위치 self-inconsistency, 20·21·22·23 verbatim 정정)
- ⭐⭐ **R-S3 HIGH = "진짜 단독" framing R-4 위반 risk** (3-way Consensus)
- ⭐ **R-S4 MEDIUM = FROM 처리 모드 3종** + embedded version verify step 부재
- ⭐ **R-S5 MEDIUM = LICENSE / tag 자동 부여 / 권한 verify 부재**
- 본 합의 자체 머신 변경 0건
- 3 Agent 모두 APPROVE w/ COND 일치, 정면 충돌 0건
- chain 영구 종결 의무 답습 영구 = (h-OM-X) prime/super-prime 자동 진입 명백 부정

---

**본 합의 완료** (Phase 3.5-OM (h-OM) Ollama Modelfile bartowski 등록 cycle entry brief v1 풀 3+1 합의. APPROVE w/ COND 3-way 일치 + BLOCKING 15 + R-S 5 + 권고 16 + NOTE 18 + 기각 5. brief v1.1 보강 의무 = 사용자 명시 별도 단계. 본 합의 머신 변경 0건.)
