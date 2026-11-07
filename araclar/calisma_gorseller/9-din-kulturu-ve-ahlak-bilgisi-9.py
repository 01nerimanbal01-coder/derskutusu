"""9. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12 birimlik yazı ≈ 8,5–9 pt. Ayet meali kullanılmadı; sure içerikleri özetle anıldı.
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


def sar(metin, n):
    satirlar, s = [], ''
    for k in metin.split():
        if s and len(s) + 1 + len(k) > n:
            satirlar.append(s); s = k
        else:
            s = (s + ' ' + k).strip()
    return satirlar + [s]


def g_agac():
    ic = kutu(2, 2, 356, 176, '#f6fbf3', '#9cc79a', 8)
    ic += '<rect x="168" y="70" width="24" height="68" fill="#8a5a33"/>'
    ic += '<ellipse cx="180" cy="62" rx="92" ry="48" fill="#5fae5a"/><ellipse cx="140" cy="54" rx="40" ry="30" fill="#6cbb63"/><ellipse cx="222" cy="52" rx="44" ry="30" fill="#6cbb63"/>'
    for x, y in ((128, 70), (166, 40), (204, 76), (238, 54), (150, 92), (214, 30)):
        ic += f'<circle cx="{x}" cy="{y}" r="7" fill="#e5484d" stroke="#a32a2e"/>'
    ic += '<rect x="20" y="138" width="320" height="34" fill="#c9a77d"/>'
    for a in (-60, -30, 0, 30, 60):
        ic += f'<path d="M180 138 q{a * 0.6:.0f} 14 {a * 1.6:.0f} 30" fill="none" stroke="#6b4423" stroke-width="2.4"/>'
    ic += kutu(262, 96, 88, 24, '#fff', KIR, 6) + yazi(306, 112, 'salih amel', 11.5, KIR)
    ic += f'<line x1="262" y1="108" x2="240" y2="64" stroke="{KIR}" stroke-width="0.8"/>'
    ic += kutu(16, 150, 70, 22, '#fff', '#6b4423', 6) + yazi(51, 165, 'iman', 11.5, '#6b4423')
    ic += f'<line x1="86" y1="161" x2="140" y2="160" stroke="#6b4423" stroke-width="0.8"/>'
    ic += kutu(262, 146, 88, 22, '#fff', MAVI, 6) + yazi(306, 161, 'sahih bilgi', 11.5, MAVI)
    ic += f'<line x1="262" y1="157" x2="216" y2="154" stroke="{MAVI}" stroke-width="0.8"/>'
    return svg(ic, 360, 180, 'İman, bilgi ve amel ilişkisini anlatan ağaç benzetmesi', 44)


def g_asr():
    k = [('1', 'İman etmek', MAVI, MAVI_A), ('2', 'Salih amel işlemek', YES, YES_A), ('3', 'Birbirine hakkı tavsiye etmek', MOR, MOR_A), ('4', '?', KIR, KIR_A)]
    ic = kutu(2, 2, 356, 146, GRI_A, GRI, 8) + yazi(180, 22, 'Asr suresine göre ziyandan kurtulmanın şartları', 12, LAC)
    for i, (n, t, c, a) in enumerate(k):
        y = 32 + i * 28
        ic += kutu(40, y, 280, 24, a, c, 7) + f'<circle cx="56" cy="{y + 12}" r="9" fill="{c}"/>' + yazi(56, y + 16.5, n, 11.5, '#fff')
        ic += yazi(74, y + 17, t, 12, c, 'start')
    return svg(ic, 360, 150, 'Asr suresine göre dört şart', 36)


def balon(x, y, w, baslik, metin, c, a, n=40):
    st = sar(metin, n)
    h = 28 + len(st) * 17
    s = kutu(x, y, w, h, a, c, 10)
    s += yazi(x + 12, y + 18, baslik, 11.5, c, 'start')
    for i, t in enumerate(st):
        s += yazi(x + 12, y + 36 + i * 17, t, 12, LAC, 'start', True)
    return s, h


def g_iki():
    b1, h1 = balon(8, 8, 344, 'Öğrenci A', 'Ailem nasıl inanıyorsa ben de öyle inanıyorum; bunun nedenleri üzerinde hiç düşünmedim.', TUR, TUR_A, 52)
    b2, h2 = balon(8, 16 + h1, 344, 'Öğrenci B', 'Evrendeki düzeni ve ayetleri düşündükçe inancımın gerekçelerini daha iyi kavrıyorum.', MAVI, MAVI_A, 52)
    H = 28 + h1 + h2
    return svg(kutu(2, 2, 356, H - 4, GRI_A, GRI, 8) + b1 + b2, 360, H, 'İki öğrencinin inançları hakkındaki sözleri', H * 0.25)


def g_olay():
    m = ('Markette kasadan fazla para üstü alan bir genç, kimsenin fark etmediğini bildiği hâlde '
         'birkaç adım sonra geri dönüyor ve fazla parayı kasiyere iade ediyor.')
    st = sar(m, 52)
    h = 36 + len(st) * 18
    ic = kutu(2, 2, 356, h, '#fff', YES, 8, 1.1) + f'<rect x="2" y="2" width="356" height="22" rx="8" fill="{YES}"/><rect x="2" y="14" width="356" height="10" fill="{YES}"/>'
    ic += yazi(16, 18, 'Olay', 12, '#fff', 'start')
    for i, t in enumerate(st):
        ic += yazi(16, 44 + i * 18, t, 12, LAC, 'start', True)
    return svg(ic, 360, h + 4, 'Para üstünü iade eden gencin olayı', (h + 4) * 0.25)


def g_sema():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += kutu(140, 10, 80, 28, MAVI, MAVI, 14) + yazi(180, 29, 'İMAN', 13, '#fff')
    ic += f'<path d="M180 38 V50 M92 50 H268 M92 50 V58 M268 50 V58" fill="none" stroke="{SOLUK}" stroke-width="1.2"/>'
    for x, b, m, c, a in ((10, 'Bireye', ['İç huzur (sekînet)', 'Hayatın anlamı', 'Onur ve özgürlük'], YES, YES_A),
                          (186, 'Topluma', ['Güven ortamı', 'Adalet', '?'], MOR, MOR_A)):
        ic += kutu(x, 58, 164, 86, a, c, 7) + yazi(x + 82, 76, b, 12, c)
        for i, t in enumerate(m):
            ic += yazi(x + 82, 98 + i * 18, t, 11.5 if t != '?' else 14, KIR if t == '?' else LAC, ince=t != '?')
    return svg(ic, 360, 154, 'İmanın bireye ve topluma kazandırdıkları şeması', 38)


def g_zorluk():
    b, h = balon(8, 8, 344, 'Öğrencinin notu', 'Aylardır hazırlandığım yarışmada derece alamadım. Çok emek vermiştim; şimdi ne yapacağımı bilemiyorum.', TUR, '#fffaf0', 52)
    return svg(kutu(2, 2, 356, h + 16, GRI_A, GRI, 8) + b, 360, h + 20, 'Yarışmada derece alamayan öğrencinin notu', (h + 20) * 0.25)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_agac()
    s[2]['gorsel'] = g_asr()
    s[5]['gorsel'] = g_iki()
    s[7]['gorsel'] = g_olay()
    s[10]['gorsel'] = g_sema()
    s[12]['gorsel'] = g_zorluk()
