"""8. sınıf Fen Bilimleri 13. hafta görselleri (SVG; K024 insan figürsüz; K178 beyaz bantsız)."""
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
    ic = kutu(4, 4, 352, 107, GRI_A, MAVI) + yazi(180, 18, 'TANECİK BOYUTUNDA 1. VE 2. OLAY MODELLERİ', 9.2, MAVI)
    ic += kutu(10, 25, 165, 81, MAVI_A, MAVI, 5)
    ic += yazi(92.5, 39, '1. Olay: Molekül Yapısı Korundu', 8.0, MAVI)
    for cx, cy in [(38, 64), (54, 60), (46, 76)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="{MAVI}"/><circle cx="{cx+7}" cy="{cy}" r="4" fill="{CAM}"/>'
    ic += yazi(92, 68, '→', 11.0, MAVI)
    for cx, cy in [(112, 56), (144, 62), (126, 80)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="{MAVI}"/><circle cx="{cx+7}" cy="{cy}" r="4" fill="{CAM}"/>'
    ic += yazi(92.5, 98, 'Yalnız tanecikler arası mesafe arttı', 7.3, SOLUK, ince=True)
    ic += kutu(185, 25, 165, 81, KIR_A, KIR, 5)
    ic += yazi(267.5, 39, '2. Olay: Eski Bağ Koptu, Yeni Bağ!', 8.0, KIR)
    ic += f'<circle cx="212" cy="66" r="6" fill="{KIR}"/><circle cx="224" cy="66" r="6" fill="{KIR}"/>'
    ic += f'<circle cx="246" cy="66" r="5" fill="{YES}"/><circle cx="256" cy="66" r="5" fill="{YES}"/>'
    ic += yazi(274, 69, '→', 11.0, KIR)
    ic += f'<circle cx="298" cy="60" r="6" fill="{KIR}"/><circle cx="310" cy="60" r="5" fill="{YES}"/>'
    ic += f'<circle cx="298" cy="76" r="6" fill="{KIR}"/><circle cx="310" cy="76" r="5" fill="{YES}"/>'
    ic += yazi(267.5, 98, 'Farklı moleküller (yeni madde) oluştu', 7.3, SOLUK, ince=True)
    return svg(ic, 'Fiziksel ve kimyasal değişim tanecik modelleri')


def g2():
    return uclu_pano('MUTFAKTA MADDENİN GEÇİRDİĞİ DEĞİŞİMLER', [
        ('1. Dilimleme', 'Bıçakla kesme', 'Yalnız boyut küçülür'),
        ('2. Yağda Kızartma', 'Yüksek ısı etkisi', 'Renk, tat ve koku değişir'),
        ('3. Yoğurttan Ayran', 'Su ile karıştırma', 'Karışım / çözünme olayı')
    ], 'Mutfakta fiziksel ve kimyasal değişimler')


def g4():
    return kart4('LABORATUVAR GÖZLEM TÜPLERİ', [
        ('1. Tüp', 'Sirke + Karbonat', 'Gaz çıkışı var'),
        ('2. Tüp', 'İki çözelti karıştı', 'Sarı çökelti oluştu'),
        ('3. Tüp', 'Saf su (100 °C)', 'Buharlaşma (H2O)'),
        ('4. Tüp', 'Magnezyum şerit', 'Isı ve ışık yayıldı')
    ], 'Dört deney tüpünde değişim kanıtları', CAM)


def g5():
    return akis4('BUĞDAYDAN EKMEĞE ÜRETİM BASAMAKLARI', [
        ('1. Öğütme', 'Buğday → Un', 'Tanecik boyutu'),
        ('2. Mayalanma', 'Hamur kabarması', 'Gaz çıkışı (CO2)'),
        ('3. Şekil Verme', 'Hamuru yuvarlama', 'Dış görünüş'),
        ('4. Fırında Pişme', 'Ekmeğin kızarması', 'İç yapı değişimi')
    ], 'Ekmek yapımında fiziksel ve kimyasal adımlar')


def g6():
    return ikili_pano('YANAN MUM DÜZENEĞİNDE İKİ FARKLI DEĞİŞİM',
        'K Olayı: Katı Mumun Erimesi', 'Isı alan katı parafin sıvılaşır', 'Soğuduğunda tekrar katı muma döner',
        'L Olayı: Pamuk Fitilin Yanması', 'Oksijenle tepkimeye girip kararır', 'Karbondioksit, su buharı ve kül oluşur',
        'Mumun erimesi ve fitilin yanması karşılaştırması', CAM, CAM_A, KIR, KIR_A)


def g8():
    return ikili_pano('SÜTTEN ELDE EDİLEN İKİ FARKLI ÜRÜN',
        'Sütten Tereyağı Eldesi', 'Süt yayıkta çalkalanır', 'Yağ tanecikleri fiziksel olarak ayrılır',
        'Sütten Peynir (veya Yoğurt) Eldesi', 'Maya bakterileri sütü dönüştürür', 'Tat, koku ve kimyasal yapı değişir',
        'Sütten tereyağı ve peynir eldesi farkı', TUR, TUR_A, MOR, MOR_A)


def g9():
    return uclu_pano('K, L VE M ELEMENTLERİNİN ÖZELLİK KARTLARI', [
        ('K Elementi', 'Parlaktır, elektriği iletir', 'Tel ve levha olur, paslanır'),
        ('L Elementi (Bor)', 'Görünümü metal gibi', 'Kimyasal özelliği ametal'),
        ('M Elementi (8A)', 'Tek atomlu kararlı gaz', 'Kimyasal tepkimeye girmez')
    ], 'K L M element sınıfları kartları', MAVI, MAVI_A)


def g11():
    return ikili_pano('GÜNLÜK YAŞAMDA İKİ FARKLI OLAY ANALİZİ',
        'Kesilen Elmanın Açık Havada Kararması', 'Havadaki oksijenle tepkime gerçekleşir', 'Renk ve tat değişir (Yavaş yanma)',
        'Düşen Cam Bardağın Kırılması', 'Cam parçaları yine aynı cam maddesidir', 'Yalnızca şekil ve bütünlük değişir',
        'Elmanın kararması ve camın kırılması', YES, YES_A, MAVI, MAVI_A)


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
