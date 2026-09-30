"""6. sınıf İngilizce 4. hafta (roles, responsibilities, school routines, object pronouns) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""

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


def s_bayrak(x, y):
    return (f'<line x1="{x - 10}" y1="{y - 14}" x2="{x - 10}" y2="{y + 14}" stroke="{KAHVE}" stroke-width="2"/>'
            f'<rect x="{x - 9}" y="{y - 14}" width="22" height="14" fill="#e30a17"/><circle cx="{x}" cy="{y - 7}" r="3.6" fill="#fff"/><circle cx="{x + 1}" cy="{y - 7}" r="2.9" fill="#e30a17"/>')


def s_mikrofon(x, y):
    return (f'<rect x="{x - 5}" y="{y - 14}" width="10" height="16" rx="5" fill="{LAC}"/><path d="M{x - 9} {y - 4} a9 9 0 0 0 18 0" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
            f'<line x1="{x}" y1="{y + 5}" x2="{x}" y2="{y + 12}" stroke="{LAC}" stroke-width="1.8"/><line x1="{x - 6}" y1="{y + 12}" x2="{x + 6}" y2="{y + 12}" stroke="{LAC}" stroke-width="1.8"/>')


def s_nota(x, y):
    return (f'<ellipse cx="{x - 6}" cy="{y + 8}" rx="5" ry="3.6" fill="{MOR}"/><ellipse cx="{x + 8}" cy="{y + 5}" rx="5" ry="3.6" fill="{MOR}"/>'
            f'<path d="M{x - 2} {y + 7} V{y - 12} L{x + 12} {y - 15} V{y + 4}" fill="none" stroke="{MOR}" stroke-width="2"/>')


def s_susleme(x, y):
    ic = f'<path d="M{x - 18} {y - 10} Q{x} {y + 2} {x + 18} {y - 10}" fill="none" stroke="{SOLUK}" stroke-width="1"/>'
    for k, c in enumerate([KIR, ALTIN, MAVI, YES, TUR]):
        px = x - 16 + k * 8
        py = y - 10 + 12 * (1 - ((px - x) / 18) ** 2) - 1
        ic += f'<path d="M{px - 4} {py} L{px + 4} {py} L{px} {py + 8} Z" fill="{c}"/>'
    return ic


def gorev_cizelgesi():
    ic = kutu(4, 4, 352, 112, '#fff', GRI, 8, 1.3) + f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{KIR}"/><rect x="4" y="18" width="352" height="8" fill="{KIR}"/>'
    ic += yazi(180, 20, '29 October Ceremony · Roles', 12, '#fff')
    kisi = [('Ali', s_bayrak), ('Zeynep', s_mikrofon), ('Ece', s_nota), ('Can', s_susleme)]
    for i, (ad, f) in enumerate(kisi):
        x0 = 12 + i * 86
        ic += kutu(x0, 34, 78, 74, GRI_A, GRI, 6, 1) + f(x0 + 39, 64) + yazi(x0 + 39, 100, ad, 12, LAC)
    return svg(360, 120, ic, 'Görev çizelgesi: Ali bayrak, Zeynep mikrofon, Ece müzik notası, Can süsleme', 26)


def karne():
    ders = [('Maths', '95'), ('Science', '92'), ('English', '98'), ('Turkish', '94')]
    ic = kutu(4, 4, 352, 100, '#fff', MAVI, 8, 1.4) + yazi(180, 24, 'Ada Yılmaz · Report Card', 12.5, MAVI)
    for i, (d, n) in enumerate(ders):
        x0 = 14 + i * 85
        ic += kutu(x0, 36, 78, 58, MAVI_A, MAVI, 6, 1) + yazi(x0 + 39, 56, d, 11.5, LAC, 'middle', True) + yazi(x0 + 39, 82, n, 17, YES)
    return svg(360, 108, ic, 'Ada’nın karnesi: Maths 95, Science 92, English 98, Turkish 94', 22)


def haftalik():
    gun = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    satir = [('walk to school', [1, 1, 1, 1, 1]), ('take the bus', [0, 0, 0, 0, 0]), ('read a book', [0, 1, 0, 0, 1]), ('do homework', [1, 1, 1, 1, 1])]
    ic = kutu(4, 4, 352, 126, '#fff', GRI, 6, 1.2) + yazi(180, 21, 'Hakan’s week', 12.5, LAC)
    for j, g in enumerate(gun):
        ic += yazi(150 + j * 44, 42, g, 11, SOLUK)
    for i, (a, v) in enumerate(satir):
        y = 50 + i * 19
        ic += f'<rect x="10" y="{y}" width="340" height="18" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>' + yazi(16, y + 13, a, 11.5, LAC, 'start', True)
        for j, t in enumerate(v):
            cx = 150 + j * 44
            if t:
                ic += f'<path d="M{cx - 5} {y + 9} l4 4 l7 -8" fill="none" stroke="{YES}" stroke-width="2.2"/>'
            else:
                ic += f'<path d="M{cx - 4} {y + 5} l8 8 M{cx + 4} {y + 5} l-8 8" stroke="{KIR}" stroke-width="1.8"/>'
    return svg(360, 134, ic, 'Hakan’s week: walk to school her gün, take the bus hiçbir gün, read a book salı ve cuma, do homework her gün', 28)


def mert_karti():
    ic = kutu(4, 4, 352, 70, TUR_A, TUR, 10, 1.4) + yazi(18, 26, 'Mert:', 12.5, TUR, 'start')
    ic += yazi(18, 46, '“I always walk to school.', 12.5, LAC, 'start', True) + yazi(18, 64, 'I never take the bus.”', 12.5, LAC, 'start', True)
    return svg(360, 78, ic, 'Mert: I always walk to school. I never take the bus.', 17)


def rutinler():
    ic = ''
    for i in range(3):
        x0 = 4 + i * 119
        ic += kutu(x0, 4, 114, 76, [TUR_A, CAM_A, MOR_A][i], [TUR, CAM, MOR][i], 8, 1.2) + rozet(x0 + 14, 17, str(i + 1), [TUR, CAM, MOR][i])
    # 1 zil ve sıra olmuş ayak izleri
    x = 61
    ic += (f'<path d="M{x - 12} 44 a12 12 0 0 1 24 0 v6 h4 v4 h-32 v-4 h4 z" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1"/><circle cx="{x}" cy="58" r="3" fill="{KAHVE}"/>'
           f'<path d="M{x + 18} 36 q5 6 0 12 M{x - 18} 36 q-5 6 0 12" fill="none" stroke="{SOLUK}" stroke-width="1.4"/>'
           + ''.join(f'<ellipse cx="{x - 30 + k * 15}" cy="70" rx="4" ry="2.4" fill="{TUR}"/>' for k in range(5)))
    # 2 sıra ve bez
    x = 180
    ic += (f'<rect x="{x - 34}" y="40" width="68" height="8" rx="2" fill="#c98a4a"/><rect x="{x - 30}" y="48" width="4" height="22" fill="{KAHVE}"/><rect x="{x + 26}" y="48" width="4" height="22" fill="{KAHVE}"/>'
           f'<rect x="{x - 8}" y="30" width="22" height="12" rx="3" fill="{CAM}"/><path d="M{x - 26} 34 q4 -4 8 0 M{x + 22} 30 q4 -4 8 0" fill="none" stroke="{CAM}" stroke-width="1.2"/>')
    # 3 kitap ve takvim
    x = 299
    ic += (f'<rect x="{x - 30}" y="34" width="26" height="34" rx="2" fill="{MOR}"/><rect x="{x - 27}" y="37" width="3" height="28" fill="#fff" opacity="0.6"/>'
           f'<rect x="{x + 2}" y="34" width="30" height="32" rx="3" fill="#fff" stroke="{GRI}"/><rect x="{x + 2}" y="34" width="30" height="9" rx="3" fill="{KIR}"/>'
           f'<path d="M{x + 10} 56 l4 4 l8 -9" fill="none" stroke="{YES}" stroke-width="2"/><path d="M{x - 2} 50 h4" stroke="{SOLUK}" stroke-width="1.6"/>')
    return svg(360, 84, ic, 'Resimler: 1 çalan zil ve sıraya girmiş ayak izleri, 2 temizlenen sıra, 3 kitap ve işaretli takvim', 19)


def konusma():
    ic = (f'<path d="M12 6 H346 a8 8 0 0 1 8 8 V34 a8 8 0 0 1 -8 8 H40 L26 54 L28 42 H12 a8 8 0 0 1 -8 -8 V14 a8 8 0 0 1 8 -8 Z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
          + yazi(18, 29, 'Selin: Can you give', 11.5, LAC, 'start', True) + f'<line x1="140" y1="31" x2="172" y2="31" stroke="{MAVI}" stroke-width="1.4" stroke-dasharray="3 2"/>'
          + yazi(176, 29, 'some pencils? We need them.', 11.5, LAC, 'start', True))
    ic += (f'<path d="M180 62 H348 a8 8 0 0 1 8 8 V86 a8 8 0 0 1 -8 8 H332 L334 106 L320 94 H180 a8 8 0 0 1 -8 -8 V70 a8 8 0 0 1 8 -8 Z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
           + yazi(188, 83, 'Emre: Sure, here you are.', 11.5, LAC, 'start', True))
    return svg(360, 110, ic, 'Konuşma: Selin: Can you give boş some pencils? We need them. Emre: Sure, here you are.', 23)


def afis():
    ic = kutu(4, 4, 352, 98, KIR_A, KIR, 10, 1.6) + f'<rect x="4" y="4" width="352" height="26" rx="10" fill="{KIR}"/><rect x="4" y="20" width="352" height="10" fill="{KIR}"/>'
    ic += yazi(180, 22, 'Republic Day Ceremony · Volunteers wanted!', 12.5, '#fff')
    rol = ['reading a poem', 'carrying the flag', 'singing in the choir', 'guiding the programme']
    for i, r in enumerate(rol):
        x, y = 22 + (i % 2) * 170, 52 + (i // 2) * 28
        ic += f'<circle cx="{x}" cy="{y - 4}" r="4" fill="{KIR}"/>' + yazi(x + 10, y, r, 12, LAC, 'start', True)
    return svg(360, 106, ic, 'Tören afişi: Republic Day Ceremony, volunteers wanted: reading a poem, carrying the flag, singing in the choir, guiding the programme', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gorev_cizelgesi()
    s[3]['gorsel'] = karne()
    s[4]['gorsel'] = haftalik()
    s[6]['gorsel'] = mert_karti()
    s[7]['gorsel'] = rutinler()
    s[9]['gorsel'] = konusma()
    s[10]['gorsel'] = afis()
