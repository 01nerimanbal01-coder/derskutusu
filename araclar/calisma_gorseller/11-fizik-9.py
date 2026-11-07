"""11. sınıf Fizik 9. hafta görselleri: sürtünme düzenekleri ve f–F grafikleri (SVG; insan figürü yok)."""
LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe'
GRI, GRI_A, SOLUK, KAHVE, KAHVE_A = '#9aa6bd', '#f3f5f9', '#5b6479', '#8a5a2b', '#f3e3cf'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def alt(m):
    return f'<tspan baseline-shift="sub" font-size="72%">{m}</tspan>'


def zemin(x1, x2, y):
    ic = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{LAC}" stroke-width="1.8"/>'
    for x in range(x1 + 4, x2, 12):
        ic += f'<line x1="{x}" y1="{y + 1}" x2="{x - 8}" y2="{y + 9}" stroke="{GRI}" stroke-width="1"/>'
    return ic


def ok(x1, y1, x2, y2, renk, k=2.4):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 8 * math.cos(a):.1f}" y2="{y2 - 8 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{k}"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{renk}"/>')


def blok(x, y, w, h, metin, dolgu=KAHVE_A, cizgi=KAHVE):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{dolgu}" stroke="{cizgi}" stroke-width="1.6"/>'
            + yazi(x + w / 2, y + h / 2 + 5, metin, 13, LAC))


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def duzenek(kutle, kuvvet, ek_yazi, hiz=False):
    """Yatay zeminde blok; sağa F kuvveti; sağda bilgi."""
    ic = cerceve(360, 130) + zemin(20, 340, 104)
    ic += blok(70, 54, 84, 50, kutle)
    ic += ok(154, 79, 236, 79, KIR) + yazi(196, 70, kuvvet, 13, KIR)
    if hiz:
        ic += ok(80, 36, 144, 36, YES, 1.8) + yazi(112, 28, 'v = sabit', 12, YES)
    for i, t in enumerate(ek_yazi):
        ic += yazi(338, 34 + i * 20, t, 12, SOLUK, 'end', True)
    return svg(ic, 360, 130, 'Yatay zeminde kuvvet uygulanan cisim', 30)


def grafik(nokta, fsmax, fk, isaret, etiket, en=360, boy=170, mm=36, aci=False):
    """f–F grafiği: (0,0)→(fsmax,fsmax), sonra fk'de sabit. nokta: ölçek birimi (px/N)."""
    ox, oy = 46, boy - 30
    ic = cerceve(en, boy)
    ic += ok(ox, oy, ox, 16, LAC, 1.4) + ok(ox, oy, en - 14, oy, LAC, 1.4)
    ic += yazi(ox + 8, 22, f'f{alt("sürtünme")} (N)', 12, LAC, 'start')
    ic += yazi(en - 16, oy + 22, 'F (N)', 12, LAC, 'end')
    X = lambda v: ox + v * nokta
    Y = lambda v: oy - v * nokta
    ic += (f'<polyline points="{ox},{oy} {X(fsmax):.1f},{Y(fsmax):.1f} {X(fsmax):.1f},{Y(fk):.1f} {en - 26},{Y(fk):.1f}" '
           f'fill="none" stroke="{MAVI}" stroke-width="2.6" stroke-linejoin="round"/>')
    for v, r in ((fsmax, KIR), (fk, YES)):
        ic += f'<line x1="{ox}" y1="{Y(v):.1f}" x2="{X(fsmax):.1f}" y2="{Y(v):.1f}" stroke="{r}" stroke-width="1" stroke-dasharray="4 3"/>'
        ic += yazi(ox - 6, Y(v) + 4.5, str(v), 12, r, 'end')
    ic += f'<line x1="{X(fsmax):.1f}" y1="{Y(fsmax):.1f}" x2="{X(fsmax):.1f}" y2="{oy}" stroke="{GRI}" stroke-width="1" stroke-dasharray="4 3"/>'
    ic += yazi(X(fsmax), oy + 16, str(fsmax), 12, LAC)
    ic += yazi(ox - 6, oy + 14, '0', 12, LAC, 'end')
    if isaret:
        ic += yazi((ox + X(fsmax)) / 2, oy - 8, 'durgun', 11.5, SOLUK, ince=True)
        ic += yazi((X(fsmax) + en - 26) / 2, Y(fk) + 18, 'kayıyor', 11.5, SOLUK, ince=True)
    if aci:
        ic += f'<path d="M {ox + 26} {oy} A 26 26 0 0 0 {ox + 18.4:.1f} {oy - 18.4:.1f}" fill="none" stroke="{TUR}" stroke-width="1.4"/>'
        ic += yazi(ox + 34, oy - 6, 'α', 13, TUR, 'start')
    return svg(ic, en, boy, etiket, mm)


def yuzey_alani():
    ic = cerceve(360, 130) + zemin(14, 346, 104)
    ic += yazi(90, 26, 'I', 14, MAVI) + blok(40, 66, 100, 38, 'tuğla') + ok(140, 85, 186, 85, KIR) + yazi(163, 76, 'F', 13, KIR)
    ic += yazi(262, 26, 'II', 14, MAVI) + blok(240, 34, 44, 70, 'tuğla') + ok(284, 69, 330, 69, KIR) + yazi(307, 60, 'F', 13, KIR)
    return svg(ic, 360, 130, 'Aynı tuğla geniş ve dar yüzeyi üzerinde', 30)


def ust_uste():
    ic = cerceve(360, 140) + zemin(14, 346, 114)
    ic += yazi(95, 24, 'I', 14, MAVI) + blok(55, 72, 80, 42, '3 kg') + ok(135, 93, 172, 93, KIR, 2) + yazi(150, 84, 'v', 12, KIR)
    ic += yazi(268, 24, 'II', 14, MAVI) + blok(228, 72, 80, 42, '3 kg') + blok(238, 34, 60, 38, '3 kg', MAVI_A, MAVI)
    ic += ok(308, 93, 345, 93, KIR, 2) + yazi(323, 84, 'v', 12, KIR)
    return svg(ic, 360, 140, 'Aynı yüzeyde kayan tek blok ve üst üste iki blok', 31)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = duzenek('6 kg', 'F = 15 N', ['k' + alt('s') + ' = 0,4', 'g = 10 m/s²'])
    s[2]['gorsel'] = grafik(4.4, 24, 18, True, 'Sürtünme kuvveti–uygulanan kuvvet grafiği')
    s[4]['gorsel'] = duzenek('5 kg', 'F = 35 N', ['k' + alt('s') + ' = 0,6', 'k' + alt('k') + ' = 0,4', 'g = 10 m/s²'])
    s[6]['gorsel'] = yuzey_alani()
    s[7]['gorsel'] = ust_uste()
    s[11]['gorsel'] = duzenek('7 kg', 'F = 21 N', ['g = 10 m/s²'], hiz=True)
    s[13]['gorsel'] = grafik(3.0, 30, 24, False, 'Statik bölgesi açıyla gösterilen f–F grafiği', boy=160, mm=32, aci=True)
