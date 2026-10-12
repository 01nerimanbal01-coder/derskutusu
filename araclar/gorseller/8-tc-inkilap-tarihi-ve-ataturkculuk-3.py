"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük, 3. hafta: Mustafa Kemal’in fikir hayatının oluşması.

Görseller yalnız MEB 8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük ders kitabındaki bilgilerle çizilir (kitap PDF s. 26-29).
Renk anlamı: mavi = şehir (ortam), yeşil = yerli şair ve yazar, mor = yabancı düşünür, turuncu = Mustafa Kemal’e etkisi.
Çizimlerde ölçü ve harita yoktur; kutu boyları bilginin önemini ya da süreyi göstermez, yalnız ilişkiyi gösterir.
İnsan figürü kullanılmaz.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _olc(t, boyut, kalin=False):
    """Yazı genişliği tahmini (karakter başına ≈ yazı boyutu × 0,58; kalınlarda biraz fazla)."""
    return len(t) * boyut * (0.64 if kalin else 0.60)


def _kutu(x, y, w, h, renk, rx=10, kalinlik=1.5):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="{kalinlik}"/>')


def _yaz(x, y, t, boyut=12, kalin=False, sinif='g-y', ankor=None, sigan=None):
    """Tek satır yazı; sığacağı genişlik verilirse taşma denetlenir."""
    if sigan is not None and _olc(t, boyut, kalin) > sigan:
        raise ValueError(f'yazı taşar: {t!r} ({_olc(t, boyut, kalin):.0f} > {sigan})')
    a = f' text-anchor="{ankor}"' if ankor else ''
    g = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}"{a} font-size="{boyut:g}"{g} class="{sinif}">{t}</text>'


def _satirlar(x, y, w, h, satirlar, boyut=12, kalin=False, sinif='g-y', ankor='start', pay=10):
    """Kutunun içine dikey ortalanmış 1-3 satır; satır aralığı 15."""
    n = len(satirlar)
    ilk = y + h / 2 - (n - 1) * 7.5 + boyut * 0.35
    ic = ''
    for i, t in enumerate(satirlar):
        if ankor == 'middle':
            ic += _yaz(x + w / 2, ilk + i * 15, t, boyut, kalin, sinif, 'middle', w - 2 * pay)
        else:
            ic += _yaz(x + pay, ilk + i * 15, t, boyut, kalin, sinif, None, w - 2 * pay)
    return ic


def sehir_sutunlari(sol, sag, etki_sol, etki_sag, etiket):
    """İki şehir yan yana: başlık, beş özellik satırı, turuncu etki kutusu, renk açıklaması."""
    ic = ''
    for x, (ad, satirlar), etki in ((8, sol, etki_sol), (244, sag, etki_sag)):
        w = 228
        ic += f'<rect x="{x}" y="8" width="{w}" height="28" rx="14" class="g-mf"/>'
        ic += _yaz(x + w / 2, 27, ad, 14, True, 'g-b', 'middle', w - 20)
        for i, s in enumerate(satirlar):
            y = 44 + i * 46
            ic += _kutu(x, y, w, 40, 'mavi')
            ic += _satirlar(x, y, w, 40, s)
        ic += _kutu(x, 276, w, 46, 'turuncu')
        ic += _satirlar(x, 276, w, 46, etki, 12, True, 'g-y')
    ic += '<circle cx="150" cy="342" r="6" class="g-tf"/>'
    ic += _yaz(162, 346, 'turuncu kutu: Mustafa Kemal’e etkisi', 12, False, 'g-s')
    return svg(480, 352, ic, etiket)


def selanik_manastir():
    """Selânik ve Manastır (kitap s. 26)."""
    sol = ('Selânik', [
        ['Makedonya’nın gelişmiş şehri'],
        ['Edebî faaliyetler ve', 'milliyetçilik hareketleri'],
        ['İşlek liman; Avrupa ile', 'demir yolu bağlantısı'],
        ['Farklı din, mezhep ve', 'milletler yan yana'],
        ['Askerî okullar gelişmiş;', 'özel eğitim kurumları var'],
    ])
    sag = ('Manastır', [
        ['Ordu ve vilayet merkezi'],
        ['Kültürel ve siyasi', 'açıdan önemli şehir'],
        ['Birçok Avrupa devletinin', 'konsolosluğu var'],
        ['Merkezî yönetim zayıf:', 'sık sık isyan'],
        ['Tarih öğretmeni Yüzbaşı', 'Mehmet Tevfik Bey'],
    ])
    return sehir_sutunlari(
        sol, sag,
        ['Batı etkisine açık ortam', 've yeni fikirler'],
        ['Avrupa’nın girişimlerini', 've niyetlerini gözlemleme'],
        'Selânik ve Manastır: Selânik, Makedonya Bölgesi’nin gelişmiş şehridir, edebî faaliyetler ve milliyetçilik hareketleri yoğundur, '
        'limanı ve demir yolu vardır, farklı din ve milletler yan yana yaşar, askerî okullar gelişmiştir; Batı etkisine açık bir ortam sunar. '
        'Manastır ordu ve vilayet merkezidir, kültürel ve siyasi bakımdan önemlidir, birçok Avrupa devletinin konsolosluğu vardır, sık sık isyan çıkar '
        've tarih öğretmeni Yüzbaşı Mehmet Tevfik Bey buradadır; Mustafa Kemal Avrupa’nın girişimlerini ve niyetlerini gözlemler.')


def sofya_istanbul():
    """Sofya ve İstanbul (kitap s. 27)."""
    sol = ('Sofya', [
        ['1913: ataşemiliter olarak', 'görevlendirildi'],
        ['Avrupa kültürü ve', 'günlük toplum yaşamı'],
        ['Toplantılarda Avrupalı', 'temsilcilerle görüşme'],
        ['Opera ile ilk tanışma;', 'Türkçe gazetelerle ilişki'],
        ['Bulgar Meclisi toplantıları:', 'parlamenter rejim'],
    ])
    sag = ('İstanbul', [
        ['Başkent: siyasi faaliyetler', 'yakından izlenir'],
        ['Beyoğlu (Pera) ve Galata:', 'Batı’ya bakan yüz'],
        ['Elçilikler; tiyatro, konser,', 'davet ve balo'],
        ['Avrupa’dan haber veren', 'Fransızca günlük gazeteler'],
        ['Arkadaşlarla Osmanlı’nın', 'sorunlarına çözüm arayışı'],
    ])
    return sehir_sutunlari(
        sol, sag,
        ['Parlamenter rejimi tanıma;', 'yeni savaşı sakıncalı bulma'],
        ['İnkılapçı yönünün', 'güçlenmesi'],
        'Sofya ve İstanbul: Sofya’da 1913’te ataşemiliter olarak görev yapan Mustafa Kemal Avrupa kültürünü ve toplum yaşamını gözlemler, '
        'Avrupalı temsilcilerle görüşür, operayı tanır, Türkçe gazetelerle ilişki kurar, Bulgar Meclisini izleyerek parlamenter rejimi öğrenir ve '
        'Osmanlı Devleti’nin yeniden savaşa girmesini sakıncalı bulur. İstanbul başkenttir; Beyoğlu ve Galata Batı’ya bakan yüzdür, elçilikler, tiyatro, konser, davet ve balo vardır; '
        'Fransızca günlük gazeteler Avrupa’dan haber verir; Mustafa Kemal arkadaşlarıyla çözüm arar ve inkılapçı yönü güçlenir.')


def kisi_etki(satirlar, renk, ad_renk, etiket, aciklama, kimlik='okIta3'):
    """Düşünür → etkilendiği düşünce: soldaki renkli kutuda ad, okla turuncu kutuya bağlanır."""
    ic = '<defs>' + ok_isareti(kimlik, 'g-s') + '</defs>'
    for i, (adlar, ana, alt) in enumerate(satirlar):
        y = 8 + i * 58
        ic += _kutu(8, y, 140, 48, renk)
        ic += _satirlar(8, y, 140, 48, adlar, 13.5, True, ad_renk, 'middle')
        ic += f'<line x1="152" y1="{y + 24}" x2="168" y2="{y + 24}" class="g-c" stroke-width="2" marker-end="url(#{kimlik})"/>'
        ic += _kutu(178, y, 294, 48, 'turuncu')
        punto = 12 if _olc(ana, 12, True) <= 274 else 11.5
        ic += _yaz(188, y + 21, ana, punto, True, 'g-y', None, 274)
        ic += _yaz(188, y + 38, alt, 12, False, 'g-y', None, 274)
    ic += f'<circle cx="18" cy="{8 + len(satirlar) * 58 + 12}" r="6" class="{RENK[renk][2]}"/>'
    ic += _yaz(30, 8 + len(satirlar) * 58 + 16, aciklama[0], 12, False, 'g-s')
    ic += f'<circle cx="236" cy="{8 + len(satirlar) * 58 + 12}" r="6" class="g-tf"/>'
    ic += _yaz(248, 8 + len(satirlar) * 58 + 16, aciklama[1], 12, False, 'g-s', None, 224)
    return svg(480, 8 + len(satirlar) * 58 + 28, ic, etiket)


def yerli_dusunurler():
    """Yerli şair ve yazarlar (kitap s. 28)."""
    satirlar = [
        (['Namık Kemal'], 'Vatan sevgisi, milliyetçilik', 'Genç Osmanlılar’ın öncülerinden'),
        (['Mehmet Emin', 'Yurdakul'], 'Millî ve manevi değerler', 'Şiirlerinde vatan teması'),
        (['Tevfik Fikret'], 'Vatan ve hürriyet kavramları', 'İkinci Meşrutiyet’in savunucusu'),
        (['Ziya Gökalp'], 'Türkleşmek, muasırlaşmak, İslamlaşmak', 'Türk millî ve manevi değerleri'),
    ]
    return kisi_etki(
        satirlar, 'yesil', 'g-y',
        'Yerli şair ve yazarlar ile Mustafa Kemal’e etkileri: Namık Kemal vatan sevgisi ve milliyetçilik; Mehmet Emin Yurdakul millî ve manevi değerler; '
        'Tevfik Fikret vatan ve hürriyet kavramları; Ziya Gökalp Türkleşmek, muasırlaşmak ve İslamlaşmak.',
        ('yeşil: yerli şair ve yazar', 'turuncu: Mustafa Kemal’e etkisi'))


def yabanci_dusunurler():
    """Yabancı düşünürler (kitap s. 29)."""
    satirlar = [
        (['Montesquieu'], 'Halk egemenliğine dayanan cumhuriyet', 'Monarşiye ve diktatörlüğe karşı'),
        (['Kant'], 'Akılcılık, bilimsellik, laiklik', 'Sorunlar akılla çözülebilir'),
        (['Rousseau'], 'Millî egemenlik, hukuk devleti', 'Toplumsal dayanışma, milliyetçilik'),
        (['Voltaire'], 'Demokratikleşme', 'Aydınlanma Çağı’na katkı'),
    ]
    return kisi_etki(
        satirlar, 'mor', 'g-y',
        'Yabancı düşünürler ve Mustafa Kemal’e etkileri: Montesquieu halk egemenliğine dayanan cumhuriyet; Kant akılcılık, bilimsellik ve laiklik; '
        'Rousseau millî egemenlik, hukuk devleti ve toplumsal dayanışma; Voltaire demokratikleşme.',
        ('mor: yabancı düşünür', 'turuncu: Mustafa Kemal’e etkisi'), 'okIta3b')


def uygula(o):
    g = {
        'Selânik ve Manastır: ilk ortamlar': selanik_manastir(),
        'Sofya ve İstanbul: Avrupa’yı yakından görmek': sofya_istanbul(),
        'Yerli düşünürler ve yazarlar': yerli_dusunurler(),
        'Yabancı düşünürler': yabanci_dusunurler(),
    }
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
