"""8. sınıf Arapça 4. hafta (1. Ünite: Etkinlikler — Tiyatro, Soru Edatları, Bağlaçlar, Saatler ve Dört Ana Yön) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def dort_yon_pusula_karti():
    ic = kutu(4, 4, 172, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, 'Kuzey (الشَّمَالُ)', MAVI)
    ic += yazi_ar(90, 44, 'طَرَابْزُون فِي شَمَالِ تُرْكِيَا', LAC)

    ic += kutu(184, 4, 172, 48, KIR_A, KIR, 8)
    ic += yazi_tr(270, 20, 'Güney (الْجَنُوبُ)', KIR)
    ic += yazi_ar(270, 44, 'أَنْطَالْيَا فِي جَنُوبِ تُرْكِيَا', LAC)

    ic += kutu(4, 58, 172, 48, MOR_A, MOR, 8)
    ic += yazi_tr(90, 74, 'Batı (الْغَرْبُ)', MOR)
    ic += yazi_ar(90, 98, 'إِزْمِير فِي غَرْبِ تُرْكِيَا', LAC)

    ic += kutu(184, 58, 172, 48, TUR_A, TUR, 8)
    ic += yazi_tr(270, 74, 'Doğu (الشَّرْقُ)', TUR)
    ic += yazi_ar(270, 98, 'وَان فِي شَرْقِ تُرْكِيَا', LAC)
    return svg(360, 110, ic, 'Türkiye dört ana yön ve şehir konumları kartı.', 15)


def dijital_saat_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Saat', MAVI, 'start')
    ic += yazi_ar(224, 27, 'السَّاعَةُ الثَّالِثَةُ تَمَامًا', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Saat', YES, 'start')
    ic += yazi_ar(224, 63, 'السَّاعَةُ السَّابِعَةُ وَالرُّبْعُ', LAC)

    ic += kutu(4, 76, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 96, '3. Saat', TUR, 'start')
    ic += yazi_ar(224, 99, 'السَّاعَةُ الْعَاشِرَةُ إِلَّا الرُّبْعَ', LAC)
    return svg(360, 112, ic, 'Tam üç, yediyi çeyrek geçiyor ve ona çeyrek var saat kartları.', 15)


def gosteri_izlenim_karti():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(14, 24, '1. Sahne', MOR, 'start')
    ic += yazi_ar(224, 27, 'لَعِبَ الْمُمَثِّلُ دَوْرًا مُهِمًّا', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Salon', YES, 'start')
    ic += yazi_ar(224, 63, 'كَانَ الْعَرْضُ رَائِعًا وَصَفَّقَ الْجُمْهُورُ', LAC)

    ic += kutu(4, 76, 352, 32, KIR_A, KIR, 7)
    ic += yazi_tr(14, 96, '3. Bilet', KIR, 'start')
    ic += yazi_ar(224, 99, 'لٰكِنَّ التَّذْكِرَةَ غَالِيَةٌ', LAC)
    return svg(360, 112, ic, 'Tiyatro gösterisi izlenim kartı: Önemli rol, seyirci alkışı ve pahalı bilet.', 15)


def zitlik_bilet_karti():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. İstek Cümlesi', MAVI)
    ic += yazi_ar(90, 56, 'أَرَادَ عَلِيٌّ مُشَاهَدَةَ', LAC)
    ic += yazi_ar(90, 86, 'الْمَسْرَحِيَّةِ', LAC)

    ic += kutu(184, 6, 172, 94, KIR_A, KIR, 8)
    ic += yazi_tr(270, 24, '2. Karşıt Durum', KIR)
    ic += yazi_ar(270, 56, '___ التَّذَاكِرَ نَفِدَتْ', LAC)
    ic += yazi_tr(270, 86, 'Biletler tükendi', LAC, 'middle', False)
    return svg(360, 106, ic, 'Ali oyunu izlemek istedi fakat biletler tükendi kartı.', 15)


def otobus_gecikme_karti():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Sebep', TUR, 'start')
    ic += yazi_ar(224, 36, 'تَأَخَّرَتِ الْحَافِلَةُ فِي الطَّرِيقِ', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Sonuç (لِذٰلِكَ)', YES, 'start')
    ic += yazi_ar(224, 90, 'لِذٰلِكَ وَصَلْنَا مُتَأَخِّرِينَ', LAC)
    return svg(360, 110, ic, 'Otobüs gecikti, bu yüzden geç ulaştık sebep-sonuç kartı.', 15)


def davet_gosteri_akisi():
    adimlar = [
        (4, '1. Davet', 'هَلْ تُرِيدُ؟', MAVI, MAVI_A),
        (93, '2. Kabul', 'بِكُلِّ سُرُورٍ', YES, YES_A),
        (182, '3. Saat', 'الْخَامِسَةُ وَالنِّصْفُ', TUR, TUR_A),
        (271, '4. Alkış', 'صَفَّقَ الْجُمْهُورُ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Tiyatro daveti, kabul, izleme saati ve alkış dört aşamalı şeması.', 15)


def ceyrek_gece_kala_karti():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, '1. Kart (04.15)', YES, 'start')
    ic += yazi_ar(228, 36, 'السَّاعَةُ الرَّابِعَةُ وَالرُّبْعُ', LAC)

    ic += kutu(4, 58, 352, 48, KIR_A, KIR, 8)
    ic += yazi_tr(14, 78, '2. Kart (03.45)', KIR, 'start')
    ic += yazi_ar(228, 90, 'السَّاعَةُ الرَّابِعَةُ إِلَّا الرُّبْعَ', LAC)
    return svg(360, 110, ic, '04.15 ve 03.45 (dörde çeyrek var) karşılaştırma kartı.', 15)


def oyun_konusu_diyalogu():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Soru', MAVI, 'start')
    ic += yazi_ar(224, 36, '؟', KIR)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Cevap', TUR, 'start')
    ic += yazi_ar(224, 90, 'مَوْضُوعُ الْمَسْرَحِيَّةِ تَارِيخِيٌّ وَمُفِيدٌ', LAC)
    return svg(360, 110, ic, 'Tiyatro oyununun konusu nedir sorusu ve tarihîdir cevabı.', 15)


def tiyatro_konum_saat_ipuclari():
    ic = kutu(4, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(90, 24, 'Tiyatronun Konumu', YES)
    ic += yazi_ar(90, 56, 'يَقَعُ الْمَسْرَحُ', LAC)
    ic += yazi_ar(90, 86, 'فِي جَنُوبِ الْمَدِينَةِ', LAC)

    ic += kutu(184, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(270, 24, 'İzleme Saati (05.45)', MOR)
    ic += yazi_ar(270, 56, 'السَّاعَةُ السَّادِسَةُ', LAC)
    ic += yazi_ar(270, 86, 'إِلَّا الرُّبْعَ', LAC)
    return svg(360, 106, ic, 'Tiyatronun şehrin güneyindeki konumu ve 05.45 izleme saati kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_yon_pusula_karti()
    s[2]['gorsel'] = dijital_saat_kartlari()
    s[3]['gorsel'] = gosteri_izlenim_karti()
    s[5]['gorsel'] = zitlik_bilet_karti()
    s[7]['gorsel'] = otobus_gecikme_karti()
    s[8]['gorsel'] = davet_gosteri_akisi()
    s[9]['gorsel'] = ceyrek_gece_kala_karti()
    s[11]['gorsel'] = oyun_konusu_diyalogu()
    s[12]['gorsel'] = tiyatro_konum_saat_ipuclari()
