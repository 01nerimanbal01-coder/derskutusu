"""10. sınıf Felsefe, 1. hafta: Felsefenin Anlamı, Felsefi Düşüncenin Özellikleri ve Gelişimi, Felsefi Sorular (FEL.10.1.1).

Görseller yalnız MEB 10. sınıf Felsefe ders kitabındaki bilgilerle çizilir (kitap s. 16-17, 20, 24-27).
Renk anlamı: mor = felsefe / felsefi düşünme; turuncu = philia (sevgi) ve felsefenin kökleri;
mavi = sophia (bilgelik) ve pratik düşünme; yeşil = felsefeyle ilişkili kavramlar ve yaratıcı düşünme.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'mor': ('g-oa', 'g-os', 'g-of'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boy=12, sinif='g-y', kalin=False, hiza='middle'):
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _kenara(cx, cy, w, h, ux, uy):
    """Merkezi (cx, cy) olan w × h dikdörtgenin (ux, uy) yönündeki kenar noktasına uzaklık."""
    tx = (w / 2) / abs(ux) if ux else float('inf')
    ty = (h / 2) / abs(uy) if uy else float('inf')
    return min(tx, ty)


def kavram_agi():
    """philia + sophia → philosophia; felsefenin ilişkili olduğu kavramlar (kitap s. 16-17 bilgi görseli)."""
    import math
    ic = '<defs>' + ok_isareti('okF10a', 'g-of') + '</defs>'
    # üst satır: sözcüğün kökeni
    ic += _kutu(8, 8, 150, 72, 'turuncu')
    ic += _yazi(83, 32, 'philia', 14, 'g-tf', True)
    ic += _yazi(83, 52, 'sevmek, aramak,', 11.5)
    ic += _yazi(83, 68, 'peşinden gitmek', 11.5)
    ic += _yazi(172, 52, '+', 20, 'g-s', True)
    ic += _kutu(186, 8, 108, 72, 'mavi')
    ic += _yazi(240, 36, 'sophia', 14, 'g-mf', True)
    ic += _yazi(240, 58, 'bilgelik', 12)
    ic += f'<line x1="300" y1="44" x2="322" y2="44" class="g-os" stroke-width="2.5" marker-end="url(#okF10a)"/>'
    ic += _kutu(332, 8, 132, 72, 'mor')
    ic += _yazi(398, 36, 'philosophia', 14, 'g-of', True)
    ic += _yazi(398, 58, 'bilgelik sevgisi', 12, 'g-of', True)
    # alt bölüm: merkezde felsefe, çevresinde kitap görselindeki altı kavram
    hx, hy, hr = 236, 206, 52  # 52: "hakikat arayışı" alt satırı daireden taşmasın
    ic += f'<circle cx="{hx}" cy="{hy}" r="{hr}" class="g-of"/>'
    ic += _yazi(hx, hy - 2, 'FELSEFE', 14, 'g-b', True)
    ic += _yazi(hx, hy + 16, 'hakikat arayışı', 11, 'g-b')
    W, H = 148, 46
    uydular = [  # (merkez x, merkez y, ad, açıklama, renk)
        (80, 206, 'Sevgi', 'bilgelik sevgisi', 'turuncu'),
        (150, 124, 'Bilgi', 'merak ve öğrenme', 'yesil'),
        (322, 124, 'Düşünme', 'anlama ve açıklama', 'yesil'),
        (392, 206, 'Arayış', 'sürekli sorgulama', 'yesil'),
        (322, 288, 'Erdem', 'bilgiye uygun davranış', 'yesil'),
        (150, 288, 'Bilinç', 'farkındalık', 'yesil'),
    ]
    for cx, cy, ad, alt, renk in uydular:
        dx, dy = cx - hx, cy - hy
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        bas = hr + 5
        son = L - _kenara(cx, cy, W, H, ux, uy) - 5
        ic += (f'<line x1="{hx + ux * bas:.1f}" y1="{hy + uy * bas:.1f}" x2="{hx + ux * son:.1f}" y2="{hy + uy * son:.1f}" '
               f'class="g-c" stroke-width="2" stroke-linecap="round"/>')
        _, _, f = RENK[renk]
        ic += _kutu(cx - W / 2, cy - H / 2, W, H, renk, rx=10)
        ic += _yazi(cx, cy - 3, ad, 13, f, True)
        ic += _yazi(cx, cy + 14, alt, 11)
    return svg(472, 320, ic, 'Felsefe sözcüğü Yunanca philia (sevmek, aramak, peşinden gitmek) ile sophia (bilgelik) kelimelerinin birleşmesinden oluşan philosophia teriminden gelir; anlamı bilgelik sevgisidir. Felsefe; sevgi (bilgelik sevgisi), bilgi (merak ve öğrenme), düşünme (anlama ve açıklama), arayış (sürekli sorgulama), erdem (bilgiye uygun davranış) ve bilinç (farkındalık) kavramlarıyla ilişkilidir.')


def dusunme_bicimleri():
    """Pratik, yaratıcı, eleştirel ve felsefi düşünme; kitaptaki örneklerle (kitap s. 20)."""
    ic = _yazi(236, 20, 'Düşünmenin tek bir yolu yoktur.', 13, 'g-y', True)
    kartlar = [
        (8, 'mavi', 'Pratik düşünme', ('Yağmuru gören kişi', 'yanına şemsiye alır.')),
        (162, 'yesil', 'Yaratıcı düşünme', ('Balıkçı, tekne zarar', 'görmesin diye yanına', 'eski lastikler asar.')),
        (316, 'turuncu', 'Eleştirel düşünme', ('Bilgisayar alan kişi', 'reklamı ve yorumları', 'sorgulayarak seçer.')),
    ]
    for x, renk, ad, satirlar in kartlar:
        _, _, f = RENK[renk]
        ic += _kutu(x, 34, 148, 112, renk)
        ic += _yazi(x + 74, 58, ad, 12.5, f, True)
        for k, s in enumerate(satirlar):
            ic += _yazi(x + 74, 84 + k * 18, s, 11.5)
    ic += _yazi(236, 174, 'Felsefi düşünme bu biçimlerin hepsinden ayrılır:', 12.5, 'g-of', True)
    ic += _kutu(8, 186, 456, 156, 'mor')
    ic += _yazi(236, 212, 'Felsefi düşünme', 14, 'g-of', True)
    ic += _yazi(236, 234, 'Varlığı, bilgiyi ve değerleri akıl ve mantık ilkelerine', 12)
    ic += _yazi(236, 252, 'dayanıp bütüncül biçimde kavrar ve temellendirir.', 12)
    ornek = ('Örnek: “Gerçeklik nedir?” sorusunu temellendirmek',
             'Örnek: Özgürlük ile sorumluluk ilişkisini çözümlemek')
    for k, s in enumerate(ornek):
        yy = 278 + k * 20
        ic += f'<circle cx="42" cy="{yy - 4}" r="3.5" class="g-of"/>' + _yazi(52, yy, s, 12, hiza='start')
    # sorgulamanın dört niteliği (kitap s. 20: sistemli, tutarlı, şüpheci, kapsamlı)
    for k, s in enumerate(('sistemli', 'tutarlı', 'şüpheci', 'kapsamlı')):
        x = 44 + k * 100
        ic += f'<rect x="{x}" y="{314}" width="84" height="20" rx="10" class="g-of"/>'
        ic += _yazi(x + 42, 328, s, 11.5, 'g-b', True)
    return svg(472, 350, ic, 'Düşünmenin tek bir yolu yoktur. Pratik düşünme: yağmuru gören kişi yanına şemsiye alır. Yaratıcı düşünme: balıkçı tekne zarar görmesin diye yanına eski lastikler asar. Eleştirel düşünme: bilgisayar alan kişi reklamı ve yorumları sorgulayarak seçer. Felsefi düşünme bunlardan ayrılır: varlığı, bilgiyi ve değerleri akıl ve mantık ilkelerine dayanıp bütüncül biçimde kavrar ve temellendirir; sistemli, tutarlı, şüpheci ve kapsamlı bir sorgulamadır. Örnekler: Gerçeklik nedir sorusunu temellendirmek, özgürlük ile sorumluluk ilişkisini çözümlemek.')


def zaman_seridi():
    """Felsefi düşüncenin gelişimi: kökler ve beş dönem (kitap s. 24-27)."""
    # kalın zaman çizgisinin ok ucu küçük tutulur (işaret çizgi kalınlığıyla büyür); dolgu mor
    ic = ('<defs><marker id="okF10b" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="3.6" markerHeight="3.6" orient="auto">'
          '<path d="M0 0L10 5L0 10z" class="g-of"/></marker></defs>')
    # kökler (turuncu)
    ic += _kutu(8, 8, 456, 58, 'turuncu')
    ic += _yazi(236, 31, 'Temeller: Çin, Hindistan, İran, Mısır, Mezopotamya', 12.5, 'g-tf', True)
    ic += _yazi(236, 52, 'Yazıyla artan bilgi birikimi felsefenin doğuşuna zemin hazırlar.', 11.5)
    donemler = [
        (('MÖ 6. yüzyıl –', 'MS 2. yüzyıl'),
         ('Yunan, Çin ve Hint felsefeleri gelişir.', 'Çin ve Hint’te ahlak ile inanç bağlanır.',
          'Yunan’da evren ve doğa olayları sorgulanır.')),
        (('MS 2. yüzyıl –', '15. yüzyıl'),
         ('Felsefe dinlerle etkileşir.', 'Tanrı ve inanç konuları merkeze yerleşir.',
          'İslam felsefesinin birikimi Batı’ya geçer.')),
        (('15. yüzyıl –', '17. yüzyıl'),
         ('Kilisenin otoritesi sarsılır.', 'Akla güven artar, hümanizm ortaya çıkar.',
          'Modern bilim doğar.')),
        (('18. yüzyıl –', '19. yüzyıl'),
         ('İnsan kendi aklıyla yaşamını düzenler.', 'Gelenekler ve siyasi otoriteler eleştirilir.',
          'Düşünce ve ifade özgürlüğü yaygınlaşır.')),
        (('20. yüzyıl',),
         ('Felsefi sorunlara yeni yaklaşımlar gelişir.', 'Disiplinler arası sınırlar belirginleşir.',
          'Birçok felsefi ekol ortaya çıkar.')),
    ]
    X_CIZGI, Y0, ADIM, H = 148, 84, 72, 60
    son_y = Y0 + (len(donemler) - 1) * ADIM + H / 2
    # dikey zaman çizgisi: köklerden 20. yüzyıla, aşağı doğru oklu
    ic += (f'<line x1="{X_CIZGI}" y1="70" x2="{X_CIZGI}" y2="{son_y + 26:.0f}" class="g-os" stroke-width="3" '
           f'stroke-linecap="round" marker-end="url(#okF10b)"/>')
    for i, (etiket, satirlar) in enumerate(donemler):
        y = Y0 + i * ADIM
        orta = y + H / 2
        ic += f'<rect x="6" y="{orta - 23:.0f}" width="128" height="46" rx="23" class="g-of"/>'
        if len(etiket) == 2:
            ic += _yazi(70, orta - 4, etiket[0], 12, 'g-b', True) + _yazi(70, orta + 13, etiket[1], 12, 'g-b', True)
        else:
            ic += _yazi(70, orta + 4, etiket[0], 12.5, 'g-b', True)
        ic += f'<circle cx="{X_CIZGI}" cy="{orta:.0f}" r="7" class="g-of"/>'
        ic += _kutu(160, y, 306, H, 'mor', rx=10)
        for k, s in enumerate(satirlar):
            ic += _yazi(172, y + 18 + k * 17, s, 11.5, hiza='start')
    return svg(472, int(son_y + 40), ic, 'Felsefi düşüncenin gelişimi. Temeller: Çin, Hindistan, İran, Mısır ve Mezopotamya medeniyetleri; yazıyla artan bilgi birikimi felsefenin doğuşuna zemin hazırlar. MÖ 6. yüzyıl ile MS 2. yüzyıl arası: Yunan, Çin ve Hint felsefeleri gelişir; Çin ve Hint’te ahlak ile inanç bağlanır; Yunan’da evren ve doğa olayları sorgulanır. MS 2. ile 15. yüzyıl arası: felsefe dinlerle etkileşir, Tanrı ve inanç konuları merkeze yerleşir, İslam felsefesinin birikimi Batı’ya geçer. 15. ile 17. yüzyıl arası: kilisenin otoritesi sarsılır, akla güven artar, hümanizm ortaya çıkar, modern bilim doğar. 18. ile 19. yüzyıl arası: insan kendi aklıyla yaşamını düzenler, gelenekler ve siyasi otoriteler eleştirilir, düşünce ve ifade özgürlüğü yaygınlaşır. 20. yüzyıl: felsefi sorunlara yeni yaklaşımlar gelişir, disiplinler arası sınırlar belirginleşir, birçok felsefi ekol ortaya çıkar.')


def uygula(o):
    g = {'Felsefenin anlamı': kavram_agi(),
         'Felsefi düşüncenin özellikleri': dusunme_bicimleri(),
         'Felsefi düşüncenin gelişimi': zaman_seridi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
