/* Renkli ana sayfanın vitrini, okul haftası ve sayaçları. Ortak betikten sonra yüklenir. */
(() => {
  'use strict';

  if (typeof ortakVeri === 'undefined' || typeof veri !== 'function') return;

  const liste = document.querySelector('[data-yeni-icerikler]');
  const haftaRozeti = document.querySelector('[data-okul-haftasi]');
  const kisaTarih = new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long' });
  const sayiBicim = new Intl.NumberFormat('tr-TR');
  const tarihMetni = (deger) => {
    const iso = typeof deger === 'string' ? deger.slice(0, 10) : '';
    return /^\d{4}-\d{2}-\d{2}$/.test(iso) && Number.isFinite(Date.parse(iso)) ? iso : '';
  };
  const gun = (iso) => new Date(`${iso}T12:00:00`);
  const sayaciYaz = (secici, deger) => {
    const yer = document.querySelector(secici);
    if (yer && Number.isSafeInteger(deger) && deger >= 0) yer.textContent = sayiBicim.format(deger);
  };
  const icerikYolu = (adres) => {
    if (typeof adres !== 'string') return '';
    const yol = adres.startsWith('/') ? adres : `/${adres}`;
    return /^\/(?:ozet|calisma)\/[a-z0-9-]+\.html$/.test(yol) ? yol : '';
  };
  const okulHaftasi = haftaRozeti ? veri('agac/8-matematik.json') : null;
  const yaziliVerisi = liste || document.querySelector('[data-son-ekleme]') ? veri('yazili-kagitlari.json') : null;

  if (document.querySelector('[data-pdf-indirme-sayi]')) {
    veri('indirmeler.json').then((indirmeler) => sayaciYaz('[data-pdf-indirme-sayi]', indirmeler?.toplam));
  }

  // Ziyaret ve görüntüleme sayaçlarını ortak.js doldurur.
  if (document.querySelector('[data-goruntuleme]:not([data-goruntuleme-sayi])')) {
    veri('ziyaret.json').then((ziyaret) => sayaciYaz('[data-goruntuleme]:not([data-goruntuleme-sayi])', ziyaret?.goruntuleme));
  }

  const dersGorselleri = new Map();
  for (const kutu of document.querySelectorAll('.ders-kutu')) {
    const ders = new URL(kutu.href).searchParams.get('ders');
    if (ders) dersGorselleri.set(ders, {
      gorsel: kutu.querySelector('img')?.getAttribute('src'),
      renk: kutu.style.getPropertyValue('--r'),
    });
  }
  const varsayilanGorsel = document.querySelector('.alt-marka img')?.getAttribute('src');

  const ok = () => {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 20 20');
    const yol = document.createElementNS(svg.namespaceURI, 'path');
    yol.setAttribute('d', 'M4 10h11M11 5l5 5-5 5');
    yol.setAttribute('stroke', 'currentColor');
    yol.setAttribute('stroke-width', '2.6');
    yol.setAttribute('stroke-linecap', 'round');
    yol.setAttribute('stroke-linejoin', 'round');
    yol.setAttribute('fill', 'none');
    svg.append(yol);
    return svg;
  };

  const kart = (icerik, dersler) => {
    const dersAdi = dersler?.dersler?.[icerik.ders] || icerik.ders;
    const { gorsel, renk } = dersGorselleri.get(icerik.ders) || {};
    const baslik = icerik.baslik.replace(/^\d+\.\s*Sınıf\s+.*?\d+\.\s*Hafta(?:\s+Çalışma Kâğıdı)?\s*:\s*/i, '');
    const resim = gorsel || varsayilanGorsel;
    return el('li', {}, el('a', { sinif: 'kart', href: icerik.adres, style: `--r:${renk || '#4338CA'}` },
      el('span', { sinif: 'kart-ust' },
        el('span', { sinif: 'tur' }, icerik.tur),
        resim && el('img', { src: resim, alt: '', width: 64, height: 64 })),
      el('div', { sinif: 'kart-govde' },
        el('span', { sinif: 'ders-cip' }, `${dersAdi} · ${icerik.sinif}. sınıf`),
        el('h3', {}, baslik),
        el('span', { sinif: 'kart-alt' },
          el('span', {}, icerik.hafta ? `${icerik.hafta}. hafta · ` : null,
            el('time', { datetime: icerik.tarih }, kisaTarih.format(gun(icerik.tarih)))),
          el('span', { sinif: 'git', 'aria-hidden': 'true' }, ok())))));
  };

  const tarihSirasi = (a, b) => b.tarih.localeCompare(a.tarih);
  const yaziliKartlari = (veriDosyasi) => {
    const tarih = tarihMetni(veriDosyasi?.guncelleme);
    if (!tarih || !yayinda({ tarih })) return [];
    return Object.entries(veriDosyasi.tablolar || {}).flatMap(([anahtar, tablo]) => {
      const eslesme = /^([5-9]|1[0-2])-([a-z-]+)$/.exec(anahtar);
      if (!eslesme || !Object.values(tablo || {}).some((senaryolar) => Array.isArray(senaryolar) && senaryolar.length)) return [];
      const [, sinif, ders] = eslesme;
      const parametreler = new URLSearchParams({ sinif, ders });
      return [{ adres: `/yazili.html?${parametreler}`, sinif, ders, tarih,
        tur: 'Ortak yazılı', baslik: 'Ortak yazılı sınav kâğıtları' }];
    }).slice(0, 2);
  };

  Promise.all([ortakVeri, okulHaftasi, yaziliVerisi]).then(([{ dersler, icerikler, iceriklerYuklendi }, takvim, yazili]) => {
    if (!iceriklerYuklendi) return;

    const yayindakiler = icerikler.filter(yayinda);
    const ozetler = yayindakiler.filter((icerik) => icerik.tur === 'Konu anlatımı' && icerikYolu(icerik.goruntule));
    sayaciYaz('[data-icerik-sayi]', ozetler.length);

    const hafta = takvim?.haftalar && haftaBul(takvim.haftalar);
    if (haftaRozeti && hafta && ['hafta', 'haftasonu'].includes(hafta.durum) && ozetler.some((icerik) => Number(icerik.hafta) === hafta.no)) {
      haftaRozeti.textContent = `${hafta.no}. hafta yayında`;
    }

    const yaziliKartlariGuncel = yaziliKartlari(yazili);
    const sonEkleme = [tarihMetni(yazili?.guncelleme), ...yayindakiler.map((icerik) => tarihMetni(icerik.tarih))]
      .filter((tarih) => tarih && yayinda({ tarih })).sort().at(-1);
    const sonEklemeYeri = document.querySelector('[data-son-ekleme]');
    if (sonEklemeYeri && sonEkleme) sonEklemeYeri.replaceChildren('Son ekleme: ',
      el('time', { datetime: sonEkleme }, tarihBicim.format(gun(sonEkleme))));
    if (!liste) return;

    const vitrindekiKayitlar = (kayitlar) => kayitlar.flatMap((icerik) => {
      const adres = icerikYolu(icerik.goruntule);
      const tarih = tarihMetni(icerik.tarih);
      return adres && tarih && icerik.baslik && icerik.ders && icerik.sinif ? [{ ...icerik, adres, tarih }] : [];
    }).sort(tarihSirasi);
    const konuKartlari = vitrindekiKayitlar(ozetler).slice(0, 6);
    const calismaKartlari = vitrindekiKayitlar(yayindakiler.filter((icerik) => icerik.tur === 'Çalışma kâğıdı'));
    const secilenler = [...konuKartlari, ...yaziliKartlariGuncel,
      ...calismaKartlari.slice(0, 8 - konuKartlari.length - yaziliKartlariGuncel.length)].sort(tarihSirasi);
    if (secilenler.length) liste.replaceChildren(...secilenler.map((icerik) => kart(icerik, dersler)));
  });
})();
