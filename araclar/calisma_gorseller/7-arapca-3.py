"""7. sınıf Arapça 3. hafta (1. Ünite: Meslekler — 2. Ders: Öğretmenim) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


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


def bifadlihi_kazanim_kartlari():
    kartlar = [
        (4, 4, '1. الرِّيَاضِيَّاتُ', 'بِفَضْلِهِ أَتَعَلَّمُ الْحِسَابَ', MAVI, MAVI_A),
        (184, 4, '2. الْعُلُومُ', 'بِفَضْلِهِ أَقُومُ بِتَجَارِبَ', YES, YES_A),
        (4, 60, '3. التَّارِيخُ (Hatalı)', 'بِفَضْلِهَا أَتَعَلَّمُ الْأَغَانِيَ', KIR, KIR_A),
        (184, 60, '4. الرَّسْمُ', 'بِفَضْلِهِ أَتَعَلَّمُ كَيْفَ أَرْسُمُ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Dört branş öğretmeni ve kazanım eşleştirme kartı.', 15)


def esatizetuna_okuma_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, 'Selma', MAVI, 'start')
    ic += yazi_ar(220, 27, 'مُدَرِّسَةٌ نَشِيطَةٌ · دَرْسُهَا مُمْتِعٌ جِدًّا', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, 'Leyla', TUR, 'start')
    ic += yazi_ar(220, 63, 'مُدَرِّسٌ طَيِّبٌ · دَرْسُهُ صَعْبٌ وَلٰكِنْ نُحِبُّ', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, 'Ahmed', YES, 'start')
    ic += yazi_ar(220, 99, 'مُدَرِّسٌ مُخْلِصٌ · نَقُومُ بِتَجَارِبَ عِلْمِيَّةٍ', LAC)
    return svg(360, 112, ic, 'Hocalarımız okuma metninden üç öğrenci tanıtım kartı.', 15)


def ders_programi_panosu():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Şube Yanıtı', MAVI)
    ic += yazi_ar(90, 60, 'نَدْرُسُ مَادَّةَ الرِّيَاضِيَّاتِ', LAC)
    ic += yazi_tr(90, 88, 'Sınıfta (فِي الصَّفِّ)', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Şube Yanıtı', YES)
    ic += yazi_ar(270, 60, 'نَدْرُسُ مَادَّةَ الرِّيَاضَةِ', LAC)
    ic += yazi_tr(270, 88, 'Salonda (فِي صَالَةِ الرِّيَاضَةِ)', LAC, 'middle', False)
    return svg(360, 108, ic, 'İki şubenin işlediği dersleri gösteren pano.', 15)


def sinif_ici_ifade_balonlari():
    balonlar = [
        (4, 4, '1. Balon', 'أَسْتَمِعُ إِلَى الْمُدَرِّسِ', MAVI, MAVI_A),
        (184, 4, '2. Balon', 'آسِفٌ لِأَنَّنِي تَأَخَّرْتُ', KIR, KIR_A),
        (4, 60, '3. Balon', 'أَكْتُبُ وَاجِبَاتِي كُلَّ يَوْمٍ', YES, YES_A),
        (184, 60, '4. Balon', 'نَتَكَلَّمُ الْعَرَبِيَّةَ فَقَطْ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in balonlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Sınıf içi dört günlük konuşma ve özür balonu.', 15)


def riyada_riyadiyyat_farki():
    ic = kutu(4, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(90, 24, '1. Ders Kartı (Tekil)', YES)
    ic += yazi_ar(90, 60, 'مَادَّةُ الرِّيَاضَةِ', LAC)
    ic += yazi_tr(90, 88, 'Spor Salonu Dersi', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, TUR_A, TUR, 8)
    ic += yazi_tr(270, 24, '2. Ders Kartı (Çoğul)', TUR)
    ic += yazi_ar(270, 60, 'مَادَّةُ الرِّيَاضِيَّاتِ', LAC)
    ic += yazi_tr(270, 88, 'Hesap ve Sayılar Dersi', LAC, 'middle', False)
    return svg(360, 108, ic, 'Er-riyâda ve er-riyâdiyyât ders kartları.', 15)


def koridor_diyalog_sema():
    adimlar = [
        (4, '1. Soru', 'أَيَّ مَادَّةٍ؟', MAVI, MAVI_A),
        (93, '2. Ders', 'مَادَّةَ الْعُلُومِ', YES, YES_A),
        (182, '3. Kazanım', 'بِفَضْلِ الْمُدَرِّسِ؟', TUR, TUR_A),
        (271, '4. Deney', 'تَجَارِبَ عِلْمِيَّةٍ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 100, ic, 'Ders ve laboratuvar diyaloğu akış şeması.', 15)


def ilim_ozdeyisleri_panosu():
    ic = kutu(4, 4, 352, 48, MOR_A, MOR, 8)
    ic += yazi_tr(14, 24, '1. Özdeyiş', MOR, 'start')
    ic += yazi_ar(220, 36, 'مَنْ عَلَّمَنِي حَرْفًا صِرْتُ لَهُ عَبْدًا', LAC)
    ic += kutu(4, 58, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 78, '2. Özdeyiş', MAVI, 'start')
    ic += yazi_ar(220, 90, 'اُطْلُبُوا الْعِلْمَ مِنَ الْمَهْدِ إِلَى اللَّحْدِ', LAC)
    return svg(360, 110, ic, 'İlim ve öğretmene vefa konulu iki Arapça özdeyiş panosu.', 15)


def arapca_ogretmeni_zamir_karti():
    ic = kutu(4, 6, 352, 96, SARI_A, TUR, 8)
    ic += yazi_tr(180, 24, 'Kadın Öğretmen İçin Zamir Uyumu', TUR)
    ic += yazi_ar(180, 60, 'أُحِبُّ مُدَرِّسَةَ اللُّغَةِ الْعَرَبِيَّةِ، ___ أَتَعَلَّمُ الْمُحَادَثَةَ', LAC)
    ic += yazi_tr(180, 88, 'Arapça öğretmenini seviyorum, ... konuşmayı öğreniyorum.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Kadın Arapça öğretmeni sayesinde konuşma öğrenme cümle kartı.', 15)


def fen_deney_ipucu_kartlari():
    kartlar = [
        (4, '1. Sevgi', 'أُحِبُّ مُدَرِّسَ الْعُلُومِ', MAVI, MAVI_A),
        (124, '2. Bağlantı', 'بِفَضْلِهِ أَتَعَلَّمُ', YES, YES_A),
        (244, '3. Kazanım', 'تَجَارِبَ عِلْمِيَّةٍ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(kartlar):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 104, ic, 'Fen bilimleri öğretmeni ve bilimsel deneyler ipucu kartları.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bifadlihi_kazanim_kartlari()
    s[2]['gorsel'] = esatizetuna_okuma_kartlari()
    s[3]['gorsel'] = ders_programi_panosu()
    s[5]['gorsel'] = sinif_ici_ifade_balonlari()
    s[7]['gorsel'] = riyada_riyadiyyat_farki()
    s[8]['gorsel'] = koridor_diyalog_sema()
    s[9]['gorsel'] = ilim_ozdeyisleri_panosu()
    s[11]['gorsel'] = arapca_ogretmeni_zamir_karti()
    s[12]['gorsel'] = fen_deney_ipucu_kartlari()
