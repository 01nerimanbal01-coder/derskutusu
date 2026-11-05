"""12. sınıf İngilizce 3. hafta (Music Preferences & Survey Report) çalışma kâğıdı görselleri."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'

YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def dort_muzik_terimi_karti():
    kartlar = [
        ('1. Acoustic', 'Natural Instruments · Unplugged', MAVI, MAVI_A),
        ('2. Survey', 'Data Analysis · Statistics', YES, YES_A),
        ('3. Melody', 'Catchy Tune · Memorable', TUR, TUR_A),
        ('4. Opinion', 'Polite Agreement · Respect', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:
            ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.0, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' · ')[1], 8.8, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Four music vocabulary cards.", 34)

def music_survey_chart_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "SCHOOL MUSIC PREFERENCE SURVEY RESULTS", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Pop &amp; Rock: 65%", 10.0, YES)
    ic += yazi(95, 74, "Vast majority of students", 9.0, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, MOR_A, MOR)
    ic += yazi(265, 54, "Classical: 15%", 10.0, MOR)
    ic += yazi(265, 74, "Small minority of listeners", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Music survey results chart panel.", 34)

def opinion_agreement_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "EXPRESSING STRONG AND POLITE AGREEMENT", 10.5, YES)
    ic += yazi(180, 52, "“I completely AGREE with your viewpoint on this song.”", 10.0, LAC)
    ic += yazi(180, 76, "Sharing common feelings and mutual appreciation politely", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Expressing agreement panel.", 34)

def agreement_contrast_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "OPINION EXPRESSION CONVERSATION DYNAMICS", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, YES_A, YES)
    ic += yazi(92, 56, "Polite Agreement", 10.0, YES)
    ic += yazi(92, 74, "That is exactly how I feel", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, KIR_A, KIR)
    ic += yazi(267, 56, "Gentle Disagreement", 10.0, KIR)
    ic += yazi(267, 74, "I see your point, but...", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Opinion conversation dynamics diagram.", 34)

def survey_writing_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "SURVEY REPORT WRITING STAGES", 10.5, MAVI)
    adimlar = ["1. Questions", "2. Data Stats", "3. Analysis", "4. Report"]
    for i, a in enumerate(adimlar):
        x = 16 + i * 82
        ic += kutu(x, 42, 76, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 38, 70, a, 9.4, LAC)
        if i < 3:
            ic += yazi(x + 80, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Survey writing stages sequence.", 34)

def dialogue_opinion_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "CONVERSATION ON MUSIC STYLES", 10.5, MOR)
    ic += yazi(180, 52, "Mark: 'Heavy metal music is too loud and exhausting.'", 9.8, LAC)
    ic += yazi(180, 76, "Lisa: 'I see your point, but electric guitar solos require talent.'", 9.2, YES, ince=True)
    return svg(360, 110, ic, "Dialogue on music styles panel.", 34)

def dort_intonation_karti():
    kartlar = [
        ('1. Yes/No Q.', 'Rising Intonation (↗)', MAVI, MAVI_A),
        ('2. Wh- Quest.', 'Falling Intonation (↘)', YES, YES_A),
        ('3. Lists', 'Rise then Fall (↗↘)', TUR, TUR_A),
        ('4. Invitation', 'Rising Polite (↗)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Four intonation patterns card.", 34)

def sifre_rhythm_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "MUSIC TERMINOLOGY WORD PUZZLE", 10.8, TUR)
    ic += yazi(180, 50, "RAP · HARMONY · YOUTH · TEMPO · HIT · MELODY", 9.4, LAC)
    ic += yazi(180, 76, "Solve the clues to uncover the hidden musical element (6 letters).", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Password rhythm music puzzle panel.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_muzik_terimi_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = music_survey_chart_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = opinion_agreement_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = agreement_contrast_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = survey_writing_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = dialogue_opinion_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_intonation_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_rhythm_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True