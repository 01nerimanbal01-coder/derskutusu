"""5. sınıf Sosyal Bilgiler, 3. hafta: kültürel özelliklere saygı ve birlikte yaşama kültürü.

Görseller yalnız MEB 5. sınıf Sosyal Bilgiler ders kitabındaki bilgilerle çizilir (kitap s. 22-23, 25-28, 33).
Renk anlamı: ülke kültürü kartlarında mavi = Bulgaristan'dan katılan çocuğun anlattıkları;
Türkiye-KKTC tablosunda yeşil = iki yerde de görülen özellik; bir araya gelme durumlarında
mavi = turizm, turuncu = eğitim, yeşil = iş için göç, mor = uyum projesi;
selamlaşma tablosunda turuncu = Türk ve Japon kültürlerinde ortak biçim, mavi = diğer biçimler.
"""
from ozet_gorsel import svg

RENK = {  # (dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _kart(x, y, w, h, renk, baslik, satirlar, ilk=44, aralik=16):
    ic = _kutu(x, y, w, h, renk)
    ic += f'<text x="{x + 12}" y="{y + 24}" font-size="13.5" font-weight="800" class="{RENK[renk][2]}">{baslik}</text>'
    for k, t in enumerate(satirlar):
        ic += f'<text x="{x + 12}" y="{y + ilk + k * aralik}" font-size="12" class="g-y">{t}</text>'
    return ic


def ulke_basliklari():
    """Bulgaristan'dan katılan çocuğun anlattıkları, altı başlıkta (kitap s. 22, 26)."""
    kart = [('Sanat', ('Kalaycılık: bakır kapların', 'üzerine özel kaplama yapılır')),
            ('Müzik', ('Kaval, zurna ve gadulka', '(gadulka yaylı bir çalgıdır)')),
            ('Yemek', ('Hem sıcak hem soğuk servis', 'edilebilen çorbalar')),
            ('Giyim-kuşam', ('Kukeri adı verilen kostümler', '(hayvan kürklerinden yapılır)')),
            ('Kutlama', ('Surva Festivali', '(kukeri burada giyilir)')),
            ('Gelenek ve görenekler', ('Marteniçka adlı bileklik', 'mart ayında takılır'))]
    ic = ''
    for i, (ad, satir) in enumerate(kart):
        x = 8 + (i % 2) * 232
        y = 8 + (i // 2) * 72
        ic += _kart(x, y, 224, 64, 'mavi', ad, satir, ilk=42, aralik=15)
    ic += '<text x="236" y="236" text-anchor="middle" font-size="12" class="g-s">Bulgaristan’dan katılan çocuğun anlattıkları, altı başlıkta.</text>'
    return svg(472, 246, ic, 'Bulgaristan’dan katılan çocuğun anlattıkları altı başlıkta: sanat: kalaycılık; müzik: kaval, zurna ve gadulka; '
               'yemek: hem sıcak hem soğuk servis edilebilen çorbalar; giyim-kuşam: kukeri kostümleri; kutlama: Surva Festivali; '
               'gelenek ve görenekler: marteniçka takma.')


def ortak_ozellikler():
    """Türkiye ile KKTC'de ortak görülen kültürel özellikler (kitap s. 25)."""
    ic = '<rect x="8" y="8" width="456" height="30" rx="8" class="g-yf"/>'
    ic += '<text x="236" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">Türkiye ile KKTC’de ortak görülen özellikler</text>'
    satir = [('Yemek', 42, ('Enginar dolması, kabak çiçeği dolması, humus,', 'tarhana çorbası, ızgara hellim')),
             ('Halk oyunu', 28, ('Zeybek (tek başına ya da daire biçiminde)',)),
             ('El sanatı', 28, ('Zembil, ahşap baskı, ebru, el dokuması kilim',)),
             ('Giyim-kuşam', 42, ('Tarabulus kuşağı', '(Anadolu’daki bazı köylerde de görülür)')),
             ('İkram', 28, ('Kahve (yanında su ve macunla ikram edilir)',))]
    y = 46
    for ad, h, metin in satir:
        ic += f'<rect x="8" y="{y}" width="108" height="{h}" rx="6" class="g-z"/>'
        ic += f'<rect x="8" y="{y}" width="108" height="{h}" rx="6" class="g-c" stroke-width="1.5"/>'
        ic += f'<text x="16" y="{y + h / 2 + 4:g}" font-size="12.5" font-weight="800" class="g-y">{ad}</text>'
        ic += f'<rect x="122" y="{y}" width="342" height="{h}" rx="6" class="g-ya"/>'
        for k, t in enumerate(metin):
            ty = y + (19 if h == 28 else 18 + 16 * k)
            ic += f'<text x="130" y="{ty}" font-size="12" class="g-y">{t}</text>'
        y += h + 6
    return svg(472, 244, ic, 'Türkiye ile KKTC’de ortak görülen özellikler: yemek: enginar dolması, kabak çiçeği dolması, humus, tarhana çorbası, '
               'ızgara hellim; halk oyunu: zeybek; el sanatı: zembil, ahşap baskı, ebru, el dokuması kilim; giyim-kuşam: Tarabulus kuşağı, '
               'Anadolu’daki bazı köylerde de görülür; ikram: kahve, yanında su ve macunla.')


def bir_araya_gelme():
    """Farklı kültürlerden insanların bir araya geldiği dört durum (kitap s. 27-28)."""
    kart = [('mavi', 'Turizm', ('Hollandalı bir turist', 'Kuşadası’nda dalış öğrendi,', 'tatilini orada geçiriyor.')),
            ('turuncu', 'Eğitim', ('Ganalı öğrenci Rize’de', 'tıp okurken horon ve', 'türkü öğrendi.')),
            ('yesil', 'İş için göç', ('Türk işçiler 1961-1973', 'arasında Almanya’ya gitti;', 'döner yaygınlaştı.')),
            ('mor', 'Uyum projesi', ('Suriyeli ve Türk aileler', 'yemeklerini birbirine', 'ikram etti: dostluk sofrası.'))]
    ic = ''
    for i, (renk, ad, satir) in enumerate(kart):
        x = 8 + (i % 2) * 232
        y = 8 + (i // 2) * 92
        ic += _kart(x, y, 224, 84, renk, ad, satir, ilk=46, aralik=16)
    ic += '<text x="236" y="206" text-anchor="middle" font-size="12" class="g-s">Bu dört durumda farklı kültürlerden insanlar bir araya gelir.</text>'
    return svg(472, 216, ic, 'Farklı kültürlerden insanların bir araya geldiği dört durum: turizm (Hollandalı turist, Kuşadası), eğitim (Ganalı öğrenci, Rize), '
               'iş için göç (Almanya’ya giden Türk işçiler, döner), uyum projesi (Türk ve Suriyeli ailelerin dostluk sofrası).')


def selamlasma():
    """Selamlaşma biçimleri (kitap s. 33): Türk ve Japon kültürlerinde ortak biçim turuncu."""
    satir = [('turuncu', 'Türk kültürü', 44, ('El sıkışma, sarılma, el öpme ve', 'başı hafifçe öne eğme')),
             ('turuncu', 'Japonya', 28, ('Başı hafifçe öne eğme',)),
             ('mavi', 'Filipinliler', 28, ('Büyüklerin elini alnına koyma',)),
             ('mavi', 'Fransa', 28, ('Birbirini yanaktan öpme',)),
             ('mavi', 'Yunanlar', 28, ('Tanıdığının sırtına ya da omzuna dokunma',)),
             ('mavi', 'Maori halkı', 28, ('Burun ve alınları birbirine bastırma',))]
    ic = ''
    y = 8
    for renk, ad, h, metin in satir:
        a, s, f = RENK[renk]
        ic += f'<rect x="8" y="{y}" width="112" height="{h}" rx="6" class="g-z"/>'
        ic += f'<rect x="8" y="{y}" width="112" height="{h}" rx="6" class="g-c" stroke-width="1.5"/>'
        ic += f'<text x="16" y="{y + h / 2 + 4:g}" font-size="12.5" font-weight="800" class="g-y">{ad}</text>'
        ic += f'<rect x="126" y="{y}" width="338" height="{h}" rx="6" class="{a}"/>'
        for k, t in enumerate(metin):
            ty = y + (19 if h == 28 else 18 + 16 * k)
            ic += f'<text x="134" y="{ty}" font-size="12" class="g-y">{t}</text>'
        y += h + 6
    ic += '<circle cx="16" cy="244" r="6" class="g-tf"/>'
    ic += '<text x="28" y="248" font-size="12" class="g-y">Başı hafifçe öne eğme: iki kültürde ortak</text>'
    ic += '<circle cx="340" cy="244" r="6" class="g-mf"/>'
    ic += '<text x="352" y="248" font-size="12" class="g-y">Diğer biçimler</text>'
    return svg(472, 258, ic, 'Selamlaşma biçimleri: Türk kültüründe el sıkışma, sarılma, el öpme ve başı hafifçe öne eğme; Japonya’da başı hafifçe öne eğme '
               '(iki kültürde ortak); Filipinliler büyüklerin elini alınlarına koyar; Fransa’da yanaktan öpme; Yunanlar tanıdıklarının sırtına ya da omzuna dokunur; '
               'Maori halkı burun ve alınları birbirine bastırır.')


def uygula(o):
    g = {'Ülkeler kültürünü altı başlıkta tanıtır': ulke_basliklari(),
         'Türkiye ve KKTC arasındaki ortak özellikler': ortak_ozellikler(),
         'Farklı kültürler hangi durumlarda bir araya gelir?': bir_araya_gelme(),
         'Selamlaşma ve aşure benzetmesi': selamlasma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
