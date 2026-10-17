// Akıllı tahta kalemi: her sayfada sayfanın (ya da belge görüntüleyicinin) üstüne yazma, tahta.html'de boş tahta.
// Hız ve hassasiyet: iki katman — biten çizgiler alt tuvalde, çizilmekte olan çizgi üst tuvalde requestAnimationFrame ile çizilir;
// çizgiler vektör olarak tutulur (geri al / yinele / silgi), kalem basıncı, hız uyumlu sönümleme (stabilizasyon),
// birleşik (coalesced) ve öngörülen (predicted) olaylar kullanılır.
// Dışarıdan hiçbir şey yüklenmez; çizimler yalnız bu tarayıcıda kalır.

const Tahta = (() => {
  const RENKLER = ['#111a2e', '#e62117', '#2451d6', '#12a150', '#f29f05', '#8b3fd6', '#00a3b4', '#ffffff'];
  const KALINLIK = { cokince: 1.4, ince: 2.5, orta: 4.5, kalin: 8.5, cokkalin: 14 };
  const KALINLIK_AD = {
    cokince: 'Çok ince (satır arası ve üs/indis için)',
    ince: 'İnce',
    orta: 'Orta',
    kalin: 'Kalın',
    cokkalin: 'Çok kalın (başlık ve vurgu için)',
  };
  const SILGI = { cokince: 5, ince: 9, orta: 16, kalin: 28, cokkalin: 42 }; // kısmi silginin yarıçapı (px)
  const SEKILLER = new Set(['cizgi', 'ok', 'dikdortgen', 'cember', 'ucgen', 'eksen']);
  const ARAC_SIMGE = {
    kalem: 'M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3',
    fosforlu: 'M6 14l6-6 4 4-6 6H6v-4zM4 20h16',
    kesikli: 'M4 17l3-3M9.5 11.5l3-3M15 6l3-3M3 21h4M10 21h4M17 21h4',
    lazer: 'M12 8a4 4 0 100 8 4 4 0 000-8zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1',
    silgi: 'M8 20h12M5 15l7-7 5 5-5 5H9l-4-3z',
    cizgisil: 'M3 16c3-4 6-4 9 0s6 4 9 0M9 6l6 6M15 6l-6 6',
    cizgi: 'M4 20L20 4M6 14l4 4M11 9l4 4',
    ok: 'M5 19L19 5M11 5h8v8',
    dikdortgen: 'M4 6h16v12H4z',
    cember: 'M12 4a8 8 0 100 16 8 8 0 000-16z',
    ucgen: 'M12 4L3 19h18L12 4z',
    eksen: 'M3 12h18M12 3v18M18 9l3 3-3 3M9 6l3-3 3 3',
    metin: 'M5 6V4h14v2M12 4v16M9 20h6',
    odak: 'M12 8a4 4 0 100 8 4 4 0 000-8zM3 12c2.5-5 5.8-7.5 9-7.5s6.5 2.5 9 7.5c-2.5 5-5.8 7.5-9 7.5s-6.5-2.5-9-7.5z',
    el: 'M8 13V6a1.5 1.5 0 013 0v5m0-6a1.5 1.5 0 013 0v6m0-5a1.5 1.5 0 013 0v7a6 6 0 01-6 6h-1a6 6 0 01-5-3l-2-4a1.5 1.5 0 012.5-1.5L8 15',
  };
  const svg = (d) => `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${d}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

  // Geometrik şekilleri silgi ve çarpışma testi için sık noktalı poliline dönüştürür
  function parcaOrnekle(x0, y0, x1, y1, adim = 4) {
    const L = Math.hypot(x1 - x0, y1 - y0), say = Math.max(1, Math.ceil(L / adim));
    const n = [];
    for (let i = 0; i <= say; i++) {
      const s = i / say;
      n.push([x0 + (x1 - x0) * s, y0 + (y1 - y0) * s, 1]);
    }
    return n;
  }

  function sekilNoktalari(c) {
    if (!c.bas || !c.son) return c.n || [];
    const [x0, y0] = c.bas, [x1, y1] = c.son;
    const tur = c.sekil || c.arac;
    if (tur === 'cizgi') return parcaOrnekle(x0, y0, x1, y1);
    if (tur === 'ok') {
      const n = parcaOrnekle(x0, y0, x1, y1);
      const L = Math.hypot(x1 - x0, y1 - y0);
      if (L > 4) {
        const aci = Math.atan2(y1 - y0, x1 - x0), boy = Math.min(22, Math.max(10, c.g * 3.2), L * 0.45);
        const sol = [x1 - boy * Math.cos(aci - Math.PI / 6), y1 - boy * Math.sin(aci - Math.PI / 6)];
        const sag = [x1 - boy * Math.cos(aci + Math.PI / 6), y1 - boy * Math.sin(aci + Math.PI / 6)];
        n.push(...parcaOrnekle(x1, y1, sol[0], sol[1]), ...parcaOrnekle(x1, y1, sag[0], sag[1]));
      }
      return n;
    }
    if (tur === 'dikdortgen') {
      return [
        ...parcaOrnekle(x0, y0, x1, y0),
        ...parcaOrnekle(x1, y0, x1, y1),
        ...parcaOrnekle(x1, y1, x0, y1),
        ...parcaOrnekle(x0, y1, x0, y0),
      ];
    }
    if (tur === 'cember') {
      const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
      const rx = Math.abs(x1 - x0) / 2, ry = Math.abs(y1 - y0) / 2;
      const cevre = Math.PI * (3 * (rx + ry) - Math.sqrt((3 * rx + ry) * (rx + 3 * ry)));
      const say = Math.max(24, Math.min(180, Math.ceil(cevre / 4)));
      const n = [];
      for (let i = 0; i <= say; i++) {
        const a = (i / say) * Math.PI * 2;
        n.push([cx + Math.cos(a) * rx, cy + Math.sin(a) * ry, 1]);
      }
      return n;
    }
    if (tur === 'ucgen') {
      const ustX = c.dik ? x0 : (x0 + x1) / 2;
      return [
        ...parcaOrnekle(ustX, y0, x1, y1),
        ...parcaOrnekle(x1, y1, x0, y1),
        ...parcaOrnekle(x0, y1, ustX, y0),
      ];
    }
    if (tur === 'eksen') {
      const dx = Math.abs(x1 - x0), dy = Math.abs(y1 - y0);
      if (dy < 26 || dy < dx * 0.22) {
        return parcaOrnekle(x0, y0, x1, y0);
      }
      const ox = (x0 + x1) / 2, oy = (y0 + y1) / 2;
      return [...parcaOrnekle(x0, oy, x1, oy), ...parcaOrnekle(ox, y0, ox, y1)];
    }
    return c.n || [];
  }

  function olustur({ kap, kaydir = false, zemin = null, kapat = null }) {
    // kap: tuvallerin konacağı öğe; kaydir: true → çizgiler sayfa kaydırmasıyla, öğe → o öğenin (ör. PDF kabı) kaydırmasıyla kayar
    const alt = document.createElement('canvas');
    const ust = document.createElement('canvas');
    alt.className = 'tahta-tuval'; ust.className = 'tahta-tuval tahta-ust';
    kap.append(alt, ust);
    const a = alt.getContext('2d'), u = ust.getContext('2d');
    const d = {
      arac: 'kalem', renk: RENKLER[1], kalinlik: 'orta',
      cizgiler: [], ileri: [], gecmis: [],
      canli: null, tahmin: [], lazerIz: [],
      imlec: null, istek: 0, zemin,
    };
    let oran = 1, gen = 0, yuk = 0;

    const kay = () => (kaydir === true ? { x: scrollX, y: scrollY } : kaydir ? { x: kaydir.scrollLeft, y: kaydir.scrollTop } : { x: 0, y: 0 });
    function boyutla() {
      const r = kap.getBoundingClientRect();
      oran = Math.min(window.devicePixelRatio || 1, 3);
      gen = r.width; yuk = r.height;
      for (const t of [alt, ust]) { t.width = Math.round(gen * oran); t.height = Math.round(yuk * oran); t.style.width = gen + 'px'; t.style.height = yuk + 'px'; }
      hepsiniCiz();
    }
    function zeminCiz() {
      a.save();
      a.setTransform(oran, 0, 0, oran, 0, 0);
      if (d.zemin) {
        const koyuMu = d.zemin === 'koyu';
        a.fillStyle = koyuMu ? '#132620' : '#fdfdfb';
        a.fillRect(0, 0, gen, yuk);
        a.strokeStyle = koyuMu ? 'rgba(255,255,255,.08)' : 'rgba(36,81,214,.15)';
        a.fillStyle = koyuMu ? 'rgba(255,255,255,.22)' : 'rgba(36,81,214,.28)';
        a.lineWidth = 1;
        const aralik = 28;
        if (d.zemin === 'kareli' || d.zemin === 'cizgili' || d.zemin === 'koyu') {
          a.beginPath();
          for (let y = aralik; y < yuk; y += aralik) { a.moveTo(0, y + .5); a.lineTo(gen, y + .5); }
          if (d.zemin !== 'cizgili') for (let x = aralik; x < gen; x += aralik) { a.moveTo(x + .5, 0); a.lineTo(x + .5, yuk); }
          a.stroke();
        } else if (d.zemin === 'noktali') {
          for (let y = aralik; y < yuk; y += aralik) for (let x = aralik; x < gen; x += aralik) a.fillRect(x - 1, y - 1, 2, 2);
        } else if (d.zemin === 'izometrik') {
          const dy = aralik * Math.sin(Math.PI / 3);
          let satir = 0;
          for (let y = dy; y < yuk; y += dy, satir++) {
            const kayma = (satir % 2) * (aralik / 2);
            for (let x = aralik / 2 + kayma; x < gen; x += aralik) {
              a.beginPath(); a.arc(x, y, 1.3, 0, Math.PI * 2); a.fill();
            }
          }
        } else if (d.zemin === 'koordinat' || d.zemin === 'birim-cember') {
          const ox = Math.round(gen / (2 * aralik)) * aralik + 0.5;
          const oy = Math.round(yuk / (2 * aralik)) * aralik + 0.5;
          a.beginPath();
          for (let x = ox % aralik; x < gen; x += aralik) { a.moveTo(x, 0); a.lineTo(x, yuk); }
          for (let y = oy % aralik; y < yuk; y += aralik) { a.moveTo(0, y); a.lineTo(gen, y); }
          a.stroke();
          a.strokeStyle = 'rgba(17,26,46,.55)'; a.fillStyle = 'rgba(17,26,46,.65)'; a.lineWidth = 1.8;
          a.beginPath(); a.moveTo(0, oy); a.lineTo(gen, oy); a.moveTo(ox, 0); a.lineTo(ox, yuk); a.stroke();
          for (let x = ox + aralik; x < gen - 12; x += aralik) { a.beginPath(); a.moveTo(x, oy - 4); a.lineTo(x, oy + 4); a.stroke(); }
          for (let x = ox - aralik; x > 12; x -= aralik) { a.beginPath(); a.moveTo(x, oy - 4); a.lineTo(x, oy + 4); a.stroke(); }
          for (let y = oy + aralik; y < yuk - 12; y += aralik) { a.beginPath(); a.moveTo(ox - 4, y); a.lineTo(ox + 4, y); a.stroke(); }
          for (let y = oy - aralik; y > 12; y -= aralik) { a.beginPath(); a.moveTo(ox - 4, y); a.lineTo(ox + 4, y); a.stroke(); }
          if (d.zemin === 'birim-cember') {
            const r = aralik * 5;
            a.strokeStyle = 'rgba(36,81,214,.45)'; a.lineWidth = 2;
            a.beginPath(); a.arc(ox, oy, r, 0, Math.PI * 2); a.stroke();
          }
        } else if (d.zemin === 'sayidogrusu') {
          const satirArasi = 110;
          a.strokeStyle = 'rgba(17,26,46,.45)'; a.fillStyle = 'rgba(17,26,46,.6)'; a.lineWidth = 1.6;
          a.font = '600 11px -apple-system, "Segoe UI", Roboto, Arial, sans-serif'; a.textAlign = 'center';
          const ox = Math.round(gen / 2);
          for (let y = 70; y < yuk - 30; y += satirArasi) {
            a.beginPath(); a.moveTo(36, y); a.lineTo(gen - 36, y);
            a.moveTo(44, y - 5); a.lineTo(36, y); a.lineTo(44, y + 5);
            a.moveTo(gen - 44, y - 5); a.lineTo(gen - 36, y); a.lineTo(gen - 44, y + 5);
            a.stroke();
            const adim = 42, adet = Math.floor((gen - 110) / (2 * adim));
            for (let i = -adet; i <= adet; i++) {
              const x = ox + i * adim;
              a.beginPath(); a.moveTo(x, y - (i === 0 ? 7 : 4)); a.lineTo(x, y + (i === 0 ? 7 : 4)); a.stroke();
              a.fillText(String(i), x, y + 19);
            }
          }
        } else if (d.zemin === 'muzik') {
          a.strokeStyle = 'rgba(17,26,46,.28)'; a.lineWidth = 1;
          for (let blok = 44; blok < yuk - 60; blok += 92) {
            a.beginPath();
            for (let s = 0; s < 5; s++) {
              const y = blok + s * 10 + 0.5;
              a.moveTo(28, y); a.lineTo(gen - 28, y);
            }
            a.stroke();
          }
        }
      }
      a.restore();
    }

    function okUcuCiz(t, x0, y0, x1, y1, g) {
      const L = Math.hypot(x1 - x0, y1 - y0);
      if (L < 4) return;
      const aci = Math.atan2(y1 - y0, x1 - x0), boy = Math.min(22, Math.max(10, g * 3.2), L * 0.45);
      t.beginPath();
      t.moveTo(x1 - boy * Math.cos(aci - Math.PI / 6), y1 - boy * Math.sin(aci - Math.PI / 6));
      t.lineTo(x1, y1);
      t.lineTo(x1 - boy * Math.cos(aci + Math.PI / 6), y1 - boy * Math.sin(aci + Math.PI / 6));
      t.stroke();
    }

    function sekilCiz(c, t) {
      const [x0, y0] = c.bas, [x1, y1] = c.son;
      const tur = c.sekil || c.arac;
      t.lineWidth = c.g;
      if (tur === 'cizgi') {
        t.beginPath(); t.moveTo(x0, y0); t.lineTo(x1, y1); t.stroke();
      } else if (tur === 'ok') {
        t.beginPath(); t.moveTo(x0, y0); t.lineTo(x1, y1); t.stroke();
        okUcuCiz(t, x0, y0, x1, y1, c.g);
      } else if (tur === 'dikdortgen') {
        t.beginPath(); t.rect(Math.min(x0, x1), Math.min(y0, y1), Math.abs(x1 - x0), Math.abs(y1 - y0)); t.stroke();
      } else if (tur === 'cember') {
        const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, rx = Math.abs(x1 - x0) / 2, ry = Math.abs(y1 - y0) / 2;
        t.beginPath(); t.ellipse(cx, cy, rx, ry, 0, 0, Math.PI * 2); t.stroke();
      } else if (tur === 'ucgen') {
        const ustX = c.dik ? x0 : (x0 + x1) / 2;
        t.beginPath(); t.moveTo(ustX, y0); t.lineTo(x1, y1); t.lineTo(x0, y1); t.closePath(); t.stroke();
        if (c.dik && Math.abs(x1 - x0) > 20 && Math.abs(y1 - y0) > 20) {
          const b = Math.min(14, Math.abs(x1 - x0) * 0.25, Math.abs(y1 - y0) * 0.25);
          const sx = x1 >= x0 ? 1 : -1, sy = y1 >= y0 ? -1 : 1;
          t.save(); t.lineWidth = Math.max(1.2, c.g * 0.65);
          t.beginPath(); t.moveTo(x0 + sx * b, y1); t.lineTo(x0 + sx * b, y1 + sy * b); t.lineTo(x0, y1 + sy * b); t.stroke();
          t.restore();
        }
      } else if (tur === 'eksen') {
        const dx = Math.abs(x1 - x0), dy = Math.abs(y1 - y0);
        const adim = 36, tBoy = Math.max(4, c.g * 1.4);
        if (dy < 26 || dy < dx * 0.22) {
          // Tek boyutlu bölmeli sayı doğrusu
          t.beginPath(); t.moveTo(x0, y0); t.lineTo(x1, y0); t.stroke();
          okUcuCiz(t, x1, y0, x0, y0, c.g * 0.85);
          okUcuCiz(t, x0, y0, x1, y0, c.g * 0.85);
          const ox = (x0 + x1) / 2, yari = Math.floor(dx / (2 * adim));
          t.beginPath();
          for (let i = -yari; i <= yari; i++) {
            const x = ox + i * adim, h = i === 0 ? tBoy * 1.45 : tBoy;
            t.moveTo(x, y0 - h); t.lineTo(x, y0 + h);
          }
          t.stroke();
        } else {
          // İki boyutlu dik koordinat ekseni
          const sol = Math.min(x0, x1), sag = Math.max(x0, x1), ustY = Math.min(y0, y1), altY = Math.max(y0, y1);
          const ox = (sol + sag) / 2, oy = (ustY + altY) / 2;
          t.beginPath(); t.moveTo(sol, oy); t.lineTo(sag, oy); t.moveTo(ox, altY); t.lineTo(ox, ustY); t.stroke();
          okUcuCiz(t, sol, oy, sag, oy, c.g * 0.85);
          okUcuCiz(t, ox, altY, ox, ustY, c.g * 0.85);
          t.beginPath();
          for (let x = ox + adim; x < sag - 12; x += adim) { t.moveTo(x, oy - tBoy); t.lineTo(x, oy + tBoy); }
          for (let x = ox - adim; x > sol + 12; x -= adim) { t.moveTo(x, oy - tBoy); t.lineTo(x, oy + tBoy); }
          for (let y = oy + adim; y < altY - 12; y += adim) { t.moveTo(ox - tBoy, y); t.lineTo(ox + tBoy, y); }
          for (let y = oy - adim; y > ustY + 12; y -= adim) { t.moveTo(ox - tBoy, y); t.lineTo(ox + tBoy, y); }
          t.stroke();
        }
      }
    }

    function olcuEtiketiCiz(c, t) {
      if (!c.bas || !c.son) return;
      const [x0, y0] = c.bas, [x1, y1] = c.son;
      const dx = x1 - x0, dy = y1 - y0, L = Math.round(Math.hypot(dx, dy));
      if (L < 12) return;
      const tur = c.sekil || c.arac;
      let yazi = '';
      if (tur === 'cizgi' || tur === 'ok') {
        let derece = Math.round((-Math.atan2(dy, dx) * 180) / Math.PI);
        if (derece < 0) derece += 360;
        yazi = `${L} px · ${derece}°`;
      } else {
        yazi = `${Math.round(Math.abs(dx))} × ${Math.round(Math.abs(dy))} px`;
      }
      const mx = (x0 + x1) / 2, my = (y0 + y1) / 2 - 18;
      t.save();
      t.font = '600 12px -apple-system, "Segoe UI", Roboto, Arial, sans-serif';
      const w = t.measureText(yazi).width + 14;
      t.fillStyle = 'rgba(17,26,46,.86)';
      t.beginPath(); t.roundRect ? t.roundRect(mx - w / 2, my - 11, w, 22, 6) : t.rect(mx - w / 2, my - 11, w, 22); t.fill();
      t.fillStyle = '#fff'; t.textAlign = 'center'; t.textBaseline = 'middle';
      t.fillText(yazi, mx, my);
      t.restore();
    }

    function egriCiz(n, g, t) {
      t.lineWidth = g; t.beginPath(); t.moveTo(n[0][0], n[0][1]);
      for (let i = 1; i < n.length - 1; i++) t.quadraticCurveTo(n[i][0], n[i][1], (n[i][0] + n[i + 1][0]) / 2, (n[i][1] + n[i + 1][1]) / 2);
      t.lineTo(n[n.length - 1][0], n[n.length - 1][1]); t.stroke();
    }

    function cizgiCiz(c, t, k, tahmin = null) {
      const n = tahmin && tahmin.length ? [...c.n, ...tahmin] : c.n;
      if (!n.length && !c.sekil && !c.metin) return;
      t.save();
      t.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      t.lineCap = 'round'; t.lineJoin = 'round';
      t.strokeStyle = c.renk; t.fillStyle = c.renk;
      t.globalAlpha = c.arac === 'fosforlu' ? 0.32 : 1;

      if (c.metin && c.bas) {
        const boy = Math.round(c.boy || Math.max(16, c.g * 4.2));
        t.font = `700 ${boy}px -apple-system, "Segoe UI", Roboto, Arial, sans-serif`;
        t.textBaseline = 'top';
        const satirlar = c.metin.split('\n');
        satirlar.forEach((s, i) => t.fillText(s, c.bas[0], c.bas[1] + i * (boy * 1.25)));
        t.restore();
        return;
      }

      if (c.sekil && !c.parca && c.bas && c.son) {
        sekilCiz(c, t);
        if (t === u && d.canli === c) olcuEtiketiCiz(c, t);
        t.restore();
        return;
      }

      if (n.length === 1) {
        t.beginPath();
        t.arc(n[0][0], n[0][1], Math.max(0.8, c.g * (c.arac === 'fosforlu' ? 1 : n[0][2]) / 2), 0, Math.PI * 2);
        t.fill(); t.restore(); return;
      }
      if (c.arac === 'fosforlu') {
        // Fosforlu tek yol olarak çizilir: üst üste binen yerler koyulaşmaz.
        egriCiz(n, c.g, t);
      } else if (c.arac === 'kesikli') {
        t.setLineDash([Math.max(5, c.g * 2.2), Math.max(4, c.g * 1.7)]);
        egriCiz(n, c.g, t);
      } else {
        // Hassas kalem: basınca ve hıza göre değişen kalınlık, orta noktalardan geçen yumuşak kuadratik eğriler.
        for (let i = 1; i < n.length; i++) {
          const p0 = i > 1 ? [(n[i - 2][0] + n[i - 1][0]) / 2, (n[i - 2][1] + n[i - 1][1]) / 2] : n[0];
          const p1 = [(n[i - 1][0] + n[i][0]) / 2, (n[i - 1][1] + n[i][1]) / 2];
          t.lineWidth = Math.max(0.6, c.g * (n[i - 1][2] + n[i][2]) / 2);
          t.beginPath(); t.moveTo(p0[0], p0[1]); t.quadraticCurveTo(n[i - 1][0], n[i - 1][1], p1[0], p1[1]); t.stroke();
        }
        const s = n[n.length - 1], o = n[n.length - 2];
        t.lineWidth = Math.max(0.6, c.g * s[2]);
        t.beginPath(); t.moveTo((o[0] + s[0]) / 2, (o[1] + s[1]) / 2); t.lineTo(s[0], s[1]); t.stroke();
      }
      t.restore();
    }

    function hepsiniCiz() {
      a.setTransform(1, 0, 0, 1, 0, 0); a.clearRect(0, 0, alt.width, alt.height);
      zeminCiz();
      const k = kay();
      for (const c of d.cizgiler) cizgiCiz(c, a, k);
    }

    function lazerCiz(k, simdi) {
      d.lazerIz = d.lazerIz.filter((p) => simdi - p[2] < 1100);
      if (!d.lazerIz.length && (!d.imlec || d.arac !== 'lazer')) return;
      u.save();
      u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      u.lineCap = 'round'; u.lineJoin = 'round';
      for (let i = 1; i < d.lazerIz.length; i++) {
        const o = d.lazerIz[i - 1], p = d.lazerIz[i];
        if (p[3]) continue; // yeni iz başlangıcı
        const yas = Math.max(0, 1 - (simdi - p[2]) / 1100);
        u.strokeStyle = `rgba(255, 34, 20, ${yas * 0.45})`;
        u.lineWidth = 10 * yas + 2;
        u.beginPath(); u.moveTo(o[0], o[1]); u.lineTo(p[0], p[1]); u.stroke();
        u.strokeStyle = `rgba(255, 235, 230, ${yas * 0.95})`;
        u.lineWidth = 3.2 * yas + 0.8;
        u.beginPath(); u.moveTo(o[0], o[1]); u.lineTo(p[0], p[1]); u.stroke();
      }
      if (d.imlec && d.arac === 'lazer') {
        const [lx, ly] = d.imlec;
        u.fillStyle = 'rgba(255, 34, 20, 0.32)';
        u.beginPath(); u.arc(lx, ly, 12, 0, Math.PI * 2); u.fill();
        u.fillStyle = '#ff2214';
        u.beginPath(); u.arc(lx, ly, 5, 0, Math.PI * 2); u.fill();
        u.fillStyle = '#ffffff';
        u.beginPath(); u.arc(lx, ly, 2, 0, Math.PI * 2); u.fill();
      }
      u.restore();
      if (d.lazerIz.length) iste();
    }

    function odakCiz(k) {
      if (d.arac !== 'odak' || !d.imlec) return;
      const [ox, oy] = d.imlec;
      const r = SILGI[d.kalinlik] * 5.2 + 45;
      u.save();
      u.setTransform(oran, 0, 0, oran, 0, 0);
      u.fillStyle = 'rgba(11, 18, 32, 0.62)';
      u.fillRect(0, 0, gen, yuk);
      const sx = ox - k.x, sy = oy - k.y;
      u.globalCompositeOperation = 'destination-out';
      const grd = u.createRadialGradient(sx, sy, r * 0.72, sx, sy, r);
      grd.addColorStop(0, 'rgba(0,0,0,1)');
      grd.addColorStop(1, 'rgba(0,0,0,0)');
      u.fillStyle = grd;
      u.beginPath(); u.arc(sx, sy, r, 0, Math.PI * 2); u.fill();
      u.globalCompositeOperation = 'source-over';
      u.strokeStyle = 'rgba(255, 255, 255, 0.65)';
      u.lineWidth = 2;
      u.beginPath(); u.arc(sx, sy, r * 0.86, 0, Math.PI * 2); u.stroke();
      u.restore();
    }

    function canliCiz() {
      d.istek = 0;
      u.setTransform(1, 0, 0, 1, 0, 0); u.clearRect(0, 0, ust.width, ust.height);
      const k = kay(), simdi = performance.now();
      if (d.arac === 'odak') odakCiz(k);
      if (d.canli) cizgiCiz(d.canli, u, k, d.tahmin);
      if (d.lazerIz.length || d.arac === 'lazer') lazerCiz(k, simdi);
      imlecCiz(k);
    }
    const iste = () => { if (!d.istek) d.istek = requestAnimationFrame(canliCiz); };

    // Hassas nokta yakalama: kalem basıncı + fare/dokunmatik hızına duyarlı doğal uç inceltme
    let sonZaman = 0, sonHam = null;
    function nokta(o, ilk = false) {
      const r = kap.getBoundingClientRect(), k = kay();
      const x = o.clientX - r.left + k.x, y = o.clientY - r.top + k.y;
      const t = o.timeStamp || performance.now();
      let b = 1;
      if (o.pointerType === 'pen') {
        const hamB = Math.min(1.75, Math.max(0.22, (o.pressure || 0.5) * 1.65));
        b = ilk || !sonHam ? hamB : sonHam[2] * 0.35 + hamB * 0.65;
      } else if (!ilk && sonHam && t > sonZaman) {
        const hiz = Math.hypot(x - sonHam[0], y - sonHam[1]) / Math.max(1, t - sonZaman); // px/ms
        const hedefB = Math.max(0.78, Math.min(1.12, 1.08 - hiz * 0.12));
        b = sonHam[2] * 0.65 + hedefB * 0.35;
      }
      sonZaman = t;
      sonHam = [x, y, b];
      return [x, y, b];
    }

    // Yavaş yazarken (üs, indis, karekök, küçük harf) el titremesini sönümleyen hız-uyumlu filtre
    function yumusat(onceki, yeni) {
      if (!onceki) return yeni;
      const mesafe = Math.hypot(yeni[0] - onceki[0], yeni[1] - onceki[1]);
      // Küçük harekette yüksek sönümleme (pürüzsüz harf), hızlı harekette sıfıra yakın gecikme
      const alfa = Math.min(0.88, Math.max(0.5, 0.46 + mesafe * 0.06));
      return [
        onceki[0] + (yeni[0] - onceki[0]) * alfa,
        onceki[1] + (yeni[1] - onceki[1]) * alfa,
        onceki[2] + (yeni[2] - onceki[2]) * 0.6,
      ];
    }

    // Cetvel, ok ve şekiller için açı/oran kilitleme (Shift tuşu ya da ana açılara yakınlık)
    function sekilHedef(basNokta, sonNokta, arac, shift) {
      let [x0, y0] = basNokta, [x1, y1] = sonNokta;
      const dx = x1 - x0, dy = y1 - y0;
      if (arac === 'cizgi' || arac === 'ok') {
        const L = Math.hypot(dx, dy);
        if (L > 6) {
          const aci = Math.atan2(dy, dx), adim = Math.PI / 4;
          const enYakin = Math.round(aci / adim) * adim;
          // Shift basılıysa 45° katlarına, değilse yatay/dikey eksene 3° yaklaşınca mıknatıslanır
          const fark = Math.abs(aci - enYakin);
          const dikVeyaYatay = Math.abs(Math.sin(enYakin)) < 0.01 || Math.abs(Math.cos(enYakin)) < 0.01;
          if (shift || (dikVeyaYatay && fark < (3.2 * Math.PI) / 180)) {
            x1 = x0 + Math.cos(enYakin) * L;
            y1 = y0 + Math.sin(enYakin) * L;
          }
        }
      } else if ((arac === 'dikdortgen' || arac === 'cember') && shift) {
        const m = Math.max(Math.abs(dx), Math.abs(dy));
        x1 = x0 + (dx >= 0 ? m : -m);
        y1 = y0 + (dy >= 0 ? m : -m);
      }
      return [x1, y1];
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
        for (const q of c.n) { if (q[0] < x0) x0 = q[0]; if (q[0] > x1) x1 = q[0]; if (q[1] < y0) y0 = q[1]; if (q[1] > y1) y1 = q[1]; }
        const pay = (c.g || 4) + 4;
        c.k = [x0 - pay, y0 - pay, x1 + pay, y1 + pay];
      }
      return c.k;
    }
    const yakin = (c, p, r) => { const k = kutu(c); return !(p[0] < k[0] - r || p[0] > k[2] + r || p[1] < k[1] - r || p[1] > k[3] + r); };
    // Kısmi silgi: yalnız silginin değdiği kısmı siler; çizgi gerekirse ikiye bölünür.
    function kismiSil(p) {
      const r = SILGI[d.kalinlik];
      let degisti = false;
      const sonuc = [];
      for (const c of d.cizgiler) {
        if (!yakin(c, p, r)) { sonuc.push(c); continue; }
        if (c.metin) {
          const vur = c.n.some((q) => Math.hypot(q[0] - p[0], q[1] - p[1]) < r + 8);
          if (vur) { degisti = true; cikar(c); } else sonuc.push(c);
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
          const yeni = { arac: c.arac === 'fosforlu' || c.arac === 'kesikli' ? c.arac : 'kalem', renk: c.renk, g: c.g, n: pn, parca: true };
          sonuc.push(yeni); oturum.yeni.add(yeni);
        }
      }
      if (degisti) { d.cizgiler = sonuc; hepsiniCiz(); }
    }
    // Çizgi silgisi: dokunulan çizgiyi ya da şekli bütünüyle siler.
    function cizgiSil(p) {
      const esik = 12, once = d.cizgiler.length;
      d.cizgiler = d.cizgiler.filter((c) => {
        if (!yakin(c, p, esik)) return true;
        const vur = c.n.some((q, i) => {
          const r = i ? c.n[i - 1] : q;
          const dx = q[0] - r[0], dy = q[1] - r[1], L = dx * dx + dy * dy;
          const s = L ? Math.max(0, Math.min(1, ((p[0] - r[0]) * dx + (p[1] - r[1]) * dy) / L)) : 0;
          return Math.hypot(p[0] - (r[0] + s * dx), p[1] - (r[1] + s * dy)) < esik + c.g / 2;
        });
        if (vur) cikar(c);
        return !vur;
      });
      if (d.cizgiler.length !== once) hepsiniCiz();
    }
    let sonSilgi = null;
    function silgiUygula(p) {
      // Hızlı harekette aradaki yerler de silinsin: son noktadan bu noktaya küçük adımlarla ilerle.
      const adim = Math.max(3, (d.arac === 'silgi' ? SILGI[d.kalinlik] : 12) / 2);
      const s = sonSilgi || p, L = Math.hypot(p[0] - s[0], p[1] - s[1]), say = Math.max(1, Math.ceil(L / adim));
      for (let i = 1; i <= say; i++) {
        const q = [s[0] + (p[0] - s[0]) * i / say, s[1] + (p[1] - s[1]) * i / say, 1];
        d.arac === 'silgi' ? kismiSil(q) : cizgiSil(q);
      }
      sonSilgi = p;
    }

    // Canlı imleç: silgide silme halkası, kalemde/fosforluda hassas uç boyutu önizlemesi
    function imlecCiz(k = kay()) {
      if (!d.imlec) return;
      if (d.arac === 'silgi') {
        const r = SILGI[d.kalinlik];
        u.save(); u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
        u.beginPath(); u.arc(d.imlec[0], d.imlec[1], r, 0, Math.PI * 2);
        u.lineWidth = 1.5; u.strokeStyle = 'rgba(17,26,46,.75)'; u.fillStyle = 'rgba(255,255,255,.35)'; u.fill(); u.stroke();
        u.restore();
      } else if (d.arac === 'kalem' || d.arac === 'fosforlu' || d.arac === 'kesikli') {
        const r = Math.max(1.5, (KALINLIK[d.kalinlik] * (d.arac === 'fosforlu' ? 3.2 : 1)) / 2);
        u.save(); u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
        u.beginPath(); u.arc(d.imlec[0], d.imlec[1], r, 0, Math.PI * 2);
        u.fillStyle = d.renk; u.globalAlpha = d.arac === 'fosforlu' ? 0.38 : 0.78; u.fill();
        u.globalAlpha = 0.9; u.lineWidth = 1;
        u.strokeStyle = d.renk.toLowerCase() === '#ffffff' ? '#111a2e' : 'rgba(255,255,255,.9)';
        u.stroke();
        u.restore();
      }
    }

    // Metin / etiket ekleme kutusu
    let aktifGirdi = null;
    function metinKutusuAc(p, clientX, clientY) {
      if (aktifGirdi) aktifGirdi.blur();
      const r = kap.getBoundingClientRect();
      const boy = Math.round(Math.max(16, KALINLIK[d.kalinlik] * 4.2));
      const girdi = document.createElement('textarea');
      girdi.className = 'tahta-metin-girdi';
      girdi.rows = 1;
      girdi.placeholder = 'Metin yazın…';
      girdi.style.left = `${Math.max(8, Math.min(r.width - 140, clientX - r.left))}px`;
      girdi.style.top = `${Math.max(8, Math.min(r.height - 48, clientY - r.top - boy / 2))}px`;
      girdi.style.font = `700 ${boy}px -apple-system, "Segoe UI", Roboto, Arial, sans-serif`;
      girdi.style.color = d.renk;
      kap.append(girdi);
      aktifGirdi = girdi;
      setTimeout(() => girdi.focus(), 10);

      let kaydedildi = false;
      const kaydet = () => {
        if (kaydedildi) return;
        kaydedildi = true;
        aktifGirdi = null;
        const yazi = girdi.value.trim();
        girdi.remove();
        if (!yazi) return;
        const satirlar = yazi.split('\n');
        const enUzun = Math.max(...satirlar.map((s) => s.length));
        const genTahmin = Math.max(24, enUzun * boy * 0.58);
        const yukTahmin = satirlar.length * boy * 1.25;
        const n = [
          ...parcaOrnekle(p[0], p[1], p[0] + genTahmin, p[1], 6),
          ...parcaOrnekle(p[0], p[1] + yukTahmin / 2, p[0] + genTahmin, p[1] + yukTahmin / 2, 6),
          ...parcaOrnekle(p[0], p[1] + yukTahmin, p[0] + genTahmin, p[1] + yukTahmin, 6),
        ];
        const yeni = { arac: 'metin', metin: yazi, renk: d.renk, g: KALINLIK[d.kalinlik], boy, bas: [p[0], p[1]], n };
        d.cizgiler.push(yeni);
        d.gecmis.push({ tur: 'ekle', cizgi: yeni });
        d.ileri = [];
        hepsiniCiz();
        guncelle();
      };
      girdi.addEventListener('input', () => {
        girdi.style.height = 'auto';
        girdi.style.height = `${girdi.scrollHeight}px`;
      });
      girdi.addEventListener('keydown', (e) => {
        e.stopPropagation();
        if (e.key === 'Escape') { kaydedildi = true; aktifGirdi = null; girdi.remove(); }
        else if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); kaydet(); }
      });
      girdi.addEventListener('blur', kaydet);
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
      const e = document.elementsFromPoint(x, y).find((e) => e !== ust && e !== alt && e !== kap && !cubuk.contains(e));
      return e?.closest(TIKLANIR) || null;
    };
    let bas = null;

    let aktif = null;
    ust.addEventListener('pointerdown', (o) => {
      if (d.arac === 'el' || o.button > 0) return;
      o.preventDefault();
      try { ust.setPointerCapture(o.pointerId); } catch { /* yapay olay */ }
      if (o.pointerType === 'touch') {
        dokunma.set(o.pointerId, [o.clientX, o.clientY]);
        if (dokunma.size >= 2) {                    // ikinci parmak: çizimi bırak, kaydırmaya geç
          if (d.canli) { d.canli = null; d.tahmin = []; iste(); }
          if (oturum) oturumKapat();
          aktif = null; pan = kaydir ? orta() : null; return;
        }
      }
      const p = nokta(o, true);
      d.imlec = p;
      if (d.arac === 'metin') {
        const hedef = alttaki(o.clientX, o.clientY);
        if (hedef) { hedef.click(); return; }
        metinKutusuAc(p, o.clientX, o.clientY);
        return;
      }
      aktif = o.pointerId;
      bas = { x: o.clientX, y: o.clientY, t: performance.now(), uzak: 0 };
      if (d.arac === 'odak') { iste(); return; }
      if (d.arac === 'lazer') {
        d.lazerIz.push([p[0], p[1], performance.now(), true]);
        iste();
        return;
      }
      if (d.arac === 'silgi' || d.arac === 'cizgisil') { oturumAc(); sonSilgi = null; silgiUygula(p); iste(); return; }
      if (SEKILLER.has(d.arac)) {
        d.canli = { arac: d.arac, sekil: d.arac, renk: d.renk, g: KALINLIK[d.kalinlik], bas: [p[0], p[1]], son: [p[0], p[1]], dik: o.shiftKey, n: [[p[0], p[1], 1]] };
        iste();
        return;
      }
      d.tahmin = [];
      d.canli = { arac: d.arac, renk: d.renk, g: KALINLIK[d.kalinlik] * (d.arac === 'fosforlu' ? 3.2 : 1), n: [p] };
      iste();
    });

    ust.addEventListener('pointermove', (o) => {
      if (dokunma.has(o.pointerId)) {
        dokunma.set(o.pointerId, [o.clientX, o.clientY]);
        if (pan && dokunma.size >= 2) { const m = orta(); kaydirBy(pan[0] - m[0], pan[1] - m[1]); pan = m; return; }
      }
      const guncelNokta = nokta(o);
      if (['silgi', 'kalem', 'fosforlu', 'kesikli', 'lazer', 'odak'].includes(d.arac)) {
        d.imlec = guncelNokta;
        iste();
      }
      if (aktif === null && o.pointerType === 'mouse' && d.arac !== 'silgi' && d.arac !== 'cizgisil') {
        ust.style.cursor = alttaki(o.clientX, o.clientY) ? 'pointer' : (d.arac === 'metin' ? 'text' : 'crosshair');
      }
      if (o.pointerId !== aktif) return;
      if (bas) bas.uzak = Math.max(bas.uzak, Math.hypot(o.clientX - bas.x, o.clientY - bas.y));
      const birlesik = o.getCoalescedEvents?.() || [];
      const olaylar = birlesik.length ? birlesik : [o];
      if (d.arac === 'odak') { iste(); return; }
      if (d.arac === 'lazer') {
        const simdi = performance.now();
        for (const e of olaylar) {
          const lp = nokta(e);
          d.lazerIz.push([lp[0], lp[1], simdi, false]);
        }
        iste();
        return;
      }
      if (d.arac === 'silgi' || d.arac === 'cizgisil') { for (const e of olaylar) silgiUygula(nokta(e)); return; }
      if (!d.canli) return;
      if (d.canli.sekil) {
        d.canli.dik = o.shiftKey;
        d.canli.son = sekilHedef(d.canli.bas, [guncelNokta[0], guncelNokta[1]], d.canli.sekil, o.shiftKey);
        d.canli.n = sekilNoktalari(d.canli);
        iste();
        return;
      }
      for (const e of olaylar) {
        const ham = nokta(e), s = d.canli.n[d.canli.n.length - 1];
        const p = yumusat(s, ham);
        if (Math.hypot(p[0] - s[0], p[1] - s[1]) > 0.25) d.canli.n.push(p);
      }
      const ongorulen = o.getPredictedEvents?.() || [];
      d.tahmin = ongorulen.slice(0, 2).map((e) => nokta(e));
      iste();
    });

    const bitir = (o) => {
      dokunma.delete(o.pointerId);
      if (dokunma.size < 2) pan = null;
      if (o.pointerId !== aktif) return;
      aktif = null;
      d.tahmin = [];
      const hedef = o.type === 'pointerup' && bas && bas.uzak < 6 && performance.now() - bas.t < 500 ? alttaki(o.clientX, o.clientY) : null;
      const suruklendi = bas ? bas.uzak >= 4 : true;
      bas = null;
      if (hedef && d.canli) { d.canli = null; iste(); }
      if (oturum) { oturumKapat(); sonSilgi = null; }
      if (d.canli) {
        if (d.canli.sekil && !suruklendi) {
          d.canli = null; iste();
        } else {
          if (d.canli.sekil) d.canli.n = sekilNoktalari(d.canli);
          d.cizgiler.push(d.canli); d.gecmis.push({ tur: 'ekle', cizgi: d.canli }); d.ileri = [];
          cizgiCiz(d.canli, a, kay());
          d.canli = null; iste(); guncelle();
        }
      }
      if (hedef) { if (hedef.matches('input, select, textarea')) hedef.focus(); hedef.click(); }
    };
    ust.addEventListener('pointerup', bitir);
    ust.addEventListener('pointercancel', bitir);
    ust.addEventListener('pointerleave', () => { if (d.imlec && aktif === null && d.arac !== 'odak') { d.imlec = null; iste(); } });

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

    // İndirilen görüntüde sağ alt köşede Ders Kutusu mührü ve adresi (kullanıcı 29.09: "indirilebilen her şeyin üzerinde logo olmalı")
    const pngLogolu = () => new Promise((coz) => {
      const c = document.createElement('canvas'); c.width = alt.width; c.height = alt.height;
      const x = c.getContext('2d');
      x.fillStyle = d.zemin === 'koyu' ? '#132620' : '#fff';
      x.fillRect(0, 0, c.width, c.height);
      x.drawImage(alt, 0, 0);
      const img = new Image();
      const bitir = () => {
        const b = 52 * oran, p = 14 * oran;
        try { x.drawImage(img, c.width - b - p, c.height - b - p, b, b); } catch { /* mühür yüklenemedi: yalnız adres */ }
        x.font = `700 ${13 * oran}px -apple-system, "Segoe UI", Roboto, Arial, sans-serif`;
        x.fillStyle = d.zemin === 'koyu' ? '#e9eef6' : '#0b2257';
        x.textAlign = 'right'; x.textBaseline = 'middle';
        x.fillText('derskutusu.com', c.width - b - p - 8 * oran, c.height - p - b / 2);
        coz(c.toDataURL('image/png'));
      };
      img.onload = bitir; img.onerror = bitir; img.src = '/simge-192.png';
    });

    // Araç çubuğu
    const cubuk = document.createElement('div');
    cubuk.className = 'tahta-cubuk';
    cubuk.setAttribute('role', 'toolbar');
    cubuk.setAttribute('aria-label', 'Tahta araçları');
    const dugme = (ad, ic, is, ek = '') => `<button type="button" class="${ek}" data-${ad}="${is}" title="${ic.baslik}" aria-label="${ic.baslik}">${ic.html}</button>`;
    const yazimAraclari = [
      ['kalem', 'Hassas kalem (K)'],
      ['fosforlu', 'Fosforlu vurgu kalemi (F)'],
      ['kesikli', 'Kesikli çizgi kalemi (N)'],
      ['lazer', 'Lazer işaretçi — izi kendiliğinden silinir (L)'],
      ['silgi', 'Kısmi silgi: değdiği yeri siler (S)'],
      ['cizgisil', 'Çizgi / şekil silgisi: tamamını siler (Ç)'],
    ];
    const sekilAraclari = [
      ['cizgi', 'Cetvel / düz çizgi — Shift ile açı kilitler (D)'],
      ['ok', 'Ok / vektör çizimi (O)'],
      ['dikdortgen', 'Dikdörtgen / kutu — Shift ile kare (R)'],
      ['cember', 'Çember / elips — Shift ile tam çember (M)'],
      ['ucgen', 'Üçgen — Shift ile dik üçgen (U)'],
      ['eksen', 'Sayı doğrusu / koordinat ekseni (X)'],
      ['metin', 'Metin / etiket ekle (T)'],
      ['odak', 'Odak / spot ışığı perdesi (G)'],
      ...(kaydir ? [['el', 'Sayfayı kaydır (E) — iki parmakla da kaydırabilirsiniz']] : []),
    ];
    cubuk.innerHTML =
      `<div class="tahta-grup">${yazimAraclari.map(([is, b]) => dugme('arac', { baslik: b, html: svg(ARAC_SIMGE[is]) }, is)).join('')}</div>` +
      `<div class="tahta-grup">${sekilAraclari.map(([is, b]) => dugme('arac', { baslik: b, html: svg(ARAC_SIMGE[is]) }, is)).join('')}</div>` +
      `<div class="tahta-grup">${Object.keys(KALINLIK).map((k) => {
        const cap = Math.max(3, Math.min(16, Math.round(KALINLIK[k] + 2)));
        return dugme('kalinlik', { baslik: `Kalınlık: ${KALINLIK_AD[k]}`, html: `<i style="width:${cap}px;height:${cap}px"></i>` }, k, 'kalin');
      }).join('')}</div>` +
      `<div class="tahta-grup">${RENKLER.map((r, i) => dugme('renk', { baslik: `Renk ${i + 1}`, html: `<span style="background:${r}"></span>` }, r, 'renk')).join('')}` +
      `<label class="tahta-ozel-renk" title="Özel renk seç" aria-label="Özel renk seç"><input type="color" value="${d.renk}"><span></span></label></div>` +
      `<div class="tahta-grup">` +
      dugme('is', { baslik: 'Geri al (Ctrl+Z)', html: svg('M9 14L4 9l5-5M4 9h10a6 6 0 010 12h-3') }, 'geri') +
      dugme('is', { baslik: 'İleri al (Ctrl+Y)', html: svg('M15 14l5-5-5-5M20 9H10a6 6 0 000 12h3') }, 'ileri') +
      dugme('is', { baslik: 'Çizimi PNG olarak indir', html: svg('M12 4v11m-5-5 5 5 5-5M5 20h14') }, 'indir') +
      dugme('is', { baslik: 'Hepsini temizle', html: svg('M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3') }, 'temizle') +
      (kapat ? dugme('is', { baslik: 'Kalemi kapat (Esc)', html: svg('M6 6l12 12M18 6L6 18') }, 'kapat', 'kapat') : '') + `</div>`;
    kap.append(cubuk);
    sabitBoy(cubuk);

    const ozelRenkGirdi = cubuk.querySelector('.tahta-ozel-renk input');
    const guncelle = () => {
      cubuk.querySelectorAll('[data-arac]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.arac === d.arac)));
      cubuk.querySelectorAll('[data-renk]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.renk.toLowerCase() === d.renk.toLowerCase())));
      cubuk.querySelectorAll('[data-kalinlik]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.kalinlik === d.kalinlik)));
      ust.style.pointerEvents = d.arac === 'el' ? 'none' : 'auto';
      ust.style.cursor = d.arac === 'silgi' ? 'none' : d.arac === 'cizgisil' ? 'cell' : d.arac === 'metin' ? 'text' : 'crosshair';
      const g = cubuk.querySelector('[data-is=geri]'), i = cubuk.querySelector('[data-is=ileri]');
      if (g) g.disabled = !d.gecmis.length;
      if (i) i.disabled = !d.ileri.length;
      if (d.arac === 'odak' && !d.imlec) {
        const k = kay();
        d.imlec = [k.x + gen / 2, k.y + yuk / 2, 1];
      }
      iste();
    };

    ozelRenkGirdi?.addEventListener('input', (o) => {
      d.renk = o.target.value;
      if (['silgi', 'cizgisil', 'el', 'lazer', 'odak'].includes(d.arac)) d.arac = 'kalem';
      guncelle();
    });

    cubuk.addEventListener('click', (o) => {
      const b = o.target.closest('button'); if (!b) return;
      if (b.dataset.arac) d.arac = b.dataset.arac;
      if (b.dataset.renk) {
        d.renk = b.dataset.renk;
        if (ozelRenkGirdi && /^#[0-9a-f]{6}$/i.test(d.renk)) ozelRenkGirdi.value = d.renk;
        if (['silgi', 'cizgisil', 'el', 'lazer', 'odak'].includes(d.arac)) d.arac = 'kalem';
      }
      if (b.dataset.kalinlik) d.kalinlik = b.dataset.kalinlik;
      if (b.dataset.is === 'geri') geriAl();
      if (b.dataset.is === 'ileri') yinele();
      if (b.dataset.is === 'indir') {
        pngLogolu().then((adres) => { const link = document.createElement('a'); link.href = adres; link.download = 'derskutusu-not.png'; link.click(); });
      }
      if (b.dataset.is === 'temizle') temizle();
      if (b.dataset.is === 'kapat') kapat?.();
      guncelle();
    });

    const tus = (o) => {
      // Gizli kalem ve sunumun arkasındaki sayfa kısayollara yanıt vermez.
      const modal = document.querySelector('dialog[open]');
      if (!kap.isConnected || kap.closest('[hidden]') || (modal && !modal.contains(kap))) return;
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)) return;
      const k = o.key.toLowerCase();
      if ((o.ctrlKey || o.metaKey) && k === 'z') { o.preventDefault(); o.shiftKey ? yinele() : geriAl(); return; }
      if ((o.ctrlKey || o.metaKey) && k === 'y') { o.preventDefault(); yinele(); return; }
      if (o.ctrlKey || o.metaKey || o.altKey) return;
      const aracHaritasi = {
        k: 'kalem', f: 'fosforlu', n: 'kesikli', l: 'lazer',
        s: 'silgi', 'ç': 'cizgisil', d: 'cizgi', o: 'ok',
        r: 'dikdortgen', m: 'cember', u: 'ucgen', 'ü': 'ucgen',
        x: 'eksen', t: 'metin', g: 'odak', e: kaydir ? 'el' : null,
      };
      const arac = aracHaritasi[k];
      if (arac) { d.arac = arac; guncelle(); }
      if (k === 'escape') {
        if (d.arac === 'odak') { d.arac = 'kalem'; guncelle(); }
        else if (kapat) kapat();
      }
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
      zemin: (z) => {
        d.zemin = z;
        if (z === 'koyu' && d.renk === '#111a2e') d.renk = '#ffffff';
        else if (z !== 'koyu' && d.renk === '#ffffff') d.renk = '#111a2e';
        hepsiniCiz(); guncelle();
      },
      yukle: (cizgiler) => { d.cizgiler = cizgiler; d.gecmis = []; d.ileri = []; hepsiniCiz(); guncelle(); },
      png: () => alt.toDataURL('image/png'),
      pngLogolu,
      // Yakınlaştırmada çizgiler içerikle birlikte ölçeklenir.
      olcekle: (k) => {
        const hepsi = new Set([...d.cizgiler, ...[...d.gecmis, ...d.ileri].flatMap((g) => g.cizgiler || (g.cizgi ? [g.cizgi] : [...g.eski, ...g.yeni]))]);
        for (const c of hepsi) {
          c.g *= k; c.k = null;
          if (c.boy) c.boy *= k;
          if (c.bas) { c.bas[0] *= k; c.bas[1] *= k; }
          if (c.son) { c.son[0] *= k; c.son[1] *= k; }
          for (const q of c.n) { q[0] *= k; q[1] *= k; }
        }
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
    document.getElementById('t-tam').addEventListener('click', () => (document.fullscreenElement ? document.exitFullscreen() : document.getElementById('tahta-alan').requestFullscreen?.()));
    sayfaYaz();
  } else {
    // Öteki sayfalar: sağ altta kalem düğmesi → sayfanın üstüne yaz
    const ac = document.createElement('button');
    ac.type = 'button'; ac.className = 'kalem-dugme'; ac.title = 'Kalemle sayfaya yaz (akıllı tahta)'; ac.setAttribute('aria-label', 'Kalemle sayfaya yaz');
    ac.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Kalemle yaz</span>';
    document.body.append(ac);
    sabitBoy(ac, 'sag');
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
    // Konu sayfasının başlığındaki "Kalemle yaz" düğmesi ekrandayken sağ alttaki kopyası gizlenir (aynı işi iki düğme yapmaz)
    const sayfaDugmesi = document.querySelector('button[onclick*="kalemAc"]');
    if (sayfaDugmesi && 'IntersectionObserver' in window) {
      new IntersectionObserver(([g]) => ac.classList.toggle('gizli', g.isIntersecting)).observe(sayfaDugmesi);
    }
  }
}

// Konu sayfalarındaki sunum, mevcut tahta ve etkinlik davranışlarını yeniden kullanır.
if (typeof document !== 'undefined' && document.querySelector('article.ozet')) {
  const ders = document.createElement('script');
  ders.src = '/ders-slayt.js?v=20261006-1';
  document.head.append(ders);
}
