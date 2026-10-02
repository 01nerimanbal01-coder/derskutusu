/* KPSS: yalnız yerel ilerleme; yanıtlar ve sonuçlar sunucuya gönderilmez. */
(() => {
  'use strict';
  const KEY = 'derskutusu-kpss-v1';
  const $ = (s, p = document) => p.querySelector(s);
  const $$ = (s, p = document) => [...p.querySelectorAll(s)];
  const warn = () => { const node = $('#kp-storage-warning'); if (node) node.hidden = false; };
  let state = { modules: {}, level: 'ortaogretim' };
  try {
    const saved = JSON.parse(localStorage.getItem(KEY));
    if (saved && typeof saved === 'object' && saved.modules && typeof saved.modules === 'object' && !Array.isArray(saved.modules)) state = saved;
  } catch (_) { warn(); }
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (_) { warn(); } };
  const guides = {
    'ortaogretim': 'https://osym.gov.tr/2026-kpss-ortaogretim-kilavuz-ve-basvuru-bilgileri',
    'on-lisans': 'https://osym.gov.tr/2026-kpss-on-lisans-kilavuz-ve-basvuru-bilgileri',
    'lisans': 'https://www.osym.gov.tr/2026kpss-lisans-kilavuz-ve-basvuru-bilgileri'
  };
  if ($('#kp-home')) {
    const level = $('#kp-level');
    level.value = Object.hasOwn(guides, state.level) ? state.level : 'ortaogretim';
    const syncGuide = () => { $('#kp-guide').href = guides[level.value]; };
    syncGuide();
    level.addEventListener('change', () => { state.level = level.value; save(); syncGuide(); });
    const cards = $$('[data-module]'); let completed = 0;
    cards.forEach(card => {
      const r = state.modules[card.dataset.module];
      if (!r || r.version !== 1) return;
      const parts = [];
      if (r.learned) parts.push('Konu çalışıldı');
      if (r.full && r.full.total === 10 && Number.isInteger(r.full.correct)) {
        completed++;
        parts.push(`Son tam test: ${r.full.correct} doğru · ${r.full.wrong} yanlış · ${r.full.blank} boş`);
      }
      if (parts.length) $('.kp-progress', card).textContent = parts.join(' — ');
    });
    $('#kp-total').textContent = `${completed} / ${cards.length} test tamamlandı`;
  }
  const root = $('[data-kp-module]'); if (!root) return;
  const mid = root.dataset.kpModule, version = Number(root.dataset.version);
  let record = state.modules[mid];
  if (!record || typeof record !== 'object' || record.version !== version) record = { version, learned: false };
  state.modules[mid] = record;
  const learned = $('#kp-learned');
  const syncLearned = () => {
    learned.setAttribute('aria-pressed', String(!!record.learned));
    learned.textContent = record.learned ? '✓ Konu çalışıldı' : 'Konuyu çalıştım';
    $('#kp-learn-status').textContent = record.learned ? 'İşareti kaldırmak için yeniden tıklayabilirsin.' : '';
  };
  syncLearned(); learned.addEventListener('click', () => { record.learned = !record.learned; save(); syncLearned(); });
  const form = $('#kp-quiz'), questionSet = $('#kp-question-set'), all = $$('.kp-question', form);
  const start = $('#kp-start'), finish = $('#kp-finish'), retry = $('#kp-retry'), reset = $('#kp-reset');
  const duration = $('#kp-duration'), timer = $('#kp-timer'), answered = $('#kp-answered'), result = $('#kp-result');
  let active = all, missed = [], running = false, ended = false, deadline = 0, interval = null;
  const stopClock = () => { if (interval !== null) clearInterval(interval); interval = null; };
  const countAnswers = () => { answered.textContent = `${active.filter(q => $('input:checked', q)).length} / ${active.length} yanıtlandı`; };
  const paragraph = text => { const p = document.createElement('p'); p.textContent = text; return p; };
  function conclude(expired = false) {
    if (!running || ended) return;
    running = false; ended = true; stopClock(); questionSet.disabled = true; finish.disabled = true;
    let correct = 0, wrong = 0, blank = 0; missed = [];
    active.forEach(q => {
      const picked = $('input:checked', q), key = Number(q.dataset.answer), answer = picked ? Number(picked.value) : null;
      const isCorrect = answer === key;
      if (isCorrect) correct++; else { missed.push(q); if (answer === null) blank++; else wrong++; }
      $$('.kp-option', q).forEach(label => {
        const value = Number($('input', label).value);
        label.classList.toggle('is-correct', value === key);
        label.classList.toggle('is-wrong', value === answer && !isCorrect);
      });
      $('.kp-verdict', q).textContent = `${isCorrect ? 'Doğru' : answer === null ? 'Boş bırakıldı' : 'Yanlış'} · Doğru cevap: ${'ABCDE'[key]}`;
      $('.kp-explanation', q).hidden = false;
    });
    const score = { correct, wrong, blank, total: active.length, date: new Date().toISOString() };
    record.last = score;
    if (active.length === all.length) record.full = score;
    record.missed = missed.map(q => q.dataset.id); save();
    result.replaceChildren();
    const h = document.createElement('h3'); h.textContent = `${correct} doğru · ${wrong} yanlış · ${blank} boş`;
    result.append(h, paragraph(`${expired ? 'Süre tamamlandı. ' : ''}${active.length} soru değerlendirildi. Açıklamalar her sorunun altında açıldı.`));
    if (missed.length) result.append(paragraph(`Tekrar konuların: ${[...new Set(missed.map(q => q.dataset.topic))].join(', ')}.`));
    else result.append(paragraph('Bu çalışmadaki bütün soruları doğru yanıtladın.'));
    result.hidden = false; retry.hidden = !missed.length; reset.hidden = false;
    timer.textContent = expired ? 'Süre bitti' : 'Tamamlandı'; result.focus();
  }
  function tick() {
    if (!running || !deadline) return;
    const seconds = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
    timer.textContent = `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`;
    if (seconds === 0) conclude(true);
  }
  function prepare(questions) {
    stopClock(); active = questions; running = false; ended = false; deadline = 0; form.reset();
    all.forEach(q => { q.hidden = !active.includes(q); $('.kp-explanation', q).hidden = true; $$('.kp-option', q).forEach(x => x.classList.remove('is-correct', 'is-wrong')); });
    questionSet.disabled = true; start.disabled = false; duration.disabled = false; finish.disabled = true;
    retry.hidden = true; reset.hidden = active.length === all.length; result.hidden = true;
    timer.textContent = 'Hazır'; countAnswers(); start.focus();
  }
  start.addEventListener('click', () => {
    if (running || ended) return;
    running = true; questionSet.disabled = false; start.disabled = true; duration.disabled = true; finish.disabled = false;
    retry.hidden = true; reset.hidden = true;
    const seconds = Number(duration.value);
    if (seconds > 0) { deadline = Date.now() + seconds * 1000; tick(); interval = setInterval(tick, 250); } else timer.textContent = 'Süresiz';
    const first = $('input', active[0]); if (first) first.focus();
  });
  form.addEventListener('submit', event => { event.preventDefault(); conclude(); });
  form.addEventListener('change', countAnswers);
  retry.addEventListener('click', () => { if (missed.length) prepare([...missed]); });
  reset.addEventListener('click', () => prepare(all));
  document.addEventListener('visibilitychange', tick);
  if (Array.isArray(record.missed)) {
    missed = all.filter(q => record.missed.includes(q.dataset.id));
    retry.hidden = !missed.length;
  }
})();
