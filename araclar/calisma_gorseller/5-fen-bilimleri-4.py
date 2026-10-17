"""5. sınıf Fen Bilimleri 4. hafta (Ay) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""
import math
import random

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
G_DIS, G_ORTA = '#ffc93c', '#f7a21b'
AY, AY_K, AY_C = '#d7dae1', '#8e95a3', '#9aa0ad'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk=LAC, r=11, boy=13):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{renk}"/>' + yazi(x, y + boy * 0.35, metin, boy, '#fff')


def ok(x1, y1, x2, y2, renk, kesik=False, kal=2.4, uc=9):
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - uc * math.cos(a), y2 - uc * math.sin(a)
    k = ' stroke-dasharray="6 5"' if kesik else ''
    s = f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{renk}" stroke-width="{kal}"{k}/>'
    p1 = (bx + uc * 0.55 * math.sin(a), by - uc * 0.55 * math.cos(a))
    p2 = (bx - uc * 0.55 * math.sin(a), by + uc * 0.55 * math.cos(a))
    return s + f'<path d="M{x2:.1f} {y2:.1f} L{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f} Z" fill="{renk}"/>'


def ok_ucu(x, y, dx, dy, renk, uc=10):
    n = math.hypot(dx, dy)
    dx, dy = dx / n, dy / n
    bx, by = x - uc * dx, y - uc * dy
    return (f'<path d="M{x + dx * 2:.1f} {y + dy * 2:.1f} L{bx - uc * 0.55 * dy:.1f} {by + uc * 0.55 * dx:.1f} '
            f'L{bx + uc * 0.55 * dy:.1f} {by - uc * 0.55 * dx:.1f} Z" fill="{renk}"/>')


def gunes(cx, cy, r, isin=True):
    s = ''
    if isin:
        for k in range(12):
            a = k * math.pi / 6
            s += (f'<line x1="{cx + (r + 4) * math.cos(a):.1f}" y1="{cy + (r + 4) * math.sin(a):.1f}" '
                  f'x2="{cx + (r + 11) * math.cos(a):.1f}" y2="{cy + (r + 11) * math.sin(a):.1f}" stroke="{G_ORTA}" stroke-width="2.4" stroke-linecap="round"/>')
    return s + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{G_DIS}" stroke="{G_ORTA}" stroke-width="2"/>'


def ay(cx, cy, r, dolgu=AY, cizgi=AY_C, saydam=1):
    s = f'<g opacity="{saydam}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="1.6"/>'
    for dx, dy, k in [(-0.35, -0.25, 0.22), (0.3, 0.2, 0.16), (-0.1, 0.42, 0.12), (0.38, -0.35, 0.1)]:
        s += f'<circle cx="{cx + dx * r:.1f}" cy="{cy + dy * r:.1f}" r="{k * r:.1f}" fill="#c3c7cf" stroke="{cizgi}" stroke-width="0.8"/>'
    return s + '</g>'


def dunya(cx, cy, r):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#4f8fe8" stroke="#2a62b8" stroke-width="1.8"/>'
    s += (f'<path d="M{cx - 0.55 * r:.1f} {cy - 0.45 * r:.1f} q{0.3 * r:.1f} {-0.25 * r:.1f} {0.55 * r:.1f} {-0.05 * r:.1f} '
          f'q{0.1 * r:.1f} {0.35 * r:.1f} {-0.2 * r:.1f} {0.45 * r:.1f} q{-0.3 * r:.1f} {0.15 * r:.1f} {-0.35 * r:.1f} {-0.4 * r:.1f} z" fill="#3fae5a"/>')
    s += (f'<path d="M{cx + 0.1 * r:.1f} {cy + 0.1 * r:.1f} q{0.35 * r:.1f} {-0.1 * r:.1f} {0.55 * r:.1f} {0.15 * r:.1f} '
          f'q{-0.05 * r:.1f} {0.4 * r:.1f} {-0.35 * r:.1f} {0.5 * r:.1f} q{-0.25 * r:.1f} {-0.2 * r:.1f} {-0.2 * r:.1f} {-0.65 * r:.1f} z" fill="#3fae5a"/>')
    return s


def modeller():
    ic = ''
    for i, (bas, renk) in enumerate([('I. model', MOR), ('II. model', MAVI)]):
        x = 4 + i * 302
        ic += f'<rect x="{x}" y="4" width="290" height="168" rx="12" fill="#f7f9fd" stroke="{GRI}" stroke-width="1.4"/>'
        ic += f'<rect x="{x}" y="4" width="290" height="28" rx="12" fill="{renk}"/><rect x="{x}" y="20" width="290" height="12" fill="{renk}"/>'
        ic += yazi(x + 145, 23, bas, 14, '#fff')
    x = 4                                                         # I. model: ışık Ay'ın kendisinden çıkar
    for k in range(10):
        a = k * math.pi / 5
        ic += (f'<line x1="{x + 80 + 31 * math.cos(a):.1f}" y1="{96 + 31 * math.sin(a):.1f}" x2="{x + 80 + 41 * math.cos(a):.1f}" '
               f'y2="{96 + 41 * math.sin(a):.1f}" stroke="{TUR}" stroke-width="2.2" stroke-linecap="round"/>')
    ic += ay(x + 80, 96, 25) + dunya(x + 236, 96, 26)
    ic += ok(x + 126, 96, x + 204, 96, TUR)
    ic += yazi(x + 80, 146, 'Ay', 13) + yazi(x + 236, 136, 'Dünya', 13)
    ic += yazi(x + 145, 164, 'Işık Ay’ın kendisinden çıkar.', 13, LAC, ince=True)
    x = 306                                                       # II. model: Güneş -> Ay -> Dünya
    ic += gunes(x + 46, 72, 22) + ay(x + 145, 104, 17) + dunya(x + 244, 72, 25)
    ic += ok(x + 80, 82, x + 126, 98, TUR)
    ic += ok(x + 164, 98, x + 216, 82, TUR, kesik=True)
    ic += yazi(x + 46, 120, 'Güneş', 13) + yazi(x + 145, 137, 'Ay', 13) + yazi(x + 244, 112, 'Dünya', 13)
    ic += yazi(x + 145, 164, 'Işık Güneş’ten gelir, Ay’dan yansır.', 13, LAC, ince=True)
    return svg(600, 176, ic, 'İki model. I. model: Ay’dan dışarı ışınlar çıkıyor, ışık Ay’dan Dünya’ya gidiyor; “Işık Ay’ın kendisinden çıkar.” II. model: ışık Güneş’ten Ay’a gidiyor, Ay’dan Dünya’ya yansıyor; “Işık Güneş’ten gelir, Ay’dan yansır.”', 36)


def ay_bolgeleri():
    cx, cy, r = 220, 98, 88
    ic = f'<defs><clipPath id="f4ayk"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{AY}"/>'
    ic += '<g clip-path="url(#f4ayk)" fill="#8e95a3">'
    ic += '<path d="M150 40 C170 25 205 28 215 45 C225 62 210 80 190 84 C175 90 165 110 150 120 C138 128 120 112 124 95 C128 78 135 55 150 40 Z"/>'
    ic += '<path d="M232 52 C250 44 270 52 272 68 C285 72 292 90 284 104 C276 118 258 116 248 106 C238 96 226 84 228 70 C229 62 228 56 232 52 Z"/>'
    ic += '<ellipse cx="292" cy="70" rx="12" ry="10"/>'
    ic += '<path d="M190 128 C200 120 215 124 214 136 C212 146 198 148 190 142 C184 138 185 132 190 128 Z"/>'
    ic += '</g>'
    for x, y, k in [(240, 160, 7), (205, 170, 5), (265, 140, 5), (172, 152, 4), (300, 126, 4), (230, 182, 3), (150, 140, 3)]:
        ic += f'<circle cx="{x}" cy="{y}" r="{k}" fill="#c5c9d2" stroke="#a3a9b5" stroke-width="1"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{AY_C}" stroke-width="2"/>'
    ic += f'<circle cx="170" cy="62" r="4" fill="{LAC}"/><line x1="170" y1="62" x2="66" y2="40" stroke="{LAC}" stroke-width="1.6"/>' + rozet(52, 38, 'K', LAC, 14, 15)
    ic += f'<circle cx="252" cy="152" r="4" fill="{LAC}"/><line x1="252" y1="152" x2="372" y2="172" stroke="{LAC}" stroke-width="1.6"/>' + rozet(386, 174, 'L', LAC, 14, 15)
    return svg(440, 192, ic, 'Dünya’dan görünen Ay: yüzeyde koyu ve açık bölgeler var. K harfi koyu renkli bir bölgeyi, L harfi kraterli açık renkli bir bölgeyi gösteriyor.', 30)


def parcalanma():
    rnd = random.Random(54)
    ic = ''
    for x, bas, deger, acik, renk in [(110, 'Gündüz', '125 °C’ye kadar', TUR_A, TUR), (310, 'Gece', '−174 °C’ye kadar', '#e6e9f5', LAC)]:
        ic += f'<rect x="{x}" y="6" width="180" height="52" rx="10" fill="{acik}" stroke="{renk}" stroke-width="1.8"/>'
        if bas == 'Gündüz':
            ic += gunes(x + 28, 32, 9)
        else:
            ic += f'<circle cx="{x + 28}" cy="32" r="13" fill="#f2c94c"/><circle cx="{x + 34}" cy="27" r="11" fill="{acik}"/>'
        ic += yazi(x + 52, 27, bas, 13, renk, 'start') + yazi(x + 52, 47, deger, 15, LAC, 'start')
    ornek = ['Kum', 'Kaya', 'Toz', 'Taş']
    for i, ad in enumerate(ornek):
        x = 12 + i * 148
        ic += f'<rect x="{x}" y="72" width="132" height="84" rx="12" fill="#f6f3ee" stroke="#b9ab95" stroke-width="1.6"/>'
        mx, my = x + 66, 116
        if ad == 'Kaya':
            nk = [(0, -30), (24, -22), (36, 2), (26, 26), (-6, 30), (-30, 20), (-38, -4), (-22, -24)]
            ic += '<path d="M' + ' L'.join(f'{mx + a:.0f} {my + b:.0f}' for a, b in nk) + f' Z" fill="#8d8478" stroke="#5f574d" stroke-width="1.6"/>'
            ic += f'<path d="M{mx - 8} {my - 18} l6 12 l-4 10 M{mx + 14} {my - 6} l-8 10" fill="none" stroke="#5f574d" stroke-width="1.2"/>'
        elif ad == 'Taş':
            for a, b, rx, ry in [(-34, -10, 13, 10), (-6, -18, 11, 9), (22, -8, 14, 10), (-20, 16, 12, 9), (12, 18, 13, 10), (40, 18, 9, 7)]:
                ic += f'<ellipse cx="{mx + a}" cy="{my + b}" rx="{rx}" ry="{ry}" fill="#9a9184" stroke="#665d52" stroke-width="1.2"/>'
        elif ad == 'Kum':
            for _ in range(70):
                ic += f'<circle cx="{mx + rnd.uniform(-52, 52):.1f}" cy="{my + rnd.uniform(-28, 30):.1f}" r="{rnd.uniform(1.8, 2.8):.1f}" fill="#b09f83" stroke="#8a7b62" stroke-width="0.4"/>'
        else:
            ic += f'<ellipse cx="{mx}" cy="{my + 8}" rx="54" ry="26" fill="#ddd6cb"/>'
            for _ in range(260):
                ic += f'<circle cx="{mx + rnd.uniform(-54, 54):.1f}" cy="{my + rnd.uniform(-26, 32):.1f}" r="0.9" fill="#9e968a"/>'
        ic += yazi(mx, 176, ad, 14)
    return svg(600, 184, ic, 'Ay’da gündüz sıcaklık 125 °C’ye kadar çıkar, gece −174 °C’ye kadar iner. Altta yüzeyden alınmış dört örnek: kum, kaya, toz, taş.', 36)


def dolanma_konum():
    cx, cy, R = 220, 130, 92
    ic = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{GRI}" stroke-width="1.6" stroke-dasharray="6 5"/>'
    ic += dunya(cx, cy, 30) + yazi(cx, cy + 50, 'Dünya', 13)
    konum = [(1, 0), (2, 90), (3, 180), (4, 270)]
    for no, aci in konum:
        a = math.radians(aci)
        mx, my = cx + R * math.cos(a), cy - R * math.sin(a)
        ic += ay(mx, my, 17)
        yon = -1 if no == 3 else 1                                 # 3. konum hatalı: krater Dünya'ya bakmıyor
        ux, uy = (cx - mx) / R * yon, (cy - my) / R * yon
        ic += f'<circle cx="{mx + 10 * ux:.1f}" cy="{my + 10 * uy:.1f}" r="5" fill="{KIR}" stroke="#fff" stroke-width="1.2"/>'
        bx, by = mx + 33 * math.cos(a + math.radians(35)), my - 33 * math.sin(a + math.radians(35))
        ic += rozet(bx, by, str(no), LAC)
    a1, a2, Rr = math.radians(24), math.radians(66), 108
    sx, sy = cx + Rr * math.cos(a1), cy - Rr * math.sin(a1)
    ex, ey = cx + Rr * math.cos(a2), cy - Rr * math.sin(a2)
    ic += f'<path d="M{sx:.1f} {sy:.1f} A{Rr} {Rr} 0 0 0 {ex:.1f} {ey:.1f}" fill="none" stroke="{TUR}" stroke-width="3"/>'
    ic += ok_ucu(ex, ey, -math.sin(a2), -math.cos(a2), TUR, 11)
    ic += yazi(330, 48, 'Dolanma yönü', 13, TUR, 'start')
    ic += f'<circle cx="26" cy="246" r="5" fill="{KIR}" stroke="#fff" stroke-width="1.2"/>' + yazi(38, 251, 'Krater', 13, LAC, 'start', ince=True)
    return svg(440, 262, ic, 'Dünya ortada; Ay çevresinde 1, 2, 3 ve 4 numaralı dört konumda. Kırmızı nokta Ay yüzeyindeki bir krater: 1, 2 ve 4. konumlarda Dünya’ya dönük, 3. konumda Dünya’nın tersine dönük. Dolanma yönü saatin dönme yönünün tersi.', 64)


def iki_dolanma():
    ic = gunes(80, 105, 40) + yazi(80, 168, 'Güneş', 13)
    ic += f'<path d="M245 22.7 A330 95 0 0 1 245 187.3" fill="none" stroke="{GRI}" stroke-width="1.6" stroke-dasharray="7 5"/>'
    ex, ey = 410, 105
    ic += f'<circle cx="{ex}" cy="{ey}" r="55" fill="none" stroke="{GRI}" stroke-width="1.4" stroke-dasharray="5 4"/>'
    ic += dunya(ex, ey, 22) + yazi(ex, ey + 40, 'Dünya', 13)
    mx, my = ex + 55 * math.cos(math.radians(45)), ey - 55 * math.sin(math.radians(45))
    ic += ay(mx, my, 11) + yazi(mx + 18, my - 8, 'Ay', 13, LAC, 'start')
    a1, a2, r1 = math.radians(100), math.radians(160), 68                 # 1: Dünya çevresinde dolanma
    s1 = (ex + r1 * math.cos(a1), ey - r1 * math.sin(a1))
    e1 = (ex + r1 * math.cos(a2), ey - r1 * math.sin(a2))
    ic += f'<path d="M{s1[0]:.1f} {s1[1]:.1f} A{r1} {r1} 0 0 0 {e1[0]:.1f} {e1[1]:.1f}" fill="none" stroke="{MOR}" stroke-width="3"/>'
    ic += ok_ucu(e1[0], e1[1], -math.sin(a2), -math.cos(a2), MOR, 11) + rozet(352, 40, '1', MOR)
    pts = [(80 + 315 * math.cos(math.radians(t)), 105 - 82 * math.sin(math.radians(t))) for t in range(-58, -33, 2)]
    ic += '<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + f'" fill="none" stroke="{TUR}" stroke-width="3"/>'
    t = math.radians(-34)
    ic += ok_ucu(pts[-1][0], pts[-1][1], -315 * math.sin(t), -82 * math.cos(t), TUR, 11) + rozet(268, 196, '2', TUR)
    ic += yazi(592, 202, 'Ölçekli değildir.', 11, GRI, 'end', ince=True)
    return svg(600, 210, ic, 'Güneş solda; Dünya, Güneş çevresindeki yörüngesinde. Ay, Dünya çevresindeki küçük yörüngede. 1 numaralı ok Ay’ın Dünya çevresindeki dolanmasını, 2 numaralı ok Dünya’nın yörüngesi boyunca Güneş çevresindeki dolanmayı gösteriyor. Ölçekli değildir.', 38)


def gozlem_defteri():
    notlar = ['Ay çok parlaktı; demek ki kendi ışığını yayıyor.', 'Ay’ın yüzeyinde açık ve koyu bölgeler seçtim.',
              'Ay sabah saatlerinde gökyüzünde de görünüyordu.', 'Dürbünle bakınca kraterleri daha net gördüm.']
    ic = f'<rect x="4" y="4" width="552" height="188" rx="10" fill="#fffdf5" stroke="#d9c79a" stroke-width="1.8"/>'
    ic += f'<line x1="52" y1="4" x2="52" y2="192" stroke="#f0a8a8" stroke-width="1.4"/>'
    for k in range(7):
        ic += f'<circle cx="24" cy="{24 + k * 26}" r="6" fill="#fff" stroke="#b9a777" stroke-width="1.6"/>'
    ic += yazi(70, 34, 'Deniz’in gözlem notları', 15, '#8a6d12', 'start')
    for k, n in enumerate(notlar):
        y = 72 + k * 34
        ic += f'<line x1="64" y1="{y + 9}" x2="540" y2="{y + 9}" stroke="#cfdcf2" stroke-width="1"/>'
        ic += yazi(70, y, f'{k + 1}.', 15, '#8a6d12', 'start') + yazi(92, y, n, 15, LAC, 'start', ince=True)
    return svg(560, 196, ic, 'Deniz’in gözlem notları: 1. Ay çok parlaktı; demek ki kendi ışığını yayıyor. 2. Ay’ın yüzeyinde açık ve koyu bölgeler seçtim. 3. Ay sabah saatlerinde gökyüzünde de görünüyordu. 4. Dürbünle bakınca kraterleri daha net gördüm.', 36)


def krater(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#c4c7cd" stroke="#8b9099" stroke-width="1"/>'
            f'<circle cx="{cx + r * 0.12:.1f}" cy="{cy + r * 0.12:.1f}" r="{r * 0.74:.1f}" fill="#80858f"/>'
            f'<path d="M{cx - r * 0.6:.1f} {cy + r * 0.45:.1f} A{r * 0.75:.1f} {r * 0.75:.1f} 0 0 0 {cx + r * 0.6:.1f} {cy + r * 0.45:.1f}" fill="none" stroke="#e3e5e9" stroke-width="{max(1, r * 0.12):.1f}"/>')


def krater_goruntuleri():
    rnd = random.Random(31)
    eski = [(60, 50, 22), (172, 40, 14), (122, 104, 18)]
    yeni = [(204, 102, 9), (52, 114, 7)]
    ic = ''
    for i, (bas, liste) in enumerate([('1. görüntü (önce)', eski), ('2. görüntü (sonra)', eski + yeni)]):
        x, y = 30 + i * 290, 30
        ic += yazi(x + 125, 20, bas, 14)
        ic += f'<rect x="{x}" y="{y}" width="250" height="140" rx="8" fill="#a9adb5" stroke="{LAC}" stroke-width="1.5"/>'
        r2 = random.Random(5)
        for _ in range(60):
            ic += f'<circle cx="{x + r2.uniform(6, 244):.1f}" cy="{y + r2.uniform(6, 134):.1f}" r="{r2.uniform(0.6, 1.4):.1f}" fill="#979ba3"/>'
        for a, b, r in liste:
            ic += krater(x + a, y + b, r)
    ic += ok(284, 100, 314, 100, LAC, kal=2.2)
    ic += yazi(300, 188, 'Aynı bölge · Ay Keşif Yörünge Aracı görüntüleri', 12, GRI, ince=True)
    rnd.random()
    return svg(600, 194, ic, 'Ay Keşif Yörünge Aracı’nın aynı bölgeden çektiği iki görüntü. 1. görüntüde (önce) 3 krater, 2. görüntüde (sonra) aynı 3 kraterle birlikte 2 yeni küçük krater var.', 34)


def gok_tasi():
    rnd = random.Random(12)
    ic = '<defs><clipPath id="f4gt"><rect x="4" y="4" width="592" height="172" rx="12"/></clipPath></defs><g clip-path="url(#f4gt)">'
    ic += '<rect x="4" y="4" width="592" height="172" fill="#1b2650"/>'
    for _ in range(22):
        ic += f'<circle cx="{rnd.uniform(14, 586):.1f}" cy="{rnd.uniform(12, 100):.1f}" r="{rnd.uniform(0.7, 1.4):.1f}" fill="#fff" opacity="0.8"/>'
    ic += '<path d="M0 122 L232 122 Q250 113 262 124 Q300 166 338 124 Q350 113 368 122 L600 122 V180 H0 Z" fill="#b9bcc4"/>'
    ic += '<path d="M262 124 Q300 166 338 124" fill="none" stroke="#8b9099" stroke-width="2"/>'
    for _ in range(26):
        x, y = rnd.uniform(20, 580), rnd.uniform(140, 170)
        if 250 < x < 350 and y < 150:
            continue
        ic += f'<path d="M{x:.1f} {y - 3.5:.1f} l3 3.5 l-3 3.5 l-3 -3.5 z" fill="#8fd3ff" stroke="#3a8fc4" stroke-width="0.6"/>'
    for x, y in [(282, 98), (300, 84), (320, 96), (268, 110), (336, 108), (306, 104), (290, 112)]:
        ic += f'<path d="M{x} {y - 4} l3.5 4 l-3.5 4 l-3.5 -4 z" fill="#8fd3ff" stroke="#3a8fc4" stroke-width="0.7"/>'
    for k in range(4):
        ic += f'<line x1="{150 + k * 4}" y1="{8 + k * 6}" x2="{200 + k * 2}" y2="{36 + k * 3}" stroke="#ffb15c" stroke-width="{2.4 - k * 0.4:.1f}" opacity="{0.9 - k * 0.15:.2f}" stroke-linecap="round"/>'
    ic += '<path d="M206 34 L220 30 L230 40 L227 54 L212 58 L202 48 Z" fill="#7a6a58" stroke="#4e4336" stroke-width="1.4"/>'
    ic += f'<line x1="232" y1="58" x2="286" y2="116" stroke="#ffb15c" stroke-width="1.6" stroke-dasharray="5 4"/>'
    ic += '</g>'
    ic += f'<rect x="4" y="4" width="592" height="172" rx="12" fill="none" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(250, 32, 'Gök taşı', 13, '#ffd9a8', 'start')
    ic += f'<line x1="342" y1="100" x2="370" y2="84" stroke="#cfe9ff" stroke-width="1.2"/>' + yazi(376, 88, 'Yüzeye çıkan buz parçacıkları', 13, '#cfe9ff', 'start')
    ic += yazi(300, 160, 'Krater', 13, LAC)
    ic += yazi(470, 146, 'Ay yüzeyi', 13, LAC, 'start')
    return svg(600, 180, ic, 'Ay yüzeyine çarparak krater açan bir gök taşı; çarpmayla yüzeyin altındaki buz parçacıkları yüzeye çıkıyor.', 24)


def uzay_programi():
    kutu = [('2021', MAVI, MAVI_A, ['Millî Uzay Programı', 'başlatıldı']),
            ('İlk aşama', TUR, TUR_A, ['Millî uzay aracı Ay’ın', 'yörüngesine ulaşır']),
            ('Sonraki hedef', YES, YES_A, ['Ay’a sert ve', 'yumuşak iniş'])]
    ic = ''
    for i, (bas, renk, acik, satir) in enumerate(kutu):
        x = 8 + i * 202
        ic += f'<rect x="{x}" y="6" width="180" height="118" rx="10" fill="{acik}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="6" width="180" height="26" rx="10" fill="{renk}"/><rect x="{x}" y="20" width="180" height="12" fill="{renk}"/>'
        ic += yazi(x + 90, 24, bas, 13, '#fff')
        mx = x + 90
        if i == 0:
            ic += dunya(mx, 56, 17)
        elif i == 1:
            ic += f'<ellipse cx="{mx}" cy="56" rx="38" ry="12" fill="none" stroke="{renk}" stroke-width="1.4" stroke-dasharray="4 3"/>' + ay(mx, 56, 14)
            ic += f'<rect x="{mx + 30}" y="61" width="10" height="7" rx="1.5" fill="{LAC}"/><rect x="{mx + 24}" y="63" width="6" height="3" fill="{MAVI}"/><rect x="{mx + 40}" y="63" width="6" height="3" fill="{MAVI}"/>'
        else:
            ic += f'<path d="M{mx - 46} 76 Q{mx} 62 {mx + 46} 76 Z" fill="{AY}" stroke="{AY_C}" stroke-width="1.4"/>'
            ic += f'<path d="M{mx - 8} 50 h16 l4 10 h-24 z" fill="{LAC}"/><line x1="{mx - 10}" y1="60" x2="{mx - 15}" y2="69" stroke="{LAC}" stroke-width="1.8"/><line x1="{mx + 10}" y1="60" x2="{mx + 15}" y2="69" stroke="{LAC}" stroke-width="1.8"/>'
        for k, s in enumerate(satir):
            ic += yazi(mx, 98 + k * 18, s, 13, LAC, ince=True)
        if i < 2:
            ic += ok(x + 183, 65, x + 201, 65, LAC, kal=2.2, uc=8)
    return svg(600, 128, ic, 'Millî Uzay Programı: 2021’de başlatıldı; ilk aşamada millî uzay aracı Ay’ın yörüngesine ulaşır; sonraki hedef Ay’a sert ve yumuşak iniş.', 27)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = modeller()
    s[3]['gorsel'] = ay_bolgeleri()
    s[4]['gorsel'] = parcalanma()
    s[6]['gorsel'] = dolanma_konum()
    s[7]['gorsel'] = iki_dolanma()
    s[9]['gorsel'] = gozlem_defteri()
    s[10]['gorsel'] = krater_goruntuleri()
    s[11]['gorsel'] = gok_tasi()
    s[12]['gorsel'] = uzay_programi()
