"""12. sınıf İngilizce 4. hafta (Suggestions & Preferences) çalışma kâğıdı görselleri."""

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

def dort_tercih_kalibi_karti():
    kartlar = [
        ('1. Prefer ... to', 'Noun / V-ing · Latin Root', MAVI, MAVI_A),
        ('2. Would Rather', 'Bare Verb (V1) · Than', YES, YES_A),
        ('3. How About?', 'Gerund (-ing) · Informal', TUR, TUR_A),
        ('4. Why Not?', 'Base Verb · Suggestion', MOR, MOR_A),
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
    return svg(360, 110, ic, "Four preference patterns card.", 34)

def would_rather_structure_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "WOULD RATHER GRAMMAR PATTERN", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Stay Home (V1)", 10.0, YES)
    ic += yazi(95, 74, "I would rather stay...", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, "Go Out (V1)", 10.0, TUR)
    ic += yazi(265, 74, "...THAN go to a concert", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Would rather grammar pattern panel.", 34)

def how_about_gerund_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "MAKING SUGGESTIONS: HOW ABOUT + V-ING", 10.5, YES)
    ic += yazi(180, 52, "“How about LISTENING to acoustic guitar tonight?”", 10.0, LAC)
    ic += yazi(180, 76, "Offering friendly options gently with gerund constructions", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "How about suggestion panel.", 34)

def preference_contrast_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "PREFERENCE COMPARISON STRUCTURES", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "Prefer ... TO ...", 10.0, MAVI)
    ic += yazi(92, 74, "I prefer jazz to rock", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Rather ... THAN ...", 10.0, YES)
    ic += yazi(267, 74, "Rather read than sleep", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Preference comparison structures diagram.", 34)

def weekend_dialogue_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "WEEKEND ACTIVITY DIALOGUE SEQUENCE", 10.5, MAVI)
    adimlar = ["1. Rock Plan?", "2. Too Loud", "3. Art Museum?", "4. Great Idea!"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 40, 70, a, 8.6, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Weekend activity dialogue sequence.", 34)

def friendship_virtues_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "ESSENTIAL VIRTUES OF TRUE FRIENDSHIP", 10.5, MOR)
    ic += yazi(180, 52, "Reliable · Honest · Empathetic · Supportive", 10.0, LAC)
    ic += yazi(180, 76, "Backing friends up and keeping promises under all conditions", 9.2, YES, ince=True)
    return svg(360, 110, ic, "Friendship virtues panel.", 34)

def dort_baglac_karti():
    kartlar = [
        ('1. Because', 'Direct Cause · Clause', MAVI, MAVI_A),
        ('2. Since', 'Known Reason · Context', YES, YES_A),
        ('3. As', 'Evident Reason', TUR, TUR_A),
        ('4. Therefore', 'Logical Consequence', MOR, MOR_A),
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
    return svg(360, 110, ic, "Four causal conjunctions card.", 34)

def sifre_friend_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "FRIENDSHIP TERMINOLOGY WORD PUZZLE", 10.8, TUR)
    ic += yazi(180, 50, "FESTIVAL · REASON · INSTRUMENT · EVENT · NOTE · DRUM", 9.2, LAC)
    ic += yazi(180, 76, "Solve the clues to uncover the core social value (6 letters).", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Password friend puzzle panel.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_tercih_kalibi_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = would_rather_structure_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = how_about_gerund_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = preference_contrast_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = weekend_dialogue_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = friendship_virtues_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_baglac_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_friend_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True