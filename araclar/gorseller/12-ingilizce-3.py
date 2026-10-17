def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 200, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "THEME 2: FRIENDSHIP — DESCRIBING PERSONAL QUALITIES", 14, "#1e3a8a", "bold")
    cols = [
        (25, "#f0fdf4", "#16a34a", "#166534", "Positive Qualities (Olumlu)", "• reliable / trustworthy (güvenilir)", "• generous (cömert) &amp; sincere (içten)", "• supportive &amp; understanding", "• humble / modest (alçakgönüllü)"),
        (362, "#fef2f2", "#ef4444", "#991b1b", "Negative Qualities (Olumsuz)", "• arrogant / conceited (kibirli)", "• stubborn / obstinate (inatçı)", "• jealous / envious (kıskanç)", "• stingy / mean (cimri) &amp; bad-tempered")
    ]
    for x, bg, st, tc, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 312, 146, bg, st, 10, 1.8)
        ic += _metin(x+156, 72, b, 12, tc, "bold")
        ic += _metin(x+156, 98, s1, 11, "#334155")
        ic += _metin(x+156, 122, s2, 11, "#334155")
        ic += _metin(x+156, 146, s3, 11, "#334155")
        ic += _metin(x+156, 170, s4, 11, "#334155")
    return _svg(700, 220, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "FRIENDSHIP IDIOMS &amp; PHRASAL VERBS", 14, "#92400e", "bold")
    items = [
        (25, "get on well with", "biriyle iyi geçinmek", "(have a good relationship)"),
        (192, "count on / rely on", "birine güvenmek,", "bel bağlamak"),
        (359, "through thick and thin", "iyi günde kötü günde,", "her koşulda"),
        (526, "see eye to eye", "aynı fikirde olmak,", "uzlaşmak")
    ]
    for x, b, s1, s2 in items:
        ic += _kutu(x, 48, 150, 138, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+75, 76, b, 12, "#b45309", "bold")
        ic += _metin(x+75, 110, s1, 11, "#334155")
        ic += _metin(x+75, 134, s2, 10, "#64748b")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 200, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "RELATIVE CLAUSES: DEFINING FRIEND &amp; PERSON QUALITIES", 14, "#6b21a8", "bold")
    rows = [
        (50, "who / that", "İnsanları niteler (Özne/Nesne)", "A true friend is someone who supports you in hard times."),
        (100, "whose", "İyelik / sahiplik bildirir (+ noun)", "I admire people whose actions match their words."),
        (150, "whom", "İnsanları niteler (Nesne / Edatla)", "She is the colleague with whom I share my projects.")
    ]
    for y, pr, tr, ex in rows:
        ic += _kutu(25, y, 120, 40, "#f3e8ff", "#9333ea", 8, 1.5)
        ic += _metin(85, y+25, pr, 12, "#581c87", "bold")
        ic += _kutu(155, y, 520, 40, "#ffffff", "#d8b4fe", 8, 1.2)
        ic += _metin(415, y+17, tr, 11, "#6b21a8", "bold")
        ic += _metin(415, y+33, ex, 10, "#334155")
    return _svg(700, 220, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "DESCRIBING APPEARANCE vs. PERSONALITY", 14, "#166534", "bold")
    ic += _kutu(28, 48, 310, 134, "#ffffff", "#22c55e", 10, 1.8)
    ic += _metin(183, 72, "What is he/she like? (Personality)", 12, "#15803d", "bold")
    ic += _metin(183, 98, "Karakter ve kişilik özelliklerini sorar:", 11, "#475569")
    ic += _metin(183, 122, "→ She is kind, outgoing and disciplined.", 11, "#1e293b", "bold")
    ic += _metin(183, 146, "→ He has a great sense of humor.", 11, "#334155")

    ic += _kutu(362, 48, 310, 134, "#ffffff", "#22c55e", 10, 1.8)
    ic += _metin(517, 72, "What does he/she look like? (Appearance)", 12, "#15803d", "bold")
    ic += _metin(517, 98, "Fiziksel dış görünüşü sorar:", 11, "#475569")
    ic += _metin(517, 122, "→ He is tall and well-built with curly hair.", 11, "#1e293b", "bold")
    ic += _metin(517, 146, "→ She is in her late twenties.", 11, "#334155")
    return _svg(700, 210, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]