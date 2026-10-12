"""8. sınıf Din Kültürü ve Ahlak Bilgisi, 4. hafta: kaderle ilgili kavramlar (ömür ve ecel, rızık, tevekkül, başarı, sağlık).

Görseller yalnız MEB 8. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap s. 21, 24-25, 28).
Renk anlamı: birinci görselde mavi = ömür (kumların tamamı), turuncu = ecel (son kum tanesi); ikinci görselde mavi = tevekkülün
adımları, yeşil = doğru tevekkül, turuncu = tevekkülle bağdaşmayan davranış; üçüncü görselde yeşil = hastalanmadan önce alınacak önlemler ve
hastalanınca yapılacaklar.
Çizimlerde ölçü yoktur; kum miktarı ve kutu boyutları süre ya da büyüklük göstermez, yalnız ilişkiyi gösterir.
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


def _zemin(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boyut=12, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def kum_saati():
    """Kum saatindeki kumların tamamı ömre, son kum tanesinin düştüğü an ecele benzetilir (kitap s. 21)."""
    ic = '<rect x="50" y="10" width="100" height="10" rx="4" class="g-ma"/><rect x="50" y="10" width="100" height="10" rx="4" class="g-ms" stroke-width="2"/>'
    ic += '<rect x="50" y="210" width="100" height="10" rx="4" class="g-ma"/><rect x="50" y="210" width="100" height="10" rx="4" class="g-ms" stroke-width="2"/>'
    ic += ('<path d="M58 20 L142 20 C142 64 106 90 104 115 C106 140 142 166 142 210 L58 210 C58 166 94 140 96 115 C94 90 58 64 58 20 Z" class="g-z"/>'
           '<path d="M58 20 L142 20 C142 64 106 90 104 115 C106 140 142 166 142 210 L58 210 C58 166 94 140 96 115 C94 90 58 64 58 20 Z" class="g-c" stroke-width="2.5" stroke-linejoin="round"/>')
    ic += '<path d="M64 208 L136 208 C132 190 118 170 100 158 C82 170 68 190 64 208 Z" class="g-mf"/>'
    ic += '<circle cx="100" cy="128" r="3.5" class="g-tf"/>'
    # açıklama: ömür
    ic += '<rect x="188" y="34" width="20" height="20" rx="4" class="g-mf"/>' + _yazi(218, 51, 'Ömür', 15, True, 'g-mf', 'start')
    ic += _yazi(188, 76, 'kumların tamamı:', 12.5, False, 'g-y', 'start') + _yazi(188, 94, 'doğumdan ölüme kadar', 12.5, False, 'g-y', 'start') + _yazi(188, 112, 'geçen süre', 12.5, False, 'g-y', 'start')
    # açıklama: ecel
    ic += '<circle cx="198" cy="150" r="9" class="g-tf"/>' + _yazi(218, 156, 'Ecel', 15, True, 'g-tf', 'start')
    ic += _yazi(188, 178, 'son kum tanesinin', 12.5, False, 'g-y', 'start') + _yazi(188, 196, 'düştüğü an:', 12.5, False, 'g-y', 'start') + _yazi(188, 214, 'ömrün bittiği an', 12.5, False, 'g-y', 'start')
    return svg(480, 230, ic, 'Kum saati: kumların tamamı ömrü, yani doğumdan ölüme kadar geçen süreyi gösterir; son kum tanesinin düştüğü an eceli, yani ömrün bittiği anı gösterir.')


def tevekkul_tablosu():
    """Tevekkülün adımları ve doğru tevekkül ile tevekkülle bağdaşmayan davranışlar (kitap s. 24)."""
    ic = '<defs>' + ok_isareti('okDK84a', 'g-s') + '</defs>'
    adimlar = [(6, '1. Görevini yap', 'önlemini al'), (169, '2. Allah’a güven', 'dua et'), (332, '3. Sonucu bekle', 'sonuç Allah’tan')]
    for x, baslik, alt in adimlar:
        ic += _kutu(x, 6, 142, 52, 'mavi') + _yazi(x + 71, 29, baslik, 12, True, 'g-mf') + _yazi(x + 71, 47, alt, 11.5)
    for x1, x2 in ((151, 166), (314, 329)):
        ic += f'<line x1="{x1}" y1="32" x2="{x2}" y2="32" class="g-c" stroke-width="2" marker-end="url(#okDK84a)"/>'
    ic += _kutu(78, 74, 192, 26, 'yesil', 13) + _yazi(174, 92, 'Doğru tevekkül', 13, True, 'g-yf')
    ic += _kutu(278, 74, 194, 26, 'turuncu', 13) + _yazi(375, 92, 'Tevekkülle bağdaşmaz', 13, True, 'g-tf')
    satirlar = [
        ('Öğrenci', ('Derslerine çalışır,', 'başarı için dua eder'), ('Dersine çalışmadan', 'başarı ister')),
        ('Çiftçi', ('Tohumu eker, gereğini', 'yapar, ürün bekler'), ('Gereğini yapmadan', 'bol ürün bekler')),
        ('Şoför', ('Aracını bakıma götürür,', 'sonra yola çıkar'), ('Bakımsız araçla', 'yola çıkar')),
    ]
    for i, (ad, sol, sag) in enumerate(satirlar):
        y = 108 + i * 56
        ic += _zemin(6, y, 66, 50) + _yazi(39, y + 29, ad, 12, True)
        ic += _kutu(78, y, 192, 50, 'yesil', 10) + _yazi(90, y + 21, sol[0], 11.5, False, 'g-y', 'start') + _yazi(90, y + 39, sol[1], 11.5, False, 'g-y', 'start')
        ic += _kutu(278, y, 194, 50, 'turuncu', 10) + _yazi(290, y + 21, sag[0], 11.5, False, 'g-y', 'start') + _yazi(290, y + 39, sag[1], 11.5, False, 'g-y', 'start')
    return svg(480, 280, ic, 'Tevekkülün adımları: önce görevini yap ve önlemini al, sonra Allah’a güven ve dua et, sonucu Allah’tan bekle. '
               'Doğru tevekkül: öğrenci derslerine çalışıp dua eder, çiftçi tohumu ekip gereğini yapar ve ürün bekler, şoför aracını bakıma götürüp yola çıkar. '
               'Tevekkülle bağdaşmayan davranış: öğrenci çalışmadan başarı ister, çiftçi gereğini yapmadan ürün bekler, şoför bakımsız araçla yola çıkar.')


def saglik_onlem_tedavi():
    """Hastalanmadan önce önlem almak, hastalanınca tedavi olmak ve dua etmek (kitap s. 28)."""
    ic = '<defs>' + ok_isareti('okDK84b', 'g-s') + '</defs>'
    ic += _kutu(6, 8, 250, 146, 'yesil') + _yazi(22, 33, 'Hastalanmadan önce', 13.5, True, 'g-yf', 'start')
    for i, satir in enumerate(('Yediğine ve içtiğine dikkat et', 'Yaşadığın ortama dikkat et', 'Yeterli uyku, dinlenme, hareket', 'Helal ve temiz olanı seç')):
        y = 62 + i * 24
        ic += f'<circle cx="28" cy="{y - 4}" r="3" class="g-yf"/>' + _yazi(40, y, satir, 11.5, False, 'g-y', 'start')
    ic += '<line x1="260" y1="81" x2="282" y2="81" class="g-c" stroke-width="2" marker-end="url(#okDK84b)"/>'
    ic += _kutu(286, 8, 188, 146, 'yesil') + _yazi(302, 33, 'Hastalanınca', 13.5, True, 'g-yf', 'start')
    for i, satir in enumerate(('Tedavi ol', 'Allah’a dua et', 'İyileşme yollarını ara', 'Sorumluluktan kaçma')):
        y = 62 + i * 24
        ic += f'<circle cx="308" cy="{y - 4}" r="3" class="g-yf"/>' + _yazi(320, y, satir, 11, False, 'g-y', 'start')
    ic += _yazi(240, 182, 'Önlem almak ve tedavi olmak insanın sorumluluğudur.', 12.5, True)
    return svg(480, 194, ic, 'Hastalanmadan önce yediğine, içtiğine ve yaşadığın ortama dikkat et, yeterli uyku, dinlenme ve hareketle helal ve temiz olanı seç. '
               'Hastalanınca tedavi ol, Allah’a dua et, iyileşme yollarını ara ve sorumluluktan kaçma. Önlem almak ve tedavi olmak insanın sorumluluğudur.')


def uygula(o):
    g = {'Ömür ve ecel': kum_saati(),
         'Tevekkül': tevekkul_tablosu(),
         'Sağlık ve hastalık': saglik_onlem_tedavi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
