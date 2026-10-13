// Çevrimiçi test (test.html): gerçek tarayıcıda kurulum, bütün soru türleri, anında/sonunda dönüt, yenilemede sürdürme, sonuç ve yanlışları tekrar.
// Yalnız izole test sunucusu; canlı siteye veri göndermez.
const { chromium, webkit, expect } = require('@playwright/test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const http = require('node:http');
const root = path.resolve(__dirname, '../public');
const output = path.resolve('online-test-results');
const report = { checks: [], errors: [] };
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.ico': 'image/x-icon' };
const server = http.createServer(async (req, res) => {
  const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  const file = path.resolve(root, '.' + (pathname === '/' ? '/index.html' : pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  try { res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream' }).end(await fs.readFile(file)); }
  catch { res.writeHead(404).end(); }
});
async function cevapla(page, tur) {
  if (tur === 'coktan') await page.locator('.t-soru .etk-sec').first().click();
  else if (tur === 'dy') for (const satir of await page.locator('.etk-dy-satir').all()) await satir.locator('button').first().click();
  else if (tur === 'bosluk') { const n = await page.locator('.etk-bosluk-yer').count(); for (let k = 0; k < n; k++) await page.locator('.etk-kelime:not([hidden])').first().click(); }
  else if (tur === 'eslestir') { const n = await page.locator('[data-sol]').count(); for (let k = 0; k < n; k++) { await page.locator(`[data-sol="${k}"]`).click(); await page.locator(`[data-sag="${k}"]`).click(); } }
  else if (tur === 'siralama') await page.locator('.t-soru .etk-kontrol').click();
  else if (tur === 'acik') { await page.getByRole('button', { name: 'Cevabı göster' }).click(); await page.getByRole('button', { name: 'Bildim' }).click(); }
}
async function run(engine, name, base) {
  const browser = await engine.launch();
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, hasTouch: true });
  const page = await context.newPage(); page.setDefaultTimeout(10000);
  page.on('pageerror', (e) => report.errors.push({ browser: name, url: page.url(), message: e.message }));
  await context.route('**/*', (route) => route.request().url().startsWith(base) ? route.continue() : route.abort());
  const ok = (text) => { report.checks.push({ browser: name, check: text }); console.log(`${name}: ${text}`); };
  try {
    // Kurulum: adresle ön seçim, havuz sayısı, konu/çıktı daralması
    await page.goto(base + '/test.html?sinif=5&ders=matematik&adet=0');
    await expect(page.locator('#t-havuz')).toContainText('Havuzda');
    await expect(page.locator('#t-ders')).toHaveValue('matematik');
    const tumu = Number((await page.locator('#t-havuz').textContent()).match(/Havuzda (\d+)/)[1]);
    assert(tumu >= 20, 'Havuz küçük');
    await page.selectOption('#t-konu', { index: 2 });
    const konu = Number((await page.locator('#t-havuz').textContent()).match(/Havuzda (\d+)/)[1]);
    assert(konu > 0 && konu < tumu, 'Konu süzgeci havuzu daraltmadı');
    assert((await page.locator('#t-cikti option').count()) >= 2, 'Çıktı seçenekleri yok');
    await page.selectOption('#t-konu', '');
    ok('Kurulum: adres ön seçimi, konu ve çıktı daralması');

    // Anında dönüt, havuzun tamamı, her tür cevaplanır
    await page.selectOption('#t-donut', 'aninda');
    await page.click('#t-basla');
    await expect(page.locator('.t-ilerleme-yazi')).toContainText('Soru 1 /');
    const toplam = Number((await page.locator('.t-ilerleme-yazi').textContent()).match(/\/ (\d+)/)[1]);
    assert.equal(toplam, tumu, 'Havuzdaki hepsi seçilmeli');
    const turler = new Set();
    for (let i = 0; i < toplam; i++) {
      const tur = (await page.locator('.t-soru').getAttribute('class')).match(/t-(coktan|dy|bosluk|eslestir|siralama|acik)/)[1];
      turler.add(tur);
      await expect(page.locator('#t-sonraki')).toBeDisabled();   // önce cevapla
      await cevapla(page, tur);
      await expect(page.locator('.t-soru .etk-geri')).toBeVisible();
      await expect(page.locator('#t-sonraki')).toBeEnabled();
      await page.click('#t-sonraki');
    }
    assert(turler.size >= 4, 'Soru türleri çeşitlenmedi: ' + [...turler]);
    await expect(page.locator('#t-sonuc')).toBeVisible();
    await expect(page.locator('.t-sonuc-kart h2')).toContainText(`/ ${toplam} doğru`);
    assert.equal(await page.locator('.t-gozden-oge').count(), toplam);
    await page.screenshot({ path: path.join(output, name + '-sonuc.png'), fullPage: true });
    const gecmis = await page.evaluate(() => JSON.parse(localStorage.getItem('test-gecmis')));
    assert(gecmis?.[0]?.toplam === toplam, 'Sonuç geçmişe yazılmadı');
    ok(`Anında dönüt: ${toplam} soru, türler ${[...turler].join(', ')}, sonuç ve geçmiş`);

    // Sonunda dönüt, klavye, geri gelince seçim korunur, yenilemede sürdürme, boş sorularla bitirme, yanlışları tekrar
    await page.goto(base + '/test.html?sinif=5&ders=fen-bilimleri&tur=coktan&adet=10&donut=sonunda');
    await expect(page.locator('#t-basla')).toBeEnabled();
    await page.click('#t-basla');
    await expect(page.locator('.t-ilerleme-yazi')).toContainText('Soru 1 / 10');
    await expect(page.locator('#t-sonraki')).toBeEnabled();
    await page.locator('.t-soru-metin').focus();
    await page.keyboard.press('2');
    await expect(page.locator('.etk-sec.secili')).toHaveCount(1);
    await expect(page.locator('.t-soru .etk-geri')).toBeHidden();
    await page.keyboard.press('Enter');
    await expect(page.locator('.t-ilerleme-yazi')).toContainText('Soru 2 / 10');
    await page.keyboard.press('ArrowLeft');
    await expect(page.locator('.etk-sec.secili')).toHaveCount(1);
    await page.keyboard.press('ArrowRight');
    await page.reload();
    await expect(page.locator('#t-test')).toBeVisible();
    await expect(page.locator('.t-ilerleme-yazi')).toContainText('Soru 2 / 10');
    page.once('dialog', (d) => d.accept());
    await page.click('#t-bitir');
    await expect(page.locator('#t-sonuc')).toBeVisible();
    assert.equal(await page.locator('.t-gozden-oge.bos').count(), 9, 'Boş sorular işaretlenmeli');
    await page.getByRole('button', { name: /Yanlışları tekrar/ }).click();
    await expect(page.locator('.t-ilerleme-yazi')).toContainText('yanlışlar');
    ok('Sonunda dönüt, klavye, sürdürme, boş bitirme ve yanlışları tekrar');

    // Dar ekran: taşma yok
    await page.setViewportSize({ width: 360, height: 780 });
    await page.goto(base + '/test.html?sinif=5&ders=matematik&basla=1');
    await expect(page.locator('#t-test')).toBeVisible();
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'Dar ekranda yatay taşma');
    await page.screenshot({ path: path.join(output, name + '-360.png') });
    ok('360 piksel: otomatik başlama ve taşma yok');
  } catch (error) {
    report.errors.push({ browser: name, error: error.message });
    await page.screenshot({ path: path.join(output, name + '-failure.png') }).catch(() => {});
    throw error;
  } finally {
    await fs.writeFile(path.join(output, 'report.json'), JSON.stringify(report, null, 2));
    await browser.close();
  }
}
(async () => {
  await fs.mkdir(output, { recursive: true });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const base = 'http://127.0.0.1:' + server.address().port;
  try {
    await run(chromium, 'chromium', base); await run(webkit, 'webkit', base);
    assert.deepEqual(report.errors, []);
    console.log(JSON.stringify({ status: 'passed', checks: report.checks.length }));
  } finally { server.close(); }
})().catch((error) => { console.error(error); process.exitCode = 1; });
