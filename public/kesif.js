// Keşif görünümü: mevcut içerik dizini kullanılır; hiçbir içerik veya üretim işi değişmez.
(() => {
  'use strict';
  const categories = [
    ['Konu anlatımı', 'Konu anlatımları', 'Konuyu öğren, slaytla birlikte işle.', 'kitap', 'mor'],
    ['Çalışma kâğıdı', 'Çalışma kâğıtları', 'Pekiştir, çöz ve yazdır.', 'kalem', 'yesil'],
    ['Deneme sınavı', 'Deneme sınavları (ASDS)', 'Cevapsız ve cevaplı A/B kitapçıkları.', 'onay', 'lacivert'],
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
  const SUBJECT_COLOR = {
    'matematik': 'mavi',
    'fen-bilimleri': 'yesil',
    'biyoloji': 'zumrut',
    'fizik': 'mor',
    'kimya': 'turkuaz',
    'turkce': 'kirmizi',
    'turk-dili-ve-edebiyati': 'kirmizi',
    'ingilizce': 'lacivert',
    'arapca': 'sari',
    'mesleki-arapca': 'sari',
    'sosyal-bilgiler': 'turuncu',
    'tc-inkilap-tarihi-ve-ataturkculuk': 'turuncu',
    'tarih': 'turuncu',
    'cografya': 'zumrut',
    'felsefe': 'pembe',
    'din-kulturu-ve-ahlak-bilgisi': 'turkuaz',
    'kuran-i-kerim': 'zumrut',
    'peygamberimizin-hayati': 'yesil',
    'siyer': 'yesil',
    'temel-dini-bilgiler': 'turkuaz',
    'fikih': 'mor',
    'hadis': 'pembe',
    'akaid': 'lacivert',
    'kelam': 'mavi',
    'tefsir': 'turkuaz',
    'dinler-tarihi': 'sari',
    'islam-kultur-ve-medeniyeti': 'turuncu',
    'hitabet-ve-mesleki-uygulama': 'pembe',
  };
  const subjectColor = key => SUBJECT_COLOR[key] || subjectGroups.find(g => g.keys.includes(key))?.color || 'lacivert';
  const gradeColor = grade => colors[((Number(grade) - 5) % colors.length + colors.length) % colors.length];
  // Ders simgeleri (24×24, çizgi): ders kartlarında baş harf yerine; yerel çizim, dışarıdan yükleme yok
  const ICON_PATHS = {
    kitap: 'M3 5.5c3.2-1.2 6.2-.9 9 1.2 2.8-2.1 5.8-2.4 9-1.2v13c-3.2-1.2-6.2-.9-9 1.2-2.8-2.1-5.8-2.4-9-1.2zM12 6.7v13.2M6 9.5h3M6 12.5h3M15 9.5h3M15 12.5h3',
    hesap: 'M7 4.5v6M4 7.5h6M14 7.5h6M5 15l4 4M9 15l-4 4M14 15.5h6M14 18.5h6',
    deney: 'M9 3h6M10 3v6.2L4.6 18.4A1.7 1.7 0 0 0 6.1 21h11.8a1.7 1.7 0 0 0 1.5-2.6L14 9.2V3M7.2 15h9.6',
    atom: 'M12 10.6a1.4 1.4 0 1 0 0 2.8 1.4 1.4 0 0 0 0-2.8zM5.28 5.28A9.5 3.8 45 1 1 18.72 18.72 9.5 3.8 45 1 1 5.28 5.28zM5.28 18.72A9.5 3.8 -45 1 1 18.72 5.28 9.5 3.8 -45 1 1 5.28 18.72zM2.5 12a9.5 3.8 0 1 1 19 0 9.5 3.8 0 1 1-19 0z',
    yaprak: 'M5 19c0-8.5 5-13.8 15-15-1 10-6 15-15 15zM5 19l8.5-8.5M9.5 14.5h4M12 12V8',
    dunya: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3.5 9h17M3.5 15h17M12 3c-2.6 2.6-3.8 5.6-3.8 9s1.2 6.4 3.8 9M12 3c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9',
    insanlar: 'M9 11a3.2 3.2 0 1 0 0-6.4A3.2 3.2 0 0 0 9 11zM3 20a6 6 0 0 1 12 0M16 11a2.7 2.7 0 1 0 0-5.4M17.5 14.2A5.2 5.2 0 0 1 21 19',
    sutun: 'M3 9 12 4l9 5zM5.5 10v8M9.8 10v8M14.2 10v8M18.5 10v8M3 20.5h18',
    bayrak: 'M5 21V3.5M5 4h13l-2.6 4.5L18 13H5',
    ampul: 'M9.5 18h5M10.2 21h3.6M12 3a6 6 0 0 0-3.6 10.8c.7.6 1.1 1.4 1.1 2.2v.2h5V16c0-.8.4-1.6 1.1-2.2A6 6 0 0 0 12 3z',
    konusma: 'M3.5 4.5h11v8h-6l-3.5 3v-3H3.5zM14.5 8.5h6v8h-1.8v3l-3.4-3h-4.8v-4',
    kalem: 'M4 20l1.2-4.6L16 4.6a2.1 2.1 0 0 1 3 3L8.2 18.4zM14.5 6.2l3.2 3.2M4 20l4.2-1.6',
    kalp: 'M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7.3a4.3 4.3 0 0 1 7.5 2.5C19.5 15.4 12 20 12 20z',
    isaret: 'M3.5 5.5c3-1.1 5.8-.8 8.5 1.1 2.7-1.9 5.5-2.2 8.5-1.1v13c-3-1.1-5.8-.8-8.5 1.1-2.7-1.9-5.5-2.2-8.5-1.1zM12 6.6v13M15.5 4.6V10l1.6-1.2 1.6 1.2V5',
    rulo: 'M8 4h10.5A2.5 2.5 0 0 1 21 6.5V7h-4.5M16.5 6.5V17a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3v-.5h10.5V17a3 3 0 0 0 3 3M8 4a2.5 2.5 0 0 0-2.5 2.5v10M9 9h4.5M9 12.5h4.5',
    kandil: 'M12 3.2c1.6 2 2.6 3.2 2.6 4.6a2.6 2.6 0 0 1-5.2 0c0-1.4 1-2.6 2.6-4.6zM5.5 12.5h13l-1.6 5H7.1zM12 17.5V21M8.5 21h7',
    tirnak: 'M4.5 11.5H9V18H4v-4.2c0-3.2 1.1-5.4 4.2-6.6M15 11.5h4.5V18h-5v-4.2c0-3.2 1.1-5.4 4.2-6.6',
    kubbe: 'M3.5 20.5h17M5.5 20.5V13M18.5 20.5V13M4.5 13h15M6 13c0-4.2 3-6.4 6-8 3 1.6 6 3.8 6 8M12 5V2.8M10 20.5v-3a2 2 0 0 1 4 0v3',
    mikrofon: 'M12 3a3 3 0 0 0-3 3v5a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3zM5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21M8.5 21h7',
  };
  const SUBJECT_ICON = {
    'turkce': 'kitap', 'turk-dili-ve-edebiyati': 'kitap', 'matematik': 'hesap', 'fen-bilimleri': 'deney', 'kimya': 'deney',
    'fizik': 'atom', 'biyoloji': 'yaprak', 'cografya': 'dunya', 'sosyal-bilgiler': 'insanlar', 'tarih': 'sutun',
    'tc-inkilap-tarihi-ve-ataturkculuk': 'bayrak', 'felsefe': 'ampul', 'ingilizce': 'konusma', 'arapca': 'kalem', 'mesleki-arapca': 'kalem',
    'din-kulturu-ve-ahlak-bilgisi': 'kalp', 'kuran-i-kerim': 'isaret', 'tefsir': 'isaret', 'peygamberimizin-hayati': 'rulo', 'siyer': 'rulo',
    'temel-dini-bilgiler': 'kandil', 'fikih': 'kandil', 'akaid': 'kandil', 'kelam': 'kandil', 'hadis': 'tirnak',
    'dinler-tarihi': 'sutun', 'islam-kultur-ve-medeniyeti': 'kubbe', 'hitabet-ve-mesleki-uygulama': 'mikrofon',
  };
  const subjectIcon = key => {
    const d = ICON_PATHS[SUBJECT_ICON[key] || 'kitap'];
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 24 24'); svg.setAttribute('aria-hidden', 'true'); svg.setAttribute('class', 'ders-simge');
    const path = document.createElementNS(svg.namespaceURI, 'path');
    for (const [a, v] of Object.entries({ d, fill: 'none', stroke: 'currentColor', 'stroke-width': '1.8', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' })) path.setAttribute(a, v);
    svg.append(path);
    return svg;
  };
  window.Kesif = Object.freeze({ categories, category, subjectColor, gradeColor, subjectIcon });
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
      ['Pekiştir', 'Öğrendiklerini uygula', ['Çalışma kâğıdı', 'Deneme sınavı', 'Kelime çalışması']],
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
