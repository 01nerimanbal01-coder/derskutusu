"""8. sınıf Arapça 9. hafta (2. Ünite: Kültür ve Sanat — 2. Ders: Kitap Fuarında) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe Noto Sans 11-12 pt, Arapça Arial 20-22 pt RTL (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=True, boy=11.2):
    ag = '700' if kalin else '500'
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle', boy=20):
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="{boy}" fill="{renk}">{metin}</text>'


def fuar_salon_tabelalari():
    """Soru 2 (s[1]): 1 ve 2 numaralı salon tabelaları."""
    ic = kutu(4, 4, 352, 28, MOR_A, MOR, 7)
    ic += yazi_tr(85, 22, 'Fuar Salon Tabelaları', MOR)
    ic += yazi_ar(255, 24, 'فِي مَعْرِضِ الْكِتَابِ', LAC, boy=18)

    ic += kutu(4, 38, 172, 60, TUR_A, TUR, 8)
    ic += yazi_tr(90, 56, '1. Salon (جَنَاح ١)', TUR)
    ic += yazi_ar(90, 86, 'قِصَصُ الْأَطْفَالِ', LAC)

    ic += kutu(184, 38, 172, 60, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 56, '2. Salon (جَنَاح ٢)', MAVI)
    ic += yazi_ar(270, 86, 'الْكُتُبُ الْعِلْمِيَّةُ', LAC)
    return svg(360, 102, ic, 'Kitap fuarı 1. salon çocuk hikâyeleri ve 2. salon bilimsel kitaplar tabelası.', 16)


def sifat_tamlamasi_kartlari():
    """Soru 3 (s[2]): Sıfat tamlaması mevsuf-sıfat uyum kartları."""
    kartlar = [
        (4, 4, '1. Eril Tekil', 'كِتَابٌ مُفِيدٌ', MAVI, MAVI_A),
        (184, 4, '2. Dişil Tekil', 'قِصَّةٌ مُشَوِّقَةٌ', TUR, TUR_A),
        (4, 54, '3. Akılsız Çoğul', 'الْكُتُبُ الْجَدِيدَةُ', YES, YES_A),
        (184, 54, '4. Belirli Eril', 'الْمَعْرِضُ الدَّوْلِيُّ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kartlar:
        ic += kutu(x, y, 172, 46, z, r, 7)
        ic += yazi_tr(x + 86, y + 17, bas, r, boy=10.5)
        ic += yazi_ar(x + 86, y + 40, ar, LAC, boy=18)
    return svg(360, 104, ic, 'Dört sıfat tamlaması uyum kartı.', 16)


def kiminle_diyalog_panosu():
    """Soru 6 (s[5]): مَعَ مَنْ تَذْهَبُ diyalog panosu."""
    ic = kutu(4, 4, 352, 44, MOR_A, MOR, 8)
    ic += yazi_tr(14, 22, 'Soru:', MOR, 'start')
    ic += yazi_ar(215, 33, '___ تَذْهَبُ إِلَى الْمَعْرِضِ يَا حَسَنُ؟', LAC, boy=19)

    ic += kutu(4, 54, 352, 44, YES_A, YES, 8)
    ic += yazi_tr(14, 72, 'Hasan:', YES, 'start')
    ic += yazi_ar(215, 85, 'أَذْهَبُ إِلَى الْمَعْرِضِ مَعَ أُسْرَتِي', LAC, boy=19)
    return svg(360, 102, ic, 'Hasan ile yapılan kitap fuarı diyalog kartı.', 16)


def dort_tamlama_uyum_karti():
    """Soru 7 (s[6]): 4 sıfat tamlaması kartı (2. kart hatalı: كُتُبٌ مُفِيدٌ)."""
    kartlar = [
        (4, 4, '1. Kart', 'قِصَّةٌ جَمِيلَةٌ', YES, YES_A),
        (184, 4, '2. Kart', 'كُتُبٌ مُفِيدٌ', KIR, KIR_A),
        (4, 54, '3. Kart', 'رِوَايَةٌ تَارِيخِيَّةٌ', MAVI, MAVI_A),
        (184, 54, '4. Kart', 'كَاتِبٌ مَشْهُورٌ', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kartlar:
        ic += kutu(x, y, 172, 46, z, r, 7)
        ic += yazi_tr(x + 36, y + 27, bas, r, boy=10.8)
        ic += yazi_ar(x + 118, y + 32, ar, LAC, boy=18)
    return svg(360, 104, ic, 'Dört sıfat tamlaması kartı.', 16)


def akilsiz_cogul_donusum_karti():
    """Soru 8 (s[7]): الْجَنَاحُ الْكَبِيرُ -> الْأَجْنِحَةُ الْكَبِيرَةُ dönüşüm kartı."""
    ic = kutu(4, 6, 168, 86, MAVI_A, MAVI, 8)
    ic += yazi_tr(88, 24, 'Tekil (Müfred Eril)', MAVI)
    ic += yazi_ar(88, 56, 'الْجَنَاحُ الْكَبِيرُ', LAC, boy=19)
    ic += yazi_tr(88, 80, '(Büyük stant)', LAC, kalin=False, boy=10.2)

    ic += f'<path d="M175 49 L189 49" stroke="{MOR}" stroke-width="2"/>'
    ic += kutu(188, 6, 168, 86, YES_A, YES, 8)
    ic += yazi_tr(272, 24, 'Akılsız Çoğul + Sıfat', YES)
    ic += yazi_ar(272, 56, 'الْأَجْنِحَةُ ...', KIR, boy=19)
    ic += yazi_tr(272, 80, '(Tekil dişil sıfat gelir)', YES, kalin=False, boy=10.2)
    return svg(360, 98, ic, 'Tekil sıfat tamlamasının akılsız çoğula dönüştürülmesi şeması.', 15)


def fuar_ziyaret_siralama_sema():
    """Soru 9 (s[8]): 4 aşamalı fuar ziyareti zaman akışı."""
    adimlar = [
        (4, '1. Giriş', 'قَبْلَ الظُّهْرِ', MAVI, MAVI_A),
        (93, '2. Gezinti', 'فِي الصَّالُونِ', MOR, MOR_A),
        (182, '3. İmza Günü', 'ثُمَّ التَّوْقِيعُ', TUR, TUR_A),
        (271, '4. Satın Alma', 'بَعْدَ ذٰلِكَ', YES, YES_A),
    ]
    ic = ''
    for x, bas, ar, r, z in adimlar:
        ic += kutu(x, 6, 85, 82, z, r, 7)
        ic += yazi_tr(x + 42, 25, bas, r, boy=10.5)
        ic += yazi_ar(x + 42, 64, ar, LAC, boy=17)
    return svg(360, 94, ic, 'Fuar ziyaretinin 4 aşamalı sıralama şeması.', 15)


def okuma_ozdeyis_panosu():
    """Soru 10 (s[9]): Kütüphane panosundaki iki Arapça hikmetli söz."""
    ic = kutu(4, 4, 352, 44, SARI_A, TUR, 8)
    ic += yazi_tr(14, 24, '1. Vecize', TUR, 'start')
    ic += yazi_ar(222, 33, 'الْقِرَاءَةُ غِذَاءُ الرُّوحِ وَالْعَقْلِ', LAC, boy=19)

    ic += kutu(4, 54, 352, 44, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 74, '2. Vecize', MAVI, 'start')
    ic += yazi_ar(222, 83, 'خَيْرُ جَلِيسٍ فِي الزَّمَانِ كِتَابٌ', LAC, boy=19)
    return svg(360, 102, ic, 'Okuma kültürüyle ilgili iki Arapça vecize panosu.', 16)


def ziyaretci_cumle_karti():
    """Soru 12 (s[11]): Fuar ziyaretçi cümle kurma kartı."""
    ic = kutu(4, 6, 172, 86, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, 'Ziyaret ve Refakat', MOR)
    ic += yazi_ar(90, 54, 'ذَهَبْتُ إِلَى الْمَعْرِضِ', LAC, boy=18)
    ic += yazi_ar(90, 80, 'مَعَ صَدِيقِي', LAC, boy=18)

    ic += kutu(184, 6, 172, 86, YES_A, YES, 8)
    ic += yazi_tr(270, 24, 'Satın Alınan Tür', YES)
    ic += yazi_ar(270, 54, 'اشْتَرَيْتُ رِوَايَةً', LAC, boy=18)
    ic += yazi_ar(270, 80, 'تَارِيخِيَّةً', LAC, boy=18)
    return svg(360, 98, ic, 'Fuar ziyaretçi kartı: Arkadaşla gidiş ve tarihî roman satın alma.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = fuar_salon_tabelalari()
    s[2]['gorsel'] = sifat_tamlamasi_kartlari()
    s[5]['gorsel'] = kiminle_diyalog_panosu()
    s[6]['gorsel'] = dort_tamlama_uyum_karti()
    s[7]['gorsel'] = akilsiz_cogul_donusum_karti()
    s[8]['gorsel'] = fuar_ziyaret_siralama_sema()
    s[9]['gorsel'] = okuma_ozdeyis_panosu()
    s[11]['gorsel'] = ziyaretci_cumle_karti()
