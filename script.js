// portfolio-site interactions: reveal on scroll, close mobile menu on nav
(function(){
  var links = document.querySelector('.nav-links');
  if(links){
    links.addEventListener('click', function(e){
      if(e.target.tagName === 'A') links.classList.remove('open');
    });
  }
  var els = document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){
    els.forEach(function(el){ el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, {threshold: 0.08});
  els.forEach(function(el){ io.observe(el); });
})();
