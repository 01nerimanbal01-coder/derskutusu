// Akıllı site içi arama. Dışarıdan hiçbir şey yüklenmez; bütün arama tarayıcıda yapılır.
// Çekirdek (Arama) sayfadan bağımsızdır: Türkçe harf eşleme, yazım hatası toleransı, eş anlamlılar,
// sorgudan sınıf / ders / tür / sınav çıkarma, gevşetmeli sıralama. Arayüz: üst menüdeki kutu (öneriler) ve ara.html.

const Arama = (() => {
  // ---------- metin ----------
  const HARF = { İ: 'i', I: 'i', ı: 'i', Ç: 'c', ç: 'c', Ğ: 'g', ğ: 'g', Ö: 'o', ö: 'o', Ş: 's', ş: 's', Ü: 'u', ü: 'u', Â: 'a', â: 'a', Î: 'i', î: 'i', Û: 'u', û: 'u' };
  // Uzunluğu korur (vurgulama için): her UTF-16 birimi tek harfe dönüşür.
  function duz(s) {
    s = String(s ?? '');
    let o = '';
    for (let i = 0; i < s.length; i++) {
      const h = s[i];
      let k = HARF[h] ?? h.toLowerCase();
      if (k.length !== 1 || !/[a-z0-9]/.test(k)) k = ' ';
      o += k;
    }
    return o;
  }
  const kelimeler = (s) => duz(s).replace(/(\d)([a-z])/g, '$1 $2').replace(/([a-z])(\d)/g, '$1 $2').split(/\s+/).filter(Boolean);

  // Damerau-Levenshtein (sınırlı): sınırı aşarsa sinir + 1 döner.
  function uzaklik(a, b, sinir) {
    if (Math.abs(a.length - b.length) > sinir) return sinir + 1;
    const m = a.length, n = b.length;
    let onceki2 = null, onceki = Array.from({ length: n + 1 }, (_, j) => j);
    for (let i = 1; i <= m; i++) {
      const simdi = [i];
      let enKucuk = i;
      for (let j = 1; j <= n; j++) {
        const bedel = a[i - 1] === b[j - 1] ? 0 : 1;
        let d = Math.min(onceki[j] + 1, simdi[j - 1] + 1, onceki[j - 1] + bedel);
        if (onceki2 && i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d = Math.min(d, onceki2[j - 2] + 1);
        simdi.push(d);
        if (d < enKucuk) enKucuk = d;
      }
      if (enKucuk > sinir) return sinir + 1;
      onceki2 = onceki; onceki = simdi;
    }
    return onceki[n];
  }
  const hataSiniri = (u) => (u >= 8 ? 2 : u >= 4 ? 1 : 0);

  // Sorgu kelimesi (q) ile belge kelimesi (k) eşleşmesi: 1 tam, 0.8 ek/kök, 0.7 yazarken önek, 0.55 yazım hatası.
  function eslesme(q, k, sonKelime) {
    if (q === k) return 1;
    if (k.length >= 4 && q.startsWith(k) && q.length - k.length <= 5) return 0.8;          // planlari → plan
    if (q.length >= 4 && k.startsWith(q)) return 0.8;                                       // matem → matematik
    if (sonKelime && q.length >= 2 && k.startsWith(q)) return 0.7;
    const s = hataSiniri(Math.min(q.length, k.length));
    if (s && /^[a-z]+$/.test(q) && uzaklik(q, k, s) <= s) return 0.55;
    return 0;
  }

  // ---------- sözlükler ----------
  const DURAK = new Set(('ve ile icin de da bir bu su o ne nasil nerede nedir hangi kac mi mu mı mü zaman ' +
    'indir indirme bul goster ara arama istiyorum lazim var yok dosya dosyasi dosyalari pdf word excel ' +
    'sinif sinifi siniflar sinifin ders dersi dersleri dersin icerik icerikler egitim ogretim yili yil 2026 2027 donem').split(' '));

  const SAYI = { besinci: 5, bes: 5, altinci: 6, alti: 6, yedinci: 7, yedi: 7, sekizinci: 8, sekiz: 8, dokuzuncu: 9, dokuz: 9, onuncu: 10 };

  // Ek kısaltma ve eş anlamlılar (dersler.json adları kendiliğinden eklenir).
  const DERS_ES = {
    turkce: ['turkce', 'trk'],
    matematik: ['mat', 'matematik', 'math', 'maths'],
    'fen-bilimleri': ['fen', 'fen bilimleri', 'fen bilgisi', 'fen ve teknoloji'],
    'sosyal-bilgiler': ['sosyal', 'sosyal bilgiler', 'sosyal bilgisi'],
    ingilizce: ['ingilizce', 'ing', 'english', 'yabanci dil'],
    'din-kulturu-ve-ahlak-bilgisi': ['din', 'din kulturu', 'dkab', 'din dersi', 'ahlak bilgisi'],
    'tc-inkilap-tarihi-ve-ataturkculuk': ['inkilap', 'inkilap tarihi', 'ataturkculuk', 'tc inkilap', 'inkilap tarihi ve ataturkculuk'],
    'turk-dili-ve-edebiyati': ['edebiyat', 'tde', 'turk dili', 'turk edebiyati', 'turk dili ve edebiyati'],
    fizik: ['fizik', 'fzk'],
    kimya: ['kimya', 'kmy'],
    biyoloji: ['biyo', 'biyoloji', 'bio'],
    tarih: ['tarih', 'trh'],
    cografya: ['cog', 'cografya', 'cografi'],
    felsefe: ['felsefe', 'fls'],
    'kuran-i-kerim': ['kuran', 'kuran i kerim', 'kurani kerim', 'kuranikerim'],
    'peygamberimizin-hayati': ['peygamber', 'peygamberimizin hayati', 'peygamberin hayati'],
    'temel-dini-bilgiler': ['temel dini bilgiler', 'tdb', 'dini bilgiler'],
    'hitabet-ve-mesleki-uygulama': ['hitabet'],
    'islam-kultur-ve-medeniyeti': ['islam kultur', 'islam medeniyeti', 'islam kultur ve medeniyeti'],
  };

  // Tür ve konu niyetleri: kelime öbeği → { tur | grup | ozel, sinif ipucu }
  const NIYET = [
    { ad: 'Yıllık plan', ob: ['yillik plan', 'yillik', 'senelik plan', 'yillik planlar', 'cerceve plan', 'unitelendirilmis plan'], tur: 'Yıllık plan' },
    { ad: 'Günlük plan', ob: ['gunluk plan', 'gunluk', 'ders plani', 'haftalik plan', 'gunluk planlar', 'ders planlari'], tur: 'Ders planı' },
    { ad: 'Plan', ob: ['plan', 'planlar', 'planlama'], turler: ['Yıllık plan', 'Ders planı'] },
    { ad: 'Öğretim programı', ob: ['ogretim programi', 'mufredat', 'kazanim', 'kazanimlar', 'ogrenme ciktisi', 'ogrenme ciktilari', 'program'], tur: 'Öğretim programı' },
    { ad: 'Konu anlatımı', ob: ['konu anlatimi', 'konu anlatim', 'anlatim'], tur: 'Konu anlatımı' },
    { ad: 'Soru çözümü', ob: ['soru cozumu', 'cozum', 'cozumlu'], tur: 'Soru çözümü' },
    { ad: 'Video', ob: ['video', 'videolar', 'youtube'], tur: 'Video' },
    { ad: 'Test', ob: ['test', 'testler', 'deneme'], tur: 'Test' },
    { ad: 'Çalışma kâğıdı', ob: ['calisma kagidi', 'calisma kagitlari', 'etkinlik kagidi'], tur: 'Çalışma kâğıdı' },
    { ad: 'Ortak yazılı', ob: ['ortak yazili', 'yazili', 'yazililar', 'konu soru dagilim', 'soru dagilim', 'dagilim tablosu', 'senaryo'], grup: 'yazili', tur: 'Yazılı soruları' },
    { ad: 'LGS', ob: ['lgs', 'liselere gecis', 'liseye gecis', 'lise sinavi', 'merkezi sinav'], grup: 'lgs', sinif: 8 },
    { ad: 'YKS', ob: ['yks', 'tyt', 'ayt', 'ydt', 'universite sinavi', 'osym'], grup: 'yks', siniflar: [11, 12] },
    { ad: 'Kılavuz', ob: ['kilavuz', 'klavuz', 'kilavuzlar', 'rehber'], grup: 'kilavuz' },
    { ad: 'Takvim', ob: ['takvim', 'calisma takvimi', 'tatil', 'ara tatil', 'yariyil', 'karne', 'okullar ne zaman'], ozel: 'takvim' },
    { ad: 'Öğretmen', ob: ['ogretmen', 'ogretmenler', 'zumre'], kitle: 'ogretmen' },
    { ad: 'Öğrenci', ob: ['ogrenci', 'ogrenciler', 'veli'], kitle: 'ogrenci' },
  ];

  // ---------- dizin ----------
  let DIZIN = null;

  function kayit(o) {
    o.a = { baslik: kelimeler(o.baslik), diger: kelimeler([o.aciklama, o.dersAd, o.tur, o.kaynak, o.grupAd, o.ek].filter(Boolean).join(' ')) };
    return o;
  }

  function kur({ dersler, icerikler = [], belgeler = null }) {
    const dAd = dersler?.dersler || {};
    const siniflar = dersler?.siniflar || {};
    const secmeli = dersler?.secmeli || {};
    const belgeler_ = [];
    const ekle = (o) => belgeler_.push(kayit(o));

    // Sayfalar
    ekle({ tip: 'sayfa', baslik: 'İçerikler', aciklama: 'Bütün içerikler: sınıf, ders ve türe göre süzün.', adres: '/icerikler.html', ek: 'kutuphane liste' });
    ekle({ tip: 'sayfa', baslik: 'Resmî belgeler', aciklama: 'Öğretim programları, kılavuzlar, ortak yazılı tabloları, LGS ve YKS belgeleri.', adres: '/belgeler.html', ek: 'meb odsgm dogm osym resmi' });
    ekle({ tip: 'sayfa', baslik: 'Öğretmen köşesi', aciklama: 'Yıllık planlar, günlük planlar, yazılı soruları ve çalışma kâğıtları.', adres: '/icerikler.html?kitle=ogretmen', kitle: 'ogretmen', ek: 'ogretmen' });
    ekle({ tip: 'sayfa', baslik: 'İletişim', aciklama: 'Bize e-posta ve sosyal medyadan ulaşın.', adres: '/#iletisim', ek: 'iletisim eposta mail adres' });
    ekle({ tip: 'sayfa', baslik: 'Gizlilik ve çerezler', aciklama: 'Kişisel veriler ve çerez tercihleri.', adres: '/gizlilik.html', ek: 'kvkk cerez gizlilik' });
    ekle({ tip: 'sayfa', baslik: 'Sosyal medya', aciklama: 'YouTube, Instagram ve Facebook hesaplarımız.', adres: '/#sosyal', ek: 'youtube instagram facebook takip' });
    for (const n of Object.keys(siniflar)) {
      const no = Number(n);
      ekle({ tip: 'sayfa', alt: 'sinif', baslik: `${no}. sınıf`, aciklama: `${no <= 8 ? 'Ortaokul' : 'Lise'} ${no}. sınıfın bütün dersleri.`, adres: `/sinif.html?no=${no}`, sinif: no });
      for (const d of [...siniflar[n], ...(secmeli[n] || [])]) {
        ekle({ tip: 'sayfa', alt: 'ders', baslik: `${no}. sınıf ${dAd[d]}`, aciklama: `${no}. sınıf ${dAd[d]} dersinin bütün içerikleri.`, adres: `/icerikler.html?sinif=${no}&ders=${d}`, sinif: no, ders: d });
      }
    }
    for (const [d, ad] of Object.entries(dAd)) {
      ekle({ tip: 'sayfa', alt: 'ders-tum', baslik: `${ad} (bütün sınıflar)`, aciklama: `${ad} dersinin bütün sınıflardaki içerikleri.`, adres: `/icerikler.html?ders=${d}`, ders: d });
    }
    // İçerikler
    for (const i of icerikler) {
      ekle({ tip: 'icerik', baslik: i.baslik, aciklama: i.aciklama, adres: i.dosya ? `/${i.dosya}` : i.baglanti, dosya: !!i.dosya,
        dis: !i.dosya && /^https?:/.test(i.baglanti || ''), sinif: i.sinif ? Number(i.sinif) : null, ders: i.ders, dersAd: dAd[i.ders],
        tur: i.tur, kitle: i.kitle, kaynak: i.kaynak, tarih: i.tarih });
    }
    // Resmî belgeler
    for (const g of belgeler?.gruplar || []) {
      for (const b of g.belgeler) {
        const kademe = b.kademe === 'Ortaokul' ? [5, 6, 7, 8] : b.kademe === 'Ortaöğretim' ? [9, 10, 11, 12] : null;
        ekle({ tip: 'belge', baslik: b.baslik, aciklama: b.aciklama, adres: b.dosya ? `/${b.dosya}` : b.baglanti, dosya: !!b.dosya,
          dis: !b.dosya, grup: g.kimlik, grupAd: g.ad, ders: b.ders || null, dersAd: dAd[b.ders],
          sinif: b.sinif || null, siniflar: b.sinif ? [b.sinif] : g.kimlik === 'yks' ? [11, 12] : kademe,
          tur: g.kimlik === 'program' ? 'Öğretim programı' : 'Resmî belge', kitle: b.kitle, kaynak: b.kaynak, kademe: b.kademe });
      }
    }

    // Ders eş anlamlıları
    const dersOb = [];
    for (const [d, ad] of Object.entries(dAd)) {
      const obekler = new Set([duz(ad).trim().replace(/\s+/g, ' '), duz(d.replace(/-/g, ' ')).trim(), ...(DERS_ES[d] || [])]);
      for (const o of obekler) dersOb.push({ ob: o.split(' '), ders: d });
    }
    const niyetOb = NIYET.flatMap((n) => n.ob.map((o) => ({ ob: o.split(' '), niyet: n })));
    const sozluk = new Set();
    for (const b of belgeler_) for (const k of [...b.a.baslik, ...b.a.diger]) sozluk.add(k);
    for (const x of [...dersOb, ...niyetOb]) for (const k of x.ob) sozluk.add(k);
    DIZIN = { belgeler: belgeler_, dersOb, niyetOb, sozluk: [...sozluk].filter((k) => k.length >= 3 && !/^\d+$/.test(k)), dAd };
    return DIZIN;
  }

  // ---------- sorgu çözümleme ----------
  function obekBul(ks, liste, bas, sonKelime) {
    // bas konumunda başlayan en uzun öbek; tek kelimelik öbekte yazım hatası ve (son kelimede) önek kabul edilir.
    let en = null;
    for (const x of liste) {
      const u = x.ob.length;
      if (bas + u > ks.length) continue;
      let tamam = true, puan = 0;
      for (let j = 0; j < u; j++) {
        const q = ks[bas + j], k = x.ob[j];
        let e = q === k ? 1 : 0;
        if (!e && k.length >= 4) {
          const son = sonKelime && bas + j === ks.length - 1;
          if (son && q.length >= 3 && k.startsWith(q)) e = 0.75;
          else if (q.length >= 4 && hataSiniri(k.length) && uzaklik(q, k, hataSiniri(Math.min(q.length, k.length))) <= hataSiniri(Math.min(q.length, k.length))) e = 0.6;
          else if (k.length >= 5 && q.startsWith(k) && q.length - k.length <= 4) e = 0.85;   // matematigi, planlari
        }
        if (!e) { tamam = false; break; }
        puan += e;
      }
      if (tamam && (!en || u > en.u || (u === en.u && puan > en.puan))) en = { ...x, u, puan, tam: puan === u };
    }
    return en;
  }

  function cozumle(sorgu, { yaziyor = false } = {}) {
    const ks = kelimeler(sorgu);
    const s = { ham: sorgu, sinif: null, dersler: [], niyetler: [], kitle: null, serbest: [], duzeltmeler: [] };
    for (let i = 0; i < ks.length;) {
      const q = ks[i];
      const son = yaziyor && i === ks.length - 1;
      // sınıf: "8", "8 sinif", "sekizinci sinif", "10 uncu"
      if (/^\d{1,2}$/.test(q) && +q >= 5 && +q <= 12) {
        s.sinif = +q; i++;
        while (i < ks.length && /^(sinif|sinifi|sn|s|inci|nci|uncu|nci|ci|ncu|uncu)$/.test(ks[i])) i++;
        continue;
      }
      if (SAYI[q] && (ks[i + 1] || '').startsWith('sinif')) { s.sinif = SAYI[q]; i += 2; continue; }
      if (q === 'on' && ['birinci', 'ikinci', 'bir', 'iki'].includes(ks[i + 1])) { s.sinif = ks[i + 1].startsWith('bir') ? 11 : 12; i += 2; if ((ks[i] || '').startsWith('sinif')) i++; continue; }
      const d = obekBul(ks, DIZIN.dersOb, i, son);
      const n = obekBul(ks, DIZIN.niyetOb, i, son);
      // Aynı yerde ikisi de eşleşirse uzun ve tam olan kazanır ("temel dini bilgiler" > "din").
      const secilen = [d, n].filter(Boolean).sort((a, b) => b.u - a.u || b.puan - a.puan)[0];
      if (secilen && (secilen.ders || !DURAK.has(q) || secilen.u > 1)) {
        const kaynak = ks.slice(i, i + secilen.u).join(' ');
        if (secilen.ders) { if (!s.dersler.includes(secilen.ders)) s.dersler.push(secilen.ders); }
        else if (secilen.niyet.kitle) s.kitle = secilen.niyet.kitle;
        else if (!s.niyetler.includes(secilen.niyet)) s.niyetler.push(secilen.niyet);
        if (!secilen.tam && secilen.puan / secilen.u < 0.8) s.duzeltmeler.push([kaynak, secilen.ob.join(' ')]);
        i += secilen.u;
        continue;
      }
      if (!DURAK.has(q) && !(q.length === 1 && !/\d/.test(q))) s.serbest.push(q);
      i++;
    }
    // "plan" hem yıllık hem günlük; daha belirgin bir plan niyeti varsa genel olanı at.
    if (s.niyetler.some((n) => n.tur === 'Yıllık plan' || n.tur === 'Ders planı')) s.niyetler = s.niyetler.filter((n) => n.ad !== 'Plan');
    // "program" tek başına ders adıyla gelirse öğretim programı sayılır; aksi hâlde serbest kelime de olabilir.
    return s;
  }

  // ---------- puanlama ----------
  function turUyar(b, s) {
    const turNiyet = s.niyetler.filter((n) => n.tur || n.turler || n.grup || n.ozel);
    if (!turNiyet.length) return true;
    return turNiyet.some((n) =>
      (n.tur && b.tur === n.tur) || (n.turler && n.turler.includes(b.tur)) || (n.grup && b.grup === n.grup) ||
      (n.ozel === 'takvim' && /takvim/.test(duz(b.baslik))));
  }

  function sinifUyar(b, sinif) {
    if (!sinif) return 0;
    if (b.sinif) return b.sinif === sinif ? 2 : -1;
    if (b.siniflar) return b.siniflar.includes(sinif) ? 1 : -1;
    return 0;
  }

  function serbestPuan(b, terimler, yaziyor) {
    let toplam = 0, bulunan = 0;
    terimler.forEach((q, i) => {
      const son = yaziyor && i === terimler.length - 1;
      let en = 0;
      for (const k of b.a.baslik) { const e = eslesme(q, k, son) * 10; if (e > en) en = e; }
      for (const k of b.a.diger) { const e = eslesme(q, k, son) * 4; if (e > en) en = e; }
      if (en) bulunan++;
      toplam += en;
    });
    return { toplam, bulunan };
  }

  function puanla(s, kural, yaziyor) {
    const ipucuSinif = s.sinif ?? s.niyetler.find((n) => n.sinif)?.sinif ?? null;
    const sonuc = [];
    for (const b of DIZIN.belgeler) {
      let p = 0;
      // Sayfa kısayolları yalnız sınıf/ders sorulunca; türlü sorguda (ör. yıllık plan) içerik öne çıkar.
      if (b.tip === 'sayfa' && b.alt) {
        if (b.alt === 'sinif' && !(s.sinif && !s.dersler.length && b.sinif === s.sinif)) continue;
        if (b.alt === 'ders' && !(s.dersler.includes(b.ders) && (s.sinif ? b.sinif === s.sinif : false))) continue;
        if (b.alt === 'ders-tum' && !(s.dersler.includes(b.ders) && !s.sinif)) continue;
        p += 60 - (s.niyetler.length ? 25 : 0);
      } else {
        if (kural.tur && !turUyar(b, s)) continue;
        if (kural.ders && s.dersler.length) {
          if (b.ders && !s.dersler.includes(b.ders)) continue;
          if (!b.ders && !s.niyetler.some((n) => n.grup || n.ozel) && !s.serbest.length) continue;
          if (b.ders) p += 30;
        }
        if (kural.sinif && s.sinif) {
          const u = sinifUyar(b, s.sinif);
          if (u < 0) continue;
          p += u * 12;
        } else if (ipucuSinif) p += Math.max(0, sinifUyar(b, ipucuSinif)) * 4;
        if (s.kitle) p += b.kitle === s.kitle ? 8 : -4;
        if (s.niyetler.length && turUyar(b, s)) p += 20;
      }
      if (s.serbest.length) {
        const { toplam, bulunan } = serbestPuan(b, s.serbest, yaziyor);
        if (kural.hepsi && bulunan < s.serbest.length) continue;
        if (!bulunan && b.tip !== 'sayfa') {
          // Sorguda yalnız serbest kelime varsa eşleşmeyen belge gösterilmez.
          if (!s.dersler.length && !s.niyetler.length && !s.sinif) continue;
          if (!kural.tur && !kural.ders && !kural.sinif) continue;
        }
        p += toplam;
      } else if (!s.dersler.length && !s.niyetler.length && !s.sinif && !s.kitle) continue;
      if (b.tip === 'sayfa' && !b.alt && !s.serbest.length && !s.niyetler.length) continue;
      if (b.tip === 'sayfa' && !b.alt && s.serbest.length && !serbestPuan(b, s.serbest, yaziyor).bulunan) continue;
      if (b.tip !== 'sayfa' && p <= 0) continue;
      sonuc.push({ b, p });
    }
    // Aynı adrese giden kayıtlardan yalnız en yüksek puanlı kalır (ör. 5–8. sınıfların ortak öğretim programı).
    const enIyi = new Map();
    for (const r of sonuc) { const e = enIyi.get(r.b.adres); if (!e || r.p > e.p || (r.p === e.p && r.b.tip === 'belge')) enIyi.set(r.b.adres, r); }
    return [...enIyi.values()].sort((x, y) => y.p - x.p || (x.b.tip === 'sayfa' ? -1 : 0) - (y.b.tip === 'sayfa' ? -1 : 0) || x.b.baslik.localeCompare(y.b.baslik, 'tr', { numeric: true }));
  }

  // Sonuç yoksa kısıtlar sırayla gevşetilir.
  const GEVSEME = [
    { kural: { tur: true, ders: true, sinif: true, hepsi: true }, not: null },
    { kural: { tur: true, ders: true, sinif: true, hepsi: false }, not: 'Bütün kelimeleri içeren sonuç yok; en yakın sonuçlar gösteriliyor.' },
    { kural: { tur: false, ders: true, sinif: true, hepsi: false }, not: 'İstediğiniz türde içerik yok; aynı sınıf ve dersin öteki içerikleri gösteriliyor.' },
    { kural: { tur: false, ders: true, sinif: false, hepsi: false }, not: 'Bu sınıf için içerik yok; öteki sınıflardaki içerikler gösteriliyor.' },
    { kural: { tur: false, ders: false, sinif: false, hepsi: false }, not: 'Tam eşleşme yok; ilgili olabilecek sonuçlar gösteriliyor.' },
  ];

  function ara(sorgu, { yaziyor = false } = {}) {
    if (!DIZIN) throw new Error('Arama dizini kurulmadı');
    const s = cozumle(sorgu, { yaziyor });
    const bos = !s.sinif && !s.dersler.length && !s.niyetler.length && !s.kitle && !s.serbest.length;
    if (bos) return { sorgu: s, sonuclar: [], not: null, anlasilan: [] };
    let sonuclar = [], not = null;
    for (const g of GEVSEME) {
      sonuclar = puanla(s, g.kural, yaziyor);
      const gercek = sonuclar.filter((r) => r.b.tip !== 'sayfa');
      if (gercek.length || (sonuclar.length && !s.niyetler.length && !s.serbest.length)) { not = g.not; break; }
    }
    // Serbest kelimelerde yazım düzeltmesi önerisi
    for (const q of s.serbest) {
      if (q.length < 4 || DIZIN.sozluk.includes(q)) continue;
      if (DIZIN.sozluk.some((k) => k.startsWith(q))) continue;
      const sinir = hataSiniri(q.length);
      let en = null, enD = sinir + 1;
      for (const k of DIZIN.sozluk) { const d = uzaklik(q, k, sinir); if (d < enD) { enD = d; en = k; } }
      if (en) s.duzeltmeler.push([q, en]);
    }
    const anlasilan = [
      s.sinif && { tur: 'sinif', ad: `${s.sinif}. sınıf` },
      ...s.dersler.map((d) => ({ tur: 'ders', ad: DIZIN.dAd[d], deger: d })),
      ...s.niyetler.map((n) => ({ tur: 'niyet', ad: n.ad })),
      s.kitle && { tur: 'kitle', ad: s.kitle === 'ogretmen' ? 'Öğretmen' : 'Öğrenci' },
    ].filter(Boolean);
    return { sorgu: s, sonuclar, not, anlasilan };
  }

  // Başlıkta eşleşen kelimeleri bul: [bas, son] aralıkları (özgün metin konumları).
  function vurgular(metin, sorgu) {
    const s = cozumle(sorgu);
    const terimler = [...s.serbest, ...s.dersler.flatMap((d) => kelimeler(DIZIN.dAd[d]))];
    const d = duz(metin);
    const araliklar = [];
    const re = /[a-z0-9]+/g;
    let m;
    while ((m = re.exec(d))) {
      if (terimler.some((q) => eslesme(q, m[0], true) >= 0.7)) araliklar.push([m.index, m.index + m[0].length]);
    }
    return araliklar;
  }

  // Kütüphane süzgeci için basit akıllı eşleşme: bütün kelimeler (hatalı yazım dahil) metinde var mı?
  function metinEslesir(metin, sorgu) {
    const qs = kelimeler(sorgu).filter((q) => !DURAK.has(q));
    if (!qs.length) return true;
    const ks = kelimeler(metin);
    return qs.every((q, i) => ks.some((k) => eslesme(q, k, i === qs.length - 1) > 0));
  }

  return { duz, kelimeler, uzaklik, kur, cozumle, ara, vurgular, metinEslesir, dizin: () => DIZIN };
})();

if (typeof module !== 'undefined') module.exports = Arama;

// ---------- arayüz ----------
if (typeof document !== 'undefined') {
  const TUR_ETIKET = { sayfa: 'Sayfa', icerik: 'İçerik', belge: 'Resmî belge' };
  let hazir = null;
  const dizinHazirla = () => (hazir ||= Promise.all([ortakVeri, veri('belgeler.json')]).then(([v, belgeler]) => Arama.kur({ ...v, belgeler })));

  const vurgula = (metin, sorgu) => {
    const parca = [];
    let son = 0;
    for (const [a, b] of Arama.vurgular(metin, sorgu)) {
      if (a > son) parca.push(metin.slice(son, a));
      parca.push(el('mark', {}, metin.slice(a, b)));
      son = b;
    }
    parca.push(metin.slice(son));
    return parca;
  };
  const altBilgi = (b) => [b.sinif && `${b.sinif}. sınıf`, b.dersAd, b.tip === 'sayfa' ? null : b.tur, b.kaynak].filter(Boolean).join(' · ');
  const hedef = (b) => (b.dis ? { target: '_blank', rel: 'noopener' } : b.dosya ? { download: '' } : {});

  // Üst menüdeki kutu: anlık öneriler
  const form = $('.ust-arama');
  if (form) {
    const kutu = $('input', form);
    if (matchMedia('(max-width: 560px)').matches) kutu.placeholder = 'Ara';
    const liste = $('.oneri', form);
    let secili = -1, son = [];
    const kapat = () => { liste.hidden = true; kutu.setAttribute('aria-expanded', 'false'); secili = -1; };
    const isaretle = () => $$('li', liste).forEach((li, i) => { li.setAttribute('aria-selected', String(i === secili)); if (i === secili) li.scrollIntoView({ block: 'nearest' }); });
    const goster = async () => {
      const q = kutu.value.trim();
      if (q.length < 2) { kapat(); return; }
      await dizinHazirla();
      const r = Arama.ara(q, { yaziyor: true });
      son = r.sonuclar.slice(0, 7);
      const satirlar = son.map(({ b }, i) => el('li', { role: 'option', id: `oneri-${i}`, 'aria-selected': 'false' },
        el('a', { href: b.adres, tabindex: '-1', ...hedef(b) },
          el('span', { sinif: `oneri-tip ${b.tip}` }, TUR_ETIKET[b.tip]),
          el('span', { sinif: 'oneri-metin' }, el('strong', {}, ...vurgula(b.baslik, q)), el('small', {}, altBilgi(b))))));
      satirlar.push(el('li', { role: 'option', id: `oneri-${son.length}`, sinif: 'oneri-tumu', 'aria-selected': 'false' },
        el('a', { href: `/ara.html?q=${encodeURIComponent(q)}`, tabindex: '-1' },
          r.sonuclar.length ? `Bütün sonuçlar (${r.sonuclar.length})` : `“${q}” için sonuç yok; arama sayfasında dene`, simge('ok'))));
      liste.replaceChildren(...satirlar);
      liste.hidden = false;
      kutu.setAttribute('aria-expanded', 'true');
      secili = -1;
    };
    let zaman;
    kutu.addEventListener('input', () => { clearTimeout(zaman); zaman = setTimeout(goster, 90); });
    kutu.addEventListener('focus', () => { dizinHazirla(); if (kutu.value.trim().length >= 2) goster(); });
    kutu.addEventListener('keydown', (o) => {
      const n = $$('li', liste).length;
      if (o.key === 'ArrowDown' && n) { o.preventDefault(); secili = (secili + 1) % n; isaretle(); }
      else if (o.key === 'ArrowUp' && n) { o.preventDefault(); secili = (secili - 1 + n) % n; isaretle(); }
      else if (o.key === 'Escape') { kapat(); kutu.blur(); }
      else if (o.key === 'Enter' && secili >= 0 && !liste.hidden) { o.preventDefault(); $$('li a', liste)[secili]?.click(); }
      if (secili >= 0) kutu.setAttribute('aria-activedescendant', `oneri-${secili}`); else kutu.removeAttribute('aria-activedescendant');
    });
    document.addEventListener('click', (o) => { if (!form.contains(o.target)) kapat(); });
    form.addEventListener('submit', (o) => { if (!kutu.value.trim()) o.preventDefault(); });
    document.addEventListener('keydown', (o) => {
      if (o.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName) && !o.metaKey && !o.ctrlKey) { o.preventDefault(); kutu.focus(); }
    });
  }

  // ara.html: bütün sonuçlar
  const sayfa = $('#arama-sonuclari');
  if (sayfa) {
    const kutu = $('#arama-kutu');
    const q0 = new URLSearchParams(location.search).get('q') || '';
    kutu.value = q0;
    let gosterilen = 30;
    const ciz = async () => {
      await dizinHazirla();
      const q = kutu.value.trim();
      const r = Arama.ara(q);
      document.title = q ? `“${q}” araması · Ders Kutusu` : 'Arama · Ders Kutusu';
      $('#anlasilan').replaceChildren(...(r.anlasilan.length ? [el('span', { sinif: 'anlasilan-bas' }, 'Anlaşılan:'), ...r.anlasilan.map((a) => el('span', { sinif: `cip ${a.tur}` }, a.ad))] : []));
      const notlar = [];
      if (r.sorgu.duzeltmeler.length) notlar.push(`Yazım düzeltildi: ${r.sorgu.duzeltmeler.map(([a, b]) => `“${a}” → “${b}”`).join(', ')}`);
      if (r.not) notlar.push(r.not);
      $('#arama-not').replaceChildren(...notlar.map((n) => el('p', {}, n)));
      $('#arama-sayi').textContent = q ? (r.sonuclar.length ? `${r.sonuclar.length} sonuç` : 'Sonuç bulunamadı') : '';
      $('#arama-bos').hidden = !!(q && r.sonuclar.length);
      sayfa.replaceChildren(...r.sonuclar.slice(0, gosterilen).map(({ b }) =>
        el('article', { sinif: `kart arama-kart ${b.tip}` },
          el('div', { sinif: 'ust-bilgi' },
            el('span', { sinif: `etiket ${b.tip === 'belge' ? 'ogretmen' : b.tip === 'sayfa' ? '' : 'tur'}` }, TUR_ETIKET[b.tip]),
            b.sinif && el('span', { sinif: 'etiket' }, `${b.sinif}. sınıf`),
            b.dersAd && b.tip !== 'sayfa' && el('span', { sinif: 'etiket tur' }, b.dersAd),
            b.tur && b.tip !== 'sayfa' && b.tur !== TUR_ETIKET[b.tip] && el('span', { sinif: `etiket ${b.kitle === 'ogretmen' ? 'ogretmen' : 'tur'}` }, b.tur)),
          el('h3', {}, el('a', { href: b.adres, ...hedef(b) }, ...vurgula(b.baslik, q))),
          b.aciklama && el('p', {}, b.aciklama),
          el('a', { sinif: 'ac', href: b.adres, ...hedef(b) }, b.dosya ? 'İndir' : b.dis ? 'Aç' : 'Git', simge('ok')))));
      $('#daha-fazla').hidden = r.sonuclar.length <= gosterilen;
    };
    let zaman;
    kutu.addEventListener('input', () => {
      clearTimeout(zaman);
      zaman = setTimeout(() => {
        gosterilen = 30;
        const q = kutu.value.trim();
        history.replaceState(null, '', q ? `?q=${encodeURIComponent(q)}` : location.pathname);
        ciz();
      }, 150);
    });
    $('#arama-form').addEventListener('submit', (o) => { o.preventDefault(); ciz(); });
    $('#daha-fazla').addEventListener('click', () => { gosterilen += 30; ciz(); });
    $$('[data-ornek]').forEach((a) => a.addEventListener('click', (o) => { o.preventDefault(); kutu.value = a.dataset.ornek; kutu.dispatchEvent(new Event('input')); }));
    ciz();
  }
}
