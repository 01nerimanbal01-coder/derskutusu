// Resmî belgeler sayfası: veri/belgeler.json gruplarını listeler (bağlantılar resmî kaynaklara gider).

function belgeKarti(b, dersler) {
  const dersAd = b.ders && dersler?.dersler[b.ders];
  return el('article', { sinif: 'kart' },
    el('div', { sinif: 'ust-bilgi' },
      el('span', { sinif: 'etiket' }, b.kaynak),
      b.kademe && el('span', { sinif: 'etiket tur' }, b.kademe),
      b.sinif && el('span', { sinif: 'etiket tur' }, `${b.sinif}. sınıf`),
      el('span', { sinif: `etiket ${b.kitle === 'ogretmen' ? 'ogretmen' : 'tur'}` }, b.kitle === 'ogretmen' ? 'Öğretmen' : 'Öğrenci ve veli')),
    el('h3', {}, b.baslik),
    b.aciklama && el('p', {}, b.aciklama),
    dersAd && !b.baslik.startsWith(dersAd) && el('p', { sinif: 'kucuk' }, dersAd),
    el('div', { sinif: 'eylemler' },
      b.goruntule && el('a', { sinif: 'ac', href: `/${b.goruntule}` }, 'Aç', simge('ok')),
      b.goruntule && /^kitap-/.test(b.kimlik || '') && !b.dosya && el('a', { sinif: 'ac', href: `/${b.goruntule}&yerel=1`, title: 'Kitabın bilgisayarınızdaki PDF dosyasını açar; internet beklenmez' }, 'Bilgisayardan aç'),
      b.dosya && el('a', { sinif: 'ac', href: `/${b.dosya}`, download: '' }, 'İndir', simge('indir')),
      !b.goruntule && !b.dosya && el('a', { sinif: 'ac', href: b.baglanti, target: '_blank', rel: 'noopener' }, 'Aç', simge('ok'))));
}

Promise.all([veri('belgeler.json'), ortakVeri]).then(([belgeler, { dersler }]) => {
  if (!belgeler) {
    // Liste gelmedi (ağ hatası): boş sayfa yerine açık hata; süzgeç çalışmayacağından kapalı
    $('#belge-gruplari').replaceChildren(el('div', { sinif: 'kap' }, el('div', { role: 'alert', sinif: 'bos' },
      el('p', {}, 'Belge listesi yüklenemedi. Bağlantınızı kontrol edip yeniden deneyin.'),
      el('button', { type: 'button', sinif: 'dugme', onclick: () => location.reload() }, 'Yeniden dene'))));
    $('#grup-gecis')?.setAttribute('hidden', '');
    for (const e of document.querySelectorAll('.belge-suzgec input, .belge-suzgec select')) e.disabled = true;
    return;
  }
  const kayit = [];   // süzgeç için: belge + kartı
  $('#grup-gecis').replaceChildren(...belgeler.gruplar.map((g) => el('a', { href: `#${g.kimlik}` }, g.ad)));
  $('#belge-gruplari').replaceChildren(...belgeler.gruplar.map((g, s) =>
    el('section', { sinif: `bolum${s % 2 ? ' koyu-zemin' : ''}`, id: g.kimlik },
      el('div', { sinif: 'kap' },
        el('div', { sinif: 'bolum-bas' },
          el('div', {}, el('p', { sinif: 'ust-baslik' }, `${g.belgeler.length} belge`), el('h2', {}, g.ad), g.aciklama && el('p', {}, g.aciklama))),
        el('div', { sinif: 'kartlar' }, g.belgeler.map((b) => { const k = belgeKarti(b, dersler); kayit.push({ b, k }); return k; }))))));
  if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();

  // Süzgeç (kullanıcı ihtiyacı: 120 belge tek sayfada): ara, sınıf, kitle; ?sinif=&kitle=&q= ile de açılır
  const form = $('.belge-suzgec');
  if (!form) return;
  const duz = (s) => String(s || '').toLocaleLowerCase('tr').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i');
  const ara = $('#b-ara'), sinifSec = $('#b-sinif'), kitleSec = $('#b-kitle'), sonuc = $('#b-sonuc');
  sinifSec.append(...[...new Set(kayit.map((x) => x.b.sinif).filter(Boolean))].sort((a, b) => a - b).map((n) => el('option', { value: String(n) }, `${n}. sınıf`)));
  const p = new URLSearchParams(location.search);
  if (p.get('q')) ara.value = p.get('q');
  if (p.get('sinif')) sinifSec.value = p.get('sinif');
  if (p.get('kitle')) kitleSec.value = p.get('kitle');
  const suz = () => {
    const q = duz(ara.value).split(/\s+/).filter(Boolean), sinif = sinifSec.value, kitle = kitleSec.value;
    let gorunen = 0;
    for (const x of kayit) {
      const m = duz([x.b.baslik, x.b.aciklama, x.b.kaynak, x.b.kademe, dersler?.dersler[x.b.ders], x.b.sinif && `${x.b.sinif}. sınıf`].filter(Boolean).join(' '));
      const uyar = q.every((s) => m.includes(s)) && (!sinif || String(x.b.sinif) === sinif) && (!kitle || x.b.kitle === kitle);
      x.k.hidden = !uyar; if (uyar) gorunen++;
    }
    for (const sec of $$('#belge-gruplari > section')) sec.hidden = !sec.querySelector('.kart:not([hidden])');
    const aktif = q.length || sinif || kitle;
    sonuc.textContent = aktif ? (gorunen ? `${gorunen} belge bulundu` : 'Eşleşen belge yok. Aramayı kısaltın ya da süzgeçleri kaldırın.') : '';
    $('#grup-gecis').hidden = Boolean(aktif);   // grup bağlantıları gizlenen bölümlere götürmesin
  };
  form.addEventListener('submit', (o) => o.preventDefault());
  ara.addEventListener('input', suz); sinifSec.addEventListener('change', suz); kitleSec.addEventListener('change', suz);
  if (ara.value || sinifSec.value || kitleSec.value) suz();
});
