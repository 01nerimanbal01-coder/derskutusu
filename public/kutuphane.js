// İçerik kütüphanesi: sinif.html (bir sınıfın dersleri) ve icerikler.html (süzgeçli liste).
// Veriler: veri/dersler.json (sınıf, ders, tür) ve veri/icerikler.json (içerikler).

const parametre = new URLSearchParams(location.search);

// Ortak içerikler (ör. çalışma kâğıtları) iki kitlede de sayılır ve listelenir.
function kitleDenetleyici(dersler) {
  const turKitle = Object.fromEntries(dersler.turler.map((t) => [t.ad, t.kitle]));
  return (i, k) => (i.kitle || 'ogrenci') === k || turKitle[i.tur] === k;
}

function icerikKarti(i, dersler) {
  const dersAd = dersler.dersler[i.ders] || i.ders;
  const adres = i.dosya || i.baglanti;
  return el('article', { sinif: 'kart', 'data-renk': window.Kesif?.category(i.tur).color || 'mavi' },
    el('div', { sinif: 'ust-bilgi' },
      i.hafta && el('span', { sinif: 'etiket' }, `${i.hafta}. hafta`),
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
    el('a', { href: `sinif.html?no=${n}`, 'data-renk': window.Kesif?.gradeColor(n) || 'mavi', 'aria-current': Number(n) === no ? 'page' : null }, `${n}. sınıf`)));
  const buSinif = icerikler.filter((i) => Number(i.sinif) === no);
  const kitleUyar = kitleDenetleyici(dersler);
  const dersKarti = (d, s) => {
    const ad = dersler.dersler[d];
    const ogrenci = buSinif.filter((i) => i.ders === d && kitleUyar(i, 'ogrenci')).length;
    const ogretmen = buSinif.filter((i) => i.ders === d && kitleUyar(i, 'ogretmen')).length;
    return el('a', { sinif: 'ders-kart', 'data-renk': window.Kesif?.subjectColor(d) || 'mavi', href: `icerikler.html?sinif=${no}&ders=${d}` },
      el('div', { sinif: 'ders-kart-ust' },
        el('span', { sinif: 'ders-harf' }, ad.replace(/^T\.C\. /, '').charAt(0)),
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
  const alan = { sinif: $('#s-sinif'), ders: $('#s-ders'), tur: $('#s-tur'), hafta: $('#s-hafta'), kitle: $('#s-kitle'), ara: $('#s-ara') };
  const sirala = $('#s-sirala');
  if (sirala && ['yeni', 'baslik', 'sinif'].includes(parametre.get('sirala'))) sirala.value = parametre.get('sirala');
  let gorunen = 12;
  const kategoriAlan = $('#kategori-secimleri');
  const kategoriler = window.Kesif?.categories || [];
  alan.sinif.append(...Object.keys(dersler.siniflar).map((n) => el('option', { value: n }, `${n}. sınıf`)));
  const haftalar = [...new Set(icerikler.map((i) => Number(i.hafta)).filter((n) => Number.isInteger(n) && n > 0))].sort((a, b) => a - b);
  alan.hafta.append(...haftalar.map((n) => el('option', { value: String(n) }, `${n}. hafta`)));
  const dersSecenekleri = () => {
    const n = alan.sinif.value;
    const kisa = n ? [...dersler.siniflar[n], ...(dersler.secmeli?.[n] || [])] : Object.keys(dersler.dersler).sort((a, b) => dersler.dersler[a].localeCompare(dersler.dersler[b], 'tr'));
    const onceki = alan.ders.value;
    alan.ders.replaceChildren(el('option', { value: '' }, 'Bütün dersler'), ...kisa.map((d) => el('option', { value: d }, dersler.dersler[d])));
    if (kisa.includes(onceki)) alan.ders.value = onceki;
  };
  const kitleUyar = kitleDenetleyici(dersler);
  const turSecenekleri = () => {
    const k = alan.kitle.value;
    const onceki = alan.tur.value;
    const turler = dersler.turler.filter((t) => !k || t.kitle === k || icerikler.some((i) => i.tur === t.ad && kitleUyar(i, k)));
    alan.tur.replaceChildren(el('option', { value: '' }, 'Bütün türler'), ...turler.map((t) => el('option', { value: t.ad }, t.ad)));
    if (turler.some((t) => t.ad === onceki)) alan.tur.value = onceki;
  };
  for (const a of ['sinif', 'kitle']) if (parametre.get(a)) alan[a].value = parametre.get(a);
  dersSecenekleri(); turSecenekleri();
  for (const a of ['ders', 'tur', 'hafta']) if (parametre.get(a)) alan[a].value = parametre.get(a);
  if (parametre.get('ara')) alan.ara.value = parametre.get('ara');

  const secimiKaldir = (ad) => {
    alan[ad].value = '';
    if (ad === 'sinif') dersSecenekleri();
    if (ad === 'kitle') turSecenekleri();
    ciz();
    alan[ad].focus();
  };
  const hepsiniTemizle = () => {
    Object.values(alan).forEach((e) => { e.value = ''; });
    dersSecenekleri(); turSecenekleri(); ciz();
    alan.sinif.focus();
  };
  const ciz = (daha = false) => {
    if (daha !== true) gorunen = 12;
    const f = Object.fromEntries(Object.entries(alan).map(([a, e]) => [a, e.value.trim()]));
    const sonuc = icerikler.filter((i) => (!f.sinif || String(i.sinif) === f.sinif) && (!f.ders || i.ders === f.ders)
      && (!f.hafta || String(i.hafta) === f.hafta) && (!f.tur || i.tur === f.tur) && (!f.kitle || kitleUyar(i, f.kitle))
      && (!f.ara || aramaEslesir(`${i.baslik} ${i.aciklama} ${dersler.dersler[i.ders] || ''} ${i.tur}`, f.ara)))
      .sort((a, b) => sirala?.value === 'baslik' ? a.baslik.localeCompare(b.baslik, 'tr')
        : sirala?.value === 'sinif' ? Number(a.sinif || 0) - Number(b.sinif || 0) || a.baslik.localeCompare(b.baslik, 'tr')
        : String(b.tarih || '').localeCompare(String(a.tarih || '')));
    const url = new URLSearchParams(Object.entries(f).filter(([, d]) => d));
    if (sirala && sirala.value !== 'yeni') url.set('sirala', sirala.value);
    history.replaceState(null, '', url.toString() ? `?${url}` : location.pathname);
    const secili = Object.values(f).some(Boolean);
    $('#sonuc-sayi').textContent = `${sonuc.length} içerik`;
    $('#temizle').hidden = !secili;
    const secimler = $('#secili-suzgecler');
    if (secimler) {
      const adlar = { sinif: 'Sınıf', ders: 'Ders', kitle: 'Kimin için', tur: 'Tür', hafta: 'Hafta', ara: 'Arama' };
      secimler.replaceChildren(...Object.entries(f).filter(([, deger]) => deger).map(([ad, deger]) => {
        const metin = ad === 'ara' ? deger : alan[ad].selectedOptions[0].textContent;
        return el('button', { type: 'button', sinif: 'secili-suzgec',
          'aria-label': `${adlar[ad]} seçimini kaldır: ${metin}`, onclick: () => secimiKaldir(ad) },
          el('span', {}, `${adlar[ad]}: ${metin}`), el('span', { 'aria-hidden': 'true' }, '×'));
      }));
      secimler.hidden = !secili;
    }
    const kartlar = $('#kartlar');
    // Uzun listelerde yüzlerce kartı aynı anda oluşturma; filtre değişince ilk sayfaya dön.
    const parcali = Boolean($('#daha-goster'));
    kartlar.replaceChildren(...(parcali ? sonuc.slice(0, gorunen) : sonuc).map((i) => icerikKarti(i, dersler)));
    if (parcali) {
      $('#daha-alani').hidden = !sonuc.length;
      $('#gosterilen-sayi').textContent = `${sonuc.length} kaynaktan ${Math.min(gorunen, sonuc.length)} tanesi gösteriliyor`;
      $('#daha-goster').hidden = gorunen >= sonuc.length;
    }
    if (kategoriAlan) {
      // Kategori sayıları, tür dışındaki seçimlerle eşleşen gerçek kayıt sayılarıdır.
      const kapsam = icerikler.filter(i => (!f.sinif || String(i.sinif) === f.sinif) && (!f.ders || i.ders === f.ders)
        && (!f.hafta || String(i.hafta) === f.hafta) && (!f.kitle || kitleUyar(i, f.kitle))
        && (!f.ara || aramaEslesir(`${i.baslik} ${i.aciklama} ${dersler.dersler[i.ders] || ''} ${i.tur}`, f.ara)));
      for (const b of kategoriAlan.querySelectorAll('button')) {
        b.setAttribute('aria-pressed', String(b.dataset.tur === f.tur));
        b.querySelector('small').textContent = kapsam.filter(i => !b.dataset.tur || i.tur === b.dataset.tur).length;
      }
    }
    $('#icerik-yakinda').hidden = sonuc.length > 0;
    if ($('#sonucsuz-baslik')) {
      $('#sonucsuz-baslik').textContent = f.ara ? 'Aramanızla eşleşen içerik bulunamadı' : 'Bu seçimde henüz içerik yok';
      $('#sonucsuz-aciklama').textContent = f.ara
        ? 'Daha kısa bir sözcükle arayın veya yalnız aramayı temizleyerek seçtiğiniz dersin içeriklerine dönün.'
        : 'Başka bir sınıf, ders, hafta veya tür seçebilir; tüm seçimleri temizleyerek içeriklere göz atabilirsiniz.';
      $('#aramayi-temizle').hidden = !f.ara;
      $('#sonucsuz-temizle').hidden = !secili;
    }
    kartlar.hidden = !sonuc.length;
  };
  alan.sinif.addEventListener('change', () => { dersSecenekleri(); ciz(); });
  alan.kitle.addEventListener('change', () => { turSecenekleri(); ciz(); });
  alan.ders.addEventListener('change', ciz);
  alan.tur.addEventListener('change', ciz);
  alan.hafta.addEventListener('change', ciz);
  alan.ara.addEventListener('input', ciz);
  $('#temizle').addEventListener('click', hepsiniTemizle);
  $('#sonucsuz-temizle')?.addEventListener('click', hepsiniTemizle);
  $('#aramayi-temizle')?.addEventListener('click', () => secimiKaldir('ara'));
  sirala?.addEventListener('change', ciz);
  $('#daha-goster')?.addEventListener('click', () => {
    const onceki = gorunen; gorunen += 12; ciz(true);
    const ilkYeni = $('#kartlar').children[onceki];
    ilkYeni?.querySelector('a')?.focus({ preventScroll: true });
    ilkYeni?.scrollIntoView({ block: 'start', behavior: 'instant' });
  });
  if (kategoriAlan) kategoriAlan.replaceChildren(...[{ type: '', title: 'Bütün kaynaklar', icon: 'kitap', color: 'yesil' }, ...kategoriler].map(k =>
    el('button', { type: 'button', 'data-tur': k.type, 'data-renk': k.color, 'aria-pressed': 'false', onclick: () => {
      // Öğrenci/öğretmen filtresi seçilen türü dışlıyorsa herkes görünümüne dön.
      if (![...alan.tur.options].some(o => o.value === k.type)) { alan.kitle.value = ''; turSecenekleri(); }
      alan.tur.value = k.type; ciz();
    } }, simge(k.icon), el('span', {}, k.title), el('small', {}, ''))));
  ciz();
}

ortakVeri.then((v) => {
  if (!v.dersler || v.iceriklerYuklendi === false) {
    const yer = $('#kartlar') || $('#ders-listesi');
    if (yer) {
      yer.hidden = false;
      yer.replaceChildren(el('div', { role: 'alert', style: 'grid-column: 1 / -1' },
        el('p', {}, 'Kaynak listesi yüklenemedi. Bağlantınızı kontrol edip yeniden deneyin.'),
        el('button', { type: 'button', sinif: 'dugme', onclick: () => location.reload() }, 'Yeniden dene')));
    }
    for (const secici of ['#s-sinif', '#s-ders', '#s-kitle', '#s-hafta', '#s-tur', '#s-ara', '#s-sirala']) {
      const alan = $(secici);
      if (alan) alan.disabled = true;
    }
    for (const secici of ['#icerik-yakinda', '#daha-alani', '#secili-suzgecler', '#temizle']) {
      const alan = $(secici);
      if (alan) alan.hidden = true;
    }
    const sayi = $('#sonuc-sayi');
    if (sayi) sayi.textContent = '';
    return;
  }
  if ($('#ders-listesi')) sinifSayfasi(v);
  if ($('#s-sinif')) icerikSayfasi(v);
});
