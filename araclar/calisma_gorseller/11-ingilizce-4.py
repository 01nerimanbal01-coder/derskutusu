"""11. sınıf İngilizce 4. hafta (Preferences and Abilities) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def preference_structures_cards():
    kartlar = [
        ("1. Prefer", "V-ing + TO + V-ing", MAVI, MAVI_A),
        ("2. Would Rather", "V1 + THAN + V1", TUR, TUR_A),
        ("3. Would Prefer", "to V1 + RATHER THAN + V1", YES, YES_A),
        ("4. Past Ability", "could vs was able to", MOR, MOR_A),
    ]
    ic = ""
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, "#ffffff")
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Grammatical preference structures cards.", 34)


def would_rather_diagram():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "WOULD RATHER: SPECIFIC CHOICE FORMULA", 10.0, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Preferred Option", 9.2, TUR)
    ic += yazi(92, 76, "Subject + would rather", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "+ Bare Verb 1 (cook)", 8.4, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Alternative Option", 9.2, YESIL_K)
    ic += yazi(267, 76, "+ THAN + Bare Verb 1", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "than eat cold fast food", 8.4, YES, ince=True)
    return svg(360, 125, ic, "Would rather grammatical formula diagram.", 34)


def past_ability_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "PAST ABILITY: COULD VS WAS / WERE ABLE TO", 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, "#ffffff", MAVI)
    ic += yazi(92, 56, "COULD (General)", 9.2, MAVI)
    ic += yazi(92, 76, "Past general ability", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "I could swim when I was 5", 8.2, MAVI, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "WAS ABLE TO (Specific)", 9.2, YESIL_K)
    ic += yazi(267, 76, "Overcoming a challenge", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "We managed to escape fire", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Could vs was able to comparative diagram.", 34)


def prefer_structure_flow():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "PREFER PATTERNS: GENERAL ROUTINE PREFERENCES", 9.8, YESIL_K)
    steps = [
        ("Subject", "I / You / She", 16),
        ("Verb: prefer", "habitual action", 102),
        ("Gerund 1", "studying (V-ing)", 188),
        ("Preposition: to", "to working (V-ing)", 274),
    ]
    for b, a, x in steps:
        ic += kutu(x, 36, 70, 70, "#ffffff", YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Prefer sentence formation flowchart.", 34)


def preference_matrix_table():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "PREFERENCE STRUCTURES AND CONJUNCTIONS MATRIX", 9.8, MOR)
    satirlar = [
        ("Structure", "Verb Form", "Connector", "Context", MOR),
        ("prefer", "Gerund (V-ing)", "TO", "General Routine", MAVI),
        ("would rather", "Base Verb (V1)", "THAN", "Specific Moment", TUR),
        ("would prefer", "Infinitive (to V1)", "RATHER THAN", "Specific Choice", YESIL_K),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(55, y + 13, k1, 8.0, r)
        ic += yazi(130, y + 13, k2, 7.8, LAC, ince=(i > 0))
        ic += yazi(210, y + 13, k3, 8.0, LAC, ince=(i > 0))
        ic += yazi(295, y + 13, k4, 7.8, LAC, ince=(i > 0))
    return svg(360, 125, ic, "Preference conjunctions matrix table.", 34)


def ability_timeline_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, "MODAL TIMELINE: ABILITY ACROSS TIME", 10.0, CAM)
    ic += kutu(20, 36, 145, 70, "#ffffff", CAM)
    ic += yazi(92, 56, "Present Ability", 9.2, CAM)
    ic += yazi(92, 76, "can / am able to", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "I can speak German", 8.2, CAM, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(267, 56, "Past Ability", 9.2, TUR)
    ic += yazi(267, 76, "could (general)", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "was able to (specific)", 8.2, TUR, ince=True)
    return svg(360, 125, ic, "Present vs past ability timeline diagram.", 34)


def would_prefer_cards():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "WOULD PREFER: CLAUSE COMPONENTS", 10.0, TUR)
    kartlar = [
        ("1. Subject", "We / They / He", 16),
        ("2. Verb Form", "would prefer to V1", 102),
        ("3. Connector", "rather than", 188),
        ("4. Base Verb", "drive in traffic", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Would prefer clause components cards.", 34)


def grammar_rule_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, "KEY GRAMMAR CHECKPOINTS", 10.0, YESIL_K)
    kutular = ["prefer ... to", "would rather", "than ... V1", "was able to"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", YESIL_K, r=4)
        ic += yazi(x + 37, 66, f"Rule {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.0, YESIL_K)
    return svg(360, 125, ic, "Grammar checkpoints overview boxes.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = preference_structures_cards()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = would_rather_diagram()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = past_ability_kesiti()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = prefer_structure_flow()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = preference_matrix_table()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = ability_timeline_kesiti()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = would_prefer_cards()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = grammar_rule_kutulari()
    s[10]["en_fazla"] = 34
