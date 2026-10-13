"""7. sınıf İngilizce, 2. hafta: sıfatları görünüş ve kişilik diye ayırma, İngilizce tanımdan sıfat bulma,
dinlerken başlıklı not alma ve bilgi tablosundaki notları cümleye çevirme.

Görseller yalnız MEB 7. sınıf İngilizce ders kitabındaki bilgilerle çizilir (Unit 1, s10-s14 ve s18; Track 1.1 başlıkları
height, weight, hair, eyes, age; s13 Name, Appearance, Personality, Hobbies tablosu); kişi adları ve notlar kurgusaldır.
Renk anlamı:
- Ayırma: mavi = görünüş (appearance), yeşil = kişilik (personality).
- Tanım: mavi = davranışı anlatan İngilizce cümle (anahtar söz kalın), yeşil = o davranışın kişilik sıfatı.
- Not tablosu: mor = dinlenen kişi, mavi = başlık, gri = alınan not.
- Tablodan cümleye: mavi = görünüş, yeşil = kişilik, turuncu = hobiler; cümle kutusu, aynı renkteki sütundan kurulur.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _gri(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boy=12.5, sinif='g-y', kalin=False, hiza='middle'):
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, kimlik):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="2" '
            f'marker-end="url(#{kimlik})"/>')


def _cip(x, y, w, ad, renk):
    """Sözcük kartı: tema zemininde, sütun renginde çerçeveli küçük kutu."""
    _, s, f = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="12" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="12" class="{s}" stroke-width="1.5"/>'
            + _yazi(x + w / 2, y + 19, ad, 12, f))


def ayirma():
    """Kitap s10-s11 ve s18 (Test Yourself 1): sıfatlar görünüş ve kişilik diye iki gruba ayrılır; Track 1.2'deki
    friendly, serious, strict ve good-looking de bu gruplara girer."""
    ic = _yazi(236, 20, 'Appearance or personality?', 12.5, 'g-s', kalin=True)
    gruplar = [('mavi', 8, 'Appearance', 'görünüş: gözle görülür',
                ['beautiful', 'handsome', 'good-looking', 'plump', 'blonde', 'middle-aged']),
               ('yesil', 240, 'Personality', 'kişilik: davranışla anlaşılır',
                ['easy-going', 'generous', 'stubborn', 'friendly', 'serious', 'strict'])]
    for renk, x, ad, alt, sozler in gruplar:
        ic += _kutu(x, 32, 224, 182, renk)
        ic += _yazi(x + 112, 54, ad, 13, RENK[renk][2], kalin=True)
        ic += _yazi(x + 112, 72, alt, 12, RENK[renk][2])
        for n, soz in enumerate(sozler):
            ic += _cip(x + 12 + (n % 2) * 104, 88 + (n // 2) * 40, 96, soz, renk)
    return svg(472, 222, ic, 'Sıfatları gruplama: beautiful, handsome, good-looking, plump, curly ve middle-aged görünüşü; '
               'easy-going, generous, stubborn, friendly, serious ve strict kişiliği anlatır.')


def tanim():
    """Kitap s11 (Activity 3) ve s18: kişilik sıfatı, davranışı anlatan bir İngilizce cümleden bulunur; cümleler özgündür."""
    ic = '<defs>' + ok_isareti('okING72a', 'g-s') + '</defs>'
    ic += _yazi(236, 20, 'Davranışı anlatan anahtar söz → kişilik sıfatı', 12.5, 'g-s', kalin=True)
    satirlar = [('He ', 'never changes his mind', '.', 'stubborn'),
                ('She ', 'shares', ' her things with others.', 'generous'),
                ('He ', 'only thinks about', ' himself.', 'selfish'),
                ('She ', 'doesn’t worry', ' about small things.', 'easy-going'),
                ('He ', 'loves meeting new people', '.', 'outgoing')]
    for n, (bas, anahtar, son, sifat) in enumerate(satirlar):
        y = 32 + n * 40
        ic += _kutu(8, y, 300, 30, 'mavi', rx=8)
        ic += (f'<text x="20" y="{y + 20}" text-anchor="start" font-size="12" class="g-mf">{bas}'
               f'<tspan font-weight="800">{anahtar}</tspan>{son}</text>')
        ic += _ok(312, y + 15, 340, y + 15, 'okING72a')
        ic += _kutu(344, y, 120, 30, 'yesil', rx=8) + _yazi(404, y + 20, sifat, 12.5, 'g-yf', kalin=True)
    return svg(472, 232, ic, 'Anahtar sözden sıfata: never changes his mind stubborn; shares generous; only thinks about himself selfish; '
               'doesn’t worry easy-going; loves meeting new people outgoing.')


def not_tablosu():
    """Kitap s12 (Activity 5) ve Track 1.1: dinlerken notlar height, weight, hair, eyes ve age başlıkları altına yazılır."""
    ic = _yazi(236, 20, 'Dinlerken not tablosu', 12.5, 'g-s', kalin=True)
    ic += _kutu(8, 30, 456, 30, 'mor', rx=8) + _yazi(236, 50, 'Listen: Mrs. Aksoy, our new music teacher', 12.5, 'g-of', kalin=True)
    satirlar = [('Height', 'of medium height'), ('Weight', 'slim'), ('Hair', 'short · wavy · dark'),
                ('Eyes', 'hazel'), ('Age', 'middle-aged (not young, not old)')]
    for n, (baslik, not_) in enumerate(satirlar):
        y = 68 + n * 34
        ic += _kutu(8, y, 116, 28, 'mavi', rx=6) + _yazi(66, y + 19, baslik, 12.5, 'g-mf', kalin=True)
        ic += _gri(132, y, 332, 28, rx=6) + _yazi(146, y + 19, not_, 12.5, 'g-y', hiza='start')
    return svg(472, 242, ic, 'Dinlerken not tablosu: Mrs. Aksoy için height of medium height, weight slim, hair short wavy dark, '
               'eyes hazel, age middle-aged.')


def tablo_cumle():
    """Kitap s13 (Activity 7-8) ve s140 (Student B): Name, Appearance, Personality, Hobbies tablosundaki notlar cümleye çevrilir."""
    ic = '<defs>' + ok_isareti('okING72b', 'g-s') + '</defs>'
    sutun = [('gri', 8, 100, 'Name', ['Zeynep']),
             ('mavi', 112, 120, 'Appearance', ['tall, slim,', 'dark hair,', 'brown eyes']),
             ('yesil', 236, 112, 'Personality', ['friendly,', 'honest']),
             ('turuncu', 352, 112, 'Hobbies', ['swimming,', 'drawing'])]
    for renk, x, w, baslik, notlar in sutun:
        if renk == 'gri':
            ic += _gri(x, 8, w, 26, rx=6) + _yazi(x + w / 2, 26, baslik, 12.5, 'g-y', kalin=True)
            ic += _gri(x, 38, w, 64, rx=6)
            yazi = 'g-y'
        else:
            ic += _kutu(x, 8, w, 26, renk, rx=6) + _yazi(x + w / 2, 26, baslik, 12.5, RENK[renk][2], kalin=True)
            ic += _kutu(x, 38, w, 64, renk, rx=6)
            yazi = RENK[renk][2]
        ilk = 74 - 8 * (len(notlar) - 1)
        for n, satir in enumerate(notlar):
            ic += _yazi(x + w / 2, ilk + 16 * n, satir, 12, yazi, kalin=(renk == 'gri'))
    ic += _ok(236, 106, 236, 124, 'okING72b')
    cumleler = [('mavi', 'She is tall and slim. She has dark hair and brown eyes.'),
                ('yesil', 'She is friendly and honest.'),
                ('turuncu', 'She likes swimming and drawing.')]
    for n, (renk, cumle) in enumerate(cumleler):
        y = 128 + n * 36
        ic += _kutu(8, y, 456, 30, renk, rx=8) + _yazi(236, y + 20, cumle, 12.5, RENK[renk][2])
    return svg(472, 244, ic, 'Tablodan cümleye: Zeynep için görünüş notları “She is tall and slim. She has dark hair and brown eyes.”, '
               'kişilik notları “She is friendly and honest.”, hobi notları “She likes swimming and drawing.” cümlesine çevrilir.')


def uygula(o):
    g = {'Görünüş mü, kişilik mi?': ayirma(),
         'İngilizce tanımdan sıfata': tanim(),
         'Dinlerken başlıklara göre not alma': not_tablosu(),
         'Tablodaki notlardan cümleye': tablo_cumle()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
