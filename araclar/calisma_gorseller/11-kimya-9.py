"""11. sınıf Kimya 9. hafta görselleri: tepkime hızını etkileyen faktörler (SVG; insan figürü yok)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def us(m):
    return f'<tspan baseline-shift="super" font-size="70%">{m}</tspan>'


def alt(m):
    return f'<tspan baseline-shift="sub" font-size="70%">{m}</tspan>'


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def ok(x1, y1, x2, y2, renk=LAC, k=1.4):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 9 * math.cos(a) + 4.5 * math.sin(a), y2 - 9 * math.sin(a) - 4.5 * math.cos(a))
    p2 = (x2 - 9 * math.cos(a) - 4.5 * math.sin(a), y2 - 9 * math.sin(a) + 4.5 * math.cos(a))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 7 * math.cos(a):.1f}" y2="{y2 - 7 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{k}"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{renk}"/>')


def tepkime_kartlari():
    kart = [('I', f'Ag{us("+")}(suda) + Cl{us("−")}(suda) → AgCl(k)', MAVI, MAVI_A),
            ('II', f'CH{alt("4")}(g) + 2O{alt("2")}(g) → CO{alt("2")}(g) + 2H{alt("2")}O(g)', TUR, TUR_A),
            ('III', f'5Fe{us("2+")}(suda) + MnO{alt("4")}{us("−")}(suda) + 8H{us("+")}(suda) → …', MOR, MOR_A)]
    ic = cerceve(360, 128)
    for i, (n, t, c, a) in enumerate(kart):
        y = 10 + i * 38
        ic += f'<rect x="10" y="{y}" width="340" height="32" rx="6" fill="{a}" stroke="{c}" stroke-width="1"/>'
        ic += yazi(30, y + 21, n, 13, c) + yazi(52, y + 21, t, 12.5, LAC, 'start')
    return svg(ic, 360, 128, 'Üç tepkime denklemi', 30)


def mb_egri(s, x0, y0, en, olcek):
    pts = []
    for i in range(0, 121):
        x = i / 120 * en
        y = (x * x) / (2 * s ** 3) * math.exp(-x / s)
        pts.append((x0 + x, y0 - y * olcek))
    return pts


def mb_grafik(sicaklik=True):
    en, boy, ox, oy = 360, 170, 40, 140
    ic = cerceve(en, boy) + ok(ox, oy, ox, 14) + ok(ox, oy, en - 12, oy)
    ic += yazi(ox + 8, 22, 'Tanecik sayısı', 12, LAC, 'start') + yazi(en - 14, oy + 20, 'Kinetik enerji', 12, LAC, 'end')
    if sicaklik:
        ea = 200
        e1, e2 = mb_egri(42, ox, oy, 300, 9000), mb_egri(66, ox, oy, 300, 9000)
        golge = [p for p in e2 if p[0] >= ox + ea]
        ic += '<polygon points="' + f'{ox + ea},{oy} ' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in golge) + f' {golge[-1][0]:.1f},{oy}" fill="{TUR_A}" stroke="none"/>'
        ic += '<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in e1) + f'" fill="none" stroke="{MAVI}" stroke-width="2.2"/>'
        ic += '<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in e2) + f'" fill="none" stroke="{KIR}" stroke-width="2.2"/>'
        ic += yazi(ox + 96, 36, f'T{alt("1")}', 13, MAVI) + yazi(ox + 160, 82, f'T{alt("2")}', 13, KIR)
        ic += f'<line x1="{ox + ea}" y1="{oy}" x2="{ox + ea}" y2="40" stroke="{LAC}" stroke-width="1.3" stroke-dasharray="5 3"/>'
        ic += yazi(ox + ea, 34, f'E{alt("a")}', 13)
    else:
        e1 = mb_egri(50, ox, oy, 300, 10000)
        ic += '<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in e1) + f'" fill="none" stroke="{MAVI}" stroke-width="2.2"/>'
        for x, n, r in ((215, '1', LAC), (140, '2', YES)):
            ic += f'<line x1="{ox + x}" y1="{oy}" x2="{ox + x}" y2="40" stroke="{r}" stroke-width="1.3" stroke-dasharray="5 3"/>'
            ic += yazi(ox + x, 34, f'E{alt("a" + n)}', 13, r)
        ic += ok(ox + 205, 52, ox + 152, 52, YES, 1.6)
        ic += yazi(ox + 268, 60, 'T sabit', 12, SOLUK, ince=True)
    return svg(ic, en, boy, 'Tanecik sayısı–kinetik enerji dağılım grafiği', 36)


def pe_grafik():
    en, boy, ox, oy = 360, 190, 54, 168
    Y = lambda v: oy - v * 1.2
    ic = cerceve(en, boy) + ok(ox, oy, ox, 12) + ok(ox, oy, en - 12, oy)
    ic += yazi(ox + 8, 20, 'Potansiyel enerji (kJ)', 12, LAC, 'start') + yazi(en - 14, oy + 16, 'Tepkime koordinatı', 11.5, LAC, 'end')

    def yol(tepe):
        return (f'M {ox} {Y(40)} L {ox + 40} {Y(40)} C {ox + 80} {Y(40)}, {ox + 100} {Y(tepe)}, {ox + 140} {Y(tepe)} '
                f'C {ox + 180} {Y(tepe)}, {ox + 200} {Y(10)}, {ox + 240} {Y(10)} L {ox + 290} {Y(10)}')
    ic += f'<path d="{yol(120)}" fill="none" stroke="{MAVI}" stroke-width="2.4"/>'
    ic += f'<path d="{yol(80)}" fill="none" stroke="{YES}" stroke-width="2.2" stroke-dasharray="6 4"/>'
    for v in (10, 40, 80, 120):
        ic += f'<line x1="{ox}" y1="{Y(v):.1f}" x2="{ox + 290}" y2="{Y(v):.1f}" stroke="{GRI}" stroke-width="0.7" stroke-dasharray="3 3"/>'
        ic += yazi(ox - 6, Y(v) + 4.5, str(v), 12, LAC, 'end')
    ic += yazi(ox + 6, Y(40) - 7, 'Tepkenler', 11.5, SOLUK, 'start', True) + yazi(ox + 266, Y(10) - 7, 'Ürünler', 11.5, SOLUK, ince=True)
    ic += f'<line x1="{ox + 200}" y1="40" x2="{ox + 222}" y2="40" stroke="{MAVI}" stroke-width="2.4"/>' + yazi(ox + 228, 44.5, 'katalizörsüz', 11.5, MAVI, 'start')
    ic += f'<line x1="{ox + 200}" y1="60" x2="{ox + 222}" y2="60" stroke="{YES}" stroke-width="2.2" stroke-dasharray="6 4"/>' + yazi(ox + 228, 64.5, 'katalizörlü', 11.5, YES, 'start')
    return svg(ic, en, boy, 'Katalizörlü ve katalizörsüz potansiyel enerji grafiği', 38)


def erlen(x, renk_toz, toz):
    ic = f'<path d="M {x - 14} 30 L {x - 14} 62 L {x - 46} 128 Q {x - 48} 134 {x - 40} 134 L {x + 40} 134 Q {x + 48} 134 {x + 46} 128 L {x + 14} 62 L {x + 14} 30 Z" fill="#fff" stroke="{LAC}" stroke-width="1.5"/>'
    ic += f'<path d="M {x - 30} 96 L {x - 46} 128 Q {x - 48} 134 {x - 40} 134 L {x + 40} 134 Q {x + 48} 134 {x + 46} 128 L {x + 30} 96 Z" fill="{MAVI_A}" stroke="none"/>'
    if toz:
        import random
        r = random.Random(7)
        for _ in range(60):
            ic += f'<circle cx="{x - 30 + r.random() * 60:.1f}" cy="{126 + r.random() * 6:.1f}" r="1.3" fill="{renk_toz}"/>'
    else:
        ic += f'<rect x="{x - 12}" y="116" width="24" height="16" rx="3" fill="{renk_toz}"/>'
    for i in range(3):
        ic += f'<circle cx="{x - 8 + i * 8}" cy="{104 - i * 6}" r="2.6" fill="none" stroke="{MAVI}" stroke-width="1"/>'
    return ic


def deney():
    ic = cerceve(360, 176)
    ic += erlen(95, GRI, False) + erlen(265, GRI, True)
    ic += yazi(95, 22, 'I', 14, MAVI) + yazi(265, 22, 'II', 14, MAVI)
    ic += yazi(95, 156, '5 g parça Zn', 12, LAC, ince=True) + yazi(265, 156, '5 g toz Zn', 12, LAC, ince=True)
    ic += yazi(180, 170, '100 mL 1 M HCl · 25 °C', 11.5, SOLUK, ince=True)
    return svg(ic, 360, 176, 'Parça ve toz çinko ile aynı asit çözeltisi', 36)


def tanecik():
    ic = cerceve(360, 130)
    import random
    for k, (x, n, ad) in enumerate(((30, 5, 'I'), (200, 10, 'II'))):
        ic += f'<rect x="{x}" y="22" width="130" height="80" rx="4" fill="#fff" stroke="{LAC}" stroke-width="1.4"/>'
        ic += yazi(x + 65, 17, ad, 13, MAVI)
        r = random.Random(3 + k)
        hucre = r.sample(range(15), n)
        for i, h in enumerate(hucre):
            cx, cy = x + 16 + (h % 5) * 24.5 + r.uniform(-4, 4), 36 + (h // 5) * 26 + r.uniform(-4, 4)
            ic += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{KIR if i % 2 else MAVI}"/>'
    ic += yazi(180, 120, 'Aynı hacim ve aynı sıcaklık', 11.5, SOLUK, ince=True)
    return svg(ic, 360, 130, 'Aynı hacimde farklı sayıda tanecik', 30)


def uc_deney():
    veri = [('I', 'parça', '1 M', '20 °C', MAVI, MAVI_A), ('II', 'toz', '1 M', '40 °C', TUR, TUR_A), ('III', 'toz', '0,5 M', '20 °C', MOR, MOR_A)]
    ic = cerceve(360, 120)
    for i, (n, hal, der, t, c, a) in enumerate(veri):
        x = 10 + i * 116
        ic += f'<rect x="{x}" y="10" width="108" height="100" rx="7" fill="{a}" stroke="{c}" stroke-width="1"/>'
        ic += yazi(x + 54, 32, n, 14, c) + f'<line x1="{x + 12}" y1="42" x2="{x + 96}" y2="42" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 62, f'CaCO{alt("3")}: {hal}', 12, LAC, ince=True)
        ic += yazi(x + 54, 82, f'HCl: {der}', 12, LAC, ince=True) + yazi(x + 54, 101, t, 12, LAC, ince=True)
    return svg(ic, 360, 120, 'Üç deneyin koşulları', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = tepkime_kartlari()
    s[2]['gorsel'] = mb_grafik(True)
    s[3]['gorsel'] = pe_grafik()
    s[5]['gorsel'] = deney()
    s[8]['gorsel'] = mb_grafik(False)
    s[10]['gorsel'] = tanecik()
    s[12]['gorsel'] = uc_deney()
