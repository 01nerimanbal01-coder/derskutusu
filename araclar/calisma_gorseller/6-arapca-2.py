"""6. sınıf Arapça 2. hafta (Akrabalarım: Dinleme Metni, Kameri ve Şemsi Harfler) çalışma kâğıdı görselleri.
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


def yasemin_ailesi_kartlari():
    kartlar = [
        ('Dede', 'هَذا جَدّي وَهُوَ طَبّاخ', MAVI, MAVI_A),
        ('Nine', 'جَدَّتي زَهْرَة مُتَقاعِدَة', MOR, MOR_A),
        ('Baba', 'والِدي أَحْمَد مُحامٍ', YES, YES_A),
        ('Anne', 'والِدَتي فاطِمَة مُعَلِّمَة', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 96, y + 40, ar_metin, LAC)
    return svg(360, 110, ic, 'Yasemin’in dört aile bireyini tanıtan cümle kartları.', 18)


def hareke_kontrol_kartlari():
    kartlar = [
        ('1. Kart', 'الدَّرْس', YES, YES_A),
        ('2. Kart', 'الْمَطْبَخ', MAVI, MAVI_A),
        ('3. Kart', 'اَلْتِلْميذ', KIR, '#fdeaea'),
        ('4. Kart', 'النّافِذَة', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 114, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Şemsi ve kameri kelimelerde hareke kontrol kartları.', 18)


def akraba_meslek_siniflama_kartlari():
    kartlar = [
        ('1', 'جَدَّة', MAVI, MAVI_A),
        ('2', 'طَبّاخ', TUR, TUR_A),
        ('3', 'والِد', YES, YES_A),
        ('4', 'مُحامِيَة', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 14, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Akraba ve meslek sınıflama kartları.', 18)


def zamir_karsilastirma_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Eril Tanıtım Kalıbı', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'هَذا جَدّي · هُوَ طَبّاخ', LAC)
    ic += tr_yazi(91, 80, 'Bu dedem, o aşçıdır.', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Dişil Tanıtım Kalıbı', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'هَذِهِ أُمِّي · هِيَ مُعَلِّمَة', LAC)
    ic += tr_yazi(269, 80, 'Bu annem, o öğretmendir.', LAC)
    return svg(360, 100, ic, 'Eril ve dişil akraba tanıtım cümle kalıpları.', 18)


def dinleme_sirasi_panosu():
    kartlar = [
        ('A', 'جَدّي - طَبّاخ', MAVI, MAVI_A),
        ('B', 'جَدَّتي - مُتَقاعِدَة', MOR, MOR_A),
        ('C', 'والِدي - مُحامٍ', YES, YES_A),
        ('D', 'والِدَتي - مُعَلِّمَة', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 96, y + 40, ar_metin, LAC)
    return svg(360, 110, ic, 'Dinleme metnindeki aile bireyleri sırası.', 18)


def ay_gunes_kelime_panosu():
    kartlar = [
        ('1. Kelime', 'الْبُرْتُقال', MAVI, MAVI_A),
        ('2. Kelime', 'الْجَمَل', YES, YES_A),
        ('3. Kelime', 'الْخُبْز', MOR, MOR_A),
        ('4. Kelime', 'الرُّمّان', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 118, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Üç kameri ve bir şemsi kelimeden oluşan pano.', 18)


def hel_soru_cevap_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'هَلِ الْوالِدَة مُحامِيَة؟', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 85, 'Metin Bilgisi: Anne Fatma öğretmendir.', YESIL_K, 'start', kalin=True)
    return svg(360, 110, ic, 'Annenin avukat olup olmadığını soran diyalog kartı.', 18)


def belirsiz_belirli_ev_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Durum (Belirsiz)', LAC, kalin=True)
    ic += ar_yazi(91, 56, 'بَيْت', LAC)
    ic += tr_yazi(91, 80, 'Herhangi bir ev', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Durum (Belirli)', YESIL_K, kalin=True)
    ic += ar_yazi(269, 56, 'الْبَيْت', LAC)
    ic += tr_yazi(269, 80, 'O bilinen ev', LAC)
    return svg(360, 100, ic, 'Belirsiz ve belirli isim karşılaştırma kartı.', 18)


def mekan_ipucu_kartlari():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Kart: Tarla / Ekin', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'جَدّي ...', LAC)
    ic += tr_yazi(91, 80, 'İpucu: Toprak ve hasat', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Kart: Sınıf / Tahta', MAVI, kalin=True)
    ic += ar_yazi(269, 56, 'والِدَتي ...', LAC)
    ic += tr_yazi(269, 80, 'İpucu: Yazı tahtası ve ders', LAC)
    return svg(360, 100, ic, 'Tarla ve sınıf ipuçlarıyla meslek bulma kartları.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yasemin_ailesi_kartlari()
    s[4]['gorsel'] = hareke_kontrol_kartlari()
    s[5]['gorsel'] = akraba_meslek_siniflama_kartlari()
    s[6]['gorsel'] = zamir_karsilastirma_panosu()
    s[7]['gorsel'] = dinleme_sirasi_panosu()
    s[8]['gorsel'] = ay_gunes_kelime_panosu()
    s[9]['gorsel'] = hel_soru_cevap_karti()
    s[11]['gorsel'] = belirsiz_belirli_ev_karti()
    s[12]['gorsel'] = mekan_ipucu_kartlari()
