"""7. sınıf Din Kültürü ve Ahlak Bilgisi, 3. hafta: dünya ve ahiret hayatı, ömür ve ecel, ölüm ile kıyamet.

Görseller yalnız MEB 7. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap s. 22, 25, 26).
Renk anlamı: ilk görselde mavi = dünya hayatı, mor = ahiret hayatı, turuncu = ölüm; ikinci görselde mavi = ömür,
turuncu = ecel, yeşil = doğum; üçüncü görselde turuncu = ölüm, mor = kıyamet.
Çizimlerde ölçü yoktur; kutu ve çubuk uzunlukları sürenin uzunluğunu göstermez, yalnız ilişkiyi gösterir.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12.5, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def dunya_ve_ahiret():
    """Dünya hayatı ölümle sona erer, ahiret hayatı ölümle başlar ve sürer (kitap s. 22, 26)."""
    ic = '<defs>' + ok_isareti('okDK73a', 'g-s') + '</defs>'
    ic += _kutu(12, 28, 176, 60, 'mavi')
    ic += _yazi(100, 54, 'Dünya hayatı', 15, True, 'g-mf') + _yazi(100, 74, 'bir sonu vardır', 12.5)
    ic += _kutu(216, 36, 48, 44, 'turuncu') + _yazi(240, 63, 'Ölüm', 13, True, 'g-tf')
    ic += '<line x1="192" y1="58" x2="210" y2="58" class="g-c" stroke-width="2" marker-end="url(#okDK73a)"/>'
    ic += '<line x1="268" y1="58" x2="286" y2="58" class="g-c" stroke-width="2" marker-end="url(#okDK73a)"/>'
    ic += _kutu(292, 28, 176, 60, 'mor')
    ic += _yazi(380, 54, 'Ahiret hayatı', 15, True, 'g-of') + _yazi(380, 74, 'bitmeyen hayat', 12.5)
    ic += _yazi(100, 112, 'Ölümle sona erer') + _yazi(380, 112, 'Ölümle başlar, bitmez')
    ic += _yazi(240, 148, 'Ölüm, dünya hayatını bitirir; ahiret hayatını başlatır.', 12.5, True)
    return svg(480, 164, ic, 'Dünya hayatı ile ahiret hayatı: dünya hayatının bir sonu vardır ve ölümle sona erer; '
               'ahiret hayatı ölümle başlar ve bitmez. Ölüm, dünya hayatını bitirir ve ahiret hayatını başlatır.')


def omur_ve_ecel():
    """Ömür doğumdan ölüme kadar geçen süredir; ecel ölüm vaktinin gelmesidir (kitap s. 25)."""
    ic = '<circle cx="22" cy="52" r="8" class="g-yf"/>'
    ic += _yazi(26, 90, 'Doğum', 12.5, True, 'g-yf')
    ic += '<line x1="30" y1="52" x2="44" y2="52" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'
    ic += _kutu(44, 30, 332, 44, 'mavi')
    ic += _yazi(210, 50, 'Ömür', 15, True, 'g-mf') + _yazi(210, 67, 'yaşam süresi', 12.5)
    ic += _kutu(384, 30, 84, 44, 'turuncu')
    ic += _yazi(426, 50, 'Ecel', 15, True, 'g-tf') + _yazi(426, 67, 'ölüm vakti', 11.5)
    ic += _yazi(240, 112, 'Ömür bir süredir; ecel o sürenin bittiği zamandır.', 12.5, True)
    return svg(480, 126, ic, 'Ömür ve ecel: doğumdan ölüme kadar geçen yaşam süresi ömürdür; '
               'ölüm vaktinin gelmesi, yani sürenin bittiği zaman eceldir.')


def olum_ve_kiyamet():
    """Ölüm ile kıyametin karşılaştırılması (kitap s. 26)."""
    ic = '<rect x="100" y="6" width="180" height="30" rx="15" class="g-tf"/>' + _yazi(190, 26, 'Ölüm', 14, True, 'g-b')
    ic += '<rect x="288" y="6" width="184" height="30" rx="15" class="g-of"/>' + _yazi(380, 26, 'Kıyamet', 14, True, 'g-b')
    satirlar = [
        ('Sona eren', ['Bir insanın', 'dünya hayatı'], ['Dünya ve kâinattaki', 'her şey']),
        ('Sebebi', ['Ecelin gelmesi'], ['İsrafil’in Allah’ın', 'emriyle sûra üflemesi']),
        ('Ardından', ['Kabir hayatı', '(berzah) başlar'], ['Sonsuz hayat', 'ardından başlar']),
    ]
    for k, (etiket, a, b) in enumerate(satirlar):
        y = 44 + k * 56
        ic += f'<rect x="8" y="{y}" width="84" height="48" rx="10" class="g-z"/><rect x="8" y="{y}" width="84" height="48" rx="10" class="g-c" stroke-width="1.5"/>'
        ic += _yazi(50, y + 28, etiket, 12, True)
        ic += _kutu(100, y, 180, 48, 'turuncu', 10) + _kutu(288, y, 184, 48, 'mor', 10)
        for x, satir in ((190, a), (380, b)):
            if len(satir) == 1:
                ic += _yazi(x, y + 29, satir[0])
            else:
                ic += _yazi(x, y + 21, satir[0]) + _yazi(x, y + 38, satir[1])
    ic += _yazi(240, 226, 'Kıyametin ne zaman kopacağını yalnız Allah bilir.', 12.5, True, 'g-of')
    return svg(480, 240, ic, 'Ölüm ile kıyamet: ölüm bir insanın dünya hayatını sona erdirir, ecelin gelmesiyle olur ve kabir hayatı olan berzah başlar. '
               'Kıyamet dünyayı ve kâinattaki her şeyi sona erdirir, İsrafil’in Allah’ın emriyle sûra üflemesiyle kopar ve ardından sonsuz hayat başlar. '
               'Kıyametin ne zaman kopacağını yalnız Allah bilir.')


def uygula(o):
    g = {'Dünya hayatı ve ahiret hayatı': dunya_ve_ahiret(),
         'Ömür ve ecel': omur_ve_ecel(),
         'Kıyamet': olum_ve_kiyamet()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
