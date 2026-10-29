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
      if (ozetler.length) yaz('ozet', `${ozetler.length.toLocaleString('tr-TR')} haftalık konu özeti · sesli & etkileşimli`);
      if (calismalar.length) yaz('calisma', `${calismalar.length.toLocaleString('tr-TR')} çalışma kâğıdı · cevapsız & cevaplı PDF`);
      if (toplamYazili) yaz('yazili', `${toplamYazili.toLocaleString('tr-TR')} yazılı PDF · senaryo & öğrenme çıktısı`);
      if (planSay) yaz('plan', `${planSay.toLocaleString('tr-TR')}+ yıllık ve günlük plan · Word & PDF`);
      yaz('sinav', '8. Sınıf LGS · 12. Sınıf YKS hazırlık ve konu dağılımı');
      if (belgeSay) yaz('belge', `${belgeSay.toLocaleString('tr-TR')} MEB ders kitabı, öğretim programı & kılavuz`);
    };
    vitrinGuncelle();

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

      return el('article', { sinif: `sm-ders-kart${secmeliMi ? ' secmeli' : ''}`, 'data-renk': renk },
        el('a', { sinif: 'sm-ders-ust', href: dersHref },
          el('span', { sinif: 'sm-ders-simge', 'aria-hidden': 'true' }, K().subjectIcon ? K().subjectIcon(d) : simge('kitap')),
          el('span', { sinif: 'sm-ders-baslik' },
            el('strong', {}, ad),
            el('small', {}, ag ? `${ag.unite} ünite · ${ag.konu} konu` : 'Üniteler ve konular')),
          el('span', { sinif: 'sm-ders-ac', 'aria-hidden': 'true' }, 'Üniteler →')),
        el('div', { sinif: 'sm-eylemler', role: 'group', 'aria-label': `${ad} hızlı erişim` },
          el('a', { sinif: 'sm-eylem', href: dersHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('kitap'), 'Konu Özeti'),
            el('b', { sinif: 'sm-eylem-sayi' }, ozetSay ? `${ozetSay} hafta` : 'Aç')),
          el('a', { sinif: 'sm-eylem', href: calismaHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('kalem'), 'Çalışma Kâğıdı'),
            el('b', { sinif: 'sm-eylem-sayi' }, calismaSay ? `${calismaSay} PDF` : 'Ünite')),
          el('a', { sinif: 'sm-eylem', href: yaziliHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('onay'), 'Yazılı Soruları'),
            el('b', { sinif: 'sm-eylem-sayi' }, yaziliSay ? `${yaziliSay} PDF` : 'Senaryo')),
          el('a', { sinif: 'sm-eylem', href: planHref },
            el('span', { sinif: 'sm-eylem-ad' }, simge('takvim'), 'Yıllık & Günlük Plan'),
            el('b', { sinif: 'sm-eylem-sayi' }, 'Word/PDF'))));
    };

    const merkezCiz = () => {
      if (!smSekmeler || !smDersler || !sinif) return;
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
      smDersler.replaceChildren(
        el('div', { sinif: 'sm-izgara' }, anaDersler.map((d) => smDersKarti(sinif, d, false))),
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
      liste.replaceChildren(
        ana.length ? el('div', { sinif: 'bh-kartlar' }, ana.map((i) => kart(i, sinif))) : null,
        secmeli.length ? el('h3', { sinif: 'bh-alt-baslik' }, 'Seçmeli dersler') : null,
        secmeli.length ? el('div', { sinif: 'bh-kartlar kucuk' }, secmeli.map((i) => kart(i, sinif))) : null,
        el('div', { sinif: 'bh-alt' }, tumu));
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
