"""8. sınıf Matematik, 3. hafta: tam sayıların tam sayı kuvvetleri (üssü sıfır ve negatif ifadeler, çarpma/bölme/üssün üssü kuralları,
tabanları ya da üsleri eşitleyerek denk ifadeler kurma).

Görseller yalnız MEB 8. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 33-41).
Renk anlamı: mavi = üssü pozitif (ve tabanlar aynı kuralı), yeşil = üssü sıfır, turuncu = üssü negatif (ve üsler aynı kuralı), mor = işlem türü.
Görseldeki her ifade ve her adım metindeki örneklerle aynıdır.
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


def ornuntu():
    """5 tabanlı örüntü: 5³ → 5⁻³; üs her adımda 1 azalır, değer 5'e bölünür (metindeki örüntüyle aynı)."""
    ic = '<defs>' + ok_isareti('okU1', 'g-s') + '</defs>'
    ust = ['3', '2', '1', '0', '−1', '−2', '−3']
    deg = [('125', None), ('25', None), ('5', None), ('1', None), ('1', '5'), ('1', '25'), ('1', '125')]
    renk = [MAVI] * 3 + [YESIL] + [TURUNCU] * 3
    ic += _yazi(220, 18, 'her adımda üs 1 azalır', 12.5, 'g-s', 'middle')
    ic += '<line x1="14" y1="28" x2="424" y2="28" class="g-c" stroke-width="2" marker-end="url(#okU1)"/>'
    for i in range(7):
        xc = 40 + 60 * i
        f, a, s = renk[i]
        ic += _kutu(xc - 27, 40, 54, 36, a, s, 10, 1.8)
        ic += _ort(xc, 58, [('u', '5', ust[i])], 17, f)
        ic += f'<line x1="{xc}" y1="79" x2="{xc}" y2="96" class="g-c" stroke-width="1.8" marker-end="url(#okU1)"/>'
        ic += _kutu(xc - 27, 100, 54, 46, 'g-z', s, 10, 1.8)
        pay, payda = deg[i]
        if payda is None:
            ic += _ort(xc, 123, [('m', pay)], 17, f)
        else:
            ic += _ort(xc, 123, [('k', [('m', pay)], [('m', payda)])], 15, f)
    ic += '<line x1="14" y1="162" x2="424" y2="162" class="g-c" stroke-width="2" marker-end="url(#okU1)"/>'
    ic += _yazi(220, 182, 'değer her adımda 5’e bölünür', 12.5, 'g-s', 'middle')
    for x, (f, a, s), ad in ((14, MAVI, 'üssü pozitif'), (150, YESIL, 'üssü sıfır'), (262, TURUNCU, 'üssü negatif')):
        ic += _kutu(x, 202, 14, 14, a, s, 4, 1.6)
        ic += _yazi(x + 21, 214, ad, 12.5, 'g-y', 'start', 600)
    return svg(440, 228, ic, 'Her adımda üs 1 azalır ve değer 5’e bölünür: 5 üssü 3 eşittir 125, 5 üssü 2 eşittir 25, 5 üssü 1 eşittir 5, '
               '5 üssü 0 eşittir 1, 5 üssü eksi 1 eşittir 1 bölü 5, 5 üssü eksi 2 eşittir 1 bölü 25, 5 üssü eksi 3 eşittir 1 bölü 125. '
               'Üssü pozitif olanlar mavi, üssü sıfır olan yeşil, üssü negatif olanlar turuncudur.')


def kural_matrisi():
    """Dört kural: çarpma/bölme × tabanlar aynı/üsler aynı; her hücrede kural, metindeki örnek ve işlem adı."""
    u = lambda t, e: ('u', t, e)
    m = lambda t: ('m', t)
    k = lambda p, q: ('k', p, q)
    hucre = {
        (0, 0): ([u('a', 'x'), m(' · '), u('a', 'y'), m(' = '), u('a', 'x + y')],
                 [u('6', '2'), m(' · '), u('6', '3'), m(' = '), u('6', '5')], 'üsler toplanır'),
        (0, 1): ([u('a', 'x'), m(' · '), u('b', 'x'), m(' = '), u('(a · b)', 'x')],
                 [u('4', '5'), m(' · '), u('5', '5'), m(' = '), u('20', '5')], 'tabanlar çarpılır'),
        (1, 0): ([k([u('a', 'b')], [u('a', 'c')]), m(' = '), u('a', 'b − c')],
                 [k([u('7', '6')], [u('7', '2')]), m(' = '), u('7', '4')], 'üsler çıkarılır'),
        (1, 1): ([k([u('a', 'c')], [u('b', 'c')]), m(' = '), ('kp', [m('a')], [m('b')], 'c')],
                 [k([u('20', '4')], [u('5', '4')]), m(' = '), u('4', '4')], 'tabanlar bölünür'),
    }
    ic = ''
    sx, gen, yuk = (80, 262), 174, 120
    ic += _hap(sx[0], 6, gen, 28, 'Tabanlar aynı', 'g-mf', 13.5)
    ic += _hap(sx[1], 6, gen, 28, 'Üsler aynı', 'g-tf', 13.5)
    for r, (y0, ad) in enumerate(((44, 'Çarpma'), (172, 'Bölme'))):
        ic += _kutu(8, y0, 64, yuk, MOR[1], MOR[2], 12, 2)
        ic += _yazi(40, y0 + yuk / 2 + 5, ad, 13.5, 'g-of', 'middle')
        for c in (0, 1):
            f, a, s = (MAVI, TURUNCU)[c]
            x0 = sx[c]
            kural, ornek, fiil = hucre[(r, c)]
            ic += _kutu(x0, y0, gen, yuk, a, s, 12, 1.8)
            ic += f'<path d="M{x0} {y0 + 12}a12 12 0 0 1 12 -12h{gen - 24}a12 12 0 0 1 12 12v10h-{gen}z" class="{f}"/>'
            ic += _yazi(x0 + gen / 2, y0 + 16, fiil, 12.5, 'g-b', 'middle')
            ic += _ort(x0 + gen / 2, y0 + 52, kural, 15, f)
            ic += _ort(x0 + gen / 2, y0 + 96, ornek, 14, 'g-y', 600)
    return svg(440, 300, ic, 'Dört kural. Tabanlar aynıysa: çarpmada üsler toplanır, a üssü x çarpı a üssü y eşittir a üssü x artı y, örnek 6 üssü 2 çarpı 6 üssü 3 eşittir 6 üssü 5; '
               'bölmede üsler çıkarılır, a üssü b bölü a üssü c eşittir a üssü b eksi c, örnek 7 üssü 6 bölü 7 üssü 2 eşittir 7 üssü 4. '
               'Üsler aynıysa: çarpmada tabanlar çarpılır, a üssü x çarpı b üssü x eşittir a çarpı b’nin x’inci kuvveti, örnek 4 üssü 5 çarpı 5 üssü 5 eşittir 20 üssü 5; '
               'bölmede tabanlar bölünür, a üssü c bölü b üssü c eşittir a bölü b’nin c’inci kuvveti, örnek 20 üssü 4 bölü 5 üssü 4 eşittir 4 üssü 4.')


def esitleme():
    """Farklı görünen ifadeleri eşitleme: solda tabanlar eşitlenir (25³·125²·5⁻⁴ → 5⁸), sağda üsler eşitlenir (8⁴·7¹² → 14¹²)."""
    u = lambda t, e: ('u', t, e)
    m = lambda t: ('m', t)
    ic = '<defs>' + ok_isareti('okE1', 'g-s') + '</defs>'
    kartlar = (
        (6, MAVI, 'Tabanları eşitle', [
            [u('25', '3'), m(' · '), u('125', '2'), m(' · '), u('5', '−4')],
            [m('('), u('5', '2'), m(')'), ('s', '3'), m(' · '), m('('), u('5', '3'), m(')'), ('s', '2'), m(' · '), u('5', '−4')],
            [u('5', '6'), m(' · '), u('5', '6'), m(' · '), u('5', '−4')],
            [u('5', '8')]],
         [[m('25 = '), u('5', '2'), m(',  125 = '), u('5', '3')], [m('üsler çarpılır')], [m('üsler toplanır')]]),
        (222, TURUNCU, 'Üsleri eşitle', [
            [u('8', '4'), m(' · '), u('7', '12')],
            [m('('), u('2', '3'), m(')'), ('s', '4'), m(' · '), u('7', '12')],
            [u('2', '12'), m(' · '), u('7', '12')],
            [u('14', '12')]],
         [[m('8 = '), u('2', '3')], [m('üsler çarpılır')], [m('tabanlar çarpılır')]]),
    )
    for x0, (f, a, s), baslik, satirlar, etiketler in kartlar:
        ic += _kutu(x0, 8, 212, 236, a, s, 14, 2)
        ic += _hap(x0 + 36, 16, 140, 24, baslik, f, 13)
        ys = [64, 116, 168, 223]
        for i, ps in enumerate(satirlar):
            if i < 3:
                ic += _ort(x0 + 106, ys[i], ps, 13.5, 'g-y', 700)
                ic += f'<line x1="{x0 + 20}" y1="{ys[i] + 14}" x2="{x0 + 20}" y2="{ys[i] + 38}" class="g-c" stroke-width="1.8" marker-end="url(#okE1)"/>'
                ic += _sol(x0 + 32, ys[i] + 29, etiketler[i], 12.5, 'g-s', 600)
            else:
                w = _wl(ps, 17) + 26
                ic += _kutu(x0 + 106 - w / 2, ys[i] - 14, w, 28, 'g-z', s, 14, 2)
                ic += _ort(x0 + 106, ys[i], ps, 17, f, 800)
    return svg(440, 252, ic, 'Farklı görünen üslü ifadeleri eşitleme. Solda tabanlar eşitlenir: 25 üssü 3 çarpı 125 üssü 2 çarpı 5 üssü eksi 4; 25 = 5 üssü 2 ve 125 = 5 üssü 3 yazılır, '
               'üsler çarpılır ve 5 üssü 6 çarpı 5 üssü 6 çarpı 5 üssü eksi 4 olur, üsler toplanınca sonuç 5 üssü 8 bulunur. '
               'Sağda üsler eşitlenir: 8 üssü 4 çarpı 7 üssü 12; 8 = 2 üssü 3 yazılır, üsler çarpılır ve 2 üssü 12 çarpı 7 üssü 12 olur, tabanlar çarpılınca sonuç 14 üssü 12 bulunur.')


def uygula(o):
    g = {'Üssü sıfır ve negatif olan ifadeler': ornuntu(),
         'Bölme kuralları': kural_matrisi(),
         'Üssün üssü ve denk ifadeler': esitleme()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
