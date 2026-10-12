"""7. sınıf Matematik, 4. hafta: devirli ondalık gösterimi kesre çevirme, 0,999… = 1, rasyonel sayıları sayı doğrusunda karşılaştırma ve sıralama.

Görseller yalnız MEB 7. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 45-53).
Renk anlamı: mavi = devretmeyen rakam, turuncu = devreden rakam; sıcaklık ve sayı doğrularında turuncu = negatif (eksi) değer,
mavi = pozitif (artı) değer; yeşil = bulunan sonuç; gri = açıklama. Sayı doğruları tek ölçekle çizilir; sıcaklık doğrusunda
100 °C = 54 birim uzunluk, sıralama doğrusunda 1 birim = 52 uzunluk (metindeki değerlerle aynıdır).
"""
from ozet_gorsel import svg, kesir_svg

EKSI = '−'


def _kutu(x, y, w, h, sinif_dolgu, sinif_cizgi, rx=10, kalin=2):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{sinif_dolgu}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{sinif_cizgi}" stroke-width="{kalin}"/>')


def _ok_ucu(x, y, yon, sinif='g-s'):
    """Sayı doğrusu ucu (dolu üçgen): yon = 1 sağa, -1 sola. x ok ucunun (tepe) yeridir."""
    return f'<path d="M{x - 10 * yon} {y - 5.5} L{x} {y} L{x - 10 * yon} {y + 5.5}z" class="{sinif}"/>'


def kesre_cevirme():
    """0,8333… = 0,83̅ → 75/90 = 5/6 ve 0,2727… = 0,2̅7̅ → 27/99 = 3/11."""
    gen, yuk = 26, 34
    ic = ''
    veri = [
        dict(x0=8, hucre=[('0', 'tam'), (',', 'nokta'), ('8', 'sab'), ('3', 'dev')], bar=(3, 3),
             satir=[('Bütün rakamlar: 83', 'g-z', 'g-c', 'g-y'), ('Devretmeyen rakam: 8', 'g-ma', 'g-ms', 'g-mf'),
                    ('Pay: 83 ' + EKSI + ' 8 = 75', 'g-z', 'g-c', 'g-y'), ('Payda: 90 (bir 9, bir 0)', 'g-z', 'g-c', 'g-y')],
             pay=('75', '90'), sade=('5', '6')),
        dict(x0=226, hucre=[('0', 'tam'), (',', 'nokta'), ('2', 'dev'), ('7', 'dev')], bar=(2, 3),
             satir=[('Bütün rakamlar: 27', 'g-z', 'g-c', 'g-y'), ('Devretmeyen rakam: yok', 'g-ma', 'g-ms', 'g-mf'),
                    ('Pay: 27 ' + EKSI + ' 0 = 27', 'g-z', 'g-c', 'g-y'), ('Payda: 99 (iki 9)', 'g-z', 'g-c', 'g-y')],
             pay=('27', '99'), sade=('3', '11')),
    ]
    for v in veri:
        x0, y0 = v['x0'], 8
        ic += _kutu(x0, y0, 206, 274, 'g-z', 'g-c', rx=14, kalin=1.6)
        # rakam hücreleri (devir işareti devreden hücrelerin üstünde)
        x = x0 + 57
        konum = []
        for ch, t in v['hucre']:
            if t == 'nokta':
                ic += f'<text x="{x + 7}" y="{y0 + 50}" text-anchor="middle" font-size="19" font-weight="700" class="g-y">{ch}</text>'
                konum.append((x, 14)); x += 14
                continue
            a, s, f = {'tam': ('g-z', 'g-c', 'g-y'), 'dev': ('g-ta', 'g-ts', 'g-tf'), 'sab': ('g-ma', 'g-ms', 'g-mf')}[t]
            ic += (f'<rect x="{x + 1}" y="{y0 + 24}" width="{gen - 2}" height="{yuk}" rx="6" class="{a}"/>'
                   f'<rect x="{x + 1}" y="{y0 + 24}" width="{gen - 2}" height="{yuk}" rx="6" class="{s}" stroke-width="1.8"/>'
                   f'<text x="{x + gen / 2:g}" y="{y0 + 49}" text-anchor="middle" font-size="19" font-weight="800" class="{f}">{ch}</text>')
            konum.append((x, gen)); x += gen
        b1, b2 = v['bar']
        ic += (f'<line x1="{konum[b1][0] + 3}" y1="{y0 + 16}" x2="{konum[b2][0] + konum[b2][1] - 3}" y2="{y0 + 16}" '
               f'class="g-ts" stroke-width="3" stroke-linecap="round"/>')
        for i, (yazi, a, s, f) in enumerate(v['satir']):
            y = y0 + 74 + i * 36
            ic += _kutu(x0 + 8, y, 190, 28, a, s, rx=8, kalin=1.5)
            ic += f'<text x="{x0 + 103}" y="{y + 19}" text-anchor="middle" font-size="12.5" font-weight="700" class="{f}">{yazi}</text>'
        # sonuç: pay/payda = sade kesir
        cy = y0 + 240
        ic += kesir_svg(x0 + 52, cy, v['pay'][0], v['pay'][1], 'g-yf', 17)
        ic += f'<text x="{x0 + 98}" y="{cy + 6}" text-anchor="middle" font-size="19" font-weight="800" class="g-y">=</text>'
        ic += kesir_svg(x0 + 144, cy, v['sade'][0], v['sade'][1], 'g-yf', 17)
    return svg(440, 290, ic, 'Devirli ondalık gösterimi kesre çevirme. 0,8333… yani 0,83 devir işaretiyle: bütün rakamlar 83, devretmeyen rakam 8; '
               'pay 83 eksi 8 eşittir 75, payda bir 9 ve bir 0 ile 90; sonuç 75 bölü 90 eşittir 5 bölü 6. '
               '0,2727… yani 0,27 devir işaretiyle: bütün rakamlar 27, devretmeyen rakam yok; pay 27 eksi 0 eşittir 27, payda iki 9 ile 99; '
               'sonuç 27 bölü 99 eşittir 3 bölü 11.')


def dokuzlar():
    """0,9 → 0,99 → 0,999 sayı doğrularıyla 1'e yaklaşma: her satırda son aralık 10 eş parçaya bölünür."""
    ic = ''
    x0, x1 = 40, 400
    adim = (x1 - x0) / 10
    satirlar = [
        (50, '0', '0,9', 'g-ta', '1’e uzaklık: 0,1'),
        (140, '0,9', '0,99', 'g-ta', '1’e uzaklık: 0,01'),
        (230, '0,99', '0,999', 'g-ta', '1’e uzaklık: 0,001'),
    ]
    for k, (y, sol, isaret, _, uzak) in enumerate(satirlar):
        # son aralık vurgusu
        xs = x0 + 9 * adim
        ic += f'<rect x="{xs:g}" y="{y - 13}" width="{adim:g}" height="26" rx="5" class="g-ta"/>'
        ic += f'<rect x="{xs:g}" y="{y - 13}" width="{adim:g}" height="26" rx="5" class="g-ts" stroke-width="1.6"/>'
        ic += f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" class="g-ms" stroke-width="3" stroke-linecap="round"/>'
        for t in range(11):
            tx = x0 + t * adim
            ic += f'<line x1="{tx:g}" y1="{y - 7}" x2="{tx:g}" y2="{y + 7}" class="g-ms" stroke-width="2"/>'
        ic += f'<circle cx="{xs:g}" cy="{y}" r="6" class="g-tf"/>'
        ic += f'<text x="{x0}" y="{y - 22}" text-anchor="middle" font-size="14" font-weight="800" class="g-y">{sol}</text>'
        ic += f'<text x="{x1}" y="{y - 22}" text-anchor="middle" font-size="14" font-weight="800" class="g-y">1</text>'
        ic += f'<text x="{xs:g}" y="{y - 22}" text-anchor="middle" font-size="14" font-weight="800" class="g-tf">{isaret}</text>'
        ic += f'<text x="{x0}" y="{y + 28}" font-size="12.5" class="g-s">{uzak}</text>'
        if k < 2:
            ic += f'<text x="220" y="{y + 48}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-tf">Turuncu aralık büyütülüp 10 eş parçaya bölünür</text>'
    ic += '<text x="220" y="284" text-anchor="middle" font-size="13.5" font-weight="800" class="g-yf">9’lar sonsuza kadar sürerse sayı 1’e eşit olur.</text>'
    return svg(440, 296, ic, 'Sayı doğrusunda 0,9, 0,99 ve 0,999 sayıları 1’e giderek yaklaşır. Birinci doğruda 0 ile 1 arası 10 eş parçaya bölünmüş ve 0,9 işaretlenmiştir; '
               'son aralık büyütülünce 0,9 ile 1 arasında 0,99, onun son aralığında 0,999 görülür. 1’e uzaklıklar 0,1, 0,01 ve 0,001’dir. '
               '9’lar sonsuza kadar sürerse sayı 1’e eşit olur. Her doğru kendi ölçeğiyle çizilmiştir.')


def sicakliklar():
    """Gezegenlerin yüzey sıcaklıkları (°C), tek ölçekli sayı doğrusunda: 100 °C = 54 uzunluk."""
    s = 0.54

    def X(t):
        return 20 + (t + 250) * s

    y = 120
    ic = f'<line x1="22" y1="{y}" x2="422" y2="{y}" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'
    ic += _ok_ucu(432, y, 1) + _ok_ucu(12, y, -1)
    for t in range(-200, 401, 100):
        ic += f'<line x1="{X(t):g}" y1="{y - 6}" x2="{X(t):g}" y2="{y + 6}" class="g-c" stroke-width="2"/>'
        ic += f'<text x="{X(t):g}" y="{y + 24}" text-anchor="middle" font-size="12" class="g-s">{(EKSI + str(-t)) if t < 0 else t}</text>'
    # (ad, değer, etiket merkezi x, etiket seviyesi: ust1 | ust2 | alt)
    gez = [('Neptün', -200, 36, 'ust1'), ('Uranüs', -165, 64, 'alt'), ('Satürn', -140, 79, 'ust2'),
           ('Jüpiter', -110, 114, 'ust1'), ('Mars', -65, 126, 'alt'), ('Dünya', 15, 172, 'ust1'),
           ('Merkür', 167, 245, 'ust1'), ('Venüs', 464, 396, 'ust1')]
    seviye = {'ust1': (72, 86, 92, 112), 'ust2': (24, 38, 44, 112), 'alt': (172, 186, 152, 128)}
    for ad, t, cx, sv in gez:
        px = X(t)
        f, st = ('g-tf', 'g-ts') if t < 0 else ('g-mf', 'g-ms')
        yn, yd, l1, l2 = seviye[sv]
        deger = (EKSI + str(-t) if t < 0 else str(t)) + ' °C'
        ic += f'<text x="{cx}" y="{yn}" text-anchor="middle" font-size="12.5" font-weight="800" class="{f}">{ad}</text>'
        ic += f'<text x="{cx}" y="{yd}" text-anchor="middle" font-size="12" class="g-y">{deger}</text>'
        if sv == 'alt':
            ic += f'<line x1="{px:.1f}" y1="{y + 8}" x2="{px:.1f}" y2="158" class="g-c" stroke-width="1.2"/>'
        else:
            ic += f'<line x1="{cx}" y1="{l1}" x2="{px:.1f}" y2="{l2 - 5}" class="g-c" stroke-width="1.2"/>'
        ic += f'<circle cx="{px:.1f}" cy="{y}" r="5.5" class="{f}"/>'
    ic += '<circle cx="20" cy="206" r="6" class="g-tf"/><text x="32" y="210" font-size="12.5" class="g-y">negatif değer</text>'
    ic += '<circle cx="146" cy="206" r="6" class="g-mf"/><text x="158" y="210" font-size="12.5" class="g-y">pozitif değer</text>'
    ic += '<text x="430" y="210" text-anchor="end" font-size="12.5" class="g-s">Sağa doğru büyür →</text>'
    return svg(440, 222, ic, 'Gezegenlerin yüzey sıcaklıkları aynı ölçekli sayı doğrusunda: Neptün eksi 200, Uranüs eksi 165, Satürn eksi 140, Jüpiter eksi 110 ve '
               'Mars eksi 65 santigrat derece sıfırın solundadır; Dünya 15, Merkür 167 ve Venüs 464 santigrat derece sıfırın sağındadır. '
               'Sağa gidildikçe değer büyür: Neptün en küçük, Venüs en büyük değerdir.')


def siralama_dogrusu():
    """−3 < −5/2 < −3/4 < 1/4 < 7/4: sayı doğrusunda 1 birim = 52 uzunluk."""
    u = 52
    x0 = 212

    def X(v):
        return x0 + u * v

    y = 128
    ic = f'<line x1="22" y1="{y}" x2="418" y2="{y}" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'
    ic += _ok_ucu(428, y, 1) + _ok_ucu(12, y, -1)
    for v in range(-3, 4):
        ic += f'<line x1="{X(v):g}" y1="{y - 6}" x2="{X(v):g}" y2="{y + 6}" class="g-c" stroke-width="2"/>'
        ic += f'<text x="{X(v):g}" y="{y + 24}" text-anchor="middle" font-size="13" class="g-s">{(EKSI + str(-v)) if v < 0 else v}</text>'
    # noktalar: (değer, etiket türü, seviye) ; seviye 1 alçak, 2 yüksek
    nok = [(-3, ('tam', EKSI + '3'), 2), (-2.5, ('kes', EKSI, '5', '2'), 1), (-0.75, ('kes', EKSI, '3', '4'), 1),
           (0.25, ('kes', '', '1', '4'), 1), (1.75, ('kes', '', '7', '4'), 1)]
    for v, et, sv in nok:
        px = X(v)
        f = 'g-tf' if v < 0 else 'g-mf'
        yl = 84 if sv == 1 else 50
        if et[0] == 'tam':
            ic += f'<text x="{px:g}" y="{yl + 5}" text-anchor="middle" font-size="16" font-weight="800" class="{f}">{et[1]}</text>'
            ic += f'<line x1="{px:g}" y1="{yl + 12}" x2="{px:g}" y2="{y - 8}" class="g-c" stroke-width="1.2"/>'
        else:
            ic += kesir_svg(px, yl, et[2], et[3], f, 16, et[1])
            ic += f'<line x1="{px:g}" y1="{yl + 22}" x2="{px:g}" y2="{y - 8}" class="g-c" stroke-width="1.2"/>'
        ic += f'<circle cx="{px:g}" cy="{y}" r="5.5" class="{f}"/>'
    ic += '<text x="14" y="172" font-size="12.5" class="g-s">← Sola gidildikçe küçülür</text>'
    ic += '<text x="426" y="172" text-anchor="end" font-size="12.5" class="g-s">Sağa gidildikçe büyür →</text>'
    # soldan sağa okuma
    ic += '<text x="14" y="206" font-size="12.5" font-weight="700" class="g-y">Soldan sağa okuma:</text>'
    x = 148
    belirtec = [('tam', EKSI + '3', 'g-tf'), ('lt',), ('kes', EKSI, '5', '2', 'g-tf'), ('lt',), ('kes', EKSI, '3', '4', 'g-tf'),
                ('lt',), ('kes', '', '1', '4', 'g-mf'), ('lt',), ('kes', '', '7', '4', 'g-mf')]
    for b in belirtec:
        if b[0] == 'tam':
            ic += f'<text x="{x + 9}" y="{211}" text-anchor="middle" font-size="16" font-weight="800" class="{b[2]}">{b[1]}</text>'
            x += 24
        elif b[0] == 'lt':
            ic += f'<text x="{x + 6}" y="211" text-anchor="middle" font-size="16" font-weight="700" class="g-y">&lt;</text>'
            x += 16
        else:
            sign = b[1]
            if sign:
                ic += f'<text x="{x + 5}" y="211" text-anchor="middle" font-size="16" font-weight="800" class="{b[4]}">{sign}</text>'
                x += 12
            ic += kesir_svg(x + 9, 206, b[2], b[3], b[4], 16)
            x += 24
    ic += '<circle cx="20" cy="244" r="6" class="g-tf"/><text x="32" y="248" font-size="12.5" class="g-y">negatif sayı</text>'
    ic += '<circle cx="146" cy="244" r="6" class="g-mf"/><text x="158" y="248" font-size="12.5" class="g-y">pozitif sayı</text>'
    ic = f'<g transform="translate(0 -26)">{ic}</g>'   # üstteki boş payı kırp
    return svg(440, 232, ic, 'Sayı doğrusunda eksi 3, eksi 5 bölü 2, eksi 3 bölü 4, 1 bölü 4 ve 7 bölü 4 sayıları yerleştirilmiştir. Soldan sağa gidildikçe sayılar büyür: '
               'eksi 3 küçüktür eksi 5 bölü 2 küçüktür eksi 3 bölü 4 küçüktür 1 bölü 4 küçüktür 7 bölü 4.')


def uygula(o):
    g = {'Devirli ondalık gösterimi kesre çevirmek': kesre_cevirme(),
         'Sonsuz 9’lar: 0,999… ile 1 aynı sayıdır': dokuzlar(),
         'Tam sayıları sayı doğrusunda karşılaştırmak': sicakliklar(),
         'Rasyonel sayıları sayı doğrusunda sıralamak': siralama_dogrusu()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
