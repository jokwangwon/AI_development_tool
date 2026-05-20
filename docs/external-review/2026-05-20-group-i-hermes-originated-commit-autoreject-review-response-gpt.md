## Cross-vendor Blind 검토 응답 — Group I / Hermes-originated commit auto-reject

* **응답자 vendor**: OpenAI GPT-5.5 Thinking
* **응답 일자**: 2026-05-20
* **검토 기준**: 첨부된 Group I blind 검토 의뢰서(`2026-05-20-group-i-hermes-originated-commit-autoreject-review-request.md`)와, 보조 확인용 Git/GitHub 공식 문서. 본 의뢰는 Group I를 "Hermes-originated commit auto-reject"로 정의하고, T3 영역의 self-approval 차단을 위한 3-layer defense in depth를 검토 대상으로 제시하고 있습니다.
* **응답 권위 한계**: 본 응답 = 풀 3+1 합의 *입력 한정* (강제 채택 0건 — brief §7 + ADR-011 외부 LLM 입력 원칙 답습). framing 변경/채택은 풀 3+1 + 사용자 명시 결정 권한.

---

## 핵심 판정

**조건부로 풀 3+1 합의 진입 가능**합니다. 다만 현재 문구의 핵심 위험은 "Hermes-originated commit을 commit metadata로 식별해 차단한다"는 인상입니다. 이 방향은 약합니다.

더 안전한 설계 명제는 다음이어야 합니다.

> **Hermes commit을 사후 식별하는 것이 아니라, Hermes가 사람용 signing key·push credential·protected branch write path에 접근하지 못하게 만든다.**

즉 Group I의 중심은 **metadata 판별기**가 아니라 **credential boundary + external enforcement + audit**이어야 합니다.

---

## Q1. Hermes commit은 어떻게 식별해야 하는가?

**판정 / 권고:**
단일 신호로 식별하면 안 됩니다. **negative detection**보다는 **positive allow-list**가 적절합니다.

권고 신호 우선순위는 다음입니다.

1. **사람 전용 signing key로 서명된 commit만 protected T3 변경 허용**
2. **서버가 관측한 pusher / actor / token identity 확인**
3. **protected path 변경 시 CI provenance check 강제**
4. **Hermes 전용 bot identity / bot key / bot trailer는 audit 보조 신호로만 사용**
5. **author, committer, email, trailer는 신뢰 신호가 아니라 참고 신호**

근거:

* Git author/committer metadata는 환경변수나 config로 정해질 수 있고, Git 문서는 name 자체가 인증에 영향을 주지 않는다고 설명합니다. 따라서 author/committer는 Hermes 식별의 root signal이 될 수 없습니다.
* GitHub는 GPG, SSH, S/MIME commit signature를 검증할 수 있으므로, 서명은 metadata보다 강한 신호입니다. 하지만 이것도 "키를 가진 주체"를 증명할 뿐, "사람이 의식적으로 승인했다"는 사실까지 증명하지는 않습니다.

한계 / 가정:

* Hermes가 사람의 signing key, SSH agent, GitHub token, `gh` auth, browser session에 접근할 수 있다면 commit만 보고 사람/Hermes를 구분하는 것은 사실상 불가능합니다.

---

## Q2. author / committer / signature / metadata 중 무엇을 신뢰할 수 있는가?

**판정 / 권고:**
신뢰 등급을 명확히 분리해야 합니다.

| 신호                              |   신뢰도 | 판단                            |
| ------------------------------- | ----: | ----------------------------- |
| author name/email               |    낮음 | spoof 가능. 인증 신호 아님            |
| committer name/email            |    낮음 | spoof 가능. 인증 신호 아님            |
| commit trailer                  |    낮음 | convention일 뿐. Hermes가 작성 가능  |
| committer email domain          | 낮음~중간 | 계정 관리가 엄격할 때만 보조 신호           |
| verified signature              | 중간~높음 | 키 격리 시 강함. 키 공유 시 무력화         |
| server-observed pusher identity | 중간~높음 | token 격리 시 강함. token 공유 시 무력화 |
| human-only hardware-backed key  |    높음 | 1인 운영에서 가장 실용적인 강한 신호         |

자동 에이전트가 사람 identity를 사칭하는 경우는 **metadata 위조 사건**이 아니라 **credential boundary 실패 사건**으로 다뤄야 합니다. 이 경우 해당 commit만 reject할 것이 아니라 다음을 해야 합니다.

* 사람용 key/token 회수
* Hermes container/실행환경 credential 접근 차단
* audit alert
* protected branch ruleset 재검증
* 최근 T3 파일 변경 이력 재검토

---

## Q3. Hermes가 우회할 수 없는 외부 enforcement layer는 무엇인가?

**판정 / 권고:**
Hermes runtime 내부의 reject만으로는 부족합니다. Hermes가 끌 수 없는 enforcement는 **Hermes 밖**에 있어야 합니다.

권고 layer:

1. **GitHub ruleset / branch protection**

   * signed commit required
   * required status checks
   * force push 차단
   * bypass 권한 최소화

2. **CI provenance check**

   * protected files 변경 시 commit signature, pusher, changed path, PR label, manual approval marker를 검사
   * 실패 시 merge 불가

3. **컨테이너 / OS 권한 경계**

   * Hermes container에는 `.git` write 권한 없음
   * remote push credential 없음
   * SSH/GPG agent socket mount 금지
   * 사람의 `$HOME`, `~/.ssh`, `~/.gnupg`, GitHub CLI auth 접근 금지
   * Hermes는 patch/diff/artifact만 생성

4. **hardware-backed human signing**

   * FIDO2/YubiKey/SSH security key처럼 물리적 touch/PIN이 필요한 방식이 1인 개발자에게 실용적입니다.

한계:

* 같은 OS 사용자, 같은 홈 디렉터리, 같은 SSH agent, 같은 GitHub token을 공유하면 "우회 불가능"이라는 목표는 성립하지 않습니다.

---

## Q4. pre-commit / pre-push / server-side / GitHub ruleset 중 어느 계층이 적절한가?

**판정 / 권고:**
**다계층 Defense in depth가 필수**입니다. 단일 계층으로는 부적절합니다.

| 계층                                 | 장점                                            | 한계                                                                                                          |
| ---------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| pre-commit                         | 빠른 로컬 피드백                                     | `--no-verify`, hook 삭제, config 변경으로 우회 가능                                                                  |
| pre-push                           | push 직전 경고 가능                                 | 역시 client-side라 Hermes가 변경 가능                                                                              |
| server-side pre-receive            | 가장 강한 custom reject 가능                        | GitHub 공식 문서는 pre-receive hook을 GitHub Enterprise Server appliance에서 실행되는 정책 스크립트로 설명. 일반 GitHub.com 환경의 기본 수단으로 가정하면 안 됨 |
| GitHub ruleset / branch protection | GitHub.com에서 현실적으로 강한 server-side enforcement | custom provenance logic은 CI와 결합해야 함                                                                       |
| CI required check                  | 복잡한 정책 검사 가능                                  | CI workflow 자체 보호 필요                                                                                       |

권고 구성:

1. **Hermes container read-only / no credential**
2. **GitHub ruleset: signed commits + required checks + no force push**
3. **CI provenance verifier**
4. **local hooks는 UX 보조**
5. **GHES/self-hosted Git이면 pre-receive hook 추가**

---

## Q5. 1인 single-host 환경에서 false positive를 어떻게 통제할 것인가?

**판정 / 권고:**
false positive 통제는 "탐지 정확도 향상"보다 "보호 범위 축소 + 명시적 복구 절차"가 중요합니다.

권고:

* 모든 commit을 차단 대상으로 보지 말고, **T3 protected path**에 한정합니다.

  * Constitution
  * ADR
  * consensus reports
  * gate definitions
  * `.github/workflows`
  * Hermes runtime policy
  * security config
* 일반 코드/문서 변경은 audit-only 또는 warning으로 시작합니다.
* 초기 1~2주 또는 몇 cycle은 **observe mode**로 false positive/false negative를 측정합니다.
* reject 대신 **quarantine branch** 또는 **patch artifact 저장**을 제공해 작업 손실을 막습니다.
* 사람 commit 허용 기준은 "사람 서명 + 사람 token + protected ruleset 통과"로 둡니다.

한계:

* 사용자와 Hermes가 같은 host, 같은 계정, 같은 credential을 공유하면 false positive보다 더 큰 문제는 **false negative**, 즉 Hermes가 사람으로 보이는 commit을 만드는 것입니다.

---

## Q6. 사용자 직접 commit은 허용하고 Hermes commit만 차단하는 것이 가능한가?

**판정 / 권고:**
**가능하지만 조건부**입니다. 핵심 조건은 사람과 Hermes의 credential/process boundary가 실제로 분리되어야 한다는 점입니다.

가능한 설계:

```text
Hermes:
  - repo read 가능
  - working tree 일부 write 가능
  - .git write 불가
  - push credential 없음
  - signing key 없음
  - patch/artifact만 생성

User:
  - patch 검토
  - 직접 git add/commit
  - hardware-backed signing
  - protected branch PR/merge
```

또는:

```text
Hermes bot identity:
  - bot key로만 commit 가능
  - protected T3 path 변경은 bot key reject
  - bot commit은 자동 PR 생성까지만 허용
```

불가능한 경우:

* Hermes가 사용자의 SSH key, GPG key, SSH agent, GitHub token, `gh auth`, browser session을 사용할 수 있으면 기술적으로 구분 신뢰도가 낮습니다.

보완:

* 이 경우 "Hermes-originated commit만 자동 차단"이라는 표현을 낮추고, "T3 변경은 사용자 explicit approval 없이는 merge 불가"로 목표를 바꿔야 합니다.

---

## Q7. Hermes ≠ root of trust 원칙을 어떻게 보존할 것인가?

**판정 / 권고:**
차단 메커니즘 자체가 Hermes 내부에만 있으면 원칙이 무너집니다. root of trust는 다음 중 하나 이상에 있어야 합니다.

* GitHub ruleset / branch protection
* OS/container permission boundary
* hardware-backed human key
* 별도 사용자 관리 credential
* tamper-evident audit log

반드시 지켜야 할 조건:

* Hermes는 GitHub ruleset을 수정할 token을 가지면 안 됩니다.
* Hermes는 CI workflow를 단독으로 수정·merge할 수 없어야 합니다.
* Hermes는 signing key와 push credential을 가지면 안 됩니다.
* Hermes는 audit log를 삭제·수정할 수 없어야 합니다.
* Group I enforcement 설정 변경 자체는 T3로 분류해야 합니다.

현재 의뢰서의 "Hermes-originated commit reject(runtime)" 표현은 주의가 필요합니다. runtime이 스스로를 reject하는 구조라면 self-reference가 남습니다. runtime은 **provenance sensor / audit producer**일 수는 있지만, 최종 reject 권한은 Hermes 밖에 있어야 합니다.

---

## Q8. 3-layer 책무 분리는 적절한가?

**판정 / 권고:**
큰 방향은 적절합니다. 다만 현재 3-layer 설명에는 보강해야 할 공백이 있습니다.

의뢰서의 3-layer 구도는 branch protection, Hermes-originated commit reject, filesystem read-only ACL을 분리합니다. 이 분리는 self-reference와 단일 source-of-truth 문제를 다루려는 방향으로 타당합니다.

보강점:

1. **`.git/` 직접 변조는 commit으로 잡히지 않습니다.**
   `.git/config`, hooks, refs, index, credential helper 변경은 commit-based 검사로 탐지되지 않으므로 filesystem ACL layer에서 막아야 합니다.

진입 전 brief에는 다음 문장을 명시하는 것이 안전합니다.

> **Single-host에서 사람과 Hermes가 동일 credential을 공유하면 commit만으로 Hermes-originated 여부를 신뢰성 있게 판별할 수 없다. 따라서 Group I의 핵심은 commit metadata 판별이 아니라 credential isolation, protected branch enforcement, CI provenance check, filesystem ACL의 결합이다.**

### 본 의뢰 자료의 주요 결함 / 누락

* "Hermes-originated commit 식별"과 "T3 변경 승인 권한 통제"가 섞여 있습니다.
* runtime reject가 실제 enforcement인지, sensor인지 불명확합니다.
* `.git/` 직접 변조와 commit-based 검사의 차이가 충분히 분리되어 있지 않습니다.
* GitHub.com ruleset과 GHES pre-receive hook의 운영 차이가 명시되어 있지 않습니다.
* 사람용 signing key/token을 Hermes에서 어떻게 격리할지 구체안이 없습니다.
* false positive 복구 절차와 audit log tamper-resistance가 부족합니다.
* Group I가 PMO/Operational Readiness의 positive evidence로 오용되지 않도록 "negative control only" 조항을 추가해야 합니다.

### 최종 권고

**보강 후 풀 3+1 진입**을 권고합니다.
진입 자체를 막을 정도로 방향이 틀린 것은 아니지만, "metadata 기반 Hermes 식별"을 중심에 두면 구현 단계에서 잘못된 안전감을 만들 수 있습니다. Group I의 최종 설계명은 차라리 다음에 가까워야 합니다.

> **Hermes-originated commit auto-reject**
> → **Human-authorized T3 change enforcement with Hermes credential isolation**

---

## 참고 문서 (응답자 제시)

| # | 출처 |
|----|----|
| [1] | Git — git-commit Documentation (`git-scm.com/docs/git-commit`) — author/committer name은 인증 신호 아님 |
| [2] | GitHub Docs — About commit signature verification — GPG/SSH/S/MIME 서명 검증 |
| [3] | GitHub Docs — About rulesets — push/삭제/force push/signed commit 제어 |
| [4] | GitHub Docs (Enterprise Server 3.16) — About pre-receive hooks — GHES appliance 한정 정책 스크립트 |
