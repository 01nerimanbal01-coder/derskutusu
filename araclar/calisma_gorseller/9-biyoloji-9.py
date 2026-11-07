"""9. sınıf Biyoloji 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12 birimlik yazı ≈ 8,5–9 pt.
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


def ok(x1, y1, x2, y2, renk, kalin=1.6):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    u1 = (x2 - 7 * math.cos(a) + 3.5 * math.sin(a), y2 - 7 * math.sin(a) - 3.5 * math.cos(a))
    u2 = (x2 - 7 * math.cos(a) - 3.5 * math.sin(a), y2 - 7 * math.sin(a) + 3.5 * math.cos(a))
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<path d="M{x2:.1f} {y2:.1f} L{u1[0]:.1f} {u1[1]:.1f} L{u2[0]:.1f} {u2[1]:.1f} z" fill="{renk}"/>')


def g_koful():
    ic = kutu(2, 2, 356, 150, MAVI_A, MAVI, 8)
    ic += yazi(14, 22, 'Tatlı su', 12, MAVI, 'start')
    ic += '<path d="M60 76 C60 36 130 28 180 34 C240 40 296 50 294 84 C292 120 236 132 176 128 C112 124 60 116 60 76 z" fill="#f4fbf2" stroke="#2f8a3b" stroke-width="1.6"/>'
    ic += f'<ellipse cx="150" cy="82" rx="22" ry="16" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.1"/>' + yazi(150, 86, 'çekirdek', 10, MOR, ince=True)
    ic += f'<circle cx="236" cy="72" r="15" fill="#d9ecff" stroke="{MAVI}" stroke-width="1.2"/>'
    for a in range(0, 360, 60):
        import math
        ic += f'<line x1="{236 + 15 * math.cos(math.radians(a)):.1f}" y1="{72 + 15 * math.sin(math.radians(a)):.1f}" x2="{236 + 25 * math.cos(math.radians(a)):.1f}" y2="{72 + 25 * math.sin(math.radians(a)):.1f}" stroke="{MAVI}" stroke-width="1"/>'
    ic += ok(246, 60, 300, 24, KIR, 2)
    ic += yazi(306, 22, 'su', 12, KIR, 'start')
    for x, y in ((30, 60), (30, 100), (100, 146), (200, 150)):
        pass
    ic += ok(22, 70, 58, 76, MAVI, 1.6) + ok(22, 104, 64, 96, MAVI, 1.6) + ok(120, 148, 128, 124, MAVI, 1.6)
    ic += yazi(14, 132, 'su girişi', 11, MAVI, 'start', True)
    ic += f'<line x1="236" y1="97" x2="250" y2="128" stroke="{SOLUK}" stroke-width="0.7"/>' + yazi(250, 142, 'kontraktil koful', 11, LAC, 'middle')
    ic += yazi(312, 40, 'ATP', 11, TUR, 'start')
    return svg(ic, 360, 154, 'Tatlı su tek hücrelisinde kontraktil koful ile su atılması', 38)


def g_buyume():
    d = Duzlem(0, 10, 0, 10, 15, 50, 20, 'Yaş', 'Boy', sayilar=False)
    import math
    k = ' '.join(f'{d.X(x / 10):.1f},{d.Y(0.5 + 0.9 * x / 10):.1f}' for x in range(0, 101, 5))
    l = ' '.join(f'{d.X(x / 10):.1f},{d.Y(0.4 + 5.2 * (1 - math.exp(-x / 22))):.1f}' for x in range(0, 101, 5))
    d.ic += f'<polyline points="{k}" fill="none" stroke="{YES}" stroke-width="2.4"/>'
    d.ic += f'<polyline points="{l}" fill="none" stroke="{TUR}" stroke-width="2.4"/>'
    ic = kutu(2, 2, 356, 186, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(9.6), d.Y(9.6), 'K', 14, YES, 'end') + yazi(d.X(9.6), d.Y(5.4) - 6, 'L', 14, TUR, 'end')
    ic += yazi(d.X(0) - 5, d.Y(0) + 13, '0', 10, SOLUK, 'end', True)
    return svg(ic, 360, 190, 'K ve L canlılarının boy–yaş grafiği', 44)


def g_ureme():
    ic = kutu(2, 2, 356, 176, GRI_A, GRI, 8)
    ic += kutu(10, 10, 340, 74, '#fff', MAVI, 7) + kutu(10, 94, 340, 76, '#fff', TUR, 7)
    ic += yazi(30, 52, 'I. yol', 12, MAVI)
    ic += f'<circle cx="86" cy="47" r="18" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.3"/>' + yazi(86, 51, 'ata', 11, MAVI)
    ic += ok(110, 47, 168, 47, LAC) + yazi(136, 38, 'bölünme', 11, LAC, ince=True)
    for y in (30, 64):
        ic += f'<circle cx="200" cy="{y}" r="13" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.3"/>'
    ic += yazi(222, 51, 'kalıtsal yapısı', 11, LAC, 'start', True) + yazi(222, 65, 'atayla aynı yavrular', 11, LAC, 'start', True)
    ic += yazi(30, 138, 'II. yol', 12, TUR)
    ic += f'<circle cx="78" cy="116" r="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.3"/>' + f'<circle cx="78" cy="152" r="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.3"/>'
    ic += yazi(92, 120, 'üreme hücresi', 10.5, TUR, 'start', True) + yazi(92, 156, 'üreme hücresi', 10.5, MOR, 'start', True)
    ic += ok(168, 120, 198, 131, LAC) + ok(168, 150, 198, 139, LAC) + yazi(176, 112, 'döllenme', 11, LAC, ince=True)
    ic += f'<circle cx="218" cy="135" r="15" fill="#fff" stroke="{TUR}" stroke-width="1.3"/><circle cx="218" cy="135" r="6" fill="{MOR_A}" stroke="{MOR}"/>'
    ic += yazi(242, 132, 'zigot →', 11, LAC, 'start', True) + yazi(242, 147, 'farklı özellikli', 11, LAC, 'start', True) + yazi(242, 161, 'yavru', 11, LAC, 'start', True)
    return svg(ic, 360, 180, 'İki farklı üreme biçiminin şeması', 44)


def g_uyum():
    kart = [('Kaktüs', 'Çöl', 'Yaprakları diken biçiminde', YES, YES_A), ('Kutup ayısı', 'Buzul', 'Kalın yağ tabakası, beyaz post', MAVI, MAVI_A),
            ('Nilüfer', 'Göl', 'Suyun üstünde geniş yaprak', MOR, MOR_A)]
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    for i, (ad, ort, oz, c, a) in enumerate(kart):
        x = 8 + i * 117
        ic += kutu(x, 8, 110, 100, a, c, 7)
        ic += yazi(x + 55, 28, ad, 12.5, c)
        ic += yazi(x + 55, 46, f'Ortam: {ort}', 11, LAC, ince=True)
        ic += f'<line x1="{x + 10}" y1="54" x2="{x + 100}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        sozler = oz.split(' ')
        satir, satirlar = '', []
        for s in sozler:
            if len(satir + ' ' + s) > 15 and satir:
                satirlar.append(satir); satir = s
            else:
                satir = (satir + ' ' + s).strip()
        satirlar.append(satir)
        for j, st in enumerate(satirlar):
            ic += yazi(x + 55, 72 + j * 14, st, 11, LAC)
    return svg(ic, 360, 116, 'Üç canlının yaşadığı ortam ve özelliği', 30)


def g_isi():
    d = Duzlem(0, 40, 0, 40, 36, 92, 26, 'Ortam (°C)', 'Vücut (°C)', adim=10, yadim=10)
    d.dogru(0, 36.5, KIR, 2.4, xa=0, xb=40)
    d.dogru(1, 0, GRI, 1.2, True, xa=0, xb=40)
    ic = kutu(2, 2, 356, 186, GRI_A, GRI, 8) + d.ic
    ic += yazi(d.X(40) + 8, d.Y(36.5) - 2, 'vücut sıcaklığı', 11, KIR, 'start') + yazi(d.X(40) + 8, d.Y(36.5) + 12, '36,5 °C', 11, KIR, 'start')
    ic += yazi(d.X(40) + 8, d.Y(22), 'ortam = vücut', 10.5, SOLUK, 'start', True)
    return svg(ic, 360, 190, 'Ortam sıcaklığına göre vücut sıcaklığı', 44)


def g_fasulye():
    gun = ['0', '3', '6', '9', '12']
    boy = ['0', '1,2', '3,0', '5,4', '8,1']
    yap = ['0', '0', '2', '2', '4']
    ic = kutu(2, 2, 356, 124, GRI_A, GRI, 8)
    ic += yazi(180, 22, 'Fasulye fidesi gözlem kaydı (ortam 22 °C)', 12, YES)
    x0, w0, w = 14, 106, 46
    for r, (bas, deg, c, a) in enumerate((('Gün', gun, LAC, '#e9edf5'), ('Boy (cm)', boy, YES, YES_A), ('Yaprak sayısı', yap, MAVI, MAVI_A))):
        y = 32 + r * 29
        ic += kutu(x0, y, w0, 29, a, c, 0) + yazi(x0 + w0 / 2, y + 19, bas, 11.5, c)
        for i, v in enumerate(deg):
            ic += kutu(x0 + w0 + i * w, y, w, 29, '#fff', c, 0) + yazi(x0 + w0 + i * w + w / 2, y + 19, v, 12.5, LAC)
    return svg(ic, 360, 128, 'Fasulye fidesinin günlere göre boy ve yaprak sayısı', 32)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_koful()
    s[2]['gorsel'] = g_buyume()
    s[5]['gorsel'] = g_ureme()
    s[7]['gorsel'] = g_uyum()
    s[10]['gorsel'] = g_isi()
    s[12]['gorsel'] = g_fasulye()
