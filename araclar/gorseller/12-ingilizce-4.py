# -*- coding: utf-8 -*-
"""12. Sınıf İngilizce — 4. Hafta görsel modülü: Theme 2 Friendship (Invitations, Accepting/Refusing, Apologizing)."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">MAKING INVITATIONS &amp; SUGGESTIONS (DAVET VE ÖNERİ KALIPLARI)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Structures Followed by V₁ / To + V₁", [
        "• Would you like to + V₁ ...?",
        "  (Would you like to join our study group?)",
        "• Do you want to + V₁ ...?",
        "• Why don't we / you + V₁ ...?",
        "• Shall we + V₁ ...? / Let's + V₁ ...",
        "• How about + Noun? (How about a movie tonight?)"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Structures Followed by V-ing (Gerund)", [
        "• How about / What about + V-ing ...?",
        "  (What about going to the book fair on Saturday?)",
        "• Do you fancy + V-ing ...?",
        "  (Do you fancy having coffee after school?)",
        "• Would you mind + V-ing ...?",
        "• Are you free on Sunday afternoon?"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">ACCEPTING AND REFUSING INVITATIONS (KABUL VE RED İFADELERİ)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Accepting an Invitation (Kabul Etme)", [
        "• Sure, I'd love to! / Yes, with pleasure!",
        "• That sounds great / awesome / wonderful!",
        "• Why not? Count me in! (Beni de say!)",
        "• I wouldn't miss it for the world! (Asla kaçırmam)",
        "• Sure! What time shall we meet?",
        "• That's a brilliant idea! I'll be there."
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Refusing Politely &amp; Giving Reasons (Reddetme)", [
        "• I'd love to, but I have another commitment.",
        "• I'm afraid I can't make it. (Korkarım gelemem.)",
        "• Thanks for inviting me, but I must study for my exam.",
        "• Sorry, I have other plans for tonight.",
        "• Maybe another time / Can I take a rain check?",
        "  (Take a rain check = Başka sefere ertelemek)"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">APOLOGIZING &amp; GIVING EXPLANATIONS (ÖZÜR VE AÇIKLAMA)</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Apologizing (Özür Dileme)", [
        "• I sincerely apologize for...",
        "• Please forgive me for + V-ing",
        "• It was entirely my fault.",
        "• I didn't mean to hurt you.",
        "• I owe you an apology.",
        "• Sorry for keeping you waiting."
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Giving Explanations", [
        "• The reason is that...",
        "• Because / Since / As + Clause",
        "• Due to / Because of + Noun",
        "• I completely forgot about it.",
        "• My alarm didn't go off.",
        "• I got stuck in heavy traffic."
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "Accepting Apologies", [
        "• Never mind. / No problem.",
        "• Don't worry about it.",
        "• That's quite all right.",
        "• Forget about it.",
        "• It doesn't matter at all.",
        "• No harm done! (Sorun yok)"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">EXPRESSING OPINIONS ON FRIENDSHIP &amp; PROVERBS</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Expressing Personal Opinions", [
        "• In my opinion / To my mind / From my point of view...",
        "• As far as I'm concerned, honesty is the pillar of",
        "  a lifelong friendship.",
        "• I strongly believe that true friends never judge.",
        "• It seems to me that mutual respect comes first.",
        "• Personally, I think actions speak louder than words."
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Proverbs &amp; Collocations on Friendship", [
        "• A friend in need is a friend indeed. (Kara gün dostu)",
        "• Birds of a feather flock together. (Bana arkadaşını söyle)",
        "• Make up with someone: Birisiyle barışmak",
        "• Fall out with someone: Birisiyle küsmek / bozuşmak",
        "• Keep in touch / Stay in touch: İletişimi koparmamak",
        "• Drift apart: Zamanla birbirinden uzaklaşmak"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]
