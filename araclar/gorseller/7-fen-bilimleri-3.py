"""7. sınıf Fen Bilimleri, 3. hafta: yıldızların yaşamı (doğum aşamaları, yaşam yolları, yaş tahmini yöntemleri).

Görseller yalnız haftanın metnindeki bilgilerle çizilir.
Renk anlamı: bulutsuda mavi = gaz ve toz bulutu, turuncu = ön yıldız ve yıldız evresinin rakamı ve başlığı (ön yıldızın gövdesi donuk kırmızı çizilir); yaşam yolu şemasında mavi = bulutsu,
yeşil = küçük kütleli yıldızın yolu, turuncu = büyük kütleli yıldızın yolu; yaş tahmini görselinde mavi = yöntem başlığı,
yeşil = genç yıldız, turuncu = yaşlı yıldız (dalga çizgisi de yöntem rengiyle mavidir).
Boyutlar ve uzaklıklar ölçekli değildir; ölçü yazan öğe yoktur.
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


def _yay_ok(cx, cy, r, a0, a1, sinif, kimlik, w=2.4):
    """Saat yönünde (ekranda) a0°'den a1°'ye yay; uçta ok başı. Açılar +x ekseninden saat yönünde ölçülür."""
    kisalt = math.degrees(1.8 * w / r)
    a1k = a1 - kisalt
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1k)), cy + r * math.sin(math.radians(a1k)))
    buyuk = 1 if (a1k - a0) > 180 else 0
    return (f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 {buyuk} 1 {p1[0]:.1f} {p1[1]:.1f}" class="{sinif}" '
            f'stroke-width="{w}" stroke-linecap="round" marker-end="url(#{kimlik})"/>')


def _noktalar(cx, cy, r, adet, sinif, nr=2.4):
    """Daire içine altın açı dizilimiyle dağıtılmış küçük noktalar (toz)."""
    s = ''
    for i in range(adet):
        rr = r * math.sqrt((i + .5) / adet)
        a = i * 2.399963
        s += f'<circle cx="{cx + rr * math.cos(a):.1f}" cy="{cy + rr * math.sin(a):.1f}" r="{nr}" class="{sinif}"/>'
    return s


def _kutu(x, y, w, h, metin, dolgu, cizgi, yazi, boyut=13, kalin=True):
    """Yuvarlak köşeli kutu ve ortalanmış tek satır yazı."""
    agirlik = ' font-weight="700"' if kalin else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="{dolgu}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="{cizgi}" stroke-width="2"/>'
            f'<text x="{x + w / 2:g}" y="{y + h / 2 + boyut * .35:.1f}" text-anchor="middle" font-size="{boyut}"{agirlik} class="{yazi}">{metin}</text>')


# ---------- 1) Bulutsudan yıldıza: dört adım ----------
def bulutsudan_yildiza():
    ic = '<defs>' + ok_isareti('f73a', 'g-s') + ok_isareti('f73b', 'g-mf') + '</defs>'
    cx = [56, 168, 280, 392]
    cy = 84
    renk = [('g-mf', 'g-ma', 'g-ms'), ('g-mf', 'g-ma', 'g-ms'), ('g-tf', 'g-ta', 'g-ts'), ('g-tf', 'g-ta', 'g-ts')]
    # adım numaraları
    for k in range(4):
        f, a, s = renk[k]
        ic += f'<circle cx="{cx[k]}" cy="14" r="11" class="{f}"/>'
        ic += f'<text x="{cx[k]}" y="19" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{k + 1}</text>'
    # 1. bulutsu: geniş gaz ve toz bulutu
    ic += f'<circle cx="{cx[0]}" cy="{cy}" r="34" class="g-ma"/><circle cx="{cx[0]}" cy="{cy}" r="34" class="g-ms" stroke-width="2" stroke-dasharray="5 4"/>'
    ic += _noktalar(cx[0], cy, 27, 16, 'g-mf')
    # 2. çökme: küçülen bulut ve içe doğru oklar
    ic += f'<circle cx="{cx[1]}" cy="{cy}" r="14" class="g-ma"/><circle cx="{cx[1]}" cy="{cy}" r="14" class="g-ms" stroke-width="2"/>'
    ic += _noktalar(cx[1], cy, 9, 6, 'g-mf', 2)
    for ac in (45, 135, 225, 315):
        r1, r2 = 34, 21
        x1 = cx[1] + r1 * math.cos(math.radians(ac)); y1 = cy + r1 * math.sin(math.radians(ac))
        x2 = cx[1] + r2 * math.cos(math.radians(ac)); y2 = cy + r2 * math.sin(math.radians(ac))
        ic += _ok(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), 'g-ms', 'f73b', 2)
    # 3. ön yıldız: donuk kırmızı (soluk turuncu)
    ic += f'<circle cx="{cx[2]}" cy="{cy}" r="17" fill="#d93a2f" opacity=".45"/><circle cx="{cx[2]}" cy="{cy}" r="17" fill="none" stroke="#d93a2f" stroke-width="2"/>'
    # 4. yıldız: parlak gövde, merkezde çekirdek, ışınlar
    ic += f'<circle cx="{cx[3]}" cy="{cy}" r="26" class="g-ta"/><circle cx="{cx[3]}" cy="{cy}" r="17" class="g-tf"/><circle cx="{cx[3]}" cy="{cy}" r="6" class="g-b"/>'
    for ac in range(0, 360, 45):
        c, s_ = math.cos(math.radians(ac)), math.sin(math.radians(ac))
        ic += (f'<line x1="{cx[3] + 29 * c:.1f}" y1="{cy + 29 * s_:.1f}" x2="{cx[3] + 34 * c:.1f}" y2="{cy + 34 * s_:.1f}" '
               f'class="g-ts" stroke-width="2" stroke-linecap="round"/>')
    # adımlar arası oklar
    for k in range(3):
        ic += _ok(cx[k] + 42, cy, cx[k + 1] - 42, cy, 'g-c', 'f73a', 2.4)
    # başlıklar ve alt yazılar
    basliklar = [('Bulutsu', 'g-mf', 'gaz ve toz', 'bulutu'), ('Çökme', 'g-mf', 'kütle çekimiyle', 'çöker, ısınır'),
                 ('Ön yıldız', 'g-tf', 'donuk kırmızı', 'yapı'), ('Yıldız', 'g-tf', 'çekirdek', 'tepkimeleri')]
    for k, (b, f, s1, s2) in enumerate(basliklar):
        ic += f'<text x="{cx[k]}" y="146" text-anchor="middle" font-size="14" font-weight="800" class="{f}">{b}</text>'
        ic += f'<text x="{cx[k]}" y="163" text-anchor="middle" font-size="12" class="g-s">{s1}</text>'
        ic += f'<text x="{cx[k]}" y="178" text-anchor="middle" font-size="12" class="g-s">{s2}</text>'
    return svg(460, 188, ic, 'Bir yıldızın doğum yolu dört adımda: 1 bulutsu (gaz ve toz bulutu), 2 çökme (kütle çekimiyle çöker ve ısınır), '
               '3 ön yıldız (donuk kırmızı yapı), 4 yıldız (merkezde çekirdek tepkimeleri başlar). Boyutlar ölçekli değildir.')


# ---------- 2) Küçük ve büyük kütleli yıldızların yaşam yolu ----------
def yasam_yolu():
    ic = '<defs>' + ok_isareti('f73c', 'g-mf') + ok_isareti('f73d', 'g-yf') + ok_isareti('f73e', 'g-tf') + '</defs>'
    # bulutsu (başlangıç)
    ic += _kutu(185, 4, 90, 26, 'Bulutsu', 'g-mf', 'g-ms', 'g-b')
    # iki kütle grubu başlıkları (sütun merkezleri 111 ve 349)
    for x, f, ad, alt2 in ((2, 'g-yf', 'Küçük kütleli yıldız', '8 Güneş kütlesinden az'),
                           (240, 'g-tf', 'Büyük kütleli yıldız', '8 Güneş kütlesinden fazla')):
        ic += f'<rect x="{x}" y="48" width="218" height="54" rx="10" class="{f}"/>'
        ic += f'<text x="{x + 109}" y="66" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{ad}</text>'
        ic += f'<text x="{x + 109}" y="81" text-anchor="middle" font-size="11" class="g-b">başlangıç kütlesi yaklaşık</text>'
        ic += f'<text x="{x + 109}" y="94.5" text-anchor="middle" font-size="11" class="g-b">{alt2}</text>'
    ic += _ok(210, 31, 111, 46, 'g-ms', 'f73c', 2.2) + _ok(250, 31, 349, 46, 'g-ms', 'f73c', 2.2)
    # küçük kütleli yol (yeşil)
    for y, ad in ((120, 'Kırmızı dev'), (168, 'Gezegenimsi bulutsu'), (216, 'Beyaz cüce')):
        ic += _kutu(26, y, 170, 30, ad, 'g-ya', 'g-ys', 'g-yf')
    for y1, y2 in ((104, 118), (152, 166), (200, 214)):
        ic += _ok(111, y1, 111, y2, 'g-ys', 'f73d', 2.2)
    # büyük kütleli yol (turuncu)
    for y, ad in ((120, 'Kırmızı süperdev'), (168, 'Süpernova')):
        ic += _kutu(264, y, 170, 30, ad, 'g-ta', 'g-ts', 'g-tf')
    for y1, y2 in ((104, 118), (152, 166)):
        ic += _ok(349, y1, 349, y2, 'g-ts', 'f73e', 2.2)
    ic += _ok(349, 201, 292, 228, 'g-ts', 'f73e', 2.2) + _ok(349, 201, 404, 228, 'g-ts', 'f73e', 2.2)
    ic += '<text x="349" y="222" text-anchor="middle" font-size="11" class="g-s">ya da</text>'
    ic += _kutu(240, 230, 104, 30, 'Nötron yıldızı', 'g-ta', 'g-ts', 'g-tf', 11.5, False)
    ic += _kutu(352, 230, 104, 30, 'Kara delik', 'g-ta', 'g-ts', 'g-tf', 11.5, False)
    return svg(460, 266, ic, 'Yıldızların yaşam yolu. Bulutsuda doğan yıldız başlangıç kütlesine göre ayrılır. Küçük kütleli yıldız (yaklaşık 8 Güneş '
               'kütlesinden az): kırmızı dev, gezegenimsi bulutsu, beyaz cüce. Büyük kütleli yıldız (yaklaşık 8 Güneş kütlesinden fazla): kırmızı süperdev, '
               'süpernova, ardından nötron yıldızı ya da kara delik.')


# ---------- 3) Yaş tahmininde üç yöntem ----------
def yas_tahmini():
    ic = '<defs>' + ok_isareti('f73f', 'g-s') + ok_isareti('f73g', 'g-yf') + ok_isareti('f73h', 'g-tf') + '</defs>'
    x0 = (4, 156, 308)
    baslik = (('Parlaklık ve', 'sıcaklık grafiği'), ('Dönme', 'hızı'), ('Parlaklık', 'değişimi'))
    for k in range(3):
        ic += f'<rect x="{x0[k]}" y="4" width="148" height="40" rx="10" class="g-ma"/><rect x="{x0[k]}" y="4" width="148" height="40" rx="10" class="g-ms" stroke-width="2"/>'
        ic += f'<text x="{x0[k] + 74}" y="21" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">{baslik[k][0]}</text>'
        ic += f'<text x="{x0[k] + 74}" y="36" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">{baslik[k][1]}</text>'
    # A) parlaklık-sıcaklık grafiği
    a = x0[0]
    ic += f'<line x1="{a + 22}" y1="176" x2="{a + 22}" y2="70" class="g-c" stroke-width="2" marker-end="url(#f73f)"/>'
    ic += f'<line x1="{a + 22}" y1="176" x2="{a + 138}" y2="176" class="g-c" stroke-width="2" marker-end="url(#f73f)"/>'
    ic += f'<text x="{a + 26}" y="62" font-size="11.5" class="g-s">Parlaklık</text>'
    ic += f'<text x="{a + 140}" y="194" text-anchor="end" font-size="11.5" class="g-s">Sıcaklık</text>'
    for dx, dy in ((0, 0), (14, 8), (28, -2), (40, 10), (8, 20), (30, 22)):
        ic += f'<circle cx="{a + 44 + dx}" cy="{88 + dy}" r="4.5" class="g-yf"/>'
        ic += f'<circle cx="{a + 44 + dx}" cy="{136 + dy}" r="4.5" class="g-tf"/>'
    ic += f'<text x="{a + 104}" y="106" font-size="12.5" font-weight="800" class="g-yf">genç</text>'
    ic += f'<text x="{a + 104}" y="154" font-size="12.5" font-weight="800" class="g-tf">yaşlı</text>'
    # B) dönme hızı
    b = x0[1]
    ic += f'<circle cx="{b + 34}" cy="96" r="14" class="g-yf"/>'
    ic += _yay_ok(b + 34, 96, 25, -50, 215, 'g-ys', 'f73g', 2.4)
    ic += f'<text x="{b + 68}" y="94" font-size="12.5" font-weight="800" class="g-yf">genç</text>'
    ic += f'<text x="{b + 68}" y="110" font-size="11.5" class="g-s">hızlı döner</text>'
    ic += f'<circle cx="{b + 34}" cy="160" r="14" class="g-tf"/>'
    ic += _yay_ok(b + 34, 160, 25, -50, 15, 'g-ts', 'f73h', 2)
    ic += f'<text x="{b + 68}" y="158" font-size="12.5" font-weight="800" class="g-tf">yaşlı</text>'
    ic += f'<text x="{b + 68}" y="174" font-size="11.5" class="g-s">yavaş döner</text>'
    # C) parlaklık değişimi
    c = x0[2]
    ic += f'<line x1="{c + 22}" y1="176" x2="{c + 22}" y2="70" class="g-c" stroke-width="2" marker-end="url(#f73f)"/>'
    ic += f'<line x1="{c + 22}" y1="176" x2="{c + 138}" y2="176" class="g-c" stroke-width="2" marker-end="url(#f73f)"/>'
    ic += f'<text x="{c + 26}" y="62" font-size="11.5" class="g-s">Parlaklık</text>'
    ic += f'<text x="{c + 140}" y="194" text-anchor="end" font-size="11.5" class="g-s">Zaman</text>'
    pts = []
    for i in range(0, 41):
        x = c + 28 + i * 2.7
        y = 124 - 24 * math.sin(i / 40 * 2.5 * 2 * math.pi)
        pts.append(f'{x:.1f},{y:.1f}')
    ic += f'<polyline points="{" ".join(pts)}" class="g-ms" stroke-width="2.6" stroke-linejoin="round"/>'
    ic += f'<text x="{c + 76}" y="86" text-anchor="middle" font-size="11.5" class="g-s">titreşimler</text>'
    ic += f'<text x="{c + 82}" y="166" text-anchor="middle" font-size="11.5" font-weight="700" class="g-mf">iç yapı ve yaş</text>'
    return svg(460, 202, ic, 'Yıldızın yaşını tahmin etmenin üç yolu. Parlaklık ve sıcaklık grafiğinde genç yıldızlar üst bölgede, yaşlı yıldızlar alt bölgede yer alır. '
               'Dönme hızında genç yıldız hızlı, yaşlı yıldız daha yavaş döner. Parlaklık değişiminde titreşimler nedeniyle değişen parlaklık incelenerek '
               'iç yapı ve yaş tahmin edilir.')


def uygula(o):
    g = {'Bulutsudan yıldıza': bulutsudan_yildiza(),
         'Büyük kütleli yıldızların yaşamı': yasam_yolu(),
         'Yıldızların yaşını nasıl tahmin ederiz?': yas_tahmini()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
