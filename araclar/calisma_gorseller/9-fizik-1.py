"""9. sınıf Fizik 1. hafta (fizik bilimi) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


SU, GOK = '#5aa9e6', '#dff1fd'


def olaylar():
    ic = ''
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 80, GOK if i != 3 else '#fff', GRI, 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), LAC)
    # 1 gökkuşağı
    cx, cy = 46, 70
    for k, c in enumerate([KIR, TUR, ALTIN, YES, MAVI, MOR]):
        r = 34 - k * 3.2
        ic += f'<path d="M{cx - r:.1f} {cy} a{r:.1f} {r:.1f} 0 0 1 {2 * r:.1f} 0" fill="none" stroke="{c}" stroke-width="3"/>'
    ic += f'<ellipse cx="22" cy="70" rx="12" ry="6" fill="#fff"/><ellipse cx="70" cy="70" rx="12" ry="6" fill="#fff"/>'
    # 2 rampa + kaykay
    x = 93
    ic += f'<path d="M{x + 6} 76 H{x + 60} V40 Q{x + 56} 72 {x + 6} 72 Z" fill="{SOLUK}"/>'
    ic += f'<path d="M{x + 60} 38 Q{x + 66} 14 {x + 78} 30" fill="none" stroke="{TUR}" stroke-width="1.4" stroke-dasharray="3 3"/>'
    ic += f'<g transform="rotate(-38 {x + 66} 24)"><rect x="{x + 56}" y="22" width="20" height="3" rx="1.5" fill="{KIR}"/><circle cx="{x + 60}" cy="27" r="1.8" fill="{LAC}"/><circle cx="{x + 72}" cy="27" r="1.8" fill="{LAC}"/></g>'
    # 3 dev dalga
    x = 182
    ic += f'<path d="M{x + 4} 78 V58 Q{x + 22} 50 {x + 34} 30 Q{x + 48} 8 {x + 70} 26 Q{x + 56} 24 {x + 56} 40 Q{x + 58} 56 {x + 80} 58 V78 Z" fill="{SU}"/>'
    ic += f'<path d="M{x + 60} 22 q6 -2 10 4" fill="none" stroke="#fff" stroke-width="2"/><rect x="{x + 66}" y="50" width="8" height="8" fill="{KAHVE}"/><path d="M{x + 64} 50 l6 -6 l6 6 Z" fill="{KIR}"/>'
    # 4 pota ve top
    x = 271
    ic += f'<rect x="{x + 64}" y="18" width="4" height="60" fill="{SOLUK}"/><rect x="{x + 54}" y="18" width="12" height="18" fill="#fff" stroke="{SOLUK}" stroke-width="1.2"/><ellipse cx="{x + 48}" cy="36" rx="8" ry="2.4" fill="none" stroke="{KIR}" stroke-width="1.8"/>'
    ic += f'<path d="M{x + 14} 64 Q{x + 26} 8 {x + 46} 30" fill="none" stroke="{TUR}" stroke-width="1.4" stroke-dasharray="3 3"/><circle cx="{x + 14}" cy="66" r="6" fill="{TUR}" stroke="{KAHVE}" stroke-width="1"/>'
    return svg(360, 88, ic, 'Olaylar: 1 gökkuşağının oluşması, 2 kaykayın rampadan kayıp havada süzülmesi, 3 tsunaminin yayılması, 4 basketbol topunun potaya atılması', 22)


def disiplin_tablosu():
    sat = [('Güneş’in hareketleri', 'fizik, astronomi, coğrafya'), ('İklim olayları', 'fizik, coğrafya'), ('Su döngüsü', 'fizik, kimya, biyoloji, coğrafya'), ('Fotosentez', 'fizik, kimya, biyoloji')]
    ic = kutu(4, 4, 352, 100, '#fff', MAVI, 6, 1.3) + f'<rect x="4" y="4" width="352" height="20" rx="6" fill="{MAVI_A}"/>'
    ic += yazi(12, 18, 'Olay', 11.5, LAC, 'start') + yazi(140, 18, 'İnceleyen disiplinler', 11.5, LAC, 'start')
    ic += f'<line x1="132" y1="4" x2="132" y2="104" stroke="{MAVI}" stroke-width="0.8"/>'
    for k, (a, b) in enumerate(sat):
        y = 24 + k * 20
        ic += f'<line x1="4" y1="{y}" x2="356" y2="{y}" stroke="{MAVI}" stroke-width="0.8"/>' + yazi(12, y + 14, a, 11, LAC, 'start', True) + yazi(140, y + 14, b, 11, LAC, 'start', True)
    return svg(360, 108, ic, 'Tablo. Güneş’in hareketleri: fizik, astronomi, coğrafya. İklim olayları: fizik, coğrafya. Su döngüsü: fizik, kimya, biyoloji, coğrafya. Fotosentez: fizik, kimya, biyoloji.', 31)


def calgi():
    ic = f'<ellipse cx="84" cy="44" rx="56" ry="34" fill="#e6b877" stroke="{KAHVE}" stroke-width="1.6"/><circle cx="96" cy="44" r="12" fill="{KAHVE}"/>'
    ic += f'<rect x="130" y="36" width="160" height="16" fill="{KAHVE}"/><path d="M290 32 H330 a6 6 0 0 1 6 6 V50 a6 6 0 0 1 -6 6 H290 Z" fill="#6b4420"/>'
    ic += ''.join(f'<line x1="56" y1="{39 + k * 3.4:.1f}" x2="326" y2="{39 + k * 3.4:.1f}" stroke="#f7f3e8" stroke-width="0.9"/>' for k in range(4))
    ic += f'<rect x="52" y="36" width="5" height="16" fill="{LAC}"/>'
    ic += ''.join(f'<rect x="{300 + k * 14}" y="22" width="5" height="10" rx="2" fill="{GRI}" stroke="{SOLUK}" stroke-width="0.8"/><rect x="{300 + k * 14}" y="56" width="5" height="10" rx="2" fill="{GRI}" stroke="{SOLUK}" stroke-width="0.8"/>' for k in range(2))
    ic += f'<line x1="200" y1="16" x2="200" y2="38" stroke="{LAC}" stroke-width="1"/>' + rozet(200, 12, '1', LAC)
    ic += f'<line x1="330" y1="76" x2="317" y2="66" stroke="{LAC}" stroke-width="1"/>' + rozet(336, 80, '2', LAC)
    return svg(360, 92, ic, 'Telli çalgı: 1 numara tel, 2 numara akort vidası', 20)


def is_semasi():
    ad = [['Kandil', 'isi'], ['Hava', 'kanalları'], ['İs', 'odası'], None]
    ic = ''
    for i, a in enumerate(ad):
        x = 6 + i * 90
        bos = a is None
        ic += kutu(x, 6, 76, 40, '#fff' if bos else TUR_A, TUR, 8, 1.4, ' stroke-dasharray="4 3"' if bos else '')
        ic += yazi(x + 38, 32, '?', 15, TUR) if bos else ''.join(yazi(x + 38, 23 + k * 13, s, 11, LAC) for k, s in enumerate(a))
        if i < 3:
            ic += ok(x + 77, 26, x + 89, 26)
    return svg(360, 52, ic, 'Şema: kandil isi, hava kanalları, is odası, soru işareti', 12)


def tiyatro():
    ic = f'<rect x="4" y="4" width="352" height="92" rx="8" fill="{GOK}"/>'
    pts = 'M120 88 '
    for k in range(8):
        pts += f'H{148 + k * 26} V{80 - k * 9} '
    ic += f'<path d="{pts}H352 V88 Z" fill="#d9c8a9" stroke="{KAHVE}" stroke-width="1"/>'
    ic += f'<rect x="20" y="78" width="100" height="10" fill="#b79b6c" stroke="{KAHVE}" stroke-width="1"/>' + yazi(70, 72, 'Sahne', 11, LAC) + yazi(196, 24, 'Oturma alanı', 11, LAC)
    ic += ''.join(f'<path d="M{96 + r * 0.5:.1f} {62 - r * 0.87:.1f} A{r} {r} 0 0 1 {96 + r * 0.98:.1f} {62 - r * 0.17:.1f}" fill="none" stroke="{MAVI}" stroke-width="1.5"/>' for r in (12, 22, 32))
    return svg(360, 100, ic, 'Antik tiyatro kesiti: altta sahne, sahneye doğru basamak basamak eğimli oturma alanı, sahneden yayılan ses', 22)


def araclar():
    ic = kutu(4, 4, 172, 70, '#fff', GRI, 8, 1.2) + kutu(184, 4, 172, 70, '#fff', GRI, 8, 1.2)
    ic += f'<rect x="68" y="12" width="44" height="34" rx="5" fill="{LAC}"/><rect x="72" y="16" width="36" height="22" rx="2" fill="#cfe8b9"/><path d="M76 34 l10 -8 l8 5 l12 -11" fill="none" stroke="#fff" stroke-width="1.6"/><path d="M90 20 a5 5 0 0 1 10 0 c0 4 -5 9 -5 9 s-5 -5 -5 -9 Z" fill="{KIR}"/>' + yazi(90, 64, 'GPS cihazı', 11.5, LAC)
    ic += f'<path d="M258 28 a12 12 0 0 1 24 0 c0 6 -5 8 -5 13 h-14 c0 -5 -5 -7 -5 -13 Z" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.2"/><rect x="263" y="41" width="14" height="7" rx="2" fill="{SOLUK}"/>' + ''.join(f'<line x1="{270 + 17 * math.cos(a):.1f}" y1="{28 + 17 * math.sin(a):.1f}" x2="{270 + 22 * math.cos(a):.1f}" y2="{28 + 22 * math.sin(a):.1f}" stroke="{TUR}" stroke-width="1.6" stroke-linecap="round"/>' for a in (-2.6, -2.0, -1.57, -1.14, -0.54)) + yazi(270, 64, 'LED lamba', 11.5, LAC)
    return svg(360, 78, ic, 'İki araç: GPS cihazı ve LED lamba', 18)


def ornek_kartlari():
    kart = [('1', 'Gezegenlerin yörüngeleri hesaplanır.', MOR, MOR_A), ('2', 'Bitki dokusu mikroskopla görüntülenir.', YES, YES_A), ('3', 'Atom altı parçacıkların davranışı incelenir.', MAVI, MAVI_A)]
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 91, ic, 'Örnekler: 1 Gezegenlerin yörüngeleri hesaplanır. 2 Bitki dokusu mikroskopla görüntülenir. 3 Atom altı parçacıkların davranışı incelenir.', 25)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = olaylar()
    s[2]['gorsel'] = disiplin_tablosu()
    s[5]['gorsel'] = calgi()
    s[7]['gorsel'] = is_semasi()
    s[8]['gorsel'] = tiyatro()
    s[9]['gorsel'] = araclar()
    s[11]['gorsel'] = ornek_kartlari()
