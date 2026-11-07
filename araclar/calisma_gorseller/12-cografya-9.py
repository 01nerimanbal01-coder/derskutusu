"""12. sınıf Coğrafya 9. hafta görselleri (şematik, ölçeksiz; insan figürü yok; görsel içi yazı ≈ gövde puntosu)."""
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


DENIZ, KARA = '#d6e6fb', '#f4ecd9'


def bogazlar():
    ic = kutu(2, 2, 356, 176, KARA, GRI, 8)
    ic += f'<ellipse cx="210" cy="48" rx="88" ry="28" fill="{DENIZ}" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(210, 52, 'KARADENİZ', 13, MAVI)
    ic += f'<ellipse cx="118" cy="116" rx="34" ry="12" fill="{DENIZ}" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(118, 120, 'Marmara', 11, MAVI, ince=True)
    ic += f'<path d="M2 156 Q50 148 80 164 L80 178 L2 178 Z" fill="{DENIZ}" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(34, 172, 'Ege', 11, MAVI, ince=True)
    ic += f'<path d="M134 106 L146 72" stroke="{MAVI}" stroke-width="4"/>'
    ic += f'<path d="M88 124 L66 156" stroke="{MAVI}" stroke-width="4"/>'
    ic += yazi(150, 96, 'İstanbul Boğazı', 11, KIR, 'start')
    ic += yazi(34, 128, 'Çanakkale', 11, KIR) + yazi(34, 141, 'Boğazı', 11, KIR)
    for x, y, ad, h in [(190, 14, 'Ukrayna', 'middle'), (346, 30, 'Rusya', 'end'), (352, 66, 'Gürcistan', 'end'), (116, 40, 'Romanya', 'end'), (116, 74, 'Bulgaristan', 'end')]:
        ic += yazi(x, y, ad, 11, LAC, h, True)
    ic += yazi(250, 150, 'TÜRKİYE', 13, LAC)
    return svg(ic, 360, 180, 'Karadeniz, Türk Boğazları ve Karadeniz kıyısındaki ülkeler (şematik)', 42)


def ucus():
    ic = kutu(2, 2, 356, 160, GRI_A, GRI, 8)
    cx, cy = 180, 82
    ic += f'<circle cx="{cx}" cy="{cy}" r="70" fill="{MAVI_A}" stroke="{MAVI}" stroke-dasharray="5 4"/>'
    ic += kutu(cx - 40, cy - 14, 80, 28, LAC, LAC, 14) + yazi(cx, cy + 5, 'Türkiye', 12.5, '#fff')
    for a, ad in [(-130, 'Avrupa'), (-20, 'Asya'), (110, 'Afrika')]:
        r = math.radians(a)
        x, y = cx + 70 * math.cos(r), cy + 70 * math.sin(r)
        ic += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{TUR}"/>'
        if ad == 'Afrika':
            ic += yazi(x - 10, y + 5, ad, 12, TUR, 'end')
        else:
            ic += yazi(x + (-10 if math.cos(r) < 0 else 10), y - 8, ad, 12, TUR, 'end' if math.cos(r) < 0 else 'start')
    ic += yazi(cx, cy - 30, '≈ 4 saatlik uçuş', 12, MAVI)
    ic += yazi(cx, cy + 36, '60’tan fazla ülke', 11, MAVI, ince=True)
    return svg(ic, 360, 164, 'Türkiye merkezli dört saatlik uçuş halkası', 40)


def havalimani():
    ic = kutu(2, 2, 356, 140, GRI_A, GRI, 8)
    ic += yazi(180, 22, 'Türkiye’de hizmet veren havalimanı sayısı', 12, MAVI)
    oy = 112
    ic += f'<line x1="40" y1="{oy}" x2="320" y2="{oy}" stroke="{LAC}"/>'
    for x, v, et, alt_ in [(90, 26, '26', '2000’lerin başı'), (230, 57, '57+', 'Günümüz')]:
        h = v * 1.25
        ic += f'<rect x="{x}" y="{oy - h}" width="44" height="{h}" rx="3" fill="{MAVI}"/>'
        ic += yazi(x + 22, oy - h - 5, et, 13, MAVI) + yazi(x + 22, oy + 18, alt_, 11.5, LAC, ince=True)
    return svg(ic, 360, 142, 'Havalimanı sayısı 2000’lerin başında 26, günümüzde 57’nin üzerinde', 34)


def tanap():
    ic = kutu(2, 2, 356, 132, GRI_A, GRI, 8)
    ic += f'<path d="M40 50 Q60 34 120 40 Q200 30 280 38 Q330 44 340 60 Q330 96 280 104 Q200 112 120 104 Q60 100 40 86 Z" fill="{KARA}" stroke="{SOLUK}" stroke-width="0.9"/>'
    ic += yazi(190, 124, 'Türkiye (şematik)', 11, SOLUK, ince=True)
    pts = [(326, 52), (280, 62), (220, 66), (160, 62), (100, 66), (46, 58)]
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    ic += f'<path d="{d}" fill="none" stroke="{TUR}" stroke-width="3"/>'
    ic += f'<circle cx="326" cy="52" r="4" fill="{KIR}"/><circle cx="46" cy="58" r="4" fill="{KIR}"/>'
    ic += yazi(326, 30, 'Ardahan', 11, LAC, 'middle', True) + yazi(48, 30, 'Edirne', 11, LAC, 'middle', True)
    ic += ok(36, 58, 10, 58, TUR, 1.5) + yazi(18, 78, 'Avrupa', 10.5, TUR)
    ic += ok(352, 46, 334, 50, TUR, 1.5)
    ic += yazi(190, 90, 'Azerbaycan doğal gazı', 12, TUR)
    return svg(ic, 360, 136, 'Doğudan batıya Türkiye’yi geçen doğal gaz boru hattı (şematik)', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bogazlar()
    s[3]['gorsel'] = ucus()
    s[6]['gorsel'] = havalimani()
    s[9]['gorsel'] = tanap()
