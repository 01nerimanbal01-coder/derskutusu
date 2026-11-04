"""7. sınıf Arapça 5. hafta (1. Ünite: Meslekler — 3. Ders: Hayalim) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def likey_amac_kartlari():
    kartlar = [
        (4, 4, '1. طَبِيبًا', 'لِكَيْ أُعَالِجَ الْمَرْضَى', MAVI, MAVI_A),
        (184, 4, '2. مُحَامِيًا', 'لِكَيْ أُدَافِعَ عَنِ الْمَظْلُومِينَ', YES, YES_A),
        (4, 60, '3. مِعْمَارِيًّا', 'لِكَيْ أُصَمِّمَ بُيُوتًا جَمِيلَةً', MOR, MOR_A),
        (184, 60, '4. صَيْدَلِيًّا (Uyumsuz)', 'لِكَيْ أَقُودَ الطَّائِرَةَ', KIR, KIR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Dört meslek ve li-key amaç eşleştirme kartı.', 15)


def hayal_sebep_tablo_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Ben', MAVI, 'start')
    ic += yazi_ar(220, 27, 'طَيَّارًا · لِأَنَّنِي أُحِبُّ الطَّيَرَانَ', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Selim', TUR, 'start')
    ic += yazi_ar(220, 63, 'رَائِدَ فَضَاءٍ · لِأَنَّهُ يُحِبُّ الْفَضَاءَ', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Zeynep', YES, 'start')
    ic += yazi_ar(220, 99, 'صَحَفِيَّةً · لِأَنَّهَا تُحِبُّ الْأَخْبَارَ', LAC)
    return svg(360, 112, ic, 'Üç öğrencinin meslek hayali ve li-enne gerekçe kartları.', 15)


def limaza_ogretmen_diyalogu():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Soru', MAVI, 'start')
    ic += yazi_ar(220, 36, 'لِمَاذَا تُرِيدُ أَنْ تَكُونَ مُعَلِّمًا؟', LAC)
    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Cevap', TUR, 'start')
    ic += yazi_ar(220, 90, 'لِأَنَّنِي ... ؟', KIR)
    return svg(360, 110, ic, 'Neden öğretmen olmak istiyorsun sorusu ve cevap kartı.', 15)


def yahlumu_cekim_kartlari():
    kartlar = [
        (4, 4, '1. Kart (Doğru)', 'أَنَا أَحْلُمُ أَنْ أَكُونَ عَالِمًا', MAVI, MAVI_A),
        (184, 4, '2. Kart (Hatalı Çekim)', 'سَلِيمٌ تَحْلُمُ أَنْ يَكُونَ طَيَّارًا', KIR, KIR_A),
        (4, 60, '3. Kart (Doğru)', 'زَيْنَبُ تَحْلُمُ أَنْ تَكُونَ صَحَفِيَّةً', YES, YES_A),
        (184, 60, '4. Kart (Doğru)', 'هُوَ يَحْلُمُ أَنْ يَكُونَ مِعْمَارِيًّا', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Ehlümü, yahlümü ve tahlümü fiil çekim kartları.', 15)


def lienneni_likey_farki():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Yapı: Sebep Bildirme', MAVI)
    ic += yazi_ar(90, 60, 'لِأَنَّنِي أُحِبُّ الطَّيَرَانَ', LAC)
    ic += yazi_tr(90, 88, 'لِمَاذَا؟ sorusuna sebep', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Yapı: Amaç Bildirme', YES)
    ic += yazi_ar(270, 60, 'لِكَيْ أُعَالِجَ الْمَرْضَى', LAC)
    ic += yazi_tr(270, 88, 'Hedeflenen amaç', LAC, 'middle', False)
    return svg(360, 108, ic, 'Li-ennenî ve li-key bağlaçlarının karşılaştırma kartları.', 15)


def hayal_diyalog_akis_sema():
    adimlar = [
        (4, '1. Hayal Sorusu', 'مَا هُوَ حُلْمُكَ؟', MAVI, MAVI_A),
        (93, '2. Meslek', 'أَنْ أَكُونَ طَبِيبًا', YES, YES_A),
        (182, '3. Neden Sorusu', 'لِمَاذَا تُرِيدُ؟', TUR, TUR_A),
        (271, '4. Amaç', 'لِكَيْ أُعَالِجَ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Meslek hayali ve neden sorma diyaloğunun dört adımı.', 15)


def cedde_ve_itkan_panosu():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Atasözü', MAVI, 'start')
    ic += yazi_ar(220, 36, 'مَنْ جَدَّ وَجَدَ، وَمَنْ زَرَعَ حَصَدَ', LAC)
    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Hadis-i Şerif', YES, 'start')
    ic += yazi_ar(220, 90, 'إِنَّ اللّٰهَ يُحِبُّ إِذَا عَمِلَ أَحَدُكُمْ عَمَلًا أَنْ يُتْقِنَهُ', LAC)
    return svg(360, 110, ic, 'Men cedde vecede atasözü ve itkân hadis-i şerifi panosu.', 15)


def zeynep_lienneha_karti():
    ic = kutu(4, 6, 352, 96, TUR_A, TUR, 8)
    ic += yazi_tr(180, 24, 'Zeynep’in Meslek Seçme Nedeni', TUR)
    ic += yazi_ar(180, 60, 'زَيْنَبُ تَحْلُمُ أَنْ تَكُونَ صَحَفِيَّةً؛ ___ تُحِبُّ الْأَخْبَارَ', LAC)
    ic += yazi_tr(180, 88, 'Zeynep gazeteci olmayı hayal ediyor; ... haberleri seviyor.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Zeynep için li-ennehâ zamirli sebep cümlesi kartı.', 15)


def avukat_hayal_yapi_taslari():
    kartlar = [
        (4, '1. Başlangıç', 'حُلْمِي أَنْ أَكُونَ', MAVI, MAVI_A),
        (124, '2. Meslek', 'مُحَامِيًا فِي الْمُسْتَقْبَلِ', YES, YES_A),
        (244, '3. Amaç (لِكَيْ)', 'أُدَافِعَ عَنِ الْمَظْلُومِينَ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(kartlar):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 112, ic, 'Avukat olma hayali ve mazlumları savunma amacı yapı taşları.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = likey_amac_kartlari()
    s[2]['gorsel'] = hayal_sebep_tablo_kartlari()
    s[3]['gorsel'] = limaza_ogretmen_diyalogu()
    s[5]['gorsel'] = yahlumu_cekim_kartlari()
    s[7]['gorsel'] = lienneni_likey_farki()
    s[8]['gorsel'] = hayal_diyalog_akis_sema()
    s[9]['gorsel'] = cedde_ve_itkan_panosu()
    s[11]['gorsel'] = zeynep_lienneha_karti()
    s[12]['gorsel'] = avukat_hayal_yapi_taslari()
