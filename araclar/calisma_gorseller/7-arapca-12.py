"""7. sınıf Arapça 12. hafta (Kırtasiyede ve Giyim Mağazasında Alışveriş, Fiyat Sorma ve Renkler) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT_TR = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
FONT_AR = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="16"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT_TR} font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT_AR} fill="{renk}">{metin}</text>'


def kirtasiye_fiyat_karti():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, 'Kırtasiye (الْمَكْتَبَةُ)', MAVI, kalin=True)
    ic += yazi_ar(92, 54, 'أُرِيدُ دَفْتَرًا وَمِسْطَرَةً', LAC)
    ic += yazi_ar(92, 82, 'بِكَمْ هٰذَا يَا بَائِعُ؟', MAVI)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 24, 'Satıcı Fişi (الْفَاتُورَةُ)', YES, kalin=True)
    ic += yazi_ar(269, 56, 'بِخَمْسَ عَشْرَةَ لِيرَةً', LAC)
    ic += yazi(269, 88, 'Toplam Tutar: 15 TL', YES, kalin=True)
    return svg(ic, 'Kırtasiyede defter ve cetvel fiyat sorma diyaloğu.')


def dort_urun_etiketi():
    kartlar = [
        (6, 6, '1. قَلَمٌ أَحْمَرُ', 'Kırtasiye Reyonu', KIR, KIR_A),
        (184, 6, '2. فُسْتَانٌ أَخْضَرُ', 'Giyim Reyonu', YES, YES_A),
        (6, 60, '3. حَقِيبَةٌ صَفْرَاءُ', 'Okul Çantası', TUR, TUR_A),
        (184, 60, '4. حِذَاءٌ أَسْوَدُ', 'Ayakkabı Reyonu', MAVI, MAVI_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi_ar(x + 85, y + 22, b1, r)
        ic += yazi(x + 85, y + 41, b2, LAC, kalin=True)
    return svg(ic, 'Kırtasiye ve giyim mağazası ürün etiketleri.')


def giyim_tercih_vitrini():
    ic = kutu(6, 6, 172, 103, TUR_A, TUR)
    ic += yazi(92, 24, 'Satıcının Sorusu', TUR, kalin=True)
    ic += yazi_ar(92, 54, 'أَتُفَضِّلُ الْقَمِيصَ الْأَزْرَقَ', LAC)
    ic += yazi_ar(92, 82, 'أَمِ الْقَمِيصَ الْأَبْيَضَ؟', TUR)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 24, 'Müşterinin Tercihi', MAVI, kalin=True)
    ic += yazi_ar(269, 56, 'أُفَضِّلُ الْقَمِيصَ الْأَزْرَقَ', LAC)
    ic += yazi(269, 86, 'Secim: قَمِيصٌ أَزْرَقُ', MAVI, kalin=True)
    return svg(ic, 'Giyim mağazasında mavi ve beyaz gömlek tercih diyaloğu.')


def renk_uyum_kartlari():
    kartlar = [
        (6, 6, '1. Kart (Eril?)', 'قَلَمٌ حَمْرَاءُ', KIR, KIR_A),
        (184, 6, '2. Kart (Dişil)', 'حَقِيبَةٌ زَرْقَاءُ', MAVI, MAVI_A),
        (6, 60, '3. Kart (Eril?)', 'فُسْتَانٌ بَيْضَاءُ', MOR, MOR_A),
        (184, 60, '4. Kart (Dişil?)', 'مِمْحَاةٌ أَخْضَرُ', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 18, b1, r, kalin=True)
        ic += yazi_ar(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Renk sıfatlarında eril ve dişil uyum kartları.')


def kirtasiye_fisi_cevirisi():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'Kırtasiye Sipariş Fişi (فِي الْمَكْتَبَةِ)', CAM, kalin=True)
    ic += yazi_ar(180, 58, 'أُرِيدُ ثَلَاثَةَ دَفَاتِرَ وَقَلَمَيْنِ بِعَشْرِ لِيرَاتٍ', LAC)
    ic += yazi(180, 92, 'ثَلَاثَةَ دَفَاتِرَ (3) + قَلَمَيْنِ (2) = ١٠ لِيرَاتٍ (10 TL)', MAVI, kalin=True)
    return svg(ic, 'Üç defter ve iki kalem içeren kırtasiye sipariş fişi.')


def magaza_diyalog_adimlari():
    adimlar = [
        (6, '1. Adım', 'هَلْ عِنْدَكَ قَمِيصٌ؟', MAVI, MAVI_A),
        (94, '2. Adım', 'نَعَمْ، تَفَضَّلْ', YES, YES_A),
        (182, '3. Adım', 'بِكَمْ هٰذَا؟', TUR, TUR_A),
        (270, '4. Adım', 'بِـ ١٧ لِيرَةً', MOR, MOR_A),
    ]
    ic = ''
    for x, ad, ar, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 32, ad, r, kalin=True)
        ic += yazi_ar(x + 42, 70, ar, LAC)
    return svg(ic, 'Giyim mağazasında dört adımlı alışveriş diyaloğu.')


def unite_degerlendirme_panosu():
    kartlar = [
        (6, 6, '1. الْمَخْبَزُ', 'خُبْزٌ طَازَجٌ وَكَعْكٌ', TUR, TUR_A),
        (184, 6, '2. الْمَكْتَبَةُ', 'دَفْتَرٌ وَمِسْطَرَةٌ', MAVI, MAVI_A),
        (6, 60, '3. مَحَلُّ الْمَلَابِسِ', 'جَزَرٌ وَبَصَلٌ (؟)', KIR, KIR_A),
        (184, 60, '4. الْبَقَّالُ', 'جُبْنٌ وَزَيْتُونٌ', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi_ar(x + 85, y + 20, b1, r)
        ic += yazi_ar(x + 85, y + 41, b2, LAC)
    return svg(ic, 'İkinci ünite alışveriş mekânları ve ürünler eşleştirme panosu.')


def alisveris_listesi_karti():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, '1. Ürün: Mavi Çanta', MAVI, kalin=True)
    ic += yazi_ar(92, 58, 'حَقِيبَةٌ زَرْقَاءُ', LAC)
    ic += yazi(92, 88, '(Müennes / Dişil Renk)', MAVI)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 26, '2. Ürün: Kırmızı Kalem', KIR, kalin=True)
    ic += yazi_ar(269, 58, 'قَلَمٌ أَحْمَرُ', LAC)
    ic += yazi(269, 88, 'Kalıp: أُرِيدُ ... وَ ...', KIR, kalin=True)
    return svg(ic, 'Mavi çanta ve kırmızı kalemden oluşan kırtasiye alışveriş listesi.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kirtasiye_fiyat_karti()
    s[2]['gorsel'] = dort_urun_etiketi()
    s[5]['gorsel'] = giyim_tercih_vitrini()
    s[6]['gorsel'] = renk_uyum_kartlari()
    s[7]['gorsel'] = kirtasiye_fisi_cevirisi()
    s[8]['gorsel'] = magaza_diyalog_adimlari()
    s[9]['gorsel'] = unite_degerlendirme_panosu()
    s[11]['gorsel'] = alisveris_listesi_karti()
