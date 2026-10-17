"""6. sınıf Matematik 4. hafta (deneysel olasılık) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K048); görsel içi yazı sayfa puntosunda (K150 EK); kesirler yalnız dikey (K155: pay üstte, çizgi, payda altta)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM, SARI = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5', '#f5d33b'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=13, renk=LAC, hiza='start', ara=16):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kesir(x, y, pay, payda, boy=11.5, renk=LAC):
    """Dikey kesir: pay üstte, çizgi, payda altta (K155)."""
    w = max(len(pay), len(payda)) * boy * 0.62 + 4
    return (yazi(x, y - 2, pay, boy, renk) + f'<line x1="{x - w / 2:.1f}" y1="{y + 1}" x2="{x + w / 2:.1f}" y2="{y + 1}" stroke="{renk}" stroke-width="1.2"/>'
            + yazi(x, y + boy + 1, payda, boy, renk))


def cark(cx, cy, r, renkler, ok_aci=-50):
    ic = ''
    n = len(renkler)
    for i, c in enumerate(renkler):
        a0, a1 = math.radians(-90 + i * 360 / n), math.radians(-90 + (i + 1) * 360 / n)
        ic += (f'<path d="M{cx} {cy} L{cx + r * math.cos(a0):.1f} {cy + r * math.sin(a0):.1f} A{r} {r} 0 0 1 {cx + r * math.cos(a1):.1f} {cy + r * math.sin(a1):.1f} Z" '
               f'fill="{c}" stroke="#fff" stroke-width="1.5"/>')
    a = math.radians(ok_aci)
    ic += (f'<line x1="{cx - 0.5 * r * math.cos(a):.1f}" y1="{cy - 0.5 * r * math.sin(a):.1f}" x2="{cx + 0.8 * r * math.cos(a):.1f}" y2="{cy + 0.8 * r * math.sin(a):.1f}" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/>'
           f'<circle cx="{cx}" cy="{cy}" r="4" fill="{LAC}"/>')
    return ic


def cark_torba():
    """Dört renkli çark ve 1-4 kartlı torba."""
    ic = cark(70, 48, 38, [KIR, MAVI, YES, SARI]) + yazi(70, 100, 'çark', 12.5)
    ic += f'<path d="M210 40 q-24 10 -24 36 v16 a6 6 0 0 0 6 6 h92 a6 6 0 0 0 6 -6 v-16 q0 -26 -24 -36 z" fill="#c9a06b" stroke="{KAHVE}" stroke-width="1.5"/>'
    ic += f'<path d="M210 40 q0 -8 10 -10 h38 q10 2 10 10" fill="none" stroke="{KAHVE}" stroke-width="1.5"/>'
    for i, (x, a) in enumerate([(216, -12), (236, -4), (256, 4), (276, 12)]):
        ic += f'<g transform="rotate({a} {x + 10} 40)"><rect x="{x}" y="14" width="20" height="26" rx="3" fill="#fff" stroke="{LAC}" stroke-width="1.2"/>' + yazi(x + 10, 32, str(i + 1), 12) + '</g>'
    ic += yazi(246, 100, 'torba', 12.5) + yazi(246, 84, 'kartlar: 1, 2, 3, 4', 11, '#fff')
    return svg(360, 106, ic, 'Solda kırmızı, mavi, yeşil ve sarı dilimli bir çark ve oku. Sağda 1, 2, 3, 4 kartlarının bulunduğu torba.', 27)


def spektrum():
    """Olasılık spektrumu: 0 imkânsız, ortada 1/2, 1 kesin; A, B, C, D noktaları."""
    x0, x1, y = 36, 324, 52
    ic = f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LAC}" stroke-width="2.5"/>'
    for x, alt in [(x0, '0'), ((x0 + x1) / 2, None), (x1, '1')]:
        ic += f'<line x1="{x:.1f}" y1="{y - 7}" x2="{x:.1f}" y2="{y + 7}" stroke="{LAC}" stroke-width="2"/>'
        ic += yazi(x, y + 24, alt, 13) if alt else kesir(x, y + 22, '1', '2', 11.5)
    ic += yazi(x0, y + 40, 'imkânsız', 11.5, SOLUK) + yazi(x1, y + 40, 'kesin', 11.5, SOLUK)
    for h, t in [('A', 0.12), ('B', 0.5), ('C', 0.85), ('D', 1.0)]:
        x = x0 + (x1 - x0) * t
        ic += f'<circle cx="{x:.1f}" cy="{y}" r="6" fill="{TUR}" stroke="#fff" stroke-width="1.5"/>' + yazi(x, y - 14, h, 12.5, TUR)
    return svg(360, 100, ic, 'Olasılık spektrumu: sol uçta 0 imkânsız, ortada bir bölü iki, sağ uçta 1 kesin. Turuncu noktalar: A sıfıra yakın, B tam ortada, C bire yakın, D 1 noktasında.', 25)


def cetele():
    """Dört renkli çarkın çetele tablosu: kırmızı 12, mavi 8, sarı 5, mor 15."""
    veri = [('kırmızı', 12, KIR), ('mavi', 8, MAVI), ('sarı', 5, '#d4b000'), ('mor', 15, MOR)]
    ic = kutu(4, 4, 352, 120, '#fff', GRI, 6, 1.2) + f'<rect x="4" y="4" width="352" height="24" rx="6" fill="{MAVI_A}"/><rect x="4" y="18" width="352" height="10" fill="{MAVI_A}"/>'
    ic += yazi(50, 21, 'Renk', 12, LAC) + yazi(220, 21, 'Çetele', 12, LAC) + f'<line x1="96" y1="4" x2="96" y2="124" stroke="{GRI}" stroke-width="1"/>'
    for i, (ad, n, renk) in enumerate(veri):
        y = 46 + i * 24
        ic += f'<line x1="4" y1="{y + 12}" x2="356" y2="{y + 12}" stroke="{GRI_A}" stroke-width="1"/>' + yazi(50, y + 4, ad, 12.5, renk)
        x = 112
        for g in range(n // 5):
            ic += ''.join(f'<line x1="{x + k * 6}" y1="{y - 8}" x2="{x + k * 6}" y2="{y + 8}" stroke="{LAC}" stroke-width="1.8" stroke-linecap="round"/>' for k in range(4))
            ic += f'<line x1="{x - 3}" y1="{y + 7}" x2="{x + 21}" y2="{y - 7}" stroke="{LAC}" stroke-width="1.8" stroke-linecap="round"/>'
            x += 34
        ic += ''.join(f'<line x1="{x + k * 6}" y1="{y - 8}" x2="{x + k * 6}" y2="{y + 8}" stroke="{LAC}" stroke-width="1.8" stroke-linecap="round"/>' for k in range(n % 5))
    return svg(360, 128, ic, 'Çetele tablosu. Kırmızı: beşli iki grup ve iki çizgi, 12. Mavi: beşli bir grup ve üç çizgi, 8. Sarı: beşli bir grup, 5. Mor: beşli üç grup, 15.', 32)


def kup_karti():
    """Kayıt kartı: sayı küpü 25 atış, 3 sayısı 7 kez."""
    ic = kutu(40, 6, 280, 76, KUM, GRI, 8, 1.2) + f'<rect x="40" y="6" width="280" height="22" rx="8" fill="{LAC}"/><rect x="40" y="18" width="280" height="10" fill="{LAC}"/>'
    ic += yazi(180, 21.5, 'KAYIT KARTI · sayı küpü', 12, '#fff')
    ic += yazi(56, 50, 'Atış sayısı:', 12.5, SOLUK, 'start') + yazi(150, 50, '25', 13.5, LAC, 'start')
    ic += yazi(56, 72, '3 gelme sayısı:', 12.5, SOLUK, 'start')
    x = 172
    ic += ''.join(f'<line x1="{x + k * 6}" y1="63" x2="{x + k * 6}" y2="77" stroke="{LAC}" stroke-width="1.8" stroke-linecap="round"/>' for k in range(4))
    ic += f'<line x1="{x - 3}" y1="76" x2="{x + 21}" y2="64" stroke="{LAC}" stroke-width="1.8" stroke-linecap="round"/>'
    ic += ''.join(f'<line x1="{x + 34 + k * 6}" y1="63" x2="{x + 34 + k * 6}" y2="77" stroke="{LAC}" stroke-width="1.8" stroke-linecap="round"/>' for k in range(2))
    ic += yazi(236, 72, '(7)', 13, KIR, 'start')
    # küp simgesi
    ic += f'<rect x="268" y="40" width="30" height="30" rx="5" fill="#fff" stroke="{LAC}" stroke-width="1.4"/>' + ''.join(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="{LAC}"/>' for cx, cy in [(276, 48), (283, 55), (290, 62)])
    return svg(360, 88, ic, 'Kayıt kartı, sayı küpü. Atış sayısı 25. 3 gelme sayısı: çetele ile 7. Yanda üç noktalı küp yüzü.', 22)


def sutun_grafik():
    """Sayı küpü 40 atış: 1:6, 2:8, 3:5, 4:9, 5:7, 6:5."""
    veri = [6, 8, 5, 9, 7, 5]
    tx, ty, h = 40, 104, 76
    ic = yazi(190, 14, 'Sayı küpü · 40 atış · sıklıklar', 12.5)
    ic += f'<line x1="{tx}" y1="{ty - h - 4}" x2="{tx}" y2="{ty}" stroke="{SOLUK}" stroke-width="1.2"/><line x1="{tx}" y1="{ty}" x2="348" y2="{ty}" stroke="{SOLUK}" stroke-width="1.2"/>'
    for v in (0, 2, 4, 6, 8, 10):
        y = ty - v * h / 10
        ic += f'<line x1="{tx - 3}" y1="{y:.1f}" x2="348" y2="{y:.1f}" stroke="{GRI_A}" stroke-width="1"/>' + yazi(tx - 7, y + 4, str(v), 11, SOLUK, 'end')
    for i, n in enumerate(veri):
        x = tx + 14 + i * 50
        yuk = n * h / 10
        ic += f'<rect x="{x}" y="{ty - yuk:.1f}" width="30" height="{yuk:.1f}" rx="3" fill="{[MAVI, YES, TUR, MOR, CAM, KIR][i]}"/>'
        ic += yazi(x + 15, ty + 16, str(i + 1), 12.5)
    ic += yazi(190, ty + 32, 'üst yüze gelen sayı', 11.5, SOLUK)
    return svg(360, 140, ic, 'Sütun grafiği, sayı küpü 40 atış. Sıklıklar: 1 için 6, 2 için 8, 3 için 5, 4 için 9, 5 için 7, 6 için 5. Dikey eksen 0’dan 10’a ikişer.', 35)


def skor():
    """Ayşe ve Can'ın atış kartları."""
    ic = ''
    for i, (ad, atis, isabet, renk, zemin) in enumerate([('Ayşe', 40, 30, MAVI, MAVI_A), ('Can', 50, 35, YES, YES_A)]):
        x = 6 + i * 178
        ic += kutu(x, 4, 170, 80, zemin, renk, 8, 1.4) + yazi(x + 85, 24, ad, 13.5, renk)
        ic += yazi(x + 14, 48, 'Atış sayısı:', 12, SOLUK, 'start') + yazi(x + 110, 48, str(atis), 13, LAC, 'start')
        ic += yazi(x + 14, 70, 'İsabet sayısı:', 12, SOLUK, 'start') + yazi(x + 110, 70, str(isabet), 13, LAC, 'start')
        cx, cy = x + 148, 56
        ic += ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>' for r, c in [(14, KIR), (9.5, '#fff'), (5, KIR)])
    return svg(360, 90, ic, 'İki kart. Ayşe: atış sayısı 40, isabet sayısı 30. Can: atış sayısı 50, isabet sayısı 35. Her kartta hedef simgesi.', 22)


def torba():
    """Torba: kırmızı ve mavi toplar; not kartı: 60 çekiliş, kırmızı 0,35."""
    ic = f'<path d="M40 44 q-28 12 -28 42 v18 a7 7 0 0 0 7 7 h98 a7 7 0 0 0 7 -7 v-18 q0 -30 -28 -42 z" fill="#c9a06b" stroke="{KAHVE}" stroke-width="1.5"/>'
    ic += f'<path d="M40 44 q0 -9 12 -11 h32 q12 2 12 11" fill="none" stroke="{KAHVE}" stroke-width="1.5"/>'
    toplar = [(44, 92, KIR), (60, 84, MAVI), (76, 94, MAVI), (92, 86, KIR), (108, 94, MAVI), (52, 70, MAVI), (84, 70, KIR), (68, 58, MAVI)]
    ic += ''.join(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{c}" stroke="#fff" stroke-width="1"/>' for cx, cy, c in toplar)
    ic += kutu(160, 14, 194, 84, KUM, GRI, 6, 1.2) + f'<rect x="200" y="8" width="114" height="12" rx="2" fill="{GRI}" opacity=".5"/>'
    ic += duz(172, 40, ['Çekiliş sayısı: 60', 'Top her seferinde geri kondu.', 'Kırmızı gelme olayının', 'deneysel olasılığı: 0,35'], 12, LAC, 'start', 16)
    return svg(360, 118, ic, 'Kırmızı ve mavi topların bulunduğu torba. Not kartı: Çekiliş sayısı 60. Top her seferinde geri kondu. Kırmızı gelme olayının deneysel olasılığı 0,35.', 30)


def tahmin():
    """Deniz'in tahmini (1/2) ve deney sonucu: 4 kırmızı 4 mavi boncuk; 50 çekilişte 23 mavi."""
    x0, x1, y = 24, 200, 40
    ic = f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LAC}" stroke-width="2.5"/>'
    for x, alt in [(x0, '0'), ((x0 + x1) / 2, None), (x1, '1')]:
        ic += f'<line x1="{x:.1f}" y1="{y - 6}" x2="{x:.1f}" y2="{y + 6}" stroke="{LAC}" stroke-width="2"/>'
        ic += yazi(x, y + 22, alt, 12.5) if alt else kesir(x, y + 20, '1', '2', 11)
    xm = (x0 + x1) / 2
    ic += f'<circle cx="{xm}" cy="{y}" r="6" fill="{TUR}" stroke="#fff" stroke-width="1.5"/>' + yazi(xm, y - 14, 'Deniz’in tahmini: mavi', 11.5, TUR)
    ic += yazi(112, 84, 'kavanoz: 4 kırmızı, 4 mavi', 11.5, SOLUK)
    ic += ''.join(f'<circle cx="{40 + k * 18}" cy="100" r="6.5" fill="{KIR if k < 4 else MAVI}"/>' for k in range(8))
    ic += kutu(222, 10, 132, 96, YES_A, YES, 8, 1.4) + yazi(288, 32, 'Deney sonucu', 12.5, YES)
    ic += duz(234, 56, ['Çekiliş: 50', 'Mavi: 23 kez', 'Kırmızı: 27 kez'], 12.5, LAC, 'start', 20)
    return svg(360, 112, ic, 'Solda olasılık spektrumu; tam ortada bir bölü iki noktasında Deniz’in tahmini: mavi. Altında kavanoz: 4 kırmızı, 4 mavi boncuk. Sağda deney sonucu kartı: Çekiliş 50, mavi 23 kez, kırmızı 27 kez.', 29)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = cark_torba()
    s[1]['gorsel'] = spektrum()
    s[2]['gorsel'] = cetele()
    s[3]['gorsel'] = kup_karti()
    s[4]['gorsel'] = sutun_grafik()
    s[6]['gorsel'] = skor()
    s[7]['gorsel'] = torba()
    s[9]['gorsel'] = tahmin()
