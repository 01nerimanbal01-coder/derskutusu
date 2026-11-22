const assert = require('node:assert/strict');
const { readFile } = require('node:fs/promises');
const { createServer } = require('node:http');
const path = require('node:path');
const { chromium, webkit, expect } = require('@playwright/test');

const site = path.resolve(__dirname, '../public');
const types = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml', '.woff': 'font/woff' };

async function main() {
  const server = createServer(async (request, response) => {
    try {
      const { pathname } = new URL(request.url, 'http://localhost');
      const file = path.resolve(site, '.' + (pathname === '/' ? '/index.html' : decodeURIComponent(pathname)));
      if (!file.startsWith(site + path.sep)) throw new Error('Geçersiz yol');
      const data = await readFile(file);
      response.writeHead(200, { 'Content-Type': types[path.extname(file)] || 'application/octet-stream' }).end(data);
    } catch {
      response.writeHead(404).end();
    }
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const base = 'http://127.0.0.1:' + server.address().port;
  const { icerikler } = JSON.parse(await readFile(path.join(site, 'veri/icerikler.json'), 'utf8'));
  const available = new Map(icerikler.filter((x) => x.goruntule).map((x) => [new URL(x.goruntule, base).href, x]));

  async function openPage(browser, options = {}) {
    const context = await browser.newContext({ reducedMotion: 'reduce', ...options });
    await context.route('**/*', (route) => new URL(route.request().url()).origin === base ? route.continue() : route.abort());
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', (error) => errors.push(error.message));
    await page.clock.setFixedTime(new Date('2026-11-22T12:00:00+03:00'));
    await page.goto(base, { waitUntil: 'load' });
    await expect(page.locator('.renkli-ust')).toBeVisible();
    return { page, context, errors };
  }

  async function interactionChecks(browser, name) {
    const { page, context, errors } = await openPage(browser, { viewport: { width: 320, height: 720 }, isMobile: true, hasTouch: true });
    const menu = page.getByRole('button', { name: 'Menü', exact: true });
    const search = page.locator('.ara-dugme');
    const topic = page.locator('#hb-konu');
    await expect(menu).toBeVisible();
    const titleBox = await page.locator('.renkli-marka').boundingBox();
    const searchBox = await search.boundingBox();
    assert(Math.abs(titleBox.y + titleBox.height / 2 - searchBox.y - searchBox.height / 2) < 4, `${name}: 320 px başlık tek satıra sığmalı`);
    await menu.tap();
    await expect(menu).toHaveAttribute('aria-expanded', 'true');
    await search.tap();
    await expect(menu).toHaveAttribute('aria-expanded', 'false');
    await expect(topic).toBeFocused();

    const selected = page.locator('#slayt-1 a');
    await selected.focus();
    await selected.press('ArrowRight');
    await expect(selected).toBeFocused();
    await expect(page.locator('#slayt-1')).toHaveAttribute('aria-hidden', 'false');
    await page.getByRole('button', { name: 'Sonraki slayt' }).press('ArrowRight');
    await expect(page.locator('#slayt-2')).toHaveAttribute('aria-hidden', 'false');
    await expect(page.locator('#slayt-dur')).toBeHidden();

    await page.locator('#hb-sinif').selectOption('10');
    await expect(page.locator('#hb-ders option[value="fizik"]')).toBeAttached();
    await page.locator('#hb-ders').selectOption('fizik');
    const suggestions = page.locator('#hb-sonuc li a');
    await expect(suggestions.first()).not.toContainText('Seçtiğin içerikleri aç');
    for (const uri of await suggestions.evaluateAll((links) => links.slice(0, -1).map((link) => link.href))) {
      const row = available.get(uri);
      assert(row?.sinif === 10 && row.ders === 'fizik' && row.tarih <= '2026-11-22', `${name}: öneri tarih veya filtre dışı`);
    }
    await page.locator('#hb-sinif').selectOption('');
    await page.locator('#hb-ders').selectOption('');
    await topic.fill('التَّسَوُّقُ');
    await expect(suggestions.first()).toHaveAttribute('href', /\/calisma\/\d+-arapca-/);
    await topic.fill('___');
    await expect(suggestions).toHaveCount(1);

    await expect(page.locator('[data-son-ekleme] time')).toBeVisible();
    await expect(page.locator('[data-yeni-icerikler] li')).toHaveCount(8);
    const dates = await page.locator('[data-yeni-icerikler] time').evaluateAll((nodes) => nodes.map((node) => node.dateTime));
    assert(dates.length === 8 && dates.every((date, i) => !i || dates[i - 1] >= date), `${name}: yeni içerikler tarih sırasıyla gitmeli`);
    assert.deepEqual(errors, [], `${name}: JavaScript hatası`);
    await context.close();
  }

  async function layoutChecks(browser, name) {
    const { page, context } = await openPage(browser, { viewport: { width: 390, height: 844 }, colorScheme: 'dark' });
    const colors = await page.locator('#sosyal h2').evaluate((title) => [getComputedStyle(title).color, getComputedStyle(title.closest('section')).backgroundColor]);
    const luminance = (rgb) => rgb.match(/\d+/g).slice(0, 3).map(Number).map((n) => n / 255)
      .map((n) => n <= 0.04045 ? n / 12.92 : ((n + 0.055) / 1.055) ** 2.4)
      .reduce((sum, value, i) => sum + value * [0.2126, 0.7152, 0.0722][i], 0);
    const [x, y] = colors.map(luminance);
    assert((Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05) >= 4.5, `${name}: sosyal başlık kontrastı ${colors}`);
    for (const width of [320, 360, 390, 768, 1440]) {
      await page.setViewportSize({ width, height: 860 });
      for (const selector of ['.renkli-menu', '.hizli', '.sinif-kart', '[data-yeni-icerikler]']) {
        const box = await page.locator(selector).boundingBox();
        assert(box && box.x >= -1 && box.x + box.width <= width + 1, `${name}: ${width} px taşması ${selector}`);
      }
    }
    await context.close();
  }

  try {
    for (const engine of [chromium, webkit]) {
      const browser = await engine.launch();
      try {
        await interactionChecks(browser, engine.name());
        await layoutChecks(browser, engine.name());
        console.log(`${engine.name()}: menü, odak, slayt, öneri, tarih, koyu tema ve 5 ekran genişliği başarılı.`);
      } finally {
        await browser.close();
      }
    }
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
