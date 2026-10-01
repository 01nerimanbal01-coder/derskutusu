// İngilizce kelime çalışması (kelime.html): MEB İngilizce ders kitaplarının sözlük bölümündeki sözcükler.
// Kipler: Kartlar, Dinle, Test, Yaz, Eşleştir. Sesler tarayıcının kendi okuma özelliğiyle (speechSynthesis) çıkar;
// ses dosyası ya da üçüncü taraf yüklenmez. İlerleme yalnız bu tarayıcıda tutulur, hiçbir yere gönderilmez.

(() => {
  const alan = $('#k-alan');
  if (!alan) return;
  const KIPLER = [['kartlar', 'Kartlar'], ['dinle', 'Dinle'], ['test', 'Test'], ['yaz', 'Yaz'], ['eslestir', 'Eşleştir']];
  const ANAHTAR = 'dk-kelime-ogrenildi';
  const durum = { veri: null, sinif: 5, tema: 1, kip: 'kartlar' };

  // ---------- ilerleme (yalnız tarayıcıda) ----------
  let ogrenildi = {};
  try { ogrenildi = JSON.parse(localStorage.getItem(ANAHTAR) || '{}') || {}; } catch { ogrenildi = {}; }
  const kimlik = (k) => `${durum.sinif}|${k.en}`;
  const bildi = (k) => !!ogrenildi[kimlik(k)];
  const isaretle = (k, deger) => {
    if (deger) ogrenildi[kimlik(k)] = 1; else delete ogrenildi[kimlik(k)];
    try { localStorage.setItem(ANAHTAR, JSON.stringify(ogrenildi)); } catch {}
    ilerlemeGoster();
  };

  // ---------- yardımcılar ----------
  const karistir = (d) => { const a = [...d]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const temaBul = () => durum.veri.siniflar.find((s) => s.sinif === durum.sinif)?.temalar.find((t) => t.no === durum.tema);
  const kelimeler = () => temaBul()?.kelimeler || [];
  const sade = (s) => s.toLowerCase().replace(/[’‘`]/g, "'").replace(/[.!?,]/g, '').replace(/\s+/g, ' ').trim();

  const sesVar = 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
  function soyle(metin, bitince) {
    if (!sesVar) { bitince?.(); return; }
    const u = new SpeechSynthesisUtterance(metin.replace(/\//g, ', '));
    u.lang = 'en-GB'; u.rate = 0.85;
    const sesler = speechSynthesis.getVoices();
    u.voice = sesler.find((v) => v.lang === 'en-GB') || sesler.find((v) => v.lang.startsWith('en')) || null;
    if (bitince) u.onend = u.onerror = bitince;
    speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
  if (sesVar) speechSynthesis.getVoices();
  const sesDugme = (metin, etiket = 'Dinle') => sesVar
    ? el('button', { type: 'button', sinif: 'k-ses', 'aria-label': `${etiket}: ${metin}`, title: etiket, onclick: (e) => { e.stopPropagation(); soyle(metin); } }, simge('ses'), el('span', { sinif: 'gizli' }, etiket))
    : null;

  // ---------- seçim çubuğu ----------
  function adresYaz() {
    const p = new URLSearchParams({ s: durum.sinif, t: durum.tema, k: durum.kip });
    history.replaceState(null, '', `?${p}`);
  }
  function secimKur() {
    const sinifSekme = $('#k-sinif'); sinifSekme.replaceChildren();
    for (const s of durum.veri.siniflar) {
      sinifSekme.append(el('button', { type: 'button', sinif: 'sekme', 'aria-pressed': String(s.sinif === durum.sinif),
        onclick: () => { durum.sinif = s.sinif; durum.tema = s.temalar[0].no; secimKur(); ciz(); } }, `${s.sinif}. sınıf`));
    }
    const temaSec = $('#k-tema'); temaSec.replaceChildren();
    for (const t of durum.veri.siniflar.find((s) => s.sinif === durum.sinif).temalar) {
      temaSec.append(el('option', { value: t.no, selected: t.no === durum.tema }, `Theme ${t.no} · ${t.ad} (${t.kelimeler.length})`));
    }
    temaSec.onchange = () => { durum.tema = Number(temaSec.value); ciz(); };
    const kip = $('#k-kipler'); kip.replaceChildren();
    for (const [ad, yazi] of KIPLER) {
      kip.append(el('button', { type: 'button', sinif: 'sekme', 'aria-pressed': String(ad === durum.kip),
        onclick: () => { durum.kip = ad; secimKur(); ciz(); } }, yazi));
    }
  }
  function ilerlemeGoster() {
    const k = kelimeler(); const n = k.filter(bildi).length;
    $('#k-ilerleme-sayi').textContent = `${n} / ${k.length}`;
    $('#k-ilerleme-cubuk').style.width = `${k.length ? (100 * n / k.length) : 0}%`;
  }

  // ---------- Kartlar ----------
  function kartlar() {
    let yalnizYeni = false, sira = 0, liste = [];
    const kutu = el('div', { sinif: 'k-kart-kap' });
    const yeniKutu = el('input', { type: 'checkbox', onchange: (e) => { yalnizYeni = e.target.checked; kur(); } });
    alan.append(el('label', { sinif: 'k-secenek' }, yeniKutu, ' Yalnız öğrenmediğim kelimeler'), kutu);
    function kur() { liste = karistir(kelimeler().filter((k) => !yalnizYeni || !bildi(k))); sira = 0; goster(); }
    function goster() {
      kutu.replaceChildren();
      if (!liste.length) { kutu.append(el('p', { sinif: 'k-bos' }, 'Bu temadaki bütün kelimeleri öğrendin. Tebrikler!')); return; }
      if (sira >= liste.length) {
        kutu.append(el('div', { sinif: 'k-bitti' }, el('p', {}, `${liste.length} kartın hepsine baktın.`),
          el('button', { type: 'button', sinif: 'dugme ana', onclick: kur }, 'Kartları karıştır, yeniden başla')));
        return;
      }
      const k = liste[sira];
      const kart = el('button', { type: 'button', sinif: 'k-kart', 'aria-label': `${k.en}. Çevirmek için dokun.`,
        onclick: () => { kart.classList.toggle('cevrik'); kart.setAttribute('aria-label', kart.classList.contains('cevrik') ? `${k.en}: ${k.tr}` : `${k.en}. Çevirmek için dokun.`); } },
        el('span', { sinif: 'k-yuz on' }, el('b', {}, k.en), k.tur ? el('small', {}, k.tur) : null, el('em', {}, 'Türkçesi için dokun')),
        el('span', { sinif: 'k-yuz arka' }, el('b', {}, k.tr), el('small', {}, k.en)));
      kutu.append(
        el('p', { sinif: 'k-sira' }, `${sira + 1} / ${liste.length}`, bildi(k) ? el('span', { sinif: 'k-rozet' }, 'Öğrendin') : null),
        el('div', { sinif: 'k-kart-satir' }, kart, sesDugme(k.en)),
        el('div', { sinif: 'k-dugmeler' },
          el('button', { type: 'button', sinif: 'dugme', onclick: () => { sira++; goster(); } }, 'Tekrar edeceğim'),
          el('button', { type: 'button', sinif: 'dugme ana', onclick: () => { isaretle(k, true); sira++; goster(); } }, 'Biliyorum')));
    }
    kur();
  }

  // ---------- Dinle ----------
  function dinle() {
    if (!sesVar) alan.append(el('p', { sinif: 'k-uyari' }, 'Tarayıcınız sesli okumayı desteklemiyor. Kelimeleri yine de listeden çalışabilirsiniz.'));
    let calisiyor = false;
    const liste = el('ol', { sinif: 'k-liste' });
    const tum = el('button', { type: 'button', sinif: 'dugme ana', hidden: !sesVar, onclick: () => {
      if (calisiyor) { calisiyor = false; speechSynthesis.cancel(); tum.textContent = 'Hepsini sırayla dinle'; return; }
      calisiyor = true; tum.textContent = 'Durdur';
      const satirlar = $$('li', liste); let i = 0;
      const sonraki = () => {
        satirlar.forEach((s) => s.classList.remove('okunuyor'));
        if (!calisiyor || i >= satirlar.length) { calisiyor = false; tum.textContent = 'Hepsini sırayla dinle'; return; }
        const s = satirlar[i++]; s.classList.add('okunuyor'); s.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        soyle(s.dataset.en, () => setTimeout(sonraki, 900));
      };
      sonraki();
    } }, 'Hepsini sırayla dinle');
    for (const k of kelimeler()) {
      liste.append(el('li', { 'data-en': k.en, sinif: bildi(k) ? 'bildi' : null }, sesDugme(k.en), el('b', {}, k.en), el('span', {}, k.tr), k.tur ? el('small', {}, k.tur) : null));
    }
    alan.append(el('div', { sinif: 'k-dugmeler sol' }, tum), liste);
  }

  // ---------- Test ----------
  function test() {
    let yon = 'en-tr';
    const yonSec = el('div', { sinif: 'sekmeler', role: 'group', 'aria-label': 'Soru yönü' });
    const kutu = el('div', {});
    alan.append(yonSec, kutu);
    function yonKur() {
      yonSec.replaceChildren(...[['en-tr', 'İngilizce → Türkçe'], ['tr-en', 'Türkçe → İngilizce']].map(([a, y]) =>
        el('button', { type: 'button', sinif: 'sekme', 'aria-pressed': String(a === yon), onclick: () => { yon = a; yonKur(); kur(); } }, y)));
    }
    function kur() {
      const tumu = kelimeler(); const sorular = karistir(tumu).slice(0, Math.min(10, tumu.length));
      let puan = 0, cevaplanan = 0;
      const sonuc = el('p', { sinif: 'etk-puan' });
      const yaz = () => { sonuc.replaceChildren('Puan: ', el('b', {}, String(puan)), ` / ${sorular.length}`); };
      yaz();
      const ol = el('ol', { sinif: 'etk-liste' });
      sorular.forEach((k, i) => {
        const ayni = tumu.filter((x) => x !== k && x.tr !== k.tr && x.en !== k.en);
        const tercihli = karistir(ayni.filter((x) => k.tur && x.tur === k.tur));
        const celdirici = [...tercihli, ...karistir(ayni)].filter((x, j, a) => a.indexOf(x) === j).slice(0, 3);
        const secenekler = karistir([k, ...celdirici]);
        const gor = (x) => (yon === 'en-tr' ? x.tr : x.en);
        const li = el('li', { sinif: 'etk etk-coktan' });
        const geri = el('p', { sinif: 'etk-geri', hidden: true, role: 'status' });
        const harfler = 'ABCD';
        const dugmeler = secenekler.map((x, j) => el('button', { type: 'button', sinif: 'etk-sec', onclick: () => {
          if (li.classList.contains('bitti')) return;
          li.classList.add('bitti'); cevaplanan++;
          dugmeler.forEach((d) => d.setAttribute('aria-disabled', 'true'));
          dugmeler[secenekler.indexOf(k)].classList.add('dogru');
          if (x === k) { puan++; geri.className = 'etk-geri dogru'; geri.replaceChildren(el('b', {}, 'Doğru!'), el('span', {}, `${k.en} = ${k.tr}`)); }
          else { dugmeler[j].classList.add('yanlis'); geri.className = 'etk-geri yanlis'; geri.replaceChildren(el('b', {}, 'Yanlış.'), el('span', {}, `Doğrusu: ${k.en} = ${k.tr}`)); }
          geri.hidden = false; yaz();
          if (yon === 'tr-en' || x === k) soyle(k.en);
          if (cevaplanan === sorular.length) bitis();
        } }, el('span', { sinif: 'etk-harf' }, harfler[j]), gor(x)));
        li.append(el('p', { sinif: 'etk-soru' }, el('span', { sinif: 'etk-no' }, String(i + 1)),
          el('span', {}, yon === 'en-tr' ? `"${k.en}" sözcüğünün Türkçesi hangisidir?` : `"${k.tr}" anlamına gelen İngilizce sözcük hangisidir?`)),
          yon === 'en-tr' ? el('div', { sinif: 'k-soru-ses' }, sesDugme(k.en)) : null,
          el('div', { sinif: 'etk-secenekler' }, dugmeler), geri);
        ol.append(li);
      });
      function bitis() {
        kutu.append(el('div', { sinif: 'k-bitti' }, el('p', {}, `Test bitti: ${sorular.length} sorudan ${puan} doğru.`),
          el('button', { type: 'button', sinif: 'dugme ana', onclick: kur }, 'Yeni test')));
      }
      kutu.replaceChildren(el('div', { sinif: 'etk-bas' }, el('h2', {}, `${sorular.length} soruluk test`), sonuc), ol);
    }
    yonKur(); kur();
  }

  // ---------- Yaz ----------
  function yaz() {
    const kutu = el('div', {});
    alan.append(kutu);
    function kur() {
      const sorular = karistir(kelimeler()).slice(0, 10);
      let i = 0, dogru = 0;
      const goster = () => {
        if (i >= sorular.length) {
          kutu.replaceChildren(el('div', { sinif: 'k-bitti' }, el('p', {}, `${sorular.length} kelimeden ${dogru} tanesini doğru yazdın.`),
            el('button', { type: 'button', sinif: 'dugme ana', onclick: kur }, 'Yeni 10 kelime')));
          return;
        }
        const k = sorular[i]; let ipucu = 0, bitti = false;
        const girdi = el('input', { type: 'text', sinif: 'k-girdi', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', lang: 'en', 'aria-label': 'İngilizcesi' });
        const geri = el('p', { sinif: 'etk-geri', hidden: true, role: 'status' });
        const ipucuYaz = el('p', { sinif: 'k-ipucu', 'aria-live': 'polite' });
        const kontrol = () => {
          if (bitti) { i++; goster(); return; }
          if (!girdi.value.trim()) { girdi.focus(); return; }
          bitti = true; girdi.readOnly = true;
          if (sade(girdi.value) === sade(k.en)) { dogru++; isaretle(k, true); geri.className = 'etk-geri dogru'; geri.replaceChildren(el('b', {}, 'Doğru!'), el('span', {}, k.en)); }
          else { geri.className = 'etk-geri yanlis'; geri.replaceChildren(el('b', {}, 'Doğrusu:'), el('span', {}, k.en)); }
          geri.hidden = false; soyle(k.en); dugme.textContent = 'Sonraki kelime'; dugme.focus();
        };
        const dugme = el('button', { type: 'submit', sinif: 'dugme ana' }, 'Kontrol et');
        kutu.replaceChildren(
          el('p', { sinif: 'k-sira' }, `${i + 1} / ${sorular.length}`),
          el('form', { sinif: 'k-yaz', onsubmit: (e) => { e.preventDefault(); kontrol(); } },
            el('p', { sinif: 'k-yaz-tr' }, el('b', {}, k.tr), k.tur ? el('small', {}, k.tur) : null),
            el('label', {}, 'İngilizcesini yazın', girdi), ipucuYaz, geri,
            el('div', { sinif: 'k-dugmeler sol' }, dugme,
              el('button', { type: 'button', sinif: 'dugme', onclick: () => {
                if (bitti) return; ipucu = Math.min(ipucu + 1, k.en.length);
                ipucuYaz.textContent = `İpucu: ${k.en.slice(0, ipucu)}${'_'.repeat(Math.max(0, k.en.length - ipucu)).replace(/_/g, ' _')}`;
                girdi.focus();
              } }, 'Harf ipucu'),
              sesVar ? el('button', { type: 'button', sinif: 'dugme', onclick: () => { soyle(k.en); girdi.focus(); } }, simge('ses'), 'Dinle') : null)));
        girdi.focus({ preventScroll: true });
      };
      goster();
    }
    kur();
  }

  // ---------- Eşleştir ----------
  function eslestir() {
    const kutu = el('div', {});
    alan.append(kutu);
    function kur() {
      const tumu = karistir(kelimeler());
      const tur = [];
      for (const k of tumu) if (!tur.some((x) => x.tr === k.tr || x.en === k.en) && tur.length < 6) tur.push(k);
      let secili = null, kalan = tur.length, hata = 0;
      const sol = el('div', { sinif: 'etk-sutun' }), sag = el('div', { sinif: 'etk-sutun' });
      const durumYaz = el('p', { sinif: 'etk-puan', role: 'status' }, 'İngilizce sözcüğü, sonra Türkçesini seçin.');
      const sec = (d, k, taraf) => {
        if (d.classList.contains('esli')) return;
        if (!secili || secili.taraf === taraf) {
          if (secili) secili.d.classList.remove('secili');
          secili = { d, k, taraf }; d.classList.add('secili'); if (taraf === 'en') soyle(k.en); return;
        }
        const [a, b] = [secili, { d, k, taraf }]; secili = null; a.d.classList.remove('secili');
        if (a.k === b.k) {
          for (const x of [a.d, b.d]) { x.classList.add('esli', 'dogru'); x.setAttribute('aria-disabled', 'true'); }
          kalan--; isaretle(a.k, true);
          if (!kalan) {
            durumYaz.textContent = hata ? `Bitti! ${hata} yanlış denemeyle eşleştirdin.` : 'Bitti! Hiç yanlış yapmadın.';
            kutu.append(el('div', { sinif: 'k-bitti' }, el('button', { type: 'button', sinif: 'dugme ana', onclick: kur }, 'Yeni eşleştirme')));
          }
        } else {
          hata++;
          for (const x of [a.d, b.d]) { x.classList.add('yanlis'); setTimeout(() => x.classList.remove('yanlis'), 700); }
        }
      };
      for (const k of tur) sol.append(el('button', { type: 'button', sinif: 'etk-sec', lang: 'en', onclick: (e) => sec(e.currentTarget, k, 'en') }, k.en));
      for (const k of karistir(tur)) sag.append(el('button', { type: 'button', sinif: 'etk-sec', onclick: (e) => sec(e.currentTarget, k, 'tr') }, k.tr));
      kutu.replaceChildren(durumYaz, el('div', { sinif: 'etk etk-eslestir' }, el('div', { sinif: 'etk-sutunlar' }, sol, sag)));
    }
    kur();
  }

  const CIZ = { kartlar, dinle, test, yaz, eslestir };
  function ciz() {
    if (sesVar) speechSynthesis.cancel();
    alan.replaceChildren();
    adresYaz(); ilerlemeGoster();
    const t = temaBul();
    $('#k-tema-baslik').textContent = t ? `${durum.sinif}. sınıf · Theme ${t.no}: ${t.ad}` : '';
    CIZ[durum.kip]();
  }

  veri('kelimeler.json').then((v) => {
    if (!v) { alan.replaceChildren(el('p', { sinif: 'k-uyari' }, 'Kelimeler yüklenemedi. Sayfayı yenileyin.')); return; }
    durum.veri = v;
    const p = new URLSearchParams(location.search);
    const s = v.siniflar.find((x) => x.sinif === Number(p.get('s'))) || v.siniflar[0];
    durum.sinif = s.sinif;
    durum.tema = (s.temalar.find((t) => t.no === Number(p.get('t'))) || s.temalar[0]).no;
    if (CIZ[p.get('k')]) durum.kip = p.get('k');
    secimKur(); ciz();
    $('#k-sifirla').onclick = () => {
      if (!confirm('Bu temadaki "öğrendim" işaretleri silinsin mi?')) return;
      for (const k of kelimeler()) delete ogrenildi[kimlik(k)];
      try { localStorage.setItem(ANAHTAR, JSON.stringify(ogrenildi)); } catch {}
      ciz();
    };
  });
})();
