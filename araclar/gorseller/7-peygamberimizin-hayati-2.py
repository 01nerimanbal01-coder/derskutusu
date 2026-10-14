"""7. sınıf Peygamberimizin Hayatı, 2. hafta: tepkilerin sertleşmesi, Ebu Talib'e iki heyet, boykot, Hüzün Yılı.

Görseller yalnız MEB 7. sınıf Peygamberimizin Hayatı ders kitabındaki bilgilerle çizilir (kitap s. 19-22).
Renk anlamı: mavi = Hz. Muhammed'e yönelik / kişiler, turuncu = Müslümanlara yönelik / boykot, yeşil = sonuç.
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


def tepki_asamalari():
    """Tepkilerin sırası (s. 19): ikna → iftira, hakaret, eziyet → baskı ve zulüm → boykot."""
    ic = _yazi(236, 20, 'Müşriklerin tepkileri adım adım sertleşti', 13, kalin=True, hiza='middle')
    satir = [('mavi', 'İkna', 'Amaç: Hz. Muhammed’i davasından vazgeçirmek'),
             ('mavi', 'İftira, hakaret, eziyet', 'Amaç: Hz. Muhammed’i itibarsızlaştırmak'),
             ('turuncu', 'Baskı ve zulüm', 'Amaç: Müslümanları inançlarından döndürmek'),
             ('turuncu', 'Boykot', 'Konuşma, evlilik, ticaret ve yardım yasağı')]
    for k, (renk, ad, aciklama) in enumerate(satir):
        x, y = 8 + k * 18, 30 + k * 54
        yazi = RENK[renk][2]
        ic += _kutu(x, y, 456 - k * 18, 48, renk)
        ic += f'<circle cx="{x + 24}" cy="{y + 24}" r="13" class="g-z"/>'
        ic += _yazi(x + 24, y + 29, str(k + 1), 13, yazi, kalin=True, hiza='middle')
        ic += _yazi(x + 48, y + 21, ad, 13, yazi, kalin=True)
        ic += _yazi(x + 48, y + 39, aciklama, 12)
    ic += _kutu(8, 250, 456, 34, 'yesil', rx=10)
    ic += _yazi(236, 272, 'Sonuç: Davet sürdü, İslam yayılmaya devam etti', 13, 'g-yf', kalin=True, hiza='middle')
    ic += '<rect x="8" y="292" width="456" height="28" rx="8" class="g-z"/>'
    ic += _yazi(236, 311, 'Mavi: Hz. Muhammed’e yönelik  ·  Turuncu: Müslümanlara yönelik', 12, kalin=True, hiza='middle')
    return svg(472, 328, ic, 'Müşriklerin tepkileri adım adım sertleşti. 1. İkna: Hz. Muhammed’i davasından vazgeçirmek. '
               '2. İftira, hakaret ve eziyet: Hz. Muhammed’i itibarsızlaştırmak. 3. Baskı ve zulüm: Müslümanları '
               'inançlarından döndürmek. 4. Boykot: konuşma, evlilik, ticaret ve yardım yasağı. '
               'Sonuç: davet sürdü, İslam yayılmaya devam etti.')


def iki_heyet():
    """Okuyalım (s. 22): Ebu Talib'e iki ziyaret, istek ve dil değişir; sonunda kararlılık ve söz."""
    ic = '<defs>' + ok_isareti('okPH72a', 'g-s') + '</defs>'
    sutun = [(8, 'mavi', '1. ziyaret', 'Ya yeğenini vazgeçir', 'ya korumayı bırak', 'Dil: yakınma, iki seçenek',
              'Yumuşak sözle geri gönderir'),
             (248, 'turuncu', '2. ziyaret', 'Ya onu uzaklaştır', 'ya onunla savaşırız', 'Dil: açık tehdit',
              'Yeğenine anlatır')]
    for x, renk, ad, istek1, istek2, dil, cevap in sutun:
        yazi = RENK[renk][2]
        orta = x + 108
        ic += _kutu(x, 8, 216, 136, renk)
        ic += _yazi(orta, 32, ad, 13.5, yazi, kalin=True, hiza='middle')
        ic += _yazi(orta, 56, 'Heyetin isteği', 12, 'g-s', kalin=True, hiza='middle')
        ic += _yazi(orta, 78, istek1, 13, kalin=True, hiza='middle')
        ic += _yazi(orta, 98, istek2, 13, kalin=True, hiza='middle')
        ic += _yazi(orta, 126, dil, 12, hiza='middle')
        ic += _gri(x, 152, 216, 56)
        ic += _yazi(orta, 174, 'Ebu Talib', 12, 'g-s', kalin=True, hiza='middle')
        ic += _yazi(orta, 196, cevap, 12.5, kalin=True, hiza='middle')
    ic += '<line x1="226" y1="76" x2="244" y2="76" class="g-c" stroke-width="2" marker-end="url(#okPH72a)"/>'
    ic += '<line x1="356" y1="210" x2="356" y2="228" class="g-c" stroke-width="2" marker-end="url(#okPH72a)"/>'
    ic += _kutu(8, 234, 456, 58, 'yesil')
    ic += _yazi(236, 258, 'Hz. Muhammed görevini bırakmayacağına yemin eder.', 12.5, 'g-yf', kalin=True, hiza='middle')
    ic += _yazi(236, 280, 'Ebu Talib onu hiçbir zaman terk etmeyeceğine söz verir.', 12.5, hiza='middle')
    return svg(472, 300, ic, 'Ebu Talib’e iki ziyaret. Birinci ziyaret: heyet ya yeğenini vazgeçir ya korumayı bırak der; '
               'dil yakınma, iki seçenek sunulur; Ebu Talib onları yumuşak sözle geri gönderir. İkinci ziyaret: '
               'ya onu uzaklaştır ya onunla savaşırız derler; dil açık tehdittir; Ebu Talib durumu yeğenine anlatır. '
               'Sonunda Hz. Muhammed görevini bırakmayacağına yemin eder, Ebu Talib onu hiçbir zaman terk etmeyeceğine söz verir.')


def boykot_karti():
    """Boykot (s. 19): dört yasak ve boykotun yeri, başlangıcı, süresi, bitişi."""
    ic = _yazi(236, 20, 'Boykot kararı: dört yasak', 13, kalin=True, hiza='middle')
    for k, ad in enumerate(['konuşma yok', 'evlilik yok', 'ticaret yok', 'yardım yok']):
        x = 8 + k * 116
        ic += _kutu(x, 30, 108, 40, 'turuncu', rx=10)
        ic += _yazi(x + 54, 55, ad, 12.5, 'g-tf', kalin=True, hiza='middle')
    hucre = [(8, 82, 'Yer', 'Ebu Talib Mahallesi'), (240, 82, 'Başlangıç', '616 yılı'),
             (8, 140, 'Süre', 'Üç yıl'), (240, 140, 'Bitiş', 'Bazı Mekkelilerin çabası')]
    for x, y, etiket, deger in hucre:
        ic += _gri(x, y, 224, 50)
        ic += _yazi(x + 14, y + 20, etiket, 12, 'g-s', kalin=True)
        ic += _yazi(x + 14, y + 40, deger, 13, kalin=True)
    return svg(472, 198, ic, 'Boykot kararı, dört yasak: Müslümanlarla konuşulmayacak, evlenilmeyecek, ticaret yapılmayacak, '
               'yardım edilmeyecek. Yer: Ebu Talib Mahallesi. Başlangıç: 616 yılı. Süre: üç yıl. '
               'Bitiş: bazı Mekkelilerin çabası.')


def huzun_seridi():
    """Boykottan Hüzün Yılı'na (s. 19): 616 başlangıç, üç yıl sonra bitiş, 620 iki vefat."""
    ic = _yazi(146, 32, 'Boykot (üç yıl)', 12.5, 'g-tf', kalin=True, hiza='middle')
    ic += '<line x1="20" y1="50" x2="452" y2="50" class="g-c" stroke-width="2"/>'
    ic += '<rect x="56" y="44" width="180" height="12" rx="6" class="g-ta"/>'
    ic += '<rect x="56" y="44" width="180" height="12" rx="6" class="g-ts" stroke-width="1.5"/>'
    for cx, renk, ust, alt in ((56, 'turuncu', '616', 'boykot başlar'), (236, 'turuncu', 'üç yıl sonra', 'boykot biter'),
                               (416, 'mavi', '620', 'Hüzün Yılı')):
        a, s, yazi = RENK[renk]
        ic += f'<circle cx="{cx}" cy="50" r="8" class="{a}"/><circle cx="{cx}" cy="50" r="8" class="{s}" fill="none" stroke-width="2"/>'
        ic += _yazi(cx, 76, ust, 13, yazi, kalin=True, hiza='middle')
        ic += _yazi(cx, 94, alt, 12, hiza='middle')
    kart = [(8, 'Hz. Hatice', 'Peygamberimizin eşi', 'Cömert, ahlaklı, akıllı', 'Merhametli · Tahira'),
            (240, 'Ebu Talib', 'Peygamberimizin amcası', 'Haşimoğulları’nın reisi', 'Yeğenini sonuna kadar korudu')]
    for x, ad, s1, s2, s3 in kart:
        ic += _kutu(x, 108, 224, 112, 'mavi')
        ic += _yazi(x + 112, 132, ad, 13.5, 'g-mf', kalin=True, hiza='middle')
        ic += _yazi(x + 112, 156, s1, 12.5, hiza='middle')
        ic += _yazi(x + 112, 178, s2, 12.5, hiza='middle')
        ic += _yazi(x + 112, 200, s3, 12.5, hiza='middle')
    ic += '<rect x="8" y="228" width="456" height="30" rx="8" class="g-z"/>'
    ic += _yazi(236, 248, '620: art arda iki kayıp, peygamberliğin onuncu yılı Hüzün Yılı', 12.5, kalin=True, hiza='middle')
    return svg(472, 266, ic, 'Zaman şeridi: 616 yılında boykot başlar, üç yıl sonra biter. 620 yılı Hüzün Yılı. '
               'O yıl Peygamberimizin eşi Hz. Hatice ile amcası Ebu Talib vefat etti. Hz. Hatice: cömert, ahlaklı, akıllı, '
               'merhametli, Tahira. Ebu Talib: Haşimoğulları’nın reisi, yeğenini sonuna kadar korudu. '
               '620, peygamberliğin onuncu yılı, Hüzün Yılı.')


def uygula(o):
    g = {'Tepkiler adım adım sertleşti': tepki_asamalari(),
         'Ebu Talib’e giden iki heyet': iki_heyet(),
         'Boykot yılları': boykot_karti(),
         'Hüzün Yılı: art arda iki kayıp': huzun_seridi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
