// Etkileşimli etkinlikler: çoktan seçmeli, doğru-yanlış, eşleştirme, boşluk doldurma, öğretici soru.
// İşaretlemeyi ozet_uret.py üretir; bu betik yalnız davranışı ekler. Puan yalnız bu sayfada tutulur, hiçbir yere gönderilmez.
(() => {
  function etkinlikKur(kok) {
  if (!kok || kok.dataset.etkinlikKuruldu === '1') return;
  kok.dataset.etkinlikKuruldu = '1';
  const ilkHal = kok.querySelector('.etk-liste').innerHTML;

  function kur() {
    const liste = kok.querySelector('.etk-liste');
    const puanYaz = kok.querySelector('.etk-puan');
    let dogru = 0, cevaplanan = 0;
    const toplam = liste.querySelectorAll('.etk-coktan, .etk-dy-satir, .etk-eslestir [data-sol], .etk-bosluk-yer').length;
    const guncelle = () => {
      puanYaz.innerHTML = `<b>${dogru}</b> / ${toplam} doğru` + (cevaplanan === toplam ? ' · <span>Tamamlandı</span>' : '');
    };
    const sonuc = (ok) => { cevaplanan++; if (ok) dogru++; guncelle(); };
    const geriBildirim = (yer, ok, metin) => {
      yer.hidden = false;
      yer.className = 'etk-geri ' + (ok ? 'dogru' : 'yanlis');
      yer.firstElementChild.textContent = ok ? 'Doğru!' : 'Yanlış.';
      if (metin != null) yer.lastElementChild.textContent = metin;
    };

    // Çoktan seçmeli
    liste.querySelectorAll('.etk-coktan').forEach((s) => {
      const dogruNo = s.dataset.dogru;
      s.querySelectorAll('.etk-sec').forEach((b) => b.addEventListener('click', () => {
        if (s.classList.contains('bitti')) return;
        s.classList.add('bitti');
        const ok = b.dataset.i === dogruNo;
        b.classList.add(ok ? 'dogru' : 'yanlis');
        s.querySelector(`.etk-sec[data-i="${dogruNo}"]`).classList.add('dogru');
        s.querySelectorAll('.etk-sec').forEach((x) => { x.setAttribute('aria-disabled', 'true'); });
        geriBildirim(s.querySelector('.etk-geri'), ok);
        sonuc(ok);
      }));
    });

    // Doğru-yanlış
    liste.querySelectorAll('.etk-dy-satir').forEach((r) => {
      r.querySelectorAll('button').forEach((b) => b.addEventListener('click', () => {
        if (r.classList.contains('bitti')) return;
        r.classList.add('bitti');
        const ok = b.dataset.c === r.dataset.dogru;
        b.classList.add(ok ? 'dogru' : 'yanlis');
        if (!ok) r.querySelector(`button[data-c="${r.dataset.dogru}"]`).classList.add('dogru');
        geriBildirim(r.querySelector('.etk-geri'), ok);
        sonuc(ok);
      }));
    });

    // Eşleştirme: bir sol, bir sağ öğeye dokun; doğru eşler aynı renge boyanır.
    liste.querySelectorAll('.etk-eslestir').forEach((e) => {
      let secili = null, renk = 0;
      const hata = new Set();
      e.querySelectorAll('[data-sol], [data-sag]').forEach((b) => b.addEventListener('click', () => {
        if (b.classList.contains('esli')) return;
        if (!secili || secili === b || ('sol' in secili.dataset) === ('sol' in b.dataset)) {
          if (secili) secili.classList.remove('secili');
          secili = secili === b ? null : b;
          if (secili) secili.classList.add('secili');
          return;
        }
        const sol = 'sol' in b.dataset ? b : secili, sag = sol === b ? secili : b;
        secili.classList.remove('secili'); secili = null;
        if (sol.dataset.sol === sag.dataset.sag) {
          renk = (renk % 5) + 1;
          for (const x of [sol, sag]) { x.classList.add('esli', 'r' + renk); x.setAttribute('aria-disabled', 'true'); }
          sonuc(!hata.has(sol.dataset.sol));
          if (!e.querySelector('[data-sol]:not(.esli)')) geriBildirim(e.querySelector('.etk-geri'), true, 'Bütün eşler bulundu.');
        } else {
          hata.add(sol.dataset.sol);
          for (const x of [sol, sag]) { x.classList.add('titre'); setTimeout(() => x.classList.remove('titre'), 450); }
        }
      }));
    });

    // Boşluk doldurma: kelimeye dokun → seçili (ya da ilk boş) yere yerleşir; dolu yere dokun → kelime geri döner.
    liste.querySelectorAll('.etk-bosluk').forEach((k) => {
      let hedef = null;
      const yerler = [...k.querySelectorAll('.etk-bosluk-yer')];
      const sec = (y) => { yerler.forEach((x) => x.classList.toggle('secili', x === y)); hedef = y; };
      yerler.forEach((y) => y.addEventListener('click', () => {
        if (k.classList.contains('bitti')) return;
        if (y.dataset.kelime) {                      // dolu yeri boşalt
          k.querySelector(`.etk-kelime[data-k="${y.dataset.kelimeNo}"]`).hidden = false;
          y.textContent = ''; delete y.dataset.kelime; delete y.dataset.kelimeNo;
        }
        sec(y);
      }));
      k.querySelectorAll('.etk-kelime').forEach((w) => w.addEventListener('click', () => {
        if (k.classList.contains('bitti')) return;
        const y = hedef && !hedef.dataset.kelime ? hedef : yerler.find((x) => !x.dataset.kelime);
        if (!y) return;
        y.textContent = w.textContent; y.dataset.kelime = w.textContent; y.dataset.kelimeNo = w.dataset.k; w.hidden = true;
        sec(yerler.find((x) => !x.dataset.kelime) || null);
      }));
      k.querySelector('.etk-kontrol').addEventListener('click', () => {
        if (k.classList.contains('bitti')) return;
        if (yerler.some((y) => !y.dataset.kelime)) { k.querySelector('.etk-uyari').hidden = false; return; }
        k.classList.add('bitti'); k.querySelector('.etk-uyari').hidden = true; sec(null);
        let hepsi = true;
        yerler.forEach((y) => {
          const ok = y.dataset.kelime === y.dataset.cevap;
          y.classList.add(ok ? 'dogru' : 'yanlis');
          if (!ok) { hepsi = false; y.title = 'Doğrusu: ' + y.dataset.cevap; y.insertAdjacentHTML('afterend', `<small class="etk-duzelt">${y.dataset.cevap}</small>`); }
          sonuc(ok);
        });
        geriBildirim(k.querySelector('.etk-geri'), hepsi, hepsi ? 'Bütün boşluklar doğru.' : 'Kırmızı boşlukların doğrusu yanlarında yazıyor.');
      });
    });

    // Öğretici soru: ipuçları sırayla açılır, en sonda cevap
    liste.querySelectorAll('.etk-ogretici').forEach((o) => {
      const ipuclari = [...o.querySelectorAll('.etk-ipucu')];
      const dugme = o.querySelector('.etk-ipucu-dugme');
      const cevap = o.querySelector('.etk-cevap');
      let n = 0;
      dugme.addEventListener('click', () => {
        if (n < ipuclari.length) { ipuclari[n].hidden = false; n++; }
        else { cevap.hidden = false; dugme.hidden = true; return; }
        dugme.textContent = n < ipuclari.length ? `${n + 1}. ipucunu göster` : 'Cevabı göster';
      });
    });
    guncelle();
  }

  kok.querySelector('.etk-sifirla').addEventListener('click', () => { kok.querySelector('.etk-liste').innerHTML = ilkHal; kur(); });
  kur();
  }
  window.etkinlikKur = etkinlikKur;
  etkinlikKur(document.getElementById('etkinlikler'));
})();
