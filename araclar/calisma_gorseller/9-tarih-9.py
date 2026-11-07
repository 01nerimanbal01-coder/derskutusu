"""9. sınıf Tarih 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12 birimlik yazı ≈ 8,5–9 pt. Grafik ve ağ verileri öğretim amaçlı örnek veridir.
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


def g_siklik():
    yil = [1860, 1870, 1880, 1890, 1900, 1910, 1920]
    tel = [4, 10, 18, 24, 27, 27, 26]
    dem = [2, 3, 5, 8, 20, 31, 36]
    ic = kutu(2, 2, 356, 190, GRI_A, GRI, 8)
    ox, oy, en, boy = 46, 156, 290, 124
    for j in (10, 20, 30, 40):
        y = oy - j * boy / 40
        ic += f'<line x1="{ox}" y1="{y:.1f}" x2="{ox + en}" y2="{y:.1f}" stroke="#dfe4ee" stroke-width="0.6"/>' + yazi(ox - 6, y + 4, str(j), 10, SOLUK, 'end', True)
    ic += f'<line x1="{ox}" y1="{oy}" x2="{ox + en}" y2="{oy}" stroke="{LAC}"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - boy - 6}" stroke="{LAC}"/>'
    for i, y_ in enumerate(yil):
        ic += yazi(ox + 12 + i * 44, oy + 15, str(y_), 10, SOLUK, ince=True)
    for veri, c in ((tel, TUR), (dem, MAVI)):
        p = ' '.join(f'{ox + 12 + i * 44:.1f},{oy - v * boy / 40:.1f}' for i, v in enumerate(veri))
        ic += f'<polyline points="{p}" fill="none" stroke="{c}" stroke-width="2.2"/>'
        for i, v in enumerate(veri):
            ic += f'<circle cx="{ox + 12 + i * 44:.1f}" cy="{oy - v * boy / 40:.1f}" r="2.8" fill="{c}"/>'
    ic += yazi(ox + 4, 20, '1000 sayfada geçme sayısı', 10.5, SOLUK, 'start', True)
    ic += f'<rect x="62" y="40" width="12" height="4" fill="{TUR}"/>' + yazi(80, 46, 'telgraf', 11.5, TUR, 'start')
    ic += f'<rect x="62" y="58" width="12" height="4" fill="{MAVI}"/>' + yazi(80, 64, 'demiryolu', 11.5, MAVI, 'start')
    ic += yazi(346, 186, 'Yıl', 10.5, SOLUK, 'end', True)
    return svg(ic, 360, 194, 'Gazetelerde iki kelimenin yıllara göre geçme sıklığı', 46)


def g_ag():
    n = {'İstanbul': (176, 96), 'Bursa': (90, 146), 'Venedik': (56, 56), 'Halep': (284, 146), 'Tebriz': (300, 52), 'Kefe': (176, 24)}
    k = [('İstanbul', 'Bursa'), ('İstanbul', 'Venedik'), ('İstanbul', 'Halep'), ('İstanbul', 'Kefe'), ('Halep', 'Tebriz'), ('Bursa', 'Venedik'), ('Bursa', 'Halep')]
    ic = kutu(2, 2, 356, 168, GRI_A, GRI, 8)
    for a, b in k:
        (x1, y1), (x2, y2) = n[a], n[b]
        ic += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#8aa0c2" stroke-width="1.6"/>'
    for ad, (x, y) in n.items():
        w = len(ad) * 7.6 + 16
        c = MAVI if ad == 'İstanbul' else MOR
        ic += kutu(x - w / 2, y - 12, w, 24, '#fff', c, 12, 1.3) + yazi(x, y + 4.5, ad, 12, c)
    ic += yazi(346, 164, 'örnek veri', 10, SOLUK, 'end', True)
    return svg(ic, 360, 172, 'Ticaret merkezleri arasındaki bağlantıları gösteren ağ haritası', 42)


def g_kart():
    sat = [('Belge türü', 'Ferman'), ('Tarih', '1577'), ('Dil', 'Osmanlı Türkçesi'), ('Arşiv fon kodu', 'ÖRN.0423 - Dosya 17'), ('Sayfa', '2 varak'), ('Erişim', 'Dijital arşiv, görüntü + metin')]
    ic = kutu(2, 2, 356, 168, '#fff', MAVI, 8, 1.2)
    ic += f'<rect x="2" y="2" width="356" height="26" rx="8" fill="{MAVI}"/><rect x="2" y="18" width="356" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 20, 'Belge kayıt kartı (üst veri)', 12.5, '#fff')
    for i, (a, b) in enumerate(sat):
        y = 50 + i * 21
        ic += yazi(16, y, a, 11.5, MAVI, 'start') + yazi(138, y, b, 11.5, LAC, 'start', True)
        ic += f'<line x1="12" y1="{y + 7}" x2="348" y2="{y + 7}" stroke="#e1e6f0" stroke-width="0.7"/>'
    return svg(ic, 360, 172, 'Dijital arşivdeki bir belgenin kayıt kartı', 42)


def g_paylasim():
    ic = kutu(2, 2, 356, 196, '#fff', GRI, 10, 1)
    ic += f'<circle cx="22" cy="22" r="10" fill="{MAVI_A}" stroke="{MAVI}"/>' + yazi(38, 20, 'tarihmeraklisi_42', 11.5, LAC, 'start')
    ic += yazi(38, 34, '"1908 yılında çekilmiş İstanbul sokağı!"', 11, LAC, 'start', True)
    ic += '<rect x="12" y="44" width="336" height="128" rx="4" fill="#f3e6cf"/>'
    ic += '<rect x="30" y="74" width="110" height="98" fill="#d9b98c" stroke="#9c7a4c"/><path d="M24 76 L85 50 L146 76 z" fill="#b5523b"/>'
    for x in (44, 76, 108):
        ic += f'<rect x="{x}" y="88" width="18" height="24" fill="#fff8e8" stroke="#9c7a4c"/>'
    ic += '<rect x="76" y="132" width="20" height="40" fill="#7a5532"/>'
    ic += '<rect x="196" y="64" width="130" height="108" fill="#e2c9a0" stroke="#9c7a4c"/>'
    for x in (210, 246, 282):
        ic += f'<rect x="{x}" y="80" width="22" height="28" fill="#fff8e8" stroke="#9c7a4c"/>'
    ic += '<ellipse cx="300" cy="134" rx="15" ry="11" fill="#c8ccd4" stroke="#6c7280" transform="rotate(-25 300 134)"/><line x1="300" y1="134" x2="312" y2="124" stroke="#6c7280" stroke-width="1.4"/>'
    ic += f'<line x1="300" y1="148" x2="300" y2="190" stroke="{KIR}" stroke-width="0.8"/>'
    ic += '<path d="M12 172 h336" stroke="#9c7a4c"/>'
    ic += yazi(306, 192, '?', 12, KIR, 'start') + yazi(20, 192, '♥ 12 bin beğeni · 3 bin paylaşım', 10.5, KIR, 'start', True)
    return svg(ic, 360, 200, 'Sosyal medyada paylaşılan, 1908 tarihli olduğu söylenen fotoğraf', 48)


def g_iki():
    ic = kutu(2, 2, 356, 130, GRI_A, GRI, 8)
    kart = [('1975: Araştırmacı A', ['Arşive trenle gider', 'Belgeyi büyüteçle okur', 'Notları fişlere yazar', 'Basılı kitap yayımlar'], TUR, TUR_A),
            ('2025: Araştırmacı B', ['Veri tabanında arar', 'Belgeyi OCR ile tarar', 'Verileri tabloya işler', 'Etkileşimli site kurar'], MAVI, MAVI_A)]
    for i, (b, m, c, a) in enumerate(kart):
        x = 8 + i * 176
        ic += kutu(x, 8, 168, 118, a, c, 7) + yazi(x + 84, 28, b, 12, c)
        for j, t in enumerate(m):
            ic += f'<circle cx="{x + 14}" cy="{48 + j * 21}" r="2.6" fill="{c}"/>' + yazi(x + 22, 52 + j * 21, t, 11, LAC, 'start', True)
    return svg(ic, 360, 134, 'İki araştırmacının çalışma biçimi', 34)


def g_katman():
    ic = kutu(2, 2, 356, 176, GRI_A, GRI, 8)
    adlar = [('3. katman: 1890 nüfus defteri köyleri', KIR), ('2. katman: 1830 nüfus defteri köyleri', MAVI), ('1. katman: akarsu ve yol haritası', YES)]
    for i, (ad, c) in enumerate(adlar):
        y = 12 + i * 54
        ic += f'<path d="M40 {y + 40} L100 {y} L330 {y} L270 {y + 40} z" fill="#fff" fill-opacity="0.94" stroke="{c}" stroke-width="1.3"/>'
        ic += yazi(205, y + 15, ad, 11, c)
        if i < 2:
            for dx, dy in ((96, 30), (140, 26), (176, 32), (214, 24), (250, 30))[i:]:
                ic += f'<circle cx="{dx}" cy="{y + dy}" r="3.4" fill="{c}"/>'
        else:
            ic += f'<path d="M70 {y + 34} C120 {y + 26} 170 {y + 36} 250 {y + 26}" fill="none" stroke="#3a9fd0" stroke-width="2"/>'
            ic += f'<path d="M100 {y + 24} L292 {y + 22}" stroke="#a0876a" stroke-width="1.6" stroke-dasharray="4 3"/>'
    return svg(ic, 360, 180, 'H-GIS projesinin üç katmanı', 42)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_siklik()
    s[2]['gorsel'] = g_ag()
    s[5]['gorsel'] = g_kart()
    s[7]['gorsel'] = g_paylasim()
    s[10]['gorsel'] = g_iki()
    s[12]['gorsel'] = g_katman()
