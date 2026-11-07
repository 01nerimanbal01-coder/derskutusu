"""12. sınıf Türk Dili ve Edebiyatı 9. hafta görselleri (insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


def donemler():
    ic = kutu(2, 2, 356, 128, GRI_A, GRI, 8)
    veri = [('1923-1940', ['Millî Edebiyat', 'çizgisi'], MAVI, MAVI_A), ('1940-1960', ['Toplumcu', 'gerçekçi hikâye'], TUR, TUR_A), ('1960 sonrası', ['Modernist arayış,', 'küçürek hikâye'], MOR, MOR_A)]
    ic += f'<line x1="16" y1="34" x2="344" y2="34" stroke="{LAC}" stroke-width="1.4"/>'
    for i, (t, sat, r, ra) in enumerate(veri):
        x = 14 + i * 114
        ic += f'<circle cx="{x + 52}" cy="34" r="5" fill="{r}"/>' + yazi(x + 52, 22, t, 12, r)
        ic += kutu(x, 48, 104, 70, ra, r, 8, 1)
        for j, s in enumerate(sat):
            ic += yazi(x + 52, 78 + j * 18, s, 11.5, LAC, ince=j > 0)
    return svg(ic, 360, 132, 'Cumhuriyet Dönemi hikâyesinde eğilimler zaman çizelgesi', 34)


def form():
    ic = kutu(2, 2, 356, 138, GRI_A, GRI, 8)
    ic += kutu(14, 12, 332, 118, '#fff', MAVI, 8, 1)
    ic += yazi(180, 32, 'Canlandırma öz değerlendirme formu', 12.5, MAVI)
    for j, (k, p) in enumerate([('Diksiyon', 3), ('Vurgu ve tonlama', 3), ('Göz teması', 1), ('Jest ve mimik', 3)]):
        y = 56 + j * 20
        ic += yazi(34, y + 4, k, 12, LAC, 'start', True)
        for i in range(3):
            ic += f'<circle cx="{246 + i * 26}" cy="{y}" r="7" fill="{TUR if i < p else "#fff"}" stroke="{TUR}" stroke-width="1.2"/>'
    return svg(ic, 360, 142, 'Öz değerlendirme formu: diksiyon 3, tonlama 3, göz teması 1, jest-mimik 3 puan', 36)


def kucurek():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    ic += kutu(24, 12, 312, 92, '#fffdf5', TUR, 6, 1.2)
    ic += yazi(180, 34, 'Fincan', 13, TUR)
    for j, t in enumerate(['Kapıyı açtı. Kimse yoktu.', 'Masada iki fincan duruyordu;', 'biri hâlâ sıcaktı.']):
        ic += yazi(180, 56 + j * 18, t, 12, LAC, ince=True)
    return svg(ic, 360, 116, 'Küçürek hikâye metni', 30)


def uygula(o):
    s = o['sorular']
    s[4]['gorsel'] = donemler()
    s[8]['gorsel'] = form()
    s[11]['gorsel'] = kucurek()
