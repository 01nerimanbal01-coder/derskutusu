// Akıllı tahta kalemi: her sayfada sayfanın (ya da belge görüntüleyicinin) üstüne yazma, tahta.html'de boş tahta.
// Hız: iki katman — biten çizgiler alt tuvalde, çizilmekte olan çizgi üst tuvalde requestAnimationFrame ile çizilir;
// çizgiler vektör olarak tutulur (geri al / yinele / silgi), kalem basıncı, birleşik (coalesced) ve öngörülen olaylar kullanılır.
// Araç kutusu (kullanıcı 13.10.2026: "kalem daha hassas olmalı, araç kutusu düğmesi"): kalınlık sürgüsü, geniş renk paleti ve özel renk,
// şekiller (doğru, ok, dikdörtgen, elips), işaretçi, çizgi düzeltme, avuç koruması, basınç ayarı; seçimler bu tarayıcıda hatırlanır.
// Dışarıdan hiçbir şey yüklenmez; çizimler yalnız bu tarayıcıda kalır.

const Tahta = (() => {
  const RENKLER = ['#111a2e', '#e62117', '#2451d6', '#12a150', '#f29f05', '#8b3fd6', '#ffffff'];
  const PALET = [...RENKLER, '#0d9488', '#db2777', '#ea580c', '#7c3aed', '#6366f1', '#795209', '#5b6479', '#ffd400'];
  const KALINLIK = { ince: 2.5, orta: 5, kalin: 10 };
  const SILGI = { ince: 8, orta: 16, kalin: 30 };          // kısmi silginin yarıçapı (px)
  const SEKIL = { dogru: 'Doğru', ok: 'Ok', dikdortgen: 'Dikdörtgen', elips: 'Elips' };
  const ARAC_SIMGE = {
    kalem: 'M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3',
    fosforlu: 'M6 14l6-6 4 4-6 6H6v-4zM4 20h16',
    silgi: 'M8 20h12M5 15l7-7 5 5-5 5H9l-4-3z',
    cizgisil: 'M3 16c3-4 6-4 9 0s6 4 9 0M9 6l6 6M15 6l-6 6',
    el: 'M8 13V6a1.5 1.5 0 013 0v5m0-6a1.5 1.5 0 013 0v6m0-5a1.5 1.5 0 013 0v7a6 6 0 01-6 6h-1a6 6 0 01-5-3l-2-4a1.5 1.5 0 012.5-1.5L8 15',
    dogru: 'M4 20L20 4',
    ok: 'M4 20L20 4M11 4h9v9',
    dikdortgen: 'M4 6h16v12H4z',
    elips: 'M12 5a8 7 0 100 14 8 7 0 100-14z',
    isaretci: 'M12 12m-3 0a3 3 0 106 0 3 3 0 10-6 0M12 3v3M12 18v3M3 12h3M18 12h3',
    kutu: 'M4 7h10M18 7h2M4 17h4M12 17h8M14 4.5v5M8 14.5v5',
  };
  const AYAR_ANAHTAR = 'tahta-ayar';
  const ayarOku = () => { try { return JSON.parse(localStorage.getItem(AYAR_ANAHTAR)) || {}; } catch { return {}; } };
  const ayarYaz = (a) => { try { localStorage.setItem(AYAR_ANAHTAR, JSON.stringify(a)); } catch { /* gizli pencere */ } };
  const svg = (d) => `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${d}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

  function olustur({ kap, kaydir = false, zemin = null, kapat = null }) {
    // kap: tuvallerin konacağı öğe; kaydir: true → çizgiler sayfa kaydırmasıyla, öğe → o öğenin (ör. PDF kabı) kaydırmasıyla kayar
    const alt = document.createElement('canvas');
    const ust = document.createElement('canvas');
    alt.className = 'tahta-tuval'; ust.className = 'tahta-tuval tahta-ust';
    kap.append(alt, ust);
    // Üst (canlı) tuval düşük gecikmeli: desteklenen cihazlarda çizgi kalemi daha yakından izler
    const a = alt.getContext('2d'), u = ust.getContext('2d', { desynchronized: true }) || ust.getContext('2d');
    const ayar = ayarOku();
    const renkGecerli = (r) => typeof r === 'string' && /^#[0-9a-f]{6}$/i.test(r);
    const d = { arac: 'kalem', renk: renkGecerli(ayar.renk) ? ayar.renk.toLowerCase() : RENKLER[1],
      kalinlik: KALINLIK[ayar.kalinlik] ? ayar.kalinlik : 'orta', g: KALINLIK[ayar.kalinlik] || KALINLIK.orta,
      ayar: { duzelt: ayar.duzelt !== false, avuc: ayar.avuc !== false, basinc: ayar.basinc !== false },
      cizgiler: [], ileri: [], canli: null, tahmin: null, isaret: null, istek: 0, zemin };
    if (ayar.kalinlik === 'ozel' && Number.isFinite(ayar.g) && ayar.g >= 1 && ayar.g <= 24) { d.kalinlik = 'ozel'; d.g = ayar.g; }
    const ayarKaydet = () => ayarYaz({ renk: d.renk, kalinlik: d.kalinlik, g: d.g, ...d.ayar });
    const silgiR = () => (SILGI[d.kalinlik] ?? Math.max(8, Math.min(40, d.g * 3)));
    let oran = 1, gen = 0, yuk = 0, kalemGoruldu = false;

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
    // Şekiller iki noktayla tutulur (başlangıç, bitiş); ok ucu çizgi kalınlığıyla büyür.
    function sekilCiz(c, t) {
      const [x0, y0] = c.n[0], [x1, y1] = c.n[c.n.length - 1];
      t.lineWidth = c.g; t.beginPath();
      if (c.arac === 'dogru' || c.arac === 'ok') {
        t.moveTo(x0, y0); t.lineTo(x1, y1);
        if (c.arac === 'ok') {
          const aci = Math.atan2(y1 - y0, x1 - x0), L = Math.max(12, c.g * 3.5);
          for (const s of [-1, 1]) { t.moveTo(x1, y1); t.lineTo(x1 - L * Math.cos(aci - s * 0.5), y1 - L * Math.sin(aci - s * 0.5)); }
        }
      } else if (c.arac === 'dikdortgen') t.rect(Math.min(x0, x1), Math.min(y0, y1), Math.abs(x1 - x0), Math.abs(y1 - y0));
      else t.ellipse((x0 + x1) / 2, (y0 + y1) / 2, Math.abs(x1 - x0) / 2, Math.abs(y1 - y0) / 2, 0, 0, Math.PI * 2);
      t.stroke();
    }
    // Silgi ve kutu hesabı için çevre noktaları: çizgide noktaların kendisi, şekilde kenar örneklemesi
    function cevre(c) {
      if (!SEKIL[c.arac]) return c.n;
      const [x0, y0] = c.n[0], [x1, y1] = c.n[c.n.length - 1];
      if (c.arac === 'dogru' || c.arac === 'ok') return [[x0, y0, 1], [x1, y1, 1]];
      if (c.arac === 'dikdortgen') return [[x0, y0, 1], [x1, y0, 1], [x1, y1, 1], [x0, y1, 1], [x0, y0, 1]];
      const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, rx = Math.abs(x1 - x0) / 2, ry = Math.abs(y1 - y0) / 2;
      return Array.from({ length: 37 }, (_, i) => { const aci = i / 36 * Math.PI * 2; return [cx + rx * Math.cos(aci), cy + ry * Math.sin(aci), 1]; });
    }
    function cizgiCiz(c, t, k) {
      const n = c.n;
      if (!n.length) return;
      t.save();
      t.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      t.lineCap = 'round'; t.lineJoin = 'round';
      t.strokeStyle = c.renk; t.fillStyle = c.renk;
      t.globalAlpha = c.arac === 'fosforlu' ? 0.32 : 1;
      if (SEKIL[c.arac]) { sekilCiz(c, t); t.restore(); return; }
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
      if (d.canli) {
        cizgiCiz(d.canli, u, kay());
        // Tarayıcının öngördüğü noktalar yalnız canlı katmanda: çizgi kalemin ucuna yetişir, kayda girmez
        if (d.tahmin?.length && !SEKIL[d.canli.arac]) cizgiCiz({ ...d.canli, n: [d.canli.n[d.canli.n.length - 1], ...d.tahmin] }, u, kay());
      }
      isaretCiz();
      imlecCiz();
    }
    // İşaretçi: kalıcı iz bırakmayan kırmızı nokta ve sönen kuyruk (anlatırken göstermek için)
    function isaretCiz() {
      if (!d.isaret?.length) return;
      const k = kay(), simdi = performance.now();
      u.save(); u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      d.isaret.forEach((p, i) => {
        const yas = simdi - p[2], son = i === d.isaret.length - 1;
        if (!son && yas > 450) return;
        u.globalAlpha = son ? 1 : Math.max(0, 1 - yas / 450) * 0.5;
        u.beginPath(); u.arc(p[0], p[1], son ? 7 : 4 + 3 * (i / d.isaret.length), 0, Math.PI * 2);
        u.fillStyle = '#e62117'; u.fill();
        if (son) { u.lineWidth = 2; u.strokeStyle = '#fff'; u.stroke(); }
      });
      u.restore();
      if (d.isaret.length > 1) iste();   // kuyruk sönene kadar yeniden çiz
    }
    const iste = () => { if (!d.istek) d.istek = requestAnimationFrame(canliCiz); };

    function nokta(o) {
      const r = kap.getBoundingClientRect(), k = kay();
      const b = d.ayar.basinc && o.pointerType === 'pen' ? Math.max(0.15, o.pressure || 0.5) * 1.6 : 1;
      return [o.clientX - r.left + k.x, o.clientY - r.top + k.y, b];
    }

    // Bir silme hareketi (basıp bırakana kadar) geçmişe tek adım olarak yazılır: eski ve yeni çizgiler.
    let oturum = null;
    const oturumAc = () => { oturum = { eski: new Set(), yeni: new Set() }; };
    const cikar = (c) => { if (oturum.yeni.has(c)) oturum.yeni.delete(c); else oturum.eski.add(c); };
    const oturumKapat = () => {
      if (oturum && (oturum.eski.size || oturum.yeni.size)) { d.gecmis.push({ tur: 'degistir', eski: [...oturum.eski], yeni: [...oturum.yeni] }); d.ileri = []; }
      oturum = null; guncelle();
    };
    function kutu(c) {
      if (!c.k) {
        let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
        for (const q of cevre(c)) { if (q[0] < x0) x0 = q[0]; if (q[0] > x1) x1 = q[0]; if (q[1] < y0) y0 = q[1]; if (q[1] > y1) y1 = q[1]; }
        const pay = c.arac === 'ok' ? Math.max(12, c.g * 3.5) : c.g;
        c.k = [x0 - pay, y0 - pay, x1 + pay, y1 + pay];
      }
      return c.k;
    }
    // Noktanın çizgiye (ya da şeklin çevresine) uzaklığı eşiğin altında mı?
    const dokunur = (c, p, esik) => cevre(c).some((q, i, n) => {
      const r = i ? n[i - 1] : q;
      const dx = q[0] - r[0], dy = q[1] - r[1], L = dx * dx + dy * dy;
      const s = L ? Math.max(0, Math.min(1, ((p[0] - r[0]) * dx + (p[1] - r[1]) * dy) / L)) : 0;
      return Math.hypot(p[0] - (r[0] + s * dx), p[1] - (r[1] + s * dy)) < esik + c.g / 2;
    });
    const yakin = (c, p, r) => { const k = kutu(c); return !(p[0] < k[0] - r || p[0] > k[2] + r || p[1] < k[1] - r || p[1] > k[3] + r); };
    // Kısmi silgi: yalnız silginin değdiği kısmı siler; çizgi gerekirse ikiye bölünür.
    function kismiSil(p) {
      const r = silgiR();
      let degisti = false;
      const sonuc = [];
      for (const c of d.cizgiler) {
        if (!yakin(c, p, r)) { sonuc.push(c); continue; }
        if (SEKIL[c.arac]) {                        // şekil bölünmez: silgi kenarına değince bütünüyle silinir
          if (dokunur(c, p, r)) { degisti = true; cikar(c); } else sonuc.push(c);
          continue;
        }
        const esik = r + c.g / 2, n = [];
        c.n.forEach((q, i) => {                     // noktalar arası en fazla 2 px: silgi aradan kaçmasın
          if (i) {
            const o = c.n[i - 1], adim = Math.ceil(Math.hypot(q[0] - o[0], q[1] - o[1]) / 2);
            for (let j = 1; j < adim; j++) { const s = j / adim; n.push([o[0] + (q[0] - o[0]) * s, o[1] + (q[1] - o[1]) * s, o[2] + (q[2] - o[2]) * s]); }
          }
          n.push(q);
        });
        const parcalar = []; let parca = [], vurdu = false;
        for (const q of n) {
          if (Math.hypot(q[0] - p[0], q[1] - p[1]) < esik) { vurdu = true; if (parca.length) { parcalar.push(parca); parca = []; } }
          else parca.push(q);
        }
        if (parca.length) parcalar.push(parca);
        if (!vurdu) { sonuc.push(c); continue; }
        degisti = true; cikar(c);
        for (const pn of parcalar) {
          if (pn.length < 2 && c.n.length > 1) continue;
          const yeni = { arac: c.arac, renk: c.renk, g: c.g, n: pn };
          sonuc.push(yeni); oturum.yeni.add(yeni);
        }
      }
      if (degisti) { d.cizgiler = sonuc; hepsiniCiz(); }
    }
    // Çizgi silgisi: dokunulan çizgiyi bütünüyle siler.
    function cizgiSil(p) {
      const esik = 12, once = d.cizgiler.length;
      d.cizgiler = d.cizgiler.filter((c) => {
        if (!yakin(c, p, esik)) return true;
        const vur = dokunur(c, p, esik);
        if (vur) cikar(c);
        return !vur;
      });
      if (d.cizgiler.length !== once) hepsiniCiz();
    }
    let sonSilgi = null;
    function silgiUygula(p) {
      // Hızlı harekette aradaki yerler de silinsin: son noktadan bu noktaya küçük adımlarla ilerle.
      const adim = Math.max(3, (d.arac === 'silgi' ? silgiR() : 12) / 2);
      const s = sonSilgi || p, L = Math.hypot(p[0] - s[0], p[1] - s[1]), say = Math.max(1, Math.ceil(L / adim));
      for (let i = 1; i <= say; i++) {
        const q = [s[0] + (p[0] - s[0]) * i / say, s[1] + (p[1] - s[1]) * i / say, 1];
        d.arac === 'silgi' ? kismiSil(q) : cizgiSil(q);
      }
      sonSilgi = p;
    }
    d.gecmis = [];

    // Silgi imleci: silinecek alanı gösteren halka
    function imlecCiz() {
      if (!d.imlec || d.arac !== 'silgi') return;
      const k = kay(), r = silgiR();
      u.save(); u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      u.beginPath(); u.arc(d.imlec[0], d.imlec[1], r, 0, Math.PI * 2);
      u.lineWidth = 1.5; u.strokeStyle = 'rgba(17,26,46,.75)'; u.fillStyle = 'rgba(255,255,255,.35)'; u.fill(); u.stroke();
      u.restore();
    }

    // İki parmakla (dokunmatik) sayfa kaydırma: kalemi kapatmadan gezinme
    const dokunma = new Map();
    let pan = null;
    const orta = () => { const v = [...dokunma.values()]; return [(v[0][0] + v[1][0]) / 2, (v[0][1] + v[1][1]) / 2]; };
    const kaydirBy = (dx, dy) => { const s = { left: dx, top: dy, behavior: 'instant' }; if (kaydir === true) window.scrollBy(s); else if (kaydir) kaydir.scrollBy(s); };

    // Kalem açıkken kısa ve kıpırtısız dokunuş alttaki düğmeye, bağlantıya, etkinliğe geçer (çizgi bırakmaz);
    // sürükleyince çizilir. Fare tıklanabilir öğenin üstündeyken imleç el olur.
    const TIKLANIR = 'button, a[href], input, select, textarea, label, summary, [role="button"], .etk-kelime, .etk-bosluk-yer, [data-sol], [data-sag]';
    const alttaki = (x, y) => {
      const e = document.elementsFromPoint(x, y).find((e) => e !== ust && e !== alt && e !== kap);
      return e?.closest(TIKLANIR) || null;
    };
    let bas = null;

    let aktif = null;
    ust.addEventListener('pointerdown', (o) => {
      if (d.arac === 'el' || o.button > 0) return;
      o.preventDefault();
      try { ust.setPointerCapture(o.pointerId); } catch { /* yapay olay */ }
      if (o.pointerType === 'pen') kalemGoruldu = true;
      if (o.pointerType === 'touch') {
        dokunma.set(o.pointerId, [o.clientX, o.clientY]);
        if (dokunma.size >= 2) {                    // ikinci parmak: çizimi bırak, kaydırmaya geç
          if (d.canli) { d.canli = null; d.tahmin = null; iste(); }
          if (oturum) oturumKapat();
          aktif = null; pan = kaydir ? orta() : null; return;
        }
        // Avuç koruması: bu oturumda kalem kullanıldıysa parmak (avuç) çizmez; iki parmakla kaydırma sürer
        if (d.ayar.avuc && kalemGoruldu) return;
      }
      aktif = o.pointerId;
      bas = { x: o.clientX, y: o.clientY, t: performance.now(), uzak: 0 };
      const p = nokta(o);
      if (d.arac === 'silgi' || d.arac === 'cizgisil') { oturumAc(); sonSilgi = null; d.imlec = p; silgiUygula(p); iste(); return; }
      if (d.arac === 'isaretci') { d.isaret = [[p[0], p[1], performance.now()]]; iste(); return; }
      const arac = d.arac === 'kalem' && o.shiftKey ? 'dogru' : d.arac;   // Shift basılı kalem: düz çizgi
      d.canli = { arac, renk: d.renk, g: d.g * (arac === 'fosforlu' ? 3.2 : 1), n: SEKIL[arac] ? [p, p] : [p] };
      iste();
    });
    ust.addEventListener('pointermove', (o) => {
      if (dokunma.has(o.pointerId)) {
        dokunma.set(o.pointerId, [o.clientX, o.clientY]);
        if (pan && dokunma.size >= 2) { const m = orta(); kaydirBy(pan[0] - m[0], pan[1] - m[1]); pan = m; return; }
      }
      if (d.arac === 'silgi') { d.imlec = nokta(o); iste(); }
      if (aktif === null && o.pointerType === 'mouse' && (d.arac === 'kalem' || d.arac === 'fosforlu')) ust.style.cursor = alttaki(o.clientX, o.clientY) ? 'pointer' : 'crosshair';
      if (o.pointerId !== aktif) return;
      if (bas) bas.uzak = Math.max(bas.uzak, Math.hypot(o.clientX - bas.x, o.clientY - bas.y));
      const birlesik = o.getCoalescedEvents?.() || [];
      const olaylar = birlesik.length ? birlesik : [o];
      if (d.arac === 'silgi' || d.arac === 'cizgisil') { for (const e of olaylar) silgiUygula(nokta(e)); return; }
      if (d.arac === 'isaretci' && d.isaret) { const p = nokta(o); d.isaret.push([p[0], p[1], performance.now()]); if (d.isaret.length > 14) d.isaret.shift(); iste(); return; }
      if (!d.canli) return;
      if (SEKIL[d.canli.arac]) {                   // şekil: yalnız bitiş noktası değişir; Shift kare/daire ya da 45°'lik doğru
        const p = nokta(o), b = d.canli.n[0];
        if (o.shiftKey) {
          const dx = p[0] - b[0], dy = p[1] - b[1];
          if (d.canli.arac === 'dikdortgen' || d.canli.arac === 'elips') { const m = Math.max(Math.abs(dx), Math.abs(dy)); p[0] = b[0] + Math.sign(dx) * m; p[1] = b[1] + Math.sign(dy) * m; }
          else { const L = Math.hypot(dx, dy), aci = Math.round(Math.atan2(dy, dx) / (Math.PI / 4)) * (Math.PI / 4); p[0] = b[0] + L * Math.cos(aci); p[1] = b[1] + L * Math.sin(aci); }
        }
        d.canli.n = [b, p]; iste(); return;
      }
      // Çizgi düzeltme: her yeni nokta bir öncekine doğru çekilir; kızılötesi dokunmatik çerçevelerin titremesi azalır
      const alfa = d.ayar.duzelt ? (o.pointerType === 'pen' ? 0.75 : 0.55) : 1;
      for (const e of olaylar) {
        let p = nokta(e); const s = d.canli.n[d.canli.n.length - 1];
        if (alfa < 1 && d.canli.n.length > 1) p = [s[0] + (p[0] - s[0]) * alfa, s[1] + (p[1] - s[1]) * alfa, p[2]];
        if (Math.hypot(p[0] - s[0], p[1] - s[1]) > 0.8) d.canli.n.push(p);
      }
      d.tahmin = (o.getPredictedEvents?.() || []).slice(0, 3).map(nokta);
      iste();
    });
    const bitir = (o) => {
      dokunma.delete(o.pointerId);
      if (dokunma.size < 2) pan = null;
      if (o.pointerId !== aktif) return;
      aktif = null;
      const hedef = o.type === 'pointerup' && bas && bas.uzak < 6 && performance.now() - bas.t < 500 ? alttaki(o.clientX, o.clientY) : null;
      bas = null;
      if (d.isaret) { const iz = d.isaret; setTimeout(() => { if (d.isaret === iz) { d.isaret = null; iste(); } }, 500); }
      if (hedef && d.canli) { d.canli = null; d.tahmin = null; iste(); }
      if (oturum) { oturumKapat(); sonSilgi = null; }
      if (d.canli && !SEKIL[d.canli.arac] && o.type === 'pointerup') {   // düzeltme kalemin gerisinde kaldıysa çizgi tam bırakılan yerde biter
        const p = nokta(o), s = d.canli.n[d.canli.n.length - 1];
        if (Math.hypot(p[0] - s[0], p[1] - s[1]) > 0.8) d.canli.n.push(p);
      }
      d.tahmin = null;
      if (d.canli) {
        d.cizgiler.push(d.canli); d.gecmis.push({ tur: 'ekle', cizgi: d.canli }); d.ileri = [];
        cizgiCiz(d.canli, a, kay());
        d.canli = null; iste(); guncelle();
      }
      if (hedef) { if (hedef.matches('input, select, textarea')) hedef.focus(); hedef.click(); }
    };
    ust.addEventListener('pointerup', bitir);
    ust.addEventListener('pointercancel', bitir);
    ust.addEventListener('pointerleave', () => { if (d.imlec && aktif === null) { d.imlec = null; iste(); } });

    const geriAl = () => {
      const g = d.gecmis.pop(); if (!g) return;
      if (g.tur === 'ekle') d.cizgiler = d.cizgiler.filter((c) => c !== g.cizgi);
      else if (g.tur === 'degistir') { d.cizgiler = d.cizgiler.filter((c) => !g.yeni.includes(c)); d.cizgiler.push(...g.eski); }
      else d.cizgiler.push(...g.cizgiler);
      d.ileri.push(g); hepsiniCiz(); guncelle();
    };
    const yinele = () => {
      const g = d.ileri.pop(); if (!g) return;
      if (g.tur === 'ekle') d.cizgiler.push(g.cizgi);
      else if (g.tur === 'degistir') { d.cizgiler = d.cizgiler.filter((c) => !g.eski.includes(c)); d.cizgiler.push(...g.yeni); }
      else d.cizgiler = d.cizgiler.filter((c) => !g.cizgiler.includes(c));
      d.gecmis.push(g); hepsiniCiz(); guncelle();
    };
    const temizle = () => { if (!d.cizgiler.length) return; d.gecmis.push({ tur: 'sil', cizgiler: d.cizgiler }); d.cizgiler = []; d.ileri = []; hepsiniCiz(); guncelle(); };

    // Araç çubuğu
    const cubuk = document.createElement('div');
    cubuk.className = 'tahta-cubuk';
    cubuk.setAttribute('role', 'toolbar');
    cubuk.setAttribute('aria-label', 'Tahta araçları');
    const dugme = (ad, ic, is, ek = '') => `<button type="button" class="${ek}" data-${ad}="${is}" title="${ic.baslik}" aria-label="${ic.baslik}">${ic.html}</button>`;
    cubuk.innerHTML =
      `<div class="tahta-grup">${[['kalem', 'Kalem (K)'], ['fosforlu', 'Fosforlu kalem (F)'], ['silgi', 'Silgi: değdiği yeri siler (S)'], ['cizgisil', 'Çizgi silgisi: çizginin tamamını siler (Ç)'], ...(kaydir ? [['el', 'Sayfayı kaydır (E) — iki parmakla da kaydırabilirsiniz']] : [])]
        .map(([is, b]) => dugme('arac', { baslik: b, html: svg(ARAC_SIMGE[is]) }, is)).join('')}</div>` +
      `<div class="tahta-grup">` +
      dugme('is', { baslik: 'Geri al (Ctrl+Z)', html: svg('M9 14L4 9l5-5M4 9h10a6 6 0 010 12h-3') }, 'geri') +
      dugme('is', { baslik: 'İleri al (Ctrl+Y)', html: svg('M15 14l5-5-5-5M20 9H10a6 6 0 000 12h3') }, 'ileri') + `</div>` +
      `<div class="tahta-grup">${RENKLER.map((r, i) => dugme('renk', { baslik: `Renk ${i + 1}`, html: `<span style="background:${r}"></span>` }, r, 'renk')).join('')}</div>` +
      `<div class="tahta-grup">${Object.keys(KALINLIK).map((k) => dugme('kalinlik', { baslik: `Kalınlık: ${k}`, html: `<i style="width:${KALINLIK[k] + 2}px;height:${KALINLIK[k] + 2}px"></i>` }, k, 'kalin')).join('')}</div>` +
      `<div class="tahta-grup">` +
      dugme('is', { baslik: 'Araç kutusu: kalınlık, renkler, şekiller, hassasiyet (T)', html: svg(ARAC_SIMGE.kutu) }, 'kutu', 'kutu-dugme') +
      dugme('is', { baslik: 'Hepsini temizle', html: svg('M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3') }, 'temizle') +
      (kapat ? dugme('is', { baslik: 'Kalemi kapat (Esc)', html: svg('M6 6l12 12M18 6L6 18') }, 'kapat', 'kapat') : '') + `</div>`;
    // Araç kutusu: çubuğun üstünde açılır (çubukla birlikte ölçeklenir ve konumlanır)
    const kutuPanel = document.createElement('div');
    kutuPanel.className = 'tahta-kutu'; kutuPanel.id = `tahta-kutu-${Math.random().toString(36).slice(2, 8)}`;
    kutuPanel.setAttribute('role', 'group'); kutuPanel.setAttribute('aria-label', 'Kalem araç kutusu'); kutuPanel.hidden = true;
    const aracDugme = (is, ad) => `<button type="button" data-arac="${is}" title="${ad}">${svg(ARAC_SIMGE[is])}<span>${ad}</span></button>`;
    kutuPanel.innerHTML =
      `<div class="tk-bas"><strong>Araç kutusu</strong><button type="button" data-is="kutu-kapat" class="tk-kapat" aria-label="Araç kutusunu kapat">${svg('M6 6l12 12M18 6L6 18')}</button></div>` +
      `<div class="tk-bolum"><span class="tk-baslik">Kalınlık</span><div class="tk-satir"><span class="tk-onizle" aria-hidden="true"><i></i></span>` +
      `<input type="range" min="1" max="24" step="0.5" data-ayar="g" aria-label="Çizgi kalınlığı (piksel)"><output aria-live="off"></output></div></div>` +
      `<div class="tk-bolum"><span class="tk-baslik">Renk</span><div class="tk-satir"><div class="tk-renkler">${PALET.map((r, i) => dugme('renk', { baslik: `Renk ${i + 1}`, html: `<span style="background:${r}"></span>` }, r, 'renk')).join('')}</div>` +
      `<label class="tk-ozel">Özel <input type="color" data-ayar="renk" aria-label="Özel renk"></label></div></div>` +
      `<div class="tk-bolum"><span class="tk-baslik">Şekiller ve işaretçi</span><div class="tk-araclar">${Object.entries(SEKIL).map(([is, ad]) => aracDugme(is, ad)).join('')}${aracDugme('isaretci', 'İşaretçi')}</div>` +
      `<small>Kalemle çizerken Shift basılıysa düz çizgi; şekillerde Shift kare, daire ya da 45°'lik doğru verir.</small></div>` +
      `<div class="tk-bolum"><span class="tk-baslik">Hassasiyet</span><div class="tk-satir tk-secenekler">` +
      `<label title="El titremesini ve dokunmatik çerçeve kırıklığını azaltır"><input type="checkbox" data-ayar="duzelt"> Çizgi düzeltme</label>` +
      `<label title="Bu oturumda kalem kullanıldıysa parmak ve avuç çizmez; iki parmakla kaydırma sürer"><input type="checkbox" data-ayar="avuc"> Avuç koruması</label>` +
      `<label title="Basınç bildiren kalemlerde çizgi bastıkça kalınlaşır"><input type="checkbox" data-ayar="basinc"> Basınca duyarlı kalınlık</label></div></div>` +
      `<div class="tk-bolum"><span class="tk-baslik">Kısayollar</span><small>K kalem · F fosforlu · S silgi · Ç çizgi silgisi · D doğru · O ok · R dikdörtgen · A elips · İ işaretçi${kaydir ? ' · E el' : ''} · T araç kutusu · Ctrl+Z geri · Ctrl+Y ileri${kapat ? ' · Esc kapat' : ''}</small></div>`;
    cubuk.append(kutuPanel);
    kap.append(cubuk);
    sabitBoy(cubuk);
    const kutuDugme = cubuk.querySelector('[data-is=kutu]');
    kutuDugme.setAttribute('aria-expanded', 'false'); kutuDugme.setAttribute('aria-controls', kutuPanel.id);
    const kutuAc = (acik = kutuPanel.hidden) => {
      kutuPanel.hidden = !acik; kutuDugme.setAttribute('aria-expanded', String(acik)); kutuDugme.setAttribute('aria-pressed', String(acik));
      // Panel kabı aşmasın (tahta alanı overflow:hidden; 360×640'ta başlık ve kapat düğmesi kırpılıyordu)
      if (acik) kutuPanel.style.maxHeight = `${Math.max(180, (kap.getBoundingClientRect().height || innerHeight) - cubuk.offsetHeight - 26)}px`;
    };
    const surgu = kutuPanel.querySelector('[data-ayar=g]'), surguCikti = kutuPanel.querySelector('output'), onizle = kutuPanel.querySelector('.tk-onizle i');
    const guncelle = () => {
      cubuk.querySelectorAll('[data-arac]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.arac === d.arac)));
      cubuk.querySelectorAll('[data-renk]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.renk === d.renk)));
      cubuk.querySelectorAll('[data-kalinlik]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.kalinlik === d.kalinlik)));
      surgu.value = d.g; surguCikti.value = `${d.g} px`;
      const cap = Math.min(28, Math.max(3, d.g)); onizle.style.width = onizle.style.height = `${cap}px`; onizle.style.background = d.renk === '#ffffff' ? '#cdd5e3' : d.renk;
      kutuPanel.querySelector('[data-ayar=renk]').value = d.renk;
      for (const k of Object.keys(d.ayar)) kutuPanel.querySelector(`[data-ayar=${k}]`).checked = d.ayar[k];
      ust.style.pointerEvents = d.arac === 'el' ? 'none' : 'auto';
      ust.style.cursor = d.arac === 'silgi' || d.arac === 'isaretci' ? 'none' : d.arac === 'cizgisil' ? 'cell' : 'crosshair';
      const g = cubuk.querySelector('[data-is=geri]'), i = cubuk.querySelector('[data-is=ileri]');
      if (g) g.disabled = !d.gecmis.length;
      if (i) i.disabled = !d.ileri.length;
      if (d.arac !== 'silgi' && d.imlec) { d.imlec = null; iste(); }
    };
    cubuk.addEventListener('click', (o) => {
      const b = o.target.closest('button'); if (!b) return;
      if (b.dataset.arac) d.arac = b.dataset.arac;
      if (b.dataset.renk) { d.renk = b.dataset.renk; if (['silgi', 'cizgisil', 'el', 'isaretci'].includes(d.arac)) d.arac = 'kalem'; }
      if (b.dataset.kalinlik) { d.kalinlik = b.dataset.kalinlik; d.g = KALINLIK[d.kalinlik]; }
      if (b.dataset.is === 'geri') geriAl();
      if (b.dataset.is === 'ileri') yinele();
      if (b.dataset.is === 'temizle') temizle();
      if (b.dataset.is === 'kutu') kutuAc();
      if (b.dataset.is === 'kutu-kapat') kutuAc(false);
      if (b.dataset.is === 'kapat') kapat?.();
      if (b.dataset.arac || b.dataset.renk || b.dataset.kalinlik) ayarKaydet();
      guncelle();
    });
    kutuPanel.addEventListener('input', (o) => {
      const e = o.target; if (!e.dataset.ayar) return;
      if (e.dataset.ayar === 'g') { d.g = Math.max(1, Math.min(24, Number(e.value) || 5)); d.kalinlik = Object.keys(KALINLIK).find((k) => KALINLIK[k] === d.g) || 'ozel'; }
      else if (e.dataset.ayar === 'renk') { if (renkGecerli(e.value)) d.renk = e.value.toLowerCase(); if (['silgi', 'cizgisil', 'el', 'isaretci'].includes(d.arac)) d.arac = 'kalem'; }
      else d.ayar[e.dataset.ayar] = e.checked;
      ayarKaydet(); guncelle();
    });
    // Panel dışına tıklayınca kapanır (çubuk ve panel hariç)
    ust.addEventListener('pointerdown', () => { if (!kutuPanel.hidden) kutuAc(false); }, { capture: true });
    const tus = (o) => {
      // Gizli kalem ve sunumun arkasındaki sayfa kısayollara yanıt vermez.
      const modal = document.querySelector('dialog[open]');
      if (!kap.isConnected || kap.closest('[hidden]') || (modal && !modal.contains(kap))) return;
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)) return;
      const k = o.key.toLowerCase();
      if ((o.ctrlKey || o.metaKey) && k === 'z') { o.preventDefault(); o.shiftKey ? yinele() : geriAl(); return; }
      if ((o.ctrlKey || o.metaKey) && k === 'y') { o.preventDefault(); yinele(); return; }
      if (o.ctrlKey || o.metaKey || o.altKey) return;
      const kod = (o.code || '').replace(/^Key/, '').toLowerCase();   // İ/ı gibi harflerde fiziksel tuş
      const arac = { k: 'kalem', f: 'fosforlu', s: 'silgi', 'ç': 'cizgisil', e: kaydir ? 'el' : null, d: 'dogru', o: 'ok', r: 'dikdortgen', a: 'elips', i: 'isaretci', 'i̇': 'isaretci' }[k] || { i: 'isaretci' }[kod];
      if (arac) { d.arac = arac; guncelle(); ayarKaydet(); }
      if (k === 't' || kod === 't') kutuAc();
      if (k === 'escape') { if (!kutuPanel.hidden) kutuAc(false); else if (kapat) kapat(); }
    };
    document.addEventListener('keydown', tus);
    const olcu = new ResizeObserver(boyutla);
    olcu.observe(kap);
    const kaydirildi = () => { hepsiniCiz(); iste(); };
    const kaydirHedef = kaydir === true ? window : (kaydir || null);   // boş tahtada kaydırma yok
    kaydirHedef?.addEventListener('scroll', kaydirildi, { passive: true });
    // Kalem açıkken fare tekerleği alttaki kabı kaydırır.
    if (kaydir) ust.addEventListener('wheel', (o) => { o.preventDefault(); kaydirBy(o.deltaX, o.deltaY); }, { passive: false });
    boyutla(); guncelle();
    return {
      d, hepsiniCiz, geriAl, yinele, temizle,
      zemin: (z) => { d.zemin = z; hepsiniCiz(); },
      yukle: (cizgiler) => { d.cizgiler = cizgiler; d.gecmis = []; d.ileri = []; hepsiniCiz(); guncelle(); },
      png: () => alt.toDataURL('image/png'),
      // İndirilen görüntüde sağ alt köşede Ders Kutusu mührü ve adresi (kullanıcı 29.09: "indirilebilen her şeyin üzerinde logo olmalı")
      pngLogolu: () => new Promise((coz) => {
        const c = document.createElement('canvas'); c.width = alt.width; c.height = alt.height;
        const x = c.getContext('2d');
        x.fillStyle = '#fff'; x.fillRect(0, 0, c.width, c.height); x.drawImage(alt, 0, 0);
        const img = new Image();
        const bitir = () => {
          const b = 52 * oran, p = 14 * oran;
          try { x.drawImage(img, c.width - b - p, c.height - b - p, b, b); } catch { /* mühür yüklenemedi: yalnız adres */ }
          x.font = `700 ${13 * oran}px -apple-system, "Segoe UI", Roboto, Arial, sans-serif`;
          x.fillStyle = '#0b2257'; x.textAlign = 'right'; x.textBaseline = 'middle';
          x.fillText('derskutusu.com', c.width - b - p - 8 * oran, c.height - p - b / 2);
          coz(c.toDataURL('image/png'));
        };
        img.onload = bitir; img.onerror = bitir; img.src = '/simge-192.png';
      }),
      // Yakınlaştırmada çizgiler içerikle birlikte ölçeklenir.
      olcekle: (k) => {
        const hepsi = new Set([...d.cizgiler, ...[...d.gecmis, ...d.ileri].flatMap((g) => g.cizgiler || (g.cizgi ? [g.cizgi] : [...g.eski, ...g.yeni]))]);
        for (const c of hepsi) { c.g *= k; c.k = null; for (const q of c.n) { q[0] *= k; q[1] *= k; } }
        hepsiniCiz();
      },
      kaldir: () => { olcu.disconnect(); document.removeEventListener('keydown', tus); kaydirHedef?.removeEventListener('scroll', kaydirildi); alt.remove(); ust.remove(); cubuk.remove(); },
    };
  }
  return { olustur };
})();


// Kalem bandı ve kalem düğmesi sayfa büyütülünce büyümez (kullanıcı 01.10: "sayfayı büyüttüğümde kalem bandı çok büyüyor, sabit ve küçük kalsın").
// Tarayıcı yakınlaştırması (outerWidth / innerWidth) ve iki parmakla büyütme (visualViewport.scale) ters ölçeklenir;
// sabit konumlu öğe görünen alanın altına (bant ortada, düğme sağda) yerleştirilir, ekrandaki boyu ve kenar boşluğu değişmez.
const sabitBoy = typeof window === 'undefined' ? () => {} : (() => {
  const ogeler = new Map();
  const vv = window.visualViewport;
  const yakinlik = () => {
    const z = window.outerWidth && window.innerWidth ? window.outerWidth / window.innerWidth : 1;
    return !isFinite(z) || Math.abs(z - 1) < 0.07 ? 1 : z;   // pencere kenarı, kaydırma çubuğu ve kenar paneli küçük farkı yok sayılır
  };
  function uygula() {
    const g = 1 / (yakinlik() * (vv ? vv.scale : 1));
    const cw = document.documentElement.clientWidth, ch = document.documentElement.clientHeight;
    for (const [el, yatay] of ogeler) {
      if (!el.isConnected) { ogeler.delete(el); continue; }
      if (Math.abs(g - 1) < 0.01) { el.style.transform = el.style.transformOrigin = el.style.maxWidth = ''; continue; }
      const cs = getComputedStyle(el);
      const sabit = cs.position === 'fixed';
      const kenar = parseFloat(cs.bottom) || 16;
      let dx = 0, dy = 0;
      if (sabit && vv) {
        dx = yatay === 'sag' ? (vv.offsetLeft + vv.width - kenar * g) - (cw - kenar) : (vv.offsetLeft + vv.width / 2) - cw / 2;
        dy = (vv.offsetTop + vv.height - kenar * g) - (ch - kenar);
      }
      el.style.transformOrigin = yatay === 'sag' ? '100% 100%' : '50% 100%';
      el.style.transform = `translate(${dx.toFixed(1)}px, ${dy.toFixed(1)}px) scale(${g.toFixed(4)})`;
      if (yatay === 'orta') el.style.maxWidth = sabit && vv ? `${((vv.width - 24 * g) / g).toFixed(0)}px` : `calc((100% - 24px) / ${g.toFixed(4)})`;
    }
  }
  addEventListener('resize', uygula);         // resize ve visualViewport olayları zaten kare başına bir kez gelir
  vv?.addEventListener('resize', uygula);
  vv?.addEventListener('scroll', uygula);
  return (el, yatay = 'orta') => { ogeler.set(el, yatay); uygula(); };
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
      t.pngLogolu().then((adres) => { const a = document.createElement('a'); a.href = adres; a.download = `derskutusu-tahta-${no + 1}.png`; a.click(); });
    });
    // Tam ekran bütün tahta sayfasını alır: sayfa/zemin/kaydet düğmeleri ve çıkış görünür kalır
    const tamDugme = document.getElementById('t-tam'), tamHedef = document.querySelector('.tahta-sayfa') || document.getElementById('tahta-alan');
    tamDugme.addEventListener('click', () => (document.fullscreenElement ? document.exitFullscreen() : tamHedef.requestFullscreen?.()));
    document.addEventListener('fullscreenchange', () => { const acik = Boolean(document.fullscreenElement); tamDugme.lastChild.textContent = acik ? 'Tam ekrandan çık' : 'Tam ekran'; tamDugme.setAttribute('aria-pressed', String(acik)); });
    sayfaYaz();
  } else {
    // Öteki sayfalar: sağ altta kalem düğmesi → sayfanın üstüne yaz
    const ac = document.createElement('button');
    ac.type = 'button'; ac.className = 'kalem-dugme'; ac.title = 'Kalemle sayfaya yaz (akıllı tahta)'; ac.setAttribute('aria-label', 'Kalemle sayfaya yaz');
    ac.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Kalemle yaz</span>';
    document.body.append(ac);
    sabitBoy(ac, 'sag');
    let t = null, kap = null, kapHedef = null;
    const kapat = () => { if (kap) kap.hidden = true; ac.hidden = false; document.body.classList.remove('kalem-acik'); };
    // Belge değişince (goruntule.js yeni PDF çizer) katman DOM'dan düşer ya da hedef kap değişir: bir sonraki açılışta yeniden kurulur
    window.kalemKapat = () => { if (kap && !kap.hidden) kapat(); };
    ac.addEventListener('click', () => {
      const hedef = window.kalemHedef || null;   // goruntule.js PDF'i kendisi çizerse kabını bildirir
      if (kap && (!kap.isConnected || kapHedef !== hedef)) { kap.remove(); kap = null; t = null; window.kalemAcik = null; }
      if (!kap) {
        kapHedef = hedef;
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
      let gosterildi = false;
      try { gosterildi = localStorage.getItem('kalem-ipucu') === '1'; localStorage.setItem('kalem-ipucu', '1'); } catch { /* gizli pencere */ }
      if (!gosterildi) {
        const ip = document.createElement('div');
        ip.className = 'kalem-ipucu'; ip.setAttribute('role', 'status');
        ip.textContent = 'Kalemi kapatmadan sayfayı iki parmakla, fare tekerleğiyle ya da el aracıyla kaydırabilirsiniz.';
        kap.append(ip); setTimeout(() => ip.remove(), 6000);
      }
    });
    window.kalemAc = () => ac.click();
    // Konu sayfasının başlığındaki "Kalemle yaz" düğmesi ekrandayken sağ alttaki kopyası gizlenir (aynı işi iki düğme yapmaz).
    // goruntule.js düğmesini veri geldikten sonra kurar ve her çizişte kalemDugmeGozle ile bildirir.
    let gozcu = null;
    window.kalemDugmeGozle = (dugme) => {
      gozcu?.disconnect(); gozcu = null;
      if (!dugme || !('IntersectionObserver' in window)) { ac.classList.remove('gizli'); return; }
      gozcu = new IntersectionObserver(([g]) => ac.classList.toggle('gizli', g.isIntersecting));
      gozcu.observe(dugme);
    };
    window.kalemDugmeGozle(document.querySelector('button[onclick*="kalemAc"], [data-kalem-dugme]'));
  }
}

// Konu sayfalarındaki sunum, mevcut tahta ve etkinlik davranışlarını yeniden kullanır.
if (typeof document !== 'undefined' && document.querySelector('article.ozet')) {
  const ders = document.createElement('script');
  ders.src = '/ders-slayt.js?v=20261013-2';
  document.head.append(ders);
}
