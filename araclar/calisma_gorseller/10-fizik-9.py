"""10. sınıf Fizik 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu, K150 EK).

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


def ok(x1, y1, x2, y2, renk=KIR, kalin=2):
    a = math.atan2(y2 - y1, x2 - x1)
    u1 = (x2 - 9 * math.cos(a - 0.4), y2 - 9 * math.sin(a - 0.4))
    u2 = (x2 - 9 * math.cos(a + 0.4), y2 - 9 * math.sin(a + 0.4))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 6 * math.cos(a):.1f}" y2="{y2 - 6 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<polygon points="{x2},{y2} {u1[0]:.1f},{u1[1]:.1f} {u2[0]:.1f},{u2[1]:.1f}" fill="{renk}"/>')


def zemin(x1, x2, y, tarali=False):
    ic = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{LAC}" stroke-width="1.5"/>'
    if tarali:
        for x in range(int(x1) + 4, int(x2), 10):
            ic += f'<line x1="{x}" y1="{y}" x2="{x - 7}" y2="{y + 7}" stroke="{SOLUK}" stroke-width="0.8"/>'
    return ic


def iki_arac():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    ic += zemin(16, 344, 92)
    for x, ad, m, v, renk, acik, w in ((28, 'K', 'm', '2v', MAVI, MAVI_A, 60), (196, 'L', '2m', 'v', TUR, TUR_A, 80)):
        ic += kutu(x, 92 - 44, w, 44, acik, renk, 5, 1.4)
        ic += yazi(x + w / 2, 75, ad, 15, renk)
        ic += ok(x + w + 6, 70, x + w + 54, 70, renk)
        ic += yazi(x + w + 30, 60, v, 12.5, renk)
        ic += yazi(x + w / 2, 40, f'kütle: {m}', 12, LAC, ince=True)
    ic += yazi(180, 108, 'Sürtünmesiz yatay yol', 11, SOLUK, ince=True)
    return svg(ic, 360, 116, 'K ve L araçlarının kütleleri ve süratleri', 30)


def masa_kutu():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += zemin(16, 344, 138, True)
    ic += f'<rect x="90" y="84" width="170" height="8" fill="{SOLUK}"/>'
    ic += f'<rect x="100" y="92" width="8" height="46" fill="{SOLUK}"/><rect x="242" y="92" width="8" height="46" fill="{SOLUK}"/>'
    ic += kutu(140, 40, 60, 44, MAVI_A, MAVI, 2, 1.4) + yazi(170, 67, '2 kg', 12.5, MAVI)
    for x, y1, y2, t in ((62, 92, 138, '0,8 m'), (226, 40, 84, '0,4 m')):
        ic += f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{TUR}" stroke-width="1"/>'
        ic += f'<line x1="{x - 5}" y1="{y1}" x2="{x + 5}" y2="{y1}" stroke="{TUR}"/><line x1="{x - 5}" y1="{y2}" x2="{x + 5}" y2="{y2}" stroke="{TUR}"/>'
        ic += yazi(x + (-8 if x < 100 else 10), (y1 + y2) / 2 + 4, t, 12, TUR, 'end' if x < 100 else 'start')
    ic += yazi(300, 30, 'Türdeş kutu', 11, SOLUK, ince=True)
    return svg(ic, 360, 154, 'Masa üstündeki türdeş kutunun boyutları', 40)


def eksen(ox, oy, en, boy, xad, yad):
    ic = ok(ox, oy, ox + en, oy, LAC, 1.2) + ok(ox, oy, ox, oy - boy, LAC, 1.2)
    ic += yazi(ox + en + 2, oy + 16, xad, 11.5, LAC, 'end', True) + yazi(ox + 6, oy - boy + 4, yad, 11.5, LAC, 'start', True)
    return ic


def yay_grafik():
    ic = kutu(2, 2, 356, 156, GRI_A, GRI, 8)
    ox, oy = 70, 132
    ic += eksen(ox, oy, 240, 112, 'x (m)', 'F (N)')
    x2, y2 = ox + 180, oy - 90
    ic += f'<polygon points="{ox},{oy} {x2},{y2} {x2},{oy}" fill="{MAVI_A}"/>'
    ic += f'<line x1="{ox}" y1="{oy}" x2="{x2}" y2="{y2}" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += f'<line x1="{ox}" y1="{y2}" x2="{x2}" y2="{y2}" stroke="{GRI}" stroke-dasharray="4 3"/><line x1="{x2}" y1="{y2}" x2="{x2}" y2="{oy}" stroke="{GRI}" stroke-dasharray="4 3"/>'
    ic += yazi(ox - 6, y2 + 4, '40', 12, LAC, 'end') + yazi(x2, oy + 16, '0,2', 12, LAC) + yazi(ox - 6, oy + 14, '0', 12, LAC, 'end')
    return svg(ic, 360, 160, 'Bir yayın kuvvet-uzama grafiği', 40)


def rampa(h1, h2, sutun, etiket, k_yazi='durgun'):
    """Sol yüksek K noktası, eğri yol, sağda L (h2 yüksekliğinde ya da yerde)."""
    ic = kutu(2, 2, 356, 156, GRI_A, GRI, 8)
    yer = 134
    ic += zemin(16, 344, yer, True)
    yK, yL = 46, (yer - 34 if h2 else yer)
    ic += (f'<path d="M30 {yK} C 110 {yK} 120 {yer} 190 {yer} C 250 {yer} 270 {yL} 330 {yL}" fill="none" stroke="{LAC}" stroke-width="2"/>')
    ic += f'<circle cx="36" cy="{yK - 8}" r="8" fill="{TUR}"/>' + yazi(36, yK - 22, 'K', 13, TUR)
    ic += yazi(76, yK - 10, k_yazi, 11, SOLUK, 'start', True)
    ic += f'<line x1="22" y1="{yK}" x2="22" y2="{yer}" stroke="{MAVI}" stroke-dasharray="4 3"/>' + yazi(28, (yK + yer) / 2 + 4, h1, 12, MAVI, 'start')
    if h2:
        ic += f'<line x1="338" y1="{yL}" x2="338" y2="{yer}" stroke="{MAVI}" stroke-dasharray="4 3"/>' + yazi(332, (yL + yer) / 2 + 4, h2, 12, MAVI, 'end')
        ic += f'<circle cx="318" cy="{yL - 7}" r="4" fill="{LAC}"/>' + yazi(318, yL - 16, 'L', 13, LAC)
    else:
        ic += f'<circle cx="320" cy="{yL - 4}" r="4" fill="{LAC}"/>' + yazi(320, yL - 14, 'L', 13, LAC)
    ic += yazi(190, 152, sutun, 11, SOLUK, ince=True)
    return svg(ic, 360, 160, etiket, 40)


def dort_cisim():
    veri = [('K', '2 kg', '6 m/s', MAVI, MAVI_A), ('L', '8 kg', '2 m/s', TUR, TUR_A), ('M', '1 kg', '10 m/s', YES, YES_A), ('N', '4 kg', '3 m/s', MOR, MOR_A)]
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    for i, (ad, m, v, r, a) in enumerate(veri):
        x = 12 + i * 86
        ic += kutu(x, 12, 80, 76, a, r, 6, 1.2)
        ic += yazi(x + 40, 34, ad, 15, r)
        ic += yazi(x + 40, 56, m, 12, LAC, ince=True) + yazi(x + 40, 76, v, 12, LAC, ince=True)
    return svg(ic, 360, 100, 'K, L, M ve N cisimlerinin kütle ve süratleri', 26)


def surtunmeli():
    ic = kutu(2, 2, 356, 116, GRI_A, GRI, 8)
    ic += zemin(16, 344, 76, True)
    ic += kutu(30, 40, 50, 36, MAVI_A, MAVI, 3, 1.4) + yazi(55, 63, '2 kg', 12, MAVI)
    ic += ok(84, 50, 134, 50, KIR) + yazi(110, 40, '10 m/s', 12, KIR)
    ic += kutu(286, 40, 50, 36, '#fff', MAVI, 3, 1) .replace('stroke-width="1"', 'stroke-width="1" stroke-dasharray="4 3"')
    ic += yazi(311, 63, 'durur', 11, SOLUK, ince=True)
    ic += f'<line x1="55" y1="96" x2="311" y2="96" stroke="{TUR}"/><line x1="55" y1="90" x2="55" y2="102" stroke="{TUR}"/><line x1="311" y1="90" x2="311" y2="102" stroke="{TUR}"/>'
    ic += yazi(183, 110, '25 m', 12, TUR)
    return svg(ic, 360, 120, 'Sürtünmeli yolda yavaşlayıp duran cisim', 30)


def yay_blok():
    ic = kutu(2, 2, 356, 104, GRI_A, GRI, 8)
    ic += zemin(30, 344, 80) + f'<rect x="20" y="24" width="10" height="56" fill="{SOLUK}"/>'
    yol = 'M30 60 ' + ' '.join(f'L{36 + i * 8} {48 if i % 2 == 0 else 72}' for i in range(10)) + ' L120 60'
    ic += f'<path d="{yol}" fill="none" stroke="{LAC}" stroke-width="1.6"/>'
    ic += kutu(120, 40, 44, 40, MAVI_A, MAVI, 3, 1.4) + yazi(142, 65, 'm', 13, MAVI)
    ic += yazi(256, 52, 'Yay x kadar sıkışık;', 12, LAC, ince=True) + yazi(256, 70, 'cisim serbest bırakılıyor', 12, LAC, ince=True)
    return svg(ic, 360, 108, 'Sıkıştırılmış yayın önündeki cisim', 28)


def dusme():
    ic = kutu(2, 2, 356, 160, GRI_A, GRI, 8)
    yer = 140
    ic += zemin(16, 344, yer, True)
    ic += f'<circle cx="150" cy="26" r="9" fill="{TUR}"/>' + yazi(170, 30, '0,5 kg · serbest bırakılıyor', 12, LAC, 'start', True)
    ic += f'<line x1="150" y1="38" x2="150" y2="{yer}" stroke="{GRI}" stroke-dasharray="4 3"/>'
    ic += f'<line x1="60" y1="26" x2="60" y2="{yer}" stroke="{MAVI}"/>' + yazi(54, 86, '20 m', 12, MAVI, 'end')
    y15 = yer - 114 * 15 / 20
    ic += f'<line x1="100" y1="{y15:.1f}" x2="200" y2="{y15:.1f}" stroke="{YES}" stroke-dasharray="5 3"/>'
    ic += f'<line x1="240" y1="{y15:.1f}" x2="240" y2="{yer}" stroke="{YES}"/>' + yazi(246, (y15 + yer) / 2 + 4, '15 m', 12, YES, 'start')
    ic += yazi(206, y15 + 4, 'P', 13, YES, 'start')
    return svg(ic, 360, 164, 'Yerden 20 metre yükseklikten bırakılan top', 40)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = iki_arac()
    s[3]['gorsel'] = masa_kutu()
    s[4]['gorsel'] = yay_grafik()
    s[6]['gorsel'] = rampa('5 m', '1,8 m', 'Yol sürtünmesiz · g = 10 m/s²', 'Sürtünmesiz eğri yolda K ve L noktaları')
    s[7]['gorsel'] = dort_cisim()
    s[8]['gorsel'] = surtunmeli()
    s[9]['gorsel'] = yay_blok()
    s[11]['gorsel'] = dusme()
    s[12]['gorsel'] = rampa('6 m', '', 'Yol sürtünmeli · m = 4 kg · g = 10 m/s²', 'Sürtünmeli eğri yolda kayan cisim')
