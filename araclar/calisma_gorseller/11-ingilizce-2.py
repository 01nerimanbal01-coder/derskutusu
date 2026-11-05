"""11. sınıf İngilizce 2. hafta görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def career_idioms_cards():
    cards = [
        ('1. Outside the Box', 'Creative Thinking', YES, YES_A),
        ('2. Climb Ladder', 'Steady Promotion', MAVI, MAVI_A),
        ('3. Midnight Oil', 'Hard Diligent Work', TUR, TUR_A),
        ('4. Learn the Ropes', 'Basic Procedures', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(cards):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.0, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Career idioms overview cards.', 34)

def outside_the_box_dialogue():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'ENTREPRENEURIAL DIALOGUE &amp; CREATIVITY', 10.3, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Startup Founder A', 9.6, TUR)
    ic += yazi(92, 76, 'To lead the robotics field,', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'we must [ ? ]', 8.8, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Target Idiom Solution', 9.6, YESIL_K)
    ic += yazi(267, 76, 'Think outside the box', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Innovative &amp; fresh methods', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Thinking outside the box dialogue card.', 34)

def connected_speech_card():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'CONNECTED SPEECH: AUXILIARY VERB REDUCTIONS', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Standard Written Form', 9.4, MAVI)
    ic += yazi(92, 76, 'I am going to start', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'I want to build a venture', 8.8, MAVI, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Natural Spoken Form', 9.4, TUR)
    ic += yazi(267, 76, 'I\'m gonna start', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'I wanna build a venture', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Connected speech reductions model.', 34)

def entrepreneur_traits_diagram():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'CORE QUALITIES OF SUCCESSFUL ENTREPRENEURS', 10.3, YESIL_K)
    ic += kutu(20, 38, 95, 68, '#ffffff', YES)
    ic += yazi(67, 58, 'Visionary', 9.4, YESIL_K)
    ic += yazi(67, 78, 'Future Trends', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'AI &amp; Tech Focus', 8.8, YESIL_K, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(179, 58, 'Risk Tolerant', 9.4, TUR)
    ic += yazi(179, 78, 'Bold Choices', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Calculated Risk', 8.8, TUR, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', MAVI)
    ic += yazi(292, 58, 'Resilient', 9.4, MAVI)
    ic += yazi(292, 78, 'Perseverance', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Overcomes Failure', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Core entrepreneurial traits diagram.', 34)

def startup_launch_steps():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'STAGES OF LAUNCHING A TECH VENTURE', 10.2, MOR)
    steps = [
        ('1. Concept', 'Identify Need', 16),
        ('2. Prototype', 'Test Product', 102),
        ('3. Pitch', 'Raise Funding', 188),
        ('4. Scale Up', 'Hire &amp; Grow', 274),
    ]
    for b, d, x in steps:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Startup development stages timeline.', 34)

def future_self_note_card():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'NOTE TO MY FUTURE SELF (CAREER MOTIVATION)', 10.3, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Target Ambition', 9.4, CAM)
    ic += yazi(92, 76, 'Dear Future Self,', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Master quantum AI computing', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Impact &amp; Growth', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Launch green tech enterprise', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Inspire future innovators', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Motivational note to future self card.', 34)

def reductions_matching_card():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'SPOKEN REDUCTIONS AND STANDARD FORMS', 10.1, YESIL_K)
    kartlar = [
        ('gonna', 'going to', 16),
        ('wanna', 'want to', 102),
        ('gotta', 'got to', 188),
        ('kinda', 'kind of', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 9.0, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.8, LAC, ince=True)
    return svg(360, 125, ic, 'Speech reductions matching card.', 34)

def career_password_boxes():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 24, 'KEYWORD PASSWORD BOXES', 10.4, TUR)
    harfler = ['C', 'A', 'R', 'E', 'E', 'R']
    for i, h in enumerate(harfler):
        x = 42 + i * 46
        ic += kutu(x, 42, 40, 52, '#ffffff', TUR, r=4)
        ic += yazi(x + 20, 74, h, 16.0, TUR)
        ic += yazi(x + 20, 36, f'{i + 1}. Letter', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Career keyword password boxes.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = career_idioms_cards()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = outside_the_box_dialogue()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = connected_speech_card()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = entrepreneur_traits_diagram()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = startup_launch_steps()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = future_self_note_card()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = reductions_matching_card()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = career_password_boxes()
    s[10]['en_fazla'] = 34
