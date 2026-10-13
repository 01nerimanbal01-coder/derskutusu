"""8. sınıf Fen Bilimleri, 7. hafta: kalıtım — tek karakter çaprazlamaları, olasılık, cinsiyetin belirlenmesi ve akraba evliliği.

Görseller yalnız özet metnindeki (araclar/ozetler/8-fen-bilimleri-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı:
- Punnett karesi ve olasılık görselleri: turuncu = baskın alel S ve sarı tohum (baskın fenotip); yeşil = çekinik alel s ve yeşil tohum
  (çekinik fenotip).
- Cinsiyet görseli: mavi = anneden gelen eşey kromozomu (yumurta, her zaman X); mor = babadan gelen eşey kromozomu (sperm, X ya da Y).
- Akraba evliliği görseli: mavi = sağlıklı alel A; mor = çekinik hastalık aleli a, onun aktarım okları ve iki kopyasını alan (hasta) çocuk gözü.
- Gri çerçeveli kutular bireyleri, kartları ve sonuç alanlarını gösterir; renk anlamı taşımaz.
Ölçek: yalnız Mendel’in sayımı çubuğu ölçeklidir (uzunluk tohum sayısıyla orantılı, 8023 tohum = 438 birim); diğer çizimler ölçeksiz şemadır.
Okların ucu dolgulu üçgendir (işaretçi kullanılmaz).
"""
import math

from ozet_gorsel import svg


def _t(x, y, metin, boyut, sinif, anchor='middle', kalin=False):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    k = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}"{a} font-size="{boyut:g}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, cizgi, dolgu, w=2.4, bas=10.0):
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


def _kutu(x, y, w, h, dolgu, cizgi, rx=10, sw=1.8):
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx:g}" class="{dolgu}"/>'
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx:g}" class="{cizgi}" stroke-width="{sw:g}"/>')


def _gamet(cx, cy, harf, dolgu, r=16, boyut=16):
    """Gamet: koyu dolgulu daire, içinde alel ya da kromozom harfi."""
    return f'<circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" class="{dolgu}"/>' + _t(cx, cy + boyut * 0.36, harf, boyut, 'g-b', 'middle', True)


def _cip(x, y, harf, dolgu, b=22):
    """Alel/kromozom çipi: küçük koyu kare, içinde beyaz harf."""
    return f'<rect x="{x:g}" y="{y:g}" width="{b:g}" height="{b:g}" rx="5" class="{dolgu}"/>' + _t(x + b / 2, y + b * 0.72, harf, 13, 'g-b', 'middle', True)


# ---------- 1) Ss × Ss çaprazlamasının Punnett karesi ----------
def punnett_karesi():
    ic = _t(98, 30, 'Ss × Ss çaprazlaması', 14, 'g-y', 'middle', True)
    ic += _t(98, 50, 'melez sarı × melez sarı', 12, 'g-s') + _t(98, 68, 'S: sarı, s: yeşil', 12, 'g-s')
    # 2. bitki: gametleri sütun başlarına
    ic += _kutu(190, 8, 152, 44, 'g-z', 'g-c')
    ic += _t(266, 26, '2. bitki', 13, 'g-y', 'middle', True) + _t(266, 44, 'Ss (melez sarı)', 12.5, 'g-s')
    ic += _ok(250, 53, 238.0, 94.7, 'g-c', 'g-s') + _ok(282, 53, 294.0, 94.7, 'g-c', 'g-s')
    ic += _t(312, 80, 'gametler ayrılır', 12, 'g-s', 'start')
    ic += _gamet(233, 112, 'S', 'g-tf') + _gamet(299, 112, 's', 'g-yf')
    # 1. bitki: gametleri satır başlarına
    ic += _kutu(6, 168, 124, 44, 'g-z', 'g-c')
    ic += _t(68, 186, '1. bitki', 13, 'g-y', 'middle', True) + _t(68, 204, 'Ss (melez sarı)', 12.5, 'g-s')
    ic += _ok(130, 182, 155.6, 170.4, 'g-c', 'g-s') + _ok(130, 198, 155.6, 209.6, 'g-c', 'g-s')
    ic += _gamet(172, 163, 'S', 'g-tf') + _gamet(172, 217, 's', 'g-yf')
    # gözler: dolgu rengi fenotipi gösterir
    for x, y, gen, fen, dolgu, cizgi in ((200, 136, 'SS', 'sarı tohum', 'g-ta', 'g-ts'), (266, 136, 'Ss', 'sarı tohum', 'g-ta', 'g-ts'),
                                          (200, 190, 'Ss', 'sarı tohum', 'g-ta', 'g-ts'), (266, 190, 'ss', 'yeşil tohum', 'g-ya', 'g-ys')):
        ic += _kutu(x, y, 66, 54, dolgu, cizgi, rx=6)
        ic += _t(x + 33, y + 25, gen, 16, 'g-y', 'middle', True) + _t(x + 33, y + 44, fen, 11.5, 'g-s')
    # gözleri sayma paneli
    ic += _kutu(346, 100, 120, 162, 'g-z', 'g-c')
    ic += _t(406, 121, 'Gözleri say', 12.5, 'g-y', 'middle', True)
    for y, metin, dolgu, cizgi in ((145, '1 SS', 'g-ta', 'g-ts'), (167, '2 Ss', 'g-ta', 'g-ts'), (189, '1 ss', 'g-ya', 'g-ys')):
        ic += _kutu(366, y - 12, 14, 14, dolgu, cizgi, rx=3, sw=1.5)
        ic += _t(388, y, metin, 14, 'g-y', 'start', True)
    ic += '<line x1="356" y1="203" x2="456" y2="203" class="g-c" stroke-width="1.5" stroke-dasharray="4 4"/>'
    ic += _t(406, 223, 'genotip 1:2:1', 13, 'g-y', 'middle', True) + _t(406, 242, 'fenotip 3:1', 13, 'g-y', 'middle', True)
    ic += _t(406, 256, '(3 sarı, 1 yeşil)', 11.5, 'g-s')
    return svg(470, 272, ic, 'Ss × Ss çaprazlamasının Punnett karesi. Melez sarı iki bitkinin her biri S ve s gametleri üretir; bir bitkinin gametleri '
               'satır, diğerininkiler sütun başlarına yazılır. Dört gözde SS, Ss, Ss ve ss oluşur; SS ve Ss sarı, ss yeşil tohumludur. '
               'Gözler sayılınca genotip oranı 1:2:1, fenotip oranı 3:1 bulunur.')


# ---------- 2) Olasılık her tohum için yeniden başlar; Mendel’in sayımı ----------
def olasilik_yeniden_baslar():
    ic = _t(235, 20, 'Ss × Ss: her tohum için olasılık aynıdır', 14, 'g-y', 'middle', True)
    for i in range(4):
        x0 = 12 + i * 114
        cx = x0 + 53
        ic += _kutu(x0, 34, 106, 128, 'g-z', 'g-c')
        ic += _t(cx, 54, f'{i + 1}. tohum', 13, 'g-y', 'middle', True)
        # olasılık çarkı: dörtte üç sarı, dörtte bir yeşil
        ic += f'<circle cx="{cx}" cy="96" r="26" class="g-tf"/>'
        ic += f'<path d="M{cx} 96 L{cx} 70 A26 26 0 0 0 {cx - 26} 96 Z" class="g-yf"/>'
        ic += _t(cx, 139, '%75 sarı', 12, 'g-tf', 'middle', True) + _t(cx, 155, '%25 yeşil', 12, 'g-yf', 'middle', True)
    ic += _t(235, 184, 'Önceki tohum ne çıkarsa çıksın olasılık değişmez.', 12.5, 'g-y')
    ic += '<line x1="16" y1="198" x2="454" y2="198" class="g-c" stroke-width="1.5" stroke-dasharray="4 5"/>'
    # Mendel’in sayımı: ölçekli çubuk (438 birim = 8023 tohum)
    sari = 438 * 6022 / 8023
    ic += _t(235, 220, 'Mendel’in sayımı: 8023 tohum (ölçekli çubuk)', 13, 'g-y', 'middle', True)
    ic += f'<rect x="16" y="232" width="{sari:.1f}" height="26" class="g-tf"/>'
    ic += f'<rect x="{16 + sari:.1f}" y="232" width="{438 - sari:.1f}" height="26" class="g-yf"/>'
    ic += _t(16 + sari / 2, 250, '6022 sarı', 13, 'g-b', 'middle', True)
    ic += _t(16 + sari + (438 - sari) / 2, 250, '2001 yeşil', 12.5, 'g-b', 'middle', True)
    ic += _t(235, 280, '6022 : 2001 ≈ 3 : 1', 13, 'g-y', 'middle', True)
    ic += _t(235, 298, 'Tohum sayısı arttıkça gözlenen sonuç orana yaklaşır.', 12, 'g-y')
    return svg(470, 308, ic, 'Ss × Ss çaprazlamasında birinci, ikinci, üçüncü ve dördüncü tohum için aynı olasılık çarkı: her tohumun sarı olma '
               'olasılığı yüzde 75, yeşil olma olasılığı yüzde 25; önceki tohumun sonucu bunu değiştirmez. Altta Mendel’in sayımı ölçekli '
               'çubukla: 8023 tohumun 6022’si sarı, 2001’i yeşil; bu yaklaşık 3’e 1’dir.')


# ---------- 3) İnsanda cinsiyetin belirlenmesi ----------
def cinsiyet():
    ic = _kutu(40, 14, 160, 48, 'g-ma', 'g-ms')
    ic += _t(120, 34, 'Anne: XX', 14, 'g-y', 'middle', True) + _t(120, 52, 'bütün yumurtalar X taşır', 11.5, 'g-s')
    ic += _kutu(250, 14, 190, 48, 'g-oa', 'g-os')
    ic += _t(345, 34, 'Baba: XY', 14, 'g-y', 'middle', True) + _t(345, 52, 'spermlerin yarısı X, yarısı Y', 11.5, 'g-s')
    # gametler
    ic += _ok(120, 63, 120, 106, 'g-ms', 'g-mf')
    ic += _ok(320, 63, 297.1, 108.2, 'g-os', 'g-of') + _ok(370, 63, 392.9, 108.2, 'g-os', 'g-of')
    ic += _gamet(120, 126, 'X', 'g-mf', r=18) + _t(146, 130, 'yumurta', 12, 'g-s', 'start')
    ic += _gamet(288, 126, 'X', 'g-of', r=18) + _gamet(402, 126, 'Y', 'g-of', r=18) + _t(345, 130, 'spermler', 12, 'g-s')
    # yumurta her iki birleşime de X verir
    ic += '<path d="M120 145 V232 H215" class="g-ms" stroke-width="2.4" fill="none"/>'
    ic += '<polygon points="226,232 215,226.5 215,237.5" class="g-mf"/>'
    ic += _t(132, 172, 'anneden hep X', 11.5, 'g-s', 'start')
    ic += _ok(288, 146, 288, 184, 'g-os', 'g-of') + _ok(402, 146, 402, 184, 'g-os', 'g-of')
    # olası çocuklar
    ic += _kutu(230, 186, 230, 76, 'g-z', 'g-c')
    ic += '<line x1="345" y1="186" x2="345" y2="262" class="g-c" stroke-width="1.5"/>'
    ic += _cip(262, 194, 'X', 'g-mf') + _cip(292, 194, 'X', 'g-of')
    ic += _t(288, 236, 'XX: kız', 13, 'g-y', 'middle', True) + _t(288, 255, '%50', 14, 'g-y', 'middle', True)
    ic += _cip(376, 194, 'X', 'g-mf') + _cip(406, 194, 'Y', 'g-of')
    ic += _t(402, 236, 'XY: erkek', 13, 'g-y', 'middle', True) + _t(402, 255, '%50', 14, 'g-y', 'middle', True)
    ic += _t(235, 288, 'Cinsiyeti babadan gelen eşey kromozomu belirler.', 12.5, 'g-y', 'middle', True)
    ic += _t(235, 306, 'Her doğumda kız ya da erkek olma olasılığı %50’dir.', 12, 'g-s')
    return svg(470, 316, ic, 'İnsanda cinsiyetin belirlenmesi. Anne XX olduğundan bütün yumurtalar X taşır; baba XY olduğundan spermlerin yarısı X, '
               'yarısı Y taşır. Yumurta X taşıyan spermle birleşirse XX kız, Y taşıyan spermle birleşirse XY erkek çocuk oluşur; her doğumda '
               'ikisinin de olasılığı yüzde 50’dir. Cinsiyeti babadan gelen eşey kromozomu belirler.')


# ---------- 4) Akraba evliliğinde çekinik alelin karşılaşması ----------
def akraba_evliligi():
    ic = _kutu(140, 8, 190, 50, 'g-z', 'g-c')
    ic += _t(235, 27, 'Ortak ata (dede ya da nine)', 12.5, 'g-y', 'middle', True)
    ic += _cip(186, 33, 'A', 'g-mf') + _cip(214, 33, 'a', 'g-of') + _t(244, 49, 'taşıyıcı', 11.5, 'g-s', 'start')
    ic += _ok(190, 59, 128, 90, 'g-os', 'g-of') + _ok(280, 59, 342, 90, 'g-os', 'g-of')
    ic += _t(235, 80, 'a aleli aktarılabilir', 11.5, 'g-s')
    for cx, ad in ((120, 'Kardeş'), (350, 'Kardeş')):
        pass
    for cx, n in ((120, 1), (350, 2)):
        ic += _kutu(cx - 80, 92, 160, 50, 'g-z', 'g-c')
        ic += _t(cx, 111, f'Kardeş {n} (taşıyıcı)', 12.5, 'g-y', 'middle', True)
        ic += _cip(cx - 26, 117, 'A', 'g-mf') + _cip(cx + 4, 117, 'a', 'g-of')
        ic += _ok(cx, 143, cx, 174, 'g-os', 'g-of') + _t(cx + 8, 158, 'a aktarılabilir', 11.5, 'g-s', 'start')
        ic += _kutu(cx - 80, 176, 160, 50, 'g-z', 'g-c')
        ic += _t(cx, 195, f'Kuzen {n} (taşıyıcı)', 12.5, 'g-y', 'middle', True)
        ic += _cip(cx - 26, 201, 'A', 'g-mf') + _cip(cx + 4, 201, 'a', 'g-of')
    # kuzenlerin evliliği: Aa × Aa
    ic += '<path d="M120 227 V254 H350 V227" class="g-c" stroke-width="2" fill="none"/>'
    ic += _t(235, 243, 'akraba evliliği: Aa × Aa', 12.5, 'g-y', 'middle', True)
    ic += _ok(235, 254, 235, 278, 'g-c', 'g-s') + _t(245, 272, 'her çocuk için', 11.5, 'g-s', 'start')
    ic += _kutu(12, 280, 446, 72, 'g-z', 'g-c')
    ic += '<rect x="310" y="281" width="147" height="70" rx="8" class="g-oa"/>'
    ic += '<line x1="161" y1="280" x2="161" y2="352" class="g-c" stroke-width="1.5"/><line x1="309" y1="280" x2="309" y2="352" class="g-c" stroke-width="1.5"/>'
    for cx, h1, h2, yuzde, ad in ((86.5, 'A', 'A', '%25', 'sağlıklı, taşıyıcı değil'), (235, 'A', 'a', '%50', 'sağlıklı, taşıyıcı'),
                                  (383.5, 'a', 'a', '%25', 'hasta')):
        ic += _cip(cx - 26, 288, h1, 'g-mf' if h1 == 'A' else 'g-of') + _cip(cx + 4, 288, h2, 'g-mf' if h2 == 'A' else 'g-of')
        ic += _t(cx, 330, yuzde, 15, 'g-y', 'middle', True) + _t(cx, 346, ad, 11.5, 'g-s')
    return svg(470, 360, ic, 'Akraba evliliğinde çekinik hastalık alelinin karşılaşması. Ortak ata (dede ya da nine) Aa taşıyıcıdır; a aleli iki '
               'çocuğuna, onlardan da kuzenlere aktarılabilir. Taşıyıcı iki kuzen evlenirse Aa × Aa çaprazlaması olur: her çocuk için AA '
               '(sağlıklı, taşıyıcı değil) yüzde 25, Aa (sağlıklı, taşıyıcı) yüzde 50, aa (hasta) yüzde 25 olasılık vardır.')


def uygula(o):
    g = {'Çaprazlama ve Punnett karesi: adım adım': punnett_karesi(),
         'Oranları yorumlamak: olasılık her seferinde yeniden başlar': olasilik_yeniden_baslar(),
         'Aynı kurallar insanda da geçerli: cinsiyet nasıl belirlenir?': cinsiyet(),
         'Akraba evliliği ve genetik sonuçları': akraba_evliligi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
