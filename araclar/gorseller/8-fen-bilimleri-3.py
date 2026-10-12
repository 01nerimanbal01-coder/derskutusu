"""8. sınıf Fen Bilimleri, 3. hafta: iklim ile hava olayları arasındaki fark.

Görseller yalnız haftanın metnindeki bilgilerle çizilir:
- Yağış, sis, çiy, kırağı: satır = suyun hâli (mavi = sıvı, mor = katı/buz), sütun = oluştuğu yer.
  Yağmur sıvı, dolu ve kar katı hâlde yeryüzüne iner; çiy sıvı, kırağı katı hâlde yüzeyde birikir; sis hem damlacık hem kristal olarak havada asılı kalır.
- Basınç alanları: turuncu = ısınan hava (alçak basınç), mavi = soğuyan hava (yüksek basınç), yeşil = rüzgâr.
- Karşılaştırma: turuncu = hava olayları, mavi = iklim (alan, süre, değişkenlik); ölçek iddiası yoktur.
Okların ucu dolgulu üçgendir (işaretçi kullanılmaz).
"""
import math

from ozet_gorsel import svg


def _t(x, y, metin, boyut, sinif, anchor='middle', kalin=False):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    k = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}"{a} font-size="{boyut:g}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, cizgi, dolgu, w=3.0, bas=11.0):
    """Çizgi ve dolgulu üçgen ok başı; başın ucu (x2, y2) noktasındadır."""
    dx, dy = x2 - x1, y2 - y1
    u = math.hypot(dx, dy)
    ux, uy = dx / u, dy / u
    bx, by = x2 - ux * bas, y2 - uy * bas
    px, py = -uy, ux
    h = bas * 0.55
    nokta = f'{x2:.1f},{y2:.1f} {bx + px * h:.1f},{by + py * h:.1f} {bx - px * h:.1f},{by - py * h:.1f}'
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{bx + ux:.1f}" y2="{by + uy:.1f}" class="{cizgi}" stroke-width="{w:g}"/>'
            f'<polygon points="{nokta}" class="{dolgu}"/>')


def _damla(cx, cy, s, sinif='g-mf'):
    return (f'<path transform="translate({cx:g} {cy:g}) scale({s:g})" '
            f'd="M0 -12C5 -5 9 0 9 5A9 9 0 0 1 -9 5C-9 0 -5 -5 0 -12Z" class="{sinif}"/>')


def _kar_tanesi(cx, cy, r, sinif='g-os'):
    ic = ''
    for aci in (0, 60, 120):
        a = math.radians(aci)
        x, y = r * math.cos(a), r * math.sin(a)
        ic += f'<line x1="{cx - x:.1f}" y1="{cy - y:.1f}" x2="{cx + x:.1f}" y2="{cy + y:.1f}" class="{sinif}" stroke-width="2.2" stroke-linecap="round"/>'
    for aci in (0, 60, 120, 180, 240, 300):
        a = math.radians(aci)
        mx, my = cx + 0.58 * r * math.cos(a), cy + 0.58 * r * math.sin(a)
        for d in (-50, 50):
            b = math.radians(aci + d)
            ic += (f'<line x1="{mx:.1f}" y1="{my:.1f}" x2="{mx + 0.3 * r * math.cos(b):.1f}" y2="{my + 0.3 * r * math.sin(b):.1f}" '
                   f'class="{sinif}" stroke-width="1.8" stroke-linecap="round"/>')
    return ic


def _kristal(x, y, sinif='g-os'):
    """Yüzeyde birikmiş bir buz kristali: dikey iğne ve iki dal."""
    return (f'<path d="M{x:g} {y:g}V{y - 15:g}M{x:g} {y - 6:g}L{x - 5:g} {y - 11:g}M{x:g} {y - 6:g}L{x + 5:g} {y - 11:g}" '
            f'class="{sinif}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')


def _arti(x, y, sinif='g-os'):
    return (f'<path d="M{x - 3.2:g} {y:g}H{x + 3.2:g}M{x:g} {y - 3.2:g}V{y + 3.2:g}M{x - 2.3:g} {y - 2.3:g}L{x + 2.3:g} {y + 2.3:g}M{x - 2.3:g} {y + 2.3:g}L{x + 2.3:g} {y - 2.3:g}" '
            f'class="{sinif}" stroke-width="1.5" stroke-linecap="round"/>')


# ---------- 1) Yağış, sis, çiy ve kırağı ----------
def yagis_siniflama():
    ic = ''
    # sütun başlıkları
    for cx, b1, b2 in ((134, 'Yeryüzüne iner', '(yağış)'), (266, 'Yüzeyde birikir', 'soğuk yüzeylerde'), (398, 'Havada kalır', 'yere yakın tabakada')):
        ic += _t(cx, 24, b1, 13, 'g-y', kalin=True) + _t(cx, 41, b2, 10.5, 'g-s')
    # hücre zeminleri
    ic += '<rect x="70" y="60" width="128" height="100" rx="10" class="g-ma"/><rect x="70" y="60" width="128" height="100" rx="10" class="g-ms" stroke-width="1.5"/>'
    ic += '<rect x="202" y="60" width="128" height="100" rx="10" class="g-ma"/><rect x="202" y="60" width="128" height="100" rx="10" class="g-ms" stroke-width="1.5"/>'
    ic += '<rect x="70" y="166" width="128" height="100" rx="10" class="g-oa"/><rect x="70" y="166" width="128" height="100" rx="10" class="g-os" stroke-width="1.5"/>'
    ic += '<rect x="202" y="166" width="128" height="100" rx="10" class="g-oa"/><rect x="202" y="166" width="128" height="100" rx="10" class="g-os" stroke-width="1.5"/>'
    ic += '<rect x="334" y="60" width="128" height="206" rx="10" class="g-z"/><rect x="334" y="60" width="128" height="206" rx="10" class="g-c" stroke-width="1.5"/>'
    # satır etiketleri
    ic += _t(36, 114, 'Sıvı', 14, 'g-mf', kalin=True)
    ic += _t(36, 212, 'Katı', 14, 'g-of', kalin=True) + _t(36, 229, '(buz)', 11, 'g-of')
    # yağmur
    for x, y in ((102, 104), (134, 94), (166, 104)):
        ic += _damla(x, y, 1.35)
    ic += _t(134, 148, 'Yağmur', 14, 'g-mf', kalin=True)
    # dolu ve kar
    ic += '<circle cx="104" cy="204" r="13" class="g-z"/><circle cx="104" cy="204" r="13" class="g-os" stroke-width="2.6"/>'
    ic += '<path d="M97 200A8 8 0 0 1 103 196" class="g-os" stroke-width="2" stroke-linecap="round"/>'
    ic += _kar_tanesi(166, 204, 15)
    ic += _t(104, 254, 'Dolu', 14, 'g-of', kalin=True) + _t(166, 254, 'Kar', 14, 'g-of', kalin=True)
    # çiy: soğuk yüzeyde sıvı damlacıklar
    ic += '<line x1="214" y1="118" x2="318" y2="118" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    for x, r in ((236, 8), (266, 11), (296, 8)):
        ic += f'<path d="M{x - r} 116A{r} {r} 0 0 1 {x + r} 116Z" class="g-mf"/>'
    ic += _t(266, 148, 'Çiy', 14, 'g-mf', kalin=True)
    # kırağı: soğuk yüzeyde buz kristalleri
    ic += '<line x1="214" y1="224" x2="318" y2="224" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    for x in (230, 248, 266, 284, 302):
        ic += _kristal(x, 221)
    ic += _t(266, 254, 'Kırağı', 14, 'g-of', kalin=True)
    # sis: yere yakın tabakada asılı damlacıklar ve kristaller
    ic += _t(398, 88, 'Sis', 14, 'g-y', kalin=True)
    ic += '<circle cx="364" cy="108" r="3.6" class="g-mf"/>' + _t(374, 112, 'damlacık', 11.5, 'g-mf', 'start')
    ic += _arti(364, 128, 'g-os') + _t(374, 132, 'kristal', 11.5, 'g-of', 'start')
    ic += '<rect x="346" y="160" width="104" height="76" rx="16" class="g-ma"/>'
    for x, y in ((364, 176), (394, 170), (428, 180), (378, 202), (412, 198), (440, 214), (360, 222), (400, 224)):
        ic += f'<circle cx="{x}" cy="{y}" r="3.6" class="g-mf"/>'
    for x, y in ((380, 182), (414, 176), (440, 196), (362, 208), (392, 214), (424, 220)):
        ic += _arti(x, y)
    ic += '<line x1="342" y1="244" x2="454" y2="244" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    return svg(470, 276, ic, 'Yağış, sis, çiy ve kırağının sınıflandırılması. Yağmur sıvı, dolu ve kar katı hâlde yeryüzüne iner. '
               'Çiy sıvı damlacıklar, kırağı buz kristalleri olarak soğuk yüzeylerde birikir. Sis, yere yakın bir tabakada asılı kalan '
               'su damlacıklarından ya da buz kristallerinden oluşur.')


# ---------- 2) Alçak ve yüksek basınç alanları ----------
def basinc_alanlari():
    ic = ''
    # paneller
    ic += '<rect x="6" y="6" width="226" height="238" rx="14" class="g-ta"/><rect x="6" y="6" width="226" height="238" rx="14" class="g-ts" stroke-width="2"/>'
    ic += '<rect x="238" y="6" width="226" height="238" rx="14" class="g-ma"/><rect x="238" y="6" width="226" height="238" rx="14" class="g-ms" stroke-width="2"/>'
    ic += _t(119, 30, 'Alçak basınç alanı', 15, 'g-tf', kalin=True) + _t(119, 46, 'ısınan hava', 11.5, 'g-s')
    ic += _t(351, 30, 'Yüksek basınç alanı', 15, 'g-mf', kalin=True) + _t(351, 46, 'soğuyan hava', 11.5, 'g-s')
    # yer çizgileri
    ic += '<line x1="22" y1="190" x2="216" y2="190" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    ic += '<line x1="254" y1="190" x2="448" y2="190" class="g-c" stroke-width="3.5" stroke-linecap="round"/>'
    # ---- alçak basınç: bulut + yağış, yükselen hava, rüzgâr merkeze ----
    bulut = ((101, 76, 11), (115, 69, 14), (133, 73, 12), (146, 78, 8))
    for cx, cy, r in bulut:
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-c" stroke-width="4"/>'
    ic += '<rect x="101" y="74" width="45" height="12" rx="4" class="g-c" stroke-width="4"/>'
    for cx, cy, r in bulut:
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-z"/>'
    ic += '<rect x="101" y="74" width="45" height="12" rx="4" class="g-z"/>'
    for x in (96, 142):
        ic += _damla(x, 108, 0.8)
    ic += _ok(119, 176, 119, 112, 'g-ts', 'g-tf', 5, 15)
    ic += _t(130, 142, 'yükselici', 12, 'g-tf', 'start', True) + _t(130, 157, 'hava', 12, 'g-tf', 'start', True)
    ic += _ok(28, 180, 92, 180, 'g-ys', 'g-yf', 3.5, 11) + _ok(210, 180, 146, 180, 'g-ys', 'g-yf', 3.5, 11)
    ic += _t(119, 212, 'çevreden merkeze rüzgâr', 12.5, 'g-yf', kalin=True)
    ic += _t(119, 232, 'hava kapalı, yağış olası', 12, 'g-y')
    # ---- yüksek basınç: güneş, alçalan hava, rüzgâr merkezden çevreye ----
    ic += '<circle cx="351" cy="76" r="12" fill="#f5c421"/>'
    for i in range(8):
        a = math.radians(i * 45)
        ic += (f'<line x1="{351 + 16 * math.cos(a):.1f}" y1="{76 + 16 * math.sin(a):.1f}" x2="{351 + 21 * math.cos(a):.1f}" y2="{76 + 21 * math.sin(a):.1f}" '
               f'stroke="#f5c421" stroke-width="2.6" stroke-linecap="round"/>')
    ic += _ok(351, 104, 351, 174, 'g-ms', 'g-mf', 5, 15)
    ic += _t(362, 130, 'alçalıcı', 12, 'g-mf', 'start', True) + _t(362, 145, 'hava', 12, 'g-mf', 'start', True)
    ic += _ok(340, 180, 276, 180, 'g-ys', 'g-yf', 3.5, 11) + _ok(362, 180, 426, 180, 'g-ys', 'g-yf', 3.5, 11)
    ic += _t(351, 212, 'merkezden çevreye rüzgâr', 12.5, 'g-yf', kalin=True)
    ic += _t(351, 232, 'hava açık', 12, 'g-y')
    # ---- iki alan arasında rüzgâr ----
    ic += _ok(440, 268, 30, 268, 'g-ys', 'g-yf', 4, 13)
    ic += _t(235, 259, 'Rüzgâr: yüksek basınçtan alçak basınca doğru', 13, 'g-yf', kalin=True)
    return svg(470, 282, ic, 'Alçak basınç alanında ısınan hava yükselir, rüzgârlar çevreden merkeze eser, hava kapalıdır ve yağış olasıdır. '
               'Yüksek basınç alanında soğuyan hava alçalır, rüzgârlar merkezden çevreye eser, hava açıktır. '
               'Rüzgâr yüksek basınç alanından alçak basınç alanına doğru eser.')


# ---------- 3) İklim ve hava olaylarının karşılaştırması ----------
def karsilastirma():
    ic = ''
    # kartlar
    ic += '<rect x="6" y="6" width="226" height="342" rx="14" class="g-ta"/><rect x="6" y="6" width="226" height="342" rx="14" class="g-ts" stroke-width="2"/>'
    ic += '<rect x="238" y="6" width="226" height="342" rx="14" class="g-ma"/><rect x="238" y="6" width="226" height="342" rx="14" class="g-ms" stroke-width="2"/>'
    ic += _t(119, 34, 'Hava olayları', 16, 'g-tf', kalin=True) + _t(351, 34, 'İklim', 16, 'g-mf', kalin=True)
    # satır başlıkları (ortak)
    for y, ad in ((58, 'Alan'), (168, 'Süre'), (262, 'Değişkenlik')):
        ic += _t(22, y, ad, 12, 'g-s', 'start', True) + _t(254, y, ad, 12, 'g-s', 'start', True)
        ic += f'<line x1="22" y1="{y + 8}" x2="216" y2="{y + 8}" class="g-ts" stroke-width="1" stroke-dasharray="3 4"/>'
        ic += f'<line x1="254" y1="{y + 8}" x2="448" y2="{y + 8}" class="g-ms" stroke-width="1" stroke-dasharray="3 4"/>'
    # alan: küçük dikdörtgen / büyük dikdörtgen (aynı en-boy oranı)
    ic += '<rect x="106" y="89" width="26" height="17" rx="3" class="g-tf"/>'
    ic += '<rect x="312" y="73" width="78" height="50" rx="6" class="g-mf"/>'
    ic += _t(119, 142, 'sınırlı bir yer', 13, 'g-tf', kalin=True) + _t(351, 142, 'geniş bir bölge', 13, 'g-mf', kalin=True)
    # süre: kısa çubuk / uzun çubuk
    ic += '<rect x="105" y="196" width="28" height="12" rx="6" class="g-tf"/>'
    ic += '<rect x="262" y="196" width="178" height="12" rx="6" class="g-mf"/>'
    ic += _t(119, 234, 'kısa süre', 13, 'g-tf', kalin=True) + _t(351, 234, 'en az 35–40 yıl', 13, 'g-mf', kalin=True)
    # değişkenlik: çok oynak çizgi / hemen hemen düz çizgi
    pts = [(32, 308), (52, 288), (72, 312), (92, 290), (112, 314), (132, 290), (152, 310), (172, 288), (192, 308), (210, 296)]
    ic += f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" class="g-ts" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    for x, y in pts:
        ic += f'<circle cx="{x}" cy="{y}" r="3.4" class="g-tf"/>'
    pts2 = [(264, 302), (284, 300), (304, 303), (324, 301), (344, 302), (364, 300), (384, 303), (404, 301), (424, 302), (440, 301)]
    ic += f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts2)}" class="g-ms" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    for x, y in pts2:
        ic += f'<circle cx="{x}" cy="{y}" r="3.4" class="g-mf"/>'
    ic += _t(119, 334, 'değişkenlik fazla', 13, 'g-tf', kalin=True) + _t(351, 334, 'değişkenlik az', 13, 'g-mf', kalin=True)
    return svg(470, 354, ic, 'Hava olayları ile iklimin karşılaştırılması. Hava olayları sınırlı bir yeri ve kısa bir zamanı kapsar, değişkenlikleri fazladır. '
               'İklim geniş bir bölgeyi ve en az 35 ile 40 yıllık uzun bir süreyi kapsar, değişkenliği azdır.')


def uygula(o):
    g = {'Yağış, sis, çiy ve kırağı': yagis_siniflama(),
         'Basınç alanları ve rüzgâr': basinc_alanlari(),
         'İklim ile hava olayları arasındaki farklar': karsilastirma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
