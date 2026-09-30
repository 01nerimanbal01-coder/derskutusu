"""6. sınıf Fen Bilimleri 1. hafta (Güneş sistemi) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""
import random

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, GRI, GRI_A, SOLUK = '#e8eefe', '#fff1df', '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def no_isareti(x, y, n, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="9.5" fill="{renk}"/>' + yazi(x, y + 4.3, n, 11.5, '#fff')


# (x, yarıçap, renk, halka)
GEZEGEN = [(58, 4, '#9c9c9c', 0), (82, 6, '#e6c27a', 0), (108, 6.5, '#3f8fd8', 0), (132, 5, '#d0533a', 0),
           (186, 17, '#e0a064', 1), (238, 14, '#e8cf8a', 2), (282, 10, '#8fd3e0', 1), (318, 10, '#3e63d6', 1)]


def gezegen(x, y, r, renk, halka):
    ic = ''
    if halka:
        ic += f'<ellipse cx="{x}" cy="{y}" rx="{r * 1.9:.1f}" ry="{r * 0.45:.1f}" fill="none" stroke="{"#b58a3c" if halka == 2 else GRI}" stroke-width="{2.4 if halka == 2 else 0.9}"/>'
    return ic + f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>'


def sistem():
    y = 46
    ic = f'<rect x="0" y="0" width="346" height="92" rx="8" fill="#0f1b3d"/>'
    ic += ''.join(f'<circle cx="{random.Random(k).uniform(40, 340):.0f}" cy="{random.Random(k + 99).uniform(6, 86):.0f}" r=".9" fill="#fff" opacity=".6"/>' for k in range(28))
    ic += f'<circle cx="-14" cy="{y}" r="46" fill="#ffc93c"/>'
    ic += ''.join(f'<circle cx="{random.Random(k).uniform(150, 166):.1f}" cy="{random.Random(k + 7).uniform(18, 74):.1f}" r="{random.Random(k + 3).uniform(0.8, 1.8):.1f}" fill="#b9a58a"/>' for k in range(40))
    for i, (x, r, renk, halka) in enumerate(GEZEGEN, 1):
        ic += gezegen(x, y, r, renk, halka) + yazi(x, 84, i, 11.5, '#fff')
    return svg(346, 92, ic, 'Güneş ve Güneşe yakınlık sırasıyla 1 den 8 e numaralı sekiz gezegen; 4 ile 5 arasında asteroit kuşağı', 24)


def kimlik_karti():
    ic = f'<rect x="4" y="4" width="292" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<rect x="4" y="4" width="292" height="24" rx="10" fill="{MAVI}"/><rect x="4" y="18" width="292" height="10" fill="{MAVI}"/>'
    ic += yazi(150, 21, 'GEZEGEN KİMLİK KARTI', 12, '#fff')
    ic += f'<circle cx="52" cy="68" r="28" fill="#fff" stroke="{GRI}" stroke-width="1.4" stroke-dasharray="4 3"/>' + yazi(52, 76, '?', 22, GRI)
    for i, (a, b) in enumerate([('Yapısı:', 'gazsal'), ("Güneş'e yakınlık sırası:", '7'), ('Uydusu:', 'var'), ('Halkası:', 'var')]):
        yy = 48 + i * 17
        ic += yazi(96, yy, a, 12, SOLUK, 'start') + yazi(290, yy, b, 12.5, LAC, 'end')
    return svg(300, 112, ic, "Gezegen kimlik kartı: yapısı gazsal, Güneşe yakınlık sırası 7, uydusu var, halkası var", 25)


def venn():
    ic = f'<rect x="4" y="4" width="352" height="128" rx="8" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(14, 124, 'Gezegenler', 11.5, SOLUK, 'start')
    ic += f'<circle cx="140" cy="74" r="52" fill="{MAVI}" fill-opacity=".12" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<circle cx="218" cy="74" r="52" fill="{TUR}" fill-opacity=".12" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(112, 18, 'Uydusu var', 12, MAVI) + yazi(248, 18, 'Halkası var', 12, '#b35c00')
    for harf, x, y in [('K', 112, 80), ('L', 179, 80), ('M', 246, 80), ('N', 328, 116)]:
        ic += f'<circle cx="{x}" cy="{y - 5}" r="11" fill="{LAC}"/>' + yazi(x, y, harf, 12.5, '#fff')
    return svg(360, 136, ic, 'İki kesişen küme: Uydusu var ve Halkası var. K yalnız uydusu var bölgesi, L kesişim, M yalnız halkası var, N ikisinin dışı', 30)


def tas(x, y, s=1.0, renk='#7a6a58'):
    n = [(0, -7), (6, -4), (8, 2), (3, 7), (-5, 6), (-8, 0), (-5, -5)]
    return f'<polygon points="{" ".join(f"{x + a * s:.1f},{y + b * s:.1f}" for a, b in n)}" fill="{renk}" stroke="#4a3d30" stroke-width="1"/>'


def meteor():
    ic = f'<rect x="4" y="4" width="112" height="96" rx="6" fill="#0f1b3d"/>'
    ic += ''.join(f'<circle cx="{x}" cy="{y}" r=".9" fill="#fff" opacity=".7"/>' for x, y in [(20, 20), (90, 16), (40, 80), (100, 70), (70, 30), (22, 58)])
    ic += tas(60, 52, 1.6)
    ic += f'<rect x="124" y="4" width="112" height="96" rx="6" fill="#bfe3ff"/>'
    ic += f'<path d="M136 18 L186 58 L182 64 Z" fill="{TUR}" opacity=".8"/><path d="M144 20 L186 56 L180 60 Z" fill="#ffd166"/>' + tas(190, 62, 1.1)
    ic += no_isareti(214, 30, 2)
    ic += f'<rect x="244" y="4" width="112" height="96" rx="6" fill="#dff1ff"/><path d="M244 64 H356 V100 H244 Z" fill="#c9a574"/>'
    ic += f'<path d="M268 64 Q300 96 332 64 Z" fill="#8a6a44"/>' + tas(300, 76, 0.9, '#5b4a3a')
    ic += no_isareti(300, 50, 3) + f'<line x1="300" y1="60" x2="300" y2="70" stroke="{LAC}" stroke-width="1.2"/>'
    ic += no_isareti(342, 50, 4) + f'<line x1="336" y1="57" x2="324" y2="70" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(60, 116, 'uzayda', 11.5, SOLUK) + yazi(180, 116, 'atmosferde', 11.5, SOLUK) + yazi(300, 116, 'yeryüzünde', 11.5, SOLUK)
    return svg(360, 122, ic, 'Üç sahne: uzayda bir gök taşı; atmosferde parlayarak ilerleyen gök taşı (2); yeryüzüne ulaşmış taş (3) ve açtığı çukur (4)', 27)


def cukurlar():
    ic = f'<rect x="0" y="30" width="340" height="44" fill="#c9a574"/><line x1="0" y1="30" x2="340" y2="30" stroke="#8a6a44" stroke-width="2"/>'
    ic += f'<path d="M30 30 Q110 96 190 30 Z" fill="#8a6a44"/>' + yazi(110, 20, 'A', 15, LAC)
    ic += f'<path d="M244 30 Q272 52 300 30 Z" fill="#8a6a44"/>' + yazi(272, 20, 'B', 15, LAC)
    return svg(340, 76, ic, 'Yeryüzünde iki çukur: A geniş ve derin, B küçük', 17)


def ipucu_kartlari():
    kart = ['Uydum var.', 'Halkam yok.', "Asteroit kuşağının Güneş'e yakın tarafındayım.", 'Canlı yaşamı olduğu bilinen gezegen değilim.']
    ic = ''
    for i, m in enumerate(kart):
        y = 4 + i * 31
        ic += f'<rect x="4" y="{y}" width="352" height="26" rx="7" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
        ic += f'<circle cx="19" cy="{y + 13}" r="8.5" fill="{TUR}"/>' + yazi(19, y + 17, i + 1, 11, '#fff')
        ic += yazi(34, y + 17.5, m, 12.5, LAC, 'start')
    return svg(360, 128, ic, "Dört ipucu kartı: Uydum var. Halkam yok. Asteroit kuşağının Güneşe yakın tarafındayım. Canlı yaşamı olduğu bilinen gezegen değilim.", 27)


def gruplar():
    ic = ''
    kisiler = [('Ada', [['Merkür', 'Venüs'], ['Dünya', 'Mars', 'Jüpiter', 'Satürn', 'Uranüs', 'Neptün']]),
               ('Emre', [['Merkür', 'Venüs', 'Dünya', 'Mars'], ['Jüpiter', 'Satürn', 'Uranüs', 'Neptün']])]
    for k, (ad, grup) in enumerate(kisiler):
        y0 = 4 + k * 92
        ic += yazi(8, y0 + 14, f"{ad}'nın gruplaması" if ad == 'Ada' else f"{ad}'nin gruplaması", 12, MOR, 'start')
        x = 8
        for g, liste in enumerate(grup):
            sut = 2 if len(liste) > 2 else 1
            w = 76 * sut + 12
            ic += f'<rect x="{x}" y="{y0 + 22}" width="{w}" height="62" rx="8" fill="{MAVI_A if g == 0 else TUR_A}" stroke="{MAVI if g == 0 else TUR}" stroke-width="1.4"/>'
            for i, ad_ in enumerate(liste):
                her = -(-len(liste) // sut)
                c, r = i // her, i % her
                ic += yazi(x + 10 + c * 76, y0 + 40 + r * 17, ad_, 12, LAC, 'start')
            x += w + 10
    return svg(360, 190, ic, "Ada: Merkür, Venüs bir grupta; Dünya, Mars, Jüpiter, Satürn, Uranüs, Neptün öbür grupta. Emre: Merkür, Venüs, Dünya, Mars bir grupta; Jüpiter, Satürn, Uranüs, Neptün öbür grupta", 42)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sistem()
    s[3]['gorsel'] = kimlik_karti()
    s[6]['gorsel'] = venn()
    s[7]['gorsel'] = meteor()
    s[9]['gorsel'] = cukurlar()
    s[11]['gorsel'] = ipucu_kartlari()
    s[12]['gorsel'] = gruplar()
