"""7. sınıf Arapça 2. hafta (1. Ünite: Meslekler — Okuma Metni, Diyalog ve Alıştırmalar) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def muhammed_ailesi_ozet_kartlari():
    kartlar = [
        (4, 4, 'Ağabey (Ortaokul)', 'أَخِي الْكَبِيرُ مُدَرِّسٌ', MAVI, MAVI_A),
        (184, 4, 'Küçük Kardeş (Şirket)', 'أَخِي الصَّغِيرُ طَيَّارٌ', YES, YES_A),
        (4, 60, 'Abla (Giysi Diker)', 'أُخْتِي الْكَبِيرَةُ خَيَّاطَةٌ', TUR, TUR_A),
        (184, 60, 'Küçük Kız Kardeş', 'أُخْتِي الصَّغِيرَةُ طَبَّاخَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Muhammed’in kardeşlerini ve mesleklerini gösteren dört kart.', 16)


def soru_kelimesi_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(215, 27, 'مَنْ يَبِيعُ اللَّحْمَ؟ ← الْجَزَّارُ', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(215, 63, 'مَاذَا يَفْعَلُ الْجَزَّارُ؟ ← يَبِيعُ اللَّحْمَ', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(215, 99, 'مَاذَا تَفْعَلُ الْمُذِيعَةُ؟ ← تُقَدِّمُ الْأَخْبَارَ', LAC)
    return svg(360, 112, ic, 'Men ve mâzâ soru kartları ile cevapları.', 16)


def yapilan_is_kartlari():
    ic = kutu(4, 6, 172, 96, KIR_A, KIR, 8)
    ic += yazi_tr(90, 24, '1. Görev: Yangın Söndürür', KIR)
    ic += yazi_ar(90, 60, 'أَخِي يُطْفِئُ الْحَرِيقَ', LAC)
    ic += yazi_tr(90, 88, 'مَا مِهْنَتُهُ؟', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, '2. Görev: Yolculara Hizmet', MAVI)
    ic += yazi_ar(270, 60, 'أُخْتِي تَخْدِمُ الرُّكَّابَ', LAC)
    ic += yazi_tr(270, 88, 'مَا مِهْنَتُهَا؟', LAC, 'middle', False)
    return svg(360, 108, ic, 'Yangını söndüren erkek kardeş ve yolculara hizmet eden kız kardeş kartları.', 16)


def seddeli_bulmaca_kutu_sema():
    satirlar = [
        (4, 4, '1. طَيَّار → 4 Kutu (ط - ي - ا - ر)', MAVI, MAVI_A),
        (184, 4, '2. نَجَّار → 5 Kutu (ن - ج - ج - ا - ر)', KIR, KIR_A),
        (4, 60, '3. مُذِيعَة → 5 Kutu (م - ذ - ي - ع - ة)', YES, YES_A),
        (184, 60, '4. حَلَّاق → 4 Kutu (ح - ل - ا - ق)', MOR, MOR_A),
    ]
    ic = ''
    for x, y, metin, renk, arka in satirlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 30, metin, LAC)
    return svg(360, 114, ic, 'Şeddeli meslek adlarının bulmaca kutusu sayılarını gösteren şema.', 16)


def muzari_on_ek_kartlari():
    kartlar = [
        (4, '1. أَ (Ben)', 'أَفْحَصُ الْمَرْضَى', MAVI, MAVI_A),
        (124, '2. يَـ (O - Erkek)', 'يَفْحَصُ الْمَرْضَى', YES, YES_A),
        (244, '3. تَـ (O - Kadın)', 'تَفْحَصُ الْمَرْضَى', TUR, TUR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(kartlar):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 104, ic, 'Muzâri fiil ön ekleri: Efhasu, yefhasu, tefhasu.', 16)


def oyun_akis_sema():
    adimlar = [
        (4, '1. Öneri', 'سَنَلْعَبُ لُعْبَةً', MAVI, MAVI_A),
        (93, '2. Kabul', 'هَيَّا نَبْدَأُ', YES, YES_A),
        (182, '3. Soru', 'مَنْ يُصَمِّمُ؟', TUR, TUR_A),
        (271, '4. Doğru Yanıt', 'الْمُهَنْدِسُ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 100, ic, 'Sınıf içi meslek bulma oyununun dört adımı.', 16)


def haber_sunucu_diyalog_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Öğretmen', MAVI, 'start')
    ic += yazi_ar(215, 36, 'مَنْ تُقَدِّمُ الْأَخْبَارَ فِي التِّلْفَازِ؟', LAC)
    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Öğrenci', TUR, 'start')
    ic += yazi_ar(215, 90, '؟', KIR)
    return svg(360, 110, ic, 'Öğretmen televizyonda haberleri kimin sunduğunu sorar.', 16)


def ascilik_cumle_karti():
    ic = kutu(4, 6, 352, 96, TUR_A, TUR, 8)
    ic += yazi_tr(180, 24, 'Dişil Fiil ve Özne Uyumu', TUR)
    ic += yazi_ar(180, 60, '___ تَطْبُخُ الطَّعَامَ اللَّذِيذَ', LAC)
    ic += yazi_tr(180, 88, '... lezzetli yemek pişirir.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Yemek pişiren aile bireyi cümle tamamlama kartı.', 16)


def anne_neden_bilgi_karti():
    ic = kutu(4, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(90, 24, '1. Meslek Tanıtımı', YES)
    ic += yazi_ar(90, 62, 'أُمِّي مُمَرِّضَةٌ', LAC)
    ic += yazi_tr(90, 88, 'Annem hemşiredir', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, MOR_A, MOR, 8)
    ic += yazi_tr(270, 24, '2. Sevme Nedeni (لِأَنَّهَا)', MOR)
    ic += yazi_ar(270, 62, 'تَخْدِمُ الْمَرْضَى', LAC)
    ic += yazi_tr(270, 88, 'Hastalara hizmet eder', LAC, 'middle', False)
    return svg(360, 108, ic, 'Annenin mesleği ve hastalara hizmet etme gerekçesi.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = muhammed_ailesi_ozet_kartlari()
    s[2]['gorsel'] = soru_kelimesi_kartlari()
    s[3]['gorsel'] = yapilan_is_kartlari()
    s[5]['gorsel'] = seddeli_bulmaca_kutu_sema()
    s[7]['gorsel'] = muzari_on_ek_kartlari()
    s[8]['gorsel'] = oyun_akis_sema()
    s[9]['gorsel'] = haber_sunucu_diyalog_karti()
    s[11]['gorsel'] = ascilik_cumle_karti()
    s[12]['gorsel'] = anne_neden_bilgi_karti()
