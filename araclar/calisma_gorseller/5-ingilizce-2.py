"""5. sınıf İngilizce 2. hafta (Revision 1: school routines, subjects, time, seasons, appearance, clothing) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def nesneler():
    """1 zımba, 2 hesap makinesi, 3 kulaklık, 4 çöp kutusu."""
    ic, renk = '', [TUR, MAVI, YES, MOR]
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 70, [TUR_A, MAVI_A, YES_A, MOR_A][i], renk[i], 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), renk[i])
    x, y = 50, 44  # zımba
    ic += (f'<path d="M{x - 26} {y + 12} h52 v6 h-52 z" fill="{SOLUK}"/><path d="M{x - 24} {y + 10} L{x + 22} {y - 6} q6 -2 6 4 v4 L{x - 22} {y + 12} z" fill="{KIR}"/>'
           f'<circle cx="{x - 20}" cy="{y + 10}" r="3" fill="{LAC}"/>')
    x = 135  # hesap makinesi
    ic += (f'<rect x="{x - 18}" y="{y - 22}" width="36" height="48" rx="4" fill="{LAC}"/><rect x="{x - 13}" y="{y - 17}" width="26" height="10" rx="1.5" fill="#cfe8d0"/>'
           + ''.join(f'<rect x="{x - 13 + (k % 3) * 9.5}" y="{y - 3 + (k // 3) * 8}" width="7" height="6" rx="1" fill="{[GRI_A, TUR][k == 11]}"/>' for k in range(12)))
    x = 224  # kulaklık
    ic += (f'<path d="M{x - 20} {y + 8} v-8 a20 20 0 0 1 40 0 v8" fill="none" stroke="{LAC}" stroke-width="4"/>'
           f'<rect x="{x - 26}" y="{y + 2}" width="12" height="20" rx="5" fill="{YES}"/><rect x="{x + 14}" y="{y + 2}" width="12" height="20" rx="5" fill="{YES}"/>')
    x = 313  # çöp kutusu
    ic += (f'<path d="M{x - 16} {y - 12} h32 l-4 38 h-24 z" fill="{GRI_A}" stroke="{SOLUK}" stroke-width="1.6"/><rect x="{x - 20}" y="{y - 18}" width="40" height="6" rx="2" fill="{SOLUK}"/>'
           + ''.join(f'<line x1="{x + d}" y1="{y - 6}" x2="{x + d * 0.8}" y2="{y + 20}" stroke="{GRI}" stroke-width="1.4"/>' for d in (-8, 0, 8)))
    return svg(360, 78, ic, 'Okul nesneleri: 1 zımba, 2 hesap makinesi, 3 kulaklık, 4 çöp kutusu', 18)


def saat(cx, cy, sa, dk, renk):
    ic = f'<circle cx="{cx}" cy="{cy}" r="27" fill="#fff" stroke="{renk}" stroke-width="3"/>'
    ic += ''.join(f'<line x1="{cx + 22 * math.sin(k * math.pi / 6):.1f}" y1="{cy - 22 * math.cos(k * math.pi / 6):.1f}" x2="{cx + 25 * math.sin(k * math.pi / 6):.1f}" y2="{cy - 25 * math.cos(k * math.pi / 6):.1f}" stroke="{LAC}" stroke-width="{2 if k % 3 == 0 else 1}"/>' for k in range(12))
    a_sa = (sa % 12 + dk / 60) * math.pi / 6
    a_dk = dk * math.pi / 30
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 13 * math.sin(a_sa):.1f}" y2="{cy - 13 * math.cos(a_sa):.1f}" stroke="{LAC}" stroke-width="3.2" stroke-linecap="round"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 20 * math.sin(a_dk):.1f}" y2="{cy - 20 * math.cos(a_dk):.1f}" stroke="{renk}" stroke-width="2.2" stroke-linecap="round"/>'
    return ic + f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="{LAC}"/>'


def saatler():
    ic = ''
    for i, (sa, dk) in enumerate([(8, 0), (10, 30), (1, 0), (4, 30)]):
        x = 48 + i * 88
        renk = [TUR, MAVI, YES, MOR][i]
        ic += saat(x, 40, sa, dk, renk) + rozet(x - 30, 12, 'ABCD'[i], renk)
    return svg(360, 72, ic, 'Saatler: A sekiz, B on buçuk, C bir, D dört buçuk', 17)


def hava_karti():
    ic = kutu(4, 4, 352, 70, CAM_A, CAM, 10, 1.4) + yazi(20, 24, 'Weather today', 12.5, CAM, 'start')
    # bulut ve yağmur
    ic += (f'<ellipse cx="64" cy="48" rx="26" ry="13" fill="#fff" stroke="{SOLUK}" stroke-width="1.4"/><circle cx="54" cy="40" r="11" fill="#fff" stroke="{SOLUK}" stroke-width="1.4"/>'
           f'<ellipse cx="64" cy="48" rx="25" ry="12" fill="#fff"/>'
           + ''.join(f'<line x1="{x}" y1="64" x2="{x - 4}" y2="72" stroke="{MAVI}" stroke-width="2"/>' for x in (50, 62, 74)))
    # termometre
    ic += (f'<rect x="124" y="28" width="10" height="34" rx="5" fill="#fff" stroke="{LAC}" stroke-width="1.4"/><circle cx="129" cy="64" r="7" fill="{MAVI}"/>'
           f'<rect x="126.5" y="52" width="5" height="12" fill="{MAVI}"/>')
    ic += yazi(144, 50, '5 °C', 16, MAVI, 'start') + yazi(206, 40, 'rainy', 13, LAC, 'start', True) + yazi(206, 60, 'cold and windy', 13, LAC, 'start', True)
    return svg(360, 78, ic, 'Hava durumu kartı: yağmurlu, 5 °C, soğuk ve rüzgârlı', 18)


def tanitim_karti():
    ic = kutu(4, 4, 352, 92, '#fff', MOR, 10, 1.6) + f'<rect x="4" y="4" width="352" height="22" rx="10" fill="{MOR}"/><rect x="4" y="16" width="352" height="10" fill="{MOR}"/>'
    ic += yazi(16, 20, 'Show and Tell · About me', 12, '#fff', 'start')
    satirlar = [('Name:', 'Elif'), ('Looks:', 'tall and thin, short curly hair, green eyes'), ('Personality:', 'funny and clever')]
    for k, (a, b) in enumerate(satirlar):
        ic += yazi(18, 46 + k * 19, a, 12, MOR, 'start') + yazi(110, 46 + k * 19, b, 12, LAC, 'start', True)
    return svg(360, 100, ic, 'Tanıtım kartı: Elif; tall and thin, short curly hair, green eyes; funny and clever', 22)


def program():
    gunler = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    dersler = ['Maths', 'Art', 'Science', 'Music', 'P.E.']
    renk = [MAVI, TUR, YES, MOR, KIR]
    ic = yazi(180, 16, "Kaan's timetable (first lesson)", 12.5, LAC)
    for i in range(5):
        x0 = 6 + i * 70
        ic += kutu(x0, 24, 64, 22, renk[i], renk[i], 6, 1) + yazi(x0 + 32, 39, gunler[i], 11.5, '#fff')
        ic += kutu(x0, 50, 64, 30, '#fff', renk[i], 6, 1.2) + yazi(x0 + 32, 70, dersler[i], 12, LAC, 'middle', True)
    return svg(360, 84, ic, "Kaan'ın ders programı (ilk ders): Mon Maths, Tue Art, Wed Science, Thu Music, Fri P.E.", 19)


def album():
    ic = ''
    # 1 bisiklet (6 yaş, yaz)
    ic += kutu(8, 4, 166, 86, '#fff', GRI, 4, 1.4) + f'<rect x="16" y="12" width="150" height="54" fill="{YES_A}"/>'
    ic += (f'<circle cx="62" cy="50" r="12" fill="none" stroke="{LAC}" stroke-width="2.4"/><circle cx="114" cy="50" r="12" fill="none" stroke="{LAC}" stroke-width="2.4"/>'
           f'<path d="M62 50 L82 30 L106 30 L114 50 M82 30 L90 50 L106 30 M78 24 h10 M104 30 l-2 -8 h8" fill="none" stroke="{KIR}" stroke-width="2.4" stroke-linejoin="round"/>'
           f'<circle cx="150" cy="24" r="8" fill="{ALTIN}"/>')
    ic += yazi(91, 83, 'Age 6 · summer', 12, LAC)
    # 2 uçurtma (8 yaş, sonbahar)
    ic += kutu(186, 4, 166, 86, '#fff', GRI, 4, 1.4) + f'<rect x="194" y="12" width="150" height="54" fill="{TUR_A}"/>'
    ic += (f'<path d="M270 16 L288 34 L270 56 L252 34 Z" fill="{MAVI}"/><path d="M270 16 V56 M252 34 H288" stroke="#fff" stroke-width="1.2"/>'
           f'<path d="M270 56 q-8 6 -2 10 q6 4 -4 8" fill="none" stroke="{LAC}" stroke-width="1.2"/>'
           f'<path d="M212 58 q6 -8 12 0 M318 50 q6 -8 12 0" fill="none" stroke="{TUR}" stroke-width="2"/>')
    ic += yazi(269, 83, 'Age 8 · autumn', 12, LAC)
    return svg(360, 94, ic, 'Fotoğraf albümü: 6 yaşında yazın bisiklet, 8 yaşında sonbaharda uçurtma', 21)


def kalp(x, y, renk=KIR):
    return f'<path d="M{x} {y + 5} C{x - 9} {y - 1} {x - 6} {y - 9} {x} {y - 4} C{x + 6} {y - 9} {x + 9} {y - 1} {x} {y + 5} Z" fill="{renk}"/>'


def carpi(x, y, renk=SOLUK):
    return f'<path d="M{x - 5} {y - 5} L{x + 5} {y + 5} M{x + 5} {y - 5} L{x - 5} {y + 5}" stroke="{renk}" stroke-width="2.6" stroke-linecap="round"/>'


def isaret(x, y, tur):
    """tur: 2 = love (iki kalp), 1 = like, -1 = dislike (bir çarpı), -2 = hate."""
    f = kalp if tur > 0 else carpi
    return f(x, y) if abs(tur) == 1 else f(x - 7, y) + f(x + 7, y)


def begeni():
    """Can'ın tercih çizelgesi: iki kalp love, kalp like, çarpı dislike, iki çarpı hate (çizim; glif yok)."""
    etkin = ['swimming', 'reading comics', 'wearing a scarf', 'getting up early']
    tur = [2, 1, -1, -2]
    ic = kutu(4, 4, 352, 104, '#fff', GRI, 8, 1.2) + yazi(180, 22, "Can's likes and dislikes", 12.5, LAC)
    for k in range(4):
        y = 44 + k * 18
        ic += rozet(20, y - 4, str(k + 1), [MAVI, TUR, YES, MOR][k], 8) + yazi(36, y, etkin[k], 12, LAC, 'start', True) + isaret(206, y - 4, tur[k])
    for k, (t, ad) in enumerate([(2, 'love'), (1, 'like'), (-1, 'dislike'), (-2, 'hate')]):
        y = 46 + k * 16
        ic += isaret(276, y - 4, t) + yazi(296, y, '= ' + ad, 11, LAC, 'start', True)
    ic += f'<line x1="248" y1="34" x2="248" y2="102" stroke="{GRI}" stroke-width="1"/>'
    return svg(360, 112, ic, "Can'ın tercih çizelgesi: 1 swimming love, 2 reading comics like, 3 wearing a scarf dislike, 4 getting up early hate", 25)


def agac(x, y, tur):
    """Bir mevsim kartındaki ağaç: tur 1 ilkbahar (çiçek + yağmur), 2 yaz (yeşil + güneş), 3 sonbahar (turuncu, dökülen yaprak + rüzgâr), 4 kış (çıplak + kar)."""
    ic = f'<rect x="{x - 3}" y="{y + 8}" width="6" height="18" rx="2" fill="{KAHVE}"/>'
    if tur == 4:
        ic += (f'<path d="M{x} {y + 10} V{y - 8} M{x} {y} L{x - 10} {y - 10} M{x} {y} L{x + 10} {y - 10} M{x} {y - 6} L{x - 6} {y - 14} M{x} {y - 6} L{x + 6} {y - 14}" '
               f'fill="none" stroke="{KAHVE}" stroke-width="2.2" stroke-linecap="round"/>')
        ic += ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="1.6" fill="{MAVI}"/>' for dx, dy in ((-22, -18), (-14, -4), (22, -14), (16, 2), (-20, 12), (24, 14)))
    else:
        dolgu = {1: '#bfe8c8', 2: YES, 3: TUR}[tur]
        ic += f'<circle cx="{x}" cy="{y - 4}" r="15" fill="{dolgu}"/><circle cx="{x - 9}" cy="{y + 2}" r="10" fill="{dolgu}"/><circle cx="{x + 9}" cy="{y + 2}" r="10" fill="{dolgu}"/>'
    if tur == 1:
        ic += ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="2.2" fill="#f28ab2"/>' for dx, dy in ((-8, -8), (4, -12), (10, 0), (-12, 4), (0, 2)))
        ic += ''.join(f'<line x1="{x + dx}" y1="{y - 22}" x2="{x + dx - 3}" y2="{y - 14}" stroke="{MAVI}" stroke-width="1.8" stroke-linecap="round"/>' for dx in (-20, -14, 22, 28))
    elif tur == 2:
        ic += f'<circle cx="{x + 23}" cy="{y - 23}" r="7" fill="{ALTIN}"/>' + ''.join(
            f'<line x1="{x + 23 + 10 * math.cos(k * math.pi / 4):.1f}" y1="{y - 23 + 10 * math.sin(k * math.pi / 4):.1f}" x2="{x + 23 + 13 * math.cos(k * math.pi / 4):.1f}" y2="{y - 23 + 13 * math.sin(k * math.pi / 4):.1f}" stroke="{ALTIN}" stroke-width="1.6"/>' for k in range(8))
    elif tur == 3:
        ic += ''.join(f'<ellipse cx="{x + dx}" cy="{y + dy}" rx="3.2" ry="2" transform="rotate(-30 {x + dx} {y + dy})" fill="{KIR}"/>' for dx, dy in ((-24, 6), (-30, 16), (22, 12), (28, 22)))
        ic += f'<path d="M{x - 26} {y - 16} h14 M{x - 30} {y - 10} h10 M{x + 20} {y - 20} h14" fill="none" stroke="{GRI}" stroke-width="1.8" stroke-linecap="round"/>'
    return ic


def mevsimler():
    """Dört mevsim kartı: 1 ilkbahar, 2 yaz, 3 sonbahar, 4 kış (ağaç + hava belirtisi)."""
    ic, renk = '', [YES, TUR, KIR, MAVI]
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 70, [YES_A, TUR_A, KIR_A, MAVI_A][i], renk[i], 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), renk[i])
        ic += agac(x0 + 46, 42, i + 1)
    return svg(360, 78, ic, 'Dört mevsim ağacı: 1 çiçekli ve yağmurlu, 2 yeşil ve güneşli, 3 turuncu yapraklı ve rüzgârlı, 4 çıplak ve karlı', 18)


def kis_gezisi():
    """Kış gezisi fotoğrafı: kar, kardan adam, bankta şapka ve eldivenler, beyaz ağaçlar (insan yok)."""
    ic = kutu(4, 4, 352, 92, '#fff', GRI, 4, 1.4) + f'<rect x="12" y="12" width="336" height="60" fill="{MAVI_A}"/><rect x="12" y="58" width="336" height="14" fill="#f4f7fb"/>'
    ic += yazi(180, 87, 'Class 5-A · winter trip · last year', 12, LAC)
    # kar taneleri
    ic += ''.join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="{MAVI}"/>' for x, y in ((30, 20), (70, 30), (120, 18), (170, 26), (230, 16), (280, 28), (330, 20), (300, 44), (60, 48)))
    # beyaz (karlı) ağaçlar
    for x in (40, 320):
        ic += (f'<rect x="{x - 2.5}" y="44" width="5" height="16" fill="{KAHVE}"/>'
               f'<path d="M{x} 20 L{x - 14} 46 H{x + 14} Z" fill="#fff" stroke="{GRI}" stroke-width="1.4"/><path d="M{x} 28 L{x - 10} 40 H{x + 10} Z" fill="#fff"/>')
    # kardan adam
    ic += (f'<circle cx="140" cy="56" r="13" fill="#fff" stroke="{GRI}" stroke-width="1.4"/><circle cx="140" cy="36" r="9" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
           f'<rect x="132" y="22" width="16" height="6" rx="1" fill="{LAC}"/><rect x="136" y="16" width="8" height="7" fill="{LAC}"/>'
           f'<path d="M144 37 l8 2 l-8 2 z" fill="{TUR}"/><circle cx="137" cy="34" r="1.3" fill="{LAC}"/><circle cx="141" cy="34" r="1.3" fill="{LAC}"/>'
           f'<circle cx="140" cy="52" r="1.3" fill="{LAC}"/><circle cx="140" cy="58" r="1.3" fill="{LAC}"/>'
           f'<line x1="127" y1="52" x2="114" y2="44" stroke="{KAHVE}" stroke-width="2"/><line x1="153" y1="52" x2="166" y2="44" stroke="{KAHVE}" stroke-width="2"/>')
    # bank, üstünde şapka ve eldivenler
    ic += f'<rect x="196" y="46" width="90" height="6" rx="2" fill="{KAHVE}"/><rect x="202" y="52" width="5" height="12" fill="{KAHVE}"/><rect x="275" y="52" width="5" height="12" fill="{KAHVE}"/>'
    ic += f'<path d="M206 46 v-6 a9 9 0 0 1 18 0 v6 z" fill="{KIR}"/><rect x="204" y="43" width="22" height="4" rx="2" fill="{KIR}"/>'
    for x in (240, 262):
        ic += f'<path d="M{x} 46 v-8 a5 5 0 0 1 10 0 v8 z M{x + 10} 40 l5 -4 l2 3 l-6 4" fill="{MOR}"/>'
    return svg(360, 100, ic, 'Kış gezisi fotoğrafı: karlı hava, beyaz ağaçlar, kardan adam, bankta şapka ve eldivenler; Class 5-A, winter trip, last year', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = nesneler()
    s[1]['gorsel'] = saatler()
    s[3]['gorsel'] = hava_karti()
    s[4]['gorsel'] = tanitim_karti()
    s[5]['gorsel'] = program()
    s[7]['gorsel'] = album()
    s[9]['gorsel'] = begeni()
    s[12]['gorsel'] = mevsimler()
    s[13]['gorsel'] = kis_gezisi()
