"""9. sınıf Biyoloji 1. hafta (biyolojinin önemi, dönüm noktaları, bilimin doğası) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def zaman():
    yil = ['1665', '1838', '1865', '1928', '1996', '2012']
    ad = [None, ['Hücre', 'teorisi'], None, None, ['Canlı', 'klonlama'], None]
    ic = f'<line x1="12" y1="34" x2="348" y2="34" stroke="{MAVI}" stroke-width="3" stroke-linecap="round"/>'
    no = 0
    for i, y in enumerate(yil):
        x = 30 + i * 60
        ic += yazi(x, 18, y, 11.5, MAVI)
        if ad[i] is None:
            no += 1
            ic += rozet(x, 34, str(no), TUR, 9) + kutu(x - 24, 50, 48, 24, '#fff', TUR, 6, 1.3, ' stroke-dasharray="4 3"') + yazi(x, 67, '?', 13, TUR)
        else:
            ic += f'<circle cx="{x}" cy="34" r="6" fill="{MAVI}"/>' + ''.join(yazi(x, 60 + k * 13, s, 11, LAC, 'middle', True) for k, s in enumerate(ad[i]))
    x = 14
    for s in ['CRISPR-Cas', 'Kalıtım kuralları', 'Mikroskop', 'Penisilin']:
        w = 5.7 * len(s) + 16
        ic += kutu(x, 90, w, 22, MAVI_A, MAVI, 11, 1.1) + yazi(x + w / 2, 105, s, 11, LAC, 'middle', True)
        x += w + 7
    return svg(360, 116, ic, 'Zaman şeridi: 1665 (1), 1838 hücre teorisi, 1865 (2), 1928 (3), 1996 canlı klonlama, 2012 (4). Dönüm noktaları: CRISPR-Cas, kalıtım kuralları, mikroskop, penisilin', 33)


def defter():
    ic = kutu(4, 4, 352, 88, '#fffdf5', KAHVE, 8, 1.4) + f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{KAHVE}"/><rect x="4" y="16" width="352" height="10" fill="{KAHVE}"/>'
    ic += yazi(16, 20, 'Laboratuvar notu', 11.5, '#fff', 'start')
    for k, s in enumerate(['Örnek: Çok az miktarda DNA var.', 'Sorun: Bu miktar inceleme için yetmiyor.', 'Gereken: Aynı DNA dizisinden çok sayıda kopya']):
        ic += yazi(16, 44 + k * 17, s, 11.5, LAC, 'start', True)
    ic += f'<path d="M318 36 V70 a9 9 0 0 0 18 0 V36" fill="#fff" stroke="{SOLUK}" stroke-width="1.4"/><path d="M319 72 a8 8 0 0 0 16 0 V68 H319 Z" fill="{CAM}"/><line x1="314" y1="36" x2="340" y2="36" stroke="{SOLUK}" stroke-width="1.6" stroke-linecap="round"/>'
    return svg(360, 96, ic, 'Laboratuvar notu. Örnek: Çok az miktarda DNA var. Sorun: Bu miktar inceleme için yetmiyor. Gereken: Aynı DNA dizisinden çok sayıda kopya', 26)


def alan_kartlari():
    kart = [('A', 'Bir gölün suyu ve canlıları koruma altına alınıyor.', CAM, CAM_A),
            ('B', 'Bir hastalık için yeni tedavi yöntemi geliştiriliyor.', KIR, KIR_A),
            ('C', 'Aynı tarladan daha çok ürün elde ediliyor.', TUR, TUR_A),
            ('D', 'Nesli azalan türler için üreme alanı kuruluyor.', YES, YES_A)]
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 120, ic, 'Kartlar: A Bir gölün suyu ve canlıları koruma altına alınıyor. B Bir hastalık için yeni tedavi yöntemi geliştiriliyor. C Aynı tarladan daha çok ürün elde ediliyor. D Nesli azalan türler için üreme alanı kuruluyor.', 33)


def kanun_teori():
    ic = ''
    for i, (renk, acik, soz) in enumerate([(MAVI, MAVI_A, 'NASIL'), (MOR, MOR_A, 'NEDEN')]):
        x = 4 + i * 180
        ic += kutu(x, 4, 172, 62, acik, renk, 8, 1.3) + rozet(x + 16, 19, str(i + 1), renk)
        ic += yazi(x + 86, 24, 'Doğal bir olayın', 11.5, LAC, 'middle', True) + yazi(x + 86, 40, soz, 13, renk) + yazi(x + 86, 56, 'gerçekleştiğini açıklar.', 11.5, LAC, 'middle', True)
    return svg(360, 70, ic, 'Kart 1: Doğal bir olayın nasıl gerçekleştiğini açıklar. Kart 2: Doğal bir olayın neden gerçekleştiğini açıklar.', 19)


def dna():
    ic = ''
    N = 56
    ust = [(60 + k * 240 / N, 30 + 17 * math.sin(k * 2 * math.pi / 18.7)) for k in range(N + 1)]
    alt = [(x, 60 - y) for x, y in ust]
    for k in range(1, N, 3):
        (x, y1), (_, y2) = ust[k], alt[k]
        if abs(y1 - y2) > 8:
            ym = (y1 + y2) / 2
            r = [(MAVI, TUR), (YES, KIR), (TUR, MAVI), (KIR, YES)][(k // 3) % 4]
            ic += f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{ym:.1f}" stroke="{r[0]}" stroke-width="2.4"/><line x1="{x:.1f}" y1="{ym:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{r[1]}" stroke-width="2.4"/>'
    for p, renk in ((ust, LAC), (alt, MOR)):
        ic += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in p)}" fill="none" stroke="{renk}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    return svg(360, 60, ic, 'Çift sarmal yapılı bir molekül çizimi', 14)


def haber():
    ic = kutu(4, 4, 352, 76, '#fff', SOLUK, 8, 1.4) + f'<rect x="4" y="4" width="352" height="18" rx="8" fill="{GRI_A}"/>'
    ic += ''.join(f'<circle cx="{16 + k * 11}" cy="13" r="3" fill="{c}"/>' for k, c in enumerate([KIR, ALTIN, YES]))
    ic += kutu(60, 8, 200, 10, '#fff', GRI, 5, 0.8) + yazi(66, 16.5, 'haber sitesi', 8.5, SOLUK, 'start', True)
    ic += f'<rect x="14" y="30" width="44" height="14" rx="3" fill="{KIR}"/>' + yazi(36, 40.5, 'SAĞLIK', 9, '#fff')
    ic += yazi(14, 60, '“Yeni bir çalışma kanıtladı:', 12, LAC, 'start') + yazi(14, 74, 'Bu besin bütün hastalıkları önlüyor!”', 12, LAC, 'start')
    return svg(360, 84, ic, 'Haber sitesi başlığı: Yeni bir çalışma kanıtladı: Bu besin bütün hastalıkları önlüyor!', 23)


def uzay():
    ic = ''
    ad = [['Aşırı sıcak', 've soğuk'], ['Yüksek enerjili', 'radyasyon'], ['Yer çekimsiz', 'ortam']]
    for i in range(3):
        x0 = 4 + i * 119
        ic += kutu(x0, 4, 114, 92, '#1e2a55', LAC, 8, 1.2) + ''.join(yazi(x0 + 57, 76 + k * 13, s, 11, '#fff') for k, s in enumerate(ad[i]))
    # sıcak–soğuk: termometre + güneş + kar
    ic += f'<rect x="56" y="14" width="8" height="34" rx="4" fill="#fff"/><circle cx="60" cy="50" r="7" fill="#fff"/><rect x="58.5" y="26" width="3" height="22" fill="{KIR}"/><circle cx="60" cy="50" r="4.5" fill="{KIR}"/>'
    ic += f'<circle cx="30" cy="32" r="8" fill="{ALTIN}"/>' + ''.join(f'<line x1="{90 + 9 * math.cos(a):.1f}" y1="{32 + 9 * math.sin(a):.1f}" x2="{90 - 9 * math.cos(a):.1f}" y2="{32 - 9 * math.sin(a):.1f}" stroke="#9ad7ff" stroke-width="1.8" stroke-linecap="round"/>' for a in (0, math.pi / 3, 2 * math.pi / 3))
    # radyasyon: dalgalı ışınlar
    for k in range(3):
        y = 22 + k * 14
        ic += f'<path d="M138 {y} q6 -7 12 0 t12 0 t12 0 t12 0 t12 0" fill="none" stroke="{ALTIN}" stroke-width="1.8"/><polygon points="{206},{y} {198},{y - 4} {198},{y + 4}" fill="{ALTIN}"/>'
    ic += f'<circle cx="218" cy="36" r="7" fill="#7cc3f0"/>'
    # yer çekimsiz: havada duran nesneler
    ic += f'<rect x="262" y="20" width="26" height="6" rx="3" fill="{TUR}" transform="rotate(-25 275 23)"/><circle cx="310" cy="24" r="6" fill="#7cc3f0"/><rect x="322" y="38" width="16" height="12" rx="2" fill="{YES}" transform="rotate(18 330 44)"/><circle cx="280" cy="48" r="4" fill="#7cc3f0"/><circle cx="300" cy="44" r="2.5" fill="#fff"/>'
    return svg(360, 100, ic, 'Uzay ortamının üç koşulu: aşırı sıcak ve soğuk, yüksek enerjili radyasyon, yer çekimsiz ortam', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = zaman()
    s[2]['gorsel'] = defter()
    s[3]['gorsel'] = alan_kartlari()
    s[5]['gorsel'] = kanun_teori()
    s[7]['gorsel'] = dna()
    s[9]['gorsel'] = haber()
    s[11]['gorsel'] = uzay()
