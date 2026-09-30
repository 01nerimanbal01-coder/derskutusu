"""5. sınıf Fen Bilimleri 2. hafta (Güneş) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a'
MAVI_A, GRI, GRI_A = '#e8eefe', '#9aa6bd', '#eef1f6'
G_DIS, G_ORTA, G_IC, G_LEKE = '#ffc93c', '#f7a21b', '#e4572e', '#8a4b12'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def no_isareti(x, y, n, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{renk}"/>' + yazi(x, y + 4.5, n, 12, '#fff')


def ok_tanim(kimlik, renk):
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0L10 5L0 10z" fill="{renk}"/></marker>')


def kesit():
    cx, cy, r = 78, 72, 62
    ic = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{G_DIS}" stroke="{G_ORTA}" stroke-width="2"/>'
    ic += ''.join(f'<ellipse cx="{cx + dx}" cy="{cy + dy}" rx="{a}" ry="{b}" fill="{G_LEKE}" opacity=".75"/>' for dx, dy, a, b in [(-30, 18, 6, 4), (-14, 34, 4, 3)])
    for rr, renk in [(r, '#ffe08a'), (44, G_ORTA), (24, G_IC)]:     # çeyrek kesit: iç içe katmanlar
        ic += f'<path d="M{cx} {cy} L{cx + rr} {cy} A{rr} {rr} 0 0 0 {cx} {cy - rr} Z" fill="{renk}" stroke="#c9690a" stroke-width="1"/>'
    ic += f'<line x1="{cx + 10}" y1="{cy - 10}" x2="{cx + 96}" y2="{cy - 44}" stroke="{LAC}" stroke-width="1.4"/>' + no_isareti(cx + 106, cy - 48, 1)
    ic += f'<line x1="{cx + 44}" y1="{cy + 42}" x2="{cx + 96}" y2="{cy + 52}" stroke="{LAC}" stroke-width="1.4"/>' + no_isareti(cx + 106, cy + 54, 2)
    return svg(200, 140, ic, 'Güneş, bir çeyreği kesilmiş; iç içe katmanlar görünüyor. 1 en içteki bölgeyi, 2 yüzeyi gösteriyor', 30)


def bilye_balon():
    x0, y0 = 30, 69
    ic = f'<path d="M{x0 - 5} {y0 - 5} l10 10 m0 -10 l-10 10" stroke="{LAC}" stroke-width="2.4" stroke-linecap="round"/>'
    ic += yazi(6, 96, 'Gözlem noktası', 11.5, '#5b6479', 'start')
    ic += f'<circle cx="86" cy="69" r="8" fill="{MAVI}"/>' + yazi(86, 52, 'bilye (yakında)', 11.5, LAC)
    bx, by, br = 318, 44, 22
    ic += f'<path d="M{bx - br} {by} a{br} {br} 0 1 1 {2 * br} 0 q0 14 -{br * 0.55:.1f} 26 h-{br * 0.9:.1f} q-{br * 0.45:.1f} -12 -{br * 0.55:.1f} -26z" fill="{TUR}"/>'
    ic += ''.join(f'<path d="M{bx + k * 8} {by - br + 2} q{k * 6} {br} 0 {br + 22}" fill="none" stroke="#fff" stroke-width="1.2" opacity=".7"/>' for k in (-1, 0, 1))
    ic += f'<rect x="{bx - 7}" y="{by + 30}" width="14" height="10" rx="2" fill="#8a5a2b"/>'
    ic += yazi(356, 108, 'sıcak hava balonu (çok uzakta)', 11.5, LAC, 'end')
    for yy in (61, 77):
        ic += f'<line x1="{x0}" y1="{y0}" x2="86" y2="{yy}" stroke="{MAVI}" stroke-width="1" stroke-dasharray="3 3"/>'
    for yy in (by - br, by + 40):
        ic += f'<line x1="{x0}" y1="{y0}" x2="{bx}" y2="{yy}" stroke="{TUR}" stroke-width="1" stroke-dasharray="3 3"/>'
    return svg(360, 114, ic, 'Gözlem noktasına yakın küçük bir bilye ve çok uzakta büyük bir sıcak hava balonu; bakış çizgileri bilyenin daha büyük göründüğünü gösteriyor', 26)


def hareketler():
    sx, sy = 150, 72
    ic = f'<defs>{ok_tanim("ck5fok1", KIR)}{ok_tanim("ck5fok2", MAVI)}</defs>'
    ic += f'<ellipse cx="{sx}" cy="{sy}" rx="128" ry="52" fill="none" stroke="{GRI}" stroke-width="1.4" stroke-dasharray="5 4"/>'
    ic += f'<circle cx="{sx}" cy="{sy}" r="26" fill="{G_DIS}" stroke="{G_ORTA}" stroke-width="2"/>'
    ic += f'<line x1="{sx}" y1="{sy - 36}" x2="{sx}" y2="{sy + 36}" stroke="{LAC}" stroke-width="1.2" stroke-dasharray="3 2"/>'
    ic += f'<path d="M{sx - 22} {sy - 30} A26 8 0 0 0 {sx + 24} {sy - 31}" fill="none" stroke="{KIR}" stroke-width="2.2" marker-end="url(#ck5fok1)"/>'
    ic += no_isareti(sx - 34, sy - 38, 1, KIR)
    ex, ey = sx + 128 * math.cos(math.radians(35)), sy + 52 * math.sin(math.radians(35))
    ic += f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="11" fill="{MAVI}"/><path d="M{ex - 6:.1f} {ey - 4:.1f} q4 -3 8 0 t6 3" fill="none" stroke="{YES}" stroke-width="3"/>'
    a1, a2 = math.radians(52), math.radians(88)
    ic += (f'<path d="M{sx + 128 * math.cos(a1):.1f} {sy + 52 * math.sin(a1):.1f} A128 52 0 0 1 {sx + 128 * math.cos(a2):.1f} {sy + 52 * math.sin(a2):.1f}" '
           f'fill="none" stroke="{MAVI}" stroke-width="2.2" marker-end="url(#ck5fok2)"/>')
    ic += no_isareti(sx + 50, sy + 68, 2, MAVI)
    ic += yazi(sx - 32, sy + 5, 'Güneş', 11.5, '#b35c00', 'end') + yazi(ex + 16, ey + 4, 'Dünya', 11.5, MAVI, 'start')
    return svg(300, 150, ic, "Ortada Güneş; 1 numaralı ok Güneş'in kendi ekseni etrafında dönüşünü, 2 numaralı ok Dünya'nın Güneş çevresindeki yörüngedeki hareketini gösteriyor", 30)


def ekran():
    ic = ''
    for i, (gun, kay) in enumerate([('1. gün', 0), ('3. gün', 14), ('5. gün', 28)]):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="108" height="92" rx="4" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
        ic += f'<circle cx="{x + 54}" cy="50" r="36" fill="{G_DIS}" stroke="{G_ORTA}" stroke-width="1.6"/>'
        for dx, dy, a in [(-24, -10, 5), (-14, 12, 4)]:
            ic += f'<ellipse cx="{x + 54 + dx + kay}" cy="{50 + dy}" rx="{a}" ry="{a * 0.75:.1f}" fill="{G_LEKE}"/>'
        ic += yazi(x + 54, 116, gun, 12.5, LAC)
    return svg(360, 122, ic, 'Beyaz ekrana yansıtılmış Güneş görüntüsü üç günde: 1., 3. ve 5. günde iki koyu leke giderek sağa kaymış', 24)


def buyutec():
    ic = ''.join(f'<line x1="{20 + k * 16}" y1="4" x2="{70 + k * 11}" y2="46" stroke="{G_ORTA}" stroke-width="2" opacity=".8"/>' for k in range(5))
    ic += f'<circle cx="16" cy="12" r="9" fill="{G_DIS}" stroke="{G_ORTA}" stroke-width="1.6"/>'
    ic += f'<ellipse cx="96" cy="54" rx="34" ry="10" fill="{MAVI_A}" stroke="{LAC}" stroke-width="2.2"/>'
    ic += f'<line x1="130" y1="54" x2="176" y2="44" stroke="#6b4a2b" stroke-width="7" stroke-linecap="round"/>'
    ic += ''.join(f'<line x1="{72 + k * 12}" y1="62" x2="96" y2="104" stroke="{G_ORTA}" stroke-width="1.6" opacity=".85"/>' for k in range(5))
    ic += f'<path d="M20 108 L172 108 L186 122 L34 122 Z" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<path d="M92 108 q-6 -8 0 -14 q2 7 6 3 q2 6 -2 11z" fill="{KIR}"/><ellipse cx="96" cy="110" rx="9" ry="3" fill="#3b2a1a" opacity=".6"/>'
    ic += ''.join(f'<path d="M{100 + k * 6} 92 q-6 -8 0 -16 t0 -16" fill="none" stroke="{GRI}" stroke-width="1.4" opacity=".8"/>' for k in range(2))
    return svg(200, 128, ic, 'Güneş ışınları büyüteçten geçip kâğıt üzerinde bir noktada toplanıyor; kâğıt tutuşuyor ve duman çıkıyor', 26)


def gunluk():
    ic = f'<rect x="4" y="4" width="384" height="142" rx="6" fill="#fffdf5" stroke="#e3d9b8" stroke-width="1.4"/>'
    ic += ''.join(f'<line x1="4" y1="{y}" x2="388" y2="{y}" stroke="#dbe4f5" stroke-width="1"/>' for y in range(40, 146, 26))
    ic += f'<line x1="34" y1="4" x2="34" y2="146" stroke="#f3b3b3" stroke-width="1.2"/>'
    ic += yazi(44, 28, 'Güneş Günlüğüm', 14, TUR, 'start')
    notlar = ['Güneş bir gezegendir.', "Güneş'in çekirdeği yüzeyinden daha sıcaktır.",
              'Güneş lekelerinin yeri hiç değişmez.', "Güneş, Dünya'dan küçük olduğu için küçük görünür."]
    for i, m in enumerate(notlar):
        ic += yazi(22, 60 + i * 26, i + 1, 13, MAVI) + yazi(44, 60 + i * 26, m, 13, MAVI, 'start')
    return svg(392, 150, ic, "Güneş günlüğü: 1 Güneş bir gezegendir. 2 Güneş'in çekirdeği yüzeyinden daha sıcaktır. 3 Güneş lekelerinin yeri hiç değişmez. 4 Güneş, Dünya'dan küçük olduğu için küçük görünür.", 34)


def gunes_yolu():
    cx, cy, rx, ry = 180, 114, 150, 84
    ic = f'<defs>{ok_tanim("ck5fok3", GRI)}</defs>'
    ic += f'<rect x="0" y="{cy}" width="360" height="16" fill="#e3f6ea"/><line x1="0" y1="{cy}" x2="360" y2="{cy}" stroke="{YES}" stroke-width="2"/>'
    ic += f'<path d="M{cx - rx} {cy} A{rx} {ry} 0 0 1 {cx + rx} {cy}" fill="none" stroke="{GRI}" stroke-width="1.4" stroke-dasharray="5 4" marker-end="url(#ck5fok3)"/>'
    for harf, aci in [('K', 160), ('L', 125), ('M', 90), ('N', 18)]:
        a = math.radians(aci)
        x, y = cx + rx * math.cos(a), cy - ry * math.sin(a)
        ic += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{G_DIS}" stroke="{G_ORTA}" stroke-width="1.6"/>'
        ic += yazi(x + (0 if aci == 90 else (-18 if aci > 90 else 18)), y - 15, harf, 13.5, LAC)
    ic += yazi(8, cy + 13, 'ufuk', 11, '#0c7a3c', 'start')
    return svg(360, 132, ic, 'Güneşin gün içindeki yolu: K doğuştan hemen sonra, L sabah, M öğle en yüksekte, N batmaya yakın', 24)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kesit()
    s[4]['gorsel'] = bilye_balon()
    s[5]['gorsel'] = hareketler()
    s[7]['gorsel'] = buyutec()
    s[10]['gorsel'] = ekran()
    s[11]['gorsel'] = gunluk()
    s[12]['gorsel'] = gunes_yolu()
