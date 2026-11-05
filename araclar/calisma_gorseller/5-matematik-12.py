"""5. sınıf Matematik 12. hafta (Doğal Sayılarla Dört İşlem Problemleri ve Kalanın Yorumlanması) görselleri.
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
        'Gezi Katılımcı Sayısı', '148 Öğrenci + 7 Öğretmen', 'Toplam = 155 Kişi', MAVI, MAVI_A,
        'Servis Kapasitesi: 30 Kişi', '155 ÷ 30 = 5 (Kalan: 5 kişi)', 'Kalan 5 kişi için +1 servis!', TUR, TUR_A,
        'Okul gezisi servis aracı hesaplama ve kalan yorumlama kartı.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. 125 ÷ 12 (Tam Kutu)', 'Bölüm: 10, Kalan: 5 → 10 kutu', MAVI, MAVI_A),
        ('2. 125 ÷ 12 (Tüm Yumurta)', 'Bölüm + 1 → 11 kutu gerekir', YES, YES_A),
        ('3. 250 TL ÷ 40 TL (Kitap)', 'Bölüm: 6 kitap (10 TL artar)', TUR, TUR_A),
        ('4. 95 ÷ 8 (Son Sıra Fidan)', 'Kalan: 7 fidan son sıraya', MOR, MOR_A),
    ], 'Kalanlı bölme işleminin dört farklı gerçek yaşam yorumu.')
    s[5]['gorsel'] = ikili_kart(
        'Kampanyalı Bilgisayar', 'Toplam Fiyat: 18.000 TL', 'Ödenen Peşinat: 4.500 TL', CAM, CAM_A,
        'Ödeme Planı (6 Eşit Taksit)', 'Kalan Borç = 18.000 − 4.500', '1 Taksit = Kalan ÷ 6 = ?', YES, YES_A,
        'Bilgisayar peşinat ve 6 eşit taksit hesaplama şeması.'
    )
    s[6]['gorsel'] = ikili_kart(
        'Kutu Modeli (Toplam 190)', 'Keçi: [ 1 Kutu ]', 'Koyun: [ 4 Kutu ] + 15', MOR, MOR_A,
        'Çözüm Stratejisi', '1) 190 − 15 = 175 (5 eş kutu)', '2) 1 Kutu (Keçi) = 175 ÷ 5 = ?', TUR, TUR_A,
        'Koyun ve keçi sayıları için kat (kutu) modeli şeması.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Sabah Üretimi ve Satış', 'Üretilen: 380 Simit', 'Sabah Satılan: 44 Simit', TUR, TUR_A,
        'Kutulama İşlemi', 'Kalan = 380 − 44 = 336 Simit', 'Her kutuda 12 simit → Kaç kutu?', MAVI, MAVI_A,
        'Fırındaki simitlerin kutulanması problemi şeması.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Gömlekler', '3 × 450 TL = 1.350 TL', MAVI, MAVI_A),
        ('2. Toplam Harcama', '1.350 + 950 = 2.300 TL', YES, YES_A),
        ('3. Para Üstü', '2.500 − 2.300 = 200 TL', TUR, TUR_A),
        ('4. Kontrol', '2.300 + 200 = 2.500 TL', MOR, MOR_A),
    ], 'Mağaza alışverişi dört adımlı problem çözümü.')
    s[9]['gorsel'] = ikili_kart(
        'Tam Bilet Gişesi', 'Bilet Fiyatı: 120 TL', 'İzleyici: 25 Yetişkin', MAVI, MAVI_A,
        'Öğrenci Bileti Gişesi', 'Bilet Fiyatı: 80 TL', 'İzleyici: 40 Öğrenci', YES, YES_A,
        'Sinema salonu tam ve öğrenci bileti gelir tablosu.'
    )
    s[11]['gorsel'] = ikili_kart(
        'A) 110 m Kumaş ÷ 8 m Örtü', 'Bölüm: 13, Kalan: 6 m kumaş', 'Kalan 6 m ihmal edilir → 13 örtü', MAVI, MAVI_A,
        'B) 110 Kişi ÷ 8 Kişilik Çadır', 'Bölüm: 13, Kalan: 6 kişi', '6 kişi için +1 çadır → 14 çadır', KIR, KIR_A,
        'Aynı bölme işleminde kalanın ihmal edilmesi ve bölüme 1 eklenmesi karşılaştırması.'
    )
