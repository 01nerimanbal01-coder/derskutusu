"""11. sınıf İngilizce 1. hafta (Gelecek Planları, Meslekler ve Randevu) görselleri.
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


def career_terms_cards():
    cards = [
        ('1. Resume / CV', 'Skills &amp; Experience', MAVI, MAVI_A),
        ('2. Intent Letter', 'Goals &amp; Motivation', YES, YES_A),
        ('3. Interview', 'Professional Talk', TUR, TUR_A),
        ('4. Appointment', 'Scheduled Meeting', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Job application terminology cards.', 34)


def appointment_dialogue_card():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'FORMAL TELEPHONE APPOINTMENT DIALOGUE', 10.3, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Secretary', 9.6, CAM)
    ic += yazi(92, 76, 'Dr. Adams\' office,', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'how may I assist you?', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Caller / Patient', 9.6, YESIL_K)
    ic += yazi(267, 76, 'I would like to [ ? ]', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'for next Wednesday morning.', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Telephone appointment dialogue card.', 34)


def dark_clouds_prediction_card():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'PREDICTION BASED ON VISUAL EVIDENCE', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Visual Evidence', 9.6, MAVI)
    ic += yazi(92, 76, 'Dark storm clouds gathered', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Sky turned grey and windy', 8.8, MAVI, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Target Structure', 9.6, TUR)
    ic += yazi(267, 76, 'It is going to rain soon', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Definite evidence = be going to', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Prediction based on visual evidence card.', 34)


def future_forms_summary():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'FUTURE STRUCTURES: WILL VS. BE GOING TO', 10.3, TUR)
    ic += kutu(20, 38, 145, 68, '#ffffff', TUR)
    ic += yazi(92, 58, 'WILL / WON\'T', 9.6, TUR)
    ic += yazi(92, 78, 'Instant decision / Offer', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'General promise &amp; belief', 8.8, TUR, ince=True)

    ic += kutu(195, 38, 145, 68, YES_A, YES)
    ic += yazi(267, 58, 'BE GOING TO', 9.6, YESIL_K)
    ic += yazi(267, 78, 'Pre-planned arrangement', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Visible factual evidence', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Future structures comparative chart.', 34)


def job_application_steps_card():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'CAREER APPLICATION TIMELINE STEPS', 10.2, MOR)
    steps = [
        ('Step 1', 'Find Vacancy', 16),
        ('Step 2', 'Draft CV', 102),
        ('Step 3', 'Apply Online', 188),
        ('Step 4', 'Interview', 274),
    ]
    for b, d, x in steps:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Job application sequence timeline.', 34)


def job_vacancy_candidate_matching():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'JOB REQUIREMENTS &amp; CANDIDATE MATCHING', 10.2, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YESIL_K)
    ic += yazi(92, 56, 'Job Ad Requirements', 9.6, YESIL_K)
    ic += yazi(92, 76, 'App developer · Fluent English', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Team cooperation skills', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, MAVI_A, MAVI)
    ic += yazi(267, 56, 'Best Candidate Profile', 9.6, MAVI)
    ic += yazi(267, 76, 'Software graduate, bilingual,', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'proven team player skills', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Job requirement matching card.', 34)


def future_usage_examples():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'LANGUAGE FUNCTION EXAMPLES', 10.1, CAM)
    kartlar = [
        ('Offer Help', 'I will carry', 16),
        ('Planned Idea', 'Going to open', 102),
        ('Promise', 'I won\'t share', 188),
        ('Prediction', 'Going to fall', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', CAM)
        ic += yazi(x + 35, 54, s, 8.8, CAM)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.5, LAC, ince=True)
    return svg(360, 125, ic, 'Language function examples card.', 34)


def plan_password_boxes():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'KEYWORD PASSWORD BOXES', 10.4, YESIL_K)
    harfler = ['P', 'L', 'A', 'N']
    for i, h in enumerate(harfler):
        x = 75 + i * 56
        ic += kutu(x, 42, 48, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 24, 74, h, 16.0, YESIL_K)
        ic += yazi(x + 24, 36, f'{i + 1}. Letter', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Plan keyword password boxes.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = career_terms_cards()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = appointment_dialogue_card()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = dark_clouds_prediction_card()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = future_forms_summary()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = job_application_steps_card()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = job_vacancy_candidate_matching()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = future_usage_examples()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = plan_password_boxes()
    s[10]['en_fazla'] = 34
