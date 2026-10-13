// Real Chromium/WebKit layout, keyboard and touch checks, isolated CI server.
const {chromium,webkit,expect}=require('@playwright/test');
const assert=require('node:assert/strict'),fs=require('node:fs/promises'),path=require('node:path'),http=require('node:http');
const root=path.resolve(__dirname,'../public'),output=path.resolve('site-test-results');
const report={checks:[],errors:[]};
const mime={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.ico':'image/x-icon'};
const server=http.createServer(async(req,res)=>{
  const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  const file=path.resolve(root,'.'+(pathname==='/'?'/index.html':pathname));
  if(!file.startsWith(root+path.sep)){res.writeHead(403).end();return;}
  try{res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream'}).end(await fs.readFile(file));}
  catch{res.writeHead(404).end();}
});
const routes=['/','/icerikler.html','/ogrenci.html','/ogrenci.html?sinif=5','/planlar.html','/belgeler.html','/kelime.html','/arapca.html','/kpss.html','/sinav.html','/ara.html?q=matematik','/ozet/5-matematik-hafta-1.html'];
async function ready(page,route){
  // Ana sayfa (11.10.2026): iki rol kartı ve "Son eklenenler"; sınıf ve ders kartları öğrenci ağacında (agac.js).
  if(route==='/'){await expect(page.locator('.rol-kart')).toHaveCount(2);await page.locator('#kartlar .kart').first().waitFor();}
  else if(route.includes('icerikler'))await page.locator('#kartlar .kart').first().waitFor();
  else if(route.includes('sinif='))await page.locator('.agac-ders').first().waitFor();
  else if(route.includes('ogrenci.html'))await page.locator('.agac-sinif').first().waitFor();
  else await page.locator('main').waitFor();
  await page.evaluate(()=>document.fonts.ready);
}
async function layout(page,route,name,width){
  await page.goto(base+route);await ready(page,route);
  const metrics=await page.evaluate(()=>({width:innerWidth,document:document.documentElement.scrollWidth,
    missingStyle:!Array.from(document.styleSheets).some(s=>s.href?.includes('/renkler.css')),
    overflow:Array.from(document.querySelectorAll('main *')).filter(n=>{const b=n.getBoundingClientRect();return b.width&&(b.left< -1||b.right>innerWidth+1)&&getComputedStyle(n).position!=='absolute';}).slice(0,6).map(n=>({tag:n.tagName,class:n.className}))}));
  assert(!metrics.missingStyle,'Missing shared palette: '+route);
  assert(metrics.document<=metrics.width+1,'Horizontal overflow: '+route+' '+width+' '+JSON.stringify(metrics));
  report.checks.push({browser:name,route,width,check:'layout',status:'passed'});
}
let base;
(async()=>{
  await fs.mkdir(output,{recursive:true});
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));base='http://127.0.0.1:'+server.address().port;
  const metadata=JSON.parse(await fs.readFile(path.join(root,'veri/dersler.json'),'utf8'));
  try{
    for(const[name,engine]of[['chromium',chromium],['webkit',webkit]]){
      const browser=await engine.launch();
      const context=await browser.newContext({viewport:{width:1366,height:900},hasTouch:true,colorScheme:'light',reducedMotion:'reduce'});
      await context.route('**/*',r=>r.request().url().startsWith(base)?r.continue():r.abort());
      const page=await context.newPage();page.setDefaultTimeout(12000);
      page.on('pageerror',e=>report.errors.push({browser:name,url:page.url(),message:e.message}));
      try{
        for(const width of [1366,1180,768,390,320]){
          await page.setViewportSize({width,height:900});
          for(const route of routes)await layout(page,route,name,width);
          await page.goto(base+'/ogrenci.html');await ready(page,'/ogrenci.html');
          await expect(page.locator('.agac-sinif')).toHaveCount(Object.keys(metadata.siniflar).length);
          await page.goto(base+'/');await ready(page,'/');
          await page.screenshot({path:path.join(output,`${name}-home-${width}.png`)});
          if([1366,390].includes(width)){
            for(const section of ['.rol-giris','#icerikler','#araclar'])await page.locator(section).screenshot({path:path.join(output,`${name}-${section.replace(/^[.#]/,'')}-${width}.png`)});
          }
        }
        await page.setViewportSize({width:390,height:900});
        await page.goto(base+'/');await ready(page,'/');
        await page.locator('.menu-dugme').tap();
        await expect(page.locator('.menu-dugme')).toHaveAttribute('aria-expanded','true');
        await page.locator('#ana-menu a[href="/ogrenci.html"]').tap();
        await page.waitForURL('**/ogrenci.html');await ready(page,'/ogrenci.html');
        await expect(page.locator('.menu-dugme')).toHaveAttribute('aria-expanded','false');
        const firstGrade=page.locator('.agac-sinif').first();
        await firstGrade.focus();
        // A touch followed by focus() retains pointer modality. Exercise real keyboard navigation.
        await page.keyboard.press('Tab');
        await expect(page.locator('.agac-sinif').nth(1)).toBeFocused();
        await page.keyboard.press('Shift+Tab');
        await expect(firstGrade).toBeFocused();
        assert(await firstGrade.evaluate(n=>n.matches(':focus-visible')&&getComputedStyle(n).outlineStyle!=='none'),'Keyboard focus missing');
        await page.keyboard.press('Enter');
        await page.waitForURL('**/ogrenci.html?sinif=5');await ready(page,'/ogrenci.html?sinif=5');
        await expect(page.locator('.agac-ders').first()).toBeVisible();
        report.checks.push({browser:name,check:'touch menu, keyboard grade navigation',status:'passed'});
        await page.setViewportSize({width:1366,height:900});
        for(const mode of ['system-dark','explicit-dark','explicit-light']){
          await page.emulateMedia({colorScheme:mode==='explicit-dark'?'light':'dark'});
          await page.goto(base+'/');await ready(page,'/');
          if(mode.startsWith('explicit'))await page.evaluate(theme=>document.documentElement.dataset.theme=theme,mode.split('-')[1]);
          // Renk sistemi: menü, rol kartları ve araç bağlantıları data-renk taşır (mavi, yeşil, pembe, mor, turkuaz, lacivert, sarı)
          const colors=await page.locator('.menu > a[data-renk], .rol-kart[data-renk], .kesif-arac-links a[data-renk]').evaluateAll(cards=>cards.map(n=>({ink:getComputedStyle(n).getPropertyValue('--kart-ana').trim().toUpperCase(),bg:getComputedStyle(n).backgroundColor})));
          assert(new Set(colors.map(c=>c.ink)).size>=7,'Palette colors collapsed: '+JSON.stringify(colors));
          assert(colors.some(c=>c.ink===(mode==='explicit-light'?'#6135BD':'#D2B8FF')),'Theme mismatch');
          await page.screenshot({path:path.join(output,`${name}-${mode}.png`)});
          await page.locator('.rol-giris').screenshot({path:path.join(output,`${name}-${mode}-roles.png`)});
          report.checks.push({browser:name,check:mode,status:'passed'});
        }
        await page.emulateMedia({colorScheme:'light'});
        for(const route of ['/planlar.html','/belgeler.html','/kelime.html','/kpss.html','/ogrenci.html?sinif=5']){
          await page.goto(base+route);await ready(page,route);
          await page.screenshot({path:path.join(output,`${name}-${route.split('?')[0].slice(1,-5)}.png`)});
        }
      }catch(error){report.errors.push({browser:name,error:error.message});await page.screenshot({path:path.join(output,name+'-failure.png')}).catch(()=>{});throw error;}
      finally{await fs.writeFile(path.join(output,'report.json'),JSON.stringify(report,null,2));await browser.close();}
    }
    assert.deepEqual(report.errors,[]);console.log(JSON.stringify({status:'passed',checks:report.checks.length}));
  }finally{server.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
