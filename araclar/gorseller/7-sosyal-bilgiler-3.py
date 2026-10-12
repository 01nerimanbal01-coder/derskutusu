"""7. sınıf Sosyal Bilgiler, 3. hafta: özel gereksinimli bireyler için fırsat eşitliği (kitap s. 30-34).

Renk anlamı: mor = ana kavram, mavi = güçlük alanları / birey / alan adı, turuncu = toplum,
yeşil = özel yetenek / uygulama / destekleyen değerler. İnsan figürü kullanılmaz.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {'mavi': ('g-ma', 'g-ms', 'g-mf'), 'turuncu': ('g-ta', 'g-ts', 'g-tf'),
        'yesil': ('g-ya', 'g-ys', 'g-yf'), 'mor': ('g-oa', 'g-os', 'g-of')}


def _kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="1.5"/>')


def _m(x, y, t, boyut=12.5, agirlik=None, sinif='g-y', ankor=None):
    a = f' text-anchor="{ankor}"' if ankor else ''
    g = f' font-weight="{agirlik}"' if agirlik else ''
    return f'<text x="{x}" y="{y}"{a} font-size="{boyut}"{g} class="{sinif}">{t}</text>'


def kapsam():
    """Özel gereksinimli bireylerin kapsamı: yedi grup ve takip şeridi örneği (kitap s. 33)."""
    ic = '<defs>' + ok_isareti('okSB73a', 'g-s') + '</defs>'
    ic += _kutu(8, 76, 140, 124, 'mor', 14)
    ic += _m(78, 108, 'Özel gereksinimli', 13, 800, 'g-of', 'middle')
    ic += _m(78, 126, 'birey', 13, 800, 'g-of', 'middle')
    ic += _m(78, 152, 'Ek destek ve', 11.5, None, 'g-y', 'middle')
    ic += _m(78, 168, 'eğitime gereksinim', 11.5, None, 'g-y', 'middle')
    ic += _m(78, 184, 'duyar', 11.5, None, 'g-y', 'middle')
    gruplar = [('mavi', ['Görme yetersizliği']), ('mavi', ['İşitme yetersizliği']), ('mavi', ['Bedensel yetersizlik']),
               ('mavi', ['Dil ve konuşma bozukluğu']), ('mavi', ['Dikkat eksikliği ve hiperaktivite']),
               ('mavi', ['Öğrenme güçlüğü']), ('yesil', ['Özel yetenekli'])]
    y = 12
    for i, (renk, satir) in enumerate(gruplar):
        h = 34 if len(satir) == 2 else 30
        ic += _kutu(196, y, 268, h, renk, 15)
        if len(satir) == 2:
            ic += _m(210, y + 15, satir[0], 12, 700)
            ic += _m(210, y + 29, satir[1], 12, 700)
        else:
            ic += _m(210, y + 20, satir[0], 12.5, 700)
        ic += f'<line x1="152" y1="138" x2="190" y2="{y + h / 2:.1f}" class="g-c" stroke-width="1.5" marker-end="url(#okSB73a)"/>'
        y += h + 6
    ic += _m(8, 286, 'Takip şeridi, görme yetersizliği olanların', 12, None, 'g-s')
    ic += _m(8, 302, 'kaldırımda güvenle ilerlemesini kolaylaştırır.', 12, None, 'g-s')
    ic += '<circle cx="346" cy="282" r="6" class="g-ma"/><circle cx="346" cy="282" r="6" class="g-ms" stroke-width="1.5"/>'
    ic += _m(358, 286, 'güçlük alanı', 12)
    ic += '<circle cx="346" cy="300" r="6" class="g-ya"/><circle cx="346" cy="300" r="6" class="g-ys" stroke-width="1.5"/>'
    ic += _m(358, 304, 'özel yetenek', 12)
    return svg(472, 312, ic, 'Özel gereksinimli birey, yaşıtlarından ayrı ihtiyaçları olan ve ek destek ve eğitime gereksinim duyan kişidir. '
               'Kapsamında görme yetersizliği, işitme yetersizliği, bedensel yetersizlik, dil ve konuşma bozukluğu, dikkat eksikliği ve '
               'hiperaktivite, öğrenme güçlüğü ve özel yetenekli bireyler bulunur. Takip şeridi, görme yetersizliği olan bireylerin '
               'kaldırımda güvenle ilerlemesini kolaylaştırır.')


def birey_toplum():
    """Fırsat eşitliğinin birey ve toplum için yararı (kitap s. 33)."""
    ic = '<defs>' + ok_isareti('okSB73b', 'g-s') + '</defs>'
    ic += _kutu(156, 8, 160, 34, 'mor', 17)
    ic += _m(236, 30, 'Fırsat eşitliği', 14, 800, 'g-of', 'middle')
    ic += '<line x1="210" y1="46" x2="124" y2="68" class="g-c" stroke-width="2" marker-end="url(#okSB73b)"/>'
    ic += '<line x1="262" y1="46" x2="348" y2="68" class="g-c" stroke-width="2" marker-end="url(#okSB73b)"/>'
    ic += '<rect x="16" y="74" width="212" height="28" rx="8" class="g-mf"/>'
    ic += _m(122, 93, 'Birey için', 13, 800, 'g-b', 'middle')
    ic += '<rect x="244" y="74" width="212" height="28" rx="8" class="g-tf"/>'
    ic += _m(350, 93, 'Toplum için', 13, 800, 'g-b', 'middle')
    birey = ['Yeteneklerini geliştirir', 'Hayallerine ulaşabilir', 'Kendini değerli hisseder', 'Öz güveni artar', 'Geleceğe umutla bakar']
    toplum = ['Adalet ve barış hâkim olur', 'Etkin katılımla güçlenir', 'Huzura kavuşur', 'Gelişmesine katkı sağlanır']
    for i, t in enumerate(birey):
        y = 110 + i * 34
        ic += _kutu(16, y, 212, 28, 'mavi', 14)
        ic += _m(30, y + 19, t, 12.5)
    for i, t in enumerate(toplum):
        y = 110 + i * 34
        ic += _kutu(244, y, 212, 28, 'turuncu', 14)
        ic += _m(258, y + 19, t, 12.5)
    ic += _kutu(244, 246, 212, 34, 'yesil', 10)
    ic += _m(350, 260, 'Sevgi, şefkat, anlayış ve', 11.5, 700, 'g-y', 'middle')
    ic += _m(350, 274, 'merhamet bu yararı destekler', 11.5, 700, 'g-y', 'middle')
    return svg(472, 292, ic, 'Fırsat eşitliği birey için yeteneklerini geliştirmeyi, hayallere ulaşabilmeyi, kendini değerli hissetmeyi, öz güveni '
               'artırmayı ve geleceğe umutla bakmayı sağlar. Toplum için adalet ve barış ortamı, etkin katılımla güçlenme, huzur ve gelişme '
               'sağlar. Sevgi, şefkat, anlayış ve merhamet bu yararı destekler.')


def guvence():
    """Hakların yasal güvencesi: alan → uygulama (kitap s. 34)."""
    ic = '<defs>' + ok_isareti('okSB73c', 'g-s') + '</defs>'
    ic += _kutu(116, 8, 240, 34, 'mor', 17)
    ic += _m(236, 30, 'Hakların yasal güvencesi', 14, 800, 'g-of', 'middle')
    satirlar = [(['Eğitim'], ['Kaynaştırma/bütünleştirme', 'uygulamaları; bireyselleştirilmiş', 'eğitim programları'], 64),
                (['Kamu binaları', 've ulaşım'], ['Erişilebilirlik düzenlemeleri'], 44),
                (['Sağlık'], ['Sağlık hizmetlerine kolay ulaşım'], 44),
                (['Sosyal yaşam'], ['Destekleyici hizmetler'], 44)]
    y = 56
    for alan, uyg, h in satirlar:
        orta = y + h / 2
        ic += _kutu(8, y, 164, h, 'mavi')
        if len(alan) == 2:
            ic += _m(90, orta - 2, alan[0], 12.5, 800, 'g-mf', 'middle')
            ic += _m(90, orta + 14, alan[1], 12.5, 800, 'g-mf', 'middle')
        else:
            ic += _m(90, orta + 5, alan[0], 13, 800, 'g-mf', 'middle')
        ic += f'<line x1="176" y1="{orta:.1f}" x2="202" y2="{orta:.1f}" class="g-c" stroke-width="2" marker-end="url(#okSB73c)"/>'
        ic += _kutu(208, y, 256, h, 'yesil')
        if len(uyg) == 3:
            for k, t in enumerate(uyg):
                ic += _m(222, y + 19 + k * 17, t, 11.5)
        else:
            ic += _m(222, orta + 5, uyg[0], 12.5)
        y += h + 10
    ic += _m(236, 302, 'Engelli araç park yeri bu eşitliği günlük yaşama taşır.', 12, None, 'g-s', 'middle')
    return svg(472, 312, ic, 'Özel gereksinimli bireylerin hakları yasalarla güvence altındadır. Eğitimde kaynaştırma ve bütünleştirme '
               'uygulamaları ile bireyselleştirilmiş eğitim programları, kamu binalarında ve ulaşımda erişilebilirlik düzenlemeleri, '
               'sağlıkta hizmetlere kolay ulaşım, sosyal yaşamda destekleyici hizmetler bu güvencenin uygulamalarıdır.')


def uygula(o):
    g = {'Özel gereksinimli birey kimdir?': kapsam(),
         'Fırsat eşitliği neden önemlidir?': birey_toplum(),
         'Hakların güvencesi ve erişilebilirlik': guvence()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
