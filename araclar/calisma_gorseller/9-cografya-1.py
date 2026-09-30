"""9. sınıf Coğrafya 1. hafta (coğrafyanın konusu ve bölümleri) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def ok(x1, y1, x2, y2, renk=GRI, kalin=1.8):
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2:.1f},{y2:.1f} {x2 - 7 * math.cos(a - 0.45):.1f},{y2 - 7 * math.sin(a - 0.45):.1f} {x2 - 7 * math.cos(a + 0.45):.1f},{y2 - 7 * math.sin(a + 0.45):.1f}'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/><polygon points="{u}" fill="{renk}"/>'


def yildiz(x, y, r, renk=ALTIN):
    p = ' '.join(f'{x + (r if k % 2 == 0 else r * 0.45) * math.cos(-math.pi / 2 + k * math.pi / 5):.1f},{y + (r if k % 2 == 0 else r * 0.45) * math.sin(-math.pi / 2 + k * math.pi / 5):.1f}' for k in range(10))
    return f'<polygon points="{p}" fill="{renk}"/>'


SU, YAPRAK, GOK = '#5aa9e6', '#2f9e55', '#dff1fd'


def agac(x, y, b=1.0):
    return f'<rect x="{x - 1.5 * b:.1f}" y="{y - 8 * b:.1f}" width="{3 * b:.1f}" height="{8 * b:.1f}" fill="{KAHVE}"/><path d="M{x:.1f} {y - 26 * b:.1f} L{x + 8 * b:.1f} {y - 7 * b:.1f} H{x - 8 * b:.1f} Z" fill="{YAPRAK}"/>'


def manzara():
    ic = f'<rect x="4" y="4" width="352" height="132" rx="8" fill="{GOK}"/>'
    # dağ (taş küre) ve zirvedeki buzul
    ic += f'<path d="M4 118 L96 28 L150 84 L196 52 L262 118 Z" fill="#9aa3b5"/>'
    ic += f'<path d="M96 28 L120 53 L108 49 L98 58 L88 49 L76 48 Z" fill="#fff"/>'
    # bulut (hava küre)
    ic += f'<ellipse cx="262" cy="34" rx="24" ry="10" fill="#fff"/><ellipse cx="248" cy="28" rx="12" ry="9" fill="#fff"/><ellipse cx="272" cy="26" rx="14" ry="10" fill="#fff"/>'
    # zemin, göl (su küre), ağaçlar (yaşam küre)
    ic += f'<path d="M4 112 Q120 100 200 112 T356 108 V128 a8 8 0 0 1 -8 8 H12 a8 8 0 0 1 -8 -8 Z" fill="#cfe8b9"/>'
    ic += f'<ellipse cx="216" cy="122" rx="52" ry="9" fill="{SU}"/>'
    ic += ''.join(agac(x, y, b) for x, y, b in [(296, 118, 1.0), (312, 124, 1.1), (330, 117, 0.9)])
    for no, x, y, px, py in [(1, 60, 22, 92, 40), (2, 312, 24, 284, 30), (3, 186, 96, 204, 118), (4, 28, 84, 56, 92), (5, 340, 84, 322, 100)]:
        ic += f'<line x1="{x}" y1="{y}" x2="{px}" y2="{py}" stroke="{LAC}" stroke-width="1"/>' + rozet(x, y, str(no), LAC)
    return svg(360, 140, ic, 'Manzara: 1 dağın zirvesindeki buzul, 2 bulutlu hava, 3 göl, 4 dağın kayalık yamacı, 5 ağaçlar', 34)


def unsurlar():
    ad = ['Göl', 'Köprü', 'Orman', 'Fabrika', 'Tepe', 'Yol']
    ic = ''
    for i, a in enumerate(ad):
        x0 = 4 + i * 59.5
        ic += kutu(x0, 4, 55, 66, '#fff', GRI, 7, 1.1) + yazi(x0 + 27.5, 62, a, 11, LAC)
    c = [4 + i * 59.5 + 27.5 for i in range(6)]
    ic += f'<ellipse cx="{c[0]}" cy="30" rx="19" ry="11" fill="{SU}"/><path d="M{c[0] - 10} 29 q4 -3 8 0 t8 0" fill="none" stroke="#fff" stroke-width="1.4"/>'
    ic += f'<path d="M{c[1] - 21} 40 V26 H{c[1] + 21} V40 M{c[1] - 12} 40 a12 12 0 0 1 24 0" fill="none" stroke="{SOLUK}" stroke-width="3"/><line x1="{c[1] - 23}" y1="24" x2="{c[1] + 23}" y2="24" stroke="{TUR}" stroke-width="3" stroke-linecap="round"/>'
    ic += agac(c[2] - 11, 44, 1.0) + agac(c[2] + 1, 47, 1.2) + agac(c[2] + 13, 44, 1.0)
    ic += f'<rect x="{c[3] - 18}" y="28" width="36" height="16" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.3"/><rect x="{c[3] + 6}" y="14" width="7" height="14" fill="{KIR}"/><path d="M{c[3] - 18} 28 l9 -7 v7 l9 -7 v7" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.3"/><circle cx="{c[3] + 14}" cy="10" r="3" fill="{GRI}"/>'
    ic += f'<path d="M{c[4] - 22} 46 Q{c[4]} 4 {c[4] + 22} 46 Z" fill="#a8cf8e"/>'
    ic += f'<path d="M{c[5] - 12} 46 L{c[5] - 4} 14 H{c[5] + 4} L{c[5] + 12} 46 Z" fill="{SOLUK}"/><line x1="{c[5]}" y1="18" x2="{c[5]}" y2="44" stroke="#fff" stroke-width="1.6" stroke-dasharray="5 4"/>'
    return svg(360, 74, ic, 'Altı unsur: göl, köprü, orman, fabrika, tepe, yol', 18)


def ortam_semasi():
    ic = kutu(4, 4, 352, 78, TUR_A, TUR, 10, 1.6, ' stroke-dasharray="5 3"') + yazi(180, 22, '?', 15, TUR)
    ic += kutu(16, 32, 150, 38, YES_A, YES, 8, 1.3) + yazi(91, 56, 'Doğal ortam', 12.5, LAC)
    ic += kutu(194, 32, 150, 38, MAVI_A, MAVI, 8, 1.3) + yazi(269, 56, 'Beşerî ortam', 12.5, LAC)
    ic += yazi(180, 57, '+', 17, SOLUK)
    return svg(360, 86, ic, 'Şema: doğal ortam ile beşerî ortam birlikte soru işaretiyle gösterilen en geniş alanı oluşturuyor', 20)


def konu_kartlari():
    kart = [('A', 'Bir ilde son on yılda nüfusun artışı', MOR, MOR_A),
            ('B', 'Bir kıyıdaki deniz akıntıları', MAVI, MAVI_A),
            ('C', 'Bir yörenin yemekleri ve müziği', TUR, TUR_A),
            ('D', 'Bir ovadaki sanayi ve ticaret', KIR, KIR_A)]
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 120, ic, 'Kartlar: A Bir ilde son on yılda nüfusun artışı. B Bir kıyıdaki deniz akıntıları. C Bir yörenin yemekleri ve müziği. D Bir ovadaki sanayi ve ticaret.', 33)


def soru_kartlari():
    s = ['Ne?', 'Nerede?', 'Ne zaman?', None, 'Neden önemli?']
    w = [40, 62, 78, 56, 104]
    ic, x = '', 4
    for a, g in zip(s, w):
        ic += kutu(x, 4, g, 28, '#fff' if a is None else MAVI_A, TUR if a is None else MAVI, 14, 1.4, ' stroke-dasharray="4 3"' if a is None else '')
        ic += yazi(x + g / 2, 22.5, a or '…', 11, LAC if a else TUR)
        x += g + 4
    return svg(360, 36, ic, 'Coğrafyanın soruları: Ne? Nerede? Ne zaman? (boş kart) Neden önemli?', 9)


def teras():
    ic = f'<rect x="4" y="4" width="352" height="92" rx="8" fill="{GOK}"/>'
    ic += f'<path d="M4 96 V84 L70 84 L70 70 L136 70 L136 56 L202 56 L202 42 L268 42 L268 28 L356 28 V88 a8 8 0 0 1 -8 8 Z" fill="#b08a5b"/>'
    for k in range(4):
        x, y = 8 + k * 66, 78 - k * 14
        ic += f'<rect x="{x}" y="{y}" width="58" height="6" fill="{SU}"/>' + ''.join(f'<path d="M{x + 6 + j * 9} {y + 1} v-8 m-2.5 3 l2.5 -3 l2.5 3" fill="none" stroke="{YAPRAK}" stroke-width="1.5"/>' for j in range(6))
    ic += f'<rect x="272" y="22" width="80" height="6" fill="{SU}"/>' + ''.join(f'<path d="M{280 + j * 9} 23 v-8 m-2.5 3 l2.5 -3 l2.5 3" fill="none" stroke="{YAPRAK}" stroke-width="1.5"/>' for j in range(8))
    return svg(360, 100, ic, 'Dağ yamacına basamak basamak yapılmış, su dolu pirinç tarlaları', 21)


def etkilesim():
    ic = f'<circle cx="70" cy="40" r="34" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>' + yazi(70, 45, 'Doğa', 13, LAC)
    ic += f'<circle cx="290" cy="40" r="34" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>' + yazi(290, 45, 'İnsan', 13, LAC)
    ic += ok(112, 26, 248, 26, YES, 2.2) + ok(248, 54, 112, 54, MAVI, 2.2) + rozet(180, 26, '1', YES) + rozet(180, 54, '2', MAVI)
    return svg(360, 80, ic, 'Etkileşim: 1 numaralı ok doğadan insana, 2 numaralı ok insandan doğaya', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = manzara()
    s[2]['gorsel'] = unsurlar()
    s[3]['gorsel'] = ortam_semasi()
    s[5]['gorsel'] = konu_kartlari()
    s[7]['gorsel'] = soru_kartlari()
    s[9]['gorsel'] = teras()
    s[11]['gorsel'] = etkilesim()
