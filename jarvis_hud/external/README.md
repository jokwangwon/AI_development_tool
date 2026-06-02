# 외부 관제형 읽기측 레지스트리 (패턴1 링크 허브 MVP)

> 답습: `docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md` v2.1 §4 패턴1 ·
> `docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md` (REVISE 읽기측)

자비스가 (워커로) 구축을 도운 **외부 프로젝트**를 HUD 에 **링크 카드**로 모은다.
자비스는 "입구"만 제공하고 결과는 외부에서 본다 — **읽기 전용**(제어·자격증명·게이트 0,
제어측 §3.5 는 별도 풀3+1 + DEFER).

## `registry.json` 형식

```json
{
  "entries": [
    {
      "name": "tts_lab",
      "title": "TTS 모델 테스트",
      "url": "https://tts.example.com/dashboard",
      "icon": "🔊",
      "origin": "jarvis"
    }
  ]
}
```

| 필드 | 필수 | 설명 |
|------|------|------|
| `name` | ✅ | 소문자 영숫자 + `_` `-` (path traversal 차단) |
| `title` | ✅ | 카드에 표시될 이름 |
| `url` | ✅ | **http(s) 만** — `javascript:`/`data:`/`file:` 등은 거부(XSS 차단) |
| `icon` | ❌ | 이모지/문자 (기본 빈 문자열) |
| `origin` | ✅ | ⭐ **반드시 `"jarvis"`** — provenance fail-closed (§1.5 G7) |

## ⭐ provenance fail-closed (§1.5, 비협상)

관제 대상은 **자비스가 도와 만든 프로젝트에 한정**한다. `origin != "jarvis"` 이거나
누락된 엔트리는 **거부(skip)** — origin 불명 = 관제 대상 아님. 임의 제3자 외부
시스템은 받지 않는다. **좁힘 ≠ 신뢰** — 이는 표면 완화일 뿐, 제어측 게이트는 유지된다.

불량 엔트리(provenance·url·name 위반)·깨진 JSON 은 **fail-soft** 로 조용히 skip 되며
나머지 정상 엔트리는 정상 노출된다(1개 불량이 전체를 막지 않음).
