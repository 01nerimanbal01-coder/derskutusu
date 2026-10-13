"""6. sınıf Matematik, 7. hafta: kesir-bölme ilişkisi (kesir çizgisi bölme işaretidir, kâğıt-kalemle bölmeyi sürdürme,
sonlu ve devirli ondalık gösterim, tümevarımsal akıl yürütme ve payda kuralı, kalanlı bölme ve paylaştırma).

Görseller yalnız özet metnindeki (araclar/ozetler/6-matematik-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: mavi = bölüm (bölüme yazılan basamaklar; paylaştırmada her parçaya düşen tam metre); turuncu = kalan (ve kalandan gelen
ondalık kısım); yeşil = kalan sıfır, bölme biter → sonlu gösterim (paydanın asal çarpanı 2 ya da 5); mor = aynı kalan yeniden çıkar,
bölme bitmez → devirli gösterim (paydadaki 3, 7, 11 gibi başka asal çarpan); soluk gri rakam = kalanın sağına eklenen sıfır;
gri çizgi = bölme düzeni çizgileri ve akış okları.
Ölçek: kurdele modelinde her kare 1 metredir (1 m = 56 birim), çeyrek şeritler 25 santimetredir; öteki görseller şemadır (ölçeksiz).
"""
from ozet_gorsel import svg, ok_isareti, kesir_svg


def _kutu(x, y, w, h, a, s, rx=10, kalin=1.8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="{kalin}"/>')


def _etiket(x, y, w, h, dolgu, yazi, boy=12.5):
    """Koyu dolgulu hap etiket; yazı beyaz."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" class="{dolgu}"/>'
            f'<text x="{x + w / 2:g}" y="{y + h / 2 + boy * 0.36:g}" text-anchor="middle" font-size="{boy}" font-weight="700" class="g-b">{yazi}</text>')


def _rakam(x, y, t, sinif, boy=16):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{sinif}">{t}</text>'


def bolme_surdurme():
    """3 ÷ 4 (kalan 0 → biter, 0,75) ve 1 ÷ 3 (kalan hep 1 → bitmez, 0,333…) için kâğıt-kalemle bölme düzeni, yan yana."""
    Y0, ADIM = 112, 24          # ilk satırın taban çizgisi ve satır aralığı
    ic = '<line x1="235" y1="12" x2="235" y2="270" class="g-c" stroke-width="1"/>'

    def cerceve(x0, pay, payda, bolum, etiket, dolgu, giris):
        xb = x0 + 56
        s = kesir_svg(x0 + 22, 28, pay, payda, 'g-y', 15)
        s += f'<text x="{x0 + 40}" y="33" font-size="15" font-weight="700" class="g-y">= {pay} ÷ {payda}</text>'
        s += _etiket(x0 + 124, 18, 100, 22, dolgu, etiket)
        for k, satir in enumerate(giris):
            s += f'<text x="{x0 + 6}" y="{66 + 16 * k}" font-size="12" class="g-s">{satir}</text>'
        # bölme düzeni: bölünen | bölen, altında bölüm
        s += f'<line x1="{xb}" y1="96" x2="{xb}" y2="146" class="g-c" stroke-width="2"/>'
        s += f'<line x1="{xb}" y1="120" x2="{xb + 64}" y2="120" class="g-c" stroke-width="2"/>'
        s += f'<text x="{x0 + 68}" y="{Y0}" font-size="16" font-weight="700" class="g-y">{payda}</text>'
        s += f'<text x="{x0 + 68}" y="{Y0 + 28}" font-size="17" font-weight="800" class="g-mf">{bolum}</text>'
        return s

    def c(x0, k):
        return x0 + 30 + 14 * k

    def satir(x0, r, rakamlar):
        y = Y0 + ADIM * r
        return ''.join(_rakam(c(x0, k), y, t, sinif) for k, t, sinif in rakamlar)

    def cikarma(x0, r, k1, k2):
        y = Y0 + ADIM * r + 7
        return f'<line x1="{c(x0, k1) - 7}" y1="{y}" x2="{c(x0, k2) + 8}" y2="{y}" class="g-c" stroke-width="1.5"/>'

    def notu(x0, r, x, yazi, sinif='g-s'):
        return f'<text x="{x0 + x}" y="{Y0 + ADIM * r}" font-size="12" class="{sinif}">{yazi}</text>'

    # --- 3 ÷ 4: sonlu ---
    x0 = 6
    ic += cerceve(x0, '3', '4', '0,75', 'bölme biter', 'g-yf', ['3 &lt; 4: bölüme 0 yaz, virgül koy', '3’ün sağına 0 ekle: 30 ÷ 4 = 7'])
    ic += satir(x0, 0, [(0, '3', 'g-y'), (1, '0', 'g-s')])
    ic += satir(x0, 1, [(-1, '−', 'g-y'), (0, '2', 'g-y'), (1, '8', 'g-y')]) + cikarma(x0, 1, -1, 1)
    ic += satir(x0, 2, [(1, '2', 'g-tf'), (2, '0', 'g-s')]) + notu(x0, 2, 76, 'kalan 2 → 20 ÷ 4 = 5')
    ic += satir(x0, 3, [(0, '−', 'g-y'), (1, '2', 'g-y'), (2, '0', 'g-y')]) + cikarma(x0, 3, 0, 2)
    ic += satir(x0, 4, [(2, '0', 'g-yf')])
    ic += _etiket(x0 + 74, Y0 + ADIM * 4 - 15, 104, 22, 'g-yf', 'kalan 0: bitti')
    for k, yazi in enumerate(('Mavi: bölüme yazılan basamak', 'Turuncu: kalan', 'Soluk 0: eklenen sıfır')):
        ic += f'<text x="{x0 + 6}" y="{242 + 16 * k}" font-size="12" class="g-s">{yazi}</text>'

    # --- 1 ÷ 3: devirli ---
    x0 = 240
    ic += cerceve(x0, '1', '3', '0,333…', 'bölme bitmez', 'g-of', ['1 &lt; 3: bölüme 0 yaz, virgül koy', '1’in sağına 0 ekle: 10 ÷ 3 = 3'])
    ic += satir(x0, 0, [(0, '1', 'g-y'), (1, '0', 'g-s')])
    ic += satir(x0, 1, [(0, '−', 'g-y'), (1, '9', 'g-y')]) + cikarma(x0, 1, 0, 1)
    ic += satir(x0, 2, [(1, '1', 'g-tf'), (2, '0', 'g-s')]) + notu(x0, 2, 76, 'kalan 1 → 10 ÷ 3 = 3')
    ic += satir(x0, 3, [(1, '−', 'g-y'), (2, '9', 'g-y')]) + cikarma(x0, 3, 1, 2)
    ic += satir(x0, 4, [(2, '1', 'g-tf'), (3, '0', 'g-s')]) + notu(x0, 4, 90, 'kalan yine 1 → 3')
    ic += satir(x0, 5, [(2, '−', 'g-y'), (3, '9', 'g-y')]) + cikarma(x0, 5, 2, 3)
    ic += satir(x0, 6, [(3, '1', 'g-of')])
    ic += _etiket(x0 + 88, Y0 + ADIM * 6 - 15, 130, 22, 'g-of', 'aynı kalan: bitmez')
    return svg(470, 286, ic, 'Kâğıt-kalemle bölmeyi sürdürme, yan yana iki örnek. Solda 3 bölü 4: 3, 4’ten küçük olduğu için bölüme 0 yazılıp '
               'virgül konur; 3’ün sağına 0 eklenir, 30 bölü 4 eşittir 7, kalan 2; kalanın sağına 0 eklenir, 20 bölü 4 eşittir 5, kalan 0; '
               'bölme biter, sonuç 0,75. Sağda 1 bölü 3: 10 bölü 3 eşittir 3, kalan 1; kalanın sağına 0 eklenince yine 10 bölü 3 eşittir 3 '
               've kalan yine 1 olur; aynı kalan yeniden çıktığı için bölme bitmez, sonuç 0,333… Mavi rakamlar bölüm, turuncu rakamlar kalan, '
               'soluk sıfırlar kalanın sağına eklenen sıfırlardır.')


def payda_kurali():
    """Gözle → tahmin et → sına → genelle akışı; altında sonlu ve devirli çıkan paydaların asal çarpanlara ayrılmış hâli."""
    ic = '<defs>' + ok_isareti('ok6mat7b', 'g-s') + '</defs>'
    adimlar = [('Gözle', 54, 66), ('Tahmin et', 142, 90), ('Sına', 254, 60), ('Genelle', 336, 80)]
    for ad, x, w in adimlar:
        ic += _kutu(x, 14, w, 26, 'g-ma', 'g-ms', rx=13)
        ic += f'<text x="{x + w / 2:g}" y="32" text-anchor="middle" font-size="13" font-weight="800" class="g-mf">{ad}</text>'
    for x1 in (123, 235, 317):
        ic += f'<line x1="{x1}" y1="27" x2="{x1 + 14}" y2="27" class="g-c" stroke-width="2" marker-end="url(#ok6mat7b)"/>'
    # Sına'dan Tahmin et'e geri dönüş: ters örnek
    ic += '<path d="M284 40 V60 H187 V47" class="g-c" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#ok6mat7b)"/>'
    ic += '<text x="235" y="78" text-anchor="middle" font-size="12" class="g-s">ters örnek çıkarsa tahmini düzelt</text>'

    def cip(x, cy, t):
        w = 26 if len(t) > 1 else 20
        dolgu = 'g-yf' if t in ('2', '5') else 'g-of'
        s = f'<rect x="{x}" y="{cy - 9}" width="{w}" height="18" rx="5" class="{dolgu}"/>'
        s += f'<text x="{x + w / 2:g}" y="{cy + 4.5}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-b">{t}</text>'
        return s, w

    def kart(x, baslik, dolgu, acik, cizgi, yazi, gozlem, paydalar, satirlar, sonuc):
        s = f'<rect x="{x}" y="96" width="222" height="218" rx="10" class="{acik}"/>'
        s += f'<rect x="{x}" y="96" width="222" height="32" rx="10" class="{dolgu}"/><rect x="{x}" y="116" width="222" height="12" class="{dolgu}"/>'
        s += f'<text x="{x + 111}" y="117" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{baslik}</text>'
        s += f'<text x="{x + 12}" y="146" font-size="12" class="g-s">{gozlem}</text>'
        s += f'<text x="{x + 12}" y="164" font-size="13" font-weight="700" class="g-y">{paydalar}</text>'
        for k, (sayi, carpanlar) in enumerate(satirlar):
            cy = 186 + 23 * k
            s += f'<text x="{x + 54}" y="{cy + 5}" text-anchor="end" font-size="13.5" font-weight="700" class="g-y">{sayi} =</text>'
            cx = x + 62
            for j, t in enumerate(carpanlar):
                if j:
                    s += f'<text x="{cx + 8}" y="{cy + 4}" text-anchor="middle" font-size="12" class="g-s">×</text>'
                    cx += 16
                parca, w = cip(cx, cy, t)
                s += parca
                cx += w
        s += f'<text x="{x + 12}" y="304" font-size="12.5" font-weight="700" class="{yazi}">{sonuc}</text>'
        s += f'<rect x="{x}" y="96" width="222" height="218" rx="10" class="{cizgi}" stroke-width="1.8"/>'
        return s

    ic += kart(8, 'Sonlu gösterim', 'g-yf', 'g-ya', 'g-ys', 'g-yf', 'Gözle: sonlu çıkan paydalar', '2, 4, 5, 8, 10, 16, 20, 25',
               [('4', ['2', '2']), ('8', ['2', '2', '2']), ('10', ['2', '5']), ('20', ['2', '2', '5']), ('25', ['5', '5'])],
               'Genelle: yalnız 2 ve 5 → sonlu')
    ic += kart(240, 'Devirli gösterim', 'g-of', 'g-oa', 'g-os', 'g-of', 'Gözle: devirli çıkan paydalar', '3, 6, 7, 9, 11, 12, 15',
               [('6', ['2', '3']), ('12', ['2', '2', '3']), ('15', ['3', '5']), ('7', ['7']), ('11', ['11'])],
               'Genelle: başka asal → devirli')
    return svg(470, 326, ic, 'Tümevarımsal akıl yürütme adımları: gözle, tahmin et, sına, genelle; ters örnek çıkarsa tahmin düzeltilip yeniden sınanır. '
               'Altta iki kart: sonlu çıkan kesirlerin paydaları 2, 4, 5, 8, 10, 16, 20, 25; asal çarpanları 4 = 2 × 2, 8 = 2 × 2 × 2, '
               '10 = 2 × 5, 20 = 2 × 2 × 5, 25 = 5 × 5, yani yalnız 2 ve 5. Devirli çıkanların paydaları 3, 6, 7, 9, 11, 12, 15; '
               '6 = 2 × 3, 12 = 2 × 2 × 3, 15 = 3 × 5, 7 ve 11 asal; paydada 3, 7, 11 gibi başka bir asal çarpan vardır. '
               'Yeşil çarpanlar 2 ve 5, mor çarpanlar öteki asal sayılardır.')


def kurdele_paylasimi():
    """7 m kurdele 4 eşit parçaya: 7 = 4 × 1 + 3; kalan 3 m’nin her metresi 4’e bölünür; her parça 1 m + 3 × 25 cm = 1,75 m."""
    KARE, ARA = 56, 6
    ic = '<text x="8" y="20" font-size="13.5" font-weight="700" class="g-y">7 m kurdele, 4 eşit parça: 7 ÷ 4</text>'
    for k in range(7):
        x = 21 + (KARE + ARA) * k
        if k < 4:
            ic += f'<rect x="{x}" y="34" width="{KARE}" height="40" rx="6" class="g-mf"/>'
            ic += f'<text x="{x + KARE / 2:g}" y="59" text-anchor="middle" font-size="13" font-weight="700" class="g-b">1 m</text>'
        else:
            ic += _kutu(x, 34, KARE, 40, 'g-ta', 'g-ts', rx=6)
            for j in (1, 2, 3):
                ic += f'<line x1="{x + 14 * j}" y1="35" x2="{x + 14 * j}" y2="73" class="g-ts" stroke-width="1.2"/>'
    ic += '<text x="142" y="92" text-anchor="middle" font-size="12.5" font-weight="700" class="g-mf">bölüm 1: her parçaya 1 m</text>'
    ic += '<text x="359" y="92" text-anchor="middle" font-size="12.5" font-weight="700" class="g-tf">kalan 3 m: her metre 4’e bölünür</text>'
    ic += ('<text x="21" y="124" font-size="16" font-weight="700" class="g-y">7 = <tspan class="g-mf">4 × 1</tspan> + '
           '<tspan class="g-tf">3</tspan></text>')
    ic += '<text x="160" y="124" font-size="12.5" class="g-s">bölünen = bölen × bölüm + kalan</text>'
    # bir parçanın uzunluğu
    ic += '<text x="21" y="156" font-size="13" font-weight="700" class="g-y">Bir parçanın uzunluğu:</text>'
    ic += f'<rect x="21" y="166" width="{KARE}" height="40" rx="6" class="g-mf"/>'
    ic += '<text x="49" y="191" text-anchor="middle" font-size="13" font-weight="700" class="g-b">1 m</text>'
    ic += '<text x="88" y="192" text-anchor="middle" font-size="16" font-weight="700" class="g-y">+</text>'
    for x in (102, 118, 134):
        ic += _kutu(x, 166, 14, 40, 'g-ta', 'g-ts', rx=3, kalin=1.2)
    ic += '<text x="125" y="222" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">3 × 25 cm</text>'
    ic += '<text x="166" y="192" text-anchor="middle" font-size="16" font-weight="700" class="g-y">=</text>'
    ic += '<text x="180" y="192" font-size="16" font-weight="800" class="g-y">1 m 75 cm = 1,75 m</text>'
    ic += '<text x="180" y="222" font-size="12.5" class="g-s">kalan 3 →</text>'
    ic += kesir_svg(258, 218, '3', '4', 'g-tf', 13)
    ic += '<text x="272" y="222" font-size="12.5" font-weight="700" class="g-tf">= 3 ÷ 4 = 0,75</text>'
    # sonuç
    ic += kesir_svg(30, 256, '7', '4', 'g-y', 15)
    ic += '<text x="46" y="261" font-size="15" font-weight="700" class="g-y">= 7 ÷ 4 = 1 tam</text>'
    ic += kesir_svg(186, 256, '3', '4', 'g-y', 15)
    ic += '<text x="202" y="261" font-size="16" font-weight="800" class="g-y">= 1,75 m</text>'
    return svg(470, 282, ic, 'Kalanlı bölme ve paylaştırma modeli: 7 metrelik kurdele 4 eşit parçaya kesiliyor. 7 eşittir 4 çarpı 1 artı 3; '
               'her parçaya 1 tam metre düşer, kalan 3 metrenin her metresi 4 eşit şeride bölünür ve her parçaya 3 şerit, yani 3 kere 25 santimetre '
               'eşittir 75 santimetre gelir. Kalan 3’ün bölen 4’e oranı 3 bölü 4 eşittir 0,75; sonuç 7 bölü 4 eşittir 1 tam 3 bölü 4 eşittir 1,75 metre, '
               'yani 1 metre 75 santimetre. Mavi kareler bölümü, turuncu kareler kalanı gösterir.')


def uygula(o):
    g = {'Kâğıt-kalemle bölmeyi sürdürmek': bolme_surdurme(),
         'Gözle, tahmin et, sına, genelle': payda_kurali(),
         'Kalanlı bölme ve paylaştırma problemleri': kurdele_paylasimi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
