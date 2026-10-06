// 슬라이드 넘김: 방향키, 스페이스, PageUp/Down, Home/End, 클릭, 스와이프, #번호, F 전체 화면
(() => {
  const slides = [...document.querySelectorAll('.slide')];
  const bar = document.querySelector('.progress');
  let i = 0;

  const fit = () => {
    const s = Math.min(innerWidth / 1920, innerHeight / 1080);
    document.documentElement.style.setProperty('--s', s);
  };

  const show = (n) => {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((el, k) => el.classList.toggle('active', k === i));
    if (bar) bar.style.width = ((i + 1) / slides.length) * 100 + '%';
    if (location.hash !== '#' + (i + 1)) history.replaceState(null, '', '#' + (i + 1));
  };

  const fromHash = () => {
    const n = parseInt(location.hash.slice(1), 10);
    show(Number.isFinite(n) ? n - 1 : 0);
  };

  addEventListener('resize', fit);
  addEventListener('hashchange', fromHash);
  addEventListener('keydown', (e) => {
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].includes(e.key)) { e.preventDefault(); show(i + 1); }
    else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(e.key)) { e.preventDefault(); show(i - 1); }
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(slides.length - 1);
    else if (e.key.toLowerCase() === 'f') {
      if (document.fullscreenElement) document.exitFullscreen?.();
      else document.documentElement.requestFullscreen?.().catch(() => {});
    }
  });
  addEventListener('click', (e) => {
    if (e.target.closest('a')) return;
    show(e.clientX > innerWidth / 3 ? i + 1 : i - 1);
  });
  let x0 = null;
  addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 60) show(i + (dx < 0 ? 1 : -1));
    x0 = null;
  }, { passive: true });

  fit();
  fromHash();
})();
