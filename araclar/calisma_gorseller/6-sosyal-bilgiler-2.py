"""6. sınıf Sosyal Bilgiler 2. hafta (Gelecekteki Rollerimiz, Hak ve Sorumluluklarımızın Değişimi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def gelecek_kartlari_6li():
    kartlar = [
        ('Kart 1 · Eğitim', 'TÜBİTAK proje takımında', 'çalışkan öğrenci', MAVI, MAVI_A),
        ('Kart 2 · Eğitim', 'Başarılı bir üniversite', 'öğrencisi olmak', MAVI, MAVI_A),
        ('Kart 3 · Spor', 'Ülkesini temsil eden', 'disiplinli millî sporcu', TUR, TUR_A),
        ('Kart 4 · Sanat', 'Müzik grubunda enstrüman', 'çalan müzisyen', TUR, TUR_A),
        ('Kart 5 · Toplum', 'Topluma ve çevreye duyarlı', 'STK gönüllüsü / üyesi', YES, YES_A),
        ('Kart 6 · Aile', 'Evlat ve torunlarınca', 'sevilen aile büyüğü', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 3) * 198
        y = 6 + (i // 3) * 56
        ic += kutu(x, y, 190, 50, arka, renk, 8, 1.4)
        ic += kutu(x, y, 190, 18, renk, renk, 8, 1)
        ic += yazi(x + 95, y + 13, bas, 10.2, '#fff')
        ic += yazi(x + 95, y + 31, s1, 10.1, LAC)
        ic += yazi(x + 95, y + 44, s2, 10.1, SOLUK, ince=True)
    return svg(600, 120, ic, 'Altı gelecek kartı: TÜBİTAK öğrencisi, üniversite öğrencisi, millî sporcu, müzisyen, STK üyesi ve aile büyüğü.', 23)


def anneanne_karsilastirma():
    ic = kutu(8, 6, 282, 92, TUR_A, TUR, 9, 1.6)
    ic += kutu(8, 6, 282, 22, TUR, TUR, 9, 1)
    ic += yazi(149, 21, 'GEÇMİŞ (Elif’in Anneannesi)', 10.6, '#fff')
    ic += yazi(20, 44, 'Grup : Köy okulu · Okul korosu', 10.3, LAC, 'start')
    ic += yazi(20, 62, 'Rol : Öğrenci ve koro üyesi', 10.3, LAC, 'start', ince=True)
    ic += yazi(20, 80, 'Hak / Görev : Eğitim alma / Ders çalışma', 10.2, TUR, 'start')

    ic += kutu(310, 6, 282, 92, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(310, 6, 282, 22, MAVI, MAVI, 9, 1)
    ic += yazi(451, 21, 'GÜNÜMÜZ (Elif’in Anneannesi)', 10.6, '#fff')
    ic += yazi(322, 44, 'Grup : Aile ve akraba grubu', 10.3, LAC, 'start')
    ic += yazi(322, 62, 'Rol : Emekli öğretmen ve anneanne', 10.3, LAC, 'start', ince=True)
    ic += yazi(322, 80, 'Hak / Görev : Saygı görme / Rehberlik etme', 10.2, MAVI, 'start')
    return svg(600, 104, ic, 'Elif’in anneannesinin geçmiş ve günümüz grup, rol, hak ve sorumluluk karşılaştırması.', 22)


def dede_soylesi_notlari():
    notlar = [
        ('1. Çocukluk Dönemi', 'Okul grubunda öğrenci · Eğitim hakkı ve ders sorumluluğu', MAVI, MAVI_A),
        ('2. Gençlik Dönemi', 'Fabrikada işçi · Ücret hakkı ve zamanında üretim sorumluluğu', TUR, TUR_A),
        ('3. Günümüz (Aile)', 'Aile grubunda dede · Saygı görme hakkı ve torunlara rehberlik', MOR, MOR_A),
        ('4. Günümüz (Toplum)', 'Çevre derneğinde gönüllü · Söz hakkı ve ağaçlandırma görevi', YES, YES_A),
    ]
    ic = ''
    for i, (bas, m, renk, arka) in enumerate(notlar):
        y = 6 + i * 27
        ic += kutu(8, y, 584, 23, arka, renk, 6, 1.4)
        ic += kutu(8, y, 152, 23, renk, renk, 6, 1)
        ic += yazi(84, y + 15.5, bas, 10.3, '#fff')
        ic += yazi(170, y + 15.5, m, 10.2, LAC, 'start', ince=True)
    return svg(600, 116, ic, 'Kerem’in dedesiyle yaptığı söyleşi notları: çocukluk, gençlik ve günümüzdeki iki rolü.', 22)


def aile_rol_haberi():
    ic = kutu(8, 6, 584, 90, KUM, GRI, 9, 1.6)
    ic += kutu(8, 6, 584, 24, LAC, LAC, 9, 1)
    ic += yazi(300, 22, 'HABER METNİ · AİLEDE ROL PAYLAŞIMI VE HUZUR', 10.8, '#fff')
    ic += yazi(24, 46, 'Tiyatro Benzetmesi (Prof. Dr. Nevzat Tarhan): Tiyatro sahnesindeki sanatçılar gibi', 10.3, LAC, 'start')
    ic += yazi(24, 64, '  ailede de anne, baba ve çocukların rolleri ayrıdır; herkes rolünün gereğini yapar.', 10.3, LAC, 'start', ince=True)
    ic += yazi(24, 82, 'Çözüm Anahtarı: Ailede sevgi ve şefkat yaşatıldığında sorunlar kendiliğinden düzelir.', 10.3, MOR, 'start')
    return svg(600, 102, ic, 'Ailede rol paylaşımı, tiyatro sanatçısı benzetmesi ve sevgi-şefkat vurgusu.', 22)


def etkinlik_akisi_4adim():
    adimlar = [
        ('1. Hayal Et', 'Meslek ve rol belirle', MAVI, MAVI_A),
        ('2. Tablo Doldur', 'Grup, rol, hak, görev', TUR, TUR_A),
        ('3. Kartona Çiz', 'Ortak tabloyu panoya as', MOR, MOR_A),
        ('4. İncele & Not As', 'Yapışkan notla bildir', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 76, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 136, 24, renk, renk, 9, 1)
        ic += yazi(x + 68, 24, bas, 10.5, '#fff')
        ic += yazi(x + 68, 56, alt, 10.1, LAC, ince=True)
    return svg(600, 92, ic, 'Gelecekte dâhil olacağım gruplar ve rollerim etkinliğinin 4 basamağı.', 22)


def pano_inceleme_sorulari():
    ic = kutu(8, 6, 584, 90, YES_A, YES, 9, 1.6)
    ic += kutu(8, 6, 584, 24, YES, YES, 9, 1)
    ic += yazi(300, 22, 'SINIF PANOSUNDAKİ ORTAK TABLOLARI İNCELEME SORULARI', 10.6, '#fff')
    ic += yazi(24, 46, '1. Soru : Öğrenciler gelecekte hangi gruplara dâhil olmayı hayal etmiş?', 10.3, LAC, 'start')
    ic += yazi(24, 64, '2. Soru : Panoda benim daha önce tahmin etmediğim farklı roller var mı?', 10.3, LAC, 'start')
    ic += yazi(24, 82, '3. Soru : Hak ve sorumluluklarda hangi benzerlik ve farklılıklar bulunuyor?', 10.3, YES, 'start')
    return svg(600, 102, ic, 'Sınıf panosundaki ortak tabloları incelerken cevap aranan üç soru.', 22)


def tarih_seridi_taslagi():
    donemler = [
        ('İlkokul (Geçmiş)', 'Grup: İlkokul · Rol: Öğrenci', 'Hak ve Görev: (Yazılmamış!)', MAVI, MAVI_A),
        ('Ortaokul (Bugün)', 'Grup: 6. Sınıf · Rol: Başkan', 'Hak ve Görev: (Yazılmamış!)', TUR, TUR_A),
        ('Yetişkinlik (Gelecek)', 'Grup: Hastane · Rol: Hekim', 'Hak ve Görev: (Yazılmamış!)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(donemler):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 82, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 22, renk, renk, 9, 1)
        ic += yazi(x + 94, 23, bas, 10.4, '#fff')
        ic += yazi(x + 94, 48, s1, 10.2, LAC)
        ic += yazi(x + 94, 72, s2, 10, KIR, ince=True)
    return svg(600, 98, ic, 'Can’ın hazırladığı tarih şeridi taslağı: grup ve rol yazılmış ancak hak ve sorumluluklar eksik bırakılmış.', 22)


def rol_gecis_semasi():
    kutular = [
        ('Bugünkü Rolüm', 'Okul Basketbol Takımı', 'Düzenli antrenman ve uyum', MAVI, MAVI_A),
        ('Yakın Gelecek', 'Gençlik Spor Kulübü', 'Müsabaka deneyimi kazanma', TUR, TUR_A),
        ('Uzak Gelecek', 'Millî Sporcu / Antrenör', 'Ülkeyi temsil ve liderlik', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 80, arka, renk, 9, 1.6)
        ic += yazi(x + 94, 26, bas, 10.8, renk)
        ic += yazi(x + 94, 48, s1, 10.5, LAC)
        ic += yazi(x + 94, 68, s2, 10.1, SOLUK, ince=True)
    return svg(600, 96, ic, 'Okul takımındaki öğrencinin gelecekte millî sporcu ve antrenör rolüne geçiş şeması.', 22)


def degerlendirme_raporu_karti():
    ic = kutu(8, 6, 584, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 6, 584, 24, MOR, MOR, 9, 1)
    ic += yazi(300, 22, 'KONU SONU DEĞERLENDİRME RAPORU FORMU', 10.8, '#fff')
    ic += yazi(24, 48, 'İncelenen Konu : Dâhil olduğumuz grupların ve rollerimizin zaman içindeki değişimi', 10.3, LAC, 'start')
    ic += yazi(24, 70, 'Genel Sonuç Cümlem : ……………………………………………………………………………………', 10.3, MOR, 'start', ince=True)
    return svg(600, 96, ic, 'Konu sonu değerlendirme raporu formu.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gelecek_kartlari_6li()
    s[4]['gorsel'] = anneanne_karsilastirma()
    s[5]['gorsel'] = dede_soylesi_notlari()
    s[6]['gorsel'] = aile_rol_haberi()
    s[7]['gorsel'] = etkinlik_akisi_4adim()
    s[8]['gorsel'] = pano_inceleme_sorulari()
    s[9]['gorsel'] = tarih_seridi_taslagi()
    s[10]['gorsel'] = rol_gecis_semasi()
    s[12]['gorsel'] = degerlendirme_raporu_karti()
