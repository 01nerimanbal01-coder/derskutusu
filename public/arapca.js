// Codex: Arapça harf ve kelime çalışması. İlerleme yalnız cihazda saklanır.
(() => {
  const alan = $('#a-alan'); if (!alan) return;
  const MODLAR = [['harfler','Harfler'],['hareke','Harekeler'],['kartlar','Kartlar'],['dinle','Dinle'],['test','Test'],['yaz','Yaz'],['eslestir','Eşleştir']];
  const KEY = 'dk-arapca-ogrenildi-v1';
  const state = { grade:5, topic:1, mode:'harfler' }; let data, learned={};
  try { const value=JSON.parse(localStorage.getItem(KEY)||'{}'); if(value && typeof value==='object' && !Array.isArray(value)) learned=value; } catch {}
  const mix = values => { const a=[...values]; for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a; };
  const ar = (s,cls='') => el('bdi',{lang:'ar',dir:'rtl',sinif:`a-ar ${cls}`},s);
  const button = (s,fn,cls='dugme') => el('button',{type:'button',sinif:cls,onclick:fn},s);
  const topic = () => data.siniflar.find(x=>x.sinif===state.grade).temalar.find(x=>x.no===state.topic);
  const words = () => topic().kelimeler;
  const meaningKey = w => w.tr.replace(/\s*\(.*$/, '').trim();
  function plannedSlots(n){
    // On soruda her cevap konumu 2–3 kez kullanılır; üçlü tekrar olmaz.
    for(let attempt=0;attempt<100;attempt++){
      const slots=mix(Array.from({length:n},(_,i)=>i%4));
      if(!slots.some((v,i)=>i>1 && slots[i-1]===v && slots[i-2]===v)) return slots;
    }
    return Array.from({length:n},(_,i)=>i%4);
  }
  function optionsFor(word,all,slot){
    const candidates=mix(all.filter(x=>x!==word && meaningKey(x)!==meaningKey(word)))
      .filter((x,i,a)=>a.findIndex(y=>meaningKey(y)===meaningKey(x))===i)
      .sort((a,b)=>Math.abs(a.tr.length-word.tr.length)-Math.abs(b.tr.length-word.tr.length));
    const options=mix(candidates.slice(0,3));options.splice(slot,0,word);return options;
  }
  const id = w => `${state.grade}|${w.ar}`;
  const mark = w => {learned[id(w)]=true;try{localStorage.setItem(KEY,JSON.stringify(learned));}catch{} progress();};
  function progress(){const n=words().filter(w=>learned[id(w)]).length;$('#a-ilerleme').textContent=`${n} / ${words().length}`;$('#a-cubuk').style.width=`${100*n/words().length}%`;}
  // Farklı harfler (ör. أ/ا, ة/ه, ي/ى) birleştirilmez. Hareke ve uzatma çizgisi isteğe bağlıdır.
  const base = s => s.normalize('NFC').replace(/[\u064B-\u0652\u0670\u0640]/g,'').replace(/[.!?؟،,؛]/g,'').replace(/\s+/g,' ').trim();
  // Saf yazım denetimi; ekran veya ses özelliği gerektirmez.
  function answerMatches(input,target,sensitive=false){
    if(base(input)!==base(target)) return false;
    if(!sensitive) return true;
    const ending=input.normalize('NFC').replace(/[.!?؟،,؛\u0640]/g,'').trim();
    const marks=(ending.match(/[\u064B-\u0652\u0670]+$/)||[''])[0];
    const vowels=[...marks].filter(c=>'َُِ'.includes(c));
    return vowels.length===1 && vowels[0]===target.slice(-1);
  }
  const speechOK = 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
  const voice = () => speechOK ? speechSynthesis.getVoices().find(v=>/^ar(?:-|$)/i.test(v.lang)) : null;
  function say(s,done){const v=voice();if(!v){$('#a-ses-durum').textContent='Bu cihazda Arapça ses bulunamadı. Harf ve kelimeleri yazılı çalışabilirsin.';return false;}speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(s);u.voice=v;u.lang=v.lang;u.rate=.8;u.onend=u.onerror=()=>done?.();speechSynthesis.speak(u);return true;}
  function voiceStatus(){$('#a-ses-durum').textContent=voice()?'Dinleme için cihazının Arapça sesi kullanılır. Harf seslerini MEB kitabındaki ses örnekleriyle de karşılaştır.':'Bu cihazda Arapça ses bulunamadı. Harf ve kelimeleri yazılı çalışabilirsin.';}
  const listen = s => button('Dinle',()=>say(s));
  let odak=null;
  function controls(){
    $('#a-sinif').replaceChildren(...data.siniflar.map(g=>el('button',{type:'button',sinif:'sekme','aria-pressed':String(g.sinif===state.grade),onclick:()=>{state.grade=g.sinif;state.topic=g.temalar[0].no;odak='#a-sinif';draw();}},`${g.sinif}. sınıf`)));
    const select=$('#a-konu');select.replaceChildren(...data.siniflar.find(g=>g.sinif===state.grade).temalar.map(t=>el('option',{value:t.no,selected:t.no===state.topic},`${t.ad} · 1. hafta (${t.kelimeler.length})`)));select.onchange=()=>{state.topic=Number(select.value);draw();};
    $('#a-modlar').replaceChildren(...MODLAR.map(([m,t])=>el('button',{type:'button',sinif:'sekme','aria-pressed':String(m===state.mode),onclick:()=>{state.mode=m;odak='#a-modlar';draw();}},t)));
    // Sekmeler yeniden üretildiği için odak, basılan sekmenin yenisine geri verilir.
    if(odak){$(odak+' [aria-pressed="true"]')?.focus();odak=null;}
  }
  function alphabet(){
    const detail=el('div',{sinif:'a-detay','aria-live':'polite'}), grid=el('div',{sinif:'a-harfler',dir:'rtl'});
    let selected=null;
    function show(h,b){if(selected)selected.setAttribute('aria-pressed','false');selected=b;b.setAttribute('aria-pressed','true');
      const forms=[['Tek başına',h.harf],['Başta',h.harf+(h.sonrakiyle_birlesir?'ـ':'')],['Ortada','ـ'+h.harf+(h.sonrakiyle_birlesir?'ـ':'')],['Sonda','ـ'+h.harf]];
      detail.replaceChildren(el('h3',{},`${h.ad} harfi`),el('div',{sinif:'a-bicimler'},forms.map(([label,f])=>el('div',{},ar(f,'a-buyuk'),el('span',{},label)))),el('p',{},h.sonrakiyle_birlesir?'Önceki ve sonraki harfle birleşebilir.':'ا د ذ ر ز و harfleri sonraki harfle birleşmez; kendilerinden önceki harfe bağlanabilir.'),el('p',{sinif:'kelime-not'},'Uzatma çizgileri, harfin bağlantı yerini gösterir; harfin parçası değildir.'));
    }
    for(const h of data.harfler){const b=el('button',{type:'button','aria-label':`${h.ad} harfi`,'aria-pressed':'false',onclick:()=>show(h,b)},ar(h.harf,'a-buyuk'),el('span',{dir:'ltr'},h.ad));grid.append(b);if(!selected)show(h,b);}
    alan.append(el('p',{},'Alfabedeki 28 harfi incele. Bir harfe dokunarak yazı içindeki biçimlerini gör.'),button('Harfleri tanı: 10 soru',()=>letterQuiz()),grid,detail);
  }
  // Yeni soru gelince klavye odağı kaybolmasın: soru başlığına taşınır.
  function odakla(kap){const h=kap.querySelector('h3');if(h){h.tabIndex=-1;h.focus();}}
  function letterQuiz(){
    const qs=mix(data.harfler).slice(0,10);let i=0,score=0;
    function next(){alan.replaceChildren();if(i===qs.length){alan.append(el('h3',{},`10 soruda ${score} doğru`),button('Harflere dön',draw));return;}
      const q=qs[i],fb=el('p',{role:'status'}),opts=mix([q,...mix(data.harfler.filter(h=>h!==q)).slice(0,3)]);let answered=false;
      const row=el('div',{sinif:'a-harf-sec'});opts.forEach(h=>{const b=button(ar(h.harf,'a-buyuk'),()=>{if(answered)return;answered=true;for(const x of row.children)x.disabled=true;if(h===q){score++;fb.textContent='Doğru!';}else fb.replaceChildren('Doğru harf: ',ar(q.harf),' — '+q.ad);const nb=button('Sonraki soru',()=>{i++;next();odakla(alan);},'dugme ana');alan.append(nb);nb.focus();});row.append(b);});
      alan.append(el('p',{},`${i+1} / 10`),el('h3',{},`“${q.ad}” hangi harftir?`),row,fb);
    }next();
  }
  function vowels(){
    const box=el('div',{sinif:'a-hareke'});for(const [s,t,d] of [['بَ','Üstün (fetha)','Harfin üstündeki kısa çizgi.'],['بِ','Esre (kesra)','Harfin altındaki kısa çizgi.'],['بُ','Ötre (damma)','Harfin üstündeki kıvrımlı işaret.']])box.append(el('div',{},ar(s,'a-buyuk'),el('h3',{},t),el('p',{},d),listen(s)));
    alan.append(el('p',{},'Noktalar harfi, harekeler kısa sesi ayırt etmeyi sağlar.'),box);
    let i=0,score=0;const qs=mix([['تَ','Üstün'],['تِ','Esre'],['تُ','Ötre'],['جَ','Üstün'],['جِ','Esre'],['جُ','Ötre']]);const exercise=el('div',{sinif:'a-detay'});alan.append(exercise);
    function next(){if(i===qs.length){exercise.replaceChildren(el('p',{},`6 soruda ${score} doğru`),button('Yeniden çalış',draw));return;}const [s,correct]=qs[i],feedback=el('p',{role:'status'});let answered=false;const opts=el('div',{sinif:'k-dugmeler sol'});['Üstün','Esre','Ötre'].forEach(t=>opts.append(button(t,()=>{if(answered)return;answered=true;for(const b of opts.children)b.disabled=true;if(t===correct)score++;feedback.textContent=t===correct?'Doğru!':`Doğrusu: ${correct}.`;exercise.append(button('Sonraki',()=>{i++;next();}));})));exercise.replaceChildren(el('h3',{},`${i+1} / 6 · Bu harfin harekesi hangisi?`),ar(s,'a-buyuk'),opts,feedback);}next();
  }
  function cards(){let fresh=false,list=[],i=0;const box=el('div',{}),check=el('input',{type:'checkbox',onchange:e=>{fresh=e.target.checked;start();}});alan.append(el('label',{},check,' Yalnız öğrenmediğim kelimeler'),box);
    function start(){list=mix(words().filter(w=>!fresh||!learned[id(w)]));i=0;next();}
    function next(){box.replaceChildren();if(i===list.length){box.append(el('p',{},list.length?'Kartların sonuna geldin.':'Bu grupta öğrenmediğin kelime kalmadı.'),button('Yeniden başla',start));return;}
      const w=list[i],meaning=el('p',{sinif:'a-anlam',hidden:true},w.tr),flip=button('Anlamı göster',()=>{meaning.hidden=!meaning.hidden;flip.textContent=meaning.hidden?'Anlamı göster':'Anlamı gizle';});
      box.append(el('p',{sinif:'k-sira'},`${i+1} / ${list.length}`),el('div',{sinif:'a-kart'},ar(w.ar,'a-kelime'),meaning,flip,listen(w.ar)),el('div',{sinif:'k-dugmeler'},button('Tekrar edeceğim',()=>{i++;next();}),button('Biliyorum',()=>{mark(w);i++;next();},'dugme ana')));
    }start();
  }
  function listening(){const list=el('ul',{sinif:'a-sozluk'});for(const w of words())list.append(el('li',{},ar(w.ar),el('span',{},w.tr),listen(w.ar)));alan.append(list);}
  function quiz(){const qs=mix(words()).slice(0,10),slots=plannedSlots(qs.length);let i=0,score=0;const box=el('div',{});alan.append(box);
    function next(){box.replaceChildren();if(i===qs.length){box.append(el('h3',{},`${qs.length} soruda ${score} doğru`),button('Yeni test',draw));return;}const w=qs[i],fb=el('p',{role:'status',sinif:'etk-geri'}),row=el('div',{sinif:'etk-secenekler'});let answered=false;
      optionsFor(w,words(),slots[i]).forEach(x=>row.append(button(x.tr,e=>{if(answered)return;answered=true;for(const b of row.children)b.disabled=true;if(x===w){score++;e.currentTarget.classList.add('dogru');fb.textContent='Doğru!';}else{e.currentTarget.classList.add('yanlis');fb.textContent=`Doğrusu: ${w.tr}`;}const nb=button('Sonraki soru',()=>{i++;next();odakla(box);},'dugme ana');box.append(nb);nb.focus();},'etk-sec')));
      box.append(el('p',{},`${i+1} / ${qs.length}`),el('h3',{},'Türkçe anlamı hangisidir?'),ar(w.ar,'a-kelime'),row,fb);
    }next();
  }
  function keyboard(input){const k=el('div',{sinif:'a-klavye',dir:'rtl','aria-label':'Arapça klavye'});const chars=[...data.harfler.map(h=>h.harf),'أ','إ','آ','ء','ؤ','ئ','ة','ى','َ','ِ','ُ','ْ','ّ','ً','ٍ','ٌ'];for(const ch of chars)k.append(button(ar(ch),()=>{if(input.readOnly)return;input.focus();input.setRangeText(ch,input.selectionStart,input.selectionEnd,'end');}));k.append(button('Boşluk',()=>{if(!input.readOnly){input.focus();input.setRangeText(' ',input.selectionStart,input.selectionEnd,'end');}}),button('Sil',()=>{if(input.readOnly)return;const s=input.selectionStart,e=input.selectionEnd;input.setRangeText('',s===e?Math.max(0,s-1):s,e,'end');input.focus();}));return k;}
  function writing(){const qs=mix(words()).slice(0,10);let i=0,score=0;const box=el('div',{});alan.append(box);
    function next(){box.replaceChildren();if(i===qs.length){box.append(el('h3',{},`${qs.length} kelimeden ${score} doğru`),button('Yeni kelimeler',draw));return;}
      const w=qs[i],input=el('input',{type:'text',lang:'ar',dir:'rtl',sinif:'a-ar k-girdi',autocomplete:'off',spellcheck:'false','aria-label':'Arapçasını yaz'}),fb=el('p',{role:'status'}),hint=el('p',{});let done=false,hinted=false;
      const sensitive=words().some(x=>x.ar!==w.ar && base(x.ar)===base(w.ar));
      const form=el('form',{sinif:'k-yaz',onsubmit:e=>{e.preventDefault();if(done){i++;next();return;}if(!input.value.trim()){input.focus();return;}
        const correct=answerMatches(input.value,w.ar,sensitive);
        done=true;input.readOnly=true;if(correct){score++;if(!hinted)mark(w);fb.textContent='Doğru!';}else fb.replaceChildren('Doğru yazımı: ',ar(w.ar));submit.textContent='Sonraki kelime';submit.focus();
      }}),submit=el('button',{type:'submit',sinif:'dugme ana'},'Kontrol et');
      form.append(el('label',{},'Arapçasını yaz: ',el('b',{},w.tr),input),el('p',{sinif:'kelime-not'},sensitive?'Bu ifadede son hareke anlamı değiştirir. Son harekeyi de yaz.':'Harekeleri yazman zorunlu değil. Harflerin doğru olması gerekir.'),keyboard(input),hint,fb,el('div',{sinif:'k-dugmeler sol'},submit,button('İlk harf ipucu',()=>{hinted=true;hint.replaceChildren('İlk harf: ',ar(base(w.ar)[0]));input.focus();}),listen(w.ar)));
      box.append(el('p',{},`${i+1} / ${qs.length}`),form);
    }next();
  }
  function matching(){const ws=mix(words()).filter((x,i,a)=>a.findIndex(y=>meaningKey(y)===meaningKey(x))===i).slice(0,6),left=el('div',{sinif:'etk-sutun'}),right=el('div',{sinif:'etk-sutun'}),feedback=el('p',{role:'status'},'Bir Arapça kelimeyi ve Türkçe karşılığını seç.');let picked=null,leftCount=ws.length;
    function choose(b,w,side){if(b.disabled)return;if(!picked||picked.side===side){if(picked)picked.b.classList.remove('secili');picked={b,w,side};b.classList.add('secili');return;}const previous=picked;picked=null;previous.b.classList.remove('secili');if(previous.w===w){previous.b.disabled=b.disabled=true;previous.b.classList.add('dogru');b.classList.add('dogru');mark(w);leftCount--;feedback.textContent=leftCount?`${leftCount} çift kaldı.`:'Bütün kelimeleri eşleştirdin.';if(!leftCount)alan.append(button('Yeni eşleştirme',draw));}else feedback.textContent='Bu iki kelime eşleşmiyor. Yeniden dene.';}
    for(const w of ws){const b=button(ar(w.ar),()=>choose(b,w,'ar'),'etk-sec');left.append(b);}for(const w of mix(ws)){const b=button(w.tr,()=>choose(b,w,'tr'),'etk-sec');right.append(b);}alan.append(feedback,el('div',{sinif:'etk etk-eslestir'},el('div',{sinif:'etk-sutunlar'},left,right)));
  }
  const render={harfler:alphabet,hareke:vowels,kartlar:cards,dinle:listening,test:quiz,yaz:writing,eslestir:matching};
  function draw(){if(speechOK)speechSynthesis.cancel();controls();progress();voiceStatus();alan.replaceChildren();history.replaceState(null,'',`?s=${state.grade}&t=${state.topic}&k=${state.mode}`);$('#a-baslik').textContent=['harfler','hareke'].includes(state.mode)?'Alfabe ve yazıya hazırlık':`${state.grade}. sınıf · ${topic().ad}`;render[state.mode]();}
  veri('arapca-kelimeler.json').then(v=>{if(!v){alan.textContent='İçerik yüklenemedi. Sayfayı yenileyin.';return;}data=v;const p=new URLSearchParams(location.search),g=data.siniflar.find(x=>x.sinif===Number(p.get('s')))||data.siniflar[0];state.grade=g.sinif;state.topic=(g.temalar.find(t=>t.no===Number(p.get('t')))||g.temalar[0]).no;if(Object.prototype.hasOwnProperty.call(render,p.get('k')))state.mode=p.get('k');draw();$('#a-sifirla').onclick=()=>{if(!confirm('Bu konu grubundaki öğrenme işaretleri sıfırlansın mı?'))return;for(const w of words())delete learned[id(w)];try{localStorage.setItem(KEY,JSON.stringify(learned));}catch{}progress();};if(speechOK)speechSynthesis.addEventListener('voiceschanged',voiceStatus);});
})();
