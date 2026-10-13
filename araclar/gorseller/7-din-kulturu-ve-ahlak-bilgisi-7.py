"""7. sınıf Din Kültürü ve Ahlak Bilgisi, 7. hafta: Bir Sure Öğreniyorum: Nâs Suresi (Melek ve Ahiret İnancı ünitesi).

Görseller yalnız özet metnindeki (araclar/ozetler/7-din-kulturu-ve-ahlak-bilgisi-7.json) bilgilerle çizilir;
ders kitabı sayfası kullanılmamıştır.
Renk anlamı: birinci görselde mavi = Allah’ın surede anılan üç niteliği (kime sığınılır), yeşil = tek sığınak olan Allah;
ikinci görselde turuncu = vesvese, vesveseci ve gaflet (neyden sığınılır), yeşil = Allah’ı anmak ve korunma;
üçüncü görselde mor = ünitenin kavramları (gayb, melek, ahiret), mavi = Nâs suresi ve öğrettiği sığınma;
dördüncü görselde mavi = ibadet içinde okuma, mor = Hz. Peygamber’in uygulaması, yeşil = günümüzde Müslümanların okuduğu anlar.
Çizimlerde ölçü yoktur (ölçeksiz); kutu boyutları ve ok uzunlukları yalnız ilişkiyi gösterir.
Dinî sembol, hat yazısı ve Arapça harf çizilmemiştir; yalnız kutu, ok ve Türkçe yazı kullanılır.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı/koyu dolgu)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _koyu_kutu(x, y, w, h, renk, rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{RENK[renk][2]}"/>'


def _yazi(x, y, metin, boyut=12.5, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, kimlik):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="2" marker-end="url(#{kimlik})"/>'


def kime_siginilir():
    """İlk üç ayet: insanların Rabbi, Meliki ve İlahı; üç nitelik tek sığınakta (Allah) birleşir."""
    ic = '<defs>' + ok_isareti('okDK77a', 'g-s') + '</defs>'
    ic += _yazi(240, 22, 'Kime sığınılır? Üç nitelik, tek sığınak', 15, True)
    nitelik = [('1. ayet: insanların', 'Rabbine', 'yaratan ve', 'yetiştiren'),
               ('2. ayet: insanların', 'Melikine', 'yöneten ve', 'hükmeden'),
               ('3. ayet: insanların', 'İlahına', 'ibadet edilen', 'tek varlık')]
    for k, (etiket, ad, s1, s2) in enumerate(nitelik):
        x = 8 + k * 156
        cx = x + 75
        ic += _kutu(x, 40, 150, 96, 'mavi')
        ic += _yazi(cx, 58, etiket, 12, False, 'g-s')
        ic += _yazi(cx, 84, ad, 17, True, 'g-mf')
        ic += _yazi(cx, 106, s1) + _yazi(cx, 124, s2)
    for x1, x2 in ((83, 196), (240, 240), (397, 284)):
        ic += _ok(x1, 142, x2, 186, 'okDK77a')
    ic += _koyu_kutu(120, 190, 240, 42, 'yesil') + _yazi(240, 217, 'Tek sığınak: Allah', 16, True, 'g-b')
    ic += _yazi(240, 258, 'Üç ayrı güç değil, üç yönüyle tanıtılan tek Allah', 12.5, True)
    return svg(480, 270, ic, 'Nâs suresinin ilk üç ayetinde kime sığınıldığını gösteren şema: birinci ayette insanların Rabbine '
               '(yaratan ve yetiştiren), ikinci ayette insanların Melikine (yöneten ve hükmeden), üçüncü ayette insanların İlahına '
               '(ibadet edilen tek varlık) sığınılır. Üç kutudan çıkan oklar tek bir kutuda birleşir: tek sığınak Allah’tır; '
               'üç ayrı güç değil, üç yönüyle tanıtılan tek Allah.')


def neyden_siginilir():
    """Son üç ayet: neyden, nereye, kimlerden; altta hannâsın çalışma biçimi (Allah anılınca geri çekilir, gaflette yaklaşır)."""
    ic = '<defs>' + ok_isareti('okDK77b', 'g-s') + '</defs>'
    ic += _yazi(240, 22, 'Neyden sığınılır? Son üç ayet', 15, True)
    ayet = [('4. ayet', 'Neyden?', 'sinsi vesvesecinin', 'şerrinden'),
            ('5. ayet', 'Nereye fısıldar?', 'insanların', 'kalplerine'),
            ('6. ayet', 'Kimlerden?', 'cinlerden ve', 'insanlardan')]
    for k, (etiket, soru, s1, s2) in enumerate(ayet):
        x = 8 + k * 156
        cx = x + 75
        ic += _kutu(x, 36, 150, 84, 'turuncu')
        ic += _yazi(cx, 54, etiket, 12, False, 'g-s')
        ic += _yazi(cx, 74, soru, 14, True, 'g-tf')
        ic += _yazi(cx, 94, s1) + _yazi(cx, 110, s2)
    ic += _yazi(240, 148, 'Hannâs, yani sinsi vesveseci nasıl çalışır?', 13.5, True)
    satirlar = [(162, 'yesil', 'Allah anılır', 'vesveseci geri çekilir'),
                (214, 'turuncu', 'Gaflet: Allah unutulur', 'yeniden yaklaşır ve fısıldar')]
    for y, renk, sol, sag in satirlar:
        ic += _koyu_kutu(8, y, 184, 40, renk) + _yazi(100, y + 25, sol, 13.5, True, 'g-b')
        ic += _ok(200, y + 20, 224, y + 20, 'okDK77b')
        ic += _kutu(230, y, 242, 40, renk) + _yazi(351, y + 25, sag, 12.5, True)
    ic += _yazi(240, 276, 'Korunma yolu: Allah’ı anmak, O’na sığınmak,', 12.5, True)
    ic += _yazi(240, 294, 'kötü düşünceyi büyütmeden kovmak.', 12.5, True)
    return svg(480, 304, ic, 'Son üç ayette neyden sığınıldığını gösteren kutular: dördüncü ayet sinsi vesvesecinin şerrinden '
               'sığınıldığını, beşinci ayet vesvesenin insanların kalplerine fısıldandığını, altıncı ayet vesvesecinin cinlerden ve '
               'insanlardan olabileceğini söyler. Altta hannâsın çalışma biçimi: Allah anılınca vesveseci geri çekilir; gaflete düşülüp '
               'Allah unutulunca yeniden yaklaşır ve fısıldar. Korunma yolu Allah’ı anmak, O’na sığınmak ve kötü düşünceyi '
               'büyütmeden kovmaktır.')


def unite_bagi():
    """Gayb, melek ve ahiret kavramlarından Nâs suresine giden oklar: sure, fısıltıdan Allah’a sığınmayı öğretir."""
    ic = '<defs>' + ok_isareti('okDK77c', 'g-s') + '</defs>'
    ic += _yazi(240, 22, 'Sure, ünitenin üç kavramına bağlanır', 15, True)
    kavram = [('Gayb', 'cinler ve şeytan görünmezdir;', 'ayet ve hadislerle bilinir'),
              ('Melek', 'iyiliğe çağırır ve kaydeder;', 'vesveseci ise kötülüğe çağırır'),
              ('Ahiret', 'her davranış karşılık bulur;', '“Kimse görmez.” fısıltısına cevap')]
    for k, (ad, s1, s2) in enumerate(kavram):
        y = 40 + k * 64
        ic += _kutu(8, y, 96, 44, 'mor') + _yazi(56, y + 27, ad, 14, True, 'g-of')
        ic += _yazi(112, y + 18, s1, 12.5, False, 'g-y', 'start') + _yazi(112, y + 34, s2, 12.5, False, 'g-y', 'start')
        ic += _ok(314, y + 22, 332, y + 22, 'okDK77c')
    ic += _kutu(340, 40, 132, 172, 'mavi')
    ic += _yazi(406, 78, 'Nâs suresi', 14.5, True, 'g-mf')
    for k, s in enumerate(['kötülüğe çağıran', 'fısıltıdan Allah’a', 'sığınmayı öğretir']):
        ic += _yazi(406, 104 + k * 17, s)
    ic += _yazi(406, 170, '114. ve son sure,', 12, False, 'g-s') + _yazi(406, 186, 'ünitenin son konusu', 12, False, 'g-s')
    ic += _yazi(240, 240, 'Seçim insanın; Allah’a sığınan yalnız kalmaz.', 12.5, True)
    return svg(480, 252, ic, 'Nâs suresinin ünitenin üç kavramıyla bağını gösteren şema: gayb (cinler ve şeytan görünmezdir, ayet ve '
               'hadislerle bilinir), melek (iyiliğe çağırır ve kaydeder, vesveseci ise kötülüğe çağırır) ve ahiret (her davranış '
               'karşılık bulur, “Kimse görmez.” fısıltısına cevap) kutularından oklar Nâs suresi kutusuna gider: sure, kötülüğe çağıran '
               'fısıltıdan Allah’a sığınmayı öğretir; Kur’an’ın 114. ve son suresi, ünitenin son konusudur. Seçim insanındır; '
               'Allah’a sığınan yalnız kalmaz.')


def ne_zaman_okunur():
    """Surenin okunduğu anlar üç kümede: ibadette, Hz. Peygamber’in uygulamasında, günümüzde Müslümanların hayatında."""
    def oge(x, y, renk, s1, s2):
        return _kutu(x, y, 160, 44, renk) + _yazi(x + 80, y + 18, s1) + _yazi(x + 80, y + 34, s2)

    ic = _koyu_kutu(8, 10, 130, 44, 'mavi') + _yazi(73, 37, 'İbadette', 13.5, True, 'g-b')
    ic += oge(146, 10, 'mavi', 'Namazda, Fatiha', 'suresinden sonra')
    ic += oge(312, 10, 'mavi', 'Hatimde, Kur’an’ın', 'son suresi olarak')
    ic += _koyu_kutu(8, 64, 130, 44, 'mor')
    ic += _yazi(73, 83, 'Hz. Peygamber’in', 12.5, True, 'g-b') + _yazi(73, 99, 'uygulaması', 12.5, True, 'g-b')
    ic += oge(146, 64, 'mor', 'Her gece yatmadan önce', '(İhlas, Felak, Nâs)')
    ic += oge(312, 64, 'mor', 'Hastalandığında', 'Allah’a sığınarak')
    ic += _koyu_kutu(8, 118, 130, 98, 'yesil')
    ic += _yazi(73, 162, 'Günümüzde', 13.5, True, 'g-b') + _yazi(73, 180, 'Müslümanlar', 13.5, True, 'g-b')
    ic += oge(146, 118, 'yesil', 'Sabah ve akşam', 'dualarında')
    ic += oge(312, 118, 'yesil', 'Korku ve kaygı', 'anlarında')
    ic += oge(146, 172, 'yesil', 'Çocuklara dua', 'ederken')
    ic += oge(312, 172, 'yesil', 'Kötü bir düşünceden', 'kurtulmak isteyince')
    ic += _yazi(240, 244, '“Kendi gücümle değil, Allah’a sığınarak güvendeyim.”', 12.5, True)
    return svg(480, 256, ic, 'Nâs suresinin okunduğu zamanları gösteren kutular. İbadette: namazda Fatiha suresinden sonra ve hatimde '
               'Kur’an’ın son suresi olarak. Hz. Peygamber’in uygulaması: her gece yatmadan önce İhlas, Felak ve Nâs sureleriyle '
               'birlikte ve hastalandığında Allah’a sığınarak. Günümüzde Müslümanlar: sabah ve akşam dualarında, korku ve kaygı '
               'anlarında, çocuklara dua ederken ve kötü bir düşünceden kurtulmak isteyince. Sureyi okumak “Kendi gücümle değil, '
               'Allah’a sığınarak güvendeyim.” demektir.')


def uygula(o):
    g = {'Kime sığınıyoruz? Rab, Melik ve İlah': kime_siginilir(),
         'Neyden sığınıyoruz? Sinsi vesveseci': neyden_siginilir(),
         'Sure ile ünitenin bağı: gayb, melek ve ahiret': unite_bagi(),
         'Nâs suresi ne zaman okunur?': ne_zaman_okunur()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
