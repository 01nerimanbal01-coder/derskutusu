// Etkileşimli etkinlikler, kavram kartları, görsel büyüteç, akıllı tahta sunum kipi, okuma ilerleme çubuğu,
// yerel ilerleme rozetleri ve sesli telaffuz (Arapça / İngilizce).
// İşaretlemeyi ozet_uret.py üretir; bu betik yalnız davranışı ekler. Veriler yalnız tarayıcıda tutulur.
(() => {
  const DEPO_ONEK = 'dk_ozet_';

  function ilerlemeOku(id) {
    if (!id) return null;
    try {
      const ham = localStorage.getItem(DEPO_ONEK + id);
      return ham ? JSON.parse(ham) : null;
    } catch (_) {
      return null;
    }
  }

  function ilerlemeKaydet(id, veri) {
    if (!id) return;
    try {
      localStorage.setItem(DEPO_ONEK + id, JSON.stringify(veri));
    } catch (_) {}
  }

  function haftaRozetleriniGuncelle() {
    document.querySelectorAll('.hafta-hap[data-ozet-id]').forEach((hap) => {
      const kayit = ilerlemeOku(hap.dataset.ozetId);
      const rozet = hap.querySelector('.h-tamam');
      if (kayit && kayit.tamam) {
        hap.classList.add('tamam');
        if (!rozet) {
          const i = document.createElement('i');
          i.className = 'h-tamam';
          i.setAttribute('aria-label', 'Tamamlandı');
          i.title = `Tamamlandı (${kayit.dogru}/${kayit.toplam} doğru)`;
          i.textContent = '✓';
          hap.appendChild(i);
        }
      }
    });
  }

  function etkinlikKur(kok) {
    if (!kok || kok.dataset.etkinlikKuruldu === '1') return;
    kok.dataset.etkinlikKuruldu = '1';
    const ozetId = kok.dataset.ozetId || '';
    const ilkHal = kok.querySelector('.etk-liste').innerHTML;

    function kur() {
      const liste = kok.querySelector('.etk-liste');
      const puanYaz = kok.querySelector('.etk-puan');
      let dogru = 0, cevaplanan = 0;
      const toplam = liste.querySelectorAll('.etk-coktan, .etk-dy-satir, .etk-eslestir [data-sol], .etk-bosluk-yer').length;
      const oncekiKayit = ilerlemeOku(ozetId);

      const guncelle = () => {
        const bittiMi = cevaplanan === toplam && toplam > 0;
        let ek = '';
        if (bittiMi) {
          ek = ' · <span class="etk-tamam-rozet">✓ Tamamlandı</span>';
          ilerlemeKaydet(ozetId, { dogru, cevaplanan, toplam, tamam: true, t: Date.now() });
          haftaRozetleriniGuncelle();
        } else if (cevaplanan === 0 && oncekiKayit && oncekiKayit.tamam) {
          ek = ` · <span class="etk-onceki-rozet" title="Önceki çalışmanızda tamamlandı">✓ Önceki rekor: ${oncekiKayit.dogru}/${oncekiKayit.toplam}</span>`;
        } else if (cevaplanan > 0) {
          ilerlemeKaydet(ozetId, { dogru, cevaplanan, toplam, tamam: false, t: Date.now() });
        }
        puanYaz.innerHTML = `<b>${dogru}</b> / ${toplam} doğru` + ek;
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
          if (y.dataset.kelime) {
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

  // 2. Kavram Kartları (Flashcards)
  function kartlarKur() {
    const bolum = document.getElementById('kartlar');
    if (!bolum || bolum.dataset.kuruldu === '1') return;
    bolum.dataset.kuruldu = '1';

    const veriElemanlari = [...bolum.querySelectorAll('.fkart-veri > li')];
    if (!veriElemanlari.length) return;

    let deste = veriElemanlari.map((li) => ({
      on: li.dataset.on || '',
      arka: li.dataset.arka || '',
      etiket: li.dataset.etiket || 'Kavram'
    }));
    let sira = 0;

    const kartDugme = bolum.querySelector('.fkart');
    const onYuz = bolum.querySelector('.fkart-on');
    const arkaYuz = bolum.querySelector('.fkart-arka');
    const sayac = bolum.querySelector('.fkart-sayac');
    const noktalarKap = bolum.querySelector('.fkart-noktalar');
    const oncekiDugme = bolum.querySelector('.fkart-onceki');
    const sonrakiDugme = bolum.querySelector('.fkart-sonraki');
    const karistirDugme = bolum.querySelector('.fkart-karistir');

    function noktalariOlustur() {
      noktalarKap.innerHTML = '';
      deste.forEach((_, idx) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'fkart-nokta' + (idx === sira ? ' etkin' : '');
        b.setAttribute('aria-label', `${idx + 1}. karta git`);
        b.addEventListener('click', () => { sira = idx; goster(); });
        noktalarKap.appendChild(b);
      });
    }

    function goster() {
      const k = deste[sira];
      kartDugme.classList.remove('cevrik');
      kartDugme.setAttribute('aria-pressed', 'false');
      onYuz.querySelector('.fkart-etiket').textContent = k.etiket;
      onYuz.querySelector('.fkart-metin').innerHTML = k.on;
      arkaYuz.querySelector('.fkart-metin').innerHTML = k.arka;
      sayac.textContent = `${sira + 1} / ${deste.length}`;
      [...noktalarKap.children].forEach((n, idx) => n.classList.toggle('etkin', idx === sira));
      sesliDinleKur(kartDugme);
    }

    kartDugme.addEventListener('click', (ev) => {
      if (ev.target.closest('.ses-dugme, .sesli-ar')) return;
      const cevrik = kartDugme.classList.toggle('cevrik');
      kartDugme.setAttribute('aria-pressed', cevrik ? 'true' : 'false');
    });

    oncekiDugme.addEventListener('click', () => {
      sira = (sira - 1 + deste.length) % deste.length;
      goster();
    });

    sonrakiDugme.addEventListener('click', () => {
      sira = (sira + 1) % deste.length;
      goster();
    });

    if (karistirDugme) {
      karistirDugme.addEventListener('click', () => {
        for (let i = deste.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [deste[i], deste[j]] = [deste[j], deste[i]];
        }
        sira = 0;
        goster();
      });
    }

    bolum.addEventListener('keydown', (ev) => {
      if (ev.key === 'ArrowLeft') { ev.preventDefault(); oncekiDugme.click(); }
      else if (ev.key === 'ArrowRight') { ev.preventDefault(); sonrakiDugme.click(); }
    });

    noktalariOlustur();
    goster();
  }

  // 3. SVG Görsel Büyüteç (Tam Ekran Lightbox)
  function gorselBuyutecKur() {
    const gorseller = document.querySelectorAll('.ozet-gorsel');
    if (!gorseller.length) return;

    let modal = null;
    function kapat() {
      if (!modal) return;
      modal.remove();
      modal = null;
      document.body.classList.remove('buyutec-acik');
    }

    function ac(fig) {
      const svg = fig.querySelector('svg');
      if (!svg) return;
      kapat();

      const bolum = fig.closest('.ozet-bolum');
      const baslik = bolum && bolum.querySelector('h2') ? bolum.querySelector('h2').textContent.trim() : (svg.getAttribute('aria-label') || 'Görsel');

      modal = document.createElement('div');
      modal.className = 'ozet-buyutec';
      modal.setAttribute('role', 'dialog');
      modal.setAttribute('aria-modal', 'true');
      modal.setAttribute('aria-label', baslik);

      const renkSinifi = [...(document.querySelector('main.ozet')?.classList || [])].find((c) => c.startsWith('ders-')) || '';
      if (renkSinifi) modal.classList.add(renkSinifi);

      modal.innerHTML = `
        <div class="buyutec-ic">
          <div class="buyutec-ust">
            <strong></strong>
            <div class="buyutec-dugmeler">
              <button type="button" class="dugme buyutec-kalem">✎ Kalemle Üzerine Çiz</button>
              <button type="button" class="dugme ana buyutec-kapat" aria-label="Kapat">✕ Kapat</button>
            </div>
          </div>
          <div class="buyutec-sahne ozet-gorsel"></div>
        </div>
      `;
      modal.querySelector('strong').textContent = baslik;
      const kopyaSvg = svg.cloneNode(true);
      modal.querySelector('.buyutec-sahne').appendChild(kopyaSvg);

      modal.querySelector('.buyutec-kapat').addEventListener('click', kapat);
      modal.querySelector('.buyutec-kalem').addEventListener('click', () => {
        if (typeof window.kalemAc === 'function') window.kalemAc();
      });
      modal.addEventListener('click', (ev) => {
        if (ev.target === modal) kapat();
      });

      document.body.appendChild(modal);
      document.body.classList.add('buyutec-acik');
      modal.querySelector('.buyutec-kapat').focus();
    }

    gorseller.forEach((fig) => {
      if (fig.dataset.buyutecKuruldu === '1') return;
      fig.dataset.buyutecKuruldu = '1';
      fig.addEventListener('click', () => ac(fig));
      fig.addEventListener('keydown', (ev) => {
        if (ev.key === 'Enter' || ev.key === ' ') {
          ev.preventDefault();
          ac(fig);
        }
      });
    });

    window.addEventListener('keydown', (ev) => {
      if (ev.key === 'Escape' && modal) kapat();
    });
  }

  // 4. Akıllı Tahta Sunum Modu
  let sunumDurum = null;
  function ozetSunumAc() {
    if (sunumDurum) {
      sunumDurum.kapat();
      return;
    }
    const ana = document.querySelector('main.ozet');
    if (!ana) return;
    const slaytlar = [
      ana.querySelector('.ozet-ust'),
      ...ana.querySelectorAll('.ozet-bolum.konu'),
      ana.querySelector('#kartlar'),
      ana.querySelector('#ornekler'),
      ana.querySelector('#etkinlikler'),
      ana.querySelector('#kisaca')
    ].filter(Boolean);
    if (!slaytlar.length) return;

    let indeks = 0;
    document.body.classList.add('sunum-modu');

    const cubuk = document.createElement('div');
    cubuk.className = 'sunum-cubuk';
    cubuk.setAttribute('role', 'region');
    cubuk.setAttribute('aria-label', 'Sunum denetimleri');
    cubuk.innerHTML = `
      <button type="button" class="sunum-dugme s-onceki" aria-label="Önceki slayt">← Önceki</button>
      <span class="sunum-sayac" aria-live="polite"></span>
      <button type="button" class="sunum-dugme s-sonraki" aria-label="Sonraki slayt">Sonraki →</button>
      <button type="button" class="sunum-dugme s-yazi" title="Yazı boyutunu büyüt/küçült">A+</button>
      <button type="button" class="sunum-dugme s-kalem">✎ Kalem</button>
      <button type="button" class="sunum-dugme s-kapat">✕ Çıkış</button>
    `;
    document.body.appendChild(cubuk);

    function guncelle() {
      slaytlar.forEach((s, i) => s.classList.toggle('sunum-aktif', i === indeks));
      const aktif = slaytlar[indeks];
      const h2 = aktif.querySelector('h2');
      const ad = h2 ? h2.textContent.trim() : 'Giriş ve Öğrenme Çıktıları';
      cubuk.querySelector('.sunum-sayac').textContent = `Slayt ${indeks + 1} / ${slaytlar.length} · ${ad}`;
      cubuk.querySelector('.s-onceki').disabled = indeks === 0;
      cubuk.querySelector('.s-sonraki').disabled = indeks === slaytlar.length - 1;
      aktif.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    function klavye(ev) {
      if (!sunumDurum) return;
      if (ev.target && ['INPUT', 'TEXTAREA', 'SELECT'].includes(ev.target.tagName)) return;
      if (ev.key === 'ArrowRight' || ev.key === 'PageDown') {
        if (indeks < slaytlar.length - 1) { ev.preventDefault(); indeks++; guncelle(); }
      } else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') {
        if (indeks > 0) { ev.preventDefault(); indeks--; guncelle(); }
      } else if (ev.key === 'Escape') {
        kapat();
      }
    }

    function kapat() {
      document.body.classList.remove('sunum-modu', 'sunum-iri');
      slaytlar.forEach((s) => s.classList.remove('sunum-aktif'));
      cubuk.remove();
      window.removeEventListener('keydown', klavye);
      sunumDurum = null;
    }

    cubuk.querySelector('.s-onceki').addEventListener('click', () => { if (indeks > 0) { indeks--; guncelle(); } });
    cubuk.querySelector('.s-sonraki').addEventListener('click', () => { if (indeks < slaytlar.length - 1) { indeks++; guncelle(); } });
    cubuk.querySelector('.s-yazi').addEventListener('click', (ev) => {
      const iri = document.body.classList.toggle('sunum-iri');
      ev.currentTarget.classList.toggle('etkin', iri);
    });
    cubuk.querySelector('.s-kalem').addEventListener('click', () => {
      if (typeof window.kalemAc === 'function') window.kalemAc();
    });
    cubuk.querySelector('.s-kapat').addEventListener('click', kapat);
    window.addEventListener('keydown', klavye);

    sunumDurum = { kapat };
    guncelle();
  }

  // 5. Yazdır / PDF Çalışma Yaprağı
  function ozetYazdir() {
    document.querySelectorAll('.ornek details').forEach((d) => { d.open = true; });
    window.print();
  }
  window.addEventListener('beforeprint', () => {
    document.querySelectorAll('.ornek details').forEach((d) => { d.open = true; });
  });

  // 6. Okuma İlerleme Çubuğu ve Sabit "Bu Sayfada" Vurgusu
  function okumaVeIcindekilerKur() {
    const cubuk = document.getElementById('okuma-ilerleme');
    const ana = document.querySelector('main.ozet');
    if (cubuk && ana) {
      let bekliyor = false;
      const kaydirGuncelle = () => {
        bekliyor = false;
        const r = ana.getBoundingClientRect();
        const toplam = Math.max(1, ana.offsetHeight - window.innerHeight * 0.6);
        const gecen = Math.min(toplam, Math.max(0, -r.top + window.innerHeight * 0.25));
        cubuk.style.width = Math.round((gecen / toplam) * 100) + '%';
      };
      window.addEventListener('scroll', () => {
        if (!bekliyor) { bekliyor = true; requestAnimationFrame(kaydirGuncelle); }
      }, { passive: true });
      kaydirGuncelle();
    }

    const bolumler = [...document.querySelectorAll('main.ozet section[id]')];
    const baglar = [...document.querySelectorAll('.ozet-ic-cubuk .ic-bag, .ozet-yan li a')];
    if (!bolumler.length || !baglar.length || !('IntersectionObserver' in window)) return;

    const etkinYap = (id) => {
      baglar.forEach((a) => {
        const eslesti = a.getAttribute('href') === '#' + id;
        a.classList.toggle('etkin', eslesti);
      });
    };

    const gozlemci = new IntersectionObserver((girdiler) => {
      for (const g of girdiler) {
        if (g.isIntersecting) {
          etkinYap(g.target.id);
          break;
        }
      }
    }, { rootMargin: '-18% 0px -68% 0px', threshold: 0 });

    bolumler.forEach((b) => gozlemci.observe(b));
  }

  // 7. Sesli Telaffuz (Arapça <bdi lang="ar"> ve İngilizce ders içerikleri)
  function sesliOku(metin, dil) {
    if (!('speechSynthesis' in window) || !metin) return;
    try {
      window.speechSynthesis.cancel();
      const soz = new SpeechSynthesisUtterance(metin.trim());
      soz.lang = dil;
      soz.rate = dil.startsWith('ar') ? 0.88 : 0.94;
      const sesler = window.speechSynthesis.getVoices();
      const uygun = sesler.find((s) => s.lang && s.lang.toLowerCase().startsWith(dil.slice(0, 2).toLowerCase()));
      if (uygun) soz.voice = uygun;
      window.speechSynthesis.speak(soz);
    } catch (_) {}
  }

  function sesliDinleKur(kapsayici = document) {
    if (!('speechSynthesis' in window)) return;

    // Arapça metinler (<bdi lang="ar">)
    kapsayici.querySelectorAll('bdi[lang="ar"]').forEach((bdi) => {
      if (bdi.dataset.sesKuruldu === '1') return;
      bdi.dataset.sesKuruldu = '1';
      bdi.classList.add('sesli-ar');
      bdi.title = 'Sesli dinlemek için dokunun';
      bdi.setAttribute('role', 'button');
      bdi.setAttribute('tabindex', '0');
      const oku = (ev) => {
        ev.stopPropagation();
        sesliOku(bdi.textContent, 'ar-SA');
        bdi.classList.add('okunuyor');
        setTimeout(() => bdi.classList.remove('okunuyor'), 1200);
      };
      bdi.addEventListener('click', oku);
      bdi.addEventListener('keydown', (ev) => {
        if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); oku(ev); }
      });
    });

    // İngilizce ders özetlerinde kalın/italik İngilizce ifadeler için ses düğmesi
    const ingilizceSayfa = document.querySelector('main.ozet.ders-ingilizce');
    if (ingilizceSayfa) {
      kapsayici.querySelectorAll('.ozet-bolum.konu li b, .ozet-bolum.konu p b, .fkart-on .fkart-metin').forEach((el) => {
        if (el.dataset.sesKuruldu === '1') return;
        const m = (el.textContent || '').trim();
        if (m.length < 2 || m.length > 95 || /[çğıöşüÇĞİÖŞÜ]/.test(m) || !/[a-zA-Z]/.test(m)) return;
        el.dataset.sesKuruldu = '1';
        el.classList.add('sesli-en');
        el.title = 'İngilizce telaffuzu dinlemek için dokunun';
        el.addEventListener('click', (ev) => {
          ev.stopPropagation();
          sesliOku(m, 'en-US');
          el.classList.add('okunuyor');
          setTimeout(() => el.classList.remove('okunuyor'), 1100);
        });
      });
    }
  }

  window.etkinlikKur = etkinlikKur;
  window.ozetSunumAc = ozetSunumAc;
  window.ozetYazdir = ozetYazdir;

  haftaRozetleriniGuncelle();
  etkinlikKur(document.getElementById('etkinlikler'));
  kartlarKur();
  gorselBuyutecKur();
  okumaVeIcindekilerKur();
  sesliDinleKur();
})();
