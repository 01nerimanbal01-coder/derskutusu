"""5. sınıf Arapça 3. hafta (Tanışma-Vedalaşma Konuşmaları ve Üçüncü Harf Grubu ط ظ ع غ ف ق ك ل م ن هـ و ي) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 12 pt, Arapça yazı Arial 22 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def ucuncu_grup_ikililer():
    kartlar = [
        ('1. Kart', 'ط - ظ', MAVI, MAVI_A),
        ('2. Kart', 'ع - غ', YES, YES_A),
        ('3. Kart', 'ف - ق', TUR, TUR_A),
        ('4. Kart', 'ل - م', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ikili, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, ikili, LAC)
    return svg(360, 96, ic, 'Üçüncü grup harf ikilisi kartları: Tâ-Zâ, Ayn-Gayn, Fâ-Kâf, Lâm-Mîm.', 21)


def dogrulama_soru_karti():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(220, 35, 'هَلْ أَنْتِ مَرْيَمُ؟', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 83, 'Zeynep:', MOR, 'start', kalin=True)
    ic += ar_yazi(220, 85, '؟', MOR)
    return svg(360, 106, ic, 'Sen Meryem misin sorusuna Zeynep’in verdiği doğrulama cevabı kartı.', 21)


def uc_harfli_birlestirme():
    kartlar = [
        ('1. Kelime', 'كَ - تَ - بَ', MAVI, MAVI_A),
        ('2. Kelime', 'نَ - ظَ - رَ', YES, YES_A),
        ('3. Kelime', 'قَ - رَ - أَ', TUR, TUR_A),
        ('4. Kelime', 'جَ - لَ - سَ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, harfler, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 124, y + 31, harfler, LAC)
    return svg(360, 110, ic, 'Üç harfli dört kelimenin ayrı harflerini gösteren kartlar.', 22)


def kaf_kef_karsilastirma():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Kâf Harfi (ق)', TUR, kalin=True)
    ic += ar_yazi(91, 56, 'قَ · قُ · قِ', LAC)
    ic += tr_yazi(91, 80, 'Örnek: قَلَمٌ (Kalem)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Kef Harfi (ك)', MAVI, kalin=True)
    ic += ar_yazi(269, 56, 'كَ · كُ · كِ', LAC)
    ic += tr_yazi(269, 80, 'Örnek: كَتَبَ (Yazdı)', LAC)
    return svg(360, 100, ic, 'Kâf ve Kef harflerinin nokta ve ses karşılaştırma panosu.', 21)


def alfabe_sira_ciftleri():
    gruplar = [
        ('Grup K', 'ع - غ', YES, YES_A),
        ('Grup L', 'ط - ظ', MAVI, MAVI_A),
        ('Grup M', 'و - ي', MOR, MOR_A),
        ('Grup N', 'ك - ل', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, cift, renk, arka) in enumerate(gruplar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += ar_yazi(x + 41, 66, cift, LAC)
    return svg(360, 96, ic, 'Arap alfabesinin üçüncü grubundan dört harf çifti.', 21)


def nezaketli_yonerge_kartlari():
    kartlar = [
        ('1 · Ömer (E)', 'قُمْ مِنْ فَضْلِكَ', MAVI, MAVI_A),
        ('2 · Fatma (K)', 'اِقْرَئِي مِنْ فَضْلِكِ', YES, YES_A),
        ('3 · Ayşe (K)', 'اُكْتُبْ مِنْ فَضْلِكَ', KIR, '#fdeaea'),
        ('4 · Hasan (E)', 'اِجْلِسْ مِنْ فَضْلِكَ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 86, y + 40, metin, LAC)
    return svg(360, 110, ic, 'Lütfen ifadesiyle kullanılan dört sınıf içi yönerge kartı.', 22)


def birlesmeyen_alti_harf_panosu():
    ic = f'<rect x="6" y="6" width="348" height="90" rx="10" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 24, 'Kendinden Sonraki Harfle Birleşmeyen 6 Harf', TUR, kalin=True)
    ic += ar_yazi(180, 58, 'ا · د · ذ · ر · ز · و', LAC)
    ic += tr_yazi(180, 82, 'Bu harfler sağdakine bitişir, soldaki harfe bitişmez.', LAC)
    return svg(360, 102, ic, 'Kendinden sonraki harfle birleşmeyen altı harf panosu.', 21)


def feteha_vecede_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Tam Bitişik Kelime', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'فَتَحَ', LAC)
    ic += tr_yazi(91, 80, 'fe - te - ha (Açtı)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Vâv İle Başlayan Kelime', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'وَجَدَ', LAC)
    ic += tr_yazi(269, 80, 've - ce - de (Buldu)', LAC)
    return svg(360, 100, ic, 'Feteha ve vecede kelimelerinin yazılış karşılaştırması.', 21)


def son_grup_kutulari():
    kartlar = [
        ('1. Kutu', 'ك', MAVI, MAVI_A),
        ('2. Kutu', 'ل', YES, YES_A),
        ('3. Kutu', 'م', TUR, TUR_A),
        ('4. Kutu', 'هـ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, harf, LAC)
    return svg(360, 96, ic, 'Kef, Lâm, Mîm ve Hâ harf kutuları.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ucuncu_grup_ikililer()
    s[4]['gorsel'] = dogrulama_soru_karti()
    s[5]['gorsel'] = uc_harfli_birlestirme()
    s[6]['gorsel'] = kaf_kef_karsilastirma()
    s[7]['gorsel'] = alfabe_sira_ciftleri()
    s[8]['gorsel'] = nezaketli_yonerge_kartlari()
    s[9]['gorsel'] = birlesmeyen_alti_harf_panosu()
    s[11]['gorsel'] = feteha_vecede_panosu()
    s[12]['gorsel'] = son_grup_kutulari()
