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
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

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
        ('θ = 60°', 'R = F√3', YES, YES_A),
        ('θ = 90° (Dik)', 'R = F√2 (Pisagor)', TUR, TUR_A),
        ('θ = 120°', 'R = F (Kendisine eşit)', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Kartezyen koordinat sisteminde vektör', 'KARTEZYEN SİSTEMDE VEKTÖR GÖSTERİMİ VE TOPLAMA', [
        ('A(x, y) Gösterimi', 'Başlangıç O(0, 0)', MAVI, '#f4f8fe'),
        ('Bileşke R(Rx, Ry)', 'Rx = Ax+Bx, Ry = Ay+By', YES, YES_A),
        ('Büyüklük |R|', '√(Rx² + Ry²)', TUR, TUR_A)
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
        ('4. Pisagor Al', 'R = √(Rx² + Ry²)', MOR, MOR_A)
    ])
def g6():
    return uclu_pano('Eşit kuvvetlerde açı etkisi', 'F₁ = F₂ = F İKEN AÇIYA GÖRE BİLEŞKE', [
        ('θ = 60° İken', 'R = F√3 (Daha büyük)', YES, YES_A),
        ('θ = 90° İken', 'R = F√2 (Dik köşegen)', MAVI, '#f4f8fe'),
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
