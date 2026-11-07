"""12. sınıf Kimya 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


def kap(x0, sol, sag, cozelti, kutup_sol, kutup_sag, ad=''):
    """x0'dan başlayan 150 birim genişliğinde elektroliz kabı; üstte üreteç bağlantı uçları."""
    ic = f'<path d="M{x0 + 10} 60 V150 H{x0 + 140} V60" fill="none" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<rect x="{x0 + 11}" y="78" width="128" height="71" fill="{MAVI_A}"/>'
    ic += yazi(x0 + 75, 143, cozelti, 11.5, MAVI)
    for x, et, k in ((x0 + 40, sol, kutup_sol), (x0 + 110, sag, kutup_sag)):
        ic += f'<rect x="{x - 6}" y="44" width="12" height="62" fill="{GRI}" stroke="{SOLUK}" stroke-width="0.8"/>'
        ic += yazi(x, 39, k, 16, KIR if k == '+' else (MAVI if k == '−' else SOLUK))
        ic += yazi(x, 122, et, 12, LAC)
    if ad:
        ic += yazi(x0 + 75, 168, ad, 12, LAC)
    return ic


def ureteç(x1, x2, y=16):
    ic = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{LAC}" stroke-width="1.2"/>'
    m = (x1 + x2) / 2
    ic += f'<rect x="{m - 22}" y="{y - 10}" width="44" height="20" fill="#fff" stroke="{LAC}"/>'
    ic += f'<line x1="{m - 4}" y1="{y - 7}" x2="{m - 4}" y2="{y + 7}" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="{m + 4}" y1="{y - 4}" x2="{m + 4}" y2="{y + 4}" stroke="{LAC}" stroke-width="2"/>'
    return ic


def tek_kap(sol, sag, cozelti, ks, kg, bilgi=None):
    ic = kutu(2, 2, 356, 166, GRI_A, GRI, 8)
    ic += ureteç(80, 150) + f'<line x1="80" y1="16" x2="80" y2="44" stroke="{LAC}"/><line x1="150" y1="16" x2="150" y2="44" stroke="{LAC}"/>'
    ic += kap(40, sol, sag, cozelti, ks, kg)
    if bilgi:
        ic += kutu(232, 58, 104, 64, '#fff', GRI, 8)
        for i, b in enumerate(bilgi):
            ic += yazi(284, 84 + i * 24, b, 13, LAC)
    return svg(ic, 360, 170, f'Elektroliz düzeneği: {cozelti}', 40)


def seri():
    ic = kutu(2, 2, 356, 176, GRI_A, GRI, 8)
    ic += kap(14, '', '', '{}'.format('AgNO₃(suda)'), '+', '−', 'I. kap')
    ic += kap(196, '', '', 'CuSO₄(suda)', '+', '−', 'II. kap')
    # bağlantılar: üreteç (+) → I anot; I katot → II anot; II katot → üreteç (−)
    ic += f'<line x1="54" y1="44" x2="54" y2="16" stroke="{LAC}"/><line x1="54" y1="16" x2="306" y2="16" stroke="{LAC}"/>'
    ic += f'<line x1="306" y1="16" x2="306" y2="44" stroke="{LAC}"/>'
    ic += ureteç(140, 220)
    ic += f'<path d="M124 44 V30 H236 V44" fill="none" stroke="{LAC}"/>'
    return svg(ic, 360, 180, 'Seri bağlı iki elektroliz kabı: AgNO3 ve CuSO4 çözeltileri', 42)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = tek_kap('X', 'Y', 'NaCl(s)', '+', '−')
    s[3]['gorsel'] = tek_kap('çatal', 'gümüş', 'AgNO₃(suda)', '?', '?')
    s[4]['gorsel'] = tek_kap('', '', 'AgNO₃(suda)', '+', '−', ['9,65 A', '1000 s'])
    s[6]['gorsel'] = seri()
    s[12]['gorsel'] = tek_kap('anot', 'katot', 'NaCl(s)', '+', '−', ['0,5 mol', 'Cl₂'])
