def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563EB", bg="#EFF6FF"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'THEME 3: HUMAN RIGHTS — FUNDAMENTAL CONCEPTS &amp; MOTTOS</text>'
    )
    ic += _kart(20, 44, 310, 190, "CORE HUMAN RIGHTS VOCABULARY", [
        "• Universal Declaration of Human Rights (UDHR - 1948)",
        "• Dignity (İnsan onuru), Equality (Eşitlik), Justice (Adalet)",
        "• Freedom of speech / expression (İfade özgürlüğü)",
        "• Right to education, health care and shelter",
        "• Conscience (Vicdan), Tolerance (Hoşgörü), Empathy",
        "• Non-discrimination (Ayrımcılık yapmama ilkesi)",
        "• Innate and inalienable rights (Doğuştan ve devredilemez)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "INSPIRING HUMAN RIGHTS MOTTOS", [
        "• 'All human beings are born free and equal in",
        "  dignity and rights.' (UDHR, Article 1)",
        "• 'Injustice anywhere is a threat to justice",
        "  everywhere.' — Martin Luther King Jr.",
        "• 'No one is free until we are all free.'",
        "• 'Peace at home, peace in the world.' — M. K. Atatürk",
        "• 'Respect every human being regardless of race or gender.'"
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DISADVANTAGED GROUPS AND HUMAN RIGHTS VIOLATIONS</text>'
    )
    ic += _kart(20, 44, 310, 190, "DISADVANTAGED / VULNERABLE GROUPS", [
        "• The disabled / People with disabilities (Engelli bireyler)",
        "• Refugees and asylum seekers (Mülteciler ve sığınmacılar)",
        "• The elderly (Yaşlılar) &amp; Orphans (Yetim/Öksüz çocuklar)",
        "• The underprivileged / Impoverished (Yoksul kesimler)",
        "• AccessibilitySolutions: Wheelchair ramps, Braille",
        "  alphabet, tactile paving (hissedilebilir yüzey), sign",
        "  language (işaret dili), equal job opportunities."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "PROBLEMS &amp; VIOLATIONS TO PREVENT", [
        "• Discrimination (Ayrımcılık), Racism (Irkçılık)",
        "• Prejudice / Bias (Önyargı), Stereotype (Kalıp yargı)",
        "• Bullying &amp; Cyberbullying (Zorbalık ve Siber zorbalık)",
        "• Child labor (Çocuk işçiliği), Sweatshops",
        "• Domestic violence (Aile içi şiddet), Inequality",
        "• Deprivation of basic needs (Temel ihtiyaçlardan yoksunluk)."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'MAKING SUGGESTIONS AND GIVING ADVICE ON HUMAN RIGHTS</text>'
    )
    ic += _kart(20, 44, 310, 190, "GIVING ADVICE &amp; OBLIGATION (MODALS)", [
        "• should / ought to / had better + V1:",
        "  - Society should provide equal opportunities for all.",
        "  - We ought to respect everyone's privacy and beliefs.",
        "• must / have to / need to + V1:",
        "  - Governments must protect children from child labor.",
        "  - Public buildings need to be accessible for the disabled."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "EXPRESSING SUGGESTIONS &amp; PROPOSALS", [
        "• What about / How about + V-ing?",
        "  - How about organizing a charity campaign for refugees?",
        "• Why don't we / Let's + V1:",
        "  - Why don't we raise awareness about cyberbullying?",
        "• I suggest / recommend / propose (that) + S + (should) + V1:",
        "  - I suggest that municipalities build more ramps.",
        "• It is high time + S + V2: It's high time we ended racism."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ADJECTIVES AS PLURAL NOUNS (THE + ADJECTIVE) &amp; PASSIVE MODALS</text>'
    )
    adimlar = [
        ("THE + ADJECTIVE = PLURAL NOUN GROUP", "'the disabled' (engelliler), 'the elderly' (yaşlılar), 'the poor' (yoksullar), 'the blind' (görme engelliler) -> Çoğul fiil alır (are/have)!", "#2563EB", "#EFF6FF"),
        ("PASSIVE MODALS FOR SOLUTIONS", "should be + V3 / must be + V3: 'Human rights must be protected' (İnsan hakları korunmalıdır), 'Discrimination should be banned'.", "#059669", "#ECFDF5"),
        ("BOTH ... AND / NEITHER ... NOR / NOT ONLY ... BUT ALSO", "Paralel bağlaçlarla eşitlik vurgusu: 'Every child deserves both quality education and safe healthcare.'", "#7C3AED", "#F5F3FF"),
        ("COLLOCATIONS TO REMEMBER", "raise awareness (farkındalık yaratmak), violate rights (hak ihlali yapmak), stand up for (savunmak), donate to charity.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
