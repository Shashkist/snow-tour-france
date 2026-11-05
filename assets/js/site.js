// Shared behaviour for every tour page.
(function () {
  // Lightbox: any <img data-g> opens full-screen on tap.
  var lb = document.getElementById('lb');
  if (lb) {
    var im = lb.querySelector('img');
    document.addEventListener('click', function (e) {
      var t = e.target;
      if (t.hasAttribute && t.hasAttribute('data-g')) { im.src = t.src; lb.classList.add('on'); }
      else if (lb.classList.contains('on')) { lb.classList.remove('on'); }
    });
  }
  // Countdown: <p class="cd" data-deadline="YYYY-MM-DDTHH:MM" data-text="... {d} ...">
  // The text disappears automatically once the deadline has passed.
  document.querySelectorAll('[data-deadline]').forEach(function (el) {
    try {
      var d = Math.ceil((new Date(el.getAttribute('data-deadline')) - new Date()) / 864e5);
      if (d > 0) el.textContent = el.getAttribute('data-text').replace('{d}', d);
    } catch (e) {}
  });
})();
