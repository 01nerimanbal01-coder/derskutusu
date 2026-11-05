"""5. sınıf Arapça 10. hafta (Sınıfımda: Sınıf Eşyaları, Yakın İşaret İsimleri, Soru Kalıpları ve Sınıf İçi Yönergeler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 11 pt, Arapça yazı Arial 20 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="10.6"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="19.5" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def isaret_ismi_uyum_kartlari():
    kartlar = [
        ('1. Kart (Masa)', 'هٰذَا مَكْتَبٌ', MAVI, MAVI_A),
        ('2. Kart (Silgi)', 'هٰذِهِ مِمْحَاةٌ', YES, YES_A),
        ('3. Kart (Çanta)', 'هٰذَا حَقِيبَةٌ', KIR, KIR_A),
        ('4. Kart (Masa)', 'هٰذِهِ طَاوِلَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cml, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += f'<line x1="{x + 8}" y1="29" x2="{x + 74}" y2="29" stroke="{r}" stroke-width="0.9"/>'
        ic += ar_yazi(x + 41, 58, cml, LAC)
    return svg(360, 86, ic, 'İşaret isimleri ve sınıf eşyaları uyum kartları.', 15)


def dort_egitim_araci_tablo():
    kartlar = [
        ('1. Sandalye', 'كُرْسِيٌّ', MAVI, MAVI_A),
        ('2. Tahta', 'سَبُّورَةٌ', MOR, MOR_A),
        ('3. Defter', 'دَفْتَرٌ', YES, YES_A),
        ('4. Okul', 'مَدْرَسَةٌ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, kel, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += f'<line x1="{x + 8}" y1="29" x2="{x + 74}" y2="29" stroke="{r}" stroke-width="0.9"/>'
        ic += ar_yazi(x + 41, 58, kel, LAC)
    return svg(360, 86, ic, 'Eril ve dişil dört eğitim aracı kartı.', 15)


def hel_dogrulama_karti():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += tr_yazi(16, 29, 'Meryem’in Sorusu:', MAVI, 'start', kalin=True)
    ic += ar_yazi(245, 30, 'هَلْ هٰذَا قَلَمٌ؟', LAC)

    ic += kutu(6, 50, 348, 40, TUR_A, TUR)
    ic += tr_yazi(16, 74, 'Selim (Eşya: Defter - دَفْتَرٌ):', TUR, 'start', kalin=True)
    ic += tr_yazi(275, 74, 'Olumsuz Cevap → ?', KIR, kalin=True)
    return svg(360, 96, ic, 'Hel hâzâ kalemün sorusu ve defter görselli olumsuz cevap kartı.', 16)


def sinif_yonerge_panosu():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += tr_yazi(91, 22, 'Kerem’e Yönerge (Eril)', MAVI, kalin=True)
    ic += ar_yazi(91, 48, '[ I ] اَلْكِتَابَ!', LAC)
    ic += tr_yazi(91, 71, 'Anlamı: «Kitabı aç!»', MAVI, kalin=True)

    ic += kutu(184, 6, 170, 78, MOR_A, MOR)
    ic += tr_yazi(269, 22, 'Zehra’ya Yönerge (Dişil)', MOR, kalin=True)
    ic += ar_yazi(269, 48, '[ II ] اَلدَّفْتَرَ!', LAC)
    ic += tr_yazi(269, 71, 'Anlamı: «Defteri al!»', MOR, kalin=True)
    return svg(360, 90, ic, 'Erkek ve kız öğrenciye yönelik sınıf içi emir yönergeleri.', 15)


def sesletim_cezim_sedde_karti():
    ic = kutu(6, 6, 170, 78, YES_A, YES)
    ic += tr_yazi(91, 22, '1. Kelime · Cezim ve Tenvin', YESIL_K, kalin=True)
    ic += ar_yazi(91, 49, 'مَكْتَبٌ', LAC)
    ic += tr_yazi(91, 71, 'Okunuşu: Mektebün (Masa)', LAC)

    ic += kutu(184, 6, 170, 78, TUR_A, TUR)
    ic += tr_yazi(269, 22, '2. Kelime · Şedde ve Tenvin', TUR, kalin=True)
    ic += ar_yazi(269, 49, 'سَبُّورَةٌ', LAC)
    ic += tr_yazi(269, 71, 'Okunuşu: Sebbûratün (Tahta)', LAC)
    return svg(360, 90, ic, 'Cezim, şedde ve tenvin içeren iki sınıf eşyası kartı.', 15)


def sinif_diyalog_akisi():
    adimlar = [
        ('1. Selam', 'اَلسَّلَامُ عَلَيْكُمْ', MAVI, MAVI_A),
        ('2. Soru', 'مَا هٰذِهِ؟', MOR, MOR_A),
        ('3. Doğrulama', 'هَلْ هٰذَا كِتَابٌ؟', YES, YES_A),
        ('4. İstek', 'أَعْطِنِي الْكِتَابَ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_ifade, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += ar_yazi(x + 41, 56, ar_ifade, LAC)
    return svg(360, 86, ic, 'Sınıfta selamlaşma, eşya sorma, doğrulama ve isteme akışı.', 15)


def sinif_tanitim_panosu():
    satirlar = [
        ('I. Sınıfım', 'هٰذَا صَفِّي', MAVI, MAVI_A),
        ('II. Erkek Arkadaş', 'هٰذَا صَدِيقِي أَحْمَدُ', YES, YES_A),
        ('III. Kız Arkadaş', 'هٰذِهِ صَدِيقَتِي زَيْنَبُ', MOR, MOR_A),
        ('IV. Mekân İfadesi', 'فِي الْمَدْرَسَةِ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_cml, r, z) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r)
        ic += tr_yazi(x + 86, y + 14, bas, r, kalin=True)
        ic += ar_yazi(x + 86, y + 35, ar_cml, LAC)
    return svg(360, 98, ic, '5-A sınıfı tanıtım ve arkadaşlık ifadeleri panosu.', 16)


def ma_ve_hel_soru_farki():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += tr_yazi(91, 22, '1. Nesne Adı Sorma (مَا)', MAVI, kalin=True)
    ic += ar_yazi(91, 47, 'مَا هٰذَا؟ → هٰذَا دَفْتَرٌ.', LAC)
    ic += tr_yazi(91, 71, 'Anlamı: Bu nedir? (Doğrudan ad)', LAC)

    ic += kutu(184, 6, 170, 78, YES_A, YES)
    ic += tr_yazi(269, 22, '2. Onay Sorma (هَلْ)', YESIL_K, kalin=True)
    ic += ar_yazi(269, 47, 'هَلْ هٰذَا دَفْتَرٌ؟ → نَعَمْ / لَا', LAC)
    ic += tr_yazi(269, 71, 'Anlamı: Bu defter midir?', LAC)
    return svg(360, 90, ic, 'Mâ hâzâ ve Hel hâzâ soru kalıplarının karşılaştırma kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = isaret_ismi_uyum_kartlari()
    s[2]['gorsel'] = dort_egitim_araci_tablo()
    s[5]['gorsel'] = hel_dogrulama_karti()
    s[6]['gorsel'] = sinif_yonerge_panosu()
    s[7]['gorsel'] = sesletim_cezim_sedde_karti()
    s[8]['gorsel'] = sinif_diyalog_akisi()
    s[9]['gorsel'] = sinif_tanitim_panosu()
    s[11]['gorsel'] = ma_ve_hel_soru_farki()
