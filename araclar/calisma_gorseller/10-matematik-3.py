"""10. sınıf Matematik 3. hafta (Üçgende Yardımcı Elemanlar: Açıortay, Kenarortay, Kenar Orta Dikme ve Yükseklik) çalışma kâğıdı görselleri.
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
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Ağırlık Merkezi (G)', 'Kenarortayların kesişim noktası', MAVI, MAVI_A),
        ('2:1 Kuralı', 'Köşeye 2k, kenara k birim', YES, YES_A),
        ('Muhteşem Üçlü', 'Dik üçgende hipotenüs kenarortayı', TUR, TUR_A),
        ('6 Eşit Alan (6S)', 'G üçgeni 6 eşit alana böler', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Üçgende kenarortay ve ağırlık merkezi özellikleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'ABC ÜÇGENİNDE AĞIRLIK MERKEZİ VE 2:1 ORANI', 11, MAVI)
    # Üçgen geometrisi
    ic += '<polygon points="50,84 130,34 190,84" fill="none" stroke="#2451d6" stroke-width="2"/>'
    # Kenarortay AD
    ic += '<line x1="130" y1="34" x2="120" y2="84" stroke="#ee7d12" stroke-width="1.5"/>'
    # G noktası
    ic += '<circle cx="123" cy="67" r="3" fill="#d63a3a"/>'
    ic += yazi(135, 68, 'G', 9.5, KIR)
    ic += yazi(138, 48, '2k', 8.5, TUR)
    ic += yazi(132, 78, 'k', 8.5, TUR)
    # Sağ bilgi kutusu
    ic += kutu(205, 34, 140, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(275, 52, '|AG| = 2 · |GD|', 11, MAVI)
    ic += yazi(275, 72, 'Köşe mesafesi kenarın iki katıdır', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Üçgende kenarortay üzerinde ağırlık merkezinin 2k ya k oranı şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'DİK ÜÇGENDE MUHTEŞEM ÜÇLÜ KURALI', 11, YES)
    # Dik üçgen
    ic += '<polygon points="50,84 50,34 170,84" fill="none" stroke="#12a150" stroke-width="2"/>'
    ic += '<rect x="50" y="74" width="10" height="10" fill="none" stroke="#12a150" stroke-width="1"/>'
    # Hipotenüs kenarortayı
    ic += '<line x1="50" y1="84" x2="110" y2="59" stroke="#ee7d12" stroke-width="1.8"/>'
    # Sağ açıklama kutusu
    ic += kutu(190, 34, 155, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(267, 52, '|AD| = |BD| = |DC|', 11, YES)
    ic += yazi(267, 72, 'Hipotenüse ait kenarortay parçalara eşittir', 7, LAC, ince=True)
    return svg(360, 100, ic, 'Dik üçgende hipotenüse ait muhteşem üçlü kenarortay bağıntısı', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'KENARORTAYLARIN AYIRDIĞI 6 EŞİT ALAN (6S)', 11, TUR)
    # Üçgen
    ic += '<polygon points="50,84 110,34 170,84" fill="#fff1df" stroke="#ee7d12" stroke-width="2"/>'
    # 3 Kenarortay
    ic += '<line x1="110" y1="34" x2="110" y2="84" stroke="#0b2257" stroke-width="1"/>'
    ic += '<line x1="50" y1="84" x2="140" y2="59" stroke="#0b2257" stroke-width="1"/>'
    ic += '<line x1="170" y1="84" x2="80" y2="59" stroke="#0b2257" stroke-width="1"/>'
    # Sağ bilgi kutusu
    ic += kutu(190, 34, 155, 54, '#ffffff', TUR, 6, 1.2)
    ic += yazi(267, 50, 'Alan(ABC) = 6 · S', 11, TUR)
    ic += yazi(267, 70, '3 kenarortay alanı 6 eşit üçgene böler', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Ağırlık merkezinin üçgeni 6 eşit alana bölme kuralı şeması', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'KENARORTAY UZUNLUK TEOREMİ FORMÜLÜ', 11, MOR)
    ic += kutu(16, 34, 328, 54, '#ffffff', MOR, 6, 1.2)
    ic += yazi(180, 52, '2 · Va² = b² + c² - (a² / 2)', 13, MOR)
    ic += yazi(180, 74, 'Üç kenarın uzunluğu bilinen üçgende kenarortay hesabı', 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kenarortay uzunluk teoremi matematiksel formül kartı', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'DİK ÜÇGENDE KENARORTAYLAR ARASINDAKİ BAĞINTI', 10.5, LAC)
    ic += kutu(16, 34, 328, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(180, 52, '5 · Va² = Vb² + Vc²', 13, MAVI)
    ic += yazi(180, 74, 'm(A) = 90° olan dik üçgende kenarortay kareleri ilişkisi', 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Dik üçgende kenarortaylar arası özel Pisagor bağıntısı', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    elemanlar = [
        ('Kenarortay (V)', 'Kenarı iki eşit parçaya böler, G kesişim'),
        ('Açıortay (n)', 'Açıyı iki eşit parçaya böler, I iç teğet'),
        ('Yükseklik (h)', 'Köşeden karşı kenara inen dikme, H diklik'),
        ('Orta Dikme', 'Kenarın ortasından geçen dik doğru')
    ]
    for i, (b, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Üçgenin yardımcı elemanları ve merkezleri karşılaştırma kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: K - E - N - A - R', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'E'), ('3', 'N'), ('4', 'A'), ('5', 'R')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Geometri dersi şifre anahtar harf kutuları', 34)

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
