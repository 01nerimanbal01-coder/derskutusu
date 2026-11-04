"""5. sınıf Arapça 9. hafta (Selamlaşma, Tanışma, Vedalaşma Diyalogları, Harf ve Harekelerle Kelime Okuma-Yazma ve 1. Ünite Değerlendirmesi) çalışma kâğıdı görselleri.
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


def sabah_aksam_selam_kartlari():
    ic = kutu(6, 6, 170, 78, TUR_A, TUR)
    ic += tr_yazi(91, 22, 'Sabah Selamlaşması', TUR, kalin=True)
    ic += ar_yazi(91, 47, 'صَبَاحُ الْخَيْرِ', LAC)
    ic += tr_yazi(91, 69, 'Cevap: 1 → ?', TUR, kalin=True)

    ic += kutu(184, 6, 170, 78, MAVI_A, MAVI)
    ic += tr_yazi(269, 22, 'Akşam Selamlaşması', MAVI, kalin=True)
    ic += ar_yazi(269, 47, 'مَسَاءُ الْخَيْرِ', LAC)
    ic += tr_yazi(269, 69, 'Cevap: 2 → ?', MAVI, kalin=True)
    return svg(360, 90, ic, 'Sabah ve akşam selamlaşma kartları.', 16)


def harf_birlestirme_kartlari():
    kartlar = [
        ('1. Kart', 'كَ + تَ + بَ', MAVI, MAVI_A),
        ('2. Kart', 'قَ + لَ + مٌ', YES, YES_A),
        ('3. Kart', 'دَ + رَ + سَ', TUR, TUR_A),
        ('4. Kart', 'عَ + لَ + مٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, harfler, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += f'<line x1="{x + 8}" y1="29" x2="{x + 74}" y2="29" stroke="{r}" stroke-width="0.9"/>'
        ic += ar_yazi(x + 41, 58, harfler, LAC)
    return svg(360, 86, ic, 'Dört harf birleştirme uygulama kartı.', 15)


def ayrik_harf_kelime_kartlari():
    kartlar = [
        ('1. Kart', 'كَتَبَ', MAVI, MAVI_A),
        ('2. Kart', 'دَرَسَ', YES, YES_A),
        ('3. Kart', 'وَرْدٌ', KIR, KIR_A),
        ('4. Kart', 'قَلَمٌ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, kel, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += f'<line x1="{x + 8}" y1="29" x2="{x + 74}" y2="29" stroke="{r}" stroke-width="0.9"/>'
        ic += ar_yazi(x + 41, 59, kel, LAC)
    return svg(360, 86, ic, 'Harflerin birleşme durumunu gösteren dört kelime kartı.', 15)


def dogrulama_soru_balonu():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += tr_yazi(16, 29, 'Öğretmen Sorusu:', MAVI, 'start', kalin=True)
    ic += tr_yazi(235, 29, '? (Fatma’ya soru)', MAVI, kalin=True)

    ic += kutu(6, 50, 348, 40, YES_A, YES)
    ic += tr_yazi(16, 74, 'Fatma’nın Cevabı:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(235, 75, 'نَعَمْ، أَنَا طَالِبَةٌ.', LAC)
    return svg(360, 96, ic, 'Öğretmen ve kız öğrenci Fatma arasındaki doğrulama diyaloğu.', 16)


def uc_hareke_panosu():
    kartlar = [
        ('1. Fetha (Üstün)', 'بَ · قَ', 'Üstte · e / a', MAVI, MAVI_A),
        ('2. Kesra (Esre)', 'بِ · قِ', 'Altta · i / ı', YES, YES_A),
        ('3. Damme (Ötre)', 'بُ · قُ', 'Üstte · ü / u', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_orn, ses, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 78, z, r)
        ic += tr_yazi(x + 56, 21, bas, r, kalin=True)
        ic += ar_yazi(x + 56, 49, ar_orn, LAC)
        ic += tr_yazi(x + 56, 72, ses, LAC)
    return svg(360, 90, ic, 'Fetha, kesra ve damme harekelerinin yazılışı ve sesleri.', 15)


def tanisma_akis_semasi():
    adimlar = [
        ('1. Selam', 'اَلسَّلَامُ عَلَيْكُمْ', MAVI, MAVI_A),
        ('2. Tanışma', 'مَا اسْمُكَ؟', YES, YES_A),
        ('3. Hâl Hatır', 'كَيْفَ حَالُكَ؟', TUR, TUR_A),
        ('4. Veda', 'إِلَى اللِّقَاءِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_ifade, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += ar_yazi(x + 41, 56, ar_ifade, LAC)
    return svg(360, 86, ic, 'Selamlaşma, tanışma, hâl hatır ve vedalaşma akış kartları.', 15)


def eril_disil_komut_tablosu():
    satirlar = [
        ('I. Kalk', 'قُمْ (Eril)', 'قُومِي (Dişil)', MAVI, MAVI_A),
        ('II. Otur', 'اِجْلِسْ (Eril)', 'اِجْلِسِي (Dişil)', YES, YES_A),
        ('III. Oku', 'اِقْرَأْ (Eril)', 'اِقْرَئِي (Dişil)', TUR, TUR_A),
        ('IV. Lütfen', 'مِنْ فَضْلِكِ (Eril)', 'مِنْ فَضْلِكَ (Dişil)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, eril, disil, r, z) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r)
        ic += tr_yazi(x + 86, y + 15, bas, r, kalin=True)
        ic += tr_yazi(x + 86, y + 32, f'{eril} · {disil}', LAC)
    return svg(360, 98, ic, 'Eril ve dişil sınıf içi yönergeler karşılaştırma tablosu.', 16)


def nezaket_zamir_karti():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += tr_yazi(91, 22, 'Erkek Muhatap (-ke)', MAVI, kalin=True)
    ic += ar_yazi(91, 48, 'مِنْ فَضْلِكَ · أَهْلًا بِكَ', LAC)
    ic += tr_yazi(91, 71, 'Son hareke: Üstün (ـكَ)', LAC)

    ic += kutu(184, 6, 170, 78, MOR_A, MOR)
    ic += tr_yazi(269, 22, 'Kız Muhatap (-ki)', MOR, kalin=True)
    ic += ar_yazi(269, 48, 'مِنْ فَضْلِكِ · أَهْلًا بِكِ', LAC)
    ic += tr_yazi(269, 71, 'Son hareke: Esre (ـكِ)', LAC)
    return svg(360, 90, ic, 'Erkek ve kız muhataba göre nezaket ifadelerindeki zamir değişimi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sabah_aksam_selam_kartlari()
    s[2]['gorsel'] = harf_birlestirme_kartlari()
    s[5]['gorsel'] = ayrik_harf_kelime_kartlari()
    s[6]['gorsel'] = dogrulama_soru_balonu()
    s[7]['gorsel'] = uc_hareke_panosu()
    s[8]['gorsel'] = tanisma_akis_semasi()
    s[9]['gorsel'] = eril_disil_komut_tablosu()
    s[11]['gorsel'] = nezaket_zamir_karti()
