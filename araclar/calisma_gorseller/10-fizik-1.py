"""10. sınıf Fizik 1. hafta (sabit hızlı hareket) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


KUM, YAPRAK = '#f0dfb8', '#2f9e55'


def cizelge(bas, sat, en, etiket, en_fazla, boy=11):
    """Basit tablo: bas = başlıklar, sat = satırlar, en = sütun sınırlarının x değerleri."""
    H = 24 + 20 * len(sat)
    ic = kutu(4, 4, 352, H, '#fff', MAVI, 6, 1.3) + f'<rect x="4" y="4" width="352" height="24" rx="6" fill="{MAVI_A}"/>'
    sinir = [4] + en + [356]
    ic += ''.join(f'<line x1="{x}" y1="4" x2="{x}" y2="{4 + H}" stroke="{MAVI}" stroke-width="0.8"/>' for x in en)
    ic += ''.join(yazi((sinir[k] + sinir[k + 1]) / 2, 20, b, boy, LAC) for k, b in enumerate(bas))
    for r, s in enumerate(sat):
        y = 28 + r * 20
        ic += f'<line x1="4" y1="{y}" x2="356" y2="{y}" stroke="{MAVI}" stroke-width="0.8"/>' + ''.join(yazi((sinir[k] + sinir[k + 1]) / 2, y + 14, h, boy, LAC, 'middle', True) for k, h in enumerate(s))
    return svg(360, H + 8, ic, etiket, en_fazla)


def eksen(xa, ya, xt, yt, dx, dy):
    """Eksenler: xa, ya = eksen adları; xt, yt = çentik etiketleri; dx, dy = çentik aralığı (px). Başlangıç (60, 96)."""
    X, Y = 60, 96
    ic = f'<line x1="{X}" y1="{Y}" x2="{X + dx * len(xt) + 14}" y2="{Y}" stroke="{LAC}" stroke-width="1.3"/><line x1="{X}" y1="{Y}" x2="{X}" y2="{Y - dy * len(yt) - 12}" stroke="{LAC}" stroke-width="1.3"/>'
    for n, e in enumerate(xt, 1):
        ic += f'<line x1="{X + n * dx}" y1="{Y}" x2="{X + n * dx}" y2="{Y - dy * len(yt)}" stroke="{GRI}" stroke-width="0.5" stroke-dasharray="3 3"/>' + yazi(X + n * dx, Y + 12, e, 10, LAC, 'middle', True)
    for n, e in enumerate(yt, 1):
        ic += f'<line x1="{X}" y1="{Y - n * dy}" x2="{X + dx * len(xt)}" y2="{Y - n * dy}" stroke="{GRI}" stroke-width="0.5" stroke-dasharray="3 3"/>' + yazi(X - 5, Y - n * dy + 3.5, e, 10, LAC, 'end', True)
    ic += yazi(X - 5, Y + 12, '0', 10, LAC, 'end', True) + yazi(X + dx * len(xt) + 18, Y + 12, xa, 10, LAC, 'start') + yazi(X, Y - dy * len(yt) - 16, ya, 10, LAC)
    return ic


def konum_tablosu():
    return cizelge(['Zaman (s)', '0', '1', '2', '3', '4'], [['C aracının konumu (m)', '0', '4', '8', '12', '16'], ['D aracının konumu (m)', '0', '6', '12', '18', '24']], [146, 188, 230, 272, 314],
                   'Tablo: zaman 0, 1, 2, 3, 4 s; C aracının konumu 0, 4, 8, 12, 16 m; D aracının konumu 0, 6, 12, 18, 24 m', 18, 10.5)


def xt1():
    ic = eksen('Zaman (s)', 'Konum (m)', ['1', '2', '3', '4'], ['5', '10', '15', '20'], 50, 17)
    ic += f'<line x1="60" y1="96" x2="260" y2="28" stroke="{KIR}" stroke-width="2.2"/><circle cx="260" cy="28" r="2.6" fill="{KIR}"/>'
    return svg(360, 114, ic, 'Konum-zaman grafiği: başlangıçtan 4. saniyede 20 m konumuna uzanan doğru', 28)


def vt():
    ic = eksen('Zaman (s)', 'Hız (m/s)', ['1', '2', '3', '4', '5'], ['4', '8'], 42, 28)
    ic += f'<line x1="60" y1="40" x2="270" y2="40" stroke="{KIR}" stroke-width="2.2"/>'
    return svg(360, 114, ic, 'Hız-zaman grafiği: 0 ile 5 s arasında hız 8 m/s değerinde yatay çizgi', 28)


def bant():
    ic = f'<path d="M20 30 H250 A40 40 0 0 1 290 70 V104" fill="none" stroke="{SOLUK}" stroke-width="22" stroke-linecap="butt"/>'
    ic += f'<path d="M20 30 H250 A40 40 0 0 1 290 70 V104" fill="none" stroke="#fff" stroke-width="1.2" stroke-dasharray="6 6"/>'
    ic += f'<rect x="60" y="21" width="30" height="18" rx="3" fill="{TUR}" stroke="{KAHVE}" stroke-width="1"/>' + ok(96, 30, 126, 30, '#fff', 2)
    ic += rozet(170, 58, '1', LAC) + f'<line x1="170" y1="49" x2="170" y2="42" stroke="{LAC}" stroke-width="1"/>' + rozet(246, 74, '2', LAC) + f'<line x1="253" y1="68" x2="270" y2="50" stroke="{LAC}" stroke-width="1"/>'
    return svg(360, 108, ic, 'Taşıyıcı bant: 1 numaralı düz bölüm ve 2 numaralı kıvrımlı bölüm; valiz düz bölümde ilerliyor', 25)


def xt2():
    ic = eksen('Zaman (s)', 'Konum (m)', ['1', '2', '3', '4'], ['8', '16'], 50, 30)
    ic += f'<line x1="60" y1="96" x2="260" y2="36" stroke="{KIR}" stroke-width="2.2"/>' + yazi(270, 36, 'K', 12, KIR)
    ic += f'<line x1="60" y1="36" x2="260" y2="96" stroke="{MAVI}" stroke-width="2.2"/>' + yazi(252, 84, 'L', 12, MAVI)
    return svg(360, 114, ic, 'Konum-zaman grafiği: K doğrusu 0 m’den 16 m’ye yükselir, L doğrusu 16 m’den 0 m’ye iner', 28)


def araba(x, y, renk):
    return f'<rect x="{x - 11}" y="{y - 9}" width="22" height="9" rx="3" fill="{renk}"/><circle cx="{x - 6}" cy="{y}" r="3" fill="{LAC}"/><circle cx="{x + 6}" cy="{y}" r="3" fill="{LAC}"/>'


def sayi_dogrusu():
    x0, dx = 24, 19.5
    ic = f'<line x1="{x0 - 8}" y1="50" x2="{x0 + 16 * dx + 12}" y2="50" stroke="{LAC}" stroke-width="1.4"/>'
    for v in range(0, 17, 2):
        x = x0 + v * dx
        ic += f'<line x1="{x}" y1="46" x2="{x}" y2="54" stroke="{LAC}" stroke-width="1.2"/>' + yazi(x, 67, str(v), 10.5, LAC, 'middle', True)
    ic += yazi(x0 + 16 * dx + 18, 67, 'x (m)', 10, LAC, 'start')
    for v, e in ((2, 't = 0'), (14, 't = 4 s')):
        x = x0 + v * dx
        ic += araba(x, 44, TUR) + yazi(x, 24, e, 10.5, LAC)
    return svg(380, 74, ic, 'Sayı doğrusu (metre): araba t = 0 anında 2 m konumunda, t = 4 s anında 14 m konumunda', 17)


def vt_basamak():
    X, S = 60, 62  # S: sıfır hız çizgisi
    ic = f'<line x1="{X}" y1="{S}" x2="{X + 5 * 42 + 14}" y2="{S}" stroke="{LAC}" stroke-width="1.3"/><line x1="{X}" y1="96" x2="{X}" y2="16" stroke="{LAC}" stroke-width="1.3"/>'
    for n in range(1, 6):
        ic += f'<line x1="{X + n * 42}" y1="24" x2="{X + n * 42}" y2="90" stroke="{GRI}" stroke-width="0.5" stroke-dasharray="3 3"/>' + yazi(X + n * 42 - 6, S - 4, str(n), 10, LAC, 'middle', True)
    for v, y in (('4', 34), ('2', 48), ('−2', 76), ('−4', 90)):
        ic += f'<line x1="{X}" y1="{y}" x2="{X + 210}" y2="{y}" stroke="{GRI}" stroke-width="0.5" stroke-dasharray="3 3"/>' + yazi(X - 5, y + 3.5, v, 10, LAC, 'end', True)
    ic += yazi(X - 5, S + 3.5, '0', 10, LAC, 'end', True) + yazi(X + 228, S + 4, 'Zaman (s)', 10, LAC, 'start') + yazi(X, 10, 'Hız (m/s)', 10, LAC)
    ic += f'<line x1="{X}" y1="34" x2="{X + 126}" y2="34" stroke="{KIR}" stroke-width="2.2"/><line x1="{X + 126}" y1="76" x2="{X + 210}" y2="76" stroke="{KIR}" stroke-width="2.2"/>'
    return svg(360, 100, ic, 'Hız-zaman grafiği: 0 ile 3 s arasında hız 4 m/s, 3 ile 5 s arasında hız −2 m/s', 28)


def xt3():
    ic = eksen('Zaman (s)', 'Konum (m)', ['1', '2', '3', '4', '5', '6'], ['10', '20', '30'], 34, 20)
    ic += f'<line x1="60" y1="36" x2="264" y2="96" stroke="{MAVI}" stroke-width="2.2"/><circle cx="60" cy="36" r="2.6" fill="{MAVI}"/><circle cx="264" cy="96" r="2.6" fill="{MAVI}"/>' + yazi(150, 52, 'M', 12, MAVI)
    return svg(360, 114, ic, 'Konum-zaman grafiği: M aracı 0 s anında 30 m konumunda, 6. saniyede 0 konumunda; doğru aşağı iner', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = konum_tablosu()
    s[2]['gorsel'] = xt1()
    s[3]['gorsel'] = vt()
    s[5]['gorsel'] = bant()
    s[7]['gorsel'] = xt2()
    s[9]['gorsel'] = sayi_dogrusu()
    s[12]['gorsel'] = vt_basamak()
    s[13]['gorsel'] = xt3()
