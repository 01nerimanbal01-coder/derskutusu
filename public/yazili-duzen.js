// Yazılılar sayfası düzeni (kullanıcı 13.10.2026): önce sınıf ve ders seçimi, sonra iki açık başlık:
//   1 · Senaryoya göre yazılı (ÖDSGM senaryo tablosu + hazır kâğıt ve cevap anahtarı; bölümü yazili.js çizer)
//   2 · Öğrenme çıktısına göre yazılı (her çıktı için 2 sayfalık kâğıt; bu betik aynı JSON'dan çizer)
// yazili.js (DKYAZILI) ve yazili-cikti.js (DKCIKTI) başka projelerin yayın dosyalarıdır, değiştirilmez. Bu betik onlar çizimi
// bitirdikten sonra çalışır: yazili-cikti.js'in bölümünü kaldırıp 2 numaralı bölümü kendi başlığı ve "Öğrenci kâğıdı (PDF)" /
// "Cevap anahtarı (PDF)" adlarıyla yeniden çizer. Öğrenci dalı (agac.js) yalnız öğrenci kâğıdını gösterir; cevap anahtarı yalnız burada.
//   yazili.html                     → sınıf ve ders seçimi
//   yazili.html?sinif=N&ders=<ad>   → seçili dersin iki bölümü (#senaryo-yazilisi, #cikti-yazililari)
(() => {
  const ana = $('#senaryo-yazilisi');
  if (!ana) return;
  const p = new URLSearchParams(location.search);
  const sinif = Number(p.get('sinif')), ders = p.get('ders');
  document.body.classList.add('yd-bekle');
  const bitir = () => document.body.classList.remove('yd-bekle');
  setTimeout(bitir, 5000);   // veri gelmezse sayfa gizli kalmasın

  const normal = (s) => String(s || '').toLocaleLowerCase('tr').replace(/[^a-zçğıöşü0-9]+/g, ' ').trim();
  const bekle = (ms) => new Promise((r) => setTimeout(r, ms));
  const indir = (href, ad, etiket, ana) => el('a', { sinif: `dugme${ana ? ' ana' : ''}`, href, download: '', 'aria-label': `${ad}: ${etiket}` }, simge('indir'), ad);

  Promise.all([veri('senaryolar.json'), veri('yazili-kagitlari.json'), veri('yazili-cikti.json'),
    sinif && ders ? veri(`agac/${sinif}-${ders}.json`) : null, ortakVeri]).then(async ([sen, kagit, cikti, agac, ortak]) => {
    const anahtar = `${sinif}-${ders}`;
    const t = sen?.tablolar?.[anahtar];
    const liste = cikti?.tablolar?.[anahtar];
    const secili = Boolean(t || liste);
    const ciktiVar = secili ? Boolean(liste) : (!p.has('sinif') && !p.has('ders') && Object.keys(cikti?.tablolar || {}).length > 0);
    // yazili.js ve yazili-cikti.js kendi bölümlerini çizene kadar bekle (en çok 4 sn)
    for (let i = 0; i < 80; i++) {
      if ($('#y-tablo')?.childElementCount > 0 && (!ciktiVar || $('#cikti-yazililari'))) break;
      await bekle(50);
    }
    $('#cikti-yazililari')?.remove();   // yazili-cikti.js'in bölümü (adı ve düzeni eski); yerine 2 numaralı bölüm
    const gecisP = $('#y-siniflar + p');
    if (gecisP && $('a[href="#cikti-yazililari"]', gecisP)) gecisP.remove();
    const yolSinif = $('#y-yol-sinif');
    if (yolSinif) { yolSinif.textContent = 'Öğretmen Köşesi'; yolSinif.href = '/ogretmen.html'; }
    const giris = $('#yd-giris');
    const secim = $('#yd-secim');
    const dersAd = (d, x) => ortak?.dersler?.dersler?.[d] || x?.dersAd || d;

    if (!secili) {
      // Sınıf ve ders seçimi
      ana.hidden = true;
      $('#yd-gecis').hidden = true;
      $('#y-baslik').textContent = 'Yazılılar';
      document.title = 'Yazılılar: sınıf ve ders seçin · Ders Kutusu';
      const sira = Object.keys(ortak?.dersler?.dersler || {});
      const yer = (d) => { const i = sira.indexOf(d); return i < 0 ? sira.length : i; };
      const tablolar = Object.values(sen?.tablolar || {});
      const siniflar = [...new Set(tablolar.map((x) => x.sinif))].sort((a, b) => a - b);
      let kayitliSinif = 8;
      try { kayitliSinif = Number(localStorage.getItem('dk-secili-sinif')) || 8; } catch {}
      let sec = siniflar.includes(sinif) ? sinif : (siniflar.includes(kayitliSinif) ? kayitliSinif : (siniflar[0] || 0));
      const bilinmeyen = p.has('sinif') && p.has('ders');
      const dersDugme = (x) => {
        const k = `${x.sinif}-${x.ders}`;
        const hazir = Boolean(kagit?.tablolar?.[k] || kagit?.ulke?.[k]);
        const n = cikti?.tablolar?.[k]?.length;
        return el('li', {}, el('a', { sinif: 'yd-ders', href: `?sinif=${x.sinif}&ders=${encodeURIComponent(x.ders)}` },
          dersAd(x.ders, x),
          el('small', {}, `Senaryo: ${hazir ? 'tablo ve hazır kâğıt' : 'tablo'}`),
          el('small', {}, `Öğrenme çıktısı: ${n ? `${n} kâğıt` : 'hazırlanıyor'}`)));
      };
      const ciz = (odak) => {
        secim.replaceChildren(...[
          bilinmeyen ? el('p', { sinif: 'yd-not' }, 'Bu sınıf ve ders için yazılı bulunamadı; aşağıdan seçebilirsiniz.') : null,
          el('p', { sinif: 'yd-adim', id: 'yd-sinif-b' }, '1. adım: sınıfı seçin'),
          el('div', { sinif: 'yd-sinif-sec', role: 'group', 'aria-labelledby': 'yd-sinif-b' }, siniflar.map((n) => el('button', {
            type: 'button', sinif: 'sekme', 'aria-pressed': String(n === sec), onclick: () => { sec = n; try { localStorage.setItem('dk-secili-sinif', String(n)); } catch {} ciz(true); } }, `${n}. sınıf`))),
          sec ? [el('p', { sinif: 'yd-adim', id: 'yd-ders-b' }, `2. adım: ${sec}. sınıf dersini seçin`),
            el('ul', { sinif: 'yd-dersler', 'aria-labelledby': 'yd-ders-b' },
              tablolar.filter((x) => x.sinif === sec).sort((a, b) => yer(a.ders) - yer(b.ders)).map(dersDugme))]
            : el('p', { sinif: 'yd-ipucu' }, 'Önce sınıfı seçin; o sınıfın dersleri burada açılır.')].flat().filter(Boolean));
        if (odak) $('[aria-pressed="true"]', secim)?.focus();
      };
      ciz(false);
      bitir();
      return;
    }

    // Seçili ders: iki bölüm
    const ad = dersAd(ders, t);
    document.title = `${sinif}. sınıf ${ad} yazılıları · Ders Kutusu`;
    $('#y-baslik').textContent = `${sinif}. sınıf ${ad}: yazılılar`;
    $('nav.yol')?.append(el('span', { 'aria-hidden': 'true' }, '/'), el('span', { 'aria-current': 'page' }, `${sinif}. sınıf ${ad}`));
    giris?.replaceChildren('Bu ders için iki ayrı yazılı türü var; her birinin öğrenci kâğıdı ve cevap anahtarı birlikte. Cevap anahtarları yalnız bu sayfadadır; öğrenciler kâğıtları ',
      el('a', { href: '/ogrenci.html' }, 'Öğrenci'), ' bölümünde yalnızca öğrenci kâğıdı olarak bulur.');
    const siraSecili = Object.keys(ortak?.dersler?.dersler || {});
    const yerSecili = (d) => { const i = siraSecili.indexOf(d); return i < 0 ? siraSecili.length : i; };
    const ayniSinifDersler = Object.values(sen?.tablolar || {}).filter((x) => x.sinif === sinif).sort((a, b) => yerSecili(a.ders) - yerSecili(b.ders));
    secim.replaceChildren(
      el('p', { sinif: 'yd-secili' }, 'Seçili ders: ', el('strong', {}, `${sinif}. sınıf ${ad}`), ' · ',
        el('a', { href: `/yazili.html?sinif=${sinif}` }, 'Tüm sınıflar'), ' · ',
        el('a', { href: `/ogrenci.html?sinif=${sinif}&ders=${encodeURIComponent(ders)}` }, 'Dersin Konu Özetleri & Çalışma Kâğıtları →'), ' · ',
        el('button', {
          type: 'button',
          sinif: 'agac-hizli-dugme ig-kart',
          onclick: () => window.dkIgKartAc && window.dkIgKartAc(sinif, ders, `${sinif}. Sınıf ${ad} · Yazılıya Hazırlık`, [1, 2, 3, 4]),
        }, simge('instagram'), el('span', {}, '📸 Yazılı IG Özeti')), ' ',
        el('button', {
          type: 'button',
          sinif: 'dk-ig-paylas-btn asds-wa-btn',
          onclick: (e) => window.dkSayfaPaylas && window.dkSayfaPaylas(e.currentTarget),
        }, '🟢 WhatsApp’ta Paylaş')),
      ayniSinifDersler.length > 1 ? el('nav', { sinif: 'yd-hizli-dersler', 'aria-label': `${sinif}. sınıf diğer ders yazılıları` },
        ...ayniSinifDersler.map((x) => el('a', {
          sinif: `yd-hizli-cip${x.ders === ders ? ' aktif' : ''}`,
          href: `?sinif=${sinif}&ders=${encodeURIComponent(x.ders)}`,
          'aria-current': x.ders === ders ? 'page' : null,
        }, dersAd(x.ders, x)))) : null);

    // 1 · senaryoya göre (yazili.js çizdi): hazır kâğıt yoksa not, senaryo tablosu da yoksa açıklama
    const hazirKagit = Boolean(kagit?.tablolar?.[anahtar] || kagit?.ulke?.[anahtar]);
    const aciklama1 = $('.yd-aciklama', ana);
    if (!t) {
      $('.y-secim', ana).hidden = true;
      $('#y-tablo').replaceChildren(el('p', { sinif: 'yd-bos' }, 'Bu ders için ÖDSGM ortak yazılı senaryosu yayımlanmamış.'));
    } else if (!hazirKagit) {
      aciklama1.after(el('p', { sinif: 'yd-not' }, 'Bu ders için hazır senaryo kâğıdı henüz yok; senaryo tablosu şimdilik kullanılabilir.'));
    }

    // 2 · öğrenme çıktısına göre: ünite ünite, her çıktı satırında öğrenci kâğıdı ve cevap anahtarı
    const konular = (agac?.uniteler || []).flatMap((u, ui) => u.konular.map((k) => ({ ad: k.ad, unite: u.ad, ui })));
    const uniteBul = (c) => {
      const kn = normal(c.konu);
      const k = konular.find((x) => normal(x.ad) === kn) || konular.find((x) => kn && normal(x.ad).includes(kn));
      return k ? { ui: k.ui, ad: `${k.ui + 1}. ünite: ${k.unite}` } : { ui: 999, ad: konular.length ? 'Diğer çıktılar' : '' };
    };
    const satir = (c) => el('li', { sinif: 'yd-satir', 'data-arama': normal(`${c.kod} ${c.ifade} ${c.konu}`) },
      el('div', { sinif: 'yd-govde' }, el('strong', {}, c.kod), el('div', {}, c.ifade), el('small', {}, `${c.konu} · ${c.soru} soru`)),
      el('div', { sinif: 'g-dugmeler' },
        indir(`${cikti.klasor}${c.dosya}.pdf`, 'Öğrenci kâğıdı (PDF)', `${c.kod} ${c.ifade}`, true),
        indir(`${cikti.klasor}${c.dosya}-cevapli.pdf`, 'Cevap anahtarı (PDF)', `${c.kod} ${c.ifade}`, false)));
    let ic;
    let ciktiSuzgec = null;
    if (liste?.length) {
      const gruplar = new Map();
      for (const c of liste) {
        const u = uniteBul(c);
        if (!gruplar.has(u.ad)) gruplar.set(u.ad, { ...u, kalemler: [] });
        gruplar.get(u.ad).kalemler.push(c);
      }
      const uniteBloklari = [...gruplar.values()].sort((a, b) => a.ui - b.ui).map((u) => {
        const bas = u.ad ? el('h3', { sinif: 'yd-unite' }, u.ad) : null;
        const ol = el('ol', { sinif: 'yd-liste' }, u.kalemler.map(satir));
        return { bas, ol };
      });
      ic = uniteBloklari.flatMap((b) => [b.bas, b.ol]);
      if (liste.length > 4) {
        const araInput = el('input', {
          type: 'search',
          sinif: 'agac-konu-ara yd-cikti-ara-girdi',
          placeholder: `Öğrenme çıktısı kodu, kazanım veya konu ara (${liste.length} hazır yazılı kâğıdı)…`,
          'aria-label': 'Öğrenme çıktısı yazılılarında ara',
          autocomplete: 'off',
        });
        const sayacEl = el('span', { sinif: 'belge-sonuc-sayac' }, `${liste.length} yazılı kâğıdı`);
        araInput.addEventListener('input', () => {
          const q = normal(araInput.value);
          let top = 0;
          uniteBloklari.forEach(({ bas, ol }) => {
            let g = 0;
            $$('.yd-satir', ol).forEach((li) => {
              const u = !q || String(li.dataset.arama || '').includes(q);
              li.hidden = !u;
              if (u) g++;
            });
            ol.hidden = g === 0;
            if (bas) bas.hidden = g === 0;
            top += g;
          });
          sayacEl.textContent = top === liste.length ? `${liste.length} yazılı kâğıdı` : `${top} / ${liste.length} yazılı gösteriliyor`;
        });
        ciktiSuzgec = el('div', { sinif: 'agac-suzgec-cubuk yd-cikti-suzgec' },
          el('div', { sinif: 'agac-suzgec-arama' }, simge('mercek'), araInput),
          sayacEl);
      }
    } else ic = [el('p', { sinif: 'yd-bos' }, 'Bu ders için hazırlanıyor. Hazır oldukça burada görünecek.')];
    ana.after(el('section', { sinif: 'bolum y-bolum', id: 'cikti-yazililari', 'aria-labelledby': 'yd-s2-baslik' }, el('div', { sinif: 'kap' },
      el('h2', { sinif: 'yd-baslik', id: 'yd-s2-baslik' }, '2 · Öğrenme çıktısına göre yazılı'),
      el('p', { sinif: 'yd-aciklama' }, 'Her öğrenme çıktısı için ayrı, 2 sayfalık bir kâğıt: tek bir çıktının kazanılıp kazanılmadığını ölçmek ya da çıktı bazlı yazılı yapmak için kullanılır.'),
      liste?.length ? el('p', { sinif: 'yd-not' }, 'Her kâğıt 6–8 açık uçlu soru, 40 dakika, 100 puandır; sorular MEB ders kitabına dayanır. Öğrenci kâğıdındaki karekod cevap anahtarını açar.') : null,
      ciktiSuzgec,
      ...ic)));

    // Bölüm geçişi (eski pembe düğmenin yerine): her başlığa tek dokunuşla atla
    const gecis = $('#yd-gecis');
    gecis.replaceChildren(
      el('a', { href: '#senaryo-yazilisi' }, '1 · Senaryoya göre yazılı', el('small', {}, t ? `ÖDSGM senaryo tablosu${hazirKagit ? ' ve hazır kâğıt' : ''}` : 'senaryo yayımlanmamış')),
      el('a', { href: '#cikti-yazililari' }, '2 · Öğrenme çıktısına göre yazılı', el('small', {}, liste?.length ? `${liste.length} hazır kâğıt` : 'hazırlanıyor')));
    gecis.hidden = false;
    bitir();
    // Bölümler sayfa açıldıktan sonra çizildiği için #cikti-yazililari / #senaryo-yazilisi bağlantısıyla gelindiyse oraya kaydır
    if (location.hash === '#cikti-yazililari' || location.hash === '#senaryo-yazilisi') {
      requestAnimationFrame(() => document.getElementById(location.hash.slice(1))?.scrollIntoView({ behavior: 'instant' }));
    }
  }).catch(bitir);
})();
