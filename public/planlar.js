// Günlük ders planları: planlar.html?p=<plan adı>[&sinif=N] (ya da ?sinif=N).
// Okul, öğretmen, müdür yardımcısı ve müdür adları indirmeden önce planın bütün sayfalarına yazılır; plan tüm yıl ya da
// ay ay, Word ya da PDF olarak indirilir. Her şey tarayıcıda yapılır, bilgiler hiçbir yere gönderilmez.
// Veri: veri/gunluk-planlar.json (dizin), veri/gunluk-plan/<ad>.json (PDF içeriği), dosyalar/gunluk-plan/<ad>.docx (Word şablonu).
// Word şablonundaki doldurma yerleri karakter stilli koşulardır (DKOkul, DKOgretmen, DKMudurYrd, DKMudur, DKOnay); her haftanın
// ilk paragrafında DK_H_<hafta>_<ay sırası>_<sıra> yer imi vardır (03-ARACLAR/gunluk_plan_uret.py üretir).

const Plan = (() => {
  const W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main';
  const XML_NS = 'http://www.w3.org/XML/1998/namespace';
  const DOCX_TUR = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
  const AYLAR = ['Eylül', 'Ekim', 'Kasım', 'Aralık', 'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran'];
  const AY_KISA = ['eylul', 'ekim', 'kasim', 'aralik', 'ocak', 'subat', 'mart', 'nisan', 'mayis', 'haziran'];
  const BOS_TARIH = '…/…/20…';
  const NOKTA = '..................................';

  // Kütüphaneler yalnız gerekince yüklenir (sayfa açılışını yavaşlatmaz)
  const betikler = {};
  const betikYukle = (src) => (betikler[src] ||= new Promise((tamam, hata) => {
    const s = document.createElement('script');
    s.src = src;
    s.onload = tamam;
    s.onerror = () => { delete betikler[src]; hata(new Error(`${src} yüklenemedi`)); };
    document.head.append(s);
  }));
  const zipKutuphane = () => betikYukle('/kutuphane/jszip/jszip.min.js').then(() => window.JSZip);
  const pdfKutuphane = () => betikYukle('/kutuphane/jspdf/jspdf.umd.min.js')
    .then(() => betikYukle('/kutuphane/jspdf/jspdf.plugin.autotable.min.js')).then(() => window.jspdf.jsPDF);

  const onbellek = {};
  const al = (adres, tur) => (onbellek[adres] ||= fetch(adres).then((y) => {
    if (!y.ok) throw new Error(`${adres}: ${y.status}`);
    return tur === 'json' ? y.json() : y.arrayBuffer();
  }).catch((e) => { delete onbellek[adres]; throw e; }));

  const base64 = (tampon) => {
    const b = new Uint8Array(tampon);
    let s = '';
    for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
    return btoa(s);
  };
  const buyuk = (s) => s.toLocaleUpperCase('tr-TR');
  const yil = (ay) => (ay < 4 ? 2026 : 2027);
  const dosyaAdi = (plan, ay, uzanti) => (ay == null ? `${plan.ad}.${uzanti}`
    : `${plan.ad.replace(/-2026-2027$/, '')}-${String(ay + 1).padStart(2, '0')}-${AY_KISA[ay]}-${yil(ay)}.${uzanti}`);

  // Kullanıcı bilgileri → doldurma değerleri (boş alan belgede noktalı kalır)
  const degerler = (b) => ({
    DKOkul: b.okul ? buyuk(b.okul) : null,
    DKOgretmen: b.ogretmen || null,
    DKMudurYrd: b.mudurYrd || null,
    DKMudur: b.mudur || null,
    DKOnay: b.tarih ? null : BOS_TARIH,
  });

  // Arapça harfleri PDF için sunum biçimlerine (U+FE70–FEFF) çevirir. jsPDF'in kendi şekillendiricisi harekeli harflerde ve
  // ، ؛ ؟ işaretlerinden sonra yanlış biçim seçiyor; hazır sunum biçimlerini ise değiştirmeden geçirip yalnız sırayı çeviriyor.
  const arapca = (() => {
    const B = {};   // harf → [yalın, sonda, başta, ortada]; yalnız sağa bağlananlarda baş/orta yok
    [[0x0621, 0xFE80], [0x0622, 0xFE81, 0xFE82], [0x0623, 0xFE83, 0xFE84], [0x0624, 0xFE85, 0xFE86], [0x0625, 0xFE87, 0xFE88],
      [0x0626, 0xFE89, 0xFE8A, 0xFE8B, 0xFE8C], [0x0627, 0xFE8D, 0xFE8E], [0x0628, 0xFE8F, 0xFE90, 0xFE91, 0xFE92], [0x0629, 0xFE93, 0xFE94],
      [0x062A, 0xFE95, 0xFE96, 0xFE97, 0xFE98], [0x062B, 0xFE99, 0xFE9A, 0xFE9B, 0xFE9C], [0x062C, 0xFE9D, 0xFE9E, 0xFE9F, 0xFEA0],
      [0x062D, 0xFEA1, 0xFEA2, 0xFEA3, 0xFEA4], [0x062E, 0xFEA5, 0xFEA6, 0xFEA7, 0xFEA8], [0x062F, 0xFEA9, 0xFEAA], [0x0630, 0xFEAB, 0xFEAC],
      [0x0631, 0xFEAD, 0xFEAE], [0x0632, 0xFEAF, 0xFEB0], [0x0633, 0xFEB1, 0xFEB2, 0xFEB3, 0xFEB4], [0x0634, 0xFEB5, 0xFEB6, 0xFEB7, 0xFEB8],
      [0x0635, 0xFEB9, 0xFEBA, 0xFEBB, 0xFEBC], [0x0636, 0xFEBD, 0xFEBE, 0xFEBF, 0xFEC0], [0x0637, 0xFEC1, 0xFEC2, 0xFEC3, 0xFEC4],
      [0x0638, 0xFEC5, 0xFEC6, 0xFEC7, 0xFEC8], [0x0639, 0xFEC9, 0xFECA, 0xFECB, 0xFECC], [0x063A, 0xFECD, 0xFECE, 0xFECF, 0xFED0],
      [0x0641, 0xFED1, 0xFED2, 0xFED3, 0xFED4], [0x0642, 0xFED5, 0xFED6, 0xFED7, 0xFED8], [0x0643, 0xFED9, 0xFEDA, 0xFEDB, 0xFEDC],
      [0x0644, 0xFEDD, 0xFEDE, 0xFEDF, 0xFEE0], [0x0645, 0xFEE1, 0xFEE2, 0xFEE3, 0xFEE4], [0x0646, 0xFEE5, 0xFEE6, 0xFEE7, 0xFEE8],
      [0x0647, 0xFEE9, 0xFEEA, 0xFEEB, 0xFEEC], [0x0648, 0xFEED, 0xFEEE], [0x0649, 0xFEEF, 0xFEF0], [0x064A, 0xFEF1, 0xFEF2, 0xFEF3, 0xFEF4],
    ].forEach(([k, ...f]) => { B[k] = f; });
    const LAMELIF = { 0x0622: [0xFEF5, 0xFEF6], 0x0623: [0xFEF7, 0xFEF8], 0x0625: [0xFEF9, 0xFEFA], 0x0627: [0xFEFB, 0xFEFC] };
    const saydam = (k) => (k >= 0x064B && k <= 0x065F) || k === 0x0670;   // harekeler bağlanmayı bozmaz
    const ikiYana = (k) => k === 0x0640 || B[k]?.length === 4;           // sonrakine de bağlanan (tatvil dahil)
    const bagli = (k) => k === 0x0640 || B[k]?.length >= 2;              // öncekine bağlanabilen
    return (metin) => {
      if (!/[ء-ي]/.test(metin)) return metin;
      const k = Array.from(metin, (c) => c.codePointAt(0));
      const komsu = (i, adim) => { for (let j = i + adim; j >= 0 && j < k.length; j += adim) if (!saydam(k[j])) return k[j]; return null; };
      let cikti = '';
      for (let i = 0; i < k.length; i++) {
        const c = k[i];
        if (!B[c]) { cikti += String.fromCodePoint(c); continue; }
        const onceki = komsu(i, -1);
        const oncekine = onceki != null && ikiYana(onceki) && bagli(c);
        if (c === 0x0644) {   // lam + elif bağı (araya hareke girebilir)
          let j = i + 1;
          while (j < k.length && saydam(k[j])) j++;
          if (j < k.length && LAMELIF[k[j]]) {
            cikti += String.fromCodePoint(LAMELIF[k[j]][oncekine ? 1 : 0], ...k.slice(i + 1, j));
            i = j;
            continue;
          }
        }
        const sonraki = komsu(i, 1);
        const sonrakine = ikiYana(c) && sonraki != null && bagli(sonraki);
        const f = B[c];
        cikti += String.fromCodePoint((oncekine ? (sonrakine ? f[3] : f[1]) : (sonrakine ? f[2] : f[0])) ?? f[0]);
      }
      return cikti;
    };
  })();

  // ---------- Word ----------
  async function word(plan, ay, bilgi) {
    const JSZip = await zipKutuphane();
    const zip = await JSZip.loadAsync(await al(`/dosyalar/gunluk-plan/${plan.ad}.docx`));
    const xml = await zip.file('word/document.xml').async('string');
    const d = new DOMParser().parseFromString(xml, 'application/xml');
    if (d.getElementsByTagName('parsererror').length) throw new Error('Word şablonu okunamadı');
    const govde = d.getElementsByTagNameNS(W, 'body')[0];
    if (ay != null) {   // yalnız seçilen ayın haftaları kalır
      let tut = false, kalan = 0;
      for (const e of [...govde.children]) {
        if (e.localName === 'sectPr') continue;
        const im = [...e.getElementsByTagNameNS(W, 'bookmarkStart')].map((x) => x.getAttributeNS(W, 'name') || '').find((n) => n.startsWith('DK_H_'));
        if (im) { tut = Number(im.split('_')[3]) === ay; if (tut) kalan++; }
        if (!tut) govde.removeChild(e);
      }
      if (!kalan) throw new Error('Bu ayda plan haftası yok');
      const ilk = govde.getElementsByTagNameNS(W, 'p')[0];   // ilk sayfanın başında sayfa sonu olmasın
      for (const s of [...(ilk?.getElementsByTagNameNS(W, 'pageBreakBefore') || [])]) s.parentNode.removeChild(s);
    }
    const dg = degerler(bilgi);
    for (const rs of [...d.getElementsByTagNameNS(W, 'rStyle')]) {
      const v = dg[rs.getAttributeNS(W, 'val')];
      if (!v) continue;
      const t = rs.parentNode.parentNode.getElementsByTagNameNS(W, 't')[0];
      if (!t) continue;
      t.textContent = v;
      t.setAttributeNS(XML_NS, 'xml:space', 'preserve');
    }
    const cikti = new XMLSerializer().serializeToString(d).replace(/^\s*<\?xml[^>]*\?>\s*/, '');   // tarayıcı bildirimi kendisi ekleyebilir
    zip.file('word/document.xml', `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n${cikti}`);
    return zip.generateAsync({ type: 'blob', mimeType: DOCX_TUR, compression: 'DEFLATE', compressionOptions: { level: 6 } });
  }

  // ---------- PDF ----------
  const RENK = { metin: [17, 26, 46], mavi: [31, 58, 138], lacivert: [11, 34, 87], soluk: [91, 100, 121], cizgi: [169, 182, 211], golge: [232, 238, 251] };
  const SAYFA = { sol: 15, sag: 195, orta: 105, ust: 29, alt: 280 };

  async function pdf(plan, ay, bilgi) {
    const [jsPDF, icerik, duz, kalin, logo] = await Promise.all([pdfKutuphane(), al(`/veri/gunluk-plan/${plan.ad}.json`, 'json'),
      al('/kutuphane/font/DKPlan-Regular.ttf'), al('/kutuphane/font/DKPlan-Bold.ttf'), al('/simge-192.png')]);
    const haftalar = icerik.haftalar.filter((h) => ay == null || AYLAR.indexOf(h.ay) === ay);
    if (!haftalar.length) throw new Error('Bu ayda plan haftası yok');
    const doc = new jsPDF({ unit: 'mm', format: 'a4', compress: true });
    doc.addFileToVFS('DKPlan-Regular.ttf', base64(duz));
    doc.addFont('DKPlan-Regular.ttf', 'DKPlan', 'normal');
    doc.addFileToVFS('DKPlan-Bold.ttf', base64(kalin));
    doc.addFont('DKPlan-Bold.ttf', 'DKPlan', 'bold');
    if (icerik.haftalar.some((h) => /[؀-ۿ]/.test(JSON.stringify(h.bolumler)))) doc.setLineHeightFactor(1.45);   // Arapça uzantıları üst üste binmesin
    doc.setProperties({ title: `${icerik.baslik} ${ay == null ? '2026-2027' : `${AYLAR[ay]} ${yil(ay)}`}`, author: 'Ders Kutusu', creator: 'Ders Kutusu · derskutusu.com' });
    const dg = degerler(bilgi);
    // sigdir: en çok genişlik (mm); uzun ad bu genişliğe sığacak kadar küçültülür
    const yaz = (metin, x, y, { boy = 10, kalin: k = false, renk = RENK.metin, hiza = 'left', sigdir = 0 } = {}) => {
      const m = arapca(metin);
      doc.setFont('DKPlan', k ? 'bold' : 'normal');
      doc.setFontSize(boy);
      if (sigdir && doc.getTextWidth(m) > sigdir) doc.setFontSize(boy * sigdir / doc.getTextWidth(m));
      doc.setTextColor(...renk);
      doc.text(m, x, y, { align: hiza });
    };
    const tablo = (satirlar, y) => {
      doc.autoTable({
        startY: y, body: satirlar.map((r) => r.map(arapca)), theme: 'grid',
        margin: { left: SAYFA.sol, right: 210 - SAYFA.sag, top: SAYFA.ust, bottom: 297 - SAYFA.alt },
        styles: { font: 'DKPlan', fontSize: 9, textColor: RENK.metin, lineColor: RENK.cizgi, lineWidth: 0.2, cellPadding: { top: 1.2, bottom: 1.2, left: 1.8, right: 1.8 }, valign: 'top', overflow: 'linebreak' },
        columnStyles: { 0: { cellWidth: 46, fontStyle: 'bold', fillColor: RENK.golge }, 1: { cellWidth: 'auto' } },
        didParseCell: (v) => { if (v.column.index === 1 && /^\n+$/.test(v.cell.raw || '')) v.cell.styles.minCellHeight = 16; },
      });
      return doc.lastAutoTable.finalY;
    };
    const yeniSayfa = () => { doc.addPage(); return SAYFA.ust - 2; };
    const basSayfa = [];   // her haftanın ilk sayfası (devam sayfalarına hafta etiketi yazılır)
    haftalar.forEach((h, i) => {
      if (i) doc.addPage();
      basSayfa.push([doc.getNumberOfPages(), h]);
      let y = SAYFA.ust - 1;
      yaz(dg.DKOkul || '.................................................................', SAYFA.orta, y, { boy: 11, kalin: true, renk: RENK.lacivert, hiza: 'center', sigdir: 180 });
      y += 6.5;
      yaz(icerik.baslik, SAYFA.orta, y, { boy: 12.5, kalin: true, renk: RENK.mavi, hiza: 'center', sigdir: 180 });
      y += 6;
      yaz(`${icerik.yil} · ${h.hafta}`, SAYFA.orta, y, { boy: 10, hiza: 'center', sigdir: 180 });
      y += 3;
      h.bolumler.forEach(([baslik, satirlar], k) => {
        // son bölüm (açıklamalar) imza bloğuyla aynı sayfada kalsın; başlık sayfa sonunda yalnız kalmasın
        const gerekli = k === h.bolumler.length - 1 ? 8 + 20 + 34 : 22;
        if (y + gerekli > SAYFA.alt) y = yeniSayfa();
        yaz(baslik, SAYFA.sol, y + 6, { boy: 10.5, kalin: true, renk: RENK.mavi });
        y = tablo(satirlar, y + 8);
      });
      if (y + 34 > SAYFA.alt) y = yeniSayfa();   // imza bloğu bölünmez
      y += 12;
      const sut = [45, 105, 165];
      yaz('Ders Öğretmeni', sut[0], y, { kalin: true, hiza: 'center' });
      yaz('Müdür Yardımcısı', sut[1], y, { kalin: true, hiza: 'center' });
      yaz('Uygundur', sut[2], y, { kalin: true, hiza: 'center' });
      yaz(dg.DKOnay || h.onay, sut[2], y + 5.5, { hiza: 'center' });
      yaz(dg.DKOgretmen || NOKTA, sut[0], y + 11, { hiza: 'center', sigdir: 56 });
      yaz(dg.DKMudurYrd || NOKTA, sut[1], y + 11, { hiza: 'center', sigdir: 56 });
      yaz(dg.DKMudur || NOKTA, sut[2], y + 11, { hiza: 'center', sigdir: 56 });
      yaz('Okul Müdürü', sut[2], y + 16.5, { hiza: 'center' });
    });
    const logoVeri = `data:image/png;base64,${base64(logo)}`;
    const n = doc.getNumberOfPages();
    for (let i = 1; i <= n; i++) {   // üst ve alt bilgi (logo, ders, sayfa numarası); devam sayfasında hafta etiketi
      doc.setPage(i);
      doc.addImage(logoVeri, 'PNG', SAYFA.sol, 8, 10, 10, 'logo', 'FAST');
      yaz('DERS KUTUSU', SAYFA.sol + 12, 15, { boy: 11, kalin: true, renk: RENK.lacivert });
      yaz('derskutusu.com', SAYFA.sol + 12 + doc.getTextWidth('DERS KUTUSU') + 2.5, 15, { boy: 8.5, renk: RENK.soluk });
      yaz(icerik.ust, SAYFA.sag, 15, { boy: 8.5, renk: RENK.soluk, hiza: 'right', sigdir: 100 });
      doc.setDrawColor(...RENK.lacivert);
      doc.setLineWidth(0.4);
      doc.line(SAYFA.sol, 19.5, SAYFA.sag, 19.5);
      const [ilk, hafta] = basSayfa.filter(([s]) => s <= i).pop();
      if (ilk !== i) yaz(`${hafta.hafta} · devamı`, SAYFA.orta, 25, { boy: 8.5, renk: RENK.soluk, hiza: 'center' });
      yaz(icerik.alt, SAYFA.orta, 289, { boy: 7.5, renk: RENK.soluk, hiza: 'center', sigdir: 150 });
      yaz(`${i} / ${n}`, SAYFA.sag, 289, { boy: 7.5, renk: RENK.soluk, hiza: 'right' });
    }
    return doc.output('blob');
  }

  const uret = (plan, ay, bilgi, bicim) => (bicim === 'pdf' ? pdf(plan, ay, bilgi) : word(plan, ay, bilgi));

  async function aylikZip(plan, bilgi, bicim, ilerle) {
    const JSZip = await zipKutuphane();
    const zip = new JSZip();
    const aylar = plan.aylar.map(([a]) => AYLAR.indexOf(a)).filter((a) => a >= 0);
    for (const [k, ay] of aylar.entries()) {
      ilerle?.(k + 1, aylar.length, AYLAR[ay]);
      zip.file(dosyaAdi(plan, ay, bicim), await uret(plan, ay, bilgi, bicim));
    }
    return zip.generateAsync({ type: 'blob', compression: 'STORE' });
  }

  return { AYLAR, word, pdf, uret, aylikZip, dosyaAdi, yil, arapca };
})();

// ---------- Sayfa ----------
(() => {
  if (!document.getElementById('p-bilgi')) return;
  const ANAHTAR = 'dk-plan-bilgi';
  const IH = new Set(['arapca', 'mesleki-arapca', 'fikih', 'hadis', 'siyer', 'akaid', 'tefsir', 'dinler-tarihi', 'hitabet-ve-mesleki-uygulama', 'kelam', 'islam-kultur-ve-medeniyeti']);
  const SECMELI = new Set(['kuran-i-kerim', 'peygamberimizin-hayati', 'temel-dini-bilgiler']);
  const BILDIK = ['Bu ayda plan haftası yok', 'Word şablonu okunamadı'];   // kullanıcıya olduğu gibi gösterilen iletiler
  const alan = { okul: $('#p-okul'), ogretmen: $('#p-ogretmen'), mudurYrd: $('#p-mudur-yrd'), mudur: $('#p-mudur'), tarih: $('#p-tarih'), hatirla: $('#p-hatirla') };
  const durum = $('#p-durum');
  let dizin = [], sinif = null, secili = null, mesgul = false;

  // Denetim karakterleri (PDF'ten kopyalanan U+0002 gibi) Word dosyasını bozmasın
  const temiz = (s) => s.replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F￾￿]/g, '').trim().replace(/\s+/g, ' ');
  const bilgi = () => ({
    okul: temiz(alan.okul.value), ogretmen: temiz(alan.ogretmen.value), mudurYrd: temiz(alan.mudurYrd.value), mudur: temiz(alan.mudur.value), tarih: alan.tarih.checked,
  });
  const kaydet = () => {
    try {
      if (alan.hatirla.checked) localStorage.setItem(ANAHTAR, JSON.stringify(bilgi()));
      else localStorage.removeItem(ANAHTAR);
    } catch { /* gizli pencere: hatırlanmaz */ }
  };
  try {
    const k = JSON.parse(localStorage.getItem(ANAHTAR) || 'null');
    if (k) {
      for (const a of ['okul', 'ogretmen', 'mudurYrd', 'mudur']) alan[a].value = k[a] || '';
      alan.tarih.checked = k.tarih !== false;
    }
  } catch { /* depolama kapalı */ }

  const tamAd = (p) => `${p.sinifAd} ${p.dersAd}${p.ek ? ` ${p.ek}` : ''}`;
  // Adres ve sekme başlığı seçimle uyumlu kalır (yenilenince ve paylaşılınca aynı seçim açılır)
  const durumYaz = () => {
    history.replaceState(null, '', `?sinif=${sinif}${secili ? `&p=${secili.ad}` : ''}`);
    document.title = secili ? `${tamAd(secili)} günlük planları · Ders Kutusu` : `${sinif}. sınıf günlük planları · Ders Kutusu`;
  };

  // Önizleme kâğıdı
  const onizle = () => {
    const b = bilgi(), nokta = '………………………';
    $('#k-okul').textContent = b.okul ? b.okul.toLocaleUpperCase('tr-TR') : '…………………………………………';
    $('#k-ogretmen').textContent = b.ogretmen || nokta;
    $('#k-mudur-yrd').textContent = b.mudurYrd || nokta;
    $('#k-mudur').textContent = b.mudur || nokta;
    $('#k-tarih').textContent = b.tarih ? '14.09.2026' : '…/…/20…';
    for (const [id, a] of [['k-okul', 'okul'], ['k-ogretmen', 'ogretmen'], ['k-mudur-yrd', 'mudurYrd'], ['k-mudur', 'mudur']]) $(`#${id}`).classList.toggle('dolu', !!b[a]);
    if (secili) {
      $('#k-baslik').textContent = `${tamAd(secili).toLocaleUpperCase('tr-TR')} DERSİ GÜNLÜK PLANI`;
      $('#k-ust-sag').textContent = `${tamAd(secili)} · Günlük plan`;
    }
  };
  $('#p-bilgi').addEventListener('input', () => { onizle(); kaydet(); });
  $('#p-bilgi').addEventListener('change', () => { onizle(); kaydet(); });

  const bicim = () => $('input[name="p-bicim"]:checked').value;
  const indir = (blob, ad) => {
    const a = el('a', { href: URL.createObjectURL(blob), download: ad });
    document.body.append(a);
    a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
  };
  const dugmeler = (kapali) => $$('#p-indir button').forEach((d) => { d.disabled = kapali; });
  const isle = async (is, bekleyen) => {
    if (mesgul) return;
    mesgul = true;
    $('#p-indir').setAttribute('aria-busy', 'true');
    dugmeler(true);
    durum.className = 'plan-durum';
    durum.textContent = bekleyen;
    try {
      const [blob, ad] = await is();
      indir(blob, ad);
      durum.className = 'plan-durum tamam';
      durum.textContent = `${ad} indirildi.`;
    } catch (e) {
      console.error(e);
      durum.className = 'plan-durum hata';
      durum.textContent = BILDIK.includes(e.message) ? `${e.message}.`
        : 'Dosya hazırlanamadı. İnternet bağlantınızı denetleyin, sayfayı yenileyip yeniden deneyin.';
    } finally {
      mesgul = false;
      $('#p-indir').removeAttribute('aria-busy');
      dugmeler(false);
    }
  };

  const donem = (ay) => (ay == null ? 'Tüm yıl' : `${Plan.AYLAR[ay]} ${Plan.yil(ay)}`);
  const indirPanel = () => {
    const p = secili;
    $('#p-indir').hidden = !p;
    if (!p) return;
    $('#p-secili-ad').textContent = tamAd(p);
    $('#p-secili-bilgi').textContent = `${p.hafta} haftalık günlük plan · Kaynak: ${p.kaynak} yıllık planı. Seçtiğiniz dönemin her haftası ayrı sayfada.`;
    const dugme = (ay, ad, alt) => el('button', { type: 'button', sinif: `plan-ay${ay == null ? ' tum' : ''}`, disabled: mesgul, onclick: () => {
      const b = bicim(), bl = bilgi();
      isle(async () => [await Plan.uret(p, ay, bl, b), Plan.dosyaAdi(p, ay, b)], `${donem(ay)} için ${b === 'pdf' ? 'PDF' : 'Word'} dosyası hazırlanıyor…`);
    } }, simge('indir'), el('b', {}, ad), el('small', {}, alt));
    $('#p-aylar').replaceChildren(
      dugme(null, 'Tüm yıl', `${p.hafta} hafta`),
      ...p.aylar.map(([a, n]) => dugme(Plan.AYLAR.indexOf(a), a, `${n} hafta`)));
    $('#p-zip').disabled = mesgul;
    onizle();
  };
  $('#p-zip').addEventListener('click', () => {
    if (!secili) return;
    const p = secili, b = bicim(), bl = bilgi();
    isle(async () => [await Plan.aylikZip(p, bl, b, (k, n, ay) => { durum.textContent = `${ay} hazırlanıyor (${k}/${n})…`; }),
      `${p.ad.replace(/-2026-2027$/, '')}-aylik-${b === 'pdf' ? 'pdf' : 'word'}-2026-2027.zip`], 'Aylık dosyalar hazırlanıyor…');
  });

  const grupAd = (p) => (IH.has(p.ders) || /imam hatip/i.test(p.ek || '') ? 'İmam hatip dersleri' : SECMELI.has(p.ders) ? 'Seçmeli dersler' : 'Ortak dersler');
  const kart = (p) => el('button', {
    type: 'button', sinif: `plan-ders ders-${p.ders}`, 'aria-pressed': String(p === secili),
    onclick: () => {
      secili = p;
      if (!mesgul) { durum.className = 'plan-durum'; durum.textContent = ''; }
      durumYaz();
      $$('#p-dersler .plan-ders').forEach((d) => d.setAttribute('aria-pressed', String(d.dataset.ad === p.ad)));
      indirPanel();
      $('#p-indir').scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
      $('#p-indir').focus({ preventScroll: true });
    },
    'data-ad': p.ad,
  }, el('span', { sinif: 'plan-harf', 'aria-hidden': 'true' }, p.dersAd.replace(/^T\.C\. /, '').charAt(0)),
  el('span', { sinif: 'plan-ders-ad' }, el('b', {}, p.dersAd), p.ek ? el('small', {}, p.ek.replace(/[()]/g, '')) : null,
    el('small', { sinif: 'plan-ders-sayi' }, `${p.hafta} hafta${p.siniflar.length > 1 ? ` · ${p.siniflar[0]}-${p.siniflar[p.siniflar.length - 1]}. sınıflar` : ''}`)));

  const dersler = () => {
    const q = $('#p-ara').value.trim();
    const eslesir = (p) => !q || (typeof Arama !== 'undefined' ? Arama.metinEslesir(`${p.dersAd} ${p.ek || ''}`, q)
      : `${p.dersAd} ${p.ek || ''}`.toLocaleLowerCase('tr').includes(q.toLocaleLowerCase('tr')));
    const liste = dizin.filter((p) => p.siniflar.includes(sinif) && eslesir(p));
    const gruplar = ['Ortak dersler', 'Seçmeli dersler', 'İmam hatip dersleri'].map((g) => [g, liste.filter((p) => grupAd(p) === g)]).filter(([, l]) => l.length);
    $('#p-dersler').replaceChildren(...(gruplar.length ? gruplar.map(([g, l]) => el('div', { sinif: 'plan-grup' },
      el('h3', {}, g, el('span', {}, String(l.length))), el('div', { sinif: 'plan-izgara' }, ...l.map(kart))))
      : [el('p', { sinif: 'plan-bos' }, q ? `“${q}” için ${sinif}. sınıfta plan bulunamadı.` : 'Bu sınıf için plan yok.')]));
    $('#p-sonuc').textContent = q ? (liste.length ? `${liste.length} ders bulundu.` : 'Ders bulunamadı.') : '';
  };
  const siniflar = () => {
    const tum = [...new Set(dizin.flatMap((p) => p.siniflar))].sort((a, b) => a - b);
    $('#p-siniflar').replaceChildren(...tum.map((n) => el('button', {
      type: 'button', sinif: 'sekme', 'aria-pressed': String(n === sinif), 'data-n': n,
      onclick: () => {
        sinif = n;
        if (secili && !secili.siniflar.includes(n)) { secili = null; indirPanel(); }
        // sekmeler yeniden kurulmaz: klavye odağı basılan düğmede kalır
        $$('#p-siniflar .sekme').forEach((d) => d.setAttribute('aria-pressed', String(Number(d.dataset.n) === n)));
        durumYaz();
        dersler();
      },
    }, `${n}. sınıf`)));
  };
  $('#p-ara').addEventListener('input', dersler);

  veri('gunluk-planlar.json').then((v) => {
    dizin = v?.planlar || [];
    if (!dizin.length) { $('#p-dersler').replaceChildren(el('p', { sinif: 'plan-bos' }, 'Planlar yüklenemedi. Sayfayı yenileyin.')); return; }
    const prm = new URLSearchParams(location.search);
    const ps = Number(prm.get('sinif'));
    secili = dizin.find((p) => p.ad === prm.get('p')) || null;
    sinif = secili ? (secili.siniflar.includes(ps) ? ps : secili.siniflar[0]) : (dizin.some((p) => p.siniflar.includes(ps)) ? ps : dizin[0].siniflar[0]);
    if (secili || ps) document.title = secili ? `${tamAd(secili)} günlük planları · Ders Kutusu` : `${sinif}. sınıf günlük planları · Ders Kutusu`;
    siniflar();
    dersler();
    indirPanel();
    onizle();
  }).catch((e) => {
    console.error(e);
    $('#p-dersler').replaceChildren(el('p', { sinif: 'plan-bos' }, 'Planlar gösterilemedi. Sayfayı yenileyin.'));
  });
})();
