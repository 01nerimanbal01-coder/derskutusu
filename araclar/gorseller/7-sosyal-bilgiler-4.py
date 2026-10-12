"""7. sınıf Sosyal Bilgiler, 4. hafta: fırsat eşitliği için yapılan çalışmalar ve fikir üretme (kitap s. 35-39).

Renk anlamı: mor = ana kavram / kurum, mavi, turuncu ve yeşil = ayrı hizmet, girişim ya da bölüm.
İnsan figürü kullanılmaz.
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


def hizmetler():
    """Aile ve Sosyal Hizmetler Bakanlığı'nın dört hizmeti (kitap s. 35)."""
    ic = '<rect x="86" y="8" width="300" height="34" rx="17" class="g-z"/><rect x="86" y="8" width="300" height="34" rx="17" class="g-c" stroke-width="2.5"/>'
    ic += _m(236, 30, 'Aile ve Sosyal Hizmetler Bakanlığı', 13.5, 800, 'g-y', 'middle')
    kartlar = [(8, 54, 'mavi', 'Umut Evleri', ['Toplumsal yaşama katılım', 'Günlük yaşam becerileri', 'Bağımsız yaşam']),
               (242, 54, 'turuncu', 'Gündüz bakım merkezleri', ['Aile bireylerine zaman ve', 'sosyal yaşama katılım;', 'bireye öz bakım desteği']),
               (8, 156, 'yesil', 'Geçici ve Misafir Bakım', ['Aile yanında olamayınca', '(hac, umre, sağlık, seyahat)', 'yatılı bakım sağlar']),
               (242, 156, 'mor', 'Özel bakım merkezleri', ['Devamlı bakım ve desteğe', 'gereksinimi olanlara', 'profesyonel bakım verir'])]
    for x, y, renk, bas, satir in kartlar:
        ic += _kutu(x, y, 222, 92, renk)
        ic += _m(x + 14, y + 24, bas, 13, 800, RENK[renk][2])
        for k, t in enumerate(satir):
            ic += _m(x + 14, y + 46 + k * 17, t, 12)
    ic += _m(236, 268, 'Dört hizmet de bireylerin yaşam kalitesini artırmayı amaçlar.', 12, None, 'g-s', 'middle')
    return svg(472, 280, ic, 'Aile ve Sosyal Hizmetler Bakanlığı dört hizmet sunar: Umut Evleri toplumsal yaşama katılım, günlük yaşam becerileri ve '
               'bağımsız yaşam amaçlar; gündüz bakım merkezleri aile bireylerine zaman ve sosyal yaşama katılım, bireye öz bakım desteği sağlar; '
               'Geçici ve Misafir Bakım ailelerin yanında olamadığı dönemlerde yatılı bakım verir; özel bakım merkezleri devamlı bakım ve desteğe '
               'gereksinimi olanlara profesyonel bakım verir.')


def girisimler():
    """Dört girişim ve ortak amaç (kitap s. 35-36)."""
    ic = '<defs>' + ok_isareti('okSB74a', 'g-s') + '</defs>'
    satir = [('mavi', 'Kastamonu', 'Sen de Gel: atlı terapi'),
             ('turuncu', 'Fethiye', 'Engelsiz plaj, kısa mola merkezi'),
             ('yesil', 'Millî Eğitim Bakanlığı', 'Eğitimde Engel Yok'),
             ('mor', 'Karabük', 'Evde bakım hizmeti')]
    for i, (renk, yer, ad) in enumerate(satir):
        y = 10 + i * 62
        ic += _kutu(8, y, 258, 52, renk)
        ic += _m(22, y + 22, yer, 13, 800, RENK[renk][2])
        ic += _m(22, y + 41, ad, 12)
        ic += f'<line x1="270" y1="{y + 26}" x2="306" y2="{y + 26}" class="g-c" stroke-width="2" marker-end="url(#okSB74a)"/>'
    ic += '<rect x="312" y="10" width="152" height="238" rx="14" class="g-z"/>'
    ic += '<rect x="312" y="10" width="152" height="238" rx="14" class="g-c" stroke-width="2.5"/>'
    ic += _m(388, 40, 'Ortak amaç', 14, 800, 'g-y', 'middle')
    for k, t in enumerate(['Bireylerin yaşamını', 'kolaylaştırmak;', 'toplumsal hayata', 'etkin ve güvenli', 'katılımlarına', 'yardım etmek']):
        ic += _m(388, 74 + k * 20, t, 12.5, None, 'g-y', 'middle')
    return svg(472, 258, ic, 'Dört çalışma ortak bir amaca ulaşır: Kastamonu’da Sen de Gel atlı terapi projesi, Fethiye’de engelsiz plaj ve kısa mola '
               'merkezi, Millî Eğitim Bakanlığı’nın Eğitimde Engel Yok çalışmaları, Karabük’te evde bakım hizmeti. Ortak amaç, özel gereksinimli '
               'bireylerin yaşamını kolaylaştırmak ve toplumsal hayata etkin ve güvenli katılımlarına yardım etmektir.')


def beyin_eseri():
    """Beyin eseri tekniği: beş alan ve altı adım (kitap s. 37)."""
    ic = '<defs>' + ok_isareti('okSB74b', 'g-s') + '</defs>'
    ic += _m(236, 18, 'Fikir üretilen beş alan', 13, 800, 'g-y', 'middle')
    alanlar = ['Eğitim', 'Sağlık', 'Ulaşım', 'İstihdam', 'Sosyal yaşama katılım']
    gen = [62, 62, 66, 76, 166]
    x = 8
    for t, w in zip(alanlar, gen):
        ic += f'<rect x="{x}" y="28" width="{w}" height="28" rx="14" class="g-ma"/><rect x="{x}" y="28" width="{w}" height="28" rx="14" class="g-ms" stroke-width="1.5"/>'
        ic += _m(x + w / 2, 47, t, 12, 700, 'g-mf', 'middle')
        x += w + 6
    adimlar = [('turuncu', 'Her alana ait kâğıda fikirler yazılır'), ('turuncu', 'Kâğıtlar ters çevrilerek bırakılır'),
               ('turuncu', 'Seçilen kâğıttaki öneriler sesli okunur'), ('turuncu', 'Benzer fikirler gruplandırılır'),
               ('yesil', 'En özgün öneriler belirlenir'), ('yesil', 'Öneriler ürün dosyasında saklanır')]
    for i, (renk, t) in enumerate(adimlar):
        y = 72 + i * 38
        ic += _kutu(8, y, 456, 30, renk, 15)
        ic += f'<circle cx="28" cy="{y + 15}" r="10" class="{RENK[renk][2]}"/>'
        ic += _m(28, y + 19.5, str(i + 1), 12, 800, 'g-b', 'middle')
        ic += _m(48, y + 20, t, 12.5)
        if i < 5:
            ic += f'<line x1="28" y1="{y + 31}" x2="28" y2="{y + 37}" class="g-c" stroke-width="1.2" marker-end="url(#okSB74b)"/>'
    ic += '<circle cx="14" cy="304" r="6" class="g-tf"/>'
    ic += _m(26, 308, 'fikirleri toplama ve düzenleme', 12)
    ic += '<circle cx="262" cy="304" r="6" class="g-yf"/>'
    ic += _m(274, 308, 'sonuç', 12)
    return svg(472, 320, ic, 'Beyin eseri tekniğinde fikirler eğitim, sağlık, ulaşım, istihdam ve sosyal yaşama katılım alanları için üretilir. Altı adım: '
               '1 her alana ait kâğıda fikirler yazılır, 2 kâğıtlar ters çevrilerek bırakılır, 3 seçilen kâğıttaki öneriler sesli okunur, '
               '4 benzer fikirler gruplandırılır, 5 en özgün öneriler belirlenir, 6 öneriler ürün dosyasında saklanır.')


def taslak():
    """Proje taslağının üç bölümü (kitap s. 38-39)."""
    ic = ''
    kolonlar = [(8, 128, 'mavi', 'Ekip', ['Grubun adı', 'Görevli öğrenciler']),
                (144, 144, 'turuncu', 'Projenin kimliği', ['Projenin adı', 'Amacı', 'Yeri', 'Tarihi', 'Süresi', 'Yararlanacak kişiler']),
                (296, 168, 'yesil', 'Uygulama', ['İzlenecek adımlar', 'Kaynaklar', 'Sonuç ve değerlendirme'])]
    for x, gen, renk, bas, ogeler in kolonlar:
        ic += f'<rect x="{x}" y="10" width="{gen}" height="30" rx="8" class="{RENK[renk][2]}"/>'
        ic += _m(x + gen / 2, 30, bas, 13, 800, 'g-b', 'middle')
        for i, t in enumerate(ogeler):
            y = 50 + i * 36
            ic += _kutu(x, y, gen, 30, renk, 15)
            ic += _m(x + gen / 2, y + 20, t, 12, 700, 'g-y', 'middle')
    ic += _m(236, 284, 'Proje, bütüncül dereceli puanlama anahtarıyla değerlendirilir.', 12, None, 'g-s', 'middle')
    return svg(472, 296, ic, 'Proje taslağı üç bölümden oluşur. Ekip: grubun adı ve görevli öğrenciler. Projenin kimliği: projenin adı, amacı, yeri, tarihi, '
               'süresi ve yararlanacak kişiler. Uygulama: izlenecek adımlar, kaynaklar, sonuç ve değerlendirme.')


def uygula(o):
    g = {'Fırsat eşitliği için yapılan çalışmalar': hizmetler(),
         'Ortak amaç ve değerler': girisimler(),
         'Fikir üretme: beyin eseri tekniği': beyin_eseri(),
         'Fikri projeye dönüştürmek': taslak()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
