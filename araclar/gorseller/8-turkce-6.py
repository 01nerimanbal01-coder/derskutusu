"""8. sınıf Türkçe, 6. hafta: Çanakkale’den bir olay (olay akışı, 5N1K, yazı karakterleri, özne).

Görseller yalnız MEB 8. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s42-s46, özne tanımı s59); metinden cümle alıntısı yapılmaz,
özne örnekleri kurgusaldır ve özet metnindeki cümlelerle aynıdır.
Renk anlamı:
- Olay akışı: mavi = tabyadaki durum, turuncu = Seyit’in yaptığı ve sonucu, yeşil = sonrası.
- 5N1K: mavi = kişi ve olay (Kim? Ne?), turuncu = yer ve zaman (Nerede? Ne zaman?), yeşil = biçim ve neden (Nasıl? Niçin?).
- Yazı karakterleri: mavi = dik yazı (yazarın kendi sözleri), turuncu = eğik yazı (olay anlatımı).
- Özne: mavi = özne, turuncu = yüklem, gri = diğer ögeler.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı/dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start', italik=False):
    agirlik = ' font-weight="800"' if kalin else ''
    stil = ' font-style="italic"' if italik else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik}{stil} class="{sinif}">{metin}</text>'


def _gri(x, y, w, h, rx=8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.6"/>')


def olay_akisi():
    """Olayın akışı: altı adım (s42-s43)."""
    ic = '<defs>' + ok_isareti('okH6a', 'g-s') + '</defs>'
    adim = [('mavi', 'Tabya yoğun ateş altında; cephaneliğin bir kısmı', 'havaya uçar, on altı topçu şehit olur'),
            ('mavi', 'Ayakta kalan tek topun vinci kırıktır;', 'mermiler namluya sürülemez'),
            ('turuncu', 'Seyit dua eder, 215 okkalık mermiyi omzuna alır', 'Demir basamakları üç kez inip çıkar'),
            ('turuncu', 'Üçüncü mermi namluya sürülür ve patlar;', 'OCEAN (Oşin) zırhlısı yara alır'),
            ('yesil', 'Hilmi Bey olayı izler, telefonla bildirir;', 'aynı gün geç saatlerde Cevat Paşa tabyaya gelir'),
            ('yesil', 'Cevat Paşa Seyit’i kutlar, onbaşılık verir;', 'mermiyi yeniden ister, Seyit kaldıramayacağını söyler')]
    for k, (renk, s1, s2) in enumerate(adim):
        y = 8 + k * 58
        ic += _kutu(46, y, 418, 50, renk, rx=12)
        ic += f'<circle cx="24" cy="{y + 25}" r="13" class="{RENK[renk][2]}"/>' + _yazi(24, y + 30, k + 1, 14, 'g-b', True, 'middle')
        ic += _yazi(60, y + 21, s1, 12.5, 'g-y', True)
        ic += _yazi(60, y + 39, s2, 12.5, 'g-y')
        if k < 5:
            ic += f'<line x1="24" y1="{y + 42}" x2="24" y2="{y + 62}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okH6a)"/>'
    ic += '<circle cx="20" cy="368" r="6" class="g-mf"/>' + _yazi(32, 372, 'Tabyadaki durum', 12)
    ic += '<circle cx="150" cy="368" r="6" class="g-tf"/>' + _yazi(162, 372, 'Seyit’in yaptığı ve sonucu', 12)
    ic += '<circle cx="360" cy="368" r="6" class="g-yf"/>' + _yazi(372, 372, 'Sonrası', 12)
    return svg(472, 384, ic, 'Olayın altı adımı. Bir: tabya yoğun ateş altında, cephaneliğin bir kısmı havaya uçar, on altı topçu şehit olur. '
               'İki: ayakta kalan tek topun vinci kırıktır, mermiler namluya sürülemez. Üç: Seyit dua eder, 215 okkalık mermiyi omzuna alır, demir basamakları üç kez inip çıkar. '
               'Dört: üçüncü mermi namluya sürülür ve patlar, OCEAN zırhlısı yara alır. '
               'Beş: Hilmi Bey olayı izler ve telefonla bildirir, aynı gün geç saatlerde Cevat Paşa tabyaya gelir. '
               'Altı: Cevat Paşa Seyit’i kutlar ve ona onbaşılık verir, mermiyi yeniden ister, Seyit kaldıramayacağını söyler. '
               'Mavi tabyadaki durum, turuncu Seyit’in yaptığı ve sonucu, yeşil sonrasıdır.')


def soru_kartlari():
    """5N1K soru sözcükleri ve metinden cevapları (s44)."""
    kart = [
        ('mavi', 'Kim?', ['Topçu Neferi Seyit']),
        ('mavi', 'Ne?', ['215 okkalık mermiyi', 'kaldırdı']),
        ('turuncu', 'Nerede?', ['Rumeli Mecidiye Tabyası’nda']),
        ('turuncu', 'Ne zaman?', ['18 Mart Deniz Savaşı', 'sırasında']),
        ('yesil', 'Nasıl?', ['Mermiyi omzuna alıp demir', 'basamakları üç kez', 'inip çıkarak']),
        ('yesil', 'Niçin?', ['Topun vinci kırık olduğu', 'için mermiler namluya', 'sürülemiyordu']),
    ]
    yer = [(8, 8, 68), (238, 8, 68), (8, 84, 68), (238, 84, 68), (8, 160, 86), (238, 160, 86)]
    ic = ''
    for (renk, soru, satirlar), (x, y, h) in zip(kart, yer):
        ic += _kutu(x, y, 226, h, renk, rx=12)
        ic += _yazi(x + 14, y + 23, soru, 14.5, RENK[renk][2], True)
        for i, s in enumerate(satirlar):
            ic += _yazi(x + 14, y + 44 + i * 17, s, 12, 'g-y')
    ic += _yazi(8, 268, 'Mavi: kişi ve olay. Turuncu: yer ve zaman.', 11.5, 'g-y')
    ic += _yazi(8, 285, 'Yeşil: yapılış biçimi ve neden.', 11.5, 'g-y')
    return svg(472, 296, ic, 'Metinden 5N1K örnekleri. Kim: Topçu Neferi Seyit. Ne: 215 okkalık mermiyi kaldırdı. Nerede: Rumeli Mecidiye Tabyası’nda. '
               'Ne zaman: 18 Mart Deniz Savaşı sırasında. Nasıl: mermiyi omzuna alıp demir basamakları üç kez inip çıkarak. '
               'Niçin: topun vinci kırık olduğu için mermiler namluya sürülemiyordu. Mavi kişi ve olay, turuncu yer ve zaman, yeşil yapılış biçimi ve nedendir.')


def yazi_karakterleri():
    """Metnin üç bölümü ve yazı karakterleri: dik giriş, eğik olay anlatımı, dik kapanış (s42-s43)."""
    ic = '<defs>' + ok_isareti('okH6b', 'g-s') + '</defs>'
    bant = [('mavi', 'Dik yazı', False, 'Giriş: yazar savaşın bir bütün olduğunu söyler', 've okuru olayı birlikte okumaya çağırır'),
            ('turuncu', 'Eğik yazı', True, 'Olay anlatımı: tabya, tek top, Seyit ve mermi,', 'Hilmi Bey, Cevat Paşa, Seyit’in yanıtı'),
            ('mavi', 'Dik yazı', False, 'Kapanış: yazar ordunun fedakârlığının', 'her övgünün üstünde olduğunu söyler')]
    for k, (renk, ad, italik, s1, s2) in enumerate(bant):
        y = 8 + k * 82
        ic += _kutu(8, y, 456, 64, renk, rx=12)
        ic += f'<rect x="18" y="{y + 18}" width="68" height="28" rx="14" class="{RENK[renk][2]}"/>'
        ic += _yazi(52, y + 37, ad, 11, 'g-b', True, 'middle', italik)
        ic += _yazi(98, y + 27, s1, 12.5, 'g-y', True, 'start', italik)
        ic += _yazi(98, y + 46, s2, 12.5, 'g-y', False, 'start', italik)
        if k < 2:
            ic += f'<line x1="52" y1="{y + 68}" x2="52" y2="{y + 76}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okH6b)"/>'
    ic += _yazi(8, 270, 'Mavi: dik yazı, yazarın kendi sözleri.', 11.5, 'g-y')
    ic += _yazi(8, 287, 'Turuncu: eğik yazı, olayın anlatıldığı bölüm.', 11.5, 'g-y')
    return svg(472, 298, ic, 'Metnin üç bölümü sırayla: birinci bölüm dik yazıyla yazılmış girişte yazar savaşın bir bütün olduğunu söyler ve okuru olayı birlikte okumaya çağırır; '
               'ikinci bölüm eğik yazıyla yazılmış olay anlatımıdır, tabya, tek top, Seyit ve mermi, Hilmi Bey, Cevat Paşa ve Seyit’in yanıtı anlatılır; '
               'üçüncü bölüm dik yazıyla yazılmış kapanışta yazar ordunun fedakârlığının her övgünün üstünde olduğunu söyler. '
               'Mavi dik yazı, turuncu eğik yazıdır.')


def ozne():
    """Özne ve yüklem: iki kurgusal örnek."""
    def gen(t, boyut=13):
        return round(len(t) * boyut * 0.58 + 22)

    def cip(x, y, h, satirlar, tur):
        w = max(gen(t) for t in satirlar)
        if tur == 'ozne':
            s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="g-mf"/>'
            sinif, kalin = 'g-b', True
        elif tur == 'yuklem':
            s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="g-tf"/>'
            sinif, kalin = 'g-b', True
        else:
            s = _gri(x, y, w, h, rx=10)
            sinif, kalin = 'g-y', False
        n = len(satirlar)
        for i, t in enumerate(satirlar):
            yy = y + h / 2 + 4.5 + (i - (n - 1) / 2) * 16
            s += _yazi(x + w / 2, yy, t, 13, sinif, kalin, 'middle')
        return s, w

    ic = ''
    # örnek 1
    x = 8
    y = 10
    for satirlar, tur, etiket in [(['Çanakkale gezisine', 'giden öğrenciler'], 'ozne', 'özne'),
                                  (['şehitliği', 'saygıyla'], 'diger', 'diğer ögeler'),
                                  (['gezdi'], 'yuklem', 'yüklem')]:
        s, w = cip(x, y, 44, satirlar, tur)
        ic += s
        renk = {'ozne': 'g-mf', 'yuklem': 'g-tf', 'diger': 'g-s'}[tur]
        ic += _yazi(x + w / 2, y + 64, etiket, 11.5, renk, True, 'middle')
        x += w + 8
    ic += _yazi(8, y + 88, 'Yükleme sor: Gezme eylemini kim yaptı?', 12, 'g-y')
    # örnek 2
    x = 8
    y = 120
    for satirlar, tur, etiket in [(['Bu şiir'], 'ozne', 'özne'),
                                  (['unutulmaz bir eserdir'], 'yuklem', 'yüklem')]:
        s, w = cip(x, y, 36, satirlar, tur)
        ic += s
        renk = {'ozne': 'g-mf', 'yuklem': 'g-tf'}[tur]
        ic += _yazi(x + w / 2, y + 56, etiket, 11.5, renk, True, 'middle')
        x += w + 8
    ic += _yazi(8, y + 80, 'Çekimli fiil yok: yargı “bu şiir” için söylenir, özne odur.', 12, 'g-y')
    ic += '<circle cx="20" cy="226" r="6" class="g-mf"/>' + _yazi(32, 230, 'Özne', 12)
    ic += '<circle cx="100" cy="226" r="6" class="g-tf"/>' + _yazi(112, 230, 'Yüklem', 12)
    ic += '<circle cx="196" cy="226" r="6" class="g-s"/>' + _yazi(208, 230, 'Diğer ögeler', 12)
    return svg(472, 240, ic, 'Özne örnekleri. Birinci cümle: Çanakkale gezisine giden öğrenciler şehitliği saygıyla gezdi. Özne Çanakkale gezisine giden öğrenciler öbeğidir, '
               'diğer ögeler şehitliği ve saygıyla, yüklem gezdi. Yükleme gezme eylemini kim yaptı diye sorulur. '
               'İkinci cümle: Bu şiir unutulmaz bir eserdir. Özne bu şiir, yüklem unutulmaz bir eserdir; çekimli fiil yoktur, yargı bu şiir için söylenir. '
               'Mavi özne, turuncu yüklem, gri diğer ögelerdir.')


def uygula(o):
    g = {'Metni oku: Çanakkale’den bir olay': olay_akisi(),
         'Sözcüğü tahmin et, 5N1K ile sor': soru_kartlari(),
         'Yazı karakterleri metne ne katar?': yazi_karakterleri(),
         'Özne: eylemi yapan ya da yargıyı taşıyan': ozne()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
