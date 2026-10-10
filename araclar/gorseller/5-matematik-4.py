"""5. sınıf Matematik, 4. hafta: iki ya da üç doğrunun birbirine göre durumu ve oluşan açılar.

Görseller yalnız MEB 5. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 45-56).
Renk anlamı: dar açı = mavi, geniş açı = turuncu, dik açı = yeşil, bütünler açı = mor;
doğruların durumunda kesişen = turuncu, paralel = mavi, çakışık = yeşil. Açılar gerçek ölçülerine uygun, tek ölçekle çizilir.
"""
import math

from ozet_gorsel import svg, ok_isareti


def _nk(cx, cy, r, aci):
    """Merkezi (cx, cy) olan çember üzerinde, saat yönünün tersine ölçülen aci (derece) noktası."""
    t = math.radians(aci)
    return cx + r * math.cos(t), cy - r * math.sin(t)


def _yay(cx, cy, r, a0, a1):
    x0, y0 = _nk(cx, cy, r, a0)
    x1, y1 = _nk(cx, cy, r, a1)
    buyuk = 1 if (a1 - a0) > 180 else 0
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {buyuk} 0 {x1:.1f} {y1:.1f}'


def _dilim(cx, cy, r, a0, a1):
    return f'M{cx} {cy} L' + _yay(cx, cy, r, a0, a1)[1:] + ' Z'


def _dogru(cx, cy, yar, aci, sinif='g-c', kalin=3, ok='ok4g'):
    """Merkezden geçen, iki ucu oklu doğru (aci derece)."""
    x0, y0 = _nk(cx, cy, yar, aci + 180)
    x1, y1 = _nk(cx, cy, yar, aci)
    return (f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" class="{sinif}" stroke-width="{kalin}" '
            f'stroke-linecap="round" marker-start="url(#{ok})" marker-end="url(#{ok})"/>')


def uc_durum():
    """İki doğrunun üç durumu: kesişen (turuncu), paralel (mavi), çakışık (yeşil)."""
    ic = '<defs>' + ok_isareti('ok4k', 'g-tf') + ok_isareti('ok4p', 'g-mf') + ok_isareti('ok4c', 'g-yf') + '</defs>'
    # kesişen
    cx, cy = 80, 62
    ic += _dogru(cx, cy, 54, 35, 'g-ts', 3, 'ok4k') + _dogru(cx, cy, 54, 125, 'g-ts', 3, 'ok4k')
    ic += f'<circle cx="{cx}" cy="{cy}" r="6" class="g-tf"/>'
    ic += f'<text x="{cx}" y="140" text-anchor="middle" font-size="14" font-weight="800" class="g-tf">Kesişen doğrular</text>'
    ic += f'<text x="{cx}" y="158" text-anchor="middle" font-size="12" class="g-s">bir ortak nokta</text>'
    # paralel
    cx = 240
    for y in (42, 82):
        ic += f'<line x1="{cx - 56}" y1="{y}" x2="{cx + 56}" y2="{y}" class="g-ms" stroke-width="3" stroke-linecap="round" marker-start="url(#ok4p)" marker-end="url(#ok4p)"/>'
    ic += f'<text x="{cx}" y="140" text-anchor="middle" font-size="14" font-weight="800" class="g-mf">Paralel doğrular</text>'
    ic += f'<text x="{cx}" y="158" text-anchor="middle" font-size="12" class="g-s">ortak nokta yok</text>'
    # çakışık
    cx = 400
    ic += f'<line x1="{cx - 56}" y1="62" x2="{cx + 56}" y2="62" class="g-ys" stroke-width="10" stroke-linecap="round" opacity=".28"/>'
    ic += f'<line x1="{cx - 56}" y1="62" x2="{cx + 56}" y2="62" class="g-ys" stroke-width="3" stroke-linecap="round" marker-start="url(#ok4c)" marker-end="url(#ok4c)"/>'
    ic += f'<text x="{cx}" y="140" text-anchor="middle" font-size="14" font-weight="800" class="g-yf">Çakışık doğrular</text>'
    ic += f'<text x="{cx}" y="158" text-anchor="middle" font-size="12" class="g-s">bütün noktalar ortak</text>'
    return svg(480, 168, ic, 'İki doğrunun üç durumu: kesişen doğruların bir ortak noktası vardır, paralel doğruların ortak noktası yoktur, çakışık doğruların bütün noktaları ortaktır.')


def ters_ve_komsu():
    """KM ve LN doğruları O'da kesişir: dar açılar 60° (mavi), geniş açılar 120° (turuncu)."""
    ox, oy, R = 140, 102, 108
    ic = '<defs>' + ok_isareti('ok4gb', 'g-s') + '</defs>'
    r = 48
    for (a0, a1, a, s) in ((150, 210, 'g-ma', 'g-ms'), (-30, 30, 'g-ma', 'g-ms'), (30, 150, 'g-ta', 'g-ts'), (210, 330, 'g-ta', 'g-ts')):
        ic += f'<path d="{_dilim(ox, oy, r, a0, a1)}" class="{a}"/><path d="{_yay(ox, oy, r, a0, a1)}" class="{s}" stroke-width="2"/>'
    ic += _dogru(ox, oy, R, 30, ok='ok4gb') + _dogru(ox, oy, R, 150, ok='ok4gb')
    ic += f'<circle cx="{ox}" cy="{oy}" r="4.5" class="g-y"/>'
    for ad, aci, dx, dy in (('M', 30, 6, -2), ('L', 150, -18, -2), ('K', 210, -18, 14), ('N', 330, 6, 14)):
        x, y = _nk(ox, oy, R + 6, aci)
        ic += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="16" font-weight="800" class="g-y">{ad}</text>'
    ic += f'<text x="{ox - 5}" y="{oy + 22}" font-size="14" font-weight="800" class="g-y">O</text>'
    ic += f'<text x="{ox - 70}" y="{oy + 5}" text-anchor="middle" font-size="13" font-weight="800" class="g-mf">60°</text>'
    ic += f'<text x="{ox + 72}" y="{oy + 5}" text-anchor="middle" font-size="13" font-weight="800" class="g-mf">60°</text>'
    ic += f'<text x="{ox}" y="{oy - 25}" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">120°</text>'
    ic += f'<text x="{ox}" y="{oy + 38}" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">120°</text>'
    # açıklama
    lx = 272
    ic += f'<rect x="{lx}" y="40" width="14" height="14" rx="3" class="g-ma"/><rect x="{lx}" y="40" width="14" height="14" rx="3" class="g-ms" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 22}" y="52" font-size="12" class="g-y">ters çift: 60° = 60°</text>'
    ic += f'<rect x="{lx}" y="68" width="14" height="14" rx="3" class="g-ta"/><rect x="{lx}" y="68" width="14" height="14" rx="3" class="g-ts" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 22}" y="80" font-size="12" class="g-y">ters çift: 120° = 120°</text>'
    ic += f'<rect x="{lx}" y="104" width="14" height="14" rx="3" class="g-ma"/><rect x="{lx}" y="104" width="14" height="14" rx="3" class="g-ms" stroke-width="1.5"/>'
    ic += f'<rect x="{lx + 18}" y="104" width="14" height="14" rx="3" class="g-ta"/><rect x="{lx + 18}" y="104" width="14" height="14" rx="3" class="g-ts" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 40}" y="116" font-size="12" class="g-y">komşu: 60° + 120° = 180°</text>'
    return svg(480, 208, ic, 'KM ve LN doğruları O noktasında kesişir. Karşılıklı dar açılar 60 derece, karşılıklı geniş açılar 120 derecedir; ters açılar eştir, komşu iki açının toplamı 180 derecedir.')


def uc_doğru_bir_nokta():
    """Üç doğru aynı noktada kesişir: üç durum (dar mavi, dik yeşil, geniş turuncu)."""
    R = 62
    durumlar = [(80, (0, 30, 130), [('g-tf', '2 geniş açı'), ('g-mf', '4 dar açı')]),
                (240, (0, 40, 90), [('g-yf', '2 dik açı'), ('g-mf', '4 dar açı')]),
                (400, (0, 40, 100), [('g-mf', '6 dar açı')])]
    ic = '<defs>' + ok_isareti('ok4gc', 'g-s') + '</defs>'
    cy = 82
    for cx, dgr, baslik in durumlar:
        isinlar = sorted([a for d in dgr for a in (d, d + 180)])
        isinlar.append(isinlar[0] + 360)
        for a0, a1 in zip(isinlar, isinlar[1:]):
            fark = round(a1 - a0)
            sinif = ('g-ya', 'g-ys') if fark == 90 else (('g-ma', 'g-ms') if fark < 90 else ('g-ta', 'g-ts'))
            ic += f'<path d="{_dilim(cx, cy, 40, a0, a1)}" class="{sinif[0]}"/><path d="{_yay(cx, cy, 40, a0, a1)}" class="{sinif[1]}" stroke-width="2"/>'
            if fark == 90:   # dik açı işareti
                u0, v0 = _nk(0, 0, 13, a0)
                u1, v1 = _nk(0, 0, 13, a1)
                ic += (f'<path d="M{cx + u0:.1f} {cy + v0:.1f} L{cx + u0 + u1:.1f} {cy + v0 + v1:.1f} L{cx + u1:.1f} {cy + v1:.1f}" '
                       f'class="g-ys" stroke-width="1.8"/>')
        for d in dgr:
            ic += _dogru(cx, cy, R, d, ok='ok4gc')
        ic += f'<circle cx="{cx}" cy="{cy}" r="3.5" class="g-y"/>'
        for k, (sinif, yazi) in enumerate(baslik):
            ic += f'<text x="{cx}" y="{166 + 20 * k}" text-anchor="middle" font-size="14" font-weight="800" class="{sinif}">{yazi}</text>'
    return svg(480, 194, ic, 'Üç doğru aynı noktada kesişince altı açı oluşur: ilk durumda iki geniş ve dört dar, ikinci durumda iki dik ve dört dar, üçüncü durumda altı dar açı.')


def tumler_butunler():
    """B noktasında AC, EH ve DF doğruları; m(FBC) = 32°, tümleri 58°, bütünleri 148°."""
    bx, by = 150, 158
    ic = '<defs>' + ok_isareti('ok4gd', 'g-s') + '</defs>'
    # açılar
    ic += f'<path d="{_dilim(bx, by, 72, 0, 32)}" class="g-ma"/><path d="{_yay(bx, by, 72, 0, 32)}" class="g-ms" stroke-width="2"/>'
    ic += f'<path d="{_dilim(bx, by, 72, 32, 90)}" class="g-ya"/><path d="{_yay(bx, by, 72, 32, 90)}" class="g-ys" stroke-width="2"/>'
    ic += f'<path d="{_yay(bx, by, 106, 32, 180)}" class="g-os" stroke-width="2.5" stroke-dasharray="6 4"/>'
    # doğrular
    def kenar(aci, uzun):
        x, y = _nk(bx, by, uzun, aci)
        return f'<line x1="{bx}" y1="{by}" x2="{x:.1f}" y2="{y:.1f}" class="g-c" stroke-width="3" stroke-linecap="round" marker-end="url(#ok4gd)"/>'
    ic += kenar(180, 124) + kenar(0, 124) + kenar(90, 126) + kenar(270, 58) + kenar(32, 128) + kenar(212, 128)
    ic += f'<circle cx="{bx}" cy="{by}" r="4.5" class="g-y"/>'
    # noktalar
    for ad, aci, uz, dx, dy in (('A', 180, 124, -12, -6), ('C', 0, 124, 8, 5), ('H', 90, 126, -5, -8), ('E', 270, 58, -5, 20),
                                ('F', 32, 128, 8, -4), ('D', 212, 128, -16, 16)):
        x, y = _nk(bx, by, uz, aci)
        ic += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-size="16" font-weight="800" class="g-y">{ad}</text>'
    ic += f'<text x="{bx + 9}" y="{by + 20}" font-size="16" font-weight="800" class="g-y">B</text>'
    # ölçü yazıları
    x, y = _nk(bx, by, 96, 16)
    ic += f'<text x="{x + 4:.1f}" y="{y + 5:.1f}" text-anchor="middle" font-size="14" font-weight="800" class="g-mf">32°</text>'
    x, y = _nk(bx, by, 46, 61)
    ic += f'<text x="{x + 2:.1f}" y="{y + 5:.1f}" text-anchor="middle" font-size="14" font-weight="800" class="g-yf">58°</text>'
    x, y = _nk(bx, by, 124, 108)
    ic += f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle" font-size="14" font-weight="800" class="g-of">148°</text>'
    # açıklama
    lx = 300
    ic += f'<rect x="{lx}" y="60" width="14" height="14" rx="3" class="g-ma"/><rect x="{lx}" y="60" width="14" height="14" rx="3" class="g-ms" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 22}" y="72" font-size="12" class="g-y">32° (verilen açı)</text>'
    ic += f'<rect x="{lx}" y="90" width="14" height="14" rx="3" class="g-ya"/><rect x="{lx}" y="90" width="14" height="14" rx="3" class="g-ys" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 22}" y="102" font-size="12" class="g-y">58° = 90° − 32°</text>'
    ic += f'<text x="{lx + 22}" y="118" font-size="12" class="g-s">komşu tümler</text>'
    ic += f'<line x1="{lx}" y1="140" x2="{lx + 14}" y2="140" class="g-os" stroke-width="3" stroke-dasharray="4 3"/>'
    ic += f'<text x="{lx + 22}" y="144" font-size="12" class="g-y">148° = 180° − 32°</text>'
    ic += f'<text x="{lx + 22}" y="160" font-size="12" class="g-s">komşu bütünler</text>'
    return svg(450, 250, ic, 'B noktasında kesişen AC, EH ve DF doğrularında FBC açısı 32 derecedir. Komşu tümler açısı FBH 58 derece, komşu bütünler açısı FBA 148 derecedir.')


def kesen_paralel():
    """İki paralel doğru ve bir kesen: dört dar (mavi) ve dört geniş (turuncu) açı."""
    ic = '<defs>' + ok_isareti('ok4ge', 'g-s') + '</defs>'
    y1, y2 = 64, 148
    tg = math.tan(math.radians(55))
    p1 = (160, y1)
    p2 = (160 - (y2 - y1) / tg, y2)
    for p in (p1, p2):
        for a0, a1, a, s in ((0, 55, 'g-ma', 'g-ms'), (180, 235, 'g-ma', 'g-ms'), (55, 180, 'g-ta', 'g-ts'), (235, 360, 'g-ta', 'g-ts')):
            ic += f'<path d="{_dilim(p[0], p[1], 27, a0, a1)}" class="{a}"/><path d="{_yay(p[0], p[1], 27, a0, a1)}" class="{s}" stroke-width="2"/>'
    for y in (y1, y2):
        ic += f'<line x1="20" y1="{y}" x2="262" y2="{y}" class="g-c" stroke-width="3" stroke-linecap="round" marker-start="url(#ok4ge)" marker-end="url(#ok4ge)"/>'
    ust = (160 + 44 / tg, y1 - 44)
    alt = (p2[0] - 44 / tg, y2 + 44)
    ic += (f'<line x1="{alt[0]:.1f}" y1="{alt[1]:.1f}" x2="{ust[0]:.1f}" y2="{ust[1]:.1f}" class="g-c" stroke-width="3" '
           f'stroke-linecap="round" marker-start="url(#ok4ge)" marker-end="url(#ok4ge)"/>')
    ic += f'<text x="{ust[0] + 10:.1f}" y="{ust[1] + 4:.1f}" font-size="14" font-weight="800" class="g-y">kesen</text>'
    ic += f'<text x="166" y="112" font-size="12.5" class="g-s">paralel doğrular</text>'
    lx = 296
    ic += f'<rect x="{lx}" y="70" width="14" height="14" rx="3" class="g-ma"/><rect x="{lx}" y="70" width="14" height="14" rx="3" class="g-ms" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 22}" y="82" font-size="12" class="g-y">4 dar açı</text>'
    ic += f'<rect x="{lx}" y="98" width="14" height="14" rx="3" class="g-ta"/><rect x="{lx}" y="98" width="14" height="14" rx="3" class="g-ts" stroke-width="1.5"/>'
    ic += f'<text x="{lx + 22}" y="110" font-size="12" class="g-y">4 geniş açı</text>'
    return svg(420, 208, ic, 'İki paralel doğruyu bir kesen kestiğinde iki kesişim noktasında dört dar ve dört geniş açı oluşur.')


def uygula(o):
    g = {'Doğruların birbirine göre üç durumu': uc_durum(),
         'Ters açılar ve komşu açılar': ters_ve_komsu(),
         'Üç doğru aynı noktada kesişirse': uc_doğru_bir_nokta(),
         'Tümler ve bütünler açılar': tumler_butunler(),
         'Üç doğrunun ikişer kesişimi ve kesen': kesen_paralel()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
