// Sitenin bütün içeriği veri/*.json dosyalarından gelir.
// youtube.json ve instagram.json her gün araclar/akis_guncelle.py ile yenilenir (GitHub Actions).
// Dışarıdan (YouTube, Instagram, Facebook) hiçbir şey ziyaretçi tıklamadan yüklenmez.

const $ = (s, k = document) => k.querySelector(s);
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
const tarihBicim = new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' });
const tarih = (t) => (t ? el('time', { datetime: t }, tarihBicim.format(new Date(t))) : null);
const bosKutu = (metin) => el('div', { sinif: 'bos' }, metin);
const tercih = {
  al: (a) => { try { return localStorage.getItem(a) === '1'; } catch { return false; } },
  koy: (a) => { try { localStorage.setItem(a, '1'); } catch {} },
};

async function veri(ad) {
  try {
    const y = await fetch(`veri/${ad}`, { cache: 'no-cache' });
    return y.ok ? await y.json() : null;
  } catch { return null; }
}

function ayarlariUygula(a) {
  document.querySelectorAll('[data-ayar]').forEach((e) => { if (a[e.dataset.ayar]) e.textContent = a[e.dataset.ayar]; });
  if (a.site_adi) document.title = `${a.site_adi} · ${a.slogan || ''}`.replace(/ · $/, '');
  const hesaplar = $('#hesaplar');
  const baglar = [
    ['youtube', 'yt', 'YouTube', 'tumu-video'],
    ['instagram', 'ig', 'Instagram', 'tumu-ig'],
    ['facebook', 'fb', 'Facebook', 'tumu-fb'],
  ];
  for (const [anahtar, sinif, ad, tumu] of baglar) {
    const adres = a[anahtar]?.adres;
    if (!adres) continue;
    hesaplar.append(el('a', { sinif: 'dugme', href: adres, target: '_blank', rel: 'noopener' },
      el('span', { sinif: `platform ${sinif}`, 'aria-hidden': 'true' }), ad));
    const t = document.getElementById(tumu);
    t.href = adres; t.hidden = false;
  }
  if (!hesaplar.children.length) hesaplar.append(el('span', { sinif: 'soluk' }, 'Sosyal medya hesapları bağlanınca burada görünür.'));
  if (a.eposta) $('#eposta').append(el('a', { href: `mailto:${a.eposta}` }, a.eposta));
}

function icerikleriGoster(v) {
  const liste = v?.icerikler || [];
  $('#rozet-icerik').hidden = v?.kaynak !== 'ornek';
  $('#sayi-icerik').textContent = liste.length;
  const kartlar = $('#kartlar');
  const dersler = ['Tümü', ...new Set(liste.map((i) => i.ders).filter(Boolean))];
  const ciz = (ders) => {
    kartlar.replaceChildren(...liste.filter((i) => ders === 'Tümü' || i.ders === ders).map((i) =>
      el('article', { sinif: 'kart' },
        el('div', { sinif: 'ust-bilgi' },
          i.ders && el('span', { sinif: 'etiket' }, i.ders),
          i.sinif && el('span', { sinif: 'etiket tur' }, i.sinif),
          i.tur && el('span', { sinif: 'etiket tur' }, i.tur)),
        el('h3', {}, i.baslik),
        i.aciklama && el('p', {}, i.aciklama),
        i.baglanti && el('a', { sinif: 'ac', href: i.baglanti, target: '_blank', rel: 'noopener' }, 'Aç →'))));
    if (!kartlar.children.length) kartlar.append(bosKutu('Henüz içerik eklenmedi.'));
  };
  const suzgec = $('#suzgec');
  if (dersler.length > 2) {
    suzgec.replaceChildren(...dersler.map((d, s) => el('button', {
      type: 'button', 'aria-pressed': String(s === 0),
      onclick: (o) => {
        suzgec.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(b === o.currentTarget)));
        ciz(d);
      },
    }, d)));
  }
  ciz('Tümü');
}

function videolariGoster(v) {
  const liste = v?.videolar || [];
  $('#rozet-video').hidden = v?.kaynak !== 'ornek';
  $('#sayi-video').textContent = liste.length;
  const kutu = $('#video-listesi');
  if (!liste.length) { kutu.append(bosKutu('YouTube kanalı bağlanınca son videolar burada görünür.')); return; }
  const ornek = v.kaynak === 'ornek';
  kutu.replaceChildren(...liste.map((i) => {
    const kapak = el('button', {
      sinif: 'kapak', type: 'button', 'aria-label': `${i.baslik} videosunu oynat`,
      onclick: () => {
        if (ornek) return;
        kapak.replaceWith(el('iframe', {
          src: `https://www.youtube-nocookie.com/embed/${encodeURIComponent(i.id)}?autoplay=1&rel=0`,
          title: i.baslik, allow: 'autoplay; encrypted-media; picture-in-picture', allowfullscreen: true, loading: 'lazy',
        }));
      },
    }, el('img', { src: i.gorsel, alt: '', loading: 'lazy' }), el('span', { sinif: 'oynat' }),
    i.kisa && el('span', { sinif: 'kisa-etiket' }, 'Kısa'));
    return el('article', { sinif: 'video' }, kapak, el('h3', {}, i.baslik), tarih(i.tarih));
  }));
}

function instagramGoster(v, ayar) {
  const liste = v?.gonderiler || [];
  $('#rozet-ig').hidden = v?.kaynak !== 'ornek';
  $('#sayi-paylasim').textContent = liste.length;
  const kutu = $('#ig-listesi');
  if (!liste.length) { kutu.append(bosKutu('Instagram hesabı bağlanınca paylaşımlar burada görünür.')); return; }
  const profil = ayar.instagram?.adres || null;
  // Görseli olan gönderi (API ya da örnek) yerel görselle gösterilir; yalnız bağlantısı olan (elle eklenen)
  // gönderi Instagram'ın resmî gömme koduyla, ziyaretçi izin verince yüklenir.
  const gorselli = liste.filter((i) => i.gorsel);
  const elle = liste.filter((i) => !i.gorsel && i.baglanti);
  kutu.replaceChildren(...gorselli.map((i) =>
    el('a', { sinif: 'gonderi', href: i.baglanti || profil || '#instagram', target: i.baglanti || profil ? '_blank' : null, rel: 'noopener' },
      el('img', { src: i.gorsel, alt: i.aciklama ? i.aciklama.slice(0, 120) : 'Instagram gönderisi', loading: 'lazy' }),
      i.tur === 'VIDEO' && el('span', { sinif: 'video-isaret', 'aria-hidden': 'true' }),
      i.aciklama && el('span', { sinif: 'ust-yazi' }, i.aciklama))));
  if (elle.length) {
    const gomulu = () => {
      kutu.append(...elle.map((i) => el('div', { sinif: 'gomulu' },
        el('blockquote', { class: 'instagram-media', 'data-instgrm-permalink': i.baglanti, 'data-instgrm-version': '14' },
          el('a', { href: i.baglanti, target: '_blank', rel: 'noopener' }, 'Gönderiyi Instagram’da aç')))));
      document.body.append(el('script', { src: 'https://www.instagram.com/embed.js', async: true }));
    };
    if (tercih.al('harici-ig')) gomulu();
    else kutu.after(izinKutusu('Bu gönderiler Instagram’dan yüklenir. Instagram çerez kullanabilir.', 'Gönderileri göster', () => { tercih.koy('harici-ig'); gomulu(); }));
  }
}

function izinKutusu(metin, dugme, tamam) {
  const kutu = el('div', { sinif: 'izin' }, el('p', {}, metin),
    el('button', { sinif: 'dugme ana', type: 'button', onclick: () => { kutu.remove(); tamam(); } }, dugme));
  return kutu;
}

function facebookGoster(ayar) {
  const alan = $('#fb-alan');
  const adres = ayar.facebook?.adres;
  if (!adres) { alan.append(bosKutu('Facebook sayfası bağlanınca son paylaşımlar burada görünür.')); return; }
  const yukle = () => {
    const g = Math.min(500, alan.clientWidth || 500);
    const p = new URLSearchParams({ href: adres, tabs: 'timeline', width: g, height: 640, small_header: 'true',
      adapt_container_width: 'true', hide_cover: 'false', show_facepile: 'false' });
    alan.replaceChildren(el('iframe', { src: `https://www.facebook.com/plugins/page.php?${p}`, title: 'Facebook sayfası',
      loading: 'lazy', allow: 'encrypted-media', scrolling: 'no' }));
  };
  if (tercih.al('harici-fb')) yukle();
  else alan.append(izinKutusu('Sayfa akışı Facebook’tan yüklenir. Facebook çerez kullanabilir.', 'Facebook sayfasını göster', () => { tercih.koy('harici-fb'); yukle(); }));
}

(async () => {
  const [ayar, icerik, yt, ig] = await Promise.all(['ayarlar.json', 'icerikler.json', 'youtube.json', 'instagram.json'].map(veri));
  const a = ayar || {};
  ayarlariUygula(a);
  icerikleriGoster(icerik);
  videolariGoster(yt);
  instagramGoster(ig, a);
  facebookGoster(a);
  const son = [yt?.guncelleme, ig?.guncelleme].filter(Boolean).sort().pop();
  if (son) $('#guncelleme').textContent = `Sosyal medya akışı son güncelleme: ${tarihBicim.format(new Date(son))}`;
})();
