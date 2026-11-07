"""12. sınıf Matematik 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


def terim_seridi(degerler, baslik, etiket):
    n = len(degerler); w = 340 / n
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8) + yazi(180, 22, baslik, 12.5, MAVI)
    for i, d in enumerate(degerler):
        x = 10 + i * w
        bos = d == '?'
        ic += kutu(x + 3, 40, w - 6, 34, '#fff' if bos else MAVI_A, GRI if bos else MAVI, 6, 1)
        ic += yazi(x + w / 2, 62, d, 14, SOLUK if bos else MAVI)
        ic += yazi(x + w / 2, 90, f'a{alt(i + 1)}', 12.5, LAC, ince=True)
    return svg(ic, 360, 100, etiket, 28)


def fibonacci_kareler():
    u = 16; x0, y0 = 72, 18
    kareler = [(0, 0, 8, MAVI_A, MAVI), (8, 0, 5, YES_A, YES), (10, 5, 3, TUR_A, TUR),
               (8, 6, 2, MOR_A, MOR), (8, 5, 1, KIR_A, KIR), (9, 5, 1, KIR_A, KIR)]
    ic = kutu(2, 2, 356, 164, GRI_A, GRI, 8)
    for x, y, k, d, c in kareler:
        ic += f'<rect x="{x0 + x * u}" y="{y0 + y * u}" width="{k * u}" height="{k * u}" fill="{d}" stroke="{c}" stroke-width="1.4"/>'
        if k > 1:
            ic += yazi(x0 + (x + k / 2) * u, y0 + (y + k / 2) * u + 5, str(k), 13 if k > 2 else 11, c)
        else:
            ic += yazi(x0 + (x + 0.5) * u, y0 + (y + 0.5) * u + 4, '1', 10, c)
    return svg(ic, 360, 168, 'Kenarları 1, 1, 2, 3, 5 ve 8 birim olan karelerden oluşan dikdörtgen', 40)


def top_zipla():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    zemin = 132
    ic += f'<line x1="12" y1="{zemin}" x2="348" y2="{zemin}" stroke="{LAC}" stroke-width="1.4"/>'
    yuk = [81, 54, 36, 24, 16]
    etiket = ['81 cm', '54 cm', '?', '?', '?']
    x = 30; olc = 1.25
    ic += f'<line x1="{x}" y1="{zemin}" x2="{x}" y2="{zemin - yuk[0] * olc}" stroke="{SOLUK}" stroke-dasharray="3 3"/>'
    ic += f'<circle cx="{x}" cy="{zemin - yuk[0] * olc - 6}" r="6" fill="{TUR}"/>'
    ic += yazi(x + 12, zemin - yuk[0] * olc, etiket[0], 12, LAC, 'start')
    gen = [98, 82, 68, 58]
    for i in range(1, 5):
        h = yuk[i] * olc; w = gen[i - 1]
        ic += f'<path d="M{x} {zemin} Q{x + w / 2} {zemin - 2 * h} {x + w} {zemin}" fill="none" stroke="{MAVI}" stroke-width="1.4"/>'
        tx = x + w / 2
        ic += f'<line x1="{tx}" y1="{zemin}" x2="{tx}" y2="{zemin - h}" stroke="{SOLUK}" stroke-dasharray="3 3"/>'
        ic += yazi(tx, zemin - h - 5, etiket[i], 12, LAC)
        ic += yazi(tx, zemin + 14, f'{i}. zıp.', 10.5, SOLUK, ince=True)
        x += w
    return svg(ic, 360, 154, 'Her zıplayışta yüksekliği azalan topun izlediği yol', 38)


def nufus():
    ic = kutu(2, 2, 356, 110, GRI_A, GRI, 8)
    for i, (a, d) in enumerate([('Bugün', '200 000'), ('1 yıl sonra', '?'), ('2 yıl sonra', '?')]):
        x = 16 + i * 120
        ic += kutu(x, 36, 92, 40, MAVI_A if i == 0 else '#fff', MAVI if i == 0 else GRI, 8, 1)
        ic += yazi(x + 46, 62, d, 14, MAVI if i == 0 else SOLUK)
        ic += yazi(x + 46, 98, a, 12, LAC, ince=True)
        if i < 2:
            ic += ok(x + 95, 56, x + 117, 56, TUR, 1.4) + yazi(x + 106, 30, '%10 artış', 10.5, TUR)
    return svg(ic, 360, 114, 'Nüfusun yıllara göre değişimi', 30)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = terim_seridi(['?', '6', '?', '?', '48', '?'], 'Pozitif terimli geometrik dizi', 'Geometrik dizinin ikinci terimi 6, beşinci terimi 48')
    s[3]['gorsel'] = fibonacci_kareler()
    s[4]['gorsel'] = cubuk([(f'{i}. gün', v, str(v) if i < 3 else '?') for i, v in enumerate([3, 6, 12, 24, 48, 96], 1)],
                           'Duyurunun gönderildiği yeni kişi sayısı', 'Günlere göre duyurunun gönderildiği kişi sayısı grafiği')
    s[7]['gorsel'] = top_zipla()
    s[11]['gorsel'] = nufus()
    s[12]['gorsel'] = terim_seridi(['4', '?', '?', '?', '324'], '5 terimli pozitif geometrik dizi', 'Birinci terimi 4, beşinci terimi 324 olan dizi')
