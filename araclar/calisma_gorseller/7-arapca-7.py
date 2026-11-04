"""7. sınıf Arapça 7. hafta (2. Ünite: Alışveriş — Bakkalda: Temel Gıda Maddeleri ve Fiyat Sorma) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

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


def uclu_gida_istek_karti():
    urunler = [
        (4, '1. Ürün', 'حَلِيبًا', MAVI, MAVI_A),
        (124, '2. Ürün', 'وَزَيْتُونًا', YES, YES_A),
        (244, '3. Ürün', 'وَزُبْدَةً', TUR, TUR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(urunler):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 112, ic, 'Üç gıda ürünü isteme kartı: Süt, zeytin ve tereyağı.', 15)


def bakkal_diyalog_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(220, 27, 'أَهْلًا وَسَهْلًا! أَيُّ خِدْمَةٍ؟', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(220, 63, 'هَلْ يُوجَدُ عَسَلٌ طَبِيعِيٌّ؟', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(220, 99, 'الْمَجْمُوعُ بِخَمْسِينَ لِيرَةً', LAC)
    return svg(360, 112, ic, 'Bakkal ve müşteri arasında geçen üç konuşma kartı.', 15)


def benzer_gida_etiketleri():
    etiketler = [
        (4, 4, '1. Etiket: Zeytin', 'زَيْتُونٌ', YES, YES_A),
        (184, 4, '2. Etiket: Sıvı Yağ', 'زَيْتٌ', MAVI, MAVI_A),
        (4, 60, '3. Etiket: Tereyağı', 'زُبْدَةٌ', TUR, TUR_A),
        (184, 60, '4. Etiket: Peynir (Hatalı)', 'سُكَّرٌ', KIR, KIR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in etiketler:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Zeytin, sıvı yağ, tereyağı ve şeker raf etiketleri.', 15)


def hel_yucedu_diyalog_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, 'Müşteri', MAVI, 'start')
    ic += yazi_ar(220, 36, '___ يُوجَدُ شَايٌ فِي الْبَقَّالَةِ؟', LAC)
    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Bakkal', YES, 'start')
    ic += yazi_ar(220, 90, 'نَعَمْ، يُوجَدُ. تَفَضَّلْ!', LAC)
    return svg(360, 110, ic, 'Müşterinin çay var mı sorusu ve bakkalın olumlu cevabı.', 15)


def varlik_ve_fiyat_soru_kartlari():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Kalıp (Bulunma Sorusu)', MAVI)
    ic += yazi_ar(90, 60, 'هَلْ يُوجَدُ سُكَّرٌ؟', LAC)
    ic += yazi_tr(90, 88, 'Cevap: نَعَمْ، يُوجَدُ', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, TUR_A, TUR, 8)
    ic += yazi_tr(270, 24, '2. Kalıp (Fiyat Sorusu)', TUR)
    ic += yazi_ar(270, 60, 'بِكَمْ هٰذَا الْخُبْزُ؟', LAC)
    ic += yazi_tr(270, 88, 'Cevap: بِعَشْرِ لِيرَاتٍ', LAC, 'middle', False)
    return svg(360, 108, ic, 'Hel yûcedü ve bikem soru kalıpları karşılaştırma kartları.', 15)


def alisveris_adimlari_sema():
    adimlar = [
        (4, '1. Karşılama', 'أَيُّ خِدْمَةٍ؟', MAVI, MAVI_A),
        (93, '2. İstek', 'أُرِيدُ حَلِيبًا', YES, YES_A),
        (182, '3. Fiyat', 'بِكَمِ الْمَجْمُوعُ؟', TUR, TUR_A),
        (271, '4. Ödeme', 'تَفَضَّلِ النُّقُودَ', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(adimlar):
        gx, gy = 4 + (idx % 2) * 180, 4 + (idx // 2) * 52
        ic += kutu(gx, gy, 172, 48, arka, renk, 8)
        ic += yazi_tr(gx + 86, gy + 18, bas, renk)
        ic += yazi_ar(gx + 86, gy + 41, ar, LAC)
    return svg(360, 112, ic, 'Bakkalda alışveriş diyaloğunun dört adımı.', 15)


def gida_fiyat_panosu():
    urunler = [
        (4, 'عُلْبَةُ حَلِيبٍ', '20 TL (عِشْرُونَ)', MAVI, MAVI_A),
        (124, 'خُبْزٌ', '10 TL (عَشْرٌ)', YES, YES_A),
        (244, 'كِيلُو جُبْنٍ', '50 TL (خَمْسُونَ)', TUR, TUR_A),
    ]
    ic = ''
    for x, ar, fiyat, renk, arka in urunler:
        ic += kutu(x, 6, 112, 92, arka, renk, 8)
        ic += yazi_ar(x + 56, 46, ar, LAC)
        ic += yazi_tr(x + 56, 82, fiyat, renk)
    return svg(360, 112, ic, 'Üç ürünlü fiyat panosu: Süt 20 TL, ekmek 10 TL, peynir 50 TL.', 15)


def sise_yag_ambalaj_karti():
    ic = kutu(4, 6, 352, 96, SARI_A, TUR, 8)
    ic += yazi_tr(180, 24, 'Miktar ve Ambalaj Tamlaması', TUR)
    ic += yazi_ar(180, 60, 'أُرِيدُ ___ مِنْ فَضْلِكَ', LAC)
    ic += yazi_tr(180, 88, 'Lütfen bir şişe sıvı yağ istiyorum.', LAC, 'middle', False)
    return svg(360, 108, ic, 'Bir şişe sıvı yağ isteme cümle kartı.', 15)


def siparis_fisi_kartlari():
    kartlar = [
        (4, '1. İstek (أُرِيدُ)', 'كِيلُو جُبْنٍ', MAVI, MAVI_A),
        (124, '2. Ek Ürün (وَ)', 'عُلْبَةَ حَلِيبٍ', YES, YES_A),
        (244, '3. Nezaket · Fiyat', 'بِكَمِ الْمَجْمُوعُ؟', MOR, MOR_A),
    ]
    ic = ''
    for idx, (_, bas, ar, renk, arka) in enumerate(kartlar):
        gy = 4 + idx * 36
        ic += kutu(4, gy, 352, 32, arka, renk, 7)
        ic += yazi_tr(14, gy + 21, bas, renk, 'start')
        ic += yazi_ar(225, gy + 24, ar, LAC)
    return svg(360, 112, ic, 'Bir kilo peynir, bir kutu süt ve toplam fiyat sorma fişi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = uclu_gida_istek_karti()
    s[2]['gorsel'] = bakkal_diyalog_kartlari()
    s[3]['gorsel'] = benzer_gida_etiketleri()
    s[5]['gorsel'] = hel_yucedu_diyalog_karti()
    s[7]['gorsel'] = varlik_ve_fiyat_soru_kartlari()
    s[8]['gorsel'] = alisveris_adimlari_sema()
    s[9]['gorsel'] = gida_fiyat_panosu()
    s[11]['gorsel'] = sise_yag_ambalaj_karti()
    s[12]['gorsel'] = siparis_fisi_kartlari()
