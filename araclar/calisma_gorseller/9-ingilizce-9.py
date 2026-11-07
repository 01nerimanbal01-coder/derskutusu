"""9. sınıf İngilizce 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

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
        ic += yazi(self.X(0) + 7, self.Y(y1) - 4, yad, 13, LAC, 'start', True)
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


def kart(baslik, satirlar, renk, h_satir=20, en=360):
    h = 36 + len(satirlar) * h_satir
    ic = kutu(2, 2, en - 4, h, '#fff', renk, 8, 1.2)
    ic += f'<rect x="2" y="2" width="{en - 4}" height="24" rx="8" fill="{renk}"/><rect x="2" y="16" width="{en - 4}" height="10" fill="{renk}"/>'
    ic += yazi(en / 2, 19, baslik, 12.5, '#fff')
    return ic, h


def g_plan():
    oda = [(10, 10, 160, 62, 'Library', MAVI, MAVI_A), (190, 10, 160, 62, 'Science lab', YES, YES_A),
           (10, 92, 160, 62, 'Gymnasium', TUR, TUR_A), (190, 92, 160, 62, 'Canteen', MOR, MOR_A)]
    ic = kutu(2, 2, 356, 160, '#f7f7f2', GRI, 6)
    ic += '<rect x="10" y="76" width="340" height="12" fill="#e4e1d6"/>' + yazi(180, 85.5, 'corridor', 9.5, SOLUK, ince=True)
    for x, y, w, h, ad, c, a in oda:
        ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{a}" stroke="{c}" stroke-width="1.4"/>' + yazi(x + w / 2, y + h / 2 + 5, ad, 13, c)
    return svg(ic, 360, 164, 'Okul planında dört birim', 40)


def g_lab():
    kur = [('✓', 'Wear safety goggles.', YES), ('✗', 'No food or drinks.', KIR), ('✓', 'Wash your hands after the experiment.', YES),
           ('✗', 'Never touch chemicals without your teacher.', KIR)]
    ic, h = kart('SCIENCE LAB RULES', kur, YES, 22)
    for i, (s, t, c) in enumerate(kur):
        y = 46 + i * 22
        ic += f'<circle cx="24" cy="{y - 4}" r="8" fill="{c}"/>' + yazi(24, y, s, 11, '#fff') + yazi(40, y, t, 13, LAC, 'start', True)
    return svg(ic, 360, h + 6, 'Fen laboratuvarı kuralları', (h + 6) * 0.3)


def g_kulup():
    sat = [('Robotics and Coding', 'Monday', '15.30'), ('Debate', 'Wednesday', '16.00'), ('Drama', 'Friday', '15.00'), ('Chess', 'Tuesday', '15.30')]
    ic, h = kart('AFTER-SCHOOL CLUBS', sat, MOR, 21)
    for i, (a, g, s) in enumerate(sat):
        y = 46 + i * 21
        ic += yazi(16, y, a, 13, LAC, 'start') + yazi(216, y, g, 13, MOR, 'start', True) + yazi(344, y, s, 13, LAC, 'end', True)
        ic += f'<line x1="10" y1="{y + 6}" x2="350" y2="{y + 6}" stroke="#e8e2f7" stroke-width="0.7"/>'
    ic += kutu(10, h + 10, 340, 30, '#fffaf0', TUR, 6) + yazi(20, h + 30, 'Elif: "I have volleyball training on Mondays and Fridays."', 11.5, LAC, 'start', True)
    return svg(ic, 360, h + 44, 'Kulüp programı ve Elif in notu', (h + 44) * 0.3)


def g_program():
    ic, h = kart('TUESDAY TIMETABLE', [1, 2], MAVI, 22)
    ic += yazi(16, 50, '10.00 – 10.40   Maths   Room 12', 13, LAC, 'start', True)
    ic += kutu(10, 60, 340, 22, KIR_A, KIR, 5) + yazi(20, 75.5, 'Note: This week Maths lessons are in the library.', 12, KIR, 'start')
    return svg(ic, 360, h + 6, 'Salı ders programı ve not', (h + 6) * 0.3)


def g_duyuru():
    sat = ['From Monday:', '• The library is open until 18.00.', '• The gym is closed for repairs.', '• Friday is Sports Day: uniforms are not', '   necessary, wear sports clothes.']
    ic, h = kart('NOTICE', sat, TUR, 19)
    for i, t in enumerate(sat):
        ic += yazi(16, 46 + i * 19, t, 13, LAC, 'start', i > 0)
    return svg(ic, 360, h + 6, 'Okul duyurusu', (h + 6) * 0.3)


def g_kural():
    sat = [('1', 'Saat 8.30\'dan önce okulda ol. (Zorunlu)'), ('2', 'Derste telefon kullanmak yasak.'), ('3', 'Cuma günü forma giymek zorunlu değil.')]
    ic, h = kart('Okul kuralları', sat, MAVI, 22)
    for i, (n, t) in enumerate(sat):
        y = 46 + i * 22
        ic += f'<circle cx="24" cy="{y - 4}" r="8" fill="{MAVI}"/>' + yazi(24, y, n, 11, '#fff') + yazi(40, y, t, 13, LAC, 'start', True)
    return svg(ic, 360, h + 6, 'Üç okul kuralı', (h + 6) * 0.3)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_plan()
    s[2]['gorsel'] = g_lab()
    s[5]['gorsel'] = g_kulup()
    s[7]['gorsel'] = g_program()
    s[11]['gorsel'] = g_duyuru()
    s[13]['gorsel'] = g_kural()
