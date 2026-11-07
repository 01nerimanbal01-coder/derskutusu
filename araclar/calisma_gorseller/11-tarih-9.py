"""11. sınıf Tarih 9. hafta görselleri: Sanayi Devrimi (SVG şemalar; insan figürü yok)."""
LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK, KAHVE = '#9aa6bd', '#f3f5f9', '#5b6479', '#8a5a2b'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def kutu(x, y, w, h, d, c, r=7):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{d}" stroke="{c}" stroke-width="1"/>'


def ok(x1, y1, x2, y2, renk=LAC):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 9 * math.cos(a) + 4.5 * math.sin(a), y2 - 9 * math.sin(a) - 4.5 * math.cos(a))
    p2 = (x2 - 9 * math.cos(a) - 4.5 * math.sin(a), y2 - 9 * math.sin(a) + 4.5 * math.cos(a))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 7 * math.cos(a):.1f}" y2="{y2 - 7 * math.sin(a):.1f}" stroke="{renk}" stroke-width="1.6"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{renk}"/>')


def etkenler():
    kart = [('I', ['Zengin taş kömürü', 've demir yatakları'], MAVI, MAVI_A), ('II', ['Sömürge ticaretiyle', 'sermaye birikimi'], YES, YES_A),
            ('III', ['Ada ülkesi olup', 'kıta savaşlarından', 'uzak kalması'], MOR, MOR_A), ('IV', ['Lonca teşkilatının', 'üretimi denetlemesi'], TUR, TUR_A)]
    ic = cerceve(360, 150) + yazi(180, 22, "İngiltere'de Sanayi Devrimi", 13, LAC)
    for i, (n, sat, c, a) in enumerate(kart):
        x, y = 10 + (i % 2) * 172, 32 + (i // 2) * 58
        ic += kutu(x, y, 166, 52, a, c) + yazi(x + 18, y + 31, n, 13, c)
        y0 = y + 26 - (len(sat) - 1) * 7.5 + 4
        for j, t in enumerate(sat):
            ic += yazi(x + 98, y0 + j * 15, t, 11.5, LAC, ince=True)
    return svg(ic, 360, 150, 'Dört etken kartı', 34)


def zaman():
    ic = cerceve(360, 120)
    ic += f'<line x1="20" y1="64" x2="342" y2="64" stroke="{LAC}" stroke-width="2.2"/>'
    olay = [(46, "1760'lar", 'Buhar makinesi', 'geliştirildi', MAVI), (136, '1838', 'Balta Limanı', 'Antlaşması', YES),
            (226, '1854', 'X', '', KIR), (314, '1881', 'Düyûn-ı', 'Umûmiye', MOR)]
    for x, t, a, b, c in olay:
        ic += f'<circle cx="{x}" cy="64" r="6" fill="{c}"/>' + yazi(x, 48, t, 12.5, c)
        if a == 'X':
            ic += f'<circle cx="{x}" cy="92" r="12" fill="#fff" stroke="{KIR}" stroke-width="1.4"/>' + yazi(x, 97, 'X', 13.5, KIR)
        else:
            ic += yazi(x, 88, a, 11.5, LAC, ince=True) + yazi(x, 104, b, 11.5, LAC, ince=True)
    return svg(ic, 360, 120, 'Zaman şeridi', 28)


def ticaret():
    ic = cerceve(360, 150)
    ic += kutu(12, 44, 104, 62, KIR_A, KIR) + yazi(64, 72, 'Osmanlı', 13.5, KIR) + yazi(64, 90, 'Devleti', 13.5, KIR)
    ic += kutu(244, 44, 104, 62, MAVI_A, MAVI) + yazi(296, 72, 'Avrupa', 13.5, MAVI) + yazi(296, 90, 'devletleri', 12.5, MAVI)
    ic += ok(122, 56, 238, 56, YES) + yazi(180, 30, 'Pamuk, yün, tütün,', 11.5, YES, ince=True) + yazi(180, 46, 'maden', 11.5, YES, ince=True)
    ic += ok(238, 96, 122, 96, TUR) + yazi(180, 116, 'Dokuma ve fabrika', 11.5, TUR, ince=True) + yazi(180, 132, 'ürünleri', 11.5, TUR, ince=True)
    return svg(ic, 360, 150, "Osmanlı ile Avrupa arasındaki ticaret", 34)


def zincir():
    ic = cerceve(360, 112)
    k = [(10, ['Kesintisiz', 'üretim'], MAVI, MAVI_A), (128, ['Ucuz ham madde', 've yeni pazar'], YES, YES_A), (246, ['?'], KIR, KIR_A)]
    for x, sat, c, a in k:
        ic += kutu(x, 26, 104, 60, a, c)
        if len(sat) == 1:
            ic += yazi(x + 52, 64, sat[0], 22, c)
        else:
            ic += yazi(x + 52, 52, sat[0], 11.5, LAC) + yazi(x + 52, 70, sat[1], 11.5, LAC)
    ic += ok(115, 56, 127, 56) + ok(233, 56, 245, 56)
    ic += yazi(180, 104, 'ihtiyaç → arayış → sonuç', 11, SOLUK, ince=True)
    return svg(ic, 360, 112, 'Neden-sonuç zinciri', 26)


def fabrika(x, y):
    ic = f'<rect x="{x}" y="{y + 26}" width="84" height="40" fill="#e2e6ee" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<polygon points="{x},{y + 26} {x + 21},{y + 12} {x + 21},{y + 26} {x + 42},{y + 12} {x + 42},{y + 26} {x + 63},{y + 12} {x + 63},{y + 26}" fill="#c9cfdb" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<rect x="{x + 68}" y="{y - 8}" width="10" height="34" fill="#b9805a" stroke="{LAC}" stroke-width="1"/>'
    for i, r in enumerate((5, 7, 9)):
        ic += f'<circle cx="{x + 76 + i * 9}" cy="{y - 14 - i * 8}" r="{r}" fill="#cfd4dc" opacity="0.8"/>'
    for i in range(3):
        ic += f'<rect x="{x + 8 + i * 24}" y="{y + 38}" width="14" height="12" fill="#fff" stroke="{LAC}" stroke-width="0.8"/>'
    return ic


def tezgah(x, y):
    ic = f'<rect x="{x}" y="{y + 10}" width="70" height="50" fill="none" stroke="{KAHVE}" stroke-width="2.4"/>'
    for i in range(7):
        ic += f'<line x1="{x + 8 + i * 9}" y1="{y + 14}" x2="{x + 8 + i * 9}" y2="{y + 56}" stroke="{KAHVE}" stroke-width="0.8"/>'
    ic += f'<rect x="{x + 4}" y="{y + 32}" width="62" height="6" fill="{KAHVE}"/>'
    return ic


def donusum():
    ic = cerceve(360, 162)
    ic += kutu(10, 10, 160, 142, TUR_A, TUR) + kutu(190, 10, 160, 142, MAVI_A, MAVI)
    ic += yazi(90, 30, 'Öncesi', 13, TUR) + yazi(270, 30, 'Sonrası', 13, MAVI)
    ic += tezgah(55, 38) + fabrika(228, 62)
    ic += yazi(90, 116, 'El tezgâhı · geniş aile', 11, LAC, ince=True) + yazi(90, 134, 'kırsal yaşam', 11, LAC, ince=True)
    ic += yazi(270, 140, 'Fabrika · çekirdek aile · kent', 11, LAC, ince=True)
    ic += ok(172, 78, 188, 78)
    return svg(ic, 360, 162, 'Sanayi Devrimi öncesi ve sonrası', 35)


def ulasim():
    ic = cerceve(360, 132)
    # buharlı lokomotif
    ic += f'<line x1="14" y1="100" x2="170" y2="100" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<rect x="30" y="58" width="80" height="28" rx="12" fill="#c9cfdb" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<rect x="104" y="40" width="44" height="46" rx="3" fill="{KIR_A}" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<rect x="114" y="48" width="24" height="14" fill="#fff" stroke="{LAC}" stroke-width="0.8"/>'
    ic += f'<rect x="44" y="36" width="12" height="22" fill="#6b7385" stroke="{LAC}" stroke-width="1"/>'
    for i, r in enumerate((5, 7, 9)):
        ic += f'<circle cx="{40 - i * 6}" cy="{28 - i * 6}" r="{r}" fill="#cfd4dc" opacity="0.85"/>'
    for x, r in ((48, 9), (78, 9), (126, 11)):
        ic += f'<circle cx="{x}" cy="{97 - r}" r="{r}" fill="#fff" stroke="{LAC}" stroke-width="1.6"/>'
    ic += yazi(92, 120, 'Buharlı lokomotif', 11.5, LAC, ince=True)
    # buharlı gemi
    ic += f'<path d="M 196 96 Q 270 104 346 96" fill="none" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="198,74 344,74 330,96 212,96" fill="{MAVI_A}" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<rect x="232" y="58" width="76" height="16" fill="#fff" stroke="{LAC}" stroke-width="1"/>'
    ic += f'<rect x="262" y="34" width="12" height="24" fill="{KIR}" stroke="{LAC}" stroke-width="1"/>'
    for i, r in enumerate((5, 7, 9)):
        ic += f'<circle cx="{280 + i * 9}" cy="{28 - i * 6}" r="{r}" fill="#cfd4dc" opacity="0.85"/>'
    ic += yazi(270, 120, 'Buharlı gemi', 11.5, LAC, ince=True)
    return svg(ic, 360, 132, 'Buharlı lokomotif ve buharlı gemi', 30)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = etkenler()
    s[2]['gorsel'] = zaman()
    s[4]['gorsel'] = ticaret()
    s[8]['gorsel'] = zincir()
    s[10]['gorsel'] = donusum()
    s[11]['gorsel'] = ulasim()
