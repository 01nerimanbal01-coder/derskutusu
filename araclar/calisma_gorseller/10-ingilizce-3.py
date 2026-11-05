"""10. sınıf Ingilizce 3. hafta (Okul Hayatı, Günlük Rutinler, Ders Programı, Okul Kulüpleri ve Geniş Zaman (Simple Present Tense)) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Affirmative', 'Subject + Verb(s/es)', MAVI, MAVI_A),
        ('Negative', 'don\'t / doesn\'t + Verb', KIR, KIR_A),
        ('Question', 'Do / Does + Subject + Verb', YES, YES_A),
        ('Time Frequency', 'always, usually, often, never', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Simple Present Tense sentence structures rule card', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'WEEKLY SCHOOL TIMETABLE SCHEDULE', 11, MAVI)
    gunler = [
        ('Mon', '08:30 Maths', '10:15 Biology'),
        ('Tue', '08:30 English', '10:15 History'),
        ('Wed', '08:30 Physics', '10:15 Chemistry'),
        ('Thu', '08:30 Literature', '10:15 Geography'),
        ('Fri', '08:30 Art & Music', '10:15 Sports')
    ]
    for i, (g, d1, d2) in enumerate(gunler):
        x = 10 + i * 69
        ic += kutu(x, 34, 63, 54, '#ffffff', MAVI, 5, 1)
        ic += yazi(x + 31, 48, g, 9, MAVI)
        ic += yazi(x + 31, 62, d1, 7, LAC, ince=True)
        ic += yazi(x + 31, 76, d2, 7, SOLUK, ince=True)
    return svg(360, 100, ic, 'Weekly school timetable schedule with lesson times', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'ADVERBS OF FREQUENCY SCALE', 11, YES)
    oranlar = [
        ('Always', '100%', YES),
        ('Usually', '80%', '#2e7d32'),
        ('Often', '60%', MAVI),
        ('Sometimes', '40%', TUR),
        ('Rarely', '20%', MOR),
        ('Never', '0%', KIR)
    ]
    for i, (ad, yuzde, c) in enumerate(oranlar):
        x = 10 + i * 57
        ic += kutu(x, 34, 52, 54, '#ffffff', c, 5, 1)
        ic += yazi(x + 26, 52, ad, 8, c)
        ic += yazi(x + 26, 72, yuzde, 10, LAC)
    return svg(360, 100, ic, 'Adverbs of frequency percentage scale', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'EXTRACURRICULAR SCHOOL CLUBS', 11, TUR)
    kulupler = [
        ('Science Club', 'Conducting experiments in labs', MAVI),
        ('Drama Society', 'Rehearsing theatrical plays', TUR),
        ('Debate Club', 'Discussing global issues', YES),
        ('Eco Warriors', 'Recycling and tree planting', MOR)
    ]
    for i, (b, d, c) in enumerate(kulupler):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, c)
        ic += yazi(x + 40, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Extracurricular school clubs and activities card', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, '3RD PERSON SINGULAR VERB SPELLING RULES', 10.5, MOR)
    kurallar = [
        ('General (+s)', 'work -> works, play -> plays'),
        ('End in -ch,-sh,-ss (+es)', 'watch -> watches, wash -> washes'),
        ('End in -o (+es)', 'go -> goes, do -> does'),
        ('Consonant + y (-ies)', 'study -> studies, fly -> flies')
    ]
    for i, (b, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 7.5, MOR)
        ic += yazi(x + 40, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Present simple third person verb spelling rules', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'PREPOSITIONS OF TIME: AT - ON - IN', 11, LAC)
    edatlar = [
        ('AT (Precise Times)', 'at 08:30, at noon, at midnight', MAVI),
        ('ON (Days & Dates)', 'on Monday, on 28th September', TUR),
        ('IN (Months & Years)', 'in October, in 2026, in the morning', YES)
    ]
    for i, (b, d, c) in enumerate(edatlar):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 52, b, 9, c)
        ic += yazi(x + 52, 72, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Prepositions of time rules for at on in with examples', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    adlar = [
        ('Compulsory', 'Mandatory lessons required by curriculum'),
        ('Timetable', 'A weekly schedule showing lesson hours'),
        ('Facility', 'Physical rooms like labs and sports gym'),
        ('Routine', 'Habits performed regularly every day')
    ]
    for i, (b, d) in enumerate(adlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'School life and routine vocabulary terms card', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'KEY WORD PUZZLE STRIP: H - A - B - I - T', 11.5, YES)
    harfler = [('1', 'H'), ('2', 'A'), ('3', 'B'), ('4', 'I'), ('5', 'T')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'English vocabulary puzzle key word strip boxes', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
