"""6. sınıf Temel Dinî Bilgiler (İslam 1), 2. hafta: Niçin inanıyorum?

Görseller yalnız MEB 6. sınıf Temel Dinî Bilgiler (İslam 1) ders kitabındaki bilgilerle çizilir (kitap s. 21-28).
Renk anlamı: mavi = inanç esasları, yeşil = salih amel ve mümin, turuncu = imanın kökü ve münafık,
gri = kâfir ve hadisteki uyarı.
"""
from ozet_gorsel import svg

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _gri(x, y, w, h, rx=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boy=12.5, sinif='g-y', kalin=False, hiza='middle'):
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def esaslar():
    """Kitap s. 22-23: Amentü duası ve Bilgi Görseli 1.1, İslam’ın altı inanç esası."""
    ic = _yazi(236, 20, 'Amentü’de sayılan inanç esasları', 12.5, 'g-s', kalin=True)
    ad = ['1. Allah’a', '2. Meleklere', '3. Kitaplara', '4. Peygamberlere', '5. Ahiret gününe', '6. Kader ve kazaya']
    for i, a in enumerate(ad):
        x = 6 + (i % 3) * 156
        y = 32 + (i // 3) * 64
        ic += _kutu(x, y, 148, 54, 'mavi')
        ic += _yazi(x + 74, y + 24, a, 12.5, 'g-mf', kalin=True)
        ic += _yazi(x + 74, y + 43, 'iman', 12.5, 'g-mf')
    ic += _kutu(6, 166, 460, 46, 'turuncu', rx=10)
    ic += _yazi(236, 185, 'Esaslar ayrılmaz bir bütündür.', 12.5, 'g-tf', kalin=True)
    ic += _yazi(236, 203, 'Birine inanmamak imanın bütünlüğünü bozar.', 12, 'g-tf')
    return svg(472, 220, ic, 'Amentü’de sayılan altı inanç esası: 1. Allah’a iman, 2. meleklere iman, 3. kitaplara iman, '
               '4. peygamberlere iman, 5. ahiret gününe iman, 6. kader ve kazaya iman. Esaslar ayrılmaz bir bütündür; '
               'birine inanmamak imanın bütünlüğünü bozar.')


def agac():
    """Kitap s. 25: iman ile amel bir ağacın kökü ve dalları gibidir."""
    ic = '<rect x="222" y="118" width="28" height="72" rx="4" class="g-ta"/>'
    ic += '<rect x="222" y="118" width="28" height="72" rx="4" class="g-ts" stroke-width="2"/>'
    ic += '<ellipse cx="236" cy="70" rx="226" ry="62" class="g-ya"/>'
    ic += '<ellipse cx="236" cy="70" rx="226" ry="62" class="g-ys" stroke-width="2"/>'
    ic += _yazi(236, 34, 'Dallar: salih ameller', 12.5, 'g-yf', kalin=True)
    for x, y, a in ((120, 64, 'Dürüst olmak'), (236, 64, 'Sözünü tutmak'), (360, 64, 'Yardımsever olmak'),
                    (160, 94, 'Kötülükten sakınmak'), (322, 94, 'İhtiyaç sahibine vermek')):
        ic += _yazi(x, y, a, 12.5, 'g-y', kalin=True)
    ic += '<line x1="40" y1="190" x2="432" y2="190" class="g-c" stroke-width="2"/>'
    for x2 in (196, 236, 276):
        ic += f'<line x1="236" y1="190" x2="{x2}" y2="206" class="g-ts" stroke-width="2"/>'
    ic += _yazi(210, 160, 'Kök sağlam oldukça', 12.5, 'g-s', hiza='end')
    ic += _yazi(262, 160, 'dallar canlı olur', 12.5, 'g-s', hiza='start')
    ic += _kutu(96, 206, 280, 46, 'turuncu', rx=10)
    ic += _yazi(236, 225, 'Kök: iman', 12.5, 'g-tf', kalin=True)
    ic += _yazi(236, 243, 'kalp ile tasdik, dil ile söyleme', 12, 'g-tf')
    return svg(472, 258, ic, 'İman ile amel bir ağacın kökü ve dalları gibidir. Kök imandır: kalp ile tasdik, dil ile söyleme. '
               'Dallar salih amellerdir: dürüst olmak, sözünü tutmak, yardımsever olmak, kötülükten sakınmak, ihtiyaç '
               'sahibine vermek. Kök sağlam oldukça dallar canlı olur.')


def insanlar():
    """Kitap s. 27, Bilgi Görseli 1.2: iman bakımından insanlar; münafığın alameti hadisi."""
    grup = [('Mümin', 'yesil', 'inanır', 'söyler'),
            ('Kâfir', None, 'inkâr eder', 'açıkça reddeder'),
            ('Münafık', 'turuncu', 'inanmaz', 'inandığını söyler')]
    ic = ''
    for k, (ad, renk, kalp, dil) in enumerate(grup):
        x = 6 + k * 156
        f = RENK[renk][2] if renk else 'g-s'
        ic += _kutu(x, 10, 148, 34, renk, rx=10) if renk else _gri(x, 10, 148, 34, rx=10)
        ic += _yazi(x + 74, 32, ad, 13, f, kalin=True)
        ic += _gri(x, 52, 148, 96, rx=10)
        ic += _yazi(x + 74, 72, 'Kalbiyle', 12, 'g-s')
        ic += _yazi(x + 74, 90, kalp, 12.5, 'g-y', kalin=True)
        ic += _yazi(x + 74, 114, 'Diliyle', 12, 'g-s')
        ic += _yazi(x + 74, 132, dil, 12.5, 'g-y', kalin=True)
    ic += _kutu(6, 158, 460, 48, 'turuncu', rx=10)
    ic += _yazi(236, 177, 'Münafığın üç alameti (hadis)', 12.5, 'g-tf', kalin=True)
    ic += _yazi(236, 196, 'yalan söyler · emanete ihanet eder · sözünde durmaz', 12, 'g-tf')
    return svg(472, 214, ic, 'İman bakımından insanlar: mümin kalbiyle inanır, diliyle söyler; kâfir kalbiyle inkâr eder, '
               'diliyle açıkça reddeder; münafık kalbiyle inanmaz, diliyle inandığını söyler. Hadise göre münafığın üç '
               'alameti: yalan söyler, emanete ihanet eder, sözünde durmaz.')


def uygula(o):
    g = {'Amentü ve altı inanç esası': esaslar(),
         'İman ve salih amel: kök ile dallar': agac(),
         'İman bakımından insanlar': insanlar()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
