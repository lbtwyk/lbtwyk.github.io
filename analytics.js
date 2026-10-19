// Production-only analytics. Video events count one playback start per page visit,
// including the site's existing in-view autoplay; they are not manual clicks.
(() => {
  if (location.hostname !== 'lbtwyk.github.io') return;
  const pending = [];
  const send = event => {
    if (typeof window.goatcounter?.count === 'function') window.goatcounter.count(event);
    else pending.push(event);
  };
  document.querySelectorAll('video').forEach(video => {
    video.addEventListener('playing', () => {
      const source = video.querySelector('source')?.src || video.currentSrc;
      const name = new URL(source, location.href).pathname.split('/').pop().replace(/\.mp4$/, '');
      send({ path: `video-start-${name}`, title: `Video playback: ${name}`, event: true });
    }, { once: true });
  });
  const script = document.createElement('script');
  script.src = 'https://gc.zgo.at/count.js';
  script.async = true;
  script.dataset.goatcounter = 'https://lbtwyk.goatcounter.com/count';
  script.addEventListener('load', () => {
    if (typeof window.goatcounter?.count === 'function') pending.splice(0).forEach(send);
  });
  document.head.appendChild(script);
})();
