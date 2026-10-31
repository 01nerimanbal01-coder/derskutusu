"""6. sınıf Arapça 7. hafta (Harf-i Tarif ile Akraba ve Meslek Diyalogları - 1. Ünite Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 12 pt, Arapça yazı Arial 22 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def dort_meslek_harfi_tarif():
    kartlar = [
        ('1. Kart', 'الطَّبِيبُ', TUR, TUR_A),
        ('2. Kart', 'التَّاجِرُ', MOR, MOR_A),
        ('3. Kart', 'الْفَلَّاحُ', YES, YES_A),
        ('4. Kart', 'النَّجَّارُ', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Üç şemsî ve bir kamerî meslek kartı.', 16)


def cinsiyet_uyumu_diyalog_kartlari():
    kartlar = [
        ('1. Kart', 'هٰذَا عَمِّي - هُوَ مُهَنْدِسٌ', MAVI, MAVI_A),
        ('2. Kart', 'هٰذِهِ خَالَتِي - هِيَ طَبِيبَةٌ', YES, YES_A),
        ('3. Kart', 'هٰذِهِ عَمَّتِي - هِيَ مُعَلِّمَةٌ', TUR, TUR_A),
        ('4. Kart', 'هٰذِهِ جَدَّتِي - هُوَ نَجَّارٌ', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Müzekker ve müennes uyumu kontrol kartları.', 16)


def baba_anne_tarafi_tablo_kartlari():
    kartlar = [
        ('1. Amcam', 'عَمِّي', MAVI, MAVI_A),
        ('2. Halam', 'عَمَّتِي', YES, YES_A),
        ('3. Dayım', 'خَالِي', TUR, TUR_A),
        ('4. Teyzem', 'خَالَتِي', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Baba ve anne tarafı dört akraba kartı.', 16)


def dayi_teyze_doktor_donusum():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, 'Müzekker (Eril):', MAVI, 'start', kalin=True)
    ic += ar_yazi(225, 35, 'هٰذَا خَالِي - هُوَ طَبِيبٌ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, 'Müennes (Dişil):', MOR, 'start', kalin=True)
    ic += ar_yazi(225, 87, '... خَالَتِي - ... ...', LAC)
    return svg(360, 110, ic, 'Müzekker cümleyi müennes biçime dönüştürme kartı.', 16)


def diyalog_sirasi_kartlari():
    kartlar = [
        ('Adım A', 'مَنْ هٰذَا؟', MAVI, MAVI_A),
        ('Adım B', 'هٰذَا خَالِي', YES, YES_A),
        ('Adım C', 'مَا مِهْنَةُ خَالِكَ؟', TUR, TUR_A),
        ('Adım D', 'خَالِي طَبِيبٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört adımlı akraba ve meslek diyaloğu kartları.', 16)


def semsi_kameri_meslek_tablosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Şemsî Meslekler', TUR, kalin=True)
    ic += ar_yazi(91, 54, 'الطَّبِيبُ - التَّاجِرُ', LAC)
    ic += ar_yazi(91, 82, 'الشُّرْطِيُّ - النَّجَّارُ', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Kamerî Meslekler', MAVI, kalin=True)
    ic += ar_yazi(269, 54, 'الْمُهَنْدِسُ - الْفَلَّاحُ', LAC)
    ic += ar_yazi(269, 82, 'الْمُعَلِّمُ - الْأَبُ', LAC)
    return svg(360, 100, ic, 'Şemsî ve kamerî harfle başlayan meslekler tablosu.', 16)


def amca_ciftlik_cumle_karti():
    ic = f'<rect x="6" y="14" width="348" height="82" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 36, 'Arapça Tanıtım Cümlesi', YESIL_K, kalin=True)
    ic += ar_yazi(180, 74, 'عَمِّي فَلَّاحٌ - هُوَ يَعْمَلُ فِي الْمَزْرَعَةِ', LAC)
    return svg(360, 106, ic, 'Amcanın çiftçi olduğunu ve çiftlikte çalıştığını belirten kart.', 16)


def muallim_tabib_donusum_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Dönüşüm (Kamerî)', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'مُعَلِّمٌ - اَلْمُعَلِّمُ', LAC)
    ic += tr_yazi(91, 80, 'el-muallimü', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Dönüşüm (Şemsî)', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'طَبِيبٌ - اَلطَّبِيبُ', LAC)
    ic += tr_yazi(269, 80, 'et-tabîbü', LAC)
    return svg(360, 100, ic, 'Kamerî ve şemsî iki meslek kelimesinde Harf-i Tarif dönüşümü.', 16)


def iki_soru_bosluk_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, '1. Kart:', MAVI, 'start', kalin=True)
    ic += ar_yazi(215, 35, '... أَبِيكَ؟ - أَبِي مُهَنْدِسٌ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, '2. Kart:', TUR, 'start', kalin=True)
    ic += ar_yazi(215, 87, '... عَمًّا لَكَ؟ - لِي عَمَّانِ', LAC)
    return svg(360, 110, ic, 'Meslek ve sayı sorma diyalog kartları.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_meslek_harfi_tarif()
    s[4]['gorsel'] = cinsiyet_uyumu_diyalog_kartlari()
    s[5]['gorsel'] = baba_anne_tarafi_tablo_kartlari()
    s[6]['gorsel'] = dayi_teyze_doktor_donusum()
    s[7]['gorsel'] = diyalog_sirasi_kartlari()
    s[8]['gorsel'] = semsi_kameri_meslek_tablosu()
    s[9]['gorsel'] = amca_ciftlik_cumle_karti()
    s[11]['gorsel'] = muallim_tabib_donusum_panosu()
    s[12]['gorsel'] = iki_soru_bosluk_karti()
