/* TTS 음성 비교 플러그인 — 프론트 패널 (음성 카드 그리드, UX 컨펌).
 *
 * 답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §6)
 * C-2 분리 JS: StaticFiles(/plugins/tts_compare/panel.js)로 동적 로드 → index.html
 * 의 window.registerJarvisPlugin(name, {mount}) 로 자신을 등록(첫 분리 패널 사례).
 *
 * 레이아웃: 상단 입력 + 음성 다중선택 → [생성] → 음성별 결과 카드(재생/길이/메모).
 */
(function () {
  const BASE = '/api/plugins/tts_compare';

  function el(tag, attrs, children) {
    const e = document.createElement(tag);
    if (attrs) for (const k in attrs) {
      if (k === 'style') e.style.cssText = attrs[k];
      else if (k === 'text') e.textContent = attrs[k];
      else e.setAttribute(k, attrs[k]);
    }
    (children || []).forEach((c) => e.appendChild(c));
    return e;
  }

  async function mount(root) {
    root.innerHTML = '';
    root.appendChild(el('div', { text: 'TTS 음성 비교', style: 'font-size:13px; opacity:0.7; margin:4px 0 10px;' }));

    const textInput = el('input', {
      type: 'text', placeholder: '비교할 문장 입력...',
      style: 'width:100%; padding:7px 10px; background:var(--surface,#1a1a1a); border:1px solid var(--border,#333); border-radius:8px; color:var(--text,#eee); font-family:inherit; font-size:13px; outline:none; box-sizing:border-box;',
    });
    root.appendChild(textInput);

    const voiceBar = el('div', { style: 'display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin:10px 0;' });
    root.appendChild(voiceBar);

    const genBtn = el('button', {
      text: '생성', style: 'padding:6px 16px; background:var(--accent,#4a9); border:none; border-radius:8px; color:#fff; cursor:pointer; font-family:inherit; font-size:13px;',
    });
    voiceBar.appendChild(genBtn);

    const grid = el('div', { style: 'display:grid; grid-template-columns:repeat(auto-fill, minmax(180px,1fr)); gap:10px; margin-top:12px;' });
    root.appendChild(grid);

    const status = el('div', { style: 'font-size:12px; opacity:0.6; margin-top:6px;' });
    root.appendChild(status);

    // 음성 목록 로드 → 체크박스
    const checks = {};
    try {
      const r = await fetch(BASE + '/voices');
      const voices = (await r.json()).voices || [];
      voices.forEach((v, i) => {
        const cb = el('input', { type: 'checkbox' });
        if (i < 2) cb.checked = true;  // 기본 2개 선택
        checks[v.key] = cb;
        const lbl = el('label', { style: 'display:inline-flex; align-items:center; gap:4px; font-size:12px; cursor:pointer;' }, [cb, el('span', { text: v.label })]);
        voiceBar.insertBefore(lbl, genBtn);
      });
      if (!voices.length) status.textContent = '사용 가능한 음성이 없습니다 (ref voice 미설치).';
    } catch (e) {
      status.textContent = '음성 목록 로드 실패.';
    }

    function card(res) {
      const audioSrc = 'data:audio/wav;base64,' + res.audio_b64;
      const player = el('audio', { controls: '', src: audioSrc, style: 'width:100%; margin:6px 0;' });
      const meta = el('div', { text: `${(res.ms / 1000).toFixed(1)}s · rms ${res.rms.toFixed(3)}`, style: 'font-size:11px; opacity:0.55;' });
      const memo = el('textarea', { placeholder: '메모...', rows: '2', style: 'width:100%; margin-top:6px; background:var(--surface,#1a1a1a); border:1px solid var(--border,#333); border-radius:6px; color:var(--text,#eee); font-family:inherit; font-size:11px; resize:vertical; box-sizing:border-box;' });
      return el('div', { style: 'border:1px solid var(--border,#333); border-radius:10px; padding:10px; background:var(--surface,#161616);' },
        [el('div', { text: res.label || res.voice, style: 'font-size:12px; font-weight:600; margin-bottom:2px;' }), player, meta, memo]);
    }

    async function generate() {
      const text = textInput.value.trim();
      const sel = Object.keys(checks).filter((k) => checks[k].checked);
      if (!text) { status.textContent = '문장을 입력하세요.'; return; }
      if (!sel.length) { status.textContent = '음성을 1개 이상 선택하세요.'; return; }
      genBtn.disabled = true; status.textContent = '생성 중...';
      try {
        const r = await fetch(BASE + '/synthesize', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text, voices: sel }),
        });
        if (!r.ok) { status.textContent = '생성 실패: ' + r.status; return; }
        const results = (await r.json()).results || [];
        grid.innerHTML = '';
        results.forEach((res) => grid.appendChild(card(res)));
        status.textContent = `${results.length}개 음성 생성 완료.`;
      } catch (e) {
        status.textContent = '생성 오류.';
      } finally {
        genBtn.disabled = false;
      }
    }

    genBtn.addEventListener('click', generate);
    textInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') generate(); });
  }

  if (window.registerJarvisPlugin) window.registerJarvisPlugin('tts_compare', { mount });
})();
