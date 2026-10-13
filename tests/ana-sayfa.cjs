// ortak.js'in paylaşılan yardımcıları (icerikKarti, kitleSuzgeci, konuyaEsle, yol) gerçek katalogla, en küçük DOM'da.
// Ana sayfa "Son eklenenler" ve kütüphane aynı kartı çizer (13.10.2026: akis.js/kutuphane.js kopyaları ortak.js'e taşındı).
async function runHomeChecks(source, metadata, catalog) {
  const assert = (ok, message) => { if (!ok) throw new Error(message); };
  const cases = [];
  class Node {
    constructor(tag, attrs = {}, ...children) {
      this.tag = tag; this.attrs = attrs; this.children = children.flat().filter((x) => x != null && x !== false); this.listeners = {};
      this.classList = { add: (c) => { this.attrs.sinif = `${this.attrs.sinif || ''} ${c}`.trim(); }, toggle() {}, remove() {} };
    }
    append(...children) { this.children.push(...children.flat()); }
    replaceChildren(...children) { this.children = children.flat(); }
    addEventListener(event, callback) { this.listeners[event] = callback; }
    querySelector(s) { return all(this).slice(1).find((n) => n.tag === s.split(/[.:]/)[0] && (!s.includes('.ac') || /\bac\b/.test(n.attrs.sinif || '')) && (!s.includes(':not([download])') || n.attrs.download == null)) || null; }
    get textContent() { return this.children.map((c) => c instanceof Node ? c.textContent : String(c)).join(''); }
  }
  const all = (node) => [node, ...node.children.filter((n) => n instanceof Node).flatMap(all)];
  const links = (node) => all(node).filter((n) => n.tag === 'a');
  // ortak.js tepesindeki yardımcılar (fetch/DOM gerektiren kısımlar çalıştırılmaz): tanımlar `kok`a kadar alınır
  const bas = source.indexOf('const tarihBicim'), son = source.indexOf('// Mobil menü');
  assert(bas > 0 && son > bas, 'ortak.js yardımcı kesiti bulunamadı');
  const kesit = source.slice(bas, son).replace(/^const ortakVeri[\s\S]*$/m, '');
  const api = new Function('el', 'simge', 'window', 'fetch', kesit + '\nreturn { icerikKarti, kitleSuzgeci, konuyaEsle, yol, adNormal };')(
    (tag, attrs, ...children) => new Node(tag, attrs, ...children), () => new Node('svg'), { Kesif: { category: () => ({ color: 'mor' }) } }, async () => ({ ok: false }));
  const check = (name, callback) => { callback(); cases.push({ name, status: 'passed' }); };

  check('Every catalog entry renders a card with a title and at least one action link', () => {
    for (const i of catalog) {
      const kart = api.icerikKarti(i, metadata);
      assert(all(kart).some((n) => n.tag === 'h3' && n.textContent.trim()), `Başlıksız kart: ${i.baslik}`);
      assert(links(kart).length >= 1, `Eylemsiz kart: ${i.baslik}`);
      assert(/\bkart\b/.test(kart.attrs.sinif), 'Kart sınıfı yok');
    }
  });
  check('Grade prefix is dropped from titles because the grade badge already shows it', () => {
    const kart = api.icerikKarti({ sinif: 5, ders: 'matematik', tur: 'Konu anlatımı', baslik: '5. Sınıf Matematik 3. Hafta: Açılar', goruntule: 'ozet/5-matematik-3.html' }, metadata);
    assert(all(kart).find((n) => n.tag === 'h3').textContent === 'Matematik 3. Hafta: Açılar', 'Önek kaldırılmadı');
    assert(all(kart).some((n) => n.tag === 'span' && n.textContent === '5. sınıf'), 'Sınıf rozeti yok');
    assert(/\btiklanir\b/.test(kart.attrs.sinif), 'Kartın tamamı tıklanır olmalı');
  });
  check('Textbook cards offer opening from the computer; downloads are not the whole-card action', () => {
    const kitap = api.icerikKarti({ sinif: 5, ders: 'matematik', tur: 'Ders kitabı', baslik: 'Kitap', goruntule: 'goruntule.html?b=kitap-5-mat' }, metadata);
    assert(links(kitap).some((n) => n.attrs.href === '/goruntule.html?b=kitap-5-mat&yerel=1'), 'Bilgisayardan aç bağlantısı yok');
    const dosya = api.icerikKarti({ sinif: 5, ders: 'matematik', tur: 'Yıllık plan', baslik: 'Plan', dosya: 'dosyalar/plan.pdf' }, metadata);
    assert(links(dosya).length === 1 && links(dosya)[0].attrs.download === '' && !/\btiklanir\b/.test(dosya.attrs.sinif), 'İndirme kartı tıklanır olmamalı');
  });
  check('Audience filter: shared types (worksheets) pass in both branches, others only in their own', () => {
    const ogrenci = api.kitleSuzgeci(metadata, 'ogrenci'), ogretmen = api.kitleSuzgeci(metadata, 'ogretmen'), hepsi = api.kitleSuzgeci(metadata, '');
    const kagit = catalog.find((i) => i.tur === 'Çalışma kâğıdı'), plan = catalog.find((i) => i.kitle === 'ogretmen'), ozet = catalog.find((i) => i.tur === 'Konu anlatımı');
    assert(kagit && ogrenci(kagit) && ogretmen(kagit), 'Çalışma kâğıdı iki dalda da görünmeli');
    assert(plan && ogretmen(plan) && !ogrenci(plan), 'Öğretmen içeriği öğrenci dalında görünmemeli');
    assert(ozet && ogrenci(ozet) && !ogretmen(ozet), 'Konu anlatımı öğretmen dalında görünmemeli');
    assert(catalog.every(hepsi), 'Kitle verilmeyince hepsi geçmeli');
    assert(api.kitleSuzgeci(null, 'ogrenci')({ tur: 'Konu anlatımı' }), 'dersler.json gelmeyince varsayılan kitle öğrenci');
  });
  check('Topic matching: exact name first, then containment; Turkish case and punctuation ignored', () => {
    const konular = [{ ad: 'Kesirler' }, { ad: 'Kesirlerle İşlemler' }, { ad: 'Açı Ölçme' }];
    assert(api.konuyaEsle(konular, 'KESİRLER').map((k) => k.ad).join() === 'Kesirler', 'Tam ad öncelikli olmalı');
    assert(api.konuyaEsle(konular, 'kesirlerle işlemler').length === 1, 'Tam eşleşme tek olmalı');
    assert(api.konuyaEsle(konular, 'Açı').map((k) => k.ad).join() === 'Açı Ölçme', 'İçerme eşleşmesi yok');
    assert(api.konuyaEsle(konular, '').length === 0 && api.konuyaEsle(konular, 'Kümeler').length === 0, 'Boş ya da yabancı konu eşleşmemeli');
  });
  check('Site paths are rooted once and external links untouched', () => {
    assert(api.yol('ozet/5-matematik-1.html') === '/ozet/5-matematik-1.html' && api.yol('/a.html') === '/a.html' && api.yol('https://x.y/z') === 'https://x.y/z', 'yol() yanlış');
  });
  return { status: 'passed', environment: 'Node, minimal DOM; no browser rendering', cases, resources: catalog.length, subjects: Object.keys(metadata.dersler).length };
}
if (typeof module !== 'undefined') module.exports = { runHomeChecks };
if (typeof require !== 'undefined' && require.main === module) {
  const fs = require('node:fs'), path = require('node:path'), root = path.resolve(__dirname, '../public');
  runHomeChecks(fs.readFileSync(path.join(root, 'ortak.js'), 'utf8'), JSON.parse(fs.readFileSync(path.join(root, 'veri/dersler.json'), 'utf8')), JSON.parse(fs.readFileSync(path.join(root, 'veri/icerikler.json'), 'utf8')).icerikler).then((r) => console.log(JSON.stringify(r, null, 2))).catch((e) => { console.error(e); process.exitCode = 1; });
}
