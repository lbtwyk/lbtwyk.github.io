(() => {
  const storageKey = 'lbtwyk-lang';
  let saved;
  try { saved = localStorage.getItem(storageKey); } catch (_) {}
  const query = new URLSearchParams(location.search).get('lang');
  const initial = ['en', 'zh'].includes(query) ? query : saved === 'zh' ? 'zh' : 'en';
  function setLanguage(lang) {
    document.documentElement.dataset.lang = lang;
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-set-lang]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.setLang === lang));
    });
    try { localStorage.setItem(storageKey, lang); } catch (_) {}
  }
  setLanguage(initial);
  document.querySelectorAll('[data-set-lang]').forEach(button => {
    button.addEventListener('click', () => setLanguage(button.dataset.setLang));
  });

  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const videos = [...document.querySelectorAll('video')];
  const states = new Map(videos.map(video => [video, { visible: false, manuallyPaused: false, programmaticPause: false }]));
  function pause(video) {
    if (!video.paused) {
      states.get(video).programmaticPause = true;
      video.pause();
    }
  }
  function sync(video) {
    const state = states.get(video);
    if (state.visible && !document.hidden && !motion.matches && !state.manuallyPaused) {
      video.play().catch(() => {});
    } else if (!state.visible || document.hidden || motion.matches) {
      pause(video);
    }
  }
  videos.forEach(video => {
    video.addEventListener('pause', () => {
      const state = states.get(video);
      if (state.programmaticPause) state.programmaticPause = false;
      else state.manuallyPaused = true;
    });
    video.addEventListener('play', () => { states.get(video).manuallyPaused = false; });
  });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        states.get(entry.target).visible = entry.isIntersecting && entry.intersectionRatio >= .3;
        sync(entry.target);
      });
    }, { threshold: [0, .3] });
    videos.forEach(video => observer.observe(video));
  }
  document.addEventListener('visibilitychange', () => videos.forEach(sync));
  motion.addEventListener('change', () => videos.forEach(sync));
})();
