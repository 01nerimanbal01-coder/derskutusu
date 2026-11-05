"""7. sınıf Fen Bilimleri 11. hafta (Fiziksel-Kimyasal Sindirim, Enzimler, Villuslar ve Sindirim Sağlığı) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px, max-height 21-22mm."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def deney_tupleri_sindirim():
    tupler = [
        (6, 'I. Tüp (37 °C)', 'Ekmek +', 'Tükürük sıvısı', MAVI, MAVI_A),
        (144, 'II. Tüp (37 °C)', 'Haşlanmış et +', 'Safra sıvısı', KIR, KIR_A),
        (282, 'III. Tüp (37 °C)', 'Zeytinyağı +', 'Pankreas öz suyu', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in tupler:
        ic += kutu(x, 6, 132, 84, z, r)
        ic += f'<rect x="{x + 10}" y="22" width="14" height="54" rx="7" fill="#bae6fd" stroke="{r}" stroke-width="1.2"/>'
        ic += yazi(x + 76, 26, bas, r, kalin=True)
        ic += yazi(x + 76, 52, s1, LAC)
        ic += yazi(x + 76, 74, s2, r, kalin=True)
    return svg(420, 96, ic, 'Üç deney tüpünde besin ve sindirim salgıları düzeneği.', 21)


def besin_yolculugu_semasi():
    ogeler = [
        (6, 6, '1. Makarna', 'Karbonhidrat', MAVI, MAVI_A),
        (214, 6, '2. Izgara Balık', 'Protein', KIR, KIR_A),
        (6, 54, '3. Zeytinyağı', 'Yağ', TUR, TUR_A),
        (214, 54, '4. Maden Suyu', 'Su ve Mineral', CAM, CAM_A),
    ]
    ic = ''
    for x, y, ad, grup, r, z in ogeler:
        ic += kutu(x, y, 200, 42, z, r)
        ic += yazi(x + 100, y + 18, ad, r, kalin=True)
        ic += yazi(x + 100, y + 36, grup, LAC)
    return svg(420, 102, ic, 'Öğle yemeği tepsisinde dört besin grubu kartı.', 22)


def molekul_degisim_grafigi():
    ic = kutu(6, 6, 408, 86, MAVI_A, MAVI)
    ic += yazi(210, 22, 'Besin Miktarının Organlara Göre Değişimi', MAVI, kalin=True)
    ic += f'<line x1="56" y1="30" x2="56" y2="74" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<line x1="56" y1="74" x2="386" y2="74" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<polyline points="66,38 166,38 266,56 366,73" fill="none" stroke="{KIR}" stroke-width="2.2"/>'
    ic += f'<circle cx="166" cy="38" r="3.5" fill="{KIR}"/>'
    ic += f'<circle cx="266" cy="56" r="3.5" fill="{KIR}"/>'
    ic += f'<circle cx="366" cy="73" r="3.5" fill="{KIR}"/>'
    ic += yazi(115, 88, 'X (Ağız)', LAC)
    ic += yazi(225, 88, 'Y (Mide)', KIR, kalin=True)
    ic += yazi(340, 88, 'Z (İnce Bağ.)', YES, kalin=True)
    return svg(420, 98, ic, 'Ağızda sabit kalıp midede başlayan ve ince bağırsakta biten sindirim grafiği.', 21)


def villus_kesit_semasi():
    ic = kutu(6, 6, 176, 84, YES_A, YES)
    ic += f'<path d="M 22 76 Q 38 22 54 76 Q 70 22 86 76 Q 102 22 118 76 Q 134 22 150 76" fill="#bbf7d0" stroke="{YES}" stroke-width="1.5"/>'
    ic += f'<path d="M 38 42 L 38 74 M 70 42 L 70 74 M 102 42 L 102 74 M 134 42 L 134 74" stroke="{KIR}" stroke-width="1.1"/>'
    ic += yazi(94, 22, 'Villus Kesiti', YES, kalin=True)

    ic += kutu(190, 6, 224, 84, CAM_A, CAM)
    ic += yazi(302, 26, 'Villuslardan Kana Geçiş', CAM, kalin=True)
    ic += yazi(302, 50, 'Yalnız yapı taşları emilir', LAC)
    ic += yazi(302, 74, '(Kılcal kan damarlarına)', KIR, kalin=True)
    return svg(420, 96, ic, 'İnce bağırsak villus çıkıntıları ve kılcal damar emilim kesiti.', 21)


def safra_pankreas_karsilastirma():
    ic = kutu(6, 6, 200, 84, TUR_A, TUR)
    ic += yazi(106, 25, 'Safra Sıvısı (Karaciğer)', TUR, kalin=True)
    ic += yazi(106, 51, 'Enzim içermez', LAC)
    ic += yazi(106, 74, 'Büyük yağ → Yağ damlacığı', TUR, kalin=True)

    ic += kutu(214, 6, 200, 84, YES_A, YES)
    ic += yazi(314, 25, 'Pankreas Öz Suyu', YES, kalin=True)
    ic += yazi(314, 51, 'Sindirim enzimi içerir', LAC)
    ic += yazi(314, 74, 'Yağ asidi + Gliserol', YES, kalin=True)
    return svg(420, 96, ic, 'Safra sıvısı ve pankreas öz suyunun yağlara etkisi şeması.', 21)


def yag_emilim_akisi():
    adimlar = [
        (6, '1. Geçiş', 'İnce Bağırsak', MAVI, MAVI_A),
        (110, '2. Fiziksel', 'Safra Sıvısı', TUR, TUR_A),
        (214, '3. Kimyasal', 'Pankreas Özü', YES, YES_A),
        (318, '4. Emilim', 'Villus → Kan', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 96, 84, z, r)
        ic += yazi(x + 48, 30, b1, r, kalin=True)
        ic += yazi(x + 48, 66, b2, LAC)
    return svg(420, 96, ic, 'Yağların ince bağırsakta sindirimi ve villuslardan emilim akışı.', 21)


def sindirim_sagligi_vaka_panosu():
    ic = kutu(6, 6, 200, 84, TUR_A, TUR)
    ic += yazi(106, 25, '1. Durum Bulgusu', TUR, kalin=True)
    ic += yazi(106, 50, 'Az su ve posasız gıda', LAC)
    ic += yazi(106, 74, 'Bağırsak yavaşlaması', TUR, kalin=True)

    ic += kutu(214, 6, 200, 84, KIR_A, KIR)
    ic += yazi(314, 25, '2. Durum Bulgusu', KIR, kalin=True)
    ic += yazi(314, 50, 'Mide asidi tahrişi', LAC)
    ic += yazi(314, 74, 'Mide iç duvarında yara', KIR, kalin=True)
    return svg(420, 96, ic, 'İki farklı sindirim sistemi rahatsızlığının bulgu kartları.', 21)


def villus_duz_karsilastirma():
    ic = kutu(6, 6, 200, 84, YES_A, YES)
    ic += yazi(106, 24, 'Model K (Villuslu)', YES, kalin=True)
    ic += f'<path d="M 24 72 Q 38 36 52 72 Q 66 36 80 72 Q 94 36 108 72 Q 122 36 136 72 Q 150 36 164 72 Q 176 36 188 72" fill="none" stroke="{YES}" stroke-width="2"/>'

    ic += kutu(214, 6, 200, 84, MAVI_A, MAVI)
    ic += yazi(314, 24, 'Model L (Düz Yüzey)', MAVI, kalin=True)
    ic += f'<line x1="234" y1="60" x2="394" y2="60" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += yazi(314, 80, 'Dar temas yüzeyi', LAC)
    return svg(420, 96, ic, 'Villuslu kıvrımlı yüzey ile düz bağırsak yüzeyi karşılaştırma modeli.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = deney_tupleri_sindirim()
    s[2]['gorsel'] = besin_yolculugu_semasi()
    s[5]['gorsel'] = molekul_degisim_grafigi()
    s[6]['gorsel'] = villus_kesit_semasi()
    s[7]['gorsel'] = safra_pankreas_karsilastirma()
    s[8]['gorsel'] = yag_emilim_akisi()
    s[9]['gorsel'] = sindirim_sagligi_vaka_panosu()
    s[11]['gorsel'] = villus_duz_karsilastirma()
