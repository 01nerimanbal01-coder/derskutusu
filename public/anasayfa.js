// Ana sayfa: "Kaldığın yerden devam et" ve "Bu hafta derste" (kullanıcı 25.10.2026: eksikleri tamamla, tasarımı güzelleştir).
// Hafta, sınıfın yıllık plan takviminden (veri/agac/<sınıf>-<ders>.json "haftalar") bulunur; konu anlatımları içerik dizininden.
// Seçilen sınıf ve son bakılan konular yalnız bu tarayıcıda tutulur (localStorage); dışarıdan hiçbir şey yüklenmez.
(() => {
  'use strict';
  const alan = document.getElementById('bu-hafta');
  const liste = document.getElementById('bh-liste');
  if (!alan || !liste) return;
  const K = () => window.Kesif || { subjectColor: () => 'mavi', gradeColor: () => 'mavi' };
  const SINIF_ANAHTAR = 'dk-sinif';
  const sinifOku = () => { try { return Number(localStorage.getItem(SINIF_ANAHTAR)) || null; } catch { return null; } };
  const sinifYaz = (n) => { try { localStorage.setItem(SINIF_ANAHTAR, String(n)); } catch {} };
  const yol = (a) => (/^(https?:)?\//.test(a) ? a : `/${a}`);
  // "8. Sınıf Matematik 7. Hafta: Konu (M.8.1.3.7)" → "Konu"
  const konuAdi = (b) => String(b || '').replace(/^\d+\.\s*Sınıf\s.*?\d+\.\s*Hafta:\s*/i, '').replace(/\s*\((?:[A-ZÇĞİÖŞÜ]{1,4}\.?\s?\d[^()]*|[^()]*\d\.\d[^()]*)\)\s*$/, '').trim();

  // Kaldığın yerden devam et (ortak.js): yalnız daha önce konu açılmışsa görünür
  const devam = typeof sonBakilan === 'object' ? sonBakilan.bolum() : null;
  if (devam) alan.before(devam);

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

  ortakVeri.then(async ({ dersler, icerikler, iceriklerYuklendi }) => {
    if (!dersler || !iceriklerYuklendi) return;   // statik bağlantılar yerinde kalır
    const siniflar = Object.keys(dersler.siniflar).map(Number);
    const ozetler = icerikler.filter((i) => i.tur === 'Konu anlatımı' && i.hafta && i.goruntule);
    const sonKayit = typeof sonBakilan === 'object' ? sonBakilan.oku()[0] : null;
    let sinif = [sinifOku(), sonKayit?.s].find((n) => siniflar.includes(n)) || null;
    let hafta = null, buHaftaNo = null, takvimi = null, bulunan = null;

    const secici = document.getElementById('bh-siniflar');
    const tarihYeri = document.getElementById('bh-tarih');
    const onceki = document.getElementById('bh-onceki'), sonraki = document.getElementById('bh-sonraki');
    const baslik = document.getElementById('bu-hafta-baslik');
    const etiketAl = (durum) => (typeof HAFTA_ETIKET === 'object' && HAFTA_ETIKET[durum]) || 'Bu hafta';
    // Dar ekranda sınıf düğmeleri yana kayar: seçili düğme satırın ortasına getirilir (sayfa dikey kaymaz)
    const seciliGoster = () => {
      const b = secici.querySelector('[aria-pressed="true"]');
      if (!b || secici.scrollWidth <= secici.clientWidth) return;
      const sr = secici.getBoundingClientRect(), br = b.getBoundingClientRect();
      secici.scrollLeft += (br.left + br.width / 2) - (sr.left + sr.width / 2);
    };
    secici.replaceChildren(...siniflar.map((n) => el('button', { type: 'button', sinif: 'bh-sinif', 'data-renk': K().gradeColor(n), 'data-sinif': n, 'aria-pressed': 'false' },
      `${n}. sınıf`)));

    const kart = (i, n) => {
      const ilerleme = typeof ozetIlerleme === 'function' ? ozetIlerleme(`${n}-${i.ders}-${i.hafta}`) : null;
      const ad = dersler.dersler[i.ders] || i.ders;
      return el('a', { sinif: 'bh-kart', href: yol(i.goruntule), 'data-renk': K().subjectColor(i.ders) },
        el('span', { sinif: 'bh-simge', 'aria-hidden': 'true' }, K().subjectIcon ? K().subjectIcon(i.ders) : simge('kitap')),
        el('span', { sinif: 'bh-govde' },
          el('small', {}, ad),
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
      seciliGoster();
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
    const kaydir = (yon) => {
      const numaralar = Object.keys(takvimi || {}).map(Number).sort((a, b) => a - b);
      const j = numaralar.indexOf(hafta) + yon;
      if (j >= 0 && j < numaralar.length) { hafta = numaralar[j]; ciz(); }
    };
    onceki.addEventListener('click', () => kaydir(-1));
    sonraki.addEventListener('click', () => kaydir(1));
    alan.classList.add('hazir');
    if (sinif) await sinifSec(sinif, false); else ciz();
  });
})();
