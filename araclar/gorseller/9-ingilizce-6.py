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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">THERE IS / THERE ARE (VAROLUŞ VE MEKÂN BETİMLEME)</text>'
    ic += _kart(30, 56, 195, 160, "There is (Singular / Unc.)", ["Tekil ve sayılamayanlarla:", "There is a smartboard.", "There isn’t any chalk.", "Is there a projector?"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "There are (Plural Nouns)", ["Çoğul isimlerle kullanılır:", "There are 24 desks in class.", "There aren’t any posters.", "Are there any lockers?"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "A / An / Some / Any", ["a / an: Tekil sayılabilir", "some: Olumlu cümlede (birkaç/biraz)", "any: Olumsuz (-) ve Soru (?)", "How many / How much...?"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">PREPOSITIONS OF PLACE (YER EDATLARI)</text>'
    ic += _kart(30, 56, 195, 160, "Temel Konumlar", ["in (içinde) - on (üstünde)", "under (altında)", "next to / beside (bitişiğinde)", "near (yakınında)"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Karşılıklı Konumlar", ["in front of (önünde)", "behind (arkasında)", "opposite (tam karşısında)", "between A and B (arasında)"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Üst / Alt &amp; Çevre", ["above / over (üzerinde - temassız)", "below (altında - seviye olarak)", "among (çok şeyin arasında)", "in the corner / in the middle"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">CLASSROOM OBJECTS &amp; SCHOOL FACILITIES</text>'
    ic += _kart(30, 56, 195, 160, "Classroom Objects", ["Smartboard / Interactive board", "Bulletin board (Duyuru panosu)", "Bookshelf / Bookcase (Kitaplık)", "Locker (Kilitli öğrenci dolabı)"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "School Facilities", ["Science lab / IT room", "Library / Study hall", "Gymnasium (Spor salonu)", "Canteen / Cafeteria / Auditorium"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Describing Adjectives", ["Spacious / Large (Geniş/Ferah)", "Well-equipped (Tam donanımlı)", "Bright / Airy (Aydınlık/Havadar)", "Tidy / Neat vs. Messy"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">POSSESSIVES &amp; ASKING ABOUT LOCATIONS</text>'
    ic += _kart(30, 56, 300, 160, "Possessive Adjectives vs. Pronouns", ["• my / your / his / her / our / their + NOUN", "  (This is my dictionary.)", "• mine / yours / his / hers / ours / theirs (İsimsiz!)", "  (This dictionary is mine. / Whose bag is this?)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(350, 56, 300, 160, "Asking About Places &amp; Directions", ["• Where is the science lab? -> It’s on the 2nd floor.", "• What is your classroom like? -> It’s bright and tidy.", "• Is there a library near the canteen? -> Yes, there is.", "• It’s at the end of the corridor, opposite Room 102."], "#e0e7ff", "#6366f1", "#4338ca")
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
