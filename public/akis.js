// Ana sayfa: sınıf kartları, öğretmen köşesi sayıları, son eklenen içerikler ve sosyal medya akışları.
// youtube.json ve instagram.json her gün araclar/akis_guncelle.py ile yenilenir (GitHub Actions).
// Dışarıdan (YouTube, Instagram, Facebook) hiçbir şey ziyaretçi tıklamadan yüklenmez.

const tarih = (t) => (t ? el('time', { datetime: t }, tarihBicim.format(new Date(t))) : null);
const bosKutu = (metin) => el('div', { sinif: 'bos' }, metin);

function siniflariGoster(dersler, icerikler) {
  const alan = $('#sinif-listesi');
  if (!dersler || !alan) return;
  $$('[data-sayi="ders"]').forEach((e) => { e.textContent = Object.keys(dersler.dersler).length; });
  alan.replaceChildren(...dersler.kademeler.map((k) => el('div', { sinif: 'kademe' },
    el('h3', { sinif: 'kademe-ad' }, k.ad),
    el('div', { sinif: 'sinif-izgara' }, k.siniflar.map((n) => {
      const dersSay = new Set([...(dersler.siniflar[n] || []), ...(dersler.secmeli?.[n] || [])]).size;
      const icerikSay = icerikler.filter((i) => Number(i.sinif) === n).length;
      return el('a', { sinif: 'sinif-kart', 'data-renk': window.Kesif?.gradeColor(n) || 'mavi', href: `sinif.html?no=${n}` },
        el('span', { sinif: 'sinif-no' }, String(n)),
        el('span', { sinif: 'sinif-ad' }, `${n}. sınıf`),
        el('span', { sinif: 'sinif-bilgi' }, `${dersSay} ders${icerikSay ? ` · ${icerikSay} içerik` : ''}`),
        simge('ok', 'sinif-ok'));
    })))));
}

function turSayilari(icerikler) {
  $$('[data-tur-sayi]').forEach((e) => {
    const n = icerikler.filter((i) => i.tur === e.dataset.turSayi).length;
    e.textContent = n ? `${n} dosya` : 'Yakında';
    e.classList.toggle('yakinda-etiket', !n);
  });
}

function sonEklenenler(icerikler, dersler) {
  const kartlar = $('#kartlar');
  const liste = [...icerikler].sort((a, b) => String(b.tarih || '').localeCompare(String(a.tarih || ''))).slice(0, 6);
  if (!liste.length) { kartlar.hidden = true; $('#icerik-yakinda').hidden = false; return; }
  kartlar.replaceChildren(...liste.map((i) => icerikKarti(i, dersler)));
}

function icerikKarti(i, dersler) {
  const dersAd = dersler?.dersler?.[i.ders] || i.ders;
  const adres = i.dosya || i.baglanti;
  return el('article', { sinif: 'kart', 'data-renk': window.Kesif?.category(i.tur).color || 'mavi' },
    el('div', { sinif: 'ust-bilgi' },
      i.sinif && el('span', { sinif: 'etiket' }, `${i.sinif}. sınıf`),
      dersAd && el('span', { sinif: 'etiket tur' }, dersAd),
      i.tur && el('span', { sinif: `etiket ${i.kitle === 'ogretmen' ? 'ogretmen' : 'tur'}` }, i.tur)),
    el('h3', {}, i.baslik),
    i.aciklama && el('p', {}, i.aciklama),
    i.hazirla ? el('a', { sinif: 'ac', href: `/${i.hazirla}` }, 'Hazırla ve indir', simge('ok'))
      : i.goruntule ? el('a', { sinif: 'ac', href: `/${i.goruntule}` }, 'Aç', simge('ok'))
      : adres && el('a', { sinif: 'ac', href: adres, target: i.dosya ? null : '_blank', rel: 'noopener', download: i.dosya ? '' : null },
        i.dosya ? 'İndir' : 'Aç', simge('ok')));
}

function videolariGoster(v) {
  const liste = v?.videolar || [];
  if (!liste.length || v.kaynak === 'ornek') return;
  $('#video-blok').hidden = false;
  $('#video-listesi').replaceChildren(...liste.map((i) => {
    const kapak = el('button', {
      sinif: 'kapak', type: 'button', 'aria-label': `${i.baslik} videosunu oynat`,
      onclick: () => {
        kapak.replaceWith(el('iframe', {
          src: `https://www.youtube-nocookie.com/embed/${encodeURIComponent(i.id)}?autoplay=1&rel=0`,
          title: i.baslik, allow: 'autoplay; encrypted-media; picture-in-picture', allowfullscreen: true, loading: 'lazy',
        }));
      },
    }, el('img', { src: i.gorsel, alt: '', loading: 'lazy' }), el('span', { sinif: 'oynat' }),
    i.kisa && el('span', { sinif: 'kisa-etiket' }, 'Kısa'));
    return el('article', { sinif: 'video' }, kapak, el('h4', {}, i.baslik), tarih(i.tarih));
  }));
}

function instagramGoster(v, ayar) {
  const liste = (v?.gonderiler || []).filter(() => v.kaynak !== 'ornek');
  if (!liste.length) return;
  $('#ig-blok').hidden = false;
  const kutu = $('#ig-listesi');
  const profil = ayar.instagram?.adres || null;
  // Görseli olan gönderi yerel görselle gösterilir; yalnız bağlantısı olan (elle eklenen) gönderi
  // Instagram'ın resmî gömme koduyla, ziyaretçi izin verince yüklenir.
  const gorselli = liste.filter((i) => i.gorsel);
  const elle = liste.filter((i) => !i.gorsel && i.baglanti);
  kutu.replaceChildren(...gorselli.map((i) =>
    el('a', { sinif: 'gonderi', href: i.baglanti || profil || '#sosyal', target: '_blank', rel: 'noopener' },
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
  const adres = ayar.facebook?.adres;
  if (!adres) return;
  $('#fb-blok').hidden = false;
  const alan = $('#fb-alan');
  const yukle = () => {
    const g = Math.min(500, alan.clientWidth || 500);
    const p = new URLSearchParams({ href: adres, tabs: 'timeline', width: g, height: 600, small_header: 'true',
      adapt_container_width: 'true', hide_cover: 'false', show_facepile: 'false' });
    alan.replaceChildren(el('iframe', { src: `https://www.facebook.com/plugins/page.php?${p}`, title: 'Facebook sayfası',
      loading: 'lazy', allow: 'encrypted-media', scrolling: 'no' }));
  };
  if (tercih.al('harici-fb')) yukle();
  else alan.append(izinKutusu('Sayfa paylaşımları Facebook’tan yüklenir. Facebook çerez kullanabilir.', 'Facebook paylaşımlarını göster', () => { tercih.koy('harici-fb'); yukle(); }));
}

(async () => {
  const [{ ayar, dersler, icerikler }, yt, ig] = await Promise.all([ortakVeri, veri('youtube.json'), veri('instagram.json')]);
  siniflariGoster(dersler, icerikler);
  turSayilari(icerikler);
  sonEklenenler(icerikler, dersler);
  videolariGoster(yt);
  instagramGoster(ig, ayar);
  facebookGoster(ayar);
  const son = [yt?.guncelleme, ig?.guncelleme].filter(Boolean).sort().pop();
  if (son) $('#guncelleme').textContent = `Sosyal medya akışı son güncelleme: ${tarihBicim.format(new Date(son))}`;
})();
