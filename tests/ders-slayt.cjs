// Gerçek, geçici tarayıcı bağlamları. Kullanıcının tarayıcısını veya canlı siteyi açmaz.
const { chromium, webkit, expect } = require('@playwright/test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const http = require('node:http');
const root = path.resolve(__dirname, '../public');
const results = path.resolve('slayt-test-results');
const report = [];
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.ico': 'image/x-icon' };
const server = http.createServer(async (req, res) => {
  const file = path.resolve(root, '.' + decodeURIComponent(new URL(req.url, 'http://localhost').pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  try { const data = await fs.readFile(file); res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-store' }).end(data); }
  catch { res.writeHead(404).end(); }
});

async function run(engine, name, base) {
  const browser = await engine.launch();
  const context = await browser.newContext({ viewport: { width: 1366, height: 900 }, hasTouch: true });
  const page = await context.newPage();
  page.setDefaultTimeout(10000);
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await context.route('**/*', route => route.request().url().startsWith(base) ? route.continue() : route.abort());
  const record = { browser: name, checks: [], fullscreen: null };
  const ok = text => { record.checks.push(text); console.log(name + ': ' + text); };
  const action = name => page.locator('.ds [data-action="' + name + '"]');
  const current = () => page.locator('.ds-slide:not([hidden])');
  const session = () => page.evaluate(() => JSON.parse(sessionStorage.getItem('derskutusu:slayt:v2:' + location.pathname)));
  const inkPixels = () => page.locator('.ds-ink canvas').first().evaluate(c => {
    const data = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
    let n = 0; for (let i = 3; i < data.length; i += 4) if (data[i]) n++; return n;
  });
  try {
    await page.goto(base + '/ozet/5-matematik-hafta-1.html');
    await page.locator('#ders-slayt-ac').click();
    await expect(page.locator('.ds')).toBeVisible();
    await expect(page.locator('.ds-progress')).toHaveText('1 / 23 slayt');
    await expect(current().locator('.ozet-ust')).toBeVisible();
    assert(await current().locator('.ozet-cikti li').first().evaluate(p => parseFloat(getComputedStyle(p).fontSize) >= 24), 'Öğrenme çıktısı tahta için küçük kaldı');
    await action('next').click();
    await expect(page.locator('.ds-progress')).toHaveText('2 / 23 slayt');
    await expect(current().locator('h2')).toContainText('Nokta');
    assert(await current().locator('.bolum-metin p').first().evaluate(p => parseFloat(getComputedStyle(p).fontSize) >= 24), 'Konu metni tahta için küçük kaldı');
    const hidden = await current().locator('[hidden]').count();
    await action('reveal').click();
    assert((await current().locator('[hidden]').count()) < hidden);
    const firstSet = (await session()).ids;
    await page.screenshot({ path: path.join(results, name + '-desktop.png') });
    ok('Giriş, kazanımlar, konu açılışı ve adım adım gösterim');
    while (await action('reveal').isEnabled()) await action('next').click();

    await action('ink').click();
    await expect(page.locator('.ds-ink')).toBeVisible();
    const box = await page.locator('.ds-ink canvas.tahta-ust').boundingBox();
    assert(box && box.width > 100 && box.height > 100);
    await page.mouse.move(box.x + 50, box.y + 60); await page.mouse.down();
    await page.mouse.move(box.x + 210, box.y + 100, { steps: 15 }); await page.mouse.up();
    await expect.poll(inkPixels).toBeGreaterThan(10);
    await action('next').click(); assert.equal(await inkPixels(), 0);
    await action('previous').click(); await expect.poll(inkPixels).toBeGreaterThan(10);
    await page.screenshot({ path: path.join(results, name + '-ink.png') });
    await page.keyboard.press('Escape');
    await expect(page.locator('.ds-ink')).toBeHidden(); await expect(page.locator('.ds')).toBeVisible();
    await action('close').click(); await expect(page.locator('.ds')).toBeHidden();
    await expect(page.locator('#ders-slayt-ac')).toBeFocused();
    await page.locator('#ders-slayt-ac').click(); await action('ink').click();
    await expect.poll(inkPixels).toBeGreaterThan(10); await action('ink').click();
    ok('Gerçek pointer çizimi, slayta özel çizim, ESC, kapanıp devam etme');

    await action('restart').click(); assert.deepEqual((await session()).ids, firstSet);
    await action('ink').click(); assert.equal(await inkPixels(), 0); await action('ink').click();
    await expect(page.locator('.ds-progress')).toHaveText('1 / 23 slayt');
    ok('Aynı sette yeniden başlatma çizimleri sıfırlar');

    await action('fullscreen').click();
    if (name === 'chromium') {
      await expect.poll(() => page.evaluate(() => document.fullscreenElement?.className)).toBe('ds-shell');
      record.fullscreen = 'entered';
      await action('close').click();
      await expect.poll(() => page.evaluate(() => document.fullscreenElement === null)).toBe(true);
      await page.locator('#ders-slayt-ac').click();
      await action('fullscreen').click();
      await expect.poll(() => page.evaluate(() => document.fullscreenElement?.className)).toBe('ds-shell');
      await action('fullscreen').click();
      await expect.poll(() => page.evaluate(() => document.fullscreenElement === null)).toBe(true);
    } else {
      await expect.poll(async () => (await page.evaluate(() => Boolean(document.fullscreenElement))) || (await page.locator('.ds-notice').textContent()).includes('bu pencerede')).toBe(true);
      record.fullscreen = await page.evaluate(() => document.fullscreenElement ? 'entered' : 'graceful-window-fallback');
      if (record.fullscreen === 'entered') await action('fullscreen').click();
    }
    ok('Tam ekran ve güvenli çıkış: ' + record.fullscreen);

    await page.locator('.ds [data-control="mode"]').selectOption('questions');
    const seen = new Set(), types = new Set();
    let answeredId = null;
    for (let round = 0; round < 4; round++) {
      const ids = (await session()).ids;
      for (const id of ids) { assert(!seen.has(id), 'Havuz bitmeden tekrar'); seen.add(id); }
      for (let i = 0; i < ids.length; i++) {
        const slide = current();
        if (await slide.locator('details').count()) {
          types.add('example'); await action('reveal').click(); await expect(slide.locator('details')).toHaveAttribute('open', '');
        } else if (await slide.locator('.etk-coktan').count()) {
          types.add('coktan');
          const answer = await slide.locator('.etk-coktan').getAttribute('data-dogru');
          await slide.locator('.etk-sec[data-i="' + answer + '"]').click();
          await expect(slide.locator('.etk-puan')).toContainText('1 / 1 doğru');
          await slide.locator('.etk-sec[data-i="' + answer + '"]').evaluate(b => b.click());
          await expect(slide.locator('.etk-puan')).toContainText('1 / 1 doğru');
          answeredId = ids[i];
        } else if (await slide.locator('.etk-dy').count()) {
          types.add('dy');
          for (const row of await slide.locator('.etk-dy-satir').all()) {
            await row.locator('[data-c="' + await row.getAttribute('data-dogru') + '"]').click();
          }
          await expect(slide.locator('.etk-puan')).toContainText('Tamamlandı');
        } else if (await slide.locator('.etk-eslestir').count()) {
          types.add('eslestir');
          for (const left of await slide.locator('[data-sol]').all()) {
            await left.click(); await slide.locator('[data-sag="' + await left.getAttribute('data-sol') + '"]').click();
          }
          await expect(slide.locator('.etk-geri')).toContainText('Bütün eşler bulundu.');
        } else if (await slide.locator('.etk-bosluk').count()) {
          types.add('bosluk');
          for (const blank of await slide.locator('.etk-bosluk-yer').all()) {
            await blank.click(); const answer = await blank.getAttribute('data-cevap');
            const word = slide.locator('.etk-kelime:not([hidden])').filter({ hasText: new RegExp('^' + answer + '$') }).first();
            await word.click();
          }
          await slide.locator('.etk-kontrol').click(); await expect(slide.locator('.etk-geri')).toContainText('Bütün boşluklar doğru.');
        } else if (await slide.locator('.etk-ogretici').count()) {
          types.add('ogretici');
          const n = await slide.locator('.etk-ipucu').count();
          for (let step = 0; step <= n; step++) await action('reveal').click();
          await expect(slide.locator('.etk-cevap')).toBeVisible();
          await expect(action('reveal')).toBeDisabled();
        }
        if (i + 1 < ids.length) await action('next').click();
      }
      // Mode switches keep answers and the selected question set.
      await page.locator('.ds [data-control="mode"]').selectOption('lesson');
      await page.locator('.ds [data-control="mode"]').selectOption('questions');
      assert.deepEqual((await session()).ids, ids);
      if (answeredId && ids.includes(answeredId)) await expect(page.locator('.ds-slide[data-slide="' + answeredId + '"] .etk-puan')).toContainText('1 / 1 doğru');
      await action('restart').click();
      assert.deepEqual((await session()).ids, ids);
      assert.equal(await page.locator('.ds-slide .bitti, .ds-slide .esli, .ds-slide details[open]').count(), 0);
      for (const score of await page.locator('.ds-slide .etk-puan b').all()) await expect(score).toHaveText('0');
      if (round < 3) await action('new').click();
    }
    assert.equal(seen.size, 14);
    assert.deepEqual([...types].sort(), ['example', 'coktan', 'dy', 'eslestir', 'bosluk', 'ogretici'].sort());
    await action('new').click(); await expect(page.locator('.ds-notice')).toContainText('havuzu tamamlandı');
    ok('Beş etkinlik türü, örnek çözümleri, tek puanlama, 14 soruluk havuzda tekrarsız dört tur');

    await action('next').click();
    const saved = await session();
    await page.reload(); await expect(page.locator('#ders-slayt-ac')).toHaveText('Sunuma devam et');
    await page.locator('#ders-slayt-ac').click();
    assert.deepEqual(await session(), saved);
    await page.locator('.ds-stage').focus(); await page.keyboard.press('Home');
    await expect(page.locator('.ds-progress')).toHaveText('1 / 4 slayt');
    await page.keyboard.press('End'); await expect(page.locator('.ds-progress')).toHaveText('4 / 4 slayt');
    ok('Yenilemede set/konum, Home/End gezinmesi');

    for (const width of [768, 360]) {
      await page.setViewportSize({ width, height: 900 });
      await action('restart').tap();
      const stage = await page.locator('.ds-stage').boundingBox(); assert(stage.height > 100);
      assert(await page.locator('.ds-shell').evaluate(el => el.scrollWidth <= el.clientWidth + 1));
      for (let n = 0; n < 20 && (await session()).index === 0; n++) await action('next').tap();
      await expect(page.locator('.ds-progress')).toHaveText('2 / 4 slayt');
      await page.screenshot({ path: path.join(results, name + '-' + width + '.png') });
    }
    ok('768/360 piksel ekran ve dokunma ile gezinme');
    assert.deepEqual(errors, [], 'Tarayıcı JavaScript hataları');
    record.status = 'passed';
  } catch (error) {
    record.status = 'failed'; record.error = error.stack; record.pageErrors = errors;
    await page.screenshot({ path: path.join(results, name + '-failure.png') }).catch(() => {});
    throw error;
  } finally {
    report.push(record); await fs.writeFile(path.join(results, 'report.json'), JSON.stringify(report, null, 2));
    await browser.close();
  }
}

(async () => {
  await fs.mkdir(results, { recursive: true });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = 'http://127.0.0.1:' + server.address().port;
  try { await run(chromium, 'chromium', base); await run(webkit, 'webkit', base); }
  finally { server.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
