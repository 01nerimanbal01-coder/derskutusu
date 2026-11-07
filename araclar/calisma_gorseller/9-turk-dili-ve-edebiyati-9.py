"""9. sınıf Türk Dili ve Edebiyatı 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu).

viewBox genişliği 360 birim ≈ yarım sütun; 12 birimlik yazı ≈ 8,5–9 pt. Metin parçaları Ders Kutusu için özgün yazılmıştır.
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


def g_metin():
    m = ('Bekleme salonlarını severim. Herkes bir yere yetişmeye çalışırken orada zaman, kimsenin acelesine aldırmadan '
         'ağır ağır akar. Belki de sabrı en iyi, saatin yavaşladığını sandığımız böyle yerlerde öğreniyoruz. '
         'Siz hiç beklemenin de bir yolculuk olduğunu düşündünüz mü?')
    st = sar(m, 57)
    h = 30 + len(st) * 18
    ic = kutu(2, 2, 356, h, '#fffaf0', TUR, 8, 1)
    ic += f'<rect x="2" y="2" width="5" height="{h}" fill="{TUR}"/>'
    for i, s in enumerate(st):
        ic += yazi(18, 26 + i * 18, s, 12, LAC, 'start', True)
    return svg(ic, 360, h + 4, 'Deneme türünde özgün bir metin parçası', 6 + h * 0.25)


def g_zihin():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    cx, cy = 180, 78
    dal = [('sabır', -150, MAVI), ('zaman algısı', -30, YES), ('istasyonlar', 30, MOR), ('yolculuk', 150, TUR), ('sessizlik', 90, KIR), ('beklenen kişi', -90, MAVI)]
    for ad, a, c in dal:
        x, y = cx + 128 * math.cos(math.radians(a)), cy + 58 * math.sin(math.radians(a))
        ic += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{c}" stroke-width="1.4"/>'
        w = len(ad) * 7.2 + 16
        ic += kutu(x - w / 2, y - 11, w, 22, '#fff', c, 11, 1.1) + yazi(x, y + 4, ad, 11.5, c)
    ic += kutu(cx - 44, cy - 14, 88, 28, MAVI, MAVI, 14) + yazi(cx, cy + 5, 'BEKLEMEK', 12.5, '#fff')
    return svg(ic, 360, 154, 'Bekleme kavramı etrafında hazırlanmış çalışma', 38)


def g_rubrik():
    sat = [('Hazırlık', 4), ('Göz teması', 3), ('Vurgu ve tonlama', 1), ('İçerik tutarlılığı', 4), ('Süre yönetimi', 3)]
    ic = kutu(2, 2, 356, 156, '#fff', MAVI, 8, 1)
    ic += f'<rect x="2" y="2" width="356" height="24" rx="8" fill="{MAVI}"/><rect x="2" y="16" width="356" height="10" fill="{MAVI}"/>'
    ic += yazi(16, 19, 'Ölçüt', 11.5, '#fff', 'start') + yazi(262, 19, 'Puan (1-4)', 11.5, '#fff')
    for i, (a, p) in enumerate(sat):
        y = 48 + i * 24
        ic += yazi(16, y, a, 11.5, LAC, 'start', True)
        for j in range(4):
            c = (KIR if p == 1 else YES) if j < p else '#e4e8f0'
            ic += f'<rect x="{200 + j * 30}" y="{y - 12}" width="26" height="15" rx="3" fill="{c}"/>'
        ic += yazi(334, y, f'{p}', 12, KIR if p == 1 else LAC)
        ic += f'<line x1="10" y1="{y + 8}" x2="350" y2="{y + 8}" stroke="#e1e6f0" stroke-width="0.7"/>'
    return svg(ic, 360, 160, 'Bir öğrencinin konuşmasına ait dereceli puanlama sonucu', 38)


def sapka(x, y, renk, cizgi):
    return (f'<ellipse cx="{x}" cy="{y + 8}" rx="16" ry="4" fill="{renk}" stroke="{cizgi}" stroke-width="1"/>'
            f'<path d="M{x - 10} {y + 7} C{x - 10} {y - 8} {x + 10} {y - 8} {x + 10} {y + 7} z" fill="{renk}" stroke="{cizgi}" stroke-width="1"/>')


def g_sapka():
    not_ = [('Beyaz', '#ffffff', '#8a93a6', 'Kütüphaneyi günde 120 öğrenci kullanıyor.'),
            ('Kırmızı', '#e5484d', '#a32a2e', 'Akşam sessizliğinde okumak bana huzur verir.'),
            ('Siyah', '#2b2f3a', '#111', 'Akşam için görevli sayısı yetersiz kalabilir.'),
            ('Sarı', '#ffd23f', '#b48a00', 'Sınava hazırlananlar bu saatlerden yararlanır.'),
            ('Yeşil', '#2fae5d', '#1d7a3e', 'Kütüphane şu anda saat 18.00\'de kapanıyor.')]
    ic = kutu(2, 2, 356, 196, GRI_A, GRI, 8)
    for i, (ad, r, c, t) in enumerate(not_):
        y = 10 + i * 37
        ic += kutu(8, y, 344, 32, '#fff', '#d5dbe6', 6)
        ic += sapka(30, y + 12, r, c) + yazi(54, y + 20, ad, 11.5, LAC if ad != 'Beyaz' else SOLUK, 'start')
        ic += yazi(112, y + 20, t, 11, LAC, 'start', True)
    return svg(ic, 360, 200, 'Altı şapkalı düşünme notları', 48)


def g_5n1k():
    sat = [('Kim?', 'Satıcılar, alışveriş yapan komşular'), ('Ne?', 'Haftada bir kurulan semt pazarı'), ('Nerede?', 'Okulun arka sokağı'),
           ('Ne zaman?', 'Her cumartesi sabahı'), ('Nasıl?', 'Tezgâhlar sabah erkenden sıralanır'), ('…?', '……………………………')]
    ic = kutu(2, 2, 356, 168, GRI_A, GRI, 8)
    for i, (s, c) in enumerate(sat):
        y = 10 + i * 26
        renk = KIR if s == '…?' else MAVI
        ic += kutu(10, y, 84, 22, MAVI_A if s != '…?' else KIR_A, renk, 5) + yazi(52, y + 15.5, s, 11.5, renk)
        ic += kutu(100, y, 250, 22, '#fff', '#d5dbe6', 5) + yazi(110, y + 15.5, c, 11, LAC if s != '…?' else SOLUK, 'start', True)
    return svg(ic, 360, 172, 'Mahalle pazarları konulu 5N1K çalışması', 42)


def g_oz():
    sat = ['Konuşmamda "şey" kelimesini 9 kez kullandım.', 'Yalnız ön sıralardaki arkadaşlarımla göz teması kurdum.',
           'Konuşmam planlanan süreyi 2 dakika aştı.', 'Giriş bölümüm ilgi çekiciydi.']
    ic = kutu(2, 2, 356, 132, '#fffdf2', '#d9c27a', 6, 1)
    for i in range(6):
        ic += f'<line x1="12" y1="{40 + i * 20}" x2="348" y2="{40 + i * 20}" stroke="#ece2bf" stroke-width="0.8"/>'
    ic += yazi(16, 24, 'Öz değerlendirme notum', 12.5, TUR, 'start')
    for i, s in enumerate(sat):
        ic += yazi(22, 56 + i * 20, '• ' + s, 11.5, LAC, 'start', True)
    return svg(ic, 360, 136, 'Bir öğrencinin öz değerlendirme notu', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g_metin()
    s[2]['gorsel'] = g_zihin()
    s[5]['gorsel'] = g_rubrik()
    s[7]['gorsel'] = g_sapka()
    s[10]['gorsel'] = g_5n1k()
    s[12]['gorsel'] = g_oz()
