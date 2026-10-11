// Bütün sayfalarda ortak: mobil menü, sosyal medya bağlantıları, e-posta, yıl.
// Veriler veri/*.json dosyalarından gelir; dışarıdan hiçbir şey yüklenmez.

const $ = (s, k = document) => k.querySelector(s);
const $$ = (s, k = document) => [...k.querySelectorAll(s)];
// Resmî veri alıntılarındaki düz kökleri de kapsamı belli, üst çizgili gösterime çevirir.
const kokParcalari = (metin) => {
  const s = String(metin), parcalar = []; let pos = 0;
  const re = /[√∛∜]/g; let m;
  while ((m = re.exec(s))) {
    const bas = m.index + 1; let son = bas, ic;
    if (s[bas] === '(') {
      let derinlik = 0;
      for (; son < s.length; son++) {
        if (s[son] === '(') derinlik++;
        if (s[son] === ')' && --derinlik === 0) break;
      }
      if (son === s.length) { re.lastIndex = bas; continue; } // kapanış yok (ör. arama kutusuna yazılan metin): işaret düz metin kalır
      ic = s.slice(bas + 1, son++);
    } else {
      const sayi = /^(?:\d+(?:[.,]\d+)?|[a-zA-Z])(?:[²³⁴⁵⁶⁷⁸⁹⁰¹]+)?/.exec(s.slice(bas));
      if (!sayi) { re.lastIndex = bas; continue; } // kapsam yok: işaret düz metin kalır
      ic = sayi[0]; son += ic.length;
    }
    parcalar.push({ metin: s.slice(pos, m.index) }, { kok: ic, derece: { '√': '', '∛': '3', '∜': '4' }[m[0]] });
    pos = son; re.lastIndex = son;
  }
  parcalar.push({ metin: s.slice(pos) }); return parcalar;
};
const kokDugumu = (metin) => {
  const sonuc = document.createDocumentFragment();
  for (const p of kokParcalari(metin)) {
    if (p.metin != null) { sonuc.append(p.metin); continue; }
    const kok = document.createElement('span'); kok.className = 's-kok'; kok.setAttribute('role', 'math');
    kok.setAttribute('aria-label', `${p.derece ? p.derece + '. dereceden kök' : 'karekök'}: ${p.kok}`);
    if (p.derece) { const d = document.createElement('span'); d.className = 's-kok-derece'; d.setAttribute('aria-hidden', 'true'); d.textContent = p.derece; kok.append(d); }
    const isaret = document.createElement('span'); isaret.className = 's-kok-isaret'; isaret.setAttribute('aria-hidden', 'true');
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); svg.setAttribute('viewBox', '0 0 16 24'); svg.setAttribute('preserveAspectRatio', 'none');
    const yol = document.createElementNS(svg.namespaceURI, 'path'); yol.setAttribute('d', 'M0 14 L4 12 L8 21 L14 0 H16 V1.5 H15 L8.5 24 L3.5 14 L1 15 Z'); yol.setAttribute('fill', 'currentColor'); svg.append(yol); isaret.append(svg);
    const ic = document.createElement('span'); ic.className = 's-kok-ic'; ic.setAttribute('aria-hidden', 'true'); ic.append(kokDugumu(p.kok));
    kok.append(isaret, ic); sonuc.append(kok);
  }
  return sonuc;
};
const el = (etiket, ozellik = {}, ...cocuk) => {
  const e = document.createElement(etiket);
  for (const [a, d] of Object.entries(ozellik)) {
    if (d == null || d === false) continue;
    if (a === 'sinif') e.className = d;
    else if (a.startsWith('on')) e.addEventListener(a.slice(2), d);
    else e.setAttribute(a, d === true ? '' : d);
  }
  for (const c of cocuk.flat()) if (c != null && c !== false && c !== '') e.append(typeof c === 'string' && /[√∛∜]/.test(c) ? kokDugumu(c) : c);
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
  .then(([ayar, dersler, icerik]) => ({
    ayar: ayar || {}, dersler,
    // Yükleme hatası ile geçerli, boş bir içerik listesini ayır.
    iceriklerYuklendi: Array.isArray(icerik?.icerikler),
    icerikler: Array.isArray(icerik?.icerikler) ? icerik.icerikler : []
  }));

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

// Konu özeti: sağda "Bu sayfada" paneli (geniş ekranda). Başlıklar sayfadaki h2'lerden kurulur.
(() => {
  const ic = $('.ozet-ic');
  if (!ic) return;
  const basliklar = $$('h2', ic).filter((h) => h.textContent.trim() && !h.closest('.ozet-yan'));
  if (basliklar.length < 2) return;
  const kisa = (t) => t.toLocaleLowerCase('tr').replace(/[^a-z0-9çğıöşü]+/g, '-').replace(/^-|-$/g, '');
  const baglar = basliklar.map((h, i) => {
    if (!h.id) {
      const kokId = kisa(h.textContent) || `bolum-${i + 1}`;
      let id = kokId, sira = 2;
      while (document.getElementById(id)) id = `${kokId}-${sira++}`;
      h.id = id;
    }
    return el('li', {}, el('a', { href: `#${h.id}` }, h.textContent.trim()));
  });
  const yan = el('aside', { sinif: 'ozet-yan', 'aria-label': 'Bu sayfada' },
    el('nav', {}, el('h2', {}, 'Bu sayfada'), el('ol', {}, baglar),
      $('.etk') ? el('a', { sinif: 'dugme ana yan-dugme', href: `#${($('.etk').closest('section') || $('.etk')).id || basliklar[basliklar.length - 1].id}` }, 'Etkinliklere geç') : null));
  ic.classList.add('yanli');
  ic.prepend(yan);
  if ('IntersectionObserver' in window) {
    const gozcu = new IntersectionObserver((kayit) => {
      const gorunen = kayit.find((k) => k.isIntersecting);
      if (!gorunen) return;
      $$('.ozet-yan a.etkin').forEach((a) => a.classList.remove('etkin'));
      $(`.ozet-yan a[href="#${CSS.escape(gorunen.target.id)}"]`)?.classList.add('etkin');
    }, { rootMargin: '-90px 0px -65% 0px' });
    basliklar.forEach((h) => gozcu.observe(h));
  }
})();

// Özet görselleri: SVG içindeki yazı viewBox dışına taşıyorsa viewBox yazıyı kapsayacak kadar genişletilir
// (görsel dar yan sütunda da kesilmeden ve kutudan taşmadan görünür).
(() => {
  const svgler = $$('.ozet-gorsel svg[viewBox]');
  if (!svgler.length) return;
  const sigdir = () => svgler.forEach((s) => {
    try {
      const b = s.getBBox(), v = s.viewBox.baseVal, p = 4;
      if (!b.width) return;
      const x0 = Math.min(v.x, b.x - p), y0 = Math.min(v.y, b.y - p);
      const x1 = Math.max(v.x + v.width, b.x + b.width + p), y1 = Math.max(v.y + v.height, b.y + b.height + p);
      if (x0 < v.x || y0 < v.y || x1 > v.x + v.width || y1 > v.y + v.height) s.setAttribute('viewBox', `${x0} ${y0} ${x1 - x0} ${y1 - y0}`);
    } catch { /* görünmeyen SVG */ }
  });
  (document.fonts?.ready || Promise.resolve()).then(sigdir);
})();

// "Yeni eklenenler" kayan şeridi (kullanıcı 11.10.2026): sitenin kendi içeriğinden en yeni kayıtlar, reklam değildir.
// Geniş ekranda sağ kenarda dikey sütun, dar ekranda üst bilginin altında yatay şerit (serit.css). Fare üstündeyken
// ya da odaktayken durur, durdur düğmesi vardır; hareket azaltma tercihinde kaymaz. Veri: icerikler.json + yazili-kagitlari.json.
(() => {
  const ust = $('header.ust');
  if (!ust || /^\/(tahta|goruntule)\.html$/.test(location.pathname)) return;   // tam ekran araç sayfaları
  const SERIT_SURUM = '20261011-1', EN_COK = 18;
  const kisaTarih = new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'short' });
  const yol = (a) => (/^(https?:)?\//.test(a) ? a : `/${a}`);
  const stil = el('link', { rel: 'stylesheet', href: `${kok}serit.css?v=${SERIT_SURUM}` });
  const stilHazir = new Promise((tamam) => { stil.onload = () => tamam(true); stil.onerror = () => tamam(false); });
  document.head.append(stil);

  Promise.all([ortakVeri, veri('yazili-kagitlari.json'), stilHazir]).then(([{ dersler, icerikler }, kagit, stilVar]) => {
    if (!stilVar) return;
    const dersAd = (d) => dersler?.dersler?.[d] || d || '';
    const kayitlar = icerikler.filter((i) => i.tarih && (i.hazirla || i.goruntule || i.dosya || i.baglanti)).map((i) => {
      const ad = dersAd(i.ders);
      let baslik = String(i.baslik || '').replace(/^\d+\.\s*Sınıf\s+/, '');
      if (ad && baslik.startsWith(`${ad} `)) baslik = baslik.slice(ad.length + 1);   // sınıf ve ders alt satırda
      return { tarih: i.tarih, tur: i.tur, baslik, ders: i.ders, alt: [i.sinif && `${i.sinif}. sınıf`, ad].filter(Boolean).join(' · '),
        adres: yol(i.hazirla || i.goruntule || i.dosya || i.baglanti) };
    });
    // Yazılı sınav kâğıtları sınıf başına tek kart (her ders ayrı kart olursa şeridi kaplar)
    const gruplar = new Map();
    for (const [anahtar, yazililar] of Object.entries(kagit?.tablolar || {})) {
      const [, sinif, ders] = /^(\d+)-(.+)$/.exec(anahtar) || [];
      if (!sinif) continue;
      const g = gruplar.get(sinif) || { dersler: [], sayi: 0 };
      g.dersler.push(ders);
      g.sayi += Object.values(yazililar).reduce((t, s) => t + (Array.isArray(s) ? s.length : 0), 0);
      gruplar.set(sinif, g);
    }
    if (kagit?.guncelleme) for (const [sinif, g] of gruplar) kayitlar.push({ tarih: kagit.guncelleme, tur: 'Yazılı kâğıdı', yazili: true,
      baslik: `Ortak yazılı sınav kâğıtları: ${g.sayi} kâğıt, cevaplı`, alt: `${sinif}. sınıf · ${g.dersler.map(dersAd).join(', ')}`,
      adres: `/yazili.html?sinif=${sinif}&ders=${encodeURIComponent(g.dersler[0])}` });
    const secilen = kayitlar.sort((a, b) => String(b.tarih).localeCompare(String(a.tarih))).slice(0, EN_COK);
    if (secilen.length < 4) return;

    const kart = (k) => {
      const dis = /^https?:/.test(k.adres);
      const gun = new Date(/^\d{4}-\d\d-\d\d$/.test(k.tarih) ? `${k.tarih}T12:00:00` : k.tarih);
      return el('li', { sinif: 'serit-oge' },
        el('a', { sinif: ['serit-kart', k.ders && `ders-${k.ders}`, k.yazili && 'serit-yazili'].filter(Boolean).join(' '), href: k.adres,
          target: dis ? '_blank' : null, rel: dis ? 'noopener' : null },
          el('span', { sinif: 'serit-ust' }, el('span', { sinif: 'serit-tur' }, k.tur || 'İçerik'),
            isNaN(gun) ? null : el('time', { datetime: k.tarih }, kisaTarih.format(gun))),
          el('span', { sinif: 'serit-ad' }, k.baslik),
          k.alt && el('span', { sinif: 'serit-alt' }, k.alt)));
    };
    const liste = () => el('ul', { sinif: 'serit-liste' }, secilen.map(kart));
    const kopya = liste();   // kesintisiz döngü için ikinci kopya; ekran okuyucu ve klavye için yok sayılır
    kopya.classList.add('serit-kopya'); kopya.setAttribute('aria-hidden', 'true'); kopya.inert = true;

    let durdu = false;
    try { durdu = localStorage.getItem('serit-durdu') === '1'; } catch {}
    const isaret = el('span', { 'aria-hidden': 'true' });
    const dugme = el('button', { sinif: 'serit-dur', type: 'button' }, isaret);
    const serit = el('aside', { sinif: 'serit', 'aria-label': 'Yeni eklenenler', style: `--serit-sure: ${secilen.length * 5}s` },
      el('div', { sinif: 'serit-bas' },
        el('span', { sinif: 'serit-baslik' }, el('span', {}, 'Yeni', el('span', { sinif: 'serit-uzun' }, ' eklenenler'))),
        el('a', { sinif: 'serit-tumu', href: '/icerikler.html' }, 'Tümü'), dugme),
      el('div', { sinif: 'serit-pencere' }, el('div', { sinif: 'serit-iz' }, liste(), kopya)));
    const ayarla = () => {
      serit.classList.toggle('durdu', durdu);
      const yazi = durdu ? 'Kaymayı başlat' : 'Kaymayı durdur';
      dugme.setAttribute('aria-label', yazi); dugme.title = yazi;
      isaret.textContent = durdu ? '▶' : '❚❚';
    };
    dugme.addEventListener('click', () => {
      durdu = !durdu; ayarla();
      try { localStorage.setItem('serit-durdu', durdu ? '1' : '0'); } catch {}
    });
    ayarla();
    ust.after(serit);
    document.body.classList.add('serit-var');
  });
})();
