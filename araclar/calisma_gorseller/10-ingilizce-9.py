"""10. sınıf İngilizce 9. hafta görselleri (SVG; insan figürü yok; sunum planı, grafik, konuşma balonları; görsel içi yazı ≈ gövde puntosu, K150 EK).
"""
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


def us(metin):
    return f'<tspan baseline-shift="super" font-size="70%">{metin}</tspan>'


def alt(metin):
    return f'<tspan baseline-shift="sub" font-size="70%">{metin}</tspan>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'



def f(formul, boy=None):
    """C2H6 → C₂H₆ (rakam harf/parantez ardındaysa alt simge)."""
    import re
    return re.sub(r'(?<=[A-Za-z)])(\d+)', lambda m: alt(m.group(1)), formul)


def sunum_plani():
    bol = [('1  Introduction', 'Today I will talk about e-portfolios.', MAVI, MAVI_A),
           ('2  Main body', 'First of all, ... Moreover, ...', TUR, TUR_A),
           ('3  Conclusion', '. . . . . . . . . . . . . . . . . . . .', YES, YES_A)]
    ic = kutu(2, 2, 356, 30 + 40 * len(bol), GRI_A, GRI, 8)
    ic += yazi(180, 20, 'Presentation plan', 11.5, SOLUK, ince=True)
    for i, (b, t, r, a) in enumerate(bol):
        y = 28 + 40 * i
        ic += kutu(12, y, 336, 34, '#fff', r, 6, 1.2) + f'<rect x="12" y="{y}" width="112" height="34" rx="6" fill="{a}"/>'
        ic += yazi(20, y + 22, b, 11.5, r, 'start') + yazi(132, y + 22, t, 11, LAC, 'start', True)
    return svg(ic, 360, 34 + 40 * len(bol), 'Three-part presentation plan', 34)


def grafik():
    veri = [('Podcasts', 6), ('Interactive', 12), ('Online', 9), ('Virtual', 3)]
    alt_ = ['', 'whiteboard', 'dictionary', 'classroom']
    ic = kutu(2, 2, 356, 168, GRI_A, GRI, 8)
    ic += yazi(180, 20, "Class 10-B: favourite learning tools", 11.5, SOLUK, ince=True)
    ox, oy, yuk = 40, 128, 92
    for k in (0, 4, 8, 12):
        y = oy - yuk * k / 12
        ic += f'<line x1="{ox}" y1="{y}" x2="346" y2="{y}" stroke="{GRI}" stroke-width="0.5"/>' + yazi(ox - 6, y + 4, str(k), 11, SOLUK, 'end', True)
    renk = [MAVI, TUR, YES, MOR]
    for i, (ad, d) in enumerate(veri):
        x = ox + 18 + i * 74
        h = yuk * d / 12
        ic += f'<rect x="{x}" y="{oy - h:.1f}" width="40" height="{h:.1f}" rx="3" fill="{renk[i]}"/>'
        ic += yazi(x + 20, oy + 15, ad, 11, LAC) + yazi(x + 20, oy + 28, alt_[i], 11, LAC)
    ic += yazi(14, 76, 'students', 10.5, SOLUK, 'middle', True).replace('<text', '<text transform="rotate(-90 14 76)"')
    return svg(ic, 360, 172, 'Bar chart of favourite learning tools in class 10-B', 44)


def balonlar():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    ic += kutu(12, 12, 280, 40, '#fff', MAVI, 10, 1.2) + yazi(22, 28, 'Deniz:', 11, MAVI, 'start')
    ic += yazi(22, 44, 'Would you rather revise with flashcards or solve practice tests?', 10.5, LAC, 'start', True)
    ic += kutu(130, 64, 218, 40, '#fff', TUR, 10, 1.2) + yazi(140, 80, 'Arda:', 11, TUR, 'start')
    ic += yazi(140, 96, '. . . . . . . . . . . . . . . . . .', 11, LAC, 'start', True)
    return svg(ic, 360, 116, 'A short chat between Deniz and Arda', 30)


def donustur():
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    ic += kutu(12, 12, 336, 30, '#fff', MAVI, 6, 1.2)
    ic += yazi(180, 32, 'Ece prepares a study calendar in order to plan her revision.', 11, LAC, ince=True)
    ic += f'<line x1="180" y1="44" x2="180" y2="56" stroke="{TUR}" stroke-width="1.6"/><polygon points="180,62 175,54 185,54" fill="{TUR}"/>'
    ic += kutu(12, 62, 336, 28, '#fff', TUR, 6, 1.2) + yazi(180, 81, 'Ece prepares a study calendar so that . . . . . . . . . .', 11, LAC, ince=True)
    return svg(ic, 360, 100, 'Rewrite the sentence with so that', 26)


def slayt():
    ic = kutu(2, 2, 356, 132, GRI_A, GRI, 8)
    ic += kutu(40, 12, 280, 106, '#fff', LAC, 4, 1.4)
    ic += yazi(180, 32, 'Screen time and homework', 12, LAC)
    for i, (h, r) in enumerate(((52, MAVI), (34, TUR), (68, YES))):
        x = 110 + i * 50
        ic += f'<rect x="{x}" y="{106 - h}" width="30" height="{h}" fill="{r}"/>'
    ic += f'<line x1="96" y1="106" x2="266" y2="106" stroke="{LAC}"/>'
    ic += yazi(180, 130, 'Slide 4', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 136, 'A presentation slide with a bar chart', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sunum_plani()
    s[3]['gorsel'] = grafik()
    s[7]['gorsel'] = balonlar()
    s[9]['gorsel'] = donustur()
    s[11]['gorsel'] = slayt()
