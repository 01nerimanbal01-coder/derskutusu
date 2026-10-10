"""6. sınıf Türkçe, 4. hafta: açıklayıcı metin yapısı, kabuk sözcükleri, Orhon Yazıtları, Türküz şiiri.

Görseller yalnız MEB 6. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s35-s45); metin cümleleri görsele alınmaz.
Renk anlamı:
- Üç bölüm: mavi = tanıtım, turuncu = açıklama/detaylandırma, yeşil = sonuç.
- Kabuk adları: mavi = hayvan kabukları, yeşil = bitki kabukları.
- Yazıtlar: mavi = vezirin yazıtı, turuncu = hükümdarların yazıtları; ince dal ve demet: mor = tek dal, yeşil = demet.
  Yazıt kartları yıl sırasıyla dizilir; aralıklar ölçekli değildir.
- Dörtlükler: mavi = "Türkçem" ile başlar, turuncu = tırnak işareti var, yeşil = şehir adı geçer.
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


def uc_bolum():
    """Açıklayıcı metnin üç bölümü (s35)."""
    ic = '<defs>' + ok_isareti('okB64', 'g-s') + '</defs>'
    bantlar = [
        ('mavi', ['Tanıtım'], ['Konuyu kısaca tanıtır,', 'temel bilgileri verir.']),
        ('turuncu', ['Açıklama /', 'detaylandırma'], ['Örnek ve açıklamalarla genişletir;', 'gerekirse alt başlık kullanır.']),
        ('yesil', ['Sonuç'], ['Ana fikri toparlar,', 'önemli noktaları hatırlatır.']),
    ]
    for k, (renk, etiket, aciklama) in enumerate(bantlar):
        y = 8 + k * 78
        ic += _kutu(8, y, 456, 62, renk)
        if len(etiket) == 1:
            ic += _yazi(22, y + 37, etiket[0], 14.5, RENK[renk][2], True)
        else:
            ic += _yazi(22, y + 28, etiket[0], 12.5, RENK[renk][2], True)
            ic += _yazi(22, y + 46, etiket[1], 12.5, RENK[renk][2], True)
        ic += f'<line x1="144" y1="{y + 10}" x2="144" y2="{y + 52}" class="{RENK[renk][1]}" stroke-width="1.5"/>'
        for i, s in enumerate(aciklama):
            ic += _yazi(158, y + 27 + i * 19, s, 12.5)
        if k < 2:
            ic += f'<line x1="73" y1="{y + 65}" x2="73" y2="{y + 75}" class="g-c" stroke-width="2.5" marker-end="url(#okB64)"/>'
    ic += _yazi(236, 252, 'Bilgileri tablo veya kavram haritasıyla görselleştir.', 11.5, 'g-s', False, 'middle')
    return svg(472, 260, ic, 'Açıklayıcı metnin üç bölümü sırayla: mavi, tanıtım; konuyu kısaca tanıtır, temel bilgileri verir. Turuncu, açıklama ve detaylandırma; '
               'örnek ve açıklamalarla genişletir, gerekirse alt başlık kullanır. Yeşil, sonuç; ana fikri toparlar, önemli noktaları hatırlatır. '
               'Bilgiler tablo veya kavram haritasıyla görselleştirilir.')


def kabuk_adlari():
    """Kabuk sözcükleri ve kabuğu taşıyan varlıklar (s39)."""
    ic = _yazi(120, 22, 'Hayvan kabukları', 14, 'g-mf', True, 'middle')
    ic += _yazi(352, 22, 'Bitki kabukları', 14, 'g-yf', True, 'middle')
    hayvan = [('Koza', 'İpekböceği'), ('Bağa', 'Kaplumbağa, kurbağa'), ('Kavkı', 'Salyangoz'), ('Kitin', 'Böcek')]
    bitki = [('Kapçık', 'Tahıl, ayçiçeği'), ('Kırış', 'Meyve'), ('Kışır, kışrı', 'Ağaç'), ('Gak', 'Ahlat')]
    for x, renk, liste in [(8, 'mavi', hayvan), (240, 'yesil', bitki)]:
        for k, (ad, sahip) in enumerate(liste):
            y = 34 + k * 56
            ic += _kutu(x, y, 224, 48, renk, rx=10)
            ic += _yazi(x + 14, y + 21, ad, 14, RENK[renk][2], True)
            ic += _yazi(x + 14, y + 39, sahip, 12)
    return svg(472, 258, ic, 'Kabuk adları ve sahipleri. Hayvan kabukları: koza ipekböceğinin, bağa kaplumbağa ve kurbağanın, kavkı salyangozun, kitin böceğin. '
               'Bitki kabukları: kapçık tahıl ve ayçiçeğinin, kırış meyvenin, kışır ya da kışrı ağacın, gak ahlatın.')


def tonyukuk():
    """Orhon Yazıtları ve ince dal–demet hikâyesi (s40-s41)."""
    ic = ''
    kartlar = [
        (6, 'mavi', ['Tonyukuk', 'Yazıtı'], '720', 'düşünülen yıl'),
        (161, 'turuncu', ['Kül Tigin', 'Yazıtı'], '732', 'dikildiği yıl'),
        (316, 'turuncu', ['Bilge Kağan', 'Yazıtı'], '735', 'dikildiği yıl'),
    ]
    for x, renk, baslik, yil, not_ in kartlar:
        ic += _kutu(x, 8, 150, 100, renk)
        ic += _yazi(x + 14, 30, baslik[0], 13, RENK[renk][2], True)
        ic += _yazi(x + 14, 47, baslik[1], 13, RENK[renk][2], True)
        ic += _yazi(x + 14, 76, yil, 22, 'g-y', True)
        ic += _yazi(x + 14, 97, not_, 11.5, 'g-s')
    ic += '<circle cx="18" cy="123" r="6" class="g-mf"/>' + _yazi(30, 127, 'Vezirin yazıtı', 11.5)
    ic += '<circle cx="150" cy="123" r="6" class="g-tf"/>' + _yazi(162, 127, 'Hükümdarların yazıtları', 11.5)
    ic += _yazi(236, 152, 'Üçü birlikte Orhon Yazıtları’nı oluşturur', 12.5, 'g-y', True, 'middle')
    # tek dal ve demet
    ic += _kutu(8, 168, 224, 84, 'mor')
    ic += _yazi(22, 192, 'Tek ince dal', 13, 'g-of', True)
    ic += '<line x1="22" y1="212" x2="118" y2="212" class="g-os" stroke-width="5" stroke-linecap="round"/>'
    ic += _yazi(22, 238, 'Kolay kırılır', 12)
    ic += _kutu(240, 168, 224, 84, 'yesil')
    ic += _yazi(254, 192, 'Dal demeti', 13, 'g-yf', True)
    for dy in (204, 212, 220):
        ic += f'<line x1="254" y1="{dy}" x2="350" y2="{dy}" class="g-ys" stroke-width="5" stroke-linecap="round"/>'
    ic += '<line x1="302" y1="199" x2="302" y2="225" class="g-c" stroke-width="3"/>'
    ic += _yazi(254, 244, 'Kırılması zor', 12)
    return svg(472, 260, ic, 'Orhon Yazıtları yıl sırasıyla: Tonyukuk Yazıtı 720, dikildiği düşünülen yıl, vezirin yazıtı; Kül Tigin Yazıtı 732 ve Bilge Kağan Yazıtı 735, '
               'hükümdarların yazıtları. Üçü birlikte Orhon Yazıtları’nı oluşturur. Altta tek ince dal kolay kırılır, dal demeti kırılması zordur.')


def dortlukler():
    """Şiirin sekiz dörtlüğü ve üç özellik (s43-s45)."""
    ic = ''
    ozellik = {1: 'M', 2: 'T', 3: '', 4: 'MT', 5: 'M', 6: '', 7: 'MS', 8: ''}
    yer = {'M': (-22, 'g-mf'), 'T': (0, 'g-tf'), 'S': (22, 'g-yf')}
    for n in range(1, 9):
        sutun = (n - 1) % 4
        satir = (n - 1) // 4
        x = 6 + sutun * 118
        y = 10 + satir * 76
        ic += f'<rect x="{x}" y="{y}" width="106" height="64" rx="10" class="g-z"/>'
        ic += f'<rect x="{x}" y="{y}" width="106" height="64" rx="10" class="g-c" stroke-width="1.5"/>'
        ic += _yazi(x + 53, y + 29, str(n), 20, 'g-y', True, 'middle')
        for harf in ozellik[n]:
            dx, sinif = yer[harf]
            ic += f'<circle cx="{x + 53 + dx}" cy="{y + 49}" r="6.5" class="{sinif}"/>'
    for k, (sinif, metin) in enumerate([('g-mf', '“Türkçem” ile başlayan dörtlük'), ('g-tf', 'Tırnak işareti kullanılan dörtlük'),
                                         ('g-yf', 'Şehir adı geçen dörtlük')]):
        y = 176 + k * 22
        ic += f'<circle cx="20" cy="{y}" r="6.5" class="{sinif}"/>' + _yazi(34, y + 4, metin, 12)
    ic += _yazi(14, 246, 'Noktası olmayan dörtlükte bu özellikler yoktur.', 11.5, 'g-s')
    return svg(472, 256, ic, 'Şiirin sekiz dörtlüğü ve özellikleri. Mavi nokta: Türkçem ile başlayan dörtlükler birinci, dördüncü, beşinci ve yedinci. '
               'Turuncu nokta: tırnak işareti kullanılan dörtlükler ikinci ve dördüncü. Yeşil nokta: şehir adı geçen dörtlük yedinci. '
               'Üçüncü, altıncı ve sekizinci dörtlükte bu özellikler yoktur.')


def uygula(o):
    g = {'Açıklayıcı metin yapısı': uc_bolum(),
         'Gözü boynuz, izi yaldız: kabuk sözcükleri': kabuk_adlari(),
         'Tonyukuk Yazıtı ve birliğin gücü': tonyukuk(),
         'Türküz, Türkçe Konuşuruz şiiri': dortlukler()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
