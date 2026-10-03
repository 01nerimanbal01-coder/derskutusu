// Arama önerileri: gerçek arayüz bloğu, kontrollü zamanlayıcılar ve küçük DOM benzetimi.
// Gerçek tarayıcı veya görsel test değildir.

function autocompleteFixture(source) {
  const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
  class Node {
    constructor(tag='div',attrs={},...children){this.tag=tag;this.attrs={...attrs};this.children=children;this.events={};this.hidden=false;this.value='';this.clicked=0;}
    addEventListener(type,fn){(this.events[type]??=[]).push(fn);}
    fire(type,event={}){event.preventDefault??=()=>{event.prevented=true;};for(const fn of this.events[type]??[])fn(event);return event;}
    setAttribute(k,v){this.attrs[k]=v;}
    removeAttribute(k){delete this.attrs[k];}
    replaceChildren(...items){this.children=items;}
    all(){return [this,...this.children.flatMap(c=>c instanceof Node?c.all():[])];}
    contains(n){return this.all().includes(n);}
    scrollIntoView(){}
    click(){this.clicked++;}
    focus(){document.activeElement=this;this.fire('focus');}
    blur(){document.activeElement=null;form.fire('focusout',{relatedTarget:null});}
  }
  const form=new Node('form'),input=new Node('input'),list=new Node('ul');list.hidden=true;form.children=[input,list];
  const document=new Node('document');document.activeElement=input;
  const timers=new Map();let timerId=0;let resolveIndex;let ready=new Promise(r=>{resolveIndex=r;});
  let searches=[];
  const selector=(s,node)=> s==='.ust-arama'?form:s==='input'&&node===form?input:s==='.oneri'&&node===form?list:null;
  const all=(s,node)=>s==='li'?node.children:s==='li a'?node.children.map(n=>n.children[0]):[];
  const begin=source.indexOf('  // Üst menüdeki kutu: anlık öneriler');
  const end=source.indexOf('  // ara.html: bütün sonuçlar',begin);
  assert(begin>=0&&end>begin,'Header boundaries missing');
  new Function('$','$$','el','matchMedia','dizinHazirla','Arama','adres','hedef','vurgula','TUR_ETIKET','altBilgi','simge','setTimeout','clearTimeout','document',source.slice(begin,end))(
    selector,all,(tag,attrs,...children)=>new Node(tag,attrs,...children),()=>({matches:false}),()=>ready,
    {ara:q=>{searches.push(q);return {sonuclar:[0,1].map(i=>({b:{tip:'icerik',baslik:q+' '+i,adres:'/sonuc/'+q+'/'+i}}))};}},
    b=>b.adres,()=>({}),s=>[s],{icerik:'İçerik'},()=>'',()=>new Node('svg'),
    fn=>{const id=++timerId;timers.set(id,fn);return id;},id=>timers.delete(id),document);
  const flush=async()=>{await Promise.resolve();await Promise.resolve();};
  return {form,input,list,document,timers,searches,assert,
    type(value){input.value=value;input.fire('input');},
    key(key){return input.fire('keydown',{key});},
    outside(){document.fire('click',{target:new Node()});},
    leave(){document.activeElement=new Node('button');form.fire('focusout',{relatedTarget:document.activeElement});},
    async tick(){const todo=[...timers.values()];timers.clear();todo.forEach(fn=>fn());await flush();},
    async ready(){resolveIndex();await flush();},flush
  };
}

async function runSearchChecks(source) {
  const cases=[];
  const check=async(name,run)=>{try{const f=autocompleteFixture(source);await run(f);cases.push({name,status:'passed'});}catch(e){cases.push({name,status:'failed',error:e.message});}};
  const start=async f=>{f.type('matematik');await f.tick();};
  const closed=f=>{f.assert(f.list.hidden,'Suggestions reopened or stayed visible');f.assert(f.input.attrs['aria-expanded']==='false','aria-expanded did not close');};
  await check('Escape while index is loading',async f=>{await start(f);f.key('Escape');await f.ready();closed(f);});
  await check('Escape before debounce starts',async f=>{f.type('matematik');f.key('Escape');await f.tick();await f.ready();closed(f);});
  await check('Outside click while loading',async f=>{await start(f);f.outside();await f.ready();closed(f);});
  await check('Keyboard focus leaves while loading',async f=>{await start(f);f.leave();await f.ready();closed(f);});
  await check('Editing query invalidates pending result immediately',async f=>{
    await start(f);f.type('tarih');await f.ready();closed(f);
    await f.tick();f.assert(!f.list.hidden,'Latest query did not recover');f.assert(f.searches.at(-1)==='tarih','Wrong query displayed');
  });
  await check('Clearing text hides visible suggestions immediately',async f=>{
    await start(f);await f.ready();f.assert(!f.list.hidden,'Setup did not open');f.type('');closed(f);
    await f.tick();closed(f);
  });
  await check('Rapid typing renders only latest query',async f=>{
    f.type('mat');f.type('mate');f.type('matematik');await f.tick();await f.ready();
    f.assert(f.searches.length===1&&f.searches[0]==='matematik','Superseded queries rendered');
    f.assert(!f.list.hidden&&f.list.children.length===3,'Results or all-results link missing');
  });
  await check('Focus moving to result link preserves click target',async f=>{
    await start(f);await f.ready();const link=f.list.children[0].children[0];
    f.form.fire('focusout',{relatedTarget:link});f.assert(!f.list.hidden,'Internal focus unexpectedly closed results');
    link.click();f.assert(link.clicked===1,'Link unusable');
  });
  await check('ArrowDown and Enter still activate selected result',async f=>{
    await start(f);await f.ready();const down=f.key('ArrowDown');const enter=f.key('Enter');
    f.assert(down.prevented&&enter.prevented,'Keyboard event not handled');
    f.assert(f.input.attrs['aria-activedescendant']==='oneri-0','Active result not announced');
    f.assert(f.list.children[0].children[0].clicked===1,'Selected result not activated');
  });
  await check('New input clears old keyboard selection',async f=>{
    await start(f);await f.ready();f.key('ArrowDown');f.type('tarih');
    f.assert(!('aria-activedescendant' in f.input.attrs),'Old active descendant retained');
    closed(f);await f.tick();f.assert(!f.list.hidden,'New suggestions missing');
    f.assert(!('aria-activedescendant' in f.input.attrs),'New suggestions inherit old selection');
  });
  await check('Programmatic query change cannot render stale result',async f=>{
    await start(f);f.input.value='tarih';await f.ready();closed(f);
  });
  await check('Refocusing after Escape opens a fresh search',async f=>{
    await start(f);f.key('Escape');f.input.focus();await f.ready();
    f.assert(!f.list.hidden,'Refocus could not reopen suggestions');
    f.assert(f.searches.length===1,'Cancelled search also rendered');
  });
  await check('Keyboard focus leaves already visible suggestions',async f=>{
    await start(f);await f.ready();f.leave();closed(f);
  });

  await check('First ArrowUp selects final option',async f=>{
    await start(f);await f.ready();f.key('ArrowUp');
    f.assert(f.input.attrs['aria-activedescendant']==='oneri-2','Initial Up skipped final option');
    f.assert(f.list.children[2].attrs['aria-selected']==='true','Final option not announced as selected');
  });
  await check('ArrowUp wraps from first option',async f=>{
    await start(f);await f.ready();f.key('ArrowDown');f.key('ArrowUp');
    f.assert(f.input.attrs['aria-activedescendant']==='oneri-2','First-to-last wrap failed');
  });
  await check('ArrowUp traverses every option backwards',async f=>{
    await start(f);await f.ready();
    for (const expected of [2,1,0,2]) {
      f.key('ArrowUp');
      f.assert(f.input.attrs['aria-activedescendant']==='oneri-'+expected,'Option skipped during backwards navigation');
    }
  });
  return {status:cases.every(c=>c.status==='passed')?'passed':'failed',environment:'JavaScript V8 with controlled timers and minimal DOM fixture; no browser',passed:cases.filter(c=>c.status==='passed').length,total:cases.length,cases};
}

if (typeof module !== 'undefined') module.exports = {runSearchChecks};
if (typeof require !== 'undefined' && require.main === module) {
  const fs = require('node:fs');
  const path = require('node:path');
  runSearchChecks(fs.readFileSync(path.resolve(__dirname, '../public/arama.js'), 'utf8')).then(result => {
    console.log(JSON.stringify(result, null, 2));
    if (result.status !== 'passed') process.exitCode = 1;
  }).catch(error => { console.error(error.stack); process.exitCode = 1; });
}
