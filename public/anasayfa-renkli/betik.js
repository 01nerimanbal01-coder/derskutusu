/* Ders Kutusu · renkli ana sayfanın menüsü ve slaytları */
(function () {
  'use strict';

  var azalt = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ---------- Menü ---------- */
  var menu = document.getElementById('menu');
  var menuAc = menu && menu.querySelector('.menu-ac');
  if (menuAc) {
    document.documentElement.classList.add('js');
    menuAc.addEventListener('click', function () {
      var acik = menu.classList.toggle('acik');
      menuAc.setAttribute('aria-expanded', acik ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('acik')) {
        menu.classList.remove('acik');
        menuAc.setAttribute('aria-expanded', 'false');
        menuAc.focus();
      }
    });
  }

  /* Arama simgesi: Hızlı bul alanına git ve konu kutusuna odaklan */
  var araDugme = document.querySelector('.ara-dugme');
  var konu = document.getElementById('hb-konu');
  if (araDugme && konu) {
    araDugme.addEventListener('click', function (e) {
      e.preventDefault();
      var hedef = document.getElementById('hizli-bul');
      hedef.scrollIntoView({ behavior: azalt && azalt.matches ? 'auto' : 'smooth', block: 'center' });
      setTimeout(function () { konu.focus({ preventScroll: true }); }, azalt && azalt.matches ? 0 : 450);
    });
  }

  /* ---------- Slayt ---------- */
  var slayt = document.getElementById('slayt');
  if (slayt) {
    var ogeler = Array.prototype.slice.call(slayt.querySelectorAll('.slayt-oge'));
    var noktalar = Array.prototype.slice.call(slayt.querySelectorAll('.nokta'));
    var izler = document.getElementById('slayt-izler');
    var durDugme = document.getElementById('slayt-dur');
    var sira = 0, zamanlayici = null, kullaniciDurdurdu = false, ustunde = false, odakta = false;
    var SURE = 6500;

    var goster = function (i, elle) {
      sira = (i + ogeler.length) % ogeler.length;
      ogeler.forEach(function (o, k) {
        var aktif = k === sira;
        o.classList.toggle('aktif', aktif);
        o.setAttribute('aria-hidden', aktif ? 'false' : 'true');
        if ('inert' in o) o.inert = !aktif;
      });
      noktalar.forEach(function (n, k) { n.setAttribute('aria-current', k === sira ? 'true' : 'false'); });
      izler.setAttribute('aria-live', elle ? 'polite' : 'off');
    };
    var durdur = function () { if (zamanlayici) { clearInterval(zamanlayici); zamanlayici = null; } };
    var baslat = function () {
      durdur();
      if (kullaniciDurdurdu || ustunde || odakta || (azalt && azalt.matches) || document.hidden) return;
      zamanlayici = setInterval(function () { goster(sira + 1, false); }, SURE);
    };
    var durumYaz = function () {
      var duruk = kullaniciDurdurdu;
      durDugme.hidden = Boolean(azalt && azalt.matches);
      durDugme.setAttribute('aria-pressed', duruk ? 'true' : 'false');
      durDugme.setAttribute('aria-label', duruk ? 'Slaytları kendiliğinden oynat' : 'Slaytların kendiliğinden geçmesini durdur');
    };

    slayt.querySelectorAll('.ok').forEach(function (b) {
      b.addEventListener('click', function () { goster(sira + Number(b.dataset.yon), true); baslat(); });
    });
    noktalar.forEach(function (n) {
      n.addEventListener('click', function () { goster(Number(n.dataset.git), true); baslat(); });
    });
    durDugme.addEventListener('click', function () {
      kullaniciDurdurdu = durDugme.getAttribute('aria-pressed') !== 'true';
      durumYaz(); baslat();
    });
    slayt.addEventListener('keydown', function (e) {
      if (e.target.closest && e.target.closest('input, select, textarea')) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); goster(sira + 1, true); baslat(); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); goster(sira - 1, true); baslat(); }
    });
    slayt.addEventListener('mouseenter', function () { ustunde = true; durdur(); });
    slayt.addEventListener('mouseleave', function () { ustunde = false; baslat(); });
    slayt.addEventListener('focusin', function () { odakta = true; durdur(); });
    slayt.addEventListener('focusout', function (e) { if (!slayt.contains(e.relatedTarget)) { odakta = false; baslat(); } });
    document.addEventListener('visibilitychange', baslat);
    if (azalt && azalt.addEventListener) azalt.addEventListener('change', function () { durumYaz(); baslat(); });

    /* Dokunmatik kaydırma */
    var x0 = null;
    izler.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    izler.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) { goster(sira + (dx < 0 ? 1 : -1), true); baslat(); }
    });

    goster(0, false); durumYaz(); baslat();
  }
})();
