"""11. sınıf Kimya 8. hafta görselleri (SVG; insan figürü yok K024; beyaz bant yok K178; 24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket):
    stil = ' style="width:100%;max-height:24mm;display:block;margin:1mm auto;"'
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+81},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def uclu(baslik, k1, a1, k2, a2, k3, a3, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 22, baslik, 10.0, c)
    for i, (k, a, rk, dk) in enumerate([(k1, a1, MAVI, MAVI_A), (k2, a2, TUR, TUR_A), (k3, a3, YES, YES_A)]):
        x = 12 + i * 114
        ic += kutu(x, 32, 108, 70, dk, rk) + yazi(x + 54, 54, k, 9.2, rk) + yazi(x + 54, 78, a, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.2, LAC) + yazi(180, 82, s2, 8.4, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def g0():
    return cizelge4([('Tepken Hızı', 'r = -Δ[R] / Δt', KIR, KIR_A), ('Ürün Hızı', 'r = +Δ[P] / Δt', YES, YES_A), ('SI Hız Birimi', 'mol/(L·s) = M/s', MAVI, MAVI_A), ('Anlık Hız', 'Teğetin eğimi', MOR, MOR_A)], 'Tepkime hızı bağıntıları ve birimleri')
def g1():
    return uclu('AMONYAK SENTEZİ: N2(g) + 3H2(g) -> 2NH3(g)', 'N2 Harcanma (1k)', 'r(N2) = 0,2 M/s', 'H2 Harcanma (3k)', 'r(H2) = 0,6 M/s', 'NH3 Oluşma (2k)', 'r(NH3) = 0,4 M/s', MAVI, MAVI_A, 'Amonyak sentezinde stokiyometrik hız oranları')
def g2():
    return ikili('TEPKKEN VE ÜRÜN DERİŞİMİNİN ZAMANLA DEĞİŞİMİ', 'Tepken Derişimi [R]', 'Zamanla azalır -> Δ[R] < 0', 'Ürün Derişimi [P]', 'Zamanla artar -> Δ[P] > 0', KIR, KIR_A, YES, YES_A, 'Tepken ve ürün derişim değişimi')
def g3():
    return uclu('HIZ HESAPLAMALARINDA ÜÇ TEMEL KAVRAM', 'Ortalama Hız', 'Kesen doğrunun eğimi', 'Stokiyometrik Oran', 'Katsayılarla doğru orantı', 'Anlık Hız', 't anındaki teğet eğimi', TUR, TUR_A, 'Ortalama hız, stokiyometri ve anlık hız')
def g6():
    return akis4([('1. Başlangıç', 'Derişim ve hız maks.', YES, YES_A), ('2. Harcanma', 'Tepken sayısı azalır', TUR, TUR_A), ('3. Çarpışma', 'Etkin çarpışma düşer', MAVI, MAVI_A), ('4. Yavaşlama', 'Tepkime hızı azalır', MOR, MOR_A)], 'Tepkime hızının zamanla azalma süreci')
def g7():
    return kart('GENEL TEPKİME HIZI DENKLEMİ: 2A + B -> 3C', 'r_genel = - Δ[A] / (2·Δt) = - Δ[B] / Δt = + Δ[C] / (3·Δt)', 'Madde hızları arasında: 3·r(A) = 6·r(B) = 2·r(C) bağıntısı vardır.', MAVI, MAVI_A, 'Genel tepkime hızı eşitliği')
def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 20, 'DERİŞİM - ZAMAN GRAFİĞİ VE EĞİMİN AZALMASI', 9.8, MAVI)
    ic += f'<line x1="45" y1="92" x2="325" y2="92" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<line x1="45" y1="92" x2="45" y2="28" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<path d="M 45,32 Q 115,82 310,89" fill="none" stroke="{KIR}" stroke-width="2.2"/>'
    ic += f'<path d="M 45,92 Q 115,42 310,35" fill="none" stroke="{YES}" stroke-width="2.2"/>'
    ic += yazi(280, 48, 'Ürün [P]', 9.0, YES) + yazi(280, 78, 'Tepken [R]', 9.0, KIR)
    ic += yazi(180, 105, 'Zamanla eğrinin eğimi (teğet açısı) ve anlık hız küçülür.', 8.4, LAC, ince=True)
    return svg(360, 115, ic, 'Derişim zaman grafiği eğrileri')
def g9():
    return ikili('ZAMAN ARALIKLARINDA ORTALAMA HIZ KARŞILAŞTIRMASI', '0 - 10 s Aralığı (1,0 -> 0,4 M)', 'r1 = 0,6 / 10 = 0,06 M/s', '10 - 20 s Aralığı (0,4 -> 0,1 M)', 'r2 = 0,3 / 10 = 0,03 M/s', MAVI, MAVI_A, MOR, MOR_A, 'İlk ve ikinci 10 saniyede ortalama hız')

def uygula(o):
    s = o['sorular']
    for idx, fn in [(0, g0), (1, g1), (2, g2), (3, g3), (6, g6), (7, g7), (8, g8), (9, g9)]:
        s[idx]['gorsel'] = fn()
