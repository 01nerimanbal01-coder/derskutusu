"""8. sınıf Matematik, 6. hafta: tam kare sayılar, karekök, alan–kenar ilişkisi, karekökün iki doğal sayı arasındaki yeri.

Renk anlamı: turuncu = alan (tam kare sayı), mavi = kenar uzunluğu / karekök değeri, mor = tam kare olmayan sayı ve karekökü.
Kök işareti düz karakterle değil yola çizilir; üst çizgi kök içindeki sayının tamamını kapsar.
K057: ölçülü görsellerde tek ölçek kullanılır (V1: 15 px/birim, V2: 8 px/cm, V3: 20 px/birim, V4: 320 px/birim).
Görseldeki her sayı metindeki örneklerle aynıdır.
"""
from ozet_gorsel import svg, ok_isareti

_US = 0.72    # üs yazısının oranı
_GEN = {' ': 0.30, ' ': 0.30, ',': 0.30, '.': 0.30, '·': 0.34, '(': 0.36, ')': 0.36, '’': 0.26, '=': 0.60, '>': 0.60,
        '<': 0.60, '+': 0.60, '−': 0.60, ';': 0.32, ':': 0.32, '1': 0.50, 'l': 0.30, 'i': 0.30, 't': 0.36, 'ı': 0.30}

MAVI = ('g-mf', 'g-ma', 'g-ms')
TURUNCU = ('g-tf', 'g-ta', 'g-ts')
MOR = ('g-of', 'g-oa', 'g-os')
NB = ' '

# ölçekler (K057)
OL1 = 15      # V1: px / birim
OL2 = 8       # V2: px / cm
OL3 = 20      # V3: px / birim
OL4 = 320     # V4: px / birim (sayı doğrusu)


def _cw(ch):
    if ch in '023456789':
        return 0.62        # kalın rakamlar: güvenli (geniş) tahmin
    return _GEN.get(ch, 0.58)


def _mw(metin, boy):
    metin = metin.replace('&lt;', '<').replace('&gt;', '>')      # XML kaçışı tek karakter sayılır
    return sum(_cw(c) for c in metin) * boy


def _kw(ic, boy):
    """Kök işareti + üst çizgi + içerik genişliği."""
    return boy * 0.62 + boy * 0.10 + _mw(ic, boy) + boy * 0.12


def _pw(p, boy):
    if p[0] == 'm':
        return _mw(p[1], boy)
    if p[0] == 'u':
        return _mw(p[1], boy) + _mw(p[2], boy * _US) + 1      # ('u', taban, üs, sınıf)
    return _kw(p[1], boy)                                      # ('k', içerik, işaret çizgi sınıfı, içerik dolgu sınıfı)


def _dw(ps, boy):
    return sum(_pw(p, boy) for p in ps)


def _kok_ciz(x, y, ic, boy, isaret, dolgu, kalin=700):
    """Karekök: kök işareti yolu + ifadenin TAMAMINI kapsayan üst çizgi; (x, y) işaretin sol kenarı ve yazı tabanı."""
    yt = y - boy * 0.95
    x_ic = x + boy * 0.62 + boy * 0.10
    x_son = x_ic + _mw(ic, boy) + boy * 0.12
    nokta = [(x, y - boy * 0.32), (x + boy * 0.12, y - boy * 0.40), (x + boy * 0.33, y + boy * 0.12), (x + boy * 0.62, yt)]
    d = 'M' + ' L'.join(f'{px:.1f} {py:.1f}' for px, py in nokta) + f' H{x_son:.1f}'
    sw = max(1.4, boy * 0.1)
    return (f'<path d="{d}" class="{isaret}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<text x="{x_ic:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" class="{dolgu}">{ic}</text>')


def _dizi(x, y, ps, boy, kalin=700):
    """Soldan sağa dizer; (x, y) ilk parçanın sol kenarı ve yazı tabanı. Parça: ('m', metin, sınıf) | ('u', taban, üs, sınıf) | ('k', içerik, işaret, dolgu)."""
    ic = ''
    cx = x
    for p in ps:
        if p[0] == 'm':
            ic += f'<text x="{cx:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" class="{p[2]}">{p[1]}</text>'
        elif p[0] == 'u':
            ic += f'<text x="{cx:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" class="{p[3]}">{p[1]}</text>'
            ic += (f'<text x="{cx + _mw(p[1], boy) + 1:.1f}" y="{y - boy * 0.46:.1f}" font-size="{boy * _US:.1f}" '
                   f'font-weight="{kalin}" class="{p[3]}">{p[2]}</text>')
        else:
            ic += _kok_ciz(cx, y, p[1], boy, p[2], p[3], kalin)
        cx += _pw(p, boy)
    return ic


def _ort(xc, y, ps, boy, kalin=700):
    return _dizi(xc - _dw(ps, boy) / 2, y, ps, boy, kalin)


def _kutu(x, y, w, h, dolgu, cizgi, rx=10, kalin=1.8):
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{dolgu}"/>'
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{cizgi}" stroke-width="{kalin}"/>')


def _hap(xc, y, w, h, metin, sinif, boy=12.5):
    """Ortalanmış başlık hapı: yüzey dolgusu + renkli çizgi + renkli yazı."""
    c = sinif.replace('f', 's')
    return (f'<rect x="{xc - w / 2:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{h / 2:g}" class="g-z"/>'
            f'<rect x="{xc - w / 2:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{h / 2:g}" class="{c}" stroke-width="1.8"/>'
            f'<text x="{xc:g}" y="{y + h / 2 + boy * 0.36:.1f}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{sinif}">{metin}</text>')


def _yazi(x, y, metin, boy, sinif, anchor='start', kalin=700):
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boy:g}" font-weight="{kalin}" class="{sinif}">{metin}</text>'


def _sozluk_kare(x, y, renk, metin):
    f, a, s = renk
    return (f'<rect x="{x:g}" y="{y:g}" width="14" height="14" rx="4" class="{a}"/><rect x="{x:g}" y="{y:g}" width="14" height="14" rx="4" class="{s}" stroke-width="1.6"/>'
            + _yazi(x + 21, y + 11.5, metin, 12.5, 'g-y', 'start', 600))


# ---------------------------------------------------------------------------------------------------------------------
def kare_modelleri():
    """Kenarı 1..5 birim olan kareler: alan = kenar · kenar (tek ölçek: 15 px / birim)."""
    cw, gap = 66, 10
    x0 = (440 - (5 * cw + 4 * gap)) / 2
    yb = 120
    ic = ''
    ic += _ort(220, 26, [('m', 'alan', 'g-tf'), ('m', NB + '=' + NB, 'g-y'), ('m', 'kenar', 'g-mf'), ('m', NB + '·' + NB, 'g-y'), ('m', 'kenar', 'g-mf')], 15, 800)
    for n in range(1, 6):
        xs = x0 + (n - 1) * (cw + gap)
        yan = n * OL1
        xk = xs + (cw - yan) / 2
        yk = yb - yan
        ic += _kutu(xk, yk, yan, yan, TURUNCU[1], TURUNCU[2], 2, 1.8)
        for k in range(1, n):          # birim kare çizgileri
            ic += f'<line x1="{xk + k * OL1:.1f}" y1="{yk:.1f}" x2="{xk + k * OL1:.1f}" y2="{yb:.1f}" class="g-ts" stroke-width="0.9" stroke-opacity="0.55"/>'
            ic += f'<line x1="{xk:.1f}" y1="{yk + k * OL1:.1f}" x2="{xk + yan:.1f}" y2="{yk + k * OL1:.1f}" class="g-ts" stroke-width="0.9" stroke-opacity="0.55"/>'
        xc = xs + cw / 2
        ic += _yazi(xc, yb + 20, f'{n} birim', 12.5, 'g-mf', 'middle', 700)
        ic += _ort(xc, yb + 38, [('m', str(n), 'g-mf'), ('m', NB + '·' + NB, 'g-y'), ('m', str(n), 'g-mf'), ('m', NB + '=' + NB, 'g-y'), ('m', str(n * n), 'g-tf')], 13, 700)
    ic += _sozluk_kare(60, 176, TURUNCU, 'alan (tam kare sayı)')
    ic += _sozluk_kare(250, 176, MAVI, 'kenar uzunluğu')
    return svg(440, 202, ic, 'Kenarı 1, 2, 3, 4 ve 5 birim olan beş kare aynı ölçekte çizilmiştir. Alanları kenar çarpı kenar ile bulunur: 1 çarpı 1 eşittir 1, '
               '2 çarpı 2 eşittir 4, 3 çarpı 3 eşittir 9, 4 çarpı 4 eşittir 16, 5 çarpı 5 eşittir 25. Bu alan sayıları tam kare sayılardır.')


def alan_kenar():
    """Alanı 49, 100 ve 169 cm² olan üç kare, kenarları karekökle (tek ölçek: 8 px / cm)."""
    veri = [(49, 7), (100, 10), (169, 13)]
    cw, gap = 110, 14
    x0 = (440 - (3 * cw + 2 * gap)) / 2
    yb = 148
    ic = ''
    for i, (alan, kenar) in enumerate(veri):
        xs = x0 + i * (cw + gap)
        xc = xs + cw / 2
        yan = kenar * OL2
        xk, yk = xc - yan / 2, yb - yan
        ic += _kutu(xk, yk, yan, yan, TURUNCU[1], TURUNCU[2], 3, 2)
        # üs yazısı aynı <text> içinde akar: "cm" harflerinin genişliği tahmin edilmez, ² harfe değmez
        ic += (f'<text x="{xc:.1f}" y="{yk + yan / 2 + 5:.1f}" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">'
               f'{alan}{NB}cm<tspan dx="1" dy="-6" font-size="9.4">2</tspan></text>')
        # kenar uzunluğu işareti (üstte)
        yd = yk - 9
        ic += f'<path d="M{xk:.1f} {yd + 4:.1f}V{yd - 4:.1f}M{xk + yan:.1f} {yd + 4:.1f}V{yd - 4:.1f}M{xk:.1f} {yd:.1f}H{xk + yan:.1f}" class="g-ms" stroke-width="1.6" stroke-linecap="round"/>'
        ic += _yazi(xc, yd - 8, f'{kenar} cm', 13, 'g-mf', 'middle', 800)
        # karekök denklemi
        ic += _ort(xc, yb + 26, [('k', str(alan), 'g-ms', 'g-tf'), ('m', NB + '=' + NB + str(kenar) + NB + 'cm', 'g-mf')], 15, 800)
    ic += _sozluk_kare(60, 184, TURUNCU, 'alan')
    ic += _sozluk_kare(200, 184, MAVI, 'kenar = alanın karekökü')
    return svg(440, 210, ic, 'Alanları 49, 100 ve 169 santimetrekare olan üç kare aynı ölçekte çizilmiştir. Kenar uzunlukları alanın karekökü ile bulunur: '
               '49 sayısının karekökü 7 santimetre, 100 sayısının karekökü 10 santimetre, 169 sayısının karekökü 13 santimetredir.')


def iki_dogal_sayi_arasi():
    """Alanları 36, 40 ve 49 birimkare olan kareler yan yana (tek ölçek: 20 px / birim): 6 < karekök 40 < 7."""
    import math
    veri = [(36, 6.0, TURUNCU, 'g-tf', 'g-ts'), (40, math.sqrt(40), MOR, 'g-of', 'g-os'), (49, 7.0, TURUNCU, 'g-tf', 'g-ts')]
    gap = 10
    toplam = sum(v[1] * OL3 for v in veri) + 2 * gap
    x = (440 - toplam) / 2
    yb = 150
    ic = ''
    for alan, kenar, (f, a, s), yaz, _ in veri:
        yan = kenar * OL3
        yk = yb - yan
        ic += _kutu(round(x, 1), round(yk, 1), round(yan, 1), round(yan, 1), a, s, 3, 2)
        xc = x + yan / 2
        ic += _yazi(xc, yk + yan / 2 + 5, f'{alan} birimkare', 12.5, yaz, 'middle', 800)
        if alan == 40:
            ic += _ort(xc, yb + 26, [('k', '40', 'g-os', 'g-of'), ('m', NB + 'birim', 'g-of')], 15, 800)
        else:
            ic += _ort(xc, yb + 26, [('k', str(alan), 'g-ms', 'g-tf'), ('m', NB + '=' + NB + str(int(kenar)) + NB + 'birim', 'g-mf')], 15, 800)
        x += yan + gap
    ic += _kutu(150, 184, 140, 32, 'g-z', 'g-os', 16, 1.8)
    ic += _ort(220, 206, [('m', '6' + NB + '&lt;' + NB, 'g-mf'), ('k', '40', 'g-os', 'g-of'), ('m', NB + '&lt;' + NB + '7', 'g-mf')], 16, 800)
    ic += _sozluk_kare(60, 228, TURUNCU, 'tam kare alan')
    ic += _sozluk_kare(220, 228, MOR, 'tam kare olmayan alan')
    return svg(440, 252, ic, 'Alanları 36, 40 ve 49 birimkare olan üç kare aynı ölçekte yan yana çizilmiştir. 36 sayısının karekökü 6, 49 sayısının karekökü 7 birimdir; '
               '40 birimkare alanlı karenin kenarı 40 sayısının karekökü olup 6 ile 7 arasındadır. Sonuç: 6 küçüktür 40 sayısının karekökü küçüktür 7.')


def sayi_dogrusu():
    """5 ile 6 arasında 27 ve 33'ün karekökleri (tek ölçek: 320 px / birim) ve tam karelere uzaklıklar."""
    import math
    x5, x6, yl = 60, 380, 64
    ic = f'<line x1="{x5 - 24}" y1="{yl}" x2="{x6 + 24}" y2="{yl}" class="g-c" stroke-width="2.4" stroke-linecap="round"/>'
    for xt, deger, sayi in ((x5, '5', '25'), (x6, '6', '36')):
        ic += f'<line x1="{xt}" y1="{yl - 8}" x2="{xt}" y2="{yl + 8}" class="g-ms" stroke-width="2.6" stroke-linecap="round"/>'
        ic += _ort(xt, yl + 34, [('k', sayi, 'g-ms', 'g-tf'), ('m', NB + '=' + NB + deger, 'g-mf')], 15, 800)
    for sayi in (27, 33):
        xd = x5 + (math.sqrt(sayi) - 5) * OL4
        ic += f'<circle cx="{xd:.1f}" cy="{yl}" r="6.5" class="g-of"/>'
        ic += f'<line x1="{xd:.1f}" y1="{yl - 9}" x2="{xd:.1f}" y2="{yl - 22}" class="g-os" stroke-width="1.6" stroke-linecap="round"/>'
        ic += _ort(xd, yl - 28, [('k', str(sayi), 'g-os', 'g-of')], 16, 800)
    kartlar = [
        (8, 27, 25, 36, '2 &lt; 9, 5’e yakın'),
        (224, 33, 25, 36, '3 &lt; 8, 6’ya yakın'),
    ]
    for xk, sayi, alt, ust, sonuc in kartlar:
        ic += _kutu(xk, 114, 208, 100, 'g-z', 'g-os', 12, 1.8)
        xc = xk + 104
        ic += _ort(xc, 140, [('m', f'{sayi}{NB}−{NB}{alt}{NB}={NB}{sayi - alt}', 'g-y')], 15, 700)
        ic += _ort(xc, 162, [('m', f'{ust}{NB}−{NB}{sayi}{NB}={NB}{ust - sayi}', 'g-y')], 15, 700)
        ic += _hap(xc, 174, 138, 26, sonuc, 'g-mf', 12.5)
    return svg(440, 228, ic, '5 ile 6 arasındaki sayı doğrusunda 5 noktası 25 sayısının, 6 noktası 36 sayısının karekökünü gösterir. 27 sayısının karekökü 5’e, '
               '33 sayısının karekökü 6’ya daha yakındır. 27 eksi 25 eşittir 2 ve 36 eksi 27 eşittir 9; 33 eksi 25 eşittir 8 ve 36 eksi 33 eşittir 3.')


def uygula(o):
    g = {'Kare modeli ve tam kare sayılar': kare_modelleri(),
         'Kare modelinde alan ve kenar': alan_kenar(),
         'Karekök hangi iki doğal sayı arasındadır?': iki_dogal_sayi_arasi(),
         'Karekökün yakın olduğu doğal sayı': sayi_dogrusu()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
