// Keşif renk/simge eşlemesi (window.Kesif): kategori, ders grubu ve sınıf renkleri; agac.js, kutuphane.js ve kartlar kullanır.
// (Ana sayfadaki keşif ızgarası 11.10.2026'da kaldırıldı; onu çizen home() de kaldırıldı.)
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
})();
