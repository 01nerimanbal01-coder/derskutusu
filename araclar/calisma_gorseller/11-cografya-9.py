"""11. sınıf Coğrafya 9. hafta görselleri: Web-CBS veri modelleri ve mekânsal analizler (SVG şemalar)."""
LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def pano(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#f7f4ea" stroke="{GRI}" stroke-width="1"/>'


def vektor():
    ic = cerceve(360, 140)
    for i, ad in enumerate(('I', 'II', 'III')):
        x = 10 + i * 116
        ic += pano(x, 24, 108, 90) + yazi(x + 54, 18, ad, 13, MAVI)
    for cx, cy in ((34, 50), (60, 80), (88, 44), (100, 96), (48, 100)):
        ic += f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="{KIR}" stroke="#fff" stroke-width="1"/>'
    ic += f'<path d="M 128 40 C 150 60, 170 44, 184 70 S 210 92, 230 100" fill="none" stroke="{MAVI}" stroke-width="3"/>'
    ic += f'<path d="M 184 70 C 196 58, 212 52, 226 36" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<path d="M 260 52 C 270 34, 312 36, 326 54 C 340 74, 318 104, 292 100 C 266 98, 250 72, 260 52 Z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(68, 132, 'Deprem merkez üsleri', 11, LAC, ince=True) + yazi(184, 132, 'Akarsu', 11, LAC, ince=True) + yazi(300, 132, 'Göl', 11, LAC, ince=True)
    return svg(ic, 360, 140, 'Üç vektör katmanı', 32)


DEGER = [[420, 560, 710, 880, 960], [380, 610, 790, 920, 1040], [350, 540, 820, 870, 990], [300, 470, 650, 760, 830], [260, 400, 520, 690, 740]]


def raster():
    ic = cerceve(360, 176)
    x0, y0, a = 20, 14, 30
    for r, satir in enumerate(DEGER):
        for c, v in enumerate(satir):
            d = YES_A if v < 500 else ('#fde7b8' if v < 800 else '#f3b9a4')
            ic += f'<rect x="{x0 + c * a}" y="{y0 + r * a}" width="{a}" height="{a}" fill="{d}" stroke="#fff" stroke-width="1.2"/>'
            ic += yazi(x0 + c * a + a / 2, y0 + r * a + a / 2 + 4, str(v), 10.5, LAC, ince=True)
    ic += f'<rect x="{x0}" y="{y0}" width="{5 * a}" height="{5 * a}" fill="none" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(196, 34, 'Yükselti (m)', 12.5, LAC, 'start')
    for i, (d, t) in enumerate(((YES_A, '500’den az'), ('#fde7b8', '500 – 799'), ('#f3b9a4', '800 ve üzeri'))):
        y = 50 + i * 26
        ic += f'<rect x="196" y="{y}" width="20" height="16" fill="{d}" stroke="{GRI}" stroke-width="0.8"/>' + yazi(224, y + 12.5, t, 11.5, LAC, 'start', True)
    ic += yazi(196, 150, 'Hücre: 1 km × 1 km', 11, SOLUK, 'start', True)
    return svg(ic, 360, 176, 'Raster yükselti katmanı', 38)


def tampon():
    ic = cerceve(360, 150)
    ic += pano(10, 10, 340, 130)
    yol = 'M 14 82 C 80 50, 140 110, 200 76 S 300 50, 346 70'
    ic += f'<path d="{yol}" fill="none" stroke="#cfdcfb" stroke-width="44" stroke-linecap="butt" opacity="0.9"/>'
    ic += f'<path d="{yol}" fill="none" stroke="{MAVI}" stroke-width="3"/>'
    for x, y, ad in ((70, 62, 'K'), (128, 30, 'L'), (214, 86, 'M'), (270, 118, 'N'), (312, 24, 'P')):
        ic += f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" fill="{KIR}" stroke="#fff" stroke-width="1"/>' + yazi(x + 13, y + 5, ad, 12.5, KIR, 'start')
    ic += f'<rect x="22" y="112" width="18" height="12" fill="#cfdcfb"/>' + yazi(46, 122, '500 m tampon bölge', 11, LAC, 'start', True)
    return svg(ic, 360, 150, 'Akarsu çevresinde tampon bölge', 34)


def cakistirma():
    ic = cerceve(360, 132)
    katman = [('Eğim uygun', {0, 1, 3, 4, 6, 7}, YES), ('Faya uzak', {1, 2, 4, 5, 7}, MOR), ('Yola yakın', {3, 4, 5, 8}, TUR)]
    a = 20
    for k, (ad, sec, c) in enumerate(katman):
        x0 = 14 + k * 86
        ic += yazi(x0 + 30, 22, ad, 11, c)
        for i in range(9):
            d = c if i in sec else '#fff'
            ic += f'<rect x="{x0 + (i % 3) * a}" y="{34 + (i // 3) * a}" width="{a}" height="{a}" fill="{d}" fill-opacity="{0.55 if i in sec else 1}" stroke="{LAC}" stroke-width="0.8"/>'
        if k < 2:
            ic += yazi(x0 + 72, 66, '+', 16, LAC)
    x0 = 272
    ic += yazi(x0 + 30, 22, 'Hücre adı', 11, LAC)
    for i, h in enumerate('ABCDEFGHI'):
        ic += f'<rect x="{x0 + (i % 3) * a}" y="{34 + (i // 3) * a}" width="{a}" height="{a}" fill="#fff" stroke="{LAC}" stroke-width="0.8"/>'
        ic += yazi(x0 + (i % 3) * a + 10, 34 + (i // 3) * a + 14.5, h, 11.5, LAC)
    ic += yazi(250, 66, '=', 16, LAC) if False else ''
    ic += yazi(180, 120, 'Renkli hücre: koşulu sağlıyor', 11, SOLUK, ince=True)
    return svg(ic, 360, 132, 'Üç katmanın çakıştırılması', 30)


def sembol():
    ic = cerceve(360, 150)
    ic += pano(10, 24, 166, 100) + pano(184, 24, 166, 100)
    ic += yazi(93, 18, 'I', 13, MAVI) + yazi(267, 18, 'II', 13, MAVI)
    bolge = ['M 16 30 L 80 30 L 72 74 L 16 70 Z', 'M 80 30 L 170 30 L 170 60 L 110 80 L 72 74 Z', 'M 16 70 L 72 74 L 66 118 L 16 118 Z',
             'M 72 74 L 110 80 L 170 60 L 170 118 L 66 118 Z']
    for d, r in zip(bolge, ('#fbe3cf', '#f2a46a', '#e46a2c', '#fbd0ad')):
        ic += f'<path d="{d}" fill="{r}" stroke="#fff" stroke-width="1.5"/>'
    ic += '<g transform="translate(174,0)">' + ''.join(f'<path d="{d}" fill="#eef0f3" stroke="{GRI}" stroke-width="1"/>' for d in bolge) + '</g>'
    for cx, cy, r in ((214, 50, 5), (300, 46, 11), (222, 98, 8), (310, 98, 15), (262, 80, 4)):
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{KIR}" fill-opacity="0.55" stroke="{KIR}" stroke-width="1"/>'
    ic += yazi(93, 142, 'Renk tonu derecelendirmesi', 11, LAC, ince=True) + yazi(267, 142, 'Farklı boyutlu daireler', 11, LAC, ince=True)
    return svg(ic, 360, 150, 'İki farklı sembolleştirme yöntemi', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = vektor()
    s[2]['gorsel'] = raster()
    s[4]['gorsel'] = tampon()
    s[6]['gorsel'] = cakistirma()
    s[9]['gorsel'] = sembol()
