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

  function ozetKapsayiciBul() {
    return document.querySelector('article.ozet, main.ozet, .ozet');
  }

  function etkinlikKur(kok) {
    if (!kok || kok.dataset.etkinlikKuruldu === '1') return;
    kok.dataset.etkinlikKuruldu = '1';
    const ozetId = (
      kok.dataset.ozetId ||
      kok.closest('[data-ozet-kimlik]')?.dataset.ozetKimlik ||
      document.querySelector('[data-ozet-kimlik]')?.dataset.ozetKimlik ||
      ''
    );
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
            const eski = k.querySelector(`.etk-kelime[data-k="${y.dataset.kelimeNo}"]`);
            if (eski) eski.hidden = false;
            y.innerHTML = ''; delete y.dataset.kelime; delete y.dataset.kelimeNo;
          }
          sec(y);
        }));
        k.querySelectorAll('.etk-kelime').forEach((w) => w.addEventListener('click', () => {
          if (k.classList.contains('bitti')) return;
          const y = hedef && !hedef.dataset.kelime ? hedef : yerler.find((x) => !x.dataset.kelime);
          if (!y) return;
          y.innerHTML = w.innerHTML;
          y.dataset.kelime = w.dataset.deger || w.textContent;
          y.dataset.kelimeNo = w.dataset.k;
          w.hidden = true;
          sec(yerler.find((x) => !x.dataset.kelime) || null);
        }));
        k.querySelector('.etk-kontrol').addEventListener('click', () => {
          if (k.classList.contains('bitti')) return;
          if (yerler.some((y) => !y.dataset.kelime)) { k.querySelector('.etk-uyari').hidden = false; return; }
          k.classList.add('bitti'); k.querySelector('.etk-uyari').hidden = true; sec(null);
          let hepsi = true;
          yerler.forEach((y) => {
            const ok = y.dataset.kelime === y.dataset.cevap || y.textContent.trim() === y.dataset.cevap;
            y.classList.add(ok ? 'dogru' : 'yanlis');
            if (!ok) {
              hepsi = false;
              const dogruHtml = y.dataset.cevapHtml || y.dataset.cevap;
              const gecici = document.createElement('span');
              gecici.innerHTML = dogruHtml;
              y.title = 'Doğrusu: ' + (gecici.textContent || y.dataset.cevap);
              y.insertAdjacentHTML('afterend', `<small class="etk-duzelt">${dogruHtml}</small>`);
            }
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

    kok.querySelector('.etk-sifirla').addEventListener('click', () => { kok.querySelector('.etk-liste').innerHTML = ilkHal; kur(); sesliDinleKur(kok); });
    kur();
  }

  // HTML entity çözücü (&#x27;, &amp; vb. sembolleri temizler)
  function htmlCoz(str) {
    if (!str) return '';
    const d = document.createElement('textarea');
    d.innerHTML = String(str);
    return d.value;
  }

  // İngilizce metin mi kontrolü (Türkçe etiketleri, soru kalıplarını ve formülleri dışlar)
  const TR_ETIKET_RE = /\b(ipucu|cevap|örnek|ornek|dikkat|kural|not|özet|ozet|soru|çözüm|cozum|adım|adim|yapı|yapi|olumlu|olumsuz|tekil|çoğul|cogul|özne|ozne|yüklem|yuklem|nesne|zaman|fiil|isim|sıfat|sifat|zarf|bağlaç|baglac|edat|zamir|kullanılır|kullanilir|anlamı|anlami|eklenir|gelir|olur|cümle|cumle|hal|hâl|kipi|şahıs|sahis|mi|mı|mu|mü|misiniz|mısınız|nedir|hangisidir|kabul|ret|gerekçe|gerekce|davet|özür|ozur|arkadaş|arkadas|açıklama|aciklama|düzeltiniz|duzeltiniz|yazınız|yaziniz|ilişkilendirilebilir|iliskilendirilebilir|belirtiniz|seçiniz|seciniz|hangisi)\b/i;
  function ingilizceOkunabilirMi(metin) {
    if (!metin) return false;
    const temiz = htmlCoz(String(metin)).replace(/<[^>]+>/g, ' ').replace(/[🔊📢🔈🔉]/g, '').trim();
    if (temiz.length < 2 || temiz.length > 95) return false;
    if (/[çğıöşüÇĞİÖŞÜ\u0600-\u06FF]/.test(temiz)) return false;
    if (!/[a-zA-Z]{2,}/.test(temiz)) return false;
    if (/\bV[123₁₂₃]\b|[+→=…]/.test(temiz)) return false;
    if (TR_ETIKET_RE.test(temiz)) return false;
    return true;
  }

  // 2. Kavram Kartları (Flashcards)
  function kartlarKur() {
    const bolum = document.getElementById('kartlar');
    if (!bolum || bolum.dataset.kuruldu === '1') return;
    bolum.dataset.kuruldu = '1';

    const veriElemanlari = [...bolum.querySelectorAll('.fkart-veri > .fkart-oge, .fkart-veri > li')];
    if (!veriElemanlari.length) return;

    let deste = veriElemanlari.map((el) => ({
      on: el.dataset.on || '',
      arka: el.dataset.arka || '',
      etiket: el.dataset.etiket || 'Kavram / Soru · Çevirmek için dokunun ↻'
    }));
    let sira = 0;

    const kartDugme = bolum.querySelector('.fkart');
    const onYuz = bolum.querySelector('.fkart-on');
    const arkaYuz = bolum.querySelector('.fkart-arka');
    const onMetin = onYuz ? onYuz.querySelector('.fkart-metin') : null;
    const arkaMetin = arkaYuz ? arkaYuz.querySelector('.fkart-metin') : null;
    const sayac = bolum.querySelector('.fkart-sayac');
    const noktalarKap = bolum.querySelector('.fkart-noktalar');
    const oncekiDugme = bolum.querySelector('.fkart-onceki');
    const sonrakiDugme = bolum.querySelector('.fkart-sonraki');
    const karistirDugme = bolum.querySelector('.fkart-karistir');
    let sesDugme = bolum.querySelector('.fkart-ses');
    if (!sesDugme) {
      const araclar = bolum.querySelector('.fkart-araclar');
      if (araclar) {
        sesDugme = document.createElement('button');
        sesDugme.type = 'button';
        sesDugme.className = 'dugme fkart-ses';
        sesDugme.hidden = true;
        sesDugme.textContent = '🔊 Dinle';
        araclar.prepend(sesDugme);
      }
    }

    const isIngilizceSayfa = !!document.querySelector('.ozet.ders-ingilizce, .ozet-bas.ders-ingilizce') || location.pathname.includes('ingilizce');
    const isArapcaSayfa = !!document.querySelector('.ozet.ders-arapca, .ozet-bas.ders-arapca, .ozet.ders-mesleki-arapca, .ozet-bas.ders-mesleki-arapca') || location.pathname.includes('arapca');

    function aktifKartSesBilgisi() {
      const k = deste[sira];
      if (!k) return null;
      const onTemiz = htmlCoz(String(k.on || '')).replace(/<[^>]+>/g, ' ').replace(/[🔊📢🔈🔉]/g, '').trim();
      const arkaTemiz = htmlCoz(String(k.arka || '')).replace(/<[^>]+>/g, ' ').replace(/[🔊📢🔈🔉]/g, '').trim();

      // Arapça kontrolü
      for (const t of [onTemiz, arkaTemiz]) {
        const arParcalar = t.match(/[\u0600-\u06FF\u064B-\u065F\u0670\u0640]+(?:\s+[\u0600-\u06FF\u064B-\u065F\u0670\u0640]+)*/g);
        if (arParcalar && arParcalar.length) {
          return { metin: arParcalar.join(' '), dil: 'ar-SA' };
        }
      }

      // İngilizce kontrolü: öncelik ön yüzdeki İngilizce kelimede
      if (ingilizceOkunabilirMi(onTemiz)) {
        const safEn = onTemiz.replace(/\([^)]*\)/g, '').replace(/&/g, ' and ').replace(/\s+/g, ' ').trim();
        return { metin: safEn, dil: 'en-US' };
      }
      if (ingilizceOkunabilirMi(arkaTemiz)) {
        const safEn = arkaTemiz.replace(/\([^)]*\)/g, '').replace(/&/g, ' and ').replace(/\s+/g, ' ').trim();
        return { metin: safEn, dil: 'en-US' };
      }
      return null;
    }

    function kartSesDurumunuGuncelle() {
      const bilgi = aktifKartSesBilgisi();
      if (sesDugme) {
        sesDugme.hidden = !bilgi;
        if (bilgi) {
          sesDugme.textContent = '🔊 Dinle';
          sesDugme.title = bilgi.dil === 'ar-SA' ? 'Arapça telaffuzu dinle' : 'İngilizce telaffuzu dinle';
        }
      }
      if (onMetin) {
        if (bilgi && ingilizceOkunabilirMi(k.on)) {
          onMetin.classList.add('sesli-en', 'sesli-kart');
          onMetin.title = 'İngilizce telaffuzu dinlemek için dokunun';
        } else if (bilgi && /[\u0600-\u06FF]/.test(k.on)) {
          onMetin.classList.add('sesli-ar', 'sesli-kart');
          onMetin.title = 'Arapça telaffuzu dinlemek için dokunun';
        } else {
          onMetin.classList.remove('sesli-en', 'sesli-ar', 'sesli-kart');
          onMetin.removeAttribute('title');
        }
      }
    }

    const kartiSeslendir = (e) => {
      e?.stopPropagation();
      e?.preventDefault();
      const bilgi = aktifKartSesBilgisi();
      if (!bilgi) return;
      sesliOku(bilgi.metin, bilgi.dil);
      if (sesDugme) {
        sesDugme.classList.add('okunuyor');
        setTimeout(() => sesDugme.classList.remove('okunuyor'), 1100);
      }
      if (onMetin) {
        onMetin.classList.add('okunuyor');
        setTimeout(() => onMetin.classList.remove('okunuyor'), 1100);
      }
    };

    if (sesDugme) sesDugme.addEventListener('click', kartiSeslendir);

    if (onMetin) {
      onMetin.addEventListener('click', (ev) => {
        if (!onMetin.classList.contains('sesli-kart') && !onMetin.classList.contains('sesli-en') && !onMetin.classList.contains('sesli-ar')) return;
        kartiSeslendir(ev);
      });
      onMetin.addEventListener('keydown', (ev) => {
        if ((ev.key === 'Enter' || ev.key === ' ') && (onMetin.classList.contains('sesli-en') || onMetin.classList.contains('sesli-ar') || onMetin.classList.contains('sesli-kart'))) {
          ev.preventDefault();
          kartiSeslendir(ev);
        }
      });
    }

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
      if (onMetin) onMetin.innerHTML = k.on;
      if (arkaMetin) arkaMetin.innerHTML = k.arka;
      sayac.innerHTML = `<b>${sira + 1}</b> / ${deste.length}`;
      [...noktalarKap.children].forEach((n, idx) => n.classList.toggle('etkin', idx === sira));
      kartSesDurumunuGuncelle();
    }

    kartDugme.addEventListener('click', (ev) => {
      if (ev.target.closest('.ses-dugme, .sesli-ar, .sesli-en, .fkart-ses, .sesli-kart')) return;
      const cevrik = kartDugme.classList.toggle('cevrik');
      kartDugme.setAttribute('aria-pressed', cevrik ? 'true' : 'false');
      kartSesDurumunuGuncelle();
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

      const ana = ozetKapsayiciBul();
      const renkSinifi = [...(ana?.classList || [])].find((c) => c.startsWith('ders-')) || '';
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
    const ana = ozetKapsayiciBul();
    if (!ana) return;
    const slaytlar = [
      ana.querySelector('.ozet-ust'),
      ...ana.querySelectorAll('.ozet-bolum.konu'),
      ana.querySelector('#ornekler'),
      ana.querySelector('#kartlar'),
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
      slaytlar.forEach((s, i) => {
        s.classList.toggle('sunum-aktif', i === indeks);
        s.classList.toggle('sunum-gizli', i !== indeks);
      });
      const aktif = slaytlar[indeks];
      const h2 = aktif.querySelector('h2');
      const ad = h2 ? h2.textContent.trim() : 'Giriş ve Öğrenme Çıktıları';
      cubuk.querySelector('.sunum-sayac').textContent = `Slayt ${indeks + 1} / ${slaytlar.length} · ${ad}`;
      cubuk.querySelector('.s-onceki').disabled = indeks === 0;
      cubuk.querySelector('.s-sonraki').disabled = indeks === slaytlar.length - 1;
      aktif.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
      slaytlar.forEach((s) => s.classList.remove('sunum-aktif', 'sunum-gizli'));
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
    const ana = ozetKapsayiciBul();
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

    const bolumler = [...document.querySelectorAll('article.ozet section[id], main.ozet section[id], .ozet section[id]')];
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
  function sesliOku(metin, dil = 'en-US') {
    if (!('speechSynthesis' in window) || !metin) return;
    try {
      let temiz = String(metin)
        .replace(/<[^>]+>/g, ' ')
        .replace(/[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '')
        .replace(/[🔊📢🔈🔉↻↺]/g, '')
        .replace(/\s+/g, ' ')
        .trim();
      if (dil.startsWith('ar')) {
        const arParcalar = temiz.match(/[\u0600-\u06FF\u064B-\u065F\u0670\u0640]+/g);
        if (arParcalar && arParcalar.length) temiz = arParcalar.join(' ');
      } else if (dil.startsWith('en')) {
        temiz = temiz.replace(/\([^)]*[çğıöşüÇĞİÖŞÜ][^)]*\)/g, ' ').replace(/\s+/g, ' ').trim();
      }
      if (!temiz) return;

      window.speechSynthesis.cancel();
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
      }

      const soz = new SpeechSynthesisUtterance(temiz);
      soz.lang = dil;
      soz.rate = dil.startsWith('ar') ? 0.85 : 0.92;

      const sesler = window.speechSynthesis.getVoices() || [];
      if (sesler.length) {
        const hedef = dil.toLowerCase();
        const kok = hedef.slice(0, 2);
        const tam = sesler.find((s) => s.lang && s.lang.toLowerCase() === hedef);
        const uygun = tam || sesler.find((s) => s.lang && s.lang.toLowerCase().startsWith(kok));
        if (uygun) soz.voice = uygun;
      }

      setTimeout(() => {
        try {
          if (window.speechSynthesis.paused) window.speechSynthesis.resume();
          window.speechSynthesis.speak(soz);
        } catch (_) {}
      }, 25);
    } catch (_) {}
  }

  if ('speechSynthesis' in window) {
    try {
      window.speechSynthesis.getVoices();
      window.speechSynthesis.onvoiceschanged = () => {
        try { window.speechSynthesis.getVoices(); } catch (_) {}
      };
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
        const metin = (bdi.textContent || '').replace(/[🔊📢🔈🔉]/g, '').trim();
        if (metin) sesliOku(metin, 'ar-SA');
        bdi.classList.add('okunuyor');
        setTimeout(() => bdi.classList.remove('okunuyor'), 1200);
      };
      bdi.addEventListener('click', oku);
      bdi.addEventListener('keydown', (ev) => {
        if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); oku(ev); }
      });
    });

    // İngilizce ders özetlerinde kalın İngilizce ifadeler ve tablo terimleri için ses düğmesi
    const ingilizceSayfa = document.querySelector('.ozet.ders-ingilizce, .ozet-bas.ders-ingilizce') || location.pathname.includes('ingilizce');
    if (ingilizceSayfa) {
      kapsayici.querySelectorAll('.ozet-bolum.konu li b, .ozet-bolum.konu p b, .ozet-bolum.konu .ozet-tablo tbody td:first-child').forEach((el) => {
        if (el.dataset.sesKuruldu === '1') return;
        const testMetin = (el.textContent || '').trim();
        if (!ingilizceOkunabilirMi(testMetin)) return;
        el.dataset.sesKuruldu = '1';
        el.classList.add('sesli-en');
        el.title = 'İngilizce telaffuzu dinlemek için dokunun';
        el.addEventListener('click', (ev) => {
          ev.stopPropagation();
          const anlik = (el.textContent || '').replace(/[🔊📢🔈🔉]/g, '').trim();
          if (anlik) sesliOku(anlik, 'en-US');
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
