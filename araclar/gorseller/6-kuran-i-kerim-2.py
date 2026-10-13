"""6. sınıf Kur’an-ı Kerim, 2. hafta: peltek harfler ث, ذ, ظ.

Görseller yalnız MEB 6. sınıf Kur’an-ı Kerim ders kitabındaki bilgilerle çizilir (kitap s. 21-25).
Renk anlamı: mavi = ince ve yumuşak harf (ث, ذ), turuncu = kalın ve kuvvetli harf (ظ),
yeşil = peltek harf bulunan kelime, gri = peltek harf bulunmayan kelime.
Çubuk boyları yalnız kitabın verdiği sıralamayı (biraz dışarı → daha az → en az) gösterir; ölçü değildir.
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


def anlam_degisimi():
    """Kitap s. 21: نَذَرَ (adadı) → نَظَرَ (baktı); كَثَبَ (saçtı) → كَسَبَ (kazandı)."""
    ic = '<defs>' + ok_isareti('okK62a', 'g-s') + '</defs>'
    satir = [('نَذَرَ', 'adadı', 'ذ', 'ظ', 'نَظَرَ', 'baktı'),
             ('كَثَبَ', 'saçtı', 'ث', 'س', 'كَسَبَ', 'kazandı')]
    for k, (ar1, tr1, h1, h2, ar2, tr2) in enumerate(satir):
        y = 10 + k * 78
        ic += _kutu(8, y, 150, 64, 'mavi')
        ic += _yazi(83, y + 32, ar1, 24, kalin=True)
        ic += _yazi(83, y + 54, f'“{tr1}”', 12.5, 'g-mf', kalin=True)
        ic += _kutu(314, y, 150, 64, 'turuncu')
        ic += _yazi(389, y + 32, ar2, 24, kalin=True)
        ic += _yazi(389, y + 54, f'“{tr2}”', 12.5, 'g-tf', kalin=True)
        ic += f'<line x1="166" y1="{y + 40}" x2="304" y2="{y + 40}" class="g-c" stroke-width="2" marker-end="url(#okK62a)"/>'
        ic += _yazi(198, y + 28, h1, 20, kalin=True)
        ic += _yazi(236, y + 26, 'yerine', 12, 'g-s')
        ic += _yazi(274, y + 28, h2, 20, kalin=True)
    ic += _yazi(236, 172, 'Tek harf hatalı seslendirilince kelime de anlam da değişir.', 12, 'g-s')
    return svg(472, 182, ic, 'Bir harf değişince anlam değişir: nezera adadı demektir; zel yerine zı okunursa nazara olur, '
               'baktı demektir. Keseba saçtı demektir; se yerine sin okunursa kesebe olur, kazandı demektir.')


def mahrec_gruplari():
    """Kitap s. 21: çıkış yerine göre üç grup; peltek harfler dil (diş-damak) grubunda; ince ve kalın."""
    ic = '<defs>' + ok_isareti('okK62b', 'g-s') + '</defs>'
    ic += _gri(8, 10, 148, 40)
    ic += _yazi(82, 35, 'Dudak harfleri', 12.5, 'g-s', kalin=True)
    ic += _kutu(162, 10, 148, 40, 'mavi')
    ic += _yazi(236, 35, 'Dil (diş-damak)', 12.5, 'g-mf', kalin=True)
    ic += _gri(316, 10, 148, 40)
    ic += _yazi(390, 35, 'Boğaz harfleri', 12.5, 'g-s', kalin=True)
    ic += '<line x1="236" y1="52" x2="236" y2="72" class="g-c" stroke-width="2" marker-end="url(#okK62b)"/>'
    ic += _kutu(96, 78, 280, 62, 'mavi')
    ic += _yazi(236, 98, 'Peltek harfler', 12.5, 'g-mf', kalin=True)
    for x, h in ((186, 'ث'), (236, 'ذ'), (286, 'ظ')):
        ic += _yazi(x, 128, h, 24, kalin=True)
    ic += _yazi(236, 162, 'Mahreç: dil ucunun üst yüzeyi üst ön dişlerin ucuna değer', 12, 'g-y')
    ic += _kutu(8, 174, 224, 46, 'mavi')
    ic += _yazi(20, 202, 'İnce ve yumuşak', 12.5, 'g-mf', kalin=True, hiza='start')
    ic += _yazi(172, 204, 'ث', 22, kalin=True)
    ic += _yazi(208, 204, 'ذ', 22, kalin=True)
    ic += _kutu(240, 174, 224, 46, 'turuncu')
    ic += _yazi(252, 202, 'Kalın ve kuvvetli', 12.5, 'g-tf', kalin=True, hiza='start')
    ic += _yazi(428, 204, 'ظ', 22, kalin=True)
    return svg(472, 228, ic, 'Harfler çıkış yerine göre üçe ayrılır: dudak harfleri, dil (diş-damak) harfleri, boğaz harfleri. '
               'Peltek harfler se, zel ve zı dil (diş-damak) grubundadır. Mahreç: dil ucunun üst yüzeyi üst ön dişlerin '
               'ucuna değer. Se ve zel ince ve yumuşak, zı kalın ve kuvvetlidir.')


def dil_ucu_sirasi():
    """Kitap s. 22-24: dil ucu ث'de biraz dışarı, ذ'de daha az, ظ'da en az çıkar."""
    ic = _yazi(236, 20, 'Dil ucunun dışarı çıkışı (sıralama)', 12.5, 'g-s', kalin=True)
    satir = [('ث', 360, 'mavi', 'biraz dışarı: en çok'),
             ('ذ', 240, 'mavi', 'ث’ye göre daha az'),
             ('ظ', 128, 'turuncu', 'en az')]
    for k, (h, boy, renk, etiket) in enumerate(satir):
        y = 34 + k * 48
        a, s, f = RENK[renk]
        ic += f'<circle cx="30" cy="{y + 18}" r="20" class="{a}"/>'
        ic += f'<circle cx="30" cy="{y + 18}" r="20" class="{s}" stroke-width="2"/>'
        ic += _yazi(30, y + 26, h, 22, kalin=True)
        ic += f'<rect x="62" y="{y + 4}" width="{boy}" height="28" rx="8" class="{f}"/>'
        ic += _yazi(74, y + 23, etiket, 12.5, 'g-b', kalin=True, hiza='start')
    ic += _yazi(236, 192, 'Mahreç üçünde de aynı; fark, dil ucunun ne kadar dışarı çıktığındadır.', 12, 'g-s')
    return svg(472, 202, ic, 'Dil ucunun dışarı çıkış sıralaması: se harfinde biraz dışarı, en çok; zel harfinde se harfine göre '
               'daha az; zı harfinde en az. Mahreç üçünde de aynıdır.')


def kelime_tablosu():
    """Kitap s. 25, 5. etkinlik: karışık tablodan peltek harfli kelimeleri bulma."""
    kelime = [('ثُمَّ', 1), ('مَسَّ', 0), ('ظَهَرَ', 1), ('صَدَّ', 0), ('نَبَذَ', 1), ('ضَلَّ', 0),
              ('اَرْضِ', 0), ('ذٰلِكَ', 1), ('خَوْفٌ', 0), ('ظَالِمٌ', 1), ('سَنَةٍ', 0), ('عَظِيمٌ', 1),
              ('ثَمَرَاتٍ', 1), ('زَكٰوةٌ', 0), ('يُذْكَرَ', 1), ('شَيْءٍ', 0), ('اَظْلَمُ', 1), ('اَنْزَلَ', 0)]
    ic = ''
    for i, (k, p) in enumerate(kelime):
        x = 8 + (i % 6) * 76
        y = 10 + (i // 6) * 48
        if p:
            ic += _kutu(x, y, 72, 40, 'yesil', rx=10)
            ic += _yazi(x + 36, y + 27, k, 18, 'g-yf', kalin=True)
        else:
            ic += _gri(x, y, 72, 40, rx=10)
            ic += _yazi(x + 36, y + 27, k, 18, 'g-s')
    ic += _kutu(8, 160, 18, 18, 'yesil', rx=4)
    ic += _yazi(32, 174, 'peltek harf var', 12, 'g-y', hiza='start')
    ic += _gri(156, 160, 18, 18, rx=4)
    ic += _yazi(180, 174, 'yok (س ص ض ز peltek değil)', 12, 'g-y', hiza='start')
    return svg(472, 188, ic, 'Kelime tablosu: peltek harfli kelimeler sümme, zahara, nebeze, zâlike, zâlimun, azîmun, semerâtin, '
               'yuzkera, azlemu; peltek harf bulunmayanlar messe, sadde, dalle, ardı, havfun, senetin, zekâtun, şey’in, '
               'enzele. Sin, sad, dad ve ze peltek harf değildir.')


def uygula(o):
    g = {'Bir harf değişince anlam değişir': anlam_degisimi(),
         'Mahreç: harfin çıkış yeri': mahrec_gruplari(),
         '{ar:ظ} harfi: kalın ve kuvvetli': dil_ucu_sirasi(),
         'Peltek harfli kelimeyi bulma': kelime_tablosu()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
