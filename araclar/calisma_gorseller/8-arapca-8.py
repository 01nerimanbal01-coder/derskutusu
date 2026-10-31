"""8. sınıf Arapça 8. hafta (3. Ünite: Kültür ve Sanat — 1. Ders: Edebiyat Metinleri, Kitap Fuarı ve İsim/Fiil Cümlesi Uygulamaları) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; Türkçe Noto Sans 12 pt, Arapça Arial 22 pt RTL)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


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


def fuar_klasik_afisi():
    ic = kutu(4, 4, 352, 32, MOR_A, MOR, 7)
    ic += yazi_tr(80, 24, 'Kitap Fuarı', MOR)
    ic += yazi_ar(250, 28, 'مَعْرِضُ الْكِتَابِ', LAC)

    ic += kutu(4, 42, 172, 64, TUR_A, TUR, 8)
    ic += yazi_tr(90, 60, '1. Stant (Dünya Klasiği)', TUR)
    ic += yazi_ar(90, 94, 'أَلْفُ لَيْلَةٍ وَلَيْلَةٍ', LAC)

    ic += kutu(184, 42, 172, 64, YES_A, YES, 8)
    ic += yazi_tr(270, 60, '2. Stant (Halk Edebiyatı)', YES)
    ic += yazi_ar(270, 94, 'نَوَادِرُ جُحَا', LAC)
    return svg(360, 110, ic, 'Kitap fuarı afişi: 1. Stant Elf Leyle ve Leyle, 2. Stant Nevâdiru Cuhâ.', 22)


def isim_fiil_kartlari():
    ic = kutu(4, 4, 352, 32, MAVI_A, MAVI, 7)
    ic += yazi_tr(14, 24, '1. Kart', MAVI, 'start')
    ic += yazi_ar(218, 27, 'الصُّنْدُوقُ فِي زَاوِيَةِ الْغُرْفَةِ', LAC)

    ic += kutu(4, 40, 352, 32, YES_A, YES, 7)
    ic += yazi_tr(14, 60, '2. Kart', YES, 'start')
    ic += yazi_ar(218, 63, 'قَرَأَ التِّلْمِيذُ قِصَّةَ جُحَا', LAC)

    ic += kutu(4, 76, 352, 32, TUR_A, TUR, 7)
    ic += yazi_tr(14, 96, '3. Kart', TUR, 'start')
    ic += yazi_ar(218, 99, 'الرِّوَايَةُ التَّارِيخِيَّةُ مُمْتِعَةٌ', LAC)
    return svg(360, 112, ic, 'Üç cümle kartı: 1. Sandık odanın köşesindedir, 2. Öğrenci Cuha hikâyesini okudu, 3. Tarihî roman sürükleyicidir.', 22)


def okuma_tercih_panosu():
    ic = kutu(4, 4, 172, 100, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 22, 'Selim’in Tercihi', MAVI)
    ic += yazi_ar(90, 54, 'أُحِبُّ الرِّوَايَاتِ', LAC)
    ic += yazi_ar(90, 88, 'وَالْكُتُبَ الدِّينِيَّةَ', LAC)

    ic += kutu(184, 4, 172, 100, MOR_A, MOR, 8)
    ic += yazi_tr(270, 22, 'Meryem’in Tercihi', MOR)
    ic += yazi_ar(270, 54, 'أُفَضِّلُ الشِّعْرَ', LAC)
    ic += yazi_ar(270, 88, 'لَا أُحِبُّ الْقِصَصَ', LAC)
    return svg(360, 108, ic, 'Selim ve Meryem okuma tercihleri kartları.', 22)


def soru_edati_diyalog():
    ic = kutu(4, 4, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 24, 'Soru', TUR, 'start')
    ic += yazi_ar(216, 36, '___ تَذْهَبُ إِلَى مَعْرِضِ الْكِتَابِ؟', LAC)

    ic += kutu(4, 58, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 78, 'Cevap', YES, 'start')
    ic += yazi_ar(216, 90, 'أَذْهَبُ لِأَشْتَرِيَ رِوَايَةً جَدِيدَةً', LAC)
    return svg(360, 110, ic, 'Soru edatı boş bırakılmış fuar diyaloğu ve sebep bildiren cevap.', 22)


def zaman_zarfi_cizelgesi():
    ic = kutu(4, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 24, '1. Zaman Dilimi (Önce)', MAVI)
    ic += yazi_ar(90, 58, 'قَبْلَ الظُّهْرِ', LAC)
    ic += yazi_tr(90, 86, 'Kütüphane ziyareti', LAC, 'middle', False)

    ic += kutu(184, 6, 172, 94, YES_A, YES, 8)
    ic += yazi_tr(270, 24, '2. Zaman Dilimi (Sonra)', YES)
    ic += yazi_ar(270, 58, 'بَعْدَ الدَّرْسِ', LAC)
    ic += yazi_tr(270, 86, 'Hikâye okuma saati', LAC, 'middle', False)
    return svg(360, 106, ic, 'Kable’z-zuhri ve ba’de’d-dersi zaman zarfı kartları.', 21)


def fuar_gezi_akis_sema():
    adimlar = [
        (4, '1. Davet', 'هَيَّا بِنَا', MOR, MOR_A),
        (93, '2. Varış', 'قَبْلَ', MAVI, MAVI_A),
        (182, '3. Alışveriş', 'ثُمَّ', TUR, TUR_A),
        (271, '4. Okuma', 'بَعْدَ', YES, YES_A),
    ]
    ic = ''
    for x, bas, ar, renk, arka in adimlar:
        ic += kutu(x, 8, 85, 84, arka, renk, 8)
        ic += yazi_tr(x + 42, 28, bas, renk)
        ic += yazi_ar(x + 42, 68, ar, LAC)
    return svg(360, 100, ic, 'Kitap fuarı gezisinin dört aşamalı sıralama şeması.', 20)


def mekan_betimleme_karti():
    ic = kutu(4, 4, 352, 48, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 24, '1. Cümle', MAVI, 'start')
    ic += yazi_ar(222, 36, 'الصُّنْدُوقُ فِي زَاوِيَةِ الْغُرْفَةِ', LAC)

    ic += kutu(4, 58, 352, 48, TUR_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Cümle', TUR, 'start')
    ic += yazi_ar(222, 90, 'الْكُتُبُ الدِّينِيَّةُ عَلَى الرَّفِّ', LAC)
    return svg(360, 110, ic, 'Mekân betimleme kartı: Sandık odanın köşesindedir ve dinî kitaplar rafın üzerindedir.', 22)


def iletisim_durum_karti():
    ic = kutu(4, 4, 352, 48, YES_A, YES, 8)
    ic += yazi_tr(14, 24, '1. Ömer', YES, 'start')
    ic += yazi_ar(224, 36, 'سَلَامَتُكَ يَا صَدِيقِي', LAC)

    ic += kutu(4, 58, 352, 48, SARI_A, TUR, 8)
    ic += yazi_tr(14, 78, '2. Zeynep', TUR, 'start')
    ic += yazi_ar(224, 90, '؟', KIR)
    return svg(360, 110, ic, 'İletişim durum kartları: 1. Geçmiş olsun dileği, 2. Her şey yolunda ifadesi.', 22)


def okuma_gunlugu_karti():
    ic = kutu(4, 6, 172, 94, MOR_A, MOR, 8)
    ic += yazi_tr(90, 24, 'Sevilen Edebî Tür', MOR)
    ic += yazi_ar(90, 56, 'أُحِبُّ الرِّوَايَاتِ', LAC)
    ic += yazi_ar(90, 86, 'التَّارِيخِيَّةَ', LAC)

    ic += kutu(184, 6, 172, 94, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 24, 'Fuar Etkinlik Sırası', MAVI)
    ic += yazi_ar(270, 56, 'ذَهَبْتُ إِلَى الْمَعْرِضِ', LAC)
    ic += yazi_ar(270, 86, 'ثُمَّ اشْتَرَيْتُ كِتَابًا', LAC)
    return svg(360, 106, ic, 'Okuma günlüğü kartı: Tarihî roman tercihi ve fuar alışverişi sıralaması.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = fuar_klasik_afisi()
    s[2]['gorsel'] = isim_fiil_kartlari()
    s[3]['gorsel'] = okuma_tercih_panosu()
    s[5]['gorsel'] = soru_edati_diyalog()
    s[7]['gorsel'] = zaman_zarfi_cizelgesi()
    s[8]['gorsel'] = fuar_gezi_akis_sema()
    s[9]['gorsel'] = mekan_betimleme_karti()
    s[11]['gorsel'] = iletisim_durum_karti()
    s[12]['gorsel'] = okuma_gunlugu_karti()
