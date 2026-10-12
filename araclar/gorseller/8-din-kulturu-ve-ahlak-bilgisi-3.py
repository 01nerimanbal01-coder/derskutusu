"""8. sınıf Din Kültürü ve Ahlak Bilgisi, 3. hafta: insanın iradesi ve kader (ilim, irade, önceden bilme, sorumluluk).

Görseller yalnız MEB 8. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap s. 19-20).
Renk anlamı (üç görselde de aynı): turuncu = insan, mor = Allah, mavi = tercih/davranış, yeşil = sorumluluk ve hesap.
Çizimlerde ölçü yoktur; kutu boyutları miktar göstermez, yalnız ilişkiyi gösterir.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _zemin(x, y, w, h, rx=10, kesik=False):
    k = ' stroke-dasharray="6 4"' if kesik else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"{k}/>')


def _yazi(x, y, metin, boyut=12, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def ilim_irade():
    """İnsanın ilmi ve iradesi sınırlıdır; Allah'ınki sonsuzdur, her şeyi kuşatır, görünen ve görünmeyen âlemi (gayb) kapsar (kitap s. 19)."""
    ic = _kutu(72, 6, 190, 28, 'turuncu', 14) + _yazi(167, 26, 'İnsan', 14, True, 'g-tf')
    ic += _kutu(270, 6, 202, 28, 'mor', 14) + _yazi(371, 26, 'Allah', 14, True, 'g-of')
    # birinci satır: ilim
    ic += _zemin(6, 42, 60, 68) + _yazi(36, 80, 'İlim', 13, True)
    ic += _kutu(72, 42, 190, 68, 'turuncu', 10)
    ic += _yazi(167, 70, 'Sınırlı', 13, True, 'g-tf') + _yazi(167, 90, 'her şeyi bilemez', 12)
    ic += _kutu(270, 42, 202, 68, 'mor', 10)
    ic += _yazi(371, 62, 'Sonsuz', 13, True, 'g-of') + _yazi(371, 80, 'görünen ve görünmeyen', 12) + _yazi(371, 97, 'âlemi (gayb) kapsar', 12)
    # ikinci satır: irade
    ic += _zemin(6, 118, 60, 64) + _yazi(36, 154, 'İrade', 13, True)
    ic += _kutu(72, 118, 190, 64, 'turuncu', 10)
    ic += _yazi(167, 144, 'Sınırlı', 13, True, 'g-tf') + _yazi(167, 164, 'her istediğini yapamaz', 12)
    ic += _kutu(270, 118, 202, 64, 'mor', 10)
    ic += _yazi(371, 144, 'Sonsuz', 13, True, 'g-of') + _yazi(371, 164, 'her şeyi kuşatır', 12)
    ic += _yazi(240, 208, 'İnsanın ilmi ve iradesi sınırlı, Allah’ınki sonsuzdur.', 12.5, True)
    return svg(480, 220, ic, 'İnsan ile Allah karşılaştırması: insanın ilmi sınırlıdır, her şeyi bilemez; Allah’ın ilmi sonsuzdur ve görünen ile görünmeyen âlemi (gayb) kapsar. '
               'İnsanın iradesi sınırlıdır, her istediğini yapamaz; Allah’ın iradesi sonsuzdur ve her şeyi kuşatır.')


def onceden_bilme():
    """Allah'ın önceden bilmesi insanın tercihi üzerinde etkili değildir; tercih insana aittir, Allah tercihe göre fiili yaratır (kitap s. 19)."""
    ic = '<defs>' + ok_isareti('okDK83a', 'g-s') + '</defs>'
    ic += _kutu(110, 6, 260, 52, 'mor') + _yazi(240, 28, 'Allah önceden bilir', 14, True, 'g-of') + _yazi(240, 46, 'insanın seçeceği davranışı da', 11.5)
    ic += '<line x1="240" y1="62" x2="240" y2="104" class="g-os" stroke-width="2" stroke-dasharray="5 4"/>'
    ic += '<line x1="226" y1="106" x2="254" y2="106" class="g-os" stroke-width="3.5" stroke-linecap="round"/>'
    ic += _yazi(264, 90, 'bilgi tercihi etkilemez', 12, False, 'g-of', 'start')
    ic += _kutu(6, 118, 140, 70, 'turuncu') + _yazi(76, 142, 'İnsan', 14, True, 'g-tf') + _yazi(76, 162, 'akıllı ve iradeli', 11)
    ic += _kutu(170, 118, 140, 70, 'mavi') + _yazi(240, 142, 'Tercih', 14, True, 'g-mf') + _yazi(240, 162, 'doğru ya da yanlış', 11)
    ic += _kutu(334, 118, 140, 70, 'mor') + _yazi(404, 140, 'Allah', 14, True, 'g-of') + _yazi(404, 158, 'tercihe göre', 11) + _yazi(404, 174, 'fiili yaratır', 11)
    ic += '<line x1="150" y1="153" x2="166" y2="153" class="g-c" stroke-width="2" marker-end="url(#okDK83a)"/>'
    ic += '<line x1="314" y1="153" x2="330" y2="153" class="g-c" stroke-width="2" marker-end="url(#okDK83a)"/>'
    ic += _yazi(240, 208, 'Tercih insana aittir; Allah’ın bilgisi tercihi yönlendirmez.', 12, True)
    return svg(480, 216, ic, 'Allah sonsuz bilgisiyle insanın seçeceği davranışı da önceden bilir; bu bilgi insanın tercihini etkilemez. '
               'Akıllı ve iradeli insan doğruyu ya da yanlışı seçer; Allah da bu seçime göre fiili yaratır.')


def sorumluluk_zinciri():
    """Akıl ve irade sahibi insan davranışını seçer, sonuçlarını üstlenir ve hesap verir; sorumluluk gücüyle sınırlıdır,
    iradesi dışındaki durumlardan sorumlu tutulmaz (kitap s. 19)."""
    ic = '<defs>' + ok_isareti('okDK83b', 'g-s') + '</defs>'
    ic += _kutu(3, 6, 102, 74, 'turuncu') + _yazi(54, 30, 'Akıl ve irade', 11, True, 'g-tf') + _yazi(54, 52, 'sahibi insan', 11)
    ic += _kutu(129, 6, 102, 74, 'mavi') + _yazi(180, 30, 'Tercih', 12, True, 'g-mf') + _yazi(180, 50, 'seçilen', 11) + _yazi(180, 65, 'davranış', 11)
    ic += _kutu(255, 6, 102, 74, 'yesil') + _yazi(306, 30, 'Sorumluluk', 12, True, 'g-yf') + _yazi(306, 50, 'sonuçları', 11) + _yazi(306, 65, 'üstlenme', 11)
    ic += _kutu(381, 6, 96, 74, 'yesil') + _yazi(429, 30, 'Hesap verme', 12, True, 'g-yf') + _yazi(429, 50, 'yapılanlar ve', 11) + _yazi(429, 65, 'yapılmayanlar', 11)
    for x1, x2 in ((108, 126), (234, 252), (360, 378)):
        ic += f'<line x1="{x1}" y1="43" x2="{x2}" y2="43" class="g-c" stroke-width="2" marker-end="url(#okDK83b)"/>'
    ic += _zemin(3, 96, 474, 28, 14, True) + _yazi(240, 115, 'Sorumluluk, kişinin gücüyle sınırlıdır.', 12.5, True)
    ic += _kutu(3, 138, 474, 52, 'turuncu')
    ic += _yazi(240, 160, 'İradesi dışında kalan durumlardan sorumlu tutulmaz:', 12, True, 'g-tf')
    ic += _yazi(240, 179, 'nerede doğduğu, saç rengi gibi', 11.5)
    return svg(480, 198, ic, 'Akıl ve irade sahibi insan davranışını seçer; tercih ettiği davranışın sonuçlarını üstlenir, bu da hesap vermeyi getirir. '
               'Sorumluluk kişinin gücüyle sınırlıdır; nerede doğduğu ve saç rengi gibi iradesi dışındaki durumlardan sorumlu tutulmaz.')


def uygula(o):
    g = {'İlim ve irade: insan ile Allah': ilim_irade(),
         'Allah’ın önceden bilmesi ve insanın tercihi': onceden_bilme(),
         'Sorumluluğun sınırı': sorumluluk_zinciri()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
