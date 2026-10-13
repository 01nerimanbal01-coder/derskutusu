"""7. sınıf Din Kültürü ve Ahlak Bilgisi, 2. hafta: melek, cin ve insanı karşılaştırma, Hz. Âdem kıssasında emre karşı
iki tutum, ayet ve hadislerdeki ipucundan meleğin adını ve görevini bulma, melekleri görevin zamanına göre gruplama.

Görseller yalnız MEB 7. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap s. 15-20:
Zariyat 56, Müslim “Zühd” 60, Hz. Âdem kıssası, 2. ve 3. Etkinlik, Bilgi Görseli 1.1-1.2).
Renk anlamı:
- Karşılaştırma: mavi = melek, turuncu = cin, yeşil = insan; gri = ölçüt.
- Kıssa: mor = Allah’ın emri, mavi = meleklerin tutumu, turuncu = İblis’in tutumu.
- İpucu tablosu: mor = kaynak, gri = ipucu, mavi = melek, yeşil = görev.
- Zaman: gri = görevin zamanı; mavi = dört büyük melek, mor = öteki melekler.
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
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _satirlar(x, y_orta, satirlar, boy=12, sinif='g-y', kalin=False, aralik=15):
    """Bir ya da iki satırlık yazıyı kutunun dikey ortasına yerleştirir."""
    ilk = y_orta + 4 - aralik * (len(satirlar) - 1) / 2
    return ''.join(_yazi(x, ilk + n * aralik, s, boy, sinif, kalin) for n, s in enumerate(satirlar))


def _ok(x1, y1, x2, y2, kimlik):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="2" '
            f'marker-end="url(#{kimlik})"/>')


def karsilastirma():
    """Kitap s. 16 ve s. 18: melekler nurdan, cinler yalın ateşten, Hz. Âdem topraktan yaratıldı (Müslim, “Zühd”, 60);
    cinler ve insanlar kulluk için yaratıldı, emir ve yasaklardan sorumludur (Zariyat 56); meleklerin iradeleri yoktur."""
    ic = _yazi(240, 18, 'Üç varlık, üç ölçüt', 12.5, 'g-s', kalin=True)
    sutun = [('mavi', 114, 'Melek'), ('turuncu', 236, 'Cin'), ('yesil', 358, 'İnsan')]
    for renk, x, ad in sutun:
        ic += _kutu(x, 28, 114, 30, renk, rx=8) + _yazi(x + 57, 48, ad, 13, RENK[renk][2], kalin=True)
    satirlar = [('Yaratıldığı öz', 44, [['nur'], ['yalın ateş'], ['toprak', '(Hz. Âdem)']]),
                ('Algılanma', 34, [['gayb âlemi'], ['gayb âlemi'], ['gözle görülür']]),
                ('Sorumluluk', 56, [['iradeleri yoktur'], ['emir ve', 'yasaklardan', 'sorumlu'],
                                    ['emir ve', 'yasaklardan', 'sorumlu']])]
    y = 64
    for olcut, h, degerler in satirlar:
        ic += _gri(8, y, 100, h, rx=8) + _yazi(58, y + h / 2 + 4, olcut, 12, 'g-y', kalin=True)
        for (renk, x, _), deger in zip(sutun, degerler):
            ic += _kutu(x, y, 114, h, renk, rx=8) + _satirlar(x + 57, y + h / 2, deger, 12, RENK[renk][2])
        y += h + 6
    ic += _yazi(240, y + 22, 'Şeytan cinlerdendir: ateşten yaratılmış, emre isyan etmiştir.', 12.5, 'g-y', kalin=True)
    return svg(480, y + 36, ic, 'Melek, cin ve insan karşılaştırması: melek nurdan, cin yalın ateşten, Hz. Âdem topraktan '
               'yaratılmıştır. Melek ve cin gayb âlemine aittir, insan gözle görülür. Meleklerin iradeleri yoktur; cin ve '
               'insan emir ve yasaklardan sorumludur. Şeytan cinlerdendir.')


def kissa():
    """Kitap s. 17: Hz. Âdem için saygıyla eğilme emrine meleklerin ve İblis’in tutumu."""
    ic = '<defs>' + ok_isareti('okDK72a', 'g-s') + '</defs>'
    ic += _kutu(90, 10, 300, 34, 'mor') + _yazi(240, 32, 'Emir: Hz. Âdem için saygıyla eğilin', 12.5, 'g-of', kalin=True)
    ic += _ok(170, 46, 120, 70, 'okDK72a') + _ok(310, 46, 360, 70, 'okDK72a')
    seritler = [('mavi', 8, [('Bütün melekler hemen eğildi', True), ('Emre karşı gelmediler', False),
                             ('Sonuç: itaat', True)]),
                ('turuncu', 248, [('İblis eğilmekten kaçındı', True), ('“Ben ateşten, o çamurdan” dedi', False),
                                  ('Sonuç: kibir, isyan, kovulma', True)])]
    for renk, x, kutular in seritler:
        for n, (metin, kalin) in enumerate(kutular):
            y = 76 + n * 48
            ic += _kutu(x, y, 224, 34, renk, rx=8) + _yazi(x + 112, y + 22, metin, 12.5, RENK[renk][2], kalin=kalin)
            if n < len(kutular) - 1:
                ic += _ok(x + 112, y + 36, x + 112, y + 46, 'okDK72a')
    ic += _yazi(240, 238, 'İblis yaratıldığı maddeyi üstünlük sebebi saydı;', 12.5, 'g-y')
    ic += _yazi(240, 256, 'kovulunca inananlara kıyamete kadar düşman oldu.', 12.5, 'g-y')
    return svg(480, 268, ic, 'Hz. Âdem için saygıyla eğilme emrine iki tutum: bütün melekler hemen eğildi, emre karşı gelmedi; '
               'sonuç itaattir. İblis eğilmekten kaçındı, kendisinin ateşten, Âdem’in çamurdan yaratıldığını söyledi; sonuç kibir, '
               'isyan ve cennetten kovulmadır. İblis kovulunca inananlara kıyamete kadar düşman oldu.')


def ipucu_tablosu():
    """Kitap s. 20 (3. Etkinlik) ve s. 19 (Bilgi Görseli 1.2): ayet ve hadislerdeki ipucundan meleğin adı ve görevi."""
    ic = ''
    basliklar = [('mor', 8, 86, 'Kaynak'), ('gri', 98, 128, 'İpucu'), ('mavi', 230, 126, 'Melek'),
                 ('yesil', 360, 112, 'Görev')]
    for renk, x, w, ad in basliklar:
        if renk == 'gri':
            ic += _gri(x, 8, w, 28, rx=6) + _yazi(x + w / 2, 27, ad, 12.5, 'g-y', kalin=True)
        else:
            ic += _kutu(x, 8, w, 28, renk, rx=6) + _yazi(x + w / 2, 27, ad, 12.5, RENK[renk][2], kalin=True)
    satirlar = [(['Kaf 17-18'], ['sağda ve solda', 'kaydeden iki melek'], 'Kiramen Kâtibin', ['söz ve davranışı', 'kaydetme']),
                (['Zümer 68'], ['sûra iki kez', 'üflenmesi'], 'İsrafil', ['kıyamet ve', 'diriliş için sûr']),
                (['Nahl 102'], ['Kur’an’ı indiren', 'Ruhulkudüs'], 'Cebrail', ['vahyi bildirme']),
                (['Secde 11'], ['canınızı alacak', 'ölüm meleği'], 'Azrail', ['can alma']),
                (['Buhari,', 'Cenâiz 86'], ['kabre konulan', 'müminin sorgusu'], 'Münker ve Nekir', ['sorguya çekme']),
                (['İbni Ebu', 'Şeybe'], ['yağmur ve bitki', 'ona emanet'], 'Mikâil', ['rızık ve tabiat', 'olayları'])]
    for n, (kaynak, ipucu, melek, gorev) in enumerate(satirlar):
        y = 42 + n * 44
        ic += _kutu(8, y, 86, 38, 'mor', rx=6) + _satirlar(51, y + 19, kaynak, 12, 'g-of')
        ic += _gri(98, y, 128, 38, rx=6) + _satirlar(162, y + 19, ipucu, 12, 'g-y')
        ic += _kutu(230, y, 126, 38, 'mavi', rx=6) + _yazi(293, y + 23, melek, 12, 'g-mf', kalin=True)
        ic += _kutu(360, y, 112, 38, 'yesil', rx=6) + _satirlar(416, y + 19, gorev, 12, 'g-yf')
    return svg(480, 42 + 6 * 44 + 4, ic, 'İpucundan meleğe: Kaf 17-18 sağda ve solda kaydeden iki melek, Kiramen Kâtibin, kaydetme; '
               'Zümer 68 sûra iki kez üflenmesi, İsrafil; Nahl 102 Kur’an’ı indiren Ruhulkudüs, Cebrail, vahiy; Secde 11 ölüm '
               'meleği, Azrail, can alma; Buhari kabirde sorgu, Münker ve Nekir; İbni Ebu Şeybe yağmur ve bitki, Mikâil, '
               'rızık ve tabiat olayları.')


def zaman():
    """Kitap s. 19-20: dört büyük melek ve öteki melekler, görevin yapıldığı zamana göre gruplanır."""
    ic = '<defs>' + ok_isareti('okDK72b', 'g-s') + '</defs>'
    ic += _yazi(240, 18, 'Görevin zamanına göre gruplama', 12.5, 'g-s', kalin=True)
    satirlar = [(['Dünya hayatı'], [('Cebrail', 'vahiy', 'mavi', 100), ('Mikâil', 'tabiat olayları', 'mavi', 112),
                                    ('Kiramen Kâtibin', 'kayıt tutma', 'mor', 128)]),
                (['Ölüm anı'], [('Azrail', 'can alma', 'mavi', 100)]),
                (['Kabir'], [('Münker ve Nekir', 'sorguya çekme', 'mor', 128)]),
                (['Kıyamet ve', 'diriliş'], [('İsrafil', 'iki kez sûr', 'mavi', 100)])]
    for n, (zaman_adi, melekler) in enumerate(satirlar):
        y = 30 + n * 58
        ic += _gri(8, y, 108, 44, rx=8) + _satirlar(62, y + 22, zaman_adi, 12.5, 'g-y', kalin=True)
        if n < len(satirlar) - 1:
            ic += _ok(62, y + 46, 62, y + 56, 'okDK72b')
        x = 128
        for ad, gorev, renk, w in melekler:
            ic += _kutu(x, y, w, 44, renk, rx=8)
            ic += _yazi(x + w / 2, y + 19, ad, 12.5, RENK[renk][2], kalin=True) + _yazi(x + w / 2, y + 36, gorev, 12, RENK[renk][2])
            x += w + 8
    y = 30 + 4 * 58
    ic += _kutu(40, y + 4, 22, 16, 'mavi', rx=4) + _yazi(70, y + 17, 'dört büyük melek', 12, 'g-y', hiza='start')
    ic += _kutu(250, y + 4, 22, 16, 'mor', rx=4) + _yazi(280, y + 17, 'öteki melekler', 12, 'g-y', hiza='start')
    return svg(480, y + 28, ic, 'Görevin zamanına göre melekler: dünya hayatında Cebrail vahiy, Mikâil tabiat olayları, Kiramen Kâtibin '
               'kayıt; ölüm anında Azrail can alma; kabirde Münker ve Nekir sorgu; kıyamet ve dirilişte İsrafil iki kez sûra üfleme. '
               'Mavi dört büyük meleği, mor öteki melekleri gösterir.')


def uygula(o):
    g = {'Melek, cin ve insanı karşılaştırma': karsilastirma(),
         'Emre karşı iki tutum: melekler ve İblis': kissa(),
         'Ayetten meleğin adını ve görevini bulma': ipucu_tablosu(),
         'Melekleri görevin zamanına göre gruplama': zaman()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
