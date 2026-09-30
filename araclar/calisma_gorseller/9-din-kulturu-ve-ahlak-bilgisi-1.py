"""9. sınıf Din Kültürü ve Ahlak Bilgisi 1. hafta (insan ve insanın yaratılışı) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def ayet_karti():
    """Enbiya 21/16 meali: gökyüzü ve yeryüzü simgeleriyle."""
    ic = kutu(4, 4, 352, 116, '#fbf7ee', '#c9a86a', 10, 1.6)
    ic += f'<rect x="14" y="14" width="332" height="44" rx="6" fill="#1e2a55"/>' + ''.join(yildiz(x, y, r, '#fff' if r < 4 else ALTIN) for x, y, r in [(40, 30, 5), (90, 44, 3), (150, 26, 3), (220, 40, 3), (300, 28, 5), (330, 46, 3)])
    ic += f'<circle cx="260" cy="36" r="9" fill="{ALTIN}"/><circle cx="264" cy="33" r="8" fill="#1e2a55"/>'
    ic += f'<path d="M14 58 Q90 44 170 56 T346 54 V58 Z" fill="#7fd08f"/>'
    ic += yazi(180, 80, '“Biz gökleri, yeri ve bunlar arasındakileri', 12.5, LAC, 'middle', True)
    ic += yazi(180, 97, 'oyun olsun diye yaratmadık.”', 12.5, LAC, 'middle', True) + yazi(180, 113, '(Enbiya 21/16)', 10.5, SOLUK)
    return svg(360, 124, ic, 'Ayet kartı: Biz gökleri, yeri ve bunlar arasındakileri oyun olsun diye yaratmadık. (Enbiya 21/16)', 26)


def duzen_simgeleri():
    ic = ''
    renk = [MOR, MAVI, YES, CAM]
    acik = [MOR_A, MAVI_A, YES_A, CAM_A]
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 80, acik[i], renk[i], 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), renk[i])
    # 1 yörüngeler
    cx, cy = 50, 48
    ic += ''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * 0.55:.1f}" fill="none" stroke="{MOR}" stroke-width="0.9" opacity="0.7"/>' for r in (16, 26, 34))
    ic += f'<circle cx="{cx}" cy="{cy}" r="7" fill="{ALTIN}"/><circle cx="{cx + 16}" cy="{cy}" r="3" fill="{MAVI}"/><circle cx="{cx - 20}" cy="{cy - 10}" r="3.6" fill="{KIR}"/><circle cx="{cx + 28}" cy="{cy - 11}" r="4" fill="{TUR}"/>'
    # 2 gece-gündüz
    cx = 139
    ic += f'<path d="M{cx - 26} 48 a26 26 0 0 1 52 0 z" fill="#ffe9a8"/><path d="M{cx - 26} 48 a26 26 0 0 0 52 0 z" fill="#1e2a55"/>'
    ic += f'<circle cx="{cx}" cy="36" r="7" fill="{ALTIN}"/><circle cx="{cx - 4}" cy="60" r="6" fill="#fff"/><circle cx="{cx - 1}" cy="58" r="5.5" fill="#1e2a55"/>' + yildiz(cx + 12, 62, 3, '#fff')
    # 3 canlı: bitki, güneş, yağmur
    cx = 228
    ic += f'<rect x="{cx - 26}" y="66" width="52" height="8" rx="3" fill="#d9b98f"/><path d="M{cx} 66 V46" stroke="{YES}" stroke-width="2.2"/>'
    ic += f'<path d="M{cx} 54 q-12 -2 -14 -12 q11 1 14 12 M{cx} 58 q12 -2 14 -12 q-11 1 -14 12" fill="{YES}"/>'
    ic += f'<circle cx="{cx + 24}" cy="30" r="6" fill="{ALTIN}"/>' + ''.join(f'<line x1="{cx - 26 + k * 6}" y1="{28 + (k % 2) * 4}" x2="{cx - 28 + k * 6}" y2="{34 + (k % 2) * 4}" stroke="#5aa9e6" stroke-width="1.6" stroke-linecap="round"/>' for k in range(3))
    # 4 atom
    cx, cy = 317, 46
    ic += ''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="26" ry="9" fill="none" stroke="{CAM}" stroke-width="1.4" transform="rotate({a} {cx} {cy})"/>' for a in (0, 60, 120))
    ic += f'<circle cx="{cx}" cy="{cy}" r="5" fill="{KIR}"/><circle cx="{cx + 26}" cy="{cy}" r="2.6" fill="{MAVI}"/><circle cx="{cx - 13}" cy="{cy - 22}" r="2.6" fill="{MAVI}"/>'
    return svg(360, 88, ic, 'Simgeler: 1 Güneş çevresinde yörüngelerde dönen gök cisimleri, 2 yarısı gündüz yarısı gece olan gökyüzü, 3 güneş ve yağmurla büyüyen bitki, 4 atom', 22)


def zincir():
    """Yaratılış aşamaları: 2, 4 ve 6 boş."""
    asama = [['Çamurdan', 'süzülmüş', 'öz'], None, ['Alaka'], None, ['Kemikler'], None, ['Başka bir', 'yaratışla', 'insan']]
    ic = ''
    for i, a in enumerate(asama):
        satir, sira = divmod(i, 4)
        x = 6 + sira * 90 if satir == 0 else 51 + sira * 90
        y = 8 + satir * 62
        bos = a is None
        ic += kutu(x, y, 76, 44, '#fff' if bos else TUR_A, TUR, 8, 1.4, ' stroke-dasharray="4 3"' if bos else '')
        ic += rozet(x, y, str(i + 1), TUR, 8)
        if bos:
            ic += yazi(x + 38, y + 28, '?', 15, TUR)
        else:
            ic += ''.join(yazi(x + 38, y + 26 + (k - (len(a) - 1) / 2) * 12, s, 10.5, LAC) for k, s in enumerate(a))
        if i < 6 and i != 3:
            ic += ok(x + 77, y + 22, x + 89, y + 22)
    ic += f'<path d="M318 52 V60 Q318 64 314 64 H92 Q88 64 88 68 V68" fill="none" stroke="{GRI}" stroke-width="1.8"/>' + ok(88, 64, 88, 71)
    return svg(360, 120, ic, 'Yaratılış aşamaları: 1 çamurdan süzülmüş öz, 2 boş, 3 alaka, 4 boş, 5 kemikler, 6 boş, 7 başka bir yaratışla insan', 30)


def durum_kartlari():
    kart = [('A', 'Ece, kitap okuyarak yeni bir konu öğreniyor.', MAVI, MAVI_A),
            ('B', 'Can, iki kulüpten hangisine gireceğini düşünüp seçiyor.', MOR, MOR_A),
            ('C', 'Kasabaya okul, hastane ve yeni yollar yapılıyor.', TUR, TUR_A),
            ('D', 'Deniz, bayramda akrabalarını ziyaret ediyor.', YES, YES_A)]
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 31
        ic += kutu(4, y, 352, 27, d, c, 8, 1.3) + rozet(21, y + 13.5, h, c) + yazi(38, y + 18, s, 11.5, LAC, 'start', True)
    return svg(360, 128, ic, 'Kartlar: A Ece, kitap okuyarak yeni bir konu öğreniyor. B Can, iki kulüpten hangisine gireceğini düşünüp seçiyor. C Kasabaya okul, hastane ve yeni yollar yapılıyor. D Deniz, bayramda akrabalarını ziyaret ediyor.', 29)


def isim_kartlari():
    ic = kutu(4, 4, 172, 84, MAVI_A, MAVI, 8, 1.2) + kutu(184, 4, 172, 84, MOR_A, MOR, 8, 1.2)
    ic += yazi(90, 22, 'Maddi varlıklar', 11.5, MAVI) + yazi(270, 22, 'Manevi kavramlar', 11.5, MOR)
    for k, s in enumerate(['su', 'dağ', 'ağaç', 'yıldız']):
        x, y = 16 + (k % 2) * 80, 32 + (k // 2) * 26
        ic += kutu(x, y, 68, 20, '#fff', MAVI, 5, 1) + yazi(x + 34, y + 14, s, 11.5, LAC, 'middle', True)
    for k, s in enumerate(['adalet', 'sabır', 'sevgi', 'dostluk']):
        x, y = 196 + (k % 2) * 80, 32 + (k // 2) * 26
        ic += kutu(x, y, 68, 20, '#fff', MOR, 5, 1) + yazi(x + 34, y + 14, s, 11.5, LAC, 'middle', True)
    return svg(360, 92, ic, 'İsim kartları. Maddi varlıklar: su, dağ, ağaç, yıldız. Manevi kavramlar: adalet, sabır, sevgi, dostluk', 21)


def emanet():
    ic = ''
    ad = ['Gökler', 'Yer', 'Dağlar']
    for i in range(3):
        x0 = 4 + i * 119
        ic += kutu(x0, 4, 114, 84, [MAVI_A, YES_A, GRI_A][i], [MAVI, YES, SOLUK][i], 8, 1.2) + yazi(x0 + 57, 80, ad[i], 12, LAC)
    ic += f'<rect x="14" y="14" width="94" height="48" rx="6" fill="#1e2a55"/>' + ''.join(yildiz(x, y, r, '#fff') for x, y, r in [(30, 28, 4), (60, 22, 3), (88, 34, 4), (44, 48, 3), (76, 52, 3)])
    ic += f'<circle cx="180" cy="40" r="24" fill="#7cc3f0"/><path d="M162 30 q10 -6 18 2 q6 8 16 2 M166 52 q8 -8 18 -2 q8 4 12 -2" fill="{YES}" stroke="{YES}" stroke-width="3"/>'
    ic += f'<path d="M248 66 L272 24 L290 50 L302 34 L324 66 Z" fill="#8c97ab"/><path d="M264 38 L272 24 L280 36 L274 34 Z" fill="#fff"/><path d="M298 40 L302 34 L307 41 Z" fill="#fff"/>'
    return svg(360, 92, ic, 'Emaneti yüklenmekten çekinen varlıklar: gökler, yer, dağlar', 20)


def sorumluluk():
    alan = [('Kendisine', MAVI, MAVI_A, 8, 8), ('Ailesine', YES, YES_A, 232, 8), ('Topluma', TUR, TUR_A, 8, 66), ('Allah’a (cc)', MOR, MOR_A, 232, 66)]
    ic = ''
    for a, c, d, x, y in alan:
        ic += f'<line x1="180" y1="55" x2="{x + 60}" y2="{y + 18}" stroke="{GRI}" stroke-width="1.6"/>'
    for a, c, d, x, y in alan:
        ic += kutu(x, y, 120, 36, d, c, 18, 1.5) + yazi(x + 60, y + 23, a, 12.5, LAC)
    ic += f'<circle cx="180" cy="55" r="39" fill="{LAC}"/>' + yazi(180, 51, 'Sorumluluk', 10.5, '#fff') + yazi(180, 65, 'bilinci', 10.5, '#fff')
    return svg(360, 110, ic, 'Sorumluluk bilinci: kendisine, ailesine, topluma ve Allah’a (cc) karşı', 23)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ayet_karti()
    s[2]['gorsel'] = duzen_simgeleri()
    s[4]['gorsel'] = zincir()
    s[6]['gorsel'] = durum_kartlari()
    s[7]['gorsel'] = isim_kartlari()
    s[8]['gorsel'] = emanet()
    s[10]['gorsel'] = sorumluluk()
