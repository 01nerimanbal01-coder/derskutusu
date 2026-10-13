// Çevrimiçi test (kullanıcı 13.10.2026: "öğrenci modülüne online soru havuzu; her konuya ve çıktıya özel sorular otomatik seçilsin").
// Soru havuzu: veri/soru/<sinif>-<ders>.json (araclar/soru_havuzu_uret.py üretir), dizin: veri/soru/dizin.json.
// Sunucuya hiçbir şey gönderilmez: seçimler, görülen sorular ve sonuçlar yalnız bu tarayıcıda (localStorage) tutulur.
(() => {
  'use strict';
  const P = new URLSearchParams(location.search);
  const TUR_AD = { coktan: 'Çoktan seçmeli', dy: 'Doğru / yanlış', bosluk: 'Boşluk doldurma', eslestir: 'Eşleştirme', siralama: 'Sıralama', acik: 'Açık uçlu (kendini sına)' };
  const OTOMATIK = ['coktan', 'dy', 'bosluk', 'eslestir', 'siralama'];
  const HARF = 'ABCDEF';
  const depo = {
    al: (a, varsayilan) => { try { const v = localStorage.getItem(a); return v == null ? varsayilan : JSON.parse(v); } catch { return varsayilan; } },
    koy: (a, v) => { try { localStorage.setItem(a, JSON.stringify(v)); } catch { /* gizli pencere */ } },
  };
  const html = (etiket, sinif, icerik) => { const n = document.createElement(etiket); if (sinif) n.className = sinif; if (icerik != null) n.innerHTML = icerik; return n; };
  const karistir = (dizi) => { const d = [...dizi]; for (let i = d.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [d[i], d[j]] = [d[j], d[i]]; } return d; };
  const sayi = (n, ad) => `${n} ${ad}`;

  const kurulum = document.getElementById('t-kurulum'), testAlan = document.getElementById('t-test'), sonucAlan = document.getElementById('t-sonuc'), gecmisAlan = document.getElementById('t-gecmis');
  if (!kurulum) return;
  const alan = { sinif: $('#t-sinif'), ders: $('#t-ders'), konu: $('#t-konu'), cikti: $('#t-cikti'), adet: $('#t-adet'), donut: $('#t-donut') };
  const turKutular = () => $$('#t-kurulum [name="tur"]');
  const havuzYazi = $('#t-havuz'), basla = $('#t-basla');
  let dizin = null, ders = null, dersAnahtar = '';
  const havuzOnbellek = new Map();

  // ---------------------------------------------------------------- kurulum
  function secenekDoldur(select, liste, ilk) {
    const onceki = select.value;
    select.replaceChildren(...(ilk ? [el('option', { value: '' }, ilk)] : []), ...liste.map(([v, t, ek]) => el('option', { value: v, ...(ek || {}) }, t)));
    if ([...select.options].some((o) => o.value === onceki)) select.value = onceki;
  }
  async function dersYukle() {
    dersAnahtar = `${alan.sinif.value}-${alan.ders.value}`;
    if (!dizin?.dersler?.[dersAnahtar]) { ders = null; konuDoldur(); return; }
    if (!havuzOnbellek.has(dersAnahtar)) havuzOnbellek.set(dersAnahtar, veri(`soru/${dersAnahtar}.json`));
    const yuklenen = await havuzOnbellek.get(dersAnahtar);
    if (`${alan.sinif.value}-${alan.ders.value}` !== dersAnahtar) return;   // bu arada seçim değişti
    ders = yuklenen; konuDoldur();
  }
  function konuDoldur() {
    const istenen = alan.konu.value || P.get('konu') || '';
    alan.konu.replaceChildren(el('option', { value: '' }, 'Dersin tamamı'));
    if (ders) {
      for (const u of ders.uniteler) {
        if (!u.n) continue;
        const grup = el('optgroup', { label: `${u.ad} (${u.n})` });
        if (u.konular.length > 1) grup.append(el('option', { value: `u:${u.ad}` }, `Ünitenin tamamı (${u.n} soru)`));
        for (const k of u.konular) if (k.n) grup.append(el('option', { value: k.kod }, `${k.ad} (${k.n})`));
        alan.konu.append(grup);
      }
    }
    if ([...alan.konu.options].some((o) => o.value === istenen)) alan.konu.value = istenen;
    ciktiDoldur();
  }
  const konuSuz = (s) => {
    const k = alan.konu.value;
    if (!k) return true;
    if (k.startsWith('u:')) { const u = ders.uniteler.find((x) => x.ad === k.slice(2)); return Boolean(u && u.konular.some((x) => x.kod === s.konu)); }
    return s.konu === k;
  };
  function ciktiDoldur() {
    const istenen = alan.cikti.value || P.get('cikti') || '';
    alan.cikti.replaceChildren(el('option', { value: '' }, 'Bütün çıktılar'));
    if (ders) {
      const sayilar = new Map();
      for (const s of ders.sorular) if (konuSuz(s)) for (const c of s.cikti) sayilar.set(c, (sayilar.get(c) || 0) + 1);
      for (const c of ders.ciktilar) if (sayilar.get(c.kod)) alan.cikti.append(el('option', { value: c.kod, title: c.ifade }, `${c.kod} · ${c.ifade.length > 70 ? c.ifade.slice(0, 68) + '…' : c.ifade} (${sayilar.get(c.kod)})`));
    }
    if ([...alan.cikti.options].some((o) => o.value === istenen)) alan.cikti.value = istenen;
    P.delete('konu'); P.delete('cikti');
    havuzGuncelle();
  }
  const secilenTurler = () => turKutular().filter((k) => k.checked).map((k) => k.value);
  function havuz() {
    if (!ders) return [];
    const turler = new Set(secilenTurler()), cikti = alan.cikti.value;
    return ders.sorular.filter((s) => turler.has(s.tur) && konuSuz(s) && (!cikti || s.cikti.includes(cikti)));
  }
  function havuzGuncelle() {
    const h = havuz(), oto = h.filter((s) => s.tur !== 'acik').length;
    if (!ders) { havuzYazi.textContent = dizin ? 'Bu ders için henüz soru yok. Başka bir ders seçin.' : ''; basla.disabled = true; return; }
    havuzYazi.textContent = h.length ? `Havuzda ${sayi(h.length, 'soru')} (${oto} otomatik puanlanan${h.length - oto ? `, ${h.length - oto} açık uçlu` : ''}).` : 'Bu seçimde soru yok; konuyu ya da soru türlerini genişletin.';
    basla.disabled = !h.length;
  }
  function kapsamMetni() {
    const parca = [`${ders.sinif}. sınıf ${ders.dersAd}`];
    const k = alan.konu.value;
    if (k.startsWith('u:')) parca.push(k.slice(2));
    else if (k) { const kk = ders.uniteler.flatMap((u) => u.konular).find((x) => x.kod === k); if (kk) parca.push(kk.ad); }
    if (alan.cikti.value) parca.push(alan.cikti.value);
    return parca.join(' · ');
  }

  // ---------------------------------------------------------------- test oturumu
  let oturum = null;   // { anahtar, kapsam, donut, sorular: [...], cevaplar: [...], no, baslangic, bitti }
  const OTURUM = 'test-oturum';
  function secimYap(h, adet) {
    const gorulen = new Set(depo.al(`test-gorulen:${dersAnahtar}`, []));
    const yeni = karistir(h.filter((s) => !gorulen.has(s.id))), eski = karistir(h.filter((s) => gorulen.has(s.id)));
    const secilen = [...yeni, ...eski].slice(0, adet || h.length);
    // Türler karışık gelsin: aynı türden sorular art arda yığılmasın
    const sirali = [], kalan = [...secilen];
    while (kalan.length) { const son = sirali[sirali.length - 1]; const i = Math.max(0, kalan.findIndex((s) => !son || s.tur !== son.tur)); sirali.push(kalan.splice(i, 1)[0]); }
    const tum = [...gorulen, ...sirali.map((s) => s.id)];
    depo.koy(`test-gorulen:${dersAnahtar}`, tum.slice(-Math.max(200, Math.floor(h.length * 0.8))));
    return sirali.map(hazirla);
  }
  // Seçenekler, sağ sütun ve sıralama ögeleri her testte yeniden karıştırılır; doğru cevap izlenir.
  function hazirla(s) {
    const q = { ...s };
    if (s.tur === 'coktan') { const sira = karistir(s.secenekler.map((_, i) => i)); q.secenekler = sira.map((i) => s.secenekler[i]); q.dogru = sira.indexOf(s.dogru); }
    if (s.tur === 'eslestir') q.sag = karistir(s.ciftler.map((_, i) => i));
    if (s.tur === 'siralama') { let sira; do { sira = karistir(s.ogeler.map((_, i) => i)); } while (s.ogeler.length > 2 && sira.every((v, i) => v === i)); q.sira = sira; }
    if (s.tur === 'bosluk') q.kelimeler = karistir([...s.cumleler.map((c) => c.cevap), ...(s.fazla || [])]);
    return q;
  }
  function oturumBaslat(sorular, kapsam, donut) {
    oturum = { anahtar: dersAnahtar, sinif: ders.sinif, ders: ders.ders, dersAd: ders.dersAd, kapsam, donut, sorular, cevaplar: sorular.map(() => null), no: 0, baslangic: Date.now(), bitti: false };
    kaydet(); goster('test'); soruGoster();
  }
  const kaydet = () => { try { sessionStorage.setItem(OTURUM, JSON.stringify(oturum)); } catch { /* bellek yok */ } };
  function goster(hangi) {
    kurulum.hidden = hangi !== 'kurulum'; gecmisAlan.hidden = hangi !== 'kurulum' || !gecmisAlan.querySelector('li');
    testAlan.hidden = hangi !== 'test'; sonucAlan.hidden = hangi !== 'sonuc';
    document.body.classList.toggle('test-acik', hangi === 'test');
    window.scrollTo({ top: 0, behavior: 'instant' });
  }

  // ---------------------------------------------------------------- soru ekranı
  function soruGoster() {
    const q = oturum.sorular[oturum.no], c = oturum.cevaplar[oturum.no], anlik = oturum.donut === 'aninda';
    const konuAd = ders?.uniteler.flatMap((u) => u.konular).find((k) => k.kod === q.konu)?.ad || '';
    const kart = html('div', `etk t-soru t-${q.tur}`);
    kart.setAttribute('role', 'group'); kart.setAttribute('aria-labelledby', 't-soru-baslik');
    const bas = el('div', { sinif: 't-soru-bas' },
      el('span', { sinif: 't-soru-no' }, `${oturum.no + 1}`),
      el('div', {}, el('p', { sinif: 't-soru-tur' }, [TUR_AD[q.tur], konuAd].filter(Boolean).join(' · ')),
        html('h2', 't-soru-metin', q.soru)));
    bas.querySelector('h2').id = 't-soru-baslik';
    kart.append(bas);
    const geri = el('p', { sinif: 'etk-geri', hidden: true, role: 'status' }, el('b', {}), el('span', {}));
    const kontrol = { kart, geri, q, c, anlik };
    ({ coktan: coktanCiz, dy: dyCiz, bosluk: boslukCiz, eslestir: eslestirCiz, siralama: siralamaCiz, acik: acikCiz })[q.tur](kontrol);
    kart.append(geri);
    const ilerleme = el('div', { sinif: 't-ilerleme' },
      el('p', { sinif: 't-ilerleme-yazi', role: 'status' }, `Soru ${oturum.no + 1} / ${oturum.sorular.length}`, el('small', {}, ` · ${oturum.kapsam}`)),
      el('progress', { max: oturum.sorular.length, value: oturum.no + 1, 'aria-label': 'Test ilerlemesi' }));
    const ileriMetin = oturum.no < oturum.sorular.length - 1 ? 'Sonraki soru →' : 'Testi bitir';
    const dugmeler = el('div', { sinif: 't-dugmeler' },
      el('button', { sinif: 'dugme', type: 'button', id: 't-onceki', disabled: oturum.no === 0 || anlik, onclick: () => git(oturum.no - 1) }, '← Önceki'),
      el('button', { sinif: 'dugme', type: 'button', id: 't-bitir', onclick: bitirSor }, 'Testi bitir'),
      el('button', { sinif: 'dugme ana', type: 'button', id: 't-sonraki', onclick: () => (oturum.no < oturum.sorular.length - 1 ? git(oturum.no + 1) : bitir()) }, ileriMetin));
    testAlan.replaceChildren(ilerleme, kart, dugmeler);
    if (anlik && c == null) dugmeler.querySelector('#t-sonraki').disabled = true;   // önce cevapla
    kart.querySelector('h2').setAttribute('tabindex', '-1'); kart.querySelector('h2').focus({ preventScroll: true });
  }
  function git(no) { oturum.no = Math.max(0, Math.min(no, oturum.sorular.length - 1)); kaydet(); soruGoster(); }
  // Cevabı kaydet; anında dönütte hemen değerlendir. c = { secim, dogru (bool|null), parca: [dogru, toplam] }
  function cevapla(kontrol, c) {
    oturum.cevaplar[oturum.no] = c; kaydet();
    cevapGoster(kontrol, c);
    const sonraki = testAlan.querySelector('#t-sonraki'); if (sonraki) sonraki.disabled = false;
  }
  // Anında dönütte ya da test bittiğinde doğru/yanlış işaretlenir; "sonunda" modunda yalnız seçim görünür
  function cevapGoster(kontrol, c) {
    const { kart, geri, q, anlik } = kontrol;
    if (!anlik && !oturum.bitti) { if (q.tur === 'coktan') kart.querySelector(`.etk-sec[data-i="${c.secim}"]`)?.classList.add('secili'); return; }
    kontrol.isaretle?.(c);
    kart.classList.add('bitti');
    kart.querySelectorAll('.etk-sec, .etk-dy-dugmeler button, .etk-kelime, .etk-bosluk-yer, .t-sira-dugme, .etk-kontrol').forEach((b) => { b.setAttribute('aria-disabled', 'true'); b.disabled = true; });
    const ok = c.dogru === true;
    geri.hidden = false; geri.className = `etk-geri ${ok ? 'dogru' : c.dogru === false ? 'yanlis' : 'notr'}`;
    geri.firstElementChild.textContent = ok ? 'Doğru!' : c.dogru === false ? (c.parca && c.parca[0] ? `${c.parca[0]} / ${c.parca[1]} doğru.` : 'Yanlış.') : '';
    geri.lastElementChild.innerHTML = c.aciklama || '';
  }

  function coktanCiz(k) {
    const { kart, q } = k;
    const kutu = el('div', { sinif: 'etk-secenekler' });
    q.secenekler.forEach((s, i) => {
      const b = el('button', { sinif: 'etk-sec', type: 'button', 'data-i': String(i) }, el('span', { sinif: 'etk-harf', 'aria-hidden': 'true' }, HARF[i]), html('span', '', s));
      b.addEventListener('click', () => {
        if (kart.classList.contains('bitti')) return;
        kutu.querySelectorAll('.etk-sec').forEach((x) => x.classList.remove('secili')); b.classList.add('secili');
        cevapla(k, { secim: i, dogru: i === q.dogru, aciklama: q.aciklama });
      });
      kutu.append(b);
    });
    kart.append(kutu);
    k.isaretle = (c) => { kutu.querySelector(`.etk-sec[data-i="${c.secim}"]`)?.classList.add(c.dogru ? 'dogru' : 'yanlis'); kutu.querySelector(`.etk-sec[data-i="${q.dogru}"]`)?.classList.add('dogru'); };
    sonrasi(k);
  }
  function dyCiz(k) {
    const { kart, q, c } = k;
    const secim = c?.secim ? [...c.secim] : q.ifadeler.map(() => null);
    const liste = el('ul', { sinif: 'etk-dy-liste' });
    q.ifadeler.forEach((f, i) => {
      const satir = el('li', { sinif: 'etk-dy-satir', 'data-i': String(i) }, html('span', 'etk-dy-metin', f.metin),
        el('span', { sinif: 'etk-dy-dugmeler' }, ...[['D', 'Doğru'], ['Y', 'Yanlış']].map(([v, ad]) => el('button', { type: 'button', 'data-c': v, 'aria-pressed': String(secim[i] === v), onclick: (o) => {
          if (kart.classList.contains('bitti')) return;
          secim[i] = v; satir.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === o.currentTarget)));
          if (secim.every((x) => x)) cevapla(k, degerlendirDy(q, secim)); else { oturum.cevaplar[oturum.no] = null; kaydet(); }
        } }, ad))));
      liste.append(satir);
    });
    kart.append(liste);
    k.isaretle = (c) => q.ifadeler.forEach((f, i) => {
      const satir = liste.querySelector(`[data-i="${i}"]`), dogruC = f.dogru ? 'D' : 'Y';
      satir.querySelector(`button[data-c="${c.secim[i]}"]`)?.classList.add(c.secim[i] === dogruC ? 'dogru' : 'yanlis');
      satir.querySelector(`button[data-c="${dogruC}"]`).classList.add('dogru');
      if (f.aciklama && c.secim[i] !== dogruC) satir.append(html('small', 'etk-duzelt', f.aciklama));
    });
    sonrasi(k);
  }
  const degerlendirDy = (q, secim) => { const d = q.ifadeler.filter((f, i) => secim[i] === (f.dogru ? 'D' : 'Y')).length; return { secim, dogru: d === q.ifadeler.length, parca: [d, q.ifadeler.length] }; };
  function boslukCiz(k) {
    const { kart, q, c } = k;
    const dolu = c?.secim ? [...c.secim] : q.cumleler.map(() => null);
    let hedef = null;
    const kelimeler = el('div', { sinif: 'etk-kelimeler', role: 'group', 'aria-label': 'Kelimeler' }, ...q.kelimeler.map((w, i) => el('button', { sinif: 'etk-kelime', type: 'button', 'data-k': String(i), hidden: dolu.includes(i) || null }, w)));
    const cumleler = el('ol', { sinif: 'etk-cumleler' }, ...q.cumleler.map((cm, i) => {
      const [on, arka] = cm.metin.split('___');
      const yer = el('button', { sinif: 'etk-bosluk-yer', type: 'button', 'data-i': String(i), 'aria-label': `Boşluk ${i + 1}` }, dolu[i] != null ? q.kelimeler[dolu[i]] : '');
      const li = el('li', {}); li.append(html('span', '', on || ''), yer, html('span', '', arka || '')); return li;
    }));
    const yerler = () => [...cumleler.querySelectorAll('.etk-bosluk-yer')];
    const sec = (y) => { yerler().forEach((x) => x.classList.toggle('secili', x === y)); hedef = y; };
    const guncelle = () => { if (dolu.every((x) => x != null)) cevapla(k, degerlendirBosluk(q, dolu)); else { oturum.cevaplar[oturum.no] = null; kaydet(); const s = testAlan.querySelector('#t-sonraki'); if (s && k.anlik) s.disabled = true; } };
    cumleler.addEventListener('click', (o) => {
      const y = o.target.closest('.etk-bosluk-yer'); if (!y || kart.classList.contains('bitti')) return;
      const i = Number(y.dataset.i);
      if (dolu[i] != null) { kelimeler.querySelector(`[data-k="${dolu[i]}"]`).hidden = false; dolu[i] = null; y.textContent = ''; }
      sec(y); guncelle();
    });
    kelimeler.addEventListener('click', (o) => {
      const w = o.target.closest('.etk-kelime'); if (!w || kart.classList.contains('bitti')) return;
      const bos = yerler().find((y) => dolu[Number(y.dataset.i)] == null);
      const y = hedef && dolu[Number(hedef.dataset.i)] == null ? hedef : bos; if (!y) return;
      dolu[Number(y.dataset.i)] = Number(w.dataset.k); y.textContent = w.textContent; w.hidden = true;
      sec(yerler().find((x) => dolu[Number(x.dataset.i)] == null) || null); guncelle();
    });
    kart.append(kelimeler, cumleler);
    k.isaretle = (c) => yerler().forEach((y, i) => {
      const ok = c.secim[i] != null && q.kelimeler[c.secim[i]] === q.cumleler[i].cevap;
      y.classList.add(ok ? 'dogru' : 'yanlis'); if (!ok) y.insertAdjacentElement('afterend', html('small', 'etk-duzelt', q.cumleler[i].cevap));
    });
    sonrasi(k);
  }
  const degerlendirBosluk = (q, dolu) => { const d = q.cumleler.filter((cm, i) => dolu[i] != null && q.kelimeler[dolu[i]] === cm.cevap).length; return { secim: dolu, dogru: d === q.cumleler.length, parca: [d, q.cumleler.length] }; };
  function eslestirCiz(k) {
    const { kart, q, c } = k;
    const esler = c?.secim ? { ...c.secim } : {};   // sol i → sağ j
    let secili = null, renk = 0; const hatalar = new Set(c?.hatalar || []);
    const sol = el('div', { sinif: 'etk-sutun' }, ...q.ciftler.map((cf, i) => el('button', { sinif: 'etk-sec', type: 'button', 'data-sol': String(i) }, html('span', '', cf[0]))));
    const sag = el('div', { sinif: 'etk-sutun' }, ...q.sag.map((j) => el('button', { sinif: 'etk-sec', type: 'button', 'data-sag': String(j) }, html('span', '', q.ciftler[j][1]))));
    const sutunlar = el('div', { sinif: 'etk-sutunlar' }, sol, sag);
    const boya = () => { renk = 0; for (const [i, j] of Object.entries(esler)) { renk = (renk % 5) + 1; for (const x of [sol.querySelector(`[data-sol="${i}"]`), sag.querySelector(`[data-sag="${j}"]`)]) { x.classList.add('esli', `r${renk}`); } } };
    boya();
    const kayit = () => {
      const tam = Object.keys(esler).length === q.ciftler.length;
      const dogruSay = q.ciftler.filter((_, i) => esler[i] === i && !hatalar.has(i)).length;
      if (tam) cevapla(k, { secim: esler, hatalar: [...hatalar], dogru: hatalar.size === 0, parca: [dogruSay, q.ciftler.length] });
    };
    sutunlar.addEventListener('click', (o) => {
      const b = o.target.closest('.etk-sec'); if (!b || kart.classList.contains('bitti') || b.classList.contains('esli')) return;
      if (!secili || secili === b || ('sol' in secili.dataset) === ('sol' in b.dataset)) {
        secili?.classList.remove('secili'); secili = secili === b ? null : b; secili?.classList.add('secili'); return;
      }
      const s = 'sol' in b.dataset ? b : secili, d = s === b ? secili : b; secili.classList.remove('secili'); secili = null;
      if (s.dataset.sol === d.dataset.sag) { esler[s.dataset.sol] = Number(d.dataset.sag); renk = (renk % 5) + 1; for (const x of [s, d]) x.classList.add('esli', `r${renk}`); kayit(); }
      else { hatalar.add(Number(s.dataset.sol)); for (const x of [s, d]) { x.classList.add('titre'); setTimeout(() => x.classList.remove('titre'), 450); } }
    });
    kart.append(el('p', { sinif: 'etk-ipucu-kucuk' }, 'Soldan bir öğeye, sonra sağdaki eşine dokun. Yanlış deneme puanı düşürür.'), sutunlar);
    k.isaretle = () => {};
    sonrasi(k);
  }
  function siralamaCiz(k) {
    const { kart, q, c } = k;
    let sira = c?.secim ? [...c.secim] : [...q.sira];   // ekrandaki sıra: asıl öge indeksleri
    const liste = el('ol', { sinif: 't-sira', 'aria-label': 'Sıralanacak ögeler' });
    const ciz = () => liste.replaceChildren(...sira.map((oi, pos) => el('li', { sinif: 't-sira-oge' },
      el('span', { sinif: 't-sira-no', 'aria-hidden': 'true' }, String(pos + 1)), html('span', 't-sira-metin', q.ogeler[oi]),
      el('span', { sinif: 't-sira-dugmeler' },
        el('button', { sinif: 't-sira-dugme', type: 'button', 'aria-label': 'Yukarı taşı', disabled: pos === 0 || null, onclick: () => tasi(pos, pos - 1) }, '▲'),
        el('button', { sinif: 't-sira-dugme', type: 'button', 'aria-label': 'Aşağı taşı', disabled: pos === sira.length - 1 || null, onclick: () => tasi(pos, pos + 1) }, '▼')))));
    const tasi = (a, b) => { if (kart.classList.contains('bitti')) return; [sira[a], sira[b]] = [sira[b], sira[a]]; ciz(); oturum.cevaplar[oturum.no] = null; kaydet(); };
    ciz();
    const kontrolDugme = el('button', { sinif: 'dugme etk-kontrol', type: 'button', onclick: () => { if (kart.classList.contains('bitti')) return; const d = sira.filter((oi, pos) => oi === pos).length; cevapla(k, { secim: sira, dogru: d === sira.length, parca: [d, sira.length] }); } }, 'Sıralamayı onayla');
    kart.append(el('p', { sinif: 'etk-ipucu-kucuk' }, 'Ögeleri oklarla doğru sıraya getir, sonra onayla.'), liste, kontrolDugme);
    k.isaretle = (c) => { liste.querySelectorAll('.t-sira-oge').forEach((li, pos) => li.classList.add(c.secim[pos] === pos ? 'dogru' : 'yanlis')); if (!c.dogru) kart.append(html('div', 't-sira-dogru', `<b>Doğru sıra:</b><ol>${q.ogeler.map((o) => `<li>${o}</li>`).join('')}</ol>`)); };
    sonrasi(k);
  }
  function acikCiz(k) {
    const { kart, q, c } = k;
    const cevap = html('div', 't-cevap', `<b>Cevap</b>${q.cevap}`); cevap.hidden = !c;
    const ipucu = q.ipuclari?.length ? el('details', { sinif: 't-ipucu' }, el('summary', {}, 'İpucu'), ...q.ipuclari.map((i) => html('p', '', i))) : null;
    const goster = el('button', { sinif: 'dugme', type: 'button', onclick: () => { cevap.hidden = false; goster.hidden = true; oz.hidden = false; } }, 'Cevabı göster');
    const oz = el('div', { sinif: 't-oz', hidden: true }, el('span', {}, 'Kendini değerlendir:'),
      el('button', { sinif: 'dugme etk-kontrol', type: 'button', onclick: () => cevapla(k, { secim: 'bildim', dogru: true }) }, 'Bildim'),
      el('button', { sinif: 'dugme etk-kontrol', type: 'button', onclick: () => cevapla(k, { secim: 'bilemedim', dogru: false }) }, 'Bilemedim'));
    if (c) { goster.hidden = true; oz.hidden = true; }
    kart.append(el('p', { sinif: 'etk-ipucu-kucuk' }, 'Cevabını kafanda ya da kâğıtta hazırla, sonra karşılaştır.'), ipucu, goster, cevap, oz);
    k.isaretle = () => {};
    sonrasi(k);
  }
  // Daha önce cevaplanmış soru yeniden açılınca (geri gelme, sonuçtan bakma) durumu gösterilir
  function sonrasi(k) { if (k.c != null) cevapGoster(k, k.c); }

  // ---------------------------------------------------------------- bitiş ve sonuç
  function bitirSor() {
    const bos = oturum.cevaplar.filter((c) => c == null).length;
    if (bos && !confirm(`${bos} soru cevaplanmadı. Yine de bitirilsin mi?`)) return;
    bitir();
  }
  function bitir() {
    oturum.bitti = true; oturum.sure = Math.round((Date.now() - oturum.baslangic) / 1000); kaydet();
    const dogru = oturum.cevaplar.filter((c) => c?.dogru === true).length, toplam = oturum.sorular.length;
    const gecmis = depo.al('test-gecmis', []);
    gecmis.unshift({ tarih: new Date().toISOString(), anahtar: oturum.anahtar, kapsam: oturum.kapsam, dogru, toplam, sure: oturum.sure });
    depo.koy('test-gecmis', gecmis.slice(0, 30));
    sonucGoster();
  }
  function sonucGoster() {
    const dogru = oturum.cevaplar.filter((c) => c?.dogru === true).length, toplam = oturum.sorular.length, yuzde = Math.round(100 * dogru / toplam);
    const dk = Math.floor((oturum.sure || 0) / 60), sn = (oturum.sure || 0) % 60;
    const mesaj = yuzde === 100 ? 'Mükemmel! Hepsi doğru.' : yuzde >= 80 ? 'Çok iyi! Birkaç soruya daha bakmak yeter.' : yuzde >= 50 ? 'İyi gidiyorsun; yanlışları tekrar çöz.' : 'Konu anlatımına dönüp yeniden denemek iyi olur.';
    const grupla = (anahtar) => {
      const m = new Map();
      oturum.sorular.forEach((q, i) => { for (const a of anahtar(q)) { const g = m.get(a) || { dogru: 0, toplam: 0 }; g.toplam++; if (oturum.cevaplar[i]?.dogru === true) g.dogru++; m.set(a, g); } });
      return [...m.entries()];
    };
    const konuAd = (kod) => ders?.uniteler.flatMap((u) => u.konular).find((k) => k.kod === kod)?.ad || kod;
    const ciktiAd = (kod) => ders?.ciktilar.find((c) => c.kod === kod)?.ifade || '';
    const satir = ([ad, g], alt) => el('li', {}, el('span', { sinif: 't-dagilim-ad' }, ad, alt ? el('small', {}, alt) : null),
      el('span', { sinif: 't-dagilim-sayi' }, `${g.dogru} / ${g.toplam}`), el('progress', { max: g.toplam, value: g.dogru, 'aria-hidden': 'true' }));
    const konular = grupla((q) => [q.konu]), ciktilar = grupla((q) => q.cikti);
    const yanlislar = oturum.sorular.map((q, i) => ({ q, c: oturum.cevaplar[i], i })).filter((x) => x.c?.dogru !== true);
    const liste = el('ol', { sinif: 't-gozden' }, ...oturum.sorular.map((q, i) => {
      const c = oturum.cevaplar[i];
      const li = el('li', { sinif: `t-gozden-oge ${c?.dogru === true ? 'dogru' : c ? 'yanlis' : 'bos'}` },
        el('span', { sinif: 't-gozden-durum', 'aria-hidden': 'true' }, c?.dogru === true ? '✓' : c ? '✗' : '–'),
        el('div', {}, html('p', 't-gozden-soru', q.soru), el('small', {}, [TUR_AD[q.tur], konuAd(q.konu), c ? (c.dogru === true ? 'doğru' : c.parca ? `${c.parca[0]}/${c.parca[1]} doğru` : 'yanlış') : 'cevaplanmadı'].join(' · ')),
          c?.dogru !== true ? dogruCevap(q) : null),
        el('button', { sinif: 'dugme t-gozden-ac', type: 'button', onclick: () => { oturum.no = i; goster('test'); soruGoster(); } }, 'Soruyu gör'));
      return li;
    }));
    sonucAlan.replaceChildren(
      el('div', { sinif: 't-sonuc-kart' },
        el('p', { sinif: 'ust-baslik' }, oturum.kapsam),
        el('p', { sinif: 't-puan' }, el('b', {}, `${yuzde}`), el('span', {}, '%')),
        el('h2', {}, `${dogru} / ${toplam} doğru`),
        el('p', { sinif: 't-sonuc-mesaj' }, mesaj, el('small', {}, ` Süre: ${dk ? `${dk} dk ` : ''}${sn} sn`)),
        el('div', { sinif: 't-sonuc-dugmeler' },
          yanlislar.length ? el('button', { sinif: 'dugme ana', type: 'button', onclick: () => oturumBaslat(yanlislar.map((x) => hazirla(ders.sorular.find((s) => s.id === x.q.id) || x.q)), `${oturum.kapsam} · yanlışlar`, oturum.donut) }, `Yanlışları tekrar çöz (${yanlislar.length})`) : null,
          el('button', { sinif: 'dugme ana', type: 'button', onclick: () => { const h = havuz(); if (h.length) oturumBaslat(secimYap(h, Number(alan.adet.value) || 0), kapsamMetni(), alan.donut.value); } }, 'Yeni test'),
          el('button', { sinif: 'dugme', type: 'button', onclick: () => { oturum = null; try { sessionStorage.removeItem(OTURUM); } catch {} goster('kurulum'); gecmisCiz(); } }, 'Ayarları değiştir'))),
      konular.length > 1 ? el('section', { sinif: 't-dagilim' }, el('h3', {}, 'Konulara göre'), el('ul', {}, ...konular.map(([kod, g]) => satir([konuAd(kod), g])))) : null,
      ciktilar.length ? el('section', { sinif: 't-dagilim' }, el('h3', {}, 'Öğrenme çıktılarına göre'), el('ul', {}, ...ciktilar.map(([kod, g]) => satir([kod, g], ciktiAd(kod))))) : null,
      el('section', { sinif: 't-gozden-bolum' }, el('h3', {}, 'Sorular'), liste));
    goster('sonuc');
    sonucAlan.querySelector('h2').setAttribute('tabindex', '-1'); sonucAlan.querySelector('h2').focus({ preventScroll: true });
  }
  function dogruCevap(q) {
    if (q.tur === 'coktan') return html('p', 't-dogru-cevap', `<b>Doğru cevap:</b> ${q.secenekler[q.dogru]}${q.aciklama ? ` <span>${q.aciklama}</span>` : ''}`);
    if (q.tur === 'dy') return html('p', 't-dogru-cevap', `<b>Doğrusu:</b> ${q.ifadeler.map((f) => `${f.dogru ? 'D' : 'Y'}`).join(', ')}`);
    if (q.tur === 'bosluk') return html('p', 't-dogru-cevap', `<b>Doğrusu:</b> ${q.cumleler.map((c) => c.cevap).join(', ')}`);
    if (q.tur === 'eslestir') return html('p', 't-dogru-cevap', `<b>Eşler:</b> ${q.ciftler.map((c) => `${c[0]} – ${c[1]}`).join('; ')}`);
    if (q.tur === 'siralama') return html('p', 't-dogru-cevap', `<b>Doğru sıra:</b> ${q.ogeler.join(' → ')}`);
    return html('p', 't-dogru-cevap', `<b>Cevap:</b> ${q.cevap}`);
  }
  function gecmisCiz() {
    const liste = depo.al('test-gecmis', []).slice(0, 6);
    const ol = gecmisAlan.querySelector('ol');
    ol.replaceChildren(...liste.map((g) => el('li', {}, el('span', {}, g.kapsam), el('b', {}, `${g.dogru} / ${g.toplam}`), el('time', { datetime: g.tarih }, new Date(g.tarih).toLocaleDateString('tr-TR', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })))));
    gecmisAlan.hidden = !liste.length;
  }

  // ---------------------------------------------------------------- klavye
  document.addEventListener('keydown', (o) => {
    if (testAlan.hidden || o.ctrlKey || o.metaKey || o.altKey || /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)) return;
    const q = oturum?.sorular[oturum.no]; if (!q) return;
    const k = o.key.toLowerCase();
    if (q.tur === 'coktan') { const i = /^[1-6]$/.test(k) ? Number(k) - 1 : HARF.toLowerCase().indexOf(k); if (i >= 0 && i < q.secenekler.length) { testAlan.querySelector(`.etk-sec[data-i="${i}"]`)?.click(); o.preventDefault(); return; } }
    if (o.key === 'Enter' || o.key === 'ArrowRight') { const s = testAlan.querySelector('#t-sonraki'); if (s && !s.disabled) { s.click(); o.preventDefault(); } }
    if (o.key === 'ArrowLeft') { const s = testAlan.querySelector('#t-onceki'); if (s && !s.disabled) { s.click(); o.preventDefault(); } }
  });

  // ---------------------------------------------------------------- başlat
  kurulum.addEventListener('submit', (o) => {
    o.preventDefault();
    const h = havuz(); if (!h.length) return;
    depo.koy('test-son', { sinif: alan.sinif.value, ders: alan.ders.value, turler: secilenTurler(), adet: alan.adet.value, donut: alan.donut.value });
    oturumBaslat(secimYap(h, Number(alan.adet.value) || 0), kapsamMetni(), alan.donut.value);
  });
  alan.sinif.addEventListener('change', () => { dersDoldur(); dersYukle(); });
  alan.ders.addEventListener('change', dersYukle);
  alan.konu.addEventListener('change', ciktiDoldur);
  alan.cikti.addEventListener('change', havuzGuncelle);
  turKutular().forEach((k) => k.addEventListener('change', havuzGuncelle));
  function dersDoldur() {
    const sinif = alan.sinif.value;
    const liste = Object.values(dizin.dersler).filter((d) => String(d.sinif) === sinif).sort((a, b) => a.ad.localeCompare(b.ad, 'tr'));
    secenekDoldur(alan.ders, liste.map((d) => [d.ders, `${d.ad} (${d.toplam})`]));
    if (!alan.ders.value && liste.length) alan.ders.value = liste[0].ders;
  }
  Promise.all([veri('soru/dizin.json'), ortakVeri]).then(async ([dz, { dersler }]) => {
    dizin = dz;
    if (!dizin?.dersler) { havuzYazi.textContent = 'Soru havuzu şu anda yüklenemedi. Sayfayı yenileyin.'; return; }
    const son = depo.al('test-son', {});
    const siniflar = [...new Set(Object.values(dizin.dersler).map((d) => d.sinif))].sort((a, b) => a - b);
    secenekDoldur(alan.sinif, siniflar.map((n) => [String(n), `${n}. sınıf`]));
    alan.sinif.value = [P.get('sinif'), son.sinif, String(siniflar[0])].find((v) => v && siniflar.includes(Number(v))) || String(siniflar[0]);
    dersDoldur();
    const istenenDers = P.get('ders') || son.ders;
    if (istenenDers && [...alan.ders.options].some((o) => o.value === istenenDers)) alan.ders.value = istenenDers;
    if (P.get('tur')) { const t = new Set(P.get('tur').split(',')); turKutular().forEach((k) => { k.checked = t.has(k.value); }); }
    else if (son.turler) turKutular().forEach((k) => { k.checked = son.turler.includes(k.value); });
    if (P.get('adet') && [...alan.adet.options].some((o) => o.value === P.get('adet'))) alan.adet.value = P.get('adet'); else if (son.adet) alan.adet.value = son.adet;
    if (P.get('donut')) alan.donut.value = P.get('donut'); else if (son.donut) alan.donut.value = son.donut;
    await dersYukle();
    gecmisCiz();
    // Yarım kalan test (sekme yenilendi): sürdür
    let eski = null; try { eski = JSON.parse(sessionStorage.getItem(OTURUM)); } catch {}
    if (eski && !eski.bitti && eski.sorular?.length) {
      if (eski.anahtar !== dersAnahtar) { alan.sinif.value = String(eski.sinif); dersDoldur(); alan.ders.value = eski.ders; await dersYukle(); }
      oturum = eski; goster('test'); soruGoster();
      return;
    }
    if (P.get('basla') === '1' && !basla.disabled) kurulum.requestSubmit();
  });
})();
