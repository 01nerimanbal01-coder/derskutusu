// Öğrenme çıktısı yazılıları (DKCIKTI projesi): yazili.html sayfasına hazır kâğıtları ekler.
// Veri: veri/yazili-cikti.json (tablo → çıktılar); PDF'ler /yazili/cikti/<tablo>-<kod>.pdf ve -cevapli.pdf.
// yazili.js'ten bağımsızdır: onun ürettiği öğelere dokunmaz, yalnız ana bölümün ardına kendi bölümünü koyar.
//   yazili.html?sinif=N&ders=<ad>  → o dersin çıktı yazılıları (öğrenci kâğıdı + cevap anahtarı)
//   yazili.html (parametresiz)      → çıktı yazılısı hazır olan sınıf ve dersler

Promise.all([veri('yazili-cikti.json'), ortakVeri]).then(([v, ortak]) => {
  if (!v?.tablolar) return;
  const ana = $('.y-bolum');
  if (!ana) return;
  const p = new URLSearchParams(location.search);
  const sinif = Number(p.get('sinif')), ders = p.get('ders');
  const dersAd = (d) => ortak?.dersler?.dersler?.[d] || d;
  const bolum = (...icerik) => el('section', { sinif: 'bolum y-bolum', id: 'cikti-yazililari', 'aria-labelledby': 'cy-baslik' },
    el('div', { sinif: 'kap' }, ...icerik));
  const baslik = (metin) => el('h2', { id: 'cy-baslik', style: 'font-size:clamp(20px,2.4vw,26px);font-weight:800;margin:0 0 6px' }, metin);
  const aciklama = 'Her kâğıt tek bir öğrenme çıktısını ölçer: 2 sayfa, 6–8 açık uçlu soru, 40 dakika, 100 puan. '
    + 'Sorular MEB ders kitabına dayanır; öğrenci kâğıdındaki karekod cevap anahtarını açar.';

  const liste = v.tablolar[`${sinif}-${ders}`];
  if (liste) {
    const kalem = (c) => el('li', {
      style: 'display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;justify-content:space-between;'
        + 'padding:14px 16px;border:1px solid var(--cizgi);border-radius:14px;background:var(--yuzey)' },
      el('div', { style: 'flex:1 1 340px;min-width:0' },
        el('div', { style: 'font-weight:700' }, c.kod),
        el('div', {}, c.ifade),
        el('div', { style: 'font-size:14px;color:var(--soluk);margin-top:2px' }, `${c.konu} · ${c.soru} soru`)),
      el('div', { sinif: 'g-dugmeler' },
        el('a', { sinif: 'dugme ana', href: `${v.klasor}${c.dosya}.pdf`, download: '',
          'aria-label': `${c.kod} sınav kâğıdı (PDF)` }, simge('indir'), 'Sınav kâğıdı'),
        el('a', { sinif: 'dugme', href: `${v.klasor}${c.dosya}-cevapli.pdf`, download: '',
          'aria-label': `${c.kod} cevap anahtarı (PDF)` }, simge('indir'), 'Cevap anahtarı')));
    ana.after(bolum(
      baslik(`${sinif}. sınıf ${dersAd(ders)}: öğrenme çıktısı yazılıları`),
      el('p', { style: 'margin:0 0 16px;color:var(--soluk)' }, aciklama),
      el('ol', { style: 'list-style:none;padding:0;margin:0;display:grid;gap:10px' }, ...liste.map(kalem))));
    // Sayfa başına, bölüme inen kısa bağlantı
    const gecis = $('#y-siniflar');
    if (gecis) gecis.after(el('p', { style: 'margin:12px 0 0' },
      el('a', { href: '#cikti-yazililari' }, `Öğrenme çıktısı yazılıları: ${liste.length} hazır kâğıt`)));
    // Bölüm sayfa açıldıktan sonra eklendiği için #cikti-yazililari bağlantısıyla gelindiyse oraya kaydır. yazili.js senaryo
    // tablosunu ayrıca çizer ve bölümü aşağı iter; kaydırma tablo çizildikten sonra (en geç 2,5 sn) bir kez yapılır.
    if (location.hash === '#cikti-yazililari') {
      let yapildi = false;
      const git = () => { if (!yapildi) { yapildi = true; $('#cikti-yazililari').scrollIntoView(); } };
      const tablo = $('#y-tablo');
      if (tablo && !tablo.childElementCount) {
        const g = new MutationObserver(() => { g.disconnect(); requestAnimationFrame(git); });
        g.observe(tablo, { childList: true });
        setTimeout(() => { g.disconnect(); git(); }, 2500);
      } else git();
    }
    return;
  }
  if (p.has('sinif') || p.has('ders')) return;   // seçili dersin çıktı yazılısı henüz yok

  // Giriş sayfası: çıktı yazılısı hazır olan sınıf ve dersler
  const gruplar = {};
  for (const anahtar of Object.keys(v.tablolar)) {
    const m = /^(\d+)-(.+)$/.exec(anahtar);
    if (m) (gruplar[m[1]] = gruplar[m[1]] || []).push(m[2]);
  }
  const siniflar = Object.keys(gruplar).map(Number).sort((a, b) => a - b);
  if (!siniflar.length) return;
  ana.after(bolum(
    baslik('Öğrenme çıktısı yazılıları'),
    el('p', { style: 'margin:0 0 6px;color:var(--soluk)' }, aciklama),
    ...siniflar.map((n) => el('div', { style: 'margin:18px 0' },
      el('h3', { style: 'font-size:18px;margin:0 0 10px' }, `${n}. sınıf`),
      el('div', { sinif: 'g-dugmeler' }, ...gruplar[n].map((d) => el('a', { sinif: 'dugme ana',
        href: `?sinif=${n}&ders=${encodeURIComponent(d)}#cikti-yazililari` }, simge('indir'),
        `${dersAd(d)} (${v.tablolar[`${n}-${d}`].length})`)))))));
});
