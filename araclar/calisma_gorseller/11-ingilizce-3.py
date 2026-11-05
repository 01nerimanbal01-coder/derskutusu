"""11. sınıf İngilizce 3. hafta (Future Continuous and Career Documents) görselleri.
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


def career_vocab_cards():
    kartlar = [
        ('1. Cover Letter', 'Applicant Motivation', MAVI, MAVI_A),
        ('2. Resume / CV', 'Experience &amp; Skills', YES, YES_A),
        ('3. Soft Skills', 'Empathy &amp; Teamwork', TUR, TUR_A),
        ('4. Hard Skills', 'Technical Mastery', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.0, LAC, ince=True)
    return svg(360, 125, ic, 'Career and recruitment vocabulary cards.', 34)


def future_continuous_timeline():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'FUTURE CONTINUOUS TENSE: ACTION IN PROGRESS', 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Tomorrow at 10 AM', 9.2, MAVI)
    ic += yazi(92, 76, 'Action ongoing in future', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'will be presenting...', 8.6, YESIL_K, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'Grammar Formula', 9.2, TUR)
    ic += yazi(267, 76, 'Subject + will be', 8.6, LAC, ince=True)
    ic += yazi(267, 92, '+ Verb-ing (Present Participle)', 8.2, TUR, ince=True)
    return svg(360, 125, ic, 'Future continuous tense timeline diagram.', 34)


def interview_qa_model():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'PROFESSIONAL INTERVIEW RESPONSE STRUCTURE (STAR)', 9.8, YESIL_K)
    steps = [
        ('1. Situation', 'Context &amp; background', 16),
        ('2. Task', 'Core challenge faced', 102),
        ('3. Action', 'Strategic steps taken', 188),
        ('4. Result', 'Measurable outcome', 274),
    ]
    for b, a, x in steps:
        ic += kutu(x, 36, 70, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'STAR interview technique diagram.', 34)


def work_schedule_diagram():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'WORKPLACE FUTURE SCHEDULE COMPARISON', 10.0, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Future Simple', 9.2, TUR)
    ic += yazi(92, 76, 'Spontaneous decision', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'I will call the client.', 8.6, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(267, 56, 'Future Continuous', 9.2, MAVI)
    ic += yazi(267, 76, 'Scheduled progression', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'I will be testing safety.', 8.6, MAVI, ince=True)
    return svg(360, 125, ic, 'Future simple vs future continuous diagram.', 34)


def skills_matrix_table():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'HARD SKILLS VS SOFT SKILLS MATRIX', 9.8, MOR)
    satirlar = [
        ('Category', 'Core Focus', 'Workplace Examples', MOR),
        ('Hard Skills', 'Technical competence', 'Coding, Analytics, Design', MAVI),
        ('Soft Skills', 'Human interaction', 'Communication, Empathy', YESIL_K),
        ('Combined', 'Synergistic output', 'High-performing teams', TUR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(70, y + 13, k1, 8.4, r)
        ic += yazi(180, y + 13, k2, 8.2, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.2, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Skills matrix comparison table.', 34)


def job_ad_sections_diagram():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'SECTIONS OF A FORMAL JOB ADVERTISEMENT', 10.0, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, '1. Qualifications', 9.2, CAM)
    ic += yazi(92, 76, 'Required education degree', 8.4, LAC, ince=True)
    ic += yazi(92, 92, 'Minimum years of experience', 8.4, CAM, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, '2. Responsibilities', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Daily tasks and milestones', 8.4, LAC, ince=True)
    ic += yazi(267, 92, 'Deliverable expectations', 8.4, YES, ince=True)
    return svg(360, 125, ic, 'Job advertisement sections diagram.', 34)


def workplace_timeline_cards():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'WORKPLACE DAILY SCHEDULE TIMELINE', 10.0, TUR)
    kartlar = [
        ('09:00 AM', 'Team Standup Meeting', 16),
        ('11:30 AM', 'Code Review Session', 102),
        ('02:00 PM', 'Client Video Briefing', 188),
        ('04:30 PM', 'Quality Assurance Test', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.4, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Workplace daily timeline cards.', 34)


def cover_letter_structure_boxes():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'LETTER OF INTENT (COVER LETTER) SECTIONS', 10.0, YESIL_K)
    kutular = ['Header &amp; Date', 'Salutation', 'Body Paragraphs', 'Sign-off']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'Section {i + 1}', 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, 'Cover letter structure flowchart boxes.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = career_vocab_cards()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = future_continuous_timeline()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = interview_qa_model()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = work_schedule_diagram()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = skills_matrix_table()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = job_ad_sections_diagram()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = workplace_timeline_cards()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = cover_letter_structure_boxes()
    s[10]['en_fazla'] = 34
