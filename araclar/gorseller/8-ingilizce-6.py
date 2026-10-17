def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'


def _kart(x, y, w, h, baslik, satirlar, bg, border, text_c):
    rx = 12
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}" stroke="{border}" stroke-width="2"/>'
    s += f'<text x="{x + w/2}" y="{y + 26}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{text_c}" text-anchor="middle">{baslik}</text>'
    s += f'<line x1="{x+12}" y1="{y+36}" x2="{x+w-12}" y2="{y+36}" stroke="{border}" stroke-width="1" stroke-dasharray="3,3"/>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x + w/2}" y="{y + 58 + i*22}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="middle">{st}</text>'
    return s


def gorsel_1():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">EXPRESSING LIKES AND DISLIKES (SEVİLEN &amp; SEVİLMEYENLER)</text>'
    ic += _kart(30, 56, 300, 160, "Likes (+ Verb-ing / Noun)", ["• I love / like / enjoy going to concerts.", "• I am fond of / keen on camping.", "• I am crazy about / interested in rock music.", "• He is good at playing the guitar."], "#dcfce7", "#10b981", "#047857")
    ic += _kart(350, 56, 300, 160, "Dislikes (+ Verb-ing / Noun)", ["• I dislike / hate shopping with my parents.", "• I can’t stand listening to loud music.", "• I am not interested in / not keen on opera.", "• She doesn’t like wearing formal clothes."], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">EXPRESSING PREFERENCES (PREFER &amp; WOULD RATHER)</text>'
    ic += _kart(30, 56, 195, 160, "Prefer + Noun", ["prefer + Noun + to + Noun", "I prefer rap to pop music.", "She prefers tea to coffee.", "‘to’ edatı ‘-e tercih etmek’"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Prefer + Verb-ing", ["prefer + V-ing + to + V-ing", "I prefer reading the news", "online to buying papers.", "Fiillere -ing takısı eklenir"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(454, 56, 195, 160, "Would Rather + V1", ["would rather + V1 + than + V1", "I’d rather stay at home", "than go out tonight.", "Yalın fiil (V1) kullanılır!"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">STATING PERSONAL OPINIONS &amp; TEEN LIFE ADJECTIVES</text>'
    ic += _kart(30, 56, 195, 160, "Opinion Phrases", ["I think / In my opinion...", "To be honest / Frankly...", "To me / According to me...", "I believe that..."], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Positive Adjectives (+)", ["Terrific / Awesome (Harika)", "Impressive (Etkileyici)", "Trendy / Stylish (Moda/Şık)", "Energetic / Harmonic / Fun"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Negative Adjectives (-)", ["Unbearable (Katlanılmaz)", "Ridiculous (Gülünç/Saçma)", "Boring / Dull (Sıkıcı)", "Snob (Burnu havada/Züppe)"], "#ffedd5", "#f97316", "#c2410c")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">FREQUENCY ADVERBS &amp; MAKING SIMPLE INQUIRIES</text>'
    ic += _kart(30, 56, 300, 160, "Adverbs of Frequency", ["• Always (100%) - Usually (80%) - Often (60%)", "• Sometimes (40%) - Rarely / Seldom (10%)", "• Never (0% - Olumlu cümlede olumsuz anlam!)", "• Once a day / Twice a week / Three times a month"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(350, 56, 300, 160, "Simple Inquiries (Sorular)", ["• What do you do in the evenings?", "• How often do you go to the theater?", "• What kind / type of music do you like?", "• Who is your favorite singer?"], "#f1f5f9", "#64748b", "#334155")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    bolumler = v.get("bolumler", [])
    eslesme = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    for idx, key in eslesme:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[key]
