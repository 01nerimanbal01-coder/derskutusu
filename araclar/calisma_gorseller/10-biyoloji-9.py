"""10. sınıf Biyoloji 9. hafta görselleri (SVG; insan figürü yok, organlar akış şemasıyla; görsel içi yazı ≈ gövde puntosu, K150 EK).

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



def f(formul, boy=None):
    """C2H6 → C₂H₆ (rakam harf/parantez ardındaysa alt simge)."""
    import re
    return re.sub(r'(?<=[A-Za-z)])(\d+)', lambda m: alt(m.group(1)), formul)


def ok(x1, y1, x2, y2, renk=LAC, kalin=1.4):
    a = math.atan2(y2 - y1, x2 - x1)
    u1 = (x2 - 7 * math.cos(a - 0.45), y2 - 7 * math.sin(a - 0.45))
    u2 = (x2 - 7 * math.cos(a + 0.45), y2 - 7 * math.sin(a + 0.45))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<polygon points="{x2},{y2} {u1[0]:.1f},{u1[1]:.1f} {u2[0]:.1f},{u2[1]:.1f}" fill="{renk}"/>')


def kanal():
    """Sindirim kanalı akış şeması: K → yutak → L → M → N → P → anüs (iki satır)."""
    ic = kutu(2, 2, 356, 124, GRI_A, GRI, 8)
    ust = [('K', MAVI, MAVI_A), ('yutak', GRI, '#fff'), ('L', TUR, TUR_A), ('M', YES, YES_A)]
    alt_ = [('N', MOR, MOR_A), ('P', KIR, KIR_A), ('anüs', GRI, '#fff')]
    for i, (ad, r, a) in enumerate(ust):
        x = 14 + i * 88
        ic += kutu(x, 18, 66, 36, a, r, 8, 1.3) + yazi(x + 33, 41, ad, 15 if len(ad) == 1 else 12, r if len(ad) == 1 else SOLUK, ince=len(ad) > 1)
        if i < 3:
            ic += ok(x + 68, 36, x + 86, 36)
    ic += f'<path d="M311 54 L311 70 L80 70 L80 80" fill="none" stroke="{LAC}" stroke-width="1.4"/>' + ok(80, 76, 80, 84)
    for i, (ad, r, a) in enumerate(alt_):
        x = 47 + i * 100
        ic += kutu(x, 84, 66, 34, a, r, 8, 1.3) + yazi(x + 33, 106, ad, 15 if len(ad) == 1 else 12, r if len(ad) == 1 else SOLUK, ince=len(ad) > 1)
        if i < 2:
            ic += ok(x + 68, 101, x + 98, 101)
    return svg(ic, 360, 128, 'Sindirim kanalının akış şeması; bazı yapılar harflerle gösterilmiş', 34)


def yardimci(cikarilmis=False):
    ic = kutu(2, 2, 356, 142, GRI_A, GRI, 8)
    x_ad = 'Karaciğer' if cikarilmis else 'X'
    y_ad = 'Safra kesesi' if cikarilmis else 'Y'
    z_ad = 'Pankreas' if cikarilmis else 'Z'
    ic += kutu(14, 14, 92, 34, MAVI_A, MAVI, 8, 1.3) + yazi(60, 36, x_ad, 13 if cikarilmis else 15, MAVI)
    ic += kutu(14, 70, 92, 34, YES_A, YES, 8, 1.3) + yazi(60, 92, y_ad, 12 if cikarilmis else 15, YES)
    ic += ok(60, 48, 60, 68, MAVI)
    ic += kutu(254, 14, 92, 34, TUR_A, TUR, 8, 1.3) + yazi(300, 36, z_ad, 13 if cikarilmis else 15, TUR)
    ic += kutu(120, 98, 120, 36, '#fff', LAC, 10, 1.5) + yazi(180, 115, 'onikiparmak', 11.5, LAC) + yazi(180, 128, 'bağırsağı', 11.5, LAC)
    ic += f'<path d="M106 87 L150 87 L150 96" fill="none" stroke="{YES}" stroke-width="1.4"/>' + ok(150, 92, 150, 98, YES)
    ic += yazi(112, 82, 'koledok', 11, SOLUK, 'start', True)
    ic += f'<path d="M300 48 L300 87 L210 87 L210 96" fill="none" stroke="{TUR}" stroke-width="1.4"/>' + ok(210, 92, 210, 98, TUR)
    ic += yazi(296, 70, 'Wirsung', 11, SOLUK, 'end', True)
    if cikarilmis:
        ic += f'<line x1="18" y1="72" x2="102" y2="102" stroke="{KIR}" stroke-width="2.4"/><line x1="18" y1="102" x2="102" y2="72" stroke="{KIR}" stroke-width="2.4"/>'
        ic += yazi(60, 122, 'ameliyatla alındı', 11, KIR, ince=True)
    return svg(ic, 360, 146, 'Karaciğer, safra kesesi ve pankreasın onikiparmak bağırsağına bağlantısı', 38)


def eksen(ox, oy, en, boy, xad, yad):
    ic = ok(ox, oy, ox + en, oy) + ok(ox, oy, ox, oy - boy)
    ic += yazi(ox + en, oy + 26, xad, 11.5, LAC, 'end', True) + yazi(ox + 6, oy - boy + 4, yad, 11.5, LAC, 'start', True)
    return ic


def ph_grafik():
    ic = kutu(2, 2, 356, 166, GRI_A, GRI, 8)
    ox, oy = 34, 132
    ic += eksen(ox, oy, 310, 112, 'pH', 'Enzim etkinliği')
    for p in range(0, 11, 2):
        x = ox + p * 29
        ic += f'<line x1="{x}" y1="{oy}" x2="{x}" y2="{oy + 4}" stroke="{LAC}"/>' + yazi(x, oy + 15, str(p), 11, LAC, ince=True)
    for tepe, renk, ad in ((2, KIR, 'I'), (6.8, MAVI, 'II'), (8, YES, 'III')):
        yol = ''
        for k in range(0, 61):
            p = tepe - 2 + k * 4 / 60
            x = ox + p * 29
            y = oy - 92 * math.exp(-((p - tepe) ** 2) / 0.9)
            yol += f'{"M" if k == 0 else "L"}{x:.1f} {y:.1f} '
        ic += f'<path d="{yol}" fill="none" stroke="{renk}" stroke-width="2"/>'
        ic += yazi(ox + tepe * 29 + (-24 if ad == 'II' else 24), oy - 80, ad, 13, renk)
    return svg(ic, 360, 170, 'Üç sindirim enziminin pH değerine göre etkinliği', 42)


def tupler():
    veri = [('1', '37 °C', 'pH 7', ''), ('2', '37 °C', 'pH 2', ''), ('3', '0 °C', 'pH 7', ''), ('4', '37 °C', 'pH 7', 'kaynatılmış enzim')]
    ic = kutu(2, 2, 356, 156, GRI_A, GRI, 8)
    ic += yazi(180, 20, 'Her tüpte: nişasta çözeltisi + tükürük amilazı (30 dk)', 11.5, LAC, ince=True)
    for i, (no, t, ph, ek) in enumerate(veri):
        x = 30 + i * 84
        ic += f'<path d="M{x} 34 L{x} 104 Q{x} 118 {x + 14} 118 Q{x + 28} 118 {x + 28} 104 L{x + 28} 34" fill="{MAVI_A}" stroke="{LAC}" stroke-width="1.3"/>'
        ic += yazi(x + 14, 80, no, 15, MAVI)
        ic += yazi(x + 14, 134, f'{t} · {ph}', 11, LAC, ince=True)
        if ek:
            ic += yazi(x + 14, 150, ek, 10.5, KIR, ince=True)
    return svg(ic, 360, 160, 'Farklı koşullardaki dört deney tüpü', 40)


def villus():
    ic = kutu(2, 2, 356, 140, GRI_A, GRI, 8)
    ic += f'<rect x="20" y="104" width="200" height="22" fill="{TUR_A}" stroke="{TUR}"/>'
    for i in range(4):
        x = 32 + i * 48
        ic += f'<path d="M{x} 104 L{x} 44 Q{x + 14} 22 {x + 28} 44 L{x + 28} 104" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.3"/>'
        ic += f'<path d="M{x + 9} 100 L{x + 9} 50 Q{x + 14} 42 {x + 19} 50 L{x + 19} 100" fill="none" stroke="{KIR}" stroke-width="1.1"/>'
        for k in range(7):
            yy = 50 + k * 8
            ic += f'<line x1="{x}" y1="{yy}" x2="{x - 4}" y2="{yy}" stroke="{TUR}" stroke-width="0.9"/><line x1="{x + 28}" y1="{yy}" x2="{x + 32}" y2="{yy}" stroke="{TUR}" stroke-width="0.9"/>'
    ic += ok(300, 40, 216, 40, LAC, 1) + yazi(306, 44, 'A yapısı', 12, LAC, 'start')
    ic += ok(300, 72, 182, 60, LAC, 1) + yazi(306, 76, 'kılcal', 11.5, KIR, 'start', True)
    ic += ok(300, 104, 222, 104, LAC, 1) + yazi(306, 108, 'bağırsak', 11.5, SOLUK, 'start', True) + yazi(306, 122, 'duvarı', 11.5, SOLUK, 'start', True)
    ic += yazi(120, 138, 'kıl gibi çıkıntılar: B', 11, SOLUK, ince=True)
    return svg(ic, 360, 144, 'İnce bağırsak iç yüzeyindeki çıkıntılar', 38)


def besin_grafik():
    ic = kutu(2, 2, 356, 166, GRI_A, GRI, 8)
    ox, oy = 34, 120
    ic += eksen(ox, oy, 314, 100, '', 'Sindirilmemiş miktar')
    organlar = ['Ağız', 'Yutak ve yemek b.', 'Mide', 'İnce bağırsak']
    sinir = [ox, ox + 70, ox + 140, ox + 210, ox + 300]
    for i, ad in enumerate(organlar):
        ic += f'<line x1="{sinir[i + 1]}" y1="{oy - 96}" x2="{sinir[i + 1]}" y2="{oy}" stroke="{GRI}" stroke-dasharray="3 3"/>'
        ic += yazi((sinir[i] + sinir[i + 1]) / 2, oy + 16 + (14 if i % 2 else 0), ad, 10.5, LAC, ince=True)
    cizgi = {'X': ([(ox, 36), (sinir[1], 70), (sinir[3], 70), (sinir[4] - 24, oy - 2)], MAVI),
             'Y': ([(ox, 42), (sinir[2], 42), (sinir[3], 82), (sinir[4] - 16, oy - 2)], TUR),
             'Z': ([(ox, 30), (sinir[3], 30), (sinir[4] - 8, oy - 2)], YES)}
    for ad, (nok, r) in cizgi.items():
        ic += f'<polyline points="{" ".join(f"{x},{y}" for x, y in nok)}" fill="none" stroke="{r}" stroke-width="2"/>'
    ic += f'<rect x="250" y="12" width="96" height="20" rx="4" fill="#fff"/>'
    for i, (ad, r) in enumerate((('X', MAVI), ('Y', TUR), ('Z', YES))):
        ic += f'<line x1="{256 + i * 32}" y1="22" x2="{270 + i * 32}" y2="22" stroke="{r}" stroke-width="2.4"/>' + yazi(276 + i * 32, 26, ad, 11.5, r, 'start')
    return svg(ic, 360, 170, 'Üç besinin sindirim kanalı boyunca sindirilmemiş miktarları', 42)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kanal()
    s[3]['gorsel'] = yardimci()
    s[5]['gorsel'] = ph_grafik()
    s[7]['gorsel'] = tupler()
    s[9]['gorsel'] = villus()
    s[10]['gorsel'] = yardimci(True)
    s[12]['gorsel'] = besin_grafik()
