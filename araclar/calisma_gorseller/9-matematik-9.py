"""9. sınıf Matematik 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12 birimlik yazı ≈ 8,5–9 pt. Koordinat düzlemleri birim kareli, tek ölçekli.
"""

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


def g_donusum():
    d = Duzlem(-4, 4, -3, 5, 19, 26, 18)
    d.dogru(1, 0, GRI, 1.6, True)
    d.dogru(2, 2, MAVI, 2.4)
    d.nokta(-1, 0, MAVI)
    d.nokta(0, 2, MAVI)
    d.nokta(1, 4, MAVI)
    ic = kutu(2, 2, 356, 178, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(3.9), d.Y(3.5), 'f', 13, SOLUK, 'end')
    ic += yazi(d.X(1.25), d.Y(4.6), 'g', 14, MAVI, 'start')
    ic += kutu(222, 52, 128, 74, '#fff', GRI, 7)
    ic += f'<line x1="232" y1="74" x2="262" y2="74" stroke="{GRI}" stroke-width="1.6" stroke-dasharray="5 4"/>' + yazi(268, 78, 'f(x) = x', 12, SOLUK, 'start', True)
    ic += f'<line x1="232" y1="104" x2="262" y2="104" stroke="{MAVI}" stroke-width="2.4"/>' + yazi(268, 108, 'g(x) = ?', 12, MAVI, 'start')
    return svg(ic, 360, 182, 'f(x) = x ve ondan türetilen g doğrusunun grafiği', 46)


def g_egimler():
    d = Duzlem(-3, 3, -3, 3, 22, 30, 20, sayilar=False)
    d.dogru(3, 0, MAVI, 2.2)
    d.dogru(0.5, 0, YES, 2.2)
    d.dogru(-2, 0, KIR, 2.2)
    ic = kutu(2, 2, 356, 170, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(1.0) + 6, d.Y(3) + 10, 'd₁', 13, MAVI, 'start')
    ic += yazi(d.X(3) - 2, d.Y(1.5) - 6, 'd₂', 13, YES, 'end')
    ic += yazi(d.X(-1.5) - 6, d.Y(3) + 10, 'd₃', 13, KIR, 'end')
    ic += yazi(d.X(0) - 6, d.Y(0) + 13, 'O', 11, SOLUK, 'end', True)
    ic += kutu(222, 40, 128, 96, '#fff', GRI, 7)
    for i, (ad, f, r) in enumerate((('d₁', 'y = a₁x', MAVI), ('d₂', 'y = a₂x', YES), ('d₃', 'y = a₃x', KIR))):
        y = 66 + i * 26
        ic += f'<line x1="232" y1="{y - 4}" x2="256" y2="{y - 4}" stroke="{r}" stroke-width="2.4"/>'
        ic += yazi(262, y, f'{ad}: {f}', 12, r, 'start')
    return svg(ic, 360, 174, 'Orijinden geçen üç doğru', 44)


def g_isaret():
    d = Duzlem(-2, 4, -3, 5, 18, 50, 18)
    d.dogru(-2, 4, TUR, 2.4)
    d.nokta(0, 4, TUR, '(0, 4)', 7, 4)
    d.nokta(2, 0, TUR, '(2, 0)', 6, -7)
    ic = kutu(2, 2, 356, 172, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(-1.3), d.Y(4.4), 'g', 14, TUR, 'end')
    return svg(ic, 360, 176, 'g doğrusal fonksiyonunun grafiği', 44)


def g_taksi():
    km = ['0', '2', '5', '8']
    tl = ['40', '64', '100', '136']
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    ic += yazi(180, 22, 'Taksimetre kaydı', 13, MAVI)
    x0, w = 16, 58
    ic += kutu(x0, 32, 96, 28, MAVI_A, MAVI, 0) + kutu(x0, 60, 96, 28, TUR_A, TUR, 0)
    ic += yazi(x0 + 48, 51, 'Yol (km)', 12, MAVI) + yazi(x0 + 48, 79, 'Ücret (TL)', 12, TUR)
    for i in range(4):
        x = x0 + 96 + i * w
        ic += kutu(x, 32, w, 28, '#fff', MAVI, 0) + kutu(x, 60, w, 28, '#fff', TUR, 0)
        ic += yazi(x + w / 2, 51, km[i], 13, LAC) + yazi(x + w / 2, 79, tl[i], 13, LAC)
    return svg(ic, 360, 100, 'Taksinin aldığı yol ve ücret tablosu', 26)


def g_sarj():
    d = Duzlem(0, 10, 0, 100, 26, 58, 22, 't (saat)', 'Şarj (%)', adim=1, yadim=20)
    d.dogru(-10, 90, KIR, 2.4, xa=0, xb=3)
    d.dogru(-10, 90, KIR, 1.4, True, xa=3, xb=6.5)
    d.nokta(0, 90, KIR)
    d.nokta(3, 60, KIR)
    for x, y in ((0, 90), (3, 60)):
        d.ic += f'<line x1="{d.X(0):.1f}" y1="{d.Y(y):.1f}" x2="{d.X(x):.1f}" y2="{d.Y(y):.1f}" stroke="{KIR}" stroke-width="0.8" stroke-dasharray="2 3"/>'
        d.ic += f'<line x1="{d.X(x):.1f}" y1="{d.Y(0):.1f}" x2="{d.X(x):.1f}" y2="{d.Y(y):.1f}" stroke="{KIR}" stroke-width="0.8" stroke-dasharray="2 3"/>'
    d.ic += yazi(d.X(0) - 5, d.Y(90) + 4, '90', 10, KIR, 'end')
    ic = kutu(2, 2, 356, 176, GRI_A, GRI, 8) + d.ic
    return svg(ic, 360, 180, 'Telefon şarjının zamana göre değişim grafiği', 44)


def g_depo():
    d = Duzlem(0, 12, 0, 240, 22, 54, 24, 't (dk)', 'Su (L)', adim=2, yadim=60)
    d.dogru(-30, 240, MAVI, 2.4, xa=0, xb=8)
    d.dogru(-15, 180, TUR, 2.4, xa=0, xb=12)
    d.nokta(0, 240, MAVI)
    d.nokta(8, 0, MAVI)
    d.nokta(0, 180, TUR)
    d.nokta(12, 0, TUR)
    ic = kutu(2, 2, 356, 168, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(2.2) + 4, d.Y(190), 'A', 14, MAVI, 'start')
    ic += yazi(d.X(6), d.Y(110) - 6, 'B', 14, TUR, 'start')
    return svg(ic, 360, 172, 'A ve B depolarındaki su miktarının zamana göre değişimi', 42)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_donusum()
    s[2]['gorsel'] = g_egimler()
    s[5]['gorsel'] = g_isaret()
    s[7]['gorsel'] = g_taksi()
    s[9]['gorsel'] = g_sarj()
    s[12]['gorsel'] = g_depo()
