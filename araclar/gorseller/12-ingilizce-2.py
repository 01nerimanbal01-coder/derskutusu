# -*- coding: utf-8 -*-
"""12. Sınıf İngilizce — 2. Hafta (Theme 1: Music - Part 2) SVG Görselleri"""

RENK = {
    "kirmizi": "#e63946",
    "mavi": "#2563eb",
    "yesil": "#16a34a",
    "turuncu": "#ea580c",
    "mor": "#7c3aed",
    "lacivert": "#1e293b",
    "acik_mavi": "#eff6ff",
    "acik_yesil": "#f0fdf4",
    "acik_turuncu": "#fff7ed",
    "acik_mor": "#f5f3ff",
    "acik_kirmizi": "#fef2f2",
    "gri": "#64748b",
    "acik_gri": "#f8fafc",
    "cizgi": "#cbd5e1",
    "beyaz": "#ffffff",
}


def _baslik(W, H, etiket, baslik_metni, renk):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px; font-family:\'Inter\', \'Segoe UI\', sans-serif;">'
        f'<rect width="{W}" height="{H}" rx="14" fill="{RENK["acik_gri"]}" stroke="{RENK["cizgi"]}" stroke-width="1.5"/>'
        f'<rect x="16" y="14" width="110" height="24" rx="6" fill="{renk}"/>'
        f'<text x="71" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{etiket}</text>'
        f'<text x="138" y="31" font-size="15" font-weight="700" fill="{RENK["lacivert"]}">{baslik_metni}</text>'
        f'<line x1="16" y1="48" x2="{W-16}" y2="48" stroke="{RENK["cizgi"]}" stroke-width="1"/>'
    )


def gorsel_1():
    """Music Through the Decades (1940s - 2000s) & Forum Comments"""
    W, H = 720, 320
    s = _baslik(W, H, "DECADES", "Music Through the Decades (40s – 2000s) & Inferring Ideas", RENK["mor"])
    decades = [
        ("1940s & 50s", "Jazz, Swing & Rock 'n' Roll", "Big bands, vinyl records", "Lively, nostalgic & rhythmic", RENK["turuncu"], RENK["acik_turuncu"]),
        ("1980s", "Pop, Synth-Pop & Glam Rock", "Cassettes, synthesizers", "Energetic, flashy & danceable", RENK["mavi"], RENK["acik_mavi"]),
        ("1990s", "Grunge, Hip-Hop & Teen Pop", "CDs, Walkman, music TV", "Emotional, rebellious & catchy", RENK["yesil"], RENK["acik_yesil"]),
        ("2000s & Today", "R&B, EDM & Indie Streaming", "MP3 players & smartphones", "Digital, global & diverse", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (dec, genre, media, mood, rk, ark) in enumerate(decades):
        x = 20 + i * 172
        y = 64
        s += f'<rect x="{x}" y="{y}" width="160" height="175" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="160" height="32" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+80}" y="{y+21}" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{dec}</text>'
        s += f'<text x="{x+80}" y="{y+56}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">{genre}</text>'
        s += f'<line x1="{x+14}" y1="{y+68}" x2="{x+146}" y2="{y+68}" stroke="{rk}" stroke-opacity="0.3"/>'
        s += f'<text x="{x+80}" y="{y+90}" text-anchor="middle" font-size="10.5" fill="{RENK["gri"]}">Media:</text>'
        s += f'<text x="{x+80}" y="{y+106}" text-anchor="middle" font-size="11" font-weight="600" fill="{RENK["lacivert"]}">{media}</text>'
        s += f'<text x="{x+80}" y="{y+134}" text-anchor="middle" font-size="10.5" fill="{RENK["gri"]}">Vibe / Tone:</text>'
        s += f'<text x="{x+80}" y="{y+150}" text-anchor="middle" font-size="11" font-weight="600" fill="{rk}">{mood}</text>'

    s += f'<rect x="20" y="252" width="680" height="52" rx="8" fill="#fff" stroke="{RENK["mor"]}" stroke-width="1.5"/>'
    s += f'<text x="36" y="273" font-size="12" font-weight="700" fill="{RENK["mor"]}">Reading Tip — Inferring Ideas from Forum Comments:</text>'
    s += f'<text x="36" y="292" font-size="11.5" fill="{RENK["lacivert"]}">Look for tone words (e.g., "golden era", "nothing beats...", "repetitive", "timeless") to infer whether a commenter prefers oldies or modern hits.</text>'
    s += "</svg>"
    return s


def gorsel_2():
    """Agreeing & Disagreeing Expressions"""
    W, H = 720, 340
    s = _baslik(W, H, "SPEAKING", "Expressing Agreement, Partial Agreement & Disagreement", RENK["mavi"])
    cols = [
        ("Strong Agreement (+)", RENK["yesil"], RENK["acik_yesil"], [
            "• I couldn't agree more.",
            "• No doubt about it.",
            "• You're absolutely right.",
            "• That's 100% true.",
            "• I totally / completely agree.",
            "• Exactly! / Definitely!",
        ]),
        ("Partial Agreement (+/-)", RENK["turuncu"], RENK["acik_turuncu"], [
            "• You have a point there, but...",
            "• I agree up to a point, however...",
            "• I agree to an extent.",
            "• That may be true, yet...",
            "• I see what you mean, but...",
            "• Well, it depends on...",
        ]),
        ("Disagreement (-)", RENK["kirmizi"], RENK["acik_kirmizi"], [
            "• I'm afraid I disagree.",
            "• I totally / completely disagree.",
            "• That's not always true.",
            "• I don't think so.",
            "• I'd say the exact opposite.",
            "• Not necessarily!",
        ]),
    ]
    for i, (title, rk, ark, items) in enumerate(cols):
        x = 20 + i * 230
        y = 62
        s += f'<rect x="{x}" y="{y}" width="218" height="258" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="218" height="34" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+109}" y="{y+22}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">{title}</text>'
        for j, it in enumerate(items):
            s += f'<text x="{x+14}" y="{y+62 + j*32}" font-size="11.5" font-weight="600" fill="{RENK["lacivert"]}">{it}</text>'
    s += "</svg>"
    return s


def gorsel_3():
    """Analyzing Music Festival Advertisements & Posters"""
    W, H = 720, 320
    s = _baslik(W, H, "LISTENING", "Analyzing Music Festival Ads & Announcements", RENK["turuncu"])
    s += f'<rect x="24" y="64" width="310" height="236" rx="12" fill="{RENK["lacivert"]}" stroke="{RENK["turuncu"]}" stroke-width="2"/>'
    s += f'<text x="179" y="95" text-anchor="middle" font-size="16" font-weight="800" fill="#facc15">SUMMER SOUND FEST</text>'
    s += f'<text x="179" y="116" text-anchor="middle" font-size="11.5" fill="#cbd5e1">Live Jazz • Indie • Rock • Acoustic</text>'
    s += f'<line x1="48" y1="128" x2="310" y2="128" stroke="#475569"/>'
    poster_rows = [
        ("VENUE:", "City Park Open-Air Arena"),
        ("DATES:", "July 18 – 20 (Fri–Sun)"),
        ("TIMES:", "Gates open 16:00 | Concerts 18:00–23:30"),
        ("TICKETS:", "$25/day | $60 Full Pass (Students 20% off)"),
    ]
    for i, (k, v) in enumerate(poster_rows):
        yy = 152 + i * 36
        s += f'<text x="44" y="{yy}" font-size="11.5" font-weight="700" fill="#38bdf8">{k}</text>'
        s += f'<text x="110" y="{yy}" font-size="11" fill="#fff">{v}</text>'

    s += f'<rect x="356" y="64" width="340" height="236" rx="12" fill="#fff" stroke="{RENK["cizgi"]}" stroke-width="1.5"/>'
    s += f'<text x="376" y="92" font-size="13.5" font-weight="700" fill="{RENK["turuncu"]}">4 Key Questions When Scanning an Ad</text>'
    q_list = [
        ("1. Where is the event? (Venue)", "Look for halls, stadiums, parks, arenas."),
        ("2. When does it take place? (Dates)", "Check day/month range and weekend dates."),
        ("3. What time does it start/end? (Times)", "Distinguish gate opening vs. main stage time."),
        ("4. How much / Who is it for? (Tickets)", "Look for daily vs. full pass & discounts."),
    ]
    for i, (q, ans) in enumerate(q_list):
        yy = 122 + i * 44
        s += f'<text x="376" y="{yy}" font-size="12" font-weight="700" fill="{RENK["lacivert"]}">{q}</text>'
        s += f'<text x="376" y="{yy+17}" font-size="11" fill="{RENK["gri"]}">{ans}</text>'
    s += "</svg>"
    return s


def gorsel_4():
    """Quantifiers for Interpreting Survey Charts"""
    W, H = 720, 340
    s = _baslik(W, H, "QUANTIFIERS", "Expressing Percentages & Proportions in Survey Charts", RENK["yesil"])
    bars = [
        ("78%", "The (vast) majority of / Nearly four-fifths of", 420, RENK["yesil"]),
        ("56%", "Over half of / More than half of", 300, RENK["mavi"]),
        ("24%", "About a quarter of / Almost a fourth of", 130, RENK["mor"]),
        ("11%", "A small fraction of / A minority of / A few of", 65, RENK["turuncu"]),
        ("0%", "None of the participants / No participants", 12, RENK["kirmizi"]),
    ]
    for i, (pct, phrase, bw, rk) in enumerate(bars):
        y = 66 + i * 52
        s += f'<rect x="24" y="{y}" width="64" height="36" rx="8" fill="{rk}"/>'
        s += f'<text x="56" y="{y+23}" text-anchor="middle" font-size="13" font-weight="800" fill="#fff">{pct}</text>'
        s += f'<rect x="100" y="{y+6}" width="440" height="24" rx="6" fill="#e2e8f0"/>'
        s += f'<rect x="100" y="{y+6}" width="{bw}" height="24" rx="6" fill="{rk}" fill-opacity="0.85"/>'
        s += f'<text x="112" y="{y+22}" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">{phrase}</text>'
        s += f'<text x="552" y="{y+23}" font-size="11" fill="{RENK["gri"]}">participants</text>'
    s += "</svg>"
    return s


def gorsel_5():
    """4-Part Structure of a Survey Report"""
    W, H = 720, 320
    s = _baslik(W, H, "WRITING", "How to Organize a 4-Part Music Survey Report", RENK["lacivert"])
    steps = [
        ("1. Introduction", "State what the chart/survey is about", "This bar chart illustrates the music preferences of 100 12th-grade students.", RENK["mavi"], RENK["acik_mavi"]),
        ("2. Key Finding", "Highlight the most important outcome", "Overall, the vast majority of teenagers prefer listening to pop and hip-hop.", RENK["yesil"], RENK["acik_yesil"]),
        ("3. Detailed Figures", "Give percentages & compare categories", "Over half of the students (55%) chose pop, whereas only a small fraction (8%) picked jazz.", RENK["turuncu"], RENK["acik_turuncu"]),
        ("4. Conclusion", "Summarize the bigger picture", "In conclusion, upbeat digital genres dominate youth music habits today.", RENK["mor"], RENK["acik_mor"]),
    ]
    for i, (st, desc, ex, rk, ark) in enumerate(steps):
        y = 62 + i * 60
        s += f'<rect x="24" y="{y}" width="672" height="50" rx="8" fill="{ark}" stroke="{rk}" stroke-width="1.5"/>'
        s += f'<rect x="24" y="{y}" width="150" height="50" rx="8" fill="{rk}"/>'
        s += f'<text x="99" y="{y+29}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">{st}</text>'
        s += f'<text x="188" y="{y+20}" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">{desc}</text>'
        s += f'<text x="188" y="{y+38}" font-size="11" font-style="italic" fill="{RENK["gri"]}">Example: "{ex}"</text>'
    s += "</svg>"
    return s


def gorsel_6():
    """Intonation Patterns in English (Rising, Falling, Combined)"""
    W, H = 720, 330
    s = _baslik(W, H, "PRONUNCIATION", "Four Intonation Patterns in English", RENK["kirmizi"])
    cards = [
        ("1. Rising Intonation (↗)", "Real Yes/No questions & uncertain question tags", "Do you play the guitar? ↗ | You like jazz, don't you? ↗", RENK["mavi"], RENK["acik_mavi"]),
        ("2. Falling Intonation (↘)", "WH-questions, statements, commands & exclamations", "What kind of music do you like? ↘ | Turn down the volume! ↘", RENK["yesil"], RENK["acik_yesil"]),
        ("3. Rising + Falling (↗ ↘)", "Alternatives (or), lists of items & conditionals", "Would you prefer pop ↗ or rock ↘? | Drums ↗, bass ↗, and guitar ↘.", RENK["turuncu"], RENK["acik_turuncu"]),
        ("4. Falling + Rising (↘ ↗)", "Polite invitations & tentative suggestions", "Why don't we go to the concert tonight ↘↗?", RENK["mor"], RENK["acik_mor"]),
    ]
    for i, (title, usage, ex, rk, ark) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = 22 + col * 344
        y = 64 + row * 124
        s += f'<rect x="{x}" y="{y}" width="332" height="110" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="{x+16}" y="{y+26}" font-size="13" font-weight="800" fill="{rk}">{title}</text>'
        s += f'<text x="{x+16}" y="{y+50}" font-size="11.5" font-weight="600" fill="{RENK["lacivert"]}">{usage}</text>'
        s += f'<rect x="{x+12}" y="{y+64}" width="308" height="34" rx="6" fill="#fff" stroke="{rk}" stroke-opacity="0.4"/>'
        s += f'<text x="{x+20}" y="{y+85}" font-size="10.8" font-weight="600" fill="{RENK["lacivert"]}">{ex}</text>'
    s += "</svg>"
    return s


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
    "b5": gorsel_5(),
    "b6": gorsel_6(),
}

