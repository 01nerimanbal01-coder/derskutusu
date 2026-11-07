"""10. sınıf Coğrafya 9. hafta görselleri (SVG; şematik kesit ve plan çizimleri; görsel içi yazı ≈ gövde puntosu, K150 EK).

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

TOPRAK, TOPRAK_A, SU, SU_A = '#8a6a3b', '#efe3cc', '#2a7fd4', '#d9ecfb'


def ok(x1, y1, x2, y2, renk=LAC, kalin=1.4):
    a = math.atan2(y2 - y1, x2 - x1)
    u1 = (x2 - 7 * math.cos(a - 0.45), y2 - 7 * math.sin(a - 0.45))
    u2 = (x2 - 7 * math.cos(a + 0.45), y2 - 7 * math.sin(a + 0.45))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<polygon points="{x2},{y2} {u1[0]:.1f},{u1[1]:.1f} {u2[0]:.1f},{u2[1]:.1f}" fill="{renk}"/>')


def vadiler():
    ic = kutu(2, 2, 356, 128, GRI_A, GRI, 8)
    ic += f'<path d="M16 30 L66 100 L76 100 L160 30 L160 110 L16 110 Z" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.3"/>'
    ic += f'<path d="M64 97 L78 97 L76 100 L66 100 Z" fill="{SU}"/>'
    ic += f'<path d="M200 30 L212 30 C 218 104 236 104 270 104 C 304 104 322 104 328 30 L344 30 L344 110 L200 110 Z" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.3"/>'
    ic += yazi(88, 20, 'I', 14, MAVI) + yazi(272, 20, 'II', 14, MAVI)
    ic += yazi(180, 126, 'Enine kesitler', 11, SOLUK, ince=True)
    return svg(ic, 360, 132, 'Enine kesitleri verilen I ve II numaralı vadiler', 34)


def menderes():
    ic = kutu(2, 2, 356, 140, GRI_A, GRI, 8)
    ic += f'<rect x="10" y="10" width="340" height="124" rx="6" fill="{YES_A}"/>'
    yol = 'M14 40 C 90 40 110 120 180 110 C 250 100 230 30 300 34 C 330 36 340 60 346 70'
    ic += f'<path d="{yol}" fill="none" stroke="{SU_A}" stroke-width="22"/><path d="{yol}" fill="none" stroke="{SU}" stroke-width="2"/>'
    ic += ok(40, 22, 70, 30, SU, 1.4) + yazi(36, 26, 'akış', 11, SU, 'end', True)
    ic += f'<circle cx="180" cy="124" r="5" fill="{KIR}"/>' + yazi(194, 129, 'K', 13, KIR, 'start')
    ic += f'<circle cx="174" cy="96" r="5" fill="{TUR}"/>' + yazi(174, 86, 'L', 13, TUR)
    ic += yazi(290, 96, 'Akarsuyun', 11, SOLUK, ince=True) + yazi(290, 110, 'kuşbakışı görünümü', 11, SOLUK, ince=True)
    return svg(ic, 360, 144, 'Büklüm yaparak akan akarsuyun dış kıyısında K, iç kıyısında L noktası', 38)


def kiyi():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += f'<rect x="10" y="10" width="340" height="134" rx="6" fill="{SU_A}"/>'
    ic += f'<path d="M10 10 L350 10 L350 50 C 300 52 280 46 250 50 C 236 18 174 18 160 50 C 120 46 60 52 10 50 Z" fill="{YES_A}" stroke="{TOPRAK}" stroke-width="1.2"/>'
    ic += f'<path d="M160 50 C 174 18 236 18 250 50 Z" fill="#bcdcf7"/>'
    ic += f'<path d="M158 51 C 180 54 230 54 252 51" fill="none" stroke="{TOPRAK}" stroke-width="5"/>'
    ic += yazi(205, 42, 'Y', 14, MAVI)
    ic += f'<path d="M70 50 L74 104" stroke="{TOPRAK}" stroke-width="5"/>'
    ic += f'<ellipse cx="78" cy="118" rx="28" ry="16" fill="{YES_A}" stroke="{TOPRAK}" stroke-width="1.2"/>'
    ic += yazi(98, 84, 'X', 14, KIR)
    ic += yazi(300, 30, 'kara', 12, SOLUK, ince=True) + yazi(290, 120, 'deniz', 12, SU, ince=True)
    return svg(ic, 360, 154, 'Kıyıda X ve Y ile gösterilen birikim şekilleri', 40)


def profil():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    ic += f'<path d="M14 24 C 70 30 110 70 170 84 C 230 96 290 98 346 100 L346 106 L14 106 Z" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.3"/>'
    ic += yazi(22, 18, 'kaynak', 11.5, LAC, 'start', True) + yazi(340, 92, 'ağız (deniz)', 11.5, SU, 'end', True)
    ic += ok(120, 40, 260, 76, SU, 1.6) + yazi(206, 50, 'eğim azalır', 11, SOLUK, 'start', True)
    return svg(ic, 360, 116, 'Bir akarsuyun boyuna profili', 30)


def mantarkaya():
    ic = kutu(2, 2, 356, 140, GRI_A, GRI, 8)
    ic += f'<rect x="10" y="114" width="340" height="22" fill="#f4e7c3"/>'
    ic += f'<path d="M150 114 C 160 96 164 82 156 70 C 130 66 112 50 128 34 C 160 20 220 22 238 36 C 250 52 230 66 206 70 C 198 82 200 98 212 114 Z" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.4"/>'
    for y in (90, 102):
        ic += ok(30, y, 136, y, TUR, 1.6)
    for x, y in ((50, 82), (80, 96), (110, 86), (64, 108)):
        ic += f'<circle cx="{x}" cy="{y}" r="2" fill="{TUR}"/>'
    ic += yazi(30, 78, 'kum taneli rüzgâr', 11, TUR, 'start', True)
    ic += yazi(290, 60, 'Kaya', 12, TOPRAK, ince=True)
    return svg(ic, 360, 144, 'Alt kısmı aşınmış, mantar biçimli kaya', 36)


def derinlik():
    ic = kutu(2, 2, 356, 120, GRI_A, GRI, 8)
    for x0, ad, d in ((14, 'A kıyısı', 'derin'), (190, 'B kıyısı', 'sığ')):
        ic += f'<rect x="{x0}" y="40" width="156" height="72" fill="{SU_A}"/>'
        if d == 'derin':
            ic += f'<path d="M{x0} 20 L{x0 + 48} 20 L{x0 + 52} 108 L{x0} 108 Z" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.3"/>'
            ic += f'<path d="M{x0 + 52} 108 L{x0 + 156} 112" stroke="{TOPRAK}" stroke-width="1.3"/>'
        else:
            ic += f'<path d="M{x0} 34 L{x0 + 40} 38 L{x0 + 156} 62 L{x0 + 156} 112 L{x0} 112 Z" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.3"/>'
        ic += f'<line x1="{x0}" y1="40" x2="{x0 + 156}" y2="40" stroke="{SU}" stroke-width="1.4"/>'
        ic += yazi(x0 + 78, 16, ad, 12.5, MAVI)
        ic += yazi(x0 + 110, 30, 'deniz', 11, SU, ince=True)
    return svg(ic, 360, 124, 'Kıyı ve deniz tabanı kesitleri: A kıyısı ile B kıyısı', 32)


def seki():
    ic = kutu(2, 2, 356, 130, GRI_A, GRI, 8)
    yol = 'M12 24 L60 24 L68 50 L104 50 L112 78 L150 78 L160 104 L200 104 L210 78 L248 78 L256 50 L292 50 L300 24 L348 24 L348 112 L12 112 Z'
    ic += f'<path d="{yol}" fill="{TOPRAK_A}" stroke="{TOPRAK}" stroke-width="1.3"/>'
    ic += f'<path d="M166 102 L194 102 L196 104 L164 104 Z" fill="{SU}"/>'
    for x, y, t in ((84, 46, '1'), (130, 74, '2'), (228, 74, '2'), (274, 46, '1')):
        ic += yazi(x, y, t, 12, KIR)
    ic += yazi(180, 98, 'akarsu', 11, SU, ince=True)
    ic += yazi(180, 128, 'Vadinin enine kesiti (1, 2: basamaklar)', 11, SOLUK, ince=True)
    return svg(ic, 360, 134, 'Akarsu vadisinde iki yanda karşılıklı basamaklar', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = vadiler()
    s[3]['gorsel'] = menderes()
    s[5]['gorsel'] = kiyi()
    s[6]['gorsel'] = profil()
    s[8]['gorsel'] = mantarkaya()
    s[10]['gorsel'] = derinlik()
    s[11]['gorsel'] = seki()
