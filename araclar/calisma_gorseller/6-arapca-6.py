"""6. sınıf Arapça 6. hafta (Geniş Aile Bireyleri, Meslekler ve Şemsî-Kamerî Harfler) çalışma kâğıdı görselleri.
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


def tarik_ailesi_panosu():
    kartlar = [
        ('Baba ve Anne', 'أَبِي ضَابِطٌ · أُمِّي مُعَلِّمَةٌ', MAVI, MAVI_A),
        ('Akraba Sayısı', 'لِي عَمٌّ وَخَالَتَانِ', YES, YES_A),
        ('Amca ve Dayı', 'عَمِّي طَبَّاخٌ · خَالِي بَيْطَرِيٌّ', TUR, TUR_A),
        ('Dede ve Nine', 'جَدِّي وَجَدَّتِي مُتَقَاعِدَانِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 40, ar_metin, LAC).replace('font-size="22"', 'font-size="17"')
    return svg(360, 110, ic, 'Tarık’ın ailesini ve akrabalarını tanıtan dört metin kartı.', 18)


def sahiplik_sayisi_kartlari():
    kartlar = [
        ('1. Kart', 'لِي عَمٌّ وَاحِدٌ', MAVI, MAVI_A),
        ('2. Kart', 'لِي ثَلَاثُ خَالَاتٍ', YES, YES_A),
        ('3. Kart', 'لَهُ أَخٌ وَاحِدٌ', KIR, '#fdeaea'),
        ('4. Kart', 'لِلْجَدِّ أَرْبَعَةُ أَحْفَادٍ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Sahiplik zamirleri ve akraba sayısı kartları.', 18)


def soru_ipucu_tablo_kartlari():
    kartlar = [
        ('1', 'فَلَّاحٌ نَشِيطٌ', MAVI, MAVI_A),
        ('2', 'مُمَرِّضَةٌ', YES, YES_A),
        ('3', 'فِي الْمُسْتَشْفَى', TUR, TUR_A),
        ('4', 'فِي الْعَمَلِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Soru ve anahtar kelime kartları.', 18)


def dayi_teyze_hemsire_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, 'Eril (Dayım):', MAVI, 'start', kalin=True)
    ic += ar_yazi(225, 35, 'خَالِي مُمَرِّضٌ فِي الْمُسْتَشْفَى', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, 'Dişil (Teyzem):', MOR, 'start', kalin=True)
    ic += ar_yazi(225, 87, 'خَالَتِي ...', LAC)
    return svg(360, 110, ic, 'Dayı için kurulan cümleyi teyze öznesine dönüştürme kartı.', 18)


def akraba_sayilari_sirasi():
    kartlar = [
        ('A', 'لِي عَمٌّ وَاحِدٌ', MAVI, MAVI_A),
        ('B', 'لِي عَمَّانِ', YES, YES_A),
        ('C', 'لِي ثَلَاثُ خَالَاتٍ', TUR, TUR_A),
        ('D', 'لِلْجَدِّ أَرْبَعَةُ أَحْفَادٍ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 18, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 92, y + 41, ar_metin, LAC)
    return svg(360, 110, ic, 'Birden dörde kadar akraba sayısı kartları.', 18)


def alti_kelime_semsi_kameri():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, 'Kelimeler 1:', TUR, 'start', kalin=True)
    ic += ar_yazi(220, 35, 'اَلطَّبَّاخُ - اَلْمُحَامِي - اَلشُّرْطِيُّ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, 'Kelimeler 2:', MAVI, 'start', kalin=True)
    ic += ar_yazi(220, 87, 'اَلْعَمَّةُ - اَلضَّابِطُ - اَلْجَدَّةُ', LAC)
    return svg(360, 110, ic, 'Şemsî ve kamerî olarak gruplanacak altı kelime panosu.', 18)


def sofor_mahkeme_diyalogu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'هَلْ يَعْمَلُ السَّائِقُ فِي الْمَحْكَمَةِ؟', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 85, 'Cevap İpucu: Hayır (Olumsuz)', KIR, 'start', kalin=True)
    ic += ar_yazi(245, 87, '؟', KIR)
    return svg(360, 110, ic, 'Şoförün mahkemede çalışıp çalışmadığını soran diyalog kartı.', 18)


def muzari_fiil_baslangic_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Özne: Erkek (O)', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'يَعْمَلُ - يُحِبُّ', LAC)
    ic += tr_yazi(91, 80, 'Muzâri fiil (Eril)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Özne: Kadın (O)', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'تَعْمَلُ - تُحِبُّ', LAC)
    ic += tr_yazi(269, 80, 'Muzâri fiil (Dişil)', LAC)
    return svg(360, 100, ic, 'Eril ve dişil öznelerde muzâri fiil başlangıç harfleri panosu.', 18)


def soyagaci_tanim_kartlari():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, '1. Akraba Tanımı', YESIL_K, kalin=True)
    ic += ar_yazi(91, 56, 'أَبُو الْوَالِدِ', LAC)
    ic += tr_yazi(91, 80, 'Babanın babası', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, '2. Akraba Tanımı', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'أُخْتُ الْوَالِدَةِ', LAC)
    ic += tr_yazi(269, 80, 'Annenin kız kardeşi', LAC)
    return svg(360, 100, ic, 'Babanın babası ve annenin kız kardeşi tanım kartları.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tarik_ailesi_panosu()
    s[4]['gorsel'] = sahiplik_sayisi_kartlari()
    s[5]['gorsel'] = soru_ipucu_tablo_kartlari()
    s[6]['gorsel'] = dayi_teyze_hemsire_karti()
    s[7]['gorsel'] = akraba_sayilari_sirasi()
    s[8]['gorsel'] = alti_kelime_semsi_kameri()
    s[9]['gorsel'] = sofor_mahkeme_diyalogu()
    s[11]['gorsel'] = muzari_fiil_baslangic_panosu()
    s[12]['gorsel'] = soyagaci_tanim_kartlari()
