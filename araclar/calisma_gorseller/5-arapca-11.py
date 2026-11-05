"""5. sınıf Arapça 11. hafta (Okulumda: Okulun Bölümleri, Harf-i Cerler ve Eyne Soru Kalıbı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 11 pt, Arapça yazı Arial 20 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="10.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="19.2" font-weight="700"'


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


def okul_kapisi_tabelalari():
    ic = kutu(6, 6, 170, 78, MOR_A, MOR)
    ic += tr_yazi(91, 22, '1. Kapı · Kitap Rafları', MOR, kalin=True)
    ic += ar_yazi(91, 48, 'مَكْتَبَةٌ (Dişil - ة)', LAC)
    ic += tr_yazi(91, 70, 'Tanıtım: 1 → ?', MOR, kalin=True)

    ic += kutu(184, 6, 170, 78, TUR_A, TUR)
    ic += tr_yazi(269, 22, '2. Kapı · Okul Kantini', TUR, kalin=True)
    ic += ar_yazi(269, 48, 'مَقْصَفٌ (Eril)', LAC)
    ic += tr_yazi(269, 70, 'Tanıtım: 2 → ?', TUR, kalin=True)
    return svg(360, 90, ic, 'Kütüphane ve kantin kapı tabelaları.', 15)


def dort_mekan_fi_kartlari():
    kartlar = [
        ('1. Sınıf', 'اَلصَّفُّ', MAVI, MAVI_A),
        ('2. Kütüphane', 'اَلْمَكْتَبَةُ', YES, YES_A),
        ('3. Laboratuvar', 'اَلْمُخْتَبَرُ', TUR, TUR_A),
        ('4. Bahçe', 'اَلْحَدِيقَةُ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += f'<line x1="{x + 8}" y1="29" x2="{x + 74}" y2="29" stroke="{r}" stroke-width="0.9"/>'
        ic += ar_yazi(x + 41, 58, kel, LAC)
    return svg(360, 86, ic, 'Dört okul mekânı kartı.', 15)


def semsi_kameri_mekan_kartlari():
    kartlar = [
        ('1. Kart', 'اَلْمَدْرَسَةُ', MAVI, MAVI_A),
        ('2. Kart', 'اَلطَّالِبُ', KIR, KIR_A),
        ('3. Kart', 'اَلْمَكْتَبَةُ', YES, YES_A),
        ('4. Kart', 'اَلْمُخْتَبَرُ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, kel, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += f'<line x1="{x + 8}" y1="29" x2="{x + 74}" y2="29" stroke="{r}" stroke-width="0.9"/>'
        ic += ar_yazi(x + 41, 58, kel, LAC)
    return svg(360, 86, ic, 'Şemsî ve kamerî harfli dört kelime kartı.', 15)


def nobetci_ogretmen_diyalog():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += tr_yazi(16, 29, 'Öğretmenin Sorusu:', MAVI, 'start', kalin=True)
    ic += tr_yazi(240, 29, '? (Kız öğrenciyi soruyor)', MAVI, kalin=True)

    ic += kutu(6, 50, 348, 40, YES_A, YES)
    ic += tr_yazi(16, 74, 'Zeynep’in Cevabı:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(240, 75, 'هِيَ فِي الْمَكْتَبَةِ.', LAC)
    return svg(360, 96, ic, 'Nöbetçi öğretmen ve Zeynep arasındaki yer sorma diyaloğu.', 16)


def mekteb_mektebe_karsilastirma():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += tr_yazi(91, 22, '1. Kavram · Eril (Müzekker)', MAVI, kalin=True)
    ic += ar_yazi(91, 48, 'مَكْتَبٌ', LAC)
    ic += tr_yazi(91, 71, 'Yuvarlak te (ة) yok', LAC)

    ic += kutu(184, 6, 170, 78, MOR_A, MOR)
    ic += tr_yazi(269, 22, '2. Kavram · Dişil (Müennes)', MOR, kalin=True)
    ic += ar_yazi(269, 48, 'مَكْتَبَةٌ', LAC)
    ic += tr_yazi(269, 71, 'Sonunda yuvarlak te (ة) var', LAC)
    return svg(360, 90, ic, 'Mektebün ve mektebetün kelimelerinin karşılaştırma kartları.', 15)


def koridor_diyalog_akisi():
    adimlar = [
        ('1. Selam', 'اَلسَّلَامُ عَلَيْكُمْ', MAVI, MAVI_A),
        ('2. Soru', 'إِلَى أَيْنَ تَذْهَبُ؟', TUR, TUR_A),
        ('3. Yönelme', 'إِلَى الْمَقْصَفِ', YES, YES_A),
        ('4. Veda', 'إِلَى اللِّقَاءِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_ifade, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += tr_yazi(x + 41, 22, bas, r, kalin=True)
        ic += ar_yazi(x + 41, 56, ar_ifade, LAC)
    return svg(360, 86, ic, 'Okul koridorunda karşılaşma ve yönelme diyalog akışı.', 15)


def okul_rehberi_denetim_tablosu():
    satirlar = [
        ('I. Laboratuvar (Eril)', 'هٰذَا مُخْتَبَرٌ', MAVI, MAVI_A),
        ('II. Bahçe (Dişil)', 'هٰذِهِ حَدِيقَةٌ', YES, YES_A),
        ('III. Kantinde (Kesra)', 'فِي الْمَقْصَفِ', TUR, TUR_A),
        ('IV. Okulda (Hatalı!)', 'فِي الْمَدْرَسَةُ', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, ar_c, r, z) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r)
        ic += tr_yazi(x + 86, y + 14, bas, r, kalin=True)
        ic += ar_yazi(x + 86, y + 35, ar_c, LAC)
    return svg(360, 98, ic, 'Okul bölümleri ve harf-i cer kullanım denetim tablosu.', 16)


def harfi_cer_hareke_donusumu():
    ic = kutu(6, 6, 170, 78, YES_A, YES)
    ic += tr_yazi(91, 22, 'Bulunma Edatı (فِي)', YESIL_K, kalin=True)
    ic += ar_yazi(91, 48, 'اَلْمُخْتَبَرُ ← فِي الْمُخْتَبَرِ', LAC)
    ic += tr_yazi(91, 71, 'Son hareke: -u → -i (Kesra)', LAC)

    ic += kutu(184, 6, 170, 78, MAVI_A, MAVI)
    ic += tr_yazi(269, 22, 'Yönelme Edatı (إِلَى)', MAVI, kalin=True)
    ic += ar_yazi(269, 48, 'اَلْمَدْرَسَةُ ← إِلَى الْمَدْرَسَةِ', LAC)
    ic += tr_yazi(269, 71, 'Son hareke: -u → -i (Kesra)', LAC)
    return svg(360, 90, ic, 'Fî ve ilâ harf-i cerlerinin son harekeyi kesraya dönüştürmesi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = okul_kapisi_tabelalari()
    s[2]['gorsel'] = dort_mekan_fi_kartlari()
    s[5]['gorsel'] = semsi_kameri_mekan_kartlari()
    s[6]['gorsel'] = nobetci_ogretmen_diyalog()
    s[7]['gorsel'] = mekteb_mektebe_karsilastirma()
    s[8]['gorsel'] = koridor_diyalog_akisi()
    s[9]['gorsel'] = okul_rehberi_denetim_tablosu()
    s[11]['gorsel'] = harfi_cer_hareke_donusumu()
