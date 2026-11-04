"""8. sınıf Arapça 7. hafta (3. Ünite: Kültür ve Sanat — 1. Ders: Edebiyat, Edebî Türler ve Okuma Tercihleri) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def edebiyat_kulubu_panosu():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(95, 24, 'Edebiyat Kulübü Panosu', MOR)
    ic += yazi_ar(265, 28, 'نَادِي الأَدَبِ', LAC)

    ic += kutu(4, 42, 172, 64, TUR_A, TUR, 8)
    ic += yazi_tr(90, 60, '1. Eser (الشِّعْرُ)', TUR)
    ic += yazi_ar(90, 94, 'قَصِيدَةُ حُبِّ الْوَطَنِ', LAC)

    ic += kutu(184, 42, 172, 64, YES_A, YES, 8)
    ic += yazi_tr(270, 60, '2. Eser (النَّثْرُ)', YES)
    ic += yazi_ar(270, 94, 'رِوَايَةٌ تَارِيخِيَّةٌ', LAC)
    return svg(360, 110, ic, 'Edebiyat kulübü panosu: 1. Vatan kasidesi/şiiri, 2. Tarihî roman.', 15)


def tekil_cogul_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(224, 27, 'قِصَّةٌ - قِصَصٌ', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Kart', YES, 'start')
    ic += yazi_ar(224, 63, 'رِوَايَةٌ - رِوَايَاتٌ', LAC)

    ic += kutu(4, 76, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 96, '3. Kart', TUR, 'start')
    ic += yazi_ar(224, 99, 'شَاعِرٌ - شُعَرَاءُ', LAC)
    return svg(360, 112, ic, 'Kıssa-kısas, rivâye-rivâyât ve şâir-şuarâ tekil çoğul kartları.', 15)


def dergi_yazarlari_panosu():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Fatma', MAVI, 'start')
    ic += yazi_ar(224, 27, 'فَاطِمَةُ تَكْتُبُ مَقَالَةً فِي مَجَلَّةِ الْمَدْرَسَةِ', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Ahmet', YES, 'start')
    ic += yazi_ar(224, 63, 'أَحْمَدُ يُحِبُّ قِرَاءَةَ الرِّوَايَاتِ التَّارِيخِيَّةِ', LAC)

    ic += kutu(4, 76, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(14, 96, '3. Zeynep', MOR, 'start')
    ic += yazi_ar(224, 99, 'زَيْنَبُ تَكْتُبُ قَصِيدَةً عَنْ حُبِّ الْوَطَنِ', LAC)
    return svg(360, 112, ic, 'Fatma, Ahmet ve Zeynep’in edebî etkinlik kartları.', 15)


def istiklal_marsi_sairi_karti():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Soru', TUR, 'start')
    ic += yazi_ar(224, 36, '___ نَشِيدِ الاِسْتِقْلَالِ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Cevap', YES, 'start')
    ic += yazi_ar(224, 90, 'شَاعِرُهُ هُوَ مُحَمَّد عَاكِف أَرْصُوي', LAC)
    return svg(360, 110, ic, 'İstiklal Marşı’nın şairi kimdir sorusu ve Mehmet Akif Ersoy cevabı.', 15)


def kerim_okuma_diyalogu():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Soru (تَقْرَأُ)', MAVI, 'start')
    ic += yazi_ar(224, 36, 'مَاذَا تَقْرَأُ يَا كَرِيمُ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Kerim (أَقْرَأُ)', YES, 'start')
    ic += yazi_ar(224, 90, 'أَقْرَأُ رِوَايَةً تَارِيخِيَّةً مُمْتِعَةً', LAC)
    return svg(360, 110, ic, 'Ne okuyorsun Kerim sorusu ve tarihî roman okuyorum cevabı.', 15)


def edebiyat_kulubu_akisi():
    adimlar = [
        (4, '1. Üyelik', 'نَادِي الأَدَبِ', MOR, MOR_A),
        (93, '2. Okuma', 'أَقْرَأُ كِتَابًا', MAVI, MAVI_A),
        (182, '3. Yazma', 'أَكْتُبُ قَصِيدَةً', TUR, TUR_A),
        (271, '4. Dergi', 'مَجَلَّةُ الْمَدْرَسَةِ', YES, YES_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Edebiyat kulübü üyeliği, okuma, yazma ve okul dergisi akış şeması.', 15)


def tercih_edebi_karsilastirma():
    ic = kutu(4, 4, 352, 48, MOR_A, MOR, 8)
    ic += yazi_tr(14, 24, 'Tercih (أُفَضِّلُ)', MOR, 'start')
    ic += yazi_ar(226, 36, 'أُفَضِّلُ الرِّوَايَاتِ التَّارِيخِيَّةَ', LAC)

    ic += kutu(4, 58, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 78, 'Karşılaştırma (عَلَى)', MAVI, 'start')
    ic += yazi_ar(226, 90, 'عَلَى الرِّوَايَاتِ البُولِيسِيَّةِ', LAC)
    return svg(360, 110, ic, 'Tarihî romanları polisiye romanlara tercih ederim kartı.', 15)


def kitap_yazari_soru_karti():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, 'Soru (مَنْ)', YES, 'start')
    ic += yazi_ar(224, 36, '؟', KIR)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Cevap (الْكَاتِبُ)', TUR, 'start')
    ic += yazi_ar(224, 90, 'كَاتِبُ هٰذَا الْكِتَابِ أَدِيبٌ مَشْهُورٌ', LAC)
    return svg(360, 110, ic, 'Bu kitabın yazarı kimdir sorusu ve ünlü bir ediptir cevabı.', 15)


def edebiyat_kimlik_karti():
    ic = kutu(4, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, 'Kulüp ve Tercih', MOR)
    ic += yazi_ar(90, 56, 'عُضْوٌ فِي نَادِي الأَدَبِ', LAC)
    ic += yazi_ar(90, 86, 'الْقِصَصُ الْقَصِيرَةُ', LAC)

    ic += kutu(184, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, 'Okul Dergisi Yazısı', MAVI)
    ic += yazi_ar(270, 56, 'أَكْتُبُ شِعْرًا فِي', LAC)
    ic += yazi_ar(270, 86, 'مَجَلَّةِ الْمَدْرَسَةِ', LAC)
    return svg(360, 106, ic, 'Edebiyat kulübü üyeliği, kısa hikâye tercihi ve okul dergisinde şiir yazma kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = edebiyat_kulubu_panosu()
    s[2]['gorsel'] = tekil_cogul_kartlari()
    s[3]['gorsel'] = dergi_yazarlari_panosu()
    s[5]['gorsel'] = istiklal_marsi_sairi_karti()
    s[7]['gorsel'] = kerim_okuma_diyalogu()
    s[8]['gorsel'] = edebiyat_kulubu_akisi()
    s[9]['gorsel'] = tercih_edebi_karsilastirma()
    s[11]['gorsel'] = kitap_yazari_soru_karti()
    s[12]['gorsel'] = edebiyat_kimlik_karti()
