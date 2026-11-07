"""9. sınıf Peygamberimizin Hayatı 9. hafta görselleri (SVG; insan figürü yok, kutsal şahsiyetler yalnız adla anılır; görsel içi yazı ≈ gövde puntosu).

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


def sar(metin, n):
    satirlar, s = [], ''
    for k in metin.split():
        if s and len(s) + 1 + len(k) > n:
            satirlar.append(s); s = k
        else:
            s = (s + ' ' + k).strip()
    return satirlar + [s]


def g_serit():
    olay = [('12', ['Busrâ', 'yolculuğu'], MAVI), ('20', ['Ficar', 'Savaşı'], KIR), ('~20', ["Hilfü'l-", 'Fudûl'], YES),
            ('25', ['Hz. Hatice', 'ile evlilik'], MOR), ('35', ['?'], TUR)]
    ic = kutu(2, 2, 356, 120, GRI_A, GRI, 8)
    y = 58
    ic += f'<line x1="20" y1="{y}" x2="340" y2="{y}" stroke="{LAC}" stroke-width="2"/><path d="M340 {y} l-7 -4 v8 z" fill="{LAC}"/>'
    for i, (a, t, c) in enumerate(olay):
        x = 44 + i * 68
        ic += f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>'
        ic += kutu(x - 20, y - 30, 40, 18, '#fff', c, 9) + yazi(x, y - 17, a + ' yaş' if a != '~20' else '~20', 10, c)
        for j, sat in enumerate(t):
            ic += yazi(x, y + 24 + j * 15, sat, 11.5 if sat != '?' else 16, c)
    return svg(ic, 360, 124, 'Peygamberimizin gençlik yıllarına ait zaman şeridi', 30)


def g_akis():
    ad = [('Yemenli bir tüccar malını Âs b. Vâil\'e satar.', MAVI, MAVI_A), ('Âs b. Vâil malın bedelini ödemez.', KIR, KIR_A),
          ('?', TUR, TUR_A), ('Tüccarın parası Âs b. Vâil\'den alınır.', YES, YES_A)]
    ic = kutu(2, 2, 356, 172, GRI_A, GRI, 8)
    for i, (t, c, a) in enumerate(ad):
        y = 10 + i * 41
        ic += kutu(30, y, 300, 30, a, c, 7) + yazi(180, y + 20, t, 12 if t != '?' else 15, c if t == '?' else LAC, 'middle', t != '?')
        if i < 3:
            ic += f'<path d="M180 {y + 31} v6 m-4 -4 l4 5 l4 -5" fill="none" stroke="{SOLUK}" stroke-width="1.4"/>'
    return svg(ic, 360, 176, 'Hilfü l-Fudûl e giden olayların akışı', 42)


def g_ilke():
    m = ['Sözünde durmak', 'Tartıda ve ölçüde hile yapmamak', 'Malın kusurunu gizlememek', 'Ortağına dürüst davranmak']
    ic = kutu(2, 2, 356, 132, '#fff', YES, 8, 1.2)
    ic += f'<rect x="2" y="2" width="356" height="24" rx="8" fill="{YES}"/><rect x="2" y="16" width="356" height="10" fill="{YES}"/>'
    ic += yazi(180, 19, 'Ticarette gözetilen ilkeler', 12.5, '#fff')
    for i, t in enumerate(m):
        y = 50 + i * 22
        ic += f'<circle cx="24" cy="{y - 4}" r="8" fill="{YES}"/>' + yazi(24, y, str(i + 1), 11, '#fff') + yazi(40, y, t, 12.5, LAC, 'start', True)
    return svg(ic, 360, 136, 'Ticarette gözetilen dört ilke', 34)


def g_ridâ():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += '<path d="M110 40 L250 40 L270 112 L90 112 z" fill="#e9dfc8" stroke="#a08a5c" stroke-width="1.4"/>'
    ic += '<ellipse cx="180" cy="76" rx="22" ry="15" fill="#2b2f3a"/>' + yazi(180, 80, 'taş', 10, '#fff', ince=True)
    for x, y, t, hz in ((92, 34, 'Kabile 1', 'end'), (268, 34, 'Kabile 2', 'start'), (84, 124, 'Kabile 3', 'end'), (276, 124, 'Kabile 4', 'start')):
        ic += f'<circle cx="{(110 if x < 180 else 250) if y < 80 else (90 if x < 180 else 270)}" cy="{40 if y < 80 else 112}" r="5" fill="{MOR}"/>'
        ic += yazi(x, y + 4, t, 12, MOR, hz)
    ic += yazi(180, 142, 'Yaygı ile kaldırılan taşı yerine Peygamberimiz koyar.', 11, LAC, 'middle', True)
    ic += yazi(180, 24, 'Yaygı (ridâ)', 11.5, '#8a6d33')
    return svg(ic, 360, 154, 'Hacerü l-Esved anlaşmazlığının çözüm şeması', 38)


def g_aile():
    ic = kutu(2, 2, 356, 186, GRI_A, GRI, 8)
    ic += kutu(42, 10, 130, 26, MAVI_A, MAVI, 13) + yazi(107, 27, 'Hz. Muhammed (s.a.v.)', 11, MAVI)
    ic += kutu(196, 10, 120, 26, MOR_A, MOR, 13) + yazi(256, 27, 'Hz. Hatice', 11.5, MOR)
    ic += f'<line x1="172" y1="23" x2="196" y2="23" stroke="{SOLUK}" stroke-width="1.4"/><path d="M184 23 V48 M36 48 H324" fill="none" stroke="{SOLUK}" stroke-width="1.2"/>'
    cocuk = ['Kâsım', 'Zeynep', 'Rukiyye', 'Ümmü Gülsüm', 'Fâtıma', 'Abdullah']
    for i, c in enumerate(cocuk):
        x = 36 + i * 57.6
        ic += f'<line x1="{x:.1f}" y1="48" x2="{x:.1f}" y2="58" stroke="{SOLUK}" stroke-width="1.2"/>'
        w = 54
        renk = KIR if c == 'Fâtıma' else LAC
        ic += kutu(x - w / 2, 58, w, 34, '#fff', renk if c == 'Fâtıma' else GRI, 6)
        if c == 'Ümmü Gülsüm':
            ic += yazi(x, 72, 'Ümmü', 10.5, renk) + yazi(x, 86, 'Gülsüm', 10.5, renk)
        else:
            ic += yazi(x, 79, c, 10.5, renk)
    ic += yazi(36, 106, '1. çocuk', 9.5, SOLUK, 'middle', True)
    xf = 36 + 4 * 57.6
    ic += f'<path d="M{xf:.1f} 92 V114" stroke="{KIR}" stroke-width="1.2"/>' + kutu(xf - 66, 114, 132, 24, KIR_A, KIR, 6) + yazi(xf, 130, 'Hz. Fâtıma — Hz. Ali', 11, KIR)
    ic += f'<path d="M{xf:.1f} 138 V146 M{xf - 40:.1f} 146 H{xf + 40:.1f} M{xf - 40:.1f} 146 V152 M{xf + 40:.1f} 146 V152" fill="none" stroke="{KIR}" stroke-width="1.2"/>'
    ic += yazi(xf - 40, 166, 'Hz. Hasan', 11, KIR) + yazi(xf + 40, 166, 'Hz. Hüseyin', 11, KIR)
    ic += kutu(10, 140, 150, 40, '#fff', GRI, 6) + yazi(85, 156, 'İbrahim: Medine döneminde', 10, SOLUK, 'middle', True) + yazi(85, 171, 'Hz. Mâriye\'den doğdu.', 10, SOLUK, 'middle', True)
    return svg(ic, 360, 190, 'Peygamberimizin Hz. Hatice den çocukları ve soyunun devamı', 46)


def g_durum():
    m = ('Okulumuza yeni gelen yabancı uyruklu bir öğrenci kantinde ürünün parasını ödedi; '
         'ancak ürünü verilmedi. Türkçeyi az bildiği için derdini anlatamıyor.')
    st = sar(m, 52)
    h = 36 + len(st) * 18
    ic = kutu(2, 2, 356, h, '#fff', TUR, 8, 1.1) + f'<rect x="2" y="2" width="356" height="22" rx="8" fill="{TUR}"/><rect x="2" y="14" width="356" height="10" fill="{TUR}"/>'
    ic += yazi(16, 18, 'Durum', 12, '#fff', 'start')
    for i, t in enumerate(st):
        ic += yazi(16, 44 + i * 18, t, 12, LAC, 'start', True)
    return svg(ic, 360, h + 4, 'Kantinde haksızlığa uğrayan öğrenci', (h + 4) * 0.3)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_serit()
    s[2]['gorsel'] = g_akis()
    s[5]['gorsel'] = g_ilke()
    s[7]['gorsel'] = g_ridâ()
    s[10]['gorsel'] = g_aile()
    s[12]['gorsel'] = g_durum()
