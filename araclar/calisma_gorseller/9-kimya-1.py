"""9. sınıf Kimya 1. hafta (kimya hayattır) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


SU = '#5aa9e6'


def satir_kartlari(kart, etiket, en_fazla):
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 4 + len(kart) * 29, ic, etiket, en_fazla)


def maddeler():
    ad = ['Limon tuzu', 'Antiasit tablet', 'Gazlı içecek', 'Sıvı sabun']
    ic = ''
    for i, a in enumerate(ad):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 80, '#fff', GRI, 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), LAC) + yazi(x0 + 42, 75, a, 9.8, LAC)
    c = [4 + i * 89 + 42 for i in range(4)]
    # 1 kavanoz + kristaller
    ic += f'<rect x="{c[0] - 12}" y="26" width="24" height="32" rx="4" fill="{GRI_A}" stroke="{SOLUK}" stroke-width="1.2"/><rect x="{c[0] - 10}" y="20" width="20" height="7" rx="2" fill="{ALTIN}"/>'
    ic += ''.join(f'<rect x="{c[0] - 8 + (k % 3) * 6}" y="{44 + (k // 3) * 6}" width="4" height="4" fill="#fff" stroke="{GRI}" stroke-width="0.7"/>' for k in range(6))
    # 2 tabletler
    ic += ''.join(f'<ellipse cx="{c[1] + dx}" cy="{dy}" rx="11" ry="6" fill="#fff" stroke="{CAM}" stroke-width="1.3"/><line x1="{c[1] + dx - 7}" y1="{dy}" x2="{c[1] + dx + 7}" y2="{dy}" stroke="{CAM}" stroke-width="1"/>' for dx, dy in [(-10, 34), (12, 40), (-4, 52)])
    # 3 kutu içecek
    ic += f'<rect x="{c[2] - 10}" y="22" width="20" height="38" rx="4" fill="{KIR}"/><rect x="{c[2] - 10}" y="34" width="20" height="10" fill="#fff"/><ellipse cx="{c[2]}" cy="22" rx="10" ry="2.5" fill="{GRI}"/>'
    ic += ''.join(f'<circle cx="{c[2] + dx}" cy="{dy}" r="1.8" fill="none" stroke="{KIR}" stroke-width="0.9"/>' for dx, dy in [(18, 30), (22, 22), (17, 16)])
    # 4 pompalı şişe
    ic += f'<rect x="{c[3] - 11}" y="34" width="22" height="26" rx="5" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.3"/><rect x="{c[3] - 3}" y="24" width="6" height="10" fill="{MAVI}"/><path d="M{c[3] - 3} 24 H{c[3] + 12} v4" fill="none" stroke="{MAVI}" stroke-width="3"/>'
    return svg(360, 88, ic, 'Maddeler: 1 limon tuzu, 2 antiasit tablet, 3 gazlı içecek, 4 sıvı sabun', 22)


def sos_tablosu():
    sat = [('A', '6,12', '0,047'), ('B', '5,23', '0,125'), ('C', '6,07', '0,058')]
    ic = kutu(4, 4, 352, 84, '#fff', MAVI, 6, 1.3) + f'<rect x="4" y="4" width="352" height="24" rx="6" fill="{MAVI_A}"/>'
    ic += yazi(32, 20, 'Sos', 11, LAC) + yazi(108, 20, 'Sosun pH değeri', 11, LAC) + yazi(256, 20, 'Biriken alüminyum (mg/100 g)', 11, LAC)
    ic += f'<line x1="60" y1="4" x2="60" y2="88" stroke="{MAVI}" stroke-width="0.8"/><line x1="160" y1="4" x2="160" y2="88" stroke="{MAVI}" stroke-width="0.8"/>'
    for k, (a, b, c) in enumerate(sat):
        y = 28 + k * 20
        ic += f'<line x1="4" y1="{y}" x2="356" y2="{y}" stroke="{MAVI}" stroke-width="0.8"/>' + yazi(32, y + 14, a, 11.5, LAC) + yazi(108, y + 14, b, 11.5, LAC, 'middle', True) + yazi(256, y + 14, c, 11.5, LAC, 'middle', True)
    return svg(360, 92, ic, 'Tablo: A sosu pH 6,12, biriken alüminyum 0,047; B sosu pH 5,23, biriken alüminyum 0,125; C sosu pH 6,07, biriken alüminyum 0,058 mg/100 g', 24)


def grafik():
    x0, y0, h = 70, 96, 70
    ic = f'<line x1="{x0}" y1="{y0 - h - 6}" x2="{x0}" y2="{y0}" stroke="{LAC}" stroke-width="1.3"/><line x1="{x0}" y1="{y0}" x2="330" y2="{y0}" stroke="{LAC}" stroke-width="1.3"/>'
    for v in (0.02, 0.04, 0.06):
        y = y0 - v / 0.07 * h
        ic += f'<line x1="{x0}" y1="{y:.1f}" x2="330" y2="{y:.1f}" stroke="{GRI}" stroke-width="0.6" stroke-dasharray="3 3"/>' + yazi(x0 - 5, y + 4, f'{v:.2f}'.replace('.', ','), 10, SOLUK, 'end', True)
    for x, v, ad in [(130, 0.051, '150 °C'), (240, 0.062, '250 °C')]:
        bh = v / 0.07 * h
        ic += f'<rect x="{x}" y="{y0 - bh:.1f}" width="46" height="{bh:.1f}" fill="{TUR}"/>' + yazi(x + 23, y0 - bh - 4, f'{v:.3f}'.replace('.', ','), 11, LAC) + yazi(x + 23, y0 + 13, ad, 11, LAC)
    ic += yazi(200, 12, 'A sosuyla pişirilen yiyecekte biriken alüminyum (mg/100 g)', 10.5, LAC)
    return svg(360, 114, ic, 'Sütun grafiği: A sosuyla pişirilen yiyecekte biriken alüminyum 150 °C’de 0,051, 250 °C’de 0,062 mg/100 g', 28)


def calisma_kartlari():
    return satir_kartlari([('A', 'Yakıt yanarken enerjinin nasıl dönüştüğünü incelemek', KIR, KIR_A),
                           ('B', 'İçme suyundaki maddelerin türünü ve miktarını bulmak', MAVI, MAVI_A),
                           ('C', 'Kauçukların ve yapıştırıcıların yapısını incelemek', TUR, TUR_A),
                           ('D', 'Vitaminlerin ve hormonların yapısını incelemek', YES, YES_A)],
                          'Kartlar: A Yakıt yanarken enerjinin nasıl dönüştüğünü incelemek. B İçme suyundaki maddelerin türünü ve miktarını bulmak. C Kauçukların ve yapıştırıcıların yapısını incelemek. D Vitaminlerin ve hormonların yapısını incelemek.', 33)


def cevre():
    ad = ['Atık yönetimi', 'Su arıtma', 'Yeşil teknolojiler']
    ic = ''
    for i, a in enumerate(ad):
        x0 = 4 + i * 119
        ic += kutu(x0, 4, 114, 70, YES_A, YES, 8, 1.2) + yazi(x0 + 57, 65, a, 11, LAC)
    ic += f'<path d="M48 26 h26 l-3 26 h-20 Z" fill="{SOLUK}"/><rect x="45" y="21" width="32" height="5" rx="2" fill="{LAC}"/><rect x="56" y="17" width="10" height="4" rx="1" fill="{LAC}"/>' + ''.join(f'<line x1="{55 + k * 6}" y1="31" x2="{56 + k * 5}" y2="47" stroke="#fff" stroke-width="1.4"/>' for k in range(3))
    ic += f'<path d="M180 16 c10 12 15 18 15 25 a15 15 0 0 1 -30 0 c0 -7 5 -13 15 -25 Z" fill="{SU}"/><path d="M172 42 a8 8 0 0 0 8 8" fill="none" stroke="#fff" stroke-width="1.6"/>'
    ic += f'<path d="M282 50 c-2 -22 12 -32 34 -32 c0 22 -10 34 -34 32 Z" fill="{YES}"/><path d="M284 50 q12 -14 26 -26" fill="none" stroke="#fff" stroke-width="1.4"/>'
    return svg(360, 78, ic, 'Çalışmalar: atık yönetimi, su arıtma, yeşil teknolojiler', 18)


def yemekler():
    ic = ''
    for i, (ph, sic, c, d) in enumerate([('5,2', '250 °C', KIR, KIR_A), ('6,1', '150 °C', MAVI, MAVI_A)]):
        x = 4 + i * 180
        ic += kutu(x, 4, 172, 68, d, c, 8, 1.3) + f'<rect x="{x}" y="4" width="172" height="20" rx="8" fill="{c}"/><rect x="{x}" y="14" width="172" height="10" fill="{c}"/>' + yazi(x + 86, 19, f'{i + 1}. yemek', 11.5, '#fff')
        ic += yazi(x + 12, 42, f'Sosun pH değeri: {ph}', 11.5, LAC, 'start', True) + yazi(x + 12, 60, f'Pişirme sıcaklığı: {sic}', 11.5, LAC, 'start', True)
    return svg(360, 76, ic, '1. yemek: sosun pH değeri 5,2, pişirme sıcaklığı 250 °C. 2. yemek: sosun pH değeri 6,1, pişirme sıcaklığı 150 °C.', 19)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = maddeler()
    s[2]['gorsel'] = sos_tablosu()
    s[3]['gorsel'] = grafik()
    s[5]['gorsel'] = calisma_kartlari()
    s[9]['gorsel'] = cevre()
    s[11]['gorsel'] = yemekler()
