"""12. sınıf İngilizce 9. hafta görselleri (insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


def kart(baslik, satirlar, renk, renk_a, etiket, mm=32):
    h = 44 + 18 * len(satirlar)
    ic = kutu(2, 2, 356, h + 16, GRI_A, GRI, 8)
    ic += kutu(16, 10, 328, h, '#fff', renk, 8, 1.2)
    ic += f'<rect x="16" y="10" width="328" height="26" rx="8" fill="{renk_a}"/>'
    ic += yazi(180, 28, baslik, 12.5, renk)
    for j, t in enumerate(satirlar):
        ic += yazi(32, 56 + j * 18, t, 11.5, LAC, 'start', ince=True)
    return svg(ic, 360, h + 20, etiket, mm)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kart('NOTICE — City Library', ['The only entrance has twelve steps.', 'There is no lift or ramp.', 'Wheelchair users cannot enter the building.'], KIR, KIR_A, 'Library notice: entrance has only stairs')
    s[9]['gorsel'] = kart('Essay plan', ['Topic: Equal access to education', 'Thesis: ?', 'Body 1: Education reduces poverty.', 'Body 2: Educated citizens protect rights.', 'Counter-argument: “It is too expensive.”'], MAVI, MAVI_A, 'Essay plan with missing thesis statement', 38)
    s[11]['gorsel'] = kart('Neighbourhood note', ['Mr Demir is 84 and lives alone.', 'He finds shopping difficult and', 'rarely talks to anyone during the week.'], TUR, TUR_A, 'Note about an elderly neighbour living alone')
