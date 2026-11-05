"""9. sınıf Fizik 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}"/>'

def dörtlu_kart(etiket, kartlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis_karti(etiket, adimlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def uclu_pano(etiket, ust_baslik, kutular, ana_renk=MAVI, ana_acik=MAVI_A):
    ic = kutu(4, 4, 352, 107, ana_acik, ana_renk) + yazi(180, 23, ust_baslik, 10, ana_renk)
    for i, (b, alt, c, d) in enumerate(kutular):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 66, d, c) + yazi(x + 52, 55, b, 9.5, c) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def bilgi_panosu(etiket, baslik, satir1, satir2, c=CAM, d=CAM_A, ic_d='#eaf7fa'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 25, baslik, 10, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, satir1, 9.6, LAC) + yazi(180, 82, satir2, 8.6, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return dörtlu_kart('Eşit iki vektörde özel açılar', [
        ('θ = 0° (Aynı)', 'R = 2F (Maksimum)', MAVI, MAVI_A),
        ('θ = 60°', '__G0_1__', YES, YES_A),
        ('θ = 90° (Dik)', '__G0_2__', TUR, TUR_A),
        ('θ = 120°', 'R = F (Kendisine eşit)', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Kartezyen koordinat sisteminde vektör', 'KARTEZYEN SİSTEMDE VEKTÖR GÖSTERİMİ VE TOPLAMA', [
        ('A(x, y) Gösterimi', 'Başlangıç O(0, 0)', MAVI, '#f4f8fe'),
        ('Bileşke R(Rx, Ry)', 'Rx = Ax+Bx, Ry = Ay+By', YES, YES_A),
        ('Büyüklük |R|', '__G1_1__', TUR, TUR_A)
    ], MAVI, MAVI_A)
def g2():
    return bilgi_panosu('Bileşke vektör sınır değerleri', 'İKİ VEKTÖRÜN BİLEŞKE ARALIĞI: |A - B| ≤ R ≤ A + B',
        'En büyük değer θ = 0° iken R_max = A + B · En küçük değer θ = 180° iken R_min = |A - B|',
        'İki vektör arasındaki açı arttıkça bileşke vektörün büyüklüğü (R) azalır.', CAM, CAM_A)
def g3():
    return dörtlu_kart('Vektör temel özellikleri', [
        ('Eşit Vektör (K=L)', 'Yön ve şiddet aynı', MAVI, MAVI_A),
        ('Zıt Vektör (K=-M)', 'Yön 180° tam ters', KIR, KIR_A),
        ('Skaler Çarpım', 'k<0 ise yön döner', TUR, TUR_A),
        ('Kapalı Çokgen', 'Uç uca dönerse R=0', YES, YES_A)
    ])
def g5():
    return akis_karti('Dik bileşenlerle bileşke hesabı', [
        ('1. Bileşen Ayır', 'Fx=Fcosθ, Fy=Fsinθ', MAVI, MAVI_A),
        ('2. Yatay Topla', 'Rx = ΣFx hesapla', YES, YES_A),
        ('3. Düşey Topla', 'Ry = ΣFy hesapla', TUR, TUR_A),
        ('4. Pisagor Al', '__G5_1__', MOR, MOR_A)
    ])
def g6():
    return uclu_pano('Eşit kuvvetlerde açı etkisi', 'F₁ = F₂ = F İKEN AÇIYA GÖRE BİLEŞKE', [
        ('θ = 60° İken', '__G6_1__', YES, YES_A),
        ('θ = 90° İken', '__G6_2__', MAVI, '#f4f8fe'),
        ('θ = 120° İken', 'R = F (Tek kuvvete eşit)', TUR, TUR_A)
    ], YES, YES_A)
def g7():
    return bilgi_panosu('Vektör toplama ve çıkarma yöntemleri', 'UÇ UCA EKLEME · PARALELKENAR · VEKTÖR ÇIKARMA',
        'Uç uca eklemede ilk başlangıçtan son bitişe çizilen ok bileşke vektörü (R) verir',
        'Vektör çıkarmada A - B = A + (-B) eşitliği kullanılır; çıkan vektör ters çevrilip toplanır.', TUR, TUR_A, '#fff6ea')
def g8():
    return dörtlu_kart('Özel dik üçgenlerle büyüklük', [
        ('3 - 4 - 5', 'K(3, 4) → |K| = 5', MAVI, MAVI_A),
        ('6 - 8 - 10', 'L(-6, 8) → |L| = 10', YES, YES_A),
        ('5 - 12 - 13', 'M(5, -12) → |M| = 13', TUR, TUR_A),
        ('8 - 15 - 17', 'N(8, 15) → |N| = 17', MOR, MOR_A)
    ])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()

_eski_uygula = uygula
def _temizle9(svg_s):
    svg_s = svg_s.replace('<text x="136.0" y="72.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">__G0_1__</text>', '<text x="135.0" y="72.0" text-anchor="end" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">R = F</text><path d="M 135.8 68.9 L 137.1 68.9 L 138.5 72.6 L 140.8 64.1 L 147.8 64.1" fill="none" stroke="#0b2257" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="144.3" y="72.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">3</text>')
    svg_s = svg_s.replace('<text x="222.0" y="72.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">__G0_2__</text>', '<text x="206.0" y="72.0" text-anchor="end" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">R = F</text><path d="M 206.8 69.1 L 208.1 69.1 L 209.5 72.6 L 211.8 64.7 L 218.4 64.7" fill="none" stroke="#0b2257" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="215.1" y="72.0" text-anchor="middle" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">2</text><text x="218.9" y="72.0" text-anchor="start" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257"> (dik)</text>')
    svg_s = svg_s.replace('<text x="290.0" y="78.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">__G1_1__</text>', '<path d="M 264.8 75.0 L 266.1 75.0 L 267.5 78.6 L 269.8 70.3 L 313.8 70.3" fill="none" stroke="#5b6479" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="291.8" y="78.0" text-anchor="middle" font-size="8.0" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">Rx² + Ry²</text>')
    svg_s = svg_s.replace('<text x="308.0" y="68.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">__G5_1__</text>', '<text x="286.0" y="68.0" text-anchor="end" font-size="7.4" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">R = </text><path d="M 286.8 65.2 L 288.1 65.2 L 289.5 68.6 L 291.8 60.9 L 324.0 60.9" fill="none" stroke="#0b2257" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="307.9" y="68.0" text-anchor="middle" font-size="7.4" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">Rx²+Ry²</text>')
    svg_s = svg_s.replace('<text x="66.0" y="78.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">__G6_1__</text>', '<text x="48.0" y="78.0" text-anchor="end" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">R = F</text><path d="M 48.8 75.2 L 50.1 75.2 L 51.5 78.6 L 53.8 70.8 L 60.3 70.8" fill="none" stroke="#5b6479" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="57.1" y="78.0" text-anchor="middle" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">3</text><text x="60.8" y="78.0" text-anchor="start" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479"> (büyük)</text>')
    svg_s = svg_s.replace('<text x="178.0" y="78.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">__G6_2__</text>', '<text x="162.0" y="78.0" text-anchor="end" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">R = F</text><path d="M 162.8 75.1 L 164.1 75.1 L 165.5 78.6 L 167.8 70.7 L 174.4 70.7" fill="none" stroke="#5b6479" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="171.1" y="78.0" text-anchor="middle" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">2</text><text x="174.9" y="78.0" text-anchor="start" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479"> (dik)</text>')
    return svg_s

def uygula(o):
    _eski_uygula(o)
    for q in o['sorular']:
        if q.get('gorsel'):
            q['gorsel'] = _temizle9(q['gorsel'])
