"""7. sınıf Sosyal Bilgiler, 2. hafta: birlikte yaşama kültürü, yazılı mesajda yanlış anlaşılma, içten özür ve uzlaşma.

Görseller yalnız MEB 7. sınıf Sosyal Bilgiler ders kitabındaki bilgilerle çizilir (s12 yapboz ve birlikte yaşama kültürü,
s13 ve s22-s23 yazılı mesajlar, s15 ve s28 özür ve göz teması, s26-s27 uzlaşma); kişi adları ve mesajlar kurgusaldır.
Renk anlamı:
- Yapboz: her parça ayrı renk; yeşil = ilişkiler, mor = dayanışma.
- Mesaj: mavi = yazanın mesajı, turuncu = okuyanın tepkisi, yeşil = niyeti açıkça yazmak; gri = görünmeyen ipuçları.
- Özür: mavi = özür dileyenin basamakları, yeşil = karşı tarafın tutumu, mor = sonuç.
- Uzlaşma: mavi ve mor = iki ayrı fikir, turuncu = tartışmayı büyüten, yeşil = uzlaşmaya götüren davranışlar.
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


def _cikinti(x, y, yon, renk):
    """Yapboz parçasının komşu parçaya taşan yarım daire çıkıntısı; yon: 'sag' ya da 'alt'."""
    a, s, _ = RENK[renk]
    if yon == 'sag':
        yay = f'M{x} {y - 9} A9 9 0 0 1 {x} {y + 9}'
        ort = f'<rect x="{x - 2}" y="{y - 8}" width="4" height="16" class="{a}"/>'
    else:
        yay = f'M{x - 9} {y} A9 9 0 0 0 {x + 9} {y}'
        ort = f'<rect x="{x - 8}" y="{y - 2}" width="16" height="4" class="{a}"/>'
    return (f'<path d="{yay} Z" class="{a}"/>' + ort +
            f'<path d="{yay}" fill="none" class="{s}" stroke-width="2"/>')


def yapboz():
    """Kitap s12: birlikte yaşama kültürünün unsurları yapboz parçaları gibi birleşir, ilişkileri ve dayanışmayı güçlendirir."""
    ic = '<defs>' + ok_isareti('okSB72a', 'g-s') + '</defs>'
    ic += _yazi(140, 20, 'Birlikte yaşama kültürünün parçaları', 12.5, 'g-s', kalin=True)
    # kayma: soldan çıkıntı giren parçada yazı çıkıntıdan uzaklaşsın diye sağa kaydırılır
    parca = [('mavi', ['Haklara saygı'], 8, 34, 0), ('yesil', ['Düşüncelere', 'saygı'], 140, 34, 4.5),
             ('turuncu', ['Dikkatle dinlemek'], 8, 98, 0), ('mor', ['Empati kurmak'], 140, 98, 4.5)]
    for renk, _, x, y, _k in parca:
        ic += _kutu(x, y, 132, 64, renk, rx=6)
    ic += _cikinti(140, 66, 'sag', 'mavi') + _cikinti(74, 98, 'alt', 'mavi')
    ic += _cikinti(206, 98, 'alt', 'yesil') + _cikinti(140, 130, 'sag', 'turuncu')
    for renk, satirlar, x, y, kayma in parca:
        ilk = y + 37 if len(satirlar) == 1 else y + 29
        for n, satir in enumerate(satirlar):
            ic += _yazi(x + 66 + kayma, ilk + 17 * n, satir, 12, RENK[renk][2], kalin=True)
    ic += _yazi(140, 184, 'Parçalar birleşince bütün oluşur.', 12, 'g-s')
    ic += _ok(275, 66, 297, 66, 'okSB72a')
    ic += _kutu(300, 34, 164, 64, 'yesil')
    ic += _yazi(382, 60, 'İlişkiler', 13, 'g-yf', kalin=True) + _yazi(382, 80, 'güçlenir', 12.5, 'g-yf')
    ic += _ok(382, 100, 382, 121, 'okSB72a')
    ic += _kutu(300, 124, 164, 64, 'mor')
    ic += _yazi(382, 150, 'Toplumsal dayanışma', 13, 'g-of', kalin=True) + _yazi(382, 170, 'desteklenir', 12.5, 'g-of')
    return svg(472, 196, ic, 'Birlikte yaşama kültürünün parçaları: haklara saygı, düşüncelere saygı, dikkatle dinlemek ve '
               'empati kurmak yapboz parçaları gibi birleşir. Bu unsurlar ilişkileri güçlendirir ve toplumsal dayanışmayı destekler.')


def mesaj():
    """Kitap s13, s22-s23: yazılı mesajda ses tonu ve beden dili görünmez; niyet açıkça yazılınca yanlış anlaşılma gider."""
    ic = _gri(8, 8, 196, 236, rx=18)
    ic += _yazi(106, 32, '7/A sınıf grubu', 12.5, 'g-s', kalin=True)
    ic += '<line x1="20" y1="42" x2="192" y2="42" class="g-c" stroke-width="1"/>'
    ic += _yazi(24, 62, 'Selin', 12, 'g-s', kalin=True, hiza='start')
    ic += _kutu(20, 68, 152, 34, 'mavi', rx=12) + _yazi(96, 90, 'Afişi kim yaptı ya?', 12.5, 'g-mf')
    ic += _yazi(188, 122, 'Kerem', 12, 'g-s', kalin=True, hiza='end')
    ic += _kutu(62, 128, 130, 34, 'turuncu', rx=12) + _yazi(127, 150, 'Beğenmedin mi?', 12.5, 'g-tf')
    ic += _yazi(24, 182, 'Selin', 12, 'g-s', kalin=True, hiza='start')
    ic += _kutu(20, 188, 160, 34, 'yesil', rx=12) + _yazi(100, 210, 'Hayır, çok beğendim!', 12.5, 'g-yf')
    ic += '<line x1="172" y1="80" x2="222" y2="44" class="g-c" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += '<line x1="172" y1="90" x2="222" y2="112" class="g-c" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += _kutu(222, 14, 244, 58, 'mavi')
    ic += _yazi(344, 36, 'Yazanın niyeti', 13, 'g-mf', kalin=True) + _yazi(344, 56, 'afişi beğendi, övmek istedi', 12, 'g-mf')
    ic += _kutu(222, 84, 244, 58, 'turuncu')
    ic += _yazi(344, 106, 'Okuyanın algısı', 13, 'g-tf', kalin=True) + _yazi(344, 126, 'eleştirildiğini sandı, üzüldü', 12, 'g-tf')
    ic += _gri(222, 154, 244, 90)
    ic += _yazi(344, 176, 'Mesajda görünmeyenler', 13, 'g-y', kalin=True)
    ic += _yazi(344, 195, 'ses tonu · bakış · beden dili', 12, 'g-y')
    ic += _yazi(344, 216, 'Çözüm: niyetini açıkça yaz,', 12, 'g-yf', kalin=True)
    ic += _yazi(344, 234, 'sor, gerekirse yüz yüze konuş', 12, 'g-yf', kalin=True)
    return svg(472, 252, ic, 'Yazılı mesajda yanlış anlaşılma: Selin sınıf grubuna "Afişi kim yaptı ya?" yazar; niyeti afişi '
               'övmektir. Afişi yapan Kerem eleştirildiğini sanıp "Beğenmedin mi?" diye sorar. Selin "Hayır, çok beğendim!" '
               'diye niyetini açıkça yazar. Mesajda ses tonu, bakış ve beden dili görünmez; çözüm niyeti açıkça yazmak, '
               'sormak ve gerekirse yüz yüze konuşmaktır.')


def ozur():
    """Kitap s15 ve s28: içten özrün basamakları, özrün anlayışla kabulü ve göz temasının verdiği mesaj."""
    ic = '<defs>' + ok_isareti('okSB72b', 'g-s') + '</defs>'
    ic += _yazi(236, 16, 'İçten bir özrün basamakları', 12.5, 'g-s', kalin=True)
    adim = [('mavi', '1. Dur', 'olanı fark et'),
            ('mavi', '2. Yardım et', 'zararı gider'),
            ('mavi', '3. Göz teması', 'kurarak konuş'),
            ('mavi', '4. Hatanı söyle', 'açık ve net'),
            ('mavi', '5. Özür dile', 'samimi bir sesle'),
            ('yesil', 'Karşı taraf', 'anlayışla kabul eder')]
    yer = [(6, 28), (166, 28), (326, 28), (326, 112), (166, 112), (6, 112)]
    for (renk, ad, alt), (x, y) in zip(adim, yer):
        f = RENK[renk][2]
        ic += _kutu(x, y, 140, 54, renk)
        ic += _yazi(x + 70, y + 23, ad, 13, f, kalin=True)
        ic += _yazi(x + 70, y + 41, alt, 12, f)
    ic += _ok(147, 55, 163, 55, 'okSB72b') + _ok(307, 55, 323, 55, 'okSB72b')
    ic += _ok(396, 83, 396, 109, 'okSB72b')
    ic += _ok(325, 139, 309, 139, 'okSB72b') + _ok(165, 139, 149, 139, 'okSB72b')
    ic += _ok(76, 167, 76, 189, 'okSB72b')
    ic += _kutu(6, 192, 460, 40, 'mor')
    ic += _yazi(236, 217, 'Sonuç: dostluk korunur, güven ortamı sürer', 13, 'g-of', kalin=True)
    return svg(472, 240, ic, 'İçten bir özrün basamakları: 1. Dur ve olanı fark et, 2. Yardım et, 3. Göz teması kurarak konuş, '
               '4. Hatanı açık ve net söyle, 5. Samimi bir sesle özür dile. Karşı taraf özrü anlayışla kabul eder. '
               'Sonuçta dostluk korunur, güven ortamı sürer.')


def uzlasma():
    """Kitap s26-s27: fikir ayrılığı; çatışmayı büyüten ve uzlaşmaya götüren davranışlar; ortak çözüm."""
    ic = '<defs>' + ok_isareti('okSB72c', 'g-s') + '</defs>'
    ic += _kutu(6, 8, 180, 50, 'mavi')
    ic += _yazi(96, 29, 'Kaan', 13, 'g-mf', kalin=True) + _yazi(96, 47, 'fotoğraf kullanalım', 12, 'g-mf')
    ic += _kutu(286, 8, 180, 50, 'mor')
    ic += _yazi(376, 29, 'Ela', 13, 'g-of', kalin=True) + _yazi(376, 47, 'çizim yapalım', 12, 'g-of')
    ic += _yazi(236, 38, 'fikir ayrılığı', 12, 'g-s', kalin=True)
    sutun = [('turuncu', 6, 'Tartışmayı büyütür', ['suçlamak', 'alay etmek', 'sözü kesmek', 'yalnız kendi fikrinde ısrar']),
             ('yesil', 242, 'Uzlaşmaya götürür', ['sözü kesmeden dinlemek', 'empati kurmak', 'ben dilini kullanmak',
                                                  'farklı fikre saygı'])]
    for renk, x, baslik, maddeler in sutun:
        f = RENK[renk][2]
        ic += _kutu(x, 76, 224, 116, renk)
        ic += _yazi(x + 112, 98, baslik, 13, f, kalin=True)
        for k, m in enumerate(maddeler):
            ic += _yazi(x + 16, 122 + k * 19, '• ' + m, 12.5, f, hiza='start')
    ic += _ok(354, 194, 354, 215, 'okSB72c')
    ic += _kutu(6, 218, 460, 42, 'yesil')
    ic += _yazi(236, 244, 'Ortak çözüm: panonun bir bölümü fotoğraf, öteki bölümü çizim', 12.5, 'g-yf', kalin=True)
    return svg(472, 268, ic, 'Fikir ayrılığından uzlaşmaya: Kaan fotoğraf kullanmak, Ela çizim yapmak ister. Suçlamak, alay etmek, '
               'sözü kesmek ve yalnız kendi fikrinde ısrar etmek tartışmayı büyütür. Sözü kesmeden dinlemek, empati kurmak, '
               'ben dilini kullanmak ve farklı fikre saygı uzlaşmaya götürür. Ortak çözüm: panonun bir bölümü fotoğraf, '
               'öteki bölümü çizim.')


def uygula(o):
    g = {'Birlikte yaşama kültürü ve iletişim': yapboz(),
         'Yazılı mesajlar neden yanlış anlaşılır?': mesaj(),
         'İçten bir özür ve sevgi dolu sözler': ozur(),
         'Fikir ayrılığından uzlaşmaya': uzlasma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
