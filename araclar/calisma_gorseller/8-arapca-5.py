"""8. sınıf Arapça 5. hafta (1. Ünite: Etkinlikler — 3. Ders: Gezi, Geçmiş-Şimdiki Zaman Kalıpları ve Tefekkür) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def gezi_turleri_afisi():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(95, 24, 'Hafta Sonu Etkinlik Panosu', MOR)
    ic += yazi_ar(265, 28, 'الرِّحْلَةُ وَالنُّزْهَةُ', LAC)

    ic += kutu(4, 42, 172, 64, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 60, '1. Etkinlik (الْمَتْحَفُ)', MAVI)
    ic += yazi_ar(90, 94, 'رِحْلَةٌ مَدْرَسِيَّةٌ', LAC)

    ic += kutu(184, 42, 172, 64, YES_A, YES, 8)
    ic += yazi_tr(270, 60, '2. Etkinlik (الْغَابَةُ)', YES)
    ic += yazi_ar(270, 94, 'نُزْهَةٌ فِي الطَّبِيعَةِ', LAC)
    return svg(360, 110, ic, 'Gezi afişi: 1. Okul gezisi (Müze), 2. Doğa gezintisi/piknik (Orman).', 15)


def mazi_muzari_gezi_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(224, 27, 'ذَهَبْنَا إِلَى الْمَتْحَفِ بِالْحَافِلَةِ', LAC)

    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(224, 63, 'سَنُنَظِّمُ رِحْلَةً عِلْمِيَّةً غَدًا', LAC)

    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(224, 99, 'اِلْتَقَطْنَا صُوَرًا جَمِيلَةً فِي الْغَابَةِ', LAC)
    return svg(360, 112, ic, 'Geçmiş ve gelecek zamanlı üç gezi cümlesi kartı.', 15)


def gezi_gunlugu_karti():
    ic = kutu(4, 4, 172, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, '1. Ulaşım (صَبَاحًا)', MAVI)
    ic += yazi_ar(90, 44, 'رَكِبْنَا الْحَافِلَةَ', LAC)

    ic += kutu(184, 4, 172, 48, MOR_A, MOR, 8)
    ic += yazi_tr(270, 20, '2. Ziyaret (الْمَتْحَفُ)', MOR)
    ic += yazi_ar(270, 44, 'شَاهَدْنَا الآثَارَ الْقَدِيمَةَ', LAC)

    ic += kutu(4, 58, 172, 48, YES_A, YES, 8)
    ic += yazi_tr(90, 74, '3. İzlenim', YES)
    ic += yazi_ar(90, 98, 'كَانَتِ الرِّحْلَةُ مُمْتِعَةً', LAC)

    ic += kutu(184, 58, 172, 48, TUR_A, TUR, 8)
    ic += yazi_tr(270, 74, '4. Dönüş (مَسَاءً)', TUR)
    ic += yazi_ar(270, 98, 'رَجَعْنَا إِلَى الْبَيْتِ', LAC)
    return svg(360, 110, ic, 'Dört bölümlü okul gezisi günlüğü kartı.', 15)


def ulasim_soru_diyalogu():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Soru', TUR, 'start')
    ic += yazi_ar(224, 36, '___ ذَهَبْتُمْ إِلَى الْمَتْحَفِ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Cevap (بِـ)', YES, 'start')
    ic += yazi_ar(224, 90, 'ذَهَبْنَا إِلَى الْمَتْحَفِ بِالْحَافِلَةِ', LAC)
    return svg(360, 110, ic, 'Müzeye nasıl gittiniz sorusu ve otobüsle gittik cevabı.', 15)


def tefekkur_cevre_karti():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Doğada Tefekkür', MAVI)
    ic += yazi_ar(90, 56, 'سُبْحَانَ اللَّهِ', LAC)
    ic += yazi_ar(90, 86, 'مَا أَجْمَلَ الطَّبِيعَةَ!', LAC)

    ic += kutu(184, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Çevre Temizliği', YES)
    ic += yazi_ar(270, 56, 'نُحَافِظُ عَلَى الْبِيئَةِ', LAC)
    ic += yazi_ar(270, 86, 'النَّظَافَةُ مِنَ الإِيمَانِ', LAC)
    return svg(360, 106, ic, 'Doğayı tefekkür etme ve çevreyi koruma kartı.', 15)


def gezi_akis_semasi():
    adimlar = [
        (4, '1. Hareket', 'رَكِبْنَا الْحَافِلَةَ', MAVI, MAVI_A),
        (93, '2. Müze', 'شَاهَدْنَا الْمَتْحَفَ', MOR, MOR_A),
        (182, '3. Orman', 'اِلْتَقَطْنَا صُوَرًا', YES, YES_A),
        (271, '4. Dönüş', 'رَجَعْنَا مَسَاءً', TUR, TUR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Okul gezisinin dört aşamalı sıralama şeması.', 15)


def mazi_gelecek_karsilastirma():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Cümle (ـْنَا)', MAVI, 'start')
    ic += yazi_ar(228, 36, 'تَجَوَّلْنَا فِي الْمَدِينَةِ التَّارِيخِيَّةِ', LAC)

    ic += kutu(4, 58, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Cümle (سَنَـ)', TUR, 'start')
    ic += yazi_ar(228, 90, 'سَنَذْهَبُ إِلَى إِسْطَنْبُولَ بِالْقِطَارِ', LAC)
    return svg(360, 110, ic, 'Geçmiş zaman (-nâ) ve gelecek zaman (sene-) karşılaştırma kartı.', 15)


def gezi_izlenim_diyalogu():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, '1. Soru', YES, 'start')
    ic += yazi_ar(224, 36, 'كَيْفَ كَانَتِ الرِّحْلَةُ يَا عُمَرُ؟', LAC)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Ömer', TUR, 'start')
    ic += yazi_ar(224, 90, '؟', KIR)
    return svg(360, 110, ic, 'Gezi nasıldı sorusu ve Ömer’in izlenim cevabı kartı.', 15)


def gezi_ozeti_ipuclari():
    ic = kutu(4, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, 'Ziyaret ve Ulaşım', MOR)
    ic += yazi_ar(90, 56, 'ذَهَبْنَا إِلَى الْمَتْحَفِ', LAC)
    ic += yazi_ar(90, 86, 'بِالْحَافِلَةِ', LAC)

    ic += kutu(184, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, 'Görülenler ve İzlenim', MAVI)
    ic += yazi_ar(270, 56, 'شَاهَدْنَا الآثَارَ', LAC)
    ic += yazi_ar(270, 86, 'كَانَتْ مُمْتِعَةً وَمُفِيدَةً', LAC)
    return svg(360, 106, ic, 'Müze gezisi ulaşım, görülen eserler ve izlenim kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gezi_turleri_afisi()
    s[2]['gorsel'] = mazi_muzari_gezi_kartlari()
    s[3]['gorsel'] = gezi_gunlugu_karti()
    s[5]['gorsel'] = ulasim_soru_diyalogu()
    s[7]['gorsel'] = tefekkur_cevre_karti()
    s[8]['gorsel'] = gezi_akis_semasi()
    s[9]['gorsel'] = mazi_gelecek_karsilastirma()
    s[11]['gorsel'] = gezi_izlenim_diyalogu()
    s[12]['gorsel'] = gezi_ozeti_ipuclari()
