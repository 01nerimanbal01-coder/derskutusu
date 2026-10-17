// Akıllı tahta kalemi ve sınıf araçları: her sayfada sayfanın (ya da belge görüntüleyicinin) üstüne yazma, tahta.html'de çok sayfalı akıllı tahta.
// Hız ve hassasiyet: iki katman — biten çizgiler alt tuvalde, çizilmekte olan çizgi üst tuvalde requestAnimationFrame ile çizilir;
// çizgiler vektör olarak tutulur (geri al / yinele / silgi / seç-taşı), kalem basıncı, hız uyumlu sönümleme (stabilizasyon),
// çizim sonunda bekleyince otomatik akıllı şekil tanıma, pano görseli yapıştırma (Ctrl+V), süre ölçer ve cevap perdesi içerir.
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
  const DAMGALAR = [
    { s: '✓', ad: 'Doğru', r: '#12a150' },
    { s: '✗', ad: 'Yanlış', r: '#e62117' },
    { s: '★', ad: 'Önemli / Yıldız', r: '#f29f05' },
    { s: '!', ad: 'Dikkat', r: '#e62117' },
    { s: '?', ad: 'Soru işareti', r: '#2451d6' },
    { s: '⇒', ad: 'İse / Sonuç oku', r: '#2451d6' },
    { s: '⇔', ad: 'Ancak ve ancak', r: '#8b3fd6' },
    { s: '⊥', ad: 'Diklik sembolü', r: '#111a2e' },
    { s: '∥', ad: 'Paralellik sembolü', r: '#111a2e' },
    { s: '∴', ad: 'O hâlde (sonuç)', r: '#00a3b4' },
  ];
  const ARAC_SIMGE = {
    kalem: 'M4 20l4-1 10-10-3-3L5 16l-1 4zM14 5l3 3',
    fosforlu: 'M6 14l6-6 4 4-6 6H6v-4zM4 20h16',
    kesikli: 'M4 17l3-3M9.5 11.5l3-3M15 6l3-3M3 21h4M10 21h4M17 21h4',
    lazer: 'M12 8a4 4 0 100 8 4 4 0 000-8zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1',
    silgi: 'M8 20h12M5 15l7-7 5 5-5 5H9l-4-3z',
    cizgisil: 'M3 16c3-4 6-4 9 0s6 4 9 0M9 6l6 6M15 6l-6 6',
    sec: 'M5 3l14 8-6 2-2 6-6-16zM13 13l6 6',
    cizgi: 'M4 20L20 4M6 14l4 4M11 9l4 4',
    ok: 'M5 19L19 5M11 5h8v8',
    dikdortgen: 'M4 6h16v12H4z',
    cember: 'M12 4a8 8 0 100 16 8 8 0 000-16z',
    ucgen: 'M12 4L3 19h18L12 4z',
    eksen: 'M3 12h18M12 3v18M18 9l3 3-3 3M9 6l3-3 3 3',
    metin: 'M5 6V4h14v2M12 4v16M9 20h6',
    damga: 'M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8-4.3-4.1 5.9-.9L12 3z',
    resim: 'M4 5h16v14H4zM8.5 10a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM20 15l-5-5L6 19',
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
    if (tur === 'dikdortgen' || tur === 'resim') {
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

  // Serbest çizimin sonunda kalemi basılı tutunca (~420ms) şekli otomatik tanıyan yardımcı (Düz çizgi / Çember / Dikdörtgen / Üçgen)
  function akilliSekilTani(n) {
    if (!n || n.length < 8) return null;
    let L = 0, x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (let i = 0; i < n.length; i++) {
      const [x, y] = n[i];
      if (x < x0) x0 = x; if (x > x1) x1 = x;
      if (y < y0) y0 = y; if (y > y1) y1 = y;
      if (i > 0) L += Math.hypot(x - n[i - 1][0], y - n[i - 1][1]);
    }
    if (L < 36) return null;
    const bas = n[0], son = n[n.length - 1];
    const ucMesafe = Math.hypot(son[0] - bas[0], son[1] - bas[1]);
    // 1) Düz çizgi: başlangıç-bitiş mesafesi toplam yolun %90'ından büyükse
    if (ucMesafe / L > 0.90) {
      return { sekil: 'cizgi', bas: [bas[0], bas[1]], son: [son[0], son[1]] };
    }
    const gen = x1 - x0, yuk = y1 - y0, kosegen = Math.hypot(gen, yuk);
    // 2) Kapalı şekiller: başlangıç ve bitiş birbirine yakınsa
    if (ucMesafe < Math.max(48, L * 0.28) && gen > 20 && yuk > 20) {
      const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, rx = gen / 2, ry = yuk / 2;
      let elipsHata = 0;
      for (const [x, y] of n) {
        const d = Math.hypot((x - cx) / rx, (y - cy) / ry);
        elipsHata += Math.abs(d - 1);
      }
      elipsHata /= n.length;
      if (elipsHata < 0.165) {
        const tam = Math.abs(gen - yuk) / Math.max(gen, yuk) < 0.18;
        const r = (gen + yuk) / 4;
        return {
          sekil: 'cember',
          bas: tam ? [cx - r, cy - r] : [x0, y0],
          son: tam ? [cx + r, cy + r] : [x1, y1],
        };
      }
      // Köşelere yakınlık testi: dikdörtgenin 4 kenarına ortalama uzaklık küçükse dikdörtgen, değilse üçgen
      let kenarHata = 0;
      for (const [x, y] of n) {
        const dKenar = Math.min(Math.abs(x - x0), Math.abs(x - x1), Math.abs(y - y0), Math.abs(y - y1));
        kenarHata += dKenar / kosegen;
      }
      kenarHata /= n.length;
      if (kenarHata < 0.068) {
        return { sekil: 'dikdortgen', bas: [x0, y0], son: [x1, y1] };
      }
      if (elipsHata < 0.34) {
        return { sekil: 'ucgen', bas: [x0, y0], son: [x1, y1] };
      }
    }
    return null;
  }

  function ogeKaydir(c, dx, dy) {
    c.k = null;
    if (c.bas) { c.bas[0] += dx; c.bas[1] += dy; }
    if (c.son) { c.son[0] += dx; c.son[1] += dy; }
    if (c.n) { for (const q of c.n) { q[0] += dx; q[1] += dy; } }
  }

  function ogeKopyala(c, dx = 22, dy = 22) {
    const yeni = {
      ...c,
      bas: c.bas ? [c.bas[0] + dx, c.bas[1] + dy] : undefined,
      son: c.son ? [c.son[0] + dx, c.son[1] + dy] : undefined,
      n: c.n ? c.n.map((q) => [q[0] + dx, q[1] + dy, q[2]]) : [],
      k: null,
    };
    return yeni;
  }

  function olustur({ kap, kaydir = false, zemin = null, kapat = null, degisti = null }) {
    // kap: tuvallerin konacağı öğe; kaydir: true → çizgiler sayfa kaydırmasıyla, öğe → o öğenin (ör. PDF kabı) kaydırmasıyla kayar
    const alt = document.createElement('canvas');
    const ust = document.createElement('canvas');
    alt.className = 'tahta-tuval'; ust.className = 'tahta-tuval tahta-ust';
    kap.append(alt, ust);
    const a = alt.getContext('2d'), u = ust.getContext('2d');
    const d = {
      arac: 'kalem', renk: RENKLER[1], kalinlik: 'orta', dolu: false,
      damga: DAMGALAR[0],
      cizgiler: [], ileri: [], gecmis: [],
      secili: [], secimKutu: null,
      canli: null, tahmin: [], lazerIz: [],
      imlec: null, istek: 0, zemin,
    };
    let oran = 1, gen = 0, yuk = 0;
    const bildir = () => { degisti?.(d.cizgiler, d.zemin); };

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
        t.beginPath(); t.rect(Math.min(x0, x1), Math.min(y0, y1), Math.abs(x1 - x0), Math.abs(y1 - y0));
        if (c.dolu) { t.save(); t.globalAlpha = 0.16; t.fill(); t.restore(); }
        t.stroke();
      } else if (tur === 'cember') {
        const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, rx = Math.abs(x1 - x0) / 2, ry = Math.abs(y1 - y0) / 2;
        t.beginPath(); t.ellipse(cx, cy, rx, ry, 0, 0, Math.PI * 2);
        if (c.dolu) { t.save(); t.globalAlpha = 0.16; t.fill(); t.restore(); }
        t.stroke();
      } else if (tur === 'ucgen') {
        const ustX = c.dik ? x0 : (x0 + x1) / 2;
        t.beginPath(); t.moveTo(ustX, y0); t.lineTo(x1, y1); t.lineTo(x0, y1); t.closePath();
        if (c.dolu) { t.save(); t.globalAlpha = 0.16; t.fill(); t.restore(); }
        t.stroke();
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
      if (c.otomatik) yazi = `✨ Akıllı şekil · ${yazi}`;
      const mx = (x0 + x1) / 2, my = Math.min(y0, y1) - 16;
      t.save();
      t.font = '600 12px -apple-system, "Segoe UI", Roboto, Arial, sans-serif';
      const w = t.measureText(yazi).width + 16;
      t.fillStyle = 'rgba(17,26,46,.88)';
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
      if (!n.length && !c.sekil && !c.metin && c.arac !== 'resim') return;
      t.save();
      t.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      t.lineCap = 'round'; t.lineJoin = 'round';
      t.strokeStyle = c.renk; t.fillStyle = c.renk;
      t.globalAlpha = c.arac === 'fosforlu' ? 0.32 : 1;

      if (c.arac === 'resim' && c.bas && c.son) {
        if (!c.img && c.veri) {
          const im = new Image();
          im.onload = () => { c.img = im; hepsiniCiz(); };
          im.src = c.veri;
        }
        if (c.img) {
          const rx = Math.min(c.bas[0], c.son[0]), ry = Math.min(c.bas[1], c.son[1]);
          const rw = Math.abs(c.son[0] - c.bas[0]), rh = Math.abs(c.son[1] - c.bas[1]);
          t.drawImage(c.img, rx, ry, rw, rh);
        }
        t.restore();
        return;
      }

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

    function kutu(c) {
      if (!c.k) {
        let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
        for (const q of c.n) { if (q[0] < x0) x0 = q[0]; if (q[0] > x1) x1 = q[0]; if (q[1] < y0) y0 = q[1]; if (q[1] > y1) y1 = q[1]; }
        const pay = (c.g || 4) + 4;
        c.k = [x0 - pay, y0 - pay, x1 + pay, y1 + pay];
      }
      return c.k;
    }

    function secimKutuHesapla(ogeler) {
      if (!ogeler.length) return null;
      let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
      for (const c of ogeler) {
        const b = kutu(c);
        if (b[0] < x0) x0 = b[0];
        if (b[1] < y0) y0 = b[1];
        if (b[2] > x1) x1 = b[2];
        if (b[3] > y1) y1 = b[3];
      }
      return [x0 - 4, y0 - 4, x1 + 4, y1 + 4];
    }

    function secimCiz(k) {
      if (!d.secili.length && !d.secimKutu) return;
      u.save();
      u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
      if (d.secimKutu) {
        const [x0, y0, x1, y1] = d.secimKutu;
        u.fillStyle = 'rgba(36, 81, 214, 0.1)';
        u.strokeStyle = 'rgba(36, 81, 214, 0.75)';
        u.lineWidth = 1.5;
        u.setLineDash([5, 4]);
        u.beginPath(); u.rect(Math.min(x0, x1), Math.min(y0, y1), Math.abs(x1 - x0), Math.abs(y1 - y0)); u.fill(); u.stroke();
      }
      if (d.secili.length) {
        const sb = secimKutuHesapla(d.secili);
        if (sb) {
          const [x0, y0, x1, y1] = sb;
          u.strokeStyle = '#2451d6';
          u.lineWidth = 1.8;
          u.setLineDash([6, 4]);
          u.beginPath(); u.rect(x0, y0, x1 - x0, y1 - y0); u.stroke();
          u.setLineDash([]);
          u.fillStyle = '#ffffff';
          for (const [kx, ky] of [[x0, y0], [x1, y0], [x1, y1], [x0, y1]]) {
            u.beginPath(); u.arc(kx, ky, 4.5, 0, Math.PI * 2); u.fill(); u.stroke();
          }
        }
      }
      u.restore();
    }

    function hepsiniCiz() {
      a.setTransform(1, 0, 0, 1, 0, 0); a.clearRect(0, 0, alt.width, alt.height);
      zeminCiz();
      const k = kay();
      for (const c of d.cizgiler) cizgiCiz(c, a, k);
      iste();
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
      if (d.secili.length || d.secimKutu) secimCiz(k);
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
      if (oturum && (oturum.eski.size || oturum.yeni.size)) {
        d.gecmis.push({ tur: 'degistir', eski: [...oturum.eski], yeni: [...oturum.yeni] });
        d.ileri = [];
        bildir();
      }
      oturum = null; guncelle();
    };

    const yakin = (c, p, r) => { const k = kutu(c); return !(p[0] < k[0] - r || p[0] > k[2] + r || p[1] < k[1] - r || p[1] > k[3] + r); };

    function noktaOgeyeYakinMi(c, p, esik = 10) {
      if (!yakin(c, p, esik)) return false;
      if (c.arac === 'resim' && c.bas && c.son) {
        const x0 = Math.min(c.bas[0], c.son[0]), x1 = Math.max(c.bas[0], c.son[0]);
        const y0 = Math.min(c.bas[1], c.son[1]), y1 = Math.max(c.bas[1], c.son[1]);
        return p[0] >= x0 - esik && p[0] <= x1 + esik && p[1] >= y0 - esik && p[1] <= y1 + esik;
      }
      return c.n.some((q, i) => {
        const r = i ? c.n[i - 1] : q;
        const dx = q[0] - r[0], dy = q[1] - r[1], L = dx * dx + dy * dy;
        const s = L ? Math.max(0, Math.min(1, ((p[0] - r[0]) * dx + (p[1] - r[1]) * dy) / L)) : 0;
        return Math.hypot(p[0] - (r[0] + s * dx), p[1] - (r[1] - 0 + s * dy)) < esik + (c.g || 4) / 2;
      });
    }

    // Kısmi silgi: yalnız silginin değdiği kısmı siler; çizgi gerekirse ikiye bölünür.
    function kismiSil(p) {
      const r = SILGI[d.kalinlik];
      let degistiMi = false;
      const sonuc = [];
      for (const c of d.cizgiler) {
        if (!yakin(c, p, r)) { sonuc.push(c); continue; }
        if (c.metin || c.arac === 'resim') {
          const vur = c.n.some((q) => Math.hypot(q[0] - p[0], q[1] - p[1]) < r + 8);
          if (vur) { degistiMi = true; cikar(c); } else sonuc.push(c);
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
        degistiMi = true; cikar(c);
        for (const pn of parcalar) {
          if (pn.length < 2 && c.n.length > 1) continue;
          const yeni = { arac: c.arac === 'fosforlu' || c.arac === 'kesikli' ? c.arac : 'kalem', renk: c.renk, g: c.g, n: pn, parca: true };
          sonuc.push(yeni); oturum.yeni.add(yeni);
        }
      }
      if (degistiMi) { d.cizgiler = sonuc; hepsiniCiz(); }
    }
    // Çizgi silgisi: dokunulan çizgiyi ya da şekli bütünüyle siler.
    function cizgiSil(p) {
      const esik = 12, once = d.cizgiler.length;
      d.cizgiler = d.cizgiler.filter((c) => {
        const vur = noktaOgeyeYakinMi(c, p, esik);
        if (vur) cikar(c);
        return !vur;
      });
      if (d.cizgiler.length !== once) hepsiniCiz();
    }
    let sonSilgi = null;
    function silgiUygula(p) {
      const adim = Math.max(3, (d.arac === 'silgi' ? SILGI[d.kalinlik] : 12) / 2);
      const s = sonSilgi || p, L = Math.hypot(p[0] - s[0], p[1] - s[1]), say = Math.max(1, Math.ceil(L / adim));
      for (let i = 1; i <= say; i++) {
        const q = [s[0] + (p[0] - s[0]) * i / say, s[1] + (p[1] - s[1]) * i / say, 1];
        d.arac === 'silgi' ? kismiSil(q) : cizgiSil(q);
      }
      sonSilgi = p;
    }

    // Canlı imleç: silgide silme halkası, kalemde/fosforluda hassas uç boyutu önizlemesi, damgada sembol önizlemesi
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
      } else if (d.arac === 'damga' && d.damga) {
        const boy = Math.round(Math.max(22, KALINLIK[d.kalinlik] * 5.2));
        u.save(); u.setTransform(oran, 0, 0, oran, -k.x * oran, -k.y * oran);
        u.globalAlpha = 0.55;
        u.font = `800 ${boy}px -apple-system, "Segoe UI", Roboto, Arial, sans-serif`;
        u.fillStyle = d.damga.r || d.renk;
        u.textAlign = 'center'; u.textBaseline = 'middle';
        u.fillText(d.damga.s, d.imlec[0], d.imlec[1]);
        u.restore();
      }
    }

    // Metin / etiket ekleme kutusu
    let aktifGirdi = null;
    function metinEkle(yazi, p, boy, renk = d.renk) {
      const satirlar = yazi.split('\n');
      const enUzun = Math.max(...satirlar.map((s) => s.length));
      const genTahmin = Math.max(22, enUzun * boy * 0.6);
      const yukTahmin = satirlar.length * boy * 1.25;
      const n = [
        ...parcaOrnekle(p[0], p[1], p[0] + genTahmin, p[1], 6),
        ...parcaOrnekle(p[0], p[1] + yukTahmin / 2, p[0] + genTahmin, p[1] + yukTahmin / 2, 6),
        ...parcaOrnekle(p[0], p[1] + yukTahmin, p[0] + genTahmin, p[1] + yukTahmin, 6),
      ];
      const yeni = { arac: 'metin', metin: yazi, renk, g: KALINLIK[d.kalinlik], boy, bas: [p[0], p[1]], n };
      d.cizgiler.push(yeni);
      d.gecmis.push({ tur: 'ekle', cizgi: yeni });
      d.ileri = [];
      hepsiniCiz();
      guncelle();
      bildir();
    }

    function metinKutusuAc(p, clientX, clientY) {
      if (aktifGirdi) aktifGirdi.blur();
      const r = kap.getBoundingClientRect();
      const boy = Math.round(Math.max(16, KALINLIK[d.kalinlik] * 4.2));
      const girdi = document.createElement('textarea');
      girdi.className = 'tahta-metin-girdi';
      girdi.rows = 1;
      girdi.placeholder = 'Metin yazın… (Enter: kaydet)';
      girdi.style.left = `${Math.max(8, Math.min(r.width - 150, clientX - r.left))}px`;
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
        metinEkle(yazi, p, boy, d.renk);
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

    // Görsel / soru ekran görüntüsü ekleme (Dosyadan ya da Ctrl+V panodan)
    function gorselVerisiEkle(dataUrl) {
      const im = new Image();
      im.onload = () => {
        const k = kay();
        const maxW = Math.min(520, gen * 0.65), maxH = Math.min(420, yuk * 0.65);
        const olcek = Math.min(1, maxW / (im.width || 300), maxH / (im.height || 200));
        const w = Math.round((im.width || 300) * olcek), h = Math.round((im.height || 200) * olcek);
        const x0 = Math.round(k.x + (gen - w) / 2), y0 = Math.round(k.y + Math.max(24, (yuk - h) / 2 - 30));
        const yeni = {
          arac: 'resim', img: im, veri: dataUrl, renk: '#2451d6', g: 2,
          bas: [x0, y0], son: [x0 + w, y0 + h],
          n: [],
        };
        yeni.n = sekilNoktalari(yeni);
        d.cizgiler.push(yeni);
        d.gecmis.push({ tur: 'ekle', cizgi: yeni });
        d.ileri = [];
        d.secili = [yeni];
        d.arac = 'sec';
        hepsiniCiz();
        guncelle();
        bildir();
      };
      im.src = dataUrl;
    }

    const resimGirdi = document.createElement('input');
    resimGirdi.type = 'file';
    resimGirdi.accept = 'image/*';
    resimGirdi.hidden = true;
    resimGirdi.addEventListener('change', () => {
      const dosya = resimGirdi.files?.[0];
      if (!dosya) return;
      const okuyucu = new FileReader();
      okuyucu.onload = () => { if (typeof okuyucu.result === 'string') gorselVerisiEkle(okuyucu.result); };
      okuyucu.readAsDataURL(dosya);
      resimGirdi.value = '';
    });
    kap.append(resimGirdi);

    // İki parmakla (dokunmatik) sayfa kaydırma: kalemi kapatmadan gezinme
    const dokunma = new Map();
    let pan = null;
    const orta = () => { const v = [...dokunma.values()]; return [(v[0][0] + v[1][0]) / 2, (v[0][1] + v[1][1]) / 2]; };
    const kaydirBy = (dx, dy) => { const s = { left: dx, top: dy, behavior: 'instant' }; if (kaydir === true) window.scrollBy(s); else if (kaydir) kaydir.scrollBy(s); };

    // Kalem açıkken kısa ve kıpırtısız dokunuş alttaki düğmeye, bağlantıya, etkinliğe geçer (çizgi bırakmaz);
    // sürükleyince çizilir. Fare tıklanabilir öğenin üstündeyken imleç el olur.
    const TIKLANIR = 'button, a[href], input, select, textarea, label, summary, [role="button"], .etk-kelime, .etk-bosluk-yer, [data-sol], [data-sag]';
    const alttaki = (x, y) => {
      const e = document.elementsFromPoint(x, y).find((el) => el !== ust && el !== alt && el !== kap && !cubuk.contains(el));
      return e?.closest(TIKLANIR) || null;
    };
    let bas = null;
    let aktif = null;
    let tasiBas = null, tasiToplam = [0, 0];
    let akilliZamanlayici = 0;

    ust.addEventListener('pointerdown', (o) => {
      if (d.arac === 'el' || o.button > 0) return;
      o.preventDefault();
      try { ust.setPointerCapture(o.pointerId); } catch { /* yapay olay */ }
      if (o.pointerType === 'touch') {
        dokunma.set(o.pointerId, [o.clientX, o.clientY]);
        if (dokunma.size >= 2) {                    // ikinci parmak: çizimi bırak, kaydırmaya geç
          clearTimeout(akilliZamanlayici);
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
      if (d.arac === 'damga' && d.damga) {
        const boy = Math.round(Math.max(22, KALINLIK[d.kalinlik] * 5.2));
        metinEkle(d.damga.s, [p[0] - boy * 0.35, p[1] - boy * 0.55], boy, d.damga.r || d.renk);
        return;
      }
      aktif = o.pointerId;
      bas = { x: o.clientX, y: o.clientY, t: performance.now(), uzak: 0 };

      // Seç ve Taşı aracı
      if (d.arac === 'sec') {
        const sb = secimKutuHesapla(d.secili);
        if (sb && p[0] >= sb[0] && p[0] <= sb[2] && p[1] >= sb[1] && p[1] <= sb[3]) {
          tasiBas = [p[0], p[1]]; tasiToplam = [0, 0];
          iste();
          return;
        }
        const vurulan = [...d.cizgiler].reverse().find((c) => noktaOgeyeYakinMi(c, p, 12));
        if (vurulan) {
          d.secili = o.shiftKey ? [...new Set([...d.secili, vurulan])] : [vurulan];
          tasiBas = [p[0], p[1]]; tasiToplam = [0, 0];
          guncelle(); iste();
          return;
        }
        d.secili = [];
        tasiBas = null;
        d.secimKutu = [p[0], p[1], p[0], p[1]];
        guncelle(); iste();
        return;
      }

      if (d.secili.length) { d.secili = []; guncelle(); }
      if (d.arac === 'odak') { iste(); return; }
      if (d.arac === 'lazer') {
        d.lazerIz.push([p[0], p[1], performance.now(), true]);
        iste();
        return;
      }
      if (d.arac === 'silgi' || d.arac === 'cizgisil') { oturumAc(); sonSilgi = null; silgiUygula(p); iste(); return; }
      if (SEKILLER.has(d.arac)) {
        d.canli = { arac: d.arac, sekil: d.arac, renk: d.renk, dolu: d.dolu, g: KALINLIK[d.kalinlik], bas: [p[0], p[1]], son: [p[0], p[1]], dik: o.shiftKey, n: [[p[0], p[1], 1]] };
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
      if (['silgi', 'kalem', 'fosforlu', 'kesikli', 'lazer', 'odak', 'damga'].includes(d.arac)) {
        d.imlec = guncelNokta;
        iste();
      }
      if (aktif === null && o.pointerType === 'mouse' && d.arac !== 'silgi' && d.arac !== 'cizgisil') {
        ust.style.cursor = alttaki(o.clientX, o.clientY) ? 'pointer' : (d.arac === 'metin' ? 'text' : d.arac === 'sec' ? 'move' : 'crosshair');
      }
      if (o.pointerId !== aktif) return;
      if (bas) bas.uzak = Math.max(bas.uzak, Math.hypot(o.clientX - bas.x, o.clientY - bas.y));

      if (d.arac === 'sec') {
        if (tasiBas && d.secili.length) {
          const dx = guncelNokta[0] - tasiBas[0], dy = guncelNokta[1] - tasiBas[1];
          tasiBas = [guncelNokta[0], guncelNokta[1]];
          tasiToplam[0] += dx; tasiToplam[1] += dy;
          for (const c of d.secili) ogeKaydir(c, dx, dy);
          hepsiniCiz();
        } else if (d.secimKutu) {
          d.secimKutu[2] = guncelNokta[0];
          d.secimKutu[3] = guncelNokta[1];
          const x0 = Math.min(d.secimKutu[0], d.secimKutu[2]), x1 = Math.max(d.secimKutu[0], d.secimKutu[2]);
          const y0 = Math.min(d.secimKutu[1], d.secimKutu[3]), y1 = Math.max(d.secimKutu[1], d.secimKutu[3]);
          d.secili = d.cizgiler.filter((c) => {
            const b = kutu(c);
            return !(b[2] < x0 || b[0] > x1 || b[3] < y0 || b[1] > y1);
          });
          iste();
        }
        return;
      }

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
      let ilerledi = false;
      for (const e of olaylar) {
        const ham = nokta(e), s = d.canli.n[d.canli.n.length - 1];
        const p = yumusat(s, ham);
        const mesafe = Math.hypot(p[0] - s[0], p[1] - s[1]);
        if (mesafe > 0.25) d.canli.n.push(p);
        if (mesafe > 2.2) ilerledi = true;
      }
      const ongorulen = o.getPredictedEvents?.() || [];
      d.tahmin = ongorulen.slice(0, 2).map((e) => nokta(e));
      // Kalemle çizim sonunda parmağı/kalemi kaldırmadan ~420ms bekleyince otomatik düzgün şekle dönüştür
      if (ilerledi && (d.arac === 'kalem' || d.arac === 'kesikli')) {
        clearTimeout(akilliZamanlayici);
        akilliZamanlayici = setTimeout(() => {
          if (!d.canli || d.canli.sekil || aktif === null) return;
          const taninan = akilliSekilTani(d.canli.n);
          if (taninan) {
            d.canli.sekil = taninan.sekil;
            d.canli.bas = taninan.bas;
            d.canli.son = sekilHedef(taninan.bas, taninan.son, taninan.sekil, false);
            d.canli.dolu = d.dolu;
            d.canli.otomatik = true;
            d.canli.n = sekilNoktalari(d.canli);
            d.tahmin = [];
            iste();
          }
        }, 420);
      }
      iste();
    });

    const bitir = (o) => {
      clearTimeout(akilliZamanlayici);
      dokunma.delete(o.pointerId);
      if (dokunma.size < 2) pan = null;
      if (o.pointerId !== aktif) return;
      aktif = null;
      d.tahmin = [];

      if (d.arac === 'sec') {
        if (tasiBas && (Math.abs(tasiToplam[0]) > 1 || Math.abs(tasiToplam[1]) > 1)) {
          d.gecmis.push({ tur: 'tasi', ogeler: [...d.secili], dx: tasiToplam[0], dy: tasiToplam[1] });
          d.ileri = [];
          bildir();
        }
        tasiBas = null;
        d.secimKutu = null;
        guncelle(); iste();
        return;
      }

      const hedef = o.type === 'pointerup' && bas && bas.uzak < 6 && performance.now() - bas.t < 500 ? alttaki(o.clientX, o.clientY) : null;
      const suruklendi = bas ? bas.uzak >= 4 : true;
      bas = null;
      if (hedef && d.canli) { d.canli = null; iste(); }
      if (oturum) { oturumKapat(); sonSilgi = null; }
      if (d.canli) {
        if (d.canli.sekil && !suruklendi) {
          d.canli = null; iste();
        } else {
          delete d.canli.otomatik;
          if (d.canli.sekil) d.canli.n = sekilNoktalari(d.canli);
          d.cizgiler.push(d.canli); d.gecmis.push({ tur: 'ekle', cizgi: d.canli }); d.ileri = [];
          cizgiCiz(d.canli, a, kay());
          d.canli = null; iste(); guncelle(); bildir();
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
      else if (g.tur === 'tasi') { for (const c of g.ogeler) ogeKaydir(c, -g.dx, -g.dy); }
      else d.cizgiler.push(...g.cizgiler);
      d.ileri.push(g); d.secili = []; hepsiniCiz(); guncelle(); bildir();
    };
    const yinele = () => {
      const g = d.ileri.pop(); if (!g) return;
      if (g.tur === 'ekle') d.cizgiler.push(g.cizgi);
      else if (g.tur === 'degistir') { d.cizgiler = d.cizgiler.filter((c) => !g.eski.includes(c)); d.cizgiler.push(...g.yeni); }
      else if (g.tur === 'tasi') { for (const c of g.ogeler) ogeKaydir(c, g.dx, g.dy); }
      else d.cizgiler = d.cizgiler.filter((c) => !g.cizgiler.includes(c));
      d.gecmis.push(g); d.secili = []; hepsiniCiz(); guncelle(); bildir();
    };
    const temizle = () => {
      if (!d.cizgiler.length) return;
      d.gecmis.push({ tur: 'sil', cizgiler: d.cizgiler });
      d.cizgiler = []; d.secili = []; d.ileri = [];
      hepsiniCiz(); guncelle(); bildir();
    };
    const seciliSil = () => {
      if (!d.secili.length) return;
      const silinen = [...d.secili];
      d.cizgiler = d.cizgiler.filter((c) => !silinen.includes(c));
      d.gecmis.push({ tur: 'degistir', eski: silinen, yeni: [] });
      d.ileri = []; d.secili = [];
      hepsiniCiz(); guncelle(); bildir();
    };
    const seciliCogalt = () => {
      if (!d.secili.length) return;
      const yeniler = d.secili.map((c) => ogeKopyala(c, 22, 22));
      d.cizgiler.push(...yeniler);
      d.gecmis.push({ tur: 'degistir', eski: [], yeni: yeniler });
      d.ileri = []; d.secili = yeniler;
      hepsiniCiz(); guncelle(); bildir();
    };

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

    // Sınıf içi yardımcı pencere 1: Sürüklenebilir Süre Ölçer (Kronometre / Geri Sayım)
    let sayacKutu = null, sayacInterval = 0, kalanSn = 60, sayacCalisiyor = false;
    function bipCal() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        [523.25, 659.25, 783.99].forEach((frekans, idx) => {
          const osc = ctx.createOscillator(), gain = ctx.createGain();
          osc.type = 'sine'; osc.frequency.value = frekans;
          gain.gain.setValueAtTime(0.15, ctx.currentTime + idx * 0.16);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.16 + 0.35);
          osc.connect(gain); gain.connect(ctx.destination);
          osc.start(ctx.currentTime + idx * 0.16);
          osc.stop(ctx.currentTime + idx * 0.16 + 0.36);
        });
      } catch { /* ses izni yok */ }
    }
    function sayacAcKapat() {
      if (sayacKutu) {
        clearInterval(sayacInterval); sayacCalisiyor = false;
        sayacKutu.remove(); sayacKutu = null; guncelle(); return;
      }
      sayacKutu = document.createElement('div');
      sayacKutu.className = 'tahta-sayac';
      const sureYaz = () => {
        const dk = String(Math.floor(kalanSn / 60)).padStart(2, '0');
        const sn = String(kalanSn % 60).padStart(2, '0');
        const ekran = sayacKutu?.querySelector('.ts-ekran');
        if (ekran) {
          ekran.textContent = `${dk}:${sn}`;
          ekran.classList.toggle('bitti', kalanSn === 0);
        }
      };
      sayacKutu.innerHTML =
        `<div class="ts-ust"><span>⏱ Soru Süresi</span><button type="button" data-ts="kapat" aria-label="Süre ölçeri kapat">✕</button></div>` +
        `<div class="ts-ekran" aria-live="polite">01:00</div>` +
        `<div class="ts-hazir">` +
        `<button type="button" data-sn="60">1 dk</button>` +
        `<button type="button" data-sn="120">2 dk</button>` +
        `<button type="button" data-sn="180">3 dk</button>` +
        `<button type="button" data-sn="300">5 dk</button>` +
        `<button type="button" data-ekle="30">+30 sn</button></div>` +
        `<div class="ts-eylem">` +
        `<button type="button" class="ts-ana" data-ts="baslat">Başlat</button>` +
        `<button type="button" data-ts="sifirla">Sıfırla</button></div>`;
      kap.append(sayacKutu);
      sureYaz();
      sayacKutu.addEventListener('click', (e) => {
        const b = e.target.closest('button'); if (!b) return;
        if (b.dataset.sn) { kalanSn = Number(b.dataset.sn); sureYaz(); }
        if (b.dataset.ekle) { kalanSn += Number(b.dataset.ekle); sureYaz(); }
        if (b.dataset.ts === 'sifirla') {
          clearInterval(sayacInterval); sayacCalisiyor = false; kalanSn = 60;
          sayacKutu.querySelector('[data-ts=baslat]').textContent = 'Başlat';
          sureYaz();
        }
        if (b.dataset.ts === 'baslat') {
          if (sayacCalisiyor) {
            clearInterval(sayacInterval); sayacCalisiyor = false; b.textContent = 'Devam';
          } else {
            if (kalanSn <= 0) kalanSn = 60;
            sayacCalisiyor = true; b.textContent = 'Duraklat';
            sayacInterval = setInterval(() => {
              if (kalanSn > 0) { kalanSn--; sureYaz(); }
              if (kalanSn <= 0) {
                clearInterval(sayacInterval); sayacCalisiyor = false;
                b.textContent = 'Başlat'; bipCal();
              }
            }, 1000);
          }
        }
        if (b.dataset.ts === 'kapat') sayacAcKapat();
      });
      guncelle();
    }

    // Sınıf içi yardımcı pencere 2: Cevap Gizleme Perdesi (Adım adım çözüm açma)
    let perdeOge = null;
    function perdeAcKapat() {
      if (perdeOge) { perdeOge.remove(); perdeOge = null; guncelle(); return; }
      perdeOge = document.createElement('div');
      perdeOge.className = 'tahta-perde';
      perdeOge.style.top = `${Math.round(yuk * 0.42)}px`;
      perdeOge.innerHTML =
        `<div class="tp-tutac"><span>↕ Çözümü adım adım göstermek için perdeyi aşağı sürükleyin</span>` +
        `<button type="button" aria-label="Perdeyi kapat">Perdeyi Kaldır ✕</button></div>`;
      kap.append(perdeOge);
      const tutac = perdeOge.querySelector('.tp-tutac');
      let perdeAktif = null, basY = 0, ilkTop = 0;
      tutac.addEventListener('pointerdown', (e) => {
        if (e.target.closest('button')) { perdeAcKapat(); return; }
        e.preventDefault(); e.stopPropagation();
        perdeAktif = e.pointerId; basY = e.clientY; ilkTop = parseFloat(perdeOge.style.top) || 200;
        try { tutac.setPointerCapture(e.pointerId); } catch { /* */ }
      });
      tutac.addEventListener('pointermove', (e) => {
        if (e.pointerId !== perdeAktif) return;
        const yeniTop = Math.max(48, Math.min(yuk - 44, ilkTop + (e.clientY - basY)));
        perdeOge.style.top = `${yeniTop}px`;
      });
      tutac.addEventListener('pointerup', () => { perdeAktif = null; });
      guncelle();
    }

    // Sınıf içi yardımcı pencere 3: Hatasız Ekran / Tahta ve Ses Kaydedici (MP4 & YouTube Uyumlu, Ekranda İzi Kalmayan Kayıt)
    let kayitKutu = null, kayitDurum = 'hazir'; // 'hazir' | 'kayitta' | 'duraklatildi'
    const ekranDestek = Boolean(typeof navigator !== 'undefined' && navigator.mediaDevices?.getDisplayMedia);
    let kayitModu = (kaydir && ekranDestek) ? 'ekran' : 'tuval'; // 'ekran': tüm sekme/ekran, 'tuval': doğrudan tahta (izinsiz)
    let kayitBicim = 'mp4'; // 'mp4' (Varsayılan MP4) | 'youtube' (YouTube 1080p HD MP4) | 'webm' (WebM)
    let mikIstek = true, tikirtiEngelleme = true, kayittaMenuyuGizle = true;
    let secilenDosyaAdi = '', otoMenuZamanlayici = 0;
    let kaydedici = null, kayitParcalar = [], kayitBlobUrl = null, kayitUzanti = 'mp4';
    let ekranAkisi = null, mikAkisi = null, birlesikAkis = null, sesBaglam = null;
    let kayitTimer = 0, tuvalTimer = 0, gecenMs = 0, sonTick = 0, kayitNot = '';
    const ilkSayfaBasligi = typeof document !== 'undefined' ? document.title : '';
    let muhurHazir = null;

    function muhurYukle() {
      if (muhurHazir) return muhurHazir;
      muhurHazir = new Promise((coz) => {
        const img = new Image();
        img.onload = () => coz(img);
        img.onerror = () => coz(null);
        img.src = '/simge-192.png';
      });
      return muhurHazir;
    }

    function sureBicimle(ms) {
      const topSn = Math.max(0, Math.floor(ms / 1000));
      const dk = String(Math.floor(topSn / 60)).padStart(2, '0');
      const sn = String(topSn % 60).padStart(2, '0');
      return `${dk}:${sn}`;
    }

    function adayKayitTurleri(sesVar, bicim) {
      if (typeof MediaRecorder === 'undefined' || !MediaRecorder.isTypeSupported) return [''];
      const mp4Sesli = [
        'video/mp4;codecs="avc1.64002A, mp4a.40.2"',
        'video/mp4;codecs="avc1.4D4028, mp4a.40.2"',
        'video/mp4;codecs="avc1.42E028, mp4a.40.2"',
        'video/mp4;codecs=avc1,mp4a.40.2',
        'video/mp4;codecs="avc1.42E01E, mp4a.40.2"',
        'video/mp4;codecs=h264,aac',
        'video/mp4;codecs=avc1,opus',
        'video/mp4;codecs=h264,opus',
        'video/mp4',
      ];
      const mp4Sessiz = [
        'video/mp4;codecs=avc1.64002A',
        'video/mp4;codecs=avc1.4D4028',
        'video/mp4;codecs=avc1.42E028',
        'video/mp4;codecs=avc1',
        'video/mp4;codecs=avc1.42E01E',
        'video/mp4;codecs=h264',
        'video/mp4',
      ];
      const webmSesli = [
        'video/webm;codecs=h264,opus',
        'video/webm;codecs=vp9,opus',
        'video/webm;codecs=vp8,opus',
        'video/webm',
      ];
      const webmSessiz = [
        'video/webm;codecs=h264',
        'video/webm;codecs=vp9',
        'video/webm;codecs=vp8',
        'video/webm',
      ];
      const mp4Liste = sesVar ? mp4Sesli : mp4Sessiz;
      const webmListe = sesVar ? webmSesli : webmSessiz;
      const tumAdaylar = bicim === 'webm' ? [...webmListe, ...mp4Liste] : [...mp4Liste, ...webmListe];
      const desteklenen = tumAdaylar.filter((tur) => {
        try { return MediaRecorder.isTypeSupported(tur); } catch { return false; }
      });
      return [...desteklenen, ''];
    }

    function kayitUstDugmeGuncelle() {
      const ustVideoBtn = document.getElementById('t-video');
      if (ustVideoBtn) {
        const aktif = kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi';
        ustVideoBtn.innerHTML = aktif
          ? `<span class="kayit-nokta"></span>⏹ Kaydı Bitir (${sureBicimle(gecenMs)})`
          : `<span class="kayit-nokta"></span>Ders Kaydı`;
        ustVideoBtn.classList.toggle('aktif-kayit', aktif);
      }
    }

    function kayitKaynakTemizle() {
      clearInterval(kayitTimer); kayitTimer = 0;
      clearInterval(tuvalTimer); tuvalTimer = 0;
      clearTimeout(otoMenuZamanlayici);
      for (const akis of [ekranAkisi, mikAkisi, birlesikAkis]) {
        if (!akis) continue;
        try { akis.getTracks().forEach((t) => t.stop()); } catch { /* */ }
      }
      ekranAkisi = null; mikAkisi = null; birlesikAkis = null;
      if (sesBaglam) {
        try { if (sesBaglam.state !== 'closed') sesBaglam.close(); } catch { /* */ }
        sesBaglam = null;
      }
      if (typeof document !== 'undefined' && ilkSayfaBasligi) {
        document.title = ilkSayfaBasligi;
      }
      kayitUstDugmeGuncelle();
    }

    function kayitKutuyuYokEt() {
      if (kayitKutu) {
        kayitKutu.hidden = true;
        kayitKutu.style.display = 'none';
        kayitKutu.remove();
        kayitKutu = null;
      }
    }

    // Kayıt sırasında alttaki menü videoda görünmesin diye gizlendiğinde, farenin/kalemin ekranın altına gelmesiyle geçici açılır
    function kayittaMenuyuGeciciGoster() {
      if (kayitDurum !== 'kayitta' && kayitDurum !== 'duraklatildi') return;
      if (!kayittaMenuyuGizle || typeof cubuk === 'undefined' || !cubuk) return;
      cubuk.classList.remove('kayitta-gizli');
      clearTimeout(otoMenuZamanlayici);
      otoMenuZamanlayici = setTimeout(() => {
        if (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') {
          cubuk.classList.add('kayitta-gizli');
        }
      }, 3400);
    }

    async function tuvalAkisiHazirla() {
      const kTuval = document.createElement('canvas');
      const hamG = alt.width || Math.round((gen || 1280) * oran);
      const hamY = alt.height || Math.round((yuk || 720) * oran);
      const hedefMax = kayitBicim === 'youtube' ? 1920 : 1600;
      const olcek = Math.min(1, hedefMax / Math.max(hamG, hamY, 1));
      // Donanım H.264/MP4 kodlayıcıları çift sayı genişlik/yükseklik ister
      kTuval.width = Math.max(640, Math.round((hamG * olcek) / 2) * 2);
      kTuval.height = Math.max(360, Math.round((hamY * olcek) / 2) * 2);
      const kx = kTuval.getContext('2d', { alpha: false });
      const muhur = await muhurYukle();
      const kareCiz = () => {
        const w = kTuval.width, h = kTuval.height;
        kx.fillStyle = d.zemin === 'koyu' ? '#132620' : '#fdfdfb';
        kx.fillRect(0, 0, w, h);
        try {
          if (alt.width && alt.height) kx.drawImage(alt, 0, 0, w, h);
          if (ust.width && ust.height) kx.drawImage(ust, 0, 0, w, h);
        } catch { /* */ }
        const b = Math.round(Math.min(w, h) * 0.045), p = Math.round(b * 0.32);
        if (muhur) {
          try { kx.drawImage(muhur, w - b - p, h - b - p, b, b); } catch { /* */ }
        }
        kx.font = `700 ${Math.max(12, Math.round(b * 0.28))}px -apple-system, "Segoe UI", Roboto, Arial, sans-serif`;
        kx.fillStyle = d.zemin === 'koyu' ? 'rgba(233,238,246,.82)' : 'rgba(11,34,87,.78)';
        kx.textAlign = 'right';
        kx.textBaseline = 'middle';
        kx.fillText('derskutusu.com', w - b - p - 8, h - p - b / 2);
      };
      kareCiz();
      tuvalTimer = setInterval(kareCiz, 33); // 30 FPS sabit kare üretimi
      const akis = kTuval.captureStream ? kTuval.captureStream(30) : kTuval.mozCaptureStream?.(30);
      if (!akis) throw new Error('Tarayıcı tuval video akışını desteklemiyor.');
      return akis;
    }

    function varsayilanDosyaAdi() {
      const baslik = (document.querySelector('h1')?.textContent || 'ders-kaydi')
        .toLocaleLowerCase('tr')
        .replace(/[^a-z0-9çğıöşü]+/g, '-')
        .replace(/^-|-$/g, '')
        .slice(0, 42) || 'ders-kaydi';
      const simdi = new Date();
      const tarih = `${simdi.getFullYear()}${String(simdi.getMonth() + 1).padStart(2, '0')}${String(simdi.getDate()).padStart(2, '0')}-${String(simdi.getHours()).padStart(2, '0')}${String(simdi.getMinutes()).padStart(2, '0')}`;
      return `derskutusu-${baslik}-${tarih}`;
    }

    function kayitKutuCiz() {
      // Kayıt sırasında veya kayıt bittikten sonra ekranda kesinlikle kayıt programı penceresi gösterilmez
      if (kayitDurum !== 'hazir') {
        kayitKutuyuYokEt();
        guncelle();
        return;
      }
      if (!kayitKutu) return;
      const dosyaAdDeger = secilenDosyaAdi || varsayilanDosyaAdi();
      kayitKutu.innerHTML =
        `<div class="tk-ust"><span>🎥 Ders ve Ses Kaydedici</span><button type="button" data-tk="kapat" aria-label="Kaydediciyi kapat">✕</button></div>` +
        `<div class="tk-govde">` +
        `<div class="tk-kip-grup" role="radiogroup" aria-label="Kayıt alanı">` +
        `<button type="button" class="tk-kip${kayitModu === 'tuval' ? ' etkin' : ''}" data-kip="tuval">` +
        `<strong>🎨 Sadece Tahta + Ses</strong><small>Hiçbir araç çubuğu ve pencere görünmeden yalnızca tahtayı ve sesinizi kaydeder</small></button>` +
        (ekranDestek
          ? `<button type="button" class="tk-kip${kayitModu === 'ekran' ? ' etkin' : ''}" data-kip="ekran">` +
            `<strong>🖥️ Tüm Ekran / Sekme + Ses</strong><small>Konu anlatımı metnini, PDF'i ve kalem çizimlerini birlikte kaydeder</small></button>`
          : '') +
        `</div>` +
        `<div class="tk-bicim-grup" role="radiogroup" aria-label="Video kayıt uzantısı">` +
        `<button type="button" class="tk-bicim${kayitBicim === 'mp4' ? ' etkin' : ''}" data-bicim="mp4">` +
        `<strong>🎬 MP4 (.mp4)</strong><small>Tüm cihazlar & WhatsApp</small></button>` +
        `<button type="button" class="tk-bicim${kayitBicim === 'youtube' ? ' etkin' : ''}" data-bicim="youtube">` +
        `<strong>▶️ YouTube HD (.mp4)</strong><small>1080p YouTube yükleme</small></button>` +
        `<button type="button" class="tk-bicim${kayitBicim === 'webm' ? ' etkin' : ''}" data-bicim="webm">` +
        `<strong>🌐 WebM (.webm)</strong><small>YouTube & Web</small></button>` +
        `</div>` +
        `<label class="tk-ad-etiket">Dosya adı:<input type="text" class="tk-dosya-ad" value="${dosyaAdDeger}" spellcheck="false"></label>` +
        `<label class="tk-secenek"><input type="checkbox" data-tk-mik ${mikIstek ? 'checked' : ''}><span>🎙️ Mikrofon sesimi kayda ekle</span></label>` +
        `<label class="tk-secenek"><input type="checkbox" data-tk-tikirti ${tikirtiEngelleme ? 'checked' : ''}><span>🛡️ Klavye tuş ve tablet ekranına vurma seslerini filtrele</span></label>` +
        `<label class="tk-secenek"><input type="checkbox" data-tk-menugizle ${kayittaMenuyuGizle ? 'checked' : ''}><span>🪄 Kayıt sırasında alttaki kalem menüsünü gizle (videoda görünmez)</span></label>` +
        `<p class="tk-ipucu-mini">💡 Kayıt başladığında bu pencere ve kalem menüsü otomatik gizlenir. Bitirmek için <b>F9</b> tuşuna veya ekranın altına yaklaşıp kırmızı <b>⏹ Kayıt</b> düğmesine basın; video otomatik indirilir.</p>` +
        (kayitNot ? `<p class="tk-not" role="status">${kayitNot}</p>` : '') +
        `<button type="button" class="tk-baslat" data-tk="baslat"><i class="tk-kirmizi-nokta"></i> Kaydı Başlat (.${kayitBicim === 'webm' ? 'WEBM' : 'MP4'})</button>` +
        `</div>`;
      guncelle();
    }

    async function kaydiBaslat(zorlaKip = null) {
      if (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') return;
      if (zorlaKip) kayitModu = zorlaKip;
      const adGirdi = kayitKutu?.querySelector('.tk-dosya-ad');
      secilenDosyaAdi = (adGirdi?.value || varsayilanDosyaAdi()).trim().replace(/\.(webm|mp4|mov)$/i, '') || varsayilanDosyaAdi();
      kayitNot = '';
      kayitKaynakTemizle();
      if (kayitBlobUrl) { try { URL.revokeObjectURL(kayitBlobUrl); } catch { /* */ } kayitBlobUrl = null; }

      // ÖNEMLİ: Kayıt penceresini görüntü yakalama başlamadan ÖNCE ekrandan tamamen kaldır (videoda asla görünmesin)
      kayitKutuyuYokEt();
      if (yardimKutu) { yardimKutu.remove(); yardimKutu = null; }
      guncelle();

      // Alttaki kalem menüsünün videoda görünmemesi için kayıtta gizle
      if (kayittaMenuyuGizle && typeof cubuk !== 'undefined' && cubuk) {
        cubuk.classList.add('kayitta-gizli');
      }

      // 1) Görüntü akışını hazırla
      try {
        if (kayitModu === 'ekran' && ekranDestek) {
          ekranAkisi = await navigator.mediaDevices.getDisplayMedia({
            video: {
              width: { ideal: 1920, max: 1920 },
              height: { ideal: 1080, max: 1080 },
              frameRate: { ideal: 30, max: 30 },
              cursor: 'always',
            },
            audio: true,
            preferCurrentTab: true,
            selfBrowserSurface: 'include',
            systemAudio: 'include',
          });
        } else {
          kayitModu = 'tuval';
          ekranAkisi = await tuvalAkisiHazirla();
        }
      } catch {
        // Kullanıcı ekran paylaşımını iptal ettiyse Tahta + Ses kipine yönlendir
        if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.remove('kayitta-gizli');
        kayitModu = 'tuval';
        kayitNot = 'Ekran paylaşımı seçilmedi. "🎨 Sadece Tahta + Ses" kipinde izin gerekmeden hemen kayıt başlatabilirsiniz.';
        kayitAcKapat();
        return;
      }

      // 2) Mikrofon akışını hazırla (tuş ve ekran vurma seslerini filtreleyen gelişmiş constraints)
      if (mikIstek && navigator.mediaDevices?.getUserMedia) {
        try {
          mikAkisi = await navigator.mediaDevices.getUserMedia({
            audio: {
              echoCancellation: true,
              noiseSuppression: true,
              autoGainControl: true,
              channelCount: 1,
              sampleRate: 48000,
              googEchoCancellation: true,
              googAutoGainControl: true,
              googNoiseSuppression: true,
              googHighpassFilter: true,
              googTypingNoiseDetection: true,
            },
          });
        } catch {
          mikAkisi = null;
        }
      }

      // 3) Görüntü ve ses kanallarını birleştir + Tablet Vuruşu/Tuş Ses Filtresi
      const videoIzleri = ekranAkisi ? ekranAkisi.getVideoTracks() : [];
      if (!videoIzleri.length) {
        kayitKaynakTemizle();
        if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.remove('kayitta-gizli');
        kayitModu = 'tuval';
        kayitNot = 'Görüntü kaynağı alınamadı. "🎨 Sadece Tahta + Ses" kipini deneyin.';
        kayitAcKapat();
        return;
      }
      let sesIzleri = [];
      const ekranSes = ekranAkisi ? ekranAkisi.getAudioTracks() : [];
      const mikSes = mikAkisi ? mikAkisi.getAudioTracks() : [];
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (AudioCtx && (mikSes.length || ekranSes.length)) {
          sesBaglam = new AudioCtx();
          if (sesBaglam.state === 'suspended') await sesBaglam.resume().catch(() => {});
          const hedef = sesBaglam.createMediaStreamDestination();
          if (ekranSes.length) {
            const k1 = sesBaglam.createMediaStreamSource(new MediaStream(ekranSes));
            k1.connect(hedef);
          }
          if (mikSes.length) {
            const k2 = sesBaglam.createMediaStreamSource(new MediaStream(mikSes));
            if (tikirtiEngelleme) {
              // 1. Kademe: Yüksek Geçiren Filtre (Highpass 140Hz) - Masaya, tablete el/avuç temas sarsıntısı ve gövde gümlemelerini keser
              const hp = sesBaglam.createBiquadFilter();
              hp.type = 'highpass';
              hp.frequency.value = 140;
              hp.Q.value = 0.7;

              // 2. Kademe: Klavye tuş basımı ve cam tıkırtısı rezonans çentiği (Peaking 2850Hz)
              const notch = sesBaglam.createBiquadFilter();
              notch.type = 'peaking';
              notch.frequency.value = 2850;
              notch.Q.value = 2.2;
              notch.gain.value = -8;

              // 3. Kademe: Alçak Geçiren Filtre (Lowpass 5200Hz) - Kalem ucunun cam ekrana çarpma kliklerinin tizliğini keser
              const lp = sesBaglam.createBiquadFilter();
              lp.type = 'lowpass';
              lp.frequency.value = 5200;
              lp.Q.value = 0.7;

              // 4. Kademe: Hızlı Kompresör (DynamicsCompressor) - Ani vuruş patlamalarını 2ms içinde bastırır
              const comp = sesBaglam.createDynamicsCompressor();
              comp.threshold.value = -23;
              comp.knee.value = 8;
              comp.ratio.value = 16;
              comp.attack.value = 0.002;
              comp.release.value = 0.12;

              // 5. Kademe: Akıllı Konuşma Kapısı (Smart Voice Gate) - Konuşma yokken kalemin ekrana dokunma ve vurma seslerini %100 susturur
              let zarf = 0;
              let kapiKazanc = 0;
              const KONUSMA_ESIGI = 0.015;
              const gate = sesBaglam.createScriptProcessor(1024, 1, 1);
              gate.onaudioprocess = (e) => {
                const inp = e.inputBuffer.getChannelData(0);
                const out = e.outputBuffer.getChannelData(0);
                let maks = 0;
                for (let i = 0; i < inp.length; i++) {
                  const m = Math.abs(inp[i]);
                  if (m > maks) maks = m;
                }
                if (maks > zarf) {
                  zarf = zarf * 0.35 + maks * 0.65;
                } else {
                  zarf = zarf * 0.94; // yumuşak sönüm
                }
                const hedefK = zarf > KONUSMA_ESIGI ? 1.0 : 0.0;
                for (let i = 0; i < inp.length; i++) {
                  kapiKazanc += (hedefK - kapiKazanc) * 0.025;
                  out[i] = inp[i] * (kapiKazanc < 0.005 ? 0 : kapiKazanc);
                }
              };

              k2.connect(hp);
              hp.connect(notch);
              notch.connect(lp);
              lp.connect(comp);
              comp.connect(gate);
              gate.connect(hedef);
            } else {
              k2.connect(hedef);
            }
          }
          sesIzleri = hedef.stream.getAudioTracks();
        }
      } catch {
        sesIzleri = mikSes.length ? mikSes : ekranSes;
      }
      if (!sesIzleri.length && (mikSes.length || ekranSes.length)) {
        sesIzleri = mikSes.length ? mikSes : ekranSes;
      }

      birlesikAkis = new MediaStream([...videoIzleri, ...sesIzleri]);
      videoIzleri[0].addEventListener('ended', () => {
        if (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') kaydiBitir();
      });

      // Ekranın tamamen temiz olduğundan emin olmak için iki animasyon karesi bekle
      await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));

      // 4) MediaRecorder başlat (MP4 / YouTube HD öncelikli çok katmanlı başlatıcı)
      kayitParcalar = [];
      const bitHizi = kayitBicim === 'youtube' ? 4500000 : 2800000;
      const adaylar = adayKayitTurleri(sesIzleri.length > 0, kayitBicim);
      kaydedici = null;

      for (const tur of adaylar) {
        try {
          const mr = tur
            ? new MediaRecorder(birlesikAkis, { mimeType: tur, videoBitsPerSecond: bitHizi })
            : new MediaRecorder(birlesikAkis);
          mr.ondataavailable = (e) => {
            if (e.data && e.data.size > 0) kayitParcalar.push(e.data);
          };
          mr.start(1000);
          kaydedici = mr;
          break;
        } catch {
          // Bu profil/codec mevcut ekran çözünürlüğüyle başlamadıysa sıradaki MP4/YouTube adayına geç
        }
      }

      if (!kaydedici) {
        try {
          kaydedici = new MediaRecorder(birlesikAkis);
          kaydedici.ondataavailable = (e) => {
            if (e.data && e.data.size > 0) kayitParcalar.push(e.data);
          };
          kaydedici.start();
        } catch {
          kayitKaynakTemizle();
          if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.remove('kayitta-gizli');
          kayitNot = 'Bu tarayıcıda video kaydı başlatılamadı.';
          kayitAcKapat();
          return;
        }
      }

      kaydedici.onerror = () => {
        if (kayitParcalar.length) kaydiBitir();
        else {
          kayitKaynakTemizle();
          if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.remove('kayitta-gizli');
          kayitDurum = 'hazir';
          kayitKutuyuYokEt();
          guncelle();
        }
      };

      kaydedici.onstop = () => {
        // Kayıt bittiğinde ekranda hiçbir kayıt programı penceresi açılmaz; doğrudan seçilen uzantıyla (.mp4 / .webm) indirilir
        kayitKutuyuYokEt();
        if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.remove('kayitta-gizli');
        const etkinTur = kaydedici?.mimeType || kayitParcalar[0]?.type || 'video/mp4';
        kayitUzanti = kayitBicim === 'webm' ? 'webm' : 'mp4';
        const ciktiMime = kayitUzanti === 'mp4' ? (etkinTur.includes('mp4') ? etkinTur : 'video/mp4') : 'video/webm';
        const blob = new Blob(kayitParcalar, { type: ciktiMime });
        if (kayitBlobUrl) { try { URL.revokeObjectURL(kayitBlobUrl); } catch { /* */ } }
        kayitBlobUrl = URL.createObjectURL(blob);
        kayitKaynakTemizle();
        kayitDurum = 'hazir';
        guncelle();
        if (blob.size > 0) {
          kaydiIndir();
        }
      };

      gecenMs = 0;
      sonTick = performance.now();
      kayitDurum = 'kayitta';
      kayitTimer = setInterval(() => {
        if (kayitDurum !== 'kayitta') return;
        const simdi = performance.now();
        gecenMs += simdi - sonTick;
        sonTick = simdi;
        const sureMetin = sureBicimle(gecenMs);
        if (typeof document !== 'undefined' && ilkSayfaBasligi) {
          document.title = `🔴 ${sureMetin} — ${ilkSayfaBasligi}`;
        }
        const kayitBtn = cubuk?.querySelector('[data-is=kayit]');
        if (kayitBtn) {
          kayitBtn.title = `Kaydı bitir ve .${kayitBicim === 'webm' ? 'WEBM' : 'MP4'} olarak indir (${sureMetin} — F9)`;
        }
        kayitUstDugmeGuncelle();
      }, 500);
      kayitUstDugmeGuncelle();
      guncelle();
    }

    function kaydiBitir() {
      // Kayıt biterken kayıt programı penceresi kapalı tutulur ve kalem menüsü geri getirilir
      kayitKutuyuYokEt();
      if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.remove('kayitta-gizli');
      clearTimeout(otoMenuZamanlayici);
      if (!kaydedici || kaydedici.state === 'inactive') {
        kayitKaynakTemizle();
        kayitDurum = 'hazir';
        guncelle();
        return;
      }
      if (kayitDurum === 'kayitta') gecenMs += performance.now() - sonTick;
      try { if (kaydedici.state === 'recording') kaydedici.requestData(); } catch { /* */ }
      try {
        kaydedici.stop();
      } catch {
        kayitKaynakTemizle();
        kayitDurum = 'hazir';
        guncelle();
      }
    }

    function kaydiIndir() {
      if (!kayitBlobUrl) return;
      const hamAd = (secilenDosyaAdi || varsayilanDosyaAdi()).trim().replace(/\.(webm|mp4|mov)$/i, '') || 'derskutusu-ders-kaydi';
      const a = document.createElement('a');
      a.href = kayitBlobUrl;
      a.download = `${hamAd}.${kayitUzanti}`;
      document.body.append(a);
      a.click();
      a.remove();
      setTimeout(() => {
        if (kayitBlobUrl) { try { URL.revokeObjectURL(kayitBlobUrl); } catch { /* */ } kayitBlobUrl = null; }
      }, 15000);
    }

    function kayitAcKapat() {
      // Kayıt sürerken kayıt düğmesine basılırsa doğrudan kaydı bitir ve MP4 olarak indir (pencere açma)
      if (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') {
        kaydiBitir();
        return;
      }
      if (kayitKutu) {
        kayitKaynakTemizle();
        kayitKutuyuYokEt();
        kayitDurum = 'hazir';
        kayitNot = '';
        guncelle();
        return;
      }
      secilenDosyaAdi = varsayilanDosyaAdi();
      kayitKutu = document.createElement('div');
      kayitKutu.className = 'tahta-kayit';
      kayitKutu.setAttribute('role', 'region');
      kayitKutu.setAttribute('aria-label', 'Ders ve ses kaydedici');
      kap.append(kayitKutu);

      // Başlıktan sürükleme
      let tkSurukle = null, tkKonum = [0, 0], tkBas = [0, 0];
      kayitKutu.addEventListener('pointerdown', (e) => {
        const ustBar = e.target.closest('.tk-ust');
        if (!ustBar || e.target.closest('button')) return;
        e.preventDefault(); e.stopPropagation();
        tkSurukle = e.pointerId;
        tkBas = [e.clientX - tkKonum[0], e.clientY - tkKonum[1]];
        try { ustBar.setPointerCapture(e.pointerId); } catch { /* */ }
      });
      kayitKutu.addEventListener('pointermove', (e) => {
        if (e.pointerId !== tkSurukle) return;
        tkKonum = [e.clientX - tkBas[0], e.clientY - tkBas[1]];
        kayitKutu.style.translate = `${tkKonum[0]}px ${tkKonum[1]}px`;
      });
      kayitKutu.addEventListener('pointerup', () => { tkSurukle = null; });

      kayitKutu.addEventListener('input', (e) => {
        if (e.target.matches('.tk-dosya-ad')) secilenDosyaAdi = e.target.value;
      });
      kayitKutu.addEventListener('change', (e) => {
        if (e.target.matches('[data-tk-mik]')) mikIstek = e.target.checked;
        if (e.target.matches('[data-tk-tikirti]')) tikirtiEngelleme = e.target.checked;
        if (e.target.matches('[data-tk-menugizle]')) kayittaMenuyuGizle = e.target.checked;
      });
      kayitKutu.addEventListener('click', (e) => {
        const kipBtn = e.target.closest('[data-kip]');
        if (kipBtn) {
          kayitModu = kipBtn.dataset.kip;
          kayitNot = '';
          kayitKutuCiz();
          return;
        }
        const bicimBtn = e.target.closest('[data-bicim]');
        if (bicimBtn) {
          kayitBicim = bicimBtn.dataset.bicim;
          kayitKutuCiz();
          return;
        }
        const b = e.target.closest('button[data-tk]');
        if (!b) return;
        const islem = b.dataset.tk;
        if (islem === 'kapat') kayitAcKapat();
        else if (islem === 'baslat') kaydiBaslat();
      });
      kayitKutuCiz();
    }

    // Kısayol ve ipucu yardım penceresi
    let yardimKutu = null;
    function yardimAcKapat() {
      if (yardimKutu) { yardimKutu.remove(); yardimKutu = null; guncelle(); return; }
      yardimKutu = document.createElement('div');
      yardimKutu.className = 'tahta-yardim';
      yardimKutu.innerHTML =
        `<div class="ty-ust"><strong>Akıllı Tahta İpuçları ve Kısayollar</strong><button type="button" aria-label="Kapat">✕</button></div>` +
        `<ul>` +
        `<li><b>🎥 Ders ve Ses Kaydı:</b> Araç çubuğundaki <b>● Kayıt</b> düğmesiyle ders anlatırken hem tahtayı/ekranı hem de mikrofon sesinizi kaydedip video olarak indirebilirsiniz.</li>` +
        `<li><b>✨ Akıllı Şekil Tanıma:</b> Serbest kalemle düz çizgi, çember, dikdörtgen veya üçgen çizip <b>kalemi kaldırmadan yarım saniye beklerseniz</b> otomatik düzgün geometrik şekle dönüşür.</li>` +
        `<li><b>📋 Soru Görseli Yapıştırma (Ctrl+V):</b> Ekran görüntüsü aldığınız bir soruyu doğrudan <b>Ctrl+V</b> ile tahtaya yapıştırıp üzerinde çözebilirsiniz.</li>` +
        `<li><b>✋ Seç ve Taşı (V):</b> Çizdiğiniz şekilleri, metinleri veya yapıştırdığınız görselleri seçip taşıyabilir, rengini değiştirebilir, <b>Ctrl+D</b> ile çoğaltabilir veya <b>Delete</b> ile silebilirsiniz.</li>` +
        `<li><b>📐 Açı ve Oran Kilitleme (Shift):</b> Cetvel/ok çizerken <b>Shift</b> basılı tutulursa 45° açılara kilitlenir; dikdörtgen/çemberde tam kare/daire, üçgende dik üçgen çizer.</li>` +
        `<li><b>⌨️ Hızlı Kısayollar:</b> <kbd>K</kbd> Kalem · <kbd>F</kbd> Fosforlu · <kbd>N</kbd> Kesikli · <kbd>L</kbd> Lazer · <kbd>S</kbd> Silgi · <kbd>Ç</kbd> Çizgi Sil · <kbd>V</kbd> Seç/Taşı · <kbd>D</kbd> Cetvel · <kbd>O</kbd> Ok · <kbd>R</kbd> Kutu · <kbd>M</kbd> Çember · <kbd>U</kbd> Üçgen · <kbd>X</kbd> Eksen · <kbd>T</kbd> Metin · <kbd>G</kbd> Odak · <kbd>Ctrl+Z</kbd> Geri Al</li>` +
        `</ul>`;
      yardimKutu.querySelector('button').addEventListener('click', yardimAcKapat);
      kap.append(yardimKutu);
      guncelle();
    }

    // Araç çubuğu
    const cubuk = document.createElement('div');
    cubuk.className = 'tahta-cubuk';
    cubuk.setAttribute('role', 'toolbar');
    cubuk.setAttribute('aria-label', 'Tahta araçları');
    const dugme = (ad, ic, is, ek = '') => `<button type="button" class="${ek}" data-${ad}="${is}" title="${ic.baslik}" aria-label="${ic.baslik}">${ic.html}</button>`;
    const yazimAraclari = [
      ['kalem', 'Hassas kalem — çizim sonunda beklerseniz otomatik şekle dönüşür (K)'],
      ['fosforlu', 'Fosforlu vurgu kalemi (F)'],
      ['kesikli', 'Kesikli çizgi kalemi (N)'],
      ['lazer', 'Lazer işaretçi — izi kendiliğinden silinir (L)'],
      ['silgi', 'Kısmi silgi: değdiği yeri siler (S)'],
      ['cizgisil', 'Çizgi / şekil silgisi: tamamını siler (Ç)'],
      ['sec', 'Seç ve taşı: çizimleri seçip taşı, renklendir veya çoğalt (V)'],
    ];
    const sekilAraclari = [
      ['cizgi', 'Cetvel / düz çizgi — Shift ile açı kilitler (D)'],
      ['ok', 'Ok / vektör çizimi (O)'],
      ['dikdortgen', 'Dikdörtgen / kutu — Shift ile kare (R)'],
      ['cember', 'Çember / elips — Shift ile tam çember (M)'],
      ['ucgen', 'Üçgen — Shift ile dik üçgen (U)'],
      ['eksen', 'Sayı doğrusu / koordinat ekseni (X)'],
      ['metin', 'Metin / etiket ekle (T)'],
      ['damga', 'Hızlı ders damgaları: ✓ ✗ ★ ! ? ∠ ⊥ (B)'],
      ['odak', 'Odak / spot ışığı perdesi (G)'],
      ...(kaydir ? [['el', 'Sayfayı kaydır (E) — iki parmakla da kaydırabilirsiniz']] : []),
    ];
    cubuk.innerHTML =
      `<button type="button" class="tahta-tutac" data-is="tutac" title="Araç çubuğunu sürükle (çift tıkla: merkeze sıfırla)" aria-label="Araç çubuğunu taşı">` +
      `<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="6" r="1.5" fill="currentColor"/><circle cx="15" cy="6" r="1.5" fill="currentColor"/><circle cx="9" cy="12" r="1.5" fill="currentColor"/><circle cx="15" cy="12" r="1.5" fill="currentColor"/><circle cx="9" cy="18" r="1.5" fill="currentColor"/><circle cx="15" cy="18" r="1.5" fill="currentColor"/></svg></button>` +
      `<div class="tahta-grup">${yazimAraclari.map(([is, b]) => dugme('arac', { baslik: b, html: svg(ARAC_SIMGE[is]) }, is)).join('')}</div>` +
      `<div class="tahta-grup tahta-gizlenebilir">${sekilAraclari.map(([is, b]) => dugme('arac', { baslik: b, html: svg(ARAC_SIMGE[is]) }, is)).join('')}` +
      dugme('is', { baslik: 'Şekillerin içini yarı saydam doldur', html: svg('M12 3l9 9-9 9-9-9 9-9z') }, 'dolgu') +
      dugme('is', { baslik: 'Soru görseli ekle (veya Ctrl+V ile yapıştır)', html: svg(ARAC_SIMGE.resim) }, 'resim') + `</div>` +
      `<div class="tahta-grup tahta-gizlenebilir">${Object.keys(KALINLIK).map((k) => {
        const cap = Math.max(3, Math.min(16, Math.round(KALINLIK[k] + 2)));
        return dugme('kalinlik', { baslik: `Kalınlık: ${KALINLIK_AD[k]}`, html: `<i style="width:${cap}px;height:${cap}px"></i>` }, k, 'kalin');
      }).join('')}</div>` +
      `<div class="tahta-grup">${RENKLER.map((r, i) => dugme('renk', { baslik: `Renk ${i + 1}`, html: `<span style="background:${r}"></span>` }, r, 'renk')).join('')}` +
      `<label class="tahta-ozel-renk" title="Özel renk seç" aria-label="Özel renk seç"><input type="color" value="${d.renk}"><span></span></label></div>` +
      `<div class="tahta-grup">` +
      dugme('is', { baslik: 'Ders anlatımı ekran ve ses kaydı al', html: '<span class="kayit-simge" aria-hidden="true"></span>' }, 'kayit', 'kayit-dugme') +
      dugme('is', { baslik: 'Sınıf süre ölçeri / kronometre aç', html: svg('M12 8v5l3 2M12 4a9 9 0 100 18 9 9 0 000-18zM9 2h6') }, 'sayac', 'tahta-gizlenebilir') +
      dugme('is', { baslik: 'Cevap gizleme perdesi aç', html: svg('M3 5h18v9H3zM8 18l4-3 4 3M12 14v7') }, 'perde', 'tahta-gizlenebilir') + `</div>` +
      `<div class="tahta-grup">` +
      dugme('is', { baslik: 'Geri al (Ctrl+Z)', html: svg('M9 14L4 9l5-5M4 9h10a6 6 0 010 12h-3') }, 'geri') +
      dugme('is', { baslik: 'İleri al (Ctrl+Y)', html: svg('M15 14l5-5-5-5M20 9H10a6 6 0 000 12h3') }, 'ileri') +
      dugme('is', { baslik: 'Çizimi PNG olarak indir', html: svg('M12 4v11m-5-5 5 5 5-5M5 20h14') }, 'indir', 'tahta-gizlenebilir') +
      dugme('is', { baslik: 'Hepsini temizle', html: svg('M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3') }, 'temizle') +
      dugme('is', { baslik: 'İpuçları ve klavye kısayolları (?)', html: '<b style="font-size:15px">?</b>' }, 'yardim', 'tahta-gizlenebilir') +
      dugme('is', { baslik: 'Araç çubuğunu küçült / genişlet', html: svg('M15 18l-6-6 6-6') }, 'daralt') +
      (kapat ? dugme('is', { baslik: 'Kalemi kapat (Esc)', html: svg('M6 6l12 12M18 6L6 18') }, 'kapat', 'kapat') : '') + `</div>` +
      `<div class="tahta-altpanel" hidden></div>`;
    kap.append(cubuk);
    sabitBoy(cubuk);

    // Araç çubuğunu tutaçtan sürükleme (yazı yazılacak alanı kapatmaması için)
    const tutacDugme = cubuk.querySelector('[data-is=tutac]');
    let cubukSurukle = null, cubukKonum = [0, 0], cubukBas = [0, 0];
    tutacDugme?.addEventListener('pointerdown', (e) => {
      e.preventDefault(); e.stopPropagation();
      cubukSurukle = e.pointerId;
      cubukBas = [e.clientX - cubukKonum[0], e.clientY - cubukKonum[1]];
      try { tutacDugme.setPointerCapture(e.pointerId); } catch { /* */ }
    });
    tutacDugme?.addEventListener('pointermove', (e) => {
      if (e.pointerId !== cubukSurukle) return;
      cubukKonum = [e.clientX - cubukBas[0], e.clientY - cubukBas[1]];
      cubuk.style.translate = `${cubukKonum[0]}px ${cubukKonum[1]}px`;
    });
    tutacDugme?.addEventListener('pointerup', () => { cubukSurukle = null; });
    tutacDugme?.addEventListener('dblclick', () => { cubukKonum = [0, 0]; cubuk.style.translate = ''; });

    const altPanel = cubuk.querySelector('.tahta-altpanel');
    const ozelRenkGirdi = cubuk.querySelector('.tahta-ozel-renk input');

    function altPanelGuncelle() {
      if (!altPanel) return;
      if (d.arac === 'damga') {
        altPanel.hidden = false;
        altPanel.innerHTML = DAMGALAR.map((dm, idx) =>
          `<button type="button" class="damga-sec" data-damga="${idx}" aria-pressed="${d.damga === dm}" title="${dm.ad}" style="color:${dm.r}">${dm.s}</button>`
        ).join('');
      } else if (d.arac === 'sec' && d.secili.length) {
        altPanel.hidden = false;
        altPanel.innerHTML =
          `<span class="sec-bilgi">${d.secili.length} öğe seçili</span>` +
          `<button type="button" class="sec-eylem" data-sec-is="cogalt" title="Seçili öğeleri çoğalt (Ctrl+D)">Çoğalt</button>` +
          `<button type="button" class="sec-eylem tehlike" data-sec-is="sil" title="Seçili öğeleri sil (Delete)">Sil</button>`;
      } else {
        altPanel.hidden = true;
        altPanel.innerHTML = '';
      }
    }

    const guncelle = () => {
      cubuk.querySelectorAll('[data-arac]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.arac === d.arac)));
      cubuk.querySelectorAll('[data-renk]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.renk.toLowerCase() === d.renk.toLowerCase())));
      cubuk.querySelectorAll('[data-kalinlik]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.kalinlik === d.kalinlik)));
      cubuk.querySelector('[data-is=dolgu]')?.setAttribute('aria-pressed', String(d.dolu));
      const kayitBtn = cubuk.querySelector('[data-is=kayit]');
      if (kayitBtn) {
        const aktifKayit = kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi';
        kayitBtn.setAttribute('aria-pressed', String(Boolean(kayitKutu) || aktifKayit));
        kayitBtn.classList.toggle('aktif-kayit', aktifKayit);
        if (!aktifKayit) kayitBtn.title = 'Ders anlatımı ekran ve ses kaydı al (.MP4 / YouTube — F9)';
      }
      cubuk.querySelector('[data-is=sayac]')?.setAttribute('aria-pressed', String(Boolean(sayacKutu)));
      cubuk.querySelector('[data-is=perde]')?.setAttribute('aria-pressed', String(Boolean(perdeOge)));
      cubuk.querySelector('[data-is=yardim]')?.setAttribute('aria-pressed', String(Boolean(yardimKutu)));
      ust.style.pointerEvents = d.arac === 'el' ? 'none' : 'auto';
      ust.style.cursor = d.arac === 'silgi' ? 'none' : d.arac === 'cizgisil' ? 'cell' : d.arac === 'metin' ? 'text' : d.arac === 'sec' ? 'move' : 'crosshair';
      const g = cubuk.querySelector('[data-is=geri]'), i = cubuk.querySelector('[data-is=ileri]');
      if (g) g.disabled = !d.gecmis.length;
      if (i) i.disabled = !d.ileri.length;
      if (d.arac === 'odak' && !d.imlec) {
        const k = kay();
        d.imlec = [k.x + gen / 2, k.y + yuk / 2, 1];
      }
      altPanelGuncelle();
      iste();
    };

    ozelRenkGirdi?.addEventListener('input', (o) => {
      d.renk = o.target.value;
      if (d.secili.length) {
        for (const c of d.secili) c.renk = d.renk;
        hepsiniCiz(); bildir();
      } else if (['silgi', 'cizgisil', 'el', 'lazer', 'odak'].includes(d.arac)) {
        d.arac = 'kalem';
      }
      guncelle();
    });

    cubuk.addEventListener('click', (o) => {
      const b = o.target.closest('button'); if (!b) return;
      if (b.dataset.damga !== undefined) {
        d.damga = DAMGALAR[Number(b.dataset.damga)] || DAMGALAR[0];
        guncelle();
        return;
      }
      if (b.dataset.secIs === 'sil') { seciliSil(); return; }
      if (b.dataset.secIs === 'cogalt') { seciliCogalt(); return; }
      if (b.dataset.arac) {
        d.arac = b.dataset.arac;
        if (d.arac !== 'sec') d.secili = [];
      }
      if (b.dataset.renk) {
        d.renk = b.dataset.renk;
        if (ozelRenkGirdi && /^#[0-9a-f]{6}$/i.test(d.renk)) ozelRenkGirdi.value = d.renk;
        if (d.secili.length) {
          for (const c of d.secili) c.renk = d.renk;
          hepsiniCiz(); bildir();
        } else if (['silgi', 'cizgisil', 'el', 'lazer', 'odak'].includes(d.arac)) {
          d.arac = 'kalem';
        }
      }
      if (b.dataset.kalinlik) {
        d.kalinlik = b.dataset.kalinlik;
        if (d.secili.length) {
          for (const c of d.secili) {
            c.g = KALINLIK[d.kalinlik] * (c.arac === 'fosforlu' ? 3.2 : 1);
            if (c.boy) c.boy = Math.round(Math.max(16, KALINLIK[d.kalinlik] * 4.2));
            c.k = null;
          }
          hepsiniCiz(); bildir();
        }
      }
      if (b.dataset.is === 'dolgu') {
        d.dolu = !d.dolu;
        if (d.secili.length) {
          for (const c of d.secili) if (c.sekil) c.dolu = d.dolu;
          hepsiniCiz(); bildir();
        }
      }
      if (b.dataset.is === 'resim') resimGirdi.click();
      if (b.dataset.is === 'kayit') kayitAcKapat();
      if (b.dataset.is === 'sayac') sayacAcKapat();
      if (b.dataset.is === 'perde') perdeAcKapat();
      if (b.dataset.is === 'yardim') yardimAcKapat();
      if (b.dataset.is === 'daralt') {
        const dar = cubuk.classList.toggle('dar');
        b.setAttribute('aria-pressed', String(dar));
      }
      if (b.dataset.is === 'geri') geriAl();
      if (b.dataset.is === 'ileri') yinele();
      if (b.dataset.is === 'indir') {
        pngLogolu().then((adres) => { const link = document.createElement('a'); link.href = adres; link.download = 'derskutusu-not.png'; link.click(); });
      }
      if (b.dataset.is === 'temizle') temizle();
      if (b.dataset.is === 'kapat') {
        if (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') { kaydiBitir(); return; }
        kapat?.();
      }
      guncelle();
    });

    // Panodan soru görseli yapıştırma (Ctrl+V)
    const yapistir = (o) => {
      const modal = document.querySelector('dialog[open]');
      if (!kap.isConnected || kap.closest('[hidden]') || (modal && !modal.contains(kap))) return;
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)) return;
      const dosyalar = o.clipboardData?.files;
      if (!dosyalar || !dosyalar.length) return;
      const gorsel = [...dosyalar].find((f) => f.type.startsWith('image/'));
      if (!gorsel) return;
      o.preventDefault();
      const okuyucu = new FileReader();
      okuyucu.onload = () => { if (typeof okuyucu.result === 'string') gorselVerisiEkle(okuyucu.result); };
      okuyucu.readAsDataURL(gorsel);
    };
    document.addEventListener('paste', yapistir);

    const tus = (o) => {
      // Gizli kalem ve sunumun arkasındaki sayfa kısayollara yanıt vermez.
      const modal = document.querySelector('dialog[open]');
      if (!kap.isConnected || kap.closest('[hidden]') || (modal && !modal.contains(kap))) return;
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)) return;
      const k = o.key.toLowerCase();
      if (o.key === 'F9' || (o.altKey && k === 'k')) { o.preventDefault(); kayitAcKapat(); return; }
      if (k === 'm' && !o.ctrlKey && !o.metaKey && (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi')) {
        o.preventDefault();
        if (typeof cubuk !== 'undefined' && cubuk) cubuk.classList.toggle('kayitta-gizli');
        return;
      }
      if ((o.ctrlKey || o.metaKey) && k === 'z') { o.preventDefault(); o.shiftKey ? yinele() : geriAl(); return; }
      if ((o.ctrlKey || o.metaKey) && k === 'y') { o.preventDefault(); yinele(); return; }
      if ((o.ctrlKey || o.metaKey) && k === 'd' && d.secili.length) { o.preventDefault(); seciliCogalt(); return; }
      if ((o.key === 'Delete' || o.key === 'Backspace') && d.secili.length) { o.preventDefault(); seciliSil(); return; }
      if (o.ctrlKey || o.metaKey || o.altKey) return;
      if (o.key === '?') { yardimAcKapat(); return; }
      const aracHaritasi = {
        k: 'kalem', f: 'fosforlu', n: 'kesikli', l: 'lazer',
        s: 'silgi', 'ç': 'cizgisil', v: 'sec', d: 'cizgi', o: 'ok',
        r: 'dikdortgen', m: 'cember', u: 'ucgen', 'ü': 'ucgen',
        x: 'eksen', t: 'metin', b: 'damga', g: 'odak', e: kaydir ? 'el' : null,
      };
      const arac = aracHaritasi[k];
      if (arac) { d.arac = arac; if (arac !== 'sec') d.secili = []; guncelle(); }
      if (k === 'escape') {
        if (yardimKutu) yardimAcKapat();
        else if (kayitKutu) kayitAcKapat();
        else if (d.secili.length) { d.secili = []; guncelle(); }
        else if (d.arac === 'odak') { d.arac = 'kalem'; guncelle(); }
        else if (kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') { kaydiBitir(); }
        else if (kapat) kapat();
      }
    };
    document.addEventListener('keydown', tus);

    // Kayıt esnasında ekranın altına yaklaşıldığında menüyü geçici gösteren dinleyici
    const altKenarDinleyici = (e) => {
      if ((kayitDurum === 'kayitta' || kayitDurum === 'duraklatildi') && kayittaMenuyuGizle) {
        if (e.clientY >= (window.innerHeight - 34)) {
          kayittaMenuyuGeciciGoster();
        }
      }
    };
    window.addEventListener('pointermove', altKenarDinleyici, { passive: true });
    const olcu = new ResizeObserver(boyutla);
    olcu.observe(kap);
    const kaydirildi = () => { hepsiniCiz(); iste(); };
    const kaydirHedef = kaydir === true ? window : (kaydir || null);   // boş tahtada kaydırma yok
    kaydirHedef?.addEventListener('scroll', kaydirildi, { passive: true });
    // Kalem açıkken fare tekerleği alttaki kabı kaydırır.
    if (kaydir) ust.addEventListener('wheel', (o) => { o.preventDefault(); kaydirBy(o.deltaX, o.deltaY); }, { passive: false });
    boyutla(); guncelle();
    return {
      d, hepsiniCiz, geriAl, yinele, temizle, kayitAcKapat,
      zemin: (z) => {
        d.zemin = z;
        if (z === 'koyu' && d.renk === '#111a2e') d.renk = '#ffffff';
        else if (z !== 'koyu' && d.renk === '#ffffff') d.renk = '#111a2e';
        hepsiniCiz(); guncelle(); bildir();
      },
      yukle: (cizgiler) => { d.cizgiler = cizgiler; d.secili = []; d.gecmis = []; d.ileri = []; hepsiniCiz(); guncelle(); },
      png: () => alt.toDataURL('image/png'),
      pngLogolu,
      // Yakınlaştırmada çizgiler içerikle birlikte ölçeklenir.
      olcekle: (k) => {
        const hepsi = new Set([...d.cizgiler, ...[...d.gecmis, ...d.ileri].flatMap((g) => g.cizgiler || g.ogeler || (g.cizgi ? [g.cizgi] : [...(g.eski || []), ...(g.yeni || [])]))]);
        for (const c of hepsi) {
          c.g *= k; c.k = null;
          if (c.boy) c.boy *= k;
          if (c.bas) { c.bas[0] *= k; c.bas[1] *= k; }
          if (c.son) { c.son[0] *= k; c.son[1] *= k; }
          for (const q of c.n) { q[0] *= k; q[1] *= k; }
        }
        hepsiniCiz();
      },
      kaldir: () => {
        clearInterval(sayacInterval);
        kayitKaynakTemizle();
        if (kayitBlobUrl) { try { URL.revokeObjectURL(kayitBlobUrl); } catch { /* */ } }
        olcu.disconnect();
        window.removeEventListener('pointermove', altKenarDinleyici);
        document.removeEventListener('keydown', tus);
        document.removeEventListener('paste', yapistir);
        kaydirHedef?.removeEventListener('scroll', kaydirildi);
        alt.remove(); ust.remove(); cubuk.remove(); resimGirdi.remove();
        sayacKutu?.remove(); perdeOge?.remove(); yardimKutu?.remove(); kayitKutu?.remove();
      },
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
  // tahta.html: boş tahta, sayfalar (tarayıcıda otomatik kayıtlı), çoğaltma, zemin, PNG indirme, ders kaydı
  const tahtaKap = document.getElementById('tahta');
  if (tahtaKap) {
    const DEPO_ANAHTAR = 'derskutusu-tahta-v1';
    let sayfalar = [[]], no = 0, basZemin = 'kareli';
    try {
      const kayit = JSON.parse(localStorage.getItem(DEPO_ANAHTAR) || 'null');
      if (kayit && Array.isArray(kayit.sayfalar) && kayit.sayfalar.length) {
        sayfalar = kayit.sayfalar;
        no = Math.min(Math.max(0, kayit.no || 0), sayfalar.length - 1);
        if (kayit.zemin !== undefined) basZemin = kayit.zemin;
      }
    } catch { /* gizli pencere veya kota */ }

    const zeminSec = document.getElementById('t-zemin');
    if (zeminSec && basZemin !== undefined) zeminSec.value = basZemin || '';

    const depola = () => {
      try {
        sayfalar[no] = t.d.cizgiler.map(({ img, ...kalan }) => kalan);
        localStorage.setItem(DEPO_ANAHTAR, JSON.stringify({ sayfalar, no, zemin: t.d.zemin }));
      } catch { /* kota aşıldıysa sessiz geç */ }
    };

    const t = Tahta.olustur({ kap: tahtaKap, zemin: basZemin, degisti: depola });
    if (sayfalar[no]?.length) t.yukle(sayfalar[no]);

    const sayfaYaz = () => { document.getElementById('t-sayfa').textContent = `${no + 1} / ${sayfalar.length}`; };
    const git = (yeni) => { sayfalar[no] = t.d.cizgiler; no = yeni; t.yukle(sayfalar[no]); sayfaYaz(); depola(); };
    document.getElementById('t-onceki')?.addEventListener('click', () => no > 0 && git(no - 1));
    document.getElementById('t-sonraki')?.addEventListener('click', () => { if (no === sayfalar.length - 1) sayfalar.push([]); git(no + 1); });
    document.getElementById('t-cogalt')?.addEventListener('click', () => {
      sayfalar[no] = t.d.cizgiler;
      const kopya = JSON.parse(JSON.stringify(t.d.cizgiler.map(({ img, ...kalan }) => kalan)));
      sayfalar.splice(no + 1, 0, kopya);
      git(no + 1);
    });
    document.getElementById('t-sil')?.addEventListener('click', () => {
      if (sayfalar.length <= 1) { t.temizle(); depola(); return; }
      sayfalar.splice(no, 1);
      no = Math.min(no, sayfalar.length - 1);
      t.yukle(sayfalar[no]);
      sayfaYaz();
      depola();
    });
    zeminSec?.addEventListener('change', (o) => t.zemin(o.target.value || null));
    document.getElementById('t-video')?.addEventListener('click', () => t.kayitAcKapat());
    document.getElementById('t-kaydet')?.addEventListener('click', () => {
      t.pngLogolu().then((adres) => { const a = document.createElement('a'); a.href = adres; a.download = `derskutusu-tahta-${no + 1}.png`; a.click(); });
    });
    document.getElementById('t-tam')?.addEventListener('click', () => (document.fullscreenElement ? document.exitFullscreen() : document.getElementById('tahta-alan').requestFullscreen?.()));
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
        ip.textContent = 'İpucu: Çizim sonunda kalemi bekletirseniz otomatik düzgün şekle dönüşür; Ctrl+V ile soru görseli yapıştırabilirsiniz.';
        kap.append(ip); setTimeout(() => ip.remove(), 6500);
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
