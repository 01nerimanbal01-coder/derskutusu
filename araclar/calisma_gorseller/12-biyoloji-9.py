"""12. sınıf Biyoloji 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
import math
LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def us(m):
    return f'<tspan baseline-shift="super" font-size="70%">{m}</tspan>'


def alt(m):
    return f'<tspan baseline-shift="sub" font-size="70%">{m}</tspan>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ok(x1, y1, x2, y2, renk=SOLUK, k=1):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2 - 6 * math.cos(a - 0.45):.1f},{y2 - 6 * math.sin(a - 0.45):.1f} {x2:.1f},{y2:.1f} {x2 - 6 * math.cos(a + 0.45):.1f},{y2 - 6 * math.sin(a + 0.45):.1f}'
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{renk}" stroke-width="{k}"/>'
            f'<polyline points="{u}" fill="none" stroke="{renk}" stroke-width="{k}"/>')


def cubuk(veri, baslik, etiket, mm=40, renk=MAVI, birim=''):
    """veri: [(alt yazı, değer, gösterilecek yazı)]"""
    n = len(veri); en, boy = 360, 168
    ust = max(v for _, v, _ in veri)
    ic = kutu(2, 2, 356, 164, GRI_A, GRI, 8) + yazi(180, 22, baslik, 12.5, renk)
    ox, oy, yuk = 24, 140, 96
    ic += f'<line x1="{ox}" y1="{oy}" x2="346" y2="{oy}" stroke="{LAC}" stroke-width="1"/>'
    adim = (346 - ox) / n
    for i, (a, v, g) in enumerate(veri):
        h = yuk * v / ust; x = ox + i * adim + adim * 0.2; w = adim * 0.6
        ic += f'<rect x="{x:.1f}" y="{oy - h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" fill="{renk}"/>'
        ic += yazi(x + w / 2, oy - h - 5, g, 12, renk)
        ic += yazi(x + w / 2, oy + 17, a, 12, LAC)
    return svg(ic, en, boy, etiket, mm)


def plazmit_gen():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    cx, cy, r = 92, 70, 42
    # açıklığı olan halka (sağ üstte kesik)
    a1, a2 = math.radians(-20), math.radians(-60)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
    ic += f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 1 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{MAVI}" stroke-width="6"/>'
    ic += yazi(cx, cy + 5, 'Plazmit', 12.5, MAVI)
    ic += yazi(cx + 52, cy - 52, 'kesik', 11, KIR, 'start', True)
    # hedef gen
    ic += f'<rect x="206" y="66" width="104" height="14" rx="3" fill="{TUR}"/>'
    ic += yazi(258, 104, 'Hedef gen', 12.5, TUR)
    for x in (200, 310):
        ic += f'<rect x="{x - 6}" y="60" width="12" height="7" fill="{YES}"/>'
    ic += yazi(258, 48, 'yapışkan uçlar', 11, YES, ince=True)
    ic += ok(158, 74, 194, 74, SOLUK, 1.2)
    ic += yazi(180, 140, 'Uçlar birbirini tamamlar; birleştiren enzim: ?', 11.5, LAC, ince=True)
    return svg(ic, 360, 152, 'Kesik plazmit ve uçları yapışkan hedef gen', 38)


def adaylar():
    veri = [('K', '2 yıl', '1', 'büyük', 'pahalı'), ('L', '10 gün', '400', 'küçük', 'ucuz'), ('M', '3 ay', '6', 'orta', 'pahalı')]
    satir = ['Döl süresi', 'Bir defada yavru', 'Genom', 'Bakım']
    ic = kutu(2, 2, 356, 132, GRI_A, GRI, 8)
    for j, s in enumerate(satir):
        ic += yazi(14, 52 + j * 22, s, 11, SOLUK, 'start', True)
    renk = [MOR, YES, MAVI]
    for i, (ad, *d) in enumerate(veri):
        x = 124 + i * 78
        ic += kutu(x, 12, 70, 116, '#fff', renk[i], 8, 1)
        ic += yazi(x + 35, 32, ad, 14, renk[i])
        for j, v in enumerate(d):
            ic += yazi(x + 35, 52 + j * 22, v, 12, LAC)
    return svg(ic, 360, 136, 'K, L ve M canlılarının döl süresi, yavru sayısı, genom büyüklüğü ve bakım maliyeti', 34)


def etiket():
    ic = kutu(2, 2, 356, 104, GRI_A, GRI, 8)
    ic += kutu(40, 14, 280, 80, '#fff', LAC, 10, 1.2)
    ic += yazi(180, 38, 'MISIR UNU · 500 g', 13, LAC)
    ic += kutu(58, 50, 244, 32, KIR_A, KIR, 6, 1)
    ic += yazi(180, 71, 'Genetiği değiştirilmiş mısır içerir.', 12, KIR)
    return svg(ic, 360, 108, 'Ambalaj etiketi: genetiği değiştirilmiş mısır içerir', 28)


def bolunme():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    for i, (t, n) in enumerate([('0 dk', 1), ('20 dk', 2), ('40 dk', 4)]):
        x = 30 + i * 112
        for k in range(n):
            bx = x + 30 + (k % 2) * 26 - (13 if n > 1 else 0); by = 42 + (k // 2) * 22 - (11 if n > 2 else 0)
            ic += f'<rect x="{bx - 11}" y="{by - 6}" width="22" height="12" rx="6" fill="#bfe8cf" stroke="{YES}" stroke-width="1.6"/>'
        ic += yazi(x + 30, 92, t, 12, LAC)
        if i < 2:
            ic += ok(x + 66, 50, x + 94, 50, SOLUK, 1.2)
    ic += yazi(338, 54, '…', 16, SOLUK)
    return svg(ic, 360, 116, 'Bakteri her 20 dakikada bir ikiye bölünüyor', 30)


def kesim():
    ust, alt_ = 'TCGAATTCAG', 'AGCTTAAGTC'
    ic = kutu(2, 2, 356, 118, GRI_A, GRI, 8)
    x0, w = 50, 26
    for i, (a, b) in enumerate(zip(ust, alt_)):
        x = x0 + i * w
        vurgu = 2 <= i <= 7
        ic += kutu(x, 30, w - 2, 22, TUR_A if vurgu else '#fff', TUR if vurgu else GRI, 3, 0.8) + yazi(x + w / 2 - 1, 46, a, 12.5, LAC)
        ic += kutu(x, 64, w - 2, 22, TUR_A if vurgu else '#fff', TUR if vurgu else GRI, 3, 0.8) + yazi(x + w / 2 - 1, 80, b, 12.5, LAC)
    ic += yazi(30, 46, "5'", 11, SOLUK, ince=True) + yazi(30, 80, "3'", 11, SOLUK, ince=True)
    ic += yazi(330, 46, "3'", 11, SOLUK, ince=True) + yazi(330, 80, "5'", 11, SOLUK, ince=True)
    xu = x0 + 3 * w - 1; xa = x0 + 7 * w - 1
    ic += ok(xu, 12, xu, 28, KIR, 1.6) + ok(xa, 106, xa, 90, KIR, 1.6)
    ic += yazi(xu + 6, 22, 'kesim', 11, KIR, 'start', True) + yazi(xa + 6, 104, 'kesim', 11, KIR, 'start', True)
    return svg(ic, 360, 120, 'Çift zincirli DNA parçası ve kesim yerleri', 30)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = plazmit_gen()
    s[3]['gorsel'] = adaylar()
    s[4]['gorsel'] = etiket()
    s[12]['gorsel'] = bolunme()
    s[13]['gorsel'] = kesim()
