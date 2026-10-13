// Belge görüntüleyici: goruntule.html?b=<kimlik>[&s=<sayfa>][&yerel=1].
// PDF sitedeyse ya da kaynağı izin veriyorsa (CORS, ör. cdn.eba.gov.tr) sayfalar PDF.js (yerel kopya) ile burada çizilir;
// kalemle yazılanlar sayfa koordinatında tutulur, PDF kaydırılınca ve yakınlaştırılınca yazı da birlikte kayar/büyür.
// Öteki belgeler resmî adresinden çerçeve içinde açılır; kaynak buna da izin vermiyorsa (ör. ÖSYM) düğme gösterilir.
// 12.10.2026 (kullanıcı, öğrenci isteği): sayfa numarası yazılarak doğrudan gitme (kitaptaki basılı numara, sayfa
// altındaki numaralardan öğrenilir), son kalınan sayfanın bu tarayıcıda hatırlanması ve kitabın bilgisayardaki PDF
// dosyasından açılması (dosya hiçbir yere gönderilmez; internet beklenmez). &s=78 → 78. sayfa, &yerel=1 → dosya seçimi.

const PDF_CORS = /^https:\/\/cdn\.eba\.gov\.tr\/.+\.pdf(\?|$)/i;

(() => {
  const l = document.createElement('link');
  l.rel = 'stylesheet';
  l.href = '/goruntule.css?v=20261013-1';
  document.head.append(l);
})();

const KALDIGI = (k) => `dk-kitap-sayfa:${k}`;
const kaldigiOku = (k) => { try { return Number(localStorage.getItem(KALDIGI(k))) || 0; } catch { return 0; } };
const kaldigiYaz = (k, n) => { try { localStorage.setItem(KALDIGI(k), String(n)); } catch { /* özel pencere: hatırlanmaz */ } };

let etkin = null;       // gösterilen belge: { doc, gozcu }
let surum = 0;          // yeni bir açılış eskisini geçersiz kılar (internetten yüklenirken bilgisayardan açma)

// kaynak: adres (metin) ya da { veri: ArrayBuffer, ad } (bilgisayardan seçilen dosya)
async function pdfGoster(alan, kaynak, baslik, boyut, secenek = {}) {
  const benim = ++surum;
  if (etkin) { etkin.gozcu?.disconnect(); etkin.doc?.destroy?.(); etkin = null; }
  alan.classList.add('pdf-mod');
  const kaydir = el('div', { sinif: 'pdf-kaydir', tabindex: '0', 'aria-label': `${baslik} sayfaları` });
  const sayfalar = el('div', { sinif: 'pdf-sayfalar' });
  const bilgi = el('span', { sinif: 'pdf-no', 'aria-live': 'polite' }, 'Yükleniyor…');
  const giris = el('input', { type: 'text', inputmode: 'numeric', pattern: '[0-9]*', sinif: 'pdf-git-no', autocomplete: 'off',
    placeholder: 'Sayfa', 'aria-label': 'Gidilecek sayfa numarası', title: 'Sayfa numarasını yazıp Enter’a basın' });
  const form = el('form', { sinif: 'pdf-git', onsubmit: (e) => { e.preventDefault(); git(giris.value); } },
    giris, el('button', { type: 'submit', title: 'Sayfaya git' }, 'Git'));
  const devam = el('button', { type: 'button', sinif: 'pdf-devam', hidden: true });
  const arac = el('div', { sinif: 'pdf-arac' },
    el('button', { type: 'button', 'aria-label': 'Küçült', title: 'Küçült', onclick: () => yakinlas(1 / 1.2) }, '−'),
    el('button', { type: 'button', 'aria-label': 'Sayfaya sığdır', title: 'Sığdır', onclick: () => yakinlas(0) }, '↔'),
    el('button', { type: 'button', 'aria-label': 'Büyüt', title: 'Büyüt', onclick: () => yakinlas(1.2) }, '+'),
    bilgi, form, devam);
  kaydir.append(sayfalar);
  alan.replaceChildren(kaydir, arac);
  form.hidden = true;

  // İnternet yavaşsa birkaç saniye sonra bilgisayardan açma önerilir.
  const yavas = !kaynak.veri && secenek.yerelDugme ? setTimeout(() => {
    if (benim === surum) sayfalar.append(el('div', { sinif: 'pdf-yavas', role: 'status' },
      el('p', {}, 'Kitap internetten yükleniyor. Bağlantı yavaşsa kitabın PDF dosyası bilgisayarınızdaysa oradan açabilirsiniz.'),
      secenek.yerelDugme()));
  }, 3000) : null;

  let doc;
  try {
    const pdfjs = await import('/kutuphane/pdfjs/pdf.min.js');
    pdfjs.GlobalWorkerOptions.workerSrc = '/kutuphane/pdfjs/pdf.worker.min.js';
    const PARCA = 262144;
    if (kaynak.veri) {
      doc = await pdfjs.getDocument({ data: new Uint8Array(kaynak.veri), isEvalSupported: false }).promise;
    } else if (boyut && !kaynak.startsWith('/')) {
      // MEB sunucusu Content-Length / Accept-Ranges başlıklarını tarayıcıya açmıyor: parçalar Range isteğiyle bizden gider,
      // böylece 150 MB'lık kitabın yalnız görüntülenen sayfaları iner.
      const oku = (bas, son) => fetch(kaynak, { headers: { Range: `bytes=${bas}-${son - 1}` } }).then((y) => {
        if (y.status !== 206) throw new Error('parça okunamadı');
        return y.arrayBuffer();
      });
      const tasima = new pdfjs.PDFDataRangeTransport(boyut, new Uint8Array(await oku(0, Math.min(PARCA, boyut))));
      tasima.requestDataRange = (bas, son) => { oku(bas, son).then((v) => tasima.onDataRange(bas, new Uint8Array(v))); };
      doc = await pdfjs.getDocument({ range: tasima, rangeChunkSize: PARCA, disableAutoFetch: true, isEvalSupported: false }).promise;
    } else {
      doc = await pdfjs.getDocument({ url: kaynak, rangeChunkSize: PARCA, disableAutoFetch: true, isEvalSupported: false }).promise;
    }
  } catch (e) {
    clearTimeout(yavas);
    return benim === surum ? false : 'iptal';     // false: çizilemedi, çağıran çerçeveye döner
  }
  clearTimeout(yavas);
  if (benim !== surum) { doc.destroy(); return 'iptal'; }
  const oran = Math.min(window.devicePixelRatio || 1, 2);
  const ilk = (await doc.getPage(1)).getViewport({ scale: 1 });
  if (benim !== surum) { doc.destroy(); return 'iptal'; }
  let olcek = 1;
  const genislik = () => Math.round(Math.min(kaydir.clientWidth - 24, 1100) * olcek);
  const kutular = [];
  for (let i = 1; i <= doc.numPages; i++) {
    const kutu = el('div', { sinif: 'pdf-sayfa', 'data-no': i }, el('canvas', {}));
    kutu.oran = ilk.height / ilk.width;
    kutular.push(kutu);
  }
  sayfalar.replaceChildren(...kutular);
  const boyutla = () => { const g = genislik(); for (const k of kutular) { k.style.width = g + 'px'; k.style.height = Math.round(g * k.oran) + 'px'; } };
  boyutla();

  // Kitaptaki basılı sayfa numarası ile PDF sırası arasındaki fark: çizilen sayfaların alt/üst kenarındaki
  // numaralardan öğrenilir; iki ayrı sayfa aynı farkı verince kesinleşir.
  const ornek = new Map(), bakilan = new Set();
  let kayma = null, bekleyen = null, bekleyenSaat = null;
  const kaymaOgren = async (sayfa, no) => {
    if (kayma !== null || bakilan.has(no)) return;
    bakilan.add(no);
    try {
      const h = sayfa.getViewport({ scale: 1 }).height;
      const metin = await sayfa.getTextContent();
      for (const p of metin.items) {
        const s = (p.str || '').trim();
        const y = p.transform?.[5];
        if (!/^\d{1,3}$/.test(s) || y == null || (y > h * 0.08 && y < h * 0.93)) continue;
        const k = no - Number(s);
        if (k < 0 || k > 60) continue;
        ornek.set(k, (ornek.get(k) || 0) + 1);
        if (ornek.get(k) >= 2) {
          kayma = k;
          noYaz();
          if (bekleyen != null) { const b = bekleyen; bekleyen = null; clearTimeout(bekleyenSaat); git(String(b), true); }
        }
        break;
      }
    } catch { /* metin okunamadı: PDF sırası kullanılır */ }
  };

  // Tembel çizim: yalnız görünen ve yakınındaki sayfalar; uzaklaşan sayfa kuyruktan çıkar, tuvali boşaltılır (bellek).
  // (Eskiden kaydırırken geçilen her sayfa kuyrukta kalıyordu: 78. sayfa önceki sayfaların inmesini bekliyordu.)
  const cizilen = new Map(), sira = [];
  let calisan = 0;
  const ciz = async (kutu) => {
    const g = genislik();
    if (cizilen.get(kutu) === g) return;
    cizilen.set(kutu, g);
    const no = Number(kutu.dataset.no);
    const sayfa = await doc.getPage(no);
    const v1 = sayfa.getViewport({ scale: 1 });
    kutu.oran = v1.height / v1.width;
    kutu.style.height = Math.round(g * kutu.oran) + 'px';
    const vp = sayfa.getViewport({ scale: (g / v1.width) * oran });
    const tuval = document.createElement('canvas');
    tuval.width = Math.floor(vp.width); tuval.height = Math.floor(vp.height);
    await sayfa.render({ canvasContext: tuval.getContext('2d', { alpha: false }), viewport: vp }).promise;
    if (cizilen.get(kutu) === g) kutu.replaceChildren(tuval);
    kaymaOgren(sayfa, no);
  };
  const kuyruk = () => {
    while (calisan < 2 && sira.length) {
      const k = sira.shift();
      calisan++;
      ciz(k).catch(() => cizilen.delete(k)).finally(() => { calisan--; kuyruk(); });
    }
  };
  const gozcu = new IntersectionObserver((kayitlar) => {
    for (const k of kayitlar) {
      if (k.isIntersecting) { if (!sira.includes(k.target)) sira.push(k.target); }
      else {
        const i = sira.indexOf(k.target);
        if (i >= 0) sira.splice(i, 1);
        if (cizilen.has(k.target)) { cizilen.delete(k.target); k.target.replaceChildren(el('canvas', {})); }
      }
    }
    kuyruk();
  }, { root: kaydir, rootMargin: '1500px 0px' });
  kutular.forEach((k) => gozcu.observe(k));

  const simdiki = () => {
    const orta = kaydir.scrollTop + kaydir.clientHeight / 3;
    return kutular.findIndex((k) => k.offsetTop + k.offsetHeight > orta) + 1 || kutular.length;
  };
  let kaydet = null;
  const noYaz = () => {
    const n = simdiki();
    const basili = kayma !== null && n - kayma >= 1 ? n - kayma : null;
    bilgi.textContent = basili ? `Sayfa ${basili} · ${n}/${doc.numPages}` : `Sayfa ${n} / ${doc.numPages}`;
    bilgi.title = basili ? 'Kitaptaki sayfa numarası · PDF içindeki sıra / toplam' : 'PDF içindeki sıra / toplam';
    if (secenek.kimlik) { clearTimeout(kaydet); kaydet = setTimeout(() => { if (n > 1) kaldigiYaz(secenek.kimlik, n); }, 800); }
  };
  kaydir.addEventListener('scroll', noYaz, { passive: true });

  const konumla = (n) => {
    const kutu = kutular[Math.max(1, Math.min(doc.numPages, n)) - 1];
    kaydir.scrollTop = kutu.offsetTop - 10;
    noYaz();
  };
  // Yazılan numara kitaptaki basılı numaradır; fark henüz öğrenilmediyse önce PDF sırasına gidilir,
  // fark birkaç saniye içinde öğrenilirse doğru sayfaya düzeltilir.
  function git(deger, ogrenildi = false) {
    const sayi = parseInt(String(deger).replace(/\D/g, ''), 10);
    if (!sayi) { giris.focus(); return; }
    if (kayma === null && !ogrenildi) {
      bekleyen = sayi;
      clearTimeout(bekleyenSaat);
      bekleyenSaat = setTimeout(() => { bekleyen = null; }, 10000);
    }
    konumla(sayi + (kayma ?? 0));
    giris.value = '';
    kaydir.focus({ preventScroll: true });
  }
  for (const ad of ['wheel', 'touchmove', 'keydown']) kaydir.addEventListener(ad, () => { bekleyen = null; }, { passive: true });

  form.hidden = false;
  noYaz();
  const kaldigi = secenek.kimlik ? kaldigiOku(secenek.kimlik) : 0;
  if (secenek.sayfa) git(secenek.sayfa);
  else if (kaldigi > 1 && kaldigi <= doc.numPages) {
    devam.hidden = false;
    devam.textContent = `Kaldığın yer (${kaldigi}/${doc.numPages})`;
    devam.title = 'Bu tarayıcıda en son bakılan sayfaya git';
    devam.addEventListener('click', () => { konumla(kaldigi); devam.hidden = true; });
    kaydir.addEventListener('scroll', () => { if (simdiki() === kaldigi) devam.hidden = true; }, { passive: true });
  }

  function yakinlas(k) {
    const eski = genislik();
    olcek = k === 0 ? 1 : Math.max(0.5, Math.min(3, olcek * k));
    boyutla();
    const yeni = genislik(), r = yeni / eski;
    kaydir.scrollTop *= r; kaydir.scrollLeft *= r;
    window.kalemAcik?.olcekle(r);       // yazılar sayfayla birlikte büyür/küçülür
    for (const kutu of kutular) if (cizilen.has(kutu)) { cizilen.delete(kutu); if (!sira.includes(kutu)) sira.push(kutu); }
    kuyruk();
  }
  let enOnce = kaydir.clientWidth;
  new ResizeObserver(() => { if (Math.abs(kaydir.clientWidth - enOnce) > 20) { enOnce = kaydir.clientWidth; yakinlas(1); } }).observe(kaydir);

  etkin = { doc, gozcu };
  // Kalem bu kaba bağlanır: yazı PDF sayfalarıyla birlikte kayar.
  window.kalemHedef = { kap: alan, kaydir };
  return true;
}

veri('belgeler.json').then(async (belgeler) => {
  const ara = new URLSearchParams(location.search);
  const id = ara.get('b');
  let grup = null;
  const b = belgeler?.gruplar.flatMap((g) => g.belgeler.map((x) => ((x.kimlik === id && (grup = g)), x))).find((x) => x.kimlik === id);
  if (!b) {
    $('#g-baslik').textContent = 'Belge bulunamadı';
    $('#g-alan').replaceChildren(el('div', { sinif: 'g-uyari' }, el('p', {}, 'Aradığınız belge listede yok. '), el('a', { sinif: 'dugme ana', href: '/belgeler.html' }, 'Resmî belgelere dön')));
    return;
  }
  document.title = `${b.baslik} · Ders Kutusu`;
  $('#g-baslik').textContent = b.baslik;
  const bilgiMetni = [grup?.ad, b.kaynak, b.aciklama].filter(Boolean).join(' · ');
  $('#g-bilgi').textContent = bilgiMetni;
  const resmi = b.kaynak_adres || b.baglanti;
  const alan = $('#g-alan');
  const pdf = b.dosya?.endsWith('.pdf') ? `/${b.dosya}` : PDF_CORS.test(b.baglanti || '') ? b.baglanti : null;
  const uzak = !!pdf && !b.dosya;                 // internetten (MEB sunucusundan) gelen PDF: bilgisayardan açılabilir
  const secenek = { kimlik: b.kimlik, sayfa: ara.get('s') };
  let kendimiz = false;
  let yerelPanel = false;          // dosya seçme paneli açıkken kalem/tam ekran gösterilmez (ortada belge yok)

  // Bilgisayardan aç: seçilen PDF yalnız bu tarayıcıda açılır, hiçbir yere gönderilmez.
  const dosyaSec = el('input', { type: 'file', accept: 'application/pdf,.pdf', hidden: true });
  document.body.append(dosyaSec);
  const yerelDugme = (ana) => el('button', { sinif: ana ? 'dugme ana' : 'dugme', type: 'button', onclick: () => dosyaSec.click(),
    title: 'Kitabın bilgisayarınızdaki PDF dosyasını açar; internet beklenmez' }, simge('kitap'), 'Bilgisayardan aç');
  dosyaSec.addEventListener('change', async () => {
    const f = dosyaSec.files?.[0];
    dosyaSec.value = '';
    if (!f) return;
    if (!/\.pdf$/i.test(f.name) && f.type !== 'application/pdf') {
      // Açık bir belge varsa silinmez: uyarı üstte kısa süre görünür
      const acik = alan.querySelector('.pdf-kaydir, iframe');
      const uyari = el('div', { sinif: acik ? 'g-uyari g-uyari-ust' : 'g-uyari', role: 'alert' }, el('h2', {}, 'Bu dosya PDF değil'),
        el('p', {}, `“${f.name}” açılamadı. Kitabın .pdf uzantılı dosyasını seçin.`), acik ? null : yerelDugme(true));
      if (acik) { alan.querySelector('.g-uyari-ust')?.remove(); alan.append(uyari); setTimeout(() => uyari.remove(), 6000); }
      else alan.replaceChildren(uyari);
      return;
    }
    $('#g-bilgi').textContent = `Bilgisayardaki dosya: ${f.name} · açılıyor…`;
    const sonuc = await pdfGoster(alan, { veri: await f.arrayBuffer(), ad: f.name }, b.baslik, null, secenek);
    if (sonuc === true) {
      kendimiz = true;
      $('#g-bilgi').textContent = `Bilgisayardaki dosya: ${f.name}${bilgiMetni ? ' · ' + bilgiMetni : ''}`;
      dugmeleriCiz();
    } else if (sonuc === false) {
      $('#g-bilgi').textContent = bilgiMetni;
      alan.replaceChildren(el('div', { sinif: 'g-uyari' }, el('h2', {}, 'Dosya açılamadı'),
        el('p', {}, `“${f.name}” okunamadı; dosya bozuk ya da tam inmemiş olabilir.`), yerelDugme(true)));
    }
  });

  function dugmeleriCiz() {
    const dugmeler = [
      kendimiz && el('button', { sinif: 'dugme ana', type: 'button', 'data-kalem-dugme': '', onclick: () => window.kalemAc?.() }, el('span', { 'aria-hidden': 'true' }, '✎'), 'Kalemle yaz'),
      !kendimiz && !yerelPanel && b.cerceve && el('button', { sinif: 'dugme ana', type: 'button', 'data-kalem-dugme': '', onclick: () => window.kalemAc?.() }, el('span', { 'aria-hidden': 'true' }, '✎'), 'Kalemle yaz'),
      uzak && yerelDugme(false),
      b.dosya && el('a', { sinif: 'dugme', href: `/${b.dosya}`, download: '' }, simge('indir'), 'İndir'),
      resmi && el('a', { sinif: 'dugme', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî kaynak', simge('ok')),
      (kendimiz || (b.cerceve && !yerelPanel)) && el('button', { sinif: 'dugme', type: 'button', onclick: () => (document.fullscreenElement ? document.exitFullscreen() : alan.requestFullscreen?.()) }, simge('buyut'), 'Tam ekran'),
    ];
    $('#g-dugmeler').replaceChildren(...dugmeler.filter(Boolean));
  }

  const internettenAc = async () => {
    yerelPanel = false;
    const sonuc = await pdfGoster(alan, pdf, b.baslik, b.boyut, { ...secenek, yerelDugme: uzak ? () => yerelDugme(true) : null });
    if (sonuc === 'iptal') return;              // bu arada bilgisayardan açıldı
    kendimiz = sonuc === true;
    dugmeleriCiz();
    if (kendimiz) return;
    if (b.cerceve) {
      const kaynak = b.dosya ? `/${b.dosya}` : b.baglanti;
      alan.replaceChildren(el('iframe', { src: kaynak, title: b.baslik, loading: 'eager', allow: 'fullscreen' }));
    } else {
      alan.replaceChildren(el('div', { sinif: 'g-uyari' },
        el('h2', {}, 'Bu belge yalnız resmî sitesinde açılabiliyor'),
        el('p', {}, `${b.kaynak} kendi sayfalarının başka sitelerde gösterilmesine izin vermiyor. Belge yeni sekmede, resmî adresinde açılır.`),
        uzak && yerelDugme(true),
        el('a', { sinif: 'dugme ana', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî sitede aç', simge('ok'))));
    }
  };

  if (uzak && ara.get('yerel')) yerelPanel = true;
  dugmeleriCiz();
  if (uzak && ara.get('yerel')) {
    // "Bilgisayardan aç" ile gelindi: internetten indirme başlatılmaz.
    alan.replaceChildren(el('div', { sinif: 'g-uyari g-yerel' },
      el('h2', {}, 'Kitabı bilgisayardan açın'),
      el('p', {}, 'Bu kitabın PDF dosyası bilgisayarınızda varsa seçin: sayfalar internet beklemeden açılır. Dosya hiçbir yere gönderilmez, yalnız bu tarayıcıda açılır.'),
      el('div', { sinif: 'g-yerel-eylem' }, yerelDugme(true),
        el('button', { sinif: 'dugme', type: 'button', onclick: () => internettenAc() }, 'İnternetten aç')),
      resmi && el('p', { sinif: 'g-yerel-not' }, 'Dosya bilgisayarınızda yoksa ', el('a', { href: resmi, target: '_blank', rel: 'noopener' }, 'resmî kaynaktan'),
        ' bir kez indirip kaydedin; sonraki derslerde buradan saniyeler içinde açılır.')));
    return;
  }
  if (pdf) await internettenAc();
  else {
    dugmeleriCiz();
    if (b.cerceve) {
      const kaynak = b.dosya ? `/${b.dosya}` : b.baglanti;
      alan.replaceChildren(el('iframe', { src: kaynak, title: b.baslik, loading: 'eager', allow: 'fullscreen' }));
    } else {
      alan.replaceChildren(el('div', { sinif: 'g-uyari' },
        el('h2', {}, 'Bu belge yalnız resmî sitesinde açılabiliyor'),
        el('p', {}, `${b.kaynak} kendi sayfalarının başka sitelerde gösterilmesine izin vermiyor. Belge yeni sekmede, resmî adresinde açılır.`),
        el('a', { sinif: 'dugme ana', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî sitede aç', simge('ok'))));
    }
  }
});
