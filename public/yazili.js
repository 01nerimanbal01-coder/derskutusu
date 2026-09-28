// Ortak yazılı senaryoları: yazili.html?sinif=N&ders=<kısa ad>. Veri: veri/senaryolar.json (ÖDSGM tabloları).

Promise.all([veri('senaryolar.json'), ortakVeri]).then(([sen, { dersler }]) => {
  const p = new URLSearchParams(location.search);
  const sinif = Number(p.get('sinif')), ders = p.get('ders');
  const t = sen?.tablolar[`${sinif}-${ders}`];
  const dersAd = dersler?.dersler[ders] || ders;
  if (!t) {
    $('#y-baslik').textContent = 'Senaryo bulunamadı';
    $('#y-tablo').replaceChildren(el('p', {}, 'Bu sınıf ve ders için ortak yazılı senaryosu yayımlanmamış. ', el('a', { href: '/belgeler.html#yazili' }, 'Bütün tablolar')));
    return;
  }
  document.title = `${sinif}. sınıf ${dersAd} ortak yazılı senaryoları · Ders Kutusu`;
  $('#y-yol-sinif').textContent = `${sinif}. sınıf`;
  $('#y-yol-sinif').href = `/sinif.html?no=${sinif}`;
  $('#y-baslik').textContent = `${sinif}. sınıf ${dersAd}: ortak yazılı senaryoları`;
  $('#y-dugmeler').replaceChildren(
    el('a', { sinif: 'dugme', href: `/${t.dosya}`, download: '' }, simge('indir'), 'Excel'),
    el('a', { sinif: 'dugme', href: sen.kaynak, target: '_blank', rel: 'noopener' }, 'ÖDSGM', simge('ok')));
  // Aynı dersin öteki sınıfları
  const siniflar = Object.values(sen.tablolar).filter((x) => x.ders === ders).map((x) => x.sinif).sort((a, b) => a - b);
  $('#y-siniflar').replaceChildren(...siniflar.map((n) => el('a', { href: `?sinif=${n}&ders=${ders}`, 'aria-current': n === sinif ? 'page' : null }, `${n}. sınıf`)));

  let y = 0, s = 0, hepsi = false, yalnizSoru = true;
  const toplam = (dizi) => dizi.reduce((a, b) => a + b, 0);
  const ciz = () => {
    const yz = t.yazililar[y];
    $('#y-yazililar').replaceChildren(...t.yazililar.map((x, i) => el('button', { type: 'button', sinif: 'sekme', 'aria-pressed': String(i === y), onclick: () => { y = i; s = Math.min(s, t.yazililar[i].senaryolar.length - 1); ciz(); } }, x.ad.replace(/^1\. Dönem /, ''))));
    $('#y-senaryolar').replaceChildren(
      ...yz.senaryolar.map((x, i) => el('button', { type: 'button', sinif: 'cip-dugme', 'aria-pressed': String(!hepsi && i === s), onclick: () => { s = i; hepsi = false; ciz(); } },
        `${x} · ${toplam(t.satirlar.map((r) => r.sayilar[y][i]))} soru`)),
      el('button', { type: 'button', sinif: 'cip-dugme', 'aria-pressed': String(hepsi), onclick: () => { hepsi = true; ciz(); } }, 'Bütün senaryolar'));
    const satirlar = t.satirlar.filter((r) => !yalnizSoru || (hepsi ? toplam(r.sayilar[y]) : r.sayilar[y][s]) > 0);
    const son = t.basliklar.length - 1;
    let onceki = [];
    const govde = satirlar.map((r) => {
      const hucreler = r.alanlar.map((a, k) => {
        const tekrar = k < son && onceki.slice(0, k + 1).join('|') === r.alanlar.slice(0, k + 1).join('|');
        return el('td', { sinif: k === son ? 'y-cikti' : 'y-grup' }, tekrar ? '' : a);
      });
      onceki = r.alanlar;
      const sayilar = hepsi ? r.sayilar[y].map((n) => el('td', { sinif: `y-sayi${n ? '' : ' sifir'}` }, n || '–'))
        : [el('td', { sinif: `y-sayi${r.sayilar[y][s] ? '' : ' sifir'}` }, r.sayilar[y][s] || '–')];
      return el('tr', {}, ...hucreler, ...sayilar);
    });
    const topSatir = el('tr', { sinif: 'y-toplam' }, el('td', { colspan: t.basliklar.length }, 'Toplam soru'),
      ...(hepsi ? yz.senaryolar.map((_, i) => el('td', { sinif: 'y-sayi' }, toplam(t.satirlar.map((r) => r.sayilar[y][i]))))
        : [el('td', { sinif: 'y-sayi' }, toplam(t.satirlar.map((r) => r.sayilar[y][s])))]));
    $('#y-tablo').replaceChildren(el('table', { sinif: 'y-tablo' },
      el('thead', {}, el('tr', {}, ...t.basliklar.map((b) => el('th', {}, b)), ...(hepsi ? yz.senaryolar.map((x) => el('th', { sinif: 'y-sayi' }, x.replace('Senaryo ', 'S'))) : [el('th', { sinif: 'y-sayi' }, 'Soru')]))),
      el('tbody', {}, ...govde, topSatir)));
  };
  $('#y-yalniz').addEventListener('change', (o) => { yalnizSoru = o.target.checked; ciz(); });
  ciz();
});
