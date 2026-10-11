"""6. sınıf Din Kültürü ve Ahlak Bilgisi, 3. hafta: akıl ve vahiy, vahyin mesaj alanları, vahyin yolu.

Görseller yalnız MEB 6. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap PDF s. 24-25).
Renk anlamı: ilk görselde mavi = akıl, turuncu = vahiy; ikinci görselde dört mesaj alanı dört ayrı renktedir
(mavi inanç, yeşil ibadet, mor ahlak, turuncu toplumsal konular), kıssa nötr renktedir; üçüncü görselde mavi = vahyi
gönderen Allah, turuncu = ileten peygamberler, yeşil = ulaşan insanlar, mor = vahyin temel amacı.
Çizimlerde ölçü yoktur; yalnız ilişkiler gösterilir.
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


def _yazi(x, y, metin, boyut=12.5, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def akil_ve_vahiy():
    """Akıl iyi ile kötüyü ayırt ettirir; vahiy, cevabı kişiden kişiye değişen sorularda doğru bilgiyi verir (kitap s. 24)."""
    ic = ''
    # başlık hapları
    ic += '<rect x="8" y="8" width="224" height="30" rx="15" class="g-mf"/>' + _yazi(120, 28, 'Akıl', 14, True, 'g-b')
    ic += '<rect x="248" y="8" width="224" height="30" rx="15" class="g-tf"/>' + _yazi(360, 28, 'Vahiy', 14, True, 'g-b')
    # akıl sütunu
    ic += _kutu(8, 46, 224, 178, 'mavi')
    ic += _yazi(120, 70, 'Ayırt etmeyi sağlar', 13, True)
    for y, t in [(82, 'iyi ile kötüyü'), (120, 'doğru ile yanlışı')]:
        ic += f'<rect x="24" y="{y}" width="192" height="30" rx="15" class="g-z"/><rect x="24" y="{y}" width="192" height="30" rx="15" class="g-ms" stroke-width="1.6"/>'
        ic += _yazi(120, y + 20, t)
    ic += _yazi(120, 172, 'Her büyük sorunun cevabına', 12, False, 'g-s')
    ic += _yazi(120, 189, 'yetmeyebilir', 12, False, 'g-s')
    # vahiy sütunu
    ic += _kutu(248, 46, 224, 178, 'turuncu')
    ic += _yazi(360, 68, 'Cevabı kişiden kişiye', 13, True)
    ic += _yazi(360, 85, 'değişebilen sorular', 13, True)
    for k, t in enumerate(['Ben kimim?', 'Nereden geldim?', 'Hayatın anlamı nedir?', 'Ölümden sonra hayat var mı?']):
        y = 96 + k * 30
        ic += f'<rect x="256" y="{y}" width="208" height="24" rx="12" class="g-z"/><rect x="256" y="{y}" width="208" height="24" rx="12" class="g-ts" stroke-width="1.6"/>'
        ic += _yazi(360, y + 17, t, 12)
    ic += _yazi(240, 246, 'Vahiy, bu sorularda doğru bilgiye ulaşmayı sağlar.', 12.5, True)
    return svg(480, 256, ic, 'Akıl ve vahiy: Akıl iyi ile kötüyü, doğru ile yanlışı ayırt etmeyi sağlar ama her büyük sorunun cevabına yetmeyebilir. '
               'Vahiy; Ben kimim, Nereden geldim, Hayatın anlamı nedir ve Ölümden sonra hayat var mı gibi cevabı kişiden kişiye değişebilen sorularda doğru bilgiye ulaşmayı sağlar.')


def mesaj_alanlari():
    """Vahyin mesaj alanları: inanç, ibadet, ahlak, toplumsal konular; bir kısmı kıssalarla anlatılır (kitap s. 24)."""
    ic = '<defs>' + ok_isareti('okDK63m', 'g-s') + '</defs>'
    ic += '<rect x="178" y="66" width="124" height="48" rx="14" class="g-z"/><rect x="178" y="66" width="124" height="48" rx="14" class="g-c" stroke-width="2"/>'
    ic += _yazi(240, 87, 'Vahyin', 14, True) + _yazi(240, 105, 'mesajları', 14, True)
    kutular = [(8, 16, 'mavi', ['İnanç']), (8, 118, 'yesil', ['İbadet']),
               (332, 16, 'mor', ['Ahlak']), (332, 118, 'turuncu', ['Toplumsal', 'konular'])]
    for x, y, renk, satir in kutular:
        ic += _kutu(x, y, 140, 44, renk)
        if len(satir) == 1:
            ic += _yazi(x + 70, y + 27, satir[0], 14, True)
        else:
            ic += _yazi(x + 70, y + 19, satir[0], 13, True) + _yazi(x + 70, y + 35, satir[1], 13, True)
    for x1, y1, x2, y2 in [(152, 40, 174, 74), (152, 140, 174, 106), (328, 40, 306, 74), (328, 140, 306, 106)]:
        ic += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    # kıssa bandı
    ic += '<rect x="8" y="178" width="464" height="54" rx="12" class="g-z"/>'
    ic += '<rect x="8" y="178" width="464" height="54" rx="12" class="g-c" stroke-width="1.8" stroke-dasharray="5 4"/>'
    ic += _yazi(240, 200, 'Bazı mesajlar kıssalarla aktarılır', 12.5, True)
    ic += _yazi(240, 219, 'Kıssa: geçmişteki peygamber ve milletlere ait ibretli olay', 12, False, 'g-s')
    ic += '<line x1="240" y1="174" x2="240" y2="124" class="g-c" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#okDK63m)"/>'
    return svg(480, 240, ic, 'Vahyin mesajları dört alanda toplanır: inanç, ibadet, ahlak ve toplumsal konular. '
               'Mesajların bir kısmı, geçmişteki peygamberlere ve milletlere ait ibretli olaylar olan kıssalarla anlatılır.')


def vahyin_yolu():
    """Vahyin yolu: Allah -> peygamberler -> insanlar -> doğru yol; temel amaç dünya ve ahiret mutluluğu (kitap s. 24)."""
    ic = '<defs>' + ok_isareti('okDK63y', 'g-s') + '</defs>'
    ic += _kutu(8, 12, 110, 48, 'mavi') + _yazi(63, 41, 'Allah', 14, True)
    ic += _kutu(184, 12, 110, 48, 'turuncu') + _yazi(239, 41, 'Peygamberler', 12.5, True)
    ic += _kutu(360, 12, 110, 48, 'yesil') + _yazi(415, 41, 'İnsanlar', 14, True)
    for x1, x2, t in [(123, 176, 'vahiy'), (299, 352, 'iletir')]:
        ic += f'<line x1="{x1}" y1="36" x2="{x2}" y2="36" class="g-c" stroke-width="2" marker-end="url(#okDK63y)"/>'
        ic += _yazi((x1 + x2) / 2, 28, t, 12, False, 'g-s')
    ic += '<line x1="415" y1="65" x2="415" y2="90" class="g-c" stroke-width="2" marker-end="url(#okDK63y)"/>'
    ic += _kutu(360, 98, 110, 48, 'yesil')
    ic += _yazi(415, 119, 'Doğru yola', 12.5, True) + _yazi(415, 136, 'yönelirler', 12.5, True)
    ic += '<line x1="355" y1="122" x2="301" y2="122" class="g-c" stroke-width="2" marker-end="url(#okDK63y)"/>'
    ic += _kutu(150, 98, 140, 48, 'mor')
    ic += _yazi(220, 119, 'Dünya ve ahiret', 12.5, True) + _yazi(220, 136, 'mutluluğu', 12.5, True)
    ic += _yazi(220, 90, 'Vahyin temel amacı', 12, True, 'g-of')
    ic += _yazi(240, 178, 'Kur’an-ı Kerim bu yolun kılavuzudur.', 12.5, True)
    return svg(480, 190, ic, 'Vahyin yolu: Allah vahiy gönderir, peygamberler vahyi insanlara iletir, insanlar doğru yola yönelir. '
               'Vahyin temel amacı dünya ve ahiret mutluluğunu sağlamaktır. Kur’an-ı Kerim bu yolun kılavuzudur.')


def uygula(o):
    g = {'Akıl yetmediğinde vahiy': akil_ve_vahiy(),
         'Vahyin mesajları: ahlak, ibadet, inanç ve toplum': mesaj_alanlari(),
         'Vahyin temel amacı: doğru yola yönlendirmek': vahyin_yolu()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
