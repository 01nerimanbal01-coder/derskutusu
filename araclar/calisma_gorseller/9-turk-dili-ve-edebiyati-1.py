"""9. sınıf Türk Dili ve Edebiyatı 1. hafta (şiir ve deneme okuma) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def sanat_simgeleri():
    ad = ['Resim', 'Müzik', 'Tiyatro', 'Edebiyat']
    ic = ''
    for i, a in enumerate(ad):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 80, '#fff', GRI, 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), LAC) + yazi(x0 + 42, 75, a, 11, LAC)
    c = [4 + i * 89 + 42 for i in range(4)]
    # 1 palet
    ic += f'<path d="M{c[0] - 20} 40 a20 16 0 1 1 22 16 q-6 0 -5 -6 q1 -6 -7 -4 q-10 2 -10 -6 Z" fill="#e6b877" stroke="{KAHVE}" stroke-width="1.2"/>' + ''.join(f'<circle cx="{c[0] + dx}" cy="{dy}" r="3.4" fill="{r}"/>' for dx, dy, r in [(-8, 32, KIR), (2, 28, ALTIN), (12, 33, MAVI), (14, 44, YES)])
    # 2 nota
    ic += f'<path d="M{c[1] - 8} 52 V28 l20 -5 V47" fill="none" stroke="{MOR}" stroke-width="2.4"/><ellipse cx="{c[1] - 12}" cy="52" rx="5.5" ry="4" fill="{MOR}"/><ellipse cx="{c[1] + 8}" cy="47" rx="5.5" ry="4" fill="{MOR}"/>'
    # 3 sahne perdesi
    ic += f'<rect x="{c[2] - 24}" y="24" width="48" height="34" fill="#fff" stroke="{KAHVE}" stroke-width="1.2"/><path d="M{c[2] - 24} 24 h16 q0 22 -16 34 Z" fill="{KIR}"/><path d="M{c[2] + 24} 24 h-16 q0 22 16 34 Z" fill="{KIR}"/><rect x="{c[2] - 26}" y="20" width="52" height="6" rx="2" fill="{KAHVE}"/><rect x="{c[2] - 26}" y="58" width="52" height="4" fill="{KAHVE}"/>'
    # 4 açık kitap
    ic += f'<path d="M{c[3]} 30 q-12 -8 -24 -2 v26 q12 -6 24 2 q12 -8 24 -2 v-26 q-12 -6 -24 2 Z" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/><line x1="{c[3]}" y1="30" x2="{c[3]}" y2="56" stroke="{MAVI}" stroke-width="1.4"/>' + ''.join(f'<line x1="{c[3] + s * 5}" y1="{36 + k * 5}" x2="{c[3] + s * 19}" y2="{34 + k * 5}" stroke="{GRI}" stroke-width="1"/>' for s in (-1, 1) for k in range(3))
    return svg(360, 88, ic, 'Sanat dalları: 1 resim, 2 müzik, 3 tiyatro, 4 edebiyat', 22)


def siir_kartlari():
    s = ['Sülüs yazı', 'İnce mozaik', 'Zeybeğin diz vuruşu', 'Orkestra sesleri', 'Yeşil çini', 'Kelebeğin raksı']
    ic = ''
    for k, a in enumerate(s):
        x, y = 4 + (k % 3) * 119, 4 + (k // 3) * 30
        ic += kutu(x, y, 114, 25, MOR_A, MOR, 12, 1.2) + yazi(x + 57, y + 16.5, a, 10.2, LAC, 'middle', True)
    return svg(360, 63, ic, 'Kartlar: sülüs yazı, ince mozaik, zeybeğin diz vuruşu, orkestra sesleri, yeşil çini, kelebeğin raksı', 17)


def sozluk():
    ic = kutu(4, 4, 352, 66, '#fffdf5', KAHVE, 8, 1.4) + yazi(16, 24, 'kanaat', 13.5, LAC, 'start') + yazi(72, 24, 'isim', 10.5, SOLUK, 'start', True)
    anlam = ['1. Elindekinden hoşnut olma', '2. Yetinme', '3. Birine duyulan güven', '4. Görüş']
    for k, a in enumerate(anlam):
        ic += yazi(16 + (k % 2) * 190, 43 + (k // 2) * 17, a, 11.5, LAC, 'start', True)
    return svg(360, 74, ic, 'Sözlük kartı: kanaat. 1. Elindekinden hoşnut olma 2. Yetinme 3. Birine duyulan güven 4. Görüş', 18)


def dize():
    ic = kutu(4, 4, 352, 50, MAVI_A, MAVI, 8, 1.3) + yazi(180, 26, '“Bir yanda akan benim, öbür yanda Sakarya”', 12.5, LAC) + yazi(180, 44, 'Necip Fazıl Kısakürek, Sakarya Türküsü', 10, SOLUK, 'middle', True)
    return svg(360, 58, ic, 'Dize: Bir yanda akan benim, öbür yanda Sakarya (Necip Fazıl Kısakürek, Sakarya Türküsü)', 14)


def okuma_kartlari():
    return satir_kartlari([('A', 'Metnin söz varlığını incelemek', YES, YES_A), ('B', 'Başlıktan ve görsellerden içeriği tahmin etmek', MAVI, MAVI_A), ('C', 'Vurgu ve tonlamaya dikkat ederek okumak', TUR, TUR_A)],
                          'Kartlar: A Metnin söz varlığını incelemek. B Başlıktan ve görsellerden içeriği tahmin etmek. C Vurgu ve tonlamaya dikkat ederek okumak.', 25)


def metinler():
    m = [['Çay, ılıman ve yağışlı', 'iklimde yetişir. Yaprakları', 'yılda birkaç kez toplanır.'], ['Çay bahçeleri sabah sisinde', 'yeşil bir denize dönmüş,', 'yapraklar yeni uyanıyordu.']]
    ic = ''
    for i, (c, d) in enumerate([(CAM, CAM_A), (TUR, TUR_A)]):
        x = 4 + i * 180
        ic += kutu(x, 4, 172, 78, d, c, 8, 1.3) + f'<rect x="{x}" y="4" width="172" height="20" rx="8" fill="{c}"/><rect x="{x}" y="14" width="172" height="10" fill="{c}"/>' + yazi(x + 86, 18.5, f'{i + 1}. metin', 11, '#fff')
        ic += ''.join(yazi(x + 10, 41 + k * 15, s, 10.3, LAC, 'start', True) for k, s in enumerate(m[i]))
    return svg(360, 86, ic, '1. metin: Çay, ılıman ve yağışlı iklimde yetişir. Yaprakları yılda birkaç kez toplanır. 2. metin: Çay bahçeleri sabah sisinde yeşil bir denize dönmüş, yapraklar yeni uyanıyordu.', 21)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sanat_simgeleri()
    s[2]['gorsel'] = siir_kartlari()
    s[3]['gorsel'] = sozluk()
    s[5]['gorsel'] = dize()
    s[7]['gorsel'] = okuma_kartlari()
    s[9]['gorsel'] = metinler()
