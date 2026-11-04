"""7. sınıf Arapça 6. hafta (1. Ünite: Meslekler — Çalışma Yerleri ve Gelecekteki Meslek Tercihleri) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def calisma_yeri_kartlari():
    kartlar = [
        (4, 4, '1. Kart (Doğru)', 'الْمُعَلِّمُ · فِي الْمَدْرَسَةِ', MAVI, MAVI_A),
        (184, 4, '2. Kart (Doğru)', 'الْخَبَّازُ · فِي الْفُرْنِ', YES, YES_A),
        (4, 60, '3. Kart (Hatalı Mekân)', 'الطَّبَّاخُ · فِي الْمَحْكَمَةِ', KIR, KIR_A),
        (184, 60, '4. Kart (Doğru)', 'الْمُهَنْدِسُ · فِي الْمَصْنَعِ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Dört meslek ve çalışma yeri eşleştirme kartı.', 15)


def meslek_gorev_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(220, 27, 'الْمُعَلِّمُ يُدَرِّسُ الطُّلَّابَ', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(220, 63, 'الطَّبِيبُ يُعَالِجُ الْمَرْضَى', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(220, 99, 'الْخَيَّاطُ يَخِيطُ الْمَلَابِسَ', LAC)
    return svg(360, 112, ic, 'Öğretmen, doktor ve terzinin görevlerini anlatan üç kart.', 15)


def yuridu_cekim_tablosu():
    kartlar = [
        (4, 4, 'أَنَا (Ben)', '1: ؟', MAVI, MAVI_A),
        (184, 4, 'أَنْتَ (Sen - Erkek)', 'تُرِيدُ', YES, YES_A),
        (4, 60, 'أَنْتِ (Sen - Kız)', '2: ؟', TUR, TUR_A),
        (184, 60, 'هُوَ (O - Erkek)', 'يُرِيدُ', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Yürîdü fiilinin tekil şahıs zamirlerine göre çekim tablosu.', 15)


def kiz_ogrenci_hedef_diyalogu():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Soru (Kıza)', MAVI, 'start')
    ic += yazi_ar(225, 36, 'مَاذَا تُرِيدِينَ أَنْ تَكُونِي فِي الْمُسْتَقْبَلِ؟', LAC)
    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, 'Cevap', TUR, 'start')
    ic += yazi_ar(225, 90, '؟', KIR)
    return svg(360, 110, ic, 'Kız öğrenciye gelecekte ne olmak istediğinin sorulması.', 15)


def eril_disil_meslek_kartlari():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Sağlık Alanı', MAVI)
    ic += yazi_ar(90, 60, 'طَبِيبٌ ← طَبِيبَةٌ', LAC)
    ic += yazi_tr(90, 88, 'Erkek doktor - Kadın doktor', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Eğitim Alanı', YES)
    ic += yazi_ar(270, 60, 'مُعَلِّمٌ ← مُعَلِّمَةٌ', LAC)
    ic += yazi_tr(270, 88, 'Erkek öğretmen - Kadın öğretmen', LAC, 'middle', False)
    return svg(360, 108, ic, 'Eril meslek isimlerinin tâ-i merbûta ile dişile dönüşümü.', 15)


def aile_mekan_akis_sema():
    adimlar = [
        (4, '1. Kendisi', 'أَنَا طَالِبٌ', MAVI, MAVI_A),
        (93, '2. Baba', 'فِي الْمَصْنَعِ', YES, YES_A),
        (182, '3. Anne', 'فِي الْمُسْتَشْفَى', TUR, TUR_A),
        (271, '4. Hedef', 'أَنْ أَكُونَ طَبِيبًا', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Öğrencinin kendisini, ailesinin çalışma yerlerini ve hedefini tanıtma şeması.', 15)


def kok_turev_sema():
    kartlar = [
        (4, '1. Ekmek Kökü', 'خُبْزٌ ← خَبَّازٌ', MAVI, MAVI_A),
        (124, '2. Uçuş Kökü', 'طَائِرَةٌ ← طَيَّارٌ', YES, YES_A),
        (244, '3. Pişirme Kökü', 'طَبْخٌ ← طَبَّاخٌ', TUR, TUR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(kartlar):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 112, ic, 'Aynı üç harfli kökten türeyen isim ve meslek adları şeması.', 15)


def ciftci_mekan_karti():
    ic = kutu(4, 6, 352, 96, YES_A, YES, 8)
    ic += yazi_tr(180, 24, 'Çiftçinin Çalışma Yeri (أَيْنَ يَعْمَلُ الْفَلَّاحُ؟)', YES)
    ic += yazi_ar(180, 60, 'يَعْمَلُ الْفَلَّاحُ ___', LAC)
    ic += yazi_tr(180, 88, 'Çiftçi ... çalışıyor.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Çiftçinin çalıştığı yeri tamamlama kartı.', 15)


def baba_fabrika_pilot_kartlari():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Babanın Mesleği ve Yeri', MAVI)
    ic += yazi_ar(90, 60, 'أَبِي مُهَنْدِسٌ · فِي الْمَصْنَعِ', LAC)
    ic += yazi_tr(90, 88, 'Fabrikada mühendis', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, MOR_A, MOR, 8)
    ic += yazi_tr(270, 24, '2. Gelecek Tercihi', MOR)
    ic += yazi_ar(270, 60, 'سَأَكُونُ طَيَّارًا', LAC)
    ic += yazi_tr(270, 88, 'Gelecekte pilot olacağım', LAC, 'middle', False)
    return svg(360, 108, ic, 'Babanın fabrikada mühendisliği ve gelecekte pilot olma hedefi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = calisma_yeri_kartlari()
    s[2]['gorsel'] = meslek_gorev_kartlari()
    s[3]['gorsel'] = yuridu_cekim_tablosu()
    s[5]['gorsel'] = kiz_ogrenci_hedef_diyalogu()
    s[7]['gorsel'] = eril_disil_meslek_kartlari()
    s[8]['gorsel'] = aile_mekan_akis_sema()
    s[9]['gorsel'] = kok_turev_sema()
    s[11]['gorsel'] = ciftci_mekan_karti()
    s[12]['gorsel'] = baba_fabrika_pilot_kartlari()
