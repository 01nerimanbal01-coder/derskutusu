"""7. sınıf Arapça 4. hafta (1. Ünite: Meslekler — Gelecekteki Mesleğim, Bağlaçlar ve Değerler) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=16):
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


def em_ev_baglac_kartlari():
    ic = kutu(4, 6, 172, 98, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Kart (Soru Cümlesi)', MAVI)
    ic += yazi_ar(90, 60, 'هَلْ أَخُوكَ طَبِيبٌ ___ مُهَنْدِسٌ؟', LAC)
    ic += yazi_tr(90, 90, 'Doktor mu ... mühendis mi?', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 98, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Kart (Düz Cümle)', YES)
    ic += yazi_ar(270, 60, 'سَأَكُونُ طَيَّارًا ___ مُهَنْدِسًا', LAC)
    ic += yazi_tr(270, 90, 'Pilot ... mühendis olacağım.', LAC, 'middle', False)
    return svg(360, 110, ic, 'Soru cümlesinde em ve düz cümlede ev bağlaç kartları.', 16)


def duz_soru_cumle_panosu():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(220, 27, 'أَنْتَ تُحِبُّ مِهْنَةَ التَّدْرِيسِ', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(220, 63, 'هَلْ تُحِبُّ مِهْنَةَ التَّدْرِيسِ؟', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(220, 99, 'مَاذَا سَتُصْبِحُ فِي الْمُسْتَقْبَلِ؟', LAC)
    return svg(360, 112, ic, 'Düz cümle ve soru cümlesi karşılaştırma kartları.', 16)


def mansub_hareke_kartlari():
    kartlar = [
        (4, 4, '1. Kart (Doğru)', 'سَأَكُونُ مُهَنْدِسًا', MAVI, MAVI_A),
        (184, 4, '2. Kart (Doğru)', 'سَأُصْبِحُ طَبِيبَةً', YES, YES_A),
        (4, 60, '3. Kart (Hatalı Hareke)', 'سَأَكُونُ مُدَرِّسٌ', KIR, KIR_A),
        (184, 60, '4. Kart (Doğru)', 'سَأُصْبِحُ طَيَّارًا', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Se-ekûnü ve se-usbıhu sonrası mansub hareke kartları.', 16)


def astronot_tepki_diyalogu():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Ali', MAVI, 'start')
    ic += yazi_ar(220, 36, 'سَأُصْبِحُ رَائِدَ فَضَاءٍ إِنْ شَاءَ اللّٰهُ', LAC)
    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Hasan', TUR, 'start')
    ic += yazi_ar(220, 90, '؟ — هٰذِهِ مِهْنَةٌ رَائِعَةٌ!', KIR)
    return svg(360, 110, ic, 'Ali astronot olacağını söyler, Hasan hayranlıkla karşılık verir.', 16)


def isaret_kisi_zamir_kartlari():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Kart (Eril Uyumu)', MAVI)
    ic += yazi_ar(90, 60, 'هٰذَا أَبِي، هُوَ شُرْطِيٌّ', LAC)
    ic += yazi_tr(90, 88, 'Bu babamdır, o polistir.', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, MOR_A, MOR, 8)
    ic += yazi_tr(270, 24, '2. Kart (Dişil Uyumu)', MOR)
    ic += yazi_ar(270, 60, 'هٰذِهِ أُمِّي، هِيَ مُمَرِّضَةٌ', LAC)
    ic += yazi_tr(270, 88, 'Bu annemdir, o hemşiredir.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Eril ve dişil işaret-kişi zamiri uyum kartları.', 16)


def vlog_akis_sema():
    adimlar = [
        (4, '1. Kendisi', 'أَنَا طَالِبٌ', MAVI, MAVI_A),
        (93, '2. Ailesi', 'أَبِي وَأُمِّي', YES, YES_A),
        (182, '3. Gayret', 'أَدْرُسُ ثُمَّ أَتَوَكَّلُ', TUR, TUR_A),
        (271, '4. Hedef', 'سَأُصْبِحُ طَبِيبًا', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 100, ic, 'Ahmet’in vlog tanıtım konuşmasının dört aşaması.', 16)


def degerler_panosu():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Saygı', MAVI, 'start')
    ic += yazi_ar(225, 27, 'الطَّالِبُ يَحْتَرِمُ الْمُدَرِّسَ', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Azim', TUR, 'start')
    ic += yazi_ar(225, 63, 'الطَّالِبُ عَازِمٌ عَلَى النَّجَاحِ', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Tevekkül', YES, 'start')
    ic += yazi_ar(225, 99, 'الْمُسْلِمُ يَتَوَكَّلُ عَلَى اللّٰهِ', LAC)
    return svg(360, 112, ic, 'Saygı, azim ve tevekkül değerlerini anlatan üç Arapça ilke.', 16)


def summe_siralama_karti():
    ic = kutu(4, 6, 352, 96, TUR_A, TUR, 8)
    ic += yazi_tr(180, 24, 'Zaman Aralıklı Sıralama Bağlacı', TUR)
    ic += yazi_ar(180, 60, 'أَدْرُسُ دُرُوسِي ___ أَنَامُ', LAC)
    ic += yazi_tr(180, 88, 'Derslerime çalışırım, ... uyurum.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Sıralama bağlacı cümle tamamlama kartı.', 16)


def agabey_ve_secenek_hedef_pano():
    kartlar = [
        (4, '1. Ağabey', 'أَخِي الْكَبِيرُ · مُهَنْدِسٌ', MAVI, MAVI_A),
        (124, '2. Gelecek', 'سَأَكُونُ فِي الْمُسْتَقْبَلِ', YES, YES_A),
        (244, '3. Seçenek (أَوْ)', 'طَبِيبًا أَوْ صَيْدَلِيًّا', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(kartlar):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 104, ic, 'Ağabeyin mühendisliği ve gelecekte doktor veya eczacı olma hedefi.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = em_ev_baglac_kartlari()
    s[2]['gorsel'] = duz_soru_cumle_panosu()
    s[3]['gorsel'] = mansub_hareke_kartlari()
    s[5]['gorsel'] = astronot_tepki_diyalogu()
    s[7]['gorsel'] = isaret_kisi_zamir_kartlari()
    s[8]['gorsel'] = vlog_akis_sema()
    s[9]['gorsel'] = degerler_panosu()
    s[11]['gorsel'] = summe_siralama_karti()
    s[12]['gorsel'] = agabey_ve_secenek_hedef_pano()
