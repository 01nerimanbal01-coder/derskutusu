// Akıllı tahta kalemi: her sayfada sayfanın (ya da belge görüntüleyicinin) üstüne yazma, tahta.html'de boş tahta.
// Hız: iki katman — biten çizgiler alt tuvalde, çizilmekte olan çizgi üst tuvalde requestAnimationFrame ile çizilir;
// çizgiler vektör olarak tutulur (geri al / yinele / silgi), kalem basıncı ve birleşik (coalesced) olaylar kullanılır.
// Dışarıdan hiçbir şey yüklenmez; çizimler yalnız bu tarayıcıda kalır.

const Tahta = (() => {
  const RENKLER = ['#111a2e', '#e62117', '#2451d6', '#12a150', '#f29f05', '#8b3fd6', '#ffffff'];
  const KALINLIK = { ince: 2.5, orta: 5, kalin: 10 };
  const ARAC_SIMGE = {
    kalem: 'M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3',
    fosforlu: 'M6 14l6-6 4 4-6 6H6v-4zM4 20h16',
    silgi: 'M8 20h12M5 15l7-7 5 5-5 5H9l-4-3z',
    el: 'M8 13V6a1.5 1.5 0 013 0v5m0-6a1.5 1.5 0 013 0v6m0-5a1.5 1.5 0 013 0v7a6 6 0 01-6 6h-1a6 6 0 01-5-3l-2-4a1.5 1.5 0 012.5-1.5L8 15',
  };
  const svg = (d) => `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${d}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

  function olustur({ kap, kaydir = false, zemin = null, kapat = null }) {
    // kap: tuvallerin konacağı öğe; kaydir: true → çizgiler sayfa kaydırmasıyla, öğe → o öğenin (ör. PDF kabı) kaydırmasıyla kayar
    const alt = document.createElement('canvas');
    const ust = document.createElement('canvas');
    alt.className = 'tahta-tuval'; ust.className = 'tahta-tuval tahta-ust';
    kap.append(alt, ust);
    const a = alt.getContext('2d'), u = ust.getContext('2d');
    const d = { arac: 'kalem', renk: RENKLER[1], kalinlik: 'orta', cizgiler: [], ileri: [], canli: null, istek: 0, zemin };
    let oran = 1, gen = 0, yuk = 0;

    const kay = () => (kaydir === true ? { x: scrollX, y: scrollY } : kaydir ? { x: kaydir.scrollLeft, y: kaydir.scrollTop } : { x: 0, y: 0 });
    function boyutla() {
      const r = kap.getBoundingClientRect();
      oran = Math.min(window.devicePixelRatio || 1, 2);
      gen = r.width; yuk = r.height;
      for (const t of [alt, ust]) { t.width = Math.round(gen * oran); t.height = Math.round(yuk * oran); t.style.width = gen + 'px'; t.style.height = yuk + 'px'; }
      hepsiniCiz();
    }
    function zeminCiz() {
      a.save();
      a.setTransform(oran, 0, 0, oran, 0, 0);
      if (d.zemin) {
        a.fillStyle = '#fdfdfb'; a.fillRect(0, 0, gen, yuk);
        a.strokeStyle = 'rgba(36,81,214,.16)'; a.fillStyle = 'rgba(36,81,214,.28)'; a.lineWidth = 1;
        const aralik = 28;
        if (d.zemin === 'kareli' || d.zemin === 'cizgili') {
          a.beginPath();
          for (let y = aralik; y < yuk; y += aralik) { a.moveTo(0, y + .5); a.lineTo(gen, y + .5); }
          if (d.zemin === 'kareli') for (let x = aralik; x < gen; x += aralik) { a.moveTo(x + .5, 0); a.lineTo(x + .5, yuk); }
          a.stroke();
        } else if (d.zemin === 'noktali') {
          for (let y = aralik; y < yuk; y += aralik) for (let x = aralik; x < gen; x += aralik) a.fillRect(x - 1, y - 1, 2, 2);
        }
      }
      a.restore();
    }
    function cizgiCiz(c, t, k) {
      const n = c.n;
      if (!n.length) return;
      t.save();
      t.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      t.lineCap = 'round'; t.lineJoin = 'round';
      t.strokeStyle = c.renk; t.fillStyle = c.renk;
      t.globalAlpha = c.arac === 'fosforlu' ? 0.32 : 1;
      if (n.length === 1) { t.beginPath(); t.arc(n[0][0], n[0][1], c.g * (c.arac === 'fosforlu' ? 1 : n[0][2]) / 2, 0, Math.PI * 2); t.fill(); t.restore(); return; }
      if (c.arac === 'fosforlu') {
        // Fosforlu tek yol olarak çizilir: üst üste binen yerler koyulaşmaz.
        t.lineWidth = c.g; t.beginPath(); t.moveTo(n[0][0], n[0][1]);
        for (let i = 1; i < n.length - 1; i++) t.quadraticCurveTo(n[i][0], n[i][1], (n[i][0] + n[i + 1][0]) / 2, (n[i][1] + n[i + 1][1]) / 2);
        t.lineTo(n[n.length - 1][0], n[n.length - 1][1]); t.stroke();
      } else {
        // Kalem: basınca göre değişen kalınlık, orta noktalardan geçen yumuşak eğriler.
        for (let i = 1; i < n.length; i++) {
          const p0 = i > 1 ? [(n[i - 2][0] + n[i - 1][0]) / 2, (n[i - 2][1] + n[i - 1][1]) / 2] : n[0];
          const p1 = [(n[i - 1][0] + n[i][0]) / 2, (n[i - 1][1] + n[i][1]) / 2];
          t.lineWidth = c.g * (n[i - 1][2] + n[i][2]) / 2;
          t.beginPath(); t.moveTo(p0[0], p0[1]); t.quadraticCurveTo(n[i - 1][0], n[i - 1][1], p1[0], p1[1]); t.stroke();
        }
        const s = n[n.length - 1], o = n[n.length - 2];
        t.lineWidth = c.g * s[2]; t.beginPath(); t.moveTo((o[0] + s[0]) / 2, (o[1] + s[1]) / 2); t.lineTo(s[0], s[1]); t.stroke();
      }
      t.restore();
    }
    function hepsiniCiz() {
      a.setTransform(1, 0, 0, 1, 0, 0); a.clearRect(0, 0, alt.width, alt.height);
      zeminCiz();
      const k = kay();
      for (const c of d.cizgiler) cizgiCiz(c, a, k);
    }
    function canliCiz() {
      d.istek = 0;
      u.setTransform(1, 0, 0, 1, 0, 0); u.clearRect(0, 0, ust.width, ust.height);
      if (d.canli) cizgiCiz(d.canli, u, kay());
    }
    const iste = () => { if (!d.istek) d.istek = requestAnimationFrame(canliCiz); };

    function nokta(o) {
      const r = kap.getBoundingClientRect(), k = kay();
      const b = o.pointerType === 'pen' ? Math.max(0.15, o.pressure || 0.5) * 1.6 : 1;
      return [o.clientX - r.left + k.x, o.clientY - r.top + k.y, b];
    }
    // Silgi: dokunulan çizgiyi bütünüyle siler (hızlı ve geri alınabilir).
    function sil(p) {
      const esik = 12;
      const once = d.cizgiler.length;
      const silinen = [];
      d.cizgiler = d.cizgiler.filter((c) => {
        const vur = c.n.some((q, i) => {
          const r = i ? c.n[i - 1] : q;
          const dx = q[0] - r[0], dy = q[1] - r[1], L = dx * dx + dy * dy;
          const t = L ? Math.max(0, Math.min(1, ((p[0] - r[0]) * dx + (p[1] - r[1]) * dy) / L)) : 0;
          return Math.hypot(p[0] - (r[0] + t * dx), p[1] - (r[1] + t * dy)) < esik + c.g / 2;
        });
        if (vur) silinen.push(c);
        return !vur;
      });
      if (d.cizgiler.length !== once) { d.ileri = []; d.gecmis.push({ tur: 'sil', cizgiler: silinen }); hepsiniCiz(); }
    }
    d.gecmis = [];

    let aktif = null;
    ust.addEventListener('pointerdown', (o) => {
      if (d.arac === 'el' || o.button > 0) return;
      o.preventDefault();
      try { ust.setPointerCapture(o.pointerId); } catch { /* yapay olay */ }
      aktif = o.pointerId;
      const p = nokta(o);
      if (d.arac === 'silgi') { sil(p); return; }
      d.canli = { arac: d.arac, renk: d.renk, g: KALINLIK[d.kalinlik] * (d.arac === 'fosforlu' ? 3.2 : 1), n: [p] };
      iste();
    });
    ust.addEventListener('pointermove', (o) => {
      if (o.pointerId !== aktif) return;
      const birlesik = o.getCoalescedEvents?.() || [];
      const olaylar = birlesik.length ? birlesik : [o];
      if (d.arac === 'silgi') { for (const e of olaylar) sil(nokta(e)); return; }
      if (!d.canli) return;
      for (const e of olaylar) {
        const p = nokta(e), s = d.canli.n[d.canli.n.length - 1];
        if (Math.hypot(p[0] - s[0], p[1] - s[1]) > 0.8) d.canli.n.push(p);
      }
      iste();
    });
    const bitir = (o) => {
      if (o.pointerId !== aktif) return;
      aktif = null;
      if (d.canli) {
        d.cizgiler.push(d.canli); d.gecmis.push({ tur: 'ekle', cizgi: d.canli }); d.ileri = [];
        cizgiCiz(d.canli, a, kay());
        d.canli = null; iste();
      }
    };
    ust.addEventListener('pointerup', bitir);
    ust.addEventListener('pointercancel', bitir);

    const geriAl = () => {
      const g = d.gecmis.pop(); if (!g) return;
      if (g.tur === 'ekle') d.cizgiler = d.cizgiler.filter((c) => c !== g.cizgi); else d.cizgiler.push(...g.cizgiler);
      d.ileri.push(g); hepsiniCiz();
    };
    const yinele = () => {
      const g = d.ileri.pop(); if (!g) return;
      if (g.tur === 'ekle') d.cizgiler.push(g.cizgi); else d.cizgiler = d.cizgiler.filter((c) => !g.cizgiler.includes(c));
      d.gecmis.push(g); hepsiniCiz();
    };
    const temizle = () => { if (!d.cizgiler.length) return; d.gecmis.push({ tur: 'sil', cizgiler: d.cizgiler }); d.cizgiler = []; d.ileri = []; hepsiniCiz(); };

    // Araç çubuğu
    const cubuk = document.createElement('div');
    cubuk.className = 'tahta-cubuk';
    cubuk.setAttribute('role', 'toolbar');
    cubuk.setAttribute('aria-label', 'Tahta araçları');
    const dugme = (ad, ic, is, ek = '') => `<button type="button" class="${ek}" data-${ad}="${is}" title="${ic.baslik}" aria-label="${ic.baslik}">${ic.html}</button>`;
    cubuk.innerHTML =
      `<div class="tahta-grup">${[['kalem', 'Kalem (K)'], ['fosforlu', 'Fosforlu kalem (F)'], ['silgi', 'Silgi (S)'], ...(kaydir ? [['el', 'Sayfayı kaydır (E)']] : [])]
        .map(([is, b]) => dugme('arac', { baslik: b, html: svg(ARAC_SIMGE[is]) }, is)).join('')}</div>` +
      `<div class="tahta-grup">${RENKLER.map((r, i) => dugme('renk', { baslik: `Renk ${i + 1}`, html: `<span style="background:${r}"></span>` }, r, 'renk')).join('')}</div>` +
      `<div class="tahta-grup">${Object.keys(KALINLIK).map((k) => dugme('kalinlik', { baslik: `Kalınlık: ${k}`, html: `<i style="width:${KALINLIK[k] + 2}px;height:${KALINLIK[k] + 2}px"></i>` }, k, 'kalin')).join('')}</div>` +
      `<div class="tahta-grup">` +
      dugme('is', { baslik: 'Geri al (Ctrl+Z)', html: svg('M9 14L4 9l5-5M4 9h10a6 6 0 010 12h-3') }, 'geri') +
      dugme('is', { baslik: 'Yinele (Ctrl+Y)', html: svg('M15 14l5-5-5-5M20 9H10a6 6 0 000 12h3') }, 'ileri') +
      dugme('is', { baslik: 'Temizle', html: svg('M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3') }, 'temizle') +
      (kapat ? dugme('is', { baslik: 'Kalemi kapat (Esc)', html: svg('M6 6l12 12M18 6L6 18') }, 'kapat', 'kapat') : '') + `</div>`;
    kap.append(cubuk);
    const guncelle = () => {
      cubuk.querySelectorAll('[data-arac]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.arac === d.arac)));
      cubuk.querySelectorAll('[data-renk]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.renk === d.renk)));
      cubuk.querySelectorAll('[data-kalinlik]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.kalinlik === d.kalinlik)));
      ust.style.pointerEvents = d.arac === 'el' ? 'none' : 'auto';
      ust.style.cursor = d.arac === 'silgi' ? 'cell' : 'crosshair';
    };
    cubuk.addEventListener('click', (o) => {
      const b = o.target.closest('button'); if (!b) return;
      if (b.dataset.arac) d.arac = b.dataset.arac;
      if (b.dataset.renk) { d.renk = b.dataset.renk; if (d.arac === 'silgi' || d.arac === 'el') d.arac = 'kalem'; }
      if (b.dataset.kalinlik) d.kalinlik = b.dataset.kalinlik;
      if (b.dataset.is === 'geri') geriAl();
      if (b.dataset.is === 'ileri') yinele();
      if (b.dataset.is === 'temizle') temizle();
      if (b.dataset.is === 'kapat') kapat?.();
      guncelle();
    });
    const tus = (o) => {
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)) return;
      const k = o.key.toLowerCase();
      if ((o.ctrlKey || o.metaKey) && k === 'z') { o.preventDefault(); o.shiftKey ? yinele() : geriAl(); return; }
      if ((o.ctrlKey || o.metaKey) && k === 'y') { o.preventDefault(); yinele(); return; }
      if (o.ctrlKey || o.metaKey || o.altKey) return;
      const arac = { k: 'kalem', f: 'fosforlu', s: 'silgi', e: kaydir ? 'el' : null }[k];
      if (arac) { d.arac = arac; guncelle(); }
      if (k === 'escape' && kapat) kapat();
    };
    document.addEventListener('keydown', tus);
    const olcu = new ResizeObserver(boyutla);
    olcu.observe(kap);
    const kaydirildi = () => { hepsiniCiz(); iste(); };
    const kaydirHedef = kaydir === true ? window : kaydir;
    kaydirHedef?.addEventListener('scroll', kaydirildi, { passive: true });
    // Kalem açıkken fare tekerleği alttaki kabı kaydırır.
    if (kaydir && kaydir !== true) ust.addEventListener('wheel', (o) => { o.preventDefault(); kaydir.scrollBy({ left: o.deltaX, top: o.deltaY }); }, { passive: false });
    boyutla(); guncelle();
    return {
      d, hepsiniCiz, geriAl, yinele, temizle,
      zemin: (z) => { d.zemin = z; hepsiniCiz(); },
      yukle: (cizgiler) => { d.cizgiler = cizgiler; d.gecmis = []; d.ileri = []; hepsiniCiz(); },
      png: () => alt.toDataURL('image/png'),
      // Yakınlaştırmada çizgiler içerikle birlikte ölçeklenir.
      olcekle: (k) => {
        const hepsi = new Set([...d.cizgiler, ...[...d.gecmis, ...d.ileri].flatMap((g) => g.cizgiler || [g.cizgi])]);
        for (const c of hepsi) { c.g *= k; for (const q of c.n) { q[0] *= k; q[1] *= k; } }
        hepsiniCiz();
      },
      kaldir: () => { olcu.disconnect(); document.removeEventListener('keydown', tus); kaydirHedef?.removeEventListener('scroll', kaydirildi); alt.remove(); ust.remove(); cubuk.remove(); },
    };
  }
  return { olustur };
})();

if (typeof document !== 'undefined') {
  // tahta.html: boş tahta, sayfalar, zemin, kaydet
  const tahtaKap = document.getElementById('tahta');
  if (tahtaKap) {
    const sayfalar = [[]];
    let no = 0;
    const t = Tahta.olustur({ kap: tahtaKap, zemin: 'kareli' });
    const sayfaYaz = () => { document.getElementById('t-sayfa').textContent = `${no + 1} / ${sayfalar.length}`; };
    const git = (yeni) => { sayfalar[no] = t.d.cizgiler; no = yeni; t.yukle(sayfalar[no]); sayfaYaz(); };
    document.getElementById('t-onceki').addEventListener('click', () => no > 0 && git(no - 1));
    document.getElementById('t-sonraki').addEventListener('click', () => { if (no === sayfalar.length - 1) sayfalar.push([]); git(no + 1); });
    document.getElementById('t-zemin').addEventListener('change', (o) => t.zemin(o.target.value || null));
    document.getElementById('t-kaydet').addEventListener('click', () => {
      const a = document.createElement('a'); a.href = t.png(); a.download = `tahta-${no + 1}.png`; a.click();
    });
    document.getElementById('t-tam').addEventListener('click', () => (document.fullscreenElement ? document.exitFullscreen() : document.getElementById('tahta-alan').requestFullscreen?.()));
    sayfaYaz();
  } else {
    // Öteki sayfalar: sağ altta kalem düğmesi → sayfanın üstüne yaz
    const ac = document.createElement('button');
    ac.type = 'button'; ac.className = 'kalem-dugme'; ac.title = 'Kalemle sayfaya yaz (akıllı tahta)'; ac.setAttribute('aria-label', 'Kalemle sayfaya yaz');
    ac.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    document.body.append(ac);
    let t = null, kap = null;
    const kapat = () => { kap.hidden = true; ac.hidden = false; document.body.classList.remove('kalem-acik'); };
    ac.addEventListener('click', () => {
      if (!kap) {
        const hedef = window.kalemHedef;       // goruntule.js PDF'i kendisi çizerse kabını bildirir
        kap = document.createElement('div');
        kap.className = hedef ? 'kalem-katman yerel' : 'kalem-katman';
        (hedef ? hedef.kap : document.body).append(kap);
        t = Tahta.olustur({ kap, kaydir: hedef ? hedef.kaydir : true, kapat });
        window.kalemAcik = t;
      }
      kap.hidden = false;
      ac.hidden = true;
      document.body.classList.add('kalem-acik');
      t.hepsiniCiz();
    });
    window.kalemAc = () => ac.click();
  }
}
