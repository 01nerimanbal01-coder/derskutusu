"""7. sınıf Arapça 10. hafta (2. Ünite: Alışveriş — 2. Ders: Kırtasiyede: Tekil-İkil-Çoğul İsimler, Diyalog Çözümleme ve 10-19 Sayıları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe Noto Sans 10.5 pt, Arapça Arial 19-20 pt RTL (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=True, boy=10.2):
    ag = '700' if kalin else '500'
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle', boy=19):
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="{boy}" fill="{renk}">{metin}</text>'


def musenna_istek_karti():
    ic = kutu(4, 4, 352, 42, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 21, 'Müşteri', MAVI, 'start')
    ic += yazi_ar(215, 32, 'أُرِيدُ قَلَمَانِ وَدَفْتَرَانِ مِنْ فَضْلِكَ', LAC)
    ic += kutu(4, 52, 352, 42, YES_A, YES, 8)
    ic += yazi_tr(14, 69, 'Satıcı', YES, 'start')
    ic += yazi_ar(215, 80, 'تَفَضَّلِ الْقَلَمَيْنِ وَالدَّفْتَرَيْنِ', LAC)
    return svg(360, 98, ic, 'Kırtasiye konuşma kartı: İki kalem ve iki defter isteme.', 15)


def mufred_musenna_cemi_kartlari():
    kartlar = [
        (4, 4, '1. Kalem', 'قَلَمٌ · قَلَمَانِ · أَقْلَامٌ', MAVI, MAVI_A),
        (184, 4, '2. Defter', 'دَفْتَرٌ · ؟ · دَفَاتِرُ', TUR, TUR_A),
        (4, 52, '3. Çanta', 'حَقِيبَةٌ · حَقِيبَتَانِ · ؟', YES, YES_A),
        (184, 52, '4. Kitap', 'كِتَابٌ · ؟ · ؟', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 44, arka, renk, 7)
        ic += yazi_tr(x + 86, y + 16, bas, renk, boy=10.0)
        ic += yazi_ar(x + 86, y + 38, ar, LAC, boy=18)
    return svg(360, 100, ic, 'Kırtasiye gereçlerinin müfred, müsenna ve cemi kartları.', 15)


def diyalog_cozumleme_karti():
    ic = kutu(4, 4, 352, 86, SARI_A, TUR, 8)
    ic += yazi_tr(180, 20, 'Kırtasiye Diyaloğu (فِي الْمَكْتَبَةِ)', TUR)
    ic += yazi_ar(180, 46, 'الْمُشْتَرِي: أَنَا بِحَاجَةٍ إِلَى كُرَّاسَةِ رَسْمٍ وَمِقَصٍّ', LAC, boy=18)
    ic += yazi_ar(180, 74, 'الْبَائِعُ: تَفَضَّلْ، الْمَجْمُوعُ ثَمَانِي عَشْرَةَ لِيرَةً', YES, boy=18)
    return svg(360, 94, ic, 'Kırtasiyede resim defteri ve makas alınan diyalog kartı.', 15)


def ogrenci_sayi_panosu():
    kartlar = [
        (4, 4, '1. Kart (10)', 'عَشَرَةُ طُلَّابٍ', MAVI, MAVI_A),
        (184, 4, '2. Kart (11)', 'أَحَدَ عَشَرَ طَالِبًا', YES, YES_A),
        (4, 52, '3. Kart (?)', 'اِثْنَتَا عَشْرَةَ طَالِبَةً', KIR, KIR_A),
        (184, 52, '4. Kart (13)', 'ثَلَاثَةَ عَشَرَ طَالِبًا', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 44, arka, renk, 7)
        ic += yazi_tr(x + 86, y + 16, bas, renk, boy=10.0)
        ic += yazi_ar(x + 86, y + 38, ar, LAC, boy=18)
    return svg(360, 100, ic, '10-13 arası öğrenci sayı öbekleri panosu.', 15)


def kem_bikem_fark_karti():
    ic = kutu(4, 4, 172, 86, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, '1. Kart (كَمْ - Adet)', MAVI)
    ic += yazi_ar(90, 50, 'كَمْ دَفْتَرًا تُرِيدُ؟', LAC, boy=18)
    ic += yazi_tr(90, 78, 'Kaç defter istiyorsun?', LAC, kalin=False, boy=9.8)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi_tr(270, 20, '2. Kart (بِكَمْ - Fiyat)', YES)
    ic += yazi_ar(270, 50, 'بِكَمْ هٰذَا الدَّفْتَرُ؟', LAC, boy=18)
    ic += yazi_tr(270, 78, 'Bu defter kaç lira?', LAC, kalin=False, boy=9.8)
    return svg(360, 94, ic, 'Kem ve Bikem soru edatlarının karşılaştırma kartı.', 15)


def cogul_alisveris_akisi():
    adimlar = [
        (4, '1. Varlık', 'هَلْ عِنْدَكَ؟', MAVI, MAVI_A),
        (93, '2. Miktar', 'كَمْ تُرِيدُ؟', YES, YES_A),
        (182, '3. İstek', 'ثَلَاثَةَ أَقْلَامٍ', TUR, TUR_A),
        (271, '4. Tutar', '١٩ لِيرَةً', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, ar, renk, arka in adimlar:
        ic += kutu(x, 6, 85, 76, arka, renk, 8)
        ic += yazi_tr(x + 42, 24, bas, renk, boy=10.0)
        ic += yazi_ar(x + 42, 60, ar, LAC, boy=17)
    return svg(360, 88, ic, 'Kırtasiyede çoğul ve ikil ürün alma akış şeması.', 14)


def canta_envanter_fisi():
    ic = kutu(4, 4, 172, 86, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, 'İkil Eşyalar (مُثَنَّى)', MAVI)
    ic += yazi_ar(90, 48, 'كِتَابَانِ (٢)', LAC, boy=18)
    ic += yazi_ar(90, 76, 'وَمِسْطَرَتَانِ (٢)', LAC, boy=18)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi_tr(270, 20, 'Çoğul Eşyalar (جَمْع)', YES)
    ic += yazi_ar(270, 50, 'أَرْبَعَةُ أَقْلَامٍ (٤)', LAC, boy=18)
    ic += yazi_tr(270, 78, 'Toplam: 2 Kitap, 2 Cetvel, 4 Kalem', LAC, boy=9.5)
    return svg(360, 94, ic, 'Okul çantası envanter fişi: İki kitap, iki cetvel ve dört kalem.', 15)


def sirali_istek_panosu():
    kutular = [
        (4, '1. Önce (1 Adet)', 'حَقِيبَةٌ (١)', MAVI, MAVI_A),
        (124, '2. Bağlaç', 'ثُمَّ (Sonra)', TUR, TUR_A),
        (244, '3. İkil (2 Adet)', 'دَفْتَرَانِ (٢)', YES, YES_A),
    ]
    ic = ''
    for x, bas, ar, renk, arka in kutular:
        ic += kutu(x, 6, 112, 80, arka, renk, 8)
        ic += yazi_tr(x + 56, 24, bas, renk, boy=10.0)
        ic += yazi_ar(x + 56, 62, ar, LAC, boy=18)
    return svg(360, 92, ic, 'Önce bir çanta, sonra iki defter isteme şeması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = musenna_istek_karti()
    s[2]['gorsel'] = mufred_musenna_cemi_kartlari()
    s[5]['gorsel'] = diyalog_cozumleme_karti()
    s[6]['gorsel'] = ogrenci_sayi_panosu()
    s[7]['gorsel'] = kem_bikem_fark_karti()
    s[8]['gorsel'] = cogul_alisveris_akisi()
    s[9]['gorsel'] = canta_envanter_fisi()
    s[11]['gorsel'] = sirali_istek_panosu()
