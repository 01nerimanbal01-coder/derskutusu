// Ortak yazılı senaryoları: yazili.html?sinif=N&ders=<kısa ad>. Veri: veri/senaryolar.json (ÖDSGM tabloları).
// Hazır sınav kâğıtları: veri/yazili-kagitlari.json (tablo → yazılı no → senaryo nolar); PDF'ler /yazili/pdf/ altında.

Promise.all([veri('senaryolar.json'), ortakVeri, veri('yazili-kagitlari.json')]).then(([sen, { dersler }, kagit]) => {
  const p = new URLSearchParams(location.search);
  const sinif = Number(p.get('sinif')), ders = p.get('ders');
  const t = sen?.tablolar[`${sinif}-${ders}`];
  const dersAd = dersler?.dersler[ders] || ders;
  if (!t) {
    // Giriş: sınıf/ders verilmediyse (ör. Öğretmen Köşesi kartı) ya da tablo yoksa bütün tablolar sınıf sınıf listelenir.
    document.title = 'Ortak yazılı senaryoları ve sınav kâğıtları · Ders Kutusu';
    $('#y-baslik').textContent = 'Ortak yazılı senaryoları ve sınav kâğıtları';
    for (const sec of ['#y-dugmeler', '#y-siniflar', '.y-secim']) { const e = $(sec); if (e) e.hidden = true; }
    const yolSinif = $('#y-yol-sinif');
    if (yolSinif) { yolSinif.textContent = 'Öğretmen Köşesi'; yolSinif.href = '/ogretmen.html'; }
    const kutu = $('#y-tablo');
    kutu.classList.remove('y-kaydir');   // tablo kabı (kenarlık, iç boşluksuz) giriş listesine uymuyor; düğmeler sayfayı yeniden yükler
    if (!sen?.tablolar) {
      kutu.replaceChildren(el('p', {}, 'Senaryo verisi yüklenemedi; sayfayı yenileyin. ', el('a', { href: '/belgeler.html#yazili' }, 'ÖDSGM tabloları')));
      return;
    }
    const bilinmeyen = p.has('sinif') || p.has('ders');
    const sira = Object.keys(dersler?.dersler || {});
    const yer = (d) => { const i = sira.indexOf(d); return i < 0 ? sira.length : i; };
    const gruplar = {};
    for (const x of Object.values(sen.tablolar)) (gruplar[x.sinif] = gruplar[x.sinif] || []).push(x);
    const dugme = (x) => {
      const anahtar = `${x.sinif}-${x.ders}`;
      const hazir = Boolean(kagit?.tablolar?.[anahtar] || kagit?.ulke?.[anahtar]);
      const ad = dersler?.dersler[x.ders] || x.dersAd || x.ders;
      return el('a', { sinif: hazir ? 'dugme ana' : 'dugme', href: `?sinif=${x.sinif}&ders=${encodeURIComponent(x.ders)}`,
        'aria-label': `${x.sinif}. sınıf ${ad}${hazir ? ': senaryo tablosu ve hazır sınav kâğıtları' : ': senaryo tablosu'}` },
        hazir ? simge('indir') : null, ad);
    };
    const bolumler = Object.keys(gruplar).map(Number).sort((a, b) => a - b).map((n) =>
      el('div', { sinif: 'y-giris-sinif', style: 'margin:22px 0' },
        el('h2', { style: 'font-size:20px;margin:0 0 10px' }, `${n}. sınıf`),
        el('div', { sinif: 'g-dugmeler' }, ...gruplar[n].sort((a, b) => yer(a.ders) - yer(b.ders)).map(dugme))));
    kutu.replaceChildren(
      ...(bilinmeyen ? [el('p', {}, 'Bu sınıf ve ders için ortak yazılı senaryosu yayımlanmamış; aşağıdan seçebilirsiniz.')] : []),
      el('p', {}, 'Sınıfınızı ve dersinizi seçin. İndirme simgesi olan derslerde her senaryonun hazır sınav kâğıdı ve cevap anahtarı (PDF) da vardır.'),
      ...bolumler,
      el('p', { style: 'margin-top:22px' }, el('a', { href: '/belgeler.html#yazili' }, 'ÖDSGM senaryo tabloları (resmî belgeler)')));
    return;
  }
  // Konum çubuğunun son basamağı ("Ortak yazılı") giriş listesine döner.
  const yolSon = $('nav.yol > span:last-child:not([aria-hidden])');
  if (yolSon) yolSon.replaceWith(el('a', { href: '/yazili.html' }, yolSon.textContent));
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
  // Ülke geneli ortak yazılı (MEB merkezî sınavı, senaryosuz): hazırlık denemeleri
  const ug = kagit?.ulke?.[`${sinif}-${ders}`];
  if (ug) {
    const yol = (n) => `${kagit.klasor}${sinif}-${ders}-${ug.yazili}-yazili-ulke-geneli-deneme-${n}`;
    $('#y-dugmeler').after(el('div', { sinif: 'g-dugmeler', id: 'y-ulke', style: 'margin:10px 0 4px;align-items:center' },
      el('span', { style: 'flex-basis:100%;font-size:14px;color:var(--soluk)' },
        `1. dönem ${ug.yazili}. ortak yazılı sınavı ${ug.tarih} tarihinde MEB tarafından ülke genelinde ortak yapılır; senaryosu yoktur. Hazırlık için Ders Kutusu denemeleri:`),
      Array.from({ length: ug.denemeler }, (_, i) => [
        el('a', { sinif: 'dugme ana', href: `${yol(i + 1)}.pdf`, download: '' }, simge('indir'), `Deneme ${i + 1} (PDF)`),
        el('a', { sinif: 'dugme', href: `${yol(i + 1)}-cevapli.pdf`, download: '' }, simge('indir'), `Deneme ${i + 1} cevaplı`)]).flat()));
  }
  // Seçilen senaryonun hazır sınav kâğıdı (öğrenci + cevaplı PDF)
  const kt = kagit?.tablolar?.[`${sinif}-${ders}`];
  const kagitAlan = el('div', { sinif: 'g-dugmeler', id: 'y-kagit', 'aria-live': 'polite' });
  if (kt) $('#y-senaryolar').after(kagitAlan);
  const kagitNot = (metin) => el('span', { style: 'align-self:center;font-size:14px;color:var(--soluk)' }, metin);

  let y = 0, s = 0, hepsi = false, yalnizSoru = $('#y-yalniz').checked;   // tarayıcının geri yüklediği kutu durumu
  const toplam = (dizi) => dizi.reduce((a, b) => a + b, 0);
  const ciz = () => {
    const yz = t.yazililar[y];
    $('#y-yazililar').replaceChildren(...t.yazililar.map((x, i) => el('button', { type: 'button', sinif: 'sekme', 'aria-pressed': String(i === y), onclick: () => { y = i; s = Math.min(s, t.yazililar[i].senaryolar.length - 1); ciz(); } }, x.ad.replace(/^1\. Dönem /, ''))));
    $('#y-senaryolar').replaceChildren(
      ...yz.senaryolar.map((x, i) => el('button', { type: 'button', sinif: 'cip-dugme', 'aria-pressed': String(!hepsi && i === s), onclick: () => { s = i; hepsi = false; ciz(); } },
        `${x} · ${toplam(t.satirlar.map((r) => r.sayilar[y][i]))} soru`)),
      el('button', { type: 'button', sinif: 'cip-dugme', 'aria-pressed': String(hepsi), onclick: () => { hepsi = true; ciz(); } }, 'Bütün senaryolar'));
    if (kt) {
      const yNo = (/(\d+)\. Ortak/.exec(yz.ad) || [])[1] || String(y + 1);
      const yol = `${kagit.klasor}${sinif}-${ders}-${yNo}-yazili-senaryo-${s + 1}`;
      kagitAlan.replaceChildren(...(hepsi ? (kt[yNo] ? [kagitNot('Hazır sınav kâğıdını indirmek için bir senaryo seçin.')] : [])
        : kt[yNo]?.includes(s + 1) ? [
          el('a', { sinif: 'dugme ana', href: `${yol}.pdf`, download: '' }, simge('indir'), 'Sınav kâğıdı (PDF)'),
          el('a', { sinif: 'dugme', href: `${yol}-cevapli.pdf`, download: '' }, simge('indir'), 'Cevap anahtarı (PDF)'),
          kagitNot(`${yz.senaryolar[s]} için Ders Kutusu sınav kâğıdı: 2 sayfa, 40 dakika`)] : []));
    }
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
