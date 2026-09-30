"""7. sınıf Matematik 1. hafta çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
EKSI = '−'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def kesir(x, y, pay, payda, renk=LAC, boy=14, isaret=''):
    """Pay üstte, payda altta; (x, y) kesir çizgisinin ortası."""
    g = max(len(pay), len(payda)) * boy * 0.62 + 6
    ic = yazi(x - g / 2 - 2, y + boy * 0.35, isaret, boy, renk, 'end') if isaret else ''
    ic += yazi(x, y - 3, pay, boy, renk)
    ic += f'<line x1="{x - g / 2:.1f}" y1="{y}" x2="{x + g / 2:.1f}" y2="{y}" stroke="{renk}" stroke-width="1.5"/>'
    return ic + yazi(x, y + boy + 1, payda, boy, renk)


def ok_tanim(kimlik, renk=LAC):
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" fill="{renk}"/></marker>')


def isaretli(n):
    return f'{EKSI}{-n}' if n < 0 else str(n)


def termometre():
    u, y0, x = 6, 22, 58
    Y = lambda v: y0 + (10 - v) * u
    ic = yazi(x, 12, '°C', 12, LAC)
    ic += f'<rect x="{x - 7}" y="{Y(10) - 6}" width="14" height="{Y(-10) - Y(10) + 18}" rx="7" fill="#fff" stroke="{GRI}" stroke-width="1.6"/>'
    ic += f'<rect x="{x - 3}" y="{Y(-10) + 2}" width="6" height="14" fill="{KIR}"/>'
    ic += f'<circle cx="{x}" cy="{Y(-10) + 24}" r="12" fill="{KIR}" stroke="#a32323" stroke-width="1.4"/>'
    for v in range(-10, 11):
        uzun = v % 5 == 0
        ic += f'<line x1="{x - 8 - (9 if uzun else 5)}" y1="{Y(v)}" x2="{x - 8}" y2="{Y(v)}" stroke="{LAC}" stroke-width="{1.6 if uzun else 1}"/>'
        if uzun:
            ic += yazi(x - 21, Y(v) + 4.5, '0' if v == 0 else (f'+{v}' if v > 0 else isaretli(v)), 12, LAC, 'end')
    for v, saat in [(5, '14.00'), (0, '10.00'), (-6, '06.00')]:
        ic += f'<line x1="{x + 10}" y1="{Y(v)}" x2="{x + 40}" y2="{Y(v)}" stroke="{MAVI}" stroke-width="1.6" marker-start="url(#ck7ok1)"/>'
        ic += yazi(x + 45, Y(v) + 4.5, saat, 13, MAVI, 'start')
    ic = f'<defs>{ok_tanim("ck7ok1", MAVI)}</defs>' + ic
    return svg(150, Y(-10) + 40, ic, 'Termometre −10 ile +10 °C arası; 14.00 okuması +5, 10.00 okuması 0, 06.00 okuması −6 çizgisinde', 36)


def otel():
    h, x0, w, yz = 15, 78, 150, 124
    ic = f'<rect x="0" y="{yz}" width="262" height="{2 * h + 8}" fill="#efe3d3"/>'
    for f in range(-2, 7):
        y = yz - (f + 1) * h if f >= 0 else yz + (-f - 1) * h
        ustte = f >= 0
        ic += f'<rect x="{x0}" y="{y}" width="{w}" height="{h}" fill="{MAVI_A if ustte else GRI_A}" stroke="{MAVI if ustte else GRI}" stroke-width="1.3"/>'
        ic += yazi(x0 - 12, y + 11, isaretli(f), 12, LAC, 'end')
        if ustte and f != 0:
            ic += ''.join(f'<rect x="{x0 + 10 + i * 22}" y="{y + 4}" width="12" height="7" rx="1" fill="#fff" stroke="{MAVI}" stroke-width=".8"/>' for i in range(5))
    ic += f'<rect x="{x0 + w - 26}" y="{yz - 7 * h}" width="18" height="{9 * h}" fill="#dfe5f2" stroke="{GRI}" stroke-width="1"/>'
    ic += f'<rect x="{x0 + w - 24}" y="{yz - h + 2}" width="14" height="{h - 4}" rx="2" fill="{TUR}"/>'
    ic += f'<rect x="{x0 - 4}" y="{yz - 7 * h - 5}" width="{w + 8}" height="5" fill="{LAC}"/>'
    ic += f'<line x1="0" y1="{yz}" x2="262" y2="{yz}" stroke="#8a5a2b" stroke-width="2"/>'
    ic += yazi(x0 + 12, yz - 4, 'Lobi', 11.5, LAC, 'start')
    yh = yz + h
    ic += ''.join(f'<path d="M{x0 + 10 + k * 16} {yh + 7 + j * 4} q4 -3 8 0 t8 0" fill="none" stroke="{MAVI}" stroke-width="1.3"/>' for k in range(2) for j in range(2))
    ic += yazi(x0 + 48, yh + 11, 'Havuz', 11.5, LAC, 'start')
    ic += yazi(x0 - 30, yz - 7 * h - 9, 'Kat', 11, '#5b6479', 'middle')
    return svg(262, yz + 2 * h + 8, ic, 'Otelin katları −2 ile 6 arası numaralı; lobi 0. katta, havuz −2. katta; asansör boşluğu sağda', 30)


def dogru_k():
    x0, a, y = 24, 30, 40
    ic = f'<defs>{ok_tanim("ck7ok2")}</defs>'
    ic += f'<line x1="{x0 - 16}" y1="{y}" x2="{x0 + 10 * a + 18}" y2="{y}" stroke="{LAC}" stroke-width="2" marker-start="url(#ck7ok2)" marker-end="url(#ck7ok2)"/>'
    for i in range(11):
        ic += f'<line x1="{x0 + i * a}" y1="{y - 6}" x2="{x0 + i * a}" y2="{y + 6}" stroke="{LAC}" stroke-width="1.6"/>'
    ic += yazi(x0, y + 26, f'{EKSI}8', 14) + yazi(x0 + 6 * a, y + 26, '10', 14)
    ic += f'<circle cx="{x0 + 2 * a}" cy="{y}" r="6" fill="{TUR}"/>' + yazi(x0 + 2 * a, y - 14, 'K', 15, TUR)
    return svg(x0 + 10 * a + 26, 74, ic, 'Eşit aralıklı sayı doğrusu; ilk çizgi −8, yedinci çizgi 10; K noktası üçüncü çizgide', 20)


def taslar():
    liste = [('k', '5', '9', ''), ('t', f'{EKSI}12'), ('k', '0', '4', ''), ('k', '9', '0', ''), ('k', '7', '3', EKSI), ('k', '4', 'k', '')]
    renk = [(TUR_A, TUR), (MAVI_A, MAVI), (YES_A, YES)]
    ic = ''
    for i, t in enumerate(liste):
        cx, cy = 32 + i * 60, 34
        d, c = renk[i % 3]
        ic += f'<circle cx="{cx}" cy="{cy}" r="26" fill="{d}" stroke="{c}" stroke-width="1.8"/>'
        if t[0] == 't':
            ic += yazi(cx, cy + 5, t[1], 15)
        else:
            ic += kesir(cx + (4 if t[3] else 0), cy - 3, t[1], t[2], LAC, 14, t[3])
    return svg(364, 68, ic, 'Altı sayı taşı: 5 bölü 9, −12, 0 bölü 4, 9 bölü 0, eksi 7 bölü 3, 4 bölü k', 20)


def kartlar_denk():
    liste = [('2', '5', ''), ('1', '2', EKSI), ('9', '12', ''), ('6', '15', ''), ('3', f'{EKSI}6', ''), ('3', '4', ''), ('4', '10', ''), ('4', '8', EKSI)]
    ic = ''
    for i, (p, q, s) in enumerate(liste):
        x = 4 + i * 48
        ic += f'<rect x="{x}" y="4" width="42" height="58" rx="6" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
        ic += kesir(x + 21 + (4 if s else 0), 32, p, q, LAC, 14, s)
    return svg(4 + 8 * 48, 66, ic, 'Sekiz kart: 2 bölü 5, eksi 1 bölü 2, 9 bölü 12, 6 bölü 15, 3 bölü eksi 6, 3 bölü 4, 4 bölü 10, eksi 4 bölü 8', 20)


def dogru_a():
    x0, b, y = 26, 78, 44
    ic = f'<defs>{ok_tanim("ck7ok3")}</defs>'
    ic += f'<line x1="{x0 - 16}" y1="{y}" x2="{x0 + 4 * b + 18}" y2="{y}" stroke="{LAC}" stroke-width="2" marker-start="url(#ck7ok3)" marker-end="url(#ck7ok3)"/>'
    for i in range(13):
        x = x0 + i * b / 3
        tam = i % 3 == 0
        ic += f'<line x1="{x:.1f}" y1="{y - (8 if tam else 5)}" x2="{x:.1f}" y2="{y + (8 if tam else 5)}" stroke="{LAC}" stroke-width="{1.8 if tam else 1.1}"/>'
        if tam:
            ic += yazi(x, y + 28, isaretli(i // 3 - 3), 14)
    xa = x0 + 4 * b / 3
    ic += f'<circle cx="{xa:.1f}" cy="{y}" r="6" fill="{TUR}"/>' + yazi(xa, y - 15, 'A', 15, TUR)
    return svg(x0 + 4 * b + 28, 80, ic, 'Sayı doğrusu −3 ile 1 arası; her birim 3 eş parçaya bölünmüş; A noktası −2 ile −1 arasında, −2 den sonraki birinci çizgide', 21)


def ekmekler():
    ic = ''
    for i, (h, fark, c) in enumerate([('A', '+6 g', MAVI), ('B', f'{EKSI}9 g', TUR), ('C', f'{EKSI}4 g', YES), ('Ç', '+7 g', MOR)]):
        cx = 46 + i * 90
        ic += f'<ellipse cx="{cx}" cy="28" rx="36" ry="17" fill="#e2a55a" stroke="#9a5b1f" stroke-width="1.6"/>'
        ic += ''.join(f'<path d="M{cx - 16 + k * 14} 20 l8 12" stroke="#f6d39d" stroke-width="2.4" stroke-linecap="round"/>' for k in range(3))
        ic += f'<circle cx="{cx - 22}" cy="66" r="10" fill="{c}"/>' + yazi(cx - 22, 70.5, h, 12, '#fff')
        ic += yazi(cx - 8, 71, fark, 15, LAC, 'start')
    return svg(360, 82, ic, 'Dört ekmek ve hedeften farkları: A +6 g, B −9 g, C −4 g, Ç +7 g', 21)


def kumeler():
    ic = f'<rect x="8" y="6" width="344" height="156" rx="16" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.8"/>'
    ic += yazi(22, 25, 'Rasyonel sayılar', 12.5, MOR, 'start')
    ic += f'<rect x="30" y="36" width="256" height="116" rx="14" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(44, 55, 'Tam sayılar', 12.5, MAVI, 'start')
    ic += f'<rect x="52" y="68" width="150" height="72" rx="12" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(64, 88, 'Doğal sayılar', 12.5, '#0c7a3c', 'start')
    for x, y, r in [(176, 118, 'I'), (246, 104, 'II'), (320, 104, 'III')]:
        ic += f'<circle cx="{x}" cy="{y}" r="13" fill="{LAC}"/>' + yazi(x, y + 4.5, r, 12, '#fff')
    return svg(360, 168, ic, 'İç içe üç küme: en içte doğal sayılar (I), ortada tam sayılar (II), en dışta rasyonel sayılar (III)', 27)


def hazine():
    x0, a, y = 30, 26, 56
    X = lambda n: x0 + (n + 6) * a
    ic = f'<defs>{ok_tanim("ck7ok4")}</defs>'
    ic += f'<rect x="{x0 - 16}" y="{y - 7}" width="{12 * a + 32}" height="14" rx="7" fill="#f3e2c3"/>'
    ic += f'<line x1="{x0 - 16}" y1="{y}" x2="{x0 + 12 * a + 18}" y2="{y}" stroke="{LAC}" stroke-width="2" marker-start="url(#ck7ok4)" marker-end="url(#ck7ok4)"/>'
    for n in range(-6, 7):
        ic += f'<line x1="{X(n)}" y1="{y - 6}" x2="{X(n)}" y2="{y + 6}" stroke="{LAC}" stroke-width="1.5"/>'
        ic += yazi(X(n), y + 24, isaretli(n), 12.5)
    xa = X(0)
    ic += f'<rect x="{xa - 2.5}" y="{y - 22}" width="5" height="14" fill="#8a5a2b"/><circle cx="{xa}" cy="{y - 30}" r="11" fill="{YES}"/>'
    ic += yazi(xa + 14, y - 34, 'Ağaç', 12, '#0c7a3c', 'start')
    xk = X(-1)
    ic += f'<rect x="{xk - 9}" y="{y - 22}" width="18" height="14" fill="{GRI}" stroke="#6b768c" stroke-width="1.2"/>'
    ic += f'<ellipse cx="{xk}" cy="{y - 22}" rx="9" ry="3.5" fill="#44506a"/>'
    ic += f'<path d="M{xk - 9} {y - 22} V{y - 36} H{xk + 9} V{y - 22}" fill="none" stroke="#8a5a2b" stroke-width="1.6"/>'
    ic += yazi(xk - 14, y - 26, 'Kuyu', 12, '#44506a', 'end')
    return svg(x0 + 12 * a + 30, y + 32, ic, 'Patika sayı doğrusu −6 ile 6 arası; ağaç 0 noktasında, kuyu −1 noktasında', 24)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = termometre()
    s[2]['gorsel'] = otel()
    s[3]['gorsel'] = dogru_k()
    s[5]['gorsel'] = taslar()
    s[7]['gorsel'] = kartlar_denk()
    s[8]['gorsel'] = dogru_a()
    s[10]['gorsel'] = ekmekler()
    s[11]['gorsel'] = kumeler()
    s[12]['gorsel'] = hazine()
