"""6. sınıf Türkçe 1. hafta (Kaşgarlı Mahmut, akıcı okuma, nefes/tekerleme, virgül) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
CATI, TAS = '#d9b98f', '#f5eedd'
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


def bilgi_karti():
    """Dîvânu Lugâti't-Türk bilgi kartı; 3. bilgi yanlış (750)."""
    ic = kutu(4, 4, 352, 122, '#fff', MOR, 10, 1.6) + f'<rect x="4" y="4" width="352" height="26" rx="10" fill="{MOR}"/><rect x="4" y="20" width="352" height="10" fill="{MOR}"/>'
    ic += yazi(180, 22, 'Dîvânu Lugâti’t-Türk', 13.5, '#fff')
    bilgi = ['Yazarı Kaşgarlı Mahmut’tur.', 'Türkçenin ilk sözlüğüdür.', 'İçinde 750 kelime vardır.', 'Türk boylarından ve damgalarından söz eder.']
    for i, b in enumerate(bilgi):
        y = 46 + i * 22
        ic += rozet(24, y, str(i + 1), MOR, 8) + yazi(40, y + 4.5, b, 12, LAC, 'start', True)
    return svg(360, 130, ic, 'Bilgi kartı, Dîvânu Lugâti’t-Türk: 1. Yazarı Kaşgarlı Mahmut’tur. 2. Türkçenin ilk sözlüğüdür. 3. İçinde 750 kelime vardır. 4. Türk boylarından ve damgalarından söz eder.', 26)


def avlu_plani():
    """Kuşbakışı yapı planı: A oda (çatılı), B ortadaki üstü açık, duvarla çevrili alan, C oda (çatılı), D yapının dışındaki bahçe."""
    ic = f'<rect x="206" y="24" width="86" height="118" rx="6" fill="#cdebd5"/>'
    for tx, ty in [(234, 52), (266, 92), (238, 122)]:
        ic += f'<circle cx="{tx}" cy="{ty}" r="10" fill="{YES}"/><circle cx="{tx - 3}" cy="{ty - 3}" r="4" fill="#3cc073"/>'
    ic += f'<rect x="10" y="8" width="192" height="134" fill="{CATI}" stroke="{KAHVE}" stroke-width="3"/>'
    ic += f'<rect x="48" y="42" width="116" height="66" fill="{TAS}" stroke="{KAHVE}" stroke-width="2.4"/>'
    ic += ''.join(f'<line x1="{48 + k * 14.5:.1f}" y1="42" x2="{48 + k * 14.5:.1f}" y2="108" stroke="#e6dcc4" stroke-width="0.8"/>' for k in range(1, 8))
    ic += f'<circle cx="106" cy="75" r="11" fill="#7cc3f0" stroke="{MAVI}" stroke-width="1.2"/><circle cx="106" cy="75" r="3" fill="{MAVI}"/>'
    for x1, y1, x2, y2 in [(10, 42, 48, 42), (10, 108, 48, 108), (164, 42, 202, 42), (164, 108, 202, 108), (80, 8, 80, 42), (132, 8, 132, 42), (80, 108, 80, 142), (132, 108, 132, 142)]:
        ic += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += f'<rect x="98" y="139" width="16" height="6" fill="#fff"/>'
    ic += rozet(29, 25, 'A', TUR) + rozet(78, 60, 'B', TUR) + rozet(183, 125, 'C', TUR) + rozet(282, 34, 'D', TUR)
    ic += f'<rect x="298" y="96" width="16" height="14" fill="{CATI}" stroke="{KAHVE}" stroke-width="1"/>' + yazi(298, 128, 'Üstü', 12, SOLUK, 'start', True) + yazi(298, 143, 'kapalı', 12, SOLUK, 'start', True)
    ic += yazi(106, 155, 'Giriş', 11.5, SOLUK, 'middle', True)
    return svg(360, 158, ic, 'Kuşbakışı yapı planı: A köşedeki çatılı oda, B yapının ortasında üstü açık, duvarlarla çevrili, fıskiyeli taş zeminli alan, C çatılı oda, D yapının dışındaki ağaçlı bahçe', 28)


def hikaye():
    """Durak numaralı hikâye kartı."""
    satir = ['Elif, dedesinin eski sandığını açtı. Kumaşların',
             'altında sararmış, kalın bir defter buldu.',
             'Kapağında “Kelimelerim” yazıyordu. Elif, defteri',
             'heyecanla açıp ilk sayfaya baktı.']
    ic = kutu(4, 4, 352, 118, '#fffdf5', GRI, 6, 1.2) + yazi(180, 24, 'Sandıktaki Defter', 13.5, CAM)
    for i, s in enumerate(satir):
        y = 48 + i * 20
        ic += f'<line x1="16" y1="{y + 5}" x2="344" y2="{y + 5}" stroke="{MAVI_A}" stroke-width="1"/>' + yazi(18, y, s, 12, LAC, 'start', True)
    oy = 108
    pts = ' '.join(f'{240 + 11 * math.cos(math.pi / 8 + k * math.pi / 4):.1f},{oy - 4 + 11 * math.sin(math.pi / 8 + k * math.pi / 4):.1f}' for k in range(8))
    ic += f'<polygon points="{pts}" fill="{KIR}"/>' + yazi(240, oy, '1', 11, '#fff')
    return svg(360, 126, ic, 'Hikâye, Sandıktaki Defter: Elif, dedesinin eski sandığını açtı. Kumaşların altında sararmış, kalın bir defter buldu. Kapağında Kelimelerim yazıyordu. Elif, defteri heyecanla açıp ilk sayfaya baktı. Burada 1 numaralı durak var.', 26)


def ok(x1, y1, x2, y2, renk):
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2:.1f},{y2:.1f} {x2 - 7 * math.cos(a - 0.45):.1f},{y2 - 7 * math.sin(a - 0.45):.1f} {x2 - 7 * math.cos(a + 0.45):.1f},{y2 - 7 * math.sin(a + 0.45):.1f}'
    return f'<polygon points="{u}" fill="{renk}"/>'


def goz():
    """Göz uygulamaları: sola-sağa, yukarı-aşağı, 0 çizme, yatay 8 çizme."""
    ic = ''
    ad = ['Sola, sağa', 'Yukarı, aşağı', '0 çizme', 'Yatay 8 çizme']
    renk = [MAVI, YES, TUR, MOR]
    acik = [MAVI_A, YES_A, TUR_A, MOR_A]
    for i in range(4):
        x0 = 4 + i * 89
        cx, cy, c = x0 + 42, 38, renk[i]
        ic += kutu(x0, 4, 84, 84, acik[i], c, 8, 1.2)
        if i == 0:
            ic += f'<line x1="{cx - 26}" y1="{cy}" x2="{cx + 26}" y2="{cy}" stroke="{c}" stroke-width="2.2"/>' + ok(cx, cy, cx - 30, cy, c) + ok(cx, cy, cx + 30, cy, c)
        elif i == 1:
            ic += f'<line x1="{cx}" y1="{cy - 22}" x2="{cx}" y2="{cy + 22}" stroke="{c}" stroke-width="2.2"/>' + ok(cx, cy, cx, cy - 26, c) + ok(cx, cy, cx, cy + 26, c)
        elif i == 2:
            ic += f'<ellipse cx="{cx}" cy="{cy}" rx="16" ry="23" fill="none" stroke="{c}" stroke-width="2.2"/>' + ok(cx + 16, cy - 4, cx + 16, cy + 2, c)
        else:
            pts = ' '.join(f'{cx + 30 * math.sin(t / 30 * 2 * math.pi):.1f},{cy + 15 * math.sin(t / 30 * 4 * math.pi):.1f}' for t in range(31))
            ic += f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.2"/>' + ok(cx + 26, cy + 9, cx + 29, cy + 3, c)
        ic += f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{LAC}"/>' + yazi(cx, 80, ad[i], 11, LAC)
    return svg(360, 92, ic, 'Göz uygulamaları: gözlerle sola ve sağa bakma, yukarı ve aşağı bakma, 0 çizme, yatay 8 çizme', 23)


def nefes():
    """A tavşan, B çiçek, C balon."""
    ic = ''
    renk, acik = [CAM, KIR, MOR], [CAM_A, KIR_A, MOR_A]
    for i in range(3):
        x0 = 4 + i * 119
        ic += kutu(x0, 4, 114, 76, acik[i], renk[i], 8, 1.2) + rozet(x0 + 14, 17, 'ABC'[i], renk[i])
    # tavşan
    x, y = 62, 48
    ic += (f'<ellipse cx="{x - 8}" cy="{y - 22}" rx="6" ry="17" fill="#f4f1ee" stroke="{SOLUK}" stroke-width="1.2" transform="rotate(-12 {x - 8} {y - 22})"/>'
           f'<ellipse cx="{x + 8}" cy="{y - 22}" rx="6" ry="17" fill="#f4f1ee" stroke="{SOLUK}" stroke-width="1.2" transform="rotate(12 {x + 8} {y - 22})"/>'
           f'<ellipse cx="{x - 8}" cy="{y - 22}" rx="2.6" ry="11" fill="#f7c6cf" transform="rotate(-12 {x - 8} {y - 22})"/>'
           f'<ellipse cx="{x + 8}" cy="{y - 22}" rx="2.6" ry="11" fill="#f7c6cf" transform="rotate(12 {x + 8} {y - 22})"/>'
           f'<circle cx="{x}" cy="{y}" r="17" fill="#f4f1ee" stroke="{SOLUK}" stroke-width="1.2"/><circle cx="{x - 6}" cy="{y - 3}" r="2" fill="{LAC}"/><circle cx="{x + 6}" cy="{y - 3}" r="2" fill="{LAC}"/>'
           f'<path d="M{x - 2.5} {y + 4} h5 l-2.5 3 z" fill="#e57c93"/>')
    ic += ''.join(f'<path d="M{x + 20} {y + 2 + k * 5} q6 -2 11 0" fill="none" stroke="{CAM}" stroke-width="1.3"/>' for k in range(3))
    # çiçek
    x, y = 180, 40
    ic += f'<path d="M{x} {y + 8} V{y + 34}" stroke="{YES}" stroke-width="2.4"/><path d="M{x} {y + 26} q-12 -2 -14 -12 q10 0 14 12" fill="{YES}"/>'
    ic += ''.join(f'<ellipse cx="{x + 9 * math.cos(k * math.pi / 3):.1f}" cy="{y + 9 * math.sin(k * math.pi / 3):.1f}" rx="7" ry="5" fill="#f17aa0" transform="rotate({k * 60} {x + 9 * math.cos(k * math.pi / 3):.1f} {y + 9 * math.sin(k * math.pi / 3):.1f})"/>' for k in range(6))
    ic += f'<circle cx="{x}" cy="{y}" r="5" fill="{ALTIN}"/>'
    # balon
    x, y = 299, 36
    ic += (f'<ellipse cx="{x}" cy="{y}" rx="18" ry="22" fill="{KIR}"/><ellipse cx="{x - 6}" cy="{y - 8}" rx="4" ry="6" fill="#fff" opacity="0.5"/>'
           f'<path d="M{x - 3} {y + 24} h6 l-3 -3 z" fill="{KIR}"/><path d="M{x} {y + 24} q-6 8 0 14 t0 10" fill="none" stroke="{SOLUK}" stroke-width="1.2"/>')
    return svg(360, 84, ic, 'Nefes çalışmaları: A tavşan, B çiçek, C balon', 21)


def tekerleme():
    satir = ['Kırk kırmızı kiraz kasası kırk kere kaydı,', 'kırk kere kaydıkça kırk kiraz kasadan kaçtı,', 'kaçan kırk kiraz kırk kuzguna kaldı.']
    ic = kutu(4, 4, 352, 92, YES_A, YES, 10, 1.6) + kutu(126, 10, 108, 20, YES, YES, 10, 1) + yazi(180, 24.5, 'TEKERLEME', 11.5, '#fff')
    for i, s in enumerate(satir):
        ic += yazi(180, 50 + i * 18, s, 12.5, LAC, 'middle', True)
    return svg(360, 100, ic, 'Tekerleme: Kırk kırmızı kiraz kasası kırk kere kaydı, kırk kere kaydıkça kırk kiraz kasadan kaçtı, kaçan kırk kiraz kırk kuzguna kaldı.', 23)


def notlar():
    """Üç yapışkan not: virgülün görevleri."""
    notlar_ = [['Evet, sözlüğü', 'ben getirdim.'], ['Sözlüğü açtı,', 'kelimeyi buldu,', 'deftere yazdı.'], ['Bu, dedemin', 'en eski sözlüğü.']]
    renk = ['#fff3b0', '#d9f2ff', '#ffe0ec']
    ic = ''
    for i, n in enumerate(notlar_):
        x0 = 6 + i * 118
        ic += f'<rect x="{x0}" y="6" width="110" height="78" fill="{renk[i]}" stroke="{GRI}" stroke-width="0.8" transform="rotate({[-2, 1.5, -1][i]} {x0 + 55} 45)"/>'
        ic += rozet(x0 + 14, 18, str(i + 1), MAVI, 8)
        top = 44 if len(n) == 2 else 36
        ic += ''.join(yazi(x0 + 57, top + k * 17, s, 12, LAC, 'middle', True) for k, s in enumerate(n))
    return svg(360, 90, ic, 'Notlar: 1. Evet, sözlüğü ben getirdim. 2. Sözlüğü açtı, kelimeyi buldu, deftere yazdı. 3. Bu, dedemin en eski sözlüğü.', 22)


def iki_cumle():
    ic = ''
    for i, (h, s, c, d) in enumerate([('A', 'O kelime defterini kaybetti.', MAVI, MAVI_A), ('B', 'O, kelime defterini kaybetti.', TUR, TUR_A)]):
        y = 4 + i * 32
        ic += kutu(4, y, 352, 28, d, c, 8, 1.3) + rozet(22, y + 14, h, c) + yazi(44, y + 19, s, 13, LAC, 'start')
    return svg(360, 66, ic, 'İki cümle: A. O kelime defterini kaybetti. B. O, kelime defterini kaybetti.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bilgi_karti()
    s[4]['gorsel'] = avlu_plani()
    s[5]['gorsel'] = hikaye()
    s[6]['gorsel'] = goz()
    s[7]['gorsel'] = nefes()
    s[9]['gorsel'] = tekerleme()
    s[10]['gorsel'] = notlar()
    s[11]['gorsel'] = iki_cumle()
