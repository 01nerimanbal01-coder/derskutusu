"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük, 4. hafta: Mustafa Kemal’in askerlik hayatı.

Görseller yalnız MEB 8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük ders kitabındaki bilgilerle çizilir (kitap PDF s. 31-34).
Renk anlamı: görev şeridinde mavi = görev yeri, turuncu = çatışma ya da olay, yeşil = manevra; Trablusgarp akışında
mavi = olay ya da karar, turuncu = Mustafa Kemal’in yer aldığı gelişme; Balkan Savaşları tablosunda mavi = I. savaş,
turuncu = II. savaş; son görselde mavi = olgu, turuncu = ilişkilendirilen kişilik özelliği.
Çizimlerde harita ve ölçek yoktur; kutu boyları süreyi ya da önemi göstermez, yalnız sırayı ve ilişkiyi gösterir.
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


def _koyu(x, y, w, h, renk, rx=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{RENK[renk][2]}"/>'


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


def _aciklama(ic_ogeler, y):
    """Alttaki renk açıklaması: (renk, yazı) çiftleri soldan sağa dizilir."""
    ic = ''
    x = 14
    for renk, t in ic_ogeler:
        ic += f'<circle cx="{x + 6}" cy="{y - 4}" r="6" class="{RENK[renk][2]}"/>'
        ic += _yaz(x + 18, y, t, 12, False, 'g-s')
        x += 18 + _olc(t, 12) + 16
    return ic


def gorev_seridi():
    """Birinci Dünya Savaşı’na kadar görevler, sırayla (kitap s. 31-34)."""
    satirlar = [
        ('1907’ye kadar', 'Şam: 5. Ordu', 'mavi'),
        ('1909', 'Selânik: 3. Ordu karargâhı, kurmay şubesi', 'mavi'),
        ('1909', '31 Mart Olayı: Hareket Ordusu', 'turuncu'),
        ('1910', 'Fransa: Picardie Manevraları', 'yesil'),
        ('1911-1912', 'Trablusgarp: gönüllü subay olarak görev', 'turuncu'),
        ('1912-1913', 'Balkan Savaşları', 'turuncu'),
        ('1913', 'Sofya: ataşemiliter', 'mavi'),
    ]
    ic = '<line x1="67" y1="26" x2="67" y2="%d" class="g-c" stroke-width="3" stroke-linecap="round"/>' % (8 + 6 * 42 + 18)
    for i, (yil, gorev, renk) in enumerate(satirlar):
        y = 8 + i * 42
        ic += _koyu(8, y, 118, 36, renk, 18)
        ic += _yaz(67, y + 23, yil, 12.5, True, 'g-b', 'middle', 110)
        ic += _kutu(136, y, 336, 36, renk)
        ic += _yaz(148, y + 23, gorev, 12.5, False, 'g-y', None, 316)
    ic += _aciklama([('mavi', 'görev yeri'), ('turuncu', 'çatışma ya da olay'), ('yesil', 'manevra')], 8 + 7 * 42 + 14)
    return svg(480, 8 + 7 * 42 + 24, ic,
               'Birinci Dünya Savaşı’na kadar görevler sırasıyla: 1907’ye kadar Şam’daki 5. Ordu; 1909’da Selânik’te 3. Ordu’nun karargâhında kurmay şubesi; '
               '1909’da 31 Mart Olayı’nda Hareket Ordusu; 1910’da Fransa’da Picardie Manevraları; 1911-1912’de Trablusgarp’ta gönüllü subay olarak görev; '
               '1912-1913’te Balkan Savaşları; 1913’te Sofya’da ataşemiliter. Mavi görev yeri, turuncu çatışma ya da olay, yeşil manevradır.')


def trablusgarp_akisi():
    """Trablusgarp’ta olayların sırası (kitap s. 31-32)."""
    adimlar = [
        ('29 Eylül 1911', ['İtalya, Trablusgarp’ı işgal etti'], 'mavi'),
        ('18 Aralık 1911', ['Mustafa Kemal ile Enver Paşa’nın da', 'bulunduğu gönüllü subaylar gizlice gitti'], 'turuncu'),
        ('22 Aralık 1911', ['İtalyanlar bozguna uğratıldı;', 'Mustafa Kemal önemli rol oynadı'], 'turuncu'),
        ('1912', ['Balkan Savaşları başladı;', 'Mustafa Kemal İstanbul’a çağrıldı'], 'turuncu'),
        ('Uşi Antlaşması', ['On İki Ada geçici olarak, Trablusgarp', 'kalıcı olarak İtalya’ya bırakıldı'], 'mavi'),
    ]
    ic = '<defs>' + ok_isareti('okIta4a', 'g-s') + '</defs>'
    for i, (etiket, satirlar, renk) in enumerate(adimlar):
        y = 8 + i * 58
        ic += _koyu(8, y, 128, 44, renk, 22)
        ic += _yaz(72, y + 27, etiket, 12.5, True, 'g-b', 'middle', 120)
        ic += _kutu(146, y, 326, 44, renk)
        ic += _satirlar(146, y, 326, 44, satirlar)
        if i < len(adimlar) - 1:
            ic += f'<line x1="72" y1="{y + 45}" x2="72" y2="{y + 53}" class="g-c" stroke-width="1.5" marker-end="url(#okIta4a)"/>'
    ic += _aciklama([('mavi', 'olay ya da karar'), ('turuncu', 'Mustafa Kemal’in yer aldığı gelişme')], 8 + 5 * 58 + 8)
    return svg(480, 8 + 5 * 58 + 20, ic,
               'Trablusgarp’ta olayların sırası: 29 Eylül 1911’de İtalya Trablusgarp’ı işgal etti; 18 Aralık 1911’de Mustafa Kemal ile Enver Paşa’nın da bulunduğu '
               'gönüllü subaylar gizlice gitti; 22 Aralık 1911’de İtalyanlar bozguna uğratıldı ve Mustafa Kemal önemli rol oynadı; 1912’de Balkan Savaşları başladı ve '
               'Mustafa Kemal İstanbul’a çağrıldı; Uşi Antlaşması’yla On İki Ada geçici olarak, Trablusgarp kalıcı olarak İtalya’ya bırakıldı.')


def balkan_tablosu():
    """I. ve II. Balkan Savaşı yan yana (kitap s. 32-33)."""
    sutun = [(94, 187), (287, 185)]
    ic = ''
    for (x, w), ad, renk in zip(sutun, ('I. Balkan Savaşı', 'II. Balkan Savaşı'), ('mavi', 'turuncu')):
        ic += _koyu(x, 8, w, 28, renk, 14)
        ic += _yaz(x + w / 2, 27, ad, 14, True, 'g-b', 'middle', w - 16)
    satirlar = [
        (['Başlangıç'], 30, (['8 Ekim 1912'], ['29 Haziran 1913'])),
        (['Taraflar'], 56, (['Karadağ, Bulgaristan,', 'Sırbistan, Yunanistan', 'Osmanlı’ya karşı'],
                            ['Bulgaristan’a karşı', 'Yunanistan, Sırbistan,', 'Karadağ, Romanya'])),
        (['Osmanlı', 'durumu'], 56, (['Ağır yenilgi: siyasi', 'çekişme ve ordunun', 'hazır olmaması'],
                                        ['Edirne ve Kırklareli', 'geri alındı', 'Enver Paşa komutasında'])),
        (['Antlaşma'], 44, (['Londra Antlaşması:', 'sınır Midye-Enez hattı'],
                            ['İstanbul Antlaşması:', 'sınır Meriç Nehri'])),
    ]
    y = 44
    for etiket, h, (sol, sag) in satirlar:
        ic += f'<rect x="8" y="{y}" width="80" height="{h}" rx="10" class="g-z"/>'
        ic += f'<rect x="8" y="{y}" width="80" height="{h}" rx="10" class="g-c" stroke-width="1.5"/>'
        ic += _satirlar(8, y, 80, h, etiket, 12, True, 'g-y', 'middle', 4)
        for (x, w), metin, renk in zip(sutun, (sol, sag), ('mavi', 'turuncu')):
            ic += _kutu(x, y, w, h, renk)
            ic += _satirlar(x, y, w, h, metin)
        y += h + 6
    return svg(480, y + 2, ic,
               'I. ve II. Balkan Savaşı karşılaştırması: I. Balkan Savaşı 8 Ekim 1912’de Karadağ, Bulgaristan, Sırbistan ve Yunanistan’ın Osmanlı’ya karşı savaşıyla başladı; '
               'Osmanlı siyasi çekişme ve ordunun hazır olmaması yüzünden ağır yenilgi aldı; Londra Antlaşması’yla sınır Midye-Enez hattı oldu. '
               'II. Balkan Savaşı 29 Haziran 1913’te Bulgaristan’a karşı Yunanistan, Sırbistan, Karadağ ve Romanya ile başladı; Osmanlı Enver Paşa komutasında Edirne ve Kırklareli’ni geri aldı; '
               'İstanbul Antlaşması’yla sınır Meriç Nehri oldu.')


def olay_ozellik():
    """Olgu → kişilik özelliği (ilişkilendirme; kitap s. 30-31 sorularındaki özellik adlarıyla)."""
    satirlar = [
        (['Şam’da, adı Vatan ve Hürriyet olan', 'cemiyeti kurması'], 'vatanseverlik'),
        (['Trablusgarp’a gönüllü olarak,', 'gizlice gitmesi'], 'özveri'),
        (['Picardie’de edindiği bilgiyi', 'sonraki cephelerde uygulaması'], 'çalışkanlık'),
    ]
    ic = '<defs>' + ok_isareti('okIta4b', 'g-s') + '</defs>'
    for i, (olay, ozellik) in enumerate(satirlar):
        y = 8 + i * 58
        ic += _kutu(8, y, 286, 48, 'mavi')
        ic += _satirlar(8, y, 286, 48, olay)
        ic += f'<line x1="298" y1="{y + 24}" x2="320" y2="{y + 24}" class="g-c" stroke-width="2" marker-end="url(#okIta4b)"/>'
        ic += _kutu(330, y, 142, 48, 'turuncu')
        ic += _yaz(401, y + 29, ozellik, 14, True, 'g-y', 'middle', 126)
    ic += _aciklama([('mavi', 'olgu: ne yaptı'), ('turuncu', 'yorum: hangi özellikle ilişkili')], 8 + 3 * 58 + 8)
    return svg(480, 8 + 3 * 58 + 20, ic,
               'Olgudan kişilik özelliğine: Şam’da Vatan ve Hürriyet adlı cemiyeti kurması vatanseverlik ile; Trablusgarp’a gönüllü olarak ve gizlice gitmesi özveri ile; '
               'Picardie’de edindiği bilgiyi sonraki cephelerde uygulaması çalışkanlık ile ilişkilendirilir. Mavi olguyu, turuncu yorumu gösterir.')


def uygula(o):
    g = {
        'Görevlerin genel çerçevesi': gorev_seridi(),
        'Trablusgarp’ta gönüllü görev': trablusgarp_akisi(),
        'Balkan Savaşları': balkan_tablosu(),
        'Olaylardan kişilik özelliklerine': olay_ozellik(),
    }
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
