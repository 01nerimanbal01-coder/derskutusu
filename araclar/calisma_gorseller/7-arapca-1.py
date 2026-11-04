"""7. sınıf Arapça 1. hafta (1. Ünite: Meslekler — 1. Ders: Mesleğin Nedir?) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=17):
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


def zaman_karsilastirma_kartlari():
    ic = kutu(4, 6, 172, 98, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Kart (Şimdiki Durum)', MAVI)
    ic += yazi_ar(90, 60, 'أَنَا خَبَّازٌ', LAC)
    ic += yazi_tr(90, 90, 'Ben fırıncıyım.', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 98, TUR_A, TUR, 8)
    ic += yazi_tr(270, 24, '2. Kart (Gelecek Hedefi)', TUR)
    ic += yazi_ar(270, 60, 'سَأَكُونُ طَيَّارًا', LAC)
    ic += yazi_tr(270, 90, 'Pilot olacağım.', LAC, 'middle', False)
    return svg(360, 110, ic, 'İki meslek tanıtım kartı: Şimdiki durum ve gelecek hedefi.', 17)


def meslek_soru_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(220, 27, 'مَا مِهْنَتُكَ؟', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(220, 63, 'مَا مِهْنَتُكِ؟', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(220, 99, 'مَا مِهْنَةُ وَالِدِكَ؟', LAC)
    return svg(360, 112, ic, 'Üç meslek soru kartı: Erkeğe, kadına ve babaya yönelik sorular.', 17)


def aile_meslek_panosu():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, 'Baba (أَبِي)', MAVI)
    ic += yazi_ar(90, 62, 'أَبِي شُرْطِيٌّ', LAC)
    ic += yazi_tr(90, 88, 'Güvenlik Görevlisi', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(270, 24, 'Anne (أُمِّي)', YES)
    ic += yazi_ar(270, 62, 'أُمِّي مُمَرِّضَةٌ', LAC)
    ic += yazi_tr(270, 88, 'Sağlık Görevlisi', LAC, 'middle', False)
    return svg(360, 108, ic, 'Aile meslek panosu: Babam polistir, annem hemşiredir.', 17)


def zamir_uyum_kartlari():
    kartlar = [
        (4, 4, '1. Kart (Eril)', 'هُوَ خَبَّازٌ', MAVI, MAVI_A),
        (184, 4, '2. Kart (Dişil)', 'هِيَ خَيَّاطَةٌ', YES, YES_A),
        (4, 60, '3. Kart (Uyumsuz)', 'هُوَ مُمَرِّضَةٌ', KIR, KIR_A),
        (184, 60, '4. Kart (Dişil)', 'هِيَ مُذِيعَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Dört zamir ve meslek uyum kartı.', 17)


def muhatap_soru_balonlari():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Balon (Erkek Muhatap)', MAVI)
    ic += yazi_ar(90, 62, 'مَا مِهْنَتُكَ؟', LAC)
    ic += yazi_tr(90, 88, 'Son ek: ـكَ', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, MOR_A, MOR, 8)
    ic += yazi_tr(270, 24, '2. Balon (Kadın Muhatap)', MOR)
    ic += yazi_ar(270, 62, 'مَا مِهْنَتُكِ؟', LAC)
    ic += yazi_tr(270, 88, 'Son ek: ـكِ', LAC, 'middle', False)
    return svg(360, 108, ic, 'Erkek ve kadın muhataba göre meslek sorma balonları.', 17)


def diyalog_adimlari_sema():
    adimlar = [
        (4, '1. Soru', 'مِهْنَةُ الْوَالِدِ؟', MAVI, MAVI_A),
        (93, '2. Cevap', 'أَبِي نَجَّارٌ', YES, YES_A),
        (182, '3. Hedef', 'فِي الْمُسْتَقْبَلِ؟', TUR, TUR_A),
        (271, '4. İstek', 'سَأَكُونُ طَيَّارًا', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 100, ic, 'Meslek diyaloğunun dört aşamalı akış şeması.', 17)


def eylem_gorev_panosu():
    eylemler = [
        (4, '1. Eylem Kartı', 'أَصْنَعُ الْأَثَاثَ', MAVI, MAVI_A),
        (124, '2. Eylem Kartı', 'أَبِيعُ اللَّحْمَ', YES, YES_A),
        (244, '3. Eylem Kartı', 'أُصْلِحُ السَّيَّارَةَ', TUR, TUR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(eylemler):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 104, ic, 'Üç meslek eylem kartı: Mobilya yaparım, et satarım, araba tamir ederim.', 17)


def baglac_cumle_karti():
    ic = kutu(4, 6, 352, 96, SARI_A, TUR, 8)
    ic += yazi_tr(180, 26, 'İki Kişinin Mesleğini Birleştirme', TUR)
    ic += yazi_ar(180, 62, 'أَبِي نَجَّارٌ ___ أَخِي خَبَّازٌ', LAC)
    ic += yazi_tr(180, 88, 'Babam marangozdur ... kardeşim fırıncıdır.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Bağlaç tamamlama kartı: Babam marangozdur ve kardeşim fırıncıdır.', 17)


def tanitim_fisi_pano():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Bilgi: Baba', MAVI)
    ic += yazi_ar(90, 62, 'أَبِي · خَبَّازٌ', LAC)
    ic += yazi_tr(90, 88, 'Babam fırıncıdır', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Bilgi: Gelecek Hedefi', YES)
    ic += yazi_ar(270, 62, 'سَأَكُونُ · طَيَّارًا', LAC)
    ic += yazi_tr(270, 88, 'Gelecekte pilot olacağım', LAC, 'middle', False)
    return svg(360, 108, ic, 'Tanıtım fişi: Baba fırıncı, gelecek hedefi pilot.', 17)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = zaman_karsilastirma_kartlari()
    s[2]['gorsel'] = meslek_soru_kartlari()
    s[3]['gorsel'] = aile_meslek_panosu()
    s[5]['gorsel'] = zamir_uyum_kartlari()
    s[7]['gorsel'] = muhatap_soru_balonlari()
    s[8]['gorsel'] = diyalog_adimlari_sema()
    s[9]['gorsel'] = eylem_gorev_panosu()
    s[11]['gorsel'] = baglac_cumle_karti()
    s[12]['gorsel'] = tanitim_fisi_pano()
