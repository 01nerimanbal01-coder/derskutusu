"""5. sınıf Sosyal Bilgiler, 7. hafta: Evimiz Dünya ünitesi, yaşadığı ilin göreceli konumu (SB.5.2.1).

Görseller yalnız özet metnindeki (araclar/ozetler/5-sosyal-bilgiler-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: il çevresi şemasında mor = ilim (tarif edilen il), turuncu = komşu il, mavi = su (deniz, akarsu), yeşil = dağlar,
gri kesik çizgi = ulaşım yolu; pusula gülünde mavi = ana yön, turuncu = ara yön; dört adımda mavi = kaynak toplama,
turuncu = özellikleri belirleme, yeşil = görselleştirme, mor = sözlü sunum; emanet şemasında mor = emanet (tarihî mekân ve
doğal güzellik), yeşil = koruyan (yapılacak) davranış, turuncu = zarar veren (yapılmayacak) davranış.
Ölçek: il çevresi şeması ölçeksizdir, gerçek bir il değildir, il sınırı çizilmez; üst taraf kuzey kabul edilir.
Pusula gülünde yönler gerçek açılarla yerleştirilmiştir (ana yönler 90°, ara yönler 45° arayla).
"""
import math

from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu/yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12, kalinlik=2):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="{kalinlik}"/>')


def _yazi(x, y, metin, boyut=12, kalin=False, sinif='g-y', hiza='middle'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{hiza}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def ilim_cevresi():
    """Göreceli konum: "ilim"in çevresindeki ögeler yönleriyle (ölçeksiz, sınırsız şema)."""
    ic = '<defs>' + ok_isareti('ok5sb7a', 'g-s') + '</defs>'
    # kuzey oku (sağ üst)
    ic += '<line x1="446" y1="56" x2="446" y2="30" class="g-c" stroke-width="2" marker-end="url(#ok5sb7a)"/>'
    ic += _yazi(446, 18, 'K', 13, True)
    # kuzeyde deniz
    ic += _kutu(96, 12, 280, 50, 'mavi', rx=10, kalinlik=1.5)
    ic += _yazi(236, 33, 'Kuzeyinde: deniz (kıyı)', 13, True, 'g-mf')
    for y in (46, 54):
        ic += f'<path d="M108 {y} q7 -4 14 0' + ' t14 0' * 17 + '" class="g-ms" stroke-width="1.5"/>'
    # ilim ve komşular
    ic += '<rect x="186" y="150" width="100" height="50" rx="12" class="g-of"/>'
    ic += _yazi(236, 181, 'İlim', 16, True, 'g-b')
    for x, yon in ((24, 'Batısında'), (338, 'Doğusunda')):
        ic += _kutu(x, 150, 110, 50, 'turuncu')
        ic += _yazi(x + 55, 171, yon, 12.5, True, 'g-tf')
        ic += _yazi(x + 55, 189, 'komşu il', 12)
    # batıdaki komşuya ulaşım yolu
    ic += '<line x1="138" y1="175" x2="182" y2="175" class="g-c" stroke-width="3" stroke-dasharray="7 4"/>'
    ic += _yazi(160, 141, 'ulaşım yolu', 11.5, False, 'g-s')
    # akarsu: güneydeki dağlardan kuzeydeki denize, ilin doğusundan geçer
    ic += ('<path d="M304 236 C 312 220, 318 206, 312 190 C 306 174, 318 160, 312 144 C 306 128, 320 112, 314 96 '
           'C 308 80, 316 70, 312 62" class="g-ms" stroke-width="3" stroke-linecap="round"/>')
    ic += _yazi(330, 118, 'Akarsu', 12.5, True, 'g-mf', 'start')
    # güneyde dağlar
    ic += _kutu(140, 236, 192, 64, 'yesil')
    ic += _yazi(236, 254, 'Güneyinde: dağlar', 13, True, 'g-yf')
    for p in ('156,294 188,266 220,294', '204,294 236,264 268,294', '252,294 284,268 316,294'):
        ic += f'<polygon points="{p}" class="g-yf"/>'
    # dipnot
    ic += _yazi(236, 322, 'Göreceli konum çevreye göre anlatılır, değişebilir;', 12, False, 'g-s')
    ic += _yazi(236, 339, 'mutlak konum enlem–boylamla belirlenir, değişmez.', 12, False, 'g-s')
    ic += _yazi(464, 339, 'ölçeksiz', 11.5, False, 'g-s', 'end')
    return svg(472, 348, ic, 'Göreceli konum şeması (ölçeksiz, sınır çizgisi yok): ortada ilim; kuzeyinde deniz kıyısı, doğusunda ve batısında '
               'birer komşu il, güneyinde dağlar; dağlardan denize akan bir akarsu ilin doğusundan geçer; batıdaki komşuya bir ulaşım yolu '
               'bağlanır. Göreceli konum çevreye göre anlatılır ve değişebilir; mutlak konum enlem ve boylamla belirlenir, değişmez.')


def _uc(cx, cy, aci, R, w, renk):
    """Pusula ucu: açı derece (0 kuzey, saat yönü), R uzunluk, w yarım genişlik; iki yarım (koyu/açık) ve çerçeve."""
    a, s, f = RENK[renk]
    t = math.radians(aci)
    tx, ty = cx + R * math.sin(t), cy - R * math.cos(t)
    px, py = w * math.cos(t), w * math.sin(t)
    s1 = f'{cx + px:.1f},{cy + py:.1f}'
    s2 = f'{cx - px:.1f},{cy - py:.1f}'
    uc = f'{tx:.1f},{ty:.1f}'
    return (f'<polygon points="{uc} {s1} {cx},{cy}" class="{f}"/>'
            f'<polygon points="{uc} {cx},{cy} {s2}" class="{a}"/>'
            f'<polygon points="{uc} {s1} {cx},{cy} {s2}" class="{s}" stroke-width="1" stroke-linejoin="round"/>')


def pusula_gulu():
    """Pusula gülü: dört ana yön, dört ara yön; harita kuralı ve vücutla yön bulma."""
    cx, cy = 140, 150
    ic = f'<circle cx="{cx}" cy="{cy}" r="84" class="g-c" stroke-width="1"/>'
    for aci in (45, 135, 225, 315):
        ic += _uc(cx, cy, aci, 50, 7, 'turuncu')
    for aci in (0, 90, 180, 270):
        ic += _uc(cx, cy, aci, 74, 10, 'mavi')
    ic += f'<circle cx="{cx}" cy="{cy}" r="8" class="g-z"/><circle cx="{cx}" cy="{cy}" r="8" class="g-c" stroke-width="1.5"/>'
    # ana yön adları (mavi)
    ic += _yazi(cx, cy - 92, 'Kuzey', 13.5, True, 'g-mf')
    ic += _yazi(cx, cy + 102, 'Güney', 13.5, True, 'g-mf')
    ic += _yazi(cx + 92, cy + 4.5, 'Doğu', 13.5, True, 'g-mf', 'start')
    ic += _yazi(cx - 92, cy + 4.5, 'Batı', 13.5, True, 'g-mf', 'end')
    # ara yön adları (turuncu)
    d = 69
    ic += _yazi(cx + d, cy - d + 4, 'Kuzeydoğu', 12.5, True, 'g-tf', 'start')
    ic += _yazi(cx - d, cy - d + 4, 'Kuzeybatı', 12.5, True, 'g-tf', 'end')
    ic += _yazi(cx + d, cy + d + 8, 'Güneydoğu', 12.5, True, 'g-tf', 'start')
    ic += _yazi(cx - d, cy + d + 8, 'Güneybatı', 12.5, True, 'g-tf', 'end')
    ic += _yazi(cx, 284, 'Güneş doğudan doğar, batıdan batar.', 12, False, 'g-s')
    # sağ kart: açıklamalar
    ic += '<rect x="296" y="8" width="168" height="264" rx="12" class="g-z"/>'
    ic += '<rect x="296" y="8" width="168" height="264" rx="12" class="g-c" stroke-width="1.5"/>'
    x0 = 308
    satirlar = [(32, 'Ana yönler', 13, True, 'g-mf'), (48, 'kuzey, güney,', 12, False, 'g-y'), (64, 'doğu, batı', 12, False, 'g-y'),
                (90, 'Ara yönler', 13, True, 'g-tf'), (106, 'kuzeydoğu, kuzeybatı,', 12, False, 'g-y'), (122, 'güneydoğu, güneybatı', 12, False, 'g-y'),
                (148, 'Haritada ok yoksa', 12.5, True, 'g-y'), (164, 'üst kuzey, alt güney,', 12, False, 'g-y'), (180, 'sağ doğu, sol batı.', 12, False, 'g-y'),
                (206, 'Kuzeye dönünce', 12.5, True, 'g-y'), (222, 'sağ kol doğu,', 12, False, 'g-y'), (238, 'sol kol batı,', 12, False, 'g-y'),
                (254, 'sırt güney.', 12, False, 'g-y')]
    for y, t, boyut, kalin, sinif in satirlar:
        ic += _yazi(x0, y, t, boyut, kalin, sinif, 'start')
    return svg(472, 296, ic, 'Pusula gülü: üstte kuzey, altta güney, sağda doğu, solda batı (ana yönler); aralarında kuzeydoğu, kuzeybatı, '
               'güneydoğu ve güneybatı (ara yönler). Güneş doğudan doğar, batıdan batar. Haritada ok yoksa üst taraf kuzey, alt güney, '
               'sağ doğu, sol batıdır. Yüzünü kuzeye dönünce sağ kolun doğuyu, sol kolun batıyı, sırtın güneyi gösterir.')


def dort_adim():
    """Kendi ilini incele: kaynak topla, özellikleri belirle, görselleştir, sözlü sun."""
    ic = '<defs>' + ok_isareti('ok5sb7c', 'g-s') + '</defs>'
    adim = [('mavi', 'Kaynak topla', 66, ('Atlas, haritalar, valilik ve belediye sayfaları,', 'büyükler; her bilgiyi en az iki kaynaktan doğrula.')),
            ('turuncu', 'Özellikleri belirle', 66, ('Kesim, deniz, komşu iller ve yönleri, dağ, ova,', 'akarsu, göl, tarihî mekânlar, ulaşım, komşu ülke.')),
            ('yesil', 'Görselleştir', 82, ()),
            ('mor', 'Sözlü sunum (iki üç dakika)', 66, ('Yön sözcüklerini kullan, en önemli üç özelliği', 'vurgula, kaynaklarını söyle, soruları cevapla.'))]
    y = 8
    merkezler = []
    for i, (renk, baslik, h, satir) in enumerate(adim, 1):
        a, s, f = RENK[renk]
        cy = y + h / 2
        merkezler.append(cy)
        ic += f'<circle cx="30" cy="{cy:g}" r="16" class="{f}"/>'
        ic += _yazi(30, cy + 5, str(i), 14, True, 'g-b')
        ic += _kutu(58, y, 406, h, renk)
        ic += _yazi(72, y + 22, baslik, 13, True, f, 'start')
        for k, t in enumerate(satir):
            ic += _yazi(72, y + 41 + k * 17, t, 12, False, 'g-y', 'start')
        if renk == 'yesil':
            for x, w, t in ((72, 56, 'Tablo'), (136, 190, 'Dilsiz mülki idare haritası'), (334, 88, 'Bilgi kartı')):
                ic += f'<rect x="{x}" y="{y + 32}" width="{w}" height="26" rx="13" class="{f}"/>'
                ic += _yazi(x + w / 2, y + 49, t, 12, True, 'g-b')
            ic += _yazi(72, y + 76, 'Tablo sıralar, harita yön gösterir, kart tanıtır.', 12, False, 'g-y', 'start')
        y += h + 10
    for c1, c2 in zip(merkezler, merkezler[1:]):
        ic += f'<line x1="30" y1="{c1 + 19:g}" x2="30" y2="{c2 - 22:g}" class="g-c" stroke-width="2" marker-end="url(#ok5sb7c)"/>'
    return svg(472, y - 2, ic, 'Kendi ilini inceleme adımları: 1 kaynak topla (atlas, haritalar, valilik ve belediye sayfaları, büyükler; her bilgiyi '
               'en az iki kaynaktan doğrula), 2 özellikleri belirle (kesim, deniz, komşu iller ve yönleri, dağ, ova, akarsu, göl, tarihî mekânlar, '
               'ulaşım, komşu ülke), 3 görselleştir (tablo sıralar, dilsiz mülki idare haritası yön gösterir, bilgi kartı tanıtır), '
               '4 iki üç dakikalık sözlü sunum (yön sözcüklerini kullan, en önemli üç özelliği vurgula, kaynaklarını söyle, soruları cevapla).')


def emanet_koru():
    """Doğal güzellikler ve tarihî mekânlar: emanet, korunmazsa yok olur; koruyan ve zarar veren davranışlar."""
    ic = '<defs>' + ok_isareti('ok5sb7d', 'g-s') + '</defs>'
    ic += _kutu(8, 8, 456, 66, 'mor')
    ic += _yazi(236, 30, 'Gelecek nesillere emanet', 13.5, True, 'g-of')
    ic += _yazi(236, 49, 'antik kentler, kaleler, camiler, köprüler,', 12)
    ic += _yazi(236, 65, 'millî parklar, göller, şelaleler', 12)
    ic += '<line x1="236" y1="78" x2="236" y2="88" class="g-c" stroke-width="2" marker-end="url(#ok5sb7d)"/>'
    ic += _yazi(236, 108, 'Korunmazsa yok olur, bir daha geri gelmez.', 12.5, True)
    sutun = [(8, 'yesil', 'Böyle koru', ('Çöpünü yanında götür', 'Koruma kurallarına uy', 'Zararı yetkililere bildir', 'Tanıtım panosu hazırla')),
             (240, 'turuncu', 'Bunları yapma', ('Tarihî taşlara yazı yazma', 'Doğal alanda ateş yakma', 'Kirletme, zarar verme'))]
    for x, renk, baslik, maddeler in sutun:
        a, s, f = RENK[renk]
        ic += _kutu(x, 122, 224, 120, renk)
        ic += _yazi(x + 112, 144, baslik, 13, True, f)
        for k, t in enumerate(maddeler):
            yy = 166 + k * 20
            ix = x + 22
            if renk == 'yesil':
                ic += f'<path d="M{ix - 5} {yy - 4} L{ix - 1} {yy} L{ix + 6} {yy - 8}" class="{s}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
            else:
                ic += f'<path d="M{ix - 5} {yy - 9} L{ix + 5} {yy + 1} M{ix + 5} {yy - 9} L{ix - 5} {yy + 1}" class="{s}" stroke-width="2.5" stroke-linecap="round"/>'
            ic += _yazi(x + 36, yy, t, 12, False, 'g-y', 'start')
    return svg(472, 250, ic, 'Gelecek nesillere emanet: antik kentler, kaleler, camiler, köprüler, millî parklar, göller, şelaleler; korunmazsa '
               'yok olur, bir daha geri gelmez. Böyle koru: çöpünü yanında götür, koruma kurallarına uy, zararı yetkililere bildir, '
               'tanıtım panosu hazırla. Bunları yapma: tarihî taşlara yazı yazma, doğal alanda ateş yakma, kirletme, zarar verme.')


def uygula(o):
    g = {'Konum nedir, göreceli konum nedir?': ilim_cevresi(),
         'Yönünü bul: ana ve ara yönler': pusula_gulu(),
         'Kendi ilini incele: dört adım': dort_adim(),
         'Doğal güzellikler ve tarihî mekânlar: gelecek nesillere emanet': emanet_koru()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
