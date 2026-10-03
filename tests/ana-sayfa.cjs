// Actual source and catalog, minimal DOM. Does not claim browser/layout coverage.
async function runHomeChecks(source, metadata, catalog) {
  const assert = (ok, message) => { if (!ok) throw new Error(message); };
  const cases = [];
  class Params {
    constructor(values) { this.values = values; }
    toString() { return this.values.map(([key, value]) => encodeURIComponent(key) + '=' + encodeURIComponent(value)).join('&'); }
  }
  class Node {
    constructor(tag, attrs = {}, ...children) {
      this.tag = tag; this.attrs = attrs; this.children = children.flat().filter(x => x != null); this.listeners = {}; this.value = attrs.value || '';
    }
    append(...children) { this.children.push(...children.flat()); }
    replaceChildren(...children) { this.children = children.flat(); if (this.tag === 'select') this.value = ''; }
    addEventListener(event, callback) { this.listeners[event] = callback; }
    get textContent() { return this.children.map(c => c instanceof Node ? c.textContent : String(c)).join(''); }
    set textContent(value) { this.children = [String(value)]; }
  }
  const all = node => [node, ...node.children.filter(n => n instanceof Node).flatMap(all)];
  const links = node => all(node).filter(n => n.tag === 'a');
  const query = href => Object.fromEntries(href.split('?')[1].split('&').map(p => p.split('=').map(decodeURIComponent)));
  async function render(data) {
    const ids = Object.fromEntries(['kesif-kategoriler', 'kesif-dersler', 'hizli-bul', 'kaynak', 'konu', 'sinif'].map(id => [id, new Node('div')]));
    ids['hizli-bul'].elements = Object.fromEntries(['sinif','ders','tur'].map(k => [k, new Node('select', {}, new Node('option', {value:''}))]));
    const document = {getElementById:id => ids[id], querySelector:s => ids[s.match(/"([^"]+)"/)?.[1]] || null};
    const window = {}, location = {};
    await new Function('document','window','location','URLSearchParams','el','simge','ortakVeri',source + '\nreturn ortakVeri.then(() => undefined);')(
      document,window,location,Params,(tag,attrs,...children)=>new Node(tag,attrs,...children),()=>new Node('svg'),Promise.resolve(data));
    return {ids,window,location};
  }
  const data = {dersler:metadata,icerikler:catalog,iceriklerYuklendi:true};
  const f = await render(data), grid = f.ids['kesif-kategoriler'], subjects = f.ids['kesif-dersler'];
  const check = (name, callback) => { callback(); cases.push({name,status:'passed'}); };
  check('Every resource category appears once in the three purpose groups', () => {
    assert(grid.children.length === 3, 'Expected three purpose groups');
    const types = links(grid).map(n => query(n.attrs.href).tur);
    assert(types.length === f.window.Kesif.categories.length && new Set(types).size === types.length, 'Missing or duplicated categories');
    assert(f.window.Kesif.categories.every(c=>types.includes(c.type)), 'A source category was omitted');
  });
  check('Every resource count matches the current catalog', () => {
    for (const link of links(grid)) {
      const type = query(link.attrs.href).tur;
      const count = all(link).find(n=>n.attrs.sinif==='kesif-adet').textContent;
      assert(count === catalog.filter(i=>i.tur===type).length+' kaynak',type);
    }
    assert(f.ids.kaynak.textContent===String(catalog.length),'Total count');
    assert(f.ids.konu.textContent===String(catalog.filter(i=>i.tur==='Konu anlatımı').length),'Lesson count');
    assert(f.ids.sinif.textContent===String(Object.keys(metadata.siniflar).length),'Grade count');
  });
  check('Every registered subject appears once with a usable library link', () => {
    const keys = links(subjects).map(n=>query(n.attrs.href).ders);
    assert(new Set(keys).size === keys.length, 'Repeated subject');
    assert(keys.length === Object.keys(metadata.dersler).length, 'Omitted subject');
    assert(keys.every(key=>metadata.dersler[key]), 'Unknown subject');
  });
  check('Subject and group counts match the catalog without double counting', () => {
    let total = 0;
    for (const group of subjects.children) {
      const keys = links(group).map(n=>query(n.attrs.href).ders);
      const count = catalog.filter(i=>keys.includes(i.ders)).length;
      assert(group.children[0].textContent.includes(`${keys.length} ders · ${count} kaynak`),'Wrong group count');
      total += count;
      for (const link of links(group)) {
        const count = catalog.filter(i=>i.ders===query(link.attrs.href).ders).length;
        assert(link.children[1].textContent === (count ? `${count} kaynak` : 'Henüz kaynak yok'),'Wrong subject count');
      }
    }
    assert(total===catalog.filter(i=>metadata.dersler[i.ders]).length,'Group total');
  });
  const form = f.ids['hizli-bul'], {sinif,ders,tur} = form.elements;
  check('Grade change includes electives and clears incompatible subject', () => {
    sinif.value='5'; ders.value='fizik'; sinif.listeners.change();
    const keys=ders.children.map(n=>n.attrs.value).filter(Boolean);
    assert(keys.includes('arapca') && keys.includes('matematik'),'Elective or main subject missing');
    assert(!keys.includes('fizik') && ders.value==='','Incompatible selection retained');
    ders.value='matematik';sinif.value='6';sinif.listeners.change();
    assert(ders.value==='matematik','Compatible choice lost');
  });
  check('Quick finder preserves all three choices and Turkish category encoding', () => {
    sinif.value='5';ders.value='matematik';tur.value='Çalışma kâğıdı';
    let prevented=false;form.listeners.submit({preventDefault:()=>{prevented=true;}});
    const q=query(f.location.href);
    assert(prevented && q.sinif==='5' && q.ders==='matematik' && q.tur==='Çalışma kâğıdı','Wrong navigation');
  });
  check('Eight category and grade colors remain distinct',()=>{
    assert(new Set(f.window.Kesif.categories.map(c=>c.color)).size===8,'Repeated category color');
    assert(new Set(Object.keys(metadata.siniflar).map(f.window.Kesif.gradeColor)).size===Object.keys(metadata.siniflar).length,'Repeated grade color');
  });
  const empty = await render({...data,icerikler:[]});
  check('A valid empty catalog displays zero rather than a load failure',()=>{
    assert(empty.ids.kaynak.textContent==='0','Empty total');
    assert(links(empty.ids['kesif-kategoriler']).length===8,'Empty category links lost');
    assert(!all(empty.ids['kesif-kategoriler']).some(n=>n.attrs.role==='alert'),'False error');
  });
  const failed = await render({...data,icerikler:[],iceriklerYuklendi:false});
  check('Unavailable data stops both loading placeholders and shows an error',()=>{
    assert(all(failed.ids['kesif-kategoriler']).some(n=>n.attrs.role==='alert'),'Missing load error');
    assert(failed.ids['kesif-dersler'].textContent.includes('yüklenemedi'),'Subject loading placeholder stuck');
  });
  const future = await render({...data,dersler:{...metadata,dersler:{...metadata.dersler,'yeni-ders':'Yeni ders'}},icerikler:[...catalog,{ders:'yeni-ders',tur:'Ders kitabı'}]});
  check('New subjects are included without changing source content',()=>{
    const link=links(future.ids['kesif-dersler']).find(n=>query(n.attrs.href).ders==='yeni-ders');
    assert(link && link.textContent==='Yeni ders1 kaynak','New subject missing');
  });
  return {status:'passed',environment:'JavaScript V8 minimal DOM; no browser rendering',cases,resources:catalog.length,subjects:Object.keys(metadata.dersler).length};
}
if (typeof module !== 'undefined') module.exports = {runHomeChecks};
if (typeof require !== 'undefined' && require.main === module) {
  const fs=require('node:fs'),path=require('node:path'),root=path.resolve(__dirname,'../public');
  runHomeChecks(fs.readFileSync(path.join(root,'kesif.js'),'utf8'),JSON.parse(fs.readFileSync(path.join(root,'veri/dersler.json'),'utf8')),JSON.parse(fs.readFileSync(path.join(root,'veri/icerikler.json'),'utf8')).icerikler).then(r=>console.log(JSON.stringify(r,null,2))).catch(e=>{console.error(e);process.exitCode=1;});
}
