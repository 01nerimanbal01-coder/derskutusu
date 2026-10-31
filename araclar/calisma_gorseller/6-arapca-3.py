"""6. sınıf Arapça 3. hafta (Okuma Diyaloğu, Çalışma Yerleri ve Kaç Akraban Var?) çalışma kâğıdı görselleri.
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


def busra_akrabalar_panosu():
    kartlar = [
        ('Anne Tarafı', 'خَالِي مَحْمُود · خَالَتِي', MAVI, MAVI_A),
        ('Baba Tarafı 1', 'عَمَّتِي شَيْمَاءُ مُمَرِّضَةٌ', YES, YES_A),
        ('Baba Tarafı 2', 'عَمِّي مُحَمَّدٌ مُحَامٍ', TUR, TUR_A),
        ('Baba Tarafı 3', 'بِنْتُ عَمِّي طَالِبَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Büşra’nın okuma metninde tanıttığı akrabalar panosu.', 18)


def tenvin_donusum_kartlari():
    kartlar = [
        ('1. Kart', 'طَبِيبٌ - اَلطَّبِيبُ', YES, YES_A),
        ('2. Kart', 'حَقِيبَةٌ - اَلْحَقِيبَةُ', MAVI, MAVI_A),
        ('3. Kart', 'قَمِيصٌ - اَلْقَمِيصٌ', KIR, '#fdeaea'),
        ('4. Kart', 'صَفٌّ - اَلصَّفُّ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Kelime başına el takısı ekleme ve tenvin dönüşüm kartları.', 18)


def busra_tablo_kartlari():
    kartlar = [
        ('1 · Mahmut', 'خَالِي مُعَلِّمٌ مَاهِرٌ', MAVI, MAVI_A),
        ('2 · Zehra', 'خَالَتِي بَيْطَرِيَّةٌ', MOR, MOR_A),
        ('3 · Şeyma', 'عَمَّتِي مُمَرِّضَةٌ', YES, YES_A),
        ('4 · Fatma', 'جَدَّتِي مُتَقَاعِدَةٌ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Büşra’nın dört akrabasının isim ve meslek kartları.', 18)


def olumlu_olumsuz_mekan_panosu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, '1. Cümle:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'اَلْمُعَلِّمَةُ تَعْمَلُ فِي الْمَدْرَسَةِ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, '2. Cümle:', KIR, 'start', kalin=True)
    ic += ar_yazi(215, 87, 'اَلطَّبَّاخَةُ لَا تَعْمَلُ فِي غُرْفَةِ الْجُلُوسِ', LAC)
    return svg(360, 110, ic, 'Okulda çalışan öğretmen ve oturma odasında çalışmayan aşçı cümleleri.', 18)


def okuma_sorulari_akisi():
    kartlar = [
        ('Soru A', 'أَيْنَ يَعْمَلُ الْخَالُ؟', MAVI, MAVI_A),
        ('Soru B', 'مَا مِهْنَةُ الْخَالَةِ؟', MOR, MOR_A),
        ('Soru C', 'هَلِ الْعَمُّ مُحَامٍ؟', YES, YES_A),
        ('Soru D', 'كَمْ حَفِيدًا لِجَدَّتِكِ؟', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Okuma metniyle ilgili dört soru kartı.', 18)


def calisma_mekan_uyumu_kartlari():
    kartlar = [
        ('A', 'اَلْمُعَلِّمُ - غُرْفَةِ النَّوْمِ', KIR, '#fdeaea'),
        ('B', 'اَلطَّبَّاخَةُ - غُرْفَةِ الْجُلُوسِ', TUR, TUR_A),
        ('C', 'لَا تَعْمَلُ - الْمَدْرَسَةِ', MOR, MOR_A),
        ('D', 'اَلسَّائِقُ يَعْمَلُ فِي الْعَمَلِ', YES, YES_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Meslek ve çalışma yeri eşleşme kartları.', 18)


def torun_sayisi_diyalogu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Merve’nin Sorusu:', MAVI, 'start', kalin=True)
    ic += ar_yazi(235, 35, '؟', MAVI)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 85, 'Büşra’nın Cevabı (Dört):', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(235, 87, 'أَرْبَعَةٌ', LAC)
    return svg(360, 110, ic, 'Torun sayısını soran diyalog kartı.', 18)


def veciz_soz_panosu():
    ic = f'<rect x="6" y="14" width="348" height="82" rx="10" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 36, '1. Ünite Veciz Sözü (Akrabaya İyilik)', TUR, kalin=True)
    ic += ar_yazi(180, 74, 'اَلْأَقْرَبُونَ أَوْلَى بِالْمَعْرُوفِ', LAC)
    return svg(360, 106, ic, 'Akrabaya iyiliği öğütleyen veciz söz panosu.', 18)


def semsi_kameri_grup_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Grup (Şemsi)', TUR, kalin=True)
    ic += ar_yazi(91, 54, 'اَلنَّحْلُ - اَلصَّفُّ', LAC)
    ic += tr_yazi(91, 80, '+ Boşluk 1', TUR, kalin=True)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Grup (Kameri)', MAVI, kalin=True)
    ic += ar_yazi(269, 54, 'اَلْأَبُ - اَلْوَرَقُ', LAC)
    ic += tr_yazi(269, 80, '+ Boşluk 2', MAVI, kalin=True)
    return svg(360, 100, ic, 'Şemsi ve kameri kelime grupları tamamlama panosu.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = busra_akrabalar_panosu()
    s[4]['gorsel'] = tenvin_donusum_kartlari()
    s[5]['gorsel'] = busra_tablo_kartlari()
    s[6]['gorsel'] = olumlu_olumsuz_mekan_panosu()
    s[7]['gorsel'] = okuma_sorulari_akisi()
    s[8]['gorsel'] = calisma_mekan_uyumu_kartlari()
    s[9]['gorsel'] = torun_sayisi_diyalogu()
    s[11]['gorsel'] = veciz_soz_panosu()
    s[12]['gorsel'] = semsi_kameri_grup_panosu()
