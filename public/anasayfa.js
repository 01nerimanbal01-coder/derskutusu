// Ana sayfa: "Kaldığın yerden devam et", DersimizMatematik tarzı "Sınıf ve Ders Merkezi" (#sinif-merkezi) ve "Bu hafta derste" (#bu-hafta).
// Hafta, sınıfın yıllık plan takviminden (veri/agac/<sınıf>-<ders>.json "haftalar") bulunur; konu anlatımları içerik dizininden.
// Seçilen sınıf ve son bakılan konular yalnız bu tarayıcıda tutulur (localStorage); dışarıdan hiçbir şey yüklenmez.
(() => {
  'use strict';
  const alan = document.getElementById('bu-hafta');
  const liste = document.getElementById('bh-liste');
  const merkez = document.getElementById('sinif-merkezi');
  if (!alan || !liste) return;
  const K = () => window.Kesif || { subjectColor: () => 'mavi', gradeColor: () => 'mavi' };
  const SINIF_ANAHTAR = 'dk-sinif';
  const sinifOku = () => { try { return Number(localStorage.getItem(SINIF_ANAHTAR)) || null; } catch { return null; } };
  const sinifYaz = (n) => { try { localStorage.setItem(SINIF_ANAHTAR, String(n)); } catch {} };
  const yol = (a) => (/^(https?:)?\//.test(a) ? a : `/${a}`);
  // "8. Sınıf Matematik 7. Hafta: Konu (M.8.1.3.7)" → "Konu"
  const konuAdi = (b) => String(b || '').replace(/^\d+\.\s*Sınıf\s.*?\d+\.\s*Hafta:\s*/i, '').replace(/\s*\((?:[A-ZÇĞİÖŞÜ]{1,4}\.?\s?\d[^()]*|[^()]*\d\.\d[^()]*)\)\s*$/, '').trim();
  const SINIF_ETIKET = { 8: '8. Sınıf · LGS', 12: '12. Sınıf · YKS' };
  const sinifEtiket = (n) => SINIF_ETIKET[n] || `${n}. Sınıf`;

  // Kaldığın yerden devam et (ortak.js): yalnız daha önce konu açılmışsa görünür
  const devam = typeof sonBakilan === 'object' ? sonBakilan.bolum() : null;
  if (devam) (merkez || alan).before(devam);

  // ---- Karşılama sahnesi: Canlı Etkileşimli Ders Önizlemesi (#m-canli-kart) ----
  const canliKart = document.getElementById('m-canli-kart');
  if (canliKart) {
    const gorselYer = document.getElementById('m-canli-gorsel');
    const etiketYer = document.getElementById('m-canli-etiket');
    const soruYer = document.getElementById('m-canli-soru');
    const siklarYer = document.getElementById('m-canli-siklar');
    const donutYer = document.getElementById('m-canli-donut');
    const kesirHtml = (p, q) => `<span class="m-kesir"><b>${p}</b><i></i><b>${q}</b></span>`;
    const ORNEKLER = {
      mat: {
        etiket: '6. Sınıf · Kesirler',
        soru: 'Modeldeki boyalı bölge toplamda hangi kesre denk olur?',
        svg: `<svg viewBox="0 0 360 128" role="img" aria-label="Sekiz eş parçaya bölünmüş 3 boyutlu kesir modeli">
          <defs>
            <linearGradient id="mg-zemin" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F0F7FF"/><stop offset="100%" stop-color="#E1EEFF"/></linearGradient>
            <linearGradient id="mg-dolu" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2B7FFF"/><stop offset="100%" stop-color="#0A58D6"/></linearGradient>
            <linearGradient id="mg-ek" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FF982E"/><stop offset="100%" stop-color="#F06A00"/></linearGradient>
            <linearGradient id="mg-bos" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFFFFF"/><stop offset="100%" stop-color="#E7EFFB"/></linearGradient>
          </defs>
          <rect x="4" y="4" width="352" height="120" rx="16" fill="url(#mg-zemin)"/>
          <g transform="translate(28, 28)">
            <rect x="0" y="6" width="304" height="58" rx="11" fill="#BDD2F2"/>
            <rect x="0" y="0" width="304" height="58" rx="11" fill="url(#mg-bos)" stroke="#B8CEEE" stroke-width="1.2"/>
            <rect x="4" y="4" width="35" height="50" rx="7" fill="url(#mg-dolu)"/>
            <rect x="41.5" y="4" width="35" height="50" rx="7" fill="url(#mg-dolu)"/>
            <rect x="79" y="4" width="35" height="50" rx="7" fill="url(#mg-dolu)"/>
            <rect x="116.5" y="4" width="35" height="50" rx="7" fill="url(#mg-dolu)"/>
            <rect x="154" y="4" width="35" height="50" rx="7" fill="url(#mg-dolu)"/>
            <rect x="191.5" y="4" width="35" height="50" rx="7" fill="url(#mg-ek)" stroke="#CC5600" stroke-width="1" stroke-dasharray="3 2"/>
            <text x="209" y="34" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="800">+1</text>
            <rect x="229" y="4" width="35" height="50" rx="7" fill="url(#mg-bos)" stroke="#CBD9EE"/>
            <rect x="266.5" y="4" width="33.5" height="50" rx="7" fill="url(#mg-bos)" stroke="#CBD9EE"/>
          </g>
          <text x="180" y="109" text-anchor="middle" fill="#23406E" font-size="11" font-weight="700">8 eş parçadan 5 maviye 1 turuncu parça eklendi</text>
        </svg>`,
        siklar: [kesirHtml(5, 8), kesirHtml(3, 4), kesirHtml(1, 2)],
        dogru: 1,
        aciklama: 'Doğru! 8 eş parçadan 6 parça boyalıdır; sadeleştirince dörtte üç kesrine denk olur.',
        yanlis: 'İpucu: 5 mavi + 1 turuncu = 6 boyalı parça eder. Sekizde altıyı 2 ile sadeleştirmeyi dene.',
        bag: '/ogrenci.html?sinif=6&ders=matematik',
      },
      fen: {
        etiket: '8. Sınıf · Basınç',
        soru: 'Aynı sıvıyla dolu kapta K ve L noktalarındaki sıvı basınçları nasıl sıralanır?',
        svg: `<svg viewBox="0 0 360 128" role="img" aria-label="Sıvı dolu dereceli kapta K ve L noktalarının derinlikleri">
          <defs>
            <linearGradient id="fg-sivi" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#60A5FA" stop-opacity="0.65"/><stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.88"/></linearGradient>
          </defs>
          <rect x="4" y="4" width="352" height="120" rx="16" fill="#EEF8F4"/>
          <rect x="112" y="16" width="136" height="96" rx="10" fill="#FFFFFF" stroke="#64748B" stroke-width="1.8"/>
          <path d="M114 34 H246 V103 Q246 110 239 110 H121 Q114 110 114 103 Z" fill="url(#fg-sivi)"/>
          <ellipse cx="180" cy="34" rx="66" ry="5" fill="#93C5FD"/>
          <circle cx="156" cy="56" r="5" fill="#FF7A00" stroke="#FFFFFF" stroke-width="1.5"/>
          <text x="170" y="60" fill="#FFFFFF" font-size="13" font-weight="800">K (10 cm)</text>
          <circle cx="156" cy="94" r="5" fill="#FACC15" stroke="#FFFFFF" stroke-width="1.5"/>
          <text x="170" y="98" fill="#FFFFFF" font-size="13" font-weight="800">L (30 cm)</text>
        </svg>`,
        siklar: ['K > L', 'L > K', 'K = L'],
        dogru: 1,
        aciklama: 'Harika! Aynı cins sıvıda derinlik arttıkça sıvı basıncı artar; L noktası daha derindedir.',
        yanlis: 'İpucu: Sıvı basıncı sıvının açık yüzeyine olan derinlikle doğru orantılıdır.',
        bag: '/ogrenci.html?sinif=8&ders=fen',
      },
      tur: {
        etiket: '7. Sınıf · Söz Sanatları',
        soru: 'Yukarıdaki dizelerde altı çizili ifadeyle hangi söz sanatı yapılmıştır?',
        svg: `<svg viewBox="0 0 360 128" role="img" aria-label="Şiir dizesi kartı">
          <rect x="4" y="4" width="352" height="120" rx="16" fill="#FFF7ED"/>
          <rect x="26" y="20" width="308" height="88" rx="12" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.4"/>
          <text x="180" y="54" text-anchor="middle" fill="#0D244F" font-size="14" font-weight="700">“Rüzgâr bu sabah pencereme</text>
          <text x="180" y="78" text-anchor="middle" fill="#D97706" font-size="14.5" font-weight="800" text-decoration="underline">eski bir masalı fısıldadı.”</text>
        </svg>`,
        siklar: ['Benzetme', 'Kişileştirme', 'Abartma'],
        dogru: 1,
        aciklama: 'Doğru! İnsana ait “masal fısıldama” özelliği rüzgâra verilerek kişileştirme yapılmıştır.',
        yanlis: 'İpucu: “Fısıldamak” insana özgü bir eylemdir; doğadaki bir varlığa aktarılmış.',
        bag: '/ogrenci.html?sinif=7&ders=turkce',
      },
    };
    let aktifKod = 'mat';
    const ornekCiz = (kod) => {
      const o = ORNEKLER[kod];
      if (!o) return;
      aktifKod = kod;
      $$('.m-canli-sekme', canliKart).forEach((b) => b.setAttribute('aria-selected', String(b.dataset.ornek === kod)));
      if (etiketYer && o.etiket) etiketYer.textContent = o.etiket;
      if (gorselYer) gorselYer.innerHTML = o.svg;
      if (soruYer) soruYer.textContent = o.soru;
      if (siklarYer) {
        siklarYer.innerHTML = o.siklar.map((metin, i) =>
          `<button type="button" class="m-canli-sik" data-sec="${i}" ${i === o.dogru ? 'data-dogru="1"' : ''} data-kilit-muaf="1">${metin}</button>`
        ).join('');
      }
      if (donutYer) {
        donutYer.className = 'm-canli-donut';
        donutYer.textContent = 'Bir seçeneğe dokunarak anlık geri bildirimi dene.';
      }
    };
    canliKart.addEventListener('click', (ev) => {
      const sekme = ev.target.closest('.m-canli-sekme');
      if (sekme) { ornekCiz(sekme.dataset.ornek); return; }
      const sik = ev.target.closest('.m-canli-sik');
      if (!sik) return;
      const o = ORNEKLER[aktifKod];
      const secilen = Number(sik.dataset.sec);
      $$('.m-canli-sik', siklarYer).forEach((b) => b.classList.remove('dogru', 'yanlis'));
      if (secilen === o.dogru) {
        sik.classList.add('dogru');
        donutYer.className = 'm-canli-donut dogru';
        donutYer.innerHTML = '';
        donutYer.append(o.aciklama + ' ', el('a', { href: o.bag, sinif: 'm-canli-bag' }, 'Konuya geç →'));
      } else {
        sik.classList.add('yanlis');
        donutYer.className = 'm-canli-donut yanlis';
        donutYer.textContent = o.yanlis;
      }
    });
  }

  const takvimSoz = {};
  const takvim = (n, dersler) => {
    if (!takvimSoz[n]) {
      const adaylar = [...(dersler.siniflar[n] || []), ...(dersler.secmeli?.[n] || [])];
      takvimSoz[n] = (async () => {
        for (const d of adaylar) {
          const a = await veri(`agac/${n}-${d}.json`);
          if (a?.haftalar && Object.keys(a.haftalar).length) return a.haftalar;
        }
        return null;
      })().then((h) => { if (!h) delete takvimSoz[n]; return h; });   // yüklenemediyse sonraki seçimde yeniden denenir
    }
    return takvimSoz[n];
  };

  Promise.all([
    ortakVeri,
    veri('agac/dizin.json'),
    veri('yazili-kagitlari.json'),
    veri('yazili-cikti.json'),
  ]).then(async ([{ dersler, icerikler, iceriklerYuklendi }, dizin, yzKagit, yzCikti]) => {
    if (!dersler || !iceriklerYuklendi) return;   // statik bağlantılar yerinde kalır
    const siniflar = Object.keys(dersler.siniflar).map(Number);
    const ozetler = icerikler.filter((i) => i.tur === 'Konu anlatımı' && i.hafta && i.goruntule);
    const calismalar = icerikler.filter((i) => i.tur === 'Çalışma kâğıdı');
    const calismaHafta = new Set(calismalar.filter((i) => i.hafta).map((i) => `${i.sinif}-${i.ders}-${i.hafta}`));
    const sonKayit = typeof sonBakilan === 'object' ? sonBakilan.oku()[0] : null;
    // İlk ziyarette 8. sınıf varsayılan seçilir; böylece sınıf merkezi ve bu hafta derste bölümü hiçbir zaman boş kalmaz
    let sinif = [sinifOku(), sonKayit?.s, 8].find((n) => siniflar.includes(n)) || siniflar[0] || null;
    let hafta = null, buHaftaNo = null, takvimi = null, bulunan = null;

    // Ders bazında yazılı PDF sayısı (ortak yazılı senaryoları + ülke geneli deneme + öğrenme çıktısı kâğıtları)
    const yaziliSayiBul = (n, d) => {
      const a = `${n}-${d}`;
      const kt = yzKagit?.tablolar?.[a] || {};
      const senSay = Object.values(kt).reduce((t, L) => t + (Array.isArray(L) ? L.length : 0), 0);
      const denSay = Number(yzKagit?.ulke?.[a]?.denemeler || 0);
      const ciktiSay = (yzCikti?.tablolar?.[a] || []).length;
      return senSay + denSay + ciktiSay;
    };

    // Materyal vitrini sayaçlarını canlı veriden güncelle
    const vitrinGuncelle = () => {
      const toplamSenaryo = Object.values(yzKagit?.tablolar || {}).reduce((t, m) => t + Object.values(m).reduce((s, L) => s + (Array.isArray(L) ? L.length : 0), 0), 0);
      const toplamCikti = Object.values(yzCikti?.tablolar || {}).reduce((t, L) => t + (Array.isArray(L) ? L.length : 0), 0);
      const toplamYazili = toplamSenaryo + toplamCikti;
      const planSay = icerikler.filter((i) => i.tur === 'Yıllık plan' || i.tur === 'Ders planı').length;
      const belgeSay = icerikler.filter((i) => i.tur === 'Ders kitabı' || i.tur === 'Öğretim programı' || i.tur === 'Resmî belge').length;
      const yaz = (kod, metin) => {
        const yer = document.querySelector(`[data-vitrin-sayi="${kod}"]`);
        if (yer) yer.textContent = metin;
      };
      const denemeSay = icerikler.filter((i) => i.tur === 'Deneme sınavı').length;
      if (ozetler.length) yaz('ozet', `${ozetler.length.toLocaleString('tr-TR')} haftalık konu özeti · sesli & etkileşimli`);
      if (calismalar.length) yaz('calisma', `${calismalar.length.toLocaleString('tr-TR')} çalışma kâğıdı · cevapsız & cevaplı PDF`);
      if (toplamYazili) yaz('yazili', `${toplamYazili.toLocaleString('tr-TR')} yazılı PDF · senaryo & öğrenme çıktısı`);
      if (planSay) yaz('plan', `${planSay.toLocaleString('tr-TR')}+ yıllık ve günlük plan · Word & PDF`);
      yaz('sinav', denemeSay ? `${denemeSay} ASDS deneme sınavı (5–8. sınıf A/B cevapsız & cevaplı) · LGS & YKS` : '5–8. Sınıf ASDS Deneme Sınavları · LGS & YKS');
      if (belgeSay) yaz('belge', `${belgeSay.toLocaleString('tr-TR')} MEB ders kitabı, öğretim programı & kılavuz`);
    };
    vitrinGuncelle();

    // Kişisel çalışma durumu ve hızlı araç şeridi (#calisma-durum-serit)
    if (merkez && !document.getElementById('calisma-durum-serit')) {
      const diziSay = (anahtar) => { try { const l = JSON.parse(localStorage.getItem(anahtar) || '[]'); return Array.isArray(l) ? l.length : 0; } catch { return 0; } };
      const nesneSay = (anahtar) => { try { const o = JSON.parse(localStorage.getItem(anahtar) || '{}'); return o && typeof o === 'object' ? Object.keys(o).length : 0; } catch { return 0; } };
      const tamamSay = diziSay('dk-tamamlanan-v1');
      const favSay = diziSay('dk-favoriler');
      const ingSay = nesneSay('dk-kelime-ogrenildi');
      const arSay = nesneSay('dk-arapca-ogrenildi-v1');
      const serit = el('div', { sinif: 'calisma-durum-serit', id: 'calisma-durum-serit', role: 'region', 'aria-label': 'Çalışma durumum ve hızlı araçlar' },
        el('span', { sinif: 'cds-etiket' }, 'Hızlı Erişim:'),
        el('a', { sinif: 'cds-hap', 'data-renk': 'yesil', href: `/ogrenci.html?sinif=${sinif || 8}` },
          simge('onay'), el('b', {}, tamamSay ? `${tamamSay} Konu Tamamlandı` : 'İlerleme Takibi')),
        el('a', { sinif: 'cds-hap', 'data-renk': 'sari', href: '/icerikler.html?favori=1' },
          simge('yildiz'), el('b', {}, favSay ? `${favSay} Kayıtlı Materyal` : 'Kayıtlılarım')),
        el('a', { sinif: 'cds-hap', 'data-renk': 'mavi', href: `/kelime.html?s=${sinif || 8}` },
          simge('kartlar'), el('b', {}, ingSay ? `${ingSay} İngilizce Kelime` : 'İngilizce Kelimeler')),
        el('a', { sinif: 'cds-hap', 'data-renk': 'zumrut', href: `/arapca.html?s=${sinif || 8}` },
          simge('kitap'), el('b', {}, arSay ? `${arSay} Arapça Kelime` : 'Arapça Çalışmaları')),
        el('a', { sinif: 'cds-hap', 'data-renk': 'turuncu', href: '/planlar.html?sinif=1' },
          simge('takvim'), el('b', {}, '1–12. Sınıf Günlük Planlar')),
        el('a', { sinif: 'cds-hap', 'data-renk': 'mor', href: '/sinav.html#net-hesaplayici' },
          simge('pusula'), el('b', {}, 'LGS & YKS Net Hesaplayıcı')),
        el('a', { sinif: 'cds-hap cds-hap-ig', 'data-renk': 'pembe', href: 'https://www.instagram.com/derskutusuinfo/', target: '_blank', rel: 'noopener', title: '@derskutusuinfo Instagram hesabını takip et' },
          simge('instagram'), el('b', {}, '@derskutusuinfo')));
      const smBas = merkez.querySelector('.sm-bas');
      if (smBas) smBas.after(serit);
    }

    // ---- Sınıf ve Ders Hızlı Erişim Merkezi (#sinif-merkezi) ----
    const smSekmeler = document.getElementById('sm-sekmeler');
    const smDersler = document.getElementById('sm-dersler');
    const smAciklama = document.getElementById('sm-aciklama');
    const smSinifBag = document.getElementById('sm-sinif-bag');

    if (smSekmeler) {
      smSekmeler.replaceChildren(...siniflar.map((n) => el('button', {
        type: 'button',
        role: 'tab',
        sinif: 'sm-sekme',
        'data-renk': K().gradeColor(n),
        'data-sinif': n,
        'aria-selected': String(n === sinif),
        tabindex: n === sinif ? '0' : '-1',
      }, sinifEtiket(n))));
    }

    const smDersKarti = (n, d, secmeliMi = false) => {
      const ad = dersler.dersler[d] || d;
      const renk = K().subjectColor(d);
      const ag = dizin?.[`${n}-${d}`];
      const dersIc = icerikler.filter((i) => Number(i.sinif) === n && i.ders === d);
      const ozetSay = dersIc.filter((i) => i.tur === 'Konu anlatımı').length;
      const calismaSay = dersIc.filter((i) => i.tur === 'Çalışma kâğıdı').length;
      const yaziliSay = yaziliSayiBul(n, d);
      const dersHref = `/ogrenci.html?sinif=${n}&ders=${encodeURIComponent(d)}`;
      const calismaHref = calismaSay
        ? `/icerikler.html?sinif=${n}&ders=${encodeURIComponent(d)}&tur=${encodeURIComponent('Çalışma kâğıdı')}`
        : dersHref;
      const yaziliHref = yaziliSay ? `${dersHref}#yaziliya-hazirlik` : `/yazili.html?sinif=${n}&ders=${encodeURIComponent(d)}`;
      const planHref = `/planlar.html?sinif=${n}&ders=${encodeURIComponent(d)}`;
      const igHaftalar = [1, 2, 3, 4, 5, 6, 7, 8];
      const igDugme = (n >= 5 && window.dkIgKartAc) ? el('button', {
        type: 'button',
        sinif: 'sm-eylem sm-eylem-ig',
        'data-tur': 'ig',
        title: `@derskutusuinfo ${ad} Instagram konu kartlarını aç`,
        onclick: () => window.dkIgKartAc(n, d, `${n}. Sınıf ${ad} Instagram Konu Kartları`, igHaftalar),
      },
        el('span', { sinif: 'sm-eylem-ad' }, simge('instagram'), el('span', {}, 'Instagram Kartları')),
        el('b', { sinif: 'sm-eylem-sayi' }, '1–8. Hafta →')) : null;

      return el('article', { sinif: `sm-ders-kart${secmeliMi ? ' secmeli' : ''}`, 'data-renk': renk },
        el('a', { sinif: 'sm-ders-ust', href: dersHref },
          el('span', { sinif: 'sm-ders-simge', 'aria-hidden': 'true' }, K().subjectIcon ? K().subjectIcon(d) : simge('kitap')),
          el('span', { sinif: 'sm-ders-baslik' },
            el('strong', {}, ad),
            el('small', {}, ag ? `${ag.unite} ünite · ${ag.konu} konu` : 'Üniteler ve konular')),
          el('span', { sinif: 'sm-ders-ac', 'aria-hidden': 'true' }, 'Üniteler →')),
        el('div', { sinif: 'sm-eylemler', role: 'group', 'aria-label': `${ad} hızlı erişim` },
          el('a', { sinif: 'sm-eylem', 'data-tur': 'ozet', href: dersHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('kitap'), 'Konu Özeti'),
            el('b', { sinif: 'sm-eylem-sayi' }, ozetSay ? `${ozetSay} hafta` : 'Aç')),
          el('a', { sinif: 'sm-eylem', 'data-tur': 'calisma', href: calismaHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('kalem'), 'Çalışma Kâğıdı'),
            el('b', { sinif: 'sm-eylem-sayi' }, calismaSay ? `${calismaSay} PDF` : 'Ünite')),
          el('a', { sinif: 'sm-eylem', 'data-tur': 'yazili', href: yaziliHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('onay'), 'Yazılı Soruları'),
            el('b', { sinif: 'sm-eylem-sayi' }, yaziliSay ? `${yaziliSay} PDF` : 'Senaryo')),
          el('a', { sinif: 'sm-eylem', 'data-tur': 'plan', href: planHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('takvim'), 'Yıllık & Günlük Plan'),
            el('b', { sinif: 'sm-eylem-sayi' }, 'Word · PDF')),
          igDugme));
    };

    const merkezCiz = () => {
      if (!smSekmeler || !smDersler || !sinif) return;
      if (merkez) merkez.dataset.renk = K().gradeColor(sinif);
      if (alan) alan.dataset.renk = K().gradeColor(sinif);
      $$('.sm-sekme', smSekmeler).forEach((b) => {
        const secili = Number(b.dataset.sinif) === sinif;
        b.setAttribute('aria-selected', String(secili));
        b.setAttribute('tabindex', secili ? '0' : '-1');
      });
      const anaDersler = dersler.siniflar[sinif] || [];
      const secmeliDersler = dersler.secmeli?.[sinif] || [];
      if (smAciklama) {
        smAciklama.textContent = `${sinif}. sınıfta ${anaDersler.length} ana ders${secmeliDersler.length ? ` ve ${secmeliDersler.length} seçmeli ders` : ''} · İstediğin dersin konu özetine, çalışma kâğıdına, yazılı sorularına veya planına doğrudan geç.`;
      }
      if (smSinifBag) {
        smSinifBag.href = `/ogrenci.html?sinif=${sinif}`;
        smSinifBag.replaceChildren(`${sinif}. sınıfın bütün dersleri `, simge('ok'));
      }
      const asdsKart = (sinif >= 5 && sinif <= 8) ? (() => {
        const asdsHref = `/sinav.html?sinif=${sinif}#asds-sinif-${sinif}`;
        const asdsSay = icerikler.filter((i) => i.tur === 'Deneme sınavı' && Number(i.sinif) === sinif).length || 8;
        return el('article', { sinif: 'sm-ders-kart', 'data-renk': K().gradeColor(sinif) },
          el('a', { sinif: 'sm-ders-ust', href: asdsHref },
            el('span', { sinif: 'sm-ders-simge', 'aria-hidden': 'true' }, simge('onay')),
            el('span', { sinif: 'sm-ders-baslik' },
              el('strong', {}, `${sinif}. Sınıf ASDS Deneme Sınavları`),
              el('small', {}, `${asdsSay} haftalık sınav · A & B Kitapçığı (Cevapsız ve Cevaplı)`)),
            el('span', { sinif: 'sm-ders-ac', 'aria-hidden': 'true' }, 'Denemeler →')),
          el('div', { sinif: 'sm-eylemler', role: 'group', 'aria-label': `${sinif}. Sınıf ASDS Deneme Sınavları hızlı erişim` },
            el('a', { sinif: 'sm-eylem', 'data-tur': 'ozet', href: asdsHref },
              el('span', { sinif: 'sm-eylem-ad' }, simge('indir'), 'A & B Cevapsız Kitapçık'),
              el('b', { sinif: 'sm-eylem-sayi' }, `${asdsSay * 2} PDF`)),
            el('a', { sinif: 'sm-eylem', 'data-tur': 'calisma', href: asdsHref },
              el('span', { sinif: 'sm-eylem-ad' }, simge('onay'), 'A & B Cevaplı Kitapçık'),
              el('b', { sinif: 'sm-eylem-sayi' }, `${asdsSay * 2} PDF`)),
            el('a', { sinif: 'sm-eylem', 'data-tur': 'yazili', href: asdsHref },
              el('span', { sinif: 'sm-eylem-ad' }, simge('kalem'), 'Cevap Anahtarları (A/B)'),
              el('b', { sinif: 'sm-eylem-sayi' }, `${asdsSay} PDF`)),
            el('a', { sinif: 'sm-eylem', 'data-tur': 'plan', href: `/icerikler.html?sinif=${sinif}&tur=${encodeURIComponent('Deneme sınavı')}` },
              el('span', { sinif: 'sm-eylem-ad' }, simge('kitap'), 'Kütüphanede Gör'),
              el('b', { sinif: 'sm-eylem-sayi' }, 'Tümü'))));
      })() : null;
      smDersler.replaceChildren(
        el('div', { sinif: 'sm-izgara' }, [...anaDersler.map((d) => smDersKarti(sinif, d, false)), asdsKart]),
        secmeliDersler.length ? el('details', { sinif: 'sm-secmeli-kutusu' },
          el('summary', {}, `${sinif}. sınıf seçmeli dersler (${secmeliDersler.length} ders)`),
          el('div', { sinif: 'sm-izgara secmeli' }, secmeliDersler.map((d) => smDersKarti(sinif, d, true)))) : null
      );
    };

    // ---- Bu hafta derste (#bu-hafta) ----
    const secici = document.getElementById('bh-siniflar');
    const tarihYeri = document.getElementById('bh-tarih');
    const onceki = document.getElementById('bh-onceki'), sonraki = document.getElementById('bh-sonraki');
    const baslik = document.getElementById('bu-hafta-baslik');
    const etiketAl = (durum) => (typeof HAFTA_ETIKET === 'object' && HAFTA_ETIKET[durum]) || 'Bu hafta';
    // Dar ekranda sınıf düğmeleri yana kayar: seçili düğme satırın ortasına getirilir (sayfa dikey kaymaz)
    const seciliGoster = (kapsayici, seciciSorgu) => {
      const b = kapsayici?.querySelector(seciciSorgu);
      if (!b || kapsayici.scrollWidth <= kapsayici.clientWidth) return;
      const sr = kapsayici.getBoundingClientRect(), br = b.getBoundingClientRect();
      kapsayici.scrollLeft += (br.left + br.width / 2) - (sr.left + sr.width / 2);
    };
    secici.replaceChildren(...siniflar.map((n) => el('button', { type: 'button', sinif: 'bh-sinif', 'data-renk': K().gradeColor(n), 'data-sinif': n, 'aria-pressed': 'false' },
      `${n}. sınıf`)));

    const kart = (i, n) => {
      const ilerleme = typeof ozetIlerleme === 'function' ? ozetIlerleme(`${n}-${i.ders}-${i.hafta}`) : null;
      const ad = dersler.dersler[i.ders] || i.ders;
      const calismaVar = calismaHafta.has(`${n}-${i.ders}-${i.hafta}`);
      return el('a', { sinif: 'bh-kart', href: yol(i.goruntule), 'data-renk': K().subjectColor(i.ders) },
        el('span', { sinif: 'bh-simge', 'aria-hidden': 'true' }, K().subjectIcon ? K().subjectIcon(i.ders) : simge('kitap')),
        el('span', { sinif: 'bh-govde' },
          el('span', { sinif: 'bh-ust-satir' },
            el('small', {}, ad),
            calismaVar ? el('span', { sinif: 'bh-ek-rozet' }, 'Çalışma kâğıdı') : null),
          el('strong', {}, konuAdi(i.baslik) || i.baslik),
          ilerleme?.tamam ? el('span', { sinif: 'bh-tamam' }, simge('onay'), `Etkinlikler bitti · ${ilerleme.dogru}/${ilerleme.toplam}`)
            : el('span', { sinif: 'bh-git' }, 'Konuyu aç', simge('ok'))));
    };

    // Odaktaki düğme kaldırılır ya da gizlenirse odak bölümde kalır (klavye ve ekran okuyucu yerini kaybetmez)
    const ciz = () => {
      const odak = document.activeElement;
      const icerde = Boolean(odak) && odak !== document.body && alan.contains(odak);
      cizIc();
      if (icerde && (!odak.isConnected || odak.hidden)) ([onceki, sonraki].find((b) => !b.hidden) || baslik)?.focus();
    };
    const cizIc = () => {
      $$('.bh-sinif', secici).forEach((b) => b.setAttribute('aria-pressed', String(Number(b.dataset.sinif) === sinif)));
      seciliGoster(secici, '[aria-pressed="true"]');
      seciliGoster(smSekmeler, '[aria-selected="true"]');
      if (!sinif) {
        tarihYeri.textContent = 'Sınıfını seç; bu haftanın konu anlatımları burada sıralansın.';
        liste.replaceChildren(el('p', { sinif: 'bh-bos' }, 'Yukarıdan sınıfını seç.'));
        onceki.hidden = sonraki.hidden = true;
        return;
      }
      const tumu = el('a', { sinif: 'bh-tumu', href: `/ogrenci.html?sinif=${sinif}` }, `${sinif}. sınıfın bütün dersleri`, simge('ok'));
      if (!takvimi) {   // takvim yüklenemedi: tahminle "bu hafta" denmez
        tarihYeri.replaceChildren(`${sinif}. sınıf · Haftalık takvim şu anda yüklenemedi.`);
        onceki.hidden = sonraki.hidden = true;
        liste.replaceChildren(el('div', { sinif: 'bh-bos' }, el('p', {}, 'Bağlantını denetleyip sınıf düğmesine yeniden bas ya da dersler sayfasından devam et.'), tumu));
        return;
      }
      const h = takvimi[hafta];
      const etiket = hafta === buHaftaNo ? etiketAl(bulunan?.durum) : null;
      const parca = etiket ? [el('b', {}, etiket), ' · '] : [];
      parca.push(`${sinif}. sınıf · ${hafta}. hafta`, h?.ad ? ` · ${h.ad}` : '');
      if (hafta !== buHaftaNo) parca.push(el('button', { type: 'button', sinif: 'bh-donus', onclick: () => { hafta = buHaftaNo; ciz(); } }, 'Bu haftaya dön'));
      tarihYeri.replaceChildren(...parca);
      const numaralar = Object.keys(takvimi || {}).map(Number).sort((a, b) => a - b);
      onceki.hidden = !numaralar.length || hafta <= numaralar[0];
      sonraki.hidden = !numaralar.length || hafta >= numaralar[numaralar.length - 1];
      const buSinif = ozetler.filter((i) => Number(i.sinif) === sinif && Number(i.hafta) === hafta);
      const sira = (lst) => lst.flatMap((d) => buSinif.filter((i) => i.ders === d).slice(0, 1));
      const ana = sira(dersler.siniflar[sinif] || []);
      const secmeli = sira(dersler.secmeli?.[sinif] || []);
      if (!ana.length && !secmeli.length) {
        liste.replaceChildren(el('div', { sinif: 'bh-bos' }, el('p', {}, `${hafta}. haftanın konu anlatımları hazırlanıyor.`), tumu));
        return;
      }
      const igHaftaDugme = (hafta <= 14 && ana.length) ? el('button', {
        type: 'button',
        sinif: 'dugme dk-ig-onizle-btn',
        onclick: () => {
          if (window.dkIgHikayeAc && window.dkSosyalKartYolu) {
            const kartlar = ana.map((i) => ({
              gorsel: window.dkSosyalKartYolu(sinif, i.ders, hafta),
              etiket: `${sinif}. Sınıf ${dersler.dersler[i.ders] || i.ders} · ${hafta}. Hafta: ${konuAdi(i.baslik) || i.baslik} (@derskutusuinfo)`,
            }));
            window.dkIgHikayeAc(`${sinif}. Sınıf · ${hafta}. Hafta IG Ders Kartları`, kartlar, 0);
          } else if (window.dkIgKartAc) {
            window.dkIgKartAc(sinif, ana[0].ders, `${sinif}. Sınıf · ${hafta}. Hafta`, [hafta]);
          }
        },
      }, simge('instagram'), `${sinif}. Sınıf ${hafta}. Hafta Ders Kartları (${ana.length} Ders)`) : null;
      const waHaftaDugme = el('button', {
        type: 'button',
        sinif: 'dugme dk-ig-paylas-btn',
        onclick: (ev) => window.dkSayfaPaylas && window.dkSayfaPaylas(
          ev.currentTarget,
          `${sinif}. Sınıf ${hafta}. Hafta Ders Konu Özetleri, Etkinlikler ve Çalışma Kâğıtları — @derskutusuinfo Instagram sayfasını takip ederek hemen çalış:`
        ),
      }, simge('paylas'), 'Bu Haftayı Paylaş');
      liste.replaceChildren(
        ana.length ? el('div', { sinif: 'bh-kartlar' }, ana.map((i) => kart(i, sinif))) : null,
        secmeli.length ? el('h3', { sinif: 'bh-alt-baslik' }, 'Seçmeli dersler') : null,
        secmeli.length ? el('div', { sinif: 'bh-kartlar kucuk' }, secmeli.map((i) => kart(i, sinif))) : null,
        el('div', { sinif: 'bh-alt' }, igHaftaDugme, waHaftaDugme, tumu));
    };

    const sinifSec = async (n, kaydet) => {
      sinif = n;
      if (kaydet) sinifYaz(n);
      merkezCiz();
      liste.setAttribute('aria-busy', 'true');
      takvimi = await takvim(n, dersler);
      if (sinif !== n) return;   // bu sırada başka sınıf seçildi
      bulunan = takvimi && typeof haftaBul === 'function' ? haftaBul(takvimi) : null;
      buHaftaNo = bulunan?.no ?? (takvimi ? Math.min(...Object.keys(takvimi).map(Number)) : null);
      hafta = buHaftaNo;
      liste.setAttribute('aria-busy', 'false');
      ciz();
    };
    secici.addEventListener('click', (o) => {
      const b = o.target.closest('.bh-sinif');
      if (b) sinifSec(Number(b.dataset.sinif), true);
    });
    if (smSekmeler) {
      smSekmeler.addEventListener('click', (o) => {
        const b = o.target.closest('.sm-sekme');
        if (b) sinifSec(Number(b.dataset.sinif), true);
      });
      smSekmeler.addEventListener('keydown', (o) => {
        if (o.key !== 'ArrowRight' && o.key !== 'ArrowLeft') return;
        const dugmeler = $$('.sm-sekme', smSekmeler);
        const ix = dugmeler.indexOf(document.activeElement);
        if (ix < 0) return;
        o.preventDefault();
        const yeni = dugmeler[(ix + (o.key === 'ArrowRight' ? 1 : dugmeler.length - 1)) % dugmeler.length];
        yeni.focus();
        sinifSec(Number(yeni.dataset.sinif), true);
      });
    }
    const kaydir = (yon) => {
      const numaralar = Object.keys(takvimi || {}).map(Number).sort((a, b) => a - b);
      const j = numaralar.indexOf(hafta) + yon;
      if (j >= 0 && j < numaralar.length) { hafta = numaralar[j]; ciz(); }
    };
    onceki.addEventListener('click', () => kaydir(-1));
    sonraki.addEventListener('click', () => kaydir(1));
    alan.classList.add('hazir');
    if (merkez) merkez.classList.add('hazir');
    if (sinif) await sinifSec(sinif, false); else { merkezCiz(); ciz(); }
  });
})();
