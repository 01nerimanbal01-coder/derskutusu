def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Gifted People, Talents &amp; Past Achievements</text>'
        + _kart(25, 42, 300, 145, "Could vs. Was/Were Able To (Success)", [
            "• General Past Ability -> COULD / WAS ABLE TO",
            "  Mozart could play the piano at the age of four.",
            "• Specific Achievement (One-time hard situation)",
            "  -> WAS/WERE ABLE TO, MANAGED TO, SUCCEEDED IN",
            "  She was able to win the gold medal despite her injury."
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Vocabulary: Giftedness &amp; Perseverance", [
            "• gifted / talented / prodigy: üstün yetenekli / dâhi",
            "• overcome obstacles: engelleri aşmak",
            "• pursue a passion: tutkusunun peşinden gitmek",
            "• milestone / turning point: dönüm noktası",
            "• dedication &amp; determination: adanmışlık ve kararlılık"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'How to Write a Well-Structured Biography</text>'
        + _kart(18, 42, 205, 145, "1. Introduction &amp; Early Life", [
            "• Who the person is &amp; why famous",
            "• Date and place of birth:",
            "  was born on [Date] in [Place]",
            "• Childhood, family background,",
            "  and early signs of talent"
        ], "#d97706", "#fffbeb")
        + _kart(237, 42, 205, 145, "2. Education &amp; Career", [
            "• graduated from [University]",
            "• Turning points and struggles:",
            "  had to overcome hardships",
            "• Major works, inventions,",
            "  discoveries, and awards"
        ], "#7c3aed", "#f5f3ff")
        + _kart(456, 42, 205, 145, "3. Legacy &amp; Time Linkers", [
            "• Contribution to humanity",
            "• Passed away in [Year] /",
            "  continues to inspire people",
            "• Linkers: At the age of, Later,",
            "  Eventually, Throughout his life"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 202, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
}


def uygula(v):
    hedefler = [0, 1]
    anahtarlar = ["b1", "b2"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
