"""7. sınıf Türkçe, 4. hafta: Gençliğin Kıymeti (hedef sunumu, kendini değerlendirme yazısı, sebep-sonuç metin yapısı).

Görseller yalnız MEB 7. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s29, s36-s41); metin cümleleri görsele alınmaz.
Renk anlamı:
- Sunum hazırlığı: mavi = veri toplama, turuncu = karşılaştırma, yeşil = sunuma hazırlık.
- Sunum sırasında ve sonrasında: mor = sunum sırasında dikkat edilenler; mavi, turuncu, yeşil = üç değerlendirme ölçütü.
- Yazı planı: mavi = ölçüt listesi, turuncu = ölçüt paragrafları, mor = geçiş ifadeleri, yeşil = yazım ve noktalama.
- Sebep-sonuç: mavi = sebep, turuncu = sonuç, mor = hem sonuç hem sonraki sebep (zincirin ara halkası).
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı, koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _hap(x, y, w, h, renk, metin, boyut=11):
    a, _, f, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h // 2}" class="{a}"/>'
            + _yazi(x + w / 2, y + h / 2 + boyut * 0.36, metin, boyut, f, True, 'middle'))


def _panel(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="g-c" stroke-width="1.5"/>')


def hazirlik():
    """Sunum hazırlığı: görüşme, not alma, karşılaştırma, çoklu ortam, prova (s29)."""
    adimlar = [
        ('mavi', 'Üç akranla ve üç yetişkinle konuş', 'veri toplama'),
        ('mavi', 'Hedefleri ve çalışmaları öğren', 'veri toplama'),
        ('turuncu', 'Benzerlik ve farklılıkları belirle', 'karşılaştırma'),
        ('yesil', 'Şema, grafik, tablo veya sunu hazırla', 'hazırlık'),
        ('yesil', 'Sunumu planla, materyalle prova yap', 'hazırlık'),
    ]
    ic = ''
    for i in range(4):
        ic += f'<line x1="26" y1="{8 + i * 50 + 33}" x2="26" y2="{8 + (i + 1) * 50 + 5}" class="g-c" stroke-width="2.5"/>'
    for i, (renk, metin, etiket) in enumerate(adimlar):
        y = 8 + i * 50
        _, _, yaz, koyu = RENK[renk]
        ic += _kutu(48, y, 416, 38, renk, rx=10)
        ic += f'<circle cx="26" cy="{y + 19}" r="13" class="{koyu}"/>'
        ic += _yazi(26, y + 24, str(i + 1), 13, 'g-b', True, 'middle')
        ic += _yazi(62, y + 24, metin, 12.5)
        ic += _hap(350, y + 8, 108, 22, renk, etiket, 11)
    return svg(472, 254, ic, 'Sunuma hazırlık beş adımdır. Bir, üç akranla ve üç yetişkinle konuş. İki, hedefleri ve çalışmaları not al. '
               'Bu iki adım mavidir ve veri toplamadır. Üç, benzerlik ve farklılıkları belirle; turuncudur ve karşılaştırmadır. '
               'Dört, şema, grafik, tablo veya sunu hazırla. Beş, sunumu planla ve materyalle prova yap. Son iki adım yeşildir ve hazırlıktır.')


def sunum():
    """Sunum sırasında dikkat edilenler ve sunumdan sonra üç değerlendirme ölçütü (s36)."""
    ic = '<defs>' + ok_isareti('okT4a', 'g-s') + '</defs>'
    ic += _kutu(8, 8, 456, 62, 'mor')
    ic += _yazi(22, 30, 'Sunum sırasında', 13, 'g-of', True)
    for x, w, metin in [(22, 120, 'Göz teması'), (152, 120, 'Beden dili'), (282, 170, 'Sınıfın özellikleri')]:
        ic += _hap(x, 40, w, 22, 'mor', metin, 11.5)
    ic += '<line x1="236" y1="72" x2="236" y2="100" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4a)"/>'
    ic += _yazi(248, 84, 'sunumdan sonra:', 11.5, 'g-s') + _yazi(248, 97, 'soruları cevapla, değerlendir', 11.5, 'g-s')
    kartlar = [(8, 'mavi', 'Amaca', 'ulaşma'), (164, 'turuncu', 'İçeriğin', 'yeterliliği'), (320, 'yesil', 'Dilin', 'anlaşılırlığı')]
    for i, (x, renk, s1, s2) in enumerate(kartlar):
        _, _, yaz, koyu = RENK[renk]
        ic += _kutu(x, 108, 144, 74, renk)
        ic += f'<circle cx="{x + 21}" cy="145" r="11" class="{koyu}"/>'
        ic += _yazi(x + 21, 150, str(i + 1), 12.5, 'g-b', True, 'middle')
        ic += _yazi(x + 40, 140, s1, 12, yaz, True)
        ic += _yazi(x + 40, 158, s2, 12, yaz, True)
    return svg(472, 192, ic, 'Sunum sırasında sınıfın özellikleri, göz teması ve beden dili önemlidir. Sunumdan sonra arkadaşların soruları cevaplanır ve üç ölçüte bakılır: '
               'bir, amaca ulaşma; iki, içeriğin yeterliliği; üç, dilin anlaşılırlığı.')


def yazi_plani():
    """Ölçüt listesi → her ölçüt için bir paragraf → geçiş ifadeleri → yazım ve noktalama (s36-s37)."""
    ic = '<defs>' + ok_isareti('okT4b', 'g-s') + '</defs>'
    ic += _kutu(8, 8, 132, 244, 'mavi')
    ic += _yazi(22, 32, 'Ölçüt listesi', 13, 'g-mf', True)
    for cy, metin in [(71, '1. ölçüt'), (155, '2. ölçüt'), (230, 'Diğer ölçütler')]:
        ic += _hap(20, cy - 14, 108, 28, 'mavi', metin, 11)
    ic += _yazi(176, 28, 'Kendini değerlendirme yazısı', 12.5, 'g-y', True)
    paragraflar = [(40, 62, '1. ölçütün paragrafı', ['yaşamından örnek', 'karşılaştırma sonucu']),
                   (124, 62, '2. ölçütün paragrafı', ['yaşamından örnek', 'karşılaştırma sonucu'])]
    for y, h, baslik, satirlar in paragraflar:
        ic += _kutu(176, y, 288, h, 'turuncu')
        ic += _yazi(190, y + 22, baslik, 12.5, 'g-tf', True)
        for k, s in enumerate(satirlar):
            ic += _yazi(190, y + 38 + k * 15, s, 11.5)
        ic += f'<line x1="130" y1="{y + h // 2}" x2="172" y2="{y + h // 2}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4b)"/>'
    ic += _kutu(176, 208, 288, 44, 'turuncu')
    ic += _yazi(190, 235, 'Diğer ölçütler de aynı düzende', 12.5, 'g-tf', True)
    ic += '<line x1="130" y1="230" x2="172" y2="230" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4b)"/>'
    ic += _yazi(320, 117, 'geçiş ifadesi', 11, 'g-of', True, 'middle')
    ic += _yazi(320, 201, 'geçiş ifadesi', 11, 'g-of', True, 'middle')
    ic += _kutu(176, 262, 288, 34, 'yesil')
    ic += _yazi(190, 284, 'Yazım ve noktalama denetlenir', 12.5, 'g-yf', True)
    return svg(472, 304, ic, 'Kendini değerlendirme yazısının planı: Ölçüt listesindeki her ölçüt için ayrı bir paragraf yazılır. '
               'Her paragrafta kendi yaşamından örnek ve karşılaştırma sonucu bulunur. Paragraflar geçiş ifadeleriyle bağlanır. '
               'Diğer ölçütler de aynı düzende işlenir. Son olarak yazım ve noktalama denetlenir.')


def uc_sema():
    """Sebep-sonuç metin yapısının üç grafik düzenleyicisi (s38)."""
    ic = '<defs>' + ok_isareti('okT4c', 'g-s') + '</defs>'
    for i, (satir1, satir2) in enumerate([('Çok sebep,', 'bir sonuç'), ('Bir sebep,', 'çok sonuç'), ('Sebep-sonuç', 'zinciri')]):
        x0 = 6 + i * 158
        ic += _panel(x0, 6, 150, 190)
        ic += _yazi(x0 + 75, 30, satir1, 12.5, 'g-y', True, 'middle')
        ic += _yazi(x0 + 75, 47, satir2, 12.5, 'g-y', True, 'middle')
    # 1. panel: çok sebep, bir sonuç
    x0 = 6
    for k, cy in enumerate((75, 107, 139)):
        ic += _kutu(x0 + 6, cy - 13, 64, 26, 'mavi', rx=8)
        ic += _yazi(x0 + 38, cy + 4, f'Sebep {k + 1}', 11, 'g-mf', True, 'middle')
        ic += f'<line x1="{x0 + 72}" y1="{cy}" x2="{x0 + 89}" y2="{98 + 9 * k}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4c)"/>'
    ic += _kutu(x0 + 94, 94, 50, 26, 'turuncu', rx=8)
    ic += _yazi(x0 + 119, 111, 'Sonuç', 11, 'g-tf', True, 'middle')
    # 2. panel: bir sebep, çok sonuç
    x0 = 164
    ic += _kutu(x0 + 6, 94, 48, 26, 'mavi', rx=8)
    ic += _yazi(x0 + 30, 111, 'Sebep', 11, 'g-mf', True, 'middle')
    for k, cy in enumerate((75, 107, 139)):
        ic += _kutu(x0 + 80, cy - 13, 64, 26, 'turuncu', rx=8)
        ic += _yazi(x0 + 112, cy + 4, f'Sonuç {k + 1}', 11, 'g-tf', True, 'middle')
        ic += f'<line x1="{x0 + 56}" y1="107" x2="{x0 + 75}" y2="{cy}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4c)"/>'
    # 3. panel: zincir
    x0 = 322
    cx = x0 + 75
    ic += _kutu(x0 + 25, 60, 100, 26, 'mavi', rx=8)
    ic += _yazi(cx, 77, 'Sebep', 11, 'g-mf', True, 'middle')
    ic += f'<line x1="{cx}" y1="88" x2="{cx}" y2="99" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4c)"/>'
    ic += _kutu(x0 + 15, 104, 120, 40, 'mor', rx=8)
    ic += _yazi(cx, 120, 'Sonuç ve', 11, 'g-of', True, 'middle')
    ic += _yazi(cx, 135, 'sonraki sebep', 11, 'g-of', True, 'middle')
    ic += f'<line x1="{cx}" y1="146" x2="{cx}" y2="157" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT4c)"/>'
    ic += _kutu(x0 + 25, 162, 100, 26, 'turuncu', rx=8)
    ic += _yazi(cx, 179, 'Sonuç', 11, 'g-tf', True, 'middle')
    # açıklama
    for x, renk, metin in [(16, 'mavi', 'sebep'), (96, 'turuncu', 'sonuç'), (176, 'mor', 'hem sonuç hem sonraki sebep')]:
        ic += f'<rect x="{x}" y="209" width="11" height="11" rx="3" class="{RENK[renk][3]}"/>'
        ic += _yazi(x + 17, 219, metin, 11.5, 'g-s')
    return svg(478, 228, ic, 'Sebep-sonuç metin yapısının üç şeması. Çok sebep bir sonuç: sebep bir, iki ve üç oklarla tek sonuca gider. '
               'Bir sebep çok sonuç: tek sebep okla sonuç bir, iki ve üçe gider. Sebep-sonuç zinciri: sebep bir sonuca gider; bu sonuç hem sonuç hem sonraki sebeptir ve son sonuca gider. '
               'Mavi sebep, turuncu sonuç, mor hem sonuç hem sonraki sebeptir.')


def ifadeler():
    """Sebep ifadeleri, sonuç ifadeleri ve iki listede de yer alan ifade (s38)."""
    ic = ''
    ic += _kutu(6, 6, 160, 214, 'mavi')
    ic += _yazi(20, 32, 'Sebep ifadeleri', 12.5, 'g-mf', True)
    for i, m in enumerate(['çünkü', '-dığı için', '-den dolayı']):
        ic += _kutu(16, 46 + i * 34, 140, 26, 'mavi', rx=13)
        ic += _yazi(86, 63 + i * 34, m, 12, 'g-y', False, 'middle')
    ic += _kutu(174, 6, 124, 214, 'mor')
    ic += _yazi(236, 32, 'İki listede', 12.5, 'g-of', True, 'middle')
    ic += _kutu(184, 46, 104, 26, 'mor', rx=13)
    ic += _yazi(236, 63, 'bu nedenle', 12, 'g-y', False, 'middle')
    ic += _yazi(236, 100, 'Anlama bakarak', 11, 'g-s', False, 'middle')
    ic += _yazi(236, 116, 'karar ver', 11, 'g-s', False, 'middle')
    ic += _kutu(306, 6, 160, 214, 'turuncu')
    ic += _yazi(320, 32, 'Sonuç ifadeleri', 12.5, 'g-tf', True)
    for i, m in enumerate(['böylece', 'dolayısıyla', 'buna bağlı olarak', 'bu yüzden', 'sonuç olarak']):
        ic += _kutu(316, 46 + i * 34, 140, 26, 'turuncu', rx=13)
        ic += _yazi(386, 63 + i * 34, m, 12, 'g-y', False, 'middle')
    return svg(472, 226, ic, 'Sebep ve sonuç ifadeleri. Mavi sütun sebep ifadeleri: çünkü, dığı için, den dolayı. Turuncu sütun sonuç ifadeleri: böylece, dolayısıyla, buna bağlı olarak, bu yüzden, sonuç olarak. '
               'Mor sütun iki listede de yer alan bu nedenle ifadesidir; cümlenin anlamına bakarak karar verilir.')


def zincir():
    """İyilikseverlik → güven ortamı → dayanışma kültürü → ortak değer (s40)."""
    ic = '<defs>' + ok_isareti('okT4d', 'g-s') + '</defs>'
    halkalar = [('mavi', 'İyilikseverlik', 'sebep'), ('mor', 'Güven ortamı', 'sonuç ve sonraki sebep'),
                ('mor', 'Dayanışma kültürü', 'sonuç ve sonraki sebep'), ('turuncu', 'Ortak değer olan iyilik', 'son sonuç')]
    for i, (renk, ad, rol) in enumerate(halkalar):
        y = 8 + i * 62
        _, _, yaz, _ = RENK[renk]
        ic += _kutu(16, y, 236, 36, renk, rx=10)
        ic += _yazi(134, y + 23, ad, 13.5, yaz, True, 'middle')
        ic += _yazi(268, y + 22, rol, 12, yaz, True)
        if i < 3:
            ic += f'<line x1="134" y1="{y + 39}" x2="134" y2="{y + 55}" class="g-c" stroke-width="2.5" stroke-linecap="round" marker-end="url(#okT4d)"/>'
    return svg(472, 244, ic, 'İyiliğin zincirleme etkisi: iyilikseverlik sebeptir ve güven ortamına yol açar; güven ortamı hem sonuç hem sonraki sebeptir ve dayanışma kültürüne yol açar; '
               'dayanışma kültürü de hem sonuç hem sonraki sebeptir ve iyiliğin toplumun ortak değeri olmasına yol açar. Ortak değer olan iyilik son sonuçtur.')


def uygula(o):
    g = {'Hedefleri karşılaştıran sunuma hazırlık': hazirlik(),
         'Sunumu yapmak ve değerlendirmek': sunum(),
         'Ölçüt listesiyle kendini değerlendirme yazısı': yazi_plani(),
         'Sebep-sonuç metin yapısı': uc_sema(),
         'Sebep ve sonuç ifadeleri': ifadeler(),
         'Üç yazıyı şemalarla çözümlemek': zincir()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
