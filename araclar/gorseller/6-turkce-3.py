"""6. sınıf Türkçe, 3. hafta: Türkçenin Beyliği (üç dal, kelime grupları, ses ayarları).

Görseller yalnız MEB 6. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s25-s31); metin cümleleri görsele alınmaz.
Renk anlamı:
- Üç dal ve kelime grupları: yeşil = yurt/toprak, turuncu = çarşı ve esnaf, mavi = gönül/dil, mor = Anadolu Türk halkı (kök) ve zaman.
- Ses ayarları: mavi = nefes, turuncu = hız, yeşil = ses şiddeti, mor = ses tonu.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def uc_dal():
    """Anadolu Türk halkının tutunduğu üç dal ve Karamanoğlu Mehmet Bey'in kararı (s25-s26)."""
    ic = '<defs>' + ok_isareti('okU63', 'g-s') + '</defs>'
    ic += _kutu(126, 8, 220, 38, 'mor', rx=19)
    ic += _yazi(236, 32, 'Anadolu Türk halkı', 14.5, 'g-of', True, 'middle')
    kutular = [
        (4, 'yesil', 'Anayurt', ['Yurdu bırakmaz,', 'toprağa tutunur.']),
        (161, 'turuncu', 'Anadolu çarşısı', ['Ahiler, loncalar;', 'esnaf korunur.']),
        (318, 'mavi', 'Gönül dalı', ['Dil, yol ve töre;', 'halk direnir.']),
    ]
    for x, renk, baslik, satirlar in kutular:
        ic += _kutu(x, 92, 150, 80, renk)
        ic += _yazi(x + 14, 118, baslik, 12.5, RENK[renk][2], True)
        for i, s in enumerate(satirlar):
            ic += _yazi(x + 14, 142 + i * 20, s, 12)
        cx = x + 75
        ic += f'<line x1="236" y1="48" x2="{cx}" y2="88" class="g-c" stroke-width="2.5" marker-end="url(#okU63)"/>'
    ic += _kutu(8, 204, 456, 46, 'mavi')
    ic += _yazi(24, 224, '13 Mayıs 1277', 13, 'g-mf', True)
    ic += _yazi(24, 242, 'Karamanoğlu Mehmet Bey: Türkçe devletin başında', 12)
    ic += '<line x1="393" y1="174" x2="393" y2="200" class="g-c" stroke-width="2.5" marker-end="url(#okU63)"/>'
    return svg(472, 258, ic, 'Halkın tutunduğu üç dal: yeşil, anayurt; yurdu bırakmaz, toprağa tutunur. Turuncu, Anadolu çarşısı; '
               'Ahiler ve loncalar esnafı korur. Mavi, gönül dalı; dil, yol ve töre ile halk direnir. Gönül dalından 13 Mayıs 1277 kararına ok gider: '
               'Karamanoğlu Mehmet Bey, Türkçe devletin başında.')


def kelime_gruplari():
    """Kelimelerin bir arada bulunma gerekçeleri (s28)."""
    kartlar = [
        (8, 8, 'yesil', 'Yurt kavramı', 'Yurt, toprak, vatan', 'Aynı kavramı anlatırlar.'),
        (240, 8, 'turuncu', 'Çarşı esnafı', 'Demirci, dokumacı, terzi', 'Esnaf ve zanaatçı adları.'),
        (8, 124, 'mor', 'Zaman', 'Geçmiş, bugün, gelecek', 'Zamanı gösterirler.'),
        (240, 124, 'mavi', 'Dil alanı', 'Okuma, konuşma, dil', 'Dille ilgili kavramlardır.'),
    ]
    ic = ''
    for x, y, renk, baslik, kelimeler, gerekce in kartlar:
        ic += _kutu(x, y, 224, 104, renk)
        ic += _yazi(x + 14, y + 28, baslik, 14, RENK[renk][2], True)
        ic += _yazi(x + 14, y + 56, kelimeler, 12.5)
        ic += f'<line x1="{x + 14}" y1="{y + 68}" x2="{x + 210}" y2="{y + 68}" class="{RENK[renk][1]}" stroke-width="1.5"/>'
        ic += _yazi(x + 14, y + 90, gerekce, 11.5, 'g-s')
    return svg(472, 236, ic, 'Dört kelime grubu ve ortak gerekçeleri: yeşil, yurt, toprak, vatan; aynı kavramı anlatırlar. Turuncu, demirci, dokumacı, terzi; '
               'esnaf ve zanaatçı adları. Mor, geçmiş, bugün, gelecek; zamanı gösterirler. Mavi, okuma, konuşma, dil; dille ilgili kavramlardır.')


def ses_ayarlari():
    """Nefes, hız, ses şiddeti ve ses tonu (s29-s30)."""
    ic = ''
    # nefes
    ic += _kutu(8, 8, 224, 118, 'mavi')
    ic += _yazi(22, 34, 'Nefes', 14, 'g-mf', True)
    for i, s in enumerate(['1. Burnundan derin nefes al', '2. Kısa bir süre tut', '3. Yavaşça ver']):
        ic += _yazi(22, 62 + i * 22, s, 11.5)
    # hız
    ic += _kutu(240, 8, 224, 118, 'turuncu')
    ic += _yazi(254, 34, 'Hız', 14, 'g-tf', True)
    for i, s in enumerate(['Cümleyi parçalara ayır;', 'bazı parçaları yavaş,', 'bazılarını normal söyle.']):
        ic += _yazi(254, 62 + i * 22, s, 11.5)
    # ses şiddeti
    ic += _kutu(8, 136, 224, 118, 'yesil')
    ic += _yazi(22, 162, 'Ses şiddeti', 14, 'g-yf', True)
    taban = 218
    for k, (ad, h) in enumerate([('Fısıltı', 14), ('Normal', 28), ('Yüksek', 44)]):
        x = 30 + k * 68
        ic += f'<rect x="{x}" y="{taban - h}" width="44" height="{h}" rx="4" class="g-yf"/>'
        ic += _yazi(x + 22, taban + 17, ad, 12, 'g-y', False, 'middle')
    # ses tonu
    ic += _kutu(240, 136, 224, 118, 'mor')
    ic += _yazi(254, 162, 'Ses tonu', 14, 'g-of', True)
    for i, s in enumerate(['Haber spikeri: ciddi, açık', 'Şair: duygulu, ağır', 'Yaşlı bilge: sakin, vurgulu', 'Duyuru yapan: güçlü, yüksek']):
        ic += _yazi(254, 186 + i * 18, s, 11.5)
    return svg(472, 262, ic, 'Ses kullanımının dört ayarı: nefes, burnundan derin nefes al, kısa bir süre tut, yavaşça ver; hız, cümleyi parçalara ayır, '
               'bazı parçaları yavaş bazılarını normal söyle; ses şiddeti, fısıltı en alçak, normal orta, yüksek en yüksek; ses tonu, haber spikeri ciddi ve açık, '
               'şair duygulu ve ağır, yaşlı bilge sakin ve vurgulu, duyuru yapan güçlü ve yüksek.')


def uygula(o):
    g = {'Balım Kız, Dalım Oğul: Anadolu’da üç dal': uc_dal(),
         'Anahtar kelime ve kelime ilişkileri': kelime_gruplari(),
         'Sesini uygun kullan': ses_ayarlari()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
