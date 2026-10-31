"""5. sınıf Arapça 4. hafta (Nezaket İfadeleri, Sınıf İçi Yönergeler, Harekeler ve Önce Selam Sonra Kelam Hadisi) çalışma kâğıdı görselleri.
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


def zit_yonerge_kartlari():
    kartlar = [
        ('1. Kart', 'قُمْ · اِجْلِسْ', MAVI, MAVI_A),
        ('2. Kart', 'اِقْرَأْ · اُكْتُبْ', YES, YES_A),
        ('3. Kart', 'قُمْ · اِقْرَأْ', TUR, TUR_A),
        ('4. Kart', 'اِجْلِسْ · اُكْتُبْ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cift, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 12, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 118, y + 31, cift, LAC)
    return svg(360, 110, ic, 'Dört sınıf içi yönerge çifti kartı.', 22)


def uc_hareke_panosu():
    kutular = [
        ('1. Kutu (Üstte Çizgi)', 'بَ', MAVI, MAVI_A),
        ('2. Kutu (Altta Çizgi)', 'بِ', YES, YES_A),
        ('3. Kutu (Üstte Vâv)', 'بُ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, harf, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 56, 24, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="32" x2="{x + 102}" y2="32" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 56, 68, harf, LAC)
    return svg(360, 96, ic, 'Be harfinin fetha, kesra ve damme harekeleriyle görünümü.', 21)


def hadis_kelime_panosu():
    ic = f'<rect x="6" y="6" width="348" height="90" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 24, '1. Ünite Hadis-i Şerifi · Kelime Çözümlemesi', MOR, kalin=True)
    ic += ar_yazi(180, 58, 'اَلسَّلَامُ · قَبْلَ · الْكَلَامِ', LAC)
    ic += tr_yazi(180, 82, '1. اَلسَّلَامُ   -   2. قَبْلَ   -   3. الْكَلَامِ', LAC)
    return svg(360, 102, ic, 'Es-selâmü kablel-kelâm hadisinin üç kelimesi.', 21)


def zamir_nezaket_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Eril Hitap (Sen)', MAVI, kalin=True)
    ic += ar_yazi(91, 55, 'أَنْتَ · مِنْ فَضْلِكَ', LAC)
    ic += tr_yazi(91, 80, 'Ente · Min fadlike', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Dişil Hitap (Sen)', MOR, kalin=True)
    ic += ar_yazi(269, 55, 'أَنْتِ · مِنْ فَضْلِكِ', LAC)
    ic += tr_yazi(269, 80, 'Enti · Min fadliki', LAC)
    return svg(360, 100, ic, 'Ente ve Enti zamirleriyle lütfen kalıbının kullanımı.', 21)


def yazim_adimlari_semasi():
    adimlar = [
        ('Aşama K', 'Önce Gövde', MAVI, MAVI_A),
        ('Aşama L', 'Sağdan Başla', YES, YES_A),
        ('Aşama M', 'En Son Hareke', MOR, MOR_A),
        ('Aşama N', 'Sonra Nokta', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, aciklama, renk, arka) in enumerate(adimlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="36" x2="{x + 72}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += tr_yazi(x + 41, 60, aciklama, LAC)
    return svg(360, 92, ic, 'Arap harflerini ve harekelerini yazma aşamaları.', 20)


def hel_enti_diyalog_karti():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(220, 35, 'هَلْ أَنْتِ مُعَلِّمَةٌ؟', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 83, 'Kız Öğrenci:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(220, 85, '؟', YESIL_K)
    return svg(360, 106, ic, 'Sen kadın öğretmen misin sorusuna kız öğrencinin cevabı.', 21)


def satir_ustu_alti_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Satır Üstüne Oturanlar', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'أ · ب · د · ط · ف · ك', LAC)
    ic += tr_yazi(91, 80, 'Çizgi altına inmez', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Satır Altına İnenler', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'ح · ر · س · ص · ع · ق', LAC)
    ic += tr_yazi(269, 80, 'Kuyruk/çanak alta iner', LAC)
    return svg(360, 100, ic, 'Satır çizgisinin üstüne oturan ve altına inen harfler.', 21)


def ali_zeynep_tanisma_karti():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 33, 'Ali (1. Söz):', TUR, 'start', kalin=True)
    ic += ar_yazi(225, 35, 'اَلسَّلَامُ عَلَيْكُمْ', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 83, 'Ali (2. Söz):', MAVI, 'start', kalin=True)
    ic += ar_yazi(225, 85, 'مَا اسْمُكِ؟', LAC)
    return svg(360, 106, ic, 'Ali’nin önce selam verip sonra isim sorduğu konuşma kartı.', 21)


def fatma_yonerge_panosu():
    ic = f'<rect x="6" y="6" width="348" height="90" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 25, 'Öğretmenin Kız Öğrenci Fatma’ya Yönergesi', MOR, kalin=True)
    ic += ar_yazi(180, 58, 'يَا فَاطِمَةُ، ؟', LAC)
    ic += tr_yazi(180, 82, 'İstenen Eylem: Ayağa kalk ve oku! (Dişil)', LAC)
    return svg(360, 102, ic, 'Kız öğrenci Fatma’ya ayağa kalk ve oku yönergesi panosu.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = zit_yonerge_kartlari()
    s[4]['gorsel'] = uc_hareke_panosu()
    s[5]['gorsel'] = hadis_kelime_panosu()
    s[6]['gorsel'] = zamir_nezaket_panosu()
    s[7]['gorsel'] = yazim_adimlari_semasi()
    s[8]['gorsel'] = hel_enti_diyalog_karti()
    s[9]['gorsel'] = satir_ustu_alti_panosu()
    s[11]['gorsel'] = ali_zeynep_tanisma_karti()
    s[12]['gorsel'] = fatma_yonerge_panosu()
