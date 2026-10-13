"""6. sınıf Fen Bilimleri, 7. hafta: alınan yol, yer değiştirme ve sürat; sabit süratli ve sabit hızlı hareket;
üreme, büyüme ve gelişme; eşeysiz üremenin çeşitleri.

Görseller yalnız özet metnindeki (araclar/ozetler/6-fen-bilimleri-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı — hareket görselleri (1–2): mavi = düz ya da sabit olan (yer değiştirme oku; sabit süratli A koşucusu),
turuncu = dolambaçlı ya da değişen olan (alınan yol; sürati değişen B koşucusu); gri = eksenler, yardımcı çizgiler, ev–okul kutuları.
Renk anlamı — üreme görselleri (3–4): mavi = ata canlı, yeşil = yeni oluşan canlı (yavru), turuncu = atadan oluşan ya da ayrılan parça
(tomurcuk, yumru gözü, kopan kol) ve gelişmeyle kazanılan yeni yapı (çiçek), mor = aşama rozetleri (1 üreme, 2 büyüme, 3 gelişme).
Ölçek: 1. görsel ölçeksizdir (yalnız yolun biçimi); 2. görseldeki yol–zaman çizimi ölçülüdür: 10 s = 36 birim, 20 m = 36 birim,
iki çizim aynı ölçektedir; 3–4. görseller ölçeksiz şemalardır (canlılar gerçek boyut oranında çizilmemiştir).
Ok başı, çizginin ucundan 1,8 × çizgi kalınlığı kadar taşar (işaretçi refX=7, genişlik 6); çizgi o kadar kısa bitirilir.
"""
import math

from ozet_gorsel import svg, ok_isareti

F = 'ok6fen7'


def _yazi(x, y, metin, boy=12.5, sinif='g-y', anchor='middle', kalin=0):
    w = f' font-weight="{kalin}"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boy}"{w} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, cizgi, isaret, sw=2):
    """(x1, y1)'den çıkıp ucu (x2, y2)'de biten ok; ok başı taşacağı için çizgi 1,8 × sw kısa bitirilir."""
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    bas = 1.8 * sw
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2 - ux * bas:.1f}" y2="{y2 - uy * bas:.1f}" class="{cizgi}" '
            f'stroke-width="{sw}" marker-end="url(#{isaret})"/>')


def _kutu(cx, cy, ad, w=56, h=30):
    return (f'<rect x="{cx - w / 2:g}" y="{cy - h / 2:g}" width="{w}" height="{h}" rx="7" class="g-z"/>'
            f'<rect x="{cx - w / 2:g}" y="{cy - h / 2:g}" width="{w}" height="{h}" rx="7" class="g-c" stroke-width="2"/>'
            + _yazi(cx, cy + 4.5, ad, 13, kalin=800))


# ---------------------------------------------------------------- 1. alınan yol ve yer değiştirme
def yol_ve_yer_degistirme():
    """Sol: evden okula dolambaçlı sokaklardan gidilen yol (alınan yol, turuncu) ile kuzeye 400 m'lik dümdüz yer değiştirme (mavi ok).
    Sağ: koşu pistinde bir tur; alınan yol pistin uzunluğu, yer değiştirme sıfır."""
    f = F + 'a'
    ic = '<defs>' + ok_isareti(f + 'm', 'g-mf') + ok_isareti(f + 't', 'g-tf') + '</defs>'
    ic += _yazi(130, 20, 'Evden okula', 13, kalin=800) + _yazi(360, 20, 'Koşu pistinde bir tur', 13, kalin=800)
    # ev ve okul; okul evin kuzeyinde (yukarıda)
    ic += _kutu(120, 62, 'Okul') + _kutu(120, 206, 'Ev')
    # yer değiştirme: dümdüz, yönlü (kuzeye)
    ic += _ok(120, 188, 120, 80, 'g-ms', f + 'm', sw=3)
    ic += _yazi(108, 128, 'Yer değiştirme', 12.5, 'g-mf', 'end', 800) + _yazi(108, 145, 'kuzeye 400 m', 12, 'g-mf', 'end')
    # alınan yol: sokaklardan dönerek
    ic += ('<polyline points="148,206 252,206 252,152 176,152 176,108 252,108 252,62" class="g-ts" stroke-width="3" '
           'stroke-linejoin="round" stroke-linecap="round"/>')
    ic += _ok(252, 62, 149, 62, 'g-ts', f + 't', sw=3)
    ic += _yazi(200, 176, 'Alınan yol', 12.5, 'g-tf', kalin=800) + _yazi(200, 192, '400 m’den uzun', 12, 'g-tf')
    # koşu pisti: bir tur, başlangıç = bitiş
    cx, cy, rx, ry = 360, 118, 70, 46
    nokta = [(cx + rx * math.cos(math.radians(t)), cy + ry * math.sin(math.radians(t))) for t in range(90, 431, 5)]
    yol = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in nokta)
    ic += f'<path d="{yol}" class="g-ts" stroke-width="3" stroke-linejoin="round" marker-end="url(#{f}t)"/>'
    ic += f'<circle cx="{cx}" cy="{cy + ry}" r="5.5" class="g-mf"/>'
    ic += _yazi(cx, 114, 'Alınan yol =', 12.5, 'g-tf', kalin=800) + _yazi(cx, 131, 'pistin uzunluğu', 12.5, 'g-tf')
    ic += _yazi(cx, 188, 'Başlangıç = bitiş', 12) + _yazi(cx, 206, 'Yer değiştirme = 0', 12.5, 'g-mf', kalin=800)
    ic += _yazi(16, 238, 'Dolambaçlı yolda alınan yol &gt; yer değiştirme.', 12.5, 'g-s', 'start')
    ic += _yazi(16, 254, 'Düz yolda tek yönde gidilirse ikisi eşit olur.', 12.5, 'g-s', 'start')
    return svg(460, 266, ic, 'Alınan yol ile yer değiştirmenin farkı. Solda evden okula sokaklardan dönerek gidilen dolambaçlı yol turuncu çizgiyle '
               'çizilmiştir: bu, alınan yoldur ve 400 metreden uzundur. Evden okula dümdüz giden mavi ok yer değiştirmedir: kuzeye 400 metre. '
               'Sağda koşu pistinde bir tur: alınan yol pistin uzunluğu kadardır; başlangıç ve bitiş noktası aynı olduğundan yer değiştirme sıfırdır. '
               'Dolambaçlı yolda alınan yol yer değiştirmeden büyüktür; düz yolda tek yönde gidilirse ikisi eşit olur. Çizim ölçeksizdir.')


# ---------------------------------------------------------------- 2. yol–zaman çizimi
S = 36  # 10 saniye ve 20 metrenin çizimdeki uzunluğu (ölçek)


def _cizim(f, ox, oy, yollar, cizgi, dolgu):
    """Sol alt köşesi (ox, oy) olan yol–zaman çizimi; yollar: ardışık 10 s'lik aralıklarda alınan yollar (m)."""
    g = _ok(ox, oy, ox + 4 * S + 18, oy, 'g-c', f + 's', sw=1.8) + _ok(ox, oy, ox, oy - 4 * S - 18, 'g-c', f + 's', sw=1.8)
    for k in range(1, 5):
        x, y = ox + k * S, oy - k * S
        g += f'<line x1="{x}" y1="{oy}" x2="{x}" y2="{oy + 5}" class="g-c" stroke-width="1.5"/>' + _yazi(x, oy + 18, str(10 * k), 12, 'g-s')
        g += f'<line x1="{ox - 5}" y1="{y}" x2="{ox}" y2="{y}" class="g-c" stroke-width="1.5"/>' + _yazi(ox - 8, y + 4, str(20 * k), 12, 'g-s', 'end')
    g += _yazi(ox - 6, oy + 17, '0', 12, 'g-s', 'end')
    g += _yazi(ox + 8, oy - 150, 'Yol (m)', 12, 'g-s', 'start') + _yazi(ox + 4 * S + 18, oy + 34, 'Zaman (s)', 12, 'g-s', 'end')
    toplam, p = 0, [(ox, oy)]
    for yol in yollar:
        toplam += yol
        p.append((ox + len(p) * S, oy - toplam * S / 20))
    for k in range(4):
        (x1, y1), (x2, y2) = p[k], p[k + 1]
        g += (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y1:g}" class="g-c" stroke-width="1.2" stroke-dasharray="3 3"/>'
              f'<line x1="{x2:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="g-c" stroke-width="1.2" stroke-dasharray="3 3"/>')
        g += _yazi(x2 + 6, (y1 + y2) / 2 + 6, f'{yollar[k]} m', 12, dolgu, 'start', 800)
    g += f'<polyline points="{" ".join(f"{x:g},{y:g}" for x, y in p)}" class="{cizgi}" stroke-width="2.5" stroke-linejoin="round"/>'
    for x, y in p:
        g += f'<circle cx="{x:g}" cy="{y:g}" r="3.5" class="{dolgu}"/>'
    return g


def yol_zaman():
    """A koşucusu (her 10 s'de 20 m: düz doğru, sabit süratli) ve B koşucusu (30, 20, 10, 20 m: kırık çizgi) yol–zaman çizimleri, aynı ölçek."""
    f = F + 'b'
    oy = 180
    ic = '<defs>' + ok_isareti(f + 's', 'g-s') + '</defs>'
    ic += _cizim(f, 46, oy, [20, 20, 20, 20], 'g-ms', 'g-mf') + _cizim(f, 272, oy, [30, 20, 10, 20], 'g-ts', 'g-tf')
    ic += _yazi(127, 236, 'A koşucusu: her 10 s’de 20 m', 13, 'g-mf', kalin=800) + _yazi(127, 254, 'sabit süratli: düz doğru, 2 m/s', 12, 'g-s')
    ic += _yazi(353, 236, 'B koşucusu: 30, 20, 10, 20 m', 13, 'g-tf', kalin=800) + _yazi(353, 254, 'sabit süratli değil: kırık çizgi', 12, 'g-s')
    return svg(460, 266, ic, 'İki koşucunun yol–zaman çizimleri, aynı ölçekte. Yatay eksen zaman (saniye), düşey eksen alınan yol (metre). '
               'A koşucusu her 10 saniyede 20 metre alır: noktalar 0, 20, 40, 60 ve 80 metrede eşit basamaklarla yükselir ve düz bir doğru '
               'üzerindedir; sürati sabittir, 2 metre bölü saniye. B koşucusu aynı 10 saniyelik aralıklarda 30, 20, 10 ve 20 metre alır: '
               'noktalar kırık bir çizgi oluşturur, sürati değişir, hareketi sabit süratli değildir. İkisi de 40 saniyede 80 metre almıştır.')


# ---------------------------------------------------------------- 3. üreme, büyüme ve gelişme
def _bitki(x, taban, boy, yapraklar, dolgu, cizgi):
    """Gövdesi x'te, tabanı taban çizgisinde, boy uzunluğunda bitki; yapraklar: tabandan yükseklikler (çift yaprak)."""
    g = f'<line x1="{x}" y1="{taban}" x2="{x}" y2="{taban - boy}" class="{cizgi}" stroke-width="2.5" stroke-linecap="round"/>'
    for h in yapraklar:
        for yon in (-1, 1):
            cx, cy = x + yon * 9, taban - h
            g += f'<ellipse cx="{cx}" cy="{cy}" rx="10" ry="4.5" transform="rotate({-28 * yon} {cx} {cy})" class="{dolgu}"/>'
    return g


def _cicek(x, y, dolgu):
    g = ''
    for k in range(5):
        a = math.radians(90 + 72 * k)
        g += f'<circle cx="{x + 7 * math.cos(a):.1f}" cy="{y - 7 * math.sin(a):.1f}" r="5" class="{dolgu}"/>'
    return g + f'<circle cx="{x}" cy="{y}" r="4" class="g-b"/>'


def _rozet(x, y, no):
    return f'<circle cx="{x}" cy="{y}" r="10" class="g-of"/>' + _yazi(x, y + 4.5, str(no), 12, 'g-b', kalin=800)


def ureme_buyume_gelisme():
    """Sıra: 1 üreme (ata bitkiden tohum, yeni canlı) → 2 büyüme (fide boy atar) → 3 gelişme (fide çiçek açar)."""
    f = F + 'c'
    ic = '<defs>' + ok_isareti(f + 'o', 'g-of') + ok_isareti(f + 's', 'g-s') + '</defs>'
    # aşama rozetleri ve sıra okları
    ic += _rozet(50, 24, 1) + _yazi(64, 29, 'Üreme', 14, anchor='start', kalin=800) + _ok(124, 24, 166, 24, 'g-os', f + 'o')
    ic += _rozet(188, 24, 2) + _yazi(202, 29, 'Büyüme', 14, anchor='start', kalin=800) + _ok(274, 24, 318, 24, 'g-os', f + 'o')
    ic += _rozet(340, 24, 3) + _yazi(354, 29, 'Gelişme', 14, anchor='start', kalin=800)
    for x in (154, 306):
        ic += f'<line x1="{x}" y1="44" x2="{x}" y2="246" class="g-c" stroke-width="1.2" stroke-dasharray="4 4"/>'
    for a, b in ((14, 144), (164, 296), (316, 448)):
        ic += f'<line x1="{a}" y1="170" x2="{b}" y2="170" class="g-c" stroke-width="1.5"/>'
    # 1 üreme: ata bitki (mavi) → tohum (yeşil, yeni canlı)
    ic += _bitki(44, 170, 74, [22, 42], 'g-mf', 'g-ms') + _cicek(44, 90, 'g-mf')
    ic += _ok(70, 158, 100, 158, 'g-c', f + 's')
    ic += '<ellipse cx="118" cy="164" rx="9" ry="6" class="g-yf"/>'
    ic += _yazi(44, 186, 'ata bitki', 12, 'g-s') + _yazi(118, 186, 'tohum', 12, 'g-s')
    # 2 büyüme: küçük fide → uzun fide
    ic += _bitki(200, 170, 26, [14], 'g-yf', 'g-ys') + _ok(224, 150, 248, 150, 'g-c', f + 's') + _bitki(272, 170, 76, [18, 40, 60], 'g-yf', 'g-ys')
    ic += _yazi(200, 186, 'küçük fide', 12, 'g-s') + _yazi(272, 186, 'uzun fide', 12, 'g-s')
    # 3 gelişme: uzun fide → çiçekli bitki (çiçek: yeni yapı, turuncu)
    ic += _bitki(342, 170, 76, [18, 40, 60], 'g-yf', 'g-ys') + _ok(368, 150, 392, 150, 'g-c', f + 's')
    ic += _bitki(416, 170, 76, [18, 40, 58], 'g-yf', 'g-ys') + _cicek(416, 86, 'g-tf')
    ic += _yazi(342, 186, 'uzun fide', 12, 'g-s') + _yazi(416, 186, 'çiçekli bitki', 12, 'g-s')
    # açıklamalar
    for x, satirlar in ((78, ('Yeni canlı oluşur', 'ata canlıya benzer', 'türün devamı sağlanır')),
                        (230, ('Boy ve kütle artar', 'hücre sayısı artar,', 'hücreler irileşir')),
                        (382, ('Yeni yapı ve yetenek', 'fide çiçek açar,', 'iribaş bacak çıkarır'))):
        ic += _yazi(x, 208, satirlar[0], 12.5, kalin=800) + _yazi(x, 224, satirlar[1], 12, 'g-s') + _yazi(x, 240, satirlar[2], 12, 'g-s')
    return svg(460, 252, ic, 'Üreme, büyüme ve gelişmenin sırası üç sütunda, fasulye örneğiyle. Bir: üreme; mavi ata bitkiden kendine benzer '
               'yeni canlı, yeşil tohum oluşur; türün devamı sağlanır. İki: büyüme; küçük fide uzun fide olur, boyu ve kütlesi artar, '
               'hücre sayısı artar ve hücreler irileşir. Üç: gelişme; uzun fide çiçek açar, turuncu çiçek yeni kazanılan yapıdır; '
               'iribaşın bacak çıkarması da gelişmedir. Çizim ölçeksizdir.')


# ---------------------------------------------------------------- 4. eşeysiz üremenin çeşitleri
def _hucre(x, y, r, dolgu, cizgi, cekirdek):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="{dolgu}"/><circle cx="{x}" cy="{y}" r="{r}" class="{cizgi}" stroke-width="2"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * 0.3:g}" class="{cekirdek}"/>')


def _hidra(x, y, w, h, dolgu, cizgi):
    """Gövdesi (x, y) merkezli yuvarlak dikdörtgen, üstte üç kısa dokunaç."""
    g = (f'<rect x="{x - w / 2:g}" y="{y - h / 2:g}" width="{w}" height="{h}" rx="{w / 2:g}" class="{dolgu}"/>'
         f'<rect x="{x - w / 2:g}" y="{y - h / 2:g}" width="{w}" height="{h}" rx="{w / 2:g}" class="{cizgi}" stroke-width="2"/>')
    ust = y - h / 2
    for dx, dy in ((-0.5, -0.65), (0, -0.8), (0.5, -0.65)):
        g += (f'<line x1="{x:g}" y1="{ust:g}" x2="{x + dx * w:g}" y2="{ust + dy * w:g}" class="{cizgi}" stroke-width="1.8" '
              f'stroke-linecap="round"/>')
    return g


def _yildiz(cx, cy, R, r, dolgu, cizgi, eksik=None):
    """Beş kollu deniz yıldızı; eksik: kopmuş kolun sırası (0–4), yerinde güdük kalır."""
    pts = []
    for k in range(10):
        a = math.radians(-90 + 36 * k)
        uz = R if k % 2 == 0 else r
        if eksik is not None and k == 2 * eksik:
            uz = r + 3
        pts.append(f'{cx + uz * math.cos(a):.1f},{cy + uz * math.sin(a):.1f}')
    p = ' '.join(pts)
    return (f'<polygon points="{p}" class="{dolgu}"/>'
            f'<polygon points="{p}" class="{cizgi}" stroke-width="2" stroke-linejoin="round"/>')


def _kopan_kol(cx, cy, R, r, kol, uzaklik):
    """kol sırasındaki kolun üçgeni, kol doğrultusunda uzaklik kadar ötelenmiş (kopmuş kol, turuncu)."""
    a0 = math.radians(-90 + 72 * kol)
    dx, dy = uzaklik * math.cos(a0), uzaklik * math.sin(a0)
    pts = []
    for k, uz in ((2 * kol - 1, r), (2 * kol, R), (2 * kol + 1, r)):
        a = math.radians(-90 + 36 * k)
        pts.append(f'{cx + dx + uz * math.cos(a):.1f},{cy + dy + uz * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" class="g-tf" stroke-linejoin="round"/>'


def esiysiz_cesitleri():
    """Dört küçük şema: bölünme (hücre ikiye bölünür), tomurcuklanma (hidra), vejetatif üreme (patates yumrusu), rejenerasyon (deniz yıldızı)."""
    f = F + 'd'
    ic = '<defs>' + ok_isareti(f + 's', 'g-s') + '</defs>'
    W, H = 216, 160

    def kart(x0, y0, baslik, ornek):
        return (f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" rx="10" class="g-z"/>'
                f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" rx="10" class="g-c" stroke-width="1.5"/>'
                + _yazi(x0 + 10, y0 + 19, baslik, 13, anchor='start', kalin=800) + _yazi(x0 + 10, y0 + 36, ornek, 12, 'g-s', 'start'))

    # bölünme
    x0, y0, cy = 8, 8, 92
    ic += kart(x0, y0, 'Bölünme ile üreme', 'bakteri, amip, paramesyum')
    ic += _hucre(x0 + 42, cy, 19, 'g-ma', 'g-ms', 'g-mf') + _ok(x0 + 68, cy, x0 + 104, cy, 'g-c', f + 's')
    ic += _yazi(x0 + 86, cy - 26, 'ikiye bölünür', 12, 'g-s')
    ic += _hucre(x0 + 130, cy, 14, 'g-ya', 'g-ys', 'g-yf') + _hucre(x0 + 166, cy, 14, 'g-ya', 'g-ys', 'g-yf')
    ic += _yazi(x0 + 42, y0 + 134, 'ata hücre', 12) + _yazi(x0 + 148, y0 + 134, 'iki yeni canlı', 12, 'g-yf', kalin=800)
    ic += _yazi(x0 + 108, y0 + 150, 'birbirinin tıpatıp aynısı', 12, 'g-s')
    # tomurcuklanma
    x0 = 236
    ic += kart(x0, y0, 'Tomurcuklanma ile üreme', 'hidra, bira mayası, mercan')
    ic += _hidra(x0 + 36, cy, 16, 44, 'g-ma', 'g-ms') + f'<circle cx="{x0 + 46}" cy="{cy + 2}" r="5" class="g-tf"/>'
    ic += _ok(x0 + 58, cy, x0 + 86, cy, 'g-c', f + 's')
    ic += _hidra(x0 + 100, cy, 16, 44, 'g-ma', 'g-ms') + f'<circle cx="{x0 + 114}" cy="{cy + 2}" r="9" class="g-tf"/>'
    ic += _ok(x0 + 130, cy, x0 + 150, cy, 'g-c', f + 's')
    ic += _hidra(x0 + 158, cy, 16, 44, 'g-ma', 'g-ms') + _hidra(x0 + 184, cy + 8, 10, 28, 'g-ya', 'g-ys')
    ic += _yazi(x0 + 36, y0 + 134, 'ata canlı', 12) + _yazi(x0 + 108, y0 + 134, 'tomurcuk', 12, 'g-tf', kalin=800)
    ic += _yazi(x0 + 176, y0 + 134, 'yeni canlı', 12, 'g-yf', kalin=800)
    ic += _yazi(x0 + 108, y0 + 150, 'tomurcuk büyür, ayrılır', 12, 'g-s')
    # vejetatif üreme
    x0, y0 = 8, 180
    cy = y0 + 84
    ic += kart(x0, y0, 'Vejetatif üreme', 'patates, çilek, soğan, gül')
    tx, ty = x0 + 50, cy + 8
    ic += (f'<ellipse cx="{tx}" cy="{ty}" rx="34" ry="20" class="g-ma"/>'
           f'<ellipse cx="{tx}" cy="{ty}" rx="34" ry="20" class="g-ms" stroke-width="2"/>')
    for gx, filiz in ((x0 + 36, True), (x0 + 62, True), (x0 + 76, False)):
        gy = ty - 20 * math.sqrt(1 - ((gx - tx) / 34) ** 2)
        if filiz:
            ic += f'<line x1="{gx}" y1="{gy:.1f}" x2="{gx}" y2="{gy - 22:.1f}" class="g-ys" stroke-width="2" stroke-linecap="round"/>'
            for yon in (-1, 1):
                lx, ly = gx + yon * 5, gy - 16
                ic += f'<ellipse cx="{lx}" cy="{ly:.1f}" rx="6" ry="3" transform="rotate({-30 * yon} {lx} {ly:.1f})" class="g-yf"/>'
        ic += f'<circle cx="{gx}" cy="{gy:.1f}" r="3.5" class="g-tf"/>'
    ic += _yazi(x0 + 96, cy - 14, 'göz', 11.5, 'g-tf', 'start', 800)
    ic += f'<line x1="{x0 + 80}" y1="{cy - 8}" x2="{x0 + 92}" y2="{cy - 15}" class="g-ts" stroke-width="1.2"/>'
    ic += _ok(x0 + 92, cy + 8, x0 + 120, cy + 8, 'g-c', f + 's')
    ic += _bitki(x0 + 150, cy + 28, 56, [16, 34], 'g-yf', 'g-ys')
    ic += _yazi(x0 + 50, y0 + 134, 'yumru gövde', 12) + _yazi(x0 + 150, y0 + 134, 'yeni bitki', 12, 'g-yf', kalin=800)
    ic += _yazi(x0 + 108, y0 + 150, 'gözlerinden yeni bitki çıkar', 12, 'g-s')
    # rejenerasyon
    x0 = 236
    ic += kart(x0, y0, 'Rejenerasyon ile üreme', 'deniz yıldızı, planarya')
    ic += _yildiz(x0 + 44, cy + 2, 24, 10, 'g-ma', 'g-ms', eksik=1) + _kopan_kol(x0 + 44, cy + 2, 24, 10, 1, 15)
    ic += _ok(x0 + 92, cy, x0 + 118, cy, 'g-c', f + 's')
    ic += _yildiz(x0 + 144, cy + 2, 24, 10, 'g-ma', 'g-ms') + _yildiz(x0 + 188, cy + 14, 15, 6.5, 'g-ya', 'g-ys')
    ic += _yazi(x0 + 44, y0 + 134, 'kopan kol', 12, 'g-tf', kalin=800) + _yazi(x0 + 166, y0 + 134, 'yeni canlı', 12, 'g-yf', kalin=800)
    ic += _yazi(x0 + 108, y0 + 150, 'ikisi de eksiğini tamamlar', 12, 'g-s')
    return svg(460, 348, ic, 'Eşeysiz üremenin dört çeşidi, dört küçük şemayla; mavi ata canlı, turuncu atadan ayrılan parça, yeşil yeni canlı. '
               'Bölünme: bakteri gibi tek hücreli ata hücre ikiye bölünür, birbirinin tıpatıp aynısı iki yeni canlı oluşur. '
               'Tomurcuklanma: hidranın vücudunda tomurcuk oluşur, büyür ve ayrılarak yeni canlı olur. Vejetatif üreme: patatesin yumru '
               'gövdesindeki gözlerden yeni bitki çıkar. Rejenerasyon: deniz yıldızının kopan kolu eksik kısımlarını tamamlayıp yeni deniz '
               'yıldızı olur, gövde de kolunu yeniler. Çizim ölçeksizdir.')


def uygula(o):
    g = {'Alınan yol, yer değiştirme ve sürat': yol_ve_yer_degistirme(),
         'Sabit süratli ve sabit hızlı hareket': yol_zaman(),
         'Üreme, büyüme ve gelişme': ureme_buyume_gelisme(),
         'Eşeysiz üremenin çeşitleri': esiysiz_cesitleri()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
