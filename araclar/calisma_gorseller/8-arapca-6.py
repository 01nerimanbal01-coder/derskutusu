"""8. sınıf Arapça 6. hafta (2. Ünite: Etkinlikler — Gezi, Ulaşım Araçları ve Sıralama Bağlaçları) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=True):
    ag = '700' if kalin else '500'
    dar = ' textLength="156" lengthAdjust="spacingAndGlyphs"' if (hiza == 'middle' and x in (86, 90, 266, 270) and len(metin) > 22) else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="12" font-weight="{ag}" fill="{renk}"{dar}>{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle'):
    blen = sum(1 for c in metin if not (0x064B <= ord(c) <= 0x065F or ord(c) == 0x0670))
    dar = ''
    if x in (86, 90, 266, 270) and blen > 14:
        dar = ' textLength="154" lengthAdjust="spacingAndGlyphs"'
    elif x >= 210 and blen > 25:
        dar = ' textLength="220" lengthAdjust="spacingAndGlyphs"'
    elif x == 180 and blen > 32:
        dar = ' textLength="330" lengthAdjust="spacingAndGlyphs"'
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22" fill="{renk}"{dar}>{metin}</text>'


def konya_gezi_bileti():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(95, 24, 'Gezi Ulaşım Kartı', MOR)
    ic += yazi_ar(265, 28, 'رِحْلَةٌ مَدْرَسِيَّةٌ', LAC)

    ic += kutu(4, 42, 172, 64, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 60, 'Varış Şehri', MAVI)
    ic += yazi_ar(90, 94, 'إِلَى قُونْيَا', LAC)

    ic += kutu(184, 42, 172, 64, YES_A, YES, 8)
    ic += yazi_tr(270, 60, 'Ulaşım Aracı', YES)
    ic += yazi_ar(270, 94, 'بِالْقِطَارِ السَّرِيعِ', LAC)
    return svg(360, 110, ic, 'Konya okul gezisi bileti: Hızlı trenle Konya’ya okul gezisi.', 15)


def siralama_baglac_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Aşama', MAVI, 'start')
    ic += yazi_ar(224, 27, 'أَوَّلًا زُرْنَا مَسْجِدَ آيَا صُوفْيَا', LAC)

    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Aşama', TUR, 'start')
    ic += yazi_ar(224, 63, 'ثُمَّ ذَهَبْنَا إِلَى قَصْرِ طُوبْ قَابِي', LAC)

    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Aşama', YES, 'start')
    ic += yazi_ar(224, 99, 'وَأَخِيرًا رَكِبْنَا السَّفِينَةَ فِي الْمَضِيقِ', LAC)
    return svg(360, 112, ic, 'Evvelen, sümme ve ahîran sıralama bağlaçlı İstanbul gezi kartları.', 15)


def dort_gezgin_eylem_karti():
    ic = kutu(4, 4, 172, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, '1. Salih', MAVI)
    ic += yazi_ar(90, 44, 'يُسَافِرُ إِلَى أَنْطَالْيَا بِالطَّائِرَةِ', LAC)

    ic += kutu(184, 4, 172, 48, MOR_A, MOR, 8)
    ic += yazi_tr(270, 20, '2. Meryem', MOR)
    ic += yazi_ar(270, 44, 'تُحَضِّرُ حَقِيبَةَ السَّفَرِ', LAC)

    ic += kutu(4, 58, 172, 48, YES_A, YES, 8)
    ic += yazi_tr(90, 74, '3. Tarık', YES)
    ic += yazi_ar(90, 98, 'يَلْتَقِطُ الصُّوَرَ فِي الْمُتْحَفِ', LAC)

    ic += kutu(184, 58, 172, 48, KIR_A, KIR, 8)
    ic += yazi_tr(270, 74, '4. Leyla', KIR)
    ic += yazi_ar(270, 98, 'تَنْزِلُ مِنَ الْحَافِلَةِ', LAC)
    return svg(360, 110, ic, 'Dört gezginin ulaşım ve hazırlık eylemleri kartı.', 15)


def kiminle_soru_diyalogu():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Ahmet', TUR, 'start')
    ic += yazi_ar(224, 36, '___ سَتَذْهَبُ فِي عُطْلَةِ الصَّيْفِ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Kerem', YES, 'start')
    ic += yazi_ar(224, 90, 'سَأَذْهَبُ مَعَ أُسْرَتِي', LAC)
    return svg(360, 110, ic, 'Yaz tatilinde kiminle gideceksin sorusu ve ailemle gideceğim cevabı.', 15)


def bilet_gisesi_diyalogu():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Yolcu Sorusu', MAVI)
    ic += yazi_ar(90, 56, 'كَمْ سِعْرُ', LAC)
    ic += yazi_ar(90, 86, 'التَّذْكِرَةِ؟', LAC)

    ic += kutu(184, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Uğurlama Dileği', YES)
    ic += yazi_ar(270, 56, 'رِحْلَةً سَعِيدَةً', LAC)
    ic += yazi_ar(270, 86, 'فِي أَمَانِ اللَّهِ', LAC)
    return svg(360, 106, ic, 'Bilet fiyatı sorma ve iyi yolculuklar dileği kartı.', 15)


def gezi_asamalari_sema():
    adimlar = [
        (4, '1. أَوَّلًا', 'حَضَّرْتُ الْحَقِيبَةَ', MOR, MOR_A),
        (93, '2. ثَانِيًا', 'رَكِبْتُ الْحَافِلَةَ', MAVI, MAVI_A),
        (182, '3. بَعْدَ ذٰلِكَ', 'زُرْنَا الْقَلْعَةَ', TUR, TUR_A),
        (271, '4. أَخِيرًا', 'رَجَعْنَا مَسْرُورِينَ', YES, YES_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Evvelen, sâniyen, ba’de zâlike ve ahîran dört aşamalı gezi şeması.', 15)


def bursa_gezi_cozumleme_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Gezi Planı', MAVI, 'start')
    ic += yazi_ar(228, 36, 'سَنَذْهَبُ فِي رِحْلَةٍ سِيَاحِيَّةٍ إِلَى بُورْصَةَ', LAC)

    ic += kutu(4, 58, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Kişi · Araç · Zaman', TUR, 'start')
    ic += yazi_ar(228, 90, 'مَعَ أُسْرَتِي بِالْحَافِلَةِ غَدًا', LAC)
    return svg(360, 110, ic, 'Yarın ailemle otobüsle Bursa’ya turistik geziye gideceğiz kartı.', 15)


def amac_soru_karti():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, 'Soru', YES, 'start')
    ic += yazi_ar(224, 36, '___ نَذْهَبُ إِلَى إِسْطَنْبُولَ؟', LAC)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Rehber (لِـ)', TUR, 'start')
    ic += yazi_ar(224, 90, 'لِزِيَارَةِ الأَمَاكِنِ التَّارِيخِيَّةِ', LAC)
    return svg(360, 110, ic, 'Niçin İstanbul’a gidiyoruz sorusu ve tarihî yerleri ziyaret etmek için cevabı.', 15)


def sirali_gezi_ipuclari():
    ic = kutu(4, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, '1. أَوَّلًا · 2. ثُمَّ', MOR)
    ic += yazi_ar(90, 56, 'زُرْنَا الْمُتْحَفَ', LAC)
    ic += yazi_ar(90, 86, 'اِلْتَقَطْنَا الصُّوَرَ', LAC)

    ic += kutu(184, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, '3. وَأَخِيرًا (Son Olarak)', MAVI)
    ic += yazi_ar(270, 56, 'رَجَعْنَا إِلَى بُيُوتِنَا', LAC)
    ic += yazi_ar(270, 86, 'مَسْرُورِينَ', LAC)
    return svg(360, 106, ic, 'Evvelen, sümme ve ahîran ile sıralı gezi cümlesi ipuçları.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = konya_gezi_bileti()
    s[2]['gorsel'] = siralama_baglac_kartlari()
    s[3]['gorsel'] = dort_gezgin_eylem_karti()
    s[5]['gorsel'] = kiminle_soru_diyalogu()
    s[7]['gorsel'] = bilet_gisesi_diyalogu()
    s[8]['gorsel'] = gezi_asamalari_sema()
    s[9]['gorsel'] = bursa_gezi_cozumleme_karti()
    s[11]['gorsel'] = amac_soru_karti()
    s[12]['gorsel'] = sirali_gezi_ipuclari()
