"""8. sınıf Fen Bilimleri 11. hafta (Açık Hava Basıncı, Gaz Basıncı ve Uygulamaları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); eğik kesir ve beyaz bant yok (K155/K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#15803d', '#d63a3a', '#7c3aed', '#0e7490'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A, KUM = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#e0f2fe', '#fffbeb'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def toricelli_uc_boru():
    ic = kutu(4, 4, 412, 100, MAVI_A, MAVI, 8)
    ic += yazi(210, 21, '0 °C Deniz Seviyesi — Cıvalı Barometre Boruları', MAVI)
    # Cıva çanağı
    ic += kutu(36, 78, 224, 20, '#94a3b8', LAC, 4)
    # Üst seviye kesikli hiza çizgisi
    ic += f'<line x1="42" y1="40" x2="264" y2="40" stroke="{KIR}" stroke-width="1.1" stroke-dasharray="4,3"/>'
    # I. Boru (dar dik, S)
    ic += kutu(68, 28, 12, 56, '#e2e8f0', LAC, 3)
    ic += f'<rect x="69" y="40" width="10" height="44" fill="#475569"/>'
    ic += yazi(74, 25, 'I (S)', LAC)
    # II. Boru (kalın dik, 3S)
    ic += kutu(126, 28, 28, 56, '#e2e8f0', LAC, 3)
    ic += f'<rect x="127" y="40" width="26" height="44" fill="#475569"/>'
    ic += yazi(140, 25, 'II (3S)', LAC)
    # III. Boru (dar eğik, S)
    ic += f'<polygon points="196,84 208,84 236,28 224,28" fill="#e2e8f0" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<polygon points="197,84 207,84 229,40 219,40" fill="#475569"/>'
    ic += yazi(234, 25, 'III (S)', LAC)
    # Sağ açıklama
    ic += yazi(338, 52, 'Dik yükseklikler:', KIR)
    ic += yazi(338, 76, 'h₁ , h₂ , h₃ = ?', LAC)
    return svg(420, 108, ic, 'Aynı cıva çanağındaki dar, kalın ve eğik üç barometre borusu.', 22)


def basinc_teknoloji_kartlari():
    kartlar = [
        (4, 4, '1. Hidrolik Lift', 'Sıvı ile araç kaldırma', MAVI, MAVI_A),
        (214, 4, '2. Geniş Palet', 'Yumuşak zeminde kepçe', TUR, TUR_A),
        (4, 58, '3. Plastik Vantuz', 'Cam yüzeye tutunma', CAM, CAM_A),
        (214, 58, '4. Hava Yastığı', 'Çarpma anında şişen balon', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 19, bas, r)
        ic += yazi(x + 101, y + 40, alt, LAC, ince=True)
    return svg(420, 110, ic, 'Hidrolik lift, geniş palet, vantuz ve hava yastığı kartları.', 22)


def dag_kesiti_barometre():
    ic = kutu(4, 4, 412, 100, CAM_A, CAM, 8)
    # Deniz ve dağ üçgeni
    ic += f'<rect x="12" y="84" width="90" height="14" rx="3" fill="#38bdf8"/>'
    ic += f'<polygon points="92,98 205,22 312,98" fill="#bbf7d0" stroke="{YES}" stroke-width="1.2"/>'
    ic += f'<circle cx="102" cy="84" r="4" fill="{KIR}"/>'
    ic += yazi(62, 74, 'K (76 cm)', LAC)
    ic += f'<circle cx="152" cy="58" r="4" fill="{TUR}"/>'
    ic += yazi(112, 52, 'L (71 cm)', TUR)
    ic += f'<circle cx="205" cy="24" r="4" fill="{MOR}"/>'
    ic += yazi(205, 17, 'M (65 cm)', MOR)
    ic += kutu(284, 34, 122, 60, KUM, TUR, 6)
    ic += yazi(345, 56, 'Esnek Balon', TUR)
    ic += yazi(345, 80, 'V_K , V_L , V_M ?', LAC)
    return svg(420, 108, ic, 'Deniz kıyısı K, yamaç L ve zirve M noktalarında barometre değerleri.', 22)


def teneke_kutu_deneyi():
    ic = kutu(4, 4, 412, 98, KUM, TUR, 8)
    ic += kutu(14, 16, 176, 74, KIR_A, KIR, 7)
    ic += yazi(102, 36, '1. Isıtma ve Kapatma', KIR)
    ic += f'<rect x="82" y="44" width="40" height="38" rx="4" fill="#cbd5e1" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(205, 56, '→', TUR)
    ic += kutu(224, 16, 182, 74, MAVI_A, MAVI, 7)
    ic += yazi(315, 36, '2. Soğutma Sonucu', MAVI)
    # İçe büzülmüş kutu poligonu ve dış basınç okları
    ic += f'<polygon points="295,44 335,44 326,63 335,82 295,82 304,63" fill="#94a3b8" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(274, 67, 'P₀→', KIR)
    ic += yazi(356, 67, '←P₀', KIR)
    return svg(420, 106, ic, 'Isıtılıp ağzı kapatılan teneke kutunun soğuyunca açık hava basıncıyla büzülmesi.', 21)


def xy_yogunluk_barometre():
    ic = kutu(4, 4, 200, 96, MAVI_A, MAVI, 8)
    ic += yazi(104, 24, 'X Barometresi (Cıva)', MAVI)
    ic += yazi(104, 54, 'Yoğunluk: d = 13,6', LAC)
    ic += yazi(104, 82, 'Sıvı seviyesi: h_X = 76 cm', MAVI, ince=True)
    ic += kutu(216, 4, 200, 96, YES_A, YES, 8)
    ic += yazi(316, 24, 'Y Barometresi (Etanol)', YES)
    ic += yazi(316, 54, 'Yoğunluk: d = 0,8', LAC)
    ic += yazi(316, 82, 'Sıvı seviyesi: h_Y = ?', YES)
    return svg(420, 104, ic, 'Cıva ve etanol kullanılan X ve Y barometrelerinin yoğunluk karşılaştırması.', 21)


def sise_yumurta_akisi():
    adimlar = [
        (4, '1. Isınma', 'Hava genleşir', KIR, KIR_A),
        (108, '2. Kapatma', 'Alev söner', TUR, TUR_A),
        (212, '3. Soğuma', 'P_iç düşer', CAM, CAM_A),
        (316, '4. İtilme', 'P₀ içeri iter', YES, YES_A),
    ]
    ic = ''
    for x, bas, alt, r, z in adimlar:
        ic += kutu(x, 8, 100, 88, z, r, 7)
        ic += yazi(x + 50, 34, bas, r)
        ic += f'<line x1="{x+10}" y1="46" x2="{x+90}" y2="46" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 50, 72, alt, LAC, ince=True)
    return svg(420, 104, ic, 'Haşlanmış yumurtanın açık hava basıncıyla şişeye girme aşamaları.', 21)


def celik_tup_ve_fren():
    ic = kutu(4, 4, 196, 98, MOR_A, MOR, 8)
    ic += yazi(102, 22, 'Kapalı Çelik Gaz Tüpü', MOR)
    ic += kutu(74, 32, 56, 60, '#e2e8f0', LAC, 12)
    ic += yazi(102, 48, '• K', KIR)
    ic += yazi(102, 66, '• L', MAVI)
    ic += yazi(102, 84, '• M', YES)
    ic += kutu(212, 4, 204, 98, CAM_A, CAM, 8)
    ic += yazi(314, 22, 'Hidrolik Fren Sistemi', CAM)
    ic += yazi(314, 52, 'Pedal → Fren Yağı → Balata', LAC)
    ic += yazi(314, 80, 'Sıvı basıncı aynen iletilir', CAM, ince=True)
    return svg(420, 106, ic, 'Kapalı çelik tüpte K, L, M noktaları ve hidrolik fren sistemi şeması.', 21)


def cay_tabagi_gozlem():
    ic = kutu(4, 4, 412, 98, KUM, TUR, 8)
    # Bardak ve altındaki tabak çizimi
    ic += f'<polygon points="62,24 106,24 98,66 70,66" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.2"/>'
    ic += f'<rect x="46" y="66" width="76" height="7" rx="3" fill="{MAVI}" stroke="{LAC}" stroke-width="1.0"/>'
    ic += yazi(64, 90, '↑ P₀', KIR)
    ic += yazi(104, 90, '↑ P₀', KIR)
    ic += yazi(272, 30, 'Islak Çay Tabağı Deneyi', TUR)
    ic += yazi(272, 56, 'Bardak-tabak arası su hava girişini keser', LAC, ince=True)
    ic += yazi(272, 82, 'Alttan etkiyen P₀ tabağı bardağa bastırır', KIR)
    return svg(420, 106, ic, 'Islak çay tabağının açık hava basıncı etkisiyle çay bardağına tutunması.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = toricelli_uc_boru()
    s[2]['gorsel'] = basinc_teknoloji_kartlari()
    s[5]['gorsel'] = dag_kesiti_barometre()
    s[6]['gorsel'] = teneke_kutu_deneyi()
    s[7]['gorsel'] = xy_yogunluk_barometre()
    s[8]['gorsel'] = sise_yumurta_akisi()
    s[9]['gorsel'] = celik_tup_ve_fren()
    s[11]['gorsel'] = cay_tabagi_gozlem()
