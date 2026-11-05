"""10. sınıf Biyoloji 3. hafta (Fotosentez Reaksiyonlarının İşleyiş Modeli ve Fotosentez Hızını Etkileyen Faktörler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'KLOROPLAST ORGANELİNİN ŞEMATİK YAPISI', 11, YES)
    # Kloroplast dış elips
    ic += '<ellipse cx="80" cy="58" rx="60" ry="28" fill="#c8e6c9" stroke="#12a150" stroke-width="1.6"/>'
    ic += '<ellipse cx="80" cy="58" rx="54" ry="24" fill="#a5d6a7" stroke="#12a150" stroke-width="1"/>'
    # Grana diskleri
    for dy in [-10, 0, 10]:
        ic += f'<rect x="62" y="{56 + dy}" width="36" height="5" rx="2" fill="#2e7d32"/>'
    # Bilgi kutuları sağda
    kartlar = [
        ('Çift Katlı Zar', 'Dış ve iç seçici geçirgen zar', 156),
        ('Stroma Sıvısı', 'DNA, RNA, ribozom ve enzimler', 222),
        ('Granum / Tilakoit', 'Klorofiller ve ETS elemanları', 288)
    ]
    for b, d, x in kartlar:
        ic += kutu(x, 32, 60, 56, '#ffffff', YES, 5, 1)
        ic += yazi(x + 30, 48, b, 8, YES)
        ic += yazi(x + 30, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kloroplast organelinin iç yapısı ve tilakoit zarlar şeması', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'AĞIR OKSİJEN İZOTOPU (¹⁸O) İLE FOTOSENTEZ DENEYİ', 11, MAVI)
    # Deney 1: Normal CO2 + Ağır Oksijenli Su
    ic += kutu(16, 34, 158, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(95, 50, 'CO₂ + H₂¹⁸O -> Glikoz + ¹⁸O₂↑', 9.5, LAC)
    ic += yazi(95, 72, 'Çıkan O₂ sudan gelir (Kanıtlandı)', 8.5, MAVI, ince=True)
    # Deney 2: Ağır CO2 + Normal Su
    ic += kutu(186, 34, 158, 54, '#ffffff', TUR, 6, 1.2)
    ic += yazi(265, 50, 'C¹⁸O₂ + H₂O -> Glikoz(¹⁸O) + O₂↑', 9.5, LAC)
    ic += yazi(265, 72, 'CO₂ oksijeni glikoza gider', 8.5, TUR, ince=True)
    return svg(360, 100, ic, 'Fotosentezde açığa çıkan oksijenin kaynağını belirleyen izotop deneyi', 34)

def g2():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'ENGELMANN SPEKTRUM DENEYİ VE AEROBİK BAKTERİLER', 11, LAC)
    # Prizma spektrumu şeridi
    renkler = [('#7c3aed', 'Mor', 40), ('#2451d6', 'Mavi', 35), ('#12a150', 'Yeşil', 8), ('#f2b705', 'Sarı', 12), ('#ee7d12', 'Turuncu', 20), ('#d63a3a', 'Kırmızı', 38)]
    for i, (hex_c, ad, b_sayi) in enumerate(renkler):
        x = 16 + i * 56
        ic += f'<rect x="{x}" y="34" width="52" height="18" fill="{hex_c}" rx="3"/>'
        ic += yazi(x + 26, 47, ad, 8.5, '#ffffff')
        # Bakteri yoğunluğu noktaları
        ic += yazi(x + 26, 68, f'Bakteri: {b_sayi}', 8, LAC, ince=True)
        ic += yazi(x + 26, 82, 'Çok' if b_sayi > 30 else ('Az' if b_sayi < 15 else 'Orta'), 8, hex_c)
    return svg(360, 100, ic, 'Engelmann deneyi ışık dalga boyu ve aerobik bakteri kümelenmesi', 34)

def g3():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    pigmentler = [
        ('Klorofil a', 'Mavi-yeşil renk, fotosentezin ana reaksiyon merkezi', YES, '#ffffff'),
        ('Klorofil b', 'Sarı-yeşil renk, ışığı soğurup klorofil a\'ya aktarır', '#2e7d32', '#ffffff'),
        ('Karotenoid', 'Turuncu-sarı pigmentler, aşırı ışıktan korur', TUR, '#ffffff'),
        ('Antosiyanin', 'Kırmızı-mor renk, vakuolde bulunur, fotosentez yapmaz', MOR, '#ffffff')
    ]
    for i, (b, d, c, a) in enumerate(pigmentler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Fotosentetik pigmentler ve görevleri karşılaştırma kartı', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'FOTOSENTEZİN İKİ TEMEL EVRESİ', 11, MOR)
    # Evre 1: Işığa Bağımlı
    ic += kutu(16, 34, 156, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(94, 50, 'Işığa Bağımlı Reaksiyonlar', 9, MAVI)
    ic += yazi(94, 68, 'Tilakoit zarda: H₂O -> O₂ + ATP + NADPH', 7.5, LAC, ince=True)
    ic += yazi(180, 62, '->', 14, MOR)
    # Evre 2: Işıktan Bağımsız
    ic += kutu(188, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(266, 50, 'Calvin Döngüsü (Stroma)', 9, YES)
    ic += yazi(266, 68, 'CO₂ + ATP + NADPH -> Glikoz', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Fotosentezin ışığa bağımlı ve Calvin döngüsü evreleri akış modeli', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'KLOROFİLİN IŞIK ABSORPSİYON (SOĞURMA) EĞRİSİ', 11, LAC)
    # Eksenler
    ic += '<line x1="40" y1="84" x2="330" y2="84" stroke="#9aa6bd" stroke-width="1.2"/>'
    ic += '<line x1="40" y1="84" x2="40" y2="34" stroke="#9aa6bd" stroke-width="1.2"/>'
    # Dalga boyu çizgisi ve tepe noktaları
    ic += '<path d="M 45 42 Q 85 80 160 82 T 260 80 Q 300 44 325 42" fill="none" stroke="#12a150" stroke-width="2.5"/>'
    ic += yazi(65, 36, 'Mor-Mavi (Tepe)', 8, '#7c3aed')
    ic += yazi(180, 76, 'Yeşil (Çukur)', 8, '#12a150')
    ic += yazi(305, 36, 'Kırmızı (Tepe)', 8, '#d63a3a')
    ic += yazi(185, 94, 'Dalga Boyu (400 nm - 700 nm)', 8, SOLUK, ince=True)
    return svg(360, 100, ic, 'Klorofilin dalga boyuna göre ışık soğurma grafiği', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    terimler = [
        ('Tilakoit', 'Klorofil taşıyan yassı zar kesecikleri'),
        ('Stroma', 'Calvin döngüsünün gerçekleştiği sıvı'),
        ('Granum', 'Tilakoitlerin üst üste dizili kuleleri'),
        ('Foton', 'Işık enerjisinin kuantum paketçikleri')
    ]
    for i, (b, d) in enumerate(terimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Fotosentez hücresel yapıları kavram kartları', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: E - N - G - E - L', 11.5, YES)
    harfler = [('1', 'E'), ('2', 'N'), ('3', 'G'), ('4', 'E'), ('5', 'L')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Biyoloji dersi şifre anahtar harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
