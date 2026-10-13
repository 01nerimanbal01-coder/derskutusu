"""6. sınıf Peygamberimizin Hayatı, 2. hafta: vefa, aile hayatı ve adil tutum.

Görseller yalnız MEB 6. sınıf Peygamberimizin Hayatı ders kitabındaki bilgilerle çizilir (kitap s. 15-20).
Renk anlamı: mavi = olayın adımları ve oğulları, turuncu = kızları, yeşil = örnek alınan tutum,
gri = sessiz kalınca yaşananlar (kitabın Kontrol Noktası'ndaki takım).
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


def _gri(x, y, w, h, rx=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boy=12.5, sinif='g-y', kalin=False, hiza='middle'):
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def soze_baglilik():
    """Kitap s. 15: Abdullah bin Ebu Hamsa olayı; üç gün sonra aynı yerde bekleyen Hz. Muhammed."""
    ic = '<defs>' + ok_isareti('okPH62a', 'g-s') + '</defs>'
    adim = [('1. Söz verilir', ['Borçlu genç:', '“Biraz bekle,', 'hemen getireyim.”']),
            ('2. Söz unutulur', ['Genç sözünü', 'unutur.', 'Üç gün geçer.']),
            ('3. Aynı yerde', ['Hz. Muhammed', 'sözleşilen yerde', 'bekliyor.'])]
    for k, (baslik, satir) in enumerate(adim):
        x = 8 + k * 158
        ic += _yazi(x + 70, 20, baslik, 12.5, 'g-s', kalin=True)
        ic += _kutu(x, 30, 140, 80, 'mavi')
        y0 = 70 - (len(satir) - 1) * 9
        for j, s in enumerate(satir):
            ic += _yazi(x + 70, y0 + j * 18 + 4, s, 12.5, 'g-mf', kalin=(j == 0))
        if k < 2:
            ic += (f'<line x1="{x + 142}" y1="70" x2="{x + 156}" y2="70" class="g-c" stroke-width="2" '
                   f'marker-end="url(#okPH62a)"/>')
    ic += _yazi(236, 136, '“Ey delikanlı! Bana zahmet verdin,', 12.5, 'g-y')
    ic += _yazi(236, 154, 'seni bunca zamandır burada bekliyorum.”', 12.5, 'g-y')
    for k, ad in enumerate(('vefalı', 'dürüst', 'anlayışlı')):
        x = 8 + k * 158
        ic += _kutu(x, 168, 140, 34, 'yesil', rx=10)
        ic += _yazi(x + 70, 190, ad, 13, 'g-yf', kalin=True)
    return svg(472, 210, ic, 'Söze bağlılık: 1. Borçlu genç biraz beklemesini, borcunu hemen getireceğini söyler. 2. Sözünü unutur, '
               'üç gün geçer. 3. Döndüğünde Hz. Muhammed sözleşilen yerde beklemektedir ve yalnızca “Ey delikanlı! Bana '
               'zahmet verdin, seni bunca zamandır burada bekliyorum.” der. Olay onun vefalı, dürüst ve anlayışlı '
               'olduğunu gösterir.')


def cocuklari():
    """Kitap s. 16-17: Hz. Hatice'den altı çocuk; Ebülkasım künyesi; Zeyneb adının anlamı; Hz. Mariye'den İbrahim."""
    ic = _kutu(96, 10, 120, 36, 'mavi', rx=10)
    ic += _yazi(156, 33, 'Hz. Muhammed', 12.5, 'g-mf', kalin=True)
    ic += _kutu(256, 10, 120, 36, 'turuncu', rx=10)
    ic += _yazi(316, 33, 'Hz. Hatice', 12.5, 'g-tf', kalin=True)
    ic += '<line x1="216" y1="28" x2="256" y2="28" class="g-c" stroke-width="2"/>'
    ic += '<line x1="236" y1="28" x2="236" y2="62" class="g-c" stroke-width="2"/>'
    ic += '<line x1="93" y1="62" x2="327" y2="62" class="g-c" stroke-width="2"/>'
    ic += '<line x1="93" y1="62" x2="93" y2="76" class="g-c" stroke-width="2"/>'
    ic += '<line x1="327" y1="62" x2="327" y2="76" class="g-c" stroke-width="2"/>'
    ic += _kutu(8, 76, 170, 100, 'mavi')
    ic += _yazi(93, 96, 'Oğulları', 12.5, 'g-mf', kalin=True)
    ic += _yazi(93, 120, 'Kasım', 14, kalin=True)
    ic += _yazi(93, 142, 'Abdullah', 14, kalin=True)
    ic += _yazi(93, 164, 'küçük yaşta vefat etti', 12, 'g-mf')
    ic += _kutu(190, 76, 274, 100, 'turuncu')
    ic += _yazi(327, 96, 'Kızları', 12.5, 'g-tf', kalin=True)
    for k, ad in enumerate(('Zeyneb', 'Rukiye', 'Ümmü Gülsüm', 'Fatıma (en son)')):
        ic += _yazi(258 + (k % 2) * 138, 124 + (k // 2) * 30, ad, 14, kalin=True)
    ic += _gri(8, 186, 456, 52, rx=10)
    ic += _yazi(20, 207, 'Ebülkasım: “Kasım’ın babası”', 12.5, 'g-y', hiza='start')
    ic += _yazi(452, 207, 'Zeyneb: “babasının süsü”', 12.5, 'g-y', hiza='end')
    ic += _yazi(236, 228, 'Hz. Mariye’den olan oğlu İbrahim de bebekken vefat etti.', 12, 'g-s')
    return svg(472, 246, ic, 'Hz. Muhammed ile Hz. Hatice’nin altı çocuğu: oğulları Kasım ve Abdullah küçük yaşta vefat etti; '
               'kızları Zeyneb, Rukiye, Ümmü Gülsüm ve en son dünyaya gelen Fatıma. Ebülkasım “Kasım’ın babası”, '
               'Zeyneb “babasının süsü” demektir. Hz. Mariye’den olan oğlu İbrahim de bebekken vefat etti.')


def takim_ornegi():
    """Kitap s. 20, Kontrol Noktası: zorbalığa sessiz kalınan takım; s. 19: uzlaştırıcı ve adil tutum."""
    ic = '<defs>' + ok_isareti('okPH62c', 'g-s') + '</defs>'
    ic += _yazi(118, 20, 'Sessiz kalınırsa', 12.5, 'g-s', kalin=True)
    ic += _yazi(354, 20, 'Örnek alınırsa', 12.5, 'g-yf', kalin=True)
    sol = ['Zorbalığa ses çıkmaz', 'Haksızlık yayılır', 'Motivasyon düşer', 'Bazı oyuncular ayrılır',
           'Takım ilk turda elenir']
    sag = ['Haksızlığa uğrayanı korur', 'Herkesi dinler', 'Ortak çözüm arar', 'Kimseyi kayırmaz',
           'Kırmadan uyarır']
    for k, (a, b) in enumerate(zip(sol, sag)):
        y = 32 + k * 40
        ic += _gri(8, y, 220, 28, rx=8)
        ic += _yazi(118, y + 19, a, 12.5, 'g-y')
        ic += _kutu(244, y, 220, 28, 'yesil', rx=8)
        ic += _yazi(354, y + 19, b, 12.5, 'g-yf', kalin=True)
        if k < 4:
            ic += (f'<line x1="118" y1="{y + 29}" x2="118" y2="{y + 39}" class="g-c" stroke-width="1.5" '
                   f'marker-end="url(#okPH62c)"/>')
    return svg(472, 236, ic, 'Kitaptaki takım örneği: zorbalığa ses çıkmaz, haksızlık yayılır, motivasyon düşer, bazı oyuncular '
               'ayrılır, takım ilk turda elenir. Peygamberimizin tutumu örnek alınırsa: haksızlığa uğrayan korunur, '
               'herkes dinlenir, ortak çözüm aranır, kimse kayırılmaz, kırmadan uyarılır.')


def uygula(o):
    g = {'Üç gün bekleyen genç: söze bağlılık': soze_baglilik(),
         'Çocukları ve kız çocuklarına verilen değer': cocuklari(),
         'Uzlaştırıcı tutumu bugüne taşımak': takim_ornegi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
