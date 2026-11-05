"""6. sınıf Matematik 14. hafta (Kategorik ve Nicel Veri Dağılımları) görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, ACIK = '#9aa6bd', '#eef1f6', '#475569', '#f8fafc'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def uygula(o):
    s = o['sorular']

    # s[0]: 5 sıralı veri kartı (12, 15, 15, 18, 20)
    ic0 = kutu(6, 6, 348, 103, GRI_A, GRI)
    ic0 += yazi(180, 22, 'Sıralı Nicel Veri Grubu (5 Gözlem)', 9.2, MAVI)
    sayilar = [(12, MAVI, MAVI_A), (15, YES, YES_A), (15, YES, YES_A), (18, TUR, TUR_A), (20, MOR, MOR_A)]
    for i, (val, c, d) in enumerate(sayilar):
        x = 18 + i * 66
        ic0 += kutu(x, 32, 58, 44, d, c)
        ic0 += yazi(x + 29, 60, str(val), 13.0, c)
    ic0 += yazi(180, 96, 'Toplam = 80   ·   En Küçük = 12   ·   En Büyük = 20', 8.3, SOLUK, ince=True)
    s[0]['gorsel'] = svg(ic0, '12, 15, 15, 18, 20 sıralı veri kartları')

    # s[1]: Kök-Yaprak Gösterimi (6|4 8, 7|2 5 5 9, 8|1 4 6)
    ic1 = kutu(6, 5, 348, 105, MAVI_A, MAVI)
    ic1 += yazi(180, 20, 'Kök–Yaprak Gösterimi (Matematik Puanları)', 9.0, MAVI)
    ic1 += kutu(24, 26, 200, 74, ACIK, MAVI, r=4)
    ic1 += f'<line x1="84" y1="28" x2="84" y2="98" stroke="{MAVI}" stroke-width="1.3"/>'
    ic1 += f'<line x1="28" y1="44" x2="220" y2="44" stroke="{MAVI}" stroke-width="1.0"/>'
    ic1 += yazi(54, 39, 'Kök', 8.8, MAVI) + yazi(150, 39, 'Yaprak', 8.8, MAVI)
    sat = [('6', '4   8', 59), ('7', '2   5   5   9', 76), ('8', '1   4   6', 93)]
    for k, yap, yy in sat:
        ic1 += yazi(54, yy, k, 9.5, LAC) + yazi(96, yy, yap, 9.5, LAC, hiza='start')
    ic1 += kutu(234, 38, 110, 50, YES_A, YES, r=5)
    ic1 += yazi(289, 58, 'Anahtar:', 8.5, YES)
    ic1 += yazi(289, 76, '6 | 4 = 64 puan', 8.5, LAC)
    s[1]['gorsel'] = svg(ic1, 'Dokuz öğrencinin puanlarına ait kök-yaprak tablosu')

    # s[2]: 3 Görselleştirme Aracı İkonu (Daire, Nokta, Kök-Yaprak)
    ic2 = kutu(4, 4, 352, 107, GRI_A, GRI)
    araclar = [
        ('Kategorik Oran', 'Daire / Sütun', TUR, TUR_A, 0),
        ('Küçük Kesikli Veri', 'Nokta Grafiği', YES, YES_A, 1),
        ('İki Basamaklı Veri', 'Kök–Yaprak', MOR, MOR_A, 2),
    ]
    for i, (b, alt, c, d, tip) in enumerate(araclar):
        x = 10 + i * 115
        ic2 += kutu(x, 11, 110, 93, d, c)
        ic2 += yazi(x + 55, 27, b, 8.4, c)
        if tip == 0:
            ic2 += f'<circle cx="{x+55}" cy="56" r="16" fill="{ACIK}" stroke="{c}" stroke-width="1.3"/><path d="M{x+55},56 L{x+55},40 A16,16 0 0,1 {x+70},62 Z" fill="{c}"/>'
        elif tip == 1:
            ic2 += f'<line x1="{x+22}" y1="68" x2="{x+88}" y2="68" stroke="{c}" stroke-width="1.2"/>'
            for cx, cy in [(x+34, 61), (x+54, 61), (x+54, 52), (x+74, 61)]:
                ic2 += f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="{c}"/>'
        else:
            ic2 += f'<line x1="{x+46}" y1="40" x2="{x+46}" y2="72" stroke="{c}" stroke-width="1.3"/>'
            ic2 += yazi(x + 36, 53, '7', 8.5, c) + yazi(x + 64, 53, '1  5', 8.5, LAC)
            ic2 += yazi(x + 36, 68, '8', 8.5, c) + yazi(x + 64, 68, '0  4', 8.5, LAC)
        ic2 += yazi(x + 55, 92, alt, 8.2, LAC)
    s[2]['gorsel'] = svg(ic2, 'Daire, nokta ve kök-yaprak görselleştirme araçları')

    # s[5]: Nokta Grafiği: 2(3 nokta), 3(0), 4(2 nokta), 5(1 nokta), 6(1 nokta), 7(1 nokta) -> Toplam=32, N=8
    ic5 = kutu(6, 5, 348, 105, CAM_A, CAM)
    ic5 += yazi(180, 20, 'Aylık Okunan Kitap Sayısı (Nokta Grafiği)', 9.0, CAM)
    ic5 += f'<line x1="36" y1="84" x2="324" y2="84" stroke="{LAC}" stroke-width="1.5"/>'
    frekans = {2: 3, 3: 0, 4: 2, 5: 1, 6: 1, 7: 1}
    for idx, deger in enumerate([2, 3, 4, 5, 6, 7]):
        xp = 60 + idx * 48
        ic5 += f'<line x1="{xp}" y1="81" x2="{xp}" y2="87" stroke="{LAC}" stroke-width="1.2"/>'
        ic5 += yazi(xp, 99, str(deger), 9.0, LAC)
        for k in range(frekans[deger]):
            yp = 73 - k * 14
            ic5 += f'<circle cx="{xp}" cy="{yp}" r="4.8" fill="{KIR if deger == 2 else MAVI}"/>'
    s[5]['gorsel'] = svg(ic5, 'Sekiz öğrencinin okuduğu kitap sayısını gösteren nokta grafiği')

    # s[6]: Uç değer sayı doğrusu / kartları (14, 15, 15, 16 ve uzakta 65)
    ic6 = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic6 += yazi(180, 22, '5 Günlük Çözülen Soru Sayıları ve Uç Değer', 9.0, TUR)
    ic6 += kutu(18, 34, 210, 46, YES_A, YES)
    ic6 += yazi(123, 53, '14  ·  15  ·  15  ·  16', 10.5, LAC)
    ic6 += yazi(123, 71, 'Birbirine yakın küme (Ortanca = 15)', 7.8, YES)
    ic6 += f'<line x1="228" y1="57" x2="258" y2="57" stroke="{KIR}" stroke-width="1.3" stroke-dasharray="4,3"/>'
    ic6 += kutu(258, 34, 80, 46, KIR_A, KIR)
    ic6 += yazi(298, 53, '65', 11.5, KIR)
    ic6 += yazi(298, 71, 'Uç Değer!', 8.0, KIR)
    ic6 += yazi(180, 96, 'Aritmetik Ortalama = 125 ÷ 5 = 25 (Yukarı çekilmiştir)', 8.0, SOLUK, ince=True)
    s[6]['gorsel'] = svg(ic6, 'Uç değer içeren veri grubu şeması')

    # s[7]: İki okçu karşılaştırma kartı (Efe vs Can)
    ic7 = kutu(6, 6, 170, 103, YES_A, YES)
    ic7 += yazi(91, 24, '1. Okçu · EFE', 9.2, YES)
    ic7 += yazi(91, 48, '78,  80,  80,  82', 9.6, LAC)
    ic7 += yazi(91, 70, 'Ortalama = 80 puan', 8.5, YES)
    ic7 += yazi(91, 90, 'Açıklık = 82 - 78 = 4', 8.4, SOLUK)

    ic7 += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic7 += yazi(269, 24, '2. Okçu · CAN', 9.2, TUR)
    ic7 += yazi(269, 48, '65,  75,  85,  95', 9.6, LAC)
    ic7 += yazi(269, 70, 'Ortalama = 80 puan', 8.5, TUR)
    ic7 += yazi(269, 90, 'Açıklık = 95 - 65 = 30', 8.4, SOLUK)
    s[7]['gorsel'] = svg(ic7, 'Efe ve Can puan dağılımları karşılaştırma kartı')

    # s[8]: K, L, M, N dört veri grubu açıklık kartları
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    gruplar = [
        ('K Grubu', 'En küçük: 18', 'En büyük: 24', YES, YES_A),
        ('L Grubu', 'En küçük: 12', 'En büyük: 22', MAVI, MAVI_A),
        ('M Grubu', 'En küçük: 25', 'En büyük: 40', TUR, TUR_A),
        ('N Grubu', 'En küçük: 10', 'En büyük: 32', MOR, MOR_A),
    ]
    for i, (b, ek, eb, c, d) in enumerate(gruplar):
        x = 10 + i * 86
        ic8 += kutu(x, 13, 80, 89, d, c)
        ic8 += yazi(x + 40, 32, b, 8.8, c)
        ic8 += f'<line x1="{x+8}" y1="41" x2="{x+72}" y2="41" stroke="{c}" stroke-width="0.7"/>'
        ic8 += yazi(x + 40, 62, ek, 8.0, LAC, ince=True)
        ic8 += yazi(x + 40, 82, eb, 8.0, LAC)
    s[8]['gorsel'] = svg(ic8, 'Dört veri grubunun en küçük ve en büyük değer kartları')

    # s[9]: Yanıltıcı sütun grafiği (dikey eksen 90'dan başlıyor: A=92, B=96)
    ic9 = kutu(6, 5, 348, 105, KIR_A, KIR)
    ic9 += yazi(180, 20, 'Aylık Satış Adedi (Yanıltıcı Grafik Örneği)', 8.8, KIR)
    ic9 += f'<line x1="70" y1="28" x2="70" y2="90" stroke="{LAC}" stroke-width="1.3"/>'
    ic9 += f'<line x1="70" y1="90" x2="290" y2="90" stroke="{LAC}" stroke-width="1.3"/>'
    ic9 += yazi(52, 92, '90 !', 8.5, KIR) + yazi(52, 72, '92', 8.2, LAC) + yazi(52, 36, '96', 8.2, LAC)
    ic9 += kutu(112, 72, 46, 18, MAVI_A, MAVI, r=2) + yazi(135, 103, 'A (92)', 8.4, MAVI)
    ic9 += kutu(202, 36, 46, 54, TUR_A, TUR, r=2) + yazi(225, 103, 'B (96)', 8.4, TUR)
    s[9]['gorsel'] = svg(ic9, 'Dikey ekseni 90 değerinden başlayan yanıltıcı sütun grafiği')
