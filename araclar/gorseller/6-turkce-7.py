"""6. sınıf Türkçe, 7. hafta: Cepheye Koşan At; tahmin ve çıkarım, karşılaştırma ve sınıflandırma, özetleme ve yorum.

Görseller yalnız özet metnindeki (araclar/ozetler/6-turkce-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Metin cümleleri görsele alınmaz; insan figürü yoktur. Bütün şemalar ölçeksizdir.
Renk anlamı:
- Tahmin ve çıkarım: mavi = girdi (başlık, görsel, kanıt, ön bilgi); turuncu = ulaşılan düşünce (tahmin, çıkarım);
  yeşil = sonuç (kontrol, yargı). Sayfa şemasında kalın mavi çizgi = kanıt alınan cümle, gri çizgi = diğer cümleler.
- Karşılaştırma ve sınıflandırma: turuncu = farklılık; yeşil = benzerlik (ortak alan); mavi = ölçüt;
  mor = varılan sonuç (yargı, adı verilmiş grup); gri şekiller = henüz gruplanmamış unsurlar.
- Özetleme ve yorum: mavi = özetleme adımı; yeşil = önemli bilgi ve özet; gri çizgi = özete girmeyen ayrıntı;
  turuncu = yorum (seçilen bakış açısı).
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, kimlik, kalinlik=2.5):
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="g-c" stroke-width="{kalinlik:g}" marker-end="url(#{kimlik})"/>'


def _cizgi(x1, y1, x2, y2, sinif, kalinlik):
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="{sinif}" stroke-width="{kalinlik:g}" stroke-linecap="round"/>'


def _sayfa(x, y, kanit, kalin_sinif):
    """Üç paragraflı sayfa şeması; kanit = vurgulanacak (paragraf, satır) çiftleri. Satır y'lerini döndürür."""
    ic = (f'<rect x="{x}" y="{y}" width="136" height="126" rx="6" class="g-z"/>'
          f'<rect x="{x}" y="{y}" width="136" height="126" rx="6" class="g-c" stroke-width="1.5"/>')
    yler = {}
    for p in range(3):
        for s in range(3):
            sy = y + 16 + p * 38 + s * 10
            yler[(p, s)] = sy
            x2 = x + 84 if s == 2 else x + 122
            if (p, s) in kanit:
                ic += _cizgi(x + 14, sy, x2, sy, kalin_sinif, 5)
            else:
                ic += _cizgi(x + 14, sy, x2, sy, 'g-c', 2.5)
    return ic, yler


def tahmin_cikarim():
    """Tahmin ve çıkarım akışı; basit ve üst düzey çıkarımda kanıtın alındığı yer."""
    ic = '<defs>' + ok_isareti('ok6tr7a', 'g-s') + '</defs>'
    satirlar = [
        (28, 'Okumadan önce: tahmin', ('Başlık ve', 'görsel', True), 'Tahmin', 'oku', ('Kontrol', 'tuttu mu?')),
        (104, 'Okurken: çıkarım', ('Kanıt', 'metinden', False), 'Çıkarım', '', ('Yargı', 'gerekirse tepki')),
    ]
    for y, etiket, (a1, a2, a_kalin), orta, ok_etiket, (d1, d2) in satirlar:
        ic += _yazi(8, y - 10, etiket, 12.5, 'g-y', True)
        ic += _kutu(8, y, 96, 44, 'mavi', rx=10)
        if a_kalin:
            ic += _yazi(56, y + 19, a1, 13, 'g-mf', True, 'middle') + _yazi(56, y + 36, a2, 13, 'g-mf', True, 'middle')
        else:
            ic += _yazi(56, y + 19, a1, 13, 'g-mf', True, 'middle') + _yazi(56, y + 36, a2, 11.5, 'g-y', False, 'middle')
        ic += _yazi(113, y + 27, '+', 16, 'g-s', True, 'middle')
        ic += _kutu(122, y, 78, 44, 'mavi', rx=10)
        ic += _yazi(161, y + 27, 'Ön bilgi', 13, 'g-mf', True, 'middle')
        ic += _ok(206, y + 22, 230, y + 22, 'ok6tr7a')
        ic += _kutu(236, y, 82, 44, 'turuncu', rx=10)
        ic += _yazi(277, y + 27, orta, 14, 'g-tf', True, 'middle')
        ic += _ok(324, y + 22, 344, y + 22, 'ok6tr7a')
        if ok_etiket:
            ic += _yazi(334, y + 13, ok_etiket, 11.5, 'g-s', False, 'middle')
        ic += _kutu(350, y, 114, 44, 'yesil', rx=10)
        ic += _yazi(407, y + 19, d1, 13, 'g-yf', True, 'middle')
        ic += _yazi(407, y + 36, d2, 11.5, 'g-y', False, 'middle')
    # basit ve üst düzey çıkarım: kanıt nereden toplanır?
    ic += _yazi(104, 178, 'Basit çıkarım', 13, 'g-tf', True, 'middle')
    ic += _yazi(336, 178, 'Üst düzey çıkarım', 13, 'g-tf', True, 'middle')
    sol, ysol = _sayfa(36, 188, {(1, 0), (1, 1)}, 'g-ms')
    sag, ysag = _sayfa(268, 188, {(0, 0), (1, 1), (2, 0)}, 'g-ms')
    ic += sol + sag
    ic += _yazi(182, ysol[(1, 0)] + 9, 'bir paragraf', 11.5, 'g-s')
    for (p, s), ad in [((0, 0), 'başı'), ((1, 1), 'ortası'), ((2, 0), 'sonu')]:
        ic += _yazi(412, ysag[(p, s)] + 4, ad, 11.5, 'g-s')
    ic += _yazi(104, 332, 'Kanıt sınırlı bir bölümden', 11.5, 'g-y', False, 'middle')
    ic += _yazi(336, 332, 'Kanıt metnin bütününden', 11.5, 'g-y', False, 'middle')
    ic += _cizgi(36, 350, 56, 350, 'g-ms', 5) + _yazi(62, 354, 'kanıt', 11.5, 'g-s')
    ic += _cizgi(108, 350, 128, 350, 'g-c', 2.5) + _yazi(134, 354, 'diğer cümleler', 11.5, 'g-s')
    return svg(472, 360, ic, 'Tahmin ve çıkarım akışı. Okumadan önce başlık, görsel ve ön bilgi birleşince tahmin kurulur; okuduktan sonra tahmin '
               'kontrol edilir, tuttu mu diye bakılır. Okurken metindeki kanıt ön bilgiyle birleşince çıkarım yapılır, bir yargıya varılır '
               've gerekirse tepki verilir. Altta iki sayfa şeması: basit çıkarımda kanıt tek bir paragraftan, üst düzey çıkarımda metnin '
               'başından, ortasından ve sonundan toplanır.')


def karsilastirma_siniflandirma():
    """Solda Venn şemasıyla metin içi karşılaştırma, sağda ölçütle gruplama şeması."""
    ic = '<defs>' + ok_isareti('ok6tr7b', 'g-s') + '</defs>'
    for x in (8, 240):
        ic += (f'<rect x="{x}" y="8" width="224" height="296" rx="12" class="g-z"/>'
               f'<rect x="{x}" y="8" width="224" height="296" rx="12" class="g-c" stroke-width="1.5"/>')
    # --- karşılaştırma ---
    ic += _yazi(120, 32, 'Karşılaştırma', 14, 'g-y', True, 'middle')
    ic += _yazi(120, 50, 'metnin iki bölümü', 11.5, 'g-s', False, 'middle')
    ic += _yazi(66, 72, 'Başı', 12, 'g-y', True, 'middle') + _yazi(174, 72, 'Sonu', 12, 'g-y', True, 'middle')
    lens = 'M120 88.2A52 52 0 0 1 120 175.8A52 52 0 0 1 120 88.2Z'  # iki dairenin kesişimi
    ic += '<circle cx="92" cy="132" r="52" class="g-ta"/><circle cx="148" cy="132" r="52" class="g-ta"/>'
    ic += f'<path d="{lens}" class="g-ya"/>'
    ic += '<circle cx="92" cy="132" r="52" class="g-ts" stroke-width="2"/><circle cx="148" cy="132" r="52" class="g-ts" stroke-width="2"/>'
    ic += f'<path d="{lens}" class="g-ys" stroke-width="2"/>'
    ic += _yazi(66, 136, 'korku', 12, 'g-y', False, 'middle') + _yazi(174, 136, 'sevinç', 12, 'g-y', False, 'middle')
    ic += _yazi(120, 128, 'aynı', 11.5, 'g-y', False, 'middle') + _yazi(120, 144, 'mekân', 11.5, 'g-y', False, 'middle')
    ic += _yazi(66, 206, 'Farklılık', 12, 'g-tf', True, 'middle') + _yazi(174, 206, 'Farklılık', 12, 'g-tf', True, 'middle')
    ic += _cizgi(120, 181, 120, 212, 'g-ys', 1.5)
    ic += _yazi(120, 226, 'Benzerlik', 12, 'g-yf', True, 'middle')
    ic += _ok(120, 236, 120, 250, 'ok6tr7b')
    ic += _kutu(28, 256, 184, 40, 'mor', rx=10)
    ic += _yazi(120, 273, 'Yargı', 13.5, 'g-of', True, 'middle')
    ic += _yazi(120, 289, 'listelerden sonuç çıkar', 11.5, 'g-y', False, 'middle')
    # --- sınıflandırma ---
    ic += _yazi(352, 32, 'Sınıflandırma', 14, 'g-y', True, 'middle')
    ic += _yazi(352, 50, 'karışık unsurlar', 11.5, 'g-s', False, 'middle')
    for k, x in enumerate((287, 313, 339, 365, 391, 417)):
        if k in (0, 3, 5):
            ic += f'<circle cx="{x}" cy="66" r="7" class="g-z"/><circle cx="{x}" cy="66" r="7" class="g-c" stroke-width="1.5"/>'
        else:
            ic += (f'<rect x="{x - 7}" y="59" width="14" height="14" rx="2" class="g-z"/>'
                   f'<rect x="{x - 7}" y="59" width="14" height="14" rx="2" class="g-c" stroke-width="1.5"/>')
    ic += _ok(352, 78, 352, 90, 'ok6tr7b')
    ic += '<rect x="292" y="98" width="120" height="36" rx="8" class="g-mf"/>'
    ic += _yazi(352, 113, 'Ölçüt', 13, 'g-b', True, 'middle') + _yazi(352, 128, 'ör. unsurun türü', 11.5, 'g-b', False, 'middle')
    ic += _ok(334, 138, 306, 156, 'ok6tr7b') + _ok(370, 138, 398, 156, 'ok6tr7b')
    ic += _kutu(250, 160, 100, 72, 'mor', rx=10) + _kutu(354, 160, 100, 72, 'mor', rx=10)
    ic += _yazi(300, 180, '1. grup', 12.5, 'g-of', True, 'middle') + _yazi(404, 180, '2. grup', 12.5, 'g-of', True, 'middle')
    for x in (280, 300, 320):
        ic += f'<circle cx="{x}" cy="208" r="7" class="g-of"/>'
    for x in (384, 404, 424):
        ic += f'<rect x="{x - 7}" y="201" width="14" height="14" rx="2" class="g-of"/>'
    ic += _yazi(352, 252, 'Ayır, grupla, her gruba ad ver.', 11.5, 'g-y', False, 'middle')
    ic += _yazi(352, 270, 'Her unsur tek bir gruba girer.', 11.5, 'g-s', False, 'middle')
    ic += _yazi(352, 288, 'Ölçüt değişince gruplar değişir.', 11.5, 'g-s', False, 'middle')
    return svg(472, 312, ic, 'Karşılaştırma ve sınıflandırma şeması. Solda metnin başı ve sonu için kesişen iki daire: ortadaki yeşil ortak alan '
               'benzerliği gösterir, örneğin aynı mekân; turuncu dış bölümler farklılıkları gösterir, başta korku, sonda sevinç. '
               'Benzerlik ve farklılık listelerinden bir yargıya varılır. Sağda karışık unsurlar bir ölçütten, örneğin unsurun türünden '
               'geçirilerek iki gruba ayrılır ve her gruba ad verilir; her unsur tek bir gruba girer, ölçüt değişince gruplar değişir.')


def ozetleme():
    """Özetlemenin dört adımı; metinden özete ve yoruma giden yol."""
    ic = '<defs>' + ok_isareti('ok6tr7c', 'g-s') + '</defs>'
    adimlar = [('1 · Çözümle', 'ne anlatıyor?'), ('2 · Ayır', 'önemliyi seç'), ('3 · Sırala', 'akışa göre'), ('4 · Anlat', 'kendi cümlenle')]
    for k, (baslik, alt) in enumerate(adimlar):
        x = 7 + k * 118
        ic += _kutu(x, 8, 104, 48, 'mavi', rx=10)
        ic += _yazi(x + 52, 28, baslik, 13, 'g-mf', True, 'middle')
        ic += _yazi(x + 52, 46, alt, 11.5, 'g-y', False, 'middle')
        if k < 3:
            ic += _ok(x + 106, 32, x + 112, 32, 'ok6tr7c', 1.5)
    # metin sayfası: önemli cümleler yeşil, ayrıntılar gri
    ic += _yazi(72, 84, 'Metin', 13, 'g-y', True, 'middle')
    ic += '<rect x="16" y="92" width="112" height="130" rx="6" class="g-z"/><rect x="16" y="92" width="112" height="130" rx="6" class="g-c" stroke-width="1.5"/>'
    onemli = {(0, 0): '1', (1, 1): '2', (2, 0): '3'}
    for p in range(3):
        for s in range(3):
            sy = 108 + p * 40 + s * 10
            x2 = 90 if s == 2 else 116
            if (p, s) in onemli:
                ic += _cizgi(42, sy, x2, sy, 'g-ys', 5) + _yazi(30, sy + 4, onemli[(p, s)], 11.5, 'g-yf', True, 'middle')
            else:
                ic += _cizgi(42, sy, x2, sy, 'g-c', 2.5)
    ic += _cizgi(16, 236, 36, 236, 'g-ys', 5) + _yazi(42, 240, 'önemli bilgi', 11.5, 'g-s')
    ic += _cizgi(16, 254, 36, 254, 'g-c', 2.5) + _yazi(42, 258, 'ayrıntı (özete girmez)', 11.5, 'g-s')
    ic += _ok(134, 157, 224, 121, 'ok6tr7c') + _ok(134, 157, 224, 214, 'ok6tr7c')
    ic += _yazi(178, 110, 'önemliyi seç', 11.5, 'g-s', False, 'middle')
    # özet kartı
    ic += _kutu(232, 86, 232, 72, 'yesil')
    ic += _yazi(246, 106, 'Özet', 13.5, 'g-yf', True)
    for n, (sy, x2) in enumerate(((122, 330), (135, 330), (148, 306)), 1):
        ic += _yazi(250, sy + 4, str(n), 11.5, 'g-yf', True, 'middle') + _cizgi(262, sy, x2, sy, 'g-ys', 4)
    ic += _cizgi(340, 98, 340, 150, 'g-ys', 1.5)
    for sy, s in ((112, 'önemli bilgi'), (129, 'kendi cümlen'), (146, 'doğru sıra')):
        ic += _yazi(350, sy, s, 11.5)
    # yorum kartı
    ic += _kutu(232, 176, 232, 80, 'turuncu')
    ic += _yazi(246, 196, 'Yorum', 13.5, 'g-tf', True)
    ic += _yazi(246, 214, 'kahvecinin, tarihçinin ya da', 11.5)
    ic += _yazi(246, 230, 'çocuğun gözünden yeniden anlat', 11.5)
    ic += _yazi(246, 247, 'tarihler ve olgular değişmez', 11.5)
    ic += _yazi(236, 278, 'Özet metnin küçültülmüş hâlidir, görüş katmaz.', 11.5, 'g-s', False, 'middle')
    return svg(472, 288, ic, 'Özetleme ve yorum şeması. Üstte dört adım: çözümle, her paragraf ne anlatıyor; ayır, önemliyi seç; sırala, akışa göre; '
               'anlat, kendi cümlenle. Altta bir metin sayfasında önemli cümleler yeşil ve bir, iki, üç diye numaralı, ayrıntılar gri. '
               'Metinden özete giden ok önemli bilgileri aynı sırayla kendi cümlelerinle taşır: önemli bilgi, kendi cümlen, doğru sıra. '
               'Metinden yoruma giden okta aynı olay kahvecinin, tarihçinin ya da çocuğun gözünden yeniden anlatılır; tarihler ve olgular '
               'değişmez. Özet metnin küçültülmüş hâlidir, görüş katmaz.')


def uygula(o):
    g = {'Başlıktan tahmin, satır arasından çıkarım': tahmin_cikarim(),
         'Karşılaştırma ve sınıflandırma': karsilastirma_siniflandirma(),
         'Özetleme ve yorum: önemliyi seç, kendi cümlenle anlat': ozetleme()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
