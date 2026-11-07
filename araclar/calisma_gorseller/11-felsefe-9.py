"""11. sınıf Felsefe 9. hafta görselleri: teknoloji ve ontoloji (SVG kavram şemaları; insan figürü yok)."""
LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK, KAHVE = '#9aa6bd', '#f3f5f9', '#5b6479', '#8a5a2b'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def kutu(x, y, w, h, d, c, r=7):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{d}" stroke="{c}" stroke-width="1"/>'


def ok(x1, y1, x2, y2, renk=LAC):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 9 * math.cos(a) + 4.5 * math.sin(a), y2 - 9 * math.sin(a) - 4.5 * math.cos(a))
    p2 = (x2 - 9 * math.cos(a) - 4.5 * math.sin(a), y2 - 9 * math.sin(a) + 4.5 * math.cos(a))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 7 * math.cos(a):.1f}" y2="{y2 - 7 * math.sin(a):.1f}" stroke="{renk}" stroke-width="1.6"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{renk}"/>')


def degirmen_santral():
    ic = cerceve(360, 170) + kutu(10, 10, 166, 150, YES_A, YES) + kutu(184, 10, 166, 150, MAVI_A, MAVI)
    ic += yazi(93, 30, 'Geleneksel zanaat', 12, YES) + yazi(267, 30, 'Modern teknoloji', 12, MAVI)
    # yel değirmeni
    ic += f'<polygon points="82,118 104,118 99,66 87,66" fill="#efe3cf" stroke="{KAHVE}" stroke-width="1.2"/>'
    for d in ('M 93 62 L 93 34', 'M 93 62 L 121 62', 'M 93 62 L 93 90', 'M 93 62 L 65 62'):
        ic += f'<path d="{d}" stroke="{KAHVE}" stroke-width="5" stroke-linecap="round"/>'
    ic += f'<circle cx="93" cy="62" r="4" fill="{LAC}"/>'
    ic += f'<path d="M 22 118 Q 60 110 164 118" fill="none" stroke="{YES}" stroke-width="2"/>'
    ic += yazi(93, 140, 'Rüzgârla birlikte çalışır,', 10.5, LAC, ince=True) + yazi(93, 153, 'onu depolamaz', 10.5, LAC, ince=True)
    # baraj
    ic += f'<path d="M 196 60 L 250 60 L 250 118 L 196 118 Z" fill="#cfe0fb"/>'
    ic += f'<polygon points="250,52 268,52 284,118 250,118" fill="#c9cfdb" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<path d="M 284 112 Q 310 106 340 112" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="300" y1="64" x2="300" y2="100" stroke="{LAC}" stroke-width="1.4"/><line x1="320" y1="64" x2="320" y2="100" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<path d="M 300 70 L 320 76 L 300 82 L 320 88 L 300 94" fill="none" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(267, 140, 'Nehri enerji deposu', 10.5, LAC, ince=True) + yazi(267, 153, 'olarak görür', 10.5, LAC, ince=True)
    return svg(ic, 360, 170, 'Yel değirmeni ile hidroelektrik santralinin karşılaştırılması', 36)


def cince_oda():
    ic = cerceve(360, 150)
    ic += f'<rect x="120" y="22" width="120" height="96" rx="4" fill="#fff" stroke="{LAC}" stroke-width="2"/>'
    ic += yazi(180, 16, 'Kapalı oda', 11.5, LAC)
    ic += kutu(140, 46, 80, 40, TUR_A, TUR, 4) + yazi(180, 64, 'Kural', 11.5, TUR) + yazi(180, 78, 'kitabı', 11.5, TUR)
    ic += yazi(180, 108, 'Çince bilinmiyor', 10.5, SOLUK, ince=True)
    ic += ok(20, 56, 118, 56, MAVI) + yazi(66, 46, 'Çince sorular', 11, MAVI)
    ic += ok(242, 84, 340, 84, YES) + yazi(292, 74, 'Çince yanıtlar', 11, YES)
    ic += yazi(180, 140, 'Dışarıdan bakan: “İçerisi Çince anlıyor.”', 11, KIR, ince=True)
    return svg(ic, 360, 150, 'Çince Odası düşünce deneyi şeması', 32)


def simulakr():
    ic = cerceve(360, 112)
    k = [(10, 'Gerçek', MAVI, MAVI_A), (128, 'Gerçeğin yerini', YES, YES_A), (246, '?', KIR, KIR_A)]
    for x, t, c, a in k:
        ic += kutu(x, 22, 104, 56, a, c)
    ic += yazi(62, 55, 'Gerçek', 13, MAVI)
    ic += yazi(180, 46, 'Gerçeğin yerini', 11, YES) + yazi(180, 62, 'alan kopya', 11, YES)
    ic += yazi(298, 60, '?', 22, KIR)
    ic += ok(115, 50, 127, 50) + ok(233, 50, 245, 50)
    ic += yazi(298, 96, 'gerçekten daha gerçek', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 112, 'Simülasyon kuramı zinciri', 26)


def kartlar():
    k = ['Yaşlanma ve hastalık teknolojiyle aşılabilir.', 'Genetik tasarım insan onurunu zedeler.',
         'Erişim eşitsizliği biyolojik bir kast doğurabilir.', 'İnsan kapasitesi protezlerle artırılmalıdır.']
    ic = cerceve(360, 150)
    for i, t in enumerate(k):
        y = 10 + i * 34
        ic += kutu(10, y, 340, 28, '#fff', GRI, 6)
        ic += f'<circle cx="28" cy="{y + 14}" r="9" fill="{MOR}"/>' + yazi(28, y + 18, str(i + 1), 11, '#fff')
        ic += yazi(46, y + 18.5, t, 11.5, LAC, 'start', True)
    return svg(ic, 360, 150, 'Dört görüş kartı', 34)


def venn():
    ic = cerceve(360, 132)
    ic += f'<circle cx="136" cy="60" r="48" fill="{MAVI}" fill-opacity="0.18" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<circle cx="224" cy="60" r="48" fill="{MOR}" fill-opacity="0.18" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(122, 56, 'Fiziksel', 11, MAVI) + yazi(122, 71, 'mekân', 11, MAVI)
    ic += yazi(238, 56, 'Dijital', 11, MOR) + yazi(238, 71, 'mekân', 11, MOR)
    ic += yazi(180, 56, 'VR', 10, LAC) + yazi(180, 70, 'avatar', 10, LAC)
    ic += yazi(180, 126, 'Sınırlar iç içe geçiyor', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 132, 'Fiziksel ve dijital mekânın kesişimi', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = degirmen_santral()
    s[2]['gorsel'] = cince_oda()
    s[4]['gorsel'] = simulakr()
    s[8]['gorsel'] = kartlar()
    s[10]['gorsel'] = venn()
