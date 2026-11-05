"""7. sınıf Matematik 13. hafta görselleri (SVG; K024 insan figürsüz; K178 beyaz bantsız)."""
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
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI)
    ic += yazi(180, 20, 'GÜNLÜK OKUNAN SAYFA SAYISI NOKTA GRAFİĞİ (7 ÖĞRENCİ)', 9.2, MAVI)
    ic += cizgi(28, 82, 332, 82, LAC, 0.75)
    for xv, lbl in [(45, '20'), (85, '25'), (125, '30'), (205, '50'), (285, '75'), (320, '90')]:
        ic += cizgi(xv, 79, xv, 85, LAC, 0.75) + yazi(xv, 97, lbl, 8.0, LAC)
    noktalar = [(45, 70, MAVI), (45, 58, MAVI), (85, 70, YES), (85, 58, YES), (85, 46, YES), (125, 70, MAVI), (320, 70, KIR)]
    for nx, ny, c in noktalar:
        ic += f'<circle cx="{nx}" cy="{ny}" r="4.5" fill="{c}"/>'
    ic += yazi(85, 34, 'Yığılma Bölgesi (20–30)', 7.8, YES)
    ic += yazi(295, 52, 'Aykırı Nokta: 90!', 8.0, KIR)
    return svg(ic, 'Günlük okunan sayfa sayısı nokta grafiği ve uç değer')


def g2():
    return uclu_pano('SPOR KULÜBÜ BRANŞ DAĞILIMI (TOPLAM 120 ÖĞRENCİ)', [
        ('Yüzme: 30 Öğrenci', '120’de 30 (Çeyrek)', 'Merkez Açı: 90°'),
        ('Basketbol: 60 Öğrenci', '120’de 60 (Yarım)', 'Merkez Açı: 180°'),
        ('Okçuluk: 24 Öğrenci', '120’de 24 (Beşte bir)', 'Merkez Açı: 72°')
    ], 'Spor kulübü branş sayıları ve merkez açıları')


def g4():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM)
    ic += yazi(180, 19, '5 GÜNLÜK ÖĞLE SICAKLIĞI ÇİZGİ GRAFİĞİ (°C)', 9.2, CAM)
    ic += cizgi(40, 90, 330, 90, LAC, 0.7) + cizgi(40, 28, 40, 90, LAC, 0.7)
    pts = [(65, 68, 'Pzt', '18°'), (125, 44, 'Sal', '24°'), (185, 76, 'Çar', '16°'), (245, 36, 'Per', '28°'), (305, 84, 'Cum', '14°')]
    poly = ' '.join(f'{x},{y}' for x, y, _, _ in pts)
    ic += f'<polyline points="{poly}" fill="none" stroke="{MAVI}" stroke-width="0.75"/>'
    for x, y, g, v in pts:
        ic += f'<circle cx="{x}" cy="{y}" r="3.6" fill="{KIR}"/>'
        ic += yazi(x, y - 6, v, 7.8, LAC) + yazi(x, 103, g, 7.8, SOLUK, ince=True)
    return svg(ic, 'Beş günlük öğle sıcaklığı çizgi grafiği')


def g5():
    return akis4('ORTALAMA MUTLAK SAPMA (OMS) HESAPLAMA ZİNCİRİ', [
        ('1. Ortalama', 'Verileri topla', 'Veri sayısına böl'),
        ('2. Uzaklıklar', '|Veri - Ortalama|', 'Pozitif farkları bul'),
        ('3. Fark Toplamı', 'Tüm mutlak', 'uzaklıkları topla'),
        ('4. OMS Değeri', 'Toplam uzaklığı', 'veri sayısına böl')
    ], 'Ortalama mutlak sapma adımları')


def g6():
    return ikili_pano('OKÇULUK ATIŞ PUANLARI KARŞILAŞTIRMASI (5 ATIŞ)',
        'Kaan’ın Puanları: 8, 9, 10, 11, 12', 'Aritmetik Ortalama = 10 puan', 'Uzaklıklar: 2, 1, 0, 1, 2 (Toplam = 6)',
        'Mert’in Puanları: 5, 7, 10, 13, 15', 'Aritmetik Ortalama = 10 puan', 'Uzaklıklar: 5, 3, 0, 3, 5 (Toplam = 16)',
        'Kaan ve Mert okçuluk puanları karşılaştırması', YES, YES_A, TUR, TUR_A)


def g8():
    return uclu_pano('7-A SINIFI BOY UZUNLUĞU GRUPLANDIRILMIŞ SIKLIK TABLOSU', [
        ('140–149 cm Aralığı', 'Sıklık (Frekans): 7', '150 cm altı grup'),
        ('150–159 cm Aralığı', 'Sıklık (Frekans): 11', 'Orta boy grubu'),
        ('160–169 cm Aralığı', 'Sıklık (Frekans): 6', 'En uzun boy grubu')
    ], 'Boy uzunluğu gruplandırılmış sıklık tablosu', MAVI, MAVI_A)


def g9():
    ic = kutu(4, 4, 352, 107, MOR_A, MOR)
    ic += yazi(180, 19, 'SINIF KİTAPLIĞI DAİRE GRAFİĞİ (TOPLAM 180 KİTAP)', 9.2, MOR)
    ic += f'<circle cx="72" cy="66" r="34" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="0.75"/>'
    ic += f'<path d="M72,66 L72,32 A34,34 0 0,1 106,66 Z" fill="{YES_A}" stroke="{YES}" stroke-width="0.75"/>'
    ic += cizgi(72, 66, 38, 66, MOR, 0.7) + yazi(85, 55, '90°', 7.8, YES) + yazi(58, 82, '150°', 7.8, MAVI)
    ic += kutu(130, 30, 214, 72, GRI_A, MOR, 5)
    ic += yazi(237, 48, 'Roman: 150°  ·  Şiir ve Öykü: 120°', 8.2, LAC)
    ic += yazi(237, 68, 'Bilim Kitapları Merkez Açısı = 360° - 270° = 90°', 8.0, YES)
    ic += yazi(237, 88, 'Toplam Kitap = 180 adet (360° tam daire)', 7.6, SOLUK, ince=True)
    return svg(ic, '180 kitaplık daire grafiğinde bilim kitapları merkez açısı')


def g11():
    return ikili_pano('6 ÇALIŞANIN AYLIK MAAŞ DAĞILIMI (BİN TL)',
        '5 Çalışanın Maaşları', '22 · 24 · 25 · 25 · 26 bin TL', 'Birbirine çok yakın dengeli veriler',
        '6. Çalışan (Üst Yönetici)', '128 bin TL (Aşırı Uç Değer!)', 'Ortalamayı yukarı çeken aykırı veri',
        'Maaş verisinde uç değer etkisi', MAVI, MAVI_A, KIR, KIR_A)


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
