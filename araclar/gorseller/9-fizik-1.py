"""9. sınıf Fizik, 1. hafta: Fizik Bilimi (FİZ.9.1.1).

Görseller yalnız MEB 9. sınıf Fizik ders kitabındaki bilgilerle çizilir (kitap s. 15-22).
Renk anlamı iki görselde de aynıdır: turuncu = ışık ve renk, mavi = dalgalar,
yeşil = kuvvet, hareket, enerji; mor yalnız matematik kutusunda (fizik matematikten yararlanır).
Tanım kutusu nötr renktedir.
"""
import math

from ozet_gorsel import svg

RENK = {  # (dolgu, çerçeve, yazı)
    'isik': ('g-ta', 'g-ts', 'g-tf'),
    'dalga': ('g-ma', 'g-ms', 'g-mf'),
    'kuvvet': ('g-ya', 'g-ys', 'g-yf'),
    'mat': ('g-oa', 'g-os', 'g-of'),
}


def _ok(kimlik):
    # içi dolu gri ok ucu (g-c sınıfı dolguyu kapattığı için dolgu ayrıca verilir)
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            '<path d="M0 0L10 5L0 10z" class="g-c" style="fill:var(--g-cizgi)"/></marker>')


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _notr_kutu(x, y, w, h, rx=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="2"/>')


def disiplin_haritasi():
    """Fizik biliminin ilişkili olduğu disiplinler (kitap s. 17-18 bilgi kartları, s. 22 Kontrol Noktası)."""
    sol = [('Astronomi', 'gezegen yörüngeleri', 'kuvvet'),
           ('Biyoloji', 'mikroskopla doku', 'isik'),
           ('Müzik', 'telli enstrüman sesi', 'dalga'),
           ('Matematik', 'aracın sürat grafiği', 'mat')]
    sag = [('Görsel sanatlar', 'resimde ışık ve renk', 'isik'),
           ('Kimya', 'atom ve moleküller', 'kuvvet'),
           ('Coğrafya', 'tsunami dalgaları', 'dalga'),
           ('Spor', 'basketbol atışı', 'kuvvet')]
    W, KW, KH = 472, 150, 50
    cx, cy, r = 236, 128, 48
    ic = ''
    for kolon, x in ((sol, 8), (sag, W - 8 - KW)):
        for i, (ad, ornek, renk) in enumerate(kolon):
            y = 10 + i * 62
            ym = y + KH / 2
            # bağlantı çizgisi: kutunun iç kenarından çembere, ikisine de değmeden
            bx = x + KW + 4 if x < cx else x - 4
            dx, dy = bx - cx, ym - cy
            L = math.hypot(dx, dy)
            ex, ey = cx + dx / L * (r + 5), cy + dy / L * (r + 5)
            ic += f'<line x1="{bx:.1f}" y1="{ym:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" class="g-c" stroke-width="2" stroke-linecap="round"/>'
            ic += _kutu(x, y, KW, KH, renk, rx=10)
            ic += f'<text x="{x + KW / 2:.0f}" y="{y + 21}" text-anchor="middle" font-size="12.5" font-weight="800" class="{RENK[renk][2]}">{ad}</text>'
            ic += f'<text x="{x + KW / 2:.0f}" y="{y + 39}" text-anchor="middle" font-size="11.5" class="g-y">{ornek}</text>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-z"/><circle cx="{cx}" cy="{cy}" r="{r}" class="g-c" stroke-width="3"/>'
    ic += f'<text x="{cx}" y="{cy - 3}" text-anchor="middle" font-size="15" font-weight="800" class="g-y">Fizik</text>'
    ic += f'<text x="{cx}" y="{cy + 16}" text-anchor="middle" font-size="15" font-weight="800" class="g-y">bilimi</text>'
    # renk açıklaması: iki satır, iki sütun (yazılar birbirine değmez)
    ic += f'<text x="{W / 2:.0f}" y="272" text-anchor="middle" font-size="11.5" class="g-s">Kutunun rengi, ilişkiyi kuran konuyu gösterir:</text>'
    for k, (renk, ad) in enumerate((('isik', 'ışık ve renk'), ('dalga', 'dalgalar'),
                                    ('kuvvet', 'kuvvet, hareket, enerji'), ('mat', 'fizik matematikten yararlanır'))):
        x, y = (28 if k % 2 == 0 else 250), 294 + (k // 2) * 22
        ic += f'<circle cx="{x}" cy="{y - 4}" r="6" class="{RENK[renk][2]}"/><text x="{x + 12}" y="{y}" font-size="11.5" class="g-y">{ad}</text>'
    return svg(W, 326, ic, 'Fizik biliminin ilişkili olduğu disiplinler: astronomi (gezegen yörüngeleri, hareket), biyoloji (mikroskopla doku, ışık), '
               'müzik (telli enstrüman sesi, dalgalar), matematik (fizik, aracın sürat grafiğinde matematikten yararlanır), '
               'görsel sanatlar (resimde ışık ve renk), kimya (atom ve moleküller, hareket ve enerji), coğrafya (tsunami, dalgalar), '
               'spor (basketbol atışı, kuvvet, hareket, enerji)')


def ornekten_tanima():
    """Tek tek örneklerden fizik biliminin genel tanımına (tümevarım); kitap s. 19-22."""
    ic = '<defs>' + _ok('okFZ9') + '</defs>'
    ic += '<text x="8" y="18" font-size="12.5" font-weight="800" class="g-y">1. Örnekleri incele</text>'
    kart = [('Gökkuşağı', ['ışığın kırılması'], 'isik'), ('Kaykay', ['enerji dönüşümü'], 'kuvvet'),
            ('Pota atışı', ['kuvvet, hareket,', 've enerji'], 'kuvvet'), ('Tsunami', ['dalgalar'], 'dalga')]
    KY, KH = 28, 64
    for i, (ad, konu, renk) in enumerate(kart):
        x = 8 + i * 116
        ic += _kutu(x, KY, 108, KH, renk, rx=10)
        ic += f'<text x="{x + 54}" y="{KY + 22}" text-anchor="middle" font-size="12.5" font-weight="800" class="{RENK[renk][2]}">{ad}</text>'
        ys = [KY + 44] if len(konu) == 1 else [KY + 40, KY + 55]
        for yy, satir in zip(ys, konu):
            ic += f'<text x="{x + 54}" y="{yy}" text-anchor="middle" font-size="11.5" class="g-y">{satir}</text>'
        ic += f'<line x1="{x + 54}" y1="{KY + KH + 6}" x2="{x + 54}" y2="{KY + KH + 26}" class="g-c" stroke-width="2" marker-end="url(#okFZ9)"/>'
    # 2. ortak nokta
    y2 = KY + KH + 34  # 126
    ic += _notr_kutu(8, y2, 456, 74)
    ic += f'<text x="236" y="{y2 + 22}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">2. Ortak noktayı bul</text>'
    ic += f'<text x="236" y="{y2 + 42}" text-anchor="middle" font-size="12" class="g-y">Hepsi evrende gerçekleşen bir olay.</text>'
    ic += f'<text x="236" y="{y2 + 61}" text-anchor="middle" font-size="12" class="g-y">Hepsi fiziğin kavramlarıyla açıklanıyor.</text>'
    ic += f'<line x1="236" y1="{y2 + 80}" x2="236" y2="{y2 + 100}" class="g-c" stroke-width="2" marker-end="url(#okFZ9)"/>'
    # 3. genel tanım (nötr kutu, kalın çerçeve)
    y3 = y2 + 108  # 234
    ic += (f'<rect x="8" y="{y3}" width="456" height="114" rx="12" class="g-z"/>'
           f'<rect x="8" y="{y3}" width="456" height="114" rx="12" class="g-c" stroke-width="3"/>')
    ic += f'<text x="236" y="{y3 + 22}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">3. Genel tanıma ulaş: Fizik bilimi</text>'
    for k, satir in enumerate(('kuvvet, madde, enerji, uzay ve zaman',
                               'arasındaki ilişkileri temel alarak evreni',
                               'gözlem ve matematiksel hesaplarla inceleyen',
                               'yasa ve teorilerin bütünüdür.')):
        ic += f'<text x="236" y="{y3 + 44 + k * 18}" text-anchor="middle" font-size="11.5" class="g-y">{satir}</text>'
    # ölçek şeridi
    y4 = y3 + 114 + 26  # 374
    ic += f'<text x="236" y="{y4}" text-anchor="middle" font-size="11.5" class="g-s">Fizik doğayı çok farklı ölçeklerde inceler:</text>'
    ic += f'<text x="8" y="{y4 + 26}" font-size="12" font-weight="700" class="g-y">atom altı parçacıklar</text>'
    ic += f'<line x1="180" y1="{y4 + 22}" x2="376" y2="{y4 + 22}" class="g-c" stroke-width="2" marker-start="url(#okFZ9)" marker-end="url(#okFZ9)"/>'
    ic += f'<text x="464" y="{y4 + 26}" text-anchor="end" font-size="12" font-weight="700" class="g-y">galaksiler</text>'
    return svg(472, y4 + 38, ic, 'Örneklerden fizik biliminin tanımına: 1. Örnekleri incele (gökkuşağı: ışığın kırılması; kaykay: enerji dönüşümü; '
               'pota atışı: kuvvet, hareket ve enerji; tsunami: dalgalar). 2. Ortak noktayı bul (hepsi evrende gerçekleşen, fiziğin kavramlarıyla açıklanan olaylar). '
               '3. Genel tanıma ulaş: Fizik bilimi kuvvet, madde, enerji, uzay ve zaman arasındaki ilişkileri temel alarak evreni gözlem ve matematiksel '
               'hesaplarla inceleyen yasa ve teorilerin bütünüdür. Fizik doğayı atom altı parçacıklar kadar küçük, galaksiler kadar büyük ölçeklerde inceler.')


def uygula(o):
    g = {'Fizik başka disiplinlerle nasıl ilişkilidir?': disiplin_haritasi(),
         'Örneklerden fizik biliminin tanımına': ornekten_tanima()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
