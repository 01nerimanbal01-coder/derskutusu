"""7. sınıf Fen Bilimleri, 7. hafta: kuvvet, iş ve enerji ilişkisi; kinetik ve potansiyel enerji.

Kaynak: Görseller yalnız özet metnindeki (araclar/ozetler/7-fen-bilimleri-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı (bütün görsellerde aynı):
- yeşil = cisme uygulanan kuvvet ve yapılan iş (kuvvet okları, "iş yapılır", çukur açan iş),
- mavi = hareket ve kinetik enerji (yer değiştirme ve sürat okları, düşme yönü, kinetik enerji çubukları),
- turuncu = yükseklik ve çekim potansiyel enerjisi (yükseklik okları, potansiyel enerji çubukları),
- mor = esnek cisim (yay) ve esneklik potansiyel enerjisi (gerilme miktarı, depolanan enerji çubukları),
- gri = cisimler (kutu, dolap, bilye, ok, salıncak oturağı), zemin, kum ve yardımcı çizgiler.
Ölçek: kinetik enerji çubukları ölçeklidir (1 : 2 : 4; 1 birim = 44 uzunluk) ve sürat okları 2 kat uzundur; top ve bilye boyutları,
kum çukurlarının derinliği, yay gerilmeleri ve salıncaktaki enerji çubukları ölçeksizdir (yalnız az/çok karşılaştırması).
"""
import math

from ozet_gorsel import svg, ok_isareti


def _ok(x1, y1, x2, y2, sinif, kimlik, w=2.2, kesik=None):
    """Ok başı hedefe değecek biçimde kısaltılmış çizgi (ok başı ucu çizgi ucundan 1,8·w ileridedir)."""
    dx, dy = x2 - x1, y2 - y1
    u = math.hypot(dx, dy)
    ex, ey = x2 - dx / u * 1.8 * w, y2 - dy / u * 1.8 * w
    k = f' stroke-dasharray="{kesik}"' if kesik else ''
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{ex:.1f}" y2="{ey:.1f}" class="{sinif}" stroke-width="{w}" '
            f'stroke-linecap="round"{k} marker-end="url(#{kimlik})"/>')


def _cift_ok(x1, y1, x2, y2, sinif, kimlik, w=2.2):
    """İki ucu da ok başlı çizgi; uçlar hedeflere değecek biçimde kısaltılmıştır."""
    dx, dy = x2 - x1, y2 - y1
    u = math.hypot(dx, dy)
    k = 1.8 * w
    a = (x1 + dx / u * k, y1 + dy / u * k)
    b = (x2 - dx / u * k, y2 - dy / u * k)
    return (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="{sinif}" stroke-width="{w}" '
            f'stroke-linecap="round" marker-start="url(#{kimlik})" marker-end="url(#{kimlik})"/>')


def _yay_ok(cx, cy, r, a0, a1, sinif, kimlik, w=2.4):
    """(cx, cy) merkezli, r yarıçaplı yay üzerinde a0°'den a1°'ye ok (açılar +x ekseninden, ekranda saat yönü artı)."""
    kis = math.degrees(1.8 * w / r)
    a1k = a1 - kis if a1 > a0 else a1 + kis
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1k)), cy + r * math.sin(math.radians(a1k)))
    sweep = 1 if a1 > a0 else 0
    buyuk = 1 if abs(a1k - a0) > 180 else 0
    return (f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 {buyuk} {sweep} {p1[0]:.1f} {p1[1]:.1f}" class="{sinif}" '
            f'stroke-width="{w}" stroke-linecap="round" marker-end="url(#{kimlik})"/>')


def _yazi(x, y, metin, boyut, sinif, anchor='middle', kalin=False):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}"{a} font-size="{boyut:g}"{k} class="{sinif}">{metin}</text>'


def _kutu(x, y, w, h, rx=5, kesik=None):
    """Gri çerçeveli, zemin dolgulu cisim kutusu (kesik verilirse yalnız kesik çerçeve: önceki/sonraki konum)."""
    if kesik:
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.8" stroke-dasharray="{kesik}"/>'
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="2"/>')


def _top(cx, cy, r):
    return f'<circle cx="{cx:g}" cy="{cy:g}" r="{r}" class="g-z"/><circle cx="{cx:g}" cy="{cy:g}" r="{r}" class="g-c" stroke-width="2"/>'


# ---------- 1) İş yapılan ve yapılmayan durum ----------
def is_enerji():
    """Sol: kuvvet uygulanan kutu kuvvet yönünde yol alır (iş yapılır). Sağ: itilen dolap kıpırdamaz (iş yapılmaz).
    Altta: iş yapılınca cisme enerji geçer; ikisinin de birimi joule."""
    ic = '<defs>' + ok_isareti('f77a', 'g-yf') + ok_isareti('f77b', 'g-mf') + '</defs>'
    ic += '<line x1="230" y1="8" x2="230" y2="204" class="g-c" stroke-width="1.5" stroke-dasharray="5 5"/>'
    # sol pano: iş yapılır
    ic += _yazi(116, 22, 'İş yapılır', 15, 'g-yf', kalin=True)
    ic += '<line x1="14" y1="150" x2="218" y2="150" class="g-c" stroke-width="2.4" stroke-linecap="round"/>'
    ic += _kutu(52, 110, 44, 38) + _yazi(74, 134, 'kutu', 12, 'g-y')
    ic += _kutu(150, 110, 44, 38, kesik='4 4')
    ic += _ok(14, 129, 52, 129, 'g-ys', 'f77a', 3)
    ic += _yazi(33, 117, 'kuvvet', 12, 'g-yf', kalin=True)
    ic += _ok(74, 168, 172, 168, 'g-ms', 'f77b', 2.6)
    ic += _yazi(123, 188, 'yer değiştirme (yol)', 12, 'g-mf', kalin=True)
    ic += _yazi(116, 210, 'kuvvet yönünde yol aldı', 12, 'g-y')
    # sağ pano: iş yapılmaz
    ic += _yazi(344, 22, 'İş yapılmaz', 15, 'g-s', kalin=True)
    ic += '<line x1="242" y1="150" x2="446" y2="150" class="g-c" stroke-width="2.4" stroke-linecap="round"/>'
    ic += _kutu(318, 60, 54, 88) + _yazi(345, 108, 'dolap', 12, 'g-s')
    ic += _ok(266, 118, 318, 118, 'g-ys', 'f77a', 3)
    ic += _yazi(292, 106, 'kuvvet', 12, 'g-yf', kalin=True)
    ic += _yazi(344, 180, 'yer değiştirme yok', 12, 'g-s', kalin=True)
    ic += _yazi(344, 210, 'dolap kıpırdamadı', 12, 'g-y')
    # alt not: iş ve enerji
    ic += '<rect x="12" y="226" width="436" height="42" rx="10" class="g-ya"/><rect x="12" y="226" width="436" height="42" rx="10" class="g-ys" stroke-width="1.5"/>'
    ic += _yazi(230, 243, 'İş yapılınca cisme enerji geçer.', 12.5, 'g-y', kalin=True)
    ic += _yazi(230, 259, 'İkisinin de birimi joule (J): 1 N · 1 m = 1 J', 12, 'g-y')
    return svg(460, 272, ic, 'İki durum karşılaştırılır. Solda kutuya kuvvet uygulanır ve kutu kuvvet yönünde yol alır: iş yapılır. '
               'Sağda dolaba kuvvet uygulanır ama dolap kıpırdamaz, yer değiştirme yoktur: iş yapılmaz. İş yapılınca cisme enerji geçer; '
               'işin de enerjinin de birimi joule, yani bir newton çarpı bir metre eşittir bir joule.')


# ---------- 2) Kinetik enerji: kütle ve sürat ----------
def kinetik():
    """Üç satır: temel durum, kütle 2 katı, sürat 2 katı; kinetik enerji çubukları ölçekli 1 : 2 : 4."""
    ic = '<defs>' + ok_isareti('f77c', 'g-mf') + '</defs>'
    U = 44
    ic += _yazi(16, 18, 'Kinetik enerji kütleye ve sürate bağlıdır', 14, 'g-y', 'start', True)
    ic += _yazi(16, 42, 'kütle ve sürat', 12, 'g-s', 'start')
    ic += _yazi(208, 42, 'kinetik enerji (çubuklar ölçekli)', 12, 'g-mf', 'start', True)
    satirlar = [(9, 26, ('kütle 1 birim', 'g-y', False), ('sürat 1 birim', 'g-y', False), 1, '1 birim'),
                (13, 26, ('kütle 2 katı', 'g-y', True), ('sürat aynı', 'g-s', False), 2, '2 birim'),
                (9, 52, ('sürat 2 katı', 'g-y', True), ('kütle aynı', 'g-s', False), 4, '4 birim')]
    for i, (r, L, s1, s2, kat, etiket) in enumerate(satirlar):
        y = 74 + i * 50
        cx = 34
        ic += _top(cx, y, r)
        ic += _ok(cx + r + 5, y, cx + r + 5 + L, y, 'g-ms', 'f77c', 2.4)
        ic += _yazi(110, y - 3, s1[0], 12, s1[1], 'start', s1[2]) + _yazi(110, y + 12, s2[0], 12, s2[1], 'start', s2[2])
        ic += f'<rect x="208" y="{y - 9}" width="{kat * U}" height="18" rx="4" class="g-mf"/>'
        ic += _yazi(208 + kat * U + 8, y + 5, etiket, 13, 'g-mf', 'start', True)
    ic += _yazi(230, 212, 'Sürat 2 katına çıkınca kinetik enerji 4 katına çıkar.', 12.5, 'g-mf', kalin=True)
    ic += _yazi(230, 228, 'Çubuklar ölçekli (1 : 2 : 4); top boyutu ölçeksiz.', 11.5, 'g-s')
    return svg(460, 236, ic, 'Kinetik enerji kütleye ve sürate bağlıdır. Üç satırda top ve sürat oku, sağda ölçekli kinetik enerji çubuğu vardır: '
               'temel durumda 1 birim; kütle iki katına çıkınca 2 birim; sürat iki katına çıkınca 4 birim. '
               'Sürat, kinetik enerjiyi kütleden daha güçlü etkiler.')


# ---------- 3) Çekim potansiyel enerjisi: kum deneyi ----------
def cekim_potansiyel():
    """Üç deney: küçük bilye h'den, büyük bilye h'den, küçük bilye 2h'den kuma bırakılır; çukur derinliği yapılan işi gösterir."""
    ic = '<defs>' + ok_isareti('f77d', 'g-tf') + ok_isareti('f77e', 'g-mf') + '</defs>'
    y0 = 200
    deneyler = [(80, 8, 66, 'küçük bilye', 'yükseklik h', 'h', 14, 5, 'sığ çukur: az iş', 'az enerji'),
                (230, 12, 66, 'büyük bilye', 'yükseklik h', 'h', 24, 14, 'derin çukur: çok iş', 'daha çok enerji'),
                (380, 8, 132, 'küçük bilye', 'yükseklik 2h', '2h', 20, 14, 'derin çukur: çok iş', 'daha çok enerji')]
    for c, r, h, b1, b2, hs, rx, ry, s1, s2 in deneyler:
        ic += _yazi(c, 18, b1, 13, 'g-y', kalin=True) + _yazi(c, 34, b2, 12, 'g-tf', kalin=True)
        # kum kabı ve kum
        ic += f'<rect x="{c - 56}" y="{y0}" width="112" height="52" class="g-s" opacity="0.22"/>'
        for i in range(16):
            px = c - 50 + (i * 37) % 100
            py = y0 + 6 + (i * 23) % 42
            if ((px - c) / (rx + 4)) ** 2 + ((py - y0) / (ry + 4)) ** 2 >= 1:
                ic += f'<circle cx="{px}" cy="{py}" r="1.4" class="g-s"/>'
        ic += f'<path d="M{c - 56} {y0 - 4} L{c - 56} {y0 + 52} L{c + 56} {y0 + 52} L{c + 56} {y0 - 4}" class="g-c" stroke-width="2.2" stroke-linejoin="round"/>'
        # çukur
        ic += f'<path d="M{c - rx} {y0} A{rx} {ry} 0 0 0 {c + rx} {y0} Z" class="g-z"/>'
        ic += f'<path d="M{c - rx} {y0} A{rx} {ry} 0 0 0 {c + rx} {y0}" class="g-c" stroke-width="1.6"/>'
        # bilye, yükseklik oku, düşme yönü
        yb = y0 - h
        ic += _top(c, yb - r, r)
        ic += _cift_ok(c - 40, y0 - 2, c - 40, yb, 'g-ts', 'f77d', 2.2)
        ic += _yazi(c - 50, (y0 - 2 + yb) / 2 + 5, hs, 14, 'g-tf', 'end', True)
        ic += _ok(c, yb + 6, c, y0 - 8, 'g-ms', 'f77e', 2.2, kesik='4 4')
        ic += _yazi(c, 270, s1, 12, 'g-yf', kalin=True) + _yazi(c, 286, s2, 12, 'g-tf')
    ic += _yazi(230, 308, 'Çukur derinse bilye kuma daha çok iş yapmıştır.', 12, 'g-y')
    ic += _yazi(230, 322, 'Ölçeksiz; her deneyde tek değişken değişir.', 11.5, 'g-s')
    return svg(460, 330, ic, 'Kum dolu kaba bilye bırakma deneyi üç kez gösterilir. Küçük bilye h yüksekliğinden bırakılınca sığ çukur açar: az iş. '
               'Aynı yükseklikten büyük bilye daha derin çukur açar: kütle büyük, enerji daha çok. Küçük bilye 2h yüksekliğinden bırakılınca da '
               'çukur derinleşir: yükseklik büyük, enerji daha çok. Çukur ne kadar derinse bilye kuma o kadar çok iş yapmıştır.')


# ---------- 4) Esneklik potansiyel enerjisi: az ve çok gerilen yay ----------
def esneklik():
    """İki satır: az gerilmiş ve çok gerilmiş ok yayı; depolanan enerji çubuğu ve okun fırlama sürati."""
    ic = '<defs>' + ok_isareti('f77f', 'g-s') + ok_isareti('f77g', 'g-mf') + '</defs>'
    ic += _yazi(22, 28, 'yay ve ok', 12.5, 'g-y', 'start', True)
    ic += _yazi(224, 28, 'depolanan enerji', 12.5, 'g-of', 'start', True)
    ic += _yazi(352, 28, 'okun sürati', 12.5, 'g-mf', 'start', True)
    satirlar = [(74, 14, 'az gerildi', 32, 'az', 26, ('daha yavaş',)),
                (188, 46, 'çok gerildi', 104, 'çok', 84, ('daha hızlı', 'daha uzağa'))]
    for y, p, ad, L, et, L2, sonuc in satirlar:
        # yay gövdesi (mor) ve kiriş
        ic += f'<path d="M112 {y - 40} Q136 {y} 112 {y + 40}" class="g-os" stroke-width="4" stroke-linecap="round"/>'
        ic += f'<path d="M112 {y - 40} L{112 - p} {y} L112 {y + 40}" class="g-os" stroke-width="1.6" stroke-linejoin="round"/>'
        # ok (gri cisim): gövde, uç, tüyler
        ic += _ok(112 - p, y, 112 - p + 96, y, 'g-c', 'f77f', 2.8)
        for s in (-1, 1):
            ic += f'<line x1="{112 - p + 2}" y1="{y}" x2="{112 - p + 11}" y2="{y + 6 * s}" class="g-c" stroke-width="2" stroke-linecap="round"/>'
        # gerilme miktarı (mor ayraç) ve etiketi
        ic += (f'<line x1="{112 - p}" y1="{y + 52}" x2="112" y2="{y + 52}" class="g-os" stroke-width="2"/>'
               f'<line x1="{112 - p}" y1="{y + 48}" x2="{112 - p}" y2="{y + 56}" class="g-os" stroke-width="2"/>'
               f'<line x1="112" y1="{y + 48}" x2="112" y2="{y + 56}" class="g-os" stroke-width="2"/>')
        ic += _yazi(112 - p / 2, y + 70, ad, 12.5, 'g-of', kalin=True)
        # depolanan esneklik potansiyel enerjisi çubuğu
        ic += f'<rect x="224" y="{y - 8}" width="{L}" height="16" rx="4" class="g-of"/>'
        ic += _yazi(224 + L / 2, y + 4, et, 12, 'g-b', kalin=True)
        # okun fırlama sürati (mavi)
        ic += _ok(352, y, 352 + L2, y, 'g-ms', 'f77g', 2.6)
        for j, s in enumerate(sonuc):
            ic += _yazi(352 + L2 / 2, y + 20 + j * 14, s, 12, 'g-mf')
    ic += _yazi(230, 276, 'Çok gerilen yay daha çok enerji depolar (ölçeksiz).', 12, 'g-s')
    return svg(460, 288, ic, 'Ok yayı iki durumda gösterilir. Az gerilen yay az esneklik potansiyel enerjisi depolar; bırakılınca ok daha yavaş fırlar. '
               'Çok gerilen yay çok enerji depolar; ok daha hızlı fırlar ve daha uzağa gider. Depolanan enerji, yayın ne kadar şekil değiştirdiğine bağlıdır.')


# ---------- 5) Salıncak: kinetik ve potansiyel enerji el değiştirir ----------
def salincak():
    """Salıncak üç konumda: iki uçta en yüksek nokta (P en büyük, K sıfır), ortada en alçak nokta (K en büyük, P en küçük)."""
    ic = '<defs>' + ok_isareti('f77h', 'g-mf') + '</defs>'
    ic += _yazi(14, 16, 'P: çekim potansiyel enerjisi', 12, 'g-tf', 'start', True)
    ic += _yazi(446, 16, 'K: kinetik enerji', 12, 'g-mf', 'end', True)
    px, py, R = 230, 30, 140
    ic += '<line x1="196" y1="30" x2="264" y2="30" class="g-c" stroke-width="4" stroke-linecap="round"/>'
    sol = (px - R * math.sin(math.radians(50)), py + R * math.cos(math.radians(50)))
    sag = (px + R * math.sin(math.radians(50)), py + R * math.cos(math.radians(50)))
    alt = (px, py + R)
    ic += f'<path d="M{sol[0]:.1f} {sol[1]:.1f} A{R} {R} 0 0 0 {sag[0]:.1f} {sag[1]:.1f}" class="g-c" stroke-width="1.5" stroke-dasharray="5 5"/>'
    for (sx, sy), kesik in ((sol, '5 4'), (sag, '5 4'), (alt, None)):
        k = f' stroke-dasharray="{kesik}"' if kesik else ''
        ic += f'<line x1="{px}" y1="{py}" x2="{sx:.1f}" y2="{sy:.1f}" class="g-c" stroke-width="2"{k}/>'
        ic += _kutu(round(sx - 15, 1), round(sy, 1), 30, 9, rx=3)
    ic += f'<circle cx="{px}" cy="{py}" r="4" class="g-s"/>'
    # hareket yönü: solda inerken sürat artar, sağda çıkarken azalır
    ic += _yay_ok(px, py, 122, 130, 100, 'g-ms', 'f77h', 2.4)
    ic += _yay_ok(px, py, 122, 80, 50, 'g-ms', 'f77h', 2.4)
    ic += _yazi(168, 196, 'P azalır', 12, 'g-tf', kalin=True) + _yazi(168, 210, 'K artar', 12, 'g-mf', kalin=True)
    ic += _yazi(292, 196, 'K azalır', 12, 'g-mf', kalin=True) + _yazi(292, 210, 'P artar', 12, 'g-tf', kalin=True)

    def cubuklar(x, taban, hp, hk):
        s = f'<rect x="{x}" y="{taban - hp}" width="14" height="{hp}" rx="2" class="g-tf"/>'
        s += (f'<rect x="{x + 20}" y="{taban - hk}" width="14" height="{hk}" rx="2" class="g-mf"/>' if hk
              else f'<rect x="{x + 20}" y="{taban - 2}" width="14" height="2" class="g-mf"/>')
        s += _yazi(x + 7, taban + 16, 'P', 12, 'g-tf', kalin=True) + _yazi(x + 27, taban + 16, 'K', 12, 'g-mf', kalin=True)
        return s
    ic += cubuklar(46, 168, 44, 0) + cubuklar(380, 168, 44, 0) + cubuklar(214, 246, 6, 44)
    for x in (66, 394):
        ic += _yazi(x, 204, 'en yüksek nokta', 12, 'g-y', kalin=True)
        ic += _yazi(x, 219, 'bir an durur', 12, 'g-s')
        ic += _yazi(x, 234, 'P en büyük, K sıfır', 12, 'g-y')
    ic += _yazi(230, 282, 'en alçak nokta: sürat en büyük', 12, 'g-y', kalin=True)
    ic += _yazi(230, 298, 'K en büyük, P en küçük (çubuklar ölçeksiz)', 12, 'g-y')
    return svg(460, 306, ic, 'Salıncak üç konumda çizilmiştir. İki uçtaki en yüksek noktada salıncak bir an durur: kinetik enerji sıfır, '
               'çekim potansiyel enerjisi en büyüktür. Ortadaki en alçak noktada sürat ve kinetik enerji en büyük, potansiyel enerji en küçüktür. '
               'Aşağı inerken potansiyel enerji azalır ve kinetik enerji artar; yukarı çıkarken tersi olur.')


def uygula(o):
    g = {'İş ile enerji arasındaki bağ': is_enerji(),
         'Kinetik enerji: hareket eden her cisimde': kinetik(),
         'Çekim potansiyel enerjisi: yüksekteki cisim': cekim_potansiyel(),
         'Esneklik potansiyel enerjisi: gerilen ve sıkışan cisimler': esneklik(),
         'Aynı anda ikisi birden: enerji el değiştirir': salincak()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
