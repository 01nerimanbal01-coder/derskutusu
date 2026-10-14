"""7. sınıf Kur'an-ı Kerim, 2. hafta: durak, secaventler, muaneka.

Görseller yalnız MEB 7. sınıf Kur'an-ı Kerim ders kitabındaki bilgilerle çizilir (kitap s. 22-27).
Ayet metni yazılmaz; ayet, sözcük çubuklarıyla şematik gösterilir (sağdan sola).
Renk anlamı: yeşil = durmak öne çıkar, turuncu = ikisi de olur, mavi = geçmek öne çıkar.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _gri(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boy=12.5, sinif='g-y', kalin=False, hiza='start'):
    k = ' font-weight="700"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _cubuklar(y, araliklar):
    """Sözcük çubukları: ayetin şeması (gerçek ayet metni yazılmaz)."""
    return ''.join(f'<rect x="{a}" y="{y}" width="{b - a}" height="8" rx="4" class="g-s" opacity="0.55"/>'
                   for a, b in araliklar)


def _uc_nokta(x, y):
    """Muaneka: üç nokta (biri üstte, ikisi altta)."""
    return (f'<circle cx="{x}" cy="{y}" r="3.2" class="g-y"/>'
            f'<circle cx="{x - 5.5}" cy="{y + 9}" r="3.2" class="g-y"/>'
            f'<circle cx="{x + 5.5}" cy="{y + 9}" r="3.2" class="g-y"/>')


def ayet_semasi():
    """Durak ayetin sonunda ve sayılı; secavent ayetin içinde küçük harf (s. 22, 24)."""
    ic = '<defs>' + ok_isareti('okK72a', 'g-s') + '</defs>'
    ic += _yazi(236, 20, 'Bir ayetin şeması (sağdan sola okunur)', 12.5, 'g-s', kalin=True, hiza='middle')
    ic += _gri(8, 32, 456, 46)
    ic += _cubuklar(52, [(392, 452), (334, 384), (244, 294), (176, 236), (112, 168)])
    ic += _yazi(314, 60, 'ج', 18, 'g-tf', kalin=True, hiza='middle')
    ic += '<circle cx="74" cy="55" r="17" class="g-ya"/><circle cx="74" cy="55" r="17" class="g-ys" fill="none" stroke-width="2"/>'
    ic += '<circle cx="74" cy="55" r="11" class="g-ys" fill="none" stroke-width="1.2"/>'
    ic += _yazi(74, 60, '7', 13, 'g-yf', kalin=True, hiza='middle')
    ic += '<line x1="74" y1="80" x2="74" y2="100" class="g-c" stroke-width="2" marker-end="url(#okK72a)"/>'
    ic += '<line x1="314" y1="80" x2="314" y2="100" class="g-c" stroke-width="2" marker-end="url(#okK72a)"/>'
    ic += _kutu(8, 106, 224, 86, 'yesil')
    ic += _yazi(20, 130, 'Durak', 13.5, 'g-yf', kalin=True)
    ic += _yazi(20, 154, 'Ayetin sonunda, desenli', 12.5)
    ic += _yazi(20, 176, 'İçindeki sayı: suredeki sıra', 12.5)
    ic += _kutu(240, 106, 224, 86, 'turuncu')
    ic += _yazi(252, 130, 'Secavent', 13.5, 'g-tf', kalin=True)
    ic += _yazi(252, 154, 'Ayetin içinde ya da sonunda', 12.5)
    ic += _yazi(252, 176, 'Küçük harf: dur ya da geç', 12.5)
    return svg(472, 200, ic, 'Bir ayetin şeması, sağdan sola. Ayetin içinde küçük bir secavent işareti, ayetin sonunda '
               'içinde sayı bulunan desenli durak var. Durak ayetin sonundadır, içindeki sayı ayetin suredeki sırasıdır. '
               'Secavent ayetin içinde ya da sonunda küçük harf biçimindedir, durulacak ya da geçilecek yeri gösterir.')


def _isaret_tablosu(satir, dipnot):
    ic = ''
    for k, (renk, isaret, kural, ornek) in enumerate(satir):
        y = 8 + k * 54
        ic += _kutu(8, y, 456, 48, renk)
        ic += _gri(404, y + 6, 52, 36, rx=8)
        ic += _yazi(430, y + 32, isaret, 22, RENK[renk][2], kalin=True, hiza='middle')
        ic += _yazi(20, y + 21, kural, 13, kalin=True)
        ic += _yazi(20, y + 39, ornek, 12, 'g-s')
    y = 8 + len(satir) * 54
    ic += f'<rect x="8" y="{y}" width="456" height="30" rx="8" class="g-z"/>'
    ic += _yazi(236, y + 20, dipnot, 12.5, kalin=True, hiza='middle')
    return ic, y + 38


def durma_isaretleri():
    """Durmayı öne çıkaran işaretler ve kitaptaki örnek ayetler (s. 23)."""
    ic, h = _isaret_tablosu([
        ('yesil', 'م', 'Durulması gerekir; geçilirse anlam bozulur', 'Örnek: Ankebut suresi 64. ayet'),
        ('yesil', 'ط', 'Durulması doğrudur; anlam güzel olur', 'Örnek: Neml suresi 79. ayet'),
        ('yesil', 'قف', '“Dur!” anlamında; durulması uygundur', 'Örnek: Araf suresi 26. ayet'),
        ('yesil', 'ع', 'Durulması uygundur; konu ya da kıssa biter', 'Örnek: Nebe suresi 30. ayet'),
        ('turuncu', 'ج', 'Durulabilir, geçilebilir; durmak daha uygun', 'Örnek: Mürselat suresi 38. ayet')],
        'Yeşil: durmak öne çıkar  ·  Turuncu: ikisi de olur')
    return svg(472, h, ic, 'Durmayı öne çıkaran secaventler. Mim: durulması gerekir, geçilirse anlam bozulur, Ankebut 64. '
               'Tı: durulması doğrudur, Neml 79. Kaf-fe: dur anlamında, durulması uygundur, Araf 26. '
               'Ayn: durulması uygundur, konu ya da kıssa biter, Nebe 30. Cim: durulabilir ya da geçilebilir, '
               'durmak daha uygundur, Mürselat 38.')


def gecme_isaretleri():
    """Geçmeyi öne çıkaran işaretler ve kitaptaki örnek ayetler (s. 23)."""
    ic, h = _isaret_tablosu([
        ('turuncu', 'ز', 'Durulabilir, geçilebilir; geçmek daha uygun', 'Örnek: Bakara suresi 138. ayet'),
        ('turuncu', 'ق', 'Durulabilir, geçilebilir; geçmek daha uygun', 'Örnek: Müminun suresi 17. ayet'),
        ('mavi', 'ص', 'Geçmek daha uygun; nefes yetmezse durulur', 'Örnek: Casiye suresi 37. ayet'),
        ('mavi', 'لا', '“Durma!” anlamında; durulursa geriden alınır', 'Örnek: Bakara suresi 11. ayet')],
        'Turuncu: ikisi de olur  ·  Mavi: geçmek öne çıkar')
    return svg(472, h, ic, 'Geçmeyi öne çıkaran secaventler. Ze: durulabilir ya da geçilebilir, geçmek daha uygundur, Bakara 138. '
               'Kaf: durulabilir ya da geçilebilir, geçmek daha uygundur, Müminun 17. Sad: geçmek daha uygundur, '
               'nefes yetmezse durulur, Casiye 37. Lamelif: durma anlamında, durulursa geriden alınır, Bakara 11.')


def muaneka():
    """Muaneka (s. 23): art arda iki üç nokta; yalnız birinde durulur, öbüründe geçilir."""
    ic = _yazi(236, 20, 'Art arda iki muaneka (sağdan sola): yalnız birinde durulur', 13, kalin=True, hiza='middle')
    yollar = [('1. yol', ('yesil', 'dur'), ('mavi', 'geç')), ('2. yol', ('mavi', 'geç'), ('yesil', 'dur'))]
    for k, (ad, ilk, ikinci) in enumerate(yollar):
        y = 32 + k * 82
        ic += _gri(8, y, 456, 74)
        ic += _yazi(20, y + 43, ad, 13, kalin=True)
        ic += _cubuklar(y + 16, [(400, 448), (356, 392), (262, 310), (218, 254), (130, 172), (84, 122)])
        for mx, sira, (renk, soz) in ((334, 'ilkinde', ilk), (194, 'ikincisinde', ikinci)):  # sağdaki önce okunur
            ic += _uc_nokta(mx, y + 11)
            ic += _kutu(mx - 64, y + 34, 128, 30, renk, rx=8)
            ic += _yazi(mx, y + 54, f'{sira} {soz}', 12.5, RENK[renk][2], kalin=True, hiza='middle')
    ic += '<rect x="8" y="204" width="456" height="30" rx="8" class="g-z"/>'
    ic += _yazi(236, 224, 'Muaneka noktaları başka bir secaventle birlikte yazılır', 12.5, kalin=True, hiza='middle')
    return svg(472, 242, ic, 'Bir ayette art arda iki muaneka işareti, yani üç nokta. Yalnız birinde durulur. '
               'Birinci yol: ilkinde dur, ikincisinde geç. İkinci yol: ilkinde geç, ikincisinde dur. '
               'Muaneka noktaları başka bir secaventle birlikte yazılır.')


def uygula(o):
    g = {'Secavent: ayetin içindeki küçük işaretler': ayet_semasi(),
         'Durmayı öne çıkaran işaretler': durma_isaretleri(),
         'Geçmeyi öne çıkaran işaretler': gecme_isaretleri(),
         'Muaneka ve işaretleri Mushaf’ta bulma': muaneka()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
