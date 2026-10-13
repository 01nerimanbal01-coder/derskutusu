"""7. sınıf Türkçe, 2. hafta: Martı Jonathan Livingston (problem çözme, izlediğini değerlendirme, e-postaya cevap, sunum hazırlığı).

Görseller yalnız MEB 7. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s12-s14, s20, s22-s23, s27-s29);
metin cümleleri görsele alınmaz.
Renk anlamı:
- Problem çözme: mavi = problemi anlama (tanımla, özetle), turuncu = öneri üretme, yeşil = karar; gri = Jonathan'ın öyküsü.
- Değerlendirme: mor = ölçüt sorusu, yeşil = uygunsa gerekçe, turuncu = uygun değilse öneri.
- E-postaya cevap: mavi = selam ve hitap, yeşil = konuya cevap, turuncu = gerekçe ve örnek, mor = kapanış; gri = konu.
- Sunum hazırlığı: mavi = akran, turuncu = yetişkin; adımlar mavi, yeşil, turuncu, mor.
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


def problem():
    """Kitap s20, 6. Etkinlik: problemi tanımla, özetle, öneri üret, en uygununu gerekçesiyle seç (s13-s14 öyküsüyle)."""
    adim = [('mavi', '1. Tanımla', 'Kim, neyi yaşıyor?',
             ['Jonathan uçmayı öğrenmek istiyor;', 'ailesi ve sürü onu anlamıyor.']),
            ('mavi', '2. Özetle', 'kısaca anlat',
             ['Avlanmıyor, zayıflıyor;', 'ailesi onun için kaygılanıyor.']),
            ('turuncu', '3. Öneri üret', 'birden çok yol',
             ['Hedefini anlatmak · beslenmeyi', 'ihmal etmemek · öğrendiğini paylaşmak']),
            ('yesil', '4. Seç', 'gerekçesiyle',
             ['Hem hedefi hem ailenin kaygısını', 'gözeten öneri seçilir.'])]
    ic = '<defs>' + ok_isareti('okTR72a', 'g-s') + '</defs>'
    ic += _yazi(71, 18, 'Adım', 12.5, 'g-s', kalin=True)
    ic += _yazi(312, 18, 'Jonathan’ın öyküsünde', 12.5, 'g-s', kalin=True)
    for k, (renk, ad, alt, satir) in enumerate(adim):
        y = 28 + k * 60
        f = RENK[renk][2]
        ic += _kutu(6, y, 130, 46, renk)
        ic += _yazi(71, y + 20, ad, 13, f, kalin=True)
        ic += _yazi(71, y + 37, alt, 12, f)
        ic += _gri(158, y, 308, 46)
        ic += _yazi(172, y + 19, satir[0], 12.5, hiza='start')
        ic += _yazi(172, y + 37, satir[1], 12.5, hiza='start')
        ic += f'<line x1="137" y1="{y + 23}" x2="157" y2="{y + 23}" class="g-c" stroke-width="1.5"/>'
        if k < 3:
            ic += (f'<line x1="71" y1="{y + 47}" x2="71" y2="{y + 59}" class="g-c" stroke-width="2" '
                   f'marker-end="url(#okTR72a)"/>')
    return svg(472, 260, ic, 'Problem çözme adımları ve Jonathan’ın öyküsü: 1. Tanımla: Jonathan uçmayı öğrenmek istiyor, '
               'ailesi ve sürü onu anlamıyor. 2. Özetle: avlanmıyor, zayıflıyor, ailesi kaygılanıyor. 3. Öneri üret: hedefini '
               'anlatmak, beslenmeyi ihmal etmemek, öğrendiğini paylaşmak. 4. Gerekçesiyle seç: hem hedefi hem ailenin '
               'kaygısını gözeten öneri seçilir.')


def degerlendirme():
    """Kitap s23, 9. Etkinlik: başlık, örnekler ve akış; uygunsa gerekçe, değilse öneri."""
    satir = [('Başlık', 'içeriğe uygun mu?', 'Yeni başlık öner', 'Nasıl bir başlık?'),
             ('Örnekler', 'yeterli mi?', 'Eklenecekleri yaz', 'Neler eklenebilir?'),
             ('Akış', 'ilgi çekici mi?', 'Yeni sıra öner', 'Nasıl sıralanmalı?')]
    ic = _yazi(78, 18, 'Ölçüt', 12.5, 'g-of', kalin=True)
    ic += _yazi(239, 18, 'Uygunsa', 12.5, 'g-yf', kalin=True)
    ic += _yazi(394, 18, 'Uygun değilse', 12.5, 'g-tf', kalin=True)
    for k, (ad, soru, oneri, alt) in enumerate(satir):
        y = 28 + k * 64
        ic += _kutu(6, y, 144, 54, 'mor')
        ic += _yazi(78, y + 23, ad, 13, 'g-of', kalin=True)
        ic += _yazi(78, y + 42, soru, 12, 'g-of')
        ic += _kutu(166, y, 146, 54, 'yesil')
        ic += _yazi(239, y + 23, 'Gerekçeni yaz', 12.5, 'g-yf', kalin=True)
        ic += _yazi(239, y + 42, '“Çünkü …”', 12, 'g-yf')
        ic += _kutu(322, y, 144, 54, 'turuncu')
        ic += _yazi(394, y + 23, oneri, 12.5, 'g-tf', kalin=True)
        ic += _yazi(394, y + 42, alt, 12, 'g-tf')
    ic += _yazi(236, 236, 'Örnek içerikte: okuma yazma, satranç, metal işleme,', 12, 'g-s')
    ic += _yazi(236, 254, 'araba kullanma, resim yapma, halk oyunları', 12, 'g-s')
    return svg(472, 262, ic, 'İzlenen içeriği değerlendirme: başlık içeriğe uygun mu, örnekler yeterli mi, akış ilgi çekici mi? '
               'Uygunsa gerekçe yazılır; uygun değilse yeni başlık, eklenecek örnekler ya da yeni sıralama önerilir. '
               '“Hayat Büyük Bir Okuldur” içeriğindeki örnekler: okuma yazma, satranç, metal işleme, araba kullanma, '
               'resim yapma, halk oyunları.')


def eposta_cevap():
    """Kitap s27-s28, 12. Etkinlik: Deniz’in e-postasına belediye başkanı olarak cevap ve ölçütler."""
    ic = _gri(6, 6, 300, 258, rx=12)
    ic += _yazi(18, 27, 'YENİ MESAJ', 12, 'g-s', kalin=True, hiza='start')
    ic += _yazi(18, 49, 'Alıcı: Deniz Yıldız', 12, hiza='start')
    ic += _yazi(18, 68, 'Konu: Doğal yaşam alanlarının korunması', 12, hiza='start')
    ic += '<line x1="16" y1="78" x2="296" y2="78" class="g-c" stroke-width="1.5"/>'
    blok = [('mavi', 88, 30, ['Sevgili Deniz,']),
            ('yesil', 126, 44, ['Kuş yuvalarıyla ilgili e-postanı okudum,', 'duyarlılığın için teşekkür ederim.']),
            ('turuncu', 178, 44, ['Budamada kuş yuvaları korunacak;', 'çünkü park, kuşların da yaşam alanı.']),
            ('mor', 230, 28, ['Saygılarımla · Belediye Başkanı'])]
    for renk, y, h, satir in blok:
        f = RENK[renk][2]
        ic += _kutu(16, y, 280, h, renk, rx=8)
        y0 = y + h / 2 + 4.5 - (len(satir) - 1) * 9
        for j, s in enumerate(satir):
            ic += _yazi(28, y0 + j * 18, s, 12, f, hiza='start')
    etiket = [(None, 58, 'Konu ve amaç'), ('mavi', 103, 'Selam ve hitap'), ('yesil', 148, 'Konuya cevap'),
              ('turuncu', 200, 'Gerekçe ve örnek'), ('mor', 244, 'Kapanış ve ad')]
    for renk, yc, ad in etiket:
        ic += _kutu(320, yc - 15, 146, 30, renk, rx=8) if renk else _gri(320, yc - 15, 146, 30, rx=8)
        ic += _yazi(393, yc + 4.5, ad, 12.5, RENK[renk][2] if renk else 'g-y', kalin=True)
        x1 = 306 if renk is None else 296
        ic += f'<line x1="{x1}" y1="{yc}" x2="320" y2="{yc}" class="g-c" stroke-width="1.5"/>'
    return svg(472, 270, ic, 'Bir e-postaya cevap örneği ve bölümleri: konu ve amaç (Doğal yaşam alanlarının korunması), selam ve '
               'hitap (Sevgili Deniz), konuya cevap (e-postayı okudum, duyarlılığın için teşekkür ederim), gerekçe ve örnek '
               '(budamada kuş yuvaları korunacak çünkü park kuşların da yaşam alanı), kapanış ve ad (Saygılarımla, '
               'Belediye Başkanı).')


def _kisi(x, y, sinif):
    return (f'<circle cx="{x}" cy="{y}" r="4.5" class="{sinif}"/>'
            f'<rect x="{x - 6}" y="{y + 6}" width="12" height="13" rx="5" class="{sinif}"/>')


def sunum():
    """Kitap s29, Gelecek Derse Hazırlık: görüşme, karşılaştırma, çoklu ortam materyali, plan ve prova."""
    ic = '<defs>' + ok_isareti('okTR72d', 'g-s') + '</defs>'
    adim = [('mavi', '1. Görüş', 'bilgi topla'), ('yesil', '2. Karşılaştır', 'ortak ve farklı'),
            ('turuncu', '3. Materyal seç', 'uygun olanı'), ('mor', '4. Planla', 've prova et')]
    for k, (renk, ad, alt) in enumerate(adim):
        y = 8 + k * 64
        f = RENK[renk][2]
        ic += _kutu(6, y, 130, 50, renk)
        ic += _yazi(71, y + 22, ad, 13, f, kalin=True)
        ic += _yazi(71, y + 40, alt, 12, f)
        ic += _gri(144, y, 322, 50)
        if k < 3:
            ic += (f'<line x1="71" y1="{y + 51}" x2="71" y2="{y + 63}" class="g-c" stroke-width="2" '
                   f'marker-end="url(#okTR72d)"/>')
    # 1. satır: üç akran, üç yetişkin
    ic += _yazi(156, 28, '3 akran ve 3 yetişkin', 12.5, kalin=True, hiza='start')
    ic += _yazi(156, 46, 'Beş yıllık hedefler, yapılanlar', 12, 'g-s', hiza='start')
    for j in range(3):
        ic += _kisi(374 + j * 14, 19, 'g-mf')
        ic += _kisi(422 + j * 14, 19, 'g-tf')
    # 2. satır: karşılaştırma
    ic += _yazi(156, 92, 'Gençlerin hedefleri ↔ yetişkinlerin', 12.5, kalin=True, hiza='start')
    ic += _yazi(156, 110, 'benzerlikler ve farklılıklar', 12, 'g-s', hiza='start')
    # 3. satır: materyal çipleri
    x = 154
    for ad, w in (('şema', 52), ('grafik', 56), ('tablo', 50), ('bilgisayar sunusu', 126)):
        ic += _kutu(x, 148, w, 28, 'turuncu', rx=14)
        ic += _yazi(x + w / 2, 166.5, ad, 12, 'g-tf', kalin=True)
        x += w + 7
    # 4. satır: plan ve prova
    ic += _yazi(156, 220, 'Materyallerle sunumu önceden dene.', 12.5, kalin=True, hiza='start')
    ic += _yazi(156, 238, 'Konuşma Vakti’ne hazır ol.', 12, 'g-s', hiza='start')
    return svg(472, 264, ic, 'Sözlü sunuma hazırlık: 1. Görüş: üç akran ve üç yetişkinle beş yıllık hedefleri ve yaptıklarını konuş. '
               '2. Karşılaştır: gençlerin ve yetişkinlerin hedefleri arasındaki benzerlikleri ve farklılıkları bul. '
               '3. Materyal seç: şema, grafik, tablo ya da bilgisayar sunusu. 4. Planla ve prova et: materyallerle sunumu '
               'önceden dene.')


def uygula(o):
    g = {'Jonathan’ın problemi ve çözüm önerileri': problem(),
         'İzlediğini değerlendirmek: başlık, örnekler ve akış': degerlendirme(),
         'Bir e-postaya cevap yazmak': eposta_cevap(),
         'Sözlü sunuma hazırlanmak: içerik ve çoklu ortam': sunum()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
