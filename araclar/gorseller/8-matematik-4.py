"""8. sınıf Matematik, 4. hafta: sayıların ondalık gösterimini 10'un tam sayı kuvvetleriyle çözümleme (basamak değerleri, 10'un kuvvetiyle
çarpınca virgülün kayması, aynı sayıyı 10'un farklı kuvvetleriyle yazma).

Görseller yalnız MEB 8. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 45-46).
Renk anlamı: yeşil = üssü sıfır (birler basamağı), turuncu = üssü negatif (virgülün sağı) ve sola kayma, mavi = üssü pozitif ve sağa kayma.
Görseldeki her sayı ve her adım metindeki örneklerle aynıdır.
"""
from ozet_gorsel import svg, ok_isareti, kesir_svg

_US = 0.72    # üs yazısının oranı
_GENIS = {' ': 0.30, ' ': 0.30, ',': 0.30, '.': 0.30, '·': 0.34, '(': 0.36, ')': 0.36, '’': 0.26, '=': 0.60, '+': 0.60,
          '−': 0.60, '1': 0.50, 'l': 0.30, 'i': 0.30, 't': 0.36}


def _cw(ch):
    return _GENIS.get(ch, 0.58)


def _mw(metin, boy):
    return sum(_cw(c) for c in metin) * boy


def _w(p, boy):
    t = p[0]
    if t == 'm':
        return _mw(p[1], boy)
    if t == 'u':
        return _mw(p[1], boy) + _mw(p[2], boy * _US) + 1
    if t == 's':
        return _mw(p[1], boy * _US) + 1
    if t == 'k':
        return max(_wl(p[1], boy), _wl(p[2], boy)) + 8
    if t == 'kp':
        return max(_wl(p[1], boy), _wl(p[2], boy)) + 8 + 18 + _mw(p[3], boy * _US) + 1
    raise ValueError(t)


def _wl(ps, boy):
    return sum(_w(p, boy) for p in ps)


def _ciz(x, y, ps, boy, sinif, kalin=700):
    """Soldan sağa dizer. (x, y): ilk parçanın sol kenarı ve matematik ekseni (kesir çizgisinin yüksekliği)."""
    yb = y + boy * 0.35
    ic = ''
    cx = x
    for p in ps:
        t = p[0]
        if t == 'm':
            m = p[1].replace(' ', ' ')
            ic += f'<text x="{cx:.1f}" y="{yb:.1f}" font-size="{boy:g}" font-weight="{kalin}" class="{sinif}">{m}</text>'
        elif t == 'u':
            ic += f'<text x="{cx:.1f}" y="{yb:.1f}" font-size="{boy:g}" font-weight="{kalin}" class="{sinif}">{p[1]}</text>'
            ic += (f'<text x="{cx + _mw(p[1], boy) + 1:.1f}" y="{yb - boy * 0.46:.1f}" font-size="{boy * _US:.1f}" '
                   f'font-weight="{kalin}" class="{sinif}">{p[2]}</text>')
        elif t == 's':
            yuk = p[2] if len(p) > 2 else 0.46
            ic += (f'<text x="{cx + 0.5:.1f}" y="{yb - boy * yuk:.1f}" font-size="{boy * _US:.1f}" '
                   f'font-weight="{kalin}" class="{sinif}">{p[1]}</text>')
        elif t == 'k':
            wk = max(_wl(p[1], boy), _wl(p[2], boy)) + 8
            wp, wd = _wl(p[1], boy), _wl(p[2], boy)
            ic += _ciz(cx + (wk - wp) / 2, y - 4 - boy * 0.35, p[1], boy, sinif, kalin)
            cs = sinif[:-1] + 's' if sinif.endswith('f') else 'g-c'
            ic += f'<line x1="{cx + 1:.1f}" y1="{y:.1f}" x2="{cx + wk - 1:.1f}" y2="{y:.1f}" class="{cs}" stroke-width="1.6"/>'
            ic += _ciz(cx + (wk - wd) / 2, y + boy + 3 - boy * 0.35, p[2], boy, sinif, kalin)
        elif t == 'kp':
            wk = max(_wl(p[1], boy), _wl(p[2], boy)) + 8
            cs = sinif[:-1] + 's' if sinif.endswith('f') else 'g-c'
            ic += f'<path d="M{cx + 5:.1f} {y - 19:.1f} Q{cx - 1:.1f} {y:.1f} {cx + 5:.1f} {y + 19:.1f}" class="{cs}" stroke-width="1.6" stroke-linecap="round"/>'
            ic += _ciz(cx + 8, y, [('k', p[1], p[2])], boy, sinif, kalin)
            xr = cx + 8 + wk + 3
            ic += f'<path d="M{xr:.1f} {y - 19:.1f} Q{xr + 6:.1f} {y:.1f} {xr:.1f} {y + 19:.1f}" class="{cs}" stroke-width="1.6" stroke-linecap="round"/>'
            ic += (f'<text x="{xr + 9:.1f}" y="{y - 13:.1f}" font-size="{boy * _US:.1f}" font-weight="{kalin}" class="{sinif}">{p[3]}</text>')
        cx += _w(p, boy)
    return ic


def _ort(xc, y, ps, boy, sinif, kalin=700):
    return _ciz(xc - _wl(ps, boy) / 2, y, ps, boy, sinif, kalin)


def _sol(x, y, ps, boy, sinif, kalin=700):
    return _ciz(x, y, ps, boy, sinif, kalin)


def _kutu(x, y, w, h, dolgu, cizgi, rx=10, kalin=2):
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{dolgu}"/>'
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{cizgi}" stroke-width="{kalin}"/>')


def _hap(x, y, w, h, metin, sinif, boy=12.5):
    """Başlık hapı: yüzey dolgusu + renkli çizgi + renkli yazı."""
    c = sinif.replace('f', 's')
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{h / 2:g}" class="g-z"/>'
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{h / 2:g}" class="{c}" stroke-width="1.8"/>'
            f'<text x="{x + w / 2:g}" y="{y + h / 2 + boy * 0.36:.1f}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{sinif}">{metin}</text>')


def _yazi(x, y, metin, boy, sinif, anchor='start', kalin=700):
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boy:g}" font-weight="{kalin}" class="{sinif}">{metin}</text>'


MAVI = ('g-mf', 'g-ma', 'g-ms')
TURUNCU = ('g-tf', 'g-ta', 'g-ts')
YESIL = ('g-yf', 'g-ya', 'g-ys')
MOR = ('g-of', 'g-oa', 'g-os')


def basamak_tablosu():
    """4,358: rakam, basamak adı, basamak değeri ve 10'un kuvveti (birler yeşil, virgülün sağı turuncu)."""
    u = lambda t, e: ('u', t, e)
    m = lambda t: ('m', t)
    ic = ''
    sutunlar = [(100, YESIL, '4', 'Birler', None, ('1', None), u('10', '0')),
                (194, TURUNCU, '3', 'Onda birler', None, ('1', '10'), u('10', '−1')),
                (270, TURUNCU, '5', 'Yüzde birler', None, ('1', '100'), u('10', '−2')),
                (346, TURUNCU, '8', 'Binde birler', None, ('1', '1000'), u('10', '−3'))]
    gen = 72
    satir_y = {'rakam': 40, 'ad': 92, 'deger': 142, 'kuvvet': 190}
    etiket = [('rakam', ['Rakam']), ('ad', ['Basamak']), ('deger', ['Basamak', 'değeri']), ('kuvvet', ['10’un', 'kuvveti'])]
    for x0, (f, a, s), rakam, ad, _, deger, kuvvet in sutunlar:
        xc = x0 + gen / 2
        ic += _kutu(x0, 8, gen, 206, a, s, 14, 1.8)
        ic += _kutu(xc - 21, 20, 42, 42, 'g-z', s, 10, 1.8)
        ic += _yazi(xc, 49, rakam, 24, f, 'middle', 800)
        sozler = ad.split(' ')
        if len(sozler) == 2:
            ic += _yazi(xc, 88, sozler[0], 11.5, f, 'middle', 700)
            ic += _yazi(xc, 103, sozler[1], 11.5, f, 'middle', 700)
        else:
            ic += _yazi(xc, 96, ad, 11.5, f, 'middle', 700)
        if deger[1] is None:
            ic += _ort(xc, satir_y['deger'], [m('1')], 17, f)
        else:
            ic += _ort(xc, satir_y['deger'], [('k', [m(deger[0])], [m(deger[1])])], 15, f)
        ic += _ort(xc, satir_y['kuvvet'], [kuvvet], 18, f, 800)
    ic += _yazi(182, 52, ',', 30, 'g-y', 'middle', 800)
    for anahtar, satirlar in etiket:
        y = {'rakam': 44, 'ad': 98, 'deger': 142, 'kuvvet': 190}[anahtar]
        for j, t in enumerate(satirlar):
            ic += _yazi(8, y + j * 14 - (7 if len(satirlar) == 2 else 0) + 3, t, 11.5, 'g-s', 'start', 700)
    ic += _ort(220, 244, [m('4,358 = 4 ·  '), u('10', '0'), m(' + 3 · '), u('10', '−1'), m(' + 5 · '), u('10', '−2'), m(' + 8 · '), u('10', '−3')], 15, 'g-y')
    ic += _kutu(14, 266, 14, 14, YESIL[1], YESIL[2], 4, 1.6)
    ic += _yazi(35, 278, 'üssü sıfır', 12.5, 'g-y', 'start', 600)
    ic += _kutu(150, 266, 14, 14, TURUNCU[1], TURUNCU[2], 4, 1.6)
    ic += _yazi(171, 278, 'üssü negatif', 12.5, 'g-y', 'start', 600)
    return svg(440, 292, ic, '4,358 sayısının çözümlenmesi: birler basamağındaki 4 rakamının basamak değeri 1 ve 10’un kuvveti 10 üssü 0; '
               'onda birler basamağındaki 3 için 1 bölü 10 ve 10 üssü eksi 1; yüzde birler basamağındaki 5 için 1 bölü 100 ve 10 üssü eksi 2; '
               'binde birler basamağındaki 8 için 1 bölü 1000 ve 10 üssü eksi 3. Sonuç: 4,358 eşittir 4 çarpı 10 üssü 0 artı 3 çarpı 10 üssü eksi 1 '
               'artı 5 çarpı 10 üssü eksi 2 artı 8 çarpı 10 üssü eksi 3.')


def virgul_kaydirma():
    """Dört işlem: 36,52·10¹ = 0,3652·10³ = 365,2 (sağa) ve 2764,3·10⁻¹ = 2,7643·10² = 276,43 (sola / sağa)."""
    u = lambda t, e: ('u', t, e)
    m = lambda t: ('m', t)
    ic = ''
    kartlar = (
        (8, '365,2', [([m('36,52 · '), u('10', '1')], 'virgül 1 basamak sağa', MAVI),
                      ([m('0,3652 · '), u('10', '3')], 'virgül 3 basamak sağa', MAVI)]),
        (126, '276,43', [([m('2764,3 · '), u('10', '−1')], 'virgül 1 basamak sola', TURUNCU),
                         ([m('2,7643 · '), u('10', '2')], 'virgül 2 basamak sağa', MAVI)]),
    )
    for y0, sonuc, satirlar in kartlar:
        ic += _kutu(8, y0, 424, 108, 'g-z', 'g-c', 14, 1.8)
        for i, (ps, yon, (f, a, s)) in enumerate(satirlar):
            y = y0 + 30 + i * 46
            ic += _sol(24, y, ps, 17, 'g-y', 700)
            ic += _hap(152, y - 14, 150, 28, yon, f, 11)
        ic += f'<path d="M318 {y0 + 20}q10 0 10 10v{18}q0 10 10 10q-10 0 -10 10v{18}q0 10 -10 10" class="g-c" stroke-width="2" stroke-linecap="round"/>'
        ic += _sol(348, y0 + 59, [m('= ' + sonuc)], 17, 'g-y', 800)
    return svg(440, 242, ic, 'Üssü pozitif olan 10 kuvvetiyle çarpmak virgülü sağa, negatif olan kuvvetle çarpmak sola kaydırır. '
               '36,52 çarpı 10 üssü 1 işleminde virgül 1 basamak sağa gider; 0,3652 çarpı 10 üssü 3 işleminde virgül 3 basamak sağa gider; ikisi de 365,2 eder. '
               '2764,3 çarpı 10 üssü eksi 1 işleminde virgül 1 basamak sola gider; 2,7643 çarpı 10 üssü 2 işleminde virgül 2 basamak sağa gider; ikisi de 276,43 eder.')


def merdiven():
    """365,2 sayısının 10'un beş farklı kuvvetiyle yazılışı: üs 1 azalırken katsayıdaki virgül 1 basamak sağa kayar."""
    u = lambda t, e: ('u', t, e)
    m = lambda t: ('m', t)
    ic = '<defs>' + ok_isareti('okM1', 'g-s') + '</defs>'
    satirlar = [('3', '0,3652', MAVI), ('2', '3,652', MAVI), ('1', '36,52', MAVI), ('0', '365,2', YESIL), ('−1', '3652', TURUNCU)]
    for i, (n, a, (f, fa, fs)) in enumerate(satirlar):
        y = 28 + i * 54
        ic += _hap(10, y - 14, 58, 28, 'n = ' + n, f, 12.5)
        ic += _kutu(82, y - 17, 196, 34, fa, fs, 10, 1.8)
        ic += _ort(180, y, [m(a + ' · '), u('10', n)], 17, 'g-y', 700)
        ic += _yazi(294, y + 6, '= 365,2', 17, 'g-y', 'start', 800)
        if i < 4:
            ic += f'<line x1="180" y1="{y + 19}" x2="180" y2="{y + 35}" class="g-c" stroke-width="1.8" marker-end="url(#okM1)"/>'
            ic += _yazi(194, y + 31, 'virgül sağa, üs 1 azalır', 12, 'g-s', 'start', 600)
    return svg(440, 272, ic, '365,2 sayısının 10’un farklı kuvvetleriyle yazılışları: 0,3652 çarpı 10 üssü 3, 3,652 çarpı 10 üssü 2, 36,52 çarpı 10 üssü 1, '
               '365,2 çarpı 10 üssü 0 ve 3652 çarpı 10 üssü eksi 1. Hepsi 365,2’ye eşittir. Üs 1 azaldıkça katsayıdaki virgül 1 basamak sağa kayar.')


def uygula(o):
    g = {'Basamak değerlerini 10’un kuvvetleriyle yazmak': basamak_tablosu(),
         'Bir sayıyı 10’un kuvvetiyle çarpmak virgülü kaydırır': virgul_kaydirma(),
         'Aynı sayıyı 10’un farklı kuvvetleriyle yazmak': merdiven()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
