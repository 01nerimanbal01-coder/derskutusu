// Ders Kutusu · Yayımlanmış bir konu sayfasından bağımsız sunum oturumu.
// Sunucuya veri göndermez, yeni soru üretmez; sadece bu sekmede set/konum hatırlar.
(() => {
  'use strict';
  function hash(text) {
    let n = 2166136261;
    for (const c of text) n = Math.imul(n ^ c.codePointAt(0), 16777619);
    return (n >>> 0).toString(36);
  }
  function pick(pool, seen = [], count = 4, random = Math.random) {
    const unique = [...new Set(pool)];
    const known = [...new Set(seen)].filter(id => unique.includes(id));
    let available = unique.filter(id => !known.includes(id));
    const recycled = unique.length > 0 && available.length === 0;
    if (recycled) available = [...unique];
    for (let i = available.length - 1; i > 0; i--) {
      const j = Math.floor(random() * (i + 1));
      [available[i], available[j]] = [available[j], available[i]];
    }
    const ids = available.slice(0, Math.max(0, Math.floor(count)));
    return { ids, seen: [...(recycled ? [] : known), ...ids], recycled };
  }
  function restore(value, pool) {
    if (!value || value.version !== 2 || !Array.isArray(value.ids) || !Array.isArray(value.seen)) return null;
    const ids = [...new Set(value.ids)].filter(id => pool.includes(id));
    // Değişen/kaldırılan bir soruyla eski seti sessizce karıştırma.
    if (ids.length !== value.ids.length || (pool.length && !ids.length)) return null;
    return { version: 2, ids, seen: [...new Set(value.seen)].filter(id => pool.includes(id)),
      index: Number.isSafeInteger(value.index) && value.index >= 0 ? value.index : 0,
      mode: value.mode === 'questions' ? 'questions' : 'lesson' };
  }
  function fullscreenSession(doc, target) {
    let pending = null;
    const active = () => doc.fullscreenElement === target;
    function toggle() {
      if (pending) return pending;
      if (!active() && typeof target.requestFullscreen !== 'function') return Promise.resolve(false);
      try {
        const request = active() ? doc.exitFullscreen() : target.requestFullscreen();
        pending = Promise.resolve(request).then(() => true).finally(() => { pending = null; });
        return pending;
      } catch (error) { return Promise.reject(error); }
    }
    async function exitOwned() {
      if (pending) { try { await pending; } catch {} }
      if (active()) await doc.exitFullscreen();
    }
    return { active, toggle, exitOwned };
  }
  globalThis.DersSlaytModel = Object.freeze({ hash, pick, restore, fullscreenSession });
  if (typeof document === 'undefined') return;
  const source = document.querySelector('article.ozet');
  const actions = document.querySelector('.ozet-bas .g-dugmeler');
  if (!source || !actions || document.getElementById('ders-slayt-ac')) return;
  const templates = new Map(), intro = [], topics = [], questions = [], ending = [], resources = [];
  function collect(selector, kind, target) {
    source.querySelectorAll(selector).forEach(node => {
      const id = kind + '-' + hash(node.outerHTML);
      if (templates.has(id)) return;
      templates.set(id, { kind, node: node.cloneNode(true) });
      target.push(id);
    });
  }
  collect('.ozet-ust', 'intro', intro);
  collect('.ozet-bolum.konu', 'topic', topics);
  collect('.ornekler > .ornek', 'example', questions);
  collect('.etk-liste > .etk', 'activity', questions);
  collect('.ozet-son', 'ending', ending);
  collect('.ozet-ilgili', 'resources', resources);
  if (!topics.length && !questions.length) return;

  const trigger = document.createElement('button');
  trigger.type = 'button'; trigger.id = 'ders-slayt-ac'; trigger.className = 'dugme ana';
  trigger.textContent = 'Slaytla ders işle'; trigger.setAttribute('aria-haspopup', 'dialog');
  actions.prepend(trigger);
  const css = document.createElement('link'); css.rel = 'stylesheet'; css.href = '/ders-slayt.css?v=20261003-preview2';
  document.head.append(css);

  const dialog = document.createElement('dialog');
  dialog.className = 'ds'; dialog.setAttribute('aria-labelledby', 'ds-title');
  dialog.innerHTML = `<div class="ds-shell"><header class="ds-header"><div><p class="ds-eyebrow">DERS KUTUSU · SINIFTA BİRLİKTE</p><h2 id="ds-title"></h2></div><button type="button" data-action="close">Derse dön</button></header>
    <div class="ds-tools"><label>Sunum <select data-control="mode"><option value="lesson">Dersin tamamı</option><option value="questions">Kısa soru seti</option></select></label>
    <button type="button" data-action="restart">Aynı seti baştan</button><button type="button" data-action="new">Yeni soru seti</button>
    <button type="button" data-action="ink" aria-pressed="false">Kalem</button><button type="button" data-action="fullscreen" aria-pressed="false">Tam ekran</button></div>
    <div class="ds-outline"><label>Bölüme git <select data-control="slide" aria-label="Ders bölümleri"></select></label></div>
    <p class="ds-notice" role="status"></p>
    <div class="ds-stage-wrap"><div class="ds-stage ozet" tabindex="0" aria-label="Ders slaytı"></div><div class="ds-ink" hidden></div></div>
    <footer class="ds-footer"><button type="button" data-action="previous" aria-label="Önceki slayt">← Önceki</button><div><p class="ds-progress" role="status" aria-live="polite"></p><progress aria-label="Sunum ilerlemesi"></progress></div><button type="button" class="ds-primary" data-action="reveal">Sonraki adımı göster</button><button type="button" data-action="next" aria-label="Sonraki slayt">Sonraki →</button></footer></div>`;
  document.body.append(dialog);
  dialog.querySelector('#ds-title').textContent = document.querySelector('.ozet-bas h1')?.textContent || 'Ders sunumu';
  const stage = dialog.querySelector('.ds-stage'), ink = dialog.querySelector('.ds-ink');
  // <dialog> tam ekran hedefi olamaz; içindeki normal HTML kabını kullan.
  const fullscreen = fullscreenSession(document, dialog.querySelector('.ds-shell'));
  for (const name of source.classList) if (name.startsWith('ders-')) stage.classList.add(name);
  const notice = dialog.querySelector('.ds-notice'), mode = dialog.querySelector('[data-control="mode"]');
  const button = action => dialog.querySelector(`[data-action="${action}"]`);
  const key = 'derskutusu:slayt:v2:' + location.pathname;
  let state = null, storageOK = true, slides = [], pen = null, drawing = false;
  const drawings = new Map(), slideCache = new Map();
  try { state = restore(JSON.parse(sessionStorage.getItem(key)), questions); } catch { storageOK = false; }
  if (!state) state = { version: 2, ...pick(questions), index: 0, mode: 'lesson' };
  else trigger.textContent = 'Sunuma devam et';
  if (!questions.length) { mode.querySelector('[value="questions"]').disabled = true; state.mode = 'lesson'; }
  mode.value = state.mode;
  button('new').disabled = !questions.length;
  button('ink').disabled = typeof Tahta === 'undefined';
  const baseNotice = () => state.mode === 'lesson'
    ? `Bu sayfanın tamamı: giriş, ${topics.length} konu bölümü ve ${questions.length} örnek/etkinlik. Devam et ile adımlar sırayla açılır; uzun slaytlarda aşağı kaydırabilirsiniz.`
    : `Kısa soru seti: ${questions.length} örnek/etkinlikten ${state.ids.length} seçim. Dersin tamamına Sunum menüsünden dönebilirsiniz.`;
  const explain = message => { notice.textContent = (message || baseNotice()) + (storageOK ? '' : ' Sekme belleği kapalı; yenilemede konum korunamaz.'); };
  function save() {
    try { sessionStorage.setItem(key, JSON.stringify({ version: 2, ids: state.ids, seen: state.seen, index: state.index, mode: state.mode })); }
    catch { storageOK = false; }
  }
  // Kopyalardaki SVG tanımları ve yerel başvurular asıl sayfayla çakışmaz.
  function uniqueIds(node, prefix) {
    const remap = new Map();
    for (const el of [node, ...node.querySelectorAll('[id]')]) {
      if (el.id) { remap.set(el.id, prefix + el.id); el.id = prefix + el.id; }
    }
    for (const el of [node, ...node.querySelectorAll('*')]) {
      for (const attr of [...el.attributes]) {
        let value = attr.value;
        if (['aria-labelledby', 'aria-describedby', 'aria-controls', 'for'].includes(attr.name)) {
          value = value.split(/\s+/).map(id => remap.get(id) || id).join(' ');
        } else if (['href', 'xlink:href'].includes(attr.name) && value.startsWith('#')) {
          value = '#' + (remap.get(value.slice(1)) || value.slice(1));
        }
        value = value.replace(/url\(#([^)]+)\)/g, (all, id) => remap.has(id) ? `url(#${remap.get(id)})` : all);
        if (value !== attr.value) el.setAttribute(attr.name, value);
      }
    }
  }
  function makeSlide(id) {
    if (slideCache.has(id)) { const saved = slideCache.get(id); stage.append(saved.frame); return saved; }
    const template = templates.get(id), node = template.node.cloneNode(true);
    uniqueIds(node, 'ds-' + id + '-');
    const frame = document.createElement('section'); frame.className = 'ds-slide'; frame.dataset.slide = id;
    const tag = document.createElement('p'); tag.className = 'ds-slide-tag';
    tag.textContent = { intro: 'Derse hazırlık', resources: 'Ders kaynakları', topic: 'Konu · adım adım', example: 'Birlikte çözelim', activity: 'Sıra sizde', ending: 'Dersi toparlayalım' }[template.kind];
    frame.append(tag);
    const steps = [];
    if (template.kind === 'activity') {
      const root = document.createElement('div'); root.className = 'ds-activity';
      const score = document.createElement('p'); score.className = 'etk-puan'; score.setAttribute('aria-live', 'polite');
      const reset = document.createElement('button'); reset.type = 'button'; reset.className = 'etk-sifirla'; reset.hidden = true;
      const list = document.createElement('ol'); list.className = 'etk-liste'; list.append(node);
      root.append(score, reset, list); frame.append(root);
      if (typeof window.etkinlikKur === 'function') window.etkinlikKur(root);
      else { const warning = document.createElement('p'); warning.textContent = 'Etkinlik bu sunumda açılamadı. Derse dönerek çözebilirsiniz.'; frame.append(warning); }
    } else if (template.kind === 'example') {
      const list = document.createElement('ol'); list.className = 'ornekler'; list.append(node); frame.append(list);
      node.querySelectorAll('details').forEach(d => { d.open = false; });
    } else {
      frame.append(node);
      if (template.kind === 'topic') {
        steps.push(...node.querySelectorAll('.bolum-metin > *, .bolum-yan > *'));
        steps.forEach((step, index) => { step.hidden = index > 0; });
      }
    }
    frame.hidden = true; stage.append(frame);
    const result = { id, frame, steps, kind: template.kind };
    slideCache.set(id, result);
    return result;
  }
  function rememberInk() { if (pen && slides[state.index]) drawings.set(slides[state.index].id, pen.d.cizgiler); }
  function penOff() {
    rememberInk();
    // Kapatılan sunumun Ctrl+Z/Escape olaylarını dinlemeye devam etmesini önle.
    if (pen) { pen.kaldir(); pen = null; }
    drawing = false; ink.hidden = true; button('ink').setAttribute('aria-pressed', 'false');
  }
  function build() {
    penOff(); stage.replaceChildren();
    const ids = state.mode === 'lesson' ? [...intro, ...topics, ...questions, ...ending, ...resources] : state.ids;
    slides = ids.map(makeSlide);
    const outline = dialog.querySelector('[data-control="slide"]');
    outline.replaceChildren(...ids.map((id, i) => {
      const { kind, node } = templates.get(id), option = document.createElement('option');
      const labels = { intro: 'Giriş ve öğrenme çıktıları', example: 'Örnek', activity: 'Etkinlik', ending: 'Dersi toparlayalım', resources: 'Kaynaklar' };
      const title = node.querySelector('h2')?.textContent || labels[kind] || 'Konu';
      option.value = String(i); option.textContent = `${i + 1}. ${title}`;
      return option;
    }));
    button('restart').textContent = state.mode === 'lesson' ? 'Dersi baştan' : 'Aynı seti baştan';
    button('new').textContent = state.mode === 'lesson' ? 'Kısa soru seti oluştur' : 'Yeni soru seti';
    state.index = Math.min(state.index, Math.max(0, slides.length - 1));
  }
  function revealTarget() {
    const current = slides[state.index];
    if (!current) return null;
    return current.steps.find(step => step.hidden)
      || current.frame.querySelector('details:not([open])')
      || current.frame.querySelector('.etk-ipucu-dugme:not([hidden])');
  }
  function updateReveal() {
    const target = revealTarget(), control = button('reveal');
    control.disabled = !target;
    button('next').textContent = target ? 'Devam et →' : 'Sonraki slayt →';
    button('next').disabled = !target && state.index >= slides.length - 1;
    control.textContent = target?.matches('details') ? 'Çözümü göster' : target?.matches('.etk-ipucu-dugme') ? target.textContent : target ? 'Sonraki adımı göster' : slides[state.index]?.kind === 'activity' ? 'Soruyu slaytta yanıtlayın' : 'Tüm adımlar açık';
  }
  function reveal() {
    const target = revealTarget();
    if (target?.matches('details')) target.open = true;
    else if (target?.matches('button')) target.click();
    else if (target) target.hidden = false;
    if (target) target.scrollIntoView({ block: 'nearest', behavior: 'instant' });
    updateReveal();
  }
  function nextStep() { if (revealTarget()) reveal(); else show(state.index + 1); }
  function show(index, focus = true) {
    rememberInk(); state.index = Math.max(0, Math.min(index, slides.length - 1));
    slides.forEach((slide, i) => { slide.frame.hidden = i !== state.index; });
    stage.scrollTop = 0;
    if (pen) pen.yukle(drawings.get(slides[state.index]?.id) || []);
    const number = slides.length ? state.index + 1 : 0;
    dialog.querySelector('.ds-progress').textContent = `${number} / ${slides.length} slayt`;
    const progress = dialog.querySelector('progress'); progress.max = Math.max(1, slides.length); progress.value = number;
    button('previous').disabled = state.index <= 0;
    button('next').disabled = state.index >= slides.length - 1;
    updateReveal(); save();
    dialog.querySelector('[data-control="slide"]').value = String(state.index);
    if (focus) stage.focus({ preventScroll: true });
  }
  function fullscreenLabel() {
    const active = fullscreen.active();
    button('fullscreen').textContent = active ? 'Tam ekrandan çık' : 'Tam ekran';
    button('fullscreen').setAttribute('aria-pressed', String(active));
  }
  async function close() {
    rememberInk(); penOff(); save();
    try { await fullscreen.exitOwned(); } catch {}
    dialog.close(); trigger.textContent = 'Sunuma devam et'; trigger.focus({ preventScroll: true });
  }
  trigger.addEventListener('click', () => {
    if (typeof dialog.showModal !== 'function') { explain('Bu tarayıcı sunum penceresini desteklemiyor.'); trigger.textContent = 'Sunum için güncel tarayıcı gerekir'; return; }
    dialog.showModal(); if (!slides.length) build(); show(state.index); explain();
  });
  dialog.addEventListener('cancel', event => { event.preventDefault(); close(); });
  document.addEventListener('fullscreenchange', fullscreenLabel);
  dialog.addEventListener('click', async event => {
    const control = event.target.closest('[data-action]');
    if (!control || control.disabled) return;
    switch (control.dataset.action) {
      case 'close': close(); break;
      case 'previous': show(state.index - 1); break;
      case 'next': nextStep(); break;
      case 'reveal': reveal(); break;
      case 'restart':
        penOff(); drawings.clear(); slideCache.clear(); state.index = 0; build(); show(0);
        explain((state.mode === 'lesson' ? 'Dersin tamamı' : 'Aynı soru seti') + ' baştan başladı. Cevaplar ve çizimler sıfırlandı.'); break;
      case 'new': {
        const next = pick(questions, state.seen);
        penOff(); drawings.clear(); slideCache.clear(); state = { ...state, ...next, index: 0, mode: 'questions' }; mode.value = state.mode; build(); show(0);
        explain(next.recycled ? 'Bu dersteki soru havuzu tamamlandı; önceki sorular yeniden kullanılabilir. Yeni soru üretilmedi.' : `${next.ids.length} soru/etkinlik seçildi. Bu sekmede daha önce seçilmemiş sorular kullanıldı.`); break;
      }
      case 'ink':
        if (drawing) { penOff(); break; }
        ink.hidden = false;
        if (!pen) pen = Tahta.olustur({ kap: ink, kaydir: stage, kapat: penOff });
        pen.yukle(drawings.get(slides[state.index]?.id) || []);
        drawing = true; button('ink').setAttribute('aria-pressed', 'true'); break;
      case 'fullscreen':
        control.disabled = true;
        try {
          if (!await fullscreen.toggle()) explain('Bu cihaz tam ekranı desteklemiyor; sunum bu pencerede kullanılabilir.');
        } catch { explain('Tam ekran açılamadı; sunum bu pencerede kullanılabilir.'); }
        finally { control.disabled = false; }
        fullscreenLabel(); break;
    }
  });
  stage.addEventListener('click', () => queueMicrotask(updateReveal));
  stage.addEventListener('toggle', updateReveal, true);
  mode.addEventListener('change', () => {
    penOff(); state.mode = mode.value; state.index = 0; build(); show(0); explain();
  });
  dialog.querySelector('[data-control="slide"]').addEventListener('change', event => show(Number(event.target.value)));
  dialog.addEventListener('keydown', event => {
    if (event.key === 'Escape' && drawing) { event.preventDefault(); event.stopPropagation(); rememberInk(); penOff(); return; }
    if (event.ctrlKey || event.metaKey || event.altKey || event.target.closest('button, input, textarea, select, a, summary, [contenteditable]')) return;
    if (['ArrowRight', 'PageDown', 'ArrowLeft', 'PageUp', 'Home', 'End'].includes(event.key)) {
      event.preventDefault();
      if (['ArrowRight', 'PageDown'].includes(event.key)) { nextStep(); return; }
      show(event.key === 'Home' ? 0 : event.key === 'End' ? slides.length - 1 : state.index + (['ArrowRight', 'PageDown'].includes(event.key) ? 1 : -1));
    }
  });
})();
