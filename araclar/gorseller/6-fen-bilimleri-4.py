"""6. sınıf Fen Bilimleri, 4. hafta: kuvvetin özellikleri ve bileşke kuvvet.

Görseller yalnız haftanın metnindeki bilgilerle çizilir: kuvvetin dört özelliği, aynı yönlü ve zıt yönlü kuvvetlerin
bileşkesi, üç kuvvetin bileşkesi, kareli zeminde bileşke kuvveti çizme.
Ölçek (K057): bu modüldeki bütün kuvvet okları tek ölçekle çizilir; 1 N = 28 birim (kareli zeminde bir kare kenarı).
Okun görünen uzunluğu (kuyruktan uca) büyüklükle orantılıdır. Ok başı, çizginin ucundan 1,8 × çizgi kalınlığı kadar taşar
(işaretçi: refX=7, genişlik 6 → 3 birim × 0,6 × kalınlık); bu yüzden çizgi, uca varmadan o kadar kısa bitirilir.
Renk anlamı: mavi = cisme uygulanan kuvvetler, turuncu = bileşke kuvvet, mor = özellik rozetleri; cisim açık zeminli kutudur.
Ok başlarında dolgu sınıfı kullanılır (g-mf, g-tf).
"""
from ozet_gorsel import svg, ok_isareti

BIRIM = 28          # 1 N kaç birim
SW = 3              # ok çizgisinin kalınlığı
BAS = 1.8 * SW      # ok başının çizgi ucundan taşan kısmı
RENK = {'mavi': ('g-ms', 'g-mf'), 'turuncu': ('g-ts', 'g-tf')}


def _tanim(f):
    return '<defs>' + ok_isareti(f + 'm', 'g-mf') + ok_isareti(f + 't', 'g-tf') + '</defs>'


def _ok(f, x, y, n, yon, renk='mavi'):
    """Kuyruğu (x, y) uygulama noktasında olan, n N büyüklüğünde ok. yon: +1 doğu (sağ), -1 batı (sol).
    Okun görünen uzunluğu (kuyruk-uç) tam n × BIRIM'dir; kuyrukta uygulama noktası daireyle işaretlenir."""
    cizgi, dolgu = RENK[renk]
    uc = x + yon * n * BIRIM
    bitis = uc - yon * BAS
    isaret = f + ('m' if renk == 'mavi' else 't')
    return (f'<line x1="{x:g}" y1="{y:g}" x2="{bitis:g}" y2="{y:g}" class="{cizgi}" stroke-width="{SW}" marker-end="url(#{isaret})"/>'
            f'<circle cx="{x:g}" cy="{y:g}" r="4.5" class="{dolgu}"/>')


def _cisim(x, cy, ad, w=56, h=48):
    return (f'<rect x="{x}" y="{cy - h / 2:g}" width="{w}" height="{h}" rx="6" class="g-z"/>'
            f'<rect x="{x}" y="{cy - h / 2:g}" width="{w}" height="{h}" rx="6" class="g-c" stroke-width="2"/>'
            f'<text x="{x + w / 2:g}" y="{cy + 6:g}" text-anchor="middle" font-size="16" font-weight="800" class="g-y">{ad}</text>')


def _etiket(x, y, metin, renk='g-mf', anchor='start', boy=13, agirlik=800):
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boy}" font-weight="{agirlik}" class="{renk}">{metin}</text>'


def _baslik(x, y, metin):
    return f'<text x="{x}" y="{y}" font-size="12.5" font-weight="800" class="g-y">{metin}</text>'


def _rozet(x, y, no):
    return (f'<circle cx="{x}" cy="{y}" r="9" class="g-of"/>'
            f'<text x="{x}" y="{y + 4.5:g}" text-anchor="middle" font-size="12" font-weight="800" class="g-b">{no}</text>')


def _bag(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-os" stroke-width="1.5" stroke-linecap="round"/>'


def kuvvet_ozellikleri():
    """K cismine uygulanan F1 (3 N, doğu) ve F2 (2 N, batı): uygulama noktası, yön, doğrultu, büyüklük."""
    f, cy = 'k4a', 64
    ic = _tanim(f)
    ic += f'<line x1="16" y1="{cy}" x2="444" y2="{cy}" class="g-c" stroke-width="1.6" stroke-dasharray="5 5"/>'
    ic += _cisim(190, cy, 'K')
    ic += _ok(f, 246, cy, 3, +1) + _ok(f, 190, cy, 2, -1)
    ic += _etiket(300, cy - 16, 'F1 = 3 N') + _etiket(150, cy - 16, 'F2 = 2 N', anchor='middle')
    ic += _etiket(16, cy + 20, 'Batı', 'g-s', boy=12.5, agirlik=400) + _etiket(444, cy + 20, 'Doğu', 'g-s', 'end', 12.5, 400)
    ic += _rozet(284, cy - 20, 4)                                  # büyüklük (etiketin solunda)
    ic += _rozet(272, cy + 34, 1) + _bag(266, cy + 27, 251, cy + 8)   # uygulama noktası (F1'in kuyruğu)
    ic += _rozet(358, cy + 34, 2) + _bag(354, cy + 27, 337, cy + 8)   # yön (F1'in ucu)
    ic += _rozet(70, cy - 34, 3) + _bag(70, cy - 25, 70, cy - 6)      # doğrultu (kesikli doğru)
    ls = ['Uygulama noktası: okların çıktığı noktalar', 'Yön: F1 doğu, F2 batı', 'Doğrultu: doğu-batı', 'Büyüklük: F1 3 N, F2 2 N']
    for k, yazi in enumerate(ls):
        ic += _rozet(28, cy + 74 + k * 24, k + 1) + _etiket(44, cy + 78 + k * 24, yazi, 'g-y', boy=12.5, agirlik=400)
    yb = cy + 144
    ic += (f'<line x1="260" y1="{yb}" x2="{260 + BIRIM}" y2="{yb}" class="g-c" stroke-width="2"/>'
           f'<line x1="260" y1="{yb - 6}" x2="260" y2="{yb + 6}" class="g-c" stroke-width="2"/>'
           f'<line x1="{260 + BIRIM}" y1="{yb - 6}" x2="{260 + BIRIM}" y2="{yb + 6}" class="g-c" stroke-width="2"/>')
    ic += _etiket(300, yb + 4, '= 1 N', 'g-s', boy=12.5, agirlik=400)
    ic += _etiket(260, yb + 24, 'Bütün oklar aynı ölçektedir.', 'g-s', boy=12, agirlik=400)
    return svg(460, cy + 182, ic, 'K cismine uygulanan iki kuvvet: F1 doğu yönünde 3 N, F2 batı yönünde 2 N; ikisi de doğu-batı doğrultusundadır. '
               'Her okun çıktığı nokta uygulama noktasıdır; okun ucu yönü, okun bulunduğu çizgi doğrultuyu, okun uzunluğu büyüklüğü gösterir. '
               'F1 oku F2 okundan uzundur; küçük çubuk 1 N uzunluğudur ve bütün oklar aynı ölçekle çizilmiştir.')


def ayni_yonlu():
    """K cismine doğu yönünde F1 = 2 N ve F2 = 5 N; bileşke kuvvet R = 7 N (doğu)."""
    f = 'k4b'
    ic = _tanim(f)
    ic += _baslik(16, 18, 'Uygulanan kuvvetler') + _etiket(444, 18, 'Sağ taraf: doğu', 'g-s', 'end', 12, 400)
    ic += _cisim(40, 74, 'K')
    ic += _ok(f, 96, 62, 2, +1) + _ok(f, 96, 86, 5, +1)
    ic += _etiket(164, 66, 'F1 = 2 N') + _etiket(248, 90, 'F2 = 5 N')
    ic += _baslik(16, 128, 'Bileşke kuvvet')
    ic += _cisim(40, 170, 'K')
    ic += _ok(f, 96, 170, 7, +1, 'turuncu')
    ic += _etiket(304, 175, 'R = 7 N', 'g-tf')
    ic += _etiket(16, 224, 'R = F1 + F2 = 2 N + 5 N = 7 N', 'g-y', boy=14)
    ic += _etiket(16, 246, 'Yönü: doğu · Doğrultusu: doğu-batı', 'g-s', boy=12.5, agirlik=400)
    return svg(460, 256, ic, 'K cismine doğu yönünde iki kuvvet uygulanıyor: F1 2 N ve F2 5 N. Bileşke kuvvet doğu yönünde ve 7 N büyüklüğündedir; '
               'R okunun uzunluğu F1 ve F2 oklarının uzunlukları toplamına eşittir. Üç ok aynı ölçekle çizilmiştir.')


def zit_yonlu():
    """L cismine doğu yönünde F1 = 5 N, batı yönünde F2 = 2 N; bileşke kuvvet R = 3 N (doğu)."""
    f = 'k4c'
    ic = _tanim(f)
    ic += _baslik(16, 18, 'Uygulanan kuvvetler') + _etiket(444, 18, 'Sol taraf: batı · Sağ taraf: doğu', 'g-s', 'end', 12, 400)
    ic += _cisim(100, 74, 'L')
    ic += _ok(f, 156, 74, 5, +1) + _ok(f, 100, 74, 2, -1)
    ic += _etiket(226, 56, 'F1 = 5 N', anchor='middle') + _etiket(62, 56, 'F2 = 2 N', anchor='middle')
    ic += _baslik(16, 128, 'Bileşke kuvvet')
    ic += _cisim(100, 170, 'L')
    ic += _ok(f, 156, 170, 3, +1, 'turuncu')
    ic += _etiket(252, 175, 'R = 3 N', 'g-tf')
    ic += _etiket(16, 224, 'R = F1 − F2 = 5 N − 2 N = 3 N', 'g-y', boy=14)
    ic += _etiket(16, 246, 'Yönü: doğu (büyük kuvvetin yönü) · Doğrultusu: doğu-batı', 'g-s', boy=12.5, agirlik=400)
    return svg(460, 256, ic, 'L cismine zıt yönde iki kuvvet uygulanıyor: F1 doğu yönünde 5 N, F2 batı yönünde 2 N. Bileşke kuvvet büyük kuvvetin '
               'yönünde, yani doğu yönünde ve 3 N büyüklüğündedir; R okunun uzunluğu F1 okunun uzunluğundan F2 okunun uzunluğu çıkarılarak bulunur. '
               'Üç ok aynı ölçekle çizilmiştir.')


def uc_kuvvet():
    """Masaya batı yönünde F1 = 2 N ve F2 = 3 N, doğu yönünde F3 = 2 N; önce aynı yöndekiler toplanır, sonra fark alınır: R = 3 N (batı)."""
    f = 'k4d'
    ic = _tanim(f)
    ic += _baslik(16, 18, 'Uygulanan kuvvetler') + _etiket(444, 18, 'Sol taraf: batı · Sağ taraf: doğu', 'g-s', 'end', 12, 400)
    ic += _cisim(190, 80, 'M')
    ic += _ok(f, 190, 68, 2, -1) + _ok(f, 190, 92, 3, -1) + _ok(f, 246, 80, 2, +1)
    ic += _etiket(122, 72, 'F1 = 2 N', anchor='end') + _etiket(94, 96, 'F2 = 3 N', anchor='end') + _etiket(314, 85, 'F3 = 2 N')
    ic += _baslik(16, 136, '1. adım: aynı yöndekiler toplanır')
    ic += _cisim(190, 192, 'M')
    ic += _ok(f, 190, 192, 5, -1) + _ok(f, 246, 192, 2, +1)
    ic += _etiket(120, 172, 'F1 + F2 = 5 N', anchor='middle') + _etiket(314, 197, 'F3 = 2 N')
    ic += _baslik(16, 244, '2. adım: zıt yönlü iki kuvvet gibi fark alınır')
    ic += _cisim(190, 300, 'M')
    ic += _ok(f, 190, 300, 3, -1, 'turuncu')
    ic += _etiket(94, 305, 'R = 3 N', 'g-tf', anchor='end')
    ic += _etiket(16, 352, 'R = 5 N − 2 N = 3 N', 'g-y', boy=14)
    ic += _etiket(16, 374, 'Yönü: batı (büyük taraf) · Doğrultusu: doğu-batı', 'g-s', boy=12.5, agirlik=400)
    return svg(460, 386, ic, 'M masasına batı yönünde F1 2 N ve F2 3 N, doğu yönünde F3 2 N uygulanıyor. Birinci adımda batı yönündeki kuvvetler toplanır: '
               '2 N artı 3 N eşittir 5 N. İkinci adımda 5 N batı ile 2 N doğu zıt yönlü iki kuvvet gibi çıkarılır: bileşke kuvvet batı yönünde 3 N olur. '
               'Bütün oklar aynı ölçekle çizilmiştir.')


def kareli_cizim():
    """Kareli zeminde her kare kenarı 1 N: F1 = 2 N (batı), F2 = 4 N (doğu); R = 2 N (doğu) iki kare uzunluğunda çizilir."""
    f = 'k4e'
    x0 = 16
    ic = _tanim(f)

    def izgara(y0):
        g = ''
        for k in range(11):
            g += f'<line x1="{x0 + k * BIRIM}" y1="{y0}" x2="{x0 + k * BIRIM}" y2="{y0 + 4 * BIRIM}" class="g-c" stroke-width="1" opacity=".6"/>'
        for j in range(5):
            g += f'<line x1="{x0}" y1="{y0 + j * BIRIM}" x2="{x0 + 10 * BIRIM}" y2="{y0 + j * BIRIM}" class="g-c" stroke-width="1" opacity=".6"/>'
        return g
    ic += _baslik(16, 18, 'Uygulanan kuvvetler')
    ic += izgara(28)
    ic += _cisim(x0 + 4 * BIRIM, 84, 'K', h=2 * BIRIM)
    ic += _ok(f, x0 + 4 * BIRIM, 84, 2, -1) + _ok(f, x0 + 6 * BIRIM, 84, 4, +1)
    ic += _etiket(312, 52, 'F1 = 2 N') + _etiket(312, 68, 'batı yönünde, 2 kare', 'g-s', boy=12, agirlik=400)
    ic += _etiket(312, 100, 'F2 = 4 N') + _etiket(312, 116, 'doğu yönünde, 4 kare', 'g-s', boy=12, agirlik=400)
    ic += _baslik(16, 166, 'Bileşke kuvvet')
    ic += izgara(176)
    ic += _cisim(x0 + 4 * BIRIM, 232, 'K', h=2 * BIRIM)
    ic += _ok(f, x0 + 6 * BIRIM, 232, 2, +1, 'turuncu')
    ic += _etiket(312, 204, 'R = F2 − F1', 'g-tf') + _etiket(312, 222, 'R = 4 N − 2 N = 2 N', 'g-y', boy=13, agirlik=400)
    ic += _etiket(312, 240, 'doğu yönünde, 2 kare', 'g-s', boy=12, agirlik=400)
    ic += _etiket(16, 312, 'Her kare kenarı 1 N\'lık kuvveti gösterir.', 'g-s', boy=12.5, agirlik=400)
    return svg(460, 324, ic, 'Her kare kenarı 1 N olan kareli zeminde K cismine batı yönünde F1 = 2 N (iki kare) ve doğu yönünde F2 = 4 N (dört kare) uygulanıyor. '
               'Bileşke kuvvet R = 4 N − 2 N = 2 N olur ve doğu yönündedir; iki kare uzunluğunda, doğuyu gösteren bir okla çizilir.')


def uygula(o):
    g = {'Kuvvetin özellikleri': kuvvet_ozellikleri(),
         'Aynı yönlü kuvvetlerin bileşkesi': ayni_yonlu(),
         'Zıt yönlü kuvvetlerin bileşkesi': zit_yonlu(),
         'İkiden fazla kuvvetin bileşkesi': uc_kuvvet(),
         'Bileşke kuvveti çizerek gösterme': kareli_cizim()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
