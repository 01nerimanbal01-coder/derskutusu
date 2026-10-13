"""7. sınıf Matematik, 7. hafta: rasyonel sayılarla işlemler ve problem çözme (dört adım, problemi temsile dönüştürme,
işlem önceliği, çözümü kontrol etme).

Görseller yalnız özet metnindeki (araclar/ozetler/7-matematik-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: yeşil = bulunan / doğrulanan sonuç (bütün görsellerde). Dört adım şemasında mavi = çözüm adımı, turuncu = problem metni
(verilenler). Temsil görselinde turuncu = sola (negatif) adım, mavi = sağa (pozitif) adım, gri = eksen ve başlangıç noktası; şerit
modelinde yeşil = 3/4 m'yi oluşturan parçalar. İşlem önceliği görselinde mavi = öncelik sırası, turuncu = önce yapılan işlem.
Kontrol şemasında mavi = tahmin, turuncu = tersten işlem, mor = farklı strateji (üç ayrı kontrol yolu).
Ölçek: dalgıç sayı doğrusunda 1 m = 20 uzunluk (iki doğru aynı ölçekte); şerit modelinde 1 m = 400 uzunluk, 8 eş parça;
diğer şemalar ölçeksizdir.
"""
from ozet_gorsel import svg, ok_isareti, kesir_svg

EKSI = '−'

# yazı genişliği kestirimi (em): dar / geniş karakterler; diğerleri rakam .65, büyük harf .74, küçük harf .60
_EM = {'1': .43, EKSI: .68, '+': .68, '=': .68, '÷': .68, '≈': .68, '·': .33, ':': .33, ',': .33, '.': .33, ';': .34, '(': .38, ')': .38,
       ' ': .24, '°': .46, '→': .95, '✓': .88, '?': .56, '!': .34, '’': .31, 'ı': .27, 'i': .27, 'l': .27, 'j': .28, 'f': .37, 't': .34,
       'r': .42, 'm': .91, 'w': .85, 'I': .28, 'İ': .28, 'M': .93, 'W': 1.06, 'C': .74, 'Ç': .74}


def _gen(metin, boy, kalin=700):
    k = 1.0 if kalin >= 700 else 0.96
    return sum(_EM.get(c, .65 if c.isdigit() else (.74 if c.isupper() else .60)) for c in metin) * boy * k


def _kutu(x, y, w, h, dolgu, cizgi, rx=10, kalin=1.8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{dolgu}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cizgi}" stroke-width="{kalin}"/>')


def _ok_ucu(x, y, yon, sinif='g-s'):
    """Sayı doğrusu ucu (dolu üçgen): yon = 1 sağa, -1 sola. x ok ucunun (tepe) yeridir."""
    return f'<path d="M{x - 10 * yon} {y - 5.5} L{x} {y} L{x - 10 * yon} {y + 5.5}z" class="{sinif}"/>'


def _satir(x, y, parcalar, boy=14, hiza='start', kalin=700):
    """Yazı ve kesirleri tek satırda dizer. parcalar: ('y', metin[, sinif]) yazı | ('k', pay, payda[, sinif[, isaret]]) kesir.
    y kesir çizgisinin hizasıdır; yazı taban çizgisi y + 0,35·boy. hiza: start | middle | end.
    Döndürür (svg, toplam genişlik, [(x_bas, x_son), …])."""
    PAD = 5
    genis = []
    for p in parcalar:
        if p[0] == 'y':
            genis.append(_gen(p[1], boy, kalin))
        else:
            g = max(len(p[1]), len(p[2])) * boy * 0.62 + 6
            isaret = p[4] if len(p) > 4 else ''
            genis.append(PAD + (_gen(isaret, boy) + 3 if isaret else 0) + g + PAD)
    toplam = sum(genis)
    cx = x - toplam / 2 if hiza == 'middle' else (x - toplam if hiza == 'end' else x)
    ic, konum = '', []
    for p, g in zip(parcalar, genis):
        if p[0] == 'y':
            sinif = p[2] if len(p) > 2 else 'g-y'
            ic += (f'<text x="{cx:.1f}" y="{y + boy * 0.35:.1f}" font-size="{boy}" font-weight="{kalin}" class="{sinif}">{p[1]}</text>')
        else:
            sinif = p[3] if len(p) > 3 else 'g-y'
            isaret = p[4] if len(p) > 4 else ''
            gk = max(len(p[1]), len(p[2])) * boy * 0.62 + 6
            ic += kesir_svg(round(cx + g - PAD - gk / 2, 1), y, p[1], p[2], sinif, boy, isaret)
        konum.append((cx, cx + g))
        cx += g
    return ic, toplam, konum


def dort_adim():
    """Sıcaklık problemi dört adımda: anla → plan yap → uygula → kontrol et (−3,5 + 6 − 4,5 = −2)."""
    ic = '<defs>' + ok_isareti('ok7mat7a', 'g-mf') + '</defs>'
    ic += _kutu(8, 6, 444, 50, 'g-ta', 'g-ts', rx=12)
    ic += ('<text x="230" y="26" text-anchor="middle" font-size="13" class="g-y">Problem: Sabah −3,5 °C. Öğlene kadar 6 °C artıyor,</text>'
           '<text x="230" y="45" text-anchor="middle" font-size="13" class="g-y">akşama kadar 4,5 °C düşüyor. Akşam kaç °C?</text>')
    adimlar = [
        ('1. Anla', [('Verilenler: −3,5 (sabah), +6 (artış), −4,5 (düşüş)', 'g-y', 400), ('İstenen: akşam sıcaklığı', 'g-y', 400)]),
        ('2. Plan yap', [('Önce artışı ekle, sonra düşüşü çıkar:', 'g-y', 400), ('−3,5 + 6 − 4,5', 'g-y', 700)]),
        ('3. Uygula', [('−3,5 + 6 = 2,5', 'g-y', 700), ('2,5 − 4,5 = −2 → akşam sıcaklığı −2 °C', 'g-yf', 700)]),
        ('4. Kontrol et', [('Tersten: −2 + 4,5 = 2,5 ve 2,5 − 6 = −3,5 <tspan font-weight="800" class="g-yf">✓</tspan>', 'g-y', 400),
                           ('Makul: artış − düşüş = 1,5 → −3,5 + 1,5 = −2 <tspan font-weight="800" class="g-yf">✓</tspan>', 'g-y', 400)]),
    ]
    for i, (ad, satirlar) in enumerate(adimlar):
        y0 = 66 + i * 64
        ic += f'<rect x="8" y="{y0}" width="100" height="46" rx="12" class="g-mf"/>'
        ic += f'<text x="58" y="{y0 + 28}" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{ad}</text>'
        ic += _kutu(118, y0, 334, 46, 'g-z', 'g-c', rx=10, kalin=1.5)
        for j, (yazi, sinif, kalin) in enumerate(satirlar):
            ic += f'<text x="128" y="{y0 + 19 + j * 18}" font-size="12.5" font-weight="{kalin}" class="{sinif}">{yazi}</text>'
        if i < 3:
            ic += f'<line x1="58" y1="{y0 + 49}" x2="58" y2="{y0 + 58}" class="g-ms" stroke-width="2" marker-end="url(#ok7mat7a)"/>'
    return svg(460, 312, ic, 'Problem çözmenin dört adımı sıcaklık problemiyle. Problem: sabah eksi 3,5 santigrat derece; öğlene kadar 6 derece artış, '
               'akşama kadar 4,5 derece düşüş. 1. Anla: verilenler eksi 3,5, artı 6 ve eksi 4,5; istenen akşam sıcaklığı. 2. Plan yap: önce artışı ekle, '
               'sonra düşüşü çıkar. 3. Uygula: eksi 3,5 artı 6 eşittir 2,5; 2,5 eksi 4,5 eşittir eksi 2; akşam sıcaklığı eksi 2 derece. '
               '4. Kontrol et: tersten eksi 2 artı 4,5 eşittir 2,5 ve 2,5 eksi 6 eşittir eksi 3,5, başlangıca dönüldü; sonuç makul, '
               'çünkü artış düşüşten 1,5 büyük ve eksi 3,5 artı 1,5 eşittir eksi 2.')


def temsil():
    """Dalgıç problemi iki sayı doğrusunda (−12 + (−7) = −19, −19 + 4 = −15; 1 m = 20 uzunluk) ve kurdele problemi şerit modelinde
    (1 m = 8 eş parça, 3/4 m = 6 parça; 3/4 ÷ 1/8 = 6)."""
    u = 20

    def X(v):
        return 430 + u * v

    ic = '<defs>' + ok_isareti('ok7mat7b', 'g-tf') + ok_isareti('ok7mat7c', 'g-mf') + '</defs>'
    ic += '<text x="230" y="13" text-anchor="middle" font-size="13" font-weight="700" class="g-y">Dalgıç: −12 m’den 7 m iner, sonra 4 m yükselir</text>'
    satirlar = [(74, -12, -19, 'g-tf', 'g-ts', 'ok7mat7b', EKSI + '7: 7 birim sola', f'{EKSI}12 + ({EKSI}7) = {EKSI}19'),
                (156, -19, -15, 'g-mf', 'g-ms', 'ok7mat7c', '+4: 4 birim sağa', f'{EKSI}19 + 4 = {EKSI}15')]
    for y, bas, son, dolgu, cizgi, ok, etiket, ifade in satirlar:
        ic += f'<line x1="18" y1="{y}" x2="442" y2="{y}" class="g-c" stroke-width="2.5" stroke-linecap="round"/>' + _ok_ucu(452, y, 1) + _ok_ucu(8, y, -1)
        for v in range(-20, 1):
            x = X(v)
            kalin = v % 5 == 0
            ic += f'<line x1="{x}" y1="{y - (6 if kalin else 4)}" x2="{x}" y2="{y + (6 if kalin else 4)}" class="g-c" stroke-width="{2 if kalin else 1.3}"/>'
            if kalin:
                ic += f'<text x="{x}" y="{y + 21}" text-anchor="middle" font-size="12" class="g-s">{"0 (yüzey)" if v == 0 else EKSI + str(-v)}</text>'
        xb, xs = X(bas), X(son)
        xm = (xb + xs) / 2
        yon = 1 if xs > xb else -1
        ic += f'<path d="M{xb} {y - 8} Q{xm:g} {y - 60} {xs} {y - 12}" class="{cizgi}" stroke-width="2.2" marker-end="url(#{ok})"/>'
        ic += f'<text x="{xm:g}" y="{y - 42}" text-anchor="middle" font-size="13" font-weight="700" class="{dolgu}">{etiket}</text>'
        ic += f'<text x="442" y="{y - 42}" text-anchor="end" font-size="14" font-weight="700" class="g-y">{ifade}</text>'
        ic += f'<circle cx="{xb}" cy="{y}" r="5" class="g-s"/><circle cx="{xs}" cy="{y}" r="5.5" class="{dolgu}"/>'
        # başlangıç etiketi sıçramanın ters yönünde, bitiş etiketi ark ucunun dışında (ikisi de doğrunun üstünde)
        ic += (f'<text x="{xb - 8 * yon}" y="{y - 11}" text-anchor="{"end" if yon > 0 else "start"}" font-size="13" font-weight="700" class="g-y">'
               f'{EKSI}{-bas}</text>')
        ic += (f'<text x="{xs + 8 * yon}" y="{y - 11}" text-anchor="{"start" if yon > 0 else "end"}" font-size="13" font-weight="700" class="{dolgu}">'
               f'{EKSI}{-son}</text>')
    # şerit modeli: 1 m = 8 eş parça; 3/4 m = 6 parça
    sy = 234
    for k in range(8):
        x = 30 + 50 * k
        secili = k < 6
        ic += _kutu(x, sy, 50, 36, 'g-ya' if secili else 'g-z', 'g-ys' if secili else 'g-c', rx=4, kalin=1.5)
        ic += kesir_svg(x + 25, sy + 18, '1', '8', 'g-yf' if secili else 'g-s', 12)
    ic += f'<path d="M30 {sy - 4} v-6 H330 v6" class="g-ys" stroke-width="1.8"/>'
    ic += _satir(180, sy - 30, [('k', '3', '4', 'g-yf'), ('y', 'm = 6 parça (şerit modeli)', 'g-yf')], 13, 'middle')[0]
    ic += f'<path d="M30 {sy + 40} v6 H430 v-6" class="g-c" stroke-width="1.8"/>'
    ic += f'<text x="230" y="{sy + 66}" text-anchor="middle" font-size="12.5" class="g-s">1 m = 8 eş parça</text>'
    ic += _satir(230, sy + 92, [('k', '3', '4'), ('y', '÷'), ('k', '1', '8'), ('y', '='), ('k', '3', '4'), ('y', '· 8 ='),
                                ('k', '24', '4'), ('y', '= 6', 'g-yf')], 14, 'middle')[0]
    return svg(460, 352, ic, 'Problemi temsile dönüştürme. Üstte dalgıç problemi iki sayı doğrusunda: birinci doğruda eksi 12’den 7 birim sola gidilir, '
               'eksi 12 artı eksi 7 eşittir eksi 19; ikinci doğruda eksi 19’dan 4 birim sağa gidilir, eksi 19 artı 4 eşittir eksi 15; '
               'sola gitmek negatif, sağa gitmek pozitif sayı eklemektir. Altta şerit modeli: 1 metrelik şerit 8 eş parçaya bölünmüş, '
               '3 bölü 4 metre bu parçalardan 6’sına denk gelir; 3 bölü 4 bölü 1 bölü 8 eşittir 3 bölü 4 çarpı 8 eşittir 24 bölü 4 eşittir 6.')


def oncelik():
    """İşlem önceliği sırası ve ayracın yerinin sonucu değiştirmesi: 2 − 3/4 · (−8/9) = 8/3, (2 − 3/4) · (−8/9) = −10/9."""
    ic = '<defs>' + ok_isareti('ok7mat7d', 'g-mf') + '</defs>'
    basamak = [('1. Ayraç içi', 'kesir çizgisi dahil'), ('2. Çarpma', 've bölme'), ('3. Toplama', 've çıkarma')]
    for i, (ust, alt) in enumerate(basamak):
        x = 8 + i * 156
        ic += f'<rect x="{x}" y="8" width="132" height="44" rx="10" class="g-mf"/>'
        ic += f'<text x="{x + 66}" y="{8 + 19}" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{ust}</text>'
        ic += f'<text x="{x + 66}" y="{8 + 36}" text-anchor="middle" font-size="12" class="g-b">{alt}</text>'
        if i < 2:
            ic += f'<line x1="{x + 142}" y1="30" x2="{x + 150}" y2="30" class="g-ms" stroke-width="2.5" marker-end="url(#ok7mat7d)"/>'
    ic += '<text x="230" y="70" text-anchor="middle" font-size="12.5" class="g-s">Aynı öncelikteki işlemler soldan sağa yapılır.</text>'
    kartlar = [
        (8, 'Ayraç yok: önce çarpma', [
            ([('y', '2 −'), ('k', '3', '4'), ('y', '· (−'), ('k', '8', '9'), ('y', ')')], (1, 4)),
            ([('y', '= 2 − (−'), ('k', '2', '3'), ('y', ')')], None),
            ([('y', '= 2 +'), ('k', '2', '3'), ('y', '='), ('k', '8', '3', 'g-yf')], None)]),
        (234, 'Ayraçlı: önce ayraç içi', [
            ([('y', '(2 −'), ('k', '3', '4'), ('y', ') '), ('y', '· (−'), ('k', '8', '9'), ('y', ')')], (0, 2)),
            ([('y', '='), ('k', '5', '4'), ('y', '· (−'), ('k', '8', '9'), ('y', ')')], None),
            ([('y', '= −'), ('k', '40', '36'), ('y', '='), ('k', '10', '9', 'g-yf', EKSI)], None)]),
    ]
    ky = 82
    for x, baslik, satirlar in kartlar:
        ic += _kutu(x, ky, 218, 148, 'g-z', 'g-c', rx=12, kalin=1.5)
        ic += f'<text x="{x + 109}" y="{ky + 20}" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{baslik}</text>'
        for j, (parcalar, vurgu) in enumerate(satirlar):
            c = ky + 48 + j * 36
            s, _, konum = _satir(x + 109, c, parcalar, 14, 'middle')
            if vurgu:
                a, b = konum[vurgu[0]][0] - 2, konum[vurgu[1]][1] + 2
                ic += _kutu(round(a, 1), c - 18, round(b - a, 1), 37, 'g-ta', 'g-ts', rx=7, kalin=1.5)
            ic += s
    ic += _kutu(10, 240, 14, 12, 'g-ta', 'g-ts', rx=3, kalin=1.5)
    ic += '<text x="30" y="250" font-size="12.5" class="g-s">önce yapılan işlem</text>'
    ic += _satir(452, 246, [('y', 'Ayracın yeri sonucu değiştirir: '), ('k', '8', '3', 'g-yf'), ('y', 'ile'), ('k', '10', '9', 'g-yf', EKSI),
                            ('y', 'farklıdır')], 13, 'end', 400)[0]
    return svg(460, 272, ic, 'İşlem önceliği: önce ayraç içi (kesir çizgisi dahil), sonra çarpma ve bölme, en son toplama ve çıkarma; aynı öncelikteki '
               'işlemler soldan sağa yapılır. Ayraç yokken 2 eksi 3 bölü 4 çarpı eksi 8 bölü 9 işleminde önce çarpma yapılır: eşittir 2 eksi eksi 2 bölü 3 '
               'eşittir 2 artı 2 bölü 3 eşittir 8 bölü 3. Ayraçlı yazılışta önce ayraç içi hesaplanır: 2 eksi 3 bölü 4 eşittir 5 bölü 4; '
               '5 bölü 4 çarpı eksi 8 bölü 9 eşittir eksi 40 bölü 36 eşittir eksi 10 bölü 9. Ayracın yeri sonucu değiştirir.')


def kontrol():
    """Sonucu kontrol etme şeması: anlam kontrolü, sonra tahmin, tersten işlem ve farklı strateji (metindeki üç örnekle)."""
    ic = '<defs>' + ok_isareti('ok7mat7e', 'g-s') + '</defs>'
    ic += _kutu(60, 8, 360, 48, 'g-z', 'g-c', rx=12, kalin=1.5)
    ic += ('<text x="240" y="27" text-anchor="middle" font-size="13.5" font-weight="700" class="g-y">Sonuç anlamlı mı? Uzunluk negatif olamaz,</text>'
           '<text x="240" y="46" text-anchor="middle" font-size="12.5" class="g-s">sıcaklık, derinlik ve bakiye negatif olabilir.</text>')
    ic += '<line x1="240" y1="57" x2="240" y2="68" class="g-c" stroke-width="2"/><line x1="84" y1="68" x2="396" y2="68" class="g-c" stroke-width="2"/>'
    for cx in (84, 240, 396):
        ic += f'<line x1="{cx}" y1="68" x2="{cx}" y2="78" class="g-c" stroke-width="2" marker-end="url(#ok7mat7e)"/>'
    ky = 84
    sutunlar = [
        (8, 'g-ma', 'g-ms', 'g-mf', '1. Tahmin et', [
            ([('y', '45 ·'), ('k', '7', '4'), ('y', '≈ 45 · 2 = 90')], 700, 12.5),
            ([('y', '78,75 → makul', 'g-yf')], 700, 12.5),
            ([('y', '787,5 → virgül hatası', 'g-s')], 400, 12)]),
        (164, 'g-ta', 'g-ts', 'g-tf', '2. Tersten yap', [
            ([('y', '12 ÷'), ('k', '2', '5'), ('y', '= 30')], 700, 12.5),
            ([('y', '30 ·'), ('k', '2', '5'), ('y', '= 12 ✓')], 700, 12.5),
            ([('y', 'sağlama tuttu', 'g-yf')], 700, 12.5)]),
        (320, 'g-oa', 'g-os', 'g-of', '3. Başka yol dene', [
            ([('k', '21', '4'), ('y', '÷'), ('k', '3', '4'), ('y', '= 7')], 700, 12.5),
            ([('y', '5,25 ÷ 0,75 = 7')], 700, 12.5),
            ([('y', 'iki yol da 7 ✓', 'g-yf')], 700, 12.5)]),
    ]
    for x, dolgu, cizgi, vurgu, baslik, satirlar in sutunlar:
        ic += _kutu(x, ky, 152, 140, dolgu, cizgi, rx=12)
        ic += f'<text x="{x + 76}" y="{ky + 22}" text-anchor="middle" font-size="13.5" font-weight="800" class="{vurgu}">{baslik}</text>'
        for j, (parcalar, kalin, boy) in enumerate(satirlar):
            ic += _satir(x + 76, ky + 50 + j * 33, parcalar, boy, 'middle', kalin)[0]
    ic += _kutu(8, 236, 464, 32, 'g-ya', 'g-ys', rx=10)
    ic += '<text x="240" y="257" text-anchor="middle" font-size="13" font-weight="700" class="g-yf">Farklı yollar aynı sonucu veriyorsa çözüm doğrudur.</text>'
    return svg(480, 276, ic, 'Çözümü kontrol etme şeması. Önce anlam kontrolü: uzunluk negatif olamaz; sıcaklık, derinlik ve bakiye negatif olabilir. '
               'Sonra üç yol: 1. Tahmin et: 45 çarpı 7 bölü 4 yaklaşık 45 çarpı 2 eşittir 90; 78,75 makul, 787,5 virgül hatası. '
               '2. Tersten yap: 12 bölü 2 bölü 5 eşittir 30; sağlama 30 çarpı 2 bölü 5 eşittir 12. '
               '3. Başka yol dene: 21 bölü 4 bölü 3 bölü 4 eşittir 7 ve 5,25 bölü 0,75 eşittir 7, iki yol da 7 verir. '
               'Farklı yollar aynı sonucu veriyorsa çözüm doğrudur.')


def uygula(o):
    g = {'Problem çözmenin dört adımı': dort_adim(),
         'Problemi temsile dönüştürmek': temsil(),
         'Çok adımlı işlemler ve işlem önceliği': oncelik(),
         'Çözümü kontrol etmek, farklı yollar ve genelleme': kontrol()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
