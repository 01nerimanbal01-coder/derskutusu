"""5. sınıf Arapça 2. hafta (Selamlaşma-Tanışma Diyalogları ve İkinci Harf Grubu د ذ ر ز س ش ص ض) çalışma kâğıdı görselleri.
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


def kardes_harf_ciftleri():
    kartlar = [
        ('1. Kart', 'د - ذ', MAVI, MAVI_A),
        ('2. Kart', 'ر - ز', YES, YES_A),
        ('3. Kart', 'س - ش', TUR, TUR_A),
        ('4. Kart', 'ص - ض', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cift, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, cift, LAC)
    return svg(360, 96, ic, 'Dört kardeş harf çifti kartı: Dal-Zel, Ra-Ze, Sin-Şın, Sad-Dad.', 21)


def tanisma_zamir_panolari():
    kartlar = [
        ('K · Ahmet (E)', 'كَيْفَ حَالُكَ؟', MAVI, MAVI_A),
        ('L · Meryem (K)', 'مَا اسْمُكَ؟', KIR, '#fdeaea'),
        ('M · Zeynep (K)', 'أَهْلًا بِكِ', YES, YES_A),
        ('N · Ali (E)', 'أَهْلًا بِكَ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 132, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört tanışma ve hitap panosu: K Ahmet, L Meryem, M Zeynep, N Ali.', 22)


def harekeli_harf_kartlari():
    kartlar = [
        ('1. Kart', 'دَ', MAVI, MAVI_A),
        ('2. Kart', 'شُ', YES, YES_A),
        ('3. Kart', 'صِ', TUR, TUR_A),
        ('4. Kart', 'زَ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, harf, LAC)
    return svg(360, 96, ic, 'Harekeli dört harf kartı: de, şü, sı, ze.', 21)


def bitisme_karsilastirma_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Ayrık Yazılan Harfler', TUR, kalin=True)
    ic += ar_yazi(91, 56, 'دَرَجَ', LAC)
    ic += tr_yazi(91, 80, 'de - ra - ce (Sola bitişmez)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Bitişen Harfler', YESIL_K, kalin=True)
    ic += ar_yazi(269, 56, 'صَبَرَ', LAC)
    ic += tr_yazi(269, 80, 'sa - be - ra (Bitişik yazılır)', LAC)
    return svg(360, 100, ic, 'Derece ve sabera kelimelerinde harf birleşme karşılaştırması.', 21)


def diyalog_akis_kartlari():
    adimlar = [
        ('Adım K', 'مَا اسْمُكَ؟', TUR, TUR_A),
        ('Adım L', 'اَلسَّلَامُ عَلَيْكُمْ', MAVI, MAVI_A),
        ('Adım M', 'إِلَى اللِّقَاءِ', MOR, MOR_A),
        ('Adım N', 'تَشَرَّفْتُ', YES, YES_A),
    ]
    ic = ''
    for i, (bas, soz, renk, arka) in enumerate(adimlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 12, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 122, y + 31, soz, LAC)
    return svg(360, 110, ic, 'Tanışma diyaloğunun dört aşamasını gösteren kartlar.', 22)


def harf_birlestirme_semasi():
    ic = f'<rect x="6" y="6" width="214" height="84" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(113, 24, 'Ayrı Harfler (Sağdan Sola)', MAVI, kalin=True)
    ic += ar_yazi(113, 62, 'شَ - رِ - بَ', LAC)

    ic += f'<rect x="230" y="6" width="124" height="84" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(292, 24, 'Birleşik Yazılış', YESIL_K, kalin=True)
    ic += ar_yazi(292, 62, '؟', YESIL_K)
    return svg(360, 96, ic, 'Şe, ri, be harflerinin birleştirilme şeması.', 21)


def hareke_grup_panosu():
    kartlar = [
        ('1. Seçim', 'سَ', YES, YES_A),
        ('2. Seçim', 'صَ', MAVI, MAVI_A),
        ('3. Seçim', 'ذُ', KIR, '#fdeaea'),
        ('4. Seçim', 'ضَ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += ar_yazi(x + 41, 68, harf, LAC)
    return svg(360, 96, ic, 'Fethalı ve dammalı harf seçim kartları.', 21)


def satir_cizgisi_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Satır Üstü Harfler', MAVI, kalin=True)
    ic += f'<line x1="24" y1="64" x2="158" y2="64" stroke="{GRI}" stroke-width="1.2" stroke-dasharray="4,3"/>'
    ic += ar_yazi(91, 60, 'د · ذ', LAC)
    ic += tr_yazi(91, 82, 'Tamamı çizgi üstünde', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Çanaklı Harfler', MOR, kalin=True)
    ic += f'<line x1="202" y1="54" x2="336" y2="54" stroke="{GRI}" stroke-width="1.2" stroke-dasharray="4,3"/>'
    ic += ar_yazi(269, 58, 'س · ش', LAC)
    ic += tr_yazi(269, 82, 'Dişler üstte, çanak altta', LAC)
    return svg(360, 100, ic, 'Dal-Zel ve Sin-Şın harflerinin satır çizgisine göre konumu.', 21)


def sabah_selam_diyalogu():
    ic = f'<rect x="6" y="6" width="348" height="44" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 33, 'Selim:', TUR, 'start', kalin=True)
    ic += ar_yazi(220, 35, 'صَبَاحُ الْخَيْرِ', LAC)

    ic += f'<rect x="6" y="56" width="348" height="44" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(18, 83, 'Arkadaşı:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(220, 85, '؟', YESIL_K)
    return svg(360, 106, ic, 'Sabah selamlaşması diyalog kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kardes_harf_ciftleri()
    s[4]['gorsel'] = tanisma_zamir_panolari()
    s[5]['gorsel'] = harekeli_harf_kartlari()
    s[6]['gorsel'] = bitisme_karsilastirma_panosu()
    s[7]['gorsel'] = diyalog_akis_kartlari()
    s[8]['gorsel'] = harf_birlestirme_semasi()
    s[9]['gorsel'] = hareke_grup_panosu()
    s[11]['gorsel'] = satir_cizgisi_panosu()
    s[12]['gorsel'] = sabah_selam_diyalogu()
