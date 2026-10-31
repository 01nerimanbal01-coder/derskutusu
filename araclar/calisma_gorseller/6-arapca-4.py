"""6. sınıf Arapça 4. hafta (Harf-i Tarif, Şemsî ve Kamerî Harfler, Nitelik Sıfatları ve Akrabalık Vecizesi) çalışma kâğıdı görselleri.
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


def semsi_dortlu_panosu():
    kartlar = [
        ('1. Meslek (س)', 'اَلسّائِقُ', TUR, TUR_A),
        ('2. Meslek (ط)', 'اَلطَّبّاخُ', MAVI, MAVI_A),
        ('3. Meslek (ش)', 'اَلشُّرْطِيُّ', YES, YES_A),
        ('4. Meslek (ض)', 'اَلضّابِطُ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 124, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Ünitedeki şemsî harfle başlayan dört meslek kartı.', 18)


def nitelik_sifati_uyum_kartlari():
    kartlar = [
        ('1. Kart', 'عَمّي طَبّاخٌ ماهِرٌ', MAVI, MAVI_A),
        ('2. Kart', 'خالي فَلّاحٌ نَشيطٌ', YES, YES_A),
        ('3. Kart', 'عَمَّتي طَبّاخَةٌ ماهِرَةٌ', TUR, TUR_A),
        ('4. Kart', 'خالَتي مُحامِيَةٌ ماهِرٌ', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Meslek ve nitelik sıfatı uyumu cümle kartları.', 18)


def harfi_tarif_tablo_kartlari():
    kartlar = [
        ('1', 'مُمَرِّضٌ', MAVI, MAVI_A),
        ('2', 'سائِقٌ', TUR, TUR_A),
        ('3', 'عَمٌّ', YES, YES_A),
        ('4', 'شُرْطِيٌّ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 14, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Başına Harf-i Tarif eklenecek dört belirsiz kelime kartı.', 18)


def eril_disil_ciftci_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, 'Eril (Amcam):', MAVI, 'start', kalin=True)
    ic += ar_yazi(225, 35, 'عَمّي فَلّاحٌ نَشيطٌ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, 'Dişil (Halam):', MOR, 'start', kalin=True)
    ic += ar_yazi(225, 87, 'عَمَّتي ...', LAC)
    return svg(360, 110, ic, 'Eril cümleyi dişil özneye dönüştürme kartı.', 18)


def paragraf_cumle_kartlari():
    kartlar = [
        ('A', 'هٰذِهِ عائِلَتي - والِدي مُعَلِّمٌ', MAVI, MAVI_A),
        ('B', 'وَوالِدَتي مُمَرِّضَةٌ ماهِرَةٌ', YES, YES_A),
        ('C', 'لي عَمٌّ واحِدٌ - طَبّاخٌ ماهِرٌ', TUR, TUR_A),
        ('D', 'أَنا أُحِبُّ أَقارِبي كَثيرًا', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Geniş aileyi tanıtan dört cümlelik paragraf şeması.', 18)


def cezim_sedde_ipucu_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Grup (Şeddeli)', TUR, kalin=True)
    ic += ar_yazi(91, 56, 'اَلشَّمْسُ - اَلطَّبّاخُ', LAC)
    ic += tr_yazi(91, 80, 'İlk harfte şedde (ّ ) var', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Grup (Cezimli)', MAVI, kalin=True)
    ic += ar_yazi(269, 56, 'اَلْقَمَرُ - اَلْمُعَلِّمُ', LAC)
    ic += tr_yazi(269, 80, 'Lam harfinde cezim (ْ ) var', LAC)
    return svg(360, 100, ic, 'Şedde ve cezim işaretleriyle şemsî-kamerî ayrımı panosu.', 18)


def dayi_olumsuz_olumlu_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, '1. Bölüm:', KIR, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'لا يَعْمَلُ خالي في الْمَطْعَمِ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, '2. Bölüm:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(215, 87, 'هُوَ يَعْمَلُ في الْمَزْرَعَةِ', LAC)
    return svg(360, 110, ic, 'Dayının çalışmadığı ve çalıştığı yeri gösteren cümle kartı.', 18)


def altin_kural_tenvin_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Yazım', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'اَلطَّبّاخُ', LAC)
    ic += tr_yazi(91, 80, 'Tek ötre (-u)', YESIL_K)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Yazım', KIR, kalin=True)
    ic += ar_yazi(269, 56, 'اَلطَّبّاخٌ', LAC)
    ic += tr_yazi(269, 80, 'İki ötre / tenvin (-un)', KIR)
    return svg(360, 100, ic, 'Harf-i Tarif ile tek ötre ve tenvin karşılaştırma kartı.', 18)


def baba_anne_nerede_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, '1. Diyalog:', MAVI, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'أَيْنَ والِدُكَ؟ - والِدي في الْعَمَلِ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, '2. Diyalog:', TUR, 'start', kalin=True)
    ic += ar_yazi(215, 87, 'أَيْنَ والِدَتُكَ؟ - والِدَتي في الْبَيْتِ', LAC)
    return svg(360, 110, ic, 'Baba ve annenin nerede olduğunu soran iki diyalog kartı.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = semsi_dortlu_panosu()
    s[4]['gorsel'] = nitelik_sifati_uyum_kartlari()
    s[5]['gorsel'] = harfi_tarif_tablo_kartlari()
    s[6]['gorsel'] = eril_disil_ciftci_karti()
    s[7]['gorsel'] = paragraf_cumle_kartlari()
    s[8]['gorsel'] = cezim_sedde_ipucu_panosu()
    s[9]['gorsel'] = dayi_olumsuz_olumlu_karti()
    s[11]['gorsel'] = altin_kural_tenvin_karti()
    s[12]['gorsel'] = baba_anne_nerede_karti()
