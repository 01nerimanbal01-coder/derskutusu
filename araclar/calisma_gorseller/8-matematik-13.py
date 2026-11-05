"""8. sınıf Matematik 13. hafta görselleri (SVG; K024 insan figürsüz; K178 beyaz bantsız; K155 dikey kesir)."""
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
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 19, 'ÖZDEŞ HARF KARTLARI DENEYİ (TOPLAM 9 KART)', 9.2, MAVI)
    harfler = [('M', MAVI), ('A', YES), ('T', TUR), ('E', MOR), ('M', MAVI), ('A', YES), ('T', TUR), ('İ', CAM), ('K', KIR)]
    for i, (h, c) in enumerate(harfler):
        x = 12 + i * 38
        ic += kutu(x, 28, 32, 42, GRI_A, c, 4) + yazi(x + 16, 54, h, 11.0, c)
    ic += yazi(180, 92, 'Sıklık: M (2) · A (2) · T (2) · E (1) · İ (1) · K (1)', 8.2, LAC)
    return svg(ic, 'MATEMATİK kelimesi özdeş harf kartları')


def g2():
    return uclu_pano('HİLESİZ ZAR ATMA DENEYİ: ÖRNEK UZAY = {1, 2, 3, 4, 5, 6}', [
        ('6 Eş Çıktı', '1 · 2 · 3 · 4 · 5 · 6', 'Her bir yüz eş şanslı'),
        ('Asal Çıktılar', '2, 3 ve 5 yüzleri', '6 durumdan 3 tanesi'),
        ('Uç Durumlar', '7 gelmesi: Yok (0)', '7’den küçük: Tümü (6)')
    ], 'Hilesiz zar atma deneyi örnek uzayı')


def g4():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 19, 'RENKLİ TOP TORBASI (TOPLAM 12 ÖZDEŞ TOP)', 9.2, CAM)
    gruplar = [
        (14, '4 Kırmızı Top', KIR, KIR_A, 4),
        (130, '5 Mavi Top', MAVI, MAVI_A, 5),
        (246, '3 Sarı Top', TUR, TUR_A, 3)
    ]
    for x, bas, c, a, adet in gruplar:
        ic += kutu(x, 28, 100, 76, a, c, 5) + yazi(x + 50, 44, bas, 8.2, c)
        for k in range(adet):
            cx = x + 18 + k * 16
            ic += f'<circle cx="{cx}" cy="68" r="6" fill="{c}"/>'
        ic += yazi(x + 50, 94, f'Çıktı sayısı: {adet}', 7.4, LAC, ince=True)
    return svg(ic, '12 toplu torbada mavi olmama olasılığı')


def g5():
    return kart4('OLASILIK CETVELİ: 0 (İMKÂNSIZ) İLE 1 (KESİN) ARASI', [
        ('Rakamdan 2 Bas.', '0 ile 9 arası', 'İmkânsız (0)'),
        ('Zarda 6 Gelmesi', '6’da 1 durum', 'Düşük olasılık'),
        ('Parada Tura', '2’de 1 durum', 'Yarı şans (%50)'),
        ('{2,4,6,8} Çift', '4’te 4 durum', 'Kesin olay (1)')
    ], 'Olasılık değerlerini 0 ile 1 arasında sıralama')


def g6():
    return uclu_pano('8-B SINIFI ÖĞRENCİ DAĞILIM TABLOSU (TOPLAM 30 ÖĞRENCİ)', [
        ('Kız Öğrenciler', 'Gözlüklü: 6 kişi', 'Gözlüksüz: 10 kişi'),
        ('Erkek Öğrenciler', 'Gözlüklü: 5 kişi', 'Gözlüksüz: 9 kişi'),
        ('Sınıf Toplamı', '16 Kız + 14 Erkek', 'Örnek Uzay = 30')
    ], '8-B sınıfı gözlüklü kız ve erkek öğrenci tablosu', MOR, MOR_A)


def g8():
    return ikili_pano('1’DEN 20’YE KADAR NUMARALI ÖZDEŞ KARTLAR',
        'Tüm Olası Durumlar (Örnek Uzay)', '1, 2, 3, ..., 19, 20 numaralı kartlar', 'Toplam Kart Sayısı = 20 adet',
        'İstenen Olay: Tam Kare Sayı Olması', '1×1 = 1  ·  2×2 = 4  ·  3×3 = 9  ·  4×4 = 16', '5×5 = 25 > 20 (Aralık dışında kalır!)',
        '1-20 arası kartlardan tam kare çekme olasılığı', YES, YES_A, MAVI, MAVI_A)


def g9():
    ic = kutu(4, 4, 352, 107, TUR_A, TUR) + yazi(180, 19, 'TEKNOLOJİ KULÜBÜ DAİRE GRAFİĞİ (360° TAM DAİRE)', 9.2, TUR)
    ic += f'<circle cx="70" cy="66" r="34" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="0.75"/>'
    ic += f'<path d="M70,66 L70,32 A34,34 0 0,1 99.4,83 Z" fill="{YES_A}" stroke="{YES}" stroke-width="0.75"/>'
    ic += yazi(84, 58, '120°', 8.0, YES) + yazi(52, 74, '240°', 8.0, MAVI)
    ic += kutu(126, 28, 218, 76, GRI_A, TUR, 5)
    ic += yazi(235, 46, 'Yazılım Dilimi: 150°  ·  Tasarım Dilimi: 90°', 8.0, LAC)
    ic += yazi(235, 66, 'Robotik Dilimi Merkez Açısı = 360° - 240° = 120°', 8.0, YES)
    ic += yazi(235, 86, 'İpucu: Olasılık = Robotik Açısı ÷ 360°', 7.6, SOLUK, ince=True)
    return svg(ic, 'Daire grafiğinde 120 derecelik Robotik dilimi olasılığı')


def g11():
    return ikili_pano('BEYAZ VE SİYAH TOP KUTUSU (TÜMLEYEN OLASILIK)',
        'Bilinen Veri: Beyaz Toplar', 'Kutuda 6 adet beyaz top vardır', 'Beyaz + Siyah Olasılık Toplamı = 1 (Tam)',
        'Verilen Olasılık: Siyah Çekilme Oranı', '5 eş paydan 2’si siyah, 3’ü beyazdır', '3 pay = 6 beyaz top üzerinden hesaplayınız',
        'Tümleyen olasılık ile bilinmeyen siyah top sayısı', MAVI, MAVI_A, MOR, MOR_A)


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
