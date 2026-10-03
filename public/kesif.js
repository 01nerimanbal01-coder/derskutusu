// Keşif görünümü: mevcut içerik dizini kullanılır; hiçbir içerik veya üretim işi değişmez.
(() => {
  'use strict';
  const categories = [
    ['Konu anlatımı', 'Konu anlatımları', 'Konuyu öğren, slaytla birlikte işle.', 'kitap', 'mor'],
    ['Çalışma kâğıdı', 'Çalışma kâğıtları', 'Pekiştir, çöz ve yazdır.', 'kalem', 'yesil'],
    ['Ders planı', 'Günlük planlar', 'Dersine hazırlan; Word veya PDF al.', 'takvim', 'turuncu'],
    ['Yıllık plan', 'Yıllık planlar', 'Öğretim yılını hafta hafta planla.', 'takvim', 'mavi'],
    ['Yazılı senaryosu', 'Yazılı senaryoları', 'Konu ve soru dağılımını incele.', 'onay', 'pembe'],
    ['Ders kitabı', 'Ders kitapları', 'Dersinin kaynak kitabına ulaş.', 'kitap', 'sari'],
    ['Öğretim programı', 'Öğretim programları', 'Öğrenme çıktılarını takip et.', 'onay', 'yesil'],
    ['Kelime çalışması', 'Kelime çalışmaları', 'Dinle, tekrar et ve alıştırma yap.', 'ses', 'mor'],
  ].map(([type, title, description, icon, color]) => ({ type, title, description, icon, color }));
  const category = type => categories.find(c => c.type === type) || { color: 'mavi', icon: 'kitap' };
  window.Kesif = Object.freeze({ categories, category });
  const query = values => '/icerikler.html?' + new URLSearchParams(Object.entries(values).filter(([, v]) => v));
  function home({ dersler, icerikler }) {
    const grid = document.getElementById('kesif-kategoriler');
    if (!grid) return;
    if (!dersler || !icerikler.length) {
      grid.replaceChildren(el('p', {}, 'Kaynaklar şu anda yüklenemedi. ', el('a', { href: '/icerikler.html' }, 'Kütüphaneyi aç')));
      return;
    }
    grid.replaceChildren(...categories.map(c => {
      const count = icerikler.filter(i => i.tur === c.type).length;
      return el('a', { href: query({ tur: c.type }), sinif: 'kesif-kategori', 'data-renk': c.color },
        el('span', { sinif: 'kesif-ikon' }, simge(c.icon)), el('span', { sinif: 'kesif-adet' }, `${count} kaynak`),
        el('h3', {}, c.title), el('p', {}, c.description), el('span', { sinif: 'kesif-git', 'aria-hidden': 'true' }, '↗'));
    }));
    document.querySelector('[data-kesif-sayi="kaynak"]').textContent = icerikler.length;
    document.querySelector('[data-kesif-sayi="konu"]').textContent = icerikler.filter(i => i.tur === 'Konu anlatımı').length;
    const form = document.getElementById('hizli-bul');
    const grade = form.elements.sinif, subject = form.elements.ders, type = form.elements.tur;
    grade.append(...Object.keys(dersler.siniflar).map(n => el('option', { value: n }, `${n}. sınıf`)));
    const subjects = () => {
      const previous = subject.value;
      const keys = grade.value ? [...dersler.siniflar[grade.value], ...(dersler.secmeli?.[grade.value] || [])] : Object.keys(dersler.dersler);
      subject.replaceChildren(el('option', { value: '' }, 'Bütün dersler'), ...keys.map(k => el('option', { value: k }, dersler.dersler[k])));
      if (keys.includes(previous)) subject.value = previous;
    };
    subjects(); grade.addEventListener('change', subjects);
    type.append(...categories.map(c => el('option', { value: c.type }, c.title)));
    form.addEventListener('submit', event => { event.preventDefault(); location.href = query({ sinif: grade.value, ders: subject.value, tur: type.value }); });
  }
  ortakVeri.then(home);
})();
