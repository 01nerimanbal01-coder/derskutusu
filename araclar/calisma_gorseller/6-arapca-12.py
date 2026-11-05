"""6. sınıf Arapça 12. hafta (Okulun Bölümleri, Okul Çalışanları, Sıra Sayıları ve Yer-Yön Zarfları) görselleri.
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
        '1. Kat (اَلطَّابِقُ الْأَوَّلُ)', 'اَلْمَكْتَبَةُ (Kütüphane)', 'Sol taraf birimi', MAVI, MAVI_A,
        'Sağındaki Birim (يَمِينَ)', 'اَلْمَقْصِفُ (Kantin)', 'Kütüphanenin sağında', TUR, TUR_A,
        'Birinci kattaki kütüphane ve sağındaki kantin kat planı.', ar1=True, ar2=True
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Birinci Kat', 'اَلطَّابِقُ الْأَوَّلُ', MAVI, MAVI_A),
        ('2. Altıncı Sınıf', 'اَلصَّفُّ السَّادِسُ', YES, YES_A),
        ('3. Tahtanın Önünde', 'أَمَامَ السَّبُّورَةِ الذَّكِيَّةِ', TUR, TUR_A),
        ('4. Masanın Üstünde', 'فَوْقَ الْمَكْتَبِ', MOR, MOR_A),
    ], 'Sıra sayıları ve yer-yön zarfları uygulama kartları.', ar=True)
    s[5]['gorsel'] = ikili_kart(
        'Sınıf Envanteri (فِي الصَّفِّ)', 'سَبُّورَةٌ ذَكِيَّةٌ (Akıllı tahta)', 'Duvar ve öğretmen masası', MAVI, MAVI_A,
        'Teknoloji ve Ders Araçları', 'حَاسُوبٌ وَخَرِيطَةٌ', 'Bilgisayar ve duvar haritası', YES, YES_A,
        'Sınıfta bulunan eşyalar envanter kartı.', ar1=True, ar2=True
    )
    s[6]['gorsel'] = ikili_kart(
        '1. Konum: Sıranın Altında', 'تَحْتَ الْمَقْعَدِ', 'Altında = تَحْتَ', MOR, MOR_A,
        '2. Konum: Tahtanın Önünde', 'أَمَامَ السَّبُّورَةِ', 'Önünde = أَمَامَ', CAM, CAM_A,
        'Sıranın altında ve tahtanın önünde konum kartları.', ar1=True, ar2=True
    )
    s[7]['gorsel'] = ikili_kart(
        '2. Ünite Özdeyişi', 'رُتْبَةُ الْعِلْمِ أَعْلَى الرُّتَبِ', 'İlim rütbesi en yüce rütbedir.', YES, YES_A,
        'Kelime Analizi', 'رُتْبَةُ (Rütbe/Makam) · الْعِلْمِ (İlim)', 'أَعْلَى الرُّتَبِ (Rütbelerin en yücesi)', MAVI, MAVI_A,
        'Rütbetül-ilmi a’ler-rüteb özdeyişi ve kelime analizi.', ar1=True, ar2=True
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Birinci (1.)', 'اَلْأَوَّلُ', MAVI, MAVI_A),
        ('2. İkinci (2.)', 'اَلثَّانِي', YES, YES_A),
        ('3. Üçüncü (3.)', 'اَلثَّالِثُ', TUR, TUR_A),
        ('4. Dördüncü (4.)', 'اَلرَّابِعُ', MOR, MOR_A),
    ], 'Arapça 1’den 4’e kadar sıra sayıları kartları.', ar=True)
    s[9]['gorsel'] = dortlu_kart([
        ('1. Müdür → Müdür Odası', 'اَلْمُدِيرُ فِي غُرْفَةِ الْمُدِيرِ', MAVI, MAVI_A),
        ('2. Öğretmen → Sınıf', 'اَلْمُعَلِّمُ فِي الصَّفِّ', YES, YES_A),
        ('3. Öğrenci → Kütüphane', 'اَلطَّالِبُ فِي الْمَكْتَبَةِ', TUR, TUR_A),
        ('4. Hatalı Eşleştirme (!)', 'اَلْمُوَظَّفُ فَوْقَ السَّبُّورَةِ', KIR, KIR_A),
    ], 'Okul çalışanları ve görev yerleri eşleştirme tablosu.', ar=True)
    s[11]['gorsel'] = ikili_kart(
        '1. Sınıf Düzeyim (6. Sınıf)', 'أَنَا طَالِبٌ فِي الصَّفِّ السَّادِسِ', 'Altıncı sınıf öğrencisiyim', MAVI, MAVI_A,
        '2. Sınıfımın Bulunduğu Kat', 'صَفِّي فِي الطَّابِقِ الثَّانِي', 'Sınıfım ikinci kattadır', YES, YES_A,
        'Okul ve sınıf tanıtımı yazılı anlatım rehber kartı.', ar1=True, ar2=True
    )
