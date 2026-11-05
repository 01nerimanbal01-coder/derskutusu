"""10. sınıf Kimya 2. hafta (Kimyasal Tepkimelerin Oluşumu ve Modellenmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_gosterim_duzeyleri():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    duzeyler = [
        ('Makroskobik', 'Renk & Çökelti', MAVI, MAVI_A),
        ('Alt Mikroskobik', 'Atom & Molekül', YES, YES_A),
        ('Sembolik', 'Kimyasal Denklem', TUR, TUR_A),
        ('Modelleme', 'Top-çubuk & Dolgu', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(duzeyler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kimyada üç temel gösterim düzeyi kartı', 34)


def g1_tepkime_modeli():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    # Girenler: CH4 + 2O2
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    ic += yazi(84, 28, 'Girenler (CH₄ + 2O₂)', 9.5, MAVI)
    ic += f'<circle cx="64" cy="52" r="12" fill="{LAC}"/>' # C
    ic += f'<circle cx="64" cy="34" r="6" fill="{GRI}"/>' # H
    ic += f'<circle cx="64" cy="70" r="6" fill="{GRI}"/>' # H
    ic += f'<circle cx="46" cy="52" r="6" fill="{GRI}"/>' # H
    ic += f'<circle cx="82" cy="52" r="6" fill="{GRI}"/>' # H
    ic += f'<circle cx="114" cy="52" r="9" fill="{KIR}"/>' # O
    ic += f'<circle cx="128" cy="52" r="9" fill="{KIR}"/>' # O

    # Ürünler: CO2 + 2H2O
    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 28, 'Ürünler (CO₂ + 2H₂O)', 9.5, YES)
    ic += yazi(257, 48, '• Atom türü ve sayısı korunur', 9, LAC, ince=True)
    ic += yazi(257, 62, '• Eski bağlar kopar', 9, LAC, ince=True)
    ic += yazi(257, 76, '• Yeni bağlar kurulur', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Metan yanma tepkimesi tanecik modeli', 34)


def g2_bag_kirilmasi():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += kutu(14, 12, 150, 76, '#fef6ec', TUR, 6, 1.2)
    ic += yazi(89, 28, 'Bağ Kırılması', 10.5, KIR)
    ic += yazi(89, 48, 'A—B + Enerji -> A + B', 9.5, LAC)
    ic += yazi(89, 70, 'ENDOTERMİK (Isı alan)', 9.5, KIR)

    ic += kutu(176, 12, 170, 76, '#fff8f0', TUR, 6, 1.2)
    ic += yazi(261, 28, 'Bağ Oluşumu', 10.5, YES)
    ic += yazi(261, 48, 'C + D -> C—D + Enerji', 9.5, LAC)
    ic += yazi(261, 70, 'EKZOTERMİK (Isı veren)', 9.5, YES)
    return svg(360, 100, ic, 'Kimyasal bağ kırılması ve oluşumu enerji şeması', 34)


def g3_molekul_modelleri():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    modeller = [
        ('Uzay-Dolgu', 'Gerçek hacimler', '#eaf7fa'),
        ('Top-Çubuk', 'Bağ açıları', '#dbf3f7'),
        ('Lewis Yapısı', 'Değerlik nokta', '#cbf0f5'),
        ('Çizgi-Bağ', 'Kovalent çizgiler', '#bcecf2')
    ]
    for i, (b, d, bg) in enumerate(modeller):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, bg, CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Dört farklı molekül modelleme yöntemi', 34)


def g5_reaksiyon_akisi():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    adımlar = [
        ('1. Çarpışma', 'Etkin temas'),
        ('2. Kopma', 'Eski bağlar'),
        ('3. Düzen', 'Atom geçişi'),
        ('4. Ürün', 'Yeni kararlı bağ')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kimyasal tepkimenin moleküler gerçekleşme akışı', 34)


def g6_sembolik_denklem():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += kutu(14, 12, 140, 76, '#ece4fd', MOR, 6, 1.2)
    ic += yazi(84, 30, 'DENKLEM VE ORAN', 10, MOR)
    ic += yazi(84, 52, '1 CH₄ + 2 O₂', 12, LAC)
    ic += yazi(84, 72, '1 : 2 Mol Oranı', 9.5, TUR)

    ic += kutu(168, 12, 178, 76, '#f4effe', MOR, 6, 1.2)
    ic += yazi(257, 30, 'Gösterim Düzeyi', 10.5, MOR)
    ic += yazi(257, 48, 'Sembolik ve alt mikroskobik', 9.5, LAC)
    ic += yazi(257, 66, 'seviyede tepkime denkliğini', 9, LAC, ince=True)
    ic += yazi(257, 78, 've katsayıları belirtir.', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Sembolik kimyasal denklem katsayıları şeması', 34)


def g8_model_karsilastirma():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Uzay-Dolgu', 'Bitişik küreler', MAVI, MAVI_A),
        ('Top-Çubuk', 'Ayrık & Çubuklu', YES, YES_A),
        ('Lewis Nokta', 'Değerlik e⁻', TUR, TUR_A),
        ('Çizgi-Bağ', 'Çift elektron çizgisi', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kimyasal modeller gösterim biçimleri', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: M - O - D - E - L', 11.5, YES)
    harfler = [('1', 'M'), ('2', 'O'), ('3', 'D'), ('4', 'E'), ('5', 'L')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Model şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_gosterim_duzeyleri()
    s[1]['gorsel'] = g1_tepkime_modeli()
    s[2]['gorsel'] = g2_bag_kirilmasi()
    s[3]['gorsel'] = g3_molekul_modelleri()
    s[5]['gorsel'] = g5_reaksiyon_akisi()
    s[6]['gorsel'] = g6_sembolik_denklem()
    s[8]['gorsel'] = g8_model_karsilastirma()
    s[10]['gorsel'] = g10_sifre_seridi()
