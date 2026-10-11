"""6. sınıf Sosyal Bilgiler, 3. hafta: kültürel bağlar ve millî değerler.

Görseller yalnız MEB 6. sınıf Sosyal Bilgiler ders kitabındaki bilgilerle çizilir (kitap s. 24-37).
Renk anlamı: mavi = kültürel bağlar / limandaki adımlar / yardım eden kişi, turuncu = millî değerler /
Ankara yolundaki halk / bakkal, yeşil = toplumsal birlik / sonuç adımları. İnsan figürü kullanılmaz.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="1.5"/>')


def _metin(x, y, t, boyut=12.5, agirlik=None, sinif='g-y', ankor=None):
    a = f' text-anchor="{ankor}"' if ankor else ''
    g = f' font-weight="{agirlik}"' if agirlik else ''
    return f'<text x="{x}" y="{y}"{a} font-size="{boyut}"{g} class="{sinif}">{t}</text>'


def kavram_haritasi():
    """Kültürel bağlar ve millî değerler → toplumsal birlik (kavram haritası)."""
    ic = '<defs>' + ok_isareti('okS63a', 'g-s') + '</defs>'
    # sol sütun: kültürel bağlar (mavi)
    ic += '<rect x="8" y="8" width="128" height="26" rx="8" class="g-mf"/>'
    ic += _metin(72, 26, 'Kültürel bağlar', 12.5, 800, 'g-b', 'middle')
    for i, ad in enumerate(['Gelenek-görenek', 'Sanat', 'Tarih', 'Din', 'Dil']):
        y = 42 + i * 41
        ic += _kutu(8, y, 128, 34, 'mavi', rx=8)
        ic += _metin(72, y + 22, ad, 12.5, 700, 'g-y', 'middle')
    # sağ sütun: millî değerler (turuncu)
    ic += '<rect x="268" y="8" width="196" height="26" rx="8" class="g-tf"/>'
    ic += _metin(366, 26, 'Millî değerler', 12.5, 800, 'g-b', 'middle')
    degerler = ['Bağımsızlık', 'Özgürlük', 'Vatanseverlik', 'Millet sevgisi', 'Adalet', 'Dürüstlük', 'Hoşgörü', 'Saygı',
                'Aile birliğine önem verme']
    for i, ad in enumerate(degerler):
        y = 42 + i * 22
        ic += f'<rect x="268" y="{y}" width="196" height="20" rx="10" class="g-ta"/>'
        ic += _metin(366, y + 14.5, ad, 12, None, 'g-y', 'middle')
    # sütunlar arası ok ve açıklama
    ic += '<line x1="140" y1="139" x2="262" y2="139" class="g-c" stroke-width="2" marker-end="url(#okS63a)"/>'
    ic += _metin(201, 130, 'değer doğurur', 12, None, 'g-s', 'middle')
    ic += _metin(201, 157, 'kuşaktan kuşağa', 12, None, 'g-s', 'middle')
    ic += _metin(201, 172, 'taşınır', 12, None, 'g-s', 'middle')
    # alt kutu: toplumsal birlik (yeşil)
    ic += _kutu(8, 262, 456, 34, 'yesil')
    ic += _metin(236, 284, 'Toplumsal birlik ve beraberlik', 13, 800, 'g-y', 'middle')
    ic += '<line x1="72" y1="244" x2="72" y2="258" class="g-c" stroke-width="2" marker-end="url(#okS63a)"/>'
    ic += '<line x1="366" y1="242" x2="366" y2="258" class="g-c" stroke-width="2" marker-end="url(#okS63a)"/>'
    return svg(472, 304, ic, 'Kavram haritası: kültürel bağlar (gelenek-görenek, sanat, tarih, din, dil) toplumda değerler doğurur ve bu değerler '
               'kuşaktan kuşağa taşınır. Millî değerler: bağımsızlık, özgürlük, vatanseverlik, millet sevgisi, adalet, dürüstlük, hoşgörü, saygı, '
               'aile birliğine önem verme. Hem kültürel bağlar hem millî değerler toplumsal birlik ve beraberliğe ulaşır.')


def tore_degerleri():
    """Orhun Abideleri ve Kutadgu Bilig'de işlenen dört değer: terim → anlamı (kitap s. 27)."""
    ic = '<defs>' + ok_isareti('okS63b', 'g-s') + '</defs>'
    ic += _metin(236, 18, 'Orhun Abideleri ve Kutadgu Bilig’de işlenen dört değer', 13, 800, 'g-y', 'middle')
    ic += '<rect x="8" y="30" width="170" height="26" rx="8" class="g-mf"/>'
    ic += _metin(93, 48, 'Töre değeri', 12.5, 800, 'g-b', 'middle')
    ic += '<rect x="214" y="30" width="250" height="26" rx="8" class="g-yf"/>'
    ic += _metin(339, 48, 'Anlamı', 12.5, 800, 'g-b', 'middle')
    satirlar = [('könilik', 'adalet'), ('kişilik', 'insanlık ve hoşgörü'), ('tüzlük', 'eşitlik'),
                ('uzluk', 'iyilik ve faydalılık')]
    for i, (terim, anlam) in enumerate(satirlar):
        y = 64 + i * 42
        ic += _kutu(8, y, 170, 34, 'mavi', rx=8)
        ic += _metin(93, y + 22, terim, 14, 800, 'g-y', 'middle')
        ic += f'<line x1="182" y1="{y + 17}" x2="208" y2="{y + 17}" class="g-c" stroke-width="2" marker-end="url(#okS63b)"/>'
        ic += _kutu(214, y, 250, 34, 'yesil', rx=8)
        ic += _metin(339, y + 22, anlam, 13, 700, 'g-y', 'middle')
    return svg(472, 232, ic, 'Türk töresinin dört değeri: könilik adalet demektir, kişilik insanlık ve hoşgörü, tüzlük eşitlik, '
               'uzluk iyilik ve faydalılık demektir. Bu değerler Orhun Abideleri ve Kutadgu Bilig incelendiğinde görülür.')


def istiklal_yolu():
    """İstiklal Yolu: İnebolu'dan Ankara'ya silah ve cephane (kitap s. 30)."""
    ic = '<defs>' + ok_isareti('okS63c', 'g-s') + '</defs>'
    ic += _metin(8, 18, 'İstiklal Yolu: İnebolu’dan Ankara’ya', 13, 800, 'g-y')
    adim = [('mavi', 'İnebolu Limanı’na silah ve cephane ulaşır', 'Liman, Anadolu’nun en güvenli noktalarından biridir'),
            ('mavi', 'Demirciler ve kayıkçılar yükü limandan karaya taşır', 'Millî Mücadele’nin başarısı için bu yük gereklidir'),
            ('turuncu', 'Kastamonu halkının kadınları, yaşlıları ve çocukları', 'yükü Ankara’ya ulaştırır; yolun adı İstiklal Yolu’dur'),
            ('yesil', 'Kadın, çocuk ve kayıkçılar İstiklal Madalyası ile', 'onurlandırılır (11 Şubat 1924)')]
    for i, (renk, s1, s2) in enumerate(adim):
        y = 30 + i * 68
        ic += _kutu(8, y, 456, 48, renk)
        ic += f'<circle cx="32" cy="{y + 24}" r="12" class="{RENK[renk][2]}"/>'
        ic += _metin(32, y + 29, str(i + 1), 12.5, 800, 'g-b', 'middle')
        ic += _metin(54, y + 20, s1, 12.5, 700, 'g-y')
        ic += _metin(54, y + 38, s2, 12.5, None, 'g-y')
        if i < 3:
            ic += f'<line x1="236" y1="{y + 51}" x2="236" y2="{y + 63}" class="g-c" stroke-width="2" marker-end="url(#okS63c)"/>'
    for cx, renk, t in [(16, 'mavi', 'Limanda'), (110, 'turuncu', 'Ankara yolunda'), (262, 'yesil', 'Sonuç')]:
        ic += f'<circle cx="{cx}" cy="298" r="6" class="{RENK[renk][2]}"/>'
        ic += _metin(cx + 12, 302, t, 12, None, 'g-y')
    return svg(472, 312, ic, 'İstiklal Yolu: 1 İnebolu Limanı’na silah ve cephane ulaşır, 2 demirciler ve kayıkçılar yükü limandan karaya taşır, '
               '3 Kastamonu halkının kadınları, yaşlıları ve çocukları yükü Ankara’ya ulaştırır, 4 kadın, çocuk ve kayıkçılar '
               'İstiklal Madalyası ile onurlandırılır, tarih 11 Şubat 1924.')


def zimem_defteri():
    """Zimem defteri geleneğinin adımları (kitap s. 32), yılan düzeninde."""
    ic = '<defs>' + ok_isareti('okS63d', 'g-s') + '</defs>'
    kutu = [(8, 8, 'mavi', 'Yardım eden kişi', ['ramazanda bakkala gelir', 've zimem defterini sorar']),
            (264, 8, 'turuncu', 'Bakkal', ['zimem defterini çıkarır']),
            (264, 140, 'mavi', 'Yardım eden kişi', ['sayfaların bir kısmını', 'ya da hepsini satın alır']),
            (8, 140, 'yesil', 'Sonuç', ['Borçlar kapanır;', 'bakkalın önündeki yazı', 'bunu duyurur'])]
    for i, (x, y, renk, bas, satir) in enumerate(kutu):
        ic += _kutu(x, y, 200, 100, renk)
        ic += f'<circle cx="{x + 22}" cy="{y + 22}" r="11" class="{RENK[renk][2]}"/>'
        ic += _metin(x + 22, y + 27, str(i + 1), 12.5, 800, 'g-b', 'middle')
        ic += _metin(x + 40, y + 27, bas, 12.5, 800, 'g-y')
        for k, t in enumerate(satir):
            ic += _metin(x + 14, y + 54 + k * 18, t, 12, None, 'g-y')
    ic += '<line x1="212" y1="58" x2="258" y2="58" class="g-c" stroke-width="2" marker-end="url(#okS63d)"/>'
    ic += '<line x1="364" y1="112" x2="364" y2="134" class="g-c" stroke-width="2" marker-end="url(#okS63d)"/>'
    ic += '<line x1="260" y1="190" x2="214" y2="190" class="g-c" stroke-width="2" marker-end="url(#okS63d)"/>'
    for cx, renk, t in [(16, 'mavi', 'Yardım eden kişi'), (150, 'turuncu', 'Bakkal'), (250, 'yesil', 'Sonuç')]:
        ic += f'<circle cx="{cx}" cy="262" r="6" class="{RENK[renk][2]}"/>'
        ic += _metin(cx + 12, 266, t, 12, None, 'g-y')
    return svg(472, 276, ic, 'Zimem defteri geleneği: 1 yardım eden kişi ramazanda bakkala gelip zimem defterini sorar, 2 bakkal defteri çıkarır, '
               '3 yardım eden kişi sayfaların bir kısmını ya da hepsini satın alır, 4 borçlar kapanır ve bakkalın önündeki yazı bunu duyurur.')


def uygula(o):
    g = {'Dil: değerleri taşıyan bağ': tore_degerleri(),
         'Tarih ve sanat': istiklal_yolu(),
         'Gelenek-görenek ile bayramlar': zimem_defteri(),
         'Zor günlerde birlik ve bilgiyi yeniden ifade etme': kavram_haritasi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
