"""9. sınıf Coğrafya 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12 birimlik yazı ≈ 8,5–9 pt.
"""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


class Duzlem:
    """x0..x1, y0..y1 aralığında birim kareli düzlem; (ox, oy) sol üst köşe, u birim boyu."""

    def __init__(self, x0, x1, y0, y1, u, ox, oy, xad='x', yad='y', adim=1, yadim=1, sayilar=True):
        self.x0, self.x1, self.y0, self.y1, self.u, self.ox, self.oy = x0, x1, y0, y1, u, ox, oy
        self.ux, self.uy = u / adim, u / yadim
        ic = ''
        for i in range(int(x0 / adim), int(x1 / adim) + 1):
            X = self.X(i * adim)
            ic += f'<line x1="{X:.1f}" y1="{self.Y(y0):.1f}" x2="{X:.1f}" y2="{self.Y(y1):.1f}" stroke="#dfe4ee" stroke-width="0.6"/>'
        for j in range(int(y0 / yadim), int(y1 / yadim) + 1):
            Y = self.Y(j * yadim)
            ic += f'<line x1="{self.X(x0):.1f}" y1="{Y:.1f}" x2="{self.X(x1):.1f}" y2="{Y:.1f}" stroke="#dfe4ee" stroke-width="0.6"/>'
        ic += (f'<line x1="{self.X(x0):.1f}" y1="{self.Y(0):.1f}" x2="{self.X(x1) + 10:.1f}" y2="{self.Y(0):.1f}" stroke="{LAC}" stroke-width="1"/>'
               f'<path d="M{self.X(x1) + 10:.1f} {self.Y(0):.1f} l-6 -3 v6 z" fill="{LAC}"/>'
               f'<line x1="{self.X(0):.1f}" y1="{self.Y(y0):.1f}" x2="{self.X(0):.1f}" y2="{self.Y(y1) - 10:.1f}" stroke="{LAC}" stroke-width="1"/>'
               f'<path d="M{self.X(0):.1f} {self.Y(y1) - 10:.1f} l-3 6 h6 z" fill="{LAC}"/>')
        ic += yazi(self.X(x1) + 10, self.Y(0) - 6, xad, 12, LAC, 'end', True)
        ic += yazi(self.X(0) + 7, self.Y(y1) - 4, yad, 12, LAC, 'start', True)
        if sayilar:
            for i in range(int(x0 / adim), int(x1 / adim) + 1):
                if i:
                    ic += yazi(self.X(i * adim), self.Y(0) + 13, str(i * adim).replace('-', '−'), 10, SOLUK, ince=True)
            for j in range(int(y0 / yadim), int(y1 / yadim) + 1):
                if j:
                    ic += yazi(self.X(0) - 5, self.Y(j * yadim) + 3.5, str(j * yadim).replace('-', '−'), 10, SOLUK, 'end', True)
            if x0 >= 0:
                ic += yazi(self.X(0) - 5, self.Y(0) + 13, '0', 10, SOLUK, 'end', True)
        self.ic = ic

    def X(self, x):
        return self.ox + (x - self.x0) * self.ux

    def Y(self, y):
        return self.oy + (self.y1 - y) * self.uy

    def dogru(self, m, c, renk, kalin=2, kesik=False, xa=None, xb=None):
        xa = self.x0 if xa is None else xa
        xb = self.x1 if xb is None else xb
        if m:
            lo, hi = sorted(((self.y0 - c) / m, (self.y1 - c) / m))
            xa, xb = max(xa, lo), min(xb, hi)
        ek = ' stroke-dasharray="5 4"' if kesik else ''
        self.ic += (f'<line x1="{self.X(xa):.1f}" y1="{self.Y(m * xa + c):.1f}" x2="{self.X(xb):.1f}" y2="{self.Y(m * xb + c):.1f}" '
                    f'stroke="{renk}" stroke-width="{kalin}" stroke-linecap="round"{ek}/>')

    def nokta(self, x, y, renk, etiket=None, dx=6, dy=-6, hiza='start'):
        self.ic += f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="3.2" fill="{renk}"/>'
        if etiket:
            self.ic += yazi(self.X(x) + dx, self.Y(y) + dy, etiket, 11.5, renk, hiza)


def g_katman():
    renk = [('P', '#eef1f7', SOLUK), ('N', MOR_A, MOR), ('M', '#e6ecfb', MAVI), ('L', '#e2f3fb', '#1585b5'), ('K', '#e3f6ea', YES)]
    ic = kutu(2, 2, 356, 196, GRI_A, GRI, 8)
    y = 8
    for i, (h, a, c) in enumerate(renk):
        hh = 34 if i else 30
        ic += f'<rect x="10" y="{y}" width="340" height="{hh}" fill="{a}" stroke="{c}" stroke-width="0.8"/>'
        ic += f'<circle cx="30" cy="{y + hh / 2}" r="11" fill="#fff" stroke="{c}" stroke-width="1.2"/>' + yazi(30, y + hh / 2 + 5, h, 13, c)
        y += hh
    # P: uydu
    ic += f'<rect x="196" y="16" width="16" height="12" fill="{SOLUK}"/><rect x="172" y="19" width="20" height="6" fill="#7aa0d8"/><rect x="216" y="19" width="20" height="6" fill="#7aa0d8"/>'
    # N: kutup ışığı
    ic += f'<path d="M120 66 q20 -14 40 0 t40 0 t40 0" fill="none" stroke="{YES}" stroke-width="2.2" opacity="0.8"/>'
    ic += f'<path d="M120 60 q20 -14 40 0 t40 0 t40 0" fill="none" stroke="{MOR}" stroke-width="1.4" opacity="0.7"/>'
    # M: meteor
    ic += f'<line x1="250" y1="80" x2="214" y2="98" stroke="{TUR}" stroke-width="2"/><circle cx="212" cy="99" r="3.5" fill="{KIR}"/>'
    ic += f'<line x1="150" y1="82" x2="130" y2="92" stroke="{TUR}" stroke-width="1.4"/><circle cx="129" cy="93" r="2.5" fill="{KIR}"/>'
    # L: ozon
    ic += f'<rect x="60" y="112" width="280" height="8" rx="4" fill="#5fb7dc" opacity="0.6"/>' + yazi(200, 132, 'ozon', 11, '#1585b5')
    # K: bulut, yağmur, dağ
    ic += '<path d="M60 190 L110 158 L140 176 L170 150 L220 190 z" fill="#c9e3c9" stroke="#2f8a3b" stroke-width="0.8"/>'
    ic += '<path d="M250 160 a10 10 0 0 1 18 -6 a12 12 0 0 1 22 2 a9 9 0 0 1 4 17 h-40 a7 7 0 0 1 -4 -13 z" fill="#fff" stroke="#8aa0c2" stroke-width="1"/>'
    for x in (258, 270, 282):
        ic += f'<line x1="{x}" y1="178" x2="{x - 4}" y2="188" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(346, 192, 'Yer', 10.5, SOLUK, 'end', True)
    return svg(ic, 360, 200, 'Atmosfer katmanlarının harflerle gösterildiği kesit', 48)


def g_gaz():
    ic = kutu(2, 2, 356, 132, GRI_A, GRI, 8)
    cx, cy, r = 92, 68, 54
    dilim = [(78, MAVI, 'X'), (21, TUR, 'Y'), (1, SOLUK, '')]
    a0 = -90
    for p, c, h in dilim:
        a1 = a0 + p * 3.6
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        ic += f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if p > 50 else 0} 1 {x1:.1f} {y1:.1f} z" fill="{c}" stroke="#fff" stroke-width="1.5"/>'
        if h:
            am = math.radians((a0 + a1) / 2)
            ic += yazi(cx + 30 * math.cos(am), cy + 30 * math.sin(am) + 5, h, 15, '#fff')
        a0 = a1
    for i, (ad, c, t) in enumerate((('X', MAVI, '%78'), ('Y', TUR, '%21'), ('Diğer gazlar', SOLUK, '%1'))):
        y = 42 + i * 30
        ic += f'<rect x="176" y="{y - 11}" width="14" height="14" rx="3" fill="{c}"/>' + yazi(198, y, ad, 12, LAC, 'start') + yazi(342, y, t, 12.5, c, 'end')
    return svg(ic, 360, 136, 'Atmosferdeki gazların oranlarını gösteren daire grafiği', 34)


def g_dag():
    ic = kutu(2, 2, 356, 150, '#eef6fd', GRI, 8)
    ic += '<path d="M14 136 L60 132 L120 104 L170 70 L214 30 L250 62 L300 96 L346 120 L346 146 L14 146 z" fill="#cfe6c4" stroke="#2f8a3b" stroke-width="1.2"/>'
    ic += '<path d="M200 44 L214 30 L230 46 L222 42 L214 48 L206 42 z" fill="#fff" stroke="#9fb3c9" stroke-width="0.8"/>'
    ic += '<rect x="10" y="134" width="40" height="12" fill="#9fd0f0"/>' + yazi(30, 128, 'deniz', 10.5, MAVI, ince=True)
    ic += f'<circle cx="56" cy="132" r="4" fill="{TUR}"/><circle cx="214" cy="30" r="4" fill="{KIR}"/>'
    ic += kutu(64, 102, 74, 36, '#fff', TUR, 6) + yazi(101, 117, 'A: 0 m', 11.5, TUR) + yazi(101, 132, '24 °C', 11.5, TUR)
    ic += kutu(250, 14, 96, 36, '#fff', KIR, 6) + yazi(298, 29, 'B: 2000 m', 11.5, KIR) + yazi(298, 44, '? °C', 11.5, KIR)
    ic += f'<line x1="218" y1="31" x2="250" y2="31" stroke="{KIR}" stroke-width="0.8" stroke-dasharray="3 2"/>'
    return svg(ic, 360, 154, 'Kıyıdaki A ve zirvedeki B noktası olan dağ kesiti', 38)


def g_uyari():
    ic = kutu(2, 2, 356, 120, '#fff', TUR, 10, 1.4)
    ic += f'<rect x="2" y="2" width="356" height="30" rx="10" fill="{TUR}"/><rect x="2" y="22" width="356" height="10" fill="{TUR}"/>'
    ic += '<path d="M24 26 L34 8 L44 26 z" fill="#fff"/>' + yazi(34, 23, '!', 12, TUR)
    ic += yazi(54, 22, 'METEOROLOJİK UYARI · TURUNCU KOD', 12.5, '#fff', 'start')
    ic += yazi(16, 54, 'Bölge: Batı Karadeniz kıyıları', 12, LAC, 'start')
    ic += yazi(16, 74, 'Zaman: Yarın 06.00 – 22.00', 12, LAC, 'start', True)
    ic += yazi(16, 94, 'Olay: Kuvvetli sağanak; sel ve su baskını,', 12, LAC, 'start', True)
    ic += yazi(16, 112, 'dere taşkını riski', 12, LAC, 'start', True)
    return svg(ic, 360, 124, 'Turuncu kodlu meteorolojik uyarı kartı', 30)


def ikon(x, y, tur):
    if tur == 'gunes':
        s = f'<circle cx="{x}" cy="{y}" r="9" fill="#ffc83d"/>'
        for a in range(0, 360, 45):
            s += f'<line x1="{x + 12 * math.cos(math.radians(a)):.1f}" y1="{y + 12 * math.sin(math.radians(a)):.1f}" x2="{x + 16 * math.cos(math.radians(a)):.1f}" y2="{y + 16 * math.sin(math.radians(a)):.1f}" stroke="#f0a400" stroke-width="1.6"/>'
        return s
    if tur == 'ay':
        return f'<circle cx="{x}" cy="{y}" r="11" fill="#9fb3d9"/><circle cx="{x + 6}" cy="{y - 4}" r="10" fill="#fff"/>' + yazi(x + 12, y + 14, '❄', 12, MAVI)
    s = f'<path d="M{x - 16} {y + 4} a8 8 0 0 1 10 -10 a10 10 0 0 1 18 2 a7 7 0 0 1 4 14 h-28 a6 6 0 0 1 -4 -6 z" fill="#dfe6f2" stroke="#8aa0c2"/>'
    for dx in (-8, 0, 8):
        s += f'<line x1="{x + dx}" y1="{y + 14}" x2="{x + dx - 3}" y2="{y + 21}" stroke="{MAVI}" stroke-width="1.4"/>'
    return s


def g_tahmin():
    gun = [('Pazartesi', 'gunes', '12 °C', '2 °C', 'Açık, rüzgârsız'), ('Salı', 'ay', '9 °C', '−3 °C', 'Gece don riski'), ('Çarşamba', 'yagmur', '14 °C', '5 °C', 'Gün boyu yağmur')]
    ic = kutu(2, 2, 356, 138, GRI_A, GRI, 8)
    for i, (g, t, en, ed, a) in enumerate(gun):
        x = 8 + i * 117
        c = KIR if t == 'ay' else MAVI
        ic += kutu(x, 8, 110, 126, '#fff', c, 7)
        ic += yazi(x + 55, 26, g, 12.5, c)
        ic += ikon(x + 55, 54, t)
        ic += yazi(x + 55, 92, f'En yüksek: {en}', 11, LAC, ince=True)
        ic += yazi(x + 55, 108, f'En düşük: {ed}', 11, KIR if ed.startswith('−') else LAC, ince=ed[0] != '−')
        ic += yazi(x + 55, 125, a, 11, c)
    return svg(ic, 360, 142, 'Üç günlük hava tahmini', 36)


def g_iklim():
    ay = [5, 6, 9, 13, 17, 21, 24, 24, 20, 15, 10, 6]
    d = Duzlem(0, 12, 0, 30, 22, 50, 30, '', '°C', adim=1, yadim=5, sayilar=False)
    for j in (10, 20, 30):
        d.ic += yazi(d.X(0) - 5, d.Y(j) + 3.5, str(j), 10, SOLUK, 'end', True)
    for i, v in enumerate(ay):
        x = d.X(i + 0.5)
        d.ic += f'<rect x="{x - 7:.1f}" y="{d.Y(v):.1f}" width="14" height="{d.Y(0) - d.Y(v):.1f}" rx="2" fill="{MAVI}"/>'
        d.ic += yazi(x, d.Y(0) + 13, 'OŞMNMHTAEEKA'[i], 10, SOLUK, ince=True)
    d.nokta(0.5, 18, KIR)
    ic = kutu(2, 2, 356, 190, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(0.5) + 8, d.Y(18) - 4, '15 Ocak: 18 °C', 11.5, KIR, 'start')
    ic += yazi(d.X(6.5), 20, '30 yıllık aylık ortalama sıcaklık', 11.5, MAVI)
    return svg(ic, 360, 194, 'Bir şehrin 30 yıllık aylık ortalama sıcaklıkları ve 15 Ocak ölçümü', 44)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_katman()
    s[2]['gorsel'] = g_gaz()
    s[5]['gorsel'] = g_dag()
    s[7]['gorsel'] = g_uyari()
    s[10]['gorsel'] = g_tahmin()
    s[12]['gorsel'] = g_iklim()
