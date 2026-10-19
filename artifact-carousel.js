(() => {
  'use strict';
  const carousel = document.querySelector('#web-deliverables-sample .artifact-carousel');
  if (!carousel) return;
  const track = carousel.querySelector('.artifact-track');
  const slides = Array.from(track.querySelectorAll('.artifact-slide'));
  const controls = carousel.querySelector('.artifact-controls');
  const previous = controls.querySelector('[data-previous]');
  const next = controls.querySelector('[data-next]');
  const status = controls.querySelector('[role="status"]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let selected = 0;
  let requested = 0;
  let scrollTimer;

  function update(index) {
    selected = index;
    requested = index;
    previous.disabled = index === 0;
    next.disabled = index === slides.length - 1;
    status.textContent = `${index + 1} of ${slides.length} — ${slides[index].querySelector('h5').textContent}`;
    slides.forEach((slide, position) => {
      // Offscreen links must not steal keyboard focus or move the scroller.
      slide.inert = position !== index;
      slide.setAttribute('aria-current', position === index ? 'true' : 'false');
    });
  }

  function goTo(index, instant = false) {
    requested = Math.max(0, Math.min(slides.length - 1, index));
    track.scrollTo({
      left: requested * track.clientWidth,
      behavior: instant || reducedMotion.matches ? 'instant' : 'smooth'
    });
  }

  function settle() {
    const index = Math.max(0, Math.min(slides.length - 1, Math.round(track.scrollLeft / track.clientWidth)));
    if (index !== selected) update(index);
    else requested = index;
  }

  previous.addEventListener('click', () => goTo(requested - 1));
  next.addEventListener('click', () => goTo(requested + 1));
  track.addEventListener('keydown', (event) => {
    // Do not intercept keys inside links or embedded documents.
    if (event.target !== track) return;
    const destinations = { ArrowLeft: requested - 1, ArrowRight: requested + 1, Home: 0, End: slides.length - 1 };
    if (!(event.key in destinations)) return;
    event.preventDefault();
    goTo(destinations[event.key]);
  });
  track.addEventListener('scroll', () => {
    window.clearTimeout(scrollTimer);
    scrollTimer = window.setTimeout(settle, 100);
  }, { passive: true });
  track.addEventListener('scrollend', settle);
  const resizeObserver = new ResizeObserver(() => goTo(selected, true));
  resizeObserver.observe(track);
  update(0);
  controls.hidden = false;
})();
