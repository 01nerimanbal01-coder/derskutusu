// Ana sayfa: sınıf kartları, öğretmen köşesi sayıları ve sosyal medya akışları.
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
  const blok = $('#ig-blok');
  const kutu = $('#ig-listesi');
  if (!blok || !kutu) return;
  const profil = ayar?.instagram?.adres || 'https://www.instagram.com/derskutusuinfo/';
  const liste = (v?.gonderiler || []).filter(() => v.kaynak !== 'ornek');

  blok.hidden = false;

  // Üst profil çağrı kartı ve 6 seri vitrini
  if (!$('.ig-vitrin-ust', blok)) {
    const seriler = [
      { etiket: '5–8. SINIF SERİSİ', baslik: 'Ortaokul & LGS Görsel Bilgi Kartları', aciklama: 'Türkçe, Matematik, Fen, Sosyal, İnkılap, İngilizce ve Din Kültürü haftalık özet kartları.', renk: 'mavi', sayi: '420+ Kart' },
      { etiket: '9–12. SINIF SERİSİ', baslik: 'Lise & YKS Konu Özeti Serileri', aciklama: 'Edebiyat, Matematik, Fizik, Kimya, Biyoloji, Tarih, Coğrafya ve Felsefe ders kartları.', renk: 'mor', sayi: '300+ Kart' },
      { etiket: 'YAZILI PROVALARI', baslik: 'MEB Ortak Yazılı Sınav Hazırlık Serisi', aciklama: '1. ve 2. dönem açık uçlu senaryo soruları, çözüm adımları ve puanlama ipuçları.', renk: 'kirmizi', sayi: '52 Seri' },
      { etiket: 'DENEME SINAVLARI', baslik: 'ASDS 5, 6, 7 ve 8. Sınıf Deneme Duyuruları', aciklama: 'Yeni yüklenen A/B kitapçıkları, cevap anahtarları ve haftalık deneme takvimi.', renk: 'yesil', sayi: '32 Sınav' },
      { etiket: 'HİKÂYE & REELS', baslik: 'Günlük Tek Soru – Tek Çözüm Kuşağı', aciklama: 'Hikâyelerde her gün etkileşimli mini testler, kavram yanılgıları ve sınav tüyoları.', renk: 'turuncu', sayi: 'Her Gün' },
      { etiket: 'ÖĞRETMEN KÖŞESİ', baslik: 'Yıllık & Günlük Plan ve Zümre Paylaşımları', aciklama: 'Haftalık ders planları, çalışma kâğıtları ve yeni eklenen eğitim araçları bildirimleri.', renk: 'turkuaz', sayi: '21 Branş' },
    ];
    const ustKart = el('div', { sinif: 'ig-vitrin-ust' },
      el('div', { sinif: 'ig-vitrin-kimlik' },
        el('div', { sinif: 'ig-vitrin-avatar' }, simge('instagram')),
        el('div', { sinif: 'ig-vitrin-metin' },
          el('div', { sinif: 'ig-vitrin-baslik-satir' },
            el('strong', {}, '@derskutusuinfo'),
            el('span', { sinif: 'ig-onay-tik' }, '✓ Resmî Hesap')),
          el('p', {}, '750+ Görsel Konu Özeti Kartı · Ortak Yazılı Sınav Serileri · ASDS Deneme Duyuruları · LGS & YKS Hap Bilgiler'))),
      el('div', { sinif: 'ig-vitrin-eylemler' },
        el('a', { sinif: 'dk-ig-takip-btn ig-vitrin-btn', href: profil, target: '_blank', rel: 'noopener' },
          simge('instagram'),
          el('span', {}, '@derskutusuinfo Hesabını Takip Et →'))));
    const seriIzgara = el('div', { sinif: 'gonderiler ig-seri-izgara' },
      ...seriler.map((s) =>
        el('a', { sinif: 'ig-seri-kart', 'data-renk': s.renk, href: profil, target: '_blank', rel: 'noopener' },
          el('div', { sinif: 'ig-seri-ust' },
            el('span', { sinif: 'ig-seri-etiket' }, s.etiket),
            el('span', { sinif: 'ig-seri-sayi' }, s.sayi)),
          el('strong', { sinif: 'ig-seri-baslik' }, s.baslik),
          el('p', { sinif: 'ig-seri-aciklama' }, s.aciklama),
          el('span', { sinif: 'ig-seri-alt' }, '📸 @derskutusuinfo’da İncele ve Takip Et →'))));
    const baslikEl = $('.akis-baslik', blok);
    if (baslikEl) {
      baslikEl.after(ustKart, seriIzgara);
    } else {
      blok.prepend(ustKart, seriIzgara);
    }
  }

  if (!liste.length) return;

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

(async () => {
  const [{ ayar, dersler, icerikler }, yt, ig] = await Promise.all([ortakVeri, veri('youtube.json'), veri('instagram.json')]);
  siniflariGoster(dersler, icerikler);
  turSayilari(icerikler);
  videolariGoster(yt);
  instagramGoster(ig, ayar);
  // Tarih yalnız sayfada gösterilen bir akış varsa yazılır (boş akışın eski tarihi "güncel değil" izlenimi verir)
  const son = [yt?.videolar?.length && yt.guncelleme, ig?.gonderiler?.length && ig.guncelleme].filter(Boolean).sort().pop();
  if (son) $('#guncelleme').textContent = `Sosyal medya akışı son güncelleme: ${tarihBicim.format(new Date(son))}`;
})();
