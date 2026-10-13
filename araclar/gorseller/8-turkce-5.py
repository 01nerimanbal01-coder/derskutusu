"""8. sınıf Türkçe, 5. hafta: Bu Vatan Kimin? (şiirdeki sözcükler, kişileştirme ve benzetme, akrostiş, yüklem).

Görseller yalnız MEB 8. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s37-s41); şiirden dize alıntısı yapılmaz,
yüklem örnekleri kurgusaldır ve özet metnindeki cümlelerle aynıdır.
Renk anlamı:
- Şiirdeki sözcükler: mavi = sözcük, turuncu = anlamı.
- Kişileştirme ve benzetme: mavi = anlatılan varlık ya da şey, turuncu = ona verilen insan niteliği ya da kendisine benzetilen şey,
  yeşil = benzetmedeki ortak özellik, mor = söz sanatının adı.
- Akrostiş: mavi = VATAN harfleri, turuncu = SEVGİSİ harfleri.
- Yüklem: turuncu = yüklem, yeşil = fiilimsi (yüklem değil), gri = diğer sözcükler.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı/dolgu)
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


def _gri(x, y, w, h, rx=8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.6"/>')


def sozcukler():
    """Şiirdeki sekiz sözcük ve anlamları (s38)."""
    ic = '<defs>' + ok_isareti('okH5a', 'g-s') + '</defs>'
    satir = [('şahlanmak', 'Atın arka ayakları üstünde durması'),
             ('hudut', 'Ulaşılabilecek son nokta; sınır'),
             ('bağır', 'Göğüs'),
             ('gazâ', 'Dinî amaçla yürütülen kutsal savaş'),
             ('yakut', 'Koyu kırmızı, saydam, değerli taş'),
             ('ziyade', 'Çok, daha çok, fazla'),
             ('gazi', 'Savaştan sağ dönen kişi'),
             ('hasım', 'Düşman; oyunda, yarışta karşı taraf')]
    for k, (s, a) in enumerate(satir):
        y = 8 + k * 42
        ic += _kutu(8, y, 130, 34, 'mavi', rx=10) + _yazi(73, y + 22.5, s, 14, 'g-mf', True, 'middle')
        ic += f'<line x1="146" y1="{y + 17}" x2="168" y2="{y + 17}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okH5a)"/>'
        ic += _kutu(176, y, 288, 34, 'turuncu', rx=10) + _yazi(190, y + 22, a, 12.5, 'g-y')
    ic += '<circle cx="20" cy="354" r="6" class="g-mf"/>' + _yazi(32, 358, 'Sözcük', 12)
    ic += '<circle cx="112" cy="354" r="6" class="g-tf"/>' + _yazi(124, 358, 'Sözlükteki anlamı', 12)
    return svg(472, 370, ic, 'Şiirdeki sekiz sözcük ve anlamları: şahlanmak, atın arka ayakları üstünde durması; hudut, ulaşılabilecek son nokta, yani sınır; '
               'bağır, göğüs; gazâ, dinî amaçla yürütülen kutsal savaş; yakut, koyu kırmızı, saydam, değerli taş; ziyade, çok, daha çok, fazla; '
               'gazi, savaştan sağ dönen kişi; hasım, düşman ya da oyunda ve yarışta karşı taraf. Mavi kutularda sözcükler, turuncu kutularda anlamları var.')


def sanatlar():
    """Kişileştirme ve benzetme yan yana (s40)."""
    ic = '<defs>' + ok_isareti('okH5b', 'g-s') + '</defs>'
    # sol panel: kişileştirme
    ic += _gri(8, 8, 224, 250, rx=12)
    ic += _yazi(120, 32, 'Kişileştirme (teşhis)', 14, 'g-y', True, 'middle')
    ic += _yazi(120, 56, 'İnsan olmayan varlıklar', 11.5, 'g-s', False, 'middle')
    ic += _kutu(22, 64, 196, 38, 'mavi', rx=10) + _yazi(120, 88.5, 'Nehirler, dağlar', 14, 'g-mf', True, 'middle')
    ic += '<line x1="76" y1="108" x2="76" y2="130" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okH5b)"/>'
    ic += _yazi(86, 123, 'insan niteliği verilir', 11, 'g-y')
    ic += _kutu(22, 138, 196, 38, 'turuncu', rx=10) + _yazi(120, 162.5, 'gazi, kahraman', 14, 'g-tf', True, 'middle')
    ic += _yazi(120, 190, 'İnsana özgü nitelikler', 11.5, 'g-s', False, 'middle')
    ic += '<rect x="46" y="224" width="148" height="26" rx="13" class="g-of"/>' + _yazi(120, 241.5, 'Sonuç: kişileştirme', 12.5, 'g-b', True, 'middle')
    # sağ panel: benzetme
    ic += _gri(240, 8, 224, 250, rx=12)
    ic += _yazi(352, 32, 'Benzetme (teşbih)', 14, 'g-y', True, 'middle')
    ic += _yazi(352, 56, 'Anlatılan şey', 11.5, 'g-s', False, 'middle')
    ic += _kutu(254, 64, 196, 38, 'mavi', rx=10) + _yazi(352, 88.5, 'Vatanın taşları', 14, 'g-mf', True, 'middle')
    ic += '<line x1="308" y1="108" x2="308" y2="130" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okH5b)"/>'
    ic += _yazi(320, 123, 'benzetilir', 11.5, 'g-y')
    ic += _kutu(254, 138, 196, 38, 'turuncu', rx=10) + _yazi(352, 162.5, 'Yakut', 14, 'g-tf', True, 'middle')
    ic += _yazi(352, 190, 'Kendisine benzetilen şey', 11.5, 'g-s', False, 'middle')
    ic += '<rect x="268" y="196" width="168" height="22" rx="11" class="g-yf"/>' + _yazi(352, 211.5, 'Ortak özellik: değerli', 12, 'g-b', True, 'middle')
    ic += '<rect x="278" y="224" width="148" height="26" rx="13" class="g-of"/>' + _yazi(352, 241.5, 'Sonuç: benzetme', 12.5, 'g-b', True, 'middle')
    ic += _yazi(8, 278, 'Mavi: anlatılan varlık ya da şey.', 11.5, 'g-y')
    ic += _yazi(8, 295, 'Turuncu: ona verilen nitelik ya da benzetilen şey.', 11.5, 'g-y')
    ic += _yazi(8, 312, 'Yeşil: benzetmede iki şeyi birbirine bağlayan ortak özellik.', 11.5, 'g-y')
    ic += _yazi(8, 329, 'Mor: söz sanatının adı.', 11.5, 'g-y')
    return svg(472, 340, ic, 'Kişileştirme ve benzetme karşılaştırması. Solda kişileştirme: insan olmayan varlıklar olan nehirler ve dağlara gazi ve kahraman gibi insana özgü nitelikler verilir. '
               'Sağda benzetme: anlatılan şey olan vatanın taşları, kendisine benzetilen şey olan yakuta benzetilir; ortak özellik değerli olmaktır. '
               'Mavi anlatılan varlık ya da şey, turuncu ona verilen nitelik ya da benzetilen şey, yeşil ortak özellik, mor söz sanatının adıdır.')


def akrostis():
    """Vatan sevgisi akrostişi: iki sözcük, on iki harf, on iki dize (s39)."""
    ic = ''
    harfler1, harfler2 = 'VATAN', 'SEVGİSİ'

    def grup(harfler, y0, renk):
        s = ''
        for k, h in enumerate(harfler):
            y = y0 + k * 26
            s += f'<circle cx="26" cy="{y + 11}" r="11" class="{RENK[renk][2]}"/>' + _yazi(26, y + 16, h, 13, 'g-b', True, 'middle')
            s += _kutu(48, y, 236, 22, renk, rx=6)
            s += _yazi(60, y + 15, 'dize', 11, 'g-s')
        y1, y2 = y0, y0 + (len(harfler) - 1) * 26 + 22
        c = RENK[renk][1]
        s += f'<path d="M294 {y1} h8 v{y2 - y1} h-8" class="{c}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        yo = (y1 + y2) / 2
        s += _yazi(312, yo - 2, ''.join(harfler), 14, RENK[renk][2], True)
        s += _yazi(312, yo + 15, f'{len(harfler)} dize', 12.5, 'g-y')
        return s
    ic += grup(harfler1, 10, 'mavi')
    ic += grup(harfler2, 10 + 5 * 26 + 18, 'turuncu')
    ic += '<rect x="312" y="302" width="150" height="30" rx="15" class="g-z"/><rect x="312" y="302" width="150" height="30" rx="15" class="g-c" stroke-width="1.6"/>'
    ic += _yazi(387, 322, 'Toplam: 12 dize', 13, 'g-y', True, 'middle')
    return svg(472, 346, ic, 'Vatan sevgisi akrostişi: konu iki sözcük olduğu için harfler iki grup kurar. Mavi grupta V, A, T, A, N harfleri ve beş dize; '
               'turuncu grupta S, E, V, G, İ, S, İ harfleri ve yedi dize bulunur. Her harf bir dizenin başına gelir; toplam on iki dize olur.')


def yuklem():
    """Yüklem: çekimli fiil, fiilimsi çeldiricisi ve ad öbeği olan yüklem; örnekler kurgusaldır."""
    def gen(t, boyut=13):
        return round(len(t) * boyut * 0.58 + 22)

    def cip(x, y, t, tur):
        w = gen(t)
        if tur == 'yuklem':
            s = f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="10" class="g-tf"/>' + _yazi(x + w / 2, y + 21, t, 13, 'g-b', True, 'middle')
        elif tur == 'fiilimsi':
            s = _kutu(x, y, w, 32, 'yesil', rx=10) + _yazi(x + w / 2, y + 21, t, 13, 'g-y', True, 'middle')
        else:
            s = _gri(x, y, w, 32, rx=10) + _yazi(x + w / 2, y + 21, t, 13, 'g-y', False, 'middle')
        return s, w

    satirlar = [
        [('Köylüler', 'diger'), ('meydanda', 'diger'), ('toplandı', 'yuklem')],
        [('Bayrağı göndere', 'diger'), ('çekerek', 'fiilimsi'), ('meydandan', 'diger'), ('ayrıldı', 'yuklem')],
        [('Bu şiir', 'diger'), ('unutulmaz bir eserdir', 'yuklem')],
    ]
    etiket = {'toplandı': 'yüklem: çekimli fiil', 'çekerek': 'zarf-fiil: yüklem değil', 'ayrıldı': 'yüklem: çekimli fiil',
              'unutulmaz bir eserdir': 'yüklem: yargıyı ad öbeği taşır'}
    ic = ''
    for k, satir in enumerate(satirlar):
        y = 10 + k * 76
        x = 8
        for t, tur in satir:
            s, w = cip(x, y, t, tur)
            ic += s
            if t in etiket:
                renk = {'yuklem': 'g-tf', 'fiilimsi': 'g-yf'}[tur]
                ic += _yazi(x + w / 2, y + 50, etiket[t], 11.5, renk, True, 'middle')
            x += w + 8
    ic += '<circle cx="20" cy="252" r="6" class="g-tf"/>' + _yazi(32, 256, 'Yüklem', 12)
    ic += '<circle cx="112" cy="252" r="6" class="g-yf"/>' + _yazi(124, 256, 'Fiilimsi (yüklem değil)', 12)
    ic += '<circle cx="300" cy="252" r="6" class="g-s"/>' + _yazi(312, 256, 'Diğer sözcükler', 12)
    return svg(472, 270, ic, 'Yüklemi bulma örnekleri. Birinci cümlede köylüler meydanda toplandı: yüklem toplandı, çekimli fiil. '
               'İkinci cümlede bayrağı göndere çekerek meydandan ayrıldı: çekerek zarf-fiildir ve yüklem değildir, yüklem ayrıldı. '
               'Üçüncü cümlede bu şiir unutulmaz bir eserdir: yargıyı unutulmaz bir eserdir ad öbeği taşır ve yüklem odur. '
               'Turuncu yüklem, yeşil fiilimsi, gri diğer sözcüklerdir.')


def uygula(o):
    g = {'Sözcüğün anlamını sözlükle doğrula': sozcukler(),
         'Söz sanatları: kişileştirme ve benzetme': sanatlar(),
         'Akrostiş: baş harfler bir sözcük kurar': akrostis(),
         'Cümlenin yüklemini bul': yuklem()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
