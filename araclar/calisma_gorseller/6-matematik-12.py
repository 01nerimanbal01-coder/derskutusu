"""6. sınıf Matematik 12. hafta (Kesir, Ondalık ve Yüzde Problemleri ile Uzunluk Ölçme Birimleri) görselleri.
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
    s[1]['gorsel'] = ikili_kart(
        'Romanın Tamamı: 240 Sayfa', '1. Hafta: 1/4’ü = %25’i okundu', '2. Hafta: %35’i okundu', MAVI, MAVI_A,
        'Çözüm Planı', 'Toplam Okunan: %25 + %35 = %60', 'Kalan: %40 → 240 × (40/100) = ?', YES, YES_A,
        '240 sayfalık kitabın kesir ve yüzde ile okunan/kalan hesabı.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('Uzunluk Merdiveni (×10 / ÷10)', 'km → hm → dam → m → dm → cm → mm', MAVI, MAVI_A),
        ('1. 2,4 km → m ve cm', '2.400 m = 240.000 cm', YES, YES_A),
        ('2. 8,5 dam ve 3. 21 dm', '1 dam = 10 m · 10 dm = 1 m', TUR, TUR_A),
        ('4. 1.500 mm → m ve cm', '1.000 mm = 1 m = 100 cm', MOR, MOR_A),
    ], 'Standart uzunluk ölçme birimleri dönüşüm şeması.')
    s[5]['gorsel'] = ikili_kart(
        'Cadde Uzunluğu: 3,6 km', 'Metreye Dönüşüm: 3,6 × 1000', 'Toplam Yol = 3.600 metre', CAM, CAM_A,
        'Tamamlanan ve Kalan Kısım', 'Tamamlanan: 2/3’ü (2.400 m)', 'Kalan: 1/3’ü = 3.600 ÷ 3 = ?', TUR, TUR_A,
        '3,6 km caddenin metreye çevrilip kalan 1/3 kısmının bulunması.'
    )
    s[6]['gorsel'] = ikili_kart(
        'Kırtasiye Fişi · Kalem 1', '4 Adet Defter × 34,75 TL', '4 × 34,75 = 139 TL', MAVI, MAVI_A,
        'Kırtasiye Fişi · Kalem 2', 'İndirimli Çanta: 160 TL', 'Toplam = 139 + 160 = ? TL', YES, YES_A,
        'Ondalık gösterim ve yüzde içeren kırtasiye alışveriş fişi.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Başlangıç Kurdele: 5 m', 'Santimetre Karşılığı: 500 cm', '1. Kesilen Parça: 140 cm', MOR, MOR_A,
        '2. Kesilen Parça ve Kalan', '2. Parça: 18 dm = 180 cm', 'Kalan = 500 − (140 + 180) = ? cm', TUR, TUR_A,
        '5 metrelik kurdeleden kesilen parçaların santimetre cinsinden hesabı.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('K Şeridi: 850 mm', 'Metre karşılığı: 0,85 m', MAVI, MAVI_A),
        ('L Şeridi: 240 cm', 'Metre karşılığı: 2,4 m', YES, YES_A),
        ('M Şeridi: 1,5 dam', 'Metre karşılığı: 15 m', TUR, TUR_A),
        ('N Şeridi: 0,08 km', 'Metre karşılığı: 80 m', MOR, MOR_A),
    ], 'Dört farklı uzunluk biriminin metreye çevrilerek sıralanması.')
    s[9]['gorsel'] = ikili_kart(
        'Maaş Modeli (5 Eş Kutu = %100)', 'Kira (1/5): [ 1 Kutu = %20 ]', 'Geriye Kalan: [ 4 Kutu = %80 ]', MAVI, MAVI_A,
        'Kalanın 1/4’ü Mutfak Gideri', '4 kutunun 1/4’ü = [ 1 Kutu = %20 ]', 'Son Kalan: 3 Kutu = %?', YES, YES_A,
        'Kalanın kesri probleminin 5 eş kutu ve yüzde ile modellenmesi.'
    )
    s[11]['gorsel'] = ikili_kart(
        'Terzi Kumaş Topu: 12 metre', '1. Kullanım: %25’i (1/4’ü)', '12 ÷ 4 = 3 metre', TUR, TUR_A,
        '2. Kullanım ve Kalan Kumaş', '2. Kullanım: 350 cm = 3,5 metre', 'Kalan: 12 − (3 + 3,5) = ? m', YES, YES_A,
        'Terzi atölyesinde yüzde ve santimetre dönüşümlü kumaş problemi.'
    )
