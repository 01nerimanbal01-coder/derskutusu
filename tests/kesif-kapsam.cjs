// Gerçek kaynak HTML ile sunumun metin, şekil, tablo ve soru kapsamını karşılaştırır.
// Yalnız izole test sunucusu; canlı siteye veri göndermez.
const { chromium, webkit, expect } = require('@playwright/test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const http = require('node:http');
const root = path.resolve(__dirname, '../public');
const output = path.resolve('kesif-test-results');
const report = { lessons: [], interfaces: [], errors: [] };
const mime = { '.html':'text/html', '.js':'text/javascript', '.css':'text/css', '.json':'application/json', '.svg':'image/svg+xml', '.png':'image/png', '.ico':'image/x-icon' };
const server = http.createServer(async (req, res) => {
  const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  const file = path.resolve(root, '.' + (pathname === '/' ? '/index.html' : pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  try { const data = await fs.readFile(file); res.writeHead(200, { 'Content-Type':mime[path.extname(file)] || 'application/octet-stream' }).end(data); }
  catch { res.writeHead(404).end(); }
});
async function coverage(page, base, browserName, filenames) {
  for (const filename of filenames) {
    try {
    await page.goto(base + '/ozet/' + filename);
    await page.locator('#ders-slayt-ac').click();
    const result = await page.evaluate(() => {
      const definitions = [['intro','.ozet-ust'], ['topic','.ozet-bolum.konu'], ['example','.ornekler > .ornek'], ['activity','.etk-liste > .etk'], ['ending','.ozet-son'], ['resources','.ozet-ilgili']];
      const source = document.querySelector('article.ozet');
      const frames = [...document.querySelectorAll('.ds-slide')];
      const content = [];
      const normalize = text => text.replace(/\s+/g, ' ').trim();
      const snapshot = (node, kind) => {
        const text = normalize(node.textContent);
        return {
          // Eşleştirme/kelime düğmeleri her açılışta karıştırılır; sözcük kaybı yine yakalanır.
          text:kind === 'activity' ? text.split(' ').sort().join(' ') : text,
          svg:node.querySelectorAll('svg').length,
          paths:[...node.querySelectorAll('svg path')].map(p => p.getAttribute('d')),
          images:[...node.querySelectorAll('img')].map(p => p.getAttribute('src')),
          tables:[...node.querySelectorAll('table')].map(p => normalize(p.textContent)),
          math:[...node.querySelectorAll('[role="math"]')].map(p => p.getAttribute('aria-label')),
          cells:[...node.querySelectorAll('td,th')].map(p => normalize(p.textContent)),
        };
      };
      let index = 0;
      for (const [kind, selector] of definitions) {
        for (const node of source.querySelectorAll(selector)) {
          const frame = frames[index++];
          const copy = frame?.querySelector(selector);
          content.push({ kind, equal:Boolean(copy) && JSON.stringify(snapshot(node, kind)) === JSON.stringify(snapshot(copy, kind)),
            original:copy ? undefined : normalize(node.textContent).slice(0, 100),
            source:snapshot(node,kind), actual:copy ? snapshot(copy,kind) : null });
        }
      }
      const ids = [...document.querySelectorAll('[id]')].map(n => n.id);
      return { frames:frames.length, expected:index, content, duplicateIds:ids.filter((id,i) => ids.indexOf(id) !== i),
        counts:Object.fromEntries(definitions.map(([kind,selector]) => [kind,source.querySelectorAll(selector).length])) };
    });
    assert.equal(result.frames, result.expected, filename + ': slayt sayısı');
    assert.deepEqual(result.content.filter(c => !c.equal), [], filename + ': kaynak ile sunum farklı');
    assert.deepEqual(result.duplicateIds, [], filename + ': yinelenen HTML/SVG kimliği');
    // Her bölüm menüden açılır; bütün adımlar ileri düğmesiyle, atlanmadan erişilir.
    const navigation = await page.evaluate(() => {
      const select = document.querySelector('[data-control="slide"]');
      const next = document.querySelector('[data-action="next"]');
      const steps = [];
      for (let i = 0; i < select.options.length; i++) {
        select.value = String(i); select.dispatchEvent(new Event('change', { bubbles:true }));
        const frame = document.querySelector('.ds-slide:not([hidden])');
        let reveals = 0;
        while (!document.querySelector('[data-action="reveal"]').disabled && reveals < 100) {
          next.click(); reveals++;
          if (document.querySelector('.ds-slide:not([hidden])') !== frame) return { error:'Adım açılmadan bölüm atlandı', i };
        }
        const remains = [...frame.querySelectorAll('.bolum-metin > *, .bolum-yan > *, details')].filter(n => n.hidden || (n.matches('details') && !n.open));
        if (remains.length || reveals >= 100) return { error:'Açılamayan içerik', i };
        if (i < select.options.length - 1) { next.click(); if (Number(select.value) !== i + 1) return { error:'Sonraki bölüm açılamadı', i }; }
        steps.push(reveals);
      }
      return { visited:steps.length, reveals:steps.reduce((a,b) => a+b,0), lastDisabled:next.disabled };
    });
    assert(!navigation.error, filename + ': ' + JSON.stringify(navigation));
    assert.equal(navigation.visited, result.expected);
    assert(navigation.lastDisabled);
    report.lessons.push({ browser:browserName, file:filename, slides:result.frames, ...result.counts, reveals:navigation.reveals,
      svg:result.content.reduce((n,c)=>n+c.source.svg,0), tables:result.content.reduce((n,c)=>n+c.source.tables.length,0), status:'passed' });
    if (filename === '5-matematik-hafta-1.html') {
      await page.locator('[data-control="slide"]').selectOption('1');
      await page.locator('[data-action="restart"]').click();
      await page.screenshot({ path:path.join(output,browserName+'-slayt-giris.png') });
      await page.locator('[data-control="slide"]').selectOption('1');
      await page.locator('[data-action="next"]').click();
      await page.screenshot({ path:path.join(output,browserName+'-slayt-konu.png') });
    }
    if (report.lessons.length % 20 === 0) console.log('Kapsam doğrulandı: ' + report.lessons.length);
    } catch (error) {
      report.lessons.push({browser:browserName,file:filename,status:'failed',error:error.message});
      console.error(browserName + ' / ' + filename + ': ' + error.message.slice(0,700));
      if (report.lessons.filter(r=>r.status==='failed').length<=3) await page.screenshot({path:path.join(output,browserName+'-'+filename+'.png')}).catch(()=>{});
    }
  }
}
async function interfaces(page, base, name) {
  const data = JSON.parse(await fs.readFile(path.join(root,'veri/icerikler.json'),'utf8')).icerikler;
  await page.goto(base + '/');
  await expect(page.locator('.kesif-kategori')).toHaveCount(8);
  await expect(page.locator('[data-kesif-sayi="kaynak"]')).toHaveText(String(data.length));
  const categories = await page.locator('.kesif-kategori').evaluateAll(nodes => nodes.map(n => ({ href:n.getAttribute('href'), count:n.querySelector('.kesif-adet').textContent })));
  for (const item of categories) {
    const type = new URL(item.href,'http://localhost').searchParams.get('tur');
    assert.equal(parseInt(item.count),data.filter(i=>i.tur===type).length);
  }
  await page.screenshot({ path:path.join(output,name+'-ana-sayfa.png'), fullPage:true });
  await page.screenshot({ path:path.join(output,name+'-home-viewport.png') });
  await page.locator('#hizli-bul [name="sinif"]').selectOption('5');
  await page.locator('#hizli-bul [name="ders"]').selectOption('matematik');
  await page.locator('#hizli-bul [name="tur"]').selectOption('Konu anlatımı');
  await page.locator('#hizli-bul button').click();
  await expect(page.locator('#s-sinif')).toHaveValue('5');
  await expect(page.locator('#s-ders')).toHaveValue('matematik');
  await expect(page.locator('#s-tur')).toHaveValue('Konu anlatımı');
  await expect(page.locator('#sonuc-sayi')).toHaveText(data.filter(i=>i.sinif===5&&i.ders==='matematik'&&i.tur==='Konu anlatımı').length+' içerik');
  // Kaynak türlerinin her birini gerçek arayüz üzerinden seç ve sayıları doğrula.
  await page.locator('#temizle').click();
  for (const item of categories) {
    const type = new URL(item.href,'http://localhost').searchParams.get('tur');
    await page.locator('#kategori-secimleri button').filter({ has:page.locator('span') }).evaluateAll((buttons,type) => buttons.find(b=>b.dataset.tur===type).click(),type);
    await expect(page.locator('#sonuc-sayi')).toHaveText(data.filter(i=>i.tur===type).length+' içerik');
    await expect(page.locator('#s-tur')).toHaveValue(type);
  }
  await page.locator('#temizle').click();
  await expect(page.locator('#kartlar .kart')).toHaveCount(12);
  await page.locator('#daha-goster').click();
  await expect(page.locator('#kartlar .kart')).toHaveCount(24);
  await page.locator('#s-sirala').selectOption('baslik');
  const titles = await page.locator('#kartlar h3').allTextContents();
  assert.deepEqual(titles,[...titles].sort((a,b)=>a.localeCompare(b,'tr')));
  await page.locator('#s-sinif').selectOption('5');
  await page.locator('#s-ders').selectOption('matematik');
  await page.locator('#s-ara').fill('zxqvbulunamayankonu');
  await expect(page.locator('#icerik-yakinda')).toBeVisible();
  await page.locator('#aramayi-temizle').click();
  await expect(page.locator('#s-sinif')).toHaveValue('5');
  await expect(page.locator('#s-ders')).toHaveValue('matematik');
  await expect(page.locator('#icerik-yakinda')).toBeHidden();
  await page.reload();
  await expect(page.locator('#s-ders')).toHaveValue('matematik');
  await page.locator('#temizle').click();
  await page.evaluate(()=>window.scrollTo({top:0,behavior:'instant'}));
  await page.screenshot({ path:path.join(output,name+'-kutuphane.png'), fullPage:true });
  await page.screenshot({ path:path.join(output,name+'-library-viewport.png') });
  for (let grade=5;grade<=12;grade++) {
    await page.goto(base + '/sinif.html?no='+grade);
    await expect(page.locator('#baslik')).toContainText(grade+'. sınıf');
    assert(await page.locator('.ders-kart').count()>0);
    for (const href of await page.locator('.ders-kart').evaluateAll(nodes=>nodes.map(n=>n.getAttribute('href')))) assert.equal(new URL(href,base).searchParams.get('sinif'),String(grade));
  }
  await page.goto(base + '/sinif.html?no=5');
  await page.locator('.ders-kart').first().waitFor();
  await page.screenshot({ path:path.join(output,name+'-sinif.png'), fullPage:true });
  for (const width of [768,360]) {
    await page.setViewportSize({width,height:900});
    for (const route of ['/', '/icerikler.html', '/sinif.html?no=5']) {
      await page.goto(base+route); await page.locator(route==='/'?'.kesif-kategori':route.includes('icerikler')?'#kartlar .kart':'.ders-kart').first().waitFor();
      const overflow = await page.evaluate(() => [...document.body.querySelectorAll('*')].filter(n => {
        const box = n.getBoundingClientRect(); return box.width && (box.right > innerWidth + 1 || box.left < -1) && getComputedStyle(n).position !== 'absolute';
      }).slice(0,12).map(n=>({tag:n.tagName,class:n.className,width:n.getBoundingClientRect().width,right:n.getBoundingClientRect().right})));
      assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1), 'Yatay taşma: '+route+' '+width+' '+JSON.stringify(overflow));
      await page.screenshot({path:path.join(output,name+'-'+(route==='/'?'home':route.includes('icerikler')?'library':'class')+'-'+width+'.png'),fullPage:true});
    }
  }
  await page.goto(base+'/');
  await page.locator('.menu-dugme').click();
  await expect(page.locator('.menu-dugme')).toHaveAttribute('aria-expanded','true');
  await page.locator('#ana-menu a').filter({hasText:'Kütüphane'}).click();
  await expect(page.locator('#kartlar .kart')).toHaveCount(12);
  await page.emulateMedia({colorScheme:'dark',reducedMotion:'reduce'});
  await page.screenshot({path:path.join(output,name+'-koyu-tema.png'),fullPage:true});
  await page.emulateMedia({colorScheme:'light'});
  await page.setViewportSize({width:1366,height:900});
  report.interfaces.push({browser:name,status:'passed', categories:8,classes:8,widths:[1366,768,360],checks:['gerçek kategori sayıları','hızlı bul','bağımlı filtreler','kısa ve uzun liste','sıralama','sonuçsuz arama','aramayı temizle','yenileme','mobil menü','karanlık tema','yatay taşma']});
}
(async()=>{
  await fs.mkdir(output,{recursive:true});
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base='http://127.0.0.1:'+server.address().port;
  const lessons=(await fs.readdir(path.join(root,'ozet'))).filter(f=>f.endsWith('.html')).sort();
  assert(lessons.length>=116,'Ders sayfaları eksik');
  try {
    for(const [name,engine] of [['chromium',chromium],['webkit',webkit]]) {
      const browser=await engine.launch();
      const context=await browser.newContext({viewport:{width:1366,height:900},hasTouch:true,colorScheme:'light'});
      await context.route('**/*',route=>route.request().url().startsWith(base)?route.continue():route.abort());
      const page=await context.newPage(); page.setDefaultTimeout(10000);
      page.on('pageerror',e=>report.errors.push({browser:name,url:page.url(),message:e.message}));
      try { await coverage(page,base,name,lessons); await interfaces(page,base,name); }
      catch(error) { await page.screenshot({path:path.join(output,name+'-failure.png')}).catch(()=>{}); throw error; }
      finally { await fs.writeFile(path.join(output,'report.json'),JSON.stringify(report,null,2)); await browser.close(); }
    }
    assert.deepEqual(report.errors,[]);
    assert.equal(report.lessons.filter(r=>r.status==='failed').length,0,'Kaynak-sunum karşılaştırmasında başarısız dersler var; report.json dosyasına bakın');
    console.log(JSON.stringify({status:'passed',lessons:lessons.length,browsers:2,slideChecks:report.lessons.reduce((n,r)=>n+r.slides,0)}));
  } finally { server.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
