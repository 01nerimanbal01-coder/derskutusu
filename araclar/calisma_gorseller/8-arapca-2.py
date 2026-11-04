"""8. sınıf Arapça 2. hafta (1. Ünite: Etkinlikler — Kulüpler: Sorumluluklar, Tercih Cümleleri ve Alıştırmalar) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=14):
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


def arkadas_fiil_uyumu_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Erkek (صَدِيقِي)', MAVI, 'start')
    ic += yazi_ar(230, 36, 'فُرْقَان يُحِبُّ الْكُتُبَ وَلِذٰلِكَ ___ نَادِيَ الْمَكْتَبَةِ', LAC)

    ic += kutu(4, 58, 352, 48, MOR_A, MOR, 8)
    ic += yazi_tr(14, 78, '2. Kız (صَدِيقَتِي)', MOR, 'start')
    ic += yazi_ar(230, 90, 'زَيْنَبُ تُحِبُّ الرِّيَاضَةَ وَلٰكِنْ ___ نَادِيَ الْمُوسِيقَى', LAC)
    return svg(360, 110, ic, 'Erkek ve kız arkadaş tanıtımında muzari fiil uyumu kartı.', 14)


def okul_ev_sorumluluk_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Görev', MAVI, 'start')
    ic += yazi_ar(218, 27, 'الْحِفَاظُ عَلَى نَظَافَةِ الصَّفِّ', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Görev', YES, 'start')
    ic += yazi_ar(218, 63, 'مُسَاعَدَةُ الْوَالِدَيْنِ فِي الْبَيْتِ', LAC)

    ic += kutu(4, 76, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 96, '3. Görev', TUR, 'start')
    ic += yazi_ar(218, 99, 'الاِسْتِمَاعُ إِلَى الْمُدَرِّسِ فِي الدَّرْسِ', LAC)
    return svg(360, 112, ic, 'Okul ve ev sorumlulukları üçlü kartı.', 14)


def dort_ogrenci_tercih_tablosu():
    ic = kutu(4, 4, 172, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, 'Furkan (وَلِذٰلِكَ)', MAVI)
    ic += yazi_ar(90, 44, 'الْكُتُبُ - نَادِي الْمَكْتَبَةِ', LAC)

    ic += kutu(184, 4, 172, 48, MOR_A, MOR, 8)
    ic += yazi_tr(270, 20, 'Zeynep (وَلٰكِنْ)', MOR)
    ic += yazi_ar(270, 44, 'الرِّيَاضَةُ - نَادِي الْمُوسِيقَى', LAC)

    ic += kutu(4, 58, 172, 48, YES_A, YES, 8)
    ic += yazi_tr(90, 74, 'Hasan (وَلٰكِنْ)', YES)
    ic += yazi_ar(90, 98, 'الشَّطْرَنْجُ - نَادِي الطَّبِيعَةِ', LAC)

    ic += kutu(184, 58, 172, 48, TUR_A, TUR, 8)
    ic += yazi_tr(270, 74, 'Kerem (وَلٰكِنْ)', TUR)
    ic += yazi_ar(270, 98, 'الرَّسْمُ - نَادِي التِّكْنُولُوجِيَا', LAC)
    return svg(360, 110, ic, 'Dört öğrencinin sevdiği etkinlik ve seçtiği kulüp tablosu.', 14)


def kulup_tahmin_diyalogu():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, 'Soru', MAVI, 'start')
    ic += yazi_ar(220, 27, 'هَلْ أَنْتَ مَسْؤُولٌ عَنْ تَرْتِيبِ الْكُتُبِ؟', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, 'Onay', YES, 'start')
    ic += yazi_ar(220, 63, 'نَعَمْ، صَحِيحٌ!', LAC)

    ic += kutu(4, 76, 352, 32, SARI_A, TUR, 7)
    ic += yazi_tr(14, 96, 'Çıkarım', TUR, 'start')
    ic += yazi_ar(220, 99, 'إِذَنْ، أَنْتَ عُضْوٌ فِي ... ؟', KIR)
    return svg(360, 112, ic, 'Görevden kulüp tahmin etme diyaloğu.', 14)


def merve_neden_karti():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Soru (لِمَاذَا)', TUR, 'start')
    ic += yazi_ar(224, 36, 'لِمَاذَا تَخْتَارُ مَرْوَةُ نَادِيَ الرَّسْمِ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Cevap (لِأَنَّهَا)', YES, 'start')
    ic += yazi_ar(224, 90, 'لِأَنَّهَا تُحِبُّ الرَّسْمَ', LAC)
    return svg(360, 110, ic, 'Merve neden resim kulübünü seçiyor sorusu ve liennehâ cevabı.', 14)


def gunluk_sorumluluk_akisi():
    adimlar = [
        (4, '1. Sabah', 'أَسْتَيْقِظُ مُبَكِّرًا', MOR, MOR_A),
        (93, '2. Ders', 'أَسْتَمِعُ وَأَحْتَرِمُ', MAVI, MAVI_A),
        (182, '3. Yardım', 'أُسَاعِدُ أُمِّي وَأَبِي', YES, YES_A),
        (271, '4. Akşam', 'أَدْرُسُ كُلَّ مَسَاءٍ', TUR, TUR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Sabahtan akşama günlük sorumlulukların dört aşamalı akışı.', 14)


def ve_em_baglac_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Cümle (وَ)', MAVI, 'start')
    ic += yazi_ar(222, 36, 'أُحِبُّ الشَّطْرَنْجَ وَكُرَةَ السَّلَّةِ', LAC)

    ic += kutu(4, 58, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Soru (أَمْ)', TUR, 'start')
    ic += yazi_ar(222, 90, 'أَتُفَضِّلُ نَادِيَ الْمَسْرَحِيَّةِ أَمْ نَادِيَ الرَّسْمِ؟', LAC)
    return svg(360, 110, ic, 'Olumlu cümlede ve bağlacı ile seçim sorusunda em bağlacı kartı.', 14)


def aksam_ev_rutini_karti():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, 'Okuldaki Görevim', MAVI)
    ic += yazi_ar(90, 56, 'أُحَافِظُ عَلَى نَظَافَةِ', LAC)
    ic += yazi_ar(90, 86, 'مَدْرَسَتِي وَصَفِّي', LAC)

    ic += kutu(184, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(270, 24, 'Akşam Evdeki Görevim', YES)
    ic += yazi_ar(270, 56, 'أَدْرُسُ كُلَّ مَسَاءٍ', LAC)
    ic += yazi_ar(270, 86, 'وَأُرَتِّبُ غُرْفَتِي', LAC)
    return svg(360, 106, ic, 'Okuldaki ve akşam evdeki sorumlulukları gösteren okuma kartı.', 14)


def kerem_sumeyye_ipuclari():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. صَدِيقِي كَرَم (Erkek)', MAVI)
    ic += yazi_ar(90, 56, 'يُحِبُّ الرَّسْمَ', LAC)
    ic += yazi_ar(90, 86, 'نَادِي التِّكْنُولُوجِيَا', LAC)

    ic += kutu(184, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(270, 24, '2. صَدِيقَتِي سُمَيَّةُ (Kız)', MOR)
    ic += yazi_ar(270, 56, 'تُحِبُّ الشَّطْرَنْجَ', LAC)
    ic += yazi_ar(270, 86, 'نَادِي الْمَكْتَبَةِ', LAC)
    return svg(360, 106, ic, 'Kerem ve Sümeyye için lâkin bağlacıyla cümle kurma ipuçları.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = arkadas_fiil_uyumu_karti()
    s[2]['gorsel'] = okul_ev_sorumluluk_kartlari()
    s[3]['gorsel'] = dort_ogrenci_tercih_tablosu()
    s[5]['gorsel'] = kulup_tahmin_diyalogu()
    s[7]['gorsel'] = merve_neden_karti()
    s[8]['gorsel'] = gunluk_sorumluluk_akisi()
    s[9]['gorsel'] = ve_em_baglac_karti()
    s[11]['gorsel'] = aksam_ev_rutini_karti()
    s[12]['gorsel'] = kerem_sumeyye_ipuclari()
