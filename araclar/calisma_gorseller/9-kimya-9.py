"""9. sınıf Kimya 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu, K150 EK).

viewBox genişliği 360 birim ≈ yarım sütun (≈88 mm); 12 birimlik yazı ≈ 8,5–9 pt.
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


def katman_modeli(proton, katmanlar, ad):
    """Solda katman modeli (çekirdek + elektron noktaları), sağda bilgi kartı."""
    cx, cy = 92, 78
    ic = kutu(2, 2, 356, 152, GRI_A, GRI, 8)
    ic += f'<circle cx="{cx}" cy="{cy}" r="17" fill="{KIR_A}" stroke="{KIR}" stroke-width="1"/>'
    ic += yazi(cx, cy + 4.5, f'{proton}p{us("+")}', 12, KIR)
    for k, adet in enumerate(katmanlar):
        r = 31 + k * 21
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GRI}" stroke-width="0.9"/>'
        for i in range(adet):
            a = -math.pi / 2 + 2 * math.pi * i / adet + (0.35 if k % 2 else 0)
            ic += f'<circle cx="{cx + r * math.cos(a):.1f}" cy="{cy + r * math.sin(a):.1f}" r="4" fill="{MAVI}"/>'
    ic += kutu(196, 26, 150, 104, '#fff', MAVI, 8)
    ic += yazi(271, 50, f'Nötr {ad} atomu', 13, MAVI)
    ic += f'<line x1="208" y1="60" x2="334" y2="60" stroke="{MAVI}" stroke-width="0.7"/>'
    ic += yazi(271, 84, f'Proton sayısı: {proton}', 12, LAC, ince=True)
    ic += yazi(271, 112, 'Dizilim: ' + ' - '.join(map(str, katmanlar)), 12, LAC, ince=True)
    return svg(ic, 360, 156, f'Nötr {ad} atomunun katman modeli', 40)


def tablo_kesiti():
    """2. ve 3. periyot, 1A–8A; X, Y, Z, T harfleri yerlerinde."""
    x0, y0, w, h = 52, 34, 38, 40
    ic = kutu(2, 2, 356, 128, GRI_A, GRI, 8)
    ic += yazi(22, 26, 'Periyot', 11, SOLUK, ince=True)
    gruplar = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A']
    harf = {(0, 0): ('X', MAVI, MAVI_A), (0, 6): ('Y', YES, YES_A), (1, 0): ('Z', TUR, TUR_A), (1, 5): ('T', MOR, MOR_A)}
    for j, g in enumerate(gruplar):
        ic += yazi(x0 + j * w + w / 2, y0 - 8, g, 12, LAC)
    for i, p in enumerate(('2', '3')):
        y = y0 + i * h
        ic += yazi(26, y + h / 2 + 5, p, 13, LAC)
        for j in range(8):
            x = x0 + j * w
            if (i, j) in harf:
                t, c, a = harf[(i, j)]
                ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{a}" stroke="{c}" stroke-width="1.2"/>'
                ic += yazi(x + w / 2, y + h / 2 + 6, t, 17, c)
            else:
                ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="{GRI}" stroke-width="0.8"/>'
    return svg(ic, 360, 132, 'Periyodik tablo kesitinde X, Y, Z ve T elementlerinin yerleri', 34)


def ie_grafik():
    veri = [('X', 520, MAVI), ('Y', 496, YES), ('Z', 419, TUR)]
    ic = kutu(2, 2, 356, 156, GRI_A, GRI, 8)
    ox, oy, olcek = 70, 128, 0.17   # 600 kJ/mol ≈ 102 birim
    ic += f'<line x1="{ox}" y1="{oy}" x2="340" y2="{oy}" stroke="{LAC}" stroke-width="1"/>'
    ic += f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="14" stroke="{LAC}" stroke-width="1"/>'
    for d in (200, 400, 600):
        y = oy - d * olcek
        ic += f'<line x1="{ox}" y1="{y:.1f}" x2="340" y2="{y:.1f}" stroke="{GRI}" stroke-width="0.5" stroke-dasharray="3 3"/>'
        ic += yazi(ox - 6, y + 4, str(d), 11, SOLUK, 'end', True)
    ic += f'<text transform="translate(22 72) rotate(-90)" text-anchor="middle" font-size="11" {INCE} fill="{SOLUK}">İE{alt("1")} (kJ/mol)</text>'
    for i, (ad, deger, renk) in enumerate(veri):
        x = 105 + i * 80
        yuk = deger * olcek
        ic += f'<rect x="{x}" y="{oy - yuk:.1f}" width="44" height="{yuk:.1f}" rx="3" fill="{renk}"/>'
        ic += yazi(x + 22, oy - yuk - 5, str(deger), 12, renk)
        ic += yazi(x + 22, oy + 17, ad, 13, LAC)
    return svg(ic, 360, 160, 'Aynı gruptaki X, Y ve Z elementlerinin birinci iyonlaşma enerjileri', 40)


def izoelektronik():
    kart = [('Ca', '2+', 20, MOR, MOR_A), ('Cl', '−', 17, YES, YES_A), ('K', '+', 19, TUR, TUR_A), ('S', '2−', 16, MAVI, MAVI_A)]
    ic = kutu(2, 2, 356, 104, GRI_A, GRI, 8)
    for i, (s, y, p, c, a) in enumerate(kart):
        x = 10 + i * 87
        ic += kutu(x, 10, 80, 88, a, c, 7)
        ic += yazi(x + 40, 36, f'{alt(p)}{s}{us(y)}', 15, c)
        ic += f'<line x1="{x + 10}" y1="46" x2="{x + 70}" y2="46" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 66, f'{p} proton', 12, LAC, ince=True)
        ic += yazi(x + 40, 86, '18 elektron', 12, LAC, ince=True)
    return svg(ic, 360, 108, 'Dört izoelektronik iyonun proton ve elektron sayıları', 28)


def en_grafik():
    veri = [('Li', 1.0), ('Be', 1.5), ('B', 2.0), ('C', 2.5), ('N', 3.0), ('O', 3.5), ('F', 4.0), ('Ne', None)]
    ic = kutu(2, 2, 356, 156, GRI_A, GRI, 8)
    ox, oy, olcek = 20, 122, 22
    ic += yazi(180, 20, 'Elektronegatiflik (2. periyot)', 12, MAVI)
    ic += f'<line x1="{ox}" y1="{oy}" x2="346" y2="{oy}" stroke="{LAC}" stroke-width="1"/>'
    for i, (s, d) in enumerate(veri):
        x = 26 + i * 40
        if d is None:
            ic += yazi(x + 15, oy - 22, 'değer', 11, SOLUK, ince=True)
            ic += yazi(x + 15, oy - 8, 'yok', 11, SOLUK, ince=True)
        else:
            yuk = d * olcek
            renk = MAVI if i < 6 else KIR
            ic += f'<rect x="{x}" y="{oy - yuk:.1f}" width="30" height="{yuk:.1f}" rx="3" fill="{renk}"/>'
            ic += yazi(x + 15, oy - yuk - 4, f'{d:.1f}'.replace('.', ','), 11.5, renk)
        ic += yazi(x + 15, oy + 17, s, 12.5, LAC)
    return svg(ic, 360, 160, 'İkinci periyot elementlerinin elektronegatiflik değerleri', 40)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = katman_modeli(12, [2, 8, 2], 'X')
    s[3]['gorsel'] = tablo_kesiti()
    s[4]['gorsel'] = ie_grafik()
    s[6]['gorsel'] = izoelektronik()
    s[7]['gorsel'] = en_grafik()
    s[11]['gorsel'] = katman_modeli(17, [2, 8, 7], 'X')
