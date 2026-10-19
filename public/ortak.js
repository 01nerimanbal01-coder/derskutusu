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

// Toplam ziyaret ve sayfa görüntüleme (Cloudflare Web Analytics toplu verisinden günde bir kez üretilir: araclar/ziyaret_guncelle.py)
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
    const kayitlar = icerikler.filter((i) => i.tarih && kitleUyar(i) && (i.hazirla || i.goruntule || i.dosya || i.baglanti)).map((i) => {
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

// Reklam yönetimi (kullanıcı 29.09.2026, 17.10.2026, 19.10.2026): Google AdSense betiği kişiselleştirilmemiş reklam moduyla
// (requestNonPersonalizedAds = 1) doğrudan çalışır; ziyaretçi gizlilik.html sayfasından dilediği zaman reklamları kapatıp açabilir.
// Tahta ve kitap görüntüleyicide reklam yüklenmez (kalem/tahta alanına reklam konmaz).
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
    durum.textContent = s === 'hayir'
      ? 'Seçiminiz: reklamları kapattınız; bu cihazda reklam gösterilmiyor.'
      : 'Seçiminiz: kişiselleştirilmemiş reklamlar açık.';
  };
  if (secim() === 'hayir') gizle(); else yukle();

  // gizlilik.html: seçimi göster ve değiştir; Instagram (ve eski Facebook) iznini sıfırla
  durumYaz();
  $('#reklam-degistir')?.addEventListener('click', () => {
    const yeni = secim() === 'hayir' ? 'evet' : 'hayir';
    kaydet(yeni);
    if (yeni === 'hayir') gizle(); else yukle();
    durumYaz();
  });
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

