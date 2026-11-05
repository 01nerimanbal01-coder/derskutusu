"""7. sınıf Arapça 11. hafta (Fırında, Bakkalda ve Halk Pazarında Alışveriş) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px, max-height 21-22mm."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#e0f4f8'
FONT_TR = 'font-family="Noto Sans, sans-serif" font-size="12"'
FONT_AR = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18"'


def svg(w, h, ic, etiket, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT_TR} font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT_AR} fill="{renk}">{metin}</text>'


def firin_siparis_karti():
    ic = kutu(6, 6, 408, 42, TUR_A, TUR)
    ic += f'<ellipse cx="32" cy="27" rx="16" ry="9" fill="#f59e0b" stroke="{TUR}" stroke-width="1.1"/>'
    ic += yazi_tr(56, 31, 'Fırın (الْمَخْبَزُ):', TUR, 'start', True)
    ic += yazi_ar(285, 33, 'أُرِيدُ خُبْزًا طَازَجًا وَكِيسًا مِنَ الدَّقِيقِ', LAC)
    ic += kutu(6, 54, 408, 40, YES_A, YES)
    ic += yazi_tr(18, 78, 'Fırıncı Yanıtı:', YES, 'start', True)
    ic += yazi_ar(275, 80, 'تَفَضَّلْ، اَلْخُبْزُ سَاخِنٌ وَطَازَجٌ', YES)
    return svg(420, 100, ic, 'Mahalle fırınında taze ekmek ve bir paket un siparişi kartı.', 21)


def reyon_siniflama_panosu():
    kasalar = [
        (6, 6, '1. Kasa', 'جَزَرٌ وَبَصَلٌ', YES, YES_A),
        (214, 6, '2. Kasa', 'فَرَاوِلَةٌ وَمَوْزٌ', KIR, KIR_A),
        (6, 54, '3. Kasa', 'زُبْدَةٌ وَعَسَلٌ', TUR, TUR_A),
        (214, 54, '4. Kasa', 'خُبْزٌ وَكَعْكٌ', MAVI, MAVI_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kasalar:
        ic += kutu(x, y, 200, 42, z, r)
        ic += yazi_tr(x + 12, y + 26, bas, r, 'start', True)
        ic += yazi_ar(x + 132, y + 29, ar, LAC)
    return svg(420, 102, ic, 'Dört farklı gıda kasasında Arapça ürün isimleri.', 22)


def bakkal_fiyat_etiketleri():
    ic = kutu(6, 6, 206, 86, MAVI_A, MAVI)
    ic += yazi_tr(109, 24, 'Bakkal Fişi (عِنْدَ الْبَقَّالِ)', MAVI, kalin=True)
    ic += yazi_ar(109, 52, 'نِصْفُ كِيلُو مِنَ الزَّيْتُونِ', LAC)
    ic += yazi_ar(109, 80, 'وَعُلْبَةٌ مِنَ الْحَلِيبِ', LAC)

    ic += kutu(220, 6, 194, 86, YES_A, YES)
    ic += yazi_tr(317, 24, 'Terazi ve Tutar', YES, kalin=True)
    ic += f'<rect x="252" y="34" width="130" height="26" rx="5" fill="#bbf7d0" stroke="{YES}" stroke-width="1.1"/>'
    ic += yazi_tr(317, 52, 'TOPLAM: 14 LİRA', LAC, kalin=True)
    ic += yazi_ar(317, 82, '١٤ لِيرَةً', YES)
    return svg(420, 98, ic, 'Bakkal alışveriş fişi ve 14 liralık toplam tutar göstergesi.', 21)


def tercih_diyalog_panosu():
    ic = kutu(6, 6, 204, 86, TUR_A, TUR)
    ic += yazi_tr(108, 24, 'Satıcının Sorusu', TUR, kalin=True)
    ic += yazi_ar(108, 54, 'أَتُفَضِّلُ الْبُرْتُقَالَ أَمِ الْمَوْزَ؟', LAC)
    ic += yazi_tr(108, 80, 'Tercih sorusu (أَمْ)', TUR)

    ic += kutu(218, 6, 196, 86, YES_A, YES)
    ic += yazi_tr(316, 24, 'Müşteri Sepeti', YES, kalin=True)
    ic += f'<circle cx="246" cy="52" r="9" fill="#fb923c" stroke="{TUR}" stroke-width="1.1"/>'
    ic += f'<circle cx="268" cy="52" r="9" fill="#ef4444" stroke="{KIR}" stroke-width="1.1"/>'
    ic += yazi_ar(342, 57, 'بُرْتُقَالٌ وَتُفَّاحٌ', LAC)
    ic += yazi_tr(316, 80, 'Portakal ve taze elma', LAC)
    return svg(420, 98, ic, 'Manav tezgâhında tercih sorusu ve portakal-elma sepeti.', 21)


def tarti_ahlaki_levhasi():
    ic = kutu(6, 6, 134, 86, CAM_A, CAM)
    ic += f'<line x1="73" y1="22" x2="73" y2="74" stroke="{CAM}" stroke-width="2"/>'
    ic += f'<line x1="35" y1="36" x2="111" y2="36" stroke="{CAM}" stroke-width="2"/>'
    ic += f'<polygon points="25,58 45,58 35,36" fill="#bae6fd" stroke="{CAM}" stroke-width="1.1"/>'
    ic += f'<polygon points="101,58 121,58 111,36" fill="#bae6fd" stroke="{CAM}" stroke-width="1.1"/>'
    ic += f'<rect x="53" y="74" width="40" height="8" rx="3" fill="{CAM}"/>'

    ic += kutu(148, 6, 266, 86, TUR_A, TUR)
    ic += yazi_tr(281, 24, 'Ticaret Ahlakı Levhası', TUR, kalin=True)
    ic += yazi_ar(281, 52, 'اِنْتَبِهْ لِلْكَيْلِ وَالْمِيزَانِ', LAC)
    ic += yazi_ar(281, 80, 'اللّٰهُ لَا يُحِبُّ الْمُطَفِّفِينَ', KIR)
    return svg(420, 98, ic, 'Dengeli terazi çizimi ve ölçü-tartı ahlakı levhası.', 21)


def pazar_alisveris_adimlari():
    adimlar = [
        (6, '1. Selam', 'هَلْ عِنْدَكَ؟', MAVI, MAVI_A),
        (110, '2. Ürünler', 'إِجَّاصٌ وَعِنَبٌ', YES, YES_A),
        (214, '3. Tartı', 'كِيلُو ثُمَّ نِصْفُ', TUR, TUR_A),
        (318, '4. Tutar', '١٧ لِيرَةً', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, ar, r, z in adimlar:
        ic += kutu(x, 6, 96, 84, z, r)
        ic += yazi_tr(x + 48, 26, bas, r, kalin=True)
        ic += yazi_ar(x + 48, 64, ar, LAC)
    return svg(420, 96, ic, 'Halk pazarında dört adımlı alışveriş akış şeması.', 21)


def mutfak_liste_kontrol():
    maddeler = [
        (6, 6, '1.', 'كِيلُو مِنَ الْفُلْفُلِ', YES, YES_A),
        (214, 6, '2.', 'نِصْفُ كِيلُو مِنَ الْجُبْنِ', MAVI, MAVI_A),
        (6, 54, '3.', 'خَمْسَ عَشْرَةَ بَيْضَةً', TUR, TUR_A),
        (214, 54, '4.', 'كِيلُو مِنَ الْبَطِّيخِ', KIR, KIR_A),
    ]
    ic = ''
    for x, y, no, ar, r, z in maddeler:
        ic += kutu(x, y, 200, 42, z, r)
        ic += yazi_tr(x + 12, y + 26, no, r, 'start', True)
        ic += yazi_ar(x + 112, y + 29, ar, LAC)
    return svg(420, 102, ic, 'Dört maddelik Arapça mutfak alışveriş listesi.', 22)


def sirali_manav_sepeti():
    ic = kutu(6, 6, 150, 84, TUR_A, TUR)
    ic += yazi_tr(81, 25, '1. Önce (1 Kilo)', TUR, kalin=True)
    ic += yazi_ar(81, 56, 'كِيلُو مِنَ الْجَزَرِ', LAC)
    ic += yazi_tr(81, 79, 'Havuç', LAC)

    ic += kutu(164, 6, 92, 84, MOR_A, MOR)
    ic += yazi_tr(210, 28, 'Bağlaç', MOR, kalin=True)
    ic += yazi_ar(210, 58, 'ثُمَّ', MOR)
    ic += yazi_tr(210, 79, 'Sonra', LAC)

    ic += kutu(264, 6, 150, 84, YES_A, YES)
    ic += yazi_tr(339, 25, '2. Yarım Kilo', YES, kalin=True)
    ic += yazi_ar(339, 56, 'نِصْفُ كِيلُو تُفَّاحٍ', LAC)
    ic += yazi_tr(339, 79, 'Elma', LAC)
    return svg(420, 96, ic, 'Önce bir kilo havuç sonra yarım kilo elma isteme şeması.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = firin_siparis_karti()
    s[2]['gorsel'] = reyon_siniflama_panosu()
    s[5]['gorsel'] = bakkal_fiyat_etiketleri()
    s[6]['gorsel'] = tercih_diyalog_panosu()
    s[7]['gorsel'] = tarti_ahlaki_levhasi()
    s[8]['gorsel'] = pazar_alisveris_adimlari()
    s[9]['gorsel'] = mutfak_liste_kontrol()
    s[11]['gorsel'] = sirali_manav_sepeti()
