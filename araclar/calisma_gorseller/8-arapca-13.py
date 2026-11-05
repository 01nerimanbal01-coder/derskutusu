"""8. sınıf Arapça 13. hafta görselleri (SVG; K024 insan figürsüz; K178 beyaz bantsız)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
STIL = 'width:100%;max-height:22mm;display:block;margin:1mm auto;'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="{STIL}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    t = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{t}</text>'


def cizgi(x1, y1, x2, y2, renk=GRI, kalin=0.65, kesik=''):
    d = f' stroke-dasharray="{kesik}"' if kesik else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kalin}"{d}/>'


def kart4(baslik, kartlar, etiket, ana=MAVI, arka=GRI_A):
    ic = kutu(4, 4, 352, 107, arka, ana) + yazi(180, 19, baslik, 9.4, ana)
    palet = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, s1, s2) in enumerate(kartlar):
        c, a = palet[i % 4]
        x = 9 + i * 86
        ic += kutu(x, 26, 82, 80, a, c, 5)
        ic += yazi(x + 41, 43, b, 8.2, c)
        ic += cizgi(x + 7, 50, x + 75, 50, c, 0.55)
        ic += yazi(x + 41, 69, s1, 7.6, LAC, ince=True)
        ic += yazi(x + 41, 89, s2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def ikili_pano(baslik, b1, d1a, d1b, b2, d2a, d2b, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1) + yazi(180, 19, baslik, 9.4, c1)
    ic += kutu(10, 26, 165, 80, a1, c1, 5)
    ic += yazi(92.5, 43, b1, 8.6, c1) + cizgi(20, 50, 165, 50, c1, 0.55)
    ic += yazi(92.5, 69, d1a, 7.8, LAC, ince=True) + yazi(92.5, 89, d1b, 7.4, SOLUK, ince=True)
    ic += kutu(185, 26, 165, 80, a2, c2, 5)
    ic += yazi(267.5, 43, b2, 8.6, c2) + cizgi(195, 50, 340, 50, c2, 0.55)
    ic += yazi(267.5, 69, d2a, 7.8, LAC, ince=True) + yazi(267.5, 89, d2b, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_pano(baslik, uclu, etiket, ana=YES, arka=YES_A):
    ic = kutu(4, 4, 352, 107, arka, ana) + yazi(180, 19, baslik, 9.4, ana)
    palet = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, s1, s2) in enumerate(uclu):
        c, a = palet[i % 3]
        x = 10 + i * 114
        ic += kutu(x, 26, 108, 80, a, c, 5)
        ic += yazi(x + 54, 43, b, 8.4, c) + cizgi(x + 8, 50, x + 100, 50, c, 0.55)
        ic += yazi(x + 54, 69, s1, 7.6, LAC, ince=True) + yazi(x + 54, 89, s2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana) + yazi(180, 19, baslik, 9.4, ana)
    palet = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, s1, s2) in enumerate(adimlar):
        c, a = palet[i % 4]
        x = 8 + i * 87
        ic += kutu(x, 26, 79, 80, a, c, 5)
        ic += yazi(x + 39.5, 43, b, 8.0, c)
        ic += yazi(x + 39.5, 68, s1, 7.4, LAC, ince=True)
        ic += yazi(x + 39.5, 88, s2, 7.0, SOLUK, ince=True)
        if i < 3:
            ox = x + 80.5
            ic += f'<polygon points="{ox:.1f},61 {ox+5:.1f},66 {ox:.1f},71" fill="{ana}"/>'
    return svg(ic, etiket)


def g1():
    return uclu_pano('FİİL CÜMLESİ (الْجُمْلَةُ الْفِعْلِيَّةُ) ÖGE ÇÖZÜMLEMESİ', [
        ('1. Fiil (الْفِعْلُ)', 'يُسَاعِدُ', 'Yardım ediyor'),
        ('2. Fail (الْفَاعِلُ)', 'الْغَنِيُّ (Ötreli)', 'Zengin (Özne)'),
        ('3. Mef’ûl (الْمَفْعُولُ بِهِ)', 'الْفَقِيرَ (Üstünlü)', 'Fakire (Nesne)')
    ], 'Arapça fiil cümlesi ögeleri')


def g2():
    return uclu_pano('YARDIMLAŞMA VE CÖMERTLİK SÖZLÜK KARTLARI', [
        ('Zıt Sıfatlar', 'كَرِيمٌ ↔ بَخِيلٌ', 'Eli açık ↔ Eli sıkı'),
        ('Üstün Özveri', 'الْإِيثَارُ', 'Kardeşini kendine tercih'),
        ('Bayram Tebriği', 'عِيدٌ مُبَارَكٌ', 'Bayram kutlama kalıbı')
    ], 'Arapça değerler sözlük kartları', MAVI, MAVI_A)


def g4():
    return ikili_pano('YARDIM TEKLİFİ VE NEZAKET KALIPLARI',
        'Yardım Teklif Sorusu', 'هَلْ تُرِيدُ مُسَاعَدَةً؟', 'Anlamı: Yardım ister misin?',
        'Nezaketli Kabul ve Teşekkür', 'مِنْ فَضْلِكَ · بِكُلِّ سُرُورٍ · شُكْرًا', 'Lütfen · Memnuniyetle · Teşekkürler',
        'Arapça yardım teklifi diyaloğu', CAM, CAM_A, YES, YES_A)


def g5():
    return akis4('DAYANIŞMA DİYALOĞU AKIŞ ADIMLARI', [
        ('1. Selam ve Rica', 'أَرْجُو الْمُسَاعَدَةَ', 'Yardım isteği'),
        ('2. Kabul ve Soru', 'بِكُلِّ سُرُورٍ!', 'Nasıl yardım edeyim?'),
        ('3. Durumu Açıklama', 'الصُّنْدُوقُ ثَقِيلٌ', 'Kutu çok ağır'),
        ('4. Birlikte Taşıma', 'التَّعَاوُنُ جَمِيلٌ', 'Yardımlaşmak güzeldir')
    ], 'Yardımlaşma diyaloğu sıralama kartı')


def g6():
    return ikili_pano('SEBEP VE SONUÇ BAĞLAÇLARI KULLANIMI',
        'Sebep Cümlesi (1. Yargı)', 'أُحِبُّ صَدِيقِي (Arkadaşımı seviyorum)', 'Sevgi burada temel nedendir',
        'Sonuç Cümlesi (2. Yargı)', '___ أُسَاعِدُهُ دَائِمًا (Ona hep yardım ederim)', 'Sonuç bildiren «bu yüzden» bağlacı aranıyor',
        'Sebep sonuç bağlacı tamamlama', MOR, MOR_A, TUR, TUR_A)


def g8():
    return ikili_pano('HİKMET VE SINIF DAYANIŞMASI LEVHASI',
        'Arapça Fiil Cümlesi', 'يَتَعَاوَنُ الطُّلَّابُ فِي الصَّفِّ', 'Cümle başındaki tekil fiil: يَتَعَاوَنُ',
        'Kelime İpuçları', 'الطُّلَّابُ = Öğrenciler (Çoğul fail)', 'فِي الصَّفِّ = Sınıfta (Yer tamlayıcısı)',
        'Sınıfta yardımlaşma fiil cümlesi levhası', YES, YES_A, MAVI, MAVI_A)


def g9():
    return ikili_pano('FİİL CÜMLESİ İLE İSİM CÜMLESİ AYRIMI',
        'Fiil Cümlesi (الْجُمْلَةُ الْفِعْلِيَّةُ)', 'Çekimli bir fiille (يُحِبُّ، يُسَاعِدُ، يُكْرِمُ) başlar', 'Örnek yapı: Fiil + Fail + Mef’ûlün bih',
        'İsim Cümlesi (الْجُمْلَةُ الِاسْمِيَّةُ)', 'Belirli bir isimle (اَلـ... Mübteda) başlar', 'Örnek yapı: Mübteda + Haber',
        'Fiil ve isim cümlesi yapı farkı', MAVI, MAVI_A, KIR, KIR_A)


def g11():
    return uclu_pano('KUR’AN İLKESİ: تَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَى', [
        ('İyilikte Kenetlenme', 'الْبِرِّ (Hayır ve iyilik)', 'Muhtaca el uzatma'),
        ('Takva Bilinci', 'التَّقْوَى (Sorumluluk)', 'Kötülükte birleşmeme'),
        ('Toplumsal Meyvesi', 'التَّضَامُنُ (Dayanışma)', 'Güven ve kardeşlik')
    ], 'İyilik ve takva üzere yardımlaşma panosu', TUR, TUR_A)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[4]['gorsel'] = g4()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[9]['gorsel'] = g9()
    s[11]['gorsel'] = g11()
