// Bütün sayfalarda ortak: mobil menü, sosyal medya bağlantıları, e-posta, yıl.
// Veriler veri/*.json dosyalarından gelir; dışarıdan hiçbir şey yüklenmez.

const $ = (s, k = document) => k.querySelector(s);
const $$ = (s, k = document) => [...k.querySelectorAll(s)];
const el = (etiket, ozellik = {}, ...cocuk) => {
  const e = document.createElement(etiket);
  for (const [a, d] of Object.entries(ozellik)) {
    if (d == null || d === false) continue;
    if (a === 'sinif') e.className = d;
    else if (a.startsWith('on')) e.addEventListener(a.slice(2), d);
    else e.setAttribute(a, d === true ? '' : d);
  }
  for (const c of cocuk.flat()) if (c != null && c !== false && c !== '') e.append(c);
  return e;
};
const simge = (ad, sinif) => {
  const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  if (sinif) s.setAttribute('class', sinif);
  s.setAttribute('aria-hidden', 'true');
  const u = document.createElementNS('http://www.w3.org/2000/svg', 'use');
  u.setAttribute('href', `#s-${ad}`);
  s.append(u);
  return s;
};
const tarihBicim = new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' });
const tercih = {
  al: (a) => { try { return localStorage.getItem(a) === '1'; } catch { return false; } },
  koy: (a) => { try { localStorage.setItem(a, '1'); } catch {} },
};
const kok = '/';   // veri dosyaları her zaman site kökünden (alt klasördeki sayfalar da, ör. /ozet/)

async function veri(ad) {
  try {
    const y = await fetch(`${kok}veri/${ad}`, { cache: 'no-cache' });
    return y.ok ? await y.json() : null;
  } catch { return null; }
}

const ortakVeri = Promise.all(['ayarlar.json', 'dersler.json', 'icerikler.json'].map(veri))
  .then(([ayar, dersler, icerik]) => ({ ayar: ayar || {}, dersler, icerikler: icerik?.icerikler || [] }));

// Mobil menü
const menuDugme = $('.menu-dugme');
if (menuDugme) {
  const kapat = () => { document.body.classList.remove('menu-acik'); menuDugme.setAttribute('aria-expanded', 'false'); menuDugme.setAttribute('aria-label', 'Menüyü aç'); };
  menuDugme.addEventListener('click', () => {
    const acik = document.body.classList.toggle('menu-acik');
    menuDugme.setAttribute('aria-expanded', String(acik));
    menuDugme.setAttribute('aria-label', acik ? 'Menüyü kapat' : 'Menüyü aç');
  });
  $$('#ana-menu a').forEach((a) => a.addEventListener('click', kapat));
  document.addEventListener('keydown', (o) => { if (o.key === 'Escape') kapat(); });
}

$$('[data-yil]').forEach((e) => { e.textContent = new Date().getFullYear(); });

// Toplam ziyaret (Cloudflare Web Analytics toplu verisinden günde bir kez üretilir: araclar/ziyaret_guncelle.py)
veri('ziyaret.json').then((z) => {
  const yer = $('#ziyaret');
  if (!yer || !z || !(z.toplam > 0)) return;
  yer.textContent = `Toplam ziyaret: ${z.toplam.toLocaleString('tr-TR')}`;
  yer.hidden = false;
});

ortakVeri.then(({ ayar }) => {
  for (const ag of ['youtube', 'instagram', 'facebook']) {
    const adres = ayar[ag]?.adres;
    $$(`[data-sosyal="${ag}"]`).forEach((a) => { if (adres) { a.href = adres; a.hidden = false; } });
    const kullanici = adres ? '@' + adres.replace(/\/+$/, '').split('/').pop().replace(/^@/, '') : '';
    $$(`[data-kullanici="${ag}"]`).forEach((e) => { e.textContent = kullanici; });
  }
  if (ayar.eposta) {
    $$('[data-eposta]').forEach((a) => {
      a.href = `mailto:${ayar.eposta}`;
      const yazi = a.querySelector('span') || a;
      yazi.textContent = ayar.eposta;
    });
  }
});
