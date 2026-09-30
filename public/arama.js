// Akıllı site içi arama. Dışarıdan hiçbir şey yüklenmez; bütün arama tarayıcıda yapılır.
// Çekirdek (Arama) sayfadan bağımsızdır: Türkçe harf eşleme, Türkçe ek çözümleme, yazım hatası toleransı,
// eş anlamlılar, sorgudan sınıf / kademe / ders / tür / sınav çıkarma, gevşetmeli sıralama.
// Arayüz: üst menüdeki kutu (anlık öneriler) ve ara.html. Sınama: 03-ARACLAR/arama_sina.js (jsc).

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
  // Kesme işareti kelimeyi bölmez: kur'an → kuran, Türkçe'nin → turkcenin.
  const kelimeler = (s) => duz(String(s ?? '').replace(/['’‘`´]/g, '')).replace(/(\d)([a-z])/g, '$1 $2').replace(/([a-z])(\d)/g, '$1 $2').split(/\s+/).filter(Boolean);

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
  // Yazım hatası sınırı; kısa kelimelerde kapalı (tarif ≠ tarih, fen ≠ ben).
  const hataSiniri = (u) => (u >= 8 ? 2 : u >= 6 ? 1 : 0);

  // ---------- Türkçe ekler ----------
  // Harfleri düzleştirilmiş (ı→i, ü→u, ö→o) yaygın çekim ve iyelik ekleri.
  const EKLER = new Set(('i u a e in un nin nun si su yi yu ya ye na ne ni nu da de ta te dan den tan ten nda nde ndan nden ' +
    'la le yla yle lar ler lari leri larin lerin lara lere larda lerde lardan lerden ki daki deki taki teki ' +
    'sin sinin sini sina sine sinda sinde sindan sinden ini ina ine inda inde indan inden inin ' +
    'dir tir lik luk lug lig ligi lugu ci cu').split(' '));
  // Kök sonundaki yumuşama geri alınır: matematig → matematik, kitab → kitap.
  const sertles = (k) => k.replace(/g$/, 'k').replace(/b$/, 'p').replace(/d$/, 't');
  const KOK = new Map();
  function kokler(w) {
    let r = KOK.get(w);
    if (r) return r;
    r = new Set([w]);
    for (let i = 3; i < w.length; i++) {
      const ek = w.slice(i);
      if (ek.length <= 6 && EKLER.has(ek)) { const k = w.slice(0, i); r.add(k); r.add(sertles(k)); }
    }
    KOK.set(w, r);
    return r;
  }
  // Aynı kelimenin ekli biçimi mi? (planı ~ plan, matematiğin ~ matematik, anahtarı ~ anahtarları)
  function ekli(q, k) {
    if (q === k) return true;
    if (Math.min(q.length, k.length) < 3) return false;
    const a = kokler(q), b = kokler(k);
    for (const x of a) if (x.length >= 3 && (b.has(x) || b.has(sertles(x)))) return true;
    return false;
  }

  // Sorgu kelimesi (q) ile belge kelimesi (k): 1 tam, 0.85 ekli, 0.8 önek, 0.7 yazarken önek, 0.55 yazım hatası.
  function eslesme(q, k, sonKelime) {
    if (q === k) return 1;
    if (ekli(q, k)) return 0.85;
    if (q.length >= 4 && k.startsWith(q)) return 0.8;
    if (sonKelime && q.length >= 2 && k.startsWith(q)) return 0.7;
    const s = hataSiniri(Math.min(q.length, k.length));
    if (s && /^[a-z]+$/.test(q) && uzaklik(q, k, s) <= s) return 0.55;
    return 0;
  }

  // ---------- sözlükler ----------
  const DURAK = new Set(('ve ile icin de da bir bu su o ne nasil nerede nedir hangi kac mi mu zaman ' +
    'indir indirme bul goster ara arama istiyorum lazim var yok dosya dosyasi dosyalari pdf word excel ' +
    'ders dersi dersleri dersin icerik icerikler egitim ogretim yili yil 2026 2027 donem donemi').split(' '));
  const sinifKelimesi = (q) => /^sinif[a-z]{0,6}$/.test(q) || ['sn', 'inci', 'nci', 'uncu', 'ncu', 'ci', 'cu', 'ncii'].includes(q);

  const SAYI = { besinci: 5, altinci: 6, yedinci: 7, sekizinci: 8, dokuzuncu: 9, onuncu: 10, onbirinci: 11, onikinci: 12,
    bes: 5, alti: 6, yedi: 7, sekiz: 8, dokuz: 9, on: 10, onbir: 11, oniki: 12 };

  // Ek kısaltma ve eş anlamlılar (dersler.json adları kendiliğinden eklenir).
  const DERS_ES = {
    turkce: ['turkce', 'trk'],
    matematik: ['mat', 'matematik', 'math', 'maths'],
    'fen-bilimleri': ['fen', 'fen bilimleri', 'fen bilgisi', 'fen ve teknoloji'],
    'sosyal-bilgiler': ['sosyal', 'sos', 'sb', 'sosyal bilgiler', 'sosyal bilgisi'],
    ingilizce: ['ingilizce', 'ing', 'english', 'yabanci dil'],
    'din-kulturu-ve-ahlak-bilgisi': ['din', 'din kulturu', 'dkab', 'din dersi', 'ahlak bilgisi'],
    'tc-inkilap-tarihi-ve-ataturkculuk': ['inkilap', 'ink', 'inkilap tarihi', 'ataturkculuk', 'tc inkilap', 'inkilap tarihi ve ataturkculuk'],
    'turk-dili-ve-edebiyati': ['edebiyat', 'edb', 'tde', 'turk dili', 'turk edebiyati', 'turk dili ve edebiyati'],
    fizik: ['fizik', 'fzk'],
    kimya: ['kimya', 'kmy'],
    biyoloji: ['biyo', 'biyoloji', 'bio'],
    tarih: ['tarih', 'trh'],
    cografya: ['cog', 'cografya'],
    felsefe: ['felsefe', 'fls'],
    'kuran-i-kerim': ['kuran', 'kuran i kerim', 'kurani kerim', 'kuranikerim'],
    'peygamberimizin-hayati': ['peygamber', 'peygamberimizin hayati', 'peygamberin hayati'],
    'temel-dini-bilgiler': ['temel dini bilgiler', 'tdb', 'dini bilgiler'],
    'hitabet-ve-mesleki-uygulama': ['hitabet'],
    'islam-kultur-ve-medeniyeti': ['islam kultur', 'islam medeniyeti', 'islam kultur ve medeniyeti'],
  };
  // Sınıfta bulunmayan ders istenirse o sınıftaki karşılığı (8 ve 12'de tarih = inkılap tarihi).
  const ESDEGER = { tarih: ['tc-inkilap-tarihi-ve-ataturkculuk'], arapca: ['mesleki-arapca'], 'mesleki-arapca': ['arapca'],
    'turk-dili-ve-edebiyati': ['turkce'], turkce: ['turk-dili-ve-edebiyati'], 'fen-bilimleri': ['fizik', 'kimya', 'biyoloji'],
    'sosyal-bilgiler': ['tarih', 'cografya'] };

  const PLANLAR = ['Yıllık plan', 'Ders planı'];
  // Tür ve konu niyetleri. baslikta: başlığında bu öbek geçen belge de niyeti karşılar.
  const NIYET = [
    { ad: 'Yıllık plan', ob: ['yillik plan', 'yillik', 'senelik plan', 'cerceve plan', 'cerceve yillik plan', 'unitelendirilmis plan'], tur: 'Yıllık plan', grup: 'plan' },
    { ad: 'Günlük plan', ob: ['gunluk plan', 'gunluk', 'ders plani', 'haftalik plan', 'gunluk ders plani'], tur: 'Ders planı' },
    { ad: 'Plan', ob: ['plan'], turler: PLANLAR, grup: 'plan' },
    { ad: 'Öğretim programı', ob: ['ogretim programi', 'mufredat', 'kazanim', 'ogrenme ciktisi', 'ogrenme ciktilari', 'program'], tur: 'Öğretim programı' },
    { ad: 'Konu anlatımı', ob: ['konu anlatimi', 'konu anlatim', 'anlatim', 'konu ozeti', 'ozet'], tur: 'Konu anlatımı' },
    { ad: 'Soru çözümü', ob: ['soru cozumu', 'cozum', 'cozumlu'], tur: 'Soru çözümü' },
    { ad: 'Video', ob: ['video', 'youtube'], tur: 'Video' },
    { ad: 'Test', ob: ['test', 'deneme'], tur: 'Test' },
    { ad: 'Çalışma kâğıdı', ob: ['calisma kagidi', 'etkinlik kagidi'], tur: 'Çalışma kâğıdı' },
    { ad: 'Ortak yazılı', ob: ['ortak yazili', 'yazili', 'konu soru dagilim', 'soru dagilim', 'konu soru dagilimi', 'dagilim tablosu', 'senaryo'], grup: 'yazili', turler: ['Yazılı soruları', 'Yazılı senaryosu'] },
    { ad: 'LGS', ob: ['lgs', 'liselere gecis', 'liseye gecis', 'lise sinavi', 'merkezi sinav'], grup: 'lgs', sinif: 8 },
    { ad: 'YKS', ob: ['yks', 'tyt', 'ayt', 'ydt', 'universite sinavi', 'osym'], grup: 'yks', siniflar: [11, 12] },
    { ad: 'Sınav', ob: ['sinav', 'sinavlar'], gruplar: ['lgs', 'yks', 'yazili'] },
    { ad: 'Sınav takvimi', ob: ['sinav takvimi', 'sinav tarihi', 'sinav tarihleri', 'sinavlar ne zaman'], ozel: 'sinav-takvim' },
    { ad: 'Okul takvimi', ob: ['takvim', 'calisma takvimi', 'okul takvimi', 'tatil', 'ara tatil', 'yariyil', 'yariyil tatili', 'somestr', 'karne',
      'okullar ne zaman', 'okul ne zaman', 'egitim ogretim takvimi', 'egitim ogretim yili takvimi', 'okullar acilis'], ozel: 'okul-takvim' },
    { ad: 'Kılavuz', ob: ['kilavuz', 'klavuz', 'rehber'], grup: 'kilavuz' },
    { ad: 'Ortaokul', ob: ['ortaokul', 'temel egitim', 'imam hatip ortaokulu'], kademe: [5, 6, 7, 8] },
    { ad: 'Lise', ob: ['lise', 'ortaogretim', 'anadolu lisesi'], kademe: [9, 10, 11, 12] },
    { ad: 'Öğretmen', ob: ['ogretmen', 'zumre'], kitle: 'ogretmen' },
    { ad: 'Öğrenci', ob: ['ogrenci'], kitle: 'ogrenci' },
    { ad: 'Veli', ob: ['veli', 'veli bilgilendirme'], kitle: 'ogrenci', ipucu: true },
  ];

  // ---------- dizin ----------
  let DIZIN = null;

  function kayit(o) {
    o.a = { baslik: kelimeler(o.baslik), diger: kelimeler([o.aciklama, o.dersAd, o.tur, o.kaynak, o.grupAd, o.ek].filter(Boolean).join(' ')) };
    return o;
  }
  const kademedenSinif = (metin) => (/temel egitim|ortaokul/.test(duz(metin)) ? [5, 6, 7, 8] : /ortaogretim|lise/.test(duz(metin)) ? [9, 10, 11, 12] : null);

  function kur({ dersler, icerikler = [], belgeler = null }) {
    KOK.clear();
    const dAd = dersler?.dersler || {};
    const siniflar = dersler?.siniflar || {};
    const secmeli = dersler?.secmeli || {};
    const sinifDersleri = {};
    const dersSira = {};
    for (const n of Object.keys(siniflar)) {
      sinifDersleri[n] = [...siniflar[n], ...(secmeli[n] || [])];
      siniflar[n].forEach((d, i) => { dersSira[d] = Math.min(dersSira[d] ?? 99, i); });
      (secmeli[n] || []).forEach((d, i) => { dersSira[d] = Math.min(dersSira[d] ?? 99, 50 + i); });
    }
    const kayitlar = [];
    const ekle = (o) => kayitlar.push(kayit(o));

    // Sayfalar
    ekle({ tip: 'sayfa', baslik: 'İçerikler', aciklama: 'Bütün içerikler: sınıf, ders ve türe göre süzün.', adres: '/icerikler.html', ek: 'kutuphane liste' });
    ekle({ tip: 'sayfa', baslik: 'Resmî belgeler', aciklama: 'Öğretim programları, kılavuzlar, ortak yazılı tabloları, LGS ve YKS belgeleri.', adres: '/belgeler.html', ek: 'meb odsgm dogm osym resmi' });
    ekle({ tip: 'sayfa', baslik: 'Günlük planlar', aciklama: 'Okul, öğretmen ve yönetici adları her sayfaya yazılı günlük ders planları; tüm yıl ya da aylık, Word veya PDF.', adres: '/planlar.html', kitle: 'ogretmen', ek: 'ogretmen', tur: 'Ders planı' });
    ekle({ tip: 'sayfa', baslik: 'Öğretmen köşesi', aciklama: 'Yıllık planlar, günlük planlar, yazılı soruları ve çalışma kâğıtları.', adres: '/icerikler.html?kitle=ogretmen', kitle: 'ogretmen', ek: 'ogretmen' });
    ekle({ tip: 'sayfa', baslik: 'İletişim', aciklama: 'Bize e-posta ve sosyal medyadan ulaşın.', adres: '/#iletisim', ek: 'iletisim eposta mail adres' });
    ekle({ tip: 'sayfa', baslik: 'Gizlilik ve çerezler', aciklama: 'Kişisel veriler ve çerez tercihleri.', adres: '/gizlilik.html', ek: 'kvkk cerez gizlilik' });
    ekle({ tip: 'sayfa', alt: 'sinav', baslik: 'Sınavlar: LGS ve YKS', aciklama: 'LGS ve YKS oturumları, testler, soru sayıları ve süreler; çıkmış sorular ve kılavuzlar.', adres: '/sinav.html', ek: 'lgs yks tyt ayt ydt sinav' });
    ekle({ tip: 'sayfa', baslik: 'Akıllı tahta', aciklama: 'Kalem, fosforlu kalem, silgi; kareli, çizgili zemin. Sayfaların ve PDF’lerin üzerine de yazılabilir.', adres: '/tahta.html', ek: 'tahta kalem cizim yazi beyaz tahta akilli tahta' });
    ekle({ tip: 'sayfa', baslik: 'Katkıda bulun', aciklama: 'Hata bildirin, içerik önerin, paylaşın, materyal gönderin.', adres: '/katki.html', ek: 'katki destek yardim hata oneri materyal gonder' });
    ekle({ tip: 'sayfa', baslik: 'Sosyal medya', aciklama: 'YouTube, Instagram ve Facebook hesaplarımız.', adres: '/#sosyal', ek: 'youtube instagram facebook takip' });
    for (const n of Object.keys(siniflar)) {
      const no = Number(n);
      ekle({ tip: 'sayfa', alt: 'sinif', baslik: `${no}. sınıf`, aciklama: `${no <= 8 ? 'Ortaokul' : 'Lise'} ${no}. sınıfın bütün dersleri.`, adres: `/sinif.html?no=${no}`, sinif: no });
      for (const d of sinifDersleri[n]) {
        ekle({ tip: 'sayfa', alt: 'ders', baslik: `${no}. sınıf ${dAd[d]}`, aciklama: `${no}. sınıf ${dAd[d]} dersinin bütün içerikleri.`, adres: `/icerikler.html?sinif=${no}&ders=${d}`, sinif: no, ders: d });
      }
    }
    for (const [d, ad] of Object.entries(dAd)) {
      ekle({ tip: 'sayfa', alt: 'ders-tum', baslik: `${ad} (bütün sınıflar)`, aciklama: `${ad} dersinin bütün sınıflardaki içerikleri.`, adres: `/icerikler.html?ders=${d}`, ders: d });
    }
    // İçerikler
    for (const i of icerikler) {
      ekle({ tip: 'icerik', baslik: i.baslik, aciklama: i.aciklama, adres: i.hazirla ? `/${i.hazirla}` : i.dosya ? `/${i.dosya}` : i.baglanti, dosya: !!i.dosya && !i.hazirla,
        dis: !i.dosya && /^https?:/.test(i.baglanti || ''), sinif: i.sinif ? Number(i.sinif) : null, ders: i.ders, dersAd: dAd[i.ders],
        goruntule: i.goruntule ? `/${i.goruntule}` : null, tur: i.tur, kitle: i.kitle, kaynak: i.kaynak, tarih: i.tarih });
    }
    // Resmî belgeler
    for (const g of belgeler?.gruplar || []) {
      for (const b of g.belgeler) {
        const kademe = b.kademe ? kademedenSinif(b.kademe) : g.kimlik === 'kilavuz' ? kademedenSinif(b.baslik) : null;
        ekle({ tip: 'belge', baslik: b.baslik, aciklama: b.aciklama, adres: b.dosya ? `/${b.dosya}` : b.baglanti, dosya: !!b.dosya,
          dis: !b.dosya, goruntule: b.goruntule ? `/${b.goruntule}` : null, grup: g.kimlik, grupAd: g.ad, ders: b.ders || null, dersAd: dAd[b.ders],
          sinif: b.sinif || null, siniflar: b.sinif ? [b.sinif] : g.kimlik === 'yks' ? [11, 12] : kademe,
          tur: g.kimlik === 'program' ? 'Öğretim programı' : 'Resmî belge', kitle: b.kitle, kaynak: b.kaynak, kademe: b.kademe });
      }
    }
    for (const k of kayitlar) k.sira = dersSira[k.ders] ?? 99;

    // Öbek listeleri
    const dersOb = [];
    for (const [d, ad] of Object.entries(dAd)) {
      const obekler = new Set([kelimeler(ad).join(' '), kelimeler(d.replace(/-/g, ' ')).join(' '), ...(DERS_ES[d] || [])]);
      for (const o of obekler) dersOb.push({ ob: o.split(' '), ders: d });
    }
    const niyetOb = NIYET.flatMap((n) => n.ob.map((o) => ({ ob: o.split(' '), niyet: n })));
    const sozluk = new Set();
    for (const b of kayitlar) for (const k of [...b.a.baslik, ...b.a.diger]) sozluk.add(k);
    for (const x of [...dersOb, ...niyetOb]) for (const k of x.ob) sozluk.add(k);
    DIZIN = { kayitlar, dersOb, niyetOb, sozluk: [...sozluk].filter((k) => k.length >= 3 && !/^\d+$/.test(k)), dAd, sinifDersleri };
    return DIZIN;
  }

  // ---------- sorgu çözümleme ----------
  // ks[bas…] ile başlayan en uzun öbek. Kelime eşleşmesi: tam 1, ekli 0.9, yazarken önek 0.75, yazım hatası 0.6 (düzeltme sayılır).
  function obekBul(ks, liste, bas, yaziyor) {
    let en = null;
    for (const x of liste) {
      const u = x.ob.length;
      const kalan = ks.length - bas;
      // Yazarken sorgu öbeğin ortasında bitebilir ("ogretim p" → "ogretim programi").
      const kismi = u > kalan;
      if (kismi && !yaziyor) continue;
      const bak = Math.min(u, kalan);
      let tamam = true, puan = 0, hata = false;
      for (let j = 0; j < bak; j++) {
        const q = ks[bas + j], k = x.ob[j];
        const son = yaziyor && bas + j === ks.length - 1;
        let e = 0;
        if (q === k) e = 1;
        else if (ekli(q, k) && (k.length >= 3 || EKLER.has(q.slice(k.length)))) e = 0.9;
        else if (son && k.startsWith(q) && (q.length >= 2 || j > 0)) e = 0.75;
        else {
          const s = hataSiniri(Math.min(q.length, k.length));
          if (s && uzaklik(q, k, s) <= s) { e = 0.6; hata = true; }
        }
        if (!e) { tamam = false; break; }
        puan += e;
      }
      if (!tamam) continue;
      if (kismi) puan *= 0.9;
      if (!en || bak > en.u || (bak === en.u && puan > en.puan)) en = { ...x, u: bak, puan, hata };
    }
    return en;
  }

  function cozumle(sorgu, { yaziyor = false } = {}) {
    const ks = kelimeler(sorgu);
    const s = { ham: sorgu, sinif: null, sinifDisi: null, kademe: null, dersler: [], niyetler: [], kitle: null, ipucu: [], serbest: [], duzeltmeler: [] };
    const baglam = new Set(ks);
    for (let i = 0; i < ks.length;) {
      const q = ks[i];
      const son = yaziyor && i === ks.length - 1;
      // Sınıf: "8", "8. sınıf", "8.sınıfta", "sekizinci sınıf", "on birinci sınıf", "lise 2"
      if (/^\d{1,2}$/.test(q)) {
        const n = +q;
        const sonraki = ks[i + 1] || '';
        if (n >= 5 && n <= 12) { s.sinif = n; i++; while (i < ks.length && sinifKelimesi(ks[i])) i++; continue; }
        if (sinifKelimesi(sonraki) || n < 5 || n > 12) {
          if (sinifKelimesi(sonraki) || n <= 13) { s.sinifDisi = n; i++; while (i < ks.length && sinifKelimesi(ks[i])) i++; continue; }
        }
      }
      if (q === 'on' && ['birinci', 'ikinci', 'bir', 'iki'].includes(ks[i + 1])) { s.sinif = ks[i + 1].startsWith('bir') ? 11 : 12; i += 2; while (i < ks.length && sinifKelimesi(ks[i])) i++; continue; }
      if (SAYI[q] && (sinifKelimesi(ks[i + 1] || '') || /(inci|nci|uncu|ncu)$/.test(q))) { s.sinif = SAYI[q]; i++; while (i < ks.length && sinifKelimesi(ks[i])) i++; continue; }
      if ((q === 'lise' || q === 'lisesi') && /^[1-4]$/.test(ks[i + 1] || '')) { s.sinif = 8 + +ks[i + 1]; i += 2; while (i < ks.length && sinifKelimesi(ks[i])) i++; continue; }
      if (sinifKelimesi(q) && !son) { i++; continue; }
      // "sınav tarihi", "lgs tarihi": tarih burada ders değil.
      if (/^tarih(i|leri)$/.test(q) && ['sinav', 'tatil', 'karne', 'lgs', 'yks', 'tyt', 'ayt', 'yariyil', 'okul', 'okullar', 'takvim'].some((k) => baglam.has(k))) { i++; continue; }
      const d = obekBul(ks, DIZIN.dersOb, i, yaziyor);
      const n = obekBul(ks, DIZIN.niyetOb, i, yaziyor);
      // Aynı yerde ikisi de eşleşirse uzun ve tam olan kazanır ("temel dini bilgiler" > "din").
      const secilen = [d, n].filter(Boolean).sort((a, b) => b.u - a.u || b.puan - a.puan)[0];
      if (secilen && (secilen.ders || !DURAK.has(q) || secilen.u > 1 || son)) {
        const kaynak = ks.slice(i, i + secilen.u).join(' ');
        if (secilen.ders) { if (!s.dersler.includes(secilen.ders)) s.dersler.push(secilen.ders); }
        else if (secilen.niyet.kademe) s.kademe = secilen.niyet.kademe;
        else if (secilen.niyet.kitle) { s.kitle = secilen.niyet.kitle; if (secilen.niyet.ipucu) s.ipucu.push(...ks.slice(i, i + secilen.u)); }
        else if (!s.niyetler.includes(secilen.niyet)) s.niyetler.push(secilen.niyet);
        if (secilen.hata) s.duzeltmeler.push([kaynak, secilen.ob.slice(0, secilen.u).join(' ')]);
        i += secilen.u;
        continue;
      }
      if (!DURAK.has(q) && !(q.length === 1 && !/\d/.test(q))) s.serbest.push(q);
      i++;
    }
    // Daha belirgin bir niyet varsa genel olanı at ("yıllık plan" > "plan", "sınav takvimi" > "sınav").
    if (s.niyetler.some((n) => PLANLAR.includes(n.tur))) s.niyetler = s.niyetler.filter((n) => n.ad !== 'Plan');
    if (s.niyetler.some((n) => n.ozel === 'sinav-takvim' || n.grup === 'lgs' || n.grup === 'yks' || n.grup === 'yazili')) s.niyetler = s.niyetler.filter((n) => n.ad !== 'Sınav');
    if (s.sinif && s.kademe && !s.kademe.includes(s.sinif)) s.kademe = null;
    // Sınıfta bulunmayan ders → o sınıftaki karşılığı ("8. sınıf tarih" → inkılap tarihi).
    if (s.sinif) {
      const buSinif = DIZIN.sinifDersleri[s.sinif] || [];
      s.dersler = [...new Set(s.dersler.map((d) => (buSinif.includes(d) ? d : (ESDEGER[d] || []).find((e) => buSinif.includes(e)) || d)))];
    }
    return s;
  }

  // ---------- puanlama ----------
  const takvimMi = (b) => /takvim/.test(duz(b.baslik));
  function niyetKarsilar(b, n) {
    if (n.tur && b.tur === n.tur) return true;
    if (n.turler && n.turler.includes(b.tur)) return true;
    if (n.grup && b.grup === n.grup && !(n.grup === 'plan' && takvimMi(b))) return true;
    if (n.gruplar && n.gruplar.includes(b.grup)) return true;
    if (n.ozel === 'okul-takvim') return takvimMi(b) && /egitim ogretim/.test(duz(b.baslik));
    if (n.ozel === 'sinav-takvim') return takvimMi(b) && /sinav/.test(duz(b.baslik));
    // Başlığında niyet öbeği geçen belge (ör. "Okul temelli planlama", "YKS Kılavuzu")
    return n.ob.some((o) => { const ok = o.split(' '); return ok.every((w) => b.a.baslik.some((k) => k === w || ekli(k, w))); });
  }
  const turNiyetleri = (s) => s.niyetler.filter((n) => n.tur || n.turler || n.grup || n.gruplar || n.ozel);

  function sinifUyar(b, sinifler) {
    if (!sinifler) return 0;
    if (b.sinif) return sinifler.includes(b.sinif) ? 2 : -1;
    if (b.siniflar) return b.siniflar.some((x) => sinifler.includes(x)) ? 1 : -1;
    return 0;
  }

  function terimPuani(b, terimler, yaziyor) {
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
    const hedefSinif = s.sinif ? [s.sinif] : s.kademe;
    const ipucuSinif = s.niyetler.find((n) => n.sinif)?.sinif;
    const ipucuSiniflar = ipucuSinif ? [ipucuSinif] : s.niyetler.find((n) => n.siniflar)?.siniflar;
    const turN = turNiyetleri(s);
    const grupVar = s.niyetler.some((n) => n.grup && n.grup !== 'plan' || n.gruplar || n.ozel);
    const sonuc = [];
    for (const b of DIZIN.kayitlar) {
      let p = 0;
      if (b.tip === 'sayfa' && b.alt) {
        // Sayfa kısayolları yalnız sınıf/ders sorulunca.
        if (b.alt === 'sinif' && !(s.sinif && !s.dersler.length && b.sinif === s.sinif)) continue;
        if (b.alt === 'ders' && !(s.dersler.includes(b.ders) && s.sinif === b.sinif)) continue;
        if (b.alt === 'ders-tum' && !(s.dersler.includes(b.ders) && !s.sinif)) continue;
        if (b.alt === 'sinav') { if (!s.niyetler.some((n) => n.grup === 'lgs' || n.grup === 'yks' || n.ad === 'Sınav')) continue; p += 45; sonuc.push({ b, p }); continue; }
        p += grupVar ? 15 : s.niyetler.length ? 35 : 60;
      } else if (b.tip === 'sayfa') {
        const { toplam, bulunan } = terimPuani(b, [...s.serbest, ...s.ipucu], yaziyor);
        if (!bulunan) continue;
        p += toplam;
      } else {
        const karsilanan = turN.filter((n) => niyetKarsilar(b, n)).length;
        if (kural.tur && turN.length && !karsilanan) continue;
        p += karsilanan * 20;
        if (kural.ders && s.dersler.length) {
          if (b.ders && !s.dersler.includes(b.ders)) continue;
          if (b.ders) p += 30;
          else {
            // Dersi olmayan belge: yalnız sınav/grup niyetiyle ya da serbest kelimeyle gelir; ders adı metinde geçerse artı.
            if (!grupVar && !s.serbest.length) continue;
            if (s.dersler.some((d) => kelimeler(DIZIN.dAd[d]).every((w) => [...b.a.baslik, ...b.a.diger].some((k) => ekli(k, w))))) p += 12;
          }
        }
        if (kural.sinif && hedefSinif) {
          const u = sinifUyar(b, hedefSinif);
          if (u < 0) continue;
          p += u * (s.sinif ? 12 : 6);
        } else if (hedefSinif || ipucuSiniflar) p += Math.max(0, sinifUyar(b, hedefSinif || ipucuSiniflar)) * 4;
        if (!hedefSinif && ipucuSiniflar && sinifUyar(b, ipucuSiniflar) > 0) p += 6;
        if (s.kitle) p += b.kitle === s.kitle ? 8 : -4;
        if (s.ipucu.length) p += terimPuani(b, s.ipucu, yaziyor).toplam;
        if (s.serbest.length) {
          const { toplam, bulunan } = terimPuani(b, s.serbest, yaziyor);
          if (kural.hepsi && bulunan < s.serbest.length) continue;
          if (!bulunan && !s.dersler.length && !turN.length && !hedefSinif && !s.kitle) continue;
          p += toplam;
          if (bulunan === s.serbest.length && s.serbest.every((q) => b.a.baslik.some((k) => eslesme(q, k, false) >= 0.8))) p += 15;
        } else if (!s.dersler.length && !turN.length && !hedefSinif && !s.kitle) continue;
        if (p <= 0) continue;
      }
      sonuc.push({ b, p });
    }
    // Aynı adrese giden kayıtlardan yalnız en yüksek puanlı kalır (ör. 5–8. sınıfların ortak öğretim programı).
    const enIyi = new Map();
    for (const r of sonuc) { const e = enIyi.get(r.b.adres); if (!e || r.p > e.p || (r.p === e.p && r.b.tip === 'belge')) enIyi.set(r.b.adres, r); }
    return [...enIyi.values()].sort((x, y) => y.p - x.p
      || (x.b.tip === 'sayfa' ? 0 : 1) - (y.b.tip === 'sayfa' ? 0 : 1)
      || (x.b.sinif ?? 99) - (y.b.sinif ?? 99)
      || x.b.sira - y.b.sira
      || x.b.baslik.localeCompare(y.b.baslik, 'tr', { numeric: true }));
  }

  function ara(sorgu, { yaziyor = false } = {}) {
    if (!DIZIN) throw new Error('Arama dizini kurulmadı');
    const s = cozumle(sorgu, { yaziyor });
    const bos = !s.sinif && !s.kademe && !s.dersler.length && !s.niyetler.length && !s.kitle && !s.serbest.length;
    if (bos) {
      const not = s.sinifDisi ? `Sitede 5–12. sınıfların içerikleri var; ${s.sinifDisi}. sınıf yok.` : null;
      return { sorgu: s, sonuclar: [], not, anlasilan: [] };
    }
    const dersYok = !s.dersler.length;
    const sinifAdi = s.sinif ? 'sınıf' : 'kademe';
    // Gevşetme sırası: sınav niyeti (LGS/YKS) sınıf ipucu taşıdığı için önce sınıf gevşer; öteki durumlarda önce tür.
    const sinifOnce = s.niyetler.some((n) => n.sinif || n.siniflar || n.ozel);
    const turAdim = { kural: { tur: false, ders: true, sinif: true, hepsi: false },
      not: dersYok ? `İstediğiniz türde içerik yok; aynı ${sinifAdi}ın öteki içerikleri gösteriliyor.` : `İstediğiniz türde içerik yok; aynı ${s.sinif || s.kademe ? `${sinifAdi} ve ` : ''}dersin öteki içerikleri gösteriliyor.` };
    const sinifAdim = { kural: { tur: true, ders: true, sinif: false, hepsi: false }, not: `Bu ${sinifAdi} için sonuç yok; ilgili öteki sınıfların sonuçları gösteriliyor.` };
    const GEVSEME = [
      { kural: { tur: true, ders: true, sinif: true, hepsi: true }, not: null },
      { kural: { tur: true, ders: true, sinif: true, hepsi: false }, not: 'Bütün kelimeleri içeren sonuç yok; en yakın sonuçlar gösteriliyor.' },
      ...(sinifOnce ? [sinifAdim, turAdim] : [turAdim, sinifAdim]),
      { kural: { tur: false, ders: true, sinif: false, hepsi: false }, not: 'Tam eşleşme yok; dersin öteki sınıflardaki içerikleri gösteriliyor.' },
      { kural: { tur: false, ders: false, sinif: false, hepsi: false }, not: 'Tam eşleşme yok; ilgili olabilecek sonuçlar gösteriliyor.' },
    ];
    let sonuclar = [], not = null;
    for (const g of GEVSEME) {
      sonuclar = puanla(s, g.kural, yaziyor);
      const gercek = sonuclar.filter((r) => r.b.tip !== 'sayfa');
      if (gercek.length || (sonuclar.length && !turNiyetleri(s).length && !s.serbest.length)) { not = g.not; break; }
    }
    if (!sonuclar.some((r) => r.b.tip !== 'sayfa')) {
      const turAd = turNiyetleri(s).map((n) => n.ad).join(', ');
      if (turAd) not = `${turAd} türünde içerik henüz yok.`;
    }
    if (s.sinifDisi) not = [`Sitede 5–12. sınıfların içerikleri var; ${s.sinifDisi}. sınıf yok.`, not].filter(Boolean).join(' ');
    // Serbest kelimelerde yazım düzeltmesi: dizinde karşılığı yoksa en yakın kelime önerilir.
    for (const q of s.serbest) {
      if (q.length < 4 || DIZIN.sozluk.some((k) => eslesme(q, k, false) >= 0.8)) continue;
      const sinir = hataSiniri(q.length);
      let en = null, enD = sinir + 1;
      for (const k of DIZIN.sozluk) { const d = uzaklik(q, k, sinir); if (d < enD) { enD = d; en = k; } }
      if (en) s.duzeltmeler.push([q, en]);
    }
    const anlasilan = [
      s.sinif && { tur: 'sinif', ad: `${s.sinif}. sınıf` },
      !s.sinif && s.kademe && { tur: 'sinif', ad: s.kademe[0] === 5 ? 'Ortaokul (5–8)' : 'Lise (9–12)' },
      ...s.dersler.map((d) => ({ tur: 'ders', ad: DIZIN.dAd[d], deger: d })),
      ...s.niyetler.map((n) => ({ tur: 'niyet', ad: n.ad })),
      s.kitle && { tur: 'kitle', ad: s.ipucu.length ? 'Veli' : s.kitle === 'ogretmen' ? 'Öğretmen' : 'Öğrenci' },
    ].filter(Boolean);
    return { sorgu: s, sonuclar, not, anlasilan };
  }

  // Başlıkta eşleşen kelimeleri bul: [bas, son] aralıkları (özgün metin konumları).
  function vurgular(metin, sorgu) {
    const s = cozumle(sorgu);
    const terimler = [...s.serbest, ...s.ipucu, ...s.dersler.flatMap((d) => kelimeler(DIZIN.dAd[d]))];
    const d = duz(metin);
    const araliklar = [];
    const re = /[a-z0-9]+/g;
    let m;
    while ((m = re.exec(d))) {
      if (terimler.some((q) => eslesme(q, m[0], true) >= 0.7)) araliklar.push([m.index, m.index + m[0].length]);
    }
    return araliklar;
  }

  // Kütüphane süzgeci için akıllı eşleşme: bütün kelimeler (ekli ya da hatalı yazım dahil) metinde var mı?
  function metinEslesir(metin, sorgu) {
    const qs = kelimeler(sorgu).filter((q) => !DURAK.has(q));
    if (!qs.length) return true;
    const ks = kelimeler(metin);
    return qs.every((q, i) => ks.some((k) => eslesme(q, k, i === qs.length - 1) > 0));
  }

  return { duz, kelimeler, uzaklik, ekli, kur, cozumle, ara, vurgular, metinEslesir, dizin: () => DIZIN };
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
  const adres = (b) => b.goruntule || b.adres;
  const hedef = (b) => (b.goruntule ? {} : b.dis ? { target: '_blank', rel: 'noopener' } : b.dosya ? { download: '' } : {});

  // Üst menüdeki kutu: anlık öneriler
  const form = $('.ust-arama');
  if (form) {
    const kutu = $('input', form);
    if (matchMedia('(max-width: 560px)').matches) kutu.placeholder = 'Ara';
    const liste = $('.oneri', form);
    let secili = -1;
    const kapat = () => { liste.hidden = true; kutu.setAttribute('aria-expanded', 'false'); secili = -1; kutu.removeAttribute('aria-activedescendant'); };
    const isaretle = () => $$('li', liste).forEach((li, i) => { li.setAttribute('aria-selected', String(i === secili)); if (i === secili) li.scrollIntoView({ block: 'nearest' }); });
    let sira = 0;
    const goster = async () => {
      const q = kutu.value.trim();
      const benim = ++sira;
      if (q.length < 2) { kapat(); return; }
      await dizinHazirla();
      if (benim !== sira) return;   // eski yazım için gelen sonucu at
      const r = Arama.ara(q, { yaziyor: true });
      const ilk = r.sonuclar.slice(0, 7);
      const satirlar = ilk.map(({ b }, i) => el('li', { role: 'option', id: `oneri-${i}`, 'aria-selected': 'false' },
        el('a', { href: adres(b), tabindex: '-1', ...hedef(b) },
          el('span', { sinif: `oneri-tip ${b.tip}` }, TUR_ETIKET[b.tip]),
          el('span', { sinif: 'oneri-metin' }, el('strong', {}, ...vurgula(b.baslik, q)), el('small', {}, altBilgi(b))))));
      satirlar.push(el('li', { role: 'option', id: `oneri-${ilk.length}`, sinif: 'oneri-tumu', 'aria-selected': 'false' },
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
      if (o.key === 'ArrowDown' && n && !liste.hidden) { o.preventDefault(); secili = (secili + 1) % n; isaretle(); }
      else if (o.key === 'ArrowUp' && n && !liste.hidden) { o.preventDefault(); secili = (secili - 1 + n) % n; isaretle(); }
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
          el('h3', {}, el('a', { href: adres(b), ...hedef(b) }, ...vurgula(b.baslik, q))),
          b.aciklama && el('p', {}, b.aciklama),
          el('a', { sinif: 'ac', href: adres(b), ...hedef(b) }, b.goruntule ? 'Aç' : b.dosya ? 'İndir' : b.dis ? 'Aç' : 'Git', simge('ok')))));
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
