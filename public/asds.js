// Akademik Süreç Değerlendirme Sınavları (ASDS) — 5, 6, 7 ve 8. Sınıf Haftalık Deneme Sınavları
// Her bir sınıf için ayrı başlık altında Cevapsız A ve B kitapçıkları ile Cevaplı A ve B kitapçıkları ve Cevap Anahtarı.
(() => {
  'use strict';
  const kapsayici = document.getElementById('asds-bolum');
  if (!kapsayici) return;

  const normal = (s) => String(s || '').toLocaleLowerCase('tr').replace(/[^a-zçğıöşü0-9]+/g, ' ').trim();
  const P = new URLSearchParams(location.search);

  veri('asds.json').then((asds) => {
    if (!asds?.siniflar?.length) return;
    const sinifBloklari = asds.siniflar;
    const tumSiniflar = sinifBloklari.map((b) => Number(b.sinif));

    let secSinif = 0; // 0 = Tüm sınıflar ayrı başlıklar altında
    const urlSinif = Number(P.get('sinif'));
    if (tumSiniflar.includes(urlSinif)) secSinif = urlSinif;
    let secDeneme = 0; // 0 = Tüm haftalar/denemeler
    let aramaMetin = '';

    // Hafta seçenekleri (1..8)
    const haftaSecenekleri = [];
    const gorulenHafta = new Set();
    for (const b of sinifBloklari) {
      for (const s of (b.sinavlar || [])) {
        if (!gorulenHafta.has(s.deneme_no)) {
          gorulenHafta.add(s.deneme_no);
          haftaSecenekleri.push({ no: s.deneme_no, ad: `Deneme ${s.deneme_no} · ${s.hafta_adi}` });
        }
      }
    }
    haftaSecenekleri.sort((a, b) => a.no - b.no);

    // Üst kontrol çubuğu: Sınıf sekmeleri + Hafta seçici + Konu/Kazanım arama
    const sinifSekmeKutu = el('div', { sinif: 'asds-sinif-sekmeler', role: 'tablist', 'aria-label': 'Sınıf başlığı seçimi' });
    const haftaSelect = el('select', { sinif: 'asds-hafta-sec', 'aria-label': 'Deneme haftası süzgeci' },
      el('option', { value: '0' }, `Tüm Haftalar (${haftaSecenekleri.length} Hafta)`),
      ...haftaSecenekleri.map((h) => el('option', { value: String(h.no) }, h.ad)));
    const araInput = el('input', {
      type: 'search',
      sinif: 'agac-konu-ara asds-ara-girdi',
      placeholder: 'Hafta, ders, kazanım veya konu ara (ör. Ekim 4. hafta, Güneş, karekök, fiilimsiler)…',
      'aria-label': 'Deneme sınavlarında konu veya hafta ara',
      autocomplete: 'off',
    });
    const sayacRozet = el('span', { sinif: 'belge-sonuc-sayac', 'aria-live': 'polite' });

    const suzgecCubugu = el('div', { sinif: 'asds-kontrol-pano' },
      sinifSekmeKutu,
      el('div', { sinif: 'agac-suzgec-cubuk asds-suzgec-alt' },
        el('div', { sinif: 'agac-suzgec-arama' }, simge('mercek'), araInput),
        el('label', { sinif: 'asds-hafta-etiket' }, 'Hafta:', haftaSelect),
        sayacRozet));

    // Sınıf hızlı atlama çubuğu (Tümü seçiliyken ilgili sınıfın başlığına tek tıkla kaydırır)
    const hizliBaslikBar = el('nav', { sinif: 'asds-baslik-gecis', 'aria-label': 'Sınıf başlıklarına hızlı geçiş' },
      el('span', { sinif: 'asds-gecis-etiket' }, 'Sınıf Başlıkları:'),
      ...sinifBloklari.map((b) => el('a', {
        sinif: 'asds-gecis-cip',
        'data-renk': b.renk,
        href: `#asds-sinif-${b.sinif}`,
        onclick: (e) => {
          if (secSinif !== 0 && secSinif !== Number(b.sinif)) {
            e.preventDefault();
            secSinif = 0;
            ciz();
            requestAnimationFrame(() => document.getElementById(`asds-sinif-${b.sinif}`)?.scrollIntoView({ behavior: 'smooth' }));
          }
        },
      }, `${b.sinif}. Sınıf (${(b.sinavlar || []).length} Deneme) ↓`)));

    const icerikAlani = el('div', { sinif: 'asds-sinif-listesi' });

    const pdfDugme = (href, baslik, altMetin, turSinif, etiket) => el('a', {
      sinif: `asds-pdf-dugme ${turSinif}`,
      href,
      target: '_blank',
      rel: 'noopener',
      'aria-label': `${etiket} — ${baslik} (${altMetin})`,
    },
    simge(turSinif.includes('cevapli') ? 'onay' : 'indir'),
    el('span', { sinif: 'asds-dugme-metin' },
      el('strong', {}, baslik),
      el('small', {}, altMetin)));

    const sinavKarti = (s, b) => {
      const etiketBaz = `${s.sinif}. Sınıf ${s.ad}`;
      const anahtarDizi = Object.entries(s.anahtar_a || {});
      return el('article', {
        sinif: 'asds-kart',
        id: s.kimlik,
        'data-renk': b.renk,
      },
      // 1. Üst Başlık ve Meta
      el('div', { sinif: 'asds-kart-ust' },
        el('div', { sinif: 'asds-kart-baslik-sol' },
          el('span', { sinif: 'asds-deneme-rozet' }, `${s.sinif}. SINIF · DENEME ${s.deneme_no}`),
          el('h3', {}, `${s.sinif}. Sınıf · ${s.hafta_adi} Akademik Süreç Değerlendirme Sınavı`),
          el('p', { sinif: 'asds-kart-altbilgi' },
            el('strong', {}, `Uygulama: ${s.tarih_araligi}`),
            ' · ',
            el('span', {}, `Kapsam: ${s.olculen_hafta}`))),
        el('div', { sinif: 'asds-kart-meta-sag' },
          el('span', { sinif: 'asds-meta-cip' }, `${s.soru_sayisi} Soru`),
          el('span', { sinif: 'asds-meta-cip' }, `${s.sure} Dakika`),
          el('span', { sinif: 'asds-meta-cip' }, `A & B Kitapçığı · ${s.sayfa_sayisi} Sayfa`))),

      // 2. İki Ayrı Kutu: Cevapsız Kitapçıklar (A & B) VE Cevaplı Kitapçıklar (A & B + Cevap Anahtarı)
      el('div', { sinif: 'asds-kitapcik-izgara' },
        // Kutu 1: CEVAPSIZ KİTAPÇIKLAR (A ve B)
        el('div', { sinif: 'asds-kitapcik-kutu cevapsiz-kutu' },
          el('div', { sinif: 'asds-kutu-baslik' },
            el('span', { sinif: 'asds-kutu-simge', 'aria-hidden': 'true' }, simge('indir')),
            el('div', {},
              el('strong', {}, 'Cevapsız Soru Kitapçıkları (Öğrenci / Sınav Uygulaması)'),
              el('small', {}, '24 sayfa renkli kitapçık + son sayfada kodlamalı optik cevap kâğıdı'))),
          el('div', { sinif: 'asds-dugme-grup' },
            pdfDugme(s.dosyalar.a_cevapsiz, 'A Kitapçığı (Cevapsız)', 'Soru Kitapçığı · PDF İndir / Aç', 'cevapsiz-a', etiketBaz),
            pdfDugme(s.dosyalar.b_cevapsiz, 'B Kitapçığı (Cevapsız)', 'Soru Kitapçığı · PDF İndir / Aç', 'cevapsiz-b', etiketBaz))),

        // Kutu 2: CEVAPLI KİTAPÇIKLAR (A ve B) + CEVAP ANAHTARI
        el('div', { sinif: 'asds-kitapcik-kutu cevapli-kutu' },
          el('div', { sinif: 'asds-kutu-baslik' },
            el('span', { sinif: 'asds-kutu-simge', 'aria-hidden': 'true' }, simge('onay')),
            el('div', {},
              el('strong', {}, 'Cevaplı Kitapçıklar & Cevap Anahtarı (Öğretmen / Çözüm Kontrol)'),
              el('small', {}, 'Sorular üzerinde doğru seçenekler işaretli A ve B kitapçıkları + birleşik cevap anahtarı'))),
          el('div', { sinif: 'asds-dugme-grup uclu' },
            pdfDugme(s.dosyalar.a_cevapli, 'A Kitapçığı (Cevaplı)', 'Doğru Şıklar İşaretli + Anahtar · PDF', 'cevapli-a', etiketBaz),
            pdfDugme(s.dosyalar.b_cevapli, 'B Kitapçığı (Cevaplı)', 'Doğru Şıklar İşaretli + Anahtar · PDF', 'cevapli-b', etiketBaz),
            pdfDugme(s.dosyalar.anahtar, 'Cevap Anahtarı (A & B)', '2 Sayfa Öğretmen Anahtarı · PDF', 'cevapli-anahtar', etiketBaz)))),

      // 3. Ölçülen Kazanımlar ve Hızlı Cevap Anahtarı Özeti
      el('details', { sinif: 'asds-detay-kutu' },
        el('summary', {},
          el('span', {}, `📚 ${s.hafta_adi} Sınavında Ölçülen Ders Konuları, Kazanımlar ve Hızlı Cevap Anahtarı`),
          el('small', {}, `${(s.kapsam || []).length} ders kapsamı ▾`)),
        el('div', { sinif: 'asds-detay-icerik' },
          el('div', { sinif: 'asds-kapsam-liste' },
            ...(s.kapsam || []).map(([dAd, dKonu]) => el('div', { sinif: 'asds-kapsam-satir' },
              el('strong', {}, dAd),
              el('span', {}, dKonu)))),
          anahtarDizi.length ? el('div', { sinif: 'asds-hizli-anahtar' },
            el('p', { sinif: 'asds-ha-baslik' }, 'A Kitapçığı Hızlı Cevap Dizisi (B kitapçığı anahtarı PDF içindedir):'),
            el('div', { sinif: 'asds-ha-grid' },
              ...anahtarDizi.map(([dersAd, dizi]) => el('div', { sinif: 'asds-ha-ders' },
                el('b', {}, dersAd),
                el('code', {}, dizi.split('').map((harf, idx) => `${idx + 1}-${harf}`).join('  ')))))) : null)));
    };

    const sinifBolumuCiz = (b) => {
      const q = normal(aramaMetin);
      const uygunSinavlar = (b.sinavlar || []).filter((s) => {
        if (secDeneme && s.deneme_no !== secDeneme) return false;
        if (!q) return true;
        const metin = normal(`${s.sinif}. sınıf ${s.ad} ${s.hafta_adi} ${s.tarih_araligi} ${s.olculen_hafta} ${(s.kapsam || []).map((x) => x.join(' ')).join(' ')}`);
        return metin.includes(q);
      });
      if (!uygunSinavlar.length) return null;

      return el('section', {
        sinif: 'asds-sinif-bolum',
        id: `asds-sinif-${b.sinif}`,
        'data-renk': b.renk,
        'aria-labelledby': `asds-baslik-${b.sinif}`,
      },
      el('div', { sinif: 'asds-sinif-baslik' },
        el('div', { sinif: 'asds-sb-sol' },
          el('span', { sinif: 'asds-sinif-rozet' }, `${b.sinif}. SINIF`),
          el('div', {},
            el('h2', { id: `asds-baslik-${b.sinif}` }, b.baslik),
            el('p', {}, `${b.puanlama} · Her sınavda Cevapsız A/B kitapçıkları ile Cevaplı A/B kitapçıkları ayrı ayrı sunulmuştur.`))),
        el('div', { sinif: 'asds-sb-dersler', 'aria-label': `${b.sinif}. sınıf sınav ders dağılımı` },
          ...(b.ders_dagilimi || []).map((d) => el('a', {
            sinif: 'asds-ders-cip',
            href: `/ogrenci.html?sinif=${b.sinif}&ders=${encodeURIComponent(d.kod)}`,
            title: `${b.sinif}. Sınıf ${d.ders} konu özetleri ve çalışma kâğıtları`,
          },
          el('strong', {}, d.ders),
          el('span', {}, `${d.soru} soru`))))),
      el('div', { sinif: 'asds-kartlar' },
        ...uygunSinavlar.map((s) => sinavKarti(s, b))));
    };

    const ciz = () => {
      // Sekmeler
      const toplamTumu = sinifBloklari.reduce((t, b) => t + (b.sinavlar || []).length, 0);
      sinifSekmeKutu.replaceChildren(
        el('button', {
          type: 'button',
          role: 'tab',
          sinif: 'asds-sekme',
          'data-renk': 'mavi',
          'aria-selected': String(secSinif === 0),
          onclick: () => { secSinif = 0; ciz(); },
        }, `Tüm Sınıflar Ayrı Başlıkta (${toplamTumu} Sınav)`),
        ...sinifBloklari.map((b) => el('button', {
          type: 'button',
          role: 'tab',
          sinif: 'asds-sekme',
          'data-renk': b.renk,
          'aria-selected': String(secSinif === Number(b.sinif)),
          onclick: () => { secSinif = Number(b.sinif); ciz(); },
        }, `${b.sinif}. Sınıf (${(b.sinavlar || []).length} Sınav)`)));

      hizliBaslikBar.hidden = secSinif !== 0;

      const hedefler = secSinif ? sinifBloklari.filter((b) => Number(b.sinif) === secSinif) : sinifBloklari;
      const bolumler = hedefler.map(sinifBolumuCiz).filter(Boolean);

      const gosterilenSinav = hedefler.reduce((t, b) => {
        const q = normal(aramaMetin);
        return t + (b.sinavlar || []).filter((s) => (!secDeneme || s.deneme_no === secDeneme)
          && (!q || normal(`${s.sinif}. sınıf ${s.ad} ${s.hafta_adi} ${s.tarih_araligi} ${s.olculen_hafta} ${(s.kapsam || []).map((x) => x.join(' ')).join(' ')}`).includes(q))).length;
      }, 0);

      sayacRozet.textContent = `${gosterilenSinav} sınav · ${gosterilenSinav * 5} PDF (A/B Cevapsız & Cevaplı)`;

      if (bolumler.length) {
        icerikAlani.replaceChildren(...bolumler);
      } else {
        icerikAlani.replaceChildren(
          el('div', { sinif: 'yakinda' },
            el('div', { sinif: 'yakinda-simge', 'aria-hidden': 'true' }, simge('mercek')),
            el('div', {},
              el('h3', {}, 'Eşleşen deneme sınavı bulunamadı'),
              el('p', {}, 'Arama kutusunu temizleyebilir veya tüm sınıfları/haftaları seçebilirsiniz.'),
              el('button', {
                type: 'button',
                sinif: 'dugme ana',
                onclick: () => { secSinif = 0; secDeneme = 0; aramaMetin = ''; araInput.value = ''; haftaSelect.value = '0'; ciz(); },
              }, 'Tüm Sınavları Göster'))));
      }
    };

    haftaSelect.addEventListener('change', () => {
      secDeneme = Number(haftaSelect.value) || 0;
      ciz();
    });
    araInput.addEventListener('input', () => {
      aramaMetin = araInput.value;
      ciz();
    });

    kapsayici.replaceChildren(suzgecCubugu, hizliBaslikBar, icerikAlani);
    ciz();

    // Hash ile gelindiyse (#asds-sinif-6 veya #asds-6-2026-10-h4) ilgili öğeye kaydır
    if (location.hash.startsWith('#asds-')) {
      const hedefId = decodeURIComponent(location.hash.slice(1));
      requestAnimationFrame(() => document.getElementById(hedefId)?.scrollIntoView({ behavior: 'smooth', block: 'start' }));
    }
  });
})();
