// Belge görüntüleyici: goruntule.html?b=<kimlik>. Belge sitedeyse doğrudan, değilse resmî adresinden çerçeve içinde açılır.
// Kaynak site başka sitede gösterilmeyi engelliyorsa (ör. ÖSYM) açıklama ve "Resmî sitede aç" düğmesi gösterilir.

veri('belgeler.json').then((belgeler) => {
  const id = new URLSearchParams(location.search).get('b');
  let grup = null;
  const b = belgeler?.gruplar.flatMap((g) => g.belgeler.map((x) => ((x.kimlik === id && (grup = g)), x))).find((x) => x.kimlik === id);
  if (!b) {
    $('#g-baslik').textContent = 'Belge bulunamadı';
    $('#g-alan').replaceChildren(el('div', { sinif: 'g-uyari' }, el('p', {}, 'Aradığınız belge listede yok. '), el('a', { sinif: 'dugme ana', href: '/belgeler.html' }, 'Resmî belgelere dön')));
    return;
  }
  document.title = `${b.baslik} · Ders Kutusu`;
  $('#g-baslik').textContent = b.baslik;
  $('#g-bilgi').textContent = [grup?.ad, b.kaynak, b.aciklama].filter(Boolean).join(' · ');
  const resmi = b.kaynak_adres || b.baglanti;
  const dugmeler = [
    b.dosya && el('a', { sinif: 'dugme ana', href: `/${b.dosya}`, download: '' }, simge('indir'), 'İndir'),
    resmi && el('a', { sinif: 'dugme', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî kaynak', simge('ok')),
    b.cerceve && el('button', { sinif: 'dugme', type: 'button', onclick: () => $('#g-alan').requestFullscreen?.() }, simge('buyut'), 'Tam ekran'),
  ];
  $('#g-dugmeler').replaceChildren(...dugmeler.filter(Boolean));
  if (b.cerceve) {
    const kaynak = b.dosya ? `/${b.dosya}` : b.baglanti;
    $('#g-alan').replaceChildren(el('iframe', { src: kaynak, title: b.baslik, loading: 'eager', allow: 'fullscreen' }));
  } else {
    $('#g-alan').replaceChildren(el('div', { sinif: 'g-uyari' },
      el('h2', {}, 'Bu belge yalnız resmî sitesinde açılabiliyor'),
      el('p', {}, `${b.kaynak} kendi sayfalarının başka sitelerde gösterilmesine izin vermiyor. Belge yeni sekmede, resmî adresinde açılır.`),
      el('a', { sinif: 'dugme ana', href: resmi, target: '_blank', rel: 'noopener' }, 'Resmî sitede aç', simge('ok'))));
  }
});
