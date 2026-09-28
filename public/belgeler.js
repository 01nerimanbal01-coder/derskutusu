// Resmî belgeler sayfası: veri/belgeler.json gruplarını listeler (bağlantılar resmî kaynaklara gider).

function belgeKarti(b, dersler) {
  const dersAd = b.ders && dersler?.dersler[b.ders];
  return el('article', { sinif: 'kart' },
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
      b.dosya && el('a', { sinif: 'ac', href: `/${b.dosya}`, download: '' }, 'İndir', simge('indir')),
      !b.goruntule && !b.dosya && el('a', { sinif: 'ac', href: b.baglanti, target: '_blank', rel: 'noopener' }, 'Aç', simge('ok'))));
}

Promise.all([veri('belgeler.json'), ortakVeri]).then(([belgeler, { dersler }]) => {
  if (!belgeler) return;
  $('#grup-gecis').replaceChildren(...belgeler.gruplar.map((g) => el('a', { href: `#${g.kimlik}` }, g.ad)));
  $('#belge-gruplari').replaceChildren(...belgeler.gruplar.map((g, s) =>
    el('section', { sinif: `bolum${s % 2 ? ' koyu-zemin' : ''}`, id: g.kimlik },
      el('div', { sinif: 'kap' },
        el('div', { sinif: 'bolum-bas' },
          el('div', {}, el('p', { sinif: 'ust-baslik' }, `${g.belgeler.length} belge`), el('h2', {}, g.ad), g.aciklama && el('p', {}, g.aciklama))),
        el('div', { sinif: 'kartlar' }, g.belgeler.map((b) => belgeKarti(b, dersler)))))));
  if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();
});
