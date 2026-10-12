"""7. sınıf Fen Bilimleri, 4. hafta: yıldız, galaksi ve evren kavramları.

Görseller yalnız haftanın metnindeki bilgilerle çizilir:
- Yıldız rengi ve sıcaklığı: mavi = sıcak yüzey, turuncu = soğuk yüzey; yıldızların kendi renkleri (beyaz, sarı, kırmızı) doğrudan çizilir.
- Işık yılı şeridi: tek ölçek (1 ışık yılı = 88 birim); Dünya ile Proxima Centauri arası 4,24 ışık yılıdır.
- Büyükayı ve Kutup Yıldızı: yıldız konumları gerçek gökyüzü açılarından yansıtılmıştır; Kutup Yıldızı, uçtaki iki yıldızın arasındaki
  uzaklığın tam 5 katı kadar ileriye konur (tek ölçek).
- Galaksiler: Andromeda'nın çapı Samanyolu'nun tam 2 katı çizilir (tek ölçek); mavi = galaksi (Samanyolu ve Andromeda), yeşil = Güneş sistemi.
- Kapsama şeması: mor = evren, mavi = galaksi, yeşil = Güneş sistemi, turuncu = yıldız, küçük mavi nokta = Dünya.
Boyutlar dışında ölçek iddiası yoktur.
"""
import math

from ozet_gorsel import svg, ok_isareti


def _ok(x1, y1, x2, y2, sinif, kimlik, w=2.2):
    """Ok başı hedefe değecek biçimde kısaltılmış çizgi (ok başı ucu çizgi ucundan 1,8·w ileridedir)."""
    dx, dy = x2 - x1, y2 - y1
    u = math.hypot(dx, dy)
    ex, ey = x2 - dx / u * 1.8 * w, y2 - dy / u * 1.8 * w
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{ex:.1f}" y2="{ey:.1f}" class="{sinif}" stroke-width="{w}" '
            f'stroke-linecap="round" marker-end="url(#{kimlik})"/>')


def _cift_ok(x1, y1, x2, y2, sinif, kimlik, w=2.2):
    """İki ucu da ok başlı çizgi; uçlar hedeflere değecek biçimde kısaltılmıştır."""
    dx, dy = x2 - x1, y2 - y1
    u = math.hypot(dx, dy)
    k = 1.8 * w
    a = (x1 + dx / u * k, y1 + dy / u * k)
    b = (x2 - dx / u * k, y2 - dy / u * k)
    return (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="{sinif}" stroke-width="{w}" '
            f'stroke-linecap="round" marker-start="url(#{kimlik})" marker-end="url(#{kimlik})"/>')


def _yazi(x, y, metin, boyut, sinif, anchor='middle', kalin=False):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}"{a} font-size="{boyut:g}"{k} class="{sinif}">{metin}</text>'


# ---------- 1) Yıldızların rengi ve sıcaklığı ----------
def renk_sicaklik():
    """Beş yıldız diski (mavi, beyaz, sarı, turuncu, kırmızı) yüzey sıcaklığı ekseninde; üç sıcaklık bölgesi."""
    ic = '<defs>' + ok_isareti('f74a', 'g-s') + '</defs>'
    ic += _yazi(30, 16, 'yüksek', 12, 'g-mf', 'start', True)
    ic += _yazi(230, 16, 'yüzey sıcaklığı', 12, 'g-s')
    ic += _yazi(430, 16, 'düşük', 12, 'g-tf', 'end', True)
    ic += _ok(30, 30, 430, 30, 'g-c', 'f74a', 2.4)
    cx = [62, 146, 230, 314, 398]
    cy = 78
    # mavi, beyaz, sarı, turuncu, kırmızı (yıldızın görünen rengi)
    ic += f'<circle cx="{cx[0]}" cy="{cy}" r="26" class="g-mf"/>'
    ic += f'<circle cx="{cx[1]}" cy="{cy}" r="26" class="g-b"/><circle cx="{cx[1]}" cy="{cy}" r="26" class="g-c" stroke-width="2"/>'
    ic += f'<circle cx="{cx[2]}" cy="{cy}" r="26" fill="#f5c421"/>'
    ic += f'<circle cx="{cx[3]}" cy="{cy}" r="26" class="g-tf"/>'
    ic += f'<circle cx="{cx[4]}" cy="{cy}" r="26" fill="#d93a2f"/>'
    for x, ad in zip(cx, ('mavi', 'beyaz', 'sarı', 'turuncu', 'kırmızı')):
        ic += _yazi(x, 122, ad, 13, 'g-y', kalin=True)
    # sıcaklık bölgeleri: ayraç çizgileri ve etiketler
    for x0, x1, ad, sinif in ((36, 172, 'sıcak yüzey', 'g-mf'), (204, 256, 'orta sıcaklık', 'g-yf'), (288, 424, 'soğuk yüzey', 'g-tf')):
        ic += (f'<line x1="{x0}" y1="134" x2="{x1}" y2="134" class="g-c" stroke-width="2" stroke-linecap="round"/>'
               f'<line x1="{x0}" y1="130" x2="{x0}" y2="134" class="g-c" stroke-width="2" stroke-linecap="round"/>'
               f'<line x1="{x1}" y1="130" x2="{x1}" y2="134" class="g-c" stroke-width="2" stroke-linecap="round"/>')
        ic += _yazi((x0 + x1) / 2, 153, ad, 13, sinif, kalin=True)
    ic += _yazi(104, 170, 'genç ya da büyük', 11, 'g-s') + _yazi(104, 184, 'kütleli yıldızlar', 11, 'g-s')
    ic += _yazi(230, 170, 'Güneş', 11, 'g-s') + _yazi(230, 184, 'sarı-turuncu', 11, 'g-s')
    ic += _yazi(356, 170, 'kırmızı dev hâline', 11, 'g-s') + _yazi(356, 184, 'gelmiş yıldızlar', 11, 'g-s')
    return svg(460, 194, ic, 'Yıldızların rengi yüzey sıcaklığına göre değişir. Sıcak yüzeyli yıldızlar mavi ya da beyaz, orta sıcaklıktakiler sarı, '
               'soğuk yüzeyli yıldızlar turuncu ya da kırmızı görünür. Genç ya da büyük kütleli yıldızlar sıcak ve mavi, kırmızı dev hâline gelmiş yıldızlar '
               'soğuk ve kırmızıdır; Güneş sarı-turuncudur.')


# ---------- 2) Işık yılı şeridi (tek ölçek) ----------
def isik_yili():
    """Dünya'dan Proxima Centauri'ye: her parça 1 ışık yılı; toplam 4,24 ışık yılı. 1 ışık yılı = 88 birim."""
    U = 88.0
    x0 = 34.0
    x1 = x0 + 4.24 * U
    ic = _yazi(230, 16, 'Her tam parça 1 ışık yılı: yaklaşık 9,46 trilyon km', 12, 'g-s')
    # şerit: dört tam parça ve 0,24'lük kalan parça
    for i in range(5):
        a = x0 + i * U
        b = min(x0 + (i + 1) * U, x1)
        koyu = (i % 2 == 0)
        ic += (f'<rect x="{a:.1f}" y="60" width="{b - a:.1f}" height="12" class="{"g-yf" if koyu else "g-ya"}"/>'
               f'<rect x="{a:.1f}" y="60" width="{b - a:.1f}" height="12" class="g-ys" stroke-width="1.5"/>')
    # Dünya ve Proxima Centauri
    ic += f'<circle cx="{x0:g}" cy="66" r="15" class="g-mf"/>'
    ic += f'<circle cx="{x1:.1f}" cy="66" r="9" class="g-ta"/><circle cx="{x1:.1f}" cy="66" r="5" class="g-tf"/>'
    # cetvel: 1, 2, 3, 4 ve 4,24
    for i in range(1, 5):
        x = x0 + i * U
        ic += f'<line x1="{x:.1f}" y1="74" x2="{x:.1f}" y2="80" class="g-c" stroke-width="1.6"/>'
        ic += _yazi(round(x, 1), 94, str(i), 12, 'g-s')
    ic += f'<line x1="{x1:.1f}" y1="82" x2="{x1:.1f}" y2="86" class="g-c" stroke-width="1.6"/>'
    ic += _yazi(round(x1 + 8, 1), 99, '4,24', 12, 'g-tf', kalin=True)
    ic += _yazi(x0, 108, 'Dünya', 13, 'g-mf', kalin=True)
    ic += _yazi(round(x1, 1), 118, 'Proxima', 13, 'g-tf', kalin=True) + _yazi(round(x1, 1), 133, 'Centauri', 13, 'g-tf', kalin=True)
    # toplam uzaklık ayracı
    ic += (f'<line x1="{x0:g}" y1="146" x2="{x1:.1f}" y2="146" class="g-c" stroke-width="2" stroke-linecap="round"/>'
           f'<line x1="{x0:g}" y1="141" x2="{x0:g}" y2="146" class="g-c" stroke-width="2" stroke-linecap="round"/>'
           f'<line x1="{x1:.1f}" y1="141" x2="{x1:.1f}" y2="146" class="g-c" stroke-width="2" stroke-linecap="round"/>')
    ic += _yazi(round((x0 + x1) / 2, 1), 165, '4,24 ışık yılı: yaklaşık 40 trilyon km', 12.5, 'g-y', kalin=True)
    return svg(460, 174, ic, 'Dünya ile Proxima Centauri arasındaki uzaklık tek ölçekle gösterilmiştir: her parça bir ışık yılıdır ve yaklaşık '
               '9,46 trilyon km eder. Dört tam parça ve küçük bir kalan parça, toplam 4,24 ışık yılı ya da yaklaşık 40 trilyon km yapar.')


# ---------- 3) Büyükayı ve Kutup Yıldızı ----------
def buyukayi():
    """Yedi yıldızlı Büyükayı (cezve) ve Kutup Yıldızı. Konumlar gerçek (RA, Dec) değerlerinden izdüşümle bulunur;
    Kutup Yıldızı, uçtaki iki yıldızın arası uzaklığın tam 5 katı kadar ileriye konur."""
    S = {'Dubhe': (165.93, 61.75), 'Merak': (165.46, 56.38), 'Phecda': (178.46, 53.69), 'Megrez': (183.86, 57.03),
         'Alioth': (193.51, 55.96), 'Mizar': (200.98, 54.93), 'Alkaid': (206.89, 49.31)}
    c = math.cos(math.radians(56))
    P = {k: ((190 - ra) * c, dec) for k, (ra, dec) in S.items()}
    d = (P['Dubhe'][0] - P['Merak'][0], P['Dubhe'][1] - P['Merak'][1])
    dl = math.hypot(*d)
    P['Polaris'] = (P['Dubhe'][0] + 5 * d[0], P['Dubhe'][1] + 5 * d[1])
    rot = math.radians(48) - math.atan2(d[1], d[0])
    Q = {k: (x * math.cos(rot) - y * math.sin(rot), x * math.sin(rot) + y * math.cos(rot)) for k, (x, y) in P.items()}
    xmin = min(v[0] for v in Q.values()); ymin = min(v[1] for v in Q.values())
    s = 8.6

    def T(k):
        return (30 + (Q[k][0] - xmin) * s, 236 - (Q[k][1] - ymin) * s)
    pt = {k: T(k) for k in Q}
    dpx = dl * s  # iki uç yıldız arası, piksel
    u = ((pt['Polaris'][0] - pt['Dubhe'][0]) / (5 * dpx), (pt['Polaris'][1] - pt['Dubhe'][1]) / (5 * dpx))  # birim vektör
    n = (-u[1], u[0])  # doğrultuya dik, sağ-alt yön (ekran)
    if n[0] < 0:
        n = (-n[0], -n[1])
    ic = ''
    # cezve çizgileri: kâse ve sap
    def cizgi(a, b):
        return f'<line x1="{pt[a][0]:.1f}" y1="{pt[a][1]:.1f}" x2="{pt[b][0]:.1f}" y2="{pt[b][1]:.1f}" class="g-c" stroke-width="2.4" stroke-linecap="round"/>'
    for a, b in (('Merak', 'Phecda'), ('Phecda', 'Megrez'), ('Megrez', 'Dubhe'), ('Dubhe', 'Merak'),
                 ('Megrez', 'Alioth'), ('Alioth', 'Mizar'), ('Mizar', 'Alkaid')):
        ic += cizgi(a, b)
    # 5 eşit parça: Dubhe'den Kutup Yıldızı'na kesik çizgi ve işaretler
    ic += (f'<line x1="{pt["Dubhe"][0]:.1f}" y1="{pt["Dubhe"][1]:.1f}" x2="{pt["Polaris"][0]:.1f}" y2="{pt["Polaris"][1]:.1f}" '
           f'class="g-ts" stroke-width="2.4" stroke-dasharray="7 5"/>')
    for k in range(1, 5):
        tx = pt['Dubhe'][0] + u[0] * dpx * k
        ty = pt['Dubhe'][1] + u[1] * dpx * k
        ic += (f'<line x1="{tx - n[0] * 6:.1f}" y1="{ty - n[1] * 6:.1f}" x2="{tx + n[0] * 6:.1f}" y2="{ty + n[1] * 6:.1f}" '
               f'class="g-ts" stroke-width="2.4" stroke-linecap="round"/>')
        ic += _yazi(round(tx + n[0] * 15, 1), round(ty + n[1] * 15 + 4, 1), str(k), 12, 'g-tf', kalin=True)
    # uçtaki iki yıldızın arası: ayraç
    a = (pt['Merak'][0] + n[0] * 16, pt['Merak'][1] + n[1] * 16)
    b = (pt['Dubhe'][0] + n[0] * 16, pt['Dubhe'][1] + n[1] * 16)
    ic += (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="g-ts" stroke-width="2.4" stroke-linecap="round"/>'
           f'<line x1="{a[0] - n[0] * 5:.1f}" y1="{a[1] - n[1] * 5:.1f}" x2="{a[0] + n[0] * 5:.1f}" y2="{a[1] + n[1] * 5:.1f}" class="g-ts" stroke-width="2.4" stroke-linecap="round"/>'
           f'<line x1="{b[0] - n[0] * 5:.1f}" y1="{b[1] - n[1] * 5:.1f}" x2="{b[0] + n[0] * 5:.1f}" y2="{b[1] + n[1] * 5:.1f}" class="g-ts" stroke-width="2.4" stroke-linecap="round"/>')
    # yıldızlar
    for k in ('Phecda', 'Megrez', 'Alioth', 'Mizar', 'Alkaid'):
        ic += f'<circle cx="{pt[k][0]:.1f}" cy="{pt[k][1]:.1f}" r="5.5" class="g-mf"/>'
    for k in ('Merak', 'Dubhe'):
        ic += f'<circle cx="{pt[k][0]:.1f}" cy="{pt[k][1]:.1f}" r="7" class="g-tf"/>'
    ic += f'<circle cx="{pt["Polaris"][0]:.1f}" cy="{pt["Polaris"][1]:.1f}" r="14" class="g-ya"/><circle cx="{pt["Polaris"][0]:.1f}" cy="{pt["Polaris"][1]:.1f}" r="8" class="g-yf"/>'
    # etiketler
    ic += _yazi(round(pt['Mizar'][0] - 4, 1), round(pt['Mizar'][1] - 32, 1), 'Büyükayı', 13, 'g-mf', 'middle', True)
    ic += _yazi(round(pt['Mizar'][0] - 4, 1), round(pt['Mizar'][1] - 18, 1), 'yedi yıldız', 12, 'g-mf', 'middle')
    ic += _yazi(round(pt['Polaris'][0] - 22, 1), round(pt['Polaris'][1] + 5, 1), 'Kutup Yıldızı', 13, 'g-yf', 'end', True)
    ic += _yazi(round(pt['Polaris'][0] + 4, 1), round(pt['Polaris'][1] + 36, 1), '5', 12, 'g-tf', 'start', True)
    ic += _yazi(round(b[0] + 16, 1), round(b[1] + 22, 1), 'uçtaki iki yıldızın arası', 12, 'g-tf', 'start', True)
    ic += _yazi(round(pt['Dubhe'][0] + u[0] * dpx * 2.5 - n[0] * 20, 1), round(pt['Dubhe'][1] + u[1] * dpx * 2.5 - n[1] * 20 - 2, 1),
                'bu uzaklığın 5 katı', 12, 'g-tf', 'end', True)
    return svg(460, 262, ic, 'Büyükayı takımyıldızı yedi yıldızdan oluşan bir cezve biçimindedir. Cezvenin ucundaki iki yıldız arasındaki uzaklığın '
               '5 katı kadar ileride parlak Kutup Yıldızı bulunur.')


# ---------- 4) Samanyolu ve Andromeda ----------
def _kol(cx, cy, R, th0, tur=1.5, r0=0.14, n=90):
    pts = []
    for i in range(n + 1):
        t = i / n
        a = th0 + tur * 2 * math.pi * t
        r = R * (r0 + (1 - r0) * t)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def _galaksi(cx, cy, R, dolgu, cizgi, ses, kalinlik):
    ic = f'<circle cx="{cx}" cy="{cy}" r="{R}" class="{dolgu}"/><circle cx="{cx}" cy="{cy}" r="{R}" class="{cizgi}" stroke-width="1.8"/>'
    for th0 in (0, math.pi):
        pts = _kol(cx, cy, R - 4, th0)
        ic += (f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" class="{cizgi}" stroke-width="{kalinlik}" '
               f'stroke-linecap="round" stroke-linejoin="round"/>')
    ic += f'<circle cx="{cx}" cy="{cy}" r="{R * 0.14:.1f}" class="{ses}"/>'
    return ic


def galaksiler():
    """İki sarmal galaksi tek ölçekle: Andromeda'nın çapı Samanyolu'nun tam 2 katı; Güneş sistemi Samanyolu'nun Avcı kolunda."""
    ic = '<defs>' + ok_isareti('f74b', 'g-mf') + ok_isareti('f74d', 'g-s') + '</defs>'
    cs, rs = (90, 112), 45
    ca, ra = (335, 112), 90
    ic += _galaksi(cs[0], cs[1], rs, 'g-ma', 'g-ms', 'g-mf', 3.4)
    ic += _galaksi(ca[0], ca[1], ra, 'g-ma', 'g-ms', 'g-mf', 5.6)
    # Güneş sistemi: Samanyolu'nun bir kolu üzerinde
    pts = _kol(cs[0], cs[1], rs - 4, 0)
    gx, gy = pts[int(len(pts) * 0.62)]
    ic += f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="5.5" class="g-yf"/>'
    ic += f'<line x1="{gx - 8:.1f}" y1="{gy - 9:.1f}" x2="104" y2="40" class="g-ys" stroke-width="1.6" stroke-linecap="round"/>'
    ic += _yazi(90, 16, 'Güneş sistemi', 13, 'g-yf', 'middle', True)
    ic += _yazi(90, 32, 'Avcı (Orion) kolunda', 11.5, 'g-s')
    # en yakın galaksi
    ic += _yazi(190, 98, 'en yakın', 12, 'g-s') + _yazi(190, 113, 'galaksi', 12, 'g-s')
    ic += _cift_ok(145, 126, 235, 126, 'g-c', 'f74d', 2)
    # çap çizgileri (tek ölçek): Samanyolu 90, Andromeda 180
    ic += _cift_ok(cs[0] - rs, 216, cs[0] + rs, 216, 'g-ms', 'f74b', 2.2)
    ic += _cift_ok(ca[0] - ra, 216, ca[0] + ra, 216, 'g-ms', 'f74b', 2.2)
    ic += _yazi(cs[0], 238, 'Samanyolu galaksisi', 13, 'g-mf', 'middle', True) + _yazi(cs[0], 254, 'çap: 1 birim', 12, 'g-s')
    ic += _yazi(ca[0], 238, 'Andromeda galaksisi', 13, 'g-mf', 'middle', True) + _yazi(ca[0], 254, 'çap: yaklaşık 2 birim', 12, 'g-s')
    return svg(460, 262, ic, 'İki sarmal galaksi tek ölçekle çizilmiştir: Andromeda galaksisinin çapı Samanyolu galaksisinin çapının yaklaşık iki katıdır. '
               'Güneş sistemi, Samanyolu galaksisinin Avcı (Orion) kolundadır. Andromeda, Samanyolu\'na en yakın galaksidir.')


# ---------- 5) Evren, galaksi, Güneş sistemi, Dünya iç içe ----------
def kapsama():
    """Evren > galaksi (Samanyolu, Andromeda) > Güneş sistemi > Güneş (yıldız) ve Dünya."""
    ic = '<rect x="4" y="4" width="452" height="292" rx="16" class="g-oa"/><rect x="4" y="4" width="452" height="292" rx="16" class="g-os" stroke-width="2.4"/>'
    ic += _yazi(20, 30, 'Evren', 17, 'g-of', 'start', True)
    # Samanyolu galaksisi
    ic += '<ellipse cx="165" cy="172" rx="150" ry="112" class="g-ma"/><ellipse cx="165" cy="172" rx="150" ry="112" class="g-ms" stroke-width="2.4"/>'
    ic += _yazi(165, 92, 'Samanyolu galaksisi', 13, 'g-mf', 'middle', True)
    # Güneş sistemi
    ic += _yazi(165, 118, 'Güneş sistemi', 12.5, 'g-yf', 'middle', True)
    ic += '<circle cx="165" cy="190" r="64" class="g-ya"/><circle cx="165" cy="190" r="64" class="g-ys" stroke-width="2.4"/>'
    ic += '<circle cx="135" cy="190" r="16" class="g-tf"/>' + _yazi(135, 222, 'Güneş', 12, 'g-tf', 'middle', True)
    ic += '<circle cx="198" cy="186" r="8" class="g-mf"/>' + _yazi(198, 210, 'Dünya', 12, 'g-mf', 'middle', True)
    # diğer yıldızlar
    for x, y in ((56, 172), (90, 182), (70, 158)):
        ic += f'<circle cx="{x}" cy="{y}" r="3.6" class="g-tf"/>'
    ic += _yazi(72, 208, 'diğer', 11.5, 'g-s') + _yazi(72, 222, 'yıldızlar', 11.5, 'g-s')
    # Andromeda galaksisi
    ic += '<ellipse cx="385" cy="172" rx="62" ry="48" class="g-ma"/><ellipse cx="385" cy="172" rx="62" ry="48" class="g-ms" stroke-width="2.4"/>'
    ic += _yazi(385, 170, 'Andromeda', 12.5, 'g-mf', 'middle', True) + _yazi(385, 186, 'galaksisi', 12.5, 'g-mf', 'middle', True)
    ic += _yazi(385, 252, 'Boyutlar', 11, 'g-s') + _yazi(385, 266, 'ölçekli değildir', 11, 'g-s')
    return svg(460, 300, ic, 'İç içe kapsama: evren, galaksileri kapsar (Samanyolu galaksisi ve Andromeda galaksisi). Samanyolu galaksisi, '
               'Güneş sistemini ve diğer yıldızları kapsar. Güneş sisteminde Güneş (bir yıldız) ve Dünya bulunur.')


def uygula(o):
    g = {'Yıldızların rengi ve sıcaklığı': renk_sicaklik(),
         'Işık yılı: uzaklığı ölçmek': isik_yili(),
         'Takımyıldızlar ve yıldız kümeleri': buyukayi(),
         'Galaksi: gök adalar': galaksiler(),
         'Evren ve kapsama ilişkisi': kapsama()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
