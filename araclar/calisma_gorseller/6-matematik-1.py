"""6. sınıf Matematik 1. hafta çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a'
MAVI_A, TUR_A, YES_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#9aa6bd', '#eef1f6'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def dikdortgenler():
    b = 12
    ic = f'<rect x="0" y="0" width="{23 * b}" height="{9 * b}" fill="#fff"/>'
    ic += ''.join(f'<line x1="{i * b}" y1="0" x2="{i * b}" y2="{9 * b}" stroke="#d5dbe7" stroke-width="0.8"/>' for i in range(24))
    ic += ''.join(f'<line x1="0" y1="{j * b}" x2="{23 * b}" y2="{j * b}" stroke="#d5dbe7" stroke-width="0.8"/>' for j in range(10))
    for x, y, w, h, dolgu, cizgi in [(1, 1, 20, 1, TUR_A, TUR), (1, 4, 10, 2, MAVI_A, MAVI), (14, 3, 5, 4, YES_A, YES)]:
        ic += f'<rect x="{x * b}" y="{y * b}" width="{w * b}" height="{h * b}" fill="{dolgu}" stroke="{cizgi}" stroke-width="2.2"/>'
    return svg(23 * b, 9 * b, ic, 'Kareli zeminde alanı 20 birimkare olan üç dikdörtgen: 1 e 20, 2 ye 10 ve 4 e 5 birim', 24)


def sayi_dogrusu():
    x0, u, y = 22, 11, 58
    ic = f'<defs><marker id="ck6ok1" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{LAC}"/></marker></defs>'
    ic += f'<line x1="{x0 - 10}" y1="{y}" x2="{x0 + 38 * u}" y2="{y}" stroke="{LAC}" stroke-width="2" marker-end="url(#ck6ok1)"/>'
    for i in range(37):
        uzun = i % 6 == 0
        ic += f'<line x1="{x0 + i * u}" y1="{y - (7 if uzun else 4)}" x2="{x0 + i * u}" y2="{y + (7 if uzun else 4)}" stroke="{LAC}" stroke-width="{1.8 if uzun else 1}"/>'
    for k in range(6):
        a, c = x0 + k * 6 * u, x0 + (k + 1) * 6 * u
        ic += f'<path d="M{a} {y - 9} Q{(a + c) / 2} {y - 44} {c} {y - 9}" fill="none" stroke="{TUR}" stroke-width="2.2"/>'
        ic += f'<path d="M{c - 6} {y - 16} L{c} {y - 9} L{c - 8} {y - 9}" fill="none" stroke="{TUR}" stroke-width="2" stroke-linejoin="round"/>'
    for i in (0, 6, 12):
        ic += yazi(x0 + i * u, y + 24, i)
    return svg(x0 + 40 * u, 88, ic, "0'dan başlayıp eşit uzunlukta altı atlama; 0, 6 ve 12 işaretli", 22)


def kartlar():
    ic, x = '', 4
    for s in ['1', '2', '3', '4', None, '8', '12', '24']:
        if s is None:
            ic += f'<rect x="{x}" y="6" width="40" height="54" rx="6" fill="{MAVI}" stroke="{LAC}" stroke-width="1.6"/>'
            ic += f'<rect x="{x + 5}" y="11" width="30" height="44" rx="4" fill="none" stroke="#fff" stroke-width="1.2" stroke-dasharray="3 3"/>'
            ic += yazi(x + 20, 40, '?', 18, '#fff')
        else:
            ic += f'<rect x="{x}" y="6" width="40" height="54" rx="6" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
            ic += yazi(x + 20, 39, s, 16)
        x += 48
    return svg(x, 66, ic, 'Sekiz kart: 1, 2, 3, 4, ters çevrilmiş kart, 8, 12, 24', 17)


def kalemler():
    renkler = [KIR, MAVI, YES, TUR, '#8a4fd6', '#e0b400', '#1aa3b8', '#e0559b']
    ic = ''
    for p in range(3):
        px = 10 + p * 92
        for i, r in enumerate(renkler):
            x = px + 9 + i * 8.5
            ic += f'<rect x="{x}" y="12" width="6" height="44" rx="1.5" fill="{r}"/>'
            ic += f'<path d="M{x} 12 L{x + 3} 4 L{x + 6} 12 Z" fill="#f3d9b1"/><path d="M{x + 2} 6.5 L{x + 3} 4 L{x + 4} 6.5 Z" fill="{r}"/>'
        ic += f'<rect x="{px}" y="30" width="80" height="34" rx="5" fill="{GRI_A}" fill-opacity=".92" stroke="{GRI}" stroke-width="1.6"/>'
        ic += yazi(px + 40, 52, '8 kalem', 13)
    return svg(290, 70, ic, 'Her birinde 8 kalem olan 3 paket', 18)


def raflar():
    ic, x = '', 6
    for no in [1, 2, 3, 4, 5, 6, 7, 8, None, 30]:
        if no is None:
            ic += yazi(x + 16, 40, '…', 20)
            x += 34
            continue
        ic += f'<rect x="{x}" y="8" width="34" height="46" rx="2" fill="#d9a066" stroke="#8a5a2b" stroke-width="1.5"/>'
        for yy in (22, 38):
            ic += f'<line x1="{x}" y1="{yy}" x2="{x + 34}" y2="{yy}" stroke="#8a5a2b" stroke-width="1.5"/>'
        for i, r in enumerate([MAVI, YES, TUR]):
            ic += f'<rect x="{x + 5 + i * 8}" y="{11 + (i % 2)}" width="6" height="{11 - (i % 2)}" fill="{r}"/>'
        etiketler = ([KIR] if no % 4 == 0 else []) + ([MAVI] if no % 6 == 0 else [])
        for i, r in enumerate(etiketler):
            ic += f'<rect x="{x + 4 + i * 14}" y="42" width="12" height="9" rx="1.5" fill="{r}"/>'
        ic += yazi(x + 17, 72, no, 13)
        x += 40
    return svg(x, 78, ic, '1 den 8 e kadar raflar ve 30 numaralı raf; 4 ve 8 numaralı raflarda kırmızı, 6 ve 30 numaralı raflarda mavi etiket', 20)


def kilit():
    ic = f'<path d="M34 50 V34 a28 28 0 0 1 56 0 V50" fill="none" stroke="{GRI}" stroke-width="9"/>'
    ic += f'<rect x="18" y="48" width="88" height="70" rx="10" fill="{TUR}" stroke="#b85c06" stroke-width="2"/>'
    for i in range(2):
        ic += f'<rect x="{32 + i * 32}" y="66" width="26" height="34" rx="4" fill="#fff" stroke="#b85c06" stroke-width="1.6"/>'
        ic += yazi(45 + i * 32, 90, '?', 16, GRI)
    ipuclari = ['İki basamaklıdır.', "9'un katıdır.", '4, bu sayının çarpanıdır.', "50'den küçüktür."]
    for i, m in enumerate(ipuclari):
        yy = 30 + i * 26
        ic += f'<circle cx="138" cy="{yy - 5}" r="9" fill="{MAVI}"/>' + yazi(138, yy, i + 1, 12, '#fff')
        ic += yazi(156, yy, m, 14, LAC, 'start')
    return svg(360, 126, ic, "İki haneli şifreli kilit ve dört ipucu: iki basamaklıdır, 9'un katıdır, 4 bu sayının çarpanıdır, 50'den küçüktür", 27)


def zaman():
    x0, u, y = 30, 7, 70
    ic = f'<line x1="{x0}" y1="{y}" x2="{x0 + 60 * u}" y2="{y}" stroke="{LAC}" stroke-width="2"/>'
    for m in range(0, 61, 4):
        ic += f'<line x1="{x0 + m * u}" y1="{y - 4}" x2="{x0 + m * u}" y2="{y + 4}" stroke="{LAC}" stroke-width="1"/>'
    for m, s in [(0, '18.00'), (20, '18.20'), (40, '18.40'), (60, '19.00')]:
        ic += f'<line x1="{x0 + m * u}" y1="{y - 7}" x2="{x0 + m * u}" y2="{y + 7}" stroke="{LAC}" stroke-width="2"/>'
        ic += yazi(x0 + m * u, y + 24, s, 13)
    for m in (0, 12):                                   # fıskiye: su damlası
        cx = x0 + m * u
        ic += f'<path d="M{cx} {y - 50} C{cx + 9} {y - 38} {cx + 9} {y - 30} {cx} {y - 30} C{cx - 9} {y - 30} {cx - 9} {y - 38} {cx} {y - 50} Z" fill="{MAVI}"/>'
        ic += f'<line x1="{cx}" y1="{y - 27}" x2="{cx}" y2="{y - (31 if m == 0 else 9)}" stroke="{MAVI}" stroke-width="1.4" stroke-dasharray="3 2"/>'
    for m in (0, 8, 16):                                # ışık: yıldız (18.00'de damlanın altında, aynı dikeyde)
        cx, cy = x0 + m * u, y - 20
        ic += _yildiz(cx, cy, TUR)
        ic += f'<line x1="{cx}" y1="{cy + 9}" x2="{cx}" y2="{y - 9}" stroke="{TUR}" stroke-width="1.4" stroke-dasharray="3 2"/>'
    ic += _yildiz(x0 + 44 * u, 16, TUR) + yazi(x0 + 44 * u + 14, 21, 'ışık gösterisi', 13, LAC, 'start')
    ic += f'<path d="M{x0 + 44 * u} 30 C{x0 + 44 * u + 6} 38 {x0 + 44 * u + 6} 43 {x0 + 44 * u} 43 C{x0 + 44 * u - 6} 43 {x0 + 44 * u - 6} 38 {x0 + 44 * u} 30 Z" fill="{MAVI}"/>'
    ic += yazi(x0 + 44 * u + 14, 42, 'fıskiye', 13, LAC, 'start')
    return svg(x0 + 60 * u + 30, 100, ic, 'Zaman çizelgesi 18.00 ile 19.00 arası; fıskiye 18.00 ve 18.12 de, ışık gösterisi 18.00, 18.08 ve 18.16 da başlıyor', 24)


def _yildiz(cx, cy, renk):
    import math
    nok = []
    for k in range(10):
        r = 8 if k % 2 == 0 else 3.4
        a = -math.pi / 2 + k * math.pi / 5
        nok.append(f'{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(nok)}" fill="{renk}"/>'


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dikdortgenler()
    s[3]['gorsel'] = sayi_dogrusu()
    s[7]['gorsel'] = kartlar()
    s[8]['gorsel'] = kalemler()
    s[10]['gorsel'] = raflar()
    s[11]['gorsel'] = kilit()
    s[12]['gorsel'] = zaman()
