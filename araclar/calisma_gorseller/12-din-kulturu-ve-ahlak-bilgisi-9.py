"""12. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta görselleri (insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


def surec():
    ic = kutu(2, 2, 356, 140, GRI_A, GRI, 8)
    ic += yazi(180, 24, 'Talas, 751', 13.5, LAC)
    ic += kutu(16, 40, 120, 44, MAVI_A, MAVI, 8, 1) + yazi(76, 67, 'Abbasi ordusu', 12, MAVI)
    ic += kutu(224, 40, 120, 44, KIR_A, KIR, 8, 1) + yazi(284, 67, 'Çin ordusu', 12, KIR)
    ic += yazi(180, 67, '⚔', 18, SOLUK)
    ic += kutu(120, 100, 120, 32, TUR_A, TUR, 8, 1) + yazi(180, 121, 'Karluk Türkleri', 12, TUR)
    ic += yazi(180, 92, '?', 14, TUR)
    return svg(ic, 360, 144, 'Talas Savaşı: Abbasi ordusu, Çin ordusu ve Karluk Türkleri', 36)


def ribat():
    ic = kutu(2, 2, 356, 130, GRI_A, GRI, 8)
    ic += kutu(16, 14, 328, 104, '#fff', MOR, 8, 1)
    ic += yazi(180, 36, 'Kurum: ?', 13, MOR)
    for j, t in enumerate(['• Sınır boylarında kurulmuştur.', '• Önce güvenlik ve savunma amacı taşımıştır.', '• Zamanla eğitim, konaklama ve tasavvuf', '  merkezine dönüşmüştür.']):
        ic += yazi(34, 58 + j * 17, t, 11.5, LAC, 'start', True)
    return svg(ic, 360, 132, 'Özellikleri verilen kurum kartı', 34)


def levha():
    ic = kutu(2, 2, 356, 104, GRI_A, GRI, 8)
    ic += f'<rect x="54" y="16" width="252" height="76" rx="4" fill="#7a4b22"/>'
    ic += f'<rect x="62" y="24" width="236" height="60" rx="3" fill="#fff6e6"/>'
    ic += yazi(180, 46, 'Eline, beline, diline', 14, '#7a4b22')
    ic += yazi(180, 68, 'sahip ol.', 14, '#7a4b22')
    return svg(ic, 360, 108, 'Ahi esnafının dükkân levhası: Eline, beline, diline sahip ol', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = surec()
    s[4]['gorsel'] = ribat()
    s[9]['gorsel'] = levha()
