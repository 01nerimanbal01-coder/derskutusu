"""5. sınıf Arapça 6. hafta (Selamlaşma, Hal-Hatır Sorma, Tanışma Diyalogları ve اَلسَّلَامُ قَبْلَ الْكَلَامِ İlkesi) çalışma kâğıdı görselleri.
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


def muenneslik_tasi_kartlari():
    kartlar = [
        ('1. Kart', 'صَبَاح - مَسَاء', MAVI, MAVI_A),
        ('2. Kart', 'طَالِبٌ - طَالِبَةٌ', YES, YES_A),
        ('3. Kart', 'قُمْ - اِجْلِسْ', TUR, TUR_A),
        ('4. Kart', 'نَعَمْ - لَا', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cift, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 118, y + 31, cift, LAC)
    return svg(360, 110, ic, 'Yuvarlak tâ ile eril-dişil dönüşümü kartları.', 18)


def hel_soru_cevap_kartlari():
    kartlar = [
        ('K · Eril Uyumu', 'هَلْ أَنْتَ طَالِبٌ؟ · نَعَمْ، أَنَا طَالِبٌ', MAVI, MAVI_A),
        ('L · Dişil Uyumu', 'هَلْ أَنْتِ طَالِبَةٌ؟ · نَعَمْ، أَنَا طَالِبَةٌ', YES, YES_A),
        ('M · Hatalı Eşleşme', 'هَلْ أَنْتِ مُعَلِّمَةٌ؟ · لَا، أَنَا مُعَلِّمٌ', KIR, '#fdeaea'),
        ('N · Eril Uyumu', 'هَلْ أَنْتَ مُعَلِّمٌ؟ · لَا، أَنَا طَالِبٌ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kartlar):
        y = 4 + i * 28
        ic += f'<rect x="6" y="{y}" width="348" height="25" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
        ic += tr_yazi(14, y + 17, bas, renk, 'start', kalin=True)
        ic += ar_yazi(238, y + 19, metin, LAC)
    return svg(360, 118, ic, 'Hel ente ve hel enti soru-cevap uyum kartları.', 18)


def iletisim_islev_kartlari():
    kartlar = [
        ('1. İfade', 'صَبَاحُ الْخَيْرِ', MAVI, MAVI_A),
        ('2. İfade', 'تَشَرَّفْتُ', YES, YES_A),
        ('3. İfade', 'فِي أَمَانِ اللَّهِ', TUR, TUR_A),
        ('4. İfade', 'فُرْصَةٌ سَعِيدَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ifade, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 118, y + 31, ifade, LAC)
    return svg(360, 110, ic, 'Selamlaşma, memnuniyet ve vedalaşma ifade kartları.', 18)


def ya_seslenme_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Yalın İsim (Tenvinli)', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'حَسَنٌ · عَلِيٌّ', LAC)
    ic += tr_yazi(91, 80, 'Sonda iki ötre var', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Seslenme Edatıyla (يَا)', YESIL_K, kalin=True)
    ic += ar_yazi(269, 56, 'يَا حَسَنُ · يَا عَلِيُّ', LAC)
    ic += tr_yazi(269, 80, 'Sonda tek ötre kalır', LAC)
    return svg(360, 100, ic, 'Yâ seslenme edatından sonra özel isimlerde tenvinin düşmesi.', 18)


def omer_hasan_diyalog_kartlari():
    kartlar = [
        ('Cümle K', 'أَنَا عُمَرُ، مَا اسْمُكَ؟', TUR, TUR_A),
        ('Cümle L', 'اَلسَّلَامُ عَلَيْكُمْ، صَبَاحُ الْخَيْرِ!', MAVI, MAVI_A),
        ('Cümle M', 'فُرْصَةٌ سَعِيدَةٌ! إِلَى اللِّقَاءِ.', MOR, MOR_A),
        ('Cümle N', 'هَلْ أَنْتَ طَالِبٌ جَدِيدٌ؟', YES, YES_A),
    ]
    ic = ''
    for i, (bas, cumle, renk, arka) in enumerate(kartlar):
        y = 4 + i * 28
        ic += f'<rect x="6" y="{y}" width="348" height="25" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
        ic += tr_yazi(14, y + 17, bas, renk, 'start', kalin=True)
        ic += ar_yazi(228, y + 19, cumle, LAC)
    return svg(360, 118, ic, 'Ömer ve Hasan arasındaki tanışma diyaloğunun dört cümlesi.', 18)


def cift_yonerge_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Erkek Öğrenci Kerem’e', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'قُمْ وَاقْرَأْ!', LAC)
    ic += tr_yazi(91, 80, 'Ey Kerem, kalk ve oku!', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Kız Öğrenci Meryem’e', MOR, kalin=True)
    ic += ar_yazi(269, 56, '؟', MOR)
    ic += tr_yazi(269, 80, 'Ey Meryem, kalk ve oku!', LAC)
    return svg(360, 100, ic, 'Kerem ve Meryem için ayağa kalk ve oku yönergesi karşılaştırması.', 18)


def muhatap_zamir_kurali():
    ic = f'<rect x="6" y="6" width="348" height="90" rx="10" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 24, 'Altın Kural · Muhatap Zamiri Seçimi', TUR, kalin=True)
    ic += ar_yazi(180, 56, 'مَرْحَبًا بِكَ · كَيْفَ حَالُكَ · مَا اسْمُكَ', LAC)
    ic += tr_yazi(180, 82, 'Muhatap Ömer (Erkek) olduğu için üstünlü (-ke) gelir.', LAC)
    return svg(360, 102, ic, 'Erkek muhatap Ömer’e hitap edilirken kullanılan -ke zamiri panosu.', 18)


def mesmuke_mesmuki_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Erkek Arkadaşa Sorarken', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'مَا اسْمُكَ؟', LAC)
    ic += tr_yazi(91, 80, 'Sonu üstünlü (-ke)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Kız Arkadaşa Sorarken', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'مَا اسْمُكِ؟', LAC)
    ic += tr_yazi(269, 80, 'Sonu esreli (-ki)', LAC)
    return svg(360, 100, ic, 'Erkek ve kız muhataba göre isim sorma kalıbı.', 18)


def veciz_soz_yapbozu():
    kutular = [
        ('1. Parça · Selam', 'اَلسَّلَامُ', YES, YES_A),
        ('2. Parça · Önce', '؟', TUR, TUR_A),
        ('3. Parça · Söz', 'الْكَلَامِ', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, kel, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 56, 24, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="32" x2="{x + 102}" y2="32" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 56, 68, kel, LAC)
    return svg(360, 96, ic, 'Es-selâmü kablel-kelâm veciz sözü yapboz kutuları.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = muenneslik_tasi_kartlari()
    s[4]['gorsel'] = hel_soru_cevap_kartlari()
    s[5]['gorsel'] = iletisim_islev_kartlari()
    s[6]['gorsel'] = ya_seslenme_panosu()
    s[7]['gorsel'] = omer_hasan_diyalog_kartlari()
    s[8]['gorsel'] = cift_yonerge_panosu()
    s[9]['gorsel'] = muhatap_zamir_kurali()
    s[11]['gorsel'] = mesmuke_mesmuki_panosu()
    s[12]['gorsel'] = veciz_soz_yapbozu()
