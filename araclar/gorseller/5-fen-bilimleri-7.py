"""5. sınıf Fen Bilimleri, 7. hafta: Kuvvet ve Kuvvetin Ölçülmesi (ünite: Kuvveti Tanıyalım).

Görseller yalnız özet metnindeki (araclar/ozetler/5-fen-bilimleri-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: turuncu ok = itme kuvveti; mavi ok = çekme kuvveti (kesikli mavi ok = cisme dokunmadan etki eden çekme);
mor = esnek cisim (yay, lastik); yeşil = yayın uzama miktarı ve ölçek işaretleri; gri/nötr kutular = kuvvet uygulanan cisimler
ve araç parçaları (karton, kanca, kapı). Ok uzunluğu kuvvetin büyüklüğünü gösterir.
Ölçek: yay uzamaları ve ok uzunlukları birbirine orantılı çizilmiştir, gerçek ölçüde değildir (görsellerde "ölçeksiz" yazılır).
"""
from ozet_gorsel import svg, ok_isareti


def _kutu(x, y, w, h, rx=10, dolgu='g-z', cerceve='g-c', kalinlik=1.8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{dolgu}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cerceve}" stroke-width="{kalinlik}"/>')


def _yazi(x, y, metin, boy=12.5, sinif='g-y', hiza='start', kalin=''):
    k = f' font-weight="{kalin}"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, sinif, kimlik, kalinlik=2.6, kesik=False):
    k = ' stroke-dasharray="6 4"' if kesik else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{sinif}" stroke-width="{kalinlik}"{k} '
            f'marker-end="url(#{kimlik})"/>')


def _yay(x, y0, boy, n=8, a=12):
    """Dikey zikzak yay: tepesi (x, y0), toplam uzunluğu boy. Sarım sayısı sabittir; yay uzadıkça sarımlar açılır."""
    uc = 8
    adim = (boy - 2 * uc) / n
    d = f'M{x} {y0} v{uc}'
    for i in range(n):
        d += f' L{x + (a if i % 2 == 0 else -a)} {y0 + uc + adim * (i + 0.5):.1f}'
    d += f' L{x} {y0 + boy - uc} v{uc}'
    return f'<path d="{d}" class="g-os" stroke-width="2.4" stroke-linejoin="round"/>'


def _olcu(x, y1, y2):
    """Dikey uzama ölçüsü: yeşil çizgi ve iki uçta kısa çentik."""
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" class="g-ys" stroke-width="2"/>'
            f'<line x1="{x - 6}" y1="{y1}" x2="{x + 6}" y2="{y1}" class="g-ys" stroke-width="2"/>'
            f'<line x1="{x - 6}" y1="{y2}" x2="{x + 6}" y2="{y2}" class="g-ys" stroke-width="2"/>')


def _lastik(x, y0, boy):
    """Paket lastiği: ince, uzun bir halka (mor çizgi)."""
    return f'<rect x="{x - 5}" y="{y0}" width="10" height="{boy}" rx="5" class="g-os" stroke-width="2.4"/>'


def _kanca(x, y0):
    """Ataştan kanca: kısa dikey tel ve altta açık bir yay."""
    return f'<path d="M{x} {y0} v8 a7 7 0 0 0 14 0 v-3" class="g-c" stroke-width="2" stroke-linecap="round"/>'


def _isaret(x, y, ad):
    """Karton üzerindeki ölçek işareti: yeşil çentik ve sağında adı."""
    return (f'<line x1="{x}" y1="{y}" x2="{x + 14}" y2="{y}" class="g-ys" stroke-width="2.2"/>'
            + _yazi(x + 19, y + 4, ad, 12.5, 'g-yf', kalin='800'))


def itme_cekme():
    """Kuvvet itme ya da çekmedir: itme cismi uzaklaştırır, çekme yaklaştırır; mıknatıs ve Dünya dokunmadan çeker."""
    ic = '<defs>' + ok_isareti('ok5fen7a', 'g-tf') + ok_isareti('ok5fen7b', 'g-mf') + '</defs>'
    ic += _yazi(20, 18, 'Kuvvet: bir cisme uygulanan itme ya da çekme', 14, kalin='800')
    for cy, cisim in ((62, 'Kapı'), (128, 'Çekmece')):
        ic += f'<circle cx="46" cy="{cy}" r="20" class="g-z"/><circle cx="46" cy="{cy}" r="20" class="g-c" stroke-width="2"/>'
        ic += _yazi(46, cy + 4, 'Sen', 13, hiza='middle', kalin='800')
        ic += _kutu(140, cy - 20, 86, 40) + _yazi(183, cy + 4, cisim, 13, hiza='middle', kalin='700')
    ic += _ok(72, 62, 134, 62, 'g-ts', 'ok5fen7a') + _yazi(103, 50, 'itme', 12.5, 'g-tf', 'middle', '800')
    ic += _yazi(244, 57, 'İtme: cismi kendinden') + _yazi(244, 74, 'uzaklaştırır.')
    ic += _ok(134, 128, 72, 128, 'g-ms', 'ok5fen7b') + _yazi(103, 116, 'çekme', 12.5, 'g-mf', 'middle', '800')
    ic += _yazi(244, 123, 'Çekme: cismi kendine') + _yazi(244, 140, 'doğru getirir.')
    ic += '<line x1="20" y1="168" x2="450" y2="168" class="g-c" stroke-width="1.2"/>'
    ic += _yazi(20, 192, 'Mıknatıs toplu iğneyi çeker', 13, kalin='800')
    ic += _yazi(250, 192, 'Dünya kalemi aşağı çeker', 13, kalin='800')
    # mıknatıs ve toplu iğne (dokunmadan çekme: kesikli ok)
    ic += _kutu(30, 212, 76, 36) + _yazi(68, 235, 'Mıknatıs', 13, hiza='middle', kalin='700')
    ic += '<rect x="168" y="227" width="30" height="6" rx="2" class="g-s"/><circle cx="202" cy="230" r="4.5" class="g-s"/>'
    ic += _ok(162, 230, 114, 230, 'g-ms', 'ok5fen7b', 2.2, kesik=True)
    ic += _yazi(186, 258, 'toplu iğne', 12, hiza='middle')
    # Dünya ve kalem
    ic += '<rect x="326" y="204" width="8" height="30" rx="2" class="g-s"/><path d="M326 234 L334 234 L330 242 Z" class="g-s"/>'
    ic += _yazi(342, 224, 'kalem', 12)
    ic += _ok(330, 248, 330, 266, 'g-ms', 'ok5fen7b', 2.2, kesik=True)
    yer = 'M280 298 V284 Q280 272 292 272 H368 Q380 272 380 284 V298 Z'
    ic += f'<path d="{yer}" class="g-z"/><path d="{yer}" class="g-c" stroke-width="1.8"/>'
    ic += _yazi(330, 290, 'Dünya', 13, hiza='middle', kalin='700')
    ic += _yazi(20, 316, 'Kesikli ok: cisme dokunmadan etki eden çekme kuvveti', 12.5, 'g-s')
    return svg(470, 326, ic, 'Kuvvet, bir cisme uygulanan itme ya da çekmedir. Üstte iki sıra: Sen kapıyı itersin, turuncu itme oku '
               'kapıya doğru gider ve kapı senden uzaklaşır; sen çekmeceyi çekersin, mavi çekme oku sana doğru gelir ve çekmece sana '
               'yaklaşır. Altta kesikli mavi oklar dokunmadan etki eden çekme kuvvetlerini gösterir: mıknatıs toplu iğneyi kendine '
               'çeker, Dünya kalemi aşağı doğru çeker.')


def nitelikler():
    """Kuvvetin üç niteliği: büyüklük (ok uzunluğu), yön (sağa/sola) ve uygulama noktası (kapıda kol ile menteşe)."""
    ic = '<defs>' + ok_isareti('ok5fen7c', 'g-tf') + ok_isareti('ok5fen7d', 'g-mf') + '</defs>'
    for x, bas, alt in ((80, 'Büyüklük', 'Ne kadar?'), (240, 'Yön', 'Hangi yöne?'), (400, 'Uygulama noktası', 'Neresine?')):
        ic += _yazi(x, 20, bas, 13, hiza='middle', kalin='800') + _yazi(x, 37, alt, 12, 'g-s', 'middle')
    for x in (160, 320):
        ic += f'<line x1="{x}" y1="48" x2="{x}" y2="236" class="g-c" stroke-width="1.2"/>'
    # büyüklük: kısa ok küçük kuvvet, uzun ok büyük kuvvet
    ic += _kutu(76, 72, 74, 36) + _yazi(113, 95, 'Boş kutu', 12.5, hiza='middle', kalin='700')
    ic += _ok(46, 90, 70, 90, 'g-ts', 'ok5fen7c') + _yazi(80, 126, 'küçük kuvvet', 12.5, hiza='middle')
    ic += _kutu(76, 152, 74, 36) + _yazi(113, 175, 'Dolu dolap', 12.5, hiza='middle', kalin='700')
    ic += _ok(12, 170, 70, 170, 'g-ts', 'ok5fen7c') + _yazi(80, 206, 'büyük kuvvet', 12.5, hiza='middle')
    # yön: ip sağa çekilince kutu sağa, sola çekilince sola gider
    ic += _kutu(210, 72, 60, 36) + _yazi(240, 95, 'Kutu', 12.5, hiza='middle', kalin='700')
    ic += _ok(276, 90, 314, 90, 'g-ms', 'ok5fen7d') + _yazi(240, 126, 'sağa çek → sağa gider', 12, hiza='middle')
    ic += _kutu(210, 152, 60, 36) + _yazi(240, 175, 'Kutu', 12.5, hiza='middle', kalin='700')
    ic += _ok(204, 170, 166, 170, 'g-ms', 'ok5fen7d') + _yazi(240, 206, 'sola çek → sola gider', 12, hiza='middle')
    # uygulama noktası: üstten görünen kapı; solda menteşe, sağda kol; aynı uzunlukta iki itme oku
    ic += '<rect x="352" y="132" width="116" height="10" rx="2" class="g-s"/>'
    ic += '<circle cx="356" cy="137" r="6" class="g-y"/><circle cx="458" cy="137" r="4" class="g-y"/>'
    ic += _yazi(356, 163, 'menteşe', 12, hiza='middle') + _yazi(458, 163, 'kol', 12, hiza='middle')
    ic += _ok(372, 80, 372, 124, 'g-ts', 'ok5fen7c') + _yazi(372, 70, 'zor', 12.5, hiza='middle', kalin='800')
    ic += _ok(452, 80, 452, 124, 'g-ts', 'ok5fen7c') + _yazi(452, 70, 'kolay', 12.5, hiza='middle', kalin='800')
    ic += _yazi(400, 190, 'Aynı büyüklükte itme:', 12, hiza='middle')
    ic += _yazi(400, 206, 'kola yakın → kolay,', 12, hiza='middle')
    ic += _yazi(400, 222, 'menteşeye yakın → zor.', 12, hiza='middle')
    ic += _yazi(12, 252, 'Ok boyu = kuvvetin büyüklüğü; ölçeksiz.', 12, 'g-s')
    return svg(480, 262, ic, 'Kuvvetin üç niteliği. Büyüklük: boş kutuyu kısa bir itme oku, dolu dolabı uzun bir itme oku iter; ok uzunluğu '
               'kuvvetin büyüklüğünü gösterir. Yön: ipi sağa çekersen kutu sağa, sola çekersen sola gider. Uygulama noktası: üstten '
               'görünen bir kapı, bir ucunda menteşe, diğer ucunda kol; aynı büyüklükte iki itme oku, kola yakın olan kapıyı kolay, '
               'menteşeye yakın olan zor açar. Ölçeksiz.')


def yay_uzamasi():
    """Yay uzaması kuvvetle düzenli artar: kuvvet iki katına çıkınca uzama da iki katına çıkar."""
    ic = '<defs>' + ok_isareti('ok5fen7e', 'g-mf') + '</defs>'
    ic += _yazi(452, 16, 'Ölçeksiz; uzunluklar orantılı.', 12, 'g-s', 'end')
    ic += '<rect x="60" y="24" width="350" height="10" rx="2" class="g-s"/>'
    ic += '<line x1="70" y1="134" x2="386" y2="134" class="g-c" stroke-width="1.4" stroke-dasharray="5 4"/>'
    ic += _yazi(392, 131, 'yayın ilk', 12, 'g-s') + _yazi(392, 147, 'uzunluğu', 12, 'g-s')
    # 1: kuvvet yok, uzama yok
    ic += _yay(100, 34, 100) + '<circle cx="100" cy="139" r="4.5" class="g-os" stroke-width="2"/>'
    ic += _yazi(100, 164, 'Kuvvet yok', 13, hiza='middle', kalin='800') + _yazi(100, 181, 'uzama yok', 12.5, 'g-s', 'middle')
    # 2: kuvvet → uzama
    ic += _yay(230, 34, 140) + '<circle cx="230" cy="179" r="4.5" class="g-os" stroke-width="2"/>'
    ic += _ok(230, 186, 230, 220, 'g-ms', 'ok5fen7e') + _yazi(240, 207, 'kuvvet', 12.5, 'g-mf', kalin='800')
    ic += _olcu(204, 134, 174) + _yazi(196, 158, 'uzama', 12.5, 'g-yf', 'end', '800')
    # 3: 2 kat kuvvet → 2 kat uzama (uzama 40 → 80, ok 34 → 68)
    ic += _yay(370, 34, 180) + '<circle cx="370" cy="219" r="4.5" class="g-os" stroke-width="2"/>'
    ic += _ok(370, 226, 370, 294, 'g-ms', 'ok5fen7e')
    ic += _yazi(380, 254, '2 kat', 12.5, 'g-mf', kalin='800') + _yazi(380, 270, 'kuvvet', 12.5, 'g-mf', kalin='800')
    ic += _olcu(344, 134, 214) + _yazi(336, 178, '2 kat uzama', 12.5, 'g-yf', 'end', '800')
    ic += _yazi(30, 318, 'Kuvvet 2 katına çıkınca uzama da 2 katına çıkar.', 13, kalin='800')
    ic += _yazi(30, 336, 'Esneklik sınırı aşılırsa yay eski hâline dönmez.', 12, 'g-s')
    return svg(460, 346, ic, 'Bir çubuğa asılı üç yay. Birinci yaya kuvvet uygulanmıyor, uzama yok. İkinci yayı aşağı doğru bir çekme '
               'kuvveti çeker ve yay bir miktar uzar; uzama yeşil ölçüyle gösterilir. Üçüncü yayı iki kat büyük bir kuvvet çeker ve '
               'uzama da iki kat olur. Kuvvet iki katına çıkınca uzama da iki katına çıkar. Esneklik sınırı aşılırsa yay eski hâline '
               'dönmez. Uzunluklar orantılı, ölçeksiz.')


def kuvvet_olcer_modeli():
    """Karton şerit, lastik ve ataştan kuvvet ölçer modeli: serbest uçta 0, cisim asılınca yeni işaret."""
    ic = '<defs>' + ok_isareti('ok5fen7f', 'g-mf') + '</defs>'
    ic += _yazi(95, 12, '1. Lastik serbest', 13, hiza='middle', kalin='800')
    ic += _yazi(295, 12, '2. Su şişesi asılı', 13, hiza='middle', kalin='800')
    for x0 in (50, 250):
        ic += _kutu(x0, 24, 90, 220, rx=6) + f'<circle cx="{x0 + 45}" cy="36" r="4" class="g-s"/>'
    # sol: lastik serbest, ucu 0 işaretinde
    ic += _lastik(95, 38, 88) + _kanca(95, 126) + _isaret(104, 126, '0')
    for y, ad in ((40, 'raptiye'), (86, 'lastik'), (138, 'ataş')):
        ic += _yazi(44, y, ad, 12, hiza='end')
    ic += '<line x1="47" y1="36" x2="88" y2="36" class="g-c" stroke-width="1"/>'
    ic += '<line x1="47" y1="82" x2="88" y2="82" class="g-c" stroke-width="1"/>'
    ic += '<line x1="47" y1="134" x2="92" y2="134" class="g-c" stroke-width="1"/>'
    # sağ: su şişesi asılı, lastik uzamış; daha önceki cisimlerin işaretleri de kartonda
    ic += _lastik(295, 38, 190) + _kanca(295, 228)
    for y, ad in ((126, '0'), (160, 'silgi'), (194, 'makas'), (228, 'su şişesi')):
        ic += _isaret(304, y, ad)
    ic += _kutu(288, 246, 28, 40, rx=5)
    ic += _ok(330, 250, 330, 288, 'g-ms', 'ok5fen7f')
    ic += _yazi(338, 266, 'çekme', 12.5, 'g-mf', kalin='800') + _yazi(338, 282, 'kuvveti', 12.5, 'g-mf', kalin='800')
    ic += _yazi(95, 306, 'Serbest uç: 0 işareti', 12.5, hiza='middle')
    ic += _yazi(295, 306, 'Cisim as, yeni ucu işaretle', 12.5, hiza='middle')
    ic += _yazi(230, 332, 'Kuvvet büyüdükçe işaret 0’dan daha uzağa düşer.', 13, hiza='middle', kalin='800')
    return svg(460, 344, ic, 'Kartondan kuvvet ölçer modeli, iki adım. Birinci adım: raptiyeyle karton şeride tutturulmuş lastik serbest '
               'sarkar, ucunda ataştan kanca var; lastiğin ucunun geldiği yere sıfır işareti konur. İkinci adım: kancaya su şişesi '
               'asılınca lastik uzar; silgi, makas ve su şişesi için ucun geldiği yerler kartona yeşil çentiklerle işaretlenir. '
               'Cisim ne kadar büyük çekme kuvveti uygularsa işaret sıfırdan o kadar uzağa düşer.')


def uygula(o):
    g = {'Kuvvet nedir? İtme ve çekme': itme_cekme(),
         'Kuvvetin nitelikleri': nitelikler(),
         'Yaylar ve esneklik: Kuvvet neden yayla ölçülür?': yay_uzamasi(),
         'Kendi kuvvet ölçerini yap': kuvvet_olcer_modeli()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
