"""6. sınıf Din Kültürü ve Ahlak Bilgisi, 7. hafta: Bir Sure Öğreniyorum: Felak Suresi — felak kelimesi ve surenin
Kur’an içindeki yeri, dört kötülük–tek sığınak ilişki şeması, günlük durum–ayet eşlemesi ile sığınma + tedbir,
anlamı değiştirmeden özetleme süzgeci.

Görseller yalnız özet metnindeki (araclar/ozetler/6-din-kulturu-ve-ahlak-bilgisi-7.json) bilgilerle çizilir;
ders kitabı sayfası kullanılmamıştır.
Renk anlamı (bütün görsellerde aynı): mor = sığınılan kötülükler ve gece karanlığı; mavi = Allah’a sığınma (tek sığınak,
ana düşünce); turuncu = sabah aydınlığı (felak); yeşil = doğru davranış ve ölçüt (tedbir, özet süzgeci, iyi özet);
gri = yapı kutuları, günlük hayattan durumlar ve özete girmeyen eklemeler. Çizimler ölçeksizdir; yalnız ilişkiler
gösterilir. Dinî sembol, hat yazısı ve Arapça harf kullanılmaz.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12, kalinlik=2):
    """Açık dolgu + aynı renk çerçeve; renk='gri' ise yüzey dolgusu + gri çizgi."""
    if renk == 'gri':
        a, s = 'g-z', 'g-c'
    else:
        a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="{kalinlik}"/>')


def _yazi(x, y, metin, boyut=12.5, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def _hap(x, y, w, metin, renk, h=20, boyut=11.5):
    """Küçük etiket (ör. ayet numarası): yüzey dolgusu, renkli çerçeve ve renkli yazı (iki temada da okunur)."""
    _, s, f = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" class="{s}" stroke-width="1.5"/>'
            + _yazi(x + w / 2, y + h / 2 + 4, metin, boyut, True, f))


def _ok(x1, y1, x2, y2, kimlik, sinif='g-c', kalinlik=2):
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="{sinif}" stroke-width="{kalinlik}" '
            f'marker-end="url(#{kimlik})"/>')


def felak_ve_sure():
    """Sol: Kur’an → Felak suresi (113. sure, 5 ayet) → 1. ayetteki “felak” kelimesi (parça-bütün).
    Sağ: gece karanlığını yararak çıkan sabah aydınlığı (felak) ve surenin sığınmayla başlaması."""
    ic = '<defs>' + ok_isareti('ok6dk7a', 'g-tf') + '</defs>'
    # sol: parça-bütün kutuları (gri = yapı)
    ic += _kutu(8, 8, 236, 242, 'gri', 12, 1.5)
    ic += _yazi(126, 30, 'Kur’an-ı Kerim', 13, True)
    ic += _yazi(126, 47, 'sureler ve ayetlerden oluşur', 11.5, False, 'g-s')
    ic += _kutu(20, 58, 212, 182, 'gri', 10, 1.5)
    ic += _yazi(126, 79, 'Felak suresi', 13, True)
    ic += _yazi(126, 95, '113. sure, 5 ayet', 11.5, False, 'g-s')
    ic += _yazi(126, 110, 'adı 1. ayetteki kelimeden', 11.5, False, 'g-s')
    for k in range(5):
        y = 118 + k * 24
        if k == 0:
            ic += _kutu(32, y, 188, 20, 'turuncu', 6, 1.5)
            ic += _yazi(126, y + 14, '1. ayet: “felak”', 12, True)
        else:
            ic += _kutu(32, y, 188, 20, 'gri', 6, 1.2)
            ic += _yazi(126, y + 14, f'{k + 1}. ayet', 12, False, 'g-s')
    # sağ: gece karanlığı (mor) ve onu yararak çıkan sabah aydınlığı (turuncu); ölçeksiz
    ic += _kutu(256, 8, 216, 150, 'mor', 12)
    ic += '<polygon points="312,8 416,8 376,158 352,158" class="g-ta"/>'
    ic += '<polygon points="312,8 416,8 376,158 352,158" class="g-ts" stroke-width="2"/>'
    ic += _yazi(364, 36, 'sabah', 12, True) + _yazi(364, 52, 'aydınlığı', 12)
    for cx in (294, 434):
        ic += _yazi(cx, 98, 'gece', 12) + _yazi(cx, 114, 'karanlığı', 12)
    ic += _ok(346, 138, 300, 138, 'ok6dk7a', 'g-ts') + _ok(382, 138, 428, 138, 'ok6dk7a', 'g-ts')
    ic += _yazi(364, 176, 'Felak: “yarmak” kökünden;', 12)
    ic += _yazi(364, 192, 'karanlığı yarıp çıkan sabah', 12)
    ic += _yazi(364, 208, 'aydınlığı demektir.', 12)
    ic += _kutu(256, 216, 216, 36, 'mavi', 10)
    ic += _yazi(364, 230, 'Sure, sabah aydınlığının', 12) + _yazi(364, 246, 'Rabbine sığınmayla başlar.', 12, True)
    return svg(480, 260, ic, 'Felak suresinin yeri ve adı: Kur’an-ı Kerim surelerden, sureler ayetlerden oluşur; Felak suresi 113. suredir, '
               'beş ayettir ve adını 1. ayetteki felak kelimesinden alır. Yanda gece karanlığını yararak ortaya çıkan sabah aydınlığı '
               'çizilmiştir: felak, yarmak kökünden gelir ve sabah aydınlığı demektir. Sure, sabah aydınlığının Rabbine sığınmayla başlar.')


def dort_kotuluk_tek_siginak():
    """İlişki şeması: 2–5. ayetlerdeki dört kötülük (mor) oklarla tek sığınağa, Allah’a (mavi) bağlanır."""
    ic = '<defs>' + ok_isareti('ok6dk7b', 'g-s') + '</defs>'
    ic += _yazi(146, 26, 'Sığınılan dört kötülük', 14, True) + _yazi(406, 26, 'Tek sığınak', 14, True)
    kotulukler = [('2. ayet', 'Yaratılmışların kötülüğü', 'zarar verebilen her şey'),
                  ('3. ayet', 'Gecenin karanlığı', 'tehlikeler görünmez'),
                  ('4. ayet', 'Düğümlere üfleyenler', 'büyü yapan kişiler'),
                  ('5. ayet', 'Haset eden kişi', 'başkasının nimetini çekememe')]
    hedef_y = (142, 156, 170, 184)
    for k, (ayet, bas, alt) in enumerate(kotulukler):
        y = 44 + k * 62
        ic += _kutu(8, y, 276, 50, 'mor', 12)
        ic += _hap(16, y + 15, 56, ayet, 'mor')
        ic += _yazi(80, y + 21, bas, 12, True, 'g-y', 'start')
        ic += _yazi(80, y + 39, alt, 11.5, False, 'g-s', 'start')
        ic += _ok(288, y + 25, 335, hedef_y[k], 'ok6dk7b')
    ic += _kutu(340, 96, 132, 132, 'mavi', 14, 2.5)
    ic += _yazi(406, 134, 'Allah’a', 22, True, 'g-mf') + _yazi(406, 158, 'sığınırım', 13, True, 'g-mf')
    ic += _yazi(406, 188, 'sabah aydınlığının', 11.5) + _yazi(406, 204, 'Rabbi (1. ayet)', 11.5)
    ic += _yazi(240, 300, 'Dördünün kötülüğünden de yalnızca Allah’a sığınılır.', 12, True)
    ic += _yazi(240, 317, '2. ayet geneldir; 3, 4 ve 5. ayetler üç örnektir.', 11.5, False, 'g-s')
    return svg(480, 326, ic, 'Dört kötülük, tek sığınak şeması: 2. ayet yaratılmışların kötülüğü, 3. ayet gecenin karanlığı, 4. ayet düğümlere '
               'üfleyenler yani büyü yapanlar, 5. ayet haset eden kişi. Dört kutudan çıkan oklar tek bir kutuda birleşir: '
               'Allah’a sığınırım, sabah aydınlığının Rabbi (1. ayet). 2. ayet geneldir; 3, 4 ve 5. ayetler bunun içinden üç örnektir.')


def hayata_tasimak():
    """Günlük hayattan üç durum ilgili ayete bağlanır; altta sığınma (mavi) + tedbir (yeşil) toplamı."""
    ic = '<defs>' + ok_isareti('ok6dk7c', 'g-s') + '</defs>'
    ic += _yazi(135, 18, 'Günlük hayattan bir durum', 12, False, 'g-s') + _yazi(386, 18, 'İlgili ayet', 12, False, 'g-s')
    satirlar = [('Gece elektrikler kesilince', 'korkuyorsun', '3. ayet', 'gecenin', 'karanlığı'),
                ('Fal, uğur ve büyüye inanan', 'birini görüyorsun', '4. ayet', 'düğümlere', 'üfleyenler'),
                ('Bir arkadaşın başarını', 'kıskanıp seni üzüyor', '5. ayet', 'haset eden', 'kişi')]
    for k, (d1, d2, ayet, a1, a2) in enumerate(satirlar):
        y = 26 + k * 52
        ic += _kutu(8, y, 254, 44, 'gri', 10, 1.5)
        ic += _yazi(135, y + 18, d1, 12) + _yazi(135, y + 34, d2, 12)
        ic += _ok(266, y + 22, 292, y + 22, 'ok6dk7c')
        ic += _kutu(300, y, 172, 44, 'mor', 10)
        ic += _hap(308, y + 12, 56, ayet, 'mor')
        ic += _yazi(372, y + 18, a1, 12, True, 'g-y', 'start') + _yazi(372, y + 34, a2, 12, True, 'g-y', 'start')
    ic += _yazi(240, 200, 'Sığınmak tedbiri bırakmak değildir', 13, True)
    ornekler = [('Gece korkan çocuk:', 'Allah’a sığınır', 'ailesine seslenir'),
                ('Sınav kaygısı:', 'dua eder', 'çalışır')]
    for k, (durum, sigin, tedbir) in enumerate(ornekler):
        y = 212 + k * 46
        ic += _yazi(8, y + 23, durum, 12, False, 'g-y', 'start')
        ic += _kutu(142, y, 140, 36, 'mavi', 10) + _yazi(212, y + 23, sigin, 12, True)
        ic += _yazi(296, y + 24, '+', 18, True)
        ic += _kutu(310, y, 162, 36, 'yesil', 10) + _yazi(391, y + 23, tedbir, 12, True)
    ic += _yazi(240, 318, 'Yapabileceğini yap, sonra kalbini Allah’a emanet et.', 12)
    return svg(480, 330, ic, 'Sureyi hayata taşıma şeması: gece elektrikler kesilince korkmak 3. ayete (gecenin karanlığı), fal, uğur ve '
               'büyüye inanan birini görmek 4. ayete (düğümlere üfleyenler), bir arkadaşın başarını kıskanıp seni üzmesi 5. ayete '
               '(haset eden kişi) bağlanır. Sığınmak tedbiri bırakmak değildir: gece korkan çocuk Allah’a sığınır artı ailesine seslenir; '
               'sınav kaygısı olan dua eder artı çalışır. Yapabileceğini yap, sonra kalbini Allah’a emanet et.')


def ozet_suzgeci():
    """Özetleme akışı: sure meali (5 ayet) → üç ölçüt süzgeci → özet; surede olmayan eklemeler süzgeçte durdurulur."""
    ic = '<defs>' + ok_isareti('ok6dk7d', 'g-s') + '</defs>'
    # sure meali: 1. ayet sığınma (mavi), 2–5 kötülükler (mor)
    ic += _kutu(8, 10, 140, 156, 'gri', 10, 1.5) + _yazi(78, 32, 'Sure meali', 13, True)
    ayetler = [('1 Allah’a sığınma', 'mavi'), ('2 yaratılmışlar', 'mor'), ('3 gece karanlığı', 'mor'),
               ('4 büyü yapanlar', 'mor'), ('5 hasetçi', 'mor')]
    for k, (m, renk) in enumerate(ayetler):
        y = 42 + k * 24
        ic += _kutu(16, y, 124, 20, renk, 6, 1.5) + _yazi(78, y + 14, m, 11.5)
    ic += _ok(152, 88, 174, 88, 'ok6dk7d')
    # süzgeç: üç ölçüt (yeşil)
    ic += _kutu(178, 10, 156, 156, 'yesil', 10) + _yazi(256, 32, 'Üç ölçüt süzgeci', 13, True)
    for k, m in enumerate(['ana düşünce korunur', 'ayet sırası korunur', 'ekleme, çıkarma yok']):
        ic += _yazi(256, 62 + k * 24, m, 12)
    ic += _yazi(256, 150, 'kendi cümlelerinle', 11.5, False, 'g-s')
    ic += _ok(338, 88, 360, 88, 'ok6dk7d')
    # özet (yeşil = iyi özet)
    ic += _kutu(364, 10, 108, 156, 'yesil', 10) + _yazi(418, 32, 'Özet', 13, True)
    for k, m in enumerate(['kısa', 'sıralı', 'eksiksiz', 'anlamı aynı']):
        ic += _yazi(418, 62 + k * 24, m, 12, True)
    # süzgeçte durdurulan eklemeler (gri)
    ic += _yazi(256, 186, 'surede olmayan bilgi özete giremez', 11.5, False, 'g-s')
    ic += '<line x1="128" y1="194" x2="384" y2="194" class="g-c" stroke-width="4" stroke-linecap="round"/>'
    for k, (s1, s2) in enumerate([('kendi', 'yorumların'), ('duyduğun', 'hikâyeler'), ('kaynağı belli', 'olmayan sözler')]):
        x = 71 + k * 126
        ic += _kutu(x, 224, 118, 40, 'gri', 10, 1.5)
        ic += _yazi(x + 59, 240, s1, 11.5, False, 'g-s') + _yazi(x + 59, 256, s2, 11.5, False, 'g-s')
        ic += _ok(x + 59, 220, x + 59, 201, 'ok6dk7d')
    ic += _yazi(240, 286, '“Okuyana hiçbir kötülük dokunmaz” sözü surede yok.', 11.5, False, 'g-s')
    return svg(480, 296, ic, 'Özetleme süzgeci: sure mealindeki beş öge (Allah’a sığınma, yaratılmışlar, gece karanlığı, büyü yapanlar, '
               'hasetçi) üç ölçüt süzgecinden geçer: ana düşünce korunur, ayet sırası korunur, ekleme ve çıkarma yapılmaz; özet kısa, '
               'sıralı, eksiksiz ve anlamı aynı olur. Kendi yorumların, duyduğun hikâyeler ve kaynağı belli olmayan sözler süzgeçte durur: '
               'surede olmayan bilgi özete giremez. Örneğin okuyana hiçbir kötülük dokunmaz sözü surede yoktur.')


def uygula(o):
    g = {'Felak suresiyle tanışalım': felak_ve_sure(),
         'Surenin mesajları: dört kötülük, tek sığınak': dort_kotuluk_tek_siginak(),
         'Sureyi kendi hayatına taşımak': hayata_tasimak(),
         'Anlamı değiştirmeden özetlemek': ozet_suzgeci()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
