"""6. sınıf Arapça 5. hafta (Mesleklerin Çalışma Yerleri, Fiil Cümlesi, Şemsî-Kamerî Harfler ve Sıla-i Rahim) çalışma kâğıdı görselleri.
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


def meslek_isyeri_kartlari():
    kartlar = [
        ('1. Kart', 'مُهَنْدِسٌ - فِي الْفُرْنِ', TUR, TUR_A),
        ('2. Kart', 'عَامِلٌ - فِي الْمَصْنَعِ', YES, YES_A),
        ('3. Kart', 'خَبَّازٌ - فِي الصَّيْدَلِيَّةِ', MAVI, MAVI_A),
        ('4. Kart', 'فَلَّاحٌ - فِي الْمَحْكَمَةِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Meslek ve iş yeri eşleştirme kartları.', 18)


def fi_harfi_cer_kutulari():
    kartlar = [
        ('1. Kutu', 'فِي الْمَدْرَسَةِ', YES, YES_A),
        ('2. Kutu', 'فِي الْمَصْنَعُ', KIR, '#fdeaea'),
        ('3. Kutu', 'فِي الشَّرِكَةِ', MAVI, MAVI_A),
        ('4. Kutu', 'فِي الْمَزْرَعَةِ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'fî harf-i cerri ve son hareke kontrol kutuları.', 18)


def isyeri_tablo_kartlari():
    kartlar = [
        ('1', 'فِي الْمُسْتَشْفَى', MAVI, MAVI_A),
        ('2', 'فِي الْمَصْنَعِ', YES, YES_A),
        ('3', 'فِي الْمَزْرَعَةِ', TUR, TUR_A),
        ('4', 'فِي الْمَطْعَمِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 12, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört iş yeri kartı.', 18)


def ulama_karsilastirma_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Kamerî Geçiş', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'فِي الْمَزْرَعَةِ', LAC)
    ic += tr_yazi(91, 80, 'Okunuş: fi’l-mezra’ati', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Şemsî Geçiş', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'فِي الشَّرِكَةِ', LAC)
    ic += tr_yazi(269, 80, 'Okunuş: fi’ş-şeriketi', LAC)
    return svg(360, 100, ic, 'fî edatıyla kamerî ve şemsî ulama okunuşu panosu.', 18)


def dayi_butuncul_tanitim_kartlari():
    kartlar = [
        ('1. Adım', 'هٰذَا خَالِي', MAVI, MAVI_A),
        ('2. Adım', 'هُوَ مُهَنْدِسٌ نَشِيطٌ', YES, YES_A),
        ('3. Adım', 'يَعْمَلُ فِي الشَّرِكَةِ', TUR, TUR_A),
        ('4. Adım', 'أَنَا أُحِبُّ خَالِي', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Dayıyı dört aşamada tanıtan bütüncül paragraf kartları.', 18)


def silai_rahim_panosu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Vecize:', TUR, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'اَلْأَقْرَبُونَ أَوْلَى بِالْمَعْرُوفِ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(180, 85, 'Sıla-i Rahim: Akrabaları ziyaret etmek ve bağları korumak', YESIL_K, kalin=True)
    return svg(360, 110, ic, 'Sıla-i rahim ve akrabalık hukuku panosu.', 18)


def teyze_hastane_diyalogu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'أَيْنَ تَعْمَلُ خَالَتُكَ؟', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 85, 'Cevap (Hastanede):', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(235, 87, '؟', YESIL_K)
    return svg(360, 110, ic, 'Teyzenin nerede çalıştığını soran diyalog kartı.', 18)


def teyze_doktor_paragraf_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, '1. Cümle:', MOR, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'هٰذِهِ خَالَتِي - هِيَ طَبِيبَةٌ مَاهِرَةٌ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, '2. Cümle:', MAVI, 'start', kalin=True)
    ic += ar_yazi(215, 87, 'هِيَ تَعْمَلُ فِي الْمُسْتَشْفَى', LAC)
    return svg(360, 110, ic, 'Teyzeyi ve çalıştığı hastaneyi tanıtan iki cümle kartı.', 18)


def dortlu_ulama_kartlari():
    kartlar = [
        ('1. Kart', 'فِي الْمُسْتَشْفَى', MAVI, MAVI_A),
        ('2. Kart', 'فِي الْمَكْتَبِ', YES, YES_A),
        ('3. Kart', 'فِي الصَّيْدَلِيَّةِ', TUR, TUR_A),
        ('4. Kart', 'فِي الدُّكَّانِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'fî edatıyla dört iş yeri ulama kartı.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = meslek_isyeri_kartlari()
    s[4]['gorsel'] = fi_harfi_cer_kutulari()
    s[5]['gorsel'] = isyeri_tablo_kartlari()
    s[6]['gorsel'] = ulama_karsilastirma_panosu()
    s[7]['gorsel'] = dayi_butuncul_tanitim_kartlari()
    s[8]['gorsel'] = silai_rahim_panosu()
    s[9]['gorsel'] = teyze_hastane_diyalogu()
    s[11]['gorsel'] = teyze_doktor_paragraf_karti()
    s[12]['gorsel'] = dortlu_ulama_kartlari()
