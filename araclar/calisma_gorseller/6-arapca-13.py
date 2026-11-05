"""6. sınıf Arapça 13. hafta (Sınıfımda ve Okul Bahçesinde, Yer Zarfları ve Emirler) görselleri.
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
        '1. Konum · Üstünde (فَوْقَ)', 'اَلْكِتَابُ فَوْقَ الطَّاوِلَةِ', 'Kitap masanın üstündedir', MAVI, MAVI_A,
        '2. Konum · Altında (تَحْتَ)', 'اَلْحَقِيبَةُ تَحْتَ الْمَقْعَدِ', 'Çanta sıranın altındadır', TUR, TUR_A,
        'Üstünde ve altında yer zarfları karşılaştırma kartları.', ar1=True, ar2=True
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Otur (اِجْلِسْ / اِجْلِسِي)', 'اِجْلِسْ مَكَانَكَ · اِجْلِسِي مَكَانَكِ', MAVI, MAVI_A),
        ('2. Oku (اِقْرَأْ / اِقْرَئِي)', 'اِقْرَأِ الدَّرْسَ · اِقْرَئِي الدَّرْسَ', YES, YES_A),
        ('3. Yaz (اُكْتُبْ / اُكْتُبِي)', 'اُكْتُبْ · اُكْتُبِي عَلَى الدَّفْتَرِ', TUR, TUR_A),
        ('4. Bak (اُنْظُرْ / اُنْظُرِي)', 'اُنْظُرْ · اُنْظُرِي إِلَى السَّبُّورَةِ', MOR, MOR_A),
    ], 'Sınıf içi eril ve dişil emir kalıpları tablosu.', ar=True)
    s[5]['gorsel'] = ikili_kart(
        '1. Kat (الطَّابِقُ الْأَوَّلُ)', 'اَلْمُخْتَبَرُ فِي الطَّابِقِ الْأَوَّلِ', 'Laboratuvar 1. kattadır', CAM, CAM_A,
        '2. Kat (الطَّابِقُ الثَّانِي)', 'اَلصَّفُّ السَّادِسُ فِي الطَّابِقِ الثَّانِي', '6. Sınıf 2. kattadır', YES, YES_A,
        'Okul katları ve sıra sayıları yerleşim şeması.', ar1=True, ar2=True
    )
    s[6]['gorsel'] = ikili_kart(
        'Erkek Öğrenciye Yönerge', 'اُنْظُرْ إِلَى السَّبُّورَةِ وَاقْرَأْ', 'Tahtaya bak ve oku (Eril)', MAVI, MAVI_A,
        'Kız Öğrenciye (Merve) Yönerge', 'اُنْظُرِي إِلَى السَّبُّورَةِ وَاقْرَئِي', 'Tahtaya bak ve oku (Dişil)', MOR, MOR_A,
        'Eril ve dişil birleşik sınıf yönergeleri.', ar1=True, ar2=True
    )
    s[7]['gorsel'] = ikili_kart(
        'Yer Sorusu (أَيْنَ يُوجَدُ...؟)', 'أَيْنَ يُوجَدُ الْحَاسُوبُ؟', 'Bilgisayar nerede bulunur?', MAVI, MAVI_A,
        'Görsel İpucu: Masa Üstü', 'فَوْقَ الطَّاوِلَةِ', 'Masanın üstünde', YES, YES_A,
        'Bilgisayarın konumunu sorma ve yanıtlama kartı.', ar1=True, ar2=True
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Sıra Sayısı (Birinci)', 'اَلْأَوَّلُ (1.)', MAVI, MAVI_A),
        ('2. Sıra Sayısı (İkinci)', 'اَلثَّانِي (2.)', YES, YES_A),
        ('3. Sıra Sayısı (Üçüncü)', 'اَلثَّالِثُ (3.)', TUR, TUR_A),
        ('4. Sıra Sayısı (Dördüncü)', 'اَلرَّابِعُ (4.)', MOR, MOR_A),
    ], 'Arapça 1’den 4’e kadar sıra sayıları kartları.', ar=True)
    s[9]['gorsel'] = dortlu_kart([
        ('1. Kart (Doğru - Eril)', 'أَيْنَ يُوجَدُ الْمَقْعَدُ؟', YES, YES_A),
        ('2. Kart (Doğru - Dişil)', 'أَيْنَ تُوجَدُ السَّبُّورَةُ؟', MAVI, MAVI_A),
        ('3. Kart (Hatalı Uyum!)', 'أَيْنَ يُوجَدُ الْخَرِيطَةُ؟', KIR, KIR_A),
        ('4. Kart (Doğru - Zarf)', 'اَلسَّلَّةُ يَمِينَ الْبَابِ', CAM, CAM_A),
    ], 'يُوجَدُ ve تُوجَدُ fiillerinin eril-dişil uyum incelemesi.', ar=True)
    s[11]['gorsel'] = ikili_kart(
        '1. Zarf İpucu: فَوْقَ (Üstünde)', 'اَلْكِتَابُ فَوْقَ الْمَكْتَبِ', 'Kitap masanın üstündedir', MAVI, MAVI_A,
        '2. Zarf İpucu: أَمَامَ (Önünde)', 'اَلْمُعَلِّمُ أَمَامَ السَّبُّورَةِ', 'Öğretmen tahtanın önündedir', YES, YES_A,
        'Yer zarflarıyla sınıf içi konum cümlesi kurma kartları.', ar1=True, ar2=True
    )
