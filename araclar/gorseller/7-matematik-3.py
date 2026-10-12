"""7. sınıf Matematik, 3. hafta: rasyonel sayıların ondalık gösterimleri (bölme, sonlu/devirli, paydanın asal çarpanları,
paydayı 10'un kuvvetine getirme).

Görseller yalnız MEB 7. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 41-44).
Renk anlamı: mavi = sonlu ondalık gösterim (ve devretmeyen rakam), turuncu = devirli ondalık gösterim (ve devreden rakam),
mavi sonuç kutusu = sonlu ondalık gösterim; gri = açıklama. Her bölünme/genişletme adımı metindeki örneklerle aynıdır.
"""
from ozet_gorsel import svg, ok_isareti, kesir_svg


def _kutu(x, y, w, h, sinif_dolgu, sinif_cizgi, rx=10, kalin=2):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{sinif_dolgu}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{sinif_cizgi}" stroke-width="{kalin}"/>')


def _hap(x, y, w, h, metin, sinif, boy=12.5):
    """Başlık hapı: yüzey dolgusu + renkli çizgi + renkli yazı (açık ve koyu temada okunur)."""
    c = sinif.replace('f', 's')
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" class="{c}" stroke-width="1.8"/>'
            f'<text x="{x + w / 2:g}" y="{y + h / 2 + boy * 0.36:.1f}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{sinif}">{metin}</text>')


def bolme():
    """1/5 → 0,2 (kalan 0, bölme biter); 1/3 → 0,333… (kalan hep 1, bölme sürer)."""
    ic = '<defs>' + ok_isareti('okW3a', 'g-mf') + ok_isareti('okW3b', 'g-tf') + '</defs>'
    y0 = 8
    for x0, ad, f, a, s, pay, payda, ok in ((8, 'Sonlu ondalık gösterim', 'g-mf', 'g-ma', 'g-ms', '1', '5', 'okW3a'),
                                            (226, 'Devirli ondalık gösterim', 'g-tf', 'g-ta', 'g-ts', '1', '3', 'okW3b')):
        cx = x0 + 103
        ic += _kutu(x0, y0, 206, 230, a, s, rx=14)
        ic += _hap(x0 + 8, y0 + 10, 190, 24, ad, f)
        ic += kesir_svg(x0 + 58, y0 + 60, pay, payda, f, 16)
        ic += f'<text x="{x0 + 80}" y="{y0 + 66}" font-size="16" font-weight="700" class="g-y">= {pay} ÷ {payda}</text>'
        # 1. adım
        ic += _kutu(x0 + 14, y0 + 90, 178, 26, 'g-z', s, rx=8, kalin=1.6)
        bol = '10 ÷ 5 = 2, kalan 0' if payda == '5' else '10 ÷ 3 = 3, kalan 1'
        ic += f'<text x="{cx}" y="{y0 + 108}" text-anchor="middle" font-size="14" font-weight="700" class="{f}">{bol}</text>'
        if payda == '3':
            ic += _kutu(x0 + 14, y0 + 122, 178, 26, 'g-z', s, rx=8, kalin=1.6)
            ic += f'<text x="{cx}" y="{y0 + 140}" text-anchor="middle" font-size="14" class="g-y">yine 10 ÷ 3, kalan 1</text>'
            ic += f'<text x="{cx}" y="{y0 + 170}" text-anchor="middle" font-size="13" font-weight="700" class="{f}">Kalan hep 1: bölme sürer</text>'
            sonuc = '0,333…'
        else:
            ic += f'<line x1="{cx}" y1="{y0 + 120}" x2="{cx}" y2="{y0 + 144}" class="{s}" stroke-width="2.2" marker-end="url(#{ok})"/>'
            ic += f'<text x="{cx}" y="{y0 + 170}" text-anchor="middle" font-size="13" font-weight="700" class="{f}">Kalan 0: bölme biter</text>'
            sonuc = '0,2'
        ic += _kutu(x0 + 51, y0 + 184, 104, 32, 'g-z', f.replace('f', 's'), rx=16, kalin=2)
        ic += f'<text x="{cx}" y="{y0 + 206}" text-anchor="middle" font-size="19" font-weight="800" class="{f}">{sonuc}</text>'
    return svg(440, 246, ic, 'Payı paydaya bölme: 1 bölü 5 için 10 bölü 5 eşittir 2, kalan 0; bölme biter ve sonuç 0,2 sonlu ondalık gösterimdir. '
               '1 bölü 3 için 10 bölü 3 eşittir 3, kalan 1; yine 10 bölü 3 gelir, kalan hep 1 kalır, bölme sürer ve sonuç 0,333… devirli ondalık gösterimdir.')


def devir_hucreleri():
    """0,333… → 0,3̅ ; 0,2727… → 0,2̅7̅ ; 0,8333… → 0,83̅ (devreden = turuncu, devretmeyen = mavi)."""
    ic = '<defs>' + ok_isareti('okW3d', 'g-s') + '</defs>'
    gen, yuk = 26, 34
    ic += '<text x="14" y="17" font-size="12.5" font-weight="700" class="g-s">Açık yazılış</text>'
    ic += '<text x="236" y="17" font-size="12.5" font-weight="700" class="g-s">Devir işaretiyle</text>'

    def hucre(x, y, ch, tur):
        if tur == 'nokta':
            return f'<text x="{x + 7}" y="{y + 25}" text-anchor="middle" font-size="19" font-weight="700" class="g-y">{ch}</text>', 14
        if tur == 'bos':
            return f'<text x="{x + gen / 2:g}" y="{y + 25}" text-anchor="middle" font-size="19" font-weight="700" class="g-s">{ch}</text>', gen
        a, s, f = {'tam': ('g-z', 'g-c', 'g-y'), 'dev': ('g-ta', 'g-ts', 'g-tf'), 'sab': ('g-ma', 'g-ms', 'g-mf')}[tur]
        r = (f'<rect x="{x + 1}" y="{y}" width="{gen - 2}" height="{yuk}" rx="6" class="{a}"/>'
             f'<rect x="{x + 1}" y="{y}" width="{gen - 2}" height="{yuk}" rx="6" class="{s}" stroke-width="1.8"/>'
             f'<text x="{x + gen / 2:g}" y="{y + 25}" text-anchor="middle" font-size="19" font-weight="800" class="{f}">{ch}</text>')
        return r, gen

    satirlar = [
        (['0', ',', '3', '3', '3', '…'], ['tam', 'nokta', 'dev', 'dev', 'dev', 'bos'],
         ['0', ',', '3'], ['tam', 'nokta', 'dev']),
        (['0', ',', '2', '7', '2', '7', '…'], ['tam', 'nokta', 'dev', 'dev', 'dev', 'dev', 'bos'],
         ['0', ',', '2', '7'], ['tam', 'nokta', 'dev', 'dev']),
        (['0', ',', '8', '3', '3', '3', '…'], ['tam', 'nokta', 'sab', 'dev', 'dev', 'dev', 'bos'],
         ['0', ',', '8', '3'], ['tam', 'nokta', 'sab', 'dev']),
    ]
    for k, (acik, tur, kisa, ktur) in enumerate(satirlar):
        y = 36 + k * 62
        x = 14
        for ch, t in zip(acik, tur):
            s, w = hucre(x, y, ch, t)
            ic += s
            x += w
        ic += f'<line x1="196" y1="{y + 17}" x2="216" y2="{y + 17}" class="g-c" stroke-width="2" marker-end="url(#okW3d)"/>'
        x = 236
        bas = None
        for ch, t in zip(kisa, ktur):
            if t == 'dev' and bas is None:
                bas = x
            s, w = hucre(x, y, ch, t)
            ic += s
            x += w
        ic += f'<line x1="{bas + 3:g}" y1="{y - 7}" x2="{x - 3:g}" y2="{y - 7}" class="g-ts" stroke-width="3" stroke-linecap="round"/>'
    ic += '<rect x="14" y="224" width="16" height="16" rx="4" class="g-ta"/><rect x="14" y="224" width="16" height="16" rx="4" class="g-ts" stroke-width="1.8"/>'
    ic += '<text x="38" y="237" font-size="12.5" class="g-y">devreden rakam</text>'
    ic += '<rect x="166" y="224" width="16" height="16" rx="4" class="g-ma"/><rect x="166" y="224" width="16" height="16" rx="4" class="g-ms" stroke-width="1.8"/>'
    ic += '<text x="190" y="237" font-size="12.5" class="g-y">devretmeyen rakam</text>'
    return svg(440, 250, ic, '0,333… sayısı 0,3 üzerinde devir işaretiyle, 0,2727… sayısı 0,27 üzerinde devir işaretiyle yazılır. '
               '0,8333… sayısında 8 devretmeyen rakamdır, 3 devreden rakamdır ve devir işareti yalnız 3’ün üzerine çizilir.')


def asal_carpan_karari():
    """En sade hâldeki paydanın asal çarpanlarına göre karar: 2 ve 5 ise sonlu, değilse devirli (dört örnek)."""
    ic = ''
    sutun = ((8, 'g-mf', 'g-ma', 'g-ms', ('En sade hâlde paydada', 'yalnız 2 ve 5 varsa: sonlu')),
             (226, 'g-tf', 'g-ta', 'g-ts', ('En sade hâlde paydada', 'başka çarpan varsa: devirli')))
    for x0, f, a, s, (l1, l2) in sutun:
        ic += _kutu(x0, 8, 206, 46, a, s, rx=12, kalin=2)
        ic += f'<text x="{x0 + 103}" y="28" text-anchor="middle" font-size="12" font-weight="800" class="{f}">{l1}</text>'
        ic += f'<text x="{x0 + 103}" y="46" text-anchor="middle" font-size="12" font-weight="800" class="{f}">{l2}</text>'

    def kart(x0, y0, f, a, s, ic_kesir, payda_yazi, sonuc, genis=76):
        r = _kutu(x0, y0, 206, 88, a, s, rx=12, kalin=1.6)
        r += ic_kesir
        r += f'<text x="{x0 + 14}" y="{y0 + 76}" font-size="13" class="g-y">{payda_yazi}</text>'
        r += _kutu(x0 + 206 - 14 - genis, y0 + 20, genis, 30, 'g-z', f.replace('f', 's'), rx=15, kalin=2)
        r += f'<text x="{x0 + 206 - 14 - genis / 2:g}" y="{y0 + 41}" text-anchor="middle" font-size="15" font-weight="800" class="{f}">{sonuc}</text>'
        return r

    y1, y2 = 62, 158
    # sonlu kartlar
    k1 = (kesir_svg(8 + 30, y1 + 36, '72', '15', 'g-mf', 15)
          + f'<text x="{8 + 56}" y="{y1 + 41}" font-size="15" font-weight="700" class="g-y">=</text>'
          + kesir_svg(8 + 86, y1 + 36, '24', '5', 'g-mf', 15))
    ic += kart(8, y1, 'g-mf', 'g-ma', 'g-ms', k1, 'Sadeleşince payda 5', '4,8', 60)
    k2 = kesir_svg(8 + 30, y2 + 36, '3', '20', 'g-mf', 15)
    ic += kart(8, y2, 'g-mf', 'g-ma', 'g-ms', k2, 'Payda: 20 = 2 · 2 · 5', '0,15', 60)
    # devirli kartlar
    k3 = kesir_svg(226 + 30, y1 + 36, '92', '15', 'g-tf', 15)
    ic += kart(226, y1, 'g-tf', 'g-ta', 'g-ts', k3, 'Payda: 15 = 3 · 5', '6,1333…')
    k4 = kesir_svg(226 + 30, y2 + 36, '5', '6', 'g-tf', 15)
    ic += kart(226, y2, 'g-tf', 'g-ta', 'g-ts', k4, 'Payda: 6 = 2 · 3', '0,8333…')
    return svg(440, 254, ic, 'En sade hâlde paydada yalnız 2 ve 5 asal çarpanı varsa ondalık gösterim sonludur: 72 bölü 15 sadeleşince 24 bölü 5 olur ve 4,8 bulunur; '
               '3 bölü 20 için 20 eşittir 2 çarpı 2 çarpı 5 ve sonuç 0,15’tir. Paydada başka bir asal çarpan varsa devirlidir: '
               '92 bölü 15 için 15 eşittir 3 çarpı 5 ve sonuç 6,1333…; 5 bölü 6 için 6 eşittir 2 çarpı 3 ve sonuç 0,8333…’tür.')


def genisletme():
    """Paydayı 10'un kuvvetine getirme: 7/20 → 5 ile çarp → 35/100 → 0,35; 5/8 → 125 ile çarp → 625/1000 → 0,625; 2 3/4 → 25 ile çarp → 2 75/100 → 2,75."""
    ic = '<defs>' + ok_isareti('okW3c', 'g-tf') + '</defs>'
    satir = [
        (None, ('7', '20'), '5', None, ('35', '100'), '0,35', 'iki basamak'),
        (None, ('5', '8'), '125', None, ('625', '1000'), '0,625', 'üç basamak'),
        ('2', ('3', '4'), '25', '2', ('75', '100'), '2,75', 'iki basamak'),
    ]
    for k, (tam1, (p1, q1), carpan, tam2, (p2, q2), sonuc, basamak) in enumerate(satir):
        cy = 44 + k * 72
        if tam1:
            ic += f'<text x="18" y="{cy + 6}" text-anchor="middle" font-size="18" font-weight="700" class="g-mf">{tam1}</text>'
            ic += kesir_svg(44, cy, p1, q1, 'g-mf', 17)
        else:
            ic += kesir_svg(34, cy, p1, q1, 'g-mf', 17)
        ic += f'<line x1="78" y1="{cy}" x2="150" y2="{cy}" class="g-ts" stroke-width="2.4" marker-end="url(#okW3c)"/>'
        ic += f'<text x="114" y="{cy - 13}" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">{carpan} ile çarp</text>'
        ic += f'<text x="114" y="{cy + 22}" text-anchor="middle" font-size="12" class="g-s">pay ve payda</text>'
        if tam2:
            ic += f'<text x="178" y="{cy + 6}" text-anchor="middle" font-size="18" font-weight="700" class="g-mf">{tam2}</text>'
            ic += kesir_svg(210, cy, p2, q2, 'g-mf', 17)
        else:
            ic += kesir_svg(196, cy, p2, q2, 'g-mf', 17)
        ic += f'<text x="258" y="{cy + 6}" text-anchor="middle" font-size="18" font-weight="700" class="g-y">=</text>'
        ic += _kutu(274, cy - 17, 74, 34, 'g-z', 'g-ms', rx=17, kalin=2)
        ic += f'<text x="311" y="{cy + 6}" text-anchor="middle" font-size="19" font-weight="800" class="g-mf">{sonuc}</text>'
        ic += f'<text x="357" y="{cy + 5}" font-size="12" class="g-s">{basamak}</text>'
    return svg(440, 232, ic, 'Paydayı 10’un kuvvetine getirme: 7 bölü 20, pay ve payda 5 ile çarpılınca 35 bölü 100 olur ve 0,35 bulunur; '
               '5 bölü 8, pay ve payda 125 ile çarpılınca 625 bölü 1000 olur ve 0,625 bulunur; tam sayılı kesir 2 tam 3 bölü 4, '
               'kesirli kısım 25 ile genişleyince 2 tam 75 bölü 100 olur ve 2,75 bulunur. Payda 100 iki, payda 1000 üç basamak verir.')


def uygula(o):
    g = {'Payı paydaya bölerek ondalık gösterim bulmak': bolme(),
         'Sonlu ve devirli ondalık gösterim': devir_hucreleri(),
         'Paydanın asal çarpanları neyi belirler?': asal_carpan_karari(),
         'Paydayı 10’un kuvvetine getirmek': genisletme()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
