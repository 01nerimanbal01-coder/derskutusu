"""5. sınıf Matematik 4. hafta (doğruların oluşturduğu açılar) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex).
Açılar matematik yönünde verilir: 0° sağ, saat yönünün tersine artar (SVG'de y aşağı olduğu için sin eksiyle)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
YOL, CIM, AGAC = '#c9d0dc', '#cdebd6', '#3f9b5a'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk=LAC, r=11, boy=13):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{renk}"/>' + yazi(x, y + boy * 0.35, metin, boy, '#fff')


def nk(cx, cy, r, aci):
    a = math.radians(aci)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def ok_ucu(x, y, dx, dy, renk, uc=10):
    n = math.hypot(dx, dy)
    dx, dy = dx / n, dy / n
    bx, by = x - uc * dx, y - uc * dy
    return (f'<path d="M{x + dx * 2:.1f} {y + dy * 2:.1f} L{bx - uc * 0.55 * dy:.1f} {by + uc * 0.55 * dx:.1f} '
            f'L{bx + uc * 0.55 * dy:.1f} {by - uc * 0.55 * dx:.1f} Z" fill="{renk}"/>')


def dogru_parca(x1, y1, x2, y2, renk, kal=2.4, kesik=False, uc=9):
    """İki ucu oklu doğru (doğrunun iki yönde sonsuza uzadığını gösterir)."""
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ex, ey = dx / n * (uc - 2), dy / n * (uc - 2)
    k = ' stroke-dasharray="7 5"' if kesik else ''
    s = f'<line x1="{x1 + ex:.1f}" y1="{y1 + ey:.1f}" x2="{x2 - ex:.1f}" y2="{y2 - ey:.1f}" stroke="{renk}" stroke-width="{kal}" stroke-linecap="round"{k}/>'
    return s + ok_ucu(x2, y2, dx, dy, renk, uc) + ok_ucu(x1, y1, -dx, -dy, renk, uc)


def dogru(cx, cy, aci, uz, renk, kal=2.4, kesik=False, uc=9):
    x1, y1 = nk(cx, cy, uz, aci + 180)
    x2, y2 = nk(cx, cy, uz, aci)
    return dogru_parca(x1, y1, x2, y2, renk, kal, kesik, uc)


def yay(cx, cy, r, a1, a2, renk, dolgu=None, kal=2):
    """a1'den a2'ye (saat yönünün tersine) açı yayı; dolgu verilirse daire dilimi."""
    x1, y1 = nk(cx, cy, r, a1)
    x2, y2 = nk(cx, cy, r, a2)
    buyuk = 1 if (a2 - a1) % 360 > 180 else 0
    s = ''
    if dolgu:
        s += f'<path d="M{cx:.1f} {cy:.1f} L{x1:.1f} {y1:.1f} A{r} {r} 0 {buyuk} 0 {x2:.1f} {y2:.1f} Z" fill="{dolgu}" stroke="none"/>'
    return s + f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {buyuk} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{renk}" stroke-width="{kal}"/>'


def dik_isareti(cx, cy, a1, boy, renk, kal=1.8):
    ux, uy = nk(0, 0, boy, a1)
    vx, vy = nk(0, 0, boy, a1 + 90)
    return (f'<path d="M{cx + ux:.1f} {cy + uy:.1f} L{cx + ux + vx:.1f} {cy + uy + vy:.1f} L{cx + vx:.1f} {cy + vy:.1f}" '
            f'fill="none" stroke="{renk}" stroke-width="{kal}"/>')


def etiket_kutu(x, y, metin, renk, boy=14, gen=None):
    g = gen or (len(metin) * boy * 0.62 + 10)
    return (f'<rect x="{x - g / 2:.1f}" y="{y - boy * 0.85:.1f}" width="{g:.1f}" height="{boy * 1.3:.1f}" rx="4" fill="#fff" stroke="{renk}" stroke-width="1.2"/>'
            + yazi(x, y + boy * 0.1, metin, boy, renk))


def kagit(x, y, w, h, dolgu='#fff'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{dolgu}" stroke="{GRI}" stroke-width="1.4"/>'
            f'<path d="M{x + w - 16} {y} L{x + w} {y + 16} L{x + w - 16} {y + 16} Z" fill="{GRI_A}" stroke="{GRI}" stroke-width="1"/>')


def dogru_ciftleri():
    ciftler = [((20, 40, 180, 120), (20, 115, 180, 45)),
               ((20, 55, 180, 85), (20, 95, 180, 125)),
               ((20, 40, 180, 70), (20, 120, 180, 95))]
    ic = ''
    for i, (a, b) in enumerate(ciftler):
        x0 = 5 + i * 200
        ic += kagit(x0, 5, 190, 140)
        ic += f'<g transform="translate({x0} 5)">'
        ic += dogru_parca(*a, MAVI) + dogru_parca(*b, TUR)
        ic += '</g>' + rozet(x0 + 16, 21, str(i + 1))
    return svg(600, 150, ic, 'Üç kâğıtta birer doğru çifti. 1. kâğıtta doğrular kâğıdın içinde kesişiyor. 2. kâğıtta doğrular aynı eğimle uzanıyor, aralarındaki uzaklık değişmiyor. 3. kâğıtta doğrular sağa doğru birbirine yaklaşıyor ama kâğıdın içinde kesişmiyor.', 24)


def kavsak():
    cx, cy = 220, 120
    ic = '<defs><clipPath id="m4-kavsak"><rect x="4" y="4" width="432" height="222" rx="10"/></clipPath></defs>'
    ic += f'<rect x="4" y="4" width="432" height="222" rx="10" fill="#f7f9fc" stroke="{GRI}" stroke-width="1.4"/>'
    ic += '<g clip-path="url(#m4-kavsak)">'
    # park (sağ üst bölge)
    ic += f'<path d="M265 88 L302 4 L436 4 L436 88 Z" fill="{CIM}"/>'
    for x, y in [(330, 30), (365, 52), (400, 28), (318, 68), (410, 66)]:
        ic += f'<circle cx="{x}" cy="{y}" r="11" fill="{AGAC}"/><circle cx="{x - 3}" cy="{y - 3}" r="4" fill="#6cc187"/>'
    ic += yazi(372, 82, 'Park', 13, '#1f6b3a')
    # yollar
    ic += f'<rect x="0" y="{cy - 22}" width="440" height="44" fill="{YOL}"/>'
    ic += f'<g transform="rotate(-65 {cx} {cy})"><rect x="{cx - 230}" y="{cy - 22}" width="460" height="44" fill="{YOL}"/>'
    ic += f'<line x1="{cx - 230}" y1="{cy}" x2="{cx + 230}" y2="{cy}" stroke="#fff" stroke-width="2.6" stroke-dasharray="12 9"/></g>'
    ic += f'<line x1="0" y1="{cy}" x2="440" y2="{cy}" stroke="#fff" stroke-width="2.6" stroke-dasharray="12 9"/>'
    ic += '</g>'
    # fırın (sol alt) ve eczane (sol üst)
    ic += f'<rect x="58" y="162" width="78" height="52" rx="3" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += f'<path d="M54 162 L140 162 L134 150 L60 150 Z" fill="{TUR}"/>'
    ic += yazi(97, 182, 'Fırın', 13, '#9a4a00')
    ic += f'<rect x="70" y="190" width="18" height="24" fill="#fff" stroke="{TUR}" stroke-width="1.2"/><rect x="100" y="190" width="24" height="14" fill="#fff" stroke="{TUR}" stroke-width="1.2"/>'
    ic += f'<rect x="62" y="22" width="86" height="56" rx="3" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<rect x="96" y="12" width="18" height="18" rx="2" fill="#fff" stroke="{YES}" stroke-width="1.6"/>'
    ic += f'<path d="M105 15 V27 M99 21 H111" stroke="{YES}" stroke-width="3"/>'
    ic += yazi(105, 50, 'Eczane', 13, '#16348f')
    ic += f'<rect x="74" y="58" width="18" height="20" fill="#fff" stroke="{MAVI}" stroke-width="1.2"/><rect x="104" y="58" width="32" height="12" fill="#fff" stroke="{MAVI}" stroke-width="1.2"/>'
    # açılar
    ic += yay(cx, cy, 34, 0, 65, YES, '#12a15033', 2.4)
    ic += etiket_kutu(*nk(cx, cy, 60, 32.5), '65°', YES, 14)
    ic += yay(cx, cy, 30, 65, 180, MAVI, '#2451d62e', 2.4)
    ic += etiket_kutu(*nk(cx, cy, 52, 122.5), '?', MAVI, 14, 22)
    ic += yay(cx, cy, 34, 180, 245, TUR, '#ee7d1233', 2.4)
    ic += etiket_kutu(*nk(cx, cy, 58, 212.5), '?', TUR, 14, 22)
    ic += f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{LAC}"/>'
    return svg(440, 230, ic, 'Kavşak: yatay bir cadde ile ona 65° eğimli ikinci cadde kesişiyor. Orta çizgiler arasındaki sağ üst açı 65°; bu bölgede park var. Sol üst bölgedeki eczanenin köşesindeki açı ve sol alt bölgedeki fırının köşesindeki açı soru işaretiyle gösterilmiş.', 40)


def rt_su():
    cx, cy = 180, 100
    ic = dogru(cx, cy, 165, 165, MAVI) + dogru(cx, cy, 50, 100, TUR)
    for aci, r, ad, renk in [(165, 130, 'R', MAVI), (345, 130, 'T', MAVI), (230, 85, 'S', TUR), (50, 85, 'U', TUR)]:
        x, y = nk(cx, cy, r, aci)
        ic += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{renk}"/>'
        lx, ly = nk(x, y, 15, aci + 90)
        ic += yazi(lx, ly + 5, ad, 16, renk)
    ic += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{LAC}"/>' + yazi(cx + 4, cy + 22, 'O', 16, LAC)
    return svg(360, 200, ic, 'RT doğrusu ile SU doğrusu O noktasında kesişiyor. R sol üstte, T sağ altta; S sol altta, U sağ üstte.', 34)


def uc_dogru_cizimleri():
    cizimler = [(0, 25, 55), (0, 40, 90), (0, 60, 120)]
    renkler = (MAVI, TUR, YES)
    ic = ''
    for i, acilar in enumerate(cizimler):
        x0 = 5 + i * 200
        ic += f'<rect x="{x0}" y="5" width="190" height="140" rx="8" fill="#fbfcfe" stroke="{GRI}" stroke-width="1.2"/>'
        cx, cy = x0 + 95, 75
        for a, renk in zip(acilar, renkler):
            ic += dogru(cx, cy, a, 62, renk, 2.2)
        if acilar[2] == 90:
            ic += dik_isareti(cx, cy, 90, 12, KIR) + dik_isareti(cx, cy, 270, 12, KIR)
        ic += f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="{LAC}"/>'
        ic += rozet(x0 + 17, 21, str(i + 1))
    return svg(600, 150, ic, 'Üç çizim; her birinde üç doğru aynı noktada kesişiyor. 1. çizim: doğrular yatayla 0°, 25° ve 55° yapıyor. 2. çizim: 0°, 40° ve 90°; yatay ile dikey doğru arasında dik açı işaretleri var. 3. çizim: 0°, 60° ve 120°.', 24)


def ucgen_park():
    A, B, C = (110, 170), (110, 60), (330, 170)
    ic = '<defs><clipPath id="m4-park"><rect x="4" y="4" width="432" height="212" rx="10"/></clipPath></defs>'
    ic += f'<rect x="4" y="4" width="432" height="212" rx="10" fill="#f7f9fc" stroke="{GRI}" stroke-width="1.4"/>'
    ic += '<g clip-path="url(#m4-park)">'
    ic += f'<path d="M{B[0]} {B[1]} L{A[0]} {A[1]} L{C[0]} {C[1]} Z" fill="{CIM}" stroke="#7cc596" stroke-width="1.5"/>'
    for x, y in [(140, 145), (168, 152), (138, 118), (200, 156), (162, 128), (232, 158)]:
        ic += f'<circle cx="{x}" cy="{y}" r="8" fill="{AGAC}"/><circle cx="{x - 2}" cy="{y - 2}" r="3" fill="#6cc187"/>'
    for (x1, y1, x2, y2) in [(0, 170, 440, 170), (110, 0, 110, 220), (0, 5, 440, 225)]:
        ic += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YOL}" stroke-width="18"/>'
        ic += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#fff" stroke-width="1.8" stroke-dasharray="9 7"/>'
    ic += '</g>'
    ic += dik_isareti(A[0], A[1], 0, 14, KIR, 2.2)
    for x, y in (A, B, C):
        ic += f'<circle cx="{x}" cy="{y}" r="3.5" fill="{LAC}"/>'
    ic += yazi(196, 150, 'Park', 13, '#1f6b3a')
    return svg(440, 220, ic, 'Üç düz yol ikişer ikişer kesişerek üçgen biçimli bir parkı çevreliyor: yatay yol, dikey yol ve eğik yol. Yatay ve dikey yolun kesiştiği köşede park tarafında dik açı işareti var.', 36)


def paralel_kesen():
    L, U = (170, 150), (226, 60)
    aci = math.degrees(math.atan2(L[1] - U[1], U[0] - L[0]))  # kesenin yatayla açısı ≈ 58°
    ic = dogru_parca(20, 60, 420, 60, MAVI) + dogru_parca(20, 150, 420, 150, MAVI)
    x1, y1 = L[0] - 40 * (56 / 90), 190
    x2, y2 = U[0] + 45 * (56 / 90), 15
    ic += dogru_parca(x1, y1, x2, y2, TUR)
    ic += yay(U[0], U[1], 26, 0, aci, YES, '#12a15030', 2.2) + yazi(*nk(U[0] + 2, U[1] + 6, 46, aci / 2), '58°', 15, YES)
    ic += yay(U[0], U[1], 20, aci, 180, MOR, '#7c3aed26', 2.2) + yazi(*nk(U[0], U[1] + 6, 36, (aci + 180) / 2), '1', 16, MOR)
    ic += yay(L[0], L[1], 26, 0, aci, KIR, '#d63a3a26', 2.2) + yazi(*nk(L[0] + 2, L[1] + 6, 44, aci / 2), '2', 16, KIR)
    ic += yay(L[0], L[1], 20, aci + 180, 360, MAVI, '#2451d626', 2.2) + yazi(*nk(L[0], L[1] + 6, 36, (aci + 540) / 2), '3', 16, MAVI)
    ic += f'<circle cx="{U[0]}" cy="{U[1]}" r="3.2" fill="{LAC}"/><circle cx="{L[0]}" cy="{L[1]}" r="3.2" fill="{LAC}"/>'
    ic += yazi(428, 66, 'd<tspan font-size="11" dy="4">1</tspan>', 16, MAVI, 'start')
    ic += yazi(428, 156, 'd<tspan font-size="11" dy="4">2</tspan>', 16, MAVI, 'start')
    ic += yazi(x2 + 12, y2 + 8, 'k', 16, TUR, 'start')
    return svg(440, 200, ic, 'Paralel d1 ve d2 doğrularını k doğrusu kesiyor. Üst kesişimde sağ üstteki açı 58°, sol üstteki açı 1 numaralı. Alt kesişimde sağ üstteki açı 2, sağ alttaki açı 3 numaralı.', 34)


def ece_karti():
    cx, cy = 150, 95
    ic = dogru(cx, cy, 0, 130, MAVI) + dogru(cx, cy, 48, 120, TUR)
    for no, (a1, a2), r in [(1, (0, 48), 30), (2, (48, 180), 24), (3, (180, 228), 30), (4, (228, 360), 24)]:
        renk = (YES, MOR, YES, MOR)[no - 1]
        ic += yay(cx, cy, r, a1, a2, renk, None, 2)
        ic += rozet(*nk(cx, cy, r + 22, (a1 + a2) / 2), str(no), renk, 10, 12)
    ic += f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{LAC}"/>'
    x0, y0 = 330, 14
    ic += f'<rect x="{x0}" y="{y0}" width="250" height="164" rx="10" fill="#fffbe6" stroke="#d9b84a" stroke-width="1.8"/>'
    ic += f'<rect x="{x0}" y="{y0}" width="250" height="34" rx="10" fill="#f3e3a6"/><rect x="{x0}" y="{y0 + 24}" width="250" height="10" fill="#f3e3a6"/>'
    ic += yazi(x0 + 125, y0 + 23, 'Ece’nin ölçümleri', 15, '#8a6d12')
    for k, deger in enumerate(['48°', '132°', '48°', '122°']):
        y = y0 + 60 + k * 30
        ic += yazi(x0 + 24, y, f'{k + 1}. açı', 15, LAC, 'start', ince=True)
        ic += f'<line x1="{x0 + 92}" y1="{y - 4}" x2="{x0 + 180}" y2="{y - 4}" stroke="#d9b84a" stroke-width="1.2" stroke-dasharray="2 4"/>'
        ic += yazi(x0 + 226, y, deger, 17, LAC, 'end')
    return svg(600, 190, ic, 'Kesişen iki doğru dört açı oluşturuyor: 1 ve 3 numaralı açılar dar, 2 ve 4 numaralı açılar geniş. Ece’nin ölçümleri kartı: 1. açı 48°, 2. açı 132°, 3. açı 48°, 4. açı 122°.', 30)


def tumler_kartlari():
    kartlar = [('30°', '60°', '150°', MAVI, MAVI_A), ('70°', '20°', '110°', TUR, TUR_A), ('45°', '45°', '135°', YES, YES_A)]
    ic = ''
    for i, (aci, tum, but, renk, acik) in enumerate(kartlar):
        x = 5 + i * 200
        ic += f'<rect x="{x}" y="5" width="190" height="110" rx="10" fill="{acik}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="5" width="190" height="34" rx="10" fill="{renk}"/><rect x="{x}" y="29" width="190" height="10" fill="{renk}"/>'
        ic += yazi(x + 95, 29, f'Açı: {aci}', 17, '#fff')
        ic += yazi(x + 16, 68, 'Tümleri', 15, LAC, 'start', ince=True) + yazi(x + 174, 68, tum, 17, LAC, 'end')
        ic += f'<line x1="{x + 12}" y1="80" x2="{x + 178}" y2="80" stroke="{renk}" stroke-width="1" opacity="0.5"/>'
        ic += yazi(x + 16, 102, 'Bütünleri', 15, LAC, 'start', ince=True) + yazi(x + 174, 102, but, 17, LAC, 'end')
    return svg(600, 120, ic, 'Üç kart. Açı 30°: tümleri 60°, bütünleri 150°. Açı 70°: tümleri 20°, bütünleri 110°. Açı 45°: tümleri 45°, bütünleri 135°.', 20)


def makas():
    px, py = 285, 85
    ic = ''
    # parçaların üzerinden geçen doğrular (kesik)
    for a in (20, -20):
        x1, y1 = nk(px, py, 175, a + 180)
        x2, y2 = nk(px, py, 215, a)
        ic += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{MOR}" stroke-width="1.6" stroke-dasharray="7 5"/>'
    # ağızlar
    for a, dis in ((20, 1), (-20, -1)):
        n = a + 90 * dis
        p = lambda r, k: nk(*nk(px, py, r, a), k, n)
        noktalar = [p(-12, 8), p(150, 6), nk(px, py, 194, a), p(150, -1.5), p(-12, -6)]
        d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in noktalar) + ' Z'
        ic += f'<path d="{d}" fill="#c5ccd8" stroke="#5f6a7d" stroke-width="1.4" stroke-linejoin="round"/>'
    # saplar: üst ağız (+20°) alttaki sapla (200°), alt ağız (-20°) üstteki sapla (160°) aynı parçadır
    for a, renk in ((200, TUR), (160, MAVI)):
        x1, y1 = nk(px, py, 10, a)
        x2, y2 = nk(px, py, 104, a)
        ic += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{renk}" stroke-width="10" stroke-linecap="round"/>'
        hx, hy = nk(px, py, 130, a)
        ic += f'<ellipse cx="{hx:.1f}" cy="{hy:.1f}" rx="27" ry="17" transform="rotate({-a:.1f} {hx:.1f} {hy:.1f})" fill="none" stroke="{renk}" stroke-width="7"/>'
    ic += f'<circle cx="{px}" cy="{py}" r="7" fill="#8b95a8" stroke="{LAC}" stroke-width="1.5"/><circle cx="{px}" cy="{py}" r="2.2" fill="{LAC}"/>'
    ic += yay(px, py, 62, 160, 200, KIR, '#d63a3a22', 2.2) + etiket_kutu(*nk(px, py, 86, 180), '40°', KIR, 14)
    ic += yay(px, py, 62, -20, 20, KIR, '#d63a3a22', 2.2) + etiket_kutu(*nk(px, py, 86, 0), '?', KIR, 14, 22)
    return svg(600, 170, ic, 'Açık bir makas: perçin noktasında iki parça kesişiyor. Her parçanın üzerinden kesik çizgiyle bir doğru geçiyor. Sapların arasındaki açı 40°, ağızların arasındaki açı soru işaretiyle gösterilmiş.', 28)


def seffaf_kagit():
    eg = 56 / 90  # kesenin y'deki her birim için x kayması
    ic = yazi(140, 18, '1. Çiz ve kes', 14, LAC) + yazi(445, 18, '2. Kesişim noktalarını üst üste getir', 14, LAC)
    # 1. adım: bütün kâğıt
    ic += f'<rect x="30" y="30" width="220" height="90" fill="{MAVI_A}"/><rect x="30" y="120" width="220" height="90" fill="{TUR_A}"/>'
    ic += f'<rect x="30" y="30" width="220" height="180" rx="3" fill="none" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<line x1="30" y1="75" x2="250" y2="75" stroke="{MAVI}" stroke-width="2.4"/><line x1="30" y1="165" x2="250" y2="165" stroke="{TUR}" stroke-width="2.4"/>'
    kx = lambda y: 120 + (165 - y) * eg
    ic += f'<line x1="{kx(30):.1f}" y1="30" x2="{kx(120):.1f}" y2="120" stroke="{MAVI}" stroke-width="2.4"/>'
    ic += f'<line x1="{kx(120):.1f}" y1="120" x2="{kx(210):.1f}" y2="210" stroke="{TUR}" stroke-width="2.4"/>'
    ic += f'<line x1="26" y1="120" x2="254" y2="120" stroke="{KIR}" stroke-width="2" stroke-dasharray="8 5"/>'
    ic += yazi(246, 114, 'kesme çizgisi', 11, KIR, 'end')
    ic += f'<circle cx="176" cy="75" r="3.2" fill="{LAC}"/><circle cx="120" cy="165" r="3.2" fill="{LAC}"/>'
    ic += f'<line x1="262" y1="120" x2="292" y2="120" stroke="{LAC}" stroke-width="2.4"/>' + ok_ucu(300, 120, 1, 0, LAC)
    # 2. adım: parçalar üst üste (alt parça önce, üst parça yarı saydam üstte)
    cx, cy = 450, 120
    ic += f'<rect x="360" y="75" width="220" height="90" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.2"/>'
    ic += f'<rect x="304" y="75" width="220" height="90" fill="{MAVI_A}" fill-opacity="0.72" stroke="{MAVI}" stroke-width="1.2"/>'
    aci = math.degrees(math.atan2(90, 56))
    ic += yay(cx, cy, 24, 0, aci, YES, '#12a15040', 2.2) + yay(cx, cy, 24, 180, 180 + aci, YES, '#12a15040', 2.2)
    ic += yay(cx, cy, 18, aci, 180, MOR, '#7c3aed33', 2.2) + yay(cx, cy, 18, 180 + aci, 360, MOR, '#7c3aed33', 2.2)
    # üst parçanın çizgileri (düz, mavi): d1 ve kesenin üst kısmı
    ic += f'<line x1="304" y1="{cy}" x2="524" y2="{cy}" stroke="{MAVI}" stroke-width="2.4"/>'
    ic += f'<line x1="{cx - 45 * eg:.1f}" y1="165" x2="{cx + 45 * eg:.1f}" y2="75" stroke="{MAVI}" stroke-width="2.4"/>'
    # alt parçanın çizgileri (kesik, turuncu): d2 ve kesenin alt kısmı
    ic += f'<line x1="360" y1="{cy}" x2="580" y2="{cy}" stroke="{TUR}" stroke-width="2.4" stroke-dasharray="7 5"/>'
    ic += f'<line x1="{cx - 45 * eg:.1f}" y1="165" x2="{cx + 45 * eg:.1f}" y2="75" stroke="{TUR}" stroke-width="2.4" stroke-dasharray="7 5"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{LAC}"/>'
    ic += f'<rect x="320" y="182" width="12" height="12" rx="2" fill="#12a15040" stroke="{YES}" stroke-width="1.6"/>' + yazi(338, 193, 'dar açılar', 12, LAC, 'start', ince=True)
    ic += f'<rect x="440" y="182" width="12" height="12" rx="2" fill="#7c3aed33" stroke="{MOR}" stroke-width="1.6"/>' + yazi(458, 193, 'geniş açılar', 12, LAC, 'start', ince=True)
    return svg(600, 216, ic, '1. adım: şeffaf kâğıtta paralel iki doğru ve onları kesen doğru çizilmiş; kâğıt iki paralel doğrunun arasından kesilecek. 2. adım: iki parça, kesişim noktaları üst üste gelecek biçimde konmuş; üst parçanın doğruları alt parçanınkilerle çakışıyor; dar açılar dar açıların, geniş açılar geniş açıların üzerine geliyor.', 34)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dogru_ciftleri()
    s[3]['gorsel'] = kavsak()
    s[4]['gorsel'] = rt_su()
    s[5]['gorsel'] = uc_dogru_cizimleri()
    s[6]['gorsel'] = ucgen_park()
    s[7]['gorsel'] = paralel_kesen()
    s[8]['gorsel'] = ece_karti()
    s[9]['gorsel'] = tumler_kartlari()
    s[10]['gorsel'] = makas()
    s[11]['gorsel'] = seffaf_kagit()
