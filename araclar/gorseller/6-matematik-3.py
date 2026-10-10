"""6. sınıf Matematik, 3. hafta: asal sayılar, asal çarpanlar, ortak kat, ortak bölen.

Görseller yalnız MEB 6. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 38-56).
Renk anlamı: asal sayı ve asal çarpan = turuncu; asal olmayan sayı = mavi; ortak kat ve ortak bölen = yeşil;
4'ün katları = mavi, 6'nın katları = turuncu (sayı doğrusunda); kalburda her adımın katları ayrı renktir.
Ölçü içeren görseller tek ölçekle çizilir (kare birimleri aynı boyda, sayı doğrusunda birim aralığı sabit).
"""
from ozet_gorsel import svg, ok_isareti, dugum, dal


def _asallar(n):
    return [k for k in range(2, n + 1) if all(k % d for d in range(2, int(k ** 0.5) + 1))]


def dikdortgen_modelleri():
    """Alanı 2-9 birimkare olan dikdörtgen zeminler: asal alan tek modelli, asal olmayan alan birden çok modelli."""
    u = 10
    sol = [(2, [(1, 2)]), (3, [(1, 3)]), (5, [(1, 5)]), (7, [(1, 7)])]
    sag = [(4, [(1, 4), (2, 2)]), (6, [(1, 6), (2, 3)]), (8, [(1, 8), (2, 4)]), (9, [(1, 9), (3, 3)])]
    ic = '<text x="12" y="20" font-size="13" font-weight="800" class="g-tf">Tek dikdörtgen</text>'
    ic += '<text x="232" y="20" font-size="13" font-weight="800" class="g-mf">Birden çok dikdörtgen</text>'
    for kol, veri, x_et, x_model, renk in ((0, sol, 12, 68, ('g-ta', 'g-ts', 'g-tf')), (1, sag, 232, 286, ('g-ma', 'g-ms', 'g-mf'))):
        for i, (n, modeller) in enumerate(veri):
            cy = 59 + 58 * i
            ic += f'<text x="{x_et}" y="{cy + 5}" font-size="13" font-weight="800" class="{renk[2]}">Alan {n}</text>'
            x = x_model
            for (r, c) in modeller:
                w, h = c * u, r * u
                top = cy - h / 2
                for rr in range(r):
                    for cc in range(c):
                        ic += f'<rect x="{x + cc * u + 0.75:g}" y="{top + rr * u + 0.75:g}" width="{u - 1.5:g}" height="{u - 1.5:g}" rx="1.5" class="{renk[0]}"/>'
                ic += f'<rect x="{x}" y="{top:g}" width="{w}" height="{h}" rx="2" class="{renk[1]}" stroke-width="1.8"/>'
                ic += f'<text x="{x + w / 2:g}" y="{cy + 29}" text-anchor="middle" font-size="12" class="g-s">{r} × {c}</text>'
                x += w + 16
    ic += '<text x="12" y="284" font-size="12" class="g-s">Her kare 1 birimkaredir.</text>'
    return svg(440, 292, ic, 'Alanı 2, 3, 5 ve 7 birimkare olan zeminler yalnız tek dikdörtgenle, alanı 4, 6, 8 ve 9 birimkare olan zeminler '
               'birden çok dikdörtgenle modellenir. Dikdörtgenler: 2 için 1 × 2; 3 için 1 × 3; 5 için 1 × 5; 7 için 1 × 7; 4 için 1 × 4 ve 2 × 2; '
               '6 için 1 × 6 ve 2 × 3; 8 için 1 × 8 ve 2 × 4; 9 için 1 × 9 ve 3 × 3.')


def kalbur():
    """Eratosten kalburu: yüzlük tabloda 2, 3, 5 ve 7'nin katları çizilir; üzeri çizilmeyenler asaldır."""
    asal = set(_asallar(100))
    cw, ch, x0, y0 = 34, 28, 20, 12
    stil = {2: ('g-ma', 'g-mf'), 3: ('g-ya', 'g-yf'), 5: ('g-oa', 'g-of'), 7: ('g-s', 'g-s')}
    ic = ''
    for n in range(1, 101):
        r, c = divmod(n - 1, 10)
        x, y = x0 + c * cw, y0 + r * ch
        tx, ty = x + cw / 2, y + ch / 2 + 4.5
        if n == 1:
            ic += f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="4" class="g-c" stroke-width="1.2" stroke-dasharray="3 3"/>'
            ic += f'<text x="{tx:g}" y="{ty:g}" text-anchor="middle" font-size="13" class="g-s">1</text>'
        elif n in asal:
            ic += f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="4" class="g-tf"/>'
            ic += f'<text x="{tx:g}" y="{ty:g}" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{n}</text>'
        else:
            p = next(p for p in (2, 3, 5, 7) if n % p == 0)
            dolgu, yazi = stil[p]
            sk = ' fill-opacity=".22"' if p == 7 else ''
            ic += f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="4" class="{dolgu}"{sk}/>'
            ic += f'<text x="{tx:g}" y="{ty:g}" text-anchor="middle" font-size="13" text-decoration="line-through" class="{yazi}">{n}</text>'
    # gösterge
    def chip(x, y, metin, sinif, ek=''):
        s = f'<rect x="{x}" y="{y - 12}" width="16" height="16" rx="4" class="{sinif}"/>' + ek
        return s + f'<text x="{x + 22}" y="{y}" font-size="12" class="g-y">{metin}</text>'
    yl = y0 + 10 * ch + 22
    ic += chip(20, yl, 'asal sayı', 'g-tf')
    ic += chip(130, yl, '2’nin katları', 'g-ma')
    ic += chip(255, yl, '3’ün katları', 'g-ya')
    yl2 = yl + 22
    ic += chip(20, yl2, '5’in katları', 'g-oa')
    ic += chip(140, yl2, '7’nin katları', 'g-s').replace('class="g-s"/>', 'class="g-s" fill-opacity=".22"/>', 1)
    ic += (f'<rect x="258" y="{yl2 - 12}" width="16" height="16" rx="4" class="g-c" stroke-width="1.2" stroke-dasharray="3 3"/>'
           f'<text x="280" y="{yl2}" font-size="12" class="g-y">1 (asal değil)</text>')
    ic += f'<text x="20" y="{yl2 + 24}" font-size="12" class="g-s">Renk, sayının ilk çizildiği adımı gösterir.</text>'
    return svg(384, yl2 + 34, ic, 'Yüzlük tabloda 2, 3, 5 ve 7’nin katlarının üzeri sırayla çizilir. 1 asal değildir. Üzeri çizilmeyen sayılar asaldır: '
               + ', '.join(str(a) for a in sorted(asal)) + '.')


def agac_ve_algoritma():
    """60'ın asal çarpanları: çarpan ağacı (solda) ve asal çarpan algoritması (sağda)."""
    D = {'60': (120, 48, 'kok', 22), 'a': (70, 108, 'asal', 22), '30': (170, 108, 'bilesik', 22),
         'b': (130, 168, 'asal', 22), '15': (210, 168, 'bilesik', 22), 'c': (170, 228, 'asal', 22), 'd': (250, 228, 'asal', 22)}
    ad = {'60': '60', 'a': '2', '30': '30', 'b': '2', '15': '15', 'c': '3', 'd': '5'}
    kenar = [('60', 'a'), ('60', '30'), ('30', 'b'), ('30', '15'), ('15', 'c'), ('15', 'd')]
    ic = '<text x="12" y="16" font-size="14" font-weight="800" class="g-mf">Çarpan ağacı</text>'
    ic += ''.join(dal(D[a][0], D[a][1], D[a][3], D[b][0], D[b][1], D[b][3]) for a, b in kenar)
    ic += ''.join(dugum(x, y, ad[k], t, r) for k, (x, y, t, r) in D.items())
    # algoritma
    ic += '<text x="312" y="16" font-size="14" font-weight="800" class="g-mf">Asal çarpan</text>'
    ic += '<text x="312" y="32" font-size="14" font-weight="800" class="g-mf">algoritması</text>'
    satir = [(60, 2), (30, 2), (15, 3), (5, 5), (1, None)]
    ic += '<line x1="362" y1="52" x2="362" y2="246" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'
    for i, (n, b) in enumerate(satir):
        y = 72 + 40 * i
        ic += f'<text x="352" y="{y}" text-anchor="end" font-size="20" font-weight="{800 if i == 0 else 600}" class="{"g-mf" if i == 0 else "g-y"}">{n}</text>'
        if b:
            ic += f'<circle cx="386" cy="{y - 7}" r="14" class="g-tf"/><text x="386" y="{y - 1.5:g}" text-anchor="middle" font-size="16" font-weight="800" class="g-b">{b}</text>'
    ic += ('<text x="215" y="284" text-anchor="middle" font-size="19" font-weight="700" class="g-y">60 = '
           '<tspan class="g-tf">2</tspan> × <tspan class="g-tf">2</tspan> × <tspan class="g-tf">3</tspan> × <tspan class="g-tf">5</tspan></text>')
    ic += '<circle cx="96" cy="305" r="7" class="g-tf"/><text x="108" y="310" font-size="13" class="g-s">asal çarpan</text>'
    ic += '<circle cx="230" cy="305" r="7" class="g-ma"/><circle cx="230" cy="305" r="7" class="g-ms" stroke-width="1.5"/><text x="242" y="310" font-size="13" class="g-s">asal değil</text>'
    return svg(430, 322, ic, '60 sayısının asal çarpanları. Çarpan ağacında 60 = 2 × 30, 30 = 2 × 15, 15 = 3 × 5; uçlarda 2, 2, 3 ve 5 kalır. '
               'Asal çarpan algoritmasında 60, 30, 15, 5 ve 1 sayıları alt alta, sağda 2, 2, 3 ve 5 yazılır. Sonuç: 60 = 2 × 2 × 3 × 5.')


def sayi_dogrusu_katlar():
    """4'ün ve 6'nın katları aynı ölçekli sayı doğrularında; ortak katlar 12, 24 ve 36."""
    x0, b = 112, 9.2
    X = lambda n: x0 + b * n
    ic = '<defs>' + ok_isareti('okK3', 'g-s') + '</defs>'
    satirlar = [(40, '4’ün katları', range(4, 37, 4), 'g-mf'), (100, '6’nın katları', range(6, 37, 6), 'g-tf'), (160, 'Ortak katlar', range(12, 37, 12), 'g-yf')]
    for y, ad, kat, f in satirlar:
        ic += f'<text x="8" y="{y + 4}" font-size="12" font-weight="800" class="{f}">{ad}</text>'
        ic += f'<line x1="{x0}" y1="{y}" x2="462" y2="{y}" class="g-c" stroke-width="2" marker-end="url(#okK3)"/>'
        ic += f'<circle cx="{x0}" cy="{y}" r="3.5" class="g-s"/>'
        for n in kat:
            ic += f'<circle cx="{X(n):g}" cy="{y}" r="11" class="{f}"/>'
            ic += f'<text x="{X(n):g}" y="{y + 4.5}" text-anchor="middle" font-size="12" font-weight="800" class="g-b">{n}</text>'
    for y, y2 in ((40, 100), (100, 160)):
        for n in (12, 24, 36):
            ic += f'<line x1="{X(n):g}" y1="{y + 12}" x2="{X(n):g}" y2="{y2 - 12}" class="g-ys" stroke-width="2" stroke-dasharray="4 4"/>'
    for y in (40, 100):
        ic += f'<text x="{x0}" y="{y + 21}" text-anchor="middle" font-size="12" class="g-s">0</text>'
    ic += '<text x="8" y="198" font-size="12.5" class="g-y">Yeşil noktalar iki sayının da katı olan sayılardır.</text>'
    return svg(470, 208, ic, 'Aynı ölçekli üç sayı doğrusu. 0’dan başlayıp dörder ilerleyince 4, 8, 12, 16, 20, 24, 28, 32, 36 işaretlenir; altışar ilerleyince '
               '6, 12, 18, 24, 30, 36 işaretlenir. İki doğruda da işaretlenen 12, 24 ve 36 ortak katlardır.')


def venn_bolenler():
    """18 ile 27'nin bölenleri; ortak bölenler 1, 3 ve 9."""
    ic = '<circle cx="160" cy="118" r="86" class="g-ma"/><circle cx="280" cy="118" r="86" class="g-ta"/>'
    ic += '<path d="M220 56.4 A86 86 0 0 1 220 179.6 A86 86 0 0 1 220 56.4 Z" class="g-ya"/>'
    ic += '<circle cx="160" cy="118" r="86" class="g-ms" stroke-width="2.5"/><circle cx="280" cy="118" r="86" class="g-ts" stroke-width="2.5"/>'
    ic += '<text x="132" y="22" text-anchor="middle" font-size="14" font-weight="800" class="g-mf">18’in bölenleri</text>'
    ic += '<text x="308" y="22" text-anchor="middle" font-size="14" font-weight="800" class="g-tf">27’nin bölenleri</text>'
    for k, n in enumerate((2, 6, 18)):
        ic += f'<text x="130" y="{95 + 30 * k}" text-anchor="middle" font-size="20" font-weight="800" class="g-mf">{n}</text>'
    for k, n in enumerate((1, 3, 9)):
        ic += f'<text x="220" y="{95 + 30 * k}" text-anchor="middle" font-size="20" font-weight="800" class="g-yf">{n}</text>'
    ic += '<text x="308" y="125" text-anchor="middle" font-size="20" font-weight="800" class="g-tf">27</text>'
    ic += '<text x="220" y="232" text-anchor="middle" font-size="15" font-weight="800" class="g-yf">Ortak bölenler: 1, 3, 9</text>'
    return svg(440, 244, ic, '18’in bölenleri 1, 2, 3, 6, 9 ve 18; 27’nin bölenleri 1, 3, 9 ve 27. İki kümenin kesişiminde yer alan 1, 3 ve 9 ortak bölenlerdir; '
               'yalnız 18’de 2, 6 ve 18, yalnız 27’de 27 bulunur.')


def uygula(o):
    g = {'Asal sayı: yalnız iki çarpanı olan sayı': dikdortgen_modelleri(),
         'Eratosten kalburuyla asal sayıları bulma': kalbur(),
         'Asal çarpanlar ve çarpan ağacı': agac_ve_algoritma(),
         'İki sayının ortak katları': sayi_dogrusu_katlar(),
         'İki sayının ortak bölenleri': venn_bolenler()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
