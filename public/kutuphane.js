// İçerik kütüphanesi: sinif.html (bir sınıfın dersleri) ve icerikler.html (süzgeçli liste).
// Veriler: veri/dersler.json (sınıf, ders, tür) ve veri/icerikler.json (içerikler).

const parametre = new URLSearchParams(location.search);
const FAV_ANAHTAR = 'dk-favoriler';
const GORUNUM_ANAHTAR = 'dk-kutuphane-gorunum';
const favoriOku = () => { try { const l = JSON.parse(localStorage.getItem(FAV_ANAHTAR) || '[]'); return new Set(Array.isArray(l) ? l : []); } catch { return new Set(); } };
const favoriYaz = (set) => { try { set.size ? localStorage.setItem(FAV_ANAHTAR, JSON.stringify([...set])) : localStorage.removeItem(FAV_ANAHTAR); } catch {} };
const kaynakAnahtari = (i) => String(i.goruntule || i.hazirla || i.dosya || i.baglanti || `${i.sinif || ''}-${i.ders || ''}-${i.tur || ''}-${i.hafta || ''}-${i.baslik || ''}`);
let favoriSet = favoriOku();
let favoriDegisti = null;

// Ortak içerikler (ör. çalışma kâğıtları) iki kitlede de sayılır ve listelenir.
function kitleDenetleyici(dersler) {
  const turKitle = Object.fromEntries(dersler.turler.map((t) => [t.ad, t.kitle]));
  return (i, k) => (i.kitle || 'ogrenci') === k || turKitle[i.tur] === k;
}

function icerikKarti(i, dersler) {
  const dersAd = dersler.dersler[i.ders] || i.ders;
  const adres = i.dosya || i.baglanti;
  // Sınıf zaten rozette: "5. Sınıf Matematik 7. Hafta: …" başlığı "Matematik 7. Hafta: …" olarak kısalır (dar ekranda kart boyu)
  const baslik = String(i.baslik || '').replace(/^\d+\.\s*Sınıf\s+(?=\S)/, '') || i.baslik;
  const anahtar = kaynakAnahtari(i);
  const kayitliMi = favoriSet.has(anahtar);
  const favDugme = el('button', {
    type: 'button',
    sinif: 'fav-dugme',
    'aria-pressed': String(kayitliMi),
    title: kayitliMi ? 'Kaydedilenlerden çıkar' : 'Daha sonra hızlı erişmek için kaydet',
    'aria-label': kayitliMi ? 'Kaydedilenlerden çıkar' : 'Kaydet',
    onclick: (o) => {
      o.stopPropagation();
      if (favoriSet.has(anahtar)) favoriSet.delete(anahtar);
      else favoriSet.add(anahtar);
      favoriYaz(favoriSet);
      const yeni = favoriSet.has(anahtar);
      favDugme.setAttribute('aria-pressed', String(yeni));
      favDugme.title = yeni ? 'Kaydedilenlerden çıkar' : 'Daha sonra hızlı erişmek için kaydet';
      favDugme.textContent = yeni ? '★ Kayıtlı' : '☆ Kaydet';
      if (typeof favoriDegisti === 'function') favoriDegisti();
    },
  }, kayitliMi ? '★ Kayıtlı' : '☆ Kaydet');

  const kartRenk = (i.ders && window.Kesif?.subjectColor(i.ders)) || window.Kesif?.category(i.tur).color || 'mavi';
  const kart = el('article', { sinif: 'kart', 'data-renk': kartRenk },
    el('div', { sinif: 'ust-bilgi' },
      i.hafta && el('span', { sinif: 'etiket' }, `${i.hafta}. hafta`),
      i.sinif && el('span', { sinif: 'etiket' }, `${i.sinif}. sınıf`),
      dersAd && el('span', { sinif: 'etiket tur' }, dersAd),
      i.tur && el('span', { sinif: `etiket ${i.kitle === 'ogretmen' ? 'ogretmen' : 'tur'}` }, i.tur),
      favDugme),
    el('h3', {}, baslik),
    i.aciklama && el('p', {}, i.aciklama),
    el('div', { sinif: 'eylemler' },
      i.goruntule && el('a', { sinif: 'ac', href: `/${i.goruntule}` }, 'Aç', simge('ok')),
      i.goruntule && i.tur === 'Ders kitabı' && el('a', { sinif: 'ac', href: `/${i.goruntule}&yerel=1`, title: 'Kitabın bilgisayarınızdaki PDF dosyasını açar; internet beklenmez' }, 'Bilgisayardan aç'),
      i.hazirla && el('a', { sinif: 'ac', href: `/${i.hazirla}` }, 'Hazırla ve indir', simge('indir')),
      !i.hazirla && adres && (i.dosya || !i.goruntule) && el('a', { sinif: 'ac', href: i.dosya ? `/${i.dosya}` : adres, target: i.dosya ? null : '_blank', rel: 'noopener', download: i.dosya ? '' : null },
        i.dosya_b ? 'A (Cevapsız)' : (i.dosya ? 'İndir' : 'Aç'), simge(i.dosya ? 'indir' : 'ok')),
      i.dosya_b && el('a', { sinif: 'ac', href: `/${i.dosya_b}`, download: '' }, 'B (Cevapsız)', simge('indir')),
      i.dosya_a_cevapli && el('a', { sinif: 'ac', href: `/${i.dosya_a_cevapli}`, download: '' }, 'A (Cevaplı)', simge('onay')),
      i.dosya_b_cevapli && el('a', { sinif: 'ac', href: `/${i.dosya_b_cevapli}`, download: '' }, 'B (Cevaplı)', simge('onay')),
      i.dosya_anahtar && el('a', { sinif: 'ac', href: `/${i.dosya_anahtar}`, download: '' }, 'Anahtar', simge('kalem'))));
  // Kartın tamamı ilk eyleme götürür (indirme bağlantısı hariç); metin seçimi ve bağlantıya tıklama bozulmaz.
  const birincil = kart.querySelector('a.ac:not([download])');
  if (birincil) {
    kart.classList.add('tiklanir');
    kart.addEventListener('click', (o) => {
      if (o.target.closest('a, button') || getSelection()?.toString()) return;
      birincil.click();
    });
  }
  return kart;
}

function sinifSayfasi({ dersler, icerikler }) {
  const no = Number(parametre.get('no'));
  const liste = dersler.siniflar[no];
  if (!liste) { location.replace('icerikler.html'); return; }
  location.replace(`/ogrenci.html?sinif=${no}`); return;   // site ağacı (11.10.2026): sınıf sayfası öğrenci dalına taşındı
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
  let yalnizFavori = parametre.get('favori') === '1';
  const kategoriAlan = $('#kategori-secimleri');
  const hizliSuzgecler = $('#hizli-suzgecler');
  const gorunumSecici = $('#gorunum-secici');
  const kategoriler = window.Kesif?.categories || [];

  // Görünüm seçici (Kart / Kompakt Liste)
  if (gorunumSecici) {
    let aktifGorunum = 'kart';
    try { if (localStorage.getItem(GORUNUM_ANAHTAR) === 'liste') aktifGorunum = 'liste'; } catch {}
    const gorunumUygula = (kip) => {
      aktifGorunum = kip;
      $('#kartlar')?.classList.toggle('liste-gorunum', kip === 'liste');
      $$('.gorunum-dugme', gorunumSecici).forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.gorunum === kip)));
      try { localStorage.setItem(GORUNUM_ANAHTAR, kip); } catch {}
    };
    gorunumSecici.addEventListener('click', (o) => {
      const b = o.target.closest('.gorunum-dugme');
      if (b) gorunumUygula(b.dataset.gorunum);
    });
    gorunumUygula(aktifGorunum);
  }
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
  // Dar ekranda süzgeçler katlanır: seçim varsa açık gelir; geniş ekrana geçince hep açık (CSS yalnız başlığı gizler)
  const acilir = $('.suzgec-acilir');
  const genis = window.matchMedia?.('(min-width: 761px)');
  if (acilir) {
    acilir.open = Boolean(genis?.matches || location.search);
    genis?.addEventListener?.('change', () => { if (genis.matches) acilir.open = true; });
  }

  const secimiKaldir = (ad) => {
    alan[ad].value = '';
    if (ad === 'sinif') dersSecenekleri();
    if (ad === 'kitle') turSecenekleri();
    ciz();
    alan[ad].focus();
  };
  const hepsiniTemizle = () => {
    Object.values(alan).forEach((e) => { e.value = ''; });
    yalnizFavori = false;
    dersSecenekleri(); turSecenekleri(); ciz();
    alan.sinif.focus();
  };
  const hizliCipGuncelle = (f) => {
    if (!hizliSuzgecler) return;
    const cipler = [
      { id: 'tumu', ad: 'Tümü', aktif: !yalnizFavori && !f.sinif && !f.tur && !f.kitle, yap: () => { yalnizFavori = false; alan.sinif.value = ''; alan.kitle.value = ''; dersSecenekleri(); turSecenekleri(); alan.tur.value = ''; ciz(); } },
      { id: 'favori', ad: `★ Kaydedilenler (${favoriSet.size})`, aktif: yalnizFavori, yap: () => { yalnizFavori = !yalnizFavori; ciz(); } },
      { id: 'lgs', ad: '8. Sınıf · LGS', aktif: !yalnizFavori && f.sinif === '8' && !f.tur, yap: () => { yalnizFavori = false; alan.sinif.value = '8'; dersSecenekleri(); alan.tur.value = ''; ciz(); } },
      { id: 'yks', ad: '12. Sınıf · YKS', aktif: !yalnizFavori && f.sinif === '12' && !f.tur, yap: () => { yalnizFavori = false; alan.sinif.value = '12'; dersSecenekleri(); alan.tur.value = ''; ciz(); } },
      { id: 'ozet', ad: 'Konu Anlatımları', aktif: !yalnizFavori && f.tur === 'Konu anlatımı', yap: () => { yalnizFavori = false; alan.kitle.value = ''; turSecenekleri(); alan.tur.value = 'Konu anlatımı'; ciz(); } },
      { id: 'calisma', ad: 'Çalışma Kâğıtları PDF', aktif: !yalnizFavori && f.tur === 'Çalışma kâğıdı', yap: () => { yalnizFavori = false; alan.kitle.value = ''; turSecenekleri(); alan.tur.value = 'Çalışma kâğıdı'; ciz(); } },
      { id: 'plan', ad: 'Yıllık Planlar', aktif: !yalnizFavori && f.tur === 'Yıllık plan', yap: () => { yalnizFavori = false; alan.kitle.value = ''; turSecenekleri(); alan.tur.value = 'Yıllık plan'; ciz(); } },
      { id: 'kitap', ad: 'Ders Kitapları', aktif: !yalnizFavori && f.tur === 'Ders kitabı', yap: () => { yalnizFavori = false; alan.kitle.value = ''; turSecenekleri(); alan.tur.value = 'Ders kitabı'; ciz(); } },
    ];
    hizliSuzgecler.replaceChildren(...cipler.map((c) => el('button', {
      type: 'button',
      sinif: `hizli-cip${c.id === 'favori' ? ' favori-cip' : ''}`,
      'aria-pressed': String(c.aktif),
      onclick: c.yap,
    }, c.ad)));
  };
  favoriDegisti = () => {
    const f = Object.fromEntries(Object.entries(alan).map(([a, e]) => [a, e.value.trim()]));
    hizliCipGuncelle(f);
    if (yalnizFavori) ciz();
  };
  const ciz = (daha = false) => {
    if (daha !== true) gorunen = 12;
    const f = Object.fromEntries(Object.entries(alan).map(([a, e]) => [a, e.value.trim()]));
    hizliCipGuncelle(f);
    const sonuc = icerikler.filter((i) => (!yalnizFavori || favoriSet.has(kaynakAnahtari(i)))
      && (!f.sinif || String(i.sinif) === f.sinif) && (!f.ders || i.ders === f.ders)
      && (!f.hafta || String(i.hafta) === f.hafta) && (!f.tur || i.tur === f.tur) && (!f.kitle || kitleUyar(i, f.kitle))
      && (!f.ara || aramaEslesir(`${i.baslik} ${i.aciklama} ${dersler.dersler[i.ders] || ''} ${i.tur}`, f.ara)))
      .sort((a, b) => sirala?.value === 'baslik' ? a.baslik.localeCompare(b.baslik, 'tr')
        : sirala?.value === 'sinif' ? Number(a.sinif || 0) - Number(b.sinif || 0) || a.baslik.localeCompare(b.baslik, 'tr')
        : String(b.tarih || '').localeCompare(String(a.tarih || '')));
    const url = new URLSearchParams(Object.entries(f).filter(([, d]) => d));
    if (yalnizFavori) url.set('favori', '1');
    if (sirala && sirala.value !== 'yeni') url.set('sirala', sirala.value);
    history.replaceState(null, '', url.toString() ? `?${url}` : location.pathname);
    const secili = Object.values(f).some(Boolean) || yalnizFavori;
    $('#sonuc-sayi').textContent = `${sonuc.length} içerik`;
    $('#temizle').hidden = !secili;
    const suzgecSayi = $('#suzgec-sayi');
    if (suzgecSayi) {
      const n = Object.values(f).filter(Boolean).length;
      suzgecSayi.textContent = n ? `${n} seçili` : '';
      suzgecSayi.hidden = !n;
    }
    const secimler = $('#secili-suzgecler');
    if (secimler) {
      const adlar = { sinif: 'Sınıf', ders: 'Ders', kitle: 'Kimin için', tur: 'Tür', hafta: 'Hafta', ara: 'Arama' };
      secimler.replaceChildren(...Object.entries(f).filter(([, deger]) => deger).map(([ad, deger]) => {
        const metin = ad === 'ara' ? deger : alan[ad].selectedOptions[0].textContent;
        return el('button', { type: 'button', sinif: 'secili-suzgec',
          'aria-label': `${adlar[ad]}: ${metin}, seçimi kaldır`, onclick: () => secimiKaldir(ad) },
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
