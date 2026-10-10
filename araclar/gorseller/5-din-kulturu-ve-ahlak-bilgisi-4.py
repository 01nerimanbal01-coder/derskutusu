"""5. sınıf Din Kültürü ve Ahlak Bilgisi, 4. hafta: Allah’ın güzel isimleri, Rahman ile Rahîm, besmele.

Görseller yalnız MEB 5. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap PDF s. 30-33).
Renk anlamı: Rahman = mavi, Rahîm = turuncu (her görselde aynı), ortak yön ve besmele = yeşil; kaynak = mavi,
öğrenme = yeşil, kullanma = turuncu; günlük durumlar nötr (yüzey rengi).
Çizimlerde ölçü yoktur; yalnız ilişkiler gösterilir.
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


def _nötr(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _satirlar(cx, ilk_y, aralik, satirlar, boyut=12, kalin=False, sinif='g-y'):
    agirlik = ' font-weight="700"' if kalin else ''
    return ''.join(f'<text x="{cx:g}" y="{ilk_y + i * aralik:g}" text-anchor="middle" font-size="{boyut}"{agirlik} class="{sinif}">{t}</text>'
                   for i, t in enumerate(satirlar))


def kaynaktan_dua_etmeye():
    """Kaynak → öğrenme → kullanma (kitap s. 30): Kur’an ve hadisler; yücelik, merhamet, adalet; anmak ve dua etmek."""
    ic = '<defs>' + ok_isareti('okD4kay', 'g-s') + '</defs>'
    for x, ad in [(8, 'Kaynak'), (178, 'Öğrenme'), (348, 'Kullanma')]:
        ic += f'<text x="{x + 70}" y="18" text-anchor="middle" font-size="12" font-weight="700" class="g-s">{ad}</text>'
    ic += _kutu(8, 28, 140, 86, 'mavi') + _satirlar(78, 68, 18, ['Kur’an-ı Kerim', 've hadisler'], 13, True, 'g-mf')
    ic += _kutu(178, 28, 140, 86, 'yesil') + _satirlar(248, 60, 17, ['Yücelik, merhamet', 've adalet daha', 'iyi kavranır'])
    ic += _kutu(348, 28, 140, 86, 'turuncu') + _satirlar(418, 60, 17, ['Güzel isimlerle', 'anmak ve', 'dua etmek'])
    for x1, x2 in [(152, 174), (322, 344)]:
        ic += f'<line x1="{x1}" y1="71" x2="{x2}" y2="71" class="g-c" stroke-width="2" marker-end="url(#okD4kay)"/>'
    return svg(496, 124, ic, 'Kur’an-ı Kerim ve hadisler, güzel isimlerin kaynağıdır. Bu isimleri öğrenince Allah’ın yüceliği, merhameti ve '
               'adaleti daha iyi kavranır. Allah güzel isimleriyle anılır ve bu isimlerle dua edilir.')


def rahman_rahim():
    """Rahman ile Rahîm’in karşılaştırılması (kitap s. 32): iki isim, ortak yön merhamet."""
    ic = ''
    for x, renk, ad in [(8, 'mavi', 'Rahman'), (248, 'turuncu', 'Rahîm')]:
        ic += f'<rect x="{x}" y="8" width="224" height="32" rx="16" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{x + 112}" y="30" text-anchor="middle" font-size="15" font-weight="800" class="g-b">{ad}</text>'
    rahman = [['Bütün varlıklara', 'şefkat gösterir'], ['İnsanlar arasında ayrım', 'yapmadan merhamet eder'],
              ['Nimetleri sürekli verir'], ['Rahmeti sonsuzdur']]
    rahim = [['Karşılık beklemeden', 'nimet verir'], ['Varlıkları korur, esirger', 've bağışlar'],
             ['Ahirette inanan kullara', 'şefkat edip ödüllendirir'], ['İyilik yapanlara ahirette', 'özel ikramda bulunur']]
    for i in range(4):
        y = 48 + i * 46
        for x, renk, satir in [(8, 'mavi', rahman[i]), (248, 'turuncu', rahim[i])]:
            ic += _kutu(x, y, 224, 40, renk, 10)
            if len(satir) == 1:
                ic += _satirlar(x + 112, y + 25, 17, satir)
            else:
                ic += _satirlar(x + 112, y + 15, 17, satir)
    ic += _kutu(8, 234, 464, 30, 'yesil', 15)
    ic += '<text x="240" y="254" text-anchor="middle" font-size="12.5" class="g-y">İkisi de merhameti anlatır ve birlikte anılır.</text>'
    return svg(480, 272, ic, 'Rahman: bütün varlıklara şefkat gösterir, insanlar arasında ayrım yapmadan merhamet eder, nimetleri sürekli verir, '
               'rahmeti sonsuzdur. Rahîm: karşılık beklemeden nimet verir, varlıkları korur, esirger ve bağışlar, ahirette inanan kullara '
               'şefkat edip ödüllendirir, iyilik yapanlara ahirette özel ikramda bulunur. İkisi de merhameti anlatır ve birlikte anılır.')


def besmele_akisi():
    """Besmele çekilen durumlar → besmele → Rahman ve Rahîm (kitap s. 32-33)."""
    ic = '<defs>' + ok_isareti('okD4bes', 'g-s') + '</defs>'
    durum = [(12, ['Sofraya', 'otururken']), (66, ['Ders çalışmaya', 'başlarken']), (120, ['Yeni bir işe', 'girişirken'])]
    for y, satir in durum:
        ic += _nötr(8, y, 116, 44) + _satirlar(66, y + 19, 17, satir)
    for y1, y2 in [(34, 70), (88, 88), (142, 106)]:
        ic += f'<line x1="128" y1="{y1}" x2="164" y2="{y2}" class="g-c" stroke-width="2" marker-end="url(#okD4bes)"/>'
    ic += _kutu(170, 56, 100, 64, 'yesil') + _satirlar(220, 84, 18, ['Besmele', 'çekmek'], 14, True, 'g-yf')
    for y1, y2 in [(76, 48), (100, 116)]:
        ic += f'<line x1="274" y1="{y1}" x2="296" y2="{y2}" class="g-c" stroke-width="2" marker-end="url(#okD4bes)"/>'
    ic += _kutu(300, 14, 212, 62, 'mavi')
    ic += _satirlar(406, 34, 17, ['Rahman'], 13, True, 'g-mf') + _satirlar(406, 52, 15, ['bütün varlıklara', 'merhamet eden'])
    ic += _kutu(300, 84, 212, 62, 'turuncu')
    ic += _satirlar(406, 104, 17, ['Rahîm'], 13, True, 'g-tf')
    ic += _satirlar(406, 122, 15, ['iyilik yapanlara özel', 'ikram sunan'])
    ic += '<text x="260" y="184" text-anchor="middle" font-size="12.5" class="g-y">Her işe şefkat ve merhametle yaklaşmayı hatırlatır.</text>'
    return svg(520, 196, ic, 'Besmele: sofraya otururken, ders çalışmaya başlarken ya da yeni bir işe girişirken çekilir. Besmelede Rahman ve Rahîm '
               'isimleri vardır: Rahman bütün varlıklara merhamet eden, Rahîm iyilik yapanlara özel ikram sunan Allah’ı hatırlatır. '
               'Besmele her işe şefkat ve merhametle yaklaşmayı hatırlatır.')


def uygula(o):
    g = {'Güzel isimleri nereden öğrenir, nasıl anarız?': kaynaktan_dua_etmeye(),
         'Rahîm: iyilik yapanlara özel ikram': rahman_rahim(),
         'Besmele: Rahman ve Rahîm’i hatırlamak': besmele_akisi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
