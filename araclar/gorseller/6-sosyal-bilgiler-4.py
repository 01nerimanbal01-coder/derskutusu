"""6. sınıf Sosyal Bilgiler, 4. hafta: toplumsal sorunlar ve çözüm önerileri.

Görseller yalnız MEB 6. sınıf Sosyal Bilgiler ders kitabındaki bilgilerle çizilir (kitap s. 38-49).
Renk anlamı: vakıflar görselinde mavi = vakıf, turuncu = sorun, yeşil = çözüm; plastik zincirinde turuncu = neden,
mavi = yayılma yolu, mor = sonuç; göç grafiğinde turuncu = karşılaştırılan iki yıl, mavi = aradaki yıllar;
Çözüm Köşesi akışında mavi = sorunu çözümleme, turuncu = çözüm üretme, yeşil = düzenleme. İnsan figürü kullanılmaz.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="1.5"/>')


def _metin(x, y, t, boyut=12.5, agirlik=None, sinif='g-y', ankor=None):
    a = f' text-anchor="{ankor}"' if ankor else ''
    g = f' font-weight="{agirlik}"' if agirlik else ''
    return f'<text x="{x}" y="{y}"{a} font-size="{boyut}"{g} class="{sinif}">{t}</text>'


def _etiket(x, y, w, renk, ad):
    """Küçük renkli etiket (beyaz yazı koyu dolguda)."""
    _, _, f = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="20" rx="10" class="{f}"/>'
            + _metin(x + w / 2, y + 14.5, ad, 12, 800, 'g-b', 'middle'))


def vakiflar():
    """Üç vakıf: yer ve yıl, çözdüğü sorun, çözüm (kitap s. 39)."""
    kartlar = [
        ('Bulaşıcı Hastalıkları Tedavi Vakfı', 'Sivas, 1321',
         'Cüzzam gibi bulaşıcı hastalıklar',
         ['Hastaların tedavisi; fakirlerin ve miskinlerin', 'cenaze ve defin giderlerinin karşılanması']),
        ('İsrafı Önleyen Vakıf', 'İstanbul, 1613',
         'Sofralarda artan yemeklerin israfı',
         ['Artan yemekler çöpe atılmaz, toplanır;', 'yaban hayvanlarına ve kuşlara ulaştırılır']),
        ('Afet Sonrası Bakım ve Onarım Yapan Vakıf', 'İstanbul, 1549',
         'Deprem ve yangın hasarı',
         ['Vakfiyede kayıtlı mescit, mektep ve diğer', 'mekânlar özenle onarılır']),
    ]
    ic = ''
    for i, (ad, yer, sorun, cozum) in enumerate(kartlar):
        y = 8 + i * 114
        ic += _kutu(8, y, 456, 104, 'mavi')
        ic += _metin(20, y + 22, ad, 12, 800, 'g-mf')
        ic += _metin(452, y + 22, yer, 12, None, 'g-y', 'end')
        ic += _etiket(20, y + 34, 56, 'turuncu', 'Sorun')
        ic += _metin(86, y + 49, sorun, 12)
        ic += _etiket(20, y + 62, 56, 'yesil', 'Çözüm')
        for k, satir in enumerate(cozum):
            ic += _metin(86, y + 77 + k * 17, satir, 12)
    return svg(472, 346, ic, 'Üç vakıf ve çözdükleri sorunlar. 1321’de Sivas’ta kurulan Bulaşıcı Hastalıkları Tedavi Vakfı: sorun cüzzam gibi bulaşıcı hastalıklardır; '
               'çözüm hastaların tedavisi ile fakir ve miskin kişilerin cenaze ile defin giderlerinin karşılanmasıdır. 1613’te İstanbul’da kurulan '
               'İsrafı Önleyen Vakıf: sorun sofralarda artan yemeklerin israfıdır; çözüm yemeklerin toplanıp yaban hayvanlarına ve kuşlara '
               'ulaştırılmasıdır. 1549’da İstanbul’da kurulan Afet Sonrası Bakım ve Onarım Yapan Vakıf: sorun deprem ve yangın hasarıdır; '
               'çözüm vakfiyede kayıtlı mescit, mektep ve diğer mekânların onarılmasıdır.')


def plastik_zinciri():
    """Plastik atıkların Karadeniz'e ulaşması: neden-sonuç zinciri (kitap s. 41)."""
    ic = '<defs>' + ok_isareti('okS64a', 'g-s') + '</defs>'
    ic += _metin(8, 18, 'Plastik atıklar: neden-sonuç zinciri', 13, 800)
    adim = [('turuncu', ['Plastik çöpler doğaya bırakılır']),
            ('mavi', ['Yağmur, rüzgâr ve akarsular', 'çöpleri Karadeniz’e ulaştırır']),
            ('mor', ['Görüntü kirliliği oluşur;', 'deniz yaşamı tehdit edilir']),
            ('mor', ['Plastiğin bulunduğu ortamlardaki', 'balıklar yer değiştirmek zorunda kalır']),
            ('mor', ['Karadeniz’deki balık miktarı olumsuz etkilenir'])]
    y = 30
    for i, (renk, satir) in enumerate(adim):
        h = 34 if len(satir) == 1 else 52
        ic += _kutu(8, y, 456, h, renk)
        ic += f'<circle cx="32" cy="{y + h / 2}" r="12" class="{RENK[renk][2]}"/>'
        ic += _metin(32, y + h / 2 + 4.5, str(i + 1), 12.5, 800, 'g-b', 'middle')
        for k, t in enumerate(satir):
            ty = y + (21 if len(satir) == 1 else 22 + k * 18)
            ic += _metin(54, ty, t, 12.5)
        if i < len(adim) - 1:
            ic += f'<line x1="236" y1="{y + h + 2}" x2="236" y2="{y + h + 16}" class="g-c" stroke-width="2" marker-end="url(#okS64a)"/>'
        y += h + 18
    y += 4
    for cx, renk, t in [(16, 'turuncu', 'Neden'), (96, 'mavi', 'Yayılma yolu'), (210, 'mor', 'Sonuçlar')]:
        ic += f'<circle cx="{cx}" cy="{y}" r="6" class="{RENK[renk][2]}"/>'
        ic += _metin(cx + 12, y + 4, t, 12)
    return svg(472, y + 14, ic, 'Plastik atıkların neden-sonuç zinciri: 1 plastik çöpler doğaya bırakılır, 2 yağmur, rüzgâr ve akarsular çöpleri '
               'Karadeniz’e ulaştırır, 3 görüntü kirliliği oluşur ve deniz yaşamı tehdit edilir, 4 plastiğin bulunduğu ortamlardaki balıklar yer '
               'değiştirmek zorunda kalır, 5 Karadeniz’deki balık miktarı olumsuz etkilenir.')


def goc_grafigi():
    """Doğduğu ülkeden başka bir ülkeye göç edenlerin dünya geneli sayısı, milyon kişi (kitap s. 42); tek ölçek, sıfırdan başlar."""
    veri = [(1970, 84), (1980, 102), (1990, 153), (2000, 173), (2010, 221), (2015, 248), (2019, 272), (2020, 281)]
    x0, olcek = 56, 300 / 281
    ic = _metin(8, 18, 'Doğduğu ülkeden başka bir ülkede yaşayanlar', 13, 800)
    ic += _metin(8, 36, '(dünya geneli, milyon kişi)', 12, None, 'g-s')
    ic += f'<line x1="{x0}" y1="46" x2="{x0}" y2="{50 + len(veri) * 28}" class="g-c" stroke-width="1.5"/>'
    for i, (yil, deger) in enumerate(veri):
        y = 54 + i * 28
        renk = 'turuncu' if yil in (1970, 2020) else 'mavi'
        uz = round(deger * olcek, 1)
        ic += _metin(x0 - 8, y + 14, str(yil), 12.5, 700, 'g-y', 'end')
        ic += f'<rect x="{x0 + 2}" y="{y}" width="{uz}" height="20" rx="5" class="{RENK[renk][2]}"/>'
        ic += _metin(x0 + 2 + uz + 8, y + 14.5, f'{deger} milyon', 12.5, 700 if renk == 'turuncu' else None)
    y = 54 + len(veri) * 28 + 10
    for cx, renk, t in [(16, 'turuncu', 'Karşılaştırılan iki yıl'), (200, 'mavi', 'Aradaki yıllar')]:
        ic += f'<circle cx="{cx}" cy="{y}" r="6" class="{RENK[renk][2]}"/>'
        ic += _metin(cx + 12, y + 4, t, 12)
    return svg(472, y + 14, ic, 'Doğduğu ülkeden başka bir ülkede yaşayanların dünya geneli sayısı, milyon kişi olarak: 1970’te 84, 1980’de 102, 1990’da 153, 2000’de 173, '
               '2010’da 221, 2015’te 248, 2019’da 272, 2020’de 281. Sayı yarım yüzyılda üç katından fazla büyümüştür.')


def cozum_kosesi():
    """Çözüm Köşesi etkinliğinin dört adımı (kitap s. 46-47)."""
    ic = '<defs>' + ok_isareti('okS64b', 'g-s') + '</defs>'
    ic += _metin(8, 18, 'Çözüm Köşesi: dört adım', 13, 800)
    adim = [('mavi', 'Sorunu seç, nedenleri listele',
             ['Gruplar günlük yaşamdan bir toplumsal sorun seçer;', 'aynı sorunu en az iki grup seçer; nedenler yazılır']),
            ('mavi', 'Nedenleri paylaş, görüşleri karşılaştır',
             ['Benzer yönler “Benzerlikler”, farklı yönler', '“Farklılıklar” tablosuna yazılır']),
            ('turuncu', 'Çözüm önerileri geliştir',
             ['Öneri özgün, uygulanabilir ve sürdürülebilir olur;', 'toplumsal fayda sağlar']),
            ('yesil', 'Paylaş, geri bildirim al, yeniden düzenle',
             ['Diğer gruplar önerinin güçlü ve zayıf yönlerini', 'belirler; grup öneriyi bu geri bildirimle düzenler'])]
    y = 30
    for i, (renk, baslik, satir) in enumerate(adim):
        ic += _kutu(8, y, 456, 66, renk)
        ic += f'<circle cx="32" cy="{y + 33}" r="12" class="{RENK[renk][2]}"/>'
        ic += _metin(32, y + 37.5, str(i + 1), 12.5, 800, 'g-b', 'middle')
        ic += _metin(54, y + 23, baslik, 12.5, 800)
        for k, t in enumerate(satir):
            ic += _metin(54, y + 41 + k * 17, t, 12)
        if i < len(adim) - 1:
            ic += f'<line x1="236" y1="{y + 68}" x2="236" y2="{y + 82}" class="g-c" stroke-width="2" marker-end="url(#okS64b)"/>'
        y += 84
    y += 2
    for cx, renk, t in [(16, 'mavi', 'Sorunu çözümleme'), (164, 'turuncu', 'Çözüm üretme'), (286, 'yesil', 'Düzenleme')]:
        ic += f'<circle cx="{cx}" cy="{y}" r="6" class="{RENK[renk][2]}"/>'
        ic += _metin(cx + 12, y + 4, t, 12)
    return svg(472, y + 14, ic, 'Çözüm Köşesi etkinliğinin dört adımı: 1 sorunu seç ve nedenleri listele, 2 nedenleri paylaş ve görüşleri benzerlikler ile '
               'farklılıklar tablosunda karşılaştır, 3 özgün, uygulanabilir, sürdürülebilir ve toplumsal fayda sağlayan çözüm önerileri geliştir, '
               '4 önerileri paylaş, güçlü ve zayıf yönler hakkında geri bildirim al ve öneriyi yeniden düzenle.')


def uygula(o):
    g = {'Vakıflar: geçmişin çözümleri': vakiflar(),
         'Doğal afetler ve çevre sorunları': plastik_zinciri(),
         'Göç ve salgın hastalıklar': goc_grafigi(),
         'Çözüm Köşesi: nedenleri karşılaştır, çözüm öner': cozum_kosesi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
