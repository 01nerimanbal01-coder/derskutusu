"""6. sınıf İngilizce 14. hafta (Theme 3: Personal Life) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#475569'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def uygula(o):
    s = o['sorular']

    # s[0]: 3 Question Cards (Appearance / Personality / Belongings)
    ic0 = kutu(4, 4, 352, 107, GRI_A, GRI)
    q_cards = [
        ('APPEARANCE', 'What does he', 'look like?', MAVI, MAVI_A),
        ('PERSONALITY', 'What is she', 'like?', YES, YES_A),
        ('BELONGINGS', 'Whose trainers', 'are these?', TUR, TUR_A),
    ]
    for i, (b, l1, l2, c, d) in enumerate(q_cards):
        x = 10 + i * 115
        ic0 += kutu(x, 11, 110, 93, d, c)
        ic0 += yazi(x + 55, 29, b, 8.8, c)
        ic0 += f'<line x1="{x+10}" y1="38" x2="{x+100}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic0 += yazi(x + 55, 62, l1, 8.8, LAC)
        ic0 += yazi(x + 55, 80, l2, 8.8, LAC)
    s[0]['gorsel'] = svg(ic0, 'Appearance, personality and belongings question cards')

    # s[1]: Sports Bag, Trainers and Protective Knee/Ankle Pads (no human figures)
    ic1 = kutu(6, 6, 348, 103, CAM_A, CAM)
    # Spor çantası çizimi
    ic1 += kutu(20, 38, 86, 52, '#f8fafc', CAM, r=8, kalin=1.3)
    ic1 += f'<path d="M42,38 C42,20 84,20 84,38" fill="none" stroke="{CAM}" stroke-width="2"/>'
    ic1 += yazi(63, 68, 'SPORTS KIT', 8.2, CAM)
    ic1 += kutu(122, 16, 218, 38, '#f8fafc', MAVI, r=5)
    ic1 += yazi(231, 33, 'Protective Pads · Safety Gear', 8.8, MAVI)
    ic1 += yazi(231, 47, 'Protect: knees and ankles in football', 8.2, LAC, ince=True)
    ic1 += kutu(122, 61, 218, 38, YES_A, YES, r=5)
    ic1 += yazi(231, 78, 'Healthy Exercise Benefits', 8.6, YES)
    ic1 += yazi(231, 92, 'Strong heart, stomach and back', 8.0, SOLUK, ince=True)
    s[1]['gorsel'] = svg(ic1, 'Sports kit bag and knee-ankle protection card')

    # s[2]: Grammar Reference Cards (-er / more / plural-uncountable)
    ic2 = kutu(4, 4, 352, 107, GRI_A, GRI)
    gram = [
        ('1-Syllable Adj.', 'tall → taller', 'slim → slimmer', MAVI, MAVI_A),
        ('2+ Syllables', 'more generous', 'more outgoing', MOR, MOR_A),
        ('Noun Agreement', 'trainers → ARE', 'jewellery → IS', TUR, TUR_A),
    ]
    for i, (b, g1, g2, c, d) in enumerate(gram):
        x = 10 + i * 115
        ic2 += kutu(x, 11, 110, 93, d, c)
        ic2 += yazi(x + 55, 29, b, 8.6, c)
        ic2 += f'<line x1="{x+10}" y1="38" x2="{x+100}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic2 += yazi(x + 55, 62, g1, 8.4, LAC)
        ic2 += yazi(x + 55, 82, g2, 8.4, c)
    s[2]['gorsel'] = svg(ic2, 'Comparative adjectives and noun agreement cards')

    # s[5]: Selin’s Wardrobe: Usually vs Today (hanger and jersey icons, no person)
    ic5 = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic5 += yazi(91, 22, 'USUALLY (Weekdays)', 8.8, MAVI)
    # Askıda okul forması (geometrik tişört/ceket)
    ic5 += f'<polygon points="71,36 111,36 122,48 112,54 106,48 106,74 76,74 76,48 70,54 60,48" fill="#f8fafc" stroke="{MAVI}" stroke-width="1.2"/>'
    ic5 += yazi(91, 93, 'School Uniform (Present Simple)', 7.8, LAC)

    ic5 += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic5 += yazi(269, 22, 'TODAY / RIGHT NOW', 8.8, TUR)
    ic5 += f'<polygon points="249,36 289,36 300,48 290,54 284,48 284,74 254,74 254,48 248,54 238,48" fill="#f8fafc" stroke="{TUR}" stroke-width="1.2"/>'
    ic5 += yazi(269, 60, '10', 9.5, TUR)
    ic5 += yazi(269, 93, 'Sports Kit and Trainers (-ing)', 7.8, LAC)
    s[5]['gorsel'] = svg(ic5, 'Wardrobe comparison between weekday routine and today')

    # s[6]: Accessories Showcase (Necklace, Bracelet, Wallet)
    ic6 = kutu(4, 4, 352, 107, GRI_A, GRI)
    acc = [
        ('NECKLACE / CHAIN', 'around the neck', MOR, MOR_A, 'circle'),
        ('BRACELET', 'on the wrist', CAM, CAM_A, 'oval'),
        ('WALLET / PURSE', 'in the pocket / bag', YES, YES_A, 'rect'),
    ]
    for i, (b, alt, c, d, sekil) in enumerate(acc):
        x = 10 + i * 115
        ic6 += kutu(x, 11, 110, 93, d, c)
        ic6 += yazi(x + 55, 27, b, 8.3, c)
        if sekil == 'circle':
            ic6 += f'<circle cx="{x+55}" cy="55" r="14" fill="none" stroke="{c}" stroke-width="1.6"/><circle cx="{x+55}" cy="71" r="3.5" fill="{c}"/>'
        elif sekil == 'oval':
            ic6 += f'<ellipse cx="{x+55}" cy="56" rx="18" ry="11" fill="none" stroke="{c}" stroke-width="1.8" stroke-dasharray="4,2"/>'
        else:
            ic6 += kutu(x + 35, 44, 40, 24, '#f8fafc', c, r=3, kalin=1.3) + kutu(x + 61, 52, 14, 8, d, c, r=2)
        ic6 += yazi(x + 55, 91, alt, 8.0, LAC, ince=True)
    s[6]['gorsel'] = svg(ic6, 'Accessories showcase with necklace, bracelet and wallet')

    # s[7]: Two Data Cards (Arda vs Bora)
    ic7 = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic7 += yazi(91, 24, 'PROFILE CARD · ARDA', 9.0, MAVI)
    ic7 += yazi(91, 50, 'Height: 162 cm', 9.0, LAC)
    ic7 += yazi(91, 70, 'Social trait: Quiet / Shy (+)', 8.2, SOLUK, ince=True)
    ic7 += yazi(91, 90, 'Hair: Short straight', 8.0, MAVI, ince=True)

    ic7 += kutu(184, 6, 170, 103, YES_A, YES)
    ic7 += yazi(269, 24, 'PROFILE CARD · BORA', 9.0, YES)
    ic7 += yazi(269, 50, 'Height: 154 cm', 9.0, LAC)
    ic7 += yazi(269, 70, 'Social trait: Outgoing (+++)', 8.2, SOLUK, ince=True)
    ic7 += yazi(269, 90, 'Hair: Curly brown', 8.0, YES, ince=True)
    s[7]['gorsel'] = svg(ic7, 'Arda and Bora height and personality data cards')

    # s[8]: Lost Bracelet Dialogue Flow (4 steps)
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    flow = [
        ('1. Find Item', 'Silver bracelet!', MAVI, MAVI_A),
        ('2. Ask Owner', 'Whose is it?', TUR, TUR_A),
        ('3. Identify', 'Defne’s jewellery', MOR, MOR_A),
        ('4. Return It', 'Give it back now', YES, YES_A),
    ]
    for i, (b, alt, c, d) in enumerate(flow):
        x = 10 + i * 86
        ic8 += kutu(x, 14, 80, 87, d, c)
        ic8 += yazi(x + 40, 38, b, 8.4, c)
        ic8 += f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.7"/>'
        ic8 += yazi(x + 40, 74, alt, 7.8, LAC, ince=True)
        if i < 3:
            ic8 += f'<polygon points="{x+81},57 {x+85},52 {x+85},62" fill="{c}"/>'
    s[8]['gorsel'] = svg(ic8, 'Four-step lost and found bracelet dialogue flow')

    # s[9]: Character Qualities Chart
    ic9 = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic9 += yazi(180, 22, 'CHARACTER QUALITIES CHECKLIST', 9.2, MOR)
    ic9 += kutu(18, 32, 154, 66, '#f8fafc', YES, r=5)
    ic9 += yazi(95, 50, 'Trait 1: Shares items', 8.6, YES)
    ic9 += yazi(95, 68, 'Helps friends in need', 8.0, LAC, ince=True)
    ic9 += yazi(95, 86, '→ GENEROUS', 8.8, YES)

    ic9 += kutu(188, 32, 154, 66, '#f8fafc', MAVI, r=5)
    ic9 += yazi(265, 50, 'Trait 2: Keeps secrets', 8.6, MAVI)
    ic9 += yazi(265, 68, 'Never breaks promises', 8.0, LAC, ince=True)
    ic9 += yazi(265, 86, '→ RELIABLE', 8.8, MAVI)
    s[9]['gorsel'] = svg(ic9, 'Generous and reliable character traits checklist')
