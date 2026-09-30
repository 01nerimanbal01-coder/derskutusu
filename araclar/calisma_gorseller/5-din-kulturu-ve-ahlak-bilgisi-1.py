"""5. sınıf Din Kültürü ve Ahlak Bilgisi 1. hafta (evrendeki mükemmel düzen) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def ok(x1, y1, x2, y2, renk=GRI, kalin=2):
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2:.1f},{y2:.1f} {x2 - 7 * math.cos(a - 0.45):.1f},{y2 - 7 * math.sin(a - 0.45):.1f} {x2 - 7 * math.cos(a + 0.45):.1f},{y2 - 7 * math.sin(a + 0.45):.1f}'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/><polygon points="{u}" fill="{renk}"/>'


def bulut(x, y, s=1, renk='#c9d3e3'):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="-14" cy="4" r="10" fill="{renk}"/><circle cx="0" cy="-2" r="13" fill="{renk}"/>'
            f'<circle cx="15" cy="4" r="10" fill="{renk}"/><rect x="-24" y="4" width="48" height="10" rx="5" fill="{renk}"/></g>')


def su_ihtiyaci():
    """1: yağmur kuru toprağa yağıyor, 2: su şişesinden bardağa su dolduruluyor."""
    ic = kutu(4, 4, 172, 112, CAM_A, CAM, 8, 1.2) + kutu(184, 4, 172, 112, MAVI_A, MAVI, 8, 1.2)
    ic += bulut(90, 28, 1.3)
    ic += ''.join(f'<line x1="{66 + k * 12}" y1="{50 + (k % 2) * 6}" x2="{62 + k * 12}" y2="{62 + (k % 2) * 6}" stroke="#5aa9e6" stroke-width="2" stroke-linecap="round"/>' for k in range(5))
    ic += f'<rect x="14" y="86" width="152" height="24" rx="4" fill="#d9b98f"/>'
    ic += ''.join(f'<path d="M{30 + k * 34} 90 l6 8 l-4 6 l7 5" fill="none" stroke="{KAHVE}" stroke-width="1.1"/>' for k in range(4))
    ic += f'<path d="M122 86 v-14" stroke="{YES}" stroke-width="2"/><path d="M122 76 q-8 -2 -10 -9 q8 1 10 9 M122 80 q8 -2 10 -9 q-8 1 -10 9" fill="{YES}"/>'
    # şişe ve bardak
    ic += (f'<g transform="rotate(-40 250 40)"><rect x="238" y="22" width="24" height="46" rx="6" fill="#bfe3f5" stroke="{MAVI}" stroke-width="1.4"/>'
           f'<rect x="244" y="12" width="12" height="11" rx="2" fill="{MAVI}"/></g>')
    ic += f'<path d="M226 56 q3 20 4 32" fill="none" stroke="#5aa9e6" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<path d="M212 72 L220 110 H248 L256 72 Z" fill="#fff" stroke="{GRI}" stroke-width="1.4"/><path d="M216 92 L220 110 H248 L252 92 Z" fill="#7cc3f0"/>'
    ic += f'<circle cx="18" cy="18" r="9" fill="{CAM}"/>' + yazi(18, 22, '1', 11, '#fff')
    ic += f'<circle cx="198" cy="18" r="9" fill="{MAVI}"/>' + yazi(198, 22, '2', 11, '#fff')
    return svg(360, 120, ic, '1: Yağmur bulutundan kurumuş toprağa ve küçük bir bitkiye yağmur yağıyor. 2: Su şişesinden boş bir bardağa su dolduruluyor.', 27)


def cicek(cx, cy, desen):
    ic = ''.join(f'<ellipse cx="{cx + 20 * math.cos(k * math.pi / 3):.1f}" cy="{cy + 20 * math.sin(k * math.pi / 3):.1f}" rx="14" ry="10" fill="{ALTIN}" '
                 f'transform="rotate({k * 60} {cx + 20 * math.cos(k * math.pi / 3):.1f} {cy + 20 * math.sin(k * math.pi / 3):.1f})"/>' for k in range(6))
    if desen:
        ic += ''.join(f'<line x1="{cx + 9 * math.cos(k * math.pi / 3):.1f}" y1="{cy + 9 * math.sin(k * math.pi / 3):.1f}" x2="{cx + 26 * math.cos(k * math.pi / 3):.1f}" y2="{cy + 26 * math.sin(k * math.pi / 3):.1f}" stroke="{MOR}" stroke-width="3" stroke-linecap="round"/>' for k in range(6))
        ic += f'<circle cx="{cx}" cy="{cy}" r="13" fill="{MOR}" opacity="0.85"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="8" fill="#e08a00"/>'
    return ic


def ari_cicek():
    ic = kutu(4, 4, 172, 116, '#fff', GRI, 8, 1.2) + kutu(184, 4, 172, 116, MOR_A, MOR, 8, 1.2)
    ic += cicek(90, 58, False) + cicek(270, 58, True)
    ic += yazi(90, 110, 'İnsanın gördüğü', 11.5, LAC) + yazi(270, 110, 'Arının gördüğü', 11.5, MOR)
    return svg(360, 124, ic, 'Aynı çiçek: insanın gördüğü sarı çiçek; arının gördüğü, ortasında ve yapraklarında insanın göremediği mor desenler bulunan çiçek', 26)


def gunes_yolu():
    ic = ''
    for i, gun in enumerate(['Pazartesi', 'Salı', 'Çarşamba']):
        x0 = 4 + i * 119
        ic += kutu(x0, 4, 114, 100, CAM_A, CAM, 8, 1.2)
        ic += f'<rect x="{x0 + 1}" y="74" width="112" height="29" rx="7" fill="#bfe6c9"/>'
        ic += f'<path d="M{x0 + 14} 74 Q{x0 + 57} -2 {x0 + 100} 74" fill="none" stroke="{TUR}" stroke-width="1.6" stroke-dasharray="4 3"/>'
        for t, r in [(0.08, 6), (0.5, 8), (0.92, 6)]:
            bx = (1 - t) ** 2 * (x0 + 14) + 2 * (1 - t) * t * (x0 + 57) + t * t * (x0 + 100)
            by = (1 - t) ** 2 * 74 + 2 * (1 - t) * t * -2 + t * t * 74
            ic += f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{r}" fill="{ALTIN}"/>'
        ic += yazi(x0 + 57, 18, gun, 11, LAC) + yazi(x0 + 12, 92, 'Doğu', 10, SOLUK, 'start', True) + yazi(x0 + 102, 92, 'Batı', 10, SOLUK, 'end', True)
    return svg(360, 108, ic, 'Pazartesi, salı ve çarşamba günleri Güneş’in yolu: her gün doğudan doğup gökyüzünde yay çizerek batıdan batıyor', 24)


def toprak():
    ic = f'<rect x="4" y="78" width="352" height="28" rx="6" fill="#d9b98f"/>'
    # tohum
    ic += f'<ellipse cx="40" cy="90" rx="7" ry="4.5" fill="{KAHVE}"/>'
    # fidan
    ic += f'<path d="M126 90 V66" stroke="{YES}" stroke-width="2.4"/><path d="M126 70 q-12 -2 -14 -12 q11 1 14 12 M126 74 q12 -2 14 -12 q-11 1 -14 12" fill="{YES}"/>'
    # ağaç
    ic += f'<rect x="210" y="46" width="10" height="36" fill="{KAHVE}"/><circle cx="215" cy="36" r="22" fill="{YES}"/><circle cx="200" cy="46" r="12" fill="#0f8a44"/><circle cx="230" cy="46" r="12" fill="#0f8a44"/>'
    # meyve veren ağaç
    ic += f'<rect x="306" y="46" width="10" height="36" fill="{KAHVE}"/><circle cx="311" cy="36" r="22" fill="{YES}"/><circle cx="296" cy="46" r="12" fill="#0f8a44"/><circle cx="326" cy="46" r="12" fill="#0f8a44"/>'
    ic += ''.join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{KIR}"/>' for x, y in [(300, 28), (318, 22), (324, 42), (296, 46), (312, 40)])
    ic += ok(56, 82, 104, 82) + ok(146, 62, 182, 50) + ok(246, 50, 280, 50)
    ic += yazi(40, 70, 'Tohum', 11, LAC) + yazi(126, 50, 'Fidan', 11, LAC) + yazi(215, 8, 'Ağaç', 11, LAC) + yazi(311, 8, 'Meyve', 11, LAC)
    return svg(360, 110, ic, 'Aşamalar: topraktaki tohum, fidan, ağaç, meyve veren ağaç', 23)


def sepet():
    ic = kutu(4, 4, 352, 104, YES_A, YES, 8, 1.2)
    renk = ['#f17aa0', ALTIN, MOR, KIR, '#f17aa0', ALTIN, MOR, KIR, '#f17aa0', ALTIN]
    for k in range(10):
        x, y = 22 + k * 20 + (k % 2) * 6, 70 + (k % 3) * 10
        if x > 212:
            x += 110
        ic += f'<path d="M{x} {y} v18" stroke="{YES}" stroke-width="1.6"/><circle cx="{x}" cy="{y}" r="5" fill="{renk[k]}"/><circle cx="{x}" cy="{y}" r="1.8" fill="#fff"/>'
    ic += ''.join(f'<path d="M{x} {y} v12" stroke="{YES}" stroke-width="1.4"/><circle cx="{x}" cy="{y}" r="4" fill="{c}"/>' for x, y, c in [(40, 40, ALTIN), (90, 34, '#f17aa0'), (320, 40, MOR), (190, 36, KIR)])
    # boş sepet
    ic += (f'<path d="M232 60 H300 L292 96 H240 Z" fill="#c98a4a" stroke="{KAHVE}" stroke-width="1.4"/>'
           f'<path d="M238 60 Q266 22 294 60" fill="none" stroke="{KAHVE}" stroke-width="3"/>'
           + ''.join(f'<line x1="{236 + k * 8}" y1="62" x2="{242 + k * 7}" y2="94" stroke="{KAHVE}" stroke-width="0.8"/>' for k in range(8))
           + f'<ellipse cx="266" cy="61" rx="34" ry="4" fill="#8a5a2b" opacity="0.5"/>')
    return svg(360, 112, ic, 'Çiçeklerle dolu bir çayır ve içi boş bir sepet', 23)


def agac(cx, mevsim):
    ic = f'<rect x="{cx - 4}" y="56" width="8" height="30" fill="{KAHVE}"/>'
    if mevsim == 'kış':
        ic += (f'<path d="M{cx} 60 L{cx - 16} 38 M{cx} 56 L{cx + 16} 34 M{cx} 50 L{cx} 26 M{cx - 9} 48 L{cx - 20} 44 M{cx + 9} 45 L{cx + 20} 42" stroke="{KAHVE}" stroke-width="2.4" stroke-linecap="round"/>'
               + ''.join(f'<circle cx="{cx + dx}" cy="{dy}" r="2" fill="#fff" stroke="{GRI}" stroke-width="0.6"/>' for dx, dy in [(-22, 30), (18, 24), (-6, 18), (24, 52), (-26, 60)]))
        return ic
    renk = {'ilkbahar': '#7fd08f', 'yaz': YES, 'sonbahar': TUR}[mevsim]
    ic += f'<circle cx="{cx}" cy="38" r="22" fill="{renk}"/>'
    if mevsim == 'ilkbahar':
        ic += ''.join(f'<circle cx="{cx + dx}" cy="{38 + dy}" r="3" fill="#f7b6c8"/>' for dx, dy in [(-10, -8), (6, -12), (12, 4), (-4, 8), (-14, 6), (2, -2)])
    if mevsim == 'sonbahar':
        ic += ''.join(f'<ellipse cx="{cx + dx}" cy="{dy}" rx="3" ry="1.8" fill="{TUR}"/>' for dx, dy in [(-20, 80), (16, 82), (26, 70)])
    return ic


def mevsimler():
    ic = ''
    ad = ['İlkbahar', 'Yaz', 'Sonbahar', 'Kış']
    acik = [YES_A, '#d7f0dc', TUR_A, MAVI_A]
    for i, m in enumerate(['ilkbahar', 'yaz', 'sonbahar', 'kış']):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 80, 100, acik[i], GRI, 8, 1) + agac(x0 + 40, m) + yazi(x0 + 40, 98, ad[i], 11, LAC)
        if i < 3:
            ic += ok(x0 + 80, 54, x0 + 89, 54, SOLUK, 1.6)
    ic += f'<path d="M324 106 Q180 132 36 106" fill="none" stroke="{SOLUK}" stroke-width="1.6" stroke-dasharray="4 3"/>' + ok(44, 108.5, 36, 106, SOLUK, 1.6)
    return svg(360, 124, ic, 'Bir ağacın bir yıllık görünümleri: ilkbaharda çiçekli, yazın yemyeşil, sonbaharda yaprakları turuncu ve dökülüyor, kışın yapraksız ve karlı; sonra yeniden ilkbahar', 26)


def uygula(o):
    s = o['sorular']
    s[3]['gorsel'] = su_ihtiyaci()
    s[5]['gorsel'] = ari_cicek()
    s[6]['gorsel'] = gunes_yolu()
    s[7]['gorsel'] = toprak()
    s[8]['gorsel'] = sepet()
    s[9]['gorsel'] = mevsimler()
