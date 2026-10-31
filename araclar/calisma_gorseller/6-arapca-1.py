"""6. sınıf Arapça 1. hafta (Aile Bireyleri, Meslekler ve Belirli İsimler) çalışma kâğıdı görselleri.
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


def akraba_tanitim_kartlari():
    kartlar = [
        ('1. Kart', 'خَالِي مُعَلِّم', MAVI, MAVI_A),
        ('2. Kart', 'عَمِّي طَبَّاخ', YES, YES_A),
        ('3. Kart', 'عَمَّتِي مُمَرِّضَة', TUR, TUR_A),
        ('4. Kart', 'خَالَتِي مُحَامِيَة', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 96, y + 40, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört akraba ve meslek tanıtım kartı.', 18)


def eril_disil_meslek_kutulari():
    kartlar = [
        ('1. Kutu', 'مُعَلِّم - مُعَلِّمَة', MAVI, MAVI_A),
        ('2. Kutu', 'طَبَّاخ - طَبَّاخَة', YES, YES_A),
        ('3. Kutu', 'شُرْطِيّ - فَلَّاح', KIR, '#fdeaea'),
        ('4. Kutu', 'مُمَرِّض - مُمَرِّضَة', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 96, y + 40, ar_metin, LAC)
    return svg(360, 110, ic, 'Mesleklerin eril ve dişil eşleştirme kutuları.', 18)


def belirli_isim_kartlari():
    kartlar = [
        ('1', 'الْبَيْت', MAVI, MAVI_A),
        ('2', 'الدَّرْس', TUR, TUR_A),
        ('3', 'الْحَقِيبَة', YES, YES_A),
        ('4', 'التِّلْفَاز', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 14, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Kameri ve şemsi harfli dört belirli isim kartı.', 18)


def meslek_soru_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Eril Meslek Sorusu', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'مَا مِهْنَتُهُ؟', LAC)
    ic += tr_yazi(91, 80, 'Onun (erkek) mesleği ne?', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Dişil Meslek Sorusu', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'مَا مِهْنَتُهَا؟', LAC)
    ic += tr_yazi(269, 80, 'Onun (kadın) mesleği ne?', LAC)
    return svg(360, 100, ic, 'Eril ve dişil zamirli meslek sorma kalıpları.', 18)


def tanitma_basamaklari_semasi():
    kartlar = [
        ('Kim?', 'هَذَا خَالِي', MAVI, MAVI_A),
        ('Meslek', 'هُوَ مُعَلِّمٌ', YES, YES_A),
        ('Özellik', 'مَاهِرٌ وَنَشِيطٌ', TUR, TUR_A),
        ('Yer', 'يَعْمَلُ فِي مَدْرَسَتِي', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 96, y + 40, ar_metin, LAC)
    return svg(360, 110, ic, 'Bir akrabayı dört basamakta tanıtma şeması.', 18)


def dayi_calisma_yeri_diyalogu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(210, 35, 'أَيْنَ يَعْمَلُ خَالُكَ؟', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 85, 'Eksik Cevap:', TUR, 'start', kalin=True)
    ic += ar_yazi(210, 87, 'خَالِي مُعَلِّمٌ', LAC)
    return svg(360, 110, ic, 'Dayının nerede çalıştığını soran diyalog kartı.', 18)


def anne_sifat_tamamlama_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Cümle:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'وَالِدَتِي طَبَّاخَةٌ ...', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(180, 85, 'Anlamı: Annem becerikli bir aşçıdır.', LAC, kalin=True)
    return svg(360, 110, ic, 'Kadın aşçı için nitelik sıfatı tamamlama kartı.', 18)


def kameri_semsi_karsilastirma():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Kameri Harf (ب)', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'الْبَيْت', LAC)
    ic += tr_yazi(91, 80, 'Lam okunur: el-beyt', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Şemsi Harf (د)', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'الدَّرْس', LAC)
    ic += tr_yazi(269, 80, 'Dal şeddeli: ed-ders', LAC)
    return svg(360, 100, ic, 'Kameri ve şemsi harfli iki kelimenin karşılaştırma panosu.', 18)


def calisma_fiil_kartlari():
    kartlar = [
        ('A', 'هُوَ يَعْمَلُ', MAVI, MAVI_A),
        ('B', 'هِيَ تَعْمَلُ', YES, YES_A),
        ('C', 'لَا يَعْمَلُ', TUR, TUR_A),
        ('D', 'لَا تَعْمَلُ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 14, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Olumlu ve olumsuz çalışma fiili kartları.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = akraba_tanitim_kartlari()
    s[4]['gorsel'] = eril_disil_meslek_kutulari()
    s[5]['gorsel'] = belirli_isim_kartlari()
    s[6]['gorsel'] = meslek_soru_panosu()
    s[7]['gorsel'] = tanitma_basamaklari_semasi()
    s[8]['gorsel'] = dayi_calisma_yeri_diyalogu()
    s[9]['gorsel'] = anne_sifat_tamamlama_karti()
    s[11]['gorsel'] = kameri_semsi_karsilastirma()
    s[12]['gorsel'] = calisma_fiil_kartlari()
