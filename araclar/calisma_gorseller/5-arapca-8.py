"""5. sınıf Arapça 8. hafta (Arap Alfabesinin Kalan Harfleri س - ي, Sınıf İçi Yönergeler ve Vedalaşma İfadeleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 12 pt, Arapça yazı Arial 22 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22"'


def svg(w, h, ic, etiket, en_fazla=19):
    stil = f' style="max-height:19mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def harf_ses_kartlari():
    kartlar = [
        ('1. Kart', 'ص', MAVI, MAVI_A),
        ('2. Kart', 'ك', YES, YES_A),
        ('3. Kart', 'ط', TUR, TUR_A),
        ('4. Kart', 'ق', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, harf, LAC)
    return svg(360, 96, ic, 'Dört harf kartı: 1. Sad, 2. Kef, 3. Tı, 4. Kaf.', 21)


def sinif_yonerge_kartlari():
    kartlar = [
        ('K · Ali', 'قُمْ', MAVI, MAVI_A),
        ('L · Meryem', 'اِقْرَئِي', YES, YES_A),
        ('M · Yusuf', 'اِجْلِسِي', KIR, '#fdeaea'),
        ('N · Ömer', 'اُكْتُبْ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 12, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 124, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört sınıf içi yönerge kartı: K Ali, L Meryem, M Yusuf, N Ömer.', 22)


def kelime_inceleme_kartlari():
    kartlar = [
        ('1. Kart', 'سَمَك', MAVI, MAVI_A),
        ('2. Kart', 'طَالِب', YES, YES_A),
        ('3. Kart', 'عَيْن', TUR, TUR_A),
        ('4. Kart', 'كِتَاب', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 67, kel, LAC)
    return svg(360, 96, ic, 'Dört kelime kartı: semek, tâlib, ayn ve kitâb.', 21)


def eril_disil_yonerge_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Erkek Öğrenciye Hitap', MAVI, kalin=True)
    ic += ar_yazi(91, 54, 'اِقْرَأْ · اُكْتُبْ', LAC)
    ic += tr_yazi(91, 80, 'Oku · Yaz (Eril)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Kız Öğrenciye Hitap', MOR, kalin=True)
    ic += ar_yazi(269, 54, 'اِقْرَئِي · اُكْتُبِي', LAC)
    ic += tr_yazi(269, 80, 'Oku · Yaz (Dişil)', LAC)
    return svg(360, 100, ic, 'Erkek ve kız öğrenciye hitap eden oku ve yaz yönerge panoları.', 21)


def alfabe_sira_vagonlari():
    gruplar = [
        ('Grup K', 'ط - ظ', TUR, TUR_A),
        ('Grup L', 'س - ش', MAVI, MAVI_A),
        ('Grup M', 'و - ي', MOR, MOR_A),
        ('Grup N', 'ف - ق', YES, YES_A),
    ]
    ic = ''
    for i, (bas, ikili, renk, arka) in enumerate(gruplar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += ar_yazi(x + 41, 65, ikili, LAC)
    return svg(360, 96, ic, 'Arap alfabesindeki dört harf ikilisi kartı.', 21)


def hadis_iletisim_panosu():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 24, 'İslam İletişim Adabı · Hadis-i Şerif', TUR, kalin=True)
    ic += ar_yazi(180, 56, 'اَلسَّلَامُ قَبْلَ الْكَلَامِ', LAC)
    ic += tr_yazi(180, 82, 'Selam, kelamdan (konuşmadan) öncedir.', LAC)
    return svg(360, 104, ic, 'Selam kelamdan öncedir hadis-i şerif panosu.', 21)


def vedalasma_diyalog_karti():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 33, '1. Öğrenci:', MAVI, 'start', kalin=True)
    ic += ar_yazi(220, 35, 'مَعَ السَّلَامَةِ', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 83, '2. Öğrenci:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(220, 85, '؟', YESIL_K)
    return svg(360, 106, ic, 'Okul çıkışında vedalaşan iki öğrencinin konuşma kartı.', 21)


def vav_birlesme_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Bitişen Harfler', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'قَلَم', LAC)
    ic += tr_yazi(91, 80, 'Kalem (Tüm harfler bitişik)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Vav Harfi Kuralı', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'وَلَد', LAC)
    ic += tr_yazi(269, 80, 'Veled (Vav sonraya bitişmez)', LAC)
    return svg(360, 100, ic, 'Kalem ve veled kelimelerinde harflerin birleşme karşılaştırması.', 21)


def noktali_harf_ciftleri():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Harf Çifti', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'ع - ؟', LAC)
    ic += tr_yazi(91, 80, 'Noktasız Ayn · Üstte 1 Nokta', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Harf Çifti', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'ص - ؟', LAC)
    ic += tr_yazi(269, 80, 'Noktasız Sad · Üstte 1 Nokta', LAC)
    return svg(360, 100, ic, 'Ayn ve Sad harflerine birer nokta eklenmesi şeması.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = harf_ses_kartlari()
    s[4]['gorsel'] = sinif_yonerge_kartlari()
    s[5]['gorsel'] = kelime_inceleme_kartlari()
    s[6]['gorsel'] = eril_disil_yonerge_panosu()
    s[7]['gorsel'] = alfabe_sira_vagonlari()
    s[8]['gorsel'] = hadis_iletisim_panosu()
    s[9]['gorsel'] = vedalasma_diyalog_karti()
    s[11]['gorsel'] = vav_birlesme_karti()
    s[12]['gorsel'] = noktali_harf_ciftleri()
