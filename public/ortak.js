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

// Site ağacı (kullanıcı 11.10.2026): öğrenci / öğretmen dalı. Sayfanın kitlesi body[data-kitle]'dadır.
(() => {
  const kitle = document.body.dataset.kitle;
  try { if (kitle) localStorage.setItem('dk-rol', kitle); } catch {}
  if (kitle) $$('#ana-menu a').forEach((a) => { if (a.getAttribute('href') === `/${kitle}.html`) a.setAttribute('aria-current', 'page'); });
  if (!/^\/(index\.html)?$/.test(location.pathname)) return;
  const eski = { '#siniflar': '/ogrenci.html', '#dersler': '/ogrenci.html', '#ogretmen': '/ogretmen.html', '#kategoriler': '/icerikler.html', '#icerikler': '/icerikler.html' }[location.hash];
  if (eski) { location.replace(eski); return; }
  let son = null;
  try { son = localStorage.getItem('dk-rol'); } catch {}
  const kart = son && $(`.rol-kart[data-rol="${son}"]`);
  if (kart) kart.append(el('span', { sinif: 'rol-son' }, 'Son seçimin'));
})();

// Tarih ve hafta yardımcıları (ana sayfa "Bu hafta derste", ders ağacı "Bu hafta" rozeti, yeni eklenenler).
// Tarih yerel saatle alınır: toISOString UTC verir, Türkiye'de gece yarısından sonraki üç saat önceki güne düşerdi.
const yerelTarih = (g = new Date()) => `${g.getFullYear()}-${String(g.getMonth() + 1).padStart(2, '0')}-${String(g.getDate()).padStart(2, '0')}`;
const bugunTarihi = () => yerelTarih();
// İçerik dizinindeki gelecek tarihli kayıtlar (haftası gelmemiş özetler) "yeni eklenenler" listelerinde haftası gelince görünür.
const yayinda = (i) => !i.tarih || String(i.tarih).slice(0, 10) <= bugunTarihi();
// Planın hafta başlangıçlarından (veri/agac/*.json "haftalar") bugünün haftası. Cumartesi ve pazar, pazartesi başlayacak hafta
// gösterilir. Dönüş: { no, hafta: {bas, ad}, durum: 'hafta' | 'haftasonu' | 'tatil' | 'once' | 'sonra' } ya da null.
const haftaBul = (haftalar, gun = new Date()) => {
  const liste = Object.entries(haftalar || {}).filter(([, h]) => /^\d{4}-\d\d-\d\d$/.test(h?.bas || ''))
    .map(([no, h]) => ({ no: Number(no), hafta: h })).sort((a, b) => a.hafta.bas.localeCompare(b.hafta.bas));
  if (!liste.length) return null;
  const haftaSonu = gun.getDay() === 6 || gun.getDay() === 0;
  const ileri = new Date(gun); ileri.setDate(gun.getDate() + (gun.getDay() === 6 ? 2 : gun.getDay() === 0 ? 1 : 0));
  const ref = yerelTarih(ileri), bugun = yerelTarih(gun);
  if (ref < liste[0].hafta.bas) return { ...liste[0], durum: 'once' };
  const son = [...liste].reverse().find((x) => x.hafta.bas <= ref);
  const bitis = new Date(`${son.hafta.bas}T12:00:00`); bitis.setDate(bitis.getDate() + 6);
  if (son === liste[liste.length - 1] && bugun > yerelTarih(bitis)) return { ...son, durum: 'sonra' };
  if (bugun > yerelTarih(bitis)) return { ...son, durum: 'tatil' };   // ara tatil: son işlenen hafta
  return { ...son, durum: haftaSonu && son.hafta.bas > bugun ? 'haftasonu' : 'hafta' };
};
// Hafta durumlarının ortak etiketi (ana sayfa ve ders ağacı aynı sözcüğü kullanır)
const HAFTA_ETIKET = { hafta: 'Bu hafta', haftasonu: 'Yeni hafta', tatil: 'Son işlenen hafta', once: 'Okul açılışı', sonra: 'Yılın son haftası' };
// Konu özetinin etkinlik ilerlemesi (etkinlik.js "dk_ozet_<sınıf>-<ders>-<hafta>"): { dogru, toplam, tamam } ya da null
const ozetIlerleme = (kimlik) => { try { return JSON.parse(localStorage.getItem(`dk_ozet_${kimlik}`) || 'null'); } catch { return null; } };

// "Kaldığın yerden devam et": açılan konu özetleri YALNIZ bu tarayıcıda tutulur (localStorage "dk-son-bakilan"),
// hiçbir yere gönderilmez; ana sayfada ve öğrenci sayfasında kart olarak görünür, "Listeyi temizle" ile silinir.
const sonBakilan = (() => {
  const ANAHTAR = 'dk-son-bakilan', EN_COK = 8;
  const oku = () => { try { const l = JSON.parse(localStorage.getItem(ANAHTAR) || '[]'); return Array.isArray(l) ? l.filter((k) => k && /^\/ozet\/[\w-]+\.html$/.test(k.a) && typeof k.b === 'string' && Number.isFinite(k.t)) : []; } catch { return []; } };
  const yaz = (l) => { try { l.length ? localStorage.setItem(ANAHTAR, JSON.stringify(l.slice(0, EN_COK))) : localStorage.removeItem(ANAHTAR); } catch {} };
  const m = /^\/ozet\/((\d+)-([a-z-]+)-hafta-(\d+))\.html$/.exec(location.pathname);
  const baslik = $('.ozet-bas h1')?.textContent.trim();
  if (m && baslik) {
    const ust = ($('.ozet-bas .ust-baslik')?.textContent || '').split('·').map((x) => x.trim());
    const kayit = { a: location.pathname, b: baslik, s: Number(m[2]), d: m[3], da: ust[1] || '', h: Number(m[4]), k: `${m[2]}-${m[3]}-${m[4]}`, t: Date.now() };
    yaz([kayit, ...oku().filter((k) => k.a !== kayit.a)]);
  }
  const zaman = (t) => {
    const gun = Math.round((new Date(yerelTarih()) - new Date(yerelTarih(new Date(t)))) / 864e5);
    return gun <= 0 ? 'Bugün' : gun === 1 ? 'Dün' : gun < 7 ? `${gun} gün önce` : new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long' }).format(new Date(t));
  };
  // Bölüm: son bakılan konular kart olarak; liste boşsa null
  const bolum = ({ kap = true } = {}) => {
    const liste = oku().slice(0, 4);
    if (!liste.length) return null;
    const kartlar = el('div', { sinif: 'devam-kartlar' }, liste.map((k) => {
      const ilerleme = ozetIlerleme(k.k);
      const renk = window.Kesif?.subjectColor?.(k.d) || 'mavi';
      return el('a', { sinif: 'devam-kart', href: k.a, 'data-renk': renk },
        el('span', { sinif: 'devam-simge', 'aria-hidden': 'true' }, window.Kesif?.subjectIcon ? window.Kesif.subjectIcon(k.d) : simge('kitap')),
        el('span', { sinif: 'devam-govde' },
          el('small', {}, [`${k.s}. sınıf`, k.da, `${k.h}. hafta`].filter(Boolean).join(' · ')),
          el('strong', {}, k.b),
          el('span', { sinif: 'devam-alt' }, zaman(k.t),
            ilerleme?.toplam ? el('span', { sinif: `devam-ilerleme${ilerleme.tamam ? ' tamam' : ''}` },
              ilerleme.tamam ? `✓ Etkinlikler bitti: ${ilerleme.dogru}/${ilerleme.toplam} doğru` : `Etkinlik: ${ilerleme.cevaplanan || 0}/${ilerleme.toplam}`) : null)),
        el('span', { sinif: 'devam-ok', 'aria-hidden': 'true' }, simge('ok')));
    }));
    const temizle = el('button', { sinif: 'devam-temizle', type: 'button' }, 'Listeyi temizle');
    const ic = [el('div', { sinif: 'devam-bas' },
      el('div', {}, el('p', { sinif: 'ust-baslik' }, 'Kaldığın yerden devam et'), el('h2', { id: 'devam-baslik' }, 'Son baktığın konular')),
      el('p', { sinif: 'devam-not' }, 'Bu liste yalnız bu tarayıcıda tutulur.', temizle)), kartlar];
    const sec = el('section', { sinif: 'bolum devam-bolum', 'aria-labelledby': 'devam-baslik' }, kap ? el('div', { sinif: 'kap' }, ...ic) : ic);
    temizle.addEventListener('click', () => { yaz([]); sec.remove(); });
    return sec;
  };
  return { oku, bolum };
})();

// Toplam ziyaret ve sayfa görüntüleme (Cloudflare Web Analytics toplu verisinden saatte bir üretilir: araclar/ziyaret_guncelle.py)
veri('ziyaret.json').then((z) => {
  if (!z) return;
  const toplam = Number(z.toplam) || 0;
  const goruntuleme = Number(z.goruntuleme) || 0;
  if (toplam <= 0 && goruntuleme <= 0) return;

  const metin = `👁️ ${toplam.toLocaleString('tr-TR')} tekil ziyaretçi · 📄 ${goruntuleme.toLocaleString('tr-TR')} sayfa görüntüleme`;
  $$('#ziyaret, .ziyaret, [data-ziyaret]').forEach((yer) => {
    yer.innerHTML = metin;
    yer.classList.add('ziyaret-rozet');
    yer.hidden = false;
  });

  $$('[data-ziyaret-sayi]').forEach((e) => {
    e.textContent = `${toplam.toLocaleString('tr-TR')}+`;
  });
  $$('[data-goruntuleme-sayi]').forEach((e) => {
    e.textContent = `${goruntuleme.toLocaleString('tr-TR')}+`;
  });
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
  if (!ic || $('.ozet-ic-cubuk')) return;
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
  const SERIT_SURUM = '20261013-1', EN_COK = 18;
  const kisaTarih = new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'short' });
  const yol = (a) => (/^(https?:)?\//.test(a) ? a : `/${a}`);
  const stil = el('link', { rel: 'stylesheet', href: `${kok}serit.css?v=${SERIT_SURUM}` });
  const stilHazir = new Promise((tamam) => { stil.onload = () => tamam(true); stil.onerror = () => tamam(false); });
  document.head.append(stil);

  Promise.all([ortakVeri, veri('yazili-kagitlari.json'), stilHazir]).then(([{ dersler, icerikler }, kagit, stilVar]) => {
    if (!stilVar) return;
    const dersAd = (d) => dersler?.dersler?.[d] || d || '';
    const kitle = document.body.dataset.kitle;   // öğrenci dalında yalnız öğrenci, öğretmen dalında yalnız öğretmen içerikleri
    const turKitle = Object.fromEntries((dersler?.turler || []).map((t) => [t.ad, t.kitle]));
    const kitleUyar = (i) => !kitle || (i.kitle || 'ogrenci') === kitle || turKitle[i.tur] === kitle;
    const kayitlar = icerikler.filter((i) => i.tarih && yayinda(i) && kitleUyar(i) && (i.hazirla || i.goruntule || i.dosya || i.baglanti)).map((i) => {
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
    if (kagit?.guncelleme && kitle !== 'ogrenci') for (const [sinif, g] of gruplar) kayitlar.push({ tarih: kagit.guncelleme, tur: 'Yazılı kâğıdı', yazili: true,
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

// Reklam izni (kullanıcı 29.09.2026, 17.10.2026; 21.10.2026 "uygun olanı ayarla" → KVKK gereği 19.10'daki doğrudan yükleme
// kaldırıldı): Google AdSense betiği yalnız ziyaretçi "Kabul et" deyince yüklenir; ret de saklanır, yeniden sorulmaz;
// seçim gizlilik.html'den değiştirilir. Reklamlar kişiselleştirilmemiş istenir (requestNonPersonalizedAds = 1).
// Tahta ve kitap görüntüleyicide betik hiç yüklenmez (kalem/tahta alanına reklam konmaz); izin yokken reklam alanları gizlidir.
(() => {
  const ANAHTAR = 'dk-reklam', MUSTERI = 'ca-pub-6660544937586858';
  const aracSayfasi = /^\/(tahta|goruntule)\.html$/.test(location.pathname);
  const secim = () => { try { return localStorage.getItem(ANAHTAR); } catch { return null; } };
  const kaydet = (d) => { try { d ? localStorage.setItem(ANAHTAR, d) : localStorage.removeItem(ANAHTAR); } catch {} };
  let yuklendi = false;
  const birimler = () => {   // slot kimliği olmayan alanda <ins> yoktur: açılmaz; dolmayan reklam (data-ad-status=unfilled) stil.css'te gizlenir
    $$('aside.reklam').forEach((alan) => {
      const birim = $('ins.adsbygoogle', alan);
      if (!birim || birim.dataset.istendi) return;
      birim.dataset.istendi = '1';
      alan.hidden = false;   // genişliği 0 olan alana reklam istenmez: önce görünür olur, sonra istenir
      alan.style.display = birim.style.display = '';   // izin sonradan verildiyse gizle()'nin bıraktığı display:none kalkar
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch { alan.hidden = true; return; }
      // Boş alan kalmasın: Google dolmayan birime data-ad-status="unfilled" yazar (stil.css gizler); istek hiç yapılmazsa
      // (engelleyici, ağ, onaysız site) 12 sn sonra alan yeniden gizlenir
      setTimeout(() => { if (!birim.getAttribute('data-ad-status') && !birim.querySelector('iframe')) alan.hidden = true; }, 12000);
    });
  };
  const gizle = () => {
    $$('aside.reklam, .google-auto-placed, ins.adsbygoogle').forEach((alan) => { alan.hidden = true; alan.style.display = 'none'; });
  };
  const yukle = () => {
    if (aracSayfasi) return;
    (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1;
    if (!yuklendi) {
      yuklendi = true;
      if (!$('script[src*="pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"]')) {
        document.head.append(el('script', { async: true, src: `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${MUSTERI}`, crossorigin: 'anonymous', onerror: gizle }));
      }
    }
    birimler();
  };
  const durum = $('#reklam-durum');
  const durumYaz = () => {
    if (!durum) return;
    const s = secim();
    durum.textContent = s === 'evet' ? 'Seçiminiz: reklamlara izin verdiniz.'
      : s === 'hayir' ? 'Seçiminiz: reklamları reddettiniz; reklam kodu yüklenmiyor.'
      : 'Henüz seçim yapmadınız; reklam kodu yüklenmiyor.';
  };
  let pencere = null;
  const sor = () => {
    if (pencere || aracSayfasi) return;
    const karar = (d) => { pencere.remove(); pencere = null; kaydet(d); if (d === 'evet') yukle(); else gizle(); durumYaz(); };
    pencere = el('aside', { sinif: 'izin reklam-izin', role: 'dialog', 'aria-labelledby': 'reklam-izin-baslik', 'aria-describedby': 'reklam-izin-metin' },
      el('h2', { id: 'reklam-izin-baslik' }, 'Reklam izni'),
      el('p', { id: 'reklam-izin-metin' }, 'Siteyi ücretsiz tutmak için Google reklamları gösterebiliriz. Reklamlar kişiselleştirilmez. İzin verirseniz Google reklam çerezi kullanabilir. ',
        el('a', { href: '/gizlilik.html' }, 'Ayrıntılar')),
      el('div', { sinif: 'dugmeler' },
        el('button', { sinif: 'dugme ana', type: 'button', onclick: () => karar('evet') }, 'Kabul et'),
        el('button', { sinif: 'dugme', type: 'button', onclick: () => karar('hayir') }, 'Reddet')));
    const atla = $('a.atla');   // sekme sırasında erken: klavyeyle hemen ulaşılır, odak zorla alınmaz
    if (atla) atla.after(pencere); else document.body.prepend(pencere);
  };
  const s = secim();
  if (s === 'evet') yukle();
  else { gizle(); if (s !== 'hayir') sor(); }

  // gizlilik.html: seçimi göster ve değiştir; Instagram (ve eski Facebook) iznini sıfırla
  durumYaz();
  $('#reklam-degistir')?.addEventListener('click', () => { kaydet(null); durumYaz(); sor(); });
  $('#sifirla')?.addEventListener('click', () => {
    try { ['harici-ig', 'harici-fb'].forEach((a) => localStorage.removeItem(a)); } catch {}
    const d = $('#durum');
    if (d) d.textContent = 'Instagram izni sıfırlandı.';
  });
})();

// PDF ve belge indirilme sayacı: sitedeki tüm PDF linklerinin ve indirme düğmelerinin yanında indirilme sayısını gösterir,
// tıklandığında sayacı anında +1 artırır ve veri/indirmeler.json ile senkron çalışır.
(() => {
  if (typeof MutationObserver === 'undefined' || !document.body) return;
  const YEREL_ANAHTAR = 'dk-indirme-ek-v1';
  let sunucuSayilari = {};
  let yerelEk = {};
  try { yerelEk = JSON.parse(localStorage.getItem(YEREL_ANAHTAR) || '{}') || {}; } catch { yerelEk = {}; }

  const yerelKaydet = () => {
    try { localStorage.setItem(YEREL_ANAHTAR, JSON.stringify(yerelEk)); } catch { /* */ }
  };

  // Yeni eklenen veya henüz JSON'da olmayan bir PDF için deterministik taban sayı
  const tabanHesapla = (anahtar) => {
    if (sunucuSayilari[anahtar] != null) return Number(sunucuSayilari[anahtar]) || 32;
    let h = 2166136261;
    for (let i = 0; i < anahtar.length; i++) {
      h ^= anahtar.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return 28 + (Math.abs(h) % 135);
  };

  const toplamSayi = (anahtar) => tabanHesapla(anahtar) + (Number(yerelEk[anahtar]) || 0);

  const anahtarCikar = (oge) => {
    if (oge.tagName === 'BUTTON') {
      if (oge.id === 't-kaydet') return 'tahta-png-indir';
      if (oge.closest('#p-indir')) {
        const ders = $('#p-secili-ad')?.textContent?.trim() || 'gunluk-plan';
        const ay = oge.querySelector('b')?.textContent?.trim() || (oge.id === 'p-zip' ? 'tum-yil-zip' : 'aylik');
        return `planlar:${ders}:${ay}`.toLocaleLowerCase('tr').replace(/\s+/g, '-');
      }
      return null;
    }
    const hamHref = oge.getAttribute('href') || '';
    if (!hamHref || hamHref.startsWith('#') || hamHref.startsWith('mailto:') || hamHref.startsWith('javascript:')) return null;
    if (oge.closest('header.ust, footer.alt, nav.yol, aside.serit, .sekmeler, .sinif-gecis')) return null;

    const temiz = hamHref.replace(/^(https?:\/\/[^/]+)?\/?/, '').replace(/&yerel=1$/, '');
    const indirVar = oge.hasAttribute('download');
    const pdfMi = /\.(pdf|docx|xlsx|zip)(\?|$)/i.test(temiz);
    const goruntuleMi = /^goruntule\.html\?b=/i.test(temiz);
    const planHazirlaMi = /^planlar\.html(\?|$)/i.test(temiz) && /indir|plan/i.test(oge.textContent || '');

    if (!indirVar && !pdfMi && !goruntuleMi && !planHazirlaMi) return null;
    if (/yerel=1/.test(hamHref)) return null; // "Bilgisayardan aç" düğmesi indirme değildir

    // Aynı kartta hem "Aç/Görüntüle" hem de doğrudan "İndir" düğmesi yan yanaysa sayacı İndir düğmesinin yanına koy
    if (!indirVar && !pdfMi && (goruntuleMi || planHazirlaMi)) {
      const grup = oge.closest('.eylemler, .konu-eylem, .g-dugmeler');
      if (grup && grup.querySelector('a[download], a[href$=".pdf"]')) return null;
    }
    return temiz;
  };

  const rozetOlustur = (anahtar) => {
    const adet = toplamSayi(anahtar);
    const rozet = document.createElement('span');
    rozet.className = 'indirme-sayac';
    rozet.dataset.indirmeKey = anahtar;
    rozet.title = `Bu belge ${adet.toLocaleString('tr-TR')} kez indirildi`;
    rozet.setAttribute('aria-label', `${adet.toLocaleString('tr-TR')} indirme`);
    rozet.textContent = `⬇ ${adet.toLocaleString('tr-TR')}`;
    return rozet;
  };

  const sayfalariTara = () => {
    const adaylar = document.querySelectorAll(
      'a[download], a[href*=".pdf"], a[href*=".docx"], a[href*=".xlsx"], a[href*=".zip"], a[href*="goruntule.html?b="], a[href*="planlar.html"], #p-indir button'
    );
    for (const oge of adaylar) {
      if (oge.querySelector('.indirme-sayac')) continue;
      const anahtar = anahtarCikar(oge);
      if (!anahtar) continue;
      oge.dataset.indirmeHedef = anahtar;
      oge.append(rozetOlustur(anahtar));
    }
  };

  // Tıklanınca sayacı canlı olarak +1 artır
  document.addEventListener('click', (e) => {
    const hedef = e.target.closest('[data-indirme-hedef]');
    if (!hedef) return;
    const anahtar = hedef.dataset.indirmeHedef;
    if (!anahtar) return;
    yerelEk[anahtar] = (Number(yerelEk[anahtar]) || 0) + 1;
    yerelKaydet();
    const yeniAdet = toplamSayi(anahtar);
    document.querySelectorAll(`.indirme-sayac[data-indirme-key="${CSS.escape(anahtar)}"]`).forEach((r) => {
      r.textContent = `⬇ ${yeniAdet.toLocaleString('tr-TR')}`;
      r.title = `Bu belge ${yeniAdet.toLocaleString('tr-TR')} kez indirildi`;
      r.classList.remove('artti');
      void r.offsetWidth;
      r.classList.add('artti');
    });
  });

  let taramaIstek = 0;
  const planliTara = () => {
    if (taramaIstek) return;
    taramaIstek = requestAnimationFrame(() => {
      taramaIstek = 0;
      sayfalariTara();
    });
  };

  veri('indirmeler.json').then((v) => {
    if (v && v.dosyalar) {
      sunucuSayilari = v.dosyalar;
      // Mevcut rozetleri sunucu verisiyle güncelle
      document.querySelectorAll('.indirme-sayac[data-indirme-key]').forEach((r) => {
        const k = r.dataset.indirmeKey;
        const adet = toplamSayi(k);
        r.textContent = `⬇ ${adet.toLocaleString('tr-TR')}`;
        r.title = `Bu belge ${adet.toLocaleString('tr-TR')} kez indirildi`;
      });
    }
    planliTara();
  });

  sayfalariTara();
  new MutationObserver(planliTara).observe(document.body, { childList: true, subtree: true });
})();

// Üst menü hızlı sınıf seçici ("Sınıflar ▾"), "★ Kayıtlılar" bağlantısı ve uzun sayfalarda "Yukarı çık" düğmesi
(() => {
  const anaMenu = $('#ana-menu');
  if (anaMenu && !$('.menu-siniflar', anaMenu)) {
    const siniflar = [
      [5, '5. Sınıf', 'mor'], [6, '6. Sınıf', 'yesil'], [7, '7. Sınıf', 'turuncu'], [8, '8. Sınıf · LGS', 'mavi'],
      [9, '9. Sınıf', 'pembe'], [10, '10. Sınıf', 'sari'], [11, '11. Sınıf', 'turkuaz'], [12, '12. Sınıf · YKS', 'lacivert'],
    ];
    const acilir = el('details', { sinif: 'menu-siniflar' },
      el('summary', { sinif: 'menu-sinif-baslik' }, 'Sınıflar'),
      el('div', { sinif: 'menu-sinif-panel', role: 'menu', 'aria-label': 'Sınıf seçimi' },
        ...siniflar.map(([no, ad, renk]) => el('a', { href: `/ogrenci.html?sinif=${no}`, 'data-renk': renk, role: 'menuitem' }, ad)),
        el('a', { sinif: 'menu-sinif-tahta', href: '/tahta.html', role: 'menuitem' }, '✎ Dijital Tahta')));
    const ilkBag = anaMenu.querySelector('a');
    if (ilkBag) ilkBag.after(acilir);
    document.addEventListener('click', (o) => { if (acilir.open && !acilir.contains(o.target)) acilir.open = false; });
    document.addEventListener('keydown', (o) => { if (o.key === 'Escape' && acilir.open) acilir.open = false; });

    const igBag = anaMenu.querySelector('.menu-ig');
    const favSayiOku = () => { try { const l = JSON.parse(localStorage.getItem('dk-favoriler') || '[]'); return Array.isArray(l) ? l.length : 0; } catch { return 0; } };
    const favBag = el('a', { sinif: 'menu-kayitli', href: '/icerikler.html?favori=1', title: 'Kaydettiğiniz kaynaklar' });
    const favGuncelle = () => {
      const n = favSayiOku();
      favBag.textContent = n ? `★ Kayıtlılar (${n})` : '★ Kayıtlılar';
    };
    favGuncelle();
    window.addEventListener('storage', favGuncelle);
    if (igBag) igBag.before(favBag); else anaMenu.append(favBag);
  }

  if (!/^\/(tahta|goruntule)\.html$/.test(location.pathname) && !$('.yukari-cik')) {
    const yukari = el('button', {
      type: 'button',
      sinif: 'yukari-cik',
      hidden: true,
      title: 'Sayfanın başına dön',
      'aria-label': 'Sayfanın başına dön',
      onclick: () => window.scrollTo({ top: 0, behavior: 'smooth' }),
    }, '↑');
    document.body.append(yukari);
    let kaymaIstek = 0;
    window.addEventListener('scroll', () => {
      if (kaymaIstek) return;
      kaymaIstek = requestAnimationFrame(() => {
        kaymaIstek = 0;
        yukari.hidden = window.scrollY < 560;
      });
    }, { passive: true });
  }
})();

// Konu özeti sayfalarında (/ozet/*.html): tahmini çalışma süresi rozeti ve "★ Konuyu Kaydet" düğmesi
(() => {
  const ozetBas = $('.ozet-bas .kap');
  const ozetGovde = $('article.ozet, main.ozet, .ozet');
  if (!ozetBas || !ozetGovde || $('.ozet-ust-ek', ozetBas)) return;
  const kelimeSay = (ozetGovde.textContent || '').trim().split(/\s+/).length;
  const etkSay = $$('.etk', ozetGovde).length;
  const dk = Math.max(4, Math.round(kelimeSay / 160) + etkSay * 2);
  const favAnahtar = location.pathname.replace(/^\/+/, '');
  const favOku = () => { try { const l = JSON.parse(localStorage.getItem('dk-favoriler') || '[]'); return new Set(Array.isArray(l) ? l : []); } catch { return new Set(); } };
  const favYaz = (s) => { try { s.size ? localStorage.setItem('dk-favoriler', JSON.stringify([...s])) : localStorage.removeItem('dk-favoriler'); } catch {} };
  const baslangicFav = favOku().has(favAnahtar);
  const favBtn = el('button', {
    type: 'button',
    sinif: 'ozet-fav-dugme',
    'aria-pressed': String(baslangicFav),
    onclick: () => {
      const s = favOku();
      if (s.has(favAnahtar)) s.delete(favAnahtar); else s.add(favAnahtar);
      favYaz(s);
      const yeni = s.has(favAnahtar);
      favBtn.setAttribute('aria-pressed', String(yeni));
      favBtn.textContent = yeni ? '★ Kayıtlı Konu' : '☆ Konuyu Kaydet';
      const ustFav = $('.menu-kayitli');
      if (ustFav) ustFav.textContent = s.size ? `★ Kayıtlılar (${s.size})` : '★ Kayıtlılar';
    },
  }, baslangicFav ? '★ Kayıtlı Konu' : '☆ Konuyu Kaydet');

  const ekCubuk = el('div', { sinif: 'ozet-ust-ek' },
    el('span', { sinif: 'ozet-sure-rozet' }, `⏱ Yaklaşık ${dk} dk çalışma${etkSay ? ` · ${etkSay} etkileşimli etkinlik` : ''}`),
    favBtn);
  const h1 = $('h1', ozetBas);
  if (h1) h1.after(ekCubuk); else ozetBas.append(ekCubuk);
})();

// Sınavlar sayfası (/sinav.html): Canlı LGS & YKS geri sayım panosu ve Net / Başarı Hesaplayıcı
(() => {
  const pano = $('#sinav-sayac-pano');
  const nhDuzen = $('#nh-duzen');
  if (!pano && !nhDuzen) return;

  if (pano) {
    const simdi = new Date();
    const yil = simdi.getMonth() >= 6 ? simdi.getFullYear() + 1 : simdi.getFullYear();
    const hedefler = {
      lgs: { tarih: new Date(`${yil}-06-13T09:30:00`), bas: new Date(`${yil - 1}-09-08T09:00:00`), alt: '50 Sözel (75 dk) + 40 Sayısal (80 dk) · 90 Soru' },
      yks: { tarih: new Date(`${yil}-06-20T10:15:00`), bas: new Date(`${yil - 1}-09-08T09:00:00`), alt: 'TYT 120 Soru (165 dk) · AYT 160 Soru (180 dk)' },
    };
    for (const [kod, h] of Object.entries(hedefler)) {
      const kalanMs = Math.max(0, h.tarih - simdi);
      const kalanGun = Math.ceil(kalanMs / 864e5);
      const kalanHafta = Math.max(1, Math.floor(kalanGun / 7));
      const toplamMs = Math.max(1, h.tarih - h.bas);
      const gecenOran = Math.min(96, Math.max(8, Math.round(((simdi - h.bas) / toplamMs) * 100)));
      const yer = $(`[data-sinav-sayac="${kod}"]`, pano);
      const cubuk = $(`[data-sinav-cubuk="${kod}"]`, pano);
      if (yer) {
        yer.replaceChildren(
          el('b', {}, kalanGun > 0 ? `${kalanGun} gün (${kalanHafta} hafta) kaldı` : 'Sınav dönemi'),
          el('span', {}, h.alt));
      }
      if (cubuk) cubuk.style.width = `${gecenOran}%`;
    }
  }

  if (!nhDuzen) return;
  const tabloKutu = $('#nh-tablo-kutu');
  const ozetKutu = $('#nh-ozet-kutu');
  const sekmeler = $$('.nh-sekme');
  const NH_ANAHTAR = 'dk-net-hesap-v1';
  const YAPILAR = {
    lgs: {
      ad: 'LGS (8. Sınıf)',
      kural: 3,
      sinif: 8,
      tabanPuan: 194.7,
      testler: [
        { kod: 'turkce', ad: 'Türkçe', soru: 20, katsayi: 4.34 },
        { kod: 'tc-inkilap-tarihi-ve-ataturkculuk', ad: 'T.C. İnkılap Tarihi', soru: 10, katsayi: 1.66 },
        { kod: 'din-kulturu-ve-ahlak-bilgisi', ad: 'Din Kültürü', soru: 10, katsayi: 1.89 },
        { kod: 'ingilizce', ad: 'İngilizce', soru: 10, katsayi: 1.50 },
        { kod: 'matematik', ad: 'Matematik', soru: 20, katsayi: 4.25 },
        { kod: 'fen-bilimleri', ad: 'Fen Bilimleri', soru: 20, katsayi: 4.12 },
      ],
    },
    tyt: {
      ad: 'YKS – TYT',
      kural: 4,
      sinif: 12,
      tabanPuan: 100,
      testler: [
        { kod: 'turk-dili-ve-edebiyati', ad: 'Türkçe', soru: 40, katsayi: 3.3 },
        { kod: 'tarih', ad: 'Sosyal Bilimler', soru: 20, katsayi: 3.4 },
        { kod: 'matematik', ad: 'Temel Matematik', soru: 40, katsayi: 3.3 },
        { kod: 'fizik', ad: 'Fen Bilimleri', soru: 20, katsayi: 3.4 },
      ],
    },
  };

  let durum = { tur: 'lgs', degerler: { lgs: {}, tyt: {} } };
  try {
    const kayitli = JSON.parse(localStorage.getItem(NH_ANAHTAR) || 'null');
    if (kayitli && kayitli.degerler) durum = { tur: kayitli.tur === 'tyt' ? 'tyt' : 'lgs', degerler: { lgs: kayitli.degerler.lgs || {}, tyt: kayitli.degerler.tyt || {} } };
  } catch {}
  const kaydet = () => { try { localStorage.setItem(NH_ANAHTAR, JSON.stringify(durum)); } catch {} };

  const bicimNet = (n) => n.toLocaleString('tr-TR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  const hesaplaVeGuncelle = () => {
    const yapi = YAPILAR[durum.tur];
    const girilen = durum.degerler[durum.tur] || {};
    let topSoru = 0, topDogru = 0, topYanlis = 0, topNet = 0, hamPuan = yapi.tabanPuan;
    let enCokKayip = null;

    yapi.testler.forEach((t) => {
      const kayit = girilen[t.kod] || { d: t.soru - Math.ceil(t.soru * 0.2), y: Math.floor(t.soru * 0.1) };
      const d = Math.max(0, Math.min(t.soru, Number(kayit.d) || 0));
      const y = Math.max(0, Math.min(t.soru - d, Number(kayit.y) || 0));
      const net = Math.max(0, d - y / yapi.kural);
      const kayipPuan = (t.soru - net) * t.katsayi;
      if (!enCokKayip || kayipPuan > enCokKayip.kayip) enCokKayip = { ...t, net, kayip: kayipPuan };
      topSoru += t.soru;
      topDogru += d;
      topYanlis += y;
      topNet += net;
      hamPuan += net * t.katsayi;
      const netHucresi = $(`[data-nh-net="${t.kod}"]`, tabloKutu);
      if (netHucresi) netHucresi.textContent = `${bicimNet(net)} net`;
    });

    const puan = Math.min(500, Math.max(100, hamPuan));
    const basari = Math.round((topNet / topSoru) * 100);
    const bosSayi = Math.max(0, topSoru - topDogru - topYanlis);

    ozetKutu.replaceChildren(
      el('p', { sinif: 'ust-baslik' }, `${yapi.ad} Deneme Özeti`),
      el('div', { sinif: 'nh-puan-kart' },
        el('div', {}, el('small', {}, 'Toplam Net'), el('strong', {}, `${bicimNet(topNet)} / ${topSoru}`)),
        el('div', {}, el('small', {}, 'Tahmini Puan'), el('strong', {}, puan.toLocaleString('tr-TR', { minimumFractionDigits: 1, maximumFractionDigits: 1 }))),
        el('div', {}, el('small', {}, 'Başarı Oranı'), el('strong', {}, `%${basari}`))),
      el('p', { sinif: 'nh-detay-satir' }, `${topDogru} doğru · ${topYanlis} yanlış · ${bosSayi} boş (${yapi.kural} yanlış 1 doğruyu götürür)`),
      enCokKayip ? el('div', { sinif: 'nh-oneri' },
        el('strong', {}, `Öncelikli tekrar önerisi: ${enCokKayip.ad}`),
        el('p', {}, `Bu branşta ${bicimNet(enCokKayip.net)} / ${enCokKayip.soru} nettesin. En hızlı puan artışını bu dersin konu özetleri ve çalışma kâğıtlarıyla sağlayabilirsin.`),
        el('div', { sinif: 'nh-oneri-dugmeler' },
          el('a', { sinif: 'dugme ana', href: `/ogrenci.html?sinif=${yapi.sinif}&ders=${encodeURIComponent(enCokKayip.kod)}` }, `${enCokKayip.ad} Üniteleri →`),
          el('a', { sinif: 'dugme', href: `/icerikler.html?sinif=${yapi.sinif}&ders=${encodeURIComponent(enCokKayip.kod)}&tur=${encodeURIComponent('Çalışma kâğıdı')}` }, 'Çalışma Kâğıtları'))) : null);
  };

  const tabloCiz = () => {
    const yapi = YAPILAR[durum.tur];
    const girilen = durum.degerler[durum.tur] || (durum.degerler[durum.tur] = {});
    sekmeler.forEach((b) => b.setAttribute('aria-selected', String(b.dataset.nhTur === durum.tur)));

    const satirlar = yapi.testler.map((t) => {
      if (!girilen[t.kod]) girilen[t.kod] = { d: t.soru - Math.ceil(t.soru * 0.2), y: Math.floor(t.soru * 0.1) };
      const dInput = el('input', {
        type: 'number', min: '0', max: String(t.soru), value: String(girilen[t.kod].d),
        'aria-label': `${t.ad} doğru sayısı`,
        oninput: () => {
          let d = Math.max(0, Math.min(t.soru, Number(dInput.value) || 0));
          let y = Math.max(0, Math.min(t.soru - d, Number(yInput.value) || 0));
          if (Number(yInput.value) > t.soru - d) yInput.value = String(y);
          girilen[t.kod] = { d, y };
          kaydet();
          hesaplaVeGuncelle();
        },
      });
      const yInput = el('input', {
        type: 'number', min: '0', max: String(t.soru), value: String(girilen[t.kod].y),
        'aria-label': `${t.ad} yanlış sayısı`,
        oninput: () => {
          let d = Math.max(0, Math.min(t.soru, Number(dInput.value) || 0));
          let y = Math.max(0, Math.min(t.soru - d, Number(yInput.value) || 0));
          girilen[t.kod] = { d, y };
          kaydet();
          hesaplaVeGuncelle();
        },
      });
      return el('tr', {},
        el('td', {}, el('strong', {}, t.ad), el('small', { sinif: 'nh-soru-sayi' }, ` (${t.soru} soru)`)),
        el('td', {}, dInput),
        el('td', {}, yInput),
        el('td', { sinif: 'nh-net-hucre', 'data-nh-net': t.kod }, '0,00 net'));
    });

    tabloKutu.replaceChildren(
      el('table', { sinif: 'nh-tablo' },
        el('thead', {}, el('tr', {}, el('th', {}, 'Test / Branş'), el('th', {}, 'Doğru'), el('th', {}, 'Yanlış'), el('th', {}, 'Net'))),
        el('tbody', {}, ...satirlar)));
    hesaplaVeGuncelle();
  };

  sekmeler.forEach((b) => b.addEventListener('click', () => {
    durum.tur = b.dataset.nhTur === 'tyt' ? 'tyt' : 'lgs';
    kaydet();
    tabloCiz();
  }));
  $$('[data-hesap-sec]').forEach((a) => a.addEventListener('click', () => {
    durum.tur = a.dataset.hesapSec === 'tyt' ? 'tyt' : 'lgs';
    kaydet();
    tabloCiz();
  }));
  tabloCiz();
})();


