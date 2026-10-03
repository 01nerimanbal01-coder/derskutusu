
// Dependency-free regression tests for the actual source files.
// Uses a small DOM fixture, not a browser; no layout/accessibility-tree assertions.
async function runCatalogChecks(commonSource, librarySource) {
  const assert = (ok, message) => { if (!ok) throw new Error(message); };
  const cases = [];
  class Params {
    constructor(value = '') {
      this.values = new Map(Array.isArray(value) ? value : String(value).replace(/^\?/, '').split('&').filter(Boolean).map(s => s.split('=').map(decodeURIComponent)));
    }
    get(key) { return this.values.get(key) ?? null; }
    set(key, value) { this.values.set(key, value); }
    toString() { return [...this.values].map(([k, v]) => encodeURIComponent(k) + '=' + encodeURIComponent(v)).join('&'); }
  }
  class Node {
    constructor(tag = 'div', attrs = {}, ...children) {
      this.tag = tag; this.attrs = {}; this.dataset = {}; this.children = [];
      this.hidden = false; this.disabled = false; this._value = ''; this.listeners = {};
      Object.entries(attrs).forEach(([key, value]) => {
        if (key === 'onclick') this.listeners.click = value;
        else if (key === 'value') this.value = value;
        else this.setAttribute(key, value);
      });
      this.append(...children);
    }
    append(...children) { this.children.push(...children.filter(c => c != null)); }
    replaceChildren(...children) { this.children = []; this.append(...children); if (this.tag === 'select') this.value = ''; }
    setAttribute(key, value) { this.attrs[key] = String(value); if (key.startsWith('data-')) this.dataset[key.slice(5)] = String(value); }
    addEventListener(type, callback) { this.listeners[type] = callback; }
    focus() {}
    scrollIntoView() {}
    get value() { return this._value; }
    set value(value) { this._value = String(value); }
    get textContent() { return this.children.map(c => typeof c === 'string' ? c : c.textContent).join(''); }
    set textContent(value) { this.children = [String(value)]; }
    get options() { return this.children.filter(c => c.tag === 'option'); }
    get selectedOptions() { return this.options.filter(c => c.value === this.value); }
    querySelectorAll(selector) {
      return this.children.flatMap(c => typeof c === 'string' ? [] : [...(c.tag === selector ? [c] : []), ...c.querySelectorAll(selector)]);
    }
    querySelector(selector) { return this.querySelectorAll(selector)[0] ?? null; }
  }
  const metadata = { siniflar: {5: ['matematik']}, secmeli: {}, kademeler: [{ad: 'Ortaokul', siniflar: [5]}],
    dersler: {matematik: 'Matematik'}, turler: [{ad: 'Konu anlatımı', kitle: 'ogrenci'}] };
  const record = {sinif:5, ders:'matematik', tur:'Konu anlatımı', baslik:'Kesirler', aciklama:'Örnek ders', url:'/ozet/ornek.html', tarih:'2026-10-03', hafta:1};
  const start = commonSource.indexOf('async function veri(');
  const end = commonSource.indexOf('// Mobil menü', start);
  assert(start >= 0 && end > start, 'Shared loader boundaries missing');
  const loader = commonSource.slice(start, end);
  async function load(mode) {
    return new Function('fetch', 'kok', loader + '\nreturn ortakVeri;')(async url => {
      const catalog = url.endsWith('icerikler.json');
      if (catalog && mode === 'network') throw new Error('offline');
      return {
        ok: !(catalog && mode === 'http') && !(url.endsWith('dersler.json') && mode === 'metadata-http'),
        json: async () => {
          if (url.endsWith('ayarlar.json')) { if (mode === 'settings-json') throw new Error('invalid settings'); return {}; }
          if (url.endsWith('dersler.json')) return metadata;
          if (mode === 'json') throw new Error('invalid JSON');
          if (mode === 'shape') return {icerikler: {}};
          if (mode === 'missing') return {};
          return {icerikler: mode === 'empty' ? [] : [record]};
        }
      };
    }, '/');
  }
  async function render(page, data) {
    const ids = page === 'library'
      ? ['s-sinif','s-ders','s-kitle','s-hafta','s-tur','s-ara','s-sirala','kartlar','sonuc-sayi','temizle','icerik-yakinda','sonucsuz-baslik','sonucsuz-aciklama','aramayi-temizle','sonucsuz-temizle','daha-goster','daha-alani','gosterilen-sayi','secili-suzgecler']
      : ['ders-listesi','baslik','yol-sinif','aciklama','sinif-gecis','tum-icerik','secmeli-listesi','secmeli-bolum','ogretmen-hizli'];
    const nodes = Object.fromEntries(ids.map(id => [id, new Node(id.startsWith('s-') && id !== 's-ara' ? 'select' : 'div')]));
    if (nodes['s-sirala']) nodes['s-sirala'].value = 'yeni';
    const state = {reloads:0, replaced:[], url:null};
    const location = {search:page === 'class' ? '?no=5' : '', pathname:page === 'class' ? '/sinif.html' : '/icerikler.html',
      reload:() => state.reloads++, replace:url => state.replaced.push(url)};
    await new Function('$','el','simge','location','document','window','history','URLSearchParams','ortakVeri',
      librarySource + '\nreturn ortakVeri.then(() => undefined);')(
        selector => nodes[selector.replace(/^#/, '')] ?? null,
        (tag, attrs, ...children) => new Node(tag, attrs, ...children),
        () => new Node('svg'), location, {title:''}, {}, {replaceState:(_a,_b,url) => {state.url = url;}},
        Params, Promise.resolve(data));
    return {nodes, state, target:nodes[page === 'library' ? 'kartlar' : 'ders-listesi']};
  }
  for (const mode of ['http', 'network', 'json', 'shape', 'missing', 'metadata-http']) {
    const data = await load(mode);
    for (const page of ['library', 'class']) {
      const {nodes, state, target} = await render(page, data);
      const alert = target.children.find(n => n?.attrs?.role === 'alert');
      assert(alert && alert.textContent.includes('Kaynak listesi yüklenemedi'), mode + '/' + page + ': missing load error');
      assert(target.hidden === false, mode + '/' + page + ': error hidden');
      assert(!target.textContent.includes('yakında'), mode + '/' + page + ': misleading availability text');
      const retry = alert.querySelector('button');
      assert(retry?.attrs.type === 'button' && retry.textContent === 'Yeniden dene', 'Retry must be a native button');
      retry.listeners.click();
      assert(state.reloads === 1, 'Retry must reload');
      if (page === 'library') {
        assert(nodes['sonuc-sayi'].textContent === '', 'Failed load must not show zero results');
        assert(nodes['icerik-yakinda'].hidden && nodes['daha-alani'].hidden, 'Empty/pagination UI exposed on failure');
        for (const id of ['s-sinif','s-ders','s-kitle','s-hafta','s-tur','s-ara','s-sirala']) assert(nodes[id].disabled, id + ' usable with unavailable data');
      }
      cases.push({name:mode + '/' + page, status:'passed'});
    }
  }
  for (const mode of ['populated', 'empty', 'settings-json']) {
    const data = await load(mode);
    assert(data.iceriklerYuklendi === true, mode + ': valid catalog marked unavailable');
    for (const page of ['library', 'class']) {
      const {nodes, target} = await render(page, data);
      assert(!target.children.some(n => n?.attrs?.role === 'alert'), mode + '/' + page + ': unexpected load error');
      if (page === 'library') {
        assert(nodes['sonuc-sayi'].textContent === (mode === 'empty' ? '0 içerik' : '1 içerik'), mode + ': wrong count');
        assert(nodes['icerik-yakinda'].hidden === (mode !== 'empty'), mode + ': wrong empty state');
        assert(!nodes['s-sinif'].disabled, 'Loaded filter disabled');
        if (mode !== 'empty') assert(target.textContent.includes('Kesirler'), 'Real content lost');
      } else {
        assert(target.textContent.includes('Matematik'), 'Class subject lost');
        assert(target.textContent.includes(mode === 'empty' ? 'Öğrenci içerikleri yakında' : '1 öğrenci içeriği'), 'Wrong class count');
      }
      cases.push({name:mode + '/' + page, status:'passed'});
    }
  }
  return {status:'passed', environment:'JavaScript V8 with minimal DOM fixture; not a browser', cases};
}
if (typeof module !== 'undefined') module.exports = {runCatalogChecks};

if (typeof require !== 'undefined' && require.main === module) {
  const fs = require('node:fs');
  const path = require('node:path');
  const root = path.resolve(__dirname, '..');
  runCatalogChecks(
    fs.readFileSync(path.join(root, 'public/ortak.js'), 'utf8'),
    fs.readFileSync(path.join(root, 'public/kutuphane.js'), 'utf8')
  ).then(result => console.log(JSON.stringify(result, null, 2))).catch(error => {
    console.error(error.stack);
    process.exitCode = 1;
  });
}
