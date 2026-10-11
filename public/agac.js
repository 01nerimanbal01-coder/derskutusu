// Öğrenci / öğretmen ağacı (kullanıcı 11.10.2026): ogrenci.html ve ogretmen.html.
// Öğrenci: sınıf → ders → ünite → konu (yıllık plandan; veri/agac/<sinif>-<ders>.json) → içerik türleri.
// Öğretmen: kategori → sınıf → derslere göre dosyalar. Her dal yalnız kendi kitlesinin içeriğini gösterir.
// Veriler sitenin kendi JSON'larından; dışarıdan hiçbir şey yüklenmez.
(() => {
  'use strict';
  const alan = document.getElementById('agac');
  if (!alan) return;
  const KITLE = document.body.dataset.kitle === 'ogretmen' ? 'ogretmen' : 'ogrenci';
  const P = new URLSearchParams(location.search);
  const K = () => window.Kesif || { category: () => ({ color: 'mavi', icon: 'kitap' }), subjectColor: () => 'mavi', gradeColor: () => 'mavi' };
  const yol = (a) => (/^(https?:)?\//.test(a) ? a : `/${a}`);
  const adres = (o) => `${location.pathname}?${new URLSearchParams(Object.entries(o).filter(([, v]) => v !== '' && v != null))}`;
  const sayiYaz = (n, ad) => `${n} ${ad}`;
  const ilkHarf = (ad) => String(ad).replace(/^T\.C\.\s*/, '').charAt(0);

  // Konum çubuğu ve başlık
  const konum = (...parca) => el('nav', { sinif: 'yol', 'aria-label': 'Konum' },
    parca.flatMap((p, i) => [i ? el('span', { 'aria-hidden': 'true' }, '/') : null,
      p.href && i < parca.length - 1 ? el('a', { href: p.href }, p.ad) : el('span', { 'aria-current': i === parca.length - 1 ? 'page' : null }, p.ad)]));
  const KOK_YOL = { ad: 'Ana sayfa', href: '/' };
  const DAL_YOL = KITLE === 'ogrenci' ? { ad: 'Öğrenci', href: '/ogrenci.html' } : { ad: 'Öğretmen Köşesi', href: '/ogretmen.html' };
  const bolum = (sinif, ...ic) => el('section', { sinif: `agac-bolum ${sinif || ''}` }, el('div', { sinif: 'kap' }, ...ic));
  const basBolum = (yolParca, ust, baslik, aciklama, ...ek) => el('section', { sinif: 'agac-bas' }, el('div', { sinif: 'kap' },
    konum(KOK_YOL, ...yolParca), ust ? el('p', { sinif: 'agac-ust' }, ust) : null, el('h1', {}, baslik), aciklama ? el('p', { sinif: 'agac-aciklama' }, aciklama) : null, ...ek));
  const baslikSatiri = (baslik, alt, sag) => el('div', { sinif: 'agac-bolum-bas' }, el('div', {}, el('h2', {}, baslik), alt ? el('p', {}, alt) : null), sag || null);
  const bos = (baslik, metin, ...eylem) => el('div', { sinif: 'agac-bos', role: 'status' }, el('span', { sinif: 'agac-bos-simge', 'aria-hidden': 'true' }, simge('kitap')),
    el('div', {}, el('h3', {}, baslik), el('p', {}, metin), eylem.length ? el('div', { sinif: 'agac-bos-eylem' }, ...eylem) : null));

  // İçerik kartı: kütüphanedeki kartla aynı eylemler (Aç, Hazırla ve indir, İndir)
  const kart = (i, dersler, { dersGoster = true } = {}) => {
    const kat = K().category(i.tur);
    const dersAd = dersler?.dersler?.[i.ders] || i.ders;
    return el('article', { sinif: 'agac-kart', 'data-renk': kat.color || 'mavi' },
      el('div', { sinif: 'agac-kart-ust' },
        el('span', { sinif: 'agac-kart-simge', 'aria-hidden': 'true' }, simge(kat.icon || 'kitap')),
        el('span', { sinif: 'agac-etiket' }, i.tur),
        i.hafta ? el('span', { sinif: 'agac-etiket soluk' }, `${i.hafta}. hafta`) : null,
        dersGoster && i.sinif ? el('span', { sinif: 'agac-etiket soluk' }, `${i.sinif}. sınıf${dersAd ? ' · ' + dersAd : ''}`) : null),
      el('h3', {}, i.baslik),
      i.aciklama ? el('p', {}, i.aciklama) : null,
      el('div', { sinif: 'agac-kart-eylem' },
        i.goruntule ? el('a', { sinif: 'dugme ana', href: yol(i.goruntule) }, 'Aç', simge('ok')) : null,
        i.hazirla ? el('a', { sinif: 'dugme ana', href: yol(i.hazirla) }, 'Hazırla ve indir', simge('indir')) : null,
        !i.hazirla && i.dosya ? el('a', { sinif: 'dugme', href: yol(i.dosya), download: '' }, /\.pdf$/i.test(i.dosya) ? 'PDF indir' : 'İndir', simge('indir')) : null,
        !i.hazirla && !i.dosya && !i.goruntule && i.baglanti ? el('a', { sinif: 'dugme ana', href: i.baglanti, target: '_blank', rel: 'noopener' }, 'Aç', simge('ok')) : null));
  };
  const kartlar = (liste, dersler, secenek) => el('div', { sinif: 'agac-kartlar' }, liste.map((i) => kart(i, dersler, secenek)));
  const yeniler = (liste) => [...liste].sort((a, b) => String(b.tarih || '').localeCompare(String(a.tarih || '')));

  // Kitle süzgeci: çalışma kâğıdı iki dalda da (dersler.json "turler" eşlemesi)
  const kitleUyar = (dersler) => {
    const turKitle = Object.fromEntries((dersler?.turler || []).map((t) => [t.ad, t.kitle]));
    return (i) => (i.kitle || 'ogrenci') === KITLE || turKitle[i.tur] === KITLE;
  };

  // Bu haftanın numarası (planın hafta başlangıç tarihlerinden)
  const buHafta = (haftalar) => {
    const bugun = new Date().toISOString().slice(0, 10);
    let no = null;
    for (const [n, h] of Object.entries(haftalar || {})) if (h.bas && h.bas <= bugun && (no == null || Number(n) > no)) no = Number(n);
    return no;
  };
  const haftaMetni = (h) => {
    if (!h?.length) return '';
    const s = [...h].sort((a, b) => a - b);
    const ardisik = s.every((n, i) => !i || n === s[i - 1] + 1);
    return s.length === 1 ? `${s[0]}. hafta` : ardisik ? `${s[0]}–${s[s.length - 1]}. hafta` : `${s.join(', ')}. hafta`;
  };
  const tarihMetni = (h, haftalar) => {
    if (!h?.length || !haftalar) return '';
    const s = [...h].sort((a, b) => a - b);
    const ilk = haftalar[s[0]]?.ad || '', son = haftalar[s[s.length - 1]]?.ad || '';
    if (s.length === 1) return ilk;
    const [a, b = ''] = ilk.split('-').map((x) => x.trim());
    const bas = /[^\d\s]/.test(a) ? a : `${a} ${b.split(' ').slice(1).join(' ')}`.trim();   // "5-9 Ekim" → "5 Ekim"
    return `${bas} – ${son.split('-').pop().trim()}`;
  };

  // İçeriği konuya bağla: aynı haftayı içeren konulardan başlıkla en çok sözcük paylaşan
  const sozcuk = (s) => new Set(String(s).toLocaleLowerCase('tr').replace(/[^a-zçğıöşü0-9 ]+/g, ' ').split(/\s+/).filter((x) => x.length > 2));
  const konuyaBagla = (agac, icerikler) => {
    const konular = agac.uniteler.flatMap((u, ui) => u.konular.map((k) => ({ ...k, unite: u.ad, ui, icerik: [] })));
    const disarida = [];
    for (const i of icerikler) {
      const aday = konular.filter((k) => i.hafta && k.haftalar.includes(Number(i.hafta)));
      if (!aday.length) { disarida.push(i); continue; }
      const w = sozcuk(i.baslik);
      aday.sort((a, b) => [...sozcuk(b.ad)].filter((x) => w.has(x)).length - [...sozcuk(a.ad)].filter((x) => w.has(x)).length);
      aday[0].icerik.push(i);
    }
    return { konular, disarida };
  };

  const sinifKarti = (n, href, alt, dersler) => el('a', { sinif: 'agac-sinif', href, 'data-renk': K().gradeColor(n) },
    el('span', { sinif: 'agac-sinif-no' }, String(n)), el('span', { sinif: 'agac-sinif-ad' }, '. Sınıf'),
    alt ? el('small', {}, alt) : null, el('span', { sinif: 'agac-git', 'aria-hidden': 'true' }, '→'));
  const sinifIzgarasi = (dersler, hrefYap, altYap, suz = () => true) => dersler.kademeler.map((kd) => {
    const s = kd.siniflar.filter(suz);
    return s.length ? el('div', { sinif: 'agac-kademe' }, el('h2', {}, kd.ad),
      el('div', { sinif: 'agac-siniflar' }, s.map((n) => sinifKarti(n, hrefYap(n), altYap(n), dersler)))) : null;
  });
  const sinifGecis = (dersler, secili, hrefYap, suz = () => true) => el('nav', { sinif: 'agac-gecis', 'aria-label': 'Sınıflar' },
    Object.keys(dersler.siniflar).filter((n) => suz(Number(n))).map((n) => el('a', { href: hrefYap(n), 'data-renk': K().gradeColor(n), 'aria-current': Number(n) === secili ? 'page' : null }, `${n}. sınıf`)));

  // ---------------------------------------------------------------- ÖĞRENCİ
  const ARACLAR_OGRENCI = [
    { ad: 'İngilizce kelime çalışması', alt: '5 ve 6. sınıf · kart, dinleme, test', href: '/kelime.html', simge: 'ses', renk: 'lacivert' },
    { ad: 'Arapça harf ve kelime', alt: 'Harfler, harekeler, kartlar', href: '/arapca.html', simge: 'kalem', renk: 'turkuaz' },
    { ad: 'Sınavlar: LGS ve YKS', alt: 'Oturumlar, kılavuzlar, kaynaklar', href: '/sinav.html', simge: 'onay', renk: 'pembe' },
    { ad: 'Öğrenci kütüphanesi', alt: 'Bütün öğrenci içeriklerinde ara', href: '/icerikler.html?kitle=ogrenci', simge: 'mercek', renk: 'mor' },
  ];
  const aracKarti = (a) => el('a', { sinif: 'agac-arac', href: a.href, 'data-renk': a.renk },
    el('span', { sinif: 'agac-arac-simge', 'aria-hidden': 'true' }, simge(a.simge)), el('span', {}, el('strong', {}, a.ad), el('small', {}, a.alt)));

  function ogrenciKok({ dersler, icerikler }, dizin) {
    const ogr = icerikler.filter(kitleUyar(dersler));
    const arama = el('form', { sinif: 'agac-arama', action: '/ara.html', role: 'search' },
      el('label', { sinif: 'gizli', for: 'agac-q' }, 'Konu ara'), el('input', { id: 'agac-q', name: 'q', type: 'search', placeholder: 'Konu, ders ya da hafta ara…', autocomplete: 'off' }),
      el('button', { sinif: 'dugme ana', type: 'submit' }, simge('mercek'), 'Ara'));
    alan.replaceChildren(
      basBolum([{ ad: 'Öğrenci' }], 'Öğrenci', 'Merhaba! Hangi sınıftasın?', 'Sınıfını seç; derslerine, ünitelere ve haftanın konu anlatımlarına ulaş.', arama),
      bolum('', ...sinifIzgarasi(dersler, (n) => adres({ sinif: n }), (n) => {
        const d = [...dersler.siniflar[n], ...(dersler.secmeli?.[n] || [])];
        const c = ogr.filter((i) => Number(i.sinif) === n).length;
        return `${d.length} ders · ${c ? sayiYaz(c, 'içerik') : 'içerikler hazırlanıyor'}`;
      })),
      bolum('koyu-zemin', baslikSatiri('Öğrenci araçları', 'Tekrar et, dinle, sınava hazırlan.'), el('div', { sinif: 'agac-araclar' }, ARACLAR_OGRENCI.map(aracKarti))),
      bolum('', baslikSatiri('Öğrencilere son eklenenler', null, el('a', { sinif: 'tumu', href: '/icerikler.html?kitle=ogrenci' }, 'Tümünü gör', simge('ok'))),
        kartlar(yeniler(ogr).slice(0, 6), dersler)));
  }

  function ogrenciSinif({ dersler, icerikler }, dizin, n) {
    const ogr = icerikler.filter(kitleUyar(dersler)).filter((i) => Number(i.sinif) === n);
    document.title = `${n}. Sınıf Dersleri · Öğrenci · Ders Kutusu`;
    const dersKarti = (d) => {
      const ad = dersler.dersler[d] || d;
      const ag = dizin?.[`${n}-${d}`];
      const ic = ogr.filter((i) => i.ders === d);
      const say = (t) => ic.filter((i) => i.tur === t).length;
      const ozet = [say('Konu anlatımı') && sayiYaz(say('Konu anlatımı'), 'konu anlatımı'), say('Çalışma kâğıdı') && sayiYaz(say('Çalışma kâğıdı'), 'çalışma kâğıdı'), say('Ders kitabı') && 'ders kitabı'].filter(Boolean);
      return el('a', { sinif: 'agac-ders', href: adres({ sinif: n, ders: d }), 'data-renk': K().subjectColor(d) },
        el('span', { sinif: 'agac-ders-harf', 'aria-hidden': 'true' }, ilkHarf(ad)),
        el('span', { sinif: 'agac-ders-govde' }, el('strong', {}, ad),
          el('small', {}, ag ? `${ag.unite} ünite · ${ag.konu} konu` : 'Konular hazırlanıyor'),
          el('span', { sinif: 'agac-ders-icerik' }, ozet.length ? ozet.join(' · ') : 'İçerikler hazırlanıyor')),
        el('span', { sinif: 'agac-basla' }, 'Başla', el('span', { 'aria-hidden': 'true' }, ' →')));
    };
    const secmeli = dersler.secmeli?.[n] || [];
    alan.replaceChildren(
      basBolum([DAL_YOL, { ad: `${n}. sınıf` }], 'Öğrenci', `${n}. Sınıf Dersleri`, 'Dersini seç: üniteler ve konular yıllık plana göre sıralı.',
        sinifGecis(dersler, n, (s) => adres({ sinif: s }))),
      bolum('', el('div', { sinif: 'agac-dersler' }, dersler.siniflar[n].map(dersKarti))),
      secmeli.length ? bolum('koyu-zemin', baslikSatiri('Seçmeli dersler'), el('div', { sinif: 'agac-dersler' }, secmeli.map(dersKarti))) : null,
      ogr.length ? bolum('', baslikSatiri(`${n}. sınıfa son eklenenler`, null, el('a', { sinif: 'tumu', href: `/icerikler.html?kitle=ogrenci&sinif=${n}` }, 'Tümünü gör', simge('ok'))),
        kartlar(yeniler(ogr).slice(0, 6), dersler, { dersGoster: true })) : null);
  }

  async function ogrenciDers({ dersler, icerikler }, n, d) {
    const ad = dersler.dersler[d] || d;
    const renk = K().subjectColor(d);
    const agac = await veri(`agac/${n}-${d}.json`);
    const ogr = icerikler.filter(kitleUyar(dersler)).filter((i) => Number(i.sinif) === n && i.ders === d);
    const haftalik = ogr.filter((i) => i.hafta);
    const dersDuzeyi = ogr.filter((i) => !i.hafta);
    const konuKodu = P.get('konu');
    const dersYol = { ad, href: adres({ sinif: n, ders: d }) };
    const sinifYol = { ad: `${n}. sınıf`, href: adres({ sinif: n }) };
    if (!agac) {   // yıllık planı olmayan ders: içerikler haftaya göre
      document.title = `${n}. Sınıf ${ad} · Öğrenci · Ders Kutusu`;
      alan.replaceChildren(basBolum([DAL_YOL, sinifYol, { ad }], `${n}. Sınıf`, ad, null),
        bolum('', ogr.length ? kartlar(yeniler(ogr), dersler, { dersGoster: false }) : bos('İçerikler hazırlanıyor', 'Bu dersin konu anlatımları eklendikçe burada listelenecek.', el('a', { sinif: 'dugme', href: adres({ sinif: n }) }, `${n}. sınıf derslerine dön`))));
      return;
    }
    const { konular, disarida } = konuyaBagla(agac, haftalik);
    const simdi = buHafta(agac.haftalar);
    if (konuKodu) return ogrenciKonu({ dersler }, n, d, ad, renk, agac, konular, konuKodu, dersYol, sinifYol, dersDuzeyi, simdi);
    document.title = `${n}. Sınıf ${ad}: Üniteler ve Konular · Ders Kutusu`;
    const icerikSay = konular.reduce((t, k) => t + k.icerik.length, 0) + disarida.length;
    const kaynaklar = dersDuzeyi.map((i) => el('a', { sinif: 'agac-kaynak', href: yol(i.goruntule || i.dosya || i.baglanti || '#'), 'data-renk': K().category(i.tur).color },
      simge(K().category(i.tur).icon || 'kitap'), el('span', {}, el('strong', {}, i.tur), el('small', {}, i.baslik))));
    const buKonu = konular.find((k) => simdi && k.haftalar.includes(simdi));
    const konuSatiri = (k) => {
      const turler = [...new Set(k.icerik.map((i) => i.tur))];
      const ayni = k.ad === k.unite;
      return el('li', {}, el('a', { sinif: `agac-konu${k.icerik.length ? ' dolu' : ''}`, href: adres({ sinif: n, ders: d, konu: k.kod }) },
        el('span', { sinif: 'agac-konu-isaret', 'aria-hidden': 'true' }, k.icerik.length ? '✓' : ''),
        el('span', { sinif: 'agac-konu-govde' }, el('strong', {}, ayni ? 'Ünitenin konuları' : k.ad),
          el('small', {}, [haftaMetni(k.haftalar), tarihMetni(k.haftalar, agac.haftalar)].filter(Boolean).join(' · '))),
        el('span', { sinif: 'agac-konu-turler' },
          buKonu === k ? el('span', { sinif: 'agac-rozet bu-hafta' }, 'Bu hafta') : null,
          turler.length ? turler.map((t) => el('span', { sinif: 'agac-rozet', 'data-renk': K().category(t).color }, t)) : el('span', { sinif: 'agac-rozet soluk' }, 'Yakında')),
        el('span', { sinif: 'agac-ok', 'aria-hidden': 'true' }, '›')));
    };
    const uniteler = agac.uniteler.map((u, ui) => {
      const ks = konular.filter((k) => k.ui === ui);
      const dolu = ks.reduce((t, k) => t + k.icerik.length, 0);
      const acik = (buKonu && buKonu.ui === ui) || (!buKonu && ui === 0);
      return el('details', { sinif: 'agac-unite', open: acik || null, 'data-renk': renk },
        el('summary', {}, el('span', { sinif: 'agac-unite-no' }, String(ui + 1)),
          el('span', { sinif: 'agac-unite-govde' }, el('strong', {}, u.ad), el('small', {}, [`${ks.length} konu`, dolu ? sayiYaz(dolu, 'içerik') : null].filter(Boolean).join(' · '))),
          el('span', { sinif: 'agac-unite-ok', 'aria-hidden': 'true' }, '›')),
        el('ol', { sinif: 'agac-konular' }, ks.map(konuSatiri)));
    });
    alan.replaceChildren(
      el('section', { sinif: 'agac-bas agac-ders-bas', 'data-renk': renk }, el('div', { sinif: 'kap' },
        konum(KOK_YOL, DAL_YOL, sinifYol, { ad }),
        el('div', { sinif: 'agac-ders-kart' },
          el('span', { sinif: 'agac-ders-harf buyuk', 'aria-hidden': 'true' }, ilkHarf(ad)),
          el('div', {}, el('p', { sinif: 'agac-ust' }, `${n}. Sınıf`), el('h1', {}, ad),
            el('div', { sinif: 'agac-cipler' }, el('span', {}, `${agac.uniteler.length} ünite`), el('span', {}, `${konular.length} konu`), el('span', {}, icerikSay ? sayiYaz(icerikSay, 'içerik') : 'İçerikler hazırlanıyor')))),
        buKonu ? el('a', { sinif: 'agac-bu-hafta', href: adres({ sinif: n, ders: d, konu: buKonu.kod }) },
          el('span', { sinif: 'agac-rozet bu-hafta' }, `Bu hafta · ${simdi}. hafta`), el('strong', {}, buKonu.ad === buKonu.unite ? buKonu.unite : buKonu.ad), el('span', { 'aria-hidden': 'true' }, '→')) : null)),
      kaynaklar.length ? bolum('agac-ince', el('div', { sinif: 'agac-kaynaklar' }, kaynaklar)) : null,
      bolum('', baslikSatiri('Üniteler ve konular', 'Konuya dokun; konu anlatımı, etkinlikler ve çalışma kâğıdı açılır.'), el('div', { sinif: 'agac-uniteler' }, uniteler)),
      disarida.length ? bolum('koyu-zemin', baslikSatiri('Diğer içerikler'), kartlar(disarida, dersler, { dersGoster: false })) : null);
  }

  function ogrenciKonu({ dersler }, n, d, ad, renk, agac, konular, kod, dersYol, sinifYol, dersDuzeyi, simdi) {
    const ix = konular.findIndex((k) => k.kod === kod);
    if (ix < 0) { location.replace(adres({ sinif: n, ders: d })); return; }
    const k = konular[ix];
    const baslik = k.ad === k.unite ? k.unite : k.ad;
    document.title = `${baslik} · ${n}. Sınıf ${ad} · Ders Kutusu`;
    const turler = [...new Set(k.icerik.map((i) => i.tur))];
    const liste = el('div', { sinif: 'agac-kartlar', id: 'konu-icerik', role: 'tabpanel' });
    const ciz = (tur) => {
      const L = k.icerik.filter((i) => !tur || i.tur === tur).sort((a, b) => (a.hafta - b.hafta) || a.tur.localeCompare(b.tur, 'tr'));
      liste.replaceChildren(...L.map((i) => kart(i, dersler, { dersGoster: false })));
    };
    const sekme = (etiket, tur, sayi) => el('button', { type: 'button', role: 'tab', sinif: 'agac-sekme', 'aria-selected': tur === '' ? 'true' : 'false', 'aria-controls': 'konu-icerik', 'data-tur': tur,
      onclick: (o) => { $$('.agac-sekme', sekmeler).forEach((b) => b.setAttribute('aria-selected', String(b === o.currentTarget))); ciz(tur); } },
      etiket, el('small', {}, String(sayi)));
    const sekmeler = el('div', { sinif: 'agac-sekmeler', role: 'tablist', 'aria-label': 'İçerik türleri' },
      sekme('Tümü', '', k.icerik.length), ...turler.map((t) => sekme(K().category(t).title || t, t, k.icerik.filter((i) => i.tur === t).length)));
    const komsu = (j, yon) => j >= 0 && j < konular.length ? el('a', { sinif: `agac-komsu ${yon}`, href: adres({ sinif: n, ders: d, konu: konular[j].kod }) },
      el('small', {}, yon === 'onceki' ? '← Önceki konu' : 'Sonraki konu →'), el('strong', {}, konular[j].ad === konular[j].unite ? konular[j].unite : konular[j].ad)) : el('span', {});
    alan.replaceChildren(
      el('section', { sinif: 'agac-bas agac-ders-bas', 'data-renk': renk }, el('div', { sinif: 'kap' },
        konum(KOK_YOL, DAL_YOL, sinifYol, dersYol, { ad: baslik }),
        el('p', { sinif: 'agac-ust' }, `${n}. Sınıf · ${ad} · ${k.ui + 1}. ünite: ${k.unite}`),
        el('h1', {}, baslik),
        el('div', { sinif: 'agac-cipler' }, el('span', {}, haftaMetni(k.haftalar)), tarihMetni(k.haftalar, agac.haftalar) ? el('span', {}, tarihMetni(k.haftalar, agac.haftalar)) : null,
          simdi && k.haftalar.includes(simdi) ? el('span', { sinif: 'agac-rozet bu-hafta' }, 'Bu hafta') : null))),
      bolum('', k.icerik.length ? el('div', {}, sekmeler, liste)
        : bos('Bu konunun içerikleri hazırlanıyor', 'Konu anlatımı ve çalışma kâğıdı yıllık plan sırasıyla ekleniyor. Bu arada ders kitabından çalışabilirsin.',
          ...dersDuzeyi.filter((i) => i.tur === 'Ders kitabı').map((i) => el('a', { sinif: 'dugme ana', href: yol(i.goruntule || i.baglanti) }, 'Ders kitabını aç', simge('ok'))),
          el('a', { sinif: 'dugme', href: dersYol.href }, 'Bütün üniteler')),
        el('nav', { sinif: 'agac-komsular', 'aria-label': 'Konular arasında geçiş' }, komsu(ix - 1, 'onceki'), komsu(ix + 1, 'sonraki'))));
    if (k.icerik.length) ciz('');
  }

  // ---------------------------------------------------------------- ÖĞRETMEN
  const KATEGORILER = [
    { kod: 'gunluk-plan', tur: 'Ders planı', ad: 'Günlük planlar', aciklama: 'Okul ve yönetici adları her sayfaya yazılır; tüm yıl ya da ay ay, Word veya PDF.', simge: 'takvim', renk: 'turuncu', sayfa: '/planlar.html' },
    { kod: 'yillik-plan', tur: 'Yıllık plan', ad: 'Yıllık planlar', aciklama: 'Güncel öğretim programına göre haftalık yıllık planlar.', simge: 'takvim', renk: 'mavi' },
    { kod: 'yazili', tur: 'Yazılı senaryosu', ad: 'Yazılı senaryoları ve kâğıtları', aciklama: 'Ortak yazılı konu-soru dağılımları ve cevaplı yazılı kâğıtları.', simge: 'onay', renk: 'pembe', sayfa: '/yazili.html' },
    { kod: 'ogretim-programi', tur: 'Öğretim programı', ad: 'Öğretim programları', aciklama: 'Öğrenme çıktıları, süreç bileşenleri ve açıklamalar.', simge: 'kitap', renk: 'turkuaz' },
    { kod: 'calisma-kagidi', tur: 'Çalışma kâğıdı', ad: 'Çalışma kâğıtları', aciklama: 'Derste kullanmak için cevaplı ve cevapsız PDF.', simge: 'kalem', renk: 'yesil' },
    { kod: 'belgeler', ad: 'Resmî belgeler', aciklama: 'MEB, ÖDSGM, DÖGM ve ÖSYM kılavuzları ve tabloları.', simge: 'kitap', renk: 'lacivert', sayfa: '/belgeler.html' },
    { kod: 'tahta', ad: 'Akıllı tahta', aciklama: 'Kalem, renkler, kareli zemin; tarayıcıda çalışır.', simge: 'kalem', renk: 'sari', sayfa: '/tahta.html' },
    { kod: 'kpss', ad: 'KPSS hazırlık', aciklama: 'Öğretmen adayları için konu anlatımı ve testler.', simge: 'onay', renk: 'mor', sayfa: '/kpss.html' },
  ];

  function ogretmenKok({ dersler, icerikler }) {
    const ogt = icerikler.filter(kitleUyar(dersler));
    const kategoriKarti = (k) => {
      const sayi = k.tur ? ogt.filter((i) => i.tur === k.tur).length : null;
      return el('a', { sinif: 'agac-kategori', href: k.sayfa || adres({ kategori: k.kod }), 'data-renk': k.renk },
        el('span', { sinif: 'agac-kategori-simge', 'aria-hidden': 'true' }, simge(k.simge)),
        sayi ? el('span', { sinif: 'agac-adet' }, sayiYaz(sayi, 'dosya')) : null,
        el('h3', {}, k.ad), el('p', {}, k.aciklama), el('span', { sinif: 'agac-basla' }, 'Aç', el('span', { 'aria-hidden': 'true' }, ' →')));
    };
    alan.replaceChildren(
      basBolum([{ ad: 'Öğretmen Köşesi' }], 'Öğretmen', 'Öğretmen Köşesi', 'Bir kategori seçin: planlar, yazılılar, programlar ve derse hazırlık dosyaları.'),
      bolum('', el('div', { sinif: 'agac-kategoriler' }, KATEGORILER.map(kategoriKarti))),
      bolum('koyu-zemin', baslikSatiri('Öğretmenlere son eklenenler', null, el('a', { sinif: 'tumu', href: '/icerikler.html?kitle=ogretmen' }, 'Tümünü gör', simge('ok'))),
        kartlar(yeniler(ogt).slice(0, 6), dersler)));
  }

  function ogretmenKategori({ dersler, icerikler }, kat, n) {
    const ogt = icerikler.filter(kitleUyar(dersler)).filter((i) => i.tur === kat.tur);
    const katYol = { ad: kat.ad, href: adres({ kategori: kat.kod }) };
    const siniflar = new Set(ogt.map((i) => Number(i.sinif)));
    if (!n) {
      document.title = `${kat.ad} · Öğretmen Köşesi · Ders Kutusu`;
      alan.replaceChildren(
        basBolum([DAL_YOL, { ad: kat.ad }], 'Öğretmen Köşesi', kat.ad, 'Sınıfınızı seçin.'),
        bolum('', ...sinifIzgarasi(dersler, (s) => adres({ kategori: kat.kod, sinif: s }), (s) => sayiYaz(ogt.filter((i) => Number(i.sinif) === s).length, 'dosya'), (s) => siniflar.has(s))),
        kat.sayfa ? bolum('koyu-zemin', el('a', { sinif: 'dugme ana', href: kat.sayfa }, `${kat.ad} sayfasını aç`, simge('ok'))) : null);
      return;
    }
    document.title = `${n}. Sınıf ${kat.ad} · Öğretmen Köşesi · Ders Kutusu`;
    const buSinif = ogt.filter((i) => Number(i.sinif) === n);
    const sira = [...dersler.siniflar[n] || [], ...(dersler.secmeli?.[n] || [])];
    const dersAnahtar = [...new Set(buSinif.map((i) => i.ders))].sort((a, b) => (sira.indexOf(a) + 1 || 99) - (sira.indexOf(b) + 1 || 99));
    alan.replaceChildren(
      basBolum([DAL_YOL, katYol, { ad: `${n}. sınıf` }], kat.ad, `${n}. sınıf · ${kat.ad}`, null,
        sinifGecis(dersler, n, (s) => adres({ kategori: kat.kod, sinif: s }), (s) => siniflar.has(s))),
      bolum('', buSinif.length ? kartlar(dersAnahtar.flatMap((d) => buSinif.filter((i) => i.ders === d)), dersler)
        : bos('Bu sınıfta henüz dosya yok', 'Dosyalar eklendikçe burada listelenecek.', el('a', { sinif: 'dugme', href: katYol.href }, 'Başka sınıf seç'))));
  }

  // ---------------------------------------------------------------- başlat
  Promise.all([ortakVeri, veri('agac/dizin.json')]).then(async ([v, dizin]) => {
    if (!v.dersler || !v.iceriklerYuklendi) {
      alan.replaceChildren(bolum('', bos('İçerikler şu anda yüklenemedi', 'Sayfayı yenileyin ya da kütüphaneden arayın.', el('a', { sinif: 'dugme ana', href: '/icerikler.html' }, 'Kütüphaneyi aç'))));
      return;
    }
    const n = Number(P.get('sinif')) || null;
    if (n && !v.dersler.siniflar[n]) { location.replace(location.pathname); return; }
    if (KITLE === 'ogrenci') {
      const d = P.get('ders');
      if (n && d && (v.dersler.dersler[d])) await ogrenciDers(v, n, d);
      else if (n) ogrenciSinif(v, dizin, n);
      else ogrenciKok(v, dizin);
    } else {
      const kat = KATEGORILER.find((k) => k.kod === P.get('kategori') && k.tur);
      if (kat) ogretmenKategori(v, kat, n);
      else ogretmenKok(v);
    }
    alan.setAttribute('aria-busy', 'false');
  });
})();
