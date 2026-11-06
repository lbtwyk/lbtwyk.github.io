(() => {
  const valid = value => ['zh', 'en'].includes(value);
  let saved; try { saved = localStorage.getItem('portfolio-explore-lang'); } catch {}
  const query = new URLSearchParams(location.search).get('lang');
  function setLanguage(lang) {
    document.documentElement.dataset.lang = lang;
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('button[data-lang]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === lang)));
    document.querySelector('[data-original]').href = `../?lang=${lang}`;
    document.querySelector('[data-compare]').href = `../compare/?lang=${lang}`;
    try { localStorage.setItem('portfolio-explore-lang', lang); } catch {}
  }
  setLanguage(valid(query) ? query : valid(saved) ? saved : 'zh');
  document.querySelectorAll('button[data-lang]').forEach(b => b.addEventListener('click', () => setLanguage(b.dataset.lang)));
  const videos = [...document.querySelectorAll('video')];
  videos.forEach(video => video.addEventListener('play', () => videos.forEach(other => { if (other !== video) other.pause(); })));
  document.addEventListener('visibilitychange', () => { if (document.hidden) videos.forEach(v => v.pause()); });
})();
