"""5. sınıf İngilizce 4. hafta (School Life: people, places, rules, clubs, countries) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
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


def raf(x, y):
    ic = f'<rect x="{x - 24}" y="{y - 22}" width="48" height="44" rx="2" fill="#c98a4a" stroke="{KAHVE}" stroke-width="1.2"/><line x1="{x - 24}" y1="{y}" x2="{x + 24}" y2="{y}" stroke="{KAHVE}" stroke-width="1.6"/>'
    renk = [KIR, MAVI, YES, ALTIN, MOR, CAM]
    ic += ''.join(f'<rect x="{x - 21 + k * 7}" y="{y - 19}" width="6" height="18" fill="{renk[k]}"/>' for k in range(6))
    ic += ''.join(f'<rect x="{x - 21 + k * 7}" y="{y + 3}" width="6" height="17" fill="{renk[5 - k]}"/>' for k in range(6))
    return ic


def sise(x, y):
    return (f'<path d="M{x - 5} {y - 22} V{y - 6} L{x - 18} {y + 18} Q{x - 20} {y + 22} {x - 15} {y + 22} H{x + 15} Q{x + 20} {y + 22} {x + 18} {y + 18} L{x + 5} {y - 6} V{y - 22} Z" fill="#fff" stroke="{CAM}" stroke-width="1.6"/>'
            f'<path d="M{x - 11} {y + 6} H{x + 11} L{x + 17} {y + 19} H{x - 17} Z" fill="#7fd08f"/><circle cx="{x - 3}" cy="{y + 12}" r="2" fill="#fff"/><rect x="{x - 7}" y="{y - 25}" width="14" height="4" rx="1" fill="{CAM}"/>')


def tepsi(x, y):
    return (f'<rect x="{x - 26}" y="{y + 4}" width="52" height="16" rx="3" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>'
            f'<ellipse cx="{x - 12}" cy="{y + 4}" rx="10" ry="4" fill="#fff" stroke="{GRI}"/><path d="M{x - 18} {y + 2} q6 -8 12 0" fill="{TUR}"/>'
            f'<rect x="{x + 6}" y="{y - 12}" width="10" height="16" rx="2" fill="#bfe3f5" stroke="{MAVI}" stroke-width="1"/><circle cx="{x - 12}" cy="{y - 12}" r="6" fill="{KIR}"/><path d="M{x - 12} {y - 18} l2 -4" stroke="{YES}" stroke-width="1.6"/>')


def kale(x, y):
    return (f'<rect x="{x - 28}" y="{y + 8}" width="56" height="14" fill="#7fd08f"/><path d="M{x - 24} {y + 10} V{y - 16} H{x + 24} V{y + 10}" fill="none" stroke="#fff" stroke-width="3"/>'
            f'<path d="M{x - 24} {y - 16} H{x + 24}" stroke="{SOLUK}" stroke-width="1"/>'
            + ''.join(f'<line x1="{x - 24 + k * 8}" y1="{y - 16}" x2="{x - 24 + k * 8}" y2="{y + 10}" stroke="{GRI}" stroke-width="0.5"/>' for k in range(7))
            + f'<circle cx="{x + 12}" cy="{y + 14}" r="6" fill="#fff" stroke="{LAC}" stroke-width="1.2"/><path d="M{x + 9} {y + 11} l3 2 l3 -2 M{x + 12} {y + 13} v4" stroke="{LAC}" stroke-width="1"/>')


def esyalar():
    ic = ''
    for i, f in enumerate([raf, sise, tepsi, kale]):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 72, [TUR_A, CAM_A, KIR_A, YES_A][i], [TUR, CAM, KIR, YES][i], 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), [TUR, CAM, KIR, YES][i]) + f(x0 + 46, 42)
    return svg(360, 80, ic, 'Eşyalar: 1 kitap rafı, 2 deney şişesi, 3 yemek tepsisi, 4 futbol kalesi ve top', 19)


def plan():
    """Okul planı: odalar adlarıyla; spor sahasında düdük."""
    ic = kutu(4, 4, 352, 132, '#fff', LAC, 6, 2)
    oda = [('library', 4, 4, 120, 64, MAVI_A), ('canteen', 124, 4, 112, 64, TUR_A), ('science lab', 4, 68, 120, 68, CAM_A), ('sports field', 236, 4, 120, 132, '#cdebd5')]
    for ad, x, y, w, h, d in oda:
        ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{d}" stroke="{LAC}" stroke-width="1.6"/>' + yazi(x + w / 2, y + 20, ad, 12, LAC)
    ic += f'<rect x="124" y="68" width="112" height="68" fill="{GRI_A}" stroke="{LAC}" stroke-width="1.6"/>' + yazi(180, 106, 'corridor', 11, SOLUK, 'middle', True)
    # düdük (antrenör)
    x, y = 296, 78
    ic += (f'<path d="M{x - 16} {y - 6} H{x + 6} a10 10 0 1 1 -10 10 H{x - 16} Z" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.2"/><circle cx="{x - 2}" cy="{y + 4}" r="3" fill="{KAHVE}"/>'
           f'<path d="M{x - 16} {y - 4} Q{x - 34} {y - 22} {x - 20} {y - 34}" fill="none" stroke="{KIR}" stroke-width="1.6"/>')
    ic += f'<path d="M{x + 12} {y - 14} l6 -6 M{x + 16} {y - 6} l8 -2" stroke="{SOLUK}" stroke-width="1.4" stroke-linecap="round"/>'
    return svg(360, 140, ic, 'Okul planı: library, canteen, science lab, corridor ve sports field; spor sahasında bir düdük var', 30)


def afisler():
    ic = ''
    renk = [MOR, MAVI, LAC, YES]
    acik = [MOR_A, MAVI_A, GRI_A, YES_A]
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 84, acik[i], renk[i], 6, 1.4) + rozet(x0 + 13, 17, 'ABCD'[i], renk[i])
    # A palet
    x, y = 48, 52
    ic += f'<path d="M{x - 24} {y} a24 20 0 1 1 30 18 q-6 2 -4 -6 q2 -6 -8 -4 q-18 4 -18 -8 z" fill="#f3d9a4" stroke="{KAHVE}" stroke-width="1.2"/>'
    ic += ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="4" fill="{c}"/>' for dx, dy, c in [(-10, -8, KIR), (2, -12, MAVI), (12, -4, YES), (14, 8, ALTIN)])
    # B notalar
    x = 137
    ic += f'<ellipse cx="{x - 10}" cy="66" rx="7" ry="5" fill="{MAVI}" transform="rotate(-20 {x - 10} 66)"/><ellipse cx="{x + 14}" cy="60" rx="7" ry="5" fill="{MAVI}" transform="rotate(-20 {x + 14} 60)"/>'
    ic += f'<path d="M{x - 4} 64 V30 L{x + 20} 24 V58" fill="none" stroke="{MAVI}" stroke-width="2.4"/><path d="M{x - 4} 32 L{x + 20} 26 V32 L{x - 4} 38 Z" fill="{MAVI}"/>'
    # C satranç atı
    x = 226
    ic += (f'<path d="M{x - 14} 74 H{x + 16} V68 H{x - 14} Z M{x - 10} 68 L{x - 6} 50 Q{x - 16} 46 {x - 12} 38 L{x + 2} 28 Q{x + 16} 30 {x + 14} 48 L{x + 12} 68 Z" fill="{LAC}"/>'
           f'<circle cx="{x + 2}" cy="38" r="1.8" fill="#fff"/>')
    # D ağaç ve yaprak
    x = 315
    ic += f'<rect x="{x - 3}" y="52" width="6" height="22" fill="{KAHVE}"/><circle cx="{x}" cy="44" r="18" fill="{YES}"/><path d="M{x - 8} 44 q8 -14 16 0 q-8 10 -16 0" fill="#bff0c9"/><rect x="{x - 26}" y="74" width="52" height="4" rx="2" fill="#7fd08f"/>'
    return svg(360, 92, ic, 'Afişler: A boya paleti, B müzik notaları, C satranç atı, D ağaç ve yaprak', 21)


def konusma():
    ic = (f'<path d="M12 6 H236 a8 8 0 0 1 8 8 V34 a8 8 0 0 1 -8 8 H40 L26 54 L28 42 H12 a8 8 0 0 1 -8 -8 V14 a8 8 0 0 1 8 -8 Z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
          + yazi(18, 29, 'Ela: What is your favourite school club?', 12, LAC, 'start', True))
    ic += (f'<path d="M124 62 H348 a8 8 0 0 1 8 8 V90 a8 8 0 0 1 -8 8 H332 L334 110 L320 98 H124 a8 8 0 0 1 -8 -8 V70 a8 8 0 0 1 8 -8 Z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
           + yazi(130, 85, 'Can:', 12, LAC, 'start', True) + f'<line x1="166" y1="88" x2="344" y2="88" stroke="{TUR}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    return svg(360, 114, ic, 'Konuşma: Ela: What is your favourite school club? Can: boş', 24)


def zemin(x, y):
    return f'<circle cx="{x}" cy="{y}" r="24" fill="#fff"/>'


def levha(x, y, renk, yasak):
    ic = f'<circle cx="{x}" cy="{y}" r="24" fill="none" stroke="{renk}" stroke-width="4"/>'
    if yasak:
        ic += f'<line x1="{x - 17}" y1="{y - 17}" x2="{x + 17}" y2="{y + 17}" stroke="{renk}" stroke-width="4"/>'
    return ic


def levhalar():
    ic = ''
    yer = ['Library', 'Classroom', 'School', 'Science lab']
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 84, GRI_A, GRI, 8, 1.2) + yazi(x0 + 42, 82, yer[i], 11, LAC)
    # A ses dalgası (bağırma)
    x, y = 46, 38
    ic += zemin(x, y) + f'<path d="M{x - 10} {y - 6} h6 l8 -7 v26 l-8 -7 h-6 z" fill="{LAC}"/><path d="M{x + 8} {y - 6} q5 6 0 12 M{x + 12} {y - 10} q9 10 0 20" fill="none" stroke="{LAC}" stroke-width="1.8"/>' + levha(x, y, KIR, True)
    # B spor ayakkabı
    x = 135
    ic += zemin(x, y) + f'<path d="M{x - 14} {y - 4} q6 2 10 -4 l4 6 q8 2 14 8 v6 h-28 z" fill="{MAVI}"/><path d="M{x - 18} {y - 8} h-6 M{x - 18} {y - 2} h-8 M{x - 18} {y + 4} h-6" stroke="{SOLUK}" stroke-width="1.4"/>' + levha(x, y, KIR, True)
    # C sakız
    x = 224
    ic += zemin(x, y) + f'<rect x="{x - 12}" y="{y - 8}" width="24" height="16" rx="3" fill="#f7b6c8" stroke="#e57c93" stroke-width="1.2"/><line x1="{x - 4}" y1="{y - 8}" x2="{x - 4}" y2="{y + 8}" stroke="#e57c93"/>' + levha(x, y, KIR, True)
    # D koruyucu gözlük
    x = 313
    ic += zemin(x, y) + (f'<path d="M{x - 17} {y - 6} h34 v10 q-8 6 -13 0 h-8 q-5 6 -13 0 z" fill="#bfe3f5" stroke="{LAC}" stroke-width="1.6"/>'
           + levha(x, y, YES, False) + f'<path d="M{x + 10} {y + 12} l4 4 l8 -9" fill="none" stroke="{YES}" stroke-width="2.4"/>')
    return svg(360, 92, ic, 'Levhalar: kütüphanede bağırmak yasak, sınıfta koşmak yasak, okulda sakız yasak, fen laboratuvarında koruyucu gözlük takılır', 21)


def blog():
    ic = kutu(4, 4, 352, 96, '#fff', GRI, 8, 1.3) + f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MOR}"/><rect x="4" y="18" width="352" height="8" fill="{MOR}"/>'
    ic += yazi(16, 20, 'Our Class Blog · Rules', 12, '#fff', 'start')
    ic += yazi(18, 48, '1. Don’t be rude.', 12.5, LAC, 'start', True)
    ic += yazi(18, 70, '2.', 12.5, LAC, 'start', True) + f'<line x1="36" y1="72" x2="340" y2="72" stroke="{GRI}" stroke-dasharray="4 3"/>'
    ic += yazi(18, 92, '3.', 12.5, LAC, 'start', True) + f'<line x1="36" y1="94" x2="340" y2="94" stroke="{GRI}" stroke-dasharray="4 3"/>'
    return svg(360, 104, ic, 'Blog sayfası kuralları: 1. Don’t be rude. 2. boş 3. boş', 22)


def bayraklar():
    ic = ''
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 66, GRI_A, GRI, 8, 1) + rozet(x0 + 13, 17, 'ABCD'[i], LAC)
    # A Türkiye
    x, y = 20, 28
    ic += f'<rect x="{x}" y="{y}" width="60" height="38" fill="#e30a17"/><circle cx="{x + 23}" cy="{y + 19}" r="9.5" fill="#fff"/><circle cx="{x + 25.5}" cy="{y + 19}" r="7.6" fill="#e30a17"/>'
    sx, sy, r = x + 35, y + 19, 4.2
    ic += '<polygon points="' + ' '.join(f'{sx + (r if k % 2 == 0 else r * 0.4) * math.cos(math.pi + k * math.pi / 5):.1f},{sy + (r if k % 2 == 0 else r * 0.4) * math.sin(math.pi + k * math.pi / 5):.1f}' for k in range(10)) + '" fill="#fff"/>'
    # B Japonya
    x = 109
    ic += f'<rect x="{x}" y="{y}" width="60" height="38" fill="#fff" stroke="{GRI}" stroke-width="0.8"/><circle cx="{x + 30}" cy="{y + 19}" r="11" fill="#bc002d"/>'
    # C Fransa
    x = 198
    ic += f'<rect x="{x}" y="{y}" width="20" height="38" fill="#0055a4"/><rect x="{x + 20}" y="{y}" width="20" height="38" fill="#fff"/><rect x="{x + 40}" y="{y}" width="20" height="38" fill="#ef4135"/><rect x="{x}" y="{y}" width="60" height="38" fill="none" stroke="{GRI}" stroke-width="0.8"/>'
    # D Almanya
    x = 287
    ic += f'<rect x="{x}" y="{y}" width="60" height="12.7" fill="#000"/><rect x="{x}" y="{y + 12.7}" width="60" height="12.7" fill="#dd0000"/><rect x="{x}" y="{y + 25.4}" width="60" height="12.6" fill="#ffce00"/>'
    return svg(360, 74, ic, 'Bayraklar: A kırmızı zemin üzerinde beyaz ay yıldız, B beyaz zemin ortasında kırmızı daire, C dikey mavi, beyaz, kırmızı şeritler, D yatay siyah, kırmızı, sarı şeritler', 17)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = esyalar()
    s[3]['gorsel'] = plan()
    s[4]['gorsel'] = afisler()
    s[5]['gorsel'] = konusma()
    s[6]['gorsel'] = levhalar()
    s[8]['gorsel'] = blog()
    s[9]['gorsel'] = bayraklar()
