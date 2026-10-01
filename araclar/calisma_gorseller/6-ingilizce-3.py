"""6. sınıf İngilizce 3. hafta (Revision 2: places, food, animals, comparisons, holiday plans) çalışma kâğıdı görselleri (SVG; insan figürü yok)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#f3e2b3'
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


def park_panosu():
    """Millî park panosu: elephant 3 m, bear 1.5 m, deer 1.2 m (height); cheetah 100 km/h, tiger 60 km/h (speed)."""
    ic = yazi(180, 13, 'National park · info board', 11.5, LAC)
    veri = [('elephant', '3 m', 'height', YES), ('bear', '1.5 m', 'height', YES), ('deer', '1.2 m', 'height', YES), ('cheetah', '100 km/h', 'speed', TUR), ('tiger', '60 km/h', 'speed', TUR)]
    for i, (ad, deger, etiket, renk) in enumerate(veri):
        x0 = 6 + i * 70
        ic += kutu(x0, 20, 64, 52, YES_A if renk == YES else TUR_A, renk, 6, 1.2) + yazi(x0 + 32, 35, ad, 11, LAC) + yazi(x0 + 32, 53, deger, 12, renk) + yazi(x0 + 32, 66, etiket, 9.5, SOLUK, 'middle', True)
    return svg(360, 78, ic, 'Millî park panosu: elephant 3 m, bear 1.5 m, deer 1.2 m boy; cheetah 100 km/h, tiger 60 km/h hız', 17)


def menu():
    """Restoran menüsü: soup 40, sandwich 60, salad 35, lemonade 25, cake 45, ice cream 30 TL."""
    ic = kutu(20, 4, 320, 92, '#fffdf7', KAHVE, 8, 1.6) + yazi(180, 20, 'MENU', 13, KAHVE)
    sol = [('Vegetable soup', '40 TL'), ('Tuna sandwich', '60 TL'), ('Green salad', '35 TL')]
    sag = [('Lemonade', '25 TL'), ('Chocolate cake', '45 TL'), ('Ice cream', '30 TL')]
    for k, ((a, b), (c, d)) in enumerate(zip(sol, sag)):
        y = 40 + k * 18
        ic += yazi(34, y, a, 11, LAC, 'start', True) + yazi(168, y, b, 11, KIR, 'end') + yazi(192, y, c, 11, LAC, 'start', True) + yazi(326, y, d, 11, KIR, 'end')
    ic += f'<line x1="180" y1="30" x2="180" y2="88" stroke="{GRI}" stroke-width="1"/>'
    return svg(360, 100, ic, 'Menü: Vegetable soup 40 TL, Tuna sandwich 60 TL, Green salad 35 TL, Lemonade 25 TL, Chocolate cake 45 TL, Ice cream 30 TL', 20)


def kaplar():
    """1 bardak limonata, 2 dilim pasta, 3 kâse çorba, 4 şişe su (ad yok)."""
    ic = ''
    renk = [ALTIN, KAHVE, TUR, MAVI]
    for i in range(4):
        x0 = 4 + i * 89; cx = x0 + 46
        ic += kutu(x0, 4, 84, 66, GRI_A, GRI, 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), [TUR, MOR, KIR, MAVI][i])
        if i == 0:  # bardak limonata
            ic += f'<path d="M{cx - 11} 22 h22 l-3 34 h-16 z" fill="#fff" stroke="{LAC}" stroke-width="1.4"/><path d="M{cx - 9} 34 h18 l-2 21 h-14 z" fill="{ALTIN}"/><line x1="{cx + 4}" y1="18" x2="{cx + 12}" y2="40" stroke="{KIR}" stroke-width="2"/>'
        elif i == 1:  # dilim pasta
            ic += f'<path d="M{cx - 16} 56 L{cx + 16} 56 L{cx} 26 Z" fill="{KAHVE}"/><path d="M{cx - 8} 41 L{cx + 8} 41 L{cx} 26 Z" fill="#f28ab2"/><path d="M{cx - 16} 56 h32 v4 h-32 z" fill="#5a3717"/>'
        elif i == 2:  # kâse çorba
            ic += f'<path d="M{cx - 20} 40 h40 q0 18 -20 18 q-20 0 -20 -18 z" fill="#fff" stroke="{LAC}" stroke-width="1.4"/><ellipse cx="{cx}" cy="40" rx="20" ry="4" fill="{TUR}"/>' + ''.join(f'<path d="M{cx + dx} 32 q3 -5 0 -10" fill="none" stroke="{GRI}" stroke-width="1.4"/>' for dx in (-7, 0, 7))
        else:  # şişe su
            ic += f'<rect x="{cx - 8}" y="26" width="16" height="32" rx="4" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/><rect x="{cx - 4}" y="18" width="8" height="8" fill="{MAVI}"/><rect x="{cx - 8}" y="38" width="16" height="10" fill="{MAVI}" opacity="0.5"/>'
    return svg(360, 74, ic, 'Kaplar: 1 bardak limonata, 2 dilim pasta, 3 kâse çorba, 4 şişe su', 17)


def tatil_plani():
    """Tatil planı kartı: tiny house in the forest, 2 bedrooms, food festival, local band."""
    ic = kutu(30, 4, 300, 92, '#fff', YES, 8, 1.6) + f'<rect x="30" y="4" width="300" height="20" rx="8" fill="{YES}"/><rect x="30" y="14" width="300" height="10" fill="{YES}"/>' + yazi(180, 18, 'OUR HOLIDAY PLAN', 11, '#fff')
    satirlar = ['a tiny house in the forest', '2 bedrooms', 'a food festival', 'a local band']
    for k, m in enumerate(satirlar):
        x0 = 44 + (k % 2) * 148; y = 44 + (k // 2) * 30
        ic += kutu(x0, y - 14, 136, 24, YES_A, YES, 6, 1) + yazi(x0 + 68, y + 2, m, 10.5, LAC, 'middle', True)
    return svg(360, 100, ic, 'Tatil planı: ormanda küçük ev, 2 yatak odası, yemek festivali, yerel müzik grubu', 20)


def tatil_takvimi():
    """Elif'in tatil takvimi: Saturday beach and sandcastles, Sunday ancient theatre."""
    ic = yazi(180, 13, "Elif's holiday", 11.5, LAC)
    for i, (gun, etiket, renk, acik) in enumerate([('Saturday', 'beach · sandcastles', TUR, TUR_A), ('Sunday', 'ancient theatre', MOR, MOR_A)]):
        x0 = 40 + i * 150; cx = x0 + 65
        ic += kutu(x0, 20, 130, 18, renk, renk, 4, 1) + yazi(cx, 33, gun, 11, '#fff') + kutu(x0, 40, 130, 44, acik, renk, 4, 1.2) + yazi(cx, 79, etiket, 10, LAC, 'middle', True)
        if i == 0:  # kumdan kale
            ic += f'<rect x="{cx - 16}" y="57" width="32" height="11" fill="{KUM}" stroke="{KAHVE}" stroke-width="1"/><rect x="{cx - 8}" y="50" width="16" height="8" fill="{KUM}" stroke="{KAHVE}" stroke-width="1"/><path d="M{cx} 50 v-6 l6 2 l-6 2" fill="{KIR}" stroke="{KIR}" stroke-width="1"/>'
        else:  # antik tiyatro
            ic += ''.join(f'<path d="M{cx - r} 66 a{r} {r * 0.6} 0 0 1 {2 * r} 0" fill="none" stroke="{MOR}" stroke-width="2.4"/>' for r in (10, 17, 24)) + f'<rect x="{cx - 8}" y="62" width="16" height="4" fill="{MOR}"/>'
    return svg(360, 90, ic, "Elif'in tatil takvimi: cumartesi plaj ve kumdan kale, pazar antik tiyatro", 19)


def yasam_alanlari():
    """Yaşam alanları: 1 forest (ağaçlar), 2 ocean (dalgalar), 3 desert (güneş ve kum tepeleri)."""
    ic = ''
    for i, (ad, renk, acik) in enumerate([('forest', YES, YES_A), ('ocean', MAVI, MAVI_A), ('desert', TUR, TUR_A)]):
        x0 = 12 + i * 116; cx = x0 + 52
        ic += kutu(x0, 4, 104, 64, acik, renk, 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), renk, 8) + yazi(cx, 62, ad, 10.5, LAC, 'middle', True)
        if i == 0:
            ic += ''.join(f'<path d="M{cx + dx - 9} 40 L{cx + dx + 9} 40 L{cx + dx} 20 Z" fill="{YES}"/><rect x="{cx + dx - 1.5}" y="40" width="3" height="6" fill="{KAHVE}"/>' for dx in (-22, 0, 22))
        elif i == 1:
            ic += ''.join(f'<path d="M{cx - 28} {y} q8 -6 16 0 t16 0 t16 0 t16 0" fill="none" stroke="{MAVI}" stroke-width="2"/>' for y in (27, 36, 45))
        else:
            ic += f'<circle cx="{cx - 12}" cy="22" r="7" fill="{ALTIN}"/><path d="M{cx - 40} 46 q20 -16 40 0 q14 -10 40 0 v4 h-80 z" fill="{KUM}" stroke="{TUR}" stroke-width="1"/>'
    return svg(360, 72, ic, 'Yaşam alanları: 1 orman, 2 okyanus, 3 çöl', 16)


def harita():
    """Harita: üst sıra café, museum, cinema; alt sıra park, bank, school; ortada cadde."""
    ic = kutu(4, 4, 352, 92, '#f7f9fc', GRI, 8, 1.2) + '<rect x="4" y="44" width="352" height="12" fill="#d9dee8"/>' + ''.join(f'<rect x="{x}" y="49" width="12" height="2" fill="#fff"/>' for x in range(14, 350, 28))
    ust = [('café', TUR), ('museum', MOR), ('cinema', KIR)]
    alt = [('park', YES), ('bank', MAVI), ('school', CAM)]
    for i, (ad, renk) in enumerate(ust):
        x0 = 14 + i * 116
        ic += kutu(x0, 10, 104, 28, '#fff', renk, 4, 1.4) + yazi(x0 + 52, 28, ad, 11, renk)
    for i, (ad, renk) in enumerate(alt):
        x0 = 14 + i * 116
        ic += kutu(x0, 62, 104, 28, '#fff', renk, 4, 1.4) + yazi(x0 + 52, 80, ad, 11, renk)
    return svg(360, 100, ic, 'Harita: caddenin üstünde café, museum, cinema; altında park, bank, school', 20)


def binis_karti():
    """Biniş kartı: Elif, to Antalya, Saturday 10:20, gate 5."""
    ic = kutu(20, 4, 320, 76, '#fff', MAVI, 8, 1.6) + f'<rect x="20" y="4" width="320" height="20" rx="8" fill="{MAVI}"/><rect x="20" y="14" width="320" height="10" fill="{MAVI}"/>' + yazi(180, 18, 'BOARDING PASS', 11, '#fff')
    ic += f'<line x1="250" y1="24" x2="250" y2="80" stroke="{GRI}" stroke-width="1" stroke-dasharray="3 3"/>'
    for k, (a, b) in enumerate([('Passenger:', 'Elif'), ('To:', 'Antalya'), ('Date · Time:', 'Saturday · 10:20')]):
        y = 42 + k * 15
        ic += yazi(34, y, a, 10.5, MAVI, 'start') + yazi(112, y, b, 10.5, LAC, 'start', True)
    ic += yazi(295, 46, 'GATE', 10, MAVI) + yazi(295, 68, '5', 18, LAC)
    return svg(360, 84, ic, 'Biniş kartı: Elif, Antalya, cumartesi 10:20, kapı 5', 18)


def hava_tahmini():
    """Hava tahmini: Antalya 34 °C sunny, Nevşehir 22 °C cloudy."""
    ic = yazi(180, 13, 'Weather forecast · Saturday', 11.5, LAC)
    for i, (sehir, derece, durum, renk, acik) in enumerate([('Antalya', '34 °C', 'sunny', TUR, TUR_A), ('Nevşehir', '22 °C', 'cloudy', MAVI, MAVI_A)]):
        x0 = 40 + i * 150; cx = x0 + 65
        ic += kutu(x0, 20, 130, 48, acik, renk, 6, 1.2) + yazi(x0 + 12, 38, sehir, 11.5, renk, 'start') + yazi(x0 + 12, 58, derece + ' · ' + durum, 11, LAC, 'start', True)
        if i == 0:
            ic += f'<circle cx="{x0 + 108}" cy="44" r="9" fill="{ALTIN}"/>' + ''.join(f'<line x1="{x0 + 108 + 12 * math.cos(k * math.pi / 4):.1f}" y1="{44 + 12 * math.sin(k * math.pi / 4):.1f}" x2="{x0 + 108 + 15 * math.cos(k * math.pi / 4):.1f}" y2="{44 + 15 * math.sin(k * math.pi / 4):.1f}" stroke="{ALTIN}" stroke-width="1.6"/>' for k in range(8))
        else:
            ic += f'<ellipse cx="{x0 + 108}" cy="48" rx="16" ry="8" fill="#fff" stroke="{SOLUK}" stroke-width="1.4"/><circle cx="{x0 + 102}" cy="42" r="8" fill="#fff" stroke="{SOLUK}" stroke-width="1.4"/><ellipse cx="{x0 + 108}" cy="48" rx="15" ry="7" fill="#fff"/>'
    return svg(360, 74, ic, 'Hava tahmini: Antalya 34 derece güneşli, Nevşehir 22 derece bulutlu', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = park_panosu()
    s[1]['gorsel'] = menu()
    s[2]['gorsel'] = kaplar()
    s[3]['gorsel'] = tatil_plani()
    s[5]['gorsel'] = tatil_takvimi()
    s[8]['gorsel'] = yasam_alanlari()
    s[9]['gorsel'] = harita()
    s[10]['gorsel'] = binis_karti()
    s[14]['gorsel'] = hava_tahmini()
