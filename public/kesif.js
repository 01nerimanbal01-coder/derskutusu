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
    ['Öğretim programı', 'Öğretim programları', 'Öğrenme çıktılarını takip et.', 'onay', 'turkuaz'],
    ['Kelime çalışması', 'Kelime çalışmaları', 'Dinle, tekrar et ve alıştırma yap.', 'ses', 'lacivert'],
  ].map(([type, title, description, icon, color]) => ({ type, title, description, icon, color }));
  const category = type => categories.find(c => c.type === type) || { color: 'mavi', icon: 'kitap' };
  const colors = ['mor', 'yesil', 'turuncu', 'mavi', 'pembe', 'sari', 'turkuaz', 'lacivert'];
  const subjectGroups = [
    { title: 'Matematik ve fen', color: 'mavi', keys: ['matematik', 'fen-bilimleri', 'fizik', 'kimya', 'biyoloji'] },
    { title: 'Dil ve edebiyat', color: 'pembe', keys: ['turkce', 'turk-dili-ve-edebiyati', 'ingilizce', 'arapca', 'mesleki-arapca'] },
    { title: 'Sosyal bilimler', color: 'turuncu', keys: ['sosyal-bilgiler', 'tc-inkilap-tarihi-ve-ataturkculuk', 'tarih', 'cografya', 'felsefe'] },
    { title: 'Din kültürü ve meslek dersleri', color: 'turkuaz', keys: ['din-kulturu-ve-ahlak-bilgisi', 'kuran-i-kerim', 'peygamberimizin-hayati', 'temel-dini-bilgiler', 'fikih', 'hadis', 'siyer', 'akaid', 'tefsir', 'dinler-tarihi', 'hitabet-ve-mesleki-uygulama', 'kelam', 'islam-kultur-ve-medeniyeti'] },
  ];
  const subjectColor = key => subjectGroups.find(g => g.keys.includes(key))?.color || 'lacivert';
  const gradeColor = grade => colors[((Number(grade) - 5) % colors.length + colors.length) % colors.length];
  window.Kesif = Object.freeze({ categories, category, subjectColor, gradeColor });
  const query = values => '/icerikler.html?' + new URLSearchParams(Object.entries(values).filter(([, v]) => v));
  function home({ dersler, icerikler, iceriklerYuklendi }) {
    const grid = document.getElementById('kesif-kategoriler');
    if (!grid) return;
    const subjectsGrid = document.getElementById('kesif-dersler');
    if (!dersler || iceriklerYuklendi === false) {
      grid.replaceChildren(el('p', { role: 'alert' }, 'Kaynaklar şu anda yüklenemedi. ', el('a', { href: '/icerikler.html' }, 'Kütüphaneyi aç')));
      subjectsGrid?.replaceChildren(el('p', {}, 'Ders listesi şu anda yüklenemedi. ', el('a', { href: '/icerikler.html' }, 'Kütüphaneyi aç')));
      return;
    }
    const card = c => {
      const count = icerikler.filter(i => i.tur === c.type).length;
      return el('a', { href: query({ tur: c.type }), sinif: 'kesif-kategori', 'data-renk': c.color },
        el('span', { sinif: 'kesif-ikon' }, simge(c.icon)), el('span', { sinif: 'kesif-adet' }, `${count} kaynak`),
        el('h4', {}, c.title), el('p', {}, c.description), el('span', { sinif: 'kesif-git', 'aria-hidden': 'true' }, '↗'));
    };
    const groups = [
      ['Öğren', 'Konuya ilk adım', ['Konu anlatımı', 'Ders kitabı']],
      ['Pekiştir', 'Öğrendiklerini uygula', ['Çalışma kâğıdı', 'Kelime çalışması']],
      ['Derse hazırlan', 'Planla, takip et, değerlendir', ['Ders planı', 'Yıllık plan', 'Yazılı senaryosu', 'Öğretim programı']],
    ];
    grid.replaceChildren(...groups.map(([title, description, types]) =>
      el('section', { sinif: 'kesif-kategori-grup', 'aria-label': title },
        el('div', { sinif: 'kesif-grup-bas' }, el('h3', {}, title), el('p', {}, description)),
        el('div', { sinif: 'kesif-grup-kartlar' }, types.map(type => card(category(type)))))));
    if (subjectsGrid) {
      const known = new Set(subjectGroups.flatMap(g => g.keys));
      const extra = Object.keys(dersler.dersler).filter(key => !known.has(key));
      const groups = [...subjectGroups, { title: 'Diğer dersler', color: 'lacivert', keys: extra }];
      subjectsGrid.replaceChildren(...groups.filter(g => g.keys.some(key => dersler.dersler[key])).map(g => {
        const keys = g.keys.filter(key => dersler.dersler[key]);
        const count = icerikler.filter(i => keys.includes(i.ders)).length;
        return el('section', { sinif: 'kesif-ders-grup', 'data-renk': g.color },
          el('div', { sinif: 'kesif-grup-bas' }, el('h3', {}, g.title), el('p', {}, `${keys.length} ders · ${count} kaynak`)),
          el('ul', { sinif: 'kesif-ders-baglari' }, keys.map(key => {
            const count = icerikler.filter(i => i.ders === key).length;
            return el('li', {}, el('a', { href: query({ ders: key }) },
              el('span', {}, dersler.dersler[key]), el('small', {}, count ? `${count} kaynak` : 'Henüz kaynak yok')));
          })));
      }));
    }
    document.querySelector('[data-kesif-sayi="kaynak"]').textContent = icerikler.length;
    document.querySelector('[data-kesif-sayi="konu"]').textContent = icerikler.filter(i => i.tur === 'Konu anlatımı').length;
    const grades = document.querySelector('[data-kesif-sayi="sinif"]');
    if (grades) grades.textContent = Object.keys(dersler.siniflar).length;
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
