"""10. sınıf Biyoloji 1. hafta (enerji ve ATP) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def cokgen(cx, cy, r, n, dolgu, cizgi, don=-90):
    p = ' '.join(f'{cx + r * math.cos(math.radians(don + k * 360 / n)):.1f},{cy + r * math.sin(math.radians(don + k * 360 / n)):.1f}' for k in range(n))
    return f'<polygon points="{p}" fill="{dolgu}" stroke="{cizgi}" stroke-width="1.4"/>'


def molekul(x, y, fosfat, b=1.0):
    """Adenin (çift halka) + riboz (beşgen) + fosfat daireleri; harf yok."""
    ic = cokgen(x, y, 11 * b, 6, MAVI_A, MAVI) + cokgen(x + 17 * b, y - 5 * b, 8 * b, 5, MAVI_A, MAVI, -18)
    rx = x + 17 * b
    ic += f'<line x1="{rx:.1f}" y1="{y + 3 * b:.1f}" x2="{rx:.1f}" y2="{y + 12 * b:.1f}" stroke="{SOLUK}" stroke-width="1.4"/>' + cokgen(rx, y + 22 * b, 10 * b, 5, YES_A, YES)
    px = rx + 9 * b
    for k in range(fosfat):
        cx = rx + (24 + k * 22) * b
        ic += f'<line x1="{px:.1f}" y1="{y + 22 * b:.1f}" x2="{cx - 8 * b:.1f}" y2="{y + 22 * b:.1f}" stroke="{SOLUK}" stroke-width="1.4"/><circle cx="{cx:.1f}" cy="{y + 22 * b:.1f}" r="{8 * b:.1f}" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
        px = cx + 8 * b
    return ic


def atp():
    ic = molekul(110, 34, 3, 1.5)
    ic += f'<line x1="70" y1="20" x2="94" y2="28" stroke="{LAC}" stroke-width="1"/>' + rozet(62, 18, '1', LAC)
    ic += f'<line x1="120" y1="98" x2="132" y2="80" stroke="{LAC}" stroke-width="1"/>' + rozet(116, 104, '2', LAC)
    ic += f'<path d="M158 44 v-6 h92 v6" fill="none" stroke="{LAC}" stroke-width="1"/><line x1="204" y1="38" x2="204" y2="30" stroke="{LAC}" stroke-width="1"/>' + rozet(204, 22, '3', LAC)
    return svg(360, 116, ic, 'ATP molekülü şeması: 1 çift halkalı baz, 2 beşgen şeker, 3 art arda bağlı üç daire', 27)


def molekuller():
    ic = ''
    for i, (h, f) in enumerate([('A', 1), ('B', 3), ('C', 0), ('D', 2)]):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 56
        ic += kutu(x, y, 172, 50, '#fff', GRI, 8, 1.2) + rozet(x + 15, y + 14, h, LAC) + molekul(x + 52, y + 17, f, 0.9)
    return svg(360, 114, ic, 'Dört molekül şeması: A baz, şeker ve bir fosfat; B baz, şeker ve üç fosfat; C baz ve şeker; D baz, şeker ve iki fosfat', 28)


def alt_yazi(x, y, boy=13):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{boy}" {YAZI} fill="{LAC}">ADP + P<tspan dy="3" font-size="{boy * 0.7:.1f}">i</tspan><tspan dy="-3"> + enerji  →  ATP + H</tspan>'
            f'<tspan dy="3" font-size="{boy * 0.7:.1f}">2</tspan><tspan dy="-3">O</tspan></text>')


def tepkime():
    ic = kutu(4, 4, 352, 36, TUR_A, TUR, 8, 1.4) + alt_yazi(180, 27)
    return svg(360, 44, ic, 'Tepkime: ADP + Pi + enerji → ATP + H2O', 11)


def dongu():
    ic = kutu(140, 6, 80, 28, TUR_A, TUR, 14, 1.5) + yazi(180, 25, 'ATP', 13, LAC)
    ic += kutu(130, 88, 100, 28, MAVI_A, MAVI, 14, 1.5) + f'<text x="180" y="107" text-anchor="middle" font-size="13" {YAZI} fill="{LAC}">ADP + P<tspan dy="3" font-size="9">i</tspan></text>'
    ic += f'<path d="M128 100 Q84 62 134 24" fill="none" stroke="{YES}" stroke-width="2.4"/><polygon points="138,20 126,22 132,31" fill="{YES}"/>' + rozet(100, 62, '1', YES)
    ic += f'<path d="M226 24 Q276 62 236 98" fill="none" stroke="{KIR}" stroke-width="2.4"/><polygon points="232,103 233,91 243,97" fill="{KIR}"/>' + rozet(260, 62, '2', KIR)
    ic += yazi(44, 58, 'Besinlerdeki', 10.5, LAC) + yazi(44, 71, 'enerji', 10.5, LAC) + ok(72, 62, 88, 62, YES, 1.8)
    ic += ok(272, 62, 288, 62, KIR, 1.8) + yazi(322, 52, 'Hücre', 10.5, LAC) + yazi(322, 65, 'faaliyetleri', 10.5, LAC) + yazi(322, 78, 'için enerji', 10.5, LAC)
    return svg(360, 122, ic, 'ATP döngüsü: 1 numaralı okla besinlerdeki enerji kullanılarak ADP ve Pi’den ATP oluşur; 2 numaralı okla ATP, ADP ve Pi’ye dönüşür ve hücre faaliyetleri için enerji çıkar', 28)


def mevsimler():
    ic = ''
    for i, (b, m, c, d) in enumerate([('Sonbahar', 'Bol besin bulur.', TUR, TUR_A), ('Kış', 'Besin bulamaz, uyur.', MAVI, MAVI_A)]):
        x = 4 + i * 190
        ic += kutu(x, 4, 162, 46, d, c, 8, 1.3) + yazi(x + 81, 22, b, 12, c) + yazi(x + 81, 40, m, 11, LAC, 'middle', True)
    ic += ok(170, 27, 192, 27)
    return svg(360, 54, ic, 'Kirpi: sonbaharda bol besin bulur; kışın besin bulamaz, uyur.', 13)


def hucreler():
    ic = ''
    for i, n in enumerate([3, 1]):
        x = 10 + i * 210
        ic += f'<rect x="{x}" y="6" width="130" height="66" rx="30" fill="{YES_A}" stroke="{YES}" stroke-width="2"/>' + yazi(x + 65, 88, f'{i + 1}. hücre', 11, LAC)
        for k in range(n):
            ic += kutu(x + 14 + k * 36, 28, 30, 20, TUR_A, TUR, 6, 1.2) + yazi(x + 29 + k * 36, 42, 'ATP', 9.5, LAC)
    ic += ok(146, 39, 214, 39, KIR, 2) + yazi(180, 30, '?', 15, KIR)
    return svg(360, 94, ic, 'İki komşu hücre: 1. hücrede üç ATP, 2. hücrede bir ATP; aradaki okun üstünde soru işareti', 21)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = atp()
    s[2]['gorsel'] = molekuller()
    s[3]['gorsel'] = tepkime()
    s[7]['gorsel'] = dongu()
    s[9]['gorsel'] = mevsimler()
    s[11]['gorsel'] = hucreler()
