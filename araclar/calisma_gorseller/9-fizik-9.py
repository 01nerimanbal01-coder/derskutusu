"""9. sınıf Fizik 9. hafta görselleri (SVG; birim kareli düzlem, vektör okları; insan figürü yok; yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12–13 birimlik yazı ≈ 8,5–9 pt.
"""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
GRI, GRI_A, SOLUK, IZGARA = '#9aa6bd', '#f3f5f9', '#5b6479', '#d5dbe7'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, boy, etiket, mm):
    return (f'<svg viewBox="0 0 360 {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def alt(m):
    return f'<tspan baseline-shift="sub" font-size="70%">{m}</tspan>'


def ok(x1, y1, x2, y2, renk, kalin=2.4, kesik=False):
    """Uçta dolu üçgen başlı ok (işaretçi kullanılmaz: aynı sayfadaki SVG'lerde kimlik çakışmasın)."""
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - 10 * math.cos(a), y2 - 10 * math.sin(a)
    sol = (bx + 4.5 * math.sin(a), by - 4.5 * math.cos(a))
    sag = (bx - 4.5 * math.sin(a), by + 4.5 * math.cos(a))
    cizgi = ' stroke-dasharray="5 4"' if kesik else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{renk}" stroke-width="{kalin}"{cizgi}/>'
            f'<polygon points="{x2:.1f},{y2:.1f} {sol[0]:.1f},{sol[1]:.1f} {sag[0]:.1f},{sag[1]:.1f}" fill="{renk}"/>')


def izgara(xmin, xmax, ymin, ymax, vektorler, etiket, hucre=22, eksen_adi=True, cisim=False, ust=8):
    """Birim kareli düzlem; vektörler: (x1, y1, x2, y2, ad, renk, etiket_dx, etiket_dy) düzlem biriminde."""
    w = (xmax - xmin) * hucre
    ox = (360 - w) / 2 - xmin * hucre
    oy = ust + ymax * hucre
    boy = ust + (ymax - ymin) * hucre + 10
    P = lambda x, y: (ox + x * hucre, oy - y * hucre)
    ic = f'<rect x="1" y="1" width="358" height="{boy - 2}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'
    for i in range(xmin, xmax + 1):
        x, _ = P(i, 0)
        ic += f'<line x1="{x}" y1="{P(0, ymax)[1]}" x2="{x}" y2="{P(0, ymin)[1]}" stroke="{IZGARA}" stroke-width="0.8"/>'
    for j in range(ymin, ymax + 1):
        _, y = P(0, j)
        ic += f'<line x1="{P(xmin, 0)[0]}" y1="{y}" x2="{P(xmax, 0)[0]}" y2="{y}" stroke="{IZGARA}" stroke-width="0.8"/>'
    ic += ok(*P(xmin, 0), *P(xmax, 0), SOLUK, 1.1)
    ic += ok(*P(0, ymin), *P(0, ymax), SOLUK, 1.1)
    if eksen_adi:
        ic += yazi(P(xmax, 0)[0] - 4, P(xmax, 0)[1] + 16, '+x', 12, SOLUK, ince=True)
        ic += yazi(P(0, ymax)[0] + 16, P(0, ymax)[1] + 12, '+y', 12, SOLUK, ince=True)
    if cisim:
        ic += f'<rect x="{ox - 9}" y="{oy - 9}" width="18" height="18" rx="2" fill="{GRI}" stroke="{LAC}" stroke-width="0.8"/>'
    else:
        ic += f'<circle cx="{ox}" cy="{oy}" r="3" fill="{LAC}"/>'
    for x1, y1, x2, y2, ad, renk, dx, dy in vektorler:
        ic += ok(*P(x1, y1), *P(x2, y2), renk)
        lx, ly = P((x1 + x2) / 2, (y1 + y2) / 2)
        ic += yazi(lx + dx, ly + dy, ad, 14, renk)
    return svg(ic, boy, etiket, round(boy * 88 / 360) + 1)


def aci_53():
    ox, oy, L = 70, 150, 120
    a = math.radians(53)
    ex, ey = ox + L * math.cos(a), oy - L * math.sin(a)
    ic = f'<rect x="1" y="1" width="358" height="170" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'
    ic += ok(ox - 20, oy, 200, oy, SOLUK, 1.1) + ok(ox, oy + 12, ox, 14, SOLUK, 1.1)
    ic += yazi(196, oy + 16, '+x', 12, SOLUK, ince=True) + yazi(ox + 16, 24, '+y', 12, SOLUK, ince=True)
    ic += f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{ex:.1f}" y2="{oy}" stroke="{GRI}" stroke-width="1" stroke-dasharray="4 3"/>'
    ic += f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{ox}" y2="{ey:.1f}" stroke="{GRI}" stroke-width="1" stroke-dasharray="4 3"/>'
    ic += ok(ox, oy, ex, ey, MAVI, 2.6)
    ic += f'<path d="M {ox + 32} {oy} A 32 32 0 0 0 {ox + 32 * math.cos(a):.1f} {oy - 32 * math.sin(a):.1f}" fill="none" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(ox + 48, oy - 12, '53°', 12.5, TUR)
    ic += yazi(ox + 30, oy - 76, 'F = 15 N', 13.5, MAVI, 'end')
    ic += f'<rect x="222" y="54" width="126" height="64" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(285, 80, 'sin 53° = 0,8', 12.5, LAC, ince=True)
    ic += yazi(285, 104, 'cos 53° = 0,6', 12.5, LAC, ince=True)
    return svg(ic, 172, 'Yatayla 53 derece açı yapan 15 newtonluk F kuvveti', 43)


def uc_kuvvet():
    ox, oy, L = 130, 104, 70
    ic = f'<rect x="1" y="1" width="358" height="190" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'
    renk = [MAVI, YES, KIR]
    for i, aci in enumerate((90, 210, 330)):
        a = math.radians(aci)
        ex, ey = ox + L * math.cos(a), oy - L * math.sin(a)
        ic += ok(ox, oy, ex, ey, renk[i], 2.4)
        ic += yazi(ex + 16 * math.cos(a), ey - 16 * math.sin(a) + 5, f'F{alt(i + 1)}', 13.5, renk[i])
    for aci in (150, 270, 30):
        a = math.radians(aci)
        ic += yazi(ox + 34 * math.cos(a), oy - 34 * math.sin(a) + 5, '120°', 11.5, TUR)
    ic += f'<circle cx="{ox}" cy="{oy}" r="4" fill="{LAC}"/>'
    ic += f'<rect x="236" y="60" width="112" height="62" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(292, 86, f'F{alt(1)} = F{alt(2)} = F{alt(3)}', 12.5, LAC, ince=True)
    ic += yazi(292, 108, '= 10 N', 12.5, LAC, ince=True)
    return svg(ic, 192, 'Aralarındaki açılar 120 derece olan eşit büyüklükte üç kuvvet', 46)


def aci_37_duseyle():
    ox, oy, L = 90, 158, 125
    a = math.radians(90 - 37)
    ex, ey = ox + L * math.cos(a), oy - L * math.sin(a)
    ic = f'<rect x="1" y="1" width="358" height="176" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'
    ic += ok(ox - 20, oy, 210, oy, SOLUK, 1.1) + ok(ox, oy + 12, ox, 14, SOLUK, 1.1)
    ic += yazi(206, oy + 16, '+x', 12, SOLUK, ince=True) + yazi(ox - 16, 24, '+y', 12, SOLUK, ince=True)
    ic += f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{ex:.1f}" y2="{oy}" stroke="{GRI}" stroke-width="1" stroke-dasharray="4 3"/>'
    ic += f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{ox}" y2="{ey:.1f}" stroke="{GRI}" stroke-width="1" stroke-dasharray="4 3"/>'
    ic += ok(ox, oy, ex, ey, MAVI, 2.6)
    ic += f'<path d="M {ox} {oy - 40} A 40 40 0 0 1 {ox + 40 * math.cos(a):.1f} {oy - 40 * math.sin(a):.1f}" fill="none" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(ox + 13, oy - 50, '37°', 12.5, TUR)
    ic += yazi(ex + 8, ey + 40, 'T = 50 N', 13.5, MAVI, 'start')
    ic += f'<rect x="232" y="54" width="118" height="64" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(291, 80, 'sin 37° = 0,6', 12.5, LAC, ince=True)
    ic += yazi(291, 104, 'cos 37° = 0,8', 12.5, LAC, ince=True)
    return svg(ic, 178, 'Düşeyle 37 derece açı yapan 50 newtonluk T kuvveti', 44)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = izgara(-1, 6, -1, 4, [(0, 0, 4, 3, 'A', MAVI, -10, -8)], 'Kareli düzlemde A vektörü')
    s[1]['gorsel'] = izgara(-3, 5, -5, 4, [(0, 0, 3, 2, 'K', MAVI, 4, -10), (0, 0, -1, 3, 'L', YES, -14, 0),
                                           (0, 0, 2, -4, 'M', KIR, 14, 4)], 'Kareli düzlemde K, L ve M vektörleri', hucre=20)
    s[2]['gorsel'] = izgara(-3, 7, -1, 3, [(0, 0, 6, 2, f'F{alt(1)}', MAVI, 0, -10), (0, 0, -2, 1, f'F{alt(2)}', KIR, 0, -10)],
                            'Cisme etki eden iki kuvvet', hucre=26, cisim=True)
    s[4]['gorsel'] = aci_53()
    s[5]['gorsel'] = izgara(-1, 5, -1, 4, [(0, 0, 3, 1, 'A', MAVI, 6, 14), (0, 0, 1, 3, 'B', YES, -20, 4)],
                            'Kareli düzlemde A ve B vektörleri')
    s[6]['gorsel'] = izgara(-4, 4, -1, 1, [(0, 0, 2, 0, 'A', MAVI, 6, 20)], 'Artı x yönünde 2 birimlik A vektörü', hucre=26, ust=6)
    s[8]['gorsel'] = uc_kuvvet()
    s[9]['gorsel'] = izgara(-5, 5, -4, 4, [(0, 0, 2, 3, 'K', MAVI, -10, -4), (0, 0, -4, 1, 'L', YES, 0, -10),
                                           (0, 0, 1, -3, 'M', KIR, 12, 2), (0, 0, 3, -2, 'N', MOR, 6, -10)],
                            'Kareli düzlemde K, L, M ve N vektörleri', hucre=20)
    s[13]['gorsel'] = aci_37_duseyle()
