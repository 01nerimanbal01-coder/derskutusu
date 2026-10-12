"""8. sınıf Fen Bilimleri, 4. hafta: sera etkisi, kromozom sayıları, nükleotid ve kalıtım birimleri.

Görseller yalnız haftanın metnindeki bilgilerle çizilir:
- Sera etkisi: turuncu = Güneş ışınları (gelen ve yansıyan), mor = yeryüzünden yayılan ısı, yeşil = sera gazları, mavi = atmosfer.
- Kromozom sayıları: çubuk uzunluğu sayıyla orantılı, tek ölçek (1 kromozom = 0,62 birim); turuncu = farklı türde aynı sayı (insan ve moli balığı, 46).
- Nükleotid: mor = fosfat grubu, yeşil = deoksiriboz şekeri, turuncu = azotlu organik baz (A, T, G, C).
- Kalıtım birimleri: iç içe kutular; mor = çekirdek, mavi = kromozom, yeşil = DNA, turuncu = gen, dolu mor = nükleotid.
Boyutlar dışında ölçek iddiası yoktur. Okların ucu dolgulu üçgendir (işaretçi kullanılmaz).
"""
import math

from ozet_gorsel import svg


def _t(x, y, metin, boyut, sinif, anchor='middle', kalin=False):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    k = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}"{a} font-size="{boyut:g}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, cizgi, dolgu, w=3.0, bas=11.0, kesik=None):
    """Çizgi ve dolgulu üçgen ok başı; başın ucu (x2, y2) noktasındadır."""
    dx, dy = x2 - x1, y2 - y1
    u = math.hypot(dx, dy)
    ux, uy = dx / u, dy / u
    bx, by = x2 - ux * bas, y2 - uy * bas
    px, py = -uy, ux
    h = bas * 0.55
    nokta = f'{x2:.1f},{y2:.1f} {bx + px * h:.1f},{by + py * h:.1f} {bx - px * h:.1f},{by - py * h:.1f}'
    kz = f' stroke-dasharray="{kesik}"' if kesik else ''
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{bx + ux:.1f}" y2="{by + uy:.1f}" class="{cizgi}" stroke-width="{w:g}"{kz}/>'
            f'<polygon points="{nokta}" class="{dolgu}"/>')


def _besgen(cx, cy, r, sinif):
    pts = [(cx + r * math.cos(math.radians(-90 + 72 * i)), cy + r * math.sin(math.radians(-90 + 72 * i))) for i in range(5)]
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" class="{sinif}" stroke-linejoin="round"/>'


# ---------- 1) Sera etkisi ----------
def sera_etkisi():
    ic = ''
    # atmosfer ve yeryüzü
    ic += '<rect x="8" y="88" width="454" height="96" rx="16" class="g-ma"/>'
    ic += '<rect x="8" y="236" width="454" height="48" rx="10" class="g-z"/><rect x="8" y="236" width="454" height="48" rx="10" class="g-c" stroke-width="2"/>'
    ic += _t(22, 108, 'atmosfer', 12.5, 'g-mf', 'start', True)
    ic += _t(22, 264, 'yeryüzü', 12.5, 'g-s', 'start', True)
    # Güneş
    ic += '<circle cx="56" cy="42" r="20" fill="#f5c421"/>'
    for i in range(8):
        a = math.radians(i * 45)
        ic += (f'<line x1="{56 + 26 * math.cos(a):.1f}" y1="{42 + 26 * math.sin(a):.1f}" x2="{56 + 33 * math.cos(a):.1f}" y2="{42 + 33 * math.sin(a):.1f}" '
               f'stroke="#f5c421" stroke-width="3" stroke-linecap="round"/>')
    # gelen Güneş ışınları (üç paralel ok)
    for x in (92, 116, 140):
        ic += _ok(x, 54, x + 57, 232, 'g-ts', 'g-tf', 3.2, 12)
    ic += _t(14, 210, 'Güneş ışınları', 12.5, 'g-tf', 'start', True)
    # yeryüzünden uzaya yansıyan ışınların bir kısmı
    ic += _ok(201, 230, 245, 66, 'g-ts', 'g-tf', 3, 12, '7 5')
    ic += _t(232, 50, 'uzaya yansıyan ışınlar', 12.5, 'g-tf', 'middle', True)
    # sera gazları
    for x, y in ((300, 130), (346, 126), (368, 144), (410, 128), (432, 146), (448, 126), (304, 160), (350, 162), (424, 168), (448, 164)):
        ic += f'<circle cx="{x}" cy="{y}" r="4.4" class="g-yf"/>'
    ic += _t(386, 108, 'sera gazları', 12.5, 'g-yf', 'middle', True)
    # yeryüzünden yayılan ısı: biri uzaya çıkar, biri sera gazlarınca tutulur
    ic += _ok(324, 232, 324, 40, 'g-os', 'g-of', 3.4, 13)
    ic += _t(334, 70, 'uzaya çıkan ısı', 12.5, 'g-of', 'start', True)
    ic += _ok(392, 232, 392, 174, 'g-os', 'g-of', 3.4, 13)
    ic += _t(404, 206, 'tutulan', 12.5, 'g-of', 'start', True) + _t(404, 221, 'ısı', 12.5, 'g-of', 'start', True)
    return svg(470, 292, ic, 'Sera etkisi. Güneş ışınları atmosferden geçerek yeryüzüne ulaşır; ışınların bir kısmı yeryüzünden uzaya yansır. '
               'Yeryüzünden yayılan ısının bir kısmı uzaya çıkar, bir kısmı atmosferdeki sera gazları tarafından tutulur.')


# ---------- 2) Kromozom sayıları (tek ölçek) ----------
def kromozom_sayilari():
    K = 0.62
    X0 = 122
    veri = (('Eğrelti otu', 500, 'g-mf'), ('Denizyıldızı', 94, 'g-mf'), ('İnsan', 46, 'g-tf'),
            ('Moli balığı', 46, 'g-tf'), ('Buğday', 42, 'g-mf'), ('Kızıl tilki', 38, 'g-mf'))
    ic = _t(X0, 16, 'kromozom sayısı', 12, 'g-s', 'start', True)
    ic += f'<line x1="{X0}" y1="24" x2="{X0}" y2="228" class="g-c" stroke-width="2"/>'
    for i, (ad, n, sinif) in enumerate(veri):
        y = 34 + i * 33
        ic += _t(X0 - 10, y + 17, ad, 13, 'g-y', 'end', True)
        ic += f'<rect x="{X0}" y="{y}" width="{n * K:.1f}" height="24" rx="4" class="{sinif}"/>'
        ic += _t(round(X0 + n * K + 8, 1), y + 17, str(n), 13, 'g-tf' if sinif == 'g-tf' else 'g-mf', 'start', True)
    # insan ve moli balığı: farklı tür, aynı sayı
    ic += ('<path d="M196 100H204V157H196" class="g-ts" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    ic += _t(214, 126, 'farklı türler,', 12.5, 'g-tf', 'start', True) + _t(214, 142, 'aynı sayı', 12.5, 'g-tf', 'start', True)
    return svg(470, 236, ic, 'Bazı canlıların kromozom sayıları, tek ölçekle çizilmiş çubuklarla: eğrelti otu 500, denizyıldızı 94, insan 46, moli balığı 46, '
               'buğday 42, kızıl tilki 38. İnsan ile moli balığı farklı türlerdir; ikisinde de 46 kromozom vardır.')


# ---------- 3) Nükleotidin parçaları ve adlandırılması ----------
def nukleotid():
    ic = _t(235, 20, 'Bir nükleotidin üç parçası', 14, 'g-y', 'middle', True)
    # büyük model
    ic += '<circle cx="84" cy="68" r="24" class="g-of"/>'
    ic += _besgen(200, 68, 27, 'g-yf')
    ic += '<rect x="286" y="46" width="112" height="44" rx="12" class="g-tf"/>' + _t(342, 74, 'baz', 16, 'g-b', 'middle', True)
    ic += '<line x1="112" y1="68" x2="170" y2="68" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    ic += '<line x1="228" y1="68" x2="282" y2="68" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    ic += _t(84, 114, 'fosfat grubu', 13, 'g-of', 'middle', True)
    ic += _t(200, 114, 'deoksiriboz', 13, 'g-yf', 'middle', True) + _t(200, 129, '(beş karbonlu şeker)', 11, 'g-s')
    ic += _t(342, 114, 'azotlu organik baz', 13, 'g-tf', 'middle', True)
    ic += '<line x1="24" y1="148" x2="446" y2="148" class="g-c" stroke-width="1.5" stroke-dasharray="4 5"/>'
    # dört nükleotid: şeker ve fosfat aynı, baz farklı
    ic += _t(235, 172, 'Nükleotidin adını baz belirler', 14, 'g-y', 'middle', True)
    for x0, harf, ad in ((22, 'A', 'adenin'), (136, 'T', 'timin'), (250, 'G', 'guanin'), (364, 'C', 'sitozin')):
        ic += f'<circle cx="{x0 + 9}" cy="212" r="9" class="g-of"/>'
        ic += _besgen(x0 + 33, 212, 11, 'g-yf')
        ic += f'<rect x="{x0 + 52}" y="199" width="34" height="26" rx="8" class="g-tf"/>' + _t(x0 + 69, 218, harf, 15, 'g-b', 'middle', True)
        ic += f'<line x1="{x0 + 18}" y1="212" x2="{x0 + 22}" y2="212" class="g-c" stroke-width="2.4" stroke-linecap="round"/>'
        ic += f'<line x1="{x0 + 44}" y1="212" x2="{x0 + 52}" y2="212" class="g-c" stroke-width="2.4" stroke-linecap="round"/>'
        ic += _t(x0 + 43, 250, ad, 13, 'g-tf', 'middle', True) + _t(x0 + 43, 265, 'nükleotidi', 11.5, 'g-s')
    ic += _t(235, 292, 'Şeker ve fosfat aynıdır; değişen parça bazdır.', 12.5, 'g-y')
    return svg(470, 300, ic, 'Bir nükleotid üç parçadan oluşur: fosfat grubu, deoksiriboz şekeri ve azotlu organik baz. '
               'Şeker ve fosfat her nükleotidde aynıdır; baz adenin (A), timin (T), guanin (G) ya da sitozin (C) olabilir ve nükleotid bazın adıyla anılır.')


# ---------- 4) Büyükten küçüğe kalıtım birimleri ----------
def kalitim_birimleri():
    # (ad, açıklama, zemin, çizgi, yazı, x, y, w, h)
    seviye = [('Hücre', '', 'g-z', 'g-c', 'g-y', 6, 6, 458, 214),
              ('Çekirdek', '', 'g-oa', 'g-os', 'g-of', 22, 32, 426, 178),
              ('Kromozom', 'kromatin ağının kısalıp kalınlaşmış hâli', 'g-ma', 'g-ms', 'g-mf', 38, 58, 394, 142),
              ('DNA', 'çift nükleotid dizisi, sarmal yapı', 'g-ya', 'g-ys', 'g-yf', 54, 84, 362, 106),
              ('Gen', 'belirli bir özellikten sorumlu', 'g-ta', 'g-ts', 'g-tf', 70, 110, 330, 70)]
    ic = ''
    for ad, ac, zemin, cizgi, yazi, x, y, w, h in seviye:
        ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="{zemin}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="{cizgi}" stroke-width="2"/>'
        ic += _t(x + 12, y + 18, ad, 13.5, yazi, 'start', True)
        if ac:
            ic += _t(x + w - 12, y + 18, ac, 11.5, 'g-s', 'end')
    # en içte nükleotid
    ic += '<rect x="86" y="136" width="298" height="34" rx="10" class="g-of"/>'
    ic += _t(98, 158, 'Nükleotid', 13.5, 'g-b', 'start', True) + _t(372, 158, 'DNA’nın yapı birimi', 11.5, 'g-b', 'end')
    return svg(470, 226, ic, 'İç içe kutular, büyükten küçüğe: hücrenin içinde çekirdek, çekirdeğin içinde kromozom, kromozomun içinde DNA, DNA üzerinde gen, '
               'genin yapısında nükleotid bulunur.')


def uygula(o):
    g = {'Etkenler, sera gazları ve iklim değişikliği': sera_etkisi(),
         'Kromatin ve kromozom': kromozom_sayilari(),
         'Gen ve nükleotid': nukleotid(),
         'Kalıtım birimleri arasındaki ilişki': kalitim_birimleri()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
