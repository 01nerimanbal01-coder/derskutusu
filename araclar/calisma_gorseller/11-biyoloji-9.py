"""11. sınıf Biyoloji 9. hafta görselleri: sinir sistemi (şematik SVG; insan figürü yok, yalnız organ şemaları)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK, PEMBE, PEMBE_K = '#9aa6bd', '#f3f5f9', '#5b6479', '#f9dfe4', '#c7647a'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def isaret(x1, y1, x2, y2, ad, renk=LAC):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="1"/>'
            f'<circle cx="{x1}" cy="{y1}" r="2.4" fill="{renk}"/>' + yazi(x2 + (8 if x2 >= x1 else -8), y2 + 4.5, ad, 13, renk, 'start' if x2 >= x1 else 'end'))


UC = 'M 40 92 C 30 50, 80 14, 160 14 C 240 12, 296 40, 300 86 C 302 108, 286 118, 262 116 L 120 120 C 80 124, 46 116, 40 92 Z'


def beyin(mod):
    ic = cerceve(360, 196)
    if mod == 'lob':
        ic += f'<defs><clipPath id="bl9uc"><path d="{UC}"/></clipPath></defs>'
        ic += '<g clip-path="url(#bl9uc)">'
        ic += f'<rect x="0" y="0" width="128" height="200" fill="{MAVI_A}"/>'
        ic += f'<polygon points="128,0 252,0 236,84 128,78" fill="{YES_A}"/>'
        ic += f'<polygon points="252,0 360,0 360,200 236,200 236,84" fill="{MOR_A}"/>'
        ic += f'<polygon points="70,200 70,96 128,78 236,84 236,200" fill="{TUR_A}"/>'
        ic += '</g>'
        ic += f'<path d="M 128 15 L 128 78 L 236 84 L 252 12 M 128 78 L 74 108 M 236 84 L 236 118" fill="none" stroke="{LAC}" stroke-width="1.2" stroke-dasharray="4 3"/>'
    else:
        ic += f'<path d="{UC}" fill="{PEMBE}" stroke="none"/>'
    for d in ('M 90 40 C 110 52, 100 70, 120 80', 'M 170 26 C 160 46, 186 56, 176 74', 'M 220 34 C 236 50, 220 64, 244 72', 'M 270 56 C 258 70, 280 84, 266 98'):
        ic += f'<path d="{d}" fill="none" stroke="{PEMBE_K}" stroke-width="1" opacity="0.6"/>'
    ic += f'<path d="{UC}" fill="none" stroke="{PEMBE_K}" stroke-width="1.8"/>'
    # beyin sapı ve beyincik
    ic += f'<path d="M 186 112 C 184 136, 196 150, 194 190 L 214 190 C 214 150, 226 132, 222 112 Z" fill="#f4cfd7" stroke="{PEMBE_K}" stroke-width="1.5"/>'
    ic += f'<ellipse cx="208" cy="132" rx="17" ry="11" fill="#efc0cb" stroke="{PEMBE_K}" stroke-width="1.2"/>'
    ic += f'<ellipse cx="258" cy="136" rx="40" ry="22" fill="#f1c6cf" stroke="{PEMBE_K}" stroke-width="1.6"/>'
    for i in range(4):
        ic += f'<path d="M {228 + i * 4} {124 + i * 5} Q 258 {118 + i * 8} {292 - i * 3} {128 + i * 5}" fill="none" stroke="{PEMBE_K}" stroke-width="0.8"/>'
    if mod == 'lob':
        for x, y, n in ((80, 66, '1'), (186, 46, '2'), (270, 80, '3'), (150, 102, '4')):
            ic += f'<circle cx="{x}" cy="{y}" r="11" fill="#fff" stroke="{LAC}" stroke-width="1.2"/>' + yazi(x, y + 4.5, n, 13)
        ic += yazi(22, 186, 'ön', 12, SOLUK, 'start', True) + yazi(338, 186, 'arka', 12, SOLUK, 'end', True)
    else:
        ic += f'<ellipse cx="190" cy="96" rx="20" ry="11" fill="#e9a9b8" stroke="{PEMBE_K}" stroke-width="1.2"/>'
        ic += isaret(120, 46, 60, 170, 'K') + isaret(270, 142, 316, 170, 'L') + isaret(204, 172, 150, 182, 'M') + isaret(198, 96, 318, 40, 'N')
    return svg(ic, 360, 196, 'Beynin yandan şematik kesiti', 40)


def zarlar():
    ic = cerceve(360, 196)
    katman = [('1', 'Kafatası kemiği', 28, '#efe3cf', '#b58b52'), ('2', '', 22, '#e9b4be', PEMBE_K), ('3', '', 22, '#f6e7ea', PEMBE_K),
              ('4', '', 26, '#d7e9fb', MAVI), ('5', '', 22, '#f2bfc9', PEMBE_K)]
    y = 12
    for n, ad, h, d, c in katman:
        ic += f'<rect x="56" y="{y}" width="288" height="{h}" fill="{d}" stroke="{c}" stroke-width="0.9"/>'
        ic += f'<circle cx="32" cy="{y + h / 2}" r="9.5" fill="#fff" stroke="{LAC}" stroke-width="1.1"/>' + yazi(32, y + h / 2 + 4.5, n, 12.5)
        if ad:
            ic += yazi(200, y + h / 2 + 4.5, ad, 12, '#7a5a2e', ince=True)
        if n == '3':
            for x in range(66, 340, 16):
                ic += f'<path d="M {x} {y + h} l 6 22 M {x + 8} {y + h} l -4 24" stroke="{PEMBE_K}" stroke-width="0.6" opacity="0.7"/>'
        y += h
    ic += f'<path d="M 56 {y} ' + ' '.join(f'Q {x + 12} {y + 26} {x + 24} {y}' for x in range(56, 344, 24)) + f' L 344 184 L 56 184 Z" fill="{PEMBE}" stroke="{PEMBE_K}" stroke-width="1"/>'
    ic += yazi(200, 178, 'Beyin dokusu', 12, PEMBE_K, ince=True)
    return svg(ic, 360, 196, 'Beyni saran katmanlar', 38)


def omurilik():
    ic = cerceve(360, 176)
    cx, cy = 130, 92
    ic += f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="60" fill="#fbf3f4" stroke="{PEMBE_K}" stroke-width="1.6"/>'
    kelebek = (f'M {cx} {cy - 8} C {cx - 10} {cy - 46}, {cx - 46} {cy - 50}, {cx - 40} {cy - 22} C {cx - 36} {cy - 6}, {cx - 22} {cy - 4}, {cx - 26} {cy + 8} '
               f'C {cx - 46} {cy + 30}, {cx - 40} {cy + 46}, {cx - 16} {cy + 34} C {cx - 8} {cy + 28}, {cx - 4} {cy + 14}, {cx} {cy + 12} '
               f'C {cx + 4} {cy + 14}, {cx + 8} {cy + 28}, {cx + 16} {cy + 34} C {cx + 40} {cy + 46}, {cx + 46} {cy + 30}, {cx + 26} {cy + 8} '
               f'C {cx + 22} {cy - 4}, {cx + 36} {cy - 6}, {cx + 40} {cy - 22} C {cx + 46} {cy - 50}, {cx + 10} {cy - 46}, {cx} {cy - 8} Z')
    ic += f'<path d="{kelebek}" fill="#d9a3ae" stroke="{PEMBE_K}" stroke-width="1.1"/>'
    ic += f'<circle cx="{cx}" cy="{cy + 2}" r="3" fill="#fff" stroke="{PEMBE_K}" stroke-width="0.8"/>'
    # arka kök (üstte, gangliyonlu) ve ön kök (altta)
    ic += f'<path d="M {cx + 34} {cy - 30} C {cx + 70} {cy - 54}, {cx + 100} {cy - 50}, {cx + 150} {cy - 40}" fill="none" stroke="{TUR}" stroke-width="5" stroke-linecap="round"/>'
    ic += f'<ellipse cx="{cx + 112}" cy="{cy - 46}" rx="13" ry="9" fill="{TUR}"/>'
    ic += f'<path d="M {cx + 34} {cy + 30} C {cx + 70} {cy + 52}, {cx + 100} {cy + 46}, {cx + 150} {cy + 36}" fill="none" stroke="{MAVI}" stroke-width="5" stroke-linecap="round"/>'
    ic += isaret(cx - 64, cy - 26, 26, 24, 'K') + isaret(cx - 30, cy + 30, 26, 160, 'L')
    ic += isaret(cx + 150, cy - 40, 312, 30, 'M') + isaret(cx + 150, cy + 36, 312, 152, 'N')
    ic += yazi(cx, 22, 'sırt tarafı', 11.5, SOLUK, ince=True) + yazi(cx, 166, 'karın tarafı', 11.5, SOLUK, ince=True)
    return svg(ic, 360, 176, 'Omuriliğin enine kesiti', 36)


def nabiz():
    en, boy, ox, oy = 360, 170, 50, 138
    ic = cerceve(en, boy)
    ic += f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="16" stroke="{LAC}" stroke-width="1.4"/><line x1="{ox}" y1="{oy}" x2="{en - 14}" y2="{oy}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(ox + 6, 22, 'Kalp atış hızı (atım/dk)', 12, LAC, 'start') + yazi(en - 16, oy + 22, 'Zaman', 12, LAC, 'end')
    Y = lambda v: oy - (v - 50) * 1.4
    ic += f'<path d="M {ox} {Y(72)} L 120 {Y(72)} C 140 {Y(72)}, 150 {Y(124)}, 175 {Y(124)} L 205 {Y(124)} C 240 {Y(124)}, 270 {Y(74)}, 330 {Y(72)}" fill="none" stroke="{KIR}" stroke-width="2.6"/>'
    for v in (72, 124):
        ic += f'<line x1="{ox}" y1="{Y(v):.1f}" x2="205" y2="{Y(v):.1f}" stroke="{GRI}" stroke-width="0.8" stroke-dasharray="3 3"/>' + yazi(ox - 6, Y(v) + 4.5, str(v), 12, LAC, 'end')
    for x in (120, 175, 205, 300):
        ic += f'<line x1="{x}" y1="{oy}" x2="{x}" y2="{oy - 92}" stroke="{GRI}" stroke-width="0.8" stroke-dasharray="3 3"/>'
    ic += yazi(147, oy - 8, 'I', 13, MAVI) + yazi(252, oy - 8, 'II', 13, MAVI)
    ic += f'<path d="M 120 36 L 120 {Y(76):.1f}" stroke="{TUR}" stroke-width="1.6"/><polygon points="120,{Y(74):.1f} 115,{Y(80):.1f} 125,{Y(80):.1f}" fill="{TUR}"/>'
    ic += yazi(112, 62, 'ani gürültü', 11.5, TUR, 'end', True)
    return svg(ic, en, boy, 'Korku anında kalp atış hızının zamanla değişimi', 34)


def hastalar():
    ic = cerceve(360, 132)
    for i, (ad, satir, c, a) in enumerate((('Hasta X', ['Bilinç ve istemli hareket yok', 'Solunum kendiliğinden sürüyor', 'Kalp atışı düzenli'], MAVI, MAVI_A),
                                           ('Hasta Y', ['Bilinç ve istemli hareket yok', 'Solunum yalnız cihazla', 'Beyin sapı refleksleri yok'], KIR, KIR_A))):
        x = 10 + i * 172
        ic += f'<rect x="{x}" y="10" width="166" height="112" rx="7" fill="{a}" stroke="{c}" stroke-width="1"/>'
        ic += yazi(x + 83, 32, ad, 13.5, c) + f'<line x1="{x + 12}" y1="42" x2="{x + 154}" y2="42" stroke="{c}" stroke-width="0.6"/>'
        for j, t in enumerate(satir):
            ic += yazi(x + 83, 64 + j * 22, t, 11.5, LAC, ince=True)
    return svg(ic, 360, 132, 'İki hastanın durum kartları', 30)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = beyin('bolum')
    s[2]['gorsel'] = beyin('lob')
    s[4]['gorsel'] = zarlar()
    s[6]['gorsel'] = omurilik()
    s[8]['gorsel'] = nabiz()
    s[10]['gorsel'] = hastalar()
