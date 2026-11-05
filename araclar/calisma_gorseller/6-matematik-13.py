"""6. sınıf Matematik 13. hafta (Uzunluk Ölçme Problemleri ve İstatistiksel Veri Dağılımları) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18.5" font-weight="700"'


def svg(ic, etiket, w=360, h=115, mm=20):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def ikili_kart(b1, s1a, s1b, r1, z1, b2, s2a, s2b, r2, z2, etiket, ar1=False, ar2=False):
    ic = kutu(6, 6, 170, 103, z1, r1)
    ic += yazi(91, 28, b1, r1, kalin=True)
    ic += (ar_yazi(91, 60, s1a, LAC) if ar1 else yazi(91, 58, s1a, LAC, kalin=True))
    ic += yazi(91, 90, s1b, r1)
    ic += kutu(184, 6, 170, 103, z2, r2)
    ic += yazi(269, 28, b2, r2, kalin=True)
    ic += (ar_yazi(269, 60, s2a, LAC) if ar2 else yazi(269, 58, s2a, LAC, kalin=True))
    ic += yazi(269, 90, s2b, r2)
    return svg(ic, etiket)


def dortlu_kart(kartlar, etiket, ar=False):
    konum = [(6, 6), (184, 6), (6, 60), (184, 60)]
    ic = ''
    for (x, y), (b1, b2, r, z) in zip(konum, kartlar):
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 18, b1, r, kalin=True)
        ic += (ar_yazi(x + 85, y + 41, b2, LAC) if ar else yazi(x + 85, y + 39, b2, LAC))
    return svg(ic, etiket)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dortlu_kart([
        ('1. Etap: 2,4 km', '2,4 × 1000 = 2400 m', MAVI, MAVI_A),
        ('2. Etap: 850 m', 'Doğrudan metre: 850 m', YES, YES_A),
        ('3. Etap: 15 000 cm', '15 000 ÷ 100 = 150 m', TUR, TUR_A),
        ('Toplam Parkur (m)', '2400 + 850 + 150 = ? m', MOR, MOR_A),
    ], 'Üç etaplı yürüyüş parkurunda uzunluk birimlerini metreye çevirme.')
    s[2]['gorsel'] = ikili_kart(
        'Kategorik (Nitel) Veri', 'Spor dalı · Meyve · Göz rengi', 'Araç: Sıklık Tablosu / Sütun Grafiği', MOR, MOR_A,
        'Nicel (Kesikli) Veri', 'Okunan kitap · Sınav puanı · Kardeş', 'Araç: Nokta Grafiği / Kök-Yaprak', YES, YES_A,
        'Kategorik ve nicel kesikli verilerin özellikleri ve grafik araçları.'
    )
    s[5]['gorsel'] = dortlu_kart([
        ('1. Başkent Neresidir?', 'Tek sabit cevap → Araştırma değil', KIR, KIR_A),
        ('2. 1 km Kaç Metredir?', 'Sabit kural (1000 m) → Değil', TUR, TUR_A),
        ('3. 6. Sınıfların Soru Sayısı?', 'Hedef kitle + Değişebilirlik (✓)', YES, YES_A),
        ('4. Öğretmenin Memleketi?', 'Tek kişilik bilgi → Araştırma değil', MAVI, MAVI_A),
    ], 'İstatistiksel araştırma sorusu ölçütlerinin incelenmesi.')
    s[6]['gorsel'] = ikili_kart(
        'Kök-Yaprak Gösterimi (7 Veri)', 'Kök 1 | Yaprak: 2  5  5  → (12, 15, 15)', 'Kök 2 | Yaprak: 0  4  8  9 → (20, 24, 28, 29)', MAVI, MAVI_A,
        'Özetleme İpuçları', 'Tepe Değer (Mod): En çok tekrar eden', 'Açıklık: En büyük (29) − En küçük (12)', YES, YES_A,
        'Kök-yaprak gösteriminden tepe değer ve açıklık hesaplama.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Başlangıç Çıta Uzunluğu', '3 m 60 cm = 300 + 60 = 360 cm', 'Ortak birim: Santimetre (cm)', CAM, CAM_A,
        'Kesilen Parçalar', '1. Uç: 4 dm = 40 cm', '2. Uç: 200 mm = 20 cm', TUR, TUR_A,
        'Farklı uzunluk birimlerindeki çıta kesme problemi şeması.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('800 mm', '800 ÷ 10 = 80 cm (0,8 m)', KIR, KIR_A),
        ('15 dm', '15 × 10 = 150 cm (1,5 m)', TUR, TUR_A),
        ('4 m', '4 × 100 = 400 cm (4 m)', MAVI, MAVI_A),
        ('0,02 km', '0,02 × 1000 = 20 m (2000 cm)', YES, YES_A),
    ], 'Dört farklı uzunluk biriminin metre ve santimetre karşılıkları.')
    s[9]['gorsel'] = ikili_kart(
        'Nokta Grafiği Verileri (5 Gün)', 'Sıralı: 4,  6,  6,  8,  11', 'Toplam = 4 + 6 + 6 + 8 + 11 = 35', MAVI, MAVI_A,
        'Merkezî Eğilim Ölçüleri', 'Ortalama = Toplam ÷ 5 = 35 ÷ 5', 'Ortanca = Sıralı dizide tam ortadaki (3.)', YES, YES_A,
        'Nokta grafiği verilerinden aritmetik ortalama ve ortanca bulma.'
    )
    s[11]['gorsel'] = ikili_kart(
        '1. En Sevilen Kitap Türü', 'Sözel grup → Kategorik Veri', 'Grafik: Sıklık Tablosu / Sütun', MOR, MOR_A,
        '2. Haftalık Okunan Sayfa Sayısı', 'Sayısal sayma → Nicel (Kesikli)', 'Grafik: Nokta / Kök-Yaprak', YES, YES_A,
        'Kitap türü ve sayfa sayısı verilerinin sınıflandırılması.'
    )
