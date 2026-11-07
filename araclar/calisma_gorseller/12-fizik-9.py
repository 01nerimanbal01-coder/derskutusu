"""12. sınıf Fizik 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


def yay_bhh(cisim='L'):
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    ic += f'<rect x="14" y="16" width="10" height="62" fill="{SOLUK}"/>'
    ic += f'<line x1="14" y1="78" x2="346" y2="78" stroke="{LAC}" stroke-width="1.4"/>'
    xs = {'K': 100, 'O': 190, 'L': 280}
    cx = xs[cisim]
    # yay (zikzak)
    n = 14; x0, x1 = 24, cx - 20
    pts = [f'{x0},50'] + [f'{x0 + (x1 - x0) * (i + 0.5) / n:.1f},{40 if i % 2 else 60}' for i in range(n)] + [f'{x1},50']
    ic += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += kutu(cx - 20, 32, 40, 46, TUR_A, TUR, 4, 1.4) + yazi(cx, 60, 'm', 13, TUR)
    for ad, x in xs.items():
        ic += f'<line x1="{x}" y1="74" x2="{x}" y2="84" stroke="{LAC}" stroke-width="1.4"/>'
        ic += yazi(x, 100, ad, 13, KIR if ad == 'O' else LAC)
    ic += yazi(320, 100, 'Sürtünmesiz', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 116, f'Yaya bağlı cisim, K ile L arasında salınıyor; cisim {cisim} noktasında', 30)


def cember_golge():
    cx, cy, r = 120, 92, 56
    ic = kutu(2, 2, 356, 170, GRI_A, GRI, 8)
    for x in (60, 100, 140, 180):
        ic += ok(x, 12, x, 28, TUR, 1.1)
    ic += yazi(250, 22, 'Paralel ışık', 11.5, TUR, ince=True)
    ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<line x1="{cx - r}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{LAC}" stroke-width="1.6"/>'
    a = math.radians(-50); px, py = cx + r * math.cos(a), cy + r * math.sin(a)
    ic += f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{SOLUK}" stroke-width="1"/>'
    ic += yazi(cx + 10, cy - 24, 'r', 12, SOLUK)
    ic += f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{px:.1f}" y2="{cy}" stroke="{SOLUK}" stroke-dasharray="3 3"/>'
    ic += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{TUR}"/>'
    ic += f'<ellipse cx="{px:.1f}" cy="{cy}" rx="6" ry="3" fill="{LAC}"/>'
    ic += yazi(px - 8, cy + 18, 'gölge', 11, LAC, 'end', True)
    ic += f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="{KIR}"/>'
    ic += kutu(214, 62, 134, 62, '#fff', MAVI, 8)
    ic += yazi(281, 86, 'r = 20 cm', 13, MAVI)
    ic += yazi(281, 110, '1 tur: 4 s', 13, MAVI)
    return svg(ic, 360, 172, 'Çember üzerinde dönen cisim ve yatay çap üzerindeki gölgesi', 42)


def yorungeler():
    cx, cy = 120, 82
    ic = kutu(2, 2, 356, 160, GRI_A, GRI, 8)
    ic += f'<circle cx="{cx}" cy="{cy}" r="72" fill="none" stroke="{MOR}" stroke-width="1.3"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="18" fill="none" stroke="{YES}" stroke-width="1.3"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="8" fill="{TUR}"/>'
    ic += f'<circle cx="{cx + 18}" cy="{cy}" r="5" fill="{YES}"/>' + yazi(cx + 18, cy - 9, 'Y', 12, YES)
    ic += f'<circle cx="{cx + 72}" cy="{cy}" r="6" fill="{MOR}"/>' + yazi(cx + 72, cy - 11, 'X', 12, MOR)
    ic += ok(cx, cy + 26, cx + 18, cy + 26, YES) + yazi(cx + 9, cy + 42, 'R', 12, YES)
    ic += ok(cx, cy + 56, cx + 72, cy + 56, MOR) + yazi(cx + 36, cy + 50, '?', 13, MOR)
    ic += kutu(222, 50, 126, 64, '#fff', GRI, 8)
    ic += yazi(285, 76, f'T{alt("Y")} = 1 yıl', 13, YES)
    ic += yazi(285, 100, f'T{alt("X")} = 27 yıl', 13, MOR)
    return svg(ic, 360, 164, 'Güneş çevresinde iki yörünge; iç yörüngenin yarıçapı R', 40)


def elips(alanlar, gunes_ust=False):
    cx, cy, a, b = 180, 82, 150, 64
    c = math.sqrt(a * a - b * b); gx = cx - c
    ic = kutu(2, 2, 356, 160, GRI_A, GRI, 8)
    def nokta(t):
        return cx + a * math.cos(t), cy + b * math.sin(t)
    for t1, t2, renk, dol, et in alanlar:
        pts = [f'{gx:.1f},{cy}'] + ['{:.1f},{:.1f}'.format(*nokta(t1 + (t2 - t1) * i / 20)) for i in range(21)]
        ic += f'<polygon points="{" ".join(pts)}" fill="{dol}" stroke="{renk}" stroke-width="1"/>'
        xs = [gx] + [nokta(t1 + (t2 - t1) * i / 20)[0] for i in range(21)]
        ys = [cy] + [nokta(t1 + (t2 - t1) * i / 20)[1] for i in range(21)]
        lx, ly = (sum(xs) / len(xs), sum(ys) / len(ys) + 5) if et != 'S' else (82, 116)
        ic += yazi(lx, ly, et, 13, renk)
    ic += f'<ellipse cx="{cx}" cy="{cy}" rx="{a}" ry="{b}" fill="none" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<circle cx="{gx:.1f}" cy="{cy}" r="9" fill="{TUR}"/>' + (yazi(gx - 2, cy + 24, 'Güneş', 11, TUR) if gunes_ust else yazi(gx + 14, cy + 4, 'Güneş', 11, TUR, 'start'))
    return ic


def elips_ab():
    ic = elips([])
    ic += f'<circle cx="30" cy="82" r="5" fill="{MAVI}"/>' + yazi(18, 86, 'A', 13, MAVI)
    ic += f'<circle cx="330" cy="82" r="5" fill="{MAVI}"/>' + yazi(343, 86, 'B', 13, MAVI)
    return svg(ic, 360, 164, 'Güneş bir odakta; A Güneşe yakın, B uzak nokta', 38)


def elips_alan():
    ic = elips([(math.radians(100), math.radians(235), MAVI, MAVI_A, 'S'), (math.radians(-25), math.radians(25), YES, YES_A, '2S')], True)
    return svg(ic, 360, 164, 'Eliptik yörüngede taranan S ve 2S alanları', 38)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = yay_bhh('L')
    s[3]['gorsel'] = cember_golge()
    s[6]['gorsel'] = yorungeler()
    s[7]['gorsel'] = elips_ab()
    s[11]['gorsel'] = yay_bhh('K')
    s[12]['gorsel'] = elips_alan()
