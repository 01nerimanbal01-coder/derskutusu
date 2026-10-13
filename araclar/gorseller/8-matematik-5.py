"""8. sınıf Matematik, 5. hafta: bilimsel gösterim (a · 10ⁿ, 1 ≤ |a| < 10), çok büyük ve çok küçük sayıların yazılışı, karşılaştırma.

Renk anlamı: mor = katsayı (rakamları), mavi = pozitif üs ve sola kayan virgül, turuncu = negatif üs ve sağa kayan virgül.
Görseldeki her sayı ve her adım metindeki örneklerle aynıdır; hiçbir şekil ölçekli çizim iddiası taşımaz.
"""
from ozet_gorsel import svg, ok_isareti

_US = 0.72    # üs yazısının oranı
_GEN = {' ': 0.30, ' ': 0.30, ',': 0.30, '.': 0.30, '·': 0.34, '(': 0.36, ')': 0.36, '’': 0.26, '=': 0.60, '>': 0.60,
        '<': 0.60, '+': 0.60, '−': 0.60, ';': 0.32, ':': 0.32, '1': 0.50, 'l': 0.30, 'i': 0.30, 't': 0.36, 'ı': 0.30}

MAVI = ('g-mf', 'g-ma', 'g-ms')
TURUNCU = ('g-tf', 'g-ta', 'g-ts')
MOR = ('g-of', 'g-oa', 'g-os')
NB = ' '


def _cw(ch):
    if ch in '023456789':
        return 0.62        # kalın rakamlar: güvenli (geniş) tahmin
    return _GEN.get(ch, 0.58)


def _mw(metin, boy):
    return sum(_cw(c) for c in metin) * boy


def _pw(p, boy):
    if p[0] == 'm':
        return _mw(p[1], boy)
    return _mw(p[1], boy) + _mw(p[2], boy * _US) + 1      # ('u', taban, üs, sınıf)


def _dw(ps, boy):
    return sum(_pw(p, boy) for p in ps)


def _dizi(x, y, ps, boy, kalin=700, anchor='start'):
    """Parçaları tek <text> içinde akışla dizer (genişlik tahmini yok; yazı tipi ne olursa olsun boşluklar korunur).
    (x, y): başlangıç (ya da anchor='middle' ise orta) noktası ve yazı tabanı. Parça: ('m', metin, sınıf) ya da ('u', taban, üs, sınıf)."""
    ic = f'<text x="{x:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" text-anchor="{anchor}">'
    geri = 0.0
    for p in ps:
        dy = f' dy="{geri:.1f}"' if geri else ''
        geri = 0.0
        if p[0] == 'm':
            ic += f'<tspan class="{p[2]}"{dy}>{p[1]}</tspan>'
        else:
            ic += f'<tspan class="{p[3]}"{dy}>{p[1]}</tspan>'
            ic += f'<tspan class="{p[3]}" font-size="{boy * _US:.1f}" dy="{-boy * 0.46:.1f}">{p[2]}</tspan>'
            geri = boy * 0.46
    return ic + '</text>'


def _ort(xc, y, ps, boy, kalin=700):
    return _dizi(xc, y, ps, boy, kalin, 'middle')


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


def _rozet(x, y, n, renk, r=8.5):
    f, a, s = renk
    return (f'<circle cx="{x:.1f}" cy="{y:g}" r="{r}" class="{a}"/><circle cx="{x:.1f}" cy="{y:g}" r="{r}" class="{s}" stroke-width="1.6"/>'
            f'<text x="{x:.1f}" y="{y + 3.7:.1f}" text-anchor="middle" font-size="10.5" font-weight="800" class="{f}">{n}</text>')


def _sozluk_kare(x, y, renk, metin):
    f, a, s = renk
    return (f'<rect x="{x:g}" y="{y:g}" width="14" height="14" rx="4" class="{a}"/><rect x="{x:g}" y="{y:g}" width="14" height="14" rx="4" class="{s}" stroke-width="1.6"/>'
            + _yazi(x + 21, y + 11.5, metin, 12.5, 'g-y', 'start', 600))


def _lejant(renk, rozet_metin):
    """Virgül şeritlerinin açıklaması (iki satır): ilk yer, yeni yer, katsayının rakamları, kayılan basamak sayısı."""
    f, a, s = renk
    ic = f'<line x1="14" y1="196" x2="28" y2="196" class="g-c" stroke-width="2.4" stroke-dasharray="4 3" stroke-linecap="round"/>'
    ic += _yazi(35, 200, 'virgülün ilk yeri', 12.5, 'g-y', 'start', 600)
    ic += f'<line x1="224" y1="196" x2="238" y2="196" class="{s}" stroke-width="3" stroke-linecap="round"/>'
    ic += _yazi(245, 200, 'virgülün yeni yeri', 12.5, 'g-y', 'start', 600)
    ic += _sozluk_kare(14, 211, MOR, 'katsayının rakamları')
    ic += _rozet(231, 218, 1, renk, 7.5)
    ic += _yazi(245, 222, rozet_metin, 12.5, 'g-y', 'start', 600)
    return ic


# ---------------------------------------------------------------------------------------------------------------------
def gezegenler():
    """Merkür, Dünya, Neptün: yazılışı → bilimsel gösterim. Katsayı mor, 10'un kuvveti mavi."""
    satirlar = [('Merkür', '57' + NB + '000' + NB + '000' + NB + 'km', '5,7', '7'),
                ('Dünya', '148' + NB + '000' + NB + '000' + NB + 'km', '1,48', '8'),
                ('Neptün', '4' + NB + '495' + NB + '000' + NB + '000' + NB + 'km', '4,495', '9')]
    ic = '<defs>' + ok_isareti('okG', 'g-s') + '</defs>'
    ic += _yazi(100, 20, 'Ortalama uzaklık', 11.5, 'g-s')
    ic += _yazi(282, 20, 'Bilimsel gösterim', 11.5, 'g-s')
    for i, (ad, sayi, kats, us) in enumerate(satirlar):
        y0 = 30 + i * 58
        ic += _kutu(8, y0, 424, 48, 'g-z', 'g-c', 12, 1.8)
        ic += _yazi(22, y0 + 29, ad, 15, 'g-y', 'start', 800)
        ic += _yazi(100, y0 + 29, sayi, 14, 'g-y', 'start', 600)
        ic += f'<line x1="248" y1="{y0 + 24}" x2="270" y2="{y0 + 24}" class="g-c" stroke-width="1.8" marker-end="url(#okG)"/>'
        ic += _dizi(282, y0 + 30, [('m', kats, 'g-of'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', us, 'g-mf'), ('m', NB + 'km', 'g-y')], 16, 700)
    ic += _sozluk_kare(14, 208, MOR, 'katsayı: 1 ile 10 arasında')
    ic += _sozluk_kare(240, 208, MAVI, '10’un kuvveti')
    return svg(440, 232, ic, 'Merkür, Dünya ve Neptün’ün Güneş’e ortalama uzaklıkları ve bilimsel gösterimleri: Merkür 57 milyon kilometre, 5,7 çarpı 10 üssü 7; '
               'Dünya 148 milyon kilometre, 1,48 çarpı 10 üssü 8; Neptün 4 milyar 495 milyon kilometre, 4,495 çarpı 10 üssü 9. '
               'Katsayı 1 ile 10 arasında kalır; üs 7, 8, 9 diye artar.')


def _virgul_seridi(rakamlar, vurgulu, x0, bw, gap, y, h):
    """Rakam kutuları. vurgulu: katsayının rakamlarının dizinleri (mor), diğerleri soluk."""
    ic = ''
    for k, r in enumerate(rakamlar):
        x = x0 + k * (bw + gap)
        if k in vurgulu:
            ic += _kutu(x, y, bw, h, MOR[1], MOR[2], 7, 1.8)
            ic += _yazi(x + bw / 2, y + h / 2 + 7, r, 21, MOR[0], 'middle', 800)
        else:
            ic += _kutu(x, y, bw, h, 'g-z', 'g-c', 7, 1.5)
            ic += _yazi(x + bw / 2, y + h / 2 + 6.5, r, 19, 'g-s', 'middle', 700)
    return ic


def buyuk_sayi():
    """63 400 000 000: virgül sağ uçtan ilk rakamın sağına 10 basamak sola gelir → 6,34 · 10¹⁰."""
    rak = list('63400000000')                       # 11 rakam
    bw, gap, x0, y, h = 32, 2, 34, 42, 36
    adim = bw + gap
    ic = '<defs>' + ok_isareti('okB', 'g-mf') + '</defs>'
    ic += _virgul_seridi(rak, {0, 1, 2}, x0, bw, gap, y, h)
    # virgülün ilk yeri: son rakamın sağı (kesikli), yeni yeri: ilk rakamın sağı (mavi çizgi)
    x_son = x0 + 11 * adim - gap + 4
    ic += f'<line x1="{x_son:g}" y1="{y - 6}" x2="{x_son:g}" y2="{y + h + 6}" class="g-c" stroke-width="2.4" stroke-dasharray="4 3" stroke-linecap="round"/>'
    x_yeni = x0 + 1 * adim - gap / 2
    ic += f'<line x1="{x_yeni:g}" y1="{y - 6}" x2="{x_yeni:g}" y2="{y + h + 6}" class="g-ms" stroke-width="3" stroke-linecap="round"/>'
    for b in range(1, 11):                          # b. sınır: kutu b-1 ile b arasında
        xb = x0 + b * adim - gap / 2
        ic += _rozet(xb, 22, 11 - b, MAVI)
    ic += f'<line x1="{x_son:g}" y1="{y + h + 20}" x2="{x_yeni + 7:g}" y2="{y + h + 20}" class="g-ms" stroke-width="2.2" marker-end="url(#okB)"/>'
    ic += _hap(238, y + h + 30, 196, 26, 'virgül 10 basamak sola', 'g-mf', 12.5)
    ic += _ort(220, 170, [('m', '63' + NB + '400' + NB + '000' + NB + '000' + NB + '=' + NB, 'g-y'), ('m', '6,34', 'g-of'),
                          ('m', NB + '·' + NB, 'g-y'), ('u', '10', '10', 'g-mf')], 18, 800)
    ic += _lejant(MAVI, 'kaydığı basamak sayısı')
    return svg(440, 232, ic, '63 400 000 000 sayısının bilimsel gösterimi: sayının sonundaki virgül, ilk rakam olan 6’nın sağına kadar 10 basamak sola kayar; '
               'katsayı 6,34 olur ve üs 10’dur. Sonuç: 63 400 000 000 eşittir 6,34 çarpı 10 üssü 10.')


def kucuk_sayi():
    """0,000 000 52: virgül ilk yerinden 5'in sağına 7 basamak sağa gelir → 5,2 · 10⁻⁷."""
    rak = ['0', '0', '0', '0', '0', '0', '0', '5', '2']     # D0 (virgülün solu), D1..D6 sıfır, D7 = 5, D8 = 2
    bw, gap, x0, y, h = 36, 2, 50, 42, 36
    adim = bw + gap
    ic = '<defs>' + ok_isareti('okK', 'g-tf') + '</defs>'
    ic += _virgul_seridi(rak, {7, 8}, x0, bw, gap, y, h)
    x_ilk = x0 + 1 * adim - gap / 2                  # 1. sınır: 0 ile 0 arası
    x_yeni = x0 + 8 * adim - gap / 2                 # 8. sınır: 5 ile 2 arası
    ic += f'<line x1="{x_ilk:g}" y1="{y - 6}" x2="{x_ilk:g}" y2="{y + h + 6}" class="g-c" stroke-width="2.4" stroke-dasharray="4 3" stroke-linecap="round"/>'
    ic += f'<line x1="{x_yeni:g}" y1="{y - 6}" x2="{x_yeni:g}" y2="{y + h + 6}" class="g-ts" stroke-width="3" stroke-linecap="round"/>'
    for b in range(2, 9):                            # 2..8. sınırlar: virgülün geçtiği basamaklar
        ic += _rozet(x0 + b * adim - gap / 2, 22, b - 1, TURUNCU)
    ic += f'<line x1="{x_ilk:g}" y1="{y + h + 20}" x2="{x_yeni - 7:g}" y2="{y + h + 20}" class="g-ts" stroke-width="2.2" marker-end="url(#okK)"/>'
    ic += _hap(220, y + h + 30, 190, 26, 'virgül 7 basamak sağa', 'g-tf', 12.5)
    ic += _ort(220, 170, [('m', '0,000' + NB + '000' + NB + '52' + NB + '=' + NB, 'g-y'), ('m', '5,2', 'g-of'),
                          ('m', NB + '·' + NB, 'g-y'), ('u', '10', '−7', 'g-tf')], 18, 800)
    ic += _lejant(TURUNCU, 'kaydığı basamak sayısı')
    return svg(440, 232, ic, '0,000 000 52 sayısının bilimsel gösterimi: virgül ilk yerinden, sıfır olmayan ilk rakam olan 5’in sağına kadar 7 basamak sağa kayar; '
               'katsayı 5,2 olur ve üs eksi 7’dir. Sonuç: 0,000 000 52 eşittir 5,2 çarpı 10 üssü eksi 7.')


def karsilastirma():
    """Üç karşılaştırma: kararı veren parça renklidir (üs mavi/turuncu, katsayı mor)."""
    kartlar = [
        (8, MAVI, [('m', '4,2', 'g-y'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', '6', 'g-mf')],
         [('m', '9,8', 'g-y'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', '5', 'g-mf')], 'üslere bak: 6 > 5', 150),
        (92, MOR, [('m', '3,6', 'g-of'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', '8', 'g-y')],
         [('m', '3,06', 'g-of'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', '8', 'g-y')], 'üsler eşit; katsayılara bak: 3,6 > 3,06', 292),
        (176, TURUNCU, [('m', '3', 'g-y'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', '−5', 'g-tf')],
         [('m', '8', 'g-y'), ('m', NB + '·' + NB, 'g-y'), ('u', '10', '−7', 'g-tf')], 'üslere bak: −5 > −7', 160),
    ]
    ic = ''
    for y0, (f, a, s), sol, sag, neden, pw in kartlar:
        ic += _kutu(8, y0, 424, 76, 'g-z', s, 12, 1.8)
        ic += _ort(116, y0 + 30, sol, 20, 700)
        ic += _yazi(220, y0 + 32, '&gt;', 26, 'g-y', 'middle', 800)
        ic += _ort(324, y0 + 30, sag, 20, 700)
        ic += _hap(220, y0 + 44, pw, 24, neden, f, 12)
    return svg(440, 260, ic, 'Üç karşılaştırma. 4,2 çarpı 10 üssü 6, 9,8 çarpı 10 üssü 5’ten büyüktür çünkü üs 6, 5’ten büyüktür. '
               '3,6 çarpı 10 üssü 8, 3,06 çarpı 10 üssü 8’den büyüktür çünkü üsler eşittir ve 3,6, 3,06’dan büyüktür. '
               '3 çarpı 10 üssü eksi 5, 8 çarpı 10 üssü eksi 7’den büyüktür çünkü eksi 5, eksi 7’den büyüktür.')


def uygula(o):
    g = {'Bilimsel gösterim nedir?': gezegenler(),
         'Çok büyük sayıları bilimsel gösterimle yazmak': buyuk_sayi(),
         'Çok küçük sayıları bilimsel gösterimle yazmak': kucuk_sayi(),
         'Bilimsel gösterimle yazılan sayıları karşılaştırmak': karsilastirma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
