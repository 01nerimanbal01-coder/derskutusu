"""10. sınıf Felsefe 1. hafta (felsefenin anlamı, özellikleri, gelişimi) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def ok(x1, y1, x2, y2, renk=GRI, kalin=1.8):
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2:.1f},{y2:.1f} {x2 - 7 * math.cos(a - 0.45):.1f},{y2 - 7 * math.sin(a - 0.45):.1f} {x2 - 7 * math.cos(a + 0.45):.1f},{y2 - 7 * math.sin(a + 0.45):.1f}'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/><polygon points="{u}" fill="{renk}"/>'


def yildiz(x, y, r, renk=ALTIN):
    p = ' '.join(f'{x + (r if k % 2 == 0 else r * 0.45) * math.cos(-math.pi / 2 + k * math.pi / 5):.1f},{y + (r if k % 2 == 0 else r * 0.45) * math.sin(-math.pi / 2 + k * math.pi / 5):.1f}' for k in range(10))
    return f'<polygon points="{p}" fill="{renk}"/>'


SU = '#5aa9e6'


def satir_kartlari(kart, etiket, en_fazla):
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 4 + len(kart) * 29, ic, etiket, en_fazla)


def formul():
    ic = kutu(14, 6, 86, 30, MAVI_A, MAVI, 8, 1.4) + yazi(57, 26, 'philia', 13, LAC) + yazi(115, 27, '+', 17, SOLUK)
    ic += kutu(130, 6, 86, 30, MOR_A, MOR, 8, 1.4) + yazi(173, 26, 'sophia', 13, LAC) + yazi(231, 27, '=', 17, SOLUK)
    ic += kutu(246, 6, 104, 30, TUR_A, TUR, 8, 1.4) + yazi(298, 26, 'philosophia', 13, LAC)
    return svg(360, 42, ic, 'philia + sophia = philosophia', 11)


def dusunme_kartlari():
    return satir_kartlari([('A', 'Bulutları görünce çamaşırları içeri alır.', MAVI, MAVI_A), ('B', 'Eski kavanozları boyayıp kalemlik yapar.', TUR, TUR_A),
                           ('C', 'Bir ilanın doğruluğunu farklı kaynaklardan araştırır.', YES, YES_A), ('D', '“Gerçeklik nedir?” sorusunu gerekçeleriyle tartışır.', MOR, MOR_A)],
                          'Kartlar: A Bulutları görünce çamaşırları içeri alır. B Eski kavanozları boyayıp kalemlik yapar. C Bir ilanın doğruluğunu farklı kaynaklardan araştırır. D Gerçeklik nedir sorusunu gerekçeleriyle tartışır.', 33)


def soru_kartlari():
    s = [('I', 'Güzel nedir?'), ('II', 'Su kaç derecede kaynar?'), ('III', 'Varlığın bir amacı var mıdır?'), ('IV', 'Bu şehrin nüfusu kaçtır?')]
    ic = ''
    for k, (no, a) in enumerate(s):
        x, y = 4 + (k % 2) * 180, 4 + (k // 2) * 32
        ic += kutu(x, y, 172, 27, '#fff', MAVI, 8, 1.3) + yazi(x + 16, y + 18, no, 11, MAVI) + yazi(x + 30, y + 18, a, 9.7, LAC, 'start', True)
    return svg(360, 67, ic, 'Sorular: I Güzel nedir? II Su kaç derecede kaynar? III Varlığın bir amacı var mıdır? IV Bu şehrin nüfusu kaçtır?', 17)


def ozellik_kartlari():
    return satir_kartlari([('A', 'Zihnin kendi düşünceleri üzerine yeniden düşünmesi', MOR, MOR_A), ('B', 'Düşünceler arasında çelişki bulunmaması', MAVI, MAVI_A),
                           ('C', 'Önceki filozofların düşüncelerini geliştirerek ilerleme', TUR, TUR_A), ('D', 'Bütün insanlığı ilgilendiren problemleri ele alma', YES, YES_A)],
                          'Kartlar: A Zihnin kendi düşünceleri üzerine yeniden düşünmesi. B Düşünceler arasında çelişki bulunmaması. C Önceki filozofların düşüncelerini geliştirerek ilerleme. D Bütün insanlığı ilgilendiren problemleri ele alma.', 33)


def serit():
    d = [['MÖ 6. yy –', 'MS 2. yy'], ['2 – 15.', 'yüzyıllar'], ['15 – 17.', 'yüzyıllar'], ['18 – 19.', 'yüzyıllar']]
    renk = [MAVI, MOR, TUR, YES]
    ic = ''
    for i, a in enumerate(d):
        x = 4 + i * 89
        ic += f'<rect x="{x}" y="22" width="84" height="8" rx="4" fill="{renk[i]}"/>' + rozet(x + 42, 26, str(i + 1), renk[i], 10) + ''.join(yazi(x + 42, 50 + k * 13, s, 10.5, LAC) for k, s in enumerate(a))
    return svg(360, 70, ic, 'Zaman şeridi: 1 MÖ 6. yüzyıl – MS 2. yüzyıl, 2 2-15. yüzyıllar, 3 15-17. yüzyıllar, 4 18-19. yüzyıllar', 17)


def iki_soru():
    ic = ''
    for i, (a, c, d) in enumerate([('Adalet nedir?', MOR, MOR_A), ('Bu karar adil mi?', CAM, CAM_A)]):
        x = 4 + i * 180
        ic += kutu(x, 4, 172, 34, d, c, 8, 1.3) + rozet(x + 16, 21, str(i + 1), c) + yazi(x + 96, 25.5, a, 12, LAC)
    return svg(360, 42, ic, '1. soru: Adalet nedir? 2. soru: Bu karar adil mi?', 11)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = formul()
    s[2]['gorsel'] = dusunme_kartlari()
    s[3]['gorsel'] = soru_kartlari()
    s[5]['gorsel'] = ozellik_kartlari()
    s[7]['gorsel'] = serit()
    s[9]['gorsel'] = iki_soru()
