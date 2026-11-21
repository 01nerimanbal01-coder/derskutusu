(() => {
  'use strict';

  const form = document.getElementById('hizli-form');
  if (!form) return;

  const sinif = document.getElementById('hb-sinif');
  const ders = document.getElementById('hb-ders');
  const konu = document.getElementById('hb-konu');
  const sonuc = document.getElementById('hb-sonuc');
  const sade = (metin) => metin.toLocaleLowerCase('tr').normalize('NFD')
    .replace(/\p{M}/gu, '').replace(/ı/g, 'i').replace(/[^a-z0-9]+/g, ' ').trim();

  let dersVerisi;
  let kayitlar = [];
  const dersAdi = (kod) => dersVerisi?.dersler?.[kod] || kod;
  const adres = (yol, alanlar) => `${yol}?${new URLSearchParams(alanlar)}`;

  const dersleriGuncelle = () => {
    if (!dersVerisi?.dersler) return;
    const secili = ders.value;
    const siniflar = sinif.value ? [sinif.value] : Object.keys(dersVerisi.siniflar || {});
    const kodlar = new Set(siniflar.flatMap((kod) => [
      ...(dersVerisi.siniflar?.[kod] || []), ...(dersVerisi.secmeli?.[kod] || []),
    ]));
    const secenekler = [...kodlar].filter((kod) => dersVerisi.dersler[kod])
      .sort((a, b) => dersAdi(a).localeCompare(dersAdi(b), 'tr'));
    ders.replaceChildren(new Option('Bütün dersler', ''),
      ...secenekler.map((kod) => new Option(dersAdi(kod), kod)));
    if (secenekler.includes(secili)) ders.value = secili;
  };

  function hedefAdres() {
    const sinifKodu = sinif.value;
    const dersKodu = ders.value;
    const konuMetni = konu.value.trim();
    if (konuMetni) {
      const q = [sinifKodu && `${sinifKodu}. sınıf`, dersKodu && dersAdi(dersKodu), konuMetni]
        .filter(Boolean).join(' ');
      return adres('/ara.html', { q });
    }
    if (sinifKodu) {
      const secimler = { sinif: sinifKodu };
      if (dersKodu) secimler.ders = dersKodu;
      return adres('/ogrenci.html', secimler);
    }
    if (dersKodu) return adres('/icerikler.html', { ders: dersKodu });
    return null;
  }

  function sonucSatiri(href, etiket, yazi) {
    const li = document.createElement('li');
    const a = document.createElement('a');
    const b = document.createElement('b');
    const span = document.createElement('span');
    a.href = href;
    b.textContent = etiket;
    span.textContent = yazi;
    a.append(b, span);
    li.append(a);
    return li;
  }

  function onerileriGoster() {
    const hedef = hedefAdres();
    if (!hedef) {
      sonuc.replaceChildren();
      return;
    }

    const aranan = sade(konu.value);
    const kelimeler = aranan ? aranan.split(' ') : [];
    const eslesen = kayitlar.filter(({ sinifKodu, dersKodu, metin }) =>
      (!sinif.value || sinif.value === sinifKodu) && (!ders.value || ders.value === dersKodu)
      && kelimeler.every((kelime) => metin.includes(kelime))).slice(0, 3);
    const liste = document.createElement('ul');
    eslesen.forEach(({ href, tur, baslik }) => liste.append(sonucSatiri(href, tur, baslik)));
    const ara = Boolean(konu.value.trim());
    liste.append(sonucSatiri(hedef, ara ? 'Ara' : sinif.value ? 'Sınıf' : 'Ders',
      ara ? 'Bütün arama sonuçları' : 'Seçtiğin içerikleri aç'));
    sonuc.replaceChildren(liste);
  }

  sinif.addEventListener('change', () => { dersleriGuncelle(); onerileriGoster(); });
  ders.addEventListener('change', onerileriGoster);
  konu.addEventListener('input', onerileriGoster);
  form.addEventListener('submit', (olay) => {
    olay.preventDefault();
    const hedef = hedefAdres();
    if (hedef) location.assign(hedef);
    else konu.focus();
  });
  document.addEventListener('keydown', (olay) => {
    if (olay.key !== '/' || olay.ctrlKey || olay.metaKey || olay.altKey
      || document.activeElement?.closest('input, textarea, select, [contenteditable="true"]')) return;
    olay.preventDefault();
    konu.focus();
  });

  if (typeof ortakVeri === 'undefined') return;
  ortakVeri.then(({ dersler, icerikler }) => {
    dersVerisi = dersler;
    dersleriGuncelle();
    const sinifKodlari = new Set([...sinif.options].map((secenek) => secenek.value));
    kayitlar = (icerikler || []).flatMap((kayit) => {
      const { baslik, tur, tarih, ders: dersKodu, sinif: sinifNo } = kayit;
      const sinifKodu = String(sinifNo);
      const kaynak = kayit.goruntule || kayit.hazirla || kayit.dosya || kayit.baglanti;
      if (!baslik || !tur || !kaynak || !sinifKodlari.has(sinifKodu)) return [];
      try {
        const url = new URL(kaynak, `${location.origin}/`);
        if (url.origin !== location.origin) return [];
        return [{ href: url.href, baslik, tur, tarih: tarih || '', sinifKodu, dersKodu,
          metin: sade(`${baslik} ${dersAdi(dersKodu)} ${tur}`) }];
      } catch { return []; }
    }).sort((a, b) => b.tarih.localeCompare(a.tarih));
    onerileriGoster();
  }).catch(() => {});
})();
