"""7. sınıf Arapça 8. hafta (2. Ünite: Alışveriş — 1. Ders: Bakkalda Diyalogları, Miktar ve Fiyat Sorma ile Bağlaçlar) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:17mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=True):
    ag = '700' if kalin else '500'
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="12" font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22" fill="{renk}">{metin}</text>'


def bakkal_istek_fisi():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 22, 'Müşteri', MAVI, 'start')
    ic += yazi_ar(212, 36, 'أَنَا بِحَاجَةٍ إِلَى دَقِيقٍ وَزَيْتُونٍ لَوْ سَمَحْتَ', LAC)
    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 76, 'Bakkal', YES, 'start')
    ic += yazi_ar(212, 90, 'تَفَضَّلْ، هَلْ تُرِيدُ شَيْئًا آخَرَ؟', LAC)
    return svg(360, 110, ic, 'Bakkal alışveriş fişi: Müşteri un ve zeytin ister, bakkal buyur diyerek karşılık verir.', 22)


def cumle_turu_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(220, 27, 'عِنْدِي عَسَلٌ طَازَجٌ', LAC)
    ic += kutu(4, 40, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 60, '2. Kart', TUR, 'start')
    ic += yazi_ar(220, 63, 'هَلْ عِنْدَكَ جُبْنٌ أَبْيَضُ؟', LAC)
    ic += kutu(4, 76, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 96, '3. Kart', YES, 'start')
    ic += yazi_ar(220, 99, 'بِكَمِ الْمَجْمُوعُ؟', LAC)
    return svg(360, 112, ic, 'Üç cümle kartı: 1. Düz cümle, 2. Varlık sorusu, 3. Toplam fiyat sorusu.', 22)


def baglac_panosu():
    ic = kutu(4, 4, 172, 102, TUR_A, TUR, 8)
    ic += yazi_tr(90, 22, 'A Kartı (Seçenek Sorusu)', TUR)
    ic += yazi_ar(90, 56, 'أَتُرِيدُ شَايًا ___ قَهْوَةً؟', LAC)
    ic += yazi_tr(90, 90, 'Çay mı ... kahve mi?', LAC, 'middle', False)

    ic += kutu(184, 4, 172, 102, MOR_A, MOR, 8)
    ic += yazi_tr(270, 22, 'B Kartı (Oluş Sırası)', MOR)
    ic += yazi_ar(270, 56, 'آخُذُ الْخُبْزَ ___ أَدْفَعُ', LAC)
    ic += yazi_tr(270, 90, 'Alırım, ... öderim.', LAC, 'middle', False)
    return svg(360, 110, ic, 'A ve B bağlaç kartları: Seçenek sorusu ve sıralama cümlesi.', 22)


def reyon_fiyat_etiketleri():
    etiketler = [
        (4, 4, '1. Etiket · 40 TL', 'بِكَمْ هٰذَا الْجُبْنُ؟', MAVI, MAVI_A),
        (184, 4, '2. Etiket · 60 TL', 'بِكَمْ هٰذَا الزُّبْدَةُ؟', KIR, KIR_A),
        (4, 60, '3. Etiket · 90 TL', 'بِكَمْ هٰذَا الْعَسَلُ؟', YES, YES_A),
        (184, 60, '4. Etiket · 50 TL', 'بِكَمْ هٰذِهِ الْقَهْوَةُ؟', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in etiketler:
        ic += kutu(x, y, 172, 50, arka, renk, 8)
        ic += yazi_tr(x + 86, y + 18, bas, renk)
        ic += yazi_ar(x + 86, y + 43, ar, LAC)
    return svg(360, 114, ic, 'Dört reyon fiyat etiketi: peynir, tereyağı, bal ve kahve.', 22)


def hareke_farki_kartlari():
    ic = kutu(4, 6, 172, 96, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Kart (Fiil + Nesne)', MAVI)
    ic += yazi_ar(90, 60, 'أُرِيدُ خُبْزًا', LAC)
    ic += yazi_tr(90, 88, 'Üstün (fetha) harekeli', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 96, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Kart (Harf-i Cer)', YES)
    ic += yazi_ar(270, 60, 'أَنَا بِحَاجَةٍ إِلَى خُبْزٍ', LAC)
    ic += yazi_tr(270, 88, 'Esre (kesra) harekeli', LAC, 'middle', False)
    return svg(360, 108, ic, 'İki ekmek isteme kartı: Ürîdü hubzen ve Enâ bi-hâcetin ilâ hubzin.', 21)


def diyalog_akis_sema():
    adimlar = [
        (4, '1. Adım', 'السَّلَامُ وَالْإِرَادَةُ', MAVI, MAVI_A),
        (93, '2. Adım', 'تَفَضَّلْ وَالسُّؤَالُ', YES, YES_A),
        (182, '3. Adım', 'بِكَمِ الْمَجْمُوعُ؟', TUR, TUR_A),
        (271, '4. Adım', 'الدَّفْعُ وَالْوَدَاعُ', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, ar, renk, arka in adimlar:
        ic += kutu(x, 8, 85, 84, arka, renk, 8)
        ic += yazi_tr(x + 42, 28, bas, renk)
        ic += yazi_ar(x + 42, 68, ar, LAC)
    return svg(360, 100, ic, 'Alışveriş diyaloğunun dört aşamalı akış şeması.', 20)


def sepet_ve_kasa_fisi():
    ic = kutu(4, 4, 172, 100, YES_A, YES, 8)
    ic += yazi_tr(90, 22, 'Sepetteki Ürünler', YES)
    ic += yazi_ar(90, 52, 'زُجَاجَةُ زَيْتٍ', LAC)
    ic += yazi_ar(90, 84, 'وَطَبَقُ بَيْضٍ', LAC)

    ic += kutu(184, 4, 172, 100, TUR_A, TUR, 8)
    ic += yazi_tr(270, 22, 'Kasa Toplam Fişi', TUR)
    ic += yazi_ar(270, 56, 'الْمَجْمُوعُ مِائَةُ لِيرَةٍ', LAC)
    ic += yazi_tr(270, 88, 'Toplam Tutar: 100 TL', LAC)
    return svg(360, 108, ic, 'Alışveriş sepetinde bir şişe yağ ve bir koli yumurta; kasa fişi 100 lira.', 22)


def nezaket_konusma_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Müşteri', MAVI, 'start')
    ic += yazi_ar(220, 36, 'أُرِيدُ جُبْنًا مِنْ فَضْلِكَ', LAC)
    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Bakkal', TUR, 'start')
    ic += yazi_ar(220, 90, '؟', KIR)
    return svg(360, 110, ic, 'Müşteri lütfen peynir istiyorum der, bakkalın yanıtı soru işaretiyle gösterilir.', 22)


def liste_sirali_pano():
    kutular = [
        (4, '1. Önce', 'عُلْبَةُ حَلِيبٍ', MAVI, MAVI_A),
        (124, '2. Sonra (ثُمَّ)', 'كِيلُو جُبْنٍ', YES, YES_A),
        (244, '3. Fiyat Sorusu', 'بِكَمِ الْمَجْمُوعُ؟', TUR, TUR_A),
    ]
    ic = ''
    for x, bas, ar, renk, arka in kutular:
        ic += kutu(x, 6, 112, 92, arka, renk, 8)
        ic += yazi_tr(x + 56, 26, bas, renk)
        ic += yazi_ar(x + 56, 68, ar, LAC)
    return svg(360, 104, ic, 'Sıralı alışveriş listesi: 1. Bir kutu süt, 2. Bir kilo peynir, 3. Toplamı kaç lira.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bakkal_istek_fisi()
    s[2]['gorsel'] = cumle_turu_kartlari()
    s[3]['gorsel'] = baglac_panosu()
    s[5]['gorsel'] = reyon_fiyat_etiketleri()
    s[7]['gorsel'] = hareke_farki_kartlari()
    s[8]['gorsel'] = diyalog_akis_sema()
    s[9]['gorsel'] = sepet_ve_kasa_fisi()
    s[11]['gorsel'] = nezaket_konusma_karti()
    s[12]['gorsel'] = liste_sirali_pano()
