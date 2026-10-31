"""5. sınıf Arapça 7. hafta (Arap Alfabesindeki Harfler أ - ز Arası Harfler, Harekelerle Seslendirme ve Tanışma İfadeleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 12 pt, Arapça yazı Arial 22 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def kardes_harf_kartlari():
    kartlar = [
        ('1. Kart', 'ج', MAVI, MAVI_A),
        ('2. Kart', 'ح', YES, YES_A),
        ('3. Kart', 'خ', TUR, TUR_A),
        ('4. Kart', 'ث', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, harf, LAC)
    return svg(360, 96, ic, 'Cim, Ha, Hı ve Se kardeş harf kartları.', 18)


def isaret_ismi_kartlari():
    kartlar = [
        ('K · Eril Kişi', 'هٰذَا عَلِيٌّ', MAVI, MAVI_A),
        ('L · Dişil Kişi', 'هٰذِهِ زَيْنَبُ', YES, YES_A),
        ('M · Eril Nesne', 'هٰذَا دَفْتَرٌ', TUR, TUR_A),
        ('N · Dişil Nesne', 'هٰذَا حَقِيبَةٌ', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 124, y + 31, metin, LAC)
    return svg(360, 110, ic, 'Hâzâ ve Hâzihî işaret isimleriyle dört tanıtım kartı.', 18)


def ilk_grup_kelime_kartlari():
    kartlar = [
        ('1. Kart', 'تُفَّاحٌ', MAVI, MAVI_A),
        ('2. Kart', 'ثَوْبٌ', YES, YES_A),
        ('3. Kart', 'ذَهَبٌ', TUR, TUR_A),
        ('4. Kart', 'زَهْرَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, kel, LAC)
    return svg(360, 96, ic, 'Tüffâhun, sevbün, zehebün ve zehratün kelime kartları.', 18)


def haza_hazihi_nesne_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Müzekker (Eril) İsim', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'هٰذَا دَفْتَرٌ', LAC)
    ic += tr_yazi(91, 80, 'Bu bir defterdir.', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Müennes (Dişil - ة) İsim', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'هٰذِهِ حَقِيبَةٌ', LAC)
    ic += tr_yazi(269, 80, 'Bu bir çantadır.', LAC)
    return svg(360, 100, ic, 'Defter ve çanta kelimelerinde Hâzâ ve Hâzihî kullanımı.', 18)


def ilk_onbir_harf_vagonlari():
    gruplar = [
        ('Grup K', 'ج - ح - خ', YES, YES_A),
        ('Grup L', 'أ - ب - ت - ث', MAVI, MAVI_A),
        ('Grup M', 'ر - ز', MOR, MOR_A),
        ('Grup N', 'د - ذ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, dizi, renk, arka) in enumerate(gruplar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 116, y + 31, dizi, LAC)
    return svg(360, 110, ic, 'Elif’ten Ze’ye dört kardeş harf grubu kartı.', 18)


def cim_ha_hi_sifresi():
    kutular = [
        ('1 · Altta Nokta', '؟', MAVI, MAVI_A),
        ('2 · Noktasız', '؟', YES, YES_A),
        ('3 · Üstte Nokta', '؟', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, isaret, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 56, 24, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="32" x2="{x + 102}" y2="32" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 56, 68, isaret, LAC)
    return svg(360, 96, ic, 'Cim, Ha ve Hı harflerinin nokta yeri şifresi kutuları.', 18)


def ilk_grup_birlesmeyenler():
    ic = f'<rect x="6" y="6" width="348" height="90" rx="10" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 24, 'أ - ز Arasında Sonraki Harfle Birleşmeyenler', TUR, kalin=True)
    ic += ar_yazi(180, 56, 'أ · د · ذ · ر · ز', LAC)
    ic += tr_yazi(180, 82, 'Bu beş harf kendinden sonra gelen harfe bitişmez.', LAC)
    return svg(360, 102, ic, 'Elif, Dal, Zel, Ra ve Ze birleşmeyen harfler panosu.', 18)


def sukun_ornek_kartlari():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Kelime (Ekmek)', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'خُبْزٌ', LAC)
    ic += tr_yazi(91, 80, 'hub - zün (بْ cezimli)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Kelime (Kız)', MAVI, kalin=True)
    ic += ar_yazi(269, 56, 'بِنْتٌ', LAC)
    ic += tr_yazi(269, 80, 'bin - tün (نْ cezimli)', LAC)
    return svg(360, 100, ic, 'Hubzün ve bintün kelimelerinde sükûn işareti.', 18)


def tanitma_zamir_karti():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 33, 'Eril Tanıtım:', MAVI, 'start', kalin=True)
    ic += ar_yazi(225, 35, 'هٰذَا عُمَرُ، هُوَ طَالِبٌ.', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 83, 'Dişil Tanıtım:', MOR, 'start', kalin=True)
    ic += ar_yazi(225, 85, 'هٰذِهِ مَرْيَمُ، ؟ طَالِبَةٌ.', LAC)
    return svg(360, 106, ic, 'Ömer ve Meryem tanıtım cümlelerinde hüve ve hiye zamirleri.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kardes_harf_kartlari()
    s[4]['gorsel'] = isaret_ismi_kartlari()
    s[5]['gorsel'] = ilk_grup_kelime_kartlari()
    s[6]['gorsel'] = haza_hazihi_nesne_panosu()
    s[7]['gorsel'] = ilk_onbir_harf_vagonlari()
    s[8]['gorsel'] = cim_ha_hi_sifresi()
    s[9]['gorsel'] = ilk_grup_birlesmeyenler()
    s[11]['gorsel'] = sukun_ornek_kartlari()
    s[12]['gorsel'] = tanitma_zamir_karti()
