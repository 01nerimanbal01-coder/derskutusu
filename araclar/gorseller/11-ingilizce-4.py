def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'EXPRESSING LIKES, DISLIKES &amp; INTERESTS (+ GERUND / V-ING)</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Likes &amp; Strong Interests (+ Noun / V-ing)",
        [
            "• be keen on / be fond of / be into + V-ing:",
            "  'She is keen on playing chess and coding.'",
            "• be crazy about / be passionate about + V-ing:",
            "  'He is crazy about taking nature photos.'",
            "• enjoy / love / like / fancy + V-ing:",
            "  'I really enjoy doing archery at weekends.'",
            "• be gifted in / be good at + V-ing.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Dislikes &amp; Lack of Interest (+ Noun / V-ing)",
        [
            "• can't stand / can't bear + V-ing (Tahammül edememek):",
            "  'I can\'t stand waiting in long queues.'",
            "• dislike / hate / detest + V-ing:",
            "  'They dislike doing extreme sports.'",
            "• be tired of / be fed up with / be sick of + V-ing:",
            "  'He is fed up with playing video games all day.'",
            "• '...is not my cup of tea' (Bana göre değil).",
        ],
        "#dc2626", "#fef2f2"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'STATING PREFERENCES: PREFER vs. WOULD RATHER vs. WOULD PREFER</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. PREFER (General Preference)",
        [
            "• prefer + Noun + TO + Noun:",
            "  'I prefer tea to coffee.'",
            "• prefer + V-ing + TO + V-ing:",
            "  'She prefers reading to watching'",
            "• prefer + to V1 + RATHER THAN",
            "  + V1:",
            "  'I prefer to walk rather than run'",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. WOULD RATHER (Specific)",
        [
            "• would rather ('d rather) + V1",
            "  + THAN + V1 (Yalın fiil!):",
            "  'I\'d rather stay home than go'",
            "• Negative: would rather NOT + V1",
            "  'I\'d rather not join the club.'",
            "• Question: Would you rather",
            "  play tennis or swim?",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. WOULD PREFER (Specific)",
        [
            "• would prefer ('d prefer) + TO V1",
            "  + RATHER THAN + V1:",
            "  'I\'d prefer to paint rather than",
            "  knit.'",
            "• Negative: would prefer NOT",
            "  TO + V1:",
            "  'She\'d prefer not to travel.'",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'EXPRESSING ABILITY: CAN vs. COULD vs. BE ABLE TO</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Present &amp; General Past Ability (Can / Could)",
        [
            "• CAN / BE ABLE TO (Present Ability - Şimdiki Yetenek):",
            "  'I can / am able to speak three languages.'",
            "• COULD (General Past Ability - Geçmişteki Genel Yetenek):",
            "  'Mozart could compose music when he was five.'",
            "• COULDN'T (Both General &amp; Specific Past Inability):",
            "  'I couldn\'t ride a bike when I was four.'",
            "  'We couldn\'t win the match yesterday.'",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Specific Past Achievement: WAS/WERE ABLE TO!",
        [
            "• Geçmişte tek seferlik zor bir durumu başarma",
            "  (managed to / succeeded in) anlamında OLUMLU",
            "  cümlede 'could' DEĞİL, 'was/were able to' kullanılır!",
            "• Örnek: 'The exam was very hard, but I was able to",
            "  (managed to) pass it!' (NOT: could pass).",
            "• Diğer zamanlarda (will be able to, have been",
            "  able to) yalnızca 'be able to' kullanılır.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'THEME 2 VOCABULARY: HOBBIES, CRAFTS, SPORTS &amp; TALENTS</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Arts, Crafts &amp; Indoor Hobbies",
        [
            "• Calligraphy (Hat sanatı) &amp; Marbling / Ebru",
            "• Pottery / Ceramics (Çömlekçilik / Seramik)",
            "• Knitting (Örgü) &amp; Origami (Kâğıt katlama)",
            "• Woodcarving (Ahşap oymacılığı) &amp; Sculpture",
            "• Playing an instrument / Composing music",
            "• Photography &amp; Digital illustration",
        ],
        "#7c3aed", "#f5f3ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Outdoor Hobbies, Sports &amp; Skills",
        [
            "• Archery (Okçuluk) &amp; Fencing (Eskrim)",
            "• Mountaineering / Rock climbing (Dağcılık)",
            "• Scuba diving (Tüplü dalış) &amp; Paragliding",
            "• Trekking / Hiking (Doğa yürüyüşü) &amp; Camping",
            "• Key Adjectives: Gifted / Talented (Yetenekli),",
            "  Ambitious (Hırslı), Creative (Yaratıcı), Skilled.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]