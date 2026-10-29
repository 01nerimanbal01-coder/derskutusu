// Resmî belgeler sayfası: veri/belgeler.json gruplarını listeler (bağlantılar resmî kaynaklara gider).

const normalBelge = (s) => String(s || '').toLocaleLowerCase('tr-TR')
  .replace(/ı/g, 'i').replace(/ğ/g, 'g').replace(/ü/g, 'u').replace(/ş/g, 's').replace(/ö/g, 'o').replace(/ç/g, 'c')
  .replace(/[âîû]/g, (h) => ({ â: 'a', î: 'i', û: 'u' }[h]));

function belgeKarti(b, dersler, grupAd) {
  const dersAd = b.ders && dersler?.dersler[b.ders];
  return el('article', {
    sinif: 'kart belge-kart',
    'data-arama': normalBelge(`${b.baslik || ''} ${b.aciklama || ''} ${dersAd || ''} ${b.kaynak || ''} ${grupAd || ''}`),
    'data-kitle': b.kitle || 'ortak',
    'data-sinif': b.sinif ? String(b.sinif) : '',
    'data-kademe': normalBelge(b.kademe || ''),
  },
  el('div', { sinif: 'ust-bilgi' },
    el('span', { sinif: 'etiket' }, b.kaynak),
    b.kademe && el('span', { sinif: 'etiket tur' }, b.kademe),
    b.sinif && el('span', { sinif: 'etiket tur' }, `${b.sinif}. sınıf`),
    el('span', { sinif: `etiket ${b.kitle === 'ogretmen' ? 'ogretmen' : 'tur'}` }, b.kitle === 'ogretmen' ? 'Öğretmen' : 'Öğrenci ve veli')),
  el('h3', {}, b.baslik),
  b.aciklama && el('p', {}, b.aciklama),
  dersAd && !b.baslik.startsWith(dersAd) && el('p', { sinif: 'kucuk' }, dersAd),
  el('div', { sinif: 'eylemler' },
    b.goruntule && el('a', { sinif: 'ac', href: `/${b.goruntule}` }, 'Aç', simge('ok')),
    b.goruntule && /^kitap-/.test(b.kimlik || '') && !b.dosya && el('a', { sinif: 'ac', href: `/${b.goruntule}&yerel=1`, title: 'Kitabın bilgisayarınızdaki PDF dosyasını açar; internet beklenmez' }, 'Bilgisayardan aç'),
    b.dosya && el('a', { sinif: 'ac', href: `/${b.dosya}`, download: '' }, 'İndir', simge('indir')),
    !b.goruntule && !b.dosya && el('a', { sinif: 'ac', href: b.baglanti, target: '_blank', rel: 'noopener' }, 'Aç', simge('ok'))));
}

Promise.all([veri('belgeler.json'), ortakVeri]).then(([belgeler, { dersler }]) => {
  if (!belgeler) return;
  const grupGecis = $('#grup-gecis');
  const belgeGruplari = $('#belge-gruplari');
  grupGecis.replaceChildren(...belgeler.gruplar.map((g) => el('a', { href: `#${g.kimlik}` }, `${g.ad} (${g.belgeler.length})`)));

  const toplamSayi = belgeler.gruplar.reduce((t, g) => t + g.belgeler.length, 0);
  const bolumler = belgeler.gruplar.map((g, s) =>
    el('section', { sinif: `bolum${s % 2 ? ' koyu-zemin' : ''}`, id: g.kimlik },
      el('div', { sinif: 'kap' },
        el('div', { sinif: 'bolum-bas' },
          el('div', {}, el('p', { sinif: 'ust-baslik belge-grup-sayi' }, `${g.belgeler.length} belge`), el('h2', {}, g.ad), g.aciklama && el('p', {}, g.aciklama))),
        el('div', { sinif: 'kartlar' }, g.belgeler.map((b) => belgeKarti(b, dersler, g.ad))))));

  let aktifKitle = 'tumu';
  let aktifSinif = 'tumu';
  const aramaGirdi = el('input', {
    type: 'search',
    sinif: 'belge-ara-girdi',
    placeholder: 'Belge, ders kitabı, öğretim programı veya branş ara…',
    'aria-label': 'Resmî belgelerde ara',
    autocomplete: 'off',
  });
  const sonucSayac = el('span', { sinif: 'belge-sonuc-sayac' }, `${toplamSayi} resmî belge`);
  const bosMesaj = el('div', { sinif: 'kap', hidden: true },
    el('p', { sinif: 'agac-suzgec-bos' }, 'Seçtiğiniz arama ve süzgeçlerle eşleşen resmî belge bulunamadı.'));

  const suzgecUygula = () => {
    const sorgu = normalBelge(aramaGirdi.value.trim());
    let gorunenToplam = 0;
    bolumler.forEach((sec, idx) => {
      const kartList = $$('.belge-kart', sec);
      let grupGorunen = 0;
      kartList.forEach((k) => {
        const aramaUygun = !sorgu || String(k.dataset.arama || '').includes(sorgu);
        const kitleUygun = aktifKitle === 'tumu'
          || (aktifKitle === 'ogretmen' && k.dataset.kitle === 'ogretmen')
          || (aktifKitle === 'ogrenci' && k.dataset.kitle !== 'ogretmen');
        const sinifUygun = aktifSinif === 'tumu'
          || (aktifSinif === 'ortaokul' && (['5', '6', '7', '8'].includes(k.dataset.sinif) || k.dataset.kademe.includes('ortaokul')))
          || (aktifSinif === 'lise' && (['9', '10', '11', '12'].includes(k.dataset.sinif) || k.dataset.kademe.includes('lise')))
          || k.dataset.sinif === aktifSinif;
        const goster = aramaUygun && kitleUygun && sinifUygun;
        k.hidden = !goster;
        if (goster) grupGorunen++;
      });
      sec.hidden = grupGorunen === 0;
      const sayiEtiket = $('.belge-grup-sayi', sec);
      if (sayiEtiket) sayiEtiket.textContent = `${grupGorunen} belge`;
      gorunenToplam += grupGorunen;
      const gecisBag = grupGecis.children[idx];
      if (gecisBag) gecisBag.hidden = grupGorunen === 0;
    });
    sonucSayac.textContent = gorunenToplam === toplamSayi ? `${toplamSayi} resmî belge` : `${gorunenToplam} / ${toplamSayi} belge gösteriliyor`;
    bosMesaj.hidden = gorunenToplam > 0;
  };

  const kitleDugme = (kod, ad) => el('button', {
    type: 'button',
    sinif: 'agac-suzgec-dugme belge-kitle-dugme',
    'aria-pressed': String(kod === aktifKitle),
    onclick: (o) => {
      aktifKitle = kod;
      $$('.belge-kitle-dugme', suzgecBolum).forEach((b) => b.setAttribute('aria-pressed', String(b === o.currentTarget)));
      suzgecUygula();
    },
  }, ad);

  const sinifDugme = (kod, ad) => el('button', {
    type: 'button',
    sinif: 'agac-suzgec-dugme belge-sinif-dugme',
    'aria-pressed': String(kod === aktifSinif),
    onclick: (o) => {
      aktifSinif = kod;
      $$('.belge-sinif-dugme', suzgecBolum).forEach((b) => b.setAttribute('aria-pressed', String(b === o.currentTarget)));
      suzgecUygula();
    },
  }, ad);

  aramaGirdi.addEventListener('input', suzgecUygula);

  const suzgecBolum = el('section', { sinif: 'bolum belge-suzgec-bolum' },
    el('div', { sinif: 'kap' },
      el('div', { sinif: 'agac-suzgec-cubuk belge-suzgec-cubuk' },
        el('div', { sinif: 'agac-suzgec-arama' }, simge('mercek'), aramaGirdi),
        el('div', { sinif: 'agac-suzgec-cipler', role: 'group', 'aria-label': 'Hedef kitle süzgeci' },
          kitleDugme('tumu', 'Tümü'),
          kitleDugme('ogrenci', 'Öğrenci ve Veli'),
          kitleDugme('ogretmen', 'Öğretmen')),
        sonucSayac),
      el('div', { sinif: 'agac-suzgec-cipler belge-sinif-cipler', role: 'group', 'aria-label': 'Sınıf ve kademe süzgeci' },
        sinifDugme('tumu', 'Tüm Sınıflar'),
        sinifDugme('ortaokul', 'Ortaokul (5–8)'),
        sinifDugme('lise', 'Lise (9–12)'),
        ...['5', '6', '7', '8', '9', '10', '11', '12'].map((s) => sinifDugme(s, `${s}. Sınıf`)))));

  belgeGruplari.replaceChildren(suzgecBolum, ...bolumler, bosMesaj);
  if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();
});
