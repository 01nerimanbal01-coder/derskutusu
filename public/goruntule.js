// Belge görüntüleyici: goruntule.html?b=<kimlik>.
// PDF sitedeyse ya da kaynağı izin veriyorsa (CORS, ör. cdn.eba.gov.tr) sayfalar PDF.js (yerel kopya) ile burada çizilir;
// kalemle yazılanlar sayfa koordinatında tutulur, PDF kaydırılınca ve yakınlaştırılınca yazı da birlikte kayar/büyür.
// Öteki belgeler resmî adresinden çerçeve içinde açılır; kaynak buna da izin vermiyorsa (ör. ÖSYM) düğme gösterilir.

const PDF_CORS = /^https:\/\/cdn\.eba\.gov\.tr\/.+\.pdf(\?|$)/i;

async function pdfGoster(alan, adres, baslik, boyut) {
  alan.classList.add('pdf-mod');
  const kaydir = el('div', { sinif: 'pdf-kaydir', tabindex: '0', 'aria-label': `${baslik} sayfaları` });
  const sayfalar = el('div', { sinif: 'pdf-sayfalar' });
  const bilgi = el('span', { sinif: 'pdf-no', 'aria-live': 'polite' }, 'Yükleniyor…');
  const arac = el('div', { sinif: 'pdf-arac' },
    el('button', { type: 'button', 'aria-label': 'Küçült', title: 'Küçült', onclick: () => yakinlas(1 / 1.2) }, '−'),
    el('button', { type: 'button', 'aria-label': 'Sayfaya sığdır', title: 'Sığdır', onclick: () => yakinlas(0) }, '↔'),
    el('button', { type: 'button', 'aria-label': 'Büyüt', title: 'Büyüt', onclick: () => yakinlas(1.2) }, '+'),
    bilgi);
  kaydir.append(sayfalar);
  alan.replaceChildren(kaydir, arac);

  let doc;
  try {
    const pdfjs = await import('/kutuphane/pdfjs/pdf.min.js');
    pdfjs.GlobalWorkerOptions.workerSrc = '/kutuphane/pdfjs/pdf.worker.min.js';
    const PARCA = 262144;
    if (boyut && !adres.startsWith('/')) {
      // MEB sunucusu Content-Length / Accept-Ranges başlıklarını tarayıcıya açmıyor: parçalar Range isteğiyle bizden gider,
      // böylece 150 MB'lık kitabın yalnız görüntülenen sayfaları iner.
      const oku = (bas, son) => fetch(adres, { headers: { Range: `bytes=${bas}-${son - 1}` } }).then((y) => {
        if (y.status !== 206) throw new Error('parça okunamadı');
        return y.arrayBuffer();
      });
      const tasima = new pdfjs.PDFDataRangeTransport(boyut, new Uint8Array(await oku(0, Math.min(PARCA, boyut))));
      tasima.requestDataRange = (bas, son) => { oku(bas, son).then((v) => tasima.onDataRange(bas, new Uint8Array(v))); };
      doc = await pdfjs.getDocument({ range: tasima, rangeChunkSize: PARCA, disableAutoFetch: true, isEvalSupported: false }).promise;
    } else {
      doc = await pdfjs.getDocument({ url: adres, rangeChunkSize: PARCA, disableAutoFetch: true, isEvalSupported: false }).promise;
    }
  } catch (e) {
    return false;                       // çizilemedi: çağıran çerçeveye döner
  }
  const oran = Math.min(window.devicePixelRatio || 1, 2);
  const ilk = (await doc.getPage(1)).getViewport({ scale: 1 });
  let olcek = 1;
  const genislik = () => Math.round(Math.min(kaydir.clientWidth - 24, 1100) * olcek);
  const kutular = [];
  for (let i = 1; i <= doc.numPages; i++) {
    const kutu = el('div', { sinif: 'pdf-sayfa', 'data-no': i }, el('canvas', {}));
    kutu.oran = ilk.height / ilk.width;
    kutular.push(kutu);
  }
  sayfalar.append(...kutular);
  const boyutla = () => { const g = genislik(); for (const k of kutular) { k.style.width = g + 'px'; k.style.height = Math.round(g * k.oran) + 'px'; } };
  boyutla();

  // Tembel çizim: yalnız görünen ve yakınındaki sayfalar; uzaklaşanın tuvali boşaltılır (bellek).
  const cizilen = new Map(), sira = [];
  let calisan = 0;
  const ciz = async (kutu) => {
    const g = genislik();
    if (cizilen.get(kutu) === g) return;
    cizilen.set(kutu, g);
    const sayfa = await doc.getPage(Number(kutu.dataset.no));
    const v1 = sayfa.getViewport({ scale: 1 });
    kutu.oran = v1.height / v1.width;
    kutu.style.height = Math.round(g * kutu.oran) + 'px';
    const vp = sayfa.getViewport({ scale: (g / v1.width) * oran });
    const tuval = document.createElement('canvas');
    tuval.width = Math.floor(vp.width); tuval.height = Math.floor(vp.height);
    await sayfa.render({ canvasContext: tuval.getContext('2d', { alpha: false }), viewport: vp }).promise;
    if (cizilen.get(kutu) === g) kutu.replaceChildren(tuval);
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
      else if (cizilen.has(k.target)) { cizilen.delete(k.target); k.target.replaceChildren(el('canvas', {})); }
    }
    kuyruk();
  }, { root: kaydir, rootMargin: '1500px 0px' });
  kutular.forEach((k) => gozcu.observe(k));

  const noYaz = () => {
    const orta = kaydir.scrollTop + kaydir.clientHeight / 3;
    const n = kutular.findIndex((k) => k.offsetTop + k.offsetHeight > orta) + 1 || kutular.length;
    bilgi.textContent = `Sayfa ${n} / ${doc.numPages}`;
  };
  kaydir.addEventListener('scroll', noYaz, { passive: true });
  noYaz();

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

  // Kalem bu kaba bağlanır: yazı PDF sayfalarıyla birlikte kayar.
  window.kalemHedef = { kap: alan, kaydir };
  return true;
}

veri('belgeler.json').then(async (belgeler) => {
  const id = new URLSearchParams(location.search).get('b');
  let grup = null;
  const b = belgeler?.gruplar.flatMap((g) => g.belgeler.map((x) => ((x.kimlik === id && (grup = g)), x))).find((x) => x.kimlik === id);
  if (!b) {
    $('#g-baslik').textContent = 'Belge bulunamadı';
    $('#g-alan').replaceChildren(el('div', { sinif: 'g-uyari' }, el('p', {}, 'Aradığınız belge listede yok. '), el('a', { sinif: 'dugme ana', href: '/belgeler.html' }, 'Resmî belgelere dön')));
    return;
  }
  document.title = `${b.baslik} · Ders Kutusu`;
  $('#g-baslik').textContent = b.baslik;
  $('#g-bilgi').textContent = [grup?.ad, b.kaynak, b.aciklama].filter(Boolean).join(' · ');
  const resmi = b.kaynak_adres || b.baglanti;
  const alan = $('#g-alan');
  const pdf = b.dosya?.endsWith('.pdf') ? `/${b.dosya}` : PDF_CORS.test(b.baglanti || '') ? b.baglanti : null;
  const kendimiz = pdf && await pdfGoster(alan, pdf, b.baslik, b.boyut);
  const dugmeler = [
    (kendimiz || b.cerceve) && el('button', { sinif: 'dugme ana', type: 'button', onclick: () => window.kalemAc?.() }, el('span', { 'aria-hidden': 'true' }, '✎'), 'Kalemle yaz'),
    b.dosya && el('a', { sinif: 'dugme', href: `/${b.dosya}`, download: '' }, simge('indir'), 'İndir'),
    resmi && el('a', { sinif: 'dugme', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî kaynak', simge('ok')),
    (kendimiz || b.cerceve) && el('button', { sinif: 'dugme', type: 'button', onclick: () => (document.fullscreenElement ? document.exitFullscreen() : alan.requestFullscreen?.()) }, simge('buyut'), 'Tam ekran'),
  ];
  $('#g-dugmeler').replaceChildren(...dugmeler.filter(Boolean));
  if (kendimiz) return;
  if (b.cerceve) {
    const kaynak = b.dosya ? `/${b.dosya}` : b.baglanti;
    alan.replaceChildren(el('iframe', { src: kaynak, title: b.baslik, loading: 'eager', allow: 'fullscreen' }));
  } else {
    alan.replaceChildren(el('div', { sinif: 'g-uyari' },
      el('h2', {}, 'Bu belge yalnız resmî sitesinde açılabiliyor'),
      el('p', {}, `${b.kaynak} kendi sayfalarının başka sitelerde gösterilmesine izin vermiyor. Belge yeni sekmede, resmî adresinde açılır.`),
      el('a', { sinif: 'dugme ana', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî sitede aç', simge('ok'))));
  }
});
