"""8. sınıf Arapça 1. hafta (1. Ünite: Etkinlikler — 1. Ders: Kulüpler ve Kısa Diyaloglar) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def kulup_kayit_karti():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(95, 24, 'Öğrenci Kulüp Kayıt Kartı', MOR)
    ic += yazi_ar(265, 28, 'الأَنْدِيَةُ الطُّلَّابِيَّةُ', LAC)

    ic += kutu(4, 42, 172, 64, TUR_A, TUR, 8)
    ic += yazi_tr(90, 60, '1. Sevilen Etkinlik', TUR)
    ic += yazi_ar(90, 94, 'أُحِبُّ الْمُوسِيقَى', LAC)

    ic += kutu(184, 42, 172, 64, YES_A, YES, 8)
    ic += yazi_tr(270, 60, '2. Karşıt Seçim (لٰكِنْ)', YES)
    ic += yazi_ar(270, 94, 'لٰكِنْ أَخْتَارُ نَادِيَ الْمَكْتَبَةِ', LAC)
    return svg(360, 110, ic, 'Kulüp kayıt kartı: Müziği severim fakat kütüphane kulübünü seçerim.', 15)


def gorev_sorumluluk_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(216, 27, 'أَنَا مَسْؤُولٌ عَنْ تَرْتِيبِ الْكُتُبِ', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Kart', YES, 'start')
    ic += yazi_ar(216, 63, 'أَنَا مَسْؤُولَةٌ عَنْ نَظَافَةِ الصَّفِّ', LAC)

    ic += kutu(4, 76, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 96, '3. Kart', TUR, 'start')
    ic += yazi_ar(216, 99, 'أَنَا مَسْؤُولٌ عَنِ الأَدَوَاتِ الرِّيَاضِيَّةِ', LAC)
    return svg(360, 112, ic, 'Üç kulüp görev kartı: Kitap düzenleme, sınıf temizliği ve spor araçları.', 15)


def toplanti_saat_cizelgesi():
    ic = kutu(4, 6, 112, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(60, 24, '1. Toplantı', MAVI)
    ic += yazi_ar(60, 56, 'الْوَاحِدَةُ', LAC)
    ic += yazi_ar(60, 86, 'وَالنِّصْفُ', LAC)

    ic += kutu(124, 6, 112, 94, YES_A, YES, 8)
    ic += yazi_tr(180, 24, '2. Toplantı', YES)
    ic += yazi_ar(180, 56, 'الرَّابِعَةُ', LAC)
    ic += yazi_ar(180, 86, 'وَالنِّصْفُ', LAC)

    ic += kutu(244, 6, 112, 94, TUR_A, TUR, 8)
    ic += yazi_tr(300, 24, '3. Toplantı', TUR)
    ic += yazi_ar(300, 56, 'الثَّانِيَةُ', LAC)
    ic += yazi_ar(300, 86, 'إِلَّا رُبْعًا', LAC)
    return svg(360, 106, ic, 'Kulüp toplantı saatleri: 01.30, 04.30 ve 01.45 (ikiye çeyrek var).', 15)


def gerekce_soru_diyalogu():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Soru', TUR, 'start')
    ic += yazi_ar(216, 36, '___ تَخْتَارُ نَادِيَ الشَّطْرَنْجِ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Cevap', YES, 'start')
    ic += yazi_ar(216, 90, 'لِأَنِّي أُحِبُّ الشَّطْرَنْجَ كَثِيرًا', LAC)
    return svg(360, 110, ic, 'Neden sorusu ve çünkü satrancı çok seviyorum cevabı.', 15)


def sebep_sonuc_semasi():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Neden (السَّبَبُ)', MAVI)
    ic += yazi_ar(90, 58, 'أُحِبُّ الْقِرَاءَةَ', LAC)
    ic += yazi_tr(90, 86, 'Okumayı severim', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Sonuç (لِذٰلِكَ)', YES)
    ic += yazi_ar(270, 58, 'أَخْتَارُ نَادِيَ الْمَكْتَبَةِ', LAC)
    ic += yazi_tr(270, 86, 'Kütüphane kulübünü seçerim', LAC, 'middle', False)
    return svg(360, 106, ic, 'Sebep ve lizâlike bağlacıyla sonuç şeması.', 15)


def kulup_akis_semasi():
    adimlar = [
        (4, '1. İlgi', 'أُحِبُّ الْكُتُبَ', MOR, MOR_A),
        (93, '2. Seçim', 'لِذٰلِكَ أَخْتَارُ', MAVI, MAVI_A),
        (182, '3. Saat', 'الْوَاحِدَةُ وَالنِّصْفُ', TUR, TUR_A),
        (271, '4. Görev', 'ثُمَّ أُرَتِّبُ', YES, YES_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Kulüp seçimi ve görev akışı dört aşamalı şeması.', 15)


def tercih_karsilastirma_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Öğrenci', MAVI, 'start')
    ic += yazi_ar(222, 36, 'أُحِبُّ الطَّبِيعَةَ لِذٰلِكَ أَخْتَارُ نَادِيَ الطَّبِيعَةِ', LAC)

    ic += kutu(4, 58, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Öğrenci', TUR, 'start')
    ic += yazi_ar(222, 90, 'أُحِبُّ الرَّسْمَ لٰكِنْ أُفَضِّلُ نَادِيَ التِّكْنُولُوجِيَا', LAC)
    return svg(360, 110, ic, 'İki öğrencinin lizâlike ve lâkin bağlaçlı kulüp tercih kartı.', 15)


def cikarim_diyalog_karti():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, '1. Elif', YES, 'start')
    ic += yazi_ar(224, 36, 'أَنَا مَسْؤُولَةٌ عَنْ نَظَافَةِ الصَّفِّ', LAC)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Kerem (إِذَنْ ...)', TUR, 'start')
    ic += yazi_ar(224, 90, '؟', KIR)
    return svg(360, 110, ic, 'Elif sınıf temizliğinden sorumlu olduğunu söyler, Kerem izen ile kulübünü çıkarır.', 15)


def kulup_tanitim_ipuclari():
    ic = kutu(4, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, 'Seçilen Kulüp ve Gerekçe', MOR)
    ic += yazi_ar(90, 56, 'نَادِي الْمَكْتَبَةِ', LAC)
    ic += yazi_ar(90, 86, 'لِأَنِّي أُحِبُّ الْقِرَاءَةَ', LAC)

    ic += kutu(184, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, 'Üstlenilen Görev', MAVI)
    ic += yazi_ar(270, 56, 'أَنَا مَسْؤُولٌ عَنْ', LAC)
    ic += yazi_ar(270, 86, 'تَرْتِيبِ الْكُتُبِ', LAC)
    return svg(360, 106, ic, 'Kütüphane kulübü seçimi, okuma sevgisi ve kitap düzenleme görevi kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kulup_kayit_karti()
    s[2]['gorsel'] = gorev_sorumluluk_kartlari()
    s[3]['gorsel'] = toplanti_saat_cizelgesi()
    s[5]['gorsel'] = gerekce_soru_diyalogu()
    s[7]['gorsel'] = sebep_sonuc_semasi()
    s[8]['gorsel'] = kulup_akis_semasi()
    s[9]['gorsel'] = tercih_karsilastirma_karti()
    s[11]['gorsel'] = cikarim_diyalog_karti()
    s[12]['gorsel'] = kulup_tanitim_ipuclari()
