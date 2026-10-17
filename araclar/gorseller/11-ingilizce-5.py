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
        'PAST HABITS AND STATES: USED TO VS. WOULD</text>'
    )
    ic += _kart(20, 44, 310, 190, "USED TO + V1 (ACTIONS &amp; STATES)", [
        "• Geçmişte yapılan ama artık yapılmayan alışkanlıklar",
        "  (past habits) ve geçmişteki durumlar (past states).",
        "• Olumlu: S + used to + V1",
        "  Ex: I used to play chess every weekend.",
        "  Ex: She used to have long hair / live in Izmir.",
        "• Olumsuz: S + didn't use to + V1",
        "• Soru: Did + S + use to + V1?"
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "WOULD + V1 (REPEATED PAST ACTIONS ONLY)", [
        "• Geçmişte tekrarlanan eylemleri (nostaljik anıları)",
        "  anlatmak için kullanılır.",
        "• Ex: Every summer, we would swim in the lake.",
        "• DİKKAT: Durum fiilleriyle (be, have, live, know,",
        "  belong, love) ASLA 'would' kullanılmaz!",
        "• Yanlış: We would live in a small village.",
        "• Doğru: We used to live in a small village."
    ], "#9333EA", "#FAF5FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'USED TO / BE USED TO / GET USED TO KARŞILAŞTIRMASI</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. USED TO + V1", [
        "• Anlam: Eskiden yapardı",
        "  (Geçmiş alışkanlık).",
        "• Ardından yalın fiil (V1) gelir.",
        "• Ex: He used to wake up",
        "  late when he was a student.",
        "• Şimdi artık erken kalkıyor",
        "  anlamı taşır."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(237, 44, 205, 190, "2. BE USED TO + V-ING / NOUN", [
        "• Anlam: ...-ya alışkın olmak",
        "  (Mevcut alışkanlık durumu).",
        "• Ardından İSİM veya V-ing gelir!",
        "• Ex: He is used to waking",
        "  up early now.",
        "• Ex: I am used to spicy food.",
        "• (am/is/are/was/were used to)"
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "3. GET USED TO + V-ING / NOUN", [
        "• Anlam: ...-ya alışmak",
        "  (Alışma süreci / değişim).",
        "• Ardından İSİM veya V-ing gelir!",
        "• Ex: She is getting used to",
        "  living in a big city.",
        "• Ex: You will soon get used",
        "  to the cold weather."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'EXPRESSING ABILITY AND TALENTS IN THE PAST (COULD vs. WAS/WERE ABLE TO)</text>'
    )
    ic += _kart(20, 44, 310, 190, "COULD (GENERAL ABILITY IN THE PAST)", [
        "• Geçmişteki genel yetenek ve becerileri ifade eder.",
        "• Ex: Mozart could compose music at the age of five.",
        "• Ex: My grandfather could speak three languages.",
        "• Algı fiilleriyle (see, hear, smell, taste, understand)",
        "  tek seferlik durumlarda da 'could' kullanılır.",
        "• Olumsuz: couldn't (Hem genel hem tek seferlik",
        "  başarısızlıklarda rahatlıkla kullanılır)."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "WAS/WERE ABLE TO (SPECIFIC ACHIEVEMENT)", [
        "• Geçmişte zor bir durumda TEK SEFERLİK bir engeli",
        "  aşarak başarma ('managed to' / 'succeeded in').",
        "• Ex: The exam was very hard, but she was able to",
        "  pass it with a high score. ('could pass' denmez!)",
        "• Ex: Despite the heavy storm, the pilot was able to",
        "  land the plane safely.",
        "• Eş anlamlı: managed to + V1 / succeeded in + V-ing."
    ], "#E11D48", "#FFF1F2")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'THEME 2 VOCABULARY: HOBBIES, SKILLS &amp; INSPIRING SUCCESS STORIES</text>'
    )
    kelimeler = [
        ("HOBBIES &amp; CRAFTS", "archery (okçuluk), pottery (çömlekçilik), calligraphy (hat), origami, scuba diving, mountaineering.", "#2563EB", "#EFF6FF"),
        ("GIFTS &amp; TALENTS", "gifted / talented (yetenekli), prodigy (dahi çocuk), innate ability (doğuştan yetenek), master a skill.", "#059669", "#ECFDF5"),
        ("OVERCOMING OBSTACLES", "perseverance (azim), determination (kararlılık), overcome difficulties (zorlukları aşmak), pursue a dream.", "#D97706", "#FEF3C7"),
        ("PHRASAL VERBS", "take up (yeni bir hobiye başlamak), give up (bırakmak/vazgeçmek),keen on / fond of (meraklı/düşkün olmak).", "#9333EA", "#FAF5FF")
    ]
    for i, (b, m, r, bg) in enumerate(kelimeler):
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
