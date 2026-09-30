// İçerik kütüphanesi: sinif.html (bir sınıfın dersleri) ve icerikler.html (süzgeçli liste).
// Veriler: veri/dersler.json (sınıf, ders, tür) ve veri/icerikler.json (içerikler).

const RENKLER = ['#2451d6', '#12a150', '#e0662b', '#8b3fd6', '#0e8fa8', '#c2366b', '#b86e00', '#3a5a8c', '#1f9d8b', '#d6453d', '#5b6ee1'];
const parametre = new URLSearchParams(location.search);

function icerikKarti(i, dersler) {
  const dersAd = dersler.dersler[i.ders] || i.ders;
  const adres = i.dosya || i.baglanti;
  return el('article', { sinif: 'kart' },
    el('div', { sinif: 'ust-bilgi' },
      i.sinif && el('span', { sinif: 'etiket' }, `${i.sinif}. sınıf`),
      dersAd && el('span', { sinif: 'etiket tur' }, dersAd),
      i.tur && el('span', { sinif: `etiket ${i.kitle === 'ogretmen' ? 'ogretmen' : 'tur'}` }, i.tur)),
    el('h3', {}, i.baslik),
    i.aciklama && el('p', {}, i.aciklama),
    el('div', { sinif: 'eylemler' },
      i.goruntule && el('a', { sinif: 'ac', href: `/${i.goruntule}` }, 'Aç', simge('ok')),
      i.hazirla && el('a', { sinif: 'ac', href: `/${i.hazirla}` }, 'Hazırla ve indir', simge('indir')),
      !i.hazirla && adres && (i.dosya || !i.goruntule) && el('a', { sinif: 'ac', href: i.dosya ? `/${i.dosya}` : adres, target: i.dosya ? null : '_blank', rel: 'noopener', download: i.dosya ? '' : null },
        i.dosya ? 'İndir' : 'Aç', simge(i.dosya ? 'indir' : 'ok'))));
}

function sinifSayfasi({ dersler, icerikler }) {
  const no = Number(parametre.get('no'));
  const liste = dersler.siniflar[no];
  if (!liste) { location.replace('icerikler.html'); return; }
  const kademe = dersler.kademeler.find((k) => k.siniflar.includes(no))?.ad || '';
  document.title = `${no}. sınıf · Ders Kutusu`;
  $('#baslik').textContent = `${no}. sınıf`;
  $('#yol-sinif').textContent = `${no}. sınıf`;
  $('#aciklama').textContent = `${kademe} ${no}. sınıf: ${liste.length} ders için konu anlatımları, soru çözümleri, videolar ve öğretmen dosyaları.`;
  $('#sinif-gecis').replaceChildren(...Object.keys(dersler.siniflar).map((n) =>
    el('a', { href: `sinif.html?no=${n}`, 'aria-current': Number(n) === no ? 'page' : null }, `${n}. sınıf`)));
  const buSinif = icerikler.filter((i) => Number(i.sinif) === no);
  const dersKarti = (d, s) => {
    const ad = dersler.dersler[d];
    const ogrenci = buSinif.filter((i) => i.ders === d && i.kitle !== 'ogretmen').length;
    const ogretmen = buSinif.filter((i) => i.ders === d && i.kitle === 'ogretmen').length;
    return el('a', { sinif: 'ders-kart', href: `icerikler.html?sinif=${no}&ders=${d}` },
      el('div', { sinif: 'ders-kart-ust' },
        el('span', { sinif: 'ders-harf', style: `background:${RENKLER[s % RENKLER.length]}` }, ad.replace(/^T\.C\. /, '').charAt(0)),
        el('h3', {}, ad)),
      el('div', { sinif: 'sayilar' },
        el('span', {}, ogrenci ? `${ogrenci} öğrenci içeriği` : 'Öğrenci içerikleri yakında'),
        el('span', { sinif: 'ogretmen' }, ogretmen ? `${ogretmen} öğretmen dosyası` : 'Öğretmen dosyaları yakında')));
  };
  $('#ders-listesi').replaceChildren(...liste.map(dersKarti));
  const secmeli = dersler.secmeli?.[no] || [];
  if (secmeli.length && $('#secmeli-listesi')) {
    $('#secmeli-listesi').replaceChildren(...secmeli.map((d, s) => dersKarti(d, s + liste.length)));
    $('#secmeli-bolum').hidden = false;
  }
  $('#tum-icerik').href = `icerikler.html?sinif=${no}`;
  const hizli = $('#ogretmen-hizli');   // öğretmen kısayolları: bu sınıfın günlük ve yıllık planları
  if (hizli) {
    hizli.replaceChildren(el('span', {}, 'Öğretmen:'),
      el('a', { href: `/planlar.html?sinif=${no}` }, simge('takvim'), 'Günlük planlar', el('small', {}, 'Word · PDF · aylık')),
      el('a', { href: `/icerikler.html?sinif=${no}&kitle=ogretmen&tur=${encodeURIComponent('Yıllık plan')}` }, simge('kitap'), 'Yıllık planlar'));
    hizli.hidden = false;
  }
}

// Akıllı arama yüklüyse yazım hatasına dayanıklı eşleşme, değilse düz içerme.
const aramaEslesir = (metin, q) => (typeof Arama !== 'undefined' ? Arama.metinEslesir(metin, q) : metin.toLocaleLowerCase('tr').includes(q.toLocaleLowerCase('tr')));

function icerikSayfasi({ dersler, icerikler }) {
  const alan = { sinif: $('#s-sinif'), ders: $('#s-ders'), tur: $('#s-tur'), kitle: $('#s-kitle'), ara: $('#s-ara') };
  alan.sinif.append(...Object.keys(dersler.siniflar).map((n) => el('option', { value: n }, `${n}. sınıf`)));
  const dersSecenekleri = () => {
    const n = alan.sinif.value;
    const kisa = n ? [...dersler.siniflar[n], ...(dersler.secmeli?.[n] || [])] : Object.keys(dersler.dersler).sort((a, b) => dersler.dersler[a].localeCompare(dersler.dersler[b], 'tr'));
    const onceki = alan.ders.value;
    alan.ders.replaceChildren(el('option', { value: '' }, 'Bütün dersler'), ...kisa.map((d) => el('option', { value: d }, dersler.dersler[d])));
    if (kisa.includes(onceki)) alan.ders.value = onceki;
  };
  // İçerik hem kendi kitlesinde hem türünün kitlesinde görünür (çalışma kâğıdı öğrenciye de öğretmene de).
  const turKitle = Object.fromEntries(dersler.turler.map((t) => [t.ad, t.kitle]));
  const kitleUyar = (i, k) => (i.kitle || 'ogrenci') === k || turKitle[i.tur] === k;
  const turSecenekleri = () => {
    const k = alan.kitle.value;
    const onceki = alan.tur.value;
    const turler = dersler.turler.filter((t) => !k || t.kitle === k || icerikler.some((i) => i.tur === t.ad && kitleUyar(i, k)));
    alan.tur.replaceChildren(el('option', { value: '' }, 'Bütün türler'), ...turler.map((t) => el('option', { value: t.ad }, t.ad)));
    if (turler.some((t) => t.ad === onceki)) alan.tur.value = onceki;
  };
  for (const a of ['sinif', 'kitle']) if (parametre.get(a)) alan[a].value = parametre.get(a);
  dersSecenekleri(); turSecenekleri();
  for (const a of ['ders', 'tur']) if (parametre.get(a)) alan[a].value = parametre.get(a);
  if (parametre.get('ara')) alan.ara.value = parametre.get('ara');

  const kucuk = (s) => (s || '').toLocaleLowerCase('tr');
  const ciz = () => {
    const f = Object.fromEntries(Object.entries(alan).map(([a, e]) => [a, e.value.trim()]));
    const sonuc = icerikler.filter((i) => (!f.sinif || String(i.sinif) === f.sinif) && (!f.ders || i.ders === f.ders)
      && (!f.tur || i.tur === f.tur) && (!f.kitle || kitleUyar(i, f.kitle))
      && (!f.ara || aramaEslesir(`${i.baslik} ${i.aciklama} ${dersler.dersler[i.ders] || ''} ${i.tur}`, f.ara)))
      .sort((a, b) => String(b.tarih || '').localeCompare(String(a.tarih || '')));
    const url = new URLSearchParams(Object.entries(f).filter(([, d]) => d));
    history.replaceState(null, '', url.toString() ? `?${url}` : location.pathname);
    const secili = Object.values(f).some(Boolean);
    $('#sonuc-sayi').textContent = `${sonuc.length} içerik`;
    $('#temizle').hidden = !secili;
    const kartlar = $('#kartlar');
    kartlar.replaceChildren(...sonuc.map((i) => icerikKarti(i, dersler)));
    $('#icerik-yakinda').hidden = sonuc.length > 0;
    kartlar.hidden = !sonuc.length;
  };
  alan.sinif.addEventListener('change', () => { dersSecenekleri(); ciz(); });
  alan.kitle.addEventListener('change', () => { turSecenekleri(); ciz(); });
  alan.ders.addEventListener('change', ciz);
  alan.tur.addEventListener('change', ciz);
  alan.ara.addEventListener('input', ciz);
  $('#temizle').addEventListener('click', () => { Object.values(alan).forEach((e) => { e.value = ''; }); dersSecenekleri(); turSecenekleri(); ciz(); });
  ciz();
}

ortakVeri.then((v) => {
  if (!v.dersler) return;
  if ($('#ders-listesi')) sinifSayfasi(v);
  if ($('#s-sinif')) icerikSayfasi(v);
});
