// Sekiz Kapı · 6. kapı: yerleşim denetimi (araclar/sekiz_kapi.py bu betiği çalıştırır).
// Gerçek Chromium'da seçili sayfaları üç genişlikte açar; yatay taşma, üst üste binen metinler,
// sayfa betiği hataları ve yüklenemeyen yerel kaynakları JSON olarak yazar. Canlı siteyi açmaz.
//
//   node tests/sekiz-kapi-yerlesim.cjs [--cikti sekiz-kapi-sonuc/yerlesim.json] [--genislikler 1366,768,360]
//                                      [--rotalar /,/sinav.html] [--ornek 3] [--ekran-goruntusu]
//
// Playwright: önce bulut oturumunda kurulu olan "playwright", yoksa "@playwright/test" (CI kurar).
const fs = require('node:fs/promises');
const path = require('node:path');
const http = require('node:http');

function playwright() {
  for (const ad of ['playwright', '@playwright/test']) {
    try { return require(ad); } catch {}
  }
  console.error('Playwright bulunamadı: npm install @playwright/test (ayrıntı: KURULUM.md → Sekiz Kapı)');
  process.exit(3);
}

const arg = (ad, varsayilan) => { const i = process.argv.indexOf(ad); return i > 0 && process.argv[i + 1] ? process.argv[i + 1] : varsayilan; };
const root = path.resolve(__dirname, '../public');
const cikti = path.resolve(arg('--cikti', 'sekiz-kapi-sonuc/yerlesim.json'));
const genislikler = arg('--genislikler', '1366,768,360').split(',').map(Number);
const ornekAdet = Number(arg('--ornek', '3'));
const ekranGoruntusu = process.argv.includes('--ekran-goruntusu');

// Her denetimde bakılan sayfalar; özet ve çalışma kâğıdı sayfalarından ayrıca örnek alınır.
const SABIT_ROTALAR = ['/', '/ogrenci.html', '/ogretmen.html', '/icerikler.html', '/sinif.html?no=5', '/sinif.html?no=9',
  '/yazili.html', '/yazili.html?sinif=5&ders=matematik', '/sinav.html?sinif=5', '/sinav.html?sinif=8', '/planlar.html',
  '/belgeler.html', '/kelime.html', '/arapca.html', '/kpss.html', '/ara.html?q=matematik', '/hakkimizda.html', '/iletisim.html', '/404.html'];

const mime = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.ico': 'image/x-icon', '.webmanifest': 'application/manifest+json', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.pdf': 'application/pdf' };
const server = http.createServer(async (req, res) => {
  const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  const file = path.resolve(root, '.' + (pathname.endsWith('/') ? pathname + 'index.html' : pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  try { res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-store' }).end(await fs.readFile(file)); }
  catch { res.writeHead(404).end(); }
});

// Sayfa içinde çalışır: yatay taşma + metin üst üste binmesi.
function sayfaOlc() {
  const SKIP = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'SVG', 'OPTION', 'SELECT', 'CANVAS', 'TEXTAREA', 'IFRAME']);
  const bellek = new Map();
  // Kendisi ya da atalarından biri görünmez, katman (fixed/absolute), kapalı <details> içi, arka yüz ya da hareketli mi?
  const disarida = (n) => {
    if (!n || n === document.body) return false;
    if (bellek.has(n)) return bellek.get(n);
    const cs = getComputedStyle(n);
    let d = cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0 || cs.position === 'fixed' || cs.position === 'absolute'
      || cs.backfaceVisibility === 'hidden' || (cs.animationName && cs.animationName !== 'none')
      || (n.parentElement && n.parentElement.tagName === 'DETAILS' && !n.parentElement.open && n.tagName !== 'SUMMARY');
    if (!d) d = disarida(n.parentElement);
    bellek.set(n, d); return d;
  };
  const kirpar = (n) => { for (let e = n.parentElement; e && e !== document.documentElement; e = e.parentElement) { const o = getComputedStyle(e).overflowX; if (o === 'hidden' || o === 'clip' || o === 'auto' || o === 'scroll') return true; } return false; };
  const yol = (n) => { const p = []; let e = n; while (e && e !== document.body && p.length < 4) { p.unshift(e.tagName.toLowerCase() + (typeof e.className === 'string' && e.className.trim() ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '') + (e.id ? '#' + e.id : '')); e = e.parentElement; } return p.join('>'); };

  // 1. Yatay taşma: sayfa genişliği pencereden büyükse, kırpılmayan taşkın öğeler listelenir
  const tasma = [];
  if (document.documentElement.scrollWidth > innerWidth + 1) {
    const taskin = [];
    for (const n of document.body.querySelectorAll('*')) {
      const b = n.getBoundingClientRect(); if (!b.width) continue;
      const cs = getComputedStyle(n); if (cs.position === 'fixed' || cs.position === 'absolute') continue;
      if ((b.right > innerWidth + 1 || b.left < -1) && !kirpar(n)) taskin.push(n);
    }
    // yalnız en dıştaki taşkın öğeler: içindekiler onunla birlikte taşar
    for (const n of taskin) {
      if (taskin.some((u) => u !== n && u.contains(n))) continue;
      const b = n.getBoundingClientRect();
      tasma.push({ oge: yol(n), genislik: Math.round(b.width), sag: Math.round(b.right), metin: (n.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50) });
      if (tasma.length >= 6) break;
    }
  }

  // 2. Üst üste binme: doğrudan metin taşıyan görünür öğelerin satır kutuları (getClientRects) birbirine giriyor mu?
  const ogeler = [];
  for (const n of document.body.querySelectorAll('*')) {
    if (SKIP.has(n.tagName) || n.closest('svg')) continue;
    const metin = [...n.childNodes].filter((c) => c.nodeType === 3).map((c) => c.textContent.trim()).join(' ').trim();
    if (!metin || disarida(n)) continue;
    const kutular = [...n.getClientRects()].filter((r) => r.width >= 3 && r.height >= 3);
    if (kutular.length) ogeler.push({ n, kutular, metin: metin.slice(0, 40) });
  }
  const binme = [];
  const gorulen = new Set();
  for (let i = 0; i < ogeler.length && binme.length < 12; i++) {
    for (let j = i + 1; j < ogeler.length && binme.length < 12; j++) {
      const a = ogeler[i], b = ogeler[j];
      if (a.n.contains(b.n) || b.n.contains(a.n)) continue;
      let bulundu = null;
      for (const ra of a.kutular) {
        for (const rb of b.kutular) {
          const ix = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
          const iy = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
          if (ix < 3 || iy < 3) continue;
          const oran = (ix * iy) / Math.min(ra.width * ra.height, rb.width * rb.height);
          if (oran >= 0.35) { bulundu = { oran, cx: Math.max(ra.left, rb.left) + ix / 2, cy: Math.max(ra.top, rb.top) + iy / 2 }; break; }
        }
        if (bulundu) break;
      }
      if (!bulundu) continue;
      // Kesişim noktasında gerçekten üstte boyanan öğe ikisinden biri mi? (başka bir katman kapatıyorsa sayılmaz)
      const sayfaY = bulundu.cy + scrollY;
      scrollTo(0, Math.max(0, sayfaY - innerHeight / 2));
      const ust = document.elementFromPoint(bulundu.cx, sayfaY - scrollY);
      if (!ust || !(a.n.contains(ust) || b.n.contains(ust))) continue;
      const anahtar = yol(a.n) + '|' + yol(b.n);
      if (gorulen.has(anahtar)) continue;
      gorulen.add(anahtar);
      binme.push({ a: yol(a.n), aMetin: a.metin, b: yol(b.n), bMetin: b.metin, oran: +bulundu.oran.toFixed(2), x: Math.round(bulundu.cx), y: Math.round(sayfaY) });
    }
  }
  scrollTo(0, 0);
  return { ogeSayisi: ogeler.length, sayfaGenisligi: document.documentElement.scrollWidth, pencere: innerWidth, tasma, binme, baslik: document.title, h1: !!document.querySelector('h1') };
}

async function rotalar() {
  const sec = (klasor, onek) => fs.readdir(path.join(root, klasor)).then((d) => {
    const l = d.filter((f) => f.endsWith('.html')).sort();
    if (!l.length || !ornekAdet) return [];
    const adim = Math.max(1, Math.floor(l.length / ornekAdet));
    return [...new Set(Array.from({ length: ornekAdet }, (_, i) => l[Math.min(l.length - 1, i * adim)]))].map((f) => onek + f);
  }).catch(() => []);
  const ozel = arg('--rotalar', '');
  if (ozel) return ozel.split(',');
  return [...SABIT_ROTALAR, ...(await sec('ozet', '/ozet/')), ...(await sec('calisma', '/calisma/')), ...(await sec('kpss', '/kpss/'))];
}

(async () => {
  const { chromium } = playwright();
  await fs.mkdir(path.dirname(cikti), { recursive: true });
  const kareler = path.join(path.dirname(cikti), 'ekran');
  if (ekranGoruntusu) await fs.mkdir(kareler, { recursive: true });
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  const base = 'http://127.0.0.1:' + server.address().port;
  const liste = await rotalar();
  const rapor = { baslangic: new Date().toISOString(), genislikler, sayfalar: [], tarayici: 'chromium' };
  const browser = await chromium.launch();
  try {
    const context = await browser.newContext({ viewport: { width: 1366, height: 900 }, hasTouch: true, colorScheme: 'light', reducedMotion: 'reduce', locale: 'tr-TR' });
    await context.route('**/*', (route) => route.request().url().startsWith(base) ? route.continue() : route.abort());
    // Reklam izni penceresi her sayfada açılır; ölçümü kapatmasın diye önceden karar verilmiş sayılır
    await context.addInitScript(() => { try { localStorage.setItem('dk-reklam', 'hayir'); } catch {} });
    const page = await context.newPage();
    page.setDefaultTimeout(15000);
    let hatalar = [], kaynaklar = [];
    page.on('pageerror', (e) => hatalar.push(e.message.slice(0, 200)));
    page.on('response', (r) => { if (r.url().startsWith(base) && r.status() >= 400) kaynaklar.push(r.url().slice(base.length) + ' (' + r.status() + ')'); });
    for (const genislik of genislikler) {
      await page.setViewportSize({ width: genislik, height: 900 });
      for (const rota of liste) {
        hatalar = []; kaynaklar = [];
        const kayit = { rota, genislik };
        try {
          await page.goto(base + rota, { waitUntil: 'networkidle' }).catch(() => page.goto(base + rota, { waitUntil: 'load' }));
          await page.addStyleTag({ content: 'aside.reklam-izin{display:none!important}' }).catch(() => {});
          await page.evaluate(() => document.fonts.ready);
          await page.waitForTimeout(250);
          Object.assign(kayit, await page.evaluate(sayfaOlc));
          if (!kayit.baslik) hatalar.push('<title> boş');
          if (ekranGoruntusu && (kayit.tasma.length || kayit.binme.length)) {
            const ad = (rota.replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '') || 'ana') + '-' + genislik + '.png';
            await page.screenshot({ path: path.join(kareler, ad), fullPage: true }).catch(() => {});
            kayit.ekran = path.join('ekran', ad);
          }
        } catch (e) {
          hatalar.push('sayfa açılamadı: ' + e.message.slice(0, 160));
          Object.assign(kayit, { tasma: [], binme: [] });
        }
        kayit.betikHatalari = [...new Set(hatalar)];
        kayit.yuklenemeyen = [...new Set(kaynaklar)].filter((k) => !k.startsWith('/404.html'));
        rapor.sayfalar.push(kayit);
        const sorun = kayit.tasma.length + kayit.binme.length + kayit.betikHatalari.length + kayit.yuklenemeyen.length;
        console.log(`${genislik}px ${rota}: ${sorun ? sorun + ' bulgu' : 'temiz'}${kayit.tasma.length ? ' · yatay taşma ' + kayit.sayfaGenisligi + '>' + kayit.pencere : ''}${kayit.binme.length ? ' · binme ' + kayit.binme.length : ''}`);
      }
    }
  } finally {
    await browser.close();
    server.close();
  }
  rapor.bitis = new Date().toISOString();
  rapor.toplam = { sayfa: rapor.sayfalar.length, tasma: rapor.sayfalar.filter((s) => s.tasma.length).length, binme: rapor.sayfalar.reduce((n, s) => n + s.binme.length, 0),
    betikHatasi: rapor.sayfalar.reduce((n, s) => n + s.betikHatalari.length, 0), yuklenemeyen: rapor.sayfalar.reduce((n, s) => n + s.yuklenemeyen.length, 0) };
  await fs.writeFile(cikti, JSON.stringify(rapor, null, 1));
  console.log(JSON.stringify(rapor.toplam));
  process.exitCode = (rapor.toplam.tasma + rapor.toplam.binme + rapor.toplam.betikHatasi + rapor.toplam.yuklenemeyen) ? 1 : 0;
})().catch((e) => { console.error(e); process.exitCode = 2; });
