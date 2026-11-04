"""8. sınıf Arapça 3. hafta (1. Ünite: Etkinlikler — 2. Ders: Tiyatro, Saatler, Bağlaçlar ve Yön Tarifleri) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def tiyatro_bilet_karti():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(95, 24, 'Okul Tiyatrosu Giriş Bileti', MOR)
    ic += yazi_ar(265, 28, 'تَذْكِرَةُ الْمَسْرَحِ', LAC)

    ic += kutu(4, 42, 172, 64, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 60, 'Gösteri Salonu', MAVI)
    ic += yazi_ar(90, 94, 'صَالَةُ الْمَسْرَحِ', LAC)

    ic += kutu(184, 42, 172, 64, TUR_A, TUR, 8)
    ic += yazi_tr(270, 60, 'Başlama Saati', TUR)
    ic += yazi_ar(270, 94, 'السَّادِسَةُ إِلَّا رُبْعًا', LAC)
    return svg(360, 110, ic, 'Tiyatro bileti: Saletü’l-mesrah, başlama saati es-sâdisetü illâ rub’an (05.45).', 15)


def saat_kaliplari_kartlari():
    ic = kutu(4, 4, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 24, '1. Kart (Buçuk)', YES, 'start')
    ic += yazi_ar(230, 27, 'السَّاعَةُ الرَّابِعَةُ وَالنِّصْفُ', LAC)

    ic += kutu(4, 40, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 60, '2. Kart (Çeyrek Geçe)', MAVI, 'start')
    ic += yazi_ar(230, 63, 'السَّاعَةُ السَّادِسَةُ وَالرُّبْعُ', LAC)

    ic += kutu(4, 76, 352, 32, KIR_A, KIR, 7)
    ic += yazi_tr(14, 96, '3. Kart (Çeyrek Var)', KIR, 'start')
    ic += yazi_ar(230, 99, 'السَّاعَةُ السَّادِسَةُ إِلَّا رُبْعًا', LAC)
    return svg(360, 112, ic, 'Üç saat kartı: 04.30, 06.15 ve 05.45.', 15)


def yol_tarifi_krokisi():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, 'Soru', MAVI, 'start')
    ic += yazi_ar(224, 27, 'كَيْفَ أَذْهَبُ إِلَى نَادِي الرِّيَاضَةِ؟', LAC)

    ic += kutu(4, 42, 112, 64, YES_A, YES, 8)
    ic += yazi_tr(60, 60, '1. Adım', YES)
    ic += yazi_ar(60, 92, 'اِعْبُرِ الطَّرِيقَ', LAC)

    ic += kutu(124, 42, 112, 64, TUR_A, TUR, 8)
    ic += yazi_tr(180, 60, '2. Adım', TUR)
    ic += yazi_ar(180, 92, 'اِتَّجِهْ نَحْوَ الْيَمِينِ', LAC)

    ic += kutu(244, 42, 112, 64, MOR_A, MOR, 8)
    ic += yazi_tr(300, 60, '3. Konum', MOR)
    ic += yazi_ar(300, 92, 'قَرِيبَةٌ مِنْ هُنَا', LAC)
    return svg(360, 110, ic, 'Spor kulübüne yol tarifi: Karşıya geç, sağa yönel, buraya yakındır.', 15)


def sebep_sonuc_tiyatro_karti():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Cümle (Sebep)', MAVI)
    ic += yazi_ar(90, 58, 'أُحِبُّ التَّمْثِيلَ', LAC)
    ic += yazi_tr(90, 86, 'Oyunculuğu seviyorum', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Cümle (Sonuç)', YES)
    ic += yazi_ar(270, 58, '___ أَنَا فِي نَادِي الْمَسْرَحِ', LAC)
    ic += yazi_tr(270, 86, 'Tiyatro kulübündeyim', LAC, 'middle', False)
    return svg(360, 106, ic, 'Oyunculuğu seviyorum, bu yüzden tiyatro kulübündeyim kartı.', 15)


def sehir_konum_karti():
    ic = kutu(4, 4, 352, 48, MOR_A, MOR, 8)
    ic += yazi_tr(14, 24, 'Niteleme', MOR, 'start')
    ic += yazi_ar(224, 36, 'إِسْطَنْبُولُ مَدِينَةٌ جَمِيلَةٌ وَتَارِيخِيَّةٌ', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Konum', YES, 'start')
    ic += yazi_ar(224, 90, 'تَقَعُ مَدِينَةُ أَنْقَرَةَ فِي مِنْطَقَةِ وَسَطِ الأَنَاضُولِ', LAC)
    return svg(360, 110, ic, 'İstanbul ve Ankara şehir tanıtım ve coğrafi konum kartı.', 15)


def tiyatro_ulasim_akisi():
    adimlar = [
        (4, '1. Soru', 'كَيْفَ أَذْهَبُ؟', MAVI, MAVI_A),
        (93, '2. Yön', 'عَبَرَ الطَّرِيقَ', YES, YES_A),
        (182, '3. Bilet', 'اِشْتَرَى تَذْكِرَةً', TUR, TUR_A),
        (271, '4. Sahne', 'خَشَبَةُ الْمَسْرَحِ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Tiyatroya ulaşım, bilet alma ve oyunu izleme dört aşamalı şeması.', 15)


def baglac_karsilastirma_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Cümle (لِأَنَّهُ)', MAVI, 'start')
    ic += yazi_ar(226, 36, 'أُحِبُّ الْمَسْرَحَ لِأَنَّهُ مُمْتِعٌ', LAC)

    ic += kutu(4, 58, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Cümle (إِذَنْ)', TUR, 'start')
    ic += yazi_ar(226, 90, 'إِذَنْ نَذْهَبُ مَعًا إِلَى الْمَسْرَحِ', LAC)
    return svg(360, 110, ic, 'Liennehu ile sebep ve izen ile karar bildiren iki cümle kartı.', 15)


def salon_soru_edatlari_karti():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, '1. Kişi Sorusu', YES, 'start')
    ic += yazi_ar(228, 36, '___ فِي صَالَةِ الْمَسْرَحِ؟ — الْمُمَثِّلُ', LAC)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Nesne Sorusu', TUR, 'start')
    ic += yazi_ar(228, 90, '___ تُشَاهِدُ؟ — أُشَاهِدُ مَسْرَحِيَّةً', LAC)
    return svg(360, 110, ic, 'Salonda kim var ve ne izliyorsun diyalog kartı.', 15)


def tiyatro_etkinlik_plani_karti():
    ic = kutu(4, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, 'Sevgi ve Sebep (لِأَنَّهُ)', MOR)
    ic += yazi_ar(90, 56, 'أُحِبُّ الْمَسْرَحَ', LAC)
    ic += yazi_ar(90, 86, 'لِأَنَّهُ مُمْتِعٌ', LAC)

    ic += kutu(184, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, 'Oyun Başlama Saati', MAVI)
    ic += yazi_ar(270, 56, 'تَبْدَأُ الْمَسْرَحِيَّةُ', LAC)
    ic += yazi_ar(270, 86, 'الرَّابِعَةُ وَالنِّصْفُ', LAC)
    return svg(360, 106, ic, 'Tiyatro sevgisi sebebi ve saat dört buçukta başlama kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tiyatro_bilet_karti()
    s[2]['gorsel'] = saat_kaliplari_kartlari()
    s[3]['gorsel'] = yol_tarifi_krokisi()
    s[5]['gorsel'] = sebep_sonuc_tiyatro_karti()
    s[7]['gorsel'] = sehir_konum_karti()
    s[8]['gorsel'] = tiyatro_ulasim_akisi()
    s[9]['gorsel'] = baglac_karsilastirma_karti()
    s[11]['gorsel'] = salon_soru_edatlari_karti()
    s[12]['gorsel'] = tiyatro_etkinlik_plani_karti()
